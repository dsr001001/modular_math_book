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
  $\delta_p=\dim V^{I_p}$ for $p\ne\ell$ (for $p=\ell$ use $V_{\ell'}E$, $\ell'\ne p$; important_notes.md point N4 of Part 7). Wherever a
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
$P_p(X)=(1-\alpha^2X)(1-pX)(1-\beta^2X)$. Reference: elementary; DFG04 1.7.2 (as quoted by the paper; verify the wording). Paper:
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
extends meromorphically to $\C$ (Shimura proved this, with holomorphy, via the series $\sum a_{n^2}n^{-s}$ of 8.2(B) and a theta series of
weight $1/2$; cite the paper, proposed key `Shimura75`, Part 6.5). (ii) (Gelbart and Jacquet 1978) there is an automorphic
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
| $L(\ad f,s)$ | paper Sections 1, 1.1; DFG04 (1.7.2, $L(\ad^0M_f,s)$ at $s=1$; verify) | itself | $s\leftrightarrow1-s$ | $s=1$ | true |
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
$\frac{6N}{\pi^2\mu(N)}L^{\nv}(\Sym f,2)$ ($L^{\nv}(\Sym f,s)$ is holomorphic and nonzero near $s=2$, by 4.3 and continuity of the Euler product up to
the edge, or by 7.1); compare. For square-free $N$ this is Chapter 13's 10.3(ii). So "$\langle f,f\rangle$ is $L(\Sym f,2)$ up to the local factors at
the bad primes" (paper, Section 1) holds in the precise form: up to $N/(8\pi^3)$ and the omitted factors at the **additive** primes only;
the multiplicative primes contribute nothing beyond $N$. Verified (PARI, 18 digits; $\langle f,f\rangle$ as $\mu(N)$ times `mfpetersson`, $L(\Sym f,2)$ by
`lfun(lfunsympow(E,2),2)`): 11a1, 14a1, 20a1, 27a1, 36a1, 49a1, 50a1, 64a1, 99a1, 121a1, 121c1, 121d1, 162a1, 52a1, 80a1, with correction
factors $1,1,3/2,1,2,8/7,6/5,1,4/3,12/11,12/11,120/121,4/3,3/2,1$ (table 12.2). Reference: Rankin39; Selberg40 (proposed `bib/ch19.bib`
key); Shimura76 (verify which statement); Zagier85; Watkins02 (the method of `ellmoddegree`; cite the section); DFG04 Lemma 2.12
(as cited by the paper; content not re-checked: the writer must not attribute this exact formula to it without checking).
Paper: Section 1 ("Rankin, Shimura; see DFG04 Lemma 2.12").

**8.4 `cor:lfunctions:degree-formula`** (corollary; P given 8.3 and Chapter 14, its 7.3). (i) For every modular parametrisation
$\varphi\colon X_0(N)\to E$ with Manin constant $c_\varphi$: $\deg\varphi\cdot\operatorname{vol}(\Lambda_E)=c_\varphi^2\,N\,L^{\nv}(\ad f,1)/(2\pi)$. (ii) For the optimal curve
($c_E=\pm1$ for the curves of the tables, Chapter 14): $\degphi=N\,L^{\nv}(\ad f,1)/(2\pi\operatorname{vol}(\Lambda_E))$. (iii) Put
$B_E=N\,L(\ad f,1)/(2\pi\operatorname{vol}(\Lambda_E))$. Then $B_E=\degphi\prod_{q^2\mid N}P_q(q^{-2})^{-1}\in\Q^\times$ (for $c_E=\pm1$) and, for every prime $\ell\nmid N$,
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

