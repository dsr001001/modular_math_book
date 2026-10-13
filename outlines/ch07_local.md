# Line-up for Chapter 07: Local fields (`ch:local`, `chapters/ch07_local.tex`)

Stage 1 output (core results in teaching order). Part II (Number fields and local fields). Target length 2,080
lines of LaTeX excluding the card (Part 10 below), inside the 1,000 to 2,200 range of PLAN.md Section 7.3.
Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference.

Item format (as in the Chapter 2 to 6 outlines): number, label-ready name, kind, rigour tag; the precise
statement with all hypotheses; reference (book and theorem number only where sure, otherwise book and chapter or
section); the paper's use by its `\label` names, or "background". Small computations (Hensel lifts, Teichmuller
lifts, unit indices, the Tate parameter of 11a1, the tame relation at finite level, the adjoint of $\mathrm{sp}(2)$,
quadratic extensions of $\Q_2$) were checked by Python scripts in `/tmp/ch07` (verification log, Part 14).

## 0. Purpose of the chapter, and what it must deliver

### 0.1 Purpose

The paper works at a bad prime $q\ne\ell$ with the restriction of $\rho=\rho_{E,\ell}$ to a decomposition group
$G_{\Q_q}$. Every local statement it makes rests on a small amount of local field theory, which this chapter supplies
in full:

1. **Lemma lem:tamagawa-exp.** Unramified base change does not change inertia; $\mu_{\ell^\infty}\subset\Q_q^{\mathrm{ur}}$;
   the units of $\Q_q^{\mathrm{ur}}$ are $\ell^t$-th powers (Hensel); hence $x\in\Q_q^\times$ has an $\ell^t$-th root in
   $\Q_q^{\mathrm{ur}}$ iff $\ell^t\mid v_q(x)$ (items 4.2, 4.4, 6.2).
2. **Lemma lem:tamfactor.** The tame character $t_\ell\colon I_q\to\Z_\ell(1)$, the identification of the maximal pro-$\ell$
   quotient of $I_q$ with $\Z_\ell(1)$ (kernel of supernatural order prime to $\ell$), the relation $\Frob\,t\,\Frob^{-1}=t^{q}$,
   i.e. $\Frob^{-1}t\Frob=t^{q^{-1}}$ (arithmetic $\Frob$), the restriction of a Kummer class $\kappa_x$ to $I_q$ being
   $v_q(x)\,t_\ell$, the decomposition $\kappa_x=v_q(x)\kappa_q+\kappa_u$, the existence of a Frobenius lift fixing the
   $\ell$-power roots of $q$, and the explicit group $\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}\simeq\Z_\ell\times\Z/\ell^{v_\ell(q-1)}$
   (items 2.7, 5.3 to 5.5, 6.1, 6.2). The group cohomology is Chapter 16, the cohomological identification of $c'$ is
   Chapter 17.
3. **Lemma lem:IV, Remark rem:types, Lemma lem:euler.** A finite image of inertia of order prime to $q$ is cyclic and
   Frobenius acts on it by the $q$-th power; the Weil-Deligne description of the local representations (unramified,
   finite cyclic tame inertia, $\mathrm{sp}(2)$ and its twists); inertia invariants; the local $L$-factor with an explicit
   Frobenius convention; the adjoint of each shape and its $L$-factor (items 5.6, 7.1 to 7.6, 8.1, 8.2, 9.1 to 9.4).
4. **Lemma lem:twist (iii) and the conductor exponents in Lemma lem:twist (i), (ii), Lemma lem:IV, Remark rem:types.**
   The Artin conductor $a(V)=\operatorname{codim}V^{I}+\operatorname{sw}(V)$ and the Weil-Deligne conductor; tame
   quadratic characters at odd $q$; the unramified twist of Steinberg has exponent $1$, its twist by a ramified
   quadratic character has exponent $2$; finite inertia of order $2,3,4,6$ without fixed vectors has exponent $2$ when
   tame (items 6.3, 6.4, 8.3, 8.4, 9.2, 9.3).
5. **Remark rem:wild and Section sec:wild.** Wild inertia $P_q$ is pro-$q$; its image in $\GL_2(\Z_\ell)$ is a finite $q$-group;
   at $q=2,3$ the image of inertia need not be cyclic and the Swan conductor can be positive; an inertia image of order
   $3$ is wild at $q=3$ and tame at $q=2$ (items 5.1, 5.7, 9.5).
6. **Section 1.1 (the definition of $L_p(A_f,s)$), Lemma lem:fpr and the paragraph after Lemma lem:dfg21.** The
   geometric Frobenius in $L$-factors, so that $L_p(M(1),s)=L_p(M,s+1)$ (item 8.2; important_notes.md point 11).

It also discharges what earlier chapters deferred to it (by `\Cref{ch:local}`): Chapter 2 (the completion $\Q_p$,
Hensel, the structure of $\Z_p^\times$, $u\in\Z_q^\times$ versus its reduction), Chapter 3 ($\Q_p$ analytically; Chapter 3
has $\Z_\ell$ algebraically), Chapter 5 (Kummer theory over $\Q_p$ and $\Q_p^{\mathrm{ur}}$, unramified base change,
$\Frob\,t\,\Frob^{-1}=t^q$), Chapter 6 (item 3.10(v): $D_p\simeq G_{\Q_p}$; item 3.11 in profinite form; item 4.7(iv): the local
meaning of $\Z_3[\zeta_3]$; item 4.9: Hensel; item 5.7(ii): Artin conductors of characters; item 7.4:
$\mathcal O_K\otimes\Z_\ell=\prod_\lambda\mathcal O_{K,\lambda}$), Chapter 16 (the imported facts of its tame-inertia-example and
model-setting).

### 0.2 Global conventions fixed in this chapter (to be typeset as `convention` environments)

* **L1 (fields).** $p$ is a prime; $K$ denotes $\Q_p$ or a finite extension of it, with valuation ring $\mathcal O_K$, maximal
  ideal $\mathfrak m_K$, uniformiser $\varpi_K$, residue field $k_K=\F_q$ ($q=p^{f}$), normalised valuation $v_K$ ($v_K(\varpi_K)=1$)
  and normalised absolute value $|x|_K=q^{-v_K(x)}$. On $\Q_p$: $v_p$, $|\cdot|_p$, as in Chapter 2. When the paper's prime
  is meant, the local field is $\Q_q$ and $\ell\ne q$; in the general theory the residue characteristic is $p$ and
  $\ell\ne p$. Say once that the letter $q$ is used both for $\#k_K$ and for the paper's bad prime, which agree when $K=\Q_q$.
* **L2 (closures).** $\Qbar_p$ is a fixed algebraic closure; $G_K=\Gal(\Qbar_p/K)$; $K^{\mathrm{ur}}\subset K^{\mathrm{tame}}\subset\Qbar_p$
  the maximal unramified and maximal tamely ramified extensions; $I_K=\Gal(\Qbar_p/K^{\mathrm{ur}})$, $P_K=\Gal(\Qbar_p/K^{\mathrm{tame}})$;
  for $K=\Q_p$: $I_p$, $P_p$. Embeddings $\Qbar\to\Qbar_p$ identify $G_{\Q_p}$ with decomposition groups in $G_\Q$ (3.5).
* **L3 (Frobenius: both, named).** $\Frob=\Frob_K$ denotes an **arithmetic** Frobenius: any element of $G_K$ inducing
  $x\mapsto x^{q}$ on $\bar k_K$, well defined modulo $I_K$; it acts on $\mu_m$ ($p\nmid m$) by $\zeta\mapsto\zeta^q$, and
  $\chi_\ell(\Frob)=q$ for $\ell\ne p$. The **geometric** Frobenius is $\Phi=\Frob^{-1}$. An eigenvalue $\lambda$ of $\Frob$ is an
  eigenvalue $\lambda^{-1}$ of $\Phi$. Group-theoretic statements (the tame relation, conjugation actions, the matrices of
  Lemma lem:tamfactor) use $\Frob$; local $L$-factors use $\Phi$ (8.2). This is the convention of Chapter 5 (C2),
  Chapter 6 (3.7), Chapter 16 and Chapter 21 (C2), and of DFG04 1.7.2 for $L$-factors.
* **L4 (the norm on the Weil group and the monodromy relation).** For $w$ in the Weil group $W_K$, $d(w)\in\Z$ is defined
  by $w|_{K^{\mathrm{ur}}}=\Frob^{d(w)}$ and $\|w\|=q^{d(w)}$; so $\|\Frob\|=q$, $\|\Phi\|=q^{-1}$, and $\|w\|=\chi_\ell(w)$ for $\ell\ne p$.
  A Weil-Deligne representation satisfies $r(w)Nr(w)^{-1}=\|w\|N$, that is
  $$r(\Frob)\,N\,r(\Frob)^{-1}=q\,N,\qquad r(\Phi)\,N\,r(\Phi)^{-1}=q^{-1}N .$$
  (PLAN.md writes "$\Frob\,N\,\Frob^{-1}=p^{-1}N$": that is the geometric form; see Part 15, B-a.) This $\|\cdot\|$ agrees with
  Tate's normalisation in "Number theoretic background" ($\|\Phi\|=q^{-1}$).
* **L5 (Tate twists and the tame character).** $\Z_\ell(1)=\varprojlim_k\mu_{\ell^k}$ (Chapter 5, C6), written additively when it
  carries cocycles; $G_K$ acts through $\chi_\ell$. The tame character $t_\ell\colon I_K\to\Z_\ell(1)$ is canonical (5.3). Wherever
  a $\Z_\ell$-valued version is needed, a generator $\zeta=(\zeta_{\ell^k})_k$ of $\Z_\ell(1)$ is fixed and
  $t_\zeta\colon I_K\to\Z_\ell$ is $t_\ell$ followed by $\Z_\ell(1)\simeq\Z_\ell$, $\zeta\mapsto1$. Changing $\zeta$ multiplies $t_\zeta$ by a unit.
* **L6 ($L$-factors).** For a continuous representation $V$ of $G_K$ over a finite extension of $\Q_\ell$, $\ell\ne p$:
  $L(V,s)=\det(1-\Phi\,q^{-s}\mid V^{I_K})^{-1}$, $\Phi$ geometric. For $K=\Q_p$ and a $G_\Q$-representation this is the
  paper's $L_p(V,s)$ (Section 1.1) read with the geometric Frobenius (important_notes.md point 11).
* **L7 (labels and typography).** Labels `...:local:...`; the names in the line-up are the label stems. No em or en
  dashes, no double hyphens anywhere (write "Grothendieck's monodromy theorem", "Weil-Deligne", "Hasse-Arf" with plain
  hyphens; ranges "1 to 8"); ASCII source; `\ell`; Kodaira symbols as in PLAN.md 7.1. Use `\operatorname{sp}` or
  `\mathrm{sp}` for the special representation and `\operatorname{sw}` for the Swan conductor (no new macros).

### 0.3 Scope check (PLAN.md Section 4 entry for Chapter 7)

Each scope item is mapped to line-up items in Part 11 (coverage table). In order of the PLAN entry: absolute values,
completions (1.1 to 1.3); $\Q_p$ and $\Z_p$ as completions and as inverse limits, $p$-adic expansions (1.4, 1.5); Hensel in two
forms (2.1, 2.2, 2.3); $\Z_p^\times$ and $\Q_p^\times$, $1+p\Z_p\simeq\Z_p$ via $\log/\exp$ (2.5); roots of unity, Teichmuller (2.4,
2.6); squares and $\ell$-th powers in $\Q_p^\times$ (2.7, 2.8); finite extensions, $e$, $f$ (3.1 to 3.4); unramified extensions
(4.1, 4.2); totally ramified, tamely and wildly ramified extensions (3.2, 3.3, 3.6, 5.1); $\Q_p^{\mathrm{ur}}$ (4.2); $I_p$, $P_p$, the
tame quotient and the tame character (5.2, 5.3); the tame relation (5.4, 5.8); $G_{\Q_p}$ and its filtration (5.1, 5.2); Kummer
theory over $\Q_p$, restriction of a Kummer class to inertia (6.1, 6.2); quadratic extensions and characters locally (6.3,
6.4); the Weil group and Weil-Deligne representations (7.1 to 7.6); inertia invariants, $L$-factor, Artin conductor (8.1 to
8.4); the special cases (9.1 to 9.5). Additions not in the PLAN entry but needed by deferrals or by the paper: local
class field theory as a statement (6.5, for conductors of characters), $\epsilon$-factors as a statement (8.5, which
Chapter 15 "recalls from Chapter 7"), the decomposition-group comparison (3.5).

## 1. Line-up, Section 1: absolute values, completions, $\Q_p$ and $\Z_p$

### 1.1 `def:local:absval` (definition and proposition) P
An *absolute value* on a field $F$ is a map $|\cdot|\colon F\to\R_{\ge0}$ with $|x|=0$ iff $x=0$, $|xy|=|x||y|$ and
$|x+y|\le|x|+|y|$; it is *nonarchimedean* if $|x+y|\le\max(|x|,|y|)$ (ultrametric). (i) $|\cdot|$ is nonarchimedean iff
$|n\cdot1|\le1$ for all $n\in\Z$. (ii) If nonarchimedean: $|x+y|=\max(|x|,|y|)$ whenever $|x|\ne|y|$ ("all triangles are
isosceles"); $\mathcal O=\{|x|\le1\}$ is a subring (the valuation ring), $\mathfrak m=\{|x|<1\}$ its unique maximal ideal,
$\mathcal O^\times=\{|x|=1\}$, $k=\mathcal O/\mathfrak m$ the residue field; open balls are closed, every point of a ball is a
centre; a series $\sum a_n$ in a complete $F$ converges iff $a_n\to0$. (iii) $|\cdot|$ is *discrete* if $|F^\times|$ is a
discrete subgroup of $\R_{>0}$; then $|F^\times|=c^{\Z}$, $\mathcal O$ is a DVR (Chapter 3) and $|x|=c^{v(x)}$ for the normalised
valuation $v$. (iv) Two absolute values define the same topology iff $|\cdot|_1=|\cdot|_2^{s}$ for some $s>0$ (equivalent).
(v) (Recalled from Chapter 2, item 11.2; R) Ostrowski: every nontrivial absolute value on $\Q$ is equivalent to $|\cdot|_\infty$
or to exactly one $|\cdot|_p$. Examples: $|\cdot|_p$ on $\Q$ with $\mathcal O=\Z_{(p)}$, $k=\F_p$; the $\mathfrak p$-adic absolute value
$|x|_{\mathfrak p}=N\mathfrak p^{-v_{\mathfrak p}(x)}$ on a number field (Chapter 6, 2.2, 2.4(iv)). Reference: Neukirch II.3; Koblitz
Ch. I; Cassels-Frohlich Ch. II (Cassels, "Global fields"). Paper: background (the field $\Q_q$ and the ring $\Z_\ell$ in
Sections 2 and 4).

### 1.2 `rem:local:ostrowski-product` (remark) R
Product formula $\prod_{v\le\infty}|x|_v=1$ for $x\in\Q^\times$ (Chapter 2, 11.2(ii); cite, do not redo). Weak approximation for
finitely many inequivalent absolute values (stated). Reference: Neukirch II.3. Paper: background.

### 1.3 `thm:local:completion` (construction and theorem) P
Let $(F,|\cdot|)$ be a field with an absolute value. There is a field $\hat F$ with an absolute value extending $|\cdot|$,
complete (every Cauchy sequence converges), in which $F$ is dense; it is unique up to a unique isometric
$F$-isomorphism (the *completion*). Construction: Cauchy sequences modulo null sequences. If $|\cdot|$ is nonarchimedean:
(i) $|\hat F^\times|=|F^\times|$ (the value group does not grow); (ii) $\hat{\mathcal O}$ is the closure of $\mathcal O$ and
$\mathcal O/\mathfrak m^n\simeq\hat{\mathcal O}/\hat{\mathfrak m}^n$ for discrete $|\cdot|$ (in particular the residue field does not change);
(iii) for discrete $|\cdot|$ with uniformiser $\varpi$, $\hat{\mathcal O}\simeq\varprojlim_n\mathcal O/\varpi^n\mathcal O$ as topological rings (this
is the bridge to Chapter 3's algebraic completion). Reference: Neukirch II.4; Serre, Local Fields, Ch. II, Section 1.
Paper: background.

### 1.4 `def:local:qp` (definition and theorem) P
$\Q_p$ is the completion of $\Q$ for $|\cdot|_p$, and $\Z_p=\{x\in\Q_p:|x|_p\le1\}$. Then: (i) $\Z_p$ is the closure of $\Z$ (and
of $\Z_{(p)}$) in $\Q_p$; it is a complete DVR with uniformiser $p$, residue field $\F_p$, ideals $p^n\Z_p$, and $v_p$ extends to
$\Q_p$; (ii) $\Z_p\to\varprojlim_n\Z/p^n$, $x\mapsto(x\bmod p^n)_n$, is an isomorphism of topological rings (product of
discrete topologies on the right), so the analytic $\Z_p$ of this chapter is the algebraic $\Z_\ell$ of Chapter 3 (item 6.4)
and the profinite group of Chapter 1 (item 7.2) at $\ell=p$; (iii) $\Z_p^\times=\{|x|_p=1\}$, and $x\in\Z_p$ is a unit iff
$x\not\equiv0\pmod p$; every $x\in\Q_p^\times$ is uniquely $x=p^{v_p(x)}u$ with $u\in\Z_p^\times$, so
$\Q_p^\times=p^{\Z}\times\Z_p^\times$ and $\Q_p=\Z_p[1/p]=\operatorname{Frac}\Z_p$; (iv) $\Z_p$ is compact, $\Q_p$ is locally compact and
totally disconnected; (v) for $q\ne p$ prime, $q\in\Z_p^\times$, so $q^{-1}\in\Z_p$ (the exponent $q^{-1}$ of the tame relation).
Reference: Serre, Course in Arithmetic, Ch. II, Section 1; Koblitz Ch. I; Neukirch II.1-II.2 (cite II.1, II.2). Paper:
background (every $\Z_\ell$, $\Q_\ell$, $\Q_q$); the exponent $q^{-1}\in\Z_\ell$ in Lemma lem:tamfactor.

### 1.5 `prop:local:expansions` (proposition) P
Every $x\in\Q_p$ has a unique expansion $x=\sum_{i\ge v}a_ip^i$, $v=v_p(x)$, $a_i\in\{0,1,\dots,p-1\}$, $a_v\ne0$ (for $x\ne0$), the
series converging in $\Q_p$; $x\in\Z_p$ iff $v\ge0$; the digits of $x\in\Z_p$ are those of the residues $x\bmod p^n$. $x\in\Q$ iff
the digit sequence is eventually periodic. Examples: $-1=\sum_{i\ge0}(p-1)p^i$; $1/(1-p)=\sum p^i$; in $\Z_5$,
$\sqrt{-1}\equiv2+1\cdot5+2\cdot5^2+1\cdot5^3\pmod{5^4}$ (that is $182$, item 2.3). (RHB aside: a "Laurent series in $p$", but
with carries.) Reference: Koblitz Ch. I; Serre, Course in Arithmetic, Ch. II. Paper: background.

## 2. Line-up, Section 2: Hensel's lemma, units, roots of unity, powers

### 2.1 `thm:local:hensel` (theorem, Hensel's lemma in two forms) P
Let $K$ be a field complete for a nonarchimedean absolute value with valuation ring $\mathcal O$, maximal ideal $\mathfrak m$ and
residue field $k$ (in this chapter $K$ is $\Q_p$ or a finite extension; also the $\ell$-adic fields). Let $f\in\mathcal O[X]$.
(a) (Simple-root form.) If $a_0\in\mathcal O$ satisfies $f(a_0)\equiv0\pmod{\mathfrak m}$ and $f'(a_0)\not\equiv0\pmod{\mathfrak m}$, there is a
unique $a\in\mathcal O$ with $f(a)=0$ and $a\equiv a_0\pmod{\mathfrak m}$. (b) (Newton form.) If $a_0\in\mathcal O$ satisfies
$|f(a_0)|<|f'(a_0)|^2$, then the Newton sequence $a_{n+1}=a_n-f(a_n)/f'(a_n)$ lies in $\mathcal O$ and converges to a root $a$ of
$f$, which is the unique root with $|a-a_0|<|f'(a_0)|$; moreover $|a-a_0|=|f(a_0)/f'(a_0)|$ and $|f'(a)|=|f'(a_0)|$. (a) is
(b) with $|f'(a_0)|=1$. Proof: the Taylor expansion $f(x+h)=f(x)+f'(x)h+h^2g(x,h)$ with $g\in\mathcal O[x,h]$ gives
$|f(a_{n+1})|\le|f(a_n)|^2/|f'(a_0)|^2$ and $|f'(a_n)|=|f'(a_0)|$ inductively; uniqueness from the same expansion. Warning: (a)
is false without the hypothesis on $f'(a_0)$ ($X^2-p$ has a root mod $p$, none in $\Q_p$; $X^2+7$ has
no simple root mod $2$, since $f'=2X$, yet $-7$ is a square in $\Z_2$ by (b)). Reference: Neukirch II.4 (Hensel's lemma and its
Newton form; cite the section); Serre, Course in Arithmetic, Ch. II, Section 2; K. Conrad, "Hensel's lemma" (expository
notes; add to `bib/ch07.bib` only if cited). Paper: Lemma lem:tamagawa-exp (units of $\Q_q^{\mathrm{ur}}$ are $\ell^t$-th powers),
Lemma lem:tamfactor (an $\ell^k$-th power in $\F_q^\times$ lifts), via 2.7 and 6.2; Chapter 6 (4.9: $\Z_\ell[\zeta_3]$).

### 2.2 `thm:local:hensel-factor` (theorem, factorisation form, with a corollary) S
Let $K,\mathcal O,k$ be as in 2.1. If $f\in\mathcal O[X]$ is primitive ($\max|a_i|=1$) and $\bar f=\bar g\bar h$ in $k[X]$ with $\bar g,\bar h$
coprime, then $f=gh$ in $\mathcal O[X]$ with $\bar g$, $\bar h$ the reductions of $g,h$ and $\deg g=\deg\bar g$. Corollary: if
$f=a_nX^n+\dots+a_0\in K[X]$ is irreducible with $a_0a_n\ne0$, then $\max_i|a_i|=\max(|a_0|,|a_n|)$; in particular a monic
irreducible $f$ with $f(0)\in\mathcal O$ lies in $\mathcal O[X]$. (Sketch: successive approximation modulo $\mathfrak m^n$, using a
Bezout relation for $\bar g,\bar h$.) Reference: Neukirch II.4 (cite the section). Paper: background (used in 3.1).

### 2.3 `ex:local:hensel-examples` (worked examples) P
(a) $\sqrt{-1}\in\Z_5$: the two roots are $\equiv182$ and $\equiv443\pmod{5^4}$; $182$ is the Teichmuller lift of $2$ (2.4) and
$182^2+1=53\cdot5^4$. (b) $\sqrt{-3}\in\Z_7$: roots $\equiv37,306\pmod{7^3}$. (c) $X^2+X+1$ in $\Z_7$: roots $\equiv18,30\pmod{49}$,
so $\Z_7[\zeta_3]\simeq\Z_7\times\Z_7$ (Chapter 6, 4.9(ii)). (d) $\sqrt2\in\Z_7$: roots $\equiv108,235\pmod{7^3}$. (e) Squares in
$\Z_2$: $u\in\Z_2^\times$ is a square iff $u\equiv1\pmod8$ (2.1(b) with $f=X^2-u$, $a_0=1$, $|f'(1)|^2=1/4$; conversely odd
squares are $\equiv1\bmod8$); so $-7$ is a square in $\Z_2$, $-1$, $3$, $5$ are not. (f) Squares in $\Z_p$, $p$ odd: $u\in\Z_p^\times$ is
a square iff $\bar u$ is a square in $\F_p$. (g) The trichotomy of Chapter 6, 4.9, for $\Z_\ell[\zeta_3]$ and $\Z_\ell[i]$ is now
proved: split iff $X^2+X+1$ (resp. $X^2+1$) has a simple root mod $\ell$. Paper: Lemma lem:euler (the rings
$\Z_\ell[\zeta_3]$, $\Z_\ell[i]$; important_notes.md point 12), background.

### 2.4 `thm:local:teichmuller` (theorem) P
Let $K$ be complete and discretely valued with finite residue field $k=\F_q$. (i) For $a\in k$ and any lift $\tilde a\in\mathcal O$,
the limit $\omega(a)=\lim_{n\to\infty}\tilde a^{q^n}$ exists and does not depend on $\tilde a$; $\omega(a)$ is the unique lift of $a$
with $\omega(a)^q=\omega(a)$. (ii) $\omega\colon k^\times\to\mathcal O^\times$ is an injective homomorphism with image $\mu_{q-1}(K)$, and
reduction $\mu_{q-1}(K)\to k^\times$ is an isomorphism; $\omega(0)=0$; $\omega$ is multiplicative but not additive. (iii)
$\mathcal O^\times=\mu_{q-1}(K)\times U^{(1)}$, $U^{(1)}=1+\mathfrak m$, the projection to the first factor being $u\mapsto\omega(\bar u)$.
Examples: in $\Z_5$, $\omega(2)\equiv182$, $\omega(3)\equiv443$, $\omega(4)\equiv624\equiv-1\pmod{5^4}$. Reference: Serre, Local
Fields, Ch. II, Section 4; Serre, Course in Arithmetic, Ch. II, Section 3. Paper: Lemma lem:tamfactor (the class of the
unit part $u$ depends only on $\bar u$; important_notes.md point 31), background.

### 2.5 `thm:local:units-structure` (theorem) P
(i) For $p$ odd: $\Z_p^\times=\mu_{p-1}\times(1+p\Z_p)$; the series $\log(1+x)=\sum_{n\ge1}(-1)^{n+1}x^n/n$ and $\exp(x)=\sum x^n/n!$ converge on
$p\Z_p$ and give mutually inverse isomorphisms of topological groups $1+p\Z_p\simeq p\Z_p$, carrying $1+p^n\Z_p$ onto $p^n\Z_p$
for $n\ge1$; hence $1+p\Z_p\simeq\Z_p$, topologically generated by $1+p$, and
$$\Q_p^\times\simeq p^{\Z}\times\mu_{p-1}\times(1+p\Z_p)\simeq\Z\times\Z/(p-1)\times\Z_p .$$
(ii) For $p=2$: $\Z_2^\times=\{\pm1\}\times(1+4\Z_2)$, $\log$ and $\exp$ give $1+4\Z_2\simeq4\Z_2$, $1+4\Z_2\simeq\Z_2$ generated by $5$, and
$\Q_2^\times\simeq\Z\times\Z/2\times\Z_2$. (iii) These are the limits of the finite statements of Chapter 2 (5.3, 5.4: $(\Z/p^k)^\times$
cyclic for $p$ odd, $\{\pm1\}\times\langle5\rangle$ for $p=2$). (iv) (For a finite extension $K$ with residue field $\F_q$; stated
in the form used.) $K^\times=\varpi_K^{\Z}\times\mu_{q-1}(K)\times U^{(1)}_K$ and $U^{(1)}_K$ is a $\Z_p$-module, finitely generated; in
particular it is uniquely $m$-divisible for every $m$ prime to $p$. Reference: Serre, Course in Arithmetic, Ch. II,
Section 3 (cite the section); Neukirch II.5. Paper: background (Lemma lem:tamfactor uses only (iv) for $m=\ell^k$, through
2.7).

### 2.6 `cor:local:roots-of-unity` (corollary) P
$\mu(\Q_p)=\mu_{p-1}$ for $p$ odd and $\mu(\Q_2)=\{\pm1\}$. For $m$ prime to $p$: $\mu_m(\Q_p)=\mu_{\gcd(m,p-1)}$; in particular for a
prime $\ell\ne p$, $\mu_{\ell^k}\subset\Q_p$ iff $\ell^k\mid p-1$, and $\#\mu_{\ell^\infty}(\Q_p)=\ell^{v_\ell(p-1)}$. More generally
$\mu_{m}(K)=\mu_{\gcd(m,q-1)}(K)$ for $p\nmid m$ ($q=\#k_K$). $\mu_{p^n}\subset\Q_p$ only for $p^n=2$ (and $p^n=1$). Reference: as 2.5.
Paper: Lemma lem:tamfactor ($\Z_\ell(1)^{G/I}$, "$\Z_\ell(1)/(q-1)\simeq\Z/\ell^{v_\ell(q-1)}$"), background for Chapter 17.

### 2.7 `thm:local:powers` (theorem; $\ell$-th powers in $\Q_p^\times$ for $\ell\ne p$) P
Let $\ell\ne p$ be primes and $k\ge1$; $K$ finite over $\Q_p$ with residue field $\F_q$ and uniformiser $\varpi$ (for $K=\Q_p$:
$q=p$, $\varpi=p$). (i) $U^{(1)}_K=1+\mathfrak m_K$ is uniquely $\ell^k$-divisible (2.1(b) with $f=X^{\ell^k}-u$, $a_0=1$, $f'(1)=\ell^k$ a unit;
or 2.5). (ii) $u\in\mathcal O_K^\times$ is an $\ell^k$-th power in $K$ iff its reduction $\bar u$ is an $\ell^k$-th power in $\F_q^\times$
(2.4(iii) and (i)); by Chapter 2, 7.1, iff $\bar u^{(q-1)/\gcd(\ell^k,q-1)}=1$. (iii) $x=\varpi^au\in K^\times$ is an $\ell^k$-th power iff
$\ell^k\mid a$ and $\bar u\in(\F_q^\times)^{\ell^k}$. (iv) Hence
$$K^\times/(K^\times)^{\ell^k}\ \simeq\ \Z/\ell^k\times\F_q^\times/(\F_q^\times)^{\ell^k}\ \simeq\ \Z/\ell^k\times\Z/\ell^{\min(k,v_\ell(q-1))},$$
the first factor by $v_K$ (canonical), the splitting by the choice of $\varpi$, the second isomorphism by a choice of
generator of $\F_q^\times$. In particular $\#K^\times/(K^\times)^{\ell^k}=\ell^k\cdot\#\mu_{\ell^k}(K)$ (a first instance of the local Euler
characteristic formula, Chapter 17). (v) Passing to the limit: $\widehat{K^\times}:=\varprojlim_kK^\times/(K^\times)^{\ell^k}$ sits in a canonical
exact sequence $0\to\F_q^\times\otimes\Z_\ell\to\widehat{K^\times}\xrightarrow{v_K}\Z_\ell\to0$, split by $\varpi$, so
$\widehat{K^\times}\simeq\Z_\ell\times\Z/\ell^{v_\ell(q-1)}$; and $\F_q^\times\otimes\Z_\ell\simeq\F_q^\times/(\F_q^\times)^{\ell^{v_\ell(q-1)}}\simeq\mu_{\ell^{v_\ell(q-1)}}(\F_q)$
(Chapter 2, 7.2; Chapter 5, galois:kummer-finite-field). (vi) (The case $\ell=2$, $p$ odd, written out.) $\Q_p^\times/(\Q_p^\times)^2$ has
order $4$, with representatives $1,u_0,p,u_0p$, $u_0$ a non-square unit; $\Q_2^\times/(\Q_2^\times)^2$ has order $8$, representatives
$\pm1,\pm5,\pm2,\pm10$ (by 2.3(e)). Reference: Serre, Course in Arithmetic, Ch. II, Section 3 (squares); elementary from
2.1 to 2.5 otherwise. Paper: Lemma lem:tamfactor ("$H^1(G,\Z_\ell(1))=\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}$", "$c$ the class of $u$", "$u$
is an $\ell^k$-th power in $\F_q^\times$" read as the reduction, important_notes.md point 31), Lemma lem:tamagawa-exp
(via 6.2), Section sec:tam.

### 2.8 `ex:local:powers-examples` (worked examples) P
(a) $\Q_7^\times/(\Q_7^\times)^3\simeq\Z/3\times\Z/3$; the unit cubes reduce to $\{1,6\}$ mod $7$: $-1$ and $6$ are cubes in $\Q_7$; $2$ is
not; $14$ is not ($v_7=1$); $7^3\cdot6$ is. (b) $\Q_{19}^\times/(\Q_{19}^\times)^9\simeq\Z/9\times\Z/9$, $v_3(18)=2$; the classes of $2,8,-1$
have $v_3(c)=0,1,2$ (Chapter 2, 7.3(b), now read in $\Z_{19}^\times$). (c) $\Q_{11}^\times/(\Q_{11}^\times)^5\simeq\Z/5\times\Z/5$; the unit fifth
powers reduce to $\{\pm1\}$ mod $11$. For 11a1 the Tate parameter at $11$ has $v_{11}(q_E)=5$ and unit part $u\equiv-1\pmod{11}$ (from
$j=-2^{12}31^3/11^5$ and $q_E=j^{-1}+744j^{-2}+\dots$; Chapter 10 for the Tate parameter), so $q_E\in(\Q_{11}^\times)^5$: both the
valuation and the unit part are fifth powers. (d) $\Q_5^\times/(\Q_5^\times)^3\simeq\Z/3$: every unit of $\Z_5$ is a cube. Paper: Lemma
lem:tamfactor and Section sec:tam (the extra term $\min(v_\ell(n),v_\ell(q-1),v_\ell(c))$), Chapter 16, Exercise 10 (11a1 at $\ell=5$).

## 3. Line-up, Section 3: finite extensions of $\Q_p$

### 3.1 `thm:local:extension-absval` (theorem) P (existence via 2.2; equivalence of norms S)
Let $K$ be complete for a nonarchimedean absolute value (in practice $\Q_p$ or a finite extension) and $L/K$ an algebraic
extension. Then $|\cdot|$ extends uniquely to an absolute value on $L$; for $[L:K]=n<\infty$ it is
$$|x|_L=|N_{L/K}(x)|^{1/n},$$
$L$ is complete, and $\mathcal O_L=\{|x|\le1\}$ is the integral closure of $\mathcal O_K$ in $L$. Uniqueness uses that all norms on a
finite-dimensional vector space over a complete field are equivalent (S). Consequences: $\sigma\in\Aut(L/K)$ is an isometry;
conjugate elements have the same absolute value; $\Qbar_p$ carries a unique absolute value extending $|\cdot|_p$ (not
complete; its completion $\C_p$ is mentioned only). Reference: Neukirch II.4 and II.6 (cite the sections); Serre, Local
Fields, Ch. II, Section 2. Paper: background.

### 3.2 `thm:local:ef` (definition and theorem) P
For $L/K$ finite of degree $n$ (both complete, discretely valued, finite residue fields): the *ramification index*
$e=e(L/K)=[|L^\times|:|K^\times|]=v_L(\varpi_K)$ and the *residue degree* $f=f(L/K)=[k_L:k_K]$ satisfy $ef=n$; $\mathcal O_L$ is free of
rank $n$ over $\mathcal O_K$ with basis $\{\alpha_i\varpi_L^j:1\le i\le f,\ 0\le j<e\}$ ($\alpha_i$ lifting a basis of $k_L/k_K$); $e$ and $f$
are multiplicative in towers. Terminology: $L/K$ is *unramified* if $e=1$, *totally ramified* if $f=1$, *tamely ramified* if
$p\nmid e$, *wildly ramified* if $p\mid e$ ($p$ the residue characteristic). (Residue fields are finite, hence perfect, so
no separability condition is needed.) Comparison with Chapter 6, 3.1: one prime above, $g=1$. Reference: Neukirch II.6;
Serre, Local Fields, Ch. I, Section 4 and Ch. II, Section 2. Paper: background.

### 3.3 `thm:local:eisenstein` (theorem and examples) P
$L/K$ is totally ramified of degree $e$ iff $L=K(\pi)$ with $\pi$ a root of an Eisenstein polynomial of degree $e$ over $\mathcal O_K$;
then $\pi$ is a uniformiser of $L$ and $\mathcal O_L=\mathcal O_K[\pi]$. Conversely the minimal polynomial of any uniformiser of a
totally ramified $L$ is Eisenstein. Examples (all proved): (a) $\Q_p(\zeta_{p^n})$: $\Phi_{p^n}(X+1)$ is Eisenstein, so the extension is
totally ramified of degree $\varphi(p^n)$, uniformiser $1-\zeta_{p^n}$, ring of integers $\Z_p[\zeta_{p^n}]$, and
$\Gal(\Q_p(\zeta_{p^n})/\Q_p)\simeq(\Z/p^n)^\times$ is all inertia. (b) $\Q_3(\zeta_3)=\Q_3(\sqrt{-3})$, totally ramified quadratic, tame
($3\nmid2$), with ring of integers $\Z_3[\zeta_3]$ and uniformiser $\pi=1-\zeta_3$, $\pi^2=-3\zeta_3$: this is the local meaning of
Chapter 6, 4.7, and $\Z_3[\zeta_3]$ is the $\pi$-adic completion of $\Z[\zeta_3]$ (by 3.4). (c) $\Q_p(p^{1/m})$, $X^m-p$ Eisenstein:
totally ramified of degree $m$. (d) $\Q_p(\sqrt{p^*})$, $p$ odd, $p^*=(-1)^{(p-1)/2}p$: totally ramified quadratic (6.3). Reference:
Serre, Local Fields, Ch. I, Section 6; Neukirch II.5. Paper: Lemma lem:IV ("$\Z_3[\zeta_3]$, a discrete valuation ring with
uniformiser $\pi=1-\zeta_3$ and residue field $\F_3$", now as the ring of integers of $\Q_3(\sqrt{-3})$), Lemma lem:twist ($\Q_q(\sqrt{q^*})$).

### 3.4 `thm:local:completion-numberfield` (theorem) P
Let $F$ be a number field and $p$ a prime with $p\mathcal O_F=\prod_{\mathfrak p\mid p}\mathfrak p^{e_{\mathfrak p}}$, residue degrees $f_{\mathfrak p}$ (Chapter 6,
3.1). (i) The absolute values of $F$ extending $|\cdot|_p$ are exactly the maps $x\mapsto p^{-v_{\mathfrak p}(x)/e_{\mathfrak p}}$, one for each
$\mathfrak p\mid p$ (distinct primes give inequivalent absolute values). (ii) The completion $F_{\mathfrak p}$ is a finite extension of $\Q_p$ with $e(F_{\mathfrak p}/\Q_p)=e_{\mathfrak p}$,
$f(F_{\mathfrak p}/\Q_p)=f_{\mathfrak p}$, and $\mathcal O_{F_{\mathfrak p}}=\varprojlim_n\mathcal O_F/\mathfrak p^n$. (iii) $F\otimes_\Q\Q_p\simeq\prod_{\mathfrak p\mid p}F_{\mathfrak p}$ and
$\mathcal O_F\otimes_\Z\Z_p\simeq\prod_{\mathfrak p\mid p}\mathcal O_{F_{\mathfrak p}}$, hence $\sum_{\mathfrak p}e_{\mathfrak p}f_{\mathfrak p}=[F:\Q]$. (Proof of (iii): write $F=\Q(\theta)$,
factor the minimal polynomial over $\Q_p$, CRT; or: $\mathcal O_F\otimes\Z_p=\varprojlim\mathcal O_F/p^n$ and CRT for $p^n\mathcal O_F=\prod\mathfrak p^{ne_{\mathfrak p}}$.)
This is the result Chapter 6, 7.4 states and defers here. Examples: $\Z[\zeta_3]\otimes\Z_3=\Z_3[\zeta_3]$ (ramified), $\Z[\zeta_3]\otimes\Z_7\simeq
\Z_7\times\Z_7$ (split), $\Z[\zeta_3]\otimes\Z_2$ the unramified quadratic extension's ring of integers (inert); the coefficient ring
$\mathcal O_\lambda$ of a newform (Chapters 13, 15). Reference: Neukirch II.8 (cite the section); Serre, Local Fields, Ch. II,
Section 3. Paper: Lemma lem:crit and Lemma lem:old ("the same statements hold with $\Z$ replaced by $\Z_\ell$", primes $\lambda\mid\ell$),
Lemma lem:ddt417 ($\mathcal O$ a DVR), Lemma lem:IV, Lemma lem:euler.

### 3.5 `prop:local:decomposition` (proposition) S
(i) Let $L/F$ be a finite Galois extension of number fields, $\mathfrak P\mid\mathfrak p$. Restriction identifies $\Gal(L_{\mathfrak P}/F_{\mathfrak p})$ with
the decomposition group $D_{\mathfrak P}$, and its inertia subgroup (3.2 and 5.1) with $I_{\mathfrak P}$ (Chapter 6, 3.5). (ii) An embedding
$\iota\colon\Qbar\to\Qbar_p$ induces $G_{\Q_p}\to G_\Q$, $\sigma\mapsto\iota^{-1}\sigma\iota$; it is injective (because $\iota(\Qbar)$ is dense in $\Qbar_p$, by
Krasner's lemma, stated) with image the decomposition group $D_{\bar{\mathfrak P}}$ of the prime $\bar{\mathfrak P}$ of $\bar\Z$ determined
by $\iota$, and it carries $I_p$ onto $I_{\bar{\mathfrak P}}$ and arithmetic Frobenius lifts to Frobenius elements (Chapter 6, 3.10(v),
which states this and defers it here). Changing $\iota$ conjugates the image. (iii) Hence for a representation $\rho$ of
$G_\Q$, "$\rho|_{G_{\Q_p}}$", "$\rho(I_p)$", "$V^{I_p}$" and "$\rho(\Frob_p)$ for $\rho$ unramified at $p$" are well defined up to
conjugation. Reference: Neukirch II.8 and II.9 (cite the sections); Serre, Local Fields, Ch. II, Section 3. Paper: Section
1.1 ($I_p$, $\delta_p=\dim V^{I_p}$), Lemmas lem:tamagawa-exp, lem:tamfactor, lem:euler (all local arguments at $q$).

### 3.6 `prop:local:tame-totally-ramified` (proposition) P
Let $L/K$ be totally ramified of degree $e$ with $p\nmid e$. Then $L=K(\alpha)$ with $\alpha^e=\varpi$ for some uniformiser $\varpi$ of $K$.
$L/K$ is Galois iff $\mu_e\subset K$ (iff $e\mid q-1$), and then $\Gal(L/K)\simeq\mu_e$ via $\sigma\mapsto\sigma(\alpha)/\alpha$, cyclic. Proof:
$\pi_L^e=\varpi_Kw$ with $w\in\mathcal O_L^\times$; as $k_L=k_K$, $w=w_0w_1$ with $w_0\in\mathcal O_K^\times$ and $w_1\in1+\mathfrak m_L$, and $w_1$ is an
$e$-th power by 2.7(i); so $(\pi_Lw_1^{-1/e})^e=\varpi_Kw_0$ is a uniformiser of $K$. Galois criterion: the conjugates of $\alpha$ are
$\zeta\alpha$, $\zeta\in\mu_e$, and $\mu_e\subset L$ forces $\mu_e\subset K$ by 2.4 since $k_L=k_K$. Reference: Serre, Local Fields, Ch. IV,
Section 2 (cite the section); Neukirch II.7. Paper: background for 5.2 (the tame extensions of $\Q_p^{\mathrm{ur}}$).

## 4. Line-up, Section 4: unramified extensions, $\Q_p^{\mathrm{ur}}$ and Frobenius

### 4.1 `thm:local:unramified` (theorem) P
Let $K$ be finite over $\Q_p$ with residue field $\F_q$. (i) For each $f\ge1$ there is, inside $\Qbar_p$, exactly one unramified
extension $K_f/K$ of degree $f$, namely $K_f=K(\mu_{q^f-1})$. (ii) $K_f/K$ is Galois and reduction gives an isomorphism
$\Gal(K_f/K)\to\Gal(\F_{q^f}/\F_q)$; so $\Gal(K_f/K)$ is cyclic of order $f$, generated by the unique $\Frob_{K_f/K}$ with
$\Frob(x)\equiv x^q\pmod{\mathfrak m}$ for $x\in\mathcal O_{K_f}$ (arithmetic Frobenius; on $\mu_{q^f-1}$ it is $\zeta\mapsto\zeta^q$). (iii) A finite
$L/K$ is unramified iff $L\subseteq K_f$ for some $f$; composita and subextensions of unramified extensions are unramified;
every finite $L/K$ has a maximal unramified subextension $L_0$, with $[L_0:K]=f(L/K)$ and $L/L_0$ totally ramified. (iv) If
$L/K$ is unramified and $\alpha\in\mathcal O_L$ reduces to a generator of $k_L/k_K$, then $L=K(\alpha)$ (Hensel). Proof: lift the
irreducible polynomial of a generator of $\F_{q^f}^\times$ (Hensel for the simple root), Teichmuller (2.4). Reference: Serre,
Local Fields, Ch. III, Section 5; Neukirch II.7. Paper: Lemma lem:tamagawa-exp and Lemma lem:tamfactor ("the unramified
quadratic extension of $\Q_q$").

### 4.2 `def:local:qpur` (definition and proposition) P
$K^{\mathrm{ur}}=\bigcup_fK_f=K(\mu_m:p\nmid m)$. (i) Its residue field is $\bar\F_q$; restriction gives
$\Gal(K^{\mathrm{ur}}/K)\simeq\Gal(\bar\F_q/\F_q)\simeq\hat\Z$, topologically generated by the arithmetic Frobenius (Chapter 5,
galois:finite-field-galois and the profinite theory). (ii) The valuation of $K^{\mathrm{ur}}$ is discrete with the same value group
as $K$ (each $K_f$ is unramified), $\varpi_K$ is a uniformiser, but $K^{\mathrm{ur}}$ is not complete. (iii) Hensel's lemma holds for
$\mathcal O_{K^{\mathrm{ur}}}$ (a polynomial and an approximate root live in some complete $\mathcal O_{K_f}$, and the root found there lies
in $K^{\mathrm{ur}}$). (iv) For every $m$ prime to $p$: $\mu_m\subset K^{\mathrm{ur}}$, every unit of $\mathcal O_{K^{\mathrm{ur}}}$ is an $m$-th power in
$K^{\mathrm{ur}}$ (because $\bar\F_q^\times$ is $m$-divisible, then (iii)), and $x\in(K^{\mathrm{ur}})^\times$ is an $m$-th power iff $m\mid v_K(x)$. In
particular $\mu_{\ell^\infty}\subset\Q_q^{\mathrm{ur}}$ for $\ell\ne q$. Reference: Serre, Local Fields, Ch. III, Section 5; Neukirch II.7 and
II.9. Paper: Lemma lem:tamagawa-exp ("$\ell^t$-th power in $\Q_q^{\mathrm{ur}}$"; the units of its valuation ring are $\ell^t$-th powers:
important_notes.md point 8), Lemma lem:tamfactor ($G/I$, Kummer theory over $\Q_q^{\mathrm{ur}}$); Chapter 5's paperlink for
galois:kummer-character.

### 4.3 `conv:local:frobenius` (convention, with a dictionary) P
Convention L3 in a `convention` environment, with the dictionary: (a) $\Frob$ acts on $\mu_m$ ($p\nmid m$) by $\zeta\mapsto\zeta^q$,
$\chi_\ell(\Frob)=q$, $\chi_\ell(\Phi)=q^{-1}$; (b) $\Frob$ is defined modulo $I_K$ and up to conjugation in $G_K$; any statement
about $\rho(\Frob)$ for $\rho$ ramified must be checked to be independent of the lift (as in 5.6 and 6.2(iii)); (c) the
arithmetic eigenvalues $\lambda$ correspond to geometric eigenvalues $\lambda^{-1}$; when the multiset of eigenvalues on the
relevant space is stable under inversion ($\ad V$ at a good prime, the lines with eigenvalue $\pm1$) the two conventions
give the same $L$-factor, otherwise they do not (the Steinberg case, 9.3); (d) the paper uses the arithmetic $\Frob$ in Lemma
lem:tamfactor ("$\Frob^{-1}t\Frob=t^{q^{-1}}$", $\rho(\Frob)=\begin{psmallmatrix}\varepsilon q&c'\\0&\varepsilon\end{psmallmatrix}$) and the
geometric one, without saying so, in Section 1.1, Lemma lem:euler and Lemma lem:fpr (important_notes.md point 11). Reference:
Deligne73 Section 2; Tate79 Section 4 (add both to `bib/ch07.bib`). Paper: as in (d).

### 4.4 `prop:local:unram-basechange` (proposition) P
Let $K/\Q_p$ be a finite unramified extension of degree $f$. Then $K^{\mathrm{ur}}=\Q_p^{\mathrm{ur}}$, hence $I_K=I_{\Q_p}$ and $P_K=P_{\Q_p}$ as
subgroups of $G_K\subseteq G_{\Q_p}$; the tame characters agree (5.3: $p$ is a uniformiser of both); $\Frob_K=\Frob_{\Q_p}^f$ modulo $I$.
Consequently, for a representation $\rho$ of $G_{\Q_p}$: $\rho(I_p)$, $V^{I_p}$, tame or wild ramification, the Swan and Artin
conductors (8.3, 8.4) and the monodromy operator $N$ (7.2) are unchanged by restriction to $G_K$. More generally (stated) for
any finite $K/\Q_p$, $I_K=I_{\Q_p}\cap G_K$ is open of index $e(K/\Q_p)$ in $I_{\Q_p}$. (Translation theorem, Chapter 5,
galois:translation-theorem.) Paper: Lemma lem:tamagawa-exp and Lemma lem:tamfactor ("over the unramified quadratic
extension of $\Q_q$ (which does not change the inertia group)"), Lemma lem:twist (i) ("invariant under unramified base
change"; the field-theoretic half).

### 4.5 `prop:local:cyclotomic-local` (proposition) P
(i) For $\ell\ne p$: $\Q_p(\mu_{\ell^k})/\Q_p$ is unramified of degree the order of $p$ in $(\Z/\ell^k)^\times$ (Chapter 2, 5.4(iv) for the
$\ell$-adic valuations), and $\Frob$ acts on $\mu_{\ell^\infty}$ by $\zeta\mapsto\zeta^p$: $\chi_\ell|_{G_{\Q_p}}$ is unramified with
$\chi_\ell(\Frob)=p$. (ii) For $\ell=p$: $\Q_p(\mu_{p^n})/\Q_p$ is totally ramified with group $(\Z/p^n)^\times$ (3.3(a)), so $\chi_p(I_p)=\Z_p^\times$,
and $\Q_p(\mu_{p^\infty})\cap\Q_p^{\mathrm{ur}}=\Q_p$. (iii) Global consequence (with 3.5): for $p\ne\ell$, $\chi_\ell(\Frob_p)=p$ (Chapter 5, C4;
Chapter 6, 5.2). Reference: Serre, Local Fields, Ch. IV, Section 4; Washington Ch. 2. Paper: Lemma lem:tamfactor
($\chi_\ell\varepsilon$ on the diagonal, $\chi_\ell(\Frob)=q$), Lemma lem:old ($\bar\chi_\ell$), background.

## 5. Line-up, Section 5: ramification groups, inertia, wild inertia, the tame quotient

### 5.1 `def:local:ramgroups` (definition and proposition) S (P for (i), (ii), (iii))
Let $L/K$ be finite Galois with group $G$, $\pi_L$ a uniformiser of $L$. For $i\ge-1$ the *lower ramification groups* are
$G_i=\{\sigma\in G:v_L(\sigma(x)-x)\ge i+1\text{ for all }x\in\mathcal O_L\}$. (i) $G_{-1}=G$, $G_0=I(L/K)$ is the kernel of $G\to\Gal(k_L/k_K)$
(so $\#G_0=e$), the $G_i$ are normal in $G$ and decreasing, and $G_i=1$ for $i\gg0$; if $\mathcal O_L=\mathcal O_K[\pi_L]$ (e.g. $L/K$ totally
ramified), $\sigma\in G_i$ iff $v_L(\sigma(\pi_L)-\pi_L)\ge i+1$. (ii) $\sigma\mapsto\sigma(\pi_L)/\pi_L\bmod\mathfrak m_L$ is an injective homomorphism
$G_0/G_1\to k_L^\times$, independent of $\pi_L$; so $G_0/G_1$ is cyclic of order prime to $p$. (iii) For $i\ge1$, $\sigma\mapsto\sigma(\pi_L)/\pi_L-1$
induces an injective homomorphism $G_i/G_{i+1}\to\mathfrak m_L^i/\mathfrak m_L^{i+1}\simeq(k_L,+)$; so $G_1$ is a $p$-group, the *wild
inertia group* $P(L/K)$, the unique Sylow $p$-subgroup of $G_0$; $L/K$ is tamely ramified iff $G_1=1$. (iv) (Stated.) Herbrand's
function $\varphi_{L/K}(u)=\int_0^u dt/[G_0:G_t]$ defines the *upper numbering* $G^{\varphi(u)}=G_u$; upper numbering is compatible
with quotients ($(G/H)^v=G^vH/H$, Herbrand); for $G$ abelian the jumps of the upper filtration are integers (Hasse-Arf). (v)
Examples (proved): $\Q_2(i)/\Q_2$, $\pi=1+i$: $\sigma(\pi)-\pi=-2i$, $v_L=2$, so $G_0=G_1=G$, $G_2=1$; $\Q_2(\sqrt2)/\Q_2$, $\pi=\sqrt2$:
$v_L(-2\sqrt2)=3$, so $G_0=G_1=G_2=G$, $G_3=1$; $\Q_3(\sqrt{-3})/\Q_3$ and $\Q_p(\sqrt p)/\Q_p$ ($p$ odd), $\Q_p(\zeta_p)/\Q_p$: tame, $G_1=1$.
Reference: Serre, Local Fields, Ch. IV, Sections 1 to 3 (cite the sections; the injections are its Propositions 7 and 9
of Section 2 only if the writer checks the numbers); Neukirch II.10. Paper: Remark rem:wild, Section sec:wild (wild
primes $2$, $3$), background for 8.3.

### 5.2 `thm:local:inertia-structure` (theorem) S (P for (i), (iii))
Let $G=G_K$. (i) $I_K=\Gal(\Qbar_p/K^{\mathrm{ur}})$ is a closed normal subgroup with $G/I_K\simeq\Gal(\bar k_K/k_K)\simeq\hat\Z$ (4.2), and for
every finite Galois $L/K$ the image of $I_K$ in $\Gal(L/K)$ is $I(L/K)=G_0$. (ii) $P_K$, the closure of the union of the images
of the wild inertia groups (equivalently $\Gal(\Qbar_p/K^{\mathrm{tame}})$, $K^{\mathrm{tame}}$ the union of the finite tamely ramified extensions of
$K$), is a normal pro-$p$ subgroup of $G$, and it is the unique pro-$p$ Sylow subgroup of $I_K$. (iii) $K^{\mathrm{tame}}=\bigcup_{p\nmid m}K^{\mathrm{ur}}(\varpi^{1/m})$
for any uniformiser $\varpi$ of $K$: every finite tamely ramified extension of $K^{\mathrm{ur}}$ is $K^{\mathrm{ur}}(\varpi^{1/m})$ for some $m$ prime to
$p$ (by 3.6 at a finite level, and $\varpi u$ with $u\in\mathcal O_{K^{\mathrm{ur}}}^\times$ an $m$-th power by 4.2(iv)), and these are Galois over
$K^{\mathrm{ur}}$ because $\mu_m\subset K^{\mathrm{ur}}$. (iv) (The filtration of $G_{\Q_p}$, stated.) $G_K\supset I_K\supset P_K\supset\{1\}$ is the start of
the upper ramification filtration $G_K^u$ ($u\ge-1$): $G_K^{-1}=G_K$, $G_K^0=I_K$, $\overline{\bigcup_{u>0}G_K^u}=P_K$; upper numbering is
defined on $G_K$ by passing to the limit (possible by (iv) of 5.1). Reference: Serre, Local Fields, Ch. IV; Neukirch II.9;
Serre, Abelian l-adic representations, Ch. I (cite chapters). Paper: Lemma lem:tamfactor ("the kernel of $I\to\langle t\rangle$ has
trivial pro-$\ell$ quotient"), Remark rem:wild, Section 1.1 ($I_p$).

### 5.3 `thm:local:tame-character` (theorem and definition) P
Let $m$ be prime to $p$ and $\varpi$ a uniformiser of $K$. (i) $\theta_m\colon I_K\to\mu_m$, $\sigma\mapsto\sigma(\varpi^{1/m})/\varpi^{1/m}$, is a
continuous surjective homomorphism, independent of the choice of the root $\varpi^{1/m}$ and of the uniformiser $\varpi$ (for
$\varpi'=u\varpi$, $u^{1/m}\in K^{\mathrm{ur}}$ is fixed by $I_K$), and of replacing $K$ by an unramified extension (4.4). (ii) $\theta_{mm'}^{m'}=\theta_m$;
the limit $\theta\colon I_K\to\varprojlim_{p\nmid m}\mu_m=\prod_{\ell\ne p}\Z_\ell(1)$ is surjective with kernel $P_K$:
$$I_K/P_K\ \simeq\ \prod_{\ell\ne p}\Z_\ell(1),$$
procyclic, abelian, of supernatural order prime to $p$ (it has no quotient of order $p$). (iii) For $\ell\ne p$ the
$\ell$-component $t_\ell\colon I_K\to\Z_\ell(1)$, $\sigma\mapsto\bigl(\sigma(\varpi^{1/\ell^k})/\varpi^{1/\ell^k}\bigr)_k$ (for a compatible system of roots), is the
**tame character**; it is surjective, its kernel is an extension of $\prod_{\ell'\ne\ell,p}\Z_{\ell'}(1)$ by $P_K$, of supernatural order
prime to $\ell$, and $t_\ell$ identifies the maximal pro-$\ell$ quotient $I_K^{(\ell)}$ of $I_K$ with $\Z_\ell(1)$; a topological generator
$t$ of $I_K^{(\ell)}$ is "a generator of tame inertia" in the paper's sense. (iv) Consequently every continuous homomorphism
from $I_K$ to a pro-$\ell$ group (for example to $1+\ell M_n(\Z_\ell)$, or to a group of unipotent matrices over $\Z_\ell$) factors
through $t_\ell$. Reference: Serre, Local Fields, Ch. IV, Section 2 (cite the section); Neukirch II.9; Serre-Tate68,
Section 1 (add to `bib/ch07.bib`). Paper: Lemma lem:tamfactor ("$I$ acts through its maximal pro-$\ell$ tame quotient,
generated by an element $t$", "the kernel of $I\to\langle t\rangle$ has trivial pro-$\ell$ quotient", "the tame character"); Chapter 16
(tame-inertia-example, model-setting), which imports exactly (ii) to (iv).

### 5.4 `thm:local:tame-relation` (theorem) P
(i) For $\tau\in G_K$ and $\sigma\in I_K$: $t_\ell(\tau\sigma\tau^{-1})=\tau\cdot t_\ell(\sigma)=\chi_\ell(\tau)\,t_\ell(\sigma)$ (the Galois action on $\Z_\ell(1)$), and
likewise $\theta(\tau\sigma\tau^{-1})=\tau(\theta(\sigma))$. (Proof: $\tau^{-1}(\varpi^{1/m})=\zeta_\tau\varpi^{1/m}$ with $\zeta_\tau\in\mu_m$; $\sigma\in I_K$
fixes $\mu_m$; apply $\tau$.) (ii) Hence for every arithmetic Frobenius lift $\Frob\in G_K$ and every $t\in I_K/P_K$:
$$\Frob\,t\,\Frob^{-1}=t^{q},\qquad\text{equivalently}\qquad\Frob^{-1}\,t\,\Frob=t^{q^{-1}},$$
where $q^{-1}$ is the inverse of $q$ in $\prod_{\ell\ne p}\Z_\ell$, the ring of exponents of the procyclic group $I_K/P_K$; for the
geometric Frobenius, $\Phi\,t\,\Phi^{-1}=t^{q^{-1}}$. The same holds in the maximal pro-$\ell$ quotient $I_K^{(\ell)}=\Z_\ell(1)$ with
$q^{-1}\in\Z_\ell$, and modulo $\ker t_\ell$ in $G_K/\ker t_\ell$. (iii) (Structure, S.) $\Gal(K^{\mathrm{tame}}/K)\simeq\bigl(\prod_{\ell\ne p}\Z_\ell(1)\bigr)\rtimes\hat\Z$, the
generator $1\in\hat\Z$ acting by multiplication by $q$; the extension splits (choose $\Frob$ fixing all $\varpi^{1/m}$, 5.5); it is
topologically generated by $t$ and $\Frob$ subject to $\Frob\,t\,\Frob^{-1}=t^q$ (stated; Iwasawa). This is Chapter 6, 3.11 in
profinite form and the foretaste in Chapter 1 (its semidirect-product item). Reference: Serre, Local Fields, Ch. IV, Section 2;
Neukirch II.9 (cite the section); NSW, Ch. VII, Section 5 (structure, stated). Paper: Lemma lem:tamfactor
("$\Frob^{-1}t\Frob=t^{q^{-1}}$" with the arithmetic Frobenius), Lemma lem:euler ("Frobenius centralises $\sigma$ if $q\equiv1\pmod3$
and inverts it if $q\equiv2$"), Chapter 16 (frobenius-on-h1-inertia).

### 5.5 `cor:local:frob-fixing-roots` (corollary) P
Let $\varpi$ be a uniformiser of $K$ and $(\varpi^{1/m})_{p\nmid m}$ a compatible system of roots. There is an arithmetic Frobenius lift
$\Frob\in G_K$ fixing every $\varpi^{1/m}$, hence fixing the field $K_\varpi=K(\varpi^{1/m}:p\nmid m)$; two such lifts differ by an element of
$G_{K_\varpi}\cap I_K$, which lies in $\ker t_\ell$ for every $\ell$. Proof: $K_\varpi/K$ is totally ramified (each $K(\varpi^{1/m})$ is, by
Eisenstein), so $K_\varpi\cap K^{\mathrm{ur}}=K$, and by the translation theorem (Chapter 5) restriction $G_{K_\varpi}\to\Gal(K^{\mathrm{ur}}/K)$ is
surjective. For $K=\Q_q$, $\varpi=q$: a Frobenius fixing all $\ell$-power roots of $q$, so that the Kummer cocycle $\kappa_q$ of 6.2
vanishes on it. Paper: Lemma lem:tamfactor (the correct reading of "$c'$ is the image of $\kappa$", important_notes.md point 7).

### 5.6 `cor:local:finite-tame-image` (corollary) P
Let $H$ be a group and $\rho\colon G_K\to H$ a homomorphism with $\rho(I_K)$ finite of order prime to $p$ (for example
$\rho\colon G_K\to\GL_n(\Q_\ell)$ continuous with finite image of inertia of order prime to $p$). Then $\rho(P_K)=1$, $\rho|_{I_K}$
factors through the procyclic $I_K/P_K$, so $\rho(I_K)$ is cyclic, generated by $\rho(t)$ for a topological generator $t$ of
$I_K/P_K$, and $\rho(\Frob)\,h\,\rho(\Frob)^{-1}=h^q$ for all $h\in\rho(I_K)$, for every Frobenius lift; the statement does not depend on the
lift ($\rho(I_K)$ is abelian). In particular if $\rho(I_K)=\langle g\rangle$ has order $m$: $\rho(\Frob)$ commutes with $g$ iff $q\equiv1\pmod m$, and
inverts it iff $q\equiv-1\pmod m$. Proof: $\rho(P_K)$ is a finite quotient of a pro-$p$ group inside a group of order prime to $p$;
then 5.3 and 5.4. Compare Chapter 6, 3.11 and 3.12 (which prove the same for a finite Galois extension directly).
Reference: Serre, Local Fields, Ch. IV, Section 2. Paper: Lemma lem:IV ("the image is tame since $q\ne3$, hence cyclic"),
Lemma lem:euler (types II, II$^*$, IV, IV$^*$: Frobenius centralises or inverts $\sigma$ by $q\bmod3$; types III, III$^*$: by $q\bmod4$),
Remark rem:types.

### 5.7 `prop:local:wild-image` (proposition) P
Let $\ell\ne p$, $E/\Q_\ell$ finite with ring of integers $\mathcal O$, and $\rho\colon G_K\to\GL_n(\mathcal O)$ continuous. Then $\rho(P_K)$ is a
finite $p$-group, mapping injectively to $\GL_n(\mathcal O/\ell)$ (the kernel $1+\ell M_n(\mathcal O)$ of reduction is pro-$\ell$). Hence:
(i) there is an open subgroup $I_1\subseteq I_K$, normal in $G_K$, on which $\rho$ factors through $t_\ell$ (namely
$I_1=I_K\cap\rho^{-1}(1+\ell^2M_n(\mathcal O))$, or $1+\ell M_n$ for $\ell$ odd); (ii) $\rho$ is tamely ramified ($\rho(P_K)=1$) iff the
image of inertia has no element of order $p$; automatically so if $\rho(I_K)$ is finite of order prime to $p$. Warning: for a
general $\rho$ nothing forbids wild ramification at $p\ge5$ ($\GL_2(\Z_\ell)$ contains elements of order $5$ when $\ell\equiv1\pmod5$). For
$\rho=\rho_{E,\ell}$ with potentially good reduction the characteristic polynomials of $\rho(\sigma)$, $\sigma\in I_K$, have integer
coefficients independent of $\ell$, so $\rho(I_K)$ has order in $\{1,2,3,4,6\}$ for $p\ge5$ and is tame (Serre-Tate68, Kraus90;
proved or stated in Chapters 10, 11, not here).
Examples of wild images at $p=2,3$ (stated; Chapters 10, 11): $Q_8$ and $\SL_2(\F_3)$ at $p=2$; cyclic of order $3$ or $6$ at $p=3$
(wild there, since $I/P$ has no quotient of order $3$). Reference: Serre-Tate68, Section 2; Serre, Local Fields, Ch. IV.
Paper: Remark rem:wild ("At $q=2,3$ the Kodaira type does not determine $L_q(A_f,s)$"), Lemma lem:IV ("tame since
$q\ne3$"), Lemma lem:twist (ii) at $q=3$ (important_notes.md point 28).

### 5.8 `ex:local:tame-explicit` (worked example) P
Let $\ell\ne q$ be primes, $m=\ell^k$, $L=\Q_q(\mu_m,q^{1/m})$. With a primitive $\zeta\in\mu_m$ fixed, $\sigma_{a,b}\colon\zeta\mapsto\zeta^a$,
$q^{1/m}\mapsto\zeta^bq^{1/m}$ identifies $\Gal(L/\Q_q)$ with the subgroup $\{(a,b):a\in\langle q\rangle\subseteq(\Z/m)^\times,\ b\in\Z/m\}$ of the
affine group (Chapter 5, galois:kummer-affine), with $(a,b)(a',b')=(aa',ab'+b)$. The inertia subgroup is $\{a=1\}\simeq\Z/m$,
generated by $t=\sigma_{1,1}$, and $t_\ell\bmod m$ is $\sigma_{1,b}\mapsto\zeta^b$; $\Frob=\sigma_{q,0}$ is a Frobenius fixing $q^{1/m}$ (5.5);
$\Frob\,t\,\Frob^{-1}=\sigma_{1,q}=t^q$ and $\Frob^{-1}t\,\Frob=\sigma_{1,q'}=t^{q'}$ with $qq'\equiv1\pmod m$. (Checked: $(q,\ell,k)=(7,3,2)$ gives
$t^7$ and $t^4$; $(13,3,2)$ gives $t^4$ and $t^7$; $(2,3,2)$ gives $t^2$ and $t^5$.) Paper: Lemma lem:tamfactor (the relation,
at every finite level), Exercise 8.

## 6. Line-up, Section 6: Kummer theory over $\Q_p$, quadratic characters, local class field theory

### 6.1 `prop:local:kummer-qp` (proposition) P for (i), (iii); R for (ii)
Let $K$ be finite over $\Q_p$, $\ell\ne p$ (the statements (i), (ii) hold for any $n$ in characteristic $0$). (i) (Chapter 5,
galois:kummer-character and galois:l-adic-kummer, recalled.) For $x\in K^\times$ and a compatible system $(x^{1/\ell^k})_k$ in $\Qbar_p$, the
Kummer cocycle $\kappa_x\colon G_K\to\Z_\ell(1)$, $\kappa_x(\sigma)=(\sigma(x^{1/\ell^k})/x^{1/\ell^k})_k$, satisfies
$\kappa_x(\sigma\tau)=\kappa_x(\sigma)+\chi_\ell(\sigma)\kappa_x(\tau)$; changing the system changes it by $\sigma\mapsto(\chi_\ell(\sigma)-1)z$; $\kappa_{xy}=\kappa_x+\kappa_y$
for the product systems; $\kappa_x\bmod\ell^k$ vanishes on $G_{K'}$ iff $x\in(K'^\times)^{\ell^k}$, for any $K'\supseteq K(\mu_{\ell^k})$. (ii) (Stated
here, proved in Chapter 17 via Hilbert 90.) The Kummer maps $K^\times/(K^\times)^{\ell^k}\to H^1(K,\mu_{\ell^k})$ and
$\widehat{K^\times}=\varprojlim K^\times/(K^\times)^{\ell^k}\to H^1(K,\Z_\ell(1))$ are isomorphisms. (iii) With 2.7: $H^1(K,\Z_\ell(1))\simeq\Z_\ell\times\Z/\ell^{v_\ell(q-1)}$,
the projection to $\Z_\ell$ being $v_K$ and the torsion being the image of the units, $\F_q^\times\otimes\Z_\ell\simeq\Z_\ell(1)/(q-1)\Z_\ell(1)$;
$H^1(K,\mu_{\ell^k})$ has order $\ell^k\cdot\#\mu_{\ell^k}(K)$. Reference: Serre, Local Fields, Ch. XIV (cite chapter); NSW Ch. VII
(cite chapter); Chapter 17. Paper: Lemma lem:tamfactor ("$\kappa$ the Kummer class of $q_E$ in $H^1(G,\Z_\ell(1))=\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}$"),
Lemma lem:tamagawa-exp.

### 6.2 `thm:local:kummer-inertia` (theorem; the Kummer class on inertia) P
Let $K$ be finite over $\Q_p$ with uniformiser $\varpi$, residue field $\F_q$, $\ell\ne p$, $x\in K^\times$, $a=v_K(x)$, $x=\varpi^au$ with
$u\in\mathcal O_K^\times$. Choose compatible systems of $\ell$-power roots of $\varpi$ and of $u$, and give $x$ the product system. (i)
$\kappa_x=a\,\kappa_\varpi+\kappa_u$. (ii) $\kappa_\varpi|_{I_K}=t_\ell$ (5.3, computed with $\varpi$), and $\kappa_u|_{I_K}=0$ because $u^{1/\ell^k}\in K^{\mathrm{ur}}$
(4.2(iv)); hence
$$\kappa_x|_{I_K}=v_K(x)\cdot t_\ell,$$
independently of all choices (a cocycle restricted to the normal subgroup $I_K$ on which $\chi_\ell=1$ is a homomorphism, and
coboundaries $(\chi_\ell-1)z$ vanish there). (iii) $\kappa_u$ is unramified: it factors through $G_K/I_K=\langle\Frob\rangle$, and
$\kappa_u(\Frob)\in\Z_\ell(1)$ is well defined modulo $(q-1)\Z_\ell(1)$; its class in $\Z_\ell(1)/(q-1)\Z_\ell(1)\simeq\mu_{\ell^{v_\ell(q-1)}}(\F_q)$ is
$\bar u^{(q-1)/\ell^{v_\ell(q-1)}}$, i.e. the class of $\bar u$ in $\F_q^\times\otimes\Z_\ell$ (Chapter 5, galois:kummer-finite-field (b), applied to the
Teichmuller decomposition $u=\omega(\bar u)u_1$ with $u_1$ uniquely $\ell$-divisible, 2.4, 2.7(i)). In particular $\kappa_u\equiv0$ modulo
coboundaries iff $\bar u\in(\F_q^\times)^{\ell^{v_\ell(q-1)}}$. (iv) If $\Frob$ fixes the chosen roots of $\varpi$ (5.5), then $\kappa_\varpi(\Frob)=0$ and
$\kappa_x(\Frob)=\kappa_u(\Frob)$. For any other lift $\Frob\cdot\sigma$, $\sigma\in I_K$: $\kappa_x(\Frob\sigma)=\kappa_x(\Frob)+q\,a\,t_\ell(\sigma)$. So
$c'=\kappa_x(\Frob)$ is well defined modulo the ideal $(a,q-1)\Z_\ell$ (after $\Z_\ell(1)\simeq\Z_\ell$), and $\min(v_\ell(a),v_\ell(q-1),v_\ell(c'))$ does not
depend on any choice. (v) (Inertia on $\ell^k$-th roots.) $I_K$ fixes the $\ell^k$-th roots of $x$ iff $\ell^k\mid a$; the image of $I_K$ in
$\Gal(K^{\mathrm{ur}}(x^{1/\ell^k})/K^{\mathrm{ur}})\simeq\mu_{\ell^k}$ has order $\ell^{k-\min(k,v_\ell(a))}$. Equivalently, $x$ is an $\ell^k$-th power in $K^{\mathrm{ur}}$
iff $\ell^k\mid v_K(x)$. Reference: Serre, Abelian l-adic representations, Ch. IV, A.1 (Tate curves; cite the chapter);
Silverman ATAEC Ch. V (cite the chapter); elementary from 5.3, 4.2. Paper: Lemma lem:tamagawa-exp (proof: "inertia acts
trivially on $E[\ell^t]$ exactly when ... $\ell^t\mid n_q$"; (v) is the correct form, important_notes.md point 8), Lemma
lem:tamfactor ("the restriction of $\kappa$ to $I$ is $n$ times the tame character", "$v_\ell(n')=v_\ell(n)$", and the identification
of $c'$: (iii), (iv) are the field-theoretic half of the fix in important_notes.md point 7; the cohomological half is
Chapter 17), Definition def:terms and Section sec:tam ($t_\ell(E,q)$ and the class of the unit part).

### 6.3 `prop:local:quadratic-ext` (proposition) P
(i) $p$ odd: $\Q_p$ has exactly three quadratic extensions (2.7(vi) and Kummer theory for $n=2$, Chapter 5): the unramified one
$\Q_p(\sqrt{u_0})=\Q_p(\mu_{p^2-1})$ ($u_0$ a non-square unit), and the ramified $\Q_p(\sqrt p)$, $\Q_p(\sqrt{u_0p})$. The field $\Q_p(\sqrt{p^*})$ is
$\Q_p(\sqrt p)$ if $p\equiv1\pmod4$ and $\Q_p(\sqrt{-p})=\Q_p(\sqrt{u_0p})$ if $p\equiv3\pmod4$ ($-1$ is a non-square then). Both ramified ones are
tame (3.6). (ii) $p$ odd: the quadratic characters of $G_{\Q_p}$ are $1$, the unramified $\eta_{\mathrm{ur}}$ ($\eta_{\mathrm{ur}}(\Frob)=-1$), and two
ramified ones $\chi,\chi\eta_{\mathrm{ur}}$; every ramified one restricts on $I_p$ to the unique character of order $2$ of $I_p$, namely
$\theta_2\colon\sigma\mapsto\sigma(\sqrt p)/\sqrt p$ (unique because $I_p/P_p$ is procyclic and $P_p$ is pro-odd); all have Artin conductor
exponent $a\le1$ (8.4). (iii) $p=2$: $\Q_2$ has seven quadratic extensions, $\Q_2(\sqrt d)$ for $d\in\{-1,\pm5,\pm2,\pm10\}$; the unramified one is
$\Q_2(\sqrt5)=\Q_2(\sqrt{-3})$ ($-15\equiv1\bmod8$); $\Q_2(\sqrt{-1})$, $\Q_2(\sqrt{-5})=\Q_2(\sqrt3)$ are wildly ramified with conductor exponent $2$;
$\Q_2(\sqrt{\pm2})$, $\Q_2(\sqrt{\pm10})$ with conductor exponent $3$ (5.1(v) and 8.3). Reference: Serre, Course in Arithmetic, Ch. II,
Section 3; Serre, Local Fields, Ch. IV. Paper: Lemma lem:twist (the twist by $\Q(\sqrt{q^*})$ is ramified only at $q$, tamely for
$q$ odd), Lemma lem:euler (types $\mathrm{I}_0^*$, $\mathrm{I}_n^*$: $V=V'\otimes\chi_q$), Remark rem:types (a ramified quadratic character times a
unipotent), Theorem thm:qual (b), (c).

### 6.4 `prop:local:global-quadratic-local` (proposition) P
Let $d$ be a nonsquare integer, $D$ the discriminant of $\Q(\sqrt d)$ and $\chi_d$ its character (Chapter 5, C3). Via 3.5, $\chi_d|_{G_{\Q_p}}$
is the character of $\Q_p(\sqrt d)$. (i) It is unramified iff $p\nmid D$, and then $\chi_d(\Frob_p)=\bigl(\frac Dp\bigr)$ (Chapter 6, 4.2). (ii) For an
odd prime $q$ and $\chi_q:=\chi_{q^*}$: at $p\ne q$, including $p=2$, $\chi_q$ is unramified with $\chi_q(\Frob_p)=\bigl(\frac pq\bigr)$
($q^*\equiv1\pmod4$, so $\Q_2(\sqrt{q^*})$ is unramified); at $p=q$ it is ramified, tame, $\chi_q|_{I_q}=\theta_2$, and its local conductor exponent
is $1$. (iii) $\chi_{-3}$ at $3$: tame, exponent $1$; $\chi_{-4}$ at $2$: wild, exponent $2$; $\chi_{\pm2}$ at $2$: exponent $3$; in each case
the product of $p^{a_p(\chi)}$ is the conductor of the Dirichlet character (Chapter 2, 10.3; the general statement is 6.5(iii)).
(iv) For a finite set $S$ of odd primes, $\chi_S=\prod_{q\in S}\chi_q$ is unramified outside $S$ and at each $q\in S$ restricts to $\theta_2$ on
$I_q$. (v) Consequently, for any representation $\rho$ of $G_\Q$: $(\rho\otimes\chi_q)|_{I_p}=\rho|_{I_p}$ for $p\ne q$, and $(\rho\otimes\chi_q)|_{I_q}=
\rho|_{I_q}\otimes\theta_2$; so twisting by $\chi_q$ changes nothing at $p\ne q$ (inertia, $V^{I_p}$, conductor exponent; Frobenius
changes by the sign $\chi_q(\Frob_p)$), and at $q$ multiplies the inertia action by $\pm1$. Reference: as 6.3; Chapter 6, 4.2, 4.3.
Paper: Lemma lem:twist (i) ("$\chi$ is unramified at $p$, so $E$ and $E^{(q)}$ become isomorphic over an unramified extension of
$\Q_p$") and (ii) at $q$, Theorem thm:twist ($\chi_S$), Theorem thm:quant, Lemma lem:euler ($V=V'\otimes\chi_q$), Theorem thm:qual (b), (c).

### 6.5 `thm:local:lcft` (theorem; local class field theory for $\Q_p$, explicit form) R
(i) (Local Kronecker-Weber.) $\Q_p^{\mathrm{ab}}=\Q_p^{\mathrm{ur}}\cdot\Q_p(\mu_{p^\infty})$. (ii) There is a unique continuous homomorphism
$\mathrm{Art}\colon\Q_p^\times\to G_{\Q_p}^{\mathrm{ab}}$ with: $\mathrm{Art}(p)$ is the arithmetic Frobenius on $\Q_p^{\mathrm{ur}}$ and trivial on $\Q_p(\mu_{p^\infty})$; for
$u\in\Z_p^\times$, $\mathrm{Art}(u)$ is trivial on $\Q_p^{\mathrm{ur}}$ and acts on $\mu_{p^\infty}$ by $\zeta\mapsto\zeta^{u^{-1}}$. It is injective with dense image,
$\mathrm{Art}(\Z_p^\times)=I_p^{\mathrm{ab}}$ (image of $I_p$), $\mathrm{Art}(1+p^n\Z_p)$ is the image of the upper ramification group $G_{\Q_p}^n$ ($n\ge1$),
and it extends to an isomorphism $\Q_p^\times\simeq W_{\Q_p}^{\mathrm{ab}}$ (7.1). (iii) For a character $\chi$ of $G_{\Q_p}$ of finite order, the
Artin conductor exponent (8.4) equals the least $n\ge0$ with $\chi\circ\mathrm{Art}(1+p^n\Z_p)=1$ (with $1+p^0\Z_p:=\Z_p^\times$); with Chapter 6,
5.7 this gives "the Artin conductor of $\psi_\chi$ equals the conductor of the Dirichlet character $\chi$" (Chapter 6, 5.7(ii),
stated there with a pointer here). Warning: Deligne's normalisation sends uniformisers to geometric Frobenius
elements; the book uses the arithmetic one (as Chapter 6, 5.6(iii)) and never needs the other. Reference: Serre, "Local class
field theory" in Cassels-Frohlich (cite the chapter); Milne CFT, Ch. I (cite the chapter); Neukirch V. Paper: background
(conductors of the quadratic characters in Lemma lem:twist; Section 1 table: $\chi_{-3}$, $\chi_{-4}$).

## 7. Line-up, Section 7: the Weil group and Weil-Deligne representations

### 7.1 `def:local:weil-group` (definition and proposition) P
$W_K=\{w\in G_K:\ w|_{K^{\mathrm{ur}}}\in\Frob^{\Z}\}$, with $d\colon W_K\to\Z$ defined by $w|_{K^{\mathrm{ur}}}=\Frob^{d(w)}$ and $\|w\|=q^{d(w)}$ (L4). (i) $W_K$ is a dense
subgroup of $G_K$ containing $I_K$; $W_K/I_K\simeq\Z$; it is a topological group when $I_K$ (with its profinite topology) is declared
open, and this topology is finer than the one induced from $G_K$. (ii) $\|\Frob\|=q$, $\|\Phi\|=q^{-1}$, $\|\cdot\|$ is trivial on $I_K$, and
$\|w\|=\chi_\ell(w)$ for every $\ell\ne p$ and $w\in W_K$ (4.5). (iii) Unramified characters $\mu\colon W_K\to\Omega^\times$ (trivial on $I_K$) are
determined by $\mu(\Phi)\in\Omega^\times$, which may be any element (not only units, unlike characters of $G_K$); $\|\cdot\|$ is one, with
$\|\Phi\|=q^{-1}$. (iv) (With 6.5.) $W_{\Q_p}^{\mathrm{ab}}\simeq\Q_p^\times$, with $\|\mathrm{Art}(x)\|=|x|_p^{-1}$ in the book's normalisation
($\mathrm{Art}(p)$ arithmetic, $\|\mathrm{Art}(p)\|=p$). Reference: Tate79, Section 1; Deligne73, Section 2 (add both to `bib/ch07.bib`);
Rohrlich94, Sections 1 to 3 (add). Paper: background (Lemma lem:euler and Lemma lem:twist (iii) speak of "local
components" and "Steinberg"; the Galois side is the Weil-Deligne representation).

### 7.2 `thm:local:grothendieck` (theorem, Grothendieck's $\ell$-adic monodromy theorem) P
Let $\ell\ne p$, $E/\Q_\ell$ finite, $V$ a finite-dimensional $E$-vector space and $\rho\colon G_K\to\GL(V)$ continuous (or only
$\rho\colon W_K\to\GL(V)$ continuous). Fix a generator $\zeta$ of $\Z_\ell(1)$ and let $t_\zeta\colon I_K\to\Z_\ell$ be as in L5. Then there are an open
subgroup $I_1\subseteq I_K$, normal in $G_K$, and a unique nilpotent $N\in\End_E(V)$ with
$$\rho(\sigma)=\exp\bigl(t_\zeta(\sigma)N\bigr)\quad\text{for all }\sigma\in I_1,$$
and $\rho(w)N\rho(w)^{-1}=\|w\|N$ for all $w\in W_K$ (so $\rho(\Frob)N\rho(\Frob)^{-1}=qN$). $N=0$ iff $\rho(I_K)$ is finite. Replacing $\zeta$ by
$\zeta^a$ ($a\in\Z_\ell^\times$) replaces $N$ by $a^{-1}N$. Proof: choose a stable lattice; take $I_1=I_K\cap\rho^{-1}(1+\ell^2M_n(\mathcal O))$; by 5.7 and
5.3(iv), $\rho|_{I_1}$ factors through $t_\zeta(I_1)=\ell^m\Z_\ell$; put $N=\ell^{-m}\log\rho(\sigma_1)$ for $\sigma_1\in I_1$ with $t_\zeta(\sigma_1)=\ell^m$
($\log$ and $\exp$ converge on $1+\ell^2M_n(\mathcal O)$ and $\ell^2M_n(\mathcal O)$); the relation follows from 5.4(i), and $N\sim qN$ forces all
eigenvalues of $N$ to vanish. Reference: Serre-Tate68, Appendix (cite the section); Deligne73, Section 8; Tate79,
Section 4.2; Rohrlich94, Section 4. Paper: background for Lemma lem:euler ("through a quadratic character times a unipotent
when it is potentially multiplicative"), Lemma lem:tamfactor (the unipotent action of $t$); Chapters 11, 15.

### 7.3 `def:local:wd` (definition and proposition) P
Let $\Omega$ be a field of characteristic $0$. A *Weil-Deligne representation* of $W_K$ over $\Omega$ is a triple $(r,N,V)$: $V$ a
finite-dimensional $\Omega$-vector space, $r\colon W_K\to\GL(V)$ a homomorphism whose restriction to $I_K$ has open kernel (so $r(I_K)$ is
finite), and $N\in\End(V)$ nilpotent with
$$r(w)\,N\,r(w)^{-1}=\|w\|\,N\qquad(w\in W_K),$$
that is $r(\Frob)Nr(\Frob)^{-1}=qN$ and $r(\Phi)Nr(\Phi)^{-1}=q^{-1}N$ (L4). Morphisms commute with $r$ and $N$. Constructions: $V\oplus V'$;
$V\otimes V'$ with $N\otimes1+1\otimes N'$; the dual with $r^\vee(w)=r(w^{-1})^{t}$ and $-N^{t}$; $\Hom(V,V')$; $\End V$ and $\ad V$ (trace zero)
with $N_{\ad}=[N,\cdot\,]$; twisting by a character $\mu$ of $W_K$. $(r,N)$ is *Frobenius-semisimple* if $r(\Phi)$ is semisimple; every
$(r,N)$ has a Frobenius-semisimplification (replace $r(\Phi)$ by its semisimple part; stated). (Check of the relation for $\ad$:
$r(w)[N,x]r(w)^{-1}=\|w\|[N,r(w)xr(w)^{-1}]$.) Reference: Deligne73, Section 8; Tate79, Section 4.1. Paper: background.

### 7.4 `thm:local:wd-equivalence` (theorem) S (construction P, equivalence R)
In the situation of 7.2, fix $\Phi$ (a geometric Frobenius lift) and $\zeta$. Put $r(\Phi^n\sigma)=\rho(\Phi^n\sigma)\exp(-t_\zeta(\sigma)N)$ for $n\in\Z$,
$\sigma\in I_K$. (i) $(r,N)$ is a Weil-Deligne representation over $E$ (P: $r$ is a homomorphism by 5.4(i) and the relation for $N$;
$r$ is trivial on $I_1$). (ii) Its isomorphism class does not depend on $\Phi$ or $\zeta$ (S). (iii) (R) $\rho\mapsto\mathrm{WD}(\rho)$ is an
equivalence between continuous representations of $W_K$ on finite-dimensional $E$-spaces and Weil-Deligne
representations over $E$; those that extend to $G_K$ are the ones for which the eigenvalues of $r(\Phi)$ are $\ell$-adic units. It is
compatible with $\oplus$, $\otimes$, duals, $\ad$, and unramified twists; $\Q_\ell(1)$ goes to $(\|\cdot\|,0)$ (the unramified
character with $\Phi\mapsto q^{-1}$). (iv) The Weil-Deligne representation of $\rho$ (Frobenius-semisimplified) does not depend on $\ell$
for the Tate modules of elliptic curves (stated; Chapters 11, 15), which is why $L$-factors and conductors are independent of
$\ell$. Reference: Deligne73, Section 8 (cite the section); Tate79, Section 4.2; Rohrlich94. Paper: Section 1.1
("$L_p(A_f,s)$" independent of $\ell$), Lemma lem:euler, Lemma lem:twist (iii) ("local component ... Steinberg").

### 7.5 `def:local:sp` (definition and proposition) P (classification (iii) S)
(i) For $n\ge1$, $\mathrm{sp}(n)$ is $V=\bigoplus_{i=0}^{n-1}\Omega e_i$ with $r(w)e_i=\|w\|^ie_i$ and $Ne_i=e_{i+1}$ ($e_n:=0$). The relation holds:
$r(w)Nr(w)^{-1}e_i=\|w\|e_{i+1}$. On $\mathrm{sp}(2)$: $\Phi$ acts on $e_0,e_1$ by $1,q^{-1}$ (geometric), $\Frob$ by $1,q$; $\ker N=\Omega e_1$. For a
character $\mu$ of $W_K$, $\mathrm{sp}(n)\otimes\mu$ is the *special (Steinberg) representation twisted by $\mu$*; it is indecomposable;
$\mathrm{sp}(2)\otimes\mu$ for $\mu$ unramified is the *unramified twist of Steinberg*, for $\mu$ ramified a *ramified twist*. (ii) (Every
two-dimensional $(r,N)$ with $N\ne0$ is a twist of $\mathrm{sp}(2)$.) If $\dim V=2$, $N\ne0$ and $(r,N)$ is Frobenius-semisimple, then
$(r,N)\simeq\mathrm{sp}(2)\otimes\mu$ for a unique character $\mu$ of $W_K$. Proof: $\ker N=\operatorname{im}N$ is an $r$-stable line with character $\mu'$;
$r$ on $V/\ker N$ is a character $\mu$, and $N\colon V/\ker N\to\ker N$ is an isomorphism with $\mu'=\|\cdot\|\mu$; a Frobenius eigenvector
$e_0$ outside $\ker N$ exists because $r(\Phi)$ is semisimple with the distinct eigenvalues $\mu(\Phi)$, $q^{-1}\mu(\Phi)$; $r(I_K)$ is finite,
hence acts semisimply, through the same character $\mu|_{I_K}=\mu'|_{I_K}$ on $\ker N$ and on $V/\ker N$, hence by scalars; put $e_1=Ne_0$. (iii) (S/R.) A Frobenius-semisimple $(r,0)$ of dimension $2$ is either a sum of
two characters or irreducible; an irreducible one is induced from a character of $W_{K'}$, $K'/K$ quadratic, except possibly
when $p=2$ ("primitive" representations). Reference: Tate79, Section 4.1.4; Rohrlich94, Sections 5 to 8. Paper: Lemma
lem:twist (iii) ("unramified twist of the Steinberg representation"), Lemma lem:euler (type $\mathrm{I}_n$: "unramified twist of the
Steinberg representation"); Chapter 15 (local components: principal series, Steinberg, supercuspidal).

### 7.6 `ex:local:tate-shape-wd` (worked example) P
Let $\ell\ne p$, $x\in K^\times$ with $a=v_K(x)$, $\varepsilon\colon G_K\to\{\pm1\}$ unramified, and $\rho$ on $\Q_\ell e_1\oplus\Q_\ell e_2$ given by
$$\rho(g)=\begin{pmatrix}\chi_\ell(g)\varepsilon(g)&\varepsilon(g)\kappa_x(g)\\0&\varepsilon(g)\end{pmatrix}$$
(the twist by $\varepsilon$ of the Kummer extension $\begin{psmallmatrix}\chi_\ell&\kappa_x\\0&1\end{psmallmatrix}$ of Chapter 5, galois:l-adic-kummer; the
corner of the twisted representation is $\varepsilon\kappa_x$, see Part 15, N1). (i) On $I_K$: $\rho(\sigma)=\begin{psmallmatrix}1&a\,t_\ell(\sigma)\\0&1\end{psmallmatrix}$
(6.2(ii)); so $N=a\,u_\zeta E_{12}$ ($u_\zeta\in\Z_\ell^\times$ from identifying the $e_1$-line with $\Z_\ell(1)$), and $N\ne0$ iff $a\ne0$. (ii) If
$a\ne0$: $\mathrm{WD}(\rho)\simeq\mathrm{sp}(2)\otimes\mu_\varepsilon$ with $\mu_\varepsilon$ unramified, $\mu_\varepsilon(\Phi)=\varepsilon(\Frob)$ ($e_0$ a $\Phi$-eigenvector over $e_2$, $e_1=Ne_0$);
$V^{I_K}=\Q_\ell e_1$ with $\Phi$ acting by $\varepsilon q^{-1}$ and $\Frob$ by $\varepsilon q$. (iii) If $a=0$: $\rho$ is unramified with $\Frob$-eigenvalues $\varepsilon q$,
$\varepsilon$ (distinct), $N=0$. (iv) Integrally ($\Z_\ell e_1\oplus\Z_\ell e_2$): $I_K$ acts on the lattice mod $\ell^k$ trivially iff $\ell^k\mid a$ (6.2(v)).
Chapters 10 and 11 show that $T_\ell E$ at a prime of multiplicative reduction has exactly this shape with $x=q_E$ the
Tate parameter and $\varepsilon$ trivial or the unramified quadratic character (split or nonsplit). Paper: Lemma lem:tamagawa-exp,
Lemma lem:tamfactor (the matrices, $te_2=e_2+n'e_1$ with $v_\ell(n')=v_\ell(n)$), Lemma lem:euler (type $\mathrm{I}_n$), Definition def:terms ($\delta_q=1$).

## 8. Line-up, Section 8: inertia invariants, local $L$-factors, conductors, $\epsilon$-factors

### 8.1 `prop:local:invariants` (proposition) P
Let $\rho\colon G_K\to\GL(V)$ be continuous ($\ell\ne p$) with $\mathrm{WD}(\rho)=(r,N)$. Then
$$V^{\rho(I_K)}=(\ker N)^{r(I_K)},$$
and $\rho(\Phi)=r(\Phi)$ on it (for the $\Phi$ used in 7.4). In particular $\dim V^{I_K}$ and the characteristic polynomial of Frobenius on
$V^{I_K}$ depend only on the Weil-Deligne representation. Proof: if $v\in\ker N$ is $r(I_K)$-fixed then $\rho(\sigma)v=r(\sigma)\exp(t_\zeta(\sigma)N)v=v$;
conversely, $\exp(tN)v=v$ for $t$ in an open subgroup of $\Z_\ell$ gives $Nv=0$ (take logarithms), and then $r(\sigma)v=v$. Examples:
$\mathrm{sp}(2)\otimes\mu$ with $\mu$ unramified: $\Omega e_1$; with $\mu$ ramified: $0$; $(r,0)$ with $r(I_K)$ finite: $V^{r(I_K)}$. Notation: the
paper's $\delta_p=\dim V^{I_p}$ for $V=V_\ell E$ (Section 1.1). Reference: Tate79, Section 4.2; Deligne73, Section 8. Paper: Section 1.1
($\delta_p$, $A_f^{I_p}$), Lemma lem:euler ("$(\ad V)^{I_q}$ is a line"), Lemma lem:dfg21 and the paragraph after it ($(V^D)^{I_p}$).

### 8.2 `def:local:L-factor` (definition, convention and proposition) P
For $\rho$ as in 8.1 (or a Weil-Deligne representation $(r,N)$):
$$L(V,s)=\det\bigl(1-\Phi\,q^{-s}\bigm|V^{I_K}\bigr)^{-1}=\det\bigl(1-r(\Phi)q^{-s}\bigm|(\ker N)^{r(I_K)}\bigr)^{-1},\qquad\Phi=\Frob^{-1}\text{ geometric.}$$
(i) It is well defined (any two geometric Frobenius lifts agree on $V^{I_K}$) and depends only on the Weil-Deligne class.
(ii) $L(V\oplus V',s)=L(V,s)L(V',s)$. (iii) For $\mu$ unramified with $\mu(\Phi)=\lambda$: $L(\mu,s)=(1-\lambda q^{-s})^{-1}$; $L(\Q_\ell(1),s)=(1-q^{-1-s})^{-1}$;
$L(V(1),s)=L(V,s+1)$, and more generally $L(V\otimes\|\cdot\|^{k},s)=L(V,s+k)$. (iv) With the arithmetic $\Frob$ in place of $\Phi$ one would get
$L(V(1),s)=L(V,s-1)$ and the factor $(1-q^{1-s})^{-1}$ for $\Q_\ell(1)$; this is why the geometric convention is forced by the paper's
Lemma lem:fpr ("$L_p(A_f,1)^{-1}=L_p(A_f(1),0)^{-1}$") and table (important_notes.md point 11). (v) Examples: $L(\mathrm{sp}(2)\otimes\mu,s)=
(1-\mu(\Phi)q^{-1-s})^{-1}$ for $\mu$ unramified, $=1$ for $\mu$ ramified; for $E/\Q$ with good reduction at $p\ne\ell$, the arithmetic
Frobenius on $V_\ell E$ has eigenvalues $\alpha,\beta$ ($\alpha+\beta=a_p$, $\alpha\beta=p$; Chapter 9), the geometric one $\alpha^{-1},\beta^{-1}$, so
$L(V_\ell E,s)=(1-a_pp^{-1-s}+p^{-1-2s})^{-1}=L_p(E,s+1)$ and $L(V_\ell E^\vee,s)=(1-a_pp^{-s}+p^{1-2s})^{-1}=L_p(E,s)$ (as Chapter 6, 3.7). Reference:
Deligne73, Section 8 (cite the section); Tate79, Section 4.1; DFG04 1.7.2 for the convention in the paper's source. Paper:
Section 1.1 (definition of $L_p(A_f,s)$, $L_p^{\nv}$), the table of Section 1, Definition def:terms, Lemma lem:euler, Lemma lem:fpr, the
paragraph after Lemma lem:dfg21 ("$\det(1-\Frob_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}$", true with $\Frob_p$ read as geometric).

### 8.3 `def:local:swan` (definition and theorem) S (definition P, integrality R)
Let $V$ be a finite-dimensional representation over a field $\Omega$ of $G_K$, $W_K$ or just $I_K$, such that $I_K$ acts through a finite
quotient: there is a finite Galois $L/K$, $G=\Gal(L/K)$, with $I_K$ acting through its image $G_0=I(L/K)$ (5.2(i)). For an $\ell$-adic $\rho$,
apply this to $r|_{I_K}$ of 7.4, or to $\rho|_{P_K}$, which has finite image by 5.7. With $g_i=\#G_i$:
$$\operatorname{sw}(V)=\sum_{i\ge1}\frac{g_i}{g_0}\dim\bigl(V/V^{G_i}\bigr),\qquad a(V)=\sum_{i\ge0}\frac{g_i}{g_0}\dim\bigl(V/V^{G_i}\bigr)=\dim V/V^{I_K}+\operatorname{sw}(V).$$
(i) These do not depend on $L$ (Herbrand); in upper numbering $\operatorname{sw}(V)=\int_0^\infty\dim(V/V^{G_K^u})\,du$ (S). (ii) (R; Artin, Serre)
$\operatorname{sw}(V)$ and $a(V)$ are nonnegative integers. (iii) $\operatorname{sw}(V)=0$ iff $P_K$ acts trivially (tame); $\operatorname{sw}$ depends only on $V|_{P_K}$;
both are additive in $V$ and unchanged by unramified base change (4.4) and by twisting by unramified characters. (iv) For a
character $\chi$: $a(\chi)=0$ if unramified, $1$ if tamely ramified, and $1+c$ if wildly ramified with largest upper jump $c$; this
agrees with 6.5(iii). Examples: $\chi_{-4}$ at $2$: $\operatorname{sw}=1$, $a=2$; $\chi_{\pm2}$ at $2$: $\operatorname{sw}=2$, $a=3$ (5.1(v)). (v) The same
definitions apply verbatim to representations over $\F_\ell$ (where the image of inertia is finite); this is the local factor
of the Serre conductor used in Chapter 11 and in the paper (Lemma lem:IV: "the Serre conductor exponent at $q$ is
$\dim E[3]-\dim E[3]^{I_q}=1$, there being no wild part"). Reference: Serre, Local Fields, Ch. VI, Section 2 (cite the section);
Serre, Linear representations of finite groups, Ch. 19 (Artin representation; cite the chapter). Paper: Lemma lem:IV, Remark
rem:types, Remark rem:wild (wild primes), Lemma lem:twist (ii) ("the conductor exponents are the standard ones for $q$ odd
(tame)", important_notes.md point 28).

### 8.4 `def:local:conductor` (definition and proposition) P
The conductor exponent of a Weil-Deligne representation $(r,N,V)$ is
$$a(r,N)=a(r)+\dim V^{r(I_K)}-\dim(\ker N)^{r(I_K)}=\dim V-\dim(\ker N)^{r(I_K)}+\operatorname{sw}(r),$$
and for $\ell$-adic $\rho$, $a(\rho):=a(\mathrm{WD}(\rho))=\dim V-\dim V^{\rho(I_K)}+\operatorname{sw}(\rho)$, where $\operatorname{sw}(\rho)=\operatorname{sw}(\rho|_{P_K})$ (8.1; $\rho(P_K)=r(P_K)$
since $P_K\subseteq\ker t_\zeta$). Properties: additive; invariant under unramified twists and unramified base change; $a=0$ iff
unramified; for $\rho$ tamely ramified, $a(\rho)=\dim V-\dim V^{I_K}$. For $E/\Q$ and $\ell\ne p$, $a(V_\ell E|_{G_{\Q_p}})$ is the exponent of $p$ in
the conductor of $E$ (Ogg-Saito, stated; Chapter 10). Reference: Serre-Tate68, Section 2 (conductor of an $\ell$-adic
representation); Tate79, Section 4.1; Rohrlich94. Paper: Lemma lem:twist (ii), (iii) ("conductor exponent $2$"), Lemma lem:IV,
Remark rem:types, Theorem thm:qual (Serre conductors), Section 1.4.

### 8.5 `def:local:epsilon` (theorem and definition) R
(Langlands, Deligne.) For a nontrivial additive character $\psi$ of $K$ and a Haar measure $dx$ there is a unique way to attach
$\epsilon(r,\psi,dx)\in\Omega^\times$ to representations $r$ of $W_K$ (with $r(I_K)$ finite), multiplicative in exact sequences, inductive in
degree $0$, and equal to Tate's local constant for characters; for Weil-Deligne representations
$\epsilon(r,N,\psi,dx)=\epsilon(r,\psi,dx)\det\bigl(-\Phi\bigm|V^{r(I_K)}/(\ker N)^{r(I_K)}\bigr)$. The local root number is
$w(V)=\epsilon(V,\psi,dx)/|\epsilon(V,\psi,dx)|$ (for $V$ with real structure; stated). The paper does not use $\epsilon$-factors; Chapter 15
recalls this item. Reference: Deligne73, Sections 4 to 5 and 8; Tate79, Sections 3 and 4. Paper: none (background for
Chapter 15 and the functional equations of Chapter 19).

## 9. Line-up, Section 9: the local shapes the paper meets, and their adjoints

Standing hypotheses of this section: $K=\Q_q$ ($q$ the paper's prime, so $\#k_K=q$), $\ell\ne q$, $V$ a two-dimensional $\Q_\ell$-representation
(or over a finite extension) of $G_{\Q_q}$ with $\det V|_{I_q}=1$ (true for $V_\ell E$, whose determinant is $\chi_\ell$, unramified at $q$),
$A=\ad V$ the trace-zero adjoint (Chapter 4), $\Phi$ geometric. The linear algebra of the inertia actions is Chapter 4, items 9.1 to
9.4, and Chapter 6, 4.10; this section adds the Weil-Deligne description, the conductors and the $L$-factors. The
dictionary to Kodaira types is a black box from Chapters 10 and 11 and is quoted only in the last column of 9.4.

### 9.1 `prop:local:unramified-shape` (proposition) P
If $V$ is unramified with arithmetic Frobenius eigenvalues $\alpha,\beta$: $\mathrm{WD}(V)=(r,0)$, $a(V)=0$, $L(V,s)=(1-\alpha^{-1}q^{-s})^{-1}(1-\beta^{-1}q^{-s})^{-1}$,
$A$ is unramified with eigenvalues $\alpha/\beta,1,\beta/\alpha$ for both Frobenii (inversion-stable set), and
$$L(A,s)^{-1}=\Bigl(1-\frac\alpha\beta q^{-s}\Bigr)(1-q^{-s})\Bigl(1-\frac\beta\alpha q^{-s}\Bigr),\qquad L(A,1)^{-1}=\frac{q-1}q\cdot\frac{(q+1)^2-a^2}{q^2}\ \text{ if }\alpha+\beta=a,\ \alpha\beta=q$$
(the algebraic identity is Chapter 2, 11.4). Paper: the $\mathrm{I}_0^*$ row of the table ($V=V'\otimes\chi_q$, $A=\ad V'$ unramified), Theorem
thm:dfg14 (Wiles's level-raising factor at a good prime), Lemma lem:euler.

### 9.2 `prop:local:tame-cyclic-shape` (proposition) P
Suppose $\rho(I_q)$ is finite cyclic of order $m\in\{2,3,4,6\}$ with $q\nmid m$ (tame; 5.6), generated by $g$. Then $N=0$ and:
(i) $m=2$: $g=-1$; for $q$ odd and any ramified quadratic character $\chi$ of $G_{\Q_q}$ (6.3), $V\otimes\chi$ is unramified, $V^{I_q}=0$,
$a(V)=2$, $L(V,s)=1$, and $A=\ad(V\otimes\chi)$ is unramified, so $L(A,s)$ is as in 9.1 for $V\otimes\chi$. (ii) $m\in\{3,4,6\}$: $g$ has
eigenvalues $\zeta,\zeta^{-1}$ ($\zeta$ primitive of order $m$, Chapter 4, 9.3), so $V^{I_q}=0$, $a(V)=2$ (tame) and $L(V,s)=1$. Put $m'=3$ if
$m\in\{3,6\}$ and $m'=4$ if $m=4$, and $\chi=\chi_{-3}$, resp. $\chi_{-4}$. Then $\Frob\,g\,\Frob^{-1}=g^q$ (5.6), so $\rho(\Frob)$ commutes with $g$ if
$q\equiv1\pmod{m'}$ and conjugates $g$ to $g^{-1}$ if $q\equiv-1\pmod{m'}$ (for $m=6$, $g=-\sigma$ and $\sigma\mapsto\sigma^q$); in the first case
$V\otimes\Omega(\zeta)$ is a sum of two characters of $W_{\Q_q}$ restricting to $\zeta^{\pm1}$-characters of $I_q$; in the second $V\otimes\Omega(\zeta)$ is
induced from a character of $W_{K_2}$, $K_2$ the unramified quadratic extension (the two eigenlines are swapped by $\Frob$).
(iii) $A^{I_q}$ is the line spanned by $2g-\tr g$ (that is $2\sigma+1$, with square $-3$, for $m=3,6$; $\tau=g$ for $m=4$; Chapter 4, 9.2), and both
$\Frob$ and $\Phi$ act on it by $\chi(q)\in\{\pm1\}$ (for $\Phi$: $\Phi g\Phi^{-1}=g^{q'}$ with $qq'\equiv1$, and $q'\equiv q\pmod{m'}$). Hence
$$L(A,s)^{-1}=1-\chi(q)\,q^{-s},\qquad a(A)=2.$$
Reference: elementary from 5.6, 8.1 to 8.4 and Chapters 4 and 6. Paper: Lemma lem:euler (types $\mathrm{II},\mathrm{II}^*,\mathrm{IV},\mathrm{IV}^*$ with
$\chi_{-3}$, types $\mathrm{III},\mathrm{III}^*$ with $\chi_{-4}$, type $\mathrm{I}_0^*$ via (i)), the table of Section 1, Lemma lem:IV (cyclic tame image; the
mod $3$ computation is Chapter 4, 9.4 and Chapter 6, 4.8), Remark rem:types, Section 1.4 (conductor exponent $2$ at additive primes).

### 9.3 `prop:local:steinberg-shape` (proposition) P
Let $\mu$ be an unramified character and $\chi$ a ramified quadratic character of $G_{\Q_q}$.
(i) $V=\mathrm{sp}(2)\otimes\mu$: $V^{I_q}=\ker N$ is a line on which $\Phi$ acts by $\mu(\Phi)q^{-1}$ ($\Frob$ by $\mu(\Frob)q$); $a(V)=1$;
$L(V,s)=(1-\mu(\Phi)q^{-1-s})^{-1}$. (ii) $V=\mathrm{sp}(2)\otimes\mu\chi$: $V^{I_q}=0$, $L(V,s)=1$, $a(V)=2a(\chi)$, which is $2$ for $q$ odd (tame $\chi$) and $4$
or $6$ for $q=2$ (6.3(iii)). This is the content of "the twist of an unramified twist of Steinberg by a ramified quadratic
character has conductor exponent $2$" (Lemma lem:twist (iii), $q$ odd). (iii) The adjoint: $\ad(\mathrm{sp}(2)\otimes\mu\chi^{j})=\ad\mathrm{sp}(2)\simeq
\mathrm{sp}(3)\otimes\|\cdot\|^{-1}$: in the basis $E_{01}$, $h=E_{00}-E_{11}$, $E_{10}=N$ (with $E_{ij}=e_i\otimes e_j^\vee$), $\Phi$ acts by $q,1,q^{-1}$ and
$[N,E_{01}]=-h$, $[N,h]=2N$, $[N,N]=0$. So $A^{I_q}=\ker[N,\cdot\,]=\Omega N$, $\Phi$ acts on it by $q^{-1}$ ($\Frob$ by $q$), $a(A)=2$ and
$$L(\ad V,s)=(1-q^{-1-s})^{-1}\qquad\text{for }V=\mathrm{sp}(2)\otimes\mu\text{ and }V=\mathrm{sp}(2)\otimes\mu\chi .$$
With the arithmetic Frobenius one would get $(1-q^{1-s})^{-1}$; the paper's table has $1-q^{-1-s}$ (important_notes.md point 11). (iv) The line
$\Omega N$ is the line $\Z_\ell e$, $e=e_1\otimes e_2^\vee$, of Lemma lem:tamfactor (in the paper's basis, 7.6). Reference: Tate79, Section 4.1;
Rohrlich94, Sections 9 to 11; elementary (verified symbolically). Paper: Lemma lem:twist (iii), Lemma lem:euler (types $\mathrm{I}_n$
and $\mathrm{I}_n^*$: "$(\ad V)^{I_q}$ is a line with eigenvalue $q^{-1}$", "$V=V'\otimes\chi_q$ with $V'$ Steinberg ... $\ad V=\ad V'$"), Definition def:terms
($e_\ell=0$ at multiplicative primes: naive and true factors agree), Lemma lem:fpr ($L_p(A_f,1)^{-1}=1-p^{-2}$ at a multiplicative $p$),
Theorem thm:dfg14 (the factor $1-p^{-2}$), Lemma lem:tamfactor.

### 9.4 `thm:local:shapes-table` (summary table) P (the last column R, forward)
For $V$ two-dimensional, $\det V|_{I_q}=1$, $q\ge5$ (so every finite inertia image below is tame), the shapes and their invariants are:

| shape of $\mathrm{WD}(V)$ | $\rho(I_q)$ | $\dim V^{I_q}$ | $a(V)$ | $L(V,s)^{-1}$ | $\dim A^{I_q}$ | $L(A,s)^{-1}$ ($\Phi$ geometric) | Kodaira types (Ch. 10, 11) |
|-|-|-|-|-|-|-|-|
| unramified, $\Frob$-eigenvalues $\alpha,\beta$ | $1$ | 2 | 0 | $(1-\alpha^{-1}q^{-s})(1-\beta^{-1}q^{-s})$ | 3 | $(1-\frac\alpha\beta q^{-s})(1-q^{-s})(1-\frac\beta\alpha q^{-s})$ | $\mathrm{I}_0$ |
| $(\text{unramified})\otimes\chi$, $\chi$ ramified quadratic | $\{\pm1\}$ | 0 | 2 | $1$ | 3 | as for the untwisted row | $\mathrm{I}_0^*$ |
| $\mathrm{sp}(2)\otimes\mu$, $\mu$ unramified | unipotent, infinite | 1 | 1 | $1-\mu(\Phi)q^{-1-s}$ | 1 | $1-q^{-1-s}$ | $\mathrm{I}_n$, $n\ge1$ |
| $\mathrm{sp}(2)\otimes\mu\chi$ | $\pm$ unipotent | 0 | 2 | $1$ | 1 | $1-q^{-1-s}$ | $\mathrm{I}_n^*$, $n\ge1$ |
| $N=0$, $\rho(I_q)$ cyclic of order $3$ or $6$ | $\langle\sigma\rangle$ or $\langle-\sigma\rangle$ | 0 | 2 | $1$ | 1 | $1-\chi_{-3}(q)q^{-s}$ | $\mathrm{IV},\mathrm{IV}^*$; $\mathrm{II},\mathrm{II}^*$ |
| $N=0$, $\rho(I_q)$ cyclic of order $4$ | $\langle\tau\rangle$ | 0 | 2 | $1$ | 1 | $1-\chi_{-4}(q)q^{-s}$ | $\mathrm{III},\mathrm{III}^*$ |

$\delta_q=\dim V^{I_q}$ is $2,0,1,0,0,0$ down the rows, and the naive factor of the paper is $L(A,s)$ when $\delta_q>0$ and $1$ when $\delta_q=0$
(Section 1.1); so the omitted factor is $L(A,s)^{-1}$ in rows 2, 4, 5, 6 and nothing in rows 1, 3. The $\ell$-adic valuations at $s=1$
($e_\ell(E,q)$) are Chapter 2 (11.3 to 11.5) and Chapter 19. Writer's note: Chapter 4's table 9.3 already lists $\rho(I_q)$, $\dim V^{I_q}$,
$\dim A^{I_q}$ and the generator of $A^{I_q}$; here cite it for those columns and add the columns $a(V)$, $L(V,s)$, $L(A,s)$. Reference: as
9.1 to 9.3; Kraus90 and Serre-Tate68 for the Kodaira column (Chapters 10, 11). Paper: Lemma lem:euler and the table of Section 1
(every row), Definition def:terms, Lemma lem:twist (ii), (iii), Remark rem:types, Section 1.4.

### 9.5 `ex:local:wild-shapes` (worked example and remarks) S
(i) At $q=3$ an inertia image of order $3$ (or $6$) is wild, since $I_3/P_3$ has no quotient of order $3$ (5.3(ii)); the computation of
9.2(iii) still gives $A^{I_3}$ spanned by $2\sigma+1$ when $\rho(I_3)$ is cyclic, but nothing forces cyclicity and $a(V)=2+\operatorname{sw}(V)$ with
$\operatorname{sw}(V)$ possibly positive; this is why the paper's Lemmas lem:IV and lem:euler assume $q\ge5$ and why the Kodaira type does not
determine the factor at $q=2,3$ (Remark rem:wild). (ii) At $q=2$ an inertia image of order $3$ is tame ($2\nmid3$) and 9.2 applies
verbatim: $\chi_{-3}(2)=-1$, so $L(A,s)^{-1}=1+2^{-s}$, i.e. $L(\Sym f,s)^{-1}=L(A,s-1)^{-1}=1+2\cdot2^{-s}$, $P_2(X)=1+2X$, and $e_3(E,2)=v_3(1+2\cdot2^{-2})=v_3(3/2)=1$;
this agrees with the paper's Remark rem:wild ("a type $\mathrm{IV}$ at $2$ has $P_2(X)=1+2X$ and $e_3=1$") on the assumption, from Chapters 10, 11
(not proved here), that the image of inertia at $2$ for that type is cyclic of order $3$. (iii) At $q=2$ a non-abelian inertia image
acting absolutely irreducibly (e.g. $Q_8$, $\SL_2(\F_3)$) has $A^{I_2}=\End_{I_2}(V)_{\tr=0}=0$ (Schur), so $L(A,s)=1$: consistent with "a type $\mathrm{II}$
at $2$ has $P_2=1$" when the image is of that kind (again a black box from Chapters 10, 11). (iv) For $\mathrm{sp}(2)\otimes\mu\chi$ at $q=2$ with
$\chi$ wild, $a=4$ or $6$ (9.3(ii)); and a potentially good $\rho$ at $q=2$ of Kodaira type $\mathrm{I}_n^*$ is possible (Definition def:terms:
"$t_\ell=0$" then), because at $q=2$ the Kodaira type does not determine the Weil-Deligne shape. Reference: Serre-Tate68, Section 2;
Kraus90; Rohrlich94. Paper: Remark rem:wild, Section sec:wild, Definition def:terms (the $\mathrm{I}_n^*$ at $2$ remark), Proposition prop:forms
($\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ with $e_3(E,2)\ge1$).

## 10. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200). The card lists all 53 items (about 190 lines,
not counted).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: items 1.1 to 9.5, each stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | lem:tamagawa-exp (4.2, 4.4, 6.2(v)); lem:tamfactor (5.3 to 5.5, 6.1, 6.2, 2.7); lem:IV and rem:types (5.6, 5.7, 8.3, 9.2); lem:twist (i) to (iii) (4.4, 6.3, 6.4, 8.4, 9.3); lem:euler and the table (8.1, 8.2, 9.1 to 9.4); rem:wild and sec:wild (5.1, 5.7, 9.5); Section 1.1, def:terms, lem:fpr, the paragraph after lem:dfg21 (8.2, convention L3) | 40 |
| 1 | Absolute values, completions, $\Q_p$ and $\Z_p$ | 1.1 to 1.5; RHB aside (digits and carries); `warning`: the analytic $\Z_p$ equals Chapter 3's algebraic $\Z_\ell$ (1.4(ii)) | 190 |
| 2 | Hensel's lemma; units, roots of unity and powers | 2.1 to 2.8; the conventions box L1; `paperlink` for lem:tamfactor (2.7: $\ell$-th powers of units read on the reduction) | 240 |
| 3 | Finite extensions of $\Q_p$ | 3.1 to 3.6; `paperlink` for lem:IV ($\Z_3[\zeta_3]$ as ring of integers of $\Q_3(\sqrt{-3})$) and for Chapter 6's deferred items (3.4, 3.5) | 190 |
| 4 | Unramified extensions, $\Q_p^{\mathrm{ur}}$ and Frobenius | 4.1 to 4.5; convention L3 as `convention` 4.3 with the dictionary; `paperlink` for lem:tamagawa-exp (4.2(iv), 4.4) | 150 |
| 5 | Ramification groups, inertia and the tame quotient | 5.1 to 5.8; the diagram $G_K\supset I_K\supset P_K$ with quotients $\hat\Z$, $\prod_{\ell\ne p}\Z_\ell(1)$; `paperlink` for lem:tamfactor (5.3, 5.4, 5.5) and lem:IV, lem:euler (5.6); `warning` on the sign: $\Frob\,t\,\Frob^{-1}=t^q$ versus $\Phi\,t\,\Phi^{-1}=t^{q^{-1}}$ | 270 |
| 6 | Kummer theory over local fields; quadratic characters | 6.1 to 6.5; `paperlink` for lem:tamagawa-exp (6.2(v), important_notes.md point 8) and lem:tamfactor (6.2(ii) to (iv), point 7); `warning` on the two normalisations of the Artin map | 210 |
| 7 | The Weil group and Weil-Deligne representations | 7.1 to 7.6; convention L4; RHB aside: $N$ as the "logarithm of the monodromy", like $\log$ of a unipotent matrix; `paperlink` for lem:twist (iii) and lem:euler ("Steinberg") | 220 |
| 8 | Inertia invariants, $L$-factors and conductors | 8.1 to 8.5; convention L6 restated; `warning` (important_notes.md point 11): the paper's $L_p$ needs $\Phi$; `paperlink` for Section 1.1, lem:fpr, the paragraph after lem:dfg21 | 170 |
| 9 | The local shapes and their adjoints | 9.1 to 9.5, the table 9.4; `paperlink` for lem:euler (every row) and rem:wild (9.5) | 220 |
| 10 | Exercises | 18 exercises (Part 11) | 140 |
| 11 | Notes and references | Serre (Local Fields; Course in Arithmetic; Abelian l-adic representations; Linear representations), Neukirch, Koblitz, Cassels-Frohlich, Milne CFT, NSW, Silverman ATAEC, Serre-Tate68, Deligne73, Tate79, Rohrlich94; which numbers were cited (none of the theorem numbers flagged "check") | 40 |
| | **total** | | **2080** |

## 11. Coverage table and exercises

### 11.1 Coverage

| PLAN.md scope item, Section 6 map row, or paper hook | line-up items |
|-|-|
| absolute values | 1.1, 1.2 |
| completions | 1.3, 3.4 |
| $\Q_p$ and $\Z_p$ as completions and as inverse limits | 1.4 |
| $p$-adic expansions | 1.5, 2.3(a) |
| Hensel's lemma (two forms) | 2.1 (simple root, Newton), 2.2 (factorisation), 2.3, 4.2(iii) |
| structure of $\Z_p^\times$ and $\Q_p^\times$; $1+p\Z_p\simeq\Z_p$ via $\log/\exp$ ($p$ odd) | 2.5 |
| roots of unity in $\Q_p$; Teichmuller lift | 2.4, 2.6 |
| squares and $\ell$-th powers in $\Q_p^\times$; $u\in\Z_p^\times$ an $\ell$-th power iff its reduction is | 2.3(e), (f), 2.7, 2.8 |
| finite extensions; ramification index, residue degree | 3.1, 3.2, 3.4 |
| unramified extensions (one of each degree, cyclic, roots of unity of order prime to $p$, Frobenius) | 4.1, 4.3 |
| totally ramified extensions | 3.3, 3.6 |
| tamely and wildly ramified extensions | 3.2, 3.6, 5.1, 5.2 |
| maximal unramified extension $\Q_p^{\mathrm{ur}}$ | 4.2, 4.4 |
| inertia group $I_p$; wild inertia $P_p$ (pro-$p$) | 5.1, 5.2, 5.7 |
| tame quotient $I_p/P_p=\prod_{\ell\ne p}\Z_\ell(1)$; tame character $t_\ell$ via roots of $p$ or of any uniformiser | 5.3 |
| $\Frob^{-1}t\,\Frob=t^{p^{-1}}$, equivalently $\Frob\,t\,\Frob^{-1}=t^p$ | 5.4, 5.8 |
| $G_{\Q_p}$ and its filtration | 5.1(iv), 5.2(iv) |
| Kummer theory over $\Q_p$: $H^1(G_{\Q_p},\mu_{\ell^k})=\Q_p^\times/(\Q_p^\times)^{\ell^k}$ (foreshadowing Chapter 17) | 6.1 |
| restriction of the Kummer class of $u\in\Q_p^\times$ to $I_p$ is $v_p(u)$ times the tame character | 6.2(ii) |
| unramified quadratic extension; ramified $\Q_p(\sqrt{p^*})$ and their characters | 6.3 |
| local behaviour of quadratic characters of $G_\Q$ ($\chi_q$ unramified at $p\ne q$, ramified at $q$) | 6.4 |
| Weil group $W_{\Q_p}$ | 7.1, 6.5(ii) |
| Weil-Deligne representations, $(r,N)$, the relation (explicit convention) | 7.2, 7.3, 7.4, convention L4 |
| inertia invariants | 8.1 |
| local $L$-factor (explicit Frobenius convention) | 8.2, 4.3, convention L6 |
| Artin conductor $a(r)=\operatorname{codim}V^I+\mathrm{Swan}$ | 8.3, 8.4 |
| special cases: unramified; tamely ramified through a finite cyclic quotient | 9.1, 9.2, 5.6 |
| $\mathrm{sp}(2)$ and its unramified twists (conductor exponent $1$) | 7.5, 9.3(i) |
| twist of $\mathrm{sp}(2)$ by a ramified quadratic character (conductor exponent $2$) | 9.3(ii) |
| finite image of inertia of order $2,3,4,6$ (conductor exponent $2$ for $q\ge5$) | 9.2, 9.4 |
| Section 6 row: Tate parameter, unit part, $\ell$-th powers in $\F_q^\times$, $t_\ell(E,q)$, potentially multiplicative reduction (Chapters 2, 7, 10) | 2.7, 2.8, 6.2, 7.6, 9.3 |
| Section 6 row: Steinberg representation, unramified twists, ramified twist has conductor exponent $2$ (Chapters 7, 15) | 7.5, 9.3, 9.4 |
| Section 6 row: image of inertia on $T_\ell E$ at additive primes, unipotent elements, $\Z_3[\zeta_3]$ (Chapters 4, 6, 7, 11) | 3.3(b), 5.6, 5.7, 7.2, 9.2, 9.5 |
| Section 6 row: Kummer theory, Kummer classes, $H^1(G,\Z_\ell(1))$, tame character, $\Frob^{-1}t\Frob=t^{q^{-1}}$ (Chapters 5, 7, 16, 17) | 5.3, 5.4, 5.5, 6.1, 6.2 |
| hook: Lemma lem:tamagawa-exp (Tate curve over the unramified quadratic extension; $\ell^t$-th roots) | 4.1, 4.2(iv), 4.4, 6.2(v), 7.6(iv) |
| hook: Lemma lem:tamfactor (tame character; $\Frob^{-1}t\Frob=t^{q^{-1}}$; Kummer class $\kappa$; restriction to $I$ is $n$ times $t_\ell$; $\Z_\ell(1)/(q-1)$) | 2.6, 2.7(v), 5.3, 5.4, 5.5, 6.1, 6.2, 7.6, 9.3(iv) |
| hook: Lemma lem:IV and Remark rem:types (tame inertia cyclic; wild at $2$ and $3$) | 3.3(b), 5.6, 5.7, 8.3(v), 9.2, 9.5(i) |
| hook: Lemma lem:twist (iii) (unramified twist of Steinberg; ramified twist has exponent $2$) | 7.5, 9.3(ii), 8.4 |
| hook: Lemma lem:twist (i), (ii) (unramified base change; tame quadratic characters at odd $q$; point 28) | 4.4, 6.3, 6.4(v), 8.3(iii) |
| hook: Lemma lem:euler (eigenvalues of Frobenius on inertia invariants) | 5.6, 8.1, 8.2, 9.1 to 9.4 |
| hook: Remark rem:wild (and Section sec:wild, Definition def:terms at $q=2$) | 5.1(v), 5.7, 8.3, 9.5 |
| also: Section 1.1 ($\delta_p$, $L_p(A_f,s)$), Lemma lem:fpr ($L_p(A_f(1),0)=L_p(A_f,1)$), paragraph after Lemma lem:dfg21 | 8.1, 8.2(iii), (iv) |
| also: Chapter 6's deferred items (3.10(v), 3.11 profinite, 4.7(iv), 4.9 Hensel, 5.7(ii) conductors, 7.4) | 3.5, 5.4, 3.3(b), 2.3(g), 6.5(iii), 3.4 |
| also: Chapter 16's imported facts ($I/P$, $I^{(\ell)}=\Z_\ell(1)$, kernel prime to $\ell$, the relation, $\chi_\ell(\Frob)=p$, Kummer on inertia) | 5.3, 5.4, 4.5, 6.2 |

### 11.2 Exercises (Section 10 of the chapter), graded from easy to harder

1. Find the $5$-adic expansions of $-1/3$ and $1/3$ to five digits, and prove that $x\in\Q_p$ is rational iff its expansion is
   eventually periodic.
2. Prove that $\Z_p\to\varprojlim\Z/p^n$ is an isomorphism of topological rings and that $\Z_{(p)}$ is dense in $\Z_p$ (so the $\Z_\ell$ of
   Chapter 3 is the $\Z_p$ of this chapter at $p=\ell$).
3. By Newton's iteration find $\sqrt{-1}\in\Z_5$ mod $5^4$ (answers $182$, $443$), the roots of $X^2+X+1$ in $\Z_7$ mod $49$ ($18$, $30$) and
   $\sqrt{-3}\in\Z_7$ mod $7^3$ ($37$, $306$). Show that $182$ is the Teichmuller lift of $2$ mod $5^4$ and deduce $\Z_7[\zeta_3]\simeq\Z_7\times\Z_7$.
4. Prove that $u\in\Z_2^\times$ is a square iff $u\equiv1\pmod8$. List the seven quadratic extensions of $\Q_2$, show that $\Q_2(\sqrt{-3})=\Q_2(\sqrt5)$ is
   the unramified one, and compute the ramification groups of $\Q_2(i)/\Q_2$ and $\Q_2(\sqrt2)/\Q_2$ and their conductor exponents $2$ and $3$;
   compare with the conductors $4$ and $8$ of $\chi_{-4}$ and $\chi_2$.
5. Show that $\log$ and $\exp$ give $1+p\Z_p\simeq p\Z_p$ for $p$ odd and $1+4\Z_2\simeq4\Z_2$, but not $1+2\Z_2\simeq2\Z_2$. Deduce the structure of
   $\Q_p^\times$ and of $\Q_p^\times/(\Q_p^\times)^2$.
6. Compute $\Q_7^\times/(\Q_7^\times)^3$ and decide which of $2,-1,6,14,7^3\cdot6$ are cubes in $\Q_7$. Do the same for ninth powers in $\Q_{19}$ with
   $2,8,-1$ (valuations of the class $c$: $0,1,2$).
7. Check the paper's claim in Lemma lem:tamagawa-exp: for $x\in\Q_q^\times$ and $\ell\ne q$, $x$ is an $\ell^t$-th power in $\Q_q^{\mathrm{ur}}$ iff $\ell^t\mid v_q(x)$.
   Apply it to 11a1 at $q=11$ ($n_{11}=5$): $\rho\bmod5$ is unramified at $11$ and $\rho\bmod25$ is not. Compare with $E(\Q)\simeq\Z/5$.
8. Check the paper's claim $\Frob^{-1}t\,\Frob=t^{q^{-1}}$ (proof of Lemma lem:tamfactor) at finite level: in $\Gal(\Q_q(\mu_{\ell^k},q^{1/\ell^k})/\Q_q)$
   (item 5.8) compute $\Frob\,t\,\Frob^{-1}$ and $\Frob^{-1}t\,\Frob$ for $(q,\ell,k)=(7,3,2)$ and $(2,3,2)$. Then prove $\Phi\,t\,\Phi^{-1}=t^{q^{-1}}$ for the
   geometric Frobenius.
9. Check the paper's claim that "the restriction of $\kappa$ to $I$ is $n$ times the tame character" (Lemma lem:tamfactor), with
   $\kappa$ the Kummer cocycle of $q_E$, $v_q(q_E)=n$. Show that $c'=\kappa(\Frob)$ changes by $qn\,t_\ell(\sigma)$ when $\Frob$ is replaced by $\Frob\sigma$
   ($\sigma\in I$) and by $(q-1)z$ when the roots are changed, and that $\min(v_\ell(n),v_\ell(q-1),v_\ell(c'))$ is independent of all choices.
10. For 11a1 ($j=-2^{12}31^3/11^5$) and $q_E=j^{-1}+744j^{-2}+356652j^{-3}+\dots$ show $v_{11}(q_E)=5$ and $q_E11^{-5}\equiv-1\pmod{11}$; deduce that $q_E$ is a
    fifth power in $\Q_{11}$ and that $v_5(c)=1=v_5(11-1)$ (the data entering Chapter 16, Exercise 10).
11. Show that $I_K=I_{\Q_p}$ for $K/\Q_p$ finite unramified and that this fails for $K=\Q_p(\sqrt p)$ (index $2$). Check the paper's claim
    "the unramified quadratic extension of $\Q_q$ ... does not change the inertia group".
12. For $\rho=\begin{psmallmatrix}\chi_\ell&\kappa_x\\0&1\end{psmallmatrix}$ compute $N$ (7.2) and $\mathrm{WD}(\rho)$; show $\mathrm{WD}(\rho)\simeq\mathrm{sp}(2)$ if $v_p(x)\ne0$ and
    $\simeq1\oplus\|\cdot\|$ (with $N=0$) if $x$ is a unit. Show that the twist by an unramified quadratic $\varepsilon$ has corner $\varepsilon\kappa_x$ (Part 15,
    N1).
13. Compute $a(\mathrm{sp}(2)\otimes\mu)=1$ and $a(\mathrm{sp}(2)\otimes\mu\chi)=2$ for $\chi$ tamely ramified quadratic, and $a=4$ for $\chi=\chi_{-4}$ at $2$. Check the
    paper's claim in the proof of Lemma lem:twist (iii) that the twist of an unramified twist of Steinberg by a ramified
    quadratic character has conductor exponent $2$ ($q$ odd).
14. Show $\ad\mathrm{sp}(2)\simeq\mathrm{sp}(3)\otimes\|\cdot\|^{-1}$ and $L(\ad\mathrm{sp}(2),s)=(1-q^{-1-s})^{-1}$. Show that with the arithmetic Frobenius one gets
    $(1-q^{1-s})^{-1}$, and check the paper's claims that at a multiplicative prime $e_\ell(E,q)=0$ and $L_q(A_f,1)^{-1}=1-q^{-2}$
    (Definition def:terms, Lemma lem:fpr).
15. Check the paper's claim in Lemma lem:euler for types $\mathrm{IV}$, $\mathrm{IV}^*$, $\mathrm{II}$, $\mathrm{II}^*$: if $\rho(I_q)$ is cyclic of order $3$ or $6$ ($q\ne3$, $\det=1$)
    then $L(\ad\rho,s)^{-1}=1-\chi_{-3}(q)q^{-s}$; and the analogue with $\chi_{-4}$ for order $4$. For $q=2$ and order $3$ deduce $P_2(X)=1+2X$ and
    $e_3(E,2)=1$ (Remark rem:wild).
16. Check the paper's claim in Lemma lem:IV that an inertia image of order $3$ at $q\ge5$ is tame and cyclic; show that at $q=3$ an
    inertia image of order $3$ is necessarily wild.
17. For $\rho(I_q)$ cyclic of order $4$ with $\det=1$: show that $V\otimes\Q_\ell(i)$ is a sum of two characters of $W_{\Q_q}$ if $q\equiv1\pmod4$ and is
    induced from the unramified quadratic extension if $q\equiv3\pmod4$.
18. (Harder) Prove Grothendieck's monodromy theorem (7.2) for $\rho\colon G_{\Q_p}\to\GL_2(\Z_\ell)$, $\ell$ odd: show that $\rho(P_p)$ embeds in $\GL_2(\F_\ell)$,
    that $\rho$ restricted to $I_p\cap\rho^{-1}(1+\ell M_2(\Z_\ell))$ factors through $t_\ell$, and that $N$ is nilpotent. Deduce: $\rho(I_p)$ finite iff $N=0$.

## 12. Dependencies and forward pointers

Results from earlier chapters used here (by chapter label only):
* Chapter 1 (`ch:groups`): profinite groups, $\Z_p$ and $\hat\Z$ as inverse limits, pro-$p$ groups and their maps to groups of order
  prime to $p$ (5.2, 5.6, 5.7), semidirect products (5.4(iii)), $1+\ell M_n(\Z_\ell)$ pro-$\ell$ and torsion-free for $\ell$ odd (5.7, 7.2).
* Chapter 2 (`ch:rings`): $v_p$, $|\cdot|_p$, Ostrowski and the product formula (1.1, 1.2), $\Z_{(p)}$ and reduction, $(\Z/p^k)^\times$ and
  lifting the exponent (2.5), finite fields, $\ell$-th powers in $\F_q^\times$ and the class $c$ (2.7, 6.2), the identity of 9.1 (11.4), the
  values $v_\ell(\cdot)$ of the omitted factors (9.4).
* Chapter 3 (`ch:modules`): DVRs, $\Z_\ell$ algebraically, completions of Noetherian rings (1.3(iii), 1.4(ii)), finitely generated
  modules over a DVR (3.2), $\Q_\ell/\Z_\ell$.
* Chapter 4 (`ch:reps`): unipotent elements and their invariants (9.1 there), commutants (9.2 there), the table of cyclic
  inertia shapes (9.3 there), reduction mod $3$ of order-$3$ elements (9.4 there), $\ad V$, $\End V=V\otimes V^\vee$, Schur's lemma (used in 9.5(iii) here),
  induction (9.2(ii)).
* Chapter 5 (`ch:galois`): finite and infinite Galois theory, the translation theorem (4.4, 5.5), finite fields and
  $G_{\F_q}\simeq\hat\Z$, Kummer theory for fields containing $\mu_n$, the affine group of $x^n-a$ (5.8), the $\ell$-adic Kummer cocycle and
  galois:kummer-finite-field (6.1, 6.2), quadratic extensions (6.3), the cyclotomic character, conventions C2 to C6.
* Chapter 6 (`ch:ant`): $e,f$ for number fields, Dedekind-Kummer, decomposition and inertia groups and Frobenius (3.4, 3.5),
  convention 3.7, 3.11 and 3.12 (finite-level tame relation; 5.4, 5.6 here are the profinite forms), $\Z_3[\zeta_3]$ and
  $\Z_\ell[\zeta_3]$ (2.3(g), 3.3(b)), quadratic characters and their conductors (6.4), Dirichlet characters as Galois characters
  (6.5(iii)).

Black boxes imported from later chapters (stated with a forward `\Cref`, never used in a proof of an earlier item): Hilbert 90
and $H^1(K,\mu_n)\simeq K^\times/(K^\times)^n$ (Chapter 17: 6.1(ii)); the Tate curve and the shape of $T_\ell E$ at multiplicative primes
(Chapters 10, 11: 7.6's last sentence); Kraus's theorem and the Kodaira-type dictionary (Chapters 10, 11: 5.7, 9.4 last column, 9.5);
the conductor of an elliptic curve equals the Artin conductor of $V_\ell E$ (Chapter 10: 8.4); independence of $\ell$ of the
Weil-Deligne representation of $V_\ell E$ (Chapters 11, 15: 7.4(iv)); the symmetric square normalisation $L(\Sym f,s)=L(A,s-1)$ and
PARI's $P_q$ (Chapter 19: 9.5(ii)).

Forward pointers (chapters that use this one):
* Chapter 8 and Chapter 9 (`ch:curves`, `ch:ellcurves`, outlined in parallel): only $\Q_p$, $\Z_p$, Hensel (points over $\Z_p$ and reduction)
  and the arithmetic Frobenius of 4.3 (the characteristic polynomial $X^2-a_pX+p$ is for $\Frob$ on $V_\ell E$); nothing about elliptic
  curves is done here.
* Chapter 10 (`ch:reduction`): minimal models over $\Z_p$, Hensel (2.1), $E_1(\Q_p)$ (2.5 for formal-group style filtrations), the Tate
  curve over $\Q_p$ and over the unramified quadratic extension (4.1, 4.4), $v_q(q_E)$ and the unit part (2.7, 2.8, 6.2), tame versus wild
  at $2$, $3$ (5.7, 8.3), the conductor exponent (8.4), quadratic twists locally (6.3, 6.4).
* Chapter 11 (`ch:galrep`): Lemma lem:tamagawa-exp in full (6.2(v), 7.6), Lemma lem:IV and Remark rem:types (5.6, 9.2, 8.3(v)), the
  Serre conductor (8.3(v), 8.4), Grothendieck's theorem and Neron-Ogg-Shafarevich (7.2), unramified base change (4.4).
* Chapter 15 (`ch:modgalrep`): Weil-Deligne representations, local $L$- and $\epsilon$-factors, $\mathrm{sp}(2)$ and its twists, the
  classification 7.5(ii), (iii) (principal series, Steinberg, supercuspidal on the Galois side), conductors 8.4, 9.3.
* Chapter 16 (`ch:cohomology`): exactly the imported facts of its tame-inertia-example and model-setting: 4.2(i) ($G/I\simeq\hat\Z$), 4.5
  ($\chi_\ell(\Frob)=q$), 5.3(ii) to (iv), 5.4(ii), 6.2(ii).
* Chapter 17 (`ch:galcoh`): Kummer theory over $\Q_p$ (6.1, 6.2), $\widehat{\Q_p^\times}$ (2.7(v)), the unramified class $\kappa_u$ (6.2(iii)), the
  Frobenius lift of 5.5, $H^1_{\mathrm{ur}}$ via $G/I\simeq\hat\Z$ (4.2), the local Euler characteristic count (2.7(iv)).
* Chapter 18 (`ch:blochkato`): $V^{I_p}$, $L_p(V,s)$ with $\Phi$ (8.1, 8.2), $L_p(V(1),s)=L_p(V,s+1)$.
* Chapter 19 (`ch:lfunctions`): the convention 8.2, the shapes table 9.4, the adjoint computations 9.1 to 9.3, the wild primes 9.5.
* Chapter 20 (`ch:congruence`): the factor $1-p^{-2}$ (9.3(iii)) and Wiles's level-raising factor (9.1) in Theorem thm:dfg14.
* Chapters 21, 22 (`ch:paper`, `ch:computation`): convention L3/L6 (Chapter 21's C2), 5.4, 6.2, 9.4; the Tate parameter and its unit
  part computed with PARI (2.8(c)).

## 13. Notes for the writer

### 13.1 Conventions (to be set as `convention` environments at first use)
* **Both Frobenii, named every time.** Convention L3 in Section 4 (item 4.3). In every display write $\Frob$ (arithmetic) or $\Phi$
  (geometric), never an unqualified "Frobenius" in a formula. Group theory ($t$, conjugation, the matrices of Lemma lem:tamfactor,
  $\chi_\ell(\Frob)=q$) uses $\Frob$; $L$-factors use $\Phi$. State the one-line dictionary: arithmetic eigenvalue $\lambda$ is geometric
  eigenvalue $\lambda^{-1}$. The book's $\Frob_p$ macro means the arithmetic one, as in Chapters 5, 6, 16 and 21.
* **The tame relation, in exactly these forms:** $\Frob\,t\,\Frob^{-1}=t^{q}$; equivalently $\Frob^{-1}t\,\Frob=t^{q^{-1}}$; for the geometric one
  $\Phi\,t\,\Phi^{-1}=t^{q^{-1}}$. Exponents live in $\prod_{\ell\ne p}\Z_\ell$ (on $I/P$) or in $\Z_\ell$ (on $I^{(\ell)}$). Give the finite-level check 5.8.
* **The sign in the Weil-Deligne relation:** $r(w)Nr(w)^{-1}=\|w\|N$ with $\|\Frob\|=q$, $\|\Phi\|=q^{-1}$; so $\Frob N\Frob^{-1}=qN$ and $\Phi N\Phi^{-1}=q^{-1}N$.
  PLAN.md's "$\Frob\,N\,\Frob^{-1}=p^{-1}N$" is the geometric form (Part 15, B-a); write both and say which is which. Check it on $\mathrm{sp}(2)$
  and on the Tate shape (7.6): $\rho(\Frob)$ multiplies $e_1$ by $\varepsilon q$ and $e_2$ by $\varepsilon$, and $N$ maps $e_2$ to $e_1$.
* **Normalisation of local factors:** $L(V,s)=\det(1-\Phi q^{-s}\mid V^{I})^{-1}$. Consequences to display: $L(\Q_\ell(1),s)=(1-q^{-1-s})^{-1}$,
  $L(V(1),s)=L(V,s+1)$, $L(V_\ell E,s)=L_p(E,s+1)$, $L(V_\ell E^\vee,s)=L_p(E,s)$, $L(\ad\mathrm{sp}(2),s)=(1-q^{-1-s})^{-1}$. The paper's $L_p(\Sym f,s)=L_p(A_f,s-1)$
  and PARI's $P_q$ are Chapter 19's; mention them only in 9.5(ii) with a `\Cref{ch:lfunctions}`.
* **The choice of $\zeta$** (generator of $\Z_\ell(1)$) enters $t_\zeta$ and $N$; $N$ is defined up to $\Z_\ell^\times$; none of $V^I$, $a$, $L$ depends on it.
* **Uniformiser-dependence:** $t_\ell$ on $I_K$ is independent of $\varpi$; the cocycle $\kappa_\varpi$ on $G_K$ is not (it changes by $\kappa_u$); the
  Frobenius lift of 5.5 depends on $\varpi$ and on the roots.
* **Notation clash:** $q$ is both $\#k_K$ and the paper's prime; $\chi_q$ is the quadratic character of conductor $q$ (Chapter 5, C3) and $\chi_\ell$
  the cyclotomic character (important_notes.md point 32); write $\theta_2$ for the order-two character of inertia and $\eta_{\mathrm{ur}}$ for the
  unramified quadratic character; $\varepsilon$ is reserved for the unramified character of the Tate shape (paper's notation); $\epsilon$ for
  $\epsilon$-factors; $e$ is both a ramification index and the basis vector $e=e_1\otimes e_2^\vee$ (paper): say so.

### 13.2 Pitfalls
* Hensel (simple-root form) needs $f'(a_0)$ a unit; give $X^2-p$ and $X^2+7$ over $\Z_2$ (the Newton form succeeds where the simple form
  fails). $\Q_p^{\mathrm{ur}}$ is not complete; Hensel holds there by passing to a finite level (4.2(iii)); say this, because Lemma
  lem:tamagawa-exp uses it.
* "$u$ is an $\ell^k$-th power in $\F_q^\times$" for $u\in\Z_q^\times$ means its reduction (important_notes.md point 31); by 2.7(ii) this is equivalent to
  $u\in(\Z_q^\times)^{\ell^k}$ for $\ell\ne q$. False for $\ell=q$ (e.g. $1+q$ is not a $q$-th power in $\Z_q$ for $q$ odd).
* $\Z_\ell[\zeta_3]$ is $\Z_\ell[X]/(X^2+X+1)$, not a domain for $\ell\equiv1\pmod3$ (2.3(c); important_notes.md point 12).
* $I/P$ has no quotient of order $p$: an inertia image of order $p$ is wild. At $q=3$ an image of order $3$ is wild; at $q=2$ an image of
  order $3$ is tame. Do not write "tame since $q\ge5$" when "$q\nmid\#\rho(I)$" is meant.
* Grothendieck's theorem gives $N$ only on an open subgroup of $I$; $\rho(I)$ itself can be $\{\pm1\}\times(\text{unipotent})$ (the $\mathrm{I}_n^*$ shape),
  and $V^{I}$ must be computed as $(\ker N)^{r(I)}$ (8.1), not as $\ker N$.
* The Artin conductor of a twist: $a(\mathrm{sp}(2)\otimes\chi)=2a(\chi)$, not $a(\chi)+1$; and $a(V\otimes\chi)\ne a(V)$ in general for ramified $\chi$.
  Lemma lem:twist (ii) at $q=3$: twisting a good or multiplicative curve by the tame $\chi_3=\chi_{-3}$ gives exponent $2$, but a general
  additive curve at $3$ can have exponent up to $5$ (point 28).
* Local class field theory normalisations: say "uniformiser to arithmetic Frobenius" and give the sign $u\mapsto u^{-1}$ on $\mu_{p^\infty}$
  (6.5(ii)); avoid using LCFT in any proof the paper needs (only 6.5(iii) for characters, as a statement).
* The Swan conductor is an integer only by a theorem (Artin); do not present 8.3(ii) as obvious.
* Do not claim Krasner's lemma or the equivalence of norms as proved (3.1, 3.5: S).
* Do not present the Kodaira-type column of 9.4 or the inertia images of elliptic curves as proved here: they are
  black boxes from Chapters 10 and 11.

### 13.3 What to leave to neighbouring chapters
* Chapter 2: $v_p$, $|\cdot|_p$ on $\Q$, Ostrowski, $(\Z/p^k)^\times$, powers in $\F_q^\times$, the class $c(u)$, the numerical identities of the
  omitted factors. Cite; do not redo.
* Chapter 3: $\Z_\ell$ as an algebraic completion and complete DVR, lengths, Fitting ideals, $\Q_\ell/\Z_\ell$. Chapter 7 adds only the
  analytic description and the equality 1.4(ii).
* Chapter 4: the linear algebra of unipotent and finite cyclic actions (9.1 to 9.4 there), $\ad$, Schur. Cite its table 9.3.
* Chapter 5: Kummer theory for fields containing $\mu_n$, the $\ell$-adic Kummer cocycle (its definition and cocycle identity), the
  translation theorem, finite fields. Chapter 7 adds the local field input (Hensel, inertia, valuations).
* Chapter 6: global $e,f,g$, Dedekind-Kummer, global decomposition groups, the finite-level 3.11, 3.12, $\Z_3[\zeta_3]$ as a DVR.
* Chapters 9, 10, 11: everything about elliptic curves: minimal models, reduction types, Tate's algorithm, the Tate curve itself,
  $E_q[\ell^t]$, Kraus's theorem, Neron-Ogg-Shafarevich, the proofs of Lemmas lem:tamagawa-exp and lem:IV and of Remark rem:types,
  the Serre conductor of $\bar\rho_{E,\ell}$. Chapter 7 provides the local field statements they quote.
* Chapter 15: local Langlands, local components $\pi_p$ of newforms, Carayol's theorem; Chapter 7 gives only the Galois side.
* Chapters 16, 17: group cohomology, $H^1(I,M)=M/(t-1)M$, inflation-restriction, Hilbert 90 in cohomological form, the identification of
  $H^1(K,\Z_\ell(1))$ with $\widehat{K^\times}$ and of $c'$ with the class of the unit part (Chapter 17 proves the end of Lemma
  lem:tamfactor). Chapter 7 proves only the field-level statements 6.2.
* Chapter 19: the symmetric-square normalisation, PARI's $P_q$, $e_\ell(E,q)$, the naive factor, Lemma lem:euler in the language of
  Kodaira types.

### 13.4 How each relevant point of important_notes.md is handled
* **Point 7 (Lemma lem:tamfactor, "image of $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)$").** Items 5.5 (a Frobenius lift fixing the $\ell$-power roots of $q$)
  and 6.2(i) to (iv) (the decomposition $\kappa=n\kappa_q+\kappa_u$, $\kappa_u$ unramified with value the class of $\bar u$, the indeterminacy
  $(n,q-1)\Z_\ell$) give the field-theoretic half of the fix; Exercise 9 makes the reader check it. The cohomological statement is
  Chapter 17's. A `paperlink` at 6.2 quotes the paper's sentence and the corrected reading.
* **Point 8 (Lemma lem:tamagawa-exp, notation and "up to units").** Item 6.2(v) is the precise statement ("$x$ is an $\ell^t$-th power in
  $\Q_q^{\mathrm{ur}}$ iff $\ell^t\mid v_q(x)$"), with 4.2(iv) for the units; the chapter calls the Tate parameter $q_E$ and its unit part $u$, as
  Chapters 10, 11, 21 do. Exercise 7.
* **Point 11 (geometric versus arithmetic Frobenius).** Conventions L3, L6, item 4.3 and 8.2(iv): both Frobenii are defined, the
  $L$-factor uses $\Phi$, the group theory uses $\Frob$; 9.3(iii) shows that the paper's $1-q^{-1-s}$ requires $\Phi$; 8.2(iii) gives
  $L(V(1),s)=L(V,s+1)$ (Lemma lem:fpr). Exercises 8, 14. A `warning` environment in Section 8 repeats the point.
* **Point 28 (Lemma lem:twist, "the conductor exponents are the standard ones for $q$ odd (tame)").** Items 6.3, 6.4(ii), (v), 8.3(iii),
  9.3(ii): quadratic characters of $\Q_q$, $q$ odd, are tame of exponent $1$; twisting a tame representation by them keeps it tame; at
  $q=3$ general additive reduction can be wild (5.7, 9.5(i)). The `paperlink` at 9.3 says exactly which exchanges are tame.
* **B1 (which Frobenius has eigenvalues $\alpha,\beta$ on $V_\ell E$).** Item 8.2(v) states: the arithmetic Frobenius on $V_\ell E$ has
  eigenvalues $\alpha,\beta$; the geometric one $\alpha^{-1},\beta^{-1}$; the geometric one on $V_\ell E^\vee$ has $\alpha,\beta$; on $\ad V$ the set $\alpha/\beta,1,\beta/\alpha$
  is the same for both. Part 15, B-b, records that the slip is still present in the Chapter 21 outline's C2(b).
* **Points 12, 13, 22, 29, 31, 32 (adjacent).** 12: 2.3(c), (g) and the pitfall above; 13: not this chapter's (Chapter 4, 6 notation);
  22: 9.2, 9.4 give the complete list of $V^{I}$ and conductors for every tame additive shape, which is the corrected Remark
  rem:types on the Galois side; 29: not this chapter's (Weierstrass models); 31: 2.7(ii) and the pitfall above; 32: the notation note in 13.1.

### 13.5 References and bibliography
`SerreLocalFields`, `SerreCourse`, `SerreAbelian`, `SerreLinearReps`, `Neukirch`, `Koblitz`, `CasselsFrohlich`, `MilneCFT`, `NSW`,
`SilvermanATAEC`, `Kraus90`, `Washington`, `DFG04` are in `refs.bib`. Add to `bib/ch07.bib` (complete entries; check against the
sources): `Deligne73` (P. Deligne, "Les constantes des equations fonctionnelles des fonctions L", Modular functions of one variable
II, Lecture Notes in Math. 349, Springer, 1973, 501-597), `Tate79` (J. Tate, "Number theoretic background", Automorphic forms,
representations and L-functions, Proc. Sympos. Pure Math. 33, Part 2, AMS, 1979, 3-26), `SerreTate68` (J.-P. Serre and J. Tate, "Good
reduction of abelian varieties", Ann. of Math. 88 (1968), 492-517), `Rohrlich94` (D. E. Rohrlich, "Elliptic curves and the Weil-Deligne
group", Elliptic curves and related topics, CRM Proc. Lecture Notes 4, AMS, 1994, 125-157). The `Deligne` key of `refs.bib` is the
Bourbaki talk on modular forms and $\ell$-adic representations, not the $\epsilon$-factor paper; do not confuse them. No theorem
numbers are cited from these works in this outline; the writer cites sections only unless checked against the source.

## 14. Verification log (computations done for this outline)

Python scripts `/tmp/ch07/check1.py`, `/tmp/ch07/check2.py` and hand computations.
* Hensel lifts by Newton iteration: $\sqrt{-1}\in\Z_5$ is $182$ or $443$ mod $5^4$ ($182^2+1=53\cdot625$); roots of $X^2+X+1$ mod $49$: $18,30$; $\sqrt{-3}$ mod
  $7^3$: $37,306$; $\sqrt2$ mod $7^3$: $108,235$.
* Teichmuller lifts in $\Z_5$ mod $5^4$: $\omega(1,2,3,4)=1,182,443,624$, each with fourth power $1$; so $\omega(2)=\sqrt{-1}$.
* Unit indices: for $p\in\{7,13,19,31\}$, $\ell\in\{3,5\}$, $k\in\{1,2\}$, the index of $\ell^k$-th powers in $(\Z/p^3)^\times$ equals $\ell^{\min(k,v_\ell(p-1))}$
  (consistent with 2.7(ii), (iv)); $\ell^k\cdot\ell^{\min(k,v_\ell(p-1))}=\ell^k\gcd(\ell^k,p-1)$ for $p\le37$, $k\le3$ (2.7(iv), Euler characteristic
  form).
* 11a1: $j=-2^{12}31^3/11^5$; with $q_E=j^{-1}+744j^{-2}+356652j^{-3}$, $v_{11}(q_E)=5$ and $q_E11^{-5}\equiv10\equiv-1\pmod{11}$ (by hand:
  $2^{12}\equiv4$, $31^3\equiv3$, product $\equiv1$). The fifth powers in $\F_{11}^\times$ are $\{\pm1\}$.
* Cubes mod $7$: $\{1,6\}$.
* Tame relation in the affine model of $\Gal(\Q_q(\mu_{\ell^k},q^{1/\ell^k})/\Q_q)$: $\Frob\,t\,\Frob^{-1}=t^q$ and $\Frob^{-1}t\,\Frob=t^{q'}$, $qq'\equiv1$, for
  $(q,\ell,k)=(7,3,2),(11,5,1),(13,3,2),(2,3,2)$ (outputs $t^7,t^4$; $t,t$; $t^4,t^7$; $t^2,t^5$).
* $\mathrm{sp}(2)$ with $\Phi=\operatorname{diag}(1,q^{-1})$, $N=E_{10}$: $\Phi N\Phi^{-1}=q^{-1}N$; $[N,E_{01}]=-h$, $[N,h]=2N$, $[N,N]=0$; $\Phi$-eigenvalues on $E_{01},h,E_{10}$:
  $q,1,q^{-1}$ (symbolic, sympy). Hence $\ad\mathrm{sp}(2)\simeq\mathrm{sp}(3)\otimes\|\cdot\|^{-1}$ and $L(\ad\mathrm{sp}(2),s)=(1-q^{-1-s})^{-1}$.
* Tate shape twisted by $\varepsilon$: $\begin{psmallmatrix}\chi\varepsilon&\varepsilon\kappa\\0&\varepsilon\end{psmallmatrix}$ is a homomorphism when $\kappa(gh)=\kappa(g)+\chi(g)\kappa(h)$, while
  $\begin{psmallmatrix}\chi\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$ would need $\kappa(gh)=\varepsilon(h)\kappa(g)+\chi(g)\varepsilon(g)\kappa(h)$ (hand computation; Part 15, N1).
* Quadratic extensions of $\Q_2$: square classes $\pm1,\pm5,\pm2,\pm10$; $(-3)\cdot5=-15\equiv1\pmod8$ so $\Q_2(\sqrt{-3})=\Q_2(\sqrt5)$, unramified; $3\cdot(-5)\equiv1\pmod8$
  so $\Q_2(\sqrt3)=\Q_2(\sqrt{-5})$. Ramification groups: $\Q_2(i)$, $\pi=1+i$, $\sigma(\pi)-\pi=-2i$ of $v_L=2$: lower jump $1$, $a=2$; $\Q_2(\sqrt2)$: $v_L(-2\sqrt2)=3$, jump
  $2$, $a=3$; these match the conductors $4$ and $8$.
* Conductor exponents: $a(\mathrm{sp}(2)\otimes\mu)=0+2-1=1$; $a(\mathrm{sp}(2)\otimes\chi)=2a(\chi)+0-0$; finite cyclic tame inertia without fixed vectors in
  dimension $2$: $a=2$. Omitted factor at $2$ for order-$3$ inertia: $L(A,s)^{-1}=1+2^{-s}$, $P_2(X)=1+2X$, $e_3=v_3(3/2)=1$.
* Not verified (recalled): the theorem and section numbers of Serre's Local Fields, Neukirch, Deligne73, Tate79 and Rohrlich94;
  the outline cites chapters and sections only, and the writer must check them before citing anything finer.

## 15. Points for important_notes.md

### 15.1 New points about the paper

**N1. Lemma lem:tamfactor, proof, first sentence: in the nonsplit case the corner of the matrix is $\varepsilon\kappa$, not the Kummer class
$\kappa$.** Location: "$T$ has a basis $e_1,e_2$ in which $G=G_{\Q_q}$ acts through matrices $\begin{psmallmatrix}\chi_\ell\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$, with
$\varepsilon$ unramified of order at most $2$ and $\kappa$ the Kummer class of $q_E$". Problem: for nonsplit reduction $T_\ell E\simeq T_\ell E_{q_E}\otimes\varepsilon$,
and $T_\ell E_{q_E}$ has the matrices $\begin{psmallmatrix}\chi_\ell&\kappa\\0&1\end{psmallmatrix}$ with $\kappa$ the Kummer cocycle of $q_E$; tensoring with $\varepsilon$ gives the
corner $\varepsilon\kappa$. A map $g\mapsto\begin{psmallmatrix}\chi_\ell\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$ with $\kappa$ a Kummer cocycle
($\kappa(gh)=\kappa(g)+\chi_\ell(g)\kappa(h)$) is not a homomorphism unless $\varepsilon=1$. Fix: write the corner as $\varepsilon\kappa$ ("with $\varepsilon$ unramified of
order at most $2$ and $\kappa$ a Kummer cocycle of $q_E$"), or say "$\varepsilon\kappa$ is the cocycle"; then $c'=\varepsilon(\Frob)\kappa(\Frob)=\pm\kappa(\Frob)$. Effect: none.
On $I_q$, $\varepsilon=1$, so $n'$ is unchanged; $v_\ell(c')$ is unchanged by the sign; the formula for $\Tam_q$ stands. (The Chapter 16 outline's
item cocycle-in-the-corner already reads the paper's matrix this way: "the cocycle is $\varepsilon\kappa$".) Confidence: high (two-line
computation; also in Part 14).

**N2 (observation, not an error; to be entered only if Kraus90 confirms the inertia claim). Lemma lem:euler and Remark rem:wild:
the $q\ge5$ hypothesis is used only for the shape of the inertia image; the type IV value at $2$ is the same formula.** A remark for
Chapters 19 and 21. The proof for the types $\mathrm{II},\mathrm{II}^*,\mathrm{IV},
\mathrm{IV}^*$, $\mathrm{III},\mathrm{III}^*$ uses only that $\rho(I_q)$ is cyclic of order $m$ with $q\nmid m$ (item 9.2). At $q=2$ with inertia image cyclic of
order $3$ (tame at $2$), or of order $6$ generated by $-\sigma$ (the sign is wild but disappears on $\ad V$, and Frobenius still acts on
$\langle\sigma\rangle$ by the $2$-nd power), it predicts $P_2(X)=1+2X$ and $e_3(E,2)=v_3(2-\chi_{-3}(2))=1$, which is what Remark rem:wild reports from PARI for type $\mathrm{IV}$ at $2$
and what Proposition prop:forms needs ("$e_3(E,2)\ge1$ for all $92{,}812$ curves of type $\mathrm{IV}$ or $\mathrm{IV}^*$ at $2$"). If Chapters 10 and 11
confirm that types $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ always have cyclic inertia image of order $3$ or $6$ (I believe this is in Kraus90, but did not verify
it), the exception in Proposition prop:forms disappears and the "PARI's factor at $2$ is $1+2X$ for every one of them" becomes a
theorem. Fix (optional): add to Remark rem:wild "for type $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ the image of inertia is cyclic of order $3$ or $6$, and the proof of Lemma lem:euler applies verbatim". Confidence: high for the computation; low (unverified) for the claim
about the inertia image at $2$, which must be checked against Kraus90 before anything is written in the paper.

No other new problem was found in the paper in this chapter's area. The local statements of Lemmas lem:tamagawa-exp, lem:IV,
lem:twist (iii), lem:euler, lem:tamfactor and Remark rem:wild were rechecked here; the known issues are points 7, 8, 11, 12, 13, 22,
28, 29, 31, 32 of important_notes.md.

### 15.2 Book-internal inconsistencies

* **B-a. PLAN.md, Chapter 7 entry: "$\Frob\,N\,\Frob^{-1}=p^{-1}N$".** With the book's convention ($\Frob$ arithmetic: Chapter 5 C2, Chapter 6 3.7,
  Chapter 16, Chapter 21 C2) the relation is $\Frob\,N\,\Frob^{-1}=pN$; the PLAN formula is the geometric form $\Phi N\Phi^{-1}=p^{-1}N$. This
  outline states both (convention L4). Action: none needed in the chapters; if PLAN.md is edited, write "$\Phi N\Phi^{-1}=p^{-1}N$ for the
  geometric Frobenius $\Phi$".
* **B-b. Chapter 21 outline, convention C2(b), still carries the slip recorded as B1.** It says that on $V_\ell E$ the geometric Frobenius
  has eigenvalues $\alpha,\beta$ and the arithmetic one $p/\alpha=\beta$, $p/\beta=\alpha$, "the same set", and that $L_p(V_\ell E,s)=(1-a_pp^{-s}+p^{1-2s})^{-1}$ with
  the geometric Frobenius. In fact the arithmetic Frobenius on $V_\ell E$ has eigenvalues $\alpha,\beta$, the geometric one $\alpha^{-1}=\beta/p$, $\beta^{-1}=\alpha/p$
  (a different set), so $\det(1-\Phi p^{-s}\mid V_\ell E)^{-1}=(1-a_pp^{-1-s}+p^{-1-2s})^{-1}=L_p(E,s+1)$; the factor $(1-a_pp^{-s}+p^{1-2s})^{-1}$ is that of
  $V_\ell E^\vee$ (Chapter 6, 3.7; this outline, 8.2(v)). Nothing about $\ad V$ changes. Action: the Chapter 21 writer must use 8.2(v).
* **B-c. Chapter 21 outline, A2.7 step (1).** It repeats the paper's matrix with corner $\kappa$ "the Kummer class of $q_E$"; with N1 the corner
  is $\varepsilon\kappa$ (Chapter 16's cocycle-in-the-corner already says so). Step (7)'s indeterminacy argument is unaffected. Action: the
  Chapter 21 writer adds the factor $\varepsilon$.
* **B-d. Chapter 6 outline, 3.10(v) and 4.7(iv), 7.4, 5.7(ii); Chapter 2 outline, 11.2(iii); Chapter 3 outline, 6.4; Chapter 16 outline,
  imported facts.** All deferrals to Chapter 7 are honoured by items 3.5, 3.3(b), 3.4, 6.5(iii), 1.3, 1.4(ii), 5.3, 5.4, 6.2 respectively;
  no conflict found. The normalisation of the Artin map in Chapter 6, 5.6(iii) (uniformiser to arithmetic Frobenius, units acting
  by $u^{-1}$ on $\mu_{p^\infty}$) agrees with 6.5(ii) here.
* **B-e. Chapter 4 outline, table 9.3, row "unipotent".** It gives the mod $3$ dimension of $(T/3T)^{I}$ for type $\mathrm{I}_n$ as "1 if $3\nmid n$, 2 if
  $3\mid n$"; this agrees with 6.2(v) and 7.6(iv) here ($I$ acts trivially on $T/3T$ iff $3\mid n$). No conflict; recorded because the same fact
  is stated in three chapters (4, 7, 11) and must stay consistent.
