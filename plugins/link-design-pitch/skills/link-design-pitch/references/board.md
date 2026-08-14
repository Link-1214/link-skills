# Building the boards

One self-contained HTML file: the ten-direction board. Inline every style, embed assets as data
URIs, no external requests. It must open from disk and survive being emailed to someone.

The per-surface detail spec is a different file built by a different skill — see
`link-design-pitch-detail`. This file covers the board only.

## Assemble, do not author

**Every panel is HTML and CSS you write. Nothing is downloaded, searched for, or pasted in.** The
catalog carries the palette and the shape language; a reference image found online cannot contain
this project's content, and the whole point of the board is to see that content in each style.

The single largest cost in a run is hand-writing ten palettes. Do not. Each catalog entry opens with
a ready-made token line, and the file ends with the few extra rules the shadow- and blur-based
directions need.

The structure that makes this cheap: **write the mockup markup once, and give each direction a
wrapper class that redefines the whole token line** — all fifteen values, not just the colours.

**Copy every value the catalog gives you.** A wrapper that redefines only the six colours produces
ten panels in one typeface at one size with one rhythm, differing in hue alone. Measured on real
boards built that way, the rendered typeface was identical in every panel and a viewer counted six
distinct designs out of ten. The colours are the least of what separates these directions.

```html
<div class="mock d-swiss">…markup…</div>
<div class="mock d-dark">…same markup…</div>
```

```css
.mock { --g:#fff;--s:#fff;--l:#E3E6E8;--t:#1B1F23;--t2:#6B7480;--ac:#2F6FED;--r:6px;
        --f:var(--ui);--fw:400;--hw:600;--sc:2.2;--ls:0;--d:1;--bw:1px;--sh:none;
        background:var(--g); color:var(--t);
        font-family:var(--f); font-weight:var(--fw); letter-spacing:var(--ls);
        font-size:calc(14px * var(--d)); line-height:calc(1.45 * var(--d)); }
.mock h2   { font-weight:var(--hw); font-size:calc(14px * var(--d) * var(--sc)); }
.mock .card{ background:var(--s); border:var(--bw) solid var(--l); border-radius:var(--r);
             box-shadow:var(--sh); padding:calc(10px * var(--d)); }
.mock .rows{ display:flex; flex-direction:column; gap:max(0px, calc(7px * var(--d))); }

.d-swiss { --g:#fff;--s:#fff;--l:#111;--t:#111;--t2:#6A6A6A;--ac:#D32F2F;--r:0;
           --f:var(--sans);--fw:400;--hw:700;--sc:2.6;--ls:-.01em;--d:1.0;--bw:1px;--sh:none }
.d-dark  { --g:#0C1211;--s:#141D1B;--l:#25322F;--t:#E6EFEC;--t2:#8FA29D;--ac:#3FBF9C;--r:8px;
           --f:var(--ui);--fw:400;--hw:600;--sc:2.3;--ls:.01em;--d:1.05;--bw:1px;--sh:none }
```

Bind the six font roles once, near the top, from the table in `directions.md`:

```css
:root { --ui:"Segoe UI",system-ui,"Malgun Gothic","Hiragino Sans",sans-serif;
        --sans:Arial,Helvetica,Dotum,"Hiragino Kaku Gothic ProN",sans-serif;
        --serif:Georgia,"Times New Roman",Batang,"Hiragino Mincho ProN",serif;
        --class:"Times New Roman",Georgia,Gungsuh,"Yu Mincho",serif;
        --mono:Consolas,"Courier New",DotumChe,"MS Gothic",monospace;
        --heavy:"Arial Black",Impact,Haettenschweiler,Gulim,sans-serif; }
```

**Wrap every `--d`-driven gap in `max(0px, …)`.** A density below 1 can drive a subtraction negative,
and rows then overlap into each other's borders — it renders, it looks merely tight, and nothing
reports an error.

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

**Same size means the same frame width, never a fixed height.** Setting `height` on the mockup makes
density structurally unable to express: a dense operational direction and an airy minimal one get
squeezed into an identical box, and the channel that separates them most visibly is gone. On boards
where the height was pinned, every panel rendered at exactly the same height and the directions
became indistinguishable below the colour.

**`min-height` is the same trap wearing a different name.** Set it high enough to tidy the short
panels and the tight directions rise to meet it, which is the flattening again — measured on a real
board, two panels landed on exactly the stated `min-height`. Let the panels be uneven. Uneven height
*is* the density channel showing you it works.

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
- **`font-family` is what you asked for, not what rendered.** A face the machine lacks falls back
  silently, so ten panels can report ten different families and paint one. Measure the rendered face
  instead, and **probe with a string in the content's own script** — a Latin probe on a Korean board
  reports ten distinct faces while every Hangul glyph on screen comes from one fallback, which is
  the exact bug this check exists to catch.
- **On CJK, comparing `measureText` widths does not work at all.** Han and Hangul advance a fixed em,
  so every face returns the identical width and the check reports total collapse whatever the truth
  is — measured, ten panels all returned `672.00`. Rasterise instead: draw the probe string to a
  canvas, **crop to the ink bounding box**, and hash the pixels. Without the crop, two panels whose
  text merely sits at different offsets read as different faces.
- **Count what separates the panels, not just what differs.** For each of typeface, weight, size,
  tracking, density and radius, count how many distinct rendered values appear across the ten. Any
  channel sitting at one value is contributing nothing, and if only colour is above one, the board
  has collapsed no matter how good each panel looks alone.

When the harness cannot run scripts in the page at all, the same measurements work headlessly:
append a probe script that writes its JSON result into a `<div>`, then read it back out of
`chrome --headless --dump-dom`. One command, no browser pane required.

## Capture a PNG

After verifying, screenshot the board to `<output>/01-directions.png`.

This is not only for agents. **Nowhere outside a local browser renders HTML** — not a repository
page, not a chat message, not a phone. The picture is how most people will actually see this board,
and it is how an agent with vision sees the styles rather than reading markup. Anything without
vision falls back to `DECISION.md`, which carries every value in text.

Look at it yourself before shipping it. The rendered board catches things no measurement asks
about.

If the harness has a working screenshot tool, use it. When it does not — a preview pane that is not
displayed cannot composite frames, and will time out — **headless Chrome or Edge is on almost every
machine** and takes one command:

```bash
chrome --headless=new --disable-gpu --hide-scrollbars   --window-size=1200,7200 --screenshot=out.png --user-data-dir=/tmp/shot   file:///absolute/path/to/01-directions.html
```

On Windows neither browser is on PATH: use the full path — typically
`C:\Program Files\Google\Chrome\Application\chrome.exe` or
`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` — and point `--user-data-dir`
at a Windows temp path such as `%TEMP%\shot`.

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
