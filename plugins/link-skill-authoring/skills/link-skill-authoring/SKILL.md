---
name: link-skill-authoring
description: Criteria a skill must meet to hold up — what it guarantees, what it refuses to guess, and the failures that stay invisible until they are expensive. Use when creating, editing, reviewing, or splitting a skill or SKILL.md, when deciding what a new skill should be responsible for, when writing or fixing a skill description, or when a skill fires at the wrong time or never fires. Also use before publishing a skill to a marketplace. Runs alongside skill-creator, which owns the process.
---

# Skill authoring — what a skill has to guarantee

A skill that audits code and a skill that opens up design options are not good in the same
way. Hold every skill to one checklist and the author fills boxes that do not apply, with
words instead of decisions.

So only two rules apply to every skill. Everything else each skill settles for itself.

**Contract — this skill supplies criteria and never writes the skill for you.** It will say
which rule a draft breaks and whether a contract can be written for it. Producing the
wording is separate work, and doing it here would hide whether the author had actually
decided anything.

Answer in the language the user is writing in.

## Where this sits

`skill-creator` owns the process — drafting, running test prompts, evaluating, iterating.
This skill owns the criteria that process aims at. Run both. Neither replaces the other.

## The test for a rule

**Only what fails silently earns a rule here.**

A skill that reads confusingly, or runs slow, or does too much, teaches the author by being
used. Those need no rule. A rule pays for itself only where the skill is wrong and nobody
can tell — because then no amount of use surfaces it.

Two things pass that test.

## Rule 1 — it fires when needed, and stays quiet otherwise

A skill nobody loads is worth nothing, however well written. The `description` is the only
thing a model sees when deciding, so spend it on triggers — the phrasings a user would
actually type, the symptoms they would describe, the synonyms they might reach for. Models
undertrigger far more often than they overtrigger, so lean pushy.

**Then keep the procedure out of it.** The superpowers repository measured this and named
it The Description Trap. A description that summarised the workflow got followed *instead
of* the body, and a review the body defined in two stages ran as one. The summary displaced
the source it was meant to advertise.

Identity and outcome are fine — a clause saying what the skill is for. An ordered sequence
is not.

> **The test.** If the description alone lets a model conclude "I know the steps now, no
> need to open the file", it is written wrong.

The risk scales with how much procedure the body carries. A skill whose body is mostly
reference material barely has this problem.

Two mechanical traps, both of which silence a skill completely:

- A colon followed by a space inside an unquoted YAML scalar parses as a mapping and
  discards the whole frontmatter. Use an em dash instead.
- A UTF-8 byte order mark before the opening `---` breaks frontmatter parsing the same way.
  Save without BOM.

## Rule 2 — it does not hide a guess

When a skill is uncertain and proceeds anyway without saying so, the output still looks
right. That is what makes this the second rule and not a preference — the user has no
signal that anything went wrong.

The rule holds across kinds; only its shape changes.

| Kind of skill | The same rule looks like |
|---|---|
| Ideation, options | Spread the candidates and stop, rather than narrowing to one silently |
| Audit, review | Do not report an unverified finding as settled |
| Analysis, aggregation | Put the assumptions that move the number into the output |
| Reference, explanation | Do not state what the source does not contain |

A worked case. Asked for average handling time, a skill can compute something without
knowing whether this organisation counts hold time, after-call work, or transfers. Each
choice changes the number. Pick one silently and a non-expert receives a confident wrong
answer, with nothing to question.

Lifting the guess costs one sentence. Naming the assumption in the output is usually
enough — stopping to ask is for when the choice genuinely changes the conclusion.

## What each skill settles for itself — one line of contract

Rather than growing the shared rules, every skill states its own promise in `SKILL.md`.
One line, near the top, in the form *this skill will not X* or *this skill guarantees Y*.

| Skill | Contract |
|---|---|
| `link-design-pitch` | Writes no styling code before a direction is chosen |
| `link-design-pitch-detail` | Refuses to run when no chosen direction is on record |

A contract earns its line by being checkable — one read settles whether a run honoured it.
It also carries the skill's boundary, which is what a broad skill most often lacks. If the
contract cannot be written, the skill is not yet decided; that is the finding, and it is
worth saying so rather than proceeding.

## Questions to answer before building

No answers are supplied. They differ by kind, and "not applicable" is a real answer. What
matters is that none of them is unanswerable.

1. How does this skill behave when it does not know?
2. How would the user tell that a result is wrong?
3. What does this skill not do?
4. Does a small request still run the whole procedure?
5. Six months on, what breaks first?

Question 3 goes missing most often, and the wider the skill's reach the more it costs — a
skill that does eight things is a black box until its boundary is written down.

Question 5 usually points at whatever the body hardcodes. Paths, schemas, versions, and
definitions move; keeping them out of the body is what makes a later fix local.
