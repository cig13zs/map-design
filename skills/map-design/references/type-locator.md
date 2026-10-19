# Locator with inset

Where is this small place? An island, a province, a town, a site.

- Main map: the place and enough surroundings to recognise it, fitted with
  `fitExtent(box, feature)` plus a margin. The place in `--accent`, neighbours in `--land-2`, the rest
  in `--land`.
- Inset: a small globe or a region map, about 220 x 220, in a corner over sea, with a 1px `--grat`
  frame and a `--card` background. Mark the main map's extent on the inset with a 1.5px `--accent`
  rectangle (draw the main projection's bounds as a polygon in the inset projection).
- Label the place at 16px 600 and two or three orientation places at 12px `--muted` (the capital, the
  nearest big city).
- Sub-national areas (a province, a state) need finer geometry than world-atlas. Use us-atlas for the
  US. For other countries, Natural Earth admin-1 GeoJSON
  (`https://cdn.jsdelivr.net/gh/nvkelso/natural-earth-vector@v5.1.2/geojson/ne_10m_admin_1_states_provinces.geojson`,
  large: filter it once and inline only the feature you need).
- Scale bar on locators only: a 1px `--ink` line with a round distance ("100 km"), bottom-right. Compute
  its length from the projection at the map's centre latitude.
