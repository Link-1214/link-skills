# Building the boards

Two HTML files: the ten-direction board (Phase 2) and the detail spec (Phase 4). Both are self-contained — inline every style, embed any asset as a data URI, make no external request. They must open from disk, be readable by another agent, and survive being emailed to someone.

## The comparison rule

The board's only job is to make ten things comparable. Comparison dies the moment the variables multiply, so hold everything constant except style: **same content, same size, same crop, same order of elements in every panel.**

If panel 3 shows a settings screen and panel 7 shows a landing hero, the owner is choosing between scenes, not styles, and will pick based on which content they happen to like. Pick one representative screen — usually the one carrying the Phase 1 action — and render that same screen ten times.

Same applies to effort. Ten at equal fidelity beats three polished and seven sketched; uneven detail reads as a thumb on the scale, and the owner will sense they are being steered.

The ten are ten **distinct** directions. If the recommendation turns out to be a combination of two of them, that composite is an eleventh panel placed after the ten and labelled as such — never one of the ten. A combination in a slot costs a whole direction of coverage, and the one it displaces is usually the stretch option that would have been most informative.

## Ten-direction board

Per panel:

1. **Number and name** — `01 / 10`, the direction name in the owner's language with the English term beneath. The count tells them where they are; the pairing keeps the term searchable.
2. **The mockup** — the project's real screen at a fixed frame size, styled in this direction. Real labels, real numbers, real navigation.
3. **One line of signature** — ground, accent, type stance. Enough to recognize what makes it this and not that.
4. **A feasibility badge** — `가능` / `부분` / `불가` (or the equivalent), with the blocking property named when it is not fully possible. Putting this on the panel itself, rather than only in the table below, stops someone falling for an impossible option while scrolling.

Then, if the recommendation composes two of them, the composite panel — same frame, same content, headed with the two source numbers (`05 + 06`) so its origin is visible.

Then the comparison table beneath: direction · good at · costs · feasible · verdict. One scannable row each, with the composite as a final marked row.

Then the recommendation as prose. Then the strongest objection to it, answered.

A layout that works: full-width stacked panels, each a titled block. Vertical stacking beats a grid here — side-by-side thumbnails are too small to judge type, and type is most of what separates these.

## Detail spec

Once a direction is chosen:

- **Every screen.** One panel per screen or tab, full size, real content.
- **Per screen: what dominates and why.** Name the element carrying the Phase 1 action in one line. If you cannot name it, the hierarchy is not working yet.
- **The token table.** Ground, surface, border, text (primary/secondary/muted), accent, semantic up/down, and any ordinal scale. Hex values, with a swatch beside each.
- **The implementation checklist.** File paths, line numbers, ordered. What must not change.

## Content

Use the project's actual content throughout. Lorem ipsum and placeholder numbers hide exactly the thing the board exists to test: whether the style survives real data. A five-cell bento is beautiful until the real screen has nineteen fields and three of the labels are long compound nouns.

If real data is sensitive, use synthetic values with the same *shape* — same magnitudes, same label lengths, same field count. Never real personal data on a file that may be shared.

## Theme

The board itself is a document about design, so it should not fight the designs it holds. Neutral chrome — near-white or near-black ground, restrained type, panels clearly framed. Let the panels carry the color.

If the harness has a preview or publish tool, publishing the board is a convenience. The local file is still the deliverable: hosted links often cannot be fetched by other tools, and the decision has to outlive the session.
