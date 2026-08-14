# Feasibility by platform

The failure this file prevents: an owner falls in love with a direction the target cannot render,
and nobody finds out until implementation. The failure is usually *silent* — the property parses, no
error appears, and the effect simply is not there.

## How to read this file

**Read the two tables below, then read only the section for your target.** The tables are
cross-platform and always apply; the per-platform sections are detail you need for one target and
not the other six.

Where you are unsure, verify rather than trust this file — render one throwaway element with the
risky property and look at it. Platforms change; a measurement beats a table.

## Platform index

| Target | Used for | What it blocks |
|---|---|---|
| **Qt / PySide6 / PyQt** | Desktop apps in Python or C++ | `box-shadow` · `backdrop-filter` · `opacity` · `transition` · `transform` · flex/grid — **all parse silently and do nothing**. Charts never take the stylesheet |
| **Web (browser)** | Anything in a browser | Nothing structural. Watch CSP blocking font CDNs, and design both themes |
| **Native mobile** | SwiftUI · Compose · React Native | Blur is native on iOS, API 31+ on Android, a package on React Native. Shadows differ between iOS and Android |
| **Terminal / TUI** | Shell tools | No images, shadows, gradients or custom type. Pitch three directions honestly, not ten |
| **Email (HTML)** | Newsletters, transactional mail | No flexbox, grid, web fonts or JavaScript. Dark mode is inverted by clients unpredictably |
| **Print / PDF** | Reports, anything on paper | No motion, no interaction, no dark mode. Hairlines under 0.25pt vanish; saturated RGB shifts in CMYK |
| **Slides (PowerPoint / Keynote)** | Decks | Fonts must exist on the presenting machine or slides reflow. Projectors crush contrast — push it further than feels right |

## What the token line survives

The colours and `--r` port everywhere. Of the eight structural values, these are what actually
arrives on each target — verified on Qt, reasoned elsewhere from the platform notes below.

| Value | Qt / QSS | Email | Print | Slides | Spreadsheet |
|---|---|---|---|---|---|
| `--f` family | yes | yes (system only) | yes | must exist on the presenting machine | yes |
| `--fw` `--hw` | yes | yes | yes | yes | yes |
| `--sc` as computed px | yes | yes | yes | yes | yes |
| `--ls` | yes, but read as a **percentage** | partial | yes | yes | **no cell-level equivalent** |
| `--bw` | yes | yes | thins below 0.25pt | yes | quantised to preset weights |
| `--d` | **the `calc()` chain is silently ignored** | ignored | — | — | — |
| `--sh` | **parses, does nothing** | dropped | prints as muddy grey | yes | no |

**`calc()` does not exist in QSS, and neither do custom properties.** Outside a browser the token
line is a *specification to hand-translate*, not CSS to paste: compute the five density-driven
numbers yourself and write them as literals. A `--*` custom property left in a Qt stylesheet
invalidates the whole sheet, and the type falls back to the default face with no error.

## What each direction actually depends on

Most styles survive anywhere. A few have a single point of failure — remove one property and nothing recognizable remains.

| Direction | Hard dependency | Survives without it? |
|---|---|---|
| Glassmorphism | `backdrop-filter` (blur what is behind) | No. Translucency without blur is just a tint. |
| Liquid Glass | Apple's glass materials; elsewhere `backdrop-filter` + SVG displacement | No. Without refraction and motion response it degrades to plain glassmorphism. |
| Neumorphism | `box-shadow`, two per element | No. The form *is* the shadows. |
| 3D / immersive | WebGL, a 3D runtime, or pre-rendered assets | No. |
| Claymorphism | `box-shadow` (soft, large) | Weakly — flat pastel with big radius reads as generic. |
| Neon / cyber | shadow-based glow | Partly — bright borders on dark still read as "system". |
| Material | shadow-based elevation | Partly — swap elevation for borders and it becomes flat design. |
| Gradient mesh | multi-stop gradients (SVG/canvas for true mesh) | Yes — a 2–3 stop linear gradient approximates it. |
| Kinetic typography | variable fonts + animation | Partly — a static cut still reads, but the direction is gone. |
| Skeuomorphism | raster texture assets or heavy gradients | Yes, but the cost is per-control artwork, not per-theme. |
| Everything else | nothing exotic | Yes. |

Brutalism, terminal, editorial, Swiss, minimalism, dark, bento, monochrome, document, and dense-operational need only solid fills, borders, and type. They are the safe pitches on constrained platforms — and brutalism in particular is often the *only* expressive option, because its hard offset shadow is a plain filled rectangle rather than a blur.

## A note on charts, on every platform

Chart libraries own their own rendering and almost never inherit the app's theme. Whatever the platform, treat chart background, axes, gridlines, tick labels, legends, and series colors as a separate work item with its own line in the implementation checklist.

And regardless of direction: avoid 3D bars, 3D pie, and drop shadows on data marks. Perspective and shadow distort perceived magnitude, which turns a styling choice into a reporting error.

---

# Per-platform detail

Read the one that matches your target. If the deliverable spans two — a web app that also gets
printed — read both.

## Qt / PySide6 / PyQt (QSS)

QSS looks like CSS and is a small subset of it. Unsupported properties **parse without error and do nothing** — the most dangerous failure mode on this list, because the code looks right.

Not supported: `box-shadow` · `backdrop-filter` · `filter` · `opacity` on widgets · `transition` · `transform` · `flex`/`grid` · pseudo-elements (`::before`, `::after`) · web fonts.

Supported: `qlineargradient` · `qradialgradient` · `qconicalgradient` · `rgba()` · `border-radius` · `border-image` · `background-image` · per-state selectors (`:hover`, `:pressed`, `:focus`, `:disabled`, `:checked`).

Consequences worth knowing before you pitch:

- Depth must come from gradients and borders. A subtle `qradialgradient` behind a hero panel is the closest available thing to a glow.
- Layout is code (`QVBoxLayout`, `QGridLayout`, `setRowStretch`), not stylesheet. A bento grid is entirely feasible — it is just written in Python instead of CSS.
- Animation needs `QPropertyAnimation`, not `transition`.
- **Charts do not take QSS at all.** pyqtgraph and QtCharts keep their own background, axis, grid, and legend colors. A dark theme applied only to the stylesheet leaves the plots white — the single most common way a Qt dark mode ships broken. Budget for `setBackground`, view-box color, axis pens, tick text pens, grid color, and legend brush/pen as separate work.
- Table cell colors set through `QTableWidgetItem.setBackground/setForeground` also bypass the stylesheet, as does anything drawn in a `paintEvent`.

Before estimating a theme swap here, count the color literals:

```bash
grep -oE '#[0-9a-fA-F]{6}' path/to/ui.py | wc -l
```

Split the count between inside and outside the stylesheet string. The ones outside are the hidden cost. If the total is large, recommend introducing a token layer first as a no-visual-change step — that makes the swap reviewable and reversible instead of a thousand-line diff nobody can verify.

## Web (browser)

Everything works. `backdrop-filter` is broadly supported now but still worth a fallback for the panel background so text stays legible if it is unavailable.

Real constraints are elsewhere: a strict CSP may block font CDNs and external assets, so inline fonts as data URIs rather than linking them — a silently failed webfont falls back to a system face and the whole type direction evaporates. Respect `prefers-reduced-motion`. Design both themes if the page follows the viewer's preference.

## Native mobile

**SwiftUI / iOS** — real blur exists as `Material` (`.ultraThinMaterial`), so glassmorphism is native here and idiomatic. Liquid Glass is the current house material and is available directly; on this platform it is cheaper than approximating glassmorphism by hand. Shadows, gradients, and spring animation all available. Respect Dynamic Type: fixed-size text breaks accessibility settings.

**Jetpack Compose / Android** — elevation and shadows are first-class; blur (`Modifier.blur`) requires API 31+, so glass needs a fallback on older devices. Material You can pull accent colors from the user's wallpaper, which will override a fixed accent unless explicitly opted out.

**React Native** — no `backdrop-filter`; blur needs a community BlurView package. Shadows diverge: iOS uses `shadowColor/Offset/Opacity/Radius`, Android uses `elevation` only, and they do not look the same. Avoid directions whose identity is shadow-based unless you accept two different looks.

## Terminal / TUI

No images, no shadows, no gradients, no custom type. Color is 16 / 256 / truecolor depending on the emulator, and truecolor is not guaranteed. Layout is a character grid.

Terminal/monospace is the direction. Dense-operational and brutalism partially survive as heavy box-drawing rules and full-saturation ANSI color. Nothing else on the list is viable — do not pitch ten directions here; pitch three honestly.

## Email (HTML)

The most restricted target in common use. Assume table-based layout, inline styles, no flexbox or grid, no web fonts, no JavaScript, no dark-mode reliability — several clients invert colors on their own and will wreck a hand-tuned dark palette.

Pitch only flat-fill directions with system fonts. Test in the actual clients; support varies more between them than between browsers.

## Print / PDF

No motion, no interaction, no dark mode — a dark ground means a page of solid ink, which readers and printers both object to. Hairlines below ~0.25pt may vanish. Color needs CMYK consideration if it goes to press; saturated RGB accents shift noticeably.

Document, editorial, and Swiss are the natural fits. Dark, neon, glass, and neumorphism are non-starters.

## Slides (PowerPoint / Keynote)

Gradients, shadows, and images all fine. Fonts must exist on the presenting machine or be embedded — otherwise substitution silently reflows every slide. Assume the room's projector crushes contrast: mid-greys on white disappear, and thin light type on dark disappears faster. Push contrast further than feels right on a laptop.
