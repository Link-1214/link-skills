---
name: link-skill-packer
description: Package an agent skill — any folder with a SKILL.md in it — into a zip that installs by copying one folder, for handing a skill to someone when git and plugin marketplaces are out of reach. Use when the user wants to package, zip, bundle, share, send, hand off, move, export, or distribute a skill they wrote — to a coworker, a shared drive, or an email attachment — or asks how to get a skill onto another machine without git or a marketplace. Also use when a skill that arrived as a copied folder never appears in the skill list at all — no error, just absent — because the checks that gate packing name the cause. Not for writing a skill or fixing when it fires; that is link-skill-authoring.
---

# Skill packer — moving a skill without git

**Contract — this skill writes no zip until the checks pass and the author has confirmed the
skill being packed.** One confirmation, about the target, with everything they should see
shown alongside it. There is no second round of judgements to answer, because packing is a
mechanical job with right answers and the script finds them.

Answer in the language the user is writing in.

## Why this exists

A skill normally travels as a plugin from a git marketplace. Inside a company that blocks
GitHub, that route is gone, and a skill written on one machine cannot reach the person sitting
next to its author. This packs the folder into a zip that moves over a shared drive, an email,
or a chat attachment, and installs by copying one folder.

The packer earns its place through the checks, not the zipping. A skill fails on the recipient's
machine in ways that produce **no error at all** — it simply never appears, and the recipient
reports "it doesn't work" with nothing to go on. Those failures are cheap to catch here and
expensive to diagnose there.

## The two commands

```
python scripts/pack.py check <skill-folder>
python scripts/pack.py build <skill-folder> --out <destination> [--author "name"] [--force]
```

`check` writes nothing. `build` re-runs the same checks and refuses on any FAIL, so there is no
way to skip them by calling `build` directly.

Paths are relative to this skill's own directory. Locate the script from where this `SKILL.md`
sits rather than assuming a working directory.

## Step 1 — pick the skill, run the checks, and confirm the target

### If the ask is a diagnosis, not a pack

A copied skill folder that never appears in the skill list has usually failed in one of three
ways, and only one of them is in the files. Run `check` on the folder as installed — it names a
byte order mark or broken frontmatter if that is the cause. The other two it cannot see. The
skill list is read once at session start, so a skill installed during the current session is
absent by design and appears in the next one. And a folder copied one level too deep, described
under "What the recipient does" below, puts `SKILL.md` somewhere `check` would never be pointed
— confirm it sits directly under `skills/<name>/`.

Report what you find and stop there. There is no zip to build and nothing to confirm; the fix
belongs in the folder on the machine where it is broken. Do not roll a diagnosis into a pack —
nobody asked for a delivery.

### Where skills live

Skills live in one of two places, and both are ordinary folders containing `SKILL.md`.

| Location | Path |
|---|---|
| This project only | `.claude/skills/<name>/` |
| Every project for this user | `~/.claude/skills/<name>/` |

Do not pack from `~/.claude/plugins/cache/`. Those paths carry a version number that will not
exist on the recipient's machine, and the copy there is a build artifact rather than the source.
If the user wants to pass along an installed plugin, say so and ask where the original lives.

### Read the report

Run `check` and read the whole report. It returns three severities.

**FAIL — the skill will not work on the recipient's machine.** Every one of these means the
skill loads as if it had no metadata, or reaches for a file that is not in the zip. There is no
error message on the other end; the skill is simply absent.

| Check | What goes wrong |
|---|---|
| `SKILL.md` missing | Not a skill folder |
| Byte order mark before the frontmatter | Frontmatter parsing breaks and every field is dropped |
| No frontmatter block | Same result, no metadata to match on |
| `description` missing | Nothing for a model to match, so the skill never fires |
| Unquoted `description` containing a colon followed by a space | YAML reads it as a mapping and discards the entire frontmatter |

Every one of those is decidable from the file alone, and that is the bar. Two checks used to
sit here and no longer do, both because running against the 81 skills installed on this
machine proved them wrong. A `name` that disagrees with the folder does **not** stop a skill
loading — five installed skills have it and all five appear in the skill list, because the
folder name is what a skill is invoked as. And a referenced file that is not in the bundle
blocked 13 working skills, since a skill's prose names paths in the user's project as freely
as its own. Both are questions now.

**WARN — worth the author's eye before they confirm.** These never block, because each has
legitimate cases the packer cannot tell apart. Each prints with what makes it ambiguous;
show them alongside the target rather than as findings on their own.

| Check | Why it is a judgement |
|---|---|
| Absolute paths, UNC paths, home directories | Fine in an example, broken as a real reference |
| Links pointing outside the skill folder | The target does not travel in the zip, so the link breaks — harmless in prose, not in a step the skill depends on |
| Credential-shaped strings, private IPs, email addresses | Often a placeholder, sometimes the real thing leaving the building |
| A document where some referenced paths resolve and some do not | The author is pointing at bundled files in that file, and these do not land. That is what a typo looks like |
| A bundled `.py` that does not parse | Its imports were never read, so the dependency list below is incomplete — and a script that will not parse may not run either |
| A bundle large for a skill | Build output or sample data drifts into a folder while it is being worked on. Only the author can say which it is |

**NOTE — background, not something to weigh.** The test is whether it could change the
author's answer. If it cannot, it belongs here however reasonable it sounds. Four things
live here, two of them promoted down once the numbers came in.

| Note | Why it is not a question |
|---|---|
| Bundled scripts | Asking authors to vouch for code they wrote changes nothing. The recipient benefits from knowing, and `INSTALL.md` tells them |
| Outside dependencies | The zip cannot carry them either way. Naming them is the whole remedy |
| A `name` that disagrees with the folder | Packing keeps the folder name unconditionally, so every answer produces the same zip |
| A document where **no** referenced path resolves | It is describing the user's project, not pointing at its own files. True 22 times out of 22 across the installed skills |

Demoting the last two took WARN from 36 runs in 81 down to 9. Nothing was lost — none of the
27 had a real problem behind it, and a confirmation cluttered with items that never change the
answer is one nobody reads.

**Outside dependencies are the half of the bundle a zip cannot carry.** The script names the
interpreter every bundled script needs, and reads the imports in every bundled `.py` to name
anything outside the standard library. A skill whose collector imports `pandas` ships complete
and still dies on a machine without it, and the packer is the last place that can be said out
loud, so it lands in `INSTALL.md` under what the recipient has to already have.

Import scanning is python-only. A bundled `.js` gets Node named as a requirement but its npm
packages are not read, so say so rather than implying the list is complete. Writing a parser
per language would cost more than it returns; naming the interpreter is what stops the silent
death.

The packer does not edit the skill. Not the byte order mark, not the description, nothing —
fixing someone's skill on the way out means the thing they tested is not the thing that shipped.
Report what to change and let the author change it.

### Confirm the target, once

Put one thing to the author — **is this the skill to pack?** — with what they should see in
the same breath. Then wait.

A confirmation, not a quiz. Packing is mechanical and has right answers, and the script has
already found them; there is nothing here that only a person's taste or intent can settle.
The one thing the script genuinely cannot know is whether some file must not leave the
building, and that surfaces naturally when the target is named with its contents rather than
as a separate round of judgements.

So the shape is:

> Packing `<name>` — 12 files, 84 KB. `실적_2026Q2.xlsx` is a data file rather than skill
> material. Go ahead?

**Show what stands out, not the folder.** The report does not list every file and neither
should you. Reading fourteen filenames back at someone is how the one that mattered goes past
with the rest — nobody can audit a flat list, and nobody reads one. The script counts the
ordinary files and names only those that break the shape, each with the reason: a spreadsheet
or archive, a name that reads like a draft or a personal copy, a file large for a skill, a
markdown in `references/` that nothing links to.

What a file *is* can flag it; where its author put it cannot. Two layout rules once lived here
and produced 136 of 137 hits across the installed skills, 49 from one skill alone, purely
because those authors did not use the folder structure the rules assumed.

**Most runs have nothing to show.** Seventy-two of the 81 installed skills raise no WARN at
all; the confirmation is then just the name and the count. Do not pad it out. Every check that
once fired on every run turned out to be measuring something other than risk, and each had to
be walked back once the numbers came in. `--all` is there for an author who wants the full
list anyway.

**Name the target.** Asking "is this okay?" instead gets a yes every time, and then the
confirmation half of the contract exists on paper only. That is the failure this step is shaped
to avoid — it is the likeliest step to lose, because by now the checks have passed and building
looks like a formality. A zip is not a draft. It lands on a shared drive and gets copied onward,
so the moment to catch something is before it is written.

**If a FAIL is outstanding, there is nothing to confirm.** Report it and stop. Do not offer to
work around it.

**If something must not go, the fix is the folder, not a flag.** Have the author remove or
move the file, then run `check` again. The packer never packs a subset — a zip that differs
from the folder means the next person to pack it gets a different result, and the author's
tested skill is not the shipped one. Same reason nothing is auto-fixed.

## Step 2 — build

`build` writes `<skill-name>-skill.zip` to the destination, named after the **folder**, not the
frontmatter. A skill is invoked by its folder name, so packing under the name inside the file
would quietly rename it on arrival — `taste-skill` would install as `design-taste-frontend` and
nobody's existing habit would work. The layout makes installation one copy:

```
<skill-name>-skill.zip
├── INSTALL.md          what it is, how to install it, what is inside
└── <skill-name>/       copy this one folder into .claude/skills/
```

`INSTALL.md` carries three things the recipient cannot work out for themselves — what has to be
installed on their machine before the skill will run, the file list, and a SHA-256 digest per
file. The digest is what turns "copy it, do not rewrite it" from an instruction into something
checkable: an agent that helpfully reformats `SKILL.md` changes the digest, and the recipient
sees it rather than discovering later that the skill never loads.

It refuses to overwrite an existing zip unless `--force` is passed. Confirm with the user before
passing it — a stale copy on a shared drive is recoverable, and one silently replaced is not.

`--author "name"` records who packed it in `INSTALL.md`. Offer it; do not guess a name or read
one from the system.

Report the output path when it is done, and tell the user where the recipient should be told to
put it.

## What the recipient does

`INSTALL.md` is written for someone who does not have this skill, so nothing on the receiving
end depends on it. It is a copy manifest and nothing more — it never asks the recipient's agent
to run anything, because an attachment that steers someone else's agent is a bad shape however
much the sender is trusted.

Two things in it matter enough to repeat when handing the zip over.

**Copy the folder, do not read and rewrite it.** An agent told to "install this" may re-save
`SKILL.md`, which can add a byte order mark and break the frontmatter — the same silent failure
the checks exist to prevent, reintroduced at the last step. The digest table is there so this
does not have to be taken on trust; a rewritten file no longer matches.

**A newly installed skill is invisible until the next session.** The skill list is read at
session start. The recipient checking in the session where they installed it will find nothing
and conclude it failed.

**Copying the wrong folder buries it one level too deep.** Extracting the zip in Windows
Explorer creates a `<name>-skill` folder holding `INSTALL.md` and `<name>`; copying the outer
one lands `SKILL.md` at `skills/<name>-skill/<name>/SKILL.md` and the skill never appears. When
diagnosing a skill that will not show up, this ranks with the other two — check that `SKILL.md`
sits directly under `skills/<name>/` before looking further.

## What this does not do

It does not create or edit skills — `link-skill-authoring` covers what a skill should guarantee,
and a skill-building process covers drafting it. **It does not pack a subset of the folder**, so
there is no exclude option to reach for; the zip is the folder as it stands. It does not install
anything on the packing machine. It does not upload, send, or copy the zip anywhere; it writes
one file to the path given and stops. It does not judge whether the skill is any good, only
whether it will survive the trip.
