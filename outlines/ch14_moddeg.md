# Chapter 14: Modular curves over Q, Jacobians and the modular degree (`ch:moddeg`, `chapters/ch14_moddeg.tex`)

Stage 1 line-up. Part IV (Modular forms and modular curves). Target length 1,980 lines of LaTeX (the card excluded; see
Part 3), inside the 1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2
to 12 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book and
chapter or section; a theorem number only where sure, otherwise marked "(verify)" or given by section); the paper's use
by its `\label` names, or "background". Every number quoted below (modular degrees, congruence numbers, Petersson norms
and period areas, Manin constants of the class 11a, dimensions of $J_0(N)$, cusp counts, images of the cusp $0$, the data
checks of Watkins's conjecture and of the theorem of Calegari and Emerton) was checked with PARI/GP 2.17 through `cypari2`
and Cremona's `ecdata` files for conductors below 10,000 (verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

The paper uses this chapter in six places, and the chapter is built around them.

1. **The optimal curve, the modular parametrisation and its degree** (abstract; Section 1: "Among the curves in the
   isogeny class of $E$ there is a distinguished one, the $X_0(N)$-optimal curve, for which the modular parametrisation
   $\varphi_E\colon X_0(N)\to E$ has minimal degree"; Section 6: "Optimality is determined in the tables for every class of
   conductor at most $400000$"). The chapter supplies $X_0(N)$ over $\Q$, $J_0(N)$, the Eichler-Shimura construction of the
   quotient $A_f$, modularity, the factorisation of every modular parametrisation of every curve of the class through the
   optimal one, the equivalence of "minimal degree", "connected kernel" and "saturated pullback on $H^1$", and the Cremona
   labelling convention with its one exception.
2. **The Petersson norm and the Manin constant** (Section 1: "Up to explicit factors $\deg\varphi_E$ is $\langle f,f\rangle$ divided
   by the area of the period lattice of $E$ (Zagier, Watkins)"). The chapter states and proves the exact formula
   $\deg\varphi\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c^2\langle f,f\rangle$ with $\varphi^*\omega_E=c\cdot2\pi i\,f(z)\,dz$ (important_notes.md B10), defines the
   Manin constant and states what is known about it.
3. **The congruence number and the theorem of Agashe, Ribet and Stein** (Section 1; Section 3 preamble; Lemma lem:crit;
   Lemma lem:hecke; the remark after Theorem thm:qual on 99A1). The chapter defines $r_E$ and the Hecke congruence ideal,
   states Lemma lem:crit (proved in Chapter 15), states ARS12 Theorem 2.2 and **proves its divisibility half at every
   prime** from Section 9, and verifies 99A1 ($\deg\varphi_E=4$, $r_E=12$) by direct computation.
4. **$H^1(X_0(N),\Z_\ell)$, the Hecke correspondences, $T^t=w_NTw_N$ and the pairing $\hat\delta_!$** (Section 4.1: "the pairing $\hat\delta_!$
   is the cup product composed with ... the Atkin-Lehner involution $w_{M^\Sigma}$; it is perfect and alternating ..., and the
   Hecke operators, $U_p$ included, are self-adjoint for it, because $w_{M^\Sigma}T_nw_{M^\Sigma}^{-1}$ is the adjoint of $T_n$ for the
   cup product"). The chapter supplies the Hecke correspondences on $X_0(N)$ over $\Q$, their compatibility with the
   Hecke operators of Chapter 13, the identity $C^t=w_NCw_N$ for every Hecke correspondence (proved by a matrix
   computation), and, with Chapter 8, its 12.3, the pairing $\hat\delta(x,y)=\langle x,w_N^*y\rangle$.
5. **Lemma lem:hecke and important_notes.md point 39** (Section 4.1, Lemma lem:hecke, Remark rem:free, Theorem thm:main,
   Theorem thm:quant Step 4). The chapter proves that for the optimal curve the lattice $M_{f,\lambda}$ is exactly
   $\varphi_E^*H^1(E,\Z_\ell)$, that $\hat\delta$ has ideal of values $\deg\varphi_E\cdot\Z_\ell$ on it, and hence that
   $v_\lambda(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$ with no multiplicity-one hypothesis, provided DFG04's $\eta$ is normalised as the paper
   describes it; it lists exactly what remains to be checked against DFG04.
6. **Multiplicity one, Gorenstein, the Eisenstein ideal, Shimura curves, the prime 2** (Remark rem:free; Conjecture
   conj:eis, Section sec:eis and Open question 4; Section 1.5; Section sec:two and Open question 5). The chapter states
   the multiplicity one theorem and deduces freeness and the Gorenstein property from Chapter 3's criterion; defines
   the cuspidal subgroup, the Shimura subgroup and Mazur's Eisenstein ideal, proves Manin-Drinfeld for the cusps
   $0$, $\infty$ and the formula $\varphi_E(0)=c\,L(E,1)$ modulo $\Lambda_E$; states the theorem of Ribet and Takahashi, the abc
   connection, Watkins's conjecture and the theorem of Calegari and Emerton, with data checks.

The physics reader appears twice, in one sentence each: the Zagier-Watkins formula is "the area of a $d$-sheeted cover
is $d$ times the area of the base" applied to the $L^2$ norm of a holomorphic one-form (7.3); the projection formula
$\langle\varphi^*x,\varphi^*y\rangle=\deg\varphi\,\langle x,y\rangle$ is the same statement for intersection numbers of loops (9.3).

### 1.2 Global conventions fixed in this chapter

* **C1 (curves and levels).** $N\ge1$; $X_0(N)$ is the compact Riemann surface of Chapter 12 (its 5.2) and, by 2.1, a smooth
  projective curve over $\Q$; $Y_0(N)$ its non-cuspidal part; $\infty$ and $0$ the two cusps of Chapter 12, its 4.2; $g=g(X_0(N))$.
  $\Gamma=\Gamma_0(N)$. $W_N=\begin{psmallmatrix}0&-1\\N&0\end{psmallmatrix}$ and $w_N$ the involution of $X_0(N)$ (Chapter 12, C4).
* **C2 (Hecke actions; which action where).** $\T=\Z[T_n:n\ge1]\subset\End_\C S_2(\Gamma_0(N))$ is Chapter 13's full Hecke algebra, $U_p$
  included. A Hecke correspondence $\mathcal C$ (3.1) acts on $J_0(N)$, on $H_1(X_0(N),\Z)$ and on $T_\ell J_0(N)$ by pushforward
  $\mathcal C_*$ ("Albanese"; on moduli: $T_p(E,C)=\sum_D(E/D,(C+D)/D)$), and on $H^0(\Omega^1)$, $H^1(X_0(N),\Z)$, $H^1(X_0(N),\Z_\ell)$ by
  pullback $\mathcal C^*$, the transpose of $\mathcal C_*$ (Chapter 8, its 12.2(a)). On $S_2=H^0(\Omega^1)$, $\mathcal C^*$ is Chapter 13's operator (3.2).
  Because $\T$ is commutative, $t\mapsto t_*$ and $t\mapsto t^*$ are both ring homomorphisms from $\T$, and every statement
  "$\T$ acts on ..." in this chapter means one of these two, named each time.
* **C3 (notation for adjoints, duals, pullbacks).** As in Chapter 8, C4: $A^\dagger$ is the adjoint of $A$ for a pairing; $^*$
  is pullback; $M^\vee=\Hom(M,\Z_\ell)$; the paper's Pontryagin duals ($^*$) occur only inside `paperlink` environments, which
  say so (important_notes.md B4).
* **C4 (Petersson product and the Manin constant).** $\langle f,g\rangle$ is Chapter 12's **unnormalised** product (its C5). For an
  elliptic curve $E/\Q$, $\omega_E$ is the Neron differential of a global minimal model (Chapters 9, 10), $\Lambda_E$ its period
  lattice and $\operatorname{vol}(\Lambda_E)=\frac i2\int_{E(\C)}\omega_E\wedge\bar\omega_E$ (Chapter 9, its 7.6). For a modular parametrisation $\varphi$, the
  constant $c_\varphi$ is defined by $\varphi^*\omega_E=c_\varphi\cdot2\pi i\,f(z)\,dz=c_\varphi f(q)\,dq/q$ (7.1). PARI's `mfpetersson` divides by
  $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]$.
* **C5 (Frobenius).** As in Chapter 8, C7: the arithmetic Frobenius acts on $T_\ell J$ as the $p$-power Frobenius endomorphism
  $F$; $V=pF^{-1}$ is the Verschiebung; on $H^1=(T_\ell J)^\vee$ the geometric Frobenius has the same eigenvalues.
* **C6 (optimal; labels).** "Optimal" always means $X_0(N)$-optimal (6.2). Cremona labels as in Chapter 9, its 12.1; ARS12 and
  Cremona97 print 99A1 for 99a1. $\lambda=\ell$ and $\mathcal O=\Z_\ell$ throughout, since the newform of an elliptic curve has rational
  coefficients.
* **C7 (Eisenstein).** A maximal ideal $\mathfrak m$ of $\T$ (or of $\T\otimes\Z_\ell$) is *Eisenstein* if the residual representation $\bar\rho_{\mathfrak m}$
  (Chapter 15) is reducible; for $\mathfrak m$ attached to $(f_E,\ell)$ this happens iff $E[\ell]$ is reducible (11.3). Mazur's *Eisenstein
  ideal* $I_{\mathrm{Eis}}$ at prime level is a specific ideal (11.2); the two uses are kept apart.
* **C8 (typography).** PLAN.md Section 7.2: no dash ligatures; "Eichler-Shimura", "Agashe-Ribet-Stein", "Zagier-Watkins",
  "Manin-Drinfeld", "Ribet-Takahashi", "Calegari-Emerton", "Deligne-Rapoport" with plain hyphens; labels `...:moddeg:...`.

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 1. Overview and standing notation

**1.1 `conv:moddeg:setup`** (conventions C1 to C8 as `convention` environments, and the standing notation; P). Throughout,
$E/\Q$ is an elliptic curve of conductor $N$, $f=f_E\in S_2(\Gamma_0(N))$ its newform (5.3), $\phi_f\colon\T\to\Z$, $T_n\mapsto a_n(f)$, its
eigencharacter, $I_f=\ker\phi_f$ (the paper's $I$ in Lemma lem:crit, the paper's $\wp$ in Lemma lem:ddt417), $f^\perp$ the Petersson
orthogonal complement of $f$ (Chapter 12, its 10.3; $\T$-stable by Chapter 13). A roadmap paragraph says which section
answers which sentence of the paper (Part 1.1 above). Paper: background.

### Section 2. The modular curve $X_0(N)$ over $\Q$

**2.1 `thm:moddeg:x0-over-q`** (theorem; R). (i) There is a smooth projective geometrically connected curve $X_0(N)_\Q$ over $\Q$
whose complex points form the Riemann surface $X_0(N)$ of Chapter 12, such that for every field $K\subseteq\C$ (indeed every field of
characteristic $0$) the moduli bijection of Chapter 12, its 5.4(i), is compatible with $\Aut(\C/K)$ on points with $j\ne0,1728$.
(ii) The involutions $w_d$ ($d\,\|\,N$) and the forgetful map $X_0(N)\to X(1)=\mathbb P^1_j$ are defined over $\Q$; $w_N(E,C)=(E/C,E[N]/C)$.
(iii) $X_0(N)$ has good reduction at every prime $p\nmid N$ (Igusa; Deligne-Rapoport), and a regular model over $\Z_p$ with
semistable reduction for $p\,\|\,N$ (two copies of $X_0(N/p)_{\F_p}$ crossing at the supersingular points). Proof idea (one
paragraph): the field $\Q(j,j_N)$ with $j_N(z)=j(Nz)$ is the function field of $X_0(N)$ over $\Q$, cut out by the modular
polynomial $\Phi_N(j,j_N)=0$, which has integer coefficients (Kronecker); the $q$-expansion principle shows the model is the
right one. Reference: Shimura71 6.7 (cite the section); DiamondShurman 7.7 (cite the section); DiamondIm (Sections 8, 9; cite
the sections); Deligne-Rapoport (proposed key `DeligneRapoport73`, refs.bib, see Part 6.5) and Katz-Mazur (`KatzMazur85`). Paper:
Section 1 ("$\varphi_E\colon X_0(N)\to E$" is a morphism over $\Q$), Section 4.1 ($H^1$ of a curve over $\Q$).

**2.2 `prop:moddeg:cusps-over-q`** (proposition; S, with the count P given Chapter 12, its 4.2). (i) The cusps of $X_0(N)$ are the
classes $a/c$ with $c\mid N$, $\gcd(a,c)=1$, $a$ taken modulo $\gcd(c,N/c)$; there are $\varphi(\gcd(c,N/c))$ of denominator $c$ ($\varphi$ is
Euler's function here only). (ii) The cusps of denominator $c$ are defined over $\Q(\zeta_{\gcd(c,N/c)})$ and permuted simply
transitively by its Galois group ($\sigma_t\colon\zeta\mapsto\zeta^t$ sends $a/c$ to the cusp $a'/c$ with $a'\equiv t^{\pm1}a$; the sign is a convention,
state one and check it). (iii) In particular $\infty$ ($c=N$) and $0$ ($c=1$) are $\Q$-rational, and every cusp is rational iff
$\gcd(c,N/c)\le2$ for all $c\mid N$. Examples (P, checked): $X_0(20)$ has $6$ cusps, all rational; $X_0(99)$ has $8$ cusps, of which
the two of denominator $3$ and the two of denominator $33$ form two pairs conjugate over $\Q(\sqrt{-3})$; $X_0(121)$ has $12$
cusps, ten of them (denominator $11$) conjugate over $\Q(\zeta_{11})$. Reference: Ogg 1973 (proposed key `Ogg73`, refs.bib, Part 6.5), DiamondShurman 3.8
(cite the section), Stein (book), Chapter 8 (cite the chapter). Paper: background (the cusp $\infty$ is the base point of
$\varphi_E$; the cusp $0$ in 11.4; the cuspidal subgroup in 11.1, Conjecture conj:eis, Open question 4).

**2.3 `prop:moddeg:rational-points`** (proposition; S for (i), R for (ii)). (i) Let $K$ be a field of characteristic $0$. If $E/K$
has a cyclic subgroup $C$ of order $N$ stable under $G_K$, the point $(E,C)$ of $Y_0(N)$ is $K$-rational; conversely a $K$-rational
point of $Y_0(N)$ with $j\ne0,1728$ is represented by such a pair over $K$, unique up to quadratic twist. (ii) (Mazur78,
Kenku) $Y_0(N)(\Q)\ne\emptyset$ iff $N\in\{1,\dots,19,21,25,27,37,43,67,163\}$; $Y_0(N)(\Q)$ is infinite exactly when $g(X_0(N))=0$; the
rational points of $Y_0(27)$, $Y_0(43)$, $Y_0(67)$, $Y_0(163)$ have CM. Consequence used in the book: a rational cyclic $27$-isogeny forces CM (Chapter 9, its 9.8, the proof of
important_notes.md point 17). Reference: Mazur78 (cite the section), Kenku (cite in Chapter 9's bib; verify). Paper: Conjecture
conj:eis and Section sec:eis (rational $\ell$-isogenies, $\Z/3\oplus\mu_3$, point 17).

**2.4 `ex:moddeg:small-levels`** (worked examples; P given 2.1, Chapter 12's 5.3 and 9.2, and 6.2). (a) $X_0(11)$ has genus $1$
and the rational point $\infty$; it is the elliptic curve 11a1 $[0,-1,1,-10,-20]$ with origin $\infty$ (its $j$-invariant
$-122023936/161051$ is recovered from the period ratio, Chapter 9, its 7.7), $J_0(11)=X_0(11)$ and $\varphi_{\text{11a1}}=\mathrm{id}$, of degree $1$.
(b) $X_0(20)$ is 20a1 and $X_0(14)$ is 14a1 in the same way (degree $1$). (c) $X_0(37)$ has genus $2$; $w_{37}$ has $2$ fixed points and
$X_0(37)/w_{37}$ has genus $1$ (Chapter 12, its 12.2(ii)); with origin the image of $\infty$ it is the curve 37a1, the class 37a has
one curve, and the quotient map $X_0(37)\to X_0(37)/w_{37}$ is the optimal parametrisation of 37a1, of degree $2$ (`ecdata`
agrees). Its pullback of differentials is the $w_{37}$-invariant part $S_2^+=\C f_{37a}$ ($\varepsilon_{37}(f_{37a})=+1$, root number $-1$, rank $1$). Paper:
background (the smallest cases of $\varphi_E$; Section sec:two: 37a1 has rank $1$ and $2\mid\deg$).

### Section 3. Hecke correspondences and their adjoints

**3.1 `def:moddeg:hecke-correspondence`** (definition and proposition; P for the group theory, S for the moduli description).
Let $\alpha\in M_2(\Z)$ with $\det\alpha>0$ lie in $\Delta_0(N)=\{\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}:N\mid c,\ \gcd(a,N)=1\}$, and $\Gamma_\alpha=\Gamma\cap\alpha^{-1}\Gamma\alpha$. The
*Hecke correspondence* of $\Gamma\alpha\Gamma$ is $\mathcal C_\alpha=(X(\Gamma_\alpha),\pi_1,\pi_\alpha)$ with $\pi_1(\Gamma_\alpha z)=\Gamma z$ and $\pi_\alpha(\Gamma_\alpha z)=\Gamma\alpha z$
(Chapter 8, its 12.1). For a prime $p$: $T_p:=\mathcal C_{\mathrm{diag}(1,p)}$ if $p\nmid N$ and $U_p:=\mathcal C_{\mathrm{diag}(1,p)}$ if $p\mid N$; in both cases
$X(\Gamma_\alpha)\simeq X_0(Np)$ (conjugate by $\mathrm{diag}(p,1)$), $\deg\pi_1=p+1$ resp. $p$. (i) $\mathcal C_\alpha$ depends only on $\Gamma\alpha\Gamma$, and
$\Gamma\alpha\Gamma=\bigsqcup_i\Gamma\alpha_i$ with $\alpha_i=\alpha\gamma_i$, $\gamma_i$ running over $\Gamma_\alpha\backslash\Gamma$. (ii) On moduli (S): $T_p(E,C)=\sum_D(E/D,(C+D)/D)$ over the
$p+1$ subgroups $D$ of order $p$; $U_p(E,C)=\sum_{D\cap C=0}(E/D,(C+D)/D)$ over the $p$ subgroups $D$ of order $p$ meeting $C$ trivially.
(iii) Hence $T_p$, $U_p$ and $w_d$ are correspondences defined over $\Q$, and so are all $T_n$ (polynomials in them,
Chapter 13). Reference: Shimura71 Chapter 7 (cite the sections); DiamondShurman 5.2, 6.3, 7.9 (cite the sections); DiamondIm
(cite the sections). Paper: Section 4.1 ("the Hecke operators, $U_p$ included"), Lemma lem:hecke, Theorem thm:quant Steps 1, 2.

**3.2 `prop:moddeg:hecke-compatibility`** (proposition; P for (i), (ii); S for (iii)). (i) For $f\in S_2(\Gamma_0(N))$ and $\alpha$ as in 3.1,
$\mathcal C_\alpha^*(f(z)\,dz)=\bigl(\sum_if|_2\alpha_i\bigr)(z)\,dz=(f|[\Gamma\alpha\Gamma]_2)(z)\,dz$ (compute $\pi_\alpha^*(f\,dz)=(f|_2\alpha)\,dz$ by Chapter 12, C3, and the trace
$\pi_{1*}$ as the sum over $\Gamma_\alpha\backslash\Gamma$). With $\alpha=\mathrm{diag}(1,p)$ and $\alpha_i\in\{\begin{psmallmatrix}1&j\\0&p\end{psmallmatrix}\}\cup\{\mathrm{diag}(p,1)\text{ if }p\nmid N\}$ this is
Chapter 13's $T_p$ (or $U_p$) in weight $2$, where the normalisations $(\det)^{k/2}$ and $(\det)^{k-1}$ agree. (ii) Consequently
$t\mapsto t^*$ identifies $\T$ with the subring of $\End H^1(X_0(N),\Z)$ generated by the $\mathcal C^*$ ($H^1(X_0(N),\C)=S_2\oplus\overline{S_2}$ by Chapter 8,
its 10.2(iii), with $\mathcal C^*$ acting on $\overline{S_2}$ by the complex conjugate matrix, so faithfulness on $S_2$ gives faithfulness on $H^1$);
in particular $\T$ is a finite free $\Z$-module (a subring of $\End$ of a lattice) and $t\mapsto t_*$ embeds $\T$ in $\End_\Q J_0(N)$.
(iii) (The $H^1$ route to Shimura's integral basis, Chapter 12, its 11.2, in weight $2$.) Since $\T\otimes\C\simeq\Hom_\C(S_2,\C)$ by the
pairing $(t,g)\mapsto a_1(tg)$ (Chapter 13), every $\psi\in\Hom_\Z(\T,\Z)$ is $t\mapsto a_1(tg_\psi)$ for a unique $g_\psi\in S_2$, and $a_n(g_\psi)=\psi(T_n)\in\Z$:
so $S_2(\Gamma_0(N);\Z)$ has rank $g$. This item only records the route; Chapters 12 and 13 own the statements (important_notes.md
B11). Reference: DiamondShurman 6.3, 6.5 (cite the sections); Shimura71 3.4, 7.3 (cite the sections). Paper: Section 3
preamble ($\T$ "the subring of $\End S_2(\Gamma_0(N))$ generated over $\Z$ by all $T_n$"), Section 4.1 (the Hecke action on $H^1$).

**3.3 `thm:moddeg:transpose`** (theorem; P). (i) For $\alpha\in\Delta_0(N)$ put $\alpha'=(\det\alpha)\alpha^{-1}$. Then $\mathcal C_\alpha^t\simeq\mathcal C_{\alpha'}$ as correspondences:
the map $u\colon X(\Gamma_\alpha)\to X(\Gamma_{\alpha'})$, $\Gamma_\alpha z\mapsto\Gamma_{\alpha'}\alpha z$, is an isomorphism ($\alpha\Gamma_\alpha\alpha^{-1}=\Gamma\cap\alpha\Gamma\alpha^{-1}=\Gamma_{\alpha'}$, scalars acting
trivially) with $\pi_1\circ u=\pi_\alpha$ and $\pi_{\alpha'}\circ u=\pi_1$. (ii) For $\beta$ normalising $\Gamma$ (for instance $W_N$),
$\mathcal C_{\beta\alpha\beta^{-1}}=w_\beta\circ\mathcal C_\alpha\circ w_\beta^{-1}$, so $\mathcal C_{\beta\alpha\beta^{-1}}^*=(w_\beta^{-1})^*\mathcal C_\alpha^*w_\beta^*$. (iii) $W_N\,\mathrm{diag}(1,p)\,W_N^{-1}=\mathrm{diag}(p,1)=\mathrm{diag}(1,p)'$
(a two-line matrix product). Hence **$T_p^t=w_NT_pw_N$ and $U_p^t=w_NU_pw_N$ for every prime $p$**, and since $t\mapsto t^t$ reverses
products and $\T$ is commutative, **$t^t=w_Ntw_N$ for every $t\in\T$** (as correspondences up to equivalence, hence on $H^1$, $H_1$, $J_0(N)$).
(iv) For $p\nmid N$ also $T_p^t=T_p$ ($\Gamma\,\mathrm{diag}(1,p)\,\Gamma=\Gamma\,\mathrm{diag}(p,1)\,\Gamma$ by elementary divisors in $\Delta_0(N)$, since $\gcd(p,N)=1$); for
$p\mid N$, $U_p^t\ne U_p$ in general (Exercise 2: on the span of $f_{11}(z)$, $f_{11}(2z)$ at level $22$). Reference: Shimura71 Chapter 7
(cite the section); DDT Section 4.4 (cite the section, as the paper does); DFG04 Sections 1.6.1, 1.8.2 (as the paper cites
them). Paper: Section 4.1 ("$w_{M^\Sigma}T_nw_{M^\Sigma}^{-1}$ is the adjoint of $T_n$ for the cup product (this is what the composition with $w$
is for)"); Chapter 8, its 12.4(d), points here.

**3.4 `cor:moddeg:delta-hat`** (corollary; P given 3.3 and Chapter 8, its 12.3 and 12.3(e)). Let $R$ be $\Z$, $\Z_\ell$ or $\Q_\ell$ and
$\langle\ ,\ \rangle$ the cup product on $H^1(X_0(N),R)$ (Chapter 8, its 10.3). (i) $(t^*)^\dagger=w_N^*t^*w_N^*$ for every $t\in\T$. (ii) The pairing
$$\hat\delta(x,y)=\langle x,w_N^*y\rangle$$
is perfect and alternating on $H^1(X_0(N),R)$, and every $t^*$, $t\in\T$ (the $U_p^*$ included), is self-adjoint for it. (iii) Every
idempotent of $\T\otimes\Z_\ell$ is self-adjoint, $H^1(X_0(N),\Z_\ell)=\bigoplus_{\mathfrak m}H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ is an orthogonal decomposition and $\hat\delta$ is
perfect on each summand (important_notes.md point 36). (iv) For weight $2$ and trivial character, $\hat\delta$ is the pairing
$\hat\delta_!$ of DFG04 (13), (14) **as the paper reads it** in Section 4.1 (the operator $[UwU]\omega$ being $w_N$, with no scalar,
Chapter 12, C3, C4); the comparison of normalisations is item 9.6. Paper: Section 4.1, Lemma lem:hecke ("with the pairing
$\hat\delta_!$ of Section sec:dfg, perfect and alternating with $\T$ self-adjoint"), Theorem thm:quant Step 2, Lemma lem:ddt417 as
applied.

**3.5 `rem:moddeg:petersson-analogue`** (remark; R, pointer). The same identity on the Petersson side: $T_n$ is self-adjoint for
$(n,N)=1$ and $U_p^\dagger=w_NU_pw_N$ (Chapter 13); a newform is a $w_N$-eigenvector with eigenvalue $\varepsilon_N(f)=\pm1$ (Chapter 13; Chapter
12, its 12.4(c)). One sentence on why the two adjoint statements agree: under $S_2\subset H^1(X_0(N),\C)$ the Hodge inner product
$\frac i2\int\omega\wedge\bar\eta$ is the Petersson product (Chapter 12, its 10.1(iv)), and complex conjugation exchanges $S_2$ and
$\overline{S_2}$. Paper: Lemma lem:crit ("$f$ is an eigenvector of the adjoints of the $T_n$ as well").

### Section 4. The Jacobian $J_0(N)$, its homology and the $f$-lattice

**4.1 `def:moddeg:j0`** (definition and theorem; P for (ii), (iv); R for (i), (iii)). (i) $J_0(N):=\operatorname{Jac}(X_0(N)_\Q)$ is an abelian
variety over $\Q$ of dimension $g=\dim S_2(\Gamma_0(N))$ (Chapter 8, its 11.3; Chapter 12, its 8.2), with good reduction at every
$p\nmid N$ (from 2.1(iii)). (ii) $J_0(N)(\C)=S_2(\Gamma_0(N))^\vee/H_1(X_0(N),\Z)$, with $\gamma\mapsto(f\mapsto\int_\gamma f(z)\,dz)$ (Chapter 8, its 11.2, and
$S_2=H^0(\Omega^1)$). (iii) The Abel-Jacobi map $\iota\colon X_0(N)\to J_0(N)$, $P\mapsto[(P)-(\infty)]$, is defined over $\Q$ because $\infty$ is
rational (2.2), and has the universal property of Chapter 8, its 11.3(iii). (iv) Table (checked: `mfdim([N,2],1)` and the
ranks of the integral lattices of Part 6.6): $\dim J_0(N)=1,1,1,2,7,9,6,19,49,109,145$ for $N=11,14,20,37,77,99,121,140,539,726,980$.
Reference: DiamondShurman 6.1, 6.6, 7.9 (cite the sections); Milne, Jacobian varieties (Chapter 8's key). Paper: Section 1,
Remark rem:free ("$J_0(N)[\mathfrak m]$"), Conjecture conj:eis and Open question 4 (torsion, cuspidal subgroup).

**4.2 `prop:moddeg:hecke-on-j0`** (proposition; P given 3.1, 3.2 and Chapter 8, its 12.2). (i) $t\mapsto t_*$ is an injective ring
homomorphism $\T\to\End_\Q(J_0(N))$; on $J_0(N)(\C)=S_2^\vee/H_1$ it is the transpose of $t^*$ on $S_2$ and $t_*$ on $H_1$. (ii) On
$T_\ell J_0(N)=H_1(X_0(N),\Z_\ell)$ (Chapter 8, its 11.7) the action is $t_*$, commuting with $G_\Q$ (the correspondences are defined over $\Q$).
(iii) The involution $t\mapsto t^t=w_Ntw_N$ of $\T$ (3.3) fixes $\phi_f$ for every newform $f$ (since $f$ is a $w_N$-eigenvector, $\phi_f(U_p^t)=\phi_f(U_p)$),
so $I_f$ is stable under it; hence the quotient $J_0(N)/I_fJ_0(N)$ and the lattice $M_{f,\ell}$ of 4.4 are the same whether one uses
the Albanese action $t_*$ or the Picard action $(t^t)_*$ (pitfall in Part 6.2). Reference: DiamondShurman 6.3, 6.6 (cite the
sections). Paper: Remark rem:free ("the localised Hecke algebra", "the Tate module"), Section 4.1.

**4.3 `prop:moddeg:tate-module-vs-h1`** (proposition; P for (i), (ii) given Chapter 8, its 11.7, 11.8, 12.3(c); R for the etale
input). (i) $H^1(X_0(N),\Z_\ell)=\Hom_{\Z_\ell}(T_\ell J_0(N),\Z_\ell)$, with $t^*$ the transpose of $t_*$; as $G_\Q$-modules (etale cohomology)
$H^1_{\mathrm{et}}(X_0(N)_{\bar\Q},\Z_\ell)\simeq T_\ell J_0(N)(-1)$, and the cup product is $G_\Q$-equivariant with values in $\Z_\ell(-1)$. (ii) The map
$\Psi=w_{N*}\circ\operatorname{PD}\colon H^1(X_0(N),\Z_\ell)\to H_1(X_0(N),\Z_\ell)=T_\ell J_0(N)$ is an isomorphism of $\T$-modules for the actions $t^*$ on the source
and $t_*$ on the target (Chapter 8, its 12.3(c): $\operatorname{PD}\circ\mathcal C^*=(\mathcal C^t)_*\circ\operatorname{PD}$, and 3.3); $\operatorname{PD}$ alone intertwines $t^*$ with $(t^t)_*$. Over
$\bar\Q$, $\Psi$ becomes $G_\Q$-equivariant after the twist by $\Z_\ell(-1)$ ($w_N$ is defined over $\Q$). (iii) Hence freeness over a
localisation $\T_{\mathfrak m}$ transfers between $T_\ell J_0(N)_{\mathfrak m}$ and $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ (important_notes.md point 41). Reference: Chapter 8
outline items cited; Milne, Etale cohomology (Chapter 8's citation). Paper: Remark rem:free ("the Tate module is free of
rank two"), Section 4.2 (point 26).

**4.4 `def:moddeg:f-lattice`** (definition and proposition; P given Chapter 13's multiplicity one). Let $f$ be a newform of level
$N$ with rational coefficients. (i) $H^1(X_0(N),\Q)\otimes\C=S_2\oplus\overline{S_2}$, and the subspace killed by $I_f\otimes\C$ is $\C\,\omega_f\oplus\C\,\overline{\omega_f}$, of
dimension $2$ (the eigensystem $\phi_f$ occurs once in $S_2$, Chapter 13, and its complex conjugate system, equal to $\phi_f$, once in
$\overline{S_2}$). So $V_f:=H^1(X_0(N),\Q)[I_f]$ is a $2$-dimensional $\Q$-space with $V_f\otimes\R$ spanned by $\operatorname{Re}\omega_f$, $\operatorname{Im}\omega_f$. (ii) Define
$$M_{f,\ell}:=H^1(X_0(N),\Z_\ell)[I_f]=\{x:tx=\phi_f(t)x\ \forall t\in\T\}=H^1(X_0(N),\Z_\ell)\cap(V_f\otimes\Q_\ell),$$
a saturated $\Z_\ell$-sublattice of rank $2$ (saturated as a kernel, Chapter 3). This is the paper's $M_{f,\lambda}$ "the kernel on it of the
kernel of the eigencharacter" (Section 4.1 with $\Sigma=\emptyset$). (iii) $w_N^*$ preserves $V_f$ and $M_{f,\ell}$ and acts on both by
$\varepsilon_N(f)$ (Chapter 12, its 12.2(iii); integrality because $w_N^*$ preserves $H^1(X_0(N),\Z_\ell)$). (iv) $M_{f,\ell}$ is $G_\Q$-stable (the
Hecke and Galois actions commute) and is a lattice in the Galois representation of $f$ (Chapter 15). Paper: Section 4.1, Lemma
lem:hecke ("$L[\wp]=M_{f,\lambda}$ has rank $2$"), Section 4.2 (point 26).

### Section 5. Eichler-Shimura and modularity

**5.1 `thm:moddeg:shimura-quotient`** (theorem; S for (i), (ii); R for (iii)). Let $f$ be a newform of level $N$ with coefficient
field $K_f$ and $I_f=\ker(\T\to K_f)$. (i) $I_fJ_0(N)$ (the subgroup generated by the images $t_*J_0(N)$, $t\in I_f$) is an abelian
subvariety over $\Q$ (an image of the abelian variety $J_0(N)^r$ under a homomorphism, hence connected), and $A_f:=J_0(N)/I_fJ_0(N)$
is an abelian variety over $\Q$ of dimension $[K_f:\Q]$, on which $\T$ acts through $\T/I_f\hookrightarrow\mathcal O_{K_f}$; the quotient map
$\pi_f\colon J_0(N)\to A_f$ has connected kernel by construction. (ii) For $f$ with rational coefficients, $A_f=:E_f$ is an elliptic
curve over $\Q$ with $\T$ acting through $\phi_f$; $\pi_f^*\colon H^1(E_f,\Q)\to H^1(J_0(N),\Q)=H^1(X_0(N),\Q)$ has image $V_f$ (4.4). (iii)
(Shimura) $L(A_f,s)=\prod_{\sigma\colon K_f\to\C}L(f^\sigma,s)$, in particular $L(E_f,s)=L(f,s)$. Reference: Shimura71 Theorem 7.14 (verify the
number), Shimura73; DiamondShurman 6.6 and Theorem 6.6.6 (verify the number). Paper: Section 1 (the optimal curve is $E_f$,
6.2), Lemma lem:hecke (via 9.1), Section 4.2.

**5.2 `thm:moddeg:eichler-shimura`** (theorem; R for (i), P for (ii) given (i) and Chapter 8, its 11.8(d)). (i) (Eichler-Shimura
congruence relation.) For $p\nmid N$, in $\End((J_0(N))_{\F_p})$: $(T_p)_*=F+V$, where $F$ is the Frobenius endomorphism and $V=pF^{-1}$
the Verschiebung (Kronecker's congruence: modulo $p$ the correspondence $T_p$ is the graph of the Frobenius morphism plus its
transpose; proof idea from the moduli description 3.1(ii): for an ordinary curve in characteristic $p$, the quotient by the
connected subgroup of order $p$ is the Frobenius image, and the quotients by the $p$ etale subgroups are the Frobenius preimages). (ii) Consequences: on $T_\ell A_f$
($\ell\ne p$) the arithmetic Frobenius satisfies $F^2-T_pF+p=0$; for $f$ rational, $\det(X-\Frob_p\mid T_\ell E_f)=X^2-a_p(f)X+p$, so
$a_p(E_f)=p+1-\#E_f(\F_p)=a_p(f)$ for every $p\nmid N$ (with Chapter 9, its 8.x, and Chapter 8, its 11.8(d)); on $H^1$ the
geometric Frobenius has the same characteristic polynomial (C5). (iii) This is how the Galois representation of a weight-two
newform is constructed (Chapter 15). Reference: Shimura71 Section 7.4 (verify the theorem number), DiamondShurman 8.7
(cite the section), DiamondIm Section 10 (cite the section). Paper: Section 1 ("$f=f_E$ the newform attached to it"), Lemma
lem:old ($a_p$ as traces of Frobenius), Section 4.2.

**5.3 `thm:moddeg:modularity`** (theorem; R). (Wiles, Taylor-Wiles, Breuil-Conrad-Diamond-Taylor.) For every elliptic curve
$E/\Q$ of conductor $N$ there is a newform $f_E\in S_2(\Gamma_0(N))$ with rational coefficients and $a_p(f_E)=a_p(E)$ for every prime $p$
(including $p\mid N$; the level equals the conductor by Carayol86); equivalently $E$ is isogenous over $\Q$ to $E_{f_E}$ (5.1), and
$L(E,s)=L(f_E,s)$. One paragraph of history: Taniyama, Shimura, Weil; semistable case Wiles95, TaylorWiles; general case BCDT;
the role of $R=\T$ (Chapter 20). Reference: Wiles95, TaylorWiles, BCDT, Carayol86. Paper: Section 1 ("let $f=f_E$ be the newform
attached to it"), everything.

**5.4 `cor:moddeg:classes-and-newforms`** (corollary; S). $E\mapsto f_E$ is a bijection from $\Q$-isogeny classes of elliptic curves
of conductor $N$ to newforms of level $N$ with rational coefficients. (Injectivity: isogenous curves have the same $a_p$; curves
with the same $a_p$ for almost all $p$ are isogenous by Faltings's isogeny theorem (R). Surjectivity: $E_f$ has conductor $N$
(Carayol86, R) and $f_{E_f}=f$ by 5.2(ii) and strong multiplicity one, Chapter 13.) Example: 11a $\leftrightarrow f_{11}=\eta(z)^2\eta(11z)^2$;
the level $99$ has four classes 99a, 99b, 99c, 99d and $\dim S_2(\Gamma_0(99))=9=4+2\cdot1+3\cdot1$ (newforms of levels $99$, $33$, $11$ counted
with the number of divisors of $99/M$: $4\cdot1+1\cdot2+1\cdot3$). Paper: Section 1 ("the isogeny class of $E$"), Section sec:data
(classes).

**5.5 `ex:moddeg:class-11a`** (worked example; P given 2.4, 5.2, 6.2 and the numerics of Part 6.6). The class 11a has three curves,
11a1 $=X_0(11)$, 11a2, 11a3, linked by $5$-isogenies (11a1 to 11a2 and to 11a3 of degree $5$, 11a2 to 11a3 of degree $25$). Since
$X_0(11)=J_0(11)=$ 11a1, Eichler-Shimura for $X_0(11)$ proves $a_p(\text{11a1})=a_p(f_{11})$ for every $p\ne11$ (the identity Chapter 12, its
9.2(iv), checked numerically, is now a theorem). The modular parametrisations of 11a2 and 11a3 are the two $5$-isogenies out of
11a1, of degree $5$ each (6.2(ii)); 11a3 is $X_1(11)$ (R). Paper: background; Section 3 Example (11a1 as the congruent form).

### Section 6. Optimal curves, the modular parametrisation and the modular degree

**6.1 `def:moddeg:parametrisation`** (definition; P for the equivalence). Let $E/\Q$ have conductor $N$. A *modular parametrisation*
of $E$ is a nonconstant morphism $\varphi\colon X_0(N)\to E$ over $\Q$ with $\varphi(\infty)=O$. By the universal property (4.1(iii)) these
correspond bijectively to nonzero homomorphisms $h\colon J_0(N)\to E$ over $\Q$, via $\varphi=h\circ\iota$ and $h=\varphi_*$ (Chapter 8, its 11.4(iv)).
Paper: abstract and Section 1 ("$\varphi_E\colon X_0(N)\to E$ its modular parametrisation").

**6.2 `thm:moddeg:optimal`** (theorem; S for (i), with R inputs; P for (ii) to (iv) given (i) and Chapter 8, its 11.5). Let $\mathcal I$
be an isogeny class of conductor $N$, $f$ its newform (5.4) and $E_f=J_0(N)/I_fJ_0(N)$ with $\varphi_{E_f}=\pi_f\circ\iota$ (5.1). (i) Every
homomorphism $h\colon J_0(N)\to E$ to a curve $E\in\mathcal I$ vanishes on $I_fJ_0(N)$. Sketch: the identity component $B$ of $\ker h$ is an
abelian subvariety of codimension $1$ with $V_\ell B=\ker(h_*\colon V_\ell J_0(N)\to V_\ell E)$; the Galois-stable quotient $V_\ell J_0(N)/V_\ell B\simeq V_\ell E$
has Frobenius traces $a_p(f)$; decomposing $V_\ell J_0(N)\otimes\bar\Q_\ell$ into the generalised eigenspaces of $\T$ (Galois-stable, Chapter 3,
its 10.5), on which Frobenius satisfies $X^2-a_p(g)X+p$ by 5.2, strong multiplicity one (Chapter 13) and Chebotarev (Chapter 5)
show that only the $\phi_f$-eigenspace, of dimension $2$ by 4.4, can map onto $V_\ell E$; so $V_\ell B\supseteq V_\ell(I_fJ_0(N))$, both have
dimension $2g-2$, and an abelian subvariety is determined by its rational Tate module, so $B=I_fJ_0(N)$. (ii) **Factorisation.**
For every $E\in\mathcal I$ and every modular parametrisation $\varphi$ of $E$ there is a unique isogeny $\psi\colon E_f\to E$ with $\varphi=\psi\circ\varphi_{E_f}$;
hence $\deg\varphi=\deg\psi\cdot\deg\varphi_{E_f}$. (iii) **Characterisations.** For $E\in\mathcal I$ and a modular parametrisation $\varphi$ of $E$ the
following are equivalent: (a) $\psi$ in (ii) is an isomorphism; (b) $\ker(\varphi_*\colon J_0(N)\to E)$ is connected; (c) $\varphi_*\colon H_1(X_0(N),\Z)\to H_1(E,\Z)$
is surjective; (d) $\varphi^*H^1(E,\Z)$ is saturated in $H^1(X_0(N),\Z)$; (e) $\varphi^*\colon E=E^\vee\to J_0(N)$ is injective; (f) $\deg\varphi$ is the
minimum of the degrees of all modular parametrisations of all curves in $\mathcal I$. ((b) to (e): Chapter 8, its 11.5(iii); (a)$\Leftrightarrow$(b)
by (i); (a)$\Leftrightarrow$(f) by (ii).) (iv) **Uniqueness.** The pair $(E_f,\varphi_{E_f})$ is the unique pair up to unique isomorphism
satisfying these conditions; it is called the *$X_0(N)$-optimal curve* (or strong Weil curve) $E$ of $\mathcal I$, and $\deg\varphi_E$ its
*modular degree*. Reference: Cremona97 Chapter II (cite the section); ARS12 Section 2 or 3 (cite the section); Stevens,
*Stevens89* (proposed key, optional; see Part 6.5). Paper: abstract, Section 1 ("for which the modular parametrisation has
minimal degree"), Theorem thm:main and Lemma lem:hecke ("$E$ be $X_0(N)$-optimal"), Section 3 preamble ("let $E_0$ be the optimal
curve in the class").

**6.3 `prop:moddeg:degree-descriptions`** (proposition; P given 6.2 and Chapter 8, its 11.4, 11.5). Let $E$ be optimal, $d=\deg\varphi_E$,
$A=\varphi_E^*(E)\subseteq J_0(N)$ (an elliptic curve isomorphic to $E$, by 6.2(iii)(e)) and $B=\ker\varphi_{E*}=I_fJ_0(N)$. (i) $d$ is the degree of the
morphism of curves, in each of the senses of Chapter 8 (field degree, preimage count, pullback of divisors, topological
degree). (ii) $\varphi_{E*}\circ\varphi_E^*=[d]$ on $E$, the composition $E^\vee\to J_0(N)\to E$ of PLAN.md. (iii) $A\cap B=\varphi_E^*(E[d])\simeq(\Z/d)^2$, so $d$ is
the exponent of $A\cap B$ (the "modular exponent" of ARS12). (iv) $\langle\varphi_E^*x,\varphi_E^*y\rangle_{X_0(N)}=d\,\langle x,y\rangle_E$ on $H^1$ (Chapter 8, its 11.5(i)); the
Gram determinant of the cup product on $\varphi_E^*H^1(E,\Z)$ is $d^2$ and its ideal of values is $d\Z$. (v) $\deg\varphi_E$ is computable
(Section 12, 12.6). Paper: Section 1 ("the modular degree is computable"), Lemma lem:hecke (via 9.3).

**6.4 `prop:moddeg:valuation-in-class`** (proposition; P). Let $E$ be optimal in $\mathcal I$, $\ell$ a prime with $E[\ell]$ irreducible, and
$E'\in\mathcal I$. Then every isogeny $E\to E'$ of minimal degree is cyclic of degree prime to $\ell$, so the minimal degree of a modular
parametrisation of $E'$ (6.2(ii)) has the same $\ell$-adic valuation as $\deg\varphi_E$. (A cyclic isogeny of degree divisible by $\ell$ has a
rational subgroup of order $\ell$ in its kernel, contradicting irreducibility, Chapter 9.) So under the paper's standing
hypothesis "$E[\ell]$ irreducible" the choice of curve in the class does not affect $v_\ell$ of the degree (important_notes.md point
27). Without irreducibility it does: 11a1, 11a2, 11a3 at $\ell=5$ (degrees $1$, $5$, $5$). Paper: Theorem thm:qual ("the
$X_0(N)$-optimal curve in the isogeny class of $E$"), Section 3 preamble ($E_0$), Theorem thm:main.

**6.5 `conv:moddeg:cremona-optimal`** (convention and data; R for the data). In Cremona's tables curve number $1$ of each class is
the optimal curve, with the single exception of 990h, whose optimal curve is 990h3 $=[1,-1,1,-1568,-4669]$ (modular degree $1728$
in `ecdata`'s `degphi` file); optimality is established for every class of conductor at most $400000$ and for a large part of
the classes up to $500000$ (the paper, Section 6: $359{,}009$ further classes); the LMFDB numbering differs (Chapter 9, its 12.1).
How optimality is certified (one paragraph, R): compare the period lattices of the curves in the class with the lattice
of $\varphi^*$ computed from modular symbols (Cremona97 Chapter II; Cremona's later papers). Paper: Section 6 ("Optimality is
determined in the tables ..."), important_notes.md point 25 (the abstract's "every optimal curve of conductor at most
$500000$").

**6.6 `ex:moddeg:running-degrees`** (worked example table; data R from `ecdata`, the consistency checks P). Modular degrees of the
optimal curves of the paper's world (all equal to PARI's `ellmoddegree`, Part 6.6):

| curve | $N$ | rank | $\#E(\Q)_{\mathrm{tors}}$ | $\deg\varphi_E$ | $\dim J_0(N)$ | role |
|-|-|-|-|-|-|-|
| 11a1 | $11$ | $0$ | $5$ | $1$ | $1$ | $X_0(11)$ itself |
| 20a1 | $2^2\cdot5$ | $0$ | $6$ | $1$ | $1$ | $X_0(20)$ itself |
| 37a1 | $37$ | $1$ | $1$ | $2$ | $2$ | $X_0(37)/w_{37}$ |
| 99a1 (99A1) | $3^2\cdot11$ | $1$ | $2$ | $4=2^2$ | $9$ | $r_E=12$ (8.5) |
| 121a1 | $11^2$ | $0$ | $1$ | $6=2\cdot3$ | $6$ | thm:qual (b), $e_3=1$ attained |
| 539c1 | $7^2\cdot11$ | $1$ | $2$ | $288=2^5\cdot3^2$ | $49$ | thm:qual (c), $\ell=3$ |
| 980i1 | $2^2\cdot5\cdot7^2$ | $0$ | $1$ | $2880=2^6\cdot3^2\cdot5$ | $145$ | Section 3 Example, $\ell=5$ |
| 726a1 | $2\cdot3\cdot11^2$ | $1$ | $2$ | $144=2^4\cdot3^2$ | $109$ | 3Ns, $r_E=1584$ (8.5) |

Supporting curves (all `ecdata`): 77c1 ($6$), 140b1 ($60$), 121c1 ($6$), 121d1 ($24$), 539d1 ($72$), 990h3 ($1728$). Paper: the Example of
Section 3, the remark on 99A1, the appendix (121a1, 726a1), Section sec:anomaly.

### Section 7. The Manin constant and the formula of Zagier and Watkins

**7.1 `def:moddeg:manin-constant`** (definition and proposition; P). Let $\varphi$ be a modular parametrisation of $E$ (6.1). (i)
$\varphi^*\omega_E$ is a nonzero holomorphic differential lying in $V_f\otimes\C$ (by 6.2(ii), $\varphi^*$ factors through $\pi_f^*$, and 5.1(ii)), hence a
multiple of $\omega_f=f(z)\,dz$: $\varphi^*\omega_E=c_\varphi\cdot2\pi i\,f(z)\,dz=c_\varphi\,f(q)\,\frac{dq}q$. (ii) $c_\varphi\in\Q^\times$: $\varphi$ and $\omega_E$ are defined over $\Q$ and
the cusp $\infty$ is rational, so the expansion of $\varphi^*\omega_E$ in the local parameter $q$ at $\infty$ has rational coefficients, and
$a_1(f)=1$. (iii) For $\varphi=\psi\circ\varphi_E$ (6.2(ii)), $c_\varphi=c_{\varphi_E}\cdot u_\psi$ where $\psi^*\omega_{E'}=u_\psi\,\omega_E$, $u_\psi\in\Z\setminus\{0\}$. The *Manin
constant* of $E$ is $c_E:=c_{\varphi_E}$ for the optimal curve, well defined up to sign (the sign of $\omega_E$). Paper: background (the
"explicit factors" of Section 1).

**7.2 `thm:moddeg:manin-known`** (theorem; R; every item to be checked against the source before printing). (i) (Edixhoven)
$c_E\in\Z$, by the $q$-expansion principle on the Neron model; more generally $c_\varphi\in\Z$ for every modular parametrisation. (ii)
(Manin's conjecture) $c_E=\pm1$ for the optimal curve. (iii) Known results: if a prime $p$ divides $c_E$ then $p=2$ or $p^2\mid N$
(Mazur78 for $p\nmid2N$; AU96 for $p^2\nmid N$); $c_E=\pm1$ for every optimal curve of conductor below a large bound (Cremona's
computations; ARS's paper on the Manin constant) and for semistable optimal curves (Cesnavicius); the recent bound $c_E\mid\deg\varphi_E$
and related results (Cesnavicius, Neururer, Saha). The writer cites only what is checked; proposed keys in Part 6.5. (iv) For
non-optimal curves $c_\varphi\ne\pm1$ is possible: 7.4. Paper: background; the paper's tables assume $c_E=1$ implicitly only through the
Zagier-Watkins heuristic of Section 1, not in any proof.

**7.3 `thm:moddeg:zagier-watkins`** (theorem; P given Chapter 8, its 9.4(b), 11.5(i), and Chapter 12, its 10.1(iv)). For every
modular parametrisation $\varphi$ of $E$,
$$\deg\varphi\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c_\varphi^2\,\langle f,f\rangle,$$
with the unnormalised Petersson product (C4). In particular, for the optimal curve with $c_E=\pm1$,
$\deg\varphi_E=4\pi^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$. Proof (three lines): $\frac i2\int_{X_0(N)}\varphi^*\omega_E\wedge\overline{\varphi^*\omega_E}=\deg\varphi\cdot\frac i2\int_E\omega_E\wedge\bar\omega_E$ (a
$\deg\varphi$-sheeted orientation-preserving cover away from finitely many points), the right side is $\deg\varphi\cdot\operatorname{vol}(\Lambda_E)$, and
the left is $c_\varphi^2\cdot4\pi^2\cdot\frac i2\int\omega_f\wedge\bar\omega_f=4\pi^2c_\varphi^2\langle f,f\rangle$. **The Manin constant stands in the numerator**
(important_notes.md B10). Physics aside (one sentence): the $L^2$ norm of a pulled-back one-form counts every sheet of the
cover. Reference: Zagier85; Watkins02; Cremona97 Chapter II (cite the sections; check their normalisations of $\langle\ ,\ \rangle$ before
saying they agree). Paper: Section 1 ("Up to explicit factors $\deg\varphi_E$ is $\langle f,f\rangle$ divided by the area of the period lattice of
$E$ (Zagier, Watkins)").

**7.4 `ex:moddeg:zw-numerics`** (worked example; P as a computation, Part 6.6). Unnormalised Petersson norms ($\mu(N)$ times PARI's
`mfpetersson`), period areas $\operatorname{vol}(\Lambda_E)$ and $4\pi^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)=\deg\varphi/c_\varphi^2$ (30 digits):

| curve | $\langle f,f\rangle$ | $\operatorname{vol}(\Lambda_E)$ | $4\pi^2\langle f,f\rangle/\operatorname{vol}$ | $\deg\varphi$ | $c_\varphi$ |
|-|-|-|-|-|-|
| 11a1 | $0.04690014787349518782$ | $1.85154362345595931771$ | $1$ | $1$ | $1$ |
| 11a2 | same | $0.37030872469119186354$ | $5$ | $5$ | $1$ |
| 11a3 | same | $9.25771811727979658854$ | $1/5$ | $5$ | $5$ |
| 37a1 | $0.37175414751069605028$ | $7.33813274078957673907$ | $2$ | $2$ | $1$ |
| 99a1 | $0.53851956871086065179$ | $5.31497510542145355032$ | $4$ | $4$ | $1$ |
| 121a1 | $0.42823936001195717858$ | $2.81770204819580190671$ | $6$ | $6$ | $1$ |

(The 20a1 value $1$ is in Chapter 12, its 10.4.) Reading: in the class 11a the parametrisations of 11a2 and 11a3 both have degree
$5$ (6.2(ii)), and the formula forces $c=1$ for 11a2 and $c=5$ for 11a3 (the $5$-isogeny 11a1 $\to$ 11a3 pulls $\omega_{\text{11a3}}$ back to
$5\,\omega_{\text{11a1}}$). Paper: Section 1; the Chapter 22 computations.

**7.5 `rem:moddeg:rankin-and-computation`** (remark; R, pointers). (a) Rankin and Shimura express $\langle f,f\rangle$ through $L(\operatorname{Sym}^2f,2)$
with explicit factors at the bad primes (Chapter 19; DFG04 Lemma 2.12 as the paper cites it; Shimura76); combined with 7.3 this
is Watkins's method of computing $\deg\varphi_E$ (Watkins02), implemented in PARI's `ellmoddegree`. (b) The Rankin series
$\sum a_n^2n^{-s}$ is not the naive adjoint $L$-function (important_notes.md point 30; Chapter 12, its 10.5(b); Chapter 19). (c) The
"explicit factors" of the paper's Section 1 are $4\pi^2c_E^2$ in the book's normalisation. Paper: Section 1 (Zagier, Watkins,
Rankin, Shimura, Flach), Section 6 (`ellmoddegree`).

### Section 8. The congruence number and the theorem of Agashe, Ribet and Stein

**8.1 `def:moddeg:congruence-number`** (definitions recalled from Chapter 13, its 4.3, and proposition; P for (ii), (iii)). (i) (The
paper's definition, Section 1 and Section 3 preamble; Chapter 13's $r_f$ for $f=f_E$.) The *congruence number* $r_E$ of $E$ (of $f=f_E$) is the largest integer $r$ such that $f\equiv g\pmod r$ coefficientwise for
some $g\in S_2(\Gamma_0(N);\Z)\cap f^\perp$. (ii) The *Hecke congruence ideal* of $f$ is $\eta_f=\phi_f(\operatorname{Ann}_\T I_f)\subseteq\Z$, and $\eta_f\otimes\Z_\ell=\phi_f(\operatorname{Ann}_{\T_\ell}(I_f\T_\ell))$ is
computed in the localisation $\T_{\mathfrak m}$ at the maximal ideal $\mathfrak m$ containing $\ell$ and $I_f$ (Chapter 3, its 11.1(v); important_notes.md point
35: the other local factors lie in $\ker\phi_f$, not in the annihilator). (iii) Since $f$ is a newform its eigensystem has multiplicity
one, $\T\otimes\Q=\Q\times\T'$, $I_f\cap\operatorname{Ann}(I_f)=0$ and $\eta_f\ne0$ (Chapter 3, its 11.1(ii); important_notes.md point 19). Paper: Section 1 ("the
congruence number $r_E$"), Lemma lem:crit, Lemma lem:hecke.

**8.2 `lem:moddeg:crit`** (lemma, the paper's Lemma lem:crit; R here, **proved in full in Chapter 15**, restated as a theorem on
congruence modules in Chapter 20). $\T/(I_f+J)\simeq\Z/r_E$ with $J=\operatorname{Ann}_\T(f^\perp)=\operatorname{Ann}_\T(I_f)$, so $r_E\Z=\eta_f$; the same over $\Z_\ell$ with $r_E$ replaced
by its $\ell$-part; and a normalised eigenform $g\in f^\perp$ congruent to $f$ at every $n$ modulo a prime $\lambda\mid\ell$ forces $\ell\mid r_E$.
Chapter 14 uses only the identity $r_E\Z_\ell=\eta_f\Z_\ell$. Paper: Lemma lem:crit; Lemma lem:hecke ("$r_E\Z_\ell$ is the congruence ideal ...
by Lemma lem:crit").

**8.3 `thm:moddeg:ars`** (theorem; R as a whole; the divisibility is **proved here** in 9.4, the equality for $\ell\nmid 2N$ with $E[\ell]$
irreducible in 10.3). (Agashe, Ribet and Stein, ARS12 Theorem 2.2 as the paper cites it; verify the number and the exact
hypotheses.) Let $E$ be optimal. Then $\deg\varphi_E\mid r_E$, and $v_p(\deg\varphi_E)=v_p(r_E)$ for every prime $p$ with $p^2\nmid N$. Proof idea of
ARS (one paragraph): with $A$, $B$ as in 6.3, the modular degree is the exponent of $H_1(J_0(N),\Z)/(H_1(A,\Z)+H_1(B,\Z))$ and the
congruence number is the exponent of $S_2(\Z)/(S_2(\Z)[I_f]+S_2(\Z)[J])$; the perfect pairing $S_2(\Z)\times\T\to\Z$ (Chapter 13) and the
action of $\T$ on $H_1$ compare the two, and they agree at $p$ when $H_1(X_0(N),\Z_p)$ is locally free of rank two over $\T\otimes\Z_p$ at the
relevant maximal ideal (multiplicity one, which ARS establish for $p^2\nmid N$, including Eisenstein and $p=2$ cases, by citing
Mazur, Ribet and others). Reference: ARS12 Sections 2 and 3 (cite the sections); Ribet83 (congruence primes); Zagier85 (the
first comparison of $\deg\varphi_E$ with congruence primes). Paper: Section 1, Section 3 preamble, Lemma lem:hecke, the remark
after Theorem thm:qual.

**8.4 `rem:moddeg:abc-size`** (remark; R). The size of $\deg\varphi_E$: the conjecture $\deg\varphi_E\ll_\varepsilon N^{2+\varepsilon}$ is equivalent to a form of the
abc conjecture (Frey; Mai-Murty; see ARS12 Section 2, as the paper cites it); lower bounds $\deg\varphi_E\gg N^{7/6-\varepsilon}$ are known
(Watkins; cite only if checked). Paper: Section 1 ("its size is tied to deep questions").

**8.5 `ex:moddeg:99a1-and-726a1`** (worked example; P as a computation, Part 6.6; R for the comparison with ARS12 Table 1).
Congruence numbers computed directly (integral basis of $S_2(\Gamma_0(N);\Z)$ by saturating the $q$-expansions to beyond the Sturm
bound; the Hecke matrices on it; the primitive integral functional $\lambda$ that is a common left eigenvector with eigenvalues
$\phi_f(T_p)$, $p\le19$, which vanishes exactly on $f^\perp\cap S_2(\Z)$; then $r_E=|\lambda(f)|$, by the cyclic-quotient argument of Lemma
lem:crit):

| curve | $N$ | $\deg\varphi_E$ | $r_E$ | $r_E/\deg\varphi_E$ | primes $p$ with $p^2\mid N$ |
|-|-|-|-|-|-|
| 11a1 | $11$ | $1$ | $1$ | $1$ | none |
| 20a1 | $20$ | $1$ | $1$ | $1$ | $2$ |
| 37a1 | $37$ | $2$ | $2$ | $1$ | none |
| 77c1 | $77$ | $6$ | $6$ | $1$ | none |
| 99a1 | $99$ | $4$ | $12$ | $3$ | $3$ |
| 99b1, 99c1 | $99$ | $12$ | $12$ | $1$ | $3$ |
| 99d1 | $99$ | $6$ | $6$ | $1$ | $3$ |
| 121a1 | $121$ | $6$ | $6$ | $1$ | $11$ |
| 539c1 | $539$ | $288$ | $288$ | $1$ | $7$ |
| 726a1 | $726$ | $144$ | $1584$ | $11$ | $11$ |
| 980i1 | $980$ | $2880$ | $2880$ | $1$ | $2$, $7$ |

So 99A1 has $\deg\varphi_E=4$ and $r_E=12$ exactly as ARS12 Table 1 and the paper's remark after Theorem thm:qual say, and the
discrepancy is at $3$ with $3^2\mid99$. The congruence behind $3\mid r_E$: $f_{99a}\equiv f_{99b}\equiv f_{99d}\pmod3$ coefficientwise (checked for
$n\le30$, beyond the Sturm bound $B_2(99)=24$ of Chapter 12, its 11.3; both are newforms of level $99$, hence in $f^\perp$). The
paper's own 726a1 is a second example, with ratio $11$ and $11^2\mid726$. In every other case of the table the two numbers agree,
also at primes $p$ with $p^2\mid N$: the equality can hold there, it is just not guaranteed. Paper: the remark after Theorem
thm:qual ("Table 1 of ARS12 lists the curve 99A1 ... with modular degree $4$ and congruence number $12$"), Section 1, Lemma
lem:hecke ("as $\ell^2\nmid N$").

### Section 9. The modular degree as a congruence ideal (important_notes.md point 39)

The section opens with one paragraph: the paper proves $v_\ell(\deg\varphi_E)\ge v_\lambda(\eta^\emptyset_{f,\lambda})$ (Lemma lem:hecke) and needs multiplicity
one (Remark rem:free) for equality; for the optimal curve the lattice $M_{f,\ell}$ is the pullback of $H^1(E)$, the projection formula
computes the pairing on it, and the equality holds unconditionally. Everything in 9.1 to 9.5 is proved; 9.6 lists what
must still be compared with DFG04.

**9.1 `prop:moddeg:mf-is-pullback`** (proposition; P given 4.4, 5.1, 6.2 and Chapter 8, its 11.5, 11.7, 11.8, 12.2(a); the Chapter 15 outline's
2.6(ii) states the same result and should cite this item, Part 7, B-c). Let $E$ be optimal with newform $f$ and let $\ell$ be any prime. (a) **Hecke equivariance.** $\varphi_{E*}=\pi_{f*}\circ\iota_*\colon H_1(X_0(N),\Z)\to H_1(E,\Z)$ satisfies
$\varphi_{E*}\circ t_*=\phi_f(t)\,\varphi_{E*}$ for $t\in\T$ ($\T$ acts on $E=J_0(N)/I_fJ_0(N)$ through $\phi_f$); transposing (C2), $t^*\varphi_E^*x=\phi_f(t)\varphi_E^*x$ for $x\in H^1(E,\Z_\ell)$,
so $\varphi_E^*H^1(E,\Z_\ell)\subseteq M_{f,\ell}$. (b) **Ranks.** Both are free of rank $2$ ($\varphi_E^*$ is injective, since $\varphi_{E*}\varphi_E^*=\deg\varphi_E\ne0$; $M_{f,\ell}$ by
4.4). (c) **Saturation.** $E$ is optimal, so $\varphi_{E*}$ is surjective on $H_1$ and $\varphi_E^*H^1(E,\Z)$ is saturated (6.2(iii)); saturation is kept by
$\otimes\Z_\ell$. A saturated sublattice of full rank in the saturated lattice $M_{f,\ell}$ equals it. Hence
$$M_{f,\ell}=\varphi_E^*H^1(E,\Z_\ell).$$
(d) **Galois structure** (important_notes.md points 26, 40). $\varphi_E$ is defined over $\Q$, so in etale cohomology $\varphi_E^*$ is
$G_\Q$-equivariant and $M_{f,\ell}\simeq H^1_{\mathrm{et}}(E_{\bar\Q},\Z_\ell)\simeq\Hom_{\Z_\ell}(T_\ell E,\Z_\ell)\simeq T_\ell E(-1)$ (Weil pairing): an equality of lattices up to this
canonical isomorphism, with no irreducibility hypothesis; and $\ad M_{f,\ell}\simeq\ad T_\ell E$ ($\ad$ is insensitive to duals and twists,
Chapter 4). Paper: Section 4.1 ($M_{f,\lambda}$), Section 4.2 ("the lattice $M_{f,\lambda}$ of DFG04 and $T_\ell E$ are homothetic when $\bar\rho$ is
irreducible": correct up to the dual, and exact for the optimal curve), Lemma lem:hecke ("$L[\wp]=M_{f,\lambda}$ has rank $2$").

**9.2 `lem:moddeg:wn-on-mf`** (lemma; P given 4.4(iii)). $w_N^*$ acts on $M_{f,\ell}=\varphi_E^*H^1(E,\Z_\ell)$ by $\varepsilon_N(f)=\pm1$; so $\hat\delta(x,y)=\varepsilon_N(f)\langle x,y\rangle$ on
$M_{f,\ell}$. (Equivalently: $w_N$ preserves $I_fJ_0(N)$ by 4.2(iii), descends to the automorphism $[\varepsilon_N(f)]$ of $E$, and
$\varphi_E\circ w_N=\varepsilon_N(f)\,\varphi_E+\varphi_E(0)$ (evaluate at $\infty$ to check the constant); Exercise 13.) Paper:
Section 4.1 ("composed with ... $w_{M^\Sigma}$").

**9.3 `thm:moddeg:degree-is-eta`** (theorem; P). Let $E$ be optimal and $\ell$ any prime. On $M_{f,\ell}$ the pairing $\hat\delta$ of 3.4 has
$$\hat\delta(\varphi_E^*a,\varphi_E^*b)=\varepsilon_N(f)\,\deg\varphi_E\,\langle a,b\rangle_E\qquad(a,b\in H^1(E,\Z_\ell)),$$
with $\langle\ ,\ \rangle_E$ unimodular (Chapter 8, its 10.3). Hence the ideal of values of $\hat\delta$ on $M_{f,\ell}\times M_{f,\ell}$ is $\deg\varphi_E\cdot\Z_\ell$, and the
Gram determinant of $\hat\delta$ on a basis of $M_{f,\ell}$ is $(\deg\varphi_E)^2$ up to a unit (a rank-two alternating form, Chapter 3, its 9.4).
**Consequently, if DFG04's ideal $\eta^\emptyset_{f,\lambda}$ is the ideal of values of $\hat\delta_!$ on $M_{f,\lambda}$, as the paper's Section 4.1 describes it,
then $v_\lambda(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$ for every prime $\ell\nmid2N$, with no multiplicity-one, irreducibility or Gorenstein
hypothesis.** Proof: 9.1, 9.2, 6.3(iv). Physics aside: the projection formula is the statement that a loop on $E$ lifts to
$\deg\varphi$ loops whose intersection numbers add up. Paper: Lemma lem:hecke, Remark rem:free, Theorem thm:main
("with equality when ... free"), important_notes.md point 39.

**9.4 `cor:moddeg:ars-divisibility`** (corollary; P given 9.3, 8.2 and Chapter 3, its 9.3, 11.1, 11.3). For $E$ optimal and every
prime $\ell$: $v_\ell(r_E)\ge v_\ell(\deg\varphi_E)$; that is, $\deg\varphi_E\mid r_E$ (the divisibility half of 8.3). Proof (the assembly of Chapter 3, its
11.3, in the case at hand; Chapter 20 proves the general statement as Lemma lem:ddt417): take $\mathcal O=\Z_\ell$, the algebra $\T_\ell=\T\otimes\Z_\ell$
acting by $t^*$ on $L=H^1(X_0(N),\Z_\ell)$ with the pairing $\hat\delta$ (perfect, $\T_\ell$ self-adjoint, 3.4), $\pi=\phi_f$, $\wp=I_f\T_\ell$, $I=\operatorname{Ann}(\wp)$, so
that $\pi(I)=r_E\Z_\ell$ by 8.2 and $\wp\cap I=0$ by 8.1(iii). Then $L[\wp]=M_{f,\ell}$, $Q=L/(L[\wp]\oplus L[I])$ is killed by $r_E$ and generated by $2$
elements, and $Q\simeq\coker(M_{f,\ell}\to\Hom(M_{f,\ell},\Z_\ell))$ has order $\#\Z_\ell/(\deg\varphi_E)^2$ by 9.3; so $2v_\ell(\deg\varphi_E)\le2v_\ell(r_E)$. Equality holds
when $L_{\mathfrak m}$ is free over $\T_{\mathfrak m}$ (Chapter 3, its 11.3(v)), for instance in the situation of 10.3. Paper: Section 1 ("By a theorem
of Agashe, Ribet and Stein, $\deg\varphi_E$ divides the congruence number"), Lemma lem:hecke.

**9.5 `thm:moddeg:lem-hecke`** (theorem, the paper's Lemma lem:hecke in the strengthened form; P given 8.3 (R) and 9.3). Let $E$
be optimal and $\ell$ an odd prime with $\ell\nmid N$. Then
$$v_\ell(\deg\varphi_E)=v_\ell(r_E)=v_\ell\bigl(\text{ideal of values of }\hat\delta\text{ on }M_{f,\ell}\bigr),$$
the first equality by ARS12 Theorem 2.2 ($\ell^2\nmid N$), the second by 9.3; and, with DFG04's normalisation as the paper reads
it, both equal $v_\lambda(\eta^\emptyset_{f,\lambda})$. The hypotheses "$\bar\rho$ irreducible" and "free over $\T_{\mathfrak m}$" of the paper's Lemma lem:hecke are
not needed for this. Consequences (stated, proved in Chapter 20 where the assembly lives): (a) the identity (eq:identity) of
Theorem thm:main holds **with equality** whenever $\ell\notin S_f$; (b) Step 4 of the proof of Theorem thm:quant needs no
freeness at level $N_S$ (apply 9.3 to the optimal curve in the class of $E_S$, then ARS at $N_S$), which partly answers
important_notes.md point 24; (c) Remark (2) after Theorem thm:quant still needs multiplicity one at level $N$, because there the
lattice belongs to the depleted form $g^S$, which is not the pullback of an elliptic curve under an optimal map (10.4). Paper:
Lemma lem:hecke, Remark rem:free, Theorem thm:main, Theorem thm:quant.

**9.6 `rem:moddeg:dfg-normalisation`** (remark; R: what remains to be checked against DFG04 before the paper or the book
asserts 9.5 for DFG04's $\eta$). 9.3 is a theorem about the ideal of values of $\langle x,w_N^*y\rangle$ on $H^1(X_0(N),\Z_\ell)[I_f]$. That this is
DFG04's $\eta^\emptyset_{f,\lambda}$ needs five checks in DFG04 Sections 1.5.3, 1.6.1, 1.6.2, 1.7.3 and (13), (14):
(1) **Which curve.** That DFG04's integral structure $M(N,1)_{!,\lambda}$ for weight $2$ and trivial character is $H^1(X_0(N),\Z_\ell)$ (as the
paper says), and not the trivial-character part of the cohomology of a $\Gamma_1(N)$-type curve: if it were
$H^1(X_1(N),\Z_\ell)^{(\Z/N)^\times}$, the pullback along $X_1(N)\to X_0(N)$ would multiply the cup product by the degree $\#(\Z/N)^\times/\{\pm1\}$, which
can be divisible by $\ell$ (for example $\ell=3$, $N=7\cdot m$), and its saturation would involve the Shimura subgroup (11.3).
(2) **Interior cohomology.** That "$!$" means the image of compactly supported cohomology of $Y_0(N)$ in cohomology, which for
constant coefficients is $H^1(X_0(N))$ (an exact-sequence argument: $H^1_c(Y)\to H^1(X)$ is onto and $H^1(X)\to H^1(Y)$ is injective), and
that group cohomology of $\Gamma_0(N)$ agrees with it for constant coefficients ($\Hom(\Gamma_0(N),\Z_\ell)=\Hom(\pi_1(Y_0(N)),\Z_\ell)$, the elliptic
elements being torsion; P). (3) **The operator.** That $[UwU]\omega$ is $w_N^*$ with no scalar factor in weight $2$ (Chapter 12, C3, C4
suggest so) and that DFG04's cup product lands in $H^2_c\simeq\Z_\ell$ with the standard normalisation (a factor $2$ from $\pm1$ is
harmless for odd $\ell$; at $\ell=3$ check the treatment of elliptic points of order $3$, which exist when every prime factor of $N$
is $1\bmod3$ and $9\nmid N$). (4) **Kernel, not projection.** That $M_{f,\lambda}$ is the kernel lattice $L[\wp]$ (saturated), as the paper says,
and not the image of $L$ under the projection to the $f$-component (the dual lattice, which would change the ideal of values
by the congruence ideal). (5) **Values versus Gram.** That $\eta$ is defined as the ideal of values (equivalently the square root of
the Gram determinant), as the paper says, and that DFG04 Theorem 3.7 and Proposition 1.4(c) are stated for this ideal. If all
five hold, 9.5 applies to DFG04's $\eta$ verbatim; if (3) or (5) differ by a unit nothing changes; if (1) or (4) differ, the paper's
own description of $\eta$ in Section 4.1 needs correcting, independently of point 39. Confidence of the book: high for 9.3,
medium for the identification. Paper: Section 4.1, Lemma lem:hecke, Theorem thm:dfg14, Theorem thm:dfg37.

**9.7 `ex:moddeg:99-at-3`** (worked example; P given 8.5, 9.3, 9.4 and Chapter 3, its 11.5). For 99a1 and $\ell=3$ (where $3^2\mid99$ and
the paper's theorems do not apply): the ideal of values of $\hat\delta$ on $M_{f,3}$ is $4\Z_3=\Z_3$ (9.3), while $v_3(r_E)=1$ (8.5). So the inequality
of 9.4 is strict, $L_{\mathfrak m}=H^1(X_0(99),\Z_3)_{\mathfrak m}$ is **not** free over $\T_{\mathfrak m}$ at the maximal ideal $\mathfrak m$ of 99a1 mod $3$, and by Chapter 3, its
11.5 (hypothesis (b) holds, rank $L_{\mathfrak m}=2\,\rank\T_{\mathfrak m}$), $\dim_{\T/\mathfrak m}L/\mathfrak mL>2$: multiplicity one fails for $J_0(99)$ at $\mathfrak m$, although
$\bar\rho_{\text{99a1},3}$ is irreducible (the class 99a has only a $2$-isogeny). This is why Remark rem:free needs $\ell\nmid N$. Paper: the remark
after Theorem thm:qual (99A1), Remark rem:free.

### Section 10. Multiplicity one, the Gorenstein property and Remark rem:free

**10.1 `def:moddeg:maximal-ideal`** (definition; P for (i), R for (ii)). (i) For $f=f_E$ and a prime $\ell$, $\mathfrak m=\mathfrak m_{f,\ell}$ is the maximal ideal of
$\T_\ell=\T\otimes\Z_\ell$ containing $\ell$ and $I_f$, the kernel of $\T_\ell\to\Z_\ell\to\F_\ell$; $\T_\ell=\prod_{\mathfrak m'}\T_{\mathfrak m'}$ (Chapter 3, its 10.3). (ii) There is a
semisimple representation $\bar\rho_{\mathfrak m}\colon G_\Q\to\GL_2(\T/\mathfrak m)$, unramified outside $N\ell$, with $\operatorname{tr}\bar\rho_{\mathfrak m}(\Frob_p)=T_p\bmod\mathfrak m$ and
$\det=\bar\chi_\ell$ (Chapter 15); for $\mathfrak m_{f,\ell}$ it is $\bar\rho_{E,\ell}^{\mathrm{ss}}$ (5.2, Chebotarev and Brauer-Nesbitt, Chapters 4, 5). $\mathfrak m$ is
Eisenstein if $\bar\rho_{\mathfrak m}$ is reducible (C7). Paper: Lemma lem:hecke ("$\mathfrak m$ the maximal ideal of $\T\otimes\Z_\ell$ containing $\ell$ and
$\ker\phi_f$"), Remark rem:free.

**10.2 `thm:moddeg:multiplicity-one`** (theorem; R, with the reduction to $J_1(N)$ sketched as in the paper). Let $\ell\nmid2N$ and $\mathfrak m$
non-Eisenstein. Then $J_0(N)[\mathfrak m]$ is $2$-dimensional over $\T/\mathfrak m$ (hence $\simeq\bar\rho_{\mathfrak m}$ by Boston-Lenstra-Ribet). References: Mazur77
(prime level; Chapter II, cite the section); Mazur's argument via the $q$-expansion principle mod $\ell$ and the good reduction of
$J_0(N)$ at $\ell$, as written in Ribet90 Section 5 (verify the theorem number); the paper's route: RibetStein Theorem 3.5 for $J_1(N)$
(as the paper cites it; check the exceptional case "Serre weight $\ell$" and that it cannot occur for weight $2$ and $\ell\nmid N$:
$\det\bar\rho=\bar\chi_\ell$ is ramified at $\ell$), and the pullback $J_0(N)[\mathfrak m]\to J_1(N)[\mathfrak m']$, injective because its kernel lies in the
Shimura subgroup (11.3), on which $\T$ acts through Eisenstein ideals. Paper: Remark rem:free.

**10.3 `thm:moddeg:gorenstein`** (theorem; P given 10.2, 4.3 and Chapter 3, its 11.4, 11.5). In the situation of 10.2: $\T_{\mathfrak m}$ is
Gorenstein, and $H^1(X_0(N),\Z_\ell)_{\mathfrak m}\simeq\T_{\mathfrak m}^2\simeq T_\ell J_0(N)_{\mathfrak m}$ as $\T_{\mathfrak m}$-modules (Tilouine97; Wiles95 Chapter 2; DDT Section 4, cite
the sections). Proof: $L=H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ with $\hat\delta$ (perfect on the summand, 3.4(iii)) satisfies (a) $\dim L/\mathfrak mL=\dim J_0(N)[\mathfrak m]=2$
(the pairing identifies $L/\mathfrak mL$ with the dual of $(L/\ell L)[\mathfrak m]$, and $L/\ell L$ with $J_0(N)[\ell]_{\mathfrak m}$ up to the Hecke-equivariant
identification 4.3(ii)) and (b) $\rank_{\Z_\ell}L=2\rank_{\Z_\ell}\T_{\mathfrak m}$ (4.4(i) for every eigensystem, localised); Chapter 3, its 11.5, applies.
Consequence: equality in 9.4 at such $\ell$, that is $v_\ell(r_E)=v_\ell(\deg\varphi_E)$ for $\ell\nmid2N$ with $E[\ell]$ irreducible, an independent proof of
this case of 8.3. Paper: Remark rem:free ("the localised Hecke algebra is then Gorenstein and the Tate module is free of
rank two \cite{Tilouine97}"), Lemma lem:hecke (equality clause).

**10.4 `rem:moddeg:rem-free-after-39`** (remark; P given 9.5). What Remark rem:free is still needed for, once 9.5 is known: (a)
not for the equality in Lemma lem:hecke or in (eq:identity) (9.5); (b) yes for the equality between the Hecke congruence ideal
and the cohomological one for forms that are not attached to an optimal quotient, in particular the depleted form $g^S$ of
Theorem thm:quant (Step 2 is an inequality without it, and Remark (2) after Theorem thm:quant uses multiplicity one at level
$N$); (c) as the conceptual reason for the equality in ARS12 at $\ell\nmid2N$ (10.3). It fails for $\ell\mid N$ in general (9.7: $N=99$,
$\ell=3$). Paper: Remark rem:free, Theorem thm:quant and the remark after it, important_notes.md points 24, 39.

### Section 11. The Eisenstein ideal, the cuspidal subgroup and the Shimura subgroup

**11.1 `def:moddeg:cuspidal-subgroup`** (definition and theorem; P for (ii), (iii), R for (i) in general). (i) The *cuspidal
subgroup* $C_N\subseteq J_0(N)(\bar\Q)$ is generated by the classes of the degree-zero divisors supported on the cusps; it is finite
(Manin-Drinfeld) and $G_\Q$-stable (2.2); its $G_\Q$-invariants contain the rational cuspidal subgroup generated by the classes of
$\Q$-rational cuspidal divisors. (ii) For $p\nmid N$: $T_p(\infty)=(p+1)(\infty)$ and $T_p(0)=(p+1)(0)$ as divisors (the $p+1$ matrices $\alpha_i$
of 3.2(i) fix $\infty$; they send $0$ to $0$ and to $j/p$, which are $\Gamma_0(N)$-equivalent to $0$ since $\gcd(p,N)=1$). (iii) Hence
$(T_p-1-p)_*$ kills $x=[(0)-(\infty)]$; $T_p-1-p$ is an isogeny of $J_0(N)$, its eigenvalues $a_p(g)-1-p$ on $S_2$ being nonzero by the
Ramanujan-Petersson bound $|a_p(g)|\le2\sqrt p<p+1$ (Chapter 12, its 6.5, R); so $x$ is torsion. This is Manin-Drinfeld for the two
rational cusps, in full. Reference: Manin (1972) and Drinfeld (1973) for (i), cited through DiamondShurman or Stein (book)
by section (verify where it is stated); Ogg73.
Paper: Conjecture conj:eis, Section sec:eis, Open question 4 ("presumably through the cuspidal subgroup of $J_0(N)$").

**11.2 `thm:moddeg:mazur-prime-level`** (theorem; R, with the example P). (Mazur77.) Let $N$ be prime and $n=\operatorname{num}\frac{N-1}{12}$. (i) The
class of $(0)-(\infty)$ has order $n$ and generates $C_N$. (ii) $J_0(N)(\Q)_{\mathrm{tors}}=C_N\simeq\Z/n$. (iii) The *Eisenstein ideal*
$I_{\mathrm{Eis}}\subseteq\T$ generated by $T_\ell-1-\ell$ ($\ell\ne N$) and $1+w_N$ satisfies $\T/I_{\mathrm{Eis}}\simeq\Z/n$; it annihilates $C_N$ and the Shimura
subgroup $\Sigma_N$ (11.3), which is $\mu$-type of order $n$ and Cartier dual to $C_N$. (iv) For $\ell$ odd, a maximal ideal $\mathfrak m\ni\ell$ is
Eisenstein in the sense of C7 iff $\mathfrak m\supseteq I_{\mathrm{Eis}}$, and such $\mathfrak m$ exist iff $\ell\mid n$ (Mazur77, Chapter II; verify the exact statement
and the cases $\ell=2$, $\ell=N$). Example (P, checked): $N=11$, $n=5$, $J_0(11)(\Q)=$ 11a1$(\Q)\simeq\Z/5$, $\ell=5$ is
Eisenstein, and $f_{11}\equiv$ the Eisenstein series $-\frac1{24}E_2^{(11)}\pmod5$ (Chapter 12, its 8.4); $N=37$, $n=3$, and 37b1 has
torsion $\Z/3$. Reference: Mazur77 (Chapter II; cite the sections; "Theorem 1" of the introduction for (ii), verify). Paper:
Conjecture conj:eis, Section sec:eis, Open question 4, Section 6 table of counts (the Eisenstein column).

**11.3 `def:moddeg:shimura-subgroup`** (definition and proposition; R for (ii), (iii), P for (i)). (i) The *Shimura subgroup*
$\Sigma_N=\ker(\pi^*\colon J_0(N)\to J_1(N))$, $\pi\colon X_1(N)\to X_0(N)$ the forgetful map; by Chapter 8, its 11.5(iii) (with $(d)\Leftrightarrow(a)$), $\Sigma_N=0$ iff
$\pi^*H^1(X_0(N),\Z)$ is saturated in $H^1(X_1(N),\Z)$. (ii) $\Sigma_N$ is finite, of multiplicative type (Cartier dual to a constant
group), and $T_\ell$ acts on it by $1+\ell$ for $\ell\nmid N$: it is Eisenstein (Mazur77 for prime $N$; Ling-Oesterle and Ribet88 in
general, cite the sections). (iii) So $\Sigma_N[\mathfrak m]=0$ for non-Eisenstein $\mathfrak m$, which is the injectivity used in 10.2. (iv) For the
optimal curve, $\bar\rho_{E,\ell}$ reducible (a rational $\ell$-isogeny, Chapter 11, its 9.1) iff $\mathfrak m_{f,\ell}$ is Eisenstein; then 10.2, 10.3,
DFG04 and Lemma lem:hecke's hypothesis fail, and the modular degree can lose local divisibility (the deficit $D$ of
Conjecture conj:eis; Chapter 11, its 9.3). Paper: Remark rem:free ("the Shimura subgroup, is Eisenstein"), Conjecture
conj:eis, Section sec:eis.

**11.4 `prop:moddeg:image-of-zero`** (proposition; P). Let $E$ be optimal with Manin constant $c_E$. Then $\varphi_E(0)\in E(\Q)_{\mathrm{tors}}$ (the cusp $0$
is rational, 2.2, and $\varphi_{E*}$ maps the torsion class $[(0)-(\infty)]$ of 11.1 to $\varphi_E(0)$), and under $E(\C)=\C/\Lambda_E$,
$$\varphi_E(0)\equiv\pm c_E\,L(E,1)\pmod{\Lambda_E},$$
because $\varphi_E(z)=\int_{i\infty}^zc_E\cdot2\pi i f(\tau)\,d\tau$ and $\int_0^{i\infty}2\pi if(\tau)\,d\tau=-2\pi\int_0^\infty f(iy)\,dy=-L(f,1)$ (Chapter 19; the sign depends on the
orientation conventions, state one). Since $\Lambda_E\cap\R=\Z\Omega_E$ with $\Omega_E$ the least positive real period, the order of $\varphi_E(0)$ is
the denominator of $L(E,1)/\Omega_E$ when $c_E=\pm1$. Checks (P, PARI): $L/\Omega=1/5$ (11a1, torsion $\Z/5$), $1/6$ (14a1, $\Z/6$), $1/6$ (20a1, $\Z/6$),
$1/3$ (19a1, $\Z/3$), $2/3$ (37b1, $\Z/3$), $1$ (121a1, trivial torsion), $0$ for the rank-one curves 37a1, 99a1, 539c1, 726a1 (so $\varphi_E(0)=O$).
Paper: Conjecture conj:eis and Open question 4 (a heuristic link between rational torsion, the cuspidal subgroup and the
Eisenstein deficit; the book says it is a heuristic, not an argument).

**11.5 `rem:moddeg:eisenstein-and-the-paper`** (remark; R, pointers). Why the Eisenstein case is outside every theorem of the
paper: Ihara's lemma and Proposition 1.4 of DFG04, multiplicity one (10.2), $\ell\notin S_f$, and the identification of $T_\ell E$ with
$M_{f,\lambda}$ up to homothety all use $\bar\rho$ irreducible (9.1 does not, but its use in DFG04 does). The paper's Conjecture conj:eis
bounds the deficit by torsion, and Open question 4 asks for an Eisenstein-ideal interpretation; important_notes.md point 17
(Chapter 9, its 9.8) proves the bound $D\le2$ from the first bound. Paper: Conjecture conj:eis, Section sec:eis, Open question 4.

### Section 12. Shimura curves, the prime $2$ and the computation of the modular degree

**12.1 `def:moddeg:shimura-curve`** (definition; R). For $D$ a product of an even number of distinct primes and $M$ prime to $D$,
$X_0^D(M)$ is the Shimura curve attached to an Eichler order of level $M$ in the indefinite quaternion algebra over $\Q$ of
discriminant $D$; it is a smooth projective curve over $\Q$ without cusps. By Jacquet-Langlands (Ribet's form) its Jacobian is
isogenous to the $D$-new quotient of $J_0(DM)$, Hecke-equivariantly. For $E$ of conductor $N=DM$ with $D\,\|\,N$ (so $E$ is
multiplicative at every $q\mid D$) there is an optimal parametrisation $\varphi_{E,D}\colon X_0^D(M)\to E$ (defined via the Jacobian, a base
point being chosen; its degree does not depend on the choice), of degree $\delta_D$. Reference: Ribet90 (Shimura curves and
level lowering; cite the section), RibetTakahashi97, Takahashi01. Paper: Section 1.5 ("compared $\deg\varphi_E$ with the degree of a
parametrisation by a Shimura curve").

**12.2 `thm:moddeg:ribet-takahashi`** (theorem; R; check every hypothesis against the sources before printing). (Ribet and
Takahashi; Takahashi.) Let $E$ be optimal and semistable of conductor $N=DM$ as in 12.1. Then for every prime $\ell$ such that
$E[\ell]$ is irreducible (and under the further hypotheses of RibetTakahashi97 and Takahashi01, to be listed exactly)
$$v_\ell(\deg\varphi_E)=v_\ell(\delta_D)+\sum_{q\mid D}v_\ell(n_q),\qquad n_q=v_q(\Delta_E)=\#\Phi_q(\bar\F_q),$$
the order of the geometric component group at $q$ (the source must be checked on whether the arithmetic $c_q$ or the geometric
$n_q$ appears; they differ at nonsplit $q$, and the paper's Section 1.5 says $n_q$). Pasten controls the error term at the
reducible primes. Proof idea (one paragraph): Ribet's exact sequence relating the character groups of the tori of $J_0(N)$ at
$q$ and of $J_0^D(M)$ at another prime, and the component groups as cokernels of the monodromy pairing. Consequence: the
multiplicative part $v_\ell(\deg\varphi_E)\ge\sum_{q\mid D}t_\ell(E,q)$ of (eq:main) for the primes of $D$. Paper: Section 1.5 (history), Remark
rem:ko (Kim-Ota: the same congruence ideal in another guise; Chapter 15).

**12.3 `conj:moddeg:watkins`** (conjecture and data; R, with the data P). (Watkins02.) For every optimal $E/\Q$,
$2^{\operatorname{rank}E(\Q)}\mid\deg\varphi_E$. Data (Part 6.6): all $38{,}042$ optimal curves of conductor below $10{,}000$ satisfy it; examples 37a1 (rank $1$,
$\deg=2$), 99a1 ($1$, $4$), 539c1 ($1$, $288$), 726a1 ($1$, $144$). Known results (Dummigan06, CalegariEmerton09, Yazdani11, CaroPasten22,
HatleyKundu, BKP as the paper cites them) are listed without statements unless checked. Paper: Section sec:two, Open question 5.

**12.4 `thm:moddeg:calegari-emerton`** (theorem; R; the statement to be copied from CalegariEmerton09 with its exact
hypotheses). The paper's paraphrase: a curve of odd modular degree has at most two odd primes of bad reduction and either
a rational point of order $2$ or prime conductor. Data (Part 6.6): $103$ optimal curves of conductor below $10{,}000$ have odd
modular degree; all have at most two odd bad primes; all but two have a rational $2$-torsion point or prime conductor; the
two exceptions are 27a1 ($\deg=1$, torsion $\Z/3$) and 243b1 ($\deg=9$, torsion $\Z/3$), both with $j=0$ (CM by $\Z[\zeta_3]$). So the
paraphrase needs the hypothesis or exception that CalegariEmerton09 state (presumably "without CM", or prime-power
conductor allowed); Part 7, point N1. Paper: Section sec:two.

**12.5 `rem:moddeg:computing-the-degree`** (remark; R). Three methods: (a) Zagier: compute $\varphi_E$ on $H_1$ from modular symbols
and read the degree off the index of 6.3(iv) (Zagier85; Cremona97 Chapter II); (b) Watkins: $\langle f,f\rangle$ from the symmetric square
special value with the bad Euler factors, then 7.3 (Watkins02); (c) Cremona's period-lattice comparison used to certify
optimality (6.5). PARI's `ellmoddegree` implements (b) and needs `parisizemax` of a few hundred megabytes in the thousands
(the paper's appendix); Chapter 22 has the sessions. Paper: Section 1 ("The modular degree is computable"), Section 6, the
appendix.

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200). The card lists the 56 items of Part 2
(numbered 14.1 to 14.56 in the book; conventions C1 to C8 in one line each), about 170 lines, not counted.

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2 with its tag and `\Cref`; the formula of 7.3 and the identity of 9.3 displayed | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1 (optimal curve, $\varphi_E$, $\deg\varphi_E$, Zagier-Watkins, ARS, $r_E$, abc); Section 1.5 (Ribet-Takahashi); Section 3 preamble, Lemma lem:crit (stated), the remark on 99A1; Section 4.1 ($H^1(X_0(M^\Sigma),\Z_\ell)$, $\hat\delta_!$, $M_{f,\lambda}$); Lemma lem:hecke and Remark rem:free (with the strengthening 9.5 and the checklist 9.6); Section 4.2 ($M_{f,\lambda}$ versus $T_\ell E$); Theorem thm:main (equality), Theorem thm:quant Steps 2, 4; Section 6 (optimality, `ellmoddegree`); Conjecture conj:eis, Section sec:eis, Open question 4; Section sec:two, Open question 5 | 50 |
| 1 | Overview and conventions | the opening paragraph (the six uses, Part 1.1); C1 to C8 as `convention` environments; 1.1; a roadmap table "paper sentence $\to$ item" | 80 |
| 2 | The modular curve $X_0(N)$ over $\Q$ | 2.1 to 2.4; the cusp table for $N=20,99,121$; `paperlink`: Section 1 ($\varphi_E$ over $\Q$), Conjecture conj:eis (rational isogenies, point 17) | 140 |
| 3 | Hecke correspondences and adjoints | 3.1 to 3.5; the matrix computation $W_N\,\mathrm{diag}(1,p)\,W_N^{-1}=\mathrm{diag}(p,1)$ displayed; `paperlink`: Section 4.1 (the sentence on $w_{M^\Sigma}T_nw_{M^\Sigma}^{-1}$), point 36 | 170 |
| 4 | The Jacobian, its homology, the $f$-lattice | 4.1 to 4.4; the dimension table; a `warning` box "Albanese versus Picard, $H_1$ versus $H^1$, $\operatorname{PD}$ versus $w_N\circ\operatorname{PD}$" (points 26, 41) | 160 |
| 5 | Eichler-Shimura and modularity | 5.1 to 5.5; the class 11a in full; one page of history of modularity; `paperlink`: Section 1 ("the newform attached to it") | 150 |
| 6 | Optimal curves and the modular degree | 6.1 to 6.6; the proof of 6.2(ii) to (iv) in full, (i) sketched; the running table; `paperlink`: Section 1 ("minimal degree"), Section 6 (optimality, point 25), point 27 | 190 |
| 7 | The Manin constant and the Zagier-Watkins formula | 7.1 to 7.5; the three-line proof of 7.3; the numerical table; `warning`: where $c^2$ stands (B10) and which Petersson normalisation | 120 |
| 8 | The congruence number and Agashe-Ribet-Stein | 8.1 to 8.5; the computation of $r_E$ explained as an algorithm; the table; `paperlink`: the remark after Theorem thm:qual (99A1) | 140 |
| 9 | The modular degree as a congruence ideal | 9.1 to 9.7; all proofs in full; a `paperlink` quoting Lemma lem:hecke and stating the strengthened form; the checklist 9.6 as a `remark` with the five items numbered; the 99 at 3 example | 200 |
| 10 | Multiplicity one and the Gorenstein property | 10.1 to 10.4; `paperlink`: Remark rem:free, line by line, with what point 39 changes | 130 |
| 11 | Eisenstein ideal, cuspidal and Shimura subgroups | 11.1 to 11.5; the computation $T_p(0)=(p+1)(0)$; the table of $L(E,1)/\Omega_E$ against torsion; `paperlink`: Conjecture conj:eis, Section sec:eis, Open question 4 | 140 |
| 12 | Shimura curves, the prime $2$, computing $\deg\varphi_E$ | 12.1 to 12.5; `paperlink`: Section 1.5, Section sec:two (with point N1 of Part 7), the appendix (`ellmoddegree`) | 130 |
| 13 | Exercises | the 17 exercises of Part 4.2 | 140 |
| 14 | Notes and references | Shimura71, DiamondShurman, DiamondIm, Cremona97, Zagier85, Watkins02, ARS12, Mazur77, Mazur78, Ribet90, RibetStein, Tilouine97, Wiles95, TaylorWiles, BCDT, Carayol86, LingOesterle, Ribet88, RibetTakahashi97, Takahashi01, Pasten, CalegariEmerton09, AU96, the proposed keys of Part 6.5; which numbers were cited and which are marked (verify) | 45 |
| | **total** | | **1,985** |

________________________________________________________________________________

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| $X_0(N)$ as a smooth projective curve over $\Q$ (statement) | 2.1 |
| its cusps | 2.2, 11.1(ii) |
| its points over $\Q$ | 2.3, 2.4 |
| $J_0(N)$, abelian variety of dimension $g$, $J_0(N)(\C)=S_2^\vee/H_1(X_0(N),\Z)$ | 4.1 |
| the Hecke action on $J_0(N)$ by correspondences, $T_p(E,C)=\sum(E/D,(C+D)/D)$ | 3.1, 3.2, 4.2 |
| Eichler-Shimura relation $T_p=\Frob_p+\Frob_p^*$ mod $p$, $a_p(f)$ = trace of Frobenius | 5.2 |
| the Hecke action on $H^1(X_0(N),\Z)$ and $H_1$ | 3.2, 4.2, 4.3 |
| the cup product on $H^1(X_0(N),\Z)$ (perfect, alternating) | 3.4 (with Chapter 8, its 10.3) |
| adjoint of $T_n$ under the cup product is $w_NT_nw_N$; $\langle x,w_Ny\rangle$ perfect, alternating, all $T_n$, $U_p$ self-adjoint; $=\hat\delta_!$ of DFG04 | 3.3, 3.4, 9.6 |
| $T_\ell J_0(N)=H_1\otimes\Z_\ell$ and $H^1(X_0(N),\Z_\ell)$ dual; etale cohomology (statement) | 4.3 |
| the modularity theorem (statement, history) | 5.3, 5.4 |
| the abelian variety $A_f=J_0(N)/I_fJ_0(N)$; for rational $f$ the elliptic curve quotient | 5.1, 5.5 |
| the modular parametrisation $\varphi_E$ ($\infty\mapsto O$) | 6.1 |
| the $X_0(N)$-optimal curve: unique, connected kernel, strong Weil curve; Cremona label 1, checked to $400000$ | 6.2, 6.5 |
| the modular degree: degree of the morphism; $E^\vee\to J_0(N)\to E$ is $[\deg\varphi_E]$; computability | 6.3, 6.6, 12.5 |
| the Manin constant: definition, the conjecture $c=1$, known results, role in the formulas | 7.1, 7.2, 7.4 |
| the Zagier-Watkins formula $\deg\varphi_E=4\pi^2c^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$ with $\varphi^*\omega_E=c\,2\pi if\,dz$ | 7.3, 7.4, 7.5 |
| the congruence number $r_E$ and the congruence ideal; Lemma lem:crit (proved in Chapter 15) | 8.1, 8.2 |
| Agashe-Ribet-Stein: $\deg\varphi_E\mid r_E$, equality for $p^2\nmid N$; 99A1 with $\deg=4$, $r=12$; proof idea | 8.3, 8.5, 9.4, 10.3 |
| multiplicity one, $\mathfrak m$, $J_0(N)[\mathfrak m]$ two-dimensional (Mazur, Ribet-Stein 3.5, Shimura subgroup) | 10.1, 10.2, 11.3 |
| Gorenstein (Tilouine), $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ free of rank two; Remark rem:free | 10.3, 10.4 |
| the Eisenstein ideal, the cuspidal subgroup, the Shimura subgroup; Mazur at prime level; why reducible is Eisenstein | 11.1, 11.2, 11.3, 11.5 |
| Shimura curves and Ribet-Takahashi | 12.1, 12.2 |
| the abc connection ($\deg\varphi_E\ll N^{2+\varepsilon}$; ARS12 Section 2) | 8.4 |
| Watkins's conjecture; Calegari-Emerton | 12.3, 12.4 |
| Mazur's theorem on $J_0(N)(\Q)_{\mathrm{tors}}$ for prime $N$ | 11.2 |
| computing the modular degree (Watkins, Cremona, `ellmoddegree`) | 7.5, 12.5 |
| Section 6 row: optimal curve, modular parametrisation, modular degree, Manin constant | 6.1 to 6.6, 7.1 to 7.4 |
| Section 6 row: congruence ideal, $r_E$, $\eta^\Sigma$, $M_{f,\lambda}$, $\hat\delta_!$ (with 13, 20) | 3.4, 4.4, 8.1, 9.1 to 9.6 |
| Section 6 row: Agashe-Ribet-Stein | 8.3, 8.5, 9.4 |
| Section 6 row: multiplicity one, freeness, Gorenstein, $J_0(N)[\mathfrak m]$ (with 3, 20) | 10.1 to 10.4, 9.7 |
| Section 6 row: Eisenstein case, torsion, cuspidal subgroup, Eisenstein ideal (with 9, 11) | 11.1 to 11.5, 2.3 |
| Section 6 row: Petersson norm, Zagier, Watkins (with 12, 13, 19) | 7.3 to 7.5 |
| Section 6 row: $H^1(X_0(N),\Z_\ell)$, cup product, Atkin-Lehner, Hecke self-adjointness (with 8) | 3.3, 3.4, 4.3, 4.4 |
| Section 6 row: Ribet-Takahashi, Pollack-Weston, Kim-Ota, Tamagawa exponent (with 15, 20) | 12.2 (Pollack-Weston, Kim-Ota: Chapters 15, 20) |
| Section 6 row: Watkins's conjecture, Calegari-Emerton | 12.3, 12.4 |
| Section 6 row: the worked examples 11a1, 20a1, 99A1 (with 9, 15, 21, 22) | 2.4, 5.5, 6.6, 7.4, 8.5, 9.7, 11.4 |
| hook: Section 1 (optimal curve, modular degree, Petersson norm, Zagier, Watkins, ARS, congruence number) | 6.2, 6.3, 7.3, 8.1, 8.3 |
| hook: Lemma lem:crit (congruence number versus congruence ideal) | 8.1, 8.2 |
| hook: Lemma lem:hecke | 9.1 to 9.5 |
| hook: Remark rem:free | 10.2, 10.3, 10.4 |
| hook: Section 4.1 ($H^1(X_0(N),\Z_\ell)$, $\hat\delta_!$, Atkin-Lehner) | 3.3, 3.4, 4.4, 9.6 |
| hook: the remark after Theorem thm:qual (99A1) | 8.5, 9.7 |
| hook: Section 1.5 (Ribet-Takahashi) | 12.1, 12.2 |
| hook: Section sec:two (Watkins, Calegari-Emerton) | 12.3, 12.4 |
| hook: Conjecture conj:eis and Section sec:eis (Eisenstein ideal, cuspidal subgroup, Mazur) | 11.1 to 11.5 |
| hook: Open question 4 | 11.2, 11.4, 11.5 |
| also: Section 4.2 ($M_{f,\lambda}$ versus $T_\ell E$; points 26, 40) | 9.1(d) |
| also: Theorem thm:main (equality), Theorem thm:quant Steps 2, 4 and Remark (2) (point 39, point 24) | 9.5, 10.4 |
| also: what Chapters 8, 9, 11, 12 defer to Chapter 14 (Part 5) | 2.1 to 2.4, 3.1 to 3.4, 4.1 to 4.4, 5.1 to 5.5, 6.1 to 6.5, 7.1, 7.3, 9.1, 11.1 to 11.3 |

### 4.2 Exercises (Section 13 of the chapter), graded from easy to harder

1. List the cusps of $X_0(20)$, $X_0(99)$ and $X_0(121)$ with their denominators and fields of definition (2.2); check the counts
   $6$, $8$, $12$ against Chapter 12, its 4.2, and decide which are $\Q$-rational.
2. Compute $W_N\,\mathrm{diag}(1,p)\,W_N^{-1}$ and deduce $U_p^t=w_NU_pw_N$ (3.3). On the span of $f_{11}(z)$, $f_{11}(2z)$ in $S_2(\Gamma_0(22))$ write the
   matrix of $U_2$ (from $a_2(f_{11})=-2$) and of $w_{22}$ (Chapter 12, its 12.4(b)); check that $U_2$ is not self-adjoint for the Petersson
   product but that $w_{22}U_2w_{22}$ is its adjoint.
3. Prove 3.4(ii), (iii) in detail: $\hat\delta$ is alternating, every $t^*$ is self-adjoint, idempotents are self-adjoint and the
   $\mathfrak m$-decomposition is orthogonal (important_notes.md point 36).
4. Using Eichler-Shimura (5.2) and $X_0(11)=$ 11a1, prove $\#\text{11a1}(\F_p)=p+1-a_p(f_{11})$ for $p\ne11$, and check it for $p=2,3,5,7,13$ from the
   $\eta$-product (Chapter 12, its 9.2).
5. Show that $X_0(37)\to X_0(37)/w_{37}$ is a modular parametrisation of 37a1 of degree $2$, that 37a1 is optimal, and deduce
   $\deg\varphi_{\text{37a1}}=2$ without `ecdata` (2.4(c), 6.2).
6. Check the paper's claim that the optimal curve is the curve of minimal modular degree in its class on the class 11a: using
   6.2(ii) and the isogeny degrees $5,5,25$, list the minimal degrees of the parametrisations of 11a1, 11a2, 11a3, and confirm them
   with the volumes of 7.4.
7. (Manin constant.) From $\operatorname{vol}(\Lambda_{\text{11a3}})=5\operatorname{vol}(\Lambda_{\text{11a1}})$ and 7.3 show that the parametrisation of 11a3 has $c=5$, and that
   $c\in\Z$ in this case directly from the $5$-isogeny 11a1 $\to$ 11a3 ($\psi^*\omega=5\omega$).
8. Check the paper's claim that $\deg\varphi_{\text{121a1}}=6$ with the numbers of 7.4 (or recompute $\langle f,f\rangle$ with PARI's `mfpetersson`,
   remembering the factor $\mu(121)=132$).
9. Check the paper's claim (the remark after Theorem thm:qual, quoting ARS12 Table 1) that 99A1 has modular degree $4$ and
   congruence number $12$: (a) show $f_{99a}\equiv f_{99b}\pmod3$ for $n\le24$ and conclude by Sturm (Chapter 12, its 11.3) and Lemma lem:crit
   that $3\mid r_E$; (b) show $4\mid r_E$ from 9.4; (c) explain why this does not contradict ARS12 Theorem 2.2.
10. In the situation of Exercise 9 prove that $H^1(X_0(99),\Z_3)_{\mathfrak m}$ is not free over $\T_{\mathfrak m}$ and that $J_0(99)[\mathfrak m]$ has dimension at least $3$ over
    $\T/\mathfrak m$ (9.7, Chapter 3, its 11.5). Which hypothesis of Remark rem:free fails?
11. Check the paper's 726a1 against ARS12: $\deg\varphi_E=144=2^4\cdot3^2$ and $r_E=1584$. Which prime carries the discrepancy, and why is this
    allowed? (Describe the algorithm of 8.5; running it is optional.)
12. Prove 6.4: if $E[\ell]$ is irreducible, $v_\ell$ of the minimal parametrisation degree is the same for every curve of the class
    (important_notes.md point 27); give the counterexample at $\ell=5$ in the class 11a.
13. Prove $\varphi_E(0)\equiv\pm c_EL(E,1)\pmod{\Lambda_E}$ and $\varphi_E\circ w_N=\varepsilon_N(f)\varphi_E+\varphi_E(0)$ (11.4, 9.2). Compute the order of $\varphi_E(0)$ for 11a1 and
    for 37b1 from $L(E,1)/\Omega_E=1/5$, $2/3$, and compare with $E(\Q)_{\mathrm{tors}}$; explain why $\varphi_E(0)=O$ for 37a1.
14. Prove $T_p(\infty)=(p+1)(\infty)$ and $T_p(0)=(p+1)(0)$ for $p\nmid N$, and deduce Manin-Drinfeld for $[(0)-(\infty)]$ (11.1). For $N=11$ show
    that $5[(0)-(\infty)]=0$ using $T_2-3$ and the eigenvalue $a_2(f_{11})-3=-5$.
15. Check the paper's claim (Section sec:two) that Watkins's conjecture holds for 37a1, 99a1, 539c1 and 726a1, and find in
    `ecdata` the optimal curves of odd modular degree below conductor $100$; test the paper's paraphrase of Calegari-Emerton on
    27a1 and decide which hypothesis of CalegariEmerton09 excludes it (12.4).
16. Prove 9.1 and 9.3 for $N=11$ directly ($\varphi_E=\mathrm{id}$, $M_{f,\ell}=H^1(X_0(11),\Z_\ell)$, $w_{11}^*=-1$), and then for 37a1 using 2.4(c): the
    pullback of $H^1$ of $X_0(37)/w_{37}$ has cup-product values $2\Z$.
17. (Harder.) Let $\pi\colon X_1(N)\to X_0(N)$ be the forgetful map. Show $\langle\pi^*x,\pi^*y\rangle=\deg\pi\,\langle x,y\rangle$ and that $\pi^*H^1(X_0(N),\Z)$ is saturated iff
    the Shimura subgroup vanishes (11.3). Explain why this is the first item of the checklist 9.6.

________________________________________________________________________________

## 5. Dependencies and forward pointers

Results from other chapters used here:
* Chapter 3 (`ch:modules`): saturated sublattices and kernels (5.5), perfect pairings and the Gram determinant (9.1 to 9.4), adjoints
  (9.5), finite free algebras and idempotents (10.3, 10.5), congruence ideals and $\wp\cap I=0$ (11.1, important_notes.md point 19), the
  module ingredients of Lemma lem:ddt417 (11.3), Gorenstein and the freeness criterion (11.4, 11.5).
* Chapter 4 (`ch:reps`): $\ad$ is insensitive to duals and twists (9.1(d)); Brauer-Nesbitt (10.1).
* Chapter 5 (`ch:galois`): Chebotarev (6.2(i), 10.1).
* Chapter 8 (`ch:curves`): curves, morphisms and degree (its 6.4), Riemann existence and GAGA (8.3), positivity and area (9.4),
  $H_1$, $H^1$, cup product, Poincare duality (10.1 to 10.3), the Jacobian and Abel-Jacobi (11.1 to 11.4), **the degree and the cup
  product, the saturation criterion (11.5)**, torsion and Tate modules (11.6, 11.7), Weil pairing and etale cohomology (11.8),
  correspondences and their actions (12.1, 12.2), **adjoint = transpose and the self-adjointness lemma (12.3, 12.3(e))**.
* Chapter 9 (`ch:ellcurves`): isogenies and dual isogenies, the period lattice and its area (7.6), $a_p$ and $\#E(\F_p)$ (Section 8),
  rational isogenies and torsion (Section 9, 9.8), labels and the running table (12.1, 12.2).
* Chapter 10 (`ch:reduction`): the Neron model and Neron differential (7.1), $n_q=\#\Phi_q(\bar\F_q)$ at multiplicative primes (12.2).
* Chapter 11 (`ch:galrep`): reducible $\bar\rho$ and rational isogenies (its 9.1), the Eisenstein case (its 9.3).
* Chapter 12 (`ch:modforms`): $X_0(N)$ as a compact Riemann surface and its $\Q$-model as a statement (its 5.2, 5.4(v)), cusps (4.2),
  genus and $\dim S_2$ (5.3, 8.2), the slash operator (C3), $W_N$ and $w_N$ (12.1), $w_N^*$ on $\omega_f$ and on $H^1$ (12.2(iii)), the
  Petersson product and its normalisation (10.1, C5), Sturm (11.3), the Eisenstein congruence for $f_{11}$ (8.4), the $\eta$-product (9.2).
* Chapter 13 (`ch:hecke`): $\T$, $T_p$ and $U_p$ on $q$-expansions, newforms, multiplicity one and strong multiplicity one, $\varepsilon_N(f)$,
  Petersson adjoints, the perfect pairing $S_2(\Z)\times\T\to\Z$, $f^\perp$ $\T$-stable.

Black boxes imported from later chapters (stated with a forward `\Cref`, used only in examples, remarks and `paperlink`s, or as
named inputs of R items): Lemma lem:crit (Chapter 15; used in 8.2, 9.4, 9.5 as a cited result); the Galois representation
$\bar\rho_{\mathfrak m}$ (Chapter 15; 10.1); the Rankin-Shimura formula and $L(f,1)$ (Chapter 19; 7.5, 11.4); the assembly of Theorem thm:main
and Lemma lem:ddt417 in general (Chapter 20; 9.5(a), 9.4 proves only its case $d=2$ from Chapter 3); DFG04's definitions (Chapter 20;
9.6). The use of Lemma lem:crit in 9.4 is a forward reference to Chapter 15; to keep linear reading, Chapter 13 states the
identity $r_E\Z=\phi_f(\operatorname{Ann}I_f)$ if the Chapter 13 outline proves the perfect pairing (it then follows in five lines); otherwise
Chapter 14 states it with `\Cref{ch:modgalrep}` and says so.

Forward pointers (chapters that use this one):
* Chapter 15 (`ch:modgalrep`): $J_0(N)$, $A_f$, Eichler-Shimura (5.1, 5.2) for $\rho_{f,\lambda}$; $M_{f,\ell}\simeq T_\ell E(-1)$ for the optimal curve
  (9.1(d)) for Section 4.2 of the paper; the congruence number and ARS (8.1 to 8.3) for Theorem thm:qual ("it suffices to prove
  $\ell\mid r$"); 12.2 for Section 1.5 and Remark rem:ko.
* Chapter 19 (`ch:lfunctions`): 7.3 (the Petersson norm and the modular degree) for the Bloch-Kato heuristic; 11.4 ($L(E,1)$).
* Chapter 20 (`ch:congruence`): 3.4 ($\hat\delta_!$), 4.4 ($M_{f,\lambda}$), 9.1 to 9.6 (Lemma lem:hecke as an equality and the DFG04 checklist),
  10.2 to 10.4 (Remark rem:free), 8.1, 8.3, 8.5. Chapter 20 should cite 9.3 and 9.5 rather than re-derive them, and present the
  equality in (eq:identity) accordingly.
* Chapter 21 (`ch:paper`): A1 (Section 1: optimal curve, Zagier-Watkins, ARS), A1.9 (12.2), A3.7 (99A1: 8.5, 9.7), A4.1 (3.4, 4.4),
  A4.4 and A4.5 (9.5, 10.3, 10.4), A4.6 (9.1(d)), A6.10 and Open question 4 (11.1 to 11.5), A7.1 (12.3, 12.4).
* Chapter 22 (`ch:computation`): `ellmoddegree` (12.5, 7.4), `mfpetersson` and its normalisation (7.4), the congruence-number
  algorithm (8.5), the optimality convention (6.5), the $L(E,1)/\Omega$ check (11.4).

________________________________________________________________________________

## 6. Notes for the writer

### 6.1 Conventions to state (Section 1 of the chapter, as `convention` environments)

C1 to C8 of Part 1.2. In addition a `warning` box in Section 4: "Four identifications that are easy to confuse: (1) $T_\ell J_0(N)=H_1\otimes\Z_\ell$
(covariant, action $t_*$); (2) $H^1(X_0(N),\Z_\ell)=\Hom(T_\ell J_0(N),\Z_\ell)$ (contravariant, action $t^*$, Galois-equivariantly $T_\ell J_0(N)(-1)$); (3) $\operatorname{PD}$
intertwines $t^*$ with $(t^t)_*$; (4) $w_{N*}\circ\operatorname{PD}$ intertwines $t^*$ with $t_*$." And a `warning` box in Section 7: "$c^2$ in the numerator;
unnormalised Petersson product; PARI divides by $\mu(N)$".

### 6.2 Pitfalls

* **Albanese versus Picard.** $\T$ acts on $J_0(N)$ by $t_*$ (C2); some books use the Picard action $t\mapsto(t^t)_*=(w_Ntw_N)_*$. For $T_n$ with
  $(n,N)=1$ the two agree; for $U_p$ they differ by conjugation by $w_N$. Everything in this chapter (the quotient $A_f$, the lattice
  $M_{f,\ell}$, the congruence ideal) is invariant because $\phi_f$ is (4.2(iii)), but a writer who mixes the two in one computation
  will get wrong matrices. State the action every time.
* **"$\hat\delta$ is DFG04's $\hat\delta_!$" is the paper's reading, not a theorem of this chapter.** Say "the pairing of DFG04 as the paper
  describes it" and point to 9.6.
* **Point 39 is about the optimal curve.** 9.1 fails for a non-optimal curve (Chapter 8, its 11.5(v): the pullback has index $\deg\psi$ in
  its saturation), and for depleted forms there is no elliptic curve at all (10.4(b)). Do not write "$v(\eta)=v(\deg)$" for $g^S$.
* **Lemma lem:crit is proved in Chapter 15.** Chapter 14 states it (8.2) and uses only $r_E\Z_\ell=\eta_f\Z_\ell$; do not reprove it here
  (PLAN.md's Chapter 14 entry allows "here or in Chapter 20"; the split of this book puts the proof in Chapter 15).
* **ARS12 Theorem 2.2.** Quote it exactly as the paper does and mark the number (verify). The book proves the divisibility at
  every prime (9.4) and the equality only for $\ell\nmid2N$ with $E[\ell]$ irreducible (10.3); the equality for $p\,\|\,N$, for $p=2$ and in the
  Eisenstein case is ARS's, stated (R).
* **Equality of $\deg\varphi_E$ and $r_E$ at $p$ with $p^2\mid N$ is possible** (121a1, 539c1, 980i1, 99b1, 99d1 in 8.5); only the guarantee is lost.
  Do not write "differ at $p^2\mid N$".
* **The Manin constant.** $c_E=\pm1$ is a conjecture in general; the paper never needs it in a proof, only in the Section 1
  heuristic. Results about $c_E$ (7.2(iii)) must be checked against the sources; cite nothing from memory with a theorem
  number.
* **Optimality versus Cremona label $1$**: 990h is the exception (990h3); optimality is proved in the tables only up to $400000$ and
  for part of the range above (point 25).
* **Cusps and fields of definition.** The sign in the Galois action on cusps of denominator $c$ is convention-dependent (2.2(ii));
  only the field of definition is used.
* **Signs in 11.4.** $\varphi_E(0)=\pm c_EL(E,1)$: fix the orientation of the path from $i\infty$ to $0$ and the sign of $\omega_E$ once; the
  order of the point does not depend on them.
* **Ribet-Takahashi: $n_q$ or $c_q$.** The paper says $n_q$; the book must check the source (12.2) and say which.
* **Calegari-Emerton.** Copy the statement from the paper; the paper's paraphrase fails for 27a1 and 243b1 (12.4; Part 7, N1).
* **Theorem numbers marked (verify)**: Shimura71 7.9 and 7.14, DiamondShurman 6.6.6 and 8.7.x, ARS12 2.2, RibetStein 3.5, Ribet90 Section
  5, Mazur77's numbering, Mazur78 on the Manin constant. Cite by section unless checked.
* Typography (PLAN.md 7.2): "Eichler-Shimura", "Manin-Drinfeld", "Agashe-Ribet-Stein", "Ribet-Takahashi", "Calegari-Emerton",
  "Boston-Lenstra-Ribet", "Jacquet-Langlands" with plain hyphens; tables with `booktabs`.

### 6.3 What to leave to Chapters 8, 12, 13, 15, 19, 20

* **Chapter 8** (`ch:curves`): general curves, Jacobians, $H^1$ and the cup product, correspondences, adjoint $=$ transpose, the
  self-adjointness lemma 12.3(e), the degree-and-cup-product proposition 11.5 with the saturation criterion. Chapter 14 applies
  them to $X_0(N)$ (3.3, 3.4, 6.2(iii), 9.1, 9.3) and does not reprove them.
* **Chapter 12** (`ch:modforms`): $X_0(N)$ over $\C$, cusps, genus, the moduli bijection over $\C$, $W_N$ and $w_N$ on forms and on $X_0(N)$, the
  Petersson product and its numerics (its 10.4), Sturm. Chapter 14 adds the $\Q$-structure, rationality of cusps, rational
  points, and everything about $J_0(N)$.
* **Chapter 13** (`ch:hecke`): Hecke operators on forms and $q$-expansions, $\T$ as a ring, newforms, multiplicity one, Petersson
  adjoints, the perfect pairing with $S_2(\Z)$, twists (Atkin-Li), oldforms and $U_p$-eigenvalues. Chapter 14 adds only the
  correspondences, their compatibility with Chapter 13's operators (3.2) and the cup-product adjoints (3.3, 3.4).
* **Chapter 15** (`ch:modgalrep`): $\rho_{f,\lambda}$, local-global compatibility, Lemma lem:crit and Lemma lem:old in full, level lowering
  and level raising, Kim-Ota and Pollack-Weston. Chapter 14 states lem:crit (8.2), uses 5.2 to start the construction of $\rho_f$, and
  states Ribet-Takahashi (12.2).
* **Chapter 19** (`ch:lfunctions`): $L(f,s)$, $L(\operatorname{Sym}^2f,s)$, the Rankin-Shimura formula for $\langle f,f\rangle$ with the bad factors, point 30.
  Chapter 14 uses only $L(f,1)=2\pi\int_0^\infty f(iy)\,dy$ (11.4) and points to the rest (7.5).
* **Chapter 20** (`ch:congruence`): congruence modules in general, Wiles's numerical criterion and Lemma lem:ddt417 in full, DFG04's
  definitions of $M_{f^\Sigma,\lambda}$, $\eta^\Sigma$ and their Theorems 3.7, Proposition 1.4, the assembly of Theorem thm:main and the proof of
  Theorem thm:quant. Chapter 14 supplies Lemma lem:hecke in its strengthened form (9.5), the checklist (9.6) and Remark rem:free
  (10.3); Chapter 20 should cite them.

### 6.4 How the relevant important_notes.md points are handled

* **Point 39** (Lemma lem:hecke is always an equality). Proved in full in 9.1 to 9.5: saturation of $\varphi_E^*H^1(E)$ from the
  connectedness of $\ker(J_0(N)\to E)$ (6.2(iii), Chapter 8, its 11.5), Hecke equivariance (9.1(a)), $w_N$ by the Atkin-Lehner sign (9.2), the
  projection formula (6.3(iv)); conclusion $v_\lambda(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$ for every $\ell\nmid2N$, unconditionally, **provided DFG04's $\eta$ is the
  ideal of values of $\langle x,w_N^*y\rangle$ on $H^1(X_0(N),\Z_\ell)[I_f]$**. What remains to be checked against DFG04 is the five-item list 9.6: the
  curve ($X_0(N)$ versus a $\Gamma_1(N)$-type curve with trivial-character part), interior cohomology, the operator $[UwU]\omega$ without
  scalar and the normalisation of $H^2_c$ (including elliptic points at $\ell=3$), kernel lattice versus projection lattice, ideal of
  values versus Gram determinant. 9.5(a) to (c) state the consequences for Theorem thm:main and Theorem thm:quant.
* **Point 40** ($M_{f,\lambda}=\varphi_E^*H^1(E,\Z_\ell)\simeq T_\ell E(-1)$ exactly): 9.1(c), (d).
* **Point 26** ($M_{f,\lambda}$ is homothetic to the dual of $T_\ell E$): 9.1(d), with the `warning` of Section 4.
* **Point 41** (Tate module versus $H^1$ as Hecke modules): 4.3(ii), (iii): $w_{N*}\circ\operatorname{PD}$ is $\T$-equivariant and, after the twist by
  $\Z_\ell(-1)$, $G_\Q$-equivariant; freeness transfers.
* **Point 36** (the pairing stays perfect on the $\mathfrak m$-component): 3.4(iii), from Chapter 8, its 12.3(e), and 3.3.
* **Point 35** (other local factors lie in the kernel): 8.1(ii), citing Chapter 3, its 11.1(v); the `paperlink` for Lemma lem:hecke
  quotes the corrected wording.
* **Point 19** ($\wp\cap I=0$): 8.1(iii) and 9.4, citing Chapter 3, its 11.1(ii) (the argument uses $\eta\ne0$, which multiplicity one of the
  newform gives; not "$\T$ reduced").
* **Point 27** (optimality plays no role at $\ell$ when $E[\ell]$ is irreducible): 6.4, proved, with the class 11a at $\ell=5$ as the
  counterexample without irreducibility.
* **Point 24** (the abstract calls the Theorem thm:quant argument elementary): 9.5(b) removes multiplicity one from Step 4, but
  Step 4 still uses ARS12 at level $N_S$, Step 3 uses DFG04 Proposition 1.4 and Step 2 the commutative algebra; so "elementary"
  remains an overstatement, now a smaller one. The `paperlink` for Theorem thm:quant says this.
* **Point 25** (optimality established only up to $400000$ and for part of the classes beyond): 6.5 states exactly what is known.
* **B3** (Chapter 21 outline, A4.4 and A4.6): the Chapter 21 writer should cite 8.1(ii) for the "kernel, not annihilator" wording, 9.1(d)
  for $M_{f,\lambda}$ versus $T_\ell E$, and 9.5 for the equality; see also Part 7, B-a below.
* **B10** (the Manin constant in the numerator): 7.3, with the derivation and the class 11a check (7.4), and a `warning` box.
* **B14** (bibliography): every proposed key in 6.5 that another chapter also needs goes into `refs.bib`; the others into
  `bib/ch14.bib`. Checked: `refs.bib` already has DiamondIm, LingOesterle, Ribet88, Carayol86, Mazur78, AU96, Tilouine97, RibetStein,
  Shimura73, Stein, Ogg (but Ogg is the 1967 wild ramification paper, not Ogg 1973 on cusps), ecdata; no chapter bib file has any key
  yet except `bib/chA.bib`.
