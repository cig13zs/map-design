# Labels

Labels are most of what makes a map look made by a person. Spend the time here.

## Hierarchy

1. End points and the focal place: 16px, 600.
2. Other places on the subject (stops, cities on a route, labelled symbols): 13px, 400.
3. Orientation (a capital or a country name the reader needs to find their bearings): 12px, `--muted`.
4. Regions, seas, deserts, mountain ranges: 11px spaced caps, `--region-label`, no halo.

Use at most two or three orientation labels. If the reader can't place the map without ten, the crop is
wrong.

## Placement

- Default position for a point label is above-right, then right, then above, then below. Pick per point
  so labels don't collide; alternating above and below along a route works well for dense stops.
- Keep 4px between a dot and its label.
- Coastal cities: put the label on the sea side if the land side is crowded, and keep the halo.
- Region labels follow the shape: wide regions get more letter-spacing, never curved text in v0.1.
- Sea labels go in open water, centred, and can be italic if the type family has one. Plex Sans
  Condensed doesn't need it; spaced caps are enough.
- Never rotate place labels. Rotate only labels that follow a long line (a river, a border), and then by
  less than 30 degrees.

## Halo

`label()` draws text with a 3px stroke in `--halo` behind the fill (`paint-order: stroke`). That keeps
names readable over routes and borders. Over the sea, pass `halo: css('--sea')`; over the card (legends,
labels outside the map) pass `halo: css('--card')`.

## Collisions

After drawing, check every pair of label boxes:

```js
const boxes = svg.selectAll('text').nodes().map(n => n.getBBox());
const hits = [];
boxes.forEach((a, i) => boxes.slice(i + 1).forEach(b => {
  if (a.x < b.x + b.width && b.x < a.x + a.width && a.y < b.y + b.height && b.y < a.y + a.height) hits.push([a, b]);
}));
console.log('label collisions', hits.length);
```

Move the label (not the point) until the count is 0. If a cluster can't be cleared, label the
important one, drop the rest, or use a leader line: a 0.75px `--faint` line from the dot to a label in
open space.

## What not to label

- Every country on a world map.
- Places the data doesn't mention.
- The ocean the reader obviously knows, when space is tight. "Pacific Ocean" is optional on a Pacific map.
