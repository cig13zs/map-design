# Flows and globe

Connections from one place to many: flight routes, migration from one country, exports to partners.

## Globe (one origin, destinations on one hemisphere)

```js
const proj = d3.geoOrthographic().rotate([-125, -18]).clipAngle(90)
  .fitExtent([[60, 20], [W - 60, H - 20]], { type: 'Sphere' });
base(svg, path, w, { sphere: true });
```

- Centre the globe between the origin and the destinations, not on the origin, so the far ends stay on
  the visible face. Check every destination with `d3.geoDistance(dest, centre) < Math.PI / 2`; anything
  outside goes in the dek ("plus London, beyond the horizon") rather than as a half-hidden label.
- Draw each flow as a two-point `LineString`; D3 draws the great circle.
- Fill the origin country with `--accent` and leave the destinations as dots. Label the origin at 17px
  600, destinations at 14px.

## Flat world (one origin, destinations everywhere)

Equal Earth rotated so the origin sits near the centre. Great circles from the origin then fan out
without crossing the map edge.

## Width means amount

When flows carry a value (passengers, tonnes), map it to stroke width with `d3.scaleSqrt`, from about
1px to 8px, and add a three-line width legend. Draw the widest flows first so thin ones stay on top.
Without a value, all flows are 2.2px.

## Don't

- Don't draw flows between every pair of places (a hairball). Pick an origin.
- Don't use curved arcs that aren't great circles. They look nice and mean nothing.
