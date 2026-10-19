# Route

A path through places in order: a trade route, an expedition, a road trip, a supply chain.

- Projection: conic equal-area for a mid-latitude region, Equal Earth rotated for a route that crosses
  an ocean. Fit to the route's bounding box plus about 15% on each side.
- Draw with `route()`: halo first, then the accent line. Solid for a known path, dashed (`'4 4'`) for
  approximate or historical legs. Mixed is fine: draw each leg separately.
- Stops: `dot()`; first and last are `end: true`. Label every stop that the text mentions, alternate
  label above and below where stops are close.
- Add two or three `regionLabel()`s for the land the route crosses (deserts, plateaus, seas). They do
  more for the story than country names.
- Legs over sea vs land can use the same colour. If the mode matters (ship vs caravan), use solid vs
  dashed and say so in the source line, not in a legend.
- Numbers belong in the dek ("roughly 6,400 km"), not on the line.

Optional: arrowheads every few hundred pixels show direction. Make them small chevrons in the accent,
not filled triangles.

Example: `assets/template.html` (the Silk Road).
