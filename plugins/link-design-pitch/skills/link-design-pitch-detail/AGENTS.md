# link-design-pitch-detail — for Codex and other agents

A written procedure any coding agent can follow. Plain Markdown, nothing Claude-specific.

## This is the second of two skills

| Step | Skill |
|---|---|
| Ask five questions → ten directions → recommend → stop for the choice | `../link-design-pitch/SKILL.md` |
| *The owner builds the real features and content* | — |
| Apply the chosen direction to every surface → present interaction options | **this one** |

## Refuse to start without a decision

Find `docs/design/DECISION.md` or `design/DECISION.md`. **If it is missing, or its `Status` is not a
chosen direction, stop and point at `link-design-pitch`.**

Do not improvise a direction. The value of the first skill is that ten options were surveyed and one
was chosen with reasons; inventing one here throws that away silently, and the owner will not know.

## How to use it

Read `SKILL.md` and follow it.

| File | When |
|---|---|
| `references/spec.md` | Phase 4 — building and verifying the per-surface file, plus five measurement traps that have each produced a wrong finding |
| `references/behavior.md` | Phase 5 — the interaction forks to put to the owner, and the states checklist |

## The one hard limit

**Phase 5 presents options. It does not build them.** No state mockups, no behavior specification,
no motion tables. Options, trade-offs, a recommendation, then ask.

This is about cost. A full behavior spec runs longer than everything else in both skills combined
and is discarded the moment the owner names a model you did not offer. That has already happened:
a complete spec written around "optimistic vs confirmed" was invalidated by a third answer — stage
the changes, apply them together — in one sentence.

## Output contract

Appends to what the first skill produced, in the same directory:

| File | Audience |
|---|---|
| `02-detail-<direction>.html` | People — the direction across every surface |
| `02-detail-<direction>.png` | Agents with vision |
| `DECISION.md` | Updated in place — measurements, interaction answers, implementation list |

Before treating the record's implementation list as a plan, check whether the code already reflects
it. This has already cost one round of duplicated work: a checklist said *pending* while every item
had shipped.
