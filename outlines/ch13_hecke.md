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

