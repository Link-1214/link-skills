# Direction catalog

Twenty-nine directions. **Pick ten per pitch.**

The catalog is deliberately larger than the board. If it held exactly ten, every project would
receive the same ten and the board would be a template — a bank's operations console would get Y2K
pitched at it every time. A larger pool means the selection itself carries information: the owner
can tell these ten were chosen for them.

## How to read this file

**Read the index. Pick ten. Then read only those ten entries.**

The index carries everything selection needs — what each direction is good at, where it breaks, and
which ones die without a property the target may not have. The entries below carry what *rendering*
needs: the token line, the type and shape signature, and the notes worth knowing once a direction is
actually on the board.

Reading all twenty-nine entries to choose ten costs roughly three times what this file needs to
cost, and the nineteen you did not pick never appear in the output.

## Index

| # | Direction | Good at | Where it breaks |
|---|---|---|---|
| 1 | Minimalism | Long daily use; dense data made calm | No hierarchy means it is just low contrast. Reads unfinished on first-impression pages |
| 2 | Swiss / International | Clear hierarchy; print and export; earns trust fast | The grid *is* the design, so one misalignment shows. Cold where warmth is wanted |
| 3 | Monochrome + one accent | Color carries state, not decoration — the accent is unmissable | Cannot spend the one accent on data that needs several categorical colors |
| 4 | Document / newsprint | Reports, audit trails, long reading, anything going to print | Rules and paper suggest read-only; buttons look pasted on |
| 5 | Bento grid | Dashboards where unrelated things coexist; gives the eye an entry point | Equal-sized cells make it a plain card grid. Pointless for one long list |
| 6 | Material / elevation | Android and cross-platform; a documented system over a distinctive look | A house style millions of apps already wear. **Needs real shadows** |
| 7 | Dense operational | Operators who want more rows per screen, not more air | Intimidating to occasional users. Small hit targets hurt drag-first tools |
| 8 | Dark mode | Long sessions in dim rooms; anomalies pop; saturated accents stay readable | No good in print. Long body text is harder to read. **Charts keep their own light background** |
| 9 | Glassmorphism | Hero surfaces, media-rich apps where depth is the point | **Dies without `backdrop-filter`.** Text contrast shifts with whatever is behind it |
| 10 | Gradient mesh | Landing pages and product marketing; current without structural work | The ground competes with every chart color. Dates quickly |
| 11 | Neon / cyber | Security, gaming, monitoring, developer tools | Everything already glows, so warning red loses its meaning. Needs shadow-based glow |
| 12 | Neumorphism | Control panels, sliders, toggles — physical-feeling inputs | **Contrast to ground is near zero by construction.** Controls are hard to find for low vision. **Dies without `box-shadow`** |
| 13 | Claymorphism | Consumer apps, onboarding, non-expert audiences | Reads toy-like on financial or operational tools. Needs shadows |
| 14 | 3D / immersive | Product configurators, spatial data — where the object *is* the content | **Perspective distorts perceived magnitude, so 3D charts misinform.** Expensive assets; rare in desktop toolkits |
| 15 | Brutalism | Portfolios, launches, anything that must not look templated | Genuinely tiring all day, and no quiet register is left for secondary information |
| 16 | Editorial | Content-led products, reports meant to be read, authority | Display serifs lack tabular figures, so number columns wobble |
| 17 | Retro / Y2K | Entertainment, youth-facing products, deliberate nostalgia | Bevels and glow eat legibility; semantic color drowns in an already-loud field |
| 18 | Terminal / monospace | Developer tools, logs, CI — audiences who live in a shell | Wrong for non-technical users; monospace prose is measurably slower to read |
| 19 | Liquid Glass | Apple-native apps; hierarchy as depth; current without inventing anything | Contrast shifts with background *and* motion. Off Apple platforms it costs more and lands as plain glassmorphism |
| 20 | Maximalism | Culture, fashion, events, personal sites; being remembered | No quiet register, so secondary information and status colors drown. Fails in execution more than in concept |
| 21 | Skeuomorphism | Makes unfamiliar controls instantly legible by borrowing a known object | Every control needs its own artwork, so the tenth does not match. Dates fastest of all |
| 22 | Kinetic typography | Hero sections, single-message pages, launches | Motion interferes with scanning and re-reading. Needs variable fonts plus animation |
| 23 | Memphis / postmodern | Youth-facing products, events; signalling not-corporate | Decorative shapes weigh the same as chart marks, so ornament and information blur |
| 24 | Broken grid / overlap | Editorial and portfolios; non-templated while staying restrained | Wrong for tables, forms, anything dense. Responsive collapse costs real work |
| 25 | Bauhaus | Education, culture, product — geometry makes the structure legible at a glance | Three primaries at full strength collide with status colors. On data screens the shapes compete with the marks |
| 26 | Art Deco | Luxury, spirits, hotels, invitations — formality and occasion | Gold reads as yellow-grey on a screen. Hard to hit contrast targets, and wrong for dense UI |
| 27 | Constructivism | Campaigns, manifestos, anything that needs urgency — diagonals pull the eye through | Diagonal composition breaks under responsive reflow, and it is hostile to long reading |
| 28 | Anti-AI / handmade | When the thing must not look machine-made. Texture, collage, deliberate imperfection | The texture and irregularity blur information. Assets are expensive and do not scale to a hundred screens |
| 29 | Japandi / warm minimal | Screens people sit in for hours — quiet without minimalism's coldness | Low-saturation naturals leave status colors and accents nowhere loud to stand |

**Bold** marks a hard dependency or a failure that disqualifies the direction outright for some
targets. Check those against `feasibility.md` before putting them on the board.

## Choosing ten

Cover the range rather than the comfortable middle. A workable spread:

- two or three restrained (1–4, 7, 29)
- one or two structural (5, 6, 24, 25)
- two atmospheric (8–11, 19)
- one tactile (12–14, 21, 28)
- two expressive (15–18, 20, 23, 26, 27)
- type-led (22) when the page is message-first rather than data-first

Then adjust for the answers. A daily-use internal tool has no business seeing Y2K in its top ten —
unless you include it precisely to make the point that loud styles cost legibility, which is a
legitimate reason to spend one slot.

Say why each of the ten is present. "Included to show where the ceiling is" is a good reason.
Silence is not.

**Interaction patterns are not visual directions.** Trend lists mix the two freely — adaptive
layouts, agentic flows, multimodal input, and data storytelling all show up alongside styles. They
are worth doing and they belong in the recommendation prose, but they cannot be rendered as a panel,
and comparing them against Swiss or brutalism is a category error. This catalog holds only things
you can draw.

**And keep the ten distinct.** Composition is a Phase 3 move — spending a slot on "dark + bento"
quietly reduces the board to nine ideas, and what gets dropped is almost always the stretch option
that would have shown the owner where the edges are.

---

# Entries

Read only the ten you picked. Each gives the token line to render with, the type and shape stance,
and anything worth knowing once it is on the board. What each direction is good at and where it
breaks is in the index above and is not repeated here.

The mockup markup reads seven variables — `--g` ground, `--s` surface, `--l` line, `--t`/`--t2` text
primary and muted, `--ac` accent, `--r` radius. Set them on a wrapper class per direction and the
same markup renders as any style.

## 1. Minimalism

`--g:#FAFAF9;--s:#fff;--l:#E8E8E5;--t:#1A1A1A;--t2:#7C817E;--ac:#4A5B52;--r:6px`

Ground `#FAFAF8` · surface `#FFFFFF` · text `#1A1A1A`/`#6B6B6B` · accent one muted hue (`#7C8B6F`)
Type: one grotesque, three sizes, weight does the work. Shape: 6–8px radius, hairline `#E8E8E4` borders, no shadow. Space is the main material.

## 2. Swiss / International

`--g:#fff;--s:#fff;--l:#111;--t:#111;--t2:#6A6A6A;--ac:#D32F2F;--r:0`

Ground `#FFFFFF` · ink `#111111` · accent `#D32F2F` used once per view
Type: Helvetica-lineage, tight tracking, flush-left ragged-right, strict modular scale. Shape: no radius, 1px rules, visible column grid, asymmetric balance.

## 3. Monochrome + one accent

`--g:#FAFAFA;--s:#fff;--l:#E3E3E3;--t:#141414;--t2:#8A8A8A;--ac:#2F6FED;--r:4px`

Ground/text: a full grey ramp with a slight hue bias (`#0F1211` → `#F7F8F8`) · accent exactly one hue, everywhere it appears meaning something
Type: any well-set sans. Shape: whatever suits — the discipline is chromatic, not formal.

## 4. Document / newsprint

`--g:#FBFAF7;--s:#FDFCF9;--l:#D6D2C8;--t:#1C1B18;--t2:#7A736A;--ac:#7B2D26;--r:0`

Ground `#FBFAF7` (paper) · ink `#1C1B18` · rules `#D6D2C8` · accent oxblood `#7B2D26`
Type: serif body at generous measure, small-caps labels, footnote sizing. Shape: rules instead of boxes, dense tabular blocks.

## 5. Bento grid

`--g:#EEF0F2;--s:#fff;--l:#E2E5E8;--t:#1B1F23;--t2:#767D85;--ac:#2F6FED;--r:12px`

A layout method, not a palette — composes with any color system.
Cells of deliberately different sizes in a tight grid, gap 12–16px, consistent radius. **Cell area encodes importance.** One hero cell per screen answers the screen's main question; supporting cells orbit it.

## 6. Material / elevation

`--g:#F5F5F5;--s:#fff;--l:#E0E0E0;--t:#212121;--t2:#757575;--ac:#1976D2;--r:4px`

Ground `#F5F5F5` · surface `#FFFFFF` at four elevation levels · accent a saturated primary
Type: Roboto-lineage. Shape: 4px radius, shadow depth encodes layer, ink ripples on press.

## 7. Dense operational

`--g:#fff;--s:#fff;--l:#D0D7DE;--t:#1F2328;--t2:#656D76;--ac:#0969DA;--r:3px`

Ground `#FFFFFF` · text `#1F2328` · borders `#D0D7DE` · semantic red/amber/green reserved for state
Type: 12–13px system sans, tabular numerals mandatory. Shape: 3px radius, 4–6px padding, rules over whitespace, sortable table headers.

## 8. Dark mode

`--g:#0C1211;--s:#141D1B;--l:#25322F;--t:#E6EFEC;--t2:#8FA29D;--ac:#3FBF9C;--r:8px`

Ground `#0C1211` · surface `#141D1B` · border `#25322F` · text `#E6EFEC`/`#8FA29D` · accent luminous (`#3FBF9C`)
Shape: as the paired layout dictates. The signature is that the accent appears to emit rather than reflect.

## 9. Glassmorphism

`--g:transparent;--s:rgba(255,255,255,.20);--l:rgba(255,255,255,.42);--t:#12203A;--t2:#4A5D80;--ac:#3B4FE0;--r:12px`

Translucent panels over a colorful ground, blurred backdrop, 1px light border on the top edge, soft outer shadow.
Ground: a saturated gradient or photograph. Panels `rgba(255,255,255,0.12)` with `backdrop-filter: blur(20px)`.

## 10. Gradient mesh

`--g:transparent;--s:#fff;--l:#EAEAF2;--t:#1A1A2E;--t2:#6E6E8A;--ac:#6B5BFF;--r:12px`

Multi-point color field as ground (three to five stops bleeding into each other), UI in clean white cards on top.
Ground: `#FF5F6D → #6B5BFF → #00C2FF` at low angle. Cards `#FFFFFF`, radius 12px.

## 11. Neon / cyber

`--g:#05070D;--s:#0D1420;--l:#1B2838;--t:#DCE7F5;--t2:#7A8CA3;--ac:#22D3EE;--r:4px`

Ground `#05070D` · surface `#0D1420` · accent electric cyan `#22D3EE` and magenta `#E879F9` · glow via layered outer shadow
Type: condensed sans or mono, uppercase labels, wide tracking. Shape: thin bright borders, scanline texture.

## 12. Neumorphism

`--g:#E9EDF2;--s:#E9EDF2;--l:#E9EDF2;--t:#3A4450;--t2:#93A0AE;--ac:#5B7CFA;--r:12px`

Ground and surface the *same* color (`#E8ECF1`), form made entirely from paired shadows — light from top-left, dark from bottom-right. Pressed states invert both.

## 13. Claymorphism

`--g:#EEF2FF;--s:#fff;--l:#E3E8FF;--t:#2B2F4A;--t2:#7C82A8;--ac:#7C6CF5;--r:24px`

Ground pastel (`#EEF2FF`) · surfaces heavily rounded (20–28px) in soft saturated pastels · thick soft shadow plus a subtle inner highlight
Type: rounded geometric sans, generous weight.

## 14. 3D / immersive

`--g:#F0EBE3;--s:#FAF7F2;--l:#DED5C8;--t:#2A241E;--t2:#8A7D6E;--ac:#C1683F;--r:14px`

Rendered objects as the hero — a product, an abstract composition — with flat UI arranged around them. Neutral ground (`#F0EBE3`), one material accent (`#C1683F`).

## 15. Brutalism

`--g:#FDF6E3;--s:#fff;--l:#000;--t:#000;--t2:#000;--ac:#1B4DFF;--r:0`

Ground `#FDF6E3` · ink `#000000` · primaries `#1B4DFF` `#FFD400` `#F5453B` at full saturation
Type: heavy grotesque, huge scale jumps, uppercase. Shape: 2–3px black borders, hard offset shadows (no blur), zero radius.

## 16. Editorial

`--g:#F7F5F0;--s:#FDFCF9;--l:#D8D2C6;--t:#16181D;--t2:#7A736A;--ac:#6B1F2A;--r:0`

Ground `#F7F5F0` · ink `#16181D` · accent deep `#6B1F2A` · secondary steel `#4A6A8A`
Type: a real display serif at 48px+ against a small sans for UI, wide measure, generous leading, hanging indents. Shape: rules, not boxes; asymmetric columns; images bleeding off one edge.

## 17. Retro / Y2K

`--g:#DCE9FB;--s:#EFF6FF;--l:#A9C7E8;--t:#1B2A50;--t2:#6076A8;--ac:#FF5FA2;--r:8px`

Ground pale blue-lilac gradient · chrome bevels · gloss highlights · pink/violet/cyan `#FF5FA2` `#8B5CF6` `#38BDF8`
Type: bubbly grotesque or pixel. Shape: heavy bevels, inner glow, star and sparkle motifs, beveled window chrome.

## 18. Terminal / monospace

`--g:#0B0E14;--s:#0B0E14;--l:#1E2430;--t:#C8D3E0;--t2:#6B7A8D;--ac:#4AF626;--r:0`

Ground `#0B0E14` or `#F5F5F0` · one mono family throughout · accent green `#4AF626` or amber `#FFB000`
Shape: no radius, ASCII or 1px rules, everything on a character grid, block cursors.

## 19. Liquid Glass

`--g:transparent;--s:rgba(255,255,255,.34);--l:rgba(255,255,255,.55);--t:#16233D;--t2:#5A6A85;--ac:#3B62E0;--r:14px`

Ground: whatever is behind it — the material is the point, not a palette.
Panels translucent with **refraction at the edges**, a specular highlight that tracks motion, and
layers that respond to scroll and to the content beneath. Corner radii are continuous, not circular.

**Not the same thing as glassmorphism.** Glassmorphism is a static recipe — blur the backdrop, tint
the panel, add a light top border. Liquid Glass is a *material system*: light bends at the edge, the
highlight moves, and the surface reports state and focus through how it reacts. Apple introduced it
at WWDC 2025 and it is now the house look across their platforms.

## 20. Maximalism

`--g:#1B0F2E;--s:#2A1348;--l:#4A2B72;--t:#FFF3E6;--t2:#C9A6E8;--ac:#FF3D8B;--r:8px`

Ground saturated or patterned · three or more type families on purpose · layered, overlapping
composition · dense to the edges · several hues at full strength at once.

## 21. Skeuomorphism

`--g:#D7CDBE;--s:#F2EBE0;--l:#B9AC98;--t:#2E271D;--t2:#7C7060;--ac:#9C5B2E;--r:8px`

Interface elements imitate specific real objects: stitched leather, ruled paper, brushed metal, a
switch shaped like a switch. Textures and highlights are photographic rather than abstract.

**Distinct from neumorphism**, which abstracts extrusion out of a single flat color. Skeuomorphism
names a real material; neumorphism only implies one. Returning in diluted form through Liquid
Glass's material realism.

## 22. Kinetic typography

`--g:#0E0E10;--s:#0E0E10;--l:#26262B;--t:#F4F4F6;--t2:#8A8A94;--ac:#E8FF3D;--r:0`

Type is the motion: words reveal on scroll, weight and width respond to cursor or velocity through
variable-font axes, headlines transform between states. The layout can be otherwise plain — the
movement carries the personality.

## 23. Memphis / postmodern

`--g:#FBF7EE;--s:#fff;--l:#111;--t:#111;--t2:#5A5A5A;--ac:#FF5F7E;--r:10px`

Off-white or boldly colored ground · geometric confetti — squiggles, triangles, dots, terrazzo ·
clashing pastels held together by black outlines · type set at angles.

## 24. Broken grid / overlap

`--g:#F4F2ED;--s:#fff;--l:#DCD8CF;--t:#191714;--t2:#7A756B;--ac:#B5462F;--r:0`

Elements deliberately break their column, overlap one another, and bleed past the margin. Images sit
under type; blocks are offset rather than aligned. The grid is present but violated on purpose.

## 25. Bauhaus

`--g:#F2EFE9;--s:#fff;--l:#111111;--t:#111111;--t2:#5A5A5A;--ac:#D62828;--r:0`

Primaries at full strength — red `#D62828`, blue `#1D4ED8`, yellow `#FBBF24` — on a warm off-white.
Type: geometric sans, lowercase headlines, tight leading. Shape: circles, triangles and squares used
structurally rather than decoratively; a visible grid; no radius.

**Notes** the ancestor of Swiss, flat design and Material, so it reads as familiar rather than
retro. Distinct from Swiss in that Bauhaus is playful and geometric where Swiss is strict and
typographic. Keep the primaries for structure and leave status color out of that set, or red means
two things at once.

## 26. Art Deco

`--g:#0E1A1A;--s:#132423;--l:#C9A227;--t:#F2EDE3;--t2:#A99B7E;--ac:#C9A227;--r:0`

Deep ground with metallic gold rules. Type: high-contrast display serif or geometric caps with wide
tracking. Shape: strict bilateral symmetry, stepped and fan motifs, sharp angles, thin gold hairlines
framing everything.

**Notes** gold is a texture, not a color — on screen `#C9A227` is a yellow-grey and none of the sheen
survives. Use it for rules and accents, never for text that has to be read. The symmetry is the
signature; break it and the style disappears.

## 27. Constructivism

`--g:#F2EDE4;--s:#FFFFFF;--l:#111111;--t:#111111;--t2:#4A4A4A;--ac:#D2231F;--r:0`

Red, black and paper. Type: heavy condensed sans, often rotated. Shape: diagonal axes, hard-edged
photographic montage, oversized numerals, elements running off the edge to imply motion.

**Notes** designed to look urgent, which is exactly why it wears badly on anything read daily. Nearest
neighbour is brutalism, but constructivism is dynamic where brutalism is static. The diagonals are
where responsive layout breaks first — decide early how they collapse.

## 28. Anti-AI / handmade

`--g:#EDE7DA;--s:#F7F3EA;--l:#C9BCA4;--t:#2A241C;--t2:#6E6354;--ac:#B4552E;--r:4px`

Paper and ink rather than pixels. Visible texture, torn and cut edges, slight rotation on elements,
hand-drawn rules, photographed materials. Type: a face with irregularity in it, or actual handwriting
for accents.

**Notes** the 2026 counter-movement to AI's uniform polish — the point is that a person made it, so
the imperfection has to look intentional rather than sloppy. Punk-revival collage sits at the loud end
of the same idea. Expensive: every texture is an asset, and it does not scale to a hundred screens.
Strongest where the audience is already suspicious that the work was generated.

## 29. Japandi / warm minimal

`--g:#F3F0EA;--s:#FBFAF7;--l:#DED8CC;--t:#2C2A26;--t2:#7A756B;--ac:#8A9A7B;--r:8px`

Minimalism with warmth added back. Warm neutrals, muted sage or clay accent, generous space, natural
material texture at low opacity. Type: humanist sans, comfortable leading, nothing tight.

**Notes** solves minimalism's actual failure — that restraint on a cold grey ground reads as
unfinished. Distinct from plain minimalism in temperature, not in density. The muted accent is the
risk: check that status colors still separate from it before committing.

---

### The ones that need more than a token line

Most directions are the token line and nothing else. These seven also need structural CSS, and it is
the same few rules every time:

| Direction | Add |
|---|---|
| Glassmorphism · Liquid Glass | gradient or photo on `--g`'s element, `backdrop-filter:blur(16px)` on surfaces, `inset 0 1px 0 rgba(255,255,255,.6)` for the edge |
| Gradient mesh · Maximalism | `background:` with two or three `radial-gradient` stops over a base `linear-gradient` |
| Neumorphism | `box-shadow:4px 4px 9px #C9D0D9,-4px -4px 9px #fff` on surfaces; inset the same for pressed |
| Claymorphism | `box-shadow:0 8px 20px rgba(60,50,140,.18), inset 0 -3px 0 rgba(0,0,0,.06)` |
| Brutalism | `border:2px solid #000; box-shadow:3px 3px 0 #000` — a solid offset, no blur |
| Neon / cyber | `box-shadow:0 0 12px currentColor` on accented borders |
| Terminal | `font-family:ui-monospace,Consolas,monospace` throughout |
| Anti-AI / handmade | a paper texture as a repeating data-URI background, plus `transform:rotate(-.4deg)` on cards so nothing sits perfectly square |
| Art Deco | `border-image` or stacked 1px gold rules for the stepped frames; symmetry has to be built into the layout, not added as CSS |
| Constructivism | `transform:rotate(-8deg)` on headline blocks, and a decision about how they un-rotate on narrow widths |

Adjust values toward the project's brand when it has one. What you should not do is start from a
blank palette — that is where the run time goes.
