# Panel 4 — auto-updating RADAR + TROPHIES

GitHub activity can't live inside a static SVG, so this package regenerates
the panel **from your real stats** on a nightly GitHub Action and commits the
fresh SVG. The README just points at `panel4_radar.svg` like any other image.

## What it draws
- **L-shaped Curry-Gold panel** (locked bevel recipe: OFF=9, BEV=5, BW=18),
  bottom-right 350x350 notch left open for the `more(me)` square.
- **Prompt** `> github.exe -RADAR` — VT323 40px, black, pulsing (panel-2/3 style).
- **Radar** (left arm): COMMITS / PRS / ISSUES / REVIEWS from your last 12
  months (`contributionsCollection`), blackberry polygon on diamond rings,
  raw counts on each axis, grow-in animation.
- **Trophies** (top band): STARS, COMMITS, PRS, FOLLOWERS pixel cups with
  rank letters (C/B/A/S by thresholds in `THRESH`), staggered pop-in.

## Install (your profile repo, e.g. McVarHQ/McVarHQ)
1. Copy into the repo root:
   - `.github/workflows/radar.yml`
   - `scripts/gen_radar.py`, `scripts/fonts.py`, `scripts/palette.py`
   - `fonts/Early_GameBoy.ttf`, `fonts/VT323-Regular.ttf`  ← you must add the TTFs
2. Commit. The workflow runs on push (and nightly, and via the *Run workflow*
   button under Actions). It writes/updates `panel4_radar.svg` in the repo root.
3. Reference it from README.md:
   `<p align="center"><img src="./panel4_radar.svg" width="880"></p>`
   (final assembly will interlock it with `more(me)` — later step.)

No PAT needed: the default `GITHUB_TOKEN` covers the GraphQL stats query and
the commit (workflow has `contents: write`).

## Tuning
- `CAPS` in `gen_radar.py` — what count = 100% on each radar axis.
- `THRESH` — trophy rank cutoffs per metric.
- `MOCK` — numbers used with `--mock` (preview without API).

## Local preview
```
FONT_DIR=path/to/ttfs python scripts/gen_radar.py --mock --out preview.svg
```
`--static` strips animations (for rasterizers that can't run SMIL).
