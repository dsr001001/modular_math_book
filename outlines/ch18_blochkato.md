# Chapter 18: Bloch-Kato Selmer groups, Tamagawa factors and the adjoint motive (`ch:blochkato`, `chapters/ch18_blochkato.tex`)

Stage 1 line-up. Part V (Cohomology, Selmer groups and L-functions). Target length 2,630 lines of LaTeX (the card
excluded; see Part 3), inside the 2,800 lines that PLAN.md Section 7.3 allows for this chapter.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2
to 16 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book and
chapter or section; a theorem number only where sure, otherwise the section, and numbers marked "(verify)" must be checked
before they are printed); the paper's use by its `\label` names, or "background". Every number quoted below (Tate
parameters and unit parts, Tamagawa factors, modular degrees, the counts for Section sec:tam, the freeness of $\ad T$ over
$\Z_3[C_3]$, the brute-force check of the Tamagawa formula and of its twist) was checked with PARI/GP 2.17 through `cypari2`
and Cremona's `ecdata` files for conductors below 10,000 in `/tmp/ch09/data` (verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

The paper's Theorem thm:main is an identity between the modular degree and three kinds of terms: the length of a
Bloch-Kato Selmer group, Tamagawa factors, and omitted Euler factors. This chapter owns the first two and the
bookkeeping that connects them. Concretely it must deliver:

1. **The objects of Section 1.2 of the paper.** $\ell$-adic representations, lattices $T$, divisible modules $W$, Tate twists,
   the three duals (linear, Kummer-Cartier $V^D=V^\vee(1)$, Pontryagin), the trace form and $T^D\simeq A(1)$ for $A=\ad T$ and $\ell$ odd;
   the Bloch-Kato local conditions at $p\ne\ell$, at $\ell$ (crystalline, with $p$-adic Hodge theory as a black box) and at
   $\infty$; their propagation to $T$ and $W$; the global Selmer groups $H^1_f$ and the $\Sigma$-imprimitive $H^1_\Sigma$ of DFG04
   Section 2.1; the Tamagawa factor $\Tam_p(M)=\Fitt_{\Zl}\bigl((H^1(I_p,M)_{\mathrm{tor}})^{G_{\Q_p}}\bigr)$ with the parenthesis in the right
   place (important_notes.md point 37).
2. **Lemma lem:fpr in full for $p\ne\ell$** (Fontaine and Perrin-Riou): $\Fitt H^1_f(\Q_p,T^D)=L_p(A_f,1)^{-1}\Tam_p(T^D)$, with the
   index description $\#\bigl(H^1_f(\Q_p,M)/H^1_{\mathrm{ur}}(\Q_p,M)\bigr)=\ell^{v_\ell(\Tam_p(M))}$, and $\Tam_p(T^D)=\Tam_p(A)$ proved in every case that occurs for an
   elliptic curve (DFG04 (57) in general).
3. **Lemma lem:tamfactor in full, every step**, assembled from Chapter 16 (the group cohomology), Chapter 7 and Chapter 17
   (the Kummer class and the identification of $c'$, important_notes.md point 7 and its addendum), Chapter 11 (the Tate shape with the corner
   $\varepsilon\kappa$, point 42), with the arithmetic Frobenius named (point 11), the reading of $v_\ell(c)$ fixed (point 31) and the class
   renamed $c(u)$ (point 23); its extension to additive potentially multiplicative primes, including $q=2$ (point 18).
4. **New: the Tamagawa factor of $\ad T$ at every additive prime.** It is trivial at every prime $q\ne\ell$ of potentially good
   reduction, for every odd $\ell$ (item 9.3: the image of inertia has order dividing $24$, and for $\ell=3$ the lattice $\ad T$ is
   free over $\Z_3[C_3]$). This answers the first half of the paper's Open question 3 and makes (eq:identity) fully explicit
   (item 9.4).
5. **The Selmer side of the proof of Theorem thm:main**: the exceptional set $S_f$, DFG04 Theorem 2.7 (stated), DFG04 Lemma 2.1
   (proved from Chapter 17's comparison of Selmer structures, with every term identified), the restatement of Lemma lem:h0
   in its corrected form (proved in Chapter 11; points 5, 6, 10, 14) as the identification $H^1_f(\Q,T^D)\simeq H^0(\Q,W^D)$, and the length
   identity $\len H^1_\Sigma=\len H^1_f+\sum(\text{Euler}+\text{Tamagawa})-h_\ell(E)$, which is the proof step of Theorem thm:main when $h_\ell(E)=0$ and
   Remark rem:ns when $h_3(E)=1$.
6. **Remark rem:ko(1), Section sec:tam, Open questions 2 and 3, the term $h_\ell(E)$ of Conjecture conj:euler**, with a
   reproduction of the Tamagawa test of Section sec:tam on conductors below $10{,}000$.
7. **The Tamagawa number conjecture and the adjoint motive**: the shape of the conjecture, BSD as the model case, the adjoint
   motive of $f$, $L(\ad f,s)=L(\Sym f,s+1)$ in the paper's normalisation, DFG04 Theorems 0.1 and 0.2 (stated), Flach's
   theorem; why (eq:identity) is the Tamagawa number conjecture for the adjoint read through the modular degree.

The physics reader appears twice, in one sentence each: a Tate twist is a change of "weight" exactly like multiplying a
field by a character of the scaling group (2.2); the Tamagawa factor is the size of a local "defect" counted by the
torsion of a first cohomology group, as an index of a sublattice is a volume ratio (7.2).

### 1.2 Split with the neighbouring chapters (decided here, consistent with PLAN.md Section 4 and the written outlines)

* **Chapter 3** proves Fitting ideals over $\Zl$ ($\Fitt(A)=\ell^{\len A}\Zl$ for finite $A$: its 7.4 to 7.6), lengths, Pontryagin duality and the
  duality between $T$ and $T\otimes\Qlmod$ (8.1 to 8.4). Cited, not reproved.
* **Chapter 4** proves the trace form and $\Hom(A,\Zl(\chi))\simeq A(\chi)$ for $\ell$ odd (its 7.6), the invariance of $\ad$ under twists, duals and
  homotheties (7.7), the cyclic and unipotent shapes (9.1 to 9.4), and the twist-length lemma behind $h_\ell$ (10.5).
* **Chapter 7** fixes the Frobenius conventions ($\Frob$ arithmetic, $\Phi=\Frob^{-1}$ geometric, $L(V,s)=\det(1-\Phi q^{-s}\mid V^{I})^{-1}$: its L3, L6, 8.2),
  proves the Kummer class on inertia and the field-theoretic half of the identification of $c'$ (6.2), and tabulates the local
  shapes and adjoint $L$-factors (9.1 to 9.4). Cited.
* **Chapter 10** defines the Tate parameter $q_E=\mathsf q(j_E)$, its unit part $u$ and the class $c(u)$ (its 7.2, 7.4), the component
  groups and $c_q$ (7.6), additive potentially multiplicative reduction (7.7) and Kraus's defect.
* **Chapter 11** proves the Tate shape with corner $\varepsilon\kappa$ (its 3.2), Lemma lem:tamagawa-exp (3.3), the potentially
  multiplicative case at every $q$ including $2$ (3.4), the inertia images by Kodaira type (Section 4), crystallinity at $\ell$ (5.1(ii),
  stated), and **Lemma lem:h0 in corrected form** (8.5) with the description of $S_f$ (8.6). Chapter 18 restates lem:h0 in Selmer
  language and does not reprove it.
* **Chapter 14** proves important_notes.md point 39 (its 9.1 to 9.5: $v_\lambda(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$ for the optimal curve) and
  lists the DFG04 checklist (9.6, point 56), now settled against the published DFG04 (Chapter 20 outline, Part 7; important_notes.md point 73). Chapter 18 cites it
  for "equality in (eq:identity)".
* **Chapter 16** proves the group cohomology of the Tate shape (its model-computation, frobenius-on-h1-inertia, procyclic-compact,
  inflation-restriction, lengths-in-exact-sequences). Chapter 18 cites those items for Steps 2 and 3 of Lemma lem:tamfactor and
  adds the definition of $\Tam$, the identification of $c'$ and the conclusion.
* **Chapter 17** (its outline `outlines/ch17_galcoh.md` is written) owns Galois cohomology proper: the Kummer duals $T^D$, $V^D$, $W^D$ in general (its 2.1), Kummer theory, Tate local duality for finite, compact and
  discrete coefficients, local Euler characteristics, $H^1_{\mathrm{ur}}$ and its annihilator, the cohomology of the real place, $G_{\Q,S}$,
  classical Selmer groups, Selmer structures and their duals, Greenberg-Wiles and Poitou-Tate, **the comparison exact sequence
  for two Selmer structures** (the abstract form of DFG04 Lemma 2.1), the sequences relating $H^1(K,T)$, $H^1(K,V)$, $H^1(K,W)$, and the
  Kummer class of the Tate parameter with $H^1(G/I,\Zl(1))=\Zl(1)/(q-1)$. Chapter 18 never reproves these; it instantiates them with the
  Bloch-Kato conditions. Chapter 18 needs from Chapter 17 exactly the items listed in Part 5 (inputs K1 to K8, with Chapter 17's item
  numbers): in particular the identification of $c'$ (its 5.3, 5.4), the propagation and orthogonality of local conditions (4.4, 4.5), $H^1_f(\Q_p,T^D)=H^1(\Q_p,T^D)_{\mathrm{tor}}\simeq H^0(\Q_p,W^D)$
  for $p\in\Sigma$ (4.6), and the abstract form of DFG04 Lemma 2.1 (10.3, 10.4). Chapter 18 adds the Bloch-Kato conditions, $\Tam_p$ and Lemma lem:fpr,
  the assembly of Lemma lem:tamfactor, Lemma lem:dfg21 in the paper's form (Chapter 17, 10.3 applied to the Bloch-Kato structure with DFG04
  Theorem 2.7 as hypothesis), and $T^D\simeq A(1)$.
* **Chapter 19** (outlined in parallel) owns $L$-functions: the table of omitted Euler factors, Lemma lem:euler, $e_\ell(E,q)$, $P_q$,
  the naive factor, $L(\Sym f,s)$ and the Rankin-Shimura formula. Chapter 18 uses only the values $v_\ell(L_q(A_f,1)^{-1})$ (stated with a
  `\Cref{ch:lfunctions}`) and their integrality (proved here, 3.5).
* **Chapter 20** owns congruence ideals and the DFG04 assembly: $\eta^\Sigma_{f,\lambda}$, Proposition 1.4 (thm:dfg14), Theorem 3.7
  (thm:dfg37), the Taylor-Wiles method, Lemma lem:ddt417, Lemma lem:hecke, and the proof of Theorem thm:main as an assembly.
  Chapter 18 supplies the Selmer half (Section 11 here: item 11.1) and Chapter 20 cites it. Theorems 0.1 and 0.2 of DFG04 are
  stated here (14.4, 14.5) because they are statements about Selmer groups and Tamagawa factors; Theorem 3.7 is stated here
  only as a pointer (14.5) and lives in Chapter 20.
* **Chapters 21, 22** use the card: the tour cites 7.1, 7.4, 8.2, 9.3, 10.4, 11.1, 12.1; the computation chapter uses 8.5 and 13.1.

### 1.3 Global conventions fixed in this chapter

* **C1 (objects).** As Chapter 11, C1: $E/\Q$ with global minimal model and conductor $N$; $\ell$ an odd prime unless said otherwise;
  $T=T_\ell E$, $V=T\otimes\Ql$, $\rho=\rho_{E,\ell}$, $\bar\rho$; $A=\ad T$ (trace zero, the paper's `\ad`), $A_f=\ad V=A\otimes\Ql$, $W=A\otimes\Qlmod$.
  $\Sigma$ is the set of primes dividing $N$ (so $\ell\notin\Sigma$ when $\ell\nmid N$). $\delta_p=\dim V^{I_p}$.
* **C2 (duals; important_notes.md B4).** For a $\Zl$-module $M$: $M^\vee=\Hom_{\Zl}(M,\Zl)$ (linear dual; $V^\vee=\Hom_{\Ql}(V,\Ql)$; Bloch-Kato and
  PLAN.md write $V^*$); $M(n)=M\otimes\Zl(1)^{\otimes n}$; the **Kummer (Cartier) dual** $M^D=\Hom_{\Zl}(M,\Zl(1))=M^\vee(1)$, and for the paper's
  objects $T^D=\Hom(A,\Zl(1))$, $V^D=T^D\otimes\Ql=A_f^\vee(1)$, $W^D=V^D/T^D=\Hom(A,\Qlmod(1))$; the **Pontryagin dual** of a compact or discrete
  $\ell$-primary module is $X^*=\Hom_{\mathrm{cont}}(X,\Qlmod)$, the paper's ${}^*$ (as in Chapter 16). The symbol ${}^*$ never means a linear dual
  in this chapter.
* **C3 (Frobenius; points 11, B1, B6, B7).** As Chapter 7, L3 and L6: $\Frob_p$ is an arithmetic Frobenius, $\Phi_p=\Frob_p^{-1}$ the
  geometric one. Group-theoretic statements (conjugation on $H^1(I_p,-)$, the Tate matrices, Lemma lem:tamfactor) use $\Frob_p$;
  $L$-factors use $\Phi_p$: $L_p(M,s)=\det(1-\Phi_pp^{-s}\mid M^{I_p})^{-1}$. Consequences: $L_p(M(1),s)=L_p(M,s+1)$, so
  $L_p(A_f(1),0)=L_p(A_f,1)$ (Lemma lem:fpr); $L_p(V_\ell E,s)=L_p(E,s+1)$ while $L_p(E,s)=L_p(V_\ell E^\vee,s)$ (Chapter 7, 8.2(v); B7, B9).
  On $V_\ell E$ at a good prime the arithmetic Frobenius has eigenvalues $\alpha,\beta$ (roots of $X^2-a_pX+p$), the geometric one
  $\alpha^{-1},\beta^{-1}$; on $A_f$ both give $\alpha/\beta,1,\beta/\alpha$ (B1). In cohomology the choice is invisible:
  $(\Frob-1)M=(\Phi-1)M$, and $\det(1-\Frob\mid X)$, $\det(1-\Phi\mid X)$ have the same $\ell$-adic valuation for a lattice $X$ (they differ by the unit
  $\det(-\Phi\mid X)$); but as rational numbers only $\det(1-\Phi\mid(V^D)^{I_p})$ equals $L_p(A_f,1)^{-1}$.
* **C4 (Hodge-Tate weights).** $\Ql(1)$ has Hodge-Tate weight $1$, so $V_\ell E$ has weights $\{0,1\}$ (as Chapter 15, 4.1), $A_f$ has
  $\{-1,0,1\}$, $V^D=A_f(1)$ has $\{0,1,2\}$. Some sources (including, possibly, DFG04 and BlochKato) use the opposite sign; every
  formula below that depends on the sign (4.5) says so.
* **C5 (cohomology).** Continuous cochain cohomology throughout (Chapter 16, continuous-cohomology), with coefficients of type
  (D), (C), (V) as there; $H^i(K,M)=H^i(G_K,M)$; $H^i(\R,M)=H^i(\Gal(\C/\R),M)$; $G_{\Q,S}$ for a finite set $S$ of places containing
  $\ell$, $\infty$ and the primes where $M$ ramifies. "Length" is $\Zl$-length; $v_\ell$ of a nonzero ideal $\ell^a\Zl$ is $a$.
* **C6 (Tate data at a prime with $v_q(j)<0$; points 8, 23, 31, 42).** $q_E=\mathsf q(j_E)\in\Q_q^\times$ the Tate parameter (Chapter 10, 7.4), never
  called $u$; $\nu=v_q(q_E)=-v_q(j_E)$ ($=n=n_q$ at a multiplicative prime); $u=q_Eq^{-\nu}\in\Z_q^\times$ its unit part and $\bar u\in\F_q^\times$ its
  reduction; $c(u)$ the class of $\bar u$ in $\F_q^\times/(\F_q^\times)^{\ell^{v_\ell(q-1)}}$, and $v_\ell(c(u))$ is the largest $k\le v_\ell(q-1)$ with $\bar u\in(\F_q^\times)^{\ell^k}$ (so
  "$v_\ell(0)$" reads $v_\ell(q-1)$). The paper writes $c$ in Lemma lem:tamfactor and $c_q$ in Section sec:tam; the book writes $c(u)$
  (or $c_q(u)$) and keeps $c_q$ for the Tamagawa number. $\varepsilon$ is the unramified character with $\varepsilon(\Frob_q)=a_q(E)=\pm1$ (multiplicative
  case) and the corner of the Tate matrices is $\varepsilon\kappa$.
* **C7 (characters).** $\chi_\ell$ the cyclotomic character, $\bar\chi_\ell$ its reduction, $\chi_{-3}$, $\chi_{-4}$, $\chi_{q^*}$ quadratic (Chapter 11,
  C4; point 32). $\bar\chi_3=\chi_{-3}$.
* **C8 (typography and labels).** PLAN.md 7.2: no dash ligatures ("Bloch-Kato", "Fontaine-Perrin-Riou", "Diamond-Flach-Guo",
  "Poitou-Tate", "Greenberg-Wiles", "Fontaine-Laffaille", "Taylor-Wiles" with plain hyphens; ranges "1 to 8"); ASCII source;
  labels `...:blochkato:...`; the names in the line-up are the label stems.

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 1. Overview and conventions

**1.1 `conv:blochkato:setup`** (conventions C1 to C8 as `convention` environments, with a roadmap; P). A table "sentence of
the paper $\to$ item" for Section 1.2, the proof of Theorem thm:main, Lemma lem:tamfactor, Lemma lem:fpr, Remark rem:ko(1),
Remark rem:ns, Section sec:tam, Open questions 2 and 3. Paper: background.

### Section 2. $\ell$-adic representations, lattices, twists and duals

**2.1 `def:blochkato:l-adic-rep`** (definition and proposition; P). Let $K$ be a field and $G_K$ its absolute Galois group. An
$\ell$-adic representation is a finite-dimensional $\Ql$-vector space $V$ with a continuous homomorphism $G_K\to\GL(V)$. (i) $V$ has a
$G_K$-stable $\Zl$-lattice $T$ (the image of $G_K$ is compact, so the sum of the translates of any lattice is a lattice). (ii) Put
$W=V/T=T\otimes\Qlmod$, a discrete $\ell$-primary $G_K$-module; $0\to T\to V\to W\to0$ is exact with a continuous section (Chapter 16,
les-continuous (iii)), and $W[\ell^k]\simeq T/\ell^kT$ (Chapter 3, 8.3). (iii) Any two stable lattices are commensurable; if $T/\ell T$ is absolutely
irreducible all stable lattices are homothetic (Chapter 4, 10.3). Reference: SerreAbelian, Chapter I; Rubin, Section 1.1. Paper:
Section 1.1 ($V$, $T$), Section 4.2 ($A$, $W$).

**2.2 `def:blochkato:twists`** (definition and proposition; P). $\Zl(1)=\varprojlim\mu_{\ell^k}$ with $G_K$ acting by $\chi_\ell$ (Chapter 5), $\Ql(1)=\Zl(1)\otimes\Ql$,
$\Zl(n)=\Zl(1)^{\otimes n}$ ($n\in\Z$, negative powers via the dual), $M(n)=M\otimes\Zl(n)$. (i) $M(n)(m)=M(n+m)$, $\Hom(M(n),N)=\Hom(M,N)(-n)$.
(ii) For $p\ne\ell$, $I_p$ acts trivially on $\Zl(1)$ and $\Frob_p$ acts by $p$; so $M(n)^{I_p}=M^{I_p}(n)$ and the Frobenius eigenvalues on
$M(n)^{I_p}$ are those on $M^{I_p}$ times $p^n$ (arithmetic) or $p^{-n}$ (geometric). (iii) $\wedge^2T_\ell E\simeq\Zl(1)$ by the Weil pairing, hence
$T_\ell E^\vee\simeq T_\ell E(-1)$ (Chapter 9). Physics aside (one sentence): a twist rescales Frobenius eigenvalues by a power of $p$ as a
character of the scaling group rescales a field of given weight. Reference: Rubin 1.1; Washington. Paper: Section 4.2 ($\Zl(1)$,
$A(1)$), Lemma lem:h0 ($\ad T(1)$), Lemma lem:fpr ($A_f(1)$).

**2.3 `def:blochkato:duals`** (definition and proposition; recalled from Chapter 17, 2.1, which proves (i), (ii); P for (iii), (iv)). Conventions C2. (i) $V^D=V^\vee(1)$, $T^D=T^\vee(1)$, $W^D=V^D/T^D$; then
$W^D\simeq\Hom_{\Zl}(T,\Qlmod(1))=\Hom(T,\mu_{\ell^\infty})$ and $T^D\simeq\Hom(W,\mu_{\ell^\infty})$, so the evaluation pairings $T\times W^D\to\Qlmod(1)$ and
$W\times T^D\to\Qlmod(1)$ are perfect and $G_K$-equivariant (Chapter 3, 8.2, 8.3). (ii) $(T^D)^D=T$. (iii) $X^*$ (Pontryagin) of a finite
module has the same length; the only Pontryagin duals in the paper are of finite groups (Lemma lem:dfg21). (iv) Dictionary with the literature: Bloch-Kato and FPR94 write $V^*(1)$ for $V^D$; DFG04 write $T^D$, $V^D$, $W^D$ exactly
as the paper. Reference: BlochKato Section 3; Rubin 1.1; DFG04 Section 2.1. Paper: Section 4.2 ($T^D$, $V^D$, $W^D$), Lemma
lem:dfg21 ($^*$).

**2.4 `prop:blochkato:adjoint-self-dual`** (proposition; P given Chapter 4, 7.6 and 7.7). Let $\ell$ be odd and $A=\ad T$. (i) The trace form
$(x,y)\mapsto\tr(xy)$ is a perfect $G_K$-invariant pairing on $A$ (Gram determinant $-2$ in the basis $e,h,f$), so $A\simeq A^\vee$ and
$$T^D=\Hom(A,\Zl(1))\simeq A(1),\qquad V^D\simeq A_f(1),\qquad W^D\simeq\ad T(1)\otimes\Qlmod .$$
For $\ell=2$ the image of $A$ in $A^\vee$ has index $2$. (ii) $\ad$ is insensitive to twisting $T$ by a character, to replacing $T$ by a homothetic
lattice or by $T^\vee$: hence $\ad M_{f,\lambda}=\ad T_\ell E$ for the lattice $M_{f,\lambda}=\varphi_E^*H^1(E,\Zl)\simeq T_\ell E(-1)$ of the optimal curve (Chapter 14,
9.1(d); important_notes.md points 26, 40), and $\ad T$ is the same $G_{\Q_q}$-module for $E$ and for any quadratic twist of $E$. Paper:
Section 4.2 ("$T^D=\Hom(A,\Zl(1))\simeq A(1)$ (via the trace form)", "$M_{f,\lambda}$ and $T_\ell E$ are homothetic ... so their adjoints coincide"),
Lemma lem:h0, proof of Theorem thm:main ($\mathrm I_n^*$ primes: "$\ad T$ is unchanged by the twist").

**2.5 `def:blochkato:geometric`** (definition and theorem; R, with (iii) P given Chapter 9). (i) An $\ell$-adic representation $V$ of $G_\Q$ is
*geometric* (Fontaine-Mazur) if it is unramified outside a finite set of primes and de Rham at $\ell$ (4.1). (ii) $V_\ell E$, $\Ql(n)$, and
every tensor construction on them ($A_f$, $V^D$, $\Sym V$) are geometric (4.2, 4.3; Grothendieck for $p\ne\ell$). (iii) (purity at good
primes) For $p\nmid N\ell$ the arithmetic Frobenius eigenvalues on $V_\ell E$ have absolute value $p^{1/2}$ (Hasse; Chapter 9), so those on $A_f$
have absolute value $1$ and those on $V^D=A_f(1)$ absolute value $p$. Reference: Fontaine-Mazur (cite through Berger, Section 1;
verify); Chapter 9, Hasse bound. Paper: background (the shape of the Bloch-Kato conjecture; 3.3).

**2.6 `ex:blochkato:adjoint-of-E`** (worked example; P). For $E$ and odd $\ell$ with $\bar\rho$ absolutely irreducible: (i) $H^0(\Q,A_f)=0$ and
$H^0(\Q,W)=0$ ($H^0(\Q,W)[\ell]=H^0(\Q,\ad\bar\rho)$ consists of trace-zero scalars by Schur, which are $0$ as $2$ is invertible; Chapter 16,
h0-and-torsion). (ii) $H^0(\Q,V^D)=0$ for every $E$ (by 2.5(iii) no Frobenius eigenvalue on $V^D$ at a good prime equals $1$). (iii) $H^0(\Q,W^D)$ is
finite, cyclic, of length $h_\ell(E)$ (Chapter 11, 8.5; restated in 10.3). (iv) The three modules $A$, $A(1)=T^D$ and $A(-1)$ are pairwise
non-isomorphic, and only $A(1)$ carries the Tamagawa and Euler data that enter Lemma lem:fpr. Paper: Section 4.2, Lemma lem:h0,
Theorem thm:dfg27 ("$H^0(\Q,V^D)=0$").

### Section 3. Local behaviour at $p\ne\ell$: invariants, Euler factors, weights

**3.1 `conv:blochkato:frobenius-dictionary`** (convention with proofs; P). Convention C3 with its four consequences proved:
(a) $L_p(M(1),s)=L_p(M,s+1)$ with $\Phi_p$, and $L_p(M(1),s)=L_p(M,s-1)$ would follow with $\Frob_p$ (so the paper's
"$L_p(A_f,1)^{-1}=L_p(A_f(1),0)^{-1}$" forces $\Phi_p$; point 11); (b) $(\Frob-1)X=(\Phi-1)X$ for any $\Frob$-stable $X$; (c) for a lattice $X$ with
$\det(1-\Phi\mid X)\ne0$, $\#X/(\Frob-1)X=\ell^{v_\ell(\det(1-\Phi\mid X))}$ (the Smith form of $\Frob-1$, and $\det\Frob\in\Zl^\times$); (d) on $V_\ell E$ the
geometric Frobenius gives $L_p(E,s+1)$ and the dual gives $L_p(E,s)$ (Chapter 7, 8.2(v); important_notes.md B7, B9). Reference: Chapter 7, L3,
L6, 8.2; DFG04 Section 1.7.2 (checked: DFG04 use the geometric Frobenius; Chapter 20 outline, Part 7; important_notes.md point 73). Paper: Section 1.1 ($L_p(A_f,s)$), the paragraph after Lemma lem:dfg21, Lemma lem:fpr,
Lemma lem:tamfactor (arithmetic $\Frob$).

**3.2 `prop:blochkato:local-adjoint`** (proposition and table; P given Chapter 7, 9.4 and Chapter 11, 3.2, 3.4, Section 4). Let $p\ne\ell$. The
inertia invariants and the Frobenius action on $A_f$ and on $V^D=A_f(1)$, by reduction type at $p$ (eigenvalues of $\Phi_p$; those of
$\Frob_p$ are the inverses):

| reduction at $p$ | $\delta_p$ | $\dim A_f^{I_p}$ | $\Phi_p$ on $A_f^{I_p}$ | $\Phi_p$ on $(V^D)^{I_p}$ | $L_p(A_f,1)^{-1}=\det(1-\Phi_p\mid(V^D)^{I_p})$ |
|-|-|-|-|-|-|
| good | 2 | 3 | $\alpha/\beta,1,\beta/\alpha$ | $p^{-1}\alpha/\beta,p^{-1},p^{-1}\beta/\alpha$ | $(1-\frac\alpha{\beta p})(1-\frac1p)(1-\frac\beta{\alpha p})$ |
| multiplicative $\mathrm I_n$ | 1 | 1 | $p^{-1}$ | $p^{-2}$ | $1-p^{-2}$ |
| $\mathrm I_n^*$ (potentially multiplicative) | 0 | 1 | $p^{-1}$ | $p^{-2}$ | $1-p^{-2}$ |
| $\mathrm I_0^*$ (twist of good $E'$) | 0 | 3 | as for $E'$ | as for $E'$ | $\frac{p-1}p\cdot\frac{(p+1)^2-a_p(E')^2}{p^2}$ |
| inertia cyclic of order 3 or 6 | 0 | 1 | $\chi_{-3}(p)$ | $\chi_{-3}(p)p^{-1}$ | $1-\chi_{-3}(p)p^{-1}$ |
| inertia cyclic of order 4 | 0 | 1 | $\chi_{-4}(p)$ | $\chi_{-4}(p)p^{-1}$ | $1-\chi_{-4}(p)p^{-1}$ |
| inertia non-abelian ($p=2$: $Q_8$, $\SL_2(\F_3)$) | 0 | 0 | none | none | $1$ |

For $p\ge5$ the last three rows are the Kodaira types $\mathrm{II},\mathrm{II}^*,\mathrm{IV},\mathrm{IV}^*$; $\mathrm{III},\mathrm{III}^*$; (none); at $p=2$ type
$\mathrm{IV},\mathrm{IV}^*$ is the order-$3$ row (point 43); at $p=2,3$ the type does not determine the row (Remark rem:wild; Chapter 19 computes $P_p$
with PARI). The table is a citation: the values of $e_\ell(E,p)$ and Lemma lem:euler are Chapter 19's. Paper: Section 1.1, the table of
Section 1, Lemma lem:fpr ("valuation $e_\ell(E,p)$ at an additive prime and $v_\ell(1-p^{-2})$ at a multiplicative one"), the paragraph after
Lemma lem:dfg21.

**3.3 `lem:blochkato:no-local-invariants`** (lemma; P). Let $p\ne\ell$. (i) $H^0(\Q_p,V^D)=0$, and $\det(1-\Phi_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}$ is a
nonzero rational number. (ii) $H^0(\Q_p,A_f)$ is the $\Phi_p$-fixed part of $A_f^{I_p}$: it is $0$ at multiplicative primes, at $\mathrm I_n^*$ primes, at
the cyclic primes of 3.2 with $\chi_{-3}(p)=-1$ (resp. $\chi_{-4}(p)=-1$) and at the non-abelian primes; it is a line at good primes ($\alpha\ne\beta$
because $a_p^2\ne4p$) and at the cyclic primes with $\chi(p)=+1$; at an $\mathrm I_0^*$ prime it contains the line of the eigenvalue $1$. Proof: read
off 3.2; for (i) every eigenvalue of $\Phi_p$ on $(V^D)^{I_p}$ has complex absolute value $p^{-1}$ (2.5(iii) and the table), so none is $1$. **Warning
for the writer:** $H^0(\Q_p,A_f)\ne0$ does occur at bad primes (for example type $\mathrm{III}$ at $p\equiv1\pmod4$, and every $\mathrm I_0^*$ prime), so
$H^1(\Q_p,T^D)$ need not be finite there (3.4); only (i) enters the paper's argument. Paper: the paragraph after Lemma lem:dfg21
("$\det(1-\Frob_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}\ne0$", true with $\Frob_p$ read as geometric), Lemma lem:fpr ("a nonzero rational number").

**3.4 `cor:blochkato:local-finiteness`** (corollary; P given Chapter 17's local Euler characteristic and Tate local duality, inputs K1, K2).
Let $p\ne\ell$. (i) $H^1(\Q_p,T^D)$ is a finitely generated $\Zl$-module of rank $\dim H^0(\Q_p,V^D)+\dim H^0(\Q_p,A_f)=\dim H^0(\Q_p,A_f)$ (by 3.3(i)). (ii)
In particular, at every $p\in\Sigma$ where $H^0(\Q_p,A_f)=0$ (multiplicative and $\mathrm I_n^*$ primes, cyclic primes with $\chi(p)=-1$, non-abelian
primes), $H^1(\Q_p,T^D)$ is **finite**, equal to its torsion, and $H^1(\Q_p,W)\simeq H^1(\Q_p,T^D)^*$ is finite. (iii) In all cases
$H^1(\Q_p,T^D)_{\mathrm{tor}}$ is finite (Chapter 16, h1-finitely-generated). Paper: the paragraph after Lemma lem:dfg21 ("$H^1_f(\Q_p,T^D)$ is the torsion
of $H^1(\Q_p,T^D)$, a finite group").

**3.5 `lem:blochkato:euler-integral`** (lemma; P). For $p\ne\ell$ let $X=T^D$. Then $X^{I_p}$ is a $\Phi_p$-stable lattice in $(V^D)^{I_p}$, so
$L_p(A_f,1)^{-1}=\det(1-\Phi_p\mid X^{I_p})\in\Z_{(\ell)}\cap\Q^\times$ and $\#X^{I_p}/(\Frob_p-1)X^{I_p}=\ell^{v_\ell(L_p(A_f,1)^{-1})}$ (3.1(c), 3.3(iii)). Its valuation is $v_\ell(1-p^{-2})=v_\ell(p^2-1)$ at
multiplicative and $\mathrm I_n^*$ primes, and $e_\ell(E,p)$ at additive primes (Definition def:terms: the naive factor is $1$ there; values in
Chapter 19). Paper: Lemma lem:fpr ("a nonzero rational number which is an $\ell$-adic integer"), Theorem thm:dfg14 (the factor $1-p^{-2}$).

### Section 4. The representation at $\ell$: $p$-adic Hodge theory as a black box

The section opens by saying that nothing in the paper's proofs uses $p$-adic Hodge theory directly: it enters only through
the definition of $H^1_f(\Q_\ell,-)$ and through DFG04. Everything here is R, with precise statements.

**4.1 `def:blochkato:period-rings`** (definition; R). Fontaine's rings $B_{\mathrm{dR}}\supset B_{\mathrm{st}}\supset B_{\mathrm{cris}}$ for $\Q_\ell$, with $G_{\Q_\ell}$-actions,
the filtration on $B_{\mathrm{dR}}$ ($\mathrm{gr}^iB_{\mathrm{dR}}\simeq\C_\ell(i)$), the Frobenius $\varphi$ on $B_{\mathrm{cris}}$ and $B_{\mathrm{st}}$, the monodromy $N$ on $B_{\mathrm{st}}$,
$B_{\mathrm{dR}}^{G_{\Q_\ell}}=B_{\mathrm{cris}}^{G_{\Q_\ell}}=\Q_\ell$. For $V$ an $\ell$-adic representation of $G_{\Q_\ell}$: $D_\bullet(V)=(B_\bullet\otimes V)^{G_{\Q_\ell}}$, $\dim D_\bullet(V)\le\dim V$,
and $V$ is de Rham, semistable, crystalline if equality holds for $\bullet=\mathrm{dR},\mathrm{st},\mathrm{cris}$; crystalline $\Rightarrow$ semistable $\Rightarrow$ de
Rham. Hodge-Tate weights with convention C4. Reference: Fontaine (Asterisque 223); Berger (Sections 2 to 4). Paper: background (the
definition of $H^1_f$ at $\ell$, Section 1.2).

**4.2 `thm:blochkato:crystalline-good-reduction`** (theorem; R). Let $A/\Q_\ell$ be an abelian variety. $V_\ell A$ is crystalline iff $A$ has good
reduction (Fontaine; Coleman-Iovita for the converse), semistable iff $A$ has semistable reduction; for $E$ with good reduction at
$\ell$, $D_{\mathrm{cris}}(V_\ell E)$ is two-dimensional with $\varphi$ of characteristic polynomial $X^2-a_\ell X+\ell$ (in the normalisation where $V_\ell E$ has
Hodge-Tate weights $0,1$; verify the inverse-polynomial convention in Berger) (Chapter 11, 5.1(ii); Chapter 15, 4.1(ii)). Reference:
Berger, Section 4 (verify); Fontaine. Paper: Theorem thm:main ($\ell\nmid N$: crystalline at $\ell$, through DFG04).

**4.3 `prop:blochkato:crystalline-closure`** (proposition; R for the formal properties, P for the consequences). Crystalline
representations are stable under $\oplus$, $\otimes$, duals, subquotients and Tate twists, and $D_{\mathrm{cris}}$ is compatible with these. Hence for
$\ell\nmid N$: $A_f$, $A_f(1)=V^D$ and $V_\ell E^\vee$ are crystalline, with Hodge-Tate weights $\{-1,0,1\}$, $\{0,1,2\}$, $\{-1,0\}$. Paper: Theorem
thm:main (the Bloch-Kato condition at $\ell$ for $W$ and $W^D$).

**4.4 `thm:blochkato:fontaine-laffaille`** (theorem; R). For $\ell$ odd, the functor of Fontaine and Laffaille is an equivalence between
filtered Dieudonne modules over $\Zl$ with weights in an interval of length at most $\ell-2$ and $G_{\Q_\ell}$-stable lattices in crystalline
representations with Hodge-Tate weights in that interval; it is exact and compatible with subquotients. For $V_\ell E$ ($\ell\nmid N$,
weights $\{0,1\}$) this applies for $\ell\ge3$, and it identifies $T_\ell E$ with the lattice of the finite flat group schemes $\mathcal E[\ell^k]$ (Chapter
11, 5.1(i)). DFG04 (Sections 1 and 2) use this theory to define integral structures and the local condition at $\ell$ for the
adjoint. **Settled (Part 7, Q1; Chapter 20 outline, Part 7; important_notes.md point 73):** although the adjoint has weights spanning an interval of length $2$, which exceeds
$\ell-2$ when $\ell=3$, DFG04 (31) excludes only the primes dividing $Nk!$ ($=2N$ in weight $2$) and the residually induced case, and the local
condition at $\ell$ is defined through extensions of short objects (DFG04 Proposition 2.2, Corollary 2.3, needing only $\ell>2$); so DFG04
Theorem 3.7 covers $\ell=3$ in weight $2$ and the paper's reading of $S_f$ is the complete list of excluded primes. Reference: FontaineLaffaille; DFG04 Sections 1.1 to 1.3 and 2.1 (verify the
section numbers); BlochKato Section 4. Paper: background (DFG04's hypotheses), the optimal-level paragraph ("good" at $\ell$).

**4.5 `prop:blochkato:dimension-formula`** (proposition; R). For $V$ de Rham, with convention C4:
$$\dim_{\Ql}H^1_f(\Q_\ell,V)=\dim H^0(\Q_\ell,V)+\dim D_{\mathrm{dR}}(V)/\mathrm{Fil}^0D_{\mathrm{dR}}(V),$$
and $\dim D_{\mathrm{dR}}/\mathrm{Fil}^0$ is the number of positive Hodge-Tate weights (counted with multiplicity). For $\ell\nmid N$: $\dim H^1_f(\Q_\ell,A_f)=1$,
$\dim H^1_f(\Q_\ell,V^D)=2$, and $1+2=3=\dim H^1(\Q_\ell,A_f)$, as the duality 5.4 requires. Examples: $H^1_f(\Q_\ell,\Ql(1))=\Zl^\times\hat\otimes\Ql$ (dimension $1$),
$H^1_f(\Q_\ell,\Ql)=H^1_{\mathrm{ur}}(\Q_\ell,\Ql)$ (dimension $1$). Reference: BlochKato Corollary 3.8.4 (verify the number); Berger; Rubin 1.3. Paper:
background (6.7, the Euler-characteristic check).

### Section 5. Bloch-Kato local conditions

**5.1 `def:blochkato:local-conditions`** (definition; P for the equalities stated). Let $V$ be an $\ell$-adic representation of $G_{\Q_p}$.
(i) For $p\ne\ell$: $H^1_f(\Q_p,V)=H^1_{\mathrm{ur}}(\Q_p,V)=\ker\bigl(H^1(\Q_p,V)\to H^1(I_p,V)\bigr)=H^1(G_{\Q_p}/I_p,V^{I_p})$ (inflation-restriction, Chapter 16).
(ii) For $p=\ell$: $H^1_e=\ker(H^1(\Q_\ell,V)\to H^1(\Q_\ell,B_{\mathrm{cris}}^{\varphi=1}\otimes V))$, $H^1_f=\ker(H^1(\Q_\ell,V)\to H^1(\Q_\ell,B_{\mathrm{cris}}\otimes V))$,
$H^1_g=\ker(H^1(\Q_\ell,V)\to H^1(\Q_\ell,B_{\mathrm{dR}}\otimes V))$, with $H^1_e\subseteq H^1_f\subseteq H^1_g$; $H^1_f(\Q_\ell,V)$ classifies the crystalline extensions of $\Ql$ by $V$. (iii) At
$\infty$: $H^1_f(\R,V)=0$ ($=H^1(\R,V)$, which is $0$ anyway, Chapter 16, z2-on-l-adic). Only $H^1_f$ is used in the paper; $H^1_e$, $H^1_g$ are defined
for orientation. Reference: BlochKato Section 3 (Definition 3.7, verify); FPR94 I.3 (verify); Rubin 1.3. Paper: Section 1.2 ("the
Bloch-Kato Selmer group"), Section 4.2 ($H^1_f(\Q_p,V^D)$).

**5.2 `def:blochkato:propagation`** (definition; P). For a stable lattice $T\subset V$, $W=V/T$, $\iota\colon H^1(\Q_p,T)\to H^1(\Q_p,V)$, $\pi\colon H^1(\Q_p,V)\to H^1(\Q_p,W)$:
$H^1_f(\Q_p,T)=\iota^{-1}H^1_f(\Q_p,V)$ and $H^1_f(\Q_p,W)=\pi H^1_f(\Q_p,V)$; likewise $H^1_f(\Q_p,T^D)$, $H^1_f(\Q_p,W^D)$ from $V^D$. Properties: (a)
$H^1_f(\Q_p,T)\supseteq H^1(\Q_p,T)_{\mathrm{tor}}=\ker\iota$; (b) $H^1_f(\Q_p,W)\simeq(\Qlmod)^{\dim H^1_f(\Q_p,V)}$ is divisible (the image of $H^1_f(\Q_p,T)$ in $H^1_f(\Q_p,V)$ is a lattice), so it is $0$ exactly when
$H^1_f(\Q_p,V)=0$; (c) $H^1_f(\Q_p,T)/H^1(\Q_p,T)_{\mathrm{tor}}$ is a lattice in $H^1_f(\Q_p,V)$. Reference: BlochKato Section 3;
Rubin 1.3 (verify). Paper: Lemma lem:dfg21 ("$H^1_f(\Q_p,T^D)=\iota^{-1}H^1_f(\Q_p,V^D)$").

**5.3 `prop:blochkato:local-unramified`** (proposition; P given Chapter 16, procyclic-compact and inflation-restriction, and Chapter 17,
$H^1_{\mathrm{ur}}$, input K3). Let $p\ne\ell$ and $T$ a $G_{\Q_p}$-stable lattice. (i) $H^1_f(\Q_p,V)=V^{I_p}/(\Frob_p-1)V^{I_p}$, of dimension
$\dim H^0(\Q_p,V)$. (ii) There is an exact sequence $0\to H^1_{\mathrm{ur}}(\Q_p,T)\to H^1(\Q_p,T)\to H^1(I_p,T)^{G_{\Q_p}}\to0$ (the $H^2$ of $\widehat\Z$ vanishes on
type (C) modules), with $H^1_{\mathrm{ur}}(\Q_p,T)=T^{I_p}/(\Frob_p-1)T^{I_p}$. (iii) $H^1_f(\Q_p,T)$ is the preimage of $H^1(I_p,T)_{\mathrm{tor}}$, so
$$H^1_f(\Q_p,T)/H^1_{\mathrm{ur}}(\Q_p,T)\;\simeq\;\bigl(H^1(I_p,T)_{\mathrm{tor}}\bigr)^{G_{\Q_p}}.$$
(iv) $H^1_f(\Q_p,W)$ is the maximal divisible subgroup of $H^1_{\mathrm{ur}}(\Q_p,W)$. (v) If $H^0(\Q_p,V)=0$ then $H^1_f(\Q_p,V)=0$, $H^1_f(\Q_p,W)=0$ and
$H^1_f(\Q_p,T)=H^1(\Q_p,T)_{\mathrm{tor}}$; if moreover $H^0(\Q_p,V^D)=0$ then $H^1(\Q_p,T)$ is finite and $H^1_f(\Q_p,T)=H^1(\Q_p,T)$ (3.4). Paper: the paragraph
after Lemma lem:dfg21 ("$H^1_f(\Q_p,V^D)=H^1_{\mathrm{ur}}(\Q_p,V^D)=(V^D)^{I_p}/(\Frob_p-1)$ vanishes ... so $H^1_f(\Q_p,T^D)$ is the torsion of $H^1(\Q_p,T^D)$"), Lemma
lem:fpr.

**5.4 `prop:blochkato:local-duality-f`** (proposition; P for $p\ne\ell$ given Chapter 17's Tate local duality and the annihilator of
$H^1_{\mathrm{ur}}$, inputs K1, K4; R for $p=\ell$). Under the local Tate pairing $H^1(\Q_p,V)\times H^1(\Q_p,V^D)\to H^2(\Q_p,\Ql(1))=\Ql$ the subspaces
$H^1_f(\Q_p,V)$ and $H^1_f(\Q_p,V^D)$ are exact annihilators of each other, for every $p$ (for $p=\ell$: BlochKato Proposition 3.8, verify). Integrally,
under the perfect pairing $H^1(\Q_p,W)\times H^1(\Q_p,T^D)\to\Qlmod$, the exact annihilator of $H^1_f(\Q_p,W)$ is $H^1_f(\Q_p,T^D)$, hence
$$H^1(\Q_p,W)/H^1_f(\Q_p,W)\simeq H^1_f(\Q_p,T^D)^*.$$
Proof for $p\ne\ell$: the $\Ql$ statement from the unramified annihilator and dimensions (5.3(i), 3.3); the integral statement by
taking preimages and images (Rubin, Proposition 1.4.3, or Flach, verify). Paper: Lemma lem:dfg21 (the local terms $H^1_f(\Q_p,T^D)^*$).

**5.5 `ex:blochkato:ur-versus-f`** (worked example and warning; P). "Unramified" and "$f$" differ for $W$. Let $E$ have split multiplicative
reduction at $p\ne\ell$ with $\ell\mid n_p$, and $W=E[\ell^\infty]$. Then $H^1_f(\Q_p,V_\ell E)=0$ (the $\Frob_p$-eigenvalue on $V^{I_p}=\Ql e_1$ is $p\ne1$), so
$H^1_f(\Q_p,W)=0$, while $W^{I_p}=(\Qlmod)e_1\oplus(\Z/\ell^{v_\ell(n_p)})e_2$ and $H^1_{\mathrm{ur}}(\Q_p,W)=W^{I_p}/(\Frob_p-1)W^{I_p}\simeq\Z/\ell^{v_\ell(n_p)}\ne0$: the $\ell$-part of the
component group. This is the classical fact that the Kummer condition at $p\ne\ell$ is $E(\Q_p)\otimes\Qlmod=0$, not the unramified one, and the reason
Tamagawa factors appear. For the adjoint at a multiplicative prime $H^1_f(\Q_q,W)=0$ always (5.3(v), 3.3), and $H^1_{\mathrm{ur}}(\Q_q,W)=0$ when $\ell\nmid n_q$
(Exercise 4). Paper: background to Lemma lem:dfg21 and Lemma lem:fpr (the difference between the "unramified" and "Bloch-Kato" conditions
in DFG04's $H^1_\Sigma$).

### Section 6. Global Bloch-Kato Selmer groups and the $\Sigma$-imprimitive Selmer group

**6.1 `def:blochkato:selmer`** (definition and proposition; P). Let $M$ be one of $V,T,W,V^D,T^D,W^D$ for a geometric $V$ of $G_\Q$, and $S$ a
finite set of places containing $\ell$, $\infty$ and the primes where $V$ ramifies. $H^1_f(\Q,M)=\{c\in H^1(G_{\Q,S},M):\operatorname{loc}_p(c)\in H^1_f(\Q_p,M)\text{ for all }p\in S\}$.
It does not depend on $S$: for $p\notin S$, $H^1_f(\Q_p,M)=H^1_{\mathrm{ur}}(\Q_p,M)$ (5.3, $M$ unramified), and a class of $H^1(\Q,M)$ unramified outside $S$ comes
from $G_{\Q,S}$ (inflation-restriction). Reference: BlochKato Section 5 (verify); Rubin 1.5; DFG04 Section 2.1. Paper: Section 1.2 ("Let
$H^1_f(\Q,\ad T\otimes\Qlmod)$ be the Bloch-Kato Selmer group"), Section 4.2.

**6.2 `prop:blochkato:selmer-relations`** (proposition; P given Chapter 17's $T$, $V$, $W$ sequences, input K6, R for (iii)). (i)
$H^1_f(\Q,T)$ is the preimage of $H^1_f(\Q,V)$ under $H^1(G_{\Q,S},T)\to H^1(G_{\Q,S},V)$, and $H^1_f(\Q,T)_{\mathrm{tor}}=H^1(G_{\Q,S},T)_{\mathrm{tor}}$ is the image of $H^0(\Q,W)$.
(ii) $H^1_f(\Q,W)$ is a cofinitely generated $\Zl$-module. (iii) Its maximal divisible subgroup is the image of $H^1_f(\Q,V)$, so
$\operatorname{corank}H^1_f(\Q,W)=\dim H^1_f(\Q,V)$; in particular $H^1_f(\Q,W)$ is finite iff $H^1_f(\Q,V)=0$ (Rubin, Section 1.5, verify the
statement number; Flach92 for the adjoint). Paper: Theorem thm:main ("$\len_{\Zl}H^1_f(\Q,\ad T\otimes\Qlmod)$" is finite by 10.2 and (iii)).

**6.3 `def:blochkato:sigma-selmer`** (definition; P). For a finite set $\Sigma$ of primes not containing $\ell$:
$H^1_\Sigma(\Q,W)=\{c\in H^1(\Q,W):\operatorname{loc}_\ell c\in H^1_f(\Q_\ell,W),\ \operatorname{loc}_pc\in H^1_{\mathrm{ur}}(\Q_p,W)\text{ for }p\notin\Sigma\cup\{\ell\}\}$, no condition at $p\in\Sigma$ (none is
needed at $\infty$, $\ell$ odd). For $p\notin\Sigma\cup\{\ell\}$ with $W$ unramified at $p$, $H^1_{\mathrm{ur}}(\Q_p,W)=W/(\Frob_p-1)W$ is divisible and equals $H^1_f(\Q_p,W)$
(5.3(iv)); so $H^1_\Sigma(\Q,W)\supseteq H^1_f(\Q,W)$ is "Bloch-Kato outside $\Sigma$, nothing on $\Sigma$" as soon as $\Sigma$ contains the primes $p\ne\ell$ where $W$
ramifies. For the paper $\Sigma$ is the set of primes dividing $N$; it contains the $\mathrm I_0^*$ primes, where $A_f$ is unramified (3.2), which is
harmless. Reference: DFG04 Section 2.1 (verify the notation $H^1_\Sigma$). Paper: Section 4.2 ("with no condition at the primes of $\Sigma$, the
Bloch-Kato condition at $\ell$ and the unramified condition elsewhere").

**6.4 `prop:blochkato:sigma-finite`** (proposition; P). If $H^1_f(\Q,V)=0$ then $H^1_\Sigma(\Q,W)$ is finite: the kernel of
$H^1_\Sigma(\Q,W)\to\bigoplus_{p\in\Sigma}H^1(\Q_p,W)/H^1_f(\Q_p,W)$ is $H^1_f(\Q,W)$ (finite by 6.2(iii)), and each target is cofinitely generated with
$H^1(\Q_p,W)/H^1_f(\Q_p,W)\simeq H^1_f(\Q_p,T^D)^*$ finite (5.4, 3.4(iii), 5.3(v) for $T^D$). Paper: Theorem thm:dfg37 ("$H^1_\Sigma(\Q,W)$ is finite").

**6.5 `ex:blochkato:classical-selmer`** (example; S given Chapter 17's classical Selmer group, R for the comparison at $\ell$). For $T=T_\ell E$,
$W=E[\ell^\infty]$: $H^1_f(\Q,E[\ell^\infty])=\operatorname{Sel}_{\ell^\infty}(E/\Q)$. At $p\ne\ell$ both local conditions are $0$: $E(\Q_p)\otimes\Qlmod=0$, and
$H^1_f(\Q_p,V_\ell E)=0$ since $H^0(\Q_p,V_\ell E)=0$ (5.3(i); compare 5.5); at $\ell$ the Kummer image $E(\Q_\ell)\otimes\Qlmod$ is $H^1_f(\Q_\ell,W)$ (BlochKato
Example 3.11, verify). So the Bloch-Kato Selmer group is the model of Chapter 17 rewritten, and Tamagawa factors are invisible in the
Selmer group itself: they live in the comparison with relaxed conditions (Section 10). Paper: background (orientation for Section
1.2).

**6.6 `def:blochkato:adjoint-selmer`** (definition; P). The paper's objects: $W=\ad T\otimes\Qlmod$, $H^1_f(\Q,W)$ (6.1), $H^1_\Sigma(\Q,W)$ with $\Sigma$
the primes dividing $N$ (6.3), $W^D\simeq\ad T(1)\otimes\Qlmod$ (2.4), $H^1_f(\Q,V^D)$, $H^0(\Q,W^D)$. The Selmer group of Theorem thm:main is $H^1_f(\Q,W)$ with
discrete coefficients; the Selmer group of $A_f$ with $\Ql$ coefficients is $0$ under the hypothesis (10.2), so "the length of the
Bloch-Kato Selmer group of $\ad V_\ell E$" in the paper's abstract means $\len H^1_f(\Q,W)$ (Part 7, N3). Paper: abstract, Section 1.2, Theorem
thm:main, Section 4.2.

**6.7 `prop:blochkato:euler-characteristic`** (proposition; S given the Greenberg-Wiles formula with $\Ql$ coefficients, input K7). For
$V=A_f$ with $\ell\nmid N$: $\dim H^1_f(\Q,A_f)-\dim H^1_f(\Q,V^D)=\dim H^0(\Q,A_f)-\dim H^0(\Q,V^D)+\sum_{v}\bigl(\dim H^1_f(\Q_v,A_f)-\dim H^0(\Q_v,A_f)\bigr)=0$: the
terms at $p\ne\ell$ vanish by 5.3(i), the term at $\ell$ is $+1$ (4.5), the term at $\infty$ is $-\dim A_f^{c=1}=-1$ (complex conjugation acts on $A_f$
with eigenvalues $1,-1,-1$), and $H^0(\Q,A_f)=H^0(\Q,V^D)=0$ (2.6). Hence $H^1_f(\Q,A_f)=0$ iff $H^1_f(\Q,V^D)=0$. Reference: Wiles95 Proposition 1.6
for finite modules and FPR94 for the $\Ql$ version (verify both); Chapter 17. Paper: Theorem thm:dfg27 ("and the same for $A\otimes\Ql$"),
Remark rem:ns (the hypothesis $H^1_f(\Q,V^D)=0$ for the 3Ns curves).

### Section 7. Tamagawa factors (Fontaine and Perrin-Riou)

**7.1 `def:blochkato:tamagawa`** (definition; P for well-definedness). For a prime $p\ne\ell$ and a $G_{\Q_p}$-stable $\Zl$-lattice $M$ (free of
finite rank, continuous action):
$$\Tam_p(M)=\Fitt_{\Zl}\Bigl(\bigl(H^1(I_p,M)_{\mathrm{tor}}\bigr)^{G_{\Q_p}}\Bigr),$$
the Fitting ideal of the $G_{\Q_p}$-invariants (for the conjugation action of $G_{\Q_p}/I_p$, Chapter 16, conjugation-action) of the torsion
subgroup of $H^1(I_p,M)$; it is $\ell^{a}\Zl$ with $a$ the length of that finite module (Chapter 16, h1-finitely-generated; Chapter 3, 7.6), and
$v_\ell(\Tam_p(M)):=a$. The paper's display $\Fitt_{\Zl}(H^1(I_p,M)_{\mathrm{tor}})^{G_{\Q_p}}$ must be read this way (important_notes.md point 37). Reference: FPR94
I.4.2.2 (as cited by the paper); DFG04 p. 708. Paper: Section 1.2, Theorem thm:main, Lemma lem:tamfactor, Lemma lem:fpr.

**7.2 `prop:blochkato:tam-index`** (proposition; P from 5.3(iii)). For $p\ne\ell$ and $M$ a lattice:
$$\ell^{v_\ell(\Tam_p(M))}=\#\bigl(H^1(I_p,M)_{\mathrm{tor}}\bigr)^{G_{\Q_p}}=[H^1_f(\Q_p,M):H^1_{\mathrm{ur}}(\Q_p,M)].$$
This is the "index" description of the Tamagawa factor (PLAN.md): it measures how much bigger the Bloch-Kato condition for $M$ is than the
naive unramified one. Physics aside: an index of lattices as a volume ratio. Paper: Section 1.2, Lemma lem:fpr.

**7.3 `prop:blochkato:tam-basic`** (proposition; P). Let $p\ne\ell$. (i) If $M$ is unramified at $p$, $\Tam_p(M)=\Zl$ ($H^1(I_p,M)=\Hom(I_p,M)=M(-1)$ is
torsion-free). (ii) If $I_p$ acts on $M$ through a finite quotient of order prime to $\ell$, $\Tam_p(M)=\Zl$ (9.1 with $H^1(\Delta,M)=0$). (iii)
$\Tam_p(M)$ depends only on the $G_{\Q_p}$-module $M$; $\Tam_p(cM)=\Tam_p(M)$ for $c\in\Ql^\times$. (iv) $\Tam_p(\ad T)=\Tam_p(\ad(T\otimes\chi))$ for every character $\chi$ of
$G_{\Q_p}$ (2.4(ii)). In particular $\Tam_p(\ad T)=\Zl$ at every prime of good reduction and at every $\mathrm I_0^*$ prime ($\ad T$ unramified there).
Paper: Section 1.2 ("at a prime of good reduction it is $0$"), proof of Theorem thm:main ($\mathrm I_n^*$ primes).

**7.4 `thm:blochkato:fpr-local`** (theorem, the first identity of the paper's Lemma lem:fpr, in general for $p\ne\ell$; P given 5.3 and
3.1(c)). Let $p\ne\ell$ and $X$ a $G_{\Q_p}$-stable lattice with $H^0(\Q_p,X\otimes\Ql)=0$. Then $H^1_f(\Q_p,X)=H^1(\Q_p,X)_{\mathrm{tor}}$ is finite and there is an
exact sequence
$$0\to X^{I_p}/(\Frob_p-1)X^{I_p}\to H^1(\Q_p,X)_{\mathrm{tor}}\to\bigl(H^1(I_p,X)_{\mathrm{tor}}\bigr)^{G_{\Q_p}}\to0,$$
so $\Fitt_{\Zl}H^1_f(\Q_p,X)=\det(1-\Phi_p\mid X^{I_p})\cdot\Tam_p(X)$. (Cross-check: $H^1(\Q_p,X)_{\mathrm{tor}}\simeq H^0(\Q_p,X\otimes\Qlmod)$ by Chapter 17, 4.6, so
$\#H^0(\Q_p,W^D)=\ell^{v_\ell(L_p(A_f,1)^{-1})+v_\ell(\Tam_p(T^D))}$ for $X=T^D$.) For $X=T^D$ and $p\in\Sigma$ this is
$\Fitt H^1_f(\Q_p,T^D)=L_p(A_f,1)^{-1}\Tam_p(T^D)$ (3.3(i), 3.5). Proof: (1) inflation-restriction with $H^2(\widehat\Z,X^{I_p})=0$ (Chapter 16,
procyclic-compact (iii)) gives $0\to H^1(G/I,X^I)\to H^1(G,X)\to H^1(I,X)^{G/I}\to0$; (2) $H^1(G/I,X^I)=X^I/(\Frob-1)X^I$ is finite of order $\ell^{v_\ell\det(1-\Phi\mid X^I)}$
(3.1(c)); (3) taking torsion keeps exactness (a torsion class on the right lifts to a class some multiple of which lies in the finite left
term, hence to a torsion class); (4) Fitting ideals of finite $\Zl$-modules multiply in exact sequences (lengths add; Chapter 3, 7.5, 7.6);
(5) $H^1_f(\Q_p,X)=\iota^{-1}(0)=H^1(\Q_p,X)_{\mathrm{tor}}$ by 5.3(v). Reference: FPR94 I.4.2.2; the proof of DFG04 Theorem 2.15 (as cited by the paper).
Paper: Lemma lem:fpr, proof of Theorem thm:main ("each local term is $v_\ell(L_p(A_f,1)^{-1})+v_\ell(\Tam_p(A))$"), Remark rem:ns.

**7.5 `prop:blochkato:tam-dual`** (proposition, the second identity of Lemma lem:fpr; P for the elliptic-curve adjoint in every case,
R in general). For $p\ne\ell$, $\ell$ odd and $A=\ad T_\ell E$: $\Tam_p(T^D)=\Tam_p(A(1))=\Tam_p(A)$. Proof by cases: good, $\mathrm I_0^*$ and potentially good
primes: both sides trivial (7.3, 9.3; $I_p$ acts on $\Zl(1)$ trivially, so $H^1(I_p,A(1))=H^1(I_p,A)(1)$ and the finite-image argument is unchanged);
multiplicative and potentially multiplicative primes: $H^1(I,A(1))_{\mathrm{tor}}=H^1(I,A)_{\mathrm{tor}}(1)$, on which $\Frob$ acts as $q\cdot q^{-1}\Ad\rho(\Frob)=\Ad\rho(\Frob)$, and
the invariants are $\{x\bar e+y\bar h:(q-1)x\equiv2\varepsilon c'y\pmod{\ell^{v}}\}$, the kernel of a linear form on $(\Z/\ell^v)^2$ whose image has order
$\ell^{v-\min(v,v_\ell(q-1),v_\ell(c'))}$, so the order is $\ell^{v+\min(v,v_\ell(q-1),v_\ell(c'))}$, the same as for $A$ (8.2); in fact both invariant modules are
$\simeq\Z/\ell^v\oplus\Z/\ell^{m}$, $m=\min(v,v_\ell(q-1),v_\ell(c'))$ (Smith form of the linear form; Exercise 8). Reference: DFG04 (57) (as cited by the paper) for the general statement. Paper: Lemma lem:fpr
("$\Tam_p(T^D)=\Tam_p(A)$").

**7.6 `prop:blochkato:tam-of-E`** (proposition; P at multiplicative primes, R in general). For $p\ne\ell$, $v_\ell(\Tam_p(T_\ell E))=v_\ell(c_p(E))$, the $\ell$-part
of the Tamagawa number. At a multiplicative prime this is the check at the end of Lemma lem:tamfactor (8.2, Step 6: $v_\ell(n)$ if split,
$0$ if nonsplit, $\ell$ odd); at a type $\mathrm{IV}$ or $\mathrm{IV}^*$ prime with $\ell=3$, $H^1(I_p,T)_{\mathrm{tor}}=H^1(C_3,T)=T/\pi T\simeq\F_3$ (9.2), and its
$\Frob$-invariants are $\F_3$ or $0$ according as $c_p=3$ or $1$. General case: via $H^1_{\mathrm{ur}}(\Q_p,E[\ell^\infty])\simeq$ the dual of $\Phi_p(\F_p)[\ell^\infty]$ (Grothendieck,
SGA 7, Expose IX, verify; or Rubin, Section 1.6, verify). Paper: Lemma lem:tamfactor ("As a check ... the $\ell$-part of the Tamagawa
number $c_q(E)$, as it should").

### Section 8. The Tamagawa factor of $\ad T$ at a multiplicative prime: Lemma lem:tamfactor

**8.1 `conv:blochkato:tate-data`** (convention and recollection; P by citation). Convention C6, and the inputs: (a) the Tate shape:
a $\Zl$-basis $e_1,e_2$ of $T$ with $\rho(g)=\begin{psmallmatrix}\chi_\ell\varepsilon&\varepsilon\kappa\\0&\varepsilon\end{psmallmatrix}(g)$ on $G=G_{\Q_q}$, $\kappa$ a Kummer cocycle of $q_E$ in
$H^1(G,\Zl(1))=\varprojlim\Q_q^\times/(\Q_q^\times)^{\ell^k}$ (Chapter 11, 3.2; Chapter 10, 7.5(iii); point 42); (b) $\kappa|_{I}=n\,t_\ell$ (Chapter 7, 6.2(ii)), so a generator $t$
of the pro-$\ell$ tame quotient acts by $te_1=e_1$, $te_2=e_2+n'e_1$ with $v_\ell(n')=v_\ell(n)$; (c) $\Frob\,t\,\Frob^{-1}=t^q$ with $\Frob$ arithmetic (Chapter 7, 5.4;
point 11); (d) the decomposition $\kappa=n\kappa_q+\kappa_u$ for $q_E=q^nu$ (Chapter 7, 6.2(i)); (e) the class of $\kappa_u$ in $H^1(G/I,\Zl(1))=\Zl(1)/(q-1)\simeq\F_q^\times\otimes\Zl$
is the class of $\bar u$ (Chapter 7, 6.2(iii); Chapter 17, input K8). Paper: Lemma lem:tamfactor (statement and first sentences of the proof).

**8.2 `lem:blochkato:tamfactor`** (lemma, the paper's Lemma lem:tamfactor, in corrected form; P, every step). Let $q$ be a prime of
multiplicative reduction, $n=n_q=v_q(\Delta_E)$, $\ell$ an odd prime, $\ell\ne q$, $M=\ad T$, and $q_E$, $u$, $c(u)$ as in C6. Then
$H^1(I_q,M)_{\mathrm{tor}}\simeq(\Z/\ell^{v_\ell(n)})^2$ and
$$v_\ell\bigl(\Tam_q(\ad T)\bigr)=v_\ell(n)+\min\bigl(v_\ell(n),\,v_\ell(q-1),\,v_\ell(c(u))\bigr).$$
In particular $v_\ell(\Tam_q(\ad T))\ge t_\ell(E,q)$, with equality unless $q\equiv1\pmod\ell$, $\ell\mid n$ and $\bar u$ is an $\ell$-th power in $\F_q^\times$.
Proof, in six steps, each citing its source: **Step 1** (shape) 8.1(a), (b). **Step 2** (reduction to a procyclic group) the kernel of
$I\to\langle t\rangle$ has trivial pro-$\ell$ quotient, so $H^1(I,M')=M'/(t-1)M'$ for every $\Zl$-module $M'$ of finite type with this action (Chapter 16,
tame-inertia-example, procyclic-compact). **Step 3** (the computation) in the basis $e=e_1\otimes e_2^\vee$, $h=e_1\otimes e_1^\vee-e_2\otimes e_2^\vee$, $f=e_2\otimes e_1^\vee$:
$(t-1)e=0$, $(t-1)h=-2n'e$, $(t-1)f=n'h-n'^2e$; $2\in\Zl^\times$ gives $(t-1)M=n'(\Zl e\oplus\Zl h)$ and
$H^1(I,M)=(\Zl/n')\bar e\oplus(\Zl/n')\bar h\oplus\Zl\bar f$ (Chapter 16, model-computation (a)). **Step 4** (Frobenius) the conjugation action
$(\sigma\cdot c)(i)=\sigma c(\sigma^{-1}i\sigma)$ with $\Frob^{-1}t\Frob=t^{q^{-1}}$ and $c(t^a)\equiv a\,c(t)$ modulo $(t-1)M$ makes the **arithmetic** Frobenius act on
$M/(t-1)M$ as $q^{-1}\Ad\rho(\Frob)$; with $\rho(\Frob)=\begin{psmallmatrix}\varepsilon q&c'\\0&\varepsilon\end{psmallmatrix}$, $c'=\varepsilon\kappa(\Frob)$, one has $\Ad\rho(\Frob)e=qe$,
$\Ad\rho(\Frob)h=h-2\varepsilon c'e$, so on the torsion $\bar e\mapsto\bar e$, $\bar h\mapsto q^{-1}(\bar h-2\varepsilon c'\bar e)$ and the invariants are
$\{x\bar e+y\bar h:(q-1)y\equiv0,\ c'y\equiv0\pmod{\ell^{v_\ell(n)}}\}\simeq\Z/\ell^{v_\ell(n)}\oplus\Z/\ell^{\min(v_\ell(n),v_\ell(q-1),v_\ell(c'))}$ (Chapter 16, frobenius-on-h1-inertia,
model-computation (b), (c)). **Step 5** (the class $c'$; important_notes.md point 7 with its addendum; Chapter 17, 5.3, 5.4) $c'=\varepsilon\kappa(\Frob)$ is a cocycle
value: changing the lift by $t^a$ changes it by $\varepsilon qn'a$, changing $\kappa$ by a coboundary changes it by a multiple of $q-1$, so $c'$ is well
defined only modulo $(n,q-1)\Zl$ (not modulo $q-1$ as the paper says), which leaves $\min(v_\ell(n),v_\ell(q-1),v_\ell(c'))$ unchanged (Chapter 16,
model-computation (d)). The paper's phrase "the image of $\kappa$ in $H^1(G/I,\Zl(1)^I)$" is kept, with its precise meaning: $q$ is a canonical
uniformiser of $\Q_q$, so $H^1(\Q_q,\Zl(1))=\Zl\kappa_q\oplus H^1_{\mathrm{ur}}(\Q_q,\Zl(1))$ canonically, and the projection $\operatorname{pr}_{\mathrm{ur}}$ along $\kappa_q$ sends $[\kappa]$ to
$[\kappa_u]$, the class of $\bar u$ in $H^1(G/I,\Zl(1))=\Zl(1)/(q-1)\simeq\F_q^\times\otimes\Zl$ (Chapter 17, 5.3; it is a splitting, not a functorial map, since
inflation goes the other way). For the lift $\Frob_0$ fixing a compatible system of $\ell$-power roots of $q$ (Chapter 7, 5.5), $\kappa_q(\Frob_0)=0$ and
$c'=\varepsilon\,\kappa_u(\Frob_0)$, i.e. $\varepsilon$ times that image (Chapter 17, 5.4(iii)); so $v_\ell(c')=v_\ell(c(u))$ in the sense of C6 for $\Frob_0$, and the
minimum is the same for every lift (Chapter 17, 5.4(v)). Chapter 18 cites Chapter 17, 5.4 for this step and does not reprove it. **Step 6** (definition and check) by 7.1 the Fitting ideal of the invariants has valuation
$v_\ell(n)+\min(\dots)$; for $M=T$ the same steps give $H^1(I,T)_{\mathrm{tor}}=(\Z/\ell^{v_\ell(n)})\bar e_1$ with $\Frob$ acting by $\varepsilon$, invariants of length
$v_\ell(n)$ (split) or $0$ (nonsplit), the $\ell$-part of $c_q$ (7.6; data check in Part 6.6). Paper: Lemma lem:tamfactor (all of it), Section
1.2, Theorem thm:main ((eq:thm)), Remark rem:ko(1), Section sec:tam, important_notes.md points 7, 11, 23, 31, 42.

**8.3 `cor:blochkato:tamfactor-consequences`** (corollary; P). (i) $v_\ell(\Tam_q(\ad T))-t_\ell(E,q)=\min(v_\ell(n),v_\ell(q-1),v_\ell(c(u)))\in\{0,\dots,v_\ell(n)\}$. (ii) The
excess is positive iff $\ell\mid n$, $q\equiv1\pmod\ell$ and $\bar u\in(\F_q^\times)^\ell$; for $q=2$ it is $0$. (iii) (Remark rem:ko(1)) At such a prime,
$v_\ell(\Tam_q)\ge t_\ell(E,q)+1$, and (eq:identity) raises the bound of (eq:thm) by the excess, which can exceed $1$ only if $\ell^2\mid n$ and
$\ell^2\mid q-1$. (iv) The excess does not depend on whether the reduction is split. Paper: Remark rem:ko(1), Section sec:tam, the abstract
(Part 7, N2).

**8.4 `prop:blochkato:tam-potmult`** (proposition; P given Chapter 11, 3.4 and Chapter 10, 7.4(i)). Let $q\ne\ell$ ($q=2$ allowed) be a prime of
additive, potentially multiplicative reduction, $\nu=-v_q(j_E)$, $q_E=\mathsf q(j_E)$ and $u=q_Eq^{-\nu}$. Then
$v_\ell(\Tam_q(\ad T))=v_\ell(\nu)+\min(v_\ell(\nu),v_\ell(q-1),v_\ell(c(u)))\ge t_\ell(E,q)$. Proof: there is a ramified quadratic character $\chi$ of $G_{\Q_q}$ with $T\otimes\chi$
of the Tate shape for the Tate parameter $q_E$ (which depends only on $j$); $\ad T=\ad(T\otimes\chi)$ as $G_{\Q_q}$-modules (2.4(ii)); apply 8.2 to the
shape (8.2 uses only the shape, not a global curve). For $q$ odd one may use the global twist $E^{(q)}$ of Lemma lem:twist, as the paper
does; for $q=2$ the local argument is needed (important_notes.md point 18). At $q=2$, $v_\ell(q-1)=0$ and the value is $t_\ell(E,2)=v_\ell(-v_2(j))$, which
is not $v_\ell$ of the index of the Kodaira symbol (Chapter 10, 7.7). Paper: proof of Theorem thm:main ("at such a prime $p$ the curve $E_{\{p\}}$
... is multiplicative with the same Tate parameter valuation"), Definition def:terms ($t_\ell$ via $v_q(j)$).

**8.5 `ex:blochkato:tamfactor-examples`** (worked examples; P, every number computed; Part 6.6). Tate data and Tamagawa factors
($v=v_\ell(q-1)$, $k=v_\ell(c(u))$):

| curve, prime | type | $\nu$ | $\bar u\bmod q$ | $\ell$ | $v$ | $k$ | $v_\ell(\Tam_q(\ad T))$ | $t_\ell$ | remark |
|-|-|-|-|-|-|-|-|-|-|
| 11a1, $11$ | $\mathrm I_5$ | 5 | $10=-1$ | 5 | 1 | 1 | 2 | 1 | $E[5]$ reducible: the lemma, not the theorem (Chapter 16, Exercise 10) |
| 14a1, $7$ | $\mathrm I_3$ | 3 | $6=-1$ | 3 | 1 | 1 | 2 | 1 | $E[3]$ reducible (torsion $\Z/6$), $\deg\varphi_E=1$ |
| 539c1, $7$ | $\mathrm I_3^*$ | 3 | $5$ | 3 | 1 | 0 | 1 | 1 | 5 is not a cube mod 7; same $q_E$ as 77c1 |
| 791a1, $7$ | $\mathrm I_3$ | 3 | $6=-1$ | 3 | 1 | 1 | 2 | 1 | $\deg\varphi_E=144$, $v_3=2$: bound (eq:thm) $1$, refined bound $2$ |
| 791a1, $113$ | $\mathrm I_2$ | 2 | $106$ | 3 | 0 | 0 | 0 | 0 | $113\equiv2\pmod3$ |
| 1184f1, $37$ | $\mathrm I_3$ | 3 | $36=-1$ | 3 | 2 | 2 | 2 | 1 | the cap $v_\ell(\nu)=1$ binds |
| 1748e1, $19$ | $\mathrm I_6$ | 6 | $12$ | 3 | 2 | 1 | 2 | 1 | 12 a cube, not a ninth power, mod 19 |

(791a1 and 1184f1, 1748e1 have $E[3]$ irreducible, $3\nmid N$, non-CM, image not 3Ns.) Paper: Lemma lem:tamfactor, Remark rem:ko(1), Section
sec:tam.

### Section 9. Tamagawa factors at additive primes, and Open question 3

**9.1 `lem:blochkato:finite-inertia-image`** (lemma; P). Let $q\ne\ell$ and $M$ a lattice on which $I_q$ acts through a finite quotient $\Delta=I_q/K$.
Then $H^1(I_q,M)_{\mathrm{tor}}=H^1(\Delta,M)$ (inflated), and $H^1(I_q,M)/H^1(\Delta,M)$ embeds in $\Hom(K,M)^\Delta\subseteq\Hom(\Zl(1),M)=M(-1)$, which is torsion-free. Proof:
inflation-restriction (Chapter 16), $H^1(K,M)=\Hom_{\mathrm{cont}}(K,M)$ factors through the maximal pro-$\ell$ abelian quotient of $K$, which is $\Zl(1)$ ($K$ is
the inertia group of a finite extension of $\Q_q^{\mathrm{ur}}$, Chapter 7, 5.2); $H^1(\Delta,M)$ is finite (killed by $\#\Delta$). Paper: Open question 3.

**9.2 `prop:blochkato:ad-free-c3`** (proposition; P; verified by computer). Let $\sigma\in\GL_2(\Z_3)$ have order $3$ and $T=\Z_3^2$. Then $\ad T$ is a free
$\Z_3[\langle\sigma\rangle]$-module of rank one; hence $\hat H^i(\langle\sigma\rangle,\ad T)=0$ for all $i$, in particular $H^1(\langle\sigma\rangle,\ad T)=0$. By contrast
$H^1(\langle\sigma\rangle,T)=T/\pi T\simeq\F_3$. Proof: $\sigma$ has characteristic polynomial $X^2+X+1$, so $T$ is free of rank one over $\Z_3[X]/(X^2+X+1)\simeq\Z_3[\zeta_3]$ (a
DVR with uniformiser $\pi=1-\zeta_3$; Chapter 6, 4.7, 4.8; important_notes.md points 12, 13), and $\bar\sigma$ is a nontrivial unipotent on $T/3T$ (Lemma
lem:IV; Chapter 4, 9.4); $\ad(T/3)\simeq\Sym(T/3)\otimes\det^{-1}$ (Chapter 4) and $\Sym$ of a $2\times2$ Jordan block is a single $3\times3$ Jordan block in
characteristic $3$, i.e. the regular module $\F_3[C_3]=\F_3[X]/(X-1)^3$; by Nakayama a lift of a generator gives a surjection $\Z_3[C_3]\to\ad T$ of free
$\Z_3$-modules of rank $3$, hence an isomorphism. (Check: in the basis $e,h,f$ and $\sigma=\begin{psmallmatrix}0&-1\\1&-1\end{psmallmatrix}$, $e,\sigma e,\sigma^2e$ have
determinant $\pm1$.) For $T$: the norm $1+\sigma+\sigma^2$ is $0$ on $T$ and $(\sigma-1)T=\pi T$. Paper: Open question 3; Lemma lem:euler and Lemma lem:IV
(the same lattice).

**9.3 `thm:blochkato:tam-additive`** (theorem; P given 9.1, 9.2 and the classification of inertia images, R; new, see Part 7, N1). Let $\ell$ be
odd, $q\ne\ell$ a prime of additive reduction of $E$, $A=\ad T_\ell E$. (i) If the reduction at $q$ is potentially good, $\Tam_q(A)=\Tam_q(A(1))=\Zl$. (ii) If it
is potentially multiplicative, $\Tam_q(A)$ is given by 8.4. Proof of (i): the image $\Delta$ of $I_q$ is finite, of order dividing $24$: cyclic of order
$2,3,4,6$ for $q\ge5$ (Kraus90), and one of $C_2,C_3,C_4,C_6,Q_8,\SL_2(\F_3)$ at $q=2$, of order dividing $12$ at $q=3$ (Serre-Tate, Kraus90; cite by section,
verify); by 9.1, $H^1(I_q,A)_{\mathrm{tor}}=H^1(\Delta,A)$. If $\ell\nmid\#\Delta$ this is $0$ (Chapter 16, order-kills). If $\ell\mid\#\Delta$ then $\ell=3$ and $q\ne3$; the
$3$-primary part of $H^1(\Delta,A)$ injects into $H^1(P,A)$ for a Sylow $3$-subgroup $P$ (Chapter 16, res-inf-cor (d)), which is cyclic of order $3$
because $9\nmid24$, and $H^1(P,A)=0$ by 9.2 ($P\subset\GL_2(\Z_3)$ is generated by an element of order $3$). Twisting by $\Zl(1)$ changes nothing on $I_q$.
Consequences: $\Tam_q(\ad T)$ is trivial at every potentially good prime, of every Kodaira type, at every $q\ne\ell$ including $q=2$, even for
$\ell=3$ and types $\mathrm{II},\mathrm{II}^*,\mathrm{IV},\mathrm{IV}^*$, where $\Tam_q(T)$ can be $3$ (7.6). Paper: Open question 3 ("Compute the Tamagawa factors
of $\ad T$ at the additive primes"), proof of Theorem thm:main ("$v_\ell(\Tam_p(\ad T))\ge0$ at an additive prime": it is $0$ there unless the reduction is
potentially multiplicative), Section 1.2.

**9.4 `cor:blochkato:explicit-identity`** (corollary; P given 9.3, 8.2, 8.4, 7.3). For $\ell$ odd, $\ell\nmid N$:
$$\sum_{q\mid N}v_\ell(\Tam_q(\ad T))=\sum_{q:\,v_q(j_E)<0}\Bigl(t_\ell(E,q)+\min\bigl(t_\ell(E,q),\,v_\ell(q-1),\,v_\ell(c_q(u))\bigr)\Bigr).$$
Hence, under the hypothesis of Theorem thm:main, (eq:identity) reads
$$v_\ell(\deg\varphi_E)\ \ge\ \len H^1_f(\Q,W)+\sum_{q\mid N}e_\ell(E,q)+\sum_{q:\,v_q(j)<0}\bigl(t_\ell(E,q)+\min(t_\ell(E,q),v_\ell(q-1),v_\ell(c_q(u)))\bigr),$$
with equality by Chapter 14, 9.5 (important_notes.md points 39, 56; the DFG04 checklist there is settled, Chapter 20 outline, Part 7; important_notes.md point 73). So the excess of $v_\ell(\deg\varphi_E)$ over the
explicit local bound is the length of the adjoint Bloch-Kato Selmer group. Paper: Theorem thm:main, Remark rem:ko(1), Section sec:tam,
Open question 3.

**9.5 `rem:blochkato:open-question-3`** (remark; P for the data). What remains of Open question 3 is the Selmer length, which 9.4 computes
from $\deg\varphi_E$ (the DFG04 checklist being settled: Chapter 20 outline, Part 7; important_notes.md point 73). On the optimal non-CM curves of conductor below $10{,}000$ with $\ell\nmid N$, $E[\ell]$ irreducible and (for $\ell=3$) image
not 3Ns, the excess $v_\ell(\deg\varphi_E)-(\text{explicit bound})$ is $0,1,2,3,\ge4$ for $8688,3288,942,248,37$ of $13{,}203$ curves at $\ell=3$; $19019,3993,328,19,2$ of
$23{,}361$ at $\ell=5$; $25133,2888,111,2,0$ of $28{,}134$ at $\ell=7$, and is never negative. Reading: $H^1_f(\Q,W)=0$ for about two
thirds of the curves at $\ell=3$ and $81\%$, $89\%$ at $\ell=5,7$. The Tamagawa factor at $q=\ell$ is not defined by 7.1 (it needs $p$-adic Hodge
theory) and belongs to Open question 1 (Chapter 20). Paper: Open questions 1 and 3, Section sec:sharp (the mean excess).

### Section 10. The comparison of Selmer groups (DFG04 Lemma 2.1) and $H^0(\Q,W^D)$

**10.1 `def:blochkato:exceptional-set`** (definition and proposition; P given Chapter 11, 8.6). DFG04's exceptional set, for $f=f_E$ (weight
$2$, trivial character, rational coefficients): $S_f=\{\ell:\ \ell\mid2N,\text{ or }\bar\rho|_{\Gal(\Qbar/\Q(\sqrt{\ell^*}))}\text{ is not absolutely irreducible}\}$ (DFG04 (31), as the paper
reads it for $k=2$; see 4.4 and Part 7, Q1). For $\ell\nmid2N$ the following are equivalent: $\ell\notin S_f$; $E[\ell]$ is irreducible and $h_\ell(E)=0$; $E[\ell]$ is
irreducible and not ($\ell=3$ and image 3Ns) (important_notes.md point 47). Paper: Section 4.2 ("the hypothesis of Theorem thm:main is
$\ell\notin S_f$"), Theorem thm:main, Remark rem:ns.

**10.2 `thm:blochkato:dfg27`** (theorem, the paper's Theorem thm:dfg27 = DFG04 Theorem 2.7; R, with a sketch). If $\ell\notin S_f$ then
$H^0(\Q,V^D)=H^1_f(\Q,V^D)=0$, and $H^0(\Q,A_f)=H^1_f(\Q,A_f)=0$. The $H^0$ statements hold for every $E$ with $\bar\rho$ absolutely irreducible (2.6); the content is
the vanishing of the adjoint Selmer group with $\Ql$ coefficients, which comes from the Taylor-Wiles method ($R_\emptyset\otimes\Ql=\T_\emptyset\otimes\Ql$, so the
tangent space of the deformation ring, $H^1_f(\Q,A_f)$, vanishes; DFG04 Section 2.3, verify), and the two Selmer statements are equivalent by 6.7.
Consequence: $H^1_f(\Q,W)$ is finite (6.2(iii)) and $H^1_\Sigma(\Q,W)$ is finite (6.4). Reference: DFG04 Theorem 2.7 (as cited); Flach92 for the finiteness
of the integral Selmer group of $\Sym T_\ell E$ under his hypotheses (14.6). Paper: Theorem thm:dfg27, proof of Theorem thm:main.

**10.3 `prop:blochkato:h0-selmer`** (proposition, Lemma lem:h0 in Selmer language; P given Chapter 11, 8.5 for (ii)). Let $\ell$ be odd with $\bar\rho$
absolutely irreducible (for $\bar\rho_{E,\ell}$, equivalently irreducible: Chapter 11, 1.4). (i) If $H^0(\Q,V^D)=H^1_f(\Q,V^D)=0$ then
$H^1_f(\Q,T^D)=H^1(\Q,T^D)_{\mathrm{tor}}$, and the connecting map gives $H^0(\Q,W^D)\xrightarrow{\ \sim\ }H^1_f(\Q,T^D)$ (6.2(i) for $T^D$; torsion classes satisfy every local
condition by 5.2(a)). (ii) (the paper's Lemma lem:h0, corrected; Chapter 11, 8.5, important_notes.md points 5, 6, 10, 14) $H^0(\Q,W^D)\simeq\Z/\ell^{h_\ell(E)}$ is
finite and cyclic, $h_\ell(E)$ is the largest $k$ with $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$, $h_\ell(E)=0$ for every $\ell\ge5$, and $h_3(E)\le1$ with equality iff
$\bar\rho_{E,3}\simeq\bar\rho_{E,3}\otimes\chi_{-3}$ iff the image of $\bar\rho_{E,3}$ is $N_s(\F_3)$; this holds for every $E$, with or without CM and whether or not $\ell\mid N$. The
criterion is $\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$, not $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ (point 6); the proof is the determinant argument
$\chi_\ell^2\equiv1\pmod{\ell^k}$ on $G_\Q$, which forces $\ell^k=3$, and not the paper's appeal to CM, which confuses $\chi_\ell$ with $\chi_{\ell^*}$ (point 5).
Paper: Lemma lem:h0, Conjecture conj:euler ($h_\ell(E)$), Section 1.3, proof of Theorem thm:main ("$H^0(\Q,W^D)=0$ by Lemma lem:h0"), Remark
rem:ns.

**10.4 `lem:blochkato:dfg21`** (lemma, the paper's Lemma lem:dfg21 = DFG04 Lemma 2.1; P given Chapter 17, 10.3, the abstract form). Suppose
$H^0(\Q,V^D)=H^1_f(\Q,V^D)=0$, and let $\Sigma$ be a nonempty finite set of primes, $\ell\notin\Sigma$, containing every prime $p\ne\ell$ at which $W$ is ramified. Then
there is an exact sequence
$$0\to H^1_f(\Q,W)\to H^1_\Sigma(\Q,W)\to\bigoplus_{p\in\Sigma\cup\{\infty\}}H^1_f(\Q_p,T^D)^*\to H^0(\Q,W^D)^*\to0,$$
in which the term at $\infty$ is $0$ for $\ell$ odd and, for $p\in\Sigma$, $H^1_f(\Q_p,T^D)=H^1(\Q_p,T^D)_{\mathrm{tor}}\simeq H^0(\Q_p,W^D)$ is finite (5.3(v); Chapter 17,
4.6). Proof: apply Chapter 17, 10.3 to the Bloch-Kato conditions $L_{V,v}=H^1_f(\Q_v,V)$. Its hypotheses: $L_{V,v}=H^1_{\mathrm{ur}}$ outside $S$ (5.1(i)); $L_{V,v}^\perp=L_{V^D,v}$
for all $v$ (5.4: Chapter 17, 4.4(ii) at $p\ne\ell$, BlochKato at $\ell$); (a) $H^1_f(\Q,V^D)=0$ (here a hypothesis; for $\ell\notin S_f$ it is thm:dfg27, 10.2); (b)
$H^0(\Q_p,V^D)=0$ for some $p\in\Sigma$, which holds for every $p\ne\ell$ (3.3(i)) as soon as $\Sigma\ne\emptyset$. Chapter 17's propagated conditions are Chapter 18's
$H^1_f$ on $T$, $W$ (5.2; Chapter 17, 4.5), and its relaxed structure $\mathcal L^\Sigma$ is DFG04's $H^1_\Sigma$ (6.3). What each hypothesis does (to be said in
the text): $H^1_f(\Q,V^D)=0$ makes $H^1_f(\Q,T^D)$ torsion, $\simeq H^0(\Q,W^D)$ (10.3(i)); $\Sigma\ne\emptyset$ with $H^0(\Q_p,V^D)=0$ kills the strict dual Selmer group and
gives the surjection onto $H^0(\Q,W^D)^*$; $\ell$ odd kills $\infty$. The paper's hypothesis $H^0(\Q,V^D)=0$ is implied by (b). Reference: DFG04 Lemma 2.1 (as
cited); Rubin, Theorem 1.7.3 (verify). Paper: Lemma lem:dfg21 and the paragraph after it, proof of Theorem thm:main, Remark rem:ns.

**10.5 `cor:blochkato:length-identity`** (corollary; P given 10.4, 7.4, 7.5, 6.2, 6.4). Under the hypotheses of 10.4 and $H^1_f(\Q,A_f)=0$ (automatic by
6.7), all terms are finite and
$$\len H^1_\Sigma(\Q,W)=\len H^1_f(\Q,W)+\sum_{p\in\Sigma}\Bigl(v_\ell\bigl(L_p(A_f,1)^{-1}\bigr)+v_\ell\bigl(\Tam_p(\ad T)\bigr)\Bigr)-h_\ell(E).$$
Proof: lengths in a four-term exact sequence of finite modules (Chapter 16, lengths-in-exact-sequences), Pontryagin duality preserves
length, $\len H^1_f(\Q_p,T^D)=v_\ell(L_p(A_f,1)^{-1})+v_\ell(\Tam_p(T^D))$ (7.4) and $\Tam_p(T^D)=\Tam_p(\ad T)$ (7.5), $\len H^0(\Q,W^D)=h_\ell(E)$ (10.3). Paper: proof of
Theorem thm:main (the display "$\len H^1_\Sigma=\len H^1_f+\sum\len H^1_f(\Q_p,T^D)$"), Remark rem:ns (the display with $-h_\ell(E)$), Conjecture conj:euler.

### Section 11. The Selmer half of the proof of Theorem thm:main

**11.1 `thm:blochkato:selmer-identity`** (theorem; P given 10.2 (R), 10.5, 9.4). Let $E$ be an elliptic curve over $\Q$, $\ell\notin S_f$, $\Sigma$ the set of
primes dividing $N$ (nonempty: $N>1$). Then $H^1_f(\Q,W)$ and $H^1_\Sigma(\Q,W)$ are finite and
$$\len H^1_\Sigma(\Q,W)=\len H^1_f(\Q,W)+\sum_{q\mid N}v_\ell\bigl(L_q(A_f,1)^{-1}\bigr)+\sum_{q:\,v_q(j)<0}\Bigl(t_\ell(E,q)+\min\bigl(t_\ell(E,q),v_\ell(q-1),v_\ell(c_q(u))\bigr)\Bigr).$$
($h_\ell(E)=0$ by 10.1; Tamagawa terms by 9.4.) Optimality of $E$ is not used here. Paper: proof of Theorem thm:main (from "By Theorem
thm:dfg27 the hypotheses of Lemma lem:dfg21 hold" to "each local term is ..."), Theorem thm:main.

**11.2 `rem:blochkato:assembly`** (remark; forward pointer, nothing proved). The assembly lives in Chapter 20: $v_\ell(\deg\varphi_E)=v_\lambda(\eta^\emptyset_{f,\lambda})$
(Chapter 14, 9.5: an equality for the optimal curve, important_notes.md points 39, 56; the DFG04 checklist of Chapter 14, 9.6 is settled, Chapter 20 outline, Part 7; important_notes.md point 73),
$v_\lambda(\eta^\Sigma)=v_\lambda(\eta^\emptyset)+\sum_{p\in\Sigma}v_\ell(L_p^{\nv}(A_f,1)^{-1})$ (thm:dfg14, Chapter 20), $v_\lambda(\eta^\Sigma)=\len H^1_\Sigma(\Q,W)$ (thm:dfg37, Chapter 20), and 11.1. The naive factor
equals the true one at multiplicative primes ($\delta_p=1$) and is $1$ at additive ones ($\delta_p=0$), so the Euler terms that survive are
$\sum_qe_\ell(E,q)$ (Definition def:terms). Result: (eq:identity) **with equality** for $\ell\notin S_f$ (no freeness hypothesis; Chapter 14, 9.5), and (eq:thm) from
$\len H^1_f\ge0$ and 8.3, 8.4 (including $\mathrm I_n^*$ primes at $q=2$, point 18). The chapter gives this as a one-paragraph `remark` and a
`paperlink`; it must not reprove Chapter 20's steps. Paper: Theorem thm:main and its proof.

**11.3 `ex:blochkato:selmer-examples`** (worked examples; P computed; the DFG04 checklist they depended on is settled, Chapter 20 outline, Part 7; important_notes.md point 73). At $\ell=3$: 121a1 (type $\mathrm{II}$
at $11$, $e_3=v_3(12)=1$, no potentially multiplicative prime, $\deg\varphi_E=6$): excess $0$, so $H^1_f(\Q,\ad T_3\otimes\Q_3/\Z_3)=0$. 791a1 (8.5): bound (eq:thm) $1$,
explicit bound $2$, $v_3(144)=2$: excess $0$, the Tamagawa excess is needed for equality. 1184f1: explicit bound $2$, $v_3(1728)=3$: Selmer length $1$.
1748e1: explicit bound $3$, $v_3(3240)=4$: Selmer length $1$. (Each curve: $3\nmid N$, $E[3]$ irreducible, image not 3Ns, non-CM.) Paper: Theorem
thm:main, Section sec:sharp ("the identity (eq:identity) says what the excess is").

### Section 12. Beyond the hypothesis: Remark rem:ns, $h_\ell(E)$, Open question 2

**12.1 `rem:blochkato:rem-ns`** (remark with proof of the conditional statement; P given 10.4, 10.5). Let $\ell=3$ and the image of $\bar\rho_{E,3}$ be
$N_s(\F_3)$, $3\nmid N$. Then $H^0(\Q,V^D)=0$ (2.6), $\Sigma\ne\emptyset$, $h_3(E)=1$ (10.3), and **if** $H^1_f(\Q,V^D)=0$ (equivalently $H^1_f(\Q,A_f)=0$, 6.7), 10.5 gives Remark
rem:ns's identity $\len H^1_\Sigma=\len H^1_f+\sum_p(v_\ell(L_p^{-1})+v_\ell(\Tam_p))-h_3(E)$. DFG04 Theorem 2.7 does not supply the vanishing of $H^1_f(\Q,V^D)$ here
($3\in S_f$); the book states it as a hypothesis, as the paper's "whenever" does, and records that it is predicted by the Bloch-Kato
conjecture (14.2) and that later modularity-lifting results may prove it (the writer cites one only after checking it; Part 7, N4).
Paper: Remark rem:ns, Section sec:anomaly, Conjecture conj:euler.

**12.2 `rem:blochkato:conj-euler-h`** (remark; P). In Conjecture conj:euler the correction $h_\ell(E)$ is $0$ for $\ell\ge5$ and is $1$ exactly for the curves
with mod-$3$ image $N_s(\F_3)$ (10.3; any $N$); it is the term $H^0(\Q,W^D)^*$ of Lemma lem:dfg21; the appendix's `ns3(E)` (two quadratic factors of the
$3$-division polynomial) computes it (Proposition prop:ns; Chapter 11, 8.3). Worked example: 726a1 at $\ell=3$ (outside Theorem thm:main as $3\mid726$):
type $\mathrm{III}$ at $11$ with $e_3=v_3(12)=1$, image 3Ns, `rule(E,3)` and `rule(E,3,1)` both return $[2,2]$ (recomputed). Paper: Conjecture conj:euler,
Section 1.3, Section sec:anomaly, the appendix.

**12.3 `rem:blochkato:open-question-2`** (remark; nothing proved). Open question 2 asks for $v_\lambda(\eta^\Sigma_{f,\lambda})=\len H^1_\Sigma(\Q,W)$ when the image is $N_s(\F_3)$.
On the Selmer side, 12.1 shows what the identity would give and which input is missing ($H^1_f(\Q,A_f)=0$); on the congruence side the missing
input is Taylor-Wiles for a residual representation induced from $\Q(\sqrt{-3})$ (Chapter 20). The data of Section sec:anomaly (failures by exactly $1$,
never more) are consistent with the identity with $-h_3(E)$. Paper: Open question 2, Remark rem:ns.

### Section 13. Section sec:tam: testing the Tamagawa factors on the tables

**13.1 `ex:blochkato:sec-tam`** (worked example with data; P for the recomputation). The paper's test: for curves satisfying the hypothesis
of Theorem thm:main with a multiplicative prime $q\equiv1\pmod\ell$, $\ell\mid n_q$, compare $v_\ell(\deg\varphi_E)$ with the bound raised by the Tamagawa excess (8.3). The
paper reports, on the working set, no exception, and equality rising from $45.0\%$ to $60.6\%$ ($\ell=3$, $46{,}222$ curves) and from $67.0\%$ to $78.7\%$ ($\ell=5$,
$10{,}940$ curves). Recomputation for conductors below $10{,}000$ (optimal non-CM curves, $\ell\nmid N$, $E[\ell]$ irreducible, image not 3Ns, with the
Tamagawa terms of 9.4 at all potentially multiplicative primes): at $\ell=3$, $1{,}050$ curves have a potentially multiplicative prime $q\equiv1\pmod3$ with
$3\mid\nu_q$; equality rises from $596$ ($56.8\%$) to $714$ ($68.0\%$); $186$ curves have a positive excess; at $\ell=5$, $252$ curves, $203\to220$; at $\ell=7$,
$18$ curves, $17\to18$; no violation of the refined inequality at $\ell=3,5,7$ among $13{,}203$, $23{,}361$ and $28{,}134$ curves. The rates are not comparable
with the paper's (smaller conductors, and $\mathrm I_n^*$ primes included here). Paper: Section sec:tam.

**13.2 `rem:blochkato:what-sec-tam-tests`** (remark; P). Given 11.1, 11.2 and the equality of Chapter 14, 9.5, a violation of the refined inequality
is impossible, and the proportion of equality is the proportion of curves with $H^1_f(\Q,W)=0$ (9.5). So Section sec:tam tests the Tamagawa
term of the identity, as the paper says, but its phrase "the extra divisibility of the modular degree is exactly where the Tamagawa
factor of the adjoint exceeds $\ell^{t_\ell}$" means only that the excess is accounted for in those cases; extra divisibility also arises from the
Selmer group. Paper: Section sec:tam.

### Section 14. The Tamagawa number conjecture and the adjoint motive

**14.1 `def:blochkato:adjoint-motive`** (definition and proposition; S). The adjoint motive $\ad^0M_f$ of a weight-$2$ newform: its $\ell$-adic
realisations $A_f$ (with $A_f\simeq\Sym V\otimes\det^{-1}$, Chapter 4), Betti and de Rham realisations; pure of weight $0$ with Hodge numbers
$h^{1,-1}=h^{0,0}=h^{-1,1}=1$; $L(\ad f,s)=\prod_pL_p(A_f,s)$ (true Euler factors; at $p=\ell$ via $D_{\mathrm{cris}}$, independent of $\ell$), and
$L(\ad f,s)=L(\Sym f,s+1)$ in the paper's normalisation $L_p(\Sym f,s)=L_p(A_f,s-1)$ (Chapter 19). The point $s=1$ is critical (Deligne79; DFG04
Section 1, verify), $L(\ad f,1)\ne0$ (Shimura76; GelbartJacquet), and it is the value related to $\langle f,f\rangle$ (Chapter 19). Reference: DFG04
Section 1; Deligne79; Flach92. Paper: Section 1 ("the Selmer group of $\Sym f$", "Rankin, Shimura"), Section 1.1.

**14.2 `conj:blochkato:tnc`** (conjecture; R). The Tamagawa number conjecture of Bloch and Kato, in the shape used here (the form of
FPR94, verify): for a motive $M$ over $\Q$ with $L(M,0)$ critical and nonzero, a prime $\ell$, a lattice $T$ in the $\ell$-adic realisation, $W=T\otimes\Qlmod$ and
$W^D=T^D\otimes\Qlmod$,
$$\frac{L(M,0)}{\Omega(M)}\ \sim_\ell\ \frac{\prod_{p\ne\ell}\#\bigl(\Zl/\Tam_p(T)\bigr)\cdot\#H^1_f(\Q,W^D)}{\#H^0(\Q,W)\cdot\#H^0(\Q,W^D)},$$
where $\sim_\ell$ means equality up to an $\ell$-adic unit and the contributions at $\ell$ and $\infty$ are absorbed in the choice of the period $\Omega(M)$ (Bloch-Kato's
Tamagawa measure). For $M=A_f(1)$ ($L(M,0)=L(\ad f,1)$, $T=T^D$, so the roles of $W$ and $W^D$ swap) the right side is
$\prod\Tam_p(T^D)\cdot\#H^1_f(\Q,W)/(\#H^0(\Q,W^D)\#H^0(\Q,W))$: the adjoint Selmer group of Theorem thm:main, the Tamagawa factors of Lemma lem:fpr, and
$h_\ell(E)$ in the denominator, the same sign as in Remark rem:ns. The book never uses the conjecture in a proof and says which
normalisations differ between BlochKato Section 5, FPR94 and DFG04 Section 2 (verify each). Paper: Section 1 ("expresses them through the
adjoint Selmer group and the adjoint $L$-value"), Theorem thm:main (context), Remark rem:ns.

**14.3 `ex:blochkato:bsd`** (example; R). For $M=h^1(E)(1)$ the conjecture is the Birch and Swinnerton-Dyer formula: $L(E,1)/\Omega_E$ against
$\#\text{Sha}\cdot\prod_pc_p/\#E(\Q)_{\mathrm{tors}}^2$ (rank $0$); the local terms $\Tam_p(T_\ell E)$ are the $\ell$-parts of the $c_p$ (7.6), the Selmer term is $\#\text{Sha}[\ell^\infty]$ (6.5),
and the $H^0$ terms are the torsion. Orientation only. Reference: BlochKato Section 6 (verify); Chapter 9. Paper: background.

**14.4 `thm:blochkato:dfg-01`** (theorem, DFG04 Theorem 0.1; R). For a newform $f$ of weight $k\ge2$ and $\lambda\notin S_f$, the $\lambda$-part of the
Bloch-Kato conjecture holds for $L(\ad^0M_f,1)$ (and $L(\ad^0M_f,0)$). For $f=f_E$ the identity reads, up to the exact normalisation of the
period in DFG04 Section 1.7 (verify): $v_\ell$ of the period-normalised $L(\ad f,1)$ (equivalently, by Hida's theorem and the Rankin-Shimura
method, of the congruence ideal $\eta^\emptyset_{f,\lambda}$ up to the factors at $\Sigma$) equals $\len H^1_f(\Q,W)+\sum_{p\mid N}v_\ell(\Tam_p(A))$ plus the Euler-factor
terms. The book quotes the statement with the reference and explains that (eq:identity) is its reading through the modular degree
(14.7). Reference: DFG04 Theorem 0.1 (as cited by the paper). Paper: Theorem thm:main ("the hypothesis is the one under which
Diamond, Flach and Guo prove the Tamagawa number conjecture for the adjoint motive").

**14.5 `thm:blochkato:dfg-02`** (theorem, DFG04 Theorem 0.2 = Theorem 3.7 in the paper's reading; R; home: Chapter 20). If $\lambda\notin S_f$ and $\Sigma$ is a
finite set of primes, $\ell\notin\Sigma$, outside which $M_{f,\lambda}$ is minimally ramified, then $H^1_\Sigma(\Q,W)$ is finite of length $v_\lambda(\eta^\Sigma_{f,\lambda})$. Stated here
only so that 11.1 can be read against it; the statement, the meaning of "minimally ramified" and the Taylor-Wiles sketch are Chapter
20's (thm:dfg37). Paper: Theorem thm:dfg37.

**14.6 `thm:blochkato:flach`** (theorem; R). (Flach 1992.) For $E/\Q$ modular and $\ell$ a prime outside an explicit finite set (including the primes
of bad reduction and $2$, $3$ in the original statement; verify the exact hypotheses), the Bloch-Kato Selmer group of $\Sym T_\ell E\otimes\Qlmod$ is finite,
and is annihilated by an explicit integer related to $\deg\varphi_E$ (verify). The first place where the modular degree meets the
symmetric-square Selmer group. Reference: Flach92. Paper: Section 1 ("Flach's finiteness theorem for the symmetric square ... is the first
place where the modular degree meets the Selmer group of $\Sym f$").

**14.7 `rem:blochkato:degree-as-l-value`** (remark; heuristic, clearly labelled). The chain: $\deg\varphi_E\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c_E^2\langle f,f\rangle$ (Chapter 14,
7.3); $\langle f,f\rangle$ is $L(\Sym f,2)=L(\ad f,1)$ times explicit factors and local factors at the bad primes (Chapter 19); 14.4 expresses $L(\ad f,1)$ over a period
by Selmer and Tamagawa terms; the ratio of naive to true local factors produces $\sum e_\ell(E,q)$. Theorem thm:main is the theorem behind this
heuristic, proved through congruence ideals instead of $L$-values. One paragraph; details Chapters 19 and 20. Paper: Section 1 (the
classical route via the Petersson norm), Theorem thm:main.

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3 allows up to 2,800 for this chapter). The card lists the 65 items
of Part 2 (numbered 18.1 to 18.65 in the book; conventions C1 to C8 in one line each), about 210 lines, not counted. Total of the
targets: **2,630**.

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2 with its tag and `\Cref`; the formulas of 7.1, 7.4, 8.2, 9.4, 10.4, 10.5, 11.1 displayed | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1.2 ($\Tam_p$, $H^1_f$); Theorem thm:main and its proof (thm:dfg27, lem:dfg21 and the paragraph after it, lem:fpr, lem:h0, the length bookkeeping, the $\mathrm I_n^*$ step); Lemma lem:tamfactor; Remark rem:ko(1); Remark rem:ns; Section sec:tam; Open questions 2, 3; Conjecture conj:euler ($h_\ell$); the abstract's sentences on the Selmer group and the Tamagawa formula | 45 |
| 1 | Overview and conventions | the opening paragraph (Part 1.1, seven uses); C1 to C8 as `convention` environments; 1.1 with the roadmap table "paper sentence $\to$ item"; a `warning` box on the three duals (C2) and one on the two Frobenii (C3) | 80 |
| 2 | $\ell$-adic representations, lattices, twists and duals | 2.1 to 2.6; the $3\times3$ trace-form Gram matrix displayed; `paperlink`: Section 4.2 (trace form, $T^D\simeq A(1)$; homothety of $M_{f,\lambda}$, points 26, 40) | 190 |
| 3 | Local behaviour at $p\ne\ell$ | 3.1 to 3.5; the table of 3.2 (cited from Chapters 7, 11, 19); `paperlink`: the paragraph after Lemma lem:dfg21 (geometric Frobenius, point 11); a `warning` that $H^0(\Q_p,A_f)\ne0$ at some bad primes (3.3) | 170 |
| 4 | The representation at $\ell$: $p$-adic Hodge theory as a black box | 4.1 to 4.5, all R, one paragraph each; the dimension check $1+2=3$; the writer's check on Fontaine-Laffaille at $\ell=3$ (Part 7, Q1) as a footnote-sized remark, not as a claim | 140 |
| 5 | Bloch-Kato local conditions | 5.1 to 5.5; the three exact sequences of 5.3 displayed; the worked example 5.5 in full ($E[\ell^\infty]$ at a split multiplicative prime) | 240 |
| 6 | Global Selmer groups and $H^1_\Sigma$ | 6.1 to 6.7; the classical Selmer group as 6.5; the Euler-characteristic count of 6.7 as a four-row table ($p\ne\ell$, $\ell$, $\infty$, $H^0$) | 190 |
| 7 | Tamagawa factors | 7.1 to 7.6; the definition with the parenthesis placed (point 37) and a `paperlink` quoting the paper's display; 7.4 proved in five numbered steps; 7.5 by cases | 230 |
| 8 | Lemma lem:tamfactor | 8.1 to 8.5; the proof in six numbered steps, each with its source chapter in the margin of the text; the matrices displayed; a `paperlink` per corrected sentence (points 7, 11, 23, 31, 42, 18); the table of 8.5 | 280 |
| 9 | Additive primes and Open question 3 | 9.1 to 9.5; the Jordan-block computation of 9.2 displayed; the explicit identity 9.4 displayed; the excess distribution table of 9.5 | 160 |
| 10 | DFG04 Lemma 2.1 and $H^0(\Q,W^D)$ | 10.1 to 10.5; the five-term comparison sequence and its specialisation, with a "where each hypothesis enters" list; the length identity | 240 |
| 11 | The Selmer half of Theorem thm:main | 11.1 to 11.3; the assembly paragraph 11.2 with forward `\Cref`s only; the four worked curves | 130 |
| 12 | Beyond the hypothesis | 12.1 to 12.3; 726a1 | 100 |
| 13 | Section sec:tam | 13.1, 13.2; the comparison table (paper versus recomputation) | 80 |
| 14 | The Tamagawa number conjecture and the adjoint motive | 14.1 to 14.7; the BSD dictionary as a two-column table; the heuristic 14.7 in a clearly labelled `remark` | 170 |
| 15 | Exercises | the 16 exercises of Part 4.2 | 140 |
| 16 | Notes and references | BlochKato, FPR94, Fontaine, Berger, Rubin, NSW, DFG04, Flach92, Wiles95, TateDuality, MilneADT, Greenberg89; which theorem numbers were cited and which are marked (verify); the history (Bloch-Kato 1990, Fontaine-Perrin-Riou 1994, Flach 1992, DFG 2004) in one paragraph | 45 |

________________________________________________________________________________

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| $\ell$-adic representations of $G_\Q$, lattices $T$, $W=V/T$ | 2.1 |
| Tate twists $V(n)$ | 2.2 |
| duals $V^*$ (here $V^\vee$), $V^D=V^*(1)$, $T^D$, $W^D$ | 2.3 (C2) |
| trace form on $\ad V$, self-duality, $A(1)=T^D$ for $\ell$ odd | 2.4 |
| geometric representations; local behaviour at $p\ne\ell$, Weil-Deligne, inertia invariants, $L_p(V,s)$ | 2.5, 3.1, 3.2 (Weil-Deligne by citation of Chapter 7) |
| Frobenius convention; good prime eigenvalues $\alpha/\beta,1,\beta/\alpha$; $L_p(A_f,1)$ at a good prime | 3.1, 3.2, C3 |
| de Rham, crystalline, semistable; $B_{\mathrm{dR}}$, $B_{\mathrm{cris}}$, $B_{\mathrm{st}}$; $D_{\mathrm{cris}}$; $T_\ell E$ crystalline; adjoint crystalline | 4.1, 4.2, 4.3 (and 4.4, 4.5) |
| Bloch-Kato local conditions at $p\ne\ell$, $\ell$, $\infty$; $H^1_g$, $H^1_e$ | 5.1 |
| conditions on $T$ and $W$ | 5.2, 5.3, 5.5 |
| global $H^1_f(\Q,V)$, $H^1_f(\Q,T)$, $H^1_f(\Q,W)$ and their relations | 6.1, 6.2 |
| the $\Sigma$-imprimitive Selmer group of DFG04 Section 2.1 | 6.3, 6.4, 6.6 |
| duality of the Bloch-Kato conditions for $V$ and $V^D$ | 5.4 |
| FPR Tamagawa factor $\Tam_p(T)$ (definition as in the paper; FPR94 I.4.2.2; DFG04 p. 708) | 7.1 |
| the index description and Lemma lem:fpr; $\Tam_p(T^D)=\Tam_p(T)$ | 7.2, 7.4, 7.5 |
| the Tamagawa factor of an elliptic curve is the $\ell$-part of $c_p$ | 7.6, 8.2 (Step 6) |
| the full computation of Lemma lem:tamfactor; $v_\ell(\Tam)\ge t_\ell$ with the equality criterion | 8.1 to 8.5 |
| the Tamagawa factor at an additive prime (Open question 3) | 9.1 to 9.5, 8.4 |
| the Tamagawa factor at a good prime is trivial | 7.3 |
| the Tamagawa number conjecture; the shape for the adjoint; DFG04 Theorems 0.1, 0.2 with $\ell\notin S_f$ | 14.2, 14.4, 14.5, 10.1 |
| the exact sequence of DFG04 Lemma 2.1 (lem:dfg21) | 10.4 |
| DFG04 Theorem 2.7 (thm:dfg27) | 10.2, 6.7 |
| $H^0(\Q,W^D)$ and Lemma lem:h0 (restated; proved in Chapter 11) | 10.3, 2.6 |
| the corrected sequence of Remark rem:ns ($-h_\ell(E)$) | 10.5, 12.1 |
| the adjoint motive; $L(\ad f,s)=L(\Sym f,s+1)$; Hodge numbers; critical values; Flach's theorem | 14.1, 14.6 |
| the symmetric square and the Petersson norm (connection) | 14.7 |
| Section 6 row: adjoint, $\Sym$, trace form, $A_f(1)=\Hom(A_f,\Zl(1))$ (with 4) | 2.4, 2.6, 14.1 |
| Section 6 row: $\Sigma$-imprimitive and Bloch-Kato Selmer groups, $H^1_f$, $H^1_\Sigma$ (with 17) | 5.1 to 5.5, 6.1 to 6.7 |
| Section 6 row: FPR Tamagawa factor (with 3, 16) | 7.1 to 7.6 |
| Section 6 row: computation of $\Tam_q(\ad T)$ at a multiplicative prime (with 16, 17) | 8.1 to 8.5 |
| Section 6 row: $h_\ell(E)$, $\bar\rho\simeq\bar\rho\otimes\chi$ (with 4, 11) | 10.3, 12.2 |
| Section 6 row: Taylor-Wiles, DFG04 Theorems 0.1, 0.2, 2.7, 3.7, Proposition 1.4, Lemma 2.1, Theorem 2.15 (with 20) | 10.2, 10.4, 7.4 (Theorem 2.15), 14.4, 14.5 (3.7 and 1.4: Chapter 20) |
| Section 6 row: finite flat group schemes, "good at $\ell$" (with 11) | 4.2, 4.4 |
| Section 6 row: Kummer classes, $H^1(G,\Zl(1))$, tame character (with 5, 7, 16, 17) | 8.1, 8.2 (Step 5) |
| hook: Section 1.2 (definition of $\Tam_p(M)$; the Bloch-Kato Selmer group) | 7.1, 7.3, 6.1, 6.6 |
| hook: Theorem thm:main and its proof in Section 4.3 | 11.1, 11.2, 9.4, 10.5 |
| hook: Theorem thm:dfg37 | 14.5 (home Chapter 20), 6.4 |
| hook: Theorem thm:dfg27 | 10.2 |
| hook: Lemma lem:dfg21 and the paragraph after it | 10.4, 5.3, 3.3, 3.4 |
| hook: Lemma lem:fpr | 7.4, 7.5, 3.5 |
| hook: Lemma lem:h0 | 10.3 |
| hook: Lemma lem:tamfactor (in full) | 8.2 (with 8.1, 8.3, 8.5) |
| hook: Remark rem:ko(1) | 8.3(iii), 8.5 |
| hook: Remark rem:ns | 12.1, 10.5 |
| hook: Section sec:tam | 13.1, 13.2 |
| hook: Open question 2 | 12.3 |
| hook: Open question 3 | 9.3, 9.4, 9.5 |
| hook: Conjecture conj:euler (the term $h_\ell(E)$) | 12.2, 10.3 |
| also: the abstract ("the length of the Bloch-Kato Selmer group of $\ad V_\ell E$"; "raises the bound by one whenever ...") | 6.6, 8.3 (Part 7, N2, N3) |
| also: Section sec:sharp ("the identity (eq:identity) says what the excess is") | 9.5, 11.3 |
| also: what Chapters 3, 4, 11, 15, 16, 21 defer to Chapter 18 (Part 5) | 2.4, 4.2, 4.4, 7.1, 7.4, 8.2, 10.3, 10.4 |

### 4.2 Exercises (Section 15 of the chapter), graded from easy to harder

1. (Frobenius conventions.) Compute $L_p(\Ql(1),s)$ with $\Phi_p$ and with $\Frob_p$. Show $L_p(M(1),s)=L_p(M,s+1)$ with $\Phi_p$. Check the paper's claim
   $L_p(A_f,1)^{-1}=L_p(A_f(1),0)^{-1}=1-p^{-2}$ at a multiplicative prime, and show that the arithmetic Frobenius would give $1-p^2$ (same $\ell$-adic valuation,
   different number).
2. Compute the Gram matrix of the trace form on $\ad T$ in the basis $e,h,f$, show $T^D\simeq A(1)$ for $\ell$ odd, and show the image of $A$ in $A^\vee$ has
   index $2$ when $\ell=2$ (2.4).
3. For each row of the table 3.2 find $H^0(\Q_p,V^D)$ and $H^0(\Q_p,A_f)$, and (granting the local Euler characteristic) the $\Zl$-rank of $H^1(\Q_p,T^D)$.
   Which bad primes have $H^1(\Q_p,T^D)$ infinite? Check the paper's claim that $H^1_f(\Q_p,T^D)$ is the torsion of $H^1(\Q_p,T^D)$ in each case.
4. Let $q$ be a multiplicative prime. Show $H^1_f(\Q_q,W)=0$ for $W=\ad T\otimes\Qlmod$, and that $H^1_{\mathrm{ur}}(\Q_q,W)=0$ when $\ell\nmid n_q$ ($W^{I_q}=(\Qlmod)e$). For
   $W=E[\ell^\infty]$, split reduction and $\ell\mid n_q$, show $H^1_{\mathrm{ur}}(\Q_q,W)\simeq\Z/\ell^{v_\ell(n_q)}$ while $H^1_f(\Q_q,W)=0$ (5.5).
5. Check the paper's claim $H^1(I_q,\ad T)_{\mathrm{tor}}\simeq(\Z/\ell^{v_\ell(n)})^2$ for 14a1 at $q=7$, $\ell=3$ ($n=3$, $\bar u\equiv-1$), compute the Frobenius invariants and
   $v_3(\Tam_7(\ad T))=2$, and explain why $\deg\varphi_{14a1}=1$ is no contradiction ($E[3]$ is reducible; Lemma lem:tamfactor needs no irreducibility).
6. Check the paper's claim that $c'$ is "well defined modulo $q-1$": show that changing the lift of $\Frob$ by $t^a$ and the cocycle by a coboundary
   changes $c'$ by an element of $(n,q-1)\Zl$ (not only of $(q-1)\Zl$), that $\min(v_\ell(n),v_\ell(q-1),v_\ell(c'))$ is unchanged, and that the "image of $\kappa$"
   exists through the splitting given by the uniformiser $q$, but not through a map defined for every uniformiser (point 7 and its addendum).
7. Check the paper's claim that "the same computation for $M=T$ gives ... the $\ell$-part of the Tamagawa number $c_q(E)$": for 11a1 at $q=11$,
   $\ell=5$ (split, $c_{11}=5$) and for 14a1 at $q=2$, $\ell=3$ (nonsplit, $n=6$, $c_2=2$).
8. Prove $\Tam_q(A(1))=\Tam_q(A)$ at a multiplicative prime by computing the invariants of $H^1(I_q,A(1))_{\mathrm{tor}}$ as the kernel of the linear form
   $(x,y)\mapsto(q-1)x-2\varepsilon c'y$ on $(\Z/\ell^v)^2$, and show both invariant modules are $\Z/\ell^v\oplus\Z/\ell^m$.
9. Prove 9.2: for $\sigma\in\GL_2(\Z_3)$ of order $3$, $\ad T$ is free over $\Z_3[\langle\sigma\rangle]$ while $H^1(\langle\sigma\rangle,T)\simeq\F_3$. Deduce that $\Tam_q(\ad T_3E)$ is trivial at
   a prime $q\ge5$ of type $\mathrm{IV}$, while $\Tam_q(T_3E)$ is $3$ when $c_q=3$ (for example 50a1 at $q=5$, type $\mathrm{IV}$, $c_5=3$).
10. Check the paper's claim in Remark rem:ko(1) on 791a1 ($[1,0,1,-31,117]$, $N=7\cdot113$): $n_7=3$, $\bar u\equiv-1\pmod7$ is a cube, so $v_3(\Tam_7(\ad T))=2$;
    the bound (eq:thm) is $1$, the refined bound $2$, and $v_3(\deg\varphi_E)=v_3(144)=2$.
11. Check the paper's claim in Lemma lem:fpr that $L_p(A_f,1)^{-1}$ is an $\ell$-adic integer of valuation $e_\ell(E,p)$ at an additive prime, for 121a1 at
    $p=11$ (type $\mathrm{II}$, $\ell=3$): $1-\chi_{-3}(11)/11=12/11$, $v_3=1$.
12. Prove the surjectivity at the right end of the sequence of Lemma lem:dfg21 (10.4, step 4), and show by an example of the general shape what
    fails when $\Sigma=\emptyset$.
13. Check the paper's claim (proof of Theorem thm:main) that $H^0(\Q,W^D)=0$ under its hypothesis, by the determinant argument; compute $h_3(\text{726a1})=1$
    and explain why the paper's finiteness argument via $a_p=0$ at inert primes is not the right one (points 5, 6).
14. Verify the four local terms of 6.7 and deduce $H^1_f(\Q,A_f)=0\iff H^1_f(\Q,V^D)=0$. Where is the sign convention C4 used?
15. Check the paper's claims of Section sec:tam on a small range: with the series $\mathsf q(j)$ of Chapter 10, 7.2, compute Tate parameters and unit parts,
    and reproduce, for conductors at most $2000$ and $\ell=3$, the counts $128$ curves in the population, equality $87\to102$, and $19$ curves with a positive
    Tamagawa excess (13.1; Part 6.6).
16. (Harder.) Show that the shape 14.2 for $M=V_\ell E$ reproduces the local and torsion terms of the Birch and Swinnerton-Dyer formula, and for $M=A_f(1)$
    identifies each term with a term of (eq:identity); where does $h_\ell(E)$ appear?

________________________________________________________________________________

## 5. Dependencies and forward pointers

Results from earlier chapters used here (cited with `\Cref{ch:...}`, never reproved):
* Chapter 2 (`ch:rings`): $v_\ell$ of rationals ($1-p^{-2}$, $(q+1)^2-a^2$), the $\ell^k$-th powers in $\F_q^\times$ and the index $\ell^{\min(k,v_\ell(q-1))}$ (for $c(u)$).
* Chapter 3 (`ch:modules`): Fitting ideals and lengths over $\Zl$ (7.4 to 7.6), Pontryagin duality and $T$ versus $T\otimes\Qlmod$ (8.1 to 8.4), lengths in exact
  sequences.
* Chapter 4 (`ch:reps`): the trace form and $\Hom(A,\Zl(\chi))\simeq A(\chi)$ (7.6); invariance of $\ad$ (7.7); $\ad\simeq\Sym\otimes\det^{-1}$; unipotent and cyclic
  shapes (9.1 to 9.4); the twist-length lemma (10.5).
* Chapter 5 (`ch:galois`): $\Zl(1)$, $\chi_\ell$, Kummer cocycles (galois:l-adic-kummer), $\F_q$-Kummer theory (galois:kummer-finite-field), the determinant
  obstruction (galois:twist (c)).
* Chapter 6 (`ch:ant`): $\Z_3[\zeta_3]$ as a DVR and $T\simeq\Z_3[\zeta_3]$ (4.7, 4.8); the commutant (4.10).
* Chapter 7 (`ch:local`): L3, L6, 4.3 (Frobenius dictionary), 5.2 to 5.5 (inertia, tame character, $\Frob\,t\,\Frob^{-1}=t^q$, Frobenius fixing roots), 6.2
  (the Kummer class on inertia and $\kappa=a\kappa_\varpi+\kappa_u$), 8.1, 8.2 ($V^{I}$, $L$-factors), 9.1 to 9.4 (local shapes and adjoint $L$-factors).
* Chapter 9 (`ch:ellcurves`): Weil pairing, Hasse bound, $c_p$ and the BSD orientation.
* Chapter 10 (`ch:reduction`): Tate parameter $\mathsf q(j)$ and unit part (7.2, 7.4, 7.8), $c_q$ at multiplicative primes (7.6), potentially multiplicative
  additive reduction (7.7), Kodaira types, Kraus's defect.
* Chapter 11 (`ch:galrep`): the Tate shape with corner $\varepsilon\kappa$ (3.2), Lemma lem:tamagawa-exp (3.3), potentially multiplicative primes at every
  $q$ (3.4), inertia images by type (Section 4), crystalline at $\ell$ (5.1), Lemma lem:h0 (8.5), $S_f$ (8.6).
* Chapter 14 (`ch:moddeg`): 9.5 (Lemma lem:hecke as an equality: points 39, 56) and the checklist 9.6; 9.1(d) ($M_{f,\lambda}\simeq T_\ell E(-1)$); 7.3
  (Zagier-Watkins, for 14.7).
* Chapter 15 (`ch:modgalrep`): 4.1 (crystalline at $\ell$, Fontaine-Laffaille range for $M_f$).
* Chapter 16 (`ch:cohomology`): continuous-cohomology, les-continuous, h0-and-torsion, inflation-restriction, res-inf-cor (d), order-kills,
  z2-on-l-adic, conjugation-action, cohomology-through-pro-l-quotient, tame-inertia-example, procyclic-compact, cocycle-on-powers,
  frobenius-on-h1-inertia, tate-curve-shape-matrices, model-computation, fitting-ideal-of-invariants, lengths-in-exact-sequences,
  h1-finitely-generated, galois-cohomology-convention, unramified-h1-preview.
* **Chapter 17** (`ch:galcoh`; its outline is now written, and the inputs below are its items, given in brackets): **K1** [3.3, 3.4] Tate local duality
  $H^i(\Q_p,M)\times H^{2-i}(\Q_p,M^D)\to\Qlmod$ for finite $M$, and its versions for $(W,T^D)$ and $(V,V^D)$; **K2** [3.2] the local Euler characteristic formula
  (for $p\ne\ell$: $\#H^0\#H^2/\#H^1=1$ for finite $M$; ranks for lattices); **K3** [4.1 to 4.3] $H^1_{\mathrm{ur}}(\Q_p,M)=M^{I_p}/(\Frob_p-1)M^{I_p}$ and the exact sequence
  $0\to H^1_{\mathrm{ur}}\to H^1\to H^1(I_p,M)^{G}\to0$; **K4** [4.4, 4.5] for $p\ne\ell$, $H^1_{\mathrm{ur}}$ of $M$ and of $M^D$ are exact annihilators (finite $M$ of order prime to $p$; the
  divisible and compact versions); **K5** [10.1 to 10.4] the comparison exact sequence for two Selmer structures $\mathcal F\subseteq\mathcal G$ (Poitou-Tate), in the five-term
  form used in 10.4, with discrete coefficients $W$ and compact dual $T^D$; **K6** [2.2] the sequences relating $H^1(K,T)$, $H^1(K,V)$, $H^1(K,W)$ and
  $H^1(K,T)_{\mathrm{tor}}=\delta H^0(K,W)$; **K7** [9.3, 9.5] the Greenberg-Wiles formula (finite coefficients) and, if Chapter 17 states it, its $\Ql$ version (otherwise 6.7
  states the $\Ql$ version as R); **K8** [5.1 to 5.4] the Kummer class of the Tate parameter and the identification of $H^1(G/I,\Zl(1))=\Zl(1)/(q-1)$ with $\F_q^\times\otimes\Zl$ (the
  cohomological half of point 7). Chapter 17 also proves $H^1_f(\Q_p,T^D)=H^1(\Q_p,T^D)_{\mathrm{tor}}\simeq H^0(\Q_p,W^D)$ for $p\in\Sigma$ (its 4.6) and the abstract length identity (its 10.4); Chapter
  18 cites them. If any input turns out to be missing in the written Chapter 17, Chapter 18 states it as R with reference (NSW, MilneADT, Rubin) rather than proving it.

Black boxes imported from later chapters (stated with a forward `\Cref`, used only in remarks, examples and `paperlink`s): the values
$e_\ell(E,q)$ and Lemma lem:euler (Chapter 19; used in 3.2, 3.5, 11.3); $L(\Sym f,s)$, Rankin-Shimura and $L(\ad f,1)\ne0$ (Chapter 19; used in 14.1,
14.7); thm:dfg14, thm:dfg37, Lemma lem:hecke and the assembly (Chapter 20; used in 11.2, 14.5).

Forward pointers (chapters that use this one):
* Chapter 19 (`ch:lfunctions`): 3.1 (Frobenius dictionary for $L$-factors), 3.2, 3.5 (integrality of $L_q(A_f,1)^{-1}$), 14.1 (the adjoint motive and
  $L(\ad f,s)=L(\Sym f,s+1)$), 14.2 (the shape of the Bloch-Kato conjecture for the adjoint).
* Chapter 20 (`ch:congruence`): 10.1 ($S_f$), 10.2 (thm:dfg27), 10.4 (lem:dfg21), 7.4, 7.5 (lem:fpr), 10.3 (lem:h0 in Selmer form), **11.1 (the
  Selmer half of the proof of Theorem thm:main)**, 9.4 (the explicit Tamagawa terms), 12.1 (Remark rem:ns, Open question 2), 14.4 (DFG04
  Theorem 0.1). Chapter 20 should cite 11.1 rather than repeat the Selmer bookkeeping.
* Chapter 21 (`ch:paper`): A1.3 (cite 7.1, 7.3), A2.7 (cite 8.2 and 8.4; the step list there matches 8.2), A4.6 to A4.11 (cite 6.3, 10.1 to 10.5, 7.4,
  7.5), the proof of Theorem thm:main (11.1, 11.2), Remark rem:ns (12.1), Section sec:tam (13.1), Open questions 2 and 3 (12.3, 9.3 to 9.5).
* Chapter 22 (`ch:computation`): 8.5 and the script of Part 6.6 (Tate parameters via $\mathsf q(j)$ or `ellinit(E,O(q^k)).tate`; unit parts; the
  Tamagawa terms), 13.1 (reproducing Section sec:tam), 9.5 (the excess distribution).

________________________________________________________________________________

## 6. Notes for the writer

### 6.1 Conventions to typeset (Section 1, as `convention` environments)

C1 to C8 of Part 1.3. In addition two `warning` boxes in Section 1: "**Three duals.** $M^\vee=\Hom(M,\Zl)$ (linear; Bloch-Kato's $V^*$), $M^D=\Hom(M,\Zl(1))$
(Kummer-Cartier; the paper's ${}^D$), $X^*=\Hom(X,\Qlmod)$ (Pontryagin; the paper's ${}^*$). Tate local duality pairs $H^1(\Q_p,W)$ with $H^1(\Q_p,T^D)$, and the
Pontryagin dual of a finite group is the only ${}^*$ in Lemma lem:dfg21." and "**Two Frobenii.** $\Frob_p$ arithmetic in group theory (Lemma
lem:tamfactor), $\Phi_p=\Frob_p^{-1}$ in $L$-factors (Section 1.1, Lemma lem:fpr, the paragraph after Lemma lem:dfg21); the paper names neither
(important_notes.md point 11). In cohomology the choice is invisible up to $\ell$-adic units; in $L$-factors it is not."

### 6.2 Pitfalls

* **Tate twists and Frobenius.** On $\Zl(1)$ the arithmetic Frobenius at $p\ne\ell$ acts by $p$ and the geometric one by $p^{-1}$. So on $(V^D)^{I_p}=A_f^{I_p}(1)$ at a
  multiplicative prime $\Frob_p$ acts by $p\cdot p=p^2$ and $\Phi_p$ by $p^{-2}$; $\det(1-\Phi_p)=1-p^{-2}=L_p(A_f,1)^{-1}$. Never write $1-q^{1-s}$ for the
  multiplicative adjoint factor (point 11).
* **The dual $V^D$ is $V^\vee(1)$, not $V(1)$.** For $A_f$ they agree only through the trace form, which needs $\ell$ odd (2.4). Write the isomorphism once,
  name it, and use $A(1)$ thereafter as the paper does.
* **"Unramified" is not "$f$" for $W$.** $H^1_f(\Q_p,W)$ is the divisible part of $H^1_{\mathrm{ur}}(\Q_p,W)$ (5.3(iv)); the difference is exactly the Tamagawa
  phenomenon (5.5). For $T$ the inclusion goes the other way: $H^1_{\mathrm{ur}}(\Q_p,T)\subseteq H^1_f(\Q_p,T)$ with index $\ell^{v_\ell(\Tam_p(T))}$ (7.2). DFG04's $H^1_\Sigma$ imposes
  the unramified condition outside $\Sigma\cup\{\ell\}$, which equals the $f$ condition there only because $W$ is unramified there (6.3).
* **$H^1(\Q_p,T^D)$ need not be finite at $p\in\Sigma$** (3.3, 3.4: type $\mathrm{III}$ with $p\equiv1\pmod4$, every $\mathrm I_0^*$ prime); the paper's
  "$H^1_f(\Q_p,T^D)$ is the torsion of $H^1(\Q_p,T^D)$, a finite group" is right as stated; do not "simplify" it to "$H^1(\Q_p,T^D)$ is finite".
* **The parenthesis in $\Tam_p$** (point 37): $\Fitt\bigl((H^1(I_p,M)_{\mathrm{tor}})^{G_{\Q_p}}\bigr)$, the Fitting ideal of the invariants.
* **The class $c'$** (point 7 and its addendum): "the image of $\kappa$ in $H^1(G/I,\Zl(1)^I)$" is meaningful only via the canonical splitting given
  by the uniformiser $q$ (Chapter 17, 5.3); $c'$ is a cocycle value, equal to $\varepsilon$ times that image only for the lift $\Frob_0$ fixing the $\ell$-power
  roots of $q$, and in general well defined modulo $(n,q-1)\Zl$, not $q-1$; only the minimum matters.
* **The corner $\varepsilon\kappa$** (point 42) and **arithmetic $\Frob$ in Lemma lem:tamfactor** (point 11): $\rho(\Frob)=\begin{psmallmatrix}\varepsilon q&\varepsilon\kappa(\Frob)\\0&\varepsilon\end{psmallmatrix}$.
* **$v_\ell(c(u))$ when $\bar u$ is an $\ell^{v_\ell(q-1)}$-th power** (point 31): read as $v_\ell(q-1)$; when $\ell\nmid q-1$ the minimum is $0$ whatever $\bar u$ is.
* **$c_q$ means the Tamagawa number** (point 23); the class of the unit part is $c(u)$ or $c_q(u)$.
* **$\mathrm I_n^*$ at $q=2$** (point 18): use 8.4 (local twist over $\Q_2$), not Lemma lem:twist, and $\nu=-v_2(j)$, not the index of the symbol.
* **$h_\ell(E)$**: the criterion is $\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$; $h_\ell=0$ for $\ell\ge5$ and $h_3\le1$ for every $E$ (points 5, 6, 14). The paper's sentence on
  finiteness for non-CM curves is replaced by the determinant argument; do not repeat "for $E$ without complex multiplication it is finite".
* **Hodge-Tate sign** (C4): fix it once; 4.5 depends on it; when quoting DFG04 or BlochKato check their sign.
* **The equality in (eq:identity)** is Chapter 14's theorem (point 39); the DFG04 checklist (point 56) is settled (Chapter 20 outline, Part 7; important_notes.md point 73): say "with
  equality whenever $\ell\notin S_f$, by `\Cref{ch:moddeg}` and `\Cref{ch:congruence}`", never "with equality when multiplicity one holds".
* **Remark rem:ns is conditional** on $H^1_f(\Q,V^D)=0$ for the 3Ns curves (12.1); state the condition every time.
* **Section sec:tam's population** in the paper is type $\mathrm I_n$ only; 9.4 shows that $\mathrm I_n^*$ primes carry the same Tamagawa excess; say so, do not
  change the paper's numbers.
* **Theorem numbers marked (verify)**: BlochKato Definition 3.7, Proposition 3.8, Corollary 3.8.4, Example 3.11, Section 5, Section 6;
  FPR94 I.3, I.4.2.2, III; Rubin 1.3, 1.4.3, 1.5, 1.6, 1.7.3; DDT 2.19; Wiles95 Proposition 1.6; DFG04 Sections 1.1 to 1.7, 2.1 to 2.3, (31), (57),
  Theorems 0.1, 0.2, 2.7, 2.15, 3.7, p. 708 (cite as the paper cites them); Kraus90 for the inertia groups at $2$ and $3$; Flach92's hypotheses;
  SGA 7 Expose IX for 7.6. Cite by section unless checked.

### 6.3 What to leave to Chapters 7, 11, 16, 17, 19, 20

* **Chapter 7**: Frobenius conventions, Weil-Deligne representations, $L$-factors and the local shapes table; Kummer classes on inertia and the
  field-theoretic identification of $c'$. Chapter 18 cites them (3.1, 3.2, 8.1).
* **Chapter 11**: the Tate shape, Lemma lem:tamagawa-exp, the potentially multiplicative case, inertia images by Kodaira type, crystallinity
  at $\ell$ (as a statement), **Lemma lem:h0 in corrected form (its 8.5)** and $S_f$ (8.6). Chapter 18 restates lem:h0 in Selmer form (10.3) and
  does not reprove the determinant argument beyond one sentence.
* **Chapter 16**: all group cohomology, in particular the computation $(t-1)M=n'(\Zl e\oplus\Zl h)$, $H^1=(\Zl/n')^2\oplus\Zl$, the Frobenius action and the
  invariants (its Section 10). Chapter 18's 8.2 cites Steps 2 to 4 from there and adds Steps 1, 5, 6 and the definition.
* **Chapter 17**: Tate local duality, local Euler characteristic, $H^1_{\mathrm{ur}}$ and its annihilator, Poitou-Tate and Greenberg-Wiles, the comparison
  sequence for Selmer structures, the $T$, $V$, $W$ sequences, the Kummer class of the Tate parameter (inputs K1 to K8). Chapter 18 instantiates
  them with the Bloch-Kato conditions; it does not reprove them.
* **Chapter 19**: the table of omitted Euler factors, Lemma lem:euler, $e_\ell(E,q)$, $P_q$, the naive factor (point 30), $L(\Sym f,s)$, Rankin-Shimura.
  Chapter 18 uses only the values and their integrality.
* **Chapter 20**: congruence ideals, thm:dfg14, thm:dfg37 (Taylor-Wiles), Lemma lem:ddt417 (point 19 lives there), Lemma lem:hecke, the assembly of
  Theorem thm:main, Theorem thm:quant, Remark rem:ko(2). Chapter 18 supplies 11.1 and states 14.5 only as a pointer.

### 6.4 How each relevant point of important_notes.md is handled

* **Point 5** ($h_\ell=0$ for $\ell\ge5$, $h_3\le1$, CM irrelevant; the paper's finiteness argument confuses $\chi_\ell$ with $\chi_{\ell^*}$): 10.3(ii), citing Chapter
  11, 8.5; Exercise 13; pitfall in 6.2.
* **Point 6** (the criterion for $h_\ell>0$ is $\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$): 10.3(ii), 12.2; the `paperlink` for Section 1.3 quotes the corrected wording.
* **Point 7** (with the addendum from the Chapter 17 outline): the paper's "image of $\kappa$ in $H^1(G/I,\Zl(1)^I)$" is read via the canonical
  splitting $H^1(\Q_q,\Zl(1))=\Zl\kappa_q\oplus H^1_{\mathrm{ur}}$ given by $q$; $c'=\varepsilon\cdot$(that image) for $\Frob_0$; indeterminacy $(n,q-1)$, not $q-1$: 8.2, Step 5,
  citing Chapter 17, 5.3 and 5.4; Exercise 6.
* **Point 11** (geometric Frobenius in $L$-factors, arithmetic in Lemma lem:tamfactor): C3, 3.1, 3.3, 8.2 Step 4; warning box; Exercise 1.
* **Point 12** ($\End_{I_q}(T)=\Zl[\sigma]$, not $\End_{I_q}(V)$ a field): 9.2 works with $T\simeq\Z_3[\zeta_3]$ and says "the commutant of $\sigma$ in $\End(T)$ is $\Z_3[\sigma]$"; the
  $V$-statement is never used.
* **Point 19** ($\wp\cap I=0$ in Lemma lem:ddt417): not used in Chapter 18; it belongs to Chapters 3 and 20. Mentioned only in 6.3.
* **Point 26** ($M_{f,\lambda}$ is homothetic to the dual of $T_\ell E$): 2.4(ii), citing Chapter 14, 9.1(d).
* **Point 31** (the reduction of $u$; the reading of $v_\ell(0)$): C6, 8.2.
* **Point 37** (the parenthesis in $\Tam_p$): 7.1, with a `paperlink` quoting the display.
* **Point 39** (Lemma lem:hecke is always an equality, so (eq:identity) is an equality for $\ell\notin S_f$): 9.4, 11.2, citing Chapter 14, 9.5; consequence in
  9.5 and 11.3 (the excess is the Selmer length).
* **Point 40** ($M_{f,\lambda}=\varphi_E^*H^1(E,\Zl)\simeq T_\ell E(-1)$ exactly): 2.4(ii).
* **Point 42** (corner $\varepsilon\kappa$): C6, 8.1(a), 8.2 Step 4.
* **Point 47** ($\ell\notin S_f$ iff $E[\ell]$ irreducible and $h_\ell(E)=0$, for $\ell\nmid2N$): 10.1.
* **Point 56** (the DFG04 checklist): settled by point 73 (Chapter 20 outline, Part 7); 11.2 and 9.4 cite Chapter 14, 9.6 and the Chapter 20 outline's Part 7.
* **B1** (on $V_\ell E$ the arithmetic Frobenius has eigenvalues $\alpha,\beta$): C3, 3.2.
* **B6** (PLAN.md's Weil-Deligne relation is the geometric form): not needed here; C3 follows Chapter 7's L3, L4.
* **B7** (Chapter 21's C2(b): $\det(1-\Phi p^{-s}\mid V_\ell E)^{-1}=L_p(E,s+1)$, and point 42 in its A2.7): C3, 3.1(d); 8.2 is the version Chapter 21's A2.7 should
  cite.
* **B14** (bibliography): checked `refs.bib` and every `bib/*.bib`. All keys this chapter needs are already in `refs.bib`: BlochKato, FPR94,
  DFG04, Fontaine, Berger, FontaineLaffaille, Flach92, Rubin, NSW, MilneADT, TateDuality, Greenberg89, Wiles95, Washington, Deligne79,
  Shimura76, GelbartJacquet, Kraus90, SilvermanATAEC, DDT, Hida81, Tate95, PARI, ecdata. The chapter bib files are empty except `bib/chA.bib`.
  Proposed new keys: none required. Optional, only if the writer cites them after checking: `SerreTate68` (already proposed for refs.bib
  by B16; needed here for the inertia groups in 9.3), `SGA7` (Grothendieck, *Modeles de Neron et monodromie*, SGA 7 I, Expose IX,
  Lecture Notes in Math. 288, 1972; for 7.6; Chapter 10 may also want it, so refs.bib), `ColemanIovita99` (R. Coleman, A. Iovita, *The
  Frobenius and monodromy operators for curves and abelian varieties*, Duke Math. J. 97 (1999); for the converse in 4.2; bib/ch18.bib).
  Bibliographic details recalled, not re-verified.

### 6.5 References

Main sources, in the order of the chapter: Rubin (Euler Systems, Chapter 1, for local and global conditions, propagation, the comparison
sequence; cite sections), BlochKato (Sections 3 to 6), FPR94 (I.3, I.4, III), Fontaine and Berger (for $B_{\mathrm{dR}}$, $B_{\mathrm{cris}}$), FontaineLaffaille,
NSW and MilneADT (local duality, Poitou-Tate), Wiles95 (Greenberg-Wiles), DFG04 (Sections 1, 2, 3; (31), (57), p. 708; Theorems 0.1, 0.2, 2.7,
2.15; Lemma 2.1), Flach92, Deligne79 (critical values), Shimura76 and GelbartJacquet (the symmetric square), Kraus90 (inertia images), the
paper's own references for the data (Cremona97, PARI, ecdata).

### 6.6 Verification log (computations done for this outline)

Python 3 with PARI/GP 2.17 through `cypari2`; scripts `h1c3.py`, `tate2.py`, `tamcheck.py`, `tamcheck2.py`, `brute.py`, `rule.gp` in the session
scratchpad (`ch18/`); Cremona's `ecdata` files (`allcurves`, `degphi`, `galrep`) for conductors below $10{,}000$ in `/tmp/ch09/data`.
* **Tate parameters.** $\mathsf q(j)$ as `serreverse(1/ellj(x+O(x^60)))` (Chapter 10, 7.2: $j^{-1}+744j^{-2}+750420j^{-3}+\cdots$), evaluated at $1/j_E$ in $\Q_q$;
  agrees with `ellinit(E,O(q^40)).tate[3]` for 11a1 at $11$, 14a1 at $7$ and at $2$. Unit parts as in 8.5 (11a1: $10$; 14a1 at $7$: $6$, at $2$: $1$; 539c1: $5$ at
  $7$, $3$ at $11$, agreeing with Chapter 10, 7.8; 791a1: $6$ at $7$, $106$ at $113$; 874b1: $18$ at $19$; 1184f1: $36$ at $37$; 1748e1: $12$ at $19$).
* **Brute force of Lemma lem:tamfactor and of 7.5** (`brute.py`): for $\ell\in\{3,5\}$, $v\in\{0,1,2\}$, all primes $q<120$, $q\ne\ell$, $\varepsilon=\pm1$, $c'\in\{0,\dots,\ell^3-1\}$, the
  number of $\Frob$-invariants of $(\Z/\ell^v)\bar e\oplus(\Z/\ell^v)\bar h$ for the action $q^{-1}\Ad\rho(\Frob)$ (module $A$) and $\Ad\rho(\Frob)$ (module $A(1)$) equals
  $\ell^{v+\min(v,v_\ell(q-1),v_\ell(c'))}$ in all $52{,}896$ cases.
* **$\Tam(T)$ versus $c_q$** at multiplicative primes: for all curves of `allcurves` below conductor $3000$ and $\ell\in\{3,5,7\}$, $\ell\ne q$, $v_\ell(c_q)=v_\ell(n_q)$ if
  $a_q=1$ and $0$ if $a_q=-1$: $101{,}336$ pairs, no mismatch.
* **9.2** (`h1c3.py`): with $\sigma=\begin{psmallmatrix}0&-1\\1&-1\end{psmallmatrix}$ acting on $\ad T$ by conjugation (basis $e,h,f$), $\ker N=(\sigma-1)\ad T$ (Smith form of the
  inclusion: $[1,1]$), so $H^1(C_3,\ad T)=0$; $\{e,\sigma e,\sigma^2e\}$ is a $\Z$-basis (determinant $\pm1$), so $\ad T\simeq\Z[C_3]$; by hand $H^1(C_3,T)=T/\pi T\simeq\F_3$.
* **The refined inequality and Section sec:tam** (`tamcheck2.py`): optimal curves of `degphi` below $10{,}000$, non-CM ($j$ not among the $13$ CM
  values; CM curves carry no mod-$3$ label in `galrep`, and the CM curves 121b1, 256a1, 256d1, 1936f1, with mod-$3$ image of split Cartan type,
  are the only "violations" if CM curves are not removed), $\ell\in\{3,5,7\}$, $\ell\nmid N$, $E[\ell]$ irreducible (no label $\ell$B or $\ell$Cs), and for $\ell=3$ no
  label 3Ns. $e_\ell(E,q)$ from `lfunsympow`/`lfuneuler` exactly as the paper's `rule`; Tamagawa terms by 9.4 at all potentially multiplicative
  primes. Results as in 9.5 and 13.1; no violation. For conductor at most $2000$: at $\ell=3$, $2{,}158$ curves, population $128$, equality $87\to102$,
  positive excess $19$ (Exercise 15).
* **The paper's `rule`** (appendix, copied verbatim into `rule.gp`): 121a1 gives $[1,1]$, 726a1 gives $[2,2]$ with and without `iii`, as the paper
  says; 791a1 gives $[2,1]$ (the Tamagawa excess is not in `rule`).
* **Inertia types**: 50a1 has type $\mathrm{IV}$ at $5$ with $c_5=3$; 196b1 ($\mathrm{IV}^*$ at $7$), 225b1, 225e1 likewise (Exercise 9).
* By hand: the matrix identities of 8.2 Step 4 ($F hF^{-1}=h-2\varepsilon c'e$, $FeF^{-1}=qe$); the change of $c'$ under $\Frob\mapsto\Frob t^a$; the local terms of 6.7
  (complex conjugation on $A_f$: eigenvalues $1,-1,-1$); $\Sym$ of a $2\times2$ Jordan block in characteristic $3$ is a $3\times3$ Jordan block; the exactness
  argument of 10.4 step 4; $W^{I}=(\Qlmod)e$ at a multiplicative prime with $\ell\nmid n$; $H^1_{\mathrm{ur}}(\Q_p,E[\ell^\infty])\simeq\Z/\ell^{v_\ell(n)}$ in 5.5.
* Not checked: the theorem numbers marked (verify); DFG04's normalisations ((31), (57), Section 1.7) and its treatment of $\ell=3$ (Part 7, Q1); the
  exact list of inertia groups at $q=2,3$ (Kraus90) beyond the facts that their orders divide $24$ and that a Sylow $3$-subgroup has order $3$.

________________________________________________________________________________

## 7. Points for important_notes.md

New points in this chapter's area (Bloch-Kato Selmer groups, Tamagawa factors, Lemma lem:fpr, Lemma lem:tamfactor, Lemma lem:dfg21,
Remark rem:ns, Section sec:tam, Open questions 2 and 3), not among points 1 to 62 and B1 to B20 and not among the Chapter 17 outline's
N1, N2. Points 5, 6, 7 (with its addendum), 11, 12, 18, 19, 23, 26, 31, 37, 39, 40, 42, 47, 56, B1, B6, B7, B14 are handled in Part 6.4 and not repeated.

**N1. Open question 3, first half, has an answer: $\Tam_q(\ad T)$ is trivial at every additive prime of potentially good reduction, and is
given by Lemma lem:tamfactor (with the Tate parameter of $j_E$) at every potentially multiplicative prime.**
Location: Open question 3 ("Compute the Tamagawa factors of $\ad T$ at the additive primes"); the proof of Theorem thm:main ("$v_\ell(\Tam_p(\ad T))\ge0$
at an additive prime").
Content: let $\ell$ be odd and $q\ne\ell$ additive. (a) Potentially good: inertia acts on $T$ through a finite group $\Delta$ of order dividing $24$, and
$H^1(I_q,\ad T)_{\mathrm{tor}}=H^1(\Delta,\ad T)$ (inflation-restriction; the rest of $H^1(I_q,\ad T)$ embeds in $\ad T(-1)$, torsion-free). If $\ell\ge5$ this is $0$ ($\#\Delta$ prime to
$\ell$). If $\ell=3$ its $3$-part injects into $H^1(P,\ad T)$ for a Sylow $3$-subgroup $P$ of order $3$ ($9\nmid24$), and $\ad T$ is a free $\Z_3[P]$-module (the
reduction is the adjoint of a nontrivial $2\times2$ unipotent in characteristic $3$, a single $3\times3$ Jordan block, i.e. the regular module;
Nakayama), so $H^1(P,\ad T)=0$. Hence $\Tam_q(\ad T)=\Z_\ell$ (and $\Tam_q(\ad T(1))=\Z_\ell$), even at types $\mathrm{IV}$, $\mathrm{IV}^*$ with $\ell=3$, where $\Tam_q(T)$ can be
$3$ (for example 50a1 at $5$). (b) Potentially multiplicative: $\ad T\simeq\ad(T\otimes\chi)$ for a ramified quadratic $\chi$ of $G_{\Q_q}$ making $T\otimes\chi$ of Tate shape
with parameter $\mathsf q(j_E)$, so $v_\ell(\Tam_q(\ad T))=t_\ell(E,q)+\min(t_\ell(E,q),v_\ell(q-1),v_\ell(c_q(u)))$, also at $q=2$ (this also settles point 18). Consequently
(eq:identity) becomes fully explicit: $v_\ell(\deg\varphi_E)-\bigl[\sum_qe_\ell(E,q)+\sum_{v_q(j)<0}\bigl(t_\ell(E,q)+\min(t_\ell(E,q),v_\ell(q-1),v_\ell(c_q(u)))\bigr)\bigr]=\len H^1_f(\Q,W)$ (with
equality in (eq:identity) by point 39; the checklist of point 56 is settled by point 73), which also answers the second half of Open question 3 as far
as it can be answered from $\deg\varphi_E$. Data (optimal non-CM curves, conductor below $10{,}000$, $\ell\nmid N$, $E[\ell]$ irreducible, not 3Ns): the excess is
never negative; it is $0$ for $8{,}688$ of $13{,}203$ curves at $\ell=3$, $19{,}019$ of $23{,}361$ at $\ell=5$, $25{,}133$ of $28{,}134$ at $\ell=7$.
Fix: replace "$v_\ell(\Tam_p(\ad T))\ge0$ at an additive prime" by the exact values, and restate Open question 3 as the computation of the Selmer
length. Confidence: high (the group theory is elementary; the freeness was checked by computer with an explicit basis; the only
imported fact is that potentially good inertia images over $\Q_q$, $q\ne\ell$, have order dividing $24$, Serre-Tate and Kraus90, which should be
cited with the exact statement).

**N2. Abstract: the Tamagawa sentence omits the condition $\ell\mid n_q$.**
Location: abstract, "the data confirm the Tamagawa factor formula, which raises the bound by one whenever a Steinberg prime $q\equiv1\pmod\ell$
has a Tate parameter whose unit part is an $\ell$-th power".
Problem: by Lemma lem:tamfactor the excess is $\min(v_\ell(n_q),v_\ell(q-1),v_\ell(c))$, which is $0$ when $\ell\nmid n_q$, whatever the unit part; Remark rem:ko(1) and
Section sec:tam state the condition $\ell\mid n$ correctly. Also "by one" is "by at least one" (the excess can be $2$ when $\ell^2$ divides $n_q$ and $q-1$).
Fix: "whenever a multiplicative prime $q\equiv1\pmod\ell$ with $\ell\mid n_q$ has a Tate parameter whose unit part is an $\ell$-th power (by
$\min(v_\ell(n_q),v_\ell(q-1),v_\ell(c))$, so by at least one)". Confidence: high.

**N3. Abstract: "the length of the Bloch-Kato Selmer group of $\ad V_\ell E$".**
Location: abstract ("the length of the Bloch-Kato (written with a double hyphen in the source) Selmer group of $\ad V_\ell E$ plus the Tamagawa factors plus the omitted Euler factors").
Problem: the Selmer group of the $\Ql$-representation $\ad V_\ell E$ is a $\Ql$-vector space, which is $0$ under the hypothesis (DFG04 Theorem 2.7, "and the
same for $A\otimes\Ql$"); the length meant is that of $H^1_f(\Q,\ad T\otimes\Qlmod)$, as in Theorem thm:main. Fix: "of $\ad T_\ell E\otimes\Qlmod$". Also "when
multiplicity one holds at level $N$ equals" can become "equals" by point 39 (subject to point 56). Confidence: high; low importance.

**N4. Remark rem:ns: the vanishing of $H^1_f(\Q,V^D)$ for the 3Ns curves is an unverified hypothesis, and it is the only one.**
Location: Remark rem:ns ("the exact sequence of Lemma lem:dfg21 still does [apply] whenever $H^0(\Q,V^D)=H^1_f(\Q,V^D)=0$"), Section 1.3 ("the correction is
the term that Lemma 2.1 of DFG04 produces"), Open question 2.
Problem: $H^0(\Q,V^D)=0$ always holds (weights), but for image $N_s(\F_3)$ one has $3\in S_f$, so DFG04 Theorem 2.7 does not give $H^1_f(\Q,V^D)=0$; the paper
leaves open whether the condition holds, and Section 1.3 states the conclusion without it. By the Greenberg-Wiles count with $\Ql$
coefficients the condition is equivalent to $H^1_f(\Q,\ad V_3E)=0$. Fix: in Section 1.3 and Open question 2, say "provided $H^1_f(\Q,\ad V_3E)=0$ (not
covered by DFG04 Theorem 2.7 in this case)", or cite a result proving it for residually dihedral representations after checking it.
Confidence: medium-high (the logic is certain; whether later literature already proves the vanishing for these curves was not checked).

**N5 (optional). Section sec:tam: the test can include the $\mathrm I_n^*$ primes, and one phrase overstates.**
Location: Section sec:tam ("at a prime $q$ of type $\mathrm I_n$ with $\ell\mid n$ and $q\equiv1\pmod\ell$"; "the extra divisibility of the modular degree is exactly
where the Tamagawa factor of the adjoint exceeds $\ell^{t_\ell}$").
Content: by N1(b) a prime of type $\mathrm I_n^*$ (any $q\ne\ell$) carries the same Tamagawa excess, computed from $\mathsf q(j_E)$; including such primes, our
recomputation below conductor $10{,}000$ ($\ell=3$: $1{,}050$ curves, equality $56.8\%\to68.0\%$; $\ell=5$: $252$ curves, $203\to220$) shows no violation. The phrase
"exactly where" should read "is accounted for, in these cases, by"; extra divisibility also comes from the Selmer group (N1). Confidence:
high for the data and the mathematics; optional.

**Q1 (open check, not claimed as an error; now SETTLED: DFG04 covers $\ell=3$ in weight $2$, Chapter 20 outline, Part 7; important_notes.md point 73). DFG04 at $\ell=3$ for weight $2$.**
The paper reads DFG04 (31) as $S_f=\{\lambda\mid2N\}\cup\{\text{not absolutely irreducible over }\Q(\sqrt{\ell^*})\}$ for $k=2$. DFG04 build integral structures and the local
condition at $\ell$ with Fontaine-Laffaille theory; for $M_f$ (weights $0,1$) this needs $\ell\ge3$, but the adjoint has weights spanning an interval of length
$2>\ell-2$ when $\ell=3$. Before the book asserts Theorem thm:main at $\ell=3$, the writer must check in DFG04 that $\ell=3$ is not excluded for $k=2$
(for instance by a condition such as "$\ell>k+1$" or "$\ell\nmid(k+1)!$" in (31) or in Sections 1 and 2) and how the adjoint's local condition at $\ell$ is
defined there. If $\ell=3$ were excluded, Theorem thm:main at $\ell=3$ would lose its Taylor-Wiles input (the data would be unaffected). Confidence:
none either way here (DFG04 not consulted); settled since by the Chapter 20 outline (Part 7): DFG04 covers $\ell=3$ (point 73).

Book-internal inconsistencies found while preparing this outline:

* **B-a. PLAN.md, Chapter 18 entry.** (i) "$\Tam_p(T)=\Fitt_{\Zl}(H^1(I_p,T)_{\mathrm{tors}})^{G_{\Q_p}}$" repeats the misplaced parenthesis of point 37. (ii) "the Tamagawa
  factor at an additive prime (what is known: it is at least 0; the paper does not compute it; Open question 3)" is superseded by 9.3 (N1).
  (iii) PLAN.md writes $V^*=\Hom(V,\Ql)$ for the linear dual while the paper and Chapter 16 use ${}^*$ for the Pontryagin dual (extends B4); this
  outline uses $V^\vee$ for the linear dual and keeps ${}^*$ for Pontryagin (C2), consistent with Chapters 14 and 16.
* **B-b. Chapter 21 outline.** A4.10 says $\Tam_p(T^D)=\Tam_p(A)$ is checked "in the multiplicative case" only; 7.5 here proves it in every case
  that occurs (with 9.3), and A4.10 can cite 7.5. A1.3 says nothing about additive primes; it can cite 9.3. A4.9's proof idea should cite
  Chapter 17, 10.3 and 10.4 here. Its A2.7 should cite 8.2 (with the $\varepsilon$ factor and the modulus $(n,q-1)$, as the Chapter 17 outline's B-c says).
* **B-c. Chapter 3 outline, line 106** ("$T^D$ ... the Cartier dual, Chapter 18"): the general definition is Chapter 17's 2.1, the adjoint-specific
  $T^D\simeq A(1)$ is 2.4 here (same as the Chapter 17 outline's B-a).
* **B-d. Chapter 16 outline, Exercise 10 (11a1 at $q=11$, $\ell=5$)** and 8.5 here use the same example; 8.5 cites it rather than repeating the
  computation. No conflict.
* **B-e. The paper's "$H^1_f(\Q_p,T^D)$ is the torsion of $H^1(\Q_p,T^D)$"** must not be simplified to "$H^1(\Q_p,T^D)$ is finite": the latter fails at
  $\mathrm I_0^*$ primes and at cyclic primes with $\chi(p)=1$ (3.3, 3.4). The Chapter 17 outline's 4.6 states it correctly; any later chapter should
  follow it.
* Consistency checks that passed: Chapter 4's 7.6 (Gram determinant $-2$), Chapter 7's 6.2 and 8.2, Chapter 10's 7.4 and 7.8 (unit parts of 11a1,
  539c1), Chapter 11's 3.2, 3.4, 8.5, 8.6, Chapter 14's 9.5, Chapter 16's model-computation, and Chapter 17's 4.4 to 4.6, 5.3, 5.4, 10.3, 10.4 agree with
  the line-up and with the recomputations of Part 6.6.
