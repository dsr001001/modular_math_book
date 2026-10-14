# Chapter 03: Modules and commutative algebra (`ch:modules`, `chapters/ch03_modules.tex`)

Stage 1 line-up. Part I (Algebra). Target length 2,165 lines of LaTeX (card excluded; see Part 3), inside the
1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the
Chapter 2 and 5 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference
(book and chapter or section; a theorem number only where sure, otherwise marked "check"); the paper's use by its
`\label` names, or "background". Every computation quoted below was checked by hand and by short Python/sympy scripts
in `/tmp/ch03` (verification log, Part 7).

## 0. What this chapter is for

The paper uses this chapter in nine places, and the chapter is built around them.

1. **Lengths and Fitting ideals over $\Zl$** (Section 1.2: $\Tam_p(M)=\Fitt_{\Zl}\bigl(H^1(I_p,M)_{\tors}^{G_{\Q_p}}\bigr)$;
   Lemma lem:tamfactor: the Fitting ideal of $(\Z/\ell^{v})\oplus(\Z/\ell^{m})$ is $\ell^{v+m}\Zl$; Lemma lem:fpr:
   $\Fitt_{\Zl}H^1_f(\Q_p,T^D)=L_p(A_f,1)^{-1}\Tam_p(T^D)$; Theorem thm:main, Theorem thm:dfg37, Remark rem:ns,
   Conjecture conj:euler: $\len_{\Zl}$ of Selmer groups and of $H^0$). The chapter proves that over a DVR the Fitting ideal
   of a finite-length module is $\varpi^{\mathrm{length}}$, that length is additive along exact sequences, and that
   Pontryagin duality preserves length.
2. **Pontryagin duality** (Lemma lem:dfg21: the duals $H^1_f(\Q_p,T^D)^*$ and $H^0(\Q,W^D)^*$; Lemma lem:h0 and
   Theorem thm:main: $W=\ad T\otimes\Qlmod$, $W^D=V^D/T^D$): duality for finite abelian groups and between finitely
   generated $\Zl$-modules and cofinitely generated discrete $\ell$-primary modules; the duality between $T$ and
   $T\otimes\Qlmod$; $W[\ell^k]=T/\ell^kT$.
3. **Saturated sublattices, perfect pairings, Gram determinants, alternating pairings, adjoints** (Lemma lem:ddt417:
   "the pairing identifies $L/L[\wp]^\perp$ with $\Hom(L[\wp],\mathcal O)$, because $L[\wp]$ is saturated", "$Q$ is the cokernel
   of $L[\wp]\to\Hom(L[\wp],\mathcal O)$, of order $\#\mathcal O/\Delta$"; Section 4.1: $\hat\delta_!$ perfect and alternating with all
   Hecke operators self-adjoint, "the Gram determinant of the pairing on $M_{f^\Sigma,\lambda}$ is $(\eta^\Sigma_{f,\lambda})^2$ up to a
   unit"; Lemma lem:hecke: $d=2$, $\Delta=(\eta^\emptyset)^2$).
4. **Congruence ideals as commutative algebra** (Lemma lem:crit: $I=\ker\phi_f$, $J=\Ann_\T(f^\perp)=\Ann_\T(I)$,
   "dualising the inclusion $\T\subset\T/I\times\T/J$, whose cokernel is $\T/(I+J)$", "embeds in $\Q f/\Z f$, so it is
   cyclic"; Lemma lem:ddt417: $\wp$, $I=\Ann_\T(\wp)$, $\eta=\pi(I)$, $L[\wp]$, $L[I]$, $\wp\cap I=0$, $L[\wp]^\perp=L[I]$, the
   equality case $L\simeq\T^d$). The chapter supplies every ingredient of Lemma lem:ddt417 and stops short of the
   lemma itself, which Chapter 20 proves.
5. **Finite free algebras over $\Zl$, their maximal ideals and idempotents** (Lemma lem:hecke: "$\mathfrak m$ the maximal
   ideal of $\T\otimes\Zl$ containing $\ell$ and $\ker\phi_f$", "the congruence ideal is computed in $\T_{\mathfrak m}$";
   Theorem thm:quant Step 1: "projecting $h$ to the $\mathfrak m$-component (an idempotent of $\T_\ell$, so the projection
   stays in the complement and the congruence survives)"; Remark rem:free: $\T_{\mathfrak m}$, $H^1(X_0(N),\Zl)_{\mathfrak m}$).
6. **Generalised eigenspaces, semisimple and non-semisimple operators, common eigenvectors** (Lemma lem:crit:
   $\T\otimes\Q=\Q\times\T'$; Lemma lem:old: "$U_p$ is not semisimple on this span when $0$ is a repeated eigenvalue, but each
   listed eigenvalue has an eigenvector", "for every choice of one such eigenvalue $\mu_p$ at each $p$ there is a common
   eigenform"; Theorem thm:twist: generalised eigenforms, $g^\perp$ as the sum of the other generalised eigenspaces;
   Theorem thm:quant Step 1: "the generalised eigenspace of $\pi$ ... is the line of $g^S$").
7. **Gorenstein algebras and freeness** (Remark rem:free: "the localised Hecke algebra is then Gorenstein and the Tate
   module is free of rank two"; the equality clauses of Lemma lem:ddt417, Lemma lem:hecke and Theorem thm:main).
8. **Modules over DVRs and $\Zl$** (Lemma lem:IV: "being torsion-free of $\Z_3$-rank $2$, $T$ is free of rank one over
   $\Z_3[\zeta_3]$"; Lemma lem:tamfactor: $H^1(I,M)=(\Zl/n')^2\oplus\Zl$ and its torsion; Lemma lem:crit: "the same statements
   hold with $\Z$ replaced by $\Zl$"; Lemma lem:dfg21: "$H^1(\R,T^D)$ is killed by $2$, so $H^1_f(\R,T^D)=0$ for $\ell$ odd").
9. **Foundations for Chapters 6, 7, 13, 14, 16, 17, 18, 20**: exact sequences and the snake lemma, $\Hom$ and $\otimes$,
   flatness, Noetherian rings, Nakayama, localisation, the DVR criterion, $\Zl$ as a complete DVR, the topology of finitely
   generated $\Zl$-modules, $\Qlmod$ injective.

Split with the neighbouring chapters (decided here, consistent with what their outlines assume):
* **Chapter 1** proves the structure theorem for finite abelian groups (its 4.1), $\#A[n]=\#A/nA$ (its 4.3), the
  $\ell$-primary decomposition (its 1.8) and constructs $\Zl=\varprojlim\Z/\ell^n$ as a profinite group (its 7.2). Chapter 3
  generalises the structure theorem to finitely generated modules over a PID (5.3), makes $\Zl$ a DVR (6.4), and proves
  Pontryagin duality for finite abelian groups (8.1), which Chapter 1's forward pointer assigns here.
* **Chapter 2** proves ideals, quotient rings, the two-ideal exact sequence and CRT (its 1.4), idempotents of a product of
  rings (its 1.5), prime and maximal ideals (its 2.1, 2.2), $\Z_{(p)}$ (its 2.4), PIDs and UFDs (its 3.2), $v_p$ (its 11.1),
  and defines $\Ann_R(S)$ (its 1.2). Chapter 3 uses these and does not reprove them; it gives the module version of the
  two-ideal sequence (2.2), localisation in general (4.5), the existence of maximal ideals in Noetherian rings (4.1, which
  Chapter 2's item 2.1(v) defers here), and the lifting of idempotents for finite algebras over a complete DVR (10.3,
  which Chapter 2's item 1.5 defers here).
* **Chapter 4** (outlined in parallel) does representations of groups: subrepresentations, irreducibility, Schur, Maschke,
  semisimple *modules over group algebras*, Brauer-Nesbitt, $G$-stable lattices in $\Ql$-representations, reduction mod
  $\ell$, homothety of lattices and Ribet's lemma. Chapter 3 does modules over *commutative* rings, lattices as
  finitely generated free $\mathcal O$-modules (saturation, index, elementary divisors, Gram determinants) with no group
  action, and semisimplicity of a single operator or a commuting family (10.7), not of representations. The
  Jordan-Holder theorem is needed here first (for length over a local ring, 7.1); Chapter 3 proves it for modules over a
  ring (the proof does not use commutativity), and Chapter 4 should cite `\Cref{ch:modules}` for it and add only the
  reading for $k[G]$-modules (composition factors of representations). If Chapter 4's outline also proves it, the
  writers keep one proof (Part 6, coordination note).
* **Chapter 6** uses the DVR criterion (6.1), torsion-free modules over a DVR are free (6.3), localisation (4.5), Noetherian
  rings (4.1), $\Zl$ (6.4) and "$R\otimes\Zl$ is the product of its localisations at the maximal ideals above $\ell$" (10.4).
  Chapter 3 does not treat $\Z_3[\zeta_3]$, $\Z_\ell[\zeta_3]$ or $\mathcal O_\lambda$ beyond naming them as examples.
* **Chapter 7** does $\Q_p$ as an analytic completion (absolute values, Cauchy sequences, Hensel's lemma, the structure of
  $\Z_p^\times$ and $\Q_p^\times$, finite extensions). Chapter 3 does $\Zl$ algebraically: as $\varprojlim\Z/\ell^n$ and as the
  $\ell$-adic completion of $\Z$, a complete DVR; $\Ql=\Zl[1/\ell]$; $\Qlmod$; the $\ell$-adic topology of finitely generated
  $\Zl$-modules. Idempotent lifting (10.3) is proved by a Newton iteration that needs only completeness, not Hensel.
* **Chapter 16** proves complexes, long exact sequences, Ext and Tor, group cohomology, and the length identity of
  Lemma lem:dfg21 in its own item lengths-in-exact-sequences. Chapter 3 proves the snake lemma (Chapter 16 recalls it),
  additivity of length (7.1), Fitting ideals (7.4 to 7.7), Pontryagin duality of modules (8.1 to 8.3), closedness of
  submodules and topological Nakayama (6.6), $\Qlmod$ injective (6.5).
* **Chapters 13, 14** prove the perfect pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$, the freeness of $\T$ over $\Z$, the
  Hecke-equivariance of the cup product and of $w_N$, multiplicity one and the Gorenstein property of $\T_{\mathfrak m}$
  (Mazur, Tilouine, Ribet-Stein). Chapter 3 supplies the abstract algebra those statements are about: 9.6 (an algebra
  paired perfectly with a module), 9.5 (adjoints, twisted pairings), 11.4 (Gorenstein), 11.5 (Mazur's freeness criterion).
* **Chapter 18** defines $\Tam_p$ (its item 7.1) and proves Lemma lem:fpr (its items 7.4, 7.5) and Lemma lem:tamfactor (its item 8.2); **Chapter 20** proves Lemma lem:ddt417, Lemma lem:hecke and the
  assembly. Chapter 3 gives the Fitting ideal and every ingredient of Lemma lem:ddt417 (11.1, 11.3, 9.3, 9.4) and
  checks the statement on toy algebras (11.6), but does not prove the lemma.

## 1. Global conventions fixed in this chapter

* **C1 (rings and modules).** As Chapter 2, C1: rings are commutative with $1$, homomorphisms preserve $1$, modules are
  unital. $R$ is a ring, $M,N$ are $R$-modules. An $R$-algebra is a ring $A$ with a ring homomorphism $R\to A$. The paper's
  $\T$ is a commutative ring; its modules $S_2(\Gamma_0(N);\Z)$, $H^1(X_0(N),\Zl)$, $L$ are modules over a commutative ring.
* **C2 (DVR notation).** $\mathcal O$ is a discrete valuation ring with uniformiser $\varpi$, residue field $k=\mathcal O/\varpi\mathcal O$,
  fraction field $K$, and valuation $v\colon K^\times\to\Z$ normalised by $v(\varpi)=1$, $v(0)=+\infty$. For an ideal $\mathfrak a=a\mathcal O$
  put $v(\mathfrak a)=v(a)$. For $\mathcal O=\Zl$: $\varpi=\ell$, $k=\Fl$, $v=v_\ell$ (Chapter 2, C3). The paper writes $\mathcal O$ and $\lambda$,
  $v_\lambda$; for rational newforms $\mathcal O=\Zl$ and $\lambda=\ell$.
* **C3 (torsion and duals; three different duals).** For an ideal $\mathfrak a\subset R$, $M[\mathfrak a]=\{m\in M:\mathfrak am=0\}$ (the
  paper's $L[\wp]$, $L[I]$); $M[x]=M[xR]$; $M[\ell^k]$, $M[\ell^\infty]=\bigcup_kM[\ell^k]$; $M_{\tors}$ the torsion submodule over a
  domain. **Three duals, never confused:** $M^\vee=\Hom_R(M,R)$ (the linear dual; the paper's $\Hom(L[\wp],\mathcal O)$);
  $M^*=\Hom(M,\Q/\Z)$, or $\Hom_{\Zl}(M,\Qlmod)$ for $\ell$-primary or $\Zl$-modules (the Pontryagin dual; the paper's
  ${}^*$ in Lemma lem:dfg21); $T^D=\Hom(T,\Zl(1))$ (the Cartier dual, Chapters 17 and 18; not used here).
* **C4 (lattices).** Over a PID $R$ with fraction field $K$: a *lattice* is a finitely generated free $R$-module; a lattice in a
  finite-dimensional $K$-vector space $V$ is a finitely generated $R$-submodule spanning $V$ (free of rank $\dim V$).
  $L'\subset L$ is *saturated* if $L/L'$ is torsion-free (5.5). $G$-stable lattices and homothety are Chapter 4.
* **C5 (pairings).** A pairing is an $R$-bilinear map $\langle\ ,\ \rangle\colon L\times M\to R$. Gram matrix $G=(\langle e_i,f_j\rangle)$ for bases
  $(e_i)$, $(f_j)$. For $S\subset M$: $S^\perp=\{x\in L:\langle x,S\rangle=0\}$; for $S\subset L$: ${}^\perp S$ or, when $L=M$ and the pairing is
  symmetric or antisymmetric, $S^\perp$. A pairing $L\times L\to R$ is *alternating* if $\langle x,x\rangle=0$ for all $x$. "Self-adjoint"
  for an endomorphism $t$: $\langle tx,y\rangle=\langle x,ty\rangle$.
* **C6 (length and orders).** $\len_R(M)$ is the length (7.1); "length" without subscript means $\len_{\Zl}$, as in PLAN.md
  Appendix B. "$\#\mathcal O/\Delta$" (the paper's notation) means $\#k^{v(\Delta)}$ and needs $k$ finite; for a general DVR the book
  writes $\len_{\mathcal O}(\mathcal O/\Delta\mathcal O)=v(\Delta)$.
* **C7 (localisation versus factor; the paper's $\T_{\mathfrak m}$).** For a finite free $\Z$-algebra $\T$ and a maximal ideal
  $\mathfrak m\ni\ell$, $\T_{\mathfrak m}$ **always** means $(\T\otimes\Zl)_{\mathfrak m}$, the direct factor of $\T\otimes\Zl$ cut out by an idempotent
  (10.3, 10.4); it is also the $\mathfrak m$-adic completion of $\T$. The algebraic localisation of $\T$ itself is written $\T_{(\mathfrak m)}$ and
  is not complete. Likewise $L_{\mathfrak m}=e_{\mathfrak m}(L\otimes\Zl)$ for a $\T$-module $L$. This is the paper's usage (Lemma lem:hecke,
  Remark rem:free, Theorem thm:quant).
* **C8 (matrices).** Relations are rows: a presentation $R^m\xrightarrow{A}R^n\to M\to0$ means $M=R^n/(\text{row space of }A)$ with
  $A\in\Mat_{m\times n}(R)$; Fitting ideals use the $n\times n$ minors of $A$ (7.4).
* **C9 (Frobenius).** This chapter contains no Frobenius; its examples quoting Lemma lem:tamfactor use the arithmetic
  convention of Chapter 16 and say so. (important_notes.md point 11 is not this chapter's business.)
* **C10 (typography and labels).** PLAN.md Section 7.2: no dash ligatures, ASCII source, labels `...:modules:...`; the paper's
  macros `\Fitt`, `\len`, `\Tam`, `\ad`, and the preamble's `\Hom`, `\End`, `\Ann`, `\coker`, `\rank`, `\tors`, `\Zl`, `\Ql`,
  `\Qlmod`, `\Ext` (only in remarks). The paper's $\wp$ is `\wp`.

## 2. Line-up of the core results, in teaching order

### Section 1. Modules, submodules, quotients, homomorphisms

**1.1 `def:modules:module`** (definition and proposition; P). An $R$-module; submodules; the submodule $\sum Rm_i$
generated by a family; finitely generated (f.g.) and cyclic modules; quotient modules $M/N$; homomorphisms, kernel,
image, cokernel $\coker f=N/f(M)$; $\Hom_R(M,N)$ is an $R$-module; $\End_R(M)$ is a (non-commutative in general) ring. A
cyclic module $Rm$ is isomorphic to $R/\Ann_R(m)$. Examples: $\Z$-modules are abelian groups; $K$-modules are vector
spaces; a $K[x]$-module is a $K$-vector space with one endomorphism (the dictionary used in 10.5 to 10.8); an
$R/\mathfrak a$-module is an $R$-module killed by $\mathfrak a$; an ideal is a submodule of $R$. Reference: Dummit-Foote (DF) 10.1 to
10.3; Atiyah-Macdonald (AM) Chapter 2. Paper: background.

**1.2 `def:modules:algebra-modules`** (definition and examples; P). For a ring homomorphism $\phi\colon R\to S$ every
$S$-module is an $R$-module (restriction of scalars); an $R$-algebra $A$ acting on an $R$-module $M$ is a homomorphism of
$R$-algebras $A\to\End_R(M)$; the action is *faithful* if this map is injective. A module over $R_1\times R_2$ is the same
as a pair $(M_1,M_2)$, $M=e_1M\oplus e_2M$ for the idempotents $e_1=(1,0)$, $e_2=(0,1)$ (Chapter 2, item 1.5). Running
examples, stated with forward pointers: (a) $\T\subset\End_\Z S_2(\Gamma_0(N);\Z)$ acting faithfully (Chapters 12, 13);
(b) $\T$ acting on $H^1(X_0(N),\Zl)$ (Chapter 14); (c) $T=T_3E$ with $\sigma$ of order $3$, $\det\sigma=1$: a module over
$\Z_3[X]/(X^2+X+1)=\Z_3[\zeta_3]$ (Lemma lem:IV; Chapter 6, item 4.8); (d) the toy algebras of 11.2. Reference: DF 10.1;
AM Chapter 2. Paper: Lemma lem:IV, Lemma lem:crit, Lemma lem:ddt417 ("a commutative $\mathcal O$-algebra ... acting on an
$\mathcal O$-module $L$").

**1.3 `thm:modules:isomorphism`** (theorem; P). (i) $M/\ker f\simeq f(M)$. (ii) For submodules $A,B\subset M$:
$(A+B)/B\simeq A/(A\cap B)$. (iii) For $B\subset A\subset M$: $(M/B)/(A/B)\simeq M/A$, and submodules of $M/B$ correspond to
submodules of $M$ containing $B$. (iv) If $f\colon M\to N$ is surjective with kernel $K_0$ and $A\subset M$, then $f$ induces
$M/(K_0+A)\simeq N/f(A)$ (the module form of Chapter 2, item 1.3(iii)). Reference: DF 10.2. Paper: Lemma lem:crit
("$\T/(I+J)\simeq\Z/\phi_f(J)$"), the congruence module $\T/(\wp+I)\simeq\mathcal O/\eta$ of 11.1.

### Section 2. Exact sequences, the snake lemma, direct sums and products, free and projective modules

**2.1 `def:modules:exact`** (definition and proposition; P). A sequence $\cdots\to M_{i-1}\xrightarrow{f_{i-1}}M_i\xrightarrow{f_i}M_{i+1}\to\cdots$ is
exact at $M_i$ if $\ker f_i=\im f_{i-1}$; short exact sequences $0\to M'\to M\to M''\to0$. *Splitting lemma:* for a short exact
sequence the following are equivalent: (a) there is $s\colon M''\to M$ with $ps=\id$; (b) there is $r\colon M\to M'$ with $ri=\id$;
(c) there is an isomorphism $M\simeq M'\oplus M''$ compatible with $i$ and $p$. Examples: $0\to\Z\xrightarrow{n}\Z\to\Z/n\to0$ does not
split for $n\ge2$; $0\to\Zl\xrightarrow{\ell^k}\Zl\to\Z/\ell^k\to0$; $0\to T\to V\to W\to0$ for $V=T\otimes\Ql$, $W=T\otimes\Qlmod$ does not split
when $T\ne0$ ($V$ has no nonzero torsion). Reference: DF 10.5; AM Chapter 2. Paper: Lemma lem:dfg21 (a four-term exact
sequence), background.

**2.2 `prop:modules:two-submodules`** (proposition; P). For submodules $A,B$ of $M$ the sequence
$$0\to M/(A\cap B)\xrightarrow{\ x\mapsto(x,x)\ }M/A\oplus M/B\xrightarrow{\ (y,z)\mapsto y-z\ }M/(A+B)\to0$$
is exact. If $A\cap B=0$ then $M\hookrightarrow M/A\oplus M/B$ with cokernel $M/(A+B)$; the sum $A+B$ is direct iff $A\cap B=0$.
(Module form of Chapter 2, item 1.4.) Reference: elementary. Paper: Lemma lem:crit ("the inclusion $\T\subset\T/I\times\T/J$,
whose cokernel is $\T/(I+J)$", with $I\cap J=0$), Lemma lem:ddt417 ("the sum $L[\wp]+L[I]$ is direct").

**2.3 `lem:modules:snake`** (lemma, the snake lemma; P). Given a commutative diagram with exact rows
$M'\xrightarrow{i}M\xrightarrow{p}M''\to0$ and $0\to N'\xrightarrow{j}N\xrightarrow{q}N''$ and vertical maps $f',f,f''$, there is an $R$-linear
$\delta\colon\ker f''\to\coker f'$, defined by: lift $x''\in\ker f''$ to $x\in M$; then $q(f(x))=0$, so $f(x)=j(y')$ for a unique
$y'\in N'$; put $\delta(x'')=[y']$. It is well defined, and
$\ker f'\to\ker f\to\ker f''\xrightarrow{\delta}\coker f'\to\coker f\to\coker f''$ is exact; it begins with $0\to$ if $i$ is
injective and ends with $\to0$ if $q$ is surjective. Corollaries (P): (a) for a short exact sequence $0\to A\to B\to C\to0$ and
$n\in R$, the multiplication-by-$n$ maps give an exact sequence $0\to A[n]\to B[n]\to C[n]\to A/nA\to B/nB\to C/nC\to0$;
(b) for an endomorphism $\phi$ of a finite abelian group, $\#\ker\phi=\#\coker\phi$ (compare Chapter 1, item 4.3).
Reference: AM Chapter 2 (check the proposition number); Weibel, Lemma 1.3.2 (as Chapter 16 cites it). Paper:
background (Chapter 16 recalls it and builds every connecting map on it; Lemma lem:h0 and the sequence $0\to T\to V\to W\to0$
in Chapters 16, 17).

**2.4 `lem:modules:five`** (lemma, the five lemma; P). In a commutative ladder of two exact rows of five modules, if the
four outer vertical maps are isomorphisms, so is the middle one (the two halves: injectivity from the second and fourth
being injective and the first surjective; surjectivity dually). Reference: Weibel 1.3; DF 10.5 (exercise). Paper:
background (comparisons of long exact sequences in Chapters 16, 17).

**2.5 `def:modules:sums-products`** (definition and proposition; P). External and internal direct sums $\bigoplus_iM_i$ and
direct products $\prod_iM_i$, with their universal properties; finite sums equal finite products;
$\Hom_R(\bigoplus_iM_i,N)=\prod_i\Hom_R(M_i,N)$ and $\Hom_R(N,\prod_iM_i)=\prod_i\Hom_R(N,M_i)$. $M=A\oplus B$ internally iff $A+B=M$ and
$A\cap B=0$ iff there is an idempotent $e\in\End_R(M)$ with $eM=A$, $(1-e)M=B$. Reference: DF 10.3; AM Chapter 2. Paper:
Lemma lem:ddt417 ($L[\wp]\oplus L[I]$), Lemma lem:hecke ($H^1\otimes\Zl=\bigoplus_{\mathfrak m'}H^1_{\mathfrak m'}$).

**2.6 `def:modules:free`** (definition and proposition; P). A basis; free modules $R^{(I)}$ and their universal property;
every module is a quotient of a free module, so has a presentation $F_1\to F_0\to M\to0$ with $F_0,F_1$ free; $M$ is
*finitely presented* if $F_0,F_1$ can be taken of finite rank. Rank is well defined: if $R\ne0$ and $R^m\simeq R^n$ then $m=n$
(tensor with $R/\mathfrak m$ for a maximal ideal $\mathfrak m$, which exists by 4.1 for Noetherian $R$ and by Zorn's lemma in general,
Chapter 2, item 2.1(v)). A matrix $A\in\Mat_n(R)$ is invertible iff $\det A\in R^\times$ (adjugate). Reference: DF 10.3; AM Chapter 2.
Paper: background (presentations for Fitting ideals, 7.4).

**2.7 `def:modules:projective`** (definition and proposition; P). For an $R$-module $P$ the following are equivalent: (a) every
surjection $M\to P$ splits; (b) $P$ is a direct summand of a free module; (c) $\Hom_R(P,-)$ is exact; (d) every map from $P$ lifts
along every surjection. Such $P$ is *projective*. Examples: free modules; $eR$ for an idempotent $e$ (so each factor $R_i$ of
$R=\prod R_i$ is a projective $R$-module); $\Z/2$ over $\Z/6\simeq\Z/2\times\Z/3$ is projective and not free. Over a local ring a
finitely generated projective module is free (4.3(v)); over a PID every submodule of a free module is free (5.1).
Consequence used later: if $\T$ is finite free over $\Zl$ and $e\in\T$ is idempotent, $e\T$ is projective, hence free, over $\Zl$.
Reference: DF 10.5; Weibel 2.2. Paper: Lemma lem:hecke ("Apply Lemma lem:ddt417 to $\mathcal O=\Zl$, $\T_{\mathfrak m}$": $\T_{\mathfrak m}$ is a finite
free $\Zl$-algebra), Remark rem:free.

### Section 3. Hom and tensor product; flatness

**3.1 `prop:modules:hom`** (proposition; P). (i) $\Hom_R(R,M)=M$; $\Hom_R(R^n,M)=M^n$; $\Hom_R(R/\mathfrak a,M)=M[\mathfrak a]$. (ii) $\Hom_R(-,N)$ and
$\Hom_R(N,-)$ are left exact: $0\to M'\to M\to M''$ exact gives $0\to\Hom(N,M')\to\Hom(N,M)\to\Hom(N,M'')$ exact, and
$M'\to M\to M''\to0$ exact gives $0\to\Hom(M'',N)\to\Hom(M,N)\to\Hom(M',N)$ exact. (iii) They are not right exact:
$\Hom_\Z(\Z/2,-)$ applied to $0\to\Z\xrightarrow2\Z\to\Z/2\to0$, and $\Hom_\Z(-,\Z)$ applied to the same sequence. (iv) The
linear dual $M^\vee=\Hom_R(M,R)$; for $M$ free with basis $(e_i)_{i\le n}$ the dual basis $(e_i^\vee)$; $M\to M^{\vee\vee}$ is an isomorphism for
f.g. free $M$; over a domain $M^\vee$ is torsion-free for every $M$. Reference: DF 10.5; AM Chapter 2. Paper: Lemma lem:ddt417
($\Hom(L[\wp],\mathcal O)$), Lemma lem:crit (dualising), Lemma lem:dfg21 (duals; Pontryagin version in Section 8).

**3.2 `thm:modules:tensor`** (theorem; P). (i) The tensor product $M\otimes_RN$ exists and is unique up to unique isomorphism,
with the universal property for $R$-bilinear maps; construction as a quotient of the free module on $M\times N$. (ii)
$R\otimes M=M$; $(\bigoplus M_i)\otimes N=\bigoplus(M_i\otimes N)$; $R^m\otimes R^n=R^{mn}$; $(R/\mathfrak a)\otimes M=M/\mathfrak aM$; commutativity
and associativity. (iii) Adjunction: $\Hom_R(M\otimes N,P)\simeq\Hom_R(M,\Hom_R(N,P))$. (iv) Base change: for an $R$-algebra $S$,
$S\otimes_RM$ is an $S$-module, $S\otimes_RR^n=S^n$, and $S\otimes_R(R/\mathfrak a)=S/\mathfrak aS$; the tensor product of two $R$-algebras is an
$R$-algebra. (v) Examples (checked): $\Z/m\otimes\Z/n\simeq\Z/\gcd(m,n)$; $\Q\otimes_\Z\Z/n=0$; $\Zl\otimes_\Z\Z/n\simeq\Z/\ell^{v_\ell(n)}$;
$\Qlmod\otimes_\Z A=0$ for every torsion abelian group $A$ (a divisible group tensored with a torsion group);
$\Qlmod\otimes\Qlmod=0$. Reference: DF 10.4; AM Chapter 2. Paper: $T\otimes\Qlmod$ (Theorem thm:main, Lemma lem:h0),
$\T\otimes\Zl$, $\T\otimes\Q$ (Lemmas lem:crit, lem:hecke, Theorem thm:quant).

**3.3 `prop:modules:right-exact`** (proposition; P). $-\otimes_RN$ is right exact: $M'\to M\to M''\to0$ exact gives
$M'\otimes N\to M\otimes N\to M''\otimes N\to0$ exact (via 3.1(ii) and the adjunction 3.2(iii)). It is not left exact:
$0\to\Z\xrightarrow2\Z$ tensored with $\Z/2$. $N$ is *flat* if $-\otimes_RN$ is exact. Free and projective modules are flat.
Reference: DF 10.5; AM Chapter 2. Paper: background.

**3.4 `prop:modules:flat`** (proposition; P, except (ii) in full generality, S). (i) For a multiplicative set $S$, $S^{-1}R$ is a
flat $R$-module (proof after 4.5: $S^{-1}R\otimes M\simeq S^{-1}M$ and localisation is exact). (ii) Over a PID a module is flat iff it is
torsion-free (P for finitely generated modules, by 5.3; the general case S, since tensor products commute with directed
unions and every f.g. submodule of a torsion-free module is free). Hence $\Q$, $\Z_{(\ell)}$, $\Zl$, $\Ql$ are flat over $\Z$, and $\Ql$ is
flat over $\Zl$. (iii) Consequences, for $R\to S$ flat (P): kernels, images, cokernels, finite intersections of submodules
commute with $S\otimes_R-$; for an ideal $\mathfrak a$ generated by $a_1,\dots,a_k$, $(M[\mathfrak a])\otimes_RS=(M\otimes_RS)[\mathfrak aS]$ (kernel of $M\to M^k$);
for a f.g. module $M$ with generators $m_1,\dots,m_n$, $\Ann_S(M\otimes_RS)=\Ann_R(M)S$ (kernel of $R\to M^n$); for $L'\subset L$ free over a
PID and $S$ a flat PID over it, the saturation commutes with base change. Reference: AM Chapters 2, 3; DF 10.5.
Paper: Lemma lem:crit ("the same statements hold with $\Z$ replaced by $\Zl$"; "the pairing being perfect after
tensoring with $\Zl$"), Lemma lem:hecke ("$r_E\Zl$ is the congruence ideal $\phi_f(\Ann_\T\ker\phi_f)\Zl$": $\Ann$ commutes with
$\otimes\Zl$), Theorem thm:quant Step 1 ($\Zl$-version of Lemma lem:crit).

### Section 4. Noetherian rings, Nakayama's lemma, localisation, local rings

**4.1 `prop:modules:noetherian`** (definition and proposition; P, except (iv), R). (i) For an $R$-module $M$ the following are
equivalent: every ascending chain of submodules stabilises; every nonempty set of submodules has a maximal element;
every submodule is f.g. Such $M$ is *Noetherian*; $R$ is Noetherian if it is as an $R$-module. (ii) Submodules, quotients and
extensions of Noetherian modules are Noetherian; over a Noetherian ring every f.g. module is Noetherian, so submodules
of f.g. modules are f.g. and f.g. modules are finitely presented. (iii) A nonzero Noetherian ring has a maximal ideal,
and every proper ideal lies in one (maximal element of the set of proper ideals containing it); this is the proof
promised in Chapter 2, item 2.1(v). (iv) Hilbert's basis theorem: $R$ Noetherian implies $R[x]$ Noetherian (stated). (v)
Examples: fields, PIDs (Chapter 2, item 3.2), $\Zl$, every ring that is f.g. as a module over a Noetherian ring (the
Hecke algebra $\T$ over $\Z$, $\T\otimes\Zl$ over $\Zl$). Reference: AM Chapters 6, 7 (Hilbert: Theorem 7.5, check); DF 12.1, 15.1.
Paper: background ($\T$, $\T_{\mathfrak m}$, $H^1(X_0(N),\Zl)$ are f.g. over Noetherian rings).

**4.2 `lem:modules:determinant-trick`** (lemma; P). Let $M$ be generated by $n$ elements, $\mathfrak a\subset R$ an ideal and
$\phi\in\End_R(M)$ with $\phi(M)\subset\mathfrak aM$. Then $\phi^n+a_1\phi^{n-1}+\dots+a_n=0$ with $a_i\in\mathfrak a^i$ (Cayley-Hamilton applied to a
matrix of $\phi$ with entries in $\mathfrak a$; adjugate argument over the commutative ring $R[\phi]$). Corollaries: (a) if $M$ is f.g. and
$\mathfrak aM=M$, there is $x\equiv1\pmod{\mathfrak a}$ with $xM=0$; (b) a surjective endomorphism of a f.g. module is an isomorphism.
Reference: AM Proposition 2.4 (check the number) and Chapter 2. Paper: background (proof of 4.3; 11.5).

**4.3 `thm:modules:nakayama`** (theorem, Nakayama's lemma; P). Let $(R,\mathfrak m,k)$ be a local ring (4.4) and $M$ a f.g. $R$-module.
(i) If $\mathfrak mM=M$ then $M=0$ (more generally for any ideal inside the Jacobson radical). (ii) If $N\subset M$ and $N+\mathfrak mM=M$, then
$N=M$. (iii) $x_1,\dots,x_r$ generate $M$ iff their images span the $k$-vector space $M/\mathfrak mM$; the minimal number of generators of
$M$ is $\dim_kM/\mathfrak mM$. (iv) A homomorphism $f\colon M\to N$ of f.g. modules with $N$ f.g. is surjective iff $f\otimes k$ is; a matrix in
$\Mat_n(R)$ is invertible iff its reduction mod $\mathfrak m$ is; an endomorphism of $R^n$ is an automorphism iff it is so mod $\mathfrak m$. (v) A
f.g. projective $R$-module is free. Example: over $\Zl$, a f.g. module $M$ with $M/\ell M\simeq\Fl^2$ is generated by two elements; an
endomorphism of $(\Z/\ell^k)^n$ that is invertible mod $\ell$ is invertible. Reference: AM Proposition 2.6, Corollaries 2.7,
2.8 (check); Eisenbud Chapter 4. Paper: Remark rem:free ("$J_0(N)[\mathfrak m]$ is two-dimensional" gives two generators,
through 11.5; Chapter 14), Lemma lem:h0 in the corrected form of important_notes.md point 5 (a lift of an
element of exact order $\ell^k$ is an isomorphism $\rho\bmod\ell^k\to(\rho\otimes\chi_\ell)\bmod\ell^k$ because it is one mod $\ell$), Chapter 16
(topological Nakayama, 6.6).

**4.4 `def:modules:local-ring`** (definition and proposition; P). A ring is *local* if it has exactly one maximal ideal.
$R$ is local iff its non-units form an ideal; then $R^\times=R\setminus\mathfrak m$. The Jacobson radical (intersection of the maximal ideals);
$1+x$ is a unit for $x$ in it. Examples: fields; $\Z_{(p)}$ (Chapter 2, item 2.4); DVRs (6.1); $\Z/p^n$; $k[\varepsilon]/(\varepsilon^2)$;
$\Zl[x]/(x^2)$; each factor $\T_{\mathfrak m}$ of a finite free $\Zl$-algebra (10.3). Non-examples: $\Z$; $\Zl\times\Zl$;
$\Z_{(11)}[x]/(x^2+x-1)$ (two maximal ideals, 10.3). Reference: AM Chapter 1. Paper: Lemma lem:hecke, Remark rem:free,
Theorem thm:quant ($\T_{\mathfrak m}$ local).

**4.5 `thm:modules:localisation`** (definition and theorem; P). For a multiplicative set $S\subset R$: the ring $S^{-1}R$ and the
module $S^{-1}M$ (fractions $m/s$, with $m/s=m'/s'$ iff $u(s'm-sm')=0$ for some $u\in S$). (i) Universal property: $R\to S^{-1}R$ is
initial among homomorphisms inverting $S$. (ii) $S^{-1}M\simeq S^{-1}R\otimes_RM$, and $M\mapsto S^{-1}M$ is exact (hence 3.4(i)). (iii)
Ideals: $\mathfrak b\mapsto\mathfrak b\cap R$ and $\mathfrak a\mapsto S^{-1}\mathfrak a$ give a bijection between prime ideals of $S^{-1}R$ and prime ideals of $R$ not
meeting $S$. (iv) For a prime $\mathfrak p$, $R_{\mathfrak p}=(R\setminus\mathfrak p)^{-1}R$ is local with maximal ideal $\mathfrak pR_{\mathfrak p}$; $M_{\mathfrak p}$. (v) Local
nature: $M=0$ iff $M_{\mathfrak m}=0$ for every maximal $\mathfrak m$; a map is injective (surjective) iff it is so after localising at every
maximal ideal. (vi) Localisation commutes with finite direct sums, quotients, $\Ann$ of f.g. modules (3.4(iii)) and $\Hom$
out of finitely presented modules (stated). (vii) Examples: $\Z_{(p)}$; $\Q=\Z_{(0)}$; $\Z[1/\ell]$; $(\Z/n)_{(p)}\simeq\Z/p^{v_p(n)}$; for
$R=R_1\times R_2$ and $\mathfrak p=\mathfrak p_1\times R_2$, $R_{\mathfrak p}\simeq(R_1)_{\mathfrak p_1}$ (localisation at a maximal ideal of a product picks out a
factor; this is why, for a finite algebra over a complete DVR, localisation at $\mathfrak m$ is a direct factor, 10.3). Reference: AM
Chapter 3; DF 15.4. Paper: Lemma lem:hecke, Remark rem:free, Theorem thm:quant ($\T_{\mathfrak m}$, $H^1(X_0(N),\Zl)_{\mathfrak m}$; with
convention C7).

### Section 5. Finitely generated modules over a PID; torsion; lattices and saturation

**5.1 `thm:modules:submodule-free`** (theorem; P). Let $R$ be a PID. A submodule of a free $R$-module of rank $n$ is free of rank at
most $n$ (induction on $n$, projecting to the last coordinate, whose image is a principal ideal). Corollaries: over a PID,
f.g. modules are finitely presented; f.g. projective modules are free. Reference: DF 12.1. Paper: background (5.3, 5.5).

**5.2 `thm:modules:smith`** (theorem, Smith normal form; P for Euclidean domains, which covers $\Z$, $F[x]$ and every DVR; S for a
general PID). For $A\in\Mat_{m\times n}(R)$ there are $U\in\GL_m(R)$, $V\in\GL_n(R)$ with $UAV=\operatorname{diag}(d_1,\dots,d_s,0,\dots)$, $d_i\ne0$,
$d_1\mid d_2\mid\cdots\mid d_s$. For each $k$, $d_1\cdots d_k$ generates the ideal of $k\times k$ minors of $A$ (the $k$-th determinantal
divisor, unchanged by invertible row and column operations), so the $d_i$ are unique up to units. Examples (checked):
$\begin{psmallmatrix}2&4\\6&8\end{psmallmatrix}\sim\operatorname{diag}(2,4)$; the relation matrix with rows $(2,4,4)$, $(-6,6,12)$, $(10,-4,-16)$ (DF 12.1)
$\sim\operatorname{diag}(2,6,12)$; $\begin{psmallmatrix}3&6\\9&3\end{psmallmatrix}\sim\operatorname{diag}(3,15)$ over $\Z$, $\sim\operatorname{diag}(3,3)$ over $\Z_3$. Reference: DF 12.1 (exercises), Lang
III.7; Jacobson, Basic Algebra I, 3.7 (not in refs.bib; add to `bib/ch03.bib` if cited). Paper: background (5.3, 5.6, 7.6).

**5.3 `thm:modules:structure-pid`** (theorem, structure of f.g. modules over a PID; P). Let $R$ be a PID and $M$ a f.g.
$R$-module. (i) (Invariant factors.) $M\simeq R^r\oplus R/(d_1)\oplus\cdots\oplus R/(d_s)$ with $d_i$ nonzero non-units and $d_1\mid\cdots\mid d_s$; $r$ and the
ideals $(d_i)$ are uniquely determined. (ii) (Elementary divisors.) $M\simeq R^r\oplus\bigoplus_jR/(p_j^{a_j})$ with $p_j$ primes, $a_j\ge1$; the
multiset of the ideals $(p_j^{a_j})$ is uniquely determined. (iii) Proof: existence from a presentation and 5.2; uniqueness:
$r=\dim_K(M\otimes K)$, and for each prime $p$ the numbers $\dim_{R/p}(p^{k}M_{\tors}/p^{k+1}M_{\tors})$ determine the $p$-primary part.
(iv) Special cases: $R=\Z$ gives f.g. abelian groups and recovers Chapter 1, item 4.1; $R=\mathcal O$ a DVR gives
$M\simeq\mathcal O^r\oplus\bigoplus_i\mathcal O/\varpi^{a_i}$ (6.3); $R=K[x]$ gives the rational canonical form and, over an algebraically closed field,
the Jordan form (used in 10.7). (v) Example: the module of the second example in 5.2 is $\Z/2\oplus\Z/6\oplus\Z/12$, with
elementary divisors $2,2,3,4,3$, that is $\Z/2\oplus\Z/2\oplus\Z/4\oplus\Z/3\oplus\Z/3$. Reference: DF 12.1, Theorems 5 and 6 (check); Lang III.7.
Paper: Lemma lem:tamfactor ($H^1(I,M)=(\Zl/n')\bar e\oplus(\Zl/n')\bar h\oplus\Zl\bar f$, torsion $(\Z/\ell^{v_\ell(n)})^2$), Lemma lem:IV.

**5.4 `def:modules:torsion`** (definition and proposition; P). Over a domain $R$ with fraction field $K$: torsion elements,
the torsion submodule $M_{\tors}$, torsion-free modules, $\rank M=\dim_K(M\otimes_RK)$. (i) $M/M_{\tors}$ is torsion-free; $M_{\tors}$ is the
kernel of $M\to M\otimes K$. (ii) Over a PID, a f.g. torsion-free module is free, and $M\simeq M_{\tors}\oplus M/M_{\tors}$ (the splitting is not
canonical). (iii) If $R\subset R'$ is an extension of domains with $R'$ a PID finite free of rank $e$ over $R$ (example
$\Z_3\subset\Z_3[\zeta_3]$, $e=2$), a f.g. $R'$-module that is torsion-free over $R$ of $R$-rank $n$ is free over $R'$ of rank $n/e$.
Reference: DF 12.1. Paper: Lemma lem:IV ("Being torsion-free of $\Z_3$-rank $2$, $T$ is free of rank one over $\Z_3[\zeta_3]$"; Chapter
6, item 4.8, cites (iii)), Lemma lem:tamfactor ("its torsion is $(\Z/\ell^{v_\ell(n)})^2$"), the paragraph after Lemma lem:dfg21
("the torsion of $H^1(\Q_p,T^D)$, a finite group").

**5.5 `def:modules:saturated`** (definition and proposition; P). Let $R$ be a PID with fraction field $K$, $M$ a lattice (C4) and
$L\subset M$ a submodule. $L$ is *saturated* if $M/L$ is torsion-free. Equivalent: (a) $L$ saturated; (b) $L=M\cap(K L)$ inside
$M\otimes K$; (c) $L$ is a direct summand of $M$; (d) (for $R=\mathcal O$ a DVR) $L\cap\varpi M=\varpi L$, i.e. $L/\varpi L\to M/\varpi M$ is injective.
The *saturation* $\operatorname{sat}(L)=M\cap KL$ is the smallest saturated submodule containing $L$, of the same rank, and
$\operatorname{sat}(L)/L=(M/L)_{\tors}$. Saturated submodules: kernels of maps $M\to N$ with $N$ torsion-free; $M\cap W$ for a $K$-subspace
$W\subset M\otimes K$; $M[\mathfrak a]$ for any action of a ring $\T$ on $M$ and any f.g. ideal $\mathfrak a\subset\T$ ($M/M[\mathfrak a]\hookrightarrow M^k$);
orthogonal complements for a pairing (9.2). Non-examples: $3\Z\subset\Z$; $\Z(3,3)\subset\Z^2$ (while $\Z(1,3)$ is saturated).
Reference: elementary (Bourbaki, Algebra VII, for "pure submodules"; cite DF 12.1 exercises). Paper: Lemma lem:ddt417
("because $L[\wp]$ is saturated"), Lemma lem:crit ($L=f^\perp\cap S_2(\Gamma_0(N);\Z)$ and $\Z f=S_2(\Gamma_0(N);\Z)\cap\Q f$ are saturated),
Section 4.1 ($M_{f^\Sigma,\lambda}=H^1[\ker\phi]$ is saturated), PLAN.md scope ("the lattice/saturation notion").

**5.6 `thm:modules:stacked-bases`** (theorem, stacked bases; P). Let $R$ be a PID, $M$ free of rank $n$ and $L\subset M$ a submodule of
rank $d$. There are a basis $e_1,\dots,e_n$ of $M$ and nonzero $d_1\mid\cdots\mid d_d$ such that $d_1e_1,\dots,d_de_d$ is a basis of $L$. The ideals
$(d_i)$ (the *elementary divisors of $L$ in $M$*) are unique. Consequences: $M/L\simeq R^{n-d}\oplus\bigoplus_iR/(d_i)$; $L$ is saturated iff
every $d_i$ is a unit; if $d=n$ and $B$ is the matrix of a basis of $L$ in a basis of $M$, then $M/L$ is torsion of length
$v(\det B)$ over a DVR and of order $\abs{\det B}$ over $\Z$ (the *index* $[M:L]$). Reference: DF 12.1 (Theorem 4, check); Lang III.7.
Paper: Lemma lem:crit ("$\Z f\oplus L$ has index $r'$"), 9.3, 9.4, 11.6.

**5.7 `prop:modules:dual-inclusion`** (proposition; P). Let $R$ be a PID, $L\subset M$ lattices of the same rank $n$ with $M/L$ torsion
(finite when $R=\Z$ or $\Zl$). Then restriction $M^\vee\to L^\vee$ is injective and $L^\vee/M^\vee\simeq\bigoplus_iR/(d_i)$, with the same
invariant factors as $M/L$ (dual stacked bases $e_i^\vee$ and $e_i^\vee/d_i$). For $R=\Z$ or $\Zl$: $L^\vee/M^\vee\simeq(M/L)^*$, the
Pontryagin dual (8.1), so $[L^\vee:M^\vee]=[M:L]$. Variant used by the paper: if $A\hookrightarrow B$ is an injection of lattices of the same
rank with finite cokernel $C$, then $B^\vee\hookrightarrow A^\vee$ with cokernel $\simeq C^*$. Reference: elementary. Paper: Lemma lem:crit
("Dualising the inclusion $\T\subset\T/I\times\T/J$, whose cokernel is $\T/(I+J)$, shows that $\Z f\oplus L$ has index $r'$ in
$S_2(\Gamma_0(N);\Z)$": with 9.6, $\Hom(\T/I,\Z)\oplus\Hom(\T/J,\Z)=S_2[I]\oplus S_2[J]=\Z f\oplus L$ and $\Hom(\T,\Z)=S_2(\Gamma_0(N);\Z)$).

**5.8 `prop:modules:congruence-decomposition`** (proposition, the congruence module of a decomposition; P). Let $R$ be a PID
with fraction field $K$, $M$ a lattice, $M\otimes K=V_1\oplus V_2$ a decomposition into $K$-subspaces with projections $p_1,p_2$, and
$L_i=M\cap V_i$ (saturated). (i) $L_1\oplus L_2\subset M$ has finite colength (torsion quotient), and $x\mapsto p_i(x)$ induces isomorphisms
$M/(L_1\oplus L_2)\simeq p_1(M)/L_1\simeq p_2(M)/L_2$. (ii) If $V_1=Kf$ is a line with $f\in M$ and $L_1=Rf$ (i.e. $f$ is primitive), the
quotient embeds in $Kf/Rf\simeq K/R$, so it is cyclic, $\simeq R/(r)$, generated by the class of any $h\in M$ with $p_1(h)=f/r$; then
$rh=f+g_0$ with $g_0\in L_2$, so $f\equiv-g_0\pmod{rM}$; and $(r)$ is the smallest ideal $(r')$ for which $f\equiv g\pmod{r'M}$ with some
$g\in L_2$ (the *congruence modulus* of $f$ against $L_2$). (iii) Example (checked): $M=\Z^2$, $f=(1,a)$, $g=(1,b)$,
$V_1=\Q f$, $V_2=\Q g$: $M/(\Z f\oplus\Z g)\simeq\Z/(a-b)$ and $f\equiv g\pmod{(a-b)}$ coordinatewise. Reference: Hida81 (congruence
modules); Ribet83; DDT Section 4 (cite the section). Paper: Lemma lem:crit (the whole second paragraph of its proof:
"embeds in $\Q f/\Z f$ ... so it is cyclic, generated by the class of a form $h$ with projection $f/r'$; then $r'h=f+g_0$"),
Lemma lem:ddt417 ($Q=L/(L[\wp]\oplus L[I])$ is the congruence module of the decomposition $L\otimes K=L[\wp]_K\oplus L[I]_K$), Theorem
thm:quant Step 1 (the $\Zl$-version).

### Section 6. Discrete valuation rings, completions, $\Zl$, $\Ql$, $\Qlmod$

**6.1 `thm:modules:dvr`** (definition and theorem; P for (a) to (d), R for (e)). Let $\mathcal O$ be a Noetherian local domain which is
not a field, with maximal ideal $\mathfrak m$ and fraction field $K$. The following are equivalent: (a) $\mathfrak m$ is principal; (b) $\mathcal O$ is a
PID; (c) every nonzero ideal is a power of $\mathfrak m$; (d) there is a surjective homomorphism $v\colon K^\times\to\Z$ with
$v(x+y)\ge\min(v(x),v(y))$ and $\mathcal O=\{x:v(x)\ge0\}\cup\{0\}$; (e) $\mathcal O$ is integrally closed (with $\dim\mathcal O=1$). Such $\mathcal O$ is a
*discrete valuation ring* (DVR). A generator $\varpi$ of $\mathfrak m$ is a *uniformiser*; every $x\in K^\times$ is uniquely $u\varpi^{v(x)}$ with
$u\in\mathcal O^\times$; $\mathcal O^\times=\{v=0\}$; the nonzero ideals are $\varpi^k\mathcal O$. Key step (a)$\Rightarrow$(c),(d): Krull's intersection theorem in
the principal case, $\bigcap_k\mathfrak m^k=0$, proved directly (if $x=\varpi y_1=\varpi^2y_2=\cdots$, the chain $(y_1)\subset(y_2)\subset\cdots$ stabilises,
$y_{k+1}=uy_k$, so $(1-\varpi u)y_k=0$ and $y_k=0$). Reference: AM Proposition 9.2 (check); Serre, Local Fields, Chapter I,
Section 1. Paper: background ($\mathcal O$ in Lemma lem:ddt417 and Section 4.1; Chapter 6, item 4.7, applies (a) to $\Z_3[\zeta_3]$ in Lemma
lem:IV).

**6.2 `ex:modules:dvr-examples`** (examples; P where stated). DVRs: $\Z_{(p)}$ (Chapter 2, item 2.4); $K[[x]]$; $\Zl$ (6.4); and,
with proofs in other chapters, $\Z_3[\zeta_3]$ and $\Z_\ell[\zeta_3]$ for $\ell\equiv2\pmod3$ (Chapter 6, items 4.7, 4.9), the completions
$\mathcal O_\lambda$ of rings of integers (Chapters 6, 7). Non-DVRs: $\Z$ (not local), $\Z/p^2$ and $\mathcal O[\varepsilon]/(\varepsilon^2)$ (not domains),
$\Zl\times\Zl$ (not local), $\Zl[x]$ (not local, dimension two), $\Z_{(11)}[x]/(x^2+x-1)$ (a domain with two maximal ideals).
Paper: background.

**6.3 `prop:modules:dvr-modules`** (proposition; P). Let $\mathcal O$ be a DVR and $M$ a f.g. $\mathcal O$-module. (i)
$M\simeq\mathcal O^r\oplus\bigoplus_{i=1}^s\mathcal O/\varpi^{a_i}$, $a_i\ge1$, with $r$ and the multiset $\{a_i\}$ unique (5.3). (ii) $M$ torsion-free implies $M$
free. (iii) $\dim_kM/\varpi M=r+s$ (the minimal number of generators) and $\dim_kM[\varpi]=s$. (iv) $M[\varpi^k]\simeq\bigoplus_i\mathcal O/\varpi^{\min(k,a_i)}$
if $r=0$, and $M/\varpi^kM\simeq(\mathcal O/\varpi^k)^r\oplus\bigoplus_i\mathcal O/\varpi^{\min(k,a_i)}$. (v) $M$ is cyclic iff $r+s\le1$; a torsion module with
$\dim_kM[\varpi]\le1$ is cyclic. (vi) A submodule $L$ of a free $M$ is saturated iff $L\cap\varpi M=\varpi L$ (5.5(d)). Reference: DF 12.1;
Serre, Local Fields, Chapter I. Paper: Lemma lem:IV, Lemma lem:tamfactor, Lemma lem:h0 (a finite $H^0$ whose $\ell$-torsion has
order $\ell$ is cyclic, so its length is the largest $k$ with an element of exact order $\ell^k$; Chapter 16, item h0-and-torsion).

**6.4 `thm:modules:zl`** (definition and theorem; P for (i) to (vi), R for (vii)). $\Zl=\varprojlim_n\Z/\ell^n$, a ring (Chapter 1, item 7.2,
constructs it as a profinite group). (i) $x=(x_n)\in\Zl$ is a unit iff $x_1\ne0$ in $\Fl$. (ii) Every nonzero $x$ is uniquely $\ell^ku$ with
$k\ge0$, $u\in\Zl^\times$; $\Zl$ is a domain and a DVR with uniformiser $\ell$, residue field $\Fl$, ideals $\ell^k\Zl$, and valuation extending
$v_\ell$ on $\Z$. (iii) $\Z\to\Zl$ is injective, $\Z_{(\ell)}\subset\Zl$, and $\Zl/\ell^n\Zl\simeq\Z/\ell^n$; an integer prime to $\ell$ is a unit of $\Zl$, so a
$\Zl$-module killed by an integer prime to $\ell$ is zero. (iv) $\Ql:=\Frac(\Zl)=\Zl[1/\ell]$. (v) $\Zl$ is flat over $\Z$ (3.4(ii)); for a
f.g. abelian group $A\simeq\Z^r\oplus A_{\tors}$, $A\otimes_\Z\Zl\simeq\Zl^r\oplus A_{\tors}[\ell^\infty]$; for finite $A$, $\#(A\otimes\Zl)=\ell^{v_\ell(\#A)}$ ("the
$\ell$-part"; Chapter 1, item 1.8). (vi) Completeness: every f.g. $\Zl$-module $M$ satisfies $M\simeq\varprojlim M/\ell^nM$ (by 6.3(i) and the
case $M=\Zl$, $\Z/\ell^a$). (vii) More generally, the $I$-adic completion $\hat R=\varprojlim R/I^n$ of a Noetherian ring is Noetherian and
flat over $R$, and $\hat M=M\otimes_R\hat R$ for f.g. $M$ (Artin-Rees; stated). The analytic description of $\Zl$ and $\Ql$ (absolute
value, Cauchy sequences, Hensel's lemma, $\Z_p^\times$) is Chapter 7. Reference: Serre, Local Fields, Chapter II, Section 1;
AM Chapter 10. Paper: everywhere ($\Zl$-coefficients); Lemma lem:crit ("$\Z$ replaced by $\Zl$ and $r$ by its $\ell$-part"),
Lemma lem:dfg21 and the paragraph after it ("$H^1(\R,T^D)$ is killed by $2$, so $H^1_f(\R,T^D)=0$ for $\ell$ odd"), Lemma lem:fpr
("an $\ell$-adic integer").

**6.5 `prop:modules:qlzl`** (proposition; P). (i) $\Qlmod\simeq\Z[1/\ell]/\Z\simeq(\Q/\Z)[\ell^\infty]\simeq\varinjlim_k\Z/\ell^k$ (transition maps
multiplication by $\ell$); it is isomorphic, as an abstract group, to $\mu_{\ell^\infty}(\overline\Q)$ (no Galois action here). (ii) It is
divisible and $\ell$-primary torsion; $(\Qlmod)[\ell^k]=\ell^{-k}\Zl/\Zl\simeq\Z/\ell^k$; its proper $\Zl$-submodules are exactly these. (iii)
$\End_{\Zl}(\Qlmod)=\Zl$, $\Hom_{\Zl}(\Z/\ell^k,\Qlmod)\simeq\Z/\ell^k$, $\Hom_{\Zl}(\Zl,\Qlmod)=\Qlmod$. (iv) $\Qlmod$ is an injective
$\Zl$-module, and $\Q/\Z$ an injective $\Z$-module (divisible modules over a PID are injective: Baer's criterion, proved
for a PID); hence $\Hom(-,\Qlmod)$ is exact. Reference: Weibel 2.3; DF 10.5. Paper: Theorem thm:main and Lemma lem:h0
($W=\ad T\otimes\Qlmod$), Lemma lem:dfg21 (Pontryagin duals), Chapter 16 ("$\Qlmod$ injective").

**6.6 `prop:modules:zl-topology`** (proposition; P for (i) to (iii), S for (iv)). Give f.g. $\Zl$-modules the $\ell$-adic topology
(basis of neighbourhoods $\ell^nM$). (i) A f.g. $\Zl$-module is compact, Hausdorff and complete. (ii) Every submodule of a f.g.
$\Zl$-module is f.g. (4.1) and closed; every $\Zl$-linear map between f.g. modules is continuous with closed image. (iii)
$\GL_n(\Zl)=\Aut_{\Zl}(\Zl^n)$ is profinite (Chapter 1, item 7.4). (iv) *Topological Nakayama:* a compact Hausdorff
$\Zl$-module $A$ on which $\Zl$ acts continuously and with $A/\ell A$ finite is f.g. (sketch: by Pontryagin duality 8.2, $A^*$ is
discrete $\ell$-primary with $A^*[\ell]=(A/\ell A)^*$ finite, hence cofinitely generated, so $A=A^{**}$ is f.g.; NSW, Chapter V, Section
2, or Rubin, Appendix B, for the duality of compact modules). Reference: NSW Chapter I and V; Serre, Galois
Cohomology, Chapter I (not in refs.bib; Chapter 16 adds `SerreGaloisCoh`). Paper: Chapter 16 ($(t-1)M$ closed; continuous
cohomology with $\Zl$-modules of finite type), Lemma lem:tamfactor ("every $\Zl$-module $M'$ of finite type").

### Section 7. Length, annihilators, Fitting ideals

**7.1 `thm:modules:jordan-holder`** (definition and theorem; P). A composition series of $M$ is a chain
$0=M_0\subsetneq M_1\subsetneq\cdots\subsetneq M_n=M$ with simple quotients. (i) Jordan-Holder: any two composition series have the same
length and the same factors up to order and isomorphism (proof by induction on the minimal length, comparing
$M_{n-1}$ and $M'_{n-1}$ through $M_{n-1}\cap M'_{n-1}$; commutativity of $R$ is not used). The common length is $\len_R(M)$; $\len_R(M)=\infty$
if there is no composition series. (ii) $M$ has finite length iff it is Noetherian and Artinian (stated). (iii) Additivity: for
$0\to M'\to M\to M''\to0$, $\len(M)=\len(M')+\len(M'')$; for an exact sequence $0\to M_1\to\cdots\to M_k\to0$ of modules of finite length,
$\sum_i(-1)^i\len(M_i)=0$. (iv) Over a local ring $(R,\mathfrak m,k)$ every simple module is $\simeq k$; if $\mathfrak m^NM=0$ and $M$ is f.g. then
$\len(M)=\sum_{i<N}\dim_k\mathfrak m^iM/\mathfrak m^{i+1}M$; over a Noetherian local ring a f.g. module has finite length iff it is killed by a
power of $\mathfrak m$. (v) If $R\to R'$ is a local homomorphism of local rings with $R'$ finite over $R$ and residue extension of degree
$f$, then $\len_R(M)=f\len_{R'}(M)$ for every $R'$-module of finite length. Reference: AM Chapter 6; Lang X.3; Eisenbud 2.4.
Paper: Theorem thm:main, Theorem thm:dfg37, Remark rem:ns ($\len H^1_\Sigma$, $\len H^1_f$), Lemma lem:h0 ($h_\ell(E)$), Chapter
16 (lengths-in-exact-sequences uses (iii)); Chapter 4 cites (i) for representations.

**7.2 `prop:modules:length-dvr`** (proposition; P). Let $\mathcal O$ be a DVR. (i) $\len(\mathcal O/\varpi^a)=a$; a f.g. $\mathcal O$-module has finite length
iff it is torsion, and then $\len(\bigoplus_i\mathcal O/\varpi^{a_i})=\sum_ia_i$. (ii) If $k$ is finite, $\#M=(\#k)^{\len M}$; over $\Zl$, $\len_{\Zl}(M)=v_\ell(\#M)$ for
finite $M$; over $\mathcal O_\lambda$ with residue field $\F_{\ell^f}$, $v_\ell(\#M)=f\len(M)$. (iii) $\len(M[\varpi^k])$ and $\len(M/\varpi^kM)$ from 6.3(iv);
for a finite $\mathcal O$-module, $\len M[\varpi^k]=\len M/\varpi^kM$ (snake lemma, 2.3(b)). Examples: $\len_{\Zl}(\Z/\ell^v\oplus\Z/\ell^m)=v+m$;
$\len_{\Zl}(\Zl/n')=v_\ell(n')$. Reference: as 7.1. Paper: Theorem thm:main ("$\len_{\Zl}$"), Lemma lem:tamfactor (orders
$\ell^{v_\ell(n)}\cdot\ell^{\min(\dots)}$), PLAN.md Appendix B ("length means $\Zl$-length").

**7.3 `def:modules:annihilator`** (definition and proposition; P). $\Ann_R(M)=\{r:rM=0\}$, $\Ann_R(m)$, and $M[\mathfrak a]$ (C3). (i)
$\Ann(R/\mathfrak a)=\mathfrak a$; $\Ann(M\oplus N)=\Ann M\cap\Ann N$; $\Ann(M)$ is the kernel of $R\to M^n$, $r\mapsto(rm_i)$, for generators $m_1,\dots,m_n$. (ii)
$M[\mathfrak a]=\Hom_R(R/\mathfrak a,M)$; $M[\mathfrak a]\cap M[\mathfrak b]=M[\mathfrak a+\mathfrak b]$; $M[\mathfrak a]+M[\mathfrak b]\subset M[\mathfrak a\cap\mathfrak b]$. (iii) For a ring $\T$ and an ideal $\mathfrak a$,
$\T[\mathfrak a]=\Ann_\T(\mathfrak a)$; if $L\simeq\T^r$ then $L[\mathfrak a]=\Ann_\T(\mathfrak a)^r$. (iv) Flat base change (3.4(iii)) for f.g. $M$ and f.g. $\mathfrak a$. (v) Over a
DVR: $\Ann(\bigoplus\mathcal O/\varpi^{a_i})=\varpi^{\max a_i}$. "$M$ is killed by $\eta$" means $\eta\subset\Ann(M)$. Reference: AM Chapters 1, 2. Paper: Lemma
lem:crit ($J=\Ann_\T(f^\perp)$, "$\phi_f(\Ann_\T I)$"), Lemma lem:ddt417 ($I=\Ann_\T(\wp)$, $L[\wp]$, $L[I]$, "$Q$ is killed by $\eta$", "$L\simeq\T^d$
then $Q\simeq(\T/(\wp+I))^d$"), Lemma lem:hecke, Theorem thm:quant Step 1 ($\eta^{\mathrm{Hecke}}=\pi(\Ann_\T\ker\pi)$), PLAN.md scope ("Ann").

**7.4 `def:modules:fitting`** (definition and theorem; P for the definition and for presentations over a PID, S for the
independence in general). Let $M$ be a finitely presented $R$-module with a presentation $R^m\xrightarrow{A}R^n\to M\to0$ (C8). The
(zeroth) *Fitting ideal* $\Fitt_R(M)$ is the ideal generated by the $n\times n$ minors of $A$ ($0$ if $m<n$); more generally $\Fitt_i(M)$ uses
the $(n-i)\times(n-i)$ minors. It does not depend on the presentation (sketch: two presentations are related by invertible row and
column operations, by adding redundant relations, and by adding a generator together with a relation expressing it, none
of which changes the ideal of maximal minors; Eisenbud, Section 20.2, for the full proof). Reference: Eisenbud Chapter 20;
Northcott, Finite free resolutions (not in refs.bib; add to `bib/ch03.bib` if cited); Mazur-Wiles 1984, Appendix (add to
`bib/ch03.bib` if cited). Paper: Section 1.2 ($\Tam_p$), Lemma lem:fpr, PLAN.md scope ("definition via presentations").

**7.5 `prop:modules:fitting-properties`** (proposition; P). Let $M,N$ be finitely presented. (i) $\Fitt(R/\mathfrak a)=\mathfrak a$; $\Fitt(0)=R$;
$\Fitt(R^n)=0$ for $n\ge1$. (ii) $\Fitt(M\oplus N)=\Fitt(M)\Fitt(N)$ (block-diagonal presentation; the maximal minors of a block-diagonal
matrix are sums of products of maximal minors of the blocks). (iii) If $M\to N$ is surjective, $\Fitt(M)\subset\Fitt(N)$ (a presentation of $N$
is obtained from one of $M$ by adding relations). (iv) $\Fitt(M)\subset\Ann(M)$ (adjugate), and $\Ann(M)^n\subset\Fitt(M)$ if $M$ has $n$
generators. (v) $\Fitt_S(S\otimes_RM)=\Fitt_R(M)S$ for every ring homomorphism $R\to S$ (no flatness needed). (vi) For
$0\to M'\to M\to M''\to0$: $\Fitt(M')\Fitt(M'')\subset\Fitt(M)$ (block-triangular relations define a module surjecting onto $M$; then (iii)); equality
fails in general: over $R=k[\varepsilon]/(\varepsilon^2)$ with $M=R$, $M'=\varepsilon R\simeq k$, $M''=R/\varepsilon R\simeq k$ one has $\Fitt(M)=R$ but
$\Fitt(M')\Fitt(M'')=(\varepsilon)^2=0$. (vii) Over a domain, $\Fitt(M)\ne0$ iff $M$ is torsion. Reference: Eisenbud 20.2; Mazur-Wiles
1984, Appendix. Paper: PLAN.md scope ("Fitting ideal of a direct sum, of a quotient"), Lemma lem:tamfactor (the Fitting ideal of
the invariants, a submodule, compared with that of the whole torsion: by (vi) and 7.6 it is smaller in length).

**7.6 `thm:modules:fitting-dvr`** (theorem; P). (i) Over a PID, $\Fitt(R^r\oplus\bigoplus_iR/(d_i))=0$ if $r>0$ and $=(\prod_id_i)$ if $r=0$ (5.2:
the product of the invariant factors generates the ideal of maximal minors). (ii) Over a DVR $\mathcal O$, for a f.g. torsion
module, $\Fitt_{\mathcal O}(M)=\varpi^{\len(M)}\mathcal O$; hence $v(\Fitt(M))=\len(M)$, and over $\Zl$, $\Fitt_{\Zl}(M)=\#M\cdot\Zl=\ell^{v_\ell(\#M)}\Zl$. (iii)
Consequently, over a DVR the Fitting ideal of finite-length modules is multiplicative in short exact sequences (7.1(iii)),
and $\Fitt(N)\supset\Fitt(M)$ for every submodule or quotient $N$ of $M$. (iv) $\Fitt\ne\Ann$: $(\Z/\ell)^2$ and $\Z/\ell^2$ both have
Fitting ideal $\ell^2\Zl$, with annihilators $\ell\Zl$ and $\ell^2\Zl$. Reference: Eisenbud 20.2; Mazur-Wiles 1984, Appendix. Paper:
Section 1.2 ($\Tam_p(M)$ is $\ell^{\len}$ of the invariants of the torsion of $H^1(I_p,M)$), Lemma lem:tamfactor
($v_\ell(\Tam_q(\ad T))=v_\ell(n)+\min(\dots)$ is the length of $\Z/\ell^{v}\oplus\Z/\ell^{m}$), Lemma lem:fpr ($\Fitt_{\Zl}H^1_f(\Q_p,T^D)$ is $\ell$ to the
length), PLAN.md scope ("over a DVR $\Fitt=\ell^{\mathrm{length}}$"), Section 6 map row (Tamagawa factor).

**7.7 `ex:modules:fitting-examples`** (worked examples; P, all checked). Over $\Z$ (relations as rows): $\begin{psmallmatrix}2&4\\6&8\end{psmallmatrix}$:
$\Fitt=(8)$, module $\Z/2\oplus\Z/4$, $\Ann=(4)$; the DF matrix of 5.2: $\Fitt=(144)$, $\Ann=(12)$; $\begin{psmallmatrix}3&6\\9&3\end{psmallmatrix}$: $\Fitt=(45)$, and over $\Z_3$
$\Fitt=9\Z_3$ (length $2$); a presentation with more relations than generators, rows $(6,0),(0,4),(2,2)$: module $\Z/2\oplus\Z/2$,
$\Fitt=(4)$ (gcd of the three $2\times2$ minors $24,12,-8$), $\Ann=(2)$; rows $(2),(4)$ on one generator: $\Fitt=(2)$. Over a non-PID:
$R=\Z[x]$, $M=R/(2,x)$ (one generator, relation rows $(2)$ and $(x)$): $\Fitt=(2,x)=\Ann$, while
$\Fitt(M\oplus M)=(2,x)^2=(4,2x,x^2)\subsetneq\Ann=(2,x)$. The paper's case: $\Fitt_{\Zl}(\Z/\ell^v\oplus\Z/\ell^m)=\ell^{v+m}\Zl$; for $\ell=3$, $v=2$,
$m=1$: $27\Z_3$ with annihilator $9\Z_3$. Paper: Lemma lem:tamfactor, Section 1.2.

### Section 8. Pontryagin duality

**8.1 `thm:modules:pontryagin-finite`** (theorem; P). For a finite abelian group $A$ let $A^*=\Hom(A,\Q/\Z)$. (i) $(\Z/n)^*\simeq\Z/n$,
so $A^*\simeq A$ (non-canonically, by Chapter 1, item 4.1). (ii) The evaluation map $A\to A^{**}$ is an isomorphism. (iii)
$A\mapsto A^*$ is an exact contravariant functor (6.5(iv)), and $\#A^*=\#A$. (iv) For $B\subset A$, $B^\perp=\{\varphi:\varphi(B)=0\}\simeq(A/B)^*$ and
$B^*\simeq A^*/B^\perp$; $B\mapsto B^\perp$ is an inclusion-reversing bijection between subgroups of $A$ and of $A^*$. (v) If $A$ is
$\ell$-primary, $A^*=\Hom_{\Zl}(A,\Qlmod)$ and $\len_{\Zl}A^*=\len_{\Zl}A$; dualising an exact sequence of finite $\Zl$-modules gives an exact
sequence with arrows reversed. (vi) The physics reader's dictionary: $x\mapsto e^{2\pi ix}$ identifies $A^*$ with the group of characters
$A\to\C^\times$ of Chapter 2, item 10.2 (one sentence). Reference: Serre, Course in Arithmetic, VI.1; NSW Chapter I, Section 1.
Paper: Lemma lem:dfg21 ("where ${}^*$ is the Pontryagin dual": the finite groups $H^1_f(\Q_p,T^D)$ and $H^0(\Q,W^D)$), the proof of
Theorem thm:main (lengths of the four terms), Remark rem:ns.

**8.2 `thm:modules:pontryagin-zl`** (theorem; P for the f.g. and cofinitely generated modules, R for general compact and
discrete modules). Let $\mathcal C$ be the f.g. $\Zl$-modules and $\mathcal D$ the discrete $\ell$-primary torsion $\Zl$-modules $W$ with $W[\ell]$ finite
(*cofinitely generated*). For $M\in\mathcal C$ put $M^*=\Hom_{\Zl}(M,\Qlmod)$ (every such homomorphism is continuous for the $\ell$-adic topology
on $M$ and the discrete one on $\Qlmod$); for $W\in\mathcal D$ put $W^*=\Hom_{\Zl}(W,\Qlmod)=\varprojlim_k\Hom(W[\ell^k],\Qlmod)$ with the inverse-limit
topology. (i) $\Zl^*=\Qlmod$, $(\Qlmod)^*=\Zl$, $(\Z/\ell^a)^*\simeq\Z/\ell^a$. (ii) $M\mapsto M^*$ and $W\mapsto W^*$ are exact, map $\mathcal C$ to $\mathcal D$ and
$\mathcal D$ to $\mathcal C$, and $M\to M^{**}$, $W\to W^{**}$ are isomorphisms. (iii) Every $W\in\mathcal D$ is $\simeq(\Qlmod)^r\oplus F$ with $F$ finite; $r$ is
the *corank*, equal to $\rank_{\Zl}W^*$; $W$ is finite iff its corank is $0$; $W$ is divisible iff $F=0$. (iv) Lengths of finite modules
are preserved. (v) General Pontryagin duality between compact and discrete $\ell$-primary $\Zl$-modules (stated). Reference:
NSW Chapter I, Section 1; Rubin, Appendix B; Serre, Local Fields, Chapter XIII (check). Paper: Lemma lem:dfg21 (duals),
Lemma lem:h0 ("$H^0(\Q,W^D)$ is finite"), Theorem thm:dfg37 ("$H^1_\Sigma(\Q,W)$ is finite"), Chapter 16 (pontryagin-duality-cohomology
recalls (ii) to (iv)).

**8.3 `prop:modules:t-and-w`** (proposition, the duality between $T$ and $T\otimes\Qlmod$; P). Let $T$ be a free $\Zl$-module of rank $r$,
$V=T\otimes_{\Zl}\Ql$, $W=T\otimes_{\Zl}\Qlmod$. (i) $0\to T\to V\to W\to0$ is exact (tensor $0\to\Zl\to\Ql\to\Qlmod\to0$ with the flat $T$), and
$W\simeq(\Qlmod)^r$ is divisible of corank $r$. (ii) $W[\ell^k]\simeq T/\ell^kT$ via $t\otimes\ell^{-k}\mapsto t\bmod\ell^k$; under it the inclusion
$W[\ell^k]\subset W[\ell^{k+1}]$ becomes multiplication by $\ell\colon T/\ell^k\to T/\ell^{k+1}$, and multiplication by $\ell\colon W[\ell^{k+1}]\to W[\ell^k]$ becomes
reduction. (iii) $T\simeq\varprojlim_kW[\ell^k]$ (transition maps multiplication by $\ell$): $T$ is the Tate module of $W$. (iv)
$W^*=\Hom(T\otimes\Qlmod,\Qlmod)\simeq\Hom_{\Zl}(T,\End(\Qlmod))=\Hom_{\Zl}(T,\Zl)=T^\vee$, and $T^*\simeq T^\vee\otimes\Qlmod$. (v) Everything is functorial in
$T$: a group acting $\Zl$-linearly on $T$ acts on $V$, $W$, $W[\ell^k]=T/\ell^kT$, and on the duals by $(g\varphi)(x)=\varphi(g^{-1}x)$. (vi) The same
holds over any complete DVR $\mathcal O$ with $K/\mathcal O$ in place of $\Qlmod$. Twists by $\Zl(1)$, the Cartier dual $T^D=\Hom(T,\Zl(1))$ and
$W^D=V^D/T^D$ are Chapters 17 and 18 (Chapter 17 needs them first, for local duality); the Galois action is Chapters 16, 17. Reference: NSW Chapter I; Rubin, Section 1.1 (check).
Paper: Theorem thm:main ($W=\ad T\otimes\Qlmod$), Lemma lem:h0 ("its $\ell$-torsion"; "the description of the length follows from
the $\ell^k$-torsion": $W^D[\ell^k]=T^D/\ell^k$), Lemma lem:dfg21 ($W$, $T^D$, $W^D$), PLAN.md scope ("the duality between $T$ and
$T\otimes\Ql/\Zl$").

**8.4 `cor:modules:cyclic-l-primary`** (corollary; P). An $\ell$-primary torsion $\Zl$-module $A$ with $\#A[\ell]\le\ell$ is $0$, $\Z/\ell^h$ or $\Qlmod$;
if finite, its length is the largest $k$ such that $A$ has an element of exact order $\ell^k$. (From 8.2(iii) and 6.3(v).) Reference:
elementary. Paper: Lemma lem:h0 (with important_notes.md point 5: the $\ell$-torsion of $H^0(\Q,W^D)$ is at most a line, so
$h_\ell(E)$ is the largest $k$ with $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$); Chapter 16, item h0-and-torsion (c) recalls it.

### Section 9. Pairings: perfect pairings, Gram determinants, saturated sublattices, alternating pairings, adjoints

**9.1 `def:modules:pairing`** (definition and proposition; P). For a pairing $\langle\ ,\ \rangle\colon L\times M\to R$ (C5) let
$\alpha\colon L\to M^\vee$, $x\mapsto\langle x,-\rangle$, and $\beta\colon M\to L^\vee$, $y\mapsto\langle-,y\rangle$. The pairing is *perfect* if $\alpha$ and $\beta$ are
isomorphisms, *nondegenerate* if they are injective. (i) For $L$, $M$ free of rank $n$ with bases $(e_i)$, $(f_j)$ and Gram matrix
$G=(\langle e_i,f_j\rangle)$: the pairing is perfect iff $\det G\in R^\times$ (iff one of $\alpha,\beta$ is an isomorphism); over a domain it is
nondegenerate iff $\det G\ne0$. Example: $\langle x,y\rangle=2xy$ on $\Z$ is nondegenerate, not perfect; it is perfect over $\Zl$ for $\ell$ odd. (ii)
Change of bases $e'=eP$, $f'=fQ$ gives $G'=P^{\mathsf T}GQ$ and $\det G'=\det P\det Q\det G$; for $L=M$ with the same basis change,
$\det G'=(\det P)^2\det G$. So the ideal $\Delta R$ generated by the *Gram determinant* $\Delta=\det G$ does not depend on the bases, and
over a DVR its valuation $v(\Delta)$ is basis-independent (PLAN.md scope). (iii) Perfectness is preserved by base change
$R\to S$ (the Gram determinant maps to a unit). Reference: Lang XV.1; Serre, Course in Arithmetic, V.1 (for $\Z$-lattices).
Paper: Lemma lem:ddt417 ("a perfect $\mathcal O$-bilinear pairing", "Gram determinant $\Delta\ne0$"), Lemma lem:crit ("the pairing being
perfect after tensoring with $\Zl$"), Section 4.1.

**9.2 `prop:modules:orthogonal`** (proposition; P). Let $\mathcal O$ be a DVR (or a PID) and $\langle\ ,\ \rangle\colon L\times L\to\mathcal O$ a perfect pairing on a
lattice of rank $n$, not necessarily symmetric; write $S^\perp=\{y:\langle S,y\rangle=0\}$ (right) and ${}^\perp S$ (left). (i) $S^\perp$ and
${}^\perp S$ are saturated for every subset $S$. (ii) For a submodule $N$ of rank $d$: $\rank N^\perp=n-d$ and ${}^\perp(N^\perp)=\operatorname{sat}(N)$; for
$N$ saturated, ${}^\perp(N^\perp)=N$. (iii) If the pairing is symmetric or antisymmetric, left and right orthogonals agree. Reference:
elementary. Paper: Lemma lem:ddt417 ($L[\wp]^\perp$), 9.3.

**9.3 `thm:modules:gram-cokernel`** (theorem; P). Let $\mathcal O$ be a DVR, $L$ a lattice of rank $n$ with a perfect pairing, $L'\subset L$ a
**saturated** sublattice of rank $d$, and $\Delta$ the Gram determinant of the restriction of the pairing to $L'$ (any basis). (i) The
map $\rho\colon L\to\Hom_{\mathcal O}(L',\mathcal O)$, $y\mapsto\langle-,y\rangle|_{L'}$, is surjective with kernel $L'^\perp$ (because $L'$ is a direct summand and
$L\simeq L^\vee$); so $L/L'^\perp\simeq\Hom(L',\mathcal O)$. (ii) If $\Delta\ne0$: $L'\cap L'^\perp=0$, the restriction $\rho|_{L'}\colon L'\to\Hom(L',\mathcal O)$ is injective, and
$$L/(L'\oplus L'^\perp)\ \simeq\ \coker\bigl(L'\to\Hom(L',\mathcal O)\bigr)\ \simeq\ \textstyle\bigoplus_i\mathcal O/(\delta_i),$$
where the $\delta_i$ are the invariant factors of the Gram matrix; its length is $v(\Delta)$, and its order is $\#\mathcal O/\Delta\mathcal O=(\#k)^{v(\Delta)}$
when $k$ is finite. (iii) $L'^\perp$ is saturated of rank $n-d$, and the Gram determinant of the restriction to $L'^\perp$ has the
same valuation $v(\Delta)$. (iv) Saturation is necessary: in $L=\Zl^2$ with the standard pairing, $L'=\Zl\cdot\ell e_1$ has
$\Delta=\ell^2$ while $L/(L'\oplus L'^\perp)\simeq\Z/\ell$ has length $1$. Example (checked): on $\Z^2$ with Gram matrix
$\begin{psmallmatrix}9&1\\1&0\end{psmallmatrix}$ (perfect, determinant $-1$), $L'=\Z e_1$ has $\Delta=9$, $L'^\perp=\Z(1,-9)$, and $[L:L'\oplus L'^\perp]=9$; (ii) was also checked on $500$
random perfect pairings and saturated sublattices of rank $\le5$ over $\Z$, and (iii) on $300$ of them (non-symmetric pairings). Reference:
elementary; Serre, Course in Arithmetic, V.1 (discriminants of sublattices); Eichler-style arguments in DDT Section 4
(cite the section). Paper: Lemma lem:ddt417 ("The pairing identifies $L/L[\wp]^\perp$ with $\Hom(L[\wp],\mathcal O)$, because $L[\wp]$ is
saturated"; "Hence $Q$ is the cokernel of $L[\wp]\to\Hom(L[\wp],\mathcal O)$, of order $\#\mathcal O/\Delta$"), PLAN.md scope ("for a saturated sublattice $L$
of rank $d$, the cokernel of $L\to\Hom(L,\mathcal O)$ has order $\#\mathcal O/(\text{Gram det})$").

**9.4 `prop:modules:alternating`** (proposition; P, except the Pfaffian identity and the normal form in general rank, S). A
pairing $L\times L\to R$ is alternating if $\langle x,x\rangle=0$ for all $x$; then it is antisymmetric; conversely antisymmetric implies
alternating if $2$ is a nonzerodivisor in $R$ (e.g. $R$ a domain of characteristic $0$, or $\ell$ odd). (i) The Gram matrix of an
alternating pairing is antisymmetric with zero diagonal; its determinant is $\operatorname{Pf}(G)^2$ (Pfaffian; stated with the rank $4$ case
checked), and it vanishes in odd rank; so a perfect alternating pairing exists only in even rank. (ii) Rank two: $G=\begin{psmallmatrix}0&a\\-a&0\end{psmallmatrix}$
with $a=\langle e_1,e_2\rangle$, so $\Delta=a^2$, and the ideal of values $\langle L,L\rangle=\{\langle x,y\rangle\}$ is $a\mathcal O$ (since $\langle x,y\rangle=a(x_1y_2-x_2y_1)$). Hence, basis-free:
$\Delta\mathcal O=(\text{ideal of values})^2$. (iii) Over a PID an alternating pairing has a basis in which $G$ is block diagonal with
blocks $\begin{psmallmatrix}0&d_i\\-d_i&0\end{psmallmatrix}$, $d_1\mid d_2\mid\cdots$, and zeros (symplectic normal form; S); it is perfect iff all $d_i$ are units and there
are no zero blocks. Reference: Lang XV.8 (check); Bourbaki, Algebra IX. Paper: Section 4.1 ("$\hat\delta_!$ ... perfect and alternating";
"the Gram determinant of the pairing on $M_{f^\Sigma,\lambda}$ is $(\eta^\Sigma_{f,\lambda})^2$ up to a unit", with $\eta^\Sigma_{f,\lambda}$ defined as the ideal of
values), Lemma lem:hecke ($d=2$, Gram determinant $(\eta^\emptyset_{f,\lambda})^2$), Theorem thm:quant Step 2, PLAN.md scope ("rank-two Gram
determinant is a square").

**9.5 `prop:modules:adjoint`** (proposition; P). Let $\langle\ ,\ \rangle$ be a perfect pairing on a lattice $L$ over $R$. (i) Every $A\in\End_R(L)$
has a unique adjoint $A^\dagger$ with $\langle Ax,y\rangle=\langle x,A^\dagger y\rangle$; in matrices $A^\dagger=G^{-1}A^{\mathsf T}G$ (C5, C8: write the convention once);
$(AB)^\dagger=B^\dagger A^\dagger$, $(A^\dagger)^\dagger=A$ for symmetric or antisymmetric pairings. (ii) Let $\T\subset\End_R(L)$ be a commutative subring of
self-adjoint endomorphisms. For every ideal $\mathfrak a\subset\T$: $(\mathfrak aL)^\perp=L[\mathfrak a]$ (since $\langle ax,y\rangle=\langle x,ay\rangle$ and the pairing is perfect). (iii)
Idempotents of $\T$ (or of $\T\otimes S$ for an $R$-algebra $S$) are self-adjoint; for an idempotent $e$, $L=eL\oplus(1-e)L$ is an
orthogonal decomposition, and the restriction of the pairing to $eL$ is perfect. (iv) Twisted pairings: let $w\in\Aut_R(L)$ with
$A^\dagger=wAw^{-1}$ for all $A\in\T$, and put $[x,y]=\langle x,wy\rangle$. Then $[\ ,\ ]$ is perfect and every $A\in\T$ is self-adjoint for it. If $\langle\ ,\ \rangle$ is
antisymmetric and $w^\dagger=w$ (for instance $w$ an involution preserving the pairing, so $w^\dagger=w^{-1}=w$), then $[\ ,\ ]$ is antisymmetric,
hence alternating when $2$ is a nonzerodivisor. Reference: Lang XV.1 (check). Paper: Section 4.1 ("the Hecke operators,
$U_p$ included, are self-adjoint for it, because $w_{M^\Sigma}T_nw_{M^\Sigma}^{-1}$ is the adjoint of $T_n$ for the cup product (this is what the
composition with $w$ is for)": the geometric inputs are Chapters 8 and 14), Lemma lem:ddt417 ("for which $\T$ is self-adjoint"),
Lemma lem:hecke (the restriction of $\hat\delta_!$ to the $\mathfrak m$-component is perfect, by (iii)), PLAN.md scope ("adjoints").

**9.6 `prop:modules:algebra-duality`** (proposition; P). Let $R$ be a PID (in practice $\Z$ or $\Zl$), $\T$ a commutative $R$-algebra
that is free of finite rank as an $R$-module, $S$ a $\T$-module free of finite rank over $R$, and $\langle\ ,\ \rangle\colon S\times\T\to R$ a perfect
$R$-bilinear pairing with $\langle ts,u\rangle=\langle s,tu\rangle$ (example: $\langle g,t\rangle=a_1(tg)$ on $S_2(\Gamma_0(N);\Z)\times\T$, Chapter 13). (i)
$s\mapsto\langle s,-\rangle$ is an isomorphism of $\T$-modules $S\simeq\T^\vee=\Hom_R(\T,R)$, where $(t\varphi)(u)=\varphi(tu)$. (ii) For every ideal
$\mathfrak a\subset\T$: $S[\mathfrak a]\simeq\Hom_R(\T/\mathfrak a,R)$ (the functionals vanishing on $\mathfrak a$); it is saturated in $S$ and of rank $\rank_R(\T/\mathfrak a)$.
(iii) If $I,J\subset\T$ are ideals with $I\cap J=0$ and $\T/I$, $\T/J$ torsion-free, the inclusion $\T\hookrightarrow\T/I\times\T/J$ (2.2) has finite
cokernel $\T/(I+J)$, and dually $S[I]\oplus S[J]\subset S$ with $S/(S[I]\oplus S[J])\simeq\bigl(\T/(I+J)\bigr)^*$ for $R=\Z$ or $\Zl$ (5.7), of the same
order. (iv) $\T$ acts faithfully on $S$. Reference: Ribet83 (Theorem 2.2 as the paper cites it); DDT Section 4 (cite the
section). Paper: Lemma lem:crit ("under it the forms killed by $I$ are $\Z f$ and the forms killed by $J$ are $L$"; "Dualising the
inclusion ... shows that $\Z f\oplus L$ has index $r'$"), Theorem thm:quant Step 1 (the $\Zl$-version).

### Section 10. Finite free algebras over a DVR; idempotents; generalised eigenspaces; semisimplicity

**10.1 `thm:modules:artinian-algebras`** (theorem; P). Let $A$ be a commutative algebra of finite dimension over a field $F$. (i) $A$
has finitely many maximal ideals $\mathfrak m_1,\dots,\mathfrak m_s$ ($s\le\dim A$, by CRT), every prime ideal is maximal, and the Jacobson radical
$\mathfrak J=\bigcap\mathfrak m_i$ is nilpotent (the chain $\mathfrak J^k$ stabilises; Nakayama). (ii) $A\simeq\prod_iA_{\mathfrak m_i}$, each factor local with nilpotent
maximal ideal (CRT for the comaximal $\mathfrak m_i^N$, Chapter 2, item 1.4(iii)); the factors are cut out by idempotents $e_1,\dots,e_s$ with
$\sum e_i=1$, $e_ie_j=0$. (iii) $A$ is reduced iff $\mathfrak J=0$ iff $A$ is a product of fields. (iv) Every $A$-module $V$ is $\bigoplus_ie_iV$ with
$e_iV=V_{\mathfrak m_i}$. Reference: AM Theorem 8.7 (structure theorem for Artin rings; check) and Chapter 8. Paper: Lemma lem:crit
("$\T\otimes\Q=\Q\times\T'$"), Theorem thm:quant Step 1, Section 11 below.

**10.2 `thm:modules:finite-algebra-dvr`** (theorem; P). Let $\mathcal O$ be a DVR and $\T$ a commutative $\mathcal O$-algebra that is finite and free as an
$\mathcal O$-module (a *finite flat* or *finite free* $\mathcal O$-algebra). (i) $\T$ is Noetherian; every maximal ideal of $\T$ contains $\varpi$ (if $\mathfrak M$
is maximal, $\T/\mathfrak M$ is a field finite over the image of $\mathcal O$, which is then a field, so $\mathfrak M\cap\mathcal O=\varpi\mathcal O$); so the maximal ideals of $\T$
correspond to those of the finite $k$-algebra $\T/\varpi\T$, are finite in number, and have residue fields finite over $k$. (ii) $\T$ is
torsion-free and $\T\subset\T_K:=\T\otimes_{\mathcal O}K$, a finite-dimensional $K$-algebra (10.1); $\T$ is reduced iff $\T_K$ is reduced iff $\T$
embeds in a product of fields. (iii) A surjective $\mathcal O$-algebra homomorphism $\pi\colon\T\to\mathcal O$ has kernel $\wp$ with $\T/\wp\simeq\mathcal O$ ($\wp$ is
a prime ideal, $\T=\mathcal O\cdot1\oplus\wp$ as $\mathcal O$-modules), and determines the maximal ideal $\mathfrak m_\pi=\pi^{-1}(\varpi\mathcal O)=\wp+\varpi\T$; it extends to
$\pi_K\colon\T_K\to K$, which factors through exactly one local factor of $\T_K$ (10.1). Reference: AM Chapters 5, 8; DDT Section
4 (cite the section). Paper: Lemma lem:ddt417 ("$\T$ a commutative $\mathcal O$-algebra, finite and free as an $\mathcal O$-module", "$\pi\colon\T\to\mathcal O$
surjective"), Lemma lem:hecke ("$\mathfrak m$ the maximal ideal of $\T\otimes\Zl$ containing $\ell$ and $\ker\phi_f$" is $\mathfrak m_{\phi_f}$), Lemma lem:crit
("a maximal ideal of residue characteristic $\ell$").

**10.3 `thm:modules:idempotent-lifting`** (theorem; P). Let $\mathcal O$ be a **complete** DVR (e.g. $\Zl$, or $\mathcal O_\lambda$ of Chapter 7) and $\T$ as in
10.2. (i) Every idempotent $\bar e$ of $\T/\varpi\T$ lifts to a unique idempotent of $\T$ (Newton iteration $e\mapsto3e^2-2e^3$, which squares
the error $e^2-e$ up to a unit factor and converges $\varpi$-adically; uniqueness: two idempotents congruent mod $\varpi$ are equal).
(ii) $\T\simeq\prod_{\mathfrak m}\T_{\mathfrak m}$ over the maximal ideals $\mathfrak m$, where $\T_{\mathfrak m}=e_{\mathfrak m}\T$ is the localisation of $\T$ at $\mathfrak m$, a local ring,
finite and free over $\mathcal O$ (2.7). (iii) For every $\T$-module $L$: $L=\bigoplus_{\mathfrak m}e_{\mathfrak m}L$ and $L_{\mathfrak m}=e_{\mathfrak m}L$; if $L$ is f.g. free over $\mathcal O$, so is
each $L_{\mathfrak m}$. (iv) A ring homomorphism from $\T$ to a local ring (for instance $\pi\colon\T\to\mathcal O$, or $\T\to k'$ a field) factors
through exactly one $\T_{\mathfrak m}$: $\pi(e_{\mathfrak m_\pi})=1$ and $\pi(e_{\mathfrak m'})=0$ for $\mathfrak m'\ne\mathfrak m_\pi$. (v) Completeness is necessary: $\Z_{(11)}[x]/(x^2+x-1)$ has
two maximal ideals above $11$ (the polynomial has the roots $3$ and $7$ mod $11$) but no idempotent other than $0,1$ (it is a domain,
the polynomial being irreducible over $\Q$). Reference: Eisenbud 7.5 (Hensel and idempotents; check); AM Chapter 10;
DDT Section 4 (cite the section). Paper: Lemma lem:hecke ("the other local factors of $\T\otimes\Zl$ are killed by $\phi_f$"), Theorem
thm:quant Step 1 ("the $\mathfrak m$-component (an idempotent of $\T_\ell$ ...)"), Remark rem:free, PLAN.md scope ("$\T\otimes\Zl$ is a product of
local rings, idempotents").

**10.4 `cor:modules:hecke-type`** (corollary and examples; P). Let $\T$ be a commutative ring that is free of finite rank as a
$\Z$-module (the Hecke algebra, Chapter 13). Then $\T\otimes\Zl$ is finite free over $\Zl$, its maximal ideals are the $\mathfrak m\otimes\Zl$ for the
maximal ideals $\mathfrak m\ni\ell$ of $\T$, and $\T\otimes\Zl=\prod_{\mathfrak m\ni\ell}\T_{\mathfrak m}$ with $\T_{\mathfrak m}=(\T\otimes\Zl)_{\mathfrak m}$, which is also the $\mathfrak m$-adic completion of $\T$
(convention C7). Examples (checked): (a) $\T=\Z[x]/(x^2+x-1)=\Z[\frac{1+\sqrt5}2]$ (the Hecke algebra of level $23$, Chapter 6, item
7.5): $x^2+x-1\equiv(x-3)(x-7)\pmod{11}$, so $\T\otimes\Z_{11}\simeq\Z_{11}\times\Z_{11}$ with idempotent $e=(x-r_2)/(r_1-r_2)$, $r_1\equiv7$, $r_2\equiv3$ the
Hensel lifts (computed mod $11^6$, and equal to the Newton limit of $(x-3)/4$); $x^2+x-1\equiv(x-2)^2\pmod5$, so $\T\otimes\Z_5$ is local
(a ramified DVR); mod $2$ and mod $3$ the polynomial is irreducible, so $\T\otimes\Z_2$, $\T\otimes\Z_3$ are local (unramified DVRs with
residue fields $\F_4$, $\F_9$). (b) $\T=\Z[x]/(x^2-4)\simeq\{(a,b)\in\Z^2:a\equiv b\pmod4\}$: $\T\otimes\Z_3=\Z_3\times\Z_3$ with idempotent
$(x+2)/4$; $\T\otimes\Z_2$ is local and not a domain. Reference: DDT Section 4 (cite the section); Chapter 6, item 7.3(iv), which
cites this. Paper: Lemma lem:hecke, Remark rem:free, Theorem thm:quant (all their $\T_{\mathfrak m}$).

**10.5 `thm:modules:generalised-eigenspaces`** (theorem; P). (i) Let $V$ be a finite-dimensional vector space over a field $F$ and
$\T\subset\End_F(V)$ a commutative subalgebra such that the characteristic polynomial of every $t\in\T$ splits over $F$. Then
$V=\bigoplus_\varphi V(\varphi)$, the sum over the $F$-algebra homomorphisms $\varphi\colon\T\to F$ ("systems of eigenvalues"), with
$V(\varphi)=\{v:(t-\varphi(t))^{\dim V}v=0\ \forall t\in\T\}\ne0$; the projection onto $V(\varphi)$ is the idempotent $e_\varphi\in\T$ of 10.1; every $V(\varphi)$
contains a nonzero common eigenvector ($tv=\varphi(t)v$ for all $t$); every $\T$-stable subspace $W$ satisfies $W=\bigoplus_\varphi(W\cap V(\varphi))$.
(ii) (Integral version.) Let $\mathcal O$ be a complete DVR with fraction field $K$, $L$ a lattice, $\T\subset\End_{\mathcal O}(L)$ a commutative
subalgebra (finite free over $\mathcal O$), and suppose the eigenvalues of $\T$ on $V=L\otimes K$ lie in $K$. Then every $\varphi\colon\T\to K$
takes values in $\mathcal O$ (eigenvalues are integral over $\mathcal O$), $\mathfrak m_\varphi=\varphi^{-1}(\varpi\mathcal O)$ is a maximal ideal of $\T$, $\mathfrak m_\varphi=\mathfrak m_\psi$ iff
$\varphi\equiv\psi\pmod\varpi$ on $\T$, and $e_{\mathfrak m}L\otimes K=\bigoplus_{\varphi:\mathfrak m_\varphi=\mathfrak m}V(\varphi)$. (If the eigenvalues are not in $K$, replace $\mathcal O$ by the
ring of integers of a finite extension, Chapter 7.) Reference: Lang XIV.2 (check); DF 12.3; DDT Section 4. Paper: Lemma
lem:crit ("$\T\otimes\Q=\Q\times\T'$ with $\T'$ acting faithfully on $f^\perp$"), Theorem thm:twist ("$g^\perp$, the $\T$-stable complement of the
$g$-line (the sum of the generalised eigenspaces of the other systems of eigenvalues)"), Theorem thm:quant Step 1 ("the
generalised eigenspace of $\pi$", "the $\mathfrak m$-component of $S_2(\Gamma_0(N);\Zl)$ is the sum of the line of $g^S$ and of generalised
eigenspaces ..."), PLAN.md scope ("generalised eigenspaces of commuting operators").

**10.6 `prop:modules:idempotent-congruence`** (proposition; P). In 10.5(ii) let $\mathfrak m$ be a maximal ideal of $\T$ and $e=e_{\mathfrak m}$. (i) $e$ maps
$L$ into $L$ and every $\T$-stable subspace $W\subset V$ into itself, and fixes $V(\varphi)$ pointwise for $\mathfrak m_\varphi=\mathfrak m$. (ii) If $x\in V(\varphi)\cap L$
with $\mathfrak m_\varphi=\mathfrak m$, $y\in L\cap W$, and $x\equiv y\pmod{\varpi^tL}$, then $x\equiv ey\pmod{\varpi^tL}$ with $ey\in L\cap W\cap e V$. Reference: elementary.
Paper: Theorem thm:quant Step 1 ("projecting $h$ to the $\mathfrak m$-component (an idempotent of $\T_\ell$, so the projection stays in the
complement and the congruence survives) we may take $h$ in the sum of the generalised eigenspaces above").

**10.7 `prop:modules:semisimple-operators`** (definition and proposition; P, with (iv) R). Let $A\in\End_F(V)$, $\dim V<\infty$. (i) $A$ is
*semisimple* if every $A$-stable subspace has an $A$-stable complement; for $F$ perfect (characteristic $0$ or finite) this holds iff
the minimal polynomial of $A$ is squarefree iff $A$ is diagonalisable over $\overline F$. (ii) If $V$ has a cyclic vector for $A$ (some $v$
with $v,Av,\dots,A^{n-1}v$ a basis), the minimal polynomial equals the characteristic polynomial, so $A$ is not semisimple as soon as
the characteristic polynomial has a repeated root. (iii) A commutative subalgebra $\T\subset\End_F(V)$ is reduced iff each of its
elements is semisimple (by 10.1(iii) and (i)); if one $t\in\T$ is not semisimple, its nilpotent part is a nonzero nilpotent element of $\T$.
(iv) Jordan-Chevalley: $A=A_s+A_n$ with $A_s$ semisimple, $A_n$ nilpotent, commuting, both polynomials in $A$ (stated). (v) Example (the
linear algebra of $U_p$ on oldforms; checked symbolically): on $V$ with basis $v_0,\dots,v_e$ let $Uv_j=v_{j-1}$ for $j\ge1$ and
(a) $Uv_0=av_0-pv_1$ (with $p\ne0$): the characteristic polynomial is $X^{e-1}(X^2-aX+p)$, $v_e$ is a cyclic vector, so for $e\ge3$ the
eigenvalue $0$ has a single Jordan block of size $e-1\ge2$ and $U$ is not semisimple; nevertheless every eigenvalue has an eigenvector,
e.g. $\ker U\ni v_0-av_1+pv_2$ for $e\ge2$; (b) $Uv_0=av_0$: characteristic polynomial $X^e(X-a)$, not semisimple for $e\ge2$, with
$U(v_0-av_1)=0$ for $e\ge1$. The modular meaning ($v_j=h(p^jz)$; the depleted forms) is Chapter 13. Reference: DF 12.3; Lang
XIV.2. Paper: Lemma lem:old ("The operator $U_p$ is not semisimple on this span when $0$ is a repeated eigenvalue, but each listed
eigenvalue has an eigenvector"), Theorem thm:quant Step 1 ("the operators $U_q$ ... have the eigenvalue $0$ with multiplicity one"),
PLAN.md scope ("semisimple versus non-semisimple operators"); 11.1 and Part 8, point 1 (the full Hecke algebra need not be
reduced).

**10.8 `lem:modules:common-eigenvector`** (lemma; P). (i) Commuting operators $A_1,\dots,A_k$ on a nonzero finite-dimensional space
over an algebraically closed field have a common eigenvector; more precisely, for every tuple $(\lambda_i)$ whose joint generalised
eigenspace $V(\lambda)=\bigcap_i\ker(A_i-\lambda_i)^{\dim V}$ is nonzero, $V(\lambda)$ contains a common eigenvector, and it can be chosen to be an
eigenvector of every element of any commutative algebra $\T$ containing the $A_i$ (apply 10.5(i) to $\T$ acting on the $\T$-stable
$V(\lambda)$). (ii) If $V=V_1\otimes\cdots\otimes V_k$ and $A_i$ acts on the $i$-th factor, the joint generalised eigenspace for $(\lambda_i)$ is
$V_1(\lambda_1)\otimes\cdots\otimes V_k(\lambda_k)$, nonzero iff each $\lambda_i$ is an eigenvalue of $A_i$ on $V_i$. Reference: elementary; DF 12.3.
Paper: Lemma lem:old ("Since $V$ is the tensor product of these local spaces and $\T$ is commutative, for every choice of one such
eigenvalue $\mu_p$ at each $p\mid N/M$ there is a common eigenform $g\in V\otimes\overline\Q$ of all of $\T$").

### Section 11. Congruence ideals, Gorenstein algebras, and the ingredients of Lemma lem:ddt417

**11.1 `prop:modules:congruence-ideal`** (definition and proposition; P). Let $\mathcal O$ be a DVR with fraction field $K$, $\T$ a
commutative $\mathcal O$-algebra finite and free as an $\mathcal O$-module, $\pi\colon\T\to\mathcal O$ a surjective $\mathcal O$-algebra homomorphism, $\wp=\ker\pi$,
$I=\Ann_\T(\wp)$, and $\eta=\pi(I)$, the *congruence ideal* of $\pi$; the *congruence module* is $\T/(\wp+I)\simeq\mathcal O/\eta$ (1.3(iv)). Then:
(i) $I\ne0$ (in $\T_K$ the maximal ideal $\wp_K$ has a nonzero annihilator, 10.1, and $I=\T\cap\Ann_{\T_K}(\wp_K)$).
(ii) The following are equivalent: (a) $\eta\ne0$; (b) $\wp\cap I=0$; (c) the local factor of $\T_K$ through which $\pi_K$ factors is $K$
itself, i.e. $\T_K=K\times\T'_K$ with $\pi_K$ the first projection. *Proof of (a)$\Rightarrow$(b) in two lines:* choose $t\in I$ with $\pi(t)$
generating $\eta$; for $x\in\wp\cap I$, $\pi(t)x=tx+(\pi(t)-t)x$, where $tx\in I\wp=0$ and $(\pi(t)-t)x\in\wp I=0$ (as $\pi(t)-t\in\wp$); so
$\pi(t)x=0$ and $x=0$, $\T$ being torsion-free. (b)$\Rightarrow$(a): if $\eta=0$ then $I\subset\wp$, so $\wp\cap I=I\ne0$ by (i). (a)$\Leftrightarrow$(c): if
the factor $A$ of $\T_K$ is not a field, $\Ann_A(\mathfrak m_A)\subset\mathfrak m_A$, so $\pi(I)=0$; if it is $K$, the idempotent $e_\pi=(1,0)$ has a nonzero
multiple $ae_\pi\in\T$, which lies in $I$ and has $\pi(ae_\pi)=a$.
(iii) If $\eta\ne0$: $\pi|_I\colon I\to\eta$ is an isomorphism (so $I$ is free of rank one over $\mathcal O$); $\Ann_\T(I)=\wp$ (if $xI=0$ then
$\pi(x)\pi(t)=0$); $I=\T\cap(K\times0)$ and $\wp=\T\cap(0\times\T'_K)$; and $\eta=\{a\in\mathcal O:ae_\pi\in\T\}$, the "denominator" of the idempotent $e_\pi$.
(iv) If $\T_K$ is reduced, (c) holds automatically; it can fail to be reduced (10.7(v) and Part 8, point 1), and then (c) must
be checked directly (for a newform it is multiplicity one, Chapter 13).
(v) Compatibility: if $\mathcal O$ is complete and $\mathfrak m=\mathfrak m_\pi$, then $\ker\pi=\wp_{\mathfrak m}\times\prod_{\mathfrak m'\ne\mathfrak m}\T_{\mathfrak m'}$ and
$\Ann_\T(\ker\pi)=\Ann_{\T_{\mathfrak m}}(\wp_{\mathfrak m})\times0$, so $\eta(\T,\pi)=\eta(\T_{\mathfrak m},\pi|_{\T_{\mathfrak m}})$: **the congruence ideal is computed in $\T_{\mathfrak m}$**. The other
factors $\T_{\mathfrak m'}$ lie in $\ker\pi$, not in the annihilator (Part 8, point 2). For a flat extension $\mathcal O\to\mathcal O'$ of DVRs (e.g. $\Z_{(\ell)}\to\Zl$),
$\eta(\T\otimes\mathcal O',\pi\otimes\mathcal O')=\eta\mathcal O'$ (3.4(iii)).
Reference: DDT Section 4 (cite the section; Lemma 4.17 for the context); Hida81; Ribet83. Paper: Lemma lem:crit ("$r$
generates the congruence ideal $\phi_f(J)=\phi_f(\Ann_\T I)$"; "$I\cap J=0$"), Lemma lem:ddt417 ("$\wp\cap I=0$"; important_notes.md point
19), Lemma lem:hecke ("the congruence ideal is computed in $\T_{\mathfrak m}$"), Theorem thm:quant Step 1 ($\eta^{\mathrm{Hecke}}(g^S)$ computed in $\T_{\mathfrak m}$),
Section 6 map row (Hida's congruence modules).

**11.2 `ex:modules:toy-congruence`** (examples; P, all checked). (a) $\T_r=\{(a,b)\in\mathcal O^2:a\equiv b\pmod{\varpi^r}\}\simeq\mathcal O[x]/(x(x-\varpi^r))$ (with
$x=(\varpi^r,0)$), $\pi(a,b)=a$: $\wp=0\times\varpi^r\mathcal O$, $I=\varpi^r\mathcal O\times0$, $\eta=\varpi^r\mathcal O$, congruence module $\mathcal O/\varpi^r$, $e_\pi=(1,0)=x/\varpi^r$:
"two eigenforms congruent modulo $\varpi^r$". (b) $\Z[x]/(x^2-4)$, $\pi(x)=2$: $I=\Z(x+2)$, $\eta=4\Z$, $e_\pi=(x+2)/4$, congruence module $\Z/4$.
(c) $\T_3^{\flat}=\{(a,b,c)\in\mathcal O^3:a\equiv b\equiv c\pmod\varpi\}$, $\pi$ the first coordinate: $\eta=\varpi\mathcal O$ (three pairwise congruent
eigenforms). (d) $\mathcal O[\varepsilon]/(\varepsilon^2)$, $\pi(\varepsilon)=0$: $\wp=I=\mathcal O\varepsilon$, $\eta=0$, $\wp\cap I\ne0$. (e) $\Z[x]/(x^2(x-1))$: for $\pi(x)=0$ the factor of
$\T_\Q$ is $\Q[x]/(x^2)$, $I=\Z(x-x^2)$ and $\eta=0$; for $\pi(x)=1$, $I=\Z x^2$, $\eta=\Z$, congruence module $0$. Paper: Lemma lem:crit,
Lemma lem:ddt417 (models), Exercises 8, 9.

**11.3 `prop:modules:ddt-ingredients`** (proposition, the module ingredients of Lemma lem:ddt417; P). In the setting of 11.1
with $\eta\ne0$, let $L$ be a $\T$-module that is free of finite rank over $\mathcal O$, with a perfect $\mathcal O$-bilinear pairing for which every
element of $\T$ is self-adjoint. Then: (i) $L[\wp]$ and $L[I]$ are saturated in $L$ (5.5); (ii) $L[\wp]\cap L[I]=0$ (an element killed by
$\wp+I\ni\pi(t)$ is killed by $\pi(t)\ne0$); (iii) $L[\wp]^\perp=L[I]$ and $L[I]^\perp=L[\wp]$ (for $y\in L[I]$, $x\in L[\wp]$:
$\pi(t)\langle x,y\rangle=\langle tx,y\rangle=\langle x,ty\rangle=0$, using $(\pi(t)-t)x\in\wp x=0$; conversely if $y\perp L[\wp]$ then for every $s\in I$ and $z\in L$,
$\langle sy,z\rangle=\langle y,sz\rangle=0$ since $sz\in L[\wp]$, so $sy=0$; the second equality by 9.2(ii)); (iv) more generally $(\mathfrak aL)^\perp=L[\mathfrak a]$ for every
ideal (9.5(ii)); (v) if $L\simeq\T^r$ as $\T$-modules, then $L[\wp]=I^r$ (free of rank $r$ over $\mathcal O$, by 11.1(iii)), $L[I]=\Ann_\T(I)^r=\wp^r$, and
$L/(L[\wp]\oplus L[I])\simeq(\T/(\wp+I))^r\simeq(\mathcal O/\eta)^r$. The assembly (the quotient $Q=L/(L[\wp]\oplus L[I])$ is killed by $\eta$, is generated by
$d=\rank L[\wp]$ elements, and is $\coker(L[\wp]\to\Hom(L[\wp],\mathcal O))$ of length $v(\Delta)$ by 9.3; hence $d\,v(\eta)\ge v(\Delta)$, with
equality when $L$ is free) is Lemma lem:ddt417, proved in Chapter 20. Reference: DDT, Lemma 4.17 and Section 4 (cite the
section). Paper: Lemma lem:ddt417 (every sentence of its proof except the counting), Lemma lem:hecke, Theorem thm:quant
Step 2, PLAN.md scope ("every ingredient: Ann, $L[\wp]$, saturation, $L[\wp]^\perp=L[I]$, the dual map").

**11.4 `def:modules:gorenstein`** (definition and proposition; P for (i) to (iii), R for (iv)). Let $\T$ be a commutative $\mathcal O$-algebra,
finite and free as an $\mathcal O$-module, and $\T^\vee=\Hom_{\mathcal O}(\T,\mathcal O)$ with $(t\varphi)(u)=\varphi(tu)$. $\T$ is *Gorenstein* if $\T^\vee$ is free of rank one
as a $\T$-module. (i) Equivalently there is a perfect $\mathcal O$-bilinear pairing $\T\times\T\to\mathcal O$ with $\langle st,u\rangle=\langle s,tu\rangle$ (take
$\langle s,t\rangle=\lambda(st)$ for a generator $\lambda$ of $\T^\vee$). (ii) For $\mathcal O$ complete, $\T$ is Gorenstein iff each local factor $\T_{\mathfrak m}$ (10.3) is; for $\T$ local with
maximal ideal $\mathfrak m$ and residue field $k_\T$, $\T$ is Gorenstein iff $\dim_{k_\T}(\T/\varpi\T)[\mathfrak m]=1$ (the socle of $\T/\varpi\T$ is a line) iff
$\dim_{k_\T}\T^\vee/\mathfrak m\T^\vee=1$ (proof: $\T^\vee/\varpi\T^\vee=\Hom_k(\T/\varpi\T,k)$ and $\T^\vee/\mathfrak m\T^\vee$ is dual to the socle; a cyclic $\T^\vee$ is free since $\T^\vee$
and $\T$ have the same $\mathcal O$-rank). (iii) Examples (checked): $\mathcal O[x]/(f)$ for monic $f$ is Gorenstein (a generator of $\T^\vee$ is the
coefficient of $x^{n-1}$); $\T_r$ of 11.2(a) is Gorenstein (socle dimension $1$; with $\lambda(a,b)=(a-b)/\varpi^r$ the Gram matrix of $\lambda(st)$ in
the basis $(1,1),(\varpi^r,0)$ is $\begin{psmallmatrix}0&1\\1&\varpi^r\end{psmallmatrix}$, determinant $-1$); $\T_3^\flat$ of 11.2(c) is not (socle of dimension $2$),
although $\T_3^\flat\otimes K=K^3$ is reduced; $\mathcal O[\varepsilon]/(\varepsilon^2)$ is Gorenstein and not reduced. (iv) Complete intersections are
Gorenstein; for $\T$ local Gorenstein and $\pi$ as in 11.1, Wiles's numerical criterion relates $\eta$ to $\wp/\wp^2$ (stated with
pointer to Chapter 20). Reference: Mazur77, Chapter II, Section 15 (check); Eisenbud Chapter 21; Tilouine97; DDT
Section 4. Paper: Remark rem:free ("the localised Hecke algebra is then Gorenstein"), PLAN.md scope ("Gorenstein rings
(definition: finite free $\mathcal O$-algebra $\T$ with $\Hom_{\mathcal O}(\T,\mathcal O)$ free of rank one over $\T$)"), Section 6 map row (multiplicity one,
freeness, Gorenstein).

**11.5 `thm:modules:mazur-freeness`** (theorem, a freeness criterion in the style of Mazur; P). Let $\T$ be a local commutative
$\mathcal O$-algebra, finite and free over $\mathcal O$, with maximal ideal $\mathfrak m$ and residue field $k_\T$, and let $L$ be a $\T$-module, free of finite
rank over $\mathcal O$, with a perfect $\mathcal O$-bilinear pairing for which $\T$ is self-adjoint (so $L\simeq L^\vee$ as $\T$-modules). Suppose
(a) $\dim_{k_\T}L/\mathfrak mL=d$ and (b) $\rank_{\mathcal O}L=d\cdot\rank_{\mathcal O}\T$. Then $L\simeq\T^d$ and $\T$ is Gorenstein. (Proof: by Nakayama there is a surjection
$\T^d\to L$, an isomorphism by (b) since both are free over $\mathcal O$ of the same rank; then $(\T^\vee)^d\simeq L^\vee\simeq L\simeq\T^d$, so
$\dim\T^\vee/\mathfrak m\T^\vee=1$ and 11.4(ii) applies.) In the Hecke application (Chapter 14): $d=2$; (a) is "$J_0(N)[\mathfrak m]$ is
two-dimensional over $\T/\mathfrak m$" read through Pontryagin duality (8.1, 8.2), and (b) holds because $H^1(X_0(N),\Q)\otimes\C\simeq S_2\oplus\overline{S_2}$
and $S_2(\Gamma_0(N))\simeq\Hom(\T,\C)$ by 9.6, compatibly with the idempotent decomposition 10.3. Reference: Mazur77, Chapter II,
Section 15 (check); Tilouine97; DDT Section 4 (cite the section). Paper: Remark rem:free ("since the localised Hecke algebra is
then Gorenstein and the Tate module is free of rank two"), the equality clauses of Lemma lem:ddt417, Lemma lem:hecke and
Theorem thm:main, Theorem thm:quant Step 4.

**11.6 `rem:modules:ddt417-preview`** (remark with checked examples; R for the lemma, P for the examples). Statement of
the paper's Lemma lem:ddt417 in the notation of 11.1 and 11.3 (no proof; Chapter 20), with the table: which item supplies which
step (saturation 5.5 and 11.3(i); directness 11.3(ii); $L[\wp]^\perp=L[I]$ 11.3(iii); the dual map and its cokernel 9.3; the Gram
determinant 9.1, 9.4; equality 11.3(v)). Checks of the statement on the toy algebra $\T_r$ (all computed): $L=\T_r$ with
$\langle s,t\rangle=\lambda(st)$: $L[\wp]=\mathcal O\cdot(\varpi^r,0)$, $d=1$, $\Delta=\varpi^r$, so $d\,v(\eta)=r=v(\Delta)$ (free case, equality); $L=\mathcal O^2$ with $\T_r$ acting
diagonally and the standard pairing: $L[\wp]=\mathcal Oe_1$, $\Delta=1$, $v(\Delta)=0<r$ (strict inequality; $L$ is not free over $\T_r$); $L=\T_r^2$ with
the alternating pairing $\lambda(x_1y_2-x_2y_1)$: $d=2$, $\Delta=\varpi^{2r}=\eta^2$ (the shape of Lemma lem:hecke). Also: when $\eta=0$ the
inequality $\eta^d\subset\Delta\mathcal O$ is trivial, and if moreover $L$ is free over $\T$ then $\Delta=0$ ($I\subset\wp$ gives $I\cdot I=0$, so the
pairing vanishes on $L[\wp]=I^r$), so the hypothesis $\Delta\ne0$ of the lemma already forces $\eta\ne0$ in the free case. Paper:
Lemma lem:ddt417, Lemma lem:hecke, Section 6 map row (DDT Lemma 4.17, Wiles's numerical criterion).

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200). The card lists all 64 items of Part 2
(numbered 3.1 to 3.64 in the book), about 190 lines, not counted.

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2, stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1.2 ($\Tam_p$ as a Fitting ideal); lem:tamfactor; lem:fpr; thm:main, thm:dfg37, rem:ns (lengths); lem:dfg21 (Pontryagin duals); lem:h0 ($W$, $\ell^k$-torsion, cyclicity); lem:crit (dualising, congruence module, $\T\otimes\Q=\Q\times\T'$); lem:ddt417 (every ingredient); lem:hecke ($\T_{\mathfrak m}$, idempotents, restricted pairing); rem:free (Gorenstein, freeness); thm:quant Steps 1, 2 (generalised eigenspaces, idempotents); lem:old (non-semisimple $U_p$, common eigenforms); lem:IV (modules over $\Z_3[\zeta_3]$); Section 4.1 (alternating Gram determinant) | 45 |
| 1 | Modules, submodules, quotients, homomorphisms | conventions C1 to C10 as `convention` environments; 1.1 to 1.3; the running examples announced with forward `\Cref`s | 110 |
| 2 | Exact sequences, the snake lemma, sums and products, free and projective modules | 2.1 to 2.7; the snake lemma with the diagram (`tikz-cd` if the preamble has it, else an `array`); `paperlink` for lem:crit and lem:ddt417 (2.2) | 170 |
| 3 | Hom and tensor product; flatness | 3.1 to 3.4; the examples of 3.2(v) in a small table; `paperlink` for lem:crit over $\Zl$ and lem:hecke (3.4(iii)) | 170 |
| 4 | Noetherian rings, Nakayama, localisation, local rings | 4.1 to 4.5; `paperlink` for rem:free and lem:h0 (4.3) | 180 |
| 5 | Modules over a PID; lattices and saturation | 5.1 to 5.8; worked Smith forms (5.2 examples); `paperlink` for lem:IV (5.4(iii)), lem:crit (5.7, 5.8), lem:ddt417 (5.5) | 240 |
| 6 | DVRs, completions, $\Zl$, $\Ql$, $\Qlmod$ | 6.1 to 6.6; `warning` that the analytic theory of $\Q_p$ is Chapter 7; `paperlink` for lem:dfg21 ("killed by $2$") | 170 |
| 7 | Length, annihilators, Fitting ideals | 7.1 to 7.7; the examples of 7.7 as a `booktabs` table (presentation, module, $\Fitt$, $\Ann$, length); `paperlink` for Section 1.2 and lem:tamfactor; `warning` $\Fitt\ne\Ann$ | 190 |
| 8 | Pontryagin duality | 8.1 to 8.4; `paperlink` for lem:dfg21, lem:h0 | 130 |
| 9 | Pairings | 9.1 to 9.6; the $\begin{psmallmatrix}9&1\\1&0\end{psmallmatrix}$ example and the non-saturated counterexample; `paperlink` for lem:ddt417 (9.3), Section 4.1 (9.4, 9.5), lem:crit (9.6) | 200 |
| 10 | Finite free algebras over a DVR; idempotents; generalised eigenspaces | 10.1 to 10.8; the level-$23$ example worked mod $11$, $5$, $2$, $3$; the shift-operator matrix of 10.7(v); `paperlink` for lem:hecke, thm:quant Step 1, lem:old | 210 |
| 11 | Congruence ideals and Gorenstein algebras | 11.1 to 11.6; the toy algebras of 11.2 in one table ($\wp$, $I$, $\eta$, $e_\pi$, Gorenstein or not); the item-to-step table of 11.6; `paperlink` for lem:ddt417, rem:free | 180 |
| 12 | Exercises | the 17 exercises of Part 4 | 130 |
| 13 | Notes and references | Atiyah-Macdonald, Dummit-Foote, Lang, Eisenbud, Serre (Local Fields; Course in Arithmetic), NSW, Weibel, DDT Section 4, Hida81, Mazur77, Tilouine97; which numbers were cited and which were checked; historical remark on Fitting (1936) and on Mazur's multiplicity one argument | 40 |
| | **total** | | **2,165** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| modules over commutative rings, submodules, quotients, homomorphisms | 1.1, 1.2, 1.3 |
| exact sequences | 2.1, 2.2 |
| the snake lemma | 2.3 (and 2.4) |
| Hom and tensor product: definitions, universal properties | 3.1, 3.2 |
| right exactness of the tensor product; flatness of localisation | 3.3, 3.4, 4.5(ii) |
| direct sums and products | 2.5 |
| free and projective modules | 2.6, 2.7, 4.3(v), 5.1 |
| f.g. modules over a PID: structure theorem, elementary divisors | 5.2, 5.3, 5.6 |
| torsion and torsion-free | 5.4, 6.3(ii) |
| saturated sublattices ($L$ saturated if $M/L$ torsion-free) | 5.5, 5.6, 9.2, 11.3(i) |
| Nakayama's lemma | 4.2, 4.3, 6.6(iv) |
| localisation at a prime and at a maximal ideal; local rings | 4.4, 4.5, 10.3(ii) |
| DVRs: definition, uniformiser, valuation, ideals are powers of the maximal ideal | 6.1, 6.2, 6.3 |
| completions and $\Zl$, $\Ql$, $\Qlmod$ (coordinated with Chapter 7) | 6.4, 6.5, 6.6 |
| length over a DVR and over a local ring | 7.1, 7.2 |
| Fitting ideals: presentations; over a DVR $\Fitt=\varpi^{\mathrm{length}}$; direct sums; quotients | 7.4, 7.5, 7.6, 7.7 |
| annihilators | 7.3, 11.1 |
| Pontryagin duality for finite abelian groups | 8.1 |
| Pontryagin duality for (f.g. $\Zl$-modules, discrete torsion $\Zl$-modules) via $\Hom(-,\Qlmod)$ | 8.2, 8.4, 6.5 |
| the duality between $T$ and $T\otimes\Qlmod$ | 8.3 |
| perfect pairings, the Gram determinant, basis independence of its valuation | 9.1 |
| saturated $L$ of rank $d$: cokernel of $L\to\Hom(L,\mathcal O)$ has order $\#\mathcal O/(\text{Gram det})$ | 9.3 |
| alternating pairings; rank-two Gram determinant is a square | 9.4 |
| adjoints with respect to a pairing | 9.5, 9.6 |
| finite free algebras over a DVR, maximal ideals, localisation; $\T\otimes\Zl$ a product of local rings; idempotents | 10.1, 10.2, 10.3, 10.4 |
| generalised eigenspaces of commuting operators | 10.5, 10.6, 10.8 |
| semisimple versus non-semisimple operators | 10.7 |
| Gorenstein rings: definition; Gorenstein plus a perfect self-adjoint pairing gives freeness | 11.4, 11.5 |
| ingredients of Lemma lem:ddt417: Ann, $L[\wp]$, saturation, $L[\wp]^\perp=L[I]$, the dual map | 7.3, 11.1, 11.3, 5.5, 9.3, 9.4, 11.6 |
| Section 6 row: Tamagawa factor $\Tam_p(M)=\Fitt(H^1(I_p,M)_{\tors})^G$ (with Chapters 16, 18) | 7.4, 7.5, 7.6, 7.7 |
| Section 6 row: multiplicity one, freeness of $H^1(X_0(N),\Zl)_{\mathfrak m}$ over $\T_{\mathfrak m}$, Gorenstein, $J_0(N)[\mathfrak m]$ (with Chapters 14, 20) | 4.3, 10.3, 11.4, 11.5 |
| Section 6 row: Hida's congruence modules, Wiles's numerical criterion, DDT Lemma 4.17 (with Chapter 20) | 5.8, 11.1, 11.2, 11.3, 11.6 |
| Section 6 row: Fitting ideals, lengths, Pontryagin duality, Gram determinants, saturated sublattices | 7.1 to 7.7, 8.1 to 8.4, 9.1 to 9.4, 5.5 |
| hook: Tamagawa factor as a Fitting ideal (Section 1.2, Lemma lem:tamfactor, Lemma lem:fpr) | 7.6, 7.7, 7.2 |
| hook: lengths of Selmer groups (Theorem thm:main; also thm:dfg37, rem:ns, conj:euler) | 7.1(iii), 7.2, 8.1(v), 8.2 |
| hook: Lemma lem:ddt417 | 5.5, 9.1, 9.3, 9.4, 9.5, 11.1, 11.3, 11.6 |
| hook: Lemma lem:hecke | 3.4(iii), 9.5(iii), 10.3, 10.4, 11.1(v) |
| hook: Remark rem:free (freeness, Gorenstein) | 4.3, 11.4, 11.5 |
| hook: Lemma lem:crit ($\T/(I+J)$) | 1.3(iv), 2.2, 3.4, 5.7, 5.8, 9.6, 10.1, 11.1 |
| hook: Lemma lem:h0 ($\Qlmod$-modules, $\ell^k$-torsion) | 4.3(iv), 6.3(v), 8.3, 8.4 |
| hook: Pontryagin duals in Lemma lem:dfg21 | 8.1, 8.2, 6.4(iii) ($H^1(\R,T^D)$ killed by $2$) |
| hook: proof of Theorem thm:quant Step 1 (idempotents of $\T_\ell$, generalised eigenspaces) | 10.3, 10.5, 10.6, 11.1(v) |
| also: Lemma lem:IV ($T$ free of rank one over $\Z_3[\zeta_3]$) | 5.4(iii), 6.3, 1.2(c) |
| also: Lemma lem:old (non-semisimple $U_p$; common eigenform for chosen eigenvalues) | 10.7(v), 10.8 |
| also: Theorem thm:twist ($g^\perp$ as a sum of generalised eigenspaces) | 10.5 |
| also: Section 4.1 ($\hat\delta_!$ perfect, alternating, self-adjoint Hecke operators; Gram determinant $(\eta^\Sigma)^2$) | 9.4, 9.5(iv) |
| also: Theorem thm:quant Step 2 and Step 4 (Lemma lem:ddt417 without freeness; free case) | 11.3, 11.5 |
| what Chapters 6, 14, 16, 20, 21 assume from Chapter 3 (Part 5) | 4.1, 4.5, 5.4, 6.1, 6.3, 6.4, 6.5, 6.6, 7.1, 7.6, 8.2, 9.3, 10.3, 10.4, 11.3, 11.5 |

### 4.2 Exercises (Section 12 of the chapter), graded from easy to harder

1. Compute $\Z/m\otimes\Z/n$, $\Q\otimes\Z/n$, $\Zl\otimes\Z/n$, $\Qlmod\otimes\Z/n$, $\Hom(\Z/m,\Z/n)$ and $\Hom(\Qlmod,\Z/\ell^k)$. Show that $\Hom(\Z/2,-)$ is not
   right exact and $-\otimes\Z/2$ is not left exact on $0\to\Z\xrightarrow2\Z\to\Z/2\to0$ (3.1, 3.2, 3.3).
2. Prove corollary (a) of the snake lemma: for $0\to A\to B\to C\to0$ and $n\in R$ there is an exact sequence
   $0\to A[n]\to B[n]\to C[n]\to A/n\to B/n\to C/n\to0$. Apply it to $0\to T\to V\to W\to0$ with $n=\ell^k$ to get $W[\ell^k]\simeq T/\ell^kT$ (8.3(ii)).
3. Find the Smith normal form, the invariant factors, the elementary divisors, the Fitting ideal and the annihilator of the
   abelian group with relation rows $(2,4,4)$, $(-6,6,12)$, $(10,-4,-16)$; then of its tensor product with $\Z_2$ and with $\Z_3$
   (answers: $\Z/2\oplus\Z/6\oplus\Z/12$; $\Fitt=(144)$, $\Ann=(12)$; over $\Z_2$: $\Z/2\oplus\Z/2\oplus\Z/4$, $\Fitt=16\Z_2$; over $\Z_3$:
   $\Z/3\oplus\Z/3$, $\Fitt=9\Z_3$).
4. (Check the paper's claim in Lemma lem:IV.) Let $T$ be free of rank $2$ over $\Z_3$ with an automorphism $\sigma$ satisfying
   $\sigma^2+\sigma+1=0$. Show that $T$ is a torsion-free, hence free, module of rank one over $\Z_3[X]/(X^2+X+1)$ (5.4(iii), with the DVR
   property from Chapter 6), that $T/3T\simeq\Z_3[\zeta_3]/(\pi^2)$, and that the fixed vectors of $\sigma$ on $T/3T$ form a line.
5. (Check the paper's claim in Lemma lem:tamfactor.) Show that $\Fitt_{\Zl}(\Z/\ell^v\oplus\Z/\ell^m)=\ell^{v+m}\Zl$ while its annihilator is
   $\ell^{\max(v,m)}\Zl$, and that $v_\ell$ of the Fitting ideal of the module $\{x\bar e+y\bar h\}$ of the lemma's proof is $v_\ell(n)+\min(v_\ell(n),v_\ell(q-1),v_\ell(c'))$
   once one knows its order (7.6). Why would the formula be wrong with $\Ann$ in place of $\Fitt$?
6. Show that Fitting ideals are multiplicative in short exact sequences of finite $\Zl$-modules, but not over $k[\varepsilon]/(\varepsilon^2)$ (7.5(vi)).
   Compute $\Fitt$ and $\Ann$ of $\Z[x]/(2,x)$ and of its square.
7. (Saturation is necessary.) On $\Z^2$ with Gram matrix $\begin{psmallmatrix}9&1\\1&0\end{psmallmatrix}$ compute $L'^\perp$ for $L'=\Z e_1$ and the index of $L'\oplus L'^\perp$;
   then show that for the standard pairing and $L'=\Z\cdot3e_1$ the index is $3$ while the Gram determinant is $9$. Check the paper's claim
   in Lemma lem:ddt417 that the cokernel of $L[\wp]\to\Hom(L[\wp],\mathcal O)$ "has order $\#\mathcal O/\Delta$", and say exactly where saturation enters.
8. (Check the paper's claim in Section 4.1.) Show that an alternating pairing on a free module of rank $2$ has Gram determinant
   $a^2$ with $a\mathcal O$ the ideal of values, and that no perfect alternating pairing exists in odd rank. Compute the Pfaffian identity
   $\det G=\operatorname{Pf}(G)^2$ for rank $4$.
9. (The toy congruence.) For $\T_r=\{(a,b)\in\Zl^2:a\equiv b\bmod\ell^r\}$ and $\pi(a,b)=a$ compute $\wp$, $I$, $\eta$, $\T_r/(\wp+I)$ and the
   denominator of the idempotent $(1,0)$; verify the inequality of Lemma lem:ddt417 for $L=\T_r$ (pairing $\lambda(st)$, equality), for
   $L=\Zl^2$ with the diagonal action (strict) and for $L=\T_r^2$ with an alternating pairing ($\Delta=\eta^2$).
10. (Check the paper's claim in Lemma lem:ddt417 that $\wp\cap I=0$.) Show that $\wp\cap I=0$ iff $\eta\ne0$ (11.1(ii)); give the example
    $\mathcal O[\varepsilon]/(\varepsilon^2)$; show that when $\eta=0$ the inequality of the lemma is trivial and that a free $L$ then has $\Delta=0$.
11. (Check the paper's claim in Lemma lem:crit.) Let $\T$ act on $S$ with a perfect pairing $S\times\T\to\Z$ as in 9.6, and $I$, $J$ ideals
    with $I\cap J=0$ and $\T/I$, $\T/J$ torsion-free. Show that $S/(S[I]\oplus S[J])$ has the same order as $\T/(I+J)$. Work it out for
    $\T=\Z[x]/(x^2-4)$, $I=(x-2)$, $J=(x+2)$ (answer $4$), and interpret it as a congruence modulo $4$ between two "eigenforms".
12. (Check the paper's claim in Lemma lem:hecke that "the congruence ideal is computed in $\T_{\mathfrak m}$".) For $\T\otimes\Zl=\prod_{\mathfrak m'}\T_{\mathfrak m'}$
    and $\pi$ factoring through $\T_{\mathfrak m}$, show $\Ann(\ker\pi)=\Ann_{\T_{\mathfrak m}}(\wp_{\mathfrak m})\times0$. Do the other local factors lie in the
    annihilator, as the paper's sentence says, or in the kernel?
13. Idempotents: for $\T=\Z[x]/(x^2+x-1)$ show $\T\otimes\Z_{11}\simeq\Z_{11}\times\Z_{11}$ and compute the idempotent modulo $11^3$ by the
    iteration $e\mapsto3e^2-2e^3$ from $(x-3)/4$; show $\T\otimes\Z_5$, $\T\otimes\Z_2$, $\T\otimes\Z_3$ are local and $\Z_{(11)}[x]/(x^2+x-1)$ has no
    nontrivial idempotent although it has two maximal ideals above $11$.
14. (Non-semisimple $U_p$; check the paper's claim in Lemma lem:old.) For the operator $U$ of 10.7(v)(a) compute the characteristic
    polynomial, show that $v_e$ is a cyclic vector, and find an eigenvector for each eigenvalue; deduce that for $e\ge3$ the commutative
    algebra generated by $U$ is not reduced. (With Chapter 13: the full Hecke algebra of level $88$ acting on the span of
    $f_{11}(z),f_{11}(2z),f_{11}(4z),f_{11}(8z)$, where $a_2(f_{11})=-2$.)
15. Gorenstein: show that $\mathcal O[x]/(f)$ ($f$ monic) and $\T_r$ are Gorenstein and that $\{(a,b,c)\in\Zl^3:a\equiv b\equiv c\bmod\ell\}$ is not, by
    computing socles of the reductions mod $\ell$. Which of these "Hecke algebras" admit a free module $L$ with a perfect pairing for which
    they are self-adjoint and with $\dim L/\mathfrak mL=1$?
16. (Check the paper's use of Pontryagin duals in Lemma lem:dfg21 and the proof of Theorem thm:main.) For an exact sequence
    $0\to A\to B\to\bigoplus_iC_i^*\to D^*\to0$ of finite $\Zl$-modules show $\len B=\len A+\sum_i\len C_i-\len D$; deduce the paper's length identity
    when $H^0(\Q,W^D)=0$, and the corrected one of Remark rem:ns when it has length $h_\ell(E)$.
17. Show that $\Qlmod$ is an injective $\Zl$-module, that $\End_{\Zl}(\Qlmod)=\Zl$, that $(T\otimes\Qlmod)^*\simeq\Hom(T,\Zl)$ for $T$ free of finite rank, and
    that a $\Zl$-module killed by $2$ is zero when $\ell$ is odd (the paper: "$H^1(\R,T^D)$ is killed by $2$, so $H^1_f(\R,T^D)=0$ for $\ell$ odd").

## 5. Dependencies and forward pointers

Results from other chapters used here:
* PLAN.md Section 2 background: linear algebra (vector spaces, dimension, determinants, Cayley-Hamilton, Jordan form as a
  statement, bilinear forms and Gram matrices); elementary group theory.
* Chapter 1 (`ch:groups`): the structure theorem for finite abelian groups (its 4.1, generalised in 5.3), $\#A[n]=\#A/nA$ (its
  4.3), the $\ell$-primary decomposition (its 1.8, used in 6.4(v)), $\Zl$ as an inverse limit and $\GL_n(\Zl)$ as a profinite group
  (its 7.2, 7.4, used in 6.4, 6.6).
* Chapter 2 (`ch:rings`): rings, ideals, quotients (its 1.1 to 1.3), the two-ideal exact sequence and CRT (its 1.4, used in 2.2
  and 10.1), idempotents and products of rings (its 1.5, used in 1.2, 10.1, 10.3), prime and maximal ideals and residue
  characteristic (its 2.1, 2.2, used in 10.2), $\Z_{(p)}$ (its 2.4, the first DVR, 6.2), PIDs, UFDs, Euclidean domains (its 3.1, 3.2,
  used in Section 5), $v_p$ (its 11.1, C3), $\Ann_R(S)$ as a definition (its 1.2).
* Black boxes imported from later chapters (stated with a forward `\Cref`, used only in examples and `paperlink`s, never in a
  proof of a numbered result): $\Z_3[\zeta_3]$ is a DVR (Chapter 6, used in Exercise 4 and 1.2(c)); the Hecke algebra, the
  perfect pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$ and the oldform spaces (Chapters 12, 13, used in 9.6, 10.7(v), Exercises 11, 14); the
  cup product, $w_N$ and $J_0(N)[\mathfrak m]$ (Chapters 8, 14, used in 9.5(iv), 11.5); the extensions $\mathcal O_\lambda$ (Chapters 6, 7, used in
  10.5(ii)); $\Tam_p$, $H^1_f$, $W^D$ (Chapters 16 to 18, used in `paperlink`s only).

Forward pointers (chapters that use this one):
* Chapter 4 (`ch:reps`): Jordan-Holder (7.1(i)) for composition factors of representations; modules over $\Zl$ and $\Fl$, lattices,
  saturation (5.5) and free modules over a DVR (6.3) for $G$-stable lattices; $\Hom$ and $\otimes$ (3.1, 3.2) for $\Hom_G(V,W)=(V^\vee\otimes W)^G$ and
  $\ad$; Nakayama (4.3) for reduction mod $\ell$ of lattices.
* Chapter 6 (`ch:ant`): the DVR criterion (6.1, used at its 2.1, 4.7, 4.9), torsion-free modules over a DVR are free and the rank
  count (5.4(iii), 6.3, used at its 4.8), localisation (4.5, its 2.1), Noetherian rings (4.1), $\Zl$ (6.4), $R\otimes\Zl=\prod R_{\mathfrak m}$ (10.4,
  its 7.3(iv)), f.g. modules over a PID (5.3, its 1.4, 3.1).
* Chapter 7 (`ch:local`): $\Zl$ and $\Ql$ as algebraic objects (6.4), complete DVRs and idempotent lifting (6.1, 10.3), $\Qlmod$ (6.5).
* Chapters 8, 14 (`ch:curves`, `ch:moddeg`): perfect and alternating pairings, adjoints and twisted pairings (9.1, 9.4, 9.5) for the cup
  product on $H^1(X_0(N),\Z)$ and $\langle x,w_Ny\rangle$; the idempotent decomposition $H^1\otimes\Zl=\bigoplus H^1_{\mathfrak m}$ orthogonal for the
  pairing (9.5(iii), 10.3). Chapter 14 only (not Chapter 8, which does not use Gorenstein rings; the users are Chapters 14 and 20,
  important_notes.md B5): Gorenstein and the freeness criterion (11.4, 11.5) for Remark rem:free.
* Chapter 13 (`ch:hecke`): the Hecke algebra as a finite free $\Z$-algebra (10.2, 10.4), the algebra-module duality (9.6), generalised
  eigenspaces (10.5), the shift operator and non-semisimplicity of $U_p$ (10.7(v)), common eigenvectors (10.8).
* Chapter 15 (`ch:modgalrep`): Lemma lem:crit and Lemma lem:old (5.7, 5.8, 9.6, 10.1, 10.8, 11.1).
* Chapter 16 (`ch:cohomology`): the snake lemma (2.3), $\Hom$ and $\otimes$ (Section 3), the structure of f.g. $\Zl$-modules (5.3, 6.3),
  closedness of submodules and topological Nakayama (6.6), length and its additivity (7.1, 7.2), Fitting ideals of finite
  $\Zl$-modules and of direct sums (7.5, 7.6), Pontryagin duality, exactness, $A^{**}=A$, lengths preserved (8.1, 8.2), $W[\ell^k]=T/\ell^kT$
  (8.3), $\Qlmod$ injective (6.5(iv)), cyclic $\ell$-primary modules (8.4).
* Chapter 17 (`ch:galcoh`): $0\to T\to V\to W\to0$ and its torsion (8.3), Pontryagin duality (8.2), lengths (7.1).
* Chapter 18 (`ch:blochkato`): Fitting ideals over $\Zl$ (7.6) in the definition of $\Tam_p$ (Chapter 18, item 7.1) and in Lemma lem:fpr
  (Chapter 18, items 7.4, 7.5) and Lemma lem:tamfactor (Chapter 18, item 8.2); $T$, $V$, $W$ and their duals (8.3); lengths of Selmer groups
  (7.2, 8.2).
* Chapter 20 (`ch:congruence`): everything in Sections 9 to 11: congruence ideals (11.1, 11.2), the ingredients of Lemma lem:ddt417
  (11.3, 9.3, 9.4), the computation of the congruence ideal in $\T_{\mathfrak m}$ (11.1(v)), Gorenstein and freeness (11.4, 11.5), the congruence
  module of a decomposition (5.8), idempotents and generalised eigenspaces for Theorem thm:quant (10.3, 10.5, 10.6).
* Chapters 21, 22 (`ch:paper`, `ch:computation`): the card entries cited in Chapter 21's A2.7, A3.2, A4.3, A4.4, A4.10; PARI's
  `matsnf` (Smith normal form) and `mathnf` as computational counterparts of 5.2, 5.6 (Chapter 22, one sentence).

## 6. Notes for the writer

Conventions to fix (Section 1 of the chapter, as `convention` environments): C1 to C10 of Part 1. In addition:
* **Three duals.** Use $M^\vee$ for $\Hom_R(M,R)$, $M^*$ for the Pontryagin dual and never use ${}^*$ for the linear dual; the paper's
  $\Hom(L[\wp],\mathcal O)$ is $L[\wp]^\vee$, its $H^1_f(\Q_p,T^D)^*$ is Pontryagin. The adjoint of an operator is $A^\dagger$ (9.5; $^*$ is the
  Pontryagin dual only, and a pullback when written after a map: Appendix B, B-C4).
* **Orthogonals of non-symmetric pairings.** The paper's pairings are alternating, so left and right orthogonals agree; state 9.2,
  9.3 for general perfect pairings with right orthogonals and say this once.
* **"Order $\#\mathcal O/\Delta$".** The paper's Lemma lem:ddt417 is stated for a general DVR but counts orders; write lengths
  ($v(\Delta)$, $d\,v(\eta)$) and remark that for finite $k$ this is the paper's count (Part 8, point 4).
* **$\T_{\mathfrak m}$** always means the factor of $\T\otimes\Zl$ (C7). Do not write $\T_{\mathfrak m}$ for the algebraic localisation of $\T$ at $\mathfrak m$, which is
  not complete and is not a direct factor of anything.
* **$\wp\cap I=0$.** State and prove 11.1(ii) in the two-line form: it holds iff $\eta\ne0$; do not justify it by "$\T$ is reduced",
  because the full Hecke algebra (with the $U_p$) need not be reduced (10.7(v); Part 8, point 1).
* **The congruence ideal in $\T_{\mathfrak m}$.** In 11.1(v) say explicitly that the other local factors lie in $\ker\pi$ and that their annihilator
  component is $0$ (the paper's sentence in Lemma lem:hecke says "lie in the annihilator"; Part 8, point 2).
* **Fitting versus annihilator versus order.** Over $\Zl$ the Fitting ideal of a finite module is $\#M\cdot\Zl$, not its annihilator; the
  Tamagawa factor is a Fitting ideal, so it sees the whole order (7.6(iv), Exercise 5).
* **Notation $\Tam_p(M)=\Fitt(\dots)^{G_{\Q_p}}$.** In the card and the `paperlink`, write $\Fitt_{\Zl}\bigl(H^1(I_p,M)_{\tors}^{G_{\Q_p}}\bigr)$, the Fitting ideal
  of the invariants, as Chapters 16 and 21 do; the paper's display puts the superscript outside the parentheses (Part 8,
  point 3).
* **Saturation.** Every time a Gram determinant is converted into a cokernel order, say "saturated" and point to 9.3(iv).
* **Completeness.** Idempotent lifting and $\T\otimes\Zl=\prod\T_{\mathfrak m}$ need $\Zl$ complete; give the example of 10.3(v).
* **Proof levels.** Everything is proved except: Zorn's lemma for maximal ideals in general rings (2.6, referred to Chapter 2),
  Hilbert's basis theorem (4.1(iv)), flatness of torsion-free modules over a PID in the non-f.g. case (3.4(ii), sketch), the Smith form
  over a non-Euclidean PID (5.2, sketch), DVR criterion (e) (6.1, stated), Artin-Rees and completions in general (6.4(vii), stated),
  topological Nakayama (6.6(iv), sketch), finite length iff Noetherian and Artinian (7.1(ii), stated), independence of the Fitting
  ideal of the presentation in general (7.4, sketch), Pontryagin duality for general compact modules (8.2(v), stated), the Pfaffian
  identity and the symplectic normal form in general rank (9.4, sketch), Jordan-Chevalley (10.7(iv), stated), complete
  intersections are Gorenstein and Wiles's criterion (11.4(iv), stated). Never present these as proofs.
* **Do not duplicate.** Do not prove Lemma lem:ddt417, Lemma lem:hecke, Lemma lem:crit or Remark rem:free (Chapters 15, 20, 14); do not
  prove the analytic theory of $\Q_p$, Hensel's lemma or $\Z_p^\times$ (Chapter 7); do not do $G$-stable lattices, homothety, Ribet's lemma,
  Maschke or Brauer-Nesbitt (Chapter 4); do not do Ext, Tor, long exact sequences of complexes or group cohomology (Chapter 16;
  mention $\Ext^1$ at most in one remark after 5.7); do not do $\Z_3[\zeta_3]$ as a DVR (Chapter 6); do not define $\Tam_p$, $H^1_f$, $T^D$
  (Chapter 18) beyond quoting them in `paperlink`s.
* **Coordination with Chapter 4 on Jordan-Holder.** Chapter 3 comes first and proves 7.1(i) for modules over a ring without using
  commutativity; Chapter 4 should cite it. If the Chapter 4 outline (written in parallel) also proves Jordan-Holder, the
  orchestrator should keep this proof and turn Chapter 4's into a citation, or keep Chapter 4's and make 7.1(i) here "stated;
  proved in Chapter 4" with a forward pointer; one proof only.
* **Examples from the paper.** Use the paper's curves only where the topic allows: $T_3E$ for a type $\mathrm{IV}$ curve as a
  $\Z_3[\zeta_3]$-module (1.2(c), Exercise 4); the Tamagawa module $\Z/\ell^v\oplus\Z/\ell^m$ (7.7); the level-$11$ oldforms at level $88$ (Exercise 14).
  Most examples are toy algebras (11.2), which is deliberate: they are the smallest "Hecke algebras with a congruence".
* **RHB remarks** (one sentence each): Pontryagin duality as the finite Fourier transform (8.1(vi)); generalised eigenspaces and
  the Jordan form of a matrix (10.5, 10.7); Gram matrices as metric tensors (9.1).
* **Typography** (PLAN.md 7.2): no dash ligatures ("Atiyah-Macdonald", "Jordan-Holder", "Cayley-Hamilton", "Jordan-Chevalley"
  with plain hyphens; ranges as "1 to 8"); ASCII source (write "Jordan-Holder" without the umlaut, or `H\"older`); labels with the
  `modules:` infix; the tables of 7.7 and 11.2 with `booktabs`.

References: Atiyah-Macdonald (`AtiyahMacdonald`), Dummit-Foote (`DummitFoote`), Lang (`Lang`), Eisenbud (`Eisenbud`), Serre
(`SerreLocalFields`, `SerreCourse`), NSW (`NSW`), Weibel (`Weibel`), Rubin (`Rubin`), DDT (`DDT`), Hida81, Ribet83, Mazur77, Tilouine97
are in `refs.bib`. Not in `refs.bib` (add to `bib/ch03.bib` if cited): Northcott, *Finite free resolutions* (1976); Mazur and Wiles,
*Class fields of abelian extensions of $\Q$*, Invent. Math. 76 (1984), Appendix (Fitting ideals); Matsumura, *Commutative ring
theory* (Gorenstein rings, Chapter 18); Jacobson, *Basic Algebra I* (Smith form); Bourbaki, *Algebra*, Chapters VII, IX.
Theorem numbers recalled but not re-verified against the books (cite them only after checking, otherwise cite the chapter):
AM Propositions 2.4, 2.6, Corollaries 2.7, 2.8, Theorem 7.5, Theorem 8.7, Proposition 9.2; DF Section 12.1 Theorems 4 to 6; Weibel
Lemma 1.3.2; Eisenbud Section 20.2 and Corollary 7.5. No theorem number is cited in this outline without "check".

## 7. Verification log (computations done for this outline)

Python 3.13 with sympy 1.14, scripts `c1.py` to `c5.py` in `/tmp/ch03`.
* Smith normal forms and Fitting ideals (`c1.py`): rows $(2,4),(6,8)$: $\operatorname{diag}(2,4)$, $\Fitt=(8)$; rows $(2,4,4),(-6,6,12),(10,-4,-16)$:
  $\operatorname{diag}(2,6,12)$, $\Fitt=(144)$; rows $(3,6),(9,3)$: $\operatorname{diag}(3,15)$, $\Fitt=(45)$; rows $(4,0),(0,2)$: $\operatorname{diag}(2,4)$; one generator with
  rows $(2),(4)$: $\Fitt=(2)$; rows $(6,0),(0,4),(2,2)$: $\operatorname{diag}(2,2)$, $\Fitt=(4)$ (minors $24,12,-8$). Annihilators and the $\Z_2$, $\Z_3$ parts by hand.
* Gram determinants (`c2.py`, `c5.py`): the pairing $\begin{psmallmatrix}9&1\\1&0\end{psmallmatrix}$, $L'=\Z e_1$: $L'^\perp=\Z(1,-9)$, index $9$; standard pairing and
  $L'=\Z\cdot3e_1$: Gram $9$, index $3$. Random tests: $200$ symmetric perfect pairings on $\Z^4$ and $300$ non-symmetric perfect pairings on
  $\Z^n$, $n\le5$, with random saturated sublattices: $[L:L'\oplus L'^\perp]=\abs{\Delta(L')}=\abs{\Delta(L'^\perp)}$ in every case.
* Toy algebras (`c3.py`): $\T_r$ for $\ell=3$, $r=1,2$: Gram of $\lambda(st)$ on $(1,1),(3^r,0)$ is $\begin{psmallmatrix}0&1\\1&3^r\end{psmallmatrix}$ (determinant $-1$), $L[\wp]=\Z_3(3^r,0)$
  with Gram $3^r=\eta$; the alternating pairing on $\T_2^2$: $\Delta=81=\eta^2$. Socle dimensions of the reductions mod $3$: $\T_2$: $1$;
  $\{(a,b,c):a\equiv b\equiv c\bmod3\}$: $2$, with $\eta=3$ (brute force over small coefficients). $\Z[x]/(x^2-4)$: $I=\Z(x+2)$, $\eta=4$, idempotent $(x+2)/4$.
  $\Z[x]/(x^2(x-1))$: $\eta=0$ at $x\mapsto0$, $\eta=1$ at $x\mapsto1$ (by hand).
* Shift operator (`c3.py`): characteristic polynomials $X^2-aX+p$, $X(X^2-aX+p)$, $X^2(X^2-aX+p)$ for $e=1,2,3$, with $v_e$ cyclic (rank of the
  Krylov matrix $e+1$); $U(v_0-av_1+pv_2)=0$; the variant $Uv_0=av_0$: characteristic polynomial $X^e(X-a)$, $U(v_0-av_1)=0$ (by hand).
* Idempotents (`c4.py`): $x^2+x-1$ factors mod $\ell$ as: irreducible ($\ell=2,3$), $(x-2)^2$ ($\ell=5$), $(x-3)(x-7)$ ($\ell=11$), split for $\ell=19,29,31$;
  Hensel roots mod $11^6$: $728020$, $1043540$; the idempotent $(x-r_2)/(r_1-r_2)$ satisfies $e^2=e$ mod $11^6$ and equals the limit of the Newton
  iteration $e\mapsto3e^2-2e^3$ from $(x-3)/4$.
* By hand: the two-line proof of 11.1(ii) and of 11.3(ii), (iii) (no use of reducedness); $\Ann(\ker\pi)=\Ann_{\T_{\mathfrak m}}(\wp_{\mathfrak m})\times0$ for a
  product; the $k[\varepsilon]$ counterexample to multiplicativity of $\Fitt$; $\Fitt(\Z[x]/(2,x))^2=(4,2x,x^2)$; the Gorenstein criterion via socles;
  the proof of 11.5; the claim of 11.6 that a free $L$ with $\eta=0$ has $\Delta=0$.
* The paper's proofs of Lemma lem:crit, Lemma lem:ddt417, Lemma lem:hecke, Remark rem:free and Theorem thm:quant Step 1 were
  reread sentence by sentence against the items of Sections 5 and 9 to 11; the findings are Part 8.

## 8. Points for important_notes.md

New points in the area of this chapter (commutative algebra of Lemmas lem:crit, lem:ddt417, lem:hecke, Remark rem:free, Section
1.2), not among the 32 already recorded. Point 1 refines point 19; the others are new. None changes a result of the paper. Each
was checked as stated (Part 7).

1. **Lemma lem:ddt417, proof: the justification of $\wp\cap I=0$ (refines important_notes.md point 19).** Location: "Since $L$ is
   torsion-free and $\wp\cap I=0$, the sum $L[\wp]+L[I]$ is direct." Point 19 proposes the justification "$\T$ is reduced ($\T\otimes\Q$ is a
   product of fields)". Problem: that justification is not available in general. The full Hecke algebra, which contains the $U_p$, need
   not be reduced: on the span of $h(z),h(pz),\dots,h(p^ez)$ ($h$ a newform of level $M$, $p\nmid M$) the operator $U_p$ has characteristic
   polynomial $X^{e-1}(X^2-a_pX+p)$ and the cyclic vector $h(p^ez)$, so for $e\ge3$ the eigenvalue $0$ has a Jordan block of size $e-1\ge2$
   (10.7(v); the paper itself says "$U_p$ is not semisimple on this span when $0$ is a repeated eigenvalue"). Example: level $88$, $h=f_{11}$,
   $p=2$, $e=3$. So $\T\otimes\Q$ can contain nonzero nilpotents, and Lemma lem:ddt417 is in any case stated for an arbitrary finite free $\T$.
   Fix: the correct and elementary statement is "$\wp\cap I=0$ if and only if $\eta\ne0$" (11.1(ii)): if $\eta=0$ there is nothing to prove;
   otherwise pick $t\in I$ with $\pi(t)$ generating $\eta$, and for $x\in\wp\cap I$ write $\pi(t)x=tx+(\pi(t)-t)x$, where $tx\in I\wp=0$ and
   $(\pi(t)-t)x\in\wp I=0$; so $\pi(t)x=0$ and $x=0$. Two further remarks for the same proof: (a) the step "$(\pi(t)-t)x\in L[I]$ (as
   $s(\pi(t)-t)\in\wp\cap I=0$ for $s\in I$)" needs only $I\wp=0$, since $\pi(t)-t\in\wp$; (b) the directness of $L[\wp]+L[I]$ needs only
   $\pi(t)\ne0$: an element killed by $\wp+I\ni\pi(t)$ is killed by $\pi(t)$. The equality clause uses $\Ann_\T(I)=\wp$ (for $\T[I]=\wp$ in
   "$Q\simeq(\T/(\wp+I))^d$"), which also holds exactly when $\eta\ne0$ (if $xI=0$ then $\pi(x)\pi(t)=0$). Also, if $\eta=0$ and $L$ is free over $\T$,
   then $\Delta=0$, so the hypothesis $\Delta\ne0$ excludes that case. In the applications $\eta\ne0$ because the $f$-factor of $\T\otimes K$ is
   $K$ (multiplicity one for the newform, or Step 1 of Theorem thm:quant for $g^S$). Confidence: high (the algebra is two lines;
   the Jordan block was checked symbolically).

2. **Lemma lem:hecke, proof: "the other local factors of $\T\otimes\Zl$ are killed by $\phi_f$ and lie in the annihilator".** Problem: as
   written this is false. With $\T\otimes\Zl=\T_{\mathfrak m}\times\T''$ and $\phi_f$ factoring through $\T_{\mathfrak m}$, one has $\ker\phi_f=\wp_{\mathfrak m}\times\T''$ and
   $\Ann(\ker\phi_f)=\Ann_{\T_{\mathfrak m}}(\wp_{\mathfrak m})\times0$: the factor $\T''$ lies in the kernel, and its component of the annihilator is $0$ (an element
   $(0,b)$ with $b\ne0$ does not kill $(0,1_{\T''})\in\ker\phi_f$). The conclusion, that the congruence ideal is computed in $\T_{\mathfrak m}$, is right:
   $\phi_f(\Ann(\ker\phi_f))=\phi_f(\Ann_{\T_{\mathfrak m}}(\wp_{\mathfrak m}))$. Fix: "since $\phi_f$ kills the other local factors, $\ker\phi_f=\wp_{\mathfrak m}\times\T''$ and
   $\Ann(\ker\phi_f)=\Ann_{\T_{\mathfrak m}}(\wp_{\mathfrak m})\times0$, so the congruence ideal is computed in $\T_{\mathfrak m}$" (11.1(v)). Confidence: high (expository slip;
   no effect).

3. **Lemma lem:hecke, proof: the pairing on the $\mathfrak m$-component.** Location: "Apply Lemma lem:ddt417 to ... $L=H^1(X_0(N),\Zl)_{\mathfrak m}$ with
   the pairing $\hat\delta_!$ of Section sec:dfg, perfect and alternating with $\T$ self-adjoint". Problem (small gap): Section 4.1 says
   $\hat\delta_!$ is perfect on $H^1(X_0(N),\Zl)$, not on its $\mathfrak m$-component. The restriction is perfect because the idempotent $e_{\mathfrak m}\in\T\otimes\Zl$ is
   self-adjoint (it is a limit of polynomials in self-adjoint operators, or: idempotents of a commutative algebra of self-adjoint
   operators are self-adjoint), so $H^1\otimes\Zl=e_{\mathfrak m}H^1\oplus(1-e_{\mathfrak m})H^1$ is an orthogonal decomposition and a perfect pairing restricts to a
   perfect pairing on each summand (9.5(iii)). Also $L[\wp]$, computed in $L$, is the lattice $M_{f,\lambda}$ of the whole $H^1$, since $M_{f,\lambda}$ is
   killed by $\ker\phi_f\ni1-e_{\mathfrak m}$. The same remark applies to Step 2 of the proof of Theorem thm:quant. Fix: add one sentence. Confidence:
   high (the argument is standard; the omission is minor).

4. **Section 1.2 (and the proof of Lemma lem:tamfactor): the display $\Tam_p(M)=\Fitt_{\Zl}\bigl(H^1(I_p,M)_{\mathrm{tor}}\bigr)^{G_{\Q_p}}$.** Problem
   (notation): the superscript $G_{\Q_p}$ is outside the parentheses, so the display reads as "the $G_{\Q_p}$-invariants of an ideal of $\Zl$". What
   is meant, and what the proof of Lemma lem:tamfactor computes ("the Fitting ideal of the $G$-invariants of the torsion of $H^1(I,M)$"),
   is $\Fitt_{\Zl}\bigl(H^1(I_p,M)_{\mathrm{tor}}^{G_{\Q_p}}\bigr)$. Fix: move the superscript inside the parentheses. Confidence: high that the display
   is misbracketed (the LaTeX source has `\bigr)^{G_{\Q_p}}`); importance low. Chapters 16 and 21 already write the corrected form.

5. **Lemma lem:ddt417, statement and proof: orders for a general DVR.** Location: "Let $\mathcal O$ be a discrete valuation ring ...";
   "of order $\#\mathcal O/\Delta$", "$\#\mathcal O/\Delta\le\#(\mathcal O/\eta)^d$". Problem (expository): for a DVR with infinite residue field these orders are
   infinite and the inequality is meaningless; the argument is right with lengths: $\len_{\mathcal O}Q=v(\Delta)$ (9.3), and $Q$, being generated by $d$
   elements and killed by $\eta$, is a quotient of $(\mathcal O/\eta)^d$, so $v(\Delta)\le d\,v(\eta)$. In the paper's applications $\mathcal O=\Zl$, where the two
   formulations agree. Fix: replace orders by lengths, or assume the residue field finite. Confidence: high; importance low.

Checked and found correct (recorded so that later chapters need not recheck): the paper's Lemma lem:crit argument "$\T\otimes\Q=\Q\times\T'$,
$I=\T\cap(0\times\T')$, $J=\T\cap(\Q\times0)$, $J=\Ann_\T I$" (11.1(iii)); "dualising the inclusion ... index $r'$" (5.7, 9.6); "embeds in $\Q f/\Z f$, so
it is cyclic ... $r'h=f+g_0$" (5.8); the forms killed by $I$ are $\Z f$ because $a_1(f)=1$; "Every step holds verbatim over $\Zl$" (3.4(iii));
Lemma lem:ddt417's "$L[\wp]$ is saturated" and "$L[\wp]^\perp=L[I]$" (11.3); Section 4.1's "Gram determinant $(\eta^\Sigma)^2$ up to a unit"
for an alternating rank-two lattice whose ideal of values is $\eta^\Sigma$ (9.4(ii)); Lemma lem:IV's "free of rank one over $\Z_3[\zeta_3]$"
(5.4(iii)); Theorem thm:quant Step 1's projection by the idempotent (10.6); the length identity in the proof of Theorem thm:main
(7.1(iii), 8.1(v)); "$H^1(\R,T^D)$ is killed by $2$, so $H^1_f(\R,T^D)=0$ for $\ell$ odd" (6.4(iii)).
