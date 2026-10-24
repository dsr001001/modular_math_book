# Provenance

## Source

- Repository: https://github.com/dsr001001/mcptrial
- Branch: `ccr-f42a94ab-alw7cu`
- Commit: `f57c783` (`f57c783d8e4214ca3587b5336cd6b29f2c1489cd`), 15 October 2026
- Directory: `ecmine/`

## Copied

| source (`ecmine/`) | here |
|---|---|
| `scripts/` | `scripts/` |
| `results/` | `results/` |
| `paper/tables/` | `tables/` |
| `KNOWN_RELATIONS.md`, `NULL_DESIGN.md`, `STEP6_U1_REPORT.md` | `docs/` |
| `.gitignore` | `.gitignore` |

Apart from the changes listed below, every copied file is identical to its source.

## Not copied

- The snapshots of earlier versions of the note (`Oct10/`, `Oct10_v1_7pm/`, `Oct15/`).
- The paper drafts, the memorandum and the outreach texts (`paper/` other than `paper/tables/`); the paper itself is in
  `../paper/`.
- `HANDOFF.md` and the old `README.md` (internal working log).

## Changes made here

Paths (all scripts run from this directory):
- `scripts/make_tables.py`: output directory `paper/tables/` changed to `tables/` (counts.tex, isolated3.tex, twist.tex,
  oot.tex).
- `scripts/step11_tw_boundary.py`: outputs `paper/tables/euler_uniform.tex`, `paper/tables/ns3.tex` changed to `tables/`;
  docstring updated accordingly.
- `scripts/step10_make_table.py`: output `paper/tables/euler_uniform.tex` changed to `tables/euler_uniform.tex`; docstring
  notes that this is an older layout and that the printed table is written by `step11_tw_boundary.py`.
- `scripts/conj_check.py`: docstring reference `paper/note.tex` changed to `../paper/note.tex`.
- No other script contained a path outside `data/`, `results/`, `scripts/` (all relative to this directory), so no other
  script was changed.

Reproduction scripts:
- `scripts/repro_run.sh` rewritten: bash with `set -euo pipefail`; works from the script's own location instead of a
  `<clone>/ecmine` argument; logs to `logs/repro_run_<UTC time>/`; removes stale PARI outputs before the PARI pass;
  a gp error or nonzero exit on any allcurves file is fatal (completion sentinel; warnings filtered with
  `sed '/Warning/d'`, which does not fail on empty output; the old `; true` removed); checks the ecdata commit, the
  downloaded file counts and the row counts after each stage (3,064,705 curves, 2,164,260 classes, 1,311,066 / 429,936 /
  359,009 optimal curves); diffs the regenerated checker summaries against the committed ones (copied to the log directory
  first) and exits nonzero on any difference.
- `scripts/reproduce_tables.sh` added: the steps behind the printed tables in dependency order, with diffs against the
  committed summaries and tables and a final run of `scripts/selftest.py`.

New files:
- `scripts/selftest.py`, and its output `results/selftest.log`.
- `README.md`, `ENVIRONMENT.md`, `PROVENANCE.md`, `requirements.txt`, `MANIFEST.sha256`.

Other:
- `.gitignore`: the entries for `paper/*.aux`, `paper/*.bbl`, `paper/*.blg`, `paper/*.log`, `paper/*.out` removed (no
  `paper/` here); `logs/` added.
