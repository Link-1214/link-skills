# Repo-level checks that claude plugin validate cannot run in CI (no CLI there).
# Every check here exists because its absence already broke something once.
# Run: python scripts/validate_repo.py   (stdlib only, exit 1 on any failure)
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg: str) -> None:
    errors.append(msg)


# ── plugin.json: parse, name matches folder, semver version ──────────────────
plugin_dirs = sorted(d for d in (ROOT / "plugins").iterdir() if d.is_dir())
plugin_names = []
for d in plugin_dirs:
    mf = d / ".claude-plugin" / "plugin.json"
    if not mf.exists():
        err(f"{d.name}: plugin.json missing")
        continue
    try:
        meta = json.loads(mf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"{mf}: broken JSON — {e}")
        continue
    plugin_names.append(meta.get("name", ""))
    if meta.get("name") != d.name:
        err(f"{mf}: name '{meta.get('name')}' != folder '{d.name}'")
    if not re.fullmatch(r"\d+\.\d+\.\d+", meta.get("version", "")):
        err(f"{mf}: version '{meta.get('version')}' is not semver")

# ── marketplace.json: registration in both directions ────────────────────────
# A plugin folder not registered here installs for nobody, and the symptom is
# silent — this exact gap is step 2 of AUTHORING.md's checklist.
mp = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
registered = {p["name"] if isinstance(p, dict) else p for p in mp.get("plugins", [])}
for d in plugin_dirs:
    if d.name not in registered:
        err(f"marketplace.json: plugin folder '{d.name}' is not registered")
for name in registered:
    if not (ROOT / "plugins" / name).is_dir():
        err(f"marketplace.json: registers '{name}' but plugins/{name}/ does not exist")

# ── bundle: plugins/link must depend on every other plugin ───────────────────
# Forgetting this line means the new skill never reaches people who installed
# the bundle — AUTHORING.md step 3, and the quietest failure in the list.
link_meta = json.loads((ROOT / "plugins" / "link" / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
deps = set(link_meta.get("dependencies", []))
for name in plugin_names:
    if name != "link" and name not in deps:
        err(f"plugins/link: dependencies is missing '{name}'")

# ── SKILL.md frontmatter: present, complete, and not the colon trap ──────────
# An unquoted 'description' containing ': ' parses as a YAML mapping and every
# frontmatter field is silently dropped — the skill then never triggers.
for sk in sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md")):
    text = sk.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    rel = sk.relative_to(ROOT)
    if not m:
        err(f"{rel}: no frontmatter block")
        continue
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    for key in ("name", "description"):
        if not fields.get(key):
            err(f"{rel}: frontmatter is missing '{key}'")
    if fields.get("name") and fields["name"] != sk.parent.name:
        err(f"{rel}: frontmatter name '{fields['name']}' != folder '{sk.parent.name}'")
    desc = fields.get("description", "")
    if desc and not desc.startswith(('"', "'")) and ": " in desc:
        err(f"{rel}: unquoted description contains ': ' — YAML will parse it as a "
            f"mapping and silently drop ALL frontmatter. Use an em dash instead.")

# ── tone: no emoji anywhere in the repo's markdown ───────────────────────────
emoji = re.compile("[\U0001F000-\U0001FAFF☀-➿️]")
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
        if emoji.search(line):
            err(f"{md.relative_to(ROOT)}:{i}: emoji found — house style forbids them")
            break

if errors:
    print(f"FAIL — {len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK — {len(plugin_dirs)} plugins, "
      f"{len(list((ROOT / 'plugins').glob('*/skills/*/SKILL.md')))} skills checked")
