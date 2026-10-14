# Chapter 13: Hecke operators, newforms and twists (`ch:hecke`, `chapters/ch13_hecke.tex`)

Stage 1 line-up. Part IV (Modular forms and modular curves), between Chapter 12 (spaces of modular forms, Petersson product,
Atkin-Lehner involutions, integrality and Sturm) and Chapters 14 and 15 (Jacobians and the modular degree; Galois
representations and level lowering). Target length 1,930 lines of LaTeX (card excluded; see Part 3), inside the 1,000 to 2,200
range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2 to 12
outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book and chapter or
section; a theorem number only where sure, otherwise marked "(verify)" or given by section); the paper's use by its `\label`
names, or "background". Every number quoted below (Hecke matrices, characteristic and minimal polynomials of $U_p$, dimensions of
new and old subspaces, ranks of Hecke algebras, determinants of the pairing, congruence numbers, conductors of twists, Sturm
bounds, Petersson Gram matrices, Rankin-Selberg residues) was checked by Python scripts in the session scratchpad
(`c1.py` to `c9.py`), using PARI/GP 2.17 through `cypari2` and Cremona's `ecdata` files for conductors below 10,000
(verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

The paper uses the Hecke theory of $S_2(\Gamma_0(N))$ in six places, and the chapter is built around them.

1. **The Hecke algebra and its perfect pairing with integral forms** (Section 3 preamble: "Let $\T$ be the Hecke algebra of level
   $N$, the subring of $\operatorname{End}S_2(\Gamma_0(N))$ generated over $\Z$ by all $T_n$, $n\ge1$, including the operators $U_p$ for $p\mid N$";
   Lemma lem:crit: "$\phi_f\colon\T\to\Z$, $T_n\mapsto a_n(f)$", "The pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$, $(g,t)\mapsto a_1(tg)$, is perfect",
   "the forms killed by $I$ are $\Z f$", "Every step holds verbatim over $\Z_\ell$"; Theorem thm:quant Step 1: "with the pairing
   $S_2(\Gamma_0(N);\Z_\ell)\times\T_\ell\to\Z_\ell$"). The chapter defines $T_n$ and $U_p$ (double cosets and $q$-expansions), proves
   commutativity, multiplicativity and the recursion, proves that $\T$ is free of rank $\dim S_2$ over $\Z$ and that the pairing is
   perfect (from Chapter 12's integral basis theorem and Sturm bound), and derives the dictionary "normalised eigenforms with
   values in $A$ = ring homomorphisms $\T\to A$", in particular the eigencharacter $\phi_f$ and the maximal ideals of $\T$.
2. **Petersson adjoints and the complement $f^\perp$** (Lemma lem:crit: "the $f$-line is $\T$-stable, and so is $f^\perp$, because $f$ is an
   eigenvector of the adjoints of the $T_n$ as well"; Lemma lem:old: "orthogonal to the newform $f$"; Theorem thm:twist: "$g^\perp$, the
   $\T$-stable complement of the $g$-line"). The chapter proves that $T_n$, $(n,N)=1$, is self-adjoint, that $U_p^\dagger=w_NU_pw_N$, and
   that $f^\perp$ is $\T$-stable for a newform $f$; it separates the Petersson complement from the $\T$-stable complement, which
   differ for non-newforms such as $g^S$ in Theorem thm:quant.
3. **Newforms, oldforms and strong multiplicity one** (Section 1: "the newform $f=f_E$"; Lemma lem:old: "a newform on $\Gamma_0(M)$ with
   $p^2\mid M$ has $a_p=0$ [AtkinLehner70, Theorem 3]"; Theorem thm:twist: "differing from that of $g$ at infinitely many $p$";
   Theorem thm:quant Step 1: "strong multiplicity one identifies the forms with the $T_p$-eigenvalues of $g$, $p\nmid N$, with the
   span of the $g(dz)$, $d\mid N/N_S$"). The chapter states Atkin-Lehner theory (decomposition into old and new parts, newform
   bases, multiplicity one), strong multiplicity one, and the local facts $a_p=0$ for $p^2\mid N$, $a_p=-\varepsilon_p$ for $p\,\|\,N$.
4. **$U_p$ on oldforms; stabilised and depleted forms; $f^\Sigma$, $M^\Sigma$, $\delta_p$** (Lemma lem:old: the eigenvalues of $U_p$ on the span
   of the $h(p^jz)$, the stabilisations, the depleted forms, "$U_p$ is not semisimple on this span when $0$ is a repeated
   eigenvalue"; Section 4.1: "Put $M^\Sigma=M\prod_{p\in\Sigma}p^{\delta_p}$ and let $f^\Sigma=\sum_{(n,\Sigma)=1}a_n(f)q^n$ be the $\Sigma$-depleted
   eigenform, of level $M^\Sigma$"; Theorem thm:quant Step 1: "the operators $U_q$, $q\in S$, have the eigenvalue $0$ with multiplicity
   one", "the others have $U_q$-eigenvalue $a_q(g)=\pm1$ ... or a root $\alpha,\beta$ ... which are $\ell$-adic units"). The chapter proves
   the full linear algebra (cyclic vector, Jordan blocks), the structure of $\T\otimes\Q$ and of its generalised eigenspaces, and the
   level of $f^\Sigma$, with the example at level $88$ where $\T\otimes\Q$ is not reduced (important_notes.md point 19).
5. **Twists** (Lemma lem:twist (iii): "the twist $g\otimes\chi$, with coefficients $a_n(g\otimes\chi)=\chi(n)a_n(g)$, is a newform of weight
   $2$ on $\Gamma_0(M')$, $M'=\operatorname{lcm}(M,q^2)$"; Theorem thm:twist: "$\iota\colon h\mapsto h\otimes\chi_S$ maps $S_2(\Gamma_0(N_S))$ into
   $S_2(\Gamma_0(\operatorname{lcm}(N_S,D^2)))$, preserves integrality, and sends an eigenform ... to an eigenform with eigenvalues twisted
   by $\chi_S(n)$"; Theorem thm:quant Step 1: "$\iota$ intertwines $T_p$ with $\chi_S(p)T_p$"). The chapter proves the elementary
   properties of the twist operator (Gauss sums, level, integrality, intertwining, $\iota\circ\iota=$ depletion) and states the
   theorem of Atkin and Li with its hypothesis $q^2\nmid M$, with examples where the level drops when $q^2\mid M$.
6. **Congruences between eigenforms** (Section 1: "$f\equiv g\pmod r$ coefficientwise"; Lemma lem:crit: "$a_n(g)\equiv a_n(f)\pmod\lambda$
   for every $n\ge1$"; Lemma lem:old: "the congruence for all $n$ then follows from the multiplicativity of the coefficients, from
   $a_{p^k}=a_p^k$ for $p\mid N$, and from the recursion"; Theorem thm:quant Step 1: idempotents of $\T_\ell$). The chapter proves
   that congruences at all primes give congruences at all $n$, that congruences away from $\Sigma$ give congruences of the
   $\Sigma$-depleted forms, and the decomposition $\T_\ell=\prod\T_{\mathfrak m}$ with its effect on forms and on the pairing.

It also states the $L$-function of a newform (Euler product, functional equation) and the Rankin-Selberg residue formula
with the normalisation of Chapter 12 (the exact relation with $L(\Sym f,2)$ at bad primes is Chapter 19's), and defines the
Hecke congruence ideal and the congruence number of a rational newform (the identity between them is the paper's Lemma
lem:crit, proved in Chapter 15).

It discharges the debts of earlier chapters: Chapter 12 (its C8, 6.2(e), 6.5, 6.6, 9.3, 10.3, 10.5(a), 11.2 and 11.4 as used
for the pairing, 11.4(v), 11.5, 12.4(b), (c), and its B2 = book-internal note B11: Chapter 12 states Shimura's integral-basis
theorem and proves its consequences, Chapter 13 proves the perfect pairing); Chapter 3 (its 9.6, 10.4, 10.5, 10.7(v), 10.8,
11.1(iv) and Exercise 14: the modular meaning of the shift operator, the level-$88$ example, multiplicity one); Chapter 6 (its
7.1: Galois conjugates of newforms are newforms, $K_f$ totally real); Chapter 8 (its 12.1(c): the Hecke algebra is the ring of
operators generated by the Hecke correspondences); Chapter 9 (its 8.3 and 10.4: $X^2-a_pX+p$, the recursion, twists of
newforms match twists of curves); Chapter 2 (its forward pointer: twisting by Dirichlet characters, Gauss sums, conductors in
Atkin-Li).

**The physics reader** meets three familiar objects, one sentence each: the Hecke recursion $T_{p^{r+1}}=T_pT_{p^r}-pT_{p^{r-1}}$ is the
three-term recursion of the Chebyshev polynomials of the second kind (RHB, special functions), with generating function
$\sum_rT_{p^r}X^r=(1-T_pX+pX^2)^{-1}$ (2.4); the self-adjoint commuting family $T_n$, $(n,N)=1$, diagonalised by an orthogonal basis of
eigenforms is the spectral theorem for commuting Hermitian operators (5.2); the functional equation of $L(f,s)$ comes from the
Mellin transform of $f(iy)$ (10.2), RHB's integral transforms.

### 1.2 Global conventions fixed in this chapter

* **C1 (weight, level, spaces).** $N\ge1$ is the level and $k\ge2$ an even weight; everything the paper needs is $k=2$, and every
  statement is given for $k=2$ first, with the general-$k$ form in parentheses where it costs nothing. $S_k(N)=S_k(\Gamma_0(N))$,
  $M_k(N)=M_k(\Gamma_0(N))$, trivial character throughout (the only characters are the quadratic twists of Section 9, which keep the
  character trivial because $\chi^2=1$). $S_2(N;A)=S_2(\Gamma_0(N);\Z)\otimes A$ for a commutative ring $A$ (Chapter 12, C6).
* **C2 (slash and double cosets).** The slash operator is Chapter 12's C3: $(f|_k\gamma)(z)=(\det\gamma)^{k/2}(cz+d)^{-k}f(\gamma z)$. For
  $\alpha\in\GL_2^+(\Q)$ with $\Gamma\alpha\Gamma=\bigsqcup_i\Gamma\alpha_i$ the double coset operator is
  $$[\Gamma\alpha\Gamma]_kf=(\det\alpha)^{k/2-1}\sum_if|_k\alpha_i.$$
  With this normalisation $[\Gamma\alpha\Gamma]_k$ coincides with Diamond-Shurman's operator (their slash carries $(\det\gamma)^{k-1}$ and
  no prefactor; the products agree), and in weight $2$ the prefactor is $1$. Say this once in a `convention` box.
* **C3 (names of Hecke operators; level dependence).** At level $N$ the operators are $T_n$, $n\ge1$; for a prime $p\mid N$ the operator
  $T_p$ is written $U_p$, as in the paper ("all $T_n$, $n\ge1$, including the operators $U_p$ for $p\mid N$"), and $T_{p^r}=U_p^r$. The
  operator $T_p$ depends on the level: for $h\in S_k(M)$ and $p\nmid M$, the operator $T_p$ of level $M$ and the operator $U_p$ of level
  $Mp$ differ, $T_p^{(M)}h=U_p^{(Mp)}h+p^{k-1}h(pz)$ (2.3). When two levels are in play the level is written as a superscript.
  The letter $U$ alone never denotes an operator on $q$-series; $V_d$ denotes $h(z)\mapsto h(dz)$.
* **C4 (Hecke algebras).** $\T=\T_N=\Z[T_n:n\ge1]\subset\operatorname{End}_\C S_2(N)$ is the full Hecke algebra of level $N$ (the paper's $\T$);
  $\T^{(N)}=\Z[T_n:(n,N)=1]$ is the anemic Hecke algebra; $\T_A=\T\otimes_\Z A$, $\T_\ell=\T\otimes\Z_\ell$. Unless said otherwise $\T$ acts on cusp
  forms of weight $2$ (not on $M_2$, where the Eisenstein series would add a factor).
* **C5 (eigenforms).** An *eigenform* is a nonzero simultaneous eigenvector of all of $\T$ (all $T_n$ including the $U_p$); an
  *anemic eigenform* is one for $\T^{(N)}$ only; *normalised* means $a_1=1$; a *newform* is a normalised eigenform in the new
  subspace (6.1, 6.2). A *system of eigenvalues* is a ring homomorphism $\T\to\overline\Q$ (or $\T^{(N)}\to\overline\Q$); its *generalised
  eigenspace* $V(\varphi)$ is as in Chapter 3, its 10.5. The *$\T$-stable complement* of a generalised eigenspace is the sum of the
  other generalised eigenspaces.
* **C6 (Petersson product and adjoints).** The Petersson product is Chapter 12's C5 (unnormalised, linear in the first variable;
  PARI's `mfpetersson` divides it by $\mu(N)$). Adjoints are written $t^\dagger$ (book-internal note B4: $*$ is reserved for
  pullbacks and Pontryagin duals; Chapter 8 uses $\dagger$ too).
* **C7 (characters and twists).** For a Dirichlet character $\chi$ of conductor $r$, $f\otimes\chi=\sum_n\chi(n)a_n(f)q^n$ with $\chi(n)=0$ when
  $(n,r)>1$. For an odd prime $q$, $q^*=(-1)^{(q-1)/2}q$ and $\chi_{q^*}=\bigl(\frac{q^*}{\cdot}\bigr)$ is the quadratic character of conductor $q$ (the
  paper's $\chi_q$; the chapter writes $\chi_{q^*}$, as Chapter 2 decided, to avoid the clash with the cyclotomic $\chi_\ell$,
  important_notes.md point 32). For a finite set $S$ of odd primes, $D=\prod_{q\in S}q$ and $\chi_S=\prod_{q\in S}\chi_{q^*}$, of conductor $D$.
* **C8 (depletion).** For a finite set $\Sigma$ of primes and a $q$-series $h=\sum a_nq^n$, $h^\Sigma=\sum_{(n,\Sigma)=1}a_nq^n$, where $(n,\Sigma)=1$
  means that no prime of $\Sigma$ divides $n$ (the paper's notation). For a single prime, $h^{(p)}=h^{\{p\}}$.
* **C9 (congruences).** "$f\equiv g\pmod{\mathfrak a}$" means coefficientwise at **all** $n\ge1$ (Chapter 12, C6); a congruence only at the
  primes outside a set is always written out as such. $\lambda$ is a prime of the ring of integers $\mathcal O$ of a number field, above
  $\ell$.
* **C10 (typography).** PLAN.md Section 7.2: plain hyphens in "Atkin-Lehner", "Atkin-Li", "Rankin-Selberg", "Petersson",
  "Eichler-Shimura", "Coleman-Edixhoven"; ranges "1 to 8"; labels `...:hecke:...`; tables with `booktabs`.

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 2. Hecke operators: double cosets and $q$-expansions

**2.1 `def:hecke:double-coset`** (definition and proposition; P). Let $\Gamma=\Gamma_0(N)$ and $\alpha\in\GL_2^+(\Q)$. (i) $\Gamma\cap\alpha^{-1}\Gamma\alpha$ has
finite index in $\Gamma$ (both contain $\Gamma(m)$ for a suitable $m$: scale $\alpha$ to an integer matrix and take $m=N\det\alpha$), so
$\Gamma\alpha\Gamma=\bigsqcup_{i=1}^r\Gamma\alpha_i$ is a finite disjoint union, $r=[\Gamma:\Gamma\cap\alpha^{-1}\Gamma\alpha]$. (ii) The operator $[\Gamma\alpha\Gamma]_k$ of C2 does
not depend on the representatives $\alpha_i$ and maps $M_k(N)$ to $M_k(N)$ and $S_k(N)$ to $S_k(N)$ (right multiplication by $\gamma\in\Gamma$
permutes the cosets $\Gamma\alpha_i$; each $f|_k\alpha_i$ is holomorphic and bounded, respectively vanishing, at every cusp by Chapter 12,
its 6.2). Reference: DiamondShurman 5.1 (cite the section); Shimura71 3.1 (cite the section). Paper: background (the definition
of $\T$ in the Section 3 preamble).

**2.2 `prop:hecke:coset-decomposition`** (proposition and definition; P). Let $p$ be prime and $\Gamma=\Gamma_0(N)$. (i) If $p\nmid N$,
$$\Gamma\begin{psmallmatrix}1&0\\0&p\end{psmallmatrix}\Gamma=\bigsqcup_{j=0}^{p-1}\Gamma\begin{psmallmatrix}1&j\\0&p\end{psmallmatrix}\ \sqcup\ \Gamma\begin{psmallmatrix}p&0\\0&1\end{psmallmatrix}\qquad(p+1\text{ cosets});$$
(ii) if $p\mid N$, $\Gamma\begin{psmallmatrix}1&0\\0&p\end{psmallmatrix}\Gamma=\bigsqcup_{j=0}^{p-1}\Gamma\begin{psmallmatrix}1&j\\0&p\end{psmallmatrix}$ ($p$ cosets). Define
$T_p=[\Gamma\operatorname{diag}(1,p)\Gamma]_k$ on $M_k(N)$, written $U_p$ when $p\mid N$ (C3). Proof: the coset space is in bijection with the
matrices of determinant $p$ with lower left entry divisible by $N$ modulo left multiplication by $\Gamma$ (row reduction to upper
triangular form); for $p\mid N$ every element of the double coset has upper left entry prime to $p$ (it is $\equiv a_1a_2\pmod p$ with
$a_1a_2$ a unit, since $p\mid c_i$), which excludes $\operatorname{diag}(p,1)$. Reference: DiamondShurman
5.2 (cite the section; their Proposition 5.2.1 is the decomposition for $\Gamma_1(N)$, verify); Shimura71 3.4. Paper: Section 3
preamble ($\T$ contains the $U_p$).

**2.3 `prop:hecke:Tp-q-expansion`** (proposition; P). For $f=\sum_{n\ge0}a_nq^n\in M_k(N)$ and $p$ prime:
$$a_n(T_pf)=a_{pn}(f)+p^{k-1}a_{n/p}(f)\quad(p\nmid N),\qquad a_n(U_pf)=a_{pn}(f)\quad(p\mid N),$$
for all $n\ge0$, with $a_{n/p}=0$ when $p\nmid n$. In weight $2$: $a_n(T_pf)=a_{pn}+p\,a_{n/p}$. Equivalently, with $V_p$ of C3 and the
operator $\sum a_nq^n\mapsto\sum a_{pn}q^n$ on $q$-series: $T_p^{(M)}h=U_p^{(Mp)}h+p^{k-1}V_ph$ for $h\in M_k(M)$, $p\nmid M$ (the level dependence of
C3). Proof: $f|_k\begin{psmallmatrix}1&j\\0&p\end{psmallmatrix}=p^{-k/2}f(\frac{z+j}p)$, and $\sum_{j=0}^{p-1}e^{2\pi in(z+j)/p}$ is $p\,q^{n/p}$ or $0$; $f|_k\operatorname{diag}(p,1)=p^{k/2}f(pz)$;
multiply by $p^{k/2-1}$. Reference: DiamondShurman Proposition 5.2.2 (verify) and 5.3; SerreCourse VII.5.3 (level one);
Miyake 4.5. Paper: Section 3 preamble, Lemma lem:old ("$U_ph(p^jz)=h(p^{j-1}z)$", "$U_ph=a_p(h)h-p\,h(pz)$"), Theorem thm:twist and Theorem
thm:quant Step 1 (the intertwining of 9.1).

**2.4 `thm:hecke:Tn`** (definition and theorem; P). Define $T_1=1$, $T_{p^{r+1}}=T_pT_{p^r}-p^{k-1}T_{p^{r-1}}$ for $p\nmid N$ and $r\ge1$,
$T_{p^r}=U_p^r$ for $p\mid N$, and $T_n=\prod_{p^r\|n}T_{p^r}$. Then on $M_k(N)$: (i) all the $T_n$ commute; (ii)
$$T_mT_n=\sum_{d\mid(m,n),\ (d,N)=1}d^{k-1}T_{mn/d^2},$$
in particular $T_mT_n=T_{mn}$ for $(m,n)=1$; (iii) for $f\in M_k(N)$ and $m\ge1$,
$$a_m(T_nf)=\sum_{d\mid(m,n),\ (d,N)=1}d^{k-1}a_{mn/d^2}(f),\qquad\text{in particular}\qquad a_1(T_nf)=a_n(f);$$
(iv) $\sum_{r\ge0}T_{p^r}X^r=(1-T_pX+p^{k-1}X^2)^{-1}$ for $p\nmid N$ and $(1-U_pX)^{-1}$ for $p\mid N$. Proof: (i) for primes, by
comparing the coefficient formulas of 2.3 (both $T_pT_{p'}f$ and $T_{p'}T_pf$ have $n$-th coefficient
$a_{pp'n}+p^{k-1}a_{p'n/p}+p'^{k-1}a_{pn/p'}+(pp')^{k-1}a_{n/pp'}$ for $p\ne p'$, with the obvious changes for $U$); (ii) and (iii) by induction on
$r$ from the recursion; (iv) is the recursion. Physics aside: (iv) says $T_{p^r}=p^{r(k-1)/2}U_r\bigl(T_p/(2p^{(k-1)/2})\bigr)$ with $U_r$ the
Chebyshev polynomial of the second kind. Reference: DiamondShurman Proposition 5.3.1 (verify); Shimura71 Theorem 3.24 (verify);
SerreCourse VII.5. Paper: Lemma lem:crit ($a_1(tg)$; $\T$ is the $\Z$-span of the $T_n$, used in "$\phi_g\equiv\phi_f\pmod\lambda$ on all of
$\T$"), Lemma lem:old (multiplicativity, $a_{p^k}=a_p^k$ for $p\mid N$, the recursion), Theorem thm:twist ("both are multiplicative").

**2.5 `ex:hecke:eisenstein-and-delta`** (examples; P). (i) Level one: $T_pE_k=\sigma_{k-1}(p)E_k$ (from $\sigma_{k-1}(pn)+p^{k-1}\sigma_{k-1}(n/p)=\sigma_{k-1}(p)\sigma_{k-1}(n)$
for all $n\ge1$, by multiplicativity of $\sigma_{k-1}$); $\dim S_{12}(1)=1$ forces $T_n\Delta=\tau(n)\Delta$, so $\tau$ is multiplicative and satisfies the
recursion (Mordell). (ii) Level $N$: the weight-two Eisenstein series $E_2^{(N)}$ of Chapter 12 (its 8.4) satisfies $T_pE_2^{(N)}=(1+p)E_2^{(N)}$
for $p\nmid N$, and for $N=11$ also $U_{11}E_2^{(11)}=E_2^{(11)}$ (coefficient computation with $\sigma$). With Chapter 12's congruence
$f_{11}\equiv-\frac1{24}E_2^{(11)}\pmod5$ this says that the eigencharacters of $f_{11}$ and of the Eisenstein series agree modulo $5$: the
maximal ideal $(5)$ of $\T_{11}=\Z$ contains $T_p-1-p$ ($p\ne11$) and $U_{11}-1$, so it is Eisenstein (Chapter 14). Paper: Section sec:eis and Conjecture
conj:eis (the Eisenstein case), background.

**2.6 `rem:hecke:correspondences`** (remark; R, forward pointer). In weight $2$, $f\mapsto f\,dz$ identifies $S_2(N)$ with the holomorphic
differentials on $X_0(N)$ (Chapter 12, its 8.2), and $T_p$ becomes the action on differentials of the Hecke correspondence
$X_0(N)\leftarrow X_0(Np)\rightarrow X_0(N)$, $z\mapsto z$ and $z\mapsto pz$ (Chapter 8, its 12.1(c)); this is how $\T$ acts on $J_0(N)$ and on
$H^1(X_0(N),\Z)$ (Chapter 14), and why the same ring $\T$ acts on forms and on cohomology. Nothing in this chapter depends on the
remark. Reference: DiamondShurman 6.3 (cite the section); Shimura71 7.2 (cite the section). Paper: Section 4.1 (the Hecke
action on $H^1(X_0(M^\Sigma),\Z_\ell)$), Remark rem:free.

### Section 3. The Hecke algebra, eigenforms and eigencharacters

**3.1 `def:hecke:hecke-algebra`** (definition and proposition; P). $\T=\T_N$ and $\T^{(N)}$ as in C4. (i) $\T$ is commutative (2.4(i)).
(ii) $\T$ is the $\Z$-span of $\{T_n:n\ge1\}$ (the span is closed under products by 2.4(ii)), and $\T^{(N)}$ is the $\Z$-span of the $T_n$ with
$(n,N)=1$. (iii) $\T$ preserves $S_2(N;\Z)$ (2.4(iii)); hence $\T\subset\operatorname{End}_\Z S_2(N;\Z)$ is a finitely generated free $\Z$-module (a
subgroup of a free module of rank $d^2$, $d=\dim S_2(N)$), and $\T\otimes A$ acts on $S_2(N;A)$ for every ring $A$. Reference:
DiamondShurman 6.5 (cite the section); Ribet83 Section 2 (verify). Paper: Section 3 preamble (the definition of $\T$), Lemma
lem:crit (the $\Z$-span is used in "$\phi_g\equiv\phi_f$ on all of $\T$"), Lemma lem:ddt417 and Lemma lem:hecke ("$\T$ finite and free";
Chapter 20).

**3.2 `prop:hecke:eigenforms`** (definition and proposition; P). Let $0\ne f\in S_k(N)$ with $T_nf=\lambda_nf$ for all $n\ge1$. (i) $a_n(f)=\lambda_na_1(f)$
(by 2.4(iii)), so $a_1(f)\ne0$; the *normalised* eigenform $f/a_1(f)$ has $T_nf=a_n(f)f$ and $f=\sum\lambda_nq^n$. (ii) A normalised eigenform
satisfies $a_{mn}=a_ma_n$ for $(m,n)=1$, $a_{p^{r+1}}=a_pa_{p^r}-p^{k-1}a_{p^{r-1}}$ for $p\nmid N$, and $a_{p^r}=a_p^r$ for $p\mid N$. (iii) The
*eigencharacter* $\phi_f\colon\T\to\C$, $t\mapsto$ eigenvalue of $t$ on $f$, is a ring homomorphism with $\phi_f(T_n)=a_n(f)$, and $f\mapsto\phi_f$
is injective on normalised eigenforms; distinct normalised eigenforms are linearly independent (distinct characters of a
commutative algebra). (iv) An anemic eigenform need not have $a_1\ne0$: $f_{11}(2z)\in S_2(22)$ is an eigenform of $\T^{(22)}$ with
$a_1=0$. Reference: DiamondShurman 5.8 (cite the section). Paper: Lemma lem:crit ("$\phi_f\colon\T\to\Z$, $T_n\mapsto a_n(f)$"; "normalised
eigenform $g$ ... for all of $\T$"), Lemma lem:old ("normalise it by $a_1(g)=1$"; the relations of (ii)), Theorem thm:twist,
Theorem thm:quant Step 1 ("$\pi\colon\T\to\Z$ the eigencharacter of $g^S$").

**3.3 `prop:hecke:coefficient-field`** (proposition; P given 4.1 and Chapter 6, its 7.1). Let $f$ be a normalised eigenform in $S_2(N)$.
(i) Every $a_n(f)$ is an algebraic integer, $K_f=\Q(a_n(f):n\ge1)$ is a number field and $\phi_f(\T)$ is an order in $\mathcal O_{K_f}$ (Chapter 6,
its 7.1, applied to $\T$, free of finite rank by 3.1(iii)). (ii) For $\sigma\in\operatorname{Aut}(\C)$, $f^\sigma=\sum\sigma(a_n)q^n$ is again a normalised
eigenform in $S_2(N)$ (the $T_n$ have integer matrices in a $\Z$-basis of $S_2(N;\Z)$, Chapter 12, its 11.2), and $f^\sigma$ is a newform if
$f$ is (the new subspace is defined over $\Q$, 6.1(iii)). (iii) If $f$ is a newform, $K_f$ is totally real: $a_n\in\R$ for $(n,N)=1$ by
5.2, and $a_p\in\{0,\pm1\}$ for $p\mid N$ by 6.4. (iv) Warning: a normalised eigenform of the full $\T$ that is not a newform can have
non-real coefficients: the $2$-stabilisations of $f_{11}$ in $S_2(22)$ have $a_2=-1\pm i$ (7.1). For $f=f_E$: $K_f=\Q$, $\mathcal O=\Z$, $\lambda=\ell$
(the paper's "$\lambda=\ell$" in Section 4). Reference: DiamondShurman 6.5 (cite the section); Shimura71 3.5. Paper: Lemma lem:crit
and Lemma lem:old ("coefficients in the ring of integers $\mathcal O$ of a number field", "after enlarging $\mathcal O$ and $\lambda$"), Section
4.1.

**3.4 `thm:hecke:eigen-dictionary`** (theorem; P given 4.1). Let $A$ be a commutative ring. (i) The map $S_2(N;A)\to\operatorname{Hom}_\Z(\T,A)$,
$g\mapsto(t\mapsto a_1(tg))$, is an isomorphism of $\T$-modules, where $\T$ acts on $\operatorname{Hom}(\T,A)$ by $(t\psi)(u)=\psi(tu)$. (ii) Under it the
normalised eigenforms with coefficients in $A$ (elements $g$ with $a_1(g)=1$ and $tg=\phi(t)g$ for some $\phi(t)\in A$, for all $t$)
correspond bijectively to the ring homomorphisms $\phi\colon\T\to A$, via $g=f_\phi:=\sum_n\phi(T_n)q^n$. (iii) Consequences. $A=\C$ (or
$\overline\Q$): the normalised eigenforms of $S_2(N)$ are the $f_\phi$, $\phi\in\operatorname{Hom}(\T,\overline\Q)$, finitely many. $A=\overline\F_\ell$: the mod
$\ell$ eigenforms $\sum\phi(T_n)q^n$ correspond to $\operatorname{Hom}(\T,\overline\F_\ell)$, and their kernels are the maximal ideals of $\T$ of
residue characteristic $\ell$ (each maximal ideal $\mathfrak m$ corresponding to the $[\T/\mathfrak m:\F_\ell]$ Frobenius-conjugate embeddings). $A=\mathcal O$:
$\phi_f\colon\T\to\mathcal O$ and its reduction $\T\to\mathcal O/\lambda$, whose kernel $\mathfrak m_{f,\lambda}$ is "the maximal ideal attached to $(f,\lambda)$". Proof:
(i) is 4.1(iii) tensored with $A$; (ii) $\psi$ is multiplicative with $\psi(1)=1$ iff the corresponding $g$ is a normalised eigenform,
because $a_1(t\,T_ng)=\psi(tT_n)$. Reference: DDT Section 1.6 or 4.1 (cite the section; verify); Ribet83 Section 2 (verify).
Paper: Lemma lem:crit ("$\phi_g\colon\T\to\mathcal O$", "the kernel of $\T\to\mathcal O/\lambda$, a maximal ideal of residue characteristic $\ell$"),
Lemma lem:hecke ("$\mathfrak m$ the maximal ideal of $\T\otimes\Z_\ell$ containing $\ell$ and $\ker\phi_f$"), Theorem thm:quant Step 1.

### Section 4. The integral structure: the perfect pairing

**4.1 `thm:hecke:perfect-pairing`** (theorem; P given Chapter 12, its 11.2 and 11.4). Let $S=S_2(N;\Z)$, $d=\dim S_2(N)$, $B=B_2(N)$ the
Sturm bound of Chapter 12 (its C7), $\T=\T_N$. (i) $\T$ acts faithfully on $S$. (ii) The pairing
$$S\times\T\to\Z,\qquad\langle g,t\rangle=a_1(tg),$$
is $\Z$-bilinear, satisfies $\langle ug,t\rangle=\langle g,ut\rangle$, and is perfect. (iii) Hence $\T$ is free of rank $d$ over $\Z$, $S\simeq\operatorname{Hom}_\Z(\T,\Z)$ and
$\T\simeq\operatorname{Hom}_\Z(S,\Z)$ as $\T$-modules, and for every commutative ring $A$ the induced pairing $S_2(N;A)\times\T_A\to A$ is perfect (in
particular over $\Z_\ell$). (iv) $\T$ is spanned as a $\Z$-module by $T_1,\dots,T_B$; it is in general not spanned by $T_1,\dots,T_d$. Proof:
(i) and injectivity of $\T\to\operatorname{Hom}(S,\Z)$: if $a_1(tg)=0$ for all $g$, then $a_n(tg)=a_1(T_ntg)=a_1(t\,T_ng)=0$, so $tg=0$; injectivity of
$S\to\operatorname{Hom}(\T,\Z)$: $a_n(g)=\langle g,T_n\rangle$. Surjectivity of $\T\to\operatorname{Hom}(S,\Z)$: its image contains the functionals $g\mapsto a_n(g)=\langle g,T_n\rangle$,
and these span $\operatorname{Hom}(S,\Z)$ because the truncation $S\to\Z^B$, $g\mapsto(a_1,\dots,a_B)$, is a split injection (Chapter 12, its 11.4(ii)), so its
dual $\Z^B\to\operatorname{Hom}(S,\Z)$ is onto; this also gives (iv). Then both maps are isomorphisms of free modules of the same rank
(Chapter 3, its 9.6). Verified (Part 6.6): $\operatorname{rank}_\Z\T=d$ and $\det(\langle g_i,t_j\rangle)=\pm1$ in $\Z$-bases at the levels $11,23,33,37,44,77,88,99,121,539$
($d=1,2,3,2,4,7,9,9,6,49$); $T_1,\dots,T_d$ span a sublattice of index $5$ at level $77$, $3$ at $88$, $2$ at $99$, and are linearly dependent at
$121$ and $539$. Reference: Ribet83 Theorem 2.2 and AU96 Lemma 2.1 (as cited by the paper; verify both numbers); ARS12 Section 3;
DDT Section 1 (cite the section). Paper: Lemma lem:crit ("The pairing ... is perfect", "Every step holds verbatim over $\Z_\ell$, the
pairing being perfect after tensoring with $\Z_\ell$"), Theorem thm:quant Step 1 ("with the pairing $S_2(\Gamma_0(N);\Z_\ell)\times\T_\ell\to\Z_\ell$"),
PLAN.md scope.

**4.2 `cor:hecke:pairing-consequences`** (corollary; P given 4.1 and Chapter 3, its 9.6). In the notation of 4.1: (i) a form
$g\in S_2(N;A)$ is determined by the values $a_1(tg)$, $t\in\T$; (ii) for an ideal $\mathfrak a\subset\T$ with $\T/\mathfrak a$ torsion-free, $S[\mathfrak a]\simeq\operatorname{Hom}(\T/\mathfrak a,\Z)$
is saturated in $S$ of rank $\operatorname{rank}\T/\mathfrak a$; (iii) for a ring homomorphism $\phi\colon\T\to\Z$, $S[\ker\phi]=\Z f_\phi$ (3.4(ii)); in particular for a
newform $f$ with rational coefficients, the forms killed by $I=\ker\phi_f$ are $\Z f$; (iv) for ideals $I,J$ with $I\cap J=0$ and torsion-free
quotients, $S/(S[I]\oplus S[J])$ has the order of $\T/(I+J)$ (Chapter 3, its 9.6(iii)). Paper: Lemma lem:crit ("under it the forms killed
by $I$ are $\Z f$ and the forms killed by $J$ are $L$"; "Dualising the inclusion ... shows that $\Z f\oplus L$ has index $r'$"), Section 6
map row ("a form is determined by its pairing with $\T$").

**4.3 `def:hecke:congruence-ideal`** (definition and remark; P for the remark). Let $\mathcal O$ be $\Z$, $\Z_{(\ell)}$, $\Z_\ell$ or $\mathcal O_\lambda$ and
$\phi\colon\T_{\mathcal O}\to\mathcal O$ a surjective ring homomorphism (an eigencharacter with values in $\mathcal O$). Its *Hecke congruence ideal* is
$\eta(\phi)=\phi(\operatorname{Ann}_{\T_{\mathcal O}}(\ker\phi))\subset\mathcal O$ (Chapter 3, its 11.1). For a newform $f\in S_2(N)$ with rational coefficients, the
*congruence number* $r_f$ is the largest integer $r$ such that $f\equiv g\pmod r$ for some $g\in S_2(N;\Z)\cap f^\perp$. Remark: $r_f$ is finite,
because $\Z f\oplus(f^\perp\cap S_2(N;\Z))$ has finite index in $S_2(N;\Z)$ (both summands are saturated, of ranks $1$ and $d-1$, 8.2) and a
congruence modulo $r$ produces the element $(f-g)/r$ of order $r$ in the quotient. The equality $r_f\Z=\eta(\phi_f)$ is the paper's
Lemma lem:crit, proved in Chapter 15 (restated with the commutative-algebra viewpoint in Chapter 20); for the
$X_0(N)$-optimal curve $r_E=r_{f_E}$ and its relation with $\deg\varphi_E$ (Agashe-Ribet-Stein) is Chapter 14's. The paper also uses
$\eta(\pi)$ for the eigencharacter $\pi$ of a depleted form $g^S$, which is not a newform ("$\eta^{\mathrm{Hecke}}(g^S)$", Theorem thm:quant
Step 1); 8.2 says when the definitions apply to such $\pi$. Computed values in 11.2. Paper: Section 1 (the congruence number),
Lemma lem:crit, Lemma lem:hecke, Theorem thm:quant Step 1, Section 6 map row (congruence ideal, $r_E$).

### Section 5. Petersson adjoints

**5.1 `prop:hecke:double-coset-adjoint`** (proposition; P). Let $\Gamma=\Gamma_0(N)$, $\alpha\in\GL_2^+(\Q)$ and $\alpha'=(\det\alpha)\alpha^{-1}$. For $f,g\in S_k(N)$:
$\langle[\Gamma\alpha\Gamma]_kf,g\rangle=\langle f,[\Gamma\alpha'\Gamma]_kg\rangle$. Proof: change of variables $z\mapsto\alpha z$ in the Petersson integral over
$\Gamma\cap\alpha^{-1}\Gamma\alpha$ (Chapter 12, its 10.2(iii)), and the fact that one set of representatives serves for $\Gamma\alpha\Gamma$ on the left and
on the right. Reference: DiamondShurman Proposition 5.5.2 (verify); Shimura71 3.4. Paper: background (5.2, 5.3).

**5.2 `thm:hecke:self-adjoint`** (theorem; P). For $(n,N)=1$ the operator $T_n$ is self-adjoint on $S_k(N)$. Consequently the anemic
algebra $\T^{(N)}\otimes\C$ consists of commuting self-adjoint operators: $S_k(N)$ is the orthogonal direct sum of the eigenspaces of
$\T^{(N)}$ (anemic generalised eigenspaces are eigenspaces), and the eigenvalues of $T_n$, $(n,N)=1$, are real. Proof: for $p\nmid N$,
$\operatorname{diag}(1,p)'=\operatorname{diag}(p,1)$, and $\Gamma\operatorname{diag}(1,p)\Gamma=\Gamma\operatorname{diag}(p,1)\Gamma$ (both double cosets are the set of integer matrices of
determinant $p$ with lower left entry divisible by $N$, an elementary-divisor argument), so 5.1 applies; then 2.4(ii). Spectral theorem for
commuting normal operators (linear algebra). Reference: DiamondShurman Theorem 5.5.3 (verify); SerreCourse VII.5.3 (level one).
Paper: Lemma lem:crit (adjoints), Theorem thm:twist and Theorem thm:quant Step 1 (generalised eigenspaces of the $T_p$, $p\nmid N$),
Chapter 12, its 10.5(a).

**5.3 `prop:hecke:Up-adjoint`** (proposition; P for (i), (ii); S for (iii)). Let $p\mid N$ and $w_N=|_kW_N$ (Chapter 12, its 12.1). (i)
$U_p^\dagger=w_NU_pw_N$ on $S_k(N)$. Proof: $W_N\operatorname{diag}(1,p)W_N^{-1}=\operatorname{diag}(p,1)$ and $W_N$ normalises $\Gamma$, so
$[\Gamma\operatorname{diag}(p,1)\Gamma]_k=w_N[\Gamma\operatorname{diag}(1,p)\Gamma]_kw_N^{-1}$; apply 5.1; $w_N^{-1}=w_N$ (Chapter 12's slash convention C3 makes $w_N$ an exact involution).
(ii) $U_p$ is in general neither self-adjoint nor normal: on $\operatorname{span}\{f_{11}(z),f_{11}(2z)\}\subset S_2(22)$ the Gram matrix of the
Petersson product is proportional to $\begin{psmallmatrix}1&-1/3\\-1/3&1/4\end{psmallmatrix}$, $U_2$ has matrix $\begin{psmallmatrix}-2&1\\-2&0\end{psmallmatrix}$ (columns: images of
$f_{11}(z)$, $f_{11}(2z)$), its adjoint has matrix $\begin{psmallmatrix}0&-1/2\\4&-2\end{psmallmatrix}$, and $w_{22}$ has matrix $\begin{psmallmatrix}0&-1/2\\-2&0\end{psmallmatrix}$
(Chapter 12, its 12.4(b)), with $w_{22}U_2w_{22}$ equal to the adjoint (all verified with PARI's `mfpetersson` and `mfatkininit`). (iii)
Gram entries in weight $2$: for a newform $h$ of level $M$ and $p\nmid M$, with all products at level $Mp$:
$\langle h(z),h(pz)\rangle=\frac{a_p(h)}{p(p+1)}\langle h,h\rangle$ and $\langle h(pz),h(pz)\rangle=p^{-2}\langle h,h\rangle$ (check: $-2/(2\cdot3)=-1/3$ and $1/4$ for $f_{11}$, $p=2$; the
second is a change of variables, the first from the trace $\operatorname{Tr}^{Mp}_M(h(pz))=p^{-1}T_p^{(M)}h=\frac{a_p}ph$ and
$\langle h,g\rangle_{\Gamma_0(Mp)}=\langle h,\operatorname{Tr}^{Mp}_Mg\rangle_{\Gamma_0(M)}$ for $h$ of level $M$, with $\langle h,h\rangle_{\Gamma_0(Mp)}=(p+1)\langle h,h\rangle_{\Gamma_0(M)}$ (Chapter 12, its 10.2(i)); the general-weight form, verify in DiamondShurman 5.7). Reference: DiamondShurman 5.5 (cite the section; the identity $T_p^\dagger=w_NT_pw_N^{-1}$ for all $p$ is there, verify);
AtkinLehner70. Paper: Lemma lem:crit ("because $f$ is an eigenvector of the adjoints of the $T_n$ as well"), Section 4.1 (the
cohomological analogue $w_{M^\Sigma}T_nw_{M^\Sigma}^{-1}$, Chapter 14), Theorem thm:quant Step 1 (why the complement of $g^S$ must be
the $\T$-stable one, 8.2).

**5.4 `cor:hecke:perp-stable`** (corollary; P). Let $V\subset S_k(N)$ be a subspace stable under $\T$ and under $w_N$. Then $V^\perp$ is stable
under $\T$ (and $w_N$). In particular, if $f$ is an eigenform of all of $\T$ and an eigenvector of $w_N$ (every newform is, 6.4), then
$f^\perp$ is $\T$-stable. Proof: $\langle tg,v\rangle=\langle g,t^\dagger v\rangle$ with $t^\dagger=t$ or $w_Ntw_N$ (5.2, 5.3), and $t^\dagger V\subset V$. Paper: Lemma lem:crit (the
$\T$-stability of $f^\perp$), Lemma lem:old, Theorem thm:twist ($f^\perp$ at level $N$), Chapter 12, its 10.3.

### Section 6. Oldforms and newforms: Atkin-Lehner theory

**6.1 `def:hecke:old-new`** (definition and proposition; P for (i), (ii); P given 6.2 for (iii)). For $M\mid N$ and $d\mid N/M$ let
$V_d\colon S_k(M)\to S_k(N)$, $h\mapsto h(dz)=d^{-k/2}h|_k\operatorname{diag}(d,1)$ (Chapter 12, its 6.2(e)). The *old subspace* is
$S_k^{\mathrm{old}}(N)=\sum_{p\mid N}\bigl(S_k(N/p)+V_pS_k(N/p)\bigr)$ (equivalently the span of all $V_dS_k(M)$, $M\mid N$, $M\ne N$, $d\mid N/M$) and the *new
subspace* is its Petersson orthogonal complement $S_k^{\mathrm{new}}(N)$. (i) $T_n$ with $(n,N)=1$ commutes with every $V_d$ (2.3), so both
subspaces are $\T^{(N)}$-stable (with 5.2). (ii) Both are stable under every $U_p$, $p\mid N$: the old one by the formulas of 7.1 applied to
$V_dh$, the new one by 5.4, since $w_N$ maps $V_dS_k(M)$ into $V_{N/(Md)}S_k(M)$ (Chapter 12, its 12.4(b), generalised by the same matrix
identity) and so preserves the old subspace. (iii) Both are defined over $\Q$: the new subspace is the sum of the anemic eigenspaces of
the newforms of level $N$ (6.2(iii)), and $\operatorname{Aut}(\C)$ permutes newforms (3.3(ii)). Reference: AtkinLehner70 (Section 2, cite the
section); DiamondShurman 5.6, 5.7 (cite the sections). Paper: Section 1 ("the newform"), Lemma lem:old ("the forms $h(dz)$, $d\mid N/M$"),
Section 4.1.

**6.2 `thm:hecke:atkin-lehner`** (theorem, Atkin-Lehner, Li; R, with a sketch S). (i) $S_k^{\mathrm{new}}(N)$ has a basis of *newforms*:
normalised eigenforms of all of $\T_N$ (all $T_n$, the $U_p$ included); distinct newforms are orthogonal. (ii) (Multiplicity one.) If $f$ is
a newform of level $N$ and $L$ is a multiple of $N$, the eigenspace in $S_k(L)$ of the system of eigenvalues of $f$ for $\T^{(L)}$ is
$\operatorname{span}\{f(dz):d\mid L/N\}$, of dimension $\sigma_0(L/N)$; in $S_k^{\mathrm{new}}(N)$ it is $\C f$. (iii) (Decomposition.)
$$S_k(N)=\bigoplus_{M\mid N}\ \bigoplus_{d\mid N/M}V_d\,S_k^{\mathrm{new}}(M),$$
the forms $h(dz)$, $h$ a newform of level $M\mid N$, $d\mid N/M$, form a basis of $S_k(N)$, and the old subspace is the sum of the terms with
$M\ne N$. (iv) In particular a newform $f$ of level $N$ is orthogonal to every $h(dz)$ with $h\ne f$ a newform of level $M\mid N$, so
$f^\perp=\bigoplus_{h\ne f}\operatorname{span}\{h(dz)\}$ (with 5.2: different systems are orthogonal). Sketch (DiamondShurman's route): the Main Lemma (a
form whose coefficients $a_n$ vanish for all $n$ prime to $N$ lies in $\sum_{p\mid N}V_pS_k(N/p)$) gives (ii) for the new subspace, since the
difference of two new anemic eigenforms with the same system, suitably normalised, has $a_n=0$ for $(n,N)=1$; (iii) by induction on $N$.
Reference: AtkinLehner70 (the main theorems; cite by section, the numbering to be verified); Li, *Newforms and functional
equations*, Math. Ann. 212 (1975) (proposed key `Li75`, Part 6.5); DiamondShurman Theorem 5.8.3 and the Main Lemma 5.7.1 (verify the
numbers); Miyake 4.6. Paper: Section 1 ("$f=f_E\in S_2(\Gamma_0(N))$ the newform"), Lemma lem:old ("span a $\T$-stable subspace $V$ of
$S_2(\Gamma_0(N))$ orthogonal to the newform $f$ (whether $M<N$, or $M=N$ and $h\ne f$)"), Lemma lem:crit ($\T\otimes\Q=\Q\times\T'$ needs (ii)), Theorem
thm:quant Step 1 ("the forms with the $T_p$-eigenvalues of $g$, $p\nmid N$, ... the span of the $g(dz)$, $d\mid N/N_S$").

**6.3 `thm:hecke:strong-multiplicity-one`** (theorem; R for (i), S for (ii)). (i) If $f$ and $g$ are newforms of weight $k$ and levels $M$,
$M'$, and $a_p(f)=a_p(g)$ for all but finitely many primes $p$, then $f=g$ (and $M=M'$). Equivalently: the systems of $T_p$-eigenvalues of
two distinct newforms differ at infinitely many primes. (ii) (Weight $2$, density one.) The same conclusion holds if $a_p(f)=a_p(g)$
for all $p$ in a set of primes of Dirichlet density one: the $\lambda$-adic Galois representations of $f$ and $g$ (Chapter 15) then have
equal traces on a dense set of Frobenius elements (Chebotarev, Chapter 5), hence equal traces everywhere, hence isomorphic
semisimplifications (Brauer-Nesbitt, Chapter 4), hence $a_p(f)=a_p(g)$ for all $p\nmid MM'\ell$, and (i) applies. (iii) Consequence (P): for
a newform $f$ of level $N$, a generalised eigenform $h\in S_k(L)$, $N\mid L$, of $\T^{(L)}$ whose system differs from that of $f$ at infinitely
many $p$ lies in the sum of the anemic eigenspaces of the newforms $h'\ne f$, and is orthogonal to $f$ and to every $f(dz)$. Reference: Miyake
Theorem 4.6.19 (verify); DiamondShurman 5.8 (cite the section); AtkinLehner70. Paper: Theorem thm:twist ("a system of $T_p$-eigenvalues
... differing from that of $g$ at infinitely many $p$ ... so $\iota(h)\in f^\perp$"), Theorem thm:quant Step 1 ("strong multiplicity one"),
Lemma lem:old and Theorem thm:qual ($h\ne f$; important_notes.md point 20), PLAN.md scope ("a newform is determined by $a_p$ for $p$
in any set of density one").

**6.4 `prop:hecke:newform-local`** (proposition; P for (i), (ii); R for (iii)). Let $f$ be a newform of weight $k$, level $N$, trivial
character. (i) For every $d\,\|\,N$, $f|_kW_d=\varepsilon_d(f)f$ with $\varepsilon_d(f)=\pm1$ (the involution $w_d$ commutes with $\T^{(N)}$ and preserves the new
subspace, so it preserves $\C f$ by 6.2(ii)). (ii) Hence 5.4 applies: $f^\perp$ is $\T$-stable. (iii) (AtkinLehner70, Theorem 3, as cited
by the paper; verify which parts) If $p^2\mid N$ then $a_p(f)=0$; if $p\,\|\,N$ then $a_p(f)=-p^{k/2-1}\varepsilon_p(f)$, so in weight $2$
$a_p(f)=-\varepsilon_p(f)\in\{\pm1\}$. (iv) For $f=f_E$ (Chapter 14): $a_p=1$, $-1$, $0$ for split multiplicative, nonsplit multiplicative,
additive reduction at $p$. Checks: $f_{11}$: $\varepsilon_{11}=-1$, $a_{11}=1$ (Chapter 12, its 9.2(iii)); $a_{11}=0$ for 121a to 121d; $a_7=0$ for 539c,
539d; $a_7(77c)=\pm1$. Reference: AtkinLehner70 Theorem 3 (as cited); DiamondShurman 5.8 and 6.6 (cite the sections). Paper: Lemma
lem:old (case $p^2\mid N$: "a newform on $\Gamma_0(M)$ with $p^2\mid M$ has $a_p=0$"; case $p\,\|\,N$: $a_p(h)=\pm1$), Lemma lem:crit (the $w_N$-eigenvector
property behind the $\T$-stability of $f^\perp$), Lemma lem:euler and Theorem thm:quant Step 1 ($a_q(g)=\pm1$ at a multiplicative $q$),
Chapter 12, its 12.4(c).

**6.5 `cor:hecke:dimensions`** (corollary; P given 6.2). $\dim S_k(N)=\sum_{M\mid N}\sigma_0(N/M)\dim S_k^{\mathrm{new}}(M)$, and by Moebius inversion
$\dim S_k^{\mathrm{new}}(N)=\sum_{M\mid N}\beta(N/M)\dim S_k(M)$ with $\beta=\mu*\mu$ multiplicative, $\beta(p)=-2$, $\beta(p^2)=1$, $\beta(p^r)=0$ for $r\ge3$.
Table (weight $2$; verified with PARI's `mfdim` for the full and the new space and with the formula):

| $N$ | 11 | 22 | 33 | 44 | 77 | 88 | 99 | 121 | 242 | 539 | 980 | 1089 |
|-|-|-|-|-|-|-|-|-|-|-|-|-|
| $\dim S_2(N)$ | 1 | 2 | 3 | 4 | 7 | 9 | 9 | 6 | 22 | 49 | 145 | 109 |
| $\dim S_2^{\mathrm{new}}(N)$ | 1 | 0 | 1 | 1 | 5 | 3 | 4 | 4 | 10 | 34 | 13 | 41 |

For example $S_2(121)$ is spanned by the four rational newforms 121a, 121b, 121c, 121d and the two oldforms $f_{11}(z)$, $f_{11}(11z)$ (Chapter
12, its 9.3), and $S_2(88)$ by three newforms of level $88$, $f_{44}(z)$, $f_{44}(2z)$ and the four $f_{11}(2^jz)$, $0\le j\le3$. Reference: as 6.2.
Paper: background (the levels of Section 3 and Section 4.1).

### Section 7. $U_p$ on oldforms: stabilisation, depletion, non-semisimplicity

**7.1 `prop:hecke:Up-oldspan`** (proposition; P). Let $h$ be a newform of weight $k$ and level $M$, $p$ a prime, $e\ge0$, and
$V_{h,p,e}=\operatorname{span}\{h(p^jz):0\le j\le e\}$, of dimension $e+1$ (6.2(iii)), inside $S_k(Mp^e)$; let $U_p$ be the operator of level $Mp^e$ (assume
$e\ge1$ or $p\mid M$). (i) $U_ph(p^jz)=h(p^{j-1}z)$ for $j\ge1$; $U_ph=a_p(h)h-p^{k-1}h(pz)$ if $p\nmid M$; $U_ph=a_p(h)h$ if $p\mid M$. (ii) $h(p^ez)$ is a
cyclic vector, so the characteristic and minimal polynomials of $U_p$ on $V_{h,p,e}$ coincide:
$$X^{e-1}(X^2-a_p(h)X+p^{k-1})\quad(p\nmid M,\ e\ge1),\qquad X^{e}(X-a_p(h))\quad(p\mid M).$$
(iii) Every eigenvalue has a one-dimensional eigenspace, spanned by: for $p\nmid M$, writing $X^2-a_pX+p^{k-1}=(X-\alpha_p)(X-\beta_p)$: the
*$p$-stabilisations* $h_{\alpha}=h-\beta_ph(pz)$ (eigenvalue $\alpha_p$) and $h_\beta=h-\alpha_ph(pz)$ (eigenvalue $\beta_p$), and, if $e\ge2$, the *$p$-depleted form*
$h^{(p)}=h-a_ph(pz)+p^{k-1}h(p^2z)$ (eigenvalue $0$); for $p\,\|\,M$: $h$ (eigenvalue $a_p=\pm p^{k/2-1}$) and, if $e\ge1$, $h^{(p)}=h-a_ph(pz)$
(eigenvalue $0$); for $p^2\mid M$: $h=h^{(p)}$ (eigenvalue $a_p=0$). (iv) $U_p$ is semisimple on $V_{h,p,e}$ iff its characteristic polynomial is
squarefree: iff $e\le2$ and $\alpha_p\ne\beta_p$ ($p\nmid M$), $e\le1$ ($p\,\|\,M$), $e=0$ ($p^2\mid M$); otherwise the eigenvalue $0$ has a single Jordan
block of size $e-1$, $e$ or $e+1$. (v) Each eigenvector of (iii) is a normalised eigenform of the full Hecke algebra of level $Mp^e$, with
the eigenvalues of $h$ at the other operators. Verified matrices (columns: images of $f_{11}(p^jz)$): level $22$:
$\begin{psmallmatrix}-2&1\\-2&0\end{psmallmatrix}$, $X^2+2X+2$; level $44$: $X(X^2+2X+2)$; level $88$: $X^2(X^2+2X+2)$ with a Jordan block of size $2$ at $0$; level $121$
($p=11\,\|\,M$): $\begin{psmallmatrix}1&1\\0&0\end{psmallmatrix}$, $X(X-1)$; level $1331$: $X^2(X-1)$. Reference: Chapter 3, its 10.7(v) (the linear algebra); AtkinLehner70;
DiamondShurman 5.6 and 5.7 exercises (cite the sections). Paper: Lemma lem:old (every formula of its proof: "$U_ph(p^jz)=h(p^{j-1}z)$",
"The eigenvalues of $U_p$ there are therefore the roots $\alpha_p,\beta_p$ ... together with $0$ if $e_p\ge2$", "the $p$-stabilisations",
"the depleted forms", "$U_p$ is not semisimple on this span when $0$ is a repeated eigenvalue"), Theorem thm:quant Step 1 ("on that
span the operators $U_q$ ... have the eigenvalue $0$ with multiplicity one"; "the others have $U_q$-eigenvalue $a_q(g)=\pm1$ ... or a root
$\alpha,\beta$"), Section 4.1 (stabilisations, Chapter 9, its 8.3).

**7.2 `cor:hecke:Up-eigenvalues`** (corollary; P given 6.2(iii), 6.4(iii), 7.1). Weight $2$. Every eigenvalue of $U_p$ on $S_2(N)$, $p\mid N$, is
$0$, or $\pm1$, or a root of $X^2-a_p(h)X+p$ for a newform $h$ of level $M\mid N$ with $p\nmid M$. In particular, for every prime $\lambda$ of $\overline\Q$
not above $p$, every nonzero eigenvalue of $U_p$ is a $\lambda$-adic unit (the roots are algebraic integers with product $p$), so a
generalised eigenform of $\T$ whose $U_p$-eigenvalue is $\equiv0\pmod\lambda$ has $U_p$-eigenvalue $0$. Verified characteristic
polynomials of $U_p$ (PARI `mfheckemat`): level $88$, $U_2$: $X^7(X^2+2X+2)$; level $99$, $U_3$: $X^6(X+1)(X^2+X+3)$; level $121$, $U_{11}$: $X^5(X-1)$;
level $539$, $U_7$: $X^{42}(X-1)^3(X+1)^2(X^2+2X+7)$; level $980$, $U_7$: $X^{126}(X-1)^8(X+1)^9(X^2-2X+7)$; level $1089$, $U_3$:
$X^{76}(X-1)^{10}(X+1)^{11}(X^2-2X+3)^2(X^2+X+3)^4$. Paper: Theorem thm:quant Step 1 ("The generalised eigenforms of $\T$ whose eigencharacter
is congruent to $\pi$ modulo $\mathfrak m$ have $U_q\equiv0$ at $q\in S$" and then "systems of eigenvalues with $U_q=0$": the passage from
$\equiv0$ to $=0$ is this corollary; "which are $\ell$-adic units since $\ell\ne q$").

**7.3 `rem:hecke:non-semisimple`** (remark and example; P, with (iii) R). (i) At level $88$ the minimal polynomial of $U_2$ on $S_2(88)$ is
$X^2(X^2+2X+2)$: $U_2$ is not semisimple, and $\T_{88}\otimes\Q$ contains a nonzero nilpotent element (Chapter 3, its 10.7(iii)); so the full Hecke
algebra need not be reduced (important_notes.md point 19). The source is $V_{f_{11},2,3}$ ($e=3$) and also $V_{f_{44},2,1}$ ($2^2\mid44$, $U_2$
nilpotent of order $2$ there). (ii) A large multiplicity of the eigenvalue $0$ does not by itself make $U_p$ non-semisimple: at level $539$
the eigenvalue $0$ of $U_7$ has multiplicity $42$ but the minimal polynomial $X(X-1)(X+1)(X^2+2X+7)$ is squarefree (no single $V_{h,7,e}$ has a
repeated root). (iii) (Coleman-Edixhoven.) For a newform of weight $2$ and level prime to $p$, $\alpha_p\ne\beta_p$; so $U_p$ is semisimple on the
$p$-old part of level $Mp$ (for rational $a_p$ this is elementary: $a_p^2\ne4p$). Reference: ColemanEdixhoven (in `refs.bib`; the
theorem number to be verified). Paper: Lemma lem:old ("$U_p$ is not semisimple on this span when $0$ is a repeated eigenvalue, but each
listed eigenvalue has an eigenvector"), Lemma lem:ddt417 ($\wp\cap I=0$ is not automatic, point 19).

**7.4 `def:hecke:depletion`** (definition and proposition; P). Let $f$ be a newform of weight $k$ and level $M$ and $\Sigma$ a finite set of primes.
(i) Put $\delta_p(f)=2$ if $p\nmid M$, $1$ if $p\,\|\,M$, $0$ if $p^2\mid M$; equivalently $\delta_p$ is the degree in $p^{-s}$ of the inverse Euler factor
$L_p(f,s)^{-1}$ (10.1), the number of roots of the Hecke polynomial at $p$; for $f=f_E$, $\delta_p=2,1,0$ for good, multiplicative, additive
reduction, which is $\dim V^{I_p}$ for $V=V_\ell E$ (Chapter 11; the paper's definition in Section 1.1). (ii) The *$\Sigma$-depleted form*
$f^\Sigma=\sum_{(n,\Sigma)=1}a_n(f)q^n$ (C8) equals $\bigl(\prod_{p\in\Sigma}D_p\bigr)f$ with $D_p=1-a_pV_p+p^{k-1}V_p^2$ ($p\nmid M$), $1-a_pV_p$ ($p\,\|\,M$), $1$
($p^2\mid M$), by multiplicativity and the recursion of 3.2(ii). (iii) $f^\Sigma\in S_k(M^\Sigma)$ with $M^\Sigma=M\prod_{p\in\Sigma}p^{\delta_p}$, and $M^\Sigma$ is the
least level containing $f^\Sigma$ (by 7.1(iii): the eigenvalue $0$ of $U_p$ occurs in $V_{f,p,e}$ only for $e\ge\delta_p$). (iv) $f^\Sigma$ is a normalised
eigenform of the full Hecke algebra of level $M^\Sigma$, with $U_pf^\Sigma=0$ for $p\in\Sigma$ and the eigenvalues of $f$ elsewhere, and its
generalised eigenspace in $S_k(M^\Sigma)$ is the line $\C f^\Sigma$: on $V_{f,p,\delta_p}$ the characteristic polynomial is $X(X^2-a_pX+p^{k-1})$ or $X(X-a_p)$
with $a_p\ne0$, so $0$ is a simple root (6.2(iii) and 7.1). (v) At a level $N$ with $M^\Sigma\mid N$, $N\ne M^\Sigma$, the form $f^\Sigma$ is still a
normalised eigenform of $\T_N$, but its generalised eigenspace can be larger (the depleted $f_{11}^{(2)}$ spans its generalised eigenspace at
level $44$ and lies in a Jordan block of $U_2$ at level $88$). (vi) $L(f^\Sigma,s)=L(f,s)\prod_{p\in\Sigma}L_p(f,s)^{-1}$ (10.1): depletion removes the
Euler factors at $\Sigma$, and $M^\Sigma$ raises the level by one factor $p$ per removed root. Examples (verified): $f_{11}^{\{2\}}=f_{11}+2f_{11}(2z)+2f_{11}(4z)$,
of level $44$, has $a_n=0$ for even $n$ and $a_n=a_n(f_{11})$ for odd $n$ (checked to $n=4000$); $f_{11}^{\{11\}}=f_{11}-f_{11}(11z)$, level $121$; for 121a,
$\Sigma=\{11\}$: $f^\Sigma=f$, level $121$; for $g=$ 77c and $\Sigma=\{7\}$: $g^\Sigma=g-a_7(g)g(7z)$, level $539$; for $g=f_{11}$, $\Sigma=\{7\}$:
$g^\Sigma=g+2g(7z)+7g(49z)$, level $539$ ($a_7(f_{11})=-2$). Reference: DFG04 Sections 1.5.3, 1.7.3 (as cited by the paper, for the notation
$M^\Sigma$, $f^\Sigma$; verify); DDT Section 4 (cite the section). Paper: Section 4.1 ("$M^\Sigma=M\prod_{p\in\Sigma}p^{\delta_p}$", "the $\Sigma$-depleted
eigenform, of level $M^\Sigma$"), Section 1.1 ($\delta_p$), Theorem thm:dfg14 and the paragraph after it ("adding an additive prime to $\Sigma$ changes
neither the level nor the ideal"), Theorem thm:quant ("$N_S^\Sigma=N$: the $S$-depleted form $g^S$ lives at level $N$"), Lemma lem:old (the depleted
forms).

### Section 8. The structure of $\T$, generalised eigenspaces and congruences

**8.1 `thm:hecke:structure`** (theorem; P given 6.2, 6.3, 7.1). Weight $k$, level $N$. (i) $S_k(N)\otimes\overline\Q=\bigoplus_hV_h$, the sum over the newforms
$h$ of levels $M_h\mid N$, with $V_h=\operatorname{span}\{h(dz):d\mid N/M_h\}$; $V_h$ is the eigenspace of $\T^{(N)}$ for the system of $h$, and as a module over
$\overline\Q[U_p:p\mid N]$ it is $\bigotimes_{p\mid N}V_{h,p,e_p}$ with $e_p=v_p(N/M_h)$. (ii) $\T\otimes\overline\Q\simeq\prod_hA_h$, where $A_h$ is the image of $\T\otimes\overline\Q$ in
$\operatorname{End}(V_h)$, and $A_h\simeq\bigotimes_{p\mid N}\overline\Q[X]/(m_{h,p}(X))$ with $m_{h,p}$ the characteristic polynomial of 7.1(ii) (equal to $X-a_p(h)$ when
$e_p=0$); so $\operatorname{rank}\T=\sum_h\prod_p(e_p+1)=\dim S_k(N)$, consistent with 4.1, and $S_k(N)\otimes\overline\Q$ is free of rank one over $\T\otimes\overline\Q$ (each $V_h$
is cyclic). (iii) The generalised eigenspaces of $\T\otimes\overline\Q$ are the joint generalised eigenspaces $V_h(\mu)$, $\mu=(\mu_p)$ a choice of a root of
each $m_{h,p}$, of dimension the product of the multiplicities; $\T\otimes\Q$ is reduced iff every $m_{h,p}$ is squarefree (7.1(iv)). (iv) For a
newform $f$ of level $N$ with rational coefficients: $V_f=\C f$, and $\T\otimes\Q=\Q\times\T'$ with $\T'$ acting faithfully on $f^\perp=\bigoplus_{h\ne f}V_h$
(this is the paper's "$\T\otimes\Q=\Q\times\T'$"). In general this is "$\T\otimes\Q$ is a product of fields (the new part, $K_h$ for each Galois
orbit of newforms of level $N$) times the old part", the old part possibly non-reduced. Proof: (i) is 6.2(iii) with 6.3; the
factors of (ii) are separated by idempotents of $\T^{(N)}\otimes\overline\Q$ (distinct anemic systems, 5.2), and on $V_h$ the algebra generated by the
$U_p$ is the tensor product of the algebras of 7.1, each acting with a cyclic vector (Chapter 3, its 10.5, 10.8). Verified at level $88$: $9=3\cdot1+2+4$ ($U_2$
on $V_{f_{44}}$ is $X^2$, on $V_{f_{11}}$ is $X^2(X^2+2X+2)$). Reference: DDT Section 1 or 4 (cite the section); Chapter 3, its 10.1, 10.5. Paper:
Lemma lem:crit ("Writing $\T\otimes\Q=\Q\times\T'$ with $\T'$ acting faithfully on $f^\perp$"), Lemma lem:old ("$V$ is the tensor product of these
local spaces and $\T$ is commutative"), Theorem thm:twist ("generalised eigenform", "$g^\perp$ ... the sum of the generalised eigenspaces of
the other systems"), Theorem thm:quant Step 1 ("the generalised eigenspace of $\pi$ ... is the line of $g^S$"), PLAN.md scope.

**8.2 `prop:hecke:complements`** (proposition; P given 8.1, 5.4). Let $g$ be a normalised eigenform of $\T_N$ with eigencharacter $\pi$ whose
generalised eigenspace is a line $\C g$ (a newform of level $N$, or $f^\Sigma$ at level $M^\Sigma$ by 7.4(iv), or $g^S$ in Theorem thm:quant). Let $g^c$
be the $\T$-stable complement of $\C g$ (C5). (i) $S_k(N)=\C g\oplus g^c$, $\T\otimes\overline\Q=\overline\Q\times\T''$ with $\T''$ faithful on $g^c$, and if $\pi$ has values in $\Q$
then $g^c$ is defined over $\Q$ and $g^c\cap S_2(N;\Z)$ is saturated of rank $d-1$; so the arguments of the paper's Lemma lem:crit apply to $\pi$
and $\eta(\pi)$ (4.3) is the largest modulus of a congruence $g\equiv h$, $h\in g^c\cap S_2(N;\Z)$ (proved in Chapter 15 for newforms; the proof
uses only (i)). (ii) If $g$ is a newform, $g^c=g^\perp$ (6.2(iv)). (iii) If $g$ is not a newform, $g^c\ne g^\perp$ in general: for $g=f_{11}^{\{2\}}$ at
level $44$, $g^c\ni f_{11}-\beta f_{11}(2z)$ (a stabilisation), which is not orthogonal to $g$ (Gram entries of 5.3(iii)). Paper: Theorem thm:twist
("$g^\perp$, the $\T$-stable complement of the $g$-line"; at level $N_S$ the newform $g$ makes the two notions agree), Theorem thm:quant Step 1
("in the $\T$-stable complement of the $g^S$-line"; there it is not a Petersson complement).

**8.3 `prop:hecke:local-components`** (proposition; P given Chapter 3, its 10.3, 10.5, 10.6 and 4.1). Let $\ell$ be a prime and
$\T_\ell=\T\otimes\Z_\ell=\prod_{\mathfrak m}\T_{\mathfrak m}$ over the maximal ideals $\mathfrak m\ni\ell$ of $\T$, with idempotents $e_{\mathfrak m}$. (i) $S_2(N;\Z_\ell)=\bigoplus_{\mathfrak m}e_{\mathfrak m}S_2(N;\Z_\ell)$,
and $e_{\mathfrak m}S_2(N;\Z_\ell)\otimes\overline\Q_\ell$ is the sum of the generalised eigenspaces of the $\varphi\colon\T\to\overline\Q_\ell$ with $\varphi^{-1}(\mathfrak m_{\overline\Z_\ell})=\mathfrak m$, that is,
with $\varphi\equiv$ the residual character of $\mathfrak m$. (ii) A ring homomorphism $\phi\colon\T\to\mathcal O_\lambda$ factors through exactly one $\T_{\mathfrak m}$, $\mathfrak m=\mathfrak m_{\phi,\lambda}$,
and $\phi$ kills the other factors: they lie in $\ker\phi$, not in $\operatorname{Ann}(\ker\phi)$, and $\eta(\phi)=\eta(\phi|_{\T_{\mathfrak m}})$ (important_notes.md
point 35; Chapter 3, its 11.1(v)). (iii) The pairing of 4.1 satisfies $\langle e_{\mathfrak m}g,t\rangle=\langle g,e_{\mathfrak m}t\rangle$, so it restricts to perfect pairings
$e_{\mathfrak m}S_2(N;\Z_\ell)\times\T_{\mathfrak m}\to\Z_\ell$ and $e_{\mathfrak m}S_2(N;\Z_\ell)\simeq\operatorname{Hom}(\T_{\mathfrak m},\Z_\ell)$ (the modular-forms analogue of point 36, which concerns the
cohomological pairing of Chapter 14). (iv) $e_{\mathfrak m}$ preserves integrality and every $\T$-stable subspace, and fixes the $\mathfrak m$-part; so a
congruence $g\equiv h\pmod{\ell^t}$ with $g$ in the $\mathfrak m$-part and $h\in S_2(N;\Z_\ell)\cap W$, $W$ a $\T$-stable subspace, gives $g\equiv e_{\mathfrak m}h\pmod{\ell^t}$ with
$e_{\mathfrak m}h\in W$ in the $\mathfrak m$-part (Chapter 3, its 10.6). Paper: Lemma lem:hecke ("the congruence ideal is computed in $\T_{\mathfrak m}$, since the other local
factors ... lie in the annihilator": the correction of point 35), Theorem thm:quant Step 1 ("$\mathfrak m$ the maximal ideal of $\T_\ell$ containing
$\ker\pi$ and $\ell$", "projecting $h$ to the $\mathfrak m$-component (an idempotent of $\T_\ell$, so the projection stays in the complement and the
congruence survives)"), Remark rem:free, PLAN.md scope.

**8.4 `prop:hecke:congruences`** (proposition; P). Let $\mathcal O$ be the ring of integers of a number field and $\lambda$ a prime of $\mathcal O$. (i) For
normalised eigenforms $f,g$ of $\T_N$ with coefficients in $\mathcal O$ the following are equivalent: $a_n(f)\equiv a_n(g)\pmod\lambda$ for all $n\ge1$; the
same for all primes $n=p$ (including $p\mid N$); $\phi_f\equiv\phi_g\pmod\lambda$ on all of $\T$; $\mathfrak m_{f,\lambda}=\mathfrak m_{g,\lambda}$. (From primes to all $n$: 3.2(ii),
since both satisfy the same multiplicativity, the same recursion with the same $p^{k-1}$ for $p\nmid N$, and $a_{p^r}=a_p^r$ for $p\mid N$; from $n$ to
$\T$: 3.1(ii).) (ii) If $f$, $g$ are normalised eigenforms of levels $M_f$, $M_g$, $\Sigma$ contains every prime dividing $M_fM_g$, and
$a_p(f)\equiv a_p(g)\pmod\lambda$ for all $p\notin\Sigma$, then $f^\Sigma\equiv g^\Sigma\pmod\lambda$ coefficientwise, both forms lying in $S_k(L)$,
$L=\operatorname{lcm}(M_f^\Sigma,M_g^\Sigma)$. (iii) Without depletion the conclusion can fail at the primes of $\Sigma$, and the remedy in the paper is
the choice of $U_p$-eigenvalues in Lemma lem:old (Chapter 15); a finite check of a congruence between two forms of the same space is
Sturm's bound (Chapter 12, its 11.3), which is a different tool from the recursion (important_notes.md point 46). Paper: Section 1
("$f\equiv g\pmod r$ coefficientwise"), Lemma lem:crit ("$a_n(g)\equiv a_n(f)\pmod\lambda$ for every $n\ge1$", "$\phi_g\equiv\phi_f\pmod\lambda$ on all of $\T$"), Lemma
lem:old (its reduction "the congruence for all $n$ then follows from ..."), the Example of Section 3, PLAN.md scope ("so that congruences
at primes propagate to all $n$").

