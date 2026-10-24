# Environment

## PARI/GP

- **PARI/GP 2.15** (2.15.4, as recorded in `results/twist_lemma_check.txt`) was used for the large runs. The `gp` binary is
  needed for the GP scripts:
  - `scripts/pari_features.gp` (Kodaira types and Tamagawa numbers recomputed from the a-invariants; run by `scripts/repro_run.sh`),
  - `scripts/out_of_table.gp` (generator of the out-of-table curves and their modular degrees),
  - `scripts/euler_rule.gp` (the rule for one curve, interactive use),
  - `scripts/twist_lemma_check.gp` and `scripts/pari_periods.gp` (checks and columns of the exploratory stage).
- The Python scripts of steps 9 to 12 and `scripts/selftest.py` call PARI through **cypari2**. The version of the PARI library
  under cypari2 in the large runs was not recorded.
- **PARI/GP 2.17.2** was used for the later checks below conductor 10,000 (or 30,000 where the paper says so); on that range
  they reproduce the counts obtained with 2.15 (paper, Section `sec:data`). The self-test in this directory was run with
  cypari2 2.2.4 on PARI 2.17.2.

### Known quirk of PARI/GP 2.17.2 at q = 2

As stated in Section `sec:data` of the paper: PARI/GP 2.17.2 returns q_E^5 in place of q_E for
`ellinit(E, O(2^k)).tate` when v_2(j_E) = -1, while the q-expansion of j gives q_E directly. (Checked on 14a6, 26a3, 26b2
and 30a4: the returned parameter has 2-adic valuation 5 instead of 1.) The counts are not affected: at q = 2 the Tate
parameter enters no count, since the extra Tamagawa term vanishes there (v_l(2 - 1) = 0), and t_l(E, 2) is read from
v_2(j_E). In this directory Tate parameters are computed only by `scripts/step12_tamagawa.py`, and only at primes
q with q = 1 mod l, l in {3, 5}, so never at q = 2.

### Memory settings

- `ellmoddegree` needs about 32 MB of stack with PARI 2.17 for conductors in the thousands; with PARI 2.15 and larger
  conductors, `parisizemax` of a few hundred megabytes (paper, appendix `app:repro`). For `euler_rule.gp` the header suggests
  `gp -q -D parisizemax=400000000 -D threadsizemax=200000000`.
- For the random out-of-table curves the thread stack of `ellmoddegree` must be enlarged when gp starts
  (`-D threadsizemax=...`); setting it inside the script is too late (header of `scripts/out_of_table.gp`).
- The Python scripts allocate the PARI stack themselves (`pari.allocatemem`, 400 to 600 MB).

## Python

`requirements.txt` lists the packages imported by the scripts: numpy, pandas (3.x), pyarrow, cypari2, and scipy (only
`scripts/step5_cells.py`); scikit-learn is optional (`scripts/step5.py --gbt`). The original runs used pandas 3; the other
package versions of those runs were not recorded.

Verified on 2026-10-24 with Python 3.13, numpy 2.5.3, pandas 3.0.5, pyarrow 26.0.0, scipy 1.18.1, cypari2 2.2.4 (PARI 2.17.2):
- `scripts/selftest.py` passes (`results/selftest.log`);
- steps 1 to 4 of `scripts/reproduce_tables.sh` for the out-of-table range (`oot_convert.py`, `conj_check.py`,
  `step10_sym2_euler.py oot`, `step10_rule.py oot`), which need no ecdata download, regenerate
  `results/check_oot_summary.csv` and `results/step10_rule_oot_summary.csv` byte for byte.

The full pipeline (`scripts/repro_run.sh`, `scripts/reproduce_tables.sh`) was not rerun in that environment.

## Shell and resources

- bash, curl, xargs, sed, awk, sha256sum.
- Disk: the pinned ecdata download is about 1.2 GB; the PARI pass and the parquet files add to that.
- Approximate run times from the logs and working notes of the original runs: PARI feature pass about 15 minutes with two
  gp processes, `build_features.py` about 7 minutes, `conj_check.py` on the three ranges about 8 minutes (`results/repro.log`,
  `results/repro_check2.log`); `step10_sym2_euler.py` under an hour per shard of the working set, `step11_tw_boundary.py` about
  5 minutes, `step12_tamagawa.py work` about 10 minutes.
