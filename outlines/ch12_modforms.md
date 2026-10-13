# Chapter 12: Modular forms and modular curves (`ch:modforms`, `chapters/ch12_modforms.tex`)

Stage 1 line-up. Part IV (Modular forms and modular curves). Target length 1,970 lines of LaTeX (card excluded; see
Part 3), inside the 1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2
to 9 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book and
chapter or section; a theorem number only where sure, otherwise marked "(verify)" or given by section); the paper's use
by its `\label` names, or "background". Every number quoted below (indices, cusp counts and widths, elliptic points,
genera, dimensions, Sturm bounds, $q$-expansions, Atkin-Lehner signs, Petersson norms, the paper's congruences) was
checked by Python scripts in `/tmp/ch12` (`check1.py` to `check7.py`), using PARI/GP 2.17 through `cypari2` and Cremona's
`ecdata` files for conductors below 10,000 (verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

The paper uses modular forms in five places, and the chapter is built around them.

1. **The space $S_2(\Gamma_0(N))$, the newform $f=f_E$ and its $q$-expansion** (Section 1, "let $f=f_E\in S_2(\Gamma_0(N))$
   be the newform attached to it"; Section 3 preamble, "the subring of $\operatorname{End}S_2(\Gamma_0(N))$ generated over $\Z$ by all
   $T_n$"; Lemma lem:old, "the forms $h(dz)$ ... span a $\T$-stable subspace of $S_2(\Gamma_0(N))$"). The chapter supplies the
   upper half plane, $\Gamma_0(N)$, the slash operator, holomorphy at the cusps, the spaces $M_k(\Gamma_0(N))$ and
   $S_k(\Gamma_0(N))$, $q$-expansions, their uniqueness (the $q$-expansion principle in its elementary forms), dimension
   formulas, and the worked example $S_2(\Gamma_0(11))=\C\,\eta(z)^2\eta(11z)^2$ whose coefficients are the $a_n$ of 11a1. The
   Hecke operators, newforms and eigenforms are Chapter 13's; this chapter only points forward to them.
2. **Coefficientwise congruences and integral forms** (Section 1, the definition of $r_E$: "$f\equiv g\pmod r$
   coefficientwise for some integral cusp form $g$ of level $N$ orthogonal to $f$"; Lemma lem:crit, "$a_n(g)\equiv a_n(f)\pmod\lambda$
   for every $n\ge1$" and "the pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$"; Theorem thm:twist, "preserves integrality";
   Theorem thm:quant Step 1, "$S_2(\Gamma_0(N);\Z_\ell)$", "the congruence survives"; the Example of Section 3, "checked for
   $p<500$"). The chapter supplies $S_k(\Gamma_0(N);A)$ for subrings $A\subset\C$ and $S_2(\Gamma_0(N);B)=S_2(\Gamma_0(N);\Z)\otimes B$ for
   any ring $B$ (in particular $\Z_\ell$, $\F_\ell$, $\mathcal O_\lambda$), Shimura's integral basis theorem (R), Sturm's bound,
   and the consequences: $S_2(\Gamma_0(N);\Z)$ is a $\Z$-structure of $S_2(\Gamma_0(N))$, saturated in $\Z[[q]]$, its truncated
   $q$-expansion map is a split injection, and congruences can be checked on finitely many coefficients. It proves the
   paper's three congruences of Section 3 for all $n$ (Part 7, point P1). The perfect pairing with $\T$ is Chapter 13's.
3. **The Petersson product and the Petersson norm** (Section 1, "the classical route to the degree is the Petersson
   norm ... $\deg\varphi_E$ is $\langle f,f\rangle$ divided by the area of the period lattice" (Zagier85, Watkins02); "orthogonal to
   $f$" in the definition of $r_E$; $f^\perp$ in Lemma lem:crit; "orthogonal to the newform $f$" in Lemma lem:old; $g^\perp$ in
   Theorem thm:twist). The chapter supplies the definition with an explicit, verified normalisation (unnormalised:
   $\int_{\Gamma_0(N)\backslash\mathfrak H}f\bar g\,y^k\,d\mu$), convergence, positivity, behaviour under change of group and under
   $W_N$, the identity with $\frac i2\int\omega_f\wedge\bar\omega_g$ in weight 2, and the numerical check
   $4\pi^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)=\deg\varphi_E$ on five curves of the paper's world (which fixes the
   normalisation that Chapter 14 must use). Rankin-Selberg is pointed to Chapters 13 and 19, the Zagier-Watkins formula
   with the Manin constant to Chapter 14.
4. **The Atkin-Lehner involution $w_N$** (Section 4.1: "$\hat\delta_!$ is the cup product composed with the operator
   $[UwU]\omega$, $w=\begin{psmallmatrix}0&-1\\M^\Sigma&0\end{psmallmatrix}$, which for weight 2 and trivial character is the Atkin-Lehner
   involution $w_{M^\Sigma}$"; Lemma lem:hecke and Theorem thm:quant Step 2 through it). The chapter supplies $W_d$ for
   $d\,\|\,N$, its normalising property, $W_d^2\in d\,\Gamma_0(N)$, the involutions $w_d$ of $X_0(N)$ and of $M_k(\Gamma_0(N))$, the
   identity $w_N^*(f\,dz)=(f|_2W_N)\,dz$, isometry and self-adjointness for the Petersson product, the action on cusps
   (not simple on $q$-expansions), the moduli description $w_N(E,C)=(E/C,E[N]/C)$, and the sign $f_{11}|W_{11}=-f_{11}$. The
   identity "the cup-product adjoint of $T_n$ is $w_NT_nw_N$" and the pairing $\hat\delta_!$ are Chapter 14's.
5. **$X_0(N)$ as a curve** (Section 1 and the abstract: "$\varphi_E\colon X_0(N)\to E$ its modular parametrisation"; Section 4.1:
   "$H^1(X_0(M^\Sigma),\Z_\ell)$"). The chapter supplies $Y_0(N)=\Gamma_0(N)\backslash\mathfrak H$, its compactification by the cusps, the
   charts, the structure of a compact Riemann surface, the cusps and their widths, the elliptic points, the genus formula
   (as Riemann-Hurwitz for $X_0(N)\to X(1)$, Chapter 8), tables of genera, $\dim S_2(\Gamma_0(N))=g(X_0(N))$ (background to
   multiplicity one), the moduli interpretation by pairs $(E,C)$ over $\C$, and the existence of the model over $\Q$
   (stated). Everything about $X_0(N)$ over $\Q$ beyond that statement, $J_0(N)$ and the modular degree is Chapter 14's.

It also discharges two debts of earlier chapters: Chapter 9 (its 7.5(iii) and the "Uniformisation" writer note) defers
here the fundamental domain of $\SL_2(\Z)$, the $q$-expansion of $j$ and the bijectivity of $j\colon\SL_2(\Z)\backslash\mathfrak H\to\C$ (by
the valence formula); Chapter 8 (its 5.5(f), 7.3(f), 8.1(f), 9.1, 9.3, 9.4 and Part 6.3) defers here the modular curve as a
quotient of the upper half plane, the genus formula as an application of Riemann-Hurwitz, weight-two cusp forms as
holomorphic differentials and the Petersson product.

**The physics reader's complex analysis pays off here**, in one sentence each, at three places:
* **$q$-expansions are Fourier series** (6.3): a function on $\mathfrak H$ of period $1$ in $x$ is a Fourier series in $x$, and holomorphy
  (the Cauchy-Riemann equations) forces the $n$-th mode to be $a_ne^{2\pi inx}e^{-2\pi ny}$, exactly the separated solutions of
  Laplace's equation in a half-strip that decay away from the boundary (RHB's Fourier series and separation of
  variables).
* **The valence formula is the residue theorem** (7.3): the number of zeros of a modular form in a fundamental domain is
  $\frac1{2\pi i}\oint f'/f\,dz$ around its boundary (the argument principle of RHB's contour-integration chapter), and the
  side contributions cancel in pairs by the symmetries $T$ and $S$, leaving $k/12$.
* **The Petersson product is an $L^2$ inner product** (10.1): $\langle f,g\rangle=\int f\bar g\,y^k\,d\mu$ is the weighted $L^2$ inner
  product of functions on a finite-area surface, like the weighted inner products of Sturm-Liouville theory in RHB, and
  Chapter 13's Hecke operators are self-adjoint for it, so their eigenforms are orthogonal (as eigenfunctions of a
  self-adjoint operator are).
PLAN.md's "physics aside: Fourier series on a quotient" is the first of these, placed in 6.3 and recalled in 9.2.

### 1.2 Global conventions fixed in this chapter

* **C1 (the upper half plane).** $\mathfrak H=\{z=x+iy\in\C:y>0\}$ (the paper never names it; Chapter 9 writes $\mathfrak H$). $\mathfrak H^*=\mathfrak H\cup\mathbb P^1(\Q)$,
  $\mathbb P^1(\Q)=\Q\cup\{\infty\}$. $d\mu=dx\,dy/y^2$. $q=e^{2\pi iz}$, and $q_h=e^{2\pi iz/h}$ for a cusp of width $h$. The letter $q$ is
  also the paper's name for a bad prime; in this chapter a prime is called $p$ or $\ell$ and $q$ is always $e^{2\pi iz}$, except
  in `paperlink` environments, which say so.
* **C2 (matrices).** $S=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$, $T=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$, $\rho=e^{2\pi i/3}$. $\GL_2^+(\R)$ acts on $\mathfrak H$ by Moebius
  transformations; $j(\gamma,z)=cz+d$ for $\gamma=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}$. Indices of subgroups of $\SL_2(\Z)$ are written
  $[\SL_2(\Z):\Gamma]$; the degree of $X(\Gamma)\to X(1)$ is the index of the images in $\mathrm{PSL}_2(\Z)$, which equals
  $[\SL_2(\Z):\Gamma]$ when $-I\in\Gamma$ (always for $\Gamma_0(N)$) and half of it otherwise.
* **C3 (the slash operator).** For $\gamma\in\GL_2^+(\R)$, $k\in\Z$ and $f\colon\mathfrak H\to\C$:
  $$(f|_k\gamma)(z)=(\det\gamma)^{k/2}(cz+d)^{-k}f(\gamma z).$$
  Scalars $\lambda I$ with $\lambda>0$ act trivially, $-I$ acts by $(-1)^k$, and $f|_k\gamma|_k\gamma'=f|_k(\gamma\gamma')$. This is the book's
  normalisation (Shimura71 and Miyake use it too, verify before saying so in print); Diamond-Shurman use $(\det\gamma)^{k-1}$, which agrees in weight $2$ (the only weight the paper uses) and differs
  by a positive scalar for $\det\gamma\ne1$ otherwise. In weight $2$: $(f|_2\gamma)(z)\,dz=\gamma^*(f(z)\,dz)$, because
  $d(\gamma z)/dz=\det\gamma/(cz+d)^2$. The choice $(\det)^{k/2}$ makes $W_N$ an exact involution and an isometry in every even
  weight (12.1, 12.2).
* **C4 (Atkin-Lehner).** $W_N=\begin{psmallmatrix}0&-1\\N&0\end{psmallmatrix}$ is the matrix, exactly the paper's $w$ of Section 4.1 (with $M^\Sigma$ in place of
  $N$); $w_N$ denotes both the holomorphic involution $z\mapsto-1/(Nz)$ of $X_0(N)$ and the operator $f\mapsto f|_kW_N$ on forms. Some
  books use $\begin{psmallmatrix}0&1\\-N&0\end{psmallmatrix}=-W_N$; the action on $\mathfrak H$ and on forms of even weight is the same. For $d\,\|\,N$ (that is,
  $d\mid N$ and $\gcd(d,N/d)=1$), $W_d$ is any integer matrix $\begin{psmallmatrix}dx&y\\Nz&dw\end{psmallmatrix}$ of determinant $d$.
* **C5 (the Petersson product).** **Unnormalised**: $\langle f,g\rangle=\langle f,g\rangle_{\Gamma_0(N)}=\int_{\Gamma_0(N)\backslash\mathfrak H}f(z)\overline{g(z)}\,y^k\,d\mu$ (linear in
  the first variable). It is the normalisation in which $4\pi^2\langle f,f\rangle=\deg\varphi_E\cdot\operatorname{vol}(\Lambda_E)$ holds for an optimal curve with Manin
  constant $1$, checked numerically on five curves (10.4); the normalisations of Zagier85 and Watkins02 must be checked against
  their texts before the chapter says they agree. PARI's `mfpetersson` divides by the index $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]$ (checked on five levels, 10.4); other books
  divide by $\operatorname{vol}(\Gamma_0(N)\backslash\mathfrak H)=\pi\mu(N)/3$. The `convention` box says so and never mixes them.
* **C6 (coefficients and integrality).** $a_n(f)$ is the $n$-th coefficient of the expansion at $\infty$. For a subring
  $A\subseteq\C$, $M_k(\Gamma_0(N);A)$ and $S_k(\Gamma_0(N);A)$ are the forms with all $a_n\in A$. For an arbitrary commutative ring $B$
  (such as $\Z_\ell$, $\F_\ell$, $\mathcal O_\lambda$, which are not subrings of $\C$ in a preferred way), $S_k(\Gamma_0(N);B):=S_k(\Gamma_0(N);\Z)\otimes_\Z B$,
  with its $q$-expansion map to $B[[q]]$ (injective by 11.4). "$f\equiv g\pmod{\mathfrak a}$ coefficientwise" means $a_n(f)-a_n(g)\in\mathfrak a$ for
  all $n\ge0$; "at all $n$" and "at all $p\notin\Sigma$" are distinguished every time (the paper distinguishes them in
  Lemma lem:crit versus Lemma lem:old).
* **C7 (counts attached to $N$).** $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]=N\prod_{p\mid N}(1+1/p)$; $\nu_2(N)$, $\nu_3(N)$ the numbers of elliptic points
  of order $2$, $3$; $\nu_\infty(N)$ the number of cusps; $g(N)$ the genus of $X_0(N)$; $B_k(N)=\lfloor k\mu(N)/12\rfloor$ the Sturm bound
  ($B_2(N)=\lfloor\mu(N)/6\rfloor$).
* **C8 (newforms are not defined here).** "Newform", "eigenform", "Hecke operator", "oldform" are Chapter 13's. This chapter
  uses them only in examples and `paperlink`s with a forward `\Cref{ch:hecke}`; when $\dim S_2(\Gamma_0(N))=1$ the unique
  normalised form is called "the normalised generator", not "the newform", until Chapter 13.
* **C9 (typography).** PLAN.md Section 7.2: no dash ligatures ("Atkin-Lehner", "Riemann-Hurwitz", "Ramanujan-Petersson",
  "Diamond-Shurman" with plain hyphens; ranges as "1 to 8"), ASCII source, labels `...:modforms:...`, tables with `booktabs`.

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 1. The upper half plane and the action of $\SL_2(\R)$

**1.1 `prop:modforms:upper-half-plane`** (definition and proposition; P). $\GL_2^+(\R)$ acts on $\mathfrak H$ by
$\gamma z=\frac{az+b}{cz+d}$, through $\GL_2^+(\R)/\R^\times$. For $\gamma\in\GL_2^+(\R)$ and $z\in\mathfrak H$: (i) $\operatorname{Im}(\gamma z)=\det\gamma\cdot\operatorname{Im}z/|cz+d|^2$, so
$\gamma z\in\mathfrak H$; (ii) $\frac{d}{dz}(\gamma z)=\det\gamma/(cz+d)^2$; (iii) the cocycle identity $j(\gamma\gamma',z)=j(\gamma,\gamma'z)\,j(\gamma',z)$ for
$j(\gamma,z)=cz+d$; (iv) $\mathrm{PSL}_2(\R)=\SL_2(\R)/\{\pm I\}$ acts faithfully and transitively, and the stabiliser of $i$ in $\SL_2(\R)$ is
$\mathrm{SO}(2)$, so $\mathfrak H\simeq\SL_2(\R)/\mathrm{SO}(2)$; (v) $d\mu=dx\,dy/y^2$ is $\GL_2^+(\R)$-invariant (by (i), (ii) and the Jacobian
$|d(\gamma z)/dz|^2$). Reference: Shimura71 1.1; DiamondShurman 1.1 and 2.1 (cite the sections); SerreCourse VII.1. Paper:
background. Physics aside (one sentence): $ds^2=(dx^2+dy^2)/y^2$ is the hyperbolic metric and the Moebius maps are its
isometries.

**1.2 `prop:modforms:element-types`** (definition and proposition; P). For $\gamma\in\SL_2(\R)$, $\gamma\ne\pm I$: $\gamma$ is *elliptic* if
$|\operatorname{tr}\gamma|<2$ (exactly one fixed point in $\mathfrak H$, and $\gamma$ has finite order when $\gamma\in\SL_2(\Z)$, namely $3$, $4$ or $6$), *parabolic* if
$|\operatorname{tr}\gamma|=2$ (exactly one fixed point, in $\mathbb P^1(\R)$), *hyperbolic* if $|\operatorname{tr}\gamma|>2$ (two fixed points in $\mathbb P^1(\R)$, none in $\mathfrak H$).
Proof: solve $cz^2+(d-a)z-b=0$; discriminant $(\operatorname{tr}\gamma)^2-4$. For $\gamma\in\SL_2(\Z)$ elliptic, $\operatorname{tr}\gamma\in\{0,\pm1\}$ and the characteristic
polynomial is $X^2+1$ or $X^2\pm X+1$. The set of fixed points of the parabolic elements of $\SL_2(\Z)$ is exactly $\mathbb P^1(\Q)$ (the
*cusps*). Reference: Shimura71 1.1 to 1.3 (cite the sections); DiamondShurman 2.3. Paper: background (elliptic points
and cusps of 4.1 to 4.3).

### Section 2. The modular group and its fundamental domain

**2.1 `thm:modforms:fundamental-domain`** (theorem; P). Let $\mathcal F=\{z\in\mathfrak H:|\operatorname{Re}z|\le\frac12,\ |z|\ge1\}$ and $G=\langle S,T\rangle\subseteq\SL_2(\Z)$.
(i) Every $z\in\mathfrak H$ is $G$-equivalent to a point of $\mathcal F$ (choose $\gamma\in G$ maximising $\operatorname{Im}\gamma z$, which exists by 1.1(i) since
$\{(c,d):|cz+d|\le1\}$ is finite, then translate by a power of $T$; if $|\gamma z|<1$, $S$ increases the imaginary part). (ii) If
$z\ne z'$ in $\mathcal F$ are $\SL_2(\Z)$-equivalent then $\operatorname{Re}z=\pm\frac12$ and $z'=z\mp1$, or $|z|=1$ and $z'=-1/z$. (iii) The stabiliser of
$z\in\mathcal F$ in $\mathrm{PSL}_2(\Z)$ is trivial except: $z=i$ (generated by $S$, order $2$), $z=\rho$ (generated by $ST$, order $3$), $z=-\bar\rho$
(generated by $TS$, order $3$). (iv) $G=\SL_2(\Z)$: $S$ and $T$ generate, with $S^2=(ST)^3=-I$. (v) $\operatorname{vol}_\mu(\mathcal F)=\pi/3$. Reference:
SerreCourse VII.1 (Theorem 1 and Theorem 2; verify the numbering); DiamondShurman 2.3 (cite the section). Paper: background
(Chapter 9's deferral: "isomorphism classes of $E/\C$ = $\SL_2(\Z)\backslash\mathfrak H$").

**2.2 `cor:modforms:level-one-quotient`** (corollary; P). $\SL_2(\Z)\backslash\mathfrak H$ is obtained from $\mathcal F$ by gluing the two vertical sides
by $T$ and the two halves of the arc by $S$; adding the point $\infty$ gives $X(1)=\SL_2(\Z)\backslash\mathfrak H^*$, homeomorphic to a
sphere (a closed disc whose boundary is folded and glued; P by an explicit cell decomposition: one vertex class
$\{\rho,-\bar\rho\}$, the point $i$, the edges, one face, $\chi=2$). So $X(1)$ has genus $0$ before $j$ is introduced; this
feeds the genus formula 5.3 without circularity. The orbits of $i$ and $\rho$ are the only elliptic points of $\SL_2(\Z)$,
with isotropy orders $2$ and $3$ in $\mathrm{PSL}_2(\Z)$. Reference: DiamondShurman 2.3; SerreCourse VII.1. Paper: background.

### Section 3. Congruence subgroups and their indices

**3.1 `def:modforms:congruence-subgroups`** (definitions and proposition; P). For $N\ge1$:
$\Gamma(N)=\ker(\SL_2(\Z)\to\SL_2(\Z/N))$, $\Gamma_1(N)=\{\gamma\equiv\begin{psmallmatrix}1&*\\0&1\end{psmallmatrix}\bmod N\}$, $\Gamma_0(N)=\{\gamma\equiv\begin{psmallmatrix}*&*\\0&*\end{psmallmatrix}\bmod N\}$, so
$\Gamma(N)\subseteq\Gamma_1(N)\subseteq\Gamma_0(N)\subseteq\SL_2(\Z)$; a *congruence subgroup* is any $\Gamma\supseteq\Gamma(N)$ for some $N$. (i) Reduction
$\SL_2(\Z)\to\SL_2(\Z/N)$ is surjective (lift $\bar\gamma$ to an integer matrix of determinant $\equiv1$, adjust a row using
$\gcd$ and the Chinese remainder theorem; Chapter 2), so $\Gamma(N)$ is normal of index
$\#\SL_2(\Z/N)=N^3\prod_{p\mid N}(1-p^{-2})$. (ii) $[\SL_2(\Z):\Gamma_1(N)]=N^2\prod_{p\mid N}(1-p^{-2})$ (bottom rows of order $N$) and
$[\Gamma_0(N):\Gamma_1(N)]=\varphi(N)$ ($\gamma\mapsto d\bmod N$ onto $(\Z/N)^\times$). (iii) $\Gamma_0(N)\backslash\SL_2(\Z)\simeq\mathbb P^1(\Z/N)$ via
$\Gamma_0(N)\gamma\mapsto(c:d)$, so $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]=\#\mathbb P^1(\Z/N)=N\prod_{p\mid N}(1+1/p)$. (iv) $-I\in\Gamma_0(N)$ always, and $-I\in\Gamma_1(N)$ iff
$N\le2$. Examples: $\mu(11)=12$, $\mu(20)=36$, $\mu(37)=38$, $\mu(99)=144$, $\mu(121)=132$, $\mu(539)=672$, $\mu(726)=1584$, $\mu(980)=2016$
(verified; the orders of $\SL_2(\Z/N)$ and the $\Gamma_1(N)$ indices by enumeration for $N\le12$). Reference: DiamondShurman 1.2
and 3.9 (cite the sections); Shimura71 1.6. Paper: Section 1 ("$S_2(\Gamma_0(N))$"); Remark rem:free ($J_1(N)$, pull-back to
$J_0(N)$: Chapter 14).

**3.2 `prop:modforms:coset-domains`** (proposition; P). If $\SL_2(\Z)=\bigsqcup_{i=1}^{\mu}\Gamma_0(N)\gamma_i$, then $\bigcup_i\gamma_i\mathcal F$ is a fundamental
domain for $\Gamma_0(N)$ (every point is $\Gamma_0(N)$-equivalent to a point of it; interiors of distinct translates are
disjoint and inequivalent), and $\operatorname{vol}_\mu(\Gamma_0(N)\backslash\mathfrak H)=\mu(N)\pi/3$. For $N=p$ prime one may take $\gamma_0=I$ and $\gamma_{j+1}=ST^j$,
$0\le j\le p-1$ (bottom rows $(0:1)$ and $(1:j)$). Example: $\Gamma_0(11)$ has $12$ translates of $\mathcal F$, eleven of them clustered at
$0$. Reference: DiamondShurman 2.3 (exercises; cite the section). Paper: background (10.1 integrates over this domain;
Exercise 3).

### Section 4. Cusps, widths and elliptic points of $\Gamma_0(N)$

**4.1 `def:modforms:cusp-width`** (definitions and proposition; P). The *cusps* of a congruence subgroup $\Gamma$ are the
$\Gamma$-orbits on $\mathbb P^1(\Q)$, finitely many since $\SL_2(\Z)$ acts transitively on $\mathbb P^1(\Q)$ and $[\SL_2(\Z):\Gamma]<\infty$. The *width* of the
cusp $s=\sigma\infty$ ($\sigma\in\SL_2(\Z)$) is the least $h\ge1$ with $\pm\sigma T^h\sigma^{-1}\in\Gamma$; it depends only on the $\Gamma$-orbit of $s$. (i)
Cusps of $\Gamma$ correspond to the orbits of $\langle\pm T\rangle$ acting on the right on $\Gamma\backslash\SL_2(\Z)$, and the width is the orbit length;
hence $\sum_{\text{cusps}}h_s=[\mathrm{PSL}_2(\Z):\bar\Gamma]$. (ii) When $-I\notin\Gamma$ a cusp is *irregular* if $-\sigma T^h\sigma^{-1}\in\Gamma$ but
$\sigma T^h\sigma^{-1}\notin\Gamma$ (example: the cusp $1/2$ of $\Gamma_1(4)$); $\Gamma_0(N)$ has no irregular cusps since $-I\in\Gamma_0(N)$. Reference:
DiamondShurman 2.4 and 3.8 (cite the sections); Shimura71 1.4. Paper: background.

**4.2 `prop:modforms:cusps-gamma0`** (proposition; P for $N$ squarefree and for $N=p^2$, S in general). (i) Every cusp of
$\Gamma_0(N)$ is equivalent to some $a/c$ with $c\mid N$, $c\ge1$, $\gcd(a,c)=1$; $a/c$ and $a'/c'$ of this form are equivalent iff $c=c'$
and $a\equiv a'\pmod{\gcd(c,N/c)}$. Hence
$$\nu_\infty(N)=\sum_{c\mid N}\varphi(\gcd(c,N/c)),$$
and the cusp $a/c$ has width $N/\gcd(c^2,N)$. (ii) $\infty\sim1/N$ has width $1$ and $0=0/1$ has width $N$. (iii) For $N$ squarefree the
cusps are $1/c$, $c\mid N$, $2^{\omega(N)}$ of them, of widths $N/c$. Examples (each checked by brute force on $\mathbb P^1(\Z/N)$ against
the orbit lengths of $T$): $N=11$: $\infty$, $0$, widths $1,11$; $N=20$: six cusps, widths $1,1,4,5,5,20$; $N=99$: eight cusps,
widths $1,1,1,9,11,11,11,99$; $N=121$: twelve cusps $\infty$, $0$, $a/11$ ($1\le a\le10$), widths $1,121$ and ten of width $1$;
$\nu_\infty(539)=16$, $\nu_\infty(726)=\nu_\infty(980)=48$. Reference: DiamondShurman 3.8 (cite the section); Ogg's "Rational points on
certain elliptic modular curves" (1973; add to `bib/ch12.bib` if cited). Paper: background (the cusps of $X_0(N)$; the
cusp $\infty$ is the base point of $\varphi_E$, Chapter 14).

**4.3 `prop:modforms:elliptic-gamma0`** (proposition; P). The elliptic points of order $2$ (respectively $3$) of $\Gamma_0(N)$
on $Y_0(N)$ are in bijection with the solutions $x\bmod N$ of $x^2+1\equiv0$ (respectively $x^2+x+1\equiv0$), hence
$$\nu_2(N)=\begin{cases}0&4\mid N\\\prod_{p\mid N}\bigl(1+\bigl(\tfrac{-4}{p}\bigr)\bigr)&\text{otherwise,}\end{cases}\qquad
\nu_3(N)=\begin{cases}0&9\mid N\\\prod_{p\mid N}\bigl(1+\bigl(\tfrac{-3}{p}\bigr)\bigr)&\text{otherwise,}\end{cases}$$
with $(\frac{-4}{2})=(\frac{-3}{3})=0$ (Kronecker symbols, Chapter 2). Proof: an elliptic point of order $2$ on $Y_0(N)$ lies over $i\in X(1)$ and
corresponds to a coset $\Gamma_0(N)\gamma$ fixed by $S$, that is, a point $(c:d)\in\mathbb P^1(\Z/N)$ with $(d:-c)=(c:d)$; count with the
Chinese remainder theorem and Hensel (Chapter 2). Likewise with $ST$ for order $3$. Examples: $\nu_2(11)=\nu_3(11)=0$; $\nu_2(13)=\nu_3(13)=2$;
$\nu_2(37)=\nu_3(37)=2$; $\nu_2=\nu_3=0$ for $N=121,539,726,980$. Reference: DiamondShurman 3.7 and 3.8 (cite the sections);
Shimura71 Proposition 1.43 (verify). Paper: background.

### Section 5. The modular curves as compact Riemann surfaces; genus; moduli

**5.1 `thm:modforms:y0-riemann-surface`** (theorem; P for (i), S for (ii)). Let $\Gamma$ be a congruence subgroup. (i) The action of $\Gamma$ on
$\mathfrak H$ is properly discontinuous: for compact $K\subset\mathfrak H$, $\{\gamma\in\Gamma:\gamma K\cap K\ne\emptyset\}$ is finite (1.1(i) bounds $|cz+d|$, hence $c,d$,
then $a,b$); every point has a neighbourhood $U$ with $\gamma U\cap U\ne\emptyset$ only for $\gamma$ in its (finite cyclic) stabiliser modulo
$\pm I$. Hence $Y(\Gamma)=\Gamma\backslash\mathfrak H$ is Hausdorff and connected. (ii) Charts: near a non-elliptic point, a local inverse of
$\mathfrak H\to Y(\Gamma)$; near an elliptic point $z_0$ with stabiliser of order $e$ in $\bar\Gamma$, $t=\bigl(\frac{z-z_0}{z-\bar z_0}\bigr)^e$. Transition maps
are holomorphic, so $Y(\Gamma)$ is a Riemann surface. Reference: DiamondShurman 2.1, 2.2; Shimura71 1.5 (cite the
sections). Paper: background (Section 1: $X_0(N)$).

**5.2 `thm:modforms:x0-compact`** (theorem; S). Topologise $\mathfrak H^*=\mathfrak H\cup\mathbb P^1(\Q)$ with the horoball neighbourhoods
$\{\operatorname{Im}z>C\}\cup\{\infty\}$ of $\infty$ and their $\SL_2(\Z)$-translates (discs tangent to $\R$) at the other cusps. Then
$X(\Gamma)=\Gamma\backslash\mathfrak H^*$ is a compact connected Hausdorff space ($\mathfrak H^*=\SL_2(\Z)(\mathcal F\cup\{\infty\})$ and $\Gamma$ has finite index), and with
the chart $q_h=e^{2\pi i\sigma^{-1}(z)/h}$ at a cusp $s=\sigma\infty$ of width $h$ it is a compact Riemann surface. We write $X_0(N)$,
$X_1(N)$, $X(N)$ for $\Gamma_0(N)$, $\Gamma_1(N)$, $\Gamma(N)$, and $X(1)$ for $\SL_2(\Z)$. By Riemann existence and GAGA (Chapter 8, its 8.3) $X_0(N)$ is
a smooth projective curve over $\C$, and holomorphic maps between these surfaces are morphisms. Reference:
DiamondShurman 2.4; Shimura71 1.5. Paper: Section 1 and the abstract ("$\varphi_E\colon X_0(N)\to E$"), Section 4.1
($H^1(X_0(M^\Sigma),\Z_\ell)$ is the $H^1$ of this compact Riemann surface, Chapter 8, its 10.2).

**5.3 `thm:modforms:genus-formula`** (theorem; P given Chapter 8's Riemann-Hurwitz, its 7.2 and 8.4(c), and 2.2). The map
$\pi\colon X_0(N)\to X(1)$, $\Gamma_0(N)z\mapsto\SL_2(\Z)z$, is holomorphic of degree $\mu(N)$ (since $-I\in\Gamma_0(N)$), unramified outside the images
of $i$, $\rho$, $\infty$. Above $i$ there are $\nu_2$ points with $e=1$ and $(\mu-\nu_2)/2$ with $e=2$; above $\rho$, $\nu_3$ points with $e=1$ and
$(\mu-\nu_3)/3$ with $e=3$; above $\infty$ the $\nu_\infty$ cusps with $e$ equal to the width. With $g(X(1))=0$ (2.2),
$$g(X_0(N))=1+\frac{\mu(N)}{12}-\frac{\nu_2(N)}{4}-\frac{\nu_3(N)}{3}-\frac{\nu_\infty(N)}{2}.$$
Table (verified: the formula against brute-force counts on $\mathbb P^1(\Z/N)$ for every tabulated $N\le140$, and $g$ against PARI's
`mfdim([N,2],1)`, which equals $g$ by 8.2, for every tabulated $N$):

| $N$ | $\mu$ | $\nu_2$ | $\nu_3$ | $\nu_\infty$ | $g$ | | $N$ | $\mu$ | $\nu_2$ | $\nu_3$ | $\nu_\infty$ | $g$ |
|-|-|-|-|-|-|-|-|-|-|-|-|-|
| 1 | 1 | 1 | 1 | 1 | 0 | | 37 | 38 | 2 | 2 | 2 | 2 |
| 11 | 12 | 0 | 0 | 2 | 1 | | 43 | 44 | 0 | 2 | 2 | 3 |
| 13 | 14 | 2 | 2 | 2 | 0 | | 77 | 96 | 0 | 0 | 4 | 7 |
| 14 | 24 | 0 | 0 | 4 | 1 | | 99 | 144 | 0 | 0 | 8 | 9 |
| 20 | 36 | 0 | 0 | 6 | 1 | | 121 | 132 | 0 | 0 | 12 | 6 |
| 23 | 24 | 0 | 0 | 2 | 2 | | 140 | 288 | 0 | 0 | 12 | 19 |
| 25 | 30 | 2 | 0 | 6 | 0 | | 539 | 672 | 0 | 0 | 16 | 49 |
| 27 | 36 | 0 | 0 | 6 | 1 | | 726 | 1584 | 0 | 0 | 48 | 109 |
| 36 | 72 | 0 | 0 | 12 | 1 | | 980 | 2016 | 0 | 0 | 48 | 145 |

$g(X_0(N))=0$ exactly for $N\in\{1,\dots,10,12,13,16,18,25\}$ and $g=1$ for $N\in\{11,14,15,17,19,20,21,24,27,32,36,49\}$ (verified for
$N\le2000$ with the formula; that the lists are complete for all $N$ is stated (R), and Exercise 6 gives the elementary
lower bound for $g$ that reduces it to a finite check). In particular
$X_0(11)$ has genus $1$ (PLAN.md). These agree with the Chapter 8 outline's list (its 5.5(f) and 6.6). Reference:
DiamondShurman Theorem 3.1.1 and Section 3.9 (verify the number); Shimura71 Proposition 1.40 (verify). Paper: background
(Section 1; $\dim S_2(\Gamma_0(N))$ and multiplicity one).

**5.4 `thm:modforms:moduli`** (theorem; P for (i) to (iii), R for (iv), (v)). (i) Every pair $(E,C)$ with $E/\C$ an elliptic
curve and $C\subset E$ a cyclic subgroup of order $N$ is isomorphic to $(\C/\Lambda_\tau,\langle\frac1N+\Lambda_\tau\rangle)$ for some $\tau\in\mathfrak H$,
$\Lambda_\tau=\Z+\Z\tau$, and $\Gamma_0(N)\tau\mapsto$ this pair is a bijection from $Y_0(N)$ onto isomorphism classes of such pairs (Chapter 9,
its 7.5(i), plus the computation of which $\gamma\in\SL_2(\Z)$ preserve $\langle\frac1N\rangle$). (ii) Likewise $Y_1(N)\leftrightarrow\{(E,P):P$ of exact
order $N\}$ via $\Gamma_1(N)\tau\mapsto(\C/\Lambda_\tau,\frac1N)$, and $Y(N)\leftrightarrow\{(E,(P,Q)):$ basis of $E[N]$ with Weil pairing $e^{2\pi i/N}\}$ (with
the sign convention of Chapter 9, C7). (iii) The forgetful map $(E,C)\mapsto E$ is $\pi$ of 5.3, and $(E,C)\mapsto(E/C,E[N]/C)$ is
$\Gamma_0(N)\tau\mapsto\Gamma_0(N)(-1/(N\tau))$, that is, $w_N$ (12.1(v)). (iv) (Cusps.) The cusps correspond to degenerate objects:
generalised elliptic curves (Neron polygons) with a cyclic subgroup, or the Tate curve $\mathbb G_m/q^\Z$ with the subgroup
$\mu_N$ (the cusp $\infty$) or a subgroup generated by an $N$-th root of $q$ (the cusp $0$); stated with reference to
Deligne-Rapoport, no details. (v) ($\Q$-structure.) There is a
smooth projective curve $X_0(N)_\Q$ over $\Q$ whose complex points are $X_0(N)$, such that the bijection of (i) is
$G_\Q$-equivariant on $\bar\Q$-points ($\sigma\in G_\Q$ acting on pairs over $\bar\Q$ by conjugating equations); the cusps $\infty$ and $0$ are
$\Q$-rational and a cusp of denominator $c$ is defined over $\Q(\zeta_{\gcd(c,N/c)})$. Reference: DiamondShurman 1.5 and 7.7
(cite the sections); Shimura71 6.7 (cite the section); Deligne-Rapoport (Lecture Notes in Math. 349, 1973) and
Katz-Mazur (Annals of Math. Studies 108, 1985), to be added to `bib/ch12.bib`; Ogg (1973) for the fields of definition of
cusps. Paper: Section 1 ("$X_0(N)$-optimal", "$\varphi_E\colon X_0(N)\to E$"; Chapter 14 builds on (v)), Remark rem:free
($J_1(N)$, via (ii)).

### Section 6. Modular forms, $q$-expansions, nebentypus

**6.1 `def:modforms:slash`** (definition and proposition; P). The slash operator of C3. (i) $f|_k\gamma|_k\gamma'=f|_k(\gamma\gamma')$ (by 1.1(iii));
(ii) $f|_k(\lambda I)=\operatorname{sign}(\lambda)^kf$; (iii) in weight $2$, $(f|_2\gamma)(z)\,dz=\gamma^*(f(z)\,dz)$, the pullback of the differential under
$z\mapsto\gamma z$ (by 1.1(ii)); (iv) $\operatorname{Im}(\gamma z)^{k/2}|f(\gamma z)|=\operatorname{Im}(z)^{k/2}|(f|_k\gamma)(z)|$ for $\gamma\in\GL_2^+(\R)$ (by 1.1(i)): the function
$y^{k/2}|f|$ transforms like a function. Remark: with Diamond-Shurman's $(\det\gamma)^{k-1}$ the same holds in weight $2$; (iv) and
the isometry 12.2 need $(\det\gamma)^{k/2}$. Reference: Shimura71 2.1; DiamondShurman 1.2 (cite the sections). Paper: Section 4.1
(the operator $[UwU]\omega$ of DFG04 is a slash operator; for weight $2$ and trivial character it is $f\mapsto f|_2W_{M^\Sigma}$).

**6.2 `def:modforms:modular-form`** (definition; P for the remarks). Let $\Gamma$ be a congruence subgroup and $k\in\Z$. A *modular
form of weight $k$ for $\Gamma$* is a holomorphic $f\colon\mathfrak H\to\C$ with $f|_k\gamma=f$ for all $\gamma\in\Gamma$ that is *holomorphic at every cusp*: for
every $\sigma\in\SL_2(\Z)$, $f|_k\sigma$ is bounded on $\{\operatorname{Im}z\ge1\}$ (equivalently, by 6.3, $f|_k\sigma=\sum_{n\ge0}b_nq_h^n$ with $h$ the width of
$\sigma\infty$, for $\Gamma$ without irregular cusps). It is a *cusp form* if moreover $b_0=0$ for every $\sigma$ (vanishing at every
cusp). $M_k(\Gamma)\supseteq S_k(\Gamma)$; $M_k(\Gamma_0(N))$, $S_k(\Gamma_0(N))$ are the spaces of the paper ("$S_2(\Gamma_0(N))$", "cusp form of
level $N$"). Remarks (P): (a) the condition at $\sigma$ depends only on the cusp $\sigma\infty$ modulo $\Gamma$; (b) if $-I\in\Gamma$ and $k$ is odd
then $M_k(\Gamma)=0$, so for $\Gamma_0(N)$ only even $k$ matter; (c) $M_k(\Gamma)\subseteq M_k(\Gamma')$ for $\Gamma'\subseteq\Gamma$; (d) $M_k(\Gamma)M_l(\Gamma)\subseteq M_{k+l}(\Gamma)$;
(e) for $f\in M_k(\Gamma_0(M))$ and $d\ge1$, $f(dz)=d^{-k/2}(f|_k\begin{psmallmatrix}d&0\\0&1\end{psmallmatrix})(z)$ lies in $M_k(\Gamma_0(Md))$ (P; the systematic use, oldforms, is
Chapter 13's, C8). Reference: DiamondShurman 1.2; Shimura71 2.1; SerreCourse VII.2. Paper: Section 1 ("$f=f_E\in S_2(\Gamma_0(N))$"),
Section 3 (the forms $h(dz)$ of Lemma lem:old: (e)), Section 4.1 ($f^\Sigma$ of level $M^\Sigma$, Chapter 13).

**6.3 `prop:modforms:q-expansion`** (proposition; P). Let $f\in M_k(\Gamma_0(N))$. (i) $f(z+1)=f(z)$, and
$f(z)=\sum_{n\ge0}a_n(f)q^n$, $q=e^{2\pi iz}$, converging absolutely and uniformly on $\{\operatorname{Im}z\ge y_0\}$ for every $y_0>0$, with
$a_n(f)=\int_0^1f(x+iy)e^{-2\pi in(x+iy)}\,dx$ for every $y>0$. (ii) For a holomorphic $f$ of period $1$, $f(z)=F(q)$ with $F$ holomorphic on
the punctured disc, and "bounded as $\operatorname{Im}z\to\infty$" is equivalent to "$F$ has a removable singularity at $0$" (Riemann), that is,
to $a_n=0$ for $n<0$; then $f(\infty):=a_0(f)$. (iii) The expansion at a cusp $s=\sigma\infty$ of width $h$ is that of $f|_k\sigma$ in $q_h$.
(iv) (Analytic $q$-expansion principle.) $f\mapsto(a_n(f))_{n\ge0}$ is injective on $M_k(\Gamma_0(N))$ (identity theorem); more precisely, by
8.1, $f$ is determined by $a_0,\dots,a_{B_k(N)}$. Physics aside: (i) is the Fourier series of a function periodic in $x$, and
holomorphy forces each mode $a_n(y)e^{2\pi inx}$ to be $a_ne^{-2\pi ny}e^{2\pi inx}$: Fourier series on the quotient $\mathfrak H/\langle T\rangle$, a
half-cylinder (Part 1.1). Reference: DiamondShurman 1.1, 1.2; SerreCourse VII.2. Paper: Section 1 ("coefficientwise"),
Lemma lem:crit, the Example of Section 3 (all statements about $a_n$ are about this expansion).

**6.4 `prop:modforms:hecke-bound`** (proposition; P). If $f\in S_k(\Gamma_0(N))$ then $y^{k/2}|f(z)|$ is bounded on $\mathfrak H$ (it is
$\Gamma_0(N)$-invariant by 6.1(iv), continuous, and tends to $0$ at every cusp, since $|f|_k\sigma(z)|\le Ce^{-2\pi y/h}$ near $\infty$), and hence
$|a_n(f)|\le C_fn^{k/2}$ for all $n\ge1$ (integrate over $x\in[0,1]$ at height $y=1/n$). Consequently $\sum a_n(f)n^{-s}$ converges
absolutely for $\operatorname{Re}s>k/2+1$. For $f\in M_k$ not cuspidal, $a_n=O(n^{k-1+\varepsilon})$ (example $E_k$: $\sigma_{k-1}(n)$). Reference: SerreCourse
VII.4; DiamondShurman 5.9 (cite the section). Paper: background ($L(f,s)$, Chapters 13 and 19; the convergence of the
Petersson integral, 10.1).

**6.5 `thm:modforms:ramanujan-petersson`** (theorem; R). Let $f\in S_k(\Gamma_0(N))$ be a normalised newform (Chapter 13) and
$p\nmid N$. Then $|a_p(f)|\le2p^{(k-1)/2}$; equivalently the roots $\alpha_p,\beta_p$ of $X^2-a_p(f)X+p^{k-1}$ satisfy
$|\alpha_p|=|\beta_p|=p^{(k-1)/2}$, so $\beta_p=\bar\alpha_p$ and $|\alpha_p/\beta_p|=1$; and $a_n(f)=O(n^{(k-1)/2+\varepsilon})$. For $k=2$ this is Eichler-Shimura
plus Weil's Riemann hypothesis for curves over $\F_p$ (Chapter 8, its 11.8(d); Chapter 14); for $f=f_E$ it is Hasse's bound
(Chapter 9); in general Deligne. Checks: $|a_p(\text{11a1})|\le2\sqrt p$ for all $p<10^5$; Ramanujan's $|\tau(p)|\le2p^{11/2}$ for $p<2000$.
Reference: DiamondShurman, Chapter 8 (statement; verify the section before citing it); Deligne, La conjecture de Weil I (1974; `Deligne` in
`refs.bib`). Paper: background (Lemma lem:euler and Theorem thm:dfg14 use $\alpha,\beta$ with $\alpha\beta=q$; the level-raising
factor $(1-\frac\alpha\beta q^{-1})(1-q^{-1})(1-\frac\beta\alpha q^{-1})$ is a nonzero real number because $|\alpha/\beta|=1$).

**6.6 `def:modforms:nebentypus`** (definition and proposition; P for (i), (ii), S for (iii)). Let $\chi$ be a Dirichlet character
modulo $N$. $M_k(\Gamma_0(N),\chi)=\{f\in M_k(\Gamma_1(N)):f|_k\gamma=\chi(d)f\ \forall\gamma=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\in\Gamma_0(N)\}$, and $S_k(\Gamma_0(N),\chi)$ likewise; $\chi$ is the
*nebentypus* (character). (i) $M_k(\Gamma_0(N),\mathbf 1)=M_k(\Gamma_0(N))$. (ii) $M_k(\Gamma_0(N),\chi)=0$ unless $\chi(-1)=(-1)^k$ (apply $\gamma=-I$). (iii)
The *diamond operators* $\langle d\rangle f=f|_k\gamma$ ($\gamma\in\Gamma_0(N)$ with lower right entry $\equiv d$) give an action of $(\Z/N)^\times$ on $M_k(\Gamma_1(N))$
and $M_k(\Gamma_1(N))=\bigoplus_\chi M_k(\Gamma_0(N),\chi)$, $S_k$ likewise (characters of a finite abelian group, Chapter 4). Remark (forward
pointer): the twist of $f\in S_k(\Gamma_0(M))$ by a primitive character $\chi$ of conductor $r$ has character $\chi^2$ and level dividing
$\operatorname{lcm}(M,r^2)$ (Chapter 13); for the quadratic characters of the paper $\chi^2=\mathbf 1$. Reference: DiamondShurman 4.3, 5.2 (cite the
sections); Shimura71 3.6 (cite the section). Paper: the optimal-level theorem of Section 3 ("nebentypus of order prime
to $\ell$"; "$\det\bar\sigma=\bar\chi_\ell$ forces the nebentypus ... to be trivial", Chapter 15), Lemma lem:twist(iii) and Theorem
thm:twist (characters of twists, Chapter 13), Remark rem:free ($J_1(N)$).

### Section 7. Level one: Eisenstein series, $\Delta$, $j$ and the valence formula

**7.1 `prop:modforms:eisenstein-level-one`** (proposition; P for $k\ge4$, S for $E_2$). For even $k\ge4$,
$G_k(z)=\sum_{(m,n)\ne(0,0)}(mz+n)^{-k}=2\zeta(k)E_k(z)$ with
$$E_k(z)=1-\frac{2k}{B_k}\sum_{n\ge1}\sigma_{k-1}(n)q^n\in M_k(\SL_2(\Z)),\qquad E_4=1+240\sum\sigma_3(n)q^n,\quad E_6=1-504\sum\sigma_5(n)q^n.$$
Proof: absolute convergence for $k>2$; $G_k|_k\gamma=G_k$ by reindexing the lattice; the $q$-expansion from the Lipschitz formula
$\sum_{n\in\Z}(z+n)^{-k}=\frac{(-2\pi i)^k}{(k-1)!}\sum_{m\ge1}m^{k-1}q^m$, obtained by differentiating $\pi\cot\pi z=\frac1z+\sum_{n\ne0}(\frac1{z+n}-\frac1n)$ (the
partial-fraction expansion of RHB, or Poisson summation). $G_k(z)=G_k(\Lambda_z)$ is Chapter 9's lattice sum (its 7.1). $E_2=1-24\sum\sigma(n)q^n$
converges but is not modular: $E_2(-1/z)=z^2E_2(z)+\frac{6z}{\pi i}$ (S, or R: DiamondShurman 1.2), equivalently $E_2(z)-\frac3{\pi y}$ is
invariant of weight $2$. Reference: SerreCourse VII.2.3 and VII.4.2; DiamondShurman 1.1, 1.2. Paper: background (the
Eisenstein case of Section sec:eis and Conjecture conj:eis via 8.4; Chapter 14).

**7.2 `prop:modforms:delta-j`** (proposition; P for (i), (ii), S for (iii)). (i) $\Delta=(E_4^3-E_6^2)/1728\in S_{12}(\SL_2(\Z))$, nonzero,
$\Delta=\sum\tau(n)q^n=q-24q^2+252q^3-1472q^4+4830q^5-\cdots$ with $\tau(n)\in\Z$; in Chapter 9's notation $\Delta(\Lambda_z)=(2\pi)^{12}\Delta(z)$.
(ii) $j=E_4^3/\Delta=1728E_4^3/(E_4^3-E_6^2)$ is holomorphic on $\mathfrak H$ ($\Delta$ has no zero on $\mathfrak H$, 7.4(ii), which uses only 7.3), $\SL_2(\Z)$-invariant, with
$j(z)=q^{-1}+744+196884q+21493760q^2+864299970q^3+\cdots$, all coefficients integers; $j(z)=j(\Lambda_z)$ of Chapter 9 (its 7.1,
7.5(ii)); $j(i)=1728$, $j(\rho)=0$. (iii) (Jacobi.) $\Delta=q\prod_{n\ge1}(1-q^n)^{24}=\eta^{24}$ (S via 9.1 and $\dim S_{12}=1$). Reference:
SerreCourse VII.3.4 and VII.4.4; DiamondShurman 1.1. Paper: background (Chapter 9's $j$, $\Delta$; Definition def:terms
uses $v_q(j_E)$, which is Chapter 9's algebraic $j$, equal to this $j$ at the lattice of $E$).

**7.3 `thm:modforms:valence-level-one`** (theorem, the valence formula; P). Let $f\ne0$ be meromorphic on $\mathfrak H$, with $f|_k\gamma=f$ for
$\gamma\in\SL_2(\Z)$, and meromorphic at $\infty$ ($f=\sum_{n\ge n_0}a_nq^n$). Then
$$v_\infty(f)+\tfrac12v_i(f)+\tfrac13v_\rho(f)+\sum_{p\in\SL_2(\Z)\backslash\mathfrak H,\ p\ne i,\rho}v_p(f)=\frac k{12},$$
where $v_p$ is the order at any representative and $v_\infty$ the order in $q$. Proof: integrate $\frac1{2\pi i}f'/f$ around the boundary of
$\mathcal F$ truncated at height $Y$ and indented by small arcs at $i$, $\rho$, $-\bar\rho$ (assume no other zeros on the boundary, else
indent there too): the top segment gives $-v_\infty$; the vertical sides cancel ($T$); the two halves of the arc are related by
$S$, and $\frac{f'}{f}(Sz)\,d(Sz)=\frac{f'}{f}(z)\,dz+k\frac{dz}z$ gives $\frac k{12}$; the indentations give $-\frac12v_i$ and $-\frac13v_\rho$ (angles $\pi$ and
$\pi/3+\pi/3$). Physics aside: the argument principle counts the "charge" inside a contour (RHB, residue theorem), and the
symmetries cancel the sides. Reference: SerreCourse VII.3 (Theorem 3; verify); DiamondShurman 3.1 (exercises). Paper:
background (7.4, 7.5; the Sturm bound 11.3).

**7.4 `cor:modforms:level-one-structure`** (corollary; P). (i) $M_k(\SL_2(\Z))=0$ for $k<0$, $k$ odd, and $k=2$; $M_0=\C$; $M_k=\C E_k$ for
$k=4,6,8,10,14$. (ii) $\Delta$ has no zero on $\mathfrak H$ and a simple zero at $\infty$; $E_4$ vanishes only at $\rho$ (simply) and $E_6$ only at $i$
(simply). (iii) Multiplication by $\Delta$ is an isomorphism $M_{k-12}\to S_k$, and $\dim M_k=\lfloor k/12\rfloor$ if $k\equiv2\pmod{12}$, $\lfloor k/12\rfloor+1$
otherwise ($k\ge0$ even). (iv) $M_*=\bigoplus_kM_k=\C[E_4,E_6]$, $E_4$, $E_6$ algebraically independent. (Dimensions verified against
PARI for $k\le26$.) Reference: SerreCourse VII.3.2 (Theorem 4; verify); DiamondShurman 3.5, 3.6. Paper: background.

**7.5 `thm:modforms:j-bijective`** (theorem; P). $j\colon\SL_2(\Z)\backslash\mathfrak H\to\C$ is a bijection, and it extends to an isomorphism of
Riemann surfaces $X(1)\to\mathbb P^1(\C)$ with $j(\infty)=\infty$. Proof: for $\lambda\in\C$, $f_\lambda=E_4^3-\lambda\Delta\in M_{12}$ has $v_\infty(f_\lambda)=0$, so by
7.3 $n+\frac a2+\frac b3=1$ with $n,a,b\ge0$ integers, whose only solutions are $(1,0,0)$, $(0,2,0)$, $(0,0,3)$: exactly one point of
$\SL_2(\Z)\backslash\mathfrak H$ has $j=\lambda$. Holomorphy and injectivity on $X(1)$ make $j$ a degree-one holomorphic map, hence an
isomorphism (Chapter 8, 8.2). Consequence (completing Chapter 9, its 7.3(ii) and 7.5(iii), with no circularity: nothing
here uses the uniformisation theorem): for every $j_0\in\C$ there is a lattice $\Lambda$ with $j(\Lambda)=j_0$, so every elliptic curve over $\C$ is
$\C/\Lambda$ (with Chapter 9, its 1.4 and 7.4). Reference: SerreCourse VII.3.3 (Proposition 5; verify); DiamondShurman 1.4 and
2.3. Paper: background (Chapter 9's deferral; the period lattice $\Lambda_E$ in Section 1).

### Section 8. $\Gamma_0(N)$: valence, dimensions, weight-two forms as differentials, weight-two Eisenstein series

**8.1 `thm:modforms:valence-gamma0`** (theorem; S). Let $f\in M_k(\Gamma_0(N))$, $f\ne0$. For $P\in X_0(N)$ let $v_P(f)$ be the order of $f$ at a
representative $z\in\mathfrak H$ (in the variable $z$) if $P\in Y_0(N)$, and the order in $q_h$ of the expansion at the cusp if $P$ is a cusp,
and $e_P\in\{1,2,3\}$ the order of the stabiliser of $z$ in the image $\bar\Gamma_0(N)$ of $\Gamma_0(N)$ in $\mathrm{PSL}_2(\Z)$ (and $e_P=1$
at cusps). Then
$$\sum_{P\in X_0(N)}\frac{v_P(f)}{e_P}=\frac{k\,\mu(N)}{12}.$$
In particular $v_\infty(f)\le k\mu(N)/12$, so $f$ is determined by $a_0(f),\dots,a_{B_k(N)}(f)$. Sketch: apply 7.3 to the norm
$F=\prod_{i=1}^{\mu}f|_k\gamma_i\in M_{k\mu}(\SL_2(\Z))$ (independent of the choice of coset representatives) and compare orders point by point
over $X(1)$ using the ramification of 5.3; or, for $k=2$, use 8.2 and $\deg\operatorname{div}(\omega)=2g-2$ (Chapter 8, its 5.3(b)) with the
corrections at cusps and elliptic points. Example: $f_{11}=\eta(z)^2\eta(11z)^2$ (9.2) has simple zeros at $\infty$ and at $0$ and none
elsewhere: $1+1=2\cdot12/12$. Reference: DiamondShurman 3.1 (exercises), Stein (book) Chapter 9 (cite the chapter); Shimura71
2.4. Paper: background (11.3, 6.3(iv)).

**8.2 `thm:modforms:weight-two-differentials`** (theorem; P given Chapter 8, its 9.1 and 9.3). (i) $f\mapsto\omega_f=f(z)\,dz$ is an
isomorphism from $S_2(\Gamma_0(N))$ onto the space $H^0(X_0(N),\Omega^1)$ of holomorphic differentials on $X_0(N)$. (ii) $M_2(\Gamma_0(N))$ maps
isomorphically onto the meromorphic differentials that are holomorphic on $Y_0(N)$ and have at most simple poles at the
cusps, and $\operatorname{res}_s\omega_f=\frac{h_s}{2\pi i}a_0(f|_2\sigma_s)$ at the cusp $s=\sigma_s\infty$ of width $h_s$. (iii) Hence $\dim S_2(\Gamma_0(N))=g(X_0(N))$ (Chapter 8,
its 9.3), and $\sum_sh_s\,a_0(f|_2\sigma_s)=0$ for every $f\in M_2(\Gamma_0(N))$ (residue theorem, Chapter 8, its 9.2). Proof: $\Gamma_0(N)$-invariance of
$f\,dz$ is weight $2$ by 6.1(iii); at a cusp of width $h$, $dz=\frac{h}{2\pi i}\frac{dq_h}{q_h}$; at an elliptic point of order $e$ with local
coordinate $w$ on a disc and chart $t=w^e$, an invariant $F(w)\,dw$ has $F(\zeta w)\zeta=F(w)$ for $\zeta=e^{2\pi i/e}$, so $F(w)=w^{e-1}G(w^e)$ and
$F\,dw=\frac1eG(t)\,dt$ is holomorphic in $t$: no condition at elliptic points in weight $2$. Examples: $S_2(\SL_2(\Z))=0$ and $g(X(1))=0$;
$\dim S_2(\Gamma_0(11))=1$, $\dim S_2(\Gamma_0(121))=6$, $\dim S_2(\Gamma_0(539))=49$ (PARI agrees, Part 6.6). Reference: DiamondShurman 3.3
(cite the section); Shimura71 2.4. Paper: background ("$\dim S_2$ and multiplicity one"; Section 1: $\varphi_E^*\omega_E$ is a
multiple of $\omega_f$, Chapter 14; Section 4.1: $H^1(X_0(N),\C)=H^0(\Omega^1)\oplus\overline{H^0(\Omega^1)}=\omega_{S_2}\oplus\overline{\omega_{S_2}}$ by Chapter 8, its 10.2(iii)).

**8.3 `thm:modforms:dimension-formulas`** (theorem; P for $k=2$, R for $k\ge4$ with a sketch via Riemann-Roch). For $k\ge4$ even:
$$\dim S_k(\Gamma_0(N))=(k-1)(g-1)+\Bigl(\frac k2-1\Bigr)\nu_\infty+\Bigl\lfloor\frac k4\Bigr\rfloor\nu_2+\Bigl\lfloor\frac k3\Bigr\rfloor\nu_3,\qquad\dim M_k(\Gamma_0(N))=\dim S_k(\Gamma_0(N))+\nu_\infty;$$
for $k=2$: $\dim S_2=g$, $\dim M_2=g+\nu_\infty-1$; $M_0=\C$, $S_0=0$; $M_k=0$ for $k<0$ or $k$ odd. (Verified against PARI for all
$N\le60$ and $N\in\{77,99,121,539\}$, $k\in\{2,4,\dots,14\}$.) Sketch for $k\ge4$: $f\mapsto f\,(dz)^{k/2}$ identifies $M_k$ with the sections of a
line bundle of degree $\frac k2(2g-2)+\frac k2\nu_\infty+\lfloor\frac k4\rfloor\nu_2+\lfloor\frac k3\rfloor\nu_3$ (corrections at cusps and elliptic points), and
Riemann-Roch (Chapter 8, its 5.2, 5.3(c)) gives the dimension since the degree exceeds $2g-2$. Reference: DiamondShurman
Theorems 3.5.1 and 3.6.1 (verify the numbers; else cite Sections 3.5, 3.6); Shimura71 2.6. Paper: background.

**8.4 `prop:modforms:eisenstein-weight-two`** (proposition; P given 7.1). For $N>1$, $E_2^{(N)}(z):=E_2(z)-NE_2(Nz)$ lies in $M_2(\Gamma_0(N))$
(it equals $E_2^*(z)-(E_2^*|_2\begin{psmallmatrix}N&0\\0&1\end{psmallmatrix})(z)$ with $E_2^*=E_2-\frac3{\pi y}$ invariant), is not a cusp form ($a_0=1-N$), and
$E_2^{(N)}=(1-N)-24\sum_{n\ge1}(\sigma(n)-N\sigma(n/N))q^n$ ($\sigma(n/N)=0$ if $N\nmid n$). For $N=p$ prime, $M_2(\Gamma_0(p))=\C E_2^{(p)}\oplus S_2(\Gamma_0(p))$
($\dim M_2=g+1$ by 8.3). Worked example (P, given 11.3; verified for $n\le5000$): for $p=11$, the form
$-\frac1{24}E_2^{(11)}=\frac5{12}+\sum_{n\ge1}(\sigma(n)-11\sigma(n/11))q^n$ has $5$-integral coefficients and is congruent modulo $5$ to $f_{11}$ (9.2),
coefficientwise (apply 11.3 to $12(f_{11}+\frac1{24}E_2^{(11)})\in M_2(\Gamma_0(11);\Z)$), because the two agree modulo $5$ at $n=0,1,2$ ($\frac5{12}\equiv0$; $1=1$; $3\equiv-2$) and the Sturm bound $B_2(11)$ is $2$. Hence
$a_\ell(\text{11a1})\equiv1+\ell\pmod5$ for every prime $\ell\ne11$ (and $a_{11}=1$): the Eisenstein congruence behind the rational $5$-torsion
of 11a1 (Chapter 9, its 9.7). Reference: DiamondShurman 4.6 (cite the section); Mazur77 (Eisenstein ideal; Chapter 14).
Paper: Conjecture conj:eis and Section sec:eis (the Eisenstein case: reducible $\bar\rho$, congruence with an Eisenstein series;
Chapter 14 for the Eisenstein ideal), Open question 4.

### Section 9. The Dedekind $\eta$-function and the level-$11$ example

**9.1 `prop:modforms:eta`** (proposition; R for the transformation law, P for the rest). $\eta(z)=q^{1/24}\prod_{n\ge1}(1-q^n)$ (with
$q^{1/24}=e^{2\pi iz/24}$) is holomorphic and nonvanishing on $\mathfrak H$, $\eta(z+1)=e^{\pi i/12}\eta(z)$ and $\eta(-1/z)=\sqrt{z/i}\,\eta(z)$ (principal
branch). Consequences: $\eta^{24}\in S_{12}(\SL_2(\Z))$, hence $\eta^{24}=\Delta$ (7.4(iii)); $\frac{\eta'}{\eta}=\frac{\pi i}{12}E_2$ (logarithmic derivative), which
is equivalent to the transformation law of $E_2$ in 7.1. Reference: Apostol, *Modular functions and Dirichlet series in
number theory*, Chapter 3 (add to `bib/ch12.bib`); Knapp, Chapter IX (cite the chapter); Koblitz III.2. Paper:
background.

**9.2 `thm:modforms:level-eleven`** (theorem and worked example; P for (i) to (iii), R for (iv)). Let
$f_{11}(z)=\eta(z)^2\eta(11z)^2=q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2$. (i) $f_{11}\in S_2(\Gamma_0(11))$ (from 9.1, checking $f_{11}|_2\gamma=f_{11}$ on generators,
or by the criterion of Ligozat for $\eta$-quotients, R: $\sum\delta r_\delta=24\equiv0$, $\sum(N/\delta)r_\delta=24\equiv0\pmod{24}$, $\prod\delta^{r_\delta}=11^2$ a
square); its orders at the cusps $\infty$ and $0$ are $1$ and $1$. (ii) $S_2(\Gamma_0(11))=\C f_{11}$ (dimension $g(X_0(11))=1$, 8.2), so
$f_{11}$ is the normalised generator ($a_1=1$). (iii) $f_{11}|_2W_{11}=-f_{11}$: from 9.1, $f_{11}(-1/(11z))=-11z^2f_{11}(z)$, so
$(f_{11}|_2W_{11})(z)=11(11z)^{-2}f_{11}(-1/(11z))=-f_{11}(z)$ (also checked numerically at three points, and $f_{11}(i/\sqrt{11})\approx0.1029>0$
pins the sign; PARI's `mfatkineigenvalues` gives $-1$). (iv) Its coefficients are those of 11a1:
$$f_{11}=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7-2q^9-2q^{10}+q^{11}-2q^{12}+4q^{13}+4q^{14}-q^{15}-4q^{16}-2q^{17}+4q^{18}+2q^{20}+\cdots,$$
$a_p$ for $p=2,3,5,7,11,13,17,19,23,29,31,37$: $-2,-1,1,-2,1,4,-2,0,-1,0,7,3$, equal to $p+1-\#\tilde E(\F_p)$ for
$E=$ 11a1: $y^2+y=x^3-x^2-10x-20$ (Chapter 9, its 8.7). Checked for all $n\le2000$; the same for 11a2 and 11a3 (isogenous). That
this holds for all $n$ is Eichler-Shimura for $X_0(11)$, which is itself the elliptic curve 11a1 (Chapter 14; R). Physics
aside, recalled from 6.3: $f_{11}$ is a Fourier series on the quotient. Further $\eta$-products (verified to $n=300$ against
Cremona's curves): $\eta(z)\eta(2z)\eta(7z)\eta(14z)$ (14a1), $\eta(z)\eta(3z)\eta(5z)\eta(15z)$ (15a1), $\eta(2z)^2\eta(10z)^2$ (20a1),
$\eta(2z)\eta(4z)\eta(6z)\eta(12z)$ (24a1), $\eta(3z)^2\eta(9z)^2$ (27a1), $\eta(4z)^2\eta(8z)^2$ (32a1), $\eta(6z)^4$ (36a1). Reference:
DiamondShurman 1.2, 3.9 (exercises) and 6.5 (cite the sections); Knapp, Chapter XI (verify); Ligozat (1975; add to
`bib/ch12.bib` if cited). Paper: the running example (Section 3 Example: "the form of 11a1"; Theorem thm:qual (a), (b) via
the congruences with $f_{11}$; 121d $=f_{\text{11a}}\otimes\chi_{-11}$), PLAN.md's example "$S_2(\Gamma_0(11))$ is one-dimensional spanned by
$\eta(z)^2\eta(11z)^2$".

**9.3 `ex:modforms:small-levels`** (example; P for dimensions, R for the identifications). For each $N$ with $g(X_0(N))=1$
($N=11,14,15,17,19,20,21,24,27,32,36,49$), $S_2(\Gamma_0(N))$ is spanned by the form of the strong Weil curve of conductor $N$
(Chapter 14). $\dim S_2(\Gamma_0(37))=2$: the two newforms of 37a1 and 37b1, with $W_{37}$-eigenvalues $+1$ and $-1$ (12.4(c)).
$\dim S_2(\Gamma_0(121))=6$ (four newforms, 121a to 121d, and the two oldforms $f_{11}(z)$, $f_{11}(11z)$; Chapter 13). Paper: the levels of
Section 3 (11, 20, 77, 121, 140, 539, 980) and the dimension counts behind Lemma lem:old (Chapter 13).

### Section 10. The Petersson inner product

**10.1 `def:modforms:petersson`** (definition and proposition; P). For $f\in S_k(\Gamma_0(N))$ and $g\in M_k(\Gamma_0(N))$,
$$\langle f,g\rangle=\langle f,g\rangle_{\Gamma_0(N)}=\int_{\Gamma_0(N)\backslash\mathfrak H}f(z)\overline{g(z)}\,y^k\,\frac{dx\,dy}{y^2},$$
the integral over any fundamental domain (3.2). (i) The integrand is $\Gamma_0(N)$-invariant (6.1(iv) and 1.1(v)), so the value does
not depend on the fundamental domain. (ii) It converges absolutely: on $\sigma_i\mathcal F$ near the cusp, $|(f|_k\sigma_i)(z)|\le Ce^{-2\pi y/h}$ and
$|g|_k\sigma_i|$ is bounded, against the finite measure $y^{k-2}dx\,dy$ times an exponential. (iii) On $S_k(\Gamma_0(N))$ it is a positive
definite Hermitian inner product (sesquilinear; $\langle f,f\rangle=\int|f|^2y^k\,d\mu>0$ for $f\ne0$). (iv) In weight $2$:
$\langle f,g\rangle=\frac i2\int_{X_0(N)}\omega_f\wedge\overline{\omega_g}=\iint f\bar g\,dx\,dy$ (Chapter 8, its 9.4(b)): the Petersson product is the Hodge inner
product of the holomorphic differentials of 8.2. Physics aside: a weighted $L^2$ inner product on a surface of finite
area, as in Sturm-Liouville theory. The `convention` box C5 (unnormalised; PARI divides by $\mu(N)$, others by
$\pi\mu(N)/3$). Reference: DiamondShurman 5.4 (cite the section); Shimura71 3.4; SerreCourse VII.5 (remark). Paper:
Section 1 ("the Petersson norm", "$\langle f,f\rangle$"), the definition of $r_E$ ("orthogonal to $f$"), Lemma lem:crit ($f^\perp$), Lemma
lem:old ("orthogonal to the newform $f$"), Theorem thm:twist ($g^\perp$; the paper there uses the $\T$-stable complement,
which Chapter 13 shows is the Petersson complement).

**10.2 `prop:modforms:petersson-change`** (proposition; P). (i) If $\Gamma'\subseteq\Gamma_0(N)$ has finite index then
$\langle f,g\rangle_{\Gamma'}=[\bar\Gamma_0(N):\bar\Gamma']\,\langle f,g\rangle_{\Gamma_0(N)}$ (bars: images in $\mathrm{PSL}_2(\Z)$); in particular $\langle f,g\rangle_{\Gamma_0(NM)}=\frac{\mu(NM)}{\mu(N)}\langle f,g\rangle_{\Gamma_0(N)}$
for $f,g$ of level $N$ viewed at level $NM$. This is why the normalisation matters when levels change (Chapter 13's oldforms,
the paper's $M^\Sigma$). (ii) If $\alpha\in\GL_2^+(\Q)$ normalises $\Gamma_0(N)$ (for instance $\alpha=W_d$, 12.1), then $\langle f|_k\alpha,g|_k\alpha\rangle=\langle f,g\rangle$ (change
of variables $z\mapsto\alpha z$ and 6.1(iv)). (iii) More generally, for $\alpha\in\GL_2^+(\Q)$, $\langle f|_k\alpha,g|_k\alpha\rangle_{\alpha^{-1}\Gamma\alpha}=\langle f,g\rangle_\Gamma$. Reference:
DiamondShurman 5.4, 5.5 (cite the sections). Paper: background (Section 4.1 changes level from $M$ to $M^\Sigma$; Theorem
thm:quant Step 1 works at level $N$ with forms of level $N_S$).

**10.3 `prop:modforms:orthogonal-complement`** (proposition; P, linear algebra). For $0\ne f\in S_k(\Gamma_0(N))$, $S_k(\Gamma_0(N))=\C f\oplus f^\perp$,
$f^\perp=\{g:\langle g,f\rangle=0\}$, and the projection onto $\C f$ along $f^\perp$ is $g\mapsto\frac{\langle g,f\rangle}{\langle f,f\rangle}f$. Forward pointer (Chapter 13): when $f$
is a newform with rational coefficients, $f^\perp$ is stable under all Hecke operators (including $U_p$, whose Petersson adjoint is
$w_NU_pw_N$, with $f$ an eigenvector of $w_N$), is spanned by forms with rational coefficients, and
$L=f^\perp\cap S_2(\Gamma_0(N);\Z)$ is a saturated sublattice of rank $\dim S_2-1$; none of this is proved here. Paper: Lemma lem:crit
("$J$ the annihilator in $\T$ of the orthogonal complement $f^\perp$", "projection onto $\Q f$ along $f^\perp$").

**10.4 `ex:modforms:petersson-numerics`** (worked example; P as a computation, verified with PARI). Unnormalised Petersson norms
of the normalised forms of five optimal curves, with the area of the period lattice (Chapter 9, its 7.6) and the modular
degree (from `ellmoddegree`; Chapter 14):

| curve | $N$ | $\mu(N)$ | $\langle f,f\rangle$ | $\operatorname{vol}(\Lambda_E)$ | $4\pi^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$ | $\deg\varphi_E$ |
|-|-|-|-|-|-|-|
| 11a1 | 11 | 12 | 0.0469001478734952 | 1.85154362345596 | 1.0000000 | 1 |
| 20a1 | 20 | 36 | 0.0813494568253817 | 3.21154782844007 | 1.0000000 | 1 |
| 37a1 | 37 | 38 | 0.3717541475106961 | 7.33813274078958 | 2.0000000 | 2 |
| 99a1 | 99 | 144 | 0.5385195687108607 | 5.31497510542145 | 4.0000000 | 4 |
| 121a1 | 121 | 132 | 0.4282393600119572 | 2.81770204819580 | 6.0000000 | 6 |

(PARI's `mfpetersson` returns $\langle f,f\rangle/\mu(N)$, for example $0.0039083456561246$ for 11a1.) So with C5,
$\deg\varphi_E=4\pi^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$ for these curves, whose Manin constant is $1$. The derivation is one line (Chapter 14 does it):
if $\varphi_E^*\omega_E=c\cdot2\pi i\,f(z)\,dz$ then $\deg\varphi_E\cdot\frac i2\int_E\omega_E\wedge\bar\omega_E=\frac i2\int_{X_0(N)}\varphi_E^*\omega_E\wedge\overline{\varphi_E^*\omega_E}$, that is,
$\deg\varphi_E\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c^2\langle f,f\rangle$ (Chapter 8, its 9.4(b), 11.5(i)). Note where $c^2$ stands (Part 7, B1). Paper: Section 1
("$\deg\varphi_E$ is $\langle f,f\rangle$ divided by the area of the period lattice of $E$", Zagier85, Watkins02, Cremona97); the exact formula
with the Manin constant is Chapter 14's.

**10.5 `rem:modforms:petersson-forward`** (remark; R, forward pointers only). (a) (Chapter 13.) For $(n,N)=1$ the Hecke operator
$T_n$ is self-adjoint for $\langle\ ,\ \rangle$; $U_p$ ($p\mid N$) is not, its adjoint being $w_NU_pw_N$; newforms of different eigensystems are
orthogonal, and oldforms are orthogonal to newforms. (b) (Chapters 13 and 19.) Rankin-Selberg: for a newform $f$ of weight $2$
and level $N$, $\langle f,f\rangle$ is an explicit elementary factor times $L(\operatorname{Sym}^2f,2)$ times correction factors at the primes dividing
$N$ (DFG04 Lemma 2.12, Shimura76); Chapter 19 states the exact formula. The Rankin series $\sum a_n(f)^2n^{-s}$ is **not** the
naive adjoint (symmetric square) $L$-function: at a good prime it carries an extra factor $1+p^{1-s}$, globally
$\sum a_n^2n^{-s}=\zeta^{(N)}(s-1)L^{\mathrm{nv}}(\operatorname{Sym}^2f,s)/\zeta^{(N)}(2s-2)$ up to bad factors (important_notes.md point 30). (c) (Chapter 14.) The
Zagier-Watkins formula with the Manin constant (10.4). Paper: Section 1 (Petersson norm, Rankin, Shimura, Flach,
"the Euler product of $\sum a_n(f)^2n^{-s}$", point 30).

### Section 11. Integral forms, the Sturm bound and congruences

**11.1 `def:modforms:integral-forms`** (definition; P for the remarks). For a subring $A\subseteq\C$:
$M_k(\Gamma_0(N);A)=\{f\in M_k(\Gamma_0(N)):a_n(f)\in A\ \forall n\ge0\}$ and $S_k(\Gamma_0(N);A)$ likewise (an $A$-module); for $A=\Z$ these are the
paper's "integral cusp forms" and $S_2(\Gamma_0(N);\Z)$. For any commutative ring $B$: $S_k(\Gamma_0(N);B):=S_k(\Gamma_0(N);\Z)\otimes_\Z B$, with the
$q$-expansion map $S_k(\Gamma_0(N);B)\to B[[q]]$, $f\otimes b\mapsto b\sum a_n(f)q^n$ (C6); for $B=\Z_\ell$ this is the paper's $S_2(\Gamma_0(N);\Z_\ell)$. Remarks:
(a) $S_k(\Gamma_0(N);\Z)$ is saturated in $\Z[[q]]$ by definition: if $mg\in S_k(\Gamma_0(N);\Z)$ with $g\in\Z[[q]]$ then $g\in S_k(\Gamma_0(N);\Z)$;
(b) the definition uses the expansion at $\infty$ only (integrality at other cusps is a different and subtler matter, not
needed); (c) twisting by a quadratic character preserves integrality (Theorem thm:twist; Chapter 13). Reference:
DiamondShurman 6.5 (cite the section); Shimura71 3.5. Paper: Section 1 ("integral cusp form $g$ of level $N$"), Lemma lem:crit
($S_2(\Gamma_0(N);\Z)$; "with $\Z$ replaced by $\Z_\ell$"), Theorem thm:twist ("preserves integrality"), Theorem thm:quant Step 1
($S_2(\Gamma_0(N);\Z_\ell)$).

**11.2 `thm:modforms:integral-basis`** (theorem; R). $S_k(\Gamma_0(N))$ has a $\C$-basis consisting of forms with integer
coefficients; equivalently the natural map $S_k(\Gamma_0(N);\Z)\otimes_\Z\C\to S_k(\Gamma_0(N))$ is an isomorphism. The same holds for $M_k(\Gamma_0(N))$
with $\Q$ (and, after scaling, $\Z$). Proofs: via the rationality of the Hecke eigenvalues and the Galois action on newforms
(Shimura), via the algebraic theory of modular forms (the $q$-expansion principle of Deligne-Rapoport and Katz), or for
$k=2$ via $H^1(X_0(N),\Z)$ and Eichler-Shimura (Chapter 14). Reference: Shimura71 Theorem 3.52 (verify the number);
DiamondShurman 6.5 (cite the section). Paper: Lemma lem:crit (that $S_2(\Gamma_0(N);\Z)$ has rank $\dim S_2$ is used when the perfect
pairing with $\T$ is applied, Chapter 13).

**11.3 `thm:modforms:sturm`** (theorem, Sturm's bound; S). Let $\mathcal O$ be the ring of integers of a number field, $\lambda$ a prime of $\mathcal O$,
and $f\in M_k(\Gamma_0(N);\mathcal O)$. If $a_n(f)\in\lambda$ for all $n\le k\mu(N)/12$, then $a_n(f)\in\lambda$ for all $n$. For $k=2$ the condition is on
$n\le B_2(N)=\lfloor\mu(N)/6\rfloor$. Values (agreeing with PARI's `mfsturm`): $B_2(11)=2$, $B_2(20)=6$, $B_2(37)=6$, $B_2(99)=24$, $B_2(121)=22$,
$B_2(539)=112$, $B_2(980)=336$, $B_2(1089)=264$, $B_2(4851)=1344$. Sketch: replace $f$ by the norm $\prod_if|_k\gamma_i$ suitably normalised, which
has coefficients integral at $\lambda$ (Chapter 6's integrality of algebraic integers, after adjoining $\mu_N$) and lies in
$M_{k\mu}(\SL_2(\Z))$; for level one, write it in the $\mathcal O$-basis $E_4^aE_6^b\Delta^c$ triangular in $q$ and use the mod $\lambda$ form of 7.3
(a nonzero mod-$\lambda$ form of weight $K$ and level one has $v_\infty\le K/12$). The characteristic-zero statement is 8.1. Reference:
Sturm, *On the congruence of modular forms*, Lecture Notes in Math. 1240 (1987), 275-280 (add to `bib/ch12.bib`); Stein
(book), Chapter 9 (cite the chapter; the theorem number to be verified). Paper: Section 1 and Lemma lem:crit
(coefficientwise congruences "for every $n$" are decidable), the Example of Section 3 (11.5).

**11.4 `cor:modforms:integral-lattice`** (corollary; P given 11.2, 11.3). Let $d=\dim S_2(\Gamma_0(N))$ and $B=B_2(N)$. (i)
$S_2(\Gamma_0(N);\Z)$ is free of rank $d$ and $S_2(\Gamma_0(N);\Z)\otimes\C=S_2(\Gamma_0(N))$. (ii) The truncation $\tau_B\colon S_2(\Gamma_0(N);\Z)\to\Z^B$,
$f\mapsto(a_1,\dots,a_B)$, is injective (8.1) with torsion-free cokernel: if $\tau_B(g)\in m\Z^B$ then, applying 11.3 for each prime
$p\mid m$ to $g$, $g/p$, ..., $g/m\in S_2(\Gamma_0(N);\Z)$. So $\tau_B$ is a split injection of free $\Z$-modules (Chapter 3, saturation). (iii)
Hence for every commutative ring $B'$ the $q$-expansion map $S_2(\Gamma_0(N);B')\to B'[[q]]$ is injective, and so is its truncation at
$B$; for $B'=\Z_\ell$ the image is $(S_2(\Gamma_0(N);\Q)\otimes\Q_\ell)\cap\Z_\ell[[q]]$, and for $B'=\F_\ell$ a form is zero iff its first $B$ coefficients are.
(iv) For $f,g\in S_2(\Gamma_0(N);\mathcal O)$ and an ideal $\mathfrak a\subseteq\mathcal O$, $f\equiv g\pmod{\mathfrak a}$ coefficientwise iff $a_n(f)\equiv a_n(g)\pmod{\mathfrak a}$ for
$n\le B$ (11.3 applied prime by prime to the powers of the primes of $\mathcal O$ dividing $\mathfrak a$, as in (ii)). (v) Forms of different
levels $M_1,M_2\mid N$ are compared in $S_2(\Gamma_0(N))$ with $N=\operatorname{lcm}(M_1,M_2)$ (6.2(c)); a congruence "at all $p\notin\Sigma$" must
first be turned into one "at all $n$" (depletion, Chapter 13), which raises the level and the bound. Reference: as for 11.2,
11.3. Paper: Lemma lem:crit ("every step holds verbatim over $\Z_\ell$, the pairing being perfect after tensoring with $\Z_\ell$": (iii)
gives the $q$-expansion side), Theorem thm:quant Step 1 ("projecting $h$ to the $\mathfrak m$-component ... the congruence survives": a
statement about $S_2(\Gamma_0(N);\Z_\ell)$ and its $q$-expansions), Lemma lem:old (the passage from $a_p$ to $a_n$ is Chapter 13's
recursion, not Sturm).

**11.5 `ex:modforms:paper-congruences`** (worked example; P given 11.3 and the levels of the twists from Chapter 13).
The three congruences of the Example of Section 3 hold **for every $n$** and are theorems by 11.4(iv) (Part 7, point P1):
(a) $f_{\text{121a}}\equiv f_{\text{11a}}\otimes\chi_{-11}=f_{\text{121d}}\pmod3$: both in $S_2(\Gamma_0(121);\Z)$, $B_2(121)=22$; the coefficients agree mod $3$
for $n\le22$ (also at $p=3$: $a_3=2$ and $-1$; at $p=11$: both $0$). (b) $f_{\text{539c}}\equiv f_{\text{11a}}\otimes\chi_{-7}=f_{\text{539d}}\pmod3$: both of level
$539$, $B_2(539)=112$ ($a_3=-2$ and $1$; $a_7=0$, $0$; $a_{11}=1$, $1$). (c) $f_{\text{980i}}\equiv f_{\text{20a}}\otimes\chi_{-7}\pmod5$: both of level $980$,
$B_2(980)=336$ ($a_2=0,0$; $a_5=1,1$; $a_7=0,0$). Each verified for all $n\le20000$ (and $n\le3000$ for (a)). The paper's checks
"for $p<500$" and "for $p<1000$" therefore already prove these congruences once the excluded $a_p$ are added, since the $a_n$
for $n\le B$ are determined by the $a_p$, $p\le B$, through the Hecke recursion (Chapter 13). Also (8.4): $f_{11}$ is congruent mod $5$ to
an Eisenstein series, $B_2(11)=2$. Paper: the Example of Section 3, Theorem thm:qual (b), (c) (illustrations), Conjecture
conj:eis.

### Section 12. The Atkin-Lehner involutions

**12.1 `def:modforms:atkin-lehner`** (definition and proposition; P). Let $d\,\|\,N$ (C4). Integers $x,y,z,w$ with
$d^2xw-Nyz=d$ exist (divide by $d$: solve $dxw-(N/d)yz=1$, possible since $\gcd(d,N/d)=1$), and
$W_d=\begin{psmallmatrix}dx&y\\Nz&dw\end{psmallmatrix}$, $\det W_d=d$. (i) $W_d$ normalises $\Gamma_0(N)$. (ii) $W_d^2\in d\cdot\Gamma_0(N)$ (explicitly
$W_d^2=d\begin{psmallmatrix}dx^2+(N/d)yz&(x+w)y\\Nz(x+w)&(N/d)yz+dw^2\end{psmallmatrix}$). (iii) Two choices of $W_d$ differ by left multiplication by an element of
$\Gamma_0(N)$. (iv) For $d,d'\,\|\,N$, $W_dW_{d'}\in W_{dd'/\gcd(d,d')^2}\cdot\Gamma_0(N)$ up to a positive scalar; the $W_d$ commute modulo $\Gamma_0(N)$ and scalars.
Consequently (v) $z\mapsto W_dz$ induces a holomorphic involution $w_d$ of $X_0(N)$, and the $w_d$ generate a group of automorphisms of $X_0(N)$ that is a quotient of $(\Z/2)^{\omega(N)}$ (isomorphic to it
when $N$ is squarefree, by 12.3(ii));
$W_N=\begin{psmallmatrix}0&-1\\N&0\end{psmallmatrix}$ ($x=w=0$, $y=-1$, $z=1$) gives $w_N\colon z\mapsto-1/(Nz)$; in moduli terms $w_N(E,C)=(E/C,E[N]/C)$ (5.4(iii);
P: scale $\Lambda_{N\tau}$). (vi) $f\mapsto f|_kW_d$ is a well-defined involution of $M_k(\Gamma_0(N))$ and of $S_k(\Gamma_0(N))$ for even $k$ ((ii), (iii), C3), the
operators commute, and $w_N=\prod_{p^e\|N}w_{p^e}$. (vii) In weight $2$: $w_d^*(\omega_f)=\omega_{f|_2W_d}$ (6.1(iii)). Reference: AtkinLehner70
(Section 2; cite the section); DiamondShurman 5.5 (and its exercises; cite the section); Miyake 4.6 (cite the section). Paper: Section
4.1 ("$w=\begin{psmallmatrix}0&-1\\M^\Sigma&0\end{psmallmatrix}$ ... the Atkin-Lehner involution $w_{M^\Sigma}$"), Lemma lem:hecke and Theorem thm:quant Step 2
(through $\hat\delta_!$, Chapter 14).

**12.2 `prop:modforms:atkin-lehner-petersson`** (proposition; P). (i) For even $k$ and $f,g\in S_k(\Gamma_0(N))$:
$\langle f|_kW_d,g|_kW_d\rangle=\langle f,g\rangle$ (10.2(ii)) and $\langle f|_kW_d,g\rangle=\langle f,g|_kW_d\rangle$ (apply the first to $g|_kW_d$ and use $W_d^2\in d\Gamma_0(N)$). So $w_d$ is a
self-adjoint isometric involution, $S_k(\Gamma_0(N))=S_k^+\oplus S_k^-$ orthogonally into its $\pm1$-eigenspaces, and the $w_d$ are
simultaneously diagonalisable. (ii) For $k=2$: $\dim S_2(\Gamma_0(N))^{+}$ (for $w_N$) equals the genus of $X_0(N)/w_N$ (a $w_N$-invariant
holomorphic differential descends holomorphically, by the local computation of 8.2 with $e=2$; P given Chapter 8). Check
(class numbers for the number of fixed points of $w_N$, R; Riemann-Hurwitz, Chapter 8): $N=11$: $4$ fixed points ($h(-44)+h(-11)=3+1$),
$X_0(11)/w_{11}$ of genus $0$, $S_2^+=0$; $N=23$: $6$ fixed points, genus $0$; $N=37$: $2$ fixed points ($h(-148)=2$), genus $1$, $\dim S_2^+=1$;
$N=43$: $4$, genus $1$ (PARI's Atkin-Lehner matrices agree). (iii) (The input to important_notes.md point 39(d).) $w_N$ is an
involutive automorphism of the compact Riemann surface $X_0(N)$, so $w_N^*$ is an isometry of the cup product on $H^1(X_0(N),\Z)$
with $(w_N^*)^2=1$ (Chapter 8, its 12.3(a)); if $f|_2W_N=\varepsilon f$ ($\varepsilon=\pm1$) then $w_N^*$ acts by $\varepsilon$ on $\omega_f$, on $\overline{\omega_f}$, and hence on the
real $2$-plane of $H^1(X_0(N),\R)$ spanned by $\operatorname{Re}\omega_f$, $\operatorname{Im}\omega_f$ (Chapter 8, its 10.2(iii)). Reference: DiamondShurman 5.5;
AtkinLehner70. Paper: Section 4.1 ($\hat\delta_!$ "perfect and alternating"; Chapter 8, its 12.3(e), Chapter 14), Lemma lem:hecke
(important_notes.md points 36 and 39).

**12.3 `prop:modforms:atkin-lehner-cusps`** (proposition; P). (i) $w_N$ exchanges $\infty$ and $0$, and maps the cusps of denominator
$c$ (that is, $a/c$ with $c\mid N$, 4.2) to the cusps of denominator $N/c$: $W_N(a/c)=-1/((N/c)a)$, and $\gcd((N/c)a,N)=N/c$. (ii) For $N$
squarefree, $w_e$ ($e\mid N$) maps the cusp $1/c$ to the cusp $1/(ce/\gcd(c,e)^2)$; so the group of the $w_e$ acts simply transitively on
the $2^{\omega(N)}$ cusps. (Verified for $N=6,30,77$ with explicit $W_e$.) (iii) In general $w_d$ permutes the cusps; Exercise 17 works out
$X_0(20)$ ($w_4$, $w_5$, $w_{20}$ on its six cusps). Reference: DiamondShurman 3.8 and 5.5 (exercises; cite the sections);
Ogg (1973). Paper: background (the cusps $\infty$ and $0$ of $X_0(N)$; Chapter 14's cuspidal subgroup, Conjecture conj:eis).

**12.4 `ex:modforms:atkin-lehner-q-expansions`** (examples; P for (a), (b), R for (c)). The action on $q$-expansions is not simple.
(a) $f|_kW_N$ is, up to the factor $N^{k/2}(Nz)^{-k}$, the expansion of $f$ at the cusp $0$; it is not given coefficient by coefficient by
the $a_n(f)$ (there is no formula $a_n(f|W_N)=F(a_m(f))$ valid on all of $M_k$); it is determined globally, through the
transformation law. (b) (Illustration with oldforms, which are Chapter 13's.) For $h\in M_k(\Gamma_0(M))$ and $N=Mp$, $p\nmid M$:
$W_N=W_M\begin{psmallmatrix}p&0\\0&1\end{psmallmatrix}$ and $\begin{psmallmatrix}p&0\\0&1\end{psmallmatrix}W_N=W_M\cdot pI$, so
$$(h|_kW_N)(z)=p^{k/2}(h|_kW_M)(pz),\qquad\bigl(h(pz)\bigr)|_kW_N=p^{-k/2}(h|_kW_M)(z):$$
$w_N$ exchanges the lines of $h(z)$ and $h(pz)$ (when $h$ is a $w_M$-eigenform) and is not diagonal in the basis of $q$-expansions.
Example: on $\operatorname{span}\{f_{11}(z),f_{11}(2z)\}\subset S_2(\Gamma_0(22))$, $w_{22}$ has matrix $\begin{psmallmatrix}0&-1/2\\-2&0\end{psmallmatrix}$ (from $f_{11}|W_{11}=-f_{11}$, $k=2$, $p=2$). (c)
(Chapters 13 and 19.) A newform $f\in S_k(\Gamma_0(N))$ is an eigenvector of every $w_d$ with eigenvalue $\varepsilon_d(f)=\pm1$; for $k=2$ and
$p\,\|\,N$, $a_p(f)=-\varepsilon_p(f)$ (Atkin-Lehner, Theorem 3, verify the part); and the sign of the functional equation of $L(f,s)$ is
$-\varepsilon_N(f)$ for $k=2$. Checks: 11a1: $\varepsilon_{11}=-1$ (9.2(iii)), $a_{11}=1$, root number $+1$; 37a1: $\varepsilon_{37}=+1$, root number $-1$ (rank $1$).
Paper: Section 4.1 (the sign by which $w_N$ acts on $M_{f,\lambda}$, important_notes.md point 39), Lemma lem:crit ($f$ is an eigenvector
of $w_N$, needed for $f^\perp$ to be $U_p$-stable, Chapter 13), Lemma lem:euler and Lemma lem:old ($a_p=\pm1$ at multiplicative primes,
Chapters 13 and 15).

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2 with its tag and `\Cref`; conventions C3, C5 restated in one line each | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1 ($S_2(\Gamma_0(N))$, $f$, $r_E$, Petersson norm, $X_0(N)$); Section 3 preamble and Lemma lem:crit (integral forms, coefficientwise congruences, $f^\perp$, over $\Z_\ell$); Lemma lem:old (forms $h(dz)$, orthogonality); the Example of Section 3 (congruences, Sturm); the optimal-level theorem (nebentypus); Section 4.1 ($W_{M^\Sigma}$, $H^1(X_0(M^\Sigma))$); Theorems thm:twist and thm:quant Step 1 (integrality, $S_2(\Gamma_0(N);\Z_\ell)$); Conjecture conj:eis (Eisenstein congruence) | 40 |
| 1 | The upper half plane | opening paragraph (what the chapter is for, the three physics connections); conventions C1 to C9 as `convention` environments; 1.1, 1.2 | 90 |
| 2 | The modular group and its fundamental domain | 2.1, 2.2 with a figure of $\mathcal F$ (TikZ or described in words) and the gluing; `paperlink` to Chapter 9's moduli statement | 130 |
| 3 | Congruence subgroups | 3.1, 3.2; the table of $\mu(N)$ for the paper's levels; the fundamental domain of $\Gamma_0(11)$ described | 110 |
| 4 | Cusps, widths and elliptic points | 4.1 to 4.3; worked cusp lists for $N=11,20,99,121$ with widths; `warning`: irregular cusps for $\Gamma_1(4)$ | 140 |
| 5 | Modular curves as compact Riemann surfaces | 5.1 to 5.4; the genus table; `paperlink`: Section 1 ($\varphi_E\colon X_0(N)\to E$; $X_0(11)$ has genus $1$ and is 11a1, Chapter 14); the moduli dictionary, with $w_N(E,C)=(E/C,E[N]/C)$ | 200 |
| 6 | Modular forms, $q$-expansions, nebentypus | 6.1 to 6.6; physics aside (Fourier series on the half-cylinder); `paperlink`: "coefficientwise" means 6.3(i); the optimal-level theorem's nebentypus | 170 |
| 7 | Level one: Eisenstein series, $\Delta$, $j$, valence | 7.1 to 7.5; the contour picture for 7.3 described; physics aside (argument principle); `paperlink`: Chapter 9's deferrals discharged | 190 |
| 8 | $\Gamma_0(N)$: valence, dimensions, differentials | 8.1 to 8.4; the Eisenstein congruence for 11a1 mod 5 in full; `paperlink`: Section sec:eis and Conjecture conj:eis | 160 |
| 9 | $\eta$ and the level-$11$ example | 9.1 to 9.3; the first twenty coefficients of $f_{11}$ against $a_p$(11a1); the table of genus-one $\eta$-products | 110 |
| 10 | The Petersson inner product | 10.1 to 10.5; physics aside ($L^2$); the numerical table of 10.4; `warning` on normalisations (C5, PARI); `paperlink`: Section 1 (Zagier, Watkins), point 30 | 140 |
| 11 | Integral forms, Sturm, congruences | 11.1 to 11.5; `paperlink`s: Lemma lem:crit over $\Z_\ell$, Theorem thm:quant Step 1, the Example of Section 3 proved for all $n$ | 160 |
| 12 | The Atkin-Lehner involutions | 12.1 to 12.4; `paperlink`: Section 4.1 (the paper's $w$ is $W_{M^\Sigma}$; what Chapter 14 adds: $T^t=w_NTw_N$, $\hat\delta_!$; important_notes.md points 36, 39, 41) | 160 |
| 13 | Exercises | the 18 exercises of Part 4.2 | 130 |
| 14 | Notes and references | DiamondShurman, Shimura71, SerreCourse VII, Miyake, Koblitz, Knapp, Apostol, Stein (book), Sturm 1987, Ligozat, Ogg, Deligne-Rapoport, Katz-Mazur, AtkinLehner70, Zagier85, Watkins02, Cremona97, PARI; which numbers were cited and which are marked (verify) | 40 |
| | **total** | | **1,970** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| the upper half plane and the action of $\SL_2(\R)$ and of $\SL_2(\Z)$ | 1.1, 1.2, 2.1 |
| the modular group | 2.1(iv), 2.2 |
| fundamental domains | 2.1, 2.2, 3.2 |
| the congruence subgroups $\Gamma_0(N)$, $\Gamma_1(N)$, $\Gamma(N)$ and their indices | 3.1 |
| cusps and their widths | 1.2, 4.1, 4.2, 12.3 |
| elliptic points | 1.2, 2.1(iii), 2.2, 4.3 |
| the modular curves $Y_0(N)$, $X_0(N)$ as Riemann surfaces (compactification by cusps) | 5.1, 5.2 |
| the genus formula for $X_0(N)$; tables of small genera; $X_0(11)$ has genus $1$ | 5.3 (and 8.1 for the zero count of $f_{11}$) |
| modular forms and cusp forms of weight $k$ for $\Gamma_0(N)$; holomorphy at the cusps via $q$-expansions | 6.1, 6.2, 6.3 |
| the spaces $M_k(\Gamma_0(N))$ and $S_k(\Gamma_0(N))$ | 6.2, 8.3 |
| $q$-expansions and the $q$-expansion principle | 6.3, 8.1, 11.4 (and 11.2 for the algebraic form, R) |
| Eisenstein series (brief) | 7.1, 8.4 |
| the valence formula | 7.3, 8.1 |
| dimension formulas; $\dim S_2(\Gamma_0(N))=$ genus of $X_0(N)$ | 7.4, 8.2(iii), 8.3 |
| weight-2 cusp forms as holomorphic differentials $f(z)\,dz$ | 6.1(iii), 8.2, 12.1(vii) |
| Fourier coefficients and the Ramanujan-Petersson bound (statement) | 6.4, 6.5 |
| the Petersson inner product (definition, positive definite) | 10.1 to 10.5 |
| the Sturm bound and integrality; $S_2(\Gamma_0(N);\Z)$, $S_2(\Gamma_0(N);\Z_\ell)$ | 11.1 to 11.5 |
| modular forms with character (nebentypus), briefly | 6.6 |
| the Atkin-Lehner involutions $w_d$ and $w_N$: definition; action on $q$-expansions is not simple; action on cusps | 12.1, 12.2, 12.3, 12.4 |
| $X_0(N)$ as a moduli space of pairs $(E,C)$; cusps as degenerate pairs; the $\Q$-structure (statement) | 5.4 |
| example: $S_2(\Gamma_0(11))$ spanned by $\eta(z)^2\eta(11z)^2$, the form of 11a1; its first coefficients | 9.1, 9.2 |
| physics aside: Fourier series on a quotient | 6.3, 9.2 (and Part 1.1: valence via residues 7.3, Petersson as $L^2$ 10.1) |
| Section 6 row: newform $f_E$, $S_2(\Gamma_0(N))$, $q$-expansions, coefficientwise congruences (with Chapter 13) | 6.2, 6.3, 9.2, 11.4, 11.5 (newforms: Chapter 13) |
| Section 6 row: Petersson norm, Rankin-Selberg, $L(\operatorname{Sym}^2f,2)$, Zagier, Watkins, Flach (with 13, 14, 19) | 10.1, 10.4, 10.5 |
| Section 6 row: $H^1(X_0(N),\Z_\ell)$, cup product, Atkin-Lehner, Hecke self-adjointness (Chapters 8, 14; the involution is defined here) | 5.2, 8.2, 12.1, 12.2(iii) |
| hook: $S_2(\Gamma_0(N))$, the newform $f$ (Section 1) | 6.2, 8.2, 8.3, 9.2, 9.3 |
| hook: $q$-expansions and congruences coefficientwise (Section 1, Lemma lem:crit) | 6.3, 11.3, 11.4, 11.5 |
| hook: integral forms $S_2(\Gamma_0(N);\Z)$ (Lemma lem:crit) | 11.1, 11.2, 11.4 |
| hook: the Petersson norm $\langle f,f\rangle$ (Section 1, Zagier, Watkins) | 10.1, 10.4 |
| hook: the Atkin-Lehner involution $w_N$ (Section 4.1, the pairing $\hat\delta_!$) | 12.1, 12.2, 12.4(c) |
| hook: $X_0(N)$ as a curve (Section 1) | 5.2, 5.3, 5.4 |
| hook: the genus and $\dim S_2$ (background to multiplicity one) | 5.3, 8.2, 8.3 |
| also: Section 3 optimal-level theorem (nebentypus trivial) | 6.6 |
| also: Theorem thm:quant Step 1 ($S_2(\Gamma_0(N);\Z_\ell)$, congruences survive projection) | 11.1, 11.4(iii) |
| also: Theorem thm:twist ("preserves integrality"; levels of twists: Chapter 13) | 6.6 (remark), 11.1(c) |
| also: the Example of Section 3 (121a1, 539c1, 980i1 congruences) | 11.5 |
| also: Conjecture conj:eis, Section sec:eis (Eisenstein congruence; rational $5$-torsion of 11a1) | 8.4 |
| also: Lemma lem:euler, Theorem thm:dfg14 ($|\alpha/\beta|=1$) | 6.5 |
| also: important_notes.md points 30, 36, 39, 41 | 10.5(b); 12.2(iii); 12.2(iii), 12.4(c); 12.1(v), (vii) and Part 6.4 |
| also: what Chapters 8 and 9 deferred here | 2.1, 2.2, 5.2, 5.3, 7.2, 7.5, 8.2, 10.1 |

### 4.2 Exercises (Section 13 of the chapter), graded from easy to harder

1. Prove $\operatorname{Im}(\gamma z)=\det\gamma\,\operatorname{Im}z/|cz+d|^2$ and the invariance of $dx\,dy/y^2$. Show that the stabiliser of $i$ in $\SL_2(\R)$ is $\mathrm{SO}(2)$.
2. Move $z=0.1+0.05i$ into $\mathcal F$ by an explicit word in $S$ and $T$. Show $S^2=(ST)^3=-I$ and find the stabilisers of $i$, $\rho$, $-\bar\rho$.
3. Show $\Gamma_0(N)\backslash\SL_2(\Z)\simeq\mathbb P^1(\Z/N)$ and $\mu(N)=N\prod_{p\mid N}(1+1/p)$. For $N=11$ write the twelve coset representatives and sketch
   the fundamental domain $\bigcup\gamma_i\mathcal F$; check its hyperbolic area $12\cdot\pi/3$.
4. Find the cusps of $\Gamma_0(N)$ and their widths for $N=p$, $N=p^2$ and $N=20$; check that the widths add up to $\mu(N)$. Show that $X_0(121)$
   has twelve cusps, ten of them of the form $a/11$.
5. Show that the elliptic points of order $2$ of $\Gamma_0(N)$ correspond to the roots of $x^2+1$ modulo $N$, and compute $\nu_2$, $\nu_3$ for
   $N=5,10,13,37,121$. Deduce $g(X_0(37))=2$.
6. Derive the genus formula from Riemann-Hurwitz (Chapter 8). Compute $g(X_0(N))$ for $N=11,20,37,121,539$ and compare with Chapter
   8's list. Show $g(X_0(N))\ge1+\mu(N)/12-\frac{2^{\omega(N)}}4-\frac{2^{\omega(N)}}3-\frac{\nu_\infty(N)}2$ and use it to explain why only finitely
   many $N$ have genus $0$.
7. Prove the Lipschitz formula from the partial fractions of $\pi\cot\pi z$ and derive the $q$-expansions of $E_4$ and $E_6$ (the
   constants $240$ and $-504$). Check $\Delta=(E_4^3-E_6^2)/1728=q-24q^2+252q^3-\cdots$.
8. Using the valence formula, show $M_2(\SL_2(\Z))=0$, $\dim M_{12}=2$, and that $E_4$ vanishes only at $\rho$. Prove that $j$ is a bijection
   $\SL_2(\Z)\backslash\mathfrak H\to\C$ and compute $j(i)$, $j(\rho)$.
9. Show that $f\,dz$ is $\Gamma_0(N)$-invariant iff $f$ has weight $2$; show that at a cusp $f\,dz$ is holomorphic iff $f$ vanishes there, and
   that there is no condition at elliptic points. Deduce $\dim S_2(\Gamma_0(N))=g(X_0(N))$ and the residue relation of 8.2(iii).
10. (The Eisenstein congruence.) Show $E_2(z)-11E_2(11z)\in M_2(\Gamma_0(11))$. Using the Sturm bound $B_2(11)=2$, prove that
    $a_n(f_{11})\equiv\sigma(n)-11\sigma(n/11)\pmod5$ for all $n$, hence $a_\ell(\text{11a1})\equiv1+\ell\pmod5$ for all primes $\ell\ne11$. Relate this to the
    rational $5$-torsion point of 11a1 (Chapter 9) and to the Eisenstein case of the paper (Section sec:eis).
11. From the transformation law of $\eta$, show $f_{11}=\eta(z)^2\eta(11z)^2\in S_2(\Gamma_0(11))$ and $f_{11}|_2W_{11}=-f_{11}$. Compute $a_1,\dots,a_{13}$ and
    compare with $p+1-\#E(\F_p)$ for $E=$ 11a1 at $p=2,3,5,7,13$.
12. Prove that the Petersson integrand is $\Gamma_0(N)$-invariant, that the integral converges for $f$ cuspidal, and that $W_N$ is an
    isometry and self-adjoint. Show $\langle f,g\rangle_{\Gamma_0(NM)}=\frac{\mu(NM)}{\mu(N)}\langle f,g\rangle_{\Gamma_0(N)}$.
13. (Normalisations; with PARI.) Compute `mfpetersson` for the form of 11a1 and multiply by $\mu(11)=12$; compute the area of the
    period lattice of 11a1 and check $4\pi^2\langle f,f\rangle=\operatorname{vol}(\Lambda_E)$. In the class 11a, check that $5\operatorname{vol}(\Lambda_{\text{11a3}})/\operatorname{vol}(\Lambda_{\text{11a1}})=25$
    and deduce from $\deg\varphi\cdot\operatorname{vol}(\Lambda)=4\pi^2c^2\langle f,f\rangle$ that the parametrisation $X_0(11)\to$ 11a3 of degree $5$ has $c=5$ (Part 7, B1).
14. Prove 11.4(ii): the truncation $S_2(\Gamma_0(N);\Z)\to\Z^{B_2(N)}$ is injective with torsion-free cokernel. Deduce that
    $S_2(\Gamma_0(N);\Z)\otimes\F_\ell\to\F_\ell[[q]]$ is injective.
15. (Check the paper's claim.) Using Sturm's bound, prove that $a_n(\text{121a1})\equiv a_n(\text{121d1})\pmod3$ for all $n$, given that both forms
    lie in $S_2(\Gamma_0(121);\Z)$ and that the congruence holds for $n\le22$. Do the same for 539c1 against the twist of 11a1 by $\chi_{-7}$
    ($B_2(539)=112$). Explain why the paper's check "for $p<500$" suffices once $a_3$ and $a_{11}$ are compared.
16. Show that $W_d$ exists for $d\,\|\,N$, normalises $\Gamma_0(N)$, and satisfies $W_d^2\in d\Gamma_0(N)$. Show $w_N(E,C)=(E/C,E[N]/C)$ in the moduli
    description over $\C$.
17. For squarefree $N$ show that $w_e$ maps the cusp $1/c$ to $1/(ce/\gcd(c,e)^2)$. For $N=20$ list the six cusps (4.2) and compute the
    action of $w_4$, $w_5$, $w_{20}$ on them.
18. (Atkin-Lehner on oldforms.) For $h\in S_2(\Gamma_0(M))$ and $N=Mp$, $p\nmid M$, prove $(h|_2W_N)(z)=p\,(h|_2W_M)(pz)$ and
    $h(pz)|_2W_N=p^{-1}(h|_2W_M)(z)$. Write the matrix of $w_{22}$ on $\operatorname{span}\{f_{11}(z),f_{11}(2z)\}$ and check that it squares to $1$. Show that
    $\dim S_2(\Gamma_0(N))^+$ equals the genus of $X_0(N)/w_N$, and verify it for $N=11$ and $N=37$ with the fixed-point counts of 12.2.

## 5. Dependencies and forward pointers

Results from other chapters used here:
* Background (PLAN.md Section 2): complex analysis (holomorphic and meromorphic functions, Laurent series, Riemann's removable
  singularity theorem, the identity theorem, the argument principle and the residue theorem, Moebius transformations,
  $\pi\cot\pi z$ in partial fractions, uniform convergence of series of holomorphic functions); real analysis (double integrals,
  change of variables, absolute convergence); linear algebra (Hermitian inner products, orthogonal complements, eigenspaces of
  commuting involutions); RHB (Fourier series, separation of variables, contour integration, Sturm-Liouville inner products).
* Chapter 1 (`ch:groups`): group actions, cosets, orbit-stabiliser, $\SL_2(\Z/N)$, $\mathbb P^1(\Z/N)$ and lines (its C1), the
  generators of $\SL_2$ (cited, not reproved: 2.1 proves generation of $\SL_2(\Z)$ independently).
* Chapter 2 (`ch:rings`): $\Z/N$, the Chinese remainder theorem, $(\Z/N)^\times$, Euler's $\varphi$, Kronecker symbols $(\frac{-4}{p})$, $(\frac{-3}{p})$
  and the counts of roots of $x^2+1$, $x^2+x+1$ mod $N$ (4.3), Dirichlet characters and their conductors (6.6), divisor sums.
* Chapter 3 (`ch:modules`): free modules, saturated sublattices, split injections, base change $\otimes\Z_\ell$ (11.4).
* Chapter 4 (`ch:reps`): characters of finite abelian groups (the decomposition by nebentypus, 6.6(iii)).
* Chapter 6 (`ch:ant`): rings of integers $\mathcal O$, primes $\lambda$ (11.3, 11.4(iv)); Chapter 7 (`ch:local`): $\Z_\ell$, $\Q_\ell$ (11.1, 11.4(iii)).
* Chapter 8 (`ch:curves`): Riemann surfaces and charts (its 8.1), holomorphic maps, local normal form and degree (its 8.2), Riemann
  existence and GAGA (its 8.3), topological Riemann-Hurwitz and Euler characteristic (its 8.4(c), 7.2) for 5.3, holomorphic
  differentials, residues and the residue theorem (its 9.1, 9.2), $\dim H^0(\Omega^1)=g$ (its 9.3) for 8.2, positivity
  $\frac i2\int\omega\wedge\bar\omega>0$ (its 9.4(b)) for 10.1(iv), Riemann-Roch (its 5.2, 5.3) for 8.3, $H^1(X,\C)=H^0(\Omega^1)\oplus\overline{H^0(\Omega^1)}$
  (its 10.2(iii)) and automorphisms as isometries of the cup product (its 12.3(a)) for 12.2(iii), $\deg\varphi\cdot\int_Y=\int_X\varphi^*$ (its
  11.5(i)) for 10.4.
* Chapter 9 (`ch:ellcurves`): lattices, $G_{2k}(\Lambda)$, $g_2$, $g_3$, $\Delta(\Lambda)$, $j(\Lambda)$ (its 7.1), homothety classes of lattices
  $=\SL_2(\Z)\backslash\mathfrak H$ (its 7.5(i), (ii)) for 5.4 and 7.2, the period lattice and its area (its 7.6) for 10.4, the $a_p$ of the running
  examples and the rational $5$-torsion of 11a1 (its 8.7, 9.7) for 8.4 and 9.2, quadratic twists (its 10.3, 10.4) for 11.5.

Black boxes imported from later chapters (stated with a forward `\Cref`, used only in examples, remarks, exercises and
`paperlink`s, never in the proof of a numbered result of this chapter): newforms, Hecke operators, Petersson adjoints, the
recursion for $a_n$, twisting and the levels of twists, oldforms (Chapter 13; used in 6.5, 9.3, 10.3, 10.5(a), 11.4(v), 11.5,
12.4(b), (c)); modularity, Eichler-Shimura, $X_0(11)\simeq$ 11a1, the modular degree and the Manin constant (Chapter 14; used in 9.2(iv),
10.4); the functional equation and its sign, Rankin-Selberg (Chapter 19; 10.5(b), 12.4(c)).

Forward pointers (chapters that use this one):
* Chapter 13 (`ch:hecke`): $M_k(\Gamma_0(N))$, $S_k(\Gamma_0(N))$, the slash operator and C3 (for double cosets), $q$-expansions (6.3), the maps
  $f(z)\mapsto f(dz)$ (6.2(e)), the Petersson product and its behaviour under level change (10.1, 10.2), $W_N$ and $w_N$ on forms (12.1,
  12.2) for the adjoint of $U_p$ and for Atkin-Lehner theory, $S_2(\Gamma_0(N);\Z)$, its rank and saturation and Sturm (11.1 to 11.4) for the
  perfect pairing with $\T$ and the integral Hecke algebra, nebentypus (6.6) for twists, the dimension formulas (8.3).
* Chapter 14 (`ch:moddeg`): $X_0(N)$ as a compact Riemann surface and its $\Q$-model (5.2, 5.4(v)), cusps (4.2, 12.3), $S_2=H^0(\Omega^1)$ (8.2)
  for $J_0(N)(\C)=S_2^\vee/H_1$, the involution $w_N$ of $X_0(N)$ and its action on $\omega_f$ and on $H^1$ (12.1(v), (vii), 12.2(iii)) for
  $T^t=w_NTw_N$ and $\hat\delta_!$, the Petersson norm in the C5 normalisation (10.1, 10.4) for the Zagier-Watkins formula, the
  Eisenstein series of weight $2$ (8.4) for the Eisenstein ideal and the cuspidal subgroup.
* Chapter 15 (`ch:modgalrep`): nebentypus (6.6) in the optimal-level theorem; congruences and Sturm (11.4, 11.5) for the examples of
  Theorem thm:qual.
* Chapter 19 (`ch:lfunctions`): $q$-expansions and the Hecke bound (6.3, 6.4) for $L(f,s)$, $\alpha_p$, $\beta_p$ and Ramanujan-Petersson (6.5),
  the Petersson product (10.1) and point 30 (10.5(b)) for Rankin-Selberg, the sign $-\varepsilon_N$ (12.4(c)).
* Chapter 20 (`ch:congruence`): $S_2(\Gamma_0(N);\Z_\ell)$ and its $q$-expansions (11.1, 11.4) for the $\mathfrak m$-components; $w_N$ (12.2(iii)).
* Chapter 21 (`ch:paper`): A3.1 and A3.2 (integral forms, Petersson orthogonality, coefficientwise congruences), A4.1 ($w$ is
  $W_{M^\Sigma}$), the Example of Section 3 (11.5).
* Chapter 22 (`ch:computation`): PARI's `mfinit`, `mfdim`, `mfsturm`, `mfpetersson` (divides by $\mu(N)$, C5), `mfatkineigenvalues`,
  `mffromell`, `ellmoddegree`, `ellan`, `elltwist` as used in Part 6.6.

## 6. Notes for the writer

### 6.1 Conventions to state (Section 1 of the chapter, as `convention` environments)

C1 to C9 of Part 1.2. In addition one `convention` box in Section 10, "Normalisations of the Petersson product", with
exactly these lines: the book's product is unnormalised (C5); PARI's `mfpetersson` is the book's divided by $\mu(N)$; the
"normalised" product of some books is the book's divided by $\operatorname{vol}(\Gamma_0(N)\backslash\mathfrak H)=\pi\mu(N)/3$ and is independent of the level at which
$f$, $g$ are viewed; the formula $\deg\varphi_E\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c^2\langle f,f\rangle$ (Chapter 14) holds in the book's normalisation with $c$
defined by $\varphi_E^*\omega_E=c\cdot2\pi i\,f(z)\,dz$ (as in Chapter 8, its 4.3).

### 6.2 Pitfalls

* **Slash normalisation.** $(\det\gamma)^{k/2}$ (C3) versus Diamond-Shurman's $(\det\gamma)^{k-1}$: identical in weight $2$, different otherwise.
  Under $(\det)^{k-1}$, $W_N^2=-N\cdot I$ acts by $N^{k-2}$ times $(-1)^k$, so $w_N$ is an involution only after rescaling; under C3 it is an
  involution. Say this once; the paper only needs weight $2$.
* **Petersson normalisation (C5).** Never quote a numerical Petersson norm without saying which normalisation; the factor
  between PARI and the book is $\mu(N)$ ($12$ for $N=11$), and between "normalised" and the book $\pi\mu(N)/3$. 10.4 is the check.
* **Index in $\SL_2$ versus $\mathrm{PSL}_2$.** For $\Gamma_0(N)$ they agree ($-I\in\Gamma_0(N)$); for $\Gamma_1(N)$, $N\ge3$, the degree of $X_1(N)\to X(1)$ is half
  of $[\SL_2(\Z):\Gamma_1(N)]$. The genus formula 5.3 is stated for $\Gamma_0(N)$ only.
* **Cusps.** $\infty\sim1/N$ (width $1$), $0=0/1$ (width $N$); the width is relative to $\Gamma_0(N)$, not to $\SL_2(\Z)$. Irregular cusps exist for
  $\Gamma_1(4)$ but not for $\Gamma_0(N)$; do not state "cusp form iff $b_0=0$ in $q_h$" for groups with irregular cusps without care.
* **"$q$-expansion principle".** Here it means the elementary statements 6.3(iv), 8.1, 11.4; the algebraic $q$-expansion principle
  (Deligne-Rapoport, Katz: integrality at $\infty$ controls integrality of the form over $\Z[1/N]$) is only mentioned in 11.2. Do
  not claim that integrality at $\infty$ implies integrality at the other cusps.
* **$S_2(\Gamma_0(N);\Z_\ell)$** is defined as $S_2(\Gamma_0(N);\Z)\otimes\Z_\ell$ (C6), because $\Z_\ell\not\subset\C$ canonically; 11.4(iii) shows it is the same
  as the $\Z_\ell$-integral $q$-series in $S_2(\Gamma_0(N);\Q)\otimes\Q_\ell$. The paper's Lemma lem:crit and Theorem thm:quant use it in that sense.
* **Sturm and the paper's congruences.** Sturm's bound applies to forms in the same space $M_k(\Gamma_0(N);\mathcal O)$ and to congruences at
  **all** $n$. A congruence at all $p\notin\Sigma$ first needs depletion (Chapter 13), which raises the level (for example $121\cdot9=1089$,
  $B_2=264$; $539\cdot9\cdot11=53361$, $B_2=14784$). For the paper's three examples this is unnecessary because the congruences hold at
  all $n$ (11.5). For the Eisenstein example multiply by $12$ to clear the denominator before applying Sturm.
* **$f^\perp$ is a Petersson complement**, transcendental in definition; that it is defined over $\Q$ and $\T$-stable is Chapter 13's (10.3).
  Theorem thm:twist uses the $\T$-stable complement; Chapter 13 shows the two agree for a newform.
* **Atkin-Lehner on $q$-expansions** (12.4): never write $a_n(f|W_N)=\pm a_n(f)$ for a general $f$; only for eigenforms. Chapter 21's A3.2
  draft sentence about adjoints should read: for $(n,N)=1$, $T_n$ is self-adjoint; for $p\mid N$, $U_p^\dagger=w_NU_pw_N$ (Chapter 13); $f$ is a
  $w_N$-eigenvector.
* **Signs.** $W_N$ versus $-W_N$ (C4); the Atkin-Lehner sign $\varepsilon_N$ versus the root number $-\varepsilon_N$ in weight $2$ (12.4(c)); check both on
  11a1 ($\varepsilon=-1$, root number $+1$) and 37a1 ($\varepsilon=+1$, root number $-1$) before printing.
* **Hecke operators.** None here (C8). The card must not contain $T_n$, $U_p$, eigenforms or newforms as items; they appear only in
  forward pointers. Likewise twists of forms (Chapter 13) and $J_0(N)$ (Chapter 14).
* **Modularity.** 9.2(iv) is a numerical fact here; that $f_{11}$ is the form of 11a1 for all $n$ is Eichler-Shimura for $X_0(11)$,
  Chapter 14. Never present the check to $n=2000$ as a proof.
* **$j$ and uniformisation** (Chapter 9's writer note): 7.5 proves the bijectivity of $j$ by the valence formula without using
  uniformisation; Chapter 9 states uniformisation (R) and may now cite 7.5 for its first route. No circularity.
* Typography (PLAN.md 7.2): "Atkin-Lehner", "Ramanujan-Petersson", "Riemann-Hurwitz", "Rankin-Selberg", "Eichler-Shimura",
  "Deligne-Rapoport", "Katz-Mazur", "Diamond-Shurman" with plain hyphens; ranges "1 to 8"; tables with `booktabs`.

### 6.3 What to leave to Chapters 8, 13, 14 and 19

* **Chapter 8** (`ch:curves`): Riemann surfaces in general, Riemann-Hurwitz, holomorphic differentials and $\dim H^0(\Omega^1)=g$,
  Riemann-Roch, residues, $H^1$ and the cup product, correspondences and their adjoints. Chapter 12 applies them to $X_0(N)$
  (5.3, 8.2, 8.3, 10.1(iv), 12.2(iii)) and does not reprove them.
* **Chapter 13** (`ch:hecke`): Hecke operators $T_n$, $U_p$ (double cosets and $q$-expansion formulas), the Hecke algebra $\T$, its
  freeness, the perfect pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$, self-adjointness of $T_n$ and the adjoint of $U_p$ for the Petersson
  product, eigenforms, newforms and oldforms (Atkin-Lehner theory, multiplicity one, $\varepsilon_d(f)$, $a_p=-\varepsilon_p$, $a_p=0$ for $p^2\mid N$),
  twisting by characters and Atkin-Li, depleted and stabilised forms, $L(f,s)$, the statement of Rankin-Selberg. Chapter 12
  supplies only the spaces, the slash operator, the maps $f(z)\mapsto f(dz)$ as a remark, the Petersson product, $w_d$, integrality and
  Sturm.
* **Chapter 14** (`ch:moddeg`): $X_0(N)$ over $\Q$ beyond the statement 5.4(v), its rational points and cusps over $\Q$, $J_0(N)$, the
  Hecke correspondences, $T^t=w_NTw_N$, the pairing $\hat\delta_!=\langle x,w_Ny\rangle$, Eichler-Shimura, modularity, the modular parametrisation,
  the Manin constant and the Zagier-Watkins formula, the Eisenstein ideal and the cuspidal subgroup.
* **Chapter 19** (`ch:lfunctions`): the functional equation and root numbers, the Rankin-Selberg formula for $\langle f,f\rangle$ with exact
  local factors, symmetric square and adjoint $L$-functions, point 30.

### 6.4 How the relevant important_notes.md points are handled

* **Point 30** (the naive adjoint $L$-function is not the Euler product of $\sum a_n^2n^{-s}$). Chapter 12 touches it only where the
  Petersson norm is related to $L$-values: remark 10.5(b) states the correct relation
  $\sum a_n^2n^{-s}=\zeta^{(N)}(s-1)L^{\mathrm{nv}}(\operatorname{Sym}^2f,s)/\zeta^{(N)}(2s-2)$ (up to bad factors) and says that the Rankin series is not the naive
  adjoint $L$-function; the exact statement is Chapter 19's. The `paperlink` of Section 10 quotes the paper's sentence and the fix.
* **Point 36** (the pairing stays perfect on the $\mathfrak m$-component). Chapter 8, its 12.3(e), proves the abstract statement; it needs an
  involutive automorphism $w$ of the curve acting as an isometry with $w^{*2}=1$. Chapter 12 supplies exactly that input for
  $X_0(N)$: $w_N$ is a holomorphic involution of $X_0(N)$ (12.1(v)), hence an isometry of the cup product (12.2(iii)). The identity
  $T^t=w_NTw_N$ that completes the argument is Chapter 14's.
* **Point 39** (Lemma lem:hecke is always an equality). Its step (d) needs: "$w_N$ preserves the $f$-part and acts on it by the
  Atkin-Lehner sign $\pm1$ (on $f\,dz$ and on its conjugate)". Chapter 12 supplies $w_N^*(\omega_f)=\omega_{f|_2W_N}$ (12.1(vii)) and the
  consequence that $w_N^*$ acts by $\varepsilon$ on $\omega_f$, $\overline{\omega_f}$ and the real plane they span in $H^1(X_0(N),\R)$ (12.2(iii)), given $f|_2W_N=\varepsilon f$
  (Chapter 13 for newforms in general; 9.2(iii) proves $\varepsilon=-1$ for $f_{11}$). It also fixes that the paper's $w$ is exactly $W_{M^\Sigma}$
  (C4), with no hidden scalar in weight $2$ (C3: $(\det)^{k/2}=(\det)^{k-1}$ at $k=2$). The remaining steps of point 39 are Chapter 14's.
* **Point 41** (Tate module versus $H^1$ as Hecke modules). Chapter 12 only supplies that $w_N$ is an involution, so that
  $w_N^*=(w_N^{-1})^*=(w_N)_*$ on $H^1$ and $H_1$ and the correction "Poincare duality composed with $w_N$" is well defined; the rest is
  Chapter 14's (with Chapter 8, its 12.3(c)).
* Points 15 and B8 (curve-level twists): 11.5 states the congruences at the level of forms (classes), naming 121d, 539d by class
  only.

### 6.5 References

DiamondShurman (Chapters 1 to 3, 5, 6, 7; sections cited, theorem numbers 3.1.1, 3.5.1, 3.6.1 marked "verify"), Shimura71 (Chapters
1 to 3, 6.7; Theorem 3.52 and Propositions 1.40, 1.43 marked "verify"), SerreCourse (Chapter VII; theorem numbers marked
"verify"), Miyake (4.6), Koblitz (Chapter III), Knapp (Chapters VIII, IX, XI by chapter), AtkinLehner70, Stein (book;
Chapter 9 for Sturm), Zagier85, Watkins02, Cremona97, Deligne, Shimura76, DFG04 (Lemma 2.12 as the paper cites it), PARI and
PARIusers are in `refs.bib`. Not in `refs.bib`, to be added to `bib/ch12.bib` with complete checked entries if cited: Sturm,
*On the congruence of modular forms* (Lecture Notes in Math. 1240, 1987); Apostol, *Modular Functions and Dirichlet Series in
Number Theory* (GTM 41); Ligozat, *Courbes modulaires de genre 1* (Bull. Soc. Math. France Memoire 43, 1975); Ogg, *Rational points
on certain elliptic modular curves* (Proc. Sympos. Pure Math. 24, 1973); Deligne-Rapoport, *Les schemas de modules de courbes
elliptiques* (Lecture Notes in Math. 349, 1973); Katz-Mazur, *Arithmetic Moduli of Elliptic Curves* (Annals of Math. Studies 108,
1985). Every bibliographic detail above was recalled, not re-verified; check before adding.

### 6.6 Verification log (computations done for this outline)

Python 3 with sympy 1.14 and PARI/GP 2.17 through `cypari2`; scripts in `/tmp/ch12`; Cremona `ecdata` files from `/tmp/ch09/data`.
* `check1.py`: $\mu$, $\nu_2$, $\nu_3$, $\nu_\infty$, $g$ by the formulas versus brute force on $\mathbb P^1(\Z/N)$ (fixed points of $S$ and $ST$, $T$-orbits) for 44
  levels up to $169$, all equal; cusp widths by the formula $N/\gcd(c^2,N)$ versus $T$-orbit lengths for $N\in\{4,8,9,11,20,25,27,36,49,77,99,121\}$;
  $g=$ `mfdim([N,2],1)` for all tested $N$ including $539$, $726$, $980$. Genus $0$ and $1$ lists checked for $N\le2000$.
* `check2.py`: $\eta(z)^2\eta(11z)^2$ against `ellan` of 11a1 for $n\le2000$ (and 11a2, 11a3 for $n\le200$); PARI's newform at level $11$;
  the dimension formulas 8.3 against `mfdim([N,k],1)` and `mfdim([N,k],4)` for $N\le60$ and $N\in\{77,99,121,539\}$, $k=2$ to $14$, no
  mismatch; level-one dimensions for $k\le26$; $B_2(N)=$ `mfsturm([N,2])` for ten levels.
* `check3.py`: $f_{11}|_2W_{11}/f_{11}=-1$ at three points; $f_{11}(i/\sqrt{11})\approx0.1029$; `mfatkineigenvalues` at $N=11,20,37,99,121$; root
  numbers of 11a1, 37a1; `mfpetersson`$\cdot4\pi^2/\operatorname{vol}=\deg/\mu$ for five curves (so PARI divides by $\mu$).
* `check4.py`, `check5.py`: the three congruences of the paper's Section 3 for all $n\le3000$ (121) and $n\le20000$ (539, 980), with the
  twists computed by `elltwist` and their conductors $121$, $539$, $980$; Sturm bounds at the depleted levels; Hasse for 11a1 at
  $p<10^5$; Ramanujan's bound for $\tau(p)$, $p<2000$; the $q$-expansions of $j$, $E_2$, $E_4$, $E_6$, $\Delta$.
* `check6.py`: $\#\SL_2(\Z/N)$ and $[\SL_2(\Z):\Gamma_1(N)]$ by enumeration for $N\le12$; the action of $w_e$ on cusps for $N=6,30,77$; fixed
  points of $w_N$ by class numbers and $\dim S_2^+$ by PARI's Atkin-Lehner matrix for $N=11,23,37,43$.
* `check7.py`: the $\eta$-products of 9.2 against 14a1, 15a1, 20a1, 24a1, 27a1, 32a1, 36a1 for $n\le300$; the Eisenstein congruence mod $5$
  for $n\le5000$; the unnormalised Petersson norms and $4\pi^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)=\deg\varphi_E$ to 30 digits for 11a1, 20a1, 37a1, 99a1,
  121a1; the period areas of 11a1, 11a2, 11a3 (ratios $1:\frac15:5$).
* By hand: the $W_d^2$ identity of 12.1(ii); $W_N=W_M\operatorname{diag}(p,1)$ and the matrix of $w_{22}$ on $\{f_{11}(z),f_{11}(2z)\}$ (also checked numerically);
  $\eta$-transformation for $f_{11}|W_{11}$; $\Delta(\Lambda_z)=(2\pi)^{12}\Delta(z)$; the $E_2$ transformation from $E_2^*$; the valence contour
  angles; the residue of $\omega_f$ at a cusp.
* Not checked: theorem numbers in DiamondShurman, Shimura71, SerreCourse, Stein, Miyake (marked "verify"); the normalisations
  used by Zagier85 and Watkins02 in print.

## 7. Points for important_notes.md

New points in the area of this chapter ($S_2(\Gamma_0(N))$, $q$-expansions and coefficientwise congruences, integral forms, the
Petersson norm, $w_N$, $X_0(N)$ as a curve), not among points 1 to 45 and B1 to B9 already recorded. Points 30, 36, 39, 41 are
handled in Part 6.4 and not repeated.

**Errors in the paper in this area: none found.** Checked in particular: the definition of $r_E$ (Section 1 and Section 3
preamble), the use of $S_2(\Gamma_0(N);\Z)$ and of its $\Z_\ell$-version in Lemma lem:crit and Theorem thm:quant Step 1, "orthogonal
complement" in Lemmas lem:crit and lem:old, the description of $w$ in Section 4.1 (it is exactly $W_{M^\Sigma}$ with no scalar, C3, C4),
the direction of the Zagier-Watkins relation in Section 1 ("$\langle f,f\rangle$ divided by the area": correct, the explicit factor being
$4\pi^2c^2$ in the unnormalised normalisation, 10.4), and every congruence of the Example of Section 3 (11.5).

* **P1. Example of Section 3: the three congruences hold at every $n$, and the paper's finite checks already prove them by
  Sturm's bound (an optional strengthening, not an error).**
  Location: the Example after the proof of Theorem thm:qual: "$a_p(\text{121a1})\equiv\chi_{-11}(p)a_p(\text{11a1})\pmod3$ for all $p\ne3,11$ (checked
  for $p<500$)", "$a_p(\text{539c1})\equiv\chi_{-7}(p)a_p(\text{11a1})\pmod3$ for all $p\ne3,7,11$ (checked for $p<1000$)",
  "$a_p(\text{980i1})\equiv\chi_{-7}(p)a_p(\text{20a1})\pmod5$ for all $p\ne2,5,7$ (checked for $p<1000$)".
  Observation: in each case both forms are newforms in the same space ($S_2(\Gamma_0(121))$, $S_2(\Gamma_0(539))$, $S_2(\Gamma_0(980))$: the twists
  have conductors $121$, $539$, $980$) with integer coefficients, and the congruence also holds at the excluded primes ($a_3$: $2$
  versus $-1$; $a_3$: $-2$ versus $1$, $a_7$: $0,0$, $a_{11}$: $1,1$; $a_2$: $0,0$, $a_5$: $1,1$, $a_7$: $0,0$). So the forms are congruent at
  every $n$, and by Sturm's bound ($B_2=22$, $112$, $336$) this is proved by the coefficients $n\le B_2$, which the stated checks
  cover once the excluded $a_p$ are included. Fix (optional): "and in fact $f_{\text{121a}}\equiv f_{\text{11a}}\otimes\chi_{-11}\pmod3$ coefficientwise, which
  Sturm's bound ($22$ at level $121$) reduces to a finite check", and likewise for the other two. Effect: the illustrations
  become theorems; nothing else changes. Confidence: high (all $n\le20000$, $n\le3000$ for the first; Sturm bounds from PARI
  agree with $\lfloor\mu/6\rfloor$).

Book-internal inconsistencies found while preparing this outline:

* **B1. The place of the Manin constant in the Zagier-Watkins formula.** PLAN.md (Chapter 14 scope: "$\deg\varphi_E=4\pi^2\langle f,f\rangle/(c^2
  \operatorname{vol}(\Lambda_E))$ up to the precise normalisation") and the Chapter 9 outline (Part 0, the Chapter 14 bullet: "the formula
  $\degphi=4\pi^2\langle f,f\rangle/(c^2\operatorname{vol}(\Lambda_E))$") put $c^2$ in the denominator, while the Chapter 8 outline (its 4.3) defines $c$ by
  $\varphi_E^*\omega_E=2\pi ic\,f(z)\,dz$. With that definition and the unnormalised Petersson product (C5), pulling back the area form gives
  $\deg\varphi_E\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c^2\langle f,f\rangle$, that is, $\deg\varphi_E=4\pi^2c^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$: $c^2$ in the **numerator**. Numerical check in
  the class 11a (where $X_0(11)=$ 11a1, $\deg=1$, $c=1$): the parametrisation $X_0(11)\to$ 11a3 has degree $5$ and $5\operatorname{vol}(\Lambda_{\text{11a3}})/\operatorname{vol}(\Lambda_{\text{11a1}})=25$,
  so its constant is $c=5$, an integer as it must be (the Neron differential pulls back integrally); with $c^2$ in the
  denominator one would get $c=1/5$. For optimal curves $c=1$ in all computed cases, so no number in the paper or the tables
  changes. Fix: Chapter 14 must state $\deg\varphi_E\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c^2\langle f,f\rangle$ with both conventions (C5 here, $c$ as in Chapter 8)
  spelled out; PLAN.md and the Chapter 9 outline should be read accordingly. Confidence: high (derivation in 10.4, numerics in
  Part 6.6).
* **B2. Who proves that $S_2(\Gamma_0(N);\Z)$ is a lattice.** PLAN.md puts "integrality (forms with integer coefficients,
  $S_2(\Gamma_0(N);\Z)$, $S_2(\Gamma_0(N);\Z_\ell)$)" in Chapter 12 and "the integral structure: $S_2(\Gamma_0(N);\Z)$ is a lattice" in Chapter 13.
  Resolution adopted here: Chapter 12 states Shimura's integral basis theorem (11.2, R) and proves the consequences (rank,
  saturation, split truncation, base change to $\Z_\ell$ and $\F_\ell$: 11.4); Chapter 13 cites 11.2 and 11.4 and proves the perfect pairing
  with $\T$. The Chapter 13 outline should follow this.
* **B3. Chapter 21 outline, A3.2, step (1)**, contains a self-correcting sentence ("since $T_n^*=w_NT_nw_N$ for $n$ prime to $N$... the
  writer should use: ..."). The correct statement for the Petersson product is: $T_n$ is self-adjoint for $(n,N)=1$, $U_p^\dagger=w_NU_pw_N$
  for $p\mid N$, and a newform is a $w_N$-eigenvector (Chapter 13; 10.5(a) and 12.4(c) here). Not an inconsistency in substance; the
  sentence should be cleaned when Chapter 21 is written.
* Consistency checks that passed: the Chapter 8 outline's genera ($g(X_0(N))=0,1,1,2,7,9,6,19,49,109,145$ for $N=1,11,20,37,77,99,121,140,
  539,726,980$) and its description of $X_0(N)\to X(1)$ (degree $\mu(N)$, branched over $j=0,1728,\infty$) agree with 5.3; the Chapter 9
  outline's 11a1 coefficients and the claim that they agree with the $\eta$-product (to $q^{20}$) agree with 9.2 (checked to
  $q^{2000}$); Chapter 9's deferral of the bijectivity of $j$ is discharged by 7.5 without circularity.
