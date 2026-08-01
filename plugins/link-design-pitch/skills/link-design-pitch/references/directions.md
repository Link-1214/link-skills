# Direction catalog

Twenty-four directions with concrete signatures. **Pick ten per pitch.**

The catalog is deliberately larger than the board. If it held exactly ten, every project would
receive the same ten and the board would be a template — a bank's operations console would get
Y2K pitched at it every time. A larger pool means the selection itself carries information: the
owner can tell these ten were chosen for them.

Each entry gives you enough to render a faithful mini-mockup without inventing: a ground, an accent, a type stance, a shape language, and the property that makes the style recognizable. Where a style depends on one CSS property to exist at all, that is flagged — check `feasibility.md` before pitching it.

Hex values are starting points, not law. Shift them toward the project's brand.

## Contents

Restrained: [Minimalism](#1-minimalism) · [Swiss](#2-swiss--international) · [Monochrome+1](#3-monochrome--one-accent) · [Document](#4-document--newsprint)
Structural: [Bento](#5-bento-grid) · [Material](#6-material--elevation) · [Dashboard-dense](#7-dense-operational) · [Broken grid](#24-broken-grid--overlap)
Atmospheric: [Dark](#8-dark-mode) · [Glass](#9-glassmorphism) · [Liquid Glass](#19-liquid-glass) · [Gradient mesh](#10-gradient-mesh) · [Neon/Cyber](#11-neon--cyber)
Tactile: [Neumorphism](#12-neumorphism) · [Clay](#13-claymorphism) · [3D/Immersive](#14-3d--immersive) · [Skeuomorphism](#21-skeuomorphism)
Expressive: [Brutalism](#15-brutalism) · [Editorial](#16-editorial) · [Retro Y2K](#17-retro--y2k) · [Terminal](#18-terminal--monospace) · [Maximalism](#20-maximalism) · [Memphis](#23-memphis--postmodern)
Type-led: [Kinetic typography](#22-kinetic-typography)

---

## 1. Minimalism

Ground `#FAFAF8` · surface `#FFFFFF` · text `#1A1A1A`/`#6B6B6B` · accent one muted hue (`#7C8B6F`)
Type: one grotesque, three sizes, weight does the work. Shape: 6–8px radius, hairline `#E8E8E4` borders, no shadow. Space is the main material.

**Good at** long daily use; content with inherent structure; making dense data feel calm.
**Fails when** everything is equally quiet and the eye has nothing to grab — minimalism without hierarchy is just low contrast. Also fails on first-impression pages, where restraint reads as unfinished.
**Notes** the safest direction and therefore the most common AI default. If you pitch it, earn it with real hierarchy rather than uniform greys.

## 2. Swiss / International

Ground `#FFFFFF` · ink `#111111` · accent `#D32F2F` used once per view
Type: Helvetica-lineage, tight tracking, flush-left ragged-right, strict modular scale. Shape: no radius, 1px rules, visible column grid, asymmetric balance.

**Good at** information that has real hierarchy; anything printed or exported; earning trust fast.
**Fails when** the content is emotional or the audience expects warmth. Also brittle — the grid is the design, so one misaligned element is visible.

## 3. Monochrome + one accent

Ground/text: a full grey ramp with a slight hue bias (`#0F1211` → `#F7F8F8`) · accent exactly one hue, everywhere it appears meaning something
Type: any well-set sans. Shape: whatever suits — the discipline is chromatic, not formal.

**Good at** tools where color must carry state, not decoration. If grey is the default, the accent is unmissable.
**Fails when** the data itself needs several categorical colors — you cannot spend the one accent on a five-series chart.

## 4. Document / newsprint

Ground `#FBFAF7` (paper) · ink `#1C1B18` · rules `#D6D2C8` · accent oxblood `#7B2D26`
Type: serif body at generous measure, small-caps labels, footnote sizing. Shape: rules instead of boxes, dense tabular blocks.

**Good at** reports, audit trails, long reading, anything destined for PDF or print.
**Fails when** the screen is interactive — rules and paper suggest read-only, and buttons look pasted on.

## 5. Bento grid

A layout method, not a palette — composes with any color system.
Cells of deliberately different sizes in a tight grid, gap 12–16px, consistent radius. **Cell area encodes importance.** One hero cell per screen answers the screen's main question; supporting cells orbit it.

**Good at** dashboards and overviews where several unrelated things must coexist; giving the eye a defined entry point.
**Fails when** every cell is the same size (then it is just a card grid), or when the content is a single long list.
**Notes** the most useful thing on this list to combine with another direction. Still give it its own slot on the board as a plain layout study — the combination goes in the recommendation, not in a slot.

## 6. Material / elevation

Ground `#F5F5F5` · surface `#FFFFFF` at four elevation levels · accent a saturated primary
Type: Roboto-lineage. Shape: 4px radius, shadow depth encodes layer, ink ripples on press.

**Good at** Android and cross-platform apps; teams who need a documented system more than a distinctive look.
**Fails when** distinctiveness matters — it is a house style millions of apps already wear. Depends on real shadows.

## 7. Dense operational

Ground `#FFFFFF` · text `#1F2328` · borders `#D0D7DE` · semantic red/amber/green reserved for state
Type: 12–13px system sans, tabular numerals mandatory. Shape: 3px radius, 4–6px padding, rules over whitespace, sortable table headers.

**Good at** operators who look at this eight hours a day and want more rows per screen, not more air. Bloomberg, not Stripe.
**Fails when** the audience is occasional — density reads as intimidating to anyone who has not built muscle memory.

## 8. Dark mode

Ground `#0C1211` · surface `#141D1B` · border `#25322F` · text `#E6EFEC`/`#8FA29D` · accent luminous (`#3FBF9C`)
Shape: as the paired layout dictates. The signature is that the accent appears to emit rather than reflect.

**Good at** long sessions in dim rooms; making a saturated accent readable without shouting; monitoring screens where anomalies must pop.
**Fails when** the output gets printed, or when the content is dense black-on-white text — long reading is measurably harder on dark grounds.
**Notes** never simply invert a light palette. Pure `#000` with pure `#FFF` text vibrates; pull both toward the middle. Chart libraries almost always keep their own light background and must be changed separately.

## 9. Glassmorphism

Translucent panels over a colorful ground, blurred backdrop, 1px light border on the top edge, soft outer shadow.
Ground: a saturated gradient or photograph. Panels `rgba(255,255,255,0.12)` with `backdrop-filter: blur(20px)`.

**Good at** hero surfaces and media-rich apps where depth is the point.
**Fails when** text sits on it — contrast shifts with whatever is behind, so accessibility is unstable. Dense UI turns to mush.
**Depends on** `backdrop-filter`. No fallback exists that preserves the effect. Check first.

## 10. Gradient mesh

Multi-point color field as ground (three to five stops bleeding into each other), UI in clean white cards on top.
Ground: `#FF5F6D → #6B5BFF → #00C2FF` at low angle. Cards `#FFFFFF`, radius 12px.

**Good at** landing pages and product marketing; feeling current without much structural work.
**Fails when** the app has its own data colors — the ground competes with every chart. Also dates quickly.
**Notes** a true mesh needs SVG or canvas; a two- or three-stop linear approximation is usually enough and much cheaper.

## 11. Neon / cyber

Ground `#05070D` · surface `#0D1420` · accent electric cyan `#22D3EE` and magenta `#E879F9` · glow via layered outer shadow
Type: condensed sans or mono, uppercase labels, wide tracking. Shape: thin bright borders, scanline texture.

**Good at** security, gaming, monitoring, developer tools — contexts where "system" is the mood.
**Fails when** semantic color matters, since everything already glows and warning red loses its meaning. Depends on shadow-based glow.

## 12. Neumorphism

Ground and surface the *same* color (`#E8ECF1`), form made entirely from paired shadows — light from top-left, dark from bottom-right. Pressed states invert both.

**Good at** control panels, sliders, toggles — physical-feeling inputs.
**Fails at** accessibility, and not marginally: contrast between a control and its ground is near zero by construction. Buttons are hard to find for anyone with low vision.
**Depends on** `box-shadow` entirely. Without it the style has literally no visible form. Check first.

## 13. Claymorphism

Ground pastel (`#EEF2FF`) · surfaces heavily rounded (20–28px) in soft saturated pastels · thick soft shadow plus a subtle inner highlight
Type: rounded geometric sans, generous weight.

**Good at** consumer apps, onboarding, anything for a non-expert audience that should feel friendly.
**Fails when** the audience is professional — it reads as toy-like on financial or operational tools. Depends on shadows.

## 14. 3D / immersive

Rendered objects as the hero — a product, an abstract composition — with flat UI arranged around them. Neutral ground (`#F0EBE3`), one material accent (`#C1683F`).

**Good at** product configurators, spatial data, anything where the object *is* the content.
**Fails when** applied to charts: perspective and shadow distort perceived magnitude, so a 3D bar chart actively misinforms. Assets are expensive and heavy.
**Depends on** WebGL, a 3D runtime, or pre-rendered images. Rarely available in desktop UI toolkits.

## 15. Brutalism

Ground `#FDF6E3` · ink `#000000` · primaries `#1B4DFF` `#FFD400` `#F5453B` at full saturation
Type: heavy grotesque, huge scale jumps, uppercase. Shape: 2–3px black borders, hard offset shadows (no blur), zero radius.

**Good at** portfolios, launches, editorial with attitude, anything that must not look like a template.
**Fails when** used all day — the contrast is genuinely tiring, and there is no quiet register left for secondary information.
**Notes** the hard offset shadow is a solid rectangle, not a blur, so it works in toolkits that lack real shadows — often the only expressive direction available in constrained platforms.

## 16. Editorial

Ground `#F7F5F0` · ink `#16181D` · accent deep `#6B1F2A` · secondary steel `#4A6A8A`
Type: a real display serif at 48px+ against a small sans for UI, wide measure, generous leading, hanging indents. Shape: rules, not boxes; asymmetric columns; images bleeding off one edge.

**Good at** content-led products, reports meant to be read, anything wanting authority.
**Fails when** numbers must align — most display serifs lack tabular figures, so columns wobble. Use a sans for data even if the prose is serif.

## 17. Retro / Y2K

Ground pale blue-lilac gradient · chrome bevels · gloss highlights · pink/violet/cyan `#FF5FA2` `#8B5CF6` `#38BDF8`
Type: bubbly grotesque or pixel. Shape: heavy bevels, inner glow, star and sparkle motifs, beveled window chrome.

**Good at** entertainment, youth-facing products, deliberate nostalgia.
**Fails when** anything must be read seriously — bevels and glow eat legibility, and semantic color drowns in an already-loud field.

## 18. Terminal / monospace

Ground `#0B0E14` or `#F5F5F0` · one mono family throughout · accent green `#4AF626` or amber `#FFB000`
Shape: no radius, ASCII or 1px rules, everything on a character grid, block cursors.

**Good at** developer tools, logs, CI, anything whose audience lives in a shell.
**Fails when** the audience is non-technical, and when text is long — monospace prose is measurably slower to read.
**Notes** the one direction that survives an actual terminal, and it composes well with dense operational layouts.


## 19. Liquid Glass

Ground: whatever is behind it — the material is the point, not a palette.
Panels translucent with **refraction at the edges**, a specular highlight that tracks motion, and
layers that respond to scroll and to the content beneath. Corner radii are continuous, not circular.

**Not the same thing as glassmorphism.** Glassmorphism is a static recipe — blur the backdrop, tint
the panel, add a light top border. Liquid Glass is a *material system*: light bends at the edge, the
highlight moves, and the surface reports state and focus through how it reacts. Apple introduced it
at WWDC 2025 and it is now the house look across their platforms.

**Good at** Apple-native apps, media-forward products, hierarchy expressed as depth rather than
weight; feeling current on iOS/macOS without inventing anything.
**Fails when** text density is high — contrast shifts with whatever is behind and now also with
motion, so legibility is unstable in two dimensions instead of one. Off Apple's platforms it is
expensive to fake and usually lands as ordinary glassmorphism with extra cost.
**Depends on** SwiftUI's glass materials. On the web a partial approximation needs `backdrop-filter`
plus an SVG displacement filter, which is heavy. Not available in desktop toolkits.

## 20. Maximalism

Ground saturated or patterned · three or more type families on purpose · layered, overlapping
composition · dense to the edges · several hues at full strength at once.

The deliberate opposite of strategic minimalism, and it exists because minimalism fatigue is real:
when every product wears the same restrained grid, restraint stops signalling quality.

**Good at** culture, fashion, entertainment, events, personal sites; being remembered.
**Fails at** anything operated daily. No quiet register is left for secondary information, and
accessibility is hard when the ground is busy everywhere.
**Notes** needs genuine art direction. Maximalism without a plan is just noise and reads as noise
immediately — the direction most likely to fail in execution rather than in concept.

## 21. Skeuomorphism

Interface elements imitate specific real objects: stitched leather, ruled paper, brushed metal, a
switch shaped like a switch. Textures and highlights are photographic rather than abstract.

**Distinct from neumorphism**, which abstracts extrusion out of a single flat color. Skeuomorphism
names a real material; neumorphism only implies one. Returning in diluted form through Liquid
Glass's material realism.

**Good at** making unfamiliar controls instantly legible — the affordance is borrowed from an object
the user already knows. Consumer apps, instruments, anything with a physical-world precedent.
**Fails at** scale: every new control needs its own artwork, so the tenth one either costs a day or
does not match. Dates faster than any other direction here.
**Depends on** raster assets or heavy gradient work. Feasible almost anywhere, but expensive.

## 22. Kinetic typography

Type is the motion: words reveal on scroll, weight and width respond to cursor or velocity through
variable-font axes, headlines transform between states. The layout can be otherwise plain — the
movement carries the personality.

**Good at** hero sections, single-message pages, brand moments, launches. It gives a page a
signature without spending a heavy palette.
**Fails when** text must be scanned, compared, or re-read — motion actively interferes with reading
for information.
**Depends on** variable fonts plus CSS or JS animation. Honor `prefers-reduced-motion` with a static
fallback that still reads; the effect is decoration, and decoration should never be the only way the
message arrives. Desktop toolkits animate properties but do not expose variable-font axes, so only
the coarse version survives there.

## 23. Memphis / postmodern

Off-white or boldly colored ground · geometric confetti — squiggles, triangles, dots, terrazzo ·
clashing pastels held together by black outlines · type set at angles.

**Good at** youth-facing products, events, playful consumer brands; signalling that a thing is not
corporate.
**Fails at** data of any kind. The decorative shapes carry the same visual weight as chart marks, so
the eye cannot separate ornament from information.
**Notes** the 1980s original, revived repeatedly. Dates faster than Y2K because the palette is more
specific.

## 24. Broken grid / overlap

Elements deliberately break their column, overlap one another, and bleed past the margin. Images sit
under type; blocks are offset rather than aligned. The grid is present but violated on purpose.

**Good at** editorial, portfolios, and product pages that should feel authored rather than
assembled. The cheapest way to look non-templated while keeping a restrained palette.
**Fails at** tables, forms, and anything dense — the technique needs whitespace to read as
intentional rather than as a rendering bug. Responsive collapse costs real work, since every overlap
needs a stacked fallback.
**Notes** keep DOM order matching visual order. When the two diverge, keyboard and screen-reader
users get a different page than everyone else.

---

## Choosing ten

Cover the range rather than the comfortable middle. A workable spread:

- two or three restrained (1–4, 7)
- one or two structural (5, 6, 24)
- two atmospheric (8–11, 19)
- one tactile (12–14, 21)
- two expressive (15–18, 20, 23)
- type-led (22) when the page is message-first rather than data-first

Then adjust for the answers. A daily-use internal tool has no business seeing Y2K in its top ten — unless you include it precisely to make the point that loud styles cost legibility, which is a legitimate reason to spend one slot.

Say why each of the ten is present. "Included to show where the ceiling is" is a good reason. Silence is not.

**Interaction patterns are not visual directions.** Trend lists mix the two freely — adaptive
layouts, agentic flows, multimodal input, and data storytelling all show up alongside styles.
They are worth doing and they belong in the recommendation prose, but they cannot be rendered as
a panel, and comparing them against Swiss or brutalism is a category error. This catalog holds
only things you can draw.

And keep the ten distinct. Composition is a Phase 3 move — spending a slot on "dark + bento" quietly reduces the board to nine ideas, and what gets dropped is almost always the stretch option that would have shown the owner where the edges are.
