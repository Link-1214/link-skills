# Building the boards

One self-contained HTML file: the ten-direction board. Inline every style, embed assets as data
URIs, no external requests. It must open from disk and survive being emailed to someone.

The per-surface detail spec is a different file built by a different skill — see
`link-design-pitch-detail`. This file covers the board only.

## Assemble, do not author

The single largest cost in a run is hand-writing ten palettes. Do not. `directions.md` ends with a
ready-made token line for each of the twenty-four, plus the few extra rules the shadow- and
blur-based ones need.

The structure that makes this cheap: **write the mockup markup once, and give each direction a
wrapper class that only redefines variables.**

```html
<div class="mock d-swiss">…markup…</div>
<div class="mock d-dark">…same markup…</div>
```

```css
.mock { --g:#fff; --s:#fff; --l:#E3E6E8; --t:#1B1F23; --t2:#6B7480; --ac:#2F6FED; --r:6px;
        background:var(--g); color:var(--t); }
.mock .card { background:var(--s); border:1px solid var(--l); border-radius:var(--r); }

.d-swiss { --g:#fff;--s:#fff;--l:#111;--t:#111;--t2:#6A6A6A;--ac:#D32F2F;--r:0 }
.d-dark  { --g:#0C1211;--s:#141D1B;--l:#25322F;--t:#E6EFEC;--t2:#8FA29D;--ac:#3FBF9C;--r:8px }
```

Emit the markup once and clone it — a small loop over a template string beats ten pasted copies,
because it makes "same content in every panel" structurally true instead of something you keep
having to check.

## The comparison rule

The board's only job is to make ten things comparable, and comparison dies the moment the variables
multiply. **Same content, same size, same crop, same element order in every panel.**

If panel 3 shows a settings view and panel 7 shows a landing hero, the owner is choosing between
scenes, not styles, and will pick based on which content they happen to like. Pick one
representative surface — usually the one carrying the Phase 1 action — and render that same surface
ten times.

Same applies to effort. Ten at equal fidelity beats three polished and seven sketched; uneven detail
reads as a thumb on the scale.

## Ten-direction board

Per panel:

1. **Number and name** — `01 / 10`, the direction in the owner's language with the English term
   beneath. The count tells them where they are; the pairing keeps the term searchable.
2. **The mockup** — the project's real surface at a fixed frame size, styled in this direction.
3. **One line of signature** — ground, accent, type stance.
4. **A feasibility badge** — possible / partial / impossible, naming the blocking property when it
   is not fully possible. On the panel itself, not only in the table below, so nobody falls for an
   impossible option while scrolling.

Then the comparison table: direction · good at · costs · feasible · verdict.

Then the recommendation as prose, then the strongest objection to it, answered. If the
recommendation composes two of the ten, that composite is an eleventh panel *after* the ten, headed
with its source numbers (`05 + 06`) — never one of the ten.

Full-width stacked panels beat a grid here. Side-by-side thumbnails are too small to judge type, and
type is most of what separates these.

## Verify in one pass

Render the board once and run a single script that returns everything. Six separate round-trips cost
real time and tokens for the same answer.

One call should return, per panel: frame height, element counts (so you can prove content is
identical), text-vs-ground contrast, the feasibility badge — plus panel count and whether the page
scrolls horizontally.

Two traps that have already produced wrong findings:

- **Compare the same element across directions.** Measuring a highlighted card in one direction and
  a plain card in another gives a number that means nothing. Select explicitly —
  `.card:not(.highlighted)` — rather than taking whatever is first in the DOM.
- **A viewport of `0` means the harness handed you a static snapshot, not a live layout.** Any
  overflow or width measurement from that state is an artifact. Check `clientWidth` before trusting
  anything derived from it.
- **Parse both hex and `rgb()` in your contrast helper.** `getComputedStyle` returns `rgb(...)` but
  the values you compare against are usually hex literals from the token table. A helper that only
  scans for digits reads `#FFFFFF` as `[0,0,0]` and every ratio it produces is wrong while looking
  perfectly plausible. This has happened.
- **Composite opacity before measuring contrast.** An element at `opacity:.5` does not have its
  nominal color on screen. Blend it against what is behind it first, or you will report a passing
  ratio for text that fails.

When the harness cannot run scripts in the page at all, the same measurements work headlessly:
append a probe script that writes its JSON result into a `<div>`, then read it back out of
`chrome --headless --dump-dom`. One command, no browser pane required.

## Capture a PNG

After verifying, screenshot the board to `<output>/01-directions.png`.

This is the only way an agent other than you can *see* the styles rather than read markup — and it
is worth doing for yourself too. Looking at the rendered board catches things no measurement asks
about. Agents without vision fall back to `DECISION.md`, which carries every value in text.

If the harness has a working screenshot tool, use it. When it does not — a preview pane that is not
displayed cannot composite frames, and will time out — **headless Chrome or Edge is on almost every
machine** and takes one command:

```bash
chrome --headless=new --disable-gpu --hide-scrollbars   --window-size=1200,7200 --screenshot=out.png --user-data-dir=/tmp/shot   file:///absolute/path/to/01-directions.html
```

Set the height tall enough for the whole page — ten stacked panels plus tables runs to several
thousand pixels, and a short window silently crops the bottom half. `--user-data-dir` pointed
somewhere disposable avoids colliding with a running browser profile.

## Content

Use the project's actual content. Lorem ipsum hides exactly what the board exists to test. If real
data is sensitive, use synthetic values with the same *shape* — same magnitudes, same label lengths,
same field count. Never real personal data in a file that may be shared.

## Artifacts that are not screens

The same board works for things that are not software. A deck's ten directions are ten title
layouts; a spreadsheet's are ten header-and-conditional-format schemes; a report's are ten type and
rule treatments. The board stays HTML because it renders styles natively and cheaply — what changes
is what the panel depicts, not the medium you depict it in.

## Theme

The board is a document about design, so it should not fight the designs it holds. Neutral chrome —
near-white or near-black ground, restrained type, clearly framed panels. Let the panels carry the
color.
