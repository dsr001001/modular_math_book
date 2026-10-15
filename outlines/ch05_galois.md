# Chapter 05: Galois theory, finite and infinite (`ch:galois`, `chapters/ch05_galois.tex`)

Stage 1 line-up. Part II (Number fields and local fields). Target length 2,030 lines of LaTeX (card excluded; see Part 4),
inside the 1,000 to 2,200 range of PLAN.md Section 7.3.

## 0. What this chapter is for

The paper uses Galois theory in five places, and the chapter is built around them.

1. The hypothesis of Theorem thm:main, Theorem thm:dfg37, Theorem thm:dfg27 and the set $S_f$ of Section 4.2:
   "$\bar\rho_{E,\ell}$ is absolutely irreducible when restricted to $\Gal(\overline{\Q}/\Q(\sqrt{\ell^*}))$".
   The chapter must define $G_\Q$, its open subgroup $G_{\Q(\sqrt{\ell^*})}$ of index two, the field
   $\Q(\sqrt{\ell^*})\subset\Q(\zeta_\ell)$ and its quadratic character $\chi_{\ell^*}$, the restriction of a
   representation to an open subgroup, and the equivalence (for $\bar\rho$ absolutely irreducible)
   "not absolutely irreducible on $G_{\Q(\sqrt{\ell^*})}$" iff "$\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$"
   iff "$\bar\rho$ is induced from $G_{\Q(\sqrt{\ell^*})}$" (used in Lemma lem:h0 and Proposition prop:ns).
2. Proposition prop:ns: the image of $G_{\Q(\sqrt{-3})}$ under $\bar\rho_{E,3}$ is the determinant-one
   subgroup of the image (because $\det\bar\rho_{E,3}=\chi_{-3}$ cuts out $\Q(\sqrt{-3})$), and the
   factorisation pattern of the $3$-division polynomial is the orbit pattern of the image on the four lines.
3. Lemma lem:old: "$\bar\rho_h\simeq\bar\rho$ by Chebotarev and Brauer-Nesbitt": a semisimple mod $\ell$
   representation of $G_\Q$ is determined by the characteristic polynomials of Frobenius on a density-one set.
4. Lemma lem:tamagawa-exp: Kummer theory, "$F(u^{1/\ell^t})=F$ iff $u$ is an $\ell^t$-th power in $F$"
   when $\mu_{\ell^t}\subset F$.
5. Lemma lem:tamfactor: the Kummer class $\kappa$ of the Tate parameter, as an explicit $1$-cocycle with values in
   $\Z_\ell(1)$, and the conjugation rule $\kappa(\sigma\tau\sigma^{-1})=\chi_\ell(\sigma)\kappa(\tau)$, which is
   the abstract form of $\Frob\,t\,\Frob^{-1}=t^{q}$, i.e. $\Frob^{-1}t\Frob=t^{q^{-1}}$, of Chapter 7.
6. Lemma lem:h0, Conjecture conj:euler and Section 1.3 of the paper: the difference between the reduced
   cyclotomic character $\bar\chi_\ell$ and the quadratic character $\chi_{\ell^*}=\bar\chi_\ell^{(\ell-1)/2}$
   (they coincide only for $\ell=3$), and the determinant argument "$\det(\rho\otimes\chi)=\chi^2\det\rho$"
   which shows that $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$ forces $\ell=3$ and $k=1$
   (item galois:twist below; see also Section 8 of this outline, "Points for important_notes.md").

Everything else in the chapter (field extensions, splitting fields, the fundamental theorem, cyclotomic fields,
Galois groups of polynomials, profinite groups, continuous representations, the cyclotomic character,
complex conjugation, Chebotarev) is the minimal path from the reader's background (RHB, linear algebra) to
these five points, plus what Chapters 6, 7, 11, 15, 17 need from Galois theory.

## 1. Global conventions fixed in this chapter

* **C1 (one algebraic closure).** $\Qbar\subset\C$ is the field of algebraic numbers; every algebraic extension
  of $\Q$ is taken inside $\Qbar$; $G_\Q=\Gal(\Qbar/\Q)$; for $K\subset\Qbar$, $G_K=\Gal(\Qbar/K)\subset G_\Q$.
  For a general field $F$, $F^{\mathrm{sep}}\subset\Fbar$ is a separable closure and $G_F=\Gal(F^{\mathrm{sep}}/F)$.
* **C2 (Frobenius is arithmetic).** Wherever a Frobenius element appears (the black box of Section 9, made
  precise in Chapter 6), $\Frob_p$ is the *arithmetic* Frobenius: it induces $x\mapsto x^p$ on residue fields,
  acts on $\mu_n$ ($p\nmid n$) by $\zeta\mapsto\zeta^p$, and $\chi_\ell(\Frob_p)=p$. This is the paper's
  convention (proof of Lemma lem:tamfactor: "the arithmetic Frobenius acts ... as $q^{-1}\rho(\Frob)$").
* **C3 (quadratic characters).** For $d\in\Q^\times\setminus(\Q^\times)^2$, $\chi_d\colon G_\Q\to\{\pm1\}$ is
  $\sigma\mapsto\sigma(\sqrt d)/\sqrt d$; it depends only on $d$ modulo squares and has kernel $G_{\Q(\sqrt d)}$.
  For an odd prime $q$ put $q^*=(-1)^{(q-1)/2}q$; $\chi_{q^*}$ is the character
  of $\Q(\sqrt{q^*})$, "the quadratic character of conductor $q$", which the paper writes $\chi_q$ (the book never does: PLAN.md 7.5, decision D3); $\chi_{-3}$ and $\chi_{-4}$ are the
  characters of $\Q(\sqrt{-3})$ and $\Q(i)$. Chapter 2 defines the same symbols as Dirichlet characters
  (Kronecker symbols); the two agree through $\chi_d(\Frob_p)=\bigl(\tfrac{D}{p}\bigr)$ (Kronecker symbol) for every prime
  $p\nmid D$, $D$ the discriminant of $\Q(\sqrt d)$, proved in Chapter 6.
* **C4 (the cyclotomic character and its reduction).** $\chi_\ell\colon G_\Q\to\Z_\ell^\times$ is defined by
  $\sigma(\zeta)=\zeta^{\chi_\ell(\sigma)}$ for all $\zeta\in\mu_{\ell^\infty}$; $\bar\chi_\ell\colon G_\Q\to\F_\ell^\times$
  is its reduction. $\chi_{\ell^*}=\bar\chi_\ell^{(\ell-1)/2}$ is the quadratic character of $\Q(\sqrt{\ell^*})$;
  $\chi_{\ell^*}=\bar\chi_\ell$ if and only if $\ell=3$.
* **C5 (representations).** A representation of a profinite group $G$ is a continuous homomorphism
  $\rho\colon G\to\GL_n(k)$ where $k$ is a finite field or $\Fbar_\ell$ with the discrete topology, or a finite
  extension $E$ of $\Q_\ell$ (or $\Zl$-lattice inside $E^n$) with the $\ell$-adic topology. "$\rho$ continuous into
  $\GL_n(\Qbar_\ell)$" means: into $\GL_n(E)$ for some finite $E/\Q_\ell$, continuously. For $T$ a free
  $\Zl$-module with continuous action, $\rho\bmod\ell^k$ is the action on $T/\ell^kT$ and $\bar\rho=\rho\bmod\ell$.
  Irreducible, absolutely irreducible, semisimplification $\rho^{ss}$, $\rho\otimes\chi$, $\Ind$, $\Res$ are as in
  Chapter 4. "$\rho$ is absolutely irreducible on $G_K$" means: $(\rho\otimes\bar k)|_{G_K}$ is irreducible.
* **C6 (Kummer characters live in $\mu_n$).** $\chi_a\colon G_F\to\mu_n$ is a homomorphism to $\mu_n$; it is
  identified with a homomorphism to $\Z/n\Z$ only after a primitive $\zeta_n$ is chosen.
  $\Zl(1)=\varprojlim_k\mu_{\ell^k}$ (transition maps $\zeta\mapsto\zeta^\ell$), written additively when
  convenient, with $G_F$ acting through $\chi_\ell$.
* **C7 (typography).** No em dash, no en dash, no double or triple hyphen, ASCII source, `\ell` not a Unicode letter, labels
  prefixed `...:galois:`.

## 2. Line-up of the core results, in teaching order

Format of each item: **name** (kind). Statement. *Rigour.* Reference. Paper use.

### Section 1. Field extensions and algebraic elements

**galois:field-extension-degree** (definition + proposition). A field extension $L/F$ is a field $L$ containing
$F$ as a subfield; its degree is $[L:F]=\dim_F L\in\{1,2,\dots\}\cup\{\infty\}$. *Tower law:* for
$F\subset L\subset M$, $[M:F]=[M:L]\,[L:F]$ (with the convention $\infty\cdot n=\infty$): if $(x_i)$ is an
$F$-basis of $L$ and $(y_j)$ an $L$-basis of $M$, then $(x_iy_j)$ is an $F$-basis of $M$.
*Proved here.* Lang, Algebra, V.1 (Proposition 1.2); Dummit-Foote 13.2. Background.

**galois:algebraic-element** (definition + proposition). $\alpha\in L$ is algebraic over $F$ if $f(\alpha)=0$
for some nonzero $f\in F[x]$, transcendental otherwise. If $\alpha$ is algebraic, the kernel of
$F[x]\to L$, $x\mapsto\alpha$, is generated by a unique monic irreducible polynomial $m_{\alpha,F}$, the minimal
polynomial; $F(\alpha)=F[\alpha]\simeq F[x]/(m_{\alpha,F})$ and $[F(\alpha):F]=\deg m_{\alpha,F}$;
$g(\alpha)=0$ for $g\in F[x]$ iff $m_{\alpha,F}\mid g$. Conversely if $[F(\alpha):F]<\infty$ then $\alpha$ is
algebraic. Examples: $\sqrt 2$, $\zeta_n$, $2^{1/3}$; $\pi$ is transcendental (stated).
*Proved here.* Lang V.1; Dummit-Foote 13.1, 13.2. Background.

**galois:algebraic-extensions** (proposition). (a) A finite extension is algebraic. (b) If
$\alpha_1,\dots,\alpha_r$ are algebraic over $F$ then $F(\alpha_1,\dots,\alpha_r)$ is finite over $F$, of degree
at most $\prod\deg m_{\alpha_i,F}$. (c) The elements of $L$ algebraic over $F$ form a subfield of $L$.
(d) If $M/L$ and $L/F$ are algebraic, so is $M/F$. (e) A finite extension is generated by finitely many
algebraic elements. *Proved here.* Lang V.1. Background.

**galois:algebraic-closure** (theorem). (a) Every field $F$ has an algebraic closure $\Fbar$: an algebraic
extension of $F$ which is algebraically closed; it is unique up to $F$-isomorphism (not up to unique
isomorphism). (b) If $L/F$ is algebraic and $\sigma\colon F\to\Omega$ is an embedding into an algebraically
closed field $\Omega$, then $\sigma$ extends to an embedding $L\to\Omega$. (c) $\Qbar=\{z\in\C: z$ algebraic over
$\Q\}$ is an algebraic closure of $\Q$; it is countable, and $\C$ is not algebraic over $\Q$.
*Stated; reference* for (a) and (b) (Zorn's lemma argument sketched in one paragraph); (c) proved here from
the fundamental theorem of algebra (assumed from complex analysis). Lang V.2;
Dummit-Foote 13.4. Background: $\Qbar$ and $G_\Q$ throughout the paper.

### Section 2. Splitting fields, normality, separability

**galois:splitting-field** (theorem). Let $f\in F[x]$ be nonconstant. A splitting field of $f$ over $F$ is an
extension $L=F(r_1,\dots,r_n)$ with $f=c\prod(x-r_i)$ in $L[x]$. (a) A splitting field exists, of degree
at most $n!$ over $F$ (in fact dividing $n!$; Exercise). (b) *Extension of isomorphisms:* if $\phi\colon F\to F'$ is a field
isomorphism, $L$ a splitting field of $f$ over $F$ and $L'$ a splitting field of $\phi(f)$ over $F'$, then
$\phi$ extends to an isomorphism $L\to L'$; the number of such extensions is at most $[L:F]$, with equality
if $f$ is separable. (c) In particular any two splitting fields of $f$ over $F$ are $F$-isomorphic, and the
splitting field of $f$ inside a fixed $\Fbar$ is unique. The same holds for a family of polynomials (splitting
field of a set $S\subset F[x]$). *Proved here* ((a), (b), (c) for one polynomial; the family case sketched).
Lang V.3; Dummit-Foote 13.4. Background.

**galois:normal-extension** (definition + proposition). An algebraic extension $L/F$ inside $\Fbar$ is normal
if the following equivalent conditions hold: (i) every irreducible polynomial in $F[x]$ with one root in $L$
splits into linear factors in $L[x]$; (ii) $L$ is the splitting field over $F$ of a family of polynomials;
(iii) every $F$-embedding $L\to\Fbar$ has image $L$ (so $\mathrm{Emb}_F(L,\Fbar)=\Aut(L/F)$). A finite
extension $L/F$ has a normal closure (the smallest normal extension of $F$ inside $\Fbar$ containing $L$:
the splitting field of the minimal polynomials of generators), unique inside $\Fbar$, finite over $F$.
Normality is not transitive: $\Q\subset\Q(\sqrt2)\subset\Q(2^{1/4})$. *Proved here.* Lang V.3 (Theorem 3.3);
Dummit-Foote 14.1. Background.

**galois:separability** (definition + proposition). A polynomial $f\in F[x]$ is separable if it has no repeated
root in $\Fbar$, equivalently $\gcd(f,f')=1$. (a) An irreducible $f$ is inseparable iff $f'=0$ iff
$\operatorname{char}F=p>0$ and $f\in F[x^p]$. (b) $F$ is perfect (every irreducible polynomial is separable)
iff $\operatorname{char}F=0$ or $\operatorname{char}F=p$ and $F=F^p$; fields of characteristic $0$, finite
fields and algebraically closed fields are perfect. (c) An algebraic element is separable if its minimal
polynomial is; an algebraic extension is separable if all its elements are; over a perfect field every
algebraic extension is separable. (d) For $L/F$ finite, the separable degree $[L:F]_s=\#\mathrm{Emb}_F(L,\Fbar)$
divides $[L:F]$, with equality iff $L/F$ is separable; separable degree is multiplicative in towers.
(e) *Primitive element theorem:* a finite separable extension is simple, $L=F(\theta)$; more generally a finite
extension is simple iff it has finitely many intermediate fields. *Proved here* ((a) to (d) and (e) for
infinite $F$; finite $F$ by cyclicity of $\F_q^\times$ from Chapter 2). Lang V.4 (Theorem 4.6); Dummit-Foote 13.5,
14.4. Background.

**galois:separable-closure** (definition). $F^{\mathrm{sep}}=\{\alpha\in\Fbar:\alpha$ separable over $F\}$ is a
field, Galois over $F$ (Section 3), and equals $\Fbar$ when $F$ is perfect; in particular
$\Q^{\mathrm{sep}}=\Qbar$, $\F_q^{\mathrm{sep}}=\Fbar_q$, $\Q_p^{\mathrm{sep}}=\overline{\Q}_p$.
*Proved here.* Lang V.4. Background (definition of $G_F$).

### Section 3. Galois extensions and the fundamental theorem

**galois:dedekind-independence** (theorem, Dedekind-Artin). Let $G$ be a group (or monoid) and $L$ a field.
Distinct homomorphisms $\chi_1,\dots,\chi_n\colon G\to L^\times$ are linearly independent over $L$: if
$\sum a_i\chi_i(g)=0$ for all $g\in G$ with $a_i\in L$, then all $a_i=0$. In particular distinct field
embeddings $L\to\Omega$ are linearly independent over $\Omega$. *Proved here.* Lang VI.4 (Theorem 4.1);
Dummit-Foote 14.2 (Theorem 7). Used for Artin's theorem and Hilbert 90.

**galois:artin-fixed-field** (theorem, Artin). Let $L$ be a field, $G\subset\Aut(L)$ a finite subgroup, and
$F=L^G=\{x\in L:\sigma x=x$ for all $\sigma\in G\}$. Then $L/F$ is finite, normal and separable, $[L:F]=\#G$,
and $\Aut(L/F)=G$. Conversely, for any finite extension $L/F$, $\#\Aut(L/F)\le[L:F]$, with equality iff
$L/F$ is normal and separable. *Proved here* (via Dedekind independence and the primitive element theorem).
Lang VI.1 (Theorem 1.8); Dummit-Foote 14.2. Background.

**galois:galois-extension** (definition + theorem). An algebraic extension $L/F$ is Galois if it is normal and
separable; then $\Gal(L/F):=\Aut(L/F)$. For $L/F$ finite the following are equivalent: (i) $L/F$ is Galois;
(ii) $L$ is the splitting field of a separable polynomial over $F$; (iii) $L^{\Aut(L/F)}=F$;
(iv) $\#\Aut(L/F)=[L:F]$. If $L/F$ is Galois and $F\subset M\subset L$, then $L/M$ is Galois.
*Proved here.* Lang VI.1; Dummit-Foote 14.2. Background.

**galois:fundamental-theorem** (theorem, fundamental theorem of Galois theory, finite case). Let $L/F$ be a finite
Galois extension with group $G=\Gal(L/F)$. The maps $H\mapsto L^H$ and $M\mapsto\Gal(L/M)$ are mutually
inverse, inclusion-reversing bijections between the subgroups $H\le G$ and the intermediate fields
$F\subset M\subset L$. Under them: $[L:M]=\#\Gal(L/M)$ and $[M:F]=[G:\Gal(L/M)]$; for $\sigma\in G$,
$\Gal(L/\sigma M)=\sigma\Gal(L/M)\sigma^{-1}$; $M/F$ is Galois iff $\Gal(L/M)$ is normal in $G$, and then
restriction $\sigma\mapsto\sigma|_M$ induces an isomorphism $G/\Gal(L/M)\simeq\Gal(M/F)$; intersections of
fields correspond to the subgroup generated, composita to intersections of subgroups.
*Proved here.* Lang VI.1 (Theorem 1.1); Dummit-Foote 14.2 (Theorem 14). Background: every "cuts out",
"fixed field", "index two" statement in the paper.

**galois:translation-theorem** (proposition, "shifting"). Let $L/F$ be Galois (finite or infinite) and $M/F$ an
arbitrary extension, $L$ and $M$ inside a common field. Then $LM/M$ is Galois and restriction
$\Gal(LM/M)\to\Gal(L/L\cap M)$, $\sigma\mapsto\sigma|_L$, is an isomorphism (of topological groups in the
infinite case, Section 7). Corollaries: (a) if $L_1,L_2$ are Galois over $F$ then so is $L_1L_2$, and
$\Gal(L_1L_2/F)\to\Gal(L_1/F)\times\Gal(L_2/F)$ is injective, bijective iff $L_1\cap L_2=F$; (b) for
$K/F$ finite, $[LK:K]=[L:L\cap K]$. *Proved here* (finite case; infinite case follows from Section 7).
Lang VI.1; Dummit-Foote 14.4. Background: restriction of
representations of $G_F$ to $G_K$; "unramified base change does not change inertia" in Chapter 7.

### Section 4. Finite fields, quadratic and cyclotomic extensions; worked examples

**galois:finite-field-galois** (theorem). Let $q=p^r$ and $n\ge1$; work inside a fixed $\Fbar_p$. (a) $\F_{q^n}$ is
the splitting field of $x^{q^n}-x$ over $\F_q$; every extension of $\F_q$ of degree $n$ is $\F_q$-isomorphic to it, and
inside $\Fbar_p$ it is unique. (b) $\F_{q^n}/\F_q$ is Galois, and $\Gal(\F_{q^n}/\F_q)$ is cyclic of order $n$, generated
by the $q$-power Frobenius $\phi_q(x)=x^q$. (c) The intermediate fields are the $\F_{q^d}$, $d\mid n$, with
$\F_{q^d}$ the fixed field of $\langle\phi_q^d\rangle$. (d) An irreducible $g\in\F_q[x]$ of degree $d$ with a root $\alpha$
has the $d$ distinct roots $\alpha,\alpha^q,\dots,\alpha^{q^{d-1}}$ and splits in $\F_{q^d}$; so every finite extension of
a finite field is Galois with cyclic group. *Proved here* (existence and uniqueness of $\F_q$ and cyclicity of
$\F_q^\times$ recalled from Chapter 2). Lang V.5; Dummit-Foote 14.3. Background: the Frobenius of Section 9 and
Chapter 6, unramified extensions in Chapter 7.

**galois:cyclotomic-mod-p** (proposition). Let $n\ge1$, $p$ a prime with $p\nmid n$, and $f$ the order of $p$ in
$(\Z/n)^\times$. Then $\Phi_n\bmod p$ is separable and is the product of $\varphi(n)/f$ distinct monic irreducible
polynomials of degree $f$ in $\F_p[x]$; $\F_p(\mu_n)=\F_{p^f}$. (Proof: $\mu_n(\Fbar_p)$ is cyclic of order $n$, the
Frobenius acts on it by $\zeta\mapsto\zeta^p$, and the orbits on the primitive $n$-th roots have size $f$.)
*Proved here.* Lang VI.3. Background: foreshadows "$p$ splits in $\Q(\zeta_n)$ into $\varphi(n)/f$ primes of residue
degree $f$" (Chapter 6) and $\Frob_p\mapsto p\bmod n$ (item galois:frobenius-preview).

**galois:quadratic-extensions** (proposition). Let $\operatorname{char}F\ne2$. (a) Every extension $L/F$ of degree $2$
is Galois and equals $F(\sqrt d)$ for some $d\in F^\times\setminus F^{\times2}$; $\Gal(L/F)=\{1,\sigma\}$ with
$\sigma(\sqrt d)=-\sqrt d$. (b) Inside $\Fbar$, $F(\sqrt d)=F(\sqrt{d'})$ iff $d/d'\in F^{\times2}$; so the quadratic
extensions of $F$ correspond bijectively to the nontrivial elements of $F^\times/F^{\times2}$. (c) For $F=\Q$ the
quadratic fields are the $\Q(\sqrt d)$, $d\ne0,1$ a squarefree integer, pairwise distinct. (d) If $a,b\in F^\times$ are
independent in $F^\times/F^{\times2}$, then $F(\sqrt a,\sqrt b)/F$ is Galois with group $\simeq V_4$ and exactly three
quadratic subfields $F(\sqrt a)$, $F(\sqrt b)$, $F(\sqrt{ab})$. *Proved here.* Dummit-Foote 13.2 and 14.2 (examples).
Background; convention C3; Lemma lem:twist and Theorem thm:twist (the fields $\Q(\sqrt{q^*})$ and
$\Q(\sqrt{\prod_{q\in S}q^*})$ of the characters $\chi_{q^*}$, $\chi_S$).

**galois:cyclotomic** (theorem). Let $n\ge1$, $\zeta_n=e^{2\pi i/n}\in\Qbar$, $\mu_n=\langle\zeta_n\rangle$.
(a) $\Phi_n=\prod_{(a,n)=1,\,1\le a\le n}(x-\zeta_n^a)$ lies in $\Z[x]$, and $x^n-1=\prod_{d\mid n}\Phi_d$ (Chapter 2).
(b) $\Phi_n$ is irreducible over $\Q$. (Proof: if $\zeta$ is a root of a monic irreducible factor $g\in\Z[x]$ of
$\Phi_n$ and $p\nmid n$ is prime, then $\zeta^p$ is a root of $g$; otherwise $g(x)$ and $h(x^p)$, with $h$ the minimal
polynomial of $\zeta^p$, share a factor mod $p$, so $x^n-1$ would have a repeated root mod $p$.)
(c) $\Q(\zeta_n)/\Q$ is Galois of degree $\varphi(n)$, and $a\mapsto\sigma_a$, $\sigma_a(\zeta)=\zeta^a$ for all
$\zeta\in\mu_n$, is an isomorphism $(\Z/n)^\times\to\Gal(\Q(\zeta_n)/\Q)$, independent of the choice of a primitive
$n$-th root of unity. (d) For $m\mid n$, restriction $\Gal(\Q(\zeta_n)/\Q)\to\Gal(\Q(\zeta_m)/\Q)$ is reduction
$(\Z/n)^\times\to(\Z/m)^\times$; $\Q(\zeta_m)\cap\Q(\zeta_n)=\Q(\zeta_{\gcd(m,n)})$ and
$\Q(\zeta_m)\Q(\zeta_n)=\Q(\zeta_{\operatorname{lcm}(m,n)})$; $\Q(\zeta_n)=\Q(\zeta_{2n})$ for $n$ odd; every subfield of
$\Q(\zeta_n)$ is Galois over $\Q$ with abelian group. (e) $\Q(\zeta_3)=\Q(\sqrt{-3})$ ($2\zeta_3+1=\sqrt{-3}$),
$\Q(\zeta_4)=\Q(i)$, $\Q(\zeta_8)=\Q(i,\sqrt2)$ with quadratic subfields $\Q(i)$, $\Q(\sqrt2)$, $\Q(\sqrt{-2})$.
*Proved here.* Lang VI.3; Dummit-Foote 13.6 and 14.5; Washington, Chapter 2. Paper use: $\Q(\zeta_3)=\Q(\sqrt{-3})$
(Proposition prop:ns, Theorem thm:qual, Lemma lem:h0, the optimal-level theorem quoted in Section 3); Chapter 6.

**galois:sqrt-lstar** (proposition). Let $\ell$ be an odd prime and $\ell^*=(-1)^{(\ell-1)/2}\ell$.
(a) $\disc(\Phi_\ell)=(-1)^{(\ell-1)/2}\ell^{\ell-2}=\ell^*\cdot\ell^{\ell-3}$, a square times $\ell^*$, so
$\sqrt{\ell^*}\in\Q(\zeta_\ell)$ (item galois:discriminant). (b) Equivalently, the Gauss sum
$g=\sum_{a=1}^{\ell-1}\bigl(\tfrac a\ell\bigr)\zeta_\ell^a$ satisfies $g^2=\ell^*$ (Chapter 2) and
$\sigma_a(g)=\bigl(\tfrac a\ell\bigr)g$. (c) $\Q(\sqrt{\ell^*})$ is the unique quadratic subfield of $\Q(\zeta_\ell)$ (the
cyclic group $(\Z/\ell)^\times$ of even order has a unique subgroup of index $2$, the squares), and $\sigma_a$ acts on
$\sqrt{\ell^*}$ by the Legendre symbol $\bigl(\tfrac a\ell\bigr)$. In terms of characters of $G_\Q$ (Section 7):
$\chi_{\ell^*}(\sigma)=\bigl(\tfrac{\bar\chi_\ell(\sigma)}{\ell}\bigr)$, that is $\chi_{\ell^*}=\bar\chi_\ell^{(\ell-1)/2}$.
(d) For $\ell=3$: $\Q(\sqrt{-3})=\Q(\zeta_3)$ and $\chi_{-3}=\bar\chi_3$; for $\ell\ge5$, $\chi_{\ell^*}\ne\bar\chi_\ell$
($\bar\chi_\ell$ has order $\ell-1>2$). (e) Every quadratic field $\Q(\sqrt d)$, $d$ squarefree, lies in
$\Q(\zeta_{|D|})$, $D$ its discriminant ($D=d$ if $d\equiv1\bmod4$, $D=4d$ otherwise), using (c), $i\in\Q(\zeta_4)$ and
$\sqrt2=\zeta_8+\zeta_8^{-1}$. *Proved here* ((a) via $\disc(\Phi_\ell)=\pm\Nm(\Phi_\ell'(\zeta_\ell))$, sketched; checked by
computer for $\ell\le13$). Washington, Chapter 2; Lang VI.3; Ireland-Rosen, Chapter 6 (Gauss sums). Paper use:
the hypothesis of Theorem thm:main and the set $S_f$ of Section 4.2 ($\Q(\sqrt{\ell^*})$), Lemma lem:h0
($\bar\chi_3=\chi_{-3}$), Proposition prop:ns, convention C4.

**galois:x3minus2** (worked example). $L=\Q(2^{1/3},\zeta_3)$ is the splitting field of $x^3-2$ over $\Q$, of degree
$6$ (it contains $\Q(2^{1/3})$ of degree $3$ and $\Q(\zeta_3)$ of degree $2$). With composition $(\sigma\tau)(x)=
\sigma(\tau(x))$, let $\sigma$ fix $\zeta_3$ and send $2^{1/3}\mapsto\zeta_32^{1/3}$, and let $\tau$ be complex
conjugation ($2^{1/3}$ fixed, $\zeta_3\mapsto\zeta_3^2$). Then $\sigma^3=\tau^2=1$, $\tau\sigma\tau=\sigma^{-1}$, and
$\Gal(L/\Q)\simeq S_3$, acting faithfully on the three roots. Correspondence: $\{1\}\leftrightarrow L$;
$\langle\tau\rangle\leftrightarrow\Q(2^{1/3})$; $\langle\sigma\tau\rangle\leftrightarrow\Q(\zeta_3^22^{1/3})$;
$\langle\sigma^2\tau\rangle\leftrightarrow\Q(\zeta_32^{1/3})$ (each order-two subgroup is the stabiliser of the root it
fixes); $\langle\sigma\rangle=A_3\leftrightarrow\Q(\zeta_3)=\Q(\sqrt{-3})=\Q(\sqrt{\disc})$, $\disc(x^3-2)=-108=-3\cdot6^2$;
$S_3\leftrightarrow\Q$. The three cubic fields are conjugate and not normal; $\Q(\sqrt{-3})$ is the only normal proper
subfield. *Proved here* (the correspondence was checked by hand). Dummit-Foote 14.2 (example). Paper use:
background; the model of "the quadratic subfield cut out by the sign/determinant" (Proposition prop:ns,
item galois:quartic-on-lines), and of the affine group $\mu_3\rtimes(\Z/3)^\times$ (item galois:kummer-affine).

### Section 5. Cyclic extensions: Hilbert 90, Kummer theory, Artin-Schreier

**galois:norm-trace** (definition and proposition). For $L/F$ finite separable of degree $n$ with $F$-embeddings
$\sigma_1,\dots,\sigma_n\colon L\to\Fbar$, put $\Nm_{L/F}(a)=\prod\sigma_i(a)$ and $\Tr_{L/F}(a)=\sum\sigma_i(a)$. They lie in
$F$, equal the determinant and the trace of the $F$-linear map $x\mapsto ax$ of $L$, $\Nm$ is multiplicative and $\Tr$
additive, both are transitive in towers, and for $L/F$ Galois $\Nm_{L/F}(a)=\prod_{\sigma\in\Gal(L/F)}\sigma(a)$.
*Proved here* (the determinant description sketched). Lang VI.5. Background: Hilbert 90; norms of ideals in Chapter 6.

**galois:hilbert90** (theorem, Hilbert's Theorem 90). Let $L/F$ be a finite cyclic extension of degree $n$ with
$\Gal(L/F)=\langle\sigma\rangle$. (a) For $b\in L^\times$: $\Nm_{L/F}(b)=1$ iff $b=c/\sigma(c)$ for some $c\in L^\times$.
(b) For $b\in L$: $\Tr_{L/F}(b)=0$ iff $b=c-\sigma(c)$ for some $c\in L$. (c) (General form.) For any finite Galois
$L/F$ with group $G$, every family $(a_\sigma)_{\sigma\in G}$ in $L^\times$ with $a_{\sigma\tau}=a_\sigma\,\sigma(a_\tau)$ is of the
form $a_\sigma=\sigma(c)/c$ for some $c\in L^\times$ (in the language of Chapter 16: $H^1(G,L^\times)=1$). *Proved here*
((a), (b), (c) by Dedekind independence: take $c=\sum_\tau a_\tau\tau(\theta)$ with $\theta$ chosen so that $c\ne0$; the
profinite form $H^1(G_F,(F^{\mathrm{sep}})^\times)=1$ is stated and left to Chapter 17). Lang VI.6. Paper use: through
Kummer theory (Lemmas lem:tamagawa-exp and lem:tamfactor); Chapter 17.

**galois:kummer-character** (definition and proposition). Let $n\ge1$ with $\operatorname{char}F\nmid n$ and
$\mu_n\subset F$. For $a\in F^\times$ choose $\alpha\in F^{\mathrm{sep}}$ with $\alpha^n=a$, and let $L/F$ be any Galois
extension containing $\alpha$. (a) The map $\chi_a\colon\Gal(L/F)\to\mu_n$, $\sigma\mapsto\sigma(\alpha)/\alpha$, is a
homomorphism independent of the choice of $\alpha$ (the other roots are $\zeta\alpha$, $\zeta\in\mu_n\subset F$); its
kernel is $\Gal(L/F(\alpha))$, so $F(\alpha)/F$ is Galois and cyclic of degree $d=\#\chi_a(\Gal(L/F))$, and $d$ is the
order of the class of $a$ in $F^\times/F^{\times n}$; in particular $d\mid n$. (b) $\chi_{ab}=\chi_a\chi_b$, and
$\chi_a=1$ iff $a\in F^{\times n}$; so $a\mapsto\chi_a$ is an injective homomorphism
$F^\times/F^{\times n}\to\Hom(G_F,\mu_n)$ (continuous homomorphisms, Section 7). (c) The minimal polynomial of
$\alpha$ is $x^d-\alpha^d$, and $x^n-a$ is irreducible over $F$ iff $a\notin F^{\times p}$ for every prime $p\mid n$.
(Without $\mu_n\subset F$ the correct criterion is Capelli's: $x^n-a$ is irreducible iff $a\notin F^{\times p}$ for all
primes $p\mid n$ and $a\notin-4F^{\times4}$ when $4\mid n$; stated, Lang VI.9.) *Proved here* (Capelli stated).
Lang VI.6 and VI.8. Paper use: Lemma lem:tamagawa-exp (with $F=\Q_q^{\mathrm{ur}}$, which contains $\mu_{\ell^t}$
because $q\ne\ell$, Chapter 7: $F(u^{1/\ell^t})=F$ iff $u\in F^{\times\ell^t}$), Lemma lem:tamfactor.

**galois:kummer-cyclic** (theorem). Let $\operatorname{char}F\nmid n$ and $\mu_n\subset F$. Every cyclic extension $L/F$
of degree $n$ is $L=F(\alpha)$ with $\alpha^n\in F^\times$. (Proof: with $\Gal(L/F)=\langle\sigma\rangle$,
$\Nm_{L/F}(\zeta_n^{-1})=\zeta_n^{-n}=1$, so Hilbert 90 gives $c\in L^\times$ with $\sigma(c)=\zeta_nc$; then
$c^n\in F$ and $c$ has $n$ distinct conjugates.) *Proved here.* Lang VI.6. Background (completes the classification).

**galois:kummer-classification** (theorem, Kummer theory). Let $\operatorname{char}F\nmid n$ and $\mu_n\subset F$.
(a) $\Delta\mapsto F_\Delta=F(\{\alpha\in F^{\mathrm{sep}}:\alpha^n\in\Delta\})$ is an inclusion-preserving bijection from
the subgroups $F^{\times n}\subset\Delta\subset F^\times$ to the abelian extensions of $F$ inside $F^{\mathrm{sep}}$ of exponent
dividing $n$; the inverse is $L\mapsto L^{\times n}\cap F^\times$. (b) The pairing
$\Gal(F_\Delta/F)\times\Delta/F^{\times n}\to\mu_n$, $(\sigma,a)\mapsto\sigma(\alpha)/\alpha$ ($\alpha^n=a$), is bilinear and
perfect: $\Gal(F_\Delta/F)\simeq\Hom(\Delta/F^{\times n},\mu_n)$ and $[F_\Delta:F]=[\Delta:F^{\times n}]$ when this is finite
(for infinite $\Delta$ the isomorphism is one of profinite groups, $\Delta/F^{\times n}$ discrete). (c) (The mod $n$
form.) $a\mapsto\chi_a$ is an isomorphism $F^\times/F^{\times n}\simeq\Hom_{\mathrm{cont}}(G_F,\mu_n)$; the cyclic
extensions of degree $d\mid n$ correspond to the cyclic subgroups of order $d$ of $F^\times/F^{\times n}$; after fixing a
primitive $\zeta_n$, so that $\mu_n\simeq\Z/n$, the surjections $G_F\to\Z/n$ (a $\Z/n$-extension with a chosen
identification of its group with $\Z/n$) correspond to the elements of exact order $n$ of $F^\times/F^{\times n}$.
(d) For $n=2$, $\operatorname{char}F\ne2$: $\Hom_{\mathrm{cont}}(G_F,\{\pm1\})\simeq F^\times/F^{\times2}$, recovering
galois:quadratic-extensions. *Proved here* for finite $\Delta/F^{\times n}$; the infinite case after Section 7
(sketched). Lang VI.8; Neukirch IV.3. Paper use: Lemma lem:tamfactor (Kummer classes of the Tate parameter and of
its unit part), Lemma lem:tamagawa-exp; Chapter 7 ($\Q_p^\times/(\Q_p^\times)^{\ell^k}$), Chapter 17
($H^1(K,\mu_n)=K^\times/K^{\times n}$, which removes the hypothesis $\mu_n\subset F$).

**galois:kummer-affine** (proposition). Let $\operatorname{char}F\nmid n$, without assuming $\mu_n\subset F$; let $a\in
F^\times$, $\alpha^n=a$, $L=F(\mu_n,\alpha)$, and fix a primitive $\zeta_n$. For $\sigma\in\Gal(L/F)$ write
$\sigma(\zeta_n)=\zeta_n^{c(\sigma)}$ and $\sigma(\alpha)=\zeta_n^{k(\sigma)}\alpha$. Then $\sigma\mapsto
\begin{pmatrix}c(\sigma)&k(\sigma)\\0&1\end{pmatrix}$ is an injective homomorphism $\Gal(L/F)\to
\bigl\{\begin{pmatrix}c&k\\0&1\end{pmatrix}:c\in(\Z/n)^\times,k\in\Z/n\bigr\}\simeq\Z/n\rtimes(\Z/n)^\times$; its
restriction to $\Gal(L/F(\mu_n))$ is the Kummer character. Example: $x^3-2$ over $\Q$ gives
$\Gal\simeq\Z/3\rtimes(\Z/3)^\times\simeq S_3$. *Proved here.* Lang VI.9 (examples). Paper use: the shape
$\begin{psmallmatrix}\chi_\ell\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$ in the proof of Lemma lem:tamfactor (here with
$\varepsilon=1$ and finite level; the $\ell$-adic form is galois:l-adic-kummer).

**galois:kummer-finite-field** (proposition). Let $q$ be a prime power, $\ell\nmid q$ a prime, $v=v_\ell(q-1)$, and
$u\in\F_q^\times$. (a) For $1\le k\le v$ (so $\mu_{\ell^k}\subset\F_q$), the Kummer character
$\chi_u\colon G_{\F_q}\to\mu_{\ell^k}$ satisfies $\chi_u(\phi_q)=u^{(q-1)/\ell^k}$ (because $\phi_q(\alpha)/\alpha=\alpha^{q-1}$);
hence $u\in(\F_q^\times)^{\ell^k}$ iff $u^{(q-1)/\ell^k}=1$, and $u\mapsto u^{(q-1)/\ell^v}$ is an isomorphism
$\F_q^\times/(\F_q^\times)^{\ell^v}\simeq\mu_{\ell^v}(\F_q)$ of cyclic groups of order $\ell^v$ (this group is
$\F_q^\times\otimes\Zl$). (b) ($\ell$-adic form.) For any compatible system $(\alpha_k)_{k\ge0}$ in $\Fbar_q$ with
$\alpha_0=u$, $\alpha_{k+1}^\ell=\alpha_k$, the element $\kappa_u(\phi_q)=(\phi_q(\alpha_k)/\alpha_k)_k=(\alpha_k^{q-1})_k$ of
$\Zl(1)=\varprojlim\mu_{\ell^k}(\Fbar_q)$ changes by an element of $(q-1)\Zl(1)$ when the system is changed, and its class
in $\Zl(1)/(q-1)\Zl(1)\simeq\mu_{\ell^v}(\F_q)$ is $u^{(q-1)/\ell^v}$. For $k\le v$, the class has $\ell$-adic valuation
$\ge k$ (as an element of $\Z/\ell^v$ after choosing a generator) iff $u\in(\F_q^\times)^{\ell^k}$. *Proved here.*
Elementary; compare Serre, Local Fields, Chapter IV. Paper use: Lemma lem:tamfactor ("$c$ the class of $u$ in
$\F_q^\times/(\F_q^\times)^{\ell^{v_\ell(q-1)}}$", "the class of the unit part of $q_E$ in $\F_q^\times\otimes\Zl$ by Kummer
theory"); Chapter 7 and Chapter 17 complete the passage from $\F_q$ to $\Q_q$ (Hensel, inflation from $G/I$).

**galois:artin-schreier** (theorem). Let $\operatorname{char}F=p>0$ and $\wp(b)=b^p-b$. (a) For $a\in F$ the polynomial
$x^p-x-a$ is separable; if $\alpha$ is a root, its roots are $\alpha+i$, $i\in\F_p$; it splits over $F$ if $a\in\wp(F)$ and
is irreducible otherwise, and then $F(\alpha)/F$ is cyclic of degree $p$ with group generated by $\alpha\mapsto\alpha+1$.
(b) Every cyclic extension of $F$ of degree $p$ is of this form. (c) $\Hom_{\mathrm{cont}}(G_F,\Z/p)\simeq F/\wp(F)$, the
additive analogue of Kummer theory. Example: $x^p-x-1$ is irreducible over $\F_p$, with splitting field $\F_{p^p}$.
*Stated; reference* ((a) proved in a few lines; (b) from the additive Hilbert 90, sketched). Lang VI.6.
Background (the $p$-extensions that Kummer theory cannot reach in characteristic $p$; context for wild ramification
in Chapter 7 and Remark rem:wild).

### Section 6. The Galois group of a polynomial; discriminants, cubics, quartics and the four lines

**galois:galois-group-polynomial** (definition and proposition). Let $f\in F[x]$ be separable of degree $n\ge1$, $R$ its
set of $n$ roots in $F^{\mathrm{sep}}$, $L=F(R)$ its splitting field and $G_f=\Gal(L/F)$, the Galois group of $f$.
(a) $G_f$ acts faithfully on $R$; numbering the roots gives an injective homomorphism $G_f\to S_n$ whose image is
well defined up to conjugation in $S_n$; $\#G_f=[L:F]$. (b) The $G_f$-orbits on $R$ correspond bijectively to the
monic irreducible factors of $f$ in $F[x]$: the orbit of $r$ is the set of roots of the minimal polynomial of $r$;
its size is $[F(r):F]$ and the stabiliser of $r$ is $\Gal(L/F(r))$. In particular $f$ is irreducible iff $G_f$ is
transitive on $R$, and then $n\mid\#G_f$. (c) For any Galois extension $\Omega/F$ containing $L$ (for instance
$\Omega=F^{\mathrm{sep}}$), $\Gal(\Omega/F)$ acts on $R$ through its quotient $G_f$, with the same orbits; and for an
intermediate field $F\subset M\subset\Omega$ the irreducible factors of $f$ in $M[x]$ correspond to the orbits of
$\Gal(\Omega/M)$ on $R$. *Proved here.* Dummit-Foote 14.6; Lang VI.2. Paper use: Proposition prop:ns ("the four
roots of the $3$-division polynomial correspond to the four lines", "factors as two quadratics", "irreducible
otherwise"), Section sec:data and the appendix (the test `ns3`); Chapter 9 (division polynomials).

**galois:discriminant** (definition and proposition). For $f=a\prod_{i=1}^n(x-r_i)$ separable, put
$\delta_f=\prod_{i<j}(r_i-r_j)$ (depends on the numbering up to sign) and $\disc(f)=a^{2n-2}\delta_f^2=
(-1)^{n(n-1)/2}a^{-1}\operatorname{Res}(f,f')$, an element of $F$ given by a universal integer polynomial in the
coefficients. (a) $\sigma(\delta_f)=\operatorname{sgn}(\sigma)\delta_f$ for $\sigma\in G_f\subset S_n$. (b) If
$\operatorname{char}F\ne2$: $G_f\subset A_n$ iff $\disc(f)\in F^{\times2}$; the fixed field of $G_f\cap A_n$ is
$F(\sqrt{\disc f})$, and the character of $G_F$ attached to it by galois:quadratic-extensions is
$\operatorname{sgn}\circ(\text{action on }R)$. (c) For monic $g,h$: $\disc(gh)=\disc(g)\disc(h)\operatorname{Res}(g,h)^2$.
(d) Formulas (all checked by computer algebra): $\disc(x^2+bx+c)=b^2-4c$;
$\disc(x^3+bx^2+cx+d)=b^2c^2-4c^3-4b^3d-27d^2+18bcd$, so $\disc(x^3+px+q)=-4p^3-27q^2$;
$\disc(x^n-a)=(-1)^{(n-1)(n-2)/2}n^na^{n-1}$; $\disc(\Phi_\ell)=(-1)^{(\ell-1)/2}\ell^{\ell-2}$ for $\ell$ an odd prime.
*Proved here* ((a) to (c), the quadratic and cubic formulas; $\disc(x^n-a)$ and $\disc(\Phi_\ell)$ via
$\disc(f)=\pm\prod_if'(r_i)$, sketched). Dummit-Foote 14.6. Paper use: Proposition prop:ns through
galois:quartic-on-lines (c): for $E/\Q$ the sign of the Galois action on the roots of $\psi_3$ is
$\det\bar\rho_{E,3}=\chi_{-3}$, so $\disc(\psi_3)\in-3\cdot(\Q^\times)^2$; checked: $\disc(\psi_3)=-3^3\cdot11^{10}$ for
11a1 and $-3^3\cdot11^4$ for 121a1.

**galois:cubic** (proposition). Let $\operatorname{char}F\ne2$ and $f\in F[x]$ a separable cubic. If $f$ is
irreducible, $G_f=A_3\simeq C_3$ when $\disc(f)$ is a square and $G_f=S_3$ otherwise. If $f$ is a linear factor
times an irreducible quadratic $g$, $G_f=C_2$ with splitting field $F(\sqrt{\disc g})$. Examples over $\Q$: $x^3-2$
($\disc=-108$, $G_f=S_3$, galois:x3minus2); $x^3-3x+1$ ($\disc=81$, $G_f=C_3$, roots
$2\cos(2\pi k/9)$ for $k=1,2,4$, splitting field the real cubic subfield $\Q(\zeta_9+\zeta_9^{-1})$ of $\Q(\zeta_9)$).
*Proved here.* Dummit-Foote 14.6. Background (the resolvent cubic below; the cubic factor of $\psi_3$ for a Borel
image, galois:quartic-on-lines).

**galois:quartic** (proposition). Let $\operatorname{char}F\ne2$ and $f=x^4+ax^3+bx^2+cx+d\in F[x]$ separable with
roots $r_1,\dots,r_4$. Put $\theta_1=r_1r_2+r_3r_4$, $\theta_2=r_1r_3+r_2r_4$, $\theta_3=r_1r_4+r_2r_3$ (one for each
partition of the roots into two pairs). The resolvent cubic $R_f(y)=\prod(y-\theta_i)$ equals
$y^3-by^2+(ac-4d)y-(a^2d-4bd+c^2)$, and $\disc(R_f)=\disc(f)$ (both identities checked symbolically), so the
$\theta_i$ are distinct. $S_4$ permutes the three partitions through a surjection $S_4\to S_3$ with kernel the normal
$V_4=\{1,(12)(34),(13)(24),(14)(23)\}$. (a) If $f$ is irreducible, $G_f$ is conjugate to one of $S_4$, $A_4$, $D_4$,
$C_4$, $V_4$, and: $R_f$ irreducible and $\disc f\notin F^{\times2}$ gives $S_4$; $R_f$ irreducible and
$\disc f\in F^{\times2}$ gives $A_4$; $R_f$ split into linear factors gives $V_4$; $R_f$ with exactly one root in $F$
gives $D_4$ or $C_4$, and $C_4$ iff $f$ is reducible over $F(\sqrt{\disc f})$ (Kappe-Warren). (b) For any separable
quartic, the degrees of the irreducible factors are the orbit sizes of $G_f$ (galois:galois-group-polynomial), and
$\theta_i\in F$ iff $G_f$ stabilises the $i$-th partition. *Proved here* ((a) except the $D_4$ versus $C_4$ criterion,
which is sketched). Dummit-Foote 14.6. Paper use: background for Proposition prop:ns (the Galois group of
$\psi_3$ is the image of $\bar\rho_{E,3}$ in $\PGL_2(\F_3)\simeq S_4$); Chapter 22.

**galois:quartic-on-lines** (proposition; the Galois-theoretic form of the last sentence of Proposition prop:ns).
Let $F$ be a field, $V$ a two-dimensional $\F_3$-vector space, $\rho\colon G_F\to\GL(V)\simeq\GL_2(\F_3)$ a continuous
homomorphism with image $H$, and $f\in F[x]$ a separable quartic whose root set $R$ is in a $G_F$-equivariant
bijection with the set $\PP(V)$ of the four lines of $V$. Then: (a) $G_F$ acts on $R$ through $H\to\PGL_2(\F_3)\simeq S_4$
(the action on lines is faithful modulo the scalars $\{\pm1\}$, Chapter 1), so $G_f$ is isomorphic to the image of
$H$ in $\PGL_2(\F_3)$ and the splitting field of $f$ is the fixed field of $\rho^{-1}(\{\pm1\})$; (b) the irreducible
factors of $f$ over $F$ correspond to the orbits of $H$ on the four lines, with degrees the orbit sizes; (c) the sign of
the permutation of the four lines induced by $g\in\GL_2(\F_3)$ is $\det g\in\{\pm1\}=\F_3^\times$ (Chapter 1), so, if
$\operatorname{char}F\ne2$, $F(\sqrt{\disc f})$ is the fixed field of $\ker(\det\circ\rho)$; (d) for the subgroups $H$ with
$\det(H)=\F_3^\times$, up to conjugacy (orders and patterns checked by enumerating all $16$ conjugacy classes of
subgroups of $\GL_2(\F_3)$):

| $H$ (Sutherland label) | $\#H$ | orbits on the four lines | $G_f$ | factorisation of $f$ over $F$ |
|-|-|-|-|-|
| $\GL_2(\F_3)$ (surjective) | 48 | 4 | $S_4$ | irreducible |
| $N_{ns}(\F_3)$ (3Nn) | 16 | 4 | $D_4$ | irreducible |
| $C_{ns}(\F_3)$ (3Cn) | 8 | 4 | $C_4$ | irreducible |
| $N_s(\F_3)$ (3Ns) | 8 | 2+2 | $V_4$, not normal in $S_4$ | two irreducible quadratics |
| $\mathrm{B}(\F_3)$ (3B) | 12 | 1+3 | $S_3$ | linear times irreducible cubic |
| the two of order 6 (3B.1.1, 3B.1.2) | 6 | 1+3 | $S_3$ | linear times irreducible cubic |
| $C_s(\F_3)$ (3Cs) | 4 | 1+1+2 | $C_2$ | two linear times irreducible quadratic |
| $\langle\operatorname{diag}(1,-1)\rangle$ (3Cs.1.1) | 2 | 1+1+2 | $C_2$ | two linear times irreducible quadratic |

(e) In the $N_s(\F_3)$ case the two quadratic factors have distinct splitting fields $K_1\ne K_2$, and the third
quadratic subfield of $K_1K_2$ is $F(\sqrt{\disc f})$, the fixed field of $\det\circ\rho$; in the $N_s$ and $N_{ns}$ cases
the resolvent cubic has exactly one root in $F$ (the image in $S_4$ stabilises one partition of the lines into pairs),
in the $\GL_2$ case none. (f) Consequently, if $H$ fixes no line of $V$ and contains an element of determinant $-1$
and trace $0$, then $H$ is conjugate to $\GL_2(\F_3)$, $N_{ns}(\F_3)$ or $N_s(\F_3)$ (Chapter 1), and $f$ is irreducible
in the first two cases and a product of two irreducible quadratics in the third. *Proved here.* Chapter 1 for the
group theory (the orbit table, $\det=$ sign, the three images). Paper use: Proposition prop:ns (last two sentences
of the statement and of the proof), Section sec:data ("the mod 3 images of the tables were checked against the
factorisation of the $3$-division polynomial"), Section sec:anomaly, the appendix (`ns3`). The input "the roots of
$\psi_3$ are the $x$-coordinates of the four lines of $E[3]$, Galois-equivariantly" is Chapter 9; "$\det\bar\rho_{E,3}=
\chi_{-3}$ and complex conjugation has determinant $-1$, trace $0$" is Chapters 9 and 11 (and galois:complex-conjugation).

**galois:ns-example** (worked example). The curve $E\colon y^2=x^3-6x-8$ ($j=-1728$, not a CM $j$-invariant;
$\Delta=-2^9\cdot3^3$) has $\psi_3=3x^4-36x^2-96x-36=3(x^2-4x-2)(x^2+4x+6)$, a product of two irreducible quadratics
with discriminants $24$ and $-8$, so $K_1=\Q(\sqrt6)$, $K_2=\Q(\sqrt{-2})$ and the third quadratic subfield is
$\Q(\sqrt{-3})$, as galois:quartic-on-lines (e) predicts; the image of $\bar\rho_{E,3}$ is therefore $N_s(\F_3)$ (by (d):
two orbits of size two and surjective determinant), and indeed $a_p\equiv0\pmod3$ for every prime $p\equiv2\pmod3$,
$5\le p\le71$ ($a_5=3$, $a_{11}=3$, $a_{17}=-6$, $a_{23}=6$, $a_{29}=6$, $a_{41}=6$, $a_{47}=12$, $a_{53}=-3$,
$a_{59}=12$, $a_{71}=-6$), as $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ requires (galois:index-two-restriction); note
$9\nmid a_5$. By contrast 11a1 has $\psi_3=3x^4-4x^3-60x^2-237x-21$, irreducible with irreducible resolvent cubic
and $\disc=-3^3\cdot11^{10}$: $G_{\psi_3}=S_4$, image $\GL_2(\F_3)$. *Proved here* (all values computed by
the outline author; the writer should recompute with PARI, `elldivpol(E,3)`, `factor`, `ellap`). Paper use:
Proposition prop:ns, Section sec:anomaly; the paper's own example 726a1 (image 3Ns, type III at 11) may be added after
checking it in PARI.

### Section 7. Infinite Galois extensions, the Krull topology, $G_\Q$, the cyclotomic character, complex conjugation

**galois:infinite-galois-limit** (proposition and definition). Let $L/F$ be Galois of arbitrary degree. (a) $L$ is the
union of its finite Galois subextensions $K/F$, these form a directed set under inclusion, and restriction gives a
group isomorphism $\Gal(L/F)\to\varprojlim_K\Gal(K/F)$. (b) The Krull topology on $\Gal(L/F)$ is the one in which the
subgroups $\Gal(L/K)$, $K\subset L$ finite over $F$ (equivalently finite Galois over $F$), form a basis of open
neighbourhoods of $1$; it coincides with the inverse-limit topology of Chapter 1 (directed index set), so
$\Gal(L/F)$ is a profinite group: compact, Hausdorff and totally disconnected. (c) For $L/F$ finite the topology
is discrete. *Proved here* (Tychonoff and the topological facts about profinite groups from Chapter 1).
Neukirch IV.1; NSW I.1. Background: every Galois group in the paper ($G_\Q$, $G_{\Q_p}$, $I_p$, Section 1.1).

**galois:infinite-fundamental-theorem** (theorem, Krull). Let $L/F$ be Galois with group $G$. (a) $H\mapsto L^H$ and
$M\mapsto\Gal(L/M)$ are mutually inverse inclusion-reversing bijections between the closed subgroups of $G$ and the
intermediate fields $F\subset M\subset L$. (b) For an arbitrary subgroup $H\le G$, $\Gal(L/L^H)=\overline H$ (closure).
(c) Open subgroups correspond to the intermediate fields finite over $F$, with $[G:\Gal(L/M)]=[M:F]$. (d) $M/F$ is
Galois iff $\Gal(L/M)$ is normal in $G$, and then restriction induces an isomorphism of topological groups
$G/\Gal(L/M)\simeq\Gal(M/F)$ (quotient topology on the left). (e) $\Gal(L/\sigma M)=\sigma\Gal(L/M)\sigma^{-1}$.
(f) Warnings: in $\Gal(\Fbar_p/\F_p)\simeq\hat\Z$ the subgroup $\phi_p^{\Z}$ is dense and not closed (its fixed field is
$\F_p$); and a subgroup of finite index need not be open: $\Gal(\Q(\sqrt{-1},\sqrt2,\sqrt3,\sqrt5,\dots)/\Q)\simeq
\prod_{\N}\Z/2$ (Kummer theory with $\Delta=\Q^\times$, $n=2$) has non-open subgroups of index $2$ (kernels of
non-continuous functionals; uses the axiom of choice). *Proved here* ((a) to (e) and the first warning; the second
warning stated). Neukirch IV.1; Lang VI.14; Milne, Fields and Galois Theory, Chapter 7. Paper use: background
("open subgroups", "the field cut out by", "Gal(Qbar/Q(sqrt(l*)))").

**galois:absolute-galois-group** (definition and proposition). $G_F=\Gal(F^{\mathrm{sep}}/F)$ with the Krull topology
(convention C1). (a) For $K/F$ finite separable inside $F^{\mathrm{sep}}$, $G_K$ is an open subgroup of $G_F$ of index
$[K:F]$, every open subgroup is of this form, $\sigma G_K\sigma^{-1}=G_{\sigma K}$, and $G_K$ is normal iff $K/F$ is
Galois, in which case $G_F/G_K\simeq\Gal(K/F)$. (b) $G_{\F_q}\simeq\hat\Z$, with $1\mapsto\phi_q$; its open subgroups are
the $n\hat\Z=G_{\F_{q^n}}$. (c) $G_\Q=\Gal(\Qbar/\Q)$; for a number field $K\subset\Qbar$, $G_K$ is open of index $[K:\Q]$; so
$G_{\Q(\sqrt d)}$ has index $2$ ($d$ not a square) and $G_{\Q(\zeta_n)}$ is open and normal of index $\varphi(n)$.
(d) $G_\Q$ is uncountable and non-abelian; its maximal abelian quotient is $\Gal(\Q^{\mathrm{ab}}/\Q)\simeq\hat\Z^\times$
with $\Q^{\mathrm{ab}}=\Q(\mu_\infty)$ (Kronecker-Weber, Chapter 6). *Proved here* except (d), stated. Neukirch IV.1
and VI.1. Paper use: Section 1.1 ($\rho\colon G_\Q\to\GL_2(\Zl)$), the hypothesis of Theorem thm:main, Section 4.2.

**galois:cyclotomic-character** (definition and proposition). Let $\ell$ be a prime and $\Q(\mu_{\ell^\infty})=
\bigcup_k\Q(\mu_{\ell^k})$. (a) There is a unique continuous homomorphism $\chi_\ell\colon G_\Q\to\Zl^\times$ with
$\sigma(\zeta)=\zeta^{\chi_\ell(\sigma)}$ for all $\zeta\in\mu_{\ell^\infty}$ (so $\chi_\ell(\sigma)\bmod\ell^k$ is the $a$ with
$\sigma|_{\Q(\zeta_{\ell^k})}=\sigma_a$). (b) $\chi_\ell$ is surjective with kernel $G_{\Q(\mu_{\ell^\infty})}$, so
$\Gal(\Q(\mu_{\ell^\infty})/\Q)\simeq\Zl^\times$ as topological groups. (c) $\bar\chi_\ell=\chi_\ell\bmod\ell\colon G_\Q\to\F_\ell^\times$
is surjective with kernel $G_{\Q(\zeta_\ell)}$, and $\chi_{\ell^*}=\bigl(\tfrac{\bar\chi_\ell}{\ell}\bigr)$
(galois:sqrt-lstar). (d) For any field $F$ with $\operatorname{char}F\ne\ell$, the same definition gives
$\chi_\ell\colon G_F\to\Zl^\times$ (no longer surjective in general; trivial modulo $\ell^k$ iff $\mu_{\ell^k}\subset F$;
$\chi_\ell(\phi_q)=q$ for $F=\F_q$), and $\Zl(1)=\varprojlim_k\mu_{\ell^k}$ (transition $\zeta\mapsto\zeta^\ell$) is a free
$\Zl$-module of rank one on which $G_F$ acts through $\chi_\ell$; $\Zl(1)/\ell^k=\mu_{\ell^k}$; $M(1)=M\otimes\Zl(1)$.
*Proved here.* Washington, Chapter 2; Neukirch IV.1; Serre, Abelian l-adic representations, Chapter I. Paper use:
Section 4 ($\chi_\ell$, $T(1)$, $\Hom(A,\Zl(1))$), Lemma lem:h0 ($\bar\chi_\ell$, $\bar\chi_3=\chi_{-3}$), Lemma
lem:tamfactor ($\Zl(1)$, $\Zl(1)^I$, $\Frob$ acts on $\Zl(1)$ by $q$), Lemma lem:old ($\bar\chi_\ell$ in the local
analysis); Chapter 9 ($\det\rho_{E,\ell}=\chi_\ell$ via the Weil pairing).

**galois:complex-conjugation** (proposition). Fix the inclusion $\Qbar\subset\C$ (C1) and let $c\in G_\Q$ be the restriction
of complex conjugation. (a) $c$ has order $2$ ($i\in\Qbar$); for $\sigma\in G_\Q$, the complex conjugation attached to the
embedding $\Qbar\xrightarrow{\sigma}\Qbar\subset\C$ is $\sigma^{-1}c\sigma$; "a complex conjugation" means an element of
this conjugacy class. (b) $\chi_\ell(c)=-1$ for every $\ell$; $\chi_d(c)=-1$ iff $d<0$; so $\chi_{\ell^*}(c)=
(-1)^{(\ell-1)/2}$ and $\chi_{-3}(c)=\chi_{-4}(c)=-1$. (c) (Artin-Schreier, stated.) Every element of $G_\Q$ of finite
order other than $1$ is a complex conjugation; in particular it has order $2$. (d) Let $k$ be a field with
$\operatorname{char}k\ne2$ and $\rho\colon G_\Q\to\GL_2(k)$ a homomorphism with $\det\rho(c)=-1$ (for instance
$\det\rho=\bar\chi_\ell$, $\ell$ odd, or $\det\rho=\chi_\ell$). Then $\rho(c)$ is conjugate to $\operatorname{diag}(1,-1)$,
has determinant $-1$ and trace $0$, and $\rho$ is irreducible over $k$ iff it is absolutely irreducible (a line of
$\bar k^2$ stable under $\rho(G_\Q)$ is an eigenline of $\rho(c)$, and both eigenlines are $k$-rational).
*(a), (b), (d) proved here; (c) stated; reference.* Lang XI (real fields); Serre, Course in Arithmetic, Chapter I (for
the signs). Paper use: Proposition prop:ns ("contain an element of determinant $-1$ and trace $0$ (complex
conjugation)"), Lemmas lem:h0 and lem:old (irreducible implies absolutely irreducible for $\bar\rho_{E,\ell}$, used
silently), Lemma lem:dfg21 ($G_\R=\{1,c\}$, so $H^1(\R,-)$ is killed by $2$; Chapter 17).

### Section 8. Continuous characters and representations of profinite groups

**galois:continuous-reps** (definition and proposition). Let $G$ be profinite and $\rho\colon G\to\GL_n(k)$ a homomorphism,
$k$ topologised as in C5. (a) If $k$ is discrete (a finite field, $\Fbar_\ell$, any field with the discrete topology),
$\rho$ is continuous iff $\ker\rho$ is open iff $\rho$ factors through a finite quotient $G/U$; then $\rho(G)$ is finite.
For $G=G_F$ the field cut out by $\rho$ is $F_\rho=(F^{\mathrm{sep}})^{\ker\rho}$, finite Galois over $F$ with
$\Gal(F_\rho/F)\simeq\rho(G_F)$. (b) If $k=E$ is a finite extension of $\Q_\ell$ with ring of integers $\mathcal{O}$ and
uniformiser $\lambda$, a homomorphism $\rho\colon G\to\GL_n(\mathcal{O})$ is continuous iff every $\rho\bmod\lambda^m$ is;
then $\rho(G)$ is compact, hence closed, $F_\rho=(F^{\mathrm{sep}})^{\ker\rho}$ is Galois (in general infinite) over $F$, and
$\Gal(F_\rho/F)\simeq\rho(G_F)$ as topological groups. (c) Every continuous $\rho\colon G\to\GL_n(E)$ stabilises an
$\mathcal{O}$-lattice $\Lambda\subset E^n$ (the stabiliser $U$ of $\mathcal{O}^n$ is open, of finite index; take
$\Lambda=\sum_{g\in G/U}\rho(g)\mathcal{O}^n$), so it is conjugate to a continuous $\rho\colon G\to\GL_n(\mathcal{O})$; its
reduction $\bar\rho_\Lambda$ on $\Lambda/\lambda\Lambda$ is continuous for the discrete topology. (d) Every continuous
$\rho\colon G\to\GL_n(\C)$ has finite image ($\GL_n(\C)$ has a neighbourhood of $1$ containing no nontrivial subgroup);
in particular continuous characters $G_\Q\to\C^\times$ have finite order. (e) Subrepresentations, quotients, the
semisimplification $\rho^{ss}$ (Jordan-Holder, Chapter 4), $\rho\otimes\rho'$, $\rho^\vee$, $\ad\rho$ of continuous
representations are continuous. *Proved here* ((d) sketched). Serre, Abelian l-adic representations, Chapter I,
Section 1; DDT, Section 1. Paper use: Section 1.1 ($\rho$, $\bar\rho$, $T$, $V$), Lemma lem:h0 ($\rho\bmod\ell^k$),
Lemma lem:old, Lemma lem:tamagawa-exp ($\rho\bmod\ell^t$), Section 4.2 (lattices).

**galois:quadratic-characters** (proposition). (a) $d\mapsto\chi_d$ (C3) is an isomorphism
$\Q^\times/\Q^{\times2}\simeq\Hom_{\mathrm{cont}}(G_\Q,\{\pm1\})$, with $\ker\chi_d=G_{\Q(\sqrt d)}$ (Kummer theory with
$n=2$); the nontrivial continuous quadratic characters of $G_\Q$ correspond to the quadratic fields. (b)
$\chi_{dd'}=\chi_d\chi_{d'}$; for example $\chi_{-15}=\chi_{-3}\chi_5$ (no numerical $\chi_3$: in the book a numerical subscript is always a quadratic $\chi_d$ with its sign, Appendix B, B-C6(b)), and for a set $S$ of odd primes
$\chi_S=\prod_{q\in S}\chi_{q^*}$ is the character of $\Q(\sqrt{\prod_{q\in S}q^*})$. (c) (Values at Frobenius; proved in
Chapter 6, used here as a black box, item galois:frobenius-preview.) For $p\nmid D$: $\chi_d(\Frob_p)=\bigl(\tfrac
Dp\bigr)$, which is $1$ iff $p$ splits in $\Q(\sqrt d)$; $\chi_{-3}(\Frob_p)=1$ iff $p\equiv1\pmod3$;
$\chi_{-4}(\Frob_p)=1$ iff $p\equiv1\pmod4$; $\chi_{\ell^*}(\Frob_p)=\bigl(\tfrac p\ell\bigr)$ for $p\ne\ell$, directly
from $\chi_{\ell^*}=\bigl(\tfrac{\bar\chi_\ell}{\ell}\bigr)$ and $\bar\chi_\ell(\Frob_p)=p\bmod\ell$. (Comparing with
$\chi_{\ell^*}(\Frob_p)=\bigl(\tfrac{\ell^*}{p}\bigr)$ is quadratic reciprocity: a remark, with the proof left to
Chapter 2.) (d) As Dirichlet characters (Chapters 2 and 6) $\chi_d$ has conductor $|D|$: $\chi_{q^*}$ has conductor $q$,
$\chi_{-3}$ conductor $3$, $\chi_{-4}$ conductor $4$. *(a), (b) proved here; (c), (d) stated with Chapter 6
reference; the congruence conditions in (c) were checked numerically for $p<2000$ and $\ell\le13$.* Paper use: the
table of Section 1 and Lemma lem:euler ($\chi_{-3}(q)$, $\chi_{-4}(q)$), Lemma lem:twist ($\chi_{q^*}$, $\Q(\sqrt{q^*})$),
Theorem thm:twist ($\chi_S$), Lemma lem:h0, Proposition prop:ns ($\chi_{-3}$).

**galois:twist** (proposition). Let $\rho\colon G\to\GL_n(k)$ and $\chi\colon G\to k^\times$ be continuous. (a) $\rho\otimes\chi$
is continuous, $\tr(\rho\otimes\chi)(g)=\chi(g)\tr\rho(g)$, $\det(\rho\otimes\chi)=\chi^n\det\rho$, and for $G=G_\Q$ the
field cut out by $\rho\otimes\chi$ lies in $F_\rho F_\chi$. (b) If $\rho\simeq\rho\otimes\chi$ and $n=2$ then $\chi^2=1$; if
moreover $\chi\ne1$ and $\rho$ is absolutely irreducible, every isomorphism $\phi\colon\rho\to\rho\otimes\chi$ has trace $0$
(Chapter 4). (c) Let $\rho\colon G_\Q\to\GL_2(\Zl)$ be continuous, $\ell$ odd, $k\ge1$. If
$\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$ then $\chi_\ell^2\equiv1\pmod{\ell^k}$ on $G_\Q$, which (as
$\chi_\ell(G_\Q)=\Zl^\times$) forces $\ell=3$ and $k=1$: for $\ell\ge5$, $\bar\chi_\ell^2\ne1$; for $\ell=3$,
$\chi_3^{\mathrm{cyc}}(\sigma)=2$ for some $\sigma$ and $4\not\equiv1\pmod9$. *Proved here.* Elementary. Paper use: Lemma lem:h0
("comparing determinants it forces $\bar\chi_\ell^2=1$, so $\ell=3$"; with (c), the length $h_\ell(E)$ is at most $1$,
and is $0$ for $\ell\ge5$, see Section 8 of this outline), Conjecture conj:euler, Section sec:anomaly ($h_3(E)=1$),
Lemma lem:twist and Theorem thm:twist ($a_p(f\otimes\chi)=\chi(p)a_p(f)$), Theorem thm:qual cases (b) and (c).

**galois:restriction** (definition and proposition). Let $K/F$ be finite separable inside $F^{\mathrm{sep}}$ and
$\rho\colon G_F\to\GL_n(k)$ continuous. (a) $\operatorname{Res}\rho=\rho|_{G_K}$ is continuous; $[\rho(G_F):\rho(G_K)]\le[K:F]$,
and it divides $[K:F]$ when $K/F$ is Galois ($\rho(G_K)$ is then normal in $\rho(G_F)$ with quotient a quotient of
$\Gal(K/F)$). (b) (Image of a kernel.) If $K$ is the field cut out by a character $\delta\circ\rho$, with
$\delta\colon\GL_n(k)\to A$ a homomorphism, then $\rho(G_K)=\rho(G_F)\cap\ker\delta$ (Chapter 1). (c) For an elliptic curve
$E/\Q$ and $\ell$ odd, with $\det\bar\rho_{E,\ell}=\bar\chi_\ell$ (Chapter 9): $\bar\rho_{E,\ell}(G_{\Q(\zeta_\ell)})=
\bar\rho_{E,\ell}(G_\Q)\cap\SL_2(\F_\ell)$ and $\bar\rho_{E,\ell}(G_{\Q(\sqrt{\ell^*})})=\{g\in\bar\rho_{E,\ell}(G_\Q):
\det g\in(\F_\ell^\times)^2\}$ (take $\delta=\det$, resp. $\delta=(\tfrac{\det}{\ell})$); for $\ell=3$ both are the
determinant-one subgroup of the image. (d) The field cut out by $\operatorname{Res}\rho$ is $KF_\rho$, and
$\Gal(KF_\rho/K)\simeq\Gal(F_\rho/F_\rho\cap K)$ (galois:translation-theorem). (e) "$\rho$ is absolutely irreducible on
$G_K$" means that $\rho(G_K)$ fixes no proper nonzero subspace of $\bar k^n$; it depends only on the subgroup
$\rho(G_K)$. *Proved here.* Paper use: the hypothesis of Theorem thm:main, Theorem thm:qual and the quoted DDT
Theorem 3.15 ("absolutely irreducible when restricted to $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$"), $S_f$ (Section 4.2),
Proposition prop:ns (first sentence of the proof), Lemma lem:h0.

**galois:index-two-restriction** (proposition; the Galois form of Clifford theory for index two, Chapter 4). Let
$H\subset G$ be an open subgroup of index $2$ of a profinite group (for $G=G_\Q$: $H=G_K$, $K$ quadratic), $\chi\colon
G\to G/H\simeq\{\pm1\}$, $s\in G\setminus H$, $k$ a field with $\operatorname{char}k\ne2$, and $\rho\colon G\to\GL_2(k)$
continuous and absolutely irreducible. The following are equivalent: (i) $\rho|_H$ is not absolutely irreducible;
(ii) $\rho\simeq\rho\otimes\chi$ (over $k$, equivalently over $\bar k$, since $\Hom_G(\rho,\rho\otimes\chi)$ has dimension
at most one); (iii) $\rho\otimes\bar k\simeq\Ind_H^G\psi$ for a continuous character $\psi\colon H\to\bar k^\times$. When they
hold, $\rho|_H\otimes\bar k\simeq\psi\oplus\psi^s$ with $\psi^s(h)=\psi(s^{-1}hs)\ne\psi(h)$ for some $h$, and every isomorphism
$\rho\to\rho\otimes\chi$ has trace $0$. For $\bar\rho=\bar\rho_{E,\ell}$ and $K=\Q(\sqrt{\ell^*})$: (i) is the failure of
the hypothesis of Theorem thm:main; for $\ell=3$, $\chi_{-3}=\bar\chi_3$ and (ii) is $H^0(\Q,\ad\bar\rho\otimes\bar\chi_3)\ne0$
(Lemma lem:h0); for $\ell\ge5$, (ii) for $\chi_{\ell^*}$ can hold (the "dihedral" case excluded by $S_f$) but is not the
condition $\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$, which never holds (galois:twist (c)). *Proved here* from Chapter 4
(Clifford theory, Frobenius reciprocity) plus continuity (an induced representation from an open subgroup is
continuous). Paper use: Lemma lem:h0 ("$\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ iff $\bar\rho$ is induced from
$\Gal(\Qbar/\Q(\sqrt{-3}))$, that is, iff its restriction there is not absolutely irreducible"), Proposition prop:ns
("$\bar\rho\simeq\Ind\psi$ by Frobenius reciprocity, so $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$"), Theorem thm:main
hypothesis, Section 1.3 of the paper (see Section 8 of this outline).

**galois:reduction-ss** (proposition). Let $E/\Q_\ell$ be finite with ring of integers $\mathcal{O}$, uniformiser $\lambda$,
residue field $k$, and $\rho\colon G\to\GL_n(E)$ continuous, $G$ profinite. For two $G$-stable $\mathcal{O}$-lattices
$\Lambda,\Lambda'$ the reductions $\bar\rho_\Lambda$, $\bar\rho_{\Lambda'}$ have the same characteristic polynomials (the
reductions of those of $\rho$, which lie in $\mathcal{O}[X]$), hence isomorphic semisimplifications (Brauer-Nesbitt,
Chapter 4, applied to a common finite quotient of $G$); so $\bar\rho^{ss}$ is well defined. If $\bar\rho_\Lambda$ is
irreducible, $\Lambda'$ is homothetic to $\Lambda$ (Ribet's lemma, Chapter 4). *Proved here* (Ribet's lemma quoted).
Serre, Abelian l-adic representations, Chapter I; DDT, Section 1. Paper use: Lemma lem:old ("$\bar\rho_h$"), Section
4.2 ($M_{f,\lambda}$ and $T_\ell E$ homothetic, so their adjoints coincide).

**galois:l-adic-kummer** (construction and proposition). Let $\ell\ne\operatorname{char}F$ and $a\in F^\times$. Choose a
compatible system $(\alpha_k)_{k\ge0}$ in $F^{\mathrm{sep}}$ with $\alpha_0=a$ and $\alpha_{k+1}^\ell=\alpha_k$. (a)
$\kappa_a(\sigma)=(\sigma(\alpha_k)/\alpha_k)_k\in\Zl(1)$ defines a continuous map $\kappa_a\colon G_F\to\Zl(1)$ with
$\kappa_a(\sigma\tau)=\kappa_a(\sigma)+\chi_\ell(\sigma)\kappa_a(\tau)$ ($\Zl(1)$ written additively): a continuous $1$-cocycle
(Chapter 16). Equivalently, after choosing a generator of $\Zl(1)$, $\sigma\mapsto\begin{pmatrix}\chi_\ell(\sigma)&
\kappa_a(\sigma)\\0&1\end{pmatrix}$ is a continuous homomorphism $G_F\to\GL_2(\Zl)$; it is the action on the $\Zl$-span of
a basis $e_1\in\Zl(1)$, $e_2$ with $\sigma e_2=e_2+\kappa_a(\sigma)e_1$. (b) Changing the system changes $\kappa_a$ by the
coboundary $\sigma\mapsto(\chi_\ell(\sigma)-1)z$, $z\in\Zl(1)$; $\kappa_{ab}=\kappa_a+\kappa_b$ for the product systems; and
$\kappa_a\bmod\ell^k$ restricted to $G_{F(\mu_{\ell^k})}$ is the Kummer character $\chi_a$ with $n=\ell^k$. (c) On
$\ker\chi_\ell=G_{F(\mu_{\ell^\infty})}$ the map $\kappa_a$ is a homomorphism, and for $\sigma\in G_F$, $\tau\in\ker\chi_\ell$:
$\kappa_a(\sigma\tau\sigma^{-1})=\chi_\ell(\sigma)\kappa_a(\tau)$. (d) If $K\supset F$ contains $\mu_{\ell^k}$, then
$\kappa_a\bmod\ell^k$ vanishes on $G_K$ iff $a\in(K^\times)^{\ell^k}$. *Proved here.* Serre, Abelian l-adic
representations, Chapter IV (Tate curves; for the shape); NSW, Chapter VI. Paper use: Lemma lem:tamfactor ("$\kappa$
the Kummer class of $q_E$", the matrix $\begin{psmallmatrix}\chi_\ell\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$, "the
restriction of $\kappa$ to $I$ is $n$ times the tame character", and, via (c) with $\sigma=\Frob$, $\tau=t$ in inertia,
$\Frob\,t\,\Frob^{-1}=t^q$), Lemma lem:tamagawa-exp (by (d) with $F=\Q_q$, $K=\Q_q^{\mathrm{ur}}$, $G_K=I_q$: inertia acts
trivially on $E[\ell^t]$ iff the Tate parameter is an $\ell^t$-th power in $\Q_q^{\mathrm{ur}}$; Chapter 7 turns this into
$\ell^t\mid n_q$); Chapters 7, 10, 11, 17.

### Section 9. Frobenius elements (foreshadowed) and the Chebotarev density theorem

**galois:frobenius-preview** (statement; the definitions and proofs are in Chapter 6, the local form in Chapter 7).
Let $K/\Q$ be finite Galois and $p$ a prime unramified in $K$. (a) For each prime $\mathfrak P$ of $\mathcal{O}_K$ above $p$
there is a unique $\Frob_{\mathfrak P}\in\Gal(K/\Q)$ with $\Frob_{\mathfrak P}(x)\equiv x^p\pmod{\mathfrak P}$ for all
$x\in\mathcal{O}_K$ (arithmetic Frobenius, C2); the $\Frob_{\mathfrak P}$, $\mathfrak P\mid p$, form one conjugacy class
$\Frob_p$; the order of $\Frob_{\mathfrak P}$ is the residue degree, and $p$ splits completely in $K$ iff $\Frob_p=1$.
(b) For $K'\subset K$ Galois over $\Q$, $\Frob_p(K/\Q)$ restricts to $\Frob_p(K'/\Q)$. (c) In $\Q(\zeta_n)$, $p\nmid n$:
$\Frob_p=\sigma_p$, so $\bar\chi_\ell(\Frob_p)=p\bmod\ell$ and $\chi_\ell(\Frob_p)=p$; in $\Q(\sqrt d)$, $p\nmid D$:
$\chi_d(\Frob_p)=\bigl(\tfrac Dp\bigr)$. (d) In $G_\Q$: a Frobenius element at $p$ is any $\sigma\in G_\Q$ whose
restriction to each finite Galois $K$ unramified at $p$ lies in $\Frob_p(K/\Q)$ and which comes from a decomposition
group at a prime above $p$; it is well defined up to conjugation and up to the inertia group. Hence for a continuous
$\rho$ of $G_\Q$ unramified at $p$ (trivial on the inertia groups at $p$) the conjugacy class of $\rho(\Frob_p)$, in
particular its characteristic polynomial, is well defined. (e) (Dedekind.) If $f\in\Z[x]$ is separable with leading
coefficient $a$ and $p\nmid a\disc(f)$, and $f\bmod p$ has irreducible factors of degrees $d_1,\dots,d_r$, then
$\Frob_p$ acts on the roots of $f$ with cycle type $(d_1,\dots,d_r)$. *Stated; reference* (Chapter 6; Neukirch I.9 and
I.8). Paper use: Lemma lem:old ("$X^2-a_p(h)X+p$" as characteristic polynomial of $\bar\rho_h(\Frob_p)$, the
eigenvalues of $\bar\rho(\Frob_p)$), Lemma lem:euler, Lemma lem:tamfactor ($\Frob$), Lemma lem:h0 ($a_p$ at primes
inert in $\Q(\sqrt{\ell^*})$).

**galois:frobenius-on-lines** (worked example, using the black box). For $E/\Q$ with good reduction at $p\ne3$ and
$p\nmid\disc(\psi_3)$, $\bar\rho_{E,3}(\Frob_p)$ has characteristic polynomial $X^2-a_pX+p\bmod3$ (Chapters 9, 11), and
by galois:frobenius-preview (e) and galois:quartic-on-lines the degrees of the factors of $\psi_3\bmod p$ are the orbit
sizes of $\bar\rho(\Frob_p)$ on the four lines: $X^2\pm X-1$ (order $8$) gives $(4)$; $X^2+1$ (order $4$) gives $(2,2)$;
$X^2-1$ (determinant $-1$, trace $0$) gives $(1,1,2)$; $(X\mp1)^2$ gives $(1,3)$ when $\bar\rho(\Frob_p)\ne\pm1$ and
$(1,1,1,1)$ otherwise. Checked for 11a1 and 121a1 at all primes $p<40$, $p\ne3,11$ (for 11a1: $p=2,5,17,23$ give
$(4)$; $p=7,13,31$ give $(1,3)$; $p=19,37$ give $(2,2)$; $p=29$ gives $(1,1,2)$). *Proved here* (given the black boxes).
Paper use: Proposition prop:ns, Section sec:data (consistency of the image labels with $\psi_3$), Chapter 22.

**galois:density** (definition). For a set $X$ of primes: its Dirichlet density is $\lim_{s\to1^+}\sum_{p\in X}p^{-s}/
\log\frac1{s-1}$ and its natural density is $\lim_{x\to\infty}\#\{p\le x:p\in X\}/\pi(x)$, when these exist. A set with a
natural density has the same Dirichlet density; finite sets have density $0$; "density one" means that the
complement has density $0$; "almost all $p$" means all but finitely many. *Definition; the comparison stated.* Serre,
Course in Arithmetic, Chapter VI, Section 4. Paper use: Lemma lem:old ("for all primes $p\nmid\ell N$"), Section 3
("for all $p\nmid3N$").

**galois:chebotarev** (theorem, Chebotarev's density theorem). Let $K/\Q$ be finite Galois with group $G$ and
$C\subset G$ a conjugacy class. The set of primes $p$, unramified in $K$, with $\Frob_p=C$ has Dirichlet density
$\#C/\#G$; it also has natural density $\#C/\#G$. The same holds for $K/F$ finite Galois of number fields, with
primes of $F$. Special cases: $K=\Q(\zeta_n)$ gives Dirichlet's theorem (density $1/\varphi(n)$ for each class
$a\in(\Z/n)^\times$); $K=\Q(\sqrt d)$: half the primes split; $K$ the splitting field of $x^3-2$: $x^3-2$ has exactly
one root mod $p$ for density $1/2$ of the primes (transpositions; precisely the $p\equiv2\bmod3$), three roots for
density $1/6$ and none for density $1/3$ (checked numerically: $0.516$, $0.159$, $0.325$ for $5\le p<3000$).
*Stated; reference.* Neukirch VII.13 (Dirichlet density); Serre, Abelian l-adic representations, Chapter I, Section
2.2 (with the natural-density form). Paper use: Lemma lem:old ("by Chebotarev and Brauer-Nesbitt").

**galois:chebotarev-dense** (corollary). Let $L/\Q$ be Galois (possibly infinite) and unramified outside a finite set
$S$ of primes (every finite subextension is), and let $X$ be a set of primes of Dirichlet density one. Then the
Frobenius elements $\Frob_{\mathfrak P}\in\Gal(L/\Q)$ at primes $\mathfrak P$ of $L$ above $p\in X\setminus S$ are dense in
$\Gal(L/\Q)$. (Proof: a basic open set is a coset of $\Gal(L/K)$ with $K/\Q$ finite Galois; the primes whose Frobenius
in $\Gal(K/\Q)$ is the class of the coset have density at least $1/\#\Gal(K/\Q)>0$ and so meet $X\setminus S$.)
*Proved here* from galois:chebotarev. Serre, Abelian l-adic representations, Chapter I, Section 2.2. Paper use:
Lemma lem:old.

**galois:chebotarev-brauer-nesbitt** (corollary; the form the paper uses). Let $k$ be a finite field, $\Fbar_\ell$, or a
finite extension of $\Q_\ell$, and $\rho_1,\rho_2\colon G_\Q\to\GL_n(k)$ continuous, semisimple, and unramified outside a
finite set $S$. If $\det(X-\rho_1(\Frob_p))=\det(X-\rho_2(\Frob_p))$ for all $p$ in a set of density one (with
$p\notin S$), then $\rho_1\simeq\rho_2$. (Proof: let $L$ be the field cut out by $\rho_1\oplus\rho_2$, unramified outside
$S$; $g\mapsto\det(X-\rho_1(g))-\det(X-\rho_2(g))$ is continuous on $\Gal(L/\Q)$ and vanishes on the dense set of
Frobenius elements, hence everywhere; then Brauer-Nesbitt, Chapter 4: for finite or discrete $k$ the image of
$\Gal(L/\Q)$ is finite and the finite-group form suffices; for $\ell$-adic $k$ use the form for an arbitrary group, or
in characteristic $0$ the fact that traces determine a semisimple representation.) *Proved here* from
galois:chebotarev-dense and Chapter 4. DDT, Section 1; Serre, Abelian l-adic representations, Chapter I. Paper use:
Lemma lem:old (the step $p\nmid\ell N$), Section 3 ("$\bar\rho_g\simeq\bar\rho$, that is, $a_p(g)\equiv a_p(f)\pmod\lambda$
for all $p\nmid3N$"); Chapters 11 and 15.

**galois:congruent-ap** (corollary). Let $\mathcal{O}$ be the ring of integers of a finite extension of $\Q_\ell$, $\lambda$ its
maximal ideal, $k=\mathcal{O}/\lambda$, and $\rho_1,\rho_2\colon G_\Q\to\GL_2(\mathcal{O})$ continuous and unramified outside a finite
set $S$, with $\tr\rho_1(\Frob_p)\equiv\tr\rho_2(\Frob_p)$ and $\det\rho_1(\Frob_p)\equiv\det\rho_2(\Frob_p)\pmod\lambda$ for
all $p$ in a set of density one. Then $\bar\rho_1^{ss}\simeq\bar\rho_2^{ss}$ over $k$; if moreover $\bar\rho_1$ is absolutely
irreducible, $\bar\rho_2\simeq\bar\rho_1$ (a two-dimensional representation whose semisimplification is irreducible is
irreducible). Conversely $\bar\rho_1^{ss}\simeq\bar\rho_2^{ss}$ gives the congruences at every $p\notin S$. Application
(with the Chapter 15 black box: a newform $h$ of weight $2$ and level $M$ with coefficients in $\mathcal{O}$ has
$\rho_{h,\lambda}\colon G_\Q\to\GL_2(\mathcal{O})$, unramified outside $M\ell$, $\det=\chi_\ell$, $\tr\rho_{h,\lambda}(\Frob_p)=a_p(h)$ for
$p\nmid M\ell$): if $a_p(h)\equiv a_p(f)\pmod\lambda$ for almost all $p$, then $\bar\rho_{h,\lambda}^{ss}\simeq\bar\rho_{f,\lambda}^{ss}$,
and for $f=f_E$ with $\bar\rho_{E,\ell}$ irreducible (hence absolutely irreducible, galois:complex-conjugation)
$\bar\rho_{h,\lambda}\simeq\bar\rho_{E,\ell}\otimes_{\F_\ell}k$. Note that the two residual representations may be defined over
different finite fields; compare them over a common finite extension. *Proved here* (given the Chapter 15 black
box). Paper use: Lemma lem:old ("Consequently $\bar\rho_h\simeq\bar\rho$ by Chebotarev and Brauer-Nesbitt,
$\bar\rho$ being irreducible"), Section 3 cases (a) to (c) and the Example (121a1 with 11a1, 539c1 with 11a1, 980i1
with 20a1).

## 3. Coverage check: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row or paper hook | line-up items |
|-|-|
| field extensions, degree | galois:field-extension-degree |
| algebraic and transcendental elements, minimal polynomials | galois:algebraic-element, galois:algebraic-extensions, galois:algebraic-closure |
| splitting fields | galois:splitting-field |
| separability | galois:separability, galois:separable-closure |
| normal extensions | galois:normal-extension |
| Galois extensions, the Galois group | galois:dedekind-independence, galois:artin-fixed-field, galois:galois-extension |
| fundamental theorem of Galois theory | galois:fundamental-theorem, galois:translation-theorem |
| examples: quadratic fields | galois:quadratic-extensions, galois:quadratic-characters |
| examples: $\Q(\zeta_n)$ with group $(\Z/n)^\times$ | galois:cyclotomic, galois:cyclotomic-mod-p, galois:finite-field-galois |
| examples: $\Q(2^{1/3},\zeta_3)$ | galois:x3minus2, galois:kummer-affine, galois:cubic |
| Kummer theory for cyclic extensions of degree $n$ with $\zeta_n\in F$ | galois:hilbert90, galois:kummer-character, galois:kummer-cyclic |
| mod $n$ version: $F^\times/(F^\times)^n$ classifies $\Z/n$-extensions | galois:kummer-classification (c), galois:kummer-finite-field |
| Artin-Schreier (statement) | galois:artin-schreier |
| Galois group of a polynomial, action on roots | galois:galois-group-polynomial |
| discriminant and transitivity, irreducibility | galois:galois-group-polynomial (b), galois:discriminant |
| cubic and quartic polynomials | galois:cubic, galois:quartic |
| quartic with group in $\GL_2(\F_3)$ acting on lines; 3-division polynomial (two quadratics for $N_s(\F_3)$, irreducible for $N_{ns}(\F_3)$, $\GL_2(\F_3)$) | galois:quartic-on-lines, galois:ns-example, galois:frobenius-on-lines |
| infinite Galois extensions and the Krull topology | galois:infinite-galois-limit |
| infinite fundamental theorem | galois:infinite-fundamental-theorem |
| profinite groups | galois:infinite-galois-limit (with Chapter 1, items 7.1 to 7.5) |
| $G_\Q$ and $G_K$ | galois:absolute-galois-group |
| continuous characters and representations of profinite groups | galois:continuous-reps, galois:quadratic-characters, galois:twist, galois:reduction-ss |
| Frobenius elements (foreshadowed) | galois:finite-field-galois, galois:cyclotomic-mod-p, galois:frobenius-preview |
| Chebotarev density theorem (statement) | galois:density, galois:chebotarev, galois:chebotarev-dense |
| corollary: semisimple representation determined by Frobenius characteristic polynomials on a density-one set | galois:chebotarev-brauer-nesbitt |
| corollary: congruent $a_p$ for almost all $p$ give isomorphic residual semisimplifications (with Brauer-Nesbitt) | galois:congruent-ap |
| complex conjugation as an element of order two of $G_\Q$ | galois:complex-conjugation |
| quadratic characters of $G_\Q$ and $\Q(\sqrt d)$ | galois:quadratic-characters, galois:quadratic-extensions |
| $\Q(\sqrt{\ell^*})$ as the quadratic subfield of $\Q(\zeta_\ell)$ | galois:sqrt-lstar, galois:cyclotomic-character (c) |
| restriction of representations to open subgroups such as $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$ | galois:restriction, galois:index-two-restriction, galois:translation-theorem |
| cyclotomic character, $\Zl(1)$ (needed by Section 4 of the paper) | galois:cyclotomic-character |
| hook: hypothesis "absolutely irreducible on $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$" (Theorem thm:main, Theorem thm:qual, $S_f$, DDT 3.15) | galois:sqrt-lstar, galois:absolute-galois-group, galois:restriction, galois:index-two-restriction, galois:complex-conjugation (d) |
| hook: Proposition prop:ns | galois:restriction (b), (c); galois:index-two-restriction; galois:galois-group-polynomial; galois:discriminant; galois:quartic-on-lines; galois:ns-example; galois:complex-conjugation |
| hook: Lemma lem:h0 | galois:sqrt-lstar (d), galois:cyclotomic-character, galois:twist, galois:index-two-restriction, galois:complex-conjugation (d) |
| hook: Lemma lem:old (Chebotarev and Brauer-Nesbitt) | galois:frobenius-preview, galois:chebotarev, galois:chebotarev-dense, galois:chebotarev-brauer-nesbitt, galois:congruent-ap, galois:reduction-ss |
| hook: Lemma lem:tamagawa-exp (Kummer theory, $\ell^t$-th roots of the Tate parameter) | galois:kummer-character, galois:kummer-classification, galois:l-adic-kummer (d) |
| hook: Lemma lem:tamfactor (Kummer classes) | galois:l-adic-kummer, galois:kummer-affine, galois:kummer-finite-field, galois:cyclotomic-character (d) |
| Section 6 row: $\rho_{E,\ell}$, restriction to $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$ | galois:continuous-reps, galois:restriction |
| Section 6 row: 3-division polynomial, its factorisation pattern | galois:quartic-on-lines, galois:frobenius-on-lines |
| Section 6 row: Chebotarev, Brauer-Nesbitt | galois:chebotarev-brauer-nesbitt, galois:congruent-ap |
| Section 6 row: Kummer theory, Kummer classes | galois:kummer-classification, galois:l-adic-kummer |
| also used: $\chi_{-3}$, $\chi_{-4}$, $\chi_{q^*}$, $\chi_S$ (table of Section 1, Lemma lem:euler, Lemma lem:twist, Theorem thm:twist) | galois:quadratic-characters, galois:twist |

## 4. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2, stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | thm:main hypothesis and $S_f$; prop:ns; lem:h0; lem:old; lem:tamagawa-exp; lem:tamfactor; $\chi_{-3},\chi_{-4},\chi_{q^*},\chi_S$ in Section 1, lem:euler, lem:twist, thm:twist | 40 |
| 1 | Field extensions and algebraic elements | conventions C1 to C7 as `convention` environments; galois:field-extension-degree to galois:algebraic-closure | 150 |
| 2 | Splitting fields, normality, separability | galois:splitting-field to galois:separable-closure | 190 |
| 3 | Galois extensions and the fundamental theorem | galois:dedekind-independence to galois:translation-theorem; one picture-free subgroup/subfield diagram in `tabular` | 200 |
| 4 | Finite fields, quadratic and cyclotomic extensions | galois:finite-field-galois to galois:x3minus2 | 220 |
| 5 | Cyclic extensions: Hilbert 90, Kummer, Artin-Schreier | galois:norm-trace to galois:artin-schreier; `paperlink` for lem:tamagawa-exp and lem:tamfactor | 230 |
| 6 | The Galois group of a polynomial | galois:galois-group-polynomial to galois:ns-example; the orbit table; `paperlink` for prop:ns | 250 |
| 7 | Infinite Galois theory, $G_\Q$, $\chi_\ell$, complex conjugation | galois:infinite-galois-limit to galois:complex-conjugation | 200 |
| 8 | Continuous representations of profinite groups | galois:continuous-reps to galois:l-adic-kummer; `paperlink` for the hypothesis of thm:main and lem:h0 | 230 |
| 9 | Frobenius elements and Chebotarev | galois:frobenius-preview to galois:congruent-ap; `paperlink` for lem:old | 170 |
| 10 | Exercises | 15 exercises, graded (list below) | 110 |
| 11 | Notes and references | Lang, Dummit-Foote, Milne (Fields and Galois Theory), Neukirch, NSW, Washington, Serre (Abelian l-adic representations, Course in Arithmetic), DDT; which numbers were cited | 40 |
| | **total** | | **2030** |

Exercises (Section 10), graded from easy to harder:
1. Show $\Q(\sqrt2,\sqrt3)=\Q(\sqrt2+\sqrt3)$ (minimal polynomial $x^4-10x^2+1$) and list its intermediate fields.
2. Compute the Galois group of $x^4-2$ over $\Q$ ($D_4$, order $8$) and over $\Q(i)$ ($C_4$, by Kummer theory).
3. Show that $x^3-3x+1$ has discriminant $81$ and splitting field $\Q(\zeta_9+\zeta_9^{-1})$.
4. Prove $\disc(\Phi_\ell)=(-1)^{(\ell-1)/2}\ell^{\ell-2}$ and deduce $\sqrt{\ell^*}\in\Q(\zeta_\ell)$ without Gauss sums.
5. Show that $\Q(\sqrt{-5})\subset\Q(\zeta_{20})$ and $\Q(\sqrt6)\subset\Q(\zeta_{24})$, and that neither lies in a smaller
   cyclotomic field.
6. Prove that the degree of a splitting field of a polynomial of degree $n$ divides $n!$.
7. Prove that $x^p-x-1$ is irreducible over $\F_p$, with splitting field $\F_{p^p}$.
8. Let $u\in\F_{13}^\times$. Show that $u$ is a cube iff $u^4=1$, and compute the class of $u=2$ in
   $\F_{13}^\times/(\F_{13}^\times)^3$ (illustrating galois:kummer-finite-field with $\ell=3$, $v=1$).
9. Show that $\phi_p^{\Z}$ is dense and not closed in $\Gal(\Fbar_p/\F_p)$, and that $\Gal(\Q(\mu_{\ell^\infty})/\Q)\simeq\Zl^\times$.
10. Show that every continuous homomorphism from a profinite group to $\C^\times$ has finite image.
11. Let $\bar\rho\colon G_\Q\to\GL_2(\F_\ell)$, $\ell$ odd, with $\det\bar\rho=\bar\chi_\ell$. Prove that $\bar\rho$ is irreducible iff it
    is absolutely irreducible, and that $\bar\rho(G_{\Q(\sqrt{\ell^*})})$ is the set of elements of the image with square
    determinant.
12. Check the paper's claim (Proposition prop:ns) on $y^2=x^3-6x-8$: factor $\psi_3$, find the three quadratic subfields
    of its splitting field, deduce that the image of $\bar\rho_{E,3}$ is $N_s(\F_3)$, and verify $a_p\equiv0\pmod3$ for
    the primes $p\equiv2\pmod3$ below $50$.
13. For 11a1, check that $\psi_3=3x^4-4x^3-60x^2-237x-21$ has discriminant $-3^3\cdot11^{10}$, so that
    $\Q(\sqrt{\disc\psi_3})=\Q(\sqrt{-3})$, and compare the factorisations of $\psi_3$ modulo $19$ and $29$ with
    $a_{19}=a_{29}=0$.
14. Let $\rho\colon G_\Q\to\GL_2(\Z_3)$ be continuous. Show that $\rho\bmod9\not\simeq(\rho\otimes\chi_3^{\mathrm{cyc}})\bmod9$, with $\chi_3^{\mathrm{cyc}}$ the $3$-adic cyclotomic character,, and deduce, with
    the description of $h_\ell(E)$ in Lemma lem:h0 (proved in Chapter 11), that $h_3(E)\le1$ and $h_\ell(E)=0$ for
    $\ell\ge5$.
15. Using Chebotarev, compute the densities of the primes $p$ for which $x^3-2$ has $0$, $1$, $3$ roots modulo $p$, and
    compare with a count of the primes below $3000$.

## 5. Dependencies and forward pointers

Results from other chapters used here:
* Chapter 1 (`ch:groups`): groups, cyclic groups and their $\ell^k$-th powers (1.3), index-two subgroups and the
  image of a kernel (1.6), group actions and orbits (3.1 to 3.3), $\GL_2(\F_3)$: the four lines, $\PGL_2(\F_3)\simeq S_4$,
  $\det=$ sign (5.3, 5.4), the subgroup and orbit tables and the three images (6.3 to 6.9), profinite groups, inverse
  limits, $\Zl$, $\hat\Z$, $\GL_2(\Zl)$ (7.1 to 7.5). Chapter 5 must use, not redo, these.
* Chapter 2 (`ch:rings`): polynomial rings, Gauss's lemma, Eisenstein, $\Z/n$ and $(\Z/n)^\times$, finite fields
  (existence, uniqueness, cyclic multiplicative group), cyclotomic polynomials and $x^n-1=\prod_{d\mid n}\Phi_d$, Gauss
  sums ($g^2=\ell^*$), Legendre and Kronecker symbols, $q^*$, quadratic reciprocity.
* Chapter 4 (`ch:reps`): irreducibility and absolute irreducibility, Schur, Jordan-Holder and semisimplification,
  Brauer-Nesbitt (needed for an arbitrary group, or at least for finite groups plus the characteristic-zero trace
  criterion), Clifford theory for index two, induction and Frobenius reciprocity, the trace-zero lemma, Ribet's lemma
  on lattices (statement).
* Background (PLAN Section 2): linear algebra, the fundamental theorem of algebra (complex analysis), elementary
  point-set topology (product topology; Tychonoff is quoted in Chapter 1).

Black boxes imported from later chapters (stated here with a forward `\Cref`, never used in a proof of an earlier
item): Frobenius elements and their properties (Chapter 6), Kronecker-Weber (Chapter 6), $\det\rho_{E,\ell}=\chi_\ell$ and
the four lines of $E[3]$ as the roots of $\psi_3$ (Chapter 9), the Galois representations of newforms (Chapter 15).

Forward pointers (chapters that use this one):
* Chapter 6 (`ch:ant`): primitive element theorem (number fields), Galois theory of $\Q(\zeta_n)$ and $\Q(\sqrt d)$,
  $\Q(\sqrt{\ell^*})\subset\Q(\zeta_\ell)$, decomposition and inertia groups inside $\Gal(K/\Q)$, Frobenius (made precise
  there), Chebotarev in number-field form (restated there with the Frobenius made precise), quadratic characters as
  Dirichlet characters.
* Chapter 7 (`ch:local`): finite fields and $G_{\F_q}\simeq\hat\Z$, unramified extensions, Kummer theory over $\Q_p$
  and $\Q_p^{\mathrm{ur}}$, the $\ell$-adic Kummer cocycle and the tame character, $\Frob\,t\,\Frob^{-1}=t^q$, the
  translation theorem ("unramified base change does not change inertia").
* Chapter 9 (`ch:ellcurves`): Galois action on $E[m]$ and $T_\ell E$, the 3-division polynomial and its roots, quadratic
  twists by $\chi_d$.
* Chapter 10 (`ch:reduction`): the Tate curve, $E_{\mathsf q}[\ell^t]$ generated by $\mu_{\ell^t}$ and an $\ell^t$-th root of $\mathsf q$.
* Chapter 11 (`ch:galrep`): continuity of $\rho_{E,\ell}$, irreducible versus absolutely irreducible via complex
  conjugation, restriction to $G_{\Q(\sqrt{\ell^*})}$, the proofs of Proposition prop:ns and Lemma lem:h0, the
  isomorphism class of $\bar\rho_{E,\ell}$ determined by the $a_p\bmod\ell$.
* Chapter 15 (`ch:modgalrep`): Lemma lem:old (Chebotarev and Brauer-Nesbitt), congruences between newforms, the
  optimal-level theorem's hypothesis at $\ell=3$.
* Chapters 16 and 17 (`ch:cohomology`, `ch:galcoh`): Hilbert 90 in cohomological form, $H^1(K,\mu_n)=K^\times/K^{\times n}$,
  the Kummer class in $H^1(K,\Zl(1))$, continuous cohomology of $G_K$, $G_\R=\{1,c\}$.
* Chapter 18 (`ch:blochkato`): $\ell$-adic representations of $G_\Q$, Tate twists $V(n)$, $\Zl(1)$.
* Chapters 20, 21, 22: the hypothesis $\ell\notin S_f$, the `ns3` test, the image labels.

## 6. Notes for the writer

Conventions to fix (Section 1, as `convention` environments): C1 to C7 of Part 1. In addition:
* Composition of automorphisms is $(\sigma\tau)(x)=\sigma(\tau(x))$; groups act on the left; $\sigma(\zeta)=\zeta^{\chi(\sigma)}$.
* $\Zl(1)$ is written multiplicatively as $\varprojlim\mu_{\ell^k}$ and additively when it carries cocycles; say once which.
* The quadratic character of conductor $q$ is always $\chi_{q^*}$, never $\chi_q$ (the paper's $\chi_q$ appears only when quoting the paper; decision D3), and never "the Legendre symbol mod $q$ as a character of
  $\Z$" without the identification through Frobenius; $\chi_{\ell^*}=\bar\chi_\ell^{(\ell-1)/2}$ is not $\bar\chi_\ell$ unless
  $\ell=3$. The paper itself slips on this once (Section 8 below, point 2).
* "Density" means Dirichlet density unless stated; "almost all" means all but finitely many.
* Use the paper's macros and the preamble's (`\Gal`, `\Frob`, `\Qbar`, `\Fbar`, `\Zl`, `\GL`, `\SL`, `\PGL`, `\Ind`, `\Res`,
  `\Aut`, `\Hom`, `\tr`, `\Tr`, `\Nm`, `\disc`, `\sgn`); $\operatorname{Res}$ for the resultant must not clash with the restriction
  `\Res`: write the resultant as $\operatorname{Res}_x(f,g)$ or $\operatorname{res}(f,g)$ and say so.
* Labels: `def:galois:...`, `thm:galois:...` etc.; the line-up names above are ready to be used as the label stems.

Pitfalls:
* Do not present the infinite fundamental theorem without the word "closed"; give the $\phi_p^{\Z}$ example.
* Kummer theory needs $\mu_n\subset F$ and $\operatorname{char}F\nmid n$; $x^3-2$ over $\Q$ is the example of what fails
  without roots of unity (not Galois, group $S_3$ of the affine shape). In the paper's uses the base field is
  $\Q_q^{\mathrm{ur}}$ (or $\F_q$ for $k\le v_\ell(q-1)$), which contains the relevant roots of unity because $q\ne\ell$; say so
  in the `paperlink`.
* Frobenius: everything in Section 9 that mentions primes of number fields is a black box from Chapter 6; label the
  items "stated" and make sure no proof in Sections 1 to 8 depends on them. The finite-field Frobenius
  (galois:finite-field-galois, galois:cyclotomic-mod-p) is proved here and is the honest preview.
* The quartic-on-lines proposition needs an equivariant bijection between roots and lines; for $\psi_3$ this is the
  map $\pm P\mapsto x(P)$ from Chapter 9 (distinct lines have distinct $x$-coordinates because $x(P)=x(Q)$ iff $Q=\pm P$).
  $\psi_3$ has leading coefficient $3$; irreducibility over $\Q$ is up to this constant, and Dedekind's theorem needs
  $p\ne3$.
* $N_s(\F_3)$ acts absolutely irreducibly on $\F_3^2$; only its determinant-one subgroup $C_4$ does not. The $N_s$ image
  has two orbits on lines although $E[3]$ is irreducible: the factorisation pattern detects the image, not
  reducibility. Reducible $E[3]$ always gives a linear factor of $\psi_3$ (a rational line), patterns $1+3$ or $1+1+2$.
* Brauer-Nesbitt: the paper's use is over finite fields and finite images, so the finite-group form from Chapter 4
  suffices; the residual representations of $f$ and $h$ live over possibly different finite fields, compare over a
  common one. Absolute irreducibility of $\bar\rho_{E,\ell}$ (from complex conjugation) is what upgrades
  "isomorphic semisimplifications" to "isomorphic"; make this explicit (the paper says only "irreducible").
* Natural versus Dirichlet density: Chebotarev with natural density is true but deeper; only positivity of the
  Dirichlet density is needed for galois:chebotarev-dense. Do not claim more than is cited.
* The Artin-Schreier theorem on real closed fields (complex conjugations are the only torsion in $G_\Q$) and the
  Artin-Schreier theory of degree-$p$ extensions share a name; say so.
* The tower $\Q\subset\Q(\sqrt2)\subset\Q(2^{1/4})$ (normality not transitive) and $\Q(2^{1/3})$ (not normal) should both
  appear, since "the field cut out by" is always a Galois extension and readers confuse the two.
* Typography (PLAN.md 7.2): no dash ligatures anywhere ("Artin-Schreier", "Kappe-Warren", "Brauer-Nesbitt" with plain
  hyphens; ranges as "1 to 8"); ASCII source; the orbit table as `tabular` with `booktabs`.
* The theorem numbers for Lang and Dummit-Foote kept in Sections 1 to 3 of Part 2 (Lang V.1 Proposition 1.2, Lang VI.1
  Theorems 1.1 and 1.8, Lang V.4 Theorem 4.6, Lang VI.4 Theorem 4.1, Lang V.3 Theorem 3.3, Dummit-Foote 14.2 Theorems
  7 and 14) come from the first session and were not re-verified here; check them against the books or cite the
  section only. Every other reference in this outline is by chapter or section. Ireland-Rosen and Milne's "Fields
  and Galois Theory" are not in `refs.bib`: add them to `bib/ch05.bib` if cited.

Leave to other chapters:
* Chapter 2: construction of $\F_q$, quadratic reciprocity and its proofs, Gauss sums, Dirichlet characters.
* Chapter 4: all representation theory proper (Schur, Maschke, Brauer-Nesbitt, Clifford, induction); this chapter
  only translates to profinite groups and continuity.
* Chapter 6: rings of integers, primes, decomposition and inertia groups, the definition and existence of
  Frobenius, Dedekind's factorisation theorem, Kronecker-Weber, the Chebotarev theorem for number fields restated
  with the Frobenius made precise.
* Chapter 7: $\Q_p$, $\Q_p^{\mathrm{ur}}$, inertia, the tame character, Kummer theory over local fields, Hensel.
* Chapter 9 and 11: $\det\rho_{E,\ell}=\chi_\ell$ (Weil pairing), the division polynomials, the proofs of Proposition prop:ns
  and Lemma lem:h0 as statements about elliptic curves, Zywina's list.
* Chapters 16 and 17: group cohomology; Hilbert 90 and Kummer theory in the form $H^1(K,\mu_n)=K^\times/K^{\times n}$
  (this chapter proves the field-theoretic forms only, so that Chapter 17 can cite them); the identification of the
  image of the Kummer class of the Tate parameter with the class of its unit part (end of Lemma lem:tamfactor).
* Chapter 15: the Galois representations of newforms (used here only as a black box in galois:congruent-ap).

## 7. Verification log (computations done for this outline)

All scripts were short Python/sympy programs run in `/tmp/ch05`.
* $\GL_2(\F_3)$: all $48$ elements, all $55$ subgroups in $16$ conjugacy classes; for each class: order, surjectivity of
  $\det$, presence of an element of determinant $-1$ and trace $0$, fixed lines, orbits on the four lines, image in
  $S_4$ and whether it lies in $A_4$. Result: the table in galois:quartic-on-lines; $\det g$ equals the sign of the
  permutation of the lines for all $48$ elements.
* $\disc(x^3-2)=-108$; $\disc(x^3-3x+1)=81$ (irreducible); $\disc(\Phi_\ell)=(-1)^{(\ell-1)/2}\ell^{\ell-2}$ for
  $\ell=3,5,7,11,13$; $\disc(x^n-a)$ for $n\le6$; the resolvent cubic formula and $\disc(R_f)=\disc(f)$ symbolically; the
  general cubic discriminant on $x^3+x^2+x+1$ ($-16$).
* $\Phi_n\bmod p$ factors into $\varphi(n)/f$ distinct irreducibles of degree $f=\operatorname{ord}_n(p)$ for all $3\le n<40$,
  $p<60$, $p\nmid n$.
* For $5\le p<2000$: $x^2+3$ has a root mod $p$ iff $p\equiv1\pmod3$; $x^2+1$ iff $p\equiv1\pmod4$; for
  $\ell\in\{3,5,7,11,13\}$, $\ell^*$ is a square mod $p$ iff $p$ is a square mod $\ell$.
* $\psi_3$ of 11a1 ($[0,-1,1,-10,-20]$) and 121a1 ($[1,1,1,-30,-76]$): irreducible, $\disc=-3^3\cdot11^{10}$ and
  $-3^3\cdot11^4$; factorisation degrees mod $p<40$ match the orbit sizes predicted from $X^2-a_pX+p\bmod3$ (with $a_p$ by
  point counting). Resolvent cubic of $\psi_3$(11a1) irreducible.
* Search over $y^2=x^3+Ax+B$, $|A|,|B|\le30$, $AB\ne0$: $\psi_3$ is a product of two quadratics only for $(A,B)=(-6,\mp8)$
  ($j=-1728$); for $(-6,-8)$ the factors have discriminants $24$ and $-8$, the product is $-3$ times a square, the
  resolvent cubic has exactly one rational root, and $a_p\equiv0\pmod3$ for all $p\equiv2\pmod3$, $p\le71$, with
  $a_5=3$.
* $x^3-2$: proportions of primes $5\le p<3000$ with $0$, $1$, $3$ roots: $0.325$, $0.516$, $0.159$.

## 8. Points for important_notes.md

Points found while preparing this outline, in the area of Chapter 5 (Galois theory, Kummer theory, quadratic and
cyclotomic characters, restriction to $G_{\Q(\sqrt{\ell^*})}$, the 3-division polynomial). The gap in the proof of
Proposition prop:ns ("non-abelian and faithful") is already recorded from the Chapter 1 outline and is not repeated.

1. **Lemma lem:h0, last sentence of the statement and of the proof; Section sec:anomaly.** Problem: the paper
   proves finiteness of $H^0(\Q,\ad T(1)\otimes\Q_\ell/\Z_\ell)$ "for $E$ without complex multiplication" by saying that
   $\rho\simeq\rho\otimes\chi_\ell$ would force $a_p=0$ at the primes inert in $\Q(\sqrt{\ell^*})$. That argument confuses
   the cyclotomic character $\chi_\ell$ with the quadratic character $\chi_{\ell^*}$ ($\rho\simeq\rho\otimes\chi_\ell$ is
   impossible for every $E$, since it would give $p\,a_p=a_p$ for all good $p\ne\ell$). The true statement is much
   stronger and elementary: by the paper's own description of the length, $h_\ell(E)\ge k$ iff
   $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$; taking determinants, this forces $\chi_\ell^2\equiv1\pmod{\ell^k}$
   on $G_\Q$, and since $\chi_\ell(G_\Q)=\Zl^\times$ this happens only for $\ell=3$, $k=1$ ($4\not\equiv1\bmod9$). Hence
   $h_\ell(E)=0$ for $\ell\ge5$ and $h_3(E)\le1$, with equality iff $\bar\rho_{E,3}\simeq\bar\rho_{E,3}\otimes\chi_{-3}$, for every
   $E$ with $\bar\rho_{E,\ell}$ irreducible, CM or not. Fix: replace the finiteness sentence of the proof by this
   determinant argument (one line), drop "for $E$ without complex multiplication" there, and in Section sec:anomaly
   replace "$h_3(E)\le1$ because some prime $p<1223$ inert in $\Q(\sqrt{-3})$ has $9\nmid a_p$" by "$h_3(E)\le1$ by Lemma
   lem:h0" (the numerical check is valid but no longer needed). The paper's identification of the length with "the
   largest $k$ with $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$" is correct when $\bar\rho$ is absolutely
   irreducible (then the $\ell$-torsion of $H^0$ is at most one-dimensional, $H^0$ is cyclic, and an element of exact
   order $\ell^k$ is an isomorphism mod $\ell^k$ by Nakayama). Sure: high (the determinant computation is
   elementary; the outline's galois:twist (c) and Exercise 14 carry it).

2. **Section 1.3 of the paper ("Beyond the hypotheses"), paragraph after Conjecture conj:euler.** Problem: "The
   term $h_\ell(E)$ ... is positive exactly when $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$". For $\ell\ge5$ this is wrong:
   $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ (the case where $\bar\rho$ is induced from $\Q(\sqrt{\ell^*})$, excluded by
   $S_f$) can occur, but $h_\ell(E)=0$ always for $\ell\ge5$ (Lemma lem:h0 itself says so). The criterion of Lemma lem:h0
   is $\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$, and $\bar\chi_\ell=\chi_{\ell^*}$ only for $\ell=3$. Likewise the opening
   sentence of that subsection ("a correction term when the representation is induced from $\Q(\sqrt{\ell^*})$") is
   right only for $\ell=3$. Fix: "is positive exactly when $\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$, which forces
   $\ell=3$ (where $\bar\chi_3=\chi_{-3}$); for $\ell=3$ this happens precisely when ..." and "a correction term when
   $\ell=3$ and the representation is induced from $\Q(\sqrt{-3})$". Sure: high.

3. **Lemma lem:tamfactor, proof, "Finally $c'$ is the image of $\kappa$ in $H^1(G/I,\Zl(1)^I)$".** Problem: there is no
   natural map $H^1(G,\Zl(1))\to H^1(G/I,\Zl(1)^I)$ (inflation goes the other way, and $\kappa$ is not inflated: its
   restriction to $I$ is $n$ times the tame character). The value $c'=\kappa(\Frob)$ depends on the lift of $\Frob$ (by
   multiples of $n'$) and on the cocycle (by multiples of $q-1$). Fix: write $q_E=q^nu$, so $\kappa=n\kappa_q+\kappa_u$
   (galois:l-adic-kummer (b)); $\kappa_u$ is unramified, i.e. inflated from the class of $u$ in $H^1(G/I,\Zl(1))=
   \Zl(1)/(q-1)\simeq\F_q^\times\otimes\Zl$ (galois:kummer-finite-field (b), plus Hensel, Chapter 7); choosing the lift of
   $\Frob$ that fixes a compatible system of $\ell$-power roots of $q$ (possible because $\Q_q(q^{1/\ell^\infty})$ is totally
   ramified) gives $c'=\kappa_u(\Frob)$, and in general $c'$ is well defined modulo $(n',q-1)\Zl$, which does not change
   $\min(v_\ell(n),v_\ell(q-1),v_\ell(c'))$. The conclusion of the lemma is unaffected. Sure: high that the phrase is
   imprecise; high that the conclusion stands. (The Chapter 16 outline, writer note 10, records the indeterminacy;
   the Kummer side is in this chapter and Chapter 17.)

4. **Lemma lem:tamagawa-exp, statement and proof.** Problem (expository): the proof calls the Tate parameter $u$,
   while Lemma lem:tamfactor uses $u$ for its unit part $q_Eq^{-n}$; and "inertia acts trivially on $E[\ell^t]$ exactly
   when $u$ is an $\ell^t$-th power in $\Q_q^{\mathrm{ur}}$ up to units" mixes two statements. Fix: call the Tate parameter
   $q_E$; say "by Kummer theory over $\Q_q^{\mathrm{ur}}$, which contains $\mu_{\ell^t}$ as $q\ne\ell$, inertia acts trivially
   on $E[\ell^t]$ iff $q_E$ is an $\ell^t$-th power in $\Q_q^{\mathrm{ur}}$; as the units of its valuation ring are $\ell^t$-th
   powers (Hensel), this holds iff $\ell^t\mid v_q(q_E)=n_q$". Sure: high (no mathematical error, only precision).

5. **Proposition prop:ns, hypothesis "without complex multiplication".** Problem (harmless): the proof does not use
   it. The list $\GL_2(\F_3)$, $N_{ns}(\F_3)$, $N_s(\F_3)$ follows from surjectivity of $\det\bar\rho_{E,3}=\chi_{-3}$, the
   irreducibility of $E[3]$ and the presence of complex conjugation (an element of determinant $-1$ and trace $0$),
   by pure group theory (Chapter 1, item 6.7), with no appeal to Zywina's classification, and the rest of the proof
   (Frobenius reciprocity, orbits on lines) is also CM-free. Fix: optional; either drop the hypothesis or note that
   it is not needed. Sure: high for the mathematics; whether the author wants the extra generality is a choice.

6. **Lemma lem:old (case $p\nmid\ell N$) and the proof of Lemma lem:h0: "$\bar\rho$ being irreducible".** Problem
   (minor gap): Chebotarev plus Brauer-Nesbitt give only $\bar\rho_h^{ss}\simeq\bar\rho^{ss}$ over a common finite field;
   to conclude $\bar\rho_h\simeq\bar\rho$ one needs $\bar\rho$ absolutely irreducible, and the equivalence "$\bar\rho\simeq
   \bar\rho\otimes\chi_{-3}$ iff induced from $\Q(\sqrt{-3})$ iff not absolutely irreducible there" is Clifford theory for an
   absolutely irreducible $\bar\rho$. Both are fine for $\bar\rho_{E,\ell}$ because irreducible implies absolutely
   irreducible in the presence of complex conjugation ($\ell$ odd). Fix: add "(hence absolutely irreducible, complex
   conjugation having distinct eigenvalues $\pm1$)" after "irreducible" in both places, and "over a common finite
   extension of $\F_\ell$" after "$\bar\rho_h\simeq\bar\rho$". Sure: high.
