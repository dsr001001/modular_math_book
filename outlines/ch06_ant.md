# Line-up for Chapter 06: Algebraic number theory (`ch:ant`, `chapters/ch06_ant.tex`)

Stage 1 output (core results in teaching order). Target length 1,820 lines of LaTeX excluding the card
(Part 8 below). Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference.
Frobenius is *arithmetic* throughout (Convention 3.7 below, the same as Chapter 5's convention C2):
$\Frob_P(x)\equiv x^{N\mathfrak p}\pmod P$; the *geometric* Frobenius is its inverse, and local
$L$-factors are written with the geometric Frobenius (3.7). Chapter 5's conventions C1 (one $\Qbar\subset\C$),
C3 (quadratic characters $\chi_d$, $\chi_{q^*}$, never $\chi_q$: decision D3) and C4 ($\chi_\ell$, $\bar\chi_\ell$, $\chi_{\ell^*}=
\bar\chi_\ell^{(\ell-1)/2}$) are inherited without change.

Item format: number, label-ready name, kind, rigour tag; the precise statement; reference (book and theorem
number only where sure, otherwise book and chapter); the paper's use, by its `\label` names, or "background".
Small computations (splitting of specific primes, discriminants, factorisations in $\Z[i]$ and $\Z[\zeta_3]$,
Dedekind-Kummer examples, $a_p$ of CM curves) were checked by Python scripts in `/tmp/ch06` (verification log,
Part 12).

## 0. What the chapter must deliver (checked against PLAN.md Section 4 entry and Section 6 map)

Scope items of the PLAN entry, each mapped to an item below (full table in Part 10):
number fields, rings of integers, integral closure (1.1-1.4); Dedekind domains and unique factorisation of
ideals (2.1-2.2); norms of ideals (2.3); splitting of primes, $e,f,g$, $\sum e_if_i=n$, ramified/inert/split
(3.1-3.3, 3.5); discriminant and ramification (1.4, 3.4); quadratic fields in full, Kronecker symbol, the
quadratic character of $\Q(\sqrt d)$ as a Dirichlet character (4.1-4.4, 5.7, 5.8); cyclotomic fields,
splitting governed by $p\bmod n$, $\Q(\zeta_3)=\Q(\sqrt{-3})$, $\Q(\sqrt{\ell^*})\subset\Q(\zeta_\ell)$
(5.1-5.4); decomposition and inertia groups, $\Frob_P$, its conjugacy class, arithmetic versus geometric
Frobenius, Frobenius in abelian extensions (3.5-3.12, 5.6); Artin map, Kronecker-Weber, Dirichlet characters
versus one-dimensional representations of $G_\Q$ (5.5-5.8); class group and units (1.6, 2.5, 2.6, 4.5);
$\Z[\zeta_3]$, $\Z[i]$ (Euclidean), primes above $3$, $\Z_3[\zeta_3]$ a DVR with uniformiser $\pi=1-\zeta_3$
(4.5-4.9); primes $\lambda\mid\ell$ in the coefficient field of a newform, reduction mod $\lambda$ (7.1-7.5);
densities and Chebotarev in number-field form (6.1-6.4); primes inert in $\Q(\sqrt{\ell^*})$ and CM (5.3, 6.4,
6.5).

Paper hooks of the PLAN entry: Lemma lem:IV ($\Z_3[\zeta_3]$ a DVR, $T$ free of rank one over it, $E[3]=
\Z_3[\zeta_3]/(\pi^2)$ with $\sigma$ unipotent: 4.6, 4.7, 4.8); Lemma lem:euler (Frobenius centralises or
inverts $\sigma$ according to $q\bmod3$: 3.11, 3.12; "$\Z_\ell[\zeta_3]=\End_{I_q}(V)$", the line spanned by
$\sqrt{-3}$, the action of Frobenius on it by $\chi_{-3}(q)$, and the $\Q_\ell(i)$ analogue for the types
III, III$^*$ with $\chi_{-4}(q)$: 4.9, 4.10); Lemma lem:h0 ($a_p=0$ at primes inert in $\Q(\sqrt{\ell^*})$
forces CM, in the corrected reading of important_notes.md point 5: 5.3, 6.4, 6.5); Lemma lem:crit and Lemma
lem:old (rings of integers $\mathcal O$, primes $\lambda\mid\ell$, "after enlarging $\mathcal O$ and $\lambda$",
"a prime above $\lambda$ in $\mathcal O[\alpha_p]$", "a maximal ideal of residue characteristic $\ell$":
7.1-7.4); the twist by $\Q(\sqrt{q^*})$ of Section 1.4, Lemma lem:twist and the character $\chi_S$ of
Theorems thm:twist and thm:quant (4.3, 5.7, 5.8); $\chi_{-3}$, $\chi_{-4}$ of $\Q(\sqrt{-3})$ and $\Q(i)$ (4.2,
5.8). Section 6 map rows pointing at Chapter 6: "$\chi_{-3},\chi_{-4},\chi_{q^*},q^*,\ell^*$, Kronecker symbols"
(4.1-4.3, 5.3, 5.7, 5.8); "image of inertia on $T_\ell E$ at additive primes, unipotent elements,
$\Z_3[\zeta_3]$" (3.11, 3.12, 4.6-4.10).

What Chapter 6 supplies to Chapter 5 (which states these as black boxes): the definition and existence of
$\Frob_P$ and its properties (3.8, 3.10), Dedekind's cycle-type theorem (3.9), $\chi_d(\Frob_p)=(D/p)$ (4.2),
Kronecker-Weber (5.5), the Chebotarev theorem with the Frobenius made precise (6.2). Chapter 6 does not redo
Chapter 5's Galois theory of $\Q(\zeta_n)$ and $\Q(\sqrt d)$, its Chebotarev-Brauer-Nesbitt corollaries, or its
index-two restriction criterion; it cites them.

## 1. Line-up, Section 1: number fields, integers, discriminant, units

### 1.1 `def:ant:numberfield` (definition) P
A *number field* is a field $K$ with $[K:\Q]=n<\infty$. By the primitive element theorem (`ch:galois`)
$K=\Q(\theta)$, and there are exactly $n$ field embeddings $\sigma_1,\dots,\sigma_n\colon K\to\C$, namely
$\theta\mapsto$ each root of the minimal polynomial of $\theta$. Exactly $r_1$ of them have image in $\R$
and the remaining $2r_2$ come in complex-conjugate pairs; $n=r_1+2r_2$. $K$ is *totally real* if $r_2=0$,
*imaginary quadratic* if $n=2$, $r_1=0$. Reference: Neukirch I.5; Marcus Ch. 2. Paper: background.

### 1.2 `prop:ant:integral` (definition and proposition) P
$\alpha\in K$ is an *algebraic integer* (integral over $\Z$) if it is a root of a monic polynomial in
$\Z[X]$. Equivalent: (i) the minimal polynomial of $\alpha$ over $\Q$ lies in $\Z[X]$; (ii) $\Z[\alpha]$ is
a finitely generated $\Z$-module; (iii) $\alpha$ lies in a subring of $K$ that is finitely generated as a
$\Z$-module. The set $\mathcal O_K$ of algebraic integers of $K$ is a subring (the *ring of integers*),
$\mathcal O_K\cap\Q=\Z$, $\Frac(\mathcal O_K)=K$, and for every $\alpha\in K$ there is $m\in\Z_{>0}$
with $m\alpha\in\mathcal O_K$. $\mathcal O_K$ is integrally closed in $K$. (Gauss's lemma from
`ch:rings` gives (i).) Reference: Neukirch I.2; Marcus Ch. 2. Paper: Lemma lem:crit, Lemma lem:old (the
ring $\mathcal O$ of a number field), background.

### 1.3 `def:ant:tracenorm` (definition and proposition) P
For $\alpha\in K$, $\Tr_{K/\Q}(\alpha)=\sum_i\sigma_i(\alpha)$ and $N_{K/\Q}(\alpha)=\prod_i\sigma_i
(\alpha)$ are the trace and determinant of multiplication by $\alpha$ on the $\Q$-vector space $K$; so
they lie in $\Q$, $\Tr$ is $\Q$-linear, $N$ is multiplicative, and $N(\alpha)=0$ iff $\alpha=0$. If
$K=\Q(\alpha)$ with minimal polynomial $X^n+c_{n-1}X^{n-1}+\dots+c_0$ then $\Tr(\alpha)=-c_{n-1}$,
$N(\alpha)=(-1)^nc_0$. For $\alpha\in\mathcal O_K$: $\Tr(\alpha),N(\alpha)\in\Z$, and $\alpha\in
\mathcal O_K^\times$ iff $N(\alpha)=\pm1$. In a tower $L\supseteq K\supseteq\Q$: $\Tr_{L/\Q}=\Tr_{K/\Q}
\circ\Tr_{L/K}$, $N_{L/\Q}=N_{K/\Q}\circ N_{L/K}$. (RHB aside: trace and determinant of a linear map.)
Reference: Neukirch I.2.5-2.6 (cite as I.2); Lang, Algebra VI.5. Paper: background (norms of $\pi$ in
$\Z[\zeta_3]$, $N(\sqrt{-3})=3$).

### 1.4 `thm:ant:integralbasis` (theorem) P
The trace form $(x,y)\mapsto\Tr_{K/\Q}(xy)$ is a nondegenerate symmetric bilinear form on $K$.
$\mathcal O_K$ is a free $\Z$-module of rank $n$ (an *integral basis* $\omega_1,\dots,\omega_n$ exists),
and for any $\Z$-basis the integer $\disc(\omega_1,\dots,\omega_n)=\det(\Tr(\omega_i\omega_j))=
\det(\sigma_i(\omega_j))^2$ is independent of the basis: it is the *discriminant* $d_K$ of $K$. If
$\alpha_1,\dots,\alpha_n\in\mathcal O_K$ form a $\Q$-basis of $K$ and $M=\Z\alpha_1+\dots+\Z\alpha_n$,
then $\disc(\alpha_1,\dots,\alpha_n)=[\mathcal O_K:M]^2\,d_K$; in particular if $\disc(\alpha)$ is
squarefree then $M=\mathcal O_K$. For $K=\Q(\theta)$ with $\theta\in\mathcal O_K$ of minimal polynomial
$g$: $\disc(1,\theta,\dots,\theta^{n-1})=\disc(g)=\prod_{i<j}(\theta_i-\theta_j)^2$. (RHB aside: a
lattice with a Gram matrix; the trace form is the Gram matrix.) Reference: Neukirch I.2.9-2.11 (cite as
I.2); Marcus Ch. 2, Thm 9 and Thm 14 (check numbers; else cite the chapter). Paper: background
(discriminants of $\Q(\sqrt{-3})$, $\Q(i)$, $\Q(\sqrt{q^*})$).

### 1.5 `prop:ant:quadraticintegers` (proposition) P
Let $d\in\Z$ be squarefree, $d\ne0,1$, $K=\Q(\sqrt d)$. If $d\equiv2,3\pmod4$ then $\mathcal O_K=
\Z[\sqrt d]$ and $d_K=4d$; if $d\equiv1\pmod4$ then $\mathcal O_K=\Z[(1+\sqrt d)/2]$ and $d_K=d$. In
both cases $d_K$ is the *fundamental discriminant* $D$ of $K$ and $K=\Q(\sqrt D)$; a fundamental
discriminant is an integer $D\equiv1\pmod4$ squarefree, or $D=4m$ with $m\equiv2,3\pmod4$ squarefree.
Examples: $\Q(i)$: $\mathcal O=\Z[i]$, $D=-4$. $\Q(\sqrt{-3})$: $\mathcal O=\Z[\zeta_3]$ with
$\zeta_3=(-1+\sqrt{-3})/2$, $D=-3$; note $\Z[\sqrt{-3}]\subsetneq\Z[\zeta_3]$ has index $2$. $\Q(\sqrt5)$:
$\mathcal O=\Z[(1+\sqrt5)/2]$, $D=5$. $\Q(\sqrt{-7})$, $\Q(\sqrt{-11})$: $D=-7,-11$. The norm form:
$N(a+b\zeta_3)=a^2-ab+b^2$, $N(a+bi)=a^2+b^2$. Reference: Marcus Ch. 2, Cor. to Thm 1 (cite chapter);
Neukirch I.2 (Example). Paper: $\chi_{-3},\chi_{-4}$, $\Q(\sqrt{q^*})$ (Section 1, 1.4), Lemma lem:IV.

### 1.6 `thm:ant:units` (theorem) R, imaginary quadratic case P
(Dirichlet's unit theorem.) $\mathcal O_K^\times\simeq\mu(K)\times\Z^{r_1+r_2-1}$, where $\mu(K)$, the
roots of unity in $K$, is finite cyclic. For $K$ imaginary quadratic, $\mathcal O_K^\times=\mu(K)$, which
is $\{\pm1\}$ except $\mu(\Q(i))=\mu_4=\{\pm1,\pm i\}$ and $\mu(\Q(\sqrt{-3}))=\mu_6=\{\pm1,\pm\zeta_3,
\pm\zeta_3^2\}$ (proved via $N(\alpha)=1$ and the norm forms of 1.5). Example: $\Z[\sqrt2]^\times=
\pm(1+\sqrt2)^\Z$. Reference: Neukirch I.7.4; Marcus Ch. 5, Thm 38 (check; else chapter). Paper:
background (units of $\Z[\zeta_3]$ in $3=-\zeta_3^2\pi^2$, "$\pi^2=-3$ up to a unit").

## 2. Line-up, Section 2: Dedekind domains, ideals, norms, class groups

### 2.1 `thm:ant:dedekind` (definition and theorem) P
A *Dedekind domain* is a Noetherian integrally closed integral domain, not a field, in which every nonzero
prime ideal is maximal (some books allow fields; we exclude them so that the criterion below is exact).
Theorem: $\mathcal O_K$ is a Dedekind domain (Noetherian since free of finite rank over $\Z$;
integrally closed by 1.2; $\mathcal O_K/\mathfrak p$ is a finite integral domain, hence a field, because
$\mathfrak p\cap\Z=p\Z\ne0$). A Noetherian domain $R$ is Dedekind iff $R$ is not a field and every
localisation $R_{\mathfrak p}$ at a nonzero prime is a discrete valuation ring (`ch:modules` supplies
DVRs and localisation); PIDs that are not fields are Dedekind. Reference: Neukirch I.3.1, I.11.5 (cite I.3 and I.11);
Atiyah-Macdonald Ch. 9. Paper: background for every "$\mathcal O$" and every $\lambda$.

### 2.2 `thm:ant:idealfactorisation` (theorem) P
Let $R$ be a Dedekind domain with fraction field $K$. (i) Every nonzero proper ideal $\mathfrak a$ is a
product $\mathfrak a=\mathfrak p_1^{a_1}\cdots\mathfrak p_r^{a_r}$ of distinct nonzero prime ideals with
$a_i\ge1$, uniquely up to order. (ii) The nonzero *fractional ideals* (finitely generated $R$-submodules
$\mathfrak a\ne0$ of $K$; equivalently $x\mathfrak b$ with $x\in K^\times$, $\mathfrak b$ an ideal) form
an abelian group $J_K$ under multiplication, free on the nonzero primes, with $\mathfrak a^{-1}=\{x\in K:
x\mathfrak a\subseteq R\}$. (iii) For ideals, $\mathfrak a\mid\mathfrak b$ (i.e. $\mathfrak b=\mathfrak a
\mathfrak c$) iff $\mathfrak a\supseteq\mathfrak b$; $\gcd$ is the sum, $\mathrm{lcm}$ the intersection,
and $v_{\mathfrak p}(\mathfrak a)$ denotes the exponent of $\mathfrak p$. (iv) For $\alpha\in K^\times$,
$v_{\mathfrak p}(\alpha):=v_{\mathfrak p}(\alpha R)$ is the discrete valuation of $R_{\mathfrak p}$.
Proof via "every nonzero ideal contains a product of primes" and the invertibility $\mathfrak p
\mathfrak p^{-1}=R$ (Neukirch's proof), tying to `ch:modules` DVRs. Reference: Neukirch I.3.3 and I.3.8
(cite I.3); Marcus Ch. 3, Thm 16; Atiyah-Macdonald 9.3. Paper: background (every ideal statement:
$\lambda\mid\ell$, $v_\lambda$, the ideal $\eta$ in $\Z_\ell$).

### 2.3 `prop:ant:idealnorm` (definition and proposition) P
For a nonzero ideal $\mathfrak a\subseteq\mathcal O_K$ the *norm* is $N(\mathfrak a)=\#(\mathcal O_K/
\mathfrak a)$, finite. (i) $N(\mathfrak a\mathfrak b)=N(\mathfrak a)N(\mathfrak b)$. (ii) $N(\alpha
\mathcal O_K)=|N_{K/\Q}(\alpha)|$. (iii) If $\mathfrak p\cap\Z=p\Z$ then $\mathcal O_K/\mathfrak p
\simeq\F_{p^f}$ for $f=f(\mathfrak p|p)$ and $N(\mathfrak p)=p^f$. (iv) An ideal of prime norm is prime;
if $N(\mathfrak a)$ is prime to $m$ then so is $\mathfrak a$ to $m\mathcal O_K$. (v) $\disc$ of a
$\Z$-basis of $\mathfrak a$ equals $N(\mathfrak a)^2d_K$. Reference: Neukirch I.6.1-6.2 (cite I.6);
Marcus Ch. 3, Thm 22. Paper: background (norms of $\pi$, of $\sqrt{-3}$, residue fields $\mathcal O/
\lambda$ finite of characteristic $\ell$ in Lemma lem:crit).

### 2.4 `prop:ant:crt` (proposition) P
(i) (Chinese remainder theorem.) If $\mathfrak a_1,\dots,\mathfrak a_r$ are pairwise coprime ideals
($\mathfrak a_i+\mathfrak a_j=R$) of a commutative ring then $R/\mathfrak a_1\cdots\mathfrak a_r\simeq
\prod R/\mathfrak a_i$; in a Dedekind domain distinct primes are coprime, so $R/\mathfrak a\simeq
\prod_i R/\mathfrak p_i^{a_i}$, and $R/\mathfrak p^a$ has length $a$ with $\mathfrak p^k/\mathfrak p^{k+1}
\simeq R/\mathfrak p$. (ii) In a Dedekind domain every nonzero ideal is generated by two elements, one of which
may be chosen arbitrarily (nonzero) in it. (iii) A Dedekind domain with finitely many primes is a PID;
a Dedekind domain is a UFD iff it is a PID. (iv) For a nonzero prime $\mathfrak p$ of $\mathcal O_K$ the
localisation $\mathcal O_{K,\mathfrak p}$ is a DVR with maximal ideal $\mathfrak p\mathcal O_{K,
\mathfrak p}$, residue field $\mathcal O_K/\mathfrak p$ and valuation $v_{\mathfrak p}$. Reference:
Neukirch I.3.6, I.3.9, I.11 (cite I.3); Marcus Ch. 3 (Thm 17, Cor. 2 to Thm 16: check). Paper:
background (the product decomposition $\mathcal O\otimes\Z_\ell$ in 7.4; $\Z_3[\zeta_3]/(\pi^2)$).

### 2.5 `thm:ant:classgroup` (definition and theorem) R
$\Cl(K)=J_K/P_K$, $P_K$ the principal fractional ideals; $h_K=\#\Cl(K)$ is the *class number*; $h_K=1$ iff
$\mathcal O_K$ is a PID iff it is a UFD. Theorem (Minkowski): $\Cl(K)$ is finite; every ideal class
contains an integral ideal of norm at most $M_K=(4/\pi)^{r_2}(n!/n^n)|d_K|^{1/2}$; and $|d_K|>1$ for
$K\ne\Q$, so every number field other than $\Q$ has a ramified prime (with 3.4). Examples: $h=1$ for
$\Q(i)$, $\Q(\sqrt{-3})$, $\Q(\sqrt{-7})$, $\Q(\sqrt2)$, $\Q(\sqrt5)$ (Minkowski bound $<2$: $1.27$, $1.10$, $1.68$,
$1.41$, $1.12$; also Euclidean for $\Z[i]$, $\Z[\zeta_3]$ by `ch:rings`) and for $\Q(\sqrt{-11})$ (bound $2.11>2$, but
$2$ is inert since $-11\equiv5\pmod8$, so there is no ideal of norm $2$); $h(\Q(\sqrt{-5}))=2$; $h(\Q(\sqrt{-23}))
=3$ (stated). (RHB aside: $\mathcal O_K$ embedded by $(\sigma_i)$ is a lattice in $\R^{r_1}\times
\C^{r_2}$ of covolume $2^{-r_2}|d_K|^{1/2}$; Minkowski's theorem on lattice points is the tool.)
Reference: Neukirch I.6.3 and I.5.3 (cite I.5-I.6), III.2.17 for $|d_K|>1$ (cite III.2); Marcus Ch. 5.
Paper: background (why $\mathcal O$ need not be a PID; nothing in the paper uses class groups).

### 2.6 `ex:ant:sqrtminus5` (example) P
In $\Z[\sqrt{-5}]$ (the ring of integers of $\Q(\sqrt{-5})$, $D=-20$): $6=2\cdot3=(1+\sqrt{-5})(1-
\sqrt{-5})$ are two factorisations into irreducibles, none of which is prime; the ideal factorisation is
$(2)=\mathfrak p_2^2$, $(3)=\mathfrak p_3\bar{\mathfrak p}_3$, $(1+\sqrt{-5})=\mathfrak p_2\mathfrak p_3$,
$(1-\sqrt{-5})=\mathfrak p_2\bar{\mathfrak p}_3$ with $\mathfrak p_2=(2,1+\sqrt{-5})$, $\mathfrak p_3=
(3,1+\sqrt{-5})$, $\bar{\mathfrak p}_3=(3,1-\sqrt{-5})$, all of them non-principal, of norms $2,3,3$.
Computed by Dedekind-Kummer (3.2) from $X^2+5$ modulo $2$ and $3$. Paper: background.

## 3. Line-up, Section 3: splitting of primes, ramification, decomposition and inertia groups, Frobenius

### 3.1 `thm:ant:efg` (definition and theorem) P
Let $L/K$ be an extension of number fields of degree $n$ and $\mathfrak p$ a nonzero prime of $\mathcal O_K$.
In $\mathcal O_L$ write $\mathfrak p\mathcal O_L=\mathfrak P_1^{e_1}\cdots\mathfrak P_g^{e_g}$ with distinct primes
$\mathfrak P_i$ (2.2). The $\mathfrak P_i$ are exactly the primes of $\mathcal O_L$ with $\mathfrak P_i\cap
\mathcal O_K=\mathfrak p$ ("$\mathfrak P_i$ lies above $\mathfrak p$", $\mathfrak P_i\mid\mathfrak p$); $e_i=
e(\mathfrak P_i|\mathfrak p)$ is the *ramification index* and $f_i=f(\mathfrak P_i|\mathfrak p)=[\mathcal O_L/
\mathfrak P_i:\mathcal O_K/\mathfrak p]$ the *residue degree*. Then
$$\sum_{i=1}^g e_if_i=n.$$
Terminology: $\mathfrak p$ is *ramified* in $L$ if some $e_i>1$, *unramified* otherwise; *totally ramified* if
$g=1$, $e_1=n$; *inert* if $g=1$, $e_1=1$, $f_1=n$; *split completely* if $g=n$ (so all $e_i=f_i=1$); for
$L/K$ quadratic every $\mathfrak p$ is exactly one of ramified, inert, split. Multiplicativity in towers
$K\subset M\subset L$: $e(\mathfrak P|\mathfrak p)=e(\mathfrak P|\mathfrak P\cap M)\,e(\mathfrak P\cap M|
\mathfrak p)$ and the same for $f$. Proof: $\mathcal O_L/\mathfrak p\mathcal O_L\simeq\prod_i\mathcal O_L/
\mathfrak P_i^{e_i}$ (2.4) has dimension $\sum e_if_i$ over $\mathcal O_K/\mathfrak p$ (filtration by
$\mathfrak P_i^k/\mathfrak P_i^{k+1}\simeq\mathcal O_L/\mathfrak P_i$), and dimension $n$ because
$\mathcal O_{L}\otimes_{\mathcal O_K}\mathcal O_{K,\mathfrak p}$ is free of rank $n$ over the DVR (hence PID)
$\mathcal O_{K,\mathfrak p}$; for $K=\Q$ this is just "$\mathcal O_L\simeq\Z^n$" (1.4). Reference: Neukirch I.8
(Proposition 8.2); Marcus Ch. 3. Paper: background (every "prime $\lambda\mid\ell$", "prime inert in
$\Q(\sqrt{\ell^*})$").

### 3.2 `thm:ant:dedekindkummer` (theorem, Dedekind-Kummer) P
Let $K$ be a number field, $\theta\in\mathcal O_K$ with $K=\Q(\theta)$, $g\in\Z[X]$ the (monic) minimal
polynomial of $\theta$, and $p$ a prime with $p\nmid[\mathcal O_K:\Z[\theta]]$ (for instance $p^2\nmid
\disc(g)$, by 1.4). Let $\bar g=\bar g_1^{e_1}\cdots\bar g_r^{e_r}$ be the factorisation of $\bar g=g\bmod p$
into distinct monic irreducibles in $\F_p[X]$, and let $g_i\in\Z[X]$ be monic lifts of $\bar g_i$. Then
$\mathfrak P_i=(p,g_i(\theta))=p\mathcal O_K+g_i(\theta)\mathcal O_K$ are distinct primes,
$f(\mathfrak P_i|p)=\deg\bar g_i$, and $p\mathcal O_K=\mathfrak P_1^{e_1}\cdots\mathfrak P_r^{e_r}$. The same
holds verbatim for a relative extension $L=K(\theta)$, $\theta\in\mathcal O_L$, and a prime $\mathfrak p$ of
$\mathcal O_K$ coprime to the conductor of $\mathcal O_K[\theta]$ (stated). Proof (for $K/\Q$):
$\Z[\theta]/p\Z[\theta]\simeq\F_p[X]/(\bar g)$, and when $p\nmid[\mathcal O_K:\Z[\theta]]$ the inclusion induces
$\Z[\theta]/p\Z[\theta]\simeq\mathcal O_K/p\mathcal O_K$; then the Chinese remainder theorem in $\F_p[X]$ and
the bijection between ideals of $\mathcal O_K$ containing $p$ and ideals of $\mathcal O_K/p$. Warning: the
hypothesis on the index cannot be dropped (3.3(d)). Reference: Neukirch I.8 (Proposition 8.3); Marcus Ch. 3
(Theorem 27). Paper: background (all splitting computations; proof of 4.1 and 5.2).

### 3.3 `ex:ant:dkexamples` (worked examples) P
(a) $\Q(i)$, $g=X^2+1$, index $1$: mod $2$, $(X+1)^2$, so $2\Z[i]=(1+i)^2$ and indeed $2=-i(1+i)^2$;
mod $5$, $(X-2)(X+2)$, so $5=(5,i-2)(5,i+2)=(2+i)(2-i)$; mod $3$ irreducible, so $3$ is inert.
(b) $\Q(\zeta_3)$, $g=X^2+X+1$, index $1$: mod $3$, $(X-1)^2$, so $3\Z[\zeta_3]=(3,\zeta_3-1)^2=(1-\zeta_3)^2$;
mod $7$, $(X-2)(X-4)$, so $7=(7,\zeta_3-2)(7,\zeta_3-4)$, with generators $2-\zeta_3$ and $2-\zeta_3^2$
($(2-\zeta_3)(2-\zeta_3^2)=7$); mod $2$ and mod $5$, irreducible, so $2$ and $5$ are inert (residue fields
$\F_4$, $\F_{25}$). (c) $\Q(\sqrt{-5})$: see 2.6 ($X^2+5\equiv(X+1)^2\bmod2$, $\equiv(X-1)(X+1)\bmod3$).
(d) The index matters: $\Q(\sqrt{-7})$ with $\theta=\sqrt{-7}$ ($[\mathcal O_K:\Z[\sqrt{-7}]]=2$): $X^2+7\equiv
(X+1)^2\bmod2$ would wrongly suggest that $2$ ramifies; with $\theta=(1+\sqrt{-7})/2$, $g=X^2-X+2\equiv
X(X-1)\bmod2$, so $2$ splits: $2=\frac{1+\sqrt{-7}}2\cdot\frac{1-\sqrt{-7}}2$; and $2\nmid d_K=-7$.
(e) A non-Galois cubic: $K=\Q(2^{1/3})$, $\mathcal O_K=\Z[2^{1/3}]$ (stated; $d_K=\disc(X^3-2)=-108=-2^2\cdot3^3$):
$X^3-2\equiv X^3\bmod2$ and $\equiv(X+1)^3\bmod3$, so $2$ and $3$ are totally ramified; mod $5$,
$X^3-2\equiv(X-3)(X^2+3X+4)$ with the quadratic irreducible, so $5\mathcal O_K=\mathfrak P_1\mathfrak P_2$ with
$f=1,2$ (unequal residue degrees: impossible in a Galois extension, 3.5); mod $7$ irreducible (inert); mod
$31$ three linear factors (split completely). All factorisations checked by computer (Part 12). Paper: background.

### 3.4 `thm:ant:discram` (theorem, Dedekind's discriminant theorem) P
A prime $p$ ramifies in the number field $K$ if and only if $p\mid d_K$. In particular only finitely many
primes ramify in $K$, and (with Minkowski, 2.5) at least one prime ramifies in every $K\ne\Q$. Proof: $p\mid d_K$
iff the trace form of the $\F_p$-algebra $A=\mathcal O_K/p\mathcal O_K$ is degenerate (reduce an integral
basis); $A\simeq\prod_i\mathcal O_K/\mathfrak P_i^{e_i}$ (2.4); the trace form of a finite separable field
extension of $\F_p$ is nondegenerate (finite fields are perfect), and a nonzero nilpotent element lies in the
kernel of the trace form; so the trace form of $A$ is nondegenerate iff $A$ is reduced iff all $e_i=1$.
Relative version (stated): for $L/K$, a prime $\mathfrak p$ of $K$ ramifies in $L$ iff $\mathfrak p$ divides the
relative discriminant ideal $\mathfrak d_{L/K}$. Examples: $d=-4,-3,-7,-11,5,-20$ for $\Q(i),\Q(\sqrt{-3}),
\Q(\sqrt{-7}),\Q(\sqrt{-11}),\Q(\sqrt5),\Q(\sqrt{-5})$ (1.5); $d(\Q(\zeta_\ell))=(-1)^{(\ell-1)/2}\ell^{\ell-2}$
(5.1); $d(\Q(2^{1/3}))=-108$. Reference: Neukirch III.2 (Corollary 2.12), and I.2 for the trace form;
Marcus Ch. 3 (Theorem 24). Paper: background ($\Q(\sqrt{q^*})$ is ramified only at $q$, 4.3).

### 3.5 `prop:ant:galoissplitting` (proposition and definitions) P
Let $L/K$ be Galois with group $G$, $\mathfrak p$ a prime of $K$. (i) $G$ acts transitively on the set of
primes $\mathfrak P$ of $L$ above $\mathfrak p$. Hence all $e(\mathfrak P|\mathfrak p)=e$ and all
$f(\mathfrak P|\mathfrak p)=f$ are equal, and $efg=n=\#G$. (ii) The *decomposition group* is
$D_{\mathfrak P}=\{\sigma\in G:\sigma\mathfrak P=\mathfrak P\}$ (the stabiliser, Chapter 1), and the *inertia
group* is $I_{\mathfrak P}=\{\sigma\in D_{\mathfrak P}:\sigma(x)\equiv x\pmod{\mathfrak P}\text{ for all }x\in
\mathcal O_L\}$. Then $[G:D_{\mathfrak P}]=g$, $\#D_{\mathfrak P}=ef$, $I_{\mathfrak P}\trianglelefteq D_{\mathfrak P}$,
and $D_{\sigma\mathfrak P}=\sigma D_{\mathfrak P}\sigma^{-1}$, $I_{\sigma\mathfrak P}=\sigma I_{\mathfrak P}
\sigma^{-1}$; for $G$ abelian $D_{\mathfrak P}$ and $I_{\mathfrak P}$ depend only on $\mathfrak p$.
(iii) For $K\subset M\subset L$ with $H=\Gal(L/M)$: $D_{\mathfrak P}(L/M)=D_{\mathfrak P}\cap H$,
$I_{\mathfrak P}(L/M)=I_{\mathfrak P}\cap H$; if $M/K$ is Galois, the images of $D_{\mathfrak P}$ and
$I_{\mathfrak P}$ in $G/H=\Gal(M/K)$ are $D_{\mathfrak P\cap M}$ and $I_{\mathfrak P\cap M}$. (iv) $\mathfrak p$
splits completely iff $D_{\mathfrak P}=1$; $\mathfrak p$ is unramified iff $I_{\mathfrak P}=1$.
Proof of (i): if $\mathfrak P'\ne\sigma\mathfrak P$ for all $\sigma$, CRT gives $x\in\mathfrak P'$ with
$x\equiv1\bmod\sigma\mathfrak P$ for all $\sigma$; then $N_{L/K}(x)\in\mathfrak P'\cap\mathcal O_K=\mathfrak p
\subset\mathfrak P$ but no factor $\sigma(x)$ lies in $\mathfrak P$. (RHB aside: an orbit and a stabiliser.)
Reference: Neukirch I.9 (Proposition 9.1, Definition 9.2); Marcus Ch. 4 (Theorems 23, 28; check numbers,
else cite the chapter). Paper: background for Lemma lem:euler and Lemma lem:tamfactor ("$G/I$", "$I_q$",
"Frobenius normalises inertia"), Section 1.1 ($I_p$, $\delta_p=\dim V^{I_p}$).

### 3.6 `thm:ant:residuegalois` (theorem) P
In the situation of 3.5 write $\kappa(\mathfrak P)=\mathcal O_L/\mathfrak P$, $\kappa(\mathfrak p)=
\mathcal O_K/\mathfrak p$ (finite fields, $\#\kappa(\mathfrak p)=N\mathfrak p$). Every $\sigma\in D_{\mathfrak P}$
induces an automorphism $\bar\sigma$ of $\kappa(\mathfrak P)/\kappa(\mathfrak p)$, and $\sigma\mapsto\bar\sigma$
is a surjective homomorphism $D_{\mathfrak P}\to\Gal(\kappa(\mathfrak P)/\kappa(\mathfrak p))$ with kernel
$I_{\mathfrak P}$. Hence $\#I_{\mathfrak P}=e$, $D_{\mathfrak P}/I_{\mathfrak P}$ is cyclic of order $f$,
generated by the class of any $\sigma$ with $\bar\sigma=(x\mapsto x^{N\mathfrak p})$ (Chapter 5,
galois:finite-field-galois). Proof of surjectivity: choose $\bar\theta$ generating $\kappa(\mathfrak P)^\times$,
lift it to $\theta\in\mathcal O_L$ lying in every $\sigma\mathfrak P\ne\mathfrak P$ (CRT); the polynomial
$h=\prod_{\sigma\in G}(X-\sigma\theta)\in\mathcal O_K[X]$ reduces to a polynomial with root $\bar\theta$, whose
roots are the $\overline{\sigma\theta}$; the Frobenius image of $\bar\theta$ is a root $\overline{\sigma\theta}\ne0$,
which forces $\sigma\in D_{\mathfrak P}$. Reference: Neukirch I.9 (Proposition 9.4); Marcus Ch. 4
(Theorem 28); Serre, Local Fields, Ch. I. Paper: background (the exact sequence $1\to I\to D\to
\Gal(\bar\kappa/\kappa)\to1$, used in profinite form in Lemma lem:tamfactor: "the group $G/I$").

### 3.7 `conv:ant:frobenius` (convention) P (a definition and a dictionary)
For $\mathfrak P$ unramified over $\mathfrak p$ the *arithmetic Frobenius* $\Frob_{\mathfrak P}$ is the
element of 3.8; the *geometric Frobenius* is $\Frob_{\mathfrak P}^{-1}$. The book writes $\Frob_p$ for an
arithmetic Frobenius at $p$ (Chapter 5, C2, and the paper's proof of Lemma lem:tamfactor, "the arithmetic
Frobenius"), so that $\Frob_p$ acts on $\mu_n$ ($p\nmid n$) by $\zeta\mapsto\zeta^p$, $\chi_\ell(\Frob_p)=p$,
$\bar\chi_\ell(\Frob_p)=p\bmod\ell$, and for $E/\Q$ with good reduction at $p\ne\ell$ the characteristic polynomial
of $\rho_{E,\ell}(\Frob_p)$ on $V_\ell E$ is $X^2-a_pX+p$ (Chapters 9, 11). Local $L$-factors of a
representation $V$ of $G_\Q$ are written with the geometric Frobenius:
$$L_p(V,s)=\det\bigl(1-\Frob_p^{-1}p^{-s}\bigm|V^{I_p}\bigr)^{-1},$$
so that $L_p(V(1),s)=L_p(V,s+1)$ (as $\chi_\ell(\Frob_p^{-1})=p^{-1}$), $L_p(\Q_\ell(1),s)=(1-p^{-1-s})^{-1}$,
and $L_p(V_\ell E^\vee,s)=(1-a_pp^{-s}+p^{1-2s})^{-1}$ is the Euler factor of $L(E,s)$ at a good prime (on
$V_\ell E$ itself the geometric Frobenius has eigenvalues $\alpha^{-1},\beta^{-1}$, on the dual
$V_\ell E^\vee=H^1$ it has $\alpha,\beta$). Dictionary: when the multiset of Frobenius eigenvalues on
$V^{I_p}$ is stable under inversion (e.g. $\ad V$ at a good prime: $\alpha/\beta,1,\beta/\alpha$; the lines on
which Frobenius acts by $\pm1$) the two conventions give the same factor; when it is not, they differ. The
example that matters: for $E$ with multiplicative reduction at $p$, $(\ad V)^{I_p}$ is a line on which the
arithmetic Frobenius acts by $p$ and the geometric one by $p^{-1}$, and the true factor $L_p(\ad V,s)=
(1-p^{-1-s})^{-1}$ of the paper's table needs the geometric one (Part 13, point 1). Reference: Deligne,
"Les constantes des equations fonctionnelles des fonctions L" (conventions), DDT Section 1 (cite the
section); Chapter 19 of this book for $L$-functions. Paper: Section 1.1 (definition of $L_p(A_f,s)$), the table
of Section 1, Lemma lem:euler (type $\mathrm I_n$: "a line with eigenvalue $q^{-1}$"), Lemma lem:tamfactor
(arithmetic Frobenius, $\Frob^{-1}t\Frob=t^{q^{-1}}$), Lemma lem:fpr ($L_p(A_f,1)=L_p(A_f(1),0)$).

### 3.8 `prop:ant:frobenius` (definition and proposition) P
Let $L/K$ be Galois with group $G$, $\mathfrak p$ a prime of $K$ unramified in $L$, $\mathfrak P\mid\mathfrak p$.
(i) There is a unique $\Frob_{\mathfrak P}\in G$ such that $\Frob_{\mathfrak P}(x)\equiv x^{N\mathfrak p}
\pmod{\mathfrak P}$ for all $x\in\mathcal O_L$; it lies in $D_{\mathfrak P}$ and generates it, and its order
is $f$. (ii) $\Frob_{\sigma\mathfrak P}=\sigma\Frob_{\mathfrak P}\sigma^{-1}$, so
$\{\Frob_{\mathfrak P}:\mathfrak P\mid\mathfrak p\}$ is a conjugacy class $\Frob_{\mathfrak p}$ of $G$ (the
*Frobenius class*). (iii) $\mathfrak p$ splits completely in $L$ iff $\Frob_{\mathfrak p}=\{1\}$. (iv) If $G$ is
abelian, $\Frob_{\mathfrak P}$ depends only on $\mathfrak p$ and is written $\Frob_{\mathfrak p}\in G$
(the "Frobenius of an unramified prime in an abelian extension"; over $\Q$ it is the Artin symbol of 5.6).
(v) Functoriality: if $K\subset M\subset L$ with $M/K$ Galois then $\Frob_{\mathfrak P}|_M=
\Frob_{\mathfrak P\cap M}$; if $K\subset K'\subset L$ and $\mathfrak p'=\mathfrak P\cap K'$ has residue degree
$f'$ over $\mathfrak p$ then $\Frob_{\mathfrak P}(L/K')=\Frob_{\mathfrak P}(L/K)^{f'}$. (vi) For a ramified
$\mathfrak p$ there is no well-defined Frobenius element, only a coset $\sigma I_{\mathfrak P}$ of elements of
$D_{\mathfrak P}$ inducing $x\mapsto x^{N\mathfrak p}$; any such $\sigma$ is called *a Frobenius at
$\mathfrak P$*. Examples (proved in 4.2 and 5.2): in $\Q(\zeta_n)$, $p\nmid n$: $\Frob_p=\sigma_p$; in
$\Q(\sqrt d)$, $p\nmid D$: $\Frob_p(\sqrt d)=\bigl(\frac Dp\bigr)\sqrt d$. Reference: Neukirch I.9; Marcus
Ch. 4. Paper: Lemma lem:old ("$\bar\rho(\Frob_p)$", "$X^2-a_p(h)X+p$"), Lemma lem:euler, Lemma lem:tamfactor;
supplies the black box galois:frobenius-preview of Chapter 5.

### 3.9 `prop:ant:frobsubfield` (proposition) P
Let $L/\Q$ be finite Galois with group $G$, $H\le G$, $M=L^H$, and $p$ unramified in $L$; let $\mathfrak P\mid p$
and $F=\Frob_{\mathfrak P}$. Then the primes of $M$ above $p$ correspond bijectively to the orbits of $\langle F
\rangle$ acting on $G/H$ by left multiplication (the orbit of $\sigma H$ corresponds to $\sigma^{-1}\mathfrak P\cap M$),
and the residue degree of the corresponding prime is the length of the orbit; all ramification indices are $1$.
Corollary (Dedekind's theorem, Chapter 5 galois:frobenius-preview (e)): if $f\in\Z[X]$ is separable with
leading coefficient $a$, $p\nmid a\disc(f)$, $L$ is the splitting field of $f$, and $\bar f$ has irreducible
factors of degrees $d_1,\dots,d_r$ in $\F_p[X]$, then $\Frob_{\mathfrak P}$ permutes the roots of $f$ with cycle
type $(d_1,\dots,d_r)$. (Proof of the corollary: reduction mod $\mathfrak P$ is a $D_{\mathfrak P}$-equivariant
bijection from the roots of $f$ to the roots of $\bar f$ in $\kappa(\mathfrak P)$, since $p\nmid a\disc(f)$, and
$\Frob_{\mathfrak P}$ acts on the latter as $x\mapsto x^p$, whose cycles are the irreducible factors.) Example:
3.3(e) ($p=5$: one fixed root and a transposition of the other two roots of $X^3-2$). Reference: Neukirch I.9
(Exercises) and I.8; Marcus Ch. 4. Paper: Proposition prop:ns via Chapter 5 (galois:frobenius-on-lines: the
factorisation of the $3$-division polynomial mod $p$), background.

### 3.10 `prop:ant:frobGQ` (proposition and definition) P
Let $\bar{\mathbb Z}$ be the integral closure of $\Z$ in $\Qbar$ and $p$ a prime. (i) The primes $\bar{\mathfrak P}$
of $\bar{\mathbb Z}$ above $p$ are the compatible families $(\mathfrak P_L)_L$ of primes above $p$ in the finite
Galois $L/\Q$ ($\mathfrak P_L=\bar{\mathfrak P}\cap\mathcal O_L$); $G_\Q$ acts transitively on them.
(ii) $D_{\bar{\mathfrak P}}=\varprojlim D_{\mathfrak P_L}$ and $I_{\bar{\mathfrak P}}=\varprojlim I_{\mathfrak P_L}$ are
closed subgroups of $G_\Q$ (*a decomposition group* and *an inertia group at $p$*, written $D_p$, $I_p$ once
$\bar{\mathfrak P}$ is fixed), conjugate under $G_\Q$ for different choices, and $D_{\bar{\mathfrak P}}/
I_{\bar{\mathfrak P}}\simeq\Gal(\Fbar_p/\F_p)\simeq\hat\Z$, topologically generated by the class of
$x\mapsto x^p$. (iii) *A Frobenius element at $p$* is any $\Frob_p\in D_{\bar{\mathfrak P}}$ mapping to
$x\mapsto x^p$; it is well defined up to $I_{\bar{\mathfrak P}}$ and up to conjugation in $G_\Q$, and its image in
$\Gal(L/\Q)$ lies in the class $\Frob_p(L/\Q)$ of 3.8 for every finite Galois $L$ unramified at $p$.
(iv) A continuous representation $\rho$ of $G_\Q$ is *unramified at $p$* if $\rho(I_{\bar{\mathfrak P}})=1$ for one
(equivalently every) $\bar{\mathfrak P}\mid p$; then the conjugacy class of $\rho(\Frob_p)$, in particular
$\det(X-\rho(\Frob_p))$, is well defined; for $\rho$ with finite image this is the Frobenius class of 3.8 in
the field cut out by $\rho$. (v) (Stated; Chapter 7.) Choosing an embedding $\Qbar\to\Qbar_p$ identifies
$D_{\bar{\mathfrak P}}$ with $G_{\Q_p}$ and $I_{\bar{\mathfrak P}}$ with the inertia subgroup of $G_{\Q_p}$.
Reference: Neukirch I.9 and IV.1 (cite chapters); Serre, Abelian l-adic representations, Ch. I. Paper:
Section 1.1 ($I_p$, $\Frob_p$, $V^{I_p}$), Lemma lem:old, Lemma lem:tamagawa-exp, Lemma lem:tamfactor, Lemma
lem:euler; supplies Chapter 5's galois:frobenius-preview (d).

### 3.11 `prop:ant:tameconj` (proposition) S here, P in Chapter 7
Let $L/K$ be finite Galois, $\mathfrak P\mid\mathfrak p$, $q=N\mathfrak p$ (a power of the residue
characteristic $p$), and suppose $\#I_{\mathfrak P}$ is prime to $p$ (*tamely ramified*). Then
$I_{\mathfrak P}$ is cyclic, and for every $F\in D_{\mathfrak P}$ inducing $x\mapsto x^{q}$ on
$\kappa(\mathfrak P)$ and every $\tau\in I_{\mathfrak P}$: $F\tau F^{-1}=\tau^{q}$. Sketch: with $\varpi$ a
uniformiser of the DVR $\mathcal O_{L,\mathfrak P}$, the map $\theta\colon I_{\mathfrak P}\to\kappa(\mathfrak P)^\times$,
$\tau\mapsto\tau(\varpi)/\varpi\bmod\mathfrak P$, is an injective homomorphism independent of $\varpi$ when
$I_{\mathfrak P}$ has order prime to $p$ (its kernel is the wild inertia group, a $p$-group), and
$\theta(F\tau F^{-1})=F(\theta(\tau))=\theta(\tau)^q$. Reference: Serre, Local Fields, Ch. IV, Section 2
(Propositions 7 and 9; check numbers, else cite the section); Neukirch II.9 (local form). The profinite
form $\Frob\,t\,\Frob^{-1}=t^q$ on the tame inertia quotient of $G_{\Q_q}$ is Chapter 7. Paper: Lemma lem:euler
("Frobenius centralises $\sigma$ if $q\equiv1\pmod3$ and inverts it if $q\equiv2$"), Lemma lem:tamfactor
($\Frob^{-1}t\Frob=t^{q^{-1}}$, Chapter 7).

### 3.12 `cor:ant:frobsigma` (corollary) P (given 3.11)
Let $q$ be a prime, $\ell\ne q$ an odd prime, and $\rho\colon G_\Q\to\GL_2(\Z_\ell)$ continuous with
$\rho(I_q)$ finite of order $m$ prime to $q$ (for $\rho=\rho_{E,\ell}$ at a prime $q\ge5$ of additive
potentially good reduction, $m\in\{2,3,4,6\}$ by Kraus, Chapters 10, 11). Then $\rho(I_q)$ is cyclic, and for a
Frobenius $F\in D_q$ (3.10) and $\tau\in I_q$: $\rho(F)\rho(\tau)\rho(F)^{-1}=\rho(\tau)^q$. In particular, if
$\rho(I_q)=\langle\sigma\rangle$ with $\sigma$ of order $3$ (or $\langle-\sigma\rangle$ of order $6$), then $\rho(F)$
commutes with $\sigma$ if $q\equiv1\pmod3$ and conjugates it to $\sigma^{-1}$ if $q\equiv2\pmod3$; if
$\rho(I_q)=\langle\tau\rangle$ of order $4$, $\rho(F)$ commutes with $\tau$ if $q\equiv1\pmod4$ and conjugates it to
$\tau^{-1}$ if $q\equiv3\pmod4$. The result does not depend on the choice of $F$ (two choices differ by
$I_q$, and $\rho(I_q)$ is abelian). Proof from 3.11 alone (no local fields): reduction mod $\ell$ is injective on the
finite subgroup $\rho(I_q)$ of $\GL_2(\Z_\ell)$ ($1+\ell M_2(\Z_\ell)$ is torsion-free for $\ell$ odd, Chapter 1
item 7.4); apply 3.11 to the finite Galois extension $L$ cut out by $\bar\rho$ (whose inertia group at $q$ is
$\bar\rho(I_q)\simeq\rho(I_q)$, of order prime to $q$, and $F$ restricts to an element of $D_{\mathfrak P}$
inducing $x\mapsto x^q$), and lift: $\rho(F)\rho(\tau)\rho(F)^{-1}$ and $\rho(\tau)^q$ lie in the normal subgroup
$\rho(I_q)$ of $\rho(D_q)$ and have the same reduction. Reference: as 3.11. Paper: Lemma lem:euler (types II,
II$^*$, IV, IV$^*$ and III, III$^*$), Lemma lem:IV ("the image is tame since $q\ne3$, hence cyclic").

## 4. Line-up, Section 4: quadratic fields in full; $\Z[i]$, $\Z[\zeta_3]$ and the rings $\Z_\ell[\zeta_3]$

### 4.1 `thm:ant:quadsplit` (theorem) P
Let $K=\Q(\sqrt d)$, $d\ne0,1$ squarefree, with discriminant $D$ (1.5), and $p$ a prime. Then, with
$\bigl(\frac Dp\bigr)$ the Kronecker symbol (Chapter 2: the Legendre symbol for odd $p$; for $p=2$ it is $0$ if
$2\mid D$, $+1$ if $D\equiv\pm1\pmod8$, $-1$ if $D\equiv\pm3\pmod8$):
$p$ ramifies in $K$ iff $\bigl(\frac Dp\bigr)=0$ (iff $p\mid D$); $p$ splits iff $\bigl(\frac Dp\bigr)=1$; $p$ is
inert iff $\bigl(\frac Dp\bigr)=-1$. Explicitly: for odd $p\mid D$, $p\mathcal O_K=(p,\sqrt d)^2$; for odd $p\nmid D$
with $a^2\equiv d\pmod p$, $p\mathcal O_K=(p,\sqrt d-a)(p,\sqrt d+a)$, the two factors distinct; for $p=2$:
$d\equiv3\pmod4$ gives $(2)=(2,1+\sqrt d)^2$, $d\equiv2\pmod4$ gives $(2)=(2,\sqrt d)^2$, $d\equiv1\pmod8$ gives
$(2)=(2,\frac{1+\sqrt d}2)(2,\frac{1-\sqrt d}2)$, and $d\equiv5\pmod8$ gives $2$ inert. Proof: 3.2 with
$\theta=\sqrt d$ ($p$ odd, or $d\not\equiv1\bmod4$) or $\theta=(1+\sqrt d)/2$, $g=X^2-X+\frac{1-d}4$. Checked by
computer for $23$ discriminants and all $p<400$ (Part 12). Reference: Neukirch I.8 (Proposition 8.5);
Marcus Ch. 3 (Theorem 25). Paper: $\chi_{-3},\chi_{-4}$ (table of Section 1), $\Q(\sqrt{\ell^*})$ (Theorem
thm:main), $\Q(\sqrt{q^*})$ (Section 1.4, Lemma lem:twist).

### 4.2 `prop:ant:quadchar` (proposition) P
Let $K=\Q(\sqrt d)$ with discriminant $D$ and $\chi_d\colon G_\Q\to\{\pm1\}$ its character (Chapter 5, C3).
(i) For every prime $p\nmid D$: $\chi_d(\Frob_p)=\bigl(\frac Dp\bigr)$; the right side is the value at $p$ of
the primitive real Dirichlet character $\chi_D=\bigl(\frac D\cdot\bigr)$ of conductor $|D|$ (Chapter 2). (ii)
$\chi_d$ is unramified exactly at the primes $p\nmid D$ ($\chi_d(I_p)=\{\pm1\}$ for $p\mid D$). (iii) The
characters the paper uses: $\chi_{-4}(\Frob_p)=(-1)^{(p-1)/2}$ ($p$ odd; conductor $4$); $\chi_{-3}(\Frob_p)=
\bigl(\frac p3\bigr)$, which is $1$ iff $p\equiv1\pmod3$ ($p\ne3$, including $\chi_{-3}(\Frob_2)=-1$; conductor
$3$); for an odd prime $q$, $\chi_{q^*}$ (the paper's $\chi_q$) has $\chi_{q^*}(\Frob_p)=\bigl(\frac{q^*}p\bigr)=\bigl(\frac pq\bigr)$
for all $p\ne q$ including $p=2$ (quadratic reciprocity with its supplement, Chapter 2, or 5.4; conductor $q$);
$\chi_{\pm2}$ (discriminants $8,-8$) have conductor $8$. Proof of (i): $\Frob_p$ fixes $\sqrt d$ iff
$D_{\mathfrak P}=1$ iff $p$ splits (3.8(iii)) iff $\bigl(\frac Dp\bigr)=1$ (4.1). (ii) is 3.4 with 3.5(iv). (iii)
is (i) for $D=-4,-3,q^*,\pm8$. All congruence conditions checked for $p<3000$ (Part 12). Reference: Neukirch
I.8 and VI.1 (cite chapters); Washington Ch. 3 (quadratic characters as Dirichlet characters). Paper: the
table of Section 1 and Lemma lem:euler ($\chi_{-3}(q)$, $\chi_{-4}(q)$), Definition def:terms, Proposition
prop:forms ("$q\equiv\chi_{-3}(q)\pmod3$"), Lemma lem:twist ($\chi_{q^*}$), Proposition prop:ns ($\chi_{-3}$);
supplies Chapter 5's galois:quadratic-characters (c), (d).

### 4.3 `prop:ant:ramonlyat` (proposition) P
(i) For an odd prime $q$, $\Q(\sqrt{q^*})$, $q^*=(-1)^{(q-1)/2}q$, is the unique quadratic field ramified at $q$
only; its discriminant is $q^*$ (because $q^*\equiv1\pmod4$). (ii) More generally, a quadratic field is
unramified outside a finite set $S$ of primes iff its discriminant is $D=D_0\prod_{q\in T}q^*$ with $T$ a set of
odd primes in $S$ and $D_0\in\{1,-4,8,-8\}$, $D_0=1$ unless $2\in S$ (and $D\ne1$). Every fundamental
discriminant factors uniquely in this way ("prime discriminants"). (iii) For a finite set $S$ of odd primes,
$\chi_S:=\prod_{q\in S}\chi_{q^*}$ is the character of $\Q(\sqrt{\prod_{q\in S}q^*})$, of discriminant
$\prod_{q\in S}q^*$, conductor $D_S=\prod_{q\in S}q$, ramified exactly at the primes of $S$. (iv) Hence a
quadratic twist by $\chi_{q^*}$ (or $\chi_S$) is unramified at every $p\notin S$: the Galois representation does not
change on $I_p$ for $p\notin S$, which is the arithmetic input of Lemma lem:twist (i). Proof: 3.4 and 4.1;
a fundamental discriminant that is odd is $\equiv1\pmod4$, which fixes the sign $(-1)^{(q-1)/2}$. Reference:
Washington Ch. 3; Cox, Primes of the form $x^2+ny^2$, Section 5 (cite the section). Paper: Section 1.4
($E^{(q)}$, the twist by $\Q(\sqrt{q^*})$), Lemma lem:twist (i), Theorem thm:twist ($\chi_S$, $D$), Theorem
thm:quant ($E_S$), Theorem thm:qual (b), (c).

### 4.4 `ex:ant:quadexamples` (worked examples) P
(a) $\Q(i)$, $D=-4$: $2$ ramified, $p\equiv1\pmod4$ split, $p\equiv3\pmod4$ inert. (b) $\Q(\sqrt{-3})=\Q(\zeta_3)$,
$D=-3$: $3$ ramified, $p\equiv1\pmod3$ split, $p\equiv2\pmod3$ inert (including $2$). (c) $\Q(\sqrt{-7})=
\Q(\sqrt{7^*})$, $D=-7\equiv1\pmod8$: $2$ splits; $p\ne7$ splits iff $p\equiv1,2,4\pmod7$. (d) $\Q(\sqrt{-11})=
\Q(\sqrt{11^*})$, $D=-11\equiv5\pmod8$: $2$ inert, $3$ and $5$ split, $7$ inert; $p\ne11$ splits iff $p$ is a square
mod $11$. (e) $\Q(\sqrt5)=\Q(\sqrt{5^*})$: $p\ne5$ splits iff $p\equiv\pm1\pmod5$. (f) $\Q(\sqrt{-5})$, $D=-20$: $2$, $5$
ramified, $p$ splits iff $p\equiv1,3,7,9\pmod{20}$ (stated; Exercise). The paper's twists: 121a1 twisted by
$-11$ (field (d)), 539c1 and 980i1 twisted by $-7$ (field (c)): Example after Theorem thm:qual. Paper:
Section 3 Example, Lemma lem:twist.

### 4.5 `prop:ant:gausseisenstein` (proposition) P
(i) $\Z[i]$ and $\Z[\zeta_3]$ are Euclidean for the norms $a^2+b^2$ and $a^2-ab+b^2$ (Chapter 2, cited), hence
PIDs and UFDs, with unit groups $\mu_4$ and $\mu_6$ (1.6) and class number $1$ (2.5). (ii) Primes of $\Z[i]$, up to
units: $1+i$ (with $2=-i(1+i)^2$); for $p\equiv1\pmod4$ the two non-associate factors $a\pm bi$ of $p=a^2+b^2$;
for $p\equiv3\pmod4$ the rational prime $p$. Examples $5=(2+i)(2-i)$, $13=(3+2i)(3-2i)$. (iii) Primes of
$\Z[\zeta_3]$, up to units: $\pi=1-\zeta_3$ (4.6); for $p\equiv1\pmod3$ the two non-associate factors
$a+b\zeta_3$, $a+b\zeta_3^2$ of $p=a^2-ab+b^2$; for $p\equiv2\pmod3$ the rational prime $p$. Examples:
$7=(3+\zeta_3)(3+\zeta_3^2)$, $13=(4+\zeta_3)(4+\zeta_3^2)$. (iv) Corollaries: a prime $p$ is a sum of two
squares iff $p=2$ or $p\equiv1\pmod4$ (Fermat); $p=a^2-ab+b^2$ iff $p=3$ or $p\equiv1\pmod3$, and then also
$p=x^2+3y^2$ (all checked for $p<300$). Proof: 4.1 for the splitting pattern, plus "principal ideal of norm
$p$" from (i). Reference: Ireland-Rosen, Chapters 1 and 9 (add to `bib/ch06.bib`); Marcus Ch. 3. Paper:
background for Lemma lem:IV ($\Z_3[\zeta_3]$), Lemma lem:euler ($\Z_\ell[\zeta_3]$, $\Z_\ell[i]$), the table of
Section 1 ($\chi_{-3}$, $\chi_{-4}$).

### 4.6 `prop:ant:above3` (proposition) P
In $\Z[\zeta_3]$ put $\pi=1-\zeta_3$. (i) $\pi^2=-3\zeta_3$, $3=-\zeta_3^2\pi^2$, and $\sqrt{-3}:=1+2\zeta_3=
\zeta_3-\zeta_3^2=\zeta_3\pi$ satisfies $(\sqrt{-3})^2=-3$; so $\pi$ and $\sqrt{-3}$ are associates,
$N(\pi)=3$, $(3)=(\pi)^2$ ($3$ is totally ramified) and $\pi^2=-3$ up to the unit $\zeta_3$. (ii)
$\Z[\zeta_3]/(\pi)=\F_3$, and $\zeta_3\equiv1\pmod\pi$. (iii) $\Z[\zeta_3]/(3)=\Z[\zeta_3]/(\pi^2)$ is a local
ring of length $2$ with $\F_3$-basis $1,\pi$, and multiplication by $\zeta_3=1-\pi$ on it has matrix
$\begin{psmallmatrix}1&0\\-1&1\end{psmallmatrix}$ in this basis ($\zeta_3\cdot1=1-\pi$, $\zeta_3\cdot\pi=\pi-\pi^2=\pi$):
a nontrivial unipotent map whose fixed points form the line $\pi\Z[\zeta_3]/(\pi^2)$. (iv) The analogue at
$2$ in $\Z[i]$: $(2)=(1+i)^2$, $\Z[i]/(2)=\F_2[\varepsilon]/(\varepsilon^2)$ with $\varepsilon=1+i$, and
multiplication by $i=1+\varepsilon$ is a nontrivial unipotent map (the reason the prime $2$ is wild for
$\chi_{-4}$; background for Remark rem:wild). All identities checked symbolically (Part 12). Reference:
Ireland-Rosen Ch. 9 (Section 1); Washington Ch. 1 and Lemma 1.4 (for $(1-\zeta_\ell)^{\ell-1}=\ell\cdot$unit; check
the number, else cite Ch. 1). Paper: Lemma lem:IV ("$E[3]=T/3T\simeq\Z_3[\zeta_3]/(\pi^2)$ with $\sigma$ acting as
multiplication by $\zeta_3=1-\pi$ ... a nontrivial unipotent automorphism ... its fixed space is the line
$\pi\Z_3[\zeta_3]/(\pi^2)$").

### 4.7 `thm:ant:z3zeta3dvr` (theorem) P (local-field interpretation in Chapter 7)
Let $\Z_3[\zeta_3]:=\Z_3[X]/(X^2+X+1)$ (Chapter 3 supplies $\Z_3$; $X^2+X+1$ is irreducible over $\Q_3$, being
Eisenstein after $X\mapsto X+1$: $X^2+3X+3$), write $\zeta_3$ for the class of $X$ and $\pi=1-\zeta_3$. Then:
(i) $\Z_3[\zeta_3]$ is a domain, free of rank $2$ over $\Z_3$ with basis $1,\zeta_3$ (or $1,\pi$); (ii) it is a
discrete valuation ring with maximal ideal $(\pi)$, uniformiser $\pi$ and residue field $\F_3$; every nonzero
element is $u\pi^k$ with $u$ a unit and $k\ge0$; (iii) $\pi^2=-3\zeta_3$, so $3\Z_3[\zeta_3]=\pi^2\Z_3[\zeta_3]$ and
$v_\pi(3)=2$; (iv) $\Z_3[\zeta_3]\simeq\Z_3\otimes_\Z\Z[\zeta_3]$, and it is the $\pi$-adic completion of $\Z[\zeta_3]$
(stated; Chapter 7); its fraction field $\Q_3(\zeta_3)=\Q_3(\sqrt{-3})$ is a totally ramified quadratic extension
of $\Q_3$ (stated; Chapter 7). Proof of (ii): $\Z_3[\zeta_3]/(\pi)=\Z_3[X]/(X^2+X+1,1-X)=\Z_3/3=\F_3$; if
$a+b\zeta_3\notin(\pi)$, i.e. $3\nmid a+b$, then its norm $a^2-ab+b^2\equiv(a+b)^2\not\equiv0\pmod3$ is a unit of $\Z_3$
and $(a+b\zeta_3)^{-1}=(a+b\zeta_3^2)/(a^2-ab+b^2)$; so the ring is local with principal maximal ideal $(\pi)$, and
$\bigcap_k\pi^k\Z_3[\zeta_3]=\bigcap_k3^k\Z_3[\zeta_3]=0$; a Noetherian local domain with nonzero principal
maximal ideal and this property is a DVR (Chapter 3). Reference: Serre, Local Fields, Ch. I (Proposition 17
and Section I.6 for Eisenstein extensions; check numbers); Neukirch II.5. Paper: Lemma lem:IV ("$\Z_3[\zeta_3]$,
a discrete valuation ring with uniformiser $\pi=1-\zeta_3$ and residue field $\F_3$").

### 4.8 `cor:ant:z3zeta3modules` (corollary) P
Let $T$ be a free $\Z_3$-module of rank $2$ and $\sigma\in\Aut_{\Z_3}(T)$ with $\sigma^2+\sigma+1=0$ (equivalently:
$\sigma$ of order $3$ with $\det\sigma=1$, Chapter 4). Then, with $\zeta_3$ acting as $\sigma$: (i) $T$ is a torsion-free
$\Z_3[\zeta_3]$-module (if $xt=0$ with $0\ne x$, then $N(x)t=x\bar xt=0$ with $0\ne N(x)\in\Z_3$), finitely generated,
hence free (DVR, Chapter 3), of rank $2/2=1$: $T\simeq\Z_3[\zeta_3]$; (ii) $T/3T\simeq\Z_3[\zeta_3]/(\pi^2)$, and
$\sigma$ acts on $T/3T$ as the nontrivial unipotent of 4.6(iii), with fixed line $\pi T/3T$; (iii) more generally
the $\sigma$-fixed vectors of $T/\pi^kT$ form $\pi^{k-1}T/\pi^kT$, a line over $\F_3$. (Parts (i) and (ii) are the
algebra of the paper's proof; Chapter 11 supplies $\sigma$ from Kraus's theorem.) Reference: as 4.7. Paper:
Lemma lem:IV, Theorem thm:qual (a) (Serre conductor exponent $1$), Remark rem:types (contrast).

### 4.9 `prop:ant:zlzeta3` (proposition) P, with Hensel's lemma cited from Chapter 7
For a prime $\ell$ put $\Z_\ell[\zeta_3]:=\Z_\ell[X]/(X^2+X+1)\simeq\Z_\ell\otimes_\Z\Z[\zeta_3]$ and $\Z_\ell[i]:=
\Z_\ell[X]/(X^2+1)$. (i) $\ell=3$: the ramified DVR of 4.7. (ii) $\ell\equiv1\pmod3$: $X^2+X+1$ has two distinct roots
in $\Z_\ell$ (distinct simple roots in $\F_\ell$, Hensel), and $\Z_\ell[\zeta_3]\simeq\Z_\ell\times\Z_\ell$. (iii)
$\ell\equiv2\pmod3$: $X^2+X+1$ is irreducible mod $\ell$, and $\Z_\ell[\zeta_3]$ is an unramified DVR with uniformiser
$\ell$ and residue field $\F_{\ell^2}$. The trichotomy is the splitting of $\ell$ in $\Q(\zeta_3)$ (ramified,
split, inert; 4.4(b)) and is the case $K=\Q(\zeta_3)$ of 7.4. Likewise $\Z_\ell[i]\simeq\Z_\ell\times\Z_\ell$ for
$\ell\equiv1\pmod4$, an unramified DVR with residue field $\F_{\ell^2}$ for $\ell\equiv3\pmod4$, and a ramified DVR
with uniformiser $1+i$ for $\ell=2$. (iv) In all cases $\Q_\ell[\zeta_3]:=\Z_\ell[\zeta_3][1/\ell]=\Q_\ell\otimes_\Q\Q(\zeta_3)$
carries the $\Q_\ell$-linear involution $\zeta_3\mapsto\zeta_3^2$ (the nontrivial element of
$\Gal(\Q(\zeta_3)/\Q)$ extended by scalars), which negates $\sqrt{-3}=1+2\zeta_3$; and $\sqrt{-3}$ is a unit of
$\Z_\ell[\zeta_3]$ iff $\ell\ne3$. The analogous statements hold for $i$ in $\Q_\ell[i]$. Proof: Chapter 3 for the
DVR criterion as in 4.7, CRT for (ii). Reference: Neukirch II.4 (Hensel), II.8 (extensions of valuations;
cite the chapter). Paper: Lemma lem:euler ("$\Z_\ell[\zeta_3]\simeq\End_{I_q}(V)$", "the line spanned by
$\sqrt{-3}$"; see 4.10 and Part 13, point 2), Lemma lem:IV.

### 4.10 `prop:ant:commutant` (proposition) P (the number theory behind the types II, IV, III in Lemma lem:euler)
Let $F$ be a field of characteristic $0$ (in the paper $F=\Q_\ell$, $\ell\ne q$), $V$ a $2$-dimensional $F$-vector
space, and $\sigma\in\GL(V)$ with $\sigma^2+\sigma+1=0$ (order $3$, determinant $1$). (i) The commutant
$\{x\in\End_F(V):x\sigma=\sigma x\}$ is $F[\sigma]\simeq F[X]/(X^2+X+1)=F\otimes_\Q\Q(\zeta_3)$, of dimension $2$ (a field iff
$F$ contains no primitive cube root of unity; for $F=\Q_\ell$ iff $\ell\not\equiv1\pmod3$); the same holds for
$-\sigma$ (order $6$). (ii) The trace-zero part of $F[\sigma]$ is the line $F\cdot(2\sigma+1)$, and $(2\sigma+1)^2=-3$:
"the line spanned by $\sqrt{-3}$". (iii) If $\Phi\in\GL(V)$ satisfies $\Phi\sigma\Phi^{-1}=\sigma^q$ with $q$ a prime
$\ne3$, then conjugation by $\Phi$ preserves $F[\sigma]$ and acts on it as $\mathrm{id}_F\otimes\Frob_q$, where
$\Frob_q=\sigma_q\in\Gal(\Q(\zeta_3)/\Q)$ (5.2); hence it acts on the line $F(2\sigma+1)$ by $\chi_{-3}(\Frob_q)=
\chi_{-3}(q)$ (4.2). (iv) The order-$4$ analogue: if $\tau\in\GL(V)$, $\tau^2=-1$, the commutant is $F[\tau]\simeq
F\otimes_\Q\Q(i)$, its trace-zero part is $F\tau$, and $\Phi\tau\Phi^{-1}=\tau^q$ ($q$ odd) gives the action
$\chi_{-4}(q)$ on $F\tau$. (v) Integral form: if $F=\Q_\ell$ and $T\subset V$ is a $\sigma$-stable $\Z_\ell$-lattice,
then $T$ is free of rank one over $\Z_\ell[\sigma]\simeq\Z_\ell[\zeta_3]$ (4.8 for $\ell=3$; a DVR for $\ell\equiv2
\pmod3$; for $\ell\equiv1\pmod3$ via the idempotents $(\sigma-\zeta^{-1})/(\zeta-\zeta^{-1})$, $\zeta\in\Z_\ell$ a primitive
cube root of unity, whose denominator $\pm\sqrt{-3}$ is a unit), and the commutant of $\sigma$ in $\End_{\Z_\ell}(T)$ is
$\Z_\ell[\sigma]\simeq\Z_\ell[\zeta_3]$. So the correct reading of the paper's "$\Z_\ell[\zeta_3]\simeq\End_{I_q}(V)$"
is $\End_{I_q}(T)=\Z_\ell[\sigma]\simeq\Z_\ell\otimes\Z[\zeta_3]$ and $\End_{I_q}(V)=\Q_\ell\otimes\Q(\zeta_3)$, which is
not a field (nor $\Z_\ell[\zeta_3]$ a domain) when $\ell\equiv1\pmod3$; the argument of Lemma lem:euler needs only (ii)
and (iii). Proof: $\sigma$ has distinct eigenvalues over $\bar F$, so it is cyclic and its commutant is $F[\sigma]$
(Chapter 4 or linear algebra); $\tr\sigma=-1$ gives $\tr(2\sigma+1)=0$; (iii) is $\Phi(2\sigma+1)\Phi^{-1}=2\sigma^q+1$,
which is $2\sigma+1$ if $q\equiv1$ and $2\sigma^2+1=-(2\sigma+1)$ if $q\equiv2\pmod3$; (iv) is the same with $\tau^q=
\pm\tau$. Reference: elementary. Paper: Lemma lem:euler (types II, II$^*$, IV, IV$^*$: "$\Z_\ell[\zeta_3]\simeq
\End_{I_q}(V)$", "Frobenius ... acts on the line by $\chi_{-3}(q)$"; types III, III$^*$: $\chi_{-4}(q)$), with
3.12 supplying $\Phi=\rho(F)$; the table of Section 1.

## 5. Line-up, Section 5: cyclotomic fields and class field theory over $\Q$

### 5.1 `thm:ant:cyclotomicintegers` (theorem) P for prime powers, R in general
Let $n\ge1$ and $K=\Q(\zeta_n)$, of degree $\varphi(n)$ with $\Gal(K/\Q)\simeq(\Z/n)^\times$, $a\mapsto\sigma_a$
(Chapter 5, galois:cyclotomic; not redone). (i) $\mathcal O_K=\Z[\zeta_n]$. (ii) For $n=\ell^a$, $\ell$ prime:
$\prod_{b\in(\Z/\ell^a)^\times}(1-\zeta^b)=\Phi_{\ell^a}(1)=\ell$, each $1-\zeta^b$ is a unit times $1-\zeta$, so
$\ell\mathcal O_K=(1-\zeta_{\ell^a})^{\varphi(\ell^a)}$: $\ell$ is totally ramified, with residue field $\F_\ell$.
(iii) $d(\Q(\zeta_n))=(-1)^{\varphi(n)/2}\,n^{\varphi(n)}\big/\prod_{p\mid n}p^{\varphi(n)/(p-1)}$; in particular
$d(\Q(\zeta_\ell))=(-1)^{(\ell-1)/2}\ell^{\ell-2}$, $d(\Q(\zeta_3))=-3$, $d(\Q(\zeta_4))=-4$, $d(\Q(\zeta_8))=256$.
(iv) $p$ ramifies in $\Q(\zeta_n)$ iff $p\mid n$, for $n\not\equiv2\pmod4$ (recall $\Q(\zeta_n)=\Q(\zeta_{2n})$ for $n$
odd). Proof of (i) for $n=\ell^a$: $\disc(1,\zeta,\dots)$ is $\pm$ a power of $\ell$ (3.4 bookkeeping), so the index
is a power of $\ell$, and $\Z[\zeta]$ is $\ell$-maximal because $1-\zeta$ generates a totally ramified prime
(Eisenstein at $\ell$ for $\Phi_{\ell^a}(X+1)$). General $n$: compositum argument (stated). Formula (iii) checked
against $\disc(\Phi_n)$ for $n\le20$ (Part 12). Reference: Washington Ch. 2 (Theorem 2.6, Proposition 2.7; check
numbers, else cite the chapter); Neukirch I.10. Paper: background ($\Z[\zeta_3]$, $\Q(\zeta_\ell)$).

### 5.2 `thm:ant:cyclotomicsplitting` (theorem) P
Let $n=p^am$ with $p\nmid m$, and let $f$ be the order of $p$ in $(\Z/m)^\times$. In $\Q(\zeta_n)$:
$e=\varphi(p^a)$, residue degree $f$, and $g=\varphi(m)/f$ primes above $p$. The inertia group of $p$ is
$\Gal(\Q(\zeta_n)/\Q(\zeta_m))\simeq(\Z/p^a)^\times\times\{1\}$ and the decomposition group is
$(\Z/p^a)^\times\times\langle p\rangle$ inside $(\Z/n)^\times=(\Z/p^a)^\times\times(\Z/m)^\times$. For $p\nmid n$:
$\Frob_p=\sigma_p$, $p$ splits completely iff $p\equiv1\pmod n$, and is inert iff $p$ generates $(\Z/n)^\times$
(possible only when this group is cyclic). Examples (checked, Part 12): $n=3$: $p\equiv1$ split, $p\equiv2$ inert,
$3$ ramified; $n=5$: $11$ splits completely, $19$ and $29$ give $g=f=2$, $2$ and $3$ are inert; $n=7$: $2$ gives
$f=3$, $g=2$; $13$ gives $f=2$, $g=3$; $29$ splits completely. Proof: for $p\nmid n$, $\Phi_n\bmod p$ factors into
$\varphi(n)/f$ irreducibles of degree $f$ (Chapter 5, galois:cyclotomic-mod-p) and 3.2 applies ($p\nmid
\disc\Phi_n$); $\sigma_p(\zeta)=\zeta^p\equiv\zeta^p$ identifies the Frobenius (3.8); for $p\mid n$ combine 5.1(ii) in
$\Q(\zeta_{p^a})$ (totally ramified) with the unramified $\Q(\zeta_m)$ and multiplicativity of $e,f$ (3.1).
Reference: Neukirch I.10 (Proposition 10.3); Washington Ch. 2 (Theorem 2.13; check). Paper: background
for the Frobenius identities $\chi_\ell(\Frob_p)=p$, $\bar\chi_\ell(\Frob_p)=p\bmod\ell$ (Chapter 5, C2), Lemma
lem:euler (Frobenius on $\mu_3$ and $\mu_4$).

### 5.3 `prop:ant:sqrtlstar` (proposition) P
Let $\ell$ be an odd prime. (i) $\Q(\sqrt{\ell^*})$ is the unique quadratic subfield of $\Q(\zeta_\ell)$ (Chapter
5, galois:sqrt-lstar; not redone); it is ramified only at $\ell$ (4.3), with discriminant $\ell^*$. (ii) For
$p\ne\ell$ (including $p=2$): $\chi_{\ell^*}(\Frob_p)=\bigl(\frac p\ell\bigr)$; so $p$ splits in $\Q(\sqrt{\ell^*})$ iff
$p$ is a square mod $\ell$, and $p$ is *inert* in $\Q(\sqrt{\ell^*})$ iff $p$ is a non-square mod $\ell$. The inert
primes have density $1/2$ (6.3). (iii) For $\ell=3$: $\Q(\sqrt{-3})=\Q(\zeta_3)$, and the inert primes are the
$p\equiv2\pmod3$. (iv) $\Q(\sqrt{\ell^*})$ is imaginary iff $\ell\equiv3\pmod4$. Proof of (ii): $\Frob_p=\sigma_p$ in
$\Gal(\Q(\zeta_\ell)/\Q)\simeq\F_\ell^\times$ (5.2), restriction to the quadratic subfield is the quotient by the
squares (3.8(v)). Checked for $\ell\le23$, $p<2000$ (Part 12). Reference: Washington Ch. 2; Ireland-Rosen Ch. 6.
Paper: Theorem thm:main (the hypothesis on $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$), the set $S_f$ (Section 4.2),
Lemma lem:h0 ("primes inert in $\Q(\sqrt{\ell^*})$"), Section sec:anomaly ("some prime $p<1223$ inert in
$\Q(\sqrt{-3})$").

### 5.4 `cor:ant:qr` (corollary; a second proof of quadratic reciprocity) P
For distinct odd primes $p,q$: $\bigl(\frac{q^*}p\bigr)=\bigl(\frac pq\bigr)$, i.e. $\bigl(\frac pq\bigr)\bigl(\frac qp\bigr)=
(-1)^{\frac{p-1}2\frac{q-1}2}$; and $\bigl(\frac{-1}p\bigr)=(-1)^{(p-1)/2}$, $\bigl(\frac2p\bigr)=(-1)^{(p^2-1)/8}$ from
$\Q(i)=\Q(\zeta_4)$ and $\Q(\sqrt2)\subset\Q(\zeta_8)$. Proof: compute $\chi_{q^*}(\Frob_p)$ by 4.2(i) and by 5.3(ii).
(Chapter 2 proves reciprocity by Gauss sums; this proof shows why the character of $\Q(\sqrt{q^*})$ is the
Legendre symbol mod $q$, and may be given as a remark.) Reference: Neukirch I.10 (Exercise) or Washington
Ch. 2 (cite chapter). Paper: Lemma lem:twist ($\chi_{q^*}$ "of conductor $q$" is the character of $\Q(\sqrt{q^*})$).

### 5.5 `thm:ant:kroneckerweber` (theorem, Kronecker-Weber) R
Every finite abelian extension $K/\Q$ is contained in $\Q(\zeta_n)$ for some $n$; the least such $n$ (taken
$\not\equiv2\bmod4$) is the *conductor* $f_K$ of $K$, and the primes dividing $f_K$ are exactly the primes ramified
in $K$. Equivalently $\Q^{\mathrm{ab}}=\Q(\mu_\infty)$, and the cyclotomic characters induce
$G_\Q^{\mathrm{ab}}=\Gal(\Q^{\mathrm{ab}}/\Q)\simeq\varprojlim_n(\Z/n)^\times=\hat\Z^\times=\prod_\ell\Z_\ell^\times$. For a quadratic
field $f_K=|D|$ (Chapter 5, galois:sqrt-lstar (e) gives the inclusion directly). Reference: Washington Ch. 14;
Neukirch V.1 (local form) and VI (global class field theory; cite chapters); Cox Section 8 (cite section).
Paper: background (completes Chapter 5's galois:absolute-galois-group (d)); used through 5.7.

### 5.6 `thm:ant:artinQ` (theorem; Artin reciprocity over $\Q$, explicit form) P given 5.5
Let $K/\Q$ be abelian with $K\subset\Q(\zeta_n)$. (i) The *Artin map* $\mathrm{Art}_K\colon(\Z/n)^\times\to\Gal(K/\Q)$,
$a\mapsto\sigma_a|_K$, is surjective, with kernel $H_K$, and $K\mapsto H_K$ is an inclusion-reversing bijection
between subfields of $\Q(\zeta_n)$ and subgroups of $(\Z/n)^\times$ (Galois theory). (ii) For every prime $p\nmid n$,
$\Frob_p(K/\Q)=\mathrm{Art}_K(p\bmod n)$: the Frobenius of an unramified prime in an abelian extension depends only on
$p\bmod n$ (3.8(iv), 3.8(v), 5.2); so $p\nmid n$ splits completely in $K$ iff $p\bmod n\in H_K$, and the residue degree of
$p$ in $K$ is the order of $p$ in $(\Z/n)^\times/H_K$. (iii) (Stated.) Idelic form: the global Artin map
$\Q^\times\backslash\mathbb A_\Q^\times\to G_\Q^{\mathrm{ab}}$ is surjective with kernel the connected component, and
$\mathbb A_\Q^\times=\Q^\times\cdot(\R_{>0}\times\hat\Z^\times)$; under the normalisation in which a uniformiser at $p$
maps to an arithmetic Frobenius, the idele $(1,\dots,1,u_p,1,\dots)$ with $u_p\in\Z_p^\times$ maps to an element of
the inertia group at $p$ acting on $\mu_{p^\infty}$ by $u_p^{-1}$ (sign pitfall: Deligne's normalisation sends
uniformisers to geometric Frobenius; say which one is used, and avoid it in the chapter if possible).
Reference: (i), (ii) elementary from 5.2, 5.5; (iii) Neukirch VI.5 and VI.6, Milne CFT Ch. V (cite chapters).
Paper: background for "the quadratic character of conductor $q$" (Lemma lem:twist), the table of Section 1.

### 5.7 `thm:ant:dirichletgalois` (theorem) P given 5.5
(i) There is a bijection $\chi\leftrightarrow\psi_\chi$ between primitive Dirichlet characters $\chi$ (Chapter 2) and
continuous homomorphisms $\psi\colon G_\Q\to\C^\times$ (these have finite image, Chapter 5, galois:continuous-reps (d)),
characterised by $\psi_\chi(\Frob_p)=\chi(p)$ for all $p\nmid f_\chi$; concretely, $\psi_\chi$ is $\chi$ composed with
$G_\Q\to\Gal(\Q(\zeta_{f_\chi})/\Q)\simeq(\Z/f_\chi)^\times$. It is multiplicative ($\psi_{\chi\chi'}=\psi_\chi\psi_{\chi'}$
after passing to the primitive character inducing $\chi\chi'$), and the field cut out by $\psi_\chi$ has conductor
$f_\chi$. (ii) $\psi_\chi$ is unramified at $p$ iff $p\nmid f_\chi$; more precisely, with $f_\chi=p^am$, $p\nmid m$, the image of
$I_p$ in $\Gal(\Q(\zeta_{f_\chi})/\Q)\simeq(\Z/p^a)^\times\times(\Z/m)^\times$ is $(\Z/p^a)^\times\times\{1\}$ (5.2), so
$\psi_\chi(I_p)=\chi((\Z/p^a)^\times\times\{1\})$; and the Artin conductor of $\psi_\chi$ (Chapter 7) equals $f_\chi$ (stated). (iii) The same
holds for characters with values in $\Qbar_\ell^\times$ or $\Fbar_\ell^\times$ of finite order, via a fixed
embedding of the roots of unity; and every continuous $G_\Q\to\Z_\ell^\times$ factors through $\hat\Z^\times$ (5.5),
e.g. $\chi_\ell$ is the projection $\hat\Z^\times\to\Z_\ell^\times$. (iv) One-dimensional representations of $G_\Q$ over $\C$ are
thus "the same as" primitive Dirichlet characters; under this dictionary, twisting a newform's coefficients,
$a_n\mapsto\chi(n)a_n$, corresponds to tensoring its Galois representation by $\psi_\chi$ (Chapters 13, 15).
Proof: (i) and (ii) from 5.2 (inertia groups in $\Q(\zeta_n)$) and 5.5. Reference: Washington Ch. 3; Neukirch
VII.2 (cite chapter). Paper: the characters $\chi_{-3}$, $\chi_{-4}$, $\chi_{q^*}$, $\chi_S$ used both as Galois
characters ($\rho\otimes\chi$, Lemma lem:h0, Proposition prop:ns) and as Dirichlet characters ($a_n(g\otimes\chi)=
\chi(n)a_n(g)$, Lemma lem:twist (iii), Theorem thm:twist, Theorem thm:qual (b), (c)).

### 5.8 `ex:ant:characters` (worked example; the paper's characters in both languages) P
| Galois character | field cut out | Dirichlet character | conductor | value at $\Frob_p$, $p$ unramified |
|-|-|-|-|-|
| $\chi_{-4}$ | $\Q(i)=\Q(\zeta_4)$ | the nontrivial character mod $4$ | $4$ | $(-1)^{(p-1)/2}$ |
| $\chi_{-3}=\bar\chi_3$ | $\Q(\sqrt{-3})=\Q(\zeta_3)$ | $\bigl(\frac\cdot3\bigr)$ | $3$ | $1$ iff $p\equiv1\bmod3$ |
| $\chi_{q^*}$, $q$ odd | $\Q(\sqrt{q^*})\subset\Q(\zeta_q)$ | $\bigl(\frac\cdot q\bigr)$ | $q$ | $\bigl(\frac pq\bigr)$ |
| $\chi_S=\prod_{q\in S}\chi_{q^*}$ | $\Q(\sqrt{\prod_{q\in S}q^*})$ | $\prod_{q\in S}\bigl(\frac\cdot q\bigr)$ | $\prod_{q\in S}q$ | $\prod_{q\in S}\bigl(\frac pq\bigr)$ |
| $\chi_{\ell^*}=\bar\chi_\ell^{(\ell-1)/2}$ | $\Q(\sqrt{\ell^*})$ | $\bigl(\frac\cdot\ell\bigr)$ | $\ell$ | $\bigl(\frac p\ell\bigr)$ |
| $\bar\chi_\ell$ (values in $\F_\ell^\times$) | $\Q(\zeta_\ell)$ | $a\mapsto a\bmod\ell\in\F_\ell^\times$ | $\ell$ | $p\bmod\ell$ |

Warning (important_notes.md point 6): $\chi_{\ell^*}=\bar\chi_\ell$ only for $\ell=3$. Reference: as 4.2, 5.7. Paper:
table of Section 1, Lemma lem:euler, Lemma lem:twist, Theorem thm:twist, Lemma lem:h0, Proposition prop:ns,
Conjecture conj:euler.

## 6. Line-up, Section 6: densities, Chebotarev in number-field form, complex multiplication

### 6.1 `prop:ant:dedekindzeta` (definition, theorem R, corollary P)
For a number field $K$, $\zeta_K(s)=\sum_{\mathfrak a}N\mathfrak a^{-s}=\prod_{\mathfrak p}(1-N\mathfrak p^{-s})^{-1}$
(sum over nonzero ideals, product over nonzero primes) converges absolutely for $\mathrm{Re}\,s>1$ (P, from 2.2,
2.3 and $\#\{\mathfrak p\mid p\}\le[K:\Q]$). Theorem (R): $\zeta_K$ extends meromorphically to $\mathrm{Re}\,s>1-1/[K:\Q]$
with a simple pole at $s=1$ (residue given by the analytic class number formula). Consequences (P given the pole):
$\sum_{\mathfrak p}N\mathfrak p^{-s}\sim\log\frac1{s-1}$ as $s\to1^+$, so the *Dirichlet density* $\delta(X)=
\lim_{s\to1^+}\sum_{\mathfrak p\in X}N\mathfrak p^{-s}/\log\frac1{s-1}$ of a set $X$ of primes of $K$ is defined
as in Chapter 5 (galois:density) with $N\mathfrak p$ in place of $p$; the primes of degree $f(\mathfrak p|p)\ge2$
form a set of density $0$, so the primes of degree one have density one. Reference: Neukirch VII.5 and VII.13
(cite chapters); Lang, Algebraic Number Theory, Ch. VIII (cite chapter). Paper: background ("density one",
"almost all $p$" in Lemma lem:old and Section 3 via Chapter 5).

### 6.2 `thm:ant:chebotarev` (theorem, Chebotarev density theorem, number-field form) R
Let $L/K$ be a finite Galois extension of number fields with group $G$ and $C\subset G$ a conjugacy class. The set
of primes $\mathfrak p$ of $K$, unramified in $L$, with $\Frob_{\mathfrak p}=C$ (3.8(ii)) has Dirichlet density
$\#C/\#G$; it also has natural density $\#C/\#G$ (counting $N\mathfrak p\le x$). For $G$ abelian the classes are
elements and the statement is the generalised Dirichlet theorem. Chapter 5 (galois:chebotarev) states the case
$K=\Q$ with the Frobenius as a black box; here it is restated with the Frobenius of 3.8, and for a general base.
Reference: Neukirch VII.13 (Theorem 13.4); Serre, Abelian l-adic representations, Ch. I, Section 2.2. Paper:
Lemma lem:old ("by Chebotarev and Brauer-Nesbitt"), Section 3 (the optimal-level theorem applied to
"$a_p(g)\equiv a_p(f)$ for all $p\nmid3N$").

### 6.3 `cor:ant:chebotarev` (corollary) P from 6.2
In the setting of 6.2: (i) every $\sigma\in G$ is $\Frob_{\mathfrak P}$ for infinitely many $\mathfrak P$ (a set of
primes $\mathfrak p$ of positive density); (ii) the primes of $K$ splitting completely in $L$ have density
$1/[L:K]$; for $L/K$ not Galois, the primes of $K$ having a degree-one prime above them in $L$ have positive
density (apply (i) in the Galois closure with 3.9); (iii) (Bauer) for $L,L'$ Galois over $K$: $L\subset L'$ iff
almost every prime splitting completely in $L'$ splits completely in $L$; so a Galois extension is determined by
its set of split primes; (iv) $K=\Q$, $L=\Q(\zeta_n)$: Dirichlet's theorem, density $1/\varphi(n)$ for each class
in $(\Z/n)^\times$ (by 5.2); (v) $L$ quadratic over $\Q$: the split and the inert primes each have density $1/2$;
in particular the primes inert in $\Q(\sqrt{\ell^*})$ (the $p$ with $\bigl(\frac p\ell\bigr)=-1$) have density $1/2$, and
for $\ell=3$ the primes $p\equiv2\pmod3$ have density $1/2$; (vi) if $L/\Q$ is Galois and unramified outside a finite
set, the Frobenius elements at primes outside any density-zero set are dense in $\Gal(L/\Q)$ (Chapter 5,
galois:chebotarev-dense; not redone). Reference: Neukirch VII.13 (Corollaries); Serre, Abelian l-adic
representations, Ch. I. Paper: Lemma lem:old, Lemma lem:h0 (the inert primes form a set of density $1/2$),
Section sec:anomaly.

### 6.4 `prop:ant:twistdetect` (proposition) P given 6.2 and Chapter 5
Let $k$ be a field of characteristic $\ne2$ (a finite field, $\Fbar_\ell$, or a finite extension of $\Q_\ell$),
$\rho\colon G_\Q\to\GL_2(k)$ continuous, semisimple and unramified outside a finite set $S$, and $K$ a quadratic field
with character $\chi_K$. Then $\rho\simeq\rho\otimes\chi_K$ if and only if $\tr\rho(\Frob_p)=0$ for all (equivalently,
for all but finitely many, or for a density-one subset of the) primes $p\notin S$ inert in $K$. Proof:
$\det(X-(\rho\otimes\chi_K)(\Frob_p))=X^2-\chi_K(\Frob_p)\tr\rho(\Frob_p)X+\det\rho(\Frob_p)$, which equals
$\det(X-\rho(\Frob_p))$ at split $p$ always and at inert $p$ iff $2\tr\rho(\Frob_p)=0$; conclude with Chapter 5's
galois:chebotarev-brauer-nesbitt ($\rho\otimes\chi_K$ is semisimple). Applications: (a) $\bar\rho_{E,3}$ irreducible
satisfies $\bar\rho_{E,3}\simeq\bar\rho_{E,3}\otimes\chi_{-3}$ iff $3\mid a_p$ for almost all $p\equiv2\pmod3$ (Chapter 5,
galois:ns-example); (b) $\rho_{E,\ell}\simeq\rho_{E,\ell}\otimes\chi_K$ iff $a_p=0$ for almost all $p$ inert in $K$
($\rho_{E,\ell}$ is semisimple: Faltings, stated; or irreducible, e.g. when $\bar\rho_{E,\ell}$ is). Note: this criterion
concerns twisting by a *quadratic* character; it says nothing about $\rho\otimes\chi_\ell$, which is never isomorphic
to $\rho$ (Chapter 5, galois:twist (c); important_notes.md point 5). Reference: elementary given the cited
results. Paper: Lemma lem:h0 (the finiteness sentence, corrected reading), Proposition prop:ns
("$\bar\rho\simeq\bar\rho\otimes\chi_{-3}$"), the hypothesis of Theorem thm:main.

### 6.5 `thm:ant:cm` (theorem) S for (ii), R for the rest; forward pointer to Chapter 9
Let $E/\Q$ be an elliptic curve with complex multiplication: $\End_{\Qbar}(E)\ne\Z$; then $\End_{\Qbar}(E)$ is an order
$\mathcal O$ in an imaginary quadratic field $K$, the endomorphisms are defined over $K$, and $\sigma\in G_\Q$ acts on
them through $\Gal(K/\Q)$ (Chapter 9). (i) (R) $\mathcal O$ has class number one, so $K=\Q(\sqrt{-d})$ with
$d\in\{1,2,3,7,11,19,43,67,163\}$, and $j(E)$ is one of $13$ rational values. (ii) (S) $\rho_{E,\ell}\simeq\rho_{E,\ell}
\otimes\chi_K$ for every $\ell$, and $a_p(E)=0$ for every prime $p$ of good reduction that is inert in $K$. Sketch:
take $\alpha\in\mathcal O$ with $\bar\alpha=-\alpha$ (e.g. $\alpha=\sqrt{-d}$ or $2\sqrt{-d}$); it acts on $V_\ell E$
invertibly, and $\rho(\sigma)\alpha\rho(\sigma)^{-1}=\sigma(\alpha)=\chi_K(\sigma)\alpha$, so $\alpha\colon\rho\to\rho\otimes\chi_K$ is an
isomorphism; then $\tr\rho(\sigma)=\tr(\alpha^{-1}\rho(\sigma)\alpha)=\chi_K(\sigma)\tr\rho(\sigma)$, so $\tr\rho(\Frob_p)=a_p=0$
when $\chi_K(\Frob_p)=-1$ (take $\ell\ne p$). (iii) (R) Conversely, if $a_p(E)=0$ for almost all $p$ inert in a quadratic
field $K$, then $\rho_{E,\ell}\simeq\rho_{E,\ell}\otimes\chi_K$ (6.4(b)) and $E$ has CM by $K$ (Serre's open image
theorem, Serre72: for $E$ without CM the image of $\rho_{E,\ell}$ is open in $\GL_2(\Z_\ell)$, so the trace cannot vanish
on the coset $\rho(G_\Q\setminus G_K)$); in particular $K$ is imaginary. (iv) (R) For $E$ without CM the set of $p$
with $a_p(E)=0$ has density $0$ (Serre, 1981, "Quelques applications du theoreme de densite de Chebotarev";
add to `bib/ch06.bib`). (v) (R; conductor-discriminant formula, Chapters 7 and 19) Every prime ramified in $K$
divides the conductor of $E$. (vi) Consequences for $\Q(\sqrt{\ell^*})$: "$a_p(E)=0$ for almost all $p$ inert in
$\Q(\sqrt{\ell^*})$" holds iff $E$ has CM by $\Q(\sqrt{\ell^*})$, which needs $\ell\equiv3\pmod4$ and
$\ell\in\{3,7,11,19,43,67,163\}$, and then $\ell\mid N$ by (v); so it never happens in the range $\ell\nmid N$ of
Theorem thm:main. Examples (checked: $a_p=0$ at every good inert $p<300$, nonzero at many split $p$; Part 12):
$y^2=x^3-x$ (conductor $32$, CM by $\Z[i]$); $y^2=x^3+1$ (36a1) and $y^2+y=x^3-7$ (27a1), CM by $\Q(\sqrt{-3})$;
121b1 $=[0,-1,1,-7,10]$, CM by $\Q(\sqrt{-11})=\Q(\sqrt{11^*})$. Warning for the writer: the paper's Lemma lem:h0
invokes this fact for $\rho\simeq\rho\otimes\chi_\ell$, which is the wrong character (important_notes.md point 5);
the statement to present is (ii), (iii) for $\chi_{\ell^*}$, and the finiteness of $h_\ell(E)$ needs none of it
($h_\ell(E)\le1$ by the determinant argument, Chapter 5). Reference: Silverman ATAEC Ch. II (cite chapter) and
Appendix A (the $13$ $j$-invariants); Cox Section 14 (Deuring's reduction theorem); Serre72 Section 4.5 (cite
section). Paper: Lemma lem:h0 (last sentence of the statement and the proof), Conjecture conj:euler ("without
complex multiplication"), the data sections ("not CM").

## 7. Line-up, Section 7: coefficient fields of newforms, primes $\lambda\mid\ell$, reduction mod $\lambda$

### 7.1 `prop:ant:coefffield` (proposition) P
Let $R$ be a commutative ring which is finitely generated as a $\Z$-module (in the paper the Hecke algebra
$\T$, Chapter 13), and $\phi\colon R\to\C$ a ring homomorphism. Then every $\phi(t)$ is an algebraic integer (it is a root
of the characteristic polynomial of multiplication by $t$ on $R/\mathrm{tors}$, Cayley-Hamilton; or $\Z[\phi(t)]$ is a
finitely generated $\Z$-module, 1.2(ii)); $K_\phi=\Q(\phi(R))$ is a number field and $\phi(R)$ is a subring of
$\mathcal O_{K_\phi}$ of finite index (an *order*). For $\sigma\in G_\Q$, $\sigma\circ\phi$ is another such homomorphism (the
*Galois conjugates*). Applied to the eigencharacter $\phi_f\colon\T\to\C$, $T_n\mapsto a_n(f)$, of a newform $f$: the
*coefficient field* $K_f=\Q(a_n(f):n\ge1)$ is a number field, every $a_n(f)\in\mathcal O_{K_f}$, and the conjugates
$f^\sigma=\sum\sigma(a_n)q^n$ are newforms (stated; Chapter 13); for weight $2$ and trivial character $K_f$ is
totally real (stated; Chapter 13). For $f=f_E$, $K_f=\Q$, $\mathcal O=\Z$ and the only prime above $\ell$ is
$\lambda=\ell$ (as in the paper's Section 4: "$\lambda=\ell$"). Reference: Diamond-Shurman Ch. 6 (Section 6.5;
check), Atiyah-Macdonald Ch. 5 (Proposition 5.1). Paper: Lemma lem:crit ("coefficients in the ring of integers
$\mathcal O$ of a number field"), Lemma lem:old ("with coefficients in $\mathcal O$").

### 7.2 `prop:ant:primesabove` (proposition) P
Let $K$ be a number field, $\ell$ a prime. (i) The primes $\lambda\mid\ell$ of $\mathcal O_K$ are the maximal ideals
containing $\ell$; there are at most $[K:\Q]$ of them (3.1); $k_\lambda=\mathcal O_K/\lambda\simeq\F_{\ell^{f}}$; reduction
mod $\lambda$ is the ring homomorphism $\mathcal O_K\to k_\lambda$, $a\mapsto\bar a$. (ii) For $a,b\in\Z$: $a\equiv b
\pmod\lambda$ iff $a\equiv b\pmod\ell$ ($\lambda\cap\Z=\ell\Z$); for $a\in\mathcal O_K$, $\lambda\mid a$ for every $\lambda\mid\ell$ iff
$a\in\mathrm{rad}(\ell\mathcal O_K)$, and $\ell\mid N_{K/\Q}(a)$ iff some $\lambda\mid\ell$ divides $a$. (iii) *Enlarging*: if
$K\subset K'$ then $\lambda\mathcal O_{K'}\ne\mathcal O_{K'}$ and every prime $\lambda'$ of $K'$ dividing $\lambda\mathcal O_{K'}$ satisfies
$\lambda'\cap\mathcal O_K=\lambda$; reduction mod $\lambda'$ extends reduction mod $\lambda$ along $k_\lambda\subset k_{\lambda'}$.
(iv) *Lying over* (R/P): if $A\subset B$ is an integral extension of rings (e.g. an order $\mathcal O[\alpha]$ with $\alpha$
integral over $\mathcal O$, or $B=\mathcal O_{K'}$) then every prime of $A$ is $\mathfrak q\cap A$ for some prime $\mathfrak q$ of $B$,
and $\mathfrak q$ is maximal iff $\mathfrak q\cap A$ is. (v) Example of the step in Lemma lem:old: with $\alpha_p$ a root of
$X^2-a_p(h)X+p$ ($p\ne\ell$), $\mathcal O[\alpha_p]$ is integral over $\mathcal O$, so there is a prime $\lambda'$ of
$\mathcal O[\alpha_p]$ (or of the ring of integers of $K(\alpha_p)$) above $\lambda$, and if $X^2-a_p(h)X+p\equiv(X-u)(X-w)
\pmod\lambda$ then $\alpha_p\equiv u$ or $\alpha_p\equiv w\pmod{\lambda'}$ ($\lambda'$ is prime); if $\alpha_p\equiv a_p(f)p$ with
$a_p(f)=\pm1$, then the other root $\beta_p=p/\alpha_p\equiv a_p(f)$ (since $p$ is a unit mod $\lambda'$). Reference:
Atiyah-Macdonald Ch. 5 (Theorem 5.10, Corollary 5.8); Neukirch I.8. Paper: Lemma lem:crit ("a prime
$\lambda\mid\ell$ of $\mathcal O$"), Lemma lem:old ("after enlarging $\mathcal O$ and $\lambda$", "modulo a prime above $\lambda$
in $\mathcal O[\alpha_p]$", the case $p\,\|\,N$ with $\bar\rho$ unramified).

### 7.3 `prop:ant:congruencemaximal` (proposition) P
Let $R$ be a commutative ring finitely generated as a $\Z$-module, $\mathcal O=\mathcal O_K$, $\lambda\mid\ell$, and
$\phi\colon R\to\mathcal O$ a ring homomorphism. (i) $\mathfrak m=\ker(R\xrightarrow{\phi}\mathcal O\to k_\lambda)$ is a maximal ideal of
$R$ with residue field a subfield of $k_\lambda$, of characteristic $\ell$ (a finite subring of a field is a field).
(ii) If $\phi'\colon R\to\mathcal O$ is another homomorphism with $\phi'(t)\equiv\phi(t)\pmod\lambda$ for all $t\in R$ (for $R=\T$:
$a_n(g)\equiv a_n(f)$ for all $n$, i.e. on generators), then $\phi$ and $\phi'$ define the same $\mathfrak m$. (iii) If $J\subset R$
is an ideal with $R/J$ finite cyclic of order $r$ and $J\subset\mathfrak m$, then $\ell\mid r$ ($R/J$ surjects onto $R/\mathfrak m\ne0$,
of characteristic $\ell$). (iv) For $R$ finite over $\Z$, $R\otimes\Z_\ell$ is the product of its localisations at the
maximal ideals containing $\ell$ (stated; Chapter 3), and $\phi$ extends to $R\otimes\Z_\ell\to\mathcal O_\lambda$ (7.4) factoring
through the factor $R_{\mathfrak m}$. Reference: Atiyah-Macdonald Ch. 1, 5, 8 (cite chapters); DDT Section 4.1
(cite section). Paper: Lemma lem:crit ("$I+J$ lies in the kernel of $\T\to\mathcal O/\lambda$, a maximal ideal of residue
characteristic $\ell$, and $\ell$ divides $\#\T/(I+J)=r$"; "the same statements hold with $\Z$ replaced by
$\Z_\ell$"), Lemma lem:hecke and the proof of Theorem thm:quant ("the maximal ideal $\mathfrak m$ of $\T\otimes\Z_\ell$
containing $\ell$ and $\ker\phi_f$", "the other local factors ... are killed by $\phi_f$").

### 7.4 `prop:ant:otimesZl` (proposition) R here, P in Chapter 7
For a number field $K$ and a prime $\ell$: $\mathcal O_K\otimes_\Z\Z_\ell\simeq\prod_{\lambda\mid\ell}\mathcal O_{K,\lambda}$ and
$K\otimes_\Q\Q_\ell\simeq\prod_{\lambda\mid\ell}K_\lambda$, where $\mathcal O_{K,\lambda}$ is the $\lambda$-adic completion, a complete DVR,
free over $\Z_\ell$ of rank $e_\lambda f_\lambda$ ($\sum_\lambda e_\lambda f_\lambda=[K:\Q]$, 3.1), with uniformiser any $\varpi\in\lambda\setminus
\lambda^2$ and residue field $k_\lambda$; $K_\lambda$ is a finite extension of $\Q_\ell$ of degree $e_\lambda f_\lambda$. The cases
$K=\Q(\zeta_3)$, $\Q(i)$ are 4.9. Reference: Neukirch II.8 (Proposition 8.3; check), Serre, Local Fields,
Ch. II. Paper: Section 4 ("$\lambda$", "$\mathcal O$ a discrete valuation ring" in Lemma lem:ddt417; DFG's
$\mathcal O$, $E_\lambda$), Lemma lem:crit (over $\Z_\ell$), Lemma lem:IV ($\Z_3[\zeta_3]$), Lemma lem:euler
($\Z_\ell[\zeta_3]$).

### 7.5 `ex:ant:level23` (worked example) P for the algebra, R for the modular input
$S_2(\Gamma_0(23))$ is two-dimensional, spanned by a newform $f$ and its Galois conjugate, with coefficient field
$K_f=\Q(\sqrt5)$ (stated; LMFDB 23.2.a.a; the writer must check the $q$-expansion there, in particular that $a_2(f)$
is a root of $X^2+X-1$, before quoting coefficients). Primes of $\mathcal O_{K_f}=\Z[\frac{1+\sqrt5}2]$: $5=(\sqrt5)^2$
ramified; $11$ splits ($5$ is a square mod $11$), into two primes $\lambda,\lambda'$ with residue field $\F_{11}$, giving two
different reductions of $f$ mod $11$ that are exchanged by $\Gal(K_f/\Q)$; $2$ is inert ($5\equiv5\pmod8$), residue
field $\F_4$, and a root of $X^2+X-1$ reduces to a root of $X^2+X+1$, a primitive cube root of unity in $\F_4$. So
"$a_n(g)\equiv a_n(f)\pmod\lambda$" in Lemma lem:crit depends on $\lambda$, not only on $\ell$. Paper: Lemma lem:crit,
Lemma lem:old (the forms $g$, $h$ may have non-rational coefficients), Section 3 Example (all forms there have
rational coefficients, so $\lambda=\ell$).

## 8. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: items 1.1 to 7.5, each stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | lem:IV; lem:euler; lem:h0 (corrected reading); lem:crit, lem:old; Section 1.4, lem:twist, thm:twist, thm:quant; table of Section 1 ($\chi_{-3}$, $\chi_{-4}$); the hypothesis of thm:main ($\Q(\sqrt{\ell^*})$); Section 1.1 ($I_p$, $\Frob_p$, $L_p$) | 40 |
| 1 | Number fields and their rings of integers | 1.1 to 1.6; convention: $\Qbar\subset\C$ as in Chapter 5 | 230 |
| 2 | Dedekind domains, ideals, norms and class groups | 2.1 to 2.6 | 230 |
| 3 | Splitting of primes, ramification and Frobenius | 3.1 to 3.12; Convention 3.7 (arithmetic versus geometric) as a `convention` environment; `paperlink` for lem:euler (3.12) | 330 |
| 4 | Quadratic fields, $\Z[i]$, $\Z[\zeta_3]$ and $\Z_\ell[\zeta_3]$ | 4.1 to 4.10; a table of splitting in $\Q(i)$, $\Q(\sqrt{-3})$, $\Q(\sqrt{-7})$, $\Q(\sqrt{-11})$, $\Q(\sqrt5)$; `paperlink` for lem:IV (4.7, 4.8) and lem:euler (4.10) | 300 |
| 5 | Cyclotomic fields and class field theory over $\Q$ | 5.1 to 5.8; the table of 5.8; `paperlink` for lem:twist, thm:twist ($\chi_{q^*}$, $\chi_S$) | 230 |
| 6 | Densities, Chebotarev, complex multiplication | 6.1 to 6.5; `paperlink` for lem:h0 with a `warning` on the $\chi_\ell$ versus $\chi_{\ell^*}$ confusion | 160 |
| 7 | Coefficient fields and primes above $\ell$ | 7.1 to 7.5; `paperlink` for lem:crit and lem:old | 140 |
| 8 | Exercises | 18 exercises (Part 10) | 120 |
| 9 | Notes and references | Neukirch, Marcus, Ireland-Rosen, Washington, Serre (Local Fields; Abelian l-adic representations; Serre72), Cox, Atiyah-Macdonald, Lang (Algebra; Algebraic Number Theory), Silverman ATAEC, Milne CFT, DDT; which theorem numbers were cited and which were left at chapter level | 40 |
| | **total** | | **1820** |

## 9. Dependencies and forward pointers

Results from other chapters used here (by chapter label only):
* Chapter 1 (`ch:groups`): group actions, orbits and stabilisers (decomposition groups as stabilisers, 3.5,
  3.9); cyclic groups and $(\Z/n)^\times$; profinite groups, $\hat\Z$, $\Z_\ell$; $1+\ell M_2(\Z_\ell)$ torsion-free for
  $\ell$ odd (item 7.4 there; used in 3.12).
* Chapter 2 (`ch:rings`): rings, ideals, PIDs and UFDs, Euclidean domains and the proofs that $\Z[i]$ and
  $\Z[\zeta_3]$ are Euclidean (4.5), Gauss's lemma (1.2), Eisenstein's criterion (4.7, 5.1), CRT (2.4), finite fields,
  Legendre/Jacobi/Kronecker symbols and quadratic reciprocity (4.1, 4.2), Dirichlet characters, conductors,
  primitivity (5.7), cyclotomic polynomials.
* Chapter 3 (`ch:modules`): finitely generated modules over a PID (1.4, 3.1), localisation, Noetherian rings,
  DVRs and the DVR criterion (2.1, 2.4, 4.7), $\Z_\ell$ and its completion properties (4.7, 4.9), torsion-free modules
  over a DVR are free (4.8), products of local rings for finite $\Z_\ell$-algebras (7.3).
* Chapter 4 (`ch:reps`): Brauer-Nesbitt (6.4, via Chapter 5), traces of induced representations and the
  trace-zero lemma (6.5), commutants of a cyclic endomorphism (4.10), the module side of $\Z_\ell[\zeta_3]$
  acting on lattices (4.8, 4.10).
* Chapter 5 (`ch:galois`): all of finite Galois theory, primitive elements, $\Gal(\Q(\zeta_n)/\Q)\simeq(\Z/n)^\times$,
  $\Q(\sqrt{\ell^*})\subset\Q(\zeta_\ell)$, quadratic characters $\chi_d$ (C3), cyclotomic character (C4), Krull topology and
  $G_\Q$, continuous representations, galois:chebotarev-brauer-nesbitt and galois:chebotarev-dense, galois:twist,
  galois:index-two-restriction. Chapter 6 supplies the black boxes Chapter 5 states (see Part 0).
* Background: linear algebra (trace forms, Gram determinants, Cayley-Hamilton), complex analysis (only for the
  statement of the pole of $\zeta_K$).

Black boxes imported from later chapters (stated with a forward `\Cref`, never used in a proof of an earlier
item): Hensel's lemma and completions (Chapter 7: 4.9, 7.4); the tame-inertia relation in profinite form
(Chapter 7: after 3.11); Kraus's theorem on the image of inertia (Chapters 10, 11: hypothesis of 3.12); the
Galois action on endomorphisms of a CM curve and Deuring's theorem (Chapter 9: 6.5); Hecke algebras and
newforms (Chapters 12, 13: 7.1, 7.5); Faltings's semisimplicity and Serre's open image theorem (Chapter 11: 6.4,
6.5).

Forward pointers (chapters that use this one):
* Chapter 7 (`ch:local`): completions $\mathcal O_{K,\lambda}$, $K_\lambda$, $\mathcal O\otimes\Z_\ell=\prod\mathcal O_\lambda$ (7.4); $D_p\simeq G_{\Q_p}$
  (3.10(v)); $\Z_3[\zeta_3]$ as the ring of integers of $\Q_3(\sqrt{-3})$ (4.7); ramified quadratic extensions
  $\Q_p(\sqrt{p^*})$ and the local behaviour of $\chi_{q^*}$ (4.2(ii), 4.3); tame inertia and $\Frob\,t\,\Frob^{-1}=t^q$ (3.11);
  geometric Frobenius in local $L$-factors (3.7); Artin conductors of characters (5.7(ii)).
* Chapter 9 (`ch:ellcurves`): CM curves, $a_p=0$ at inert primes (6.5), quadratic twists by $\chi_d$ with
  $a_p(E^{(d)})=\chi_d(p)a_p(E)$ (4.2, 5.7), Frobenius characteristic polynomial $X^2-a_pX+p$ (3.7).
* Chapter 10 (`ch:reduction`): the twist by $\Q(\sqrt{q^*})$ is unramified outside $q$ (4.3), $\chi_{q^*}$ at $q$.
* Chapter 11 (`ch:galrep`): Lemma lem:IV in full (4.6 to 4.8), Remark rem:types, Lemma lem:euler's inertia
  analysis (3.12, 4.10), Proposition prop:ns ($\chi_{-3}$, 6.4(a)), Lemma lem:h0 (5.3, 6.4, 6.5), unramified
  representations and $\rho(\Frob_p)$ (3.10).
* Chapters 12, 13 (`ch:modforms`, `ch:hecke`): coefficient fields, orders, primes $\lambda$ (7.1, 7.2), twisting
  newforms by Dirichlet characters (5.7(iv)), Atkin-Li (conductor $q$ of $\chi_{q^*}$, 5.8).
* Chapter 15 (`ch:modgalrep`): $\lambda$-adic representations of newforms over $\mathcal O_\lambda$ (7.4), Lemma lem:old
  (7.2(v), 7.3), Chebotarev (6.2).
* Chapter 19 (`ch:lfunctions`): Euler factors with geometric Frobenius (3.7), the values $\chi_{-3}(q)$,
  $\chi_{-4}(q)$ in the table of Section 1 (4.2, 4.10), Dedekind zeta and Dirichlet $L$-functions (6.1, 5.7).
* Chapter 20 (`ch:congruence`): congruence ideals over $\mathcal O$, maximal ideals of $\T\otimes\Z_\ell$ (7.3).
* Chapters 21, 22 (`ch:paper`, `ch:computation`): every hook in Part 0; the PARI checks of splitting and of
  CM.

## 10. Coverage table and exercises

| PLAN.md scope item, Section 6 map row, or paper hook | line-up items |
|-|-|
| number fields | 1.1 |
| rings of integers, integral closure | 1.2, 1.4, 1.5 |
| Dedekind domains and unique factorisation of ideals | 2.1, 2.2, 2.4 |
| norms of ideals | 1.3, 2.3 |
| splitting of primes in extensions ($e$, $f$, $g$; $efg=n$) | 3.1, 3.5 |
| ramified, inert, split primes | 3.1, 3.3, 4.1, 5.2 |
| Dedekind-Kummer | 3.2, 3.3, 2.6 |
| the discriminant and ramification | 1.4, 3.4, 5.1 |
| quadratic fields in full; splitting governed by the Kronecker symbol | 1.5, 4.1, 4.4 |
| the quadratic character attached to $\Q(\sqrt d)$ as a Dirichlet character | 4.2, 5.7, 5.8 |
| cyclotomic fields; splitting governed by $p\bmod n$ | 5.1, 5.2 |
| $\Q(\zeta_3)=\Q(\sqrt{-3})$ | 3.3(b), 4.4(b), 4.6, 5.3(iii) |
| $\Q(\sqrt{\ell^*})$ inside $\Q(\zeta_\ell)$ (coordinated with Chapter 5) | 5.3, 5.4 |
| decomposition groups, inertia groups | 3.5, 3.6, 3.10 |
| the Frobenius element $\Frob_P$ and its conjugacy class | 3.8, 3.10 |
| arithmetic versus geometric Frobenius | 3.7 |
| the Frobenius of an unramified prime in an abelian extension | 3.8(iv), 5.6(ii) |
| class field theory over $\Q$: Artin map, Kronecker-Weber | 5.5, 5.6 |
| Dirichlet characters as one-dimensional representations of $G_\Q$ | 5.7, 5.8 |
| class group and units (statements, examples) | 1.6, 2.5, 2.6, 4.5 |
| $\Z[\zeta_3]$ and $\Z[i]$ as Euclidean domains | 4.5 (proof in Chapter 2) |
| $3=-\zeta_3^2(1-\zeta_3)^2$; $\Z_3[\zeta_3]$ a DVR, $\pi=1-\zeta_3$, residue field $\F_3$, $\pi^2=-3$ up to a unit | 4.6, 4.7 (local interpretation in Chapter 7) |
| primes $\lambda$ above $\ell$ in the coefficient field of a newform; reduction mod $\lambda$ | 7.1, 7.2, 7.3, 7.4, 7.5 |
| density of primes; Chebotarev in number-field form (coordinated with Chapter 5) | 6.1, 6.2, 6.3 |
| primes inert in $\Q(\sqrt{\ell^*})$ and CM by that field ($a_p=0$ at inert primes) | 5.3, 6.3(v), 6.4, 6.5 |
| hook: Lemma lem:IV ($\Z_3[\zeta_3]$ as DVR) | 4.6, 4.7, 4.8, 3.12 |
| hook: Lemma lem:euler (Frobenius centralises or inverts $\sigma$ by $q\bmod3$) | 3.11, 3.12 |
| hook: Lemma lem:euler ($\Z_\ell[\zeta_3]=\End_{I_q}(V)$; $\chi_{-3}(q)$, $\chi_{-4}(q)$ on the invariant line; $L$-factor convention) | 4.9, 4.10, 3.7 |
| hook: Lemma lem:h0 ($a_p=0$ at primes inert in $\Q(\sqrt{\ell^*})$ forces CM; important_notes.md point 5) | 5.3, 6.4, 6.5 |
| hook: Lemma lem:crit (rings of integers $\mathcal O$, $\lambda\mid\ell$, maximal ideal of residue characteristic $\ell$) | 7.1, 7.2, 7.3 |
| hook: Lemma lem:old (enlarging $\mathcal O$ and $\lambda$; a prime above $\lambda$ in $\mathcal O[\alpha_p]$) | 7.2, 7.3, 6.2 |
| hook: the twist by $\Q(\sqrt{q^*})$ (Section 1.4, Lemma lem:twist, Theorems thm:twist, thm:quant) | 4.3, 4.4, 5.7, 5.8 |
| hook: $\chi_{-3}$, $\chi_{-4}$ of $\Q(\sqrt{-3})$ and $\Q(i)$ (table of Section 1, Proposition prop:forms) | 4.2, 5.8, 4.10 |
| Section 6 row: $\chi_{-3},\chi_{-4},\chi_{q^*},q^*,\ell^*$, Kronecker symbols (Chapters 2, 6) | 4.1, 4.2, 4.3, 5.3, 5.7, 5.8 |
| Section 6 row: image of inertia on $T_\ell E$ at additive primes, unipotent elements, $\Z_3[\zeta_3]$ (Chapters 4, 6, 7, 11) | 3.11, 3.12, 4.6, 4.7, 4.8, 4.10 |
| also: Section 1.1 ($I_p$, $\Frob_p$, $V^{I_p}$, $L_p$), Lemma lem:fpr ($L_p(A_f,1)=L_p(A_f(1),0)$) | 3.7, 3.10 |
| also: Chapter 5's black boxes (Frobenius, Dedekind's theorem, $\chi_d(\Frob_p)$, Kronecker-Weber, Chebotarev) | 3.8, 3.9, 3.10, 4.2, 5.5, 6.2 |

Exercises (Section 8 of the chapter), graded from easy to harder:
1. Compute $\mathcal O_K$ and $d_K$ for $\Q(\sqrt{-7})$ and $\Q(\sqrt{13})$, and factor $2$, $3$, $7$, $13$ in each.
   Show that Dedekind-Kummer with $\theta=\sqrt{-7}$ gives the wrong answer at $2$, and explain why (3.3(d)).
2. Show that $\Z[\sqrt{-3}]$ is not integrally closed and that $4=2\cdot2=(1+\sqrt{-3})(1-\sqrt{-3})$ are two
   factorisations into irreducibles there; what happens in $\Z[\zeta_3]$?
3. Factor $2$, $3$, $5$, $7$, $13$ in $\Z[i]$ and in $\Z[\zeta_3]$. Verify $3=-\zeta_3^2(1-\zeta_3)^2$,
   $\sqrt{-3}=1+2\zeta_3=\zeta_3(1-\zeta_3)$ and $(1-\zeta_3)^2=-3\zeta_3$.
4. Show that $p\ne2,5$ splits in $\Q(\sqrt{-5})$ iff $p\equiv1,3,7,9\pmod{20}$, and that the primes above $3$ and $7$ are
   not principal; deduce $h(\Q(\sqrt{-5}))\ge2$.
5. In $K=\Q(2^{1/3})$ factor $5$, $7$ and $31$ and check $\sum e_if_i=3$. Using 3.9 in the splitting field
   $\Q(2^{1/3},\zeta_3)$, determine $\Frob_p$ (up to conjugacy) for $p=5,7,31$ and explain why the residue degrees
   above $5$ differ.
6. Prove directly that an odd prime $p$ ramifies in $\Q(\sqrt d)$ iff $p\mid d$, without 3.4.
7. Factor $2$, $13$, $29$ in $\Q(\zeta_7)$ and check against 5.2. Identify the quadratic subfield and check that its
   splitting of each $p$ agrees with $\bigl(\frac p7\bigr)$.
8. Prove quadratic reciprocity from 4.2 and 5.3 (5.4), including $\bigl(\frac2p\bigr)$ via $\Q(\zeta_8)$.
9. Show that $\Q(\sqrt{q^*})$ is the only quadratic field ramified only at the odd prime $q$, and list the quadratic
   fields unramified outside $\{3,7\}$ (answer: $\Q(\sqrt{-3})$, $\Q(\sqrt{-7})$, $\Q(\sqrt{21})$). Which character is $\chi_S$
   for $S=\{3,7\}$, and what is its conductor?
10. Prove that $\Z_3[\zeta_3]$ is a DVR (4.7) and compute $v_\pi$ of $1+\zeta_3$, $2+\zeta_3$, $3$ and $\sqrt{-3}$
    (answers $0,1,2,1$).
11. Check the paper's Lemma lem:IV algebra: if $\sigma\in\GL_2(\Z_3)$ has order $3$ and determinant $1$, then $\Z_3^2$ is free
    of rank one over $\Z_3[\sigma]\simeq\Z_3[\zeta_3]$, and $\sigma\bmod3$ is a nontrivial unipotent with a fixed line. Give an
    explicit such $\sigma$ (for example the companion matrix of $X^2+X+1$).
12. Determine $\Z_\ell[\zeta_3]$ for $\ell=2,5,7$. For $\ell=7$ find the roots of $X^2+X+1$ mod $7$ and mod $49$
    (answers $2,4$ and $18,30$) and write down the idempotents of $\Z_7[\zeta_3]\simeq\Z_7\times\Z_7$ modulo $49$.
13. Check the paper's claim in Lemma lem:euler: if $\Phi\sigma\Phi^{-1}=\sigma^q$ with $\sigma$ of order $3$, then
    $\Phi(2\sigma+1)\Phi^{-1}=\chi_{-3}(q)(2\sigma+1)$; state and prove the analogue with $\tau$ of order $4$ and $\chi_{-4}(q)$, and
    deduce the entries $1-\chi_{-3}(q)q^{-s}$ and $1-\chi_{-4}(q)q^{-s}$ of the table of Section 1.
14. Check the paper's sign conventions: for $E$ with split multiplicative reduction at $q$ and
    $\rho(\Frob)=\begin{psmallmatrix}q&c'\\0&1\end{psmallmatrix}$, show that the arithmetic Frobenius acts on $(\ad V)^{I_q}$
    by $q$, and deduce that the factor $1-q^{-1-s}$ of the table requires the geometric Frobenius (3.7).
15. For $y^2=x^3-x$, show $a_p=0$ for every $p\equiv3\pmod4$ by the substitution $x\mapsto-x$, and compute $a_5=-2$,
    $a_{13}=6$, $a_{17}=2$ by counting points. Relate to 6.5(ii).
16. For 11a1 show, using 6.4 and $a_2=-2$, that $\bar\rho_{E,3}\not\simeq\bar\rho_{E,3}\otimes\chi_{-3}$. For $y^2=x^3-6x-8$ (Chapter 5,
    galois:ns-example) explain why $3\mid a_p$ for the primes $p\equiv2\pmod3$.
17. Let $K_f=\Q(\sqrt5)$ (level $23$, 7.5). Factor $2$, $5$, $11$ in $\Z[\frac{1+\sqrt5}2]$, find the roots of $X^2+X-1$
    mod $11$ (answers $3$, $7$), and describe the two reductions mod the primes above $11$.
18. Prove 7.3: if $\phi\colon\T\to\mathcal O$ and $\lambda\mid\ell$, then $\ker(\T\to\mathcal O/\lambda)$ is maximal of residue
    characteristic $\ell$; deduce the last step of the paper's Lemma lem:crit ($\ell\mid\#\T/(I+J)$).

## 11. Notes for the writer

Conventions to fix (Section 1 and Section 3 of the chapter, as `convention` environments):
* $\Qbar\subset\C$ fixed (Chapter 5, C1); $\bar{\mathbb Z}$ its ring of algebraic integers; primes of $\bar{\mathbb Z}$ written
  $\bar{\mathfrak P}$.
* Frobenius (3.7): $\Frob_{\mathfrak P}$, $\Frob_p$ are *arithmetic*; $\Frob_p^{-1}$ is geometric; $L$-factors are
  $\det(1-\Frob_p^{-1}p^{-s}\mid V^{I_p})^{-1}$. State the dictionary once, with the multiplicative example, and use the
  same words as Chapter 5 (C2). Appendix B (`ch:notation`) must record the same convention.
* $\chi_d$, $\chi_{q^*}$ (never $\chi_q$, decision D3), $\chi_{-3}$, $\chi_{-4}$, $\chi_S$, $\chi_{\ell^*}$ exactly as in Chapter 5 (C3, C4); the Dirichlet
  character attached to $\chi_d$ is $\bigl(\frac D\cdot\bigr)$ with $D$ the *discriminant*, not $d$ (e.g. $\chi_{-1}=\chi_{-4}$ has
  conductor $4$; $\chi_2$ has conductor $8$).
* $\Z_\ell[\zeta_3]$ means $\Z_\ell[X]/(X^2+X+1)=\Z_\ell\otimes\Z[\zeta_3]$, not a subring of $\Qbar_\ell$ (for $\ell\equiv1\pmod3$ it
  is $\Z_\ell\times\Z_\ell$). Say so explicitly where it first appears (4.9).
* $\sqrt{-3}$ always denotes $1+2\zeta_3=\zeta_3-\zeta_3^{-1}$ (fixing the sign); $\pi=1-\zeta_3$; $\zeta_3=e^{2\pi i/3}$ under
  $\Qbar\subset\C$. Do not use $\pi$ for $3.14159\ldots$ in the same section (write $\varpi$ for a general uniformiser).
* Labels prefixed `...:ant:...`; the names in the line-up are ready to use as label stems.

Pitfalls:
* Dedekind-Kummer needs $p\nmid[\mathcal O_K:\Z[\theta]]$; give the $\Q(\sqrt{-7})$ counterexample (3.3(d)). Equal $e$ and
  equal $f$ hold only in Galois extensions; give the $\Q(2^{1/3})$ example.
* "Unramified" for a representation means trivial on *every* inertia group above $p$ (equivalently one, by
  conjugacy); $\rho(\Frob_p)$ is defined only up to conjugacy and only for unramified $\rho$. At a ramified prime,
  "a Frobenius" is a coset of inertia; the paper's "$\Frob$" in Lemmas lem:euler and lem:tamfactor is such a lift,
  and every statement made there is independent of the lift (3.12; Chapter 7).
* Arithmetic versus geometric Frobenius: the paper's $L_p(A_f,s)$ at a multiplicative prime and its
  $L_p(A_f,1)=L_p(A_f(1),0)$ are correct only with the geometric Frobenius (Part 13, point 1); never "fix" the
  table, fix the convention. For the other types the eigenvalue sets are inversion-stable and nothing changes.
* The paper's "$\Z_\ell[\zeta_3]\simeq\End_{I_q}(V)$" is to be read as in 4.10(v) (Part 13, point 2); the argument only
  uses the trace-zero line and Frobenius's action on it.
* Lemma lem:h0 (important_notes.md point 5): present the CM fact (6.5) for the *quadratic* character $\chi_{\ell^*}$
  and say explicitly that the finiteness of $h_\ell(E)$ follows from the determinant argument of Chapter 5, not
  from CM. Do not reproduce the paper's sentence "$\rho\simeq\rho\otimes\chi_\ell$ would force $a_p=0$ ...".
* $\chi_{\ell^*}\ne\bar\chi_\ell$ for $\ell\ge5$ (important_notes.md point 6); in 5.8 put both in the table.
* The Kronecker symbol at $p=2$ ($D\equiv\pm1$ versus $\pm3\bmod8$) and the sign of $q^*$ are where errors creep in; the
  verification log checks them; keep the explicit $p=2$ rows.
* Idelic class field theory has two sign normalisations (5.6(iii)); if the chapter mentions ideles at all, state
  which, and prefer the explicit cyclotomic form 5.6(i), (ii), which is all the paper needs.
* Chebotarev: only Dirichlet density positivity is needed downstream; do not present the natural-density
  version as proved. Brauer-Nesbitt is in Chapter 4 and its Galois form in Chapter 5; cite, do not redo.
* 6.5: Deuring's theorem ($a_p=0$ at inert good primes) has a two-line proof from "$\alpha\colon\rho\to\rho\otimes\chi_K$"; give
  it as a sketch with the Galois action on endomorphisms quoted from Chapter 9. The converse and Serre's density
  zero result are stated only.
* Minkowski bound for $\Q(\sqrt{-11})$ is $2.11>2$: class number one there needs "$2$ is inert" (corrected in 2.5).
* 7.5 depends on LMFDB data (23.2.a.a) that the outline author recalled but could not verify offline: check
  the Hecke polynomial $X^2+X-1$ of $T_2$ before quoting it, or replace the example by the algebra alone.

Leave to other chapters:
* Chapter 2: Euclidean algorithms in $\Z[i]$ and $\Z[\zeta_3]$, Legendre/Jacobi/Kronecker symbols, quadratic reciprocity
  by Gauss sums, Dirichlet characters and conductors, cyclotomic polynomials, $v_p$ on $\Q$.
* Chapter 5: the Galois groups of $\Q(\zeta_n)$ and $\Q(\sqrt d)$, $\Q(\sqrt{\ell^*})\subset\Q(\zeta_\ell)$ via the discriminant or
  Gauss sums, Kummer theory, Chebotarev over $\Q$ and its Brauer-Nesbitt corollaries, the index-two criterion,
  complex conjugation and absolute irreducibility, the determinant argument for $h_\ell(E)\le1$.
* Chapter 7: completions, Hensel, $\Q_p$, local fields, $D_p\simeq G_{\Q_p}$, the higher ramification groups, tame
  inertia $\prod_{\ell\ne p}\Z_\ell(1)$ and $\Frob\,t\,\Frob^{-1}=t^p$ in profinite form, the local Kronecker-Weber and local
  class field theory, Artin conductors, Weil-Deligne representations, the local interpretation of $\Z_3[\zeta_3]$.
* Chapters 9 to 11: CM theory proper, Kraus's theorem, the inertia images of $\rho_{E,\ell}$, the elliptic-curve
  content of Lemmas lem:IV, lem:euler, lem:h0 and Proposition prop:ns; this chapter supplies only the
  arithmetic of the rings and fields involved.
* Chapters 12, 13, 15: Hecke algebras, newforms, their Galois representations; here only the algebraic
  integrality and the primes $\lambda$.

## 12. Verification log (computations done for this outline)

Short Python/sympy scripts in `/tmp/ch06` (`check1.py`, `check2.py`, `check3.py`, and one-liners).
* Splitting in quadratic fields versus the Kronecker symbol $\bigl(\frac Dp\bigr)$ (including $p=2$), by factoring the
  minimal polynomial of $\sqrt d$ or $(1+\sqrt d)/2$ mod $p$: $23$ fundamental discriminants
  ($-3,-4,-7,-8,-11,-15,-19,-20,-23,5,8,12,13,-163,17,21,24,-24,28,-52,-115,85,-67$), all $p<400$: no mismatch.
* $p\ne\ell$ inert in $\Q(\sqrt{\ell^*})$ iff $\bigl(\frac p\ell\bigr)=-1$, including $p=2$: $\ell\le23$, $p<2000$: no mismatch.
  $\chi_{-3}(p)=1$ iff $p\equiv1\pmod3$, $\chi_{-4}(p)=1$ iff $p\equiv1\pmod4$: $p<3000$. Splitting in $\Q(\sqrt{-5})$ iff
  $p\equiv1,3,7,9\pmod{20}$: $p<3000$. Split primes of $\Q(\sqrt{-7})$ are $\equiv1,2,4\pmod7$.
* Discriminants of the quadratic generators equal $D$; $\disc(\Phi_n)$ equals the formula of 5.1(iii) for
  $n\in\{3,4,5,7,8,9,11,12,13,15,16,20\}$ (e.g. $-3$, $-4$, $125$, $-16807$, $256$).
* Splitting in $\Q(\zeta_n)$: $\Phi_n\bmod p$ has $\varphi(m)/f$ factors of degree $f$ with multiplicity $\varphi(p^a)$, for all
  $3\le n\le40$, $n\not\equiv2\bmod4$, $p<80$: no mismatch. Examples of 5.2 confirmed.
* Dedekind-Kummer examples: $X^3-2$ mod $2,3,5,7,11,31$ (patterns $1^3$, $1^3$, $(1)(2)$, $(3)$, $(1)(2)$, $(1)(1)(1)$;
  mod $5$: $(X+2)(X^2-2X-1)$); $X^2+X+1$ mod $2,3,5,7,13$ (mod $7$ roots $2,4$); $X^2+7\equiv(X+1)^2$ and $X^2-X+2\equiv
  X(X+1)$ mod $2$; $X^2+5$ mod $2,3$; $X^2+1$ mod $2,3,5,13$.
* Identities in $\Z[\zeta_3]$ (reduction mod $z^2+z+1$): $\pi^2=-3\zeta_3$, $-\zeta_3^2\pi^2=3$, $(1+2\zeta_3)^2=-3$, $\zeta_3\pi=1+2\zeta_3$,
  $(3+\zeta_3)(3+\zeta_3^2)=7$, $(2-\zeta_3)(2-\zeta_3^2)=7$, $(4+\zeta_3)(4+\zeta_3^2)=13$, $1+\zeta_3=-\zeta_3^2$; in $\Z[i]$: $-i(1+i)^2=2$,
  $(2+i)(2-i)=5$, $(3+2i)(3-2i)=13$.
* Representations: $p=a^2-ab+b^2$ iff $p=3$ or $p\equiv1\pmod3$ ($p<200$); $p=x^2+3y^2$ iff $p\equiv1\pmod3$ ($5\le p<300$); $p=x^2+y^2$
  iff $p=2$ or $p\equiv1\pmod4$ ($p<300$).
* Minkowski bounds $(2/\pi)\sqrt{|d|}$: $1.10$ ($-3$), $1.27$ ($-4$), $1.68$ ($-7$), $1.80$ ($-8$), $2.11$ ($-11$), $2.85$ ($-20$),
  $3.05$ ($-23$); real: $1.12$ ($5$), $1.41$ ($8$).
* CM curves: $a_p=0$ at every good $p<300$ inert in the CM field, and $a_p\ne0$ at $26$ to $29$ split primes, for
  $y^2=x^3-x$ ($\Delta=64$), $y^2=x^3+1$ ($\Delta=-432$), 121b1 $[0,-1,1,-7,10]$ ($\Delta=-11^3$), 27a1 $[0,0,1,0,-7]$
  ($\Delta=-3^9$). For $y^2=x^3-x$: $a_5=-2$, $a_{13}=6$, $a_{17}=2$, $a_{29}=-10$, $a_{37}=-2$.
* 11a1: $a_2=-2$, $a_3=-1$, $a_5=1$, $a_7=-2$, $a_{13}=4$, $a_{17}=-2$, $a_{19}=0$, $a_{23}=-1$, $a_{29}=0$ (point counts).
* Roots of $X^2+X+1$ mod $49$: $18$, $30$; of $X^2+X-1$ mod $11$: $3$, $7$.
* Not verified (recalled): the $q$-expansion of 23.2.a.a (7.5); the theorem numbers flagged "check".

## 13. Points for important_notes.md

Points in the area of Chapter 6 not already in important/important_notes.md (points 5 and 6 there, on Lemma
lem:h0 and on $\chi_{\ell^*}$ versus $\bar\chi_\ell$, are used above and not repeated).

1. **Section 1.1 (definition of $L_p(A_f,s)$), Lemma lem:euler (type $\mathrm I_n$), Lemma lem:fpr: the Frobenius in the
   local $L$-factor must be the geometric one.** Problem: Section 1.1 defines $L_p(A_f,s)=\det(1-\Frob_pp^{-s}\mid
   A_f^{I_p})^{-1}$ with $A_f=\ad V$, $V=V_\ell E$, without saying which Frobenius; the proof of Lemma lem:tamfactor uses
   the arithmetic Frobenius on $T=T_\ell E$, with $\rho(\Frob)=\begin{psmallmatrix}\varepsilon q&c'\\0&\varepsilon\end{psmallmatrix}$ and
   "the adjoint action sends $e$ to $qe$". With that (arithmetic) Frobenius, the invariant line $(\ad V)^{I_q}=\Q_\ell e$
   at a multiplicative prime has eigenvalue $q$, so the formula of Section 1.1 would give $1-q^{1-s}$, not the
   tabulated $1-q^{-1-s}$; and the proof of Lemma lem:euler says "a line with eigenvalue $q^{-1}$". The table, the
   value $e_\ell$, PARI's factors, Lemma lem:fpr's "$L_p(A_f,1)^{-1}=L_p(A_f(1),0)^{-1}$" and the statement
   "$\det(1-\Frob_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}$" are all correct with the *geometric* Frobenius $\Frob_p^{-1}$ (with
   the arithmetic one the last determinant at a multiplicative prime is $1-q^2$, which has the same $\ell$-adic
   valuation but is a different number). Fix: in Section 1.1 write "$\det(1-\Frob_p^{-1}p^{-s}\mid A_f^{I_p})^{-1}$, with
   $\Frob_p$ an arithmetic Frobenius" (or "with $\Frob_p$ a geometric Frobenius"), and in the proof of Lemma lem:euler
   "eigenvalue $q^{-1}$ for the geometric Frobenius". Only the multiplicative and $\mathrm I_n^*$ cases are affected; for
   the other types the eigenvalues ($\pm1$, $\alpha/\beta,1,\beta/\alpha$) are stable under inversion. No numerical
   statement changes. Sure: high (direct computation with the paper's own matrices; consistent with $L(V(1),s)=
   L(V,s+1)$ only for the geometric convention).

2. **Lemma lem:euler, proof (types II, II$^*$, IV, IV$^*$): "$\sqrt{-3}\in\Z_\ell[\zeta_3]\simeq\End_{I_q}(V)$".** Problem
   (imprecise, no effect on the result): $V$ is a $\Q_\ell$-vector space, so $\End_{I_q}(V)$ is a $\Q_\ell$-algebra; it is
   $\Q_\ell[\sigma]\simeq\Q_\ell\otimes_\Q\Q(\zeta_3)$, which is a field only for $\ell\not\equiv1\pmod3$ and is $\Q_\ell\times\Q_\ell$ for
   $\ell\equiv1\pmod3$. The integral statement is $\End_{I_q}(T)=\Z_\ell[\sigma]\simeq\Z_\ell\otimes_\Z\Z[\zeta_3]$ ($T$ is free of rank
   one over $\Z_\ell[\sigma]$ in all cases; 4.10(v)). Fix: write "$(\ad V)^{I_q}$ is the trace-zero part of
   $\End_{I_q}(V)=\Q_\ell[\sigma]\simeq\Q_\ell\otimes\Q(\zeta_3)$, the line spanned by $2\sigma+1$, whose square is $-3$". The argument
   (Frobenius acts on this line through $\Gal(\Q(\zeta_3)/\Q)$, i.e. by $\chi_{-3}(q)$) is unchanged; the same remark
   applies to the types III, III$^*$ with $\Q_\ell\otimes\Q(i)$ and the element $\tau$ ("the diagonal element"). Sure: high.

3. **Lemma lem:IV, proof: "$\Z_3[\sigma]/(\sigma^2+\sigma+1)\simeq\Z_3[\zeta_3]$".** Problem (notation only): $\Z_3[\sigma]$ already
   denotes the subring of $\End(T)$ generated by $\sigma$, in which $\sigma^2+\sigma+1=0$; the intended object is
   $\Z_3[X]/(X^2+X+1)$, and the claim is $\Z_3[\sigma]\simeq\Z_3[X]/(X^2+X+1)$ (true because $\sigma$ is not a scalar, so
   $X^2+X+1$ is its minimal polynomial). Fix: "$T$ is a module over $\Z_3[\sigma]\simeq\Z_3[X]/(X^2+X+1)=\Z_3[\zeta_3]$".
   Sure: high; purely expository.

4. **Supplement to important_notes.md point 5 (Lemma lem:h0, CM).** Even in the corrected reading (with the
   quadratic character $\chi_{\ell^*}$ in place of $\chi_\ell$), the CM alternative cannot arise in the range of Theorem
   thm:main: CM by $\Q(\sqrt{\ell^*})$ requires $\Q(\sqrt{\ell^*})$ imaginary of class number one, i.e.
   $\ell\in\{3,7,11,19,43,67,163\}$, and a prime ramified in the CM field divides the conductor (conductor-discriminant
   formula for $\rho_{E,\ell}\simeq\Ind\psi$), so $\ell\mid N$ (examples 27a1, 36a1 at $\ell=3$, 121b1 at $\ell=11$). So the phrase
   "for $E$ without complex multiplication" in Lemma lem:h0 can be dropped altogether, as point 5 already
   suggests for other reasons. Sure: high for the class number one list and the examples; medium-high for the
   conductor statement (standard, but the outline author did not re-derive the conductor-discriminant formula
   for induced representations here).
