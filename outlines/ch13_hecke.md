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
(`c1.py` to `c11.py`), using PARI/GP 2.17 through `cypari2` and Cremona's `ecdata` files for conductors below 10,000
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

**6.4 `prop:hecke:newform-local`** (proposition; P for (i) given AtkinLehner70's stability of the old subspace under $w_d$, P for (ii); R for (iii)). Let $f$ be a newform of weight $k$, level $N$, trivial
character. (i) For every $d\,\|\,N$, $f|_kW_d=\varepsilon_d(f)f$ with $\varepsilon_d(f)=\pm1$ (the involution $w_d$ commutes with $\T^{(N)}$ and preserves the new
subspace, being a self-adjoint isometry that maps the old subspace into itself (AtkinLehner70), so it preserves $\C f$ by 6.2(ii)). (ii) Hence 5.4 applies: $f^\perp$ is $\T$-stable. (iii) (AtkinLehner70, Theorem 3, as cited
by the paper; verify which parts) If $p^2\mid N$ then $a_p(f)=0$; if $p\,\|\,N$ then $a_p(f)=-p^{k/2-1}\varepsilon_p(f)$, so in weight $2$
$a_p(f)=-\varepsilon_p(f)\in\{\pm1\}$. (iv) For $f=f_E$ (Chapter 14): $a_p=1$, $-1$, $0$ for split multiplicative, nonsplit multiplicative,
additive reduction at $p$. Checks: $f_{11}$: $\varepsilon_{11}=-1$, $a_{11}=1$ (Chapter 12, its 9.2(iii)); $a_{11}=0$ for 121a to 121d; $a_7=0$ for 539c,
539d; $a_7(77\text{c})=-1$, $a_{11}(77\text{c})=1$. Reference: AtkinLehner70 Theorem 3 (as cited); DiamondShurman 5.8 and 6.6 (cite the sections). Paper: Lemma
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
level $44$, $g^c\ni f_{11}-\beta f_{11}(2z)$ (a stabilisation), which is not orthogonal to $g$: with the Petersson Gram matrix of $f_{11}(z),f_{11}(2z),f_{11}(4z)$ at level $44$, proportional to
$\begin{psmallmatrix}1&-1/3&1/24\\-1/3&1/4&-1/12\\1/24&-1/12&1/16\end{psmallmatrix}$, one finds $\langle g,f_{11}-\beta f_{11}(2z)\rangle=\frac5{12}\langle f_{11},f_{11}\rangle$ (verified with PARI). Paper: Theorem thm:twist
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

### Section 9. Twisting

**9.1 `prop:hecke:twist-operator`** (proposition; P for (i), (iii) to (vi); S for (ii)). Let $\chi$ be a primitive Dirichlet character of
conductor $r$, $\mathfrak g(\bar\chi)=\sum_{u\bmod r}\bar\chi(u)e^{2\pi iu/r}$ its Gauss sum (Chapter 2), and $f\in S_k(M)$. (i)
$$f\otimes\chi=\sum_n\chi(n)a_n(f)q^n=\mathfrak g(\bar\chi)^{-1}\sum_{u\bmod r}\bar\chi(u)\,f\big|_k\begin{psmallmatrix}1&u/r\\0&1\end{psmallmatrix}$$
(from $\sum_u\bar\chi(u)e^{2\pi inu/r}=\chi(n)\mathfrak g(\bar\chi)$ for primitive $\chi$ and all $n$, Chapter 2). (ii) $f\otimes\chi\in S_k(\Gamma_0(\operatorname{lcm}(M,r^2)),\chi^2)$; for
quadratic $\chi$, $f\otimes\chi\in S_k(\operatorname{lcm}(M,r^2))$ (sketch: for $\gamma\in\Gamma_0(\operatorname{lcm}(M,r^2))$ and each $u$ there are $u'$ and $\gamma'\in\Gamma_0(M)$ with
$\begin{psmallmatrix}1&u/r\\0&1\end{psmallmatrix}\gamma=\gamma'\begin{psmallmatrix}1&u'/r\\0&1\end{psmallmatrix}$, $u'\equiv d^2u\pmod r$). (iii) If $\chi$ is quadratic and $f\in S_k(M;\Z)$ then
$f\otimes\chi\in S_k(\operatorname{lcm}(M,r^2);\Z)$ ($\chi(n)\in\{0,\pm1\}$). (iv) (Intertwining.) Let $\chi$ be quadratic and $L=\operatorname{lcm}(M,r^2)$. For a prime $p\nmid r$:
$T_p^{(L)}(f\otimes\chi)=\chi(p)\,(T_p^{(M)}f)\otimes\chi$, where on each side $T_p$ means $U_p$ if $p$ divides the level (compare coefficients with 2.3;
it uses $\chi(p)^2=1$); for $p\mid r$: $U_p^{(L)}(f\otimes\chi)=0$. So $f\mapsto f\otimes\chi$ maps the eigenspace of $\T^{(Mr)}$ for a system $(\lambda_p)$ into
the eigenspace for $(\chi(p)\lambda_p)$, and a normalised eigenform of $\T_M$ to a normalised eigenform of $\T_L$. (v) (Twisting twice.)
$(f\otimes\chi)\otimes\bar\chi=\sum_{(n,r)=1}a_n(f)q^n=f^{\{p\mid r\}}$; for a normalised eigenform $f$ this is the depleted form of 7.4. In
particular $g\otimes\chi\otimes\chi$ is the $q$-depletion of $g$, not $g$ (important_notes.md point 20). (vi) (The paper's $\iota$.) For a finite set $S$
of odd primes, $D$ and $\chi_S$ as in C7, $\iota=\iota_S\colon S_2(M)\to S_2(\operatorname{lcm}(M,D^2))$, $h\mapsto h\otimes\chi_S$, is $\C$-linear, maps $S_2(M;\Z)$ into
$S_2(\operatorname{lcm}(M,D^2);\Z)$, kills every $h(dz)$ with $(d,D)>1$, satisfies $\iota(h)=\iota(h^{S})$, and maps generalised eigenspaces of $\T^{(DM)}$ for
$(\lambda_p)$ into those for $(\chi_S(p)\lambda_p)$. Reference: Shimura71 Proposition 3.64 (verify); Miyake 4.3 (cite the section);
AtkinLi78 Section 3 (cite the section); DiamondShurman, the exercises on twists in Chapter 5 (verify, else omit). Paper: Theorem thm:twist ("$\iota$ ...
maps $S_2(\Gamma_0(N_S))$ into $S_2(\Gamma_0(\operatorname{lcm}(N_S,D^2)))$", "preserves integrality", "sends an eigenform of all $T_n$, $(n,N_S)=1$, to an
eigenform with eigenvalues twisted by $\chi_S(n)$", "kills the coefficients at multiples of $D$"), Theorem thm:quant Step 1 ("$\iota$
intertwines $T_p$ with $\chi_S(p)T_p$ for $p\nmid DN$"; "the level of a twist by $\chi_S$ divides $\operatorname{lcm}(N,D^2)=N$"), Theorem thm:qual (b), (c)
($h=g\otimes\chi$).

**9.2 `thm:hecke:atkin-li`** (theorem, Atkin-Li; R, with a sketch S via conductors). Let $g$ be a newform of weight $2$ on $\Gamma_0(M)$, $q$
an odd prime and $\chi=\chi_{q^*}$. (i) If $q\nmid M$, $g\otimes\chi$ is a newform on $\Gamma_0(Mq^2)$. (ii) If $q\,\|\,M$, $g\otimes\chi$ is a newform on
$\Gamma_0(Mq)$. In both cases the level is $\operatorname{lcm}(M,q^2)$; this is the paper's Lemma lem:twist (iii). (iii) If $q^2\mid M$, the $q$-series
$g\otimes\chi$ need not be a newform: it is the $q$-depletion $g'^{\{q\}}$ of the newform $g'$ with $a_p(g')=\chi(p)a_p(g)$ for $p\ne q$ (6.3), whose
level divides $M$ (9.1(ii) and 6.2(ii)) and may be smaller or equal. Examples (conductors of the twisted curves by PARI, labels
from `ecdata`): $q\nmid M$: 11a1 by $-11$ gives 121d2, by $-7$ gives 539d2; 20a1 by $-7$ gives 980g2 (not 980i); 37a1 by $5$ gives 925e1;
$q\,\|\,M$: 14a1 by $-7$ gives 98a3, 77c1 by $-7$ gives 539c1, 15a1 by $-3$ gives 45a4; $q^2\mid M$: 539c1 by $-7$ gives 77c1 and 539d1 by $-7$ gives 11a3
(level drops), 121a1 by $-11$ gives 121c2, 99a1 by $-3$ gives 99c1 and 49a1 by $-7$ gives 49a3 (level kept). Sketch (via Chapter 15): the level
of a newform is the conductor of its $\lambda$-adic Galois representation $\rho_g$ (Carayol86), and $\rho_{g\otimes\chi}=\rho_g\otimes\chi$; if $\rho_g$ is
unramified at $q$, or unipotent on inertia ($q\,\|\,M$, Steinberg), then $\rho_g\otimes\chi$ has no inertia invariants and is tame at $q$, so its
conductor exponent is $2$. Reference: AtkinLi78 Theorem 3.1 (as cited by the paper; verify the numbering and that the hypothesis
$q^2\nmid M$ is the one stated there); Li75 (proposed key; Part 6.5) for the case $q\nmid M$; Shimura71 3.6 (cite the section). Paper: Lemma
lem:twist (iii), Theorem thm:qual (b), (c) ("$h=g\otimes\chi$ is a newform on $\Gamma_0(Mq)$", "on $\Gamma_0(Mq^2)$"), Theorem thm:twist and Theorem
thm:quant ($\iota(g)=f$ in the cases $\mathrm{I}_n^*$, $\mathrm{I}_0^*$), the Example of Section 3 ($f_{\text{11a}}\otimes\chi_{-11}$ is the form of 121d).

**9.3 `prop:hecke:twist-transport`** (proposition; P given 6.2, 6.3, 9.1). Let $S$, $D$, $\chi_S$, $\iota$ be as in 9.1(vi). Let $g$ be a newform of
weight $2$ and level $M$ and $f$ the newform whose system is $(\chi_S(p)a_p(g))_{p\nmid DM}$ (6.3), of level $N_f$, and let $L$ be a common multiple
of $\operatorname{lcm}(M,D^2)$ and $N_f$. (i) If $h\in S_2(M)$ lies in the sum of the anemic generalised eigenspaces of systems different from that of $g$
(that is, $h\in g^\perp$ at level $M$, 6.2(iv)), then $\iota(h)\in S_2(L)$ lies in the sum of the anemic eigenspaces of systems different from that of $f$,
hence is orthogonal to every $f(dz)$; if $N_f=L$, $\iota(h)\in f^\perp$. (ii) If $f=\iota(g)$ (as $q$-series; this holds when $a_{n}(f)=0$ for all $n$ with
$(n,D)>1$, for instance when $q^2\mid N_f$ for all $q\in S$, given that $a_p(f)=\chi_S(p)a_p(g)$ also at the primes $p\mid M$ outside $S$, where the twist is
unramified; for elliptic curves this is $a_p(E^{(d)})=\chi_d(p)a_p(E)$ at a multiplicative $p\nmid d$, Chapter 9), then a congruence $g\equiv h\pmod r$ with $h\in g^\perp\cap S_2(M;\Z)$ gives $f\equiv\iota(h)\pmod r$
with $\iota(h)\in f^\perp\cap S_2(L;\Z)$. (iii) Conversely $\iota(f)=g^S$, and $\iota$ maps $f^\perp$ (at level $N_f$, with $D^2\mid N_f$) into the $\T$-stable complement
of $\C g^S$ at level $N_f$ whenever $g^S\in S_2(N_f)$ and the generalised eigenspace of $g^S$ there is a line (8.2): $f^\perp=\bigoplus_{h\ne f}V_h$, and
$\iota(V_h)\subset V_{h'}$ with $h'\ne g$, since $h'=g$ would force the system of $h$ to be that of $f$. This is the engine of the paper's Theorem
thm:twist and of Theorem thm:quant Step 1; the theorems themselves (with congruence numbers) are proved in Chapter 20. Paper:
Theorem thm:twist (its whole proof), Theorem thm:quant Step 1, Part 7 point N1.

### Section 10. The $L$-function of a newform; Rankin-Selberg

**10.1 `prop:hecke:euler-product`** (proposition; P). Let $f$ be a normalised eigenform of $\T_N$ of weight $k$. Then
$L(f,s)=\sum_{n\ge1}a_n(f)n^{-s}$ converges absolutely for $\operatorname{Re}s>k/2+1$ (Chapter 12, its 6.4) and
$$L(f,s)=\prod_{p\nmid N}\bigl(1-a_pp^{-s}+p^{k-1-2s}\bigr)^{-1}\prod_{p\mid N}\bigl(1-a_pp^{-s}\bigr)^{-1}$$
(3.2(ii) and 2.4(iv)). For a newform of weight $2$: the factor at $p\mid N$ is $(1\mp p^{-s})^{-1}$ if $p\,\|\,N$ and $1$ if $p^2\mid N$, and
$L_p(f,s)^{-1}=(1-\alpha_pp^{-s})(1-\beta_pp^{-s})$ at $p\nmid N$; $L(f^\Sigma,s)=L(f,s)\prod_{p\in\Sigma}L_p(f,s)^{-1}$; $L(f\otimes\chi,s)$ has the factors
$(1-\chi(p)a_pp^{-s}+\chi(p)^2p^{1-2s})^{-1}$ at $p\nmid rN$. For $f=f_E$, $L(f_E,s)=L(E,s)$ (modularity, Chapter 14). Reference: DiamondShurman 5.9
(cite the section). Paper: Section 1 (the $L$-function), Section 1.1 ($\delta_p$ is the degree of $L_p(f,s)^{-1}$), background.

**10.2 `thm:hecke:functional-equation`** (theorem; S). Let $f\in S_k(N)$ with $f|_kW_N=\varepsilon_Nf$ (Chapter 12, its 12.1). Then
$\Lambda(f,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(f,s)=N^{s/2}\int_0^\infty f(iy)y^{s-1}\,dy$ extends to an entire function, bounded in vertical strips, with
$\Lambda(f,s)=i^k\varepsilon_N\Lambda(f,k-s)$; in weight $2$ the sign is $-\varepsilon_N$. Sketch: split the Mellin integral at $y=1/\sqrt N$ and apply $W_N$ on
$(0,1/\sqrt N)$; each piece converges for all $s$ by the exponential decay of $f$ at the cusps. Physics aside: the Mellin transform, RHB's
integral transforms. Checks: 11a1 ($\varepsilon_{11}=-1$, sign $+1$, rank $0$), 37a1 ($\varepsilon_{37}=+1$, sign $-1$, rank $1$) (Chapter 12, its 12.4(c)).
Reference: DiamondShurman Theorem 5.10.2 (verify); Miyake 4.3 (cite the section). Paper: background (Section 1; Chapter 19 for the
adjoint and symmetric square $L$-functions).

**10.3 `thm:hecke:rankin-selberg`** (theorem; S, with numerical checks). Let $f\in S_k(N)$ (any cusp form). (i) $D(f,s)=\sum_{n\ge1}|a_n(f)|^2n^{-s}$
converges for $\operatorname{Re}s>k$, continues meromorphically to the whole plane (through the continuation of the Eisenstein series below), is
holomorphic on $\operatorname{Re}s\ge k$ except for a simple pole at $s=k$, and
$$\operatorname{Res}_{s=k}D(f,s)=\frac{3\,(4\pi)^k}{\pi\,\Gamma(k)\,\mu(N)}\,\langle f,f\rangle,\qquad\text{in weight }2:\quad\operatorname{Res}_{s=2}D(f,s)=\frac{48\pi}{\mu(N)}\langle f,f\rangle,$$
with the unnormalised Petersson product of Chapter 12 (C5) and $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]$. (ii) For a newform of weight $2$ with rational
coefficients and squarefree level: $D(f,s)=\zeta^{(N)}(s-1)\,L(\Sym f,s)/\zeta^{(N)}(2s-2)$, with $L(\Sym f,s)$ in the normalisation of the paper
and of PARI's `lfunsympow` ($L_p(\Sym f,s)=L_p(A_f,s-1)$), and so $\langle f,f\rangle=N\,L(\Sym f,2)/(8\pi^3)$. (iii) In general $D(f,s)$ is **not** the naive
symmetric square $L$-function: at a good prime $\sum_ra_{p^r}^2X^r=(1+pX)/\bigl((1-\alpha^2X)(1-pX)(1-\beta^2X)\bigr)$, an extra factor $1+p^{1-s}$; and at the
bad primes the correction factors are Chapter 19's (DFG04 Lemma 2.12, Shimura76). Sketch of (i): unfold $\int_{\Gamma_0(N)\backslash\mathfrak H}|f|^2y^kE(z,s)\,d\mu$
against the Eisenstein series $E(z,s)=\sum_{\Gamma_\infty\backslash\Gamma_0(N)}\operatorname{Im}(\gamma z)^s$, whose residue at $s=1$ is $1/\operatorname{vol}(\Gamma_0(N)\backslash\mathfrak H)=3/(\pi\mu(N))$.
Verified numerically (PARI, 30 digits): the residue formula of (i), computed from the Euler factors of `lfunsympow`, for 11a1, 37a1,
20a1, 121a1, 99a1; the formula of (ii) for 11a1 ($\langle f,f\rangle=0.04690014787\ldots$, $L(\Sym f,2)=1.05759924459\ldots$) and 37a1. Reference:
Shimura76; Rankin, *Contributions to the theory of Ramanujan's function $\tau(n)$ and similar arithmetical functions* I, II, Proc.
Cambridge Philos. Soc. 35 (1939) (proposed key `Rankin39`, Part 6.5); Zagier85; DFG04 Lemma 2.12 (as cited by the paper). Paper:
Section 1 ("$\langle f,f\rangle$ is the special value $L(\Sym f,2)$ up to the local factors at the bad primes (Rankin, Shimura; see DFG04 Lemma
2.12)"; "the Euler product of $\sum a_n(f)^2n^{-s}$", important_notes.md point 30), Section 6 map row (Petersson norm, Rankin-Selberg).

### Section 11. Worked examples from the paper's world

**11.1 `ex:hecke:level-88`** (example; P as a computation). $S_2(88)$, $d=9$: newforms of level $88$ (three, with $a_2=0$), $f_{44}$ (one, old twice),
$f_{11}$ (old four times). $U_2$ has characteristic polynomial $X^7(X^2+2X+2)$ and minimal polynomial $X^2(X^2+2X+2)$; on $V_{f_{11},2,3}$ its matrix is
$\begin{psmallmatrix}-2&1&0&0\\-2&0&1&0\\0&0&0&1\\0&0&0&0\end{psmallmatrix}$ with a Jordan block of size $2$ at $0$, kernel spanned by $f_{11}^{(2)}=f_{11}+2f_{11}(2z)+2f_{11}(4z)$, and the
stabilisations $f_{11}-\beta f_{11}(2z)$, $\alpha,\beta=-1\pm i$. So $\T_{88}\otimes\Q$ is not reduced, $\wp\cap I=0$ is a statement to be proved for the
depleted form (important_notes.md point 19), and the paper's "the eigenvalue $0$ with multiplicity one" (Theorem thm:quant Step 1) is a
statement about the minimal level $M^\Sigma$, which fails one level higher. Also $\operatorname{rank}\T_{88}=9$, pairing determinant $-1$,
$[\T_{88}:\Z T_1+\cdots+\Z T_9]=3$, congruence number of 88a1 equal to $16$ (modular degree $8$; $2^3\mid88$).

**11.2 `ex:hecke:congruence-numbers`** (example; P as a computation, by the lattice method of 4.3 and 4.2). Congruence numbers $r_f$ of
the rational newforms at small levels, against the modular degrees of the optimal curves (Cremona's `degphi` file):

| curve | 11a1 | 33a1 | 37a1 | 37b1 | 44a1 | 77a1 | 77b1 | 77c1 | 88a1 | 99a1 | 99b1 | 99c1 | 99d1 |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| $r_f$ | 1 | 3 | 2 | 2 | 2 | 4 | 20 | 6 | 16 | 12 | 12 | 12 | 6 |
| $\deg\varphi_E$ | 1 | 3 | 2 | 2 | 2 | 4 | 20 | 6 | 8 | 4 | 12 | 12 | 6 |

| curve | 121a1 | 121b1 | 121c1 | 121d1 | 539a1 | 539b1 | 539c1 | 539d1 |
|-|-|-|-|-|-|-|-|-|
| $r_f$ | 6 | 4 | 6 | 24 | 320 | 192 | 288 | 504 |
| $\deg\varphi_E$ | 6 | 4 | 6 | 24 | 320 | 192 | 288 | 72 |

The three differences (88a1 at $2$, 99a1 at $3$, 539d1 at $7$) are at primes $p$ with $p^2\mid N$, as the theorem of Agashe, Ribet and Stein
allows (Chapter 14); 99A1 with degree $4$ and congruence number $12$ is the paper's example (Remark after Theorem thm:qual, from ARS12
Table 1), and 539d1 (degree $72$, $r=504=2^3\cdot3^2\cdot7$) is a second one. Paper: Section 1, the remark after Theorem thm:qual ($99$A1).

**11.3 `ex:hecke:twist-pairs`** (example; P as a computation). The paper's twisting statements on actual forms. (a) Case (c) of Theorem
thm:twist ($N_S=N$): $r(121\text{a})=r(121\text{c})=6$ and $121\text{a}\otimes\chi_{-11}=121\text{c}$ (9.2). (b) Case $\mathrm{I}_n^*$: 539c1 has type $\mathrm{I}_3^*$ at $7$,
$539\text{c}\otimes\chi_{-7}$ corresponds to 77c ($q^2\mid M$, level drops), and $r(77\text{c})=6\mid288=r(539\text{c})$; with $\ell=3$: $v_3(288)=2=v_3(6)+v_3(7^2-1)$,
the equality case of Theorem thm:quant. (c) Case $\mathrm{I}_0^*$: 539d1, $539\text{d}\otimes\chi_{-7}$ corresponds to 11a, $r(11\text{a})=1\mid504$; $\ell=3$:
$v_3(504)=2=0+v_3(6)+v_3(8^2-(-2)^2)$. (d) Theorem thm:quant Step 1 at level $539$: the Hecke congruence modules (4.3, 8.2) of the depleted
forms $(77\text{c})^{\{7\}}=g-a_7(g)g(7z)$ and $(11\text{a})^{\{7\}}=f_{11}+2f_{11}(7z)+7f_{11}(49z)$ have orders $288$ and $504$, equal to $r(539\text{c})$ and
$r(539\text{d})$ at every prime (Part 7, point N1); and $\iota\bigl((77\text{c})^{\{7\}}\bigr)=f_{539\text{c}}$, $\iota\bigl((11\text{a})^{\{7\}}\bigr)=f_{539\text{d}}$ (checked to $n=3000$). Paper:
Theorem thm:twist (cases (a), (b), (c) and the data paragraph after it; important_notes.md point 16), Theorem thm:quant and its proof,
the remark after it.

**11.4 `ex:hecke:level-121`** (example; P). $S_2(121)$: four newforms 121a to 121d (all rational, $a_{11}=0$, $11^2\mid121$) and $V_{f_{11},11,1}$, on
which $U_{11}$ has matrix $\begin{psmallmatrix}1&1\\0&0\end{psmallmatrix}$ ($f_{11}$ has $a_{11}=1$, $11\,\|\,11$), eigenvectors $f_{11}$ (eigenvalue $1$) and $f_{11}-f_{11}(11z)$
(eigenvalue $0$, the depleted form of level $M^{\{11\}}=121$); $U_{11}$ on $S_2(121)$ has characteristic and minimal polynomials $X^5(X-1)$ and $X(X-1)$
(semisimple). $121\text{a}\equiv121\text{d}\pmod3$ at every $n$ (Chapter 12, its 11.5) and $121\text{d}=f_{11}\otimes\chi_{-11}$ (9.2(i)); $T_1,\dots,T_6$ are linearly
dependent although $\operatorname{rank}\T_{121}=6$, and $T_1,\dots,T_{22}$ ($B_2(121)=22$) span $\T_{121}$. Paper: the Example of Section 3 ((b): 121a1, 121c,
121d, 11a1), Theorem thm:qual (b).

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2 with its tag and `\Cref`; conventions C2, C3, C6, C7 restated in one line each | (excluded) |
| (starred) | Where the paper uses this chapter | Section 3 preamble ($\T$ with the $U_p$); Lemma lem:crit ($\phi_f$, $I$, $J$, $f^\perp$, the perfect pairing, over $\Z_\ell$); Lemma lem:old ($U_p$ on $h(p^jz)$, stabilisations, depleted forms, $a_p=0$ for $p^2\mid M$, multiplicativity and recursion); Lemma lem:twist (iii) (Atkin-Li); Theorem thm:twist ($\iota$, generalised eigenforms, $g^\perp\to f^\perp$); Theorem thm:quant Step 1 (strong multiplicity one, multiplicity one of $0$ for $U_q$, units, idempotents, $\eta^{\mathrm{Hecke}}$); Section 4.1 ($f^\Sigma$, $M^\Sigma$, $\delta_p$); Section 1 ($r_E$, Petersson norm and $L(\Sym f,2)$); Lemma lem:hecke (computed in $\T_{\mathfrak m}$, point 35) | 45 |
| 1 | Introduction and conventions | opening paragraph (what the chapter is for; the three physics connections); C1 to C10 as `convention` environments, with the double-coset normalisation box (C2) and the level-dependence warning (C3) | 70 |
| 2 | Hecke operators | 2.1 to 2.6; the coset computation written out; the $q$-expansion formulas; commutativity and the recursion with the Chebyshev aside; the Eisenstein examples; `paperlink`: Section 3 preamble and Lemma lem:old's formulas | 210 |
| 3 | The Hecke algebra and eigenforms | 3.1 to 3.4; `warning`: anemic eigenforms may have $a_1=0$; `warning`: full eigenforms at non-minimal level may have non-real $a_p$ ($-1\pm i$ at level $22$); `paperlink`: Lemma lem:crit's $\phi_f$ and maximal ideals | 150 |
| 4 | The integral structure: the perfect pairing | 4.1 to 4.3 with the full proof of 4.1 from Chapter 12's 11.2 and 11.4; the table of ranks and pairing determinants; `paperlink`: Lemma lem:crit "perfect", "verbatim over $\Z_\ell$"; the definitions of $\eta(\phi)$ and $r_f$ with the pointer to Chapter 15 | 160 |
| 5 | Petersson adjoints | 5.1 to 5.4; the level-$22$ Gram matrix and the adjoint of $U_2$ as a worked example; `paperlink`: Lemma lem:crit "eigenvector of the adjoints"; cohomological analogue pointer to Chapter 14 | 100 |
| 6 | Oldforms and newforms | 6.1 to 6.5; the Main Lemma sketched; strong multiplicity one with the density-one corollary via Chapter 15; the dimension table; `paperlink`: Lemma lem:old (orthogonality, $a_p=0$), Theorem thm:quant Step 1 (strong multiplicity one) | 210 |
| 7 | $U_p$ on oldforms; depletion | 7.1 to 7.4; the matrices at levels $22$, $44$, $88$, $121$; Jordan blocks; $f^\Sigma$, $M^\Sigma$, $\delta_p$ with the "why $\delta_p$" paragraph; `paperlink`: Lemma lem:old (each case), Section 4.1, Theorem thm:quant Step 1 (units and multiplicity one), point 19 | 200 |
| 8 | Structure of $\T$; congruences | 8.1 to 8.4; $\T\otimes\overline\Q=\prod A_h$; Petersson versus $\T$-stable complement with the level-$44$ computation; $\T_\ell=\prod\T_{\mathfrak m}$ on forms and on the pairing; congruences at primes versus at all $n$; `paperlink`: Lemma lem:crit's $\T\otimes\Q=\Q\times\T'$, Lemma lem:hecke (point 35), Theorem thm:quant Step 1 (idempotents) | 200 |
| 9 | Twisting | 9.1 to 9.3; Gauss-sum formula; level $\operatorname{lcm}(M,r^2)$; intertwining; $\iota\circ\iota=$ depletion (point 20); Atkin-Li with the examples table; the transport lemma; `paperlink`: Lemma lem:twist (iii), Theorem thm:twist, Theorem thm:qual (b), (c) | 170 |
| 10 | $L$-functions and Rankin-Selberg | 10.1 to 10.3; Mellin sketch (physics aside); unfolding sketch; the numerical table of residues; `warning`: the Rankin series is not the naive symmetric square (point 30); pointer to Chapter 19 | 120 |
| 11 | Worked examples | 11.1 to 11.4: level $88$; congruence numbers versus modular degrees (99A1, 539d1); the twist pairs at levels $121$ and $539$ and Step 1 of Theorem thm:quant on actual forms; level $121$ | 110 |
| 12 | Exercises | the 17 exercises of Part 4.2 | 140 |
| 13 | Notes and references | DiamondShurman, Shimura71, Miyake, SerreCourse, Koblitz, AtkinLehner70, Li75, AtkinLi78, Ribet83, AU96, ARS12, DDT, ColemanEdixhoven, Shimura76, Rankin39, Zagier85, DFG04, Stein, PARI; which numbers were cited and which are marked (verify) | 45 |
| | **total** | | **1,930** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| Hecke operators $T_n$ on $M_k(\Gamma_0(N))$ via double cosets | 2.1, 2.2, 2.4 |
| explicit formula on $q$-expansions: $a_n(T_pf)=a_{pn}+p^{k-1}a_{n/p}$ ($p\nmid N$); $a_n(U_pf)=a_{pn}$ ($p\mid N$) | 2.3, 2.4(iii) |
| commutativity; multiplicativity $T_{mn}=T_mT_n$ for coprime $m,n$; $T_{p^{r+1}}=T_pT_{p^r}-p^{k-1}T_{p^{r-1}}$ | 2.4 |
| the Hecke algebra $\T=\Z[T_n]$ in $\operatorname{End}(S_2)$, finite free over $\Z$ of rank $\dim S_2$, with the $U_p$ | 3.1, 4.1(iii) |
| self-adjointness of $T_n$, $(n,N)=1$; non-self-adjointness of $U_p$ | 5.1, 5.2, 5.3 |
| eigenforms and normalised eigenforms ($a_1=1$, $T_nf=a_nf$) | 3.2 |
| the eigencharacter $\phi_f\colon\T\to\Z$ or $\mathcal O$; coefficient field and its ring of integers | 3.2(iii), 3.3, 3.4 |
| oldforms and newforms: $f(z)\mapsto f(dz)$, $d\mid N/M$; old subspace; new subspace as orthogonal complement | 6.1 |
| Atkin-Lehner theory: newform basis of the new subspace, eigenforms for all $T_n$ and $U_p$, multiplicity one | 6.2, 6.4 |
| strong multiplicity one (density one; same eigenvalues for almost all $p$) | 6.3 |
| $U_p$ on the span of $h(z)$, $h(pz)$: $X^2-a_p(h)X+p$, stabilisations $h-\beta h(pz)$, $h-\alpha h(pz)$ | 7.1(ii), (iii) |
| on $h(z)$, $h(pz)$, $h(p^2z)$: eigenvalue $0$, depleted form $h-a_ph(pz)+ph(p^2z)$ | 7.1(iii) |
| $p\,\|\,M$: $U_p$ acts by $a_p(h)$ on $h$; $h-a_ph(pz)$ has eigenvalue $0$ | 7.1(iii) |
| $p^2\mid M$: $a_p(h)=0$ (Atkin-Lehner Theorem 3), $U_p$ kills $h$ | 6.4(iii), 7.1(iii) |
| non-semisimplicity of $U_p$ when $0$ is a repeated eigenvalue | 7.1(iv), 7.3, 11.1 |
| the $\Sigma$-depleted form $f^\Sigma$, its level $M^\Sigma=M\prod p^{\delta_p}$, $\delta_p=2,1,0$ (explain why) | 7.4 |
| $S_2(\Gamma_0(N))\otimes\overline\Q=\bigoplus$ spans of $h(dz)$ | 6.2(iii), 8.1(i) |
| generalised eigenspaces of $\T$ and their relation to newforms | 8.1(iii), 8.2 |
| $\T\otimes\Q$ as a product of fields times the old part | 8.1(ii), (iv) |
| the orthogonal complement $f^\perp$ of a newform and its $\T$-stability | 5.4, 6.2(iv), 6.4(ii), 8.1(iv) |
| twisting by Dirichlet characters; Atkin-Li ($q^2\nmid M$: $g\otimes\chi$ newform of level $\operatorname{lcm}(M,q^2)$) | 9.1, 9.2 |
| the twist map $\iota$ on the whole space; intertwines $T_p$ with $\chi(p)T_p$ for $p$ prime to the conductor | 9.1(iv), (vi), 9.3 |
| integral structure: $S_2(\Gamma_0(N);\Z)$ is a lattice (Chapter 12, B11) | 4.1 (citing Chapter 12, its 11.2, 11.4) |
| the perfect pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$, $(g,t)\mapsto a_1(tg)$ (Ribet 1983, Abbes-Ullmo), proved via the $q$-expansion principle | 4.1 |
| consequences: $\T$ free of rank $\dim S_2$; $\operatorname{Hom}(\T,\Z)=S_2(\Z)$; a form is determined by its pairing with $\T$ | 4.1(iii), 4.2, 3.4 |
| congruences between eigenforms mod $\lambda$: all $n$ versus $n$ prime to a set | 8.4 |
| the recursion for $a_{p^k}$ and multiplicativity, so congruences at primes propagate to all $n$ | 3.2(ii), 8.4(i) |
| $L(f,s)=\sum a_nn^{-s}=\prod(1-a_pp^{-s}+p^{1-2s})^{-1}\prod_{p\mid N}(1-a_pp^{-s})^{-1}$ | 10.1 |
| analytic continuation and functional equation (statement) | 10.2 |
| Rankin-Selberg and $\langle f,f\rangle=$ (explicit factor) $L(\Sym f,2)$ (statement; precise form in Chapter 19) | 10.3 |
| Section 6 row: newform $f_E$, $S_2(\Gamma_0(N))$, $q$-expansions, coefficientwise congruences (with Chapter 12) | 3.2, 6.2, 8.4 |
| Section 6 row: congruence ideal, congruence number $r_E$, $\eta^\Sigma$, $M_{f,\lambda}$, $\hat\delta_!$ (with 14, 20) | 4.3, 8.2, 8.3, 11.2 ($\eta^\Sigma$, $M_{f,\lambda}$, $\hat\delta_!$: Chapters 14, 20; $f^\Sigma$, $M^\Sigma$: 7.4) |
| Section 6 row: Petersson norm, Rankin-Selberg, $L(\Sym f,2)$ (with 12, 14, 19) | 10.3 |
| Section 6 row: Atkin-Li, Atkin-Lehner $a_p=0$, oldforms, $U_p$ eigenvalues, stabilisations, depleted forms | 6.4, 7.1, 7.2, 7.4, 9.2 |
| Section 6 row: perfect pairing $S_2(\Gamma_0(N);\Z)\times\T\to\Z$ (Ribet 1983, Abbes-Ullmo) | 4.1 |
| hook: Lemma lem:crit ($\T$, $\phi_f$, $I$, $J$, $f^\perp$, the perfect pairing, $\T/(I+J)$ cyclic of order $r$) | 3.1, 3.2, 3.4, 4.1, 4.2, 4.3, 5.4, 8.1(iv), 8.4 (the proof of the lemma: Chapter 15) |
| hook: Lemma lem:old (oldforms, $U_p$ eigenvalues, stabilisations, depleted forms, $a_p=0$ for $p^2\mid M$, multiplicativity, recursion) | 2.3, 3.2(ii), 6.2(iv), 6.4(iii), 7.1, 8.1(i), 8.4 (the proof of the lemma: Chapter 15) |
| hook: Lemma lem:twist (iii) (Atkin-Li) | 9.2 |
| hook: Theorem thm:twist ($\iota$, generalised eigenforms, $g^\perp\to f^\perp$) | 6.3, 8.1, 8.2, 9.1, 9.3, 11.3 (the proof: Chapter 20) |
| hook: Theorem thm:quant Step 1 (strong multiplicity one, stabilisations, $U_q$ eigenvalue $0$ with multiplicity one, idempotents) | 6.3, 7.1, 7.2, 7.4(iv), 8.2, 8.3, 9.3, 11.3 (the proof: Chapter 20) |
| hook: Section 4.1 ($f^\Sigma$, $M^\Sigma$, $\delta_p$) | 7.4 |
| hook: Section 1 (congruence number $r_E$, Petersson norm) | 4.3, 10.3, 11.2 |
| also: Lemma lem:hecke ("computed in $\T_{\mathfrak m}$"; point 35) | 8.3(ii) |
| also: Theorem thm:qual (b), (c) ($h=g\otimes\chi$ newform; $h\ne f$; point 20) | 6.3, 9.1(v), 9.2 |
| also: the Example of Section 3 (121d $=f_{\text{11a}}\otimes\chi_{-11}$; congruences at all $n$; point 46) | 8.4(iii), 9.2, 11.4 |
| also: the remark after Theorem thm:qual (99A1: degree $4$, congruence number $12$) | 11.2 |
| also: Section sec:eis (Eisenstein maximal ideal of $\T_{11}$) | 2.5(ii) |
| also: important_notes.md points 16, 19, 20, 21, 30, 35, 36, 46; B8, B10, B11 | 11.3; 7.3, 11.1; 9.1(v); 9.2 (980g versus 980i); 10.3(iii); 8.3(ii); 8.3(iii); 8.4(iii); 9.2; 10.3 (C5 only); 4.1 |
| also: what Chapters 2, 3, 6, 8, 9, 12 deferred here | 9.1 (Gauss sums), 7.1, 7.3, 8.1 (Chapter 3's 10.7(v), Exercise 14), 3.3 (Chapter 6's 7.1), 2.6 (Chapter 8's 12.1(c)), 3.2(ii), 9.2 (Chapter 9's 8.3, 10.4), 4.1, 5.3, 6.4, 7.4, 8.4 (Chapter 12's C8, 10.3, 10.5(a), 11.4(v), 12.4(c)) |

### 4.2 Exercises (Section 12 of the chapter), graded from easy to harder

1. Write down the coset decompositions of $\Gamma_0(N)\operatorname{diag}(1,p)\Gamma_0(N)$ for $p\nmid N$ and for $p\mid N$, and derive the $q$-expansion formulas of
   2.3, including the constant term. Show that with Diamond-Shurman's slash normalisation the operator is the same (C2).
2. Prove $T_pT_{p'}=T_{p'}T_p$ and $T_pU_q=U_qT_p$ from the $q$-expansion formulas. Prove $\sum_rT_{p^r}X^r=(1-T_pX+pX^2)^{-1}$ and identify $T_{p^r}$ with a
   rescaled Chebyshev polynomial of the second kind.
3. For 11a1 check with PARI (`ellan`) that $a_{mn}=a_ma_n$ for coprime $m,n\le200$, that $a_{p^{r+1}}=a_pa_{p^r}-pa_{p^{r-1}}$ for $p\ne11$, and that
   $a_{11^r}=1$. Explain why $a_{11^r}=a_{11}^r$ is a statement about $U_{11}$.
4. (The perfect pairing at a small level.) At level $33$ find a $\Z$-basis of $S_2(33;\Z)$ from $q$-expansions up to the Sturm bound $8$,
   write the matrices of $T_1,\dots,T_8$, show that they span a lattice of rank $3$, and check that the pairing matrix $(a_1(t_jg_i))$ has
   determinant $\pm1$. At level $77$ show that $T_1,\dots,T_7$ span a sublattice of index $5$ in $\T_{77}$.
5. (Check the paper's claim in Lemma lem:crit that the pairing stays perfect "after tensoring with $\Z_\ell$".) Show that a perfect
   pairing of free $\Z$-modules stays perfect after $\otimes A$ for every ring $A$; show that $\T_\ell=\prod_{\mathfrak m}\T_{\mathfrak m}$ and that the pairing is
   perfect on each $e_{\mathfrak m}S_2(N;\Z_\ell)\times\T_{\mathfrak m}$. Do the other local factors lie in $\ker\phi_f$ or in $\operatorname{Ann}(\ker\phi_f)$ (point 35)?
6. At level $22$ compute the Petersson Gram matrix of $f_{11}(z)$, $f_{11}(2z)$ (with PARI's `mfpetersson`, remembering that it divides by
   $\mu(22)=36$), the matrix of $U_2$ and of its adjoint, and check $U_2^\dagger=w_{22}U_2w_{22}$. Show that $U_2$ is not normal.
7. (Non-semisimple $U_p$.) Compute the matrix of $U_2$ on $\operatorname{span}\{f_{11}(2^jz):0\le j\le3\}\subset S_2(88)$, its characteristic and minimal polynomials,
   and a basis of eigenvectors and generalised eigenvectors. Deduce that $\T_{88}\otimes\Q$ is not reduced, and explain why the paper's
   Lemma lem:ddt417 needs $\wp\cap I=0$ to be proved rather than assumed (point 19).
8. (Check the paper's claims in Lemma lem:old.) For a newform $h$ of level $M$ verify that the stabilisations and depleted forms of 7.1 are
   $U_p$-eigenvectors with the stated eigenvalues in each of the cases $p\nmid M$, $p\,\|\,M$, $p^2\mid M$, and that every eigenvalue has a
   one-dimensional eigenspace.
9. (Check the paper's claim in Section 4.1 that $f^\Sigma$ has level $M^\Sigma$.) For $f=f_{11}$ compute $f^\Sigma$ for $\Sigma=\{2\}$, $\{11\}$, $\{2,11\}$,
   $\{3,5\}$, its level, and show that it is not of smaller level. Show $L(f^\Sigma,s)=L(f,s)\prod_{p\in\Sigma}L_p(f,s)^{-1}$ and explain $\delta_p$ as the
   number of roots removed.
10. (Check the paper's claim in Theorem thm:quant Step 1.) Show that every eigenvalue of $U_q$ on $S_2(N)$ is $0$, $\pm1$ or a root of
    $X^2-aX+q$, hence $0$ or an $\ell$-adic unit for $\ell\ne q$. For $g=$ 77c, $q=7$, $N=539$ and for $g=$ 11a, $q=7$, $N=539$ show that the eigenvalue
    $0$ of $U_7$ on $\operatorname{span}\{g(dz)\}$ has multiplicity one, and find the characteristic polynomial of $U_7$ on $S_2(539)$.
11. Prove the dimension formula of 6.5 and its Moebius inversion; compute $\dim S_2^{\mathrm{new}}(N)$ for $N=88,121,539$ from the dimensions of
    $S_2(M)$, $M\mid N$, and compare with PARI.
12. (Twists.) Prove the Gauss-sum formula for $f\otimes\chi$ and the intertwining $T_p(f\otimes\chi)=\chi(p)(T_pf)\otimes\chi$ for quadratic $\chi$, $p\nmid r$.
    Show $(f\otimes\chi)\otimes\chi=f^{\{p\mid r\}}$. In the paper's case (b) of Theorem thm:qual, show that $h\otimes\chi$ is the $q$-depletion of $g$,
    and use strong multiplicity one to prove $h\ne f$ (point 20).
13. (Check the paper's Lemma lem:twist (iii).) With PARI's `elltwist` and `ellglobalred`, find the conductors of the twists of 11a1
    by $-11$ and $-7$, of 14a1 and 77c1 by $-7$, and of 539c1, 539d1, 121a1 by $-7$, $-7$, $-11$. Which satisfy $q^2\nmid M$, and where does the level
    drop? Show that the twist of 20a1 by $-7$ lies in the class 980g, so that the paper's congruence for 980i1 is a congruence between
    two different newforms of level $980$.
14. (Check the paper's claim, from ARS12 Table 1, that 99A1 has modular degree $4$ and congruence number $12$.) Compute $r_f$ for the
    newform of 99a by the lattice method of 4.3 at level $99$; compare with $\deg\varphi_E$ from `ellmoddegree`, and explain why the
    discrepancy is at $3$. Do the same for 539d1 ($r=504$, degree $72$).
15. (Check case (c) of Theorem thm:twist.) Compute $r_f$ for 121a and 121c at level $121$ and verify that they are equal and that
    $121\text{a}\otimes\chi_{-11}=121\text{c}$. Check $r(77\text{c})\mid r(539\text{c})$.
16. (Rankin-Selberg; point 30.) Compute $\langle f,f\rangle$ for 11a1 (unnormalised) and $L(\Sym f,2)$ with `lfunsympow`, and check
    $\langle f,f\rangle=11\,L(\Sym f,2)/(8\pi^3)$. Show that at a good prime $\sum_ra_{p^r}^2X^r=(1+pX)/((1-\alpha^2X)(1-pX)(1-\beta^2X))$, and deduce
    that $\sum a_n^2n^{-s}$ is not the naive symmetric square $L$-function.
17. Prove the functional equation of $L(f,s)$ from the Mellin transform and $W_N$; compute the sign for 11a1 and 37a1 from $\varepsilon_N$ and
    compare with their ranks.

## 5. Dependencies and forward pointers

Results from other chapters used here:
* Background (PLAN.md Section 2): linear algebra (commuting operators, eigenspaces and generalised eigenspaces, Jordan form as a
  statement, Hermitian inner products and adjoints, the spectral theorem for commuting normal operators, tensor products of
  vector spaces); complex analysis (Fourier and Mellin transforms, change of variables in integrals); RHB (Chebyshev
  polynomials, Mellin transforms).
* Chapter 2 (`ch:rings`): Dirichlet characters, conductors, primitive characters, Gauss sums and $\sum_u\bar\chi(u)\zeta^{nu}=\chi(n)\mathfrak g(\bar\chi)$ (9.1), the
  Kronecker symbols $\chi_{q^*}$ (C7), multiplicative functions and Moebius inversion (6.5), $\sigma_{k-1}$ (2.5).
* Chapter 3 (`ch:modules`): free modules and saturation (4.1, 4.2), the algebra-module duality 9.6 (4.1, 4.2), finite free algebras and
  idempotents 10.1 to 10.4 (8.1, 8.3), generalised eigenspaces 10.5 and the idempotent congruence 10.6 (8.1, 8.3), semisimplicity and the
  shift operator 10.7(v) (7.1, 7.3), common eigenvectors 10.8 (8.1), congruence ideals 11.1 (4.3, 8.3(ii)).
* Chapter 4 (`ch:reps`): Brauer-Nesbitt (only in the sketch of 6.3(ii)).
* Chapter 5 (`ch:galois`): Chebotarev (only in the sketch of 6.3(ii)).
* Chapter 6 (`ch:ant`): algebraic integers, orders and coefficient fields (its 7.1, used in 3.3), primes $\lambda$ above $\ell$ (its 7.2).
* Chapter 7 (`ch:local`): $\Z_\ell$, $\mathcal O_\lambda$ (8.3).
* Chapter 8 (`ch:curves`): the Hecke correspondences (its 12.1(c), only in 2.6).
* Chapter 9 (`ch:ellcurves`): $X^2-a_pX+p$ with roots $\alpha$, $\beta$ (its 8.3, used in 7.1), quadratic twists of curves and $a_p(E^{(d)})=\chi_d(p)a_p(E)$
  (its 10.4, used in 9.2's examples).
* Chapter 12 (`ch:modforms`): the slash operator C3 (C2 here), $M_k$, $S_k$ and $q$-expansions (its 6.2, 6.3), $V_d$ (its 6.2(e)), the Hecke
  bound (its 6.4), nebentypus (its 6.6, for 9.1(ii)), the Petersson product and its behaviour under change of level and under $W_d$
  (its 10.1, 10.2, 12.2), the integral basis theorem and the Sturm bound with their consequences (its 11.2, 11.3, 11.4: the input of 4.1),
  the Atkin-Lehner involutions (its 12.1 to 12.4), $\mu(N)$ (its 3.1), the level-$11$ form (its 9.2), the paper's congruences (its 11.5).

Black boxes imported from later chapters (stated with a forward `\Cref`, used only in sketches, remarks, examples and `paperlink`s,
never in the proof of a numbered result here): the Galois representations of newforms, the equality of level and conductor
(Carayol) and Brauer-Nesbitt for them (Chapter 15; used in the sketches of 6.3(ii) and 9.2); modularity $f_E\leftrightarrow E$ and the
modular degree (Chapter 14; used in 6.4(iv), 10.1, 11.2); the exact Rankin-Selberg formula with bad factors and $L(\Sym f,s)$ (Chapter
19; used in 10.3(ii), (iii)).

Forward pointers (chapters that use this one):
* Chapter 14 (`ch:moddeg`): $\T$ and its freeness (3.1, 4.1) for the Hecke action on $J_0(N)$ and $H^1(X_0(N),\Z)$; the remark 2.6 on
  correspondences; $U_p^\dagger=w_NU_pw_N$ for the Petersson product (5.3) as the model of the cup-product statement
  "$w_NT_nw_N$ is the adjoint"; newforms and $a_p=\pm1,0$ (6.4); the congruence number $r_f$ and $\eta(\phi_f)$ (4.3, 11.2) for
  Agashe-Ribet-Stein; the maximal ideals $\mathfrak m$ (3.4, 8.3) for multiplicity one and the Gorenstein property; the Eisenstein example
  2.5(ii).
* Chapter 15 (`ch:modgalrep`): the perfect pairing and its consequences (4.1, 4.2), $\T\otimes\Q=\Q\times\T'$ (8.1(iv)), the eigencharacter
  dictionary (3.4) and congruences (8.4) for the proof of Lemma lem:crit; $U_p$ on oldforms, the tensor structure and the depleted
  forms (7.1, 8.1), $a_p=0$ for $p^2\mid M$ (6.4), multiplicativity and the recursion (3.2) for the proof of Lemma lem:old; strong
  multiplicity one (6.3) and Atkin-Li (9.2) for Theorem thm:qual; the level of a newform as conductor (9.2's sketch).
* Chapter 19 (`ch:lfunctions`): $L(f,s)$, its Euler factors and $\delta_p$ (10.1, 7.4), the functional equation (10.2), the Rankin-Selberg
  residue (10.3) and point 30.
* Chapter 20 (`ch:congruence`): $\T$ finite free (4.1), $\T_\ell=\prod\T_{\mathfrak m}$ on forms and the local pairing (8.3), $\eta(\phi)$ (4.3), $f^\Sigma$,
  $M^\Sigma$, $\delta_p$ and multiplicity one for $f^\Sigma$ (7.4), the $\T$-stable complement (8.2), units among $U_q$-eigenvalues (7.2), the
  twist operator and the transport lemma (9.1, 9.3) for the proofs of Theorem thm:twist and Theorem thm:quant; point N1 of Part 7.
* Chapter 21 (`ch:paper`): A3.1 to A3.3 (Lemma lem:crit, Lemma lem:old), A2.4 (Lemma lem:twist (iii)), A4.14 to A4.16 (Theorem
  thm:twist, Theorem thm:quant), the remark after Theorem thm:qual (99A1, 11.2), the Example of Section 3 (9.2, 11.4).
* Chapter 22 (`ch:computation`): PARI's `mfinit`, `mfbasis`, `mfcoefs`, `mfheckemat`, `mfdim` (with flags for the full and the new space),
  `mfsturm`, `mfpetersson`, `mfatkininit`, `mffromell`, `mfbd`, `elltwist`, `ellglobalred`, `lfunsympow`, `matrixqz` as used in Part 6.6; the
  lattice method for congruence numbers (11.2).

## 6. Notes for the writer

### 6.1 Conventions to state (Section 1 of the chapter, as `convention` environments)

C1 to C10 of Part 1.2. The three normalisations to box: (a) $T_p$ and $U_p$ (C2, C3, 2.3): $[\Gamma\alpha\Gamma]_kf=(\det\alpha)^{k/2-1}\sum f|_k\alpha_i$ with Chapter 12's
slash, giving $a_n(T_pf)=a_{pn}+p^{k-1}a_{n/p}$ and $a_n(U_pf)=a_{pn}$, the same operators as Diamond-Shurman's; $T_{p^r}=U_p^r$ for $p\mid N$;
level written as a superscript whenever two levels occur. (b) The pairing: $\langle g,t\rangle=a_1(tg)$ on $S_2(N;\Z)\times\T_N$, $\Z$-bilinear, with
$\langle ug,t\rangle=\langle g,ut\rangle$; the Petersson product is a different, sesquilinear, transcendental pairing and is never called "the pairing".
(c) Twists: $f\otimes\chi=\sum\chi(n)a_nq^n$ with $\chi(n)=0$ for $(n,r)>1$, so twisting kills the coefficients at multiples of the conductor and
twisting twice depletes; $\chi_{q^*}$ for the paper's $\chi_q$; $\iota=\iota_S$ for the paper's twist map; $\chi_{-7}(2)=+1$, $\chi_{-11}(2)=-1$.

### 6.2 Pitfalls

* **Level dependence of $T_p$** (C3). "$T_p$" on a form of level $M$ and "$U_p$" on the same form viewed at level $Mp$ differ by $p^{k-1}V_p$.
  Lemma lem:old and Theorem thm:quant Step 1 work at level $N$ with forms of lower level; every computation must say at which level
  the operator acts.
* **Anemic versus full.** Multiplicity one holds for $\T^{(N)}$ on the new subspace and for the full $\T$ on a newform at its own level,
  not for $\T^{(N)}$ on $S_k(N)$ (the anemic eigenspace of $h$ is $V_h$, of dimension $\sigma_0(N/M_h)$). An anemic eigenform can have $a_1=0$
  ($f_{11}(2z)$); only full eigenforms can be normalised.
* **Non-real eigenvalues.** Eigenforms of the full $\T$ that are not newforms can have non-real coefficients ($a_2=-1\pm i$ for the
  $2$-stabilisations of $f_{11}$); "$K_f$ totally real" is for newforms (and for anemic eigenvalues) only. Chapter 6's 7.1 states it for
  newforms; keep it so.
* **Multiplicity of an eigenvalue versus semisimplicity.** The eigenvalue $0$ of $U_7$ at level $539$ has multiplicity $42$ and $U_7$ is
  semisimple; at level $88$ the eigenvalue $0$ of $U_2$ has multiplicity $7$ and $U_2$ is not. The paper's "multiplicity one" in Theorem thm:quant
  Step 1 is the algebraic multiplicity of $0$ on the span of the $g(dz)$; say so.
* **$\T$-stable versus Petersson complement** (8.2). They agree for newforms at their level, not for depleted or stabilised forms
  (level $44$ computation). Theorem thm:twist uses the Petersson complement at level $N_S$ (where $g$ is new) and Theorem thm:quant
  Step 1 the $\T$-stable complement at level $N$; the proof of Lemma lem:crit runs for any eigencharacter whose generalised
  eigenspace is a line, with the $\T$-stable complement.
* **Twist of a $q$-series versus newform** (9.1(v), 9.2(iii)). $g\otimes\chi$ is a newform only when $q^2\nmid M$; otherwise it is the
  $q$-depletion of a newform of level dividing $M$. $g\otimes\chi\otimes\chi=g^{\{q\}}$, not $g$ (point 20). Name forms by class, not by curve, when
  twisting (point 15, B8): $11\text{a}\otimes\chi_{-11}=121\text{d}$, $11\text{a}\otimes\chi_{-7}=539\text{d}$, $20\text{a}\otimes\chi_{-7}=980\text{g}$ (not 980i),
  $77\text{c}\otimes\chi_{-7}=539\text{c}$.
* **$T_1,\dots,T_d$ do not span $\T$.** The Sturm bound $B$ is the right number (4.1(iv)); at level $121$ even linear independence fails.
* **Congruences at primes versus at all $n$** (8.4). The recursion transfers congruences at all primes (including $p\mid N$) to all $n$
  between full eigenforms of the same level; Sturm transfers a finite check to all $n$ between any two forms of the same space;
  neither turns a congruence at $p\notin\Sigma$ into one at all $n$ without depletion or a choice of $U_p$-eigenvalues (Lemma lem:old).
* **The Rankin series** (10.3(iii)): $\sum a_n^2n^{-s}$ is not the naive symmetric square (point 30); the factor $1+p^{1-s}$ at good primes and
  the bad-prime corrections must be written out; the squarefree formula $\langle f,f\rangle=NL(\Sym f,2)/(8\pi^3)$ is with the unnormalised
  Petersson product and PARI's normalisation of $L(\Sym f,s)$; the general formula is Chapter 19's.
* **Petersson normalisation** (Chapter 12, C5): PARI's `mfpetersson` divides by $\mu(N)$; Gram matrices in 5.3 and 8.2 are given up to the
  common factor and do not depend on it.
* **Theorem numbers.** Unverified: Ribet83 Theorem 2.2, AU96 Lemma 2.1, AtkinLi78 Theorem 3.1, AtkinLehner70 Theorem 3 (cited as the
  paper cites them, marked "as cited by the paper"); DiamondShurman 5.2.2, 5.3.1, 5.5.2, 5.5.3, 5.7.1, 5.8.3, 5.10.2; Shimura71 3.24, 3.64;
  Miyake 4.6.19. Cite sections where unsure.
* **Do not prove here** the paper's Lemma lem:crit or Lemma lem:old (Chapter 15), Theorem thm:twist or Theorem thm:quant (Chapter 20).
  This chapter supplies every Hecke-theoretic step they quote, and the `paperlink`s say which.
* Typography (PLAN.md 7.2): "Atkin-Lehner", "Atkin-Li", "Rankin-Selberg", "Eichler-Shimura", "Coleman-Edixhoven", "Diamond-Shurman" with
  plain hyphens; no Unicode; $\mathfrak g(\chi)$ for Gauss sums (not $g$, which names forms).

### 6.3 What to leave to Chapters 12, 14, 15, 19 and 20

* **Chapter 12** (`ch:modforms`): the spaces, the slash operator, $q$-expansions, $V_d$, the Petersson product and its normalisation, the
  Atkin-Lehner involutions $w_d$ as operators, Shimura's integral basis theorem, $S_2(N;A)$, Sturm's bound and the split truncation
  (book-internal note B11). Chapter 13 cites them and does not reprove them.
* **Chapter 14** (`ch:moddeg`): $X_0(N)$ over $\Q$, $J_0(N)$, the Hecke correspondences and their action on $J_0(N)$ and on $H^1(X_0(N),\Z)$, the
  cup-product adjointness $T_n^\dagger=w_NT_nw_N$ and the pairing $\hat\delta_!$, modularity, the modular degree, the theorem of
  Agashe-Ribet-Stein, multiplicity one $\dim J_0(N)[\mathfrak m]=2$, the Gorenstein property of $\T_{\mathfrak m}$, the Eisenstein ideal. Chapter 13 gives only
  the Petersson-product analogue (5.3) and the algebraic $\mathfrak m$ (3.4, 8.3).
* **Chapter 15** (`ch:modgalrep`): Galois representations $\rho_{f,\lambda}$, local-global compatibility, the conductor of $\rho_f$ equal to the level,
  the full proofs of Lemma lem:crit and Lemma lem:old, level lowering and Theorem thm:qual. Chapter 13 gives the Hecke side (4.1, 7.1,
  8.1, 8.4, 9.2) and uses Chapter 15 only in sketches.
* **Chapter 19** (`ch:lfunctions`): $L(\Sym f,s)$ and $L(\ad f,s)$, naive versus true factors, $\delta_p$ from the Galois side, the exact
  Rankin-Selberg formula with bad factors (DFG04 Lemma 2.12, Shimura76), point 30 in full. Chapter 13 states the residue formula and the
  squarefree case.
* **Chapter 20** (`ch:congruence`): congruence modules, $\eta^\Sigma_{f,\lambda}$, $M_{f^\Sigma,\lambda}$, Lemma lem:ddt417, Lemma lem:hecke, Theorem thm:dfg14 and
  the proofs of Theorem thm:twist and Theorem thm:quant (including point N1). Chapter 13 gives $f^\Sigma$, $M^\Sigma$, $\delta_p$ (7.4), the
  $\T$-stable complement (8.2), $\T_{\mathfrak m}$ (8.3) and the transport lemma (9.3).

### 6.4 How the relevant important_notes.md points are handled

* **Point 19** (Lemma lem:ddt417: $\wp\cap I=0$ is not automatic; the full Hecke algebra can contain nilpotents). 7.3(i) and 11.1 prove,
  with the level-$88$ matrices, that $\T_{88}\otimes\Q$ is not reduced and locate the Jordan blocks; 7.4(iv) and 8.1(iv) prove the
  multiplicity-one statements that make $\eta\ne0$ in the paper's applications (newform at its level; $f^\Sigma$ at level $M^\Sigma$; $g^S$ at
  level $N$). The algebraic fix ($\wp\cap I=0$ iff $\eta\ne0$) is Chapter 3's 11.1(ii).
* **Point 20** (Theorem thm:qual (b), (c): $g=h\otimes\chi$ is not literal). 9.1(v) proves $(g\otimes\chi)\otimes\chi=g^{\{q\}}$; Exercise 12 derives $h\ne f$
  from strong multiplicity one (6.3). Chapter 15 applies it.
* **Point 21** (980i1 is outside the hypotheses of Theorem thm:qual, $5\mid980$). Chapter 13 uses 980i1 only as a twisting and level
  example and says so; 9.2 adds that $20\text{a}\otimes\chi_{-7}$ is 980g, so the paper's congruence for 980i1 is between two different newforms.
* **Point 30** (the naive adjoint $L$-function is not the Euler product of $\sum a_n^2n^{-s}$). 10.3(ii), (iii) state the correct relation and the
  extra factor $1+p^{1-s}$; Exercise 16 checks it. The precise statement at bad primes is Chapter 19's.
* **Point 35** (Lemma lem:hecke: the other local factors lie in the kernel, not in the annihilator). 8.3(ii) states the correct version
  for $\T_\ell$ acting on forms; Exercise 5 asks the question.
* **Point 36** (the pairing stays perfect on the $\mathfrak m$-component). 8.3(iii) proves the analogue for the pairing $\langle g,t\rangle=a_1(tg)$, which is
  what Theorem thm:quant Step 1 uses; the cohomological pairing $\hat\delta_!$ is Chapter 14's and Chapter 20's, where the same
  one-line argument (idempotents of a commutative algebra of self-adjoint operators are self-adjoint) applies.
* **Point 46** (the paper's congruences in the Example of Section 3 hold at every $n$ by Sturm's bound). Chapter 12 (its 11.5) proves
  them; 8.4(iii) explains the division of labour between Sturm and the Hecke recursion; 9.2 and 11.4 identify $f_{\text{11a}}\otimes\chi_{-11}$ with
  121d.
* **B10** (the Manin constant in the Zagier-Watkins formula). Not used here; 10.3 uses only the unnormalised Petersson product of
  Chapter 12 (C5), consistent with B10.
* **B11** ($S_2(\Gamma_0(N);\Z)$ is a lattice: Chapter 12 versus Chapter 13). Followed: Chapter 13 cites Chapter 12's 11.2 and 11.4 and proves
  the perfect pairing (4.1) from them.
* Also touched: **point 16** (Theorem thm:twist data paragraph: strict inequality in case (a) too): 11.3 gives the forms behind the
  pairs 539c1/77c1 and 121d1/11a1; **points 15 and B8** (twist pairs by class): 9.2's table names classes and the curves PARI returns;
  **point 39** is Chapter 14's and is not used.

### 6.5 References

`refs.bib` already contains: DiamondShurman, Shimura71, Shimura76, Miyake, Koblitz, SerreCourse, Stein, AtkinLehner70, AtkinLi78,
Ribet83, AU96, ARS12, DDT, DFG04, Zagier85, ColemanEdixhoven, Carayol86, Sturm87, PARI, PARIusers, Cremona97, ecdata, Deligne. Not in
`refs.bib` and not in any `bib/chNN.bib` (all chapter bib files except `bib/chA.bib` are empty; checked): **`Li75`** (W.-C. W. Li,
*Newforms and functional equations*, Math. Ann. 212 (1975), 285-315) and **`Rankin39`** (R. A. Rankin, *Contributions to the theory of
Ramanujan's function $\tau(n)$ and similar arithmetical functions. I. The zeros of the function $\sum_{n=1}^\infty\tau(n)/n^s$ on the line
$\operatorname{Re}s=13/2$. II. The order of the Fourier coefficients of integral modular forms*, Proc. Cambridge Philos. Soc. 35 (1939), 351-356 and
357-372). Both are needed by more than one chapter (Li75 by Chapters 13 and 15 for newform theory with character and the levels of
twists; Rankin39 by Chapters 13 and 19 for Rankin-Selberg), so by decision B14 they go into `refs.bib`, not into `bib/ch13.bib`. Every
bibliographic detail above was recalled, not re-verified; check before adding. Theorem numbers to verify are listed in 6.2.

### 6.6 Verification log (computations done for this outline)

Python 3 with sympy and PARI/GP 2.17 through `cypari2`; scripts in the session scratchpad (`ch13/c1.py` to `c11.py`); Cremona `ecdata` files from
`/tmp/ch09/data` (`allcurves`, `degphi`, `galrep`).
* `c1.py`: multiplicativity and the recursion for 11a1 up to $n=5000$ (and $a_{11^r}=1$); the formula $a_m(T_nf)=\sum d\,a_{mn/d^2}$ consistent with
  $T_nf=a_nf$ for $m,n<60$; $\dim S_2(N)$, $\dim S_2^{\mathrm{new}}(N)$ and the formula of 6.5 for the twelve levels of the table; Sturm bounds
  ($2,6,8,12,16,24,24,22,66,112,336,264$).
* `c2.py`: matrices of $U_p$ on $V_{f_{11},2,e}$, $e=1,2,3$, and $V_{f_{11},11,e}$, $e=1,2$, with characteristic polynomials and Jordan forms (sympy); the depleted
  form $f_{11}^{\{2\}}$ to $n=4000$; $U_2$ on all of $S_2(22)$, $S_2(44)$, $S_2(88)$ (characteristic and minimal polynomials, PARI `mfheckemat`).
* `c3.py`: integral basis of $S_2(N;\Z)$ by saturating the $q$-expansion lattice (`matrixqz`), the matrices of $T_n$, $n\le\max(B,41)$, in that basis
  (all integral), $\operatorname{rank}_\Z\T$, the determinant of the pairing ($\pm1$), the index of $\Z T_1+\cdots+\Z T_d$, and congruence numbers $r_f$ by the
  index of $\Z f\oplus(f^\perp\cap S_2(N;\Z))$, $f^\perp$ computed as $\sum_p\operatorname{im}(T_p-a_p)$ over $p\le40$, $p\nmid N$ (rank $d-1$ checked), at levels $11$, $33$, $37$,
  $44$, $77$, $88$, $99$, $121$, $539$; compared with `degphi`.
* `c4.py`: Petersson Gram matrix at level $22$ (`mfpetersson` on `mfsymbol`s), the adjoint of $U_2$, and $w_{22}$ from `mfatkininit`.
* `c5.py`: conductors of the twists of 9.2 (`elltwist`, `ellglobalred`, minimal models matched to `allcurves`); $a_p(11\text{a}\otimes\chi_{-11})=\chi_{-11}(p)a_p(11\text{a})$
  for $p<3000$.
* `c6.py`: Rankin-Selberg residues from the Euler factors of `lfunsympow` against $48\pi\langle f,f\rangle/\mu(N)$ for 11a1, 37a1, 20a1, 121a1, 99a1 (30
  digits), and $\langle f,f\rangle=NL(\Sym f,2)/(8\pi^3)$ for 11a1, 37a1.
* `c7.py`: the depleted forms $(77\text{c})^{\{7\}}$, $(11\text{a})^{\{7\}}$ at level $539$, $\iota$ of them equal to $f_{539\text{c}}$, $f_{539\text{d}}$ (to $n=3000$), and their Hecke
  congruence modules ($288$, $504$), computed as the index of $\Z g\oplus(g^c\cap S_2(539;\Z))$ with $g^c$ the image of $t-\pi(t)$ for a random $t\in\T$ for
  which $\pi(t)$ is a simple root of the characteristic polynomial.
* `c8.py`: Theorem thm:quant at $q=3$ (Part 7, N2): all optimal curves of conductor below $10{,}000$ with type $\mathrm{I}_0^*$ at $3$, $\ell\in\{5,7,11,13\}$,
  $\ell\nmid N$, surjective mod $\ell$ image (`galrep`), $e_\ell>0$: $388$ cases, no case with $v_\ell(\deg\varphi_E)<e_\ell$.
* `c11.py`: PARI's $P_3(3^{-2})$ (from `lfunsympow`, `lfuneuler`) against the twist formulas $L_3(A_f,1)^{-1}=\frac23\cdot\frac{16-a_3(E')^2}9$ (type $\mathrm{I}_0^*$)
  and $\frac89$ (type $\mathrm{I}_n^*$) for all $1{,}100$ optimal curves of conductor below $3{,}000$ with one of these types at $3$: no mismatch (Part 7, N2).
* `c9.py`: $\T_{23}=\Z[T_2]$ with $T_2^2+T_2-1=0$ (consistency with Chapter 3, its 10.4(a)).
* `c10.py`: the Gram matrix of $f_{11}(z),f_{11}(2z),f_{11}(4z)$ at level $44$ and $\langle f_{11}^{\{2\}},f_{11}-\beta f_{11}(2z)\rangle=\frac5{12}\langle f_{11},f_{11}\rangle$.
* By hand: the coset decompositions of 2.2; $W_N\operatorname{diag}(1,p)W_N^{-1}=\operatorname{diag}(p,1)$; the trace identity of 5.3(iii); the intertwining of 9.1(iv); the
  conjugation identity of 9.1(ii); $\iota(f)=g^S$ and the inclusion of 9.3(iii).
* Not checked: theorem numbers in the references (6.2); the hypotheses of AtkinLi78 Theorem 3.1 in print.

## 7. Points for important_notes.md

New points in the area of this chapter (Hecke operators, the Hecke algebra and its pairing, newforms and oldforms, $U_p$ on oldforms,
depletion, twists, $L$-functions of newforms), not among points 1 to 53 and B1 to B16 already recorded. Points 16, 19, 20, 21, 30, 35,
36, 46, B10 and B11 are handled in Part 6.4 and not repeated.

**Errors in the paper in this area: none found.** Checked in particular: the $q$-expansion formulas and eigenvalues used in Lemma
lem:old (every case, 7.1); "$a_p=0$ for $p^2\mid M$" and "$a_p=\pm1$ for $p\,\|\,M$" (6.4); the $\T$-stability of $f^\perp$ in Lemma lem:crit (5.3, 5.4);
the perfect pairing at nine levels (4.1); Lemma lem:twist (iii) on twelve twists, including the failure of newness when $q^2\mid M$, which
the lemma excludes (9.2); Section 4.1's $f^\Sigma$ and $M^\Sigma$ (7.4); the claims of Theorem thm:quant Step 1 (multiplicity one of the
eigenvalue $0$, units, the transport along $\iota$, the idempotent projection: 7.1, 7.2, 8.3, 9.3), with the Hecke congruence modules
computed at level $539$; the claims of the proof of Theorem thm:twist (9.1, 9.3, 6.3); the 99A1 congruence number $12$ (11.2).

* **N1. Theorem thm:quant, Step 1: the inequality is an equality (optional strengthening, not an error).**
  Location: proof of Theorem thm:quant, Step 1, ending "$v_\ell(r_E)\ge v_\ell(\eta^{\mathrm{Hecke}}(g^S))$", and Remark (2) after the proof.
  Observation: the transport also runs the other way, with no projection. Twisting $f$ gives $\iota(f)=\sum\chi_S(n)^2a_n(g)q^n=g^S$; and $\iota$ maps
  $f^\perp=\bigoplus_{h\ne f}V_h$ (newforms $h$ of level dividing $N$, 6.2(iv)) into $\bigoplus_{h'\ne g}V_{h'}$, because $\iota(V_h)$ lies in the anemic eigenspace of the system
  $\chi_S(p)a_p(h)$ (9.1(iv), $\operatorname{lcm}(N,D^2)=N$), which is that of $g$ only if $h$ has the system of $f$, that is, $h=f$ (strong multiplicity one).
  $\bigoplus_{h'\ne g}V_{h'}$ lies in the $\T$-stable complement of the line $\C g^S$. So a congruence $f\equiv h\pmod r$ with $h\in f^\perp\cap S_2(N;\Z)$ gives
  $g^S\equiv\iota(h)\pmod r$ with $\iota(h)$ integral in the complement, and by the argument of Lemma lem:crit for $g^S$ (its generalised eigenspace
  is a line), $r_E$ divides the generator of $\eta^{\mathrm{Hecke}}(g^S)$. With Step 1 (which needs $\ell\notin S$ for the units),
  $$v_\ell(r_E)=v_\ell\bigl(\eta^{\mathrm{Hecke}}(g^S)\bigr)\quad\text{for every prime }\ell\notin S,$$
  so in the chain of Theorem thm:quant only Step 2 (freeness of $H^1(X_0(N),\Z_\ell)_{\mathfrak m}$ at the maximal ideal of $g^S$) and Step 4 (multiplicity
  one at level $N_S$) can be strict. Numerical check: at level $539$ the Hecke congruence modules of $(77\text{c})^{\{7\}}$ and $(11\text{a})^{\{7\}}$
  have orders $288$ and $504$, exactly $r(539\text{c})$ and $r(539\text{d})$ (even at $\ell=2$ and at $\ell=7=q$). Fix (optional): add after Step 1
  "Conversely $\iota(f)=g^S$ and $\iota(f^\perp)$ lies in the $\T$-stable complement of $g^S$, so Step 1 is an equality", and sharpen Remark (2)
  accordingly. Confidence: high for the argument (it uses only 6.2, 6.3, 9.1); the numerics were computed with the lattice method of
  11.2 (Part 6.6, `c7.py`).

* **N2. Theorem thm:quant: the restriction to primes $q\ge5$ is not needed (optional strengthening).**
  Location: statement of Theorem thm:quant ("let $S$ be the set of primes $q\ge5$ at which $E$ has type $\mathrm{I}_0^*$ or $\mathrm{I}_n^*$") and Step 3
  ("the values are those of Lemma lem:euler", a lemma stated for $q\ge5$).
  Observation: no step uses $q\ge5$. Lemma lem:twist (ii) gives the exchanges $\mathrm{I}_n\leftrightarrow\mathrm{I}_n^*$ and $\mathrm{I}_0\leftrightarrow\mathrm{I}_0^*$ for every odd $q$; Theorem
  thm:twist allows any odd primes; and at an $\mathrm{I}_n^*$ or $\mathrm{I}_0^*$ prime the true factor $L_q(A_f,s)$ is that of the twist $E_S$, good or
  multiplicative at $q$ (the adjoint is unchanged by the twist), so Step 3 holds at $q=3$ with the same formulas: $e_\ell(E,3)=v_\ell(8)=0$
  for $\mathrm{I}_n^*$ and $e_\ell(E,3)=v_\ell(2)+v_\ell(16-a_3(E')^2)$ for $\mathrm{I}_0^*$, which is positive for $\ell=5$ ($a_3(E')=\pm1$) and $\ell=7$ ($a_3(E')=\pm3$). ($\ell\ne3$
  automatically, as $\ell\nmid N$.) Checks: PARI's $P_3(3^{-2})$ agrees with these formulas for all $1{,}100$ optimal curves of conductor below
  $3{,}000$ with type $\mathrm{I}_0^*$ or $\mathrm{I}_n^*$ at $3$; and $v_\ell(\deg\varphi_E)\ge e_\ell(E,3)$ holds in all $388$ cases with type $\mathrm{I}_0^*$ at $3$, $\ell\in\{5,7,11,13\}$,
  $\ell\nmid N$, surjective mod $\ell$ image and $e_\ell>0$, below conductor $10{,}000$ (for example 333d1 and 477a1 at $\ell=7$, 234e1 and 333a1 at
  $\ell=5$). Fix (optional): "the set of odd primes $q$ at which ...", and say in Step 3 that the values at $q=3$ follow from the twist. The
  same remark applies to Lemma lem:euler's rows $\mathrm{I}_n^*$ and $\mathrm{I}_0^*$, which hold for every odd $q\ne\ell$. Confidence: high for the
  argument, which only uses that the adjoint representation is twist-invariant; this is for the Chapter 20 and Chapter 21 writers to
  adopt or not (Chapter 21's pitfall W8(d) currently says "$S$ contains only primes $q\ge5$", which is right as a reading of the paper).

* **N3. Lemma lem:crit and Theorem thm:quant Step 1: "the proof of Lemma lem:crit, carried out" for a non-newform (expository).**
  Location: Theorem thm:quant Step 1, "Now the proof of Lemma lem:crit, carried out over $\Z_\ell$ with the pairing ..., shows that
  $\ell^{v_\ell(\eta^{\mathrm{Hecke}}(g^S))}$ is the largest power ... with $h$ ... in the $\T$-stable complement of the $g^S$-line".
  Problem: Lemma lem:crit is stated for the newform $f$ with the Petersson complement $f^\perp$; for $g^S$ the Petersson complement is
  not $\T$-stable (8.2(iii): at level $44$, $\langle f_{11}^{\{2\}},f_{11}-\beta f_{11}(2z)\rangle\ne0$), and the proof must be run with the $\T$-stable complement,
  using only that the generalised eigenspace of the eigencharacter is a line. The paper does say "$\T$-stable complement" here, so
  this is a matter of making the reference precise. Fix (optional): state Lemma lem:crit for any eigencharacter $\pi\colon\T\to\Z$ whose
  generalised eigenspace is a line, with the $\T$-stable complement, and note that for a newform it is the Petersson complement.
  Confidence: high; importance low.

Book-internal inconsistencies and coordination notes found while preparing this outline:

* **BI1 (B8, addition).** The twist of 20a1 by $\chi_{-7}$ lies in the class 980g (980g2 by PARI's minimal model), not 980i. The paper's
  congruence $a_p(980\text{i1})\equiv\chi_{-7}(p)a_p(20\text{a1})\pmod5$ is therefore between two different newforms of level $980$; Chapter 12's 11.5(c)
  states it correctly ("$f_{980\text{i}}\equiv f_{20\text{a}}\otimes\chi_{-7}$"), and no outline claims the contrary, but writers should not say "980i is the twist of
  20a". The twist of 980i1 by $-7$ is 140b1 (Chapter 9, its 10.4; Chapter 21).
* **BI2 (PLAN.md, Chapter 13 scope).** "$T_{p^{k+1}}=T_pT_{p^k}-p^{k-1}T_{p^{k-1}}$" uses $k$ both as the exponent and as the weight. The outline
  writes $T_{p^{r+1}}=T_pT_{p^r}-p^{k-1}T_{p^{r-1}}$ with $k$ the weight ($p^{k-1}=p$ in weight $2$). Notation only.
* **BI3 (division of labour for $r_E$ and Lemma lem:crit).** PLAN.md places the proof of Lemma lem:crit in Chapter 15 ("prove it here in
  full"), mentions it for Chapter 14 ("proved in full here or in Chapter 20") and restates it in Chapter 20. This outline defines $\eta(\phi)$
  and $r_f$ (4.3) and supplies every Hecke-theoretic ingredient, but proves neither the identity $r_f\Z=\eta(\phi_f)$ nor the lemma; Chapter
  14's outline should cite Chapter 15 for the proof and not prove it a third time.
* Consistency checks that passed: Chapter 3's 10.7(v) (the shift operator: characteristic polynomial $X^{e-1}(X^2-aX+p)$, Jordan block of size
  $e-1$) and its Exercise 14 (level $88$, $a_2(f_{11})=-2$) agree with 7.1 and 11.1; Chapter 3's 10.4(a) ($\T_{23}=\Z[(1+\sqrt5)/2]$) agrees with
  `c9.py`; Chapter 12's 10.5(a) ($U_p^\dagger=w_NU_pw_N$), 12.4(b) (the matrix of $w_{22}$) and 11.5 (the congruences) agree with 5.3 and 9.2;
  Chapter 21's A4.14 and A4.15 (the twist pairs and the checks of Theorem thm:quant with Cremona's degrees) agree with 11.3, where
  the congruence numbers were computed directly; Chapter 6's 7.1 ("$K_f$ totally real" for newforms) agrees with 3.3.
