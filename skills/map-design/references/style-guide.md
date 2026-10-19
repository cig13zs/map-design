# Style guide

All colours are CSS custom properties in the template. Read them with `css('--name')`; never hard-code
a hex in `draw()`. To rebrand, change the `:root` block (and the dark block) and nothing else.

## Tokens

| Token | Light | Dark | Used for |
|---|---|---|---|
| `--page` | `#f3efe6` | `#0e1116` | page behind the card |
| `--card` | `#fbf8f1` | `#151a21` | card, route halos, hollow dots |
| `--ink` | `#2a2723` | `#ece6da` | titles, place labels |
| `--muted` | `#5c564d` | `#a9a294` | dek, legend text |
| `--faint` | `#8a8378` | `#7d776c` | source line, leader lines |
| `--sea` | `#d7e3e8` | `#10161d` | water |
| `--grat` | `#c6d4da` | `#1c2530` | graticule, globe outline |
| `--land` | `#e4ddcf` | `#262d36` | land |
| `--land-2` | `#d8cfbd` | `#313a45` | land of interest that is not the subject (neighbours, context) |
| `--border` | `#fbf8f1` | `#151a21` | country borders: drawn in the card colour, so they read as gaps |
| `--accent` | `#b8322a` | `#f0a04b` | the subject: routes, focal country, end points |
| `--accent-2` | `#e08a5f` | `#f6c98f` | secondary subject only |
| `--region-label` | `#a59b8a` | `#6f7782` | spaced caps for regions, seas, deserts |
| `--halo` | `#e4ddcf` | `#262d36` | label halo, matches land |
| `--ramp` | 5 steps, `#f4e3c7` to `#7f2a1d` | same | choropleth bins, light to dark = low to high |

In dark mode the ramp stays the same warm hues; low values get lighter, which still reads as "less" on
a dark card because the empty land is darker than the first bin.

## Type

- Title: Source Serif 4, 600, 30px, sentence case. A plain statement of what the map shows: "Where
  Brunei is", "Share of people online". No pun, no type prefix ("Locator:", "Map of").
- Dek: IBM Plex Sans Condensed, 16px, `--muted`. The takeaway or the scope, one line.
- Place labels: Plex Sans Condensed 13px. End points and the focal place 16px 600.
- Region labels: 11px, uppercase, letter-spacing about 0.28em, `--region-label`, no halo.
- Legend: 12px 600 for the title, 11px for values.
- Source: 12px `--faint`, below the map.

## Line weights

- Borders 0.9px in `--border`. Graticule 0.6px. Coastlines are not stroked: the land fill against the
  sea is the coastline.
- Routes and flows 2.2 to 3px in `--accent`, always drawn over a halo 4px wider in `--card`.
- Dashed lines (`4 4`) mean uncertain, planned, or historical-approximate. Say which in the dek or
  source.

## Layout

The card is 1100px wide, the map viewBox is 1036 x 560 by default. `shot.py` reads the viewBox and sizes
the screenshot to fit. Tall subjects (Chile, Japan, the
Philippines) can use 1036 x 760; a globe usually wants 1036 x 620. Legends sit inside the map frame in
a corner over sea, never over the subject.
