# link-design-pitch — for Codex and other agents

This directory is a skill: a written procedure any coding agent can follow. Nothing here is Claude-specific — it is Markdown instructions plus reference files.

## How to use it

Read `SKILL.md` and follow it. It runs in four phases: read the platform's constraints, ask the owner five questions, present ten visual directions rendered with their real content, recommend one, and after they choose, produce the detailed screen-by-screen spec.

Load the reference files when the phase calls for them:

| File | When |
|---|---|
| `references/feasibility.md` | Phase 0 — before pitching anything, to learn what the target platform can actually render |
| `references/directions.md` | Phase 2 — the catalog of eighteen directions to choose ten from |
| `references/board.md` | Phases 2 and 4 — how to build the HTML boards |

## When to use it

Whenever the visual direction of an interface is undecided or under question: a new UI, a restyle, a theme change, a color scheme, or an owner saying the current thing looks bland, dated, or generic. It works before the code exists, midway through, and on software that already ships — `SKILL.md` Phase 0 explains how the constraints differ.

## Wiring it into a project

Add a line to the project's own `AGENTS.md` so it is discoverable from where the work happens,
pointing at wherever you cloned or installed this directory:

```markdown
Design direction undecided or under review? Follow <path-to>/link-design-pitch/SKILL.md
```

If you installed it as a Claude Code skill it will be under `~/.claude/skills/link-design-pitch/`;
otherwise it can live anywhere on disk, since the skill is just Markdown.

## Output contract

Three files under `design-pitch/` in the target project:

| File | Audience |
|---|---|
| `01-directions.html` | People — the ten-direction board |
| `02-detail-<direction>.html` | People — the chosen direction across every screen |
| `DECISION.md` | **Agents** — questions, answers, verdicts, chosen direction, token values, implementation checklist |

`DECISION.md` is the important one for you. It is plain Markdown, so a later session or a different agent can pick up the decision without opening a browser or fetching a hosted link. Keep it accurate — a stale decision record is worse than none, because the next agent will believe it.
