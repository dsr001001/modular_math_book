# Chapter 09: Elliptic curves over fields (`ch:ellcurves`, `chapters/ch09_ellcurves.tex`)

Stage 1 line-up. Part III (Curves and elliptic curves). Target length 2,140 lines of LaTeX (card excluded; see
Part 3), inside the 1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the
Chapter 2, 5 and 6 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses;
reference (book and section or chapter; a theorem number only where the outline author is sure, otherwise the
section, and numbers marked "(verify)" must be checked against the book before they are printed); the paper's
use by its `\label` names, or "background". Every computation quoted below (invariants, division polynomials,
twists, point counts, periods, the data of the running examples) was checked by Python/sympy/mpmath scripts in
`/tmp/ch09` against Cremona's `ecdata` files for conductors below 10,000 (verification log, Part 7).

## 0. What this chapter is for

PLAN.md says the paper hooks of this chapter are "everything". Concretely the chapter must deliver the
following, and it is organised around them.

1. **The objects of Section 1.1 of the paper.** $E/\Q$ by a Weierstrass equation; $E[\ell]$, $T=T_\ell E$,
   $V=V_\ell E$, $\rho=\rho_{E,\ell}$, $\bar\rho=\bar\rho_{E,\ell}$, $\rho\bmod\ell^k$ as the action on $E[\ell^k]$; $\det\rho=\chi_\ell$ by
   the Weil pairing; complex conjugation with determinant $-1$; the Weil pairing as $T\simeq\Hom(T,\Z_\ell(1))$ (used
   for $A(1)=T^D$ in Section 4.2 and for important_notes.md point 26).
2. **Definition def:terms and the table of Section 1.** The invariant $j_E$ and $v_q(j_E)$ (independent of the
   model, invariant under every quadratic twist, so $t_\ell(E,q)$ is twist-invariant); $a_q(E)$ and the
   characteristic polynomial $X^2-a_qX+q$ of Frobenius with roots $\alpha,\beta$, $\alpha\beta=q$, $\alpha+\beta=a_q$; the
   twist $E'$ of good reduction at an $\mathrm I_0^*$ prime and the fact that only $a_q(E')^2$ enters; the
   statement "both terms are invariant under quadratic twist" in its correct form (important_notes.md point 15).
3. **Lemma lem:twist (ii) and Section 1.4** (models and invariants of twists): $E^{(d)}$ for a general Weierstrass
   model, $c_4,c_6,\Delta$ scaled by $d^2,d^3,d^6$, the same $j$, the difference between the twist by $q$ and by
   $q^*$ (important_notes.md point 29), $\rho_{E^{(d)},\ell}=\rho_{E,\ell}\otimes\chi_d$, $a_p(E^{(d)})=\chi_d(p)a_p(E)$, composite twists
   $E_S$ (Theorems thm:twist, thm:quant), and $V=V'\otimes\chi_q$ in Lemma lem:euler. (The effect on Kodaira types,
   Lemma lem:twist (i), (ii), is proved in Chapter 10.)
4. **Lemma lem:h0** (the CM facts): endomorphism rings, the thirteen CM $j$-invariants, $\rho\simeq\rho\otimes\chi_K$ and
   $a_p=0$ at good primes inert in the CM field $K$, the fact that a prime ramified in $K$ divides $N$ (so CM by
   $\Q(\sqrt{\ell^*})$ forces $\ell\mid N$: important_notes.md point 14), with the warning that the paper's sentence uses
   the wrong character (point 5).
5. **Proposition prop:ns** (the 3-division polynomial): $\psi_3=3x^4+b_2x^3+3b_4x^2+3b_6x+b_8$, its four roots are the
   $x$-coordinates of the four lines of $E[3]$, Galois-equivariantly; a rational root iff a rational $3$-isogeny; the
   factorisation pattern is the orbit pattern of the image on $\mathbb P^1(\F_3)$ (Chapters 1 and 5);
   $\operatorname{disc}\psi_3\in-3\cdot(\Q^\times)^2$. Worked factorisations for 11a1, 121a1, 726a1 (the paper's $\Ns$
   example), 20a1, 14a1, 27a1.
6. **Conjecture conj:eis and Section sec:eis** (torsion and isogenies): Mordell-Weil, Mazur's torsion theorem,
   rational $\ell$-isogenies and reducibility of $E[\ell]$, isogeny classes, the structure $\Z/\ell\oplus\mu_\ell$, and the
   proof (important_notes.md point 17, decided here) that a non-CM curve with $E[3]\simeq\Z/3\oplus\mu_3$ has no rational
   point of order $9$, which turns the paper's bound $D\le2$ from conjecture into a consequence of the first bound.
7. **Optimality and $\ell$** (important_notes.md point 27; Section sec:oot): if $E[\ell]$ is irreducible, all
   isogenies in the class are prime to $\ell$ up to $[\ell^k]$, so $T_\ell$, $\rho$, $h_\ell(E)$ and every $\ell$-adic invariant
   of the adjoint are the same for all curves of the class; a trivial isogeny class gives $E[\ell]$ irreducible for
   every $\ell$.
8. **Curves over $\C$**: lattices, $\wp$, uniformisation, $\SL_2(\Z)\backslash\mathfrak H$, the period lattice $\Lambda_E$ of a
   curve over $\Q$ and its area $\operatorname{vol}(\Lambda_E)$ (which Chapter 14 needs for the Zagier-Watkins formula),
   computed for 11a1.
9. **Curves over finite fields**: Frobenius, $a_p$, Hasse, the characteristic polynomial, supersingularity, the
   quadratic twist over $\F_q$ (the factorisation $(q+1)^2-a^2=\#E(\F_q)\#E^{\mathrm{tw}}(\F_q)$ behind the $\mathrm I_0^*$ row).
10. **$L(E,s)$ by its Euler product**, with the bad factors, and the **Cremona and LMFDB labels** of the running
    examples 11a1, 20a1, 121a1, 121c, 121d, 539c1, 980i1, 726a1, 99A1, with their basic data checked.

Split with the neighbouring chapters (decided here, consistent with PLAN.md Section 4 and with what the
written outlines assume):
* **Chapter 8** (outlined in parallel) supplies: projective plane, smooth plane curves, function fields, divisors,
  principal divisors, $\operatorname{Pic}^0$, Riemann-Roch (statement) and its consequence "a genus-one curve with a
  rational point is a plane cubic", degree of a morphism (three descriptions), separable and inseparable
  morphisms, differentials, compact Riemann surfaces versus curves over $\C$, Jacobians as complex tori,
  Abel-Jacobi. Its finished outline (`outlines/ch08_curves.md`, split section 6.3) also proves, for a general
  genus-one curve, that a genus-one curve with a rational point has a Weierstrass equation (its 5.6), the
  bijection $P\mapsto$ class of $(P)-(O)$ onto $\operatorname{Pic}^0$ (its 5.7, which gives associativity of the group law), and that
  every nonconstant morphism between genus-one curves in characteristic $0$ is unramified (its 7.3(b)). Chapter 9
  cites these from `\Cref{ch:curves}` and does not reprove them; it proves the identification of the $\operatorname{Pic}^0$
  structure with the chord-tangent law (item 2.3) and everything else in its PLAN.md scope.
* **Chapter 10** supplies: minimal models (existence, uniqueness, the criterion), reduction types, the reduction
  map and its injectivity on prime-to-$p$ torsion (formal group), the Neron model and Neron differential, Kodaira
  types, Tate's algorithm, conductor exponents, the Tate curve, and the *proofs* of Lemma lem:twist (i), (ii) on
  types. Chapter 9 uses the conductor $N$ and the types of the running examples as data, with a forward
  pointer, and states the injectivity of reduction on torsion with a forward reference.
* **Chapter 11** supplies: the images of $\bar\rho_{E,\ell}$ (Serre, Zywina, Sutherland labels), the full
  Neron-Ogg-Shafarevich criterion, local representations at bad primes and at $\ell$, irreducible versus absolutely
  irreducible, Serre conductor, and the *proofs* of Proposition prop:ns and Lemma lem:h0. Chapter 9 gives the
  objects ($\rho$, $\bar\rho$, $\det$, complex conjugation), the division polynomial, the CM facts, the isogeny facts
  and the easy direction "good reduction at $p\ne\ell$ implies unramified with $\rho(\Frob_p)$ of characteristic polynomial
  $X^2-a_pX+p$".
* **Chapter 14** supplies: modularity, $X_0(N)$, the optimal curve and its Cremona label, the modular degree, the
  Manin constant and the formula $\degphi=4\pi^2c^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$. Chapter 9 defines
  $\Lambda_E$ and its area and records the convention "Cremona's curve number 1 is the optimal curve" as a convention
  with the exception 990h (item 12.1).
* **Chapter 12** supplies the fundamental domain for $\SL_2(\Z)$, modular functions, the $q$-expansion of $j$, the
  surjectivity of $j$ on $\mathfrak H$ (valence formula). Chapter 9 proves "lattices up to homothety $=$
  $\SL_2(\Z)\backslash\mathfrak H$" and states the rest.
* **Chapter 19** supplies analytic continuation and the functional equation of $L(E,s)$ and the local factors
  via Weil-Deligne representations; Chapter 9 defines $L(E,s)$ by its Euler product.
* **Chapters 5 and 6** already contain the quartic-on-lines proposition (Chapter 5, galois:quartic-on-lines,
  which needs "the roots of $\psi_3$ are the $x$-coordinates of the four lines, Galois-equivariantly" from here) and a
  preview of CM (Chapter 6, item 6.5, which quotes "the Galois action on endomorphisms" from here). Chapter 9 is
  the home of the elliptic-curve side of both; it cites the field-theoretic and number-theoretic sides.
* **Chapter 2** has the identity $(1-\frac\alpha{\beta q})(1-\frac1q)(1-\frac\beta{\alpha q})=\frac{q-1}q\cdot\frac{(q+1)^2-a^2}{q^2}$ and quotes the
  Hasse bound and $\#E(\F_q)=q+1-a_q$ from here (its 11.4).
* **Chapter 22** supplies PARI/GP (`ellinit`, `elldivpol`, `ellap`, `elltors`, `ellisomat`, `ellperiods`); Chapter 9 may
  show one-line GP commands in `lstlisting` but explains only the mathematics.

## 1. Global conventions fixed in this chapter

* **C1 (fields and curves).** $K$ is a field, $\bar K$ a fixed algebraic closure, $G_K=\Gal(K^{\mathrm{sep}}/K)$. An elliptic curve
  over $K$ is a pair $(E,O)$, $E$ a smooth projective curve of genus one over $K$ and $O\in E(K)$; by Riemann-Roch
  (Chapter 8) it has a Weierstrass model (item 1.2). "$E/\Q$" always means a curve given by a Weierstrass equation
  with rational coefficients; from Section 9 on, by a global minimal model (Chapter 10), as in Cremona's tables.
  Whenever $\ell$ appears, $\ell\ne\operatorname{char}K$.
* **C2 (letters).** $p$, $q$, $\ell$ are primes. As in the paper, $q$ is usually a bad prime of $E/\Q$, $p$ any prime and $\ell$
  the coefficient prime. In Section 8 the size of a finite field is written $\mathfrak q=p^r$ when it need not be
  prime (Chapter 1, C4 and Chapter 2, C2 make the same warning); for $\F_p$ with $p$ prime the notation is $a_p$.
* **C3 (Weierstrass data).** $a_1,a_2,a_3,a_4,a_6$; $b_2,b_4,b_6,b_8$; $c_4,c_6$; $\Delta$; $j=c_4^3/\Delta$; the invariant
  differential $\omega=dx/(2y+a_1x+a_3)$. These are Silverman's (AEC III.1) and PARI's conventions; PARI's `ellinit`
  returns them in this order (Chapter 22).
* **C4 (twists and characters).** For $d\in K^\times$ (char $K\ne2$), $\chi_d\colon G_K\to\{\pm1\}$ is the character of
  $K(\sqrt d)/K$, $\sigma(\sqrt d)=\chi_d(\sigma)\sqrt d$. For $K=\Q$, $\chi_d(\Frob_p)=\bigl(\frac Dp\bigr)$ (Kronecker symbol) for $p\nmid D$, with
  $D$ the discriminant of $\Q(\sqrt d)$ (Chapters 2 and 6). For an odd prime $q$, $q^*=(-1)^{(q-1)/2}q$ and, **as in the
  paper**, $\chi_q:=\chi_{q^*}$ is the quadratic character of conductor $q$ (Chapter 2, C5). The paper also writes $\chi_\ell$
  for the cyclotomic character; in Chapter 9's own text the cyclotomic character is $\chi_\ell^{\mathrm{cyc}}$ or simply
  $\chi_\ell$ only where no quadratic character of conductor $\ell$ is in sight, and $\bar\chi_\ell$ is its reduction; the
  `paperlink` environments use the paper's notation and say so.
* **C5 (Frobenius).** For $E$ over a finite field $\F_{\mathfrak q}$ the Frobenius endomorphism $\pi\colon(x,y)\mapsto(x^{\mathfrak q},y^{\mathfrak q})$ acts on
  $E(\bar\F_p)$ exactly as the arithmetic Frobenius $\phi_{\mathfrak q}\in G_{\F_{\mathfrak q}}$ ($t\mapsto t^{\mathfrak q}$). For $E/\Q$ with good reduction at
  $p\ne\ell$, $\Frob_p$ in a group-theoretic statement is an **arithmetic** Frobenius (Chapter 6, 3.7; Chapter 21, C2(a));
  $\rho_{E,\ell}(\Frob_p)$ has characteristic polynomial $X^2-a_pX+p$. The Euler factor of $E$ is
  $\det(1-\Frob_p\,p^{-s}\mid V_\ell E)^{-1}$ with the arithmetic Frobenius on $V_\ell E$, equivalently with the geometric
  Frobenius on the dual $V_\ell E^\vee=H^1$; with the geometric Frobenius on $V_\ell E$ itself one gets $L_p(E,s+1)$, because
  $V_\ell E\simeq V_\ell E^\vee(1)$ (item 5.5). The chapter states this in a `convention` and Chapter 19 and Chapter 21 must
  match it (see Part 8, B3).
* **C6 (labels).** Cremona labels are written as the paper writes them (11a1, 121c, 99A1); "class 121c" means the
  isogeny class, "121c1" the curve. The capital letters of Cremona's book and of ARS12 (99A1) denote the same
  classes as the lower-case letters of the `ecdata` files. LMFDB labels are written 11.a2 (item 12.1).
* **C7 (Weil pairing sign).** The Weil pairing is Silverman's $e_m$ (AEC III.8). Some books use the inverse; every
  statement in the book that depends on the sign (the comparison with $e^{2\pi i/m}$ over $\C$, item 7.4) says which.
  $\det\rho=\chi_\ell$ does not depend on the sign.
* **C8 (typography).** PLAN.md Section 7.2: no dash ligatures (write "Mordell-Weil", "Neron-Ogg-Shafarevich",
  "pages 33 to 186"), ASCII source, labels `...:ellcurves:...`; Kodaira symbols as in PLAN.md 7.1.

## 2. Line-up of the core results, in teaching order

### Section 1. Weierstrass equations and their invariants

**1.1 `def:ellcurves:weierstrass`** (definition; P). A Weierstrass equation over $K$ is
$$y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6,\qquad a_i\in K,$$
with projective closure $Y^2Z+a_1XYZ+a_3YZ^2=X^3+a_2X^2Z+a_4XZ^2+a_6Z^3$ and the single point $O=[0:1:0]$ at infinity.
Put $b_2=a_1^2+4a_2$, $b_4=2a_4+a_1a_3$, $b_6=a_3^2+4a_6$, $b_8=a_1^2a_6+4a_2a_6-a_1a_3a_4+a_2a_3^2-a_4^2$,
$c_4=b_2^2-24b_4$, $c_6=-b_2^3+36b_2b_4-216b_6$, $\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6$, and $j=c_4^3/\Delta$ when $\Delta\ne0$.
Identities: $4b_8=b_2b_6-b_4^2$ and $1728\Delta=c_4^3-c_6^2$. If $\operatorname{char}K\ne2$, $\eta=2y+a_1x+a_3$ gives
$\eta^2=4x^3+b_2x^2+2b_4x+b_6$; if $\operatorname{char}K\ne2,3$, $(x,y)\mapsto((36x+3b_2),\,108(2y+a_1x+a_3))$ gives the short form
$y^2=x^3-27c_4x-54c_6$. Invariant differential $\omega=dx/(2y+a_1x+a_3)=dy/(3x^2+2a_2x+a_4-a_1y)$, holomorphic and
nowhere vanishing (Chapter 8 for the words). Both identities and the completed square were checked symbolically.
Reference: Silverman AEC III.1. Paper: Section 1.1 and everywhere ($E$ by a model; PARI's `ellinit([a1,a2,a3,a4,a6])`
in the appendix, e.g. 121a1 $=[1,1,1,-30,-76]$), Lemma lem:twist (ii) (models $y^2=x^3+a_2x^2+a_4x+a_6$).

**1.2 `prop:ellcurves:smooth`** (proposition; P). The curve of 1.1 is smooth iff $\Delta\ne0$. If $\Delta=0$ it has exactly
one singular point, a node if $c_4\ne0$ and a cusp if $c_4=0$. A smooth Weierstrass curve with $O$ is an elliptic
curve; conversely every elliptic curve over $K$ is isomorphic to a smooth Weierstrass curve with $O\mapsto[0:1:0]$
(via $x\in L(2O)$, $y\in L(3O)$; proved in Chapter 8, item 5.6, cited here, not reproved). Reference: AEC III.1.4(a) (verify) and III.3.1.
Paper: background (the singular reductions of Chapter 10: node $=$ multiplicative, cusp $=$ additive).

**1.3 `prop:ellcurves:coordchange`** (proposition; P). The admissible changes of coordinates are
$x=u^2x'+r$, $y=u^3y'+su^2x'+t$ with $u\in K^\times$, $r,s,t\in K$; they form a group. They transform
$ua_1'=a_1+2s$, $u^2a_2'=a_2-sa_1+3r-s^2$, $u^3a_3'=a_3+ra_1+2t$, $u^4a_4'=a_4-sa_3+2ra_2-(t+rs)a_1+3r^2-2st$,
$u^6a_6'=a_6+ra_4+r^2a_2+r^3-ta_3-t^2-rta_1$; $u^2b_2'=b_2+12r$, $u^4b_4'=b_4+rb_2+6r^2$, $u^6b_6'=b_6+2rb_4+r^2b_2+4r^3$,
$u^8b_8'=b_8+3rb_6+3r^2b_4+r^3b_2+3r^4$; $u^4c_4'=c_4$, $u^6c_6'=c_6$, $u^{12}\Delta'=\Delta$, $j'=j$, $\omega'=u\omega$. Every isomorphism
of Weierstrass curves sending $O$ to $O$ is of this form (S; AEC III.3.1(b)). All formulas checked symbolically by
substitution. Consequences used later: for $K=\Q$ and a prime $q$, $v_q(j)=3v_q(c_4)-v_q(\Delta)$ does not depend on the
model, and $v_q(\Delta)$ changes by multiples of $12$ (the minimality criterion is Chapter 10). Reference: AEC III.1,
Table 3.1. Paper: Definition def:terms ($v_q(j_E)$, $t_\ell(E,q)$), Lemma lem:twist (ii) ("$v_q(\Delta)$ ... otherwise $12$ is
subtracted"), the appendix (`valuation(E.j, q)`).

**1.4 `thm:ellcurves:jinv`** (theorem; P). (i) Two elliptic curves over $K$ are isomorphic over $\bar K$ iff they have the
same $j$. (ii) Every $j_0\in K$ is the $j$-invariant of a curve over $K$: $y^2+y=x^3$ ($j=0$), $y^2=x^3+x$ ($j=1728$), and
$y^2+xy=x^3-\frac{36}{j_0-1728}x-\frac1{j_0-1728}$ for $j_0\ne0,1728$ (checked symbolically). Proof of (i) for
$\operatorname{char}K\ne2,3$ with short models: $j=j'$ gives $u$ with $c_4'=u^{-4}c_4$, $c_6'=u^{-6}c_6$ over $\bar K$; the general
characteristic is stated (AEC Appendix A). Reference: AEC III.1.4(b), (c) (verify). Paper: Definition def:terms
($j_E$), Lemma lem:twist ("the same $j$-invariant"), Proposition prop:ns and Section sec:anomaly (CM $j$-values excluded).

**1.5 `prop:ellcurves:aut`** (proposition; P, $\operatorname{char}K\ne2,3$). $\operatorname{Aut}_{\bar K}(E)$ (automorphisms fixing $O$) is $\{\pm1\}$ if
$j\ne0,1728$, $\mu_4$ if $j=1728$ and $\mu_6$ if $j=0$, acting by $u$ with $u^4c_4=c_4$, $u^6c_6=c_6$, $r=s=t=0$ on a short
model; $[-1](x,y)=(x,-y-a_1x-a_3)$. Reference: AEC III.10.1 (verify). Paper: background for quadratic twists
(10.2: for $j\ne0,1728$ every twist is quadratic).

**1.6 `ex:ellcurves:running-invariants`** (worked example; P). The invariants of the running examples (all
recomputed from the $a$-invariants; models are the global minimal ones of `ecdata`):

| curve | $[a_1,a_2,a_3,a_4,a_6]$ | $c_4$ | $c_6$ | $\Delta$ | $j$ |
|-|-|-|-|-|-|
| 11a1 | $[0,-1,1,-10,-20]$ | $496=2^4\cdot31$ | $20008$ | $-11^5$ | $-2^{12}31^3/11^5$ |
| 11a3 | $[0,-1,1,0,0]$ | $16$ | $-152$ | $-11$ | $-2^{12}/11$ |
| 20a1 | $[0,1,0,4,4]$ | $-176$ | $-2368$ | $-2^8\cdot5^2$ | $2^4\cdot11^3/5^2$ |
| 99a1 (99A1) | $[1,-1,1,-2,0]$ | $81$ | $135$ | $3^3\cdot11$ | $3^9/11$ |
| 121a1 | $[1,1,1,-30,-76]$ | $1441=11\cdot131$ | $54703$ | $-11^2$ | $-11\cdot131^3$ |
| 121c1 | $[1,1,0,-2,-7]$ | $121$ | $5203$ | $-11^4$ | $-11^2$ |
| 121c2 | $[1,1,0,-3632,82757]$ | $174361$ | $-72809693$ | $-11^8$ | $-11\cdot131^3$ |
| 121d1 | $[0,-1,1,-40,-221]$ | $1936=2^4 11^2$ | $202312$ | $-11^7$ | $-2^{12}/11$ |
| 539c1 | $[1,0,1,170,-3237]$ | $-8183$ | $2808827$ | $-7^9\cdot11^2$ | $167^3/(7^3\cdot11^2)$ |
| 726a1 | $[1,1,0,-35,-51]$ | $1705$ | $31339$ | $2^6\cdot3^3\cdot11^3$ | $5^3\cdot31^3/(2^6\cdot3^3)$ |
| 980i1 | $[0,0,0,1568,-72716]$ | $-75264$ | $62826624$ | $-2^8\cdot5\cdot7^{11}$ | $2^{19}3^3/(5\cdot7^5)$ |

The writer may add 77c1 $[1,1,0,4,11]$ ($\Delta=-7^3\cdot11^2$, same $j$ as 539c1), 140b1 $[0,0,0,32,212]$ ($\Delta=-2^8\cdot5\cdot7^5$,
same $j$ as 980i1) and 539d1 $[0,1,1,-16,-66]$ ($\Delta=-7^6\cdot11$, same $j$ as 11a3). Reference: Cremona97, `ecdata`.
Paper: the Example of Section 3, the remark on 99A1, the appendix (121a1, 726a1); the valuations $v_q(j)$ feed
$t_\ell$ (e.g. $v_7(j(539c1))=-3$, $t_3=1$; $v_7(j(980i1))=-5$, $t_5=1$).

### Section 2. The group law

**2.1 `def:ellcurves:chordtangent`** (construction and proposition; P). For $P,Q\in E(\bar K)$ the line through $P$ and $Q$
(tangent if $P=Q$) meets $E$ in a third point $R$ counted with multiplicity (a cubic in one variable with two known
roots); $P+Q$ is the third intersection of the line through $R$ and $O$, i.e. $-R$, where
$-(x,y)=(x,-y-a_1x-a_3)$. Explicit formulas: if $x_1\ne x_2$, $\lambda=\frac{y_2-y_1}{x_2-x_1}$, $\nu=\frac{y_1x_2-y_2x_1}{x_2-x_1}$; if
$P=Q$ and $2y_1+a_1x_1+a_3\ne0$, $\lambda=\frac{3x_1^2+2a_2x_1+a_4-a_1y_1}{2y_1+a_1x_1+a_3}$, $\nu=\frac{-x_1^3+a_4x_1+2a_6-a_3y_1}{2y_1+a_1x_1+a_3}$;
then $x_3=\lambda^2+a_1\lambda-a_2-x_1-x_2$, $y_3=-(\lambda+a_1)x_3-\nu-a_3$. Duplication: $x(2P)=\dfrac{x^4-b_4x^2-2b_6x-b_8}{4x^3+b_2x^2+2b_4x+b_6}$.
The $2$-torsion points $\ne O$ are the points with $2y+a_1x+a_3=0$, whose $x$-coordinates are the roots of
$4x^3+b_2x^2+2b_4x+b_6$. Reference: AEC III.2, Algorithm 2.3. Paper: background.

**2.2 `thm:ellcurves:grouplaw`** (theorem; P, with associativity from 2.3). $(E(\bar K),+)$ is an abelian group with
identity $O$ and inverse as in 2.1; for every field $K\subset L\subset\bar K$, $E(L)$ is a subgroup; $\sigma(P+Q)=\sigma P+\sigma Q$
for $\sigma\in G_K$; addition and negation are morphisms. Commutativity, identity and inverses are immediate from
the construction; associativity is 2.3 (a direct verification is possible but long; mention it). Reference:
AEC III.2.2, III.3.6 (verify). Paper: background (every group of points: $E(\Q)_{\mathrm{tors}}$, $E[\ell]$, $E(\F_q)$).

**2.3 `prop:ellcurves:pic0`** (proposition; P given Chapter 8, item 5.7). The bijection $\kappa\colon E(\bar K)\to\operatorname{Pic}^0(E)$,
$P\mapsto[(P)-(O)]$ of Chapter 8 (cited, not reproved) satisfies $\kappa(P+Q)=\kappa(P)+\kappa(Q)$ for the chord-tangent law; hence $+$
is associative. Corollary: a divisor $D=\sum n_P(P)$ is principal iff $\deg D=0$ and $\sum[n_P]P=O$ in $E$. Proof (the part
done here): the line through $P,Q$ and the vertical line through $R$ of 2.1 have divisors $(P)+(Q)+(R)-3(O)$ and
$(R)+(-R)-2(O)$, so $(P)+(Q)\sim(P+Q)+(O)$. Reference: AEC III.3.4, III.3.5 (verify). Paper:
background (and the model for Jacobians, Chapters 8 and 14).

**2.4 `ex:ellcurves:torsion-points`** (worked example; P). On 11a1, $P=(5,5)$ has order $5$:
$2P=(16,-61)$, $3P=(16,60)$, $4P=(5,-6)$, $5P=O$. On 20a1, $(-1,0)$ has order $2$, $(0,2)$ order $3$ and $(4,10)$
order $6$. On 14a1 $[1,0,1,4,-6]$, $(2,-5)$ has order $3$ and $(9,23)$ order $6$. On 27a1 $[0,0,1,0,-7]$, $(3,4)$ has
order $3$. On 99a1, $(0,0)$ has infinite order (its multiples have growing denominators; rank $1$ by `ecdata`).
All checked with the formulas of 2.1. Paper: background for torsion (Section sec:eis), and the data of 12.2.

### Section 3. Isogenies

**3.1 `def:ellcurves:isogeny`** (definition and proposition; P given Chapter 8). An isogeny $\varphi\colon E_1\to E_2$ is a
morphism with $\varphi(O)=O$; it is constant or surjective (Chapter 8). Its degree is $[\bar K(E_1):\varphi^*\bar K(E_2)]$
($\deg0:=0$), with separable and inseparable degrees; $\varphi$ is defined over $K$ if it is $G_K$-equivariant on points.
$\operatorname{Hom}(E_1,E_2)$ is an abelian group, $\End(E)$ a ring, $[m]\in\End(E)$; $\deg(\psi\circ\varphi)=\deg\psi\deg\varphi$.
Reference: AEC III.4. Paper: background (isogeny classes, Section 1; Conjecture conj:eis; Section sec:oot).

**3.2 `thm:ellcurves:isog-hom`** (theorem; S). (i) An isogeny is a group homomorphism (through 2.3: $\varphi_*$ on
$\operatorname{Pic}^0$). (ii) A nonconstant isogeny has finite kernel of order $\deg_s\varphi$; if $\varphi$ is separable, $\#\ker\varphi=\deg\varphi$,
$\varphi$ is unramified (Chapter 8, item 7.3(b), cited), and $\bar K(E_1)/\varphi^*\bar K(E_2)$ is Galois with group $\ker\varphi$ acting by translations. Reference:
AEC III.4.8, III.4.10 (verify). Paper: background.

**3.3 `thm:ellcurves:quotient`** (theorem; R). Let $\Phi\subset E(\bar K)$ be a finite subgroup. There are an elliptic curve
$E'$ and a separable isogeny $\varphi\colon E\to E'$ with $\ker\varphi=\Phi$, unique up to isomorphism of $E'$; if $\Phi$ is
$G_K$-stable (as a set), $E'$ and $\varphi$ can be taken over $K$. Write $E'=E/\Phi$. Explicit equations: Velu's formulas
(Velu 1971, add to `bib/ch09.bib`). Reference: AEC III.4.12 and Exercise 3.13 (verify). Paper: Conjecture conj:eis
("rational $\ell$-isogeny"), 9.5, 9.8.

**3.4 `thm:ellcurves:dual`** (theorem; S). For a nonconstant isogeny $\varphi\colon E_1\to E_2$ of degree $m$ there is a unique
isogeny $\hat\varphi\colon E_2\to E_1$ with $\hat\varphi\circ\varphi=[m]_{E_1}$; then $\varphi\circ\hat\varphi=[m]_{E_2}$, $\widehat{\psi\circ\varphi}=\hat\varphi\circ\hat\psi$,
$\widehat{\varphi+\psi}=\hat\varphi+\hat\psi$, $\widehat{[m]}=[m]$, $\deg\hat\varphi=\deg\varphi$, $\hat{\hat\varphi}=\varphi$; $\hat\varphi$ is defined over $K$ if $\varphi$ is. The
degree is a positive definite quadratic form on $\operatorname{Hom}(E_1,E_2)$ ($\deg(\varphi+\psi)-\deg\varphi-\deg\psi$ is bilinear because
$\widehat{\varphi+\psi}=\hat\varphi+\hat\psi$). Sketch: $\hat\varphi$ is $E_2\to\operatorname{Pic}^0(E_2)\xrightarrow{\varphi^*}\operatorname{Pic}^0(E_1)\to E_1$. Reference: AEC III.6.1,
III.6.2 (verify). Paper: background for 9.8 and for Chapter 14 ($E^\vee\to J_0(N)\to E$ is $[\degphi]$).

**3.5 `cor:ellcurves:degm`** (corollary; P given 3.4). (i) $\deg[m]=m^2$ for $m\ne0$. (ii) If $\operatorname{char}K\nmid m$ then $[m]$
is separable and $E[m]\simeq(\Z/m)^2$. (iii) If $\operatorname{char}K=p>0$ then $E[p^e]$ is $0$ for all $e$ or $\Z/p^e$ for all $e$.
Proof of (i): $\widehat{[m]}=[m]$ and $\widehat{[m]}\circ[m]=[\deg[m]]$ give $[m^2]=[\deg[m]]$; $\End(E)$ is torsion-free. (ii) from
3.2 and the structure theorem (Chapter 1): $\#E[d]=d^2$ for every $d\mid m$ forces $(\Z/m)^2$. (iii) R.
Over $\C$ there is a second proof by lattices (7.4). Reference: AEC III.6.2(d), III.6.4 (verify). Paper: Section 1.1
($E[\ell]$ two-dimensional over $\F_\ell$), Lemma lem:IV ($E[3]=T/3T$).

**3.6 `prop:ellcurves:cyclicfactor`** (proposition; P given 3.3, 3.5; $\operatorname{char}K=0$). Let $\varphi\colon E\to E'$ be a
nonconstant isogeny and $a\ge1$ the largest integer with $E[a]\subset\ker\varphi$. Then $\ker\varphi\simeq\Z/a\times\Z/ab$ for some $b\ge1$, and
$\varphi=\psi\circ[a]$ where $\psi\colon E\to E'$ is the isogeny with $\ker\psi=a\cdot\ker\varphi\simeq\Z/b$ (cyclic). If $\varphi$ is defined over
$K$, so is $\psi$ ($a\cdot\ker\varphi$ is $G_K$-stable because $[a]$ commutes with $G_K$). An isogeny over $K$ with cyclic kernel
of order $n$ is a *cyclic $n$-isogeny*; its kernel contains exactly one subgroup of each order $d\mid n$, and that
subgroup is $G_K$-stable, so a cyclic $n$-isogeny over $K$ factors into cyclic isogenies over $K$ of prime degrees.
Proof: finite subgroups of $E(\bar K)_{\mathrm{tors}}\simeq(\Q/\Z)^2$ have at most two generators (Chapter 1). Reference: elementary;
AEC III.4. Paper: 9.6, 9.8 (cyclic $27$-isogeny), 9.9.

### Section 4. Division polynomials

**4.1 `def:ellcurves:divpol`** (definition; P). $\psi_0=0$, $\psi_1=1$, $\psi_2=2y+a_1x+a_3$, $\psi_3=3x^4+b_2x^3+3b_4x^2+3b_6x+b_8$,
$\psi_4=\psi_2\bigl(2x^6+b_2x^5+5b_4x^4+10b_6x^3+10b_8x^2+(b_2b_8-b_4b_6)x+b_4b_8-b_6^2\bigr)$, and for $m\ge2$, resp. $m\ge3$,
$$\psi_{2m+1}=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3,\qquad \psi_2\psi_{2m}=\psi_m\bigl(\psi_{m+2}\psi_{m-1}^2-\psi_{m-2}\psi_{m+1}^2\bigr).$$
These lie in $\Z[a_1,\dots,a_6,x,y]$; reduce with $\psi_2^2=4x^3+b_2x^2+2b_4x+b_6$. Reference: AEC Exercise 3.7; Washington,
*Elliptic Curves: Number Theory and Cryptography*, Section 3.2 (add to `bib/ch09.bib`). Paper: Proposition prop:ns,
the appendix (`elldivpol(E, 3)` in `ns3`).

**4.2 `prop:ellcurves:divpol-deg`** (proposition; P by induction). For odd $m$, $\psi_m\in\Z[a_i][x]$ has degree $(m^2-1)/2$ and
leading coefficient $m$; for even $m$, $\psi_m/\psi_2\in\Z[a_i][x]$ has degree $(m^2-4)/2$ and leading coefficient $m/2$.
Checked for $m\le9$ on 11a1 and 99a1 with the recursion above. Reference: AEC Exercise 3.7. Paper: background
(PLAN.md scope: "degree $(m^2-1)/2$ for odd $m$").

**4.3 `thm:ellcurves:multm`** (theorem; S). For $P=(x,y)\in E$ with $mP\ne O$:
$x(mP)=x-\dfrac{\psi_{m-1}\psi_{m+1}}{\psi_m^2}(P)$, and a similar formula for $y(mP)$ with $\psi_m^3$ in the denominator; $mP=O$ iff
$\psi_m(P)=0$ (for $P\ne O$, $m\ge2$). For $m=2$ this is the duplication formula of 2.1. Sketch: induction with the
addition formulas, or comparison of divisors: $\operatorname{div}(\psi_m)=\sum_{T\in E[m]}(T)-m^2(O)$ when $\operatorname{char}K\nmid m$.
Reference: AEC Exercise 3.7; Washington EC Theorem 3.6 (verify). Paper: background.

**4.4 `cor:ellcurves:divpol-roots`** (corollary; P given 3.5 and 4.3). Let $m$ be odd with $\operatorname{char}K\nmid m$. The roots of
$\psi_m(x)$ in $\bar K$ are exactly the $x$-coordinates of the points of $E[m]\smallsetminus\{O\}$; they are simple and there are
$(m^2-1)/2$ of them. Indeed $x(P)=x(Q)$ iff $Q=\pm P$, no nonzero point of $E[m]$ has order $2$, so $P\mapsto x(P)$ is a
$G_K$-equivariant bijection $(E[m]\smallsetminus\{O\})/\{\pm1\}\to\{\text{roots}\}$, and the count $(m^2-1)/2$ equals the degree.
Paper: Proposition prop:ns.

**4.5 `prop:ellcurves:psi3`** (proposition; P). (i) $x(2P)-x(P)=-\psi_3(x)/\psi_2(P)^2$ (polynomial identity, checked
symbolically), so for $P\ne O$ not of order $2$: $3P=O$ iff $\psi_3(x(P))=0$. (ii) Let $\operatorname{char}K\ne3$. The four roots of $\psi_3$
correspond bijectively and $G_K$-equivariantly to the four lines of the $\F_3$-plane $E[3]$ (a line $\{O,P,-P\}$ goes to
$x(P)$). Hence the factorisation pattern of $\psi_3$ over $K$ is the orbit pattern of $\bar\rho_{E,3}(G_K)$ on $\mathbb P^1(\F_3)$
(Chapter 5, galois:quartic-on-lines; Chapter 1, 6.8): $\psi_3$ has a root in $K$ iff $E[3]$ has a $G_K$-stable line iff $E$ has
a $K$-rational $3$-isogeny (9.5). (iii) For $K=\Q$, $\operatorname{disc}(\psi_3)\in-3\cdot(\Q^\times)^2$: the sign of the permutation of
the four lines is $\det\bar\rho_{E,3}=\chi_{-3}$ (5.2 and Chapter 1, 5.4(ii)), so $\Q(\sqrt{\operatorname{disc}\psi_3})=\Q(\sqrt{-3})$.
Reference: elementary given the cited chapters. Paper: Proposition prop:ns (last two sentences of statement and
proof: "the four roots of the $3$-division polynomial correspond to the four lines of $\F_3^2$", "factors as two
quadratics ... irreducible otherwise", "no rational root when $E[3]$ is irreducible"), Section sec:data, Section
sec:anomaly, the appendix (`ns3`).

**4.6 `ex:ellcurves:psi3-examples`** (worked example; P, all factorisations and discriminants recomputed with sympy;
images from `ecdata`):

| curve | $\psi_3$ over $\Q$ | $\operatorname{disc}\psi_3$ | image at 3 |
|-|-|-|-|
| 11a1 | $3x^4-4x^3-60x^2-237x-21$, irreducible | $-3^3\cdot11^{10}$ | surjective |
| 121a1 | $3x^4+5x^3-177x^2-909x-1249$, irreducible | $-3^3\cdot11^4$ | surjective |
| 726a1 | $(x^2-x-74)(3x^2+8x+20)$ | $-2^{12}3^9 11^6$ | 3Ns |
| 338d1 $[1,1,0,504,-13112]$ | $(x^2+29x+1858)(3x^2-82x-172)$ | $-2^6 3^3 13^{18}$ | 3Ns |
| 20a1 | $x(3x^3+4x^2+24x+48)$ | $-2^{16}3^3 5^4$ | 3B.1.1 |
| 14a1 $[1,0,1,4,-6]$ | $(x-2)(3x+1)(x^2+2x+13)$ | $-2^{12}3^3 7^6$ | 3Cs.1.1 |
| 27a1 (CM) | $3x(x-3)(x^2+3x+9)$ | $-3^{21}$ | 3Cs.1.1 |
| 6912d1 $y^2=x^3-6x-8$ | $3(x^2-4x-2)(x^2+4x+6)$ | $-2^{18}3^9$ | 3Ns (Chapter 5 example) |

For 726a1 the quadratic factors have discriminants $297=3^3\cdot11$ and $-176=-2^4\cdot11$, so they split over $\Q(\sqrt{33})$
and $\Q(\sqrt{-11})$, and the third quadratic subfield of their compositum is $\Q(\sqrt{-3})$, as Chapter 5 (e) predicts.
For 20a1 the root $x=0$ is the rational $3$-torsion point $(0,2)$; for 14a1 the root $2$ is the rational point $(2,-5)$
and the root $-1/3$ gives the points over $\Q(\sqrt{-3})$ spanning the line $\mu_3$ (the $y$-quadratic has discriminant
$-784/27=-3\cdot(28/9)^2$). Every discriminant is $-3$ times a square, as 4.5(iii) says. Paper: Proposition prop:ns,
Section sec:anomaly (726a1), Section sec:eis (3B.1.1, 3Cs.1.1).

### Section 5. The Weil pairing, the Tate module and the Galois representations

**5.1 `thm:ellcurves:weil`** (theorem; S). Let $m\ge1$ with $\operatorname{char}K\nmid m$. There is a pairing
$e_m\colon E[m]\times E[m]\to\mu_m$ which is (i) bilinear, (ii) alternating ($e_m(T,T)=1$, hence $e_m(S,T)=e_m(T,S)^{-1}$), (iii)
nondegenerate, (iv) Galois-equivariant: $e_m(\sigma S,\sigma T)=\sigma(e_m(S,T))$ for $\sigma\in G_K$, (v) compatible:
$e_{mm'}(S,T)=e_m(m'S,T)$ for $S\in E[mm']$, $T\in E[m]$, (vi) adjoint: $e_m(S,\hat\varphi T)=e_m(\varphi S,T)$ for an isogeny
$\varphi\colon E\to E'$, $S\in E[m]$, $T\in E'[m]$. Sketch: for $T\in E[m]$ choose $g$ with $\operatorname{div}(g)=[m]^*(T)-[m]^*(O)$
(2.3); $e_m(S,T)=g(X+S)/g(X)$. Reference: AEC III.8.1 (verify). Over $\C$, 7.4 gives a direct proof of (i) to (iii) by
a determinant. Paper: Section 4.2 ($\det\rho=\chi_\ell$, $A(1)$), Lemma lem:h0 ("comparing determinants").

**5.2 `cor:ellcurves:det`** (corollary; P from 5.1). (i) For $\sigma\in G_K$ acting on $E[m]$ in an $\Z/m$-basis,
$\det=\chi_m^{\mathrm{cyc}}(\sigma)$ where $\sigma(\zeta)=\zeta^{\chi_m^{\mathrm{cyc}}(\sigma)}$ on $\mu_m$. (ii) If $E[m]\subset E(K)$ then $\mu_m\subset K$. (iii) If
$L\subset E[\ell]$ is a $G_K$-stable line, then $E[\ell]/L\simeq\Hom(L,\mu_\ell)$ as $G_K$-modules; in particular a $K$-rational point of
order $\ell$ gives an exact sequence $0\to\Z/\ell\to E[\ell]\to\mu_\ell\to0$, and the two characters on a reducible $E[\ell]$
multiply to $\bar\chi_\ell$. Proof: $e_m(\sigma S,\sigma T)=e_m(S,T)^{\det}$ for $\sigma$ acting by a matrix. Reference: AEC III.8.1.1
(verify). Paper: Proposition prop:ns ("$\det\bar\rho_{E,3}=\chi_{-3}$ cuts out $\Q(\sqrt{-3})$"), Conjecture conj:eis and
Section sec:eis ($\Z/3\oplus\mu_3$), Lemma lem:h0.

**5.3 `def:ellcurves:tate`** (definition and proposition; P given 3.5 and Chapter 1's inverse limits). $T_\ell E=\varprojlim_nE[\ell^n]$
(transition maps $[\ell]$) is a free $\Z_\ell$-module of rank $2$; $V_\ell E=T_\ell E\otimes_{\Z_\ell}\Q_\ell$; $T_\ell E/\ell^nT_\ell E\simeq E[\ell^n]$;
$V_\ell E/T_\ell E\simeq E[\ell^\infty]\simeq(\Q_\ell/\Z_\ell)^2$. For $\ell=p=\operatorname{char}K>0$, $T_pE$ is $0$ or $\Z_p$ (R). The Weil pairings assemble to
a perfect alternating $G_K$-equivariant pairing $e\colon T_\ell E\times T_\ell E\to\Z_\ell(1)$ (P from 5.1(v)). Reference: AEC III.7,
III.8. Paper: Section 1.1 ($T$, $V$), Lemma lem:IV ($T_3E$, $E[3]=T/3T$), Lemma lem:tamfactor (basis $e_1,e_2$ of $T$).

**5.4 `def:ellcurves:rho`** (definition and proposition; P). $\rho_{E,\ell}\colon G_K\to\operatorname{Aut}_{\Z_\ell}(T_\ell E)\simeq\GL_2(\Z_\ell)$ (after a choice
of basis), $\bar\rho_{E,\ell}\colon G_K\to\operatorname{Aut}(E[\ell])\simeq\GL_2(\F_\ell)$, and $\rho\bmod\ell^k$ is the action on $E[\ell^k]=T/\ell^kT$.
(i) $\rho_{E,\ell}$ is continuous: $E[\ell^n]$ is pointwise fixed by $G_{K(E[\ell^n])}$, where $K(E[\ell^n])$ (coordinates of
$\ell^n$-torsion points) is a finite Galois extension. (ii) $\det\rho_{E,\ell}=\chi_\ell^{\mathrm{cyc}}$ (5.3). (iii) An isogeny
$\varphi\colon E\to E'$ over $K$ induces an injective $G_K$-map $\varphi_\ell\colon T_\ell E\to T_\ell E'$ with $\operatorname{coker}\varphi_\ell\simeq(\ker\varphi)[\ell^\infty]$;
so $V_\ell E\simeq V_\ell E'$, and $T_\ell E\simeq T_\ell E'$ if $\ell\nmid\deg\varphi$. Reference: AEC III.7, Serre's *Abelian $\ell$-adic
representations* I.1 (SerreAbelian). Paper: Section 1.1 ($V$, $T$, $\rho$, $\bar\rho$), Theorem thm:main hypothesis (the
restriction of $\bar\rho$ to $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$, Chapter 11), Lemma lem:h0 ($\rho\bmod\ell^k$), Section 4.2 ($M_{f,\lambda}$
and $T_\ell E$ homothetic, Chapter 15).

**5.5 `cor:ellcurves:dual-T`** (corollary; P from 5.3). The Weil pairing gives $G_K$-isomorphisms
$T_\ell E\simeq\Hom_{\Z_\ell}(T_\ell E,\Z_\ell(1))=T_\ell E^\vee(1)$ and $E[\ell^k]\simeq\Hom(E[\ell^k],\mu_{\ell^k})$; equivalently
$T_\ell E^\vee\simeq T_\ell E(-1)$ and $\rho^\vee\simeq\rho\otimes(\chi_\ell^{\mathrm{cyc}})^{-1}$ (Chapter 4's $V^\vee\simeq V\otimes\det^{-1}$ in dimension two).
Consequently $\ad(T_\ell E^\vee)=\ad(T_\ell E)$ as $G_K$-modules (Chapter 4), and a lattice homothetic to $T_\ell E^\vee$ has the
same adjoint as $T_\ell E$. Paper: Section 4.2 ("the lattice $M_{f,\lambda}$ of DFG04 and $T_\ell E$ are homothetic"), which
is right up to dualising (important_notes.md point 26: the cohomology $H^1$ gives the dual; point 40: for the
optimal curve $M_{f,\lambda}=H^1(E,\Z_\ell)=\Hom(T_\ell E,\Z_\ell)$, which by this item is exactly $T_\ell E(-1)$); Chapter 18 ($T^D$).

**5.6 `cor:ellcurves:complex-conj`** (corollary; P). Let $E/\Q$, $\ell$ odd, $c$ a complex conjugation. Then $\bar\rho_{E,\ell}(c)$ has
order dividing $2$ and determinant $\chi_\ell(c)=-1$, hence eigenvalues $1,-1$, trace $0$, and is conjugate to $\operatorname{diag}(1,-1)$;
the same holds for $\rho_{E,\ell}(c)$ in $\GL_2(\Z_\ell)$. (Directly: $E(\R)[\ell]\simeq\Z/\ell$ because $E(\R)\simeq S^1$ or $S^1\times\Z/2$.)
Paper: Proposition prop:ns ("contain an element of determinant $-1$ and trace $0$ (complex conjugation)"); Chapter 11
uses it for "irreducible implies absolutely irreducible" (important_notes.md point 10).

**5.7 `conv:ellcurves:frobenius`** (convention and warning). C5 of Part 1 typeset as a `convention`: arithmetic
Frobenius in group-theoretic statements, $\rho_{E,\ell}(\Frob_p)$ with characteristic polynomial $X^2-a_pX+p$; the Euler factor
of $E$ is $\det(1-\Frob_p^{\mathrm{arith}}p^{-s}\mid V_\ell E)^{-1}=\det(1-\Frob_p^{\mathrm{geom}}p^{-s}\mid V_\ell E^\vee)^{-1}$, while
$\det(1-\Frob_p^{\mathrm{geom}}p^{-s}\mid V_\ell E)^{-1}=L_p(E,s+1)$ (by 5.5). On $\ad V$ the two conventions differ only where an
eigenvalue $q^{\pm1}$ occurs (important_notes.md point 11; the $L$-factors of the adjoint are Chapters 18, 19).

### Section 6. Endomorphisms and complex multiplication

**6.1 `thm:ellcurves:end`** (theorem; R, with P for the parts over $\C$ in 7.4). $\End_{\bar K}(E)$ has no zero divisors and
$\deg$ is a positive definite quadratic form on it; it is isomorphic to $\Z$, to an order in an imaginary quadratic field,
or (only if $\operatorname{char}K=p>0$) to a maximal order in the quaternion algebra over $\Q$ ramified exactly at $p$ and $\infty$.
Reference: AEC III.9.4 and V.3.1 (verify). Paper: background for Lemma lem:h0.

**6.2 `prop:ellcurves:normalised`** (proposition; S). Let $\operatorname{char}K=0$. The map $\alpha\mapsto[\alpha]^*\omega/\omega\in\bar K$ is an injective ring
homomorphism $\End_{\bar K}(E)\to\bar K$; with it, $\End_{\bar K}(E)\simeq\mathcal O\subset\C$ "normalised". (i) Endomorphisms defined over
$K$ map into $K$; hence $\End_\Q(E)=\Z$ for every $E/\Q$ (an imaginary quadratic integer in $\Q$ is in $\Z$). (ii) If
$\End_{\bar\Q}(E)=\mathcal O\subset F$ ($F$ imaginary quadratic) for $E/\Q$, every endomorphism is defined over $F$, and for
$\sigma\in G_\Q$ one has $\sigma\circ[\alpha]\circ\sigma^{-1}=[\sigma(\alpha)]$ on points, i.e. $[\alpha]^\sigma=[\alpha]$ if $\sigma|_F=1$ and $[\bar\alpha]$
otherwise. Sketch: $([\alpha]^\sigma)^*\omega=\sigma(\alpha)\omega$ because $\omega$ is defined over $\Q$. Reference: AEC III.5.6 (verify);
Silverman ATAEC II.2 (SilvermanATAEC). Paper: Lemma lem:h0 (via 6.4); Chapter 6, item 6.5 quotes this.

**6.3 `def:ellcurves:cm`** (definition). An elliptic curve $E$ over a field of characteristic $0$ has *complex
multiplication* (CM) if $\End_{\bar K}(E)\ne\Z$; then $\End_{\bar K}(E)\simeq\mathcal O$, an order in an imaginary quadratic field $F$, and
$E$ has CM by $\mathcal O$ (or by $F$). CM is an isogeny invariant ($\End\otimes\Q$ is: $\alpha\mapsto\varphi\alpha\hat\varphi/\deg\varphi$; P).
Paper: Conjecture conj:euler, Conjecture conj:eis, Proposition prop:ns, Lemma lem:h0, Section sec:data ("not CM").

**6.4 `thm:ellcurves:13j`** (theorem; R, numerical check P). If $E/\Q$ has CM by $\mathcal O$, then $\mathcal O$ has class number one,
so $\operatorname{disc}\mathcal O\in\{-3,-4,-7,-8,-11,-12,-16,-19,-27,-28,-43,-67,-163\}$, and $j(E)$ is respectively
$0$, $1728$, $-3375$, $8000$, $-32768$, $54000$, $287496$, $-884736$, $-12288000$, $16581375$, $-884736000$, $-147197952000$,
$-262537412640768000$; conversely each value is the $j$-invariant of a curve over $\Q$ with CM by that order.
These are $j(\tau)$ for $\tau=\frac{-1+\sqrt D}2$ or $\frac{\sqrt D}2$ (checked to $40$ digits with `mpmath.kleinj`). Examples: 27a1,
36a1 ($j=0$, $F=\Q(\sqrt{-3})$), 32a1 ($j=1728$, $F=\Q(i)$), 121b1 ($j=-32768=-2^{15}$, $F=\Q(\sqrt{-11})$), 27a2 and 27a4
($j=-12288000=-2^{15}\cdot3\cdot5^3$, order of discriminant $-27$). Reference: AEC Appendix C, Section 11 (verify the
location); Silverman ATAEC II (Theorem II.4.3 and the class number one list, verify); Cox, *Primes of the form
$x^2+ny^2$* (add to `bib/ch09.bib`). Paper: Lemma lem:h0 ("only for curves with complex multiplication by that
field"), the data sections ("not CM"); important_notes.md point 14.

**6.5 `thm:ellcurves:cm-ap`** (theorem; (i), (ii) S, rest R). Let $E/\Q$ have CM by an order in $F$, $\chi_F$ the character of
$F$. (i) $\rho_{E,\ell}\simeq\rho_{E,\ell}\otimes\chi_F$ for every $\ell$. (ii) For every prime $p$ of good reduction inert in $F$,
$a_p(E)=0$ (Deuring: the reduction is supersingular). (iii) For $p$ good and split in $F$, $a_p(E)\ne0$ (ordinary). (iv)
Every prime ramified in $F$ divides the conductor $N$ (for instance via $\rho_{E,\ell}\simeq\Ind_{G_F}^{G_\Q}\psi$ and the conductor
of an induced representation, or Deuring's identification of $L(E,s)$ with a Hecke $L$-function); hence a curve
with CM by $\Q(\sqrt{\ell^*})$ has $\ell\mid N$. (v) Conversely, if $a_p(E)=0$ for a set of primes inert in a quadratic field $F$
of density $1/2$ (all but finitely many), then $E$ has CM by $F$ (Serre's open image theorem; Chapter 11). Sketch of
(i), (ii): take $\alpha\in\mathcal O$ with $\bar\alpha=-\alpha$; by 6.2(ii), $\alpha\colon V_\ell E\to V_\ell E$ satisfies $\rho(\sigma)\alpha\rho(\sigma)^{-1}=\chi_F(\sigma)\alpha$,
an isomorphism $\rho\to\rho\otimes\chi_F$; then $\operatorname{tr}\rho(\sigma)=\chi_F(\sigma)\operatorname{tr}\rho(\sigma)$ and $a_p=\operatorname{tr}\rho(\Frob_p)=0$ when
$\chi_F(\Frob_p)=-1$ (8.6). Checked: $a_p=0$ at every good inert $p<500$ and $a_p\ne0$ at every good split $p<500$ for
27a1, 36a1, 32a1, 121b1; for all $462$ CM curves of conductor below $10{,}000$ in `ecdata`, every prime dividing
$\operatorname{disc}F$ divides $N$. Reference: AEC Appendix C.11; ATAEC II.10 (verify); Deuring 1941 (add to bib);
Serre-Tate 1968 for (iv) (add to bib) or Serre's Local Fields VI for conductors of induced representations.
Paper: Lemma lem:h0 (last sentence of statement and proof; the correct reading uses the quadratic character
$\chi_{\ell^*}$, not the cyclotomic $\chi_\ell$: important_notes.md point 5; by (iv) the CM alternative cannot occur when
$\ell\nmid N$: point 14), Conjecture conj:euler ("without complex multiplication"). Chapter 6, item 6.5 is the
number-theoretic preview of this item and cites it.

### Section 7. Elliptic curves over $\C$

**7.1 `def:ellcurves:lattice`** (definition and proposition; P). A lattice $\Lambda=\Z\omega_1+\Z\omega_2\subset\C$ ($\omega_1,\omega_2$ linearly independent
over $\R$), oriented by $\operatorname{Im}(\omega_2/\omega_1)>0$; homothety $\Lambda'=c\Lambda$; covolume $\operatorname{vol}(\Lambda)=|\operatorname{Im}(\bar\omega_1\omega_2)|$ (the
area of a fundamental parallelogram). $\sum_{\omega\in\Lambda\smallsetminus0}|\omega|^{-s}$ converges for $s>2$ (count lattice points in
annuli; RHB-style estimate). Eisenstein series $G_{2k}(\Lambda)=\sum_{\omega\ne0}\omega^{-2k}$ ($k\ge2$), $g_2=60G_4$, $g_3=140G_6$,
$\Delta(\Lambda)=g_2^3-27g_3^2$, $j(\Lambda)=1728g_2^3/\Delta$; $G_{2k}(c\Lambda)=c^{-2k}G_{2k}(\Lambda)$, so $j$ depends only on the
homothety class. Reference: AEC VI.3; DiamondShurman 1.4. Paper: background (Section 1: "the area of the period
lattice", Chapter 14). Physics aside (one sentence): a doubly periodic function is a Fourier series on a torus.

**7.2 `thm:ellcurves:wp`** (theorem; P). $\wp(z)=z^{-2}+\sum_{\omega\ne0}\bigl((z-\omega)^{-2}-\omega^{-2}\bigr)$ converges normally on compact sets away
from $\Lambda$, is even, meromorphic, $\Lambda$-periodic with double poles exactly at $\Lambda$; $\wp(z)=z^{-2}+\sum_{k\ge1}(2k+1)G_{2k+2}z^{2k}$;
$\wp'(z)^2=4\wp(z)^3-g_2\wp(z)-g_3$ (compare principal parts; Liouville); $\Delta(\Lambda)\ne0$ (the values $\wp(\omega_1/2)$, $\wp(\omega_2/2)$,
$\wp((\omega_1+\omega_2)/2)$ are the distinct roots of $4x^3-g_2x-g_3$); the field of $\Lambda$-periodic meromorphic functions is
$\C(\wp,\wp')$. Reference: AEC VI.2, VI.3 (VI.3.1, VI.3.2, VI.3.5, verify). Paper: background.

**7.3 `thm:ellcurves:cplxuniform`** (theorem; (i) P, (ii) R with two proof routes named). (i) $z\mapsto[\wp(z):\wp'(z):1]$
($z\notin\Lambda$), $0\mapsto O$, is a complex-analytic group isomorphism $\C/\Lambda\to E_\Lambda(\C)$, $E_\Lambda\colon y^2=4x^3-g_2x-g_3$,
under which $dx/y$ pulls back to $dz$ (the addition theorem of $\wp$ matches the chord-tangent law of 2.1). (ii)
(Uniformisation.) For $A,B\in\C$ with $4A^3+27B^2\ne0$ there is a unique lattice $\Lambda$ with $g_2(\Lambda)=-4A$, $g_3(\Lambda)=-4B$; so
every $E/\C$ is $\C/\Lambda$ for a lattice unique up to homothety. Routes: surjectivity of $j\colon\mathfrak H\to\C$ (Chapter 12,
valence formula), or $\Lambda=\{\int_\gamma\omega:\gamma\in H_1(E(\C),\Z)\}$ and Abel-Jacobi (Chapter 8). Reference: AEC VI.3.6,
VI.5.1 (verify). Paper: background; Section 1 (period lattice), Chapter 14.

**7.4 `prop:ellcurves:cplxisog`** (proposition; P). (i) Holomorphic maps $\C/\Lambda_1\to\C/\Lambda_2$ sending $0$ to $0$ are $z\mapsto\alpha z$
with $\alpha\Lambda_1\subset\Lambda_2$; they are group homomorphisms; isomorphisms iff $\alpha\Lambda_1=\Lambda_2$; so $E_{\Lambda_1}\simeq E_{\Lambda_2}$ iff the
lattices are homothetic. (ii) For $\alpha\ne0$ the degree is $[\Lambda_2:\alpha\Lambda_1]$, the kernel $\alpha^{-1}\Lambda_2/\Lambda_1$; $[m]$ has degree
$m^2$ and $E[m]=\frac1m\Lambda/\Lambda\simeq(\Z/m)^2$ (second proof of 3.5). (iii) $\End(\C/\Lambda)=\{\alpha:\alpha\Lambda\subset\Lambda\}$ is $\Z$ or an order in
an imaginary quadratic field, the latter iff $\tau=\omega_2/\omega_1$ is imaginary quadratic (P: $\alpha$ satisfies a monic
integral quadratic, and $\alpha\notin\R$ if $\alpha\notin\Z$). (iv) For an oriented basis, $e_m(\omega_1/m,\omega_2/m)=e^{2\pi i/m}$ up to the
sign convention C7 (AEC Chapter VI, exercises; verify the statement and the sign before printing), and $e_m$ is
$\exp(2\pi i\det(\cdot,\cdot)/m)$ on $\frac1m\Lambda/\Lambda$. Reference: AEC VI.4 (verify). Paper: background.

**7.5 `thm:ellcurves:moduli`** (theorem; P for (i), (ii); R for (iii) with forward pointer to Chapter 12). (i) Every
lattice is homothetic to $\Lambda_\tau=\Z+\Z\tau$ with $\tau=\omega_2/\omega_1\in\mathfrak H$ (oriented basis), and $\Lambda_\tau$, $\Lambda_{\tau'}$ are
homothetic iff $\tau'=\frac{a\tau+b}{c\tau+d}$ with $\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\in\SL_2(\Z)$ (change of oriented basis). So homothety classes
of lattices, isomorphism classes of $E/\C$, and $\SL_2(\Z)\backslash\mathfrak H$ are in bijection. (ii) $j(\tau):=j(\Lambda_\tau)$ is holomorphic
on $\mathfrak H$ and $\SL_2(\Z)$-invariant; $j(i)=1728$, $j(e^{2\pi i/3})=0$. (iii) $j\colon\SL_2(\Z)\backslash\mathfrak H\to\C$ is a bijection; the
standard fundamental domain $\{|\operatorname{Re}\tau|\le\frac12,|\tau|\ge1\}$; $j(\tau)=q^{-1}+744+196884q+\cdots$, $q=e^{2\pi i\tau}$ (Chapter 12).
Reference: AEC VI.4, VI.5 and Appendix C; DiamondShurman 1.1, 1.4. Paper: background (PLAN.md scope: "isomorphism
classes $=$ lattices up to homothety $=$ points of the upper half plane modulo $\SL_2(\Z)$"); Chapter 12 builds
$X_0(N)$ on this.

**7.6 `def:ellcurves:periodlattice`** (definition and proposition; S). Let $E/\Q$ be given by a global minimal model
(Chapter 10) with Neron differential $\omega=dx/(2y+a_1x+a_3)$. Its period lattice is
$\Lambda_E=\{\int_\gamma\omega:\gamma\in H_1(E(\C),\Z)\}$, and $E(\C)\simeq\C/\Lambda_E$ with $\omega\leftrightarrow dz$. (i) $\Lambda_E$ is stable under complex
conjugation; if $\Delta>0$, $\Lambda_E=\Z\omega_1+\Z\omega_2$ with $\omega_1>0$ and $\omega_2\in i\R$ (rectangular; $E(\R)$ has two components);
if $\Delta<0$, $\Lambda_E=\Z\omega_1+\Z\omega_2$ with $\omega_1>0$ and $\operatorname{Re}\omega_2=\pm\omega_1/2$ ($E(\R)$ connected). $\omega_1$ is the least positive
real period. (ii) $\operatorname{vol}(\Lambda_E)=\omega_1\operatorname{Im}\omega_2=\frac i2\int_{E(\C)}\omega\wedge\bar\omega$. (iii) Computation by the arithmetic-geometric
mean (Cremona97 Section 3.7; Cohen's *A course in computational algebraic number theory*, Algorithm 7.4.7, add
to `bib/ch09.bib`; PARI `E.omega`, `ellperiods`). (iv) Isogenous curves have commensurable period lattices
($\varphi^*\omega'=c\,\omega$, $c\in\Q^\times$, the subject of the Manin constant, Chapter 14). Reference: Cremona97 Chapter III;
AEC VI. Paper: Section 1 ("$\degphi$ is $\langle f,f\rangle$ divided by the area of the period lattice of $E$", Zagier85,
Watkins02); Chapter 14 states the exact formula.

**7.7 `ex:ellcurves:11a1-periods`** (worked example; P numerically). For 11a1 ($\Delta=-11^5<0$), by the AGM:
$\omega_1=1.2692093042795534\ldots$ (agrees with `ecdata`'s $\Omega=1.26920930427955$), $\omega_2=-\omega_1/2+1.4588166169384952\ldots\,i$,
$\operatorname{vol}(\Lambda_E)=1.8515436234559593\ldots$; $\tau=\omega_2/\omega_1$ reduced to the fundamental domain is
$-\frac12+1.1493901061232524\ldots\,i$, and $1728\,J(\tau)=-757.67263786\ldots=-122023936/161051=j(\text{11a1})$ to $40$ digits. Paper:
background for Section 1 and Chapter 14 (11a1 has $\degphi=1$).

### Section 8. Elliptic curves over finite fields

**8.1 `def:ellcurves:frobendo`** (definition and proposition; S). Let $E/\F_{\mathfrak q}$, $\mathfrak q=p^r$. The $\mathfrak q$-th power map
$\pi\colon(x,y)\mapsto(x^{\mathfrak q},y^{\mathfrak q})$ is an endomorphism of $E$ of degree $\mathfrak q$, purely inseparable, and acts on $E(\bar\F_p)$ as the
arithmetic Frobenius $\phi_{\mathfrak q}$ (C5). $E(\F_{\mathfrak q^n})=\ker(1-\pi^n)$. $1-\pi$ is separable ($(1-\pi)^*\omega=\omega\ne0$; AEC III.5.5 and
II.4.2(c), verify), so $\#E(\F_{\mathfrak q})=\deg(1-\pi)$. Put $a_{\mathfrak q}=\mathfrak q+1-\#E(\F_{\mathfrak q})$. Reference: AEC II.2, III.5, V.1. Paper:
the table of Section 1 ($a_q(E')$), Lemma lem:old ($X^2-a_p(h)X+p$), Definition def:terms ($a_q(E)$).

**8.2 `thm:ellcurves:hasse`** (theorem, Hasse; P given 3.4 and 8.1). $|a_{\mathfrak q}|\le2\sqrt{\mathfrak q}$. Proof: $\deg(m-n\pi)=m^2-a_{\mathfrak q}mn+\mathfrak qn^2\ge0$
for all $m,n\in\Z$ (positive definite quadratic form, 3.4), so the discriminant $a_{\mathfrak q}^2-4\mathfrak q\le0$. Checked for the good primes
$p<2000$ of seven running examples. Reference: AEC V.1.1. Paper: background; Chapter 2, 11.4 needs
$(q+1)^2-a^2>0$; Lemma lem:euler and the table ($\alpha,\beta$ complex conjugate of absolute value $\sqrt q$).

**8.3 `thm:ellcurves:charpoly`** (theorem; P given 5.3 and "$\deg=\det$ on $T_\ell$", which is S from the Weil pairing:
AEC III.8.6, verify). For $\ell\ne p$, the endomorphism $\pi$ acts on $T_\ell E$ with characteristic polynomial $X^2-a_{\mathfrak q}X+\mathfrak q$
($\det\pi_\ell=\deg\pi=\mathfrak q$ and $\det(1-\pi_\ell)=\deg(1-\pi)=\#E(\F_{\mathfrak q})$); $\pi^2-a_{\mathfrak q}\pi+\mathfrak q=0$ in $\End(E)$. Its roots $\alpha,\beta\in\C$
satisfy $\alpha\beta=\mathfrak q$, $\alpha+\beta=a_{\mathfrak q}$, $|\alpha|=|\beta|=\sqrt{\mathfrak q}$, and $\#E(\F_{\mathfrak q^n})=\mathfrak q^n+1-\alpha^n-\beta^n$; in particular
$\#E(\F_{\mathfrak q^2})=\mathfrak q^2+1-(a_{\mathfrak q}^2-2\mathfrak q)$; $Z(E/\F_{\mathfrak q},T)=\frac{1-a_{\mathfrak q}T+\mathfrak qT^2}{(1-T)(1-\mathfrak qT)}$. Checked on 11a1:
$\#E(\F_{p^2})=15,35,60,180$ for $p=3,5,7,13$, by direct count in $\F_{p^2}$. Reference: AEC V.2 (Theorem V.2.3.1,
verify). Paper: the table of Section 1 and Lemma lem:euler ($\alpha,\beta$ roots of $X^2-a_q(E')X+q$, "using $\alpha\beta=q$ and
$\alpha+\beta=a_q(E')$"), Lemma lem:old, Section 4.1 (stabilisations, Chapter 13).

**8.4 `def:ellcurves:supersingular`** (definition and theorem; R, with (ii) P). (i) $E/\F_{\mathfrak q}$ is supersingular iff
$E[p]=0$ iff $p\mid a_{\mathfrak q}$ iff $\End_{\bar\F_p}(E)$ is a quaternion order; otherwise ordinary. (ii) For $\mathfrak q=p\ge5$: supersingular iff
$a_p=0$ (Hasse: $|a_p|\le2\sqrt p<p$). Reference: AEC V.3.1 (verify). Paper: Lemma lem:h0 via 6.5 ($a_p=0$ at inert
primes).

**8.5 `prop:ellcurves:twistFq`** (proposition; P). Let $\mathfrak q$ be odd, $E\colon y^2=f(x)$ over $\F_{\mathfrak q}$ ($f$ a cubic) and
$E^{\mathrm{tw}}\colon \varepsilon y^2=f(x)$ with $\varepsilon$ a non-square. Then $\#E(\F_{\mathfrak q})=\mathfrak q+1+\sum_x\eta(f(x))$ with $\eta$ the quadratic
character of $\F_{\mathfrak q}^\times$, $a_{\mathfrak q}(E^{\mathrm{tw}})=-a_{\mathfrak q}(E)$, $\#E(\F_{\mathfrak q})+\#E^{\mathrm{tw}}(\F_{\mathfrak q})=2\mathfrak q+2$, and
$(\mathfrak q+1)^2-a_{\mathfrak q}^2=\#E(\F_{\mathfrak q})\cdot\#E^{\mathrm{tw}}(\F_{\mathfrak q})$. Reference: elementary (Chapter 2, 9 and 11.4). Paper: the $\mathrm I_0^*$ row of the
table ($v_\ell((q+1)^2-a_q(E')^2)=v_\ell(\#E'(\F_q))+v_\ell(\#E'^{\mathrm{tw}}(\F_q))$: a curious reading of $e_\ell$ the writer may give in one
sentence), Lemma lem:euler.

**8.6 `thm:ellcurves:frobQ`** (theorem; S, using Chapter 10). Let $E/\Q$ have good reduction at $p$ (minimal model,
$p\nmid\Delta$) and $\ell\ne p$. Then $\rho_{E,\ell}$ is unramified at $p$ and $\rho_{E,\ell}(\Frob_p)$ (arithmetic) has characteristic polynomial
$X^2-a_pX+p$ with $a_p=a_p(E)=p+1-\#\tilde E(\F_p)$, independently of the choice of $\Frob_p$ and of $\ell$. Sketch: reduction
$E[\ell^n]\to\tilde E[\ell^n]$ is injective (Chapter 10; AEC VII.3.1, verify) hence bijective by counting, and it is equivariant for
$D_p\to G_{\F_p}$; so $I_p$ acts trivially and $\Frob_p$ acts as $\pi$ (8.3). This is the easy half of Neron-Ogg-Shafarevich
(Chapter 11 states the criterion). Write $\alpha_p,\beta_p$ for the roots. Reference: AEC VII.7 (verify). Paper: Section 1.1,
the table ($\alpha,\beta$ for $E'$), Lemma lem:old ("characteristic polynomial of $\bar\rho_h(\Frob_p)$ is $X^2-a_p(h)X+p$"), Lemma
lem:h0 ($a_p=\operatorname{tr}\rho(\Frob_p)$).

**8.7 `ex:ellcurves:aptable`** (worked example; P). $a_p$ for $p<40$ (point counts on the minimal model; at bad primes
$a_p=p+1-\#\tilde E(\F_p)$ counting the singular point, which gives $1$, $-1$, $0$ for split multiplicative, nonsplit
multiplicative and additive reduction; Chapter 10):

| curve | $a_2$ | $a_3$ | $a_5$ | $a_7$ | $a_{11}$ | $a_{13}$ | $a_{17}$ | $a_{19}$ | $a_{23}$ | $a_{29}$ | $a_{31}$ | $a_{37}$ |
|-|-|-|-|-|-|-|-|-|-|-|-|-|
| 11a1 | $-2$ | $-1$ | $1$ | $-2$ | $1$ | $4$ | $-2$ | $0$ | $-1$ | $0$ | $7$ | $3$ |
| 20a1 | $0$ | $-2$ | $-1$ | $2$ | $0$ | $2$ | $-6$ | $-4$ | $6$ | $6$ | $-4$ | $2$ |
| 99a1 | $-1$ | $0$ | $-4$ | $-2$ | $-1$ | $-2$ | $2$ | $-6$ | $4$ | $-6$ | $4$ | $-6$ |
| 121a1 | $-1$ | $2$ | $1$ | $2$ | $0$ | $-1$ | $5$ | $-6$ | $2$ | $-9$ | $-2$ | $-3$ |
| 539c1 | $1$ | $-2$ | $2$ | $0$ | $1$ | $-4$ | $-4$ | $0$ | $-4$ | $-6$ | $-10$ | $-6$ |
| 726a1 | $-1$ | $-1$ | $0$ | $0$ | $0$ | $-6$ | $6$ | $-6$ | $6$ | $-6$ | $4$ | $-2$ |
| 980i1 | $0$ | $-3$ | $1$ | $0$ | $-5$ | $3$ | $1$ | $-6$ | $6$ | $-9$ | $4$ | $2$ |

(726a1, image 3Ns: $3\mid a_p$ at the good $p\equiv2\pmod3$, as $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ requires; 11a1: $a_p\equiv1+p\pmod5$, item 9.7.)
The coefficients of 11a1 agree with $q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2$ up to $q^{20}$ (Chapter 12). Paper: the Example of Section
3 (congruences between these $a_p$, Chapter 15), Lemma lem:euler.

### Section 9. Elliptic curves over $\Q$: Mordell-Weil, torsion, isogenies

**9.1 `thm:ellcurves:mordellweil`** (theorem, Mordell; R, with the outline of proof S). $E(\Q)$ is finitely generated:
$E(\Q)\simeq\Z^r\oplus E(\Q)_{\mathrm{tors}}$, $r$ the rank, $E(\Q)_{\mathrm{tors}}$ finite. Outline: weak Mordell-Weil ($E(\Q)/2E(\Q)$ finite, Chapter 17
via the Kummer map and Selmer groups) plus the descent with the canonical height. Reference: AEC VIII.6.7 (verify),
VIII.4 to VIII.9. Paper: background (ranks in Section sec:eis "all of rank $0$", Section sec:two and Watkins's
conjecture $2^{\operatorname{rank}}\mid\degphi$).

**9.2 `prop:ellcurves:torsred`** (proposition; R from Chapter 10, with the application P). For $p$ of good reduction,
reduction is injective on $E(\Q)[m]$ for $p\nmid m$, and for $p\ge3$ it is injective on all of $E(\Q)_{\mathrm{tors}}$; so
$\#E(\Q)_{\mathrm{tors}}$ divides $\#\tilde E(\F_p)$ for every good $p\ge3$. Nagell-Lutz (R): torsion points of a model with integral
coefficients have integral coordinates (with the usual caveat at $2$). Application (P): for 11a1,
$\#\tilde E(\F_3)=5$ and $\#\tilde E(\F_7)=10$, so $\#E(\Q)_{\mathrm{tors}}\mid5$, and $(5,5)$ has order $5$: $E(\Q)_{\mathrm{tors}}\simeq\Z/5$. Reference: AEC VII.3.1,
VII.3.5, VIII.7.2 (verify). Paper: Conjecture conj:eis ($v_\ell(\#E(\Q)_{\mathrm{tors}})$), Section sec:eis.

**9.3 `thm:ellcurves:mazur`** (theorem, Mazur; R). $E(\Q)_{\mathrm{tors}}$ is isomorphic to $\Z/n$ with $1\le n\le10$ or $n=12$, or to
$\Z/2\times\Z/2n$ with $1\le n\le4$; each occurs infinitely often. Data check: the torsion orders in `ecdata` below
$10{,}000$ are $1,\dots,10,12,16$ (with $16$ only from $\Z/2\times\Z/8$). Reference: Mazur77; AEC VIII.7.5 (verify). Paper:
Conjecture conj:eis ("$D\le1$ for $\ell\ge5$": $v_5$, $v_7\le1$ and no $\ell$-torsion for $\ell\ge11$; "a point of order $9$"), Section sec:eis.

**9.4 `def:ellcurves:isogclass`** (definition and theorem; P for (i), (ii); R for (iii), (iv)). (i) Being isogenous over $\Q$
is an equivalence relation (3.4); the classes are the isogeny classes. (ii) Isogenous curves have $V_\ell E\simeq V_\ell E'$ (5.4),
hence the same $a_p$ at every prime $p$ good for both (8.6), the same $L$-function (Section 11), and the same rank
($E(\Q)\otimes\Q\simeq E'(\Q)\otimes\Q$ via $\varphi$ and $\hat\varphi$); they have the same conductor (R; Chapters 10, 11) but in general different
torsion, $\Delta$, $j$, Tamagawa numbers and periods. (iii) (Faltings) Conversely, $E$ and $E'$ over $\Q$ are isogenous iff
$a_p(E)=a_p(E')$ for almost all $p$, iff $V_\ell E\simeq V_\ell E'$ for one $\ell$. (iv) An isogeny class over $\Q$ is finite, with at
most $8$ curves (Kenku); `ecdata` below $10{,}000$ has classes of sizes $1,2,3,4,6,8$. Cremona's isogeny matrix lists
the degrees of the cyclic isogenies between the curves of a class: 11a: $\begin{psmallmatrix}1&5&5\\5&1&25\\5&25&1\end{psmallmatrix}$; 20a:
$\begin{psmallmatrix}1&2&3&6\\2&1&6&3\\3&6&1&2\\6&3&2&1\end{psmallmatrix}$; 121a, 121c: one $11$-isogeny; 121d: degrees $5,5,25$; 99a, 539c, 726a: one $2$-isogeny; 980i: trivial.
Reference: Faltings 1983 (add to `bib/ch09.bib`); Kenku 1982 (add); Cremona97 Chapter III. Paper: Section 1 ("the
isogeny class of $E$", the optimal curve, Chapter 14), Conjecture conj:eis ("the number of curves in the isogeny class
of $E$ with a rational point of order $\ell$"), Section sec:oot ("trivial isogeny class").

**9.5 `prop:ellcurves:isogline`** (proposition; P given 3.3). Let $\ell$ be a prime, $E/K$, $\operatorname{char}K\ne\ell$. The $K$-rational
$\ell$-isogenies from $E$ (up to isomorphism of the target) correspond to the $G_K$-stable lines of $E[\ell]$. Hence $E[\ell]$ is
reducible as an $\F_\ell[G_K]$-module iff $E$ has a $K$-rational $\ell$-isogeny. A $K$-rational point of order $\ell$ gives one
(its span), but not conversely: 11a2 and 539a1 have rational $5$- resp. $3$-isogenies and no rational $5$- resp.
$3$-torsion. If $E[\ell]$ is reducible, $\bar\rho_{E,\ell}^{\mathrm{ss}}=\psi_1\oplus\psi_2$ with $\psi_1\psi_2=\bar\chi_\ell$ (5.2(iii)). Data check (`ecdata`, conductor
below $10{,}000$, $\ell=3,5,7$): for curve number $1$ of every non-CM class, a Borel or split-Cartan label at $\ell$ (Chapter
11) occurs iff its row of the isogeny matrix has a degree divisible by $\ell$ ($114{,}126$ pairs; the $59$ mismatches are all
CM curves, for which `ecdata` lists no label at $\ell$). Reference: AEC III.4.12, Exercise 3.13. Paper: Conjecture conj:eis
("with a rational $\ell$-isogeny"), Section sec:eis, Conjecture conj:euler and Theorem thm:quant ("$E[\ell]$
irreducible"), Proposition prop:ns ("$E[3]$ irreducible", "no rational root").

**9.6 `thm:ellcurves:mazurkenku`** (theorem, Mazur and Kenku; R). (i) If $E/\Q$ has a rational $\ell$-isogeny with $\ell$ prime,
then $\ell\in\{2,3,5,7,11,13,17,19,37,43,67,163\}$ (Mazur78). (ii) If $E/\Q$ has a rational cyclic $n$-isogeny, then
$n\le19$ or $n\in\{21,25,27,37,43,67,163\}$ (Mazur, Kenku). (iii) The values $n=19,27,43,67,163$ occur only for CM
curves; for $n=27$ the curves have $j=-2^{15}\cdot3\cdot5^3=-12288000$ (CM by the order of discriminant $-27$; in `ecdata`
the cyclic $27$-isogeny joins 27a2 and 27a4, both with this $j$). Data check: the isogeny degrees occurring below
conductor $10{,}000$ are $1$ to $16$, $18$, $19$, $21$, $25$, $27$, $37$, $43$, $67$. Reference: Mazur78; Kenku's papers
on $X_0(N)$ for $N=39,65,91,125,169$ and the summary in Kenku 1982 (add to `bib/ch09.bib`; the writer should cite a
survey with exact statement, e.g. the table in Lozano-Robledo, Math. Ann. 357 (2013), after checking it). Paper:
Conjecture conj:eis, Section sec:eis, 9.8.

**9.7 `prop:ellcurves:zlmul`** (proposition; P). Let $\ell$ be odd and $E/\Q$ with a rational point $P_0$ of order $\ell$. (i) In a basis
$(P_0,Q)$ of $E[\ell]$, $\bar\rho_{E,\ell}=\begin{psmallmatrix}1&*\\0&\bar\chi_\ell\end{psmallmatrix}$ (5.2(iii)). (ii) The following are equivalent: the sequence
$0\to\Z/\ell\to E[\ell]\to\mu_\ell\to0$ splits; $E[\ell]\simeq\Z/\ell\oplus\mu_\ell$ as $G_\Q$-modules; the image of $\bar\rho_{E,\ell}$ is conjugate to
$\{\operatorname{diag}(1,d):d\in\F_\ell^\times\}$ (label $\ell$Cs.1.1: 3Cs.1.1 of order $2$, 5Cs.1.1 of order $4$; Chapter 1, 6.10, Chapter 11);
$E$ has two rational $\ell$-isogenies, with kernels $\Z/\ell$ and $\mu_\ell$. (iii) In that case $\#\tilde E(\F_p)\equiv0$ and $a_p\equiv1+p\pmod\ell$
for every good $p\ne\ell$ (trace of $\operatorname{diag}(1,p)$); the congruence $a_p\equiv1+p$ already follows from (i). Examples (all checked):
14a1, 19a1, 26a1 and 27a1 (CM) have $E[3]\simeq\Z/3\oplus\mu_3$; 11a1 has $E[5]\simeq\Z/5\oplus\mu_5$ ($a_p\equiv1+p\pmod5$ for all good $p<500$;
its two $5$-isogenies have kernels $\Z/5$ and $\mu_5$; $\text{11a1}/\mu_5$ contains the rational group $E[5]/\mu_5\simeq\Z/5$, so it is 11a3
(torsion $\Z/5$), and $\text{11a1}/(\Z/5)\simeq$ 11a2 (torsion $1$)); 20a1 has a
rational $3$-torsion point with non-split $E[3]$ (3B.1.1). Reference: elementary. Paper: Conjecture conj:eis
("$[E[3]\simeq\Z/3\oplus\mu_3]$"), Section sec:eis ("the split Cartan image 3Cs.1.1": see Part 8, N1).

**9.8 `prop:ellcurves:no27`** (proposition; P given 9.6(iii); this is important_notes.md point 17, decided to live
here). Let $E/\Q$ be without CM and $E[3]\simeq\Z/3\oplus\mu_3$. Then $E(\Q)$ has no point of order $9$; so $E(\Q)[3^\infty]\simeq\Z/3$ and
$v_3(\#E(\Q)_{\mathrm{tors}})=1$. Proof: suppose $P\in E(\Q)$ has order $9$. Then $3P$ is a rational point of order $3$, so $\langle3P\rangle$ is the
line $\Z/3$ ($\mu_3$ has no nonzero rational point since $\chi_{-3}\ne1$), and $\langle P\rangle\cap E[3]=\langle3P\rangle$ meets $\mu_3$ trivially.
Let $\varphi\colon E\to E'=E/\mu_3$ (rational, 3.3) and $\hat\varphi\colon E'\to E$ its dual; $\varphi\circ\hat\varphi=[3]$ gives
$\hat\varphi(E'[3])\subset\ker\varphi=\mu_3$, with equality since $\#\hat\varphi(E'[3])=9/\#\ker\hat\varphi=3$. Put $C=\hat\varphi^{-1}(\langle P\rangle)\subset E'$: it is
$G_\Q$-stable of order $\#\ker\hat\varphi\cdot9=27$. If $C\supset E'[3]$ then $\mu_3=\hat\varphi(E'[3])\subset\langle P\rangle$, a contradiction; so $C$ has
cyclic $3$-part of order $27$, i.e. $C$ is cyclic (3.6), and $E'\to E'/C$ is a rational cyclic $27$-isogeny. By 9.6(iii) $E'$ has
CM, hence so has $E$ (6.3), a contradiction. Corollary (with Mazur, 9.3): for a non-CM $E$ with a rational
$3$-isogeny, $v_3(\#E(\Q)_{\mathrm{tors}})+[E[3]\simeq\Z/3\oplus\mu_3]\le2$, so the bound "$D\le2$ for $\ell=3$" of Conjecture conj:eis follows
from its first bound and is not an additional conjecture; also $v_\ell(\#E(\Q)_{\mathrm{tors}})\le1$ for $\ell=5,7$ and $=0$ for $\ell\ge11$.
Data check: the $264$ curves of conductor below $10{,}000$ with image 3Cs.1.1 have torsion of order $3$ or $6$; the
six curves there with a point of order $9$ (54b3, 714i1, 1482l1, 1554n1, 1890r3, 6942n1) all have image 3B.1.1, as
Section sec:eis reports for its range. Reference: the argument of important_notes.md point 17 (and Chapter 21
outline, A1.13); Mazur77, 9.6. Paper: Conjecture conj:eis, Section sec:eis ("We have not proved that the two cannot
coexist, so the bound $D\le2$ is part of the conjecture"), Open question 4.

**9.9 `lem:ellcurves:primetol`** (lemma; P given 3.6, 5.4, 9.5; important_notes.md point 27). Let $E/\Q$ and $\ell$ a prime with
$E[\ell]$ irreducible. (i) Every rational isogeny $\varphi\colon E\to E'$ factors as
$\varphi=\psi\circ[a]$ with $\ker\psi$ cyclic of order prime to $\ell$ (by 3.6, a cyclic kernel of order divisible by $\ell$ contains a
rational subgroup of order $\ell$, contradicting 9.5). (ii) Hence $\psi$ induces $G_\Q$-isomorphisms $E[\ell^n]\simeq E'[\ell^n]$ and
$T_\ell E\simeq T_\ell E'$; all curves of the isogeny class have the same $\rho_{E,\ell}$ up to conjugation in $\GL_2(\Z_\ell)$, the same $\bar\rho$,
the same $\ad T$, the same $h_\ell(E)$ and the same $\ell$-adic Tamagawa factors and Selmer groups of $\ad T$; and $E'[\ell]$ is
irreducible. (iii) In particular the hypotheses and all $\ell$-adic quantities of Theorem thm:main and Conjecture
conj:euler except $\degphi$ itself do not depend on which curve of the class is the optimal one; $t_\ell(E,q)=v_\ell(-v_q(j))$
is also unchanged, because $\ell$-power-free isogenies change $v_q(j)$ at a potentially multiplicative prime by a factor
prime to $\ell$ (Tate curve, Chapter 10; state with forward pointer). Reference: elementary. Paper: Section 1
(optimality), Theorem thm:qual ("the $X_0(N)$-optimal curve in the isogeny class of $E$"), Section 3 ($E_0$), Section
sec:oot, important_notes.md point 27.

**9.10 `cor:ellcurves:trivialclass`** (corollary; P). If the isogeny class of $E/\Q$ has only one curve, then $E$ has no
rational $\ell$-isogeny for any prime $\ell$, so $E[\ell]$ is irreducible for every $\ell$ (including $\ell=2$), and $E$ is the
$X_0(N)$-optimal curve of its class (Chapter 14). Example: 980i1. Paper: Section sec:oot ("kept those with trivial
isogeny class (so that the curve is optimal and $E[\ell]$ is irreducible for every $\ell$)").

### Section 10. Quadratic twists

**10.1 `def:ellcurves:twist`** (definition and proposition; P). Let $\operatorname{char}K\ne2$ and $d\in K^\times$. For a model
$y^2=x^3+a_2x^2+a_4x+a_6$ put $E^{(d)}\colon y^2=x^3+da_2x^2+d^2a_4x+d^3a_6$ (equivalently $dy^2=x^3+a_2x^2+a_4x+a_6$ via $(x,y)\mapsto(dx,d^2y)$).
For a general model complete the square first: $\eta^2=4x^3+b_2x^2+2b_4x+b_6$ becomes $\eta^2=4x^3+db_2x^2+2d^2b_4x+d^3b_6$, and
$y^2=x^3+db_2x^2+8d^2b_4x+16d^3b_6$ is an integral model when the $a_i$ and $d$ are integral. $E^{(d)}$ depends only on
$d\bmod(K^\times)^2$ up to $K$-isomorphism; $E^{(1)}\simeq E$, $(E^{(d)})^{(d')}\simeq E^{(dd')}$; $\psi\colon E^{(d)}\to E$, $(x,y)\mapsto(x/d,y/d^{3/2})$ is an
isomorphism over $K(\sqrt d)$ with $\psi^\sigma=[\chi_d(\sigma)]\circ\psi$. Twists in general are classified by $H^1(G_K,\operatorname{Aut}E)$ (R; AEC X.2,
X.5). Reference: AEC X.2, X.5 (Proposition X.5.4, verify). Paper: Lemma lem:twist (ii) (the twist
$y^2=x^3+q^*a_2x^2+q^{*2}a_4x+q^{*3}a_6$), Section 1.4 ($E^{(q)}$), Theorem thm:twist and thm:quant ($E_S$).

**10.2 `prop:ellcurves:twistinv`** (proposition; P, checked symbolically and on examples). (i) For the first model of
10.1, $c_4(E^{(d)})=d^2c_4$, $c_6(E^{(d)})=d^3c_6$, $\Delta(E^{(d)})=d^6\Delta$, $j(E^{(d)})=j(E)$; for the integral model of a general curve the
same holds after the change $u=1/2$ (factors $2^4$, $2^6$, $2^{12}$). (ii) Conversely, if $j(E)=j(E')\ne0,1728$ then $E'\simeq E^{(d)}$ over
$K$ with $d=c_6(E')c_4(E)/(c_6(E)c_4(E'))$. (iii) **The twist by $q$ and the twist by $q^*$** ($q$ an odd prime) are different
curves when $q\equiv3\pmod4$: they differ by the twist by $-1$, which changes the sign of $c_6$ and is ramified at $2$.
The invariants of the twist by $q^*$ are $q^{*2}c_4$, $q^{*3}c_6$, $q^{*6}\Delta$; the $q$-adic valuations are the same as for the
twist by $q$, which is all Lemma lem:twist uses (important_notes.md point 29). Example (checked): $\text{121a1}^{(-11)}\simeq$ 121c2
(conductor $121$), while $\text{121a1}^{(11)}\simeq$ 1936k2 (conductor $1936=2^4\cdot11^2$). Further checked identifications:
$\text{11a1}^{(-11)}\simeq$ 121d2, $\text{11a3}^{(-11)}\simeq$ 121d1, $\text{11a2}^{(-11)}\simeq$ 121d3, $\text{539c1}^{(-7)}\simeq$ 77c1, $\text{980i1}^{(-7)}\simeq$ 140b1,
$\text{11a1}^{(-7)}\simeq$ 539d2, $\text{11a3}^{(-7)}\simeq$ 539d1, $\text{20a1}^{(-1)}\simeq$ 80b1. Paper: Lemma lem:twist (ii) ("the twist has a model with
invariants $q^2c_4$, $q^3c_6$, $q^6\Delta$ and the same $j$-invariant"), the Example of Section 3, Definition def:terms ("Both terms
are invariant under quadratic twist", see 10.7).

**10.3 `thm:ellcurves:twistgal`** (theorem; P). For $E/K$, $d\in K^\times$ and $\ell\ne\operatorname{char}K$: $\rho_{E^{(d)},\ell}\simeq\rho_{E,\ell}\otimes\chi_d$, via
$\psi_\ell\colon T_\ell E^{(d)}\to T_\ell E$ ($\psi(\sigma P)=\chi_d(\sigma)\sigma(\psi(P))$ from $\psi^\sigma=[\chi_d(\sigma)]\circ\psi$). Consequences: $\bar\rho_{E^{(d)},\ell}=\bar\rho_{E,\ell}\otimes\chi_d$,
$E^{(d)}[2]\simeq E[2]$, $\ad\rho$ unchanged (Chapter 4, 7.1(iii)), $\det$ unchanged; $E[\ell]$ is irreducible iff $E^{(d)}[\ell]$ is. Paper:
Lemma lem:euler ("$V=V'\otimes\chi_q$", "$\ad V=\ad V'$"), proof of Theorem thm:main ("$\ad T$ is unchanged by the twist"),
Theorem thm:qual (b), (c) ("$\bar\rho_{E',3}=\bar\rho\otimes\chi$"), Theorem thm:quant ("$\bar\rho\otimes\chi_S$ is irreducible"), Remark after
thm:quant ("adjoint lattices ... coincide").

**10.4 `cor:ellcurves:twistap`** (corollary; P). Let $E/\Q$, $d\in\Q^\times$ with $\Q(\sqrt d)$ of discriminant $D$, and $p$ a prime of good
reduction for $E$ with $p\nmid D$. Then $E^{(d)}$ has good reduction at $p$ (Chapter 10) and $a_p(E^{(d)})=\chi_d(p)a_p(E)$,
$\chi_d(p)=\bigl(\frac Dp\bigr)$. Elementary proof for odd $p\nmid d\Delta$: $\#E(\F_p)=p+1+\sum_x\eta(f(x))$ and the substitution $x=dx'$
gives $a_p(E^{(d)})=\eta(d)a_p(E)$ (8.5). General proof: 10.3 and 8.6. Checked for all good $p<400$ (including $p=2$ where
allowed): 121d2 versus 11a1 ($\chi_{-11}$), 121c2 versus 121a1, 77c1 versus 539c1 ($\chi_{-7}$), 140b1 versus 980i1, 539d1
versus 11a3, 121d1 versus 11a3. Reference: AEC X.2; elementary. Paper: Lemma lem:twist (iii) and Theorem thm:twist
("$a_p(f)=\chi_S(p)a_p(g)$ for $p\nmid D$"), the Example of Section 3 ("$f_{11a}\otimes\chi_{-11}$ is the form of 121d"), Theorem thm:qual
(b), (c), PLAN.md scope ("$a_p(E^{(d)})=\chi_d(p)a_p(E)$ for $p$ not dividing $2d$").

**10.5 `prop:ellcurves:twistgood`** (proposition; P given 10.4). Let $q$ be an odd prime at which $E/\Q$ has type $\mathrm I_0^*$, so
that $E'=E^{(q^*)}$ has good reduction at $q$ (Chapter 10; this is the paper's "twist of good reduction"). (i)
$V_\ell E\simeq V_\ell E'\otimes\chi_q$ with $V_\ell E'$ unramified at $q$ (10.3, 8.6). (ii) Any other twist $E^{(q^*d)}$ with $q\nmid D$ has good reduction
at $q$ and $a_q(E^{(q^*d)})=\chi_d(q)a_q(E')=\pm a_q(E')$; so $a_q(E')^2$, the pair $\{\alpha/\beta,\beta/\alpha\}$ and $(q+1)^2-a_q(E')^2$ depend only on
$E$ and $q$, not on the choice of the twist; this is why the table may say "the twist of good reduction". (iii)
Example: 539d1 has type $\mathrm I_0^*$ at $7$ and $E'=\text{539d1}^{(-7)}\simeq$ 11a3, $a_7(\text{11a})=-2$, $(7+1)^2-4=60$, so
$e_3(\text{539d1},7)=v_3(6)+v_3(60)=2=v_3(\degphi)$ ($\degphi=72$). Paper: the table of Section 1 and the abstract (type $\mathrm I_0^*$),
Lemma lem:euler, Theorem thm:quant ($S$ contains the $\mathrm I_0^*$ primes; $E_S$ good at them).

**10.6 `def:ellcurves:compositetwist`** (definition and proposition; P). For a finite set $S$ of odd primes,
$\chi_S=\prod_{q\in S}\chi_q$ is the character of $\Q(\sqrt{d_S})$ with $d_S=\prod_{q\in S}q^*$ (a fundamental discriminant, $\equiv1\pmod4$), of
conductor $\prod_{q\in S}q$, unramified outside $S$ (Chapters 2, 6); $E_S:=E^{(d_S)}=E\otimes\chi_S$ is obtained by successive twists in any
order. $a_p(E_S)=\chi_S(p)a_p(E)$ for $p\notin S$ good. Paper: Theorem thm:twist and Theorem thm:quant ($E_S$, $\chi_S$, $D=\prod q$),
the remark after thm:twist.

**10.7 `rem:ellcurves:twistinvariance`** (remark; P). Under every quadratic twist: $j$, hence $v_q(j)$ and
$t_\ell(E,q)=v_\ell(-v_q(j))$ (when $v_q(j)<0$), and $\ad\rho_{E,\ell}$ are unchanged; $a_q$, $\Delta$, the Kodaira type at a prime where the
twist ramifies, and the naive Euler factor change. So $e_\ell(E,q)$, the ratio of the true to the naive adjoint
factor, is not invariant under a twist ramified at $q$ (important_notes.md point 15): 11a1 has type $\mathrm I_5$ at $11$ and
$e_3=0$, its twist 121d2 has type $\mathrm I_5^*$ and $e_3=v_3(11^2-1)=1$ (and likewise 11a3, $\mathrm I_1$, versus 121d1, $\mathrm I_1^*$; types
from Chapter 10). It is invariant under twists unramified at $q$. Paper: Definition def:terms (last sentence),
Section 1.4.

### Section 11. The $L$-function

**11.1 `def:ellcurves:Lfunction`** (definition and proposition; P for (i) to (iii), R for (iv)). Let $E/\Q$ have conductor $N$
(Chapter 10) and minimal model; for every prime $p$ put $a_p=p+1-\#\tilde E(\F_p)$ ($\tilde E$ the reduction, singular point
included), so $a_p\in\{1,-1,0\}$ for $p\mid N$ according as the reduction is split multiplicative, nonsplit multiplicative or
additive. (i) $L(E,s)=\prod_{p\nmid N}(1-a_pp^{-s}+p^{1-2s})^{-1}\prod_{p\mid N}(1-a_pp^{-s})^{-1}=\sum_{n\ge1}a_nn^{-s}$ converges absolutely for
$\operatorname{Re}s>3/2$ (Hasse, 8.2: $|a_n|\le d(n)\sqrt n$). (ii) $a_{mn}=a_ma_n$ for coprime $m,n$; $a_{p^{k+1}}=a_pa_{p^k}-pa_{p^{k-1}}$ for $p\nmid N$;
$a_{p^k}=a_p^k$ for $p\mid N$. (iii) For $p\ne\ell$ the local factor is $\det(1-\Frob_p^{\mathrm{arith}}p^{-s}\mid V_\ell E^{I_p})^{-1}$ (C5): at good $p$ by
8.6; at bad $p$ the statement is Chapter 11 (dimension of $V^{I_p}$ is $1$ or $0$, the paper's $\delta_p$). Isogenous curves have
the same $L$-function (9.4); $L(E^{(d)},s)$ has the same local factors as the twist $\sum\chi_d(n)a_nn^{-s}$ at the primes
$p\nmid ND$ (10.4). (iv) (Modularity, Chapter 14; Chapter 19) $L(E,s)=L(f_E,s)$ for the newform $f_E$ of level $N$, it has an
analytic continuation to $\C$ and a functional equation under $s\mapsto2-s$. Example: 11a1, $L(E,s)=\sum a_nn^{-s}$ with
$a_1,\dots,a_{13}=1,-2,-1,2,1,2,-2,0,-2,-2,1,-2,4$. Reference: AEC C.16 (verify), Cremona97 Chapter II, DiamondShurman
8.8 (verify). Paper: Section 1 ("$f=f_E$ ... newform attached to it"), Section 1.1 ($\delta_p$; the naive versus true
adjoint factors are Chapter 19), Lemma lem:old (multiplicativity, the recursion).

### Section 12. Labels and the running examples

**12.1 `conv:ellcurves:labels`** (convention and facts; R for the data). (i) A Cremona label $N\,c\,k$ consists of the
conductor $N$, an isogeny-class code $c$ (a, b, ..., z, ba, bb, ...) and the number $k$ of the curve in its class. In
Cremona's tables curve number $1$ of each class is the $X_0(N)$-optimal curve, with the single exception of the class
990h, whose optimal curve is 990h3 $=[1,-1,1,-1568,-4669]$ (`ecdata`'s `degphi` file lists the modular degree $1728$ of
990h with this equation); optimality is established in the tables for $N\le400000$ and for most classes beyond (the
paper, Section 6; Chapter 14). Cremona's book (Cremona97) and ARS12 print the class code in capitals: 99A1 is
99a1. (ii) LMFDB labels $N.c\,k$ use a different ordering both of the classes and of the curves in a class, so the
same curve can have different letters and numbers; correspondence (from `ecdata`'s `alllabels` file): 11a1 $=$ 11.a2,
11a2 $=$ 11.a1, 11a3 $=$ 11.a3, 14a1 $=$ 14.a6, 20a1 $=$ 20.a4, 27a1 $=$ 27.a3, 77c1 $=$ 77.c2, 99a1 $=$ 99.a2, 121a1 $=$ 121.a2,
121c1 $=$ 121.c2, 121c2 $=$ 121.c1, 121d1 $=$ 121.d3, 140b1 $=$ 140.b1, 539c1 $=$ 539.d2, 539d1 $=$ 539.a3, 726a1 $=$ 726.b2,
980i1 $=$ 980.b1. The LMFDB number $1$ is not the optimal curve in general. The writer must not describe the LMFDB's
ordering rules beyond "different from Cremona's" unless checked against the LMFDB documentation. Reference:
Cremona97, CremonaBook (same work), LMFDB. Paper: every label (Section 3 Example, the remark on 99A1, the appendix,
Section sec:data).

**12.2 `ex:ellcurves:running`** (worked example table; invariants P (1.6), data R from `ecdata`; Kodaira types from Chapter
10 and the Chapter 21 outline's Tate algorithm). The paper's curves:

| curve | $N$ | rank | $E(\Q)_{\mathrm{tors}}$ | class (degrees) | $\degphi$ | non-surjective $\bar\rho_\ell$ (`ecdata`) | types (Ch. 10) | role in the paper |
|-|-|-|-|-|-|-|-|-|
| 11a1 | $11$ | $0$ | $\Z/5$ | 11a: $5,5,25$ | $1$ | 5Cs.1.1 | $\mathrm I_5$ at $11$ | congruent form in thm:qual (b), (c) at $\ell=3$ |
| 20a1 | $2^2\cdot5$ | $0$ | $\Z/6$ | 20a: $2,3,6$ | $1$ | 2B, 3B.1.1 | $\mathrm{IV}^*$ at $2$, $\mathrm I_2$ at $5$ | congruent form at $\ell=5$ for 980i1 |
| 121a1 | $11^2$ | $0$ | $0$ | 121a: $11$ | $6$ | 11B.1.6 | $\mathrm{II}$ at $11$ | thm:qual (b), appendix `rule` |
| 121c1, 121c2 | $11^2$ | $0$ | $0$ | 121c: $11$ | $6$ | 11B.1.7, 11B.1.5 | $\mathrm{IV}$, $\mathrm{IV}^*$ at $11$ | 121c2 $=\text{121a1}^{(-11)}$ |
| 121d1 | $11^2$ | $0$ | $0$ | 121d: $5,5,25$ | $24$ | 5B.4.1 | $\mathrm I_1^*$ at $11$ | $f_{11a}\otimes\chi_{-11}$; 121d1 $=\text{11a3}^{(-11)}$ |
| 539c1 | $7^2\cdot11$ | $1$ | $\Z/2$ | 539c: $2$ | $288=2^5 3^2$ | 2B | $\mathrm I_3^*$ at $7$, $\mathrm I_2$ at $11$ | thm:qual (c), $\ell=3$ |
| 980i1 | $2^2\cdot5\cdot7^2$ | $0$ | $0$ | trivial | $2880=2^6 3^2 5$ | none | $\mathrm{IV}^*$ at $2$, $\mathrm I_1$ at $5$, $\mathrm I_5^*$ at $7$ | thm:qual (c), $\ell=5$ |
| 726a1 | $2\cdot3\cdot11^2$ | $1$ | $\Z/2$ | 726a: $2$ | $144=2^4 3^2$ | 2B, 3Ns | $\mathrm I_6$, $\mathrm I_3$, $\mathrm{III}$ at $2,3,11$ | 3Ns example, appendix |
| 99a1 (99A1) | $3^2\cdot11$ | $1$ | $\Z/2$ | 99a: $2$ | $4$ | 2B | $\mathrm{III}$ at $3$, $\mathrm I_1$ at $11$ | $\degphi=4$ versus $r_E=12$ |

Supporting curves: 77c1 ($N=77$, $\degphi=6$, $=\text{539c1}^{(-7)}$), 140b1 ($N=140$, $\degphi=60$, $=\text{980i1}^{(-7)}$), 539d1 ($\mathrm I_0^*$ at
$7$, $\degphi=72$, $=\text{11a3}^{(-7)}$), 14a1 ($E[3]\simeq\Z/3\oplus\mu_3$), 338d1 and 6912d1 (3Ns), 27a1, 32a1, 36a1, 121b1 (CM).
Note that 539c1, 726a1 and 99a1 have rank $1$. Reference: Cremona97 and `ecdata` (`allcurves`, `allisog`, `degphi`,
`galrep`, `alllabels`). Paper: the Example of Section 3, the remark on 99A1 (ARS12 Table 1: $r_E=12$, not recomputed
here), the appendix (121a1, 726a1), Section sec:anomaly (726a1), Section sec:eis.

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2, stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1.1 ($V,T,\rho,\bar\rho$); def:terms ($j$, $v_q(j)$, $a_q$, twist invariance); the table ($E'$, $a_q(E')$, $\alpha,\beta$); Section 1.4 and lem:twist (ii); lem:euler ($V=V'\otimes\chi_q$); thm:twist, thm:quant ($E_S$); thm:qual and the Section 3 Example (twists, labels, $a_p$); lem:h0 (CM); prop:ns ($\psi_3$, $\det$, complex conjugation); conj:eis and sec:eis (torsion, isogenies, $\Z/3\oplus\mu_3$, item 9.8); Section 1 (isogeny class, period lattice); sec:oot (trivial class); the appendix (`ellinit`, `elldivpol`) | 40 |
| 1 | Weierstrass equations and their invariants | conventions C1 to C8 as `convention` environments; 1.1 to 1.6; the invariants table; `paperlink` for def:terms ($v_q(j)$) and lem:twist (ii) | 190 |
| 2 | The group law | 2.1 to 2.4; a figure in words (chord and tangent); `paperlink` for torsion in sec:eis | 150 |
| 3 | Isogenies | 3.1 to 3.6; `warning` that "isogenous" means over $\Q$ unless stated | 180 |
| 4 | Division polynomials | 4.1 to 4.6; the factorisation table (`booktabs`); `paperlink` for prop:ns, sec:data, the appendix `ns3` | 160 |
| 5 | The Weil pairing, the Tate module and the Galois representations | 5.1 to 5.7; `convention` on Frobenius (5.7); `paperlink` for Section 1.1, Section 4.2 (point 26), prop:ns | 170 |
| 6 | Endomorphisms and complex multiplication | 6.1 to 6.5; the table of the 13 $j$-invariants with discriminants; `warning` on $\chi_\ell$ versus $\chi_{\ell^*}$ in lem:h0 (points 5, 14) | 150 |
| 7 | Elliptic curves over $\C$ | 7.1 to 7.7; the 11a1 numbers; RHB aside (Fourier series on a torus); `paperlink` for Section 1 and Chapter 14 | 210 |
| 8 | Elliptic curves over finite fields | 8.1 to 8.7; the $a_p$ table; `paperlink` for the table of Section 1 and lem:euler ($\alpha,\beta$) | 160 |
| 9 | Elliptic curves over $\Q$: Mordell-Weil, torsion, isogenies | 9.1 to 9.10; 9.8 with full proof and a `paperlink` to conj:eis and sec:eis (point 17); 9.9 with a `paperlink` to optimality (point 27) | 200 |
| 10 | Quadratic twists | 10.1 to 10.7; `warning` on $q$ versus $q^*$ (point 29) and on curve-level versus class-level twist identifications; `paperlink` for lem:twist, lem:euler, thm:twist, thm:quant, the Section 3 Example | 170 |
| 11 | The $L$-function | 11.1; forward pointers to Chapters 14 and 19 | 70 |
| 12 | Labels and the running examples | 12.1, 12.2; the big table; GP one-liners in `lstlisting` (`ellinit`, `ellglobalred`, `elltors`, `ellisomat`, `elldivpol`) with a pointer to Chapter 22 | 120 |
| 13 | Exercises | the 17 exercises of Part 4 | 130 |
| 14 | Notes and references | Silverman AEC and ATAEC, Cremona97, Washington EC, Cox, DiamondShurman, Husemoller, Knapp, MilneEC, Mazur77, Mazur78, Kenku, Faltings, Velu, Serre (SerreAbelian), Cohen (AGM); which theorem numbers were cited and checked | 40 |
| | **total** | | **2,140** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| Weierstrass equations (general and short) | 1.1, 1.2 |
| $b_2,b_4,b_6,b_8,c_4,c_6,\Delta,j$; discriminant and smoothness | 1.1, 1.2, 1.6 |
| changes of coordinates $(u,r,s,t)$ and the transformation of $c_4,c_6,\Delta$ | 1.3, 1.4 |
| the group law (chord-tangent; associativity via Riemann-Roch) | 2.1, 2.2, 2.3 |
| the group of points over any field | 2.2, 2.4 |
| isogenies: definition, degree, separable isogenies and kernels | 3.1, 3.2, 3.3, 3.6 |
| the dual isogeny; $\deg[m]=m^2$ | 3.4, 3.5, 7.4 |
| structure of $E[m]$ ($\Z/m\times\Z/m$ when char $\nmid m$) | 3.5, 7.4 |
| division polynomials; degree $(m^2-1)/2$ for odd $m$ | 4.1, 4.2, 4.3, 4.4 |
| the 3-division polynomial, degree 4, roots $=$ $x$-coordinates of the four lines of $E[3]$ | 4.5, 4.6 |
| Weil pairing: nondegenerate, alternating, Galois-equivariant; $\det=$ cyclotomic | 5.1, 5.2, 5.3 |
| Tate module $T_\ell E$ (free of rank 2) and $V_\ell E$ | 5.3, 5.5 |
| the Galois action: $\rho_{E,\ell}$ and $\bar\rho_{E,\ell}$ | 5.4, 5.6, 5.7 |
| endomorphism rings ($\Z$, imaginary quadratic order, quaternion order) | 6.1, 6.2, 7.4(iii) |
| complex multiplication; the 13 $j$-invariants; $a_p=0$ at inert primes | 6.3, 6.4, 6.5, 8.4 |
| curves over $\C$: lattices, $\wp$, uniformisation, periods | 7.1, 7.2, 7.3, 7.4 |
| the period lattice $\Lambda_E$ of a curve over $\Q$ and its area | 7.6, 7.7 |
| isomorphism classes $=$ lattices up to homothety $=$ $\SL_2(\Z)\backslash\mathfrak H$ | 7.4, 7.5 |
| curves over finite fields: Frobenius endomorphism, $a_p=p+1-\#E(\F_p)$ | 8.1, 8.7 |
| the Hasse bound | 8.2 |
| characteristic polynomial $X^2-a_pX+p$ on $T_\ell E$; $\alpha\beta=p$ | 8.3, 8.6 |
| Mordell-Weil, rank and torsion | 9.1, 9.2 |
| Mazur's torsion theorem | 9.3 |
| isogenies over $\Q$ and isogeny classes (finite; Cremona's class labels) | 9.4, 12.1 |
| rational $\ell$-isogenies and reducibility of $E[\ell]$; rational $\ell$-torsion | 9.5, 9.6, 5.2(iii) |
| the structure $\Z/3+\mu_3$ | 9.7, 9.8 |
| quadratic twists: definition, model $y^2=x^3+da_2x^2+d^2a_4x+d^3a_6$ | 10.1 |
| effect on $c_4,c_6,\Delta$ ($d^2,d^3,d^6$), same $j$ | 10.2 |
| $a_p(E^{(d)})=\chi_d(p)a_p(E)$; $\rho_{E^{(d)},\ell}=\rho_{E,\ell}\otimes\chi_d$ | 10.3, 10.4, 10.6 |
| $L(E,s)$ by its Euler product with the bad factors; continuation stated | 11.1 |
| Cremona and LMFDB labels (11a1, 121a1, 539c1, 980i1, 726a1, 99A1 explained) | 12.1, 12.2 |
| Section 6 row: $\rho_{E,\ell}$, $\bar\rho$, $T_\ell E$, $V_\ell E$, $E[\ell]$ (with Chapters 4, 5, 11) | 5.3, 5.4, 5.5, 5.6 |
| Section 6 row: the twist $E'$ of good reduction, $a_q(E')$, quadratic twists and their invariants (with Chapter 10) | 8.3, 10.1, 10.2, 10.5 |
| Section 6 row: 3-division polynomial, its factorisation pattern (with Chapters 5, 11) | 4.4, 4.5, 4.6 |
| Section 6 row: Eisenstein case, rational $\ell$-isogeny, $\Z/3+\mu_3$, torsion (with Chapters 11, 14) | 9.3, 9.5, 9.6, 9.7, 9.8 |
| Section 6 row: the worked examples 11a1, 20a1, 121a1, 539c1, 980i1, 726a1, 99A1 | 1.6, 4.6, 8.7, 10.2, 12.2 |
| hook: Lemma lem:twist (ii) (models and invariants of twists; $q$ versus $q^*$) | 10.1, 10.2 |
| hook: Lemma lem:h0 (CM and $a_p=0$) | 6.2, 6.4, 6.5, 8.4 |
| hook: Proposition prop:ns (3-division polynomial; $\det\bar\rho_3=\chi_{-3}$; complex conjugation) | 4.5, 4.6, 5.2, 5.6 |
| hook: Definition def:terms ($v_q(j)$; twist invariance) | 1.3, 1.6, 10.7 |
| hook: the twist $E'$ of good reduction and $a_q(E')$ in the table of Section 1 | 8.3, 8.5, 10.5 |
| hook: Conjecture conj:eis (torsion, isogeny class, $\Z/3+\mu_3$) | 9.3, 9.4, 9.7, 9.8 |
| hook: Section 1.1 ($V,T,\rho,\bar\rho$) | 5.3, 5.4 |
| also: Lemma lem:euler ($V=V'\otimes\chi_q$, $\alpha\beta=q$) | 8.3, 10.3, 10.5 |
| also: Theorems thm:twist, thm:quant ($E_S$, $\chi_S$) | 10.4, 10.6 |
| also: Theorem thm:qual and the Section 3 Example (twists by $-11$, $-7$; labels; $a_p$) | 8.7, 10.2, 10.4, 12.2 |
| also: Lemma lem:old ($X^2-a_pX+p$, multiplicativity of $a_n$) | 8.3, 8.6, 11.1 |
| also: Section 4.2 ($T^D$, $M_{f,\lambda}$ versus $T_\ell E$, point 26) | 5.3, 5.5 |
| also: Section 1 (isogeny class, optimal curve, area of the period lattice) | 7.6, 7.7, 9.4, 12.1 |
| also: Section sec:oot (trivial isogeny class) and point 27 | 9.9, 9.10 |
| also: the appendix (`ellinit`, `elldivpol`, `ns3`) | 1.1, 4.5, 12.1 |
| also: what Chapters 1, 2, 4, 5, 6, 21 assume from Chapter 9 (Part 5) | 3.5, 4.4, 4.5, 5.2, 5.4, 6.2, 6.5, 8.2, 8.5, 10.3, 10.4, 9.8 |

### 4.2 Exercises (Section 13 of the chapter), graded from easy to harder

1. Compute $b_2,b_4,b_6,b_8,c_4,c_6,\Delta,j$ for 11a1 $[0,-1,1,-10,-20]$; verify $4b_8=b_2b_6-b_4^2$, $1728\Delta=c_4^3-c_6^2$ and
   $j=-2^{12}\cdot31^3/11^5$ (1.1, 1.6).
2. From 1.3 show that $v_q(j)=3v_q(c_4)-v_q(\Delta)$ is independent of the model, and that $v_q(\Delta)$ changes by multiples of $12$.
   Deduce that a model with $v_q(\Delta)<12$ is minimal at $q$ (the converse direction is Chapter 10).
3. Using 2.1, check that $(5,5)$ on 11a1 has order $5$ and list its multiples. With $\#\tilde E(\F_3)=5$ and $\#\tilde E(\F_7)=10$ and
   9.2, show $E(\Q)_{\mathrm{tors}}\simeq\Z/5$. Do the same for 20a1 ($\Z/6$).
4. Compute $\psi_3$ for 20a1 and 14a1, find their rational roots and the corresponding $3$-torsion points, and explain the
   factorisation patterns $1+3$ and $1+1+2$ by the orbits on the four lines (4.5, 9.7).
5. Check the paper's claim (Proposition prop:ns, Section sec:anomaly) for 726a1: $\psi_3=(x^2-x-74)(3x^2+8x+20)$; the two
   quadratic fields are $\Q(\sqrt{33})$ and $\Q(\sqrt{-11})$ and the third quadratic subfield of their compositum is $\Q(\sqrt{-3})$;
   and $3\mid a_p$ for the good primes $p\equiv2\pmod3$, $p<40$ (use 8.7).
6. Check the paper's claim (Example of Section 3) that the twist of 121a1 by $-11$ lies in the class 121c with
   $\Delta=-11^8$: compute the twisted model by 10.1, its $c_4,c_6$, and identify it with 121c2 by 10.2(ii). Then twist by
   $+11$ and show the result is not isomorphic over $\Q$ to any curve of conductor $121$ (it is 1936k2): the point of
   important_notes.md point 29.
7. Check the paper's claim that $f_{11a}\otimes\chi_{-11}$ is the form of 121d: verify $a_p(\text{121d1})=\chi_{-11}(p)a_p(\text{11a1})$ for $p\le50$
   by point counting. Show from $j$-invariants that 121d1 is the twist of 11a3, not of 11a1, and explain why the
   $a_p$ cannot see the difference (9.4).
8. Check the paper's claim that the twist of 539c1 by $-7$ has conductor $77$ and type $\mathrm I_3$ at $7$: show that it is
   77c1 (same $j=167^3/(7^3\cdot11^2)$), with $v_7(\Delta)=3$ against $9$ for 539c1 (Chapter 10 for the types).
9. For 11a1 and $p=3,5,7,13$ compute $\#E(\F_{p^2})$ from $a_p$ by 8.3 and compare with a direct count ($15,35,60,180$).
   Show $|\alpha|=\sqrt p$.
10. Prove 8.5. Using it, check the paper's $\mathrm I_0^*$ term on 539d1: $E'=$ 11a3, $a_7=-2$, $e_3(E,7)=v_3(6)+v_3(60)=2=v_3(72)$,
    and show that the value does not depend on which twist of good reduction is used (10.5).
11. Show that $a_p(\text{27a1})=0$ for the primes $p\equiv2\pmod3$, $p\le50$, and $a_p(\text{121b1})=0$ for $p$ inert in $\Q(\sqrt{-11})$, $p\le50$,
    and explain both by 6.5. Compute $j\bigl(\frac{1+\sqrt{-163}}2\bigr)$ numerically and compare with 6.4.
12. Use the Weil pairing to show that complex conjugation acts on $E[\ell]$ ($\ell$ odd) with eigenvalues $1,-1$, and that a rational
    point of order $\ell$ forces $E[\ell]/(\Z/\ell)\simeq\mu_\ell$ (5.2, 5.6).
13. Show $a_p(\text{11a1})\equiv1+p\pmod5$ for every good $p$ and check it for $p<100$; explain by $E[5]\simeq\Z/5\oplus\mu_5$ (9.7). Which of the
    two $5$-isogenous curves has a rational $5$-torsion point, and why?
14. Check the claim of 9.8 (important_notes.md point 17) in detail: prove that a non-CM curve with $E[3]\simeq\Z/3\oplus\mu_3$ has no
    rational point of order $9$, and deduce that the bound "$D\le2$ for $\ell=3$" of Conjecture conj:eis follows from its
    first bound and Mazur's theorem.
15. Check the paper's statement (Section sec:oot) that a curve with trivial isogeny class is optimal and has $E[\ell]$
    irreducible for every $\ell$ (9.10). Show more generally (9.9) that if $E[\ell]$ is irreducible then $T_\ell E\simeq T_\ell E'$ for all $E'$ in
    the class.
16. For $\Lambda=\Z+\Z i$ and $\Lambda=\Z+\Z e^{2\pi i/3}$ show $g_3=0$, resp. $g_2=0$, hence $j=1728$, resp. $0$, and compute $\End$. For 11a1,
    compute $\omega_1$ by the AGM (formula of 7.6(iii)) and check that the reduced $\tau$ gives $j(\tau)=j(E)$ (7.7).
17. Using the `alllabels` file of `ecdata`, translate 11a1, 539c1, 726a1, 980i1 into LMFDB labels. Explain why Cremona's
    curve number $1$ is the optimal curve while the LMFDB's number $1$ need not be, and look up the exception 990h.

## 5. Dependencies and forward pointers

Results from other chapters used here (by chapter label only):
* Chapter 1 (`ch:groups`): finite abelian groups (structure; $\#E[d]=d^2$ for all $d\mid m$ forces $(\Z/m)^2$), $\GL_2(\Z/m)$,
  $\GL_2(\Z_\ell)$ and inverse limits (its 7.4), the four lines of $\F_3^2$ (5.3), $\det=$ sign on lines (5.4(ii)), Borel subgroups (5.5),
  the orbit table and Sutherland labels (6.8, 6.10), complex-conjugation elements (6.9).
* Chapter 2 (`ch:rings`): finite fields, the quadratic character $\eta$ of $\F_{\mathfrak q}^\times$, Kronecker symbols, $q^*$ and $\chi_q$ (C5), $v_p$.
* Chapter 3 (`ch:modules`): $\Z_\ell$, free modules of finite rank, inverse limits of $\Z/\ell^n$-modules, Pontryagin duality
  ($E[\ell^\infty]$ versus $T_\ell E$).
* Chapter 4 (`ch:reps`): twisting by characters, $\ad(V\otimes\chi)=\ad V$, $V^\vee\simeq V\otimes\det^{-1}$ in dimension two,
  semisimplification.
* Chapter 5 (`ch:galois`): Galois theory of a polynomial (galois:galois-group-polynomial, galois:quartic-on-lines,
  galois:discriminant), profinite groups and continuity, the cyclotomic character, complex conjugation, quadratic
  characters of $G_K$.
* Chapter 6 (`ch:ant`): imaginary quadratic orders and class number one (statements), splitting of $p$ in $\Q(\sqrt d)$, the
  Frobenius element $\Frob_p$, $D_p$ and $I_p$, the arithmetic/geometric convention (its 3.7), its CM preview 6.5.
* Chapter 7 (`ch:local`, outlined in parallel): only the words "unramified at $p$", $I_p\subset D_p\simeq G_{\Q_p}$ (also in
  Chapter 6).
* Chapter 8 (`ch:curves`): projective plane and smooth plane curves, function fields, divisors and $\operatorname{Pic}^0$, Riemann-Roch,
  Weierstrass model of a genus-one curve with a point (its 5.6), $\operatorname{Pic}^0$ bijection (its 5.7), degree and
  separability of morphisms, unramified morphisms between genus-one curves (its 7.3(b)), differentials, the
  Frobenius morphism, compact Riemann surfaces, $H_1$ and Abel-Jacobi.
* Background (PLAN.md Section 2): complex analysis (Liouville, Laurent series, meromorphic functions, the residue
  theorem for the $\wp$-function), linear algebra (quadratic forms, Cauchy-Schwarz for 8.2), real analysis (convergence
  of lattice sums).

Black boxes imported from later chapters (stated with a forward `\Cref`, never used in the proof of an earlier item
of the chapter except 8.6, 9.2 and 9.9(iii), which say so): minimal models, conductor, Kodaira types, injectivity of
reduction on prime-to-$p$ torsion, the Tate curve (Chapter 10); Neron-Ogg-Shafarevich, mod $\ell$ images and their labels
(Chapter 11); the fundamental domain and the bijectivity of $j$ (Chapter 12); modularity, optimal curves, modular
degree, Manin constant (Chapter 14); analytic continuation of $L(E,s)$ (Chapter 19).

Forward pointers (chapters that use this one):
* Chapter 10 (`ch:reduction`): Weierstrass data and coordinate changes (1.1 to 1.3) for minimal models and Tate's
  algorithm; twists and their invariants (10.1, 10.2) for Lemma lem:twist (i), (ii); $\#\tilde E(\F_p)$ and $a_p$ at bad primes
  (8.7, 11.1); the Tate curve's $E_q[\ell^t]$ uses $E[\ell^t]$ (3.5, 5.3); 9.9(iii).
* Chapter 11 (`ch:galrep`): $\rho$, $\bar\rho$, $\det=\chi_\ell$, complex conjugation (5.2 to 5.6); the division polynomial (4.5, 4.6) for
  Proposition prop:ns; CM (6.5) and twists (10.3) for Lemma lem:h0; rational isogenies and $\Z/\ell\oplus\mu_\ell$ (9.5 to 9.8) for the
  Eisenstein case and the labels 3B.1.1, 3Cs.1.1; 8.6 (easy half of Neron-Ogg-Shafarevich).
* Chapter 12 (`ch:modforms`): lattices, $\SL_2(\Z)\backslash\mathfrak H$, $j(\tau)$ (7.1 to 7.5); 11a1's coefficients (8.7).
* Chapter 13 (`ch:hecke`): $X^2-a_pX+p$ and the recursion (8.3, 11.1); twisting newforms matches 10.4.
* Chapter 14 (`ch:moddeg`): isogeny classes, labels and optimality convention (9.4, 9.9, 12.1), the dual isogeny (3.4), the
  period lattice and its area (7.6, 7.7), $L(E,s)$ (11.1), torsion (9.3) for Mazur's Eisenstein-ideal results.
* Chapter 15 (`ch:modgalrep`): $\rho_{E,\ell}$ versus $\rho_{f,\lambda}$, $T_\ell E$ versus $M_{f,\lambda}$ (5.5, important_notes.md points 26, 40), twisting
  (10.3, 10.4) in Theorem thm:qual (b), (c).
* Chapters 17, 18 (`ch:galcoh`, `ch:blochkato`): $E[n]$ and the Kummer sequence, $T(1)$, $T^D$ (5.3, 5.5).
* Chapter 19 (`ch:lfunctions`): $L(E,s)$, the Frobenius convention (5.7), $\alpha,\beta$ (8.3), the $\mathrm I_0^*$ factor via 8.5 and 10.5.
* Chapters 21, 22 (`ch:paper`, `ch:computation`): every hook of Part 0, the running examples table (12.2), 9.8 for
  Conjecture conj:eis, the PARI commands.
* Chapters 1, 2, 4, 5, 6 already point here for: $E[m]\simeq(\Z/m)^2$ and $T_\ell E$ (Chapter 1), $\#E(\F_q)=q+1-a_q$, Hasse and twists
  (Chapter 2), twists $\rho\otimes\chi_d$ and the Weil pairing (Chapter 4), $\det\rho_{E,\ell}=\chi_\ell$ and the roots of $\psi_3$ (Chapter 5),
  CM and $a_p=0$ (Chapter 6). All are delivered: 3.5, 5.3, 8.1, 8.2, 10.1 to 10.4, 5.2, 4.4, 4.5, 6.2, 6.5.

## 6. Notes for the writer

Pitfalls and conventions:
* **Characteristic.** Short Weierstrass forms and the $\operatorname{Aut}$ computation need $\operatorname{char}K\ne2,3$; the general formulas of 1.1
  work in all characteristics. Over $\Q$ say once that "a model" means one with the general $a_i$, because Cremona's
  minimal models have $a_1,a_3\ne0$ in general (121a1, 726a1, 99a1).
* **Twists of general models.** Never twist $[a_1,a_2,a_3,a_4,a_6]$ by multiplying $a_2,a_4,a_6$ directly unless $a_1=a_3=0$;
  complete the square first (10.1). The scaling $u=2$ in the integral model multiplies $c_4,c_6,\Delta$ by $2^4,2^6,2^{12}$; the
  minimal model of the twist must then be recomputed (Chapter 10). $E^{(d)}$ depends on $d$ mod squares; $\chi_d$ has
  conductor $|D|$, not $|d|$.
* **$q$ versus $q^*$ (point 29).** The paper's twist is by $\Q(\sqrt{q^*})$; its invariants are $q^{*2}c_4$, $q^{*3}c_6$, $q^{*6}\Delta$. When
  $q\equiv3\pmod4$ the twist by $q$ is a different curve, ramified at $2$ (121a1: $-11$ gives 121c2, $+11$ gives 1936k2).
* **Curve versus class.** A twist of a curve is a curve, a twist of a class is a class. The paper and the Chapter 21
  outline sometimes say "the twist of 11a1 is 121d1"; the twist of 11a1 is 121d2 ($\mathrm I_5^*$ at $11$), that of 11a3 is 121d1
  ($\mathrm I_1^*$); the twist of 121a1 is 121c2, not 121c1; the twist of 11a1 by $-7$ is 539d2. Statements about $a_p$, $L$, $V_\ell$
  and (for $\ell$ prime to the isogeny degrees) $T_\ell$ are class-level; statements about $j$, $\Delta$, types, torsion and
  $v_q(j)$ are curve-level (Part 8, B2).
* **Frobenius (C5, 5.7).** $\pi$ on $\tilde E$ is the arithmetic Frobenius. $\det(1-\Frob^{\mathrm{arith}}X\mid V_\ell E)=1-a_pX+pX^2$, while
  $\det(1-\Frob^{\mathrm{geom}}X\mid V_\ell E)=1-\frac{a_p}pX+\frac1pX^2$. Do not write "the geometric Frobenius on $V_\ell E$ has eigenvalues
  $\alpha,\beta$" (that is the slip recorded in important_notes.md B1).
* **Weil pairing sign (C7).** State Silverman's definition; the comparison with $e^{2\pi i/m}$ over $\C$ has a sign that
  differs between sources: check before printing.
* **Division polynomials.** Normalisations differ ($\psi_2=2y+a_1x+a_3$ here and in PARI; some books use $2y$ for short
  models). PARI's `elldivpol(E,3)` is $\psi_3$ with leading coefficient $3$; "irreducible" means irreducible in $\Q[x]$. A $2+2$
  factorisation detects the image $N_s(\F_3)$ only for $E[3]$ irreducible and non-CM; CM curves can give $2+2$ (121b1,
  Chapter 21 outline A1.12) and reducible $E[3]$ gives a linear factor.
* **Mazur's theorems.** Keep the torsion theorem (Mazur77), the prime-degree isogeny theorem (Mazur78) and the cyclic
  $n$-isogeny list (Mazur and Kenku) apart, and say which $n$ occur only for CM curves; 9.8 uses only "$n=27$ forces CM".
* **Uniformisation.** Do not prove 7.3(ii) via the surjectivity of $j$ if Chapter 12 proves that surjectivity by the
  valence formula and cites Chapter 9: one of them must be a reference. Recommended: Chapter 9 states 7.3(ii) with
  reference (R) and names both routes.
* **Period lattice.** Use the Neron differential of the global minimal model (Chapter 10); `ecdata`'s `allbsd` column
  $\Omega$ equals $\omega_1$ for 11a1 ($\Delta<0$); for $\Delta>0$ check whether the column is $\omega_1$ or $2\omega_1$ before quoting it. The area
  $\operatorname{vol}(\Lambda_E)$ is what Chapter 14's formula uses; do not confuse it with $\Omega$.
* **Optimality convention.** "Curve number 1 is optimal" is a property of Cremona's labelling (exception 990h), not of
  the LMFDB's; the LMFDB class letters also differ (539c $=$ 539.d, 726a $=$ 726.b, 980i $=$ 980.b).
* **Labels at $\ell$.** The image labels (3Ns, 3Cs.1.1, 3B.1.1, 5Cs.1.1, ...) are Chapter 11's; use them here only in
  tables, with the intrinsic description (Chapter 1, 6.10; important_notes.md point 3).
* **Theorem numbers.** Every AEC/ATAEC number in Part 2 marked "(verify)" was recalled, not checked against the book;
  only AEC V.1.1 (Hasse) is quoted without that mark. Print section numbers if in doubt.
* Bibliography to add to `bib/ch09.bib` (complete entries, checked): Velu 1971 (C. R. Acad. Sci. Paris 273), Faltings 1983
  (Invent. Math. 73), Kenku 1982 (J. Number Theory 15), Deuring 1941 (Abh. Math. Sem. Hamburg 14), Serre-Tate 1968
  (Ann. of Math. 88), Washington's *Elliptic Curves: Number Theory and Cryptography* (2nd ed., 2008), Cox's *Primes of
  the form $x^2+ny^2$*, Cohen's *A course in computational algebraic number theory*, and optionally
  Lozano-Robledo 2013. Check every entry before adding.

What to leave to other chapters (and not do here):
* Chapter 8: Riemann-Roch, existence of the Weierstrass model, the $\operatorname{Pic}^0$ bijection, unramifiedness of isogenies,
  Jacobians.
* Chapter 10: minimality, Tate's algorithm, Kodaira types, conductor, the formal group, the Tate curve, Lemma lem:twist (i),
  (ii) on types (Chapter 9 only supplies the models and invariants).
* Chapter 11: images, Neron-Ogg-Shafarevich in full, Proposition prop:ns and Lemma lem:h0 in full (with points 1, 5, 6,
  9, 10, 33), the Ind $\psi$ over $\F_9$ issue (point 33), Serre's open image theorem.
* Chapter 12: modular forms, the fundamental domain, $j$'s $q$-expansion; Chapter 14: modularity, $X_0(N)$, optimal curves,
  the modular degree, the Manin constant, points 39 to 41; Chapter 19: the analytic theory of $L(E,s)$ and of the adjoint.

How the relevant important_notes.md points are handled:
* **Point 14** (CM by $\Q(\sqrt{\ell^*})$ forces $\ell\mid N$): 6.5(iv), stated (R) with the data check ($462$ CM curves below conductor
  $10{,}000$, no exception) and a `paperlink` to Lemma lem:h0.
* **Point 15** ($e_\ell$ not twist-invariant): 10.7, with the corrected example pairs 11a1/121d2 and 11a3/121d1.
* **Point 17** (the rational cyclic $27$-isogeny): **decided: Chapter 9**, item 9.8, with full proof. Reason: every
  ingredient (isogenies and duals, quotients by finite subgroups, cyclic factorisation, the Weil pairing for $\mu_3$, the
  CM list for $X_0(27)$, Mazur's torsion theorem) is in this chapter, and the statement is about torsion and isogenies,
  not about images. Chapter 11 restates it in the language of the label 3Cs.1.1 with a `\Cref{ch:ellcurves}`; Chapters
  14 and 21 cite it.
* **Point 26 and point 40** ($M_{f,\lambda}$ versus $T_\ell E$): 5.5 supplies $H^1(E,\Z_\ell)=\Hom(T_\ell E,\Z_\ell)\simeq T_\ell E(-1)$ exactly.
* **Point 27** (optimality irrelevant at $\ell$ when $E[\ell]$ is irreducible): 9.9, proved.
* **Point 29** ($q$ versus $q^*$): 10.2(iii), with the 121a1 example.
* **Point 33** ($\bar\rho=\Ind\psi$ only over $\F_9$): not in this chapter's scope; 4.6 only reads lines over $\F_3$.
* Points 5, 6 (the character in Lemma lem:h0): 6.5 states the CM facts for the quadratic character and a `warning`
  says the cyclotomic $\chi_\ell$ is not a quadratic character; the proof of Lemma lem:h0 is Chapter 11's.

## 7. Verification log (computations done for this outline)

Scripts in `/tmp/ch09/scripts` (`ec.py` helper; `check1.py` to `check9.py`); data in `/tmp/ch09/data` downloaded from
the `ecdata` GitHub repository (`allcurves`, `allisog`, `degphi`, `galrep`, `allbsd`, `alllabels`, all for conductors
$0$ to $9{,}999$). The LMFDB API was not reachable (captcha), so LMFDB labels come from `alllabels`.
* Symbolic (sympy, generic $a_i$): $4b_8=b_2b_6-b_4^2$; $1728\Delta=c_4^3-c_6^2$; the completed square; the short form
  $108^2\eta^2=X^3-27c_4X-54c_6$ with $X=36x+3b_2$; every transformation formula of 1.3 (by substitution); the twist
  scalings $d^2,d^3,d^6$; $x(2P)-x(P)=-\psi_3/\psi_2^2$; the curve with prescribed $j_0$ (1.4).
* Division polynomials: degrees and leading coefficients for $m=2,\dots,9$ on 11a1 and 99a1 (4.2); factorisations and
  discriminants of $\psi_3$ for the eight curves of 4.6.
* Invariants of all curves in 1.6, 4.6, 12.2 from their $a$-invariants.
* Group law: orders of the points in 2.4.
* Point counts: $a_p$ of 8.7 (and at bad primes), Hasse for good $p<2000$ on seven curves, $\#E(\F_{p^2})$ for 11a1, CM
  vanishing for 27a1, 36a1, 32a1, 121b1 ($p<500$), $a_p\equiv1+p$ for 11a1 mod $5$ and 14a1 mod $3$, the twist relations of 10.4
  ($p<400$, also $p=2$ where allowed), the Section 3 congruences (121a1 versus $\chi_{-11}\cdot$11a1 mod 3, 539c1 versus
  $\chi_{-7}\cdot$11a1 mod 3, $p<1000$; 980i1 versus $\chi_{-7}\cdot$20a1 mod 5, $3\le p<1000$), the $\eta$-product for 11a1 up to $q^{20}$.
* Twist identifications of 10.2 by comparing $j$ and $c_6c_4'/(c_6'c_4)$ against all curves of the target conductors.
* mpmath: the thirteen CM $j$-values as $1728J(\tau)$; the periods, area and reduced $\tau$ of 11a1 (AGM, Cohen 7.4.7 shape),
  $j(\tau)=j(E)$ to $40$ digits; $\omega_1$ agrees with `allbsd`.
* `ecdata`: torsion orders, class sizes, isogeny degrees, the 27a isogeny matrix and $j$-values, label/isogeny
  consistency at $\ell=3,5,7$, 3Cs.1.1 versus $9$-torsion, the six curves with a point of order $9$ (all 3B.1.1), CM curves
  and conductors, the 990h exception, modular degrees and images of the running examples, LMFDB labels.
* Not recomputed: Kodaira types at $2$ and $3$ (taken from the Chapter 21 outline's Tate algorithm), $r_E=12$ for 99A1
  (ARS12), anything beyond conductor $10{,}000$.

## 8. Points for important_notes.md

New points about the paper in this chapter's area (not already recorded; each checked as stated):

* **N1. Section sec:eis: "the split Cartan image 3Cs.1.1".** Problem: 3Cs.1.1 is not the split Cartan subgroup but its
  subgroup $\{\operatorname{diag}(1,\pm1)\}$ of order $2$ (the image when $E[3]\simeq\Z/3\oplus\mu_3$); the full split Cartan image is the label
  3Cs (order $4$), whose curves have no rational $3$-torsion (e.g. 539a2, torsion trivial). Fix: "the image 3Cs.1.1
  (inside a split Cartan subgroup, fixing a nonzero vector), i.e. $E[3]\simeq\Z/3\oplus\mu_3$". Confidence: high (`ecdata` below
  $10{,}000$: all $264$ curves labelled 3Cs.1.1 have a rational point of order $3$; Chapter 1, 6.10). Expository.
* **N2. Lemma lem:twist (ii), proof, the $\mathrm I_0\leftrightarrow\mathrm I_0^*$ sentence (addendum to point 29).** Problem: for the twisted model
  $y^2=x^3+q^*a_2x^2+q^{*2}a_4x+q^{*3}a_6$ the cubic of Tate's algorithm is $T^3+\varepsilon a_2T^2+a_4T+\varepsilon a_6$ with $\varepsilon=q^*/q$, not
  $T^3+a_2T^2+a_4T+a_6$ as written. Its roots are $\varepsilon$ times those of the latter, so "distinct roots mod $q$" is unaffected.
  Fix: "whose cubic $T^3+\varepsilon a_2T^2+a_4T+\varepsilon a_6$, $\varepsilon=q^*/q$, has distinct roots modulo $q$ because $T^3+a_2T^2+a_4T+a_6$ does".
  Confidence: high (one-line substitution $T=\varepsilon S$). Expository.
* No other new problem was found in the paper's statements about Weierstrass data, twists, torsion, isogenies, the
  3-division polynomial or CM; the Example of Section 3 (twists, labels, congruences, modular degrees), the
  appendix's 121a1 model, and Section sec:eis's claims on 3Cs.1.1 and $9$-torsion were all consistent with `ecdata`
  in the range checked.

Book-internal inconsistencies found:
* **B1 extension (Frobenius on $V_\ell E$).** The Chapter 21 outline, C2(b), says that with the geometric Frobenius
  $L_p(V_\ell E,s)=(1-a_pp^{-s}+p^{1-2s})^{-1}$ and $\det(1-\Frob^{\mathrm{geom}}X\mid V)=(1-\alpha X)(1-\beta X)$. Both are wrong: with the geometric
  Frobenius on $V_\ell E$ the factor is $(1-\frac{a_p}pp^{-s}+\frac1pp^{-2s})^{-1}=L_p(E,s+1)$; the stated formula holds for $V_\ell E^\vee=H^1$ (or
  with the arithmetic Frobenius on $V_\ell E$). Nothing on $\ad V$ changes. Chapter 9 fixes the convention in C5 and 5.7.
* **B2. Curve-level twist identifications.** important_notes.md point 15 says the twist of 11a1 by $\chi_{-11}$ has type $\mathrm I_1^*$; in
  fact $\text{11a1}^{(-11)}=$ 121d2 has type $\mathrm I_5^*$ ($v_{11}(\Delta)=11$); $\mathrm I_1^*$ is 121d1 $=\text{11a3}^{(-11)}$. The value $e_3=v_3(120)=1$ is
  the same, so the point stands. Likewise the Chapter 21 outline (A1.1, B4 item 6, Section 9 "11a1 twisted by $-7$ is
  539d1", the verification line "exact twist relations 121a1/121c1, 11a1/121d1") pairs curves that are twists only up
  to isogeny: $\text{11a1}^{(-7)}=$ 539d2, $\text{11a3}^{(-7)}=$ 539d1, $\text{121a1}^{(-11)}=$ 121c2. All quantities it uses at $\ell=3$ are
  class-level (the isogenies have degree $5$ or $11$), so no conclusion changes; the wording should be class-level.
* **Chapter 6 outline, 6.5 versus this chapter's 6.5.** Consistent; Chapter 6's item is the preview and should cite
  Chapter 9 for the Galois action on endomorphisms and for (iv), as it already plans. No conflict.
* **Chapter 5 outline, galois:ns-example.** The curve $y^2=x^3-6x-8$ is 6912d1 in Cremona's tables (conductor $6912$); its
  data agree with this outline (4.6). Not an inconsistency; the label may be added there.
