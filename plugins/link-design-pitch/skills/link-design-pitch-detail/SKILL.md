---
name: link-design-pitch-detail
description: Apply an already-chosen visual direction to every real surface — full token set, hierarchy and contrast measured rather than asserted, and the list of code changes the theme actually requires — then present interaction options with their trade-offs for the owner to choose from. Use this after link-design-pitch has settled on a direction and the actual features or content exist, when the user asks to apply the design, spec the screens, produce the detail mockups, or decide the interaction model. Refuses to run without a design record naming a chosen direction; run link-design-pitch first in that case.
---

# Design Pitch — applying the direction

`link-design-pitch` chose a direction. The owner then built the real thing. This skill applies the
direction to what now exists, and lays out the interaction options.

It is deliberately a separate run because **building sits between the two**. Trying to spec surfaces
before the content exists means guessing at it, and the guess is usually wrong in exactly the way
that matters — field counts, label lengths, how many rows there really are.

## Refuse to start without a decision

Before anything else, find the design record: `docs/design/DECISION.md`, or `design/DECISION.md`.
That path is `<output>` below.

**If it does not exist, or its `Status` is not a chosen direction, stop and say so.** Point at
`link-design-pitch` and end the run. Do not improvise a direction — the whole value of the first
skill is that ten options were surveyed and one was chosen with reasons. Inventing one here silently
throws that away, and the owner will not know it happened.

Read the record fully before starting. It carries the five answers, the tokens, the measurements,
and — most usefully — what was rejected and why. Applying a direction while contradicting the reason
it was chosen is the most common way this goes wrong.

## Phase 4 — Spec the chosen direction

**Every distinct surface, not one.** A direction that works on the landing view and falls apart on
the settings form is not a direction. For a four-tab app, four screens. For a deck, the layouts that
actually differ. For a spreadsheet, the sheet types.

For each surface, name the element carrying the record's **one action** and make it visibly
dominant, with one line on why it earns that position.

**Measure the hierarchy rather than trusting your eye — but measure the right channel.** Dominance
is usually a claim about area, and area inverts silently: an element spanning two rows quietly
outgrows the hero you placed, and the surface ends up answering a different question than intended.
Compute rendered areas, confirm the hero is largest, aim for roughly 1.3× the runner-up.

**Some designs carry hierarchy in contrast rather than area, and then area is the wrong thing to
measure.** A board that deliberately keeps every column the same size and lifts one card by
sharpness has a dominance ratio of 1.00× and is working exactly as intended. Name which channel this
design uses before measuring, and measure that one. Reporting 1.00× as a failure when the design
never claimed area is how you end up "fixing" something that was right.

**Measure contrast too**, against 4.5:1 — including the elements you deliberately pushed back.
De-emphasis is the most common way an interface quietly fails accessibility: dimming other people's
content to 50% opacity reads as tasteful and lands at 3.5:1, and that content is still something
someone has to read. Compute the *effective* contrast after opacity compositing, not the nominal
color pair. Where it fails, raise the opacity until it passes and check the gap still carries the
hierarchy — usually it does, by a wide margin.

Muted labels are the other reliable failure: they are the smallest text and therefore need *more*
contrast, not less.

Carry the token set forward from the record as literal values. If you add a token the record does
not have, append it there too — the record stays the single source of truth.

Then the part everyone forgets: **what has to change in the code.** Grep for hardcoded color
literals and count them. A theme that looks like a stylesheet swap usually is not — chart libraries,
canvas backgrounds, conditional formatting, and inline styles live outside the stylesheet and stay
stubbornly light while everything around them goes dark. List places with file and line. If the
count is large, say a token layer should land first as a no-visual-change step, because that is the
only way to make the swap reversible.

Write to `<output>/02-detail-<direction>.html` and capture `<output>/02-detail-<direction>.png`.
Read `references/spec.md` for how to build and verify it in one pass.

### If the owner does not like it

Say plainly that the direction is not working on real content, and that the fix is to go back and
choose again — `link-design-pitch`, with what you learned as input. Do not iterate the styling here
hoping to rescue it. A direction that fails on the real surfaces was the wrong direction, and
patching it produces something that is neither the chosen direction nor a considered alternative.

## Phase 5 — Interaction options, presented not built

**Skip entirely when the deliverable does not move**: a slide deck, a spreadsheet, a printed report,
a document handed over as a file. Say you are skipping it and why, and end the run.

For anything a person operates, the interaction model is a set of forks with real consequences, and
defaulting silently is how a product ends up inconsistent with itself — one screen optimistic and
another confirmed, one autosaving and another not, and nobody remembers deciding either.

**Present the options. Do not build them.**

This is a hard limit and it is about cost. A full state and behavior specification costs more than
everything else in both skills combined, and it is discarded the moment the owner names a model you
did not anticipate — which has happened: a spec written around "optimistic vs confirmed" was
invalidated by a third answer (stage the changes, apply them together) in one sentence.

So the deliverable of this phase is **a comparison, not a specification**:

- The two or three forks that actually bite for this artifact — not all of them. `references/behavior.md`
  lists the candidates; the record's **one action** tells you which sit on the path that matters.
- For each: the options, what each buys, what each costs, and what it obliges you to design later.
- A recommendation with the reason.
- Then ask, and record the answers in `DECISION.md`.

Keep it to a table and a few sentences per fork. If you find yourself drawing screens, you have
crossed the line.

**Leave the states list as a checklist, not drawings.** `references/behavior.md` has the states that
actually occur — empty, filtered-to-nothing, loading, partial, overflow, long content, read-only,
stale. Name which apply here and which do not, in one line each. Whoever builds it needs to know the
list exists; they do not need ten more mockups from you.

**Watch for answers outside your axis.** When the owner answers with something you did not offer,
that is the most valuable thing that happens in this phase — it means the fork was framed too
narrowly. Record the model they described in their words, and list what it newly makes undecided.
Do not force it back onto your two options.

## Output

Appended to what the first skill produced:

| File | Audience |
|---|---|
| `<output>/02-detail-<direction>.html` | People — the direction across every surface |
| `<output>/02-detail-<direction>.png` | Anywhere HTML does not render — GitHub, chat, an agent with vision |
| `<output>/DECISION.md` | Updated in place — measurements, interaction answers, implementation list |

Add to the record:

Sections to append: **Detail — measurements** (hierarchy channel with its numbers, contrast
including de-emphasized elements, anything that had to change to pass with before and after) ·
**Interaction** (the forks put to the owner and what they chose; if they answered outside the
options, their model in their words and what it leaves undecided; the states that apply, as a list,
not drawn) · **Implementation** (ordered, with paths and lines, noting what must not change) ·
**Status**.

**Keep the record true.** A checklist written as future work stays that way forever unless someone
changes it. Before treating this record as a plan, check whether the code already reflects it — grep
for the tokens, look for the files the checklist names. This has already cost one round of
duplicated work: a checklist said *pending* while every item had shipped.

## Working notes

**Match the owner's language.** Reply in whatever language they are using.

**Stay tool-agnostic.** Ask questions however this harness asks questions; write files with whatever
writes files.

**The record is the contract.** Everything you produce here is an application of a decision made
elsewhere. When something in the record turns out to be wrong on real content, say so and update the
record — do not quietly design around it.
