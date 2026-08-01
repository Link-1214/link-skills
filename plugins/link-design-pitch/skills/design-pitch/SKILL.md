---
name: design-pitch
description: Pitch visual design directions the way a design studio does — interview the owner with five questions, present ten distinct directions rendered with their real content, compare trade-offs and technical feasibility, recommend one, and after they pick, produce the detailed screen-by-screen spec. Use this whenever the user wants design options, mockups, a visual direction, a theme, a restyle, a "make it look better", a color scheme, or says the current UI feels bland/dated/generic — and equally when they are starting a new interface from scratch, midway through building one, or redesigning something that already ships. Reach for it before writing any styling code on a project whose look has not been decided.
---

# Design Pitch

A studio does not open with a single comp and hope. It interviews the client, puts ten directions on the wall, argues the trade-offs out loud, recommends one, and only then draws the thing in detail.

That sequence exists because the expensive mistake in design work is not picking the wrong style — it is discovering, three days into implementation, that the style could never have worked here. Ten cheap directions surface that on day one.

Run the phases in order. Do not skip ahead to a favorite.

## Phase 0 — Read the ground first

Before asking anything, find out what you are designing *into*. Two things decide whether a direction is even eligible:

**What renders here.** A browser can do anything. Qt's stylesheets silently ignore `box-shadow` and `backdrop-filter`. Email clients drop flexbox. Print has no dark mode. Pitching glassmorphism at a PySide6 app wastes everyone's time, and the failure is silent — the property parses, nothing happens, and you find out from a screenshot. Read `references/feasibility.md` and identify the target platform. If you can, verify rather than trust: render one throwaway element using the risky property and look at it.

**What already exists.** This skill runs at three different moments and the constraints differ:

| Entry point | What changes |
|---|---|
| Before code | Everything is open. Pitch widely. |
| Mid-build | Layout and component structure are usually fixed. Pitch color, type, density, and hierarchy — say plainly which directions would require restructuring. |
| Redesign of shipping software | Something works today. Find out what people rely on before proposing to remove it. Count the existing color literals — that number is the real cost of a theme swap, and the owner deserves to know it before choosing. |

State which entry point you are at in one line. It changes what you should recommend, and the owner should see that you noticed.

## Phase 1 — The five questions

Ask all five in one pass. Dripping them one at a time makes the owner do five rounds of context-switching for information you could have gathered at once.

Answer from context where you honestly can — if the conversation already told you who this is for, fill it in and ask them to confirm rather than pretending not to know. Asking a question you already know the answer to reads as procedure, not attention.

**1. Who is this for?**
Push past "users". The gap between *someone who opens this every morning for eight years* and *someone who has thirty seconds and has never heard of you* is the single largest determinant of the right answer. Daily-use tools earn their keep by disappearing; first-impression pages earn theirs by landing. Offer two or three concrete archetypes drawn from what you know of the project.

**2. What kind of page or screen is it?**
Dashboard, landing page, app screen, form or wizard, document/report, marketing site, admin tool, storefront, editor. Offer the plausible ones as choices. This governs information density and how much decoration the page can carry before it interferes.

**3. What is the core color?**
Never ask this open-ended — "what color do you like" produces a hex code with no reasoning attached and it will fight the content later. Offer four concrete palettes **derived from answers 1 and 2**, each with real hex values and one line on what it does. A daily-use tool wants low saturation because eyes sit in it for hours; a landing page can carry a loud accent because the visit is brief. Include the owner's existing brand color if there is one. Let them override with their own — just make sure a reasoned default is on the table.

**4. What layout?**
Offer choices, not an open question: bento grid (cell size encodes importance), sidebar + content, single-column scroll, three-pane, card grid, hero + stacked sections, split screen. Say in one line what each is good at. If the project already has a layout and changing it is expensive, say so here rather than letting them pick something that quietly means a rewrite.

**5. What is the one action this must drive?**
The most important question and the one people skip. Every screen has exactly one thing it is trying to get someone to do — start the trial, approve the batch, notice the anomaly, publish the post, understand what changed this month. Not three things.

This answer sets the visual hierarchy for everything downstream. **The one action gets the most weight — the largest cell, the strongest contrast, the position the eye lands on first — and everything else deliberately defers to it.** A dashboard whose four numbers are the same size is asking the reader to decide where to look, which is the job you were supposed to do.

## Phase 2 — Ten directions

Pick ten from `references/directions.md`, which catalogs eighteen with their concrete signatures. Selecting ten from eighteen means the selection carries information: the owner should be able to tell that these ten were chosen *for them*.

Choose so the set actually spans the space — do not hand over ten flavors of restraint. Include:

- three or four that genuinely fit the answers
- two or three adjacent ones worth a look
- at least two that stretch — including one you expect to lose

The losers are not filler. Watching a direction get eliminated for a concrete reason ("Qt cannot blur behind a panel") teaches the owner more about their own constraints than five safe options do, and it makes the recommendation credible rather than arbitrary.

**All ten must be distinct directions. A combination is not one of the ten.** Several directions compose — a layout method sits happily under any color system — and the combination is very often the right answer. But putting "dark + bento" in a slot means the board covers nine ideas with ten panels, and the coverage you gave up is exactly the stretch option that would have taught the owner something. Combining belongs in Phase 3, where you are already reasoning about what fits. Keep Phase 2 for surveying the space.

**Render each one with the project's real content.** Real labels, real numbers, the real navigation. Lorem ipsum and fake KPIs hide the only thing that matters — whether the style survives contact with actual data. A five-cell bento looks great until the real screen has nineteen fields.

Write the board to `design-pitch/01-directions.html` — one self-contained HTML file, no external requests, each direction as a working mini-mockup with a heading and its number. Consistent framing across all ten (same content, same size) is what makes them comparable; if each is a different scene the owner is comparing scenes, not styles.

Read `references/board.md` for the board's structure.

## Phase 3 — Trade-offs and the recommendation

A wall of pretty pictures pushes the decision back onto the owner. Do the analytical work.

For each of the ten give: what it is good at, what it costs, and whether it can actually be built here. Put it in a table so they can scan it. Be specific about the cost — "hard to maintain" is noise; "every new card needs two hand-tuned shadows, so the fifteenth one will not match" is a reason.

Then recommend **one answer**, in a short paragraph that says what it does for *this* audience and *this* action.

That answer is often a **composition of two of the ten** rather than a single panel — a layout method under a color system, a density stance inside an editorial frame. When it is, name the two by their numbers so the owner can see where it came from, and render the composite as one extra panel *after* the ten, clearly labelled as a combination. It is an eleventh picture, not an eleventh direction; the ten stay a survey of the space, and this is the proposal drawn from it.

Name the strongest objection to your own recommendation and answer it. If you cannot find one, you have not looked.

Then stop and let the owner choose. This is their call, and the pause is the point of the whole exercise.

## Phase 4 — The detailed spec

Once they pick, produce the real thing.

**Every screen, not one.** A direction that works on the landing screen and falls apart on the settings form is not a direction. Draw them all — for a four-tab app, four screens.

For each screen, name the element that carries the Phase 1 action and make it visibly dominant. Say in one line why it earns that position. This is where the answer to question 5 pays off; if you cannot point at the dominant element on each screen, the hierarchy is not doing anything.

Include the full token set — ground, surface, border, text at each level, accent, semantic colors, the ordinal scale if the data has ranks. Actual hex values, not adjectives. Anyone implementing this should never have to invent a color.

**Then measure the hierarchy rather than trusting your eye.** Dominance is a claim about area, and in a grid it inverts silently — a chart spanning two rows quietly outgrows the hero you carefully placed, and the screen ends up answering a different question than the one you intended. Compute each cell's rendered area, confirm the hero really is the largest, and aim for roughly 1.3× the runner-up so the lead reads at a glance instead of measuring out to a near-tie. Check overflow in the same pass; a hero that clips its own sentence is worse than one that is merely small.

Measure contrast while you are there. Body and muted text against their actual ground, against 4.5:1 — muted labels are usually the smallest text on the screen and therefore need *more* contrast, not less, which is exactly where shipped designs tend to fail. If the current design fails and the proposed one passes, that is a finding worth stating plainly: it turns "looks bland" from a matter of taste into a measurement.

Then the part everyone forgets: **what actually has to change in the code.** Grep the target for hardcoded color literals and count them. A theme that looks like a stylesheet swap is usually not — chart libraries, canvas backgrounds, conditional table formatting, and inline styles live outside the stylesheet and stay stubbornly light while everything around them goes dark. List the specific places with file and line. If the count is large, say that a token layer should land first as a no-visual-change step, because that is the only way to make the swap reversible.

Write to `design-pitch/02-detail-<direction>.html`.

## Output: leave a plain-text record

Alongside the HTML, always write `design-pitch/DECISION.md`. HTML boards are for humans; other agents — and you, in a later session with none of this context — need something readable without a browser. Hosted preview links are worse still, since a different tool often cannot fetch them at all.

```markdown
# Design Pitch — <project>
Date · Entry point (before/mid/after) · Target platform

## Answers
1. Audience · 2. Page type · 3. Core color · 4. Layout · 5. The one action

## Directions considered
| # | Direction | Fit | Feasible | Verdict |

## Recommended → Chosen
What was recommended, what the owner chose, and why if it differed.

## Tokens
Every value as hex.

## Implementation
Ordered checklist with file paths and line numbers. Note what must not change.
```

Keep it current if the direction shifts later. A stale decision record is worse than none, because the next agent will believe it.

## Working notes

**Match the owner's language.** Reply in whatever language they are using. The reference files are English; the pitch does not have to be.

**Stay tool-agnostic.** Ask questions however this harness asks questions; write files with whatever writes files. If a structured multiple-choice prompt is available, use it for questions 2 through 4 where the answers are enumerable. If a hosted-preview tool is available, publishing the board is a nice extra — but the local HTML file is the deliverable and it must stand on its own.

**Ten real ones beats three real and seven sketched.** If the content is heavy, simplify what each mini-mockup shows — but keep all ten at the same fidelity. Uneven effort reads as a thumb on the scale.

**Do not pitch what you cannot build.** Checking feasibility before the board goes up, rather than after they fall for something impossible, is the whole reason Phase 0 comes first.
