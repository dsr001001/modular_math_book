# Chapter 22: Computation, data and the statistical protocol (`ch:computation`, `chapters/ch22_computation.tex`)

Stage 1 line-up. Part VI, last chapter, after Chapter 21 (the guided tour). Chapter 21 explains what each computational
statement of the paper means and what it tests; this chapter explains how to run every computation, how to read
Cremona's data files, and how to judge the paper's protocol and statistics. Target length 1,940 lines of LaTeX (card
excluded; Part 3), inside the 1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags, as in the Chapter 13 to 19 outlines: **P** = proved here, **S** = proof sketched here, **R** = stated;
reference. Two further tags are used for computational items, and each maps to one of the three tags PLAN.md allows on
the card: **C** = computed here (a session or count whose exact output is printed and was reproduced for this outline,
Part 7; on the card it is tagged *(proved here)*, the proof being the printed computation) and **D** = data reported
by the paper and not reproducible in this book beyond conductor $10{,}000$ (on the card: *(stated; reference)*, the
reference being the paper's Section 6). Item format: number, label-ready name, kind, tag; the precise statement or
description; reference; the paper's use by its `\label` names. Every number below marked C was produced by the scripts
of Part 7 with PARI/GP 2.17.2 (through `cypari2` 2.2.4) and Cremona's `ecdata` files for conductor below $10{,}000$ in
`/tmp/ch09/data`.

## 1. Purpose and global conventions

### 1.1 What this chapter is for

The paper's Section 6 (sec:data and its eight subsections, five tables), its appendix (the GP functions `rule(E, l,
iii)` and `ns3(E)`) and a dozen sentences elsewhere ("PARI's `lfunsympow(E,2)` returns these factors at every prime";
"In each case the values were confirmed against PARI's `lfunsympow` on every curve of the tables"; "PARI's factor at
$2$ is $1+2X$ for every one of them"; "checked for $p<500$") rest on software and data that the reader has never used,
and on a statistical protocol that the reader's basic statistics course equips them to judge. The chapter has four
jobs.

1. **Tools.** PARI/GP from zero, with exactly the functions the paper and the book use (`ellinit`, `ellglobalred`,
   `elllocalred`, `ellap`, `ellan`, `elltors`, `ellisomat`, `elldivpol`, `factor`, `valuation`, `elltwist`,
   `ellminimalmodel`, `lfunsympow`, `lfuneuler`, `lfunparams`, `ellinit` over $\Q_q$ and `.tate`, `ellmoddegree`,
   `ellweilcurve`), and Cremona's `ecdata` files (formats as found, Part 7). This discharges the deferrals of Chapters 2,
   3, 9, 10, 11, 12, 13, 14, 15, 17, 18 and 19 (Part 5).
2. **The appendix, line by line.** `rule(E, l, iii)` and `ns3(E)` are printed verbatim, read line by line as code (the
   mathematics of each line is Chapter 19's 11.2 and Chapter 21's A9.1, cited, not repeated), proved to compute the
   right side of (eq:rule) and of its III-free form under stated conditions, and run on the running examples 121a1,
   726a1, 539c1, 980i1, 99a1, 336f1, 1232l1, 592c1 and 11a1, with every term accounted for. The pitfalls (non-optimal
   models, CM curves, Eisenstein curves, the class 990h) are shown by running the function where it gives the wrong
   answer.
3. **The protocol and the statistics.** Working set, hold-out, extension and out-of-table curves; pre-registration;
   which statement was blind-tested, which only confirmed, which is a theorem merely checked; base rates, equality
   rates, the mean excess; the calibration argument of Section sec:sharp made exact (null model, expectation by
   linearity, variance, the choice of reference population, a permutation version); multiple comparisons; and an honest
   list of what the data do and do not show. Appendix A (`ch:prereq`, its Section on probability and statistics, already
   written) supplies the vocabulary (base rate, hypothesis test, hold-out, pre-registration, linearity of expectation,
   Markov and Chebyshev); this chapter applies it and does not restate it.
4. **Reproduction.** A small version of the paper's tables (tab:uniform, tab:counts, tab:ns, tab:iso, the Tamagawa test of
   sec:tam, the Eisenstein counts of sec:eis, the twist data after Theorem thm:twist, the calibration statistic and the
   odd-part statistic of sec:sharp) on all $38{,}042$ optimal curves of conductor below $10{,}000$, with the scripts that
   produce them, a comparison with the paper's numbers, and a reproducibility checklist. Every count of the paper on the
   large ranges is quoted as data (tag D); the book's own counts (tag C) are what the reader can rerun in minutes.

**The physics reader** knows the situation from experimental practice: a blinded analysis with a signal region kept
closed until the selection is frozen is the hold-out; "unblinding" is the one-time test; a look-elsewhere correction is
the multiple-comparisons caveat (one sentence each in Sections 9 and 10, no more).

### 1.2 Global conventions fixed in this chapter

* **K1 (software and versions).** The paper used PARI/GP 2.15 and `ecdata` at commit `25cec5e` (Section sec:data, the
  appendix). The book's outputs were produced with PARI/GP 2.17.2 through `cypari2` 2.2.4 (Python 3.13), and with a
  local copy of six `ecdata` files for conductor below $10{,}000$ whose commit is not recorded (Part 6.5: the writer must
  pin it). Every printed output says which version produced it. Where 2.15 and 2.17 may differ (the return type of
  `ellmoddegree`, the availability of `readstr` and `strsplit`, the memory needed by `ellmoddegree`), the chapter says
  so and the writer checks the 2.15 manual.
* **K2 (models and labels).** Curves are given by Cremona's reduced global minimal models $[a_1,a_2,a_3,a_4,a_6]$
  (Chapter 9, C3; Chapter 10). Labels are Cremona's (`\curve{121a1}`, macro `\curve` in `preamble.tex`); the LMFDB's
  labels appear only in Section 4. "Optimal" means $X_0(N)$-optimal (Chapter 14).
* **K3 (the quantities).** $v_\ell$ is the $\ell$-adic valuation; $e_\ell(E,q)$, $t_\ell(E,q)$ (also at $q=\ell$, point 53),
  $w_3(E)$, $h_\ell(E)$ as in Definition def:terms and Conjecture conj:euler (Chapter 19, 9.1; Chapter 21, A1);
  $w_\ell(E,q)$ and $\Phig_q$ as in Section 1.4 of the paper (Chapter 10). For a curve $E$ and an odd prime $\ell$ the
  chapter names five bounds: $B^{\mathrm{rule}}_\ell(E)$ = right side of (eq:rule) = the second entry of `rule(E,l,1)`;
  $B^{\mathrm{nc}}_\ell(E)=B^{\mathrm{rule}}_\ell(E)+h_\ell(E)$ (no correction; "all types, no correction" of Section
  sec:anomaly); $B^{\mathrm{III}}_\ell(E)$ = second entry of `rule(E,l)` (types $\mathrm{III}$, $\mathrm{III}^*$ left out at
  $q\ne\ell$, no correction); $B^{\mathrm{main}}_\ell(E)=\sum_qv_\ell(\#\Phig_q)$ (eq:main); $B^{\mathrm{tw}}_\ell(E)=\sum_qw_\ell(E,q)$
  (eq:twist). The value $v=v_\ell(\degphi)$ is the *observed valuation*.
* **K4 (violation, equality, excess).** For a curve with bound $b$ and observed valuation $v$: a *violation* is $v<b$; an
  *equality* is $v=b$ with $b>0$; the *excess* is $v-b$. Rates are always among curves with $b>0$, as in the paper.
* **K5 (populations).** The *base population at $\ell$* is the set of optimal curves (one per isogeny class) without CM
  whose mod $\ell$ representation is irreducible; CM is decided by $j$ (the thirteen CM $j$-invariants, Chapter 9),
  irreducibility by the `galrep` labels (reducible iff a label starts with "$\ell$B" or "$\ell$Cs"; Section 4). The
  *Eisenstein population at $\ell$* is the optimal non-CM curves with reducible mod $\ell$ representation. The *hypothesis
  population* adds $\ell\nmid N$ and, at $\ell=3$, image not 3Ns (Theorem thm:main; important_notes.md point 47).
* **K6 (ranges).** The paper's ranges: working set $N\le300000$, hold-out $300000<N\le400000$, extension
  $400000<N\le500000$, out-of-table $500000<N\le4\cdot10^6$. The book's: $N<5000$ ("small working set"), $5000\le N<10000$
  ("small hold-out"), and their union. The book's split is for teaching only: nothing was discovered on it.
* **K7 (Kodaira codes).** PARI's codes as in Chapter 10, item 5.5 (cited, not reprinted in full): $1$ for $\mathrm I_0$,
  $n+4$ for $\mathrm I_n$ and $-(n+4)$ for $\mathrm I_n^*$ when $n\ge1$, $-1$ for $\mathrm I_0^*$, $\pm2,\pm3,\pm4$ for
  $\mathrm{II}/\mathrm{II}^*$, $\mathrm{III}/\mathrm{III}^*$, $\mathrm{IV}/\mathrm{IV}^*$ (point 52). The idioms used in code: `k >= 5` iff
  multiplicative; `k <= -5` iff $\mathrm I_n^*$, $n\ge1$; `abs(k) == 3` iff $\mathrm{III}$ or $\mathrm{III}^*$.
* **K8 ($P_q$ and the symmetric square).** As Chapter 19, C4 and C5: `lfuneuler(lfunsympow(E,2), q)` is $1/P_q(x)$ with
  $x=q^{-s}$, and $P_q(q^{-2})=L_q(A_f,1)^{-1}$. This chapter never re-derives a factor; it computes and cites.
* **K9 (code typography).** GP code in `lstlisting` with `language=GP` (defined in `preamble.tex`), Python in
  `lstlisting` without language or in `verbatim`; GP comments start with `\\`. No code line contains two consecutive
  hyphens (decrement is written `k -= 1`, never with the double-hyphen operator), so that even code blocks pass a strict
  dash grep. Outputs are printed exactly as PARI prints them.
* **K10 (statistics vocabulary).** As Appendix A (`ch:prereq`): definitions def:prereq:prob, def:prereq:test,
  def:prereq:holdout, theorem thm:prereq:expectation, example ex:prereq:calibration, paperlink pl:prereq:protocol. Cite them
  by `\Cref{ch:prereq}` only (cross-chapter rule of PLAN.md 7.1); never restate the definitions.
* **K11 (typography).** PLAN.md 7.2: plain hyphens ("Agashe-Ribet-Stein", "Fontaine-Perrin-Riou"); ranges "1 to 8";
  labels `...:computation:...`; ASCII source; numbers with thousands separators as `{,}` in math or plain commas in text,
  as the paper does.

________________________________________________________________________________

## 2. Line-up of the core items, in teaching order

### Section 1. Introduction and conventions

**1.1 `conv:computation:versions`** (convention; P as a record). K1 and K2 as one `convention` environment: the versions
(PARI/GP 2.15 for the paper, 2.17.2 for the book), the data (`ecdata` commit `25cec5e` for the paper; the book's pinned
commit, to be filled in by the writer, with the SHA-256 sums of the six files used, Part 6.5), and the rule that every
printed output names its version. Paper: Section sec:data ("PARI/GP 2.15", "commit 25cec5e"), the appendix.

**1.2 `conv:computation:bounds`** (convention; P as a definition). K3 and K4: the five bounds $B^{\mathrm{rule}}$,
$B^{\mathrm{nc}}$, $B^{\mathrm{III}}$, $B^{\mathrm{main}}$, $B^{\mathrm{tw}}$, the observed valuation, violation, equality, excess, and the
rule that rates are among positive bounds. One sentence: (eq:thm) is $B^{\mathrm{nc}}$ restricted to $q\ne\ell$ with no $w_3$
term, which agrees with $B^{\mathrm{nc}}$ whenever $\ell\nmid N$. Paper: Section sec:data, all tables.

**1.3 `conv:computation:populations`** (convention; P as a definition). K5 and K6, with the counts of the book's base
populations below conductor $10{,}000$ (C): $38{,}042$ optimal curves, of which $189$ CM; base population at $\ell=3$:
$33{,}851$; Eisenstein population at $\ell=3$: $4{,}002$; at $\ell=5,7,11,13$ the base populations have $37{,}319$, $37{,}691$,
$37{,}839$, $37{,}823$ curves. Paper: Section sec:data ("curves with $E[\ell]$ irreducible, not CM").

### Section 2. PARI/GP from zero

**2.1 `rem:computation:install`** (remark; R, with the book's setup C). (i) Two ways to run PARI: the `gp` interpreter
(Debian/Ubuntu package `pari-gp`; the PARI web site for other systems; the writer gives no version-specific install
command it has not run) and the Python package `cypari2` (`pip install cypari2`; then `import cypari2; pari =
cypari2.Pari()`; `pari('...')` evaluates any GP expression; `pari('read("file.gp")')` loads a GP file). The book's
outputs come from the second route (Part 7). (ii) Optional data packages: `elldata` (Cremona's tables inside PARI, needed by
`ellsearch` and `ellidentify`) and `galdata`. Without `elldata`, `ellsearch(11)` fails with "error opening elldata file"
(C: this is the state of the book's installation), which is why the chapter reads `ecdata` files directly (Section 4)
instead of using `ellsearch` as PLAN.md suggests. (iii) Memory: `parisize` (current stack) and `parisizemax` (the
ceiling to which PARI may grow the stack); defaults in the book's installation: 8,000,000 bytes and 8,003,584 bytes;
`default(parisizemax, 10^9)` in GP or `pari.allocatemem(10**9)` in Python. Reference: PARIusers (cite the chapters on
defaults and on elliptic curves; no section numbers unless checked). Paper: the appendix ("`ellmoddegree` needs
`parisizemax` of a few hundred megabytes").

**2.2 `rem:computation:gp-language`** (remark; P as a description). The part of the GP language the chapter needs, in
one page: integers and rationals are exact; `x` is a reserved polynomial variable (never assign to it: `lfuneuler`
returns rational functions in `x`); vectors `[a, b]` are 1-indexed, `#v` is the length, `v[2..#v]` a slice; matrices
`[1, 2; 3, 4]`, `M[i, j]`, a column `M[, 1]`; functions `f(a, {b = 0}) = ...` with optional arguments; local variables
`my(...)`; braces `{ ... }` for a definition spanning several lines in a file; comments `\\ ...` to the end of the line;
`if(c, a, b)`, `for(i = 1, n, ...)`, `foreach(v, s, ...)`, `next`; `Map()` with `mapput`, `mapisdefined`; strings with
`Str`, `strsplit`, and `readstr(file)` (a vector of the lines of a file; available in 2.17.2, verify in 2.15);
`valuation(r, l)` for rationals ($v_\ell(0)$ is `+oo`, so tests like `vj < 0` are false at $j=0$); `factor`; `kronecker`;
`O(q^k)` for $q$-adic precision. Paper: the appendix (every construct of `rule` is in this list).

**2.3 `ex:computation:first-session`** (worked example; C). On 121a1 $=[1,1,1,-30,-76]$: `E = ellinit([1,1,1,-30,-76])`;
the member functions `E.a1`, ..., `E.a6`, `E.b2`, `E.c4`, `E.c6`, `E.disc`, `E.j` give $1,1,1,-30,-76$, $b_2=5$,
$c_4=1441$, $c_6=54703$, $\Delta=-121$, $j=-24729001$; `ellan(E, 12)` gives `[1, -1, 2, -1, 1, -2, 2, 3, 1, -1, 0, -2]`
($a_{11}=0$: additive at $11$); `ellap(E, 2)` $=-1$. On 726a1: `elltors(E)` $=$ `[2, [2], [[6, -3]]]` (torsion $\Z/2$ generated by
$(6,-3)$); `ellisomat(E)[2]` $=$ `[1, 2; 2, 1]` (class 726a has two curves joined by a $2$-isogeny); on 11a1 the matrix is
`[1, 5, 5; 5, 1, 25; 5, 25, 1]`, matching `ecdata`'s `allisog` (item 4.1). Paper: the appendix (`ellinit`, `E.j`).

**2.4 `warn:computation:pitfalls`** (warning; P). (a) `ellinit` accepts any model; `ellglobalred` reports the change to a
minimal model, and `ellminimalmodel` returns it; local data are always those of the minimal model. (b) Do not assign to
`x`. (c) $q$-adic objects carry precision `O(q^k)`; results are correct only to that precision. (d) Stack overflow is an
error, not a wrong answer: raise `parisizemax`. (e) GP is 1-indexed, Python 0-indexed: `R[4][,1]` in GP is
`R[3][:,0]` in `cypari2`. (f) `factor` of a polynomial with integer coefficients returns the irreducible factors over
$\Q$ without the content: `factor(3*x^4 + 6)` is `Mat([x^4 + 2, 1])` (C); this is what makes `ns3` independent of the
leading coefficient $3$ of $\psi_3$. Paper: the appendix.

### Section 3. Invariants of a curve in PARI

**3.1 `def:computation:ellglobalred`** (definition of the output; C). `ellglobalred(E)` returns
`[N, [u, r, s, t], c, faN, L]`: the conductor, the change of variables to a global minimal model, the product
$c=\prod_pc_p$ of the Tamagawa numbers, the factorisation matrix of $N$ and the vector $L$ of local data, $L[i]=$
`elllocalred(E, p_i)` $=[f_p,k_p,[u,r,s,t],c_p]$ (conductor exponent, Kodaira code, local change of variables, Tamagawa
number). So the paper's `R[4][,1]` is the column of bad primes and `R[5][i][2]` (written `K[i][2]`) the Kodaira code at
the $i$-th one. Exact output for 726a1 (C, 2.17.2): `[726, [1, 0, 0, 0], 4, [2, 1; 3, 1; 11, 2], [[1, 10, 0, 2], [1, 7,
0, 1], [2, 3, 0, 2]]]` (types $\mathrm I_6$, $\mathrm I_3$, $\mathrm{III}$; $c_2=2$, $c_3=1$, $c_{11}=2$; PARI prints a trivial change of
variables as `0`); `elllocalred(ellinit([0,1,0,4,4]), 2)` $=$ `[2, -4, [1, 0, 0, 0], 3]` (20a1: $\mathrm{IV}^*$, $f_2=2$, $c_2=3$). The
mathematics (Tate's algorithm, $\Phig$ versus $c_q$) is Chapter 10's (its 5.2, 5.5, 10.2); this item is the data structure
only. Paper: the appendix (`R = ellglobalred(E)`, `P = R[4][,1]`, `K = R[5]`, `K[i][2]`), Section sec:data ("The Kodaira types
and discriminant exponents at the bad primes were recomputed with PARI/GP 2.15 from the $a$-invariants").

**3.2 `conv:computation:code-idioms`** (convention; P). K7 with a five-line table of the tests used in `rule` and in the
book's scripts (code test, Kodaira types selected, paper term affected): `k >= 5` ($\mathrm I_n$, $n\ge1$: divide by the naive
factor; $\#\Phig=n=k-4$); `k <= -5` ($\mathrm I_n^*$, $n\ge1$: $n=-k-4$); `k == -1` ($\mathrm I_0^*$); `abs(k) == 3` ($\mathrm{III}$, $\mathrm{III}^*$:
skipped unless `iii`); `k == 4 || k == 2` / `k == -4 || k == -2` / `k == -3` (the weights $w_3=1$, $2$, $1$ at $q=\ell=3$). Point 52
($n+4$ and $-(n+4)$ only for $n\ge1$) in one sentence. Full dictionary: Chapter 10, 5.5. Paper: the appendix ("Here `K[i][2]` is
PARI's Kodaira code ...").

**3.3 `rem:computation:lfunsympow`** (remark; C, mathematics cited from Chapter 19). `S = lfunsympow(E, 2)` is an
$L$-function object for $L(\Sym f,s)$ in the normalisation of Chapter 19, C4: `lfunparams(S)` is `[121, 3, [0, 0, 1]]` for
121a1 (conductor, motivic weight $3$, gamma shifts). `lfuneuler(S, q)` is the Euler factor as a rational function of
$x=q^{-s}$: for 121a1, `lfuneuler(S, 11)` $=$ `1/(11*x + 1)` and `lfuneuler(S, 2)` $=$ `1/(-8*x^3 - 2*x^2 + x + 1)` (a good prime,
$a_2=-1$: $P_2(X)=(1-2X)(1+3X+4X^2)$). Hence $P_q(q^{-2})$ is `subst(1/lfuneuler(S, q), x, 1/q^2)` (exact rational: $12/11$
at $q=11$), and $e_\ell(E,q)$ = `valuation(` that `/ (1 - a_q^2/q^2), l)` (Definition def:terms; Chapter 19, 11.1). Cost: the
factors at the bad primes are computed when `S` is created; creating `S` and reading all bad factors took about $0.2$
milliseconds per curve below conductor $10{,}000$ (C). `lfun(S, 2)` is $L(\Sym f,2)$, used by `ellmoddegree` (3.8). Paper:
Section 1.1 ("PARI's `lfunsympow(E,2)` returns these factors at every prime, including $2$ and $3$"), Section sec:data,
the appendix (`S = lfunsympow(E, 2)`, `F = 1/lfuneuler(S, q)`, `r = subst(F, x, 1/q^2)`).

**3.4 `ex:computation:euler-by-hand`** (worked example and check; C). For $q\ge5$ the factor is read off the Kodaira type
(Lemma lem:euler; Chapter 19, 9.3): a GP function `euler_by_type(E, q)` returning $L_q(A_f,1)^{-1}$ from the code, from
$\chi_{-3}(q)$, $\chi_{-4}(q)$ (`kronecker(-3, q)`, `kronecker(-4, q)`) and, for $\mathrm I_0^*$, from $a'=$ `ellap(ellinit(elltwist(E,
q*)), q)` with $q^*=$ `if(q % 4 == 1, q, -q)`; compared with 3.3 on every pair (optimal curve of conductor below $10{,}000$,
bad prime $q\ge5$): $67{,}745$ pairs ($\mathrm I_n$ $58{,}860$, $\mathrm I_n^*$ $2{,}709$, $\mathrm{II}$ to $\mathrm{IV}^*$ $3{,}588$, $\mathrm{III}$, $\mathrm{III}^*$
$1{,}676$, $\mathrm I_0^*$ $912$), no mismatch (C). Chapter 19's 9.3 did the same on all $64{,}687$ curves ($117{,}232$ pairs); this
item is the reader's version of that check and of the paper's sentence. Paper: Lemma lem:euler ("In each case the values
were confirmed against PARI's `lfunsympow` on every curve of the tables"), the appendix (last sentence).

**3.5 `ex:computation:tate-parameter`** (worked example; C). `Eq = ellinit(E, O(q^30))` is $E$ over $\Q_q$ to precision
$q^{30}$; for multiplicative reduction (split or nonsplit) `Eq.tate[3]` is the Tate parameter $q_E\in\Q_q$, with
$v_q(q_E)=n=-v_q(j)$ (Chapter 10, 7.3, 7.4; the series $\mathsf q(j)$ of Chapter 10, 7.2 gives the same $q_E$, as Chapter 18's verification log checked). The GP
function `tatedata(E, q, l)` (S2) returns $[n,q_E,\bar u,k]$ with $\bar u$ the reduction of the unit part $q_Eq^{-n}$ and $k$ the
largest $k\le v_\ell(q-1)$ such that $\bar u$ is an $\ell^k$-th power in $\F_q^\times$ (test: $\bar u^{(q-1)/\ell^k}=1$). Outputs (C): 11a1 at
$11$, $\ell=5$: $n=5$, $q_E=10\cdot11^5+2\cdot11^6+\cdots$, $\bar u=10$, $k=1$; 77c1 at $7$ ($a_7=-1$, nonsplit): $[3,\dots,5,0]$; 539c1 at $7$:
the same $q_E$ as 77c1 (its twist), $\bar u=5$, $k=0$; 791a1 $=[1,0,1,-31,117]$ at $7$: $\bar u=6$, $k=1$; 1577a1 $=[0,-1,1,30,-335]$ at $19$:
$\bar u=8$, $k=1$. These agree with Chapter 17, 5.5 and Chapter 18, 8.5. Warning (one sentence, PLAN.md): `elltatepairing` is
the Tate pairing on torsion points and has nothing to do with the Tate parameter. Notation: the class of $\bar u$ is
written $c(u)$, never $c_q$ (points 23, N9 of Chapter 21). Paper: Section sec:data ("the Tate parameters with `ellinit`
over $\Q_q$"), Section sec:tam, Lemma lem:tamfactor, Remark rem:ko(1).

**3.6 `ex:computation:mod3-image`** (worked example and check; C). `elldivpol(E, 3)` is $\psi_3$ (degree $4$, leading
coefficient $3$); `factor` gives the pattern. 726a1: $\psi_3=3x^4+5x^3-210x^2-612x-1480=(x^2-x-74)(3x^2+8x+20)$, pattern
$2+2$, so `ns3` $=1$ (image 3Ns, Proposition prop:ns). `polgalois` needs an irreducible polynomial and raises an error on
726a1's $\psi_3$ (C): use it only on irreducible $\psi_3$ (Chapter 11, 7.3 for the pattern-to-image table, cited). Check (C):
among the $37{,}853$ non-CM optimal curves below $10{,}000$, `ns3(E) = 1` exactly for the $90$ curves whose `galrep` entry
contains 3Ns (no mismatch either way); among the $189$ CM optimal curves `ns3` is $1$ for $13$ (all with $j=-32768$ or
$8000$, e.g. 121b1, 256a1), which `galrep` does not label (CM caveat, Chapter 11's B7). Paper: the appendix (`ns3`),
Section sec:data ("The mod 3 images of the tables were checked against the factorisation of the 3-division polynomial"),
Proposition prop:ns, Section sec:anomaly.

**3.7 `ex:computation:twists`** (worked example and check; C). `elltwist(E, d)` is the quadratic twist by $\Q(\sqrt d)$ (a
model, not necessarily minimal; `ellminimalmodel` normalises it; `ellglobalred` of the twist gives its conductor). The
GP function `twistcheck(E)` (S2) lists, for each odd bad prime $q$, the codes of $E$ and of $E\otimes\chi_{q^*}$ at $q$ and the
conductor of the twist: 121a1 gives `[[11, 2, -4, 121]]` ($\mathrm{II}\to\mathrm{IV}^*$, conductor unchanged); 539c1 gives `[[7, -7, 7, 77],
[11, 6, -6, 5929]]`; 980i1 gives `[[5, 5, -5, 4900], [7, -9, 9, 140]]`. Check of Lemma lem:twist (i), (ii) on all optimal
curves below $10{,}000$ (C): $85{,}848$ pairs (curve, odd bad prime $q$, with $q\ge5$ for the potentially good exchanges) with the
predicted code and conductor exponent at $q$, no mismatch; no change of code at any odd $p\ne q$; and at $q=3$ the
exchanges $\mathrm{II}\leftrightarrow\mathrm{IV}^*$, $\mathrm{III}\leftrightarrow\mathrm{III}^*$, $\mathrm{IV}\leftrightarrow\mathrm{II}^*$ hold in all $5{,}122$ pairs (important_notes.md point 51).
This is the book's version of the paper's `twist_lemma_check.gp`, which the paper ran on $4{,}577$ random pairs. Paper:
Lemma lem:twist, the appendix (last paragraph).

**3.8 `rem:computation:ellmoddegree`** (remark; C for the facts about the function, S for the method). (i) `ellmoddegree(E)`
returns the degree of the modular parametrisation of the given curve divided by the square of its Manin constant (PARI
manual; verify the exact wording in 2.15): on 11a1, 11a2, 11a3 it returns $1$, $5$, $1/5$ (C). So it is $\degphi$ only on the
optimal curve. (ii) `ellweilcurve(E)` returns the curves of the isogeny class with lattice data; the optimal curve is the
one whose entry is `[1, 1]` (C: for class 11a the entries are `[1, 1/5]`, `[1, 1]`, `[5, 1]`, marking 11a1; for class 990h they
are `[3, 1]`, `[1, 1]`, `[6, 1]`, `[2, 1]`, marking $[1,-1,1,-1568,-4669]$ $=$ 990h3; the writer checks the meaning of the entries in
the manual before printing more than "the entry `[1, 1]` marks the optimal curve"). (iii) The method: Watkins's, through
$L(\Sym f,2)$ and the Petersson norm (Chapter 14, 7.3 and 12.5; Chapter 19, 8.4); the `lfun` machinery prints
`_lfuninit_worker` warnings when it grows the stack (C). (iv) Cost and memory (C, 2.17.2): about $0.065$ seconds per curve on
a random sample below $10{,}000$; the default 8 MB stack suffices for most curves (e.g. 9999m1, degree $5632$) but not for
the largest degrees (9510e1, degree $100{,}254{,}000$; 9690m1, $68{,}217{,}600$; 7910b1, $31{,}272{,}384$), which need $16$ to $32$ MB.
(v) Full check: `ellmoddegree` against `ecdata`'s `degphi` on all $38{,}042$ optimal curves below $10{,}000$ (Part 7, R8;
result recorded there). Paper: Section 1 ("The modular degree is computable"), Section sec:data ("fifteen modular degrees
spanning the configurations were recomputed with `ellmoddegree`"), Section sec:oot, the appendix.

### Section 4. Cremona's tables and the `ecdata` files

**4.1 `def:computation:ecdata-files`** (definition by description; C for the formats as found). Cremona's tables
(Cremona97 for $N\le1000$ in print; the `ecdata` repository, refs.bib key `ecdata`, for everything since) are plain text
files, one per range of $10{,}000$ conductors, one line per curve or per isogeny class, fields separated by single spaces,
$a$-invariants written `[a1,a2,a3,a4,a6]` without spaces. The six files used in this book, for conductor $0$ to $9{,}999$,
with their formats (C, read off the files):

| file | lines | one line per | fields |
|-|-|-|-|
| `allcurves.00000-09999` | 64,687 | curve | $N$, class, number, $[a_1,\dots,a_6]$, rank $r$, $\#E(\Q)_{\mathrm{tors}}$ |
| `allbsd.00000-09999` | 64,687 | curve | as `allcurves`, then $\prod_pc_p$, real period $\Omega$, $L^{(r)}(E,1)/r!$, regulator, analytic order of Sha |
| `allisog.00000-09999` | 38,042 | class | $N$, class, $1$, $[a_i]$ of curve 1, the list of $[a_i]$ of the class, the isogeny-degree matrix |
| `alllabels.00000-09999` | 64,687 | curve | Cremona's $N$, class, number, then the LMFDB's $N$, class, number |
| `degphi.00000-09999` | 38,042 | class | $N$, class, number of the optimal curve, $\degphi$, the set of primes dividing $\degphi$, $[a_i]$ of the optimal curve |
| `galrep.00000-09999` | 64,687 | curve | label, then the Sutherland labels of the non-surjective mod $\ell$ images (nothing if all are surjective) |

Sample lines (C): `11 a 1 [0,-1,1,-10,-20] 0 5` (allcurves); `11 a 1 [0,-1,1,-10,-20] 0 5 5 1.26920930427955
0.253841860855911 1.00000000000000 1` (allbsd: $\prod c_p=5$, $L(E,1)/\Omega=1/5$); `11 a 1 1 {} [0,-1,1,-10,-20]` (degphi: degree
$1$, no prime divisors); `726 a 1 144 {2,3} [1,1,0,-35,-51]`; `11a1 5Cs.1.1` and `726a1 2B 3Ns` (galrep); `11 a 2 11 a 1` (alllabels:
11a2 is 11.a1). Facts the reader needs: the Kodaira symbols and the local Tamagawa numbers are **not** in these six files
(only $\prod_pc_p$ is, in `allbsd`), so they are recomputed with PARI (3.1), as the paper did; `degphi` has one line per class
and gives the optimal curve's equation; `galrep` gives images only for $\ell$ where the image is not $\GL_2(\F_\ell)$. The
repository has further directories (generators, $a_p$ lists, integral points, optimality and Manin constant data, and
others); the writer names only those checked in the repository at the pinned commit (Part 6.5), and must not write
"`alldegphi`" (PLAN.md's name; the file is `degphi`, Part 8). Paper: Section sec:data ("Cremona's tables in the form of the
`ecdata` repository at commit `25cec5e`, which contain every elliptic curve over $\Q$ of conductor below $500000$ with ...").

**4.2 `ex:computation:reading-ecdata`** (worked example; C). Reading the files in GP: `readstr(file)` gives the vector of
lines, `strsplit(s, " ")` the fields, `eval` turns `"[0,-1,1,-10,-20]"` into a vector (C, 2.17.2). In Python: `line.split()`
and `ast.literal_eval` (or `eval` on trusted data). The GP functions `readgal` (a `Map` from labels to image labels) and the
loop of S3 are printed in full. One caution: the label of the optimal curve is assembled from the `degphi` line, whose
"number" field is $1$ even for 990h, whose equation is that of 990h3 (4.3); the scripts look the equation up in
`allcurves` instead of trusting the number. Paper: background (the appendix's scripts are not in the repository of the
book).

**4.3 `rem:computation:optimality-data`** (remark; R, with C checks). (i) In Cremona's labelling, curve number $1$ of each
class is the optimal curve, with exactly one exception below $10{,}000$: class 990h, whose optimal curve is 990h3
$=[1,-1,1,-1568,-4669]$, the equation listed in `degphi` (C: of the $38{,}042$ `degphi` equations, exactly one is not curve number
$1$ in `allcurves`). Chapter 9, 12.1 states this; here it is checked and its computational consequence shown: `ellmoddegree`
gives $1728$ on 990h3 and $5184$ on 990h1, and `rule` gives `[3, 3]` and `[4, 3]` at $\ell=3$ (C). (ii) Optimality is proved for all
classes with $N\le400000$ and for $359{,}009$ classes above (the paper, Section sec:data; Chapter 14, its 6.5 for what "proved"
means); the paper's extension range uses only those classes (point 25). (iii) `ellweilcurve` (3.8(ii)) identifies the optimal
curve inside PARI for moderate conductors. (iv) Point 27 / Chapter 21's N13: when $E[\ell]$ is irreducible, $v_\ell$ of the
degree does not depend on which curve of the class is optimal; when it is reducible, it does (11a1, 11a2, 11a3 at $\ell=5$:
`rule` gives `[0, 1]`, `[1, 0]`, `[-1, 0]`, C). Paper: Section 1 ("Among the curves in the isogeny class of $E$ there is a
distinguished one"), Section sec:data ("Optimality is determined in the tables for every class of conductor at most $400000$
and for $359{,}009$ further classes up to $500000$"), the appendix.

**4.4 `conv:computation:labels`** (convention; R). (i) Cremona labels $N$ class number, class codes a, b, ..., z, ba, ...;
the capitalised form 99A1 of Cremona97 and ARS12 is 99a1. (ii) LMFDB labels $N$.class number, ordered differently; the
correspondence is the `alllabels` file (examples only: 11a1 $=$ 11.a2, 726a1 $=$ 726.b2; the full list of the running
examples is Chapter 9's 12.1, cited). (iii) Sutherland's labels of mod $\ell$ images as they occur in `galrep` (the general
scheme and the $\ell=3$ table are Chapter 11's 7.3, 7.4, cited, not reprinted); what the chapter needs: an image is reducible
iff its label starts with "$\ell$B" or "$\ell$Cs" (Borel or split Cartan subgroups and their subgroups), so `galrep` decides
membership in the base population of K5; 3Ns (image $N_s(\F_3)$), 3Cs.1.1 ($E[3]\simeq\Z/3\oplus\mu_3$, the order-$2$ subgroup of
the split Cartan, point 44) and 3B.1.1 (a rational point of order $3$, $E[3]$ non-split) are the three labels the paper uses.
Counts among the $37{,}853$ non-CM optimal curves below $10{,}000$ (C): 3B.1.1 $1{,}858$, 3B $1{,}567$, 3B.1.2 $503$, 3Nn $170$, 3Ns $90$,
3Cs.1.1 $49$, 3Cs $25$. CM caveat: `galrep` omits the labels forced by CM (Chapter 11, 7.3), so CM curves are excluded by $j$, not by
labels. (iv) Point 3 (labels to be checked against Sutherland16): the intrinsic descriptions of Chapter 11 are used in
every statement; the data checks of 3.6 and of Chapter 11 confirm the `ecdata` usage. Paper: Section 1.3 (3Ns), Section
sec:anomaly, Section sec:eis (3Cs.1.1, 3B.1.1), Section sec:data.

### Section 5. The paper's function `rule(E, l, iii)`, line by line

**5.1 `ex:computation:rule-listing`** (construction; C). The appendix code, verbatim (it is the paper's
`scripts/euler_rule.gp`), in an `lstlisting` with line numbers: the $14$ lines of `rule` and the one line of `ns3`, exactly as in the
paper (they contain no double hyphen; K9). Loaded with `read("euler_rule.gp")` in GP or `pari('read("euler_rule.gp")')` in
Python (the code cannot be pasted into `pari(...)` as one string, because a GP file joins the lines of a braced block,
while a single string does not: C, the first attempt failed with a syntax error). Paper: the appendix.

**5.2 `rem:computation:rule-reading`** (remark; P, a reading of code). One paragraph per line, saying what the line
computes as a program (types, indices, branches) and which term of (eq:rule) it is; the mathematics of each term is cited
(Chapter 19, 11.2; Chapter 21, A9.1) and not re-proved. The points that are specific to the code: (a) `P = R[4][,1]` is a
column vector of the bad primes in increasing order, and `K[i]` refers to the same order; (b) `F = 1/lfuneuler(S, q)` is a
polynomial in `x`, and `subst(F, x, 1/q^2)` an exact rational; (c) the test `k >= 5` is "multiplicative", and dividing by
`1 - 1/q^2` makes `r` equal to $1$ there (the naive factor is the true one, $e_\ell=0$); (d) at an additive prime no division is
made, because the naive factor is $1$ ($a_q=0$); (e) `abs(k) != 3 || iii` skips the types $\mathrm{III}$, $\mathrm{III}^*$ at $q\ne\ell$
unless `iii` is set; (f) the `else` branch of `if(q != l, ...)` handles $q=\ell$: no Euler term, and for $\ell=3$ the weight
$w_3$ by code ($1$ for $\mathrm{IV}$, $\mathrm{II}$, $\mathrm{III}^*$; $2$ for $\mathrm{IV}^*$, $\mathrm{II}^*$; $0$ otherwise), so `rule(E, 3)` counts the
$\mathrm{III}^*$ weight at $q=3$ even with `iii = 0` (Chapter 21, A9.1(c)); (g) `t` is computed at every bad prime, including
$q=\ell$ (point 53), and `valuation(j, q)` of $j=0$ is `+oo`, so `t = 0` there; (h) the correction `ns3(E)` is subtracted only
when `iii` is set and $\ell=3$ (for $\ell\ge5$, $h_\ell=0$ always: Lemma lem:h0 with point 5); (i) the returned pair is
$[v_\ell(\text{ellmoddegree}(E)),\ b]$, and `ellmoddegree` is by far the slowest step (3.8). Paper: the appendix.

**5.3 `prop:computation:rule-correct`** (proposition; P). Let $E$ be an optimal curve given by any model, $\ell$ an odd
prime. (i) For every bad prime $q\ne\ell$ the number `e` computed by `rule(E, l, 1)` is $e_\ell(E,q)$ of Definition def:terms,
and `t` is $t_\ell(E,q)$. (ii) If $E$ has no CM and $E[3]$ is irreducible, `ns3(E)` $=h_3(E)$. (iii) Hence, under these conditions,
`rule(E, l, 1)` returns $[v_\ell(\degphi),B^{\mathrm{rule}}_\ell(E)]$ and `rule(E, l)` returns $[v_\ell(\degphi),B^{\mathrm{III}}_\ell(E)]$; and
$B^{\mathrm{nc}}_\ell=B^{\mathrm{rule}}_\ell+$ `ns3`. Proof: (i) the code is $1$ exactly at $\mathrm I_0$ (never a bad prime), $\ge5$ exactly at
multiplicative primes, where $a_q^2=1$ and the naive factor at $s=1$ is $1-q^{-2}$; at every other bad prime $a_q=0$ and the
naive factor is $1$ (Chapter 19, 8.1); so `r` is the ratio of Definition def:terms; `t` is the definition of $t_\ell$ verbatim. (ii)
`ns3` is $1$ iff $\psi_3$ factors as $2+2$ over $\Q$ (item 3.6, `factor` ignores content and lists factors by increasing degree,
so patterns $4$, $1+3$, $1+1+2$, $1+1+1+1$ give $0$); for $E[3]$ irreducible and no CM this is image $N_s(\F_3)$ (Proposition
prop:ns, Chapter 11, 7.3), and then $h_3(E)=1$, otherwise $0$ (Lemma lem:h0 corrected by point 5: $h_3\le1$, with equality iff
$\bar\rho\simeq\bar\rho\otimes\chi_{-3}$). (iii) follows, $\degphi$ being `ellmoddegree(E)` for the optimal curve (3.8; Manin constant $1$ on
the tables, Chapter 14). Check (C): the book's independent Python implementation of the five bounds (S5) agrees with
`rule` on the running examples and with the GP loop S3 on every optimal curve below conductor $2{,}000$ at $\ell=3,5,7$. Paper:
the appendix ("`rule(E,l)` leaves the type $\mathrm{III}$ terms out and `rule(E,l,1)` is (eq:rule)").

**5.4 `warn:computation:rule-pitfalls`** (warning; C for each example). Where `rule` gives an answer that is not the paper's
quantity: (a) a non-optimal model: `ellmoddegree` returns $\deg/c^2$ of that model, so `rule` on 11a3 at $\ell=5$ returns `[-1, 0]`
(a negative "valuation of a degree") and on 990h1 at $\ell=3$ returns `[4, 3]` instead of 990h3's `[3, 3]`; (b) CM curves: `ns3`
is $1$ on $13$ CM optimal curves below $10{,}000$, where $h_3$ has no meaning in Conjecture conj:euler (which excludes CM); (c)
Eisenstein curves: 11a1 at $\ell=5$ returns `[0, 1]`, an apparent violation, but $E[5]$ is reducible (5Cs.1.1) and the curve is
outside every statement of the paper; the population filter K5 is part of the statement, not an afterthought; (d) $\ell\mid N$:
`rule` runs and the data satisfy (eq:rule) there, but no theorem applies (Theorem thm:main needs $\ell\nmid N$); (e) the
codes $n+4$, $-(n+4)$ are for $n\ge1$ (point 52); (f) versions: in 2.17.2 `ellmoddegree` returns an integer (or a rational on a
non-optimal model); the writer checks the return type in 2.15 before saying the code runs unchanged there; (g) speed: for a
table, take $\degphi$ from `degphi` and compute only the bound (the function `rulebound` of S3). Paper: the appendix ("A single
curve can be checked against (eq:rule) in PARI/GP"; important_notes.md points 27, 52, 53; Part 8, N3).

### Section 6. Worked sessions

Each item: the input, the exact output (2.17.2), the per-prime breakdown printed by `rule_terms(E, l)` of S2 (rows
$[q,k,P_q(x),P_q(q^{-2}),e,w,t]$), and the reading. Mathematics of each term: Chapters 19 and 21 (cited).

**6.1 `ex:computation:121a1`** (worked example; C). `rule(ellinit([1,1,1,-30,-76]), 3)` $=$ `[1, 1]` (with or without `iii`).
Breakdown: `[[11, 2, 11*x + 1, 12/11, 1, 0, 0]]`: type $\mathrm{II}$ at $11$, $P_{11}=1+11X$, $e_3=v_3(12/11)=1$, $t_3=0$; $\degphi=6$
(`ellmoddegree` and `degphi`). Also $B^{\mathrm{main}}_3=0$ (type $\mathrm{II}$ has $\#\Phig=1$) and $B^{\mathrm{tw}}_3=1$: the curve on which
(eq:twist) is strictly stronger than (eq:main). Paper: the appendix ("returns `[1, 1]`"), the Example of Section 3 (b).

**6.2 `ex:computation:726a1`** (worked example; C). `rule(E, 3)` and `rule(E, 3, 1)` both return `[2, 2]` for 726a1
$=[1,1,0,-35,-51]$. Breakdown with `iii = 1`: `[[2, 10, -x + 1, 3/4, 0, 0, 1], [3, 7, -x + 1, 8/9, 0, 0, 1], [11, 3, 11*x + 1,
12/11, 1, 0, 0]]`; with `iii = 0` the last row has `e = 0`. So $B^{\mathrm{III}}_3=1+1=2$ ($t_3$ at $2$ from $\mathrm I_6$, at $3=\ell$
from $\mathrm I_3$), $B^{\mathrm{nc}}_3=3$, `ns3` $=1$ ($\psi_3=(x^2-x-74)(3x^2+8x+20)$), $B^{\mathrm{rule}}_3=2$; $\degphi=144=2^43^2$. Reading: without the
correction the bound fails by exactly one, the violation involves the prime $2\equiv-1\pmod3$ with $t_3(E,2)=1$ (as Section
sec:anomaly says of every violation), and $3\mid N$ puts the curve outside Theorem thm:main anyway. The congruence number
$r_E=1584=11\cdot144$ (Chapter 14; point 58) is not computable by `rule`. Paper: the appendix ("for 726a1 ... both return
`[2, 2]`, the type $\mathrm{III}$ term and the correction cancelling"), Section sec:anomaly.

**6.3 `ex:computation:539c1`** (worked example; C). `rule(ellinit([1,0,1,170,-3237]), 3)` $=$ `[2, 2]`: $q=7$, code $-7$
($\mathrm I_3^*$), $P_7=1-X$, $P_7(7^{-2})=48/49$, $e_3=v_3(48/49)=1$ (no division: additive), $t_3=v_3(3)=1$; $q=11$, code $6$ ($\mathrm I_2$),
$e_3=0$, $t_3=0$; $\degphi=288$. At $\ell=5$: `[0, 0]`. `tatedata(E, 7, 3)` $=[3,q_E,5,0]$: the Tate parameter of the twist 77c1, and
$5$ is not a cube mod $7$, so the Tamagawa factor adds nothing beyond $t_3$ (Lemma lem:tamfactor). Paper: the Example of
Section 3, (c) at $\ell=3$ ("the two terms $e_3(E,7)=v_3(48)=1$ and $t_3(E,7)=v_3(3)=1$ are both attained").

**6.4 `ex:computation:980i1`** (worked example; C). 980i1 $=[0,0,0,1568,-72716]$: `rule(E, 3)` $=$ `[2, 2]` ($q=2$, code $-4$,
$\mathrm{IV}^*$, $P_2=1+2X$, $e_3=v_3(3/2)=1$; $q=7$, $\mathrm I_5^*$, $e_3=v_3(48/49)=1$); `rule(E, 5)` $=$ `[1, 1]` ($t_5(E,7)=v_5(5)=1$; $e_5=0$
everywhere). $\degphi=2880=2^63^25$. Reading: at $\ell=3$ the prime $2$ contributes through PARI's factor (point 43: a theorem); at
$\ell=5$, $5\mid N$, so the example illustrates the congruence, not Theorem thm:qual (point 21). Paper: the Example of Section 3,
(c) at $\ell=5$.

**6.5 `ex:computation:99a1`** (worked example; C). 99a1 $=[1,-1,1,-2,0]$, $N=3^2\cdot11$: `rule(E, 3)` $=$ `[0, 0]`: $q=3=\ell$, code $3$
($\mathrm{III}$), $w_3=0$, $t_3=0$ ($v_3(j)=9$); $q=11$, $\mathrm I_1$. $\degphi=4$; the congruence number $r_E=12$ (ARS12, Table 1; recomputed in
Chapter 14) is outside PARI's built-in functions. PARI's $P_3=1+3X$ is not used by `rule` at $q=\ell$. Reading: the bound is $0$
and there is no violation; the gap between $r_E$ and $\degphi$ at $3$ is allowed because $9\mid N$. Paper: the Remark after the
Example of Section 3 (99A1).

**6.6 `ex:computation:wild-two`** (worked example; C). Three curves where the prime $2$ contributes through PARI's factor
alone: 336f1 $=[0,1,0,-1,2]$ (type $\mathrm{II}$ at $2$, $P_2=1+2X$, $e_3=1$; `rule(E, 3)` $=$ `[1, 1]`, $\degphi=24$); 1232l1
$=[0,0,0,32,-16]$ (type $\mathrm{II}^*$ at $2$, `lfuneuler` gives $P_2=-8x^3-4x^2+2x+1=(1-2x)(1+2x)^2$, $e_3=v_3(9/8)=2$; `rule(E, 3)` $=$
`[2, 2]`, $\degphi=288$); 592c1 $=[0,0,0,-16,-16]$ (type $\mathrm{II}^*$ at $2$, $P_2=-8x^3+4x^2-2x+1=(1-2x)(1+4x^2)$, $e_5=v_5(5/8)=1$;
`rule(E, 5)` $=$ `[1, 1]`, $\degphi=80$). Reading: the type at $2$ does not determine $P_2$ (point 50; the classification of
Chapter 19, 10.1, cited), and the prime $2$ can contribute at $\ell=5$ (point 69). Paper: Remark rem:wild, Section sec:wild.

**6.7 `ex:computation:11a1-eisenstein`** (worked example; C). 11a1 at $\ell=5$: `rule(E, 5)` $=$ `[0, 1]`; `galrep` gives 5Cs.1.1
($E[5]\simeq\Z/5\oplus\mu_5$), `tatedata(E, 11, 5)` $=[5,q_E,10,1]$: $\bar u=10\equiv-1$ is a fifth power in $\F_{11}^\times$, so the Tamagawa factor
of $\ad T$ at $11$ has valuation $2$ (Lemma lem:tamfactor), while $\degphi=1$. Reading: an Eisenstein curve, outside every
statement of the paper; the example shows why the population filter (K5) is part of each statement (Chapter 16's
Exercise 10, Chapter 18's 8.5 make the same point in cohomology). Paper: Section sec:eis, Conjecture conj:eis (for 11a1 at
$\ell=5$: $D=1=v_5(\#E(\Q)_{\mathrm{tors}})$).

**6.8 `ex:computation:tamagawa-session`** (worked example; C). At $\ell=3$, multiplicative primes $q\equiv1\pmod3$ with $3\mid n$:
791a1 at $7$ ($\bar u=6$, a cube: extra term $1$; $B^{\mathrm{rule}}_3=1$, refined bound $2$, $\degphi=144$, $v_3=2$: the refined bound is
attained); 77c1 at $7$ ($\bar u=5$, not a cube: extra $0$; bound $1$, $\degphi=6$); 1577a1 at $19$ ($\bar u=8=2^3$, a cube and not a ninth power:
extra $1$; bound $2$, $\degphi=720$). Agrees with Chapter 17, 5.5 (cited for the cohomology). Paper: Section sec:tam, Remark rem:ko(1).

### Section 7. Computing modular degrees and congruence numbers

**7.1 `rem:computation:moddeg-methods`** (remark; S). Three methods, each in one paragraph, with pointers: Zagier's and
Cremona's through modular symbols and the period lattice (Zagier85; Cremona97, Chapter II), and Watkins's through the
symmetric square $L$-value and the Petersson norm (Watkins02), which is what `ellmoddegree` implements (3.8). Why it is
expensive (S, heuristic; the writer cites PARI's documentation of `lfun` or Dokchitser's method, verify): the number of
coefficients needed to evaluate $L(\Sym f,2)$ grows roughly like the square root of the conductor of $L(\Sym f,s)$, which is at
most $N^2$ (Chapter 19, 7.2), so roughly like $N$; Cremona's tables computed degrees up to
$500000$, the paper only fifteen with `ellmoddegree` inside the tables and $893$ outside. The mathematics is Chapter 14's 7.3,
12.5 and Chapter 19's 8.3, 8.4 (cited). Paper: Section 1 ("The modular degree is computable \cite{Cremona97,Watkins02}"),
Section sec:data, Section sec:oot.

**7.2 `ex:computation:moddeg-check`** (worked example; C). `ellmoddegree` against `degphi` on all $38{,}042$ optimal curves of
conductor below $10{,}000$ (script S8, four processes, Part 7, R8): result as recorded in Part 7. The paper's sentence "fifteen
modular degrees spanning the configurations were recomputed with `ellmoddegree`, all agreeing with the tables" is thereby
extended, in the book's range, to every curve. Paper: Section sec:data.

**7.3 `rem:computation:congruence-number`** (remark; R, values C in Chapter 14). PARI has no function for the congruence
number $r_E$. Chapter 14 (its 8.5 and verification log) computes it from `mfinit`, `mfbasis` and the Hecke action on the
integral lattice; quote its values $r(\text{99a1})=12$ against $\degphi=4$, $r(\text{726a1})=1584$ against $144$ (point 58), $r(\text{539d1})=504$
against $72$ (point 62), and say only where the algorithm lives. Paper: the Remark after the Example of Section 3 (99A1), Lemma
lem:crit; PLAN.md's scope item "99A1 (where `ellmoddegree` gives 4 and the congruence number 12 is not given by PARI directly)".

### Section 8. Populations, violations and descriptive statistics

**8.1 `def:computation:units`** (definition; P). What is counted. (i) The unit is a curve, one per isogeny class (the optimal
one), at a fixed $\ell$; "pairs $(E,\ell)$" (Section sec:forms) and "pairs (curve, prime $q$)" (after Theorem thm:twist; Lemma
lem:twist checks) are different units and their counts are not comparable with curve counts. (ii) The populations of K5,
with the reason for each filter: CM curves are excluded by the statements (Conjecture conj:euler, Conjecture conj:eis);
reducible $E[\ell]$ moves a curve to the Eisenstein population, where a different statement is made (Conjecture conj:eis);
the hypothesis population is where Theorem thm:main applies, so that data there are checks of a theorem, not tests. (iii)
Why only one curve per class: $v_\ell(\degphi)$ is attached to the optimal curve, and counting all curves of a class would
count the same newform several times (point 27: for $E[\ell]$ irreducible the local terms and $v_\ell$ are class invariants).
Paper: Section sec:data, Tables tab:uniform, tab:counts, tab:ns, Section sec:forms ("pairs $(E,\ell)$").

**8.2 `def:computation:rates`** (definition and remark; P). For a population and a bound $B$: the number with $B>0$; the
number of violations; the *equality rate* (equalities over positive bounds); the *mean excess* (average of $v-B$ over positive
bounds); the *base rate* of an attribute (Appendix A, def:prereq:prob). Remarks: (a) curves with $B=0$ cannot violate, so
including them would inflate every rate; (b) an equality rate is a property of the population and the range, not of "elliptic
curves": in the book's data at $\ell=3$ it is $75.1\%$ for $N<5000$ and $68.0\%$ for $5000\le N<10000$, against the paper's $57.5\%$ for
$N\le300000$ (C, D); degrees grow with $N$, and with them the room for extra divisibility; (c) the mean excess is $0.31$ and
$0.42$ on the two small ranges, $0.37$ on their union (C), against the paper's $0.63$ (D); under the hypothesis of Theorem
thm:main the excess is the Selmer length plus the Tamagawa excess (eq:identity, with equality by points 39 and 56; at additive
primes the Tamagawa factor is trivial by point 64, so the excess is the Selmer length plus the excess at multiplicative
primes); the data measure it but do not explain it (Open question 3). Paper: Section sec:sharp ("the mean excess at
$\ell=3$ is $0.63$"; "the identity says what the excess is"), Section sec:forms.

**8.3 `ex:computation:base-rates`** (worked example; C). Base rates at $\ell=3$ in the base population below $10{,}000$ ($33{,}851$
curves): $3\mid\degphi$ for $76.1\%$. Conditional on having at least one prime $q\ge5$ of a given type (a curve with several types is
counted in several rows):

| type at some $q\ge5$ | curves | share with $3\mid\degphi$ |
|-|-|-|
| $\mathrm{II}$ / $\mathrm{II}^*$ | 946 / 418 | 100% / 100% |
| $\mathrm{IV}$ / $\mathrm{IV}^*$ | 468 / 896 | 100% / 100% |
| $\mathrm I_n^*$ | 2,233 | 100% |
| $\mathrm I_n$ with $3\mid n$ | 5,134 | 100% |
| $\mathrm{III}$ / $\mathrm{III}^*$ | 813 / 807 | 75.4% / 75.5% |
| $\mathrm I_0^*$ | 692 | 73.1% |
| $\mathrm I_n$ with $3\nmid n$ | 31,185 | 74.6% |

Reading: the rows at $100\%$ are exactly the types with a term that is always positive at $\ell=3$ ($e_3\ge1$ for $\mathrm{II}$ to $\mathrm{IV}^*$ and
$\mathrm I_n^*$ at $q\ge5$; $t_3\ge1$ for $3\mid n$); the rows near the base rate are the types whose term is positive only for some $q$
($\mathrm{III}$: $q\equiv\pm1\pmod{12}$; $\mathrm I_0^*$: $q\equiv1\pmod3$ or $3\mid a'$). A base-rate table is the first thing to compute and the
weakest evidence: it is the shadow of the inequality on a coarse partition. Paper: Section sec:iso (the same idea, cell by
cell), PLAN.md ("the base rates by Kodaira type").

**8.4 `rem:computation:simpson`** (remark; P, with a C illustration). Rates pooled over ranges or over types can mislead
(aggregation, Simpson's paradox in its mildest form): the pooled equality rate on $N<10000$ ($71.0\%$) is a weighted average of
the two ranges' rates, with weights the numbers of positive bounds ($8{,}510$ and $11{,}807$), and a comparison of the paper's
$57.5\%$ with the book's $71.0\%$ says nothing about a difference in the curves' arithmetic; it says the ranges differ. The fair
comparison is like with like: the same statement, the same population definition, the same range. Paper: Section sec:sharp,
Section sec:oot ("equality in (eq:rule) for $52.5\%$").

### Section 9. The protocol

**9.1 `rem:computation:protocol`** (remark; R for the definitions, which are Appendix A's; D for the paper's description). The
four ranges (K6) with what is known about each: the working set ($N\le300000$, every class optimal-determined), the hold-out
($300000<N\le400000$, the same), the extension ($400000<N\le500000$, only $359{,}009$ classes optimal-determined, so the extension
counts are over those classes: point 25), the out-of-table curves ($893$ curves with $500000<N\le4\cdot10^6$, generated in families
with prescribed local types and kept when the isogeny class is trivial, so that the curve is optimal and every $E[\ell]$ is
irreducible; their degrees by `ellmoddegree`). Appendix A's def:prereq:holdout and pl:prereq:protocol are cited for the vocabulary
(working set, hold-out, pre-registration, blind test, confirmation). Paper: Section sec:data, Section sec:oot.

**9.2 `prop:computation:test-status`** (proposition, read off the paper's text; P as a reading, D for the facts). The status of
each data claim, from the paper's own account (Section sec:data):

| statement | formulated on | blind test | confirmation only | remark |
|-|-|-|-|-|
| (eq:main) | working set | hold-out (once), then extension | out-of-table | nothing adjusted after the hold-out test |
| Conjecture conj:eis | working set | hold-out (once), then extension | | stated for (eq:main) only; $D\le2$ is a theorem (point 17) |
| (eq:twist) | working set (replacing a weaker form) | hold-out and extension, "tested once" | out-of-table | blind only if fixed before the hold-out was opened for (eq:main); the text does not say (Part 8, N2) |
| Conjecture conj:euler: the Euler terms | working set (minima by type, Section sec:iso) | out-of-table | hold-out, extension | the terms at $2$, $3$ "fixed afterwards by PARI's Euler factors" |
| the weights $w_3$ | working set (minima at $q=3$) | out-of-table, only on curves with $3\mid N$ and potentially good reduction at $3$, if any | hold-out, extension | empirical by construction (Section sec:wild) |
| the correction $h_\ell$ | from the exceptions | none: the out-of-table set has no 3Ns curve | all ranges | $h_3=1$ on 3Ns is a theorem (Lemma lem:h0, point 5); the inequality with it is not |
| the III-free form | after the 3Ns exceptions | none | all ranges | a reformulation chosen to have no exceptions |
| Lemmas lem:euler, lem:twist; Proposition prop:forms; $h_3=1$ | | | | theorems: the data are checks of computations, not tests |
| the Tamagawa refinement (sec:tam) | from Lemma lem:tamfactor and (eq:identity) | working set, as a prediction of a theorem | | a test of the identity's Tamagawa term (point 68 on its wording) |

The proposition is the table plus the sentence: a statement is blind-tested on a range only if it was written down before any
quantity of that range entering the statement was looked at; generating data before a statement is formulated is necessary
but not sufficient (it is sufficient if the data were not examined). Paper: Section sec:data ("Since the hold-out and the
extension had already been used for (eq:main) and (eq:twist), they are a confirmation and not a blind test for Conjecture
conj:euler; the out-of-table curves, generated before the rule was formulated, are").

**9.3 `rem:computation:what-is-tested`** (remark; P). What a blind test of a universal inequality establishes: a single
violation refutes; zero violations on $n$ fresh curves is evidence whose weight depends on how likely a violation would have
been if the statement were false (Section 10: calibration), and on whether the fresh curves exercise the statement (the
out-of-table families were built with types $\mathrm{IV}$, $\mathrm{IV}^*$, two or three $\mathrm{II}$, mixed and random; they cannot test the 3Ns
correction, which needs 3Ns curves, or the $\mathrm{III}$ terms unless such primes occur). "Nothing was adjusted after the hold-out
test" means: no term, weight or population filter of (eq:main) and Conjecture conj:eis was changed after their hold-out counts
were seen; it does not cover later statements. Paper: Section sec:data, Section sec:oot, the AI statement ("a list of tests
fixed before any was run").

**9.4 `rem:computation:multiple-comparisons`** (remark; P for the arithmetic, R for the general theory: Wasserman04, chapter on
multiple testing, cite by chapter). (i) The paper's statements came out of a search: "the pre-registered search, which produced
the candidate relation" (AI statement), then successive refinements (Tamagawa number to $\Phig$, then twist-symmetrised weights,
then Euler factors, then $w_3$, then $h_\ell$). (ii) If $m$ false candidate statements each survive a working-set check with
probability $\pi$, about $m\pi$ false statements survive; a hold-out check with survival probability $\pi'$ for false statements
leaves $m\pi\pi'$; this is the whole case for holding data back (exercise). (iii) For a universal inequality the relevant $\pi'$ is
tiny when the calibration of Section 10 says hundreds of thousands of violations were expected under independence: so the
multiple-comparisons risk sits mostly in the *choice of form* (which weights, which correction, which population filter),
where the working set was used repeatedly, not in the bare existence of a relation. (iv) Post-hoc features: the $w_3$ were
defined as observed minima, so the working set cannot violate them; the III-free form was chosen to have no exceptions;
such features are validated only by data not used to choose them. The book's toy version (9.5) shows the procedure. Physics
aside (one sentence): this is the look-elsewhere effect. Paper: Section sec:data, Section sec:wild ("the weights $w_3$ ... are
empirical"), Section sec:iso.

**9.5 `ex:computation:toy-protocol`** (worked example; C). On the book's data: freeze the small working set $N<5000$; read off
the minima of $v_3(\degphi)$ over curves whose only possible contribution at $3$ is a potentially good prime $q=3$ (the paper's
recipe for $w_3$): $\mathrm{II}$ $1$ ($239$ curves), $\mathrm{II}^*$ $2$ ($156$), $\mathrm{III}$ $0$ ($221$), $\mathrm{III}^*$ $1$ ($221$), $\mathrm{IV}$ $1$ ($156$), $\mathrm{IV}^*$ $2$
($239$), $\mathrm I_0^*$ $0$ ($299$): exactly the paper's $w_3$. Then test once on the small hold-out $5000\le N<10000$: the same minima
($255$, $186$, $251$, $251$, $186$, $255$, $347$ curves), and the full rule with these frozen weights has no violation among the $11{,}699$
base-population curves with $3\mid N$ there. Reading: a replication of the recipe, not a discovery; and a reminder that the
small working set was not blind to the paper (the weights were known in advance), so this is a demonstration of the
procedure only. Paper: Section sec:wild, Conjecture conj:euler.

### Section 10. The calibration argument of Section sec:sharp

**10.1 `prop:computation:null-model`** (proposition; P). Let a population be split by a bound $b(E)\in\{0,1,2,\dots\}$, with observed
valuations $v(E)$. Null hypothesis $H_0$: $v$ is independent of $b$, all curves having the same distribution $F$ of $v$. Let
$\hat F$ be the empirical distribution of $v$ on the curves with $b=0$, and $X$ the number of violations among the curves with
$b>0$. Then (i) under $H_0$, $E[X]=\sum_{b(E)>0}F(v<b(E))$ by linearity (Appendix A, thm:prereq:expectation(a)), with no independence
between curves needed, and $\hat E=\sum_{b(E)>0}\hat F(v<b(E))$ estimates it; (ii) if moreover the $v(E)$ are independent across
curves, $X$ is a sum of independent indicators, $\operatorname{Var}X=\sum p_E(1-p_E)\le E[X]$, $P(X=0)=\prod(1-p_E)\le e^{-E[X]}$, and by
Chebyshev $P(X=0)\le\operatorname{Var}X/E[X]^2\le1/E[X]$ (pairwise independence suffices for the last bound); (iii) under $H_0$ the
pooled distribution of $v$ over all curves (bound $0$ and positive) estimates the same $F$, so a large difference between the
pooled and the bound-$0$ distributions is itself evidence against $H_0$; a permutation test makes this exact: shuffle $v$ among
the curves (within strata of conductor and number of bad primes, to respect the dependence of $v$ on $N$) and recount. Proofs:
linearity; the product formula and $1-p\le e^{-p}$; Chebyshev. Reference: Appendix A; Feller68 (chapters on expectation and
on Chebyshev's inequality; cite chapters). Paper: Section sec:sharp ("If the valuation of the degree were independent of the
local data, the $867{,}578$ working-set curves with a positive bound at $\ell=3$ would produce roughly $605{,}000$ violations (summing
over them the proportion of bound-$0$ curves whose valuation is smaller than the bound); there are none").

**10.2 `ex:computation:calibration-paper`** (worked example; D, with arithmetic P). The paper's numbers: $366{,}151$ bound-$0$
curves, of which $53.2\%$ have $3\nmid\degphi$; $867{,}578$ curves with a positive bound; expected violations about $605{,}000$, that is
$69.7\%$ of them; observed $0$. Checks: the $v=0$ part alone gives at least $0.532\cdot867{,}578\approx461{,}551$ (Chapter 21, A6.3), and
$605{,}000$ requires an average $\hat F(v<b)$ of $0.697$, consistent with the book's own ratio $70.3\%$ (10.3); under independence the
standard deviation of $X$ is at most $\sqrt{605000}\approx778$, so $0$ is about $780$ standard deviations below the mean, and the
"$p$-value" is below $e^{-605000}$: meaningless as a number, which is why the paper (and Appendix A's ex:prereq:calibration) states
the comparison of $605{,}000$ with $0$ and no $p$-value. Paper: Section sec:sharp.

**10.3 `ex:computation:calibration-small`** (worked example; C). The same statistic on the base population at $\ell=3$ below
$10{,}000$: bound-$0$ curves $13{,}534$, with $\hat F$: $v=0$: $8{,}084$ ($59.7\%$), $1$: $4{,}079$, $2$: $1{,}081$, $3$: $251$, $4$: $33$, $5$: $5$, $6$: $1$; positive
bounds $20{,}317$ (bound $1$: $13{,}553$; $2$: $5{,}534$; $3$: $1{,}109$; $4$: $112$; $5$: $9$); expected violations $\hat E=14{,}275$ ($70.3\%$ of
the bounded curves), standard deviation under independence $61.5$; observed $0$. By range: $N<5000$: $\hat E=6{,}091$ ($\hat F(0)=0.630$); $5000\le
N<10000$: $8{,}119$ ($\hat F(0)=0.566$). At $\ell=5,7,11,13$ (union): $\hat E=5{,}901$, $3{,}476$, $1{,}187$, $698$; observed $0$ each. Robustness of
the reference population (C): stratified by conductor bins of width $2500$ and by $\omega(N)$ (capped at $4$), $\hat E=14{,}177$; a
permutation of $v$ within the same strata over all curves ($200$ shuffles, seed $0$) gives a mean of $7{,}638$ violations (standard
deviation $49$, minimum $7{,}517$): the reference population changes the expected count by a factor of two, and the conclusion not
at all. The pooled share of $v=0$ is $23.9\%$ against $59.7\%$ among bound-$0$ curves: under $H_0$ these would agree (10.1(iii)).
Paper: Section sec:sharp.

**10.4 `rem:computation:calibration-reading`** (remark; P). What the calibration shows: the zero count is not an artefact of
$3$ dividing most modular degrees (base rate $76\%$ below $10{,}000$): the bound picks out, among all curves, those whose degree is
divisible, and a bound unrelated to the degree would fail tens of thousands of times in the book's range and hundreds of
thousands in the paper's. What it does not show: (a) that the inequality is true beyond the data (that is the theorem's job
under its hypotheses, and the conjecture's outside them); (b) anything on the working set about validity, because the rule was
fitted there (weights read off minima, terms at $2$, $3$ chosen after seeing minima): on the working set the calibration measures
the *strength* of the statement; its *validity* is supported by the blind tests of Section 9; (c) independence across curves
is an idealisation (twists and congruent forms tie curves together), so the standard deviations are indicative only; (d) the
null "independent of the local data" is crude; a sharper null would condition on $N$ and on the number of bad primes, as the
stratified version does. The equality rates and the mean excess are descriptive (8.2). Paper: Section sec:sharp ("The zero
counts are not tautological"; "The bounds are attained").

**10.5 `ex:computation:sharpness`** (worked example; C). How sharp the bound is, against chance: under $H_0$ the expected number of
equalities among the $20{,}317$ bounded curves at $\ell=3$ is $\sum\hat F(v=b)\approx4{,}548$; observed $14{,}420$ ($71.0\%$). Equality rates by
$\ell$ (union of the small ranges): $71.0\%$, $84.5\%$, $90.7\%$, $96.5\%$, $96.0\%$ at $\ell=3,5,7,11,13$ (paper, working set: $57.5\%$, $75.6\%$,
$84.1\%$, $91.6\%$, $92.4\%$). Mean excess at $\ell=3,5,7,11,13$: $0.37$, $0.17$, $0.10$, $0.04$, $0.04$. Paper: Section sec:sharp.

**10.6 `ex:computation:odd-part`** (worked example; C and D). The paper's last statistic: among optimal non-CM curves with no
isogeny of odd degree (so $E[\ell]$ irreducible for every odd $\ell$; decided from the `allisog` matrix), the share whose odd part of
$\degphi$ equals $\prod_\ell\ell^{B^{\mathrm{tw}}_\ell}$. Book (C): $33{,}137$ curves; equality for $5{,}675$ ($17.13\%$); the quotient is always an
integer ((eq:twist) holds for every odd $\ell$); most common quotients $3$ ($5{,}926$), $1$, $5$ ($2{,}978$), $9$ ($2{,}532$), $15$, $7$, $21$, $11$;
the smallest prime factor of a nontrivial quotient is $3$ in $59\%$ of cases and divides $N$ in $48\%$. Paper (D, working set): $1{,}226{,}216$
curves, equality $1.85\%$, quotients most often $9$, $3$, $15$, $45$, $27$, $21$, smallest prime factor $3$ in $63\%$, dividing $N$ in $52\%$.
Reading: the local terms explain a sharp part of $\degphi$ and less and less of the rest as $N$ grows (the rest is the Selmer
group and the size of the Petersson norm, Chapter 19, 8.4, 8.5); the paper's phrase "its smallest prime factor is $3$ in $63\%$ of
the cases and divides $N$ in $52\%$" is read as "the smallest prime factor of the quotient divides $N$" (the writer says so). Paper:
Section sec:sharp ("The whole odd part of $\degphi$ is another matter").

### Section 11. Reproducing the paper's tables on conductor below $10{,}000$

Each item prints a table produced by the scripts S4, S5 (Part 7), with the paper's corresponding numbers (D) beside it where
the paper gives them in the text (the paper's table files `tables/*.tex` are not available; Chapter 21, A6: never invent their
entries). All counts are over the base population at $\ell$ (K5) unless stated.

**11.1 `ex:computation:repro-uniform`** (worked example; C). Table tab:uniform in small. Columns: range, $\ell$, base population,
$B^{\mathrm{rule}}>0$, violations, equality rate, violations of $B^{\mathrm{nc}}$, $B^{\mathrm{III}}>0$, violations, equality rate.

| range | $\ell$ | curves | rule $>0$ | viol. | eq. | viol. without $h$ | III-free $>0$ | viol. | eq. |
|-|-|-|-|-|-|-|-|-|-|
| $N<5000$ | 3 | 15,102 | 8,510 | 0 | 75.1% | 16 | 8,430 | 0 | 75.0% |
| | 5 | 16,863 | 3,078 | 0 | 88.4% | 0 | 3,068 | 0 | 88.3% |
| | 7 | 17,107 | 1,644 | 0 | 91.5% | 0 | 1,642 | 0 | 91.5% |
| | 11 | 17,190 | 515 | 0 | 97.5% | 0 | 515 | 0 | 97.5% |
| | 13 | 17,180 | 296 | 0 | 97.3% | 0 | 296 | 0 | 97.3% |
| $5000\le N<10000$ | 3 | 18,749 | 11,807 | 0 | 68.0% | 20 | 11,697 | 0 | 67.6% |
| | 5 | 20,456 | 4,398 | 0 | 81.7% | 0 | 4,368 | 0 | 81.7% |
| | 7 | 20,584 | 2,291 | 0 | 90.2% | 0 | 2,287 | 0 | 90.2% |
| | 11 | 20,649 | 741 | 0 | 95.8% | 0 | 741 | 0 | 95.8% |
| | 13 | 20,643 | 432 | 0 | 95.1% | 0 | 428 | 0 | 95.1% |
| $N<10000$ | 3 | 33,851 | 20,317 | 0 | 71.0% | 36 | 20,127 | 0 | 70.7% |
| | 5 | 37,319 | 7,476 | 0 | 84.5% | 0 | 7,436 | 0 | 84.5% |
| | 7 | 37,691 | 3,935 | 0 | 90.7% | 0 | 3,929 | 0 | 90.8% |
| | 11 | 37,839 | 1,256 | 0 | 96.5% | 0 | 1,256 | 0 | 96.5% |
| | 13 | 37,823 | 728 | 0 | 96.0% | 0 | 724 | 0 | 96.0% |

The paper (D): no violation of (eq:rule) at any $\ell$ on any range; the violations without $h$ are all 3Ns curves ($364$, $68$, $43$,
$0$ on the four ranges); equality $57.5\%$ at $\ell=3$ on the working set. Agreement in kind: no violation, the uncorrected failures
are exactly the 3Ns curves (11.3), and the III-free form never fails. Paper: Section 6.2, Table tab:uniform, Section sec:sharp.

**11.2 `ex:computation:repro-counts`** (worked example; C). Table tab:counts in small: for each range and $\ell$, $B^{\mathrm{main}}>0$, violations,
equality rate; $B^{\mathrm{tw}}>0$, violations, equality rate; Eisenstein population, positive $B^{\mathrm{main}}$, positive deficit $D$, violations
of the torsion bound, violations of the class bound, $D=2$.

| range | $\ell$ | main $>0$ | viol. | eq. | twist $>0$ | viol. | eq. | Eis. | main $>0$ | $D>0$ | viol. | viol. (class) | $D=2$ |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| $N<5000$ | 3 | 5,908 | 0 | 59.0% | 6,996 | 0 | 61.3% | 2,096 | 1,725 | 284 | 0 | 0 | 11 |
| | 5 | 2,478 | 0 | 86.5% | 2,681 | 0 | 87.2% | 335 | 199 | 45 | 0 | 0 | 0 |
| | 7 | 1,351 | 0 | 89.8% | 1,452 | 0 | 90.6% | 91 | 35 | 9 | 0 | 0 | 0 |
| | 11 | 450 | 0 | 96.4% | 472 | 0 | 97.2% | 8 | 0 | 0 | 0 | 0 | 0 |
| | 13 | 272 | 0 | 96.3% | 286 | 0 | 97.2% | 18 | 2 | 0 | 0 | 0 | 0 |
| $5000\le N<10000$ | 3 | 8,069 | 0 | 49.1% | 9,545 | 0 | 51.6% | 1,906 | 1,624 | 147 | 0 | 0 | 3 |
| | 5 | 3,307 | 0 | 76.6% | 3,636 | 0 | 78.6% | 199 | 139 | 8 | 0 | 0 | 0 |
| | 7 | 1,719 | 0 | 86.9% | 1,894 | 0 | 87.8% | 71 | 32 | 3 | 0 | 0 | 0 |
| | 11 | 579 | 0 | 94.3% | 631 | 0 | 94.9% | 6 | 0 | 0 | 0 | 0 | 0 |
| | 13 | 369 | 0 | 93.8% | 389 | 0 | 94.1% | 12 | 2 | 0 | 0 | 0 | 0 |
| $N<10000$ | 3 | 13,977 | 0 | 53.3% | 16,541 | 0 | 55.7% | 4,002 | 3,349 | 431 | 0 | 0 | 14 |
| | 5 | 5,785 | 0 | 80.8% | 6,317 | 0 | 82.2% | 534 | 338 | 53 | 0 | 0 | 0 |
| | 7 | 3,070 | 0 | 88.1% | 3,346 | 0 | 89.0% | 162 | 67 | 12 | 0 | 0 | 0 |
| | 11 | 1,029 | 0 | 95.2% | 1,103 | 0 | 95.9% | 14 | 0 | 0 | 0 | 0 | 0 |
| | 13 | 641 | 0 | 94.9% | 675 | 0 | 95.4% | 30 | 4 | 0 | 0 | 0 | 0 |

The paper (D, working set): equality in (eq:twist) $39.4\%$, $71.1\%$, $81.2\%$, $91.5\%$ at $\ell=3,5,7,13$, in (eq:main) $36.9\%$, $69.7\%$,
$80.4\%$, $91.2\%$; the rule bounds $867{,}578$ curves instead of $705{,}563$ at $\ell=3$ (book: $20{,}317$ instead of $16{,}541$). Same ordering
(main below twist below rule) in both. Paper: Section sec:forms, Table tab:counts, Conjecture conj:eis.

**11.3 `ex:computation:repro-ns`** (worked example; C). Table tab:ns in small (optimal non-CM curves with image 3Ns):

| range | 3Ns curves | positive $\mathrm{III}$ term | violate $B^{\mathrm{nc}}$ | other curves violating | `ns3` $=1$ | residues mod 12 of the $\mathrm{III}$ primes of violators | shortfall |
|-|-|-|-|-|-|-|-|
| $N<5000$ | 30 | 30 | 16 (53%) | 0 | 30 | $1$: 4, $11$: 8, $q=2$: 4 | always 1 |
| $5000\le N<10000$ | 60 | 60 | 20 (33%) | 0 | 60 | $1$: 8, $11$: 12 | always 1 |
| $N<10000$ | 90 | 90 | 36 (40%) | 0 | 90 | $1$: 12, $11$: 20, $q=2$: 4 | always 1 |

Every violator has a prime $p\equiv-1\pmod3$ with $t_3(E,p)\ge1$ ($36$ of $36$); $12$ of the $36$ have $3\mid N$. Of the $90$ curves, $74$ have a type
$\mathrm{III}$ or $\mathrm{III}^*$ prime $q\ge5$ with $e_3\ge1$ and the other $16$ (conductors $3840$, $4864$, $6912$) get their positive $\mathrm{III}$ term at
$q=2$ from PARI's factor (consistent with Chapter 21, A6.7 and with point 48). The paper (D): $364$, $68$, $43$, $0$ violations, $31\%$, $23\%$,
$18\%$ of the 3Ns curves. Reading: the same phenomenon at higher rates in the small range; the falling rate with $N$ is visible
already inside the book's range. Paper: Section sec:anomaly, Table tab:ns, Remark rem:ns.

**11.4 `ex:computation:repro-iso`** (worked example; C). Section sec:iso in small: curves of the base population with exactly one
additive prime, $q\ge5$, $q\ne\ell$, and no multiplicative prime with $\ell\mid n$; minimum of $v_\ell(\degphi)$ by type and $e_\ell(E,q)$. At
$\ell=3$: $\mathrm{II}$ $e=1$: min $1$ ($264$ curves), $e=2$: $2$ ($27$); $\mathrm{II}^*$ $1$: $1$ ($135$), $2$: $2$ ($11$); $\mathrm{III}$ $0$: $0$ ($193$), $1$: $1$ ($44$), $2$: $2$
($2$); $\mathrm{III}^*$ the same counts; $\mathrm{IV}$ $1$: $1$ ($150$), $2$: $2$ ($11$); $\mathrm{IV}^*$ $1$: $1$ ($249$), $2$: $2$ ($27$); $\mathrm I_0^*$ $0$: $0$ ($146$), $1$: $1$ ($42$), $2$: $2$
($88$), $3$: $3$ ($50$); $\mathrm I_n^*$ $1$: $1$ ($813$), $2$: $2$ ($57$), $3$: $3$ ($3$), with the minimum of $v_3(\degphi)-e_3-t_3$ equal to $0$ in each $\mathrm I_n^*$ cell.
At $\ell=5$ and $\ell=7$: every cell's minimum equals $e$ (cells listed in Part 7, R5). Multiplicative primes alone: for curves with a
single multiplicative prime $q$ with $\ell\mid n$ and no additive prime, $\min(v_\ell(\degphi)-v_\ell(n))=0$ for every value of $v_\ell(q^2-1)$ ($\ell=3$:
values $0$ to $4$, $4{,}367$ curves; $\ell=5$: $0$ to $2$, $2{,}588$ curves). Two odd primes of type $\mathrm{II}$/$\mathrm{II}^*$ and nothing else at $\ell=3$:
$8$ curves, $9\mid\degphi$ for all $8$. The paper (D): the same pattern in every cell; $\mathrm{III}$: $5{,}534$, $\mathrm I_0^*$: $5{,}394$ curves with $e=0$;
$\mathrm I_0^*$ up to $e=6$; $2{,}502$ curves with two $\mathrm{II}$-type primes. Paper: Section sec:iso, Table tab:iso.

**11.5 `ex:computation:repro-tam`** (worked example; C). Section sec:tam in small: hypothesis population ($\ell\nmid N$, $E[\ell]$
irreducible, not CM, at $\ell=3$ not 3Ns) with at least one prime of type $\mathrm I_n$, $\ell\mid n$, $q\equiv1\pmod\ell$; extra term
$\min(v_\ell(n),v_\ell(q-1),v_\ell(c(u)))$ summed over such primes, from `tatedata`. $\ell=3$: $989$ curves, $179$ with a positive extra term (total
$179$), no violation of the refined bound, equality from $550$ ($55.6\%$) to $662$ ($66.9\%$). $\ell=5$: $246$ curves, $24$ positive, no violation,
equality $197$ ($80.1\%$) to $214$ ($87.0\%$). $\ell=7$: $18$ curves, $1$ positive (4171a1 at $43$), equality $17$ to $18$. The paper (D, working set):
$\ell=3$: $46{,}222$, $12{,}095$, $45.0\%$ to $60.6\%$; $\ell=5$: $10{,}940$, $1{,}646$, $67.0\%$ to $78.7\%$. Note: following the paper, only type $\mathrm I_n$
primes are used; the refinement also applies at $\mathrm I_n^*$ primes (point 68; Chapter 18 reports $1{,}050$ curves at $\ell=3$ when
they are included). Paper: Section sec:tam, Remark rem:ko(1), Lemma lem:tamfactor.

**11.6 `ex:computation:repro-eis`** (worked example; C). Section sec:eis in small, $\ell=3$: $4{,}002$ Eisenstein curves, $3{,}349$ with $B^{\mathrm{main}}>0$,
$431$ with $D>0$, $D=2$ for $14$; no curve without a rational $3$-torsion point has $D>0$; the torsion bound is attained with $D>0$ in
$427$ cases; $D=2$ occurs for twelve curves with image 3Cs.1.1 (14a1, 26a1, 35a1, 38a1, 77b1, 158d1, 278b1, 326c1, 485a1, 4385b1, 7094c1,
8027a1), all of rank $0$, with torsion $\Z/3$ except 14a1 (torsion $\Z/6$), and for two curves with a point of order $9$ (714i1, 6942n1,
image 3B.1.1). Of the $49$ optimal non-CM curves with image 3Cs.1.1, none has a point of order $9$ (torsion $\Z/3$ for $48$, $\Z/6$ for 14a1); the
four optimal curves with a point of order $9$ (714i1, 1482l1, 1554n1, 6942n1) have image 3B.1.1. At $\ell=5$, $7$: $D\le1$, and $D>0$ only with
a rational $\ell$-torsion point ($53$ and $12$ curves). Against (eq:twist) the deficit exceeds the conjectured bound for $180$ curves at $\ell=3$
and $35$ at $\ell=5$. The paper (D): $75{,}430$, $67{,}845$, $2{,}777$, $D=2$ for $22$ ($17$ with 3Cs.1.1 "all of rank 0 and torsion $\Z/3$", $5$ with
a point of order $9$); for the 14a1 discrepancy see Part 8, N1. Paper: Section sec:eis, Conjecture conj:eis (with point 17: $D\le2$ is
provable).

**11.7 `ex:computation:repro-twist`** (worked example; C). The data paragraph after Theorem thm:twist in small: for each optimal
non-CM curve, each odd $q$ with $q^2\| N$ in case (a) ($\mathrm I_n^*$), (b) ($\mathrm I_0^*$) or (c) (potentially good, $q\ge5$), the twist $E_q$ by $q^*$
(found in `allcurves` through `ellminimalmodel`), and each $\ell\in\{3,5,7,11,13\}$ with $\ell\ne q$, $\ell^2\nmid N$: compare $v_\ell$ of the two
optimal degrees. Pairs (curve, $q$): (a) $6{,}348$, (b) $2{,}183$, (c) $5{,}150$. Triples (curve, $q$, $\ell$): (a) $24{,}373$, all with $v_\ell(\degphi)\ge
v_\ell(\deg\varphi_{E_q})$, strict in $2{,}779$ (e.g. 121d1 versus 11a1 at $\ell=3$: $24$ versus $1$; 75b1 versus 15a1; 150c1 versus 30a1); (b)
$8{,}348$, strict in $1{,}308$ (e.g. 275b1 versus 11a1 at $\ell=7$: $28$ versus $1$); (c) $19{,}554$, all equal. So strict inequality occurs in cases
(a) and (b), not "only in case (b)" (important_notes.md point 16, confirmed). Paper: the paragraph after Theorem thm:twist,
Theorem thm:quant.

**11.8 `rem:computation:comparison`** (remark; P). Why the book's numbers differ from the paper's and what does agree: the
ranges differ by a factor of fifty in conductor; rates of equality, of 3Ns failures and of the odd-part statistic all fall
with $N$, inside the book's range already; the qualitative claims (no violations of (eq:rule), (eq:main), (eq:twist) and of
Conjecture conj:eis; uncorrected failures exactly on 3Ns curves and by exactly one; minima equal to $e$ cell by cell; the
weights $w_3$; the Tamagawa refinement without exception; strict twist inequalities in cases (a) and (b)) all reproduce. One
sentence of the paper does not reproduce verbatim (Part 8, N1: 14a1). Paper: Section 6.

### Section 12. Reproducibility practice

**12.1 `rem:computation:paper-repository`** (remark; R, a description only). The paper's appendix names a repository and
directory with `scripts/step10_sym2_euler.py` (Euler factors), `scripts/step10_rule.py` and `scripts/step11_tw_boundary.py` (the
rule, the correction term, image statistics), `scripts/step12_tamagawa.py` (Tamagawa factors), `scripts/conj_check.py` (the two
corollary forms), `scripts/euler_rule.gp` (the appendix code) and `twist_lemma_check.gp`, a pinned data commit and the result
tables, and states that the pipeline was rerun from a clean clone and reproduced every count of Table tab:counts. The book
lists these as the paper's claims; it does not reproduce or link the scripts beyond the URL the paper gives, and the
writer must not describe their contents beyond the appendix's own words. Paper: the appendix, the AI statement.

**12.2 `conv:computation:checklist`** (convention; P). A reproducibility checklist, applied to the book's own runs: (1) pin
the data (repository commit hash, and SHA-256 sums of the files read: Part 6.5 lists the sums of the book's six files); (2)
record software versions (PARI, `cypari2`, Python) and non-default settings (`parisizemax`; random seeds, e.g. seed $0$ for the
permutations of 10.3); (3) separate data, code and results; write results as plain files with the counts, not only as
summaries; (4) rerun from a clean copy and compare counts; (5) cross-check independently (here: GP and Python implementations of
the bound agree; `ellmoddegree` against `degphi`; `ns3` against `galrep`; Lemma lem:euler against `lfunsympow`); (6) state what was
not checked. Paper: the appendix ("The pipeline was rerun from a clean clone"), the AI statement ("The scripts, the result
files and the pinned data commit are in the repository ... so that every count can be rerun").

**12.3 `rem:computation:book-scripts`** (remark; P). The scripts the chapter prints, with their role (the code itself is in
Part 7 of this outline, tested; the writer prints S1 to S3 in full and S4 to S8 in shortened form, about $40$ lines each at
most): S1 `euler_rule.gp` (the paper's appendix, verbatim); S2 `sessions.gp` (`rule_terms`, `tatedata`, `twistcheck`); S3
`table_small.gp` (`rulebound`, `readgal`, `reducible`, `tablerow`: one row of Table 11.1 in pure GP); S4 `compute.py` (one JSON
record per optimal curve: invariants, local data, $P_q$, $P_q(q^{-2})$, $a_q$, $v_q(j)$, `ns3`, torsion counts in the class, isogeny
degrees); S5 `analyse.py` and `tables*.py` (the five bounds and Tables 11.1 to 11.4, 11.6, 11.7, and 8.3); S6 `calib2.py`
(10.3, 10.5, the stratified and permutation versions); S7 `tam.py` (11.5); S8 `moddeg_check.py` (7.2). Paper: the appendix.

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200). The card lists all items of Part 2 (about 150 lines,
not counted); computational items appear on the card with the exact output in one line (for example "`rule` on 121a1 returns
`[1, 1]`") and the tag *(proved here)* for C, *(stated; reference)* for D.

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2 with its tag and `\Cref`; K3 to K5 restated in two lines; the five bounds | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1.1 (`lfunsympow`); Section 1.4 (component groups from the tables); Lemma lem:euler and Lemma lem:twist (the PARI checks); Remark rem:wild; Proposition prop:ns (`ns3`); Proposition prop:forms (the factor at 2); the Example of Section 3 and the 99A1 remark; Section sec:data and all its subsections and tables; the paragraph after Theorem thm:twist; the abstract's counts; the appendix | 45 |
| 1 | Introduction and conventions | purpose; 1.1 to 1.3 as `convention` environments (K1 to K11 condensed); the physics aside; the debts of Chapters 2, 3, 9 to 15, 17 to 19 in one paragraph | 80 |
| 2 | PARI/GP from zero | 2.1 to 2.4; a first session in `lstlisting`; the pitfalls `warning` | 150 |
| 3 | Invariants of a curve in PARI | 3.1 to 3.8; the outputs of `ellglobalred`, `lfunsympow`, `lfuneuler`, `.tate`, `elldivpol`, `elltwist`, `ellmoddegree`, `ellweilcurve`; the code-idiom table; S2 printed | 230 |
| 4 | Cremona's tables and `ecdata` | 4.1 to 4.4; the file table with sample lines; reading files in GP and Python; optimality and 990h3; labels; `paperlink` for Section sec:data | 140 |
| 5 | The function `rule(E, l, iii)` | 5.1 (S1 printed with line numbers), 5.2 (line by line), 5.3 (proposition and proof), 5.4 (pitfalls `warning`); `paperlink` for the appendix | 170 |
| 6 | Worked sessions | 6.1 to 6.8, each with input, exact output, breakdown and a two-line reading | 210 |
| 7 | Modular degrees and congruence numbers | 7.1 to 7.3; pointers to Chapters 14 and 19 | 70 |
| 8 | Populations, violations and descriptive statistics | 8.1 to 8.4; the base-rate table; Appendix A cited for the vocabulary | 110 |
| 9 | The protocol | 9.1 to 9.5; the status table of 9.2; multiple comparisons; the toy protocol; `paperlink` for Section sec:data | 150 |
| 10 | The calibration argument | 10.1 (with proof), 10.2 to 10.6; the reading of 10.4 as a `remark` with two lists ("shows", "does not show") | 150 |
| 11 | Reproducing the paper's tables | 11.1 to 11.8; four `booktabs` tables and short readings; S3 printed, S4 to S7 shortened | 190 |
| 12 | Reproducibility practice | 12.1 to 12.3; the checklist; the book's data pin | 60 |
| 13 | Exercises | the 18 exercises of Part 4.2 | 140 |
| 14 | Notes and references | PARI, PARIusers, Cremona97, CremonaBook, ecdata, LMFDB, Sutherland16, Zywina15, Watkins02, Zagier85, Feller68, Wasserman04 (after B-b of Part 8), RHB06; the paper's appendix; what was verified and with which versions | 45 |
| | **total** | | **1,940** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 map row, or paper hook | line-up items |
|-|-|
| PARI/GP for the reader who has never used it (installation) | 2.1, 2.2, 2.3, 2.4 |
| `ellinit`, `ellglobalred` and its output (conductor, minimal model change, Kodaira symbols and Tamagawa numbers per prime, the local data structure with the Kodaira codes) | 3.1, 3.2 (codes: Chapter 10, 5.5) |
| `ellap`, `ellan`, `elltors`, `ellisomat` | 2.3 |
| `ellmoddegree` (and its memory needs) | 3.8, 7.1, 7.2 |
| `elldivpol` | 3.6 |
| `lfuncreate` / `lfunsympow` / `lfuneuler` and the conventions for the symmetric square Euler factor | 3.3, 3.4 (`lfuncreate` mentioned in 3.3 as the general constructor, not needed) |
| `ellinit` over $\Q_q$ and the Tate parameter (not `elltatepairing`), its valuation and unit part | 3.5, 6.8 |
| `valuation`, `factor` | 2.2, 2.4(f), 3.6 |
| Cremona's tables and `ecdata`: allcurves, allbsd, alldegphi (= `degphi`), allgens, alllabels, allisog; Kodaira symbols and Tamagawa numbers; mod $\ell$ images with Sutherland's labels; optimality and the label "1"; LMFDB labels | 4.1 to 4.4 (`allgens` not in the local copy: 4.1 says so) |
| reading a Cremona label (11a1, 121a1, 121c, 121d, 539c1, 980i1, 726a1, 99A1, capitalisation) | 4.4 (full list: Chapter 9, 12.1) |
| the data protocol: four ranges; pre-registration; "nothing was adjusted"; blind-tested versus confirmed; the out-of-table set for Conjecture conj:euler | 9.1, 9.2, 9.3, 9.5 |
| elementary statistics: what a violation is; the calibration argument with the numbers; what it does and does not show; equality rates and mean excess as descriptive statistics; base rates by Kodaira type; multiple comparisons; why a hold-out | 8.2, 8.3, 8.4, 9.4, 10.1 to 10.6 |
| `rule(E, l, iii)` reproduced and explained line by line (`R[4]`, `R[5]`, the code `k`, $r=P_q(q^{-2})$ with the multiplicative correction, the $\mathrm{III}$ exclusion, $w_3$, $t_\ell$ from $v_q(j)$, `ns3`) | 5.1 to 5.4 |
| worked sessions: 121a1 `[1, 1]`; 726a1 `[2, 2]` with and without `iii`; 539c1; 980i1; 99A1 (degree 4, congruence number 12 not in PARI) | 6.1 to 6.5, 7.3 |
| computing $e_\ell(E,q)$ by hand from the type and checking against `lfunsympow` | 3.4 |
| computing $t_\ell(E,q)$ | 3.5, 6.1 to 6.8 |
| the mod 3 image 3Ns via `elldivpol` | 3.6, 6.2 |
| the twist lemma check (`twist_lemma_check.gp`: how to write it) | 3.7 (S2's `twistcheck`), Exercise 14 |
| reproducing a row of the paper's tables on a small range (a GP loop over `ecdata`) | 11.1 (S3), Exercise 7 |
| how the modular degree is computed (Watkins, Cremona; why expensive) | 7.1 |
| the repository named in the appendix (descriptive list) | 12.1 |
| reproducibility practice (pinned commits, clean clone) | 12.2, 1.1 |
| Section 6 row: PARI/GP, Cremona's tables, ecdata, LMFDB, Sutherland's labels | 2, 3, 4 |
| Section 6 row: the statistical protocol, calibration, hold-out sets | 8, 9, 10 |
| Section 6 row: the function `rule(E, l)` and the Kodaira codes (with Chapter 10) | 3.2, 5 |
| Section 6 row: the worked examples 11a1, 20a1, 121a1, 539c1, 980i1, 726a1, 99A1 (with 9, 14, 15, 21) | 2.3, 3.1, 3.5, 6.1 to 6.7 |
| hook: Section 1 ("PARI's `lfunsympow(E,2)` returns these factors at every prime, including 2 and 3") | 3.3, 6.6 |
| hook: Remark rem:wild | 6.6 (mathematics: Chapter 19, 10.1, 10.2) |
| hook: Lemma lem:euler ("confirmed against PARI's `lfunsympow` on every curve of the tables") | 3.4 |
| hook: Section 1.4 (component groups; Cremona's tables and optimality) | 3.1, 3.2, 4.3, 11.2 |
| hook: Proposition prop:ns (3-division polynomial) | 3.6, 5.3(ii) |
| hook: Proposition prop:forms ($92{,}812$ curves, factor $1+2X$ at 2) | Part 7, R4 ($3{,}226$ optimal curves below $10{,}000$, all $1+2X$); point 43 |
| hook: Section sec:data, protocol paragraph | 1.1, 9.1, 9.2, 9.3 |
| hook: Section 6.2 and Table tab:uniform | 11.1 |
| hook: Section sec:sharp | 8.2, 10.1 to 10.6 |
| hook: Section sec:tam | 3.5, 6.8, 11.5 |
| hook: Section sec:iso and Table tab:iso | 8.3, 11.4 |
| hook: Section sec:forms and Table tab:counts | 11.2 |
| hook: Section sec:anomaly and Table tab:ns | 3.6, 6.2, 11.3 |
| hook: Section sec:wild and Table tab:isolated | 6.6, 9.5 (the $w_3$ minima) |
| hook: Section sec:oot and Table tab:oot | 9.1, 9.2, 9.3 (no reproduction possible: the curves are not published in the paper) |
| hook: Section sec:eis (image labels 3Cs.1.1, 3B.1.1) | 4.4, 11.6 |
| hook: the paragraph after Theorem thm:twist ($157{,}938$ and $292{,}580$ pairs) | 11.7 |
| hook: the Example of Section 3 (congruences "checked for $p<500$", $p<1000$) | 2.3 (`ellan`, `ellap`); Exercise 2; Sturm's bound: Chapter 12, point 46 |
| hook: the appendix (all paragraphs) | 1.1, 5, 6, 12.1 |
| hook: the abstract's counts ("$893$ curves", "$57\%$", "a third of the cases") | 9.1, 11.3 (point 25) |
| also: what Chapters 2, 3, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19 deferred here | Part 5 |

### 4.2 Exercises (Section 13 of the chapter), graded from easy to harder

1. Run `ellglobalred` on 20a1 and 726a1, read off the conductor, the bad primes, the Kodaira codes and the $c_p$, and say which
   entries the paper's `R[4][,1]` and `K[i][2]` are. Why does code $1$ never occur in the list?
2. With `ellan` compute $a_n$ for 121a1 and 11a1 for $n\le500$ and check the paper's claim $a_p(\text{121a1})\equiv\chi_{-11}(p)a_p(\text{11a1})\pmod3$ for
   $p\ne3,11$; then say why a check up to Sturm's bound (Chapter 12) proves it for all $n$.
3. Using `lfunsympow` and `lfuneuler`, compute $P_q$ and $e_3(E,q)$ for 121a1 at $11$, 147b1 at $7$, 539d1 at $7$ and 726a1 at $11$, and check
   them against the table of Section 1 of the paper (Lemma lem:euler) by the function `euler_by_type` of 3.4.
4. Check the paper's claim that `rule(ellinit([1,1,1,-30,-76]), 3)` returns `[1, 1]` and that for 726a1 `rule(E,3)` and `rule(E,3,1)` both
   return `[2, 2]`; print the breakdown with `rule_terms` and identify each term with a term of (eq:rule).
5. Run `rule` on 11a1, 11a2, 11a3 at $\ell=5$ and on 990h1, 990h3 at $\ell=3$. Explain each output, in particular the negative entry for
   11a3, using `ellmoddegree` and `ellweilcurve`. Which of these runs does the paper's statement concern?
6. Show that `ns3(E)` is $1$ iff $\psi_3$ is a product of two irreducible quadratics over $\Q$, whatever the content of $\psi_3$ and whatever
   order `factor` lists the factors in; find a CM curve with `ns3(E) = 1` and explain why Conjecture conj:euler excludes it.
7. Using S3, reproduce the row $\ell=5$, $N<2000$ of Table 11.1 and compare it with the Python result $[5622, 915, 0, 845]$ (curves, positive
   bounds, violations, equalities).
8. List the 3Ns optimal curves of conductor below $2000$ that violate the uncorrected bound, and check the paper's claims that
   the shortfall is always $1$ and that each violation involves a prime $p\equiv-1\pmod3$ with $t_3(E,p)\ge1$.
9. Compute the Tate parameter of 791a1 at $7$ with `ellinit(E, O(7^30)).tate`, decide whether its unit part is a cube in $\F_7^\times$, and
   check the paper's claim (Section sec:tam) that the extra Tamagawa term then raises the bound to $v_3(\degphi)$.
10. (Calibration.) Let $X$ be a sum of independent indicators with $E[X]=\mu$. Prove $P(X=0)\le e^{-\mu}$ and, using only pairwise
    independence, $P(X=0)\le\operatorname{Var}X/\mu^2\le1/\mu$. Apply both to the paper's $\mu\approx605{,}000$ and to the book's $\mu=14{,}275$.
11. Show that under the null hypothesis of 10.1 the bound-$0$ distribution and the pooled distribution of $v$ estimate the same
    thing, and explain why the book's values $59.7\%$ and $23.9\%$ for $P(v=0)$ are evidence against the null.
12. Check the paper's claim that among bound-$0$ curves $53.2\%$ have $3\nmid\degphi$ against the book's $59.7\%$ below $10{,}000$, and
    compute the same share on $N<5000$ and on $5000\le N<10000$. What does the trend suggest about the paper's ranges?
13. (Multiple comparisons.) Suppose $m=200$ false candidate inequalities each survive a working-set check with probability
    $\pi=0.05$ and a hold-out check with probability $\pi'=0.05$, independently. How many false survivors are expected after the
    working set, and after the hold-out? What changes if the hold-out is reused for a second round of candidates?
14. Write `twist_lemma_check.gp`: for every optimal curve below $2000$ and every odd bad prime $q$, compare the Kodaira code of the
    twist by $q^*$ at $q$ with Lemma lem:twist (ii), and check (i) at the other odd primes. Extend to $q=3$ and test important_notes.md
    point 51.
15. Classify each data statement of Section 6 of the paper as blind-tested, confirmed only, or a theorem checked, quoting the
    sentence of Section sec:data that decides it; say what a fresh hold-out would have to contain to test the correction term $h_3$.
16. Reproduce the list of Eisenstein curves at $\ell=3$ below $10{,}000$ with deficit $D=2$ and check the paper's claim that the
    3Cs.1.1 curves among them have "rank 0 and torsion $\Z/3$". Then prove that no non-CM curve has both $E[3]\simeq\Z/3\oplus\mu_3$ and a
    point of order $9$ (point 17).
17. (Toy protocol.) Read off the minima of $v_3(\degphi)$ at $q=3$ on $N<5000$ as in 9.5, freeze them, and test them on $5000\le N<10000$.
    Then do the same for a statement you choose yourself on the working set, and report honestly whether it survived.
18. Compute the odd-part statistic of 10.6 on $N<5000$ and on $5000\le N<10000$, and explain why the paper's $1.85\%$ is so much smaller
    than the book's $17.1\%$.
