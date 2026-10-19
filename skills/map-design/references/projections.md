# Projections

Pick by extent, then fit to the area of interest. Every projection here ships with D3.

| Extent | Projection | Notes |
|---|---|---|
| World, statistical (choropleth, symbols) | `d3.geoEqualEarth()` | equal-area, looks familiar; preferred world default |
| World, routes across the Pacific | `d3.geoEqualEarth().rotate([-150, 0])` | centre on the Pacific so trans-Pacific lines don't split |
| One hemisphere, flows from one city | `d3.geoOrthographic().rotate([-lon, -lat])` | a globe; centre slightly off the origin so the destinations fit |
| Continent or wide region (mid latitudes) | `d3.geoConicEqualArea().parallels([p1, p2]).rotate([-centreLon, 0])` | set parallels at about 1/6 and 5/6 of the latitude span |
| Region near the equator (SE Asia, Central Africa) | `d3.geoMercator()` or `d3.geoEquirectangular()` | distortion is small within about 20 degrees of the equator |
| Contiguous US | `d3.geoAlbersUsa()` | moves Alaska and Hawaii into insets for you; data from us-atlas is pre-projected only if you use the `-albers` files, so use the plain ones with this |
| One country, mid latitude | `d3.geoConicConformal().parallels(...)` or `d3.geoTransverseMercator().rotate([-lon, -lat])` | transverse Mercator suits tall countries (Chile, Japan, Philippines) |
| City | `d3.geoMercator()` | fine at this scale |

## Fitting

Fit to the corners you want visible, not to the whole world:

```js
const proj = d3.geoConicEqualArea().parallels([30, 45]).rotate([-68, 0])
  .fitExtent([[10, 20], [W - 10, H - 10]],
    { type: 'MultiPoint', coordinates: [[22, 30], [115, 48], [22, 48], [115, 28]] });
```

`fitExtent` on a feature (`fitExtent(box, someCountry)`) works for locators. For a globe, fit to
`{ type: 'Sphere' }`.

## Gotchas

- Antimeridian: lines and countries that cross 180 degrees (Russia, Fiji, any trans-Pacific route)
  break in a Pacific-cut projection. Rotate the projection so the cut falls in an ocean you don't show.
- Globes need `.clipAngle(90)`, and anything on the far side must not be labelled. Test visibility with
  `d3.geoDistance(point, centre) < Math.PI / 2`.
- Great circles: give `d3.geoPath` a `LineString` with two points and it draws the great circle
  automatically. Don't interpolate by hand.
- Antarctica fills the bottom of a world map. Drop it (`id !== '010'` in world-atlas) unless it matters.
