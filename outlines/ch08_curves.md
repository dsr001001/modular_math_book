# Chapter 08: Algebraic curves, function fields and Riemann surfaces (`ch:curves`, `chapters/ch08_curves.tex`)

Stage 1 line-up. Part III (Curves and elliptic curves). Target length 2,150 lines of LaTeX (card excluded; see Part 3),
inside the 1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2
to 6 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book and
chapter or section; a theorem number only where sure); the paper's use by its `\label` names, or "background". The
small computations quoted below (genera, smoothness of the paper's Weierstrass models, Riemann-Hurwitz counts, the
torus computations) were checked by hand and by Python/sympy scripts in `/tmp/ch08` (verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

The paper uses curves in four places, and the chapter is built around them.

1. **The modular parametrisation and its degree** (Section 1, the abstract, Theorem thm:main, Lemma lem:hecke):
   "$\varphi_E\colon X_0(N)\to E$ its modular parametrisation", "the $X_0(N)$-optimal curve, for which the modular
   parametrisation has minimal degree", "$\deg\varphi_E$, its modular degree". The chapter supplies: smooth projective
   curves and morphisms between them, the degree of a nonconstant morphism in its equivalent forms (field degree, number
   of preimages, pullback of divisors, topological degree on $H^2$), $\varphi_*\varphi^*=\deg\varphi$ on divisor classes and on
   $H^1$, and the formula $\langle\varphi^*x,\varphi^*y\rangle_X=\deg\varphi\cdot\langle x,y\rangle_Y$ for the cup product, which is the
   cohomological meaning of the modular degree (item 11.5).
2. **$H^1(X_0(M),\Z_\ell)$ with the cup product, and the pairing $\hat\delta_!$** (Section 4.1, Lemma lem:hecke, Theorem thm:quant
   Step 2, Lemma lem:ddt417 as applied): "it is perfect and alternating on $H^1(X_0(M^\Sigma),\Z_\ell)$, and the Hecke
   operators, $U_p$ included, are self-adjoint for it, because $w_{M^\Sigma}T_nw_{M^\Sigma}^{-1}$ is the adjoint of $T_n$ for the cup
   product". The chapter supplies $H_1$ and $H^1$ of a compact Riemann surface, rank $2g$, the cup product (perfect,
   alternating; Poincare duality), the base change to $\Z_\ell$, correspondences and their actions, and the general
   theorem that **the adjoint of a correspondence for the cup product is the transpose correspondence** (12.3), with the
   abstract lemma that turns "$C^t=wCw$ for all $C$" into "every $C$ is self-adjoint for $\langle x,w^*y\rangle$, which is perfect
   and alternating" (12.3(e)). The specific identity $T_n^t=w_NT_nw_N$ on $X_0(N)$ is Chapter 14's.
3. **$J_0(N)$, its torsion and its Tate module** (Remark rem:free, Section 4.2, important_notes.md point 26): "$J_0(N)[\mathfrak m]$
   is two-dimensional", "the Tate module is free of rank two", "$M_{f,\lambda}$ and $T_\ell E$ are homothetic". The chapter
   supplies the Jacobian as $\operatorname{Pic}^0$, as a complex torus $H^0(X,\Omega^1)^\vee/H_1(X,\Z)$ and as an abelian variety
   (statements), Abel-Jacobi, $J[n]\simeq H_1(X,\Z/n)\simeq(\Z/n)^{2g}$, $T_\ell J\simeq H_1(X,\Z)\otimes\Z_\ell$, and **which is dual to which**:
   $H^1(X,\Z_\ell)=\Hom(T_\ell J,\Z_\ell)$, and Galois-equivariantly $H^1_{\mathrm{et}}\simeq T_\ell J(-1)$ via the Weil pairing.
4. **Foundations for Chapters 9, 10, 12, 14, 15**: varieties and points over extensions with the Galois action (every
   $E(K)$, $E[m]$, $T_\ell E$ of the paper), Riemann-Roch and its consequences (a genus-one curve with a rational point is a
   Weierstrass cubic; $P\mapsto[(P)-(O)]$ is a bijection onto $\operatorname{Pic}^0$), separability and the Frobenius morphism,
   ramification and Riemann-Hurwitz (isogenies are unramified; genus formula of $X_0(N)$ in Chapter 12), compact Riemann
   surfaces versus complex curves (so that $X_0(N)$, built analytically in Chapter 12, is an algebraic curve), holomorphic
   differentials (weight-two cusp forms are holomorphic differentials, Chapter 12).

This is the hardest audience gap of the book: a reader who knows complex analysis and linear algebra meets algebraic
geometry and algebraic topology at once. The chapter therefore follows three rules.

* **Two languages, one dictionary.** The algebraic side is done in the classical language of Silverman's AEC, Chapters I
  and II: varieties are sets of $\bar k$-points cut out by polynomials, with $G_k$ acting on coordinates; no schemes, no
  sheaves, no sheaf cohomology. The analytic side is done on compact Riemann surfaces with charts, exactly as in a first
  complex analysis course. The dictionary between them (Riemann existence, GAGA) is stated (R) once, in 8.3, and used
  freely afterwards; every other comparison is proved from it.
* **What is proved, sketched, stated.** Proved (P): everything that is a computation with polynomials, valuations,
  local normal forms of holomorphic maps, change of variables in integrals, or linear algebra of lattices: smooth
  points have DVR local rings (2.2), rational maps from smooth curves extend (3.2), the degree formulas (6.4), the
  consequences of Riemann-Roch (5.3, 5.6, 5.7), Riemann-Hurwitz from Riemann-Roch (7.2), the residue theorem (9.2),
  positivity in the bilinear relations (9.4), the cup product on the torus (10.4), the torsion and Tate module of a
  complex torus (11.6, 11.7), the pullback formula and the saturation criterion (11.5), the adjointness of correspondences
  (12.3). Sketched (S): the degree formula $\sum e_P=\deg\varphi$ (6.3, via Chapter 6's $\sum e_if_i=n$), the genus of smooth plane
  curves (5.4), the Weierstrass embedding being an isomorphism (5.6), Riemann's bilinear relations in period form (9.4),
  Hodge decomposition (10.2). Stated (R): the Nullstellensatz, Bezout, the equivalence of categories of curves and
  function fields, Riemann-Roch, Riemann existence and GAGA, the classification of surfaces and the existence of a
  symplectic basis, Poincare duality over $\Z$, Abel's theorem and Jacobi inversion, the algebraicity of the Jacobian and
  its universal property, the Weil pairing and etale cohomology, the Weil conjectures for curves.
* **The physics reader's intuition is used, in one sentence each, where it is literally right**: contour integrals and
  residues (9.2: "total charge on a closed surface is zero"); periods of $dz$ on a torus as the primitive vectors of a
  crystal lattice, and $H^1$ as the reciprocal lattice (10.4); the torus $\R^2/\Z^2$ as a periodic box with area form
  $dx\wedge dy$ (10.4); intersection number as a signed crossing count, like a winding number (10.1); Riemann-Hurwitz as
  Euler's $V-E+F$ for a branched cover (7.2, 8.4); positivity $\frac i2\int\omega\wedge\bar\omega=\int|f|^2dx\,dy$ as a norm (9.4; the
  Petersson norm of Chapter 12 is this); lattices up to homothety (Chapter 9). Never belaboured.

### 1.2 Global conventions fixed in this chapter

* **C1 (fields).** $k$ is a **perfect** field (characteristic $0$ or a finite field are all the paper needs: $\Q$, $\Q_p$,
  $\F_p$, number fields); $\bar k$ an algebraic closure, $G_k=\Gal(\bar k/k)$ (Chapter 5, C1). Over $\C$ we write $X$ for a
  compact Riemann surface and identify it with the smooth projective curve it defines (8.3).
* **C2 (curves).** A *curve over $k$* is a projective variety of dimension one defined over $k$ (1.3); "variety" includes
  "irreducible over $\bar k$" (geometrically irreducible). Unless said otherwise curves are **smooth and projective**; a
  singular or affine model is called a *model*. Morphisms are defined over $k$ when $k$ is named, over $\bar k$ otherwise.
  The genus is $g$; for $X$ a compact Riemann surface it is also the topological genus (8.4).
* **C3 (points and Galois).** $C(L)$ is the set of points with coordinates in $L$ (for $k\subseteq L\subseteq\bar k$);
  $\sigma\in G_k$ acts on $C(\bar k)$ coordinatewise, on the left; $C(L)=C(\bar k)^{G_L}$. This is the action behind
  $\rho_{E,\ell}$ (Chapters 9, 11).
* **C4 (pullback, pushforward, transpose, adjoint).** For a nonconstant morphism $\varphi\colon X\to Y$: $\varphi^*$ is pullback
  (of functions, divisors, divisor classes, differentials, $H^1$ classes) and $\varphi_*$ is pushforward (of divisors, divisor
  classes, $H_1$ classes) and, on $H^1$, the transpose of the transfer (12.2). A correspondence is written $\mathcal C=(C,\alpha,\beta)$
  and its transpose $\mathcal C^t=(C,\beta,\alpha)$. **The adjoint of an endomorphism $A$ for a pairing is written $A^\dagger$ in this
  chapter**, because $^*$ is taken by pullbacks; Chapter 3 writes $A^*$ for the adjoint and the paper and Chapter 4 write $^*$
  for Pontryagin duals (Part 7, book-internal point B3).
* **C5 (duals).** $M^\vee=\Hom(M,\Z)$ or $\Hom_{\Z_\ell}(M,\Z_\ell)$ for lattices; $V^\vee$ for linear duals and contragredient
  representations, as in Chapter 4, C2. Pontryagin duals ($^*$ in the paper) do not occur in this chapter.
* **C6 (orientation and the cup product).** A Riemann surface is oriented by its complex structure: in a chart $z=x+iy$,
  $dx\wedge dy=\frac i2dz\wedge d\bar z$ is positive. The cup product of $H^1$ classes is $\langle\alpha,\beta\rangle=\int_X\alpha\wedge\beta$ (de Rham
  representatives), an integer on integral classes. The intersection number $a\cdot b$ of transverse oriented loops counts
  crossings with sign $+1$ when (tangent of $a$, tangent of $b$) is a positive basis. Poincare duality
  $\operatorname{PD}\colon H^1\to H_1$ is fixed by $\int_{\operatorname{PD}(\alpha)}\beta=\int_X\alpha\wedge\beta$; with these choices $\operatorname{PD}$ is an isometry,
  $\langle\alpha,\beta\rangle=\operatorname{PD}(\alpha)\cdot\operatorname{PD}(\beta)$ (checked on the torus, 10.4). Other books use other signs; the paper needs only
  "perfect and alternating", the adjointness of 12.3 and ideals of values, none of which depends on the sign.
* **C7 (Frobenius).** As in Chapter 5, C2 and Chapter 6, 3.7: the arithmetic Frobenius of $G_{\F_q}$ acts on $\bar\F_q$-points
  by raising coordinates to the $q$-th power; on $T_\ell J$ it acts as the $q$-power Frobenius endomorphism; the geometric
  Frobenius is its inverse, and on $H^1=(T_\ell J)^\vee$ the geometric Frobenius has the same eigenvalues as the arithmetic
  one on $T_\ell J$ (11.8(d)).
* **C8 (typography).** PLAN.md Section 7.2: no dash ligatures, ASCII source, labels `...:curves:...`; "Riemann-Roch",
  "Riemann-Hurwitz", "Abel-Jacobi" with plain hyphens; tables with `booktabs`.

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 1. Affine and projective space, varieties

**1.1 `def:curves:affine-variety`** (definitions and theorem; P except the Nullstellensatz, R). $\mathbb A^n=\mathbb A^n(\bar k)=\bar k^n$,
with $G_k$ acting coordinatewise and $\mathbb A^n(L)=\mathbb A^n(\bar k)^{G_L}$. For $S\subseteq\bar k[x_1,\dots,x_n]$, $V(S)$ is its zero set
(an *algebraic set*); for $Y\subseteq\mathbb A^n$, $I(Y)$ is the ideal of polynomials vanishing on $Y$. The algebraic sets are the
closed sets of the *Zariski topology*. (i) Hilbert's Nullstellensatz: $I(V(\mathfrak a))=\sqrt{\mathfrak a}$ for every ideal $\mathfrak a$ of
$\bar k[x]$ (R). (ii) An *affine variety* is an algebraic set $V$ with $I(V)$ prime; it is *defined over $k$* if $I(V)$ is
generated by polynomials in $k[x]$ (for $k$ perfect, equivalently $\sigma(V)=V$ for all $\sigma\in G_k$; R). (iii) The coordinate
ring $\bar k[V]=\bar k[x]/I(V)$ is a domain; $k[V]=k[x]/(I(V)\cap k[x])$; the function field $\bar k(V)=\operatorname{Frac}\bar k[V]$ and
$k(V)=\operatorname{Frac}k[V]$. (iv) $\dim V$ is the transcendence degree of $\bar k(V)$ over $\bar k$ (transcendence degree recalled
from Lang VIII.1, R; Chapter 5 defines only algebraic and transcendental elements). Examples: $\mathbb A^1$, the parabola
$y=x^2$ ($\bar k[V]\simeq\bar k[x]$), the affine Weierstrass cubics of 2.1. Reference: SilvermanAEC I.1; Hartshorne I.1;
Fulton, Chapter 1. Paper: background.

**1.2 `def:curves:projective-space`** (definitions and proposition; P). $\mathbb P^n=\mathbb P^n(\bar k)=(\bar k^{n+1}\setminus0)/\bar k^\times$
with homogeneous coordinates $[x_0:\dots:x_n]$ (for $n=1$ this is Chapter 1's set of lines, C1 there). (i) $G_k$ acts
coordinatewise, and $\mathbb P^n(\bar k)^{G_L}=\mathbb P^n(L)$: a $G_L$-fixed point has a representative with coordinates in $L$
(scale a nonzero coordinate to $1$; then each $\sigma$ fixes every coordinate). (ii) Homogeneous ideals, projective algebraic
sets $V(S)$ for homogeneous $S$, projective varieties (homogeneous prime $I(V)$), defined over $k$ as in 1.1. (iii) The
charts $U_i=\{x_i\ne0\}\simeq\mathbb A^n$; the projective closure $\bar V$ of an affine variety (homogenise the generators of
$I(V)$) and dehomogenisation; $\mathbb P^n=\mathbb A^n\sqcup\mathbb P^{n-1}$, $\mathbb P^1=\mathbb A^1\sqcup\{\infty\}$, with $\mathrm{PGL}_2$ acting by
Moebius transformations (Chapter 1, C1). (iv) The function field of a projective variety is the field of quotients
$F/G$ of homogeneous polynomials of equal degree with $G\notin I(V)$; it equals that of any nonempty affine chart.
Reference: SilvermanAEC I.2; Hartshorne I.2. Paper: background ($X_0(N)$ and $E$ are projective curves).

**1.3 `def:curves:curve-morphism`** (definitions; P). A *curve over $k$* is a projective variety of dimension $1$ defined
over $k$ (C2). For projective varieties $V_1$, $V_2\subseteq\mathbb P^n$, a *rational map* $\varphi=[f_0:\dots:f_n]\colon V_1\dashrightarrow V_2$ with
$f_i\in\bar k(V_1)$, not all zero, such that $\varphi(P)\in V_2$ wherever defined; $\varphi$ is *regular* at $P$ if there is $g\in\bar k(V_1)^\times$
with all $gf_i$ regular at $P$ and some $(gf_i)(P)\ne0$; a *morphism* is a rational map regular everywhere; $\varphi$ is *defined
over $k$* if it can be written with $f_i\in k(V_1)$ (for $k$ perfect: iff $\varphi(\sigma P)=\sigma\varphi(P)$ for all $\sigma$, $P$; R).
Isomorphisms. Example: $[x^2:xy:y^2]\colon\mathbb P^1\to\mathbb P^2$ onto the conic $XZ=Y^2$. Reference: SilvermanAEC I.3. Paper: background
($\varphi_E$ is a morphism defined over $\Q$, Chapter 14).

### Section 2. Plane curves and smoothness

**2.1 `def:curves:plane-curve`** (definition and proposition; P). A *plane curve of degree $d$* is $C=V(F)\subset\mathbb P^2$ for a
homogeneous $F\in k[X,Y,Z]$ of degree $d$, irreducible over $\bar k$; its affine part is $f(x,y)=F(x,y,1)=0$. A point $P\in C$
is *singular* if $F_X(P)=F_Y(P)=F_Z(P)=0$, *smooth* (nonsingular) otherwise; $C$ is smooth if it has no singular point in
$C(\bar k)$. (i) Euler's identity $XF_X+YF_Y+ZF_Z=dF$; hence if $\operatorname{char}k\nmid d$, a point of $\mathbb P^2$ where the three partials
vanish lies on $C$; on the affine part, $P$ is singular iff $f(P)=f_x(P)=f_y(P)=0$. (ii) At a smooth point the tangent line
is $F_X(P)X+F_Y(P)Y+F_Z(P)Z=0$. (iii) Examples (checked by Groebner bases over $\Q$, Part 6.6): the nodal cubic
$y^2=x^3+x^2$ and the cuspidal cubic $y^2=x^3$ have the single singular point $(0,0)$; the Fermat curve $X^d+Y^d+Z^d=0$ is
smooth iff $\operatorname{char}k\nmid d$ (in characteristic $p=d$ it is the triple line $(X+Y+Z)^p$, not even irreducible); the cubics
$y^2+y=x^3-x^2-10x-20$ (11a1), $y^2+xy+y=x^3+x^2-30x-76$ (121a1) and $y^2=x^3+x^2+4x+4$ (20a1) are smooth over $\bar\Q$,
including the point $[0:1:0]$ at infinity. The general smoothness criterion for Weierstrass cubics ($\Delta\ne0$) is
Chapter 9's. Reference: SilvermanAEC I.1 (Example 1.6 and the exercises; cite the section); Fulton, Chapters 3 and 5.
Paper: background (the curves of the paper are given by such equations; Section 1, the Appendix `ellinit`).

**2.2 `thm:curves:smooth-dvr`** (theorem; P). Let $C$ be a curve (affine plane model $f=0$ suffices) and $P\in C(\bar k)$ with
local ring $\bar k[C]_P=\{g/h:h(P)\ne0\}\subset\bar k(C)$ and maximal ideal $\mathfrak m_P$. Then $P$ is smooth iff
$\dim_{\bar k}\mathfrak m_P/\mathfrak m_P^2=1$, iff $\bar k[C]_P$ is a discrete valuation ring. At a smooth point of $f=0$, any line through $P$
other than the tangent line gives a uniformiser $t_P$ (for instance $x-x(P)$ if $f_y(P)\ne0$). The valuation
$\operatorname{ord}_P\colon\bar k(C)^\times\to\Z$ is the order of vanishing; $f(P)$ is defined iff $\operatorname{ord}_P f\ge0$. Proof: $\mathfrak m_P/\mathfrak m_P^2$ is
spanned by $x-x(P)$, $y-y(P)$ subject to the one relation $f_x(P)(x-x(P))+f_y(P)(y-y(P))\equiv0$; then Nakayama (Chapter 3,
4.3) and the DVR criterion (Chapter 3, 6.1(a)). Reference: SilvermanAEC II.1 (Proposition 1.1); Fulton 3.2; Hartshorne I.6.
Paper: background (orders of zeros and poles everywhere below).

**2.3 `thm:curves:bezout`** (theorem; R). Two plane curves of degrees $m$ and $n$ without common component meet in exactly
$mn$ points of $\mathbb P^2(\bar k)$ counted with intersection multiplicity. Special cases used: a line meets a curve of degree $d$
(not containing it) in $d$ points with multiplicity, so the divisor of a linear form on a smooth plane curve of degree $d$
(4.1) has degree $d$; a line meets a cubic in three points (the chord-tangent construction of Chapter 9). Reference:
Fulton 5.3; Hartshorne I.7. Paper: background.

**2.4 `thm:curves:smooth-model`** (theorem; R). Every curve, possibly singular or affine, is birational over $k$ to a smooth
projective curve, unique up to isomorphism (follows from 3.3). Example: the node $y^2=x^3+x^2$ is birational to $\mathbb P^1$ via
$t=y/x$, $x=t^2-1$, $y=t(t^2-1)$ (P). Reference: Hartshorne I.6; Fulton, Chapter 7. Paper: background ("the curve given by an
equation" always means its smooth projective model; Chapter 14's models of $X_0(N)$).

### Section 3. Function fields, points over extensions, the Galois action

**3.1 `def:curves:function-field`** (definition and proposition; P for (ii), (iii); R for (i), (iv)). (i) A *function field of
one variable over $k$* is a finitely generated field extension $K/k$ of transcendence degree $1$ in which $k$ is
algebraically closed; $k(C)$ is one (R). (ii) For $C$ smooth, each $P\in C(\bar k)$ gives the valuation $\operatorname{ord}_P$ on $\bar k(C)$
(2.2), with $\operatorname{ord}_P(c)=0$ for $c\in\bar k^\times$. (iii) If $f\in\bar k(C)^\times$, then $\operatorname{ord}_P f=0$ for all but finitely many $P$ (P on
a plane model: zeros and poles lie on $V(f)$, $V(g)$ for $f=g/h$, finite sets by Bezout or by dimension). (iv) A function with
no poles is constant (R here; P after 6.4). Reference: SilvermanAEC II.1 (Proposition 1.2); Hartshorne I.6. Paper: background.

**3.2 `thm:curves:extend-morphism`** (theorem; P). Let $C$ be a smooth curve, $V\subseteq\mathbb P^n$ a projective variety and
$\varphi=[f_0:\dots:f_n]\colon C\dashrightarrow V$ a rational map. Then $\varphi$ is a morphism. Proof: at $P$ put $m=\min_i\operatorname{ord}_P f_i$; then
$t_P^{-m}f_i$ are regular at $P$ and one is nonzero there. Corollaries: a rational map between smooth projective curves is a
morphism; every $f\in\bar k(C)$ is a morphism $f=[f:1]\colon C\to\mathbb P^1$ (constant or not). Reference: SilvermanAEC II.2 (Proposition
2.1). Paper: background.

**3.3 `thm:curves:equivalence`** (theorem; R). The functor $C\mapsto k(C)$, $(\varphi\colon C_1\to C_2)\mapsto(\varphi^*\colon k(C_2)\to k(C_1))$
is an equivalence (contravariant) between the category of smooth projective curves over $k$ with nonconstant morphisms
defined over $k$, and function fields of one variable over $k$ with $k$-embeddings. Consequences: two smooth projective
curves with isomorphic function fields are isomorphic; a morphism of degree $1$ (6.2) is an isomorphism. Reference:
Hartshorne I.6 (Corollary 6.12); SilvermanAEC II.2 (Theorem 2.4). Paper: background (Section 1: $\varphi_E$ corresponds to
$\Q(E)\hookrightarrow\Q(X_0(N))$, of degree $\deg\varphi_E$).

**3.4 `prop:curves:galois-action`** (proposition; P). Let $C$ be a curve over $k$. (i) $G_k$ acts on $C(\bar k)$, and
$C(\bar k)^{G_L}=C(L)$ for $k\subseteq L\subseteq\bar k$ (from 1.2(i)). (ii) $G_k$ acts on $\bar k(C)$ through the coefficients, with fixed field
$k(C)$ (R for the fixed field: Hilbert 90 for $\bar k(C)$, SilvermanAEC II.5); for $f\in\bar k(C)$ regular at $P$,
$(\sigma f)(\sigma P)=\sigma(f(P))$, and $\operatorname{ord}_{\sigma P}(\sigma f)=\operatorname{ord}_P f$. (iii) A morphism $\varphi$ defined over $k$ satisfies $\varphi(\sigma P)=\sigma\varphi(P)$;
so $\varphi(C_1(L))\subseteq C_2(L)$, and the fibres $\varphi^{-1}(Q)$ over $Q\in C_2(k)$ are $G_k$-stable. (iv) Examples: the conic
$X^2+Y^2+Z^2=0$ over $\Q$ has $C(\Q)=\emptyset$ (no real points) but $C(\Q(i))\ni[1:i:0]$, so it is a genus-$0$ curve not isomorphic
over $\Q$ to $\mathbb P^1$; Selmer's cubic $3X^3+4Y^3+5Z^3=0$ is smooth of genus $1$ with no rational point (stated). Reference:
SilvermanAEC I.1 to I.3 and II.2 (cite the sections). Paper: Section 1.1 ($\rho_{E,\ell}$ is the action of 3.4(i) on
$E[\ell^n]\subset E(\bar\Q)$; Chapters 9, 11), Proposition prop:ns (the action on $E[3]$ and on the roots of the
$3$-division polynomial), Section 4.2 ($G_\Q$ acting on $H^1$; 11.8).

### Section 4. Divisors, differentials, the Picard group

**4.1 `def:curves:divisor`** (definitions and proposition; P given 6.4 for (iii)). For a smooth curve $C$: $\operatorname{Div}(C)$ is the
free abelian group on $C(\bar k)$; $\deg\sum n_P(P)=\sum n_P$; $D\ge0$ (effective); $\operatorname{supp}D$; $G_k$ acts, and
$\operatorname{Div}_k(C)=\operatorname{Div}(C)^{G_k}$ (divisors *defined over $k$*; a $G_k$-orbit of points is one example). (i) The divisor of
$f\in\bar k(C)^\times$ is $\operatorname{div}(f)=\sum_P\operatorname{ord}_P(f)(P)$ (a finite sum by 3.1(iii)); principal divisors form a subgroup,
$\operatorname{div}(fg)=\operatorname{div}f+\operatorname{div}g$. (ii) $\operatorname{div}(f)=0$ iff $f\in\bar k^\times$ (3.1(iv)). (iii) $\deg\operatorname{div}(f)=0$: for $f$
nonconstant, $\operatorname{div}(f)=f^*((0))-f^*((\infty))$ for $f\colon C\to\mathbb P^1$, and both have degree $\deg f$ by 6.4(iii). Over $\C$ a second
proof by the residue theorem (9.2). Example: on $\mathbb P^1$, $\operatorname{div}(x-a)=(a)-(\infty)$. Reference: SilvermanAEC II.3 (Proposition
3.1). Paper: background (Abel-Jacobi, 11.2; Chapter 9's group law).

**4.2 `def:curves:picard`** (definitions and proposition; P except (iii), R). $D\sim D'$ (linearly equivalent) iff $D-D'$ is
principal. $\operatorname{Pic}(C)=\operatorname{Div}(C)/\operatorname{div}(\bar k(C)^\times)$; $\deg$ induces $\operatorname{Pic}(C)\to\Z$ with kernel
$\operatorname{Pic}^0(C)=\operatorname{Div}^0(C)/\operatorname{Prin}(C)$. (i) $\operatorname{Pic}^0(\mathbb P^1)=0$: a degree-$0$ divisor $\sum n_i(a_i)+n_\infty(\infty)$ is
$\operatorname{div}\prod(x-a_i)^{n_i}$. (ii) $G_k$ acts on $\operatorname{Pic}^0(C)$. (iii) The natural map
$\operatorname{Div}^0_k(C)/\operatorname{div}(k(C)^\times)\to\operatorname{Pic}^0(C)^{G_k}$ is injective (Hilbert 90 for $\bar k(C)$) and bijective when $C(k)\ne\emptyset$
(R; Hilbert 90, Chapter 17). Reference: SilvermanAEC II.3; Milne,
Jacobian varieties, Section 1 (cite the section). Paper: background (the definition of $J$ in 11.1).

**4.3 `def:curves:differentials`** (definition and proposition; R for (i), (ii); P for (iii), (iv)). The space $\Omega_C$ of
(meromorphic) differentials of $C$: the $\bar k(C)$-vector space generated by symbols $df$, $f\in\bar k(C)$, modulo $d(f+g)=df+dg$,
$d(fg)=f\,dg+g\,df$, $da=0$ for $a\in\bar k$. (i) $\Omega_C$ is one-dimensional over $\bar k(C)$, and $df$ is a basis iff $\bar k(C)/\bar k(f)$
is a finite separable extension (in characteristic $p$: $d(f^p)=0$). (ii) For a uniformiser $t$ at $P$, every $\omega$ is $g\,dt$ and
$\operatorname{ord}_P\omega:=\operatorname{ord}_P g$ does not depend on $t$; $\operatorname{ord}_P\omega=0$ for almost all $P$; $\operatorname{div}(\omega)=\sum\operatorname{ord}_P(\omega)(P)$;
$\operatorname{div}(f\omega)=\operatorname{div}f+\operatorname{div}\omega$. (iii) Hence all $\operatorname{div}(\omega)$, $\omega\ne0$, lie in one linear equivalence class, the
*canonical class* $K_C$; a *canonical divisor* is any $\operatorname{div}\omega$. (iv) $\omega$ is *regular* (holomorphic) if $\operatorname{div}\omega\ge0$; they form a
$\bar k$-vector space. Examples (P): on $\mathbb P^1$, $\operatorname{div}(dx)=-2(\infty)$, so no nonzero regular differential; on a smooth cubic
$y^2=h(x)$, $h$ squarefree of degree $3$, $\operatorname{char}k\ne2$, $\operatorname{div}(dx/y)=0$ (at a point with $y=0$, $y$ is a uniformiser and
$dx=2y\,dy/h'(x)$; at $\infty$, $t=x/y$ and $\operatorname{ord}_\infty(dx/y)=0$ by the computation $\operatorname{ord}x=-2$, $\operatorname{ord}y=-3$, $\operatorname{ord}dx=-3$). The
"invariant differential" and its translation invariance are Chapter 9's. Reference: SilvermanAEC II.4 (Propositions 4.2 and 4.3); Hartshorne II.8 and IV.1. Paper: background (weight-two cusp forms as
holomorphic differentials $f(z)\,dz$ on $X_0(N)$: Chapter 12; $\varphi_E^*\omega_E=2\pi ic f(z)dz$ with the Manin constant $c$: Chapter 14).

### Section 5. Riemann-Roch and its consequences

**5.1 `def:curves:riemann-roch-space`** (definition and proposition; P except (iv), R). For $D\in\operatorname{Div}(C)$,
$\mathcal L(D)=\{f\in\bar k(C)^\times:\operatorname{div}f+D\ge0\}\cup\{0\}$, a $\bar k$-vector space, $\ell(D)=\dim\mathcal L(D)$. (i) $\mathcal L(0)=\bar k$; $\mathcal L(D)=0$ if
$\deg D<0$ (by 4.1(iii)); $D\sim D'$ implies $\mathcal L(D)\simeq\mathcal L(D')$ (multiply by $h$ with $D'=D+\operatorname{div}h$). (ii)
$\ell(D+P)\le\ell(D)+1$ (the map $f\mapsto(t_P^{n+1}f)(P)$, $n$ the coefficient of $P$ in $D$, has kernel $\mathcal L(D)$); hence $\ell(D)\le\deg D+1$ for
$D\ge0$, and $\mathcal L(D)$ is finite-dimensional. (iii) Hence $\ell(D)$ and $\ell(K-D)$ depend only on the classes of $D$ and $K-D$ in $\operatorname{Pic}(C)$. (iv) If $D$ is
defined over $k$, $\mathcal L(D)$ has a basis in $k(C)$ (R; Hilbert 90 for vector spaces, SilvermanAEC II.5 (Proposition 5.8)).
Reference: SilvermanAEC II.5. Paper: background.

**5.2 `thm:curves:riemann-roch`** (theorem, Riemann-Roch; R, with the shape of the proof in one paragraph, S). Let $C$ be a
smooth projective curve over $k$ and $K$ a canonical divisor. There is an integer $g\ge0$, the *genus* of $C$, such that for
every $D\in\operatorname{Div}(C)$:
$$\ell(D)-\ell(K-D)=\deg D-g+1.$$
Shape of the proof: Riemann's inequality $\ell(D)\ge\deg D+1-g$ (with $g$ defined as the maximum defect) by comparing $\mathcal L(D)$ with
$\mathcal L(D+nP)$; the correction term $\ell(K-D)$ is the dimension of the space of obstructions to prescribing principal parts
("repartitions", the algebraic Mittag-Leffler problem), which is dual to $\mathcal L(K-D)$ via residues (Serre duality). Over $\C$
the obstruction space is $H^1(X,\mathcal O(D))$. Reference: SilvermanAEC II.5 (Theorem 5.4, proof referred to Hartshorne and
Lang); Hartshorne IV.1 (Theorem 1.3); Fulton, Chapter 8; Miranda, Chapter VI. Paper: background (everything below).

**5.3 `cor:curves:rr-consequences`** (corollary; P). (a) $\ell(K)=g$: the genus is the dimension of the space of regular
differentials ($D=0$, and $f\mapsto f\omega$ identifies $\mathcal L(\operatorname{div}\omega)$ with the regular differentials). (b) $\deg K=2g-2$ ($D=K$).
(c) If $\deg D>2g-2$ then $\ell(D)=\deg D-g+1$. (d) $g(\mathbb P^1)=0$ ($\operatorname{div}dx=-2(\infty)$); conversely a curve $C$ of genus $0$ with
$P\in C(k)$ is isomorphic over $k$ to $\mathbb P^1$ ($\ell(P)=2$ gives $f\in k(C)$ of degree $1$, an isomorphism by 3.3, 6.4); in
particular a curve with two points $P\ne Q$ and $(P)\sim(Q)$ has genus $0$. (e) If $g=1$: $\ell(D)=\deg D$ for $\deg D\ge1$, $K\sim0$, and
a nonzero regular differential has no zeros. Reference: SilvermanAEC II.5 (Corollary 5.5). Paper: background.

**5.4 `thm:curves:plane-genus`** (theorem; S). A smooth plane curve of degree $d$ over $k$ with $\operatorname{char}k\nmid d$ (or any
smooth plane curve with $\operatorname{char}k=0$) has genus $(d-1)(d-2)/2$. Sketch: with affine equation $f(x,y)=0$ and the line at
infinity in general position, $\omega_0=dx/f_y=-dy/f_x$ is regular and nowhere zero on the affine part, and
$\operatorname{div}(\omega_0)=(d-3)\cdot(\text{line at infinity})$, of degree $d(d-3)$ by Bezout (2.3); so $2g-2=d(d-3)$ by 5.3(b). The regular
differentials are exactly $h(x,y)\,\omega_0$ with $\deg h\le d-3$ ("adjoint differentials"), a space of dimension $\binom{d-1}{2}$. Reference:
Fulton, Chapter 8 (cite the chapter); Hartshorne IV.1 and I.7 (cite the sections); Miranda, Chapter VII. Paper:
background (lines and conics have genus $0$; smooth cubics genus $1$, Chapter 9).

**5.5 `ex:curves:genus-examples`** (examples; P given 5.4 and 7.2). (a) Lines and smooth conics: $g=0$. (b) Smooth plane cubics,
in particular every smooth Weierstrass cubic (11a1, 20a1, 121a1 of 2.1): $g=1$, with $\omega=dx/(2y+a_1x+a_3)$ regular and nowhere zero.
(c) The Fermat quartic $X^4+Y^4+Z^4=0$: $g=3$. (d) Hyperelliptic curves: the smooth projective model of $y^2=h(x)$, $h$
squarefree of degree $2g+1$ or $2g+2$, $\operatorname{char}k\ne2$, has genus $g$ (7.3(c)); $y^2=x^5-x$ has genus $2$. (e) Singular plane
models have smaller genus: the nodal and cuspidal cubics are rational (2.4); the general formula
$g=\frac{(d-1)(d-2)}2-\sum_P\delta_P$ is stated (R; Fulton, Chapter 7; Hartshorne IV.1 (cite the section)). (f) The
modular curves are not given as smooth plane curves; their genera come from Riemann-Hurwitz (7.3(f), Chapter 12):
$g(X_0(11))=1$, $g(X_0(20))=1$, $g(X_0(121))=6$, $g(X_0(539))=49$ (computed from Chapter 12's genus formula, Part 6.6). Paper:
background; Section 1 (the curves 11a1, 20a1, 121a1, 539c1).

**5.6 `thm:curves:genus-one-weierstrass`** (theorem; P for the equation, S for the isomorphism). Let $C$ be a smooth
projective curve of genus $1$ over $k$ and $O\in C(k)$. (i) There are $x\in\mathcal L(2(O))$ and $y\in\mathcal L(3(O))$, defined over $k$, with
$\mathcal L(2(O))=\langle1,x\rangle$ and $\mathcal L(3(O))=\langle1,x,y\rangle$ ($\operatorname{ord}_Ox=-2$, $\operatorname{ord}_Oy=-3$; by 5.3(e) and 5.1(iv)). (ii) The seven functions
$1,x,y,x^2,xy,y^2,x^3$ lie in the six-dimensional $\mathcal L(6(O))$, so they satisfy a linear relation over $k$, in which $y^2$ and $x^3$
occur with nonzero coefficients (they are the only ones with a pole of order $6$ at $O$); rescaling $x$, $y$ gives
$$y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6,\qquad a_i\in k.$$
(iii) The morphism $\phi=[x:y:1]\colon C\to\mathbb P^2$ is an isomorphism onto the projective cubic $E$ defined by this equation, with
$\phi(O)=[0:1:0]$; $E$ is smooth. Sketch of (iii): $[k(C):k(x)]=2$ and $[k(C):k(y)]=3$ (6.4: degrees of pole divisors), so $k(C)=k(x,y)$ and
$\phi$ is birational onto its image; a singular cubic is rational (2.4), which would contradict $g=1$; so $E$ is smooth and $\phi$ is an
isomorphism by 3.3. (iv) Conversely a smooth Weierstrass cubic has genus $1$ (5.4) and the point $O=[0:1:0]$ is defined over $k$.
Reference: SilvermanAEC III.3 (Proposition 3.1). Paper: background (an elliptic curve over $\Q$ "is" a Weierstrass equation:
Section 1, the Appendix (`ellinit([1,1,1,-30,-76])`); Chapter 9 starts from here).

**5.7 `prop:curves:genus-one-pic`** (proposition; P). Let $C$ have genus $1$ and $O\in C(k)$. The map
$\kappa\colon C(\bar k)\to\operatorname{Pic}^0(C)$, $P\mapsto$ the class of $(P)-(O)$, is a bijection, commuting with $G_k$. Proof: surjective, because
for $D$ of degree $0$, $\ell(D+(O))=1$ (5.3(e)), so $D+(O)\sim(P)$ for the unique zero $P$ of a generator; injective, because $(P)\sim(Q)$
with $P\ne Q$ would force genus $0$ (5.3(d)). Consequence: $C(\bar k)$ inherits a group structure from $\operatorname{Pic}^0(C)$, with
identity $O$; Chapter 9 identifies it with the chord-tangent law (via $(P)+(Q)+(R)\sim3(O)$ for collinear $P,Q,R$ on a
Weierstrass cubic) and so gets associativity for free. Reference: SilvermanAEC III.3 (Proposition 3.4). Paper: background
($E=\operatorname{Pic}^0(E)=J(E)$, so $E$ is its own Jacobian: 11.4, 11.5 and Chapter 14's $E^\vee\to J_0(N)\to E$).

### Section 6. Morphisms and their degree; separability; the Frobenius morphism

**6.1 `thm:curves:constant-or-surjective`** (theorem; R for surjectivity, P for the rest). A morphism $\varphi\colon C_1\to C_2$ of
curves (C2) is constant or surjective. If it is nonconstant, $\varphi^*\colon\bar k(C_2)\to\bar k(C_1)$, $f\mapsto f\circ\varphi$, is an injection of
fields and $\bar k(C_1)$ is a finite extension of $\varphi^*\bar k(C_2)$ (both have transcendence degree $1$; finitely generated). Reference:
SilvermanAEC II.2 (Theorem 2.3); Hartshorne II.6. Paper: background.

**6.2 `def:curves:degree`** (definitions; P). For nonconstant $\varphi\colon C_1\to C_2$: $\deg\varphi=[\bar k(C_1):\varphi^*\bar k(C_2)]$; the separable
and inseparable degrees $\deg_s\varphi$, $\deg_i\varphi$ of this extension (Chapter 5, galois:separability), $\deg\varphi=\deg_s\varphi\deg_i\varphi$; $\varphi$ is
*separable* (purely inseparable) if the extension is. Constant maps have degree $0$. The *ramification index* at $P$ is
$e_\varphi(P)=\operatorname{ord}_P(\varphi^*t_{\varphi(P)})\ge1$ ($t_Q$ a uniformiser at $Q$). Pullback $\varphi^*\colon\operatorname{Div}(C_2)\to\operatorname{Div}(C_1)$,
$(Q)\mapsto\sum_{\varphi(P)=Q}e_\varphi(P)(P)$; pushforward $\varphi_*\colon\operatorname{Div}(C_1)\to\operatorname{Div}(C_2)$, $(P)\mapsto(\varphi(P))$. Reference:
SilvermanAEC II.2 and II.3. Paper: Section 1 ("$\deg\varphi_E$", the modular degree is the degree of the morphism
$\varphi_E\colon X_0(N)\to E$ in this sense).

**6.3 `thm:curves:degree-formula`** (theorem; S). For nonconstant $\varphi\colon C_1\to C_2$ and every $Q\in C_2(\bar k)$:
$$\sum_{P\in\varphi^{-1}(Q)}e_\varphi(P)=\deg\varphi.$$
Sketch: the integral closure $B$ of the DVR $A=\bar k[C_2]_Q$ in $\bar k(C_1)$ is a semilocal Dedekind domain, finite and free of rank
$\deg\varphi$ over $A$ (finiteness: R), whose maximal ideals are the $\mathfrak m_P$, $P\in\varphi^{-1}(Q)$, with $t_QB=\prod\mathfrak m_P^{e_\varphi(P)}$; then the
argument of Chapter 6, item 3.1 ($\sum e_if_i=n$) applies with all residue degrees $f_i=1$ because the residue fields are $\bar k$.
Physics aside: the number of sheets of a branched cover, counted with multiplicity, does not jump. Reference:
SilvermanAEC II.2 (Proposition 2.6); Hartshorne II.6 (Proposition 6.9). Paper: background (Section 1).

**6.4 `cor:curves:degree-three-ways`** (corollary; P given 6.3, except the "all but finitely many" in (ii), S). Let
$\varphi\colon C_1\to C_2$ be nonconstant. (i) $\deg\varphi=[\bar k(C_1):\varphi^*\bar k(C_2)]$ (definition). (ii) $\#\varphi^{-1}(Q)=\deg_s\varphi$ for all but
finitely many $Q\in C_2(\bar k)$; in characteristic $0$, or for separable $\varphi$, $\#\varphi^{-1}(Q)=\deg\varphi$ except over the finitely many
branch points (7.1). (iii) $\deg\varphi^*D=\deg\varphi\cdot\deg D$; $\varphi_*\varphi^*D=(\deg\varphi)D$; $\varphi^*\operatorname{div}(f)=\operatorname{div}(\varphi^*f)$;
$\varphi_*\operatorname{div}(h)=\operatorname{div}(N_{\bar k(C_1)/\varphi^*\bar k(C_2)}h)$ (R for the last); hence $\varphi^*$ and $\varphi_*$ induce homomorphisms of
$\operatorname{Pic}$ and $\operatorname{Pic}^0$ with $\varphi_*\varphi^*=[\deg\varphi]$ on $\operatorname{Pic}^0(C_2)$. (iv) (Over $\C$, proved in 8.2 and 10.3.)
$\deg\varphi$ is the number of preimages of a general point, and $\varphi^*$ on $H^2(\cdot,\Z)=\Z$ is multiplication by $\deg\varphi$. (v)
$\deg(\psi\circ\varphi)=\deg\psi\deg\varphi$; $\deg\varphi=1$ iff $\varphi$ is an isomorphism (3.3). (vi) For nonconstant $f\in\bar k(C)$, the degree of
$f\colon C\to\mathbb P^1$ is $[\bar k(C):\bar k(f)]$, the degree of its divisor of zeros, and the degree of its divisor of poles; so
$\deg\operatorname{div}f=0$ (4.1(iii)) and a function without poles is constant (3.1(iv)). Reference: SilvermanAEC II.2, II.3 (cite the sections). Paper: Section 1 and Lemma lem:hecke via Chapter 14: "$\deg\varphi_E$" in all three senses, and the
description "$E^\vee\to J_0(N)\to E$ is multiplication by $\deg\varphi_E$" of PLAN Chapter 14, which is (iii) on $\operatorname{Pic}^0$ with
$E=\operatorname{Pic}^0(E)$ (5.7).

**6.5 `prop:curves:separability-frobenius`** (proposition; P for (c) identities, S for (c) degree, R for (b)). (a) In
characteristic $0$ every nonconstant morphism of curves is separable (Chapter 5: characteristic-$0$ fields are perfect).
(b) In characteristic $p$, $\varphi$ is separable iff $\varphi^*\omega\ne0$ for one (equivalently every) nonzero differential $\omega$ on $C_2$; and
every nonconstant $\varphi$ factors as $C_1\xrightarrow{\phi_q}C_1^{(q)}\xrightarrow{\lambda}C_2$ with $q=\deg_i\varphi$ and $\lambda$ separable. (c) For
$k=\F_q$ and $C\subseteq\mathbb P^n$ defined over $\F_q$, the $q$-power Frobenius morphism $\phi_q\colon[x_0:\dots:x_n]\mapsto[x_0^q:\dots:x_n^q]$ maps $C$
to itself; $\phi_q^*\bar k(C)=\bar k(C)^q$, so $\phi_q$ is purely inseparable of degree $q$ (S) and $e_{\phi_q}(P)=q$ at every point; its fixed
points are $C(\F_q)$; on $C(\bar\F_q)$ it coincides with the action of the arithmetic Frobenius of $G_{\F_q}$ (C7). Reference:
SilvermanAEC II.2 (Proposition 2.11, Corollary 2.12) and II.4 (Proposition 4.2). Paper: background (Chapter 9: the Frobenius
endomorphism and $a_p=p+1-\#E(\F_p)$; Chapter 14: Eichler-Shimura).

### Section 7. Ramification and the Riemann-Hurwitz formula

**7.1 `def:curves:ramification`** (definition and proposition; P). $\varphi$ is *unramified* at $P$ if $e_\varphi(P)=1$, *ramified*
otherwise; $\varphi(P)$ is then a *branch point*. Ramification is *tame* at $P$ if $\operatorname{char}k\nmid e_\varphi(P)$, *wild* otherwise. For
separable $\varphi$ only finitely many points are ramified (from the differential formula in 7.2: $\operatorname{ord}_P\varphi^*\omega>e_P\operatorname{ord}_{\varphi P}\omega$ at
ramified $P$, and $\varphi^*\omega$ has finitely many zeros). Over $\C$ the local normal form is $z\mapsto z^{e}$ (8.2). Reference:
SilvermanAEC II.2 (cite the section). Paper: background.

**7.2 `thm:curves:riemann-hurwitz`** (theorem; P given 5.3(b) and 4.3). Let $\varphi\colon C_1\to C_2$ be a nonconstant separable morphism of
smooth projective curves of genera $g_1$, $g_2$. Then
$$2g_1-2\ \ge\ \deg\varphi\,(2g_2-2)+\sum_{P\in C_1}(e_\varphi(P)-1),$$
with equality iff every ramification is tame (always in characteristic $0$). Proof: for a nonzero $\omega$ on $C_2$ and $Q=\varphi(P)$,
writing $t_Q=ut_P^{e}$, one gets $\operatorname{ord}_P(\varphi^*\omega)=e\operatorname{ord}_Q(\omega)+\operatorname{ord}_P(dt_Q/dt_P)$ and $\operatorname{ord}_P(dt_Q/dt_P)\ge e-1$, with equality iff
$\operatorname{char}k\nmid e$; sum over $P$ using 6.3 and take degrees with 5.3(b). Topological proof over $\C$ (S, in 8.4): triangulate $C_2$
with the branch points as vertices, lift, and count $V-E+F$. Reference: SilvermanAEC II.5 (Theorem 5.9); Hartshorne IV.2
(Corollary 2.4). Paper: background (Section 1; Chapter 12's genus formula for $X_0(N)$).

**7.3 `cor:curves:rh-consequences`** (corollary and examples; P). Let $\varphi\colon C_1\to C_2$ be nonconstant and separable. (a) If
$g_2\ge1$ then $g_1\ge g_2$; if $g_1=0$ then $g_2=0$ (Lueroth's theorem, curve form). (b) If $g_1=g_2=1$ then $\varphi$ is unramified
($0\ge\deg\varphi\cdot0+\sum(e_P-1)$). In particular, in characteristic $0$ every nonconstant morphism between genus-one curves (every
isogeny, Chapter 9) is unramified, and $\#\varphi^{-1}(Q)=\deg\varphi$ for every $Q$. (c) The double cover $x\colon C\to\mathbb P^1$ of the hyperelliptic
curve $y^2=h(x)$ ($\deg h=2g+1$ or $2g+2$, squarefree, $\operatorname{char}k\ne2$) is branched at the $2g+2$ points (roots of $h$, and $\infty$ when
$\deg h$ is odd), so $2g_C-2=2(-2)+(2g+2)$ and $g_C=g$. (d) Fermat: the projection $[X:Y:Z]\mapsto[X:Y]$ of $X^d+Y^d+Z^d=0$ has degree $d$,
total ramification ($e=d$) over the $d$ roots of $X^d+Y^d=0$ and none elsewhere, so $2g-2=-2d+d(d-1)$, $g=(d-1)(d-2)/2$, agreeing
with 5.4. (e) For a nonconstant $\varphi\colon X\to E$ over $\C$ with $g(E)=1$: $\sum_P(e_\varphi(P)-1)=2g(X)-2$, whatever $\deg\varphi$. Examples (with
$g(X_0(N))$ from Chapter 12 and the degrees from Chapter 14 and the paper): $\varphi_{11a1}\colon X_0(11)\to$ 11a1 has degree $1$, so it is an
isomorphism and $X_0(11)$ is an elliptic curve; $X_0(20)\to$ 20a1 likewise; $\varphi_{121a1}$ has degree $6$ and total ramification
$2\cdot6-2=10$; $\varphi_{539c1}$ has degree $2^5\cdot3^2=288$ and total ramification $96$. (f) Forward pointer: the genus formula of $X_0(N)$
(Chapter 12) is 7.2 for $X_0(N)\to X_0(1)\simeq\mathbb P^1$, of degree $[\mathrm{SL}_2(\Z):\Gamma_0(N)]$, ramified only over $j=0$, $1728$, $\infty$.
Reference: SilvermanAEC II.5 (exercises); Miranda, Chapter II. Paper: Section 1 (the parametrisations of 11a1, 121a1, 539c1
quoted in the Example of Section 3 and the Appendix).

### Section 8. Compact Riemann surfaces and smooth projective complex curves

**8.1 `def:curves:riemann-surface`** (definitions and examples; P for the examples). A *Riemann surface* is a connected
Hausdorff second-countable topological surface with a maximal atlas whose transition maps are holomorphic; holomorphic and
meromorphic functions, holomorphic maps between Riemann surfaces. Examples: (a) $\C$; (b) the Riemann sphere
$\mathbb P^1(\C)$ with charts $z$ and $1/z$; (c) $\C/\Lambda$ for a lattice $\Lambda=\Z\omega_1+\Z\omega_2$ (charts: local inverses of the
projection; compact, genus $1$; Chapter 9 does the Weierstrass $\wp$-function and the uniformisation of elliptic curves);
(d) the smooth points of an affine plane curve $f(x,y)=0$ (implicit function theorem: near a point with $f_y\ne0$, $x$ is a
chart); (e) hence $C(\C)$ for a smooth projective curve $C$ over $\C$ is a compact Riemann surface ($\mathbb P^n(\C)$ is compact). (f)
(Forward pointer, Chapter 12.) $\Gamma_0(N)\backslash\mathbb H$ compactified by the cusps, with special charts at the cusps and elliptic
points, is the compact Riemann surface $X_0(N)(\C)$. Reference: Miranda, Chapters I and II; Forster, Section 1. Paper:
background (Section 1: $X_0(N)$).

**8.2 `thm:curves:holomorphic-maps`** (theorem; P). Let $F\colon X\to Y$ be a nonconstant holomorphic map of compact Riemann
surfaces. (a) Local normal form: for each $P$ there are charts $z$ at $P$ and $w$ at $F(P)$, centred at $0$, with $w=z^{e}$; the
integer $e=\operatorname{mult}_P(F)\ge1$ is independent of the charts (if $w\circ F$ has a zero of order $e$, it is $h^e$ with $h$
holomorphic, $h'(0)\ne0$, and $h$ is a chart). (b) $F$ is open and surjective, and its fibres are finite. (c)
$d=\sum_{P\in F^{-1}(Q)}\operatorname{mult}_P(F)$ does not depend on $Q\in Y$ (locally constant by (a) and properness; $Y$ connected): the *degree*
of $F$. (d) $\operatorname{mult}_P(F)=1$ except at finitely many points, so $\#F^{-1}(Q)=d$ except over finitely many $Q$. (e) $F$ preserves
orientation: in local coordinates the real Jacobian determinant is $|F'(z)|^2\ge0$. Reference: Miranda, Chapter II
(Section 4; cite the section); Forster, Section 2. Paper: background.

**8.3 `thm:curves:riemann-existence`** (theorem; R). (a) (Riemann.) On a compact Riemann surface $X$ the meromorphic functions
separate points and give local coordinates; the field $\mathcal M(X)$ is a function field of one variable over $\C$. (b)
(Equivalence; GAGA for curves.) $X\mapsto\mathcal M(X)$ and $C\mapsto C(\C)$ give an equivalence between compact connected Riemann surfaces
with nonconstant holomorphic maps and smooth projective curves over $\C$ with nonconstant morphisms, under which: meromorphic
functions are rational functions; the order of a zero is $\operatorname{ord}_P$; $\operatorname{mult}_P(F)=e_F(P)$; the analytic degree of 8.2(c) is
$\deg F$ of 6.2; holomorphic differentials are regular algebraic differentials; divisors, linear equivalence and
$\operatorname{Pic}$ agree. (c) The algebraic genus $g=\ell(K)$ equals the topological genus (8.4). Reference: Miranda, Chapters VI and
VII (Riemann existence and the algebraic curve of a Riemann surface); Hartshorne, Appendix B (GAGA); Forster, Sections 14
and 16 (cite the sections). Paper: Section 1 ($X_0(N)$ is constructed analytically in Chapter 12 and is an algebraic curve
over $\Q$ in Chapter 14; $\varphi_E$ is at once a holomorphic map and a morphism, and $\deg\varphi_E$ means the same in both senses).

**8.4 `thm:curves:topology`** (theorem; R for (a), (b); S for (c)). (a) A compact Riemann surface is an orientable compact
surface, homeomorphic to a sphere with $g$ handles (classification of surfaces); $\chi(X)=2-2g$. (b) This $g$ is the genus of
5.2. (c) Topological Riemann-Hurwitz: for $F\colon X\to Y$ of degree $d$, $\chi(X)=d\,\chi(Y)-\sum_P(\operatorname{mult}_P F-1)$ (lift a triangulation
of $Y$ having the branch points among its vertices; each face and edge has $d$ lifts, a vertex $Q$ has $\#F^{-1}(Q)$ lifts).
Physics aside: Euler's $V-E+F$. Reference: Miranda, Chapters I and II (cite the chapters); Forster, Section 17.
Paper: background.

### Section 9. Holomorphic differentials, residues, periods

**9.1 `def:curves:holomorphic-differential`** (definitions; P). A meromorphic (holomorphic) $1$-form on $X$: $f(z)\,dz$ in each chart,
with $f$ meromorphic (holomorphic), transforming by $f(z)\,dz=f(z(w))z'(w)\,dw$; $\operatorname{ord}_P\omega$, $\operatorname{div}\omega$; the residue $\operatorname{res}_P\omega$
(coefficient of $z^{-1}$, chart-independent); $H^0(X,\Omega^1)$, the space of holomorphic $1$-forms. Smooth real and complex $1$- and
$2$-forms, $d$, $\wedge$, $\int_X$ of $2$-forms; Stokes' theorem on a compact surface with boundary (from the background real
analysis, R). Line integrals $\int_\gamma\omega$; a holomorphic $1$-form is closed ($d(f\,dz)=\bar\partial f\wedge dz=0$). Examples: $dz$ on $\C/\Lambda$;
$\mathbb P^1$ has none ($dz=-w^{-2}dw$). Reference: Miranda, Chapter IV. Paper: background (Chapter 12: $f\mapsto f(z)\,dz$ identifies
$S_2(\Gamma_0(N))$ with $H^0(X_0(N),\Omega^1)$).

**9.2 `thm:curves:residue`** (theorem; P). For a meromorphic $1$-form $\omega$ on a compact Riemann surface,
$\sum_{P\in X}\operatorname{res}_P\omega=0$ (Stokes on $X$ minus small discs around the poles). Corollary: for $f\in\mathcal M(X)^\times$,
$\deg\operatorname{div}f=\sum_P\operatorname{res}_P(df/f)=0$ (argument principle); a second proof of 4.1(iii) over $\C$. Physics aside: the total charge
on a closed surface is zero. Reference: Miranda, Chapter IV (cite the chapter). Paper: background.

**9.3 `thm:curves:genus-dimension`** (theorem; R via 8.3 and 5.3). $\dim_\C H^0(X,\Omega^1)=g$ and $\deg\operatorname{div}\omega=2g-2$ for every
meromorphic $\omega\ne0$. Examples: $H^0(\C/\Lambda,\Omega^1)=\C\,dz$; $H^0(\mathbb P^1,\Omega^1)=0$. Forward pointer: $\dim S_2(\Gamma_0(N))=g(X_0(N))$ (Chapter 12),
e.g. $\dim S_2(\Gamma_0(121))=6$. Reference: Miranda, Chapter VII. Paper: background (multiplicity one and the genus, Chapter 12).

**9.4 `thm:curves:bilinear-relations`** (theorem; P for (a), (b); S for (c), (d)). Let $X$ have genus $g\ge1$ and let
$a_1,\dots,a_g,b_1,\dots,b_g$ be a symplectic basis of $H_1(X,\Z)$ (10.1). (a) For $\omega,\eta\in H^0(X,\Omega^1)$: $\int_X\omega\wedge\eta=0$ ($dz\wedge dz=0$). (b)
For $\omega\ne0$ holomorphic: $\frac i2\int_X\omega\wedge\bar\omega>0$ (locally $\frac i2|f|^2dz\wedge d\bar z=|f|^2dx\wedge dy$). (c) For closed $1$-forms $\alpha,\beta$:
$$\int_X\alpha\wedge\beta=\sum_{j=1}^g\Bigl(\int_{a_j}\alpha\int_{b_j}\beta-\int_{b_j}\alpha\int_{a_j}\beta\Bigr)$$
(S: cut $X$ along the basis to a $4g$-gon and apply Stokes; checked on the torus, 10.4, where it gives $\int dx\wedge dy=1$). (d)
Riemann's bilinear relations, with periods $A_j(\omega)=\int_{a_j}\omega$, $B_j(\omega)=\int_{b_j}\omega$: $\sum_j(A_j(\omega)B_j(\eta)-B_j(\omega)A_j(\eta))=0$ and
$\sum_j\operatorname{Im}\bigl(\overline{A_j(\omega)}B_j(\omega)\bigr)>0$ for $\omega\ne0$ (from (a) to (c); signs checked on $\C/(\Z+\tau\Z)$ with $\omega=dz$, $A=1$, $B=\tau$,
where the inequality is $\operatorname{Im}\tau>0$). (e) Consequence: a holomorphic form with all $A$-periods zero is zero, so the period map
$H_1(X,\Z)\to H^0(X,\Omega^1)^\vee$ is injective with image a lattice (11.2). Physics aside: (b) is a norm $\int|f|^2$; the Petersson
product of Chapter 12 is $\frac i2\int\omega\wedge\bar\eta$ up to normalisation, and the area of a period parallelogram is (b) for $dz$.
Reference: Miranda, Chapter VIII (cite the chapter); Griffiths-Harris, Chapter 2, Section 2 (cite the section). Paper:
background (Section 1: the Petersson norm and the area of the period lattice in the Zagier-Watkins formula, Chapter 14).

### Section 10. $H_1$, $H^1$ and the cup product

**10.1 `def:curves:homology`** (definitions and theorem; R, with the torus and the picture of the $g$-holed surface). $H_1(X,\Z)$:
the abelianisation of $\pi_1(X)$, equivalently singular homology (closed oriented loops modulo boundaries, for the reader).
(i) $H_1(X,\Z)$ is free of rank $2g$, with a *symplectic basis* $a_1,\dots,a_g,b_1,\dots,b_g$ (the $a_j$ around and the $b_j$ through the
$j$-th handle). (ii) The intersection pairing $H_1\times H_1\to\Z$ (signed count of transverse crossings, C6) is bilinear,
alternating and perfect, with $a_i\cdot b_j=\delta_{ij}$, $a_i\cdot a_j=b_i\cdot b_j=0$. (iii) $H_1(X,A):=H_1(X,\Z)\otimes A$ for $A=\Z/n,\Z_\ell,\R,\C$.
Physics aside: the intersection number is a signed crossing count, like a winding or linking number. Reference: Miranda,
Chapter VIII (Section 1); Forster, Section 21; Farkas-Kra III.1 (cite the sections). Paper: background (Chapter 14: $H_1(X_0(N),\Z)$
and $J_0(N)(\C)=S_2^\vee/H_1$).

**10.2 `def:curves:cohomology`** (definitions and proposition; P for (i), R for (ii), S for (iii), R for (iv)). (i)
$H^1(X,\Z):=\Hom(H_1(X,\Z),\Z)$, free of rank $2g$; $H^1(X,A):=\Hom(H_1(X,\Z),A)=H^1(X,\Z)\otimes A$ for $A=\Z/n,\Z_\ell,\R,\C$ (since $H_1$ is
free of finite rank). (This agrees with singular cohomology by the universal coefficient theorem, $H_0$ being free; R.) (ii)
(de Rham.) $H^1_{\mathrm{dR}}(X)=\{\text{closed smooth }1\text{-forms}\}/d\{\text{smooth functions}\}\simeq H^1(X,\R)$ via $\alpha\mapsto(\gamma\mapsto\int_\gamma\alpha)$; under it
$H^1(X,\Z)$ is the lattice of classes with integral periods. $H^2(X,\Z)\simeq\Z$ via $\int_X$ (orientation, C6). (iii) (Hodge.)
$H^1(X,\C)=H^0(X,\Omega^1)\oplus\overline{H^0(X,\Omega^1)}$ (S: the map is injective by 9.4(b) and both sides have dimension $2g$ by 9.3). (iv)
For $g\ge1$, $X$ is a $K(\pi,1)$ (its universal cover is $\C$ or the disc), so $H^1(X,M)=H^1(\pi_1(X),M)$ in the sense of Chapter 16,
and the cup products agree (R); this is the bridge to the group-cohomological $H^1$ of $\Gamma_0(N)$ used by DFG04 (Chapter 14).
Reference: Miranda, Chapter VIII; Forster, Sections 12 and 19 (de Rham, Dolbeault); Griffiths-Harris, Chapter 0 (cite the
sections). Paper: Section 4.1 ("$H^1(X_0(M^\Sigma),\Z_\ell)$"), Lemma lem:hecke ($L=H^1(X_0(N),\Z_\ell)_{\mathfrak m}$), Theorem thm:quant Step 2.

**10.3 `thm:curves:cup-product`** (theorem; R for perfectness in general (Poincare duality), P for the rest given 10.1 and 9.4(c)).
The cup product $\langle\ ,\ \rangle\colon H^1(X,\Z)\times H^1(X,\Z)\to H^2(X,\Z)=\Z$, $\langle\alpha,\beta\rangle=\int_X\alpha\wedge\beta$, is bilinear, alternating
($\langle\alpha,\alpha\rangle=0$, so $\langle\alpha,\beta\rangle=-\langle\beta,\alpha\rangle$) and perfect: if $(\alpha_j,\beta_j)$ is the basis dual to a symplectic basis $(a_j,b_j)$
($\alpha_i(a_j)=\delta_{ij}$, $\alpha_i(b_j)=0$, $\beta_i(b_j)=\delta_{ij}$, $\beta_i(a_j)=0$), then by 9.4(c) $\langle\alpha_i,\beta_j\rangle=\delta_{ij}$ and $\langle\alpha_i,\alpha_j\rangle=\langle\beta_i,\beta_j\rangle=0$: the Gram
matrix is $\begin{psmallmatrix}0&I_g\\-I_g&0\end{psmallmatrix}$, of determinant $1$. The map $\operatorname{PD}\colon H^1(X,\Z)\to H_1(X,\Z)$ defined by
$\int_{\operatorname{PD}(\alpha)}\beta=\langle\alpha,\beta\rangle$ is an isomorphism (Poincare duality) and an isometry: $\langle\alpha,\beta\rangle=\operatorname{PD}(\alpha)\cdot\operatorname{PD}(\beta)$ ($\operatorname{PD}(\alpha_j)=b_j$,
$\operatorname{PD}(\beta_j)=-a_j$). Base change: for any commutative ring $R$ (in particular $\Z_\ell$, $\F_\ell$, $\Q_\ell$, $\C$) the extended pairing on
$H^1(X,R)$ is perfect and alternating (Chapter 3, 9.1(iii)). (Over $\R$ nondegeneracy also follows from 9.4(b) and 10.2(iii).)
Reference: Miranda, Chapter VIII; Griffiths-Harris, Chapter 0, Section 4 (cite the section); Hatcher, Section 3.3 (for
Poincare duality in general; not in refs.bib). Paper: Section 4.1 ("perfect and alternating on $H^1(X_0(M^\Sigma),\Z_\ell)$"), Lemma
lem:hecke and Lemma lem:ddt417 (the module $L$ "with a perfect $\mathcal O$-bilinear pairing"), Theorem thm:quant Step 2, PLAN Section 6
row "$H^1(X_0(N),\Z_\ell)$, cup product".

**10.4 `ex:curves:torus`** (example; P). $X=\C/\Lambda$, $\Lambda=\Z\omega_1+\Z\omega_2$, $\operatorname{Im}(\omega_2/\omega_1)>0$; real coordinates $z=s\omega_1+t\omega_2$, $s,t\in\R/\Z$.
$H_1=\Lambda$ with $a=[0,\omega_1]$, $b=[0,\omega_2]$, $a\cdot b=+1$. $H^1(X,\Z)$ has basis $ds$, $dt$ (dual to $a$, $b$), $\langle ds,dt\rangle=\int ds\wedge dt=1$, and
$\operatorname{PD}(ds)=b$, $\operatorname{PD}(dt)=-a$. The holomorphic form $dz=\omega_1ds+\omega_2dt$ has periods $(\omega_1,\omega_2)$, and
$\frac i2\int dz\wedge d\bar z=\operatorname{Im}(\bar\omega_1\omega_2)$ is the area of the period parallelogram (9.4(b), (d)). $[-1]\colon z\mapsto-z$ acts by $-1$ on
$H_1$ and $H^1$; multiplication by an integer $m$ acts by $m$ on $H_1$ and $H^1$ and by $m^2$ on $H^2$, so has degree $m^2$ (6.4(iv)).
Physics aside: $\Lambda$ is a crystal lattice, $H^1(X,\Z)=\Lambda^\vee$ its reciprocal lattice, $ds\wedge dt$ the normalised volume form of the
periodic box. Paper: background (genus one: $E(\C)$, Chapter 9; Section 1, the period lattice $\Lambda_E$).

### Section 11. The Jacobian: $\operatorname{Pic}^0$, complex torus, abelian variety; torsion and Tate modules

**11.1 `def:curves:jacobian`** (definition; P). For a smooth projective curve $C$ over $k$, $J(C)(\bar k):=\operatorname{Pic}^0(C)$, with its $G_k$-action
(4.2). Examples: $J(\mathbb P^1)=0$; for $g=1$ and $O\in C(k)$, $J(C)\simeq C$ via 5.7. Reference: SilvermanAEC II.3; Milne, Jacobian varieties,
Section 1. Paper: Remark rem:free ($J_0(N)$), Chapter 14.

**11.2 `thm:curves:abel-jacobi`** (theorem; P for (i), (ii), (iv); R for (iii)). Let $X$ be a compact Riemann surface of genus
$g\ge1$. (i) The period map $H_1(X,\Z)\to H^0(X,\Omega^1)^\vee$, $\gamma\mapsto(\omega\mapsto\int_\gamma\omega)$, is injective and its image $\Lambda_X$ is a lattice
(9.4(e) and 10.2(iii): a class pairing to zero with $H^0(\Omega^1)$ and its conjugate is zero in $H_1(X,\R)$). So
$J_{\mathrm{an}}(X)=H^0(X,\Omega^1)^\vee/\Lambda_X$ is a complex torus of dimension $g$. (ii) The *Abel-Jacobi map*
$u\colon\operatorname{Div}^0(X)\to J_{\mathrm{an}}(X)$, $\sum_i((P_i)-(Q_i))\mapsto\bigl(\omega\mapsto\sum_i\int_{Q_i}^{P_i}\omega\bigr)\bmod\Lambda_X$, is a well-defined homomorphism (changing
paths changes the integral by a period). (iii) Abel's theorem: $\ker u=\operatorname{Prin}(X)$. Jacobi inversion: $u$ is surjective. Hence
$u\colon\operatorname{Pic}^0(X)\xrightarrow{\sim}J_{\mathrm{an}}(X)$ (R; the "only if" half of Abel is a residue computation, S optional). (iv) For a base
point $P_0$, $\iota\colon X\to J_{\mathrm{an}}(X)$, $P\mapsto u((P)-(P_0))$, is holomorphic and injective (if $\iota(P)=\iota(Q)$, $P\ne Q$, then $(P)\sim(Q)$ and
$g=0$ by 5.3(d)), and $\iota_*\colon H_1(X,\Z)\to H_1(J_{\mathrm{an}},\Z)=\Lambda_X$ is the period isomorphism of (i) (S). For $g=1$: $X\simeq\C/\Lambda_X$, the
analytic form of 5.7 (Chapter 9 makes it explicit with $\wp$). Physics aside: $\Lambda_X$ is the lattice of periods, as in a
crystal. Reference: Miranda, Chapter VIII (Abel's theorem, Jacobi inversion); Forster, Sections 20 and 21; Griffiths-Harris,
Chapter 2, Section 2 (cite the sections). Paper: Remark rem:free, Chapter 14 ($J_0(N)(\C)=S_2(\Gamma_0(N))^\vee/H_1(X_0(N),\Z)$ via $f\mapsto f(z)dz$),
Section 1 (period lattice $\Lambda_E$).

**11.3 `thm:curves:jacobian-variety`** (theorem; R). Let $C$ be a smooth projective curve of genus $g\ge1$ over $k$. (i) There is an
abelian variety $J=\operatorname{Jac}(C)$ over $k$ of dimension $g$ (a smooth projective connected group variety) with
$J(\bar k)=\operatorname{Pic}^0(C)$ compatibly with $G_k$; $J(L)\supseteq\operatorname{Pic}^0_L(C)$ with equality when $C(L)\ne\emptyset$ (4.2(iii)). (ii) Over $\C$,
$J(\C)\simeq J_{\mathrm{an}}(C(\C))$ as complex Lie groups; the torus is algebraic because the cup product gives a Riemann form
(positivity 9.4) (Lefschetz, Riemann). (iii) Universal property (Albanese): for $P_0\in C(k)$, $\iota\colon C\to J$, $P\mapsto[(P)-(P_0)]$, is a
closed immersion for $g\ge1$, and every morphism $C\to A$ to an abelian variety over $k$ with $P_0\mapsto0$ factors uniquely as $h\circ\iota$
with $h\colon J\to A$ a homomorphism. (iv) Mordell-Weil: $J(K)$ is finitely generated for a number field $K$; in particular
$J(K)_{\mathrm{tors}}$ is finite. Reference: Milne, Jacobian varieties (Sections 1 to 6; cite the sections); Milne, Abelian
varieties; Mumford, Abelian varieties (Section 24 for the Weil pairing); BLR, Chapter 9 (the Picard functor). Paper: Section
1 ($\varphi_E$ factors as $X_0(N)\xrightarrow{\iota}J_0(N)\to E$, Chapter 14), Remark rem:free, Conjecture conj:eis and Open question 4
(torsion; cuspidal subgroup, Chapter 14).

**11.4 `prop:curves:jacobian-functoriality`** (proposition; P for (i), (ii), (iv); S for (iii)). Let $\varphi\colon X\to Y$ be a nonconstant
morphism of smooth projective curves. (i) $\varphi_*\colon J(X)\to J(Y)$ ("Albanese", pushforward of divisor classes) and
$\varphi^*\colon J(Y)\to J(X)$ ("Picard", pullback) are homomorphisms, defined over $k$ if $\varphi$ is, with $\varphi_*\varphi^*=[\deg\varphi]$ on $J(Y)$ (6.4(iii)).
(ii) Over $\C$, $\varphi_*$ is induced on $H^0(X,\Omega^1)^\vee/\Lambda_X\to H^0(Y,\Omega^1)^\vee/\Lambda_Y$ by the transpose of $\varphi^*\colon H^0(Y,\Omega^1)\to H^0(X,\Omega^1)$
and on lattices by $\varphi_*\colon H_1(X,\Z)\to H_1(Y,\Z)$ (change of variables $\int_\gamma\varphi^*\omega=\int_{\varphi_*\gamma}\omega$). (iii) $\varphi^*$ on $J$ is induced by
the trace of differentials and by the transfer $\varphi^!\colon H_1(Y)\to H_1(X)$ (lift a loop avoiding the branch points to its $\deg\varphi$
lifts; 12.2). (iv) For $Y=E$ of genus $1$ with origin $O=\varphi(P_0)$ and $J(E)=E$ (5.7), $\varphi_*\circ\iota_X=\varphi$: the morphism $\varphi$ factors
through $J(X)$ (the universal property 11.3(iii), made explicit), and $\varphi_*\circ\varphi^*\colon E\to J(X)\to E$ is multiplication by $\deg\varphi$.
Reference: Milne, Jacobian varieties, Section 6 (cite the section); Miranda, Chapter VIII. Paper: Section 1 (the modular
parametrisation and its degree; PLAN Chapter 14 "the composition $E^\vee\to J_0(N)\to E$ being multiplication by $\deg\varphi_E$" is (iv)
with $E^\vee=E$).

**11.5 `prop:curves:degree-cup-product`** (proposition; P, with the identification $H_1(X)=H_1(J(X))$ of 11.2(iv) used as S). Let
$\varphi\colon X\to Y$ be a nonconstant holomorphic map of compact Riemann surfaces, $d=\deg\varphi$. (i) $\langle\varphi^*x,\varphi^*y\rangle_X=d\,\langle x,y\rangle_Y$ for
$x,y\in H^1(Y,\Z)$ ($\int_X\varphi^*(\alpha\wedge\beta)=d\int_Y\alpha\wedge\beta$: away from the finitely many branch points $\varphi$ is a $d$-sheeted orientation-preserving
covering, 8.2). (ii) $\varphi_*\varphi^*=d$ on $H^1(Y,\Z)$ and $\varphi_*\varphi^!=d$ on $H_1(Y,\Z)$ (12.2 for $\varphi_*$ on $H^1$ and $\varphi^!$). (iii) The
following are equivalent: (a) $\varphi^*H^1(Y,\Z)$ is saturated in $H^1(X,\Z)$; (b) $\varphi_*\colon H_1(X,\Z)\to H_1(Y,\Z)$ is surjective; (c) the
homomorphism $\varphi_*\colon J(X)\to J(Y)$ has connected kernel; (d) $\varphi^*\colon J(Y)\to J(X)$ is injective. Proof of (b)$\Leftrightarrow$(c): for a surjective
homomorphism of complex tori $V/\Lambda\to W/M$ induced by $A\colon V\to W$, the group of components of the kernel is
$A^{-1}(M)/(\ker A+\Lambda)\simeq M/A(\Lambda)$, the cokernel on $H_1$. (a)$\Leftrightarrow$(b): $\varphi^*$ on $H^1$ is the transpose of $\varphi_*$ on $H_1$; $\varphi_*$ has finite cokernel (by (ii)),
so its transpose is injective with cokernel whose torsion is $\Hom(\operatorname{coker}\varphi_*,\Q/\Z)$; it is torsion-free iff $\varphi_*$ is
surjective (elementary divisors, Chapter 3, 5.3). (c)$\Leftrightarrow$(d): the torus-map form of (a) (S). (iv) If $Y=E$ has genus $1$ and (iii) holds, then
$M=\varphi^*H^1(E,\Z)$ is a saturated sublattice of rank $2$ on which the cup product has Gram determinant $d^2$ and ideal of values
$d\Z$ (by (i) and 10.3); by Chapter 3, 9.3, $[H^1(X,\Z):M\oplus M^\perp]=d^2$; the same holds over $\Z_\ell$ with $d$ replaced by $\ell^{v_\ell(d)}$. If
(iii) fails, the index of $M$ in its saturation is the order of the component group of $\ker(J(X)\to E)$. (v) Example: for an
isogeny $\psi\colon E\to E'$ of degree $n$ and $\varphi'=\psi\circ\varphi$, $(\varphi')^*H^1(E',\Z)$ has index $n$ in $\varphi^*H^1(E,\Z)$ (on $H_1$, $\psi_*$ is the inclusion
of $\Lambda$ in $\Lambda'$, of index $n=\#\ker\psi$), so $\varphi'$ never satisfies (iii) when $n>1$ and (iii) holds for $\varphi$. Reference: elementary
given 10.3 and 11.2; compare ARS12, Section 3 (cite the section) and Chapter 14. Paper: Section 1 (the modular degree,
"minimal degree" of the optimal parametrisation), Section 4.1 and Lemma lem:hecke (for $E$ optimal, Chapter 14 identifies
$M_{f,\lambda}=\varphi_E^*H^1(E,\Z_\ell)$, and then (iv) computes the ideal $\eta^\emptyset_{f,\lambda}$: Part 7, point 1), Remark rem:free, important_notes.md point 26 (Part
7, point 2).

**11.6 `prop:curves:torsion`** (proposition; P over $\C$, R over $k$). (i) For a complex torus $V/\Lambda$ of dimension $g$ and $n\ge1$:
$(V/\Lambda)[n]=\frac1n\Lambda/\Lambda\simeq\Lambda/n\Lambda\simeq(\Z/n)^{2g}$ (via $x\mapsto nx$). Hence $J(X)[n]\simeq H_1(X,\Z/n)$ for a compact Riemann surface
$X$, and $[n]\colon J\to J$ has degree $n^{2g}$. (ii) For $C$ over $k$ with $\operatorname{char}k\nmid n$: $J[n](\bar k)\simeq(\Z/n)^{2g}$ as groups, with a
continuous action of $G_k$ (R; Milne, Abelian varieties, Section 8). (iii) For a commutative ring $\mathbb T$ of endomorphisms of
$J$ and an ideal $\mathfrak a\subseteq\mathbb T$, $J[\mathfrak a]=\{P:tP=0\ \forall t\in\mathfrak a\}$ (definition); $J[\ell]$ is a $\mathbb T/\ell\mathbb T$-module, and for a maximal ideal
$\mathfrak m\ni\ell$, $J[\mathfrak m]$ is a $\mathbb T/\mathfrak m$-vector space (P). Paper: Remark rem:free ("$J_0(N)[\mathfrak m]$ is two-dimensional", "injects into
$J_1(N)[\mathfrak m']$"), Conjecture conj:eis (torsion), Chapter 14.

**11.7 `def:curves:tate-module`** (definition and proposition; P over $\C$, R over $k$). For a prime $\ell$:
$T_\ell J=\varprojlim_nJ[\ell^n]$ (transition maps multiplication by $\ell$), $V_\ell J=T_\ell J\otimes\Q_\ell$. (i) Over $\C$, the isomorphisms
$J[\ell^n]=\ell^{-n}\Lambda_X/\Lambda_X\to\Lambda_X/\ell^n\Lambda_X$, $x\mapsto\ell^nx$, are compatible with the transition maps and give a canonical isomorphism
$T_\ell J\simeq\Lambda_X\otimes\Z_\ell=H_1(X,\Z)\otimes\Z_\ell=H_1(X,\Z_\ell)$; so $T_\ell J$ is free of rank $2g$ and $T_\ell J/\ell^nT_\ell J=J[\ell^n]$. (ii)
**Duality**: $H^1(X,\Z_\ell)=\Hom(H_1(X,\Z),\Z_\ell)\simeq\Hom_{\Z_\ell}(T_\ell J,\Z_\ell)$ canonically: $H^1$ is the $\Z_\ell$-dual of the Tate module. (iii) Composing
with Poincare duality (10.3), $H^1(X,\Z_\ell)\simeq H_1(X,\Z_\ell)\simeq T_\ell J$, an isomorphism of $\Z_\ell$-modules which depends on the orientation
convention and is **not** Galois-equivariant when $X$ is defined over a number field (11.8(c)), and which intertwines a
correspondence acting by $\mathcal C^*$ on $H^1$ with its transpose acting on $T_\ell J$ (12.3(c)). (iv) Over $k$ with $\ell\ne\operatorname{char}k$: $T_\ell J$ is
free of rank $2g$ over $\Z_\ell$ with a continuous $G_k$-action (R). For $g=1$: $T_\ell J(E)=T_\ell E$ (Chapter 9). Reference: Milne, Abelian
varieties, Section 15 (cite the section); Mumford, Abelian varieties, Section 18 (cite the section). Paper: Remark rem:free
("the Tate module is free of rank two"; "$H^1(X_0(N),\Z_\ell)_{\mathfrak m}$"), Section 4.2 ($M_{f,\lambda}$ versus $T_\ell E$, important_notes.md point
26), PLAN hook "Tate modules of Jacobians".

**11.8 `thm:curves:weil-pairing-etale`** (theorem; R). Let $C$ be a smooth projective curve of genus $g$ over $k$, $J$ its Jacobian,
$\ell\ne\operatorname{char}k$. (a) (Weil pairing.) There is a perfect, alternating, $G_k$-equivariant $\Z_\ell$-bilinear pairing
$e_\ell\colon T_\ell J\times T_\ell J\to\Z_\ell(1)$ (from the canonical principal polarisation); over $\C$, after identifying $\Z_\ell(1)$ with $\Z_\ell$ by
$\zeta_{\ell^n}=e^{2\pi i/\ell^n}$, it is the intersection pairing of $H_1(X,\Z_\ell)$ up to a universal sign. For $g=1$ it is the Weil pairing of
Chapter 9, and $\det\rho_{E,\ell}=\chi_\ell$ follows. (b) (Etale cohomology.) $H^1_{\mathrm{et}}(C_{\bar k},\Z_\ell)$ is free of rank $2g$ with a continuous
$G_k$-action, and $H^1_{\mathrm{et}}(C_{\bar k},\Z_\ell)\simeq\Hom_{\Z_\ell}(T_\ell J,\Z_\ell)$ as $G_k$-modules (contragredient action, Chapter 4, C2); for $k\subseteq\C$
there is a comparison isomorphism $H^1_{\mathrm{et}}(C_{\bar k},\Z_\ell)\simeq H^1(C(\C),\Z)\otimes\Z_\ell$ compatible with 11.7(ii) and with cup products
(Artin). (c) Combining: $H^1_{\mathrm{et}}(C_{\bar k},\Z_\ell)\simeq T_\ell J(-1)=T_\ell J\otimes\Z_\ell(-1)$ as $G_k$-modules, and the cup product
$H^1\times H^1\to H^2_{\mathrm{et}}=\Z_\ell(-1)$ is perfect, alternating and $G_k$-equivariant. For $g=1$: $H^1(E,\Z_\ell)\simeq(T_\ell E)^\vee\simeq T_\ell E(-1)$, with
determinant $\chi_\ell^{-1}$. (d) (Weil.) For $k=\F_q$: the arithmetic Frobenius acts on $T_\ell J$ as the $q$-power Frobenius endomorphism
$\pi$ of $J$; $P(T)=\det(T-\pi\mid T_\ell J)$ has integer coefficients independent of $\ell$, degree $2g$, roots $\alpha_i$ with $|\alpha_i|=\sqrt q$, and
$\#C(\F_{q^n})=q^n+1-\sum_i\alpha_i^n$; on $H^1=(T_\ell J)^\vee$ the geometric Frobenius has the same eigenvalues $\alpha_i$. For $g=1$:
$a_q=q+1-\#E(\F_q)=\operatorname{tr}(\text{arithmetic Frobenius}\mid T_\ell E)=\operatorname{tr}(\text{geometric Frobenius}\mid H^1(E))$. Reference: Milne, Jacobian varieties
and Abelian varieties (Sections 16 and 19, cite the sections); Mumford, Abelian varieties, Section 20 (Weil pairing; cite the
section); Milne, Etale cohomology (lecture notes; not in refs.bib), the comparison theorem; SilvermanAEC III.8 and V.2 for
$g=1$. Paper: Section 4.2 and important_notes.md point 26 ($M_{f,\lambda}\subset H^1$ is homothetic to the dual of $T_\ell E$, that is to
$T_\ell E(-1)$, not to $T_\ell E$; the adjoints agree), Section 1.1 ($V=V_\ell E$), Chapter 6 C2/3.7 and important_notes.md point 11 and B1
(which Frobenius has which eigenvalues), Chapter 14 (Eichler-Shimura), Chapter 15 ($\rho_{f,\lambda}$ via $T_\ell$ of $A_f$ or via $H^1$).

### Section 12. Correspondences, their actions, and adjoints

**12.1 `def:curves:correspondence`** (definitions and examples; P). A *correspondence* $\mathcal C$ from $X$ to $Y$ (smooth projective
curves over $k$, or compact Riemann surfaces) is a triple $(C,\alpha,\beta)$ with $C$ a finite disjoint union of smooth projective
curves and $\alpha\colon C\to X$, $\beta\colon C\to Y$ morphisms nonconstant on every component; its *transpose* is $\mathcal C^t=(C,\beta,\alpha)$, from $Y$ to $X$;
sums are disjoint unions. Examples: (a) the graph $\Gamma_\varphi=(X,\mathrm{id},\varphi)$ of a nonconstant $\varphi\colon X\to Y$, and its transpose
$\Gamma_\varphi^t=(X,\varphi,\mathrm{id})$; (b) an automorphism $w$ of $X$ gives $\Gamma_w$, with $\Gamma_w^t$ acting as $\Gamma_{w^{-1}}$ (12.2); (c) (forward
pointer, Chapter 14) the Hecke correspondence $T_p=(X_0(Np),\pi_1,\pi_p)$ on $X_0(N)$ for a prime $p\nmid N$, with $\pi_1(z)=z$, $\pi_p(z)=pz$ on
$\mathbb H$, and $U_p$ similarly for $p\mid N$. Remark (R): the image of $(\alpha,\beta)$ is a divisor on $X\times Y$; correspondences up to the
obvious equivalence form a ring under composition (fibre products); this chapter does not need the composition, only the
actions below, because the Hecke algebra is defined as the ring of operators they generate (Chapter 13). Reference: Shimura71,
Chapter 7 (cite the chapter); DiamondShurman, Section 6.3 (cite the section); Milne, Abelian varieties (correspondences);
Fulton, Intersection theory (not in refs.bib). Paper: Section 4.1 (the Hecke operators $T_n$, $U_p$ and $w_{M^\Sigma}$ acting on
$H^1(X_0(M^\Sigma),\Z_\ell)$), Lemma lem:hecke, Theorem thm:quant Steps 1 and 2.

**12.2 `def:curves:correspondence-actions`** (definitions and proposition; P for the definitions and (a), (d); S for (b), (c)).
Let $\mathcal C=(C,\alpha,\beta)$ be a correspondence from $X$ to $Y$. (i) On divisors: $\mathcal C_*=\beta_*\alpha^*\colon\operatorname{Div}(X)\to\operatorname{Div}(Y)$; it multiplies degrees by
$\deg\alpha$, maps principal divisors to principal divisors (6.4(iii)), hence induces $\mathcal C_*\colon J(X)\to J(Y)$. (ii) On homology: the transfer
$\alpha^!\colon H_1(X,\Z)\to H_1(C,\Z)$ (a loop avoiding the branch points of $\alpha$ is replaced by the sum of its $\deg\alpha$ lifts; well defined, S) and
$\mathcal C_*=\beta_*\alpha^!\colon H_1(X,\Z)\to H_1(Y,\Z)$. (iii) On cohomology: $\alpha_*\colon H^1(C,\Z)\to H^1(X,\Z)$ is the transpose of $\alpha^!$ (on de Rham
classes, the trace: $(\alpha_*\eta)(x)=\sum_{c\in\alpha^{-1}(x)}\eta_c$ away from branch points; S), and $\mathcal C^*=\alpha_*\beta^*\colon H^1(Y,\Z)\to H^1(X,\Z)$. (iv) On
holomorphic differentials: $\mathcal C^*\omega=\alpha_*\beta^*\omega$ (the trace of a holomorphic form extends holomorphically over the branch points:
P by Riemann's removable singularity theorem). Compatibilities: (a) $\langle\mathcal C^*\xi,\gamma\rangle=\langle\xi,\mathcal C_*\gamma\rangle$ for $\xi\in H^1(Y)$, $\gamma\in H_1(X)$
(the evaluation pairing): **$\mathcal C^*$ on $H^1$ is the transpose of $\mathcal C_*$ on $H_1$** (P from the definitions). (b) Under Abel-Jacobi (11.2),
$\mathcal C_*$ on $J(X)$ is induced by the transpose of $\mathcal C^*$ on holomorphic differentials and by $\mathcal C_*$ on $H_1$ (S, from 11.4(ii), (iii));
hence on $T_\ell J(X)\simeq H_1(X,\Z_\ell)$ (11.7(i)) a correspondence acts by $\mathcal C_*$, and on $H^1(X,\Z_\ell)=\Hom(T_\ell J,\Z_\ell)$ by the transpose. (c)
For a graph: $\Gamma_\varphi^*=\varphi^*$ on $H^1$ and on differentials, $(\Gamma_\varphi)_*=\varphi_*$ on $H_1$ and on $J$ (Albanese), $(\Gamma^t_\varphi)_*=\varphi^*$ on $J$
(Picard) and $(\Gamma^t_\varphi)^*=\varphi_*$ on $H^1$. (d) Linearity in $\mathcal C$, and functoriality for composition with graphs:
$(\Gamma_u\circ\mathcal C\circ\Gamma_v)$ acts as $u_*\mathcal C_*v_*$ on $H_1$ for automorphisms $u$, $v$ (P). Reference: as in 12.1; Milne, Abelian varieties
(cite the section on correspondences). Paper: Section 4.1, Remark rem:free (the Hecke action on $J_0(N)$ and on $T_\ell J_0(N)$
versus on $H^1(X_0(N),\Z_\ell)$), Lemma lem:hecke, Chapter 14.

**12.3 `thm:curves:adjoint-transpose`** (theorem; P over $\R$ by de Rham, given the trace description of $\alpha_*$ in 12.2(iii) (S); hence over $\Z$ and $\Z_\ell$). Let $\mathcal C=(C,\alpha,\beta)$ be a
correspondence from $X$ to $Y$. For all $\xi\in H^1(Y,\Z)$ and $\eta\in H^1(X,\Z)$:
$$\langle\mathcal C^*\xi,\eta\rangle_X=\langle\xi,(\mathcal C^t)^*\eta\rangle_Y,$$
that is, **the adjoint of a correspondence for the cup product is its transpose**: $(\mathcal C^*)^\dagger=(\mathcal C^t)^*$. Proof: both sides equal
$\int_C\beta^*\xi\wedge\alpha^*\eta$, because $\int_X(\alpha_*\theta)\wedge\eta=\int_C\theta\wedge\alpha^*\eta$ for every closed $1$-form $\theta$ on $C$ (on the complement of the
finitely many branch points $\alpha$ is a $\deg\alpha$-sheeted covering, and on each sheet this is the change of variables formula; the
branch points have measure zero), and likewise for $\beta$ with the order of the factors kept. Both sides are integers on integral
classes, so the identity holds in $H^1(\cdot,\Z)$ and after $\otimes\Z_\ell$. Corollaries (P): (a) for an automorphism $w$ of $X$,
$\langle w^*x,w^*y\rangle=\langle x,y\rangle$ (take $\mathcal C=\Gamma_w$; $(\Gamma_w^t)^*=(w^{-1})^*$), so $w^*$ is an isometry; (b) $\langle\varphi^*\xi,\eta\rangle_X=\langle\xi,\varphi_*\eta\rangle_Y$ for a
morphism $\varphi$, and 11.5(i), (ii) again; (c) $\operatorname{PD}\circ\mathcal C^*=(\mathcal C^t)_*\circ\operatorname{PD}$: under Poincare duality the action $\mathcal C^*$ on $H^1$
corresponds to the action of the transpose on $H_1$, hence on $T_\ell J$ (11.7(iii)); (d) the same with $\Z_\ell$, $\Q_\ell$ or $\C$
coefficients. (e) (Abstract self-adjointness lemma.) Let $\mathbb T$ be a commutative ring of endomorphisms of $H^1(X,\Z_\ell)$, each of
the form $\sum c_i\mathcal C_i^*$ with $c_i\in\Z_\ell$, and $w$ an involutive automorphism of $X$ such that for every $t=\sum c_i\mathcal C_i^*\in\mathbb T$ the
transposed operator $t^t=\sum c_i(\mathcal C_i^t)^*$ equals $w^*tw^*$. Put $[x,y]=\langle x,w^*y\rangle$. Then $[\ ,\ ]$ is perfect and alternating on
$H^1(X,\Z_\ell)$ and every $t\in\mathbb T$ is self-adjoint for it: $[tx,y]=\langle x,t^tw^*y\rangle=\langle x,w^*ty\rangle=[x,ty]$; antisymmetric because
$[y,x]=\langle y,w^*x\rangle=\langle w^*y,x\rangle=-[x,y]$ ((a) and $w^{*2}=1$), hence alternating since $H^1(X,\Z_\ell)$ is torsion-free (Chapter 3,
9.4); perfect because $w^*$ is an automorphism (Chapter 3, 9.5(iv)). Consequently every idempotent of $\mathbb T$ is self-adjoint, $H^1(X,\Z_\ell)=\bigoplus_{\mathfrak m}H^1(X,\Z_\ell)_{\mathfrak m}$ is an orthogonal decomposition, and $[\ ,\ ]$ is perfect on each summand
(Chapter 3, 9.5(iii)): this is the sentence important_notes.md point 36 asks for. Reference: Shimura71, Chapter 7 (cite the
chapter); DDT, Section 4.4 (cite the section); DFG04, Sections 1.6.1 and 1.8.2 (as the paper cites them). Paper: Section 4.1
("the Hecke operators, $U_p$ included, are self-adjoint for it, because $w_{M^\Sigma}T_nw_{M^\Sigma}^{-1}$ is the adjoint of $T_n$ for the cup product
(this is what the composition with $w$ is for)"; "perfect and alternating"), Lemma lem:hecke and Theorem thm:quant Step 2
(Lemma lem:ddt417 applied to $L=H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ "with a perfect $\mathcal O$-bilinear pairing for which $\T$ is self-adjoint"),
important_notes.md point 36. The input "$T_n^t=w_NT_nw_N$ for all $n$, including $U_p$" on $X_0(N)$ is Chapter 14's.

**12.4 `ex:curves:correspondence-examples`** (examples; P). (a) On $X=\C/\Lambda$, the automorphism $[-1]$ acts by $-1$ on $H^1$; it is an isometry
($\langle-x,-y\rangle=\langle x,y\rangle$). (b) For $\varphi\colon X\to E$ of degree $d$, the correspondence $\Gamma_\varphi^t\circ\Gamma_\varphi$ on $E$ (that is, $\varphi_*\varphi^*$) acts on
$H^1(E)$ and on $E=J(E)$ by $d$ (11.4(iv), 11.5(ii)); $\Gamma_\varphi\circ\Gamma_\varphi^t$ on $X$ acts on $H^1(X)$ by $\varphi^*\varphi_*$, whose image is $\varphi^*H^1(E)$, and on
$\varphi^*H^1(E)$ by $d$: so $\varphi^*\varphi_*/d$ is the orthogonal projector onto $\varphi^*H^1(E,\Q)$ for the cup product (P by 12.3(b)), integral at $\ell\nmid d$. (c) On
a genus-one curve $E$, for a nonconstant morphism $\psi\colon E\to E$ fixing $O$ (an endomorphism, Chapter 9) the adjoint of $\psi^*$ on $H^1(E,\Z)$ is
$\psi_*=(\deg\psi)(\psi^*)^{-1}$ (12.3(b) and 11.5(ii)); for $\psi=[m]$, $\psi^*=\psi_*=m$ is self-adjoint, but for $E=\C/\Z[i]$ and $\psi(z)=iz$, $\psi^*$ is a
rotation of order $4$ and its adjoint is the inverse rotation: a correspondence need not be self-adjoint for the cup product
(Exercise 13). (d)
(Forward pointer, Chapter 14.) For $p\nmid N$, $T_p^t=w_NT_pw_N$ on $X_0(N)$ (in fact $=T_p$ on $\Gamma_0(N)$ as double cosets), while for $p\mid N$,
$U_p^t=w_NU_pw_N\ne U_p$ in general: this is why the paper composes the cup product with $w$. Paper: Section 4.1, Lemma lem:hecke.

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2, stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1 ($\varphi_E$, $\deg\varphi_E$, optimal curve); Section 4.1 ($H^1(X_0(M^\Sigma),\Z_\ell)$, cup product, $\hat\delta_!$, adjoints); Lemma lem:hecke; Lemma lem:ddt417 as applied; Theorem thm:quant Steps 1, 2, 4; Remark rem:free ($J_0(N)[\mathfrak m]$, Tate module, freeness); Section 4.2 ($M_{f,\lambda}$ versus $T_\ell E$, point 26); Section 1.1 and Proposition prop:ns (Galois action on points) | 40 |
| 1 | Affine and projective varieties | a one-page roadmap ("two languages, one dictionary", what is proved, sketched, stated) as the opening paragraph; conventions C1 to C8 as `convention` environments; 1.1 to 1.3 | 150 |
| 2 | Plane curves and smoothness | 2.1 to 2.4; the pictures of the node and the cusp described in words; the Weierstrass models of 11a1, 20a1, 121a1 as smooth examples | 140 |
| 3 | Function fields, points over extensions, the Galois action | 3.1 to 3.4; `paperlink`: $\rho_{E,\ell}$ is the Galois action on points (Section 1.1), the action on $E[3]$ in Proposition prop:ns; `warning`: a genus-zero curve need not have a rational point | 140 |
| 4 | Divisors, differentials, the Picard group | 4.1 to 4.3; the examples on $\mathbb P^1$ and on $y^2=h(x)$ | 150 |
| 5 | Riemann-Roch and its consequences | 5.1 to 5.7; the shape of the proof of Riemann-Roch in one paragraph; the Weierstrass derivation written out; `paperlink`: the curves of the paper as Weierstrass equations | 210 |
| 6 | Morphisms and degree; separability; Frobenius | 6.1 to 6.5; a table "degree in three (four) ways"; `paperlink`: the modular degree is $\deg\varphi_E$ in every sense | 170 |
| 7 | Ramification and Riemann-Hurwitz | 7.1 to 7.3; the worked examples (hyperelliptic, Fermat, $X_0(121)\to$ 121a1, $X_0(539)\to$ 539c1) | 120 |
| 8 | Compact Riemann surfaces and complex curves | 8.1 to 8.4; the dictionary table (algebraic versus analytic: function field, $\operatorname{ord}_P$, $e_\varphi(P)$, $\deg$, differentials, genus) | 150 |
| 9 | Holomorphic differentials, residues, periods | 9.1 to 9.4; physics asides (charge, norm, area) | 130 |
| 10 | $H_1$, $H^1$ and the cup product | 10.1 to 10.4; the torus computation in full; a `convention` box on signs (C6) and on "which is dual to which"; `paperlink`: Section 4.1, "perfect and alternating" | 170 |
| 11 | The Jacobian, torsion and Tate modules | 11.1 to 11.8; `paperlink`s: Remark rem:free, Section 4.2 (dual of $T_\ell E$, point 26), Lemma lem:hecke (11.5(iv)); `warning`: $H^1(X,\Z_\ell)\simeq T_\ell J$ is not Galois-equivariant | 240 |
| 12 | Correspondences and adjoints | 12.1 to 12.4; `paperlink`: Section 4.1 ($\hat\delta_!$, self-adjointness of $T_n$ and $U_p$), Lemma lem:hecke and important_notes.md point 36 (12.3(e)) | 170 |
| 13 | Exercises | the 18 exercises of Part 4.2 | 130 |
| 14 | Notes and references | SilvermanAEC I to III, Hartshorne I, II, IV and Appendix B, Fulton, Miranda, Forster, Griffiths-Harris, Farkas-Kra, Milne (Jacobian varieties, Abelian varieties, Etale cohomology), Mumford, Shimura71, DiamondShurman; which section numbers were cited | 40 |
| | **total** | | **2,150** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map row and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| affine and projective space | 1.1, 1.2 |
| varieties over a field | 1.1, 1.2, 1.3 |
| the projective plane and homogeneous polynomials | 1.2, 2.1 |
| smoothness and singular points | 2.1, 2.2, 2.4 |
| plane curves | 2.1, 2.3, 5.4, 5.5 |
| the function field of a curve | 1.1(iii), 1.2(iv), 3.1, 3.3 |
| points over extensions and the Galois action on points | 1.2(i), 3.4, 6.5(c) |
| the genus via Riemann-Roch; $(d-1)(d-2)/2$ for smooth plane curves | 5.2, 5.3(a), 5.4, 5.5, 7.3(d) |
| divisors, principal divisors, linear equivalence | 4.1, 4.2 |
| the Picard group | 4.2, 5.7, 11.1 |
| Riemann-Roch (statement) with standard consequences | 5.1, 5.2, 5.3 |
| a genus-one curve with a rational point is a plane cubic | 5.6 (and 5.7) |
| morphisms of curves | 1.3, 3.2, 3.3, 6.1 |
| degree: field degree, number of preimages of a general point, pullback on divisors | 6.2, 6.3, 6.4 (and 8.2(c), 11.5(i) for the analytic and cohomological forms) |
| separable and inseparable morphisms | 6.2, 6.5 |
| ramification of morphisms | 6.2, 7.1, 8.2(a) |
| the Riemann-Hurwitz formula | 7.2, 7.3, 8.4(c) |
| compact Riemann surfaces versus smooth projective curves over $\C$ (equivalence) | 8.1, 8.2, 8.3, 8.4 |
| differentials, holomorphic differentials and the genus | 4.3, 5.3(a), 9.1, 9.3 |
| the Jacobian as $\operatorname{Pic}^0$, as a complex torus, as an abelian variety (statements) | 11.1, 11.2, 11.3 |
| the Abel-Jacobi map | 11.2 |
| $H^1(X,\Z)$ of rank $2g$; intersection pairing and cup product | 10.1, 10.2, 10.3, 10.4 |
| $H^1(X,\Z_\ell)=H^1(X,\Z)\otimes\Z_\ell$; remark on etale cohomology | 10.2(i), 10.3, 11.8(b), (c) |
| the Tate module of the Jacobian is dual to $H^1$ | 11.6, 11.7, 11.8 |
| the cup product is perfect and alternating on $H^1(X,\Z)$ | 10.3 |
| correspondences and their action on $H^1$ and on the Jacobian | 12.1, 12.2, 12.4 |
| the adjoint of a correspondence under the cup product is the transpose | 12.3 |
| Section 6 row: $H^1(X_0(N),\Z_\ell)$, cup product, Atkin-Lehner, Hecke self-adjointness (with Chapter 14) | 10.3, 12.3, 12.3(e), 12.4(d) |
| hook: the modular parametrisation $X_0(N)\to E$ and its degree (Section 1) | 6.2, 6.4, 7.3(e), 8.3, 11.4, 11.5 |
| hook: $H^1(X_0(N),\Z_\ell)$ with the cup product (Section 4.1, Lemma lem:hecke) | 10.2, 10.3, 11.5(iv), 12.2, 12.3 |
| hook: $J_0(N)$ and its torsion (Remark rem:free) | 11.1 to 11.3, 11.6, 11.7 |
| hook: Tate modules of Jacobians | 11.7, 11.8 |
| also: Theorem thm:quant Step 2 (same pairing at level $N$ for $g^S$) | 10.3, 12.3(e) |
| also: Section 4.2 ($M_{f,\lambda}$ versus $T_\ell E$; important_notes.md point 26) | 11.5(iv), 11.7(ii), 11.8(c) |
| also: important_notes.md point 36 (orthogonality of the $\mathfrak m$-decomposition) | 12.3(e) |
| also: Section 1.1, Proposition prop:ns (Galois action on points, $E[3]$) | 3.4 |
| also: Section 1 (Petersson norm, area of $\Lambda_E$ in the Zagier-Watkins formula: background) | 9.4, 10.4 |
| also: what Chapters 9, 10, 12, 14, 15 assume from Chapter 8 (Part 5) | 2.1, 3.4, 4.3, 5.6, 5.7, 6.4, 6.5, 7.3(b), (f), 8.1, 8.3, 9.1, 9.3, 11.2 to 11.8, 12.1 to 12.3 |

### 4.2 Exercises (Section 13 of the chapter), graded from easy to harder

1. Find the singular points of $y^2=x^3+x^2$ and $y^2=x^3$ (projective closures included); parametrise the node by $t=y/x$ and show
   that the cusp is the image of $t\mapsto(t^2,t^3)$. Show that $X^d+Y^d+Z^d=0$ is smooth iff $\operatorname{char}k\nmid d$.
2. Check the paper's curves are smooth: for 11a1 ($y^2+y=x^3-x^2-10x-20$) and 121a1 ($y^2+xy+y=x^3+x^2-30x-76$) show that the
   three partial derivatives of the homogenised equation have no common zero on the curve over $\bar\Q$ (compute $F_Z$ at $[0:1:0]$;
   on the affine part eliminate $y$). Which primes make the reduction singular? (Answer for 11a1: only $11$; compare with Chapter 9's
   $\Delta=-11^5$.)
3. On $\mathbb P^1$ show $\operatorname{div}(dx)=-2(\infty)$, $\operatorname{Pic}^0(\mathbb P^1)=0$, and $\ell(n(\infty))=n+1$; check Riemann-Roch with $g=0$.
4. On the smooth cubic $y^2=h(x)$ ($h$ squarefree of degree $3$, $\operatorname{char}k\ne2$) compute $\operatorname{ord}_\infty x=-2$, $\operatorname{ord}_\infty y=-3$, and show
   $\operatorname{div}(dx/y)=0$. Deduce $g=1$ from 5.3(b).
5. Let $C$ have genus $1$ and $O\in C(k)$. Show $\ell(n(O))=n$ for $n\ge1$, find bases of $\mathcal L(n(O))$ for $n\le6$ in terms of $x$, $y$, and
   derive the Weierstrass equation (5.6(ii)). Why does the argument fail for the conic $X^2+Y^2+Z^2=0$ over $\Q$, and for Selmer's cubic?
6. Prove 5.7: for genus one, $P\mapsto[(P)-(O)]$ is a bijection $C(\bar k)\to\operatorname{Pic}^0(C)$. Check $G_k$-equivariance.
7. For the Weierstrass cubic, show that $x\colon C\to\mathbb P^1$ has degree $2$ and is ramified exactly at $O$ and at the three points with
   $2y+a_1x+a_3=0$; verify Riemann-Hurwitz. Do the same for $y$ (degree $3$).
8. Compute the genus of the Fermat curve of degree $d$ in two ways (5.4 and 7.3(d)), and of $y^2=x^5-x$ (answer $2$).
9. Show that a nonconstant morphism between curves of genus one in characteristic $0$ is unramified and that $\#\varphi^{-1}(Q)=\deg\varphi$ for
   every $Q$. Where does the argument use characteristic $0$? (Frobenius, 6.5(c), is a counterexample to $\#\varphi^{-1}(Q)=\deg\varphi$.)
10. Check the paper's degrees against Riemann-Hurwitz: given $g(X_0(121))=6$, $g(X_0(539))=49$ (Chapter 12) and
    $\deg\varphi_{121a1}=6$, $\deg\varphi_{539c1}=288$ (the paper, Section 3 Example), compute the total ramification of the two
    parametrisations. Given $g(X_0(11))=1$ and $\deg\varphi_{11a1}=1$, conclude $X_0(11)\simeq$ 11a1.
11. (The torus.) For $X=\C/(\Z+\tau\Z)$ compute the cup product on $H^1(X,\Z)$ in the basis $ds$, $dt$; show it is perfect and alternating;
    compute $\operatorname{PD}$ and check $\langle\alpha,\beta\rangle=\operatorname{PD}(\alpha)\cdot\operatorname{PD}(\beta)$; compute $\frac i2\int dz\wedge d\bar z=\operatorname{Im}\tau$ and check 9.4(d).
12. Show $J(X)[n]\simeq H_1(X,\Z/n)$ and $T_\ell J\simeq H_1(X,\Z)\otimes\Z_\ell$ for a compact Riemann surface; deduce
    $H^1(X,\Z_\ell)\simeq\Hom_{\Z_\ell}(T_\ell J,\Z_\ell)$. Using the Weil pairing of an elliptic curve (Chapter 9), deduce $H^1(E,\Z_\ell)\simeq T_\ell E(-1)$ as
    Galois modules and compare determinants ($\chi_\ell^{-1}$ versus $\chi_\ell$). Explain why the paper's "$M_{f,\lambda}$ and $T_\ell E$ are
    homothetic" should read "homothetic to the dual of $T_\ell E$" (important_notes.md point 26), and why the adjoints agree anyway.
13. Show that an automorphism $w$ of $X$ acts on $H^1(X,\Z)$ as an isometry of the cup product. For $E=\C/\Z[i]$ and $\psi(z)=iz$, write the
    matrix of $\psi^*$ in the basis of Exercise 11 and of its adjoint; conclude that the adjoint of a correspondence is its transpose
    and not the correspondence itself.
14. (Check the paper's claim in Section 4.1, abstractly.) Let $\langle\ ,\ \rangle$ be a perfect alternating pairing on a free $\Z_\ell$-module $L$, $w$
    an isometric involution of $L$, and $\mathbb T$ a commutative ring of endomorphisms with $t^\dagger=wtw$ for all $t\in\mathbb T$. Show that
    $[x,y]=\langle x,wy\rangle$ is perfect and alternating and that every $t\in\mathbb T$ is self-adjoint for it; deduce that the idempotents of
    $\mathbb T$ split $L$ orthogonally (important_notes.md point 36).
15. (Pullback and degree.) For $\varphi\colon X\to Y$ of degree $d$ prove $\langle\varphi^*x,\varphi^*y\rangle=d\langle x,y\rangle$ and $\varphi_*\varphi^*=d$. For $Y=E$ of genus one,
    show that the cup product on $\varphi^*H^1(E,\Z)$ has Gram determinant $d^2$ and that, if $\varphi^*H^1(E,\Z)$ is saturated,
    $[H^1(X,\Z):\varphi^*H^1(E,\Z)\oplus(\varphi^*H^1(E,\Z))^\perp]=d^2$ (with Chapter 3, 9.3).
16. (Optimality.) Let $\pi\colon V/\Lambda\to W/M$ be a surjective homomorphism of complex tori. Show that the component group of its
    kernel is $M/\pi(\Lambda)$. For an isogeny $\psi\colon E\to E'$ of degree $n$ and $\varphi\colon X\to E$, show that $(\psi\circ\varphi)^*H^1(E',\Z)$ has index $n$ in
    $\varphi^*H^1(E,\Z)$; deduce that if $\varphi^*H^1(E,\Z)$ is saturated then $(\psi\circ\varphi)^*H^1(E',\Z)$ is not (for $n>1$), and relate this to "minimal
    degree" in the paper's definition of the optimal curve (Section 1; Chapter 14 shows that every parametrisation of a curve
    isogenous to $E$ factors through the optimal one).
17. (Frobenius.) For $C$ over $\F_p$, show that $\phi_p$ is a morphism with $\phi_p^*\bar\F_p(C)=\bar\F_p(C)^p$, that $d(\phi_p^*f)=0$, that its fixed points are
    $C(\F_p)$, and that $e_{\phi_p}(P)=p$ everywhere. Explain why Riemann-Hurwitz does not apply to $\phi_p$.
18. (Residues.) Prove $\sum_P\operatorname{res}_P\omega=0$ on a compact Riemann surface and deduce $\deg\operatorname{div}f=0$. On $\mathbb P^1$ verify it for
    $\omega=dz/(z^2-1)$.

## 5. Dependencies and forward pointers

Results from other chapters used here:
* Background (PLAN.md Section 2): complex analysis (holomorphic functions, zeros of finite order and local $e$-th roots, the
  open mapping theorem, Laurent series and residues, Riemann's removable singularity theorem, Moebius maps), real analysis
  (implicit function theorem, change of variables in double integrals, Stokes/Green's theorem in the plane, used on surfaces
  via partitions of unity), linear algebra (dual bases, Gram matrices, real versus complex dimensions). Elementary point-set
  topology (compactness, connectedness, quotient topology) as in Chapter 1's profinite section.
* Chapter 1 (`ch:groups`): $\mathbb P^1(F)$ as lines and the Moebius action (its C1); $\Z_\ell$ as an inverse limit (its 7.2), used for $T_\ell J$.
* Chapter 2 (`ch:rings`): polynomial rings, irreducibility, UFDs (its 3.2, 4.3: $k[x,y]$ is a UFD, used for plane curves), the
  freshman's dream in characteristic $p$ (its 1.6, for the Frobenius morphism), finite fields (its 6.1 to 6.3).
* Chapter 3 (`ch:modules`): Nakayama (its 4.3) and the DVR criterion (its 6.1) for 2.2; localisation (its 4.5); finitely
  generated modules over a PID and saturation (its 5.3, 5.5) for 11.5(iii); perfect pairings, base change, Gram determinants,
  saturated sublattices (its 9.1, 9.3), alternating pairings (its 9.4), adjoints, twisted pairings and orthogonal idempotent
  decompositions (its 9.5) for 10.3, 11.5(iv), 12.3(e). Chapter 8 must use, not redo, these.
* Chapter 5 (`ch:galois`): algebraic and transcendental elements, separability, separable and inseparable degree (its
  galois:separability), perfect fields, $G_k$ and its Krull topology (its galois:absolute-galois-group), the cyclotomic character and
  $\Z_\ell(1)$ (its galois:cyclotomic-character), Hilbert 90 in field form (its Section 5).
* Chapter 6 (`ch:ant`): Dedekind domains and $\sum e_if_i=n$ (its 2.1, 3.1), whose proof 6.3 transports to curves; the Frobenius
  conventions (its 3.7).
* Chapter 4 (`ch:reps`): contragredient (its C2) for 11.8(b).

Black boxes imported from later chapters (stated with a forward `\Cref`, used only in examples, exercises and `paperlink`s,
never in a proof of a numbered result): the genus formula of $X_0(N)$ and $S_2(\Gamma_0(N))\simeq H^0(X_0(N),\Omega^1)$ (Chapter 12; used in 5.5(f),
7.3(e), 9.3, Exercise 10); the modular degrees of 11a1, 121a1, 539c1 (the paper; Chapter 14); the Hecke correspondences on
$X_0(N)$ and $T_n^t=w_NT_nw_N$ (Chapter 14; used in 12.1(c), 12.4(d)); the Weil pairing of an elliptic curve and $\Delta$ (Chapter 9;
Exercises 2, 12); Hilbert 90 in cohomological form (Chapter 17; used in 4.2(iii), stated); group cohomology and its cup product
(Chapter 16; 10.2(iv), a remark).

Forward pointers (chapters that use this one):
* Chapter 9 (`ch:ellcurves`): curves, points over extensions and the Galois action (3.4), smoothness of plane cubics (2.1),
  regular differentials and $\operatorname{div}(dx/y)=0$ (4.3), Riemann-Roch consequences: the Weierstrass equation (5.6) and the bijection
  $E\to\operatorname{Pic}^0(E)$ (5.7) for the group law and its associativity, the degree of a morphism and $\varphi_*\varphi^*=\deg$ (6.4) for isogenies and
  the dual isogeny, separability and the Frobenius morphism (6.5), "isogenies are unramified" (7.3(b)), complex tori $\C/\Lambda$
  (8.1(c), 10.4, 11.2 for $g=1$), $J[n]$ and $T_\ell J$ for $g=1$ (11.6, 11.7), the general Weil pairing (11.8(a)) and the point count
  $a_q=\operatorname{tr}\Frob$ (11.8(d)) as the $g=1$ cases. Chapter 9 does not redo Riemann-Roch.
* Chapter 10 (`ch:reduction`): smoothness and singular points of reductions mod $p$ (2.1, 2.2), function fields (3.1).
* Chapter 12 (`ch:modforms`): Riemann surfaces and charts (8.1), holomorphic maps and degree (8.2), Riemann-Hurwitz (7.2, 8.4(c))
  for the genus formula of $X_0(N)$, holomorphic differentials and $\dim H^0(\Omega^1)=g$ (9.1, 9.3) for $\dim S_2(\Gamma_0(N))=g$, the positivity
  9.4(b) behind the Petersson product.
* Chapter 13 (`ch:hecke`): the Hecke algebra as operators generated by correspondences (12.1, 12.2).
* Chapter 14 (`ch:moddeg`): everything in Sections 10 to 12: the Jacobian $J_0(N)$ (11.1 to 11.3), its torsion and Tate module (11.6, 11.7,
  11.8), the Hecke correspondences and their actions (12.1, 12.2), the adjoint theorem and the pairing $\langle x,w_Ny\rangle$ (12.3, 12.3(e)),
  the modular parametrisation and its degree (6.4, 11.4, 11.5), the cup product on $H^1(X_0(N),\Z_\ell)$ (10.3), the identification of
  $M_{f,\lambda}$ with $\varphi_E^*H^1(E,\Z_\ell)$ for optimal $E$ (11.5(iii), (iv); Part 7, points 1 and 2), Eichler-Shimura (with 6.5(c), 11.8(d)).
* Chapter 15 (`ch:modgalrep`): Tate modules of abelian varieties and $H^1$ (11.7, 11.8) for $\rho_{f,\lambda}$; "homothetic to the dual"
  (point 26).
* Chapter 18 (`ch:blochkato`): $H^1_{\mathrm{et}}$ and Tate twists $T_\ell J(-1)$ (11.8(c)).
* Chapter 20 (`ch:congruence`): $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ with a perfect alternating pairing for which $\T$ is self-adjoint (10.3,
  12.3(e)) as the module $L$ of Lemma lem:ddt417; 11.5(iv) (Part 7, point 1).
* Chapters 21, 22 (`ch:paper`, `ch:computation`): Section 4.1 and Remark rem:free hooks; `ellmoddegree` computes $\deg\varphi_E$ of 6.2.

## 6. Notes for the writer

### 6.1 Conventions to state (Section 1 of the chapter, as `convention` environments)

C1 to C8 of Part 1.2. In addition, one `convention` box in Section 10, "Homology, cohomology, Tate module: which is dual to
which", with exactly these lines:
* covariant objects: $H_1(X,\Z)$, the lattice $\Lambda_X$, $J(X)=H^0(X,\Omega^1)^\vee/\Lambda_X$, $J[n]=H_1(X,\Z/n)$, $T_\ell J=H_1(X,\Z_\ell)$; a morphism $\varphi$ acts by
  $\varphi_*$ and a correspondence $\mathcal C$ by $\mathcal C_*=\beta_*\alpha^!$;
* contravariant objects: $H^1(X,\Z)=\Hom(H_1,\Z)$, $H^1(X,\Z_\ell)=\Hom(T_\ell J,\Z_\ell)$, $H^0(X,\Omega^1)$; $\varphi$ acts by $\varphi^*$, $\mathcal C$ by $\mathcal C^*=\alpha_*\beta^*$;
  $\mathcal C^*$ is the transpose of $\mathcal C_*$ (12.2(a));
* the two sides are identified by Poincare duality (10.3), which is an isometry for the cup product and the intersection
  pairing and turns $\mathcal C^*$ into $(\mathcal C^t)_*$ (12.3(c)); it is canonical up to the global orientation sign;
* with Galois action (11.8): $H^1_{\mathrm{et}}=(T_\ell J)^\vee\simeq T_\ell J(-1)$; for an elliptic curve, $V_\ell E$ (the paper's $V$) has determinant $\chi_\ell$
  and $H^1(E,\Q_\ell)=V^\vee\simeq V(-1)$ has determinant $\chi_\ell^{-1}$; $\ad V$ is the same for $V$, $V^\vee$, $V(n)$ (Chapter 4);
* Frobenius (C7): the arithmetic Frobenius on $T_\ell J$ and the geometric Frobenius on $H^1$ have the same characteristic
  polynomial $P(T)$, with $\#C(\F_q)=q+1-\operatorname{tr}$.

### 6.2 Pitfalls

* **Never define $H^1$ by sheaf cohomology** and never use sheaf cohomology in a proof: $H^1(X,\Z):=\Hom(H_1(X,\Z),\Z)$, with de Rham forms
  for computing cup products. The one place sheaves appear is the remark "$\ell(K-D)=\dim H^1(X,\mathcal O(D))$" in the sketch of 5.2,
  flagged as such.
* **Sign of the cup product.** State C6 once, check it on the torus (10.4), and say that the paper needs only properties
  invariant under a global sign: perfectness, alternation, the adjointness 12.3, ideals of values, Gram determinants (in even
  rank $\det(-G)=\det G$). Do not try to reconcile with every textbook's convention.
* **Adjoint versus transpose versus inverse.** The cup-product adjoint of $\mathcal C^*$ is $(\mathcal C^t)^*$ (12.3); for an automorphism the
  transpose acts as the inverse (12.3(a)); a correspondence is self-adjoint only if it equals its transpose (as an operator).
  On $X_0(N)$, $T_p$ ($p\nmid N$) is its own transpose but $U_p$ ($p\mid N$) is not, and this is why the paper composes with $w$
  (12.4(d), Chapter 14). The adjoint is written $A^\dagger$ (C4), never $A^*$.
* **Degrees.** $\varphi_*\varphi^*=[\deg\varphi]$ on $E$, and the endomorphism $[\deg\varphi]$ of $E$ has degree $(\deg\varphi)^2$ (10.4): never write
  "$\deg(\varphi_*\varphi^*)=\deg\varphi$". The cup product on $\varphi^*H^1(E)$ is $\deg\varphi$ times that of $E$, so the Gram determinant is $(\deg\varphi)^2$
  (11.5(iv)): rank-two alternating pairings have square Gram determinants (Chapter 3, 9.4(ii)).
* **Separability.** "Number of preimages $=\deg$" holds only for separable maps and away from branch points (6.4(ii)); in
  characteristic $p$ the Frobenius is a bijection on points of degree $p$. The paper works over $\Q$ and $\C$, but Chapters 9, 10 and
  14 reduce mod $p$.
* **Rational points.** A genus-zero curve over $\Q$ need not be $\mathbb P^1$ over $\Q$ (3.4(iv)); a genus-one curve need not have a
  rational point (Selmer's cubic). 5.6 and 5.7 assume $O\in C(k)$.
* **Optimality and saturation** (11.5(iii)): saturation of $\varphi^*H^1(E,\Z)$ is equivalent to connectedness of $\ker(J(X)\to E)$, which is
  Chapter 14's definition of an optimal quotient; over $\Z_\ell$ only the $\ell$-part of the component group matters (important_notes.md
  point 27: when $E[\ell]$ is irreducible all curves of the class give the same $v_\ell$).
* **Jacobians over non-closed fields.** $J(k)=\operatorname{Pic}^0_k(C)$ needs $C(k)\ne\emptyset$ (4.2(iii), 11.3(i)); $X_0(N)$ has the rational cusp $\infty$,
  so this is harmless in the paper.
* **Do not prove Riemann-Roch, Abel-Jacobi, Riemann existence or Poincare duality.** State them precisely with references
  and give the shape of the proof in a paragraph (5.2, 11.2(iii), 8.3, 10.3). Never present a sketch as a proof (PLAN.md 7.2).
* Physics asides: at most one sentence each, at the places listed in Part 1.1.
* Typography (PLAN.md 7.2): no dash ligatures anywhere ("Riemann-Roch", "Riemann-Hurwitz", "Abel-Jacobi", "Eichler-Shimura",
  "Griffiths-Harris" with plain hyphens; ranges as "1 to 8"); ASCII source; the dictionary table of Section 8 and the degree
  table of Section 6 with `booktabs`.

### 6.3 What to leave to Chapters 9, 12, 14 (and others)

* **Chapter 9** (`ch:ellcurves`): Weierstrass invariants $b_i$, $c_4$, $c_6$, $\Delta$, $j$, the criterion $\Delta\ne0$, changes of
  coordinates; the chord-tangent group law (Chapter 8 gives only 5.7, from which associativity follows); isogenies, the dual
  isogeny, $\deg[m]=m^2$ for elliptic curves over any field, separable isogenies and kernels; $E[m]$ and the Weil pairing for
  $E$ (proofs or statements there; 11.8(a) is only the general statement); the $\wp$-function and the uniformisation $E(\C)\simeq\C/\Lambda_E$,
  the period lattice of a curve over $\Q$; elliptic curves over finite fields and Hasse. Chapter 8 must not do Weierstrass
  invariants or the group law.
* **Chapter 12** (`ch:modforms`): $\mathbb H$, $\Gamma_0(N)$, cusps and elliptic points, the charts making $X_0(N)(\C)$ a compact Riemann surface,
  the genus formula (as an application of 7.2), $S_2(\Gamma_0(N))\simeq H^0(X_0(N),\Omega^1)$ via $f\mapsto f(z)dz$ (with the check at cusps and
  elliptic points), the Petersson product. Chapter 8 gives the general theory and the pointers 5.5(f), 7.3(f), 8.1(f), 9.3.
* **Chapter 14** (`ch:moddeg`): $X_0(N)$ over $\Q$; $J_0(N)$; the Hecke correspondences $T_p$, $U_p$, $w_N$ and the identities
  $T_n^t=w_NT_nw_N$; the Hecke action on $H_1$, $H^1$, $J_0(N)$, $T_\ell J_0(N)$; Eichler-Shimura; the pairing $\langle x,w_Ny\rangle$ on
  $H^1(X_0(N),\Z_\ell)$ (an application of 12.3(e)); the modular parametrisation, optimal curves, the modular degree and its
  equivalent descriptions; the identification $M_{f,\lambda}=\varphi_E^*H^1(E,\Z_\ell)$ for optimal $E$ (11.5 applied; Part 7). Chapter 8 must state
  everything for a general curve and a general correspondence, and use $X_0(N)$ only in examples and `paperlink`s.
* **Chapter 13** (`ch:hecke`): the Hecke algebra on $S_2$; **Chapter 15**: $\rho_{f,\lambda}$; **Chapter 16**: group cohomology and its cup
  product (10.2(iv) is only a bridge remark); **Chapter 3**: all pairing algebra.

### 6.4 How the relevant important_notes.md points are handled

* **Point 26** (Section 4.2: $M_{f,\lambda}$ is homothetic to the dual of $T_\ell E$). Chapter 8 supplies the facts: 11.7(ii)
  ($H^1=\Hom(T_\ell J,\Z_\ell)$), 11.8(c) ($H^1_{\mathrm{et}}\simeq T_\ell J(-1)$, and for $E$: $H^1(E,\Z_\ell)\simeq T_\ell E(-1)$), and 11.5(iii), (iv) (for an optimal
  quotient the pullback of $H^1(E)$ is saturated). The `paperlink` of Section 11 says: "$M_{f,\lambda}\subset H^1(X_0(N),\Z_\ell)$ is homothetic to the dual
  of $T_\ell E$, that is to $T_\ell E(-1)$; for the optimal curve it is exactly $\varphi_E^*H^1(E,\Z_\ell)\simeq(T_\ell E)^\vee$ (Chapter 14); the adjoints agree
  because $\ad(T^\vee)\simeq\ad T$ and $\ad(T(-1))=\ad T$ (Chapter 4)". Exercise 12. Part 7, point 2 sharpens the note.
* **Point 36** (Lemma lem:hecke and Theorem thm:quant Step 2: the pairing stays perfect on the $\mathfrak m$-component). 12.3(e) states and
  proves the needed sentence in general: every idempotent of a ring of operators all self-adjoint for $[\ ,\ ]$ is self-adjoint,
  the decomposition is orthogonal, and the restriction of a perfect pairing to each summand is perfect (with Chapter 3, 9.5(iii)).
  The `paperlink` of Section 12 quotes Lemma lem:hecke and adds this sentence. Exercise 14.
* **Point 27** (optimality plays no role at $\ell$ when $E[\ell]$ is irreducible) is consistent with 11.5(iii), (v): an isogeny of degree
  prime to $\ell$ changes $\varphi^*H^1$ by an index prime to $\ell$. Mentioned in the pitfall above.
* **Points 11 and B1** (Frobenius conventions): 11.8(d) and C7 state which Frobenius has which eigenvalues on $T_\ell J$ and on $H^1$,
  consistently with Chapter 6, 3.7.
* **Point 35** (Lemma lem:hecke: other local factors lie in the kernel, not the annihilator) is Chapter 3's and Chapter 20's; Chapter 8
  does not touch it, but Part 7, B1 records that the Chapter 21 outline still has the old wording.

### 6.5 References

SilvermanAEC (I.1 to I.3, II.1 to II.5, III.3, III.8; the theorem numbers II.1.1, II.2.1, II.2.3, II.2.4, II.2.6, II.2.11, II.5.4,
II.5.9, III.3.1 are cited with confidence, the others by section), Hartshorne (I.6 Corollary 6.12, II.6 Proposition 6.9, IV.1
Theorem 1.3, IV.2 Corollary 2.4; Appendix B), Fulton (Algebraic curves: Chapters 3, 5, 7, 8), Miranda (Chapters I to VIII, by
chapter only), Shimura71 (Chapter 7), DiamondShurman (Section 6.3), BLR (Chapter 9) are in `refs.bib`. Not in `refs.bib`, to be
added to `bib/ch08.bib` if cited: Forster, *Lectures on Riemann Surfaces* (GTM 81); Griffiths-Harris, *Principles of Algebraic
Geometry*; Farkas-Kra, *Riemann Surfaces* (GTM 71); Hatcher, *Algebraic Topology*; Milne, *Jacobian varieties* (in Cornell-Silverman,
*Arithmetic Geometry*, 1986) and *Abelian varieties* (same volume, and his online notes); Mumford, *Abelian Varieties*; Milne,
*Lectures on Etale Cohomology* (online notes); Lang, *Algebra* (already a standard key `Lang`). All section and chapter numbers for
Miranda, Forster, Griffiths-Harris, Farkas-Kra, Milne and Mumford were recalled, not re-verified: cite them by chapter or section
only, as marked above, and check before giving any theorem number.

### 6.6 Verification log (computations done for this outline)

Python 3 with sympy 1.14, scripts `check1.py`, `check2.py` in `/tmp/ch08`.
* Genera of $X_0(N)$ from the formula $g=1+\mu/12-\nu_2/4-\nu_3/3-\nu_\infty/2$ (Chapter 12): $N=1$: $0$; $11$: $1$; $20$: $1$; $37$: $2$; $77$: $7$; $99$: $9$;
  $121$: $6$ ($\mu=132$, $\nu_2=\nu_3=0$, $\nu_\infty=12$); $140$: $19$; $539$: $49$ ($\mu=672$, $\nu_\infty=16$); $726$: $109$; $980$: $145$. The known values
  $g(X_0(11))=g(X_0(20))=1$, $g(X_0(37))=2$ are reproduced.
* Riemann-Hurwitz totals for the paper's parametrisations (degrees from the paper and the Chapter 21 outline's ecdata
  check): 11a1 and 20a1: degree $1$, total ramification $0$; 121a1: degree $6$, total $10$; 539c1: degree $288$, total $96$; 980i1: degree
  $2880$, total $288$; 726a1: degree $144$, total $216$; 99a1: degree $4$, total $16$.
* Smoothness by Groebner bases over $\Q$ of $\{F,F_X,F_Y,F_Z\}$ in each standard chart: the homogenised Weierstrass equations of
  11a1 $[0,-1,1,-10,-20]$, 121a1 $[1,1,1,-30,-76]$, 20a1 $[0,1,0,4,4]$ and the Fermat curves of degree $3,4,5$ have no singular point
  over $\bar\Q$; the nodal and cuspidal cubics have exactly the singular point $[0:0:1]$.
* By hand: $\operatorname{div}(dx/y)=0$ on $y^2=h(x)$; the bilinear identity 9.4(c) and positivity 9.4(d) on $\C/(\Z+\tau\Z)$ ($\int ds\wedge dt=1$;
  $\frac i2\int dz\wedge d\bar z=\operatorname{Im}(\bar\omega_1\omega_2)$); $\operatorname{PD}(ds)=b$, $\operatorname{PD}(dt)=-a$ and the isometry property under C6 (and under the opposite
  convention, where $\operatorname{PD}$ changes sign on both factors); the adjointness 12.3 by the projection-formula computation in both
  orders of the factors; the component-group formula $M/A(\Lambda)$ in 11.5(iii); the self-adjointness and alternation computation
  of 12.3(e) (it needs $w^*$ to be an isometry with $w^{*2}=1$, which holds for any involutive automorphism); the rank-two Gram
  determinant $d^2$ in 11.5(iv); Riemann-Hurwitz for the hyperelliptic and Fermat examples; the $\psi(z)=iz$ example of 12.4(c).

## 7. Points for important_notes.md

New points in the area of this chapter (the modular parametrisation and its degree, $H^1(X_0(N),\Z_\ell)$ with the cup product and
$\hat\delta_!$, $J_0(N)$ and its Tate module), not among the 38 points and B1, B2 already recorded. Points 26, 27, 35, 36 are used above and
not repeated. None of the three points below changes a result of the paper; point 1 removes a hypothesis from one step.

1. **Lemma lem:hecke (and Remark rem:free, Theorem thm:quant Step 4): the inequality $v_\ell(\deg\varphi_E)\ge v_\lambda(\eta^\emptyset_{f,\lambda})$ is
   always an equality, without the freeness of $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$.**
   Location: Lemma lem:hecke ("with equality if $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ is free over $\T_{\mathfrak m}$"), Remark rem:free ("So the equality ...
   holds under the hypotheses of Lemma lem:hecke"), Theorem thm:quant Step 4 ("By Lemma lem:hecke applied to $E_S$ in the free case
   (Remark rem:free ...)"), Theorem thm:main ("with equality when ... free").
   Argument (with the paper's own definition of $\eta$ as the ideal of values of $\hat\delta_!$ on $M_{f,\lambda}=H^1(X_0(N),\Z_\ell)[\ker\phi_f]$):
   (a) $\varphi_E^*\omega_E$ is a nonzero multiple of $f(z)\,dz$, so $\varphi_E^*H^1(E,\Q)$ is the two-dimensional $f$-part of $H^1(X_0(N),\Q)$, and
   $\varphi_E^*H^1(E,\Z_\ell)\subseteq M_{f,\lambda}$ with finite index. (b) $E$ optimal means $\ker(J_0(N)\to E)$ connected, so $\varphi_{E*}\colon H_1(X_0(N),\Z)\to H_1(E,\Z)$ is
   surjective and $\varphi_E^*H^1(E,\Z)$ is saturated (item 11.5(iii)); hence $M_{f,\lambda}=\varphi_E^*H^1(E,\Z_\ell)$. (c) $\langle\varphi_E^*x,\varphi_E^*y\rangle=\deg\varphi_E\langle x,y\rangle_E$ with
   $\langle\ ,\ \rangle_E$ unimodular (items 11.5(i), 10.3). (d) $w_N$ preserves the $f$-part and acts on it by the Atkin-Lehner sign $\pm1$ (on
   $f\,dz$ and on its conjugate), so $\hat\delta_!(x,y)=\langle x,w_Ny\rangle=\pm\langle x,y\rangle$ on $M_{f,\lambda}$. Hence the ideal of values is
   $\deg\varphi_E\cdot\Z_\ell$, that is, $v_\lambda(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$, for every odd $\ell\nmid N$ (indeed for every $\ell$ for which $\eta$ is defined).
   With Lemma lem:ddt417 this gives back $v_\ell(r_E)\ge v_\ell(\deg\varphi_E)$ (the divisibility of Agashe, Ribet and Stein) and, in the free
   case, their equality; with $v_\ell(\deg\varphi_E)=v_\ell(r_E)$ for $\ell^2\nmid N$ (ARS12 Theorem 2.2, as the paper uses it) it gives
   $v_\ell(r_E)=v_\lambda(\eta^\emptyset_{f,\lambda})$ directly. In Step 4 of Theorem thm:quant the same argument for the optimal curve in the class
   of $E_S$ gives $v_\lambda(\eta^\emptyset_{g,\lambda})=v_\ell(r_{E_S})$ with no appeal to Remark rem:free (which partly answers important_notes.md
   point 24: the middle term of Theorem thm:quant needs ARS12 Theorem 2.2 but not multiplicity one beyond what that theorem uses).
   Fix: replace "with equality if ... free" by "with equality" in Lemma lem:hecke, adding the four lines (a) to (d); Remark
   rem:free then becomes an alternative route (or can be kept as context for the Gorenstein property). Effect: the equality
   clause of Theorem thm:main (eq:identity) holds under the hypotheses of the theorem without citing Tilouine97 and
   RibetStein; no number changes. Confidence: high for (a) to (d) as mathematics; medium on whether DFG04's normalisation of
   $\eta^\emptyset_{f,\lambda}$ agrees exactly with the paper's description "ideal of values of $\hat\delta_!$ on $M_{f,\lambda}$" (if DFG04 normalise the
   pairing differently by a unit, nothing changes; by a non-unit, the paper's description itself would need correcting).

2. **Section 4.2 (supplement to important_notes.md point 26): for the optimal curve, $M_{f,\lambda}$ is exactly the dual of $T_\ell E$, with
   no irreducibility needed.** Location: "(the lattice $M_{f,\lambda}$ of DFG04 and $T_\ell E$ are homothetic when $\bar\rho$ is irreducible,
   so their adjoints coincide)". By point 1(a), (b), $M_{f,\lambda}=\varphi_E^*H^1(E,\Z_\ell)\simeq H^1(E,\Z_\ell)$, and $\varphi_E$ is defined over $\Q$, so in etale
   cohomology this is an isomorphism of $G_\Q$-modules $M_{f,\lambda}\simeq H^1_{\mathrm{et}}(E_{\bar\Q},\Z_\ell)\simeq\Hom(T_\ell E,\Z_\ell)\simeq T_\ell E(-1)$ (items 11.7(ii),
   11.8(c)). Fix: "the lattice $M_{f,\lambda}$ is $\varphi_E^*H^1(E,\Z_\ell)\simeq\Hom_{\Z_\ell}(T_\ell E,\Z_\ell)\simeq T_\ell E(-1)$ for the optimal curve $E$, so $\ad M_{f,\lambda}\simeq\ad T_\ell E$";
   the irreducibility of $\bar\rho$ is then not needed for this identification (it is needed elsewhere, for the homothety class of
   lattices of other curves in the class). Confidence: high (given point 1(a), (b), which use only the definition of optimality
   and the standard fact that $\varphi_E^*\omega_E$ is a multiple of $f(z)dz$).

3. **Remark rem:free: "$T_\ell J_0(N)$" versus "$H^1(X_0(N),\Z_\ell)$" as Hecke modules (expository).** Location: "the localised Hecke
   algebra is then Gorenstein and the Tate module is free of rank two \cite{Tilouine97}" followed by the conclusion for
   $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$. The Tate module carries the Albanese action $\mathcal C_*$ of the Hecke correspondences and $H^1$ the action
   $\mathcal C^*$; Poincare duality turns $\mathcal C^*$ into $(\mathcal C^t)_*$ (item 12.3(c)), so the Hecke-equivariant identification is $x\mapsto w_{N*}\operatorname{PD}(x)$,
   using $T^t=w_NTw_N$ (Chapter 14), not $\operatorname{PD}$ alone; and neither identification is Galois-equivariant (twist by $-1$, point 26).
   Freeness transfers in either case ($t\mapsto w_Ntw_N$ is an automorphism of $\T$ fixing $\mathfrak m$, because $w_N$ acts on the $f$-part by a scalar;
   alternatively $\Hom_{\Z_\ell}(\cdot,\Z_\ell)$ preserves freeness over the Gorenstein ring $\T_{\mathfrak m}$). Fix: add "(via Poincare duality composed with
   $w_N$)" after "the Tate module". Effect: none. Confidence: high; importance low.

Book-internal inconsistencies found while preparing this outline:

* **B1. Chapter 21 outline, A4.4** (expanded proof of Lemma lem:hecke) still says the local factors $\mathfrak m'\ne\mathfrak m$ "are killed by $\phi_f$ and
  lie in $\operatorname{Ann}(\ker\phi_f)$", which important_notes.md point 35 (from the Chapter 3 outline) corrects to "lie in the kernel". The
  Chapter 21 writer must use the corrected wording. (A4.4 does already contain the point 36 sentence.)
* **B2. Chapter 21 outline, A4.6** says $M_{f,\lambda}$ "is homothetic to $T_\ell E$ for $\bar\rho$ irreducible", while its own A4.1 Commentary and
  important_notes.md point 26 say "homothetic to the dual of $T_\ell E$". A4.6 should be brought in line (and can use point 2 above).
* **B3. Notation for adjoints.** Chapter 3, 9.5 writes the adjoint of $A$ as $A^*$; Chapter 4, C2 reserves $^*$ for Pontryagin duals (as the
  paper does); Chapters 8 and 14 need $^*$ for pullbacks ($\varphi^*$, $T^*$, $\mathcal C^*$). This outline writes $A^\dagger$ for adjoints (C4). Appendix B
  should fix one book-wide convention (suggestion: $A^\dagger$ for adjoints, $^\vee$ for linear duals, $^*$ for pullbacks and for the
  paper's Pontryagin duals, which never meet pullbacks in the same formula).
* **B4. Chapter 3 outline, Part 5** lists "Chapters 8, 14" as users of "Gorenstein and the freeness criterion (11.4, 11.5)"; Chapter 8 does
  not use them (Remark rem:free is Chapter 14's and Chapter 20's). Harmless; noted so that no writer looks for Gorenstein rings in
  Chapter 8.
