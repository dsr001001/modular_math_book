# Chapter 05: Galois theory, finite and infinite (`ch:galois`, `chapters/ch05_galois.tex`)

Stage 1 line-up. Part II (Number fields and local fields). Target length 2,000 lines of LaTeX (card excluded),
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
  For an odd prime $q$ put $q^*=(-1)^{(q-1)/2}q$ and, **as in the paper**, $\chi_q:=\chi_{q^*}$ (the character
  of $\Q(\sqrt{q^*})$, "the quadratic character of conductor $q$"); $\chi_{-3}$ and $\chi_{-4}$ are the
  characters of $\Q(\sqrt{-3})$ and $\Q(i)$. Chapter 2 defines the same symbols as Dirichlet characters
  (Kronecker symbols); the two agree through $\chi_d(\Frob_p)=\bigl(\tfrac{d}{p}\bigr)$, proved in Chapter 6.
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
* **C7 (typography).** No em dash, no en dash, no `--`, ASCII source, `\ell` not a Unicode letter, labels
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
algebraic elements. *Proved here.* Lang V.1 (Propositions 1.4 to 1.6). Background.

**galois:algebraic-closure** (theorem). (a) Every field $F$ has an algebraic closure $\Fbar$: an algebraic
extension of $F$ which is algebraically closed; it is unique up to $F$-isomorphism (not up to unique
isomorphism). (b) If $L/F$ is algebraic and $\sigma\colon F\to\Omega$ is an embedding into an algebraically
closed field $\Omega$, then $\sigma$ extends to an embedding $L\to\Omega$. (c) $\Qbar=\{z\in\C: z$ algebraic over
$\Q\}$ is an algebraic closure of $\Q$; it is countable, and $\C$ is not algebraic over $\Q$.
*Stated; reference* for (a) and (b) (Zorn's lemma argument sketched in one paragraph); (c) proved here from
the fundamental theorem of algebra (assumed from complex analysis). Lang V.2 (Theorems 2.5, 2.8);
Dummit-Foote 13.4. Background: $\Qbar$ and $G_\Q$ throughout the paper.

### Section 2. Splitting fields, normality, separability

**galois:splitting-field** (theorem). Let $f\in F[x]$ be nonconstant. A splitting field of $f$ over $F$ is an
extension $L=F(r_1,\dots,r_n)$ with $f=c\prod(x-r_i)$ in $L[x]$. (a) A splitting field exists, of degree
dividing $n!$ ... at most $n!$ over $F$. (b) *Extension of isomorphisms:* if $\phi\colon F\to F'$ is a field
isomorphism, $L$ a splitting field of $f$ over $F$ and $L'$ a splitting field of $\phi(f)$ over $F'$, then
$\phi$ extends to an isomorphism $L\to L'$; the number of such extensions is at most $[L:F]$, with equality
if $f$ is separable. (c) In particular any two splitting fields of $f$ over $F$ are $F$-isomorphic, and the
splitting field of $f$ inside a fixed $\Fbar$ is unique. The same holds for a family of polynomials (splitting
field of a set $S\subset F[x]$). *Proved here* ((a), (b), (c) for one polynomial; the family case sketched).
Lang V.3 (Theorem 3.3); Dummit-Foote 13.4 (Theorems 25, 27). Background.

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
Lang VI.1 (Theorem 1.8); Dummit-Foote 14.2 (Theorems 9, 13). Background.

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
Lang VI.1 (Theorem 1.12, Theorem 1.14); Dummit-Foote 14.4 (Proposition 19, 21). Background: restriction of
representations of $G_F$ to $G_K$; "unramified base change does not change inertia" in Chapter 7.
