# link-design-pitch

```bash
claude plugin install link-design-pitch@link-skills
```

One install, **two skills**. They are separate runs because building the actual thing sits between
them.

| | Invoked as | Does |
|---|---|---|
| **1** | `link-design-pitch:link-design-pitch` | Five questions → ten directions with your real content → recommend → **stops for your choice** |
| | *you build the features and content* | by hand or with another agent |
| **2** | `link-design-pitch:link-design-pitch-detail` | Applies the chosen direction to every surface, then presents interaction options |

The second refuses to run without a chosen direction on record. Run the first one.

---

## Why the split

One long run spanning the build would either stall waiting for content or guess at it — and the
guess is wrong in exactly the way that matters: field counts, label lengths, how many rows there
really are. So the first skill stops at the choice and writes `DECISION.md`; the second picks up
from that file when the thing exists.

It also keeps each run cheap. You can re-apply a direction, or go back and choose a different one,
without redoing the other half.

## Skill 1 — choosing a direction

**Phase 0 — read the ground.** What the target can actually render, and what already exists.
Directions that cannot be built are eliminated here, not after you fall for one.

**Phase 1 — five questions, in one pass.**

| | |
|---|---|
| 1 | Who is this for? |
| 2 | **What are you actually producing?** — web app, desktop app, deck, spreadsheet, report |
| 3 | Core color — answered with reasoned palettes, never an open prompt |
| 4 | Layout — offered as choices |
| 5 | **The one action this must drive** |

Question 2 decides what can be rendered, how dense a surface can be, and whether the interaction
step applies at all. Question 5 decides the hierarchy for everything downstream.

**Phase 2 — ten directions** from a catalog of twenty-four, rendered with your content at identical
size and framing so only the style varies. Some fit, some stretch, at least one is expected to lose
— watching a direction get eliminated for a concrete reason teaches you more about your constraints
than five safe options do.

**Phase 3 — trade-offs, a recommendation, the strongest objection to it answered — then it stops.**
The recommendation is whatever fits: sometimes one of the ten unchanged, sometimes two composed.
Neither is the default.

## Skill 2 — applying it

**Phase 4 — every distinct surface**, full token set, and hierarchy and contrast *measured* rather
than asserted. Dominance is a claim about area and it inverts silently; and de-emphasis is the most
common way an interface quietly fails accessibility, since dimming to 50% opacity reads as tasteful
and lands below the readable threshold. Then the part everyone forgets: what actually has to change
in the code, with paths and lines.

**Phase 5 — interaction options, presented not built.** Skipped entirely for decks, spreadsheets and
print. Otherwise: the two or three forks that actually bite here, what each buys and costs, a
recommendation — then it asks. **No state mockups, no behavior spec.** That work is discarded the
moment you name a model that was not on the list, which has already happened once.

## What you get

Placed where your project already keeps documentation (`docs/design/` if `docs/` exists, otherwise
`design/`):

| File | From | Audience |
|---|---|---|
| `01-directions.html` | skill 1 | People — the ten-direction board |
| `01-directions.png` | skill 1 | Agents with vision — the styles as a picture |
| `02-detail-<direction>.html` · `.png` | skill 2 | People, and agents with vision |
| `DECISION.md` | both | **Everyone else** — answers, verdicts, measurements, tokens, checklist |

`DECISION.md` is plain Markdown on purpose. Hosted preview links often cannot be fetched by other
tools, and a decision has to outlive the session that made it. It is also the contract between the
two skills.

## What it will not do

- Pitch something your platform cannot render. Feasibility is checked before the board goes up.
- Narrow its options to match your past picks. A pitch that learns what you always choose stops
  showing you the option you would not have chosen, which is the whole value.
- Decide for you. It recommends, states the best argument against its own recommendation, and waits.
- Build the interaction model. It lays out the options and asks.

## Reference files

Loaded on demand rather than all at once.

| File | Holds |
|---|---|
| `skills/link-design-pitch/references/directions.md` | The catalog — 24 directions with palettes, type stances, failure modes, and a ready-made token line each |
| `skills/link-design-pitch/references/feasibility.md` | What Qt/QSS, web, SwiftUI, Compose, React Native, terminal, email, print and slides can each actually render |
| `skills/link-design-pitch/references/board.md` | Building and verifying the board |
| `skills/link-design-pitch-detail/references/spec.md` | Building the per-surface file, plus five measurement traps that have each produced a wrong finding |
| `skills/link-design-pitch-detail/references/behavior.md` | The interaction forks worth asking about, and the states checklist |

## Worked example

The first public example lands here after the next run on a fresh project.
