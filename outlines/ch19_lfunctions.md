# Chapter 19: L-functions: Euler products, local factors, the adjoint and the symmetric square (`ch:lfunctions`, `chapters/ch19_lfunctions.tex`)

Stage 1 line-up. Part V (Cohomology, Selmer groups and $L$-functions), after Chapter 18 (Bloch-Kato Selmer groups, Tamagawa
factors, the Tamagawa number conjecture) and before Chapter 20 (congruence ideals and the theorem of Diamond, Flach and Guo).
Target length 1,975 lines of LaTeX (card excluded; see Part 3), inside the 1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the Chapter 2 to 15
outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference (book and chapter or
section; a theorem number only where sure, otherwise marked "(verify)" or given by section); the paper's use by its `\label`
names, or "background". Every number quoted below (Euler factors, $P_q(X)$, valuations, Petersson norms, $L$-values, modular
degrees, conductors of $L(\Sym f,s)$, the outputs of `rule(E, l)`) was checked by Python scripts `t0.py` to `t8.py` in the
session scratchpad (`.../scratchpad/ch19/`), using PARI/GP 2.17.2 through `cypari2` and Cremona's `ecdata` files for conductors
below 10,000 in `/tmp/ch09/data` (verification log, Part 6.6).

## 1. Purpose and global conventions

### 1.1 What this chapter is for

The paper's title names the object of this chapter: the local factors of the adjoint $L$-function. The chapter is built around
seven uses.

1. **Naive versus true adjoint $L$-function** (Section 1: "The $L$-function that appears there is the *naive* one: the Euler
   product of $\sum a_n(f)^2n^{-s}$, which has the true local factor at the primes of good or multiplicative reduction and the
   trivial factor at the additive primes"). The chapter defines both, proves the exact relation of the naive one with the
   Rankin series $\sum a_n^2n^{-s}$ and with Shimura's series $\sum a_{n^2}n^{-s}$ (important_notes.md point 30), and explains why
   the naive factor is $1$ exactly where $\delta_p=0$.
2. **The local terms of Section 1.1** ("$\delta_p=\dim V^{I_p}$ ...; $L_p(A_f,s)=\det(1-\Frob_p\,p^{-s}\mid A_f^{I_p})^{-1}$ is the true local
   factor, and the naive factor is $L_p^{\nv}(A_f,s)=L_p(A_f,s)$ if $\delta_p>0$ and $1$ if $\delta_p=0$. In the normalisation of the
   symmetric square, $L_p(\Sym f,s)=L_p(A_f,s-1)$, and PARI's `lfunsympow(E,2)` returns these factors at every prime, including
   $2$ and $3$"). The chapter fixes the Frobenius (geometric, point 11), proves the shift by one, and states what PARI returns.
3. **Definition def:terms, the table of Section 1 and Lemma lem:euler in full** (the omitted factor by Kodaira type at a tame
   prime $q\ge5$). The chapter assembles the inertia images of Chapter 11 and the local factors of Chapter 7 into the table,
   adds the column $P_q(X)$, and proves the valuations.
4. **Remark rem:wild and Section sec:wild** (the primes $2$ and $3$, where "the Kodaira type does not determine $L_q(A_f,s)$,
   but PARI does"). The chapter proves a classification valid at every prime $q\ne\ell$ (new item 10.1): $P_q$ is one of $1$,
   $1-X$, $1\mp qX$, or the type $\mathrm I_0^*$ cubic of a twist of good reduction, and it records which sentences of the remark
   are theorems (point 43), false (point 50) or approximate.
5. **Theorem thm:dfg14 and the paragraph after it** ("adding a good prime $p$ multiplies the ideal by
   $(1-\frac\alpha\beta p^{-1})(1-p^{-1})(1-\frac\beta\alpha p^{-1})$, Wiles's level-raising factor; adding a multiplicative prime multiplies it by
   $1-p^{-2}$"), the proof of Theorem thm:main (the cancellation of the naive factors) and Theorem thm:quant Step 3. The chapter
   computes every naive factor at $s=1$; the theorems themselves are Chapter 20's.
6. **Lemma lem:fpr, its $L$-part** ("$L_p(A_f,1)^{-1}=L_p(A_f(1),0)^{-1}$ is a nonzero rational number which is an $\ell$-adic integer,
   of valuation $e_\ell(E,p)$ at an additive prime and $v_\ell(1-p^{-2})$ at a multiplicative one") and the paragraph after Lemma
   lem:dfg21 ("$\det(1-\Frob_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}\ne0$"). The Fitting-ideal half is Chapter 18's.
7. **The Petersson norm** (Section 1: "Up to explicit factors $\degphi$ is $\langle f,f\rangle$ divided by the area of the period lattice
   of $E$ (Zagier, Watkins), and $\langle f,f\rangle$ is the special value $L(\Sym f,2)$ up to the local factors at the bad primes
   (Rankin, Shimura; see DFG04 Lemma 2.12); Flach's finiteness theorem for the symmetric square is the first place where the
   modular degree meets the Selmer group of $\Sym f$"). The chapter proves the exact formula
   $\langle f,f\rangle=\frac N{8\pi^3}L^{\nv}(\Sym f,2)$ for every level (new in this form for the book, item 8.3), deduces
   $\degphi=N\,L^{\nv}(\ad f,1)/(2\pi\operatorname{vol}\Lambda_E)$ and the unconditional identity
   $v_\ell(\degphi)=v_\ell(B_E)+\sum_{q\mid N}e_\ell(E,q)$ (item 8.4), which is the conceptual reason why the omitted factors appear in the
   paper's theorem.

It also covers the general theory that PLAN.md places here and that nothing earlier supplies: Dirichlet series and Euler
products, the Riemann zeta function, Dirichlet $L$-functions and Dedekind zeta functions of abelian fields, $L$-functions of
$\ell$-adic representations and of compatible systems, $L(E,s)$ with its functional equation, the analytic theory of
$L(\Sym f,s)$ (Shimura, Gelbart-Jacquet), critical values and Deligne's conjecture (one paragraph), Flach's theorem (statement),
the shape of the Bloch-Kato formula for the adjoint (one page, pointer to Chapter 18), and the mathematical content of the
appendix function `rule(E, l)` (the line-by-line reading is Chapter 22's).

It discharges the debts of earlier chapters: Chapter 2 (its 11.3 to 11.6 are "given the table of Section 1 as stated in
Chapters 19 and 21"; its 11.6(f) asks for the label of the $\mathrm I_0^*$ example: it is 539d1, item 12.1 here); Chapter 4 (its
7.5(iii): $L_p(\Sym f,s)=L_p(A_f,s-1)$, "the $L$-factor bookkeeping is Chapter 19's"); Chapter 6 (its 3.7: Euler factors with the
geometric Frobenius); Chapter 7 (its forward list: convention 8.2, the shapes table 9.4, the adjoint computations 9.1 to 9.3,
the wild primes 9.5, "the symmetric square normalisation and PARI's $P_q$"); Chapter 9 ("Chapter 19 supplies analytic
continuation and the functional equation of $L(E,s)$ and the local factors via Weil-Deligne representations"); Chapter 10 ("the
Euler factors $L_q(A_f,s)$, $P_q(X)$, $e_\ell(E,q)$, Lemma lem:euler in full and the Euler factors at $2$ and $3$"); Chapter 11 (its
4.1, 4.4, 4.6, 8.4(iv): "the factors $L_q(A_f,s)$ and $e_\ell(E,q)$ are computed from it in Chapter 19"); Chapter 12 (its 10.5(b): "Chapter
19 states the exact formula"); Chapter 13 (its 10.1 to 10.3: "the exact relation with $L(\Sym f,2)$ at bad primes is Chapter 19's");
Chapter 14 (its 7.5: the Rankin-Shimura formula with the bad factors); Chapter 15 (its 3.7: "the comparison is Chapter 19's").

**The physics reader** meets three familiar objects, one sentence each: the Mellin transform that turns a theta series or a
$q$-expansion into a Dirichlet series (RHB, integral transforms; item 2.3); Poisson summation for the Gaussian, which gives the
functional equation of $\zeta$ (RHB, Fourier transforms; item 3.1); and the Euler product as the partition function of a gas of
non-interacting "primons", one bosonic mode per prime (one sentence in Section 2, as an aside only).

### 1.2 Global conventions fixed in this chapter

* **C1 (objects).** $E/\Q$ is given by a global minimal model, conductor $N$; $f=f_E\in S_2(\Gamma_0(N))$ its newform (Chapter 14);
  $\ell$ a prime; $T=T_\ell E$, $V=T\otimes\Q_\ell$, $\rho=\rho_{E,\ell}$; $A=\ad T$, $A_f=\ad V$ (trace zero; the paper's macro `\ad`);
  $\delta_p=\dim V^{I_p}$ for $p\ne\ell$ (for $p=\ell$ use $V_{\ell'}E$, $\ell'\ne p$; Part 7, N4). Wherever a
  statement holds for every newform of weight $2$ with trivial character and rational coefficients, say so; the paper needs
  only $f=f_E$.
* **C2 (Frobenius).** As Chapter 7 (L3) and Chapter 11 (C3): $\Frob_p$ is an **arithmetic** Frobenius, $\Phi_p=\Frob_p^{-1}$ the
  **geometric** one. Group theory uses $\Frob_p$ ($\Frob\,g\,\Frob^{-1}=g^p$ on tame inertia); $L$-factors use $\Phi_p$. On $V_\ell E$ at a
  good prime the arithmetic Frobenius has characteristic polynomial $X^2-a_pX+p$, roots $\alpha,\beta$; the geometric one has
  $\alpha^{-1},\beta^{-1}$; on $V_\ell E^\vee=H^1$ the geometric one has $\alpha,\beta$; on $\ad V$ both give $\alpha/\beta,1,\beta/\alpha$ (important_notes.md
  B1, B9). In the paper the Frobenius of Section 1.1, of Lemma lem:euler, of Lemma lem:fpr and of the paragraph after Lemma
  lem:dfg21 is the geometric one; that of Lemma lem:tamfactor is the arithmetic one (point 11).
* **C3 (local factor).** For $p\ne\ell$ and a continuous representation $M$ of $G_{\Q_p}$ on a finite-dimensional $\Q_\ell$-space:
  $L_p(M,s)=\det(1-\Phi_p\,p^{-s}\mid M^{I_p})^{-1}$ (Chapter 7, 8.2). Consequences used throughout: $L_p(M(n),s)=L_p(M,s+n)$,
  $L_p(\Q_\ell(1),s)=(1-p^{-1-s})^{-1}$, $L_p(V_\ell E^\vee,s)=L_p(E,s)$, $L_p(V_\ell E,s)=L_p(E,s+1)$.
* **C4 (the four normalisations; display as one table, item 7.4).** $L(\ad f,s)=L(A_f,s)=\prod_pL_p(A_f,s)$: the paper's and
  DFG04's adjoint, value used at $s=1$, functional equation $s\leftrightarrow1-s$. $L(\Sym f,s)=\prod_pL_p(\Sym^2V^\vee,s)=L(A_f,s-1)$: the
  paper's symmetric square and PARI's `lfunsympow(E,2)`, value used at $s=2$, functional equation $s\leftrightarrow3-s$. $L^{\nv}$: the naive
  versions (C6). $D(f,s)=\sum a_n(f)^2n^{-s}$: the Rankin series. Never write "$L(\Sym f,s)$" for the Rankin series.
* **C5 ($P_q$).** For every prime $q$ (good or bad), $P_q(X)\in\Z[X]$ is the polynomial with $L_q(\Sym f,s)=P_q(q^{-s})^{-1}$; so
  $P_q(q^{-2})=L_q(A_f,1)^{-1}$. PARI's `lfuneuler(lfunsympow(E,2),q)` returns the rational function $1/P_q(x)$, $x=q^{-s}$.
* **C6 (naive factor).** For $p\nmid N$: $L_p^{\nv}=L_p$. For $p\mid N$: $L_p^{\nv}(A_f,s)=L_p(A_f,s)$ if $\delta_p>0$, $=1$ if $\delta_p=0$ (the paper, Section
  1.1, after DFG04 1.7.2); equivalently $L_p^{\nv}(A_f,s)^{-1}=1-a_p(f)^2p^{-1-s}$ for $p\mid N$ (item 8.1). $L^{\nv}(\ad f,s)=\prod_pL_p^{\nv}(A_f,s)$,
  $L^{\nv}(\Sym f,s)=L^{\nv}(\ad f,s-1)$.
* **C7 (characters).** $\chi_{-3}$, $\chi_{-4}$ are the quadratic characters of $\Q(\sqrt{-3})$, $\Q(i)$; for an odd prime $q$, $q^*=(-1)^{(q-1)/2}q$
  and $\chi_{q^*}$ is the quadratic character of conductor $q$ (the paper's $\chi_q$; Chapter 2 and Chapter 13 write $\chi_{q^*}$ to avoid
  the clash with the cyclotomic $\chi_\ell$, point 32). Twists: $E^{(d)}=E\otimes\chi_d$.
* **C8 (Kodaira data).** Kodaira symbols as in PLAN.md 7.1; PARI's codes (Chapter 10): $n+4$ for $\mathrm I_n$ and $-(n+4)$ for
  $\mathrm I_n^*$ **for $n\ge1$** ($\mathrm I_0$ is $1$, $\mathrm I_0^*$ is $-1$; point 52), $\pm2,\pm3,\pm4$ for $\mathrm{II}/\mathrm{II}^*$, $\mathrm{III}/\mathrm{III}^*$,
  $\mathrm{IV}/\mathrm{IV}^*$.
* **C9 (Petersson product).** Unnormalised, as Chapter 12 (C5): $\langle f,g\rangle=\int_{\Gamma_0(N)\backslash\mathfrak H}f\bar g\,y^2\,d\mu=\int f\bar g\,dx\,dy$ for weight $2$;
  PARI's `mfpetersson` is this divided by $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]=N\prod_{p\mid N}(1+p^{-1})$. Period lattice $\Lambda_E$ of the
  Neron differential of the minimal model, $\operatorname{vol}(\Lambda_E)$ its covolume (PARI: `E.area`).
* **C10 (typography).** PLAN.md 7.2: plain hyphens in "Rankin-Selberg", "Gelbart-Jacquet", "Bloch-Kato", "Weil-Deligne",
  "Coates-Schmidt"; ranges "1 to 8"; labels `...:lfunctions:...`; no new macros (write `\operatorname{Sym}^2` where the paper's
  `\Sym` would be ambiguous, `\operatorname{vol}`, `\operatorname{Res}`).

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 2. Dirichlet series and Euler products

**2.1 `def:lfunctions:dirichlet-series`** (definition and proposition; P). A Dirichlet series is $D(s)=\sum_{n\ge1}a_nn^{-s}$ with $a_n\in\C$,
$s=\sigma+it$. (i) If $\sum|a_n|n^{-\sigma_0}<\infty$ then $D$ converges absolutely and uniformly on $\operatorname{Re}s\ge\sigma_0$ and is holomorphic on
$\operatorname{Re}s>\sigma_0$ (Weierstrass M-test; uniform limits of holomorphic functions, Appendix A). (ii) The abscissa of absolute
convergence is $\sigma_a=\inf\{\sigma_0\}$; if $a_n=O(n^c)$ then $\sigma_a\le c+1$; if $a_n=O(n^{c+\varepsilon})$ for every $\varepsilon>0$, likewise. (iii)
Uniqueness: if $D(s)=0$ for all real $s$ large enough then every $a_n=0$ (multiply by $m^s$ inductively). (iv) Products of
Dirichlet series are Dirichlet series with the convolution $\sum_{de=n}a_db_e$. Reference: Davenport, Chapter 1 and Chapter 8 (cite
the chapters; proposed key `Davenport00`, Part 6.5); SerreCourse VI.2 (cite the section). Paper: background.

**2.2 `prop:lfunctions:euler-product`** (proposition; P). Let $a\colon\N\to\C$ be multiplicative ($a_{mn}=a_ma_n$ for coprime $m,n$, $a_1=1$) with
$\sum|a_n|n^{-\sigma}<\infty$. Then for $\operatorname{Re}s\ge\sigma$: $\sum_na_nn^{-s}=\prod_p\bigl(\sum_{k\ge0}a_{p^k}p^{-ks}\bigr)$, the product converging absolutely; it
is nonzero at $s$ if every factor is nonzero there. If moreover $\sum_ka_{p^k}X^k=P_p(X)^{-1}$ with $P_p\in\C[X]$, $P_p(0)=1$, $\deg P_p\le d$ for
all $p$, the series has an Euler product of degree $d$. Examples: $\zeta$ ($d=1$), $L(s,\chi)$ ($d=1$), $L(f,s)$ ($d=2$, Chapter 13, its
10.1), $L(\ad f,s)$ and $L(\Sym f,s)$ ($d=3$, Section 6), $\zeta(s)\zeta(s-1)=\sum\sigma(n)n^{-s}$ (exercise). Physics aside: $\zeta(s)=\prod_p(1-p^{-s})^{-1}$
is the partition function of free bosonic "primons" at inverse temperature $s$ (one sentence). Reference: Davenport, Chapter 1
(cite the chapter). Paper: Section 1 ("the Euler product of $\sum a_n(f)^2n^{-s}$"), Definition def:terms ($P_q$).

**2.3 `lem:lfunctions:mellin`** (lemma; P for (i), (iii), S for (ii)). (i) $\Gamma(s)=\int_0^\infty e^{-y}y^{s-1}dy$ ($\operatorname{Re}s>0$) satisfies
$\Gamma(s+1)=s\Gamma(s)$, $\Gamma(1/2)=\sqrt\pi$, and extends meromorphically to $\C$ with simple poles at $0,-1,-2,\dots$ and no zeros. Put
$\Gamma_\R(s)=\pi^{-s/2}\Gamma(s/2)$, $\Gamma_\C(s)=2(2\pi)^{-s}\Gamma(s)$; (ii) duplication: $\Gamma_\R(s)\Gamma_\R(s+1)=\Gamma_\C(s)$ (Legendre; S). (iii) Mellin: if
$a_n=O(n^c)$ and $F(y)=\sum_{n\ge1}a_ne^{-2\pi ny}$ then $\int_0^\infty F(y)y^{s-1}dy=(2\pi)^{-s}\Gamma(s)\sum a_nn^{-s}$ for $\operatorname{Re}s>c+1$ (Fubini). Physics
aside: the Mellin transform is the Fourier transform on the multiplicative group $\R_{>0}$ (RHB, integral transforms). Reference:
SerreCourse VII.4 (cite the section); Davenport, Chapter 9. Paper: background (Chapter 13, its 10.2; the gamma factors of 7.2).

### Section 3. The Riemann zeta function, Dirichlet $L$-functions and Dedekind zeta functions

**3.1 `thm:lfunctions:zeta`** (theorem; P for (i) to (iii), S for (iv), R for (v)). (i) For $\operatorname{Re}s>1$,
$\zeta(s)=\sum n^{-s}=\prod_p(1-p^{-s})^{-1}\ne0$. (ii) $\zeta(s)-\frac1{s-1}$ extends holomorphically to $\operatorname{Re}s>0$ (compare with $\int_1^\infty x^{-s}dx$
by partial summation); so $\zeta$ has a simple pole at $s=1$ with residue $1$. (iii) $\zeta(2)=\pi^2/6$ (Parseval for the Fourier series
of $x$ on $(-\pi,\pi)$, RHB). (iv) (Riemann) $\xi(s)=\Gamma_\R(s)\zeta(s)$ extends meromorphically to $\C$ with simple poles at $s=0,1$ only, and
$\xi(s)=\xi(1-s)$. Sketch: $\theta(y)=\sum_{n\in\Z}e^{-\pi n^2y}$ satisfies $\theta(1/y)=\sqrt y\,\theta(y)$ (Poisson summation; the Gaussian is its own
Fourier transform, RHB); $\xi(s)=\frac12\int_0^\infty(\theta(y)-1)y^{s/2-1}dy$; split at $y=1$ and substitute $y\mapsto1/y$. (v) $\zeta(1+it)\ne0$ for real
$t\ne0$ (Hadamard, de la Vallee Poussin; R). Reference: SerreCourse VI.3 and VII (cite sections); Davenport, Chapters 8, 13;
Washington, Chapter 4. Paper: background; $\zeta(2)$ and the residue at $1$ are used in 8.3.

**3.2 `def:lfunctions:partial-zeta`** (definition and proposition; P). For an integer $N\ge1$, $\zeta^{(N)}(s)=\zeta(s)\prod_{p\mid N}(1-p^{-s})$ (Euler
factors at $p\mid N$ removed). Then $\zeta^{(N)}(s-1)$ has a simple pole at $s=2$ with residue $\prod_{p\mid N}(1-p^{-1})$, and
$\zeta^{(N)}(2)=\frac{\pi^2}6\prod_{p\mid N}(1-p^{-2})$; hence $\operatorname{Res}_{s=2}\zeta^{(N)}(s-1)/\zeta^{(N)}(2s-2)=\frac6{\pi^2}\prod_{p\mid N}(1+p^{-1})^{-1}=\frac{6N}{\pi^2\mu(N)}$
with $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]$ (Chapter 12). Paper: Section 1 (through point 30 and 8.2, 8.3).

**3.3 `thm:lfunctions:dirichlet-L`** (definition and theorem; P for (i), (ii), (iv)(a); S for (iii); R for (iv)(b), (v)). Let $\chi$ be a
Dirichlet character modulo $m$ (Chapter 2). (i) $L(s,\chi)=\sum\chi(n)n^{-s}=\prod_p(1-\chi(p)p^{-s})^{-1}$ for $\operatorname{Re}s>1$. (ii) If $\chi\ne1$ the partial
sums of $\chi(n)$ are bounded, so $L(s,\chi)$ converges (conditionally) and is holomorphic on $\operatorname{Re}s>0$. (iii) If $\chi$ is primitive of
conductor $m>1$ and $\chi(-1)=(-1)^a$, $a\in\{0,1\}$, then $\Lambda(s,\chi)=(m/\pi)^{(s+a)/2}\Gamma(\frac{s+a}2)L(s,\chi)$ is entire and
$\Lambda(s,\chi)=W(\chi)\Lambda(1-s,\bar\chi)$ with $W(\chi)=\tau(\chi)/(i^a\sqrt m)$, $|W(\chi)|=1$, $\tau(\chi)$ the Gauss sum (Chapter 2); for real $\chi$,
$W(\chi)=1$ (Gauss's determination of the sign of the quadratic Gauss sum; stated). Sketch: the theta series $\sum\chi(n)n^ae^{-\pi n^2y/m}$
and Poisson summation twisted by $\chi$. (iv) (a) $L(1,\chi_{-4})=1-\frac13+\frac15-\dots=\frac\pi4$ (Leibniz) and $L(1,\chi_{-3})=\frac\pi{3\sqrt3}$ (P, by
integrating a geometric series); (b) $L(1,\chi)\ne0$ for every $\chi\ne1$ (R; for quadratic $\chi$ via 3.4 and the class number formula). (v)
Dirichlet's theorem on primes in arithmetic progressions (R). Reference: Davenport, Chapters 1, 4, 9; Washington, Chapter 4;
SerreCourse VI. Paper: background; $\chi_{-3}$, $\chi_{-4}$, $\chi_{q^*}$ of the table, of Lemma lem:twist and of Section 1.4 are these characters
(Chapter 2).

**3.4 `thm:lfunctions:dedekind`** (theorem; P for (i), R for (ii), (iii)). For a number field $K$, $\zeta_K(s)=\sum_{\mathfrak a}N\mathfrak a^{-s}=\prod_{\mathfrak P}(1-N\mathfrak P^{-s})^{-1}$
($\operatorname{Re}s>1$; Chapter 6). (i) For $K=\Q(\sqrt d)$ with discriminant $D_K$: $\zeta_K(s)=\zeta(s)L(s,\chi_{D_K})$; the Euler factor at $p$ is
$(1-p^{-s})^{-1}(1-\chi_{D_K}(p)p^{-s})^{-1}$ by the splitting law (Chapter 6). Examples: $\zeta_{\Q(i)}=\zeta\,L(s,\chi_{-4})$, $\zeta_{\Q(\sqrt{-3})}=\zeta\,L(s,\chi_{-3})$.
(ii) For $K/\Q$ abelian, $\zeta_K(s)=\prod_\chi L(s,\chi)$ over the primitive characters attached to the characters of $\Gal(K/\Q)$
(Washington, Theorem 4.3 (verify)). (iii) Artin formalism (R): Artin $L$-functions are additive and invariant under induction;
$\zeta_K=L(\operatorname{Ind}_{G_K}^{G_\Q}\mathbf1,s)$. Remark (one sentence): the factor $(1-\chi_{-3}(q)q^{-s})^{-1}$ of the paper's table is the Euler
factor at $q$ of $L(s,\chi_{-3})$, because the inertia-invariant line of $\ad V$ at a prime of type $\mathrm{II}$ to $\mathrm{IV}^*$ is, as a
$G_{\Q_q}$-module, the restriction of the global character $\chi_{-3}$ (item 9.3; likewise $\chi_{-4}$). Reference: Neukirch VII.5, VII.10
(cite sections); Washington, Chapter 4. Paper: background (the characters of the table).

### Section 4. $L$-functions of $\ell$-adic representations

**4.1 `def:lfunctions:local-factor`** (definition and proposition; recalled from Chapter 7 for $p\ne\ell$, P for (ii), (iii); R for
(iv)). (i) For $p\ne\ell$: $L_p(M,s)=\det(1-\Phi_pp^{-s}\mid M^{I_p})^{-1}$, which depends only on the Weil-Deligne representation of $M$ (Chapter
7, 8.1, 8.2). (ii) $L_p(M\oplus M',s)=L_p(M,s)L_p(M',s)$; $L_p(M(n),s)=L_p(M,s+n)$. (iii) Writing the factor with the arithmetic $\Frob_p$
inverts the eigenvalues; the two agree iff the eigenvalue multiset on $M^{I_p}$ is stable under $\lambda\mapsto\lambda^{-1}$ (true for $\ad V$ at a
good prime, false for $\ad V$ at a multiplicative prime and for $V_\ell E$; point 11). (iv) At $p=\ell$, for $M$ crystalline:
$L_\ell(M,s)=\det(1-\varphi\,\ell^{-s}\mid D_{\mathrm{cris}}(M))^{-1}$, in the normalisation in which $D_{\mathrm{cris}}(\Q_\ell(1))$ has $\varphi=\ell^{-1}$ (so that (ii) holds
at $\ell$ as well); for $E$ with good reduction at $\ell$, $\varphi$ on $D_{\mathrm{cris}}(V_\ell E^\vee)$ has characteristic polynomial $X^2-a_\ell X+\ell$
(Katz-Messing; R), so $L_\ell(V_\ell E^\vee,s)=L_\ell(E,s)$ and $L_\ell(A_f,s)$ is given by the good-prime formula 6.2. Reference: Chapter 7;
Fontaine (refs.bib `Fontaine`), Berger (cite the section); Tate79 Section 4 (proposed refs.bib key, Part 6.5). Paper: Section 1.1
(the definition of $L_p(A_f,s)$; the paper uses it only at $p\ne\ell$).

**4.2 `def:lfunctions:compatible-system`** (definition and theorem; R). A *weakly compatible system* is a family $(M_\ell)_\ell$ of
representations of $G_\Q$ on $\Q_\ell$-spaces (or over completions of a number field), unramified outside a finite set $S$, such that
for $p\notin S\cup\{\ell\}$ the characteristic polynomial of $\Phi_p$ on $M_\ell$ has rational coefficients independent of $\ell$. Its
$L$-function is $L(M,s)=\prod_pL_p(M_{\ell(p)},s)$ with $\ell(p)\ne p$, which is well defined when the (Frobenius-semisimplified)
Weil-Deligne representation at each bad $p$ is independent of $\ell\ne p$. Known in the cases needed: $V_\ell E$, $V_\ell E^\vee$ and
all tensor constructions of them ($\Sym^2$, $\ad$), by the Tate curve, Grothendieck's monodromy theorem and the Neron-Ogg-Shafarevich
criterion (Chapters 7, 10, 11; SerreTate68, R); $V_\lambda(f)$ for newforms (Carayol86; Chapter 15, its 3.4, R). In general it is a
conjecture. Paper: Section 1.1 ("the true local factor"; "PARI's `lfunsympow(E,2)` returns these factors at every prime").

**4.3 `prop:lfunctions:convergence`** (proposition; P given the Hasse bound, Chapter 9). Let $(M_\ell)$ be a weakly compatible system,
pure of weight $w$: for $p\notin S$ the eigenvalues of $\Phi_p$ have absolute value $p^{w/2}$ under every complex embedding, and for $p\in S$
the eigenvalues on $M^{I_p}$ have absolute value at most $p^{w/2}$. Then $L(M,s)$ converges absolutely and is nonzero for
$\operatorname{Re}s>1+w/2$ (compare with $\zeta(\sigma-w/2)^{\dim M}$). Examples: $V_\ell E^\vee$ ($w=1$): $L(E,s)$ on $\operatorname{Re}s>3/2$; $A_f$ ($w=0$; at bad
primes the eigenvalues are $q^{-1}$, $\pm1$ or $\alpha'/\beta'$ of modulus $\le1$, Section 9): $L(\ad f,s)$ on $\operatorname{Re}s>1$, hence $L(\Sym f,s)$ on $\operatorname{Re}s>2$;
$\Q_\ell(1)$ ($w=-2$): $\zeta(s+1)$. So $s=1$ for $L(\ad f,s)$ and $s=2$ for $L(\Sym f,s)$ lie on the edge of absolute convergence: the values
the paper uses are values of the analytic continuation (7.1), or of the Rankin integral (8.3). Paper: background.

**4.4 `ex:lfunctions:finite-inertia`** (worked example; P given Chapter 7, 9.2, 9.3). For $V$ two-dimensional with $\det V|_{I_q}=1$ and
$\rho(I_q)$ finite cyclic of order $m\in\{2,3,4,6\}$, $q\nmid m$: $L_q(V,s)=1$ in every case ($V^{I_q}=0$), while $L_q(\ad V,s)$ is the cubic factor of
the unramified twist ($m=2$) or $(1-\chi(q)q^{-s})^{-1}$ with $\chi=\chi_{-3}$ ($m=3,6$) or $\chi_{-4}$ ($m=4$). This is the PLAN item "the
$L$-function of a representation with finite image of inertia (the three Kodaira cases)"; the proof is Chapter 7's, the dictionary
to Kodaira types is item 9.3. Paper: Lemma lem:euler (background to it).

### Section 5. The $L$-function of an elliptic curve and of its newform

**5.1 `def:lfunctions:LE`** (definition and proposition; P given Chapters 9, 11). $L(E,s)=\prod_pL_p(E,s)$ with
$L_p(E,s)^{-1}=1-a_pp^{-s}+p^{1-2s}$ (good $p$), $1-a_pp^{-s}$ with $a_p=+1$ (split) or $-1$ (nonsplit) (multiplicative), $1$ (additive);
uniformly $a_p=p+1-\#\tilde E(\F_p)$ for every $p$, with $\tilde E$ the reduction of the minimal model, singular point included
(equivalently $a_p=p-\#\tilde E_{\mathrm{ns}}(\F_p)$ at bad $p$: $\tilde E_{\mathrm{ns}}$ is $\mathbb G_m$, its nonsplit form or $\mathbb G_a$; Chapter 10). (i) For every $p\ne\ell$, $L_p(E,s)=L_p(V_\ell E^\vee,s)=L_p(V_\ell E,s-1)$, and
$\delta_p=\deg L_p(E,s)^{-1}$ as a polynomial in $p^{-s}$ (Chapter 11, its 3.1, 3.2, 3.4, 4.1, 3.5). (ii) Absolute convergence on $\operatorname{Re}s>3/2$
(4.3). (iii) Isogenous curves have the same $L$-function. Reference: SilvermanAEC C.16 (verify); Cremona97 Chapter II. Paper:
Section 1.1 ($\delta_p$).

**5.2 `thm:lfunctions:LE-feq`** (theorem; R for modularity, S for the rest given Chapter 13, its 10.2). Let $E/\Q$ have conductor
$N$. (i) $L(E,s)=L(f_E,s)$ (modularity, Chapter 14). (ii) $\Lambda(E,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s)=N^{s/2}\int_0^\infty f_E(iy)y^{s-1}dy$ extends to an
entire function and $\Lambda(E,s)=w_E\Lambda(E,2-s)$ with $w_E=-\varepsilon_N(f_E)\in\{\pm1\}$, where $f_E|W_N=\varepsilon_N(f_E)f_E$ (Chapter 12, Chapter 13,
its 10.2). (iii) (R) $w_E=-\prod_{p\mid N}w_p$ with $w_p=-a_p$ at multiplicative $p$; the local root numbers at additive $p$ are given by
Rohrlich's formulas (Rohrlich94; not needed here). Examples: 11a1 ($w=+1$), 37a1 ($w=-1$) (Chapter 13). Reference: DiamondShurman
5.10 (cite the section); Rohrlich94 (proposed refs.bib key, B18). Paper: background (Section 1; Chapter 14, its 11.4 for $L(f,1)$).

### Section 6. The adjoint and the symmetric square: definitions and the good primes

**6.1 `def:lfunctions:ad-sym`** (definition and proposition; P given Chapter 4, its 7.5, and 4.1, 4.2). Let $f$ be a newform of weight $2$,
trivial character, rational coefficients (the paper: $f=f_E$), and $V=V_\ell E$ (or $V_\lambda(f)$). Define
$$L(\ad f,s)=L(A_f,s)=\prod_pL_p(A_f,s),\qquad L(\Sym f,s)=\prod_pL_p(\operatorname{Sym}^2V^\vee,s),$$
each local factor computed with any $\ell\ne p$ (4.2). Then: (i) $\operatorname{Sym}^2V^\vee\simeq A_f(-1)$ as $G_\Q$-representations, because
$\operatorname{Sym}^2W\simeq\ad W\otimes\det W$ for $\dim W=2$ (Chapter 4, 7.5) and $\ad V^\vee\simeq\ad V$, $\det V^\vee=\chi_\ell^{-1}$; hence
$L_p(\Sym f,s)=L_p(A_f,s-1)$ for every $p$ and $L(\Sym f,s)=L(\ad f,s-1)$ (C3). (ii) For every $p$, $P_p(X):=L_p(\Sym f,s)^{-1}|_{p^{-s}=X}$
lies in $\Z[X]$, $P_p(0)=1$, $\deg P_p=\dim A_f^{I_p}\in\{0,1,3\}$ (integrality from the explicit list 6.2, 9.2, 9.3, 10.1), and
$P_p(p^{-2})=L_p(A_f,1)^{-1}\in\Z[1/p]$. (iii) The eigenvalues of $\Phi_p$ on $\operatorname{Sym}^2V^\vee$ at a good $p$ are $\alpha^2,\alpha\beta=p,\beta^2$, so
$P_p(X)=(1-\alpha^2X)(1-pX)(1-\beta^2X)$. Reference: elementary; DFG04 1.7.2 (as quoted by the paper; the citation is correct and DFG04 use the geometric Frobenius: Chapter 20 outline, Part 7; important_notes.md point 73). Paper:
Section 1.1 ("In the normalisation of the symmetric square, $L_p(\Sym f,s)=L_p(A_f,s-1)$"), Definition def:terms ("$P_q(X)$ is the
polynomial with $L_q(\Sym f,s)=P_q(q^{-s})^{-1}$").

**6.2 `prop:lfunctions:good-factor`** (proposition; P). Let $p\nmid N$, $p\ne\ell$, $a=a_p(f)$, $\alpha+\beta=a$, $\alpha\beta=p$. (i) $\Phi_p$ and $\Frob_p$ both have
eigenvalues $\alpha/\beta,1,\beta/\alpha$ on $A_f$, and
$$L_p(A_f,s)^{-1}=\Bigl(1-\frac\alpha\beta p^{-s}\Bigr)(1-p^{-s})\Bigl(1-\frac\beta\alpha p^{-s}\Bigr)=(1-p^{-s})\bigl(1-(a^2-2p)p^{-1-s}+p^{-2s}\bigr),$$
$P_p(X)=(1-pX)(1-(a^2-2p)X+p^2X^2)$. (ii) $L_p(A_f,1)^{-1}=\frac{p-1}p\cdot\frac{(p+1)^2-a^2}{p^2}$ (Chapter 2, 11.4), which is Wiles's level-raising
factor; it is nonzero by the Hasse bound $|a|\le2\sqrt p$ ($(p+1)^2-a^2\ge(p-1)^2>0$). (iii) For $\ell\ne p$ odd:
$v_\ell(L_p(A_f,1)^{-1})>0$ iff $p\equiv1\pmod\ell$ or $a\equiv\pm(p+1)\pmod\ell$; the second condition is Ribet's level-raising condition
(Chapter 15). Reference: elementary; DDT (Wiles's factor; cite the section). Paper: Theorem thm:dfg14 and the paragraph after it
("Wiles's level-raising factor"), the $\mathrm I_0^*$ row of the table (the same formula for $E'$), Theorem thm:quant Step 3.

### Section 7. Analytic theory, normalisations and critical values

**7.1 `thm:lfunctions:sym2-analytic`** (theorem; R, with (iii) P given 8.3). Let $f$ be as in 6.1. (i) (Shimura 1975) $L(\Sym f,s)$
extends meromorphically to $\C$ (Shimura proved this, and holomorphy under conditions that the writer must copy from the paper,
via the series $\sum a_{n^2}n^{-s}$ of 8.2(B), a theta series and an Eisenstein series of half-integral weight; proposed key `Shimura75`,
Part 6.5). (ii) (Gelbart and Jacquet 1978) there is an automorphic
representation $\operatorname{Ad}(\pi_f)$ of $\GL_3(\mathbb A_\Q)$, cuspidal unless $f$ has complex multiplication, whose standard $L$-function is
$L(s,\pi_f,\operatorname{Ad})=L(\ad f,s)$ (unitary normalisation, centre $1/2$; agreement of the local factors at the bad primes with
the Galois side by local-global compatibility, Chapter 15, its 3.4, R); consequently $L(\ad f,s)$ is entire (also in the CM
case, where it is $L(s,\chi_K)$ times a Hecke $L$-function of a nontrivial character; verify) and satisfies
$\Lambda(\ad f,s)=\varepsilon\,\Lambda(\ad f,1-s)$ with $\Lambda(\ad f,s)=N_{\ad}^{s/2}\Gamma_\R(s+1)\Gamma_\C(s+1)L(\ad f,s)$, $N_{\ad}$ the conductor of $A_f$, $\varepsilon=\pm1$
(the root number; PARI's data give $\varepsilon=+1$ for every curve examined; state "$\varepsilon=+1$" only with a reference, verify).
(iii) $L(\ad f,1)>0$ (P: by 8.3, $L^{\nv}(\ad f,1)=8\pi^3\langle f,f\rangle/N>0$, and every omitted factor $L_q(A_f,1)^{-1}$ is positive, by 9.3 and
10.1). Reference: Shimura75; GelbartJacquet; Shimura76 (cite sections; verify). Paper: Section 1 ("Rankin, Shimura"); the special
value $L(\Sym f,2)=L(\ad f,1)$ of Section 1.

**7.2 `prop:lfunctions:ad-conductor`** (proposition; P given Chapter 7, 9.1 to 9.4; the gamma factor R). (i) The conductor exponent
of $A_f$ at $q\ge5$ ($q\ne\ell$) is $2$ for the types $\mathrm I_n$, $\mathrm I_n^*$ ($n\ge1$), $\mathrm{II}$, $\mathrm{II}^*$, $\mathrm{III}$, $\mathrm{III}^*$, $\mathrm{IV}$, $\mathrm{IV}^*$, and $0$
for $\mathrm I_0^*$ (where $A_f$ is unramified); so $N_{\ad}=\prod_{q\mid N,\ q\text{ not }\mathrm I_0^*}q^2$ (the square of the radical of $N$ with the $\mathrm I_0^*$ primes removed, not $N^2$) when $(N,6)=1$. (ii) The gamma factor of $L(\Sym f,s)$ is
$\Gamma_\R(s)^2\Gamma_\R(s+1)=\Gamma_\R(s)\Gamma_\C(s)$, that of $L(\ad f,s)$ is $\Gamma_\R(s+1)\Gamma_\C(s+1)$ (2.3(ii)). Checked: PARI's `lfunparams(lfunsympow(E,2))` is
`[N_sym, 3, [0, 0, 1]]` (motivic weight $3$, so $s\leftrightarrow3-s$; gamma shifts $0,0,1$), with $N_{\mathrm{sym}}=121$ for 11a1, 121a1, 539d1, 275b1 (the
$\mathrm I_0^*$ primes $7$, $5$ contribute nothing), $100$ for 20a1 (type $\mathrm{IV}^*$ at $2$: exponent $2$), $81$ for 27a1 (wild at $3$), $64$ for 64a1,
$1764=42^2$ for 336f1, $5929=77^2$ for 1232l1 (no contribution at $2$: case 10.1(b)), and sign $+1$ in all these cases.
Paper: background (Section 1.1, `lfunsympow`).

**7.3 `rem:lfunctions:critical`** (remark; R, with the rationality P given 8.3). Deligne's conjecture (Deligne79): for a motive $M$
over $\Q$, an integer $n$ is critical if neither $L_\infty(M,s)$ nor $L_\infty(M^\vee,1-s)$ has a pole at $s=n$, and then
$L(M,n)/c^\pm(M(n))\in\Q^\times$ for Deligne's period $c^\pm$. For $\ad$ of a weight-$2$ form ($L_\infty=\Gamma_\R(s+1)\Gamma_\C(s+1)$, self-dual) the critical
integers are $s=0,1$; for $L(\Sym f,s)$ they are $s=1,2$. By 8.3, $L(\ad f,1)/(\pi^3\langle f,f\rangle)=8/\bigl(N\prod_{q^2\mid N}L_q(A_f,1)^{-1}\bigr)\in\Q^\times$,
which is Deligne's conjecture at $s=1$ once his period is identified with $\pi^3\langle f,f\rangle$ up to $\Q^\times$ (Sturm proved the
analogous statement for all weights; proposed key `Sturm80`, verify; Zagier's work on $L(\Sym f,s)$ in level one; cite
sections only). One paragraph in the chapter. Paper: background (Section 1, "the special value $L(\Sym f,2)$").

**7.4 `rem:lfunctions:normalisations`** (remark with table; P for every identity, R for what each source writes). The objects that
occur, in one table (the writer checks each source's own notation before attributing it; marked "verify" where not checked):

| name | source | relation to $L(A_f,s)=L(\ad f,s)$ | functional equation | value the paper uses | factor at additive $p$ |
|-|-|-|-|-|-|
| $L(\ad f,s)$ | paper Sections 1, 1.1; DFG04 (1.7.2, $L(\ad^0M_f,s)$ at $s=1$; checked, Chapter 20 outline, Part 7; important_notes.md point 73) | itself | $s\leftrightarrow1-s$ | $s=1$ | true |
| $L(s,\pi_f,\operatorname{Ad})$ | Gelbart-Jacquet (unitary) | $=L(A_f,s)$ (weight $k$: $L(A_f,s)=L(\Sym^2,s+k-1)$) | $s\leftrightarrow1-s$ | $s=1$ | true |
| $L(\Sym f,s)$ | paper; PARI `lfunsympow(E,2)`; Watkins02; CoatesSchmidt87 (verify) | $L(A_f,s-1)$ | $s\leftrightarrow3-s$ | $s=2$ | true |
| Shimura's series | Shimura75: $\zeta^{(N)}(2s-2)\sum a_{n^2}n^{-s}$ | $L^{\nv}(A_f,s-1)$ (8.2(B)) | (via 7.1) | | naive ($1$) |
| $L^{\nv}(\ad f,s)$ | paper Section 1.1; DFG04 (the naive factors of Proposition 1.4) | $L(A_f,s)\prod_{p^2\mid N}L_p(A_f,s)^{-1}$ | none | $s=1$ | naive ($1$) |
| Rankin series $D(f,s)$ | Rankin, Selberg, Shimura76; Chapter 13, 10.3 | $\zeta^{(N)}(s-1)L^{\nv}(A_f,s-1)/\zeta^{(N)}(2s-2)$ (8.2(A)) | via $E(z,s)$ | residue at $s=2$ | naive ($1$) |
| $L(f\times f,s)$ | Rankin-Selberg convolution | $\zeta^{(N)}(2s-2)D(f,s)=\zeta^{(N)}(s-1)L^{\nv}(A_f,s-1)$ | | pole at $s=2$ | naive ($1$) |

Pitfall stated in the chapter: Hida's and Sturm's papers use weight $k$ and the classical variable; for weight $k$,
$L(\ad f,s)=L(\Sym f,s+k-1)$, so "$L(\Sym f,k)$" is $L(\ad f,1)$. Paper: Section 1.1 (normalisation sentence); Appendix B
(conventions).

### Section 8. Naive versus true; Rankin-Selberg; the Petersson norm and the modular degree

**8.1 `def:lfunctions:naive`** (definition and proposition; P given Chapter 15, its 3.5, 3.7, and Chapter 11, its 3.5). For $p\mid N$
let $L_p^{\nv}(A_f,s)=L_p(A_f,s)$ if $\delta_p>0$ and $1$ if $\delta_p=0$; for $p\nmid N$, $L_p^{\nv}=L_p$ (C6). (i) For $p\mid N$,
$L_p^{\nv}(A_f,s)^{-1}=1-a_p(f)^2p^{-1-s}$, because $a_p(f)=\pm1$ iff $\delta_p=1$ (and then $L_p(A_f,s)^{-1}=1-p^{-1-s}$, item 9.2) and $a_p(f)=0$ iff
$\delta_p=0$. So $L^{\nv}(\ad f,s)$ is determined by the Fourier coefficients $a_p(f)$ alone, through 6.2(i) at good $p$ and this formula at
bad $p$; this is what "naive" means, and why the constructions of DFG04 built from $q$-expansions and depleted forms see it. (ii)
$L^{\nv}(\ad f,s)=L(\ad f,s)\prod_{p^2\mid N}L_p(A_f,s)^{-1}$: the two differ exactly at the additive primes, by the omitted factors, which
are invisible in $a_p(f)=0$ (the local representation at an additive prime is not determined by $a_p$; Chapter 15, 3.5). Paper:
Section 1 ("the naive one ... the trivial factor at the additive primes"), Section 1.1, Definition def:terms, Theorem thm:dfg14,
Lemma lem:fpr.

**8.2 `prop:lfunctions:rankin-series`** (proposition; P; important_notes.md point 30, sharpened). Let $f$ be as in 6.1. For $\operatorname{Re}s>2$:
$$\text{(A)}\quad\sum_{n\ge1}a_n(f)^2n^{-s}=\frac{\zeta^{(N)}(s-1)}{\zeta^{(N)}(2s-2)}\,L^{\nv}(\Sym f,s),\qquad\text{(B)}\quad\sum_{n\ge1}a_{n^2}(f)\,n^{-s}=\frac{L^{\nv}(\Sym f,s)}{\zeta^{(N)}(2s-2)},$$
exactly, with no correction at the bad primes. Proof: both sides are Euler products (2.2); at a good $p$, with $X=p^{-s}$,
$\sum_ka_{p^k}^2X^k=\frac{1+pX}{(1-\alpha^2X)(1-pX)(1-\beta^2X)}$ and $\sum_ka_{p^{2k}}X^k=\frac{1-p^2X^2}{(1-\alpha^2X)(1-pX)(1-\beta^2X)}$ (write $a_{p^k}=\frac{\alpha^{k+1}-\beta^{k+1}}{\alpha-\beta}$ and
sum geometric series; or check with the recursion of Chapter 13); at $p\mid N$, $a_{p^k}=a_p^k$ with $a_p^2\in\{0,1\}$, so both local series equal
$(1-a_p^2p^{-s})^{-1}=L_p^{\nv}(\Sym f,s)$ (8.1(i)), and $\zeta^{(N)}$ has no factor at $p$. Consequences: (a) the Rankin series is **not** the naive
symmetric square: at a good $p$ it carries the extra factor $1+p^{1-s}$, e.g. for 11a1 the coefficient of $2^{-s}$ is $a_2^2=4$ in the Rankin
series and $a_2^2-2=2$ in $L^{\nv}(\Sym f,s)$; (b) Shimura's series (B), completed by $\zeta^{(N)}(2s-2)$, **is** the naive symmetric square.
`warning` environment quoting the paper's sentence and the corrected reading: "the naive one, $L^{\nv}(\Sym f,s)=\zeta^{(N)}(2s-2)\sum a_{n^2}n^{-s}$, which
differs from $\sum a_n(f)^2n^{-s}$ by the factor $\zeta^{(N)}(s-1)/\zeta^{(N)}(2s-2)$". Verified: the local identities as power series to order $20$
for $(p,a_p)=(5,2),(7,-3),(11,0),(13,5)$; the global identities at $s=6$ for 11a1, 20a1, 121a1 (agreement to $10^{-12}$, the truncation
error). Reference: Shimura75 (for (B)); Rankin39, Shimura76 (for (A)); elementary. Paper: Section 1 (point 30).

**8.3 `thm:lfunctions:petersson-sym2`** (theorem; S for the unfolding, which is Chapter 13's 10.3(i); P for the rest). Let $f$ be as in
6.1 and $\langle\ ,\ \rangle$ the unnormalised Petersson product (C9). Then
$$\langle f,f\rangle=\frac N{8\pi^3}\,L^{\nv}(\Sym f,2)=\frac N{8\pi^3}\,L(\Sym f,2)\prod_{p^2\mid N}P_p(p^{-2})=\frac N{8\pi^3}\,L(\ad f,1)\prod_{p^2\mid N}L_p(A_f,1)^{-1}.$$
Proof: Chapter 13, 10.3(i) gives $\operatorname{Res}_{s=2}D(f,s)=\frac{48\pi}{\mu(N)}\langle f,f\rangle$; by 8.2(A) and 3.2 the residue is
$\frac{6N}{\pi^2\mu(N)}L^{\nv}(\Sym f,2)$; compare. (The point $s=2$ is on the edge of absolute convergence, 4.3: write
$L^{\nv}(\Sym f,s)=D(f,s)\zeta^{(N)}(2s-2)/\zeta^{(N)}(s-1)$, which is holomorphic at $s=2$ because $D$ has at most a simple pole there (Chapter 13) and
$\zeta^{(N)}(s-1)$ has one; its value is the value at $s=2$ of the continuation 7.1, which is what PARI computes.) For square-free $N$ this is Chapter 13's 10.3(ii). So "$\langle f,f\rangle$ is $L(\Sym f,2)$ up to the local factors at
the bad primes" (paper, Section 1) holds in the precise form: up to $N/(8\pi^3)$ and the omitted factors at the **additive** primes only;
the multiplicative primes contribute nothing beyond $N$. Verified (PARI, 18 digits; $\langle f,f\rangle$ as $\mu(N)$ times `mfpetersson`, $L(\Sym f,2)$ by
`lfun(lfunsympow(E,2),2)`): 11a1, 14a1, 20a1, 27a1, 36a1, 49a1, 50a1, 64a1, 99a1, 121a1, 121c1, 121d1, 162a1, 52a1, 80a1, with correction
factors $1,1,3/2,1,2,8/7,6/5,1,4/3,12/11,12/11,120/121,4/3,3/2,1$ (table 12.2). Reference: Rankin39; Selberg40 (proposed `bib/ch19.bib`
key); Shimura76 (verify which statement); Zagier85; Watkins02 (the method of `ellmoddegree`; cite the section); DFG04 Lemma 2.12
(as cited by the paper; checked: it gives the Petersson norm with the naive $L$-value, Chapter 20 outline, Part 7; important_notes.md point 73; the writer compares its
constant with this exact formula before attributing the formula to it).
Paper: Section 1 ("Rankin, Shimura; see DFG04 Lemma 2.12").

**8.4 `cor:lfunctions:degree-formula`** (corollary; P given 8.3 and Chapter 14, its 7.3). (i) For every modular parametrisation
$\varphi\colon X_0(N)\to E$ with Manin constant $c_\varphi$: $\deg\varphi\cdot\operatorname{vol}(\Lambda_E)=c_\varphi^2\,N\,L^{\nv}(\ad f,1)/(2\pi)$. (ii) For the optimal curve
($c_E=1$ for the curves of the tables, with the sign of $\omega_E$ fixed by $c_E>0$, Chapter 14; Appendix B, B-C9): $\degphi=N\,L^{\nv}(\ad f,1)/(2\pi\operatorname{vol}(\Lambda_E))$. (iii) Put
$B_E=N\,L(\ad f,1)/(2\pi\operatorname{vol}(\Lambda_E))$. Then $B_E=\degphi\prod_{q^2\mid N}P_q(q^{-2})^{-1}\in\Q^\times$ (for $c_E=1$) and, for every prime $\ell\nmid N$,
$$v_\ell(\degphi)=v_\ell(B_E)+\sum_{q\mid N}e_\ell(E,q)$$
(at a multiplicative $q$, $e_\ell=0$; at an additive $q$, $e_\ell(E,q)=v_\ell(L_q(A_f,1)^{-1})=v_\ell(P_q(q^{-2}))$, 9.1). This identity is unconditional:
the paper's inequality (eq:thm) is equivalent to $v_\ell(B_E)\ge\sum_{q\mid N}t_\ell(E,q)$. (iv) $v_\ell(B_E)$ can be negative when the hypotheses of
Theorem thm:main fail: 539d1 ($B=343/5$, $E[5]$ reducible), 121d1 ($B=121/5$, $E[5]$ reducible), 98a1 ($B=49/3$, $E[3]$ reducible), 121b1
($B=11/3$, CM by $\Q(\sqrt{-11})$, mod $3$ image induced) (table 12.3). Verified: $B_E$ computed both as $\degphi/\prod P_q(q^{-2})$ (Cremona's
`degphi`) and numerically from `lfun` and `E.area` agree for the 19 curves of 12.1 (e.g. 121a1: $11/2$; 539c1: $294$; 980i1: $1960$;
1232l1: $256$; 592c1: $128$). Paper: Section 1 ("Up to explicit factors $\degphi$ is $\langle f,f\rangle$ divided by the area of the period lattice"),
Theorem thm:main (the role of the omitted factors), Section sec:sharp ("the size of the Petersson norm"). See Part 7, N2.

**8.5 `rem:lfunctions:bloch-kato-reading`** (remark; S, a reading, not a proof; forward pointer to Chapters 18, 20). For $\ell\notin S_f$,
the paper's identity (eq:identity), which holds with equality (important_notes.md points 39, 56; Chapters 14, 20), reads
$v_\ell(\degphi)=\len H^1_f(\Q,W)+\sum_qv_\ell(\Tam_q(\ad T))+\sum_qe_\ell(E,q)$. Comparing with 8.4(iii) gives
$v_\ell(B_E)=\len H^1_f(\Q,W)+\sum_qv_\ell(\Tam_q(\ad T))$: the $\ell$-part of the Bloch-Kato formula for $L(\ad f,1)$ with the period $2\pi\operatorname{vol}(\Lambda_E)/N$,
which is the shape of DFG04 Theorem 0.1 (Chapter 18; the period normalisation of DFG04 is not checked here, and the chapter must
say so). This is the conceptual content of the paper's sentence "the primes at which the naive and the true adjoint
$L$-functions differ are exactly the primes at which the modular degree acquires extra local divisibility": the Petersson norm,
hence $\degphi$, sees $L^{\nv}$; Bloch-Kato sees $L$; the ratio is the product of the omitted factors. Paper: Section 1 (the paragraph
before Section 1.1), Theorem thm:main.

**8.6 `thm:lfunctions:flach`** (theorem; R). (Flach 1992.) Let $E/\Q$ be modular (now always) and $p$ an odd prime satisfying the
hypotheses of Flach92 (good reduction at $p$ and a condition on the image of $\rho_{E,p}$; the writer copies them from the paper).
Then the Bloch-Kato Selmer group of $\operatorname{Sym}^2T_pE$ (for $p$ odd $\operatorname{Sym}^2T_pE\simeq\ad T(1)$, the module $T^D$ of Chapter 18) with
$\Q_p/\Z_p$ coefficients is finite, and it is annihilated by an explicit integer built from the modular degree (verify the exact
annihilator and which Selmer group, of $\operatorname{Sym}^2T_pE$ or of its Kummer dual, against Flach92 before writing anything finer). The proof
uses an Euler-system-type construction of classes from $K_2$ of $X_0(N)\times X_0(N)$ (Beilinson-Flach elements; one sentence). Reference:
Flach92 (cite the main theorem by section). Paper: Section 1 ("Flach's finiteness theorem for the symmetric square is the first
place where the modular degree meets the Selmer group of $\Sym f$"). Chapter 18 may restate it in Selmer language; the statement
lives here.

### Section 9. The local terms and Lemma lem:euler

Standing hypotheses: $q\mid N$ a bad prime, $q\ne\ell$; the inertia images are Chapter 11's (Kraus's theorem via Chapter 10), the
Weil-Deligne shapes and local factors Chapter 7's; this section assembles them, adds $P_q$, the naive factor and the valuations.

**9.1 `def:lfunctions:terms`** (definition, the paper's Definition def:terms, with the corrections of points 15 and 53; P for the
properties). For a bad prime $q\ne\ell$:
$$e_\ell(E,q)=v_\ell\Bigl(\frac{L_q(A_f,1)^{-1}}{L_q^{\nv}(A_f,1)^{-1}}\Bigr)=v_\ell\Bigl(\frac{P_q(q^{-2})}{1-a_q(E)^2q^{-2}}\Bigr);$$
for every bad prime $q$ (including $q=\ell$, as `rule(E, l)` and (eq:rule) use it; point 53): $t_\ell(E,q)=v_\ell(-v_q(j_E))$ if $v_q(j_E)<0$, else $0$.
Properties: (i) $e_\ell(E,q)$ is a finite nonnegative integer ($P_q(q^{-2})\in\Z[1/q]\setminus\{0\}$, 9.6); it is $0$ at a multiplicative $q$ (naive $=$ true,
9.2) and $v_\ell(P_q(q^{-2}))$ at an additive $q$ ($a_q=0$). (ii) $t_\ell(E,q)=v_\ell(n)$ for type $\mathrm I_n$ at any $q$ and for $\mathrm I_n^*$ at odd $q$ (Chapter
10); at $q=2$ a symbol $\mathrm I_m^*$ may have $-v_2(j)\ne m$, or $v_2(j)\ge0$ (potentially good), and then $t_\ell=0$. (iii) Twists: 9.5 ($t_\ell$
invariant; $e_\ell$ not, point 15). Paper: Definition def:terms, Theorem thm:main, Conjecture conj:euler, the appendix.

**9.2 `prop:lfunctions:multiplicative`** (proposition; P given Chapter 11, its 3.2(v), and Chapter 7, its 9.3). Let $q\ne\ell$ be a prime of
multiplicative reduction (any $q$, split or nonsplit). Then $A_f^{I_q}$ is the line spanned by $e=e_1\otimes e_2^\vee$ (the nilpotent $N$ of the
Weil-Deligne representation), $\Phi_q$ acts on it by $q^{-1}$ ($\Frob_q$ by $q$; the sign $\varepsilon$ cancels in the adjoint), so
$L_q(A_f,s)^{-1}=1-q^{-1-s}$, $P_q(X)=1-X$, $L_q(A_f,1)^{-1}=1-q^{-2}$, the naive factor equals the true one ($a_q^2=1$) and $e_\ell(E,q)=0$. With
$\Frob_q$ in place of $\Phi_q$ one would get $1-q^{1-s}$ (point 11). Paper: the $\mathrm I_n$ row of the table; Lemma lem:euler (type $\mathrm I_n$);
Definition def:terms ("it is $0$ at a multiplicative prime"); Theorem thm:dfg14 ("adding a multiplicative prime multiplies it by
$1-p^{-2}$"); Lemma lem:fpr; Section sec:iso ("Multiplicative primes show no Euler term").

**9.3 `lem:lfunctions:euler`** (lemma, the paper's Lemma lem:euler; P given Kraus's theorem (R, via Chapters 10 and 11)). Let $q\ge5$ be
a bad prime, $q\ne\ell$. Then $L_q(A_f,s)$, $P_q$ and $e_\ell(E,q)$ are as follows, where $\sigma$ denotes an element of order $3$ and $\tau$ one of
order $4$ in $\SL_2(\Z_\ell)$, $E'=E^{(q^*)}=E\otimes\chi_{q^*}$ (good reduction at $q$ for type $\mathrm I_0^*$) and $a'=a_q(E')$:

| type at $q$ | $\rho(I_q)$ | $A_f^{I_q}$ spanned by | $\Phi_q$ on it | $L_q(A_f,s)^{-1}$ | $P_q(X)$ | $P_q(q^{-2})$ | $e_\ell(E,q)$ |
|-|-|-|-|-|-|-|-|
| $\mathrm I_n$ | unipotent, infinite | $e$ | $q^{-1}$ | $1-q^{-1-s}$ | $1-X$ | $1-q^{-2}$ | $0$ |
| $\mathrm I_n^*$ | $\chi_{q^*}\cdot$unipotent | $e$ | $q^{-1}$ | $1-q^{-1-s}$ | $1-X$ | $1-q^{-2}$ | $v_\ell(q^2-1)$ |
| $\mathrm{IV},\mathrm{IV}^*$ / $\mathrm{II},\mathrm{II}^*$ | $\langle\sigma\rangle$ / $\langle-\sigma\rangle$ | $2\sigma+1$ ($(2\sigma+1)^2=-3$) | $\chi_{-3}(q)$ | $1-\chi_{-3}(q)q^{-s}$ | $1-\chi_{-3}(q)qX$ | $1-\chi_{-3}(q)/q$ | $v_\ell(q-\chi_{-3}(q))$ |
| $\mathrm{III},\mathrm{III}^*$ | $\langle\tau\rangle$ | $\tau$ | $\chi_{-4}(q)$ | $1-\chi_{-4}(q)q^{-s}$ | $1-\chi_{-4}(q)qX$ | $1-\chi_{-4}(q)/q$ | $v_\ell(q-\chi_{-4}(q))$ |
| $\mathrm I_0^*$ | $\{\pm1\}$ | all of $A_f=\ad V_\ell E'$ | $\alpha'/\beta',1,\beta'/\alpha'$ | $(1-\frac{\alpha'}{\beta'}q^{-s})(1-q^{-s})(1-\frac{\beta'}{\alpha'}q^{-s})$ | $(1-qX)(1-(a'^2-2q)X+q^2X^2)$ | $\frac{(q-1)((q+1)^2-a'^2)}{q^3}$ | $v_\ell(q-1)+v_\ell((q+1)^2-a'^2)$ |

Proof (to be written in five steps, each citing its source): (1) inertia images: Chapter 11, its 3.2, 3.4, 4.1 (Kraus for the
orders; tame since $q\ge5$, hence cyclic). (2) Invariants: $A_f^{I_q}$ is the trace-zero part of the commutant of $\rho(I_q)$ (Chapter 4);
for $\langle\pm\sigma\rangle$ the commutant is $\Q_\ell[\sigma]\simeq\Q_\ell\otimes\Q(\zeta_3)$, whose trace-zero line is spanned by $2\sigma+1$ (the paper's "$\sqrt{-3}$"); the
sign of $-\sigma$ disappears in $\ad$; for $\langle\tau\rangle$ the trace-zero line is spanned by $\tau$ itself (point 34: $\tau$ is diagonalisable over
$\Q_\ell$ only if $\ell\equiv1\pmod4$, so "the diagonal element" must not be written); for the unipotent shapes it is $\ker[N,\cdot\,]=\Q_\ell N$ (Chapter
7, 9.3); for $\{\pm1\}$ everything. The commutant statements are for $\End_{I_q}(T)=\Z_\ell[g]$ and $\End_{I_q}(V)=\Q_\ell[g]$, the latter
$\Q_\ell\otimes\Q(\zeta_3)$ or $\Q_\ell\otimes\Q(i)$, which is not a field when $\ell\equiv1\pmod3$, resp. $\pmod4$ (point 12). (3) Frobenius:
$\rho(\Frob_q)\,g\,\rho(\Frob_q)^{-1}=g^q$ (Chapter 7, 5.6); $\sigma^q=\sigma$ or $\sigma^{-1}$ as $q\equiv1$ or $2\pmod3$, and $2\sigma^{-1}+1=-(2\sigma+1)$; $\tau^q=\tau$ or
$-\tau$ as $q\equiv1$ or $3\pmod4$; $\Phi_q$ gives the same sign since $q^{-1}\equiv q$ modulo $3$ and modulo $4$; for $\mathrm I_0^*$, $V\simeq V_\ell E'\otimes\chi_{q^*}$
(Chapter 10, Lemma lem:twist (ii); Chapter 11, 4.1) and $\ad V=\ad V_\ell E'$ is unramified with eigenvalues $\alpha'/\beta',1,\beta'/\alpha'$ (6.2);
for $\mathrm I_n^*$, $V\simeq V'\otimes\chi_{q^*}$ with $V'$ of multiplicative shape and $\ad V=\ad V'$ (9.2). (4) $P_q$ by 6.1(i). (5) Valuations by
Chapter 2, 11.3 to 11.5: the naive factor is $1$ for the additive rows ($a_q=0$) and $1-q^{-2}$ for $\mathrm I_n$. Well-definedness for $\mathrm I_0^*$:
the other ramified quadratic character of $\Q_q$ gives the twist with $a_q=-a'$, and only $a'^2$ enters. Verified: on **all** $64{,}687$
curves of conductor below $10{,}000$, every one of the $117{,}232$ pairs (curve, bad prime $q\ge5$) has PARI's $P_q$ equal to the table
($\mathrm I_n$: $102{,}309$; $\mathrm I_n^*$: $6{,}224$; $\mathrm I_0^*$: $2{,}241$, with $a'$ computed from `elltwist`; $\mathrm{II}$: $1{,}575$; $\mathrm{II}^*$: $760$; $\mathrm{III}$, $\mathrm{III}^*$:
$1{,}394$ each; $\mathrm{IV}$: $760$; $\mathrm{IV}^*$: $1{,}575$); no exception. Reference: Kraus90; SerreTate68; Chapters 4, 7, 10, 11. Paper: Lemma
lem:euler, the table of Section 1, the abstract.

**9.4 `rem:lfunctions:euler-values`** (remark; P, citing Chapter 2, its 11.5). When the omitted factor is an $\ell$-adic non-unit: for
$\ell=3$, always for $\mathrm{II}$ to $\mathrm{IV}^*$ ($q\equiv\chi_{-3}(q)\pmod3$) and for $\mathrm I_n^*$; for $\mathrm{III}$, $\mathrm{III}^*$ iff $q\equiv\pm1\pmod{12}$; for $\mathrm I_0^*$ iff
$q\equiv1\pmod3$ or $3\mid a'$. For $\ell\ge5$: iff $q\equiv\chi(q)\pmod\ell$ (rows 3, 4), $q\equiv\pm1\pmod\ell$ ($\mathrm I_n^*$), $q\equiv1\pmod\ell$ or $a'\equiv\pm(q+1)\pmod\ell$
($\mathrm I_0^*$). Examples (12.1): 121a1 ($\mathrm{II}$ at $11$: $e_3=1$), 147b1 ($\mathrm{IV}^*$ at $7$: $e_3=v_3(6)=1$), 726a1 ($\mathrm{III}$ at $11$: $e_3=v_3(12)=1$), 539c1
($\mathrm I_3^*$ at $7$: $e_3=v_3(48)=1$), 539d1 ($\mathrm I_0^*$ at $7$, $E'=$ 11a3, $a'=-2$: $e_3=v_3(6)+v_3(60)=2$), 275b1 ($\mathrm I_0^*$ at $5$, $a'=\pm1$: $e_7=v_7(35)=1$,
$\degphi=28$). Paper: Proposition prop:forms (proof), the Remark after Theorem thm:quant, (1), Sections sec:iso, sec:anomaly.

**9.5 `prop:lfunctions:twists`** (proposition; P). Let $\chi$ be a quadratic character and $E^\chi=E\otimes\chi$. (i) $A_{f}$ and $A_{f\otimes\chi}$ are
isomorphic ($\ad(\rho\otimes\chi)=\ad\rho$), so $L_q(A_f,s)$, $P_q$ and $L(\ad f,s)$ are invariant under every quadratic twist. (ii) If $\chi$ is
unramified at $q$, then $\delta_q$, $a_q^2$, the naive factor and $e_\ell(E,q)$ are unchanged. (iii) For $q$ odd and $\chi=\chi_{q^*}$: $e_\ell$ is
unchanged for the exchanges $\mathrm{II}\leftrightarrow\mathrm{IV}^*$, $\mathrm{III}\leftrightarrow\mathrm{III}^*$, $\mathrm{IV}\leftrightarrow\mathrm{II}^*$ ($q\ge5$; $\delta_q=0$ on both sides), but changes for
$\mathrm I_n\leftrightarrow\mathrm I_n^*$ ($0\leftrightarrow v_\ell(q^2-1)$) and $\mathrm I_0\leftrightarrow\mathrm I_0^*$ ($e_\ell$ undefined at a good prime; $v_\ell(q-1)+v_\ell((q+1)^2-a_q^2)$ on the
$\mathrm I_0^*$ side); in every case $e_\ell(E,q)+v_\ell(L_q^{\nv}(A_f,1)^{-1})=v_\ell(L_q(A_f,1)^{-1})$ is invariant. (iv) $t_\ell(E,q)$ is invariant under every
quadratic twist ($j$ is). Example: 11a1 (type $\mathrm I_5$ at $11$, $e_3=0$) and its twist 121d2 $=$ 11a1 $\otimes\chi_{-11}$ (type $\mathrm I_5^*$, $e_3=v_3(120)=1$)
(important_notes.md point 15, B8). Paper: Definition def:terms ("Both terms are invariant under quadratic twist": true for $t_\ell$
only), Theorem thm:quant Step 3 ("$A_g=A_f$ ... its naive factor is the true one, which is the factor that $f$ omits").

**9.6 `prop:lfunctions:fpr-L-part`** (proposition; P; the $L$-part of the paper's Lemma lem:fpr). Let $\ell$ be odd, $p\mid N$, $p\ne\ell$,
$V^D=\Hom(A_f,\Q_\ell(1))\simeq A_f(1)$ (trace form, Chapter 4, 7.6). Then
$$\det\bigl(1-\Phi_p\bigm|(V^D)^{I_p}\bigr)=L_p(A_f(1),0)^{-1}=L_p(A_f,1)^{-1}=P_p(p^{-2}),$$
a nonzero element of $\Z[1/p]\subset\Z_{(\ell)}$, of valuation $e_\ell(E,p)$ at an additive $p$ and $v_\ell(1-p^{-2})=v_\ell(p^2-1)$ at a multiplicative $p$.
Nonvanishing: $1-p^{-2}$, $1\mp p^{-1}$ and $(p-1)((p+1)^2-a'^2)/p^3$ (Hasse) are nonzero, and 10.1 lists the only other shapes. With $\Frob_p$ in
place of $\Phi_p$ the determinant changes by $\det(-\Frob_p\mid(V^D)^{I_p})$, a unit of $\Z_{(\ell)}$ (a power of $p$ up to sign): the vanishing
of $H^1_{\mathrm{ur}}(\Q_p,V^D)=(V^D)^{I_p}/(\Frob_p-1)$ (Chapter 17) holds in either reading, but the equality with $L_p(A_f,1)^{-1}$ needs $\Phi_p$
(point 11). Paper: Lemma lem:fpr ("$L_p(A_f,1)^{-1}=L_p(A_f(1),0)^{-1}$ is a nonzero rational number which is an $\ell$-adic integer, of
valuation $e_\ell(E,p)$ at an additive prime and $v_\ell(1-p^{-2})$ at a multiplicative one"), the paragraph after Lemma lem:dfg21. The
Fitting-ideal identity $\Fitt H^1_f(\Q_p,T^D)=L_p(A_f,1)^{-1}\Tam_p(T^D)$ is Chapter 18's.

**9.7 `prop:lfunctions:naive-factors`** (proposition; P). At $s=1$: $L_p^{\nv}(A_f,1)^{-1}=\frac{(p-1)((p+1)^2-a_p^2)}{p^3}$ ($p\nmid N$), $1-p^{-2}$ ($p\,\|\,N$), $1$
($p^2\mid N$). Consequently, for a finite set $\Sigma$ of primes dividing $N$, $p\ne\ell$:
$\sum_{p\in\Sigma}\bigl(v_\ell(L_p(A_f,1)^{-1})-v_\ell(L_p^{\nv}(A_f,1)^{-1})\bigr)=\sum_{p\in\Sigma}e_\ell(E,p)$, the cancellation in the proof of Theorem thm:main; and for
$g=f_{E_S}$ as in Theorem thm:quant ($\delta_q(g)\ge1$ at $q\in S$): $v_\ell(L_q^{\nv}(A_g,1)^{-1})=v_\ell(L_q(A_f,1)^{-1})=e_\ell(E,q)$ (9.5(i), 9.3). Paper:
Theorem thm:dfg14 and the paragraph after it ("Only the primes with $\delta_p\ge1$ contribute"), the proof of Theorem thm:main, Theorem
thm:quant Step 3, the Remark after Theorem thm:quant, (3) ("there the quadratic twist does not lower the level, $f$ is its own
depletion, and Theorem thm:dfg14 gives no factor"). The theorem of DFG04 itself is Chapter 20's.

### Section 10. Every prime, including $2$ and $3$

**10.1 `prop:lfunctions:all-shapes`** (proposition; P given Grothendieck/Neron-Ogg-Shafarevich (Chapter 11) and local class field
theory only for the existence of quadratic characters (Chapter 7, 6.3); new in this form). Let $q\ne\ell$ be a prime of bad
reduction, any $q$ (including $2$ and $3$). Exactly one of the following holds.

(a) *Potentially multiplicative* ($v_q(j)<0$): $P_q(X)=1-X$, $L_q(A_f,1)^{-1}=1-q^{-2}$; $e_\ell(E,q)=0$ if the reduction is multiplicative and
$v_\ell(q^2-1)$ if it is additive.

(b) *Potentially good with $\rho(I_q)=\{\pm1\}$*; equivalently, some quadratic twist $E^{(d)}$ has good reduction at $q$ (for $q$ odd, $d=q^*$
works; for $q=2$, one of $d=-4,8,-8$ works). Then, with $a'=a_q(E^{(d)})$ (its square does not depend on the choice),
$P_q(X)=(1-qX)(1-(a'^2-2q)X+q^2X^2)$ and $e_\ell(E,q)=v_\ell(q-1)+v_\ell((q+1)^2-a'^2)$: the $\mathrm I_0^*$ formula, at every $q$.

(c) *Potentially good with $\rho(I_q)$ cyclic of order $3$, $4$ or $6$*: $A_f^{I_q}$ is a line spanned by $x=2g-\operatorname{tr}g$ ($g$ a generator), $\Phi_q$ acts
on it by a sign $c\in\{\pm1\}$, $P_q(X)=1-cqX$ and $e_\ell(E,q)=v_\ell(q-c)$. For $q\ge5$, $c=\chi_{-3}(q)$ or $\chi_{-4}(q)$ (9.3); for $q=2,3$ the type does not
determine $c$.

(d) *Potentially good with $\rho(I_q)$ non-abelian* ($Q_8$ or $\SL_2(\F_3)$ at $q=2$, $\Z/3\rtimes\Z/4$ at $q=3$; Chapter 11, its 4.6; Kraus90, verify the list): $A_f^{I_q}=0$, $P_q=1$,
$e_\ell(E,q)=0$.

Proof: $\rho(I_q)$ is finite in the potentially good case and lies in $\SL_2$ (Chapter 11). A finite subgroup of the upper triangular
group in characteristic $0$ meets the unipotent radical trivially, so it is abelian; hence a non-abelian finite subgroup of $\SL_2(\overline\Q_\ell)$
is absolutely irreducible and its commutant is the scalars (Schur): (d). A finite abelian subgroup of $\SL_2(\overline\Q_\ell)$ is
diagonalisable, hence cyclic; if it is not in $\{\pm1\}$ its commutant is $\overline\Q_\ell[g]$, of dimension $2$, with trace-zero line spanned by $x$,
and $x^2=(\operatorname{tr}g)^2-4$ is a nonzero scalar; $\Phi_q$ normalises $\rho(I_q)$, hence preserves the line, and $\Phi_qx\Phi_q^{-1}=cx$ with $c^2=1$
because conjugation preserves $x^2$: (c). If $\rho(I_q)=\{\pm1\}$, the character $\theta=\rho|_{I_q}$ is invariant under conjugation by $G_{\Q_q}$ ($-1$ is
central), so $\ker\theta$ is normal in $G_{\Q_q}$ and cuts out a quadratic extension $M$ of $\Q_q^{\mathrm{ur}}$ with $\Gal(M/\Q_q)$ a central extension of
$\hat\Z$ by $\Z/2$, which splits; so $\theta$ extends to a quadratic character $\chi$ of $G_{\Q_q}$, $\rho\otimes\chi$ is unramified, $E\otimes\chi$ has good
reduction (Neron-Ogg-Shafarevich), $\chi$ is the restriction of some $\chi_d$ with $d$ as stated (for $q=2$, the ramified square classes of
$\Q_2^\times$ are represented by $-1,\pm2$ up to the unramified class $5$), and $\ad V=\ad V_\ell E^{(d)}$: (b) by 6.2. (a) is 9.2 and its twist
(Chapter 11, its 3.4, for $q=2$ as well). Consequences for the wild primes: at $q=2$, $e_3(E,2)\in\{0,1,2\}$ ($1$ in cases (a)-additive and
(c) with $c=-1$; $2$ in case (b) with $a'=0$), $e_5(E,2)\in\{0,1\}$ ($1$ exactly in case (b) with $a'=\pm2$), $e_\ell(E,2)=0$ for $\ell\ge7$; at $q=3$,
$e_5(E,3)=1$ exactly in case (b) with $a'=\pm1$, $e_7(E,3)=1$ exactly in case (b) with $a'=\pm3$, and $e_\ell(E,3)=0$ otherwise (since $v_\ell(8)=v_\ell(4/3)=v_\ell(2/3)=0$
for $\ell\ge5$; $|a'|\le2\sqrt q$).
Verified on all curves of conductor below $10{,}000$ (all $64{,}687$, not only optimal ones), counting pairs (curve, $q$):

| $q$ | type | (a) $1-X$ | (b) cubic | (c) $1+qX$ | (c) $1-qX$ | (d) $1$ |
|-|-|-|-|-|-|-|
| $2$ | $\mathrm I_n$ | 25,751 | | | | |
| $2$ | $\mathrm I_m^*$ | 3,732 | 716 | 146 | | 5,073 |
| $2$ | $\mathrm I_0^*$ | | | 792 | | 1,712 |
| $2$ | $\mathrm{II}$ / $\mathrm{II}^*$ | | 136 / 291 | 469 / 108 | | 1,109 / 1,267 |
| $2$ | $\mathrm{III}$ / $\mathrm{III}^*$ | | | 42 / 42 | 56 / 56 | 2,012 / 2,202 |
| $2$ | $\mathrm{IV}$ / $\mathrm{IV}^*$ | | | 2,094 / 2,656 | | |
| $3$ | $\mathrm I_n$ / $\mathrm I_n^*$ | 25,283 / 7,805 | | | | |
| $3$ | $\mathrm I_0^*$ | | 2,283 | | | |
| $3$ | $\mathrm{II}$ / $\mathrm{II}^*$ | | | 145 / 91 | 135 / 86 | 986 / 699 |
| $3$ | $\mathrm{III}$ / $\mathrm{III}^*$ | | | 1,553 / 1,553 | | |
| $3$ | $\mathrm{IV}$ / $\mathrm{IV}^*$ | | | 91 / 145 | 86 / 135 | 699 / 986 |

Every cubic factor ($1{,}143$ at $2$, $2{,}283$ at $3$) equals the formula of (b) for a twist $E^{(d)}$ with good reduction found by `elltwist`,
and no curve without such a twist has a cubic factor; at $2$, $\mathrm I_m^*$ has $P_2=1-X$ exactly when $v_2(j)<0$. No factor of degree $2$ occurs.
Examples: 1232l1 $=$ 77a1 $\otimes\chi_{-4}$, $a_2(\text{77a1})=0$, $P_2=(1-2X)(1+2X)^2$, $e_3(E,2)=v_3(9/8)=2$, $\degphi=288=2^5\cdot3^2$ (point 50's cubic,
explained); 592c1 $=$ 37a1 $\otimes\chi_{-4}$, $a_2(\text{37a1})=-2$, $P_2=(1-2X)(1+4X^2)$, $e_5(E,2)=v_5(5/8)=1$, $\degphi=80$ (the prime $2$ contributes at
$\ell=5$; all $93$ optimal curves below $10{,}000$ with this factor, $5\nmid N$ and $E[5]$ irreducible have $5\mid\degphi$); 336f1 (type $\mathrm{II}$ at $2$, case (c),
$P_2=1+2X$, $e_3=1$, $\degphi=24$; point 50); every type $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ is case (c) with $c=\chi_{-3}(2)=-1$ (Chapter 11, its 4.4; point 43).
Reference: elementary given Chapters 7, 11; SerreTate68. Paper: Remark rem:wild, Section sec:wild ("Definition def:terms with
PARI's factor explains every one of these minima"), Proposition prop:forms, Conjecture conj:euler (the terms at $2$, $3$), the
Remark after Theorem thm:quant and point 60 (the $\mathrm I_0^*$ formula at $q=3$: case (b)).

**10.2 `rem:lfunctions:rem-wild-status`** (remark; P for the statuses, by 10.1 and the data). The sentences of Remark rem:wild, one by
one: (i) "At $q=2,3$ the Kodaira type does not determine $L_q(A_f,s)$, but PARI does": true (10.1 table); 10.1 says what does determine
it (the shape of $\rho(I_q)$ and $c$ or $a'$). (ii) "a type $\mathrm{IV}$ at $2$ has $P_2(X)=1+2X$ and $e_3=1$": a theorem (Chapter 11, its 4.4; point 43;
case (c) of 10.1). (iii) "a type $\mathrm{II}$ at $2$ has $P_2=1$ and $e_3=0$": false in general (point 50; 336f1, 1232l1; all four shapes occur for
type $\mathrm{II}$ at $2$). (iv) "a type $\mathrm I_n^*$ at $2$ has potentially good reduction in about half of the cases, with a cubic $P_2$ and $t_\ell=0$":
below conductor $10{,}000$, $5{,}935$ of the $9{,}667$ pairs (61%) are potentially good, and among them the cubic occurs for $716$ only ($P_2=1$
for $5{,}073$, $1+2X$ for $146$); the cubic there always has $a'=\pm1$, so it contributes nothing for odd $\ell$; $t_\ell=0$ is right (point 50).
(v) "At $q=\ell$ the Euler factor is not the relevant quantity": consistent with Definition def:terms ($q\ne\ell$); $t_\ell$ is used at $q=\ell$ (point 53).
Paper: Remark rem:wild; Section sec:wild.

### Section 11. Computing the factors: PARI and `rule(E, l)`

**11.1 `rem:lfunctions:pari`** (remark; P as a computation). `S = lfunsympow(E, 2)` is the $L$-function $L(\Sym f,s)$ of C4 (motivic
weight $3$; `lfunparams(S)` $=$ `[N_sym, 3, [0, 0, 1]]`, 7.2), with the true factors at every prime; `lfuneuler(S, q)` is $1/P_q(x)$, $x=q^{-s}$
(C5); `lfun(S, 2)` is $L(\Sym f,2)=L(\ad f,1)$. Hence $e_\ell(E,q)$ = `valuation(subst(1/lfuneuler(S,q), x, 1/q^2) / (1 - a_q^2/q^2), l)` (9.1). The bad
factors are computed by Watkins's method (Watkins02; cite the section, verify; Coates-Schmidt for the potentially good types at
$q\ge5$, verify). How to install and call PARI, `lfuncreate`, precision and memory are Chapter 22's. Paper: Section 1.1 ("PARI's
`lfunsympow(E,2)` returns these factors at every prime, including $2$ and $3$"), Section sec:data, the appendix.

**11.2 `ex:lfunctions:rule`** (worked example; P as a computation). The mathematical content of the appendix function: for $q\ne\ell$,
`r` $=P_q(q^{-2})=L_q(A_f,1)^{-1}$ (9.1), divided by $1-q^{-2}$ when the code `k` $\ge5$ (type $\mathrm I_n$, $n\ge1$: the naive factor is the true one,
9.2), and `e` $=v_\ell$(`r`) $=e_\ell(E,q)$, except for the codes $\pm3$ ($\mathrm{III},\mathrm{III}^*$) unless `iii` $=1$; for $q=\ell=3$ the weights $w_3$ of
Conjecture conj:euler; `t` $=t_\ell(E,q)$ from `valuation(j, q)` at every $q$, including $q=\ell$ (point 53); finally `ns3` $=h_3(E)$ subtracted when
`iii` $=1$ (Chapter 11, its 8.4, 8.5). At an additive $q$ no division is made because the naive factor is $1$ ($a_q=0$), exactly as in
Definition def:terms. Values, recomputed with PARI 2.17.2: 121a1 returns `[1, 1]` ($q=11$, type $\mathrm{II}$: `r` $=12/11$, `e` $=1$, `t` $=0$;
$\degphi=6$); 726a1 $=[1,1,0,-35,-51]$ returns `[2, 2]` both with `iii` $=0$ and `iii` $=1$ ($q=2$, $\mathrm I_6$: `r` $=1$, `t` $=v_3(6)=1$; $q=3=\ell$, $\mathrm I_3$: $w_3=0$, `t` $=1$;
$q=11$, $\mathrm{III}$: `r` $=12/11$, `e` $=1$ only with `iii`, cancelled by `ns3` $=1$ (image 3Ns); $\degphi=144=2^4\cdot3^2$). The line-by-line reading, the Kodaira
codes and the data protocol are Chapter 22's. Paper: the appendix; Conjecture conj:euler; Section sec:anomaly.

### Section 12. Worked examples

**12.1 `ex:lfunctions:examples`** (worked example; P as a computation; PARI and Cremona's `degphi`). Bad primes with type, $P_q$,
$P_q(q^{-2})$; $\degphi$; $B_E=\degphi/\prod_{q^2\mid N}P_q(q^{-2})$ (8.4), which agrees with $N\,L(\ad f,1)/(2\pi\operatorname{vol}\Lambda_E)$ numerically in every row.

| curve | bad primes: type, $P_q(X)$, $P_q(q^{-2})$ | nonzero $e_\ell$ | $\degphi$ | $B_E$ | remark |
|-|-|-|-|-|-|
| 11a1 | $11$: $\mathrm I_5$, $1-X$ | none | $1$ | $1$ | $t_5(E,11)=1$ |
| 121a1 | $11$: $\mathrm{II}$, $1+11X$, $12/11$ | $e_3=1$ | $6$ | $11/2$ | paper's Example (b); `rule` $[1,1]$ |
| 121c1 | $11$: $\mathrm{IV}$, $1+11X$, $12/11$ | $e_3=1$ | $6$ | $11/2$ | twist of 121a1 by $\chi_{-11}$ |
| 147b1 | $3$: $\mathrm I_1$; $7$: $\mathrm{IV}^*$, $1-7X$, $6/7$ | $e_3(7)=1$ | $42$ | $49$ | $\chi_{-3}(7)=+1$ |
| 200a1 | $2$: $\mathrm{II}^*$, $1$; $5$: $\mathrm{IV}^*$, $1+5X$, $6/5$ | $e_3(5)=1$ | $120$ | $100$ | surjective mod $\ell$ images |
| 350e1 | $2$: $\mathrm I_{11}$; $5$: $\mathrm{II}^*$, $1+5X$, $6/5$; $7$: $\mathrm I_2$ | $e_3(5)=1$ | $1320$ | $1100$ | $t_{11}(E,2)=1$ |
| 726a1 | $2$: $\mathrm I_6$; $3$: $\mathrm I_3$; $11$: $\mathrm{III}$, $1+11X$, $12/11$ | $e_3(11)=1$ | $144$ | $132$ | 3Ns, $h_3=1$; `rule` $[2,2]$ |
| 539c1 | $7$: $\mathrm I_3^*$, $1-X$, $48/49$; $11$: $\mathrm I_2$ | $e_3(7)=1$ | $288$ | $294$ | paper's Example (c), $\ell=3$ |
| 539d1 | $7$: $\mathrm I_0^*$, $(1-7X)(1+10X+49X^2)$, $360/343$; $11$: $\mathrm I_1$ | $e_3=2$, $e_5=1$ | $72$ | $343/5$ | $E'=$ 11a3, $a'=-2$; $E[5]$ reducible |
| 980i1 | $2$: $\mathrm{IV}^*$, $1+2X$, $3/2$; $5$: $\mathrm I_1$; $7$: $\mathrm I_5^*$, $48/49$ | $e_3(2)=e_3(7)=1$ | $2880$ | $1960$ | paper's Example (c), $\ell=5$: $t_5=1$ |
| 275b1 | $5$: $\mathrm I_0^*$, $(1-5X)(1+9X+25X^2)$, $28/25$; $11$: $\mathrm I_1$ | $e_7(5)=1$ | $28$ | $25$ | $a'=\pm1$ |
| 1232l1 | $2$: $\mathrm{II}^*$, $(1-2X)(1+2X)^2$, $9/8$; $7$: $\mathrm I_2$; $11$: $\mathrm I_1$ | $e_3(2)=2$ | $288$ | $256$ | 77a1 $\otimes\chi_{-4}$ |
| 592c1 | $2$: $\mathrm{II}^*$, $(1-2X)(1+4X^2)$, $5/8$; $37$: $\mathrm I_1$ | $e_5(2)=1$ | $80$ | $128$ | 37a1 $\otimes\chi_{-4}$ |
| 336f1 | $2$: $\mathrm{II}$, $1+2X$, $3/2$; $3$: $\mathrm I_1$; $7$: $\mathrm I_2$ | $e_3(2)=1$ | $24$ | $16$ | point 50 |
| 52a1 | $2$: $\mathrm{IV}^*$, $1+2X$, $3/2$; $13$: $\mathrm I_2$ | $e_3(2)=1$ | $3$ | $2$ | Chapter 15's case (a) at $q=2$ |
| 98a1 | $2$: $\mathrm I_2$; $7$: $\mathrm I_1^*$, $48/49$ | $e_3(7)=1$ | $16$ | $49/3$ | $E[3]$ reducible: bound fails |
| 121b1 | $11$: $\mathrm{III}$, $1+11X$, $12/11$ | $e_3=1$ | $4$ | $11/3$ | CM by $\Q(\sqrt{-11})$: bound fails |
| 121d1 | $11$: $\mathrm I_1^*$, $1-X$, $120/121$ | $e_3=e_5=1$ | $24$ | $121/5$ | $E[5]$ reducible |

Reading: whenever $\ell$ is odd, $\ell\nmid N$ and the hypothesis of Theorem thm:main holds, $v_\ell(B_E)\ge0$ in this table; the four rows with
$v_\ell(B_E)<0$ are exactly where the hypothesis fails (reducible $E[\ell]$, or CM with induced mod $3$ image). Paper: the Example of
Section 3, the appendix, Sections sec:iso, sec:wild, sec:eis.

**12.2 `ex:lfunctions:petersson-table`** (worked example; P as a computation). For 11a1, 14a1, 20a1, 27a1, 36a1, 49a1, 50a1, 64a1,
99a1, 121a1, 121c1, 121d1, 162a1, 52a1, 80a1: $\langle f,f\rangle$ (unnormalised; e.g. 11a1: $0.04690014787349518782$, 20a1:
$0.08134945682538172856$, 27a1: $0.06846465111921223464$, 49a1: $0.12524576465640295885$, 121a1: $0.42823936001195717857$, 121d1:
$0.51163797680176568534$), the correction $\prod_{p^2\mid N}P_p(p^{-2})$ ($1,1,3/2,1,2,8/7,6/5,1,4/3,12/11,12/11,120/121,4/3,3/2,1$), the ratio of $\langle f,f\rangle$ to the
right side of 8.3 ($1$ to $10^{-15}$ in every case), and $N L^{\nv}(\ad f,1)/(2\pi\operatorname{vol}\Lambda_E)=\degphi$ ($1,1,1,1,1,1,2,2,4,6,6,24,12,3,4$). $L(\Sym f,2)$ for
11a1 is $1.05759924459096\ldots$ (as in Chapter 13, its 10.3). Paper: Section 1 (Zagier, Watkins, Rankin, Shimura).

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2 with its tag and `\Cref`; C2, C3, C4, C6 restated in one line each; the table of 9.3 in compact form | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1 (naive versus true, Petersson norm, Zagier, Watkins, Rankin, Shimura, Flach, DFG04 Lemma 2.12; point 30); Section 1.1 ($\delta_p$, $L_p$, $L_p^{\nv}$, `lfunsympow`, the shift); Definition def:terms and the table; Lemma lem:euler; Remark rem:wild and Section sec:wild; Theorem thm:dfg14 and the paragraph after it; Lemma lem:fpr ($L$-part) and the paragraph after Lemma lem:dfg21; the proof of Theorem thm:main (cancellation); Theorem thm:quant Step 3 and the Remark after it; Proposition prop:forms; Conjecture conj:euler; the appendix (`rule`) | 50 |
| 1 | Introduction and conventions | what the chapter is for; the physics asides; C1 to C10 as `convention` environments; a `warning` on the two Frobenii (point 11) | 110 |
| 2 | Dirichlet series and Euler products | 2.1 to 2.3; the primon aside; Mellin transform | 100 |
| 3 | $\zeta$, Dirichlet $L$-functions, Dedekind zeta | 3.1 to 3.4; theta function and Poisson summation; $\zeta(2)$; $L(1,\chi_{-4})$, $L(1,\chi_{-3})$; $\zeta_{\Q(i)}$, $\zeta_{\Q(\sqrt{-3})}$ | 190 |
| 4 | $L$-functions of $\ell$-adic representations | 4.1 to 4.4; local factors recalled from Chapter 7; compatible systems; convergence and weights; the finite-inertia examples | 140 |
| 5 | The $L$-function of $E$ | 5.1, 5.2; functional equation and root number; examples 11a1, 37a1 | 90 |
| 6 | Adjoint and symmetric square | 6.1, 6.2; the shift by one; $P_p$; Wiles's factor and Ribet's condition; `paperlink`: Section 1.1, Theorem thm:dfg14 | 120 |
| 7 | Analytic theory, normalisations, critical values | 7.1 to 7.4; the normalisation table; conductor of $\ad$ by type; Deligne's conjecture in one paragraph | 140 |
| 8 | Naive versus true; Rankin-Selberg; Petersson norm and modular degree | 8.1 to 8.6; the `warning` on "the Euler product of $\sum a_n^2n^{-s}$" (point 30); the proof of 8.3 from Chapter 13; the identity 8.4(iii) and its reading 8.5; Flach | 230 |
| 9 | The local terms and Lemma lem:euler | 9.1 to 9.7; the full proof of Lemma lem:euler in five steps; the table with $P_q$; twists (point 15); Lemma lem:fpr's $L$-part; the naive factors of Theorem thm:dfg14; `paperlink` for each paper item | 300 |
| 10 | Every prime, including $2$ and $3$ | 10.1 with proof and the data table; 10.2 (Remark rem:wild sentence by sentence, points 43, 50) | 150 |
| 11 | Computing the factors | 11.1, 11.2 (`lfunsympow`, `lfuneuler`, the mathematics of `rule`); pointer to Chapter 22 | 70 |
| 12 | Worked examples | 12.1, 12.2 (the two tables, with a short reading) | 90 |
| 13 | Exercises | the 18 exercises of Part 4.2 | 150 |
| 14 | Notes and references | Davenport, Washington, SerreCourse, Neukirch, Rankin39, Selberg40, Shimura75, Shimura76, GelbartJacquet, Deligne79, Sturm80, Flach92, Zagier85, Watkins02, CoatesSchmidt87, DFG04, Kraus90, SerreTate68, Tate79, Rohrlich94, PARI; which numbers were cited and which are marked (verify) | 45 |
| | **total** | | **1,975** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| Dirichlet series and their convergence | 2.1 |
| Euler products | 2.2 |
| Riemann zeta: Euler product, continuation and functional equation via theta functions, Mellin transforms (physics) | 2.3, 3.1 |
| Dirichlet $L$-functions: definition, Euler product, functional equation, $L(1,\chi)\ne0$, Dirichlet's theorem | 3.3 |
| Dedekind zeta function and its factorisation for abelian fields | 3.4 |
| $L(E,s)$: local factors at good, multiplicative ($a_p=\pm1$), additive primes; the conductor | 5.1 (conductor: Chapter 10) |
| completed $\Lambda(E,s)$, functional equation with root number, as a consequence of modularity; $L(E,s)=L(f_E,s)$ | 5.2 |
| $L$-functions of $\ell$-adic representations: $L_p(V,s)=\det(1-\Frob_pp^{-s}\mid V^{I_p})^{-1}$ for $p\ne\ell$; at $p=\ell$ via $D_{\mathrm{cris}}$ | 4.1 |
| the Weil-Deligne definition, independence of $\ell$; conjecture and theorem (modular forms) | 4.1, 4.2 |
| the $L$-function of a representation with finite image of inertia (the three Kodaira cases) | 4.4, 9.3 |
| adjoint and symmetric square $L$-functions: definitions; $\ad\rho=\Sym\rho\otimes\det^{-1}$; $L(\Sym f,s)=L(\ad f,s-1)$ | 6.1 |
| normalisations in Shimura, Gelbart-Jacquet, DFG04, PARI | 7.4 (with 7.1, 8.2(B), 11.1) |
| the naive adjoint $L$-function and the Rankin-Selberg convolution (PLAN's formula corrected: Part 7, B-a) | 8.1, 8.2, 7.4 |
| $L_p^{\nv}=L_p$ when $\delta_p>0$, $=1$ when $\delta_p=0$, and why (built from $a_p$ alone) | 8.1 |
| the Rankin-Selberg method (unfolding) and the theorem of Rankin and Shimura with the exact factors at bad primes | 8.3 (unfolding: Chapter 13, 10.3) |
| the true local factors at bad primes: the paper's table derived in full (Lemma lem:euler), each Kodaira type at $q\ge5$ | 9.2, 9.3, 9.4 |
| the invariant line spanned by $\sqrt{-3}$ in $\Z_\ell[\zeta_3]$ (corrected, point 12), by $\tau$ for $\mathrm{III}$ (point 34) | 9.3 |
| $\mathrm I_0^*$: $V=V'\otimes\chi_q$, $L_q(A_f,1)^{-1}=\frac{q-1}q\frac{(q+1)^2-a_q(E')^2}{q^2}$ | 6.2, 9.3 |
| the wild primes $2$ and $3$ (type does not determine the factor; the examples of Remark rem:wild) | 10.1, 10.2 |
| how PARI computes these (`lfunsympow(E,2)`, `lfuneuler`, $P_q$, $e_\ell=v_\ell(P_q(q^{-2})/(1-a_q^2q^{-2}))$) | 11.1, 11.2 |
| the definition of $e_\ell(E,q)$ (Definition def:terms) "and its invariance under quadratic twist" (false for $e_\ell$: point 15) | 9.1, 9.5 |
| Flach's theorem on the finiteness of the Selmer group of $\Sym^2$ | 8.6 |
| special values and the Bloch-Kato conjecture for the adjoint (one page); connection to the modular degree via the Petersson norm | 8.4, 8.5 (precise statements: Chapter 18) |
| Deligne's conjecture on critical values (one paragraph) | 7.3 |
| functional equation and analytic continuation of $L(\Sym f,s)$ (Shimura; Gelbart-Jacquet) | 7.1, 7.2 |
| Section 6 row: Euler factors of the adjoint, naive versus true, $\delta_p$, $P_q(X)$, $e_\ell(E,q)$ | 6.1, 8.1, 9.1 to 9.7, 10.1 |
| Section 6 row: Petersson norm, Rankin-Selberg, $L(\Sym f,2)$, Zagier, Watkins, Flach (with 12, 13, 14) | 8.2 to 8.6, 12.2 |
| Section 6 row: level raising, Wiles's level-raising factor (with 15, 20) | 6.2, 9.7 |
| hook: Section 1 (Petersson norm, Zagier, Watkins, Rankin, Shimura, Flach, naive versus true, DFG04 Lemma 2.12) | 8.1 to 8.6 |
| hook: Section 1.1 ($\delta_p$, $L_p(A_f,s)$, the naive factor, `lfunsympow`, Definition def:terms, the table) | C1 to C6, 6.1, 8.1, 9.1, 9.3, 11.1 |
| hook: Lemma lem:euler (in full) | 9.3 (with 9.2, 6.2, 10.1) |
| hook: Remark rem:wild | 10.1, 10.2 |
| hook: Theorem thm:dfg14 and the paragraph after it (the naive factors) | 6.2, 9.2, 9.7 |
| hook: Lemma lem:fpr ($L_p(A_f,1)^{-1}=L_p(A_f(1),0)^{-1}$, an $\ell$-adic integer of valuation $e_\ell$ or $v_\ell(1-p^{-2})$) | 9.6 |
| hook: the appendix (`rule(E, l)`) | 11.2, 12.1 |
| also: proof of Theorem thm:main (cancellation of the naive factors); Theorem thm:quant Step 3; the Remark after thm:quant, (1), (3) | 9.7, 9.4, 9.5 |
| also: Proposition prop:forms (proof: $e_3=v_3(q-\chi_{-3}(q))\ge1$; the exception at $2$, point 43) | 9.4, 10.1(c) |
| also: Conjecture conj:euler and Section sec:wild (terms at $2$, $3$; $t_\ell$ at $q=\ell$, point 53) | 9.1, 10.1, 11.2 |
| also: Section sec:iso ("Multiplicative primes show no Euler term"), Section sec:sharp ("the size of the Petersson norm") | 9.2, 8.4 |
| also: important_notes.md points 11, 12, 15, 30, 34, 43, 50, 52, 53, 60; B1, B6, B7, B9, B10 | C2, 4.1(iii), 9.2, 9.6; 9.3; 9.5; 8.2; 9.3; 10.1, 10.2; 10.1, 10.2; C8, 11.2; 9.1, 11.2; 10.1(b); C2; C2 (Chapter 7's convention); C3; C3, 5.1; 8.4 (Chapter 14's formula) |
| also: what Chapters 2, 4, 6, 7, 9 to 15 deferred here | 9.4, 12.1 (Chapter 2); 6.1 (Chapter 4); C2, C3 (Chapter 6); 4.1, 4.4, 9.2, 9.3, 10.1 (Chapter 7); 5.1, 5.2 (Chapter 9); 9.3, 10.1 (Chapters 10, 11); 8.3 (Chapters 12, 13); 8.4 (Chapter 14); 8.1 (Chapter 15) |

### 4.2 Exercises (Section 13 of the chapter), graded from easy to harder

1. Prove $\zeta(s)\zeta(s-1)=\sum\sigma(n)n^{-s}$ and $\zeta(s)^2=\sum d(n)n^{-s}$ from the Euler products, and deduce $\zeta^{(N)}(s)=\zeta(s)\prod_{p\mid N}(1-p^{-s})$.
2. Show $L(1,\chi_{-4})=\pi/4$ and write down the Euler factors of $\zeta_{\Q(i)}$ at $2$, $3$, $5$; check that they are those of $\zeta(s)L(s,\chi_{-4})$.
3. (Mellin.) Show $\int_0^\infty(\theta(y)-1)y^{s/2-1}dy=2\pi^{-s/2}\Gamma(s/2)\zeta(s)$ and complete the proof of 3.1(iv) from $\theta(1/y)=\sqrt y\theta(y)$.
4. Prove $L_p(M(1),s)=L_p(M,s+1)$ with the geometric Frobenius, and that the arithmetic one would give $L_p(M,s-1)$. Check the paper's
   claim that at a multiplicative prime "$(\ad V)^{I_q}$ is a line with eigenvalue $q^{-1}$", and say for which Frobenius it holds.
5. Prove $\operatorname{Sym}^2V^\vee\simeq\ad V(-1)$ for $V=V_\ell E$, and check the paper's claim that $L_p(\Sym f,s)=L_p(A_f,s-1)$ at a good prime by
   computing both sides from $\alpha,\beta$.
6. Prove the identities $\sum_ka_{p^k}^2X^k=\frac{1+pX}{(1-\alpha^2X)(1-pX)(1-\beta^2X)}$ and $\sum_ka_{p^{2k}}X^k=\frac{1-p^2X^2}{(1-\alpha^2X)(1-pX)(1-\beta^2X)}$. Check the paper's claim
   that the naive adjoint $L$-function is "the Euler product of $\sum a_n(f)^2n^{-s}$" on 11a1 at $p=2$ (coefficients $4$ and $2$), and state the
   correct relation.
7. Check the paper's claim that $\langle f,f\rangle$ is $L(\Sym f,2)$ "up to the local factors at the bad primes": derive 8.3 from the residue
   formula of Chapter 13 and verify it numerically for 20a1 and 27a1 with PARI (`mfpetersson` times $\mu(N)$, `lfun(lfunsympow(E,2),2)`).
8. Using 8.4, compute $B_E$ for 121a1 and 539c1 and check that $v_3(\degphi)=v_3(B_E)+\sum e_3(E,q)$.
9. Check the paper's claim that for type $\mathrm I_0^*$, $L_q(A_f,1)^{-1}=\frac{q-1}q\cdot\frac{(q+1)^2-a_q(E')^2}{q^2}$, and show that it does not depend on which ramified
   quadratic twist $E'$ of good reduction is chosen. Compute it for 539d1 at $7$ ($E'=$ 11a3).
10. Prove that the trace-zero commutant of a cyclic subgroup $\langle g\rangle\subset\SL_2(\overline\Q_\ell)$, $g\ne\pm1$, of finite order is the line spanned by
    $2g-\operatorname{tr}g$, and that any element normalising $\langle g\rangle$ acts on it by $\pm1$. Deduce the $\mathrm{III}$ row of the table without
    diagonalising $\tau$ (point 34).
11. Check the paper's claim that "a type $\mathrm{IV}$ at $2$ has $P_2(X)=1+2X$ and $e_3=1$" from 10.1(c) and Chapter 11, and that "a type $\mathrm{II}$
    at $2$ has $P_2=1$" fails for 336f1 and 1232l1. Identify 1232l1 as a twist of 77a1 and compute $e_3(E,2)=2$ from the $\mathrm I_0^*$ formula.
12. Check the paper's claim that "Both terms are invariant under quadratic twist" (Definition def:terms): prove it for $t_\ell$ and
    disprove it for $e_\ell$ with 11a1 and 121d2. Show that $v_\ell(L_q(A_f,1)^{-1})$ is invariant.
13. Check the paper's claim in Lemma lem:fpr that $L_p(A_f,1)^{-1}$ is a nonzero $\ell$-adic integer of valuation $e_\ell(E,p)$ at an additive
    prime and $v_\ell(1-p^{-2})$ at a multiplicative one; where is the Hasse bound used?
14. Check the paper's claim after Theorem thm:dfg14 that adding a good prime multiplies the ideal by Wiles's level-raising factor:
    compute $L_p^{\nv}(A_f,1)^{-1}$ for 11a1 at $p=7$ and find the primes $\ell$ dividing it; relate $a_7\equiv\pm8\pmod\ell$ to Ribet's condition.
15. For $\ell=3$, list the residue classes of $q\ge5$ modulo $12$ for which each additive type gives $e_3(E,q)\ge1$, and check the paper's
    claim (Remark after Theorem thm:quant, (1)) that a prime of type $\mathrm I_0^*$ with $q\equiv1\pmod3$ forces $3\mid\degphi$ at the level of the
    Euler factor.
16. Show that the critical integers of $L(\ad f,s)$ are $0$ and $1$ from $\Gamma_\R(s+1)\Gamma_\C(s+1)$, and deduce from 8.3 that $L(\ad f,1)/(\pi^3\langle f,f\rangle)\in\Q^\times$.
17. Compute $B_E$ for 98a1, 121b1, 121d1 and 539d1, find the primes $\ell$ with $v_\ell(B_E)<0$, and explain each by the failure of a
    hypothesis of Theorem thm:main.
18. Run `rule` on 121a1 and 726a1 (with and without `iii`) and account for each term with Sections 9 to 11; explain why the type $\mathrm{III}$
    term and the correction cancel for 726a1.

## 5. Dependencies and forward pointers

Results from earlier chapters used here (by chapter label only):
* Chapter 2 (`ch:rings`): Dirichlet characters, Gauss sums, $\chi_{-3}$, $\chi_{-4}$, $\chi_{q^*}$; the valuations 11.3 to 11.5 and the identity 11.4
  (used in 6.2, 9.3, 9.4, 10.1).
* Chapter 4 (`ch:reps`): $\ad V$, commutants of cyclic and non-abelian groups, Schur, $\operatorname{Sym}^2W\simeq\ad W\otimes\det W$ (7.5), the trace form (7.6);
  used in 6.1, 9.3, 9.6, 10.1.
* Chapter 6 (`ch:ant`): Dedekind domains, splitting of primes in quadratic fields (3.4), Frobenius elements and the geometric
  convention (3.7).
* Chapter 7 (`ch:local`): conventions L3, L6; 5.6 ($\Frob\,g\,\Frob^{-1}=g^q$ on tame inertia); 6.3 (quadratic characters of $\Q_q$); 8.1, 8.2
  ($L$-factors); 8.4 (conductors); 9.1 to 9.5 (the shapes and their adjoints).
* Chapter 9 (`ch:ellcurves`): $a_p$, $\alpha$, $\beta$, the Hasse bound, $L(E,s)$ as an Euler product, quadratic twists.
* Chapter 10 (`ch:reduction`): Kodaira types, Tate's algorithm, Kraus's theorem (R), Lemma lem:twist (i), (ii), PARI's codes, the
  conductor.
* Chapter 11 (`ch:galrep`): 3.2 (Tate shape), 3.4 (potentially multiplicative), 3.5 ($\delta_p$), 4.1 (inertia images at $q\ge5$), 4.4
  (types $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$), 4.6 (wild inertia), 8.4, 8.5 (3Ns, $h_3$).
* Chapter 12 (`ch:modforms`): the Petersson product (C5), $\mu(N)$, $W_N$.
* Chapter 13 (`ch:hecke`): $L(f,s)$ and its functional equation (10.1, 10.2), the Rankin-Selberg residue (10.3(i)).
* Chapter 14 (`ch:moddeg`): modularity; the Zagier-Watkins formula with $c^2$ in the numerator (7.3; B10); $c_E=1$ on the tables.
* Chapter 15 (`ch:modgalrep`): local-global compatibility (3.4), the local types and $\delta_p$ (3.5), the naive-factor corollary (3.7).
* Chapters 17, 18 (`ch:galcoh`, `ch:blochkato`, being outlined in parallel): only as forward black boxes in 8.5, 8.6 and 9.6
  ($H^1_{\mathrm{ur}}$, Bloch-Kato Selmer groups, Tamagawa factors, DFG04 Theorem 0.1); never used in a proof here.

Forward pointers (chapters that use this one):
* Chapter 18 (`ch:blochkato`): 9.6 (the $L$-part of Lemma lem:fpr, $\det(1-\Phi_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}\ne0$), 8.5 (the Bloch-Kato reading),
  8.6 (Flach), C3 ($L_p(M(1),s)=L_p(M,s+1)$). Chapter 18 owns Bloch-Kato, the Tamagawa factors, the Tamagawa number conjecture,
  DFG04 Theorems 0.1, 0.2, 2.7, Lemma 2.1 and the Fitting-ideal half of Lemma lem:fpr.
* Chapter 20 (`ch:congruence`): 9.7 (the naive factors at $s=1$ and the cancellation), 6.2 (Wiles's factor), 9.5 ($A_g=A_f$), 9.3 (the
  values in Theorem thm:quant Step 3). Chapter 20 owns DFG04 Proposition 1.4 (Theorem thm:dfg14) and the congruence ideals.
* Chapter 21 (`ch:paper`): 9.1 (Definition def:terms, corrected), 9.3 (Lemma lem:euler), 10.2 (Remark rem:wild, sentence by sentence),
  8.2 (point 30), 8.4 (the identity behind Theorem thm:main), 12.1 (the paper's numerical examples).
* Chapter 22 (`ch:computation`): 11.1 (the normalisation of `lfunsympow` and `lfuneuler`), 11.2 (what `rule` computes), 12.1. Chapter 22
  owns PARI usage, the line-by-line reading of `rule`, the data protocol and `ellmoddegree`.
* Appendix B (`ch:notation`): C2, C4, the normalisation table 7.4.

## 6. Notes for the writer

### 6.1 Conventions to state (Section 1 of the chapter, as `convention` environments)

* C2 and C3 in one `convention` box, with the dictionary "arithmetic eigenvalue $\lambda$ = geometric eigenvalue $\lambda^{-1}$" and the four
  displays $L_p(\Q_\ell(1),s)=(1-p^{-1-s})^{-1}$, $L_p(V_\ell E^\vee,s)=L_p(E,s)$, $L_p(V_\ell E,s)=L_p(E,s+1)$, $L_p(A_f,s)^{-1}=1-p^{-1-s}$ at a multiplicative $p$.
  State, as in Chapters 7, 9, 11: on $V_\ell E$ the **arithmetic** Frobenius has eigenvalues $\alpha,\beta$ (B1, B9; the Chapter 21 outline's
  C2(b) still has the opposite, which its writer must fix).
* C4 and C6 together, then the normalisation table 7.4 as soon as all its objects are defined (end of Section 7 or Section 8).
* The variable: $L(\ad f,s)$ at $s=1$ and $L(\Sym f,s)$ at $s=2$ are the same number; write both every time a value appears, as the
  paper does ($L_q(A_f,1)^{-1}=P_q(q^{-2})$).
* Petersson product unnormalised (C9); say once that PARI's `mfpetersson` divides by $\mu(N)$.
* Characters by discriminant ($\chi_{-3}$, $\chi_{-4}$, $\chi_{q^*}$); say once that the paper's $\chi_q$ is $\chi_{q^*}$.

### 6.2 Pitfalls

* **Frobenius.** The table needs $\Phi$ (row $\mathrm I_n$: $1-q^{-1-s}$, not $1-q^{1-s}$); Lemma lem:tamfactor uses $\Frob$ (point 11). Rows $\mathrm{II}$ to
  $\mathrm{III}^*$ and $\mathrm I_0^*$ are the same for both (inversion-stable eigenvalues); say so, so that the reader sees exactly where the choice
  matters.
* **Sym versus ad.** $L(\Sym f,s)=L(\ad f,s-1)$ in weight $2$; for weight $k$ the shift is $k-1$. Never call the Rankin series
  "$L(\Sym f,s)$"; never call $\zeta^{(N)}(2s-2)\sum a_{n^2}n^{-s}$ the true symmetric square (it is the naive one, 8.2(B)).
* **Point 30.** The paper's "the Euler product of $\sum a_n(f)^2n^{-s}$" must be quoted in a `warning` with the exact relation 8.2(A). PLAN.md's
  "$L(f\times f,s)/\zeta_N(2s-2)$" is also wrong (Part 7, B-a): with $L(f\times f,s)=\zeta^{(N)}(2s-2)\sum a_n^2n^{-s}$ one has
  $L^{\nv}(\Sym f,s)=L(f\times f,s)/\zeta^{(N)}(s-1)$. Do not reproduce PLAN's formula.
* **Naive factor only at bad primes.** The formula $1-a_q^2q^{-2}$ of Definition def:terms is the naive factor at $s=1$ only for $q\mid N$; at a
  good prime the naive factor is the cubic of 6.2.
* **"The diagonal element"** (type $\mathrm{III}$): write $\tau$ (point 34). **"$\Z_\ell[\zeta_3]\simeq\End_{I_q}(V)$"**: write $\End_{I_q}(T)=\Z_\ell\otimes\Z[\zeta_3]$ and
  $\End_{I_q}(V)=\Q_\ell\otimes\Q(\zeta_3)$, not a field for $\ell\equiv1\pmod3$ (point 12).
* **$a'$ for $\mathrm I_0^*$.** $a'=a_q(E^{(q^*)})$ is defined up to sign by the choice of ramified quadratic character; only $a'^2$ enters.
* **$q\ge5$ is used only for the shape of $\rho(I_q)$** (tame, cyclic, determined by the type). At $q=2,3$ the type does not determine
  the shape (10.1); do not write "type $\mathrm{II}$ at $2$ gives $P_2=1$" (point 50). Type $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ is a theorem (point 43). The
  observation "type $\mathrm{III}$ at $3$ always gives $1+3X$" below conductor $10{,}000$ is data, not a theorem: do not state it as one.
* **$e_\ell$ is not twist-invariant** (point 15); $t_\ell$ and $L_q(A_f,s)$ are. PLAN.md's scope sentence repeats the paper's error (Part 7,
  B-a).
* **$\delta_p$ at $p=\ell$.** $V_\ell E^{I_\ell}$ is not $2$-dimensional at a good $\ell$; define $\delta_p$ for $p\ne\ell$ or with $V_{\ell'}E$ (Part 7, N4).
* **The Rankin-Shimura formula.** Do not attribute the exact form 8.3 to DFG04 Lemma 2.12 without checking it; attribute the
  unfolding to Rankin and Selberg, the bad-prime bookkeeping to this chapter, and cite Shimura76 and Watkins02 by section.
* **$B_E$.** 8.4(iii) is an identity; 8.5 is a reading through Chapters 18 and 20. Never present $v_\ell(B_E)=\len H^1_f+\sum v_\ell\Tam$ as
  proved here, and do not claim that $2\pi\operatorname{vol}(\Lambda_E)/N$ is DFG04's period.
* **Flach.** The hypotheses, the module ($\operatorname{Sym}^2T_pE$ or its dual) and the annihilator must be copied from Flach92; the outline does
  not certify them.
* **Analytic statements.** 7.1 is R; the root number of $L(\ad f,s)$ is not claimed without a reference; "entire in the CM case"
  needs a sentence of justification or a reference.
* **Petersson normalisation.** PARI's `mfpetersson` is normalised by $1/\mu(N)$; the formulas of 8.3, 8.4 use the unnormalised product
  (C9), as Chapters 12 to 14 do.
* **Shimura75 versus Shimura76.** Shimura75 (holomorphy of the symmetric square, Proc. London Math. Soc.) is not the refs.bib key
  `Shimura76` (special values of the zeta functions associated with cusp forms, Comm. Pure Appl. Math.).

### 6.3 What to leave to Chapters 7, 11, 13, 14, 18, 20 and 22

* Chapter 7: the definition of Weil-Deligne representations, $L$-factors and conductors, and the local shapes with their adjoints
  (9.1 to 9.5 there). Cite; Section 9 here only assembles them with the Kodaira dictionary and the valuations.
* Chapter 11: the inertia images by Kodaira type (4.1, 3.2, 3.4), types $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ (4.4), Lemma lem:IV, Remark rem:types, the
  3Ns structure (8.4). Cite.
* Chapter 13: the Euler product and functional equation of $L(f,s)$ and the Rankin-Selberg unfolding (10.1 to 10.3 there). Cite; 8.3 here
  adds only the exact bad factors.
* Chapter 14: the Zagier-Watkins formula and the Manin constant (7.3, 7.4 there); point 39 (Lemma lem:hecke is an equality). 8.4 here
  only combines.
* Chapter 18: Bloch-Kato Selmer groups, Tamagawa factors, the Tamagawa number conjecture, DFG04 Theorem 0.1, the Fitting-ideal half
  of Lemma lem:fpr.
* Chapter 20: DFG04 Proposition 1.4 (Theorem thm:dfg14), the congruence ideals $\eta^\Sigma$, Theorems thm:main and thm:quant.
* Chapter 22: PARI usage, `ellmoddegree`, the line-by-line reading of `rule`, the data protocol and the tables of Section 6 of the
  paper.

### 6.4 How the relevant important_notes.md points are handled

* **Point 11 (geometric Frobenius).** C2, C3, 4.1(iii), 9.2 ("with $\Frob_q$ one would get $1-q^{1-s}$"), 9.6 (the determinant changes by a
  unit, so vanishing is unaffected but the equality needs $\Phi$); Exercise 4.
* **Point 12 ($\End_{I_q}$).** 9.3, Step (2); pitfall.
* **Point 15 ($e_\ell$ not twist-invariant).** 9.1(iii), 9.5 with the 11a1/121d2 example; Exercise 12.
* **Point 30 (the naive $L$-function and $\sum a_n^2n^{-s}$).** 8.2, with the exact global identities (A) and (B) (no correction at bad
  primes), the `warning`, Exercise 6; Part 7, N1 (addendum).
* **Point 34 ($\tau$, not "the diagonal element").** 9.3, Step (2); Exercise 10.
* **Point 43 (types $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$).** 10.1(c), 10.2(ii), 12.1 (52a1, 980i1); cite Chapter 11, 4.4.
* **Point 50 (type $\mathrm{II}$ at $2$).** 10.1 explains every observed factor: the cubic of 1232l1 is the $\mathrm I_0^*$ formula for 77a1 $\otimes\chi_{-4}$;
  10.2(iii), (iv); Exercise 11.
* **Point 52 (Kodaira codes for $n\ge1$).** C8; 11.2.
* **Point 53 ($t_\ell$ at $q=\ell$).** 9.1 defines $t_\ell(E,q)$ at every bad $q$; 11.2 (726a1 at $q=3$).
* **Point 60 ($\mathrm I_0^*$ formula at $q=3$).** 10.1(b) proves it for every $q$ (including $2$ and $3$) whenever the inertia image is $\{\pm1\}$;
  all $2{,}283$ cases at $3$ checked.
* **B1, B7, B9 (which Frobenius has $\alpha,\beta$; the Euler factor of $E$).** C2, C3, 5.1(i) state them correctly.
* **B6 (Weil-Deligne relation).** Not restated; C2 refers to Chapter 7's L4.
* **B10 (Manin constant in the numerator).** 8.4(i) has $c_\varphi^2$ on the right side with $\deg\varphi$ on the left, consistent with Chapter 14's
  7.3.
* Adjacent points: 18 (the $\mathrm I_n^*$ prime at $q=2$ in the proof of Theorem thm:main): 10.1(a) gives its $L$-factor and $e_\ell(E,2)$; the
  Tamagawa argument is Chapter 18's. 39, 56 (Lemma lem:hecke an equality): used only in the reading 8.5. 47, 48 (3Ns): 11.2, 12.1.

### 6.5 References

In `refs.bib`: `DFG04`, `Flach92`, `Zagier85`, `Watkins02`, `Shimura76`, `Shimura71`, `GelbartJacquet`, `Deligne79` (Deligne's conjecture),
`BlochKato`, `Fontaine`, `Berger`, `Kraus90`, `SilvermanAEC`, `SilvermanATAEC`, `DiamondShurman`, `SerreCourse`, `Neukirch`, `Washington`,
`Carayol86`, `Cremona97`, `ecdata`, `PARI`, `PARIusers`, `DDT`, `Miyake`. Proposed additions, following decision B14 (checked: none of these
keys is in `refs.bib` or in any `bib/chNN.bib`, all of which are empty except `chA.bib`):
* to `refs.bib` (needed by more than one chapter): `Rankin39` (R. A. Rankin, "Contributions to the theory of Ramanujan's function $\tau(n)$
  and similar arithmetical functions. I, II", Proc. Cambridge Philos. Soc. 35 (1939), 351-372; Chapters 13, 19; B20), `Deligne73`
  (Chapters 7, 15, 19; B18), `Tate79` (J. Tate, "Number theoretic background", Proc. Sympos. Pure Math. 33, Part 2 (1979), 3-26; Chapters
  7, 19), `Rohrlich94` (Chapters 7, 19; B18), `SerreTate68` (B14, B16), `Shimura75` (G. Shimura, "On the holomorphy of certain Dirichlet
  series", Proc. London Math. Soc. (3) 31 (1975), 79-98; Chapters 18 and 19 both need the analytic theory of $L(\Sym f,s)$; if Chapter 18
  does not cite it, `bib/ch19.bib`);
* to `bib/ch19.bib`: `Selberg40` (A. Selberg, "Bemerkungen uber eine Dirichletsche Reihe, die mit der Theorie der Modulformen nahe
  verbunden ist", Arch. Math. Naturvid. 43 (1940), 47-50), `CoatesSchmidt87` (J. Coates and C.-G. Schmidt, "Iwasawa theory for the symmetric
  square of an elliptic curve", J. Reine Angew. Math. 375/376 (1987), 104-156), `Sturm80` (J. Sturm, "Special values of zeta functions,
  and Eisenstein series of half integral weight", Amer. J. Math. 102 (1980), 219-240), `Davenport00` (H. Davenport, *Multiplicative number
  theory*, 3rd ed., revised by H. L. Montgomery, Grad. Texts in Math. 74, Springer, 2000). If Chapter 22 cites Dokchitser's algorithm for
  `lfun`, `Dokchitser04` belongs in `refs.bib`.
The writer checks every bibliographic detail above against the source before adding it (they were recalled, not looked up). No
theorem number from these works is cited in this outline except where the paper itself cites one (DFG04 Lemma 2.12, Proposition
1.4, Theorem 0.1) and Washington Theorem 4.3 (marked verify).

### 6.6 Verification log (computations done for this outline)

Scripts in the session scratchpad, `.../scratchpad/ch19/`, PARI/GP 2.17.2 via `cypari2`, `ecdata` files below conductor $10{,}000$.
* `t1.py`: for all $64{,}687$ curves, every bad prime: PARI's $P_q$ against the table of 9.3 at $q\ge5$ ($117{,}232$ pairs, no mismatch; $\mathrm I_0^*$
  via `elltwist` and `ellap`); the distribution of $P_q$ at $q=2,3$ by type (table of 10.1); the $\mathrm I_0^*$ formula at $q=3$ ($2{,}283$ of $2{,}283$).
* `t6.py`: every cubic $P_2$ ($1{,}143$) and $P_3$ ($2{,}283$) equals the formula of 10.1(b) for a twist by $d\in\{-4,8,-8\}$, resp. $-3$, with good
  reduction; no curve with $P_q$ of degree $0$ or $1$ at $q=2,3$ has such a twist.
* `t4.py`, `t5.py`: $\mathrm I_m^*$ at $2$: $P_2=1-X$ iff $v_2(j)<0$ ($3{,}732$ of $9{,}667$); type $\mathrm{II}$, $\mathrm{II}^*$ at $2$ with $e_3(E,2)>0$ or $e_5(E,2)>0$ on optimal
  curves: with $E[\ell]$ irreducible and $\ell\nmid N$, $v_\ell(\degphi)\ge e_\ell(E,2)$ always ($162$ curves at $\ell=3$, $93$ at $\ell=5$); the only exception
  with $\ell\mid N$ is the CM curve 144a1.
* `t2.py`: the Petersson formula 8.3 and the degree formula 8.4(ii) for the $15$ curves of 12.2 (ratio $1$ to $10^{-15}$; degrees from
  `ellmoddegree`).
* Power series and global checks of 8.2 (A), (B) (see 8.2).
* `t8.py`: the rows of 12.1 ($B_E$ exactly and numerically); `t7.py`: small examples by type; `lfunparams` and the sign of `lfunsympow`
  for 11a1, 121a1, 336f1, 1232l1, 539d1, 275b1, 20a1, 27a1, 64a1, 121d2 (7.2).
* `t3.py` with `rule.gp` (the appendix code verbatim): 121a1 gives `[1, 1]`; 726a1 gives `[2, 2]` with and without `iii`; also $P_2$ and $\degphi$ of
  336f1 ($1+2X$, $24$) and 1232l1 (cubic, $288$); $e_3(\text{121d2},11)=1$ against $e_3(\text{11a1},11)=0$.
* Not verified (recalled): the contents of DFG04 Lemma 2.12 and 1.7.2; the hypotheses and annihilator of Flach92; the exact
  statements of Shimura75, Sturm80, Coates-Schmidt and Gelbart-Jacquet (in particular the root number of $L(\ad f,s)$ and the CM case);
  section numbers of Davenport, Washington, SerreCourse, Neukirch, Watkins02.

## 7. Points for important_notes.md

### 7.1 New points about the paper

No new error that changes a result was found in this chapter's area. The table of Section 1, Lemma lem:euler, the values in
Remark rem:wild for type $\mathrm{IV}$ at $2$, the naive factors after Theorem thm:dfg14, the $L$-part of Lemma lem:fpr and the outputs of
`rule(E, l)` for 121a1 and 726a1 were all confirmed (Part 6.6). The known issues in the area are points 11, 12, 15, 30, 34, 43, 50,
52, 53, 60. Four additions, none of which changes a theorem:

**N1 (addendum to point 30; Introduction, "the naive one: the Euler product of $\sum a_n(f)^2n^{-s}$").** The relation is exact, with
no correction at the bad primes: $\sum a_n(f)^2n^{-s}=\zeta^{(N)}(s-1)L^{\nv}(\Sym f,s)/\zeta^{(N)}(2s-2)$ (at $p\mid N$ both local series are
$(1-a_p^2p^{-s})^{-1}$). Moreover Shimura's series gives the naive function on the nose: $L^{\nv}(\Sym f,s)=\zeta^{(N)}(2s-2)\sum a_{n^2}(f)n^{-s}$. So
the paper's sentence can be fixed with no loss of brevity: "the naive one, $\zeta^{(N)}(2s-2)\sum a_{n^2}(f)n^{-s}$ (Shimura), which has the
true local factor ...". Point 30's "up to the factors at the bad primes" can be dropped. Confidence: high (local identities as
power series; global identities checked numerically at $s=6$ for 11a1, 20a1, 121a1).

**N2 (optional strengthening; Section 1, "Up to explicit factors $\degphi$ is $\langle f,f\rangle$ ... and $\langle f,f\rangle$ is the special value
$L(\Sym f,2)$ up to the local factors at the bad primes").** Combining the Rankin-Selberg residue with the Zagier-Watkins formula
gives, for every level and every optimal curve with Manin constant $1$,
$$\langle f,f\rangle=\frac N{8\pi^3}L^{\nv}(\Sym f,2),\qquad \degphi=\frac{N\,L^{\nv}(\ad f,1)}{2\pi\operatorname{vol}(\Lambda_E)}=B_E\prod_{q^2\mid N}L_q(A_f,1)^{-1},\quad B_E=\frac{N\,L(\ad f,1)}{2\pi\operatorname{vol}(\Lambda_E)}\in\Q^\times,$$
so $v_\ell(\degphi)=v_\ell(B_E)+\sum_{q\mid N}e_\ell(E,q)$ for every $\ell\nmid N$, unconditionally. "Up to the local factors at the bad primes" is
exactly "up to $N/(8\pi^3)$ and the omitted factors at the additive primes"; the multiplicative primes contribute nothing. This makes
the paper's guiding sentence ("the primes at which the naive and the true adjoint $L$-functions differ are exactly the primes at
which the modular degree acquires extra local divisibility, and the amount is the valuation of the omitted factor") an identity,
and reduces (eq:thm) to $v_\ell(B_E)\ge\sum_qt_\ell(E,q)$. Suggested action: one displayed formula in Section 1, citing Rankin, Shimura and
Watkins. Confidence: high for the formula (proved from the residue formula; checked to 15 digits on 15 curves with additive primes
at $2$, $3$, $7$, $11$, and $B_E$ exactly on 19 curves); the attribution to DFG04 Lemma 2.12 not checked here (DFG04 Lemma 2.12 gives the Petersson norm with the naive $L$-value: Chapter 20 outline, Part 7; important_notes.md point 73).

**N3 (optional strengthening; Remark rem:wild and Section sec:wild: the factor at $q=2,3$ is not mysterious).** At every bad prime
$q\ne\ell$, including $2$ and $3$, $P_q$ is one of: $1-X$ (potentially multiplicative); $(1-qX)(1-(a'^2-2q)X+q^2X^2)$ with $a'=a_q(E^{(d)})$ when some
quadratic twist $E^{(d)}$ has good reduction at $q$ (inertia image $\{\pm1\}$; the $\mathrm I_0^*$ formula, at every $q$); $1-cqX$ with $c=\pm1$ (cyclic
inertia image of order $3$, $4$ or $6$); $1$ (non-abelian inertia image). Proof: commutants in $\SL_2$ plus Schur (item 10.1). Checked on
all curves below conductor $10{,}000$: all $1{,}143$ cubic $P_2$ and $2{,}283$ cubic $P_3$ are the twist formula, and no other shapes occur.
Consequences worth a sentence in the paper: (a) the cubic of point 50's example 1232l1 is $(1-2X)(1+2X)^2$, because 1232l1 $=$ 77a1
$\otimes\chi_{-4}$ with $a_2(\text{77a1})=0$, so $e_3(E,2)=v_3(9/8)=2$; (b) the prime $2$ can contribute at $\ell=5$: 592c1 $=$ 37a1 $\otimes\chi_{-4}$,
$a_2(\text{37a1})=-2$, $e_5(E,2)=v_5(5/8)=1$, and $\degphi=80$ (all $93$ optimal curves below $10{,}000$ with this factor, $5\nmid N$ and $E[5]$
irreducible have $5\mid\degphi$); the paper's "For $\ell=5,7$ no term is needed at $q=\ell$ or at $q=2,3$ beyond Definition def:terms" is
consistent with this, but the reader may assume the terms at $2$ vanish for $\ell\ge5$, which is false; (c) the possible values are
$e_3(E,2)\le2$, $e_5(E,2)\le1$, $e_\ell(E,2)=0$ for $\ell\ge7$, $e_5(E,3),e_7(E,3)\le1$, $e_\ell(E,3)=0$ for $\ell\ge11$; (d) Remark rem:wild's "a type $\mathrm I_n^*$ at
$2$ has potentially good reduction in about half of the cases" is $61\%$ below conductor $10{,}000$ ($5{,}935$ of $9{,}667$), and the cubic
there has $a'=\pm1$, contributing nothing at odd $\ell$ (complements point 50). Confidence: high (proof plus complete check below
$10{,}000$); importance low to medium.

**N4 (Section 1.1, "for a prime $p$ let $\delta_p=\dim V^{I_p}$, so $\delta_p=2,1,0$ for good, multiplicative, additive reduction").** At $p=\ell$ this
is false ($V_\ell E$ is ramified at $\ell$; $V^{I_\ell}=0$ at a good $\ell$), and $L_p(A_f,s)=\det(1-\Frob_pp^{-s}\mid A_f^{I_p})^{-1}$ is not the right factor at
$p=\ell$ (it needs $D_{\mathrm{cris}}$). The paper only uses $\delta_p$ and $L_p$ at $p\ne\ell$ ($\Sigma$ never contains $\ell$), so nothing breaks. Fix:
"for a prime $p\ne\ell$", or define $\delta_p$ with $V_{\ell'}E$ for any $\ell'\ne p$. Confidence: high; importance low (expository).

### 7.2 Book-internal inconsistencies

* **B-a. PLAN.md, Chapter 19 entry.** (1) "the naive adjoint $L$-function (the Euler product of $\sum a_n^2n^{-s}$ after removing the zeta
  factor, i.e. the Rankin-Selberg convolution $L(f\times f,s)/\zeta_N(2s-2)$" is wrong twice: with $L(f\times f,s)=\zeta^{(N)}(2s-2)\sum a_n^2n^{-s}$ one has
  $L^{\nv}(\Sym f,s)=L(f\times f,s)/\zeta^{(N)}(s-1)$, and the factor to remove from $\sum a_n^2n^{-s}$ is $\zeta^{(N)}(s-1)/\zeta^{(N)}(2s-2)$ (item 8.2). (2) "and its
  invariance under quadratic twist" repeats the paper's error (point 15). (3) "type II at 2 has $P_2=1$; a type $\mathrm I_n^*$ at 2 with potentially
  good reduction has a cubic $P_2$" repeats point 50. The outline follows the corrected statements; PLAN.md should be annotated.
* **B-b. Chapter 2 outline, 11.6(e), (f).** (f) asks to check that the $\mathrm I_0^*$ example with $a_7(E')=-2$ is 539d1: confirmed (539d1 has
  type $\mathrm I_0^*$ at $7$, $E'=$ 539d1 $\otimes\chi_{-7}=$ 11a3, $a_7=-2$, $e_3(E,7)=2$, $\degphi=72$). (e) still quotes "type $\mathrm{II}$ at $2$ with $P_2=1$:
  $e_3=0$" from Remark rem:wild; it is right as a conditional, but should cite 336f1 ($P_2=1+2X$) as a counterexample to the unconditional
  sentence.
* **B-c. Chapter 13 outline, 10.3(ii); Chapter 12 outline, 10.5(b); Chapter 14 outline, 7.5(b).** Chapter 13 states
  $\langle f,f\rangle=N\,L(\Sym f,2)/(8\pi^3)$ for square-free level only, and Chapters 12 and 14 state point 30's identity "up to bad factors". Not
  contradictions: item 8.3 here gives the general level (only additive primes contribute, by $P_p(p^{-2})$) and 8.2 the exact identity. When
  those chapters are written they can cite `\Cref{ch:lfunctions}` for the general form.
* **B-d. Chapter 21 outline, convention C2(b).** Still says the geometric Frobenius on $V_\ell E$ has eigenvalues $\alpha,\beta$ and that
  $\det(1-\Phi p^{-s}\mid V_\ell E)^{-1}$ is $L_p(E,s)$ (already recorded as B1, B7, B9; not new). Its part (c) ($L_p(\Sym f,s)=L_p(A_f,s-1)$, $P_q$,
  `lfuneuler`) agrees with this outline.
* **B-e. Chapter 7 outline, 9.5(ii), (iii).** Still hedges on type $\mathrm{IV}$ at $2$ and quotes "type $\mathrm{II}$ at $2$ has $P_2=1$" as consistent
  with a non-abelian image (B13, B16; not new). Item 10.1 here supersedes both: case (c) for $\mathrm{IV}$, $\mathrm{IV}^*$, and all four shapes for $\mathrm{II}$.
* No other conflict found: Chapters 4 (7.5(iii)), 6 (3.7), 7 (8.2, 9.1 to 9.4), 9 (C5), 11 (C3, 4.1, 4.4), 15 (3.4(iii), 3.7) use the same
  normalisations as this outline.
