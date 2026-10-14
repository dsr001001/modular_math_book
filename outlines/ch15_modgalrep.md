# Chapter 15: Galois representations of modular forms, level lowering and congruences (`ch:modgalrep`, `chapters/ch15_modgalrep.tex`)

Stage 1 line-up. Part IV (Modular forms and modular curves). Target length 2,770 lines of LaTeX (card excluded; see Part 3),
inside the 2,800 lines that PLAN.md Section 7.3 allows for this chapter.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2 to 12
outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book or paper and chapter
or section; a theorem number only where the outline author is sure or where the paper itself cites it, otherwise the section,
and numbers marked "(verify)" must be checked before they are printed); the paper's use by its `\label` names, or "background".
Every computation quoted below (the congruences of the Example of Section 3 for all $n$, curve-level twist pairs, levels of
twists, Serre conductors, level-raising conditions and the congruent forms they predict, the oldform construction of Lemma
lem:old on two examples, the congruence number of 99a1, the new example 52a1 for case (a) at $q=2$, the $1{,}051$ curves with
type $\mathrm{IV}$ or $\mathrm{IV}^*$ at $2$) was checked with PARI/GP 2.17 through `cypari2` against Cremona's `ecdata` files
`allcurves`, `degphi`, `galrep` for conductors below $10{,}000$ (verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

Section 3 of the paper proves Theorem thm:qual by attaching Galois representations to newforms, lowering the level of a
residual representation, twisting, and converting a congruence between eigenforms into divisibility of the congruence number.
Section 4 reads the same mechanism quantitatively: the level-raising Euler factor of Theorem thm:dfg14, the twist map of
Theorems thm:twist and thm:quant, and the identification of the lattice $M_{f,\lambda}$ of Diamond, Flach and Guo with $T_\ell E$.
This chapter supplies all of it. Concretely it must deliver:

1. **The representation $\rho_{f,\lambda}$ of a newform of weight $2$** (Eichler-Shimura construction through $A_f$; Deligne for higher
   weight as a statement): unramified outside $N\ell$, $\tr\rho(\Frob_p)=a_p$, $\det=\chi_\ell$, odd, absolutely irreducible; lattices and
   the residual representation; congruent newforms have isomorphic residual representations (absolute irreducibility,
   important_notes.md point 10); twists $\rho_{f^\chi}\simeq\rho_f\otimes\chi$ and the distinction between the *naive twist* $f\otimes\chi$ and
   the *newform twist* $f^\chi$ (the source of important_notes.md point 20 and of the new point N1, Part 7).
2. **The comparison with $\rho_{E,\ell}$** for $f=f_E$: $T_\ell E$ is a lattice in $\rho_{f,\ell}$; for the optimal curve the lattice $M_{f,\lambda}$ of DFG04 is
   exactly $\phi^*H^1(E,\Zl)\simeq T_\ell E(-1)$, homothetic to the dual of $T_\ell E$ in general (important_notes.md points 26 and 40, B3), so
   $\ad M_{f,\lambda}=\ad T_\ell E$ (Section 4.2 of the paper).
3. **Local-global compatibility and local components** (Carayol; Langlands, Deligne): the local Langlands correspondence for
   $\GL_2(\Q_p)$ as a statement; the local types of a weight-two newform with trivial character (unramified principal series,
   unramified twist of Steinberg with DDT Theorem 3.1(e), and for $p^2\mid N$ ramified twist of Steinberg, ramified principal series,
   supercuspidal); $\delta_p=2,1,0$; $a_p=0$ and $V^{I_p}=0$ when $p^2\mid N$ (a local proof of Atkin-Lehner's Theorem 3); the Kodaira-type
   dictionary for $f=f_E$ at $q\ge5$ (the "local components" of Lemma lem:euler); **the conductor of a quadratic twist type by type**
   (item 3.8), which gives Lemma lem:twist(iii) (Atkin-Li) and the levels in Theorems thm:qual, thm:twist and thm:quant.
4. **The representation at $\ell\nmid N$** for a newform: crystalline, finite flat residual, Fontaine-Laffaille; the
   Deligne-Fontaine description and the determination of $a_\ell\bmod\lambda$ by $\bar\rho|_{D_\ell}$ (the case $p=\ell$ of Lemma lem:old).
5. **Serre's conjecture** (statement; Khare-Wintenberger), Serre conductor and weight, $N(\bar\rho_f)\mid N$ (proved), **Mazur's principle,
   Ribet's level-lowering theorem, Carayol's lemma, and the optimal-level theorem in the form of DDT Theorem 3.15** with the
   paper's specialisation to $\bar\rho_{E',\ell}$ (trivial nebentypus: proved).
6. **Ribet's level-raising theorem** ($a_q^2\equiv(q+1)^2\pmod\lambda$; the necessity proved) and the level-raising Euler factor
   $L_q^{\nv}(A_f,1)^{-1}=\frac{q-1}q\cdot\frac{(q+1)^2-a_q^2}{q^2}$ of Theorem thm:dfg14 (statement; Chapter 20 has the proof idea).
7. **The paper's Lemma lem:crit proved in full** (PLAN.md: here; Chapter 20 restates it) and **Lemma lem:old proved in full**.
8. **The paper's Theorem thm:qual proved in full**, cases (a), (b), (c), with case (a) extended to $q=2$ (important_notes.md point 43,
   settled), the corrections of points 10 and 20 and of the new point N1; the Example (121a1, 539c1, 980i1: congruences for all $n$ by
   Sturm, point 46; correct curve-level labels, B8; 980i1 outside the hypotheses, point 21); the remark on $\ell\mid N$ and 99A1 (the
   congruence number $12$ recomputed here).
9. **The twist map and levels for Theorems thm:twist and thm:quant**, the remark after Theorem thm:quant read as level raising
   (points 16, 24, 39), and the statements of Ribet-Takahashi, Pollack-Weston and Kim-Ota (Section 1.5, Remark rem:ko(2)), with a
   one-page outline of Taylor-Wiles and $R=\T$ saying what DFG04 Theorem 3.7 needs (point 47).

### 1.2 Split with the neighbouring chapters (decided here, consistent with PLAN.md Section 4 and the written outlines)

* **Chapter 3** proves the commutative algebra: dualising an inclusion of lattices (5.7), the congruence module of a decomposition
  (5.8), the algebra-module duality for a perfect pairing $S\times\T\to R$ (9.6), Artinian algebras and idempotents (10.1 to 10.6),
  non-semisimple operators and the shift-operator model of $U_p$ (10.7(v)), common eigenvectors on tensor products (10.8), congruence
  ideals (11.1). Lemma lem:crit and Lemma lem:old here cite these by `\Cref{ch:modules}` and add only the modular input.
* **Chapter 4** proves the unique stable line of a non-split extension (3.6), Brauer-Nesbitt (5.2, 5.3), lattices, reduction and the
  homothety lemma (10.1 to 10.3), adjoint invariance under duals, twists and homotheties (7.7). Cited.
* **Chapter 5** proves Chebotarev plus Brauer-Nesbitt in the form galois:congruent-ap, with the Galois representations of newforms
  as a forward black box; **this chapter discharges that black box** (item 2.1) and restates galois:congruent-ap for newforms (2.5).
* **Chapter 6** gives coefficient fields, orders, primes $\lambda$, completions $\mathcal O_\lambda$ (its 7.1 to 7.4).
* **Chapter 7** gives the Galois side of local theory: Weil-Deligne representations, $\mathrm{sp}(2)$ and its twists, the classification of
  two-dimensional Weil-Deligne representations (7.5), invariants, $L$-factors with the geometric Frobenius (8.1, 8.2), Artin and Swan
  conductors (8.3, 8.4), $\epsilon$-factors (8.5, recalled here), the shapes table (9.4). **Chapter 15 adds the automorphic side** (local
  Langlands, local components $\pi_p$, Carayol's theorem) and the types of newforms; it does not redo any Weil-Deligne computation.
* **Chapter 11** gives everything specific to $\rho_{E,\ell}$: the Tate shape and Lemma lem:tamagawa-exp (3.2, 3.3), inertia images by
  Kodaira type and Lemma lem:IV (4.1 to 4.5, with 4.4 at $q=2$), the representation at $\ell$ for $E$ (5.1 to 5.4), the Serre conductor
  formula $a_p(\bar\rho_{E,\ell})=f_p-\dim\Phi_p[\ell]$ and its examples (6.1 to 6.3), images and Proposition prop:ns, Lemma lem:h0, the
  equivalence $\ell\notin S_f\iff$ ($E[\ell]$ irreducible and not 3Ns) for $\ell\nmid 2N$ (8.6), and the *statement* of the optimal-level theorem
  for $\bar\rho_{E,\ell}$ (10.1) with its examples (10.2), leaving "the general theorem, its proof and the trivial-nebentypus argument" to
  this chapter. **Chapter 15 proves nothing about $\rho_{E,\ell}$ that Chapter 11 proves**; where an elliptic-curve fact is needed it is
  cited (`\Cref{ch:galrep}`), and Chapter 15's examples quote Chapter 11's Serre conductors instead of recomputing them in the text.
* **Chapter 12** gives $S_2(\Gamma_0(N);\Z)$, the integral basis, Sturm's bound and **the proof that the three congruences of the
  Example hold for every $n$** (its 11.3 to 11.5, important_notes.md point 46), nebentypus (6.6), Atkin-Lehner involutions (12.1 to 12.4).
  Cited, not redone.
* **Chapter 13** (outlined in parallel) gives, per PLAN.md: Hecke operators on forms, $U_p$ on oldforms with its eigenvalues,
  stabilisations and depleted forms, the decomposition of $S_2(\Gamma_0(N))\otimes\Qbar$ into spans of $h(dz)$, strong multiplicity one,
  Atkin-Lehner's $a_p=0$ for $p^2\mid M$ (their Theorem 3), the Atkin-Li theorem in the paper's form, the twist map $\iota$ on the whole space
  and its compatibility with $T_p$, the perfect pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$, the recursion for $a_{p^k}$. **Chapter 15 cites all of
  these** and adds the Galois-theoretic content: why Atkin-Li holds (local components, item 3.8), the conductor of a twist when $q^2$
  divides the level (beyond Atkin-Li), and the reading of $\iota$ as $\rho\mapsto\rho\otimes\chi$.
* **Chapter 14** (outlined in parallel) gives $J_0(N)$, Eichler-Shimura $T_p=\Frob_p+p\Frob_p^{-1}$, $A_f$ as a quotient, modularity, the
  optimal curve, the modular degree, the congruence number, Agashe-Ribet-Stein (with 99A1 as its example), multiplicity one and
  Remark rem:free, and important_notes.md point 39. Chapter 15 cites the construction of $A_f$ and Eichler-Shimura for 2.1, and
  Agashe-Ribet-Stein for the passage $r_E\to\deg\varphi_E$; it recomputes $r(99\mathrm a1)=12$ only as data for the remark of Section 3.
* **Chapter 19** computes $L_q(A_f,s)$, $P_q$ and $e_\ell(E,q)$ (Lemma lem:euler in full); Chapter 15 gives only the local types behind the
  phrase "local components" and the level-raising factor identity (7.2).
* **Chapter 20** gives congruence ideals in $\T_{\mathfrak m}$, Lemma lem:ddt417, Lemma lem:hecke, Theorem thm:dfg14 with its proof idea (Ihara's
  lemma, degeneracy maps), DFG04 Theorem 3.7, Taylor-Wiles in outline, and **the full proofs of Theorems thm:twist and thm:quant**.
  Chapter 15 states those two theorems, proves the level and twist facts they rest on (3.8, 10.1, 10.2), and explains the remark after
  Theorem thm:quant from the Galois side; Lemma lem:crit is proved here and only restated in Chapter 20 (PLAN.md).
* **Chapter 21** (written outline) proves lem:crit, lem:old and thm:qual again in its tour; it may shorten them by pointing here, and
  must take over the corrections listed in Part 7.2.

### 1.3 Global conventions fixed in this chapter

* **C1 (newforms).** $f=\sum a_n(f)q^n$ is a normalised newform of weight $2$ on $\Gamma_0(N)$ (trivial character) unless said otherwise;
  $K_f=\Q(a_n(f):n\ge1)$, a totally real number field; $\mathcal O_f$ its ring of integers; $\lambda\mid\ell$ a prime of $\mathcal O_f$ (or of a finite
  extension $\mathcal O$, "after enlarging $\mathcal O$"), $K_{f,\lambda}$ and $\mathcal O_\lambda$ the completions, $k_\lambda$ the residue field. $\T=\T(N)$ is the **full** Hecke
  algebra of level $N$ generated over $\Z$ by all $T_n$, $n\ge1$ (so including $U_p$ for $p\mid N$), as in Section 3 of the paper; $\phi_f\colon\T\to\mathcal O_f$
  its eigencharacter. Chapter 13's notation is used throughout.
* **C2 (Frobenius).** As in Chapters 7 and 11: $\Frob_p$ is an **arithmetic** Frobenius, $\Phi_p=\Frob_p^{-1}$ the geometric one; $L$-factors use
  $\Phi_p$. The normalisation of $\rho_{f,\lambda}$: $\det(X-\rho_{f,\lambda}(\Frob_p))=X^2-a_p(f)X+p$ for $p\nmid N\ell$ and $\det\rho_{f,\lambda}=\chi_\ell$, so that
  $\rho_{f_E,\ell}\simeq\rho_{E,\ell}$ (Chapter 11). The cohomological realisation $H^1(X_0(N),\cdot)$ gives the **dual** $\rho_{f,\lambda}^\vee\simeq\rho_{f,\lambda}(-1)$, on
  which the geometric Frobenius has trace $a_p$ (important_notes.md B1, points 26, 40).
* **C3 (characters).** A Dirichlet character $\chi$ is also the Galois character with $\chi(\Frob_p)=\chi(p)$ for $p\nmid\operatorname{cond}(\chi)$; $\chi_\ell$ is
  the $\ell$-adic cyclotomic character; $\chi_q:=\chi_{q^*}$, $q^*=(-1)^{(q-1)/2}q$, the quadratic character of conductor $q$ ($q$ odd), as in the
  paper and Chapter 11 (C4); write $\chi_{-3}$, never $\chi_3$, for the quadratic character of conductor $3$ (important_notes.md point 32).
* **C4 (twists: the decisive convention).** For a Dirichlet character $\chi$ of conductor $r$:
  - the **naive twist** $f\otimes\chi:=\sum_n\chi(n)a_n(f)q^n$ (the paper's $f\otimes\chi$, the map $\iota$ of Theorem thm:twist);
  - the **newform twist** $f^\chi$: the unique newform with $\rho_{f^\chi,\lambda}\simeq\rho_{f,\lambda}\otimes\chi$ (item 2.7);
  - the **$q$-depletion** $h^{(q)}:=\sum_{q\nmid n}a_n(h)q^n$ and, for a set $S$, $h^{(S)}$ (Chapter 13's depleted form; the paper's $f^\Sigma$).
  Then $f\otimes\chi=(f^\chi)^{(r)}$ (the depletion at the primes dividing $r$), and $f\otimes\chi=f^\chi$ iff $a_q(f^\chi)=0$ for every $q\mid r$.
  The paper writes $f\otimes\chi$ for both; Section 9 below shows where this matters (points 20 and N1).
* **C5 (local components).** For $p$ prime, $\pi_p$ is the local component at $p$ of the automorphic representation of $f$; the Galois
  side is $\mathrm{WD}_p(f):=\mathrm{WD}(\rho_{f,\lambda}|_{G_{\Q_p}})^{\mathrm{F\text{-}ss}}$ ($p\ne\ell$), a two-dimensional Frobenius-semisimple Weil-Deligne representation
  (Chapter 7). Statements are made on the Galois side; the automorphic names (principal series, Steinberg, supercuspidal) are labels
  via the local Langlands correspondence (3.2), with one fixed normalisation (3.2(iv)).
* **C6 (labels).** Curve labels are Cremona's (Chapter 9, C6); isogeny classes are named without the final digit (11a, 121c), curves with
  it (121c2). "99A1" in ARS12 is Cremona's 99a1. Mod $\ell$ image labels as in Chapter 11 (C6).
* **C7 (typography).** PLAN.md 7.2. Names with plain hyphens (Eichler-Shimura, Atkin-Lehner, Atkin-Li, Deligne-Fontaine,
  Fontaine-Laffaille, Khare-Wintenberger, Ribet-Takahashi, Pollack-Weston, Kim-Ota, Taylor-Wiles); labels `...:modgalrep:...`; the
  line-up names below are the label stems.

## 2. Line-up of the core results, in teaching order

### Section 1. Conventions and recollections

**1.1 `conv:modgalrep:notation`** (convention). C1 to C6 of Part 1.3 typeset as `convention` environments, with the twist
dictionary of C4 displayed: for $\chi$ of conductor $r$, $f\otimes\chi=(f^\chi)^{(r)}$; $f\otimes\chi=f^\chi$ iff $a_q(f^\chi)=0$ for all $q\mid r$; $(f\otimes\chi)\otimes\chi=f^{(r)}$
for $\chi$ quadratic. Example (checked): $f_{11a}\otimes\chi_{-11}=f_{121d}$ exactly ($a_{11}(f_{121d})=0$), while $f_{539c}\otimes\chi_{-7}=(f_{77c})^{(7)}\ne f_{77c}$ since
$a_7(f_{77c})=-1$. Paper: Section 3 (cases (b), (c)), Lemma lem:twist(iii), Theorem thm:twist ($\iota$), important_notes.md points 20, 32.

**1.2 `prop:modgalrep:newforms-recap`** (proposition, a recollection; P with the proofs cited from Chapters 12, 13). For $f$ as in C1: (i) $\phi_f(T_n)=a_n(f)$;
$a_{mn}=a_ma_n$ for $(m,n)=1$; $a_{p^{k+1}}=a_pa_{p^k}-pa_{p^{k-1}}$ for $p\nmid N$ and $a_{p^k}=a_p^k$ for $p\mid N$; (ii) $a_p(f)\in\{\pm1\}$ if $p\,\|\,N$ and $a_p(f)=0$ if $p^2\mid N$
(Atkin-Lehner, their Theorem 3, as cited by the paper; reproved locally in 3.5); (iii) strong multiplicity one: two newforms (of any
levels, trivial character) with $a_p$ equal for all $p$ outside a set of density zero are equal; (iv) $S_2(\Gamma_0(N))\otimes\Qbar=\bigoplus_{M\mid N}\bigoplus_h\bigoplus_{d\mid N/M}\Qbar\,h(dz)$
over newforms $h$ of level $M$; the span of the $h(dz)$ is $\T$-stable, and these spans are mutually orthogonal for the Petersson product;
(v) $L(f,s)=\prod_{p\nmid N}(1-a_pp^{-s}+p^{1-2s})^{-1}\prod_{p\mid N}(1-a_pp^{-s})^{-1}$. Reference: Chapter 13 (`\Cref{ch:hecke}`); AtkinLehner70; DiamondShurman
Chapter 5 (cite the sections). Paper: Lemma lem:old, Lemma lem:crit, Section 3, Theorem thm:quant Step 1.

### Section 2. The Galois representation of a newform

**2.1 `thm:modgalrep:eichler-shimura`** (theorem, the construction of Eichler, Shimura and Deligne-Rapoport for weight $2$; S for the
construction, R for the inputs). Let $f$ be as in C1, $I_f=\ker(\phi_f\colon\T\to\mathcal O_f)$ and $A_f=J_0(N)/I_fJ_0(N)$ (Chapter 14). Then: (i) $A_f$ is an abelian
variety over $\Q$ of dimension $[K_f:\Q]$, with good reduction at every $p\nmid N$, and $\T/I_f$ (an order in $K_f$) acts on it by $\Q$-endomorphisms;
(ii) for every prime $\ell$, $V_\ell(A_f)$ is free of rank $2$ over $K_f\otimes\Ql=\prod_{\lambda\mid\ell}K_{f,\lambda}$, and
$V_\lambda(f):=V_\ell(A_f)\otimes_{K_f\otimes\Ql}K_{f,\lambda}$ carries a continuous representation $\rho_{f,\lambda}\colon G_\Q\to\GL_2(K_{f,\lambda})$ with: (a) $\rho_{f,\lambda}$ is unramified at every
$p\nmid N\ell$; (b) for such $p$, $\det(X-\rho_{f,\lambda}(\Frob_p))=X^2-a_p(f)X+p$ (the Eichler-Shimura congruence relation $T_p=\Frob_p+p\,\Frob_p^{-1}$ on
$A_f\bmod p$, Chapter 14); (c) $\det\rho_{f,\lambda}=\chi_\ell$ (Weil pairing and the Rosati-stable polarisation; or Chebotarev from (b)); (d) $\rho_{f,\lambda}$ is
odd: $\det\rho_{f,\lambda}(c)=-1$ for complex conjugation $c$; (e) $\rho_{f,\lambda}$ is absolutely irreducible (2.2). (iii) The dual $\rho_{f,\lambda}^\vee\simeq\rho_{f,\lambda}(-1)$ is
realised on the rank-two $K_{f,\lambda}$-space $H^1_{\mathrm{et}}(X_0(N)_{\Qbar},\Ql)\otimes_{\T\otimes\Ql}K_{f,\lambda}$ (the $\phi_f$-eigenspace of the etale cohomology), on which the
geometric Frobenius at $p\nmid N\ell$ has trace $a_p(f)$ (Chapter 8, 11.8; Chapter 14). Proof sketch to give: (b) from Eichler-Shimura on $J_0(N)$
and the freeness in (ii) (which follows from $\dim_\Q H_1(X_0(N),\Q)[I_f\otimes\Q]=2[K_f:\Q]$, i.e. multiplicity one of $\phi_f$ in $H^1$, Chapter 14); (a) from
Neron-Ogg-Shafarevich for abelian varieties (Serre-Tate) and good reduction of $J_0(N)$ outside $N$ (Igusa; stated). Reference: Shimura71,
Chapter 7 (Theorem 7.14 and the construction in 7.5; verify the numbers); DiamondShurman Chapter 9 (cite the sections); DDT Theorem
3.1 (as cited by the paper); DiamondIm Section 12; Deligne (Bourbaki 355) for the general statement. Paper: Section 1.1 ($V$, $T$, $\rho$),
Section 4.2 ($M_{f,\lambda}$), Lemma lem:old ($\bar\rho_h$), the optimal-level paragraph ("arises from a newform").

**2.2 `prop:modgalrep:irreducible`** (proposition; S). For $f$ as in C1 and every $\lambda$, $\rho_{f,\lambda}$ is absolutely irreducible. Sketch to give (weight $2$):
if $\rho_{f,\lambda}\otimes\overline{K}_{f,\lambda}$ had a stable line, its character $\psi_1$ and the quotient $\psi_2$ would be Hodge-Tate (sub-quotients of $V_\ell(A_f)$, Faltings,
Tate; stated), hence of the form $\varepsilon_i\chi_\ell^{k_i}$ with $\varepsilon_i$ of finite order and $\{k_1,k_2\}=\{0,1\}$ (Serre's theorem on abelian Hodge-Tate
characters, stated); then $a_p=\varepsilon_1(p)+\varepsilon_2(p)p$ up to order for a density-one set of $p$, so $|a_p|\ge p-1>2\sqrt p$ for $p\ge7$, contradicting the
Ramanujan-Petersson bound (Chapter 12, 6.5; Weil). Reference: Ribet77 (the general case, add to `bib/ch15.bib`, Part 6.5). Paper:
background (the paper uses only residual irreducibility, which is a hypothesis).

**2.3 `thm:modgalrep:deligne`** (theorem; R). (Deligne; Deligne-Serre for weight $1$.) For a normalised newform $f$ of weight $k\ge2$, level $N$
and character $\varepsilon$, and $\lambda\mid\ell$, there is a continuous irreducible $\rho_{f,\lambda}\colon G_\Q\to\GL_2(K_{f,\lambda})$, unramified outside $N\ell$, with
$\det(X-\rho_{f,\lambda}(\Frob_p))=X^2-a_pX+\varepsilon(p)p^{k-1}$ for $p\nmid N\ell$ and $\det\rho_{f,\lambda}=\varepsilon\chi_\ell^{k-1}$; it is odd. Reference: Deligne (Bourbaki 355);
DiamondShurman 9.6 (cite the section). Paper: background (only weight $2$ is used; the optimal-level theorem allows a nebentypus, 6.4).

**2.4 `prop:modgalrep:lattices`** (proposition; P from Chapters 4 and 5). (i) $\rho_{f,\lambda}$ stabilises an $\mathcal O_\lambda$-lattice $L$ (compactness of $G_\Q$;
Chapter 5, galois:continuous-reps); the reduction $\bar\rho_L\colon G_\Q\to\GL_2(k_\lambda)$ has semisimplification independent of $L$ (Chapter 4, 10.2), written
$\bar\rho_{f,\lambda}^{\mathrm{ss}}$; (ii) $\bar\rho_{f,\lambda}$ is odd, and **for $\ell$ odd it is irreducible over $k_\lambda$ iff absolutely irreducible**: $\bar\rho(c)$ has the distinct
eigenvalues $1,-1\in k_\lambda$, and a stable line over $\bar k_\lambda$ is an eigenline of $\bar\rho(c)$, hence defined over $k_\lambda$ (as Chapter 11, 1.4(i), for
$E$); (iii) if $\bar\rho_L$ is irreducible, every stable lattice is homothetic to $L$ (Chapter 4, 10.3, the lemma PLAN.md calls Ribet's
lemma on lattices), so $\bar\rho_{f,\lambda}$ is well defined up to isomorphism; (iv) for $\ell\nmid N$ the "residual representation attached to $f$
and $\lambda$" in the paper means $\bar\rho_{f,\lambda}$ for any choice of $L$. Paper: Section 1.1 ($\bar\rho$), Lemma lem:old, Section 4.2 ("homothetic when
$\bar\rho$ is irreducible"), important_notes.md point 10.

**2.5 `cor:modgalrep:congruent-newforms`** (corollary; P given 2.1, 2.4 and Chapter 5, galois:congruent-ap). Let $f$, $h$ be newforms of
weight $2$ with trivial character, of levels $N_f$, $N_h$, with coefficients in the ring of integers $\mathcal O$ of a number field, and $\lambda\mid\ell$ a
prime of $\mathcal O$. (i) If $a_p(f)\equiv a_p(h)\pmod\lambda$ for all $p$ in a set of density one, then $\bar\rho_{f,\lambda}^{\mathrm{ss}}\simeq\bar\rho_{h,\lambda}^{\mathrm{ss}}$ over $k_\lambda$.
(ii) If moreover $\bar\rho_{f,\lambda}$ is irreducible and $\ell$ is odd (hence $\bar\rho_{f,\lambda}$ is absolutely irreducible, 2.4(ii)), then
$\bar\rho_{h,\lambda}\simeq\bar\rho_{f,\lambda}$ (over $k_\lambda$; in particular over a common finite extension of $\F_\ell$ when the two are first defined over different
fields). (iii) Conversely $\bar\rho_{f,\lambda}^{\mathrm{ss}}\simeq\bar\rho_{h,\lambda}^{\mathrm{ss}}$ gives $a_p(f)\equiv a_p(h)\pmod\lambda$ for every $p\nmid N_fN_h\ell$. Reference: as cited. Paper:
Lemma lem:old (case $p\nmid\ell N$: "$\bar\rho_h\simeq\bar\rho$ by Chebotarev and Brauer-Nesbitt, $\bar\rho$ being irreducible"; corrected per
important_notes.md point 10), Section 3 ("$\bar\rho_g\simeq\bar\rho$, that is, $a_p(g)\equiv a_p(f)\pmod\lambda$ for all $p\nmid3N$").

**2.6 `thm:modgalrep:comparison-E`** (theorem; P given Chapters 8, 11, 14 and modularity). Let $E/\Q$ have conductor $N$, $f=f_E$ (modularity,
Chapter 14), $E_0$ the $X_0(N)$-optimal curve of the class, $\phi=\varphi_{E_0}\colon X_0(N)\to E_0$, $\ell$ any prime. (i) $A_f=E_0$ (the quotient of
$J_0(N)$ by $I_fJ_0(N)$ is the optimal quotient; Chapter 14), so $T_\ell E_0$ is a $G_\Q$-stable lattice in $V_\lambda(f)$ with $\lambda=\ell$, and
$\rho_{E_0,\ell}=\rho_{f,\ell}$ on it; for every $E$ in the class, $V_\ell E\simeq V_\ell E_0$ through an isogeny. (ii) **(important_notes.md point 40.)** The lattice
$M_{f,\lambda}:=H^1(X_0(N),\Zl)[\ker\phi_f]$ of DFG04 (Section 4.1 of the paper, Chapter 20) equals $\phi^*H^1(E_0,\Zl)$, and $\phi^*$ gives a
$G_\Q$-isomorphism $H^1(E_0,\Zl)=\Hom_{\Zl}(T_\ell E_0,\Zl)\simeq T_\ell E_0(-1)$ onto it; no irreducibility is needed. Proof: the kernel of
$J_0(N)\to E_0$ is connected, so $\phi_*\colon H_1(X_0(N),\Z)\to H_1(E_0,\Z)$ is surjective and $\phi^*$ is injective with torsion-free cokernel (Chapter 3,
saturation); $\T$ acts on the image through $\phi_f$; both sides have rank $2$ (multiplicity one of $\phi_f$ in $H^1(X_0(N),\Q)$); a saturated
sublattice of full rank in a saturated sublattice is equal to it; Galois-equivariance by the etale comparison (Chapter 8, 11.8(c)). (iii)
**(important_notes.md point 26.)** If $\bar\rho_{E,\ell}$ is irreducible, every $G_\Q$-stable lattice in $V_\ell(E)^\vee$, in particular $M_{f,\lambda}$ and $(T_\ell E)^\vee$ for
any $E$ in the class, is homothetic to $(T_\ell E)^\vee\simeq T_\ell E(-1)$ (2.4(iii)); the paper's "$M_{f,\lambda}$ and $T_\ell E$ are homothetic" must be read
with the dual. (iv) Consequently $\ad M_{f,\lambda}=\ad T_\ell E$ inside $\End(V_\ell E)$ under $x\mapsto-x^t$ and the twist-invariance of $\ad$ (Chapter 4,
7.7; Chapter 9, 5.5), which is all the paper uses ("so their adjoints coincide"). Reference: Chapters 8, 9, 14; DFG04 Sections 1.6.2,
1.7.3 (the normalisation of $M_{f,\lambda}$ as the paper describes it; verify against DFG04 before printing the identification). Paper:
Section 4.2 (the parenthesis on $M_{f,\lambda}$ and $T_\ell E$), Lemma lem:hecke ($L[\wp]=M_{f,\lambda}$), Theorem thm:main ($A=\ad T$), important_notes.md
points 26, 39, 40 and B3.

**2.7 `prop:modgalrep:twists`** (proposition; P given 2.1, strong multiplicity one and Shimura's twisting lemma). Let $g$ be a newform of
weight $2$, trivial character, level $M$, and $\chi$ a primitive Dirichlet character of conductor $r$. (i) $\rho_{g,\lambda}\otimes\chi$ is unramified outside
$Mr\ell$ and has $\tr(\rho_{g,\lambda}\otimes\chi)(\Frob_p)=\chi(p)a_p(g)$ for $p\nmid Mr\ell$. (ii) $g\otimes\chi\in S_2(\Gamma_0(\operatorname{lcm}(M,r^2)),\chi^2)$ (Chapter 13; AtkinLi78
for the level $\operatorname{lcm}(M,r^2)$; Shimura71, Proposition 3.64, gives the weaker level $Mr^2$; verify both numbers), and there is a unique newform $g^\chi$, of character $\chi^2$ and level dividing $\operatorname{lcm}(M,r^2)$,
with $\rho_{g^\chi,\lambda}\simeq\rho_{g,\lambda}\otimes\chi$; it satisfies $a_n(g^\chi)=\chi(n)a_n(g)$ for $(n,r)=1$, and $g\otimes\chi=(g^\chi)^{(r)}$ (C4). (iii) For $\chi$ quadratic,
$(g^\chi)^\chi=g$, and the level of $g^\chi$ is $M\prod_{q\mid r}q^{a(\pi_q\otimes\chi_q)-a(\pi_q)}$, computed type by type in 3.8. (iv) For $E/\Q$ and $d$ a
fundamental discriminant, $f_{E^{(d)}}=(f_E)^{\chi_d}$ (Chapter 9, 10.3, 10.4 and strong multiplicity one). Examples (checked): $f_{11a}^{\chi_{-11}}=f_{121d}$
$=f_{11a}\otimes\chi_{-11}$; $f_{121a}^{\chi_{-11}}=f_{121c}=f_{121a}\otimes\chi_{-11}$; $f_{539c}^{\chi_{-7}}=f_{77c}$, while $f_{539c}\otimes\chi_{-7}=f_{77c}^{(7)}$; $f_{11a}^{\chi_{-7}}=f_{539d}=f_{11a}\otimes\chi_{-7}$;
$f_{20a}^{\chi_{-7}}=f_{980g}$; $f_{980i}^{\chi_{-7}}=f_{140b}$. Paper: Lemma lem:twist(iii), Theorem thm:qual (b), (c), Theorem thm:twist, Theorem thm:quant,
the Example of Section 3.

### Section 3. Local-global compatibility and local components

**3.1 `rem:modgalrep:weil-deligne-recap`** (remark, a recollection; P or R as in Chapter 7). From Chapter 7 (`\Cref{ch:local}`): Weil-Deligne
representations $(r,N)$ and $\mathrm{WD}(\rho)$ for $p\ne\ell$ (its 7.3, 7.4), $\mathrm{sp}(2)\otimes\mu$ and the classification of two-dimensional
Frobenius-semisimple $(r,N)$ (7.5(ii), (iii)), $V^{I_p}=(\ker N)^{r(I_p)}$ (8.1), $L(V,s)=\det(1-\Phi_pp^{-s}\mid V^{I_p})^{-1}$ (8.2), the Artin conductor
$a(V)=\dim V-\dim V^{I_p}+\operatorname{sw}(V)$ (8.3, 8.4), $\epsilon$-factors (8.5), the shapes table (9.4). Stated in one page, no proofs. Paper:
background for Lemma lem:euler, Lemma lem:twist(iii).

**3.2 `thm:modgalrep:local-langlands`** (theorem; R). (The local Langlands correspondence for $\GL_2(\Q_p)$: Kutzko, Bushnell-Henniart.)
Fix an isomorphism $\C\simeq\Qbar_\ell$. There is a unique bijection $\pi\mapsto\operatorname{rec}(\pi)$ from isomorphism classes of irreducible admissible
infinite-dimensional representations of $\GL_2(\Q_p)$ to isomorphism classes of two-dimensional Frobenius-semisimple Weil-Deligne
representations of $W_{\Q_p}$ such that: (i) for characters $\mu$ of $\Q_p^\times$ (identified with characters of $W_{\Q_p}$ by local class field theory,
Chapter 7, 6.5), $\operatorname{rec}(\pi\otimes(\mu\circ\det))=\operatorname{rec}(\pi)\otimes\mu$; (ii) $\det\operatorname{rec}(\pi)$ corresponds to the central character of $\pi$; (iii) $L$-
and $\epsilon$-factors of pairs and conductors are preserved, in particular $a(\operatorname{rec}\pi)=a(\pi)$, the exponent of the conductor (Casselman's
newvector theory); (iv) principal series $\pi(\mu_1,\mu_2)\mapsto\mu_1\oplus\mu_2$, twisted Steinberg $\mathrm{St}\otimes\mu\mapsto\mathrm{sp}(2)\otimes\mu$, supercuspidals $\mapsto$ irreducible
$(r,0)$; for $p$ odd every supercuspidal corresponds to $\Ind_{W_K}^{W_{\Q_p}}\theta$ for a quadratic $K/\Q_p$ and a character $\theta$ not factoring through the
norm (dihedral). The book fixes **one** normalisation and states it once: the *arithmetic* (Tate-twisted) normalisation in which a
weight-two newform with trivial character has $\mathrm{WD}_p(f)\simeq\operatorname{rec}(\pi_p\otimes|\det|^{-1/2})$, so that $\det\mathrm{WD}_p(f)=\|\cdot\|$, the character of
$W_{\Q_p}$ that matches $\det\rho=\chi_\ell$ (Chapter 7, 7.1(ii): $\|w\|=\chi_\ell(w)$); the writer must check the half-integral twist against the chosen reference and never mix two normalisations
in one formula. Reference: BushnellHenniart06 (add to `bib/ch15.bib`; cite chapters, not theorem numbers), Rohrlich94 (Sections 8 to 15
for the elliptic-curve dictionary; add to `refs.bib`, Part 6.5), Casselman73 (conductors; add to `bib/ch15.bib`). Paper: Lemma lem:euler
("local component ... Steinberg"), Lemma lem:twist(iii).

**3.3 `def:modgalrep:local-component`** (definition and theorem; R). To a newform $f$ of weight $2$ and level $N$ with trivial character
corresponds a cuspidal automorphic representation $\pi_f=\bigotimes'_v\pi_v$ of $\GL_2(\mathbb A_\Q)$ (Jacquet-Langlands); $\pi_p$ is its *local component at $p$*,
with trivial central character and conductor exponent $a(\pi_p)=v_p(N)$ (Casselman73). The Hecke eigenvalue $a_p(f)$ is determined by
$\pi_p$: it is the eigenvalue of the normalised $U_p$ (or $T_p$) on the new vector. Reference: DiamondIm Section 11 (cite the section);
BushnellHenniart06; Loeffler-Weinstein for computing $\pi_p$ in practice (add `LoefflerWeinstein12` to `bib/ch15.bib`). Paper: Lemma
lem:euler, Lemma lem:twist(iii) (the phrase "the local component of $g$ at $q$").

**3.4 `thm:modgalrep:carayol`** (theorem, local-global compatibility at $p\ne\ell$; R, with (ii), (iii) P from (i)). (Langlands, Deligne,
Carayol.) For $f$ as in C1, every prime $p$ and every $\lambda\mid\ell$ with $\ell\ne p$: (i) $\mathrm{WD}_p(f)\simeq\operatorname{rec}(\pi_p\otimes|\det|^{-1/2})$ (normalisation of 3.2);
(ii) the Artin conductor exponent of $\rho_{f,\lambda}|_{G_{\Q_p}}$ is $v_p(N)$, so **the conductor of $\rho_{f,\lambda}$ is $N$** (for $\ell\nmid N$; for $\ell\mid N$, its prime-to-$\ell$
part is that of $N$); (iii) $L_p(f,s)=L(V_\lambda(f)|_{G_{\Q_p}},s-1)=\det(1-\Phi_pp^{1-s}\mid V_\lambda(f)^{I_p})^{-1}$, i.e. $a_p(f)$ is the trace of the geometric Frobenius
$\Phi_p$ on $V_\lambda(f)^{I_p}$ multiplied by $p$ (good $p$: $\Phi_p$-eigenvalues $\alpha^{-1},\beta^{-1}$ and $p\alpha^{-1}+p\beta^{-1}=\beta+\alpha$; multiplicative $p$: the
eigenvalue $\varepsilon(\Frob_p)p^{-1}$ on the line, giving $a_p=\varepsilon(\Frob_p)$); equivalently $a_p(f)=\tr(\Phi_p\mid(V_\lambda(f)^\vee)^{I_p})$, the trace of the
geometric Frobenius on the inertia invariants of the cohomological realisation (C2). Reference:
Carayol86 (Theoreme A; the paper's Carayol89 is the mod $\ell$ paper), Langlands73 (add to `bib/ch15.bib`), Deligne73 (add to
`refs.bib`), DDT Theorem 3.1 (as cited by the paper for (e)). Paper: Lemma lem:euler, Lemma lem:twist(iii), Lemma lem:old (cases
$p\,\|\,N$), Section 1.1 ($\delta_p$), the optimal-level paragraph ("the conductor").

**3.5 `thm:modgalrep:local-types`** (theorem and table; P on the Galois side given 3.4 and Chapter 7, the automorphic names R). Let $f$ be
as in C1, $p\ne\ell$, $V=V_\lambda(f)|_{G_{\Q_p}}$, $\delta_p=\dim V^{I_p}$. Exactly one of the following holds.

| case | $v_p(N)$ | $\mathrm{WD}_p(f)$ | $\pi_p$ | $\delta_p$ | $a_p(f)$ |
|-|-|-|-|-|-|
| (U) | $0$ | unramified, $\Frob_p$-eigenvalues $\alpha,\beta$, $\alpha+\beta=a_p$, $\alpha\beta=p$ | unramified principal series | $2$ | $a_p$ |
| (St) | $1$ | $\mathrm{sp}(2)\otimes\mu$, $\mu$ unramified, $\mu^2=1$ | unramified twist of Steinberg | $1$ | $\pm1$ |
| (RSt) | $2a(\chi)$ | $\mathrm{sp}(2)\otimes\mu\chi$, $\mu$ unramified, $\chi$ ramified quadratic | ramified twist of Steinberg | $0$ | $0$ |
| (RPS) | $2a(\mu_1)\ge2$ | $\mu_1\oplus\mu_2$, both ramified, $\mu_1\mu_2$ unramified on $I_p$ | ramified principal series | $0$ | $0$ |
| (SC) | $\ge2$ | irreducible, $N=0$ | supercuspidal | $0$ | $0$ |

In case (St): $\rho_{f,\lambda}|_{G_{\Q_p}}\simeq\begin{psmallmatrix}\varepsilon\chi_\ell&*\\0&\varepsilon\end{psmallmatrix}$ with $\varepsilon$ unramified, $\varepsilon(\Frob_p)=a_p(f)$, non-split; on an
$\mathcal O_\lambda$-lattice the same shape holds (DDT Theorem 3.1(e), as cited by the paper; letter and number not re-checked here), and the
residual representation $\bar\rho|_{D_p}$ is an extension of $\bar\varepsilon$ by $\bar\varepsilon\bar\chi_\ell$, unramified iff the corner vanishes on $I_p$ modulo $\lambda$, and
non-split whenever it is ramified, with a unique stable line then (Chapter 4, 3.6). In particular **$a_p(f)=0$ and $V^{I_p}=0$ whenever $p^2\mid N$,
and $\delta_p=2,1,0$ according as $p\nmid N$, $p\,\|\,N$, $p^2\mid N$.** Proof (P, to be written in full): by 3.4(ii) $a(V)=v_p(N)$; $\det V=\chi_\ell$ is unramified at
$p$. If $a(V)=0$, (U). If $a(V)=1$: $V$ is tame and $\dim V^{I_p}=1$; $N=0$ would make $r|_{I_p}=1\oplus\psi$ with $\psi$ ramified, contradicting $\det|_{I_p}=1$; so
$N\ne0$ and $V\simeq\mathrm{sp}(2)\otimes\mu$ (Chapter 7, 7.5(ii)) with $\mu$ unramified ($a=1$), $\mu^2=1$ from $\det$, and $a_p(f)=\mu(\Frob_p)$ from 3.4(iii). If
$a(V)\ge2$: $\dim V^{I_p}=2$ is excluded ($a=0$); $\dim V^{I_p}=1$ is excluded as before ($N=0$ gives $\det|_{I_p}\ne1$; $N\ne0$ gives $\mathrm{sp}(2)\otimes\mu$ with $\mu$
unramified, $a=1$); so $V^{I_p}=0$, $L_p=1$, and $a_p(f)=0$ by 3.4(iii); the three subcases are the classification of Chapter 7, 7.5. This is a
local proof of Atkin-Lehner's Theorem 3 for weight $2$ (the paper cites AtkinLehner70 Theorem 3 in Lemma lem:old). For $f=f_E$ the
Galois-side table is also Chapter 11's 3.1, 3.2, 3.4, 4.1. Paper: Section 1.1 ("$\delta_p=2,1,0$"), Lemma lem:euler, Lemma lem:twist(iii),
Lemma lem:old (cases $p\,\|\,N$, $p^2\mid N$), Section 4.1 ($M^\Sigma$, $\delta_p$), Theorem thm:dfg14 (only $\delta_p\ge1$ contribute).

**3.6 `prop:modgalrep:kodaira-dictionary`** (proposition and table; P given Chapter 11, 3.2, 3.4, 4.1 and 3.5, R for the automorphic
names; Rohrlich94). Let $f=f_E$, $q\ge5$ a bad prime, $q\ne\ell$. The local type of $f$ at $q$ by Kodaira type:

| Kodaira type at $q$ | $\rho_{E,\ell}(I_q)$ | type of $\pi_q$ |
|-|-|-|
| $\mathrm I_n$, $n\ge1$ | unipotent, infinite | (St) |
| $\mathrm I_n^*$, $n\ge1$ | $\pm$unipotent | (RSt) with $\chi=\chi_q$ |
| $\mathrm I_0^*$ | $\{\pm1\}$ | (RPS) with $\mu_1=\chi_q\nu_{\alpha'}$, $\mu_2=\chi_q\nu_{\beta'}$ ($\nu_x$ unramified, $\Frob_q\mapsto x$; $\alpha',\beta'$ the Frobenius eigenvalues of $E^{(q)}$) |
| $\mathrm{II},\mathrm{II}^*,\mathrm{IV},\mathrm{IV}^*$ | cyclic of order $6$, $3$ | (RPS) if $q\equiv1\pmod3$, (SC) if $q\equiv2\pmod3$ |
| $\mathrm{III},\mathrm{III}^*$ | cyclic of order $4$ | (RPS) if $q\equiv1\pmod4$, (SC) if $q\equiv3\pmod4$ |

(On the Galois side the $\mathrm I_0^*$ row reads $V\simeq V'\otimes\chi_q$ with $V'=V_\ell E^{(q)}$ unramified; the automorphic labels are stated in the
normalisation of 3.2(iv) and are not used in any proof.) Proof of the last two rows: $\rho(I_q)=\langle g\rangle$ cyclic of order $m$ with $\Frob_q g\Frob_q^{-1}=g^q$
(Chapter 11, 4.1); if $q\equiv1\pmod{m'}$ ($m'=3$ or $4$) $\Frob_q$ preserves the two eigenlines of $g$ and $V\otimes\overline{K}$ is a sum of two characters
(ramified principal series); if $q\equiv-1\pmod{m'}$ it swaps them and $V\otimes\overline K$ is induced from the unramified quadratic extension,
irreducible (supercuspidal, "unramified dihedral") (Chapter 7, 9.2(ii)). Examples (checked): 11a1 at $11$ (St); 121d2 at $11$ ($\mathrm I_5^*$, RSt); 539d1
at $7$ ($\mathrm I_0^*$, RPS); 121c1 at $11$ ($\mathrm{IV}$, $11\equiv2\pmod3$: SC); 121a1 at $11$ ($\mathrm{II}$: SC); 726a1 at $11$ ($\mathrm{III}$, $11\equiv3\pmod4$: SC). Paper: Lemma
lem:euler (the phrases "local component of $f$ is an unramified twist of the Steinberg representation" and "$V=V'\otimes\chi_q$ with $V'$
Steinberg"), Lemma lem:twist(iii), Remark rem:types (background).

**3.7 `cor:modgalrep:delta-naive`** (corollary; P). With $\delta_p$ as in 3.5: $a_p(f)\in\{\pm1\}$ iff $\delta_p=1$, $a_p(f)=0$ iff $\delta_p=0$ (for $p\mid N$); hence the
naive local factor of the adjoint, which is built from $a_p$ alone, equals the true one exactly when $\delta_p>0$ (the comparison is Chapter
19's), and $\ad(\rho\otimes\chi)=\ad\rho$ makes the true adjoint factor twist-invariant while the naive one is not (important_notes.md point 15). Paper:
Section 1.1 (definition of $L^{\nv}_p$), Section 4.1 ($M^\Sigma=M\prod p^{\delta_p}$), Theorem thm:dfg14, Theorem thm:quant Step 3 ("$A_g=A_f$").

**3.8 `prop:modgalrep:twist-conductor`** (proposition and table; P given 3.4, 3.5 and Chapter 7, 8.4). Let $q$ be an odd prime, $\chi$ a
ramified quadratic character of $G_{\Q_q}$ (tame, $a(\chi)=1$), and $f$ as in C1. Then $a(\mathrm{WD}_q(f)\otimes\chi)$ is given by:

| type of $f$ at $q$ (3.5) | $a(\mathrm{WD}_q(f))$ | $a(\mathrm{WD}_q(f)\otimes\chi)$ | change of level under $f\mapsto f^{\chi_q}$ |
|-|-|-|-|
| (U) | $0$ | $2$ | $\times q^2$ |
| (St) | $1$ | $2$ | $\times q$ |
| (RSt) with the same $\chi$ | $2$ | $1$ | $\div q$ |
| (RPS) with $\mu_i=\chi\cdot$(unramified) | $2$ | $0$ | $\div q^2$ |
| (RPS) or (SC) with tame inertia of order $3$, $4$ or $6$ | $2$ | $2$ | $\times1$ |

Proof: $a(\mathrm{sp}(2)\otimes\nu)=2a(\nu)$ for ramified $\nu$ and $1$ for unramified $\nu$ (Chapter 7, 9.3); for a sum of characters add the conductors;
for tame characters $\psi$ of $I_q$ of order $3$, $4$, $6$, $\psi\chi$ has order $6$, $4$, $3$ (so it stays ramified, conductor $1$); for (SC) of the tame dihedral
kind, $\mathrm{WD}\otimes\chi$ is again tame with $V^{I}=0$, conductor $2$. Corollaries: (a) **Lemma lem:twist(iii) (Atkin-Li)**: if $q^2\nmid M$, then $g^{\chi_q}=g\otimes\chi_q$
is a newform of level $\operatorname{lcm}(M,q^2)$ (rows (U), (St); $a_q(g^{\chi_q})=0$ because its type at $q$ is (RSt) or (RPS), so the naive and the newform twist
agree, C4); (b) the conductor of $E^{(q)}$ versus $E$ at $q$ by Kodaira type agrees with Lemma lem:twist(ii) (Chapter 10, 8.2): $\mathrm I_n\leftrightarrow\mathrm I_n^*$
changes $q^1\leftrightarrow q^2$, $\mathrm I_0\leftrightarrow\mathrm I_0^*$ changes $q^0\leftrightarrow q^2$, and $\mathrm{II}\leftrightarrow\mathrm{IV}^*$, $\mathrm{III}\leftrightarrow\mathrm{III}^*$, $\mathrm{IV}\leftrightarrow\mathrm{II}^*$ keep $q^2$; (c) at
$p\ne q$ nothing changes ($\chi_q$ is unramified at $p$). Examples (checked by twisting and identifying in `allcurves`): 11a1 (St at $11$) to
121d2; 11a3 to 121d1; 11a1 (U at $7$) to 539d2; 121a1 (SC) to 121c2; 539c1 (RSt at $7$) to 77c1; 539d1 (RPS at $7$) to 11a (level $\div49$);
20a1 (U at $7$) to 980g2; 980i1 (RSt at $7$) to 140b1. Paper: Lemma lem:twist(iii) and its proof ("whose twist by a ramified quadratic
character has conductor exponent $2$"), Theorem thm:qual (b) ("$h=g\otimes\chi$ is a newform on $\Gamma_0(Mq)$"), (c) ("on $\Gamma_0(Mq^2)$"), Theorem
thm:twist (levels $N_S=N/D$, $N/D^2$, $N$), Theorem thm:quant ("$N_S^\Sigma=N$"), Section 1.4.

### Section 4. The representation at $\ell$ when $\ell\nmid N$

**4.1 `thm:modgalrep:crystalline`** (theorem; R, with (i) S). Let $f$ be as in C1, $\lambda\mid\ell$, $\ell\nmid N$. (i) $A_f$ has good reduction at $\ell$, and for every $k$ the
$G_{\Q_\ell}$-module $A_f[\ell^k]$ is the generic fibre of a finite flat group scheme over $\Zl$ (the $\ell^k$-torsion of the Neron model, an abelian
scheme); hence $\bar\rho_{f,\lambda}|_{D_\ell}$ is *finite* ("good" in the sense of DDT Theorem 3.15), as are all its reductions $\rho_{f,\lambda}\bmod\lambda^k$. (ii)
$\rho_{f,\lambda}|_{G_{\Q_\ell}}$ is crystalline with Hodge-Tate weights $\{0,1\}$, and the crystalline Frobenius on $D_{\mathrm{cris}}$ has characteristic polynomial
$X^2-a_\ell(f)X+\ell$ (Fontaine; Faltings; stated); for $\ell\ge3$ the weights lie in the Fontaine-Laffaille range, so stable lattices correspond to
Fontaine-Laffaille modules (FontaineLaffaille; stated, used in Chapter 18 and by DFG04). (iii) The Serre weight of $\bar\rho_{f,\lambda}$ is $2$ when
it is irreducible (Serre87, Section 2; Edixhoven92; verify the section numbers). Reference: DDT Sections 2.1 and 3.1 (cite the
sections); Berger; Chapter 11, 5.1 (the elliptic-curve case). Paper: the optimal-level paragraph ("the restriction to $D_\ell$ comes from
the finite flat group scheme $E'[\ell]$ and is good"), Lemma lem:old (case $p=\ell$), Theorem thm:main (crystalline at $\ell$ via DFG04,
Chapter 18).

**4.2 `thm:modgalrep:deligne-fontaine`** (theorem; R for (i), (ii), P for (iii)). Let $\ell$ be odd, $f$ as in C1 with $\ell\nmid N$, $\lambda\mid\ell$, $\bar\rho=\bar\rho_{f,\lambda}$ (any
lattice), $\omega=\bar\chi_\ell|_{I_\ell}$, $\omega_2$ a fundamental character of level $2$ (Chapter 11, 5.2). (i) (Deligne.) If $a_\ell(f)\not\equiv0\pmod\lambda$, then
$\bar\rho|_{D_\ell}\simeq\begin{psmallmatrix}\bar\chi_\ell\,\mu(\bar a_\ell^{-1})&*\\0&\mu(\bar a_\ell)\end{psmallmatrix}$ with $\mu(x)$ the unramified character sending $\Frob_\ell$ to $x$. (ii) (Fontaine.) If
$a_\ell(f)\equiv0\pmod\lambda$, then $\bar\rho|_{I_\ell}\otimes\bar k_\lambda\simeq\omega_2\oplus\omega_2^\ell$ and $\bar\rho|_{D_\ell}$ is irreducible. (iii) Consequently $a_\ell(f)\bmod\lambda$ is determined by the
isomorphism class of $\bar\rho|_{D_\ell}$: it is $0$ if $\bar\rho|_{D_\ell}$ is irreducible; otherwise $\bar\rho|_{D_\ell}$ has a unique one-dimensional unramified quotient
(unique because $\omega\ne1$ for $\ell$ odd), and $a_\ell(f)\bmod\lambda$ is the eigenvalue of $\Frob_\ell$ on it. Hence if $h$ is another newform of weight $2$
with trivial character and level prime to $\ell$ and $\bar\rho_{h,\lambda}\simeq\bar\rho_{f,\lambda}$, then $a_\ell(h)\equiv a_\ell(f)\pmod\lambda$. Proof of (iii) from (i), (ii): direct.
Reference: Edixhoven92, Section 2 (as cited by the paper; Theorems 2.5 and 2.6 there, verify); Serre87; Wiles88 (ordinary $\lambda$-adic
representations, for (i)). Paper: Lemma lem:old, case $p=\ell$ ("By the theorems of Deligne and Fontaine describing $\bar\rho_f|_{D_\ell}$ and
$\bar\rho_h|_{D_\ell}$ ... Hence $a_\ell(h)\equiv a_\ell(f)$"); the remark after the Example ("$\ell\nmid N$ is used ... in Lemma lem:old at $p=\ell$").
Example (checked): $a_3(121\mathrm c1)=2\equiv-1=a_3(11\mathrm a1)\pmod3$ (both ordinary at $3$); $a_3(f_{121d})=a_3(11\mathrm a1)\chi_{-11}(3)=-1\cdot1$, and
$a_3(121\mathrm a1)=2\equiv-1\pmod3$, as Lemma lem:old requires in the Example.

### Section 5. Serre's conjecture: conductor, weight, character

**5.1 `def:modgalrep:serre-invariants`** (definition; P for the elementary properties). For an odd irreducible continuous
$\bar\sigma\colon G_\Q\to\GL_2(\bar\F_\ell)$: the Serre conductor $N(\bar\sigma)=\prod_{p\ne\ell}p^{a_p(\bar\sigma)}$ (Chapter 11, 6.1: $a_p=\dim\bar\sigma-\dim\bar\sigma^{I_p}+\operatorname{sw}_p$, prime to $\ell$ by
definition, prime to every prime at which $\bar\sigma$ is unramified); the Serre weight $k(\bar\sigma)\ge2$ (definition by reference: Serre87,
Section 2; Edixhoven92), equal to $2$ when $\bar\sigma|_{D_\ell}$ is finite (4.1(iii)); the character $\varepsilon(\bar\sigma)$ with $\det\bar\sigma=\varepsilon(\bar\sigma)\bar\chi_\ell^{k-1}$. "$\bar\sigma$
**arises from** a newform $g$ (of level $M$)" means: $\bar\sigma\simeq\bar\rho_{g,\lambda}\otimes\bar\F_\ell$ for some $\lambda\mid\ell$; equivalently (2.5) $\tr\bar\sigma(\Frob_p)\equiv a_p(g)\pmod\lambda$
for all $p\nmid M\ell N(\bar\sigma)$ when $\bar\sigma$ is absolutely irreducible. "Modular" means: arises from some newform. Paper: the optimal-level
paragraph ("irreducible and modular", "$N(\bar\sigma)$ is the Serre conductor").

**5.2 `prop:modgalrep:serre-conductor-divides`** (proposition; P). Let $f$ be as in C1, $\lambda\mid\ell$, $p\ne\ell$. Then
$a_p(\bar\rho_{f,\lambda}^{\mathrm{ss}})\le a_p(\bar\rho_{f,\lambda})\le a_p(\rho_{f,\lambda})=v_p(N)$, with $a_p(\bar\rho)=v_p(N)-(\dim\bar\rho^{I_p}-\dim V^{I_p})$; hence $N(\bar\rho_{f,\lambda})\mid N$ (the prime-to-$\ell$ part when
$\ell\mid N$). Proof: the wild inertia $P_p$ acts on a stable lattice $L$ through a finite $p$-group (Chapter 7, 5.7), of order prime to $\ell$, so the
dimensions of the fixed spaces of the ramification subgroups $G_i$, $i\ge1$, are the same on $L\otimes K$ and on $L/\lambda L$ ($L$ is a projective
$\mathcal O_\lambda[G_i]$-module; Chapter 4, 3.2(ii)) and the Swan conductors agree; $L^{I_p}$ is saturated in $L$, so $L^{I_p}/\lambda L^{I_p}\hookrightarrow(L/\lambda L)^{I_p}$ and
$\dim\bar\rho^{I_p}\ge\dim V^{I_p}$; then 3.4(ii). The first inequality: semisimplification can only enlarge invariants of the tame part (or use the
same argument). Reference: Carayol89, Livne89 (the exact list of possible exponents; add `Livne89` to `refs.bib`, Part 6.5). For $f=f_E$
the exact formula $a_p(\bar\rho_{E,\ell})=f_p(E)-\dim_{\F_\ell}\Phi_p(\bar\F_p)[\ell]$ is Chapter 11, 6.2, with its examples in 6.3. Paper: the optimal-level paragraph
("$N(\bar\rho_{E',\ell})$ divides the conductor of $E'$ [Carayol89]"), cases (a), (b), (c) ("$M\mid N/q$", "$M\mid N/q^2$").

**5.3 `thm:modgalrep:serre-conjecture`** (theorem; R). (Serre's conjecture; Khare-Wintenberger, with Kisin; Khare for level one.) Every
odd absolutely irreducible continuous $\bar\sigma\colon G_\Q\to\GL_2(\bar\F_\ell)$ arises from a newform of weight $k(\bar\sigma)$, level $N(\bar\sigma)$ and character lifting
$\varepsilon(\bar\sigma)$. The "strong" form (optimal weight and level) follows from the "weak" form (some weight and level) by the work of
Ribet, Carayol, Diamond, Edixhoven, Buzzard and others (Section 6 for the level). Reference: KhareWintenberger; Khare; Serre87;
Edixhoven92; Diamond95. Paper: background; the paper uses only the optimal-level direction (6.4) for $\bar\rho_{E,\ell}$, which is modular because
$E$ is (modularity, Chapter 14).

### Section 6. Lowering the level

**6.1 `thm:modgalrep:mazur-principle`** (theorem; R, proof idea S). (Mazur's principle.) Let $\ell$ be odd, $f$ a newform of weight $2$ on $\Gamma_0(N)$,
$\lambda\mid\ell$ with $\bar\rho=\bar\rho_{f,\lambda}$ irreducible, and $q\,\|\,N$ a prime with $q\ne\ell$, $\bar\rho$ unramified at $q$ and $q\not\equiv1\pmod\ell$. Then $\bar\rho$ arises from a
newform of weight $2$ on $\Gamma_0(N/q)$. Proof idea (one paragraph): $\bar\rho$ occurs in $J_0(N)[\mathfrak m]$; at $q$ the Neron model of $J_0(N)$ has toric
reduction on the $q$-new part, with character group $X$ (Grothendieck's monodromy pairing; Raynaud); if $\bar\rho$ were $q$-new, $J_0(N)[\mathfrak m]$
would sit in the toric part, where $\Frob_q$ acts as $\pm q$ times something unramified and $\pm1$ on the quotient, and "unramified at $q$" with
$q\not\equiv1\pmod\ell$ forces it to come from the $q$-old part, i.e. from level $N/q$ (Ihara's lemma, 7.4, separates old from new). Reference: Ribet90,
Section 6 (verify); DDT Section 4 (cite the section); Mazur77. Paper: background for "Ribet's theorem" in case (c).

**6.2 `thm:modgalrep:ribet`** (theorem; R, proof idea S). (Ribet's level-lowering theorem.) Let $\ell$ be odd, $f$ a newform of weight $2$ on
$\Gamma_0(N)$ with $\ell\nmid N$, $\lambda\mid\ell$ with $\bar\rho=\bar\rho_{f,\lambda}$ irreducible, and $q\,\|\,N$ with $\bar\rho$ unramified at $q$. Then $\bar\rho$ arises from a newform of weight $2$ on
$\Gamma_0(N/q)$. (Ribet90, Theorem 1.1, which also allows $\ell\mid N$ under conditions stated there, in particular $q\not\equiv1\pmod\ell$, and "finite at
$q$" when $q=\ell$; quote the hypotheses from the source, verify. The paper's case (c) has $\ell\nmid N$, which is the case stated here.)
Proof idea: when $q\equiv1\pmod\ell$, Mazur's principle fails; Ribet passes through an auxiliary prime $r$ and the Shimura curve of
discriminant $qr$, comparing the character groups of $J_0(Nr)$ at $q$ and of the Shimura curve's Jacobian at $r$ (Cerednik-Drinfeld uniformisation,
"Ribet's exact sequence"), and uses multiplicity one. Reference: Ribet90; DDT Section 4; Ribet91 (without multiplicity one). Paper:
case (c) ("this is the case of Ribet's theorem [Ribet90], $q$ exactly dividing the level and $\bar\rho\otimes\chi$ unramified at $q$").

**6.3 `lem:modgalrep:carayol-lemma`** (lemma; R). (Carayol's lemma on characters.) Suppose $\bar\sigma$ arises from an eigenform in $S_k(\Gamma_1(M),\varepsilon)$,
$k\ge2$, and let $\varepsilon'\colon(\Z/M)^\times\to\bar\Q^\times$ be a character with the same reduction modulo $\lambda$ as $\varepsilon$. Then $\bar\sigma$ arises from an eigenform in
$S_k(\Gamma_1(M),\varepsilon')$ (not necessarily new). In particular the character may be taken of order prime to $\ell$ (the Teichmuller lift of $\bar\varepsilon$),
which is the source of "nebentypus of order prime to $\ell$" in 6.4. Reference: Carayol89 (cite the section); DDT Section 4 (the lemma on
changing the character; verify the number). Paper: the optimal-level theorem as quoted in Section 3.

**6.4 `thm:modgalrep:optimal-level`** (theorem; R). (Ribet, Carayol, Diamond; the form of DDT Theorem 3.15, as quoted in the paper.) Let
$\ell$ be odd and $\bar\sigma\colon G_\Q\to\GL_2(\bar\F_\ell)$ irreducible and modular, and if $\ell=3$ assume $\bar\sigma|_{\Gal(\Qbar/\Q(\sqrt{-3}))}$ absolutely irreducible. Then $\bar\sigma$ arises
from a newform of weight $2$ and level $N(\bar\sigma)\ell^{\delta(\bar\sigma)}$ with character of order prime to $\ell$, where $\delta(\bar\sigma)=0$ when $\bar\sigma|_{D_\ell}$ is good (finite flat) and
$\delta(\bar\sigma)=1$ otherwise (DDT's precise definition of "good" includes also an ordinary case; quote it). Remarks for the text: (a) the extra
hypothesis at $\ell=3$ is Diamond's; for $\bar\sigma=\bar\rho_{E,3}$ it excludes exactly the image $N_s(\F_3)$ (Chapter 11, 8.3, 8.6); (b) for $\ell\ge5$ and
$\bar\sigma=\bar\rho_{E,\ell}$ with $\ell\nmid N$, the analogous condition on $\Q(\sqrt{\ell^*})$ is automatic (important_notes.md point 47; Chapter 11, 8.2), though DDT
3.15 does not need it. Reference: DDT Theorem 3.15 (as cited; verify the statement verbatim); Ribet90; Carayol89; Diamond95. Paper:
the optimal-level paragraph of Section 3, cases (a), (b), (c).

**6.5 `cor:modgalrep:optimal-level-E`** (corollary; P given 6.4, 4.1, 5.2 and Chapter 11). Let $\ell$ be odd and $E'/\Q$ of conductor $N'$ with
$\ell\nmid N'$, $\bar\sigma=\bar\rho_{E',\ell}$ irreducible, and if $\ell=3$ image not $N_s(\F_3)$. Then there are a newform $g$ of weight $2$ on $\Gamma_0(N(\bar\sigma))$ (trivial
character) and $\lambda\mid\ell$ with $\bar\rho_{g,\lambda}\simeq\bar\sigma\otimes k_\lambda$, i.e. $a_p(g)\equiv a_p(E')\pmod\lambda$ for every $p\nmid\ell N'$; and $N(\bar\sigma)\mid N'$, with $N(\bar\sigma)$ prime to every
prime at which $\bar\sigma$ is unramified. Proof (P, every step): $\bar\sigma$ is modular (modularity of $E'$), odd, irreducible, absolutely irreducible
(2.4(ii)); $\bar\sigma|_{D_\ell}$ comes from $E'[\ell]$, finite flat, so $\delta=0$ (4.1; Chapter 11, 5.1); 6.4 gives $g$ of weight $2$, level $N(\bar\sigma)$, character $\psi$ of
order prime to $\ell$; $\det\bar\rho_{g,\lambda}=\bar\psi\bar\chi_\ell$ (2.3) and $\det\bar\sigma=\bar\chi_\ell$ give $\bar\psi=1$; reduction modulo $\lambda$ is injective on roots of unity of order
prime to $\ell$, so $\psi=1$; finally 5.2 or Chapter 11, 6.2. Remark: if $\ell\mid N'$ and $\bar\sigma|_{D_\ell}$ is not finite, the level is $N(\bar\sigma)\ell$: for 140b1 at $\ell=5$
($\mathrm I_1$ at $5$), $N(\bar\sigma)=4$ and the form is $f_{20a}$ at level $20$ (checked: $a_7(f_{20a})=2\equiv(1+7)a_7(140\mathrm b1)=-8\pmod5$). Paper: the optimal-level
paragraph ("So in that case $\bar\sigma$ arises from a newform of weight $2$ on $\Gamma_0(N(\bar\sigma))$"; "$\det\bar\sigma=\bar\chi_\ell$ forces the nebentypus ... to be
trivial").

**6.6 `ex:modgalrep:level-lowering`** (worked examples; P for the data, all checked). At $\ell=3$: 121c1 (type $\mathrm{IV}$ at $11$): $N(\bar\rho)=11$, $g=f_{11a}$;
77c1 ($\mathrm I_3$ at $7$, $\mathrm I_2$ at $11$; Ribet's case at $q=7$): $N(\bar\rho)=11$, $g=f_{11a}$; **52a1** ($\mathrm{IV}^*$ at $2$, $\mathrm I_2$ at $13$; the case (a) mechanism at
$q=2$, important_notes.md point 43): $N(\bar\rho)=26$, $g=f_{26b}$ ($a_p(52\mathrm a1)\equiv a_p(26\mathrm b1)\pmod3$ for all $p<80$, $p\ne2,3,13$); 121a1 ($\mathrm{II}$ at $11$):
$N(\bar\rho)=121$, no lowering, but $N(\bar\rho\otimes\chi_{-11})=11$ (via 121c2). At $\ell=5$: 140b1 ($\ell\mid N$, $\delta=1$): level $20$; 11a1: $N(\bar\rho_{11a1,5})=1$, and there is
no newform of weight $2$ and level $1$, consistent with $\bar\rho_{11a1,5}$ being reducible ($E[5]\simeq\Z/5\oplus\mu_5$, Chapter 11), which 6.4 excludes.
Serre conductors are quoted from Chapter 11, 6.3 (and recomputed here, Part 6.6). Paper: Section 3, the Example.

**6.7 `rem:modgalrep:level-lowering-history`** (remark; S). One page: Serre's conjecture (1987) and the epsilon conjecture; Mazur's
principle; Ribet's theorem and Fermat's Last Theorem (via the Frey curve, stated in one sentence); Carayol's and Diamond's
refinements leading to 6.4; the role of multiplicity one ($J_0(N)[\mathfrak m]$ two-dimensional, Chapter 14) and Ribet91 removing it. Reference:
Ribet90; Ribet91; Diamond95; DDT Section 4; Serre87. Paper: Section 3 (background).

### Section 7. Raising the level

**7.1 `thm:modgalrep:level-raising`** (theorem; P for necessity, R for sufficiency). (Ribet's level-raising theorem.) Let $f$ be a newform
of weight $2$ on $\Gamma_0(N)$, $\lambda\mid\ell$ with $\ell$ odd and $\bar\rho=\bar\rho_{f,\lambda}$ irreducible, and $q$ a prime with $q\nmid N\ell$. Then $\bar\rho$ arises from a newform $g$ of
weight $2$ on $\Gamma_0(M)$ with $M\mid Nq$ and $q\mid M$ (i.e. new at $q$) **iff** $a_q(f)^2\equiv(q+1)^2\pmod\lambda$; and then $a_q(f)\equiv(q+1)a_q(g)\pmod{\lambda'}$ with $a_q(g)=\pm1$.
Necessity (P): $g$ is of type (St) at $q$ (3.5), so $\bar\rho_g(\Frob_q)$ has eigenvalues $a_q(g)q$ and $a_q(g)$ (3.5, (St)); $\bar\rho\simeq\bar\rho_g$ is unramified at $q$ with
trace $a_q(f)$, so $a_q(f)\equiv a_q(g)(q+1)$ and $a_q(f)^2\equiv(q+1)^2$. Sufficiency (R): Ribet84 (the theorem announced at the 1983 ICM; check the
hypotheses on $\ell$ there), DiamondTaylor94 for the general form and for raising the level by $q^2$ (add to `bib/ch15.bib`); the proof uses
Ihara's lemma (7.4) and multiplicity one. Paper: Section 4.1 and Theorem thm:dfg14 ("Wiles's level-raising factor"), the remark after
Theorem thm:quant ("the level is raised ... the price is the level-raising Euler factor"); Lemma lem:old, case $p\,\|\,N$ unramified (the same
congruence read backwards: $X^2-a_p(h)X+p\equiv(X-a_p(f)p)(X-a_p(f))$).

**7.2 `prop:modgalrep:level-raising-factor`** (proposition; P). Let $p\nmid N$, $\alpha,\beta$ the roots of $X^2-a_p(f)X+p$. Then
$$\Bigl(1-\frac{\alpha}{\beta p}\Bigr)\Bigl(1-\frac1p\Bigr)\Bigl(1-\frac{\beta}{\alpha p}\Bigr)=\frac{p-1}{p}\cdot\frac{(p+1)^2-a_p(f)^2}{p^2},$$
a nonzero rational (algebraic) number ($|\alpha/\beta|=1$ by Ramanujan-Petersson, Chapter 12, 6.5). This is $L_p^{\nv}(A_f,1)^{-1}=L_p(A_f,1)^{-1}$ at a good $p$
(Chapter 19's normalisation, geometric Frobenius; the eigenvalues $\alpha/\beta,1,\beta/\alpha$ on $\ad V$ are the same for both Frobenii). At a
multiplicative $p$ the factor is $1-p^{-2}$; at an additive $p$ the naive factor is $1$. For $\ell\ne p$ its $\ell$-adic valuation is
$v_\ell(p-1)+v_\lambda((p+1)^2-a_p^2)$: the second term is positive iff the level-raising condition of 7.1 holds; the first records congruences at
level $Np^2$ with forms of type (RPS) whose inertial character has $\ell$-power order (possible only if $p\equiv1\pmod\ell$; DiamondTaylor94, stated
as a remark, verify). Proof of the identity: $\alpha\beta=p$, $\alpha^2+\beta^2=a_p^2-2p$, so $(1-\frac\alpha{\beta p})(1-\frac\beta{\alpha p})=1-\frac{a_p^2-2p}{p^2}+\frac1{p^2}=\frac{(p+1)^2-a_p^2}{p^2}$
(Chapter 2, 11.4 has the same identity). Paper: Theorem thm:dfg14 and the paragraph after it, the table of Section 1 ($\mathrm I_0^*$ row, with
$a_q(E')$), Lemma lem:euler ($\mathrm I_0^*$), Theorem thm:quant Step 3.

**7.3 `thm:modgalrep:dfg14`** (theorem; R; the paper's Theorem thm:dfg14, stated here, explained in Chapter 20). (DFG04, Proposition
1.4(c), as cited.) For $f$ with rational coefficients, $\ell\nmid2N$, $\bar\rho_f$ irreducible and $\Sigma$ a finite set of primes:
$\eta^\Sigma_{f,\lambda}=\eta^\emptyset_{f,\lambda}\prod_{p\in\Sigma}L_p^{\nv}(A_f,1)^{-1}$; adding an additive prime changes nothing, a good prime contributes 7.2, a multiplicative one $1-p^{-2}$.
The lattices, the pairing and the ideals are defined in Chapter 20 (from the paper's Section 4.1). Reading for this chapter: the
$\Sigma$-depleted form $f^\Sigma$ of level $M^\Sigma=M\prod_{p\in\Sigma}p^{\delta_p}$ (3.5) is "$f$ with its level raised at $\Sigma$", and the change of the congruence
ideal is the level-raising factor. Paper: Theorem thm:dfg14, proof of Theorem thm:main, Theorem thm:quant Step 3, the remark after
Theorem thm:quant.

**7.4 `lem:modgalrep:ihara`** (lemma; R). (Ihara's lemma, in Ribet's form.) For $q\nmid N$ and $\mathfrak m$ a maximal ideal of $\T(N)$ with $\bar\rho_{\mathfrak m}$
irreducible, the degeneracy map $J_0(N)^2\to J_0(Nq)$, $(x,y)\mapsto\alpha_1^*x+\alpha_q^*y$, has kernel contained in the Shimura subgroup embedded
antidiagonally, which is Eisenstein; equivalently $H^1(X_0(N),\F_\ell)^2_{\mathfrak m}\to H^1(X_0(Nq),\F_\ell)$ is injective. Reference: Ribet84 (verify the theorem
number); DDT Section 4 (cite); Ihara's original (not added). Paper: background to Theorem thm:dfg14 (Chapter 20) and to 7.1.

**7.5 `ex:modgalrep:level-raising`** (worked example; P, checked with PARI's `mfinit`, `mfeigenbasis`, `mffields` and reduction modulo
all primes above $\ell$). $f=f_{11a}$, $\ell=3$: $(q+1)^2-a_q^2$ is $35,60,180,320,400$ for $q=5,7,13,17,19$; it is divisible by $3$ exactly for $q=7,13$; and
among the newforms of level $11q$ exactly these $q$ give a form congruent to $f_{11a}$ modulo a prime above $3$: at level $77$ the rational form
$f_{77c}$ (with $a_7(77\mathrm c1)=-1$ and $a_7(11\mathrm a1)=-2\equiv8\cdot(-1)\pmod3$); at level $143$ a newform with quartic coefficient field, at one of the two
primes above $3$ (and not the rational form of 143a1); at levels $55$, $187$, $209$ none. $f=f_{20a}$, $\ell=5$ ($\bar\rho_{20a,5}$ irreducible): $q=7$ gives $60$ and
$f_{140b}$; $q=3$ gives $12$ and no form at level $60$. Paper: background to Theorem thm:dfg14 and to the Example (the congruence
$11\mathrm a\equiv77\mathrm c\pmod3$ underlies 539c1, whose twist is 77c1).

### Section 8. Congruences between eigenforms: the congruence criterion and the oldform lemma

**8.1 `def:modgalrep:congruence-number`** (definition and recollection; P for the remarks, R for Agashe-Ribet-Stein). For a newform
$f$ of weight $2$ on $\Gamma_0(N)$ with rational coefficients (so $f=f_E$): $f^\perp\subset S_2(\Gamma_0(N))$ is the orthogonal complement of $\C f$ for the Petersson
product; it is $\T$-stable and equals the sum of the generalised eigenspaces of $\T\otimes\C$ for the systems of eigenvalues other than $\phi_f$
(Chapter 13: $f$ is an eigenvector of the adjoints $T_n^*$, since $T_n^*=T_n$ for $(n,N)=1$ and $U_p^*=w_NU_pw_N$ with $w_Nf=\pm f$); the **congruence number**
$r=r_E$ is the largest integer $r$ such that $f\equiv g\pmod r$ coefficientwise for some $g\in S_2(\Gamma_0(N);\Z)\cap f^\perp$ (ARS12, Section 2; the paper's
definition in Sections 1 and 3). Agashe-Ribet-Stein (ARS12, Theorem 2.2, as cited; Chapter 14): $\deg\varphi_{E_0}\mid r$ and $v_p(\deg\varphi_{E_0})=v_p(r)$ for
every $p$ with $p^2\nmid N$. Example (computed here, Part 6.6): for 99a1 (= ARS12's 99A1, $N=3^2\cdot11$), $\deg\varphi=4$ and $r=12$, so $v_3$ differs, as
$9\mid N$ allows. Paper: Section 1, Section 3 (preamble), Lemma lem:crit, the remark after the Example (99A1), Lemma lem:hecke.

**8.2 `lem:modgalrep:crit`** (lemma, the paper's Lemma lem:crit; P, every step expanded). Let $f$ be as in 8.1, $\T$ the full Hecke algebra of
level $N$, $\phi_f\colon\T\to\Z$, $T_n\mapsto a_n(f)$, $I=\ker\phi_f$, and $J=\Ann_\T(f^\perp)$. Then: (i) $I\cap J=0$, $J=\Ann_\T(I)$, and $\T/(I+J)$ is cyclic of order $r$;
equivalently $r\Z=\phi_f(J)=\phi_f(\Ann_\T I)$, the congruence ideal of $\phi_f$ (Chapter 3, 11.1). (ii) If there are a number field with ring of
integers $\mathcal O$, a prime $\lambda\mid\ell$ of $\mathcal O$, and a normalised eigenform $g\in(S_2(\Gamma_0(N))\otimes\Qbar)\cap f^\perp$ of **all** of $\T$ with coefficients in $\mathcal O$ and
$a_n(g)\equiv a_n(f)\pmod\lambda$ for **every** $n\ge1$, then $\ell\mid r$. (iii) The same holds after $\otimes\Zl$: $\T_\ell/(I_\ell+J_\ell)\simeq\Z/\ell^{v_\ell(r)}$, $\ell^{v_\ell(r)}$ generates
$\phi_f(\Ann_{\T_\ell}I_\ell)$, and it is the largest $\ell^t$ with $f\equiv h\pmod{\ell^t}$ for some $h\in S_2(\Gamma_0(N);\Zl)\cap(f^\perp\otimes\Ql)$. Proof (the paper's, with every
step written out): (1) $\T\otimes\Q=\Q\times\T'$, $\T'$ the image of $\T\otimes\Q$ in $\End(f^\perp)$: the $\phi_f$-generalised eigenspace of $\T$ on $S_2(\Gamma_0(N))$ is the
line $\C f$ (strong multiplicity one, 1.2(iii), (iv): the system of $T_p$-eigenvalues, $p\nmid N$, of $f$ occurs on no $h(dz)$ with $h\ne f$), so the
idempotent of $\T\otimes\Q$ attached to $\phi_f$ (Chapter 3, 10.1) projects onto $\Q f$ along $f^\perp$; hence $I=\T\cap(0\times\T')$, $J=\T\cap(\Q\times0)$, $I\cap J=0$,
$J=\Ann_\T I$, and $\T/(I+J)\simeq\phi_f(\T)/\phi_f(J)=\Z/\phi_f(J)$ is cyclic, of order $r'$ say. (2) The pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$, $(g,t)\mapsto a_1(tg)$, is
perfect (Ribet83, Theorem 2.2; AU96, Lemma 2.1; Chapter 13); under it (Chapter 3, 9.6) $S_2[I]=\Hom(\T/I,\Z)=\Z f$ ($f$ is primitive: $a_1(f)=1$) and
$S_2[J]=\Hom(\T/J,\Z)=L:=f^\perp\cap S_2(\Gamma_0(N);\Z)$. (3) Dualising $\T\hookrightarrow\T/I\times\T/J$, with cokernel $\T/(I+J)$ (Chapter 3, 5.7, 9.6(iii)),
$[S_2(\Gamma_0(N);\Z):\Z f\oplus L]=r'$. (4) The quotient embeds in $\Q f/\Z f$ by projection along $f^\perp$ (Chapter 3, 5.8), so it is cyclic, generated by the
class of an $h$ with projection $f/r'$; then $r'h=f+g_0$ with $g_0\in L$, so $f\equiv-g_0\pmod{r'}$ and $r'\le r$; conversely $f\equiv g_1\pmod r$ with $g_1\in L$ makes
$(f-g_1)/r$ integral with projection $f/r$, of order exactly $r$ in the quotient, so $r\mid r'$. Hence $r=r'$. (5) For (ii): $\phi_g\colon\T\to\mathcal O$ kills $J$
($g\in f^\perp$) and $\phi_g\equiv\phi_f\pmod\lambda$ on all of $\T$ (because $a_n(g)\equiv a_n(f)$ for **every** $n$, $U_p$ included), so $\phi_g(I)\subset\lambda$; thus $I+J\subset\ker(\T\to\mathcal O/\lambda)$,
whose image is a subring of a finite field, hence a field: a maximal ideal of residue characteristic $\ell$; so $\ell\mid\#\T/(I+J)=r$. (6) Over $\Zl$: $\Zl$ is flat
over $\Z$, the pairing stays perfect, and steps (1) to (5) hold verbatim (Chapter 3, 3.4, 11.1(v); Chapter 12, 11.4(iii) for the $q$-expansion side).
Writer's notes: the congruence in (ii) must hold for all $n$, not only for primes $p\nmid N$: this is why Lemma lem:old exists; the
hypothesis "rational coefficients" is the paper's setting ($f=f_E$); the general version (coefficients in $\mathcal O_f$, $\phi_f\colon\T\to\mathcal O_f$) is Chapter 20's
restatement. Paper: Lemma lem:crit, Lemma lem:old (its conclusion), Lemma lem:hecke, Theorem thm:twist, Theorem thm:quant Step 1.
Cross-references: Chapter 14 (the same congruence number from the modular-degree side), Chapter 20 (restated as a statement about
congruence modules; Chapter 20 does not reprove it).

**8.3 `lem:modgalrep:old`** (lemma, the paper's Lemma lem:old; P, every case written out). Let $f$ be as in 8.1, $\ell$ odd with $\ell\nmid N$ and
$\bar\rho=\bar\rho_{E,\ell}$ irreducible (hence absolutely irreducible: 2.4(ii), important_notes.md point 10). Let $h\ne f$ be a newform of weight $2$ on
$\Gamma_0(M)$, $M\mid N$, with coefficients in $\mathcal O$, and $\lambda\mid\ell$ with $a_p(h)\equiv a_p(f)\pmod\lambda$ for all primes $p\nmid\ell N$. Assume $p\nmid M$ for every prime
$p\,\|\,N$ at which $\bar\rho$ is unramified. Then, after enlarging $\mathcal O$ and $\lambda$, the span $V_h$ of the $h(dz)$, $d\mid N/M$, contains a normalised
eigenform $g$ of all of $\T$ with $a_n(g)\equiv a_n(f)\pmod\lambda$ for every $n\ge1$; it lies in $f^\perp$; consequently $\ell\mid r$ (8.2(ii)). Proof:
(1) $V_h$ is $\T$-stable and orthogonal to $f$ (1.2(iv); for $M=N$ use $h\ne f$). (2) On $V_h$: $T_n$ acts by $a_n(h)$ for $(n,N)=1$; $U_p$ acts by $a_p(h)$
if $p\mid M$ and $v_p(M)=v_p(N)$; for $p\mid N/M$ with $e_p=v_p(N/M)$, on $V_{h,p}=\langle h(p^jz):0\le j\le e_p\rangle$: $U_ph(p^jz)=h(p^{j-1}z)$ ($j\ge1$),
$U_ph=a_p(h)h-p\,h(pz)$ if $p\nmid M$, $U_ph=a_p(h)h$ if $p\mid M$ (Chapter 13). (3) Eigenvalues and eigenvectors of $U_p$ on $V_{h,p}$ (Chapter 3,
10.7(v); Chapter 13):

| situation at $p\mid N/M$ | characteristic polynomial | eigenvalue | eigenvector |
|-|-|-|-|
| $p\nmid M$ | $X^{e_p-1}(X^2-a_pX+p)$ | $\alpha_p$, $\beta_p$ | $h-\beta_ph(pz)$, $h-\alpha_ph(pz)$ |
| $p\nmid M$, $e_p\ge2$ | | $0$ | $h-a_p(h)h(pz)+p\,h(p^2z)$ |
| $p\,\|\,M$ | $X^{e_p}(X-a_p)$ | $a_p(h)=\pm1$; $0$ | $h$; $h-a_p(h)h(pz)$ |
| $p^2\mid M$ | $X^{e_p+1}$ | $0$ | $h$ ($a_p(h)=0$) |

$U_p$ is not semisimple when $0$ is a repeated root, but each listed eigenvalue has an eigenvector. (4) $V_h=\bigotimes_{p\mid N/M}V_{h,p}$ compatibly
with the $U_p$, and $\T$ is commutative, so for every choice of eigenvalues $\mu_p$ ($p\mid N/M$) there is a common eigenform $g\in V_h\otimes\Qbar$ of all
of $\T$ with $U_pg=\mu_pg$ ($p\mid N/M$), $U_pg=a_p(h)g$ (other $p\mid N$), $T_ng=a_n(h)g$ ($(n,N)=1$) (Chapter 3, 10.8); normalise $a_1(g)=1$; its
coefficients lie in $\mathcal O[\alpha_p]$. (5) Choice of $\mu_p$ and the congruence at each prime $p$:
  * $p\nmid\ell N$: $a_p(g)=a_p(h)\equiv a_p(f)$ by hypothesis; so $\bar\rho_{h,\lambda}\simeq\bar\rho$ (2.5(ii)).
  * $p=\ell$: weight $2$, levels prime to $\ell$; $a_\ell(h)\equiv a_\ell(f)$ by 4.2(iii).
  * $p^2\mid N$: $a_p(f)=0$ (3.5). If $v_p(M)=v_p(N)$ then $a_p(h)=0$ (3.5 for $h$; AtkinLehner70 Theorem 3). Otherwise $e_p\ge1$, and $e_p\ge2$ when $p\nmid M$, so
    $0$ is an eigenvalue: $\mu_p=0$.
  * $p\,\|\,N$, $\bar\rho$ unramified at $p$: $p\nmid M$ by hypothesis, $e_p=1$, $\mu_p\in\{\alpha_p,\beta_p\}$. By 3.5 (St) for $f$, $\bar\rho(\Frob_p)$ has eigenvalues
    $a_p(f)p$, $a_p(f)$; $\bar\rho_h\simeq\bar\rho$ is unramified at $p$ with characteristic polynomial $X^2-a_p(h)X+p$ (2.1(ii)(b)), so
    $X^2-a_p(h)X+p\equiv(X-a_p(f)p)(X-a_p(f))$ modulo $\lambda$, and one of $\alpha_p,\beta_p$ is $\equiv a_p(f)$ modulo a prime above $\lambda$ in $\mathcal O[\alpha_p]$: take it as $\mu_p$.
    (This is the level-raising congruence 7.1 read backwards.)
  * $p\,\|\,N$, $\bar\rho$ ramified at $p$: then $p\mid M$ (else $\bar\rho_h$ would be unramified at $p$, 2.1(ii)(a)), so $v_p(M)=1=v_p(N)$ and $a_p(g)=a_p(h)=\pm1$. Both
    $\bar\rho|_{D_p}$ and $\bar\rho_h|_{D_p}$ are extensions of an unramified character by its $\bar\chi_\ell$-twist, with $\Frob_p$ acting on the unramified quotient by $a_p(f)$,
    resp. $a_p(h)$ (3.5 (St), on lattices), both non-split because ramified; a non-split extension of two characters has a unique stable line
    (Chapter 4, 3.6), so the isomorphism $\bar\rho|_{D_p}\simeq\bar\rho_h|_{D_p}$ matches the lines and the quotients: $a_p(h)\equiv a_p(f)$. (Valid also when $p\equiv1\pmod\ell$, where the two
    characters coincide.)

(6) From primes to all $n$: $a_{mn}=a_ma_n$ for coprime $m,n$ (both $f$ and $g$ are normalised eigenforms of all $T_n$); $a_{p^k}=a_p^k$ for $p\mid N$ ($U_{p^k}=U_p^k$);
the recursion $a_{p^{k+1}}=a_pa_{p^k}-pa_{p^{k-1}}$ for $p\nmid N$ (including $p=\ell$). Hence $a_n(g)\equiv a_n(f)\pmod\lambda$ for all $n$. Paper: Lemma lem:old, cases
(a), (b), (c). Writer's note: the paper's phrase "$\bar\rho_h\simeq\bar\rho$ by Chebotarev and Brauer-Nesbitt, $\bar\rho$ being irreducible" is corrected by
"(hence absolutely irreducible ...) over a common finite extension of $\F_\ell$" in a `paperlink` (important_notes.md point 10); for a weight-two
form $\alpha_p\ne\beta_p$ (ColemanEdixhoven), though the argument does not need it.

**8.4 `ex:modgalrep:old-examples`** (worked examples; P, checked). (a) **Unramified case $p\,\|\,N$:** $f=f_{77c}$, $\ell=3$, $h=f_{11a}$ ($M=11$, $N/M=7$, $7\,\|\,77$ and
$\bar\rho_{77c1,3}$ unramified at $7$ since $3\mid n_7=3$): $X^2+2X+7\equiv(X+1)^2\pmod3$, the roots $\alpha,\beta=-1\pm\sqrt{-6}$ are both $\equiv-1=a_7(77\mathrm c1)$ modulo the prime
$(3,\sqrt{-6})$ of $\Z[\sqrt{-6}]$; $g=h-\beta h(7z)$ satisfies $g\equiv f_{77c}$ modulo $(3,\sqrt{-6})$ for every $n\le3000$ (Sturm bound $16$ at level $77$, so for all $n$);
hence $3\mid r(77\mathrm c1)$, and indeed $r=\deg\varphi=6$. (b) **Additive case $p^2\mid N$:** $f=f_{52a}$, $\ell=3$, $h=f_{26b}$ ($M=26$, $N/M=2$, $2\,\|\,M$, $e_2=1$): $\mu_2=0$,
$g=h-a_2(h)h(2z)=h-h(2z)$, and $g\equiv f_{52a}\pmod3$ for all $n\le400$ (Sturm bound $14$ at level $52$, so for all $n$); $\deg\varphi_{52a1}=3$. (c) **The Example of
Section 3** (8.3 with $M=N$): $V_h=\C h$ and $g=h$; see 9.4. Paper: Lemma lem:old; the Example of Section 3.

### Section 9. Proof of Theorem thm:qual; the Example; the remark on $\ell\mid N$

**9.1 `thm:modgalrep:qual`** (theorem, the paper's Theorem thm:qual, with case (a) extended to $q=2$; P given the R items 2.1, 3.4, 4.2,
6.4 and Agashe-Ribet-Stein). Let $E/\Q$ have conductor $N$, $\ell$ an odd prime with $\ell\nmid N$, $\bar\rho_{E,\ell}$ irreducible and, if $\ell=3$, absolutely
irreducible on $\Gal(\Qbar/\Q(\sqrt{-3}))$ (equivalently image not $N_s(\F_3)$, Chapter 11, 8.6). Let $q\ne\ell$ be a prime at which $E$ has additive reduction of
one of the kinds: (a) type $\mathrm{IV}$ or $\mathrm{IV}^*$, $\ell=3$, and $q\ge5$ **or $q=2$** (the paper: $q\ge5$; the extension is important_notes.md point 43,
proved in Chapter 11, 4.4); (b) type $\mathrm{II}$ or $\mathrm{II}^*$, $q\ge5$, $\ell=3$; (c) type $\mathrm I_n^*$ with $\ell\mid n$, $q$ odd. Then $\ell$ divides the modular degree of the
$X_0(N)$-optimal curve $E_0$ of the isogeny class. Remarks: for $\ell\ge5$ only irreducibility is used; in case (a) at $q=2$ the hypothesis $3\nmid N$
excludes $q=3$; checked on the tables: all $1{,}051$ optimal curves of conductor below $10{,}000$ with type $\mathrm{IV}$ or $\mathrm{IV}^*$ at $2$, $3\nmid N$ and mod $3$ image
neither reducible nor 3Ns have $3\mid\deg\varphi$ (Part 6.6). Paper: Theorem thm:qual (statement in Section 1.5), Section sec:proof.

**9.2 `sec:modgalrep:proof-qual`** (the proof of 9.1, a subsection whose `proof` environment has numbered steps; P). Common start: $f=f_E$, $r=r_{E_0}$; as
$\ell\nmid N$, $v_\ell(\deg\varphi_{E_0})=v_\ell(r)$ (8.1), so it suffices to find $h$ as in Lemma lem:old (8.3). $\bar\rho=\bar\rho_{E,\ell}$.
* **Case (a).** $v_q(N)=2$ (type $\mathrm{IV}$, $\mathrm{IV}^*$ are additive and tame: Chapter 11, 4.3 for $q\ge5$, 4.4 for $q=2$). By Lemma lem:IV (Chapter 11, 4.3; 4.4 at
  $q=2$) the Serre conductor $M=N(\bar\rho)$ has $v_q(M)=1$, and $M\mid N$ (5.2), so $M\mid N/q$ and $M<N$. By 6.5 there is a newform $g$ on $\Gamma_0(M)$ with
  $\bar\rho_g\simeq\bar\rho$. Put $h=g$: $h\ne f$ (levels), $M\mid N$, and $p\nmid M$ for every $p$ at which $\bar\rho$ is unramified (5.1). Lemma lem:old gives $3\mid r$.
* **Case (b).** $v_q(N)=2$, $\chi=\chi_q$, $E'=E^{(q)}$. By Lemma lem:twist (i), (ii) (Chapter 10, 8.1, 8.2), $E'$ has type $\mathrm{IV}^*$ or $\mathrm{IV}$ at $q$, the
  same types as $E$ elsewhere, conductor $N$. Its newform is $f_{E'}=f^\chi$ (2.7(iv)), and here $f^\chi=f\otimes\chi$ **because** $a_q(f^\chi)=0$ ($q^2\mid N$, 3.5; C4) (the
  paper's "$f'=f\otimes\chi$, a newform on $\Gamma_0(N)$" is right in this case, but not by Atkin-Li, which needs $q^2\nmid M$). $\bar\rho_{E',3}=\bar\rho\otimes\chi$ satisfies the
  hypotheses of 6.5 (irreducibility and the condition at $\Q(\sqrt{-3})$ are twist-invariant; Chapter 11, 1.3). Lemma lem:IV for $E'$: $M=N(\bar\rho\otimes\chi)$
  has $v_q(M)=1$, $M\mid N/q$. 6.5 gives $g$ on $\Gamma_0(M)$ with $a_p(g)\equiv\chi(p)a_p(f)\pmod\lambda$ for $p\nmid3N$. As $q\,\|\,M$, $h:=g\otimes\chi=g^\chi$ is a newform on
  $\Gamma_0(Mq)$ (3.8(a), Atkin-Li), $Mq\mid N$, and $a_p(h)=\chi(p)a_p(g)\equiv a_p(f)$ for $p\nmid3N$. **$h\ne f$** (important_notes.md point 20): if $h=f$ then
  $f\otimes\chi=h\otimes\chi=g^{(q)}$ (C4: $(g\otimes\chi)\otimes\chi=g^{(q)}$), so $f_{E'}=f\otimes\chi$ and $g$ have the same $a_p$ for all $p\ne q$, hence $f_{E'}=g$ by strong multiplicity one;
  but their levels are $N$ and $M<N$. (The paper's "$g=h\otimes\chi=f\otimes\chi$" is literally false: $h\otimes\chi$ is the $q$-depletion of $g$.) Hypothesis of Lemma
  lem:old: if $p\,\|\,N$ and $\bar\rho$ is unramified at $p$, then $p\ne q$, $\bar\rho\otimes\chi$ is unramified at $p$, so $p\nmid M$ and $p\nmid Mq$. Lemma lem:old gives $3\mid r$.
* **Case (c).** $v_q(N)=2$, $\chi=\chi_q$, $E'=E^{(q)}$ of type $\mathrm I_n$ at $q$ and conductor $N/q$ (Lemma lem:twist (ii)). Here $f=(f_{E'})^\chi=f_{E'}\otimes\chi$ (Atkin-Li,
  3.8(a), as $q\,\|\,N/q$), while **$f\otimes\chi=f_{E'}^{(q)}$ is not a newform on $\Gamma_0(N/q)$** ($a_q(f_{E'})=\pm1$; new point N1, Part 7.1); the paper's "$f'=f\otimes\chi$ is a
  newform of weight $2$ on $\Gamma_0(N/q)$" must be read as "$f'=f_{E'}=f^\chi$". By Lemma lem:tamagawa-exp for $E'$ (Chapter 11, 3.3), $\bar\rho\otimes\chi=\bar\rho_{E',\ell}$ is
  unramified at $q$ ($\ell\mid n$), so $M=N(\bar\rho\otimes\chi)$ is prime to $q$ and $M\mid N/q^2$. 6.5 (here the step at $q$ is Ribet's theorem 6.2: $q$ exactly divides
  $N/q$ and $\bar\rho\otimes\chi$ is unramified at $q$) gives $g$ on $\Gamma_0(M)$ with $a_p(g)\equiv\chi(p)a_p(f)$ for $p\nmid\ell N$. As $q\nmid M$, $h:=g\otimes\chi=g^\chi$ is a newform on
  $\Gamma_0(Mq^2)$ (3.8(a)), $Mq^2\mid N$, congruent to $f$ at all $p\nmid\ell N$. **$h\ne f$**: if $h=f$ then $g^{(q)}=h\otimes\chi=f\otimes\chi=f_{E'}^{(q)}$, so $g=f_{E'}$ by strong multiplicity
  one, of levels $M$ and $N/q\ne M$. The hypothesis of Lemma lem:old holds as in (b). So $\ell\mid r$.
* **Conclusion.** $\ell\mid r$ and $v_\ell(\deg\varphi_{E_0})=v_\ell(r)$. $\square$
Paper: Section sec:proof (all of it).

**9.3 `rem:modgalrep:why-these-types`** (remark; P). Why exactly these types (Chapter 11, 4.5, table): Theorem thm:qual needs a type whose
twist by $\chi_q$ (or itself) has Serre exponent smaller than $v_q(N)$, so that the level can be lowered and raised back to a *different*
newform. (i) Types $\mathrm{III}$, $\mathrm{III}^*$: Serre exponent $2$ for $\bar\rho$ and for $\bar\rho\otimes\chi_q$; no lowering (these are the 3Ns-relevant types, Section
sec:anomaly). (ii) Type $\mathrm I_0^*$: the twist $E'$ has good reduction at $q$, $M\mid N/q^2$, but 6.5 may return $g=f_{E'}$ itself (when $N(\bar\rho\otimes\chi)=N/q^2$), and
then $h=g^\chi=f$: no new congruence; the $\mathrm I_0^*$ term is reached through level raising instead (Theorem thm:quant; the factor $(q+1)^2-a_q(E')^2$
of 7.2; example 539d1 in 10.4). (iii) Type $\mathrm I_n^*$ with $\ell\nmid n$: $\bar\rho\otimes\chi$ is ramified at $q$ with exponent $1$, $M$ has $q^1$, $h=g^\chi$ has $q^2$, and
6.5 can return $g=f_{E'}$, giving $h=f$; again Theorem thm:quant handles it. (iv) Types $\mathrm{II}$, $\mathrm{IV}$ at $\ell\ge5$: $\bar\rho_{E,\ell}$ has Serre exponent $2$ (no
$\ell$-torsion in $\Phi_q$), nothing to lower. Paper: Section 1.5 ("For $\ell\ge5$ Theorem thm:qual needs only ..."), the remark after Theorem
thm:quant ((1): "neither is in Theorem thm:qual").

**9.4 `ex:modgalrep:paper-example`** (worked example; P, all data checked; the paper's Example after case (c)). Table to typeset:

| $E$ | case, $\ell$ | type at $q$ | twist $E^{(q)}$ (curve) | $N(\bar\rho\otimes\chi_q)$, $g$ | $h=g^{\chi_q}$ | $f_E\equiv h$ | $\deg\varphi$ | bound |
|-|-|-|-|-|-|-|-|-|
| 121a1 | (b), $3$ | $\mathrm{II}$ at $11$ | 121c2 ($\mathrm{IV}^*$) | $11$, $f_{11a}$ | $f_{121d}=f_{11a}\otimes\chi_{-11}$ | mod $3$, all $n$ (Sturm $22$) | $6$ | $e_3=v_3(12)=1$ |
| 539c1 | (c), $3$ | $\mathrm I_3^*$ at $7$ | 77c1 ($\mathrm I_3$) | $11$, $f_{11a}$ | $f_{539d}=f_{11a}\otimes\chi_{-7}$ | mod $3$, all $n$ (Sturm $112$) | $2^5\cdot3^2$ | $e_3+t_3=1+1$ |
| 980i1 | (c), $5$, **$5\mid N$** | $\mathrm I_5^*$ at $7$ | 140b1 ($\mathrm I_5$) | $4$, level $20$ ($\delta=1$), $f_{20a}$ | $f_{980g}=f_{20a}\otimes\chi_{-7}$ | mod $5$, all $n$ (Sturm $336$) | $2^6\cdot3^2\cdot5$ | $t_5=1$, $e_5=0$ |
| 121c1 | (a), $3$ | $\mathrm{IV}$ at $11$ | (none needed) | $11$, $f_{11a}$ | $h=f_{11a}$, $g=h-h(11z)$ | mod $3$, all $n$ (Sturm $22$) | $6$ | $e_3=1$ |
| 52a1 | (a) at $q=2$, $3$ | $\mathrm{IV}^*$ at $2$ | (none needed) | $26$, $f_{26b}$ | $h=f_{26b}$, $g=h-h(2z)$ | mod $3$, all $n$ (Sturm $14$) | $3$ | $e_3(E,2)=1$ |

Points to make in the text: (i) the congruences hold for **every** $n$, not only for the primes checked in the paper, by Sturm's bound,
since both sides lie in $S_2(\Gamma_0(N))$ (Chapter 12, 11.5; important_notes.md point 46); in the Lemma lem:old language $M=N$ in the first three
rows, $V_h=\C h$ and $g=h$. (ii) The curve-level twists are as in the second column (important_notes.md B8): the twist of 121a1 by $-11$ is 121c2
(type $\mathrm{IV}^*$; 121c1, the optimal curve, has type $\mathrm{IV}$); $f_{11a}\otimes\chi_{-11}$ is the form of the class 121d, whose curve 121d2 is the twist of
11a1 ($\mathrm I_5^*$) and 121d1 the twist of 11a3 ($\mathrm I_1^*$); $f_{11a}\otimes\chi_{-7}$ is the form of 539d, 539d2 being the twist of 11a1; the twist of 20a1 by $-7$ is
980g2. (iii) 980i1 has $5\mid980$, so it lies outside the hypotheses of Theorem thm:qual (and of Theorem thm:main) at $\ell=5$: it illustrates the
congruence, not the theorem (important_notes.md point 21); the level of $g$ is $N(\bar\rho)\cdot5$ because $\bar\rho_{140b1,5}|_{D_5}$ is not finite (6.5, remark).
(iv) For 121c1 (case (a) with $V_h$ spanned by $h(z)$, $h(11z)$, $11\,\|\,M=11$, $e_{11}=1$): $\mu_{11}=0$, $g=h-a_{11}(h)h(11z)=f_{11a}-f_{11a}(11z)$, the $11$-depletion of
$f_{11a}$ ($a_{11}(f_{11a})=1$), congruent to $f_{121c}$ modulo $3$ for every $n$ (checked for $n\le3000$; Sturm bound $22$). (v) Modular degrees from `degphi`; $e_\ell$, $t_\ell$ from Definition def:terms (Chapter 19). Paper: the Example of Section 3, Theorem
thm:qual, Definition def:terms.

**9.5 `rem:modgalrep:l-divides-N`** (remark; P for the data). The paper's remark after the Example: $\ell\nmid N$ is used (i) in the
optimal-level theorem ($\delta=0$, weight $2$: 6.5), (ii) in Lemma lem:old at $p=\ell$ (4.2 needs level prime to $\ell$), (iii) to pass from $r$ to
$\deg\varphi$, which needs only $\ell^2\nmid N$ and fails without it: 99a1 (ARS12's 99A1, $N=9\cdot11$) has $\deg\varphi=4$, $r=12$ (both recomputed here,
Part 6.6). The data statement "so do they at $q=3$ in cases (a) and (b), where Lemma lem:IV does not apply because the ramification is
wild" concerns $q=\ell=3$, i.e. curves with $3\mid N$: the obstruction there is first that $q=\ell$ (inertia at $3$ acts on $T_3E$ through an infinite
group, so neither Kraus's defect nor Lemma lem:IV makes sense, and Theorem thm:qual requires $q\ne\ell$), and only secondarily wildness
(new point N2, Part 7.1). Paper: the remark after the Example.

### Section 10. Twisting and the levels in Theorems thm:twist and thm:quant

**10.1 `prop:modgalrep:twist-map`** (proposition; P given Chapter 13 and 2.7). Let $S$ be a finite set of odd primes, $D=\prod_{q\in S}q$, $\chi_S=\prod_{q\in S}\chi_q$,
and $\iota=\iota_S\colon h\mapsto h\otimes\chi_S=\sum\chi_S(n)a_n(h)q^n$. From Chapter 13 (cited, not reproved): $\iota$ maps $S_2(\Gamma_0(M))$ into $S_2(\Gamma_0(\operatorname{lcm}(M,D^2)))$ ($\chi_S^2=1$),
preserves integrality, and $\iota\circ T_p=\chi_S(p)\,T_p\circ\iota$ for $p\nmid DM$. Added here: (i) $\iota$ sends a generalised eigenform for $(T_p)_{p\nmid DM}$ with system
$(a_p)$ to one with system $(\chi_S(p)a_p)$, hence maps the sum of the generalised eigenspaces of systems different from that of $g$ (the
$\T$-stable complement $g^\perp$) into the sum of those different from $\chi_S\cdot g$; (ii) on newforms, $\iota(g)=(g^{\chi_S})^{(S)}$ (C4), so $\iota(g)=g^{\chi_S}$ iff $a_q(g^{\chi_S})=0$
for all $q\in S$, and $\iota$ does not distinguish $g$ from its $S$-depletion: $\iota(g)=\iota(g^{(S)})$; (iii) Galois meaning: $\rho\mapsto\rho\otimes\chi_S$, so $\ad$ and the true
local adjoint factors are unchanged (3.7). Paper: Theorem thm:twist (the map $\iota$ and "$\iota$ maps $g^\perp$ into $f^\perp$"), Theorem thm:quant (proof,
"$\iota(g^S)=f$", "which kills the coefficients at multiples of $D$").

**10.2 `prop:modgalrep:twist-levels`** (proposition; P given 3.8 and Lemma lem:twist(ii)). Let $E/\Q$ have conductor $N$, $S$ a set of odd primes $q$
with $q^2\mid N$, $E_S=E\otimes\chi_S$ of conductor $N_S$, $f=f_E$, $g=f_{E_S}$. (i) If $E$ has type $\mathrm I_n^*$ at every $q\in S$: $N_S=N/D$; type $\mathrm I_0^*$ at every
$q\in S$: $N_S=N/D^2$; types $\mathrm{II},\mathrm{III},\mathrm{IV}$ or a dual at every $q\in S$ with $q\ge5$: $N_S=N$ (3.8 rows (RSt), (RPS), last row; Chapter 10, 8.2). In each
case $\operatorname{lcm}(N_S,D^2)\mid N$, the hypothesis of Theorem thm:twist; in the third case also $\operatorname{lcm}(N,D^2)\mid N_S$. (ii) $\iota(g)=f$ exactly, for all $n$
($a_n(f)=\chi_S(n)a_n(g)$ for $(n,D)=1$ by 2.7, and $a_{q^k}(f)=0$ for $q\in S$ by 3.5). (iii) For $q\in S$ the local type of $g$ at $q$ is (St) in the
$\mathrm I_n^*$ case and (U) in the $\mathrm I_0^*$ case, so $\delta_q(g)=1$, resp. $2$, and $N_S^{S}=N_S\prod_{q\in S}q^{\delta_q(g)}=N$: **the $S$-depleted form $g^{(S)}$ has
level exactly $N$**, and $\iota(g^{(S)})=f$. Paper: Theorem thm:twist and the sentence after its proof ("The hypotheses hold when (a) ... (b) ...
(c) ..."), Theorem thm:quant (first paragraph of the proof: "$N_S^\Sigma=N$: the $S$-depleted form $g^S$ lives at level $N$").

**10.3 `thm:modgalrep:twist-monotonicity`** (theorem; R here, proved in full in Chapter 20). The paper's Theorem thm:twist: with
$S$, $D$, $\chi_S$, $E_S$, $N_S$ as in 10.2 and $q^2\mid N$ for $q\in S$, if $\operatorname{lcm}(N_S,D^2)\mid N$ then $r_{E_S}\mid r_E$; if moreover $\operatorname{lcm}(N,D^2)\mid N_S$ then $r_{E_S}=r_E$.
Proof idea in two lines (Chapter 20 writes it out): $\iota$ carries a congruence $g\equiv h\pmod r$ with $h\in g^\perp$ integral to $f\equiv\iota(h)\pmod r$ with
$\iota(h)\in f^\perp$ integral (10.1, 10.2), and 8.2. **Data remark (important_notes.md point 16):** the paper's sentence after the proof ("equality in
every pair of case (c) and strict inequality only in case (b)") is contradicted by its own Theorem thm:quant in case (a): $v_3(\deg\varphi)$ is $2$
versus $1$ for 539c1 versus 77c1, $2$ versus $1$ for 980i1 versus 140b1, $1$ versus $0$ for 121d1 versus 11a1 (checked from `degphi`), the difference
being $e_3(E,q)=v_3(q^2-1)=1$ each time. The book prints the corrected sentence: strict inequality occurs in cases (a) and (b), by the Euler
term of Theorem thm:quant. Paper: Theorem thm:twist and the data sentence after it.

**10.4 `thm:modgalrep:quant`** (theorem; R here, proved in full in Chapter 20; the level-raising reading P). The paper's Theorem thm:quant:
for $\ell$ odd, $\ell\nmid2N$, $E[\ell]$ irreducible, $S$ the set of primes $q\ge5$ of type $\mathrm I_0^*$ or $\mathrm I_n^*$, $E_S=E\otimes\chi_S$:
$v_\ell(\deg\varphi_E)\ge v_\ell(r_{E_S})+\sum_{q\in S}e_\ell(E,q)\ge\sum_{q\in S}e_\ell(E,q)$. **Reading as level raising (the remark after Theorem thm:quant, (1)):** Theorem thm:qual
lowers the level of $\bar\rho\otimes\chi$ and twists back; Theorem thm:quant goes the other way: it raises the level of $g=f_{E_S}$ from $N_S$ to
$N_S^S=N$ by depleting at $S$ (10.2(iii)), and by Theorem thm:dfg14 (7.3) the congruence ideal grows by $\prod_{q\in S}L_q^{\nv}(A_g,1)^{-1}$, which is $\prod(1-q^{-2})$
over the $\mathrm I_n^*$ primes and $\prod\frac{q-1}q\cdot\frac{(q+1)^2-a_q(E')^2}{q^2}$ over the $\mathrm I_0^*$ primes (7.2), i.e. the omitted Euler factors of $f$ (3.7);
then $\iota$ transports the congruences to $f$ (10.1). Examples (checked): 539d1 ($\mathrm I_0^*$ at $7$, twist 11a, $\ell=3$): $e_3(E,7)=v_3(6)+v_3(64-4)=2$, $v_3(r_{11a})=0$,
$\deg\varphi_{539d1}=72$, $v_3=2$: equality; 539c1 ($\mathrm I_3^*$ at $7$, twist 77c1): $e_3=v_3(48)=1$, $v_3(r_{77c})=v_3(6)=1$, $v_3(288)=2$: equality; 121d1 ($\mathrm I_1^*$ at
$11$): $e_3=v_3(120)=1$, $v_3(r_{11a})=0$, $v_3(24)=1$. Remarks (the paper's remark after the theorem, with the book's corrections): (2) under the
hypothesis of Theorem thm:main the first inequality is an equality when multiplicity one holds at level $N$; by important_notes.md point 39
(Chapter 14) Lemma lem:hecke is an equality for every optimal curve, which removes the freeness hypothesis from Step 4 and partly answers
point 24; (3) for the potentially good types $\mathrm{II}$, $\mathrm{III}$, $\mathrm{IV}$ and duals, $N_S=N$ (10.2(i)), $f$ is its own depletion, Theorem thm:dfg14 gives no
factor, and the omitted factor is reached only through Theorem thm:dfg37 (Chapter 20). The abstract's word "elementary" applies only to
Step 1 (important_notes.md point 24). Paper: Theorem thm:quant, the remark after it, Section 1.5 ("The quantitative version of case (c),
and of the type $\mathrm I_0^*$"), the abstract.

### Section 11. The literature on congruence ideals and Tamagawa exponents; Taylor-Wiles in one page

**11.1 `def:modgalrep:tamagawa-exponent`** (definition and proposition; P from Chapter 11, 3.3). For a prime $q\ne\ell$, the **Tamagawa
exponent** $t_q=t_q(\rho_{f,\lambda})$ is the largest $t\ge0$ such that $\rho_{f,\lambda}\bmod\lambda^t$ is unramified at $q$ (Kim-Ota, Definition 2.12, as cited by the paper:
verify). For $f=f_E$ and $q$ multiplicative, $t_q=v_\ell(n_q)=t_\ell(E,q)$, split or not (Lemma lem:tamagawa-exp; Chapter 11, 3.3(i)). Paper: Section 1.5,
Remark rem:ko(2), Definition def:terms.

**11.2 `thm:modgalrep:ribet-takahashi`** (theorem; R). (Ribet-Takahashi; Takahashi.) For $E$ optimal of conductor $N=N^+N^-$ with $N^-$ a
product of an even number of distinct primes, the degree of the modular parametrisation by $X_0(N)$ and that of the parametrisation by
the Shimura curve of discriminant $N^-$ have ratio $\prod_{q\mid N^-}n_q$ up to primes $\ell$ at which $E[\ell]$ is reducible (the paper's summary; the writer
quotes the exact form, with its hypotheses and the precise local factor, from the sources), and Pasten controls the error term. Reference: RibetTakahashi97, Takahashi01, Pasten; Chapter 14 (where PLAN.md places the full statement).
Paper: Section 1.5 (history).

**11.3 `thm:modgalrep:pollack-weston`** (theorem; R). Pollack and Weston conjectured that moving a prime $q$ into the "new" part of the
level changes the congruence ideal by $\lambda^{t_q}$, and proved it for weight $2$ and square-free level when $\bar\rho$ is ramified at at least two
primes (the paper's summary; verify the hypotheses against PollackWeston11 before printing). Paper: Section 1.5.

**11.4 `thm:modgalrep:kim-ota`** (theorem; R, with the consequence P). (Kim-Ota, Theorem 1.1, as cited.) Let $N=N^+N^-$ with $N^-$
square-free, $\ell\ge5$, $\ell\nmid N$, $\ell\notin S_f$, and $\bar\rho$ ramified at every $q\mid N^-$ with $q\equiv\pm1\pmod\ell$. Then
$\ord_\lambda\eta_f(N)=\ord_\lambda\eta_f(N^+,N^-)+\sum_{q\mid N^-}t_f(q)$, where $\eta_f(N)$ is the congruence ideal of $f$ in the full Hecke algebra of level $N$ and $\eta_f(N^+,N^-)$ the
congruence ideal in the $N^-$-new quotient. Consequence (P): $\eta_f(N^+,N^-)$ is integral and $\ord_\lambda\eta_f(N)=v_\ell(r_E)$ (8.2(iii)), so
$v_\ell(r_E)\ge\sum_{q\mid N^-}t_\ell(E,q)$; Theorem thm:main contains this inequality for every multiplicative prime, including $q\equiv\pm1\pmod\ell$ and $\ell=3$, but not the
equality. Paper: Section 1.5, Remark rem:ko(2) (Remark rem:ko(1) is Chapter 18's).

**11.5 `rem:modgalrep:taylor-wiles`** (remark; S, one page). Taylor-Wiles and $R=\T$ in outline: the universal deformation ring $R_\Sigma$ of $\bar\rho$
(minimally ramified outside $\Sigma$, unrestricted at $\Sigma$, flat or Fontaine-Laffaille at $\ell$), the Hecke algebra $\T_\Sigma=\T(N^\Sigma)_{\mathfrak m}$, the surjection
$R_\Sigma\to\T_\Sigma$, the theorem that it is an isomorphism of complete intersections (Wiles95, TaylorWiles; Diamond's refinement), the
identification of the dual of the tangent space with the Selmer group $H^1_\Sigma(\Q,W)$, and the numerical criterion (length of the Selmer
group equals the valuation of the congruence ideal). What DFG04 Theorem 3.7 needs and why: $\ell\notin S_f$, i.e. $\ell\nmid2N$ and $\bar\rho|_{\Gal(\Qbar/\Q(\sqrt{\ell^*}))}$
absolutely irreducible (the Taylor-Wiles hypothesis, used to find auxiliary primes); for $\ell\ge5$, $\ell\nmid N$ and $E[\ell]$ irreducible it is automatic
(important_notes.md point 47; Chapter 11, 8.2), so in the range of Theorem thm:main the hypothesis bites only for $\ell=3$ and image 3Ns; and
$\Sigma\not\ni\ell$ with $M_{f,\lambda}$ minimally ramified outside $\Sigma$. Details: Chapter 20 (`\Cref{ch:congruence}`); DDT Chapters 2 to 5. Paper: Theorem thm:dfg37,
Theorem thm:main hypothesis, Section 1.5 ("by level lowering and twisting rather than by the Taylor-Wiles method").

## 3. Section plan with target line counts

Lines of LaTeX, card excluded (PLAN.md 7.3: up to 2,800 for this chapter). Items per section: 2, 7, 8, 2, 3, 7, 5, 4, 5, 4, 5 (52 items).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2, stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1.1 ($V$, $T$, $\delta_p$); Section 1.5 (history, thm:qual, Kim-Ota); Section 3 (lem:crit, lem:old, optimal-level paragraph, cases (a), (b), (c), the Example, the remark on $\ell\mid N$); Section 4.1 ($M^\Sigma$, $f^\Sigma$); thm:dfg14 and the paragraph after it; Section 4.2 ($M_{f,\lambda}$ versus $T_\ell E$); lem:euler (local components); lem:twist(iii); thm:twist, thm:quant and the remark after it; rem:ko(2); thm:dfg37 (hypothesis) | 50 |
| 1 | Conventions and recollections | 1.1 (with the twist dictionary C4 displayed and its two examples), 1.2; `convention` environments C1 to C6 | 100 |
| 2 | The Galois representation of a newform | 2.1 to 2.7; Eichler-Shimura sketch; the irreducibility sketch; the comparison with $T_\ell E$ and $M_{f,\lambda}$ with the saturation proof; `paperlink` for Section 4.2 (points 26, 40) and for lem:old (point 10) | 300 |
| 3 | Local-global compatibility and local components | 3.1 (one-page recall of Chapter 7), 3.2 to 3.8; tables 3.5, 3.6, 3.8 (`booktabs`); the proof of 3.5 in full; `paperlink` for lem:euler ("local components"), lem:twist(iii) (Atkin-Li as a corollary of 3.8), Section 1.1 ($\delta_p$) | 380 |
| 4 | The representation at $\ell$ | 4.1, 4.2; `paperlink` for lem:old ($p=\ell$) and the optimal-level paragraph ("good") | 120 |
| 5 | Serre's conjecture | 5.1 to 5.3; the proof of $N(\bar\rho_f)\mid N$ | 150 |
| 6 | Lowering the level | 6.1 to 6.7; the trivial-nebentypus proof in full; the examples table (121c1, 77c1, 52a1, 121a1 via 121c2, 140b1, 11a1 mod 5) | 270 |
| 7 | Raising the level | 7.1 to 7.5; necessity proved; the factor identity; the level-raising example table for 11a mod 3 and 20a mod 5 | 200 |
| 8 | Congruences between eigenforms | 8.1 to 8.4; full proofs of lem:crit and lem:old with the $U_p$ table; the two worked oldform examples (77c1 with $\Z[\sqrt{-6}]$, 52a1) | 380 |
| 9 | Proof of Theorem thm:qual | 9.1 to 9.5; the proof in numbered steps per case; `paperlink` for points 20, 21, 43, 46, N1, N2; the Example table; 99A1 | 320 |
| 10 | Twisting and levels in thm:twist and thm:quant | 10.1 to 10.4; `paperlink` for the data sentence after thm:twist (point 16), the remark after thm:quant (points 24, 39) | 180 |
| 11 | Literature; Taylor-Wiles in one page | 11.1 to 11.5 | 130 |
| 12 | Exercises | the 18 exercises of Part 4.2 | 150 |
| 13 | Notes and references | which numbers are cited and which only by section; the new bib entries | 50 |
| | **total** | | **2,780** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| $\rho_{f,\lambda}\colon G_\Q\to\GL_2(\mathcal O_\lambda)$ for a newform of weight $2$; Eichler-Shimura construction via $T_\ell A_f$ | 2.1, 2.4 |
| Deligne for higher weight (statement) | 2.3 |
| unramified outside $N\ell$, $\tr\rho(\Frob_p)=a_p$, $\det=\chi_\ell$, odd, irreducible | 2.1, 2.2 |
| residual representation and semisimplification | 2.4, 2.5 |
| comparison with $\rho_{E,\ell}$; $T_\ell E$ and $M_{f,\lambda}$ homothetic (to the dual) when $\bar\rho$ irreducible; Ribet's lemma on lattices | 2.6 (with Chapter 4, 10.3) |
| local-global compatibility (Carayol; Langlands-Deligne); $\rho_f|_{G_{\Q_p}}$ corresponds to $\pi_p$ under local Langlands | 3.2, 3.3, 3.4 |
| local components of a weight-two newform with trivial character: unramified principal series; unramified twist of Steinberg (DDT 3.1(e)); for $p^2\mid N$ ramified twist of Steinberg, ramified principal series, supercuspidal | 3.5, 3.6 |
| $a_p(f)=0$ and $V^{I_p}=0$ when $p^2\mid N$; $\delta_p=2,1,0$ | 3.5, 3.7 |
| the twist of a ramified twist of Steinberg has $p$ exactly once in its level | 3.8 (row (RSt)) |
| the conductor of $\rho_f$ equals $N$ (Carayol) | 3.4(ii) |
| the Weil-Deligne representation, local $L$- and $\epsilon$-factors (recalled from Chapter 7) | 3.1, 3.4(iii) |
| the non-split extension at a multiplicative prime has a unique stable line (Lemma lem:old) | 3.5 (St), 8.3 case $p\,\|\,N$ ramified |
| the local representation at $\ell\nmid N$: crystalline, finite flat, Fontaine-Laffaille | 4.1 |
| Deligne-Fontaine description of $\bar\rho|_{D_\ell}$; $a_\ell\bmod\lambda$ from it (Edixhoven Section 2) | 4.2 |
| Serre conductor and Serre weight; weight $2$ for $\bar\rho_{E,\ell}$ with good reduction at $\ell$ | 5.1, 5.2, 4.1(iii) |
| Serre's conjecture, strong form; Khare-Wintenberger; only the optimal-level direction used | 5.3, 6.4 |
| the optimal level theorem of Ribet, Carayol, Diamond (DDT 3.15), hypotheses at $\ell=3$ | 6.4 |
| specialisation to $\bar\rho_{E',\ell}$, $\ell\nmid N(E')$: level $N(\bar\rho)$, trivial nebentypus (the paper's argument) | 6.5 |
| Ribet's level-lowering theorem ($q\,\|\,N$, $\bar\rho$ unramified at $q$), Shimura curves, Ihara/Mazur principle | 6.2, 6.1, 7.4, 6.7 |
| Mazur's principle; Carayol's lemma | 6.1, 6.3 |
| level raising (Ribet): $a_q^2\equiv(q+1)^2\pmod\lambda$ | 7.1, 7.5 |
| the level-raising factor $(1-\frac\alpha{\beta q})(1-\frac1q)(1-\frac\beta{\alpha q})=\frac{q-1}q\cdot\frac{(q+1)^2-a_q^2}{q^2}$, the form used in the paper | 7.2, 7.3 |
| congruences between newforms: the congruence criterion (Lemma lem:crit, proved in full; cross-references Chapters 14, 20) | 8.1, 8.2 |
| the oldform lemma (Lemma lem:old in full, prime by prime: $p\nmid\ell N$, $p=\ell$, $p^2\mid N$, $p\,\|\,N$ unramified, $p\,\|\,N$ ramified) | 8.3, 8.4 |
| proof of Theorem thm:qual, cases (a), (b), (c), as a worked application | 9.1, 9.2, 9.3 |
| the examples 121a1, 539c1, 980i1 with the specific congruences | 9.4 (with 2.7, 3.8, 6.6) |
| Ribet-Takahashi, Pollack-Weston, Kim-Ota, Tamagawa exponent $t_q$ (statements with hypotheses) | 11.1 to 11.4 |
| Taylor-Wiles and $R=\T$ in one page; what DFG04 Theorem 3.7 needs | 11.5 |
| Section 6 row: Steinberg representation, unramified twists, ramified twist has conductor exponent $2$ | 3.5, 3.8 (with Chapter 7) |
| Section 6 row: level lowering (DDT 3.15), Serre conductor, Serre's conjecture | 5.1 to 5.3, 6.1 to 6.6 |
| Section 6 row: level raising (Ribet), Wiles's level-raising factor | 7.1 to 7.3 |
| Section 6 row: Deligne-Fontaine description, $a_\ell\bmod\ell$ | 4.2 |
| Section 6 row: DDT Theorem 3.1(e), local structure at multiplicative primes | 3.5 (St) |
| Section 6 row: Ribet-Takahashi, Pollack-Weston, Kim-Ota, Tamagawa exponent | 11.1 to 11.4 |
| Section 6 row: the worked examples 11a1, 20a1, 121a1, 539c1, 980i1, 99A1 | 6.6, 7.5, 8.1, 9.4, 10.4 |
| hook: Section 3, Lemma lem:crit | 8.2 |
| hook: Section 3, Lemma lem:old | 8.3, 8.4 |
| hook: Section 3, the optimal-level theorem paragraph | 4.1, 5.1, 5.2, 6.4, 6.5 |
| hook: Section 3, cases (a), (b), (c) | 9.1, 9.2 |
| hook: Section 3, the Example (121a1, 539c1, 980i1) | 9.4 |
| hook: Section 3, the remark on $\ell\mid N$ and 99A1 | 9.5, 8.1 |
| hook: Section 1.5 (history, Theorem thm:qual, Remark rem:ko) | 9.1, 11.1 to 11.4 |
| hook: Section 4.2 ($M_{f,\lambda}$ versus $T_\ell E$) | 2.6 |
| hook: Lemma lem:euler (local components: Steinberg and its twists) | 3.5, 3.6 |
| hook: Lemma lem:twist(iii) (Atkin-Li) | 3.8(a), 2.7 |
| hook: Theorem thm:twist (twist map, eigenforms, levels) | 10.1, 10.2, 10.3 |
| hook: Theorem thm:quant (twist map, eigenforms, levels) | 10.1, 10.2, 10.4 |
| hook: Theorem thm:dfg14 (the level-raising factor) | 7.2, 7.3 |
| hook: the remark after Theorem thm:quant | 10.4, 9.3 |
| also: Section 1.1 ($\delta_p$, naive versus true factor at $p$) | 3.5, 3.7 |
| also: Section 4.1 ($M^\Sigma$, $f^\Sigma$ as level raising) | 7.3, 10.2(iii) |
| also: Theorem thm:dfg37 (hypothesis $\ell\notin S_f$) | 11.5 |

### 4.2 Exercises (Section 12 of the chapter), graded from easy to harder

1. Let $\ell$ be odd. Show that $\bar\rho_{f,\lambda}$ is irreducible over $k_\lambda$ iff it is absolutely irreducible. Give the step of Lemma lem:old that needs
   this, and say what goes wrong for $\ell=2$.
2. Show $(g\otimes\chi)\otimes\chi=g^{(r)}$ for $\chi$ quadratic of conductor $r$ and $g\otimes\chi=(g^\chi)^{(r)}$. Check the paper's claim (Example of Section 3) that
   $f_{11a}\otimes\chi_{-11}$ is the form of 121d, and show that $f_{539c}\otimes\chi_{-7}$ is **not** the form of 77c.
3. (B8.) Twist 11a1, 11a3, 121a1, 20a1 by the appropriate $-q$, compute minimal models and Kodaira types, and identify the curves in
   Cremona's tables (121d2, 121d1, 121c2, 980g2). Why does every quantity at $\ell=3$ in the paper depend only on the class?
4. Prove 3.5: from $a(V)=1$ and $\det V=\chi_\ell$ deduce $V\simeq\mathrm{sp}(2)\otimes\mu$ with $\mu$ unramified, $\mu^2=1$; from $a(V)\ge2$ deduce $V^{I_p}=0$ and $a_p=0$. Compare
   with Atkin-Lehner's Theorem 3.
5. Fill in table 3.8 and check it on 11a1 at $11$ and $7$, 121a1 at $11$, 539c1 and 539d1 at $7$, 20a1 at $7$ (levels of the twists). Deduce the
   paper's Lemma lem:twist(iii).
6. Prove $N(\bar\rho_{f,\lambda})\mid N$ (5.2). Compute $N(\bar\rho)$ for 52a1 at $\ell=3$ and for 140b1 at $\ell=5$, and explain why the newform attached to
   $\bar\rho_{140b1,5}$ has level $20$, not $4$.
7. Check the paper's claim (optimal-level paragraph) that the nebentypus is trivial: write out the argument for $\bar\rho_{E',\ell}$ with $\ell\nmid N'$.
   Where is $\ell\nmid N'$ used, and what replaces it for 140b1?
8. (Level raising.) Prove the necessity in 7.1. For $f_{11a}$ and $\ell=3$ list the $q<40$, $q\ne3,11$, with $3\mid(q+1)^2-a_q^2$; for $q=7$ identify the congruent
   newform at level $77$; for $q=13$ show the congruent newform at level $143$ cannot be rational.
9. Prove the identity of 7.2 and compute the $3$-adic valuation of the level-raising factor of $f_{11a}$ at $q=7$. Relate it to $e_3(539\mathrm d1,7)=2$
   and to $\deg\varphi_{539d1}=72$.
10. Check the paper's claim (Lemma lem:crit) in the toy algebra $\T=\{(a,b)\in\Z^2:a\equiv b\pmod r\}$ acting on $\Z^2$ with the standard pairing:
    compute $I$, $J$, $\T/(I+J)$ and the congruence modulus.
11. Check the paper's remark after the Example: compute (by machine) the congruence number of 99a1 as the index of $\Z f\oplus L$ in
    $S_2(\Gamma_0(99);\Z)$ and compare with $\deg\varphi=4$. Which hypothesis of Agashe-Ribet-Stein fails at $3$?
12. Check the paper's claim in Lemma lem:old, case $p\,\|\,N$ unramified, on $f=f_{77c}$, $h=f_{11a}$, $\ell=3$: compute $U_7$ on $\langle h,h(7z)\rangle$, its
    eigenvalues, the prime above $3$ in $\Z[\sqrt{-6}]$, and the congruence $h-\beta h(7z)\equiv f_{77c}$ up to the Sturm bound.
13. Check the paper's claim in case (a) on 121c1 and, at $q=2$, on 52a1: compute $N(\bar\rho_{E,3})$, the lowered newform, the eigenform $g$ of Lemma
    lem:old, and verify $3\mid\deg\varphi$. Explain why case (a) holds at $q=2$ but case (b) is not claimed there.
14. Check the paper's claim in case (b) that $h\ne f$: show that "$g=h\otimes\chi$" is false in general and give the strong multiplicity one
    argument (important_notes.md point 20).
15. Check the paper's sentence in case (c) "$f'=f\otimes\chi$ is a newform of weight $2$ on $\Gamma_0(N/q)$" on 539c1, and correct it.
16. Carry out the construction of Theorem thm:qual for a curve of type $\mathrm I_0^*$ (539d1, $\ell=3$) and show that it returns $h=f$. How does
    Theorem thm:quant nevertheless give $9\mid\deg\varphi_{539d1}$?
17. Check the paper's data sentence after Theorem thm:twist (important_notes.md point 16) on the pairs 539c1/77c1, 980i1/140b1,
    121d1/11a1 at $\ell=3$, and predict the differences from Theorem thm:quant.
18. Derive $v_\ell(r_E)\ge\sum_{q\mid N^-}t_\ell(E,q)$ from the formula of Kim and Ota, and say which of its hypotheses Theorem thm:main removes and
    which it needs.

## 5. Dependencies and forward pointers

Results from earlier chapters used here (by chapter label only, `\Cref{ch:...}`; item numbers refer to their outlines):
* Chapter 2 (`ch:rings`): $\chi_{-3}$, $\chi_{-4}$, $q^*$, Kronecker symbols; the identity $(1-\frac\alpha{\beta q})(1-\frac\beta{\alpha q})=\frac{(q+1)^2-a^2}{q^2}$ (11.4).
* Chapter 3 (`ch:modules`): saturation (5.5), stacked bases and index (5.6), dualising inclusions (5.7), the congruence module of a decomposition
  (5.8), algebra-module duality (9.6), Artinian algebras and idempotents (10.1 to 10.4), generalised eigenspaces (10.5, 10.6), non-semisimple
  operators and the $U_p$ model (10.7), common eigenvectors (10.8), congruence ideals (11.1).
* Chapter 4 (`ch:reps`): non-split extensions and the unique stable line (3.6), Brauer-Nesbitt (5.2, 5.3), fixed spaces of groups of order
  prime to $\ell$ commute with reduction (3.2(ii)), lattices and homothety (10.1 to 10.3), adjoint invariance (7.7).
* Chapter 5 (`ch:galois`): galois:continuous-reps, galois:chebotarev-brauer-nesbitt, galois:congruent-ap (whose newform black box 2.1 discharges).
* Chapter 6 (`ch:ant`): coefficient fields, $\mathcal O_\lambda$, primes above $\ell$ (7.1 to 7.4); Frobenius elements; $\Z[\sqrt{-6}]$ for 8.4(a).
* Chapter 7 (`ch:local`): Weil group and Weil-Deligne representations (7.1 to 7.5), invariants and $L$-factors (8.1, 8.2), Artin, Swan
  conductors (8.3, 8.4), $\epsilon$-factors (8.5), the shapes (9.1 to 9.4), local class field theory for characters (6.5), quadratic characters of
  $\Q_q$ (6.3), wild inertia (5.7).
* Chapter 8 (`ch:curves`): Jacobians, Tate modules and $H^1$ as duals (11.7), the etale comparison and the Weil pairing (11.8), pullback and
  pushforward on $H^1$ and $H_1$.
* Chapter 9 (`ch:ellcurves`): twists and $\rho_{E^{(d)},\ell}=\rho_{E,\ell}\otimes\chi_d$ (10.3, 10.4), the dual of $T_\ell E$ (5.5), Cremona labels.
* Chapter 10 (`ch:reduction`): Lemma lem:twist (i), (ii) (8.1, 8.2), Kodaira types, conductor exponents.
* Chapter 11 (`ch:galrep`): $\rho_{E,\ell}$, irreducible iff absolutely irreducible (1.4), twists (1.3), the Tate shape and Lemma lem:tamagawa-exp
  (3.2, 3.3), potentially multiplicative reduction (3.4), inertia images by type and Lemma lem:IV (4.1, 4.3), type IV at $2$ (4.4), the mod $3$
  table (4.5), the representation at $\ell$ (5.1 to 5.4), Serre conductors of $\bar\rho_{E,\ell}$ (6.1 to 6.3), $\ell\notin S_f$ (8.2, 8.6), the optimal-level
  statement for $E$ (10.1, 10.2).
* Chapter 12 (`ch:modforms`): $S_2(\Gamma_0(N);\Z)$, integral basis (11.1, 11.2), Sturm (11.3, 11.4), the three congruences for all $n$ (11.5),
  nebentypus (6.6), Ramanujan-Petersson (6.5), Atkin-Lehner $w_N$ (12.1).
* Chapter 13 (`ch:hecke`, outlined in parallel): Hecke operators, $U_p$ on oldforms, stabilisations and depleted forms, the decomposition of
  $S_2$ into spans of $h(dz)$, strong multiplicity one, Atkin-Lehner Theorem 3, Atkin-Li, the twist map $\iota$ and its Hecke compatibility,
  the perfect pairing with $\T$, the recursion for $a_{p^k}$. **Used in 1.2, 8.2, 8.3, 10.1 as black boxes.**
* Chapter 14 (`ch:moddeg`, outlined in parallel): $J_0(N)$, $A_f$, Eichler-Shimura, modularity, the optimal curve and connected kernel, the
  modular degree and congruence number, Agashe-Ribet-Stein, multiplicity one, point 39. **Used in 2.1, 2.6, 8.1, 9.2, 10.4.**

Forward pointers (chapters that use this one):
* Chapter 16 (`ch:cohomology`): none beyond the shapes (via Chapter 11).
* Chapter 17 (`ch:galcoh`): the local types 3.5 for unramified cohomology at $p\mid N$.
* Chapter 18 (`ch:blochkato`): crystalline at $\ell$ (4.1); $A=\ad T$ with $T=T_\ell E$ or $M_{f,\lambda}$ (2.6(iv)); $\delta_p$ (3.5).
* Chapter 19 (`ch:lfunctions`): local types and the Kodaira dictionary (3.5, 3.6), $L_p(f,s)=L(V_p,s-1)$ (3.4(iii)), the naive factor and $\delta_p$ (3.7),
  the level-raising factor (7.2).
* Chapter 20 (`ch:congruence`): Lemma lem:crit (8.2, restated there), the twist map and levels (10.1, 10.2), the level-raising reading of
  Theorem thm:quant (10.4), Theorem thm:dfg14 preview (7.3), Ihara's lemma (7.4), $\ell\notin S_f$ and Taylor-Wiles (11.5), $M_{f,\lambda}$ (2.6).
* Chapter 21 (`ch:paper`): 2.5, 2.6, 3.8, 6.5, 8.2, 8.3, 9.1 to 9.5, 10.3, 10.4, 11.4 (the tour may shorten A3.2 to A3.7 and A4.14 by pointing here; it
  must adopt the corrections of Part 7.2).
* Chapter 22 (`ch:computation`): the verification scripts of Part 6.6 (congruences up to the Sturm bound, `elltwist` and identification,
  `mfeigenbasis` and reduction modulo $\lambda$, the congruence number of 99a1).

## 6. Notes for the writer

### 6.1 Conventions to typeset (Section 1, as `convention` environments)
* C1 to C6 of Part 1.3. The twist dictionary C4 is the single most important convention: write $f\otimes\chi$ only for the naive twist and $f^\chi$
  for the newform twist, and display $f\otimes\chi=(f^\chi)^{(r)}$ once. Every place the paper writes $f\otimes\chi$ or $g\otimes\chi$ gets a `paperlink` saying which is meant.
* Frobenius: as Chapters 7 and 11; $\rho_{f,\lambda}$ normalised by the arithmetic Frobenius trace $a_p$; the cohomological lattice $M_{f,\lambda}$ is a lattice in
  the dual. $L_p(f,s)=L(V_\lambda(f)|_{G_{\Q_p}},s-1)$ with the geometric Frobenius (3.4(iii)); check the formula on 11a1 at $11$ ($a_{11}=1$) and at $2$.
* Local Langlands normalisation (3.2): fix one (the book's is the arithmetic one with the $|\det|^{-1/2}$ twist), state it once, and phrase every
  proof on the Galois side; the automorphic names are labels.
* Macros: `\ad`, `\Sym`, `\nv`, `\Frob`, `\T`, `\degphi`; there is no macro for $\mathcal O$; write `\mathcal{O}`. Labels `...:modgalrep:...`; the paper's results proved
  here get the paper's name in the optional argument (`\begin{lemma}[the paper's Lemma lem:crit]\label{lem:modgalrep:crit}`).

### 6.2 Pitfalls
* **Naive versus newform twist** (C4): $f\otimes\chi$ is a newform iff $a_q(f^\chi)=0$ at every $q\mid r$. In case (b) of Theorem thm:qual it is ($q^2\mid N$); in case (c)
  the paper's "$f'=f\otimes\chi$ on $\Gamma_0(N/q)$" is false as written (N1) and "$g=h\otimes\chi$" in (b), (c) is false as written (point 20). The conclusions
  survive by strong multiplicity one; write the arguments as in 9.2.
* **"For all $n$" versus "for almost all $p$".** Lemma lem:crit needs congruence of the full eigencharacters ($U_p$ included); a congruence of
  $a_p$ for $p\nmid\ell N$ is only $\bar\rho_h\simeq\bar\rho$. Lemma lem:old bridges the gap by choosing $U_p$-eigenvalues; never shortcut it.
* **Atkin-Li covers only $q^2\nmid M$.** Case (b) twists a form with $q^2\mid N$ at the level of $f$; there the equality $f_{E'}=f\otimes\chi$ holds because both
  have $a_q=0$ (3.5), not by Atkin-Li. Use 3.8 for all levels of twists.
* **$\ell\mid N$ examples.** 980i1 and 140b1 have $5\mid N$: the optimal-level theorem gives level $N(\bar\rho)\cdot5$ there; Lemma lem:old at $p=\ell$ and
  Agashe-Ribet-Stein are unavailable. Present 980i1 as an illustration only (point 21).
* **Residual irreducibility and absolute irreducibility.** For $\bar\rho_{f,\lambda}$ ($\ell$ odd) they agree (2.4(ii)); for restrictions to $G_{\Q(\sqrt{-3})}$ they do not
  (Chapter 11). The DDT 3.15 hypothesis at $\ell=3$ is the latter.
* **Dual versus Tate module.** $M_{f,\lambda}\subset H^1$ is a lattice in $V_\ell E^\vee\simeq V_\ell E(-1)$, not in $V_\ell E$; only $\ad$ is insensitive (points 26, 40).
* **Local types at $p=2,3$.** Table 3.6 is for $q\ge5$; at $q=2$ the dictionary to Kodaira types fails (Chapter 11, 4.6; Remark rem:wild), except types
  $\mathrm{IV}$, $\mathrm{IV}^*$ (cyclic inertia of order $3$, Chapter 11, 4.4). Do not extend case (b) of Theorem thm:qual to $q=2$.
* **Level raising hypotheses.** State Ribet's theorem with the hypotheses of the source (7.1 marks them "verify"); the necessity direction is
  elementary and is what Lemma lem:old uses.
* **Theorem numbers.** Sure only where the paper cites them (DDT Theorems 3.1(e) and 3.15, Ribet83 Theorem 2.2, AU96 Lemma 2.1, AtkinLehner70
  Theorem 3, AtkinLi78 Theorem 3.1, ARS12 Theorem 2.2, Edixhoven92 Section 2, DFG04 Proposition 1.4(c), KimOta Theorem 1.1 and Definition 2.12);
  everything marked "(verify)" must be checked or replaced by a section reference (Shimura71 7.14 and 3.64, Ribet90 Theorem 1.1 and its
  hypotheses, Carayol86 Theoreme A, Ribet84, DiamondTaylor94, Edixhoven92 Theorems 2.5, 2.6, the Carayol lemma number in DDT).
* **Congruence number versus modular degree.** Lemma lem:crit computes $r$; the passage to $\deg\varphi$ is Agashe-Ribet-Stein and needs $\ell^2\nmid N$ (99a1).
* **Optimality.** $r$ depends only on $f$; $\deg\varphi$ is that of the optimal curve; when $E[\ell]$ is irreducible $v_\ell(\deg\varphi)$ does not depend on which curve
  of the class is optimal (important_notes.md point 27; Chapter 11, 1.3(iii)).

### 6.3 What to leave to Chapters 7, 11, 13, 14 and 20
* **Chapter 7:** all Weil-Deligne computations, $L$- and $\epsilon$-factors, conductors of $\mathrm{sp}(2)\otimes\mu$, the shapes table. Here: a one-page recall (3.1) and the
  automorphic side.
* **Chapter 11:** every fact about $\rho_{E,\ell}$ (Tate shape, Lemma lem:tamagawa-exp, inertia images, Lemma lem:IV including $q=2$, Serre conductors of
  $\bar\rho_{E,\ell}$ and their examples, Proposition prop:ns, Lemma lem:h0, $\ell\notin S_f$). Here: the general newform statements and the paper's proofs that
  combine them (lem:old, thm:qual).
* **Chapter 13:** the $q$-expansion side of Hecke operators, $U_p$ on oldforms (the formulas and eigenvectors, which 8.3 tabulates by citation),
  stabilisations and depletions, Atkin-Lehner Theorem 3, Atkin-Li's statement, the twist map $\iota$ and its Hecke compatibility, the perfect
  pairing with $\T$. Here: the Galois reading (3.5, 3.8, 10.1) and the uses.
* **Chapter 14:** $J_0(N)$, $A_f$, Eichler-Shimura, modularity, modular degree, congruence number, Agashe-Ribet-Stein, multiplicity one, point 39.
  Here: cited; $r(99\mathrm a1)=12$ recomputed only as data.
* **Chapter 20:** congruence ideals over $\T_{\mathfrak m}$, Lemmas lem:ddt417, lem:hecke, Theorem thm:dfg14 with its proof idea, DFG04 Theorems 2.7, 3.7, Taylor-Wiles
  in detail, **the proofs of Theorems thm:twist and thm:quant**. Here: statements (10.3, 10.4), the level and twist facts, the level-raising reading.
  Lemma lem:crit is proved **here**; Chapter 20 restates it (PLAN.md).

### 6.4 How each relevant point of important_notes.md is handled
* **Point 10** (irreducible versus absolutely irreducible in Lemma lem:old): 2.4(ii), 2.5(ii), 8.3 (statement and step $p\nmid\ell N$), `paperlink`.
* **Point 16** (data sentence after Theorem thm:twist): 10.3, with the three pairs recomputed; Exercise 17.
* **Point 20** ("$g=h\otimes\chi$" in cases (b), (c)): C4, 9.2 (both cases, with the strong multiplicity one argument); Exercise 14.
* **Point 21** (980i1 outside the hypotheses): 9.4(iii), 6.5 remark ($\delta=1$), Pitfalls.
* **Point 24** ("elementary" in the abstract): 10.4 remark; with point 39 the middle term needs no freeness.
* **Point 26** ($M_{f,\lambda}$ homothetic to the dual): 2.6(iii), (iv), C2.
* **Point 40** ($M_{f,\lambda}=\phi^*H^1(E_0,\Zl)\simeq T_\ell E_0(-1)$ exactly for the optimal curve): 2.6(ii), with the saturation proof.
* **Point 43** (case (a) of Theorem thm:qual extends to $q=2$; settled): 9.1 (statement with $q=2$), 9.2 case (a) (citing Chapter 11, 4.4), the new
  worked example 52a1 (6.6, 8.4(b), 9.4) and the check on all $1{,}051$ table curves; Exercise 13.
* **Point 46** (the Example's congruences hold for all $n$ by Sturm): 9.4(i), citing Chapter 12, 11.5; the Lemma lem:old reading ($g=h$).
* **Point 47** ($\ell\notin S_f$ automatic for $\ell\ge5$, $\ell\nmid N$, $E[\ell]$ irreducible): 6.4 remark (b), 11.5.
* **B3** (Chapter 21's A4.4 and A4.6): 2.6 gives the correct statement of the $M_{f,\lambda}$ comparison that A4.6 must use; A4.4 is Chapter 20's and
  Chapter 3's matter (point 35) and is not touched here.
* **B8** (curve-level twists): 2.7 and 3.8 examples, 9.4 table and (ii), Exercise 3; all pairs recomputed (Part 6.6).
* Also used: point 15 (3.7: the naive factor is not twist-invariant), point 27 (6.2 Pitfalls), point 32 (C3), point 39 (2.6, 10.4), B1 (C2),
  point 29 (Lemma lem:twist(ii) is Chapter 10's; not repeated).

### 6.5 References and bibliography
In `refs.bib` already: `DDT`, `Ribet90`, `Ribet91`, `Ribet84`, `Carayol86`, `Carayol89`, `Diamond95`, `DiamondIm`, `Edixhoven92`, `Serre87`,
`KhareWintenberger`, `Khare`, `Deligne`, `FontaineLaffaille`, `Wiles88`, `Wiles95`, `TaylorWiles`, `Shimura71`, `AtkinLi78`, `AtkinLehner70`, `Ribet83`,
`AU96`, `ARS12`, `DFG04`, `KimOta`, `PollackWeston11`, `RibetTakahashi97`, `Takahashi01`, `Pasten`, `Mazur77`, `ColemanEdixhoven`, `Sturm87`,
`DiamondShurman`, `Berger`, `Stein`, `PARI`, `Cremona97`. To add (complete entries, checked against the sources before use; decision B14):
* to `refs.bib` (needed by more than one chapter): `Rohrlich94` (D. E. Rohrlich, "Elliptic curves and the Weil-Deligne group", in *Elliptic
  curves and related topics*, CRM Proc. Lecture Notes 4, Amer. Math. Soc., 1994, 125-157; also planned by Chapter 7), `Deligne73` (P.
  Deligne, "Les constantes des equations fonctionnelles des fonctions L", in *Modular functions of one variable II*, Lecture Notes in Math.
  349, Springer, 1973, 501-597; also planned by Chapter 7), `Livne89` (R. Livne, "On the conductors of mod $\ell$ Galois representations coming
  from modular forms", J. Number Theory 31 (1989), 133-141; also planned by Chapter 11);
* to `bib/ch15.bib` (this chapter only, so far): `Ribet77` (K. A. Ribet, "Galois representations attached to eigenforms with Nebentypus", in
  *Modular functions of one variable V*, Lecture Notes in Math. 601, Springer, 1977, 17-51), `Langlands73` (R. P. Langlands, "Modular forms
  and $\ell$-adic representations", in *Modular functions of one variable II*, Lecture Notes in Math. 349, Springer, 1973, 361-500),
  `BushnellHenniart06` (C. J. Bushnell and G. Henniart, *The local Langlands conjecture for GL(2)*, Grundlehren 335, Springer, 2006),
  `Casselman73` (W. Casselman, "On some results of Atkin and Lehner", Math. Ann. 201 (1973), 301-314), `LoefflerWeinstein12` (D. Loeffler
  and J. Weinstein, "On the computation of local components of a newform", Math. Comp. 81 (2012), 1179-1200), `DiamondTaylor94` (F. Diamond
  and R. Taylor, "Non-optimal levels of mod $\ell$ modular representations", Invent. Math. 115 (1994), 435-462). Page ranges to be checked.
  If Chapter 13 or 19 also cites any of these, move it to `refs.bib` (B14).

### 6.6 Verification log (computations done for this outline)
Scripts in the session scratchpad (`ch15/v1.py` to `v5.py`, `v2.gp`, `v3.gp`), PARI/GP 2.17 through `cypari2`; data `allcurves`, `degphi`, `galrep`
for conductors $0$ to $9{,}999$.
* **Example of Section 3, for all $n$** (point 46): $a_n(121\mathrm a1)\equiv\chi_{-11}(n)a_n(11\mathrm a1)\pmod3$, $a_n(539\mathrm c1)\equiv\chi_{-7}(n)a_n(11\mathrm a1)\pmod3$,
  $a_n(980\mathrm i1)\equiv\chi_{-7}(n)a_n(20\mathrm a1)\pmod5$ for all $n\le3000$; `mfsturm` gives $22$, $112$, $336$. Also $f_{121d}=f_{11a}\otimes\chi_{-11}$ and $f_{539d}=f_{11a}\otimes\chi_{-7}$
  exactly ($n\le2000$).
* **Newform twists (2.7, 3.8, B8):** $a_p$ equal away from $q$ for $11\mathrm a\otimes\chi_{-11}=121\mathrm d$, $11\mathrm a\otimes\chi_{-7}=539\mathrm d$, $121\mathrm a\otimes\chi_{-11}=121\mathrm c$, $539\mathrm c\otimes\chi_{-7}=77\mathrm c$,
  $980\mathrm i\otimes\chi_{-7}=140\mathrm b$ ($p<500$); curve-level: `elltwist` then `ellminimalmodel`, identified in `allcurves`: 11a1 by $-11$ is 121d2, 11a3 by $-11$
  is 121d1, 11a1 by $-7$ is 539d2, 121a1 by $-11$ is 121c2, 539c1 by $-7$ is 77c1, 980i1 by $-7$ is 140b1, 20a1 by $-7$ is 980g2, 121c1 by $-11$ is 121a2.
* **Kodaira types and Serre conductors** (formula of Chapter 11, 6.2): 11a1 ($\mathrm I_5$; $\ell=3$: $11$; $\ell=5$: $1$), 11a3 ($\ell=5$: $11$), 121a1 ($\mathrm{II}$; $121$),
  121c1 ($\mathrm{IV}$; $11$), 121c2 ($\mathrm{IV}^*$; $11$), 121d1 ($\mathrm I_1^*$), 121d2 ($\mathrm I_5^*$), 539c1 ($\mathrm I_3^*$ at $7$, $\mathrm I_2$ at $11$; $539$), 539d1 ($\mathrm I_0^*$ at $7$, $\mathrm I_1$ at
  $11$), 539d2 ($\mathrm I_0^*$, $\mathrm I_5$), 77c1 ($\mathrm I_3$, $\mathrm I_2$; $11$), 52a1 ($\mathrm{IV}^*$ at $2$, $\mathrm I_2$ at $13$; $26$), 26b1 ($\mathrm I_7$, $\mathrm I_1$; $26$), 980i1 ($\mathrm{IV}^*$, $\mathrm I_1$ at $5$,
  $\mathrm I_5^*$ at $7$; $\ell=5$: $196$), 140b1 ($\mathrm{IV}^*$, $\mathrm I_1$, $\mathrm I_5$; $4$), 20a1 ($\mathrm{IV}^*$, $\mathrm I_2$ at $5$; $4$), 980g2 ($\mathrm{IV}^*$, $\mathrm I_2$, $\mathrm I_0^*$; $196$), 726a1 ($121$).
* **Level raising (7.5):** for $f_{11a}$, $\ell=3$, $q\in\{2,5,7,13,17,19\}$, all newforms of level $11q$ (`mfinit([11q,2],0)`, `mfeigenbasis`, `mffields`), reduced
  modulo every prime above $3$ of the coefficient field, compared with $a_p(11\mathrm a1)$ for $p<200$, $p\nmid33q$: congruent forms exactly for $q=7$ (rational,
  77c) and $q=13$ (quartic field, one of two primes above $3$); none for $5$, $17$, $19$ ($2$: no newforms). For $f_{20a}$, $\ell=5$: $q=7$ yes (rational, 140b),
  $q=3$ no. $a_7(77\mathrm c1)=-1$, $a_7(140\mathrm b1)=-1$, consistent with $a_q(f)\equiv(q+1)a_q(g)$. 143a1 has $a_2=0\not\equiv-2$.
* **Congruence numbers** (index of $\Z f\oplus L$ in the saturated $q$-expansion lattice of `mfinit([N,2],1)`, with $L$ the image of $T_p-a_p$ for a $p$
  separating $f$): 99a1: $r=12$, $\deg\varphi=4$; 11a1: $1$; 121a1: $6=\deg\varphi$; 77c1: $6=\deg\varphi$; 539c1: $288=\deg\varphi$.
* **Lemma lem:old examples (8.4):** $f_{77c}\equiv f_{11a}-\beta f_{11a}(7z)$ modulo $(3,\sqrt{-6})$ for $n\le3000$ (Sturm $16$); $f_{52a}\equiv f_{26b}-f_{26b}(2z)\pmod3$ for $n\le400$
  (Sturm $14$), while $f_{26a}$ is not congruent; $f_{121c}\equiv f_{11a}-f_{11a}(11z)\pmod3$ for $n\le3000$ (Sturm $22$).
* **Case (a) at $q=2$ on the tables:** $1{,}051$ curves labelled "1" with type $\mathrm{IV}$ or $\mathrm{IV}^*$ at $2$ (PARI codes $\pm4$), $3\nmid N$, mod $3$ image surjective or 3Nn
  (no 3B, 3Cs or 3Ns label): $3\mid\deg\varphi$ for all of them (`degphi`); first examples 52a1 ($\deg3$), 76a1 ($6$), 92b1 ($6$).
* **Theorem thm:quant and point 16 data:** $\deg\varphi$: 539c1 $288$, 77c1 $6$, 980i1 $2880$, 140b1 $60$, 121d1 $24$, 11a1 $1$, 539d1 $72$; $e_3(539\mathrm d1,7)=v_3(6)+v_3(60)=2$.
* Not verified: the theorem numbers marked "(verify)"; the precise hypotheses of Ribet84 and Ribet90 Theorem 1.1 and of Pollack-Weston and
  Kim-Ota; the normalisation of local Langlands in the chosen reference; DFG04's normalisation of $M_{f,\lambda}$ (2.6(ii) assumes the paper's
  description); anything beyond conductor $10{,}000$.

## 7. Points for important_notes.md

### 7.1 New points about the paper (not among points 1 to 53 and B1 to B16; each checked as stated)

**N1. Theorem thm:qual, proof of case (c): "$f'=f\otimes\chi$ is a newform of weight $2$ on $\Gamma_0(N/q)$" is false as written.** Location: Section
sec:proof, case (c), second sentence ("By Lemma lem:twist, $E'$ has multiplicative reduction of type $\mathrm I_n$ at $q$ and conductor $N/q$, so
$f'=f\otimes\chi$ is a newform of weight $2$ on $\Gamma_0(N/q)$ with $q\,\|\,N/q$"), and its reuse at the end of the case ("$g=h\otimes\chi$ would otherwise equal
$f'$, of level $N/q\ne M$"). Problem: with the paper's own definition of $\otimes\chi$ (Lemma lem:twist(iii): $a_n(g\otimes\chi)=\chi(n)a_n(g)$), $f\otimes\chi$ has
$a_q=0$, whereas the newform $f_{E'}$ of the multiplicative curve $E'$ has $a_q(f_{E'})=\pm1$; in fact $f=f_{E'}\otimes\chi$ (Atkin-Li, as $q\,\|\,N/q$) and
$f\otimes\chi=f_{E'}^{(q)}$, the $q$-depletion of $f_{E'}$, which lives at level $N$, not $N/q$. Example: for 539c1 ($q=7$), $f_{539c}\otimes\chi_{-7}$ has $a_7=0$ while
$f_{77c}$ has $a_7=-1$. (In case (b) the analogous sentence is correct, because there $a_q(f_{E'})=0$; but the justification is not Atkin-Li, which
needs $q^2\nmid M$, and should be "both have $a_n=0$ for $q\mid n$".) Fix: in case (c) write "$f'=f_{E'}$, a newform on $\Gamma_0(N/q)$ with $q\,\|\,N/q$ and
$f=f'\otimes\chi$ (Lemma lem:twist(iii)), so that $a_p(f')=\chi(p)a_p(f)$ for $p\ne q$", and prove $h\ne f$ as in important_notes.md point 20: if $h=f$, then
$g^{(q)}=h\otimes\chi=f\otimes\chi=f'^{(q)}$, so $g=f'$ by strong multiplicity one, but their levels are $M$ and $N/q\ne M$. Effect: none on the theorem.
Confidence: high (definition check; numerical example). Importance: low (expository; companion to point 20).

**N2. The remark after the Example of Section 3: the reason given for $q=3$ in cases (a) and (b) is not the operative one.** Location:
"... so do they at $q=3$ in cases (a) and (b), where Lemma lem:IV does not apply because the ramification is wild." Problem: cases (a)
and (b) have $\ell=3$, so $q=3$ means $q=\ell$, i.e. $3\mid N$, which Theorem thm:qual excludes twice ($\ell\nmid N$ and $q\ne\ell$). At $q=\ell$ the inertia
group acts on $T_3E$ through an infinite image (it contains the cyclotomic character), so neither Kraus's semistability defect nor
the statement of Lemma lem:IV (an image of order $3$ in $\Aut T_3E$) is meaningful, whatever the wildness; the relevant local theory is the
$3$-adic one (finite flat or not at $3$, the $\ell^{\delta}$ of the optimal-level theorem), and these are exactly the curves of Conjecture
conj:euler's empirical weights $w_3$. Fix: "... so do they at $q=\ell=3$ in cases (a) and (b), which lie outside the theorem since then $\ell\mid N$
(this is the situation of the weights $w_3$ of Conjecture conj:euler)". Confidence: high for the logic. Importance: low (expository).

No other new problem was found in this chapter's area. Checked and found correct (beyond the points already recorded): the
statement and proof of Lemma lem:crit (the decomposition $\T\otimes\Q=\Q\times\T'$ needs only that the $\phi_f$-generalised eigenspace is $\C f$, which strong
multiplicity one gives; the maximal-ideal step; the $\Zl$-version); every case of Lemma lem:old, including the eigenvalue lists and
eigenvectors of $U_p$, the use of DDT Theorem 3.1(e) and the unique-stable-line argument (valid also when $p\equiv1\pmod\ell$); the optimal-level
paragraph (goodness at $\ell$, the trivial-nebentypus argument, $N(\bar\rho)\mid N$); cases (a), (b), (c) modulo points 20, 43 and N1 (levels
$M\mid N/q$, $Mq\mid N$, $Mq^2\mid N$; the hypothesis of Lemma lem:old); Lemma lem:twist(iii) (also derived from the local conductors, item 3.8);
the Example's congruences, curves and degrees (modulo points 21, 46 and B8); the 99A1 data ($\deg\varphi=4$, $r=12$); Theorem thm:twist's level
hypotheses in its three cases; Step 1 of Theorem thm:quant (every eigenvalue of $U_q$ congruent to $0$ modulo $\mathfrak m$ is exactly $0$, since the other
possible eigenvalues are $\pm1$ or roots of $X^2-a_qX+q$, units at $\ell\ne q$); the level-raising factor identity of the paragraph after Theorem
thm:dfg14.

### 7.2 Book-internal inconsistencies

* **I1. Chapter 21 outline, A3.5 case (c).** It repeats the paper's "$f'=f\otimes\chi$ on $\Gamma_0(N/q)$" (N1) and then argues "$h\ne f$ (if $h=f$ then
  $f'=f\otimes\chi$ is the $q$-depleted form of $g$; but $a_q(f')=\pm1$ ... while the depleted form has $a_q=0$ ...)", which is self-contradictory ($f\otimes\chi$ has
  $a_q=0$). Action: the Chapter 21 writer uses item 9.2 here (C4 notation, strong multiplicity one), or points to it.
* **I2. Chapter 21 outline, A1.10 (thm-qual) and A3.5.** Case (a) is stated for $q\ge5$ only; with point 43 settled (Chapter 11, 4.4) the tour
  should add the extension to $q=2$ in a commentary (B13 records the stale hedge on type $\mathrm{IV}$ at $2$ only for Proposition prop:forms and
  Remark rem:wild).
* **I3. Who proves Lemma lem:crit.** PLAN.md's Chapter 14 entry says "Lemma lem:crit of the paper proved in full here or in Chapter 20", its
  Chapter 15 entry says "prove it here in full", its Chapter 20 entry says "Chapter 15 proves it, Chapter 20 restates it"; the Chapter 21
  outline (A3.2) says "Chapter 15 and 20 also prove it". This outline follows the Chapter 15 and 20 entries (proved here, restated in
  Chapter 20); Chapters 14, 20 and 21 should cite `\Cref{ch:modgalrep}`.
* **I4. Bibliography keys shared with Chapters 7 and 11 (B14).** The Chapter 7 outline plans `Rohrlich94` and `Deligne73` (with `Tate79`)
  for `bib/ch07.bib`, and the Chapter 11 outline plans `Livne89` for `bib/ch11.bib`; this chapter needs all three, so by decision B14 they
  belong in `refs.bib`. Action: whoever writes the first of these chapters adds them to `refs.bib`.
* **I5. Chapter 11 outline, Part 0.2: "Chapter 15 proves ... the optimal-level theorem in general (DDT Theorem 3.15) ... and its proof".**
  PLAN.md 7.3 classes it as a deep imported theorem; this chapter states it (6.4, R) with a proof idea (6.7) and proves only the
  specialisation (6.5). The Chapter 11 writer should say "states" (no conflict of content).
* **I6. Chapter 12 outline, 11.5(c).** It writes $f_{20a}\otimes\chi_{-7}$ without naming the class; it is the newform of class 980g (the curve-level twist of
  20a1 is 980g2). Not an error; the Chapter 12 writer may add the label for consistency with 9.4 here.
* No conflict found with the Chapter 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16 outlines on the items cited in Part 5; the numerical data quoted in the
  Chapter 11 (6.3, 10.2), Chapter 12 (11.3, 11.5) and Chapter 21 (A3.6) outlines agree with the recomputations of Part 6.6.
