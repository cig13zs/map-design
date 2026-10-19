# Data

## Geometry (all public domain, Natural Earth)

| Need | URL | Join key |
|---|---|---|
| World countries, detailed | `https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-50m.json` (TopoJSON) | `id` = ISO 3166 numeric as a string ("608" Philippines), `properties.name` |
| World countries, light (world views) | `https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json` | same |
| World countries with ISO alpha-3 | `https://cdn.jsdelivr.net/gh/nvkelso/natural-earth-vector@v5.1.2/geojson/ne_110m_admin_0_countries.geojson` (GeoJSON) | `properties.ADM0_A3`. Not `ISO_A3`: it is `-99` for France and Norway |
| US states | `https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/states-10m.json` | `id` = state FIPS ("06" California) |
| US counties | `https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/counties-10m.json` | `id` = 5-digit county FIPS |

Use 50m for regional maps and locators, 110m for whole-world views (lighter, cleaner at that scale).
For a choropleth keyed by ISO alpha-3 (World Bank, UN, most CSVs), use the Natural Earth GeoJSON.

## Values

Fetch data while building, then inline it in the HTML as a `const`, with the source and the date you
fetched it:

```js
// World Bank IT.NET.USER.ZS, most recent value per country, fetched 2026-10-19
// https://api.worldbank.org/v2/country/all/indicator/IT.NET.USER.ZS?format=json&mrnev=1&per_page=400
const DATA = { PHL: 67.3, IDN: 69.2, ... };
```

Why inline: the map then renders the same way forever, works offline, and the numbers can be checked
against the file. Several common APIs (World Bank among them) don't allow browser requests from
other sites anyway.

Free sources that need no key:

- World Bank indicators: `https://api.worldbank.org/v2/country/all/indicator/<CODE>?format=json&mrnev=1&per_page=400`.
  Rows include `countryiso3code`. Aggregates (regions, income groups) are mixed in: drop rows whose
  code isn't a country in the geometry.
- USGS earthquakes: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson`
  (also `significant_month`, `2.5_week`). GeoJSON points with `properties.mag`, `time`, `place`.
- Wikipedia tables are fine for one-off facts (a list of cities and populations) if the source line
  names the article and the date.

## Classification for choropleths

- Five bins. Fewer hides variation, more can't be told apart.
- Quantile bins (`d3.scaleQuantile`) when the data is skewed and you want every colour used; round the
  break labels.
- Fixed, round breaks (`d3.scaleThreshold().domain([20, 40, 60, 80])`) when the numbers mean
  something to the reader (percentages, policy thresholds). Prefer this when it works.
- Countries with no data get `--land` with no fill and are named "No data" in the legend.

## Honesty

- Rates on choropleths, counts on symbols.
- Say the year of the data in the source line, and the year differs by country when you use "most
  recent value"; say that too.
- Don't extrapolate, don't fill gaps, don't round away a difference the dek talks about.
- If the user gives numbers, use theirs and cite them as "Data: user-supplied".
