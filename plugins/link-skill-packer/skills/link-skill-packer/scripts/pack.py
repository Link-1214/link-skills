"""Pack a skill folder into a zip that installs cleanly on someone else's machine.

Two subcommands, and the split between them is the point.

    check  reports and writes nothing
    build  re-runs the same checks, refuses on any FAIL, then writes the zip

Every FAIL here is a failure that produces no error on the recipient's machine — the
skill simply never appears. WARN is everything a person has to judge, so it is reported
and never blocks. The script cannot enforce that the author was shown the manifest and
agreed to it; that half of the contract lives in SKILL.md as a stop.

Standard library only, so it runs wherever python does.

    python pack.py check  <skill-folder>
    python pack.py build  <skill-folder> --out <destination> [--author "name"] [--force]
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import re
import sys
import zipfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# Available from 3.10. Without it the import scan cannot tell stdlib from third party, and
# guessing would produce a requirements list nobody should trust — so it goes quiet instead.
STDLIB_NAMES = getattr(sys, "stdlib_module_names", None)

# What has to already exist on the recipient's machine to run a bundled script. .bat and .cmd
# are deliberately absent — cmd.exe ships with Windows, so naming it would be noise. Node is
# not in that category, and leaving it out let a skill bundling render-graphs.js ship with
# "nothing to install" written in its own INSTALL.md.
INTERPRETERS = {
    ".py": "python",
    ".ps1": "PowerShell",
    ".sh": "bash",
    ".js": "Node.js",
    ".ts": "Node.js",
}

FAIL = "FAIL"
WARN = "WARN"
NOTE = "NOTE"

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".venv", "node_modules", ".idea", ".vscode"}
SKIP_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".swp"}

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".ps1", ".sh", ".bat", ".cmd", ".json", ".yaml", ".yml",
    ".js", ".ts", ".css", ".html", ".toml", ".ini", ".cfg", ".xml", ".sql",
}
SCRIPT_SUFFIXES = {".py", ".ps1", ".sh", ".bat", ".cmd", ".js", ".ts"}

# Suffixes that make a backticked string look like a bundled file rather than prose.
LINKABLE_SUFFIXES = TEXT_SUFFIXES | {".png", ".jpg", ".jpeg", ".svg", ".gif", ".pdf", ".csv"}

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
BACKTICK = re.compile(r"`([^`\n]+)`")
PLACEHOLDER = re.compile(r"[<>{}$%*?|\"]")

# Every WARN carries the question the author has to answer. A warning that only states
# what was found gets read as noise and scrolled past; one that names the decision is the
# reason the run stops here at all.
ASK_PATH = ("Is this an example in prose, or a path the skill actually opens? "
            "It will not exist on the recipient's machine.")
ASK_CREDENTIAL = ("Is this a placeholder or a real credential? A real one leaves the "
                  "building inside the zip and cannot be called back.")

TEXT_PATTERNS = [
    (re.compile(r"\b[A-Za-z]:\\[^\s`\"'<>|]+"), "Windows absolute path", ASK_PATH),
    (re.compile(r"\\\\[A-Za-z0-9._-]+\\[^\s`\"'<>|]+"), "UNC network path",
     "Does this name an internal server? The path will not resolve elsewhere, and the "
     "name alone tells the recipient something about your network."),
    (re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/"), "home directory path", ASK_PATH),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key block", ASK_CREDENTIAL),
    (re.compile(
        r"\b(?:api[_-]?key|secret[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret)\b"
        r"\s*[:=]\s*\S", re.IGNORECASE), "credential assignment", ASK_CREDENTIAL),
    (re.compile(r"\bpassw(?:or)?d\b\s*[:=]\s*\S", re.IGNORECASE),
     "password assignment", ASK_CREDENTIAL),
    (re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{16,}"), "bearer token", ASK_CREDENTIAL),
    (re.compile(
        r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"),
     "private IP address",
     "Is this a real address on your network? It describes your internal layout to "
     "everyone who ends up with a copy."),
    # The domain is built from dot-separated labels rather than a run of [\w.-], so a
    # sentence's full stop does not get swallowed into the excerpt the author reads.
    (re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"), "email address",
     "Is this a real person's address? It travels with every copy of the zip."),
]

MAX_REPORTED_PER_KIND = 5
LARGE_BUNDLE_BYTES = 5 * 1024 * 1024

# What a skill folder normally holds. Everything matching this is unremarkable, and printing
# it back at the author buys nothing — a list of fourteen filenames gets skimmed, and the one
# that mattered goes past with the rest. What follows is used to show the few that stand out.
STANDOUT_BYTES = 1024 * 1024

DATA_SUFFIXES = {
    ".xlsx", ".xls", ".xlsm", ".csv", ".tsv", ".db", ".sqlite", ".sqlite3", ".mdb",
    ".zip", ".7z", ".rar", ".tar", ".gz", ".pdf", ".docx", ".doc", ".pptx", ".ppt",
    ".msg", ".eml", ".pst", ".bak",
}
DRAFT_TOKENS = {"draft", "temp", "tmp", "backup", "bak", "copy", "old", "wip",
                "scratch", "personal", "private", "secret", "untitled"}
DRAFT_HINTS_KO = ("초안", "임시", "백업", "사본", "개인", "메모", "비공개")


@dataclass(frozen=True)
class Finding:
    severity: str
    check: str
    message: str
    question: str = ""  # WARN only — what the author has to decide about this

    # FAIL blocks. WARN is a question whose answer changes what happens next — proceed, or
    # go fix the folder and run again. NOTE is neither: something the recipient should be
    # told, with nothing for the author to decide. Asking a question whose answer changes
    # nothing is how a stop turns back into a rubber stamp, so those live here instead.


@dataclass(frozen=True)
class Inspection:
    root: Path
    files: list[Path]
    findings: list[Finding]
    skill_name: str
    description: str
    interpreters: list[str] = field(default_factory=list)
    third_party: list[str] = field(default_factory=list)
    unparsed: list[Path] = field(default_factory=list)
    standout: list[tuple[Path, int, list[str]]] = field(default_factory=list)

    @property
    def failures(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == FAIL]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == WARN]

    @property
    def notes(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == NOTE]

    @property
    def total_bytes(self) -> int:
        return sum((self.root / f).stat().st_size for f in self.files)

    @property
    def scripts(self) -> list[Path]:
        return [f for f in self.files if f.suffix.lower() in SCRIPT_SUFFIXES]


def collect_files(root: Path) -> list[Path]:
    """Every file that will travel, as paths relative to the skill folder."""
    found = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if SKIP_DIRS.intersection(rel.parts):
            continue
        if path.name in SKIP_NAMES or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        found.append(rel)
    return found


def read_text(path: Path) -> str:
    """Read for scanning, with line endings normalised and any BOM removed.

    A skill authored on Windows has CRLF line endings, and a frontmatter regex anchored
    on '\\n' silently fails to match one — which would report a perfectly good skill as
    having no frontmatter at all.

    The BOM is reported separately as its own FAIL, and stripped here so it does not mask
    the rest. Left in place it breaks the frontmatter match, and the author fixes one
    problem only to discover two more on the next run.
    """
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    return raw.replace("\r\n", "\n").replace("\r", "\n")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "-")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def check_frontmatter(root: Path, findings: list[Finding]) -> str:
    """Returns the description. What FAILs here is what stops the skill loading at all.

    Only the description side blocks. Claude Code invokes a skill by its folder name — five
    skills installed on this machine carry a frontmatter name that differs from their folder
    and all five load and appear in the skill list. The mismatch is untidy, not fatal, so it
    is a question rather than a block.
    """
    skill_md = root / "SKILL.md"
    raw_bytes = skill_md.read_bytes()
    if raw_bytes.startswith(b"\xef\xbb\xbf"):
        findings.append(Finding(
            FAIL, "byte order mark",
            "SKILL.md starts with a UTF-8 BOM. Frontmatter parsing breaks on it and every "
            "field is dropped, so the skill loads with no metadata and never triggers. "
            "Save it as UTF-8 without BOM."))

    text = read_text(skill_md)
    fields = parse_frontmatter(text)
    if fields is None:
        findings.append(Finding(
            FAIL, "frontmatter",
            "SKILL.md has no frontmatter block. It must open with a '---' line, the fields, "
            "and a closing '---' line."))
        return ""

    name = fields.get("name", "")
    description = fields.get("description", "")

    # A note, not a question. Packing keeps the folder name unconditionally, so whatever the
    # author answers, the same zip comes out — and a question whose answer changes nothing is
    # the padding that teaches people to stop reading questions.
    if not name:
        findings.append(Finding(
            NOTE, "frontmatter name",
            f"'name' is missing, so the skill is invoked as '{root.name}', after the folder"))
    elif name != root.name:
        findings.append(Finding(
            NOTE, "frontmatter name",
            f"the file says '{name}' and the folder says '{root.name}' — the folder wins, and "
            f"packing keeps it, so the skill behaves exactly as it does here"))

    if not description:
        findings.append(Finding(
            FAIL, "frontmatter",
            "'description' is missing. It is the only thing a model reads when deciding "
            "whether to load the skill, so without it the skill never fires."))
    elif not description.startswith(('"', "'")) and ": " in description:
        findings.append(Finding(
            FAIL, "frontmatter",
            "the unquoted 'description' contains a colon followed by a space. YAML parses "
            "that as a mapping and discards the whole frontmatter, leaving the skill with no "
            "metadata. Use an em dash instead."))

    return description


def resolve_reference(source: Path, target: str, root: Path) -> tuple[str | None, Path | None]:
    """Classify one link or path found in a document.

    Returns (verdict, path relative to the skill folder). The verdict is 'absolute',
    'outside', 'missing', or None when the target is fine. The path comes back only for a
    target that resolved to a bundled file, so the caller can tell which files the skill
    actually reaches for.
    """
    target = target.split("#")[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "#", "~")):
        return None, None
    # A path a skill writes at runtime is spelled with a placeholder — `<output>/board.png`,
    # `{project}/notes.md`. Windows forbids < > " | ? * in filenames outright, and $ % mark
    # shell variables, so none of these can name a file that ships in the bundle. Treating
    # them as missing bundled files blocked two working skills in this very repository.
    if PLACEHOLDER.search(target):
        return None, None
    if target.startswith("/") or target.startswith("\\\\") or re.match(r"^[A-Za-z]:[\\/]", target):
        return "absolute", None
    if ".." in Path(target.replace("\\", "/")).parts:
        return "outside", None
    if target.endswith("/"):
        return None, None
    resolved = (source.parent / target.replace("\\", "/")).resolve()
    if not resolved.is_file():
        return "missing", None
    try:
        return None, resolved.relative_to(root)
    except ValueError:
        return None, None


def check_references(root: Path, files: list[Path], findings: list[Finding]) -> set[Path]:
    """A file the skill reaches for mid-run has to be in the zip, or the run dies there.

    Returns the bundled files something actually links to. Inverted, that set says which
    files nothing in the skill reaches for — the likeliest shape of a leftover.
    """
    referenced: set[Path] = set()
    for rel in files:
        if rel.suffix.lower() != ".md":
            continue
        source = root / rel
        text = read_text(source)

        candidates = [(m.group(1), True) for m in MD_LINK.finditer(text)]
        for match in BACKTICK.finditer(text):
            span = match.group(1).strip()
            # Only a backticked path with a directory component reads as a bundled file.
            # A bare 'INSTALL.md' in prose usually names an output, not a shipped file.
            if " " in span or "/" not in span:
                continue
            if Path(span).suffix.lower() in LINKABLE_SUFFIXES:
                candidates.append((span, False))

        unresolved: list[str] = []
        resolved_here = 0

        for target, is_link in candidates:
            verdict, hit = resolve_reference(source, target, root)
            if hit is not None:
                referenced.add(hit)
                resolved_here += 1
            if verdict is None:
                continue
            if verdict == "missing":
                if target not in unresolved:
                    unresolved.append(target)
                pass  # gathered per file below, so one document is one question
            elif verdict == "outside":
                findings.append(Finding(
                    WARN, "outside reference",
                    f"{rel} — '{target}'",
                    "Does the skill actually open this when it runs? It sits outside the "
                    "folder and will not be in the zip, so a step that depends on it breaks. "
                    "A link in prose is harmless."))
            elif verdict == "absolute" and is_link:
                findings.append(Finding(
                    WARN, "absolute reference",
                    f"{rel} — '{target}'", ASK_PATH))

        if unresolved:
            # One question per document, not per path. Blocking on these was already wrong;
            # asking fourteen times over is the other way to make a warning worthless.
            # A file where nothing resolves is almost always describing the user's project
            # rather than pointing at its own bundle, and that difference is worth saying
            # out loud — it changes the answer from a list into a yes or no.
            sample = ", ".join(unresolved[:3])
            if len(unresolved) > 3:
                sample += f", and {len(unresolved) - 3} more"
            detail = f"{rel} — {len(unresolved)} path(s) not in the bundle — {sample}"
            if resolved_here == 0:
                # Nothing in the document resolves, so the document is describing the user's
                # project rather than pointing at its own files. Across the 81 installed
                # skills this held 22 times out of 22 — the answer never once came back
                # "those should have shipped", which makes it a note and not a question.
                findings.append(Finding(NOTE, "outside paths", detail))
            else:
                # Mixed is the case worth asking about. Some paths in this same document do
                # resolve, so the author is pointing at bundled files here and these do not
                # land — which is what a typo looks like.
                findings.append(Finding(
                    WARN, "unresolved path", detail,
                    "Other paths in this same file resolve and these do not. Are they "
                    "examples and project paths like the rest, or files that should have "
                    "been in the bundle?"))

    return referenced


def classify_files(root: Path, files: list[Path],
                   referenced: set[Path]) -> list[tuple[Path, int, list[str]]]:
    """Pick out the files a person actually has to place, with why for each.

    The author cannot audit a bare list of filenames — most of a skill folder is obviously
    skill material, and the one leftover hides in the middle of it. Everything matching the
    ordinary shape is counted rather than listed; what breaks the shape is shown with the
    reason it broke, which is the part that makes the question answerable.
    """
    standout = []
    for rel in files:
        size = (root / rel).stat().st_size
        suffix = rel.suffix.lower()
        tokens = set(re.split(r"[^a-z0-9]+", rel.stem.lower()))
        reasons = []

        if suffix in DATA_SUFFIXES:
            reasons.append("a data file rather than skill material")
        if rel.name.startswith("~$") or tokens & DRAFT_TOKENS or any(
                hint in rel.stem for hint in DRAFT_HINTS_KO):
            reasons.append("the name reads like a draft or a personal copy")
        if size > STANDOUT_BYTES:
            reasons.append(f"{human_size(size)}, large for a skill file")
        # There is deliberately no rule about where a file sits. Two once lived here — a
        # file loose in the folder root, and a folder outside references/scripts/assets —
        # and across the 81 skills installed on this machine they produced 136 of 137 hits,
        # 49 from one skill alone. They were measuring "this author did not use the layout
        # I assumed" rather than "this file should not leave", and a list that long is the
        # unreadable list this filter exists to avoid. What a file *is* survives; where its
        # author chose to put it does not.
        #
        # Being pointed at from SKILL.md is the purpose of references/, so a markdown in
        # there that nothing links to is either dead or was never part of the skill. The
        # rule stops at that folder on purpose — assets/ holds what code reads or what
        # ships in the output, and those are never linked. Applying it there flagged this
        # skill's own INSTALL_TEMPLATE.md, which pack.py reads and no document mentions.
        if (suffix == ".md" and len(rel.parts) > 1 and rel.parts[0] == "references"
                and rel not in referenced):
            reasons.append("nothing in the skill links to it")

        if reasons:
            standout.append((rel, size, reasons))
    return standout


def scan_text_patterns(root: Path, files: list[Path], findings: list[Finding]) -> None:
    """Absolute paths and credential-shaped strings. Both are judgement calls, never FAIL."""
    counts: dict[str, int] = {}
    questions: dict[str, str] = {}
    for rel in files:
        if rel.suffix.lower() not in TEXT_SUFFIXES:
            continue
        lines = read_text(root / rel).splitlines()
        for number, line in enumerate(lines, 1):
            for pattern, label, question in TEXT_PATTERNS:
                # Every match on the line, not just the first. Six addresses on one line is
                # six things to judge, and undercounting runs the wrong way for this check.
                for match in pattern.finditer(line):
                    questions[label] = question
                    seen = counts.get(label, 0)
                    counts[label] = seen + 1
                    if seen >= MAX_REPORTED_PER_KIND:
                        continue
                    excerpt = match.group(0)
                    if len(excerpt) > 60:
                        excerpt = excerpt[:57] + "..."
                    findings.append(Finding(WARN, label, f"{rel}:{number} — {excerpt}", question))

    for label, total in sorted(counts.items()):
        if total > MAX_REPORTED_PER_KIND:
            findings.append(Finding(
                WARN, label, f"...and {total - MAX_REPORTED_PER_KIND} more of the same kind",
                questions[label]))


def detect_requirements(root: Path, files: list[Path]) -> tuple[list[str], list[str], list[Path]]:
    """What the recipient's machine has to already have for the skill to run.

    The zip carries every file the skill ships, but a script that imports pandas needs
    something the zip cannot contain. That gap fails on the recipient's machine and the
    packer is the last place it can be named — so the names go into INSTALL.md rather
    than being discovered by whoever receives it.
    """
    interpreters = sorted({INTERPRETERS[f.suffix.lower()]
                           for f in files if f.suffix.lower() in INTERPRETERS})

    if STDLIB_NAMES is None:
        return interpreters, [], []

    # A module that ships inside the bundle is not something to install.
    local = {f.stem for f in files if f.suffix.lower() == ".py"}
    local |= {f.parts[0] for f in files if len(f.parts) > 1}

    third_party: set[str] = set()
    unparsed: list[Path] = []
    for rel in files:
        if rel.suffix.lower() != ".py":
            continue
        try:
            tree = ast.parse(read_text(root / rel))
        except SyntaxError:
            unparsed.append(rel)
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                # A relative import resolves inside the bundle, so it needs nothing.
                names = [node.module] if node.module and node.level == 0 else []
            else:
                continue
            for name in names:
                top = name.split(".")[0]
                if top and top not in STDLIB_NAMES and top not in local:
                    third_party.add(top)

    return interpreters, sorted(third_party), unparsed


def inspect(root: Path) -> Inspection:
    findings: list[Finding] = []

    if not root.is_dir():
        findings.append(Finding(FAIL, "skill folder", f"'{root}' is not a folder."))
        return Inspection(root, [], findings, "", "")
    if not (root / "SKILL.md").is_file():
        findings.append(Finding(
            FAIL, "skill folder",
            f"'{root}' has no SKILL.md, so it is not a skill folder. Point at the folder that "
            f"contains SKILL.md, not its parent."))
        return Inspection(root, [], findings, "", "")

    files = collect_files(root)
    # The folder name is authoritative, not the frontmatter name — it is what the skill is
    # invoked as. Naming the packed folder after the frontmatter would silently rename the
    # skill on the recipient's machine, which is the opposite of what packing is for.
    description = check_frontmatter(root, findings)
    referenced = check_references(root, files, findings)
    scan_text_patterns(root, files, findings)

    interpreters, third_party, unparsed = detect_requirements(root, files)
    standout = classify_files(root, files, referenced)
    inspection = Inspection(root, files, findings, root.name, description,
                            interpreters, third_party, unparsed, standout)

    if third_party:
        findings.append(Finding(
            NOTE, "outside dependency",
            f"the skill needs {', '.join(third_party)} installed on the recipient's machine "
            f"— not in the zip, and recorded in INSTALL.md"))
    if unparsed:
        findings.append(Finding(
            WARN, "unreadable script",
            ", ".join(p.as_posix() for p in unparsed),
            "This did not parse as python, so its imports were not checked. Is it valid, and "
            "does it need anything the recipient will not have?"))

    if inspection.scripts:
        # A note, not a question. The author wrote these and knows what they do; asking them
        # to vouch for their own code changes nothing about what gets packed. It is the
        # recipient who benefits from knowing, and INSTALL.md carries it to them.
        listed = ", ".join(p.as_posix() for p in inspection.scripts[:10])
        findings.append(Finding(
            NOTE, "executable content",
            f"the recipient will end up running {listed} — INSTALL.md says so"))
    if inspection.total_bytes > LARGE_BUNDLE_BYTES:
        findings.append(Finding(
            WARN, "size", f"the bundle is {human_size(inspection.total_bytes)}",
            "That is large for a skill. Did build output or sample data drift into the "
            "folder while you were working on it?"))

    return inspection


def human_size(size: int) -> str:
    if size < 1024:
        return f"{size} B"
    if size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size / (1024 * 1024):.1f} MB"


def print_report(inspection: Inspection, show_all: bool = False) -> None:
    root = inspection.root
    print(f"Skill folder — {root}")
    print(f"Skill name   — {inspection.skill_name}")
    print(f"Files        — {len(inspection.files)}, {human_size(inspection.total_bytes)} total")
    print()

    if inspection.files:
        print_contents(inspection, show_all)


def print_contents(inspection: Inspection, show_all: bool) -> None:
    root = inspection.root
    if show_all:
        print("Contents to be packed:")
        for rel in inspection.files:
            size = human_size((root / rel).stat().st_size)
            print(f"  {rel.as_posix():<50} {size:>10}")
        print()
        return

    standout_paths = {rel for rel, _, _ in inspection.standout}
    ordinary = [rel for rel in inspection.files if rel not in standout_paths]
    if ordinary:
        # Shape, not a list. Enough for the author to notice a count they did not expect.
        buckets: dict[str, int] = {}
        for rel in ordinary:
            key = f"{rel.parts[0]}/" if len(rel.parts) > 1 else "folder root"
            buckets[key] = buckets.get(key, 0) + 1
        shape = ", ".join(f"{key} {count}" for key, count in sorted(buckets.items()))
        print(f"{len(ordinary)} of these look like ordinary skill material — {shape}")

    if inspection.standout:
        print()
        print("These do not, and placing them is the part no scan can do:")
        for rel, size, reasons in inspection.standout:
            print(f"  {rel.as_posix():<40} {human_size(size):>9}   {'; '.join(reasons)}")
    print()
    print("Pass --all for the complete file list.")
    print()

    if inspection.failures:
        print(f"{FAIL} — the skill will not work on the recipient's machine:")
        for finding in inspection.failures:
            print(f"  [{finding.check}] {finding.message}")
        print()

    if inspection.warnings:
        print(f"{WARN} — worth a look before you say yes:")
        # Grouped by check so the question is stated once and the occurrences sit under it.
        # A flat list repeats the reasoning per line and gets skimmed.
        for check in dict.fromkeys(f.check for f in inspection.warnings):
            group = [f for f in inspection.warnings if f.check == check]
            print(f"  [{check}] {group[0].question}")
            for finding in group:
                print(f"      {finding.message}")
        print()

    if inspection.notes:
        print("NOTE — nothing to decide, just so you know:")
        for finding in inspection.notes:
            print(f"  [{finding.check}] {finding.message}")
        print()

    if not inspection.findings:
        print("No problems found.")


def render_install_doc(inspection: Inspection, author: str | None) -> str:
    template_path = Path(__file__).resolve().parent.parent / "assets" / "INSTALL_TEMPLATE.md"
    if not template_path.is_file():
        raise SystemExit(f"packer is incomplete — template missing at {template_path}")

    root = inspection.root
    # Posix separators throughout — this manifest describes what is inside the zip, and a
    # zip stores forward slashes whatever platform packed it.
    #
    # The digest is what turns "copy it, do not rewrite it" from an instruction into
    # something the recipient can check. An agent that helpfully reformats SKILL.md, or a
    # transfer that mangles line endings, changes the digest and shows up immediately.
    rows = []
    for rel in inspection.files:
        path = root / rel
        digest = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
        rows.append(f"| `{rel.as_posix()}` | {human_size(path.stat().st_size)} | `{digest}` |")
    table = "| 파일 | 크기 | SHA-256 앞 16자리 |\n|---|---|---|\n" + "\n".join(rows)

    requirements = []
    for name in inspection.interpreters:
        requirements.append(f"- **{name}** — 스킬 안의 스크립트를 실행하는 데 필요합니다.")
    if inspection.third_party:
        listed = ", ".join(f"`{name}`" for name in inspection.third_party)
        requirements.append(
            f"- **파이썬 패키지 {listed}** — 표준 라이브러리가 아니라서 zip에 담을 수 없습니다. "
            f"받는 컴퓨터에 따로 설치돼 있어야 스킬이 동작합니다.")
    # Three cases, because two of them used to collapse into one and produced a document that
    # contradicted itself — "문서 파일만 담겨 있습니다" one section above a list of the scripts
    # the recipient will run. Nothing here may claim there are no scripts unless there are none.
    if requirements:
        requirement_text = "\n".join(requirements)
    elif inspection.scripts:
        requirement_text = "스킬 안의 스크립트를 실행하는 데 따로 설치할 것은 없습니다."
    else:
        requirement_text = "따로 설치할 것은 없습니다. 문서 파일만 담겨 있습니다."

    if inspection.scripts:
        listed = "\n".join(f"- `{rel.as_posix()}`" for rel in inspection.scripts)
        notes = (
            "이 스킬에는 실행되는 스크립트가 들어 있습니다. 스킬이 동작할 때 아래 파일이 "
            "실행됩니다.\n\n" + listed
        )
    else:
        notes = "실행되는 스크립트는 들어 있지 않습니다. 문서 파일만 담겨 있습니다."

    description = inspection.description.strip()
    if len(description) > 300:
        description = description[:297] + "..."

    author_line = f", 포장한 사람 — {author}" if author else ""

    return (template_path.read_text(encoding="utf-8")
            .replace("{{SKILL_NAME}}", inspection.skill_name)
            .replace("{{DESCRIPTION}}", description or "(설명 없음)")
            .replace("{{PACKED_ON}}", date.today().isoformat())
            .replace("{{AUTHOR_LINE}}", author_line)
            .replace("{{FILE_TABLE}}", table)
            .replace("{{REQUIREMENTS}}", requirement_text)
            .replace("{{NOTES}}", notes))


def build_zip(inspection: Inspection, out_dir: Path, author: str | None, force: bool) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{inspection.skill_name}-skill.zip"
    if target.exists() and not force:
        raise SystemExit(
            f"'{target}' already exists. Pass --force to replace it, after checking that "
            f"nobody is relying on the copy that is there.")

    install_doc = render_install_doc(inspection, author)
    root = inspection.root
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("INSTALL.md", install_doc)
        for rel in inspection.files:
            archive.write(root / rel, f"{inspection.skill_name}/{rel.as_posix()}")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    checker = sub.add_parser("check", help="report what would be packed; writes nothing")
    checker.add_argument("skill", type=Path)
    checker.add_argument("--all", action="store_true", dest="show_all",
                         help="list every file instead of only the ones that stand out")

    builder = sub.add_parser("build", help="re-check, then write the zip")
    builder.add_argument("skill", type=Path)
    builder.add_argument("--all", action="store_true", dest="show_all",
                         help="list every file instead of only the ones that stand out")
    builder.add_argument("--out", type=Path, default=Path.cwd(),
                         help="destination folder for the zip (default — current directory)")
    builder.add_argument("--author", default=None, help="who packed it, recorded in INSTALL.md")
    builder.add_argument("--force", action="store_true", help="replace an existing zip")

    args = parser.parse_args()
    inspection = inspect(args.skill.expanduser().resolve())
    print_report(inspection, args.show_all)

    if inspection.failures:
        print(f"Refusing to pack — {len(inspection.failures)} blocking problem(s). "
              f"Fix them in the skill folder and run check again.")
        return 1

    if args.command == "check":
        # One confirmation, and it is about the target — is this the skill to pack. Packing
        # is a mechanical job with right answers, so there is no list of judgements to put
        # to the author; anything they should see is above, in the same breath as the name.
        print(f"Confirm with the author that '{inspection.skill_name}' is the skill to pack.")
        if inspection.warnings or inspection.standout:
            print("The items above are what to put in front of them alongside it.")
        print("Nothing has been written. To drop a file, remove it from the folder and run "
              "check again; the zip is always the folder as it stands.")
        return 0

    target = build_zip(inspection, args.out.expanduser().resolve(), args.author, args.force)
    print(f"Wrote {target} ({human_size(target.stat().st_size)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
