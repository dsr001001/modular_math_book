# samples/: wild local factors at q = 2 and q = 3

`wild_euler_q23.csv` makes the terms at the wild primes 2 and 3 reproducible for a fixed sample of curves: for each curve
and each q in {2, 3} at which the curve has additive reduction, the polynomial P_q(X) with
L_q(Sym^2 f, s) = P_q(q^{-s})^{-1} as PARI computes it, the value P_q(q^{-2}) as an exact rational, and the Euler terms
e_l(E, q) = v_l(P_q(q^{-2})) for l = 3, 5, 7 (paper, Definition `def:terms`; at an additive prime a_q = 0, so the naive
factor is 1). `wild_euler_q23.log` is the standard output of the run that wrote it (the checks below and a count by type).

## Regenerate

From `final/pipeline`, after `../../tools/setup_env.sh` (which fetches Cremona's ecdata files for N < 10,000 at the pinned
commit `25cec5ecfec8b9f016eb1631ac633194c2bed39f` into `../../data/ecdata`):

```
python3 scripts/wild_euler_samples.py > samples/wild_euler_q23.log      # optional argument: the ecdata directory
```

It takes about a second, writes `samples/wild_euler_q23.csv` and exits nonzero if any check fails. The output contains no
timestamp; two runs give identical files. Without the ecdata files only the curves named in the paper are computed, from
the a-invariants listed in the script (PARI's `elldata` package is not used; it is not installed in the reference
environment).

Reference environment: PARI 2.17.2 through cypari2 2.2.4, Python 3.13.16 (recorded in the header of the CSV).

## Sample (fixed rule)

- **paper**: every curve of the tables named in `../paper/note.tex` (the list `PAPER_CURVES` in the script; the class 54a is
  taken whole, since the paper gives the types of its three curves at 3), kept if it has additive reduction at 2 or 3:
  36 curves. 121a1 and 726a1 are named in the paper but have no additive reduction at 2 or 3, so they give no row.
- **rule**: every X_0(N)-optimal curve (flag 1 in ecdata `opt_man`) of conductor N < 2,000 without complex
  multiplication (j not one of the 13 rational CM j-invariants) with 4 | N or 9 | N: 2,882 curves.

A curve in both sets has `sample = paper+rule`. In all: 2,905 curves, 3,305 rows (1,971 at q = 2, 1,334 at q = 3), sorted
by conductor, class, curve number and q.

## File format

Lines starting with `#` are a header: the PARI and cypari2 versions, the input files with their SHA-256, the selection
rule, and the PARI commands used, in GP form (the script makes the same calls through cypari2; read it with
`pandas.read_csv(path, comment="#")`). The commands are those of `scripts/step10_sym2_euler.py`:
`L = lfunsympow(ellinit(ainvs), 2)`, `P = 1/lfuneuler(L, q)`, coefficients `Vec(Pol(P))` reversed (ascending powers of X).

| column | content |
|---|---|
| `label`, `ainvs`, `N`, `cm` | Cremona label, a-invariants, conductor, 1 if CM (only among the paper's curves) |
| `sample` | `paper`, `rule` or `paper+rule` |
| `q`, `cond_exp` | the prime, the exponent of q in N (`elllocalred(E, q)[1]`) |
| `kodaira`, `kodaira_code`, `tamagawa` | Kodaira symbol, PARI's code (`elllocalred(E, q)[2]`, checked equal to the code in `ellglobalred(E)[5]`), c_q |
| `v_q_j` | v_q(j_E), `inf` when j = 0 |
| `a_q` | `ellap(E, q)`, always 0 here |
| `P_coeffs`, `P_poly` | coefficients of P_q(X) in ascending powers, and the polynomial written out |
| `P_at_q_minus2` | P_q(q^{-2}) as an exact fraction |
| `e_3`, `e_5`, `e_7` | v_l(P_q(q^{-2})); empty when l = q (Definition `def:terms` defines e_l only for q != l; at q = l = 3 the paper uses the empirical weights w_3) |
| `shape`, `shape_param` | the shape of Proposition `prop:shapes` (i)-(iv) read off the coefficients; a for (ii), c for (iii) |
| `twist_D`, `twist_a` | a quadratic twist (discriminant D in {-4, 8, -8} at q = 2, D = -3 at q = 3) with good reduction at q, and its a_q, when one exists |
| `shape_check` | `ok`, or the reason the row does not fit the proposition |

## Relation to the paper and checks

The paper takes the terms at 2 and 3 from PARI's Euler factor (Definition `def:terms`, Section `sec:wild`), and
Proposition `prop:shapes` says that P_q has one of four shapes at every bad prime, 2 and 3 included:
(i) 1 - X when v_q(j) < 0; (ii) (1 - qX)(1 - (a^2 - 2q)X + q^2X^2), a = a_q(E') for a quadratic twist E' with good reduction
at q; (iii) 1 - cqX with c = ±1; (iv) 1. The script checks, for every row:

- the coefficients have one of the four shapes, with a an integer, a^2 <= 4q, in (ii);
- shape (i) occurs exactly when v_q(j) < 0;
- for shape (ii), one of the twists listed above has good reduction at q and its a_q reproduces the cubic; for shapes
  (iii) and (iv), none of them has good reduction at q (otherwise the inertia image would be {±1});
- e_l agrees with the formula of the shape;
- `ellglobalred` and `elllocalred` give the same Kodaira code; a_q = 0; the string form
  `1/lfuneuler(lfunsympow(ellinit(ainvs), 2), q)` of `scripts/selftest.py` gives the same polynomial as the step 10 calls.

Result of the committed run: **no row fails**; 0 shape mismatches among the 3,305 rows.

Statements of the paper at q = 2, 3 (all hold):

| statement (paper) | sample |
|---|---|
| type IV or IV* at 2 has P_2 = 1 + 2X, e_3 = 1 (Lemma `lem:IV`, Remark `rem:wild`) | 498 of 498 rows |
| 336f1, type II at 2: P_2 = 1 + 2X, e_3(E,2) = 1 (Remark `rem:wild`) | as stated |
| 1232l1, type II* at 2: P_2 = (1 - 2X)(1 + 2X)^2 = 1 + 2X - 4X^2 - 8X^3, e_3(E,2) = 2 | as stated; P_2(1/4) = 9/8 |
| 592c1, type II* at 2: P_2 = (1 - 2X)(1 + 4X^2), e_5(E,2) = 1 | as stated; P_2(1/4) = 5/8 |
| 52a1, type IV* at 2, e_3(E,2) = 1 (Example `ex:qual`(a)) | P_2 = 1 + 2X |
| 54a: types IV*, II*, II at 3 (Section `sec:data`) | 54a1 IV*, 54a2 II*, 54a3 II; P_3 = 1 for all three |
| CM curves with image N_s(F_3) and R = {2}: type III at 2, P_2 = 1 + 2X (Proposition `prop:ns-structure`(ii) and the paragraph after it, Section `sec:boundary`): 256a1, 256d1, 2304c1, 2304k1, 6400f1, 6400r1 | as stated |
| 2178b1, 2178h1: t_3(E,3) = 1 from a type I_n* at 3 (Section `sec:anomaly`) | type I3*, v_3(j) = -3, shape (i) |

Count by type on the `rule` part of the sample (from `wild_euler_q23.log`): at q = 2, types II and II* have P_2 = 1 in
230 of 315 rows, 1 + 2X in 59 and a cubic in 26 ("usually P_2 = 1", Remark `rem:wild`); types IV and IV* always 1 + 2X;
type I_n* (n >= 1) is potentially multiplicative (shape (i)) in 172 of 503 rows. At q = 3 every type I0* row has a cubic
(185 rows), every type III or III* row has 1 + 3X (238 rows), and the types II, II*, IV, IV* have 1 or 1 ± 3X.

## Step 10 parquet files

`step10_sym2_euler.py` writes `results/sym2_<set>_<shard>.parquet`, which are git-ignored and not committed (README,
"Inputs that are not committed"), and none is present in this directory. The sample therefore cannot be compared row by
row with the committed step 10 output; it uses the same PARI calls on the same a-invariants, and its q = 2 polynomials for
336f1, 1232l1 and 592c1 agree with the check in `scripts/selftest.py` (`results/selftest.log`).
