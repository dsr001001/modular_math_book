# Line-up for Chapter 06: Algebraic number theory (`ch:ant`, `chapters/ch06_ant.tex`)

Stage 1 output (core results in teaching order). Target length 1,950 lines of LaTeX excluding the card.
Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference.
Frobenius is *arithmetic* throughout (Convention 5.6 below): $\Frob_P(x)\equiv x^{N\mathfrak p}\pmod P$.

## 0. What the chapter must deliver (checked against PLAN.md Section 4 entry and Section 6 map)

Scope items of the PLAN entry, each mapped to an item below:
number fields, rings of integers, integral closure (1.1-1.4); Dedekind domains and unique factorisation of
ideals (2.1-2.2); norms of ideals (2.3); splitting of primes, $e,f,g$, $\sum e_if_i=n$, ramified/inert/split
(3.1); discriminant and ramification (1.4, 3.3); quadratic fields in full, Kronecker symbol, the quadratic
character of $\Q(\sqrt d)$ as a Dirichlet character (4.1-4.3); cyclotomic fields, splitting governed by $p
\bmod n$, $\Q(\zeta_3)=\Q(\sqrt{-3})$, $\Q(\sqrt{\ell^*})\subset\Q(\zeta_\ell)$ (5.1-5.3); decomposition and
inertia groups, $\Frob_P$, its conjugacy class, Frobenius in abelian extensions (3.5-3.6); Artin map,
Kronecker-Weber, Dirichlet characters versus one-dimensional representations of $G_\Q$ (5.4-5.7); class
group and units (1.6, 2.5); $\Z[\zeta_3]$, $\Z[i]$, primes above $3$, $\Z_3[\zeta_3]$ a DVR with uniformiser
$\pi=1-\zeta_3$ (4.4-4.8); primes $\lambda\mid\ell$ in the coefficient field of a newform, reduction mod
$\lambda$ (7.1-7.3); densities and Chebotarev in number-field form (6.1-6.4); primes inert in
$\Q(\sqrt{\ell^*})$ and CM (6.5).

Paper hooks of the PLAN entry: Lemma lem:IV ($\Z_3[\zeta_3]$ DVR: 4.6, 4.7); Lemma lem:euler (Frobenius
centralises or inverts $\sigma$ according to $q\bmod3$: 3.8, 3.9, 3.10; $\Z_\ell[\zeta_3]=\End_{I_q}(V)$,
the line spanned by $\sqrt{-3}$, the action of Frobenius on it by $\chi_{-3}(q)$, and the $\Z_\ell[i]$
analogue for types III: 4.5, 4.8, 4.9); Lemma lem:h0 ($a_p=0$ at primes inert in $\Q(\sqrt{\ell^*})$ forces
CM: 6.4, 6.5); Lemma lem:crit and Lemma lem:old (rings of integers $\mathcal O$, primes $\lambda\mid\ell$,
"after enlarging $\mathcal O$ and $\lambda$", "a prime above $\lambda$ in $\mathcal O[\alpha_p]$", "maximal
ideal of residue characteristic $\ell$": 7.1-7.3); the twist by $\Q(\sqrt{q^*})$ of Section 1.4 and
Lemma lem:twist, the character $\chi_S$ of Theorem thm:twist (4.3, 5.3); $\chi_{-3}$, $\chi_{-4}$ of
$\Q(\sqrt{-3})$ and $\Q(i)$ (4.3-4.5). Section 6 map rows: "$\chi_{-3},\chi_{-4},\chi_q,q^*,\ell^*$,
Kronecker symbols" (4.1-4.3, 5.3); "image of inertia at additive primes, $\Z_3[\zeta_3]$" (3.8-3.10,
4.6-4.9); "Chebotarev" (6.3-6.4).

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
A *Dedekind domain* is a Noetherian integrally closed integral domain in which every nonzero prime ideal
is maximal. Theorem: $\mathcal O_K$ is a Dedekind domain (Noetherian since free of finite rank over $\Z$;
integrally closed by 1.2; $\mathcal O_K/\mathfrak p$ is a finite integral domain, hence a field, because
$\mathfrak p\cap\Z=p\Z\ne0$). A Noetherian domain $R$ is Dedekind iff $R$ is not a field and every
localisation $R_{\mathfrak p}$ at a nonzero prime is a discrete valuation ring (`ch:modules` supplies
DVRs and localisation); PIDs are Dedekind. Reference: Neukirch I.3.1, I.11.5 (cite I.3 and I.11);
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
\simeq R/\mathfrak p$. (ii) In a Dedekind domain every ideal is generated by two elements, one of which
may be chosen arbitrarily (nonzero) in it. (iii) A Dedekind domain with finitely many primes is a PID;
a Dedekind domain is a UFD iff it is a PID. (iv) For a nonzero prime $\mathfrak p$ of $\mathcal O_K$ the
localisation $\mathcal O_{K,\mathfrak p}$ is a DVR with maximal ideal $\mathfrak p\mathcal O_{K,
\mathfrak p}$, residue field $\mathcal O_K/\mathfrak p$ and valuation $v_{\mathfrak p}$. Reference:
Neukirch I.3.6, I.3.9, I.11 (cite I.3); Marcus Ch. 3 (Thm 17, Cor. 2 to Thm 16: check). Paper:
background (the product decomposition $\mathcal O\otimes\Z_\ell$ in 7.1; $\Z_3[\zeta_3]/(\pi^2)$).

### 2.5 `thm:ant:classgroup` (definition and theorem) R
$\Cl(K)=J_K/P_K$, $P_K$ the principal fractional ideals; $h_K=\#\Cl(K)$ is the *class number*; $h_K=1$ iff
$\mathcal O_K$ is a PID iff it is a UFD. Theorem (Minkowski): $\Cl(K)$ is finite; every ideal class
contains an integral ideal of norm at most $M_K=(4/\pi)^{r_2}(n!/n^n)|d_K|^{1/2}$; and $|d_K|>1$ for
$K\ne\Q$, so every number field other than $\Q$ has a ramified prime (with 3.3). Examples: $h=1$ for
$\Q(i)$, $\Q(\sqrt{-3})$, $\Q(\sqrt{-7})$, $\Q(\sqrt{-11})$, $\Q(\sqrt2)$, $\Q(\sqrt5)$ (Minkowski bound
$<2$, or Euclidean for $\Z[i]$, $\Z[\zeta_3]$ by `ch:rings`); $h(\Q(\sqrt{-5}))=2$; $h(\Q(\sqrt{-23}))
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
