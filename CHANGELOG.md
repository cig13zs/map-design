# Changelog

## Unreleased

### Added

- Install with `npx skills add cig13zs/map-design`; the README says so, and the skill names the path to `shot.py` and the `CHROME` variable.
- A seventh example, `examples/route-manila-galleon.html`: the Manila galleon routes across the Pacific, with Equal Earth centred on the date line so neither route is cut, both directions labelled along their lines, and chevrons for direction. Light and dark PNGs are in the gallery.

### Fixed

- `shot.py` failed with a bare `CalledProcessError` when run as root (Docker, CI), because Chrome refuses to start as root with its sandbox on. It now passes `--no-sandbox` in that case, gives up after 120 seconds instead of hanging when the CDN can't be reached, and prints the browser's own error when a render fails.

## 0.1 (2026-10-21)

First release: the skill (six map types, style guide, projections, labels, data sources), the HTML template with its helpers, `shot.py`, and a gallery of six example maps drawn with real World Bank and USGS data.
