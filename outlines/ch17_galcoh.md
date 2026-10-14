# Line-up for Chapter 17: Galois cohomology, local and global, and Selmer groups (`ch:galcoh`, `chapters/ch17_galcoh.tex`)

Stage 1 output (core results in teaching order). Part V (Cohomology, Selmer groups and L-functions), between
Chapter 16 (group cohomology, continuous cohomology, procyclic groups, the model computation of Lemma lem:tamfactor)
and Chapter 18 (Bloch-Kato conditions, Tamagawa factors, the adjoint motive). Target length 2,110 lines of LaTeX
excluding the card (Part 11 below), inside the 1,000 to 2,200 range of PLAN.md Section 7.3.
Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference.

Item format (as in the Chapter 2 to 15 outlines): number, label-ready name, kind, rigour tag; the precise statement
with all hypotheses; reference (book and theorem number only where sure, otherwise book and chapter or section; a
number followed by "(check)" must be verified by the writer before it is printed, or replaced by the section);
the paper's use by its `\label` names, or "background". The numerical examples (Tate parameters and unit parts,
full $5$-torsion of 11a1 over $\Q_{11}$, orders of local cohomology groups, the toy Selmer computations) were
checked with PARI/GP 2.17 through cypari2 and Cremona's ecdata files (verification log, Part 15).

## 0. Purpose of the chapter, and what it must deliver

### 0.1 Purpose

Chapter 16 built the engine (cochains, inflation-restriction, continuous cohomology, procyclic groups) and did the
pure group cohomology of Lemma lem:tamfactor. This chapter specialises to Galois groups of fields, local and global,
and builds the arithmetic that the paper uses in four places:

1. **Lemma lem:tamfactor (the end of its proof) and Lemma lem:tamagawa-exp.** Hilbert 90 and Kummer theory in
   cohomological form, $H^1(K,\mu_n)=K^\times/(K^\times)^n$ and $H^1(K,\Z_\ell(1))=\varprojlim K^\times/(K^\times)^{\ell^k}$; over
   $\Q_q$ ($q\ne\ell$) the unramified classes are exactly the Kummer classes of units, $H^1(G/I,\Z_\ell(1))=\Z_\ell(1)/(q-1)
   \simeq\F_q^\times\otimes\Z_\ell$; the Kummer class of the Tate parameter $q_E=q^nu$ decomposes as $n\kappa_q+\kappa_u$, and the
   value $c'$ in the corner of $\rho(\Frob)$ is, up to the sign $\varepsilon(\Frob)$ and modulo the ideal $(n,q-1)\Z_\ell$, the
   class of the reduction $\bar u$ in $\F_q^\times\otimes\Z_\ell$. This proves the sentence "Finally $c'$ is the image of
   $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)$ ... the class of the unit part of $q_E$ in $\F_q^\times\otimes\Z_\ell$ by Kummer theory"
   in a corrected and precise form (important_notes.md points 7, 31, 42; Section 5).
2. **The paragraph after Lemma lem:dfg21.** Unramified cohomology $H^1_{\mathrm{ur}}(\Q_p,M)=M^{I_p}/(\Frob_p-1)M^{I_p}$; its
   vanishing for $V$ exactly when $\det(1-\Frob_p\mid V^{I_p})\ne0$ (a condition independent of the Frobenius convention,
   although the identification of the determinant with $L_p(A_f,1)^{-1}$ needs the geometric one, point 11); the
   torsion of $H^1(\Q_p,T)$ as $H^0(\Q_p,W)$ modulo its divisible part; hence "$H^1_f(\Q_p,T^D)$ is the torsion of
   $H^1(\Q_p,T^D)$, a finite group"; and "$H^1(\R,T^D)$ is killed by $2$" (Sections 2, 4, 6).
3. **Lemma lem:dfg21, the proof of Theorem thm:main and Remark rem:ns.** Tate local duality, the exact orthogonality of
   unramified classes, propagation of local conditions from $V$ to $T$ and $W$, Selmer structures and their duals,
   the Greenberg-Wiles formula, the Poitou-Tate sequence, the comparison sequence of two Selmer structures, and an
   abstract form of DFG04 Lemma 2.1 (relaxing the conditions at a set $\Sigma$) with the length identity
   $\len H^1_{\mathcal L^\Sigma}(\Q,W)=\len H^1_{\mathcal L}(\Q,W)+\sum_{p\in\Sigma}\len\mathcal L_{T^D,p}-\len H^0(\Q,W^D)$, of which the
   proof of Theorem thm:main uses the case $H^0(\Q,W^D)=0$ and Remark rem:ns the case of length $h_\ell(E)$
   (Sections 8 to 10). Chapter 18 plugs in the Bloch-Kato structure and DFG04 Theorem 2.7.
4. **The Selmer groups of Theorem thm:main.** $H^1_f(\Q,\ad T\otimes\Q_\ell/\Z_\ell)$ and $H^1_\Sigma(\Q,W)$ are Selmer groups
   of Selmer structures in the sense of Section 8; the classical $n$-Selmer group of an elliptic curve (Section 7) is
   the model, and it also discharges Chapter 9's deferral of the weak Mordell-Weil theorem.

It also discharges what earlier chapters deferred to it (by `\Cref{ch:galcoh}`): Chapter 5 (Hilbert 90 in profinite
form; $H^1(K,\mu_n)=K^\times/K^{\times n}$ without $\mu_n\subset K$; the Kummer class in $H^1(K,\Z_\ell(1))$; $G_\R=\{1,c\}$ and
$H^1(\R,-)$; the identification of the class of the unit part, end of Lemma lem:tamfactor), Chapter 7 (6.1(ii): the Kummer
maps are isomorphisms, via Hilbert 90; the cohomological half of the fix of point 7; the local Euler characteristic
count of its 2.7(iv)), Chapter 8 (4.2(iii): Hilbert 90 for $\bar k(C)$, stated there), Chapter 9 (9.1: weak Mordell-Weil via the
Kummer map and Selmer groups; 5.3, 5.5: $E[n]$, the Weil pairing as $E[n]\simeq E[n]^*(1)$), Chapter 10 (7.4, 7.6, 7.8: $q_E$,
$u$, $c(u)$, $c_q$ in Lemma lem:tamfactor), Chapter 11 (3.2: the Kummer class $\varepsilon\kappa$ in the corner), Chapter 15 (3.5:
the local types used for unramified cohomology at $p\mid N$), Chapter 16 (Hilbert 90, Kummer theory, Tate local duality,
$H^1_{\mathrm{ur}}$ and its annihilator, the torsion of $H^1(K,T)$ via $H^0(K,W)$, finiteness of $H^1$ for $G_{\Q_p}$ and
$G_{\Q,S}$, and the Kummer class of the Tate parameter: its writer notes 10 and 13), Chapter 21 (items A2.7 step (7),
A4.9 "attached facts" and proof idea, A4.10 steps (1) to (5) for the inputs, A5.2).

### 0.2 Global conventions fixed in this chapter (to be typeset as `convention` environments)

* **C1 (fields and groups).** $K$ is a field of characteristic not $\ell$ (in practice $\Q$, $\R$, $\Q_p$, a finite extension of
  $\Q_p$, $\F_q$); $\overline K$ a separable closure; $G_K=\Gal(\overline K/K)$ with the Krull topology. $H^n(K,M):=H^n(G_K,M)$ is
  continuous cochain cohomology (Chapter 16), with the three coefficient types of Chapter 16: (D) discrete, (C) finitely
  generated $\Z_\ell$-modules with the $\ell$-adic topology, (V) finite-dimensional $\Q_\ell$-vector spaces. For $K=\Q_p$:
  $I_p\trianglelefteq G_{\Q_p}$, $G_{\Q_p}/I_p\simeq\hat\Z$; for $K=\R$: $G_\R=\{1,c\}$; $H^n(\R,M)=H^n(G_\R,M)$.
* **C2 (Frobenius).** $\Frob=\Frob_p$ is an **arithmetic** Frobenius (acts on $\overline\F_p$ by $x\mapsto x^p$; $\chi_\ell(\Frob)=p$ for
  $\ell\ne p$), as in Chapters 5, 6, 7 (L3), 16 and 21. $\Phi=\Frob^{-1}$ is the geometric Frobenius. Group cohomology
  (conjugation actions, $H^1_{\mathrm{ur}}=M^I/(\Frob-1)$, the matrices of Lemma lem:tamfactor) uses $\Frob$. Whenever a local
  $L$-factor is named, it is $L_p(V,s)=\det(1-\Phi p^{-s}\mid V^{I_p})^{-1}$ (Chapter 7, L6). An arithmetic eigenvalue $\lambda$ is
  the geometric eigenvalue $\lambda^{-1}$. (The Weil-Deligne relation is not used in this chapter; important_notes.md B6.)
* **C3 (twists and duals).** $\Z_\ell(1)=T_\ell\mu=\varprojlim_k\mu_{\ell^k}$, $\Q_\ell/\Z_\ell(1)=\mu_{\ell^\infty}$, $\Q_\ell(1)=\Z_\ell(1)\otimes\Q_\ell$; $M(1)=M\otimes\Z_\ell(1)$.
  $A^*=\Hom_{\mathrm{cont}}(A,\Q_\ell/\Z_\ell)$ (or $\Hom(A,\Q/\Z)$ for finite $A$) is the **Pontryagin dual**, exactly as in the paper
  ("$^*$ is the Pontryagin dual" in Lemma lem:dfg21) and in Chapter 16. $T^\vee=\Hom_{\Z_\ell}(T,\Z_\ell)$, $V^\vee=\Hom_{\Q_\ell}(V,\Q_\ell)$
  are linear duals. The **Kummer dual** (Cartier dual) of a finite or discrete $\ell$-primary module $M$ is
  $M^*(1)=\Hom(M,\mu_{\ell^\infty})$; for a lattice $T$: $T^D:=\Hom_{\Z_\ell}(T,\Z_\ell(1))=T^\vee(1)$, $V^D=T^D\otimes\Q_\ell=\Hom(V,\Q_\ell(1))$,
  $W^D:=V^D/T^D\simeq\Hom(T,\Q_\ell/\Z_\ell(1))=T^*(1)$. These are the paper's $T^D,V^D,W^D$ (Section 4.2), there for
  $T=A=\ad T_\ell E$; the identification $T^D\simeq A(1)$ via the trace form is Chapter 18's (and Chapter 4's 7.6). The book's
  symbol $*$ is otherwise overloaded (important_notes.md B4); in this chapter it means Pontryagin dual only.
* **C4 (lattices).** $T$ is a free $\Z_\ell$-module of finite rank with a continuous $\Z_\ell$-linear action, $V=T\otimes_{\Z_\ell}\Q_\ell$,
  $W=T\otimes_{\Z_\ell}\Q_\ell/\Z_\ell=V/T$, $W[\ell^k]=T/\ell^kT$ (Chapter 3, 8.3); $\iota\colon H^1(K,T)\to H^1(K,V)$ and
  $\pi\colon H^1(K,V)\to H^1(K,W)$ are the maps induced by $T\subset V\to W$. "Length" is $\Z_\ell$-length; $v_\ell(\ell)=1$.
* **C5 (places, sets).** $p$ runs over primes, $v$ over places of $\Q$ including $\infty$; $\Q_\infty=\R$. $S$ is a finite set of places
  containing $\infty$; $\Q_S$ the maximal extension of $\Q$ in $\overline\Q$ unramified outside $S$; $G_{\Q,S}=\Gal(\Q_S/\Q)$. A fixed
  embedding $\overline\Q\to\overline\Q_v$ for each $v$ identifies $G_{\Q_v}$ with a decomposition group (Chapter 7, 3.5);
  localisation $\operatorname{res}_v\colon H^1(\Q,M)\to H^1(\Q_v,M)$ does not depend on the embedding (conjugate embeddings give the
  same map on cohomology, Chapter 16 conjugation-action). $\Sigma$ denotes the paper's finite set of primes (in the paper,
  the primes dividing $N$); $\ell\notin\Sigma$.
* **C6 (signs of Kummer maps).** The connecting map of $1\to\mu_n\to\overline K^\times\xrightarrow{n}\overline K^\times\to1$ is
  $\delta(a)(\sigma)=\sigma(\alpha)/\alpha$ with $\alpha^n=a$, the convention of Chapter 16 (h0-h1: $\delta(m'')=[g\mapsto gm-m]$), of
  Chapter 5 ($\chi_a$) and of Chapter 7 ($\kappa_x$). No sign is introduced anywhere.
* **C7 (labels and typography).** Labels `...:galcoh:...`; the names below are the label stems. No em or en dashes and no
  double hyphens anywhere (write "Poitou-Tate", "Greenberg-Wiles", "Bloch-Kato", "Hochschild-Serre" with plain hyphens;
  ranges "1 to 8"); ASCII source; `\ell`; macros `\Frob`, `\Fitt`, `\len`, `\Tam`, `\ad` and those listed in Chapter 16's
  writer note 16 (`\Zl`, `\Ql`, `\Qlmod`, `\Hur`, `\Hf`, `\Inf`, `\Res`, `\Cor`, `\tors`); no new macros.

### 0.3 Scope check (PLAN.md Section 4 entry for Chapter 17)

Each scope item is mapped to line-up items in Part 12 (coverage table). In order of the PLAN entry: Galois cohomology
of a field (1.1, 1.2); Hilbert 90 (1.3); Kummer theory $H^1(K,\mu_n)=K^\times/(K^\times)^n$ proved (1.4); Kummer map and class (1.5,
1.6); $H^1(K,\Z_\ell(1))=\varprojlim K^\times/(K^\times)^{\ell^k}$ and $\Z_\ell(1)=T_\ell\mu$ (2.4, 2.5); Brauer group and $H^2(K,\mu_n)$ (1.7);
finiteness of $H^i(\Q_p,M)$ (3.1); local Euler-Poincare characteristic (3.2, 3.5); Tate local duality (3.3, 3.4);
$H^1_{\mathrm{ur}}$ via inflation-restriction (4.1, 4.3); $H^1_{\mathrm{ur}}=M^{I_p}/(\Frob_p-1)M^{I_p}$ (4.2); the annihilator of $H^1_{\mathrm{ur}}$
(4.4); the real place (6.4); $G_\Q$ and $G_{\Q,S}$ (6.1, 6.2); finiteness of $H^1(G_{\Q,S},M)$ (6.3); the Kummer sequence of an
elliptic curve (7.1, 7.2); the $n$-Selmer group and Sha, finiteness, weak Mordell-Weil (7.3 to 7.5); Selmer structures and
dual structures (8.1 to 8.3); Greenberg-Wiles (9.3, 9.4, 9.5); Poitou-Tate (9.1, 9.2); comparison of Selmer groups, the
elementary part proved, and its specialisation to Lemma lem:dfg21 (10.1 to 10.6); $T$, $V$, $W$ cohomology and
$H^1(K,T)_{\mathrm{tors}}$ (2.1 to 2.3); $H^1(\Q_p,T)$ finitely generated with torsion $H^0(\Q_p,W)/\mathrm{div}$, and the paper's
"$H^1_f(\Q_p,T^D)$ is the torsion" (2.2, 3.1, 4.6); the Kummer class of the Tate parameter and its image in
$H^1(G/I,\Z_\ell(1)^I)=\Z/\ell^{v_\ell(q-1)}$, proved in full (5.1 to 5.6). Additions not in the PLAN entry but needed: propagation of
local conditions from $V$ to $T$ and $W$ (4.5; it is what makes the dual terms of Lemma lem:dfg21 the groups
$H^1_f(\Q_p,T^D)^*$), the canonical splitting of $H^1(\Q_q,\Z_\ell(1))$ given by the uniformiser $q$ (5.3), and the toy examples
9.4 and 10.5 (class field theory of $\Q$ recovered from Greenberg-Wiles and from the relaxing sequence).

____

## 1. Line-up, Section 1: Galois cohomology of a field; Hilbert 90; Kummer theory

### 1.1 `conv:galcoh:galois-cohomology` (convention and definition) P
For a field $K$ and a discrete $G_K$-module $M$ (every element has open stabiliser), $H^n(K,M)=H^n(G_K,M)=
\varinjlim_LH^n(\Gal(L/K),M^{G_L})$ over finite Galois $L/K$ inside $\overline K$, with inflation as transition maps (Chapter 16,
continuous-cohomology (D)); for $M$ of type (C) or (V), continuous cochains. $H^0(K,M)=M^{G_K}$. For $K\subset L\subset\overline K$:
restriction $H^n(K,M)\to H^n(L,M)$; for $L/K$ Galois, inflation-restriction (Chapter 16) reads
$0\to H^1(\Gal(L/K),M^{G_L})\to H^1(K,M)\to H^1(L,M)^{\Gal(L/K)}$. Conventions C1 to C6 are fixed here.
Reference: Serre, Galois Cohomology (`SerreGaloisCoh`, see 14.5), Chapter I, Section 2 and Chapter II, Section 1; NSW,
Chapter I. Paper: background for every cohomology group of the paper.

### 1.2 `ex:galcoh:galois-modules` (definitions and examples) P
Discrete $G_K$-modules: $\overline K$ (additive), $\overline K^\times$, $\mu_n=\mu_n(\overline K)$ (always with $\operatorname{char}K\nmid n$), $\Z/n$ (trivial action), $\Z/n(r)=\mu_n^{\otimes r}$, $E[n]=E(\overline K)[n]$ for an elliptic curve $E/K$ with
$\operatorname{char}K\nmid n$ (Chapter 9), $E(\overline K)$ itself. Type (C): $\Z_\ell(1)$, on which $\sigma$ acts by $\chi_\ell(\sigma)\in\Z_\ell^\times$ (Chapter 5,
cyclotomic character), $T_\ell E$; type (D, $\ell$-primary): $\mu_{\ell^\infty}=\Q_\ell/\Z_\ell(1)$, $E[\ell^\infty]$. For $K$ finite, $G_K\simeq\hat\Z$
generated by the Frobenius $x\mapsto x^{\#K}$. Reference: Serre, Local Fields, Chapter X, Section 1 (cite the chapter). Paper:
background.

### 1.3 `thm:galcoh:hilbert90` (theorem, Hilbert's Theorem 90 in cohomological form) P
For every field $K$: (i) $H^1(K,\overline K^\times)=0$; (ii) $H^1(K,\overline K)=0$ (additive; $H^n(K,\overline K)=0$ for all $n\ge1$, the
latter stated); (iii) for every finite Galois $L/K$, $H^1(\Gal(L/K),L^\times)=0$ and $H^1(\Gal(L/K),L)=0$; (iv) the same for every (possibly infinite)
Galois $L/K$, with continuous cochains and $L^\times$ discrete (for instance $L=\bar k(C)$ over $K=k(C)$ for a curve $C/k$, Chapter 8, 4.2(iii)). Proof: (iii) is Chapter 5,
galois:hilbert90 (c), recalled with its proof idea (Dedekind independence of characters; normal basis for the additive
case); (i), (ii), (iv) follow by the direct limit 1.1 over the finite Galois subextensions (each term vanishes). Reference: Serre, Local Fields, Chapter X, Section 1
(Proposition 2 there, check); `SerreGaloisCoh`, Chapter II, Section 1. Paper: through 1.4 (Lemmas lem:tamagawa-exp and
lem:tamfactor).

### 1.4 `thm:galcoh:kummer` (theorem, Kummer theory in cohomological form) P
Let $n\ge1$ with $\operatorname{char}K\nmid n$. The sequence $1\to\mu_n\to\overline K^\times\xrightarrow{x\mapsto x^n}\overline K^\times\to1$ is an exact sequence of
discrete $G_K$-modules ($X^n-a$ is separable, so it has a root in $\overline K$). Its long exact sequence and 1.3(i) give:
(i) the connecting map $\delta\colon K^\times/(K^\times)^n\to H^1(K,\mu_n)$, $\delta(a)=[\sigma\mapsto\sigma(\alpha)/\alpha]$ with $\alpha^n=a$, is an
isomorphism of groups, natural in $K$; (ii) $H^2(K,\mu_n)\simeq\operatorname{Br}(K)[n]$, the $n$-torsion of $\operatorname{Br}(K):=H^2(K,\overline K^\times)$;
(iii) if $\mu_n\subset K$, then $H^1(K,\mu_n)=\Hom_{\mathrm{cont}}(G_K,\mu_n)$ and $\delta(a)$ is the Kummer character $\chi_a$ of Chapter 5,
recovering galois:kummer-classification (c) with the hypothesis $\mu_n\subset K$ removed from (i). (iv) (Restriction and
corestriction, stated.) For finite $L/K$: $\operatorname{res}\circ\delta_K=\delta_L\circ(K^\times/n\to L^\times/n)$ (proved: same cocycle) and
$\operatorname{cor}\circ\delta_L=\delta_K\circ N_{L/K}$ (stated; Serre, Local Fields, Chapter XIV). Reference: Serre, Local Fields,
Chapter X, Section 3; `SerreGaloisCoh`, Chapter II, Section 1; NSW, Chapter VI, Section 2 (cite chapters). Paper: Lemma
lem:tamfactor ("$H^1(G,\Z_\ell(1))=\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}$", via 2.4), Lemma lem:tamagawa-exp (via 5.6).

### 1.5 `def:galcoh:kummer-class` (definition and proposition) P
The **Kummer map** of $K$ is $\delta$ of 1.4; $\delta(a)$ is the **Kummer class** of $a$ in $H^1(K,\mu_n)$, and a cocycle
$\sigma\mapsto\sigma(\alpha)/\alpha$ is a **Kummer cocycle** of $a$ (it depends on the root $\alpha$: another root $\zeta\alpha$ changes it by the
coboundary $\sigma\mapsto\sigma(\zeta)/\zeta$). (i) $\delta(a)|_{G_L}=0$ iff $a\in(L^\times)^n$, for every separable $L\supseteq K$ (by 1.4(i) for $L$).
(ii) For $\mu_n\subset K$ the kernel of $\delta(a)$ is $G_{K(\alpha)}$, so $K(\alpha)/K$ is cyclic of degree the order of $a$ in $K^\times/K^{\times n}$
(Chapter 5). (iii) Compatibility with Chapter 7, 6.1(i): for a compatible system $(a^{1/\ell^k})_k$ the $\ell$-adic Kummer cocycle
$\kappa_a(\sigma)=(\sigma(a^{1/\ell^k})/a^{1/\ell^k})_k\in\Z_\ell(1)$ reduces modulo $\ell^k$ to a Kummer cocycle of $a$ in $H^1(K,\mu_{\ell^k})$.
Reference: as 1.4. Paper: Lemma lem:tamfactor ("$\kappa$ the Kummer class of $q_E$").

### 1.6 `ex:galcoh:kummer-finite-field` (worked example) P
$K=\F_q$, $\ell\nmid q$, $v=v_\ell(q-1)$, $G_K=\langle\Frob\rangle\simeq\hat\Z$. Two computations of $H^1(\F_q,\mu_{\ell^k})$ agree: Kummer (1.4)
gives $\F_q^\times/(\F_q^\times)^{\ell^k}$, cyclic of order $\ell^{\min(k,v)}$ (Chapter 2); the procyclic formula (Chapter 16, procyclic-discrete)
gives $\mu_{\ell^k}/(\Frob-1)\mu_{\ell^k}=\mu_{\ell^k}/\mu_{\ell^k}^{\,q-1}$, of the same order; the isomorphism between them is
$u\mapsto\delta(u)(\Frob)=\alpha^{q-1}$ ($\alpha^{\ell^k}=u$), that is $u\mapsto u^{(q-1)/\ell^k}$ for $k\le v$ (Chapter 5,
galois:kummer-finite-field (a)). In the limit: $H^1(\F_q,\Z_\ell(1))=\Z_\ell(1)/(q-1)\Z_\ell(1)\simeq\F_q^\times\otimes\Z_\ell\simeq\Z/\ell^v$, the second
isomorphism canonical, the third after choosing a generator; the class of $u$ has $v_\ell\ge k$ iff $u\in(\F_q^\times)^{\ell^k}$ ($k\le v$;
the class $0$ has $v_\ell=v$ by convention, important_notes.md point 31). Paper: Lemma lem:tamfactor ("$\Z_\ell(1)/(q-1)\simeq
\Z/\ell^{v_\ell(q-1)}$", "$c\in\Z/\ell^{v_\ell(q-1)}$ the class of $u$"), Section sec:tam.

### 1.7 `thm:galcoh:brauer` (theorem) R
(i) $\operatorname{Br}(K)=H^2(K,\overline K^\times)$; $\operatorname{Br}(\F_q)=0$ (stated; finite fields are $C_1$), $\operatorname{Br}(\R)=\Z/2$, $\operatorname{Br}(\C)=0$. (ii) For $K$
finite over $\Q_p$, the invariant map $\operatorname{inv}_K\colon\operatorname{Br}(K)\xrightarrow{\sim}\Q/\Z$ is an isomorphism (local class field theory; Chapter 7,
6.5), and with 1.4(ii) $H^2(K,\mu_n)\simeq\Z/n$ canonically; $\operatorname{inv}$ is compatible with restriction (multiplication by $[L:K]$)
and corestriction (identity). (iii) For $\Q$: $0\to\operatorname{Br}(\Q)\to\bigoplus_v\operatorname{Br}(\Q_v)\xrightarrow{\sum\operatorname{inv}_v}\Q/\Z\to0$ is exact
(Albert-Brauer-Hasse-Noether), with $\operatorname{inv}_\infty\colon\operatorname{Br}(\R)\simeq\frac12\Z/\Z$. Reference: Serre, Local Fields, Chapters X, XII, XIII
(cite chapters); Cassels-Frohlich, Chapter VI (Serre's "Local class field theory") and Chapter VII (Tate's "Global class
field theory"); `SerreGaloisCoh`, Chapter II, Section 5. Paper: background (the target $H^2(\Q_p,\mu)=\Q/\Z$ of the local
pairing in 3.3; (iii) is the reciprocity law behind 9.2 and 10.1).

## 2. Line-up, Section 2: $\ell$-adic coefficients: $T$, $V$, $W$, Kummer duals, and $H^1(K,\Z_\ell(1))$

### 2.1 `def:galcoh:kummer-duals` (definition and proposition) P
With C3, C4: (i) the evaluation pairings $T\times T^D\to\Z_\ell(1)$, $V\times V^D\to\Q_\ell(1)$, $W\times T^D\to\Q_\ell/\Z_\ell(1)$, $T\times W^D\to\Q_\ell/\Z_\ell(1)$ and,
for finite $M$, $M\times M^*(1)\to\mu_{\ell^\infty}$ are perfect and $G$-equivariant ($G$ acting on $\Hom$ by $(g\varphi)(x)=g\varphi(g^{-1}x)$);
(ii) $(T/\ell^kT)^*(1)\simeq T^D/\ell^kT^D$, compatibly with $W[\ell^k]=T/\ell^kT$ and $W^D[\ell^k]=T^D/\ell^kT^D$; (iii) $(T^D)^D=T$,
$(W^D)$ is the Kummer dual of $T$ and $T^D$ that of $W$; (iv) examples: $\Z_\ell^D=\Z_\ell(1)$, $\Z_\ell(1)^D=\Z_\ell$, $(T_\ell E)^D\simeq T_\ell E$ by
the Weil pairing (Chapter 9, 5.3, 5.5), $E[n]^*(1)\simeq E[n]$. Reference: Chapter 3, 8.1 to 8.3 (algebra); Rubin, Euler Systems,
Section 1.1. Paper: Section 4.2 ($T^D$, $V^D$, $W^D$), Lemma lem:dfg21. (Chapter 18 adds the adjoint-specific $T^D\simeq A(1)$.)

### 2.2 `prop:galcoh:tvw` (proposition; the cohomology of $T$, $V$, $W$) P
Let $G$ be a profinite group and $T$ as in C4 such that $H^1(G,T/\ell T)$ and $H^2(G,T/\ell T)$ are finite (true for $G=G_{\Q_p}$,
3.1, and $G=G_{\Q,S}$, 6.3; for $G=G_{\F_q}$, $G_\R$). Then: (i) $H^n(G,T)$ is a finitely generated $\Z_\ell$-module for $n=1,2$ and
$H^n(G,V)=H^n(G,T)\otimes\Q_\ell$ (Chapter 16, h1-finitely-generated, tate-limits). (ii) **Torsion of $H^1(G,T)$.** The sequence
$H^0(G,V)\to H^0(G,W)\xrightarrow{\delta}H^1(G,T)\xrightarrow{\iota}H^1(G,V)$ is exact, $\ker\iota=H^1(G,T)_{\mathrm{tors}}$, and the image of
$H^0(G,V)$ in $H^0(G,W)$ is $H^0(G,T)\otimes\Q_\ell/\Z_\ell$, the maximal divisible subgroup $H^0(G,W)_{\mathrm{div}}$; hence
$$H^1(G,T)_{\mathrm{tors}}\ \simeq\ H^0(G,W)/H^0(G,W)_{\mathrm{div}},$$
and if $H^0(G,V)=0$ then $H^0(G,W)$ is finite and $\delta\colon H^0(G,W)\xrightarrow{\sim}H^1(G,T)_{\mathrm{tors}}$. (iii) **Divisible part of $H^1(G,W)$.**
$0\to H^1(G,T)\otimes\Q_\ell/\Z_\ell\to H^1(G,W)\to H^2(G,T)_{\mathrm{tors}}\to0$ is exact; the first term is the image of $\pi\colon H^1(G,V)\to H^1(G,W)$ and
equals $H^1(G,W)_{\mathrm{div}}$; $H^1(G,W)$ is cofinitely generated of corank $\operatorname{rank}H^1(G,T)=\dim H^1(G,V)$. (iv) **Finite levels.**
For each $k$: $0\to H^{n-1}(G,T)/\ell^k\to H^{n-1}(G,T/\ell^kT)\to H^n(G,T)[\ell^k]\to0$ and $0\to H^{n-1}(G,W)/\ell^k\to H^n(G,W[\ell^k])\to H^n(G,W)[\ell^k]\to0$
are exact (long exact sequences of $T\xrightarrow{\ell^k}T$ and $W[\ell^k]\to W\xrightarrow{\ell^k}W$, Chapter 16, les-continuous (iii), (iv)).
Proof of the key steps: a finite-index divisible subgroup of a cofinitely generated $\Z_\ell$-module is its maximal divisible
subgroup; $\ker(H^1(G,T)\to H^1(G,T)\otimes\Q_\ell)$ is the torsion of a finitely generated module. Reference: Rubin, Euler Systems,
Section 1.2 and Appendix B; Tate95, Section 2 (cite sections). Paper: the paragraph after Lemma lem:dfg21 ("$H^1_f(\Q_p,T^D)$ is
the torsion of $H^1(\Q_p,T^D)$, a finite group", with 4.6), Lemma lem:h0 and Remark rem:ns ($H^0(\Q,W^D)$ finite when $H^0(\Q,V^D)=0$,
used in 10.3), Chapter 18 (the FPR sequence).

### 2.3 `ex:galcoh:tvw-examples` (worked examples) P
(a) $G=G_{\F_q}$, $T=\Z_\ell(1)$: $H^0(G,V)=0$, $H^0(G,W)=\mu_{\ell^\infty}(\F_q)$ of order $\ell^{v_\ell(q-1)}$, and $H^1(G,T)=\Z_\ell(1)/(q-1)$ is
all torsion, $\simeq H^0(G,W)$ as 2.2(ii) predicts. (b) $G=G_\R$, $\ell$ odd, any $T$: all $H^n$, $n\ge1$, vanish (6.4) and $H^0(\R,W)=
W^{c=1}$ is divisible: $H^1(\R,T)_{\mathrm{tors}}=0$. (c) $G=G_{\Q_p}$, $p\ne\ell$, $T=\Z_\ell(1)$: by 2.5, $H^1(\Q_p,\Z_\ell(1))_{\mathrm{tors}}=\Z_p^\times\otimes\Z_\ell$,
of order $\ell^{v_\ell(p-1)}=\#\mu_{\ell^\infty}(\Q_p)=\#H^0(\Q_p,\Q_\ell/\Z_\ell(1))$, as 2.2(ii) predicts. Paper: background (checks of 2.2).

### 2.4 `thm:galcoh:kummer-ladic` (theorem) P
For every field $K$ with $\operatorname{char}K\ne\ell$: (i) $H^1(K,\Z_\ell(1))\simeq\widehat{K^\times}:=\varprojlim_kK^\times/(K^\times)^{\ell^k}$ (transition maps the
projections), the class of $a\in K^\times$ being $\kappa_a=(\delta_k(a))_k$, represented by the $\ell$-adic Kummer cocycle of 1.5(iii) (Chapter 5,
galois:l-adic-kummer; Chapter 7, 6.1). (ii) $H^1(K,\Q_\ell/\Z_\ell(1))\simeq K^\times\otimes\Q_\ell/\Z_\ell$ (direct limit over $K^\times/(K^\times)^{\ell^k}$ with
transition maps $a\mapsto a^\ell$). (iii) $\kappa_{ab}=\kappa_a+\kappa_b$; $\kappa_a=0$ iff $a\in\bigcap_k(K^\times)^{\ell^k}$; the restriction of $\kappa_a$ to $G_L$ is
$\kappa_a$ for $L$. Proof: (i) Chapter 16, tate-limits (i): $H^1(K,\Z_\ell(1))=\varprojlim_kH^1(K,\mu_{\ell^k})$ because the $H^0(K,\mu_{\ell^k})$ are finite,
plus 1.4(i) at each level and the check that $\mu_{\ell^{k+1}}\to\mu_{\ell^k}$, $\zeta\mapsto\zeta^\ell$, induces the projection on the Kummer
side ($\beta=\alpha^\ell$ is an $\ell^k$-th root of $a$ when $\alpha$ is an $\ell^{k+1}$-th root); (ii) cohomology of discrete modules commutes with
direct limits, and $\mu_{\ell^k}\subset\mu_{\ell^{k+1}}$ induces $a\mapsto a^\ell$. Reference: Rubin, Euler Systems, Section 1.6 (check); NSW,
Chapter II, Section 7. Paper: Lemma lem:tamfactor ("$\kappa$ the Kummer class of $q_E$ in $H^1(G,\Z_\ell(1))=\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}$").

### 2.5 `ex:galcoh:kummer-local` (proposition and worked example) P
Let $K$ be finite over $\Q_p$, $\ell\ne p$, residue field $\F_q$, valuation $v_K$, $\mathcal O_K^\times$ the units. (i) (Chapter 7, 2.7(v), recalled.)
$0\to\mathcal O_K^\times\otimes\Z_\ell\to\widehat{K^\times}\xrightarrow{v_K}\Z_\ell\to0$ is exact, $\mathcal O_K^\times\otimes\Z_\ell\simeq\F_q^\times\otimes\Z_\ell\simeq\Z/\ell^{v_\ell(q-1)}$; so
$H^1(K,\Z_\ell(1))\simeq\Z_\ell\times\Z/\ell^{v_\ell(q-1)}$ with torsion the unit classes. (ii) $H^1(K,\mu_{\ell^k})$ has order $\ell^k\cdot\#\mu_{\ell^k}(K)=
\ell^{k+\min(k,v_\ell(q-1))}$. (iii) $H^1(K,\Q_\ell/\Z_\ell(1))\simeq\Q_\ell/\Z_\ell$ via $v_K$ ($\mathcal O_K^\times\otimes\Q_\ell/\Z_\ell=0$: the units are a finite group times
a pro-$p$ group). (iv) $H^1(K,\Q_\ell(1))\simeq\Q_\ell$, spanned by the class of a uniformiser. Numerical instances (checked): $\Q_7$, $\ell=3$:
$H^1(\Q_7,\Z_3(1))\simeq\Z_3\times\Z/3$; $\Q_{19}$, $\ell=3$: $\Z_3\times\Z/9$; $\Q_{11}$, $\ell=5$: $\Z_5\times\Z/5$; $\Q_5$, $\ell=3$: $\Z_3$ (every unit of
$\Z_5$ is a cube). Paper: Lemma lem:tamfactor (the group $H^1(G,\Z_\ell(1))$ in which $\kappa$ lives), Section sec:tam.

## 3. Line-up, Section 3: local Galois cohomology: finiteness, Euler characteristic, Tate local duality

Throughout this section $K$ is a finite extension of $\Q_p$ (the paper needs only $K=\Q_p$), $M$ a finite discrete $G_K$-module,
$M'=M^*(1)=\Hom(M,\mu)$ its Kummer dual ($\mu$ = all roots of unity in $\overline K$).

### 3.1 `thm:galcoh:local-finiteness` (theorem) R (with a sketch for $p\nmid\#M$)
(i) $H^n(K,M)$ is finite for all $n$ and $H^n(K,M)=0$ for $n\ge3$ ($\operatorname{cd}G_K=2$). (ii) Consequently, for $T$ of type (C),
$H^n(K,T)$ is a finitely generated $\Z_\ell$-module ($n\ge0$), $H^n(K,V)$ is finite-dimensional, $H^n(K,W)$ is cofinitely generated,
and 2.2 applies with $G=G_K$. Sketch for $p\nmid\#M$ and $n\le1$ (the only case the paper uses): $M$ is trivial on an open
normal subgroup $G_L$; inflation-restriction reduces $H^1$ to $\Hom_{\mathrm{cont}}(G_L,M)^{\Gal(L/K)}$, and a continuous homomorphism
$G_L\to M$ of order prime to $p$ factors through $G_L^{\mathrm{ab}}/(\text{wild part})$, which by Chapter 7 (5.3, 5.4) is topologically
generated by two elements (a Frobenius and a generator of tame inertia), so there are finitely many. Reference: `SerreGaloisCoh`,
Chapter II, Section 5 (cite the section); NSW, Chapter VII, Section 2; MilneADT, Chapter I, Section 2. Paper: the paragraph after
Lemma lem:dfg21 ("a finite group"), Lemma lem:fpr (Chapter 18), and through 2.2.

### 3.2 `thm:galcoh:local-euler` (theorem, Tate's local Euler-Poincare characteristic formula) R
$\dfrac{\#H^0(K,M)\,\#H^2(K,M)}{\#H^1(K,M)}=\bigl|\#M\bigr|_K=p^{-[K:\Q_p]\,v_p(\#M)}$. In particular the left side is $1$ when $p\nmid\#M$.
$\ell$-adic form: $\dim H^0(K,V)-\dim H^1(K,V)+\dim H^2(K,V)=-[K:\Q_p]\dim V$ if $\ell=p$ and $=0$ if $\ell\ne p$.
Reference: `SerreGaloisCoh`, Chapter II, Section 5.7 (check); MilneADT, Chapter I, Section 2 (Theorem 2.8 there, check); NSW,
Chapter VII, Section 3. Paper: through 4.4 (the exact orthogonality of unramified classes), 9.3.

### 3.3 `thm:galcoh:tate-local-duality` (theorem, Tate local duality) R
(i) For $0\le i\le2$ the cup product (Chapter 16) followed by $M\otimes M'\to\mu$ and $\operatorname{inv}_K$ (1.7(ii)),
$$H^i(K,M)\times H^{2-i}(K,M')\longrightarrow H^2(K,\mu)\xrightarrow{\ \operatorname{inv}_K\ }\Q/\Z,$$
is a perfect pairing of finite groups; it is natural in $M$, compatible with connecting maps (up to the sign $(-1)^i$) and
with restriction and corestriction. (ii) ($\ell$-adic forms, by passage to the limit with 2.1(ii).) For $T$ as in C4 and $0\le i\le2$
there are perfect pairings $H^i(K,W)\times H^{2-i}(K,T^D)\to\Q_\ell/\Z_\ell$ (identifying the discrete group $H^i(K,W)$ with the Pontryagin
dual of the compact $H^{2-i}(K,T^D)$), $H^i(K,T)\times H^{2-i}(K,W^D)\to\Q_\ell/\Z_\ell$, and $H^i(K,V)\times H^{2-i}(K,V^D)\to\Q_\ell$ (perfect
pairing of finite-dimensional $\Q_\ell$-vector spaces). (iii) (Compatibility.) For $x\in H^1(K,V)$, $y\in H^1(K,T^D)$:
$\langle\pi x,y\rangle_{W,T^D}=\bigl(\langle x,\iota y\rangle_{V,V^D}\bmod\Z_\ell\bigr)$; and symmetrically with the roles of $(T,V,W)$ and $(T^D,V^D,W^D)$
exchanged. Reference: `SerreGaloisCoh`, Chapter II, Section 5.2 (check); TateDuality; MilneADT, Chapter I, Section 2 (Corollary
2.3 there, check); NSW, Chapter VII, Section 2; for (ii), (iii) Rubin, Euler Systems, Section 1.4 (cite the section). Paper:
Lemma lem:dfg21 (the Pontryagin duals $H^1_f(\Q_p,T^D)^*$ are the duals of $H^1(\Q_p,W)/H^1_f(\Q_p,W)$, through 4.5 and 10.3).

### 3.4 `cor:galcoh:local-duality-consequences` (corollary) P (given 3.2, 3.3)
(i) $H^2(K,M)\simeq H^0(K,M')^*$; $H^2(K,\mu_{\ell^k})\simeq\Z/\ell^k$; $H^2(K,\Z/\ell^k)\simeq\mu_{\ell^k}(K)^*$. (ii) For $\ell\ne p$:
$\#H^1(K,M)=\#H^0(K,M)\,\#H^0(K,M')$ and $\dim H^1(K,V)=\dim H^0(K,V)+\dim H^0(K,V^D)$. (iii) For $\ell\ne p$ and $T$ as in C4:
$H^2(K,T)\simeq H^0(K,W^D)^*$, finite if $H^0(K,V^D)=0$. Examples: $\dim H^1(\Q_p,\Q_\ell)=1$ ($p\ne\ell$; all classes unramified),
$\dim H^1(\Q_p,\Q_\ell(1))=1$ (2.5(iv)); for $E/\Q_p$ and $\ell\ne p$, $\#H^1(\Q_p,E[\ell])=\#E(\Q_p)[\ell]^2$ (by 2.1(iv)). Paper: background;
4.4, 4.6.

### 3.5 `ex:galcoh:local-orders` (worked example) P
(a) $\ell\ne p$, $v=v_\ell(p-1)$, $m=\min(k,v)$: $\#H^i(\Q_p,\Z/\ell^k)=\ell^k,\ \ell^{k+m},\ \ell^m$ and $\#H^i(\Q_p,\mu_{\ell^k})=\ell^m,\ \ell^{k+m},\ \ell^k$ for
$i=0,1,2$ (Kummer 2.5(ii); $\Hom(G_{\Q_p},\Z/\ell^k)=\Hom(\widehat{\Q_p^\times},\Z/\ell^k)$ by Chapter 7, 6.5; and 3.4(i)): Euler characteristic $1$ and
duality visible. (b) $p$ odd, $M=\mu_p$ over $\Q_p$: $\#H^0=1$, $\#H^1=\#\Q_p^\times/(\Q_p^\times)^p=p^2$, $\#H^2=p$, characteristic $p^{-1}=|p|_p$.
(c) 11a1 over $\Q_{11}$, $\ell=5$: the Tate parameter $q_E=11^5u$ with $\bar u=-1\in(\F_{11}^\times)^5$ is a fifth power in $\Q_{11}$ and
$\mu_5\subset\Q_{11}$, so $E[5]\subset E(\Q_{11})$ (all $12$ roots of the $5$-division polynomial lie in $\Q_{11}$ with rational $y$; checked
with PARI) and $\#H^1(\Q_{11},E[5])=5^4$. Paper: background; Chapter 16, Exercise 10 and Section sec:tam (11a1 at $\ell=5$, an
Eisenstein illustration only: $E(\Q)_{\mathrm{tors}}=\Z/5$).

## 4. Line-up, Section 4: unramified cohomology

In this section $p$ is a prime, $G=G_{\Q_p}$, $I=I_p$, $\Frob$ an arithmetic Frobenius, and $M$ a $G$-module of type (D, torsion),
(C) or (V). Statements (iv) of 4.2, 4.4 and 4.6 need $p\ne\ell$.

### 4.1 `def:galcoh:unramified` (definition and proposition) P
$H^1_{\mathrm{ur}}(\Q_p,M):=\operatorname{im}\bigl(\operatorname{inf}\colon H^1(G/I,M^I)\to H^1(\Q_p,M)\bigr)=\ker\bigl(\operatorname{res}\colon H^1(\Q_p,M)\to H^1(I,M)\bigr)$; inflation is
injective, so $H^1_{\mathrm{ur}}(\Q_p,M)\simeq H^1(G/I,M^I)$ (Chapter 16, inflation-restriction (a), continuous-cochain version). Classes in
$H^1_{\mathrm{ur}}$ are called unramified; $M$ is unramified if $I$ acts trivially. The definition is made for every $p$, including
$p=\ell$, where it is not the Bloch-Kato condition (Chapter 18). Reference: Rubin, Euler Systems, Section 1.3; `SerreGaloisCoh`,
Chapter II, Section 5.5. Paper: the paragraph after Lemma lem:dfg21 ("$H^1_f(\Q_p,V^D)=H^1_{\mathrm{ur}}(\Q_p,V^D)$", the
identification $H^1_f=H^1_{\mathrm{ur}}$ at $p\ne\ell$ being Chapter 18's), Lemma lem:tamfactor ($H^1(G/I,\Z_\ell(1)^I)$).

### 4.2 `prop:galcoh:unramified-computed` (proposition) P
(i) $c\mapsto c(\Frob)$ induces $H^1_{\mathrm{ur}}(\Q_p,M)\simeq M^I/(\Frob-1)M^I$ (Chapter 16: procyclic-compact for (C), (V), procyclic-discrete for
torsion (D), applied to $\Gamma=G/I\simeq\hat\Z$; $M^I$ is closed, of the same type). (ii) For $M$ finite, $\#H^1_{\mathrm{ur}}(\Q_p,M)=\#H^0(\Q_p,M)$.
(iii) For $V$: $\dim H^1_{\mathrm{ur}}(\Q_p,V)=\dim H^0(\Q_p,V)$, and the following are equivalent: $H^1_{\mathrm{ur}}(\Q_p,V)=0$; $H^0(\Q_p,V)=0$; $1$ is
not an eigenvalue of $\Frob$ on $V^I$; $\det(1-\Frob\mid V^I)\ne0$; $\det(1-\Phi\mid V^I)\ne0$ (the last two because
$\det(1-\Phi)=(-1)^d\det(\Phi)\det(1-\Frob)$ on $V^I$, $d=\dim V^I$). (iv) For $T$ with $V=T\otimes\Q_\ell$: $T^I=T\cap V^I$ is a saturated
sublattice of $V^I$; $H^1_{\mathrm{ur}}(\Q_p,T)=T^I/(\Frob-1)T^I$; if the conditions of (iii) hold, it is finite of order
$\ell^{v_\ell(\det(1-\Frob\mid V^I))}=\ell^{v_\ell(\det(1-\Phi\mid V^I))}$ (cokernel of an injective endomorphism of a free $\Z_\ell$-module, Chapter 3;
$\det\Phi$ is a unit on the lattice $T^I$). Reference: Rubin, Euler Systems, Lemma 1.3.2 and Section 1.3 (check); Chapter 16. Paper: the
paragraph after Lemma lem:dfg21 ("$(V^D)^{I_p}/(\Frob_p-1)$ vanishes because $\det(1-\Frob_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}\ne0$": the
vanishing is (iii) and does not depend on the Frobenius convention; the identification of the determinant with $L_p(A_f,1)^{-1}$
needs $\Phi$, important_notes.md point 11, and is Chapter 18/19's), Lemma lem:fpr (Chapter 18 uses (iv): the Euler factor
$\ell^{v_\ell(L_p(A_f,1)^{-1})}$ is the order of $H^1_{\mathrm{ur}}(\Q_p,T^D)$).

### 4.3 `prop:galcoh:ur-sequence` (proposition) P (given Chapter 16)
For $M$ of type (D, torsion), (C) or (V):
$$0\to H^1_{\mathrm{ur}}(\Q_p,M)\to H^1(\Q_p,M)\xrightarrow{\operatorname{res}}H^1(I,M)^{G/I}\to0$$
is exact, where $G/I$ acts on $H^1(I,M)$ by the conjugation action of Chapter 16 ($(\sigma\cdot c)(i)=\sigma c(\sigma^{-1}i\sigma)$). Proof: the
five-term sequence (Chapter 16, inflation-restriction (b)) ends with $H^2(G/I,M^I)$, which vanishes for $G/I\simeq\hat\Z$ and these
coefficients (Chapter 16, procyclic-discrete and procyclic-compact (iii), the latter applying because $\hat\Z$ surjects onto $\Z_\ell$).
For $p\ne\ell$ and $M$ of type (C), $H^1(I,M)$ is computed through the tame quotient (Chapter 16, tame-inertia-example).
Remark (forward): taking torsion subgroups in this sequence for $M=T^D$ is the first step of the Fontaine-Perrin-Riou formula,
and $\Fitt_{\Z_\ell}\bigl((H^1(I,M)_{\mathrm{tors}})^{G/I}\bigr)$ is the Tamagawa factor $\Tam_p(M)$ (Chapter 18; the superscript $G$ applies to the
module, not to the ideal: important_notes.md point 37). Reference: Rubin, Euler Systems, Section 1.3; FPR94, I.4. Paper: Section 1.2
(the object $H^1(I_p,M)_{\mathrm{tor}}^{G_{\Q_p}}$), Lemma lem:fpr and Lemma lem:tamfactor (through Chapters 16, 18).

### 4.4 `thm:galcoh:ur-orthogonal` (theorem, exact orthogonality of unramified classes) P (given 3.2, 3.3)
Let $p\ne\ell$. (i) For $M$ finite of $\ell$-power order and $M'=M^*(1)$, $H^1_{\mathrm{ur}}(\Q_p,M)$ and $H^1_{\mathrm{ur}}(\Q_p,M')$ are exact annihilators
of each other under the pairing of 3.3(i). (ii) For $V$ and $V^D$, $H^1_{\mathrm{ur}}(\Q_p,V)^\perp=H^1_{\mathrm{ur}}(\Q_p,V^D)$ under 3.3(ii). Proof (to be
written in full): the cup product of two inflated classes is inflated from $H^2(G/I,\mu_{\ell^\infty})=0$ (resp. $H^2(G/I,\Q_\ell(1))=0$),
so the two subgroups are orthogonal; by 4.2(ii), 3.4(i) and 3.2, $\#H^1_{\mathrm{ur}}(M)\cdot\#H^1_{\mathrm{ur}}(M')=\#H^0(M)\,\#H^0(M')=\#H^0(M)\,\#H^2(M)
=\#H^1(M)$, so each is the full annihilator of the other; (ii) the same count with dimensions (4.2(iii), 3.4(ii)). Warning (the
case $p=\ell$, checked): over $\Q_p$, $p$ odd, $\#H^1_{\mathrm{ur}}(\Q_p,\Z/p)=p$ and $\#H^1_{\mathrm{ur}}(\Q_p,\mu_p)=\#H^0(\Q_p,\mu_p)=1$, while $\#H^1(\Q_p,\Z/p)=
p^2$: the unramified subgroups are not exact annihilators at $p=\ell$ (the annihilator of $H^1_{\mathrm{ur}}(\Q_p,\Z/p)$ is the image of the
units in $\Q_p^\times/(\Q_p^\times)^p$, of order $p$); at $\ell$ the right local condition is Bloch-Kato's (Chapter 18). Reference:
`SerreGaloisCoh`, Chapter II, Section 5.5; MilneADT, Chapter I, Section 2 (Theorem 2.6 there, check); Rubin, Euler Systems, Section 1.4.
Paper: Lemma lem:dfg21 (through Chapter 18: $H^1_f(\Q_p,V)^\perp=H^1_f(\Q_p,V^D)$ for $p\ne\ell$ is exactly (ii)).

### 4.5 `prop:galcoh:propagation` (proposition, propagation of local conditions) P (given 3.3)
Let $K$ be a finite extension of $\Q_p$ (any $p$), $T$ as in C4. For a $\Q_\ell$-subspace $L_V\subseteq H^1(K,V)$ put $L_T:=\iota^{-1}(L_V)\subseteq
H^1(K,T)$ and $L_W:=\pi(L_V)\subseteq H^1(K,W)$ (the conditions **propagated** from $L_V$); likewise $L_{T^D},L_{W^D}$ from $L_{V^D}\subseteq
H^1(K,V^D)$. (i) $L_T\supseteq H^1(K,T)_{\mathrm{tors}}$; $L_W$ is divisible and $L_W\subseteq H^1(K,W)_{\mathrm{div}}$. (ii) If $L_V$ and $L_{V^D}$ are exact
annihilators under the $V$-pairing, then $L_W$ and $L_{T^D}$ are exact annihilators under $H^1(K,W)\times H^1(K,T^D)\to\Q_\ell/\Z_\ell$, so
$\bigl(H^1(K,W)/L_W\bigr)^*\simeq L_{T^D}$; and symmetrically $L_T$ and $L_{W^D}$. (iii) If $p\ne\ell$, $T$ is unramified and $L_V=H^1_{\mathrm{ur}}(K,V)$,
then $L_T=H^1_{\mathrm{ur}}(K,T)$ and $L_W=H^1_{\mathrm{ur}}(K,W)$ (so a propagated structure is unramified at every unramified $p\ne\ell$:
$H^1(I,T)=\Hom(I,T)$ is torsion-free, and $H^1_{\mathrm{ur}}(K,W)=W/(\Frob-1)W$ is divisible). Proof of (ii): if $y\in L_{T^D}$ then
$\langle\pi x,y\rangle=\langle x,\iota y\rangle\bmod\Z_\ell=0$ for $x\in L_V$ (3.3(iii)); conversely if $y\perp L_W$, then $\langle\ell^{-k}x,\iota y\rangle\in\Z_\ell$ for
all $k$ and all $x\in L_V$, so $\langle x,\iota y\rangle=0$, $\iota y\in L_V^\perp=L_{V^D}$, $y\in L_{T^D}$; perfectness of the $(W,T^D)$ pairing
finishes. Reference: Rubin, Euler Systems, Section 1.3 (propagation, check); MazurRubin04, Section 1.1 (check); Bloch-Kato,
Section 3 (for the Bloch-Kato case). Paper: Lemma lem:dfg21 ("$H^1_f(\Q_p,T^D)=\iota^{-1}H^1_f(\Q_p,V^D)$" is a propagated condition, and
the dual terms $H^1_f(\Q_p,T^D)^*$ are the quotients $H^1(\Q_p,W)/H^1_f(\Q_p,W)$, by (ii)); Chapter 18 (the Bloch-Kato conditions on $T$
and $W$ are defined this way).

### 4.6 `cor:galcoh:ur-vanishing` (corollary) P
Let $p\ne\ell$ and suppose $H^1_{\mathrm{ur}}(\Q_p,V)=0$ (4.2(iii)). Then $H^0(\Q_p,V)=0$, and for the propagated conditions of
$L_V=H^1_{\mathrm{ur}}(\Q_p,V)=0$: $L_T=\iota^{-1}(0)=H^1(\Q_p,T)_{\mathrm{tors}}\simeq H^0(\Q_p,W)$, a finite group (2.2(ii), 3.1), containing
$H^1_{\mathrm{ur}}(\Q_p,T)$ (finite by 4.2(iv)); and $L_W=0$. In the paper's situation, for $p\in\Sigma$ and $V=V^D=A_f(1)$:
"$H^1_f(\Q_p,T^D)$ is the torsion of $H^1(\Q_p,T^D)$, a finite group", and it is $\simeq H^0(\Q_p,W^D)$. Paper: the paragraph after
Lemma lem:dfg21 (exactly), Lemma lem:fpr (Chapter 18: $\len H^1_f(\Q_p,T^D)=\len H^0(\Q_p,W^D)$ is then split into the Euler factor and the
Tamagawa factor).

### 4.7 `ex:galcoh:ur-examples` (worked examples) P
(a) $T=\Z_\ell(1)$, $p\ne\ell$: $H^1_{\mathrm{ur}}(\Q_p,\Z_\ell(1))=\Z_\ell(1)/(p-1)$, which under 2.4 is the image of $\Z_p^\times$ (5.1). (b) $T=\Z_\ell$, $p\ne\ell$:
$H^1(\Q_p,\Z_\ell)=\Hom(G_{\Q_p},\Z_\ell)=\Z_\ell=H^1_{\mathrm{ur}}$, orthogonal to $H^1_{\mathrm{ur}}(\Q_p,\Q_\ell/\Z_\ell(1))=0$, consistent with 4.4. (c) Tate curve ($E$
multiplicative at $p\ne\ell$, Chapter 11, 3.2): $V^I=\Q_\ell e_1$ with $\Frob$-eigenvalue $\varepsilon p\ne1$, so $H^1_{\mathrm{ur}}(\Q_p,V_\ell E)=0$ and
$H^1(\Q_p,T_\ell E)_{\mathrm{tors}}\simeq E(\Q_p)[\ell^\infty]$. (d) $V=\ad V_\ell E$ at a multiplicative prime: $V^I=\Q_\ell e$ with $\Frob$-eigenvalue $p$; for
$V^D=V(1)$ the eigenvalue is $p^2$; $\det(1-\Phi\mid(V^D)^I)=1-p^{-2}$ (the paper's $L_p(A_f,1)^{-1}$ at a multiplicative prime) while
$\det(1-\Frob\mid(V^D)^I)=1-p^2$: different numbers, the same $\ell$-adic valuation, the same vanishing (point 11). (e) Type
$\mathrm{III}$ or $\mathrm{III}^*$ at $q\ge5$: $(\ad V)^{I}$ is a line on which $\Frob$ acts by $\chi_{-4}(q)$ (Chapter 19; Lemma lem:euler), so $(V^D)^I$ has
eigenvalue $q\chi_{-4}(q)$ and $\#H^1_{\mathrm{ur}}(\Q_q,T^D)=\ell^{v_\ell(q-\chi_{-4}(q))}=\ell^{e_\ell(E,q)}$. (f) Good prime: $V_\ell E$ unramified with eigenvalues
of absolute value $\sqrt p$, so $H^1_{\mathrm{ur}}(\Q_p,V_\ell E)=0$. Paper: the paragraph after Lemma lem:dfg21, Lemma lem:fpr ("of valuation
$e_\ell(E,p)$ at an additive prime and $v_\ell(1-p^{-2})$ at a multiplicative one"), Lemma lem:euler.

## 5. Line-up, Section 5: the Kummer class of the Tate parameter (the end of Lemma lem:tamfactor)

Throughout: $q\ne\ell$ primes, $\ell$ odd where stated, $G=G_{\Q_q}$, $I=I_q$, $v=v_\ell(q-1)$, $t_\ell\colon I\to\Z_\ell(1)$ the tame character
(Chapter 7, 5.3). This section proves, in corrected form, the last sentences of the paper's proof of Lemma lem:tamfactor.

### 5.1 `prop:galcoh:unit-classes` (proposition) P
Let $K$ be finite over $\Q_p$, $p\ne\ell$, with residue field $\F_q$. Under the Kummer isomorphisms 1.4 and 2.4:
(i) $H^1_{\mathrm{ur}}(K,\mu_{\ell^k})$ corresponds to the image of $\mathcal O_K^\times$ in $K^\times/(K^\times)^{\ell^k}$, and $H^1_{\mathrm{ur}}(K,\Z_\ell(1))$ to
$\mathcal O_K^\times\otimes\Z_\ell\subset\widehat{K^\times}$; (ii) the sequence 4.3 for $M=\Z_\ell(1)$ is the valuation sequence of 2.5(i):
$$0\to\mathcal O_K^\times\otimes\Z_\ell\to\widehat{K^\times}\xrightarrow{\ v_K\ }\Z_\ell\to0\quad\text{corresponds to}\quad0\to H^1_{\mathrm{ur}}(K,\Z_\ell(1))\to H^1(K,\Z_\ell(1))\xrightarrow{\operatorname{res}}\Hom(I_K,\Z_\ell(1))^{G/I}\to0,$$
via $\operatorname{res}\kappa_x=v_K(x)\,t_\ell$ (Chapter 7, 6.2(ii)), $\Hom(I_K,\Z_\ell(1))^{G/I}=\Z_\ell t_\ell$ ($t_\ell$ is $G$-equivariant by Chapter 7, 5.4(i); every
continuous homomorphism $I_K\to\Z_\ell(1)$ factors through $t_\ell$, Chapter 7, 5.3(iv)). Proof: units have all their $\ell$-power roots in
$K^{\mathrm{ur}}$ (Hensel, Chapter 7, 4.2(iv)), so their Kummer classes vanish on $I_K$; conversely a class with $\operatorname{res}=0$ has $v_K=0$ by
the displayed formula. Reference: `SerreGaloisCoh`, Chapter II, Section 5; Rubin, Euler Systems, Section 1.6 (check). Paper: Lemma
lem:tamfactor ("$\kappa$ ... $H^1(G/I,\Z_\ell(1)^I)$"), Lemma lem:tamagawa-exp (via 5.6).

### 5.2 `prop:galcoh:unramified-value` (proposition) P
With $K=\Q_q$: $\Z_\ell(1)^I=\Z_\ell(1)$ ($I$ acts trivially, $q\ne\ell$), and $c\mapsto c(\Frob)$ gives $H^1(G/I,\Z_\ell(1))\simeq\Z_\ell(1)/(q-1)\Z_\ell(1)$
(Chapter 16, procyclic-examples (ii)), a cyclic group of order $\ell^v$. For $u\in\Z_q^\times$ with Kummer cocycle $\kappa_u$ built from
$\ell$-power roots of $u$ in $\Q_q^{\mathrm{ur}}$: $\kappa_u$ is inflated from $G/I$ (as a cocycle, not only as a class), $\kappa_u(\Frob)$ depends only on
the image of $\Frob$ in $G/I$, and its class in $\Z_\ell(1)/(q-1)\simeq\mu_{\ell^v}(\F_q)$ is $\bar u^{(q-1)/\ell^v}$, i.e. the class of the reduction $\bar u$
in $\F_q^\times\otimes\Z_\ell=\F_q^\times/(\F_q^\times)^{\ell^v}$ (Chapter 5, galois:kummer-finite-field (b), applied to the reductions of the roots; Chapter 7,
6.2(iii)). Hence the composite $\Z_q^\times\otimes\Z_\ell\to H^1_{\mathrm{ur}}(\Q_q,\Z_\ell(1))\to\Z_\ell(1)/(q-1)$ is the isomorphism "reduce and take the class in
$\F_q^\times\otimes\Z_\ell$". After choosing a generator, $\Z_\ell(1)/(q-1)\simeq\Z/\ell^v$; $v_\ell$ of a class is well defined, with $v_\ell(0)=v$
(important_notes.md point 31). Paper: Lemma lem:tamfactor ("$H^1(G/I,\Z_\ell(1)^I)=\Z_\ell(1)/(q-1)\simeq\Z/\ell^{v_\ell(q-1)}$, the class of the unit part
of $q_E$ in $\F_q^\times\otimes\Z_\ell$ by Kummer theory").

### 5.3 `prop:galcoh:canonical-splitting` (proposition) P
For $K=\Q_q$ the prime $q$ is a canonical uniformiser, and $\Q_q^\times=q^{\Z}\times\Z_q^\times$ canonically. Hence
$$H^1(\Q_q,\Z_\ell(1))=\Z_\ell\,\kappa_q\ \oplus\ H^1_{\mathrm{ur}}(\Q_q,\Z_\ell(1))$$
canonically, and there is a canonical retraction $\operatorname{pr}_{\mathrm{ur}}\colon H^1(\Q_q,\Z_\ell(1))\to H^1_{\mathrm{ur}}(\Q_q,\Z_\ell(1))=H^1(G/I,\Z_\ell(1)^I)$ with
$\operatorname{pr}_{\mathrm{ur}}(\kappa_x)=\kappa_{x q^{-v_q(x)}}$: it sends the class of $x$ to the class of its unit part. This is the precise sense in which
"the image of $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)$" exists: not by a functorial map (inflation goes the other way, and over a general
$K$ the splitting depends on the uniformiser; important_notes.md point 7), but by the splitting attached to $q$. The value
$\kappa(\Frob)$ of a cocycle at a Frobenius lift is a different object (5.4(iii), (iv)). Paper: Lemma lem:tamfactor (the phrase
"$c'$ is the image of $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)$"); Part 16, N1.

### 5.4 `thm:galcoh:tate-kummer-class` (theorem; the identification of $c'$) P
Let $E/\Q$ have multiplicative reduction at $q$, $\ell\ne q$ odd, $q_E\in\Q_q^\times$ the Tate parameter, $n=v_q(q_E)=n_q$, $u=q_Eq^{-n}\in\Z_q^\times$ its
unit part, $\varepsilon\colon G\to\{\pm1\}$ the unramified character with $\varepsilon(\Frob)=a_q(E)$. Fix compatible systems of $\ell$-power roots of $q$
and of $u$ (the latter in $\Q_q^{\mathrm{ur}}$), give $q_E$ the product system, and let $\kappa=\kappa_{q_E}$, $\kappa_q$, $\kappa_u$ be the Kummer cocycles
(Chapter 7, 6.1). By Chapters 10 (7.5(iii)) and 11 (3.2) $T=T_\ell E$ has a basis $e_1,e_2$ in which
$\rho(g)=\begin{psmallmatrix}\chi_\ell(g)\varepsilon(g)&\varepsilon(g)\kappa(g)\\0&\varepsilon(g)\end{psmallmatrix}$ (the corner is $\varepsilon\kappa$, important_notes.md point 42). Then:
(i) $\kappa=n\kappa_q+\kappa_u$ as cocycles; in $H^1(\Q_q,\Z_\ell(1))$ the class of $\kappa$ is the Kummer class of $q_E$, and
$\operatorname{pr}_{\mathrm{ur}}[\kappa]=[\kappa_u]$ is the class of $\bar u$ in $\F_q^\times\otimes\Z_\ell$ (5.2, 5.3). (ii) $\kappa|_I=n\,t_\ell$; for a topological generator $t$ of
$I^{(\ell)}$ with $t_\ell(t)=\zeta$ (the generator of $\Z_\ell(1)$ used to write $\Z_\ell(1)=\Z_\ell$), $te_1=e_1$ and $te_2=e_2+ne_1$: the paper's $n'$ can be taken
equal to $n$, and in any case $v_\ell(n')=v_\ell(n)$. (iii) Let $\Frob_0$ be a Frobenius lift fixing the chosen $\ell$-power roots of $q$ (Chapter 7,
5.5). Then $\kappa_q(\Frob_0)=0$ and $\rho(\Frob_0)=\begin{psmallmatrix}\varepsilon q&c'\\0&\varepsilon\end{psmallmatrix}$ with $\varepsilon=a_q(E)$ and
$c'=\varepsilon\,\kappa_u(\Frob_0)$, whose class in $\Z_\ell(1)/(q-1)$ is $\pm$ the class of $\bar u$. (iv) For an arbitrary Frobenius lift $\Frob=\Frob_0\sigma$
($\sigma\in I$) and an arbitrary cocycle in the class of $\kappa$ (another system of roots), the corner $c'$ of $\rho(\Frob)$ changes by an element of
the ideal $(n,q-1)\Z_\ell$: $\kappa(\Frob_0\sigma)=\kappa(\Frob_0)+q\,n\,t_\ell(\sigma)$, and a coboundary changes the value at $\Frob$ by $(q-1)z$.
(v) Consequently
$$\min\bigl(v_\ell(n),v_\ell(q-1),v_\ell(c')\bigr)=v_\ell\bigl((n,q-1,c')\Z_\ell\bigr)=\min\bigl(v_\ell(n),v_\ell(q-1),v_\ell(c)\bigr),$$
with $c\in\Z/\ell^{v}$ the class of $\bar u$ (any generator; $v_\ell(0)=v$), independently of every choice; with Chapter 16, model-computation, this
completes the proof of the formula $v_\ell(\Tam_q(\ad T))=v_\ell(n)+\min(v_\ell(n),v_\ell(q-1),v_\ell(c))$ of Lemma lem:tamfactor (the identification of
$\Tam_q$ with the Fitting ideal of the invariants is Chapter 18's). Reference: SilvermanATAEC, Chapter V (Tate curve, cite the chapter);
SerreAbelian, Chapter IV, Appendix A.1 (cite the chapter); DDT, Theorem 3.1(e) as cited by the paper (check). Paper: Lemma
lem:tamfactor (end of the proof: "$c'$ is the image of $\kappa$ ... by Kummer theory, well defined modulo $q-1$; so $v_\ell(c')=v_\ell(c)$ in the sense
stated"; the true indeterminacy is the ideal $(n,q-1)$, which is harmless), Remark rem:ko(1), Section sec:tam.

### 5.5 `ex:galcoh:tate-kummer-examples` (worked examples; checked with PARI's `ellinit(E,O(q^30)).tate` and ecdata) P
At $\ell=3$, multiplicative primes $q\equiv1\pmod3$ with $3\mid n$; $c$ = class of $\bar u$ in $\F_q^\times/(\F_q^\times)^{3^{v_3(q-1)}}$; "extra" is
$\min(v_3(n),v_3(q-1),v_3(c))$; "bound" is the right side of (eq:identity) without the Selmer term, i.e. $\sum_q t_3+\text{extra}$ (no additive primes):

| curve, $q$ | $a_q$ | $n$ | $\bar u\bmod q$ | $\ell$-th power? | extra | bound at $\ell=3$ | $v_3(\deg\varphi_E)$ | mod 3 image |
|-|-|-|-|-|-|-|-|-|
| 77c1, $7$ | $-1$ | $3$ | $5$ | no (cubes mod $7$: $\pm1$) | $0$ | $1$ | $1$ ($\deg=6$) | surjective |
| 791a1, $7$ | $-1$ | $3$ | $6\equiv-1$ | yes | $1$ | $2$ | $2$ ($\deg=144$) | surjective |
| 1577a1, $19$ | $+1$ | $3$ | $8=2^3$ | yes (not a $9$th power) | $1$ | $2$ | $2$ ($\deg=720$) | surjective |
| 11a1, $11$ ($\ell=5$) | $+1$ | $5$ | $10\equiv-1$ | yes ($5$th powers mod $11$: $\pm1$) | $1$ | (Eisenstein) | $0$ ($\deg=1$) | 5Cs.1.1 |

(The other bad primes of 77c1, 791a1, 1577a1 are of type $\mathrm I_2$ and contribute $0$ at $\ell=3$; $3\nmid N$ in each case.) The first three
show the extra term of Remark rem:ko(1) and Section sec:tam at work and the bound attained; 11a1 (rational $5$-torsion) shows why
the paper needs $\bar\rho$ irreducible: the local term is $2$ but $\deg\varphi_E=1$. Paper: Section sec:tam, Remark rem:ko(1), Lemma lem:tamfactor;
Chapter 22.

### 5.6 `rem:galcoh:tamagawa-exp-cohomological` (remark) P
Lemma lem:tamagawa-exp in cohomological form: $\rho\bmod\ell^t$ is unramified at $q$ iff the corner $\varepsilon\kappa\bmod\ell^t$ vanishes on $I$ iff
$n\,t_\ell\equiv0\pmod{\ell^t}$ on $I$ iff $\ell^t\mid n$ (5.4(ii); $t_\ell$ is surjective), for split and nonsplit reduction alike ($\varepsilon|_I=1$). Equivalently,
by 1.5(i) over $\Q_q^{\mathrm{ur}}\supset\mu_{\ell^t}$: $q_E\in(\Q_q^{\mathrm{ur}\times})^{\ell^t}$ iff $\ell^t\mid n$ (important_notes.md point 8). The lemma itself is proved in
Chapter 11 (item 3.3 there); this remark only gives the cohomological reading. Paper: Lemma lem:tamagawa-exp, the history paragraph
of Section 1.5 ("$t_q=v_\ell(n_q)=t_\ell(E,q)$").

## 6. Line-up, Section 6: global Galois cohomology: $G_\Q$, $G_{\Q,S}$, the real place

### 6.1 `def:galcoh:gqs` (definition) P
$S$, $\Q_S$, $G_{\Q,S}$ as in C5; $G_{\Q,S}$ is the quotient of $G_\Q$ by the closed normal subgroup $H_S$ generated by the inertia groups
$I_{\mathfrak p}$ of all primes $\mathfrak p$ of $\overline\Q$ above $p\notin S$. A $G_\Q$-module $M$ (type (D) finite, (C) or (V)) is unramified outside $S$
if $H_S$ acts trivially; then it is a $G_{\Q,S}$-module. Examples: $\mu_n$ with $S\supseteq\{\infty\}\cup\{p\mid n\}$; $E[n]$, $T_\ell E$, $\ad T_\ell E$ with
$S\supseteq\{\infty,\ell\}\cup\{p\mid N\}$ (Neron-Ogg-Shafarevich, Chapter 11). Localisation maps $\operatorname{res}_v$ (C5). Reference: NSW, Chapter VIII,
Section 3 (cite the chapter); Rubin, Euler Systems, Section 1.5. Paper: Section 4.2 ($W$ unramified outside $\Sigma\cup\{\ell\}$), Lemma lem:dfg21.

### 6.2 `prop:galcoh:unramified-almost-everywhere` (proposition) P
Let $M$ be unramified outside $S$. (i) Inflation identifies $H^1(G_{\Q,S},M)$ with $\{c\in H^1(\Q,M):\operatorname{res}_pc\in H^1_{\mathrm{ur}}(\Q_p,M)$ for all
$p\notin S\}$. (ii) For $M$ finite every $c\in H^1(\Q,M)$ is unramified at almost all $p$. Proof: (i) inflation-restriction for $H_S\trianglelefteq G_\Q$
(Chapter 16): $c$ comes from $G_{\Q,S}$ iff $c|_{H_S}\in\Hom(H_S,M)$ vanishes, iff it vanishes on each $I_{\mathfrak p}$, which is the unramified
condition (conjugation-invariance, C5); (ii) $c|_{G_L}$, $L$ the field cut out by $M$, is a homomorphism with finite image, so it cuts out a
finite extension of $L$, ramified at finitely many primes. Reference: Rubin, Euler Systems, Section 1.5; MilneADT, Chapter I,
Section 4. Paper: Theorem thm:main (the Selmer groups are subgroups of $H^1(G_{\Q,S},W)$), Lemma lem:dfg21 ("unramified elsewhere").

### 6.3 `thm:galcoh:gqs-finite` (theorem) S
For $M$ finite and unramified outside the finite set $S$: (i) $H^1(G_{\Q,S},M)$ is finite; (ii) $H^2(G_{\Q,S},M)$ is finite (stated); (iii) for
$\ell$ odd and $S\ni\ell$, $H^n(G_{\Q,S},M)=0$ for $n\ge3$ when $M$ is $\ell$-primary (stated). Sketch of (i): restrict to the open subgroup
$G_{L,S}$ fixing $M$; $\Hom(G_{L,S},M)$ is finite because there are only finitely many extensions of $L$ of degree dividing $\#M$ unramified
outside $S$ (Hermite-Minkowski, stated); inflation-restriction for $G_{L,S}\trianglelefteq G_{\Q,S}$ and the finiteness of $H^1$ of the finite group
$\Gal(L/\Q)$ finish. Consequences: for $T$ unramified outside $S$, 2.2 applies with $G=G_{\Q,S}$: $H^1(G_{\Q,S},T)$ is finitely generated,
$H^1(G_{\Q,S},W)$ cofinitely generated, $H^1(G_{\Q,S},T)_{\mathrm{tors}}\simeq H^0(\Q,W)/H^0(\Q,W)_{\mathrm{div}}$. Reference: SilvermanAEC, Chapter VIII, Section 1
(Hermite-Minkowski in the proof of weak Mordell-Weil, check); NSW, Chapter VIII, Section 3; MilneADT, Chapter I, Section 4.
Paper: Theorem thm:main and Lemma lem:dfg21 (cofinite generation and finiteness statements behind "length"), Lemma lem:h0 (through
2.2: $H^0(\Q,W^D)$ finite when $H^0(\Q,V^D)=0$).

### 6.4 `prop:galcoh:real-place` (proposition, recalled from Chapter 16 z2-on-l-adic) P
$G_\R=\{1,c\}$. For every $G_\R$-module $M$ and $n\ge1$, $2H^n(\R,M)=0$; if $\ell$ is odd and $M$ is of type (D, $\ell$-primary), (C) or (V), then
$H^n(\R,M)=0$ for $n\ge1$, $\hat H^0(\R,M)=M^{c=1}/(1+c)M=0$, and $M=M^+\oplus M^-$. Consequences: for $\ell$ odd every local condition at $\infty$ is
$0=H^1(\R,M)$, the real place contributes nothing to Selmer groups and to the comparison sequences except the factor
$1/\#H^0(\R,M)$ in 9.3; and $H^1_f(\R,T^D)=H^1(\R,T^D)=0$. Example ($\ell=2$, where it fails): $H^1(\R,\mu_2)=\R^\times/\R^{\times2}=\Z/2$. Paper:
the paragraph after Lemma lem:dfg21 ("At $\infty$, $H^1(\R,T^D)$ is killed by $2$, so $H^1_f(\R,T^D)=0$ for $\ell$ odd"), the summand $p=\infty$ of
Lemma lem:dfg21.

### 6.5 `ex:galcoh:global-kummer` (worked example) P
$H^1(\Q,\mu_n)=\Q^\times/(\Q^\times)^n$; the class of $x$ is unramified at $p\nmid n$ iff $n\mid v_p(x)$ (by 5.1 over $\Q_p$), so for $S\supseteq\{\infty\}\cup\{p\mid n\}$:
$H^1(G_{\Q,S},\mu_n)=\{x\in\Q^\times:n\mid v_p(x)\ \forall p\notin S\}/(\Q^\times)^n\simeq\Z_S^\times/(\Z_S^\times)^n$ (class number one), with $\Z_S^\times=\pm\prod_{p\in S}p^{\Z}$:
finite, of order $n^{\#S-1}\cdot\#(\pm1)/(\pm1)^n$. The model case of 6.3. Paper: background (the shape of all finiteness arguments).

## 7. Line-up, Section 7: elliptic curves: the Kummer map, the $n$-Selmer group and Sha

### 7.1 `prop:galcoh:ec-kummer` (proposition) P
Let $E/K$ be an elliptic curve and $\operatorname{char}K\nmid n$. The sequence $0\to E[n]\to E(\overline K)\xrightarrow{[n]}E(\overline K)\to0$ is exact (Chapter 9: $[n]$ is
surjective on $\overline K$-points, being a nonconstant isogeny); its long exact sequence gives the **Kummer map**
$\delta\colon E(K)/nE(K)\hookrightarrow H^1(K,E[n])$, $\delta(P)=[\sigma\mapsto\sigma Q-Q]$ with $nQ=P$, and the exact sequence
$0\to E(K)/nE(K)\to H^1(K,E[n])\to H^1(K,E)[n]\to0$, where $H^1(K,E)=H^1(K,E(\overline K))$. The analogy with 1.4: replacing $E$ by $\mathbb G_m$
gives Kummer theory, and Hilbert 90 says the analogue of $H^1(K,E)$ vanishes. Reference: SilvermanAEC, Chapter VIII, Section 2 and
Chapter X, Section 1 (cite the sections). Paper: background (the model for all Selmer groups; Chapter 9, 9.1 deferral).

### 7.2 `prop:galcoh:ec-local-image` (proposition) P for (i), (ii); R for (iii)
Let $E/\Q_p$ and $p\nmid n$. (i) $\#E(\Q_p)/nE(\Q_p)=\#E(\Q_p)[n]=\#H^0(\Q_p,E[n])=\#H^1_{\mathrm{ur}}(\Q_p,E[n])$ (snake lemma for $[n]$ on $0\to E_1(\Q_p)\to E(\Q_p)\to
E(\Q_p)/E_1(\Q_p)\to0$, $E_1(\Q_p)$ uniquely $n$-divisible by the formal group, Chapter 10; then 4.2(ii)). (ii) If $E$ has good reduction at $p$,
$\delta(E(\Q_p)/n)=H^1_{\mathrm{ur}}(\Q_p,E[n])$: a point $Q$ with $nQ=P$ exists in $E(\Q_p^{\mathrm{ur}})$ (the reduction $\tilde E(\overline\F_p)$ is $n$-divisible and
$E_1(\Q_p^{\mathrm{ur}})$ is uniquely $n$-divisible), so $\delta(P)$ vanishes on $I_p$; equality by (i). (iii) (Tate, stated.) For any reduction type,
$\delta(E(\Q_p)/n)$ is its own exact annihilator under 3.3(i) with $E[n]\simeq E[n]^*(1)$ (Weil pairing). (iv) (Example, P, and the link with
Tamagawa numbers.) For $p\ne\ell$ and $W=E[\ell^\infty]$: the Kummer image $E(\Q_p)\otimes\Q_\ell/\Z_\ell$ in $H^1(\Q_p,W)$ is $0$, whereas
$H^1_{\mathrm{ur}}(\Q_p,W)=W^{I}/(\Frob-1)W^{I}$; for multiplicative reduction of type $\mathrm I_n$ ($\ell$ odd) it has order $\ell^{v_\ell(n)}$ if split and $1$ if
nonsplit (compute $W^I$ as an extension of $\Z/\ell^{v_\ell(n)}$, on which $\Frob$ acts by $\varepsilon$, by $\mu_{\ell^\infty}$, which is $(\Frob-1)$-divisible), i.e.
the $\ell$-part of the Tamagawa number $c_p$ (Chapter 10, 7.6). This is the classical shadow of the Tamagawa factors of Chapter 18 and
agrees with Chapter 16, model-computation (e). Reference: SilvermanAEC, Chapter X, Section 4; MilneADT, Chapter I, Section 3 (for
(iii)). Paper: background; Lemma lem:tamfactor (its final check "the $\ell$-part of the Tamagawa number $c_q(E)$").

### 7.3 `def:galcoh:selmer-sha` (definition and proposition) P
For $E/\Q$: $\operatorname{Sel}_n(E/\Q)=\{c\in H^1(\Q,E[n]):\operatorname{res}_vc\in\delta_v(E(\Q_v)/nE(\Q_v))\text{ for all }v\}$,
$\text{Sha}(E/\Q)=\ker\bigl(H^1(\Q,E)\to\prod_vH^1(\Q_v,E)\bigr)$, and $0\to E(\Q)/nE(\Q)\to\operatorname{Sel}_n(E/\Q)\to\text{Sha}(E/\Q)[n]\to0$ is exact (diagram chase on
7.1 for $\Q$ and all $\Q_v$). Typeset Sha with the Cyrillic letter only if the preamble provides it; otherwise `\operatorname{Sha}`. Reference:
SilvermanAEC, Chapter X, Section 4. Paper: background (Section sec:two mentions ranks, Watkins's conjecture).

### 7.4 `thm:galcoh:selmer-finite` (theorem and corollary) P (given 6.2, 6.3, 7.2(ii))
With $S=\{\infty\}\cup\{p\mid nN_E\}$: $\operatorname{Sel}_n(E/\Q)\subseteq H^1(G_{\Q,S},E[n])$ (7.2(ii) and 6.2(i)), hence $\operatorname{Sel}_n(E/\Q)$ is finite (6.3).
Corollary (weak Mordell-Weil): $E(\Q)/nE(\Q)$ is finite. With the height argument (Chapter 9, 9.1) this gives Mordell's theorem.
Reference: SilvermanAEC, Chapter VIII, Section 1 and Chapter X, Section 4 (Theorem 4.2 there, check). Paper: background (Chapter 9's
deferral; "this is the model for all Selmer groups").

### 7.5 `ex:galcoh:selmer-11a1` (worked example) P (from the data)
11a1: $E(\Q)=\Z/5$, rank $0$ and $\#\text{Sha}=1$ (Cremona's allbsd), so $\operatorname{Sel}_5(E/\Q)\simeq E(\Q)/5E(\Q)\simeq\Z/5$; and over $\Q_{11}$, $E[5]\subset E(\Q_{11})$
(3.5(c)), so the local condition at $11$ is a subgroup of order $\#E(\Q_{11})[5]=25$ of $H^1(\Q_{11},E[5])$, of order $625$ (7.2(i)). A small model of
the difference between "unramified" and "Kummer image" at a prime of bad reduction: here $H^1_{\mathrm{ur}}(\Q_{11},E[5])$ also has order $25$
(4.2(ii)), but the image of $E(\Q_{11})/5$ is a different subgroup: it is $\Hom(G_{\Q_{11}},\mu_5)\subset\Hom(G_{\Q_{11}},E[5])$ ($G_{\Q_{11}}$ acts trivially on
$E[5]\supset\mu_5$), which contains the ramified class of the uniformiser $11$, consistent with $5\mid c_{11}=5$ and with 7.2(iv) (Exercise 15).
Paper: background.

## 8. Line-up, Section 8: Selmer structures and dual Selmer structures

### 8.1 `def:galcoh:selmer-structure` (definition and examples) P
Let $M$ be a $G_\Q$-module unramified outside a finite set $S$, of one of the types: finite of $\ell$-power order; $W$ (discrete, cofinitely
generated); $T$ (type (C)). A **Selmer structure** $\mathcal L$ on $M$ is a family of subgroups $\mathcal L_v\subseteq H^1(\Q_v,M)$, one for each place $v$,
with $\mathcal L_v=H^1_{\mathrm{ur}}(\Q_v,M)$ for all $v\notin S_{\mathcal L}$, a finite set containing $S$ (for type (C) one also asks $\mathcal L_v$ closed). Its
**Selmer group** is
$$H^1_{\mathcal L}(\Q,M)=\{c\in H^1(\Q,M):\operatorname{res}_vc\in\mathcal L_v\ \forall v\}=\ker\Bigl(H^1(G_{\Q,S_{\mathcal L}},M)\to\bigoplus_{v\in S_{\mathcal L}}H^1(\Q_v,M)/\mathcal L_v\Bigr)$$
(the equality by 6.2(i)). Examples: (a) the unramified structure; (b) $\mathcal L^\Sigma$, **relaxed** at a finite set $\Sigma$ of primes:
$\mathcal L^\Sigma_p=H^1(\Q_p,M)$ for $p\in\Sigma$, $\mathcal L^\Sigma_v=\mathcal L_v$ otherwise; (c) $\mathcal L_\Sigma$, **strict** at $\Sigma$: $\mathcal L_{\Sigma,p}=0$ for $p\in\Sigma$;
(d) the classical structure $\delta_v(E(\Q_v)/n)$ on $E[n]$ (a Selmer structure by 7.2(ii)), with Selmer group $\operatorname{Sel}_n(E/\Q)$; (e) **propagated
structures**: given $\Q_\ell$-subspaces $L_{V,v}\subseteq H^1(\Q_v,V)$ with $L_{V,v}=H^1_{\mathrm{ur}}(\Q_v,V)$ for almost all $v$, the families
$(\iota^{-1}L_{V,v})_v$ on $T$ and $(\pi L_{V,v})_v$ on $W$ (4.5(iii) shows they are Selmer structures). The Bloch-Kato structure is of type (e)
(Chapter 18), and the paper's $H^1_f(\Q,W)$ and $H^1_\Sigma(\Q,W)=H^1_{f^\Sigma}(\Q,W)$ are the Selmer groups of the Bloch-Kato structure and of its
relaxation at $\Sigma$ ("no condition at the primes of $\Sigma$, the Bloch-Kato condition at $\ell$ and the unramified condition elsewhere").
Reference: MazurRubin04, Section 2.1 (check); Rubin, Euler Systems, Section 1.5; DFG04, Section 2.1. Paper: Theorem thm:main
($H^1_f(\Q,\ad T\otimes\Q_\ell/\Z_\ell)$), Section 4.2 ($H^1_\Sigma(\Q,W)\supseteq H^1_f(\Q,W)$), Lemma lem:dfg21.

### 8.2 `def:galcoh:dual-structure` (definition and proposition) P
Let $M$ be finite of $\ell$-power order, $M'=M^*(1)$, $\mathcal L$ a Selmer structure on $M$. The **dual structure** $\mathcal L^*$ on $M'$ is
$\mathcal L^*_v=\mathcal L_v^\perp$ under 3.3(i) (at $v=\infty$ under the analogous pairing on $H^1(\R,-)$; for $\ell$ odd both sides are $0$, 6.4). (i) $\mathcal L^*$ is a
Selmer structure: at $p\notin S_{\mathcal L}\cup\{\ell\}$, $\mathcal L_p^\perp=H^1_{\mathrm{ur}}(\Q_p,M)^\perp=H^1_{\mathrm{ur}}(\Q_p,M')$ by 4.4(i). (ii) $\mathcal L^{**}=\mathcal L$; $\mathcal L\subseteq\mathcal L'$
(i.e. $\mathcal L_v\subseteq\mathcal L'_v$ for all $v$) implies $\mathcal L'^*\subseteq\mathcal L^*$; $(\mathcal L^\Sigma)^*=(\mathcal L^*)_\Sigma$ (relaxed and strict are dual). (iii) ($\ell$-adic.) If
$\mathcal L$ on $W$ is propagated from $(L_{V,v})$ and $L_{V,v}^\perp=L_{V^D,v}$ for every $v$, its dual (under 3.3(ii)) is the structure on $T^D$
propagated from $(L_{V^D,v})$ (4.5(ii)); the relaxation of the first at $\Sigma$ is dual to the strict version of the second. Reference:
MazurRubin04, Section 2.3 (check); Rubin, Euler Systems, Section 1.7. Paper: Lemma lem:dfg21 (the "dual Selmer group" behind
$H^0(\Q,W^D)^*$), Chapter 18 (Bloch-Kato structures are self-dual in this sense).

### 8.3 `prop:galcoh:selmer-l-adic` (proposition) P for (i), (ii); S for (iii)
Let $\mathcal L$ be propagated from $(L_{V,v})$ (8.1(e)). (i) $H^1_{\mathcal L}(\Q,W)$ is cofinitely generated and $H^1_{\mathcal L}(\Q,T)$ finitely generated (6.3).
(ii) If the global $\Q_\ell$-Selmer group $H^1_{L_V}(\Q,V)=\{c\in H^1(G_{\Q,S},V):\operatorname{res}_vc\in L_{V,v}\ \forall v\}$ vanishes, then
$H^1_{\mathcal L}(\Q,T)=H^1(G_{\Q,S},T)_{\mathrm{tors}}\simeq H^0(\Q,W)/H^0(\Q,W)_{\mathrm{div}}$, and $\simeq H^0(\Q,W)$ if moreover $H^0(\Q,V)=0$ (every class maps to $0$ in
$H^1(G_{\Q,S},V)$, so is torsion by 2.2(ii); conversely torsion classes satisfy every propagated condition, 4.5(i)). (iii) (Stated, with a
sketch.) $\operatorname{corank}_{\Z_\ell}H^1_{\mathcal L}(\Q,W)=\dim H^1_{L_V}(\Q,V)$; in particular $H^1_{\mathcal L}(\Q,W)$ is finite iff $H^1_{L_V}(\Q,V)=0$. Reference: Rubin, Euler
Systems, Section 1.5 (check); Bloch-Kato, Section 5 (for the Bloch-Kato case, check). Paper: Lemma lem:dfg21 (with $T^D$ in place of $T$:
"$H^1_f(\Q,V^D)=0$" forces the dual Selmer group of $T^D$ to be $H^0(\Q,W^D)$), Remark rem:ns (finiteness of the Selmer groups in the
identity), Theorem thm:dfg27 (through Chapter 18).

## 9. Line-up, Section 9: global duality: Poitou-Tate and the Greenberg-Wiles formula

### 9.1 `thm:galcoh:poitou-tate` (theorem, Poitou-Tate exact sequence) R
Let $M$ be finite, unramified outside $S$, with $S\ni\infty$ and $S\ni p$ for every $p\mid\#M$; $M'=M^*(1)$; $G_S=G_{\Q,S}$. There is an exact sequence
$$0\to H^0(G_S,M)\to\bigoplus_{v\in S}\hat H^0(\Q_v,M)\to H^2(G_S,M')^*\to H^1(G_S,M)\to\bigoplus_{v\in S}H^1(\Q_v,M)\to H^1(G_S,M')^*\to H^2(G_S,M)\to\bigoplus_{v\in S}H^2(\Q_v,M)\to H^0(G_S,M')^*\to0,$$
where $\hat H^0(\Q_p,M)=H^0(\Q_p,M)$ for finite $p$, $\hat H^0(\R,M)$ is the Tate group (zero for $\#M$ odd), the maps $\bigoplus_vH^i(\Q_v,M)\to H^{2-i}(G_S,M')^*$
send $(c_v)$ to $y\mapsto\sum_v\operatorname{inv}_v(c_v\cup\operatorname{res}_vy)$ (3.3), and the others are restrictions or their duals. In particular the kernel of
$H^1(G_S,M)\to\bigoplus_{v\in S}H^1(\Q_v,M)$ (the group $\text{Sha}^1_S(M)$) is dual to $\text{Sha}^2_S(M')$. Reference: MilneADT, Chapter I, Section 4
(Theorem 4.10 there, check); NSW, Chapter VIII, Section 6; TateDuality; Rubin, Euler Systems, Section 1.7. Paper: Lemma lem:dfg21
(through 10.1, 10.2).

### 9.2 `prop:galcoh:reciprocity` (proposition) P (given 1.7(iii))
For $x\in H^1(\Q,M)$ and $y\in H^1(\Q,M')$: $\operatorname{res}_vx\cup\operatorname{res}_vy$ is unramified, hence has invariant $0$, for almost all $v$, and
$\sum_v\operatorname{inv}_v(\operatorname{res}_vx\cup\operatorname{res}_vy)=0$. Proof: $x\cup y\in H^2(\Q,M\otimes M')\to H^2(\Q,\mu_{\ell^\infty})\subseteq\operatorname{Br}(\Q)$ (via 1.4(ii)), and 1.7(iii);
almost all local cups are inflated from $H^2(\hat\Z,\mu)=0$ (as in 4.4). Paper: through 10.1 (the "complex" part of the comparison
sequence, which is all that the inequality direction needs).

### 9.3 `thm:galcoh:greenberg-wiles` (theorem, the formula of Greenberg and Wiles) R (proof idea S)
Let $M$ be finite of $\ell$-power order, $\mathcal L$ a Selmer structure on $M$ and $\mathcal L^*$ its dual. Then $H^1_{\mathcal L}(\Q,M)$ and $H^1_{\mathcal L^*}(\Q,M')$ are
finite and
$$\frac{\#H^1_{\mathcal L}(\Q,M)}{\#H^1_{\mathcal L^*}(\Q,M')}=\frac{\#H^0(\Q,M)}{\#H^0(\Q,M')}\prod_v\frac{\#\mathcal L_v}{\#H^0(\Q_v,M)},$$
the product over all places including $\infty$, almost all factors being $1$ (4.2(ii)). Proof idea: Poitou-Tate (9.1) and Tate's global
Euler characteristic formula (stated: $\#H^0(G_S,M)\#H^2(G_S,M)/\#H^1(G_S,M)=\prod_{v\mid\infty}\#H^0(\Q_v,M)/|\#M|_\infty$). Reference: Wiles95,
Proposition 1.6 (check); DDT, Theorem 2.19 (check); Washington's survey in the Boston FLT volume is an alternative (not in refs.bib;
not needed). Paper: background ("the origin of the exact sequence of DFG04 Lemma 2.1", PLAN.md); 9.5.

### 9.4 `ex:galcoh:gw-check` (worked example) P
$M=\Z/\ell$, $\ell$ odd, $M'=\mu_\ell$. (a) $\mathcal L$ = unramified at every prime (including $\ell$): $H^1_{\mathcal L}(\Q,\Z/\ell)=\Hom(G_\Q,\Z/\ell)^{\mathrm{ur}}=0$ ($\Q$ has no
unramified extension; Minkowski, stated); $\mathcal L^*_p=H^1_{\mathrm{ur}}(\Q_p,\mu_\ell)$ for $p\ne\ell$ (4.4) and $\mathcal L^*_\ell$ = image of $\Z_\ell^\times$ (4.4, warning), so
$H^1_{\mathcal L^*}(\Q,\mu_\ell)=\{x:\ell\mid v_p(x)\ \forall p\}/(\Q^\times)^\ell=\{\pm1\}/\{\pm1\}^\ell=0$. Right side: $\frac{\ell}{1}\cdot\frac{1}{\ell}$ (the factor at $\infty$ is
$\#\mathcal L_\infty/\#H^0(\R,\Z/\ell)=1/\ell$; all finite factors are $1$ by 4.2(ii)) $=1$. (b) Relax at one prime $p\ne\ell$: the left side becomes
$\#\{$characters of $G_\Q$ of order dividing $\ell$ unramified outside $p\}=\ell^{[p\equiv1\ (\ell)]}$ over $\#H^1_{(\mathcal L^*)_p}=1$; the right side gains
$\#H^1(\Q_p,\Z/\ell)/\#H^1_{\mathrm{ur}}=\#H^0(\Q_p,\mu_\ell)=\ell^{[p\equiv1\ (\ell)]}$ (3.5(a)). Both sides agree: Greenberg-Wiles recovers the count of cyclic
extensions of degree $\ell$ and conductor $p$. Paper: background (a check of 9.3 the reader can do by hand).

### 9.5 `cor:galcoh:gw-comparison` (corollary) P (given 9.3)
For Selmer structures $\mathcal L\subseteq\mathcal L'$ on finite $M$:
$\dfrac{\#H^1_{\mathcal L'}(\Q,M)}{\#H^1_{\mathcal L}(\Q,M)}=\prod_v\dfrac{\#\mathcal L'_v}{\#\mathcal L_v}\cdot\dfrac{\#H^1_{\mathcal L'^*}(\Q,M')}{\#H^1_{\mathcal L^*}(\Q,M')}$. This is the numerical shadow of the exact
sequence 10.1; applied at each finite level to the Bloch-Kato structure and its relaxation at $\Sigma$ and passed to the limit, it gives the
length identity of the proof of Theorem thm:main and of Remark rem:ns (10.4). Paper: Lemma lem:dfg21, Remark rem:ns.

## 10. Line-up, Section 10: comparing Selmer structures; the abstract form of DFG04 Lemma 2.1

### 10.1 `thm:galcoh:comparison` (theorem) P for (i), (ii); S for (iii) (from 9.1)
Let $M$ be finite of $\ell$-power order and $\mathcal L\subseteq\mathcal L'$ Selmer structures on $M$, so $\mathcal L'^*\subseteq\mathcal L^*$ on $M'$. Consider
$$0\to H^1_{\mathcal L}(\Q,M)\to H^1_{\mathcal L'}(\Q,M)\xrightarrow{\ \operatorname{loc}\ }\bigoplus_v\mathcal L'_v/\mathcal L_v\xrightarrow{\ \theta\ }H^1_{\mathcal L^*}(\Q,M')^*\xrightarrow{\ \operatorname{res}^*\ }H^1_{\mathcal L'^*}(\Q,M')^*\to0,$$
with $\theta((c_v))(y)=\sum_v\operatorname{inv}_v(c_v\cup\operatorname{res}_vy)$ (well defined because $\mathcal L^*_v$ annihilates $\mathcal L_v$; the sum is finite). (i) (Elementary.) The
sequence is exact at $H^1_{\mathcal L}$ and at $H^1_{\mathcal L'}$ (definitions), $\operatorname{res}^*$ is surjective (dual of an inclusion of finite groups), and
$\theta\circ\operatorname{loc}=0$, $\operatorname{res}^*\circ\theta=0$ (9.2: reciprocity; and $\mathcal L'^*_v=\mathcal L'^\perp_v$). (ii) Hence $\#H^1_{\mathcal L'}/\#H^1_{\mathcal L}\le\prod_v\#(\mathcal L'_v/\mathcal L_v)$, with the
defect bounded by $\#(H^1_{\mathcal L^*}/H^1_{\mathcal L'^*})$. (iii) The sequence is exact (Poitou-Tate 9.1, applied to the middle of the nine-term sequence).
Reference: Rubin, Euler Systems, Theorem 1.7.3 (check); MazurRubin04, Section 2.3 (check); Washington's survey (not needed).
Paper: Lemma lem:dfg21 (its proof).

### 10.2 `thm:galcoh:comparison-l-adic` (theorem) S
Let $T$ be as in C4, unramified outside $S$; $\mathcal L\subseteq\mathcal L'$ Selmer structures on $W$ propagated from $L_V\subseteq L'_V$ with
$L_{V,v}^\perp=L_{V^D,v}$, $L'^\perp_{V,v}=L'_{V^D,v}$; $\mathcal L^*$, $\mathcal L'^*$ the dual structures on $T^D$ (8.2(iii)). Then
$$0\to H^1_{\mathcal L}(\Q,W)\to H^1_{\mathcal L'}(\Q,W)\to\bigoplus_v\mathcal L'_v/\mathcal L_v\to H^1_{\mathcal L^*}(\Q,T^D)^*\to H^1_{\mathcal L'^*}(\Q,T^D)^*\to0$$
is exact, and $\mathcal L'_v/\mathcal L_v\simeq(\mathcal L^*_v/\mathcal L'^*_v)^*$ (4.5(ii)). Sketch: apply 10.1 to $W[\ell^k]=T/\ell^k$ with the induced structures (preimages of
$\mathcal L_v$, images of $\mathcal L^*_v$, which are mutually dual at each level), take the direct limit over $k$ for the $W$-terms (exact; the error
terms $H^0(\Q,W)/\ell^k$ of 2.2(iv) die in the limit because $H^0(\Q,W)$ is torsion) and the inverse limit for the $T^D$-terms (finite groups,
Mittag-Leffler), Pontryagin duality exchanging the two. Reference: Rubin, Euler Systems, Section 1.7 and Appendix B; Greenberg89,
Section 4 (check); DFG04, proof of Lemma 2.1. Paper: Lemma lem:dfg21.

### 10.3 `thm:galcoh:relaxing-sigma` (theorem; the abstract form of DFG04 Lemma 2.1) P (given 10.2, 2.2, 4.5, 6.4, 8.3)
Let $\ell$ be odd, $T$ unramified outside $S$, $(L_{V,v})_v$ local conditions on $V$ with $L_{V,v}=H^1_{\mathrm{ur}}(\Q_v,V)$ for $v\notin S$ and
$L_{V,v}^\perp=L_{V^D,v}$ for all $v$; $\mathcal L$ the propagated structure on $W$, $\mathcal L^*$ the propagated (dual) structure on $T^D$. Let $\Sigma$ be a finite
set of primes $p\ne\ell$. Assume (a) $H^1_{L_{V^D}}(\Q,V^D)=0$, and (b) $H^0(\Q_p,V^D)=0$ for at least one $p\in\Sigma$ (so $\Sigma\neq\emptyset$; (b) implies
$H^0(\Q,V^D)=0$). Then there is an exact sequence
$$0\to H^1_{\mathcal L}(\Q,W)\to H^1_{\mathcal L^\Sigma}(\Q,W)\to\bigoplus_{p\in\Sigma\cup\{\infty\}}\bigl(\mathcal L^*_p\bigr)^*\to H^0(\Q,W^D)^*\to0,$$
where $\mathcal L^*_p=\iota^{-1}(L_{V^D,p})\subseteq H^1(\Q_p,T^D)$ and $\mathcal L^*_\infty=H^1(\R,T^D)=0$. Proof (to be written in full): 10.2 with $\mathcal L'=\mathcal L^\Sigma$, whose dual
is $(\mathcal L^*)_\Sigma$ (8.2(ii), (iii)); $\mathcal L^\Sigma_p/\mathcal L_p=H^1(\Q_p,W)/\mathcal L_p\simeq(\mathcal L^*_p)^*$ (4.5(ii)); by (a) and 8.3(ii), $H^1_{\mathcal L^*}(\Q,T^D)=H^1(G_{\Q,S},T^D)_{\mathrm{tors}}
=\delta(H^0(\Q,W^D))\simeq H^0(\Q,W^D)$, finite since $H^0(\Q,V^D)=0$; the strict group $H^1_{(\mathcal L^*)_\Sigma}(\Q,T^D)$ consists of the $\delta(x)$ with
$\operatorname{res}_p\delta(x)=\delta_p(x)=0$ for $p\in\Sigma$, and $\delta_p$ is injective on $H^0(\Q_p,W^D)\supseteq H^0(\Q,W^D)$ at the prime $p$ of (b) (2.2(ii) locally), so
it is $0$ and the last map is onto $H^0(\Q,W^D)^*$; the summand at $\infty$ is $0$ (6.4). Paper: Lemma lem:dfg21 is this theorem for the
Bloch-Kato structure $f$ (Chapter 18 checks $L_{V,v}^\perp=L_{V^D,v}$: at $p\ne\ell$ it is 4.4(ii), at $\ell$ Bloch-Kato's Proposition 3.8 (check)), with
(a) = DFG04 Theorem 2.7 (Theorem thm:dfg27), and (b) supplied by the paragraph after Lemma lem:dfg21 ($H^1_{\mathrm{ur}}(\Q_p,V^D)=0$ for $p\in\Sigma$,
hence $H^0(\Q_p,V^D)=0$ by 4.2(iii)); the paper's hypothesis $H^0(\Q,V^D)=0$ then follows from (b).

### 10.4 `cor:galcoh:length-identity` (corollary) P
Under 10.3, if $H^1_{\mathcal L^\Sigma}(\Q,W)$ is finite then all terms are finite and
$$\len H^1_{\mathcal L^\Sigma}(\Q,W)=\len H^1_{\mathcal L}(\Q,W)+\sum_{p\in\Sigma}\len\mathcal L^*_p-\len H^0(\Q,W^D)$$
(lengths alternate in an exact sequence of finite $\Z_\ell$-modules and are preserved by Pontryagin duality: Chapter 16,
lengths-in-exact-sequences); the identity holds in $\N\cup\{\infty\}$ in general. With $\mathcal L=f$: $H^0(\Q,W^D)=0$ gives the identity
"$\len H^1_\Sigma(\Q,W)=\len H^1_f(\Q,W)+\sum_{p\in\Sigma}\len H^1_f(\Q_p,T^D)$" of the proof of Theorem thm:main; $\len H^0(\Q,W^D)=h_\ell(E)$ gives the
displayed identity of Remark rem:ns (with Lemma lem:fpr for the local lengths, Chapter 18). By important_notes.md point 5 (Chapter 11),
$h_\ell(E)=0$ for $\ell\ge5$ and $h_3(E)\le1$, with or without complex multiplication. Paper: proof of Theorem thm:main, Remark rem:ns,
Conjecture conj:euler (the term $-h_\ell(E)$).

### 10.5 `ex:galcoh:relaxing-toy` (worked example) P
$T=\Z_\ell$ (trivial action), $\ell$ odd, so $V=\Q_\ell$, $W=\Q_\ell/\Z_\ell$, $T^D=\Z_\ell(1)$, $W^D=\mu_{\ell^\infty}$. Conditions on $V$: $L_{V,p}=H^1_{\mathrm{ur}}(\Q_p,\Q_\ell)$ at every
prime including $\ell$, $0$ at $\infty$; their annihilators are $L_{V^D,p}=H^1_{\mathrm{ur}}(\Q_p,\Q_\ell(1))=0$ for $p\ne\ell$ (4.4(ii)) and $L_{V^D,\ell}=\Z_\ell^\times\otimes\Q_\ell$ at
$\ell$ (unramified characters kill unit classes, local class field theory; dimension count 3.4(ii) fails at $\ell$, use 3.2 with $\ell=p$:
$\dim H^1(\Q_\ell,\Q_\ell(1))=2$). Then: $H^1_{L_{V^D}}(\Q,\Q_\ell(1))=(\Z^\times\otimes\Q_\ell)=0$, hypothesis (a); $H^0(\Q_p,\Q_\ell(1))=0$ for every $p$, hypothesis (b);
$H^1_{\mathcal L}(\Q,W)=\Hom(G_\Q,\Q_\ell/\Z_\ell)^{\mathrm{ur}}=0$; for $\Sigma=\{p\}$, $H^1_{\mathcal L^\Sigma}(\Q,W)$ = characters of $\ell$-power order unramified outside $p$
$\simeq\Z/\ell^{v_\ell(p-1)}$; $\mathcal L^*_p=\iota^{-1}(0)=H^1(\Q_p,\Z_\ell(1))_{\mathrm{tors}}=\Z_p^\times\otimes\Z_\ell\simeq\Z/\ell^{v_\ell(p-1)}$ (2.5); $H^0(\Q,\mu_{\ell^\infty})=0$. The sequence of
10.3 reads $0\to0\to\Z/\ell^{v_\ell(p-1)}\xrightarrow{\sim}(\Z/\ell^{v_\ell(p-1)})^*\to0\to0$: the $\ell$-part of $(\Z/p)^\times$ classifies the cyclic extensions of $\ell$-power
degree and conductor $p$. (Variant with $H^0(\Q,W^D)\ne0$, the toy model of $h_3(E)=1$: $\ell=3$, $T=\Z_3(\chi_{-3})$, $W^D=\mu_{3^\infty}\otimes\chi_{-3}$, for which
$H^0(\Q,W^D)=\Z/3$ because $\bar\chi_3=\chi_{-3}$ while $\chi_3\chi_{-3}\not\equiv1\pmod9$; Exercise 13.) Paper: background for Lemma lem:dfg21 and
Remark rem:ns.

### 10.6 `rem:galcoh:handover-ch18` (remark) P (bookkeeping)
What Chapter 18 adds to obtain the paper's Lemma lem:dfg21 from 10.3: the Bloch-Kato local conditions $H^1_f(\Q_v,V)$ (with
$H^1_f=H^1_{\mathrm{ur}}$ at $p\ne\ell$ and $H^1_f(\R,-)=0$), their exact orthogonality at $\ell$ (Bloch-Kato), the vanishing $H^1_f(\Q,V^D)=0$ (DFG04
Theorem 2.7, Theorem thm:dfg27), the identification $\det(1-\Phi_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}$ (geometric Frobenius), and the
Fontaine-Perrin-Riou splitting of $\len H^1_f(\Q_p,T^D)=\len H^0(\Q_p,W^D)$ into $v_\ell(L_p(A_f,1)^{-1})+v_\ell(\Tam_p)$ (Lemma lem:fpr). This chapter supplies
the duality, the local structure (4.2 to 4.6) and the global sequence (10.1 to 10.4). Paper: Lemma lem:dfg21, Lemma lem:fpr, proof of
Theorem thm:main.

____

## 11. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200). The card lists all 54 items above (about 200
lines, not counted). Each section opens with one paragraph saying what it is for and where the paper uses it.

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: items 1.1 to 10.6, each stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | lem:tamfactor end of proof (5.1 to 5.5); lem:tamagawa-exp (1.4, 5.6); the paragraph after lem:dfg21 (2.2, 4.2, 4.6, 6.4); lem:dfg21 (3.3, 4.4, 4.5, 8.1 to 8.3, 10.1 to 10.3); proof of thm:main and rem:ns (10.4); the Selmer groups of thm:main (8.1); Section 1.2 and lem:fpr through Chapter 18 (4.3); sec:tam, rem:ko(1) (5.4, 5.5) | 40 |
| 1 | Galois cohomology of a field; Hilbert 90; Kummer theory | 1.1 to 1.7; conventions C1 to C6 as `convention` environments; `paperlink` for lem:tamfactor ("$H^1(G,\Z_\ell(1))=\varprojlim\dots$"); RHB aside: the connecting map as the "phase ambiguity" of choosing an $n$-th root, one sentence | 200 |
| 2 | $\ell$-adic coefficients | 2.1 to 2.5; C3, C4 restated; the diagram $T\to V\to W$ with its long exact sequence; `warning`: $H^1(G,V)$ sees no torsion, $H^1(G,T)_{\mathrm{tors}}$ comes from $H^0(G,W)$ | 190 |
| 3 | Local Galois cohomology: finiteness, Euler characteristic, Tate local duality | 3.1 to 3.5; the table of orders 3.5(a); the 11a1 example 3.5(c) | 200 |
| 4 | Unramified cohomology | 4.1 to 4.7; `warning` at 4.4 (the case $p=\ell$); `warning` (point 11): the vanishing in 4.2(iii) is convention-free, the value of the determinant is not; `paperlink` for the paragraph after lem:dfg21 (4.2, 4.6, 4.7(d)) | 230 |
| 5 | The Kummer class of the Tate parameter | 5.1 to 5.6; `paperlink` quoting the end of the proof of lem:tamfactor, with the corrected reading (points 7, 31, 42 and Part 16, N1); the table 5.5 | 210 |
| 6 | Global Galois cohomology: $G_\Q$, $G_{\Q,S}$, the real place | 6.1 to 6.5; `paperlink` for "$H^1(\R,T^D)$ is killed by $2$" (6.4) | 130 |
| 7 | Elliptic curves: the Kummer map, Selmer and Sha | 7.1 to 7.5; the weak Mordell-Weil theorem as the model of all finiteness proofs; 7.2(iv) as the bridge to Tamagawa numbers | 170 |
| 8 | Selmer structures and dual structures | 8.1 to 8.3; the dictionary relaxed/strict; `paperlink` for Section 4.2 ($H^1_f$, $H^1_\Sigma$) | 150 |
| 9 | Poitou-Tate and the Greenberg-Wiles formula | 9.1 to 9.5; the check 9.4 worked in full | 170 |
| 10 | Comparing Selmer structures; the abstract form of DFG04 Lemma 2.1 | 10.1 to 10.6; the proof of 10.3 in full; the toy example 10.5; `paperlink` for lem:dfg21, the proof of thm:main and rem:ns | 230 |
| 11 | Exercises | 18 exercises (Part 12.2) | 150 |
| 12 | Notes and references | Serre (Galois Cohomology; Local Fields), Tate (ICM 1962), Milne ADT, NSW, Cassels-Frohlich, Rubin, Mazur-Rubin, Greenberg, Wiles, DDT, Bloch-Kato, FPR94, Silverman AEC/ATAEC; which numbers were cited (only those verified) | 40 |
| | **total** | | **2110** |

## 12. Coverage table and exercises

### 12.1 Coverage

| PLAN.md scope item, Section 6 map row, or paper hook | line-up items |
|-|-|
| Galois cohomology of a field $H^i(K,M)$, discrete $G_K$-modules | 1.1, 1.2 |
| Hilbert 90, $H^1(K,\overline K^\times)=0$ | 1.3 |
| Kummer theory $H^1(K,\mu_n)=K^\times/(K^\times)^n$ (proved) | 1.4, 1.6 |
| the Kummer map and the Kummer class of an element | 1.5, 2.4 |
| $H^1(K,\Z_\ell(1))=\varprojlim K^\times/(K^\times)^{\ell^k}$, $\Z_\ell(1)=T_\ell\mu$ | 2.4, 2.5, C3 |
| the Brauer group and $H^2(K,\mu_n)$ (statement) | 1.4(ii), 1.7 |
| finiteness of $H^i(\Q_p,M)$ for finite $M$ | 3.1 |
| local Euler-Poincare characteristic formula (statement) | 3.2, 3.5 |
| Tate local duality (statement with reference) | 3.3, 3.4 |
| $H^1_{\mathrm{ur}}(\Q_p,M)=H^1(G/I,M^I)=\ker(H^1\to H^1(I,M))$ | 4.1, 4.3 |
| $H^1_{\mathrm{ur}}(\Q_p,M)=M^{I_p}/(\Frob_p-1)M^{I_p}$ | 4.2 |
| the annihilator of $H^1_{\mathrm{ur}}$ is $H^1_{\mathrm{ur}}$ of the dual ($p\ne\ell$) | 4.4 |
| the real place: $H^1(\R,M)$ killed by $2$, zero for $\ell$ odd | 6.4 |
| $G_\Q$ and $G_{\Q,S}$ | 6.1, 6.2 |
| finiteness of $H^1(G_{\Q,S},M)$ | 6.3, 6.5 |
| Kummer sequence of an elliptic curve and the Kummer map | 7.1, 7.2 |
| $n$-Selmer group, Sha, $0\to E(\Q)/n\to\operatorname{Sel}_n\to\text{Sha}[n]\to0$, finiteness, weak Mordell-Weil | 7.3, 7.4, 7.5 |
| Selmer structures and $H^1_{\mathcal L}(\Q,M)$ | 8.1, 8.3 |
| the dual Selmer structure via local duality | 8.2 |
| the Greenberg-Wiles formula | 9.3, 9.4, 9.5 |
| the Poitou-Tate exact sequence | 9.1, 9.2 |
| comparing Selmer groups for two sets of local conditions, elementary part proved | 10.1, 10.2 |
| Lemma lem:dfg21 as the comparison of Bloch-Kato with $\Sigma$-relaxed, dual term $H^0(\Q,W^D)^*$ | 10.3, 10.4, 10.6 |
| $H^1(K,T)$, $H^1(K,V)$, $H^1(K,W)$; $H^1(K,T)_{\mathrm{tors}}$ from $H^0(K,W)$ | 2.2, 2.3 |
| $H^1(\Q_p,T)$ finitely generated, torsion $H^0(\Q_p,W)/\mathrm{div}$; "$H^1_f(\Q_p,T^D)$ is the torsion" | 2.2, 3.1, 4.6 |
| the Tate curve: $H^1(\Q_p,\Z_\ell(1))$, the Kummer class of the Tate parameter, its image in $H^1(G/I,\Z_\ell(1)^I)=\Z/\ell^{v_\ell(q-1)}$ (proved in full) | 5.1 to 5.5 |
| Section 6 row: Sigma-imprimitive Selmer group, Bloch-Kato Selmer group, $H^1_f$, $H^1_\Sigma$ (17, 18) | 8.1, 8.2, 10.3, 10.6 |
| Section 6 row: the computation of $\Tam_q(\ad T)$ at a multiplicative prime (16, 17, 18) | 4.3, 5.4, 5.5 |
| Section 6 row: Kummer theory, Kummer classes, $H^1(G,\Z_\ell(1))$, tame character, $\Frob^{-1}t\Frob=t^{q^{-1}}$ (5, 7, 16, 17) | 1.4, 1.5, 2.4, 5.1 to 5.4 (the tame relation is Chapter 7's, used in 5.4(iv)) |
| hook: Lemma lem:tamagawa-exp | 1.4, 1.5(i), 5.6 |
| hook: Lemma lem:tamfactor (Kummer theory, $c'$, $H^1(G/I,\Z_\ell(1)^I)$) | 1.6, 2.4, 2.5, 5.1 to 5.5 |
| hook: Lemma lem:dfg21 and the paragraph after it | 2.2, 3.3, 4.2, 4.4 to 4.7, 6.4, 8.1 to 8.3, 10.1 to 10.3 |
| hook: Remark rem:ns | 8.3, 10.4, 10.5 (variant), Exercise 13 |
| hook: the Selmer groups of Theorem thm:main | 8.1, 10.4 |
| hook (through Chapter 18): Section 1.2 ($\Tam_p$), Lemma lem:fpr | 4.2(iv), 4.3, 4.6, 4.7(d), (e) |
| hook: Section sec:tam, Remark rem:ko(1) | 5.4, 5.5 |

### 12.2 Exercises (Section 11 of the chapter), graded from easy to harder

1. (Easy) From Hilbert 90 deduce $H^1(\R,\mu_n)=\R^\times/\R^{\times n}$; show it is $0$ for $n$ odd and $\Z/2$ for $n$ even; compare with 6.4.
2. Compute $\#H^i(\Q_p,\Z/\ell^k)$ and $\#H^i(\Q_p,\mu_{\ell^k})$, $i=0,1,2$, for $(p,\ell,k)=(7,3,1),(19,3,2),(5,3,2)$; check the Euler characteristic
   and the duality 3.4(i).
3. Check the paper's claim that $H^1(\R,T^D)$ is killed by $2$ and that $H^1_f(\R,T^D)=0$ for $\ell$ odd; show that $H^1(\R,\Z_2(1))=\Z/2$, so the claim
   genuinely needs $\ell$ odd.
4. Check the paper's claim "$H^1(G,\Z_\ell(1))=\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}$" by computing both sides for $q=7$, $\ell=3$ (answer $\Z_3\times\Z/3$) and
   identify the torsion with $H^0(\Q_7,\Q_3/\Z_3(1))=\mu_3$ (2.2(ii)).
5. Check the paper's claim "$\Z_\ell(1)/(q-1)\simeq\Z/\ell^{v_\ell(q-1)}$ ... the class of the unit part in $\F_q^\times\otimes\Z_\ell$": for $q=19$, $\ell=3$ compute the
   classes of $u=2,8,-1$ and their valuations $0,1,2$ (Chapter 7, 2.8(b)); explain why the class $0$ must be read as having valuation
   $v_3(18)=2$ (point 31).
6. Let $\kappa$ be a Kummer cocycle of $x=q^nu\in\Q_q^\times$. Show that $\kappa(\Frob\sigma)-\kappa(\Frob)=q\,n\,t_\ell(\sigma)$ for $\sigma\in I_q$ and that a change
   of cocycle changes $\kappa(\Frob)$ by $(q-1)z$. Conclude that the paper's "well defined modulo $q-1$" should read "modulo $(n,q-1)$", and that
   $\min(v_\ell(n),v_\ell(q-1),v_\ell(c'))$ is nevertheless well defined (point 7).
7. Check the paper's matrix in the proof of Lemma lem:tamfactor (point 42): show that $g\mapsto\begin{psmallmatrix}\chi_\ell\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$ is not a
   homomorphism when $\varepsilon\ne1$ and $\kappa$ is a Kummer cocycle, while $\begin{psmallmatrix}\chi_\ell\varepsilon&\varepsilon\kappa\\0&\varepsilon\end{psmallmatrix}$ is; what changes in $c'$?
8. (Paper check, PARI) For 791a1 at $q=7$ and 77c1 at $q=7$ ($\ell=3$) compute the Tate parameter with `ellinit(E,O(7^30)).tate`, its valuation
   $n=3$ and unit part ($\bar u=6$, resp. $5$); decide whether $\bar u$ is a cube; deduce $v_3(\Tam_7(\ad T))=2$, resp. $1$, with Chapter 16's
   model computation; compare with $v_3(\deg\varphi_E)=v_3(144)=2$, resp. $v_3(6)=1$ (ecdata). Check the paper's claim in Section sec:tam that
   the extra term raises the bound exactly where the unit part is an $\ell$-th power.
9. Check the paper's claim that $H^1_{\mathrm{ur}}(\Q_p,V^D)=0$ at a multiplicative prime: compute $(V^D)^{I_p}$ for $V=\ad V_\ell E$, the eigenvalue of $\Frob$
   ($p^2$) and of $\Phi$ ($p^{-2}$), and $\det(1-\Phi)=1-p^{-2}$ versus $\det(1-\Frob)=1-p^2$; show that both have the same $\ell$-adic valuation
   and that only the first is $L_p(A_f,1)^{-1}$ (point 11).
10. Check the paper's claim in Lemma lem:fpr that the Euler factor is an $\ell$-adic integer of valuation $e_\ell(E,q)$ at an additive prime, in the
    case of type $\mathrm{III}$ at $q\ge5$: show $\#H^1_{\mathrm{ur}}(\Q_q,T^D)=\ell^{v_\ell(q-\chi_{-4}(q))}$ using 4.2(iv) and Lemma lem:euler's description of
    $(\ad V)^{I_q}$.
11. (Greenberg-Wiles by hand) Do 9.4(b) in full: for $M=\Z/\ell$ relaxed at one prime $p\ne\ell$, compute both sides and recover the
    number of cyclic extensions of $\Q$ of degree $\ell$ and conductor $p$.
12. Do 10.5 in full: verify the hypotheses of 10.3 for $T=\Z_\ell$, $\Sigma=\{p\}$, and identify every term of the exact sequence.
13. (The toy model of $h_3(E)$.) Let $T=\Z_3(\chi_{-3})$. Show $H^0(\Q,W^D)=H^0(\Q,\mu_{3^\infty}\otimes\chi_{-3})\simeq\Z/3$, using $\bar\chi_3=\chi_{-3}$ and an element $\sigma$
    with $\chi_3(\sigma)=4$. Show that for $\ell\ge5$ and any character $\psi$ of order $2$, $H^0(\Q,\mu_{\ell^\infty}\otimes\psi)=0$. Relate this to the paper's claim in
    Lemma lem:h0 that $H^0(\Q,W^D)$ is finite and vanishes for $\ell\ge5$, and to the correct bound $h_3(E)\le1$ (point 5).
14. Over $\Q_p$, $p$ odd, compute $\#H^i(\Q_p,\mu_p)$ and check the Euler characteristic $p^{-1}$; show that $H^1_{\mathrm{ur}}(\Q_p,\Z/p)$ and $H^1_{\mathrm{ur}}(\Q_p,\mu_p)$ are
    not exact annihilators (the warning in 4.4).
15. (PARI) Show that $E[5]\subset E(\Q_{11})$ for $E=$ 11a1 (Tate parameter a fifth power, $\mu_5\subset\Q_{11}$), deduce $\#H^1(\Q_{11},E[5])=625$, and show
    that the image of the Kummer map $E(\Q_{11})/5\to H^1(\Q_{11},E[5])$ has order $25$ but is not $H^1_{\mathrm{ur}}(\Q_{11},E[5])$; relate this to $c_{11}=5$
    and 7.2(iv).
16. For the Tate curve at $p\ne\ell$ ($\ell$ odd) compute $H^1_{\mathrm{ur}}(\Q_p,E[\ell^\infty])$ in the split and nonsplit cases and compare with the $\ell$-part of $c_p$
    (Chapter 10) and with Chapter 16's model computation for $M=T$.
17. (Harder) Prove 4.4(i) for $M=\Z/\ell$, $M'=\mu_\ell$, $p\ne\ell$, directly: the cup product of an unramified character with the Kummer class
    of a unit is $0$ (use local class field theory as stated in Chapter 7, 6.5).
18. (Harder) Show that the hypothesis $H^0(\Q,V^D)=0$ of Lemma lem:dfg21 follows from $H^0(\Q_p,V^D)=0$ at one $p\in\Sigma$, and that in the paper's
    situation $H^0(\Q_p,V^D)=0$ at every $p\in\Sigma$ (4.2(iii) and the paragraph after the lemma). Where exactly does the proof of 10.3 use a
    prime of $\Sigma$ with this property, and what would the last term of the sequence be without it?

## 13. Dependencies and forward pointers

Results from earlier chapters used here (by chapter label only):
* Chapter 2 (`ch:rings`): $\ell$-th powers in $\F_q^\times$, $[\F_q^\times:(\F_q^\times)^{\ell^k}]=\ell^{\min(k,v_\ell(q-1))}$, the class $c(u)$ and $v_\ell$ of a class (1.6, 5.2, 5.4);
  $q$ prime to $\ell$ is a unit of $\Z_\ell$.
* Chapter 3 (`ch:modules`): finitely generated $\Z_\ell$-modules, torsion, saturation (4.2(iv)); lengths and their additivity; Pontryagin
  duality 8.1, 8.2 and $T$ versus $W$ 8.3, cyclic $\ell$-primary modules 8.4; cokernel of an injective endomorphism of $\Z_\ell^d$ has order
  $\ell^{v_\ell(\det)}$; maximal divisible subgroups of cofinitely generated modules.
* Chapter 4 (`ch:reps`): 7.6 (duals and the trace form, only as a pointer), unipotent and finite cyclic actions (used in 4.7).
* Chapter 5 (`ch:galois`): Hilbert 90 for finite cyclic and finite Galois extensions (galois:hilbert90), Kummer theory with $\mu_n\subset K$
  (galois:kummer-character, galois:kummer-classification), galois:kummer-finite-field, galois:l-adic-kummer, the cyclotomic character,
  profinite Galois groups, complex conjugation and $G_\R$.
* Chapter 6 (`ch:ant`): decomposition and inertia groups and Frobenius elements (6.1, 6.2), class number one of $\Q$ and the units of $\Z_S$
  (6.5).
* Chapter 7 (`ch:local`): 2.7 (powers in $K^\times$, $\widehat{K^\times}$), 4.2 ($\Q_q^{\mathrm{ur}}$, Hensel there), 5.3 (tame character, $I^{(\ell)}=\Z_\ell(1)$), 5.4
  (tame relation), 5.5 (the Frobenius lift fixing roots of $q$), 6.1, 6.2 (Kummer cocycles, $\kappa_x|_I=v(x)t_\ell$, $\kappa_u$ unramified), 6.5 (local
  class field theory, only in 3.5(a), 10.5, Exercise 17), conventions L3 and L6 (Frobenius and $L$-factors).
* Chapter 9 (`ch:ellcurves`): $E[n]$, surjectivity of $[n]$, the Weil pairing (5.3, 5.5), the descent with heights for Mordell-Weil (9.1).
* Chapter 10 (`ch:reduction`): the formal group and $E_1$ (7.2), the Tate curve and the Tate parameter $q_E$, $u$, $c(u)$ (7.4, 7.5(iii), 7.8), the
  component groups and $c_p$ (7.6).
* Chapter 11 (`ch:galrep`): 3.2 (the matrices $\begin{psmallmatrix}\chi_\ell\varepsilon&\varepsilon\kappa\\0&\varepsilon\end{psmallmatrix}$ on $T_\ell E$), 3.3 (Lemma lem:tamagawa-exp), Neron-Ogg-Shafarevich
  (6.1); Lemma lem:h0 in its corrected form (10.4).
* Chapter 16 (`ch:cohomology`): everything in its Sections 4 to 11: h0-h1 and connecting maps, inflation-restriction (a) to (d),
  conjugation-action, order-kills and z2-on-l-adic (6.4), continuous-cohomology, les-continuous, tate-limits, h1-finitely-generated,
  prime-to-l-vanishing, tame-inertia-example, procyclic-discrete, procyclic-compact, procyclic-examples, model-computation (5.4(v)),
  cup-product (3.3, 9.2), lengths-in-exact-sequences (10.4), galois-cohomology-convention and unramified-h1-preview (4.1, 4.2 are their
  full versions).

Black boxes stated here with references, never used to prove an earlier item: $\operatorname{inv}\colon\operatorname{Br}(K)\simeq\Q/\Z$ and Albert-Brauer-Hasse-Noether
(1.7); $\operatorname{cd}G_{\Q_p}=2$ and finiteness (3.1); the local Euler characteristic (3.2); Tate local duality (3.3); Hermite-Minkowski and the
finiteness of $H^2(G_{\Q,S},M)$ (6.3); Tate's self-duality of the Kummer image (7.2(iii)); Poitou-Tate (9.1); Greenberg-Wiles (9.3); the corank
formula 8.3(iii).

Forward pointers (chapters that use this one):
* Chapter 18 (`ch:blochkato`): defines the Bloch-Kato conditions as propagated structures (4.5, 8.1(e)), checks their exact orthogonality
  (4.4(ii) at $p\ne\ell$; Bloch-Kato at $\ell$), proves Lemma lem:fpr from 4.2(iv), 4.3, 4.6, states Lemma lem:dfg21 as 10.3 for $f$, with DFG04
  Theorem 2.7 for hypothesis (a), and assembles Lemma lem:tamfactor from Chapter 16's model computation and 5.4.
* Chapter 19 (`ch:lfunctions`): the value $\det(1-\Phi\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}$ and the omitted factors (4.7(d), (e) are the cohomological side).
* Chapter 20 (`ch:congruence`): the assembly of Theorem thm:main uses 10.4; the Taylor-Wiles method reads $H^1_\Sigma(\Q,W)$ as a Selmer group
  of 8.1.
* Chapter 21 (`ch:paper`): A2.7 step (7) cites 5.3, 5.4; A4.9 "attached facts" cite 2.2, 4.2, 4.6, 6.4 and its proof idea cites 10.3; A4.10 steps
  (1), (2) cite 4.3, 4.2(iv); A5.2 cites 10.4.
* Chapter 22 (`ch:computation`): Tate parameters and unit parts with PARI (5.5).

## 14. Notes for the writer

### 14.1 Conventions (to be set as `convention` environments at first use)
* **Frobenius.** C2: $\Frob$ arithmetic in all cohomological statements; $\Phi=\Frob^{-1}$ only where an $L$-factor is named. In 4.2(iii) say
  explicitly that the vanishing of $H^1_{\mathrm{ur}}(\Q_p,V)$ is equivalent to $\det(1-\Frob\mid V^I)\ne0$ and to $\det(1-\Phi\mid V^I)\ne0$, and that the order of
  $H^1_{\mathrm{ur}}(\Q_p,T)$ is $\ell^{v_\ell}$ of either determinant; then say that only $\det(1-\Phi\mid(V^D)^{I_p})$ equals $L_p(A_f,1)^{-1}$ (point 11; Exercise 9).
* **Duals.** C3: $^*$ = Pontryagin dual (the paper's), $^\vee$ = linear dual, $M^*(1)$ = Kummer dual of a finite or discrete module, $T^D=T^\vee(1)$,
  $W^D=V^D/T^D$. Chapter 3's 8.3(vi) says the Cartier dual is Chapter 18's; it is needed here first, for Tate duality. Define it here in
  general (2.1) and let Chapter 18 add the adjoint-specific identification $T^D\simeq A(1)$ (Part 16, B-a).
* **Twists.** $M(1)=M\otimes\Z_\ell(1)$; $\Frob$ acts on $\Z_\ell(1)$ by $p$ ($p\ne\ell$), $\Phi$ by $p^{-1}$. $\chi_\ell$ is the cyclotomic character; $\chi_q$ (paper) is
  the quadratic character of conductor $q$ (important_notes.md point 32): write $\chi_{q^*}$ or say so in words whenever both appear.
* **Signs.** The Kummer connecting map has no sign (C6). The Tate local pairing is compatible with connecting maps only up to $(-1)^i$
  (3.3); no sign matters for any order or length in the chapter, so say this once and never track signs.
* **Kummer cocycle versus class.** Write $\kappa$ for a cocycle and $[\kappa]$ for its class whenever a value $\kappa(\Frob)$ is taken. The paper
  calls the cocycle in the corner "the Kummer class"; 5.4 must keep the two apart, because $\kappa(\Frob)$ depends on the cocycle and the lift.

### 14.2 Pitfalls
* **$c'$ is a cocycle value, not a class.** 5.3 gives a canonical meaning to "the image of $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)$" for $\Q_q$ (the
  retraction attached to the uniformiser $q$); 5.4(iii) says $c'$ equals $\pm$ that image for the Frobenius lift fixing the roots of $q$; 5.4(iv)
  gives the indeterminacy $(n,q-1)\Z_\ell$ in general. Do not write "$c'$ is well defined modulo $q-1$" (the paper's phrase): it is well defined
  modulo $(n,q-1)$ only, which suffices. State the result as $v_\ell((n,q-1,c')\Z_\ell)$, which is visibly choice-free.
* **The corner is $\varepsilon\kappa$** (point 42); on $I$ the factor $\varepsilon$ is $1$, at $\Frob$ it is $a_q(E)=\pm1$, harmless for valuations.
* **"$u$ is an $\ell^k$-th power in $\F_q^\times$"** means its reduction (point 31); for $\ell\ne q$ this is equivalent to $u\in(\Z_q^\times)^{\ell^k}$ (Chapter 7, 2.7).
  The class $0\in\Z/\ell^v$ has valuation $v$, not $\infty$, in the formula.
* **Unramified orthogonality needs $p\ne\ell$** (4.4, warning, Exercise 14). At $\ell$ use Bloch-Kato (Chapter 18). Never write
  "$H^1_f=H^1_{\mathrm{ur}}$" at $p=\ell$.
* **Unramified for $T$ versus the propagated condition.** For $p\ne\ell$ with $T$ ramified at $p$, $\iota^{-1}(H^1_{\mathrm{ur}}(\Q_p,V))$ can be strictly larger than
  $H^1_{\mathrm{ur}}(\Q_p,T)$ (it contains all torsion); the quotient is what Chapter 18 measures by the Tamagawa factor. For $T$ unramified at $p$
  they coincide (4.5(iii)). Do not identify them in general.
* **The torsion of $H^1(G,T)$** is $H^0(G,W)$ modulo its divisible part, not $H^0(G,W)$ (2.2(ii)); the two agree when $H^0(G,V)=0$, which is
  the case in every application of the paper (4.6, 10.3).
* **Hypothesis (b) of 10.3.** The surjectivity onto $H^0(\Q,W^D)^*$ needs a prime of $\Sigma$ with $H^0(\Q_p,V^D)=0$; in DFG04's adjoint setting this is
  automatic (weights), and in the paper it follows from the paragraph after Lemma lem:dfg21. State it as a hypothesis in the abstract
  theorem and discharge it for the paper (Exercise 18). Without it, the sequence continues with $\to H^1_{\mathcal L^*_\Sigma}(\Q,T^D)^*\to0$.
* **Continuity.** All $\ell$-adic statements use continuous cochains; the limit passages in 2.4 and 10.2 rely on Chapter 16's tate-limits and
  on finiteness at each level. Do not write $H^1(G,T)=\varinjlim$ of anything.
* **Lengths versus orders.** Lemma lem:dfg21 is stated with Pontryagin duals; only lengths enter the paper; Pontryagin duality preserves
  them (Chapter 3). Use $\len$ throughout Section 10.
* **The real place.** For $\ell$ odd it contributes nothing to Selmer groups; in Greenberg-Wiles it still contributes the factor
  $1/\#H^0(\R,M)$ (9.4 shows this factor is essential).
* **Theorem numbers.** Only cite the numbers marked "(check)" after checking them against the books; otherwise cite chapter and section
  (PLAN.md Section 3). In particular: Serre's Galois Cohomology II.5.2 and II.5.7, Milne ADT I.2.3, I.2.6, I.2.8 and I.4.10, Wiles95
  Proposition 1.6, DDT Theorem 2.19, Rubin Theorem 1.7.3 and Lemma 1.3.2, Bloch-Kato Proposition 3.8, AEC X.4.2 were recalled from memory.

### 14.3 What to leave to neighbouring chapters
* Chapter 5: Hilbert 90 for finite extensions, Kummer theory with $\mu_n\subset K$, the $\ell$-adic Kummer cocycle, galois:kummer-finite-field.
  Recall in one line each; this chapter adds the cohomological form and removes $\mu_n\subset K$.
* Chapter 7: everything field-theoretic about $\Q_q$: Hensel, $\widehat{K^\times}$, the tame character and relation, the Frobenius lift fixing roots
  (5.5), the decomposition $\kappa_x=a\kappa_\varpi+\kappa_u$ and the formula $\kappa_x|_I=v(x)t_\ell$ (6.2). Cite them; Section 5 here adds only the
  cohomological statements (5.1 to 5.3) and the identification of $c'$ (5.4).
* Chapters 10, 11: the Tate curve, the matrices of $T_\ell E$ at a multiplicative prime, Lemma lem:tamagawa-exp (proved in Chapter 11, 3.3). Here
  only the cohomological reading 5.6.
* Chapter 16: the group cohomology of Lemma lem:tamfactor (the $(t-1)M$ computation, the conjugation action, the invariants, their
  Fitting ideal). Section 5 here uses Chapter 16's model-computation as a black box and supplies only the identification of $c'$.
* Chapter 18: Bloch-Kato conditions ($H^1_f$, $H^1_g$, $H^1_e$, $B_{\mathrm{cris}}$), the definition of $\Tam_p$, the Fontaine-Perrin-Riou formula (Lemma lem:fpr),
  the full proof of Lemma lem:tamfactor (assembly), DFG04 Lemma 2.1 in the paper's form and DFG04 Theorem 2.7, $T^D\simeq A(1)$, the
  adjoint motive. This chapter must not define $H^1_f$ or $\Tam_p$ except by forward reference (`\Cref{ch:blochkato}`).
* Chapter 19: local $L$-factors and their values; $e_\ell(E,q)$; Lemma lem:euler. Here only the cohomological side (4.7(d), (e)).
* Chapter 20: DFG04 Theorem 3.7 and the assembly of Theorem thm:main.

### 14.4 How each relevant point of important_notes.md is handled
* **Point 5 (Lemma lem:h0: $h_\ell(E)=0$ for $\ell\ge5$, $h_3(E)\le1$, CM irrelevant).** 10.4 quotes the corrected statement (proved in Chapter 11) when
  it names $\len H^0(\Q,W^D)=h_\ell(E)$; Exercise 13 gives the determinant mechanism in a one-dimensional toy model ($\chi_3\chi_{-3}\not\equiv1\pmod9$, and
  $\bar\chi_\ell$ of order $\ge4$ for $\ell\ge5$). Do not repeat the paper's "finite for $E$ without complex multiplication".
* **Point 7 (Lemma lem:tamfactor, "$c'$ is the image of $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)$").** Section 5 in full: 5.1, 5.2 (the unramified classes
  are the unit classes; their value at $\Frob$ is the class of $\bar u$), 5.3 (the canonical retraction attached to the uniformiser $q$, which
  gives the paper's phrase a precise meaning; Part 16, N1), 5.4 (iii) to (v) (the value $c'$, its indeterminacy $(n,q-1)$, the choice-free
  minimum). Exercise 6. A `paperlink` quotes the paper's sentence and the corrected reading.
* **Point 8 (Lemma lem:tamagawa-exp phrasing).** 5.6 uses $q_E$ for the Tate parameter and states "$q_E$ is an $\ell^t$-th power in $\Q_q^{\mathrm{ur}}$ iff
  $\ell^t\mid n$".
* **Point 11 (geometric versus arithmetic Frobenius).** C2, 4.2(iii), (iv), 4.7(d), the `warning` in Section 4, Exercise 9: the paragraph after
  Lemma lem:dfg21 is correct as a vanishing statement in either convention; the equality with $L_p(A_f,1)^{-1}$ needs $\Phi$.
* **Point 31 (the class of $u$ means the class of its reduction; $v_\ell(0)$).** 1.6, 5.2, 5.4(v), Exercise 5.
* **Point 37 ($\Tam_p$ is the Fitting ideal of the invariants).** 4.3, forward remark, written as $\Fitt_{\Z_\ell}\bigl((H^1(I,M)_{\mathrm{tors}})^{G/I}\bigr)$.
* **Point 42 (the corner is $\varepsilon\kappa$).** 5.4 setup and (iii); Exercise 7.
* **Point 32 (notation $\chi_q$ versus $\chi_\ell$).** 14.1, Twists.
* **Points 39, 56 (multiplicity one not needed).** Not in this chapter's area; nothing here depends on freeness.
* **B4 (the symbol $*$).** C3 fixes $^*$ as Pontryagin dual in this chapter, consistently with the paper and Chapter 16; Appendix B must
  record it.
* **B6 (PLAN.md's Weil-Deligne relation in geometric form).** Not used here; C2 repeats Chapter 7's convention (arithmetic $\Frob$, geometric
  $\Phi=\Frob^{-1}$) so that no formula of this chapter depends on PLAN.md's wording.
* **B7 (Chapter 21, A2.7 step (1): $\kappa$ versus $\varepsilon\kappa$).** 5.4 is the statement Chapter 21 should cite; step (7) there also omits $\varepsilon$
  in "$c'=\kappa_u(\Frob)$" (Part 16, B-c).
* **B14 (bibliography).** See 14.5.

### 14.5 References and bibliography
In `refs.bib` already: `SerreLocalFields`, `NSW`, `MilneADT`, `TateDuality` (Tate, ICM 1962), `Tate95` (Tate, "Relations between $K_2$ and
Galois cohomology", 1976: the continuous-cohomology reference, despite the key), `CasselsFrohlich`, `Rubin`, `Greenberg89`, `Wiles95`, `DDT`,
`BlochKato`, `FPR94`, `DFG04`, `SilvermanAEC`, `SilvermanATAEC`, `SerreAbelian`, `MilneCFT`. To add, following decision B14 (a reference used by
more than one chapter goes into `refs.bib`):
* `SerreGaloisCoh` (J.-P. Serre, Galois Cohomology, Springer Monographs in Mathematics, Springer-Verlag, Berlin, 1997; translated from
  Cohomologie galoisienne, Lecture Notes in Math. 5): planned by the Chapter 16 outline for `bib/ch16.bib`, but needed by Chapters 16 and
  17 (and mentioned by Chapter 3): **put it in `refs.bib`**, once, and tell the Chapter 16 writer (Part 16, B-b).
* `MazurRubin04` (B. Mazur and K. Rubin, Kolyvagin systems, Mem. Amer. Math. Soc. 168 (2004), no. 799): the source of the term "Selmer
  structure". If Chapter 18 (outlined in parallel) also cites it, it goes in `refs.bib`; otherwise in `bib/ch17.bib`. The writer must check
  `refs.bib` and `bib/ch18.bib` first.
No other new keys are needed; the writer must not add Washington's FLT-volume survey (cited above only as optional).

## 15. Verification log (computations done for this outline)

Python with cypari2 (PARI/GP 2.17.2) and Cremona's ecdata files in `/tmp/ch09/data` (allcurves, allbsd, degphi, galrep, conductor below
10,000); scripts in the session scratchpad (`scan.py`).
* Tate parameters by `ellinit(E,O(q^30)).tate[3]`, valuation $n$ and $\bar u=q_Eq^{-n}\bmod q$, for all curves numbered 1 of conductor at most 2,000 with a
  multiplicative prime $q$ and $\ell\in\{3,5,7\}$, $\ell\mid n$, $q\equiv1\pmod\ell$: 348 pairs, of which 104 have $\bar u$ an $\ell$-th power. Rows of 5.5: 11a1
  ($q=11$, $n=5$, $\bar u=10$), 77c1 ($q=7$, $n=3$, $\bar u=5$, $a_7=-1$), 791a1 ($q=7$, $n=3$, $\bar u=6$, $a_7=-1$), 1577a1 ($q=19$, $n=3$, $\bar u=8$, $a_{19}=1$); cubes
  mod $7$: $\{1,6\}$; cubes mod $19$: $\{1,7,8,11,12,18\}$; ninth powers mod $19$: $\{\pm1\}$. Kodaira codes (`elllocalred`): 791a1 $\mathrm I_3$ at $7$, $\mathrm I_2$ at
  $113$; 77c1 $\mathrm I_3$ at $7$, $\mathrm I_2$ at $11$; 1577a1 $\mathrm I_3$ at $19$, $\mathrm I_2$ at $83$. Modular degrees (degphi): 77c1 $6$, 791a1 $144$, 1577a1 $720$,
  11a1 $1$. Mod $3$ images (galrep): 77c1, 791a1, 1577a1 surjective (no entry); 11a1 has 5Cs.1.1. Hence the "bound" column of 5.5 equals
  $v_3(\deg\varphi_E)$ in all three irreducible cases.
* Observation from the same scan (not used): among split multiplicative pairs with $\bar u$ a cube at $\ell=3$ the mod $3$ image is almost always
  reducible (3Cs.1.1 or 3B.1.1) or 3Nn; nonsplit pairs with $\bar u$ a cube are mostly surjective (791a1, 805b1, 874a1, 1066a1, ...). Consistent with
  the fact that for split reduction, $3\mid n$, $q\equiv1\pmod 3$ and $q_E$ a cube, $E[3]$ is trivial as a $G_{\Q_q}$-module.
* 11a1 over $\Q_{11}$: all $12$ roots of the $5$-division polynomial lie in $\Q_{11}$ (`polrootspadic`), each with $4x^3+b_2x^2+2b_4x+b_6$ a square in $\Q_{11}$;
  so $\#E(\Q_{11})[5]=25$. allbsd: 11a1 rank $0$, torsion $5$, Tamagawa product $5$, Sha $1$.
* Orders of local cohomology (3.5(a)) by hand from the Kummer description: e.g. $(p,\ell,k)=(19,3,2)$ gives $3^2,3^4,3^2$ for both $\Z/9$ and $\mu_9$; $(5,3,2)$
  ($v_3(4)=0$, $m=0$): $\#H^i(\Q_5,\Z/9)=9,9,1$ and $\#H^i(\Q_5,\mu_9)=1,9,9$. Euler characteristic $1$ in each case.
* $\Q_p$, $\mu_p$ ($p$ odd): $\#\Q_p^\times/(\Q_p^\times)^p=p^2$ (valuation and $(1+p\Z_p)/(1+p\Z_p)^p\simeq\Z/p$); $H^2=\Z/p$; characteristic $p^{-1}$.
* Toy example 10.5 and 9.4 by hand (class field theory of $\Q$). Toy model of $h_3$: $\chi_3(\sigma)=4$ forces $\chi_{-3}(\sigma)=1$ and $4\not\equiv1\pmod9$.
* Not verified (recalled): every theorem number marked "(check)" in Parts 1 to 10.

## 16. Points for important_notes.md

### 16.1 New points about the paper

**N1 (addendum to point 7). Lemma lem:tamfactor, end of the proof: the phrase "the image of $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)$" has a precise
meaning after all; what is imprecise is "$c'$ is" that image and "well defined modulo $q-1$".** Location: proof of Lemma lem:tamfactor,
the sentence "Finally $c'$ is the image of $\kappa$ in $H^1(G/I,\Z_\ell(1)^I)=\Z_\ell(1)/(q-1)\simeq\Z/\ell^{v_\ell(q-1)}$, the class of the unit part of $q_E$ in
$\F_q^\times\otimes\Z_\ell$ by Kummer theory, well defined modulo $q-1$". Problem: point 7 says that no such map exists. That is true functorially,
but for $K=\Q_q$ the prime $q$ is a canonical uniformiser, $\Q_q^\times=q^{\Z}\times\Z_q^\times$ canonically, and so
$H^1(\Q_q,\Z_\ell(1))=\Z_\ell\kappa_q\oplus H^1_{\mathrm{ur}}(\Q_q,\Z_\ell(1))$ canonically, with $H^1_{\mathrm{ur}}=H^1(G/I,\Z_\ell(1)^I)$ (inflation is injective); the projection sends
the Kummer class of $q_E$ to the class of its unit part, which is the paper's "image" (5.3). The genuine imprecision is elsewhere: $c'$ is
the value at a chosen Frobenius lift of the cocycle $\varepsilon\kappa$ (point 42), equal to $\varepsilon(\Frob)$ times a representative of that image only for a lift
fixing a compatible system of $\ell$-power roots of $q$, and congruent to it modulo the ideal $(n,q-1)\Z_\ell$ (not modulo $q-1$) for an arbitrary
lift (5.4(iii), (iv)). Fix: "Write $H^1(G,\Z_\ell(1))=\Z_\ell\kappa_q\oplus H^1(G/I,\Z_\ell(1))$ using the uniformiser $q$; the second component of $\kappa$ is the class of
the unit part $u$, i.e. of $\bar u$ in $\F_q^\times\otimes\Z_\ell=\Z_\ell(1)/(q-1)$, and $c'\equiv\varepsilon(\Frob)\cdot$(that class) modulo $(n,q-1)$; so
$v_\ell((n,q-1,c'))=v_\ell((n,q-1,c))$." Effect: none on any result; the formula of Lemma lem:tamfactor stands. Confidence: high (the
splitting is elementary; the indeterminacy is the two-line computation of Exercise 6, the same as in Chapter 16's model-computation
(d) and Chapter 7's 6.2(iv)). Action: if point 7 is acted on, use this wording, which keeps the paper's phrase and corrects the
modulus.

**N2 (observation, not an error). Lemma lem:dfg21: the hypothesis $H^0(\Q,V^D)=0$ is implied by what the paragraph after the lemma proves,
and the surjectivity onto $H^0(\Q,W^D)^*$ uses exactly that.** Location: the statement of Lemma lem:dfg21 and the paragraph after it. In the
derivation of the four-term sequence from global duality (10.3), the last map is onto $H^0(\Q,W^D)^*$ because $\delta_p\colon H^0(\Q_p,W^D)\to
H^1(\Q_p,T^D)$ is injective for a prime $p\in\Sigma$ with $H^0(\Q_p,V^D)=0$; for $p\in\Sigma$ the paragraph after the lemma proves
$H^1_{\mathrm{ur}}(\Q_p,V^D)=0$, which is equivalent to $H^0(\Q_p,V^D)=0$ (4.2(iii)), and this implies $H^0(\Q,V^D)=0$. In DFG04's adjoint setting
this is automatic by weights; as the paper quotes the lemma for an abstract $V^D$ it is worth one clause. Fix (optional): after "vanishes,
because ... $\ne0$", add "in particular $H^0(\Q_p,V^D)=0$, and hence $H^0(\Q,V^D)=0$". Confidence: high. Low importance.

No other new problem was found in this chapter's area. The following statements of the paper were rechecked here and are correct
as stated (with the conventions of points 11 and 42): "$H^1(G,\Z_\ell(1))=\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}$"; "$H^1(G/I,\Z_\ell(1)^I)=\Z_\ell(1)/(q-1)
\simeq\Z/\ell^{v_\ell(q-1)}$"; "$H^1_f(\Q_p,V^D)=H^1_{\mathrm{ur}}(\Q_p,V^D)=(V^D)^{I_p}/(\Frob_p-1)$ vanishes" (as a vanishing statement, in either Frobenius
convention); "$H^1_f(\Q_p,T^D)$ is the torsion of $H^1(\Q_p,T^D)$, a finite group" (it is moreover $\simeq H^0(\Q_p,W^D)$); "$H^1(\R,T^D)$ is killed by $2$,
so $H^1_f(\R,T^D)=0$ for $\ell$ odd"; the four-term sequence of Lemma lem:dfg21 under its hypotheses (10.3); the length identities in the
proof of Theorem thm:main and in Remark rem:ns (10.4). The data of Section sec:tam were spot-checked on 77c1, 791a1 and 1577a1 (5.5): the
extra term and the bound behave as the paper says. The known issues in this area are points 5, 7, 8, 11, 31, 37, 42.

### 16.2 Book-internal inconsistencies

* **B-a. Who defines the Kummer (Cartier) dual.** The Chapter 3 outline, item 8.3(vi), says "Twists by $\Z_\ell(1)$, the Cartier dual $T^D=\Hom(T,\Z_\ell(1))$
  and $W^D=V^D/T^D$ are Chapter 18". Tate local duality (this chapter, 3.3) needs them first. Resolution: this chapter defines
  $M^*(1)$, $T^D$, $V^D$, $W^D$ in general (2.1); Chapter 18 adds the adjoint-specific facts ($T^D\simeq A(1)$ via the trace form, $(\ad V)^\vee\simeq\ad V$) and
  cites 2.1. The Chapter 3 writer should change "Chapter 18" to "Chapters 17 and 18".
* **B-b. `SerreGaloisCoh` must go into `refs.bib`, not `bib/ch16.bib`.** The Chapter 16 outline (writer note 12) and the Chapter 3 outline (item
  6.6) plan the key for `bib/ch16.bib`; Chapter 17 cites it too, so by decision B14 it belongs in `refs.bib`. Likewise `MazurRubin04` if Chapter 18
  cites it.
* **B-c. Chapter 21 outline, item A2.7.** Step (7) writes "$c'=\kappa_u(\Frob)$", omitting the factor $\varepsilon(\Frob)$ (important_notes.md B7 records the same
  omission in step (1) only); and its commentary "There is no such map" should be softened by N1: there is a canonical retraction for $\Q_q$,
  and the imprecision is the cocycle value and the modulus $(n,q-1)$. Chapter 21 should cite this chapter's 5.3 and 5.4.
* **B-d. Chapter 16 outline, Section 12 ("unramified-h1-preview") and this chapter's 4.2.** No conflict: Chapter 16 previews the formula
  $H^1_{\mathrm{ur}}=M^{I}/(\Frob-1)M^I$ and the vanishing criterion; 4.2 here is the full statement with the order formula (iv) and the convention
  remark. The Chapter 16 writer should keep the preview to the two displayed formulas and point here.
* **B-e. The deferrals to this chapter are all honoured:** Chapter 5 (Hilbert 90 profinite, Kummer without $\mu_n\subset K$, $H^1(K,\Z_\ell(1))$, $G_\R$): 1.3,
  1.4, 2.4, 6.4; Chapter 7 (6.1(ii), the Euler-characteristic count of 2.7(iv), the cohomological half of point 7): 1.4, 2.4, 3.5, 5.1 to 5.4; Chapter
  8 (Hilbert 90 for $\bar k(C)$): 1.3(iv); Chapter 9 (weak Mordell-Weil; Kummer sequence; $E[n]\simeq E[n]^*(1)$): 7.1 to 7.4, 2.1(iv); Chapter 10 ($q_E$, $u$,
  $c(u)$, $c_q$): 5.4, 5.5, 7.2(iv); Chapter 11 ($\varepsilon\kappa$): 5.4; Chapter 15 (local types for unramified cohomology): 4.7; Chapter 16 (all items of its
  writer note 13 assigned here): 1.3, 1.4, 3.3, 4.2, 4.4, 2.2, 3.1, 6.3, 5.4; Chapter 21 (A2.7 step (7), A4.9, A4.10 inputs, A5.2): 5.3, 5.4, 2.2,
  4.2, 4.3, 4.6, 6.4, 10.3, 10.4.
