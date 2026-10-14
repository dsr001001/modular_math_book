# Chapter 20: Hecke algebras, congruence ideals and the theorem of Diamond, Flach and Guo (`ch:congruence`, `chapters/ch20_congruence.tex`)

Stage 1 line-up. Part VI (Congruences, the modular degree and the paper). Target length 2,670 lines of LaTeX (the card excluded;
see Part 3), inside the 2,800 lines that PLAN.md Section 7.3 allows this chapter.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2 to 19
outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book and chapter or
section; a theorem number only where sure, otherwise marked "(verify)" or given by section); the paper's use by its `\label`
names, or "background"; and, for an item owned by another chapter, the item there (as "Chapter NN, its x.y").

**DFG04 was read for this outline.** The published text (Ann. Sci. Ec. Norm. Sup. (4) 37 (2004), 663-727, from Numdam, 65 pages)
and the longer arXiv version (arXiv:2512.02348, "August 2001, with minor update December 2025", 109 pages, with different
section numbers) were downloaded and read in the parts the paper cites. All DFG04 numbers below are those of the **published**
version, which is the one the paper cites (`DFG04` in `refs.bib`). Part 7 ("DFG04 checklist") records what DFG04 says, item by item,
with quotations. Every number quoted below (modular degrees, Euler terms, twist pairs) was checked with PARI/GP 2.17 through
`cypari2` and Cremona's `ecdata` files for conductors below 10,000 (verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

Chapter 20 is the place where the paper's Section 4 is proved, and where the commutative algebra of congruences meets the
theorem of Diamond, Flach and Guo. The chapter **assembles**; it does not re-derive what other chapters prove. Its own content:

1. **Congruence modules and congruence ideals** (Section 1: "The congruence number is the congruence ideal of $f$ in the full
   Hecke algebra of level $N$ (Lemma lem:crit), and the theory of such ideals, from Hida to Diamond, Flach and Guo, expresses them
   through the adjoint Selmer group and the adjoint $L$-value"). The abstract congruence module $\T/(\wp+I)\simeq\mathcal O/\eta$ (from
   Chapter 3, its 11.1), its reading in $\T_{\mathfrak m}$, the congruence ideal of a newform and of a depleted eigenform, Lemma lem:crit
   restated in this language (proved in Chapter 15, its 8.2, decision B17), and Hida's theorem as context.
2. **Wiles's numerical criterion and Lemma lem:ddt417 in full** (Section 4.1, Lemma lem:ddt417). Statement of the criterion
   (Wiles, Lenstra) for orientation, and the inequality half that the paper uses, proved in the paper's generality with the
   corrections of important_notes.md points 19 and 38, every ingredient cited from Chapter 3 (its 9.3, 9.4, 9.5, 11.1, 11.3).
3. **The lattices and ideals of DFG04** (Section 4.1). $f^\Sigma$, $M^\Sigma$, the integral structure, the kernel lattice $M_{f^\Sigma,\lambda}$, the
   pairing $\hat\delta_!$, the naive $\Sigma$-finite congruence ideal $\eta^\Sigma_{f,\lambda}$, exactly as DFG04 Sections 1.5.3, 1.6.1, 1.6.2, 1.7.3 define them,
   with the comparison to $H^1(X_0(M^\Sigma),\Z_\ell)$ that the paper asserts (Part 7, items 1 to 5). Lemma lem:hecke and Remark rem:free
   are **cited** from Chapter 14 (its 9.3, 9.5, 9.6, 10.3), not re-derived; this chapter adds that the DFG04 checklist of
   important_notes.md point 56 is now confirmed, so Lemma lem:hecke is an equality for DFG04's own $\eta$.
4. **DFG04 Proposition 1.4** (Theorem thm:dfg14): the statement, the three cases (additive: no change; good: Wiles's
   level-raising factor; multiplicative: $1-p^{-2}$), and the proof idea ($\gamma=\sum_m\epsilon_m\phi_m$, $\gamma^t\gamma=\phi\cdot\prod L^{\nv}_p(A_f,1)^{-1}$, Ihara).
5. **The exceptional set $S_f$, Theorem 3.7 and the Taylor-Wiles method in outline** (Theorem thm:dfg37, Theorem thm:dfg27,
   Section 4.2). DFG04 (31), "minimally ramified", Theorems 0.1, 0.2, 2.7, 3.7, the axiomatic Theorem 3.1 of DFG04, and a
   two-page account of why the length of a Selmer group equals the valuation of a congruence ideal. Open check Q1 is settled:
   DFG04 covers $\ell=3$ in weight $2$.
6. **The assembly of Theorem thm:main**, step by step, each input cited to the chapter that proves it (Chapter 14 for Lemma
   lem:hecke, Chapter 18 for the Selmer half, its 11.1, Chapter 19 for the naive factors, its 9.7), with the corrections of
   important_notes.md points 18, 39, 56, 63, 64, and the reading "(eq:identity) holds with equality for $\ell\notin S_f$".
7. **Theorem thm:twist and Theorem thm:quant in full**, with the remark after Theorem thm:quant, the corrections of points 16, 24,
   59, 60, 61, and a new observation (Part 8, N2): the first inequality of Theorem thm:quant is an **equality** whenever $\ell\notin S_f$,
   with no multiplicity-one hypothesis (verified on all $25{,}477$ test pairs below conductor $10{,}000$).
8. **Remark rem:ko, Remark rem:ns, Open questions 1 and 2**, with point 67.

The physics reader meets two familiar ideas, one sentence each: a congruence module measures how far an orthogonal
decomposition of a lattice fails to be a direct sum over $\Z$ (the "overlap" of two eigenspaces, as for normal modes of a
crystal lattice whose unit cells do not split); and the numerical criterion is an index theorem ("the dimension of the tangent
space bounds the defect, with equality exactly in the complete-intersection case").

### 1.2 Split with the neighbouring chapters (decided here, consistent with PLAN.md Section 4 and the written outlines)

* **Chapter 3** proves all module theory: saturation (5.5), perfect pairings and the Gram cokernel (9.1 to 9.3), alternating rank-two
  pairings (9.4: $\Delta=(\text{ideal of values})^2$), adjoints and idempotents (9.5), algebra-module duality (9.6), finite free algebras,
  idempotent lifting, generalised eigenspaces (10.1 to 10.6), congruence ideals with $\wp\cap I=0\iff\eta\ne0$ and the computation in $\T_{\mathfrak m}$ (11.1),
  toy congruence algebras (11.2), **every ingredient of Lemma lem:ddt417** (11.3), Gorenstein (11.4), Mazur's freeness criterion (11.5).
  Chapter 20 cites these and writes only the assembly of Lemma lem:ddt417 (as Chapter 3, its 11.3, says).
* **Chapter 13** proves the Hecke algebra $\T$ and its perfect pairing with $S_2(N;\Z)$ (4.1, 4.2), the Hecke congruence ideal $\eta(\phi)$ and
  $r_f$ (4.3), Petersson adjoints (5.1 to 5.4), newforms, strong multiplicity one, $U_p$ on oldforms, depletion $f^\Sigma$, $M^\Sigma$, $\delta_p$ (6.2 to
  7.4), the $\T$-stable complement (8.2), $\T_\ell=\prod\T_{\mathfrak m}$ on forms (8.3), congruences (8.4), the twist operator $\iota$ and the transport lemma
  (9.1, 9.3), Atkin-Li (9.2), the computed congruence modules at level $539$ (11.3). Chapter 20 cites them; Chapter 13 explicitly leaves
  the proofs of Theorems thm:twist and thm:quant to Chapter 20.
* **Chapter 14** proves the cup-product adjoint $t^t=w_Ntw_N$ and the pairing $\hat\delta_!$ (3.3, 3.4, with the orthogonal $\mathfrak m$-decomposition,
  point 36), the lattice $M_{f,\lambda}$ (4.4), the optimal curve (6.2), the congruence number and Agashe-Ribet-Stein (8.1 to 8.5), **point 39
  in full** (9.1 to 9.5: $M_{f,\lambda}=\varphi_E^*H^1(E,\Z_\ell)$, $\hat\delta_!$ has ideal of values $\deg\varphi_E\Z_\ell$, Lemma lem:hecke as an equality), the DFG04
  checklist (9.6), the 99 at 3 example (9.7), multiplicity one, Gorenstein and Remark rem:free (10.1 to 10.4). Chapter 20 cites 9.3, 9.5,
  9.6, 10.3 (important_notes.md B19), and resolves 9.6 (Part 7 here).
* **Chapter 15** proves Lemma lem:crit (8.2) and Lemma lem:old (8.3), states Theorem thm:dfg14 (7.3), proves the level-raising factor
  identity (7.2), states Ihara's lemma (7.4), proves the levels of twists (10.1, 10.2), states thm:twist and thm:quant (10.3, 10.4) for
  Chapter 20 to prove, states Pollack-Weston and Kim-Ota (11.3, 11.4) and gives a one-page Taylor-Wiles remark (11.5). Chapter 20 does
  not reprove lem:crit; it restates it as a statement about congruence modules (3.4 here).
* **Chapter 17** proves the abstract form of DFG04 Lemma 2.1 (its 10.3) and the length identity (10.4).
* **Chapter 18** proves Lemma lem:fpr (7.4, 7.5), Lemma lem:tamfactor (8.2), the Tamagawa factors at every additive prime (8.4, 9.3:
  point 64), Lemma lem:dfg21 in the paper's form (10.4), Lemma lem:h0 in Selmer language (10.3, from Chapter 11, its 8.5), the length
  identity (10.5), **the Selmer half of Theorem thm:main** (11.1), Remark rem:ns (12.1), and states DFG04 Theorems 0.1, 0.2, 2.7 (14.4,
  14.5, 10.2) and $S_f$ (10.1). Chapter 20 cites 11.1 rather than repeating the Selmer bookkeeping (as Chapter 18 asks).
* **Chapter 19** proves Lemma lem:euler (9.3), the naive factors at $s=1$ and the cancellation (9.7), $A_g=A_f$ (9.5), the $L$-part of Lemma
  lem:fpr (9.6), the Petersson formula with $L^{\nv}$ (8.3).
* **Chapter 21** is the guided tour; its A4 items walk through the same proofs at the level of the paper's text and should cite
  this chapter's card for the full arguments (Part 5).

### 1.3 Global conventions fixed in this chapter

* **C1 (the newform and the coefficients).** $f$ is a newform of weight $2$ on $\Gamma_0(M)$ (trivial character). In Sections 2 to 8 the
  coefficients may lie in a number field $K$ with a prime $\lambda\mid\ell$ and $\mathcal O=\mathcal O_{K,\lambda}$; from Section 9 on, $f=f_E$ has rational coefficients,
  $K=\Q$, $\lambda=\ell$, $\mathcal O=\Z_\ell$ (the paper's "$\lambda=\ell$"). $\ell$ is odd and $\ell\nmid M$ unless said otherwise.
* **C2 (Hecke algebras).** $\T=\T_M=\Z[T_n:n\ge1]\subset\End S_2(\Gamma_0(M))$, the **full** Hecke algebra, $U_p$ included (Chapter 13, C4); DFG04's $\T$ of
  Section 1.6.1 is the same ring (generated by the $T_p$ for all $p$, the double coset of $\operatorname{diag}(p,1)$ at $p\mid M$ being $U_p$). $\T_\ell=\T\otimes\Z_\ell$,
  $\mathfrak m$ a maximal ideal of $\T_\ell$, $e_{\mathfrak m}$ its idempotent. $\T$ acts on $H^1(X_0(M),\Z_\ell)$ by $t^*$ (Chapter 14, C2).
* **C3 (congruence data).** For a surjective $\mathcal O$-algebra map $\pi\colon\T_{\mathcal O}\to\mathcal O$: $\wp=\ker\pi$, $I=\Ann(\wp)$, $\eta(\pi)=\pi(I)$, congruence module
  $\Omega(\pi)=\T_{\mathcal O}/(\wp+I)\simeq\mathcal O/\eta(\pi)$ (Chapter 3, its 11.1; Chapter 13, its 4.3). The paper's letters: $I$ in Lemma lem:crit is the book's
  $\wp$, the paper's $J$ is the book's $I$; the card says so once (a `warning`).
* **C4 (two congruence ideals).** $\eta^{\mathrm{Hecke}}(\pi)$ is $\eta(\pi)$ of C3 (algebraic, computed in $\T_{\mathfrak m}$); $\eta^\Sigma_{f,\lambda}$ is DFG04's naive
  $\Sigma$-finite congruence ideal (cohomological, 5.4). Lemma lem:ddt417 compares them: $v(\eta^{\mathrm{Hecke}})\ge v(\eta^{\mathrm{coh}})$.
* **C5 (lengths).** All counts are $\mathcal O$-lengths, not orders (important_notes.md point 38); for $\mathcal O=\Z_\ell$ the two agree.
* **C6 (Frobenius, duals, twists).** As in Chapters 7 and 18: $\Frob_p$ arithmetic, $\Phi_p=\Frob_p^{-1}$ geometric, $L_p(V,s)=\det(1-\Phi_pp^{-s}\mid V^{I_p})^{-1}$
  (DFG04 Section 1.1.1 writes $\Frob_p$ for the geometric Frobenius: confirmed, Part 7); $V^D=\Hom(V,\Q_\ell(1))$, $T^D$, $W^D$; ${}^*$ is the Pontryagin
  dual only (B4), $A^\dagger$ the adjoint, $M^\vee=\Hom(M,\mathcal O)$.
* **C7 (characters and twists).** $\chi_{q^*}$ for the paper's $\chi_q$ (point 32), $\chi_S=\prod_{q\in S}\chi_{q^*}$, $D=\prod_{q\in S}q$, $\iota=\iota_S\colon h\mapsto h\otimes\chi_S$ (Chapter 13,
  its 9.1(vi)); $E_S=E\otimes\chi_S$, $N_S$ its conductor, $g=f_{E_S}$; $E^{(q)}$ for the paper's $E_{\{q\}}$.
* **C8 (typography).** PLAN.md Section 7.2; "Diamond-Flach-Guo", "Taylor-Wiles", "Agashe-Ribet-Stein", "Fontaine-Perrin-Riou",
  "Fontaine-Laffaille", "Kim-Ota", "Pollack-Weston" with plain hyphens; labels `...:congruence:...`.

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 1. Overview and conventions

**1.1 `conv:congruence:setup`** (conventions C1 to C8 as `convention` environments, with a roadmap; P). A roadmap table "sentence
of the paper's Section 4 $\to$ item of this chapter $\to$ chapter that proves the input". A `warning` box for C3 (the paper's $I$, $J$ versus
$\wp$, $I$) and for C4 (two congruence ideals). Paper: Section 4 (all of it).

### Section 2. Hecke algebras over $\Z_\ell$ and their local components (recollection)

**2.1 `prop:congruence:hecke-local`** (proposition, a recollection; P by citation). (i) $\T$ is free of rank $\dim S_2(\Gamma_0(M))$ over $\Z$ (Chapter 13, its 4.1),
so $\T_\ell$ is a finite free $\Z_\ell$-algebra and $\T_\ell=\prod_{\mathfrak m}\T_{\mathfrak m}$ over its finitely many maximal ideals (Chapter 3, its 10.2, 10.3). (ii) For a newform $f$
and $\lambda\mid\ell$, $\mathfrak m=\mathfrak m_{f,\lambda}$ is the kernel of $\T_\ell\to\mathcal O\to\mathcal O/\lambda$, generated by $\lambda$ and the $T_n-a_n(f)$ (Chapter 13, its 3.4). (iii)
$e_{\mathfrak m}S_2(M;\Z_\ell)\otimes\overline\Q_\ell$ is the sum of the generalised eigenspaces of the eigensystems $\phi\colon\T\to\overline\Q_\ell$ with $\phi\equiv\phi_f$ modulo the maximal
ideal of $\overline\Z_\ell$; for newforms $g$ this means $\bar\rho_g\simeq\bar\rho_f$ (semisimplifications; Chapter 13, its 8.3; Chapter 15, its 2.5). (iv) The pairing
$S_2(M;\Z_\ell)\times\T_\ell\to\Z_\ell$ is perfect on each $\mathfrak m$-component (Chapter 13, its 8.3(iii)); $\hat\delta_!$ on $H^1(X_0(M),\Z_\ell)$ is perfect on each
$\mathfrak m$-component, the decomposition being orthogonal (Chapter 14, its 3.4(iii); important_notes.md point 36). Paper: Lemma lem:hecke ("$\mathfrak m$
the maximal ideal of $\T\otimes\Z_\ell$ containing $\ell$ and $\ker\phi_f$"), Remark rem:free, Theorem thm:quant Step 1, PLAN.md scope.

**2.2 `ex:congruence:level-539`** (worked example; P as a computation, from Chapter 13, its 11.3). At level $539=7^2\cdot11$ and $\ell=3$: the
newforms of 539c and 539d, the depleted forms $(77\mathrm c)^{\{7\}}$ and $(11\mathrm a)^{\{7\}}$, and which of them share a maximal ideal of $\T_{539}\otimes\Z_3$;
the Hecke congruence modules of the depleted forms have orders $288$ and $504$, equal to $r(539\mathrm c)$ and $r(539\mathrm d)$. Used as the running
example of Sections 3, 12. Paper: Theorem thm:quant (background).

### Section 3. Congruence modules and congruence ideals

**3.1 `def:congruence:congruence-module`** (definition and proposition; P by citation of Chapter 3, its 11.1). Let $\mathcal O$ be a complete DVR,
$\T$ a commutative $\mathcal O$-algebra, finite and free over $\mathcal O$, $\pi\colon\T\to\mathcal O$ surjective. With C3: (i) $\Omega(\pi)=\T/(\wp+I)\simeq\mathcal O/\eta(\pi)$; (ii)
$\eta(\pi)\ne0\iff\wp\cap I=0\iff$ the factor of $\T\otimes K$ through which $\pi$ factors is $K$ (multiplicity one); (iii) if $\eta\ne0$, $I\simeq\eta$ is free of rank one,
$\Ann(I)=\wp$, and $\eta=\{a\in\mathcal O:ae_\pi\in\T\}$ ("the denominator of the idempotent"); (iv) $\eta(\T,\pi)=\eta(\T_{\mathfrak m},\pi|_{\T_{\mathfrak m}})$: the other local factors lie
in $\ker\pi$, **not** in $\Ann(\ker\pi)$ (important_notes.md point 35); (v) the second module $\Phi(\pi)=\wp/\wp^2$, the cotangent space, finite iff $\T\otimes K$ is
reduced at $\pi$ (P; one line: $\wp\otimes K/\wp^2\otimes K$ is the cotangent space of $\T_K$ at $\pi$, zero iff the factor is $K$). Reference: DDT Section 4 and
Section 5.1 (cite the sections); Lenstra95 (proposed key, Part 6.5); Hida81 Section 1 (cite the section). Paper: Lemma lem:crit,
Lemma lem:ddt417, Lemma lem:hecke, Theorem thm:quant Step 1, Section 6 map row (Hida's congruence modules).

**3.2 `ex:congruence:toy`** (examples; P, from Chapter 3, its 11.2). $\T_r=\{(a,b)\in\mathcal O^2:a\equiv b\pmod{\varpi^r}\}$: $\Omega=\mathcal O/\varpi^r$, $\Phi=\mathcal O/\varpi^r$ ("two eigenforms
congruent modulo $\varpi^r$"); $\T_3^\flat$ (three pairwise congruent forms): $\eta=\varpi\mathcal O$ but $\Phi\simeq(\mathcal O/\varpi)^2$, so $\#\Phi>\#\Omega$: not a complete intersection;
$\mathcal O[\varepsilon]/(\varepsilon^2)$: $\eta=0$, $\Phi=\mathcal O$. These three examples are the whole content of the numerical criterion (4.1) in miniature. Paper:
background for Lemma lem:ddt417.

**3.3 `def:congruence:newform-ideal`** (definition and proposition; P). For a newform $f$ of level $M$ with coefficients in $\mathcal O_K$ and $\lambda\mid\ell$,
$\phi_f\colon\T\otimes\mathcal O\to\mathcal O$ (Chapter 13, its 3.4) is surjective after enlarging $\mathcal O$ to contain the $a_n(f)$ (its image is an order; replace $\T\otimes\mathcal O$ by the
$\mathcal O$-algebra it generates). The *Hecke congruence ideal* $\eta_f=\eta(\phi_f)$ is nonzero (strong multiplicity one: the $\phi_f$-generalised eigenspace is
$\C f$, Chapter 13, its 8.1(iv)). For $f=f_E$: $\eta_f\Z_\ell=r_E\Z_\ell$ (Lemma lem:crit, 3.4). Paper: Section 1 ("the congruence ideal of $f$ in the full
Hecke algebra"), Lemma lem:crit, Lemma lem:hecke.

**3.4 `thm:congruence:crit`** (theorem, the paper's Lemma lem:crit restated; R here, **proved in full in Chapter 15, its 8.2**; the
module-theoretic reading P). Let $f=f_E$, $\T$ the full Hecke algebra of level $N$, $\phi_f$, $\wp=\ker\phi_f$ (the paper's $I$), $I=\Ann_\T(\wp)=\Ann_\T(f^\perp)$
(the paper's $J$). Then $\T/(\wp+I)\simeq\Z/r_E$, i.e. the congruence module of $\phi_f$ is cyclic of order the congruence number, and the same over
$\Z_\ell$ with $r_E$ replaced by its $\ell$-part; a normalised eigenform $g\in f^\perp$ of all of $\T$ congruent to $f$ at **every** $n$ modulo $\lambda\mid\ell$ forces $\ell\mid r_E$.
Module-theoretic reading (P, from Chapter 3, its 5.8, 9.6): under the perfect pairing $S_2(N;\Z)\times\T\to\Z$, $\Omega(\phi_f)^*\simeq S_2(N;\Z)/(\Z f\oplus L)$ with
$L=f^\perp\cap S_2(N;\Z)$: **the congruence module is dual to the failure of $S_2(N;\Z)$ to split along the eigenspace decomposition.** Paper: Lemma
lem:crit, Section 1, Lemma lem:hecke, Theorem thm:twist, Theorem thm:quant Step 1.

**3.5 `prop:congruence:crit-general`** (proposition; P given Chapter 13, its 8.2, and Chapter 15, its 8.2). Let $\pi\colon\T_N\to\Z$ be an eigencharacter
whose generalised eigenspace in $S_2(\Gamma_0(N))\otimes\overline\Q$ is a line $\C g$ (a newform at its level; a depleted form $f^\Sigma$ at level $M^\Sigma$, Chapter 13,
its 7.4(iv); $g^S$ at level $N$ in Theorem thm:quant). Let $g^c$ be the **$\T$-stable** complement of $\C g$ (the sum of the other generalised
eigenspaces). Then the proof of 3.4 runs verbatim with $g^c$ in place of $f^\perp$: $\T/(\ker\pi+\Ann\ker\pi)\simeq\Z/r(\pi)$ with $r(\pi)$ the largest modulus of a
congruence $g\equiv h$, $h\in g^c\cap S_2(N;\Z)$; the same over $\Z_\ell$. **Warning** (important_notes.md point 61): for $g$ not a newform the Petersson
complement is not $\T$-stable (level $44$: Chapter 13, its 8.2(iii)); the paper's text uses the $\T$-stable complement, which is right.
Paper: Theorem thm:quant Step 1 ("the proof of Lemma lem:crit, carried out over $\Z_\ell$ ... in the $\T$-stable complement of the $g^S$-line").

**3.6 `thm:congruence:hida`** (theorem; R). (Hida 1981.) For a newform $f$ of weight $k\ge2$ and level $N$ and a prime $\lambda$ outside an
explicit finite set (dividing $N$, $(k-2)!$ and $6$ in Hida's statement; check), the congruence primes of $f$ (the primes dividing $\eta_f$)
are exactly the primes dividing the algebraic part $L^{\nv}(A_f,1)/\Omega_f^+\Omega_f^-$ of the adjoint $L$-value, with $\langle f,f\rangle$ related to
$L^{\nv}(A_f,1)$ by the Rankin-Shimura formula (Hida81 Theorem 5.1, as DFG04 Lemma 2.12 cites it: verified there, Part 7). The book states this
as context only: the paper never uses Hida's theorem in a proof, and DFG04's $\eta^\emptyset_{f,\lambda}$ is the refinement used instead.
Reference: Hida81 (cite by section except Theorem 5.1, verified as cited by DFG04); HidaBook (cite the chapter); Ribet83 (congruence
primes); Zagier85. Paper: Section 1 ("from Hida to Diamond, Flach and Guo"), Section 6 map row (Hida's congruence modules).

**3.7 `rem:congruence:two-ideals`** (remark; P). The three ideals of this chapter and their relations, displayed once: $r_E\Z_\ell=\eta^{\mathrm{Hecke}}_f$ (3.4),
$v(\eta^{\mathrm{Hecke}}_f)\ge v(\eta^\emptyset_{f,\lambda})$ (Lemma lem:ddt417, 4.3 and 5.6), $v(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$ for the optimal curve (Chapter 14,
its 9.3, with Part 7 here), $v_\ell(\deg\varphi_E)=v_\ell(r_E)$ for $\ell^2\nmid N$ (ARS12). Hence all three agree at $\ell\nmid N$, and the inequality of Lemma lem:ddt417 is
strict exactly where freeness fails ($99$a1 at $3$: Chapter 14, its 9.7). Paper: Lemma lem:hecke, Remark rem:free.

### Section 4. Wiles's numerical criterion and Lemma lem:ddt417

**4.1 `thm:congruence:numerical-criterion`** (theorem; R, with the proof idea S). (Wiles; Lenstra.) Let $\mathcal O$ be a complete DVR with finite
residue field, $\T$ a local $\mathcal O$-algebra, finite and free over $\mathcal O$, $\pi\colon\T\to\mathcal O$ surjective, $\Phi=\wp/\wp^2$, $\eta=\eta(\pi)\ne0$. Then (i)
$\len\Phi\ge v(\eta)$; (ii) equality holds (with $\Phi$ finite) iff $\T$ is a complete intersection over $\mathcal O$; (iii) (the form used in Taylor-Wiles) if
$R\twoheadrightarrow\T$ is a surjection of complete local Noetherian $\mathcal O$-algebras compatible with $\pi$ and $\len\Phi_R\le v(\eta_\T)<\infty$, then $R\to\T$ is an isomorphism
of complete intersections. Proof idea (one paragraph): for a complete intersection $\T=\mathcal O[[x_1,\dots,x_n]]/(f_1,\dots,f_n)$ both sides equal $v(\det(\partial f_i/\partial x_j)(\pi))$
(Tate's computation of $\Ann(\wp)$ through the Jacobian); in general reduce to it by a flat-deformation argument (Lenstra). Examples 3.2 show
each case. Reference: Wiles95 Chapter 2 (Appendix); Lenstra95; DDT Section 5.1 (Wiles's numerical criterion; the theorem number to be
verified: the paper's "DDT Theorem 5.3" in PLAN.md is not confirmed); Mazur's survey in the Cornell-Silverman-Stevens volume (cite by section).
Paper: background (Section 6 map row "Wiles's numerical criterion"); the inequality half in the presence of a module is 4.3.

**4.2 `rem:congruence:why-a-module`** (remark; P). Why the paper needs a version **with a module**: the ideal that DFG04 control is not
$\eta(\pi)$ (an invariant of the ring) but the ideal of values of a pairing on the $\pi$-part of a module $L$ (5.4). Lemma lem:ddt417 compares
the two; it is an equality exactly when $L$ is free over $\T$, which is what multiplicity one gives (Chapter 3, its 11.5; Chapter 14, its 10.3).
Paper: Section 4.1 ("We also need the following piece of commutative algebra, which is the inequality half of DDT Lemma 4.17").

**4.3 `lem:congruence:ddt417`** (lemma, the paper's Lemma lem:ddt417; **P**, every step, in corrected form). Let $\mathcal O$ be a DVR, $\T$ a commutative
$\mathcal O$-algebra, finite and free over $\mathcal O$, $L$ a $\T$-module free of finite rank over $\mathcal O$ with a perfect $\mathcal O$-bilinear pairing $\langle\ ,\ \rangle$ for which every
$t\in\T$ is self-adjoint, $\pi\colon\T\to\mathcal O$ surjective, $\wp=\ker\pi$, $I=\Ann_\T(\wp)$, $\eta=\pi(I)$. Suppose $L[\wp]$ is free of rank $d$ over $\mathcal O$ with Gram
determinant $\Delta\ne0$. Then $\eta^d\subseteq\Delta\mathcal O$, i.e. $d\,v(\eta)\ge v(\Delta)$; equality holds if $L$ is free over $\T$. Proof (the paper's, with every
step expanded and lengths in place of orders, point 38): (0) if $\eta=0$ there is nothing to prove; assume $\eta\ne0$, so $\wp\cap I=0$ (3.1(ii),
Chapter 3, its 11.1(ii): **not** "because $\T$ is reduced", point 19; $\T_{88}\otimes\Q$ is not reduced, Chapter 13, its 7.3). (1) Fix $t\in I$ with $\pi(t)$ a
generator of $\eta$; for $x\in L$, $tx\in L[\wp]$ ($\wp I=0$) and $(\pi(t)-t)x\in L[I]$ ($I(\pi(t)-t)\subseteq I\wp=0$); so $Q=L/(L[\wp]+L[I])$ is killed by $\eta$. (2) $L[\wp]\cap L[I]=0$
(an element killed by $\wp+I\ni\pi(t)$ is killed by $\pi(t)\ne0$; Chapter 3, its 11.3(ii)). (3) $L[\wp]$ is saturated and $L[\wp]^\perp=L[I]$ (Chapter 3, its 11.3(i),
(iii)). (4) The map $L\to\Hom(L[\wp],\mathcal O)$, $y\mapsto\langle-,y\rangle$, is onto with kernel $L[I]$ (Chapter 3, its 9.3(i)), so $Q\simeq\coker(L[\wp]\to\Hom(L[\wp],\mathcal O))$, of length
$v(\Delta)$ (Chapter 3, its 9.3(ii)). (5) $Q$ is generated by $d$ elements and killed by $\eta$, hence a quotient of $(\mathcal O/\eta)^d$: $v(\Delta)=\len Q\le d\,v(\eta)$. (6) If
$L\simeq\T^r$ then $L[\wp]=I^r$, so $r=d$ (as $I$ is free of rank one), $L[I]=\Ann(I)^r=\wp^r$ and $Q\simeq(\T/(\wp+I))^d\simeq(\mathcal O/\eta)^d$, of length $d\,v(\eta)$
(Chapter 3, its 11.3(v)). Remarks to print: (a) in the lemma's generality $\wp\cap I=0$ can fail ($\mathcal O[\varepsilon]/(\varepsilon^2)$ acting on $\mathcal O$), but then $\eta=0$; (b)
if $\eta=0$ and $L$ is free, then $\Delta=0$, so the hypothesis $\Delta\ne0$ already forces $\eta\ne0$ in the free case (Chapter 3, its 11.6); (c) self-adjointness
is used only in (3). Reference: DDT Lemma 4.17 (as cited by the paper; the book proves only the inequality half and the equality
clause, which is what the paper states). Paper: Lemma lem:ddt417, Lemma lem:hecke, Theorem thm:quant Step 2.

**4.4 `ex:congruence:ddt417-checks`** (examples; P, from Chapter 3, its 11.6, and Chapter 14, its 9.7). (a) $L=\T_r$ with the trace-type pairing:
$d=1$, equality. (b) $L=\mathcal O^2$ with $\T_r$ acting diagonally and the standard pairing: $\Delta=1$, $v(\eta)=r$, strict; $L$ is not free. (c) $L=\T_r^2$ with an
alternating pairing: $d=2$, $\Delta=\eta^2$: the shape of Lemma lem:hecke. (d) The modular instance: $L=H^1(X_0(99),\Z_3)_{\mathfrak m}$ for 99a1: $v_3(\eta^{\mathrm{Hecke}})=1$,
$v_3(\Delta)=0$ (the ideal of values is $4\Z_3=\Z_3$), strict, so $L$ is not free (Chapter 14, its 9.7). Paper: Lemma lem:ddt417, the remark after
Theorem thm:qual (99A1).

### Section 5. The lattices and ideals of Diamond, Flach and Guo; Lemma lem:hecke and Remark rem:free

**5.1 `def:congruence:depletion-recall`** (definition, recalled from Chapter 13, its 7.4; P by citation). For a newform $f$ of level $M$ and a
finite set $\Sigma$ of primes: $\delta_p=2,1,0$ according as $p\nmid M$, $p\,\|\,M$, $p^2\mid M$ (for $f=f_E$: good, multiplicative, additive; $=\dim V^{I_p}$, and DFG04
Section 1.7.2 defines $\delta_p=\dim M_{f,\lambda}^{I_p}$, the same number since $M_{f,\lambda}$ is the dual of $V$); $M^\Sigma=M\prod_{p\in\Sigma}p^{\delta_p}$; $f^\Sigma=\sum_{(n,\Sigma)=1}a_nq^n$, a
normalised eigenform of the full $\T_{M^\Sigma}$ with $U_pf^\Sigma=0$ ($p\in\Sigma$), whose generalised eigenspace at level $M^\Sigma$ is the line $\C f^\Sigma$ (Chapter 13, its
7.4(iv)). The naive factor: $L^{\nv}_p(A_f,s)=L_p(A_f,s)$ if $\delta_p>0$, $1$ if $\delta_p=0$ (DFG04 Section 1.7.2; Chapter 19, its 8.1). Paper: Section 4.1
("Put $M^\Sigma=\dots$"), Section 1.1 ("We follow the conventions of DFG04 Section 1.7.2").

**5.2 `def:congruence:integral-structure`** (definition and proposition; R for DFG04's construction, P for the comparison (ii) given
Chapters 8, 14 and the argument of Part 7, item 1). (i) (DFG04 Sections 1.2, 1.4.1, 1.4.2.) DFG04's integral structure at level $M$ and
trivial character is $M(M,1)_{!,\lambda}$: the image of $\bigl(H^1_c(Y_{N'},\Z_\ell)\bigr)^{U_0(M)}\to\bigl(H^1(Y_{N'},\Z_\ell)^{U_0(M)}\bigr)_{\mathrm{tf}}$, where $Y_{N'}$ is the (adelic, geometrically
disconnected) full level-$N'$ modular curve for an auxiliary $N'\ge3$ with $U_{N'}\subset U_0(M)$, and $U_0(M)$ acts through $U_0(M)/U_{N'}$ (independent of $N'$,
DFG04 Section 1.4.1). (ii) (Comparison, the paper's "$M(M^\Sigma,1)_{!,\lambda}$ is $H^1(X_0(M^\Sigma),\Z_\ell)$".) Pullback identifies $H^1(X_0(M),\Z_\ell)$ with a
$\T$-stable sublattice of finite index of $M(M,1)_{!,\lambda}$; the index is $1$ when $\ell$ does not divide the order of the relevant covering group
(transfer), and in general the quotient is a subquotient of $\Hom(U_0(M)/U',\Q_\ell/\Z_\ell)$ for a torsion-free congruence subgroup $U'$, i.e. it comes from
abelian unramified subcovers of congruence covers of $X_0(M)$, of Shimura-subgroup type, on which $\T$ acts through Eisenstein ideals. So
for every **non-Eisenstein** $\mathfrak m$, $M(M,1)_{!,\lambda,\mathfrak m}=H^1(X_0(M),\Z_\ell)_{\mathfrak m}$ (S; the Eisenstein claim cited to Ling-Oesterle and Ribet88 for the
Shimura covering and stated as a sketch in general, Part 7 item 1). DFG04's own Lemma 1.8 and Corollary 1.9 use the same "kernel and
cokernel are Eisenstein" device. (iii) The paper only ever uses the $\mathfrak m$-part for $\mathfrak m=\mathfrak m_{f,\lambda}$ with $\bar\rho_f$ irreducible, where (ii) applies.
Reference: DFG04 Sections 1.2.2, 1.2.3, 1.4.1, 1.4.2; Chapter 14, its 4.3, 9.6, 11.3. Paper: Section 4.1 ("The integral structure
$M(M^\Sigma,1)_{!,\lambda}$ is $H^1(X_0(M^\Sigma),\Z_\ell)$, with its Hecke action").

**5.3 `def:congruence:dfg-pairing`** (definition and proposition; P for (ii) to (iv) given Chapter 14, its 3.3, 3.4; R for DFG04's
normalisation (i)). (i) (DFG04 Sections 1.5.1 to 1.5.3, (13), (14).) DFG04's $\hat\delta_!$ is the cup product into $H^2_c$, restricted to $U$-invariants
and divided by $[U:U_{N'}]$ (their $\bar\delta$, (11), (12)), composed with the operator $[UwU]_\omega$, $w=\begin{psmallmatrix}0&-1\\M&0\end{psmallmatrix}\in\prod_{p\mid M}\GL_2(\Z_p)$, which for
weight $2$ and trivial character is the Atkin-Lehner involution (DFG04 Section 1.5.3: $[UwU]_\omega$ "coincides with $\psi(-1_\infty)N^{k-2}[Uw^{-1}U]_\omega$", so
for $k=2$, $\psi=1$ it is an involution, with no scalar); "since $M(N,\psi)=0$ unless $\psi(-1_\infty)=(-1)^{k-2}$, ... the corresponding perfect pairing is
alternating". (ii) On pulled-back classes $\hat\delta_!(\pi^*x,\pi^*y)=c\cdot\langle x,w_M^*y\rangle_{X_0(M)}$ with $c=\deg(Y_{N'}\to Y_0(M))/[U:U_{N'}]\in\{1,\tfrac12\}$ ($-1\in U$ acts
trivially): a unit for odd $\ell$. So on $H^1(X_0(M),\Z_\ell)_{\mathfrak m}$, DFG04's $\hat\delta_!$ is, up to a unit, the pairing $\langle x,w_M^*y\rangle$ of Chapter 14, its 3.4 (which the book also calls $\hat\delta_!$, Appendix B, B-C13(f)). (iii) It
is perfect and alternating, and every $t\in\T$ ($U_p$ included) is self-adjoint for it (Chapter 14, its 3.3, 3.4(ii); DFG04 Section 1.5.2 last
paragraph and 1.8.2). (iv) Its restriction to every $\mathfrak m$-component is perfect (Chapter 14, its 3.4(iii); point 36). Paper: Section 4.1 ("the pairing
$\hat\delta_!$ is the cup product composed with the operator $[UwU]\omega$ ... perfect and alternating ... self-adjoint"), Lemma lem:hecke, Theorem thm:quant
Step 2.

**5.4 `def:congruence:eta-sigma`** (definition and proposition; P for (iii), (iv), R for (i), (ii) as DFG04's definitions). Let $\lambda\nmid2M$ (C1).
(i) (DFG04 Section 1.6.2.) For a normalised eigenform $h$ of $\T_{M'}$ with eigencharacter $\theta_h$, $M_{h,\lambda}:=M(M',1)_{!,\lambda}[\ker\theta_h]$, the **kernel** lattice
("Let $I_f=\ker\theta_f$ and $M_f=M(N,\psi)_![I_f]$", with $M[I]$ the kernel of $M\to M^r$, $x\mapsto(x_1x,\dots,x_rx)$, DFG04 Section 1.1.2). (ii) (DFG04 Section
1.7.3.) "The pairing $\hat\delta_!$ restricts to an alternating pairing on $M_{f^\Sigma}$, which Proposition 1.4 below shows is non-degenerate ... The image of
$\wedge^2M_{f^\Sigma}$ therefore defines an integral structure ... necessarily of the form $\eta^\Sigma_fM_\psi(1-k)$ ... We call $\eta^\Sigma_f$ the (naive, $\Sigma$-finite)
congruence ideal of $f$." So $\eta^\Sigma_{f,\lambda}$ is the **ideal of values** of $\hat\delta_!$ on $M_{f^\Sigma,\lambda}$ (the image of $\wedge^2$). (iii) $M_{f^\Sigma,\lambda}$ is saturated of rank
$2$, $G_\Q$-stable, and lies in the $\mathfrak m_{f,\lambda}$-component ($\theta$ factors through $\T_{\mathfrak m}$, so $\theta(e_{\mathfrak m})=1$, $1-e_{\mathfrak m}\in\ker\theta$ and $x=e_{\mathfrak m}x$ for $x\in M_{h,\lambda}$; Chapter 3, its 10.6); its Gram determinant is
$(\eta^\Sigma_{f,\lambda})^2$ up to a unit (Chapter 3, its 9.4(ii): a rank-two alternating form has Gram matrix $\begin{psmallmatrix}0&a\\-a&0\end{psmallmatrix}$). (iv) For $\Sigma=\emptyset$ and
$f=f_E$, $M_{f,\lambda}$ is homothetic to the **dual** $\Hom(T_\ell E,\Z_\ell)=T_\ell E(-1)$, and equal to $\varphi_E^*H^1(E,\Z_\ell)$ for the optimal curve (Chapter 14, its 9.1;
important_notes.md points 26, 40; confirmed by DFG04 (18): geometric Frobenius on $M_{f,\lambda}$ has characteristic polynomial $X^2-a_pX+p$, which is that of
$H^1$); $\ad M_{f,\lambda}=\ad T_\ell E$ (Chapter 4). Paper: Section 4.1, Section 4.2 ("$M_{f,\lambda}$ ... and $T_\ell E$ are homothetic": read "the dual of $T_\ell E$"),
Lemma lem:hecke, Theorem thm:quant Step 2.

**5.5 `ex:congruence:eta-values`** (worked example; P given Chapter 14, its 9.3, 8.5, and 5.6 here). $v_\ell(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$ for $\ell\nmid2N$ with
$E[\ell]$ irreducible: 121a1 ($\deg 6$; $v_3=1$), 539c1 ($288$; $v_3=2$), 77c1 ($6$), 11a1 ($1$); and the depleted forms of 2.2 with $\Sigma=\{7\}$: by
Theorem thm:dfg14, $v_3(\eta^{\{7\}}_{77\mathrm c,3})=v_3(\eta^\emptyset_{77\mathrm c,3})+v_3(1-7^{-2})=1+1=2$, matching $v_3(288)$ (this is Theorem thm:quant read backwards,
12.4). Paper: Lemma lem:hecke, Theorem thm:dfg14.

**5.6 `thm:congruence:lem-hecke`** (theorem, the paper's Lemma lem:hecke in the strengthened form; R here, **proved in Chapter 14, its 9.3 and
9.5**; the identification with DFG04's $\eta$ P given Part 7). Let $E$ be $X_0(N)$-optimal, $\ell\nmid2N$, $\bar\rho$ irreducible. Then
$$v_\ell(\deg\varphi_E)=v_\ell(r_E)=v_\lambda(\eta^\emptyset_{f,\lambda}),$$
with no freeness hypothesis: the first equality is ARS12 Theorem 2.2 ($\ell^2\nmid N$), the second is Chapter 14, its 9.3 (the ideal of values of $\hat\delta_!$ on
$M_{f,\lambda}=\varphi_E^*H^1(E,\Z_\ell)$ is $\deg\varphi_E\Z_\ell$), combined with 5.2(ii), 5.3(ii), 5.4(ii), which identify that ideal with DFG04's $\eta^\emptyset_{f,\lambda}$ (Part 7, items 1
to 5, all confirmed). The paper's own proof (via Lemma lem:ddt417 applied to $L=H^1(X_0(N),\Z_\ell)_{\mathfrak m}$, $d=2$) is printed as well, with the two
corrections: the other local factors of $\T_\ell$ lie in $\ker\phi_f$, not in its annihilator (point 35; 3.1(iv)); and $\hat\delta_!$ is perfect on the
$\mathfrak m$-component (point 36; 5.3(iv)). It gives the inequality $\ge$ unconditionally and equality when $L$ is free (Remark rem:free); point 39 shows the
equality holds anyway. Paper: Lemma lem:hecke, proof of Theorem thm:main, Theorem thm:quant Step 4, Remark rem:free.

**5.7 `rem:congruence:rem-free`** (remark, the paper's Remark rem:free; R, **proved in Chapter 14, its 10.2, 10.3**). For $\ell\nmid2N$ and $\mathfrak m$
non-Eisenstein, $J_0(N)[\mathfrak m]$ is two-dimensional (Mazur; RibetStein Theorem 3.5 for $J_1(N)$ and the Shimura subgroup), $\T_{\mathfrak m}$ is Gorenstein and
$H^1(X_0(N),\Z_\ell)_{\mathfrak m}\simeq\T_{\mathfrak m}^2$ (Tilouine97; Chapter 3, its 11.5). What it is still needed for after point 39 (Chapter 14, its 10.4, corrected by 12.6
here): **not** for the equality in Lemma lem:hecke or in (eq:identity); **not** for Step 4 of Theorem thm:quant; **not** for Remark (2) after Theorem
thm:quant (12.6, new); it remains the conceptual reason why the Hecke and the cohomological congruence ideals agree at $\ell\nmid2N$, and it fails
for $\ell\mid N$ in general (99a1 at $3$). Paper: Remark rem:free, Theorem thm:main ("with equality when ... free").

### Section 6. The variation of the congruence ideal with $\Sigma$: DFG04 Proposition 1.4

**6.1 `def:congruence:gamma`** (definition; P). (DFG04 Section 1.7.3.) For $m\mid M^\Sigma/M=\prod_{p\in\Sigma}p^{\delta_p}$ let $\epsilon_m\colon M(M,1)_!\to M(M^\Sigma,1)_!$ be the
degeneracy map $m^{-1}[U_0(M^\Sigma)\begin{psmallmatrix}m&0\\0&1\end{psmallmatrix}U_0(M)]$ (on forms: $h\mapsto h(mz)$ up to normalisation; in weight $2$ the factor $m^{1-k}$ is $m^{-1}$),
$\phi_m$ the endomorphism of $M(M,1)_!$ with $\phi_1=1$, $\phi_p=-T_p$, $\phi_{p^2}=p$ (weight $2$, trivial character), multiplicative in coprime $m$, and
$$\gamma=\sum_{m\mid M^\Sigma/M}\epsilon_m\phi_m\colon M(M,1)_!\to M(M^\Sigma,1)_!,$$
with adjoint $\gamma^t$ for the pairings $\hat\delta_!$ at the two levels. On $q$-expansions $\gamma(f)=\prod_{p\in\Sigma}(1-a_pV_p+pV_p^2)f$ or $(1-a_pV_p)f$, which is $f^\Sigma$ (Chapter 13,
its 7.4(ii)). Paper: background to Theorem thm:dfg14.

**6.2 `thm:congruence:dfg14`** (theorem, DFG04 Proposition 1.4, the paper's Theorem thm:dfg14; R for (b), S for (a), (c), P for the
reading). Let $f$ be a newform of weight $2$, level $M$, coefficients in $K$, $\lambda\nmid2M$, $\Sigma$ a finite set of primes not containing $\ell$. (a) $\gamma$ restricts to an
isomorphism $M_f\to M_{f^\Sigma}$ (over $K$) with $\gamma_{\mathrm{dR}}(f)=f^\Sigma$. (b) $\gamma^t\circ\gamma=\phi_{M^\Sigma/M}\prod_{p\in\Sigma}L^{\nv}_p(A_f,1)^{-1}$ on $M_f$, so $\hat\delta_!$ is non-degenerate on
$M_{f^\Sigma}$. (c) If $\bar M_{f,\lambda}$ is irreducible, $\gamma$ induces an isomorphism $M_{f,\lambda}\to M_{f^\Sigma,\lambda}$ and
$$\eta^\Sigma_{f,\lambda}=\eta^\emptyset_{f,\lambda}\prod_{p\in\Sigma}L^{\nv}_p(A_f,1)^{-1}.$$
(The quotations are from the published text, Part 7.) Here $\phi_{M^\Sigma/M}$ acts on $M_f$ by $\prod_{\delta_p=1}(-a_p)\prod_{\delta_p=2}p$, a $\lambda$-adic unit ($a_p=\pm1$ at $\delta_p=1$;
$p\ne\ell$). Proof of (c) from (b) (P): an irreducible $G_\Q$-lattice has only homothetic sublattices (Chapter 4), so $\gamma(M_{f,\lambda})=\lambda^nM_{f^\Sigma,\lambda}$, and $n=0$
because $\gamma_{\mathrm{dR}}(f)=f^\Sigma$ is primitive; then the ideal of values on $M_{f^\Sigma,\lambda}$ is $\hat\delta_!(\gamma x,\gamma y)=\hat\delta_!(x,\gamma^t\gamma y)$, i.e. $\eta^\emptyset$ times the
factor. Proof idea for (b) (S): double-coset computations as in Wiles95 Chapter 2 and DDT p. 121 (DFG04's references); in weight $2$ at a
good $p$ it is the $3\times3$ Gram matrix of $\epsilon_1,\epsilon_p,\epsilon_{p^2}$ under $\hat\delta_!$, whose determinant, divided by that at level $M$, is the level-raising factor
(Exercise 6). Reference: DFG04 Proposition 1.4 (verified, Part 7); Wiles95 Chapter 2; DDT Section 4 (cite); Ribet84 (Ihara's lemma, for the
integral statement behind (c) in Wiles's approach). Paper: Theorem thm:dfg14, proof of Theorem thm:main, Theorem thm:quant Step 3.

**6.3 `prop:congruence:three-cases`** (proposition; P given Chapter 19, its 9.7, and Chapter 15, its 7.2). The factor $L^{\nv}_p(A_f,1)^{-1}$ at $p\in\Sigma$: (i)
additive ($\delta_p=0$): $1$; level and ideal unchanged; (ii) good ($\delta_p=2$): $(1-\frac\alpha\beta p^{-1})(1-p^{-1})(1-\frac\beta\alpha p^{-1})=\frac{p-1}p\cdot\frac{(p+1)^2-a_p^2}{p^2}$, Wiles's
level-raising factor, of $\ell$-adic valuation $v_\ell(p-1)+v_\ell((p+1)^2-a_p^2)$ (identity checked symbolically, Part 6.6); (iii) multiplicative ($\delta_p=1$):
$1-p^{-2}$ (the factor $(1-p^{-1-s})^{-1}$ of DFG04 (23) at $s=1$, $\pi_p(f)$ special). Hence "only the primes with $\delta_p\ge1$ contribute". Interpretation: $v_\ell$ of
the factor counts the congruences between $f^\Sigma$ and forms new at $p$ (level raising: Chapter 15, its 7.1, 7.5). Paper: the paragraph after Theorem
thm:dfg14.

**6.4 `rem:congruence:ihara`** (remark; R). Where irreducibility enters: Ihara's lemma (Chapter 15, its 7.4; DFG04 Section 1.8.3, Lemma 1.11 in the
refined setting) says that the degeneracy maps are injective on $\mathfrak m$-parts mod $\lambda$, i.e. that $\gamma(M_{f,\lambda})$ is saturated; DFG04's proof of (c)
uses instead the homothety argument of 6.2. In the Eisenstein case the factor can change by a non-unit (Section sec:eis, Conjecture conj:eis:
outside every theorem of the paper). Paper: Theorem thm:dfg14 ("If $\bar\rho_f$ is irreducible").

**6.5 `rem:congruence:refined-structures`** (remark; R). DFG04 Section 1.8 ("Refined integral structures") modifies the level at the
exceptional primes $\Sigma_1=\{p\in\Sigma_e:p\equiv-1\bmod\lambda\}$ (for twist-minimal $f$, $\Sigma_e$ is the set of $p$ with $\delta_p=0$ and $L_p(A_f,s)\ne1$, i.e.
$M_{f,\lambda}|_{G_p}$ induced from the unramified quadratic extension), adds an auxiliary prime $r>3$ with $L_r(A_f,1)^{-1}$ a unit (which makes the
level sufficiently small with index prime to $\ell$, so that $\hat\delta^\Sigma_{!,\lambda}$ is perfect integrally: Corollary 1.6), and proves the generalisation
Proposition 1.12 ($\eta^\Sigma_{f,1}\subset\eta^\emptyset_{f,1}\prod_{p\in\Sigma}L_p(A_f,1)^{-1}$ with the **true** factors); "if $\Sigma_1\cup\{r\}\subset\Sigma$, then $\eta^\Sigma_{f,1}=\eta^\Sigma_{f,\lambda}$". This is the
mechanism by which the true Euler factors at exceptional primes enter DFG04's proof of Theorem 2.15. The paper never uses the
refined ideals; one paragraph. Paper: background (why Theorem thm:dfg37 is about the naive ideal).

### Section 7. The exceptional set and the theorems of Diamond, Flach and Guo

**7.1 `def:congruence:exceptional-set`** (definition and proposition; R for the definition as DFG04 (31), P for (ii) given Chapter 11,
its 8.6, and Chapter 18, its 10.1). (i) (DFG04 (31), verified.) $S_f$ is the set of primes $\lambda$ of $K$ such that "$\lambda\mid Nk!$, or the $(\mathcal O_K/\lambda)[G_F]$-module
$\bar M_{f,\lambda}$ is not absolutely irreducible, where $F=\Q(\sqrt{(-1)^{(\ell-1)/2}\ell})$ and $\lambda\mid\ell$". For $k=2$: $\lambda\mid2N$ or $\bar\rho|_{\Gal(\overline\Q/\Q(\sqrt{\ell^*}))}$ not absolutely
irreducible. There is **no** further condition on $\ell$ relative to the weight beyond $\lambda\nmid k!$ (Part 7, Q1). (ii) For $f=f_E$ and $\ell\nmid2N$: $\ell\notin S_f$ iff
$E[\ell]$ is irreducible and $h_\ell(E)=0$ iff $E[\ell]$ is irreducible and not ($\ell=3$ and image 3Ns) (important_notes.md point 47). (iii) $S_f$ is finite (DFG04
Lemma 2.4, with Lemma 2.5: for $\lambda\nmid N(2k-1)(2k-3)k!$, irreducible implies absolutely irreducible over $F$; for $k=2$ the extra primes are $3$; point 47
is the sharper elliptic-curve statement). Paper: Section 4.2 ("the hypothesis of Theorem thm:main is $\ell\notin S_f$"), Theorem thm:main, Section 1.2.

**7.2 `def:congruence:selmer-sigma`** (definition, recalled from Chapter 18, its 6.3, with DFG04's wording; P for the comparison). (DFG04 Section
2.1.) For a finite set $\Sigma$ of primes not containing $\ell$:
$H^1_\Sigma(\Q,W)=\ker\bigl(H^1(\Q,W)\to\bigoplus_{p\notin\Sigma\cup\{\ell,\infty\}}H^1(\Q_p,W)/H^1_{\mathrm{ur}}(\Q_p,W)\oplus H^1(\Q_\ell,W)/H^1_f(\Q_\ell,W)\bigr)$: no condition at $\Sigma\cup\{\infty\}$,
Bloch-Kato at $\ell$, **unramified** (not $H^1_f$) elsewhere ("slightly relaxed local conditions at primes $p$ where $H^1_{\mathrm{ur}}(\Q_p,W)$ is not divisible"). For
$\Sigma\supseteq\{p\mid N\}$ the two agree outside $\Sigma$ ($W$ unramified there, $W^{I_p}=W$ divisible). DFG04 define $H^1_f(\Q_\ell,W)$ for the adjoint as the extensions in
the essential image of the Fontaine-Laffaille functor ((32); their Proposition 2.2 compares it with Bloch-Kato's), which is why only
$\ell\nmid k!$ is needed (Part 7, Q1). Paper: Section 4.2 ("the group defined in DFG04 Section 2.1").

**7.3 `def:congruence:minimally-ramified`** (definition; R, DFG04 Section 3.1; P for (ii)). (i) A lift $\rho$ of $\rho_0=\bar\rho$ is *minimally ramified at
$p\ne\ell$* if: when $\ell\nmid\#\rho_0(I_p)$, $\rho(I_p)\simeq\rho_0(I_p)$; when $\ell\mid\#\rho_0(I_p)$, $\dim V_\rho^{I_p}=1$ (DFG04 Section 3.1; for deformations to $A$: $M/M^{I_p}$ free of
rank one). (ii) $M_{f,\lambda}$ is minimally ramified outside $\Sigma$ whenever $\Sigma$ contains every prime $p\ne\ell$ at which $\rho_f$ ramifies; in particular for
$\Sigma=\{p\mid N\}$, the paper's choice (P: unramified at $p$ means $\rho(I_p)=1=\rho_0(I_p)$). (iii) Remark: the paper never needs a smaller $\Sigma$; DFG04
use smaller $\Sigma$ internally (the minimal deformation problem, $\Sigma=\emptyset$, at the twist-minimal level). Paper: the paragraph after Theorem
thm:dfg37.

**7.4 `thm:congruence:dfg37`** (theorem, DFG04 Theorem 3.7, the paper's Theorem thm:dfg37; R, proof idea in Section 8). (Verified
statement.) "Let $f$ be a newform of weight $k\ge2$ and level $N$ with coefficients in the number field $K$. Suppose that $\lambda$ is a prime of $K$ not in
the set $S_f$ defined in (31) ... Suppose that $\Sigma$ is a finite set of primes not containing $\ell$ such that $M_{f,\lambda}$ is minimally ramified outside $\Sigma$.
Then the $\mathcal O_\lambda$-module $H^1_\Sigma(\Q,A_{f,\lambda}\otimes K_\lambda/\mathcal O_\lambda)$ has length $v_\lambda(\eta^\Sigma_f)$." Here $A_{f,\lambda}=\ad M_{f,\lambda}$ ($=\ad T_\ell E$ for $f=f_E$, 5.4(iv)) and
$\eta^\Sigma_f$ is the naive ideal of 5.4. Its proof in DFG04 applies the axiomatic Theorem 3.1 to the twist of minimal conductor and transfers
back ("the theorem holds for a twist of $f$, hence for $f$ itself"). Paper: Theorem thm:dfg37, proof of Theorem thm:main, Remark rem:ns, Open
question 2.

**7.5 `thm:congruence:dfg02`** (theorem, DFG04 Theorem 0.2 "(= Theorem 3.7)"; R). "Suppose $\Sigma$ is a finite set of rational primes containing those
dividing $N$. Suppose that $\lambda$ is a prime of $K$ which is not in $S_f$ and does not divide any prime in $\Sigma$. Then the $\mathcal O_{K,\lambda}$-module
$H^1_\Sigma(G_\Q,A_{f,\lambda}/\mathcal A_{f,\lambda})$ has length $v_\lambda(\eta^\Sigma_f)$." With $\Sigma=\{p\mid N\}$ and $\ell\nmid N$ this is exactly the paper's use (verified, Part 7).
DFG04's gloss: "$\eta^\Sigma_f$ ... is a generalization of the congruence ideal of Hida and Wiles; it can also be viewed as measuring the failure
of the pairing on $M_f$ to be perfect on $\mathcal M_f$." Chapter 18, its 14.5, states this as a pointer; this is its home. Paper: the sentence "this is
the form given as Theorem 0.2 there".

**7.6 `thm:congruence:dfg27`** (theorem, DFG04 Theorem 2.7, the paper's Theorem thm:dfg27; R; **stated in Chapter 18, its 10.2**, cited here).
For $\lambda\notin S_f$: $H^0(\Q,A_{f,\lambda})=H^1_f(\Q,A_{f,\lambda})=H^1_f(\Q,B_{f,\lambda})=H^0(\Q,B_{f,\lambda})=0$, with $B_f=A_f(1)$, so $V^D=B_{f,\lambda}$ (verified wording: DFG04 state it
as "Conjecture 2.6 holds for $A_f$ and $B_f$", with these vanishings as the "more precisely"). Its proof: $L(A_f,1)\ne0$ via Lemma 2.12, and
$H^1_f(\Q,A_{f,\lambda})=0$ because $H^1_f$ of the divisible module sits in the finite group of Theorem 3.7. Paper: Theorem thm:dfg27, proof of Theorem
thm:main; point 63 (only $H^1_f(\Q,V^D)=0$ is needed from it).

**7.7 `thm:congruence:dfg01`** (theorem, DFG04 Theorem 0.1 "(= Theorem 2.15)"; R; **stated in Chapter 18, its 14.4**, cited here). For $\lambda\notin S_f$
the $\lambda$-part of the Bloch-Kato conjecture holds for $A_f$ and $A_f(1)$. One paragraph on how DFG04 prove it: the proof of Theorem 2.15
takes $\Sigma=\{p\mid N\}$, uses Proposition 1.4 for $\gamma^t$, Lemma 2.1 for $H^1_\Sigma$ versus $H^1_f$, the Fontaine-Perrin-Riou local formula
$\Fitt H^1_f(\Q_p,M_\lambda)=L_p(M,0)^{-1}\Tam^0_p(M_\lambda)$ ("By [41, Proof of I.4.2.2]"), and Theorem 3.7: **the same assembly as the paper's proof of
Theorem thm:main** (Section 9), with the period computation (Theorem 2.10, Lemma 2.12) in place of the modular degree. Paper: Section
1.2 ("the hypothesis is the one under which Diamond, Flach and Guo prove the Tamagawa number conjecture for the adjoint motive of
$f$ \cite[Theorem 0.1]{DFG04}"), Theorem thm:main.

**7.8 `lem:congruence:dfg212`** (lemma, DFG04 Lemma 2.12; R; verified). For a newform of conductor $N$, weight $k$:
$\langle\tau(f),\tau(f)\rangle_{\Gamma_1(N)}=(k-1)!\,\delta(N)\,N\,\varphi(N)\,L^{\nv}(A_f,\tau,1)/(4^k\pi^{k+1})$, with $\delta(N)$ as in DFG04 (53); proved from Hida81 Theorem 5.1 (Rankin-Shimura)
by a local comparison (54). So the Petersson norm sees the **naive** adjoint value, as Chapter 19, its 8.3, proves in the book's normalisation
(unnormalised $\Gamma_0(N)$ product: $\langle f,f\rangle=N\,L^{\nv}(\ad f,1)/(8\pi^3)$; consistent with DFG04 since $[\bar\Gamma_0(N):\bar\Gamma_1(N)]=\varphi(N)/2$ for $N\ge3$). Paper: Section 1
("see DFG04 Lemma 2.12"). Chapter 19 states the formula; this item records the verification of the citation.

### Section 8. The Taylor-Wiles method in outline

**8.1 `def:congruence:deformation-ring`** (definition and theorem; R). (Mazur; DDT Chapter 2.) For $\rho_0=\bar\rho_{f,\lambda}$ absolutely irreducible and a
finite set $\Sigma$, the deformation problem "of type $\Sigma$" (DFG04 Section 3.1: minimally ramified outside $\Sigma\cup\{\ell\}$, determinant $\delta$, short crystalline
at $\ell$) is representable by a complete local Noetherian $\mathcal O$-algebra $R_\Sigma$; its reduced cotangent space at a point $\pi\colon R_\Sigma\to\mathcal O$ satisfies
$\Hom_{\mathcal O}(\wp_R/\wp_R^2,K/\mathcal O)\simeq H^1_\Sigma(\Q,\ad M_{\pi}\otimes K/\mathcal O)$ (Selmer group with the type-$\Sigma$ local conditions). Reference: DDT Sections 2.2 to 2.8
(cite the sections); Mazur's "deformation theory" survey (cite by section). Paper: background to Theorem thm:dfg37 (PLAN.md: "the
Selmer group as the tangent space / dual of the cotangent space").

**8.2 `def:congruence:hecke-side`** (definition and proposition; R for the existence of the modular point, S for the rest). $\T_\Sigma=\T(N^\Sigma)_{\mathfrak m}$
(the Hecke algebra acting on $L_\Sigma=M(\sigma^\Sigma)_{!,\lambda,\mathfrak m}$, DFG04 Section 3.2), with the modular deformation $R_\Sigma\to\T_\Sigma$ (surjective: $\T_\Sigma$ is generated by
traces of Frobenius); $\pi$ the point of $f$; $\eta(\T_\Sigma,\pi)$ compared with $\eta^\Sigma_f$ by Lemma lem:ddt417 and multiplicity one ($L_\Sigma$ free over $\T_\Sigma$,
DFG04 Lemma 3.2 to 3.4 and Lemma 1.10). Paper: background.

**8.3 `thm:congruence:tw-axiomatic`** (theorem, DFG04 Theorem 3.1; R, with the idea S). For $\rho_0$ odd, absolutely irreducible over $G_F$ ($F$ the
quadratic subfield of $\Q(\mu_\ell)$), of minimal conductor among its twists, with Serre weight $2\le k\le\ell-1$; given a set $\mathcal N$ of allowable (short crystalline)
lifts, a trellis $L$ and a system of perfect pairings $\varphi$ satisfying the level-raising compatibility $\varphi^\Sigma_\rho=\varphi^\emptyset_\rho\beta^\Sigma_\rho\prod_{p\in\Sigma}L_p(\ad,1)^{-1}$ and
the Taylor-Wiles conditions at horizontal primes ($q\equiv1\bmod\ell$, $\rho_0$ unramified at $q$ with distinct Frobenius eigenvalues): every allowable lift is
modular, and $\len H^1_\Sigma(\Q,A_\rho)=\len\mathcal O(\delta)/\varphi^\Sigma_\rho(\wedge^2L_\rho)$ for $\Sigma\supseteq\Sigma_\rho$. Idea: patching over sets $Q_n$ of horizontal primes gives
$R_\emptyset\simeq\T_\emptyset$, a complete intersection (4.1(iii)); then the numerical criterion and Wiles's comparison of $\Phi_{R_\Sigma}$ and $\eta^\Sigma$ under change of
$\Sigma$ (both change by the same local factors: the Selmer side by Chapter 17's comparison, the Hecke side by Proposition 1.4) give the
equality at every $\Sigma$. Reference: DFG04 Theorem 3.1 and Section 3 (verified statement); Wiles95; TaylorWiles; DDT Chapters 3 to 5;
Diamond96 (proposed key). Paper: background to Theorem thm:dfg37.

**8.4 `rem:congruence:where-hypothesis`** (remark; P). Where each hypothesis of $\ell\notin S_f$ is used: $\ell\nmid N$ (the representation is
crystalline at $\ell$, Fontaine-Laffaille applies, the level structure is prime to $\ell$); $\ell\nmid k!=2$ (Fontaine-Laffaille needs the Hodge-Tate weights
$0,1$ in $[0,\ell-2]$); absolute irreducibility over $\Q(\sqrt{\ell^*})$ (existence of horizontal primes making the dual Selmer group vanish: the
Chebotarev argument needs an element $g$ of $\Gal(\overline\Q/\Q(\mu_{\ell^n}))$ with $\bar\rho(g)$ having distinct eigenvalues, which fails exactly when $\bar\rho$ is induced from
$\Q(\sqrt{\ell^*})$). For elliptic curves with $\ell\nmid2N$ the last condition bites only for $\ell=3$, image 3Ns (point 47). Paper: Section 1.5 ("by level
lowering and twisting rather than by the Taylor-Wiles method"), Section sec:anomaly, Open question 2.

**8.5 `rem:congruence:why-length-equals-eta`** (remark; S). The slogan "length of the Selmer group equals the valuation of the congruence
ideal" in three lines: $H^1_\Sigma(\Q,W)^*\simeq\Phi_{R_\Sigma}=\wp_R/\wp_R^2$ (8.1); $R_\Sigma=\T_\Sigma$ is a complete intersection (8.3), so $\len\Phi_{\T_\Sigma}=v(\eta(\T_\Sigma))$ (4.1(ii)); and
$L_\Sigma$ is free over $\T_\Sigma$, so $\eta(\T_\Sigma)=\eta^\Sigma_f$ (4.3, equality case). Paper: Theorem thm:dfg37 (the reader's question "why should a Selmer group
know about congruences?").

### Section 9. The assembly: proof of Theorem thm:main

**9.1 `thm:congruence:main`** (theorem, the paper's Theorem thm:main in the strengthened form; P as an assembly of cited items). Let $E$ be
$X_0(N)$-optimal, $f=f_E$, $\ell$ an odd prime with $\ell\nmid2N$ and $\ell\notin S_f$ (equivalently, by 7.1(ii), $E[\ell]$ irreducible and not ($\ell=3$ and image 3Ns)), $T=T_\ell E$,
$W=\ad T\otimes\Q_\ell/\Z_\ell$. Then
$$v_\ell(\deg\varphi_E)=\len_{\Z_\ell}H^1_f(\Q,W)+\sum_{q\mid N}v_\ell\bigl(\Tam_q(\ad T)\bigr)+\sum_{q\mid N}e_\ell(E,q)\qquad\text{(eq:identity), with equality},$$
and consequently $v_\ell(\deg\varphi_E)\ge\sum_qe_\ell(E,q)+\sum_qt_\ell(E,q)$ (eq:thm). The Tamagawa terms are explicit (Chapter 18, its 8.2, 8.4, 9.3: $0$ at good and
potentially good primes, $t_\ell+\min(t_\ell,v_\ell(q-1),v_\ell(c(u)))$ at potentially multiplicative primes, $q=2$ included), so (eq:identity) reads
$\len H^1_f(\Q,W)=v_\ell(\deg\varphi_E)-B^{\mathrm{expl}}_\ell(E)$ (Chapter 18, its 9.4). The equality (rather than the paper's "$\ge$, with equality when ... free") is
important_notes.md points 39 and 56, with the DFG04 checklist confirmed (Part 7). Paper: Theorem thm:main, (eq:identity), (eq:thm).

**9.2 `sec:congruence:assembly`** (the proof of 9.1, a subsection whose `proof` environment has numbered steps, each naming its input
and the hypothesis it uses; P). $\Sigma=\{q\mid N\}$ (nonempty as $N>1$).
Step 1 (degree to congruence ideal; uses optimality and $\ell\nmid2N$, $\bar\rho$ irreducible): $v_\ell(\deg\varphi_E)=v_\lambda(\eta^\emptyset_{f,\lambda})$ (5.6 = Chapter 14, its 9.3, 9.5,
with Part 7). The paper's version ($\ge$ via Lemma lem:ddt417, equality under freeness) is printed in a `paperlink`.
Step 2 (vary $\Sigma$; uses $\bar\rho$ irreducible, $\ell\nmid2N$): $v(\eta^\emptyset)=v(\eta^\Sigma)-\sum_{q\in\Sigma}v_\ell(L^{\nv}_q(A_f,1)^{-1})$ (6.2(c)); only the multiplicative primes
contribute, each $v_\ell(1-q^{-2})=v_\ell(q^2-1)$ (6.3; Chapter 19, its 9.7).
Step 3 (Taylor-Wiles; uses $\ell\notin S_f$): $v(\eta^\Sigma)=\len H^1_\Sigma(\Q,W)$ (7.4; $M_{f,\lambda}$ is minimally ramified outside $\Sigma$, 7.3(ii); $\ad M_{f,\lambda}=\ad T$, 5.4(iv)).
Step 4 (the Selmer half; uses $\ell\notin S_f$ through thm:dfg27, $\ell$ odd, Lemma lem:h0): $\len H^1_\Sigma(\Q,W)=\len H^1_f(\Q,W)+\sum_{q\in\Sigma}\bigl(v_\ell(L_q(A_f,1)^{-1})+v_\ell(\Tam_q(\ad T))\bigr)$ (**Chapter 18, its 11.1**, which packages Lemma lem:dfg21 (its 10.4, from Chapter 17, its 10.3), Lemma
lem:fpr (its 7.4, 7.5), Lemma lem:h0 (its 10.3: $h_\ell(E)=0$), thm:dfg27 (its 10.2)). Only $H^1_f(\Q,V^D)=0$ is needed from thm:dfg27; $H^0(\Q,V^D)=0$ is automatic
(point 63; Chapter 17, its 10.3(b)).
Step 5 (cancellation; Definition def:terms): Steps 1 to 4 give (eq:identity) with the Euler sum $\sum_q\bigl(v_\ell(L_q^{-1})-v_\ell((L^{\nv}_q)^{-1})\bigr)=\sum_qe_\ell(E,q)$:
at a multiplicative $q$ true and naive factors coincide, at an additive $q$ the naive factor is $1$ (Chapter 19, its 9.7). Good primes do not divide $N$.
Step 6 ((eq:thm)): drop $\len H^1_f\ge0$; $v_\ell(\Tam_q(\ad T))\ge t_\ell(E,q)$ at every potentially multiplicative $q$, **including an $\mathrm I_n^*$ prime at $q=2$**
(important_notes.md point 18: the paper's appeal to "$E_{\{p\}}$ of Lemma lem:twist" covers only odd $p$; the local argument of Chapter 18, its 8.4,
covers every $q\ne\ell$, using $n=-v_q(j)$, not the index of the Kodaira symbol); $v_\ell(\Tam_q(\ad T))=0$ at good and potentially good primes (point 64,
Chapter 18, its 9.3).
`paperlink`: the paper's proof of Theorem thm:main, sentence by sentence, with the step that justifies it. Paper: Section 4.3.

**9.3 `rem:congruence:hypothesis-table`** (remark; P). Table "input $\to$ hypothesis used $\to$ what fails without it": optimality (Step 1:
for a non-optimal curve the pullback lattice has index $\deg\psi$ in its saturation; harmless for $v_\ell$ when $E[\ell]$ is irreducible, point 27);
$\ell\nmid N$ (Steps 1, 3, 5: ARS, Fontaine-Laffaille, $q\ne\ell$ in Lemma lem:fpr); $\ell$ odd (Step 4 at $\infty$; $\ad$ self-dual via the trace form); $\bar\rho$
irreducible (Steps 1, 2: non-Eisenstein $\mathfrak m$, homothety); absolute irreducibility over $\Q(\sqrt{\ell^*})$ (Steps 3, 4: Taylor-Wiles and $h_\ell=0$); multiplicity one
(no longer needed, 5.7). Paper: Theorem thm:main; Chapter 21's hypothesis table (B2 there) should be aligned with this one.

**9.4 `ex:congruence:main-examples`** (worked examples; P, data from Chapter 18, its 11.3, and Part 6.6). At $\ell=3$: 121a1 ($\mathrm{II}$ at $11$,
$e_3=1$, $\deg 6$): $H^1_f(\Q,W)=0$; 791a1: Tamagawa excess needed for equality; 1184f1 and 1748e1: Selmer length $1$. Each line: $\ell\nmid N$, $E[3]$ irreducible,
image not 3Ns, so $3\notin S_f$ and the identity is a theorem; the Selmer lengths are therefore **computed**, not conjectured. Paper: Theorem thm:main,
Section sec:sharp ("the identity says what the excess is").

### Section 10. Remark rem:ko: Tamagawa excess and the formula of Kim and Ota

**10.1 `rem:congruence:rem-ko-1`** (remark, Remark rem:ko(1); P given 9.1 and Chapter 18, its 8.3). At a multiplicative prime $q\equiv1\pmod\ell$ with $\ell\mid n_q$
and unit part $u$ of the Tate parameter an $\ell$-th power in $\F_q^\times$, $v_\ell(\Tam_q(\ad T))\ge t_\ell(E,q)+1$; precisely the excess is $\min(v_\ell(n),v_\ell(q-1),v_\ell(c(u)))$
(points 23, 65: "by at least one", and the class is $c(u)$, not $c_q$). By 9.1 this raises the bound exactly by that amount for $\ell\notin S_f$, also at
potentially multiplicative additive primes (point 68). Paper: Remark rem:ko(1), Section sec:tam, the abstract.

**10.2 `thm:congruence:kim-ota`** (theorem, Remark rem:ko(2); R, **stated in Chapter 15, its 11.4**; the consequence P). (KimOta Theorem 1.1, as
cited; their Definition 2.12 for the Tamagawa exponent.) For $N=N^+N^-$ with $N^-$ square-free, $\ell\ge5$, $\ell\nmid N$, $\ell\notin S_f$, and $\bar\rho$ ramified at every $q\mid N^-$
with $q\equiv\pm1\pmod\ell$: $\ord_\lambda\eta_f(N)=\ord_\lambda\eta_f(N^+,N^-)+\sum_{q\mid N^-}t_f(q)$. Consequence: $v_\ell(r_E)\ge\sum_{q\mid N^-}t_\ell(E,q)$, contained in (eq:thm) without $\ell\ge5$ and
$q\not\equiv\pm1$. What this chapter adds: (i) Kim-Ota's $\eta_f(N)$ must be checked to be the Hecke congruence ideal of 3.3 (then $=r_E\Z_\ell$ by 3.4)
and not a cohomological one (if cohomological, 5.6 gives the same value at $\ell\nmid N$ anyway); (ii) with 9.1 the comparison reads: their equality
plus (eq:identity) for $E$ give $\ord_\lambda\eta_f(N^+,N^-)=\len H^1_f(\Q,W)+\sum_{q\mid N^-}\min(\dots)+\sum_{q\mid N^+}(\dots)$, a Selmer-theoretic reading of the
$N^-$-new congruence ideal (S, one paragraph, clearly marked as a consequence of both theorems). Reference: KimOta; PollackWeston11;
RibetTakahashi97 (Chapter 14, its 12.2). Paper: Remark rem:ko(2), Section 1.5.

### Section 11. Twist monotonicity: Theorem thm:twist

**11.1 `prop:congruence:twist-inputs`** (proposition, recollection; P by citation). From Chapter 13, its 9.1, 9.3, and Chapter 15, its 10.1, 10.2:
$\iota=\iota_S$ maps $S_2(\Gamma_0(M))$ into $S_2(\Gamma_0(\operatorname{lcm}(M,D^2)))$, preserves integrality, intertwines $T_p$ with $\chi_S(p)T_p$ for $p\nmid DM$, kills the $q$-coefficients
at multiples of $D$ ($\iota(h)=\iota(h^S)$), and maps the sum of the generalised eigenspaces of systems different from that of $g$ into the sum of
those different from the twisted system; $(h\otimes\chi)\otimes\chi=h^{\{q\}}$ (point 20). Levels (Chapter 15, its 10.2): type $\mathrm I_n^*$ at all $q\in S$: $N_S=N/D$; type
$\mathrm I_0^*$: $N_S=N/D^2$; types $\mathrm{II},\mathrm{III},\mathrm{IV}$ or duals at $q\ge5$: $N_S=N$. Paper: Theorem thm:twist (its proof), the sentence after it.

**11.2 `thm:congruence:twist`** (theorem, the paper's Theorem thm:twist; **P**, every step). Let $E/\Q$ have conductor $N$, $S$ a set of odd primes, $D$, $\chi_S$,
$E_S$, $N_S$ as in C7. If $q^2\mid N$ for every $q\in S$ and $\operatorname{lcm}(N_S,D^2)\mid N$, then $r_{E_S}\mid r_E$; if moreover $\operatorname{lcm}(N,D^2)\mid N_S$, then $r_{E_S}=r_E$.
Proof (the paper's, expanded): (1) $\iota(g)=f$ for $g=f_{E_S}$: both multiplicative; $a_p(f)=\chi_S(p)a_p(g)$ for $p\nmid D$ (at $p\mid N$, $p\notin S$, the twist is unramified at $p$,
Chapter 9, its 10.4); $a_{q^k}(f)=0$ for $q\in S$ since $q^2\mid N$ (Chapter 13, its 6.4(iii)). (2) $g^\perp$ (Petersson complement at level $N_S$, where $g$ is new,
so it equals the $\T$-stable complement, Chapter 13, its 8.2(ii)) is the sum of the generalised eigenspaces of the other systems, each differing
from $g$'s at infinitely many $p$ (strong multiplicity one, Chapter 13, its 6.3); $\iota$ sends such a space into the generalised eigenspace of the
twisted system, which differs from $f$'s at infinitely many $p$, hence lies in $f^\perp$ (Chapter 13, its 6.3(iii)). (3) A congruence $g\equiv h\pmod r$ with
$h\in g^\perp$ integral gives $f\equiv\iota(h)\pmod r$ with $\iota(h)\in f^\perp$ integral (Chapter 13, its 9.1(iii)), so $r\mid r_E$ by the definition of $r_E$ (no need for
Lemma lem:crit here). (4) Under the second hypothesis $E=(E_S)_S$ and the roles exchange. Paper: Theorem thm:twist.

**11.3 `ex:congruence:twist-cases`** (worked examples and data; P, Part 6.6). The paper's cases: (a) $\mathrm I_n^*$: 539c1/77c1, 980i1/140b1, 121d1/11a1;
(b) $\mathrm I_0^*$: 539d1/11a1; (c) potentially good: 121a1/121c1 ($r=6=6$). Data check of case (c) (Part 6.6): for all $14{,}876$ pairs ($E$ optimal non-CM
with at least one prime $q\ge5$ of type $\mathrm{II},\mathrm{III},\mathrm{IV}$ or a dual, $S$ the set of such primes, $\ell\in\{3,5,7,11,13\}$, $\ell\nmid N$, $E[\ell]$ irreducible) below conductor $10{,}000$,
$v_\ell(\deg\varphi_E)=v_\ell(\deg\varphi_{E_S})$, as the theorem predicts. **Correction of the paper's data sentence** (important_notes.md point 16): strict inequality
occurs in case (a) as well as case (b), the difference being exactly the Euler term of Theorem thm:quant (12.6: $25{,}477$ pairs, equality in every
one). Paper: the paragraph after the proof of Theorem thm:twist.

### Section 12. Theorem thm:quant

**12.1 `thm:congruence:quant`** (theorem, the paper's Theorem thm:quant, with the extension to $q=3$; **P** given 6.2 (R) and Chapter 14 (R
inputs)). Let $\ell$ be odd, $\ell\nmid2N$, $E[\ell]$ irreducible; let $S$ be the set of **odd** primes $q$ at which $E$ has type $\mathrm I_0^*$ or $\mathrm I_n^*$ (the paper: $q\ge5$; the
extension to $q=3$ is important_notes.md point 60, P here, as $\ell\ne3$ is then automatic and the twist lemma for these exchanges holds at every
odd $q$); $E_S=E\otimes\chi_S$. Then $v_\ell(\deg\varphi_E)\ge v_\ell(r_{E_S})+\sum_{q\in S}e_\ell(E,q)\ge\sum_{q\in S}e_\ell(E,q)$. Paper: Theorem thm:quant.

**12.2 `sec:congruence:quant-setup`** (the set-up of the proof; P). By Lemma lem:twist ($q$ odd; Chapter 10), $E_S$ is good at the $\mathrm I_0^*$ primes ($\delta_q(g)=2$)
and multiplicative at the $\mathrm I_n^*$ primes ($\delta_q(g)=1$), so $N_S^S=N_S\prod_{q\in S}q^{\delta_q(g)}=N$ (Chapter 15, its 10.2(iii)): the depleted form $g^S$ lives at level $N$ and
$\iota(g^S)=\iota(g)=f$. The eigencharacter $\pi$ of $g^S$ on $\T_N$ has generalised eigenspace $\C g^S$ (Chapter 13, its 7.4(iv)), so 3.5 applies to it. Paper:
proof of Theorem thm:quant, first paragraph.

**12.3 `lem:congruence:quant-step1`** (lemma, Step 1, in the sharpened form; P). $v_\ell(r_E)=v_\ell(\eta^{\mathrm{Hecke}}(g^S))$ (the paper proves $\ge$). Proof of $\ge$ (the
paper's): $\mathfrak m\ni U_q$ ($q\in S$); every $U_q$-eigenvalue on $S_2(\Gamma_0(N))$ is $0$, $\pm1$ or a root of $X^2-aX+q$, so $0$ or an $\ell$-adic unit (Chapter 13, its 7.2); hence the
$\mathfrak m$-component is $\C g^S$ plus generalised eigenspaces of systems with $U_q=0$ from newforms $h\ne g$ (Chapter 13, its 7.1, 8.1); by 3.5 over $\Z_\ell$,
$\ell^{v(\eta^{\mathrm{Hecke}}(g^S))}$ is the largest $\ell^t$ with $g^S\equiv h\pmod{\ell^t}$, $h$ integral in the $\T$-stable complement (point 61); project by $e_{\mathfrak m}$ (Chapter 13, its 8.3(iv));
apply $\iota$, which lands in $f^\perp$ (11.1). Proof of $\le$ (point 59, Chapter 13, its 9.3(iii)): $\iota(f)=g^S$ and $\iota(f^\perp)$ lies in the $\T$-stable complement of
$\C g^S$, so a congruence for $f$ gives one for $g^S$ of the same modulus. Check: level $539$, orders $288$ and $504$ (2.2). Paper: Step 1, Remark
(2) after the proof.

**12.4 `lem:congruence:quant-steps234`** (lemma, Steps 2 to 4; P given 4.3, 6.2 (R), 5.6). Step 2: Lemma lem:ddt417 with $L=H^1(X_0(N),\Z_\ell)_{\mathfrak m}$,
$\hat\delta_!$ perfect on the $\mathfrak m$-part (5.3(iv), point 36), $L[\wp]=M_{g^S,\lambda}$ of rank $2$, Gram determinant $(\eta^S_{g,\lambda})^2$: $v(\eta^{\mathrm{Hecke}}(g^S))\ge v(\eta^S_{g,\lambda})$ (no freeness).
Step 3: 6.2(c) for $g$ ($\bar\rho_g=\bar\rho\otimes\chi_S$ irreducible, $\ell\nmid2N_S$): $v(\eta^S_g)=v(\eta^\emptyset_g)+\sum_{q\in S}v_\ell(L^{\nv}_q(A_g,1)^{-1})=v(\eta^\emptyset_g)+\sum_{q\in S}e_\ell(E,q)$, because
$A_g=A_f$ (Chapter 19, its 9.5(i)), $\delta_q(g)\ge1$ (so its naive factor is the true one), and the true factor of $A_f$ at $q$ is the one $f$ omits (Chapter 19,
its 9.7). At $q=3$ the values are the twist formulas $L_3(A_f,1)^{-1}=\frac23\cdot\frac{16-a_3(E')^2}9$ ($\mathrm I_0^*$) and $\frac89$ ($\mathrm I_n^*$), checked against PARI (point 60, Part 6.6).
Step 4: $v(\eta^\emptyset_g)=v_\ell(\deg\varphi_{E_S^{\mathrm{opt}}})=v_\ell(r_{E_S})$ by 5.6 for the optimal curve of the class of $E_S$ (point 39: **no freeness**, which removes
point 24's worry about Step 4; $v_\ell$ is a class invariant as $E_S[\ell]$ is irreducible, Chapter 14, its 6.4). Paper: Steps 2 to 4.

**12.5 `rem:congruence:outer-inequality`** (remark; P). The outer inequality $v_\ell(\deg\varphi_E)\ge\sum_{q\in S}e_\ell(E,q)$ needs only Steps 1 to 3 and the integrality of
$\eta^\emptyset_g$; neither multiplicity one nor ARS at level $N_S$. Still not "elementary" (point 24): Step 3 is DFG04 Proposition 1.4 and Step 2 is Lemma
lem:ddt417. The abstract's wording should be "by a twisting argument combined with the formula of Diamond, Flach and Guo". Paper:
the abstract, Section 1.5.

**12.6 `thm:congruence:quant-equality`** (theorem, the remark after Theorem thm:quant, (2), in the strengthened form; P given 9.1; **new**,
Part 8, N2). If $\ell\notin S_f$, then
$$v_\ell(\deg\varphi_E)=v_\ell(r_{E_S})+\sum_{q\in S}e_\ell(E,q),$$
and every inequality in the chain of 12.3 and 12.4 is an equality (in particular $v(\eta^{\mathrm{Hecke}}(g^S))=v(\eta^S_{g,\lambda})$ at level $N$, a freeness-type statement for
the depleted form obtained without multiplicity one). Proof: apply 9.1 (equality) to $E$ and to the optimal curve in the class of $E_S$ ($\ell\notin S_{f_{E_S}}$:
twisting does not change absolute irreducibility over $\Q(\sqrt{\ell^*})$, and $N_S\mid N$); the Selmer groups coincide ($\ad T$ is twist-invariant), so do the
Tamagawa factors (local, $\ad T$ unchanged); the Euler sums differ exactly by $\sum_{q\in S}e_\ell(E,q)$ (at $q\notin S$ the twist is unramified, same type and $e_\ell$; at
$q\in S$, $E_S$ is good or multiplicative, contributing $0$). Hence $v_\ell(\deg\varphi_E)-v_\ell(\deg\varphi_{E_S})=\sum_{q\in S}e_\ell(E,q)$, and with $v_\ell(\deg\varphi_{E_S})=v_\ell(r_{E_S})$ ($\ell^2\nmid N_S$) the
chain $v_\ell(r_E)\ge v(\eta^{\mathrm{Hecke}}(g^S))\ge v(\eta^S_g)=v_\ell(r_{E_S})+\sum e_\ell=v_\ell(r_E)$ closes. The paper's Remark (2) asks for multiplicity one at level $N$; point
56 (and Chapter 14, its 9.5(c), 10.4(b)) say it is still needed; **it is not**. Data (Part 6.6): equality in all $25{,}477$ pairs (optimal non-CM curves of
conductor below $10{,}000$ with $S\ne\emptyset$, $q=3$ included, $\ell\in\{3,5,7,11,13\}$, $\ell\nmid N$, $E[\ell]$ irreducible), including the $8$ pairs at $\ell=3$ with image 3Ns, which lie
outside the theorem. Examples: 539c1 ($2=1+1$), 980i1 ($2=1+1$), 121d1 ($1=0+1$), 539d1 ($2=0+2$). Paper: the remark after Theorem thm:quant, (2).

**12.7 `rem:congruence:after-quant`** (remark, the remark after Theorem thm:quant, (1) and (3); P). (1) Theorem thm:quant is level raising: from $N_S$ to
$N_S^S=N$, at the price of the level-raising Euler factors (Chapter 15, its 10.4). For $\ell=3$ a single $\mathrm I_n^*$ prime $q\ge5$ forces $3\mid\deg\varphi_E$ ($3\mid q^2-1$),
as does an $\mathrm I_0^*$ prime with $q\equiv1\pmod3$; neither needs absolute irreducibility over $\Q(\sqrt{-3})$. (3) For the potentially good types $N_S=N$, $f$ is its
own depletion, and Theorem thm:dfg14 gives no factor; the omitted factor is reached only through Theorem thm:dfg37, i.e. with $\ell\notin S_f$, and
Section sec:anomaly shows the hypothesis cannot be dropped (3Ns curves fail through a type $\mathrm{III}$ term). Paper: the remark after
Theorem thm:quant.

### Section 13. Beyond the hypothesis: Remark rem:ns and Open questions 1 and 2

**13.1 `rem:congruence:rem-ns`** (remark, Remark rem:ns; P for the conditional statement given Chapter 18, its 12.1). For $\ell=3$ and image
$N_s(\F_3)$, $3\nmid N$: Theorem thm:dfg37 does not apply ($3\in S_f$); Lemma lem:dfg21 applies **provided** $H^1_f(\Q,V^D)=0$ (equivalently $H^1_f(\Q,\ad V_3E)=0$), which DFG04
Theorem 2.7 does not supply here (point 67); then $\len H^1_\Sigma=\len H^1_f+\sum_p(\dots)-h_3(E)$ with $h_3(E)=1$ (Chapter 11, its 8.5; point 5). If, in addition,
$v(\eta^\Sigma)=\len H^1_\Sigma$ held, the assembly 9.2 would give (eq:identity) with $-h_3(E)$, the shape of Conjecture conj:euler. Paper: Remark rem:ns,
Section 1.3, Section sec:anomaly.

**13.2 `rem:congruence:open-question-2`** (remark, Open question 2; P for the analysis). What is missing for 3Ns curves: (a) on the
Hecke side, the identity $v(\eta^\Sigma_{f,\lambda})=\len H^1_\Sigma(\Q,W)$ needs Taylor-Wiles for $\bar\rho$ induced from $\Q(\sqrt{-3})$, where horizontal primes fail to kill the
dual Selmer group (8.4); (b) on the Selmer side, $H^1_f(\Q,\ad V_3E)=0$. The data (failures of (eq:thm) by exactly $1$, never more) and the
equality of 12.6 at the $8$ 3Ns pairs are consistent with the corrected identity. The book records that later work on residually
dihedral representations may settle (b) and (a); it cites nothing it has not checked. Paper: Open question 2.

**13.3 `rem:congruence:open-question-1`** (remark, Open question 1; P for the analysis). At $\ell\mid N$: Step 1 fails ($r_E\ne\deg\varphi_E$ possible at $\ell^2\mid N$:
99a1, 726a1, 539d1; Chapter 14, its 8.5), Step 3 fails ($\lambda\mid N$ puts $\ell$ in $S_f$; DFG04's integral structures and Fontaine-Laffaille at $\ell$ need $\ell\nmid N$), and
the Euler factor at $q=\ell$ is not the relevant local quantity (Remark rem:wild). What would replace it: a local condition at $\ell$ (finite flat,
ordinary, or semistable deformation conditions), with the empirical weights $w_3$ as the target. One paragraph. Paper: Open question 1,
Conjecture conj:euler.

### Section 14. The imported statements, verified against DFG04

**14.1 `rem:congruence:imported-table`** (remark with table; P for the verification record). A `booktabs` table: each DFG04 statement the
paper cites (Theorems 0.1, 0.2, 2.7, 2.15, 3.7; Proposition 1.4; Lemmas 2.1, 2.12; (13), (14), (31), (57); p. 708; Sections 1.5.3, 1.6.1, 1.6.2, 1.7.2,
1.7.3, 1.8.2, 2.1), what it says (quoted in the book's notation), where the paper uses it, and the status "verified against the published text"
(Part 7 here gives the record). Also the two differences of wording the reader should know: DFG04 Lemma 2.1 asks that $\Sigma$ contain every prime
where $H^1_f(\Q_p,W)\ne H^1_{\mathrm{ur}}(\Q_p,W)$ (the paper's "every $p\ne\ell$ at which $W$ is ramified" implies it); DFG04's $H^1_\Sigma$ uses $H^1_{\mathrm{ur}}$, not $H^1_f$, outside
$\Sigma\cup\{\ell\}$ (the same for $\Sigma\supseteq\{p\mid N\}$). And the warning that the arXiv version (2025) is a longer text with **different numbering** (its Sections
1.1 to 3.5 do not match the published 1.1 to 3.2); the book cites the published version. Paper: every citation of DFG04.

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: this chapter may run to 2,800). The card lists the 59 items of Part 2
(numbered 20.1 to 20.59 in the book; conventions in one line each), about 230 lines, not counted. Every section opens with one paragraph
saying what it is for and where in the paper it is used.

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2 with its tag and `\Cref`; the identity of 9.1 and the chain of 12.6 displayed | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1 (Hida, DFG04, congruence ideal, Lemma 2.12); Lemma lem:crit (restated, 3.4); Section 4.1 (5.1 to 5.4, 6.2); Lemma lem:ddt417 (4.3); Lemma lem:hecke (5.6); Remark rem:free (5.7); Section 4.2 (7.1 to 7.7); thm:dfg37, thm:dfg27, lem:dfg21, lem:fpr, lem:h0 (cited items); proof of thm:main (9.2); Remark rem:ko (10.1, 10.2); thm:twist (11.2); thm:quant and the remark after it (12.1 to 12.7); Remark rem:ns (13.1); Open questions 1, 2 (13.2, 13.3) | 50 |
| 1 | Overview and conventions | 1.1; C1 to C8 as `convention` environments; the roadmap table; `warning` boxes for C3 and C4 | 90 |
| 2 | Hecke algebras over $\Z_\ell$ | 2.1, 2.2 (recollection with citations; the level-539 example) | 110 |
| 3 | Congruence modules and congruence ideals | 3.1 to 3.7; the module-theoretic reading of Lemma lem:crit; the $\T$-stable complement; Hida; physics aside on the "overlap" | 210 |
| 4 | Wiles's numerical criterion and Lemma lem:ddt417 | 4.1 to 4.4; the criterion with the toy examples; the full proof of Lemma lem:ddt417 with steps (0) to (6); `paperlink`: the paper's proof sentence by sentence (points 19, 38) | 260 |
| 5 | The DFG04 lattices; Lemma lem:hecke; Remark rem:free | 5.1 to 5.7; quotations from DFG04 Sections 1.4 to 1.7; the comparison with $H^1(X_0(M),\Z_\ell)$; `paperlink`: Section 4.1 and Lemma lem:hecke with points 35, 36, 39 | 240 |
| 6 | DFG04 Proposition 1.4 | 6.1 to 6.5; $\gamma$, $\gamma^t\gamma$; the three cases; the level-raising factor; Ihara; refined structures in one paragraph | 190 |
| 7 | $S_f$ and the theorems of DFG04 | 7.1 to 7.8; quotations of (31), Theorems 0.1, 0.2, 2.7, 3.7, Lemma 2.12; minimally ramified | 180 |
| 8 | Taylor-Wiles in outline | 8.1 to 8.5; deformation rings, tangent spaces, horizontal primes, patching in words, DFG04 Theorem 3.1; where each hypothesis is used | 200 |
| 9 | The assembly of Theorem thm:main | 9.1 to 9.4; the six-step proof; the hypothesis table; the examples; `paperlink`: Section 4.3 sentence by sentence (point 18) | 230 |
| 10 | Remark rem:ko | 10.1, 10.2 | 80 |
| 11 | Theorem thm:twist | 11.1 to 11.3; full proof; the data paragraph corrected (point 16) | 140 |
| 12 | Theorem thm:quant | 12.1 to 12.7; Steps 1 to 4; the sharpened Step 1 (point 59); $q=3$ (point 60); the equality theorem 12.6 with the data; the remark after the theorem | 290 |
| 13 | Beyond the hypothesis | 13.1 to 13.3; Remark rem:ns (point 67); Open questions 1, 2 | 110 |
| 14 | The imported statements | 14.1, the verification table | 70 |
| 15 | Exercises | the 16 exercises of Part 4.2 | 160 |
| 16 | Notes and references | DFG04 (published versus arXiv numbering), Hida81, Wiles95, TaylorWiles, Lenstra95, Diamond96, DDT, FPR94, KimOta, PollackWeston11, ARS12, Tilouine97, RibetStein, Ribet84, DiamondTaylor94; which numbers were verified | 60 |
| | **total** | | **2,670** |

________________________________________________________________________________

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| Hecke algebras as finite flat $\Z$-algebras; $\T_{\mathfrak m}$; $\mathfrak m$ attached to $(f,\ell)$; $\T\otimes\Z_\ell=\prod\T_{\mathfrak m}$ | 2.1 (citing Chapters 3, 13) |
| the $\mathfrak m$-component of $S_2(\Gamma_0(N);\Z_\ell)$ via idempotents; which newforms belong to $\mathfrak m$ ($\bar\rho_g\simeq\bar\rho_f$) | 2.1(iii), 2.2 |
| congruence modules and ideals: $\eta=\pi(\Ann\wp)$, $\mathcal O/\eta=\T/(\wp+I)$ | 3.1, 3.2, 3.3 |
| Hida's definition and "largest modulus of a congruence with $f^\perp$"; Lemma lem:crit restated (proof in Chapter 15) | 3.4, 3.5, 3.6 |
| Hida's theorem on congruence modules and the adjoint $L$-value | 3.6, 7.8 |
| Wiles's numerical criterion (statement) | 4.1, 3.2 |
| Lemma lem:ddt417 in full, in the paper's generality, every ingredient from Chapter 3 | 4.3, 4.4 |
| Lemma lem:hecke (proof in full) and Remark rem:free | 5.6 (proved in Chapter 14, its 9.3, 9.5, cited per B19), 5.7 |
| DFG04 Sections 1.5.3, 1.6.2, 1.7.3: integral structure, $M_{f^\Sigma,\lambda}$, $\hat\delta_!$, $\eta^\Sigma$; Gram determinant a square | 5.1 to 5.5 |
| DFG04 Proposition 1.4(c), the three cases, proof idea | 6.1 to 6.5 |
| the exceptional set $S_f$, DFG04 (31) | 7.1 |
| DFG04 Theorem 3.7, "minimally ramified", why the primes dividing $N$ qualify | 7.3, 7.4, 7.5 |
| DFG04 Theorem 2.7; Theorems 0.1, 0.2 | 7.6, 7.7, 7.5 |
| Taylor-Wiles in outline ($R_\Sigma$, $R_\Sigma\to\T_\Sigma$, numerical criterion, patching, Selmer as tangent space) | 8.1 to 8.5 |
| the assembly of Theorem thm:main step by step (lem:hecke, thm:dfg14, thm:dfg37, thm:dfg27, lem:dfg21, lem:h0, lem:fpr, def:terms, lem:tamfactor; cancellation; $\mathrm I_n^*$ primes) | 9.1, 9.2, 9.3, 9.4 |
| Theorem thm:twist in full | 11.1, 11.2, 11.3 |
| Theorem thm:quant in full, Steps 1 to 4, $\eta^{\mathrm{Hecke}}(g^S)$ versus the cohomological ideal | 12.1 to 12.6 |
| the remark after Theorem thm:quant (why the argument fails for $\mathrm{II},\mathrm{III},\mathrm{IV}$) | 12.7 |
| Kim-Ota and the Tamagawa exponent (Remark rem:ko(2)) | 10.2 |
| Open questions 1 and 2 | 13.3, 13.2 |
| Section 6 row: congruence ideal, $r_E$, $\eta^\Sigma$, $M_{f,\lambda}$, $\hat\delta_!$ (with 13, 14) | 3.3, 3.4, 5.2 to 5.5 |
| Section 6 row: multiplicity one, freeness, Gorenstein, $J_0(N)[\mathfrak m]$ (with 3, 14) | 5.7, 4.2, 4.4(d) |
| Section 6 row: Hida's congruence modules, Wiles's numerical criterion, DDT Lemma 4.17 (with 3) | 3.1, 3.6, 4.1, 4.3 |
| Section 6 row: Taylor-Wiles, $R=\T$, DFG04 Theorems 0.1, 0.2, 2.7, 3.7, Proposition 1.4, Lemma 2.1, Theorem 2.15 (with 18) | 6.2, 7.4 to 7.7, 8.1 to 8.5, 14.1 (Lemma 2.1 and Theorem 2.15: Chapter 18, its 10.4, 7.4) |
| Section 6 row: level raising, Wiles's level-raising factor (with 15, 19) | 6.3, 12.7 |
| Section 6 row: Ribet-Takahashi, Pollack-Weston, Kim-Ota, Tamagawa exponent (with 14, 15) | 10.2 |
| hook: Section 4 in full (4.1 to 4.4) | Sections 4 to 12 |
| hook: Theorem thm:dfg14 | 6.2, 6.3 |
| hook: Lemma lem:ddt417 | 4.3 |
| hook: Lemma lem:hecke | 5.6 |
| hook: Remark rem:free | 5.7 |
| hook: Theorem thm:dfg37 | 7.3, 7.4, 8.5 |
| hook: Theorem thm:dfg27 | 7.6 (stated in Chapter 18, its 10.2) |
| hook: Lemma lem:dfg21 | 9.2 Step 4 (proved in Chapter 18, its 10.4), 14.1 |
| hook: Lemma lem:fpr | 9.2 Step 4 (proved in Chapter 18, its 7.4, 7.5), 7.7, 14.1 |
| hook: Lemma lem:h0 | 9.2 Step 4 (proved in Chapter 11, its 8.5; Chapter 18, its 10.3) |
| hook: the proof of Theorem thm:main | 9.2 |
| hook: Remark rem:ko | 10.1, 10.2 |
| hook: Theorem thm:twist | 11.2 |
| hook: the proof of Theorem thm:quant and the remark after it | 12.2 to 12.7 |
| hook: Section 1 (Hida, DFG04, congruence ideal) | 3.3, 3.6, 7.7, 7.8 |
| hook: Lemma lem:crit | 3.4, 3.5 |
| hook: Remark rem:ns | 13.1 |
| also: Open question 3 (answered in Chapter 18, its 9.3; the identity 9.1 makes the Selmer length computable) | 9.1, 9.4 |
| also: the abstract ("elementary twisting argument"; "Bloch-Kato Selmer group of $\ad V_\ell E$"; "with equality when multiplicity one holds") | 12.5, 9.1 |
| also: important_notes.md points 16, 18, 19, 24, 35, 36, 38, 39, 47, 56, 59, 60, 61, 63, 64, 67, Q1, B3, B17, B19 | Part 6.4 |

### 4.2 Exercises (Section 15 of the chapter), graded from easy to harder

1. For $\T_r=\{(a,b)\in\Z_\ell^2:a\equiv b\pmod{\ell^r}\}$ and $\pi(a,b)=a$ compute $\wp$, $I$, $\eta$, $\Omega$ and $\Phi=\wp/\wp^2$; do the same for $\T_3^\flat$ and show $\len\Phi>v(\eta)$ there.
   Which of the two is a complete intersection?
2. Prove that $\wp\cap I=0$ iff $\eta\ne0$ (3.1(ii)), and give an example with $\wp\cap I\ne0$. Explain why the paper's Lemma lem:ddt417 survives this
   (important_notes.md point 19).
3. Run the proof of Lemma lem:ddt417 (4.3) on $L=\T_r$, $L=\Z_\ell^2$ with diagonal action, and $L=\T_r^2$ with an alternating pairing; identify $Q$ in each case.
4. (Check the paper's claim that "the Gram determinant of the pairing on $M_{f^\Sigma,\lambda}$ is $(\eta^\Sigma_{f,\lambda})^2$ up to a unit".) Prove that for a rank-two
   alternating form the Gram determinant is the square of a generator of the ideal of values, and that the image of $\wedge^2$ is that ideal
   (DFG04's definition, 5.4(ii)).
5. Prove that the idempotents of $\T_\ell$ are self-adjoint for $\hat\delta_!$ and that the restriction of $\hat\delta_!$ to $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ is perfect (point 36). Show that
   $M_{f,\lambda}$ lies in the $\mathfrak m_{f,\lambda}$-component.
6. (Check the paper's paragraph after Theorem thm:dfg14.) For a good prime $p$ and roots $\alpha,\beta$ of $X^2-a_pX+p$, prove
   $(1-\frac\alpha{\beta p})(1-\frac1p)(1-\frac\beta{\alpha p})=\frac{p-1}p\cdot\frac{(p+1)^2-a_p^2}{p^2}$. For $f=f_{11\mathrm a}$ and $\ell=3$ list the $p<40$ with $v_3$ of this factor positive,
   and compare with the levels $11p$ at which a newform congruent to $f$ modulo $3$ exists (Chapter 15, its 7.5).
7. (Check DFG04 Proposition 1.4(b) in the smallest case.) For $f=f_{11}$ and $\Sigma=\{2\}$, compute $f^\Sigma=f+2f(2z)+2f(4z)$ and verify that the factor
   $L^{\nv}_2(A_f,1)^{-1}=\frac12\cdot\frac{9-4}{4}=\frac58$ is a unit at $\ell=3$, so $\eta^{\{2\}}_{f,3}=\eta^\emptyset_{f,3}$; and for $\Sigma=\{7\}$ that the factor $\frac67\cdot\frac{64-4}{49}$ has $v_3=2$.
8. Show that for $f=f_E$ and $\ell\nmid2N$, $\ell\notin S_f$ iff $E[\ell]$ is irreducible and not ($\ell=3$ with image 3Ns) (7.1(ii); point 47), using the
   description of $\bar\rho|_{I_\ell}$ by fundamental characters.
9. (Check the paper's description of $H^1_\Sigma$.) Show that for $\Sigma\supseteq\{p\mid N\}$ DFG04's local condition $H^1_{\mathrm{ur}}$ at $p\notin\Sigma\cup\{\ell\}$ equals $H^1_f$.
   Give a $W$ and a prime at which $H^1_{\mathrm{ur}}(\Q_p,W)\ne H^1_f(\Q_p,W)$.
10. Write out the assembly 9.2 for 121a1 at $\ell=3$: compute each term ($\Sigma=\{11\}$, type $\mathrm{II}$, $L^{\nv}_{11}=1$, $e_3=v_3(12)=1$, $\Tam_{11}(\ad T)=\Z_3$), and
    deduce $H^1_f(\Q,\ad T_3\otimes\Q_3/\Z_3)=0$ from $\deg\varphi_E=6$.
11. (Check the paper's Remark rem:ko(1).) For a multiplicative prime with $n_q=9$, $q\equiv1\pmod9$ and unit part a cube in $\F_q^\times$, compute the excess of
    $v_3(\Tam_q(\ad T))$ over $t_3(E,q)$; find such a curve in the tables, if one exists below conductor $10{,}000$.
12. Prove Theorem thm:twist (11.2) for 121a1 and 121c1 directly: show $\iota(f_{121\mathrm c})=f_{121\mathrm a}$ and conclude $r(121\mathrm a)=r(121\mathrm c)$.
13. (Check the paper's sentence after Theorem thm:twist; point 16.) For the pairs 539c1/77c1, 980i1/140b1, 121d1/11a1 compute $v_3$ of the two modular
    degrees and the Euler term $v_3(q^2-1)$; which case of the theorem are they, and is the inequality strict?
14. Prove the sharpened Step 1 (12.3): $\iota(f)=g^S$ and $\iota$ maps $f^\perp$ into the $\T$-stable complement of $\C g^S$. Why must the complement be the
    $\T$-stable one (point 61)?
15. (Theorem thm:quant at $q=3$; point 60.) Verify with PARI that $L_3(A_f,1)^{-1}=\frac23\cdot\frac{16-a_3(E')^2}9$ for a curve of type $\mathrm I_0^*$ at $3$ (for example
    from Chapter 13, its 6.6, `c11.py`: 333d1 or 477a1 at $\ell=7$) and that $v_7(\deg\varphi_E)\ge e_7(E,3)$.
16. (Harder.) Prove 12.6: for $\ell\notin S_f$, $v_\ell(\deg\varphi_E)=v_\ell(\deg\varphi_{E_S})+\sum_{q\in S}e_\ell(E,q)$, from (eq:identity) with equality for $E$ and $E_S$. Deduce that
    every inequality in the proof of Theorem thm:quant is an equality, and verify it on 539d1 ($\ell=3$: $2=0+2$).

________________________________________________________________________________

## 5. Dependencies and forward pointers

Results from other chapters used here (by item):
* Chapter 3 (`ch:modules`): saturation (5.5), the congruence module of a decomposition (5.8), perfect pairings, orthogonals and the Gram
  cokernel (9.1 to 9.3), rank-two alternating pairings (9.4), adjoints and idempotents (9.5), algebra-module duality (9.6), finite free
  algebras and idempotent lifting (10.2, 10.3), idempotent congruences (10.6), congruence ideals (11.1), toy algebras (11.2), the
  ingredients of Lemma lem:ddt417 (11.3), Gorenstein and Mazur's freeness criterion (11.4, 11.5), the toy checks (11.6).
* Chapter 4 (`ch:reps`): homothety of lattices for irreducible residual representations (used in 6.2(c)); $\ad$ invariant under duals and
  twists (5.4(iv), 12.6).
* Chapter 9 (`ch:ellcurves`): quadratic twists and $a_p(E^{(d)})$ (11.2).
* Chapter 10 (`ch:reduction`): Lemma lem:twist (i), (ii) (12.2), Kodaira types.
* Chapter 11 (`ch:galrep`): $\ell\notin S_f$ versus 3Ns (its 8.6; 7.1), Lemma lem:h0 corrected (its 8.5; 13.1).
* Chapter 13 (`ch:hecke`): $\T$ and the perfect pairing (4.1, 4.2), $\eta(\phi)$ and $r_f$ (4.3), newforms and strong multiplicity one (6.2 to 6.4), $U_p$
  on oldforms and units (7.1, 7.2), depletion (7.4), structure of $\T$ (8.1), the $\T$-stable complement (8.2), local components (8.3), congruences
  (8.4), twist operator and transport (9.1, 9.3), Atkin-Li (9.2), the level-539 computations (11.3).
* Chapter 14 (`ch:moddeg`): $\hat\delta_!$ (3.3, 3.4), $M_{f,\lambda}$ (4.4), optimal curves (6.2, 6.4), $r_E$ and ARS (8.1 to 8.5), **9.1 to 9.6** (point 39 and the
  checklist), 9.7, 10.1 to 10.4, the Shimura subgroup (11.3).
* Chapter 15 (`ch:modgalrep`): Lemma lem:crit (8.2), level raising and the factor identity (7.1, 7.2), Ihara (7.4), twist levels (10.1, 10.2), Kim-Ota
  (11.4), the Taylor-Wiles remark (11.5).
* Chapter 17 (`ch:galcoh`): the abstract DFG04 Lemma 2.1 (10.3) and the length identity (10.4).
* Chapter 18 (`ch:blochkato`): $H^1_\Sigma$ (6.3), Tamagawa factors (7.1 to 7.5, 8.2 to 8.4, 9.3, 9.4), $S_f$ (10.1), thm:dfg27 (10.2), lem:h0 (10.3), lem:dfg21 (10.4),
  the length identity (10.5), **the Selmer half 11.1**, examples (11.3), Remark rem:ns (12.1), DFG04 Theorems 0.1 and 0.2 (14.4, 14.5).
* Chapter 19 (`ch:lfunctions`): naive factors (8.1, 9.7), the Petersson formula with $L^{\nv}$ (8.3), $A_g=A_f$ (9.5), Lemma lem:euler (9.3).

Forward pointers (chapters that use this one):
* Chapter 21 (`ch:paper`): A4.1 to A4.16 should cite this card for full proofs: A4.1 (5.2 to 5.4, with the corrected "dual of $T_\ell E$"), A4.2
  (6.2), A4.3 (4.3), A4.4 and A4.5 (5.6, 5.7: equality without freeness; points 35, 39), A4.6 to A4.8 (7.1 to 7.6, with the verified DFG04
  wording), A4.12 (9.2), A4.13 (10.1, 10.2), A4.14 (11.2, 11.3), A4.15, A4.16 (12.3 to 12.7, including 12.6), A8.1 (13.2, 13.3), B3 (14.1: every
  DFG04 status becomes "verified").
* Chapter 22 (`ch:computation`): the twist test of Part 6.6 (`quant.py`, `twistc.py`) as a worked session; $e_\ell$ at $q=3$ from `lfunsympow`.
* Appendix B (`ch:notation`): $\eta^\Sigma_{f,\lambda}$, $\eta^{\mathrm{Hecke}}$, $\Omega(\pi)$, $\Phi(\pi)$, $M_{f^\Sigma,\lambda}$, $\hat\delta_!$, $S_f$, $f^\Sigma$, $M^\Sigma$, $\delta_p$, $\iota_S$, $E_S$, $g^S$.

________________________________________________________________________________

## 6. Notes for the writer

### 6.1 Conventions to state (Section 1 of the chapter, as `convention` environments)

C1 to C8 of Part 1.3. Two `warning` boxes: (a) the paper's $I$ and $J$ in Lemma lem:crit are this chapter's $\wp$ and $I$ (C3); (b) the Hecke
congruence ideal and DFG04's cohomological ideal are different objects, compared by Lemma lem:ddt417 and equal at $\ell\nmid2N$ for the optimal
curve's newform (C4, 3.7).

### 6.2 Pitfalls

* **Assemble, do not re-derive.** Lemma lem:crit is Chapter 15's (B17); Lemma lem:hecke as an equality is Chapter 14's (9.3, 9.5; B19); the Selmer
  half is Chapter 18's (11.1); the naive factors are Chapter 19's (9.7). Each step of 9.2 names the chapter; the proofs there are not
  repeated. The only full proofs written here are Lemma lem:ddt417 (4.3), Proposition 1.4(c) from (b) (6.2), the assembly (9.2),
  Theorems thm:twist and thm:quant (11.2, 12.3, 12.4), and 12.6.
* **Published versus arXiv DFG04.** The arXiv text arXiv:2512.02348 has different section and theorem numbers (e.g. its Section 2 is
  "Premotivic structures for modular forms"). Cite only the published numbering, which the paper uses and which Part 7 verified.
* **$H^1(X_0(M),\Z_\ell)$ versus DFG04's integral structure.** They agree on non-Eisenstein $\mathfrak m$-components (5.2(ii)), which is all the paper uses. Do
  not claim equality of the whole lattices.
* **The pairing normalisation.** DFG04 divide the cup product by $[U:U_{N'}]$; on $X_0(M)$ this is the cup product times $1$ or $\frac12$ (5.3(ii)). Say "up to
  a unit at odd $\ell$".
* **Ideal of values, not Gram determinant.** DFG04 define $\eta^\Sigma$ via the image of $\wedge^2$; the Gram determinant is its square (5.4).
* **Naive versus true factors.** Proposition 1.4 has the **naive** factors; DFG04's Proposition 1.12 (refined structures) has the true ones. The
  paper and this chapter use only Proposition 1.4.
* **Twist-minimality.** DFG04 assume twist-minimal $f$ in Sections 1.8 and 2, and prove Theorem 3.7 for a twist and transfer it. The paper
  applies Theorem 3.7 to $f_E$ directly, which is fine because 3.7 is stated for every newform; but $\eta^\Sigma_f$ itself depends on $f$, not only on
  $A_f$ (that is the content of Theorem thm:quant), so the transfer is about $H^1_\Sigma$ and $\eta^\Sigma$ for the same $\Sigma$, not about $\eta^\emptyset$.
* **$\mathrm I_n^*$ at $2$** (point 18): use $n=-v_2(j)$ and the local twist argument of Chapter 18, its 8.4; the Kodaira index is not the Tate valuation at $2$.
* **The $\T$-stable complement** for $g^S$ (point 61); the Petersson complement is right only for newforms at their level.
* **$q=3$ in Theorem thm:quant** (point 60): allowed; $\ell\ne3$ then, since $\ell\nmid N$. State the extension as the book's, with the proof.
* **Equality statements.** 9.1 and 12.6 are equalities for $\ell\notin S_f$; they depend on point 39 (Chapter 14) and on the checklist of Part 7, now
  confirmed. Present them as theorems of the book that strengthen the paper, with the paper's weaker statements in `paperlink`s.
* **Theorem numbers.** Verified against the published DFG04 (Part 7): Theorems 0.1, 0.2, 2.7, 2.15, 3.1, 3.6, 3.7; Propositions 1.3, 1.4, 1.12, 2.2;
  Lemmas 1.2, 1.5, 1.8, 1.10, 1.11, 2.1, 2.4, 2.5, 2.12; Corollaries 1.6, 1.9, 2.3; (13), (14), (18), (22), (23), (25), (31), (53), (57). Not verified: DDT Lemma 4.17
  and Theorem 5.3 (cite "DDT Section 4" and "Section 5.1" unless checked), Hida81 Theorem 5.1 (as DFG04 cite it), KimOta Theorem 1.1 and
  Definition 2.12, RibetStein Theorem 3.5, ARS12 Theorem 2.2 (as the paper cites them).
* Typography (PLAN.md 7.2): "Diamond-Flach-Guo", "Taylor-Wiles", "Fontaine-Laffaille", "Fontaine-Perrin-Riou", "Kim-Ota" with plain hyphens;
  no Unicode; $\eta^{\mathrm{Hecke}}$ in roman.

### 6.3 What to leave to Chapters 3, 13, 14, 15, 17, 18, 19 and 21

As in Part 1.2: the module theory (Chapter 3), Hecke theory and twists (Chapter 13), $\hat\delta_!$, point 39 and multiplicity one (Chapter 14), Lemma
lem:crit, level raising and Kim-Ota (Chapter 15), the abstract Selmer comparison (Chapter 17), Bloch-Kato, Tamagawa factors and the
Selmer half (Chapter 18), Euler factors (Chapter 19), and the line-by-line tour of the paper's text (Chapter 21).

### 6.4 How the relevant important_notes.md points are handled

* **Point 16** (strict inequality not only in case (b)): 11.3, with the corrected sentence; 12.6 shows the difference is exactly the Euler term.
* **Point 18** ($\mathrm I_n^*$ at $q=2$): 9.2 Step 6, citing Chapter 18, its 8.4.
* **Point 19** ($\wp\cap I=0$): 4.3 step (0), 3.1(ii), Exercise 2.
* **Point 24** ("elementary"): 12.5 (outer inequality needs Steps 1 to 3; still not elementary), and 12.4 Step 4 (no freeness, by point 39).
* **Point 35** (kernel, not annihilator): 3.1(iv), 5.6.
* **Point 36** (pairing perfect on the $\mathfrak m$-part): 5.3(iv), 5.6, 12.4, Exercise 5.
* **Point 38** (lengths): C5, 4.3.
* **Point 39** (Lemma lem:hecke always an equality): 5.6 cites Chapter 14, its 9.3, 9.5; Part 7 confirms the identification with DFG04's $\eta$; 9.1 and 12.4
  use it.
* **Point 47** ($\ell\notin S_f$ automatic for $\ell\ge5$): 7.1(ii), 8.4, Exercise 8.
* **Point 56** (the DFG04 checklist): Part 7, all five items confirmed (item 1 in the form needed, on non-Eisenstein components); the second
  bullet ("Remark (2) after thm:quant still needs multiplicity one") is superseded by 12.6 (Part 8, N2).
* **Point 59** (Step 1 is an equality): 12.3.
* **Point 60** ($q=3$ allowed in thm:quant): 12.1, 12.4 (with the PARI check), Exercise 15.
* **Point 61** ($\T$-stable complement): 3.5, 12.3, Exercise 14.
* **Point 63** ($H^0(\Q,V^D)=0$ automatic): 9.2 Step 4, 7.6.
* **Point 64** (Tamagawa factors at additive potentially good primes trivial): 9.1, 9.2 Step 6.
* **Point 67** (Remark rem:ns needs $H^1_f(\Q,V^D)=0$, unknown for 3Ns): 13.1, 13.2.
* **Open check Q1** (DFG04 at $\ell=3$, weight $2$): settled, Part 7 (Q1): covered.
* Also: points 5, 6, 10, 14 (Lemma lem:h0) through Chapter 18, its 10.3 (9.2 Step 4); points 26, 40 ($M_{f,\lambda}$ versus the dual of $T_\ell E$) in 5.4(iv),
  now confirmed by DFG04 (18); point 11 (geometric Frobenius is DFG04's convention) confirmed (C6); points 23, 65, 68 in 10.1; point 27 in 9.3.
* **B3** (Chapter 21's A4.4 and A4.6): Part 5 forward pointers tell Chapter 21 which items to cite (kernel not annihilator; dual of $T_\ell E$).
* **B17** (lem:crit proved in Chapter 15): 3.4 restates and cites; the module-theoretic reading is the only addition.
* **B19** (cite Chapter 14's 9.3, 9.5, 9.6, 10.3): 5.6, 5.7, Part 7.
* **B14** (bibliography): see 6.5.

### 6.5 References

In `refs.bib` and cited here: DFG04 (published numbering), DDT (Sections 1 to 5, Lemma 4.17 as the paper cites it), Hida81, HidaBook,
Wiles95, TaylorWiles, Ribet83, Ribet84, ARS12, Tilouine97, RibetStein, Mazur77, FPR94, BlochKato, FontaineLaffaille, KimOta,
PollackWeston11, RibetTakahashi97, LingOesterle, Ribet88, Zagier85, Flach92, PARI, ecdata.

Proposed new keys (none is in `refs.bib` or any `bib/chNN.bib` now; all chapter bib files except `bib/chA.bib` are empty, checked):
* `DiamondTaylor94` (F. Diamond, R. Taylor, *Non-optimal levels of mod $\ell$ modular representations*, Invent. Math. 115 (1994), 435-462; the
  data as printed in DFG04's reference [26]): planned by Chapter 15 for `bib/ch15.bib` and needed here (level raising at $p\equiv-1$, Ihara), so by
  decision B14 it goes in **`refs.bib`**.
* `Diamond96` (F. Diamond, *On deformation rings and Hecke rings*, Ann. of Math. 144 (1996), 137-166; DFG04 [22]): `bib/ch20.bib` unless Chapter 15
  also cites it (its 11.5 mentions "Diamond's refinement"; then `refs.bib`).
* `Lenstra95` (H. W. Lenstra, *Complete intersections and Gorenstein rings*, in *Elliptic curves, modular forms and Fermat's last theorem*
  (Hong Kong, 1993), International Press, 1995, 99-109; pages to be checked): `bib/ch20.bib` (Chapter 3 mentions complete intersections only as
  a pointer here).
* `DFG04long` (F. Diamond, M. Flach, L. Guo, *Adjoint motives of modular forms and the Tamagawa number conjecture*, arXiv:2512.02348, 2001,
  updated 2025): `bib/ch20.bib`, cited once in the Notes for the foundational details omitted from the published version.
The data of DiamondTaylor94 and Diamond96 were read from DFG04's bibliography; Lenstra95's pages were recalled, not re-verified.

### 6.6 Verification log (computations and readings done for this outline)

Downloads to `/tmp/ch20`: the published DFG04 from Numdam (`dfg04.pdf`, 65 pages, text by `pdftotext -layout`) and arXiv:2512.02348v2 (109
pages). Scripts in the session scratchpad (`ch20/quant.py`, `ch20/twistc.py`, `ch20/ecross.py`), Python 3 with PARI/GP 2.17 through `cypari2`,
Cremona's `ecdata` files in `/tmp/ch09/data` (`degphi`, `galrep`).
* **Reading of DFG04** (Part 7): Sections 0.2, 0.3, 1.1.1, 1.1.2, 1.2.2, 1.2.3, 1.4.1, 1.4.2, 1.5.1 to 1.5.3, 1.6.1 to 1.6.3, 1.7.1 to 1.7.3, 1.8.1, 1.8.2,
  Proposition 1.12, Section 2.1, Lemmas 2.1, 2.4, 2.5, Theorem 2.7, Lemma 2.12, Section 2.4 with (55) to (58), Theorem 2.15 (beginning of the proof),
  Section 3.1 (Theorem 3.1 and its set-up), Section 3.2 (Theorems 3.6, 3.7).
* **Theorem thm:quant, equality** (`quant.py`): for every optimal curve of conductor below $10{,}000$ (from `degphi`), not CM, with at least one odd
  prime of type $\mathrm I_0^*$ or $\mathrm I_n^*$ (Kodaira code $-1$ or $\le-5$ from `elllocalred`), $S$ the set of these primes ($q=3$ included), $E_S$ = `elltwist` by
  $\prod q^*$, minimal model, its class located in `degphi` by conductor and $a_p$ for $p<80$ (always found); for $\ell\in\{3,5,7,11,13\}$, $\ell\nmid N$, $E[\ell]$ irreducible
  (no `galrep` label with B or Cs at $\ell$): $e_\ell(E,q)=v_\ell(q^2-1)$ ($\mathrm I_n^*$) or $v_\ell(q-1)+v_\ell((q+1)^2-a_q(E')^2)$ ($\mathrm I_0^*$). Result: $25{,}477$ pairs ($15{,}607$ with
  $3\in S$, $9{,}862$ with $S$ of primes $q\ge5$, $8$ with image 3Ns at $\ell=3$), **no violation of Theorem thm:quant and equality
  $v_\ell(\deg\varphi_E)=v_\ell(\deg\varphi_{E_S})+\sum_{q\in S}e_\ell(E,q)$ in every one**.
* **Euler terms against PARI** (`ecross.py`): $P_q(q^{-2})$ from `lfunsympow(E,2)` and `lfuneuler` against the twist formulas $\frac{(q-1)((q+1)^2-a_q(E')^2)}{q^3}$
  ($\mathrm I_0^*$) and $1-q^{-2}$ ($\mathrm I_n^*$): $400$ random (curve, odd prime) pairs below conductor $10{,}000$, $q=3$ included, no mismatch.
* **Theorem thm:twist, case (c)** (`twistc.py`): $S$ the set of primes $q\ge5$ of types $\mathrm{II},\mathrm{III},\mathrm{IV}$ or duals; $14{,}876$ pairs ($42$ of them 3Ns at $\ell=3$):
  $v_\ell(\deg\varphi_E)=v_\ell(\deg\varphi_{E_S})$ in every one.
* **Level-raising identity** (6.3, Exercise 6): $(1-\frac{\alpha}{\beta q})(1-\frac1q)(1-\frac{\beta}{\alpha q})q^3=(q-1)((q+1)^2-(\alpha+\beta)^2)$ with $\beta=q/\alpha$, checked symbolically in PARI.
* By hand: the proof of Lemma lem:ddt417 on the three toy modules (4.4); the factor $c\in\{1,\frac12\}$ in 5.3(ii) ($-1$ acts trivially on the upper half
  plane); the inflation-restriction description of the comparison in 5.2(ii); the chain in 12.6; the values in Exercises 7 and 10.
* Not checked: DDT's and Hida81's theorem numbers; KimOta's definition of $\eta_f(N)$ (10.2(i)); the general Eisenstein claim of 5.2(ii) beyond
  the Shimura covering (sketched; Part 7, item 1).

________________________________________________________________________________

## 7. DFG04 checklist

Source read: F. Diamond, M. Flach, L. Guo, *The Tamagawa number conjecture of adjoint motives of modular forms*, Ann. Sci. Ecole Norm.
Sup. (4) 37 (2004), no. 5, 663-727 (Numdam, item ASENS_2004_4_37_5_663_0; DOI 10.1016/j.ansens.2004.09.001), the version the paper cites.
A longer version is now on arXiv (arXiv:2512.02348, dated "August 2001, with minor update December 2025"), with **different** numbering;
nothing below refers to it. Quotations are from the published text (mathematical symbols transcribed; page numbers of the journal).

### 7.1 The five items of important_notes.md point 56

**Item 1. Which curve: is DFG04's integral structure $H^1(X_0(N),\Z_\ell)$? Confirmed in the form the paper needs (non-Eisenstein components);
not literally for the whole lattice.**
What DFG04 say. Section 1.2.2 (p. 674): $M_B=H^1(X^{an},\mathcal F^k_B)$, $M_{c,B}=H^1_c(X^{an},\mathcal F^k_B)$ for the full level-$N'$ curve $X=X_{N'}$ (open, adelic, with
$\varphi(N')$ geometric components); 1.2.3: the $\ell$-adic realisations are $H^1(X_{\bar\Q},\mathcal F_\ell^k)$ and $H^1_c$, "$\Z_\ell\otimes M_B\simeq M_\ell$". Section 1.4.1 (p. 678-679): for a
representation $\sigma$ of an open compact $U$, "$M(\sigma)=(M\otimes V)^U$ ... $M(\sigma)_!=\operatorname{im}(M(\sigma)_c\to M(\sigma)_{\mathrm{tf}})$. We remark that $M(\sigma)_!$ may lie properly in
$(M_!\otimes V)^U$ ... $M(\sigma)_c$ and $M(\sigma)_!$ are independent of $N$." Section 1.4.2 (p. 679): $U=U_0(N)$, $\sigma=\sigma(N,\psi)$ the character $\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\mapsto\psi^{-1}(a_N)$, "We let
$M(N,\psi)_\bullet$ denote the premotivic structure $M(\sigma)_\bullet$". So for $k=2$, $\psi=1$: $M(N,1)_{!,\lambda}$ is the image of the $U_0(N)$-invariants of $H^1_c$ of the
full-level open curve in the torsion-free quotient of the invariants of $H^1$. It is **not** defined as $H^1(X_0(N),\Z_\ell)$, and it is not a
$\Gamma_1(N)$-type trivial-character part either.
Comparison (this outline, 5.2(ii)). Pullback along $Y_{N'}\to Y_0(N)$ maps $H^1(X_0(N),\Z_\ell)$ (interior cohomology of $Y_0(N)$, item 2) into $M(N,1)_{!,\lambda}$ with finite
cokernel; by inflation-restriction the cokernel is a subquotient of $\Hom(U_0(N)/U',\Q_\ell/\Z_\ell)$ for a sufficiently small $U'$, i.e. it comes from cyclic
unramified subcovers of congruence covers of $X_0(N)$ (generalised Shimura coverings), which are Eisenstein; it vanishes when $\ell$ does not divide
the order of the covering group (transfer). DFG04 themselves arrange this in Section 1.8.1 with an auxiliary prime $r>3$, $L_r(A_f,1)^{-1}$ a unit, and
$U'=U^\Sigma\cap U_1(r)$ of index $r-1$ prime to $\ell$ ("Lemma 1.2 with $U'=U^\Sigma\cap U_1(r)$ yields ... Corollary 1.6"), and their Lemma 1.8 and Corollary 1.9 use
the same "kernel and cokernel are Eisenstein" device after localising at $\mathfrak m$. Since $M_{f,\lambda}=M(N,1)_{!,\lambda}[I_f]$ lies in the $\mathfrak m_{f,\lambda}$-component, and $\mathfrak m_{f,\lambda}$
is non-Eisenstein when $\bar\rho_f$ is irreducible, **$M_{f,\lambda}^{\mathrm{DFG}}=H^1(X_0(N),\Z_\ell)[I_f]$**, which is what Lemma lem:hecke and point 39 need. Verdict: confirmed for
the use made of it; the paper's sentence "The integral structure $M(M^\Sigma,1)_{!,\lambda}$ is $H^1(X_0(M^\Sigma),\Z_\ell)$" should read "agrees with $H^1(X_0(M^\Sigma),\Z_\ell)$ after
localisation at the non-Eisenstein maximal ideals". Confidence: high for the definitions; medium-high for the Eisenstein claim in general
(certain for the Shimura covering $X_1(N)\to X_0(N)$; Ling-Oesterle, Ribet88), which is the only part not read off DFG04.

**Item 2. Interior cohomology. Confirmed.** DFG04 Section 1.4.1 define $M(\sigma)_!$ as the image of compactly supported in ordinary cohomology
(quoted above). For constant coefficients on the open curve $Y_0(N)$ this image is $H^1(X_0(N))$ (the exact-sequence argument of Chapter 14, its
9.6(2)), and group cohomology of $\Gamma_0(N)$ with coefficients $\Z_\ell$ agrees with $H^1(Y_0(N),\Z_\ell)$ since elliptic elements are torsion. Confidence: high.

**Item 3. The operator $[UwU]_\omega$ and the normalisation of the pairing. Confirmed, up to a unit at odd $\ell$.** DFG04 Section 1.5.3 (p. 682):
"Let $w$ denote $\begin{psmallmatrix}0&-1\\N&0\end{psmallmatrix}$ in $\prod_{p\mid N}\GL_2(\Z_p)$. The operator $[UwU]_\omega$ defines an isomorphism (13) $M_\bullet(N,\psi)\to M_\bullet(\sigma')$ ... One finds that
$[UwU]_\omega^{-1}=[Uw^{-1}U]_{\omega^t\otimes\psi(\det w)}$ and $[UwU]_\omega$ is adjoint to $N^{k-2}[Uw^{-1}U]_{\omega^t\otimes\psi(\det w),c}$ and coincides with $\psi(-1_\infty)N^{k-2}[Uw^{-1}U]_\omega$. Composing the
operator $[UwU]_\omega$ with the duality morphism $\bar\delta$, we obtain a duality isomorphism (14) $\hat\delta\colon M(N,\psi)\to\Hom_K(M(N,\psi)_c,M_\psi(1-k))$. Similar
assertions hold for $M(N,\psi)_!$ yielding an isomorphism $\hat\delta_!$. Since $M(N,\psi)=0$ unless $\psi(-1_\infty)=(-1)^{k-2}$, we find that the corresponding perfect
pairing is alternating." For $k=2$, $\psi=1$: $N^{k-2}=1$, $[UwU]_\omega$ is an involution (it equals $[Uw^{-1}U]_\omega$, its own inverse), the Atkin-Lehner
involution, **with no scalar**. The pairing $\bar\delta$ is defined in Section 1.5.2, (11), (12): the cup product into $H^2$ of the full-level curve, restricted to
invariants, "normalizing by dividing by $[U:U_N]$, we get an isomorphism ... independent of $N$". On classes pulled back from $X_0(N)$ this is
$\deg(Y_{N'}\to Y_0(N))/[U:U_{N'}]$ times the cup product on $X_0(N)$, and the degree is $[U:U_{N'}]$ or $[U:U_{N'}]/2$ according as $-1$ acts trivially (it does: $-1\in\GL_2(\Q)$ acts
trivially on $\mathfrak H^\pm$); so the factor is $\frac12$, a unit for odd $\ell$ (point 56 anticipated "a factor 2 ... harmless for odd $\ell$"). Integrality and
perfectness: Section 1.5.2, "Poincare duality on $X_U$ then shows that the isomorphism $\bar\delta$ arises from an injective morphism ... whose cokernel $C$
satisfies $C_\ell=0$ for $\ell\nmid N(k-2)!$" ($U$ sufficiently small), Lemma 1.2, Corollary 1.6. **Elliptic points of order 3 at $\ell=3$**: DFG04 avoid them by
working at a sufficiently small level of index prime to $\ell$ (the auxiliary prime $r$, item 1); on the non-Eisenstein components the result is the
cup product on $X_0(N)$ (a smooth curve, unimodular Poincare duality). Confidence: high.

**Item 4. Kernel lattice, not projection lattice. Confirmed.** DFG04 Section 1.6.2 (p. 683): "Let $I_f=\ker\theta_f$ and $\mathcal M_f=M(N,\psi)_![I_f]$ in the
notation of Section 1.1.2"; Section 1.1.2 (p. 671): "If $I$ is an $\mathcal O_K$-submodule of $\End\mathcal M$, then we define an object $\mathcal M[I]$ ... as the kernel of
$(x_1,\dots,x_r)\colon\mathcal M\to\mathcal M^r$ where $x_1,\dots,x_r$ generate $I$." And Section 1.7.3: "The construction of Section 1.6.2 thus yields a premotivic structure
$\mathcal M_{f^\Sigma}$ ... contained in $M(N^\Sigma,\psi)_!$." The Hecke algebra $\T$ of Section 1.6.1 is generated by the $T_p$ for **all** primes $p$ (the double coset of
$\begin{psmallmatrix}p&0\\0&1\end{psmallmatrix}$ at $p\mid N$ is $U_p$), so $I_f$ is the kernel on the full Hecke algebra, as in the paper. Confidence: high.

**Item 5. Ideal of values versus Gram determinant. Confirmed (ideal of values).** DFG04 Section 1.7.3 (p. 687): "The pairing $\hat\delta_!$ defined in Section
1.5.3 restricts to an alternating pairing on $\mathcal M_{f^\Sigma}$, which Proposition 1.4 below shows is non-degenerate, hence induces an isomorphism
$\wedge^2_K M_{f^\Sigma}\to M_\psi(1-k)$. The image of $\wedge^2_{\mathcal O_K}\mathcal M_{f^\Sigma}$ therefore defines an integral structure for $M_\psi(1-k)$, necessarily of the form
$\eta^\Sigma_f\mathcal M_\psi(1-k)$ for some fractional ideal $\eta^\Sigma_f\subset K$. We call $\eta^\Sigma_f$ the (naive, $\Sigma$-finite) congruence $\mathcal O_K$-ideal of $f$." The image of $\wedge^2$ of a
rank-two lattice under an alternating pairing is the ideal of values; its square is the Gram determinant. Theorem 3.7 and Proposition 1.4(c)
are stated for this $\eta^\Sigma_f$ ("where $\eta^\Sigma_f$ was defined before Proposition 1.4"). Confidence: high.

**Consequence.** All five items hold in the form the paper uses. Hence **important_notes.md point 39 applies to DFG04's own ideal**:
$v_\lambda(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$ for the optimal curve and every $\ell\nmid2N$ with $\bar\rho$ irreducible; Lemma lem:hecke is an equality, (eq:identity) holds
with equality for $\ell\notin S_f$, and Remark rem:free is not needed for any statement of Theorem thm:main.

### 7.2 Open check Q1: does DFG04 Theorem 3.7 cover $\ell=3$ in weight $2$? **Yes (confirmed).**

* (31) (p. 695): $S_f=\{\lambda:\lambda\mid Nk!$, or $\bar M_{f,\lambda}$ is not absolutely irreducible on $G_F$, $F=\Q(\sqrt{(-1)^{(\ell-1)/2}\ell})\}$. For $k=2$, $k!=2$: the only conditions on $\ell$ are
  $\ell\nmid2N$ and the irreducibility. The abstract says the same: "$\lambda$ is any prime of $K$ not dividing $Nk!$".
* Fontaine-Laffaille: a crystalline representation is *short* (Section 1.1.2, p. 670) if $\operatorname{Fil}^0D=D$, $\operatorname{Fil}^{\ell-1}D=0$ and no nonzero quotient $V'$ has $V'\otimes\Q_\ell(\ell-1)$
  unramified; for $M_{f,\lambda}$ (Hodge-Tate weights $0,1$) at $\ell=3$ this holds. The adjoint is **not** short at $\ell=3$ (Section 1.7.1: one can twist $A_f$ into
  $\mathcal{MF}^0$ only "if $\ell-1>2(k-1)$"), but DFG04 never need that: in Section 2.1 they define $H^1_f(\Q_\ell,W_n)$ for $W=\Hom(L_1,L_2)\otimes\Q_\ell/\Z_\ell$ with $L_1,L_2$
  short, as the extensions (32) in the essential image of the Fontaine-Laffaille functor, and Proposition 2.2 and Corollary 2.3 (which needs only
  $\ell>2$) compare it with Bloch-Kato's condition.
* Taylor-Wiles: Section 3.1 requires $\rho_0$ odd, absolutely irreducible on $G_F$, twist-minimal, with Serre weight $2\le k\le\ell-1$ (for $k=2$, $\ell=3$: $2\le2$); Section 1.8
  requires, "if $3\in\lambda$, ... its restriction to $G_{\Q(\mu_3)}$ to be absolutely irreducible", which for $\ell=3$ is the same as the $S_f$ condition
  ($\Q(\sqrt{-3})=\Q(\mu_3)$).
Verdict: Theorem thm:main at $\ell=3$ (with $3\nmid N$, image not 3Ns) has its Taylor-Wiles input. Confidence: high (the conditions were read in all
three places where $\ell$ enters).

### 7.3 The theorem numbers and references the paper cites from DFG04

| paper's citation | what DFG04 contain there (published numbering) | verdict |
|-|-|-|
| Theorem 0.1 (Section 1.2, after thm:main) | "Theorem 0.1 (= Theorem 2.15). Let $f$ be a newform of weight $k\ge2$ and level $N$ with coefficients in $K$. If $\lambda$ is not in $S_f$, then the $\lambda$-part of the Bloch-Kato conjecture holds for $A_f$ and $A_f(1)$." | confirmed |
| Theorem 0.2 ("the form given as Theorem 0.2 there") | "Theorem 0.2 (= Theorem 3.7) ... Suppose $\Sigma$ is a finite set of rational primes containing those dividing $N$. Suppose that $\lambda$ is a prime of $K$ which is not in $S_f$ and does not divide any prime in $\Sigma$. Then $H^1_\Sigma(G_\Q,A_{f,\lambda}/\mathcal A_{f,\lambda})$ has length $v_\lambda(\eta^\Sigma_f)$." | confirmed |
| Theorem 3.7 (thm:dfg37) | stated for $\Sigma$ "a finite set of primes not containing $\ell$ such that $M_{f,\lambda}$ is minimally ramified outside $\Sigma$"; $\eta^\Sigma_f$ "defined before Proposition 1.4"; proof: for a twist of minimal conductor, then for $f$ | confirmed (statement as the paper quotes it) |
| Theorem 2.7 (thm:dfg27) | "Conjecture 2.6 holds for both $M=A_f$ and $M=B_f$ if $\lambda$ is not in $S_f$. More precisely ... $H^0(\Q,A_{f,\lambda})\simeq H^1_f(\Q,A_{f,\lambda})\simeq H^1_f(\Q,B_{f,\lambda})\simeq H^0(\Q,B_{f,\lambda})\simeq0$", $B_f=A_f(1)$ | confirmed ($V^D=B_{f,\lambda}$) |
| Proposition 1.4(c) (thm:dfg14) | "If $\bar M_{f,\lambda}$ is an irreducible $(\mathcal O_K/\lambda)[G_\Q]$-module, then $\gamma$ induces an isomorphism $\mathcal M_{f,\lambda}\to\mathcal M^\Sigma_{f,\lambda}$ ... and $\eta^\Sigma_{f,\lambda}=\eta^\emptyset_{f,\lambda}\prod_{p\in\Sigma}L^{\nv}_p(A_f,1)^{-1}$"; standing hypothesis of Section 1.7.3: $\lambda\notin S^K_N$ (for $k=2$: $\ell\nmid2N$) | confirmed |
| Lemma 2.1 (lem:dfg21) | the four-term sequence, under "$\Sigma$ is nonempty and contains all primes where $H^1_f(\Q_p,W)\ne H^1_{\mathrm{ur}}(\Q_p,W)$, and ... $H^0(\Q,V^D)=H^1_f(\Q,V^D)=0$"; sum over $p\in\Sigma\cup\{\infty\}$; proof via Flach's Proposition 1.4 ([32]) | confirmed; the paper's hypothesis ("every $p\ne\ell$ at which $W$ is ramified") implies DFG04's |
| Theorem 2.15 (proof) and FPR94 I.4.2.2 (lem:fpr) | "By [41, Proof of I.4.2.2] we have for $p\in\Sigma$, $\Fitt_{\mathcal O_\lambda}H^1_f(\Q_p,M_\lambda)=L_p(M,0)^{-1}\Tam^0_p(M_\lambda)$ since $L_p(M,0)^{-1}\ne0$" (p. 709), applied with $M=A_f(1)$ | confirmed ([41] is Fontaine-Perrin-Riou, `FPR94`) |
| p. 708 (definition of $\Tam_p$) | "The argument of [41, I.4.2.2] shows that if $p\ne\ell$, then $\Tam^0_p(M_\lambda)=\Fitt_{\mathcal O_\lambda}\bigl(H^1(I_p,M_\lambda)_{\mathrm{tor}}\bigr)^{G_{\Q_p}}$" (the factors defined "as in I.4.1 (and II.5.3.3) of [41]") | confirmed; the same misplaced superscript as the paper (point 37: the invariants are of the torsion module) |
| (57) | "$\Tam^0_p(M_\lambda)=\Tam^0_p(M^D_\lambda)$" for $p\ne\ell$, deduced from the formula above | confirmed (general, not only for the adjoint) |
| (31) | as in 7.2 | confirmed |
| Lemma 2.12 (Section 1, Petersson norm) | "$\langle\tau(f),\tau(f)\rangle_{\Gamma_1(N)}=\frac{(k-1)!\delta(N)N\varphi(N)L^{\nv}(A_f,\tau,1)}{4^k\pi^{k+1}}$", from Hida81 Theorem 5.1 | confirmed: the **naive** value, as Chapter 19, its 8.3, states |
| Section 1.7.2 (conventions: $\delta_p$, $L_p$, $L^{\nv}_p$) | $\delta_p=\dim M_{f,\lambda}^{I_p}$ ($=2,1,0$ for $p\nmid N$; $p\mid N$, $a_p\ne0$; $p\mid N$, $a_p=0$); $L^{\nv}_p=L_p$ if $\delta_p>0$, $1$ if $\delta_p=0$; at $\delta_p=1$, $L_p(A_f,s)=(1-p^{-1-s})^{-1}$ if $\pi_p(f)$ is special; $\operatorname{Frob}_p$ is the **geometric** Frobenius (Section 1.1.1) | confirmed; also confirms point 11 |
| Section 2.1 (Bloch-Kato and $H^1_\Sigma$) | as in 7.2 here; "$H^1_\Sigma$ ... without local conditions at $p\in\Sigma\cup\{\infty\}$ and slightly relaxed local conditions at primes where $H^1_{\mathrm{ur}}(\Q_p,W)$ is not divisible" | confirmed |
| Sections 1.5.3, 1.6.2, 1.7.3; (13), (14) | as in items 1 to 5 | confirmed (item 1 in the form needed) |
| Sections 1.6.1, 1.8.2 (self-adjointness) | 1.6.1, Proposition 1.3: the Hecke action is compatible with "the duality morphisms $\hat\delta$ and $\hat\delta_!$ of (14)"; 1.5.2: $[U'gU]^T$ is the adjoint of $[U'gU]$; 1.8.2: "the Hecke operators are self-adjoint with respect to the pairing of (25)" | confirmed |

Also confirmed: (18) the geometric Frobenius on $M_{f,\lambda}$ has characteristic polynomial $X^2-\psi(p)^{-1}a_pX+\psi(p)^{-1}p^{k-1}$, that of $H^1$, so $M_{f,\lambda}$ is the
dual of the Tate module (points 26, 40); (22) $A_{f\otimes\psi'}\simeq A_f$; DFG04's proof of Theorem 2.15 takes $\Sigma=\{p\mid N\}$ and runs the same steps (Proposition 1.4,
Lemma 2.1, the FPR formula, Theorem 3.7) as the paper's proof of Theorem thm:main.

________________________________________________________________________________

## 8. Points for important_notes.md

New points in this chapter's area (Section 4 of the paper, DFG04, congruence ideals), not among points 1 to 72, Q1 and B1 to B23. Points
16, 18, 19, 24, 35, 36, 38, 39, 47, 56, 59, 60, 61, 63, 64, 67, Q1, B3, B17, B19 are handled in Part 6.4 and not repeated, except where N1 and N2 settle
or supersede them.

**N1. Point 56 and open check Q1 settled: DFG04 confirms the paper's reading, with one rewording (DFG04 read).**
Location: Section 4.1 ("The integral structure $M(M^\Sigma,1)_{!,\lambda}$ is $H^1(X_0(M^\Sigma),\Z_\ell)$, with its Hecke action; ... the pairing $\hat\delta_!$ is the cup
product composed with the operator $[UwU]\omega$ ... which for weight $2$ and trivial character is the Atkin-Lehner involution"); Lemma lem:hecke;
Remark rem:free; Theorem thm:main ("with equality when ... free"); Section 4.2 ($S_f$).
Content: the published DFG04 was read (Part 7). Items 2 to 5 of point 56 hold verbatim: $M(\sigma)_!$ is the image of compactly supported
cohomology (interior cohomology); $[UwU]_\omega$ is the Atkin-Lehner involution with no scalar for $k=2$ ($N^{k-2}=1$), the duality being the cup product
divided by $[U:U_{N'}]$, i.e. the cup product on $X_0(N)$ up to the unit $\frac12$; $\mathcal M_f=M(N,\psi)_![I_f]$ is the kernel lattice for the full Hecke algebra;
$\eta^\Sigma_f$ is defined by the image of $\wedge^2\mathcal M_{f^\Sigma}$, i.e. the ideal of values. Item 1 holds in the form needed: DFG04's integral structure is
not defined as $H^1(X_0(N),\Z_\ell)$ but as the image of the $U_0(N)$-invariants of the compactly supported cohomology of the full-level curve; it agrees with
$H^1(X_0(N),\Z_\ell)$ on non-Eisenstein components (the discrepancy, if any, comes from abelian unramified subcovers of congruence covers and is
Eisenstein; DFG04 avoid it with an auxiliary prime $r$, Section 1.8.1), and the paper only uses $\mathfrak m_{f,\lambda}$ with $\bar\rho$ irreducible. Q1: $S_f$ in (31) excludes only
$\lambda\mid Nk!$ ($=2N$ for $k=2$) and residually induced-from-$\Q(\sqrt{\ell^*})$ forms; Fontaine-Laffaille is applied to $M_f$ (weights $0,1$, short at $\ell=3$), and the
adjoint's local condition is defined through extensions of short objects ((32), Proposition 2.2, Corollary 2.3 for $\ell>2$); the Taylor-Wiles
set-up (Section 3.1) requires Serre weight $2\le k\le\ell-1$; so $\ell=3$ is covered in weight $2$. The paper's theorem numbers from DFG04 (Theorems 0.1,
0.2, 2.7, 2.15, 3.7; Proposition 1.4(c); Lemmas 2.1, 2.12; (31), (57); p. 708; Sections 1.5.3, 1.6.1, 1.6.2, 1.7.2, 1.7.3, 1.8.2, 2.1; (13), (14)) are all
correct for the published version.
Consequences: point 39 holds for DFG04's $\eta$: Lemma lem:hecke is an equality, (eq:identity) is an equality for $\ell\notin S_f$, the phrase "with equality
when $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ is free" and the dependence of the equality on Remark rem:free can be removed; Theorem thm:main at $\ell=3$ stands.
Fix: (a) in Section 4.1 write "The integral structure $M(M^\Sigma,1)_{!,\lambda}$ agrees, after localisation at any non-Eisenstein maximal ideal of the Hecke
algebra, with $H^1(X_0(M^\Sigma),\Z_\ell)$" and "the pairing ... is, up to the unit $\frac12$, the cup product composed with $w_{M^\Sigma}$"; (b) state Lemma lem:hecke as
an equality with the proof of point 39; (c) a footnote that the arXiv version of DFG04 (2025) has different numbering. Confidence: high for
the readings (quoted in Part 7); medium-high for the Eisenstein nature of the comparison cokernel beyond the Shimura covering (sketched,
not read off DFG04).

**N2. Remark (2) after Theorem thm:quant: the first inequality is an equality whenever $\ell\notin S_f$, with no multiplicity-one hypothesis;
the data show equality in every tested case (supersedes the second bullet of point 56 and Chapter 14, its 9.5(c), 10.4(b)).**
Location: the remark after the proof of Theorem thm:quant, (2): "so the first inequality of Theorem thm:quant is an equality when
$H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ is free, that is, under multiplicity one at level $N$"; Section 1.5 ("the identity (eq:identity) for $E$ and for $E_S$ shows that the
first inequality is then an equality when multiplicity one holds at both levels").
Problem: the hypothesis is not needed. With point 39 confirmed for DFG04's ideal (N1), (eq:identity) holds with equality for $E$ and for the optimal
curve of the class of $E_S$ whenever $\ell\notin S_f$ (then also $\ell\notin S_{f_{E_S}}$: $N_S\mid N$, and twisting does not change absolute irreducibility over $\Q(\sqrt{\ell^*})$).
The Selmer groups and Tamagawa factors of $E$ and $E_S$ coincide ($\ad T$ is twist-invariant), and the Euler sums differ by exactly $\sum_{q\in S}e_\ell(E,q)$, so
$v_\ell(\deg\varphi_E)=v_\ell(\deg\varphi_{E_S})+\sum_{q\in S}e_\ell(E,q)$; with ARS at level $N_S$ ($\ell\nmid N_S$) and the chain of Steps 1 to 3, every inequality in the proof of Theorem
thm:quant is an equality (in particular $v(\eta^{\mathrm{Hecke}}(g^S))=v(\eta^S_{g,\lambda})$ at level $N$, a freeness-type statement for the depleted form). Data: for all optimal
non-CM curves of conductor below $10{,}000$ with at least one odd prime of type $\mathrm I_0^*$ or $\mathrm I_n^*$ ($q=3$ included), $\ell\in\{3,5,7,11,13\}$, $\ell\nmid N$, $E[\ell]$
irreducible: $25{,}477$ pairs, equality $v_\ell(\deg\varphi_E)=v_\ell(\deg\varphi_{E_S})+\sum_{q\in S}e_\ell(E,q)$ in **every** one (including $8$ pairs at $\ell=3$ with image 3Ns, outside the
argument). Examples: 539c1 ($2=1+1$), 980i1 ($2=1+1$), 121d1 ($1=0+1$), 539d1 ($2=0+2$).
Fix: in Remark (2) and Section 1.5, replace "when ... free, that is, under multiplicity one at level $N$" by "whenever $\ell\notin S_f$ (by (eq:identity) for $E$
and $E_S$, each an equality by Lemma lem:hecke in its strengthened form)", and add the data line; the data paragraph after Theorem thm:twist
can then say that the difference in cases (a) and (b) is **exactly** the Euler term (point 16). Confidence: high (the argument uses only
statements proved in the book, given N1; the data are a complete count from `ecdata`).

**N3. Lemma lem:dfg21: the paper's hypothesis is a sufficient form of DFG04's (confirmation, expository).**
Location: Lemma lem:dfg21 ("let $\Sigma$ be a nonempty finite set of primes containing every prime $p\ne\ell$ at which $W$ is ramified").
Content: DFG04 Lemma 2.1 asks that $\Sigma$ be nonempty and contain "all primes where $H^1_f(\Q_p,W)\ne H^1_{\mathrm{ur}}(\Q_p,W)$" (with $\ell\notin\Sigma$ from Section 2.1); at an
unramified $p\ne\ell$ the two groups agree, so the paper's condition implies DFG04's. Similarly the paper's description of $H^1_\Sigma$ ("unramified
elsewhere") is DFG04's (they use $H^1_{\mathrm{ur}}$, not $H^1_f$, outside $\Sigma\cup\{\ell\}$). No change needed; optionally say "(a sufficient form of the hypothesis of DFG04)".
Confidence: high.

**N4. Section 1 and Lemma lem:tamfactor: "the conventions of DFG04 Section 1.7.2" include the geometric Frobenius (confirmation of point 11).**
DFG04 Section 1.1.1 (p. 668): "$\operatorname{Frob}_p$ for the geometric Frobenius element in $G_p/I_p$", and Section 1.7.2 defines $\delta_p=\dim M_{f,\lambda}^{I_p}$ with $M_{f,\lambda}$ the
$H^1$-lattice; so the paper's $L_p(A_f,s)$ "following DFG04 Section 1.7.2" is with the geometric Frobenius, as point 11 says, and the paper's
$\delta_p=\dim V^{I_p}$ ($V=V_\ell E$, the dual) is the same number. Point 11's fix for Lemma lem:tamfactor (say "arithmetic") stands. Confidence: high.

None other found. Checked and found correct (beyond the points above): Lemma lem:ddt417's statement and its use with $d=2$ (modulo points 19, 38);
Theorem thm:dfg14's three cases and the factor $1-p^{-2}$ (DFG04 (23) at $s=1$); Theorem thm:dfg37 and the minimal-ramification remark; Theorem thm:dfg27
(as DFG04's "more precisely"); the assembly of Section 4.3 (it is DFG04's own proof of Theorem 2.15 with the modular degree in place of the
period); Theorem thm:twist (proof, and case (c) equality on $14{,}876$ pairs); Theorem thm:quant (proof, no violation on $25{,}477$ pairs); the claim
$\iota(g^S)=f$; Step 3's identification of the naive factor of $g$ with the omitted factor of $f$ ($400$ PARI checks, $q=3$ included).

Book-internal inconsistencies found while preparing this outline:

* **B-a. Point 56, second bullet; Chapter 14 outline, 9.5(c) and 10.4(b); Chapter 15 outline, 10.4 remark (2); Chapter 21 outline, A4.16(2).**
  All say the equality in Theorem thm:quant (Remark (2)) still needs multiplicity one at level $N$. Superseded by N2 (item 12.6 here): it holds
  whenever $\ell\notin S_f$. The Chapter 14 writer should change 9.5(c) and 10.4(b) to cite `\Cref{ch:congruence}`.
* **B-b. "Not checked against DFG04" statuses.** Chapter 14's 9.6 ("medium for the identification"), Chapter 18's Q1 and 10.1 ("see Q1"), Chapter 19's 8.3
  ("DFG04 Lemma 2.12 ... content not re-checked") and 8.5 ("the period normalisation of DFG04 is not checked"), and Chapter 21's B3 table ("as cited")
  can now cite Part 7 here: all DFG04 citations are verified (the period normalisation of DFG04 Theorem 2.10 was **not** checked here either).
* **B-c. Chapter 13 outline, 7.4 reference line**: "DFG04 Sections 1.5.3, 1.7.3 (as cited by the paper, for the notation $M^\Sigma$, $f^\Sigma$)": $N^\Sigma$ and $f^\Sigma$ are
  in DFG04 Section 1.7.3 only; 1.5.3 is the duality. Minor.
* **B-d. Chapter 21 outline, A4.1** says $M_{f^\Sigma}$ for $\Sigma=\emptyset$ is "isomorphic to $\Hom(T_\ell E,\Z_\ell)=T_\ell E(-1)$ up to homothety", A4.6 still says "homothetic to $T_\ell E$"
  (already B3), and A4.5 routes the equality through Remark rem:free (already B19). Not new; Chapter 21 should cite 5.4(iv), 5.6, 5.7 here.
* **B-e. Chapter 18 outline, 14.5**: "DFG04 Theorem 0.2 = Theorem 3.7 in the paper's reading": DFG04 print "Theorem 0.2 (= Theorem 3.7)" themselves, with
  the hypothesis "$\Sigma$ containing those dividing $N$" in 0.2 and "minimally ramified outside $\Sigma$" in 3.7. Both readings are now quoted in 7.4, 7.5 here.
* **B-f. PLAN.md, Chapter 20 entry.** "DDT Theorem 5.3 / Lemma 4.17" for the numerical criterion: Theorem 5.3 is not verified (cite DDT Section 5.1);
  "the Gram determinant of the pairing on $M_{f^\Sigma,\lambda}$ is $(\eta^\Sigma)^2$" is right, but DFG04 define $\eta^\Sigma$ via $\wedge^2$ (ideal of values), not via the Gram
  determinant; "Remark rem:free on when freeness holds" no longer bears on Theorem thm:main (N1).
* **B-g. Bibliography (B14).** `DiamondTaylor94` is planned by Chapter 15 for `bib/ch15.bib` and is needed here: it belongs in `refs.bib`. `Diamond96`,
  `Lenstra95`, `DFG04long` go in `bib/ch20.bib` unless another chapter cites them.
* Consistency checks that passed: Chapter 3's 11.1 to 11.6 (the ingredients and toy checks of Lemma lem:ddt417), Chapter 13's 7.2, 7.4, 8.2, 8.3, 9.1,
  9.3, 11.3 (Step 1 of thm:quant, the level-539 congruence modules), Chapter 14's 9.1 to 9.7 (now unconditional), Chapter 15's 7.2, 10.1 to 10.4,
  Chapter 17's 10.3, 10.4, Chapter 18's 10.1 to 11.1 and 14.4 (the Selmer half and the DFG04 statements, now verified), Chapter 19's 8.3, 9.5 to 9.7
  (Lemma 2.12 verified; the naive factors) agree with this line-up and with Part 7.
