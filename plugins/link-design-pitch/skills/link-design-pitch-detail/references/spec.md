# Building the detail spec

One self-contained HTML file plus a PNG. Inline every style, embed assets as data URIs, no external
requests. It must open from disk and survive being emailed to someone.

## Structure

The chosen direction applied to **every distinct surface**, one panel each, at full size, with the
project's real content.

Per panel:

1. **Number and name** — `01 / 04`, the surface's actual name.
2. **What dominates and why**, in one line. If you cannot name it, the hierarchy is not working yet.
3. **The surface itself**, styled in the chosen direction.

Then, below the panels:

- **The measurement table** — hierarchy channel and its numbers, contrast including the elements you
  pushed back, and anything you had to change to make it pass, with before and after.
- **The token table**, with a swatch beside each literal value.
- **The implementation list**, ordered, with paths and lines.

Carry the tokens forward from `DECISION.md` rather than re-deriving them. Two files disagreeing
about a hex value is worse than either being wrong on its own, because now nobody knows which to
trust.

## Reuse the markup

Surfaces of the same product share most of their structure. Write the shell once — navigation,
header, the repeated row or card — and vary only what actually differs between surfaces. Two states
of the same screen (a filter off and on, say) should differ by **exactly one class**, so that the
difference in the picture is the difference in the design and nothing else.

```js
function board(focus){ /* one function, `focus` is the only variable */ }
document.getElementById('a1').innerHTML = board(false);
document.getElementById('a2').innerHTML = board(true);
```

When two panels are supposed to show a before and after, generating both from one function is the
only way to be sure they did.

## Verify in one pass

Render once and run a single script that returns everything. Six separate round-trips cost real time
and tokens for the same answer.

One call should return, per surface: rendered areas of the candidate elements (so dominance is a
number, not a claim), effective contrast of body and de-emphasized text, and whether the page
scrolls horizontally.

Four traps that have already produced wrong findings:

- **Measure the channel the design actually uses.** If hierarchy is carried by contrast, area will
  read 1.00× and that is correct, not a defect.
- **Compare the same element across panels.** Measuring a highlighted card in one and a plain card
  in another gives a number that means nothing. Select explicitly — `.card:not(.highlighted)`.
- **Parse both hex and `rgb()` in your contrast helper.** `getComputedStyle` returns `rgb(...)` but
  the values you compare against are hex literals from the token table. A helper that only scans for
  digits reads `#FFFFFF` as `[0,0,0]` and every ratio it produces is wrong while looking perfectly
  plausible. This has happened.
- **Composite opacity before measuring contrast.** An element at `opacity:.5` does not have its
  nominal color on screen. Blend it against what is behind it first, or you will report a passing
  ratio for text that fails.
- **A viewport of `0` means a static snapshot, not a live layout.** Any overflow or width
  measurement from that state is an artifact. Check `clientWidth` first.

When the harness cannot run scripts in the page, the same measurements work headlessly: append a
probe script that writes its JSON result into a `<div>`, then read it back out of
`chrome --headless --dump-dom`. One command, no browser pane required.

## Capture the PNG

```bash
chrome --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1200,3600 --screenshot=out.png --user-data-dir=/tmp/shot \
  file:///absolute/path/to/02-detail-<direction>.html
```

Set the height tall enough for the whole page; a short window silently crops the bottom. Point
`--user-data-dir` somewhere disposable so it does not collide with a running browser profile.

Look at the result yourself before shipping it. Rendered pages catch things no measurement asks
about — an element with no visible boundary, a panel that reads as empty, type that collides at real
size.

## What does not go in here

**No state or behavior mockups.** Empty views, loading skeletons, failure screens, motion — none of
it. Those depend on the interaction model, which is Phase 5's question and has not been answered
when this file is written. Drawing them early means drawing them twice; that has already happened.

The states belong in the record as a checklist, and the behavior belongs to whoever builds it.

## Content

Use the project's actual content. Lorem ipsum hides exactly what this file exists to test — whether
the direction survives real field counts, real label lengths, real row counts. If real data is
sensitive, use synthetic values with the same *shape*. Never real personal data in a file that may
be shared.

## Theme

The document is about the design, so it should not fight it. Neutral chrome — near-white or
near-black ground, restrained type, clearly framed panels. Let the panels carry the color.
