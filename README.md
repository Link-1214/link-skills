# link-design-pitch

Pitch visual design directions the way a studio does, instead of guessing at a single comp.

Ten directions on the wall, rendered with your real content. Trade-offs argued out loud. Technical feasibility checked *before* anyone falls in love with something the platform cannot render. One recommendation, one strongest objection to it, then the owner picks — and only then the detailed screen-by-screen spec.

## Why

The expensive mistake in design work is not picking the wrong style. It is discovering three days into implementation that the style could never have worked here — that Qt silently ignores `backdrop-filter`, that the email client drops flexbox, that the chart library keeps its own white background no matter what the theme says.

Ten cheap directions surface that on day one.

## The five questions

1. Who is this for? — a daily operator and a first-time visitor want opposite things
2. What kind of page is it? — governs density
3. What is the core color? — answered with four reasoned palettes, not an open prompt
4. What layout? — offered as choices, with the cost of changing an existing one stated
5. **What is the one action this must drive?** — sets the visual hierarchy for everything downstream

## Output

Three files under `design-pitch/` in your project:

| File | Audience |
|---|---|
| `01-directions.html` | People — the ten-direction board |
| `02-detail-<direction>.html` | People — every screen in the chosen direction |
| `DECISION.md` | Agents — answers, verdicts, token values, implementation checklist |

`DECISION.md` is plain Markdown on purpose. Hosted preview links often cannot be fetched by other tools, and a decision needs to outlive the session that made it.

## Install

**Claude Code** — copy the folder into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`), then invoke with `/link-design-pitch`.

**Codex or any other agent** — the skill is plain Markdown. Point at it from your project's `AGENTS.md`:

```markdown
Design direction undecided or under review? Follow <path>/link-design-pitch/SKILL.md
```

See [`AGENTS.md`](AGENTS.md) for the agent-facing summary.

## Layout

```
link-design-pitch/
├── SKILL.md                    the procedure
├── AGENTS.md                   agent-facing entry point
└── references/
    ├── directions.md           18 directions with concrete signatures
    ├── feasibility.md          what each platform can actually render
    └── board.md                how to build the boards
```

`references/feasibility.md` covers Qt/QSS, web, SwiftUI, Compose, React Native, terminal, email, print, and slides — including which directions have a single point of failure and die without it.

## When to run it

Before the code exists, midway through, or on software that already ships. Phase 0 of `SKILL.md` explains how the constraints differ at each entry point — a redesign of shipping software has to count the existing color literals first, because that number is the real cost of a theme swap and the owner deserves it before choosing.
