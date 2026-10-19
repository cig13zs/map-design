---
name: map-design
description: Make editorial maps (route, flow and globe, choropleth, proportional symbol, locator with inset, point events) as self-contained HTML + SVG in a newspaper style, with real data inlined and cited. Use when the user asks for a map, wants to show where something is or happened, compare places, or plot routes, flows, or events on geography.
license: MIT
metadata:
  version: "0.1"
---

# Map design

Make maps that look like a good newspaper graphics desk made them: a calm base, one accent colour,
labels a reader can actually read, and a source line. Output is one HTML file with inline SVG drawn by
D3 from public-domain Natural Earth geometry, plus a PNG when asked.

## 1. Before drawing

Answer these in one line each before writing code. If any answer is unclear, ask the user.

1. What is the one thing the reader should see? That decides the map type (section 3).
2. What area must be visible, and what can be cropped? The crop is part of the argument.
3. What data, from where, as of when? If there is no data source, the map shows geography only and
   says so. Never invent values to fill a choropleth or a symbol map.

## 2. Philosophy

- The base map is quiet. Land, sea and borders sit close in value; only the subject uses the accent.
- One accent. Routes, the focal country, the biggest symbol. A second, lighter tint of it only when
  something is secondary. A map with three bright colours has no subject.
- Label less. Name the places the reader needs and the two or three that orient them. A map with 40
  labels is a gazetteer.
- Crop to the story. A Silk Road map does not need Australia. A world view is a choice, not a default.
- Every map carries a title that says what it shows, a dek with the one-line takeaway or scope, and a
  source line naming the data and the base map.

## 3. Map types

| The reader should see | Type | Reference |
|---|---|---|
| A path through places, in order | Route | [type-route.md](references/type-route.md) |
| Connections from one place to many, across oceans | Flows / globe | [type-flows.md](references/type-flows.md) |
| A rate or share that varies by country or state | Choropleth | [type-choropleth.md](references/type-choropleth.md) |
| A count or size at places (cities, quakes, plants) | Proportional symbols | [type-symbols.md](references/type-symbols.md) |
| Where one small place is | Locator with inset | [type-locator.md](references/type-locator.md) |
| Many individual events or sites | Point events | [type-points.md](references/type-points.md) |

Choropleths take rates (per person, per km2, percent), never raw counts; raw counts go on symbols.
That one rule stops the most common bad map.

## 4. Build

1. Copy [assets/template.html](assets/template.html). Keep the helper block; replace `draw()`.
2. Pick the projection from [references/projections.md](references/projections.md). Fit it to the
   area with `fitExtent` on a MultiPoint of the corners you want, not on the whole world.
3. Get geometry and data per [references/data.md](references/data.md). Inline the data values in the
   file as a `const` with the source URL and the date retrieved in a comment.
4. Style only with the tokens in [references/style-guide.md](references/style-guide.md). Light is the
   default; `#dark` in the URL switches to the dark theme. Both must work.
5. Label per [references/labels.md](references/labels.md): place names with `label()`, regions and
   seas with `regionLabel()`, nothing in bold except end points and the focal place.
6. Render: `python scripts/shot.py map.html map.png` (add `--dark` for the dark version, `--height N`
   if the card is cut off).

## 5. Checks before you hand it over

Open the PNG and look. Fix anything that fails, then look again.

- Nothing important is clipped by the frame, and nothing unimportant fills a third of it.
- No two labels touch, and no label sits on a route or a symbol it doesn't belong to.
- Labels are on land or clearly in the sea, not straddling a coastline.
- The accent appears only on the subject. Squint: the subject should be the first thing you see.
- A choropleth has a legend with its bins and units; a symbol map has a circle legend with real values.
- The source line names the data, the year of the data, and "Natural Earth" for the base.
- Dark version renders with the same layout and every label still readable.
- Numbers on the map match the inlined data. Spot-check two.

## 6. Don'ts

- No drop shadows, glows, gradients on land, or 3D tilt.
- No rainbow or red-green colour ramps. Use the single-hue ramp in the style guide.
- No Mercator for world or continent views (it doubles Europe and erases Africa). It is fine for a city.
- No pins or markers from a mapping library, no tile basemaps, no API keys. Everything is drawn.
- Don't label every country on a world map. Label the ones the story is about.
