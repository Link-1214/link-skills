---
name: link-design-pitch
description: Pitch visual design directions the way a design studio does — interview the owner with five questions including what they are actually producing, present ten directions rendered with their real content, compare trade-offs and what the target can actually render, recommend one, then stop and let them choose. Use this whenever the user wants design options, mockups, a visual direction, a theme, a restyle, a "make it look better", a color scheme, or says the current thing feels bland/dated/generic. Works for any deliverable — a web or desktop app, a slide deck, a spreadsheet, a document, a printed report. Reach for it before writing any styling code on a project whose look has not been decided. Applying the chosen direction to real screens comes later, from link-design-pitch-detail.
---

# Design Pitch — choosing a direction

A studio does not open with a single comp and hope. It interviews the client, puts ten directions on
the wall, argues the trade-offs out loud, recommends one — **and then stops and lets the client
choose.**

That sequence exists because the expensive mistake in design work is not picking the wrong style. It
is discovering, three days into implementation, that the style could never have worked here. Ten
cheap directions surface that on day one.

**Surface** below means whatever the thing is: a screen, a page, a slide layout, a sheet, a printed
section. The procedure does not assume software.

## Where this sits

| Step | Who |
|---|---|
| **1. Five questions → 2. ten directions → recommend → stop for the choice** | **this skill** |
| 3. Build the actual features and content | the owner, by hand or with another agent |
| 4. Apply the direction to every real surface → 5. offer interaction options | `link-design-pitch-detail` |

The split exists because **building sits between choosing a direction and applying it.** One long run
spanning the build would either stall waiting or guess at content that does not exist yet. Finish
this skill's job, write `DECISION.md`, and stop. The detail skill picks up from that file.

## The mandatory pause

Phase 3 ends by asking which direction they want, and **this skill ends there.** Do not write
per-surface specs, detail mockups, or interaction behavior — that is the other skill, and it runs
after the thing exists.

Running past the pause takes the decision away from the person whose decision it is, and burns
effort on a direction they may not pick.

## Phase 0 — Read the ground first

**What renders here.** A browser can do anything. Qt's stylesheets silently ignore `box-shadow` and
`backdrop-filter`. Email clients drop flexbox. Print has no dark mode. Pitching glassmorphism at a
PySide6 app wastes everyone's time, and the failure is silent — the property parses, nothing
happens, and you find out from a screenshot.

`references/feasibility.md` opens with a platform index and two cross-platform tables. **Read those,
then read only the section for this target** — the other six are detail for deliverables you are not
building. Where you can, verify rather than trust: render one throwaway element with the risky
property and look at it.

**What already exists.** Three entry points, different constraints:

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

## Phase 1 — The five questions

Ask all five in one pass. Dripping them one at a time makes the owner context-switch five times for
information you could have gathered at once.

Answer from context where you honestly can — if the conversation already told you who this is for,
fill it in and ask them to confirm. Asking something you already know reads as procedure, not
attention.

**1. Who is this for?** Push past "users". The gap between *someone who opens this every morning for
years* and *someone who has thirty seconds and has never heard of you* is the single largest
determinant of the right answer. Offer two or three concrete archetypes.

**2. What are you actually producing?** Not "what kind of page" — the **deliverable format**. A web
app, a desktop app, a mobile app, a slide deck, a spreadsheet, a document, a printed report, an
email. Ask it plainly and offer the plausible ones.

This one answer decides three things at once: what can be rendered at all, how dense a surface can
be, and whether the detail skill's interaction step applies later at all. A spreadsheet and a web
app deserve different tens, and asking after you have already picked the ten is too late.

**3. What is the core color?** Never open-ended — "what color do you like" produces a hex with no
reasoning attached and it will fight the content later. Offer four concrete palettes **derived from
answers 1 and 2**, with real values and one line each on what they do. Include the owner's existing
brand color if there is one. Let them override; just put a reasoned default on the table.

Asked in one pass, answers 1 and 2 do not exist yet when you write these palettes. Derive them from
your best reading of the context and **say which reading each palette assumes** — a palette whose
premise is visible gets corrected in the same breath as the answer, instead of silently anchoring
the wrong one.

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

### What the answers switch on

Read the five answers for two things beyond their face value.

**If question 5 is about understanding rather than doing** — notice the anomaly, see what changed,
grasp where it stands — then the surface should say it in a sentence, not lay out figures and leave
the reading to the viewer. Four numbers at equal size make the reader do the work the surface was
supposed to do.

**If questions 2 or 5 involve the product acting on the user's behalf** — generating, suggesting,
approving, running by itself — note it for the detail skill, whose interaction forks then include
what the product's own work looks like while it runs. If nothing does, that fork does not exist here
and raising it only adds noise. Most dashboards, forms and documents do not.

## Phase 2 — Ten directions

`references/directions.md` opens with an index — what each direction is good at, where it breaks,
and which die without a property this target may lack. **Read the index, pick ten, then pull only
those ten entries: search for each `## <number>.` heading and read just that line range.** The
entries carry the token line and the type and shape signature, which rendering needs but choosing
does not, and the ones you drop never appear in the output — reading them is pure cost. If your
file tool can only return whole files, read the file once and never a second time.

**The mockups are written as HTML and CSS, not sourced.** Do not search for reference images. The
catalog already carries the palette and the shape language, and a found image cannot contain this
project's own content — which is the only thing the board is actually testing.

**When the target is not a browser, the board is a rendering approximation.** Phase 0 already
removed what the target cannot draw at all; what remains — font rasterization, native widget chrome
— differs in detail. Say so on the board rather than letting the owner take it as a screenshot.

**Assemble from the catalog rather than inventing values** — the palettes are already worked out,
and re-deriving them drifts between runs, which makes two boards stop being comparable.

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
ipsum hides the only thing that matters — whether the style survives contact with actual data.

Write to `<output>/01-directions.html`. Read `references/board.md` for structure, for how to verify
it in one pass rather than six, and for how to capture the PNG.

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
option to combine differently. Record the answer in `DECISION.md` and end the run.

## Output

| File | Audience |
|---|---|
| `<output>/01-directions.html` | People — the board, self-contained, opens from disk |
| `<output>/01-directions.png` | **Anywhere HTML does not render** — GitHub, chat, an agent with vision |
| `<output>/DECISION.md` | **Everyone else**, and the handoff to the detail skill |

The three files do different jobs and each is the cheapest at its own. **HTML** is for a person with
a browser, where the type renders at real size. **The PNG** is for every other place a person or an
agent might look — a repository page, a chat message, a phone — because none of those render HTML.
It costs nothing extra, since you already render the board to verify it. **`DECISION.md`** is what
anything reads to *reproduce* the design; measured on a real project it did that at roughly a third
the cost of reading the HTML, and the HTML would not have been enough on its own anyway.

PDF was considered and rejected: it is generated *from* HTML, so it is strictly more work for the
same reach.

**`DECISION.md` is the contract with `link-design-pitch-detail`, which refuses to run without it.**
Write it even if the session ends before a choice is made — with `Status: Awaiting choice`.

Sections, in this order: **Answers** (the five, verbatim) · **Directions considered** (a table with
good-at, cost, feasibility, verdict) · **Measurements** (numbers, not adjectives) · **Recommended →
Chosen** · **Tokens** (every value literal) · **Status** (`Direction chosen: <name>` or
`Awaiting choice`).

**Record divergence.** If they picked something other than your recommendation — or gave an answer
outside the options you offered — write what and why. That gap is the highest-information thing in
the document; it usually says your options were too narrow. Agreement teaches nobody anything.

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
