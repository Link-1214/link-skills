# link-skill-authoring — for Codex and other agents

Criteria for skills that hold up. Plain Markdown, nothing Claude-specific. Nothing to
install — read [`SKILL.md`](SKILL.md) and apply it.

## When to open it

Whenever a skill is being created, edited, reviewed, or split. Also when a skill fires at
the wrong moment or never fires, since that is a `description` problem and the criteria
cover it.

## What it holds

| Part | What it settles |
|---|---|
| Two rules | The only things required of every skill. Both are failures the author cannot see by using the skill |
| One line of contract | What this particular skill promises. Each skill writes its own instead of inheriting more shared rules |
| Five questions | Asked before building. Answers differ by kind of skill, and "not applicable" is a real answer |

## What it does not do

It does not run the build. On Claude Code, `skill-creator` owns drafting, test prompts, and
evaluation; this supplies the criteria that process aims at. On other runtimes there may be
no equivalent, and then the questions in `SKILL.md` are the whole procedure.

It also does not cover adding a skill to this repository — marketplace registration,
dependencies, version bumps, and validation live in
[`AUTHORING.md`](../../../../AUTHORING.md) at the repository root.

Answer in the language the user is writing in.
