# Stage 3: numbers stated in ../paper/note.tex without a committed source, recomputed from the pinned data

Run on 2026-10-24 in `final/pipeline` after the full rerun of stages 1 and 2 (PARI 2.17.2 via cypari2, ecdata commit
`25cec5e`). Every run is logged in `results/stage3.log`. Scripts: `scripts/stage3_*.py`. Nothing in `../paper` was edited.

| item | paper (section) | paper's number | recomputed | verdict | script | output |
|---|---|---|---|---|---|---|
| 1a | sec:eis | 75,430 eis. non-CM (l=3, work); 67,845 with G>0 | 75,430; 67,845 | MATCH | stage3_eis.py | stage3_eis.txt |
| 1b | sec:eis | 2,777 with D>0 | 2,777 (2,755 with D=1, 22 with D=2) | MATCH | stage3_eis.py | stage3_eis.txt |
| 1c | sec:eis | D=2: 22 = 17 (3Cs.1.1) + 5 (9-torsion, 3B.1.1) | 22 = 17 + 5; the 17 all rank 0, torsion Z/3 (16) or Z/6 (1: 14a1) | MATCH | stage3_eis.py | stage3_eis.txt, stage3_eis_D2.csv |
| 1d | sec:eis | no deficit without a rational 3-torsion point; D<=1 for Borel with a 3-point and no 9-point | 0 such curves; max D = 1 on 27,384 curves (all 3B.1.1) | MATCH | stage3_eis.py | stage3_eis.txt |
| 1e | sec:eis | none of the 2,065 curves with 3Cs.1.1, N<=400000, has a 9-point; torsion Z/3 or Z/6 | 2,065 = ALL curves (not only optimal; 259 optimal) with label 3Cs.1.1 and N<=400000; 0 with 9 \| #tors; 1,997 Z/3, 68 Z/6 | MATCH (population is all curves) | stage3_eis.py | stage3_eis.txt |
| 1f | sec:eis | "the 18 optimal curves with a point of order 9 all have image 3B.1.1" | 18 is the number of ALL curves (any number in the class) with a 9-point and N<=400000 (all 3B.1.1). Optimal ones: 13 (work), 14 (N<=400000), 15 (N<500000), all 3B.1.1 / 3B11 | MISMATCH in wording ("optimal") | stage3_eis.py | stage3_eis.txt |
| 1g | sec:eis | torsion bound attained with D>0 in 2,773 cases | 2,773 (work, l=3); holdout 473, ext 439 | MATCH (work, l=3) | stage3_eis.py | stage3_eis.txt |
| 1h | sec:eis | l=5, 7: D<=1, only with an l-torsion point; 192 and 18 (work) | 192 and 18; all with an l-torsion point; max D 1 | MATCH | stage3_eis.py | stage3_eis.txt |
| 2a | thm:twist | 157,938 (curve, I_n* prime) pairs, no exception | 157,938 pairs (q>=5), all twist classes found, 0 violations over 590,818 (pair, l) | MATCH | stage3_twist_degree.py | stage3_twist_degree.txt |
| 2b | thm:twist | 292,580 (curve, pot. good additive prime) pairs, no exception, equality in case (c) | 292,580 = 64,268 I0* + 228,312 case (c), q>=5; 0 violations; case (c) equality in all 845,817 (pair, l) | MATCH | stage3_twist_degree.py | stage3_twist_degree.txt |
| 2c | thm:twist | N<10000: difference = Euler term in all 25,477 (curve, l) pairs | 25,477 pairs (E[l] irreducible, not CM, l not dividing N, S nonempty): 25,477 equal, 0 differ | MATCH | stage3_twist_degree.py | stage3_twist_degree.txt |
| 3 | sec:two | 964,432 / 325,510 / 313,741 curves; weight-1 rule no exception; I0* weight 2: 123, 26, 20 exceptions | populations equal; weight 1: 0, 0, 0; weight 2: 123, 26, **19** | MATCH, MATCH, MISMATCH (ext 19 vs 20) | stage3_two.py | stage3_two.txt |
| 4 | sec:wild | minima of v_3(deg) at q=3: 1 (II, IV, III*), 2 (II*, IV*), 0 (III, I0*) | II 1 (8,309 curves), IV 1 (5,791), III* 1 (7,630), II* 2 (5,791), IV* 2 (8,309), III 0 (7,630), I0* 0 (12,281) | MATCH | stage3_w3.py | stage3_w3.txt |
| 5 | lem:euler | table confirmed against lfunsympow on every curve of the tables | 5,102,273 (optimal curve N<500000, bad q>=5) pairs: P_q equals the table's polynomial in all; e_l (l=3,5,7) from P_q equals the closed formula in all | MATCH | stage3_euler_lemma.py | stage3_euler_lemma.txt |
| 6 | sec:data | fifteen degrees recomputed with ellmoddegree, all agree | 60 sampled optimal curves (seed 20261024, 20 per range, 7 configurations) + 3 of sec:eis: 63/63 agree, 325 s | MATCH (fifteen not identifiable) | stage3_moddeg_sample.py | stage3_moddeg_sample.{txt,csv} |
| 7 | sec:data | mod 3 images checked against psi_3 | 2,097,505 optimal non-CM curves N<500000: ns3 (two quadratics) iff 3Ns: 1,697/1,697, 0 disagreements either way; psi_3 irreducible with Galois group D4 iff 3Nn: 3,695/3,695, 0 disagreements; every 3-label has the expected factor pattern | MATCH | stage3_ns3.py | stage3_ns3.txt |
| 8 | sec:eis | 6942n1: deg 65664 = 2^7 3^3 19, 9-point, 3B.1.1, D=2 | table deg 65664 = ellmoddegree, factor 2^7 3^3 19; torsion Z/9; 3B.1.1; D=2 (G=5, V=3) | MATCH | stage3_eis.py, stage3_moddeg_sample.py | stage3_eis.txt, stage3_moddeg_sample.txt |
| 9 | rem:degree | c_E=1 formula reproduces deg to 30 digits for 11a1, 121a1, 539d1, 1232l1, 726a1 | at 60 digits: relative error 1.7e-63, 5.9e-62, 1.7e-63, 2.8e-61, 3.6e-62 (agreement to the working precision) | MATCH | stage3_petersson.py | stage3_petersson.txt |
| 10 | sec:data | checks below 10,000 under 2.17.2 reproduce the 2.15 counts on all 38,042 optimal curves; ellmoddegree agrees with the tables on all | PARI 2.15.4 obtained (cypari2 2.2.0 wheel, Python 3.12 venv); 38,042 curves: ellmoddegree, ns3, rule(E,l) and rule(E,l,1) for l=3..13 identical under 2.15.4 and 2.17.2; ellmoddegree = table on 38,042/38,042 under both; pari_features.gp block 00000-09999 byte-identical | MATCH | stage3_rule_versions.py, stage3_rule_versions_compare.py | stage3_rule_v215.txt, stage3_rule_v217.txt, stage3_versions.txt |

## Findings beyond the verdicts

- **galrep label spelling.** Above N = 400000 the galrep labels of the tables are written without dots (`3Cs11`, `3B11`,
  `37B81`), below with dots (`3Cs.1.1`, `3B.1.1`). `scripts/conj_check.py` matches `\b3Cs\.1\.1\b` only, so on the extension
  the split-Cartan term of conj:eis is 0 for the one optimal curve labelled `3Cs11` (and `step6_*`/`step7_eis_proxy.py` likewise).
  It makes the bound smaller, and the committed result (no violation on the extension) is unaffected; the `3Ns`/`3Nn` labels
  have no dots in either range, so step 11 is unaffected. `stage3_eis.py` matches both spellings.
- **sec:two, extension: 19, not 20.** The 20th exception is 401291a1 (Kodaira [I1, I0*], deg 1389850), curve 1 of a class
  whose optimal curve is not determined in the tables (optimal flag empty); the original count evidently included it, the
  stated population (313,741) does not.
- **"18 optimal curves with a point of order 9"**: 18 counts every curve with a 9-point and N <= 400000; 14 of them are optimal.
- `results/check_work_perl.parquet` is missing after the rerun: `repro_run.sh` was killed (out of memory) while
  `conj_check.py work` wrote it (logs/repro_run_*/repro_run.log); the summary CSV had been written and compared. The
  stage 3 Eisenstein counts were recomputed directly from `results/optimal_work.parquet`.
- Theorem thm:twist: the same checks at q = 3 (156,462 I_n* and 236,278 potentially good pairs) also give no violation and
  equality in every case (c) pair.

## Item 10: PARI 2.15

PARI 2.15.4 was obtained in a few minutes: the cypari2 2.2.0 manylinux wheel (no cp313 build exists; installed into a
Python 3.12 venv under the scratchpad with uv) bundles PARI 2.15.4. With it and with 2.17.2 (`stage3_rule_versions.py`,
same code, about 82 min each, run in parallel):
- all 38,042 optimal curves with N < 10000: `ellmoddegree` equals the table degree for every curve under both versions;
  `ns3(E)` and the bounds `rule(E,l)`, `rule(E,l,1)` of `scripts/euler_rule.gp` for l = 3, 5, 7, 11, 13 are identical
  curve by curve (0 differences in any column); no violation of either form at any l (E[l] irreducible, not CM).
- `scripts/pari_features.gp` on `allcurves.00000-09999` (64,687 curves, 38,042 a_p rows) under 2.15.4 is byte-identical
  to `data/pari/{curves,ap}.00000-09999.tsv` written by 2.17.2 in the stage 1 rerun.
- In addition, the whole pipeline (originally run with 2.15) has just reproduced every committed summary and table byte
  for byte under 2.17.2, which already compares the two versions on the full ranges.
The per-curve CSVs (`rule_v215.csv`, `rule_v217.csv`) and `c215.tsv`, `a215.tsv` are in the scratchpad, not in `results/`.
`stage3_rule_versions.py` evaluates `euler_rule.gp` with two mechanical changes (bound returned without the degree, which
is computed once per curve, and `lfunsympow(E,2)` computed once per curve); a first run without the caching was stopped
after 30 min (logged).

## Output sizes

All stage 3 outputs in `results/` are small (largest: `stage3_twist_degree_viol.csv`, header only;
`stage3_eis_D2.csv` 22 rows; `stage3_moddeg_sample.csv` 63 rows). Per-curve detail of item 10 (38,042 rows per version)
and the 2.15 feature files are in the scratchpad, not in `results/`.
