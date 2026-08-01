# design-pitch — for Codex and other agents

This directory is a skill: a written procedure any coding agent can follow. Nothing here is Claude-specific — it is Markdown instructions plus reference files.

## How to use it

Read `SKILL.md` and follow it.

**It has two mandatory pauses and they are the shape of the exercise**: after the recommendation
(Phase 3) you stop and ask which direction they want, and before speccing behavior (Phase 5) you
stop and ask the interaction questions. Running past either takes the decision away from the person
whose decision it is, and burns effort on detail for a direction that may not be chosen.

Phases: read the target's constraints → five questions → ten directions rendered with their real
content → compare and recommend → **stop** → spec the chosen direction → **ask** → spec behavior.

Load the reference files when the phase calls for them:

| File | When |
|---|---|
| `references/feasibility.md` | Phase 0 — before pitching anything, to learn what the target platform can actually render |
| `references/directions.md` | Phase 2 — the catalog of twenty-four, each with a ready-made token line. **Assemble from it; do not derive palettes by hand** — that is the largest avoidable cost in a run |
| `references/board.md` | Phases 2 and 4 — how to build the HTML boards |
| `references/behavior.md` | Phase 5 — states, and the interaction forks to put to the owner. Skip when the artifact does not move (print, deck, spreadsheet) |

## When to use it

Whenever the visual direction of any designed artifact is undecided or under question — a UI, a restyle, a theme, a color scheme, a deck, a report, a spreadsheet, or an owner saying the current thing looks bland, dated, or generic. It works before the code exists, midway through, and on software that already ships — `SKILL.md` Phase 0 explains how the constraints differ.

## Wiring it into a project

Add a line to the project's own `AGENTS.md` so it is discoverable from where the work happens,
pointing at wherever you cloned or installed this directory:

```markdown
Design direction undecided or under review?
Follow <path-to>/link-skills/plugins/link-design-pitch/skills/design-pitch/SKILL.md
```

Installed through Claude Code it is invoked as `link-design-pitch:design-pitch`. Cloned, it can
live anywhere on disk — the skill is just Markdown and needs no installation.

## Output contract

Four files, placed where the project already keeps documentation — `docs/design/` when a `docs/`
directory exists, otherwise `design/`:

| File | Audience |
|---|---|
| `01-directions.html` | People — the ten-direction board |
| `01-directions.png` | **Agents with vision** — they see the styles, not just the markup |
| `02-detail-<direction>.html` | People — the chosen direction across every surface |
| `DECISION.md` | **Everyone else** — questions, answers, verdicts, measurements, token values, implementation checklist |

`DECISION.md` is the important one for you. It is plain Markdown, so a later session or a different agent can pick up the decision without opening a browser or fetching a hosted link. Keep it accurate — a stale decision record is worse than none, because the next agent will believe it.
