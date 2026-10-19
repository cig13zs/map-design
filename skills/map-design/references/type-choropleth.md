# Choropleth

A rate or share that varies by area: internet use by country, income per person by state.

- Rates only. If the value is a count (population, cases, sales), use proportional symbols instead.
- Projection: Equal Earth for the world, Albers USA for US states. Equal-area is required: a
  choropleth's message is how much area is dark, so area must be true.
- Geometry with an alpha-3 key: the Natural Earth GeoJSON (`ADM0_A3`). Data inlined per data.md.
- Colours: the five `--ramp` steps, light = low. Use `d3.scaleThreshold()` with round breaks when they
  mean something, `d3.scaleQuantile()` otherwise (see data.md).
- No-data countries keep `--land`. Add a separate "No data" swatch after the legend.
- Borders between filled countries stay in `--border` so neighbours with the same bin still separate.
- Legend: `stepLegend()` bottom-left over the sea, with units in the title ("Share of people online, %").
- Labels: none on countries by default. Annotate two or three countries the dek talks about, with the
  value: "Philippines 67%". Use a leader line if the country is small.

```js
const color = d3.scaleThreshold().domain([20, 40, 60, 80]).range(css('--ramp').split(',').map(s => s.trim()));
land.attr('fill', f => DATA[f.properties.ADM0_A3] == null ? css('--land') : color(DATA[f.properties.ADM0_A3]));
```

Drop Antarctica. Small island states vanish at 110m; that is expected. Mention it in the source line
when the dek is about islands.
