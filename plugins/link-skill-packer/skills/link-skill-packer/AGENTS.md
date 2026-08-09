# link-skill-packer — for Codex and other agents

Packs a skill folder into a zip that installs by copying one folder. Read
[`SKILL.md`](SKILL.md) and follow it. The only dependency is python, standard library only.

## When to open it

Whenever a skill has to reach another machine and git is not available — a coworker, a shared
drive, an email attachment. Also when a skill that arrived as a copied folder never loads at
all, because the checks in here name the usual cause. Not when a skill loads but fires at the
wrong moment — that is a description problem, and it belongs to `link-skill-authoring`.

## What it guarantees

No zip is written until the checks pass **and** the author has confirmed what goes in it. The
script enforces the first half in both subcommands; the second half is a stop in `SKILL.md`
and is the one that gets skipped.

## The two commands

```
python scripts/pack.py check <skill-folder>
python scripts/pack.py build <skill-folder> --out <destination> [--author "name"] [--force]
```

`check` writes nothing. `build` re-runs the same checks and refuses on any FAIL.

If the ask is a diagnosis rather than a pack — a copied skill folder that never appears in the
skill list — run `check`, report what it found, and stop. There is no zip to build and nothing
to confirm. Only one of the three usual causes is in the files; the other two are a skill list
read once at session start, and a folder copied one level too deep.

## The severity split

| Severity | Meaning |
|---|---|
| FAIL | The skill will not work on the recipient's machine, and no error is produced there — no `SKILL.md`, a BOM before the frontmatter, no frontmatter block, a missing `description`, a colon-space in an unquoted `description`. Five conditions, all decidable from the file alone |
| WARN | Reported, never blocks. Absolute paths, links leaving the folder, credential-shaped strings, a path that resolves to nothing while others in the same document do, a script that will not parse, an oversized bundle — each has legitimate cases and only a person can tell |
| NOTE | Not a question at all, because no answer changes the zip. Bundled scripts, outside dependencies, a frontmatter `name` that disagrees with the folder, a document where no referenced path resolves |

A `name` that disagrees with the folder does **not** stop a skill loading, and a referenced
path that misses is usually the skill pointing at the user's project rather than at itself.
Both were FAILs once and were demoted when running against the installed skills disproved them.
Do not restore either without the same evidence.

## What it does not do

It does not edit the skill it is packing. It does not install anything. It does not send the
zip anywhere — it writes one file to the path given. Creating and reviewing skills belongs to
`link-skill-authoring` and a skill-building process. Name it, do not link it — a path out of
this folder does not survive the zip, which is the same WARN this packer raises on everyone
else's skill.

Answer in the language the user is writing in.
