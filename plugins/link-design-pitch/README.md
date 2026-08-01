# link-design-pitch

```bash
claude plugin install link-design-pitch@link-skills
```

Invoked as `link-design-pitch:design-pitch`, or automatically whenever the visual direction of an
interface is undecided or under question.

---

## What it does

A studio does not open with a single comp and hope. It interviews the client, puts ten directions on
the wall, argues the trade-offs out loud, recommends one, and only then draws the thing in detail.

That sequence exists because the expensive mistake in design work is not picking the wrong style —
it is discovering, three days into implementation, that the style could never have worked here. Qt
silently ignores `backdrop-filter`. Email clients drop flexbox. The chart library keeps its own
white background no matter what the theme says. Ten cheap directions surface that on day one.

## When to reach for it

- Starting an interface and the look is undecided
- Midway through, and it works but looks generic
- Redesigning something that already ships
- Any time someone says the UI feels bland, dated, or "off" and nobody can say why

It behaves differently at each of those entry points. A redesign counts the existing color literals
first, because that number is the real cost of a theme swap and you deserve it before choosing.

## How it runs

**Phase 0 — read the ground.** Identify the target platform and what it can actually render, then
survey what already exists. Directions that cannot be built are eliminated here, not after you fall
for one.

**Phase 1 — five questions, asked in one pass.**

| | |
|---|---|
| 1 | Who is this for? |
| 2 | What kind of page or screen is it? |
| 3 | What is the core color? — answered with reasoned palettes, never an open prompt |
| 4 | What layout? — offered as choices |
| 5 | **What is the one action this must drive?** |

Question five is the one people skip and the one that matters most. Every screen is trying to get
someone to do exactly one thing, and that answer decides what gets the largest cell, the strongest
contrast, and the position the eye lands on first. A dashboard whose four numbers are the same size
is asking the reader to decide where to look — which was the screen's job.

**Phase 2 — ten directions**, chosen from a catalog of twenty-four and rendered with your real
content, at identical size and framing so only the style varies. Two or three that fit, a couple
worth a look, and at least two that stretch — including one expected to lose, because watching a
direction get eliminated for a concrete reason teaches you more about your own constraints than five
safe options do.

**Phase 3 — trade-offs and a recommendation.** What each is good at, what it costs, whether it can
be built here. Then one recommendation, plus the strongest objection to it, answered. Often the
answer is a *combination* of two of the ten — that gets drawn as an eleventh panel, never as one of
the ten, because a combination in a slot silently costs you a whole direction of coverage.

Then it stops and waits. The choice is yours; the pause is the point.

**Phase 4 — the detailed spec.** Every screen, not one. Full token set as hex values. Hierarchy and
contrast *measured* rather than asserted — dominance is a claim about area and it inverts silently
when a chart spans two rows. Then the part everyone forgets: what actually has to change in the
code, with file paths and line numbers.

## What you get

Three files, placed where your project already keeps documentation (`docs/design/` if `docs/`
exists, otherwise `design/`):

| File | Audience |
|---|---|
| `01-directions.html` | People — the ten-direction board, self-contained, opens from disk |
| `02-detail-<direction>.html` | People — every screen in the chosen direction |
| `DECISION.md` | **Agents** — answers, verdicts, measurements, token values, implementation checklist |

`DECISION.md` is plain Markdown on purpose. Hosted preview links often cannot be fetched by other
tools, and a decision has to outlive the session that made it.

## What it will not do

- It will not pitch something your platform cannot render. Feasibility is checked in Phase 0.
- It will not narrow its options to match your past picks. A pitch that learns what you always
  choose stops showing you the option you would not have chosen, which is the whole value.
- It will not decide for you. It recommends, states the best argument against its own
  recommendation, and waits.

## Reference files

Loaded on demand rather than all at once.

| File | Holds |
|---|---|
| `skills/design-pitch/references/directions.md` | The catalog — 24 directions with concrete palettes, type stances, and failure modes |
| `skills/design-pitch/references/feasibility.md` | What Qt/QSS, web, SwiftUI, Compose, React Native, terminal, email, print, and slides can each actually render |
| `skills/design-pitch/references/board.md` | How the boards are built, and why identical framing is non-negotiable |

## Worked example

The first public example lands here after the next run on a fresh project. Until then, the reference
files above show the shape of what gets produced.
