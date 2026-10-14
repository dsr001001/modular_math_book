# Master plan: a modular textbook leading to "Local factors of the adjoint L-function and the l-adic valuations of the modular degree"

This file is the single source of truth for everyone (human or agent) writing a chapter.
Read all of it before writing anything.

## 1. Goal

The target text is the research note

> D. Soni, *Local factors of the adjoint L-function and the l-adic valuations of the modular degree* (version of 10 October 2026).

It proves, for an X_0(N)-optimal elliptic curve E/Q and an odd prime l not dividing 2N such that the mod l
representation is absolutely irreducible over Q(sqrt(l*)), the inequality

    v_l(deg phi_E)  >=  sum_{q | N} e_l(E,q) + sum_{q | N} t_l(E,q),

where e_l(E,q) is the l-adic valuation of the Euler factor at s = 1 of the adjoint L-function that the naive
adjoint L-function omits (nonzero only at additive primes, read off the Kodaira type for tame q >= 5) and
t_l(E,q) is the l-part of the valuation of the Tate parameter at a potentially multiplicative prime. The proof
assembles: the theorem of Diamond, Flach and Guo (DFG04) on the length of the Sigma-imprimitive adjoint
Selmer group and the congruence ideal; their formula for the variation of the congruence ideal with Sigma;
the local Tamagawa formula of Fontaine and Perrin-Riou; a computation of the Tamagawa factor of the adjoint
at a multiplicative prime; the comparison of the modular degree with the congruence number (Agashe, Ribet,
Stein); the commutative algebra of Wiles's numerical criterion (DDT Lemma 4.17); and Ribet-type level
lowering plus quadratic twisting. It also identifies the boundary of the hypothesis (mod 3 image the
normaliser of a split Cartan subgroup), states conjectures beyond the hypotheses, and reports large
computations on Cremona's tables with a pre-registered protocol.

The book must take a reader from the stated background to the point where every statement, every proof and
every table of the paper can be read with understanding, and it must serve as a *refresher* for experts: a
specialist who has forgotten the exact form of, say, the Fontaine-Perrin-Riou Tamagawa factor or the
Atkin-Li twisting theorem opens the relevant chapter and finds the precise statement at the top.

## 2. Audience and assumed background

The reader has done:

* a first course in real analysis (sequences, series, continuity, differentiation, Riemann integration,
  uniform convergence, metric spaces at an elementary level);
* a first course in linear algebra (vector spaces over R and C, matrices, determinants, eigenvalues,
  diagonalisation, inner products, Jordan form at most as a statement);
* an introduction to complex analysis (holomorphic functions, Cauchy's theorem, residues, Laurent series,
  Mobius transformations at an elementary level);
* basic statistics (means, variances, distributions, hypothesis tests at an elementary level);
* Riley, Hobson and Bence, *Mathematical Methods for Physics and Engineering* (so: Fourier series and
  transforms, ordinary and partial differential equations, special functions, tensors, elementary group
  theory and representation theory of finite groups, elementary probability).

The reader has NOT done: abstract algebra beyond what RHB contains, Galois theory, algebraic number theory,
topology, algebraic geometry, homological algebra, modular forms, p-adic numbers, or any Galois cohomology.
Every one of these is built from scratch, with proofs where they are short enough to be instructive and
precise statements with references where they are not.

Two reading modes must both work:

1. **Linear mode.** Chapters are in dependency order; a reader with the background above can read from
   Chapter 1 to Chapter 22.
2. **Refresher mode.** Each chapter opens with a *Core results at a glance* card: a numbered list of the
   definitions, theorems, lemmas and constructions of the chapter, each stated precisely (not summarised),
   each pointing to where in the chapter it is proved or discussed. An expert reads the card and stops.

## 3. Design principles

* **Modular.** One chapter = one LaTeX file = one topic that can be read on its own given the card of the
  earlier chapters. Chapters never `\input` other chapters. Cross-chapter references are by chapter label
  only (`\Cref{ch:slug}`), never by theorem number of another chapter, because chapters are written
  independently and in parallel.
* **Paper-driven.** Every chapter has a section *Where the paper uses this chapter* that names the exact
  lemmas, theorems, remarks, definitions or sections of the paper that depend on the chapter, and says which
  result of the chapter they use. Nothing is included that the paper does not need, directly or as a
  prerequisite of something it needs, except where a small amount of context makes a definition natural.
* **Three levels of rigour, always declared.** Each result in the card is marked
  *(proved here)*, *(proof sketched here)* or *(stated; reference)*. Elementary results (everything in
  Parts I and II, most of Part III, the commutative algebra of Part VI) are proved. Deep theorems
  (modularity, Serre's conjecture, level lowering, the DFG theorems, the Fontaine-Perrin-Riou formula,
  Tate local duality, Poitou-Tate) are stated precisely with their hypotheses, the shape of the proof is
  explained, and a standard reference with chapter or theorem number is given.
* **Precise statements over coverage.** A card entry that is wrong is worse than one that is missing.
  Standard references are cited with theorem numbers only when the writer is sure of the number; otherwise
  cite the chapter or section.
* **Worked examples from the paper.** The curves 11a1, 20a1, 121a1, 121c, 121d, 539c1, 980i1, 726a1 and 99A1
  (Cremona labels) appear in the paper; use them as running examples where the chapter's topic allows.
* **Exercises.** Each chapter ends with 8 to 20 exercises, graded, some of them "check the paper's claim
  that ..." exercises.
* **The physics reader.** Where a construction has an RHB-style analogue (representations of finite groups,
  Fourier expansions, lattices, periods), say so in one sentence; do not belabour it.

## 4. Table of contents

Labels `ch:slug` are fixed and must be used exactly. File names are `chapters/chNN_slug.tex`.

### Part I. Algebra

**Chapter 1. Groups, group actions and matrix groups over finite fields** (`ch:groups`, `ch01_groups.tex`)
Scope: groups, subgroups, cosets, normal subgroups, quotients, homomorphism theorems, cyclic groups, direct
and semidirect products, group actions, orbits and stabilisers, orbit-stabiliser, Sylow theorems (statement
and the use for small groups), p-groups, the quaternion group Q_8, dihedral groups, finite abelian groups
(structure theorem), profinite groups as inverse limits (definition, Z_p and the Galois groups to come).
Matrix groups: GL_2(F), SL_2(F), PGL_2, PSL_2 over a field, orders over F_q, Borel subgroups, split and
nonsplit Cartan subgroups and their normalisers, unipotent elements, the action on the projective line
P^1(F_q) (lines in F_q^2), orbits of subgroups on lines. Full detail for GL_2(F_3) (order 48): its
subgroups SL_2(F_3) (order 24), Q_8, the normalisers N_s(F_3) (order 8, dihedral) and N_ns(F_3) (order 16,
semidihedral), the determinant-one subgroups of each (SL_2(F_3), C_4, Q_8), elements of determinant -1 and
trace 0, orbits of N_s(F_3) on the four lines of F_3^2 (two orbits of size two) versus transitivity of
N_ns(F_3) and GL_2(F_3). Also GL_2(F_5), GL_2(F_7) orders and the maximal subgroup types in general
(Dickson's classification, statement).
Paper hooks: Proposition prop:ns (images at l = 3, determinant-one subgroups, orbits on lines, the 3-division
polynomial factorisation), Lemma lem:IV (unipotent image of inertia), Remark rem:types, Section
sec:anomaly (image 3Ns), the Eisenstein case (Borel image), Lemma lem:h0.

**Chapter 2. Rings, fields, polynomials and characters** (`ch:rings`, `ch02_rings.tex`)
Scope: rings, ideals, quotient rings, prime and maximal ideals, integral domains, fields of fractions, PIDs,
UFDs, Euclidean domains, polynomial rings, Gauss's lemma, irreducibility criteria (Eisenstein, reduction mod
p), Z/nZ and the Chinese remainder theorem, units (Z/nZ)^x, primitive roots, finite fields F_q (existence,
uniqueness, Frobenius automorphism, subfields, multiplicative group cyclic), the l-th powers in F_q^x and
the index [F_q^x : (F_q^x)^{l^k}] = l^{min(k, v_l(q-1))}, quadratic residues, the Legendre, Jacobi and
Kronecker symbols, quadratic reciprocity (with proof via Gauss sums or Eisenstein's lemma), the characters
chi_{-3}, chi_{-4}, chi_q (q odd) = (q*/.) with q* = (-1)^{(q-1)/2} q, their conductors and the values at
primes (chi_{-3}(p) = 1 iff p = 1 mod 3; chi_{-4}(p) = 1 iff p = 1 mod 4), Dirichlet characters, their
conductors, primitive characters, orthogonality, Gauss sums (basic properties), the ring Z[zeta_3] and
Z[i] as Euclidean domains, roots of unity, cyclotomic polynomials, valuations v_p on Q and the p-adic
absolute value (definition only; completions in Chapter 7), l-adic valuation of integers and of rationals
such as (q-1)/q, (q+1)^2 - a^2, 1 - q^{-2}.
Paper hooks: Definition def:terms (valuations of rationals), the table of Section 1 (chi_{-3}, chi_{-4}),
Lemma lem:euler, Lemma lem:tamfactor (l-th powers in F_q^x, the class c of the unit part), Lemma lem:twist
(q* and chi_q), Lemma lem:crit (cyclic groups Z/r).

**Chapter 3. Modules and commutative algebra** (`ch:modules`, `ch03_modules.tex`)
Scope: modules over commutative rings, submodules, quotients, homomorphisms, exact sequences, the snake
lemma, Hom and tensor product (definitions, universal properties, right exactness, flatness of localisation),
direct sums and products, free and projective modules, finitely generated modules over a PID (structure
theorem; elementary divisors), torsion and torsion-free, the lattice/saturation notion (a submodule L of a
free module M is saturated if M/L is torsion-free), Nakayama's lemma, localisation at a prime and at a
maximal ideal, local rings, discrete valuation rings (definition, uniformiser, valuation, ideals are
powers of the maximal ideal), completions and the rings Z_l, Q_l, Q_l/Z_l, the length of a module over a
DVR and over a local ring, Fitting ideals (definition via presentations, the case of a finitely generated
module over a DVR: Fitt = l^{length}, Fitting ideal of a direct sum, of a quotient), the annihilator,
Pontryagin duality for finite abelian groups and for the pair (Z_l-modules of finite type, discrete torsion
Z_l-modules) via Hom(-, Q_l/Z_l), the duality between T and T tensor Q_l/Z_l, perfect bilinear pairings
and the Gram determinant (its valuation is independent of basis; for a saturated sublattice L of rank d, the
cokernel of L -> Hom(L, O) has order #O/(Gram det)), alternating pairings, adjoints with respect to a
pairing, finite free algebras over a DVR (finite flat), their maximal ideals and localisation (T tensor Z_l
is a product of local rings, idempotents), generalised eigenspaces of commuting operators, semisimple versus
non-semisimple operators, Gorenstein rings (definition: finite free O-algebra T with Hom_O(T, O) free of rank
one over T; statement that Gorenstein plus a perfect self-adjoint pairing gives freeness results), the
inequality half of Wiles's numerical criterion in its abstract form (the paper's Lemma lem:ddt417 is proved in
full in Chapter 20; here prepare every ingredient: Ann, L[p], saturation, Gram determinant, the dual map).
Paper hooks: Tamagawa factor as a Fitting ideal (Section 1.2, Lemma lem:tamfactor, Lemma lem:fpr), lengths of
Selmer groups (Theorem thm:main), Lemma lem:ddt417, Lemma lem:hecke, Remark rem:free (freeness, Gorenstein),
Lemma lem:crit (T/(I+J)), Lemma lem:h0 (Q_l/Z_l-modules, l^k-torsion), Pontryagin duals in Lemma lem:dfg21,
the proof of Theorem thm:quant Step 1 (idempotents of T_l, generalised eigenspaces).

**Chapter 4. Representations of finite groups and the mod l world** (`ch:reps`, `ch04_reps.tex`)
Scope: representations of a finite group over a field (any characteristic), subrepresentations,
irreducibility, absolute irreducibility (irreducible after extending scalars to the algebraic closure),
Schur's lemma in both forms, characters and the character table in characteristic zero (brief, with the
RHB connection), Maschke's theorem and its failure in characteristic dividing the group order, semisimple
versus non-semisimple modules, the Jordan-Holder theorem and composition factors, the Brauer-Nesbitt
theorem (two semisimple representations with the same characteristic polynomials of all elements are
isomorphic; in characteristic l, the char polys not just traces), restriction and induction, Frobenius
reciprocity, Mackey's criterion for irreducibility of induced representations, Clifford theory for a
subgroup of index 2 (the restriction of an irreducible is irreducible or splits into two conjugate
characters; rho is isomorphic to rho tensor the sign character iff rho is induced from the index-2
subgroup), twisting by one-dimensional characters, the trace of an isomorphism rho -> rho tensor chi is
zero when chi is nontrivial, the adjoint representation ad(rho) = End(V) with trace-zero part ad^0, the
symmetric square and the identity ad^0 rho = Sym^2 rho tensor det^{-1} for two-dimensional rho, Hom_G(V, W)
= (V^* tensor W)^G, H^0 of ad^0 rho tensor chi as Hom(rho, rho tensor chi) with trace zero, representations
of GL_2(F_3) and its subgroups on F_3^2 and on F_9^2 (the determinant-one subgroup C_4 of N_s(F_3) acts
reducibly over F_9 as psi + psi^{-1} with psi of order 4, so N_s(F_3) acts as Ind psi), unipotent and
"minus unipotent" elements and their fixed spaces, the representation theory needed for images of inertia
(cyclic groups of order 2, 3, 4, 6 acting on a rank-two lattice over Z_l, eigenvalues roots of unity, the
module structure over Z_l[zeta_3]), representations over Z_l and lattices (a G-stable lattice in a
Q_l-representation, reduction mod l, homothetic lattices, Ribet's lemma stated: when the reduction is
irreducible all stable lattices are homothetic), irreducible versus absolutely irreducible for mod l
representations of Galois groups (foretaste), Dickson's list of subgroups of PGL_2(F_l) (statement).
Paper hooks: Proposition prop:ns (induced representations, psi of order 4, Frobenius reciprocity,
rho bar = rho bar tensor chi_{-3}), Lemma lem:h0 (trace-zero isomorphisms, ad rho bar tensor chi), Lemma
lem:IV and Lemma lem:euler (eigenvalues of inertia, Z_3[zeta_3]-module structure, invariants on the
adjoint), Lemma lem:old (Brauer-Nesbitt plus Chebotarev gives rho bar_h = rho bar), Section 4.2 (homothetic
lattices M_{f,lambda} and T_l E), the adjoint A_f = ad V and the trace form A_f(1) = Hom(A_f, Z_l(1)).

### Part II. Number fields and local fields

**Chapter 5. Galois theory, finite and infinite** (`ch:galois`, `ch05_galois.tex`)
Scope: field extensions, degree, algebraic and transcendental elements, minimal polynomials, splitting
fields, separability, normal extensions, Galois extensions, the Galois group, the fundamental theorem of
Galois theory, examples (quadratic fields, Q(zeta_n) with Galois group (Z/n)^x, Q(cube root of 2, zeta_3)),
Kummer theory for cyclic extensions of degree n when zeta_n is in the base field (and the mod n version:
F^x/(F^x)^n classifies Z/n-extensions), Artin-Schreier (statement), the Galois group of a polynomial and its
action on roots, the discriminant and transitivity, cubic and quartic polynomials (the factorisation pattern
of a quartic with Galois group a subgroup of GL_2(F_3) acting on lines, as used for the 3-division
polynomial), infinite Galois extensions and the Krull topology, profinite groups, the absolute Galois group
G_Q = Gal(Qbar/Q) and G_K, continuous characters and representations of profinite groups, Frobenius elements
(definition deferred to Chapter 6 but foreshadowed), the Chebotarev density theorem (statement, with the
corollaries used: a Galois representation is determined up to semisimplification by the Frobenius
characteristic polynomials at a density-one set of primes; two newforms with a_p congruent for almost all p
have isomorphic residual semisimplifications), complex conjugation as an element of G_Q of order two, the
quadratic characters of G_Q and Q(sqrt(d)), Q(sqrt(l*)) as the quadratic subfield of Q(zeta_l),
restriction of representations to open subgroups.
Paper hooks: the hypothesis "absolutely irreducible on Gal(Qbar/Q(sqrt(l*)))", Proposition prop:ns,
Lemma lem:h0, Lemma lem:old (Chebotarev and Brauer-Nesbitt), Lemma lem:tamagawa-exp (Kummer theory:
l^t-th roots of the Tate parameter), Lemma lem:tamfactor (Kummer classes).

**Chapter 6. Algebraic number theory** (`ch:ant`, `ch06_ant.tex`)
Scope: number fields, rings of integers, integral closure, Dedekind domains and unique factorisation of
ideals, norms of ideals, the splitting of primes in extensions (e, f, g; efg = n), ramified, inert, split
primes, the discriminant and ramification, quadratic fields in full (splitting of p in Q(sqrt(d)) governed by
the Kronecker symbol; the quadratic character attached to Q(sqrt(d)) as a Dirichlet character), cyclotomic
fields (splitting of p in Q(zeta_n) governed by p mod n; Q(zeta_3) = Q(sqrt(-3)); Q(sqrt(l*)) inside
Q(zeta_l)), Galois extensions: decomposition groups, inertia groups, the Frobenius element Frob_P, its
conjugacy class, the Frobenius of an unramified prime in an abelian extension, the Artin map (statement of
the main theorems of class field theory over Q: Kronecker-Weber, and the correspondence between Dirichlet
characters and one-dimensional representations of G_Q), the class group and units (statements, examples),
the rings Z[zeta_3] and Z[i], primes above 3 in Q(zeta_3) (3 = -zeta_3^2 (1 - zeta_3)^2, so Z_3[zeta_3] is a
DVR with uniformiser pi = 1 - zeta_3, residue field F_3, pi^2 = -3 up to a unit), primes lambda above l in
the coefficient field of a newform, the reduction mod lambda, the density of primes and the Chebotarev
theorem in its number field form (Frobenius classes equidistribute), primes inert in Q(sqrt(l*)) and
complex multiplication by that field (a_p = 0 at inert primes).
Paper hooks: Lemma lem:IV (Z_3[zeta_3] as DVR), Lemma lem:euler (Frobenius centralises or inverts sigma
according to q mod 3; Z_l[zeta_3] = End_{I_q}(V)), Lemma lem:h0 (a_p = 0 at primes inert in Q(sqrt(l*))
forces CM), Lemma lem:crit and Lemma lem:old (rings of integers O of number fields, primes lambda | l),
the twist by Q(sqrt(q*)) (Section 1.4), the characters chi_{-3}, chi_{-4} of Q(sqrt(-3)) and Q(i).

**Chapter 7. Local fields** (`ch:local`, `ch07_local.tex`)
Scope: absolute values, completions, Q_p and Z_p (as completions and as inverse limits), p-adic expansions,
Hensel's lemma (two forms), the structure of Z_p^x and Q_p^x (Q_p^x = p^Z x mu_{p-1} x (1 + pZ_p); for odd
p, 1 + pZ_p = Z_p via log/exp), roots of unity in Q_p, the Teichmuller lift, squares and l-th powers in Q_p^x
(for l not p, x in Z_p^x is an l-th power iff its reduction is an l-th power in F_p^x), finite extensions of
Q_p: ramification index, residue degree, unramified extensions (one of each degree, cyclic, generated by
roots of unity of order prime to p, Galois group generated by Frobenius), totally ramified extensions,
tamely and wildly ramified extensions, the maximal unramified extension Q_p^ur, the inertia group I_p, the
wild inertia group P_p (pro-p), the tame quotient I_p/P_p = prod_{l not p} Z_l(1), the tame character t_l:
I_p -> Z_l(1) (via l^k-th roots of p, or of any uniformiser), the relation Frob^{-1} t Frob = t^{p^{-1}}
(equivalently Frob t Frob^{-1} = t^p) in Gal(Q_p^tame/Q_p), the absolute Galois group G_{Q_p} and its
filtration, Kummer theory over Q_p: H^1(G_{Q_p}, mu_{l^k}) = Q_p^x/(Q_p^x)^{l^k} (foreshadowing Chapter
17), the Kummer class of an element and its restriction to inertia (the restriction of the Kummer class of
u in Q_p^x to I_p is v_p(u) times the tame character), the unramified quadratic extension of Q_p, the ramified
quadratic extensions Q_p(sqrt(p*)) and their characters, the local behaviour of quadratic characters of
G_Q (chi_q is unramified at p not q, ramified at q), the Weil group W_{Q_p} and Weil-Deligne
representations (definition: (r, N) with r a representation of the Weil group and N nilpotent, Frob N
Frob^{-1} = p^{-1} N), the inertia invariants and the local L-factor and conductor of a Weil-Deligne
representation (definitions; the Artin conductor a(r) = codim V^{I} + Swan), special cases: unramified,
tamely ramified through a finite cyclic quotient, the special (Steinberg) representation sp(2) and its
unramified twists (conductor exponent 1), the twist of sp(2) by a ramified quadratic character (conductor
exponent 2), representations with finite image of inertia of order 2, 3, 4, 6 (conductor exponent 2 for
q >= 5).
Paper hooks: Lemma lem:tamagawa-exp (Tate curve over the unramified quadratic extension, l^t-th roots of u),
Lemma lem:tamfactor (tame character, Frob^{-1} t Frob = t^{q^{-1}}, Kummer class kappa, its restriction to
I being n times the tame character, Z_l(1)/(q-1)), Lemma lem:IV and Remark rem:types (tame inertia is
cyclic; wild at 2 and 3), Lemma lem:twist(iii) (unramified twist of Steinberg, ramified twist has conductor
exponent 2), Lemma lem:euler (eigenvalues of Frobenius on inertia invariants), Remark rem:wild.

### Part III. Curves and elliptic curves

**Chapter 8. Algebraic curves, function fields and Riemann surfaces** (`ch:curves`, `ch08_curves.tex`)
Scope: affine and projective space, varieties over a field, the projective plane and homogeneous
polynomials, smoothness and singular points, plane curves, the function field of a curve, points over
extensions and the Galois action on points, the genus (via Riemann-Roch; for smooth plane curves
(d-1)(d-2)/2), divisors, principal divisors, linear equivalence, the Picard group, Riemann-Roch (statement,
with the standard consequences: a genus-one curve with a rational point is a plane cubic), morphisms of
curves, the degree of a morphism (three equivalent descriptions: degree of the function field extension,
number of preimages of a general point, the pullback on divisors), separable and inseparable, ramification
of morphisms, the Riemann-Hurwitz formula, compact Riemann surfaces versus smooth projective curves over C
(statement of the equivalence), differentials, holomorphic differentials and the genus, the Jacobian of a
curve (definition as Pic^0, as a complex torus over C, as an abelian variety: statements), the Abel-Jacobi
map, the Tate module and the first cohomology of a curve (H^1(X, Z) for the Riemann surface; its rank 2g;
the intersection pairing / cup product; H^1(X, Z_l) as H^1(X, Z) tensor Z_l for the moment, with a remark on
etale cohomology and on the Tate module of the Jacobian being H^1 dual), the cup product pairing is perfect
and alternating on H^1(X, Z), correspondences on a curve and their action on H^1 and on the Jacobian, the
adjoint of a correspondence under the cup product is the transpose correspondence.
Paper hooks: the modular parametrisation X_0(N) -> E and its degree (Section 1), H^1(X_0(N), Z_l) with the
cup product pairing (Section 4.1, Lemma lem:hecke), J_0(N) and its torsion (Remark rem:free), Tate modules
of Jacobians.

**Chapter 9. Elliptic curves over fields** (`ch:ellcurves`, `ch09_ellcurves.tex`)
Scope: Weierstrass equations (general and short), the quantities b_2, b_4, b_6, b_8, c_4, c_6, Delta, j, the
discriminant and smoothness, changes of coordinates (u, r, s, t) and the transformation of c_4, c_6, Delta,
the group law (chord-tangent; associativity via Riemann-Roch or stated), the group of points over any
field, isogenies (definition, degree, separable isogenies and kernels, the dual isogeny, deg of
multiplication by m is m^2), the structure of E[m] (Z/m x Z/m when char does not divide m), division
polynomials (definition, degree (m^2 - 1)/2 for odd m, the 3-division polynomial of degree 4 and its roots
as the x-coordinates of the four lines of E[3]), the Weil pairing (statement; nondegenerate, alternating,
Galois-equivariant; so det of the Galois action on E[m] is the cyclotomic character), the Tate module
T_l E = lim E[l^n] (free Z_l-module of rank 2) and V_l E, the Galois action (definition of rho_{E,l} and
rho bar_{E,l} = action on E[l]), endomorphism rings (Z, an order in an imaginary quadratic field, or an
order in a quaternion algebra), complex multiplication (definition; CM curves over Q have j among the 13
values; a_p = 0 at primes inert in the CM field), elliptic curves over C (lattices, the Weierstrass
p-function, the uniformisation theorem, periods, the period lattice Lambda_E of a curve over Q and its area,
isomorphism classes = lattices up to homothety = points of the upper half plane modulo SL_2(Z)), elliptic
curves over finite fields (the Frobenius endomorphism, a_p = p + 1 - #E(F_p), the Hasse bound, the
characteristic polynomial X^2 - a_p X + p of Frobenius on T_l E, the eigenvalues alpha, beta with alpha
beta = p), the Mordell-Weil theorem (statement), rank and torsion, Mazur's theorem on torsion (statement),
isogenies over Q and isogeny classes (finite; Cremona's class labels), rational l-isogenies and reducibility
of E[l] (E[l] reducible iff E has a rational l-isogeny; rational l-torsion points; the structure
Z/3 + mu_3), quadratic twists (definition E^(d): y^2 = x^3 + d a_2 x^2 + d^2 a_4 x + d^3 a_6 for a model
y^2 = x^3 + ..., effect on c_4, c_6, Delta (d^2, d^3, d^6), same j, a_p(E^(d)) = chi_d(p) a_p(E) for p not
dividing 2d, rho_{E^(d), l} = rho_{E,l} tensor chi_d), the L-function L(E, s) (definition by Euler product,
with the local factors at bad primes; analytic continuation as a statement, see Chapter 19), the Cremona
and LMFDB labelling of curves (11a1, 121a1, 539c1, 980i1, 726a1, 99A1 explained).
Paper hooks: everything; in particular Lemma lem:twist(ii) (models and invariants of twists), Lemma lem:h0
(CM and a_p = 0), Proposition prop:ns (3-division polynomial), Definition def:terms (v_q(j)), the twist of
good reduction E' and a_q(E') in the table of Section 1, Conjecture conj:eis (torsion, isogeny class,
Z/3 + mu_3), Section 1.1 (V, T, rho, rho bar).

**Chapter 10. Elliptic curves over local fields: reduction, Kodaira types, Tate curves** (`ch:reduction`,
`ch10_reduction.tex`)
Scope: minimal Weierstrass models over Z_p (existence, uniqueness up to change of coordinates, criterion
v_p(Delta) < 12 or v_p(c_4) < 4 for p >= 5; Kraus's conditions at 2 and 3 as a remark), reduction mod p,
good, multiplicative (split and nonsplit) and additive reduction, the criterion via v_p(Delta) and
v_p(c_4), the reduction map on points and E_0(Q_p), E_1(Q_p), the formal group (statement of what is
needed: E_1 has no prime-to-p torsion), potentially good and potentially multiplicative reduction (criterion
v_p(j) >= 0 or < 0), the semistable reduction theorem, the Neron model (definition by the universal
property; existence as a statement; the special fibre, its identity component and the component group
Phi_p, a finite etale group scheme over F_p), the geometric component group Phi_p(F_p bar) and the
Tamagawa number c_p = #Phi_p(F_p), Kodaira symbols I_0, I_n, II, III, IV, I_0^*, I_n^*, IV^*, III^*, II^*
with the special fibres drawn, the orders of the geometric component groups (n; 1; 2; 3; 4; 4; 3; 2; 1)
and the structure (Z/n; trivial; Z/2; Z/3; (Z/2)^2; Z/4 or (Z/2)^2 according to the parity of n; Z/3;
Z/2; trivial), Tate's algorithm (full statement, with the steps; for p >= 5 the type is determined by
v_p(Delta) of a minimal model for potentially good reduction: 0, 2, 3, 4, 6, 8, 9, 10 for I_0, II, III,
IV, I_0^*, IV^*, III^*, II^*, and by v_p(Delta) = n or n + 6 for I_n and I_n^*), the cubic
T^3 + a_2 T^2 + a_4 T + a_6 criterion for I_0^* at odd p, the conductor exponent f_p (0, 1, 2 for good,
multiplicative, additive at p >= 5; Ogg's formula f_p = v_p(Delta) + 1 - m_p with m_p the number of
components; the wild part at 2 and 3 and the bounds f_2 <= 8, f_3 <= 5), the conductor N = prod p^{f_p},
the Tate curve (E_q: the curve with parameter q in Q_p^x, |q| < 1; the uniformisation Q_p bar^x/q^Z;
j(E_q) with v_p(j) = -v_p(q); every curve with split multiplicative reduction is a Tate curve, nonsplit
after the unramified quadratic extension; the Tate parameter of a curve with potentially multiplicative
reduction, v_p(q_E) = -v_p(j_E) = n for type I_n and for type I_n^* at odd p; the unit part u = q_E p^{-n}
and its class in F_p^x modulo l^k-th powers), the Galois module E_q[l^t] generated by mu_{l^t} and an
l^t-th root of q (statement here, representation-theoretic consequences in Chapter 11), Kraus's theorem on
the semistability defect: for p >= 5 and potentially good reduction the order of the image of inertia on
T_l E (l not p) is 12/gcd(v_p(Delta), 12) (so 1, 6, 4, 3, 2, 3, 4, 6 for the types I_0, II, III, IV, I_0^*,
IV^*, III^*, II^*), the effect of quadratic twists on reduction (the paper's Lemma lem:twist (i) and (ii)
proved in full: unramified twists change nothing; the twist by Q(sqrt(q*)) at an odd q exchanges I_n and
I_n^*, I_0 and I_0^*, and for q >= 5 exchanges II and IV^*, III and III^*, IV and II^*; v_q(Delta) goes up
by 6 modulo 12), the wild primes 2 and 3 (what changes: the Kodaira type no longer determines the inertia
action; a type I_n^* at 2 may have potentially good reduction; the paper's Remark rem:wild), Cremona's
tables: what is tabulated (Kodaira symbols, c_p, Delta, conductor), PARI's Kodaira codes (n + 4 for I_n,
-(n + 4) for I_n^*, +-2, +-3, +-4 for II/II^*, III/III^*, IV/IV^*, -1 for I_0^*).
Paper hooks: Definition def:terms (t_l(E,q), v_q(j_E), potentially multiplicative primes), the table of
Section 1, Section 1.4 (component groups, the exchange of types, the weight w_l), Lemma lem:twist, Lemma
lem:tamagawa-exp (Tate curve over the unramified quadratic extension), Lemma lem:tamfactor (Tate parameter,
unit part), Lemma lem:IV and Remark rem:types (Kraus's defect), Remark rem:wild, Proposition prop:forms,
Section sec:wild, the appendix (Kodaira codes).

**Chapter 11. Galois representations of elliptic curves** (`ch:galrep`, `ch11_galrep.tex`)
Scope: rho_{E,l}: G_Q -> Aut(T_l E) = GL_2(Z_l) and rho bar_{E,l}: G_Q -> GL_2(F_l), continuity,
det rho_{E,l} = chi_l the l-adic cyclotomic character (via the Weil pairing), det rho bar_{E,3} = chi_{-3}
cuts out Q(sqrt(-3)), complex conjugation has determinant -1 and trace 0, the criterion of Neron, Ogg and
Shafarevich (rho_{E,l} unramified at p not l iff good reduction at p; potentially good iff the image of
inertia is finite), the local representation at a prime of good reduction (unramified, Frobenius char poly
X^2 - a_p X + p), at a prime of multiplicative reduction (the Tate curve: rho|_{G_{Q_p}} is an extension of
an unramified character eps of order <= 2 by eps chi_l, the matrix form with the Kummer class kappa of the
Tate parameter in the corner, non-split; the paper's Lemma lem:tamagawa-exp proved in full: rho mod l^t
unramified at p iff l^t | n_p, split or nonsplit; DDT Theorem 3.1(e)), at a prime of additive potentially
good reduction with p >= 5 (image of inertia cyclic of order 2, 3, 4 or 6 by Kraus; eigenvalues roots of
unity of that order; the paper's Lemma lem:IV in full: for types IV and IV^* the image of I_q in Aut(T_3 E)
is cyclic of order 3, acting on E[3] as a nontrivial unipotent, E[3]^{I_q} a line, tame, Serre conductor
exponent 1; and Remark rem:types: for II, II^* the image mod 3 is minus a unipotent, for I_n^* a ramified
quadratic character times a unipotent, for I_0^*, III, III^* of order 2 or 4, with E[3]^{I_q} = 0 and Serre
conductor exponent 2 in the II/II^*/I_n^* cases), at a prime of potentially multiplicative additive
reduction (rho = rho' tensor chi_q with rho' from the twist of multiplicative reduction), at l (the
representation is crystalline/comes from a finite flat group scheme when E has good reduction at l; the
Deligne-Fontaine description of rho bar|_{D_l} for weight 2 and level prime to l: either irreducible,
"fundamental characters of level 2", and then a_l = 0 mod l, or reducible with an unramified quotient on
which Frobenius acts by the unit root, so a_l mod l is determined by rho bar|_{D_l}; statements with
reference to Edixhoven), the Artin conductor of rho bar and the Serre conductor N(rho bar) (definition:
prod p^{dim rho bar - dim rho bar^{I_p} + Swan}; N(rho bar_{E,l}) divides the conductor of E (Carayol);
N(rho bar) is prime to every prime where rho bar is unramified), the images of rho bar_{E,l}: Serre's open
image theorem (statement), the classification of possible images for E/Q without CM (Zywina's lists for
l = 3, 5, 7, 11, 13; for l = 3: GL_2(F_3), N_s(F_3), N_ns(F_3), Borel subgroups and their subgroups; the
Sutherland labels 3B, 3B.1.1, 3Cs.1.1, 3Ns, 3Nn, 3Cs, 3Cn and what each means), reducible representations
and rational isogenies (the Eisenstein case; Z/3 + mu_3 as the image 3Cs.1.1), irreducible versus absolutely
irreducible for rho bar_{E,l} (with complex conjugation present, irreducible over F_l implies absolutely
irreducible: because the image contains an element with distinct eigenvalues 1 and -1 for l odd; explain
carefully), absolute irreducibility restricted to Gal(Qbar/Q(sqrt(l*))) and the dihedral/induced case: the
paper's Proposition prop:ns proved in full (for l = 3: the image is N_s(F_3) iff rho bar is induced from
Q(sqrt(-3)) iff rho bar = rho bar tensor chi_{-3} iff the 3-division polynomial factors as two irreducible
quadratics), the paper's Lemma lem:h0 proved in full (H^0(Q, ad rho bar tensor chi_l bar) nonzero iff
rho bar = rho bar tensor chi_l bar, which forces l = 3; the length h_l(E) of H^0(Q, ad T(1) tensor
Q_l/Z_l) as the largest k with rho mod l^k = (rho tensor chi_l) mod l^k; finiteness for non-CM curves
via a_p = 0 at inert primes), the semisimplification and Brauer-Nesbitt applied to rho bar_{E,l} (the
isomorphism class of an irreducible rho bar_{E,l} is determined by the a_p mod l for p in a density-one
set), Serre's conjecture for rho bar_{E,l} (statement: it comes from a newform of weight 2 and level
N(rho bar) when E has good reduction at l; this is the optimal-level theorem used in the paper; the general
statement is in Chapter 15), the Galois representation of a quadratic twist, the computation of mod l
images in practice (division polynomials, Sutherland's algorithm; statement).
Paper hooks: Section 1.1 (V, T, rho, rho bar, A_f = ad V, delta_p = dim V^{I_p}), Theorem thm:main
hypothesis, Lemma lem:tamagawa-exp, Lemma lem:IV, Remark rem:types, Lemma lem:euler (inertia images and
invariants), Lemma lem:old (the local analysis at p = l, at p || N ramified or unramified), the
optimal-level theorem paragraph of Section 3, Proposition prop:ns, Lemma lem:h0, Section sec:anomaly, the
Eisenstein case (Section sec:eis), Conjecture conj:eis.

### Part IV. Modular forms and modular curves

**Chapter 12. Modular forms and modular curves** (`ch:modforms`, `ch12_modforms.tex`)
Scope: the upper half plane and the action of SL_2(R) and of SL_2(Z), the modular group, fundamental
domains, the congruence subgroups Gamma_0(N), Gamma_1(N), Gamma(N) and their indices, cusps and their
widths, elliptic points, the modular curves Y_0(N) and X_0(N) as Riemann surfaces (compactification by
cusps, the genus formula for X_0(N), tables of small genera: X_0(11) has genus 1), modular forms and cusp
forms of weight k for Gamma_0(N) (definitions: holomorphy at the cusps via q-expansions), the spaces
M_k(Gamma_0(N)) and S_k(Gamma_0(N)), q-expansions and the q-expansion principle, Eisenstein series (brief),
the valence formula and dimension formulas (dim S_2(Gamma_0(N)) = genus of X_0(N)), weight 2 cusp forms as
holomorphic differentials on X_0(N) (f(z) dz), Fourier coefficients and the Ramanujan-Petersson bound
(statement), the Petersson inner product on S_k (definition, positive definite), the Sturm bound and
integrality (forms with integer coefficients, S_2(Gamma_0(N); Z), S_2(Gamma_0(N); Z_l)), modular forms with
character (nebentypus) briefly, the Atkin-Lehner involutions w_d and w_N (definition, action on
q-expansions is not simple, action on cusps), the modular curve X_0(N) as a moduli space (pairs (E, C) with
C cyclic of order N; the cusps as degenerate pairs; the Q-structure of X_0(N) as a statement, with
reference), examples: S_2(Gamma_0(11)) is one-dimensional spanned by eta(z)^2 eta(11 z)^2, the form of
11a1; the first coefficients of f_{11a1}; physics aside: Fourier series on a quotient.
Paper hooks: S_2(Gamma_0(N)), the newform f, q-expansions and congruences coefficientwise (Section 1,
Lemma lem:crit), integral forms S_2(Gamma_0(N); Z) (Lemma lem:crit), the Petersson norm <f, f> (Section 1,
Zagier, Watkins), the Atkin-Lehner involution w_N (Section 4.1, the pairing delta hat), X_0(N) as a curve
(Section 1), the genus and dim S_2 (background to multiplicity one).

**Chapter 13. Hecke operators, newforms and twists** (`ch:hecke`, `ch13_hecke.tex`)
Scope: the Hecke operators T_n on M_k(Gamma_0(N)) via double cosets and via the explicit formula on
q-expansions (a_n(T_p f) = a_{pn}(f) + p^{k-1} a_{n/p}(f) for p not dividing N; U_p for p | N:
a_n(U_p f) = a_{pn}(f)), commutativity, multiplicativity (T_{mn} = T_m T_n for coprime m, n;
T_{p^{k+1}} = T_p T_{p^k} - p^{k-1} T_{p^{k-1}}), the Hecke algebra T = Z[T_n : n >= 1] inside End(S_2)
(finite free over Z; of rank dim S_2 when acting faithfully, including the U_p), self-adjointness of T_n
for p not dividing N with respect to the Petersson product and the non-self-adjointness of U_p, eigenforms
and normalised eigenforms (a_1 = 1, then T_n f = a_n f), the eigencharacter phi_f: T -> Z or O, the
coefficient field and its ring of integers, oldforms and newforms (the maps f(z) -> f(dz) for d | N/M; the
old subspace; the new subspace as its orthogonal complement; Atkin-Lehner theory: the new subspace has a
basis of newforms which are eigenforms for all T_n and U_p, with multiplicity one), the main theorem of
Atkin-Lehner (strong multiplicity one: a newform is determined by a_p for p in any set of density one;
two newforms of the same level with the same T_p eigenvalues for almost all p are equal), eigenvalues of
U_p on oldforms (for h a newform of level M with p not dividing M, U_p on the span of h(z), h(pz) has
characteristic polynomial X^2 - a_p(h) X + p, the p-stabilisations h - beta h(pz) and h - alpha h(pz); on the
span of h(z), h(pz), h(p^2 z) the eigenvalue 0 appears with the depleted form h - a_p h(pz) + p h(p^2 z);
for p || M, U_p acts by a_p(h) on h and the depleted form h - a_p h(pz) has eigenvalue 0; for p^2 | M,
a_p(h) = 0 (Atkin-Lehner, Theorem 3) and U_p kills h), the non-semisimplicity of U_p when 0 is a repeated
eigenvalue, the Sigma-depleted form f^Sigma = sum_{(n, Sigma) = 1} a_n q^n, its level M^Sigma =
M prod_{p in Sigma} p^{delta_p} with delta_p = 2, 1, 0 for good, multiplicative, additive p (explain why),
the structure of S_2(Gamma_0(N)) tensor Qbar as a direct sum of the spans of h(dz) over newforms h of level
M | N and d | N/M, generalised eigenspaces of T and their relation to newforms, T tensor Q as a product of
fields times the old part, the orthogonal complement f^perp of a newform f and its T-stability, twisting by
Dirichlet characters (the Atkin-Li theorem (their Theorem 3.1, in the form used by the paper): for a
newform g of level M and the quadratic character chi of conductor q with q^2 not dividing M, g tensor chi
is a newform of level lcm(M, q^2)), the twist map iota: h -> h tensor chi on the whole space and its
compatibility with Hecke operators T_p for p not dividing the conductor (iota intertwines T_p with chi(p)
T_p), the integral structure: S_2(Gamma_0(N); Z) is a lattice, the pairing S_2(Gamma_0(N); Z) x T -> Z,
(g, t) -> a_1(t g), is perfect (Ribet 1983 Theorem 2.2; Abbes-Ullmo Lemma 2.1; proved here via the
q-expansion principle or stated with the proof idea), consequences (T is free of rank dim S_2 over Z;
Hom(T, Z) = S_2(Z); a form is determined by its pairing with T), congruences between eigenforms modulo
primes lambda (a_n(f) = a_n(g) mod lambda for all n versus for all n prime to a set), the recursion for
a_{p^k} and multiplicativity, so that congruences at primes propagate to all n, the L-function of a
newform L(f, s) = sum a_n n^{-s} = prod (1 - a_p p^{-s} + p^{1-2s})^{-1} prod_{p | N} (1 - a_p p^{-s})^{-1},
its analytic continuation and functional equation (statement), the Rankin-Selberg method and the formula
<f, f> = (explicit factor) L(Sym^2 f, 2) (statement with the correct normalisation; the precise form in
Chapter 19).
Paper hooks: Lemma lem:crit (T, phi_f, I, J, f^perp, the perfect pairing, T/(I + J) cyclic of order r),
Lemma lem:old (oldforms, U_p eigenvalues, stabilisations, depleted forms, a_p = 0 for p^2 | M,
multiplicativity and the recursion), Lemma lem:twist(iii) (Atkin-Li), Theorem thm:twist (the twist map
iota, generalised eigenforms, g^perp -> f^perp), the proof of Theorem thm:quant Step 1 (strong multiplicity
one, stabilisations, U_q eigenvalue 0 with multiplicity one, idempotents), Section 4.1 (f^Sigma, M^Sigma,
delta_p), Section 1 (congruence number r_E, Petersson norm).

**Chapter 14. Modular curves over Q, Jacobians and the modular degree** (`ch:moddeg`, `ch14_moddeg.tex`)
Scope: X_0(N) as a smooth projective curve over Q (statement; its cusps; its points over Q), the Jacobian
J_0(N) (abelian variety over Q of dimension g; J_0(N)(C) = S_2(Gamma_0(N))^*/H_1(X_0(N), Z)), the Hecke
action on J_0(N) by correspondences (T_p as the correspondence (E, C) -> sum (E/D, (C + D)/D)), the
Eichler-Shimura relation T_p = Frob_p + Frob_p^* on J_0(N) mod p for p not dividing N (statement, with the
consequence a_p(f) = trace of Frobenius), the Hecke action on H^1(X_0(N), Z) and on H_1, the cup product
pairing on H^1(X_0(N), Z) (perfect, alternating), adjoints: the adjoint of T_n under the cup product is
w_N T_n w_N (equivalently T_n is self-adjoint for the pairing <x, w_N y>; proof or precise reference), so
the modified pairing <x, w_N y> is perfect, alternating, and all T_n and U_p are self-adjoint for it (this
is the pairing delta hat_! of DFG04 in weight 2 and trivial character), the Tate module T_l J_0(N) =
H_1(X_0(N), Z) tensor Z_l and H^1(X_0(N), Z_l) (dual; etale cohomology as a statement), the modularity
theorem (statement: every elliptic curve E/Q of conductor N has a newform f_E of weight 2 on Gamma_0(N) with
a_p(f_E) = a_p(E) for all p; history: Wiles, Taylor-Wiles, Breuil-Conrad-Diamond-Taylor), the abelian
variety A_f attached to a newform (quotient of J_0(N) by I_f J_0(N)), for rational f the elliptic curve
quotient, the modular parametrisation phi_E: X_0(N) -> E (sending the cusp infinity to O), the
X_0(N)-optimal curve (unique in its isogeny class; equivalently the kernel of J_0(N) -> E is connected;
also called the strong Weil curve; its relation to the Cremona label "1" is a convention that was checked
only up to conductor 400000 and for some classes beyond; the paper's statement about optimality in the
tables), the modular degree deg phi_E (definition as the degree of the morphism of curves; equivalently
via the composition E^vee -> J_0(N) -> E being multiplication by deg phi_E; properties: multiplicative
under nothing in particular, computability), the Manin constant (definition, the conjecture c = 1,
known results: Mazur: c | ... ; Abbes-Ullmo; Cremona's verification; the role of the Manin constant in
the formulas), the formula of Zagier and Watkins: deg phi_E = 4 pi^2 c^2 <f, f> / vol(Lambda_E), with phi^* omega_E = c 2 pi i f dz, up to the
precise normalisation (state the exact formula with the Manin constant; Zagier 1985, Watkins 2002), the
congruence number r_E (definition as in the paper: the largest r such that f = g mod r for some integral g
of level N orthogonal to f; the congruence ideal in T; Lemma lem:crit of the paper proved in full here or in
Chapter 20, see below), the theorem of Agashe, Ribet and Stein (deg phi_E | r_E, and v_p(deg phi_E) = v_p(r_E)
for p^2 not dividing N; the example 99A1 with deg = 4, r = 12; statement with proof idea: the modular degree
is the congruence number computed in the Hecke algebra of the Jacobian's quotient, and the two differ by a
factor controlled by the primes p with p^2 | N), multiplicity one and the Gorenstein property (the maximal
ideal m of T tensor Z_l attached to (f, l); J_0(N)[m] is two-dimensional when l does not divide 2N and
rho bar is irreducible: Mazur for prime level, Ribet-Stein Theorem 3.5 for J_1(N) with the exception of
Serre weight l, the pull-back J_0(N)[m] -> J_1(N)[m'] with kernel in the Shimura subgroup which is
Eisenstein; consequence (Tilouine): T_m is Gorenstein and T_l J_0(N)_m = H^1(X_0(N), Z_l)_m is free of
rank two over T_m; the paper's Remark rem:free), the Eisenstein ideal, the cuspidal subgroup and the Shimura
subgroup (definitions; Mazur's theorem for prime level; what "Eisenstein" means for a maximal ideal; why
reducible rho bar is the Eisenstein case), the parametrisations by Shimura curves and the theorem of Ribet
and Takahashi (statement: the ratio of the degrees of the parametrisations by X_0(N) and by the Shimura
curve of discriminant D is, up to primes where rho bar is reducible, the product of the c_q or n_q over
q | D; the precise statement), the abc connection (deg phi_E << N^{2 + epsilon} is equivalent to a form of
abc; statement with reference to ARS12 Section 2), Watkins's conjecture 2^{rank E(Q)} | deg phi_E and the
theorem of Calegari and Emerton on curves of odd modular degree (statements), Mazur's theorem on
J_0(N)(Q)_tors for prime N (statement), computing the modular degree (Watkins's method via the Petersson
norm; Cremona's method via the period lattice; PARI's ellmoddegree).
Paper hooks: the whole of Section 1 (optimal curve, modular degree, Petersson norm, Zagier, Watkins,
Agashe-Ribet-Stein, congruence number), Lemma lem:crit (congruence number and congruence ideal), Lemma
lem:hecke, Remark rem:free, Section 4.1 (H^1(X_0(N), Z_l), the pairing delta hat_!, Atkin-Lehner), the
remark after Theorem thm:qual (99A1), Section 1.5 (Ribet-Takahashi), Section sec:two (Watkins,
Calegari-Emerton), Conjecture conj:eis and Section sec:eis (Eisenstein ideal, cuspidal subgroup, Mazur),
Open question 4.

**Chapter 15. Galois representations of modular forms, level lowering and congruences** (`ch:modgalrep`,
`ch15_modgalrep.tex`)
Scope: the Galois representation rho_{f, lambda}: G_Q -> GL_2(O_lambda) attached to a newform f of weight
2 (Eichler-Shimura construction via the Tate module of A_f; Deligne for higher weight as a statement),
its properties: unramified outside N l, trace of Frob_p = a_p(f), det = chi_l, odd, irreducible; the
residual representation rho bar_{f, lambda} and its semisimplification; the comparison with rho_{E, l}
when f = f_E (they are isomorphic; the lattices T_l E and M_{f, lambda} are homothetic when rho bar is
irreducible, by Ribet's lemma on lattices), local-global compatibility (Carayol; Langlands-Deligne): the
restriction of rho_f to G_{Q_p} corresponds to the local component pi_p of f under the local Langlands
correspondence; the local components of a weight 2 newform of trivial character: unramified principal
series at p not dividing N (Frobenius eigenvalues alpha_p, beta_p), unramified twist of Steinberg at
p || N (rho|_{G_{Q_p}} is an extension of an unramified character eps by eps chi_l with eps(Frob_p) = a_p =
+-1; DDT Theorem 3.1(e)), and at p^2 | N either a ramified twist of Steinberg (then the twist of f by
the corresponding character has level with p exactly once, and a_p(f) = 0), or a ramified principal
series, or supercuspidal; in all cases with p^2 | N one has a_p(f) = 0 and V^{I_p} = 0 (dim V^{I_p} = delta_p
= 2, 1, 0), the conductor of rho_f equals N (Carayol), the Weil-Deligne representation at p and the local
L-factor and epsilon factor (definitions recalled from Chapter 7), the non-split extension at a
multiplicative prime has a unique stable line (used in Lemma lem:old), the local representation at l for
l not dividing N (crystalline, finite flat, weight 2: Fontaine-Laffaille range; the description of
rho bar|_{D_l} and the determination of a_l mod lambda from it (Deligne; Fontaine; Edixhoven Section 2):
if rho bar|_{D_l} is irreducible then a_l = 0 mod lambda; if reducible, rho bar|_{D_l} has an unramified
quotient on which Frobenius acts by a_l mod lambda), the Serre conductor and Serre weight of rho bar (the
weight is 2 for rho bar_{E,l} with good reduction at l), Serre's conjecture (statement; the strong form:
rho bar odd irreducible arises from a newform of weight k(rho bar) and level N(rho bar); the theorem of
Khare and Wintenberger; for the paper only the "optimal level" direction for a representation already known
to be modular is used), the optimal level theorem of Ribet, Carayol and Diamond in the form DDT Theorem
3.15: for l odd and rho bar irreducible and modular, absolutely irreducible on Gal(Qbar/Q(sqrt(-3))) if
l = 3, rho bar arises from a newform of weight 2 and level N(rho bar) l^{delta(rho bar)} with nebentypus of
order prime to l, delta = 0 when rho bar|_{D_l} is good; the specialisation to rho bar_{E', l} with l not
dividing the conductor: it arises from a newform of weight 2 on Gamma_0(N(rho bar)) (the paper's argument
that the nebentypus is trivial: det = chi_l bar forces a character trivial mod lambda of order prime to l),
Ribet's level-lowering theorem (the case q || N with rho bar unramified at q: rho bar arises from level N/q;
the original statement and proof idea via Shimura curves and the Ihara/Mazur principle), Mazur's principle,
Carayol's lemma, the level-raising theorem of Ribet (statement: rho bar arises from level N q (q not
dividing N l) iff a_q^2 = (q + 1)^2 mod lambda; the level-raising factor (1 - alpha/beta q^{-1})(1 - q^{-1})
(1 - beta/alpha q^{-1}) = (q - 1)((q + 1)^2 - a_q^2)/q^3 ... give the exact form used in the paper, namely
L_q^{nv}(A_f, 1)^{-1} = (1 - alpha/(beta q))(1 - 1/q)(1 - beta/(alpha q)) = ((q - 1)/q) ((q + 1)^2 -
a_q^2)/q^2), congruences between newforms: the congruence criterion (the paper's Lemma lem:crit; prove it
here in full with the perfect pairing from Chapter 13 and the algebra from Chapter 3, and cross-reference
Chapter 14 and Chapter 20), the oldform lemma (the paper's Lemma lem:old proved in full: given a newform h
of level M | N congruent to f at almost all primes, with p not dividing M for every p || N at which rho bar
is unramified, the span of the h(dz) contains an eigenform g for the full Hecke algebra, orthogonal to f,
congruent to f at ALL n; the prime-by-prime analysis: p not dividing l N, p = l, p^2 | N, p || N unramified,
p || N ramified), the proof of the paper's Theorem thm:qual (cases (a), (b), (c)) as a worked application,
including the examples 121a1, 539c1, 980i1 with the specific congruences, the results of Ribet-Takahashi,
Pollack-Weston and Kim-Ota on the congruence ideal and the Tamagawa exponent t_q (statements only, with
their hypotheses, as in the paper's Section 1.5 and Remark rem:ko), the Taylor-Wiles method and R = T
theorems (one-page outline: deformation rings, the numerical criterion, patching; precise statement of what
DFG04 Theorem 3.7 needs; details in Chapter 20).
Paper hooks: Sections 3 (all of it: Lemma lem:crit, Lemma lem:old, the optimal-level theorem, cases (a),
(b), (c), the example, the remark), Section 1.5 (history, Theorem thm:qual, Remark rem:ko), Section 4.2
(M_{f,lambda} homothetic to T_l E), Lemma lem:euler (local components: Steinberg and its twists), Lemma
lem:twist(iii), Theorem thm:twist and Theorem thm:quant (twist map, eigenforms, levels), Theorem thm:dfg14
(the level-raising factor), Remark after Theorem thm:quant.

### Part V. Cohomology, Selmer groups and L-functions

**Chapter 16. Homological algebra and group cohomology** (`ch:cohomology`, `ch16_cohomology.tex`)
Scope: chain complexes, cohomology of a complex, exact sequences of complexes and the long exact sequence
(with the connecting homomorphism constructed), the snake lemma, injective and projective resolutions and
derived functors in outline (Ext and Tor as statements; Ext^1 classifies extensions), group cohomology
H^n(G, M) for a group G and a G-module M (definition via the standard complex of inhomogeneous cochains;
H^0 = M^G; H^1 = crossed homomorphisms modulo principal ones; H^1(G, M) = Hom(G, M) when G acts trivially;
H^2 and extensions), functoriality in G and in M, the long exact sequence in M, restriction, corestriction,
inflation, the inflation-restriction exact sequence 0 -> H^1(G/H, M^H) -> H^1(G, M) -> H^1(H, M)^{G/H} ->
H^2(G/H, M^H), the conjugation action of G/H on H^1(H, M) (the formula (sigma . c)(h) = sigma c(sigma^{-1} h
sigma), and its independence of choices), the cohomology of a finite cyclic group (H^1(<t>, M) = ker(Norm)/
(t - 1)M, H^2 = M^G/Norm), the cohomology of Z and of Z_l (procyclic): H^1(<t>, M) = M/(t - 1)M for a
procyclic group acting continuously on a finitely generated Z_l-module (precise statement and proof),
continuous cohomology of profinite groups with discrete, finite, and compact (Z_l-module of finite type)
coefficients (definition as direct limits over open normal subgroups for discrete M; inverse limits for
compact M; the pitfalls), the cohomology of a pro-l group versus a group of order prime to l (H^i(G, M) = 0
for i > 0 when G is profinite of order prime to l and M is an l-primary torsion module or Z_l-module of
finite type; so cohomology of inertia factors through the maximal pro-l quotient when the coefficients are
l-adic), H^1(G, M)_{tors} and its Fitting ideal (compute H^1(<t>, M) = M/(t - 1)M for M = ad T with t acting
unipotently as in the paper: full worked example reproducing the computation (t - 1)e = 0, (t - 1)h = -2n' e,
(t - 1)f = n' h - n'^2 e, (t - 1)M = n'(Z_l e + Z_l h), H^1 = (Z_l/n')^2 + Z_l), cup products (definition on
cochains; H^1 x H^1 -> H^2; graded commutativity), Pontryagin duality for cohomology (statement), Tate
cohomology of finite groups (brief; H^1(G, M) is killed by #G, so H^1 of a group of order 2 is killed by
2, used for the real place), the Hochschild-Serre spectral sequence (statement; only the five-term exact
sequence is used), the cohomology of Z/2 acting on a Z_l-module for l odd (vanishes), Galois cohomology
as the special case G = G_K (notation H^i(K, M) = H^i(G_K, M); the next chapter).
Paper hooks: Lemma lem:tamfactor (every step: inflation-restriction, H^1(<t>, M) = M/(t - 1)M, the
conjugation action of G/I, the explicit (t - 1)M computation, the Fitting ideal of the invariants), Lemma
lem:dfg21 (Pontryagin duals, H^1(R, T^D) killed by 2), Lemma lem:h0 (H^0 of ad T(1) tensor Q_l/Z_l and its
l^k-torsion), the definition of Tam_p (Section 1.2), Lemma lem:fpr.

**Chapter 17. Galois cohomology, local and global, and Selmer groups** (`ch:galcoh`, `ch17_galcoh.tex`)
Scope: Galois cohomology of a field H^i(K, M) = H^i(G_K, M) with M a discrete G_K-module, Hilbert's theorem
90 (H^1(K, Kbar^x) = 0) and Kummer theory as H^1(K, mu_n) = K^x/(K^x)^n (proved), the Kummer map and the
Kummer class of an element, H^1(K, Z_l(1)) = lim K^x/(K^x)^{l^k} for a local field K (and the identification
of Z_l(1) = T_l mu = lim mu_{l^k}), the Brauer group and H^2(K, mu_n) (statement), local Galois cohomology
for K = Q_p: finiteness of H^i(Q_p, M) for finite M, the local Euler-Poincare characteristic formula
(statement), Tate local duality (H^i(Q_p, M) x H^{2 - i}(Q_p, M^*(1)) -> H^2(Q_p, mu) = Q/Z perfect;
statement with reference), unramified cohomology H^1_ur(Q_p, M) = H^1(G_{Q_p}/I_p, M^{I_p}) = ker(H^1(Q_p, M)
-> H^1(I_p, M)) (via inflation-restriction), H^1_ur(Q_p, M) = M^{I_p}/(Frob_p - 1) M^{I_p} (for M a
Z_l-module of finite type or a Q_l-vector space, by the procyclic computation), the annihilator of H^1_ur
under Tate duality is H^1_ur of the dual (for p not l, finite M of order prime to p), the cohomology of the
real place (H^1(R, M) is killed by 2; for l odd and M an l-adic module it vanishes), the cohomology of G_Q
and of G_{Q,S} (the Galois group of the maximal extension unramified outside S), finiteness of H^1(G_{Q,S},
M) for finite M (statement), the Kummer sequence for an elliptic curve 0 -> E[n] -> E -> E -> 0 and the
Kummer map E(K)/n E(K) -> H^1(K, E[n]), the classical n-Selmer group and the Shafarevich-Tate group
(definitions, the exact sequence 0 -> E(Q)/n -> Sel_n(E/Q) -> Sha[n] -> 0, finiteness of Sel_n, the weak
Mordell-Weil theorem as a consequence; this is the model for all Selmer groups), Selmer structures: a family
of local conditions L_p in H^1(Q_p, M) for all p, unramified at almost all p, and the Selmer group
H^1_L(Q, M); the dual Selmer structure L^* via local duality; the Greenberg-Wiles formula (the theorem of
Wiles on the ratio #H^1_L(Q, M)/#H^1_{L^*}(Q, M^*(1)) = #H^0(Q, M)/#H^0(Q, M^*(1)) times the product over
p of #L_p/#H^0(Q_p, M); statement with reference; this is the origin of the exact sequence of DFG04 Lemma
2.1), the Poitou-Tate exact sequence (statement), comparing Selmer groups for two sets of local
conditions: the exact sequence 0 -> H^1_L -> H^1_{L'} -> prod_p L'_p/L_p -> ... with the cokernel controlled
by the dual Selmer group (prove the elementary part; the paper's Lemma lem:dfg21 is this comparison with
L = Bloch-Kato conditions and L' = no conditions at Sigma, for which the dual term is H^0(Q, W^D)^* when
H^1_f(Q, V^D) = 0), the cohomology of Q_l/Z_l-modules versus Z_l-modules: the exact sequences relating
H^1(K, T), H^1(K, V), H^1(K, W) for T a lattice, V = T tensor Q_l, W = V/T (the divisible and torsion parts;
H^1(K, T)_{tors} = image of H^0(K, W) ... prove the needed cases), H^1(K, T)_tors and H^1(K, W) for K =
Q_p, p not l: H^1(Q_p, T) is finitely generated over Z_l with torsion H^0(Q_p, W)/(divisible) ... state
exactly what is true and used (the paper: for p in Sigma, H^1_f(Q_p, T^D) is the torsion of H^1(Q_p, T^D),
a finite group, because H^1_f(Q_p, V^D) = 0), the example of the Tate curve: H^1(Q_p, Z_l(1)) and the
Kummer class of the Tate parameter, with its image in H^1(G/I, Z_l(1)^I) = Z_l(1)/(q - 1) = Z/l^{v_l(q - 1)}
being the class of the unit part of the Tate parameter in F_p^x tensor Z_l (proved in full; this is the end
of the paper's Lemma lem:tamfactor).
Paper hooks: Lemma lem:tamagawa-exp and Lemma lem:tamfactor (Kummer theory, the class c' of the unit part,
H^1(G/I, Z_l(1)^I)), Lemma lem:dfg21 and the paragraph after it (H^1_f(Q_p, V^D) = H^1_ur = (V^D)^{I_p}/
(Frob_p - 1) vanishes because det(1 - Frob_p | (V^D)^{I_p}) = L_p(A_f, 1)^{-1} is nonzero; the torsion of
H^1(Q_p, T^D); H^1(R, T^D) killed by 2), Remark rem:ns (the exact sequence with H^0(Q, W^D) nonzero),
the Selmer groups of Theorem thm:main.

**Chapter 18. Bloch-Kato Selmer groups, Tamagawa factors and the adjoint motive** (`ch:blochkato`,
`ch18_blochkato.tex`)
Scope: l-adic representations of G_Q (continuous, on finite-dimensional Q_l-vector spaces), lattices T,
the divisible module W = V/T, Tate twists V(n) = V tensor Q_l(1)^{tensor n}, duals V^* = Hom(V, Q_l) and
the Cartier/Kummer dual V^D = V^*(1) = Hom(V, Q_l(1)), T^D = Hom(T, Z_l(1)), W^D = V^D/T^D, the trace form
on ad^0 V and the self-duality (ad^0 V)^* = ad^0 V, so A(1) = Hom(A, Z_l(1)) = T^D for A = ad^0 T when l is
odd (2 invertible), geometric representations and their local behaviour: at p not l, the Weil-Deligne
representation, the inertia invariants and the local L-factor L_p(V, s) = det(1 - Frob_p p^{-s} | V^{I_p})^{-1}
(definition; the Frobenius here is geometric or arithmetic: fix the convention and state the paper's
convention that a good prime has eigenvalues alpha/beta, 1, beta/alpha on ad V, hence L_p(A_f, s) with
s = 1 giving (1 - alpha/(beta p))(1 - 1/p)(1 - beta/(alpha p))), at l: de Rham, crystalline, semistable
representations (Fontaine's rings B_dR, B_cris, B_st as black boxes; definitions of D_cris and the crystalline
condition; the Tate module of an elliptic curve with good reduction at l is crystalline; the adjoint of a
crystalline representation is crystalline; statements only, with references to Fontaine, Berger's survey,
and DFG04 Section 2), the Bloch-Kato local conditions: H^1_f(Q_p, V) = H^1_ur(Q_p, V) = ker(H^1(Q_p, V) ->
H^1(I_p, V)) for p not l, H^1_f(Q_l, V) = ker(H^1(Q_l, V) -> H^1(Q_l, V tensor B_cris)), H^1_f(R, V) = 0,
H^1_g and H^1_e (definitions; for the paper only H^1_f matters), the Bloch-Kato conditions on T and on W:
H^1_f(Q_p, T) = preimage of H^1_f(Q_p, V) under H^1(Q_p, T) -> H^1(Q_p, V); H^1_f(Q_p, W) = image of
H^1_f(Q_p, V) under H^1(Q_p, V) -> H^1(Q_p, W), the global Bloch-Kato Selmer groups H^1_f(Q, V), H^1_f(Q, T),
H^1_f(Q, W), their relations, the Sigma-imprimitive Selmer group H^1_Sigma(Q, W) of DFG04 Section 2.1 (no
condition at p in Sigma, the Bloch-Kato condition at l, unramified elsewhere), the duality between the
Bloch-Kato conditions for V and V^D under Tate local duality (H^1_f(Q_p, V)^perp = H^1_f(Q_p, V^D) for p not l;
at l the same by Bloch-Kato; statements), the Fontaine-Perrin-Riou Tamagawa factor at p not l:
Tam_p(T) = Fitt_{Z_l}(H^1(I_p, T)_{tors})^{G_{Q_p}} ... state the definition precisely as the paper does
(the Fitting ideal of the G_{Q_p}-invariants of the torsion of H^1(I_p, T); FPR94 I.4.2.2; DFG04 p. 708),
the alternative description as [H^1_f(Q_p, T) : H^1_ur(Q_p, T)] type index or as the order of
H^1_f(Q_p, T)/(something) and the equivalence (Lemma lem:fpr of the paper: Fitt H^1_f(Q_p, T^D) =
L_p(V, 1)^{-1} (or the appropriate twist) times Tam_p(T^D), and Tam_p(T^D) = Tam_p(T): state and prove what
can be proved with the tools at hand, namely the finite group H^1_f(Q_p, T^D) = H^1(Q_p, T^D)_{tors} sits in
an exact sequence with H^0(Q_p, W^D) and the unramified part, whose orders are the Euler factor and the
Tamagawa factor; give the full argument for p not l, following FPR94 I.4 and the proof of DFG04 Theorem
2.15), the Tamagawa factor of an elliptic curve (Tam_p(T_l E) is the l-part of the Tamagawa number c_p =
#Phi_p(F_p), as a sanity check: this is the classical fact and the paper's final remark in the proof of
Lemma lem:tamfactor), the full computation of the paper's Lemma lem:tamfactor (Tam_q(ad T) at a prime of
multiplicative reduction: v_l = v_l(n) + min(v_l(n), v_l(q - 1), v_l(c)), proved in full, every step, using
Chapters 16 and 17; the consequence v_l(Tam_q(ad T)) >= t_l(E, q) with equality unless q = 1 mod l, l | n
and the unit part of the Tate parameter is an l-th power), the Tamagawa factor at an additive prime (what is
known: it is at least 0; the paper does not compute it; Open question 3), the Tamagawa factor at a prime
of good reduction is trivial, the Tamagawa number conjecture of Bloch and Kato (statement for a motive in
outline: the l-part of the special value of the L-function equals the product of the order of the Selmer
group, the Tamagawa factors, the periods and the orders of H^0 terms; the shape for the adjoint motive
of a modular form as in DFG04 Theorem 0.1: L(ad f, 1)/(period) has l-adic valuation equal to the length of
the Selmer group plus Tamagawa factors; precise statement of DFG04 Theorem 0.1 and Theorem 0.2 with the
hypothesis l not in S_f), the exact sequence of DFG04 Lemma 2.1 (the paper's Lemma lem:dfg21: statement,
hypotheses H^0(Q, V^D) = H^1_f(Q, V^D) = 0, the four terms, the Pontryagin duals; proof via the
Greenberg-Wiles / Poitou-Tate comparison of Chapter 17), DFG04 Theorem 2.7 (H^0(Q, V^D) = H^1_f(Q, V^D) = 0
for l not in S_f; statement; it is the vanishing of the adjoint Selmer group with Q_l coefficients, which
comes from Taylor-Wiles), H^0(Q, W^D) = H^0(Q, ad T(1) tensor Q_l/Z_l) and the paper's Lemma lem:h0 (restate
and connect; proved in Chapter 11), the corrected exact sequence of Remark rem:ns when H^0(Q, W^D) is
nonzero (length H^1_Sigma = length H^1_f + sum of local terms - h_l(E)), the adjoint motive of a modular
form and of an elliptic curve (ad^0 of the Tate module; its L-function L(ad f, s) = L(Sym^2 f, s + 1) in
the normalisation used; its Hodge numbers in one sentence; critical values; Flach's theorem that the
Selmer group of Sym^2 is finite), the symmetric square and the Petersson norm (connection, details in
Chapter 19).
Paper hooks: Section 1.2 (the definition of Tam_p(M), the Bloch-Kato Selmer group), Theorem thm:main and
its proof in Section 4.3 (every step of the assembly: Theorem thm:dfg37, Theorem thm:dfg27, Lemma lem:dfg21,
Lemma lem:fpr, Lemma lem:h0), Lemma lem:tamfactor (in full), Remark rem:ko(1), Remark rem:ns, Section sec:tam,
Open questions 2 and 3, Conjecture conj:euler (the term h_l(E)).

**Chapter 19. L-functions: Euler products, local factors, the adjoint and the symmetric square**
(`ch:lfunctions`, `ch19_lfunctions.tex`)
Scope: Dirichlet series and their convergence, Euler products, the Riemann zeta function (Euler product,
analytic continuation and functional equation stated with the proof idea via theta functions, the
physics-reader connection to Mellin transforms), Dirichlet L-functions (definition, Euler product, functional
equation stated, L(1, chi) nonzero and Dirichlet's theorem stated), the Dedekind zeta function of a number
field and its factorisation for abelian fields (statement), the L-function of an elliptic curve (local
factors: (1 - a_p p^{-s} + p^{1 - 2s})^{-1} at good p, (1 - a_p p^{-s})^{-1} at multiplicative p with
a_p = +-1, 1 at additive p; the conductor; the completed L-function Lambda(E, s) and the functional
equation with root number, as a consequence of modularity; L(E, s) = L(f_E, s)), L-functions of l-adic
Galois representations (the local factor L_p(V, s) = det(1 - Frob_p p^{-s} | V^{I_p})^{-1} for p not l;
at p = l via D_cris; the Weil-Deligne definition so that the factor is independent of l; the conjecture and
theorem (for modular forms) that these are compatible), the L-function of a representation with finite
image of inertia (examples: the three Kodaira cases), the adjoint and the symmetric square L-functions
(definitions: L(ad f, s) attached to ad^0 rho_f, L(Sym^2 f, s) attached to Sym^2 rho_f; the identity ad^0
rho = Sym^2 rho tensor det^{-1} and L(Sym^2 f, s) = L(ad f, s - 1) in the paper's normalisation, with care
about which normalisation each reference uses: Shimura, Gelbart-Jacquet, DFG04, PARI), the naive adjoint
L-function (the Euler product of sum a_n^2 n^{-s} after removing the zeta factor, i.e. the Rankin-Selberg
convolution L(f x f, s)/zeta^(N)(s - 1), where L(f x f, s) = zeta^(N)(2s - 2) sum a_n^2 n^{-s}: the naive local factor L_p^{nv}(A_f, s) equals the true one when
delta_p > 0 and is 1 when delta_p = 0; explain why: the naive factor at p is built from a_p alone, and at an
additive prime a_p = 0), the Rankin-Selberg method (unfolding; the theorem of Rankin and Shimura: for a
newform f of weight 2 and level N, <f, f> = (explicit constant involving N, pi, and the local factors at
bad primes) times L(Sym^2 f, 2); state the exact formula as in DFG04 Lemma 2.12 or Shimura 1976, with the
correction factors at the bad primes, since the paper's Section 1 says the Petersson norm is the special
value up to the local factors at bad primes), the true local factors at bad primes (the paper's table in
Section 1 derived in full: this is Lemma lem:euler; the computation of (ad V)^{I_q} and the Frobenius
eigenvalues for each Kodaira type at q >= 5: I_n (line with eigenvalue q^{-1}, factor 1 - q^{-1-s}), I_n^*
(same, but the naive factor is 1, so e_l = v_l(q^2 - 1)), II/II^*/IV/IV^* (image of inertia of order 3 or
6, invariant line spanned by sqrt(-3) in Z_l[zeta_3] = End_{I_q}(V), Frobenius acts by chi_{-3}(q),
factor 1 - chi_{-3}(q) q^{-s}, e_l = v_l(q - chi_{-3}(q))), III/III^* (order 4, eigenvalues +-i, invariant
line spanned by the diagonal element, Frobenius acts by chi_{-4}(q), e_l = v_l(q - chi_{-4}(q))), I_0^*
(V = V' tensor chi_q with V' unramified, ad V unramified with eigenvalues alpha/beta, 1, beta/alpha,
L_q(A_f, 1)^{-1} = ((q - 1)/q)((q + 1)^2 - a_q(E')^2)/q^2, e_l = v_l(q - 1) + v_l((q + 1)^2 - a_q(E')^2))),
the wild primes 2 and 3 (the Kodaira type does not determine the factor; examples from the paper's Remark
rem:wild: type IV at 2 has P_2(X) = 1 + 2X; type II at 2 has P_2 = 1; a type I_n^* at 2 with potentially good
reduction has a cubic P_2), how PARI computes these (lfunsympow(E, 2), lfuneuler; the polynomial P_q(X)
with L_q(Sym f, s) = P_q(q^{-s})^{-1}, and e_l = v_l(P_q(q^{-2})/(1 - a_q^2 q^{-2}))), the definition of
e_l(E, q) (the paper's Definition def:terms) and its invariance under quadratic twist, Flach's theorem on the
finiteness of the Selmer group of Sym^2 (statement), special values and the Bloch-Kato conjecture for the
adjoint (one page; the shape "L-value / period = Selmer times Tamagawa", the connection to the modular
degree via Petersson norm), Deligne's conjecture on critical values in one paragraph, the functional
equation and analytic continuation of L(Sym^2 f, s) (Shimura; Gelbart-Jacquet; statements).
Paper hooks: Section 1 (Petersson norm, Zagier, Watkins, Rankin, Shimura, Flach, naive versus true adjoint
L-function, DFG04 Lemma 2.12), Section 1.1 (delta_p, L_p(A_f, s), the naive factor, PARI's lfunsympow,
Definition def:terms, the table), Lemma lem:euler (in full), Remark rem:wild, Theorem thm:dfg14 and the
paragraph after it (the naive factors: level-raising factor at a good prime, 1 - p^{-2} at a multiplicative
prime), Lemma lem:fpr (L_p(A_f, 1)^{-1} = L_p(A_f(1), 0)^{-1} is an l-adic integer of valuation e_l at an
additive prime and v_l(1 - p^{-2}) at a multiplicative one), the appendix (rule(E, l)).

### Part VI. Congruences, the modular degree and the paper

**Chapter 20. Hecke algebras, congruence ideals and the theorem of Diamond, Flach and Guo** (`ch:congruence`,
`ch20_congruence.tex`)
Scope: Hecke algebras as finite flat Z-algebras and their localisations T_m at maximal ideals m (the maximal
ideal attached to (f, l): generated by l and the T_n - a_n(f); T tensor Z_l is the product of the T_m;
the m-component of S_2(Gamma_0(N); Z_l) via idempotents; which newforms belong to m: those with
eigencharacter congruent to phi_f mod m, i.e. with rho bar_g = rho bar_f), congruence modules and
congruence ideals (for a surjection pi: T -> O with kernel wp and I = Ann(wp): the congruence ideal eta =
pi(I); the congruence module O/eta = T/(wp + I); Hida's definition and the equality with the "largest
modulus of a congruence f = g with g in f^perp" (the paper's Lemma lem:crit; prove it in full here, in the
integral and the Z_l form; cross-reference the proof in Chapter 15 and avoid contradiction: Chapter 15
proves it, Chapter 20 restates it as a theorem of the theory of congruence modules and adds the
commutative algebra viewpoint), the theorem of Hida on congruence modules and the adjoint L-value (statement:
for weight 2 and level N, the congruence module of f is related to L(ad f, 1) / period up to primes dividing
2 N and the Euler factors; the precise statement in Hida 1981 and its refinement in DFG04), Wiles's numerical
criterion (DDT Theorem 5.3 / Lemma 4.17 in full: let O be a DVR, T a finite free O-algebra, pi: T -> O
surjective, wp = ker pi, eta = pi(Ann wp); then T is a complete intersection iff ... ; the paper only needs
the inequality half with a module L: the paper's Lemma lem:ddt417 stated and proved in full, in the
paper's generality (L free of finite rank with a perfect O-bilinear pairing for which T is self-adjoint,
L[wp] free of rank d with Gram determinant Delta: eta^d is contained in Delta O, with equality if L is free
over T), with every ingredient from Chapter 3 (saturation, L[wp]^perp = L[I], the cokernel of L[wp] ->
Hom(L[wp], O) has order #O/Delta)), the application to the modular degree (the paper's Lemma lem:hecke:
v_l(deg phi_E) = v_l(r_E) >= v_lambda(eta^empty_{f, lambda}) with equality if H^1(X_0(N), Z_l)_m is free over
T_m; proof in full; the paper's Remark rem:free on when freeness holds), the lattices and ideals of
Diamond, Flach and Guo (DFG04 Sections 1.5.3, 1.6.2, 1.7.3 as read for weight 2 and trivial character:
the integral structure M(M^Sigma, 1)_{!, lambda} = H^1(X_0(M^Sigma), Z_l) with its Hecke action; the
lattice M_{f^Sigma, lambda} = kernel of the kernel of the eigencharacter of f^Sigma (that is, the
sublattice killed by ker phi_{f^Sigma}), of rank two; the pairing delta hat_! = cup product composed with
the Atkin-Lehner involution w_{M^Sigma}, perfect and alternating, with all T_n and U_p self-adjoint; the
naive Sigma-finite congruence ideal eta^Sigma_{f, lambda} = the ideal of values of delta hat_! on
M_{f^Sigma, lambda}, equivalently the Gram determinant of the pairing on M_{f^Sigma, lambda} is
(eta^Sigma)^2 up to a unit (explain why a rank-two alternating pairing has Gram determinant a square)),
DFG04 Proposition 1.4(c) (the paper's Theorem thm:dfg14: eta^Sigma = eta^empty prod_{p in Sigma}
L_p^{nv}(A_f, 1)^{-1} when rho bar_f is irreducible; explain the three cases: additive primes change
nothing, a good prime contributes Wiles's level-raising factor, a multiplicative prime contributes
1 - p^{-2}; proof idea via Ihara's lemma / the degeneracy maps, with reference), the exceptional set S_f
(DFG04 (31): lambda | 2N or rho bar not absolutely irreducible on Gal(Qbar/Q(sqrt(l*)))), DFG04 Theorem 3.7
(the paper's Theorem thm:dfg37: for l not in S_f and Sigma a finite set of primes not containing l such that
M_{f, lambda} is minimally ramified outside Sigma, H^1_Sigma(Q, W) is finite of length v_lambda(eta^Sigma);
the meaning of "minimally ramified outside Sigma" and why the set of primes dividing N qualifies), DFG04
Theorem 2.7 (vanishing of H^0(Q, V^D) and H^1_f(Q, V^D)), DFG04 Theorem 0.1 and 0.2 (the Tamagawa number
conjecture for the adjoint motive; statement), the Taylor-Wiles method in outline (deformation rings
R_Sigma, the map R_Sigma -> T_Sigma, the numerical criterion, patching; the Selmer group H^1_Sigma(Q, W) as
the tangent space / dual of the cotangent space of R_Sigma, which is why its length is the congruence ideal:
the identity "length of Selmer group = valuation of congruence ideal" is the statement R = T plus complete
intersection; DDT Chapters 2 to 5 as the reference), the assembly: the paper's proof of Theorem thm:main
reproduced step by step with every input identified (Lemma lem:hecke, Theorem thm:dfg14, Theorem thm:dfg37,
Theorem thm:dfg27 plus Lemma lem:dfg21 plus Lemma lem:h0, Lemma lem:fpr, Definition def:terms, Lemma
lem:tamfactor; the cancellation of the naive factors at multiplicative primes; the twist argument for I_n^*
primes), the twist monotonicity theorem (the paper's Theorem thm:twist proved in full) and the proof of the
paper's Theorem thm:quant in full (Steps 1 to 4, with the Hecke congruence ideal eta^Hecke(g^S) and its
comparison with the cohomological one), the remarks after Theorem thm:quant (why the argument fails for
potentially good types II, III, IV), the Kim-Ota formula and the Tamagawa exponent (statement, Remark
rem:ko(2)), Open questions 1 and 2.
Paper hooks: Section 4 in full (Sections 4.1, 4.2, 4.3, 4.4: Theorem thm:dfg14, Lemma lem:ddt417, Lemma
lem:hecke, Remark rem:free, Theorem thm:dfg37, Theorem thm:dfg27, Lemma lem:dfg21, Lemma lem:fpr, Lemma
lem:h0, the proof of Theorem thm:main, Remark rem:ko, Theorem thm:twist, the proof of Theorem thm:quant and
the remark after it), Section 1 (Hida, DFG04, congruence ideal), Lemma lem:crit, Remark rem:ns.

**Chapter 21. Reading the paper: a guided tour** (`ch:paper`, `ch21_paper.tex`)
Scope: a complete, self-contained commentary on the paper, in the paper's order, for a reader who has the
cards of Chapters 1 to 20 at hand. For each definition, lemma, proposition, theorem, remark, conjecture and
section of the paper: restate it precisely (in the paper's notation, which the book shares), say which
chapters supply the tools, walk through the proof line by line expanding every step the paper compresses
(the paper is terse; the tour is not), and point out the exact place where each hypothesis is used. Cover:
the abstract and Section 1 (the local terms, Definition def:terms, the table; Theorem thm:main and the
reading of its hypotheses; Conjecture conj:euler and the weights w_3; the component group inequalities
(eq:main), (eq:twist) and Proposition prop:forms with its proof; the history and Theorem thm:qual, Theorem
thm:quant, Proposition prop:ns, Conjecture conj:eis); Section 2 (Lemma lem:tamagawa-exp, Lemma lem:IV,
Remark rem:types, Lemma lem:twist, Lemma lem:euler, Remark rem:wild, Lemma lem:tamfactor); Section 3 (Lemma
lem:crit, Lemma lem:old, the optimal-level theorem, cases (a), (b), (c), the example with 121a1, 539c1,
980i1, the remark on l | N and 99A1); Section 4 (Theorem thm:dfg14, Lemma lem:ddt417, Lemma lem:hecke,
Remark rem:free, Theorem thm:dfg37, Theorem thm:dfg27, Lemma lem:dfg21, Lemma lem:fpr, Lemma lem:h0, the
proof of Theorem thm:main, Remark rem:ko, Theorem thm:twist, the proof of Theorem thm:quant, the remark
after it); Section 5 (the proof of Proposition prop:ns, Remark rem:ns); Section 6 (the data and protocol;
how to read each table; the calibration argument of Section sec:sharp; the Tamagawa factor test of Section
sec:tam; the isolated terms of Section sec:iso; the two corollary forms; the 3Ns boundary; the wild primes
and w_3; out-of-table curves; the Eisenstein case); Section 7 (the prime 2 and Watkins's conjecture); the
open questions; the appendix (the PARI function rule(E, l) explained line by line, with the Kodaira codes).
Also: a dependency diagram of the paper's results (which lemma feeds which theorem), a table "hypothesis ->
where it is used -> what fails without it" (l odd; l not dividing 2N; absolute irreducibility over
Q(sqrt(l*)); X_0(N)-optimality; multiplicity one), a list of the exact statements imported from the
literature with their numbering (DFG04 Theorem 0.1, 0.2, 2.7, 3.7, Proposition 1.4, Lemma 2.1, Theorem
2.15, (31), (57), p. 708; DDT Theorem 3.1(e), 3.15, Lemma 4.17; FPR94 I.4.2.2; ARS12 Theorem 2.2; Atkin-Li
Theorem 3.1; Atkin-Lehner Theorem 3; Ribet83 Theorem 2.2; AU96 Lemma 2.1; Ribet-Stein Theorem 3.5; Kim-Ota
Theorem 1.1, Definition 2.12; Kraus 1990; Zywina 2015; Sutherland 2016), and worked verifications of the
numerical examples (121a1: e_3(E, 11) = v_3(12) = 1, deg = 6; 539c1: e_3(E, 7) = v_3(48) = 1, t_3(E, 7) = 1,
deg = 2^5 3^2; 980i1: deg = 2^6 3^2 5; 726a1: 3Ns, the cancellation; 99A1: deg 4 versus r = 12).
Paper hooks: all.

**Chapter 22. Computation, data and the statistical protocol** (`ch:computation`, `ch22_computation.tex`)
Scope: PARI/GP for the reader who has never used it (installation, ellinit, ellglobalred and its output
(conductor, minimal model change, the Kodaira symbols and Tamagawa numbers per prime, the local data
structure with the Kodaira codes), ellap, ellan, elltors, ellisomat, ellmoddegree (and its memory needs),
elldivpol, lfuncreate / lfunsympow / lfuneuler and the conventions for the symmetric square Euler factor,
ellinit over Q_q and the Tate parameter (elltatepairing is not it: explain how to extract the Tate
parameter / its valuation from v_q(j) and the unit part via the Tate curve algorithm or via ellinit(E, q)),
valuation, factor), Cremona's tables and the ecdata repository (what the files contain: allcurves, allbsd,
alldegphi, allgens, alllabels, allisog, the Kodaira symbols and Tamagawa numbers, the mod l images with
Sutherland's labels (2Cs, 3B.1.1, 3Cs.1.1, 3Ns, 3Nn, 5B, ...), optimality and the Cremona label "1"; the
LMFDB and its labels versus Cremona's), reading a Cremona label (11a1, 121a1, 121c, 121d, 539c1, 980i1,
726a1, 99A1 and the capitalisation convention), the paper's data protocol (working set N <= 300000, hold-out
300000 < N <= 400000, extension 400000 < N <= 500000, out-of-table curves with 500000 < N <= 4 million;
pre-registration: the statement was written down before the hold-out was looked at; what "nothing was
adjusted after the hold-out test" means; which statements were blind-tested and which were only confirmed;
the role of the out-of-table set for Conjecture conj:euler), elementary statistics of the tests (what a
"violation" is; the calibration argument of the paper's Section sec:sharp explained with the numbers: among
bound-zero curves 53.2% have v_3 = 0, so under independence the 867,578 curves with a positive bound would
give about 605,000 violations, there are none; what this does and does not show; equality rates and the
mean excess as descriptive statistics; the base rates by Kodaira type; a short, honest discussion of
multiple comparisons and of why a conjecture found on the working set must be tested on held-out data; the
reader's statistics background is enough for this), the PARI function rule(E, l, iii) of the paper's
appendix reproduced and explained line by line (ellglobalred's R[4] and R[5], the Kodaira code k, the
omitted factor r = P_q(q^{-2}) with the multiplicative correction, the exclusion of type III/III^* unless
iii = 1, the weights w_3 at q = 3, the Tamagawa exponent from v_q(j), the correction ns3(E) via the
factorisation of the 3-division polynomial), worked sessions: 121a1 returns [1, 1]; 726a1 returns [2, 2]
with and without iii; 539c1; 980i1; 99A1 (where ellmoddegree gives 4 and the congruence number 12 is not
given by PARI directly), computing e_l(E, q) by hand from the Kodaira type for q >= 5 and checking against
lfunsympow, computing t_l(E, q), computing the mod 3 image class 3Ns via elldivpol, the twist lemma check
(twist_lemma_check.gp: how to write it), reproducing a row of the paper's tables on a small range (a GP
script that loops over curves of conductor up to 1000 from ellsearch or from a downloaded ecdata file and
counts violations and equalities), how the modular degree is computed (Watkins's algorithm in outline;
Cremona's; why it is expensive), the repository named in the paper's appendix and what each script does
(descriptive list only), a note on reproducibility practice (pinned data commits, re-running from a clean
clone).
Paper hooks: Section 1 (PARI's lfunsympow), Remark rem:wild, Lemma lem:euler (confirmed against PARI),
Section 6 in full (sec:data and its subsections), the appendix, Section 1.4 (Cremona's tables and
optimality), Proposition prop:ns (3-division polynomial), Section sec:eis (image labels 3Cs.1.1, 3B.1.1).

### Back matter

**Appendix A. Prerequisites: what we assume and where to look** (`ch:prereq`, `chA_prereq.tex`)
Short refresher cards for the assumed background: real analysis (completeness, uniform convergence,
power series), linear algebra (eigenvalues, Jordan form, bilinear forms, Gram determinants, tensor
products of vector spaces), complex analysis (Mobius transformations, the upper half plane, residues,
Laurent expansions, uniform limits of holomorphic functions), elementary group theory and representations
as in RHB, elementary probability and statistics (what a base rate is, what a hold-out set is). Each
item with a pointer to where in the book it is first used.

**Appendix B. Notation, conventions and index of symbols** (`ch:notation`, `chB_notation.tex`)
A table of every symbol used in the paper and the book, in the paper's notation (V, T, rho, rho bar, A_f,
ad, Sym, delta_p, L_p, L_p^nv, P_q, e_l(E, q), t_l(E, q), n_q, q_E, u, c, Tam_p, Fitt, H^1_f, H^1_Sigma,
W, T^D, V^D, W^D, S_f, eta^Sigma_{f, lambda}, M_{f, lambda}, delta hat_!, phi_f, I, J, r_E, deg phi_E,
Phi_q, Phig_q, c_q, w_l(E, q), w_3(E), h_l(E), chi_{-3}, chi_{-4}, chi_q, q*, l*, E^(q), E_S, N_s, N_ns,
3Ns, Kodaira symbols and PARI codes, ...) with the chapter where it is defined. Conventions: arithmetic
versus geometric Frobenius; the normalisation of L(Sym^2 f, s) versus L(ad f, s); the sign conventions for
Tate twists; "length" means Z_l-length; v_l is the l-adic valuation normalised by v_l(l) = 1.

**Bibliography** (`refs.bib`): every work cited in the paper, with full bibliographic data, plus the standard
textbooks used as references (Silverman AEC and ATAEC, Diamond-Shurman, Serre's Local Fields and
Abelian l-adic representations, Neukirch, Milne's notes on class field theory and on elliptic curves,
Cassels-Frohlich, Washington, Atiyah-Macdonald, Eisenbud, Weibel, Brown, Neukirch-Schmidt-Wingberg,
Rubin's Euler systems, Berger's survey on p-adic representations, Hida's books, Cremona's book, the LMFDB,
the PARI manual, Lang's Algebra, Dummit-Foote, Serre's Linear representations of finite groups, Fulton's
Algebraic curves, Hartshorne, Miranda's Riemann surfaces, Bosch-Lutkebohmert-Raynaud, Conrad's notes).

## 5. Dependency graph

```
1 groups -> 4 reps -> 11 galrep
2 rings  -> 3 modules -> 16 cohomology -> 17 galcoh -> 18 blochkato
2 rings  -> 5 galois -> 6 ant -> 7 local -> 10 reduction -> 11 galrep
8 curves -> 9 ellcurves -> 10 reduction
9 ellcurves -> 11 galrep
12 modforms -> 13 hecke -> 14 moddeg -> 15 modgalrep
11 galrep, 13 hecke, 7 local -> 15 modgalrep
3 modules, 13 hecke, 14 moddeg, 15 modgalrep, 18 blochkato, 19 lfunctions -> 20 congruence
7 local, 11 galrep, 18 blochkato -> 19 lfunctions
everything -> 21 paper
9, 10, 11, 14, 19, 21 -> 22 computation
```

## 6. Concept-to-chapter map for the paper

| Notion in the paper | Chapter(s) |
|-|-|
| X_0(N)-optimal curve, modular parametrisation, modular degree, Manin constant | 14 |
| newform f_E, S_2(Gamma_0(N)), q-expansions, coefficientwise congruences | 12, 13 |
| l-adic valuations of integers and rationals | 2 |
| rho_{E,l}, rho bar, T_l E, V_l E, E[l], absolute irreducibility, restriction to Gal(Qbar/Q(sqrt(l*))) | 4, 5, 9, 11 |
| adjoint ad^0 V, Sym^2, trace form, A_f(1) = Hom(A_f, Z_l(1)) | 4, 18 |
| Euler factors of the adjoint L-function, naive versus true, delta_p, P_q(X), e_l(E, q) | 19 |
| Kodaira types, component groups, Tamagawa numbers c_q, conductor exponents, Tate's algorithm | 10 |
| chi_{-3}, chi_{-4}, chi_q, q*, l*, Kronecker symbols | 2, 6 |
| the twist E' of good reduction, a_q(E'), quadratic twists and their invariants | 9, 10 |
| Tate parameter, unit part, l-th powers in F_q^x, t_l(E, q), potentially multiplicative reduction | 2, 7, 10 |
| Sigma-imprimitive Selmer group, Bloch-Kato Selmer group, H^1_f, H^1_Sigma | 17, 18 |
| congruence ideal, congruence number r_E, eta^Sigma, M_{f, lambda}, the pairing delta hat_! | 13, 14, 20 |
| Fontaine-Perrin-Riou Tamagawa factor Tam_p(M) = Fitt(H^1(I_p, M)_tors)^G | 3, 16, 18 |
| the computation of Tam_q(ad T) at a multiplicative prime | 16, 17, 18 |
| Agashe-Ribet-Stein: deg phi_E divides r_E, equality away from p^2 \| N | 14 |
| multiplicity one, freeness of H^1(X_0(N), Z_l)_m over T_m, Gorenstein, J_0(N)[m] | 3, 14, 20 |
| Steinberg representation, unramified twists, ramified twist has conductor exponent 2 | 7, 15 |
| normaliser of a split Cartan subgroup, 3Ns, GL_2(F_3) and its subgroups, orbits on lines | 1, 4, 11 |
| h_l(E) = length of H^0(Q, ad T(1) tensor Q_l/Z_l), rho bar = rho bar tensor chi | 4, 11, 18 |
| induced representations, Frobenius reciprocity, characters of order 4 | 4 |
| 3-division polynomial, its factorisation pattern | 5, 9, 11 |
| PARI/GP, Cremona's tables, ecdata, LMFDB, Sutherland's labels | 22 |
| Eisenstein case, rational l-isogeny, Z/3 + mu_3, torsion, cuspidal subgroup, Eisenstein ideal | 9, 11, 14 |
| Petersson norm, Rankin-Selberg, L(Sym^2 f, 2), Zagier, Watkins, Flach | 12, 13, 14, 19 |
| Hida's congruence modules, Wiles's numerical criterion, DDT Lemma 4.17 | 3, 20 |
| Taylor-Wiles, R = T, DFG04 Theorems 0.1, 0.2, 2.7, 3.7, Proposition 1.4, Lemma 2.1, Theorem 2.15 | 18, 20 |
| level lowering (Ribet, Carayol, Diamond; DDT Theorem 3.15), Serre conductor, Serre's conjecture | 11, 15 |
| level raising (Ribet), Wiles's level-raising factor | 15, 19, 20 |
| Kraus's semistability defect 12/gcd(v_q(Delta), 12) | 10 |
| image of inertia on T_l E at additive primes, unipotent elements, Z_3[zeta_3] | 4, 6, 7, 11 |
| Atkin-Li twisting theorem, Atkin-Lehner a_p = 0 for p^2 \| level, oldforms, U_p eigenvalues, stabilisations, depleted forms | 13 |
| Chebotarev, Brauer-Nesbitt | 4, 5 |
| Deligne-Fontaine description of rho bar at l, a_l mod l | 11, 15 |
| DDT Theorem 3.1(e): local structure at multiplicative primes | 11, 15 |
| finite flat group schemes, "good at l" | 11, 18 |
| Kummer theory, Kummer classes, H^1(G, Z_l(1)), tame character, Frob^{-1} t Frob = t^{q^{-1}} | 5, 7, 16, 17 |
| inflation-restriction, H^1(<t>, M) = M/(t - 1)M, conjugation action of G/I on H^1(I, M) | 16 |
| Fitting ideals, lengths, Pontryagin duality, Gram determinants, saturated sublattices | 3 |
| perfect pairing S_2(Gamma_0(N); Z) x T -> Z (Ribet 1983, Abbes-Ullmo) | 13 |
| H^1(X_0(N), Z_l), cup product, Atkin-Lehner, Hecke self-adjointness | 8, 14 |
| Ribet-Takahashi, Pollack-Weston, Kim-Ota, Tamagawa exponent | 14, 15, 20 |
| Watkins's conjecture, Calegari-Emerton | 14 |
| the statistical protocol, calibration, hold-out sets | 22 |
| the function rule(E, l) and the Kodaira codes | 10, 22 |
| the worked examples 11a1, 20a1, 121a1, 539c1, 980i1, 726a1, 99A1 | 9, 14, 15, 21, 22 |

## 7. Conventions for writing

### 7.1 Files and structure

* One file per chapter: `chapters/chNN_slug.tex` (two-digit NN; appendices `chA_prereq.tex`, `chB_notation.tex`).
* A chapter file starts with `\chapter{Title}\label{ch:slug}` and contains, in this order:
  1. `\section*{Core results at a glance}`: a numbered `enumerate` list (use `\begin{enumerate}[label=\textbf{\thechapter.\arabic*}]`
     from `enumitem`), each item a precise statement of a definition, theorem, lemma, proposition or
     construction, with its rigour tag *(proved here)* / *(proof sketched here)* / *(stated; reference)*,
     and a `\Cref` to the numbered environment in the chapter where it lives. This card is the refresher.
     It must be complete: every numbered theorem, proposition and lemma of the chapter, and every definition
     the paper uses, appears on the card.
  2. `\section*{Where the paper uses this chapter}`: a short list naming the paper's lemmas, theorems,
     remarks, definitions and sections (by the paper's own labels and names, e.g. "Lemma lem:tamfactor
     (the Tamagawa factor at a multiplicative prime)") and which results of this chapter they use.
  3. The numbered sections of the exposition.
  4. `\section{Exercises}`.
  5. `\section{Notes and references}`: where to read more, which references were followed, which theorem
     numbers were cited.
* Chapters never contain `\input`, `\include`, `\newcommand`, `\renewcommand`, `\def`,
  `\DeclareMathOperator`, `\usepackage`, `\newtheorem`, `\begin{document}` or `\bibliography`. Everything
  needed is in `preamble.tex`. If a macro is missing, write `\operatorname{...}` inline.
* Labels: every label in a chapter is prefixed with the chapter slug: `\label{thm:groups:sylow}`,
  `\label{def:modules:fitting}`, `\label{eq:local:tame}`, `\label{sec:hecke:newforms}`, `\label{ex:reps:q8}`.
  Cross-chapter references use only `\Cref{ch:slug}` (chapter labels are listed in Section 4).
* Citations: `\cite{key}` with keys from `refs.bib`. Keys for the paper's own references are exactly the
  paper's keys: `Cremona97, Watkins02, ARS12, Zagier85, DFG04, Flach92, Hida81, FPR94, SilvermanATAEC,
  Sutherland16, RibetTakahashi97, Takahashi01, Pasten, PollackWeston11, KimOta, Kraus90, AtkinLi78,
  AtkinLehner70, Ribet83, AU96, Edixhoven92, DDT, Ribet90, Carayol89, Diamond95, Tilouine97, RibetStein,
  Zywina15, Mazur77, Dummigan06, CalegariEmerton09, Yazdani11, CaroPasten22, HatleyKundu, BKP, PARI`.
  Standard textbook keys: `SilvermanAEC, DiamondShurman, SerreLocalFields, SerreAbelian, SerreLinearReps,
  SerreCourse, Neukirch, NSW, MilneCFT, MilneEC, MilneANT, CasselsFrohlich, Washington, AtiyahMacdonald,
  Eisenbud, Weibel, Brown, Rubin, Berger, HidaMFG, HidaBook, CremonaBook, LMFDB, PARIusers, Lang, DummitFoote,
  Fulton, Hartshorne, Miranda, BLR, Conrad, Shimura71, Shimura76, GelbartJacquet, Miyake, Koblitz, Knapp,
  Husemoller, Tate75, TateAlgorithm, Kodaira, NeronModels, Ogg, BlochKato, Fontaine, Deligne, Wiles95,
  TaylorWiles, BCDT, KhareWintenberger, Khare, Ribet76, Ribet91, Mazur78, MazurRibet, Zagier85, Cremona97,
  Stein, Loeffler, Sutherland16, Zywina15, Serre72`. If a chapter needs a reference not in `refs.bib`, add a
  complete entry to `bib/chNN.bib` (the chapter's own bib file, which main.tex includes), never to `refs.bib`.
* Environments (defined in `preamble.tex`, all numbered `chapter.counter` in one sequence): `theorem`,
  `proposition`, `lemma`, `corollary`, `conjecture`, `definition`, `example`, `exercise`, `construction`,
  `convention`, `remark`, `warning`, `paperlink` (a remark-style environment titled "In the paper", used to
  point at the exact place in the paper where a result is used). Proofs in `proof`; for sketches use
  `\begin{proof}[Sketch of proof]`.
* The paper's macros are the book's macros: `\Q \Z \F \R \C \N \T \degphi \ord \Phig \Gal \ad \Sym \nv
  \Frob \Fitt \Tam \len \Ns` plus the operators listed in `preamble.tex`. Use `\ad V` for the trace-zero
  adjoint exactly as the paper does.
* Kodaira symbols: `\mathrm{I}_n`, `\mathrm{I}_n^*`, `\mathrm{II}`, `\mathrm{II}^*`, `\mathrm{III}`,
  `\mathrm{III}^*`, `\mathrm{IV}`, `\mathrm{IV}^*`, `\mathrm{I}_0^*`.
* Code (PARI/GP, Python) goes in `\begin{lstlisting}[language=GP]` ... `\end{lstlisting}` or `verbatim`.

### 7.2 Typography rules (strict)

* **Never use an em dash or an en dash, in any form**: not the characters "—" or "–", not the LaTeX
  ligatures `---` or `--`. Use a colon, a semicolon, a comma, or parentheses. Double names are hyphenated
  with a plain hyphen: Bloch-Kato, Atkin-Lehner, Diamond-Flach-Guo, Taylor-Wiles, Fontaine-Perrin-Riou.
  Number ranges are written "pages 663 to 727" or "663-727" with a plain hyphen. The lint script rejects
  any dash of either kind.
* No Unicode mathematics in LaTeX source (write `\ell`, `\alpha`, not the characters).
* Sentences are short. Each section starts with one paragraph saying what it is for and where in the
  paper it is used.
* Every theorem has either a proof, a sketch clearly labelled as such, or the sentence "We do not prove
  this; see ..." with a precise reference. Never present a sketch as a proof.
* Name results by their authors on first appearance (the theorem of Agashe, Ribet and Stein), then by the
  book's label.

### 7.3 Length and depth

* Target 1,000 to 2,200 lines of LaTeX per chapter (roughly 25 to 45 printed pages), the card excluded.
  Chapters 11, 15, 18, 20 and 21 may run to 2,800 lines. Appendices 400 to 800 lines.
* Depth: full proofs for everything elementary; for the deep theorems, the exact statement, the
  hypotheses, the idea of proof in a paragraph or a page, and the reference.
* The paper's own lemmas are proved in full in the book, with every compressed step expanded (the paper's
  proofs are written for experts). The paper's imported theorems (DFG04, DDT, FPR94, ARS12, Ribet, Carayol,
  Diamond, Atkin-Li, Atkin-Lehner, Kraus, Zywina, Tilouine, Ribet-Stein) are stated precisely and sketched.

### 7.4 Building and checking

* `tools/build_chapter.sh NN` compiles chapter NN alone (with the shared preamble and bibliography) into
  `build/chNN/` and prints the errors. A chapter must compile with zero errors before it is considered
  written. Warnings about undefined references to other chapters' labels are not allowed (use only
  `\Cref{ch:slug}` across chapters); undefined citations are errors to fix by adding bib entries.
* `tools/lint.py chapters/chNN_slug.tex` rejects dashes, forbidden commands, unprefixed labels, Unicode
  mathematics and stray `\input`. It must pass clean.
* `tools/build.sh` builds the whole book (`main.pdf`).

## 8. Production process

1. The plan (this file), the preamble, the build tools and the bibliography skeleton are committed first.
2. One agent per chapter, in two stages, run as a pipeline per Part:
   * **Stage 1 (line-up).** The agent reads this plan, the paper and the preamble, then lines up the core
     theorems, concepts, lemmas, definitions, constructions and examples of its chapter in teaching order,
     with precise statements, rigour levels, references and paper hooks, and a section plan with line
     targets. Output: `outlines/chNN_slug.md`.
   * **Stage 2 (writing).** A fresh agent takes the line-up and writes the chapter independently to
     `chapters/chNN_slug.tex`, compiles it, lints it, and fixes every error.
3. Each written chapter is then reviewed by two independent agents (a sceptical mathematician who tries to
   find false statements, wrong hypotheses, wrong theorem numbers, gaps presented as proofs; and an editor
   who checks coverage against the line-up and this plan, accessibility for the stated audience, the
   completeness of the card, LaTeX hygiene and the typography rules). A fourth agent applies the fixes and
   recompiles. The mathematical review is repeated until no blocking findings remain (at most three rounds).
4. After all chapters exist: a completeness critic reads the paper and all the cards and lists any notion of
   the paper not covered; a cross-reference pass upgrades chapter-level references in Chapters 21 and 22 to
   precise theorem labels where they exist; the whole book is built; the bibliography is verified.
5. Everything is committed on the branch `claude/textbook-paper-prerequisites-clhh5a`.
