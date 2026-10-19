# Proportional symbols

A count or size at a place: city populations, earthquake magnitudes as energy, power plant capacity.

- Circle area is proportional to the value: `const r = d3.scaleSqrt().domain([0, max]).range([0, 28])`.
  Never scale the radius linearly; it makes big values look four times too big.
- Fill the circles with `--accent` at 0.55 opacity and a 1px `--card` stroke, so overlapping circles
  stay distinct. Draw the largest first so small ones sit on top.
- Base map stays plain. Countries are not coloured.
- Legend: `circleLegend()` with three round values (for example 1M, 5M, 20M), bottom-left over sea.
- Label the five or so largest, or the ones the dek names, with the value on a second line in
  `--muted`: "Tokyo" then "37.4M".
- Earthquake magnitude is logarithmic. Either size by released energy (10^(1.5 * mag)) and say so, or
  size by magnitude with a stepped legend (M5, M6, M7) and say that the size is not proportional to
  energy. Don't leave it ambiguous.
