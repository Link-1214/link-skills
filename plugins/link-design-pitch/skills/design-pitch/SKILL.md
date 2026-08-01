---
name: design-pitch
description: Pitch visual design directions the way a design studio does — interview the owner with five questions, present ten directions rendered with their real content, compare trade-offs and what the target can actually render, recommend one, then stop and let them choose before speccing it in detail. Use this whenever the user wants design options, mockups, a visual direction, a theme, a restyle, a "make it look better", a color scheme, or says the current thing feels bland/dated/generic — and equally when they are starting from scratch, midway through building, or redesigning something that already ships. Works for any designed artifact, not just screens — web pages, app UIs, dashboards, slide decks, spreadsheets, printed reports. Reach for it before writing any styling code on a project whose look has not been decided.
---

# Design Pitch

A studio does not open with a single comp and hope. It interviews the client, puts ten directions on
the wall, argues the trade-offs out loud, recommends one — **and then stops and lets the client
choose.** Only after that does it draw the thing in detail.

That sequence exists because the expensive mistake in design work is not picking the wrong style. It
is discovering, three days into implementation, that the style could never have worked here. Ten
cheap directions surface that on day one.

**Surface** below means whatever the thing is: a screen, a page, a slide layout, a sheet, a printed
section. The procedure does not assume software.

## The two mandatory pauses

Everything else here is guidance. These two are the shape of the exercise.

| After | You stop and ask |
|---|---|
| **Phase 3** — the recommendation | Which direction do you want? |
| **Phase 5** — before speccing behavior | Which of these interaction choices? |

Running past a pause is the main way this goes wrong, and it goes wrong twice over: it takes the
decision away from the person whose decision it is, and it burns effort on detail for a direction
they may not pick. If you find yourself writing Phase 4 without an answer in hand, you have already
made their choice for them.

## Phase 0 — Read the ground first

**What renders here.** A browser can do anything. Qt's stylesheets silently ignore `box-shadow` and
`backdrop-filter`. Email clients drop flexbox. Print has no dark mode. Pitching glassmorphism at a
PySide6 app wastes everyone's time, and the failure is silent — the property parses, nothing
happens, and you find out from a screenshot. Read `references/feasibility.md`. Where you can, verify
rather than trust: render one throwaway element with the risky property and look at it.

**What already exists.** This runs at three different moments and the constraints differ:

| Entry point | What changes |
|---|---|
| Before any build | Everything is open. Pitch widely. |
| Mid-build | Structure is usually fixed. Pitch color, type, density, hierarchy — say which directions would require restructuring. |
| Redesign of something shipping | Something works today. Find out what people rely on. Count the existing color literals — that number is the real cost of a theme swap and the owner deserves it before choosing. |

**Where the output goes.** Put files where this project already keeps documentation: `docs/design/`
when a `docs/` directory exists, otherwise `design/` at the root. That path is `<output>` below.

Never name the folder after this skill. A folder called `design-pitch/` at the root of someone
else's repository says who made it rather than what is inside it. This is not hypothetical — it
happened, and the folder had to be moved.

State the entry point and the target in one line. It changes what you should recommend.

## Phase 1 — The five questions

Ask all five in one pass. Dripping them one at a time makes the owner context-switch five times for
information you could have gathered at once.

Answer from context where you honestly can — if the conversation already told you who this is for,
fill it in and ask them to confirm. Asking something you already know reads as procedure, not
attention.

**1. Who is this for?** Push past "users". The gap between *someone who opens this every morning for
years* and *someone who has thirty seconds and has never heard of you* is the single largest
determinant of the right answer. Offer two or three concrete archetypes.

**2. What kind of artifact is it?** Dashboard, landing page, app screen, form, report, deck,
spreadsheet, storefront, editor. This governs density, and whether Phase 5 applies at all.

**3. What is the core color?** Never open-ended — "what color do you like" produces a hex with no
reasoning attached and it will fight the content later. Offer four concrete palettes **derived from
answers 1 and 2**, with real values and one line each on what they do. Include the owner's existing
brand color if there is one. Let them override; just put a reasoned default on the table.

**4. What layout?** Offer choices, not an open question. Say in one line what each is good at. If
the project already has a layout and changing it is expensive, say so here rather than letting them
pick something that quietly means a rewrite.

**5. What is the one action this must drive?** The most important question and the one people skip.
Every surface is trying to get someone to do exactly one thing — start the trial, approve the batch,
notice the anomaly, find their next task.

This sets the hierarchy for everything downstream. **The one action gets the most weight** — the
largest cell, the strongest contrast, the position the eye lands on first — and everything else
defers to it. Four numbers at the same size ask the reader to decide where to look, which was the
surface's job.

If the answer creates tension with the artifact's conventional form — a kanban board whose job is
"find my next task" rather than "move cards" — name that tension. Resolving it *is* the design
problem, and papering over it produces something that is neither.

## Phase 2 — Ten directions

Pick ten from `references/directions.md`, which catalogs twenty-four with their signatures and a
ready-made CSS variable line for each. **Assemble from the catalog rather than inventing values** —
the palettes are already worked out, and re-deriving them each run is the largest avoidable cost in
this whole exercise.

Choose so the set spans the space:

- three or four that genuinely fit the answers
- two or three adjacent ones worth a look
- at least two that stretch — including one you expect to lose

The losers are not filler. Watching a direction get eliminated for a concrete reason teaches the
owner more about their own constraints than five safe options do, and it makes the recommendation
credible rather than arbitrary.

**All ten must be distinct directions. A combination is not one of the ten.** Combining belongs in
Phase 3. Spending a slot on "dark + bento" means ten panels cover nine ideas, and what you gave up
is the stretch option that would have taught them something.

**Render each with the project's real content.** Real labels, real numbers, real navigation. Lorem
ipsum hides the only thing that matters — whether the style survives contact with actual data. A
five-cell layout looks great until the real thing has nineteen fields.

Write to `<output>/01-directions.html`. Read `references/board.md` for structure and for how to
verify it in one pass rather than six.

## Phase 3 — Compare, recommend, then stop

A wall of pretty pictures pushes the decision back onto the owner. Do the analytical work first.

For each of the ten: what it is good at, what it costs, whether it can be built here. In a table so
they can scan it. Be specific about cost — "hard to maintain" is noise; "every new card needs two
hand-tuned shadows, so the fifteenth will not match" is a reason.

Then recommend **one answer**, in a short paragraph saying what it does for *this* audience and
*this* action.

**Recommend whatever actually fits.** Sometimes that is one of the ten, unchanged. Sometimes it is
two composed — a layout method under a color system. Neither is the default. If every pitch you
produce ends in a combination, you are applying a habit rather than reading the situation. When it
*is* a combination, name the two by number and render the composite as one extra panel after the
ten, labelled as a combination.

Name the strongest objection to your own recommendation and answer it. If you cannot find one, you
have not looked.

**Then stop and ask which direction they want.** Offer the recommendation, the runners-up, and the
option to combine differently. Do not write a single line of Phase 4 until they answer.

## Phase 4 — Spec the chosen direction

**Every distinct surface, not one.** A direction that works on the landing view and falls apart on
the settings form is not a direction. For a four-tab app, four screens. For a deck, the layouts that
actually differ. For a spreadsheet, the sheet types.

For each surface, name the element carrying the Phase 1 action and make it visibly dominant, with
one line on why it earns that position.

**Measure the hierarchy rather than trusting your eye.** Dominance is a claim about area and it
inverts silently — an element spanning two rows quietly outgrows the hero you placed, and the
surface ends up answering a different question than intended. Compute rendered areas, confirm the
hero is largest, aim for roughly 1.3× the runner-up. Check overflow in the same pass.

**Measure contrast while you are there**, against 4.5:1. Muted labels are usually the smallest text
and therefore need *more* contrast, which is exactly where shipped designs fail. When comparing
across directions, compare the same element in each — measuring a highlighted item in one and a
plain item in another produces a number that means nothing. That has already produced a wrong
finding once.

Include the full token set as actual values, not adjectives. Anyone implementing this should never
have to invent a color.

Then the part everyone forgets: **what has to change in the code.** Grep for hardcoded color
literals and count them. A theme that looks like a stylesheet swap usually is not — chart libraries,
canvas backgrounds, conditional formatting, and inline styles live outside the stylesheet and stay
stubbornly light while everything around them goes dark. List places with file and line. If the
count is large, say a token layer should land first as a no-visual-change step, because that is the
only way to make the swap reversible.

Write to `<output>/02-detail-<direction>.html`.

## Phase 5 — Behavior: ask, then spec

**Skip entirely when the artifact does not move**: a printed report, a deck, a spreadsheet handed
over as a file. Say you are skipping it and why.

For anything a person operates, a mockup showing only the resting state is half a design. What sinks
builds is rarely the color — it is the states nobody drew. The empty view on day one. The list at
four hundred rows. The label that turned out to be a long compound noun. The save that failed after
the thing already moved.

**These are decisions, not deductions. Ask.** `references/behavior.md` lists the forks worth putting
to the owner — optimistic or confirmed, undo or confirm, inline or panel or modal, autosave or
explicit. Each has real consequences, and defaulting silently is how a product ends up inconsistent
with itself. Present the two or three that actually matter here, with a recommendation each, and let
them answer before you write the spec.

Two things anchor the spec once they have:

**The Phase 1 action gets the interaction budget.** Whatever the one thing is, that path gets the
responsiveness, the feedback, and whatever motion you spend. Everything else can be plain. Polish
spread evenly reads as no priority at all.

**Motion is constrained by Phase 0, not by taste.** If the platform has no transitions, specify the
instant version that still reads. A spec describing eased motion on a toolkit that cannot ease is a
spec that silently does not happen.

## Output

Four things in `<output>`:

| File | Audience |
|---|---|
| `01-directions.html` | People — the board, self-contained, opens from disk |
| `01-directions.png` | **Agents with vision** — they see the styles, not just the markup |
| `02-detail-<direction>.html` | People — the chosen direction across every surface |
| `DECISION.md` | **Everyone else** — answers, verdicts, measurements, tokens, checklist |

The PNG costs nothing extra: you already render the board to verify it, so capture it in the same
pass. HTML shows a style natively, which no other format does as cheaply — but an agent reading HTML
source sees markup, not a design. The picture closes that gap, and `DECISION.md` carries every value
in plain text for agents without vision. PDF was considered and rejected: it is generated *from*
HTML, so it is strictly more work for the same reach.

```markdown
# 시각 방향 결정 기록 — <project>
Date · Entry point · Target

## Answers
1. Audience · 2. Artifact · 3. Core color · 4. Layout · 5. The one action

## Directions considered
| # | Direction | Good at | Cost | Feasible | Verdict |

## Measurements
Whatever you measured, with the numbers.

## Recommended → Chosen
What was recommended, what they chose, and why if it differed.

## Tokens
Every value, literal.

## Behavior
The interaction choices they made, and what was deliberately left out.

## Implementation
Ordered, with paths and lines. Note what must not change.
```

### Keeping the record true

A stale record is worse than none, because the next agent will believe it.

**Record divergence.** If they picked something other than your recommendation, write what and why.
That gap is the highest-information thing in the document — it says what you misread. Agreement
teaches nobody anything.

**Mark implementation when it lands.** A checklist written as future work stays that way forever
unless someone changes it. Before treating a record as a plan, check whether the code already
reflects it. This has already cost one round of duplicated work: a checklist said *pending* while
every item had shipped.

## On memory and personalization

If the project or harness carries memory — a memory store, a `CLAUDE.md`, an earlier `DECISION.md` —
read it. Two things in it are genuinely reusable:

- **Vocabulary.** When an owner says "washed out" and it turned out to mean contrast rather than
  saturation, that translation holds. It is a decoding, not a preference.
- **Resolved constraints.** "Orange cannot mark the previous period here because it collides with
  the semantic palette" was worked out once and stays true.

**Never use memory to narrow the ten.** A pitch that learns which directions the owner rejects and
stops showing them has destroyed the reason it exists. The value is in the option they would not have
picked. Personalization optimizes for agreement; this exists to produce informed disagreement.

## Working notes

**Match the owner's language.** Reply in whatever language they are using. The reference files are
English; the pitch does not have to be.

**Stay tool-agnostic.** Ask questions however this harness asks questions; write files with whatever
writes files. If a structured multiple-choice prompt is available, use it for the enumerable
questions. If a hosted-preview tool is available, publishing is a nice extra — the local files are
the deliverable and must stand alone.

**Ten real ones beats three real and seven sketched.** If the content is heavy, simplify what each
mini-mockup shows — but keep all ten at the same fidelity. Uneven effort reads as a thumb on the
scale.

**Do not pitch what you cannot build.** Checking feasibility before the board goes up, rather than
after they fall for something impossible, is the whole reason Phase 0 comes first.
