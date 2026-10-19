# Point events

Many individual things at places: earthquakes this month, store locations, sightings.

- Dots, 2.5 to 3.5px radius, `--accent` at 0.7 opacity, no stroke. If there are more than about 2,000,
  drop the radius to 1.5px and the opacity to 0.4 so density shows.
- If the events have a size worth showing, it's a proportional symbol map instead (type-symbols.md).
- If time matters, colour by age with two steps only: recent in `--accent`, older in `--accent-2`, and
  say the cutoff in the legend ("last 7 days" / "earlier this month").
- Annotate the two or three notable events with a leader line and a short label ("M7.1, 3 Oct").
- Projection: whatever fits the extent (see projections.md). For global quakes, Equal Earth rotated to
  the Pacific (`rotate([-150, 0])`) keeps the Ring of Fire in one piece.
- Count in the dek ("1,240 earthquakes of magnitude 4.5 or more"), with the date range.
