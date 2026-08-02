# link-design-pitch — for Codex and other agents

A written procedure any coding agent can follow. Plain Markdown, nothing Claude-specific.

## This is one of two skills

| Step | Skill |
|---|---|
| Ask five questions → present ten directions → recommend → **stop for the choice** | **this one** |
| *The owner builds the real features and content* | — |
| Apply the chosen direction to every surface → present interaction options | `../link-design-pitch-detail/SKILL.md` |

They are separate runs because building sits between them. Do not do the second half here.

## How to use it

Read `SKILL.md` and follow it. Load reference files when the phase calls for them:

| File | When |
|---|---|
| `references/feasibility.md` | Phase 0 — what the target can actually render, before pitching anything |
| `references/directions.md` | Phase 2 — the catalog of twenty-nine, each with a ready-made token line. **Assemble from it; do not derive palettes by hand** — that is the largest avoidable cost in a run |
| `references/board.md` | Phase 2 — building and verifying the board, and capturing the PNG |

## When to use it

Whenever the visual direction of any deliverable is undecided or under question — an app, a
restyle, a theme, a color scheme, a deck, a report, a spreadsheet, or an owner saying the current
thing looks bland, dated, or generic.

## Output contract

Placed where the project already keeps documentation — `docs/design/` when a `docs/` directory
exists, otherwise `design/`:

| File | Audience |
|---|---|
| `01-directions.html` | People — the ten-direction board |
| `01-directions.png` | Anywhere HTML does not render — GitHub, chat, an agent with vision |
| `DECISION.md` | **Everyone else, and the handoff to the detail skill** |

`DECISION.md` is a contract: the detail skill refuses to run without a chosen direction in it. Write
it even when the run ends before a choice, with `Status: Awaiting choice`.

Keep it accurate. A stale record is worse than none, because the next agent will believe it.
