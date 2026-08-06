# link-skill-authoring — for Codex and other agents

Criteria for skills that hold up. Plain Markdown, nothing Claude-specific. Nothing to
install — read [`SKILL.md`](SKILL.md) and apply it.

## When to open it

Whenever a skill is being created, edited, reviewed, or split. Also when a skill fires at
the wrong moment or never fires, since that is a `description` problem and the criteria
cover it.

## What it holds

| Part | What it settles | Applies to |
|---|---|---|
| Two rules | Fires when needed. Does not hide a guess. Both are failures the author cannot see by using the skill | Every skill, no exceptions |
| One line of contract | What this particular skill promises | Only where there is a boundary to promise |
| Six questions | Asked before building. "Not applicable" is a real answer | Only where they fit the kind of skill |

Keep the two tiers apart. Forcing a contract onto a skill that has nothing to promise
produces a sentence rather than a decision, which is the failure the second tier exists to
avoid.

## Where it stops

Facts and judgements need no permission — check them, say so, fix them. **Stop at one
place: before writing a contract line or a boundary.** Only the person building the skill
can say what it will guarantee, and drafting it for them would break Rule 2 in this skill's
own terms. Reviewing a contract that already exists is a judgement, so do not stop there.

The answer is recorded as the contract line in that skill's `SKILL.md`. No separate
decision file.

## What it does not do

It does not run the build. On Claude Code, `skill-creator` owns drafting, test prompts, and
evaluation; this supplies the criteria that process aims at. On other runtimes there may be
no equivalent, and then the questions in `SKILL.md` are the whole procedure.

It also does not cover adding a skill to this repository — marketplace registration,
dependencies, version bumps, and validation live in
[`AUTHORING.md`](../../../../AUTHORING.md) at the repository root.

Answer in the language the user is writing in.
