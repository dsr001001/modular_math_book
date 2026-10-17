# Important notes

Points raised while preparing the textbook that matter for the paper itself or for the book's accuracy.
Each entry says where it came from and what to do about it.

## From the Chapter 1 outline (groups and matrix groups over finite fields)

Source: `outlines/ch01_groups.md`. Group orders and subgroup claims were checked by enumerating all 48
elements and all 55 subgroups of GL_2(F_3) by computer; the orders for q = 5 and q = 7 were checked the
same way.

### 1. A gap in the paper's proof of Proposition prop:ns

The proof says that SL_2(F_3) and Q_8 act absolutely irreducibly on F_3^2 because "they are non-abelian
and act faithfully". That reason is not enough on its own: a Borel subgroup of GL_2(F_3) is also
non-abelian and acts faithfully, yet it fixes a line.

The missing step: if a subgroup G of GL_2 over an algebraically closed field fixes a line, then G lies in
a Borel subgroup, so its commutator subgroup lies in the unipotent radical and is abelian of exponent
dividing the characteristic. SL_2(F_3) and Q_8 both have commutator subgroups that are not of this kind
(Q_8 has commutator subgroup {+1, -1}, which is not unipotent; SL_2(F_3) has commutator subgroup Q_8,
which is not abelian), so neither fixes a line over F_9, hence both act absolutely irreducibly.

The outline's item 5.7 supplies this step. **Action:** consider adding one sentence to the paper's proof.

### 2. N_s(F_3) is not maximal

With the standard models (at q = 3 the non-square is -1), the normaliser of the split Cartan subgroup,
N_s(F_3) of order 8, sits inside the normaliser of the nonsplit Cartan subgroup, N_ns(F_3) of order 16,
with index 2. Likewise N_s(F_5) lies in a subgroup of order 96 whose image in PGL_2(F_5) is S_4.

So N_s is not a maximal subgroup at l = 3 or l = 5. **Action:** the book must not call it maximal there.
The paper does not claim maximality, but any reader importing the general picture for large l should be
warned.

### 3. Sutherland's labels need checking against the source

The labels 3Cs.1.1, 3Cs, 3B.1.1, 3B.1.2, 3Ns, 3B, 3Nn, 3Cn were recalled from memory and defined in the
outline by intrinsic properties. Swapping the row and column convention swaps 3B.1.1 and 3B.1.2.

**Action:** check every label against the tables of Sutherland16 (Forum Math. Sigma 4, 2016, e4) before
the chapter is written. The paper uses 3Ns, 3Cs.1.1 and 3B.1.1 (Sections sec:anomaly and sec:eis), so
those three matter most.

### 4. Citations given by section only

The exact theorem numbers for Dickson's classification of subgroups of PGL_2(F_l) (in Serre72), for
Zywina's list of possible mod 3 images (Zywina15), and for the Dummit-Foote results could not be
confirmed. The outline cites these by section.

**Action:** look up and insert the theorem numbers, or leave the section citations.

## From the Chapter 5 outline (Galois theory, Kummer theory, quadratic characters)

Source: `outlines/ch05_galois.md`, Section 8, which has the full argument for each point. Points 1 and 2
were also checked independently by the orchestrating session; points 3 to 6 are as reported by the
outline agent.

### 5. Lemma lem:h0: the finiteness argument confuses chi_l with chi_{l*}; the true bound is h_l(E) <= 1

The proof says that rho = rho tensor chi_l would force a_p = 0 at primes inert in Q(sqrt(l*)), which
happens only for CM curves. That mixes the cyclotomic character chi_l with the quadratic character
chi_{l*}. (rho = rho tensor chi_l is impossible for every E: it would give p a_p = a_p at all good p.)

The correct statement is stronger and elementary. If H^0(Q, ad T(1) tensor Q_l/Z_l) has an element of
exact order l^k, then (rhobar being absolutely irreducible, so the l-torsion of H^0 is a line) a lift of it
is an isomorphism rho mod l^k = (rho tensor chi_l) mod l^k. Taking determinants gives chi_l^2 = 1 mod l^k
on G_Q. Since chi_l(G_Q) = Z_l^x, this happens only for l = 3, k = 1 (4 is not 1 mod 9). Hence:

* h_l(E) = 0 for every l >= 5;
* h_3(E) <= 1, with equality iff rhobar_{E,3} = rhobar_{E,3} tensor chi_{-3};

for every E with rhobar irreducible, CM or not.

**Action:** replace the finiteness sentence by the determinant argument, drop "for E without complex
multiplication" there, and in Section sec:anomaly replace "h_3(E) <= 1 because some prime p < 1223 inert
in Q(sqrt(-3)) has 9 not dividing a_p" by "h_3(E) <= 1 by Lemma lem:h0". The numerical check was valid but
is no longer needed. Confidence: high (checked twice).

### 6. Section 1.3 ("Beyond the hypotheses"): the criterion for h_l(E) > 0 is stated with the wrong character

The paper says h_l(E) "is positive exactly when rhobar = rhobar tensor chi_{l*}". For l >= 5 this is wrong:
rhobar = rhobar tensor chi_{l*} can occur (rhobar induced from Q(sqrt(l*)), the case excluded by S_f), but
h_l(E) = 0 always for l >= 5, as Lemma lem:h0 itself says. The criterion of Lemma lem:h0 uses the residual
cyclotomic character chibar_l, which equals chi_{l*} only for l = 3. The opening sentence of the subsection
("a correction term when the representation is induced from Q(sqrt(l*))") is likewise right only for l = 3.

**Action:** write "is positive exactly when rhobar = rhobar tensor chibar_l, which forces l = 3, where
chibar_3 = chi_{-3}", and "a correction term when l = 3 and the representation is induced from Q(sqrt(-3))".
Confidence: high (checked twice).

### 7. Lemma lem:tamfactor: "c' is the image of kappa in H^1(G/I, Z_l(1)^I)" names a map that does not exist

There is no natural map H^1(G, Z_l(1)) -> H^1(G/I, Z_l(1)^I): inflation goes the other way, and kappa is
not inflated, since its restriction to I is n times the tame character. The value c' = kappa(Frob) depends
on the choice of Frobenius lift and of cocycle.

**Fix:** write q_E = q^n u, so kappa = n kappa_q + kappa_u. Here kappa_u is unramified, inflated from the
class of u in H^1(G/I, Z_l(1)) = Z_l(1)/(q - 1) = F_q^x tensor Z_l. Choosing the Frobenius lift that fixes a
compatible system of l-power roots of q gives c' = kappa_u(Frob); in general c' is well defined modulo
(n', q - 1) Z_l, which does not change min(v_l(n), v_l(q - 1), v_l(c')). **The conclusion of the lemma is
unaffected.** Confidence: high, as reported by the outline agent.

**Addendum (from the Chapter 17 outline, checked by the orchestrating session): point 7 overstated the
problem.** Since q != l, inertia acts trivially on Z_l(1), so H^1(G/I, Z_l(1)^I) = Z_l(1)/(q - 1) = F_q^x
tensor Z_l; and since q is a canonical uniformiser of Q_q, H^1(Q_q, Z_l(1)) = lim Q_q^x/(Q_q^x)^{l^k} splits
canonically as Z_l kappa_q + H^1_ur. Projection onto the unramified summand along kappa_q gives the paper's
"image of kappa in H^1(G/I, Z_l(1)^I)" a precise meaning (it is the class of the unit part u). What remains
imprecise: c' is a cocycle value, equal to eps(Frob) times that image only for the Frobenius lift fixing a
compatible system of l-power roots of q, and in general it is well defined only modulo (n, q - 1), not modulo
q - 1 as the paper says. The conclusion of the lemma is unaffected. **Action (revised):** keep the paper's
phrase, add "via the splitting given by the uniformiser q", and state the indeterminacy correctly.

### 8. Lemma lem:tamagawa-exp: notation clash and an imprecise phrase (expository only)

The proof calls the Tate parameter u, while Lemma lem:tamfactor uses u for its unit part q_E q^{-n}. The
phrase "u is an l^t-th power in Q_q^ur up to units" mixes two statements.

**Fix:** call the Tate parameter q_E, and say: by Kummer theory over Q_q^ur (which contains mu_{l^t} as
q is not l), inertia acts trivially on E[l^t] iff q_E is an l^t-th power in Q_q^ur; units of its valuation
ring are l^t-th powers by Hensel, so this holds iff l^t divides v_q(q_E) = n_q. No mathematical error.

### 9. Proposition prop:ns: the hypothesis "without complex multiplication" is not used (harmless)

The list GL_2(F_3), N_ns(F_3), N_s(F_3) follows from surjectivity of det rhobar_{E,3} = chi_{-3}, the
irreducibility of E[3] and complex conjugation, by pure group theory, with no appeal to Zywina's
classification. The rest of the proof is also CM-free. **Action:** optional; drop the hypothesis or say it is
not needed.

### 10. Lemma lem:old and the proof of Lemma lem:h0: "irreducible" should be "absolutely irreducible"

Chebotarev plus Brauer-Nesbitt give only rhobar_h^ss = rhobar^ss over a common finite field; to conclude
rhobar_h = rhobar one needs rhobar absolutely irreducible. The Clifford-theory equivalence in lem:h0 also
needs it. Both hold for rhobar_{E,l}, because for l odd, irreducible implies absolutely irreducible in the
presence of complex conjugation (eigenvalues +1 and -1 are distinct).

**Fix:** add "(hence absolutely irreducible, complex conjugation having distinct eigenvalues +1 and -1)"
after "irreducible" in both places, and "over a common finite extension of F_l" after "rhobar_h = rhobar".
Minor gap; confidence high.

## From the Chapter 6 outline (algebraic number theory, Frobenius)

Source: `outlines/ch06_ant.md`, Part 13. Point 11 was also checked independently by the orchestrating
session; points 12 to 14 are as reported by the outline agent.

### 11. The Frobenius convention: the L-factors need the geometric Frobenius, Lemma lem:tamfactor uses the arithmetic one

Section 1.1 defines L_p(A_f, s) = det(1 - Frob_p p^{-s} | A_f^{I_p})^{-1} without saying which Frobenius.
At a multiplicative prime, the inertia-fixed line of ad V is spanned by e = e_1 tensor e_2^vee (the map
e_2 -> e_1), on which Frobenius acts by the cyclotomic character chi_l(Frob).

* With the arithmetic Frobenius, chi_l(Frob) = q, so the factor would be 1 - q^{1-s}.
* With the geometric Frobenius, chi_l(Frob) = q^{-1}, giving the tabulated 1 - q^{-1-s}.

The table of Section 1, the proof of Lemma lem:euler (type I_n: "a line with eigenvalue q^{-1}"), PARI's
factors and the identity L_p(A_f, 1) = L_p(A_f(1), 0) of Lemma lem:fpr are all correct with the
**geometric** Frobenius, which is also DFG04's convention. But the proof of Lemma lem:tamfactor writes
rho(Frob) = [[eps q, c'], [0, eps]], which is the **arithmetic** Frobenius. Both computations are right in
their own convention; the paper never says which one it uses where.

**Action:** in Section 1.1 and in the proof of Lemma lem:euler, say "geometric Frobenius"; in the proof of
Lemma lem:tamfactor, say "arithmetic Frobenius" (or rewrite it with the geometric one). No number in the
paper changes. Confidence: high (checked twice).

### 12. Lemma lem:euler: "Z_l[zeta_3] = End_{I_q}(V)" should be stated for T, or with Q_l coefficients

For V with inertia acting through sigma of order 3 (eigenvalues zeta_3 and zeta_3^{-1}), the correct
statements are End_{I_q}(T) = Z_l[sigma] = Z_l tensor Z[zeta_3] and End_{I_q}(V) = Q_l tensor Q(zeta_3).
The latter is not a field when l = 1 mod 3 (it is Q_l x Q_l). The argument of the lemma is unaffected.
**Action:** replace V by T, or Z_l by Q_l and say "tensor". Confidence: high.

### 13. Lemma lem:IV: notation slip in "Z_3[sigma]/(sigma^2 + sigma + 1)"

The quotient is of the polynomial ring: Z_3[X]/(X^2 + X + 1), with sigma acting as X. As written,
Z_3[sigma] already satisfies the relation. **Action:** write Z_3[X]/(X^2 + X + 1). Confidence: high.

### 14. Addition to point 5 (Lemma lem:h0): the CM alternative never arises when l does not divide N

An elliptic curve over Q with CM by Q(sqrt(l*)) needs that field to have class number 1, so
l* is in {-3, -7, -11, -19, -43, -67, -163}, that is l in {3, 7, 11, 19, 43, 67, 163}. Such a curve has bad
reduction at the prime ramified in the CM field, so l divides N. Under the paper's standing hypothesis
l not dividing N, the CM case cannot occur at all. This is a side remark: point 5 already removes the need
for the CM argument. Confidence: medium-high (the conductor fact is standard but was not re-derived).

## From the Chapter 21 outline (the guided tour of the paper)

Source: `outlines/ch21_paper.md`, Section 9, with full arguments. Points 15 and 17 were also checked
independently by the orchestrating session; the others are as reported by the outline agent, which checked
the numerical claims in Python against Cremona's ecdata files. The Chapter 21 outline places all points of
this file at the paper items they concern (its Part C).

### 15. Definition def:terms: e_l(E, q) is not invariant under quadratic twist

The definition ends "Both terms are invariant under quadratic twist." That holds for t_l, not for e_l when
the twist is ramified at q and changes the type there. Example: 11a1 is multiplicative at 11, so
e_3(E, 11) = 0 (type I_5 at 11); its twist by chi_{-11} (the curve 121d2, in class 121d) has type I_5^* at 11,
so e_3 = v_3(11^2 - 1) = 1. (Corrected after the Chapter 9 outline: an earlier version said I_1^*, which
is the twist of 11a3; the value of e_3 and the conclusion are the same.) The true
adjoint factor is twist-invariant; the naive one is not, so their ratio is not.

**Action:** restrict the sentence to t_l, or to twists unramified at q. Confidence: high (checked twice).

### 16. Remark after Theorem thm:twist: strict inequality is not "only in case (b)"

The paper reports, for the data, "equality in every pair of case (c) and strict inequality only in case
(b)". This contradicts Theorem thm:quant, which predicts a gap of e_l(E, q) = v_l(q^2 - 1) in case (a) (type
I_n^*) too. The agent's counterexamples in case (a), comparing v_3 of the modular degrees:

* 539c1 versus 77c1: 2 versus 1;
* 980i1 versus 140b1: 2 versus 1;
* 121d1 versus 11a1: 1 versus 0.

**Action:** re-run the count and correct the sentence (strict inequality in cases (a) and (b), with the
difference the Euler term). Confidence: high, as reported (modular degrees from ecdata).

### 17. Conjecture conj:eis and Section sec:eis: the bound D <= 2 is provable, not conjectural

The paper says it has "not proved that the two [sources of a deficit of 2] cannot coexist". They cannot, for
E without CM. If E[3] = Z/3 + mu_3 and P is a rational point of order 9, compose the dual of E -> E/mu_3
with E -> E/<P>. The kernel has order 27, and it contains no full 3-torsion, because the dual isogeny maps
E'[3] onto mu_3, and mu_3 meets <P> trivially (the rational 3-torsion line is not mu_3). So this is a
rational cyclic 27-isogeny, and over Q that forces CM.

**Action:** replace "we have not proved" by this argument; D <= 2 then follows from the first bound.
Confidence: high (checked twice).

### 18. Proof of Theorem thm:main: the case of an I_n^* prime at q = 2 is not covered

The proof handles additive potentially multiplicative primes through Lemma lem:twist, which is for odd q
only. A prime q = 2 of type I_n^* with v_2(j) < 0 (so t_l(E, 2) may be positive) needs a separate local
argument: over the ramified quadratic extension that makes the reduction multiplicative, the Tamagawa
computation of Lemma lem:tamfactor applies to ad T, which is unchanged by the twist. **Action:** add that
case. Confidence: high, as reported.

### 19. Lemma lem:ddt417: wp intersect I = 0 is used without proof (harmless)

The proof uses wp intersect I = 0, where wp = ker pi and I = Ann(wp). This needs a short argument, and it
is NOT "because T is reduced": the full Hecke algebra can contain nilpotents (U_p has a Jordan block at
eigenvalue 0, for example U_2 at level 88 on the span of f_11(z), f_11(2z), f_11(4z), f_11(8z)). The correct
argument: take t in I with pi(t) = eta. For x in wp intersect I, tx = 0 (as t kills wp) and
(pi(t) - t)x = 0 (as pi(t) - t lies in wp and x kills wp). So eta x = 0, and x = 0 when eta is nonzero
because T is torsion-free. When eta = 0 the lemma is trivial. **Action:** add these two lines.
Confidence: high. (Corrected after the Chapter 3 outline: an earlier version of this note gave the wrong
reason.)

### 20. Theorem thm:qual, cases (b) and (c): "g = h tensor chi" is not literally right

h tensor chi is the q-depletion of g, not g itself, since a_q(h) = 0. The conclusion h != f still follows,
by strong multiplicity one. **Action:** rephrase. Confidence: high, as reported.

### 21. The example 980i1 lies outside the hypotheses of Theorem thm:qual

980 = 2^2 * 5 * 7^2, so l = 5 divides N. The example illustrates the congruence, not the theorem.
**Action:** say so.

### 22. Remark rem:types groups the additive types incompletely

Some types are listed under the wrong description of the inertia image mod 3. **Action:** see the outline's
item A2.3 for the corrected grouping. Confidence: high, as reported.

### 23. Section sec:tam: c_q means two things

c_q is the Tamagawa number elsewhere in the paper, but sec:tam uses it for the class of the unit part of
the Tate parameter. **Action:** rename the class, for example to c(u).

### 24. The abstract calls the thm:quant argument "elementary"

The outer inequality of Theorem thm:quant is elementary, but the middle term uses multiplicity one at
level N_S (Lemma lem:hecke in the free case). **Action:** reword. Confidence: high, as reported.

### 25. The abstract's wording on "every optimal curve" and "a third of the cases"

These overstate slightly what the tables show (optimality is determined only up to 400000 and for some
classes beyond; the violation rates are 31%, 23% and 18%, not one third). **Action:** reword. Confidence:
medium.

### 26. Section 4.2: M_{f,lambda} is homothetic to the dual of T_l E, not to T_l E

H^1 of X_0(N) gives the dual of the Tate module. The adjoints agree up to the trace-form isomorphism, so
nothing breaks. **Action:** say "the dual of T_l E", or note that ad is insensitive to dualising.
Confidence: medium-high (depends on DFG04's normalisation of M_{f,lambda}).

### 27. Observation: optimality plays no role at l when E[l] is irreducible

Isogenous curves are linked by isogenies of degree prime to l in that case, so v_l(deg) does not depend on
which curve of the class is optimal. Not an error; worth one sentence.

### 28. Lemma lem:twist, proof: "the conductor exponents are the standard ones for q odd (tame)"

At q = 3 a general additive curve can be wildly ramified, so "tame" is wrong in general. It is right for
the exchanges the lemma actually lists. **Action:** restrict the remark. Confidence: high, as reported.

## From the Chapter 2 outline (rings, finite fields, characters, valuations)

Source: `outlines/ch02_rings.md`, final section. Points 29 and 30 were also checked independently by the
orchestrating session; points 31 and 32 are as reported by the outline agent. None changes a result.

### 29. Lemma lem:twist (ii), proof: the invariants of the twist are those of the twist by q, not q*

The proof says the twist has invariants q^2 c_4, q^3 c_6, q^6 Delta. A twist by d scales c_4, c_6, Delta by
d^2, d^3, d^6, so these are the invariants of the twist by q. The twist by q* (the one the lemma is about)
has (q*)^2 c_4, (q*)^3 c_6, (q*)^6 Delta; the two differ in the sign of c_6 when q = 3 mod 4, that is, by the
twist by -1, which is ramified at 2. Only q-adic valuations are used, so the argument is unaffected.
**Action:** write q* for q. Confidence: high (checked twice).

### 30. Introduction: the naive adjoint L-function is not the Euler product of sum a_n^2 n^{-s}

The introduction says the naive adjoint L-function is "the Euler product of sum a_n(f)^2 n^{-s}". At a good
prime p, sum_k a(p^k)^2 X^k = (1 + pX) / ((1 - alpha^2 X)(1 - pX)(1 - beta^2 X)), so the Rankin series has an
extra factor (1 + p^{1-s}) compared with L_p(Sym^2 f, s). Globally,
sum a_n^2 n^{-s} = L^{nv}(Sym^2 f, s) zeta^{(N)}(s - 1) / zeta^{(N)}(2s - 2), up to the factors at the bad
primes. **Action:** say "the Euler product of zeta^{(N)}(2s - 2) sum a_n(f)^2 n^{-s} / zeta^{(N)}(s - 1)", or
define the naive factor directly by the local formula (as Section 1.1 already does). Confidence: high
(checked twice). This belongs to Chapter 19's area; the Chapter 19 writer must state it correctly.

### 31. Lemma lem:tamfactor, statement: "the class of u in F_q^x"

u = q_E q^{-n} lies in Z_q^x; what is meant is the class of its reduction in F_q^x / (F_q^x)^{l^v}, with
v = v_l(q - 1). Identifying that quotient with Z/l^v needs a choice of generator; v_l(c) does not depend on
the choice, and v_l(0) must be read as v. **Action:** say "the reduction of u" and fix the reading of
v_l(0). Expository; confidence high.

### 32. Notation: chi_q (quadratic, conductor q) versus chi_l (cyclotomic)

The paper uses chi_q for the quadratic character of conductor q and chi_l for the l-adic cyclotomic
character, so chi_3 is ambiguous. It also names the same character both chi_11 and chi_{-11}.
**Action:** use chi_{q*} or psi_q for the quadratic character. Expository; low importance.

## From the Chapter 4 outline (representations, lattices, the adjoint)

Source: `outlines/ch04_reps.md`, final section. Both points were also checked independently by the
orchestrating session. Neither changes a result.

### 33. Proposition prop:ns and Lemma lem:h0: "rhobar = Ind psi" holds only over F_9

In the N_s(F_3) case the determinant-one image is C_4, generated by [[0, 1], [-1, 0]], whose characteristic
polynomial X^2 + 1 is irreducible over F_3. So the restriction of rhobar to Gal(Qbar/Q(sqrt(-3))) is
irreducible over F_3 (no stable F_3-line) and only becomes psi + psi^{-1} over F_9; psi takes values in F_9.
"rhobar = Ind psi" and "induced from Gal(Qbar/Q(sqrt(-3)))" are statements about rhobar tensor F_9.
**Action:** write rhobar tensor F_9 = Ind psi; the isomorphism rhobar = rhobar tensor chi_{-3} then descends
to F_3 (an isomorphism of F_3-representations exists once one exists over F_9). Confidence: high (checked
twice).

### 34. Lemma lem:euler, types III and III*: "the diagonal element" may not exist over Q_l

The image of inertia is generated by tau of order 4 with eigenvalues i and -i. When l = 3 mod 4, i is not
in Q_l, so tau is not diagonalisable over Q_l and there is no "diagonal element". The invariant line of
ad V is spanned by tau itself (it commutes with tau and has trace 0). Frobenius acts on it by chi_{-4}(q),
as the paper says. **Action:** replace "the diagonal element" by "tau". Confidence: high (checked twice).

## Book-internal consistency (not about the paper)

### B1. Chapter 21 outline, convention C2: which Frobenius has eigenvalues alpha, beta

On V_l E the **arithmetic** Frobenius has characteristic polynomial X^2 - a_p X + p, eigenvalues alpha and
beta. The geometric Frobenius has these eigenvalues on the dual H^1 = V_l E^vee. The Chapter 21 outline
says the geometric Frobenius on V_l E has eigenvalues alpha, beta, which is a slip. On ad V the eigenvalues
alpha/beta, 1, beta/alpha are the same for both conventions, so no number changes. **Action:** the
Chapter 19 and 21 writers must state this correctly. Found by the Chapter 4 outline agent; checked by the
orchestrating session.

## From the Chapter 3 outline (modules, Fitting ideals, pairings, Hecke-type algebras)

Source: `outlines/ch03_modules.md`, final section. Point 35 was also checked independently by the
orchestrating session; the others are as reported by the outline agent. The agent's first point corrected
point 19 above. None changes a result.

### 35. Lemma lem:hecke: the other local factors lie in the kernel, not in the annihilator

The proof says "the other local factors of T tensor Z_l are killed by phi_f and lie in the annihilator".
They lie in ker phi_f = wp, but not in Ann(wp) in general: if e' is the idempotent of another local factor,
e' wp = wp intersect T_{m'}, which is usually nonzero. The conclusion, that the congruence ideal can be
computed in T_m, is still right, because phi_f factors through the projection to T_m and the annihilator
of wp decomposes along the idempotents. **Action:** replace "lie in the annihilator" by "lie in the kernel,
and Ann(wp) is the annihilator of wp_m inside T_m". Confidence: high (checked twice).

### 36. Lemma lem:hecke and Theorem thm:quant Step 2: why the pairing stays perfect on the m-component

Both proofs apply Lemma lem:ddt417 to L = H^1(X_0(N), Z_l)_m with the pairing delta-hat, which needs that
pairing to be perfect on the m-component. One sentence fixes it: the idempotent e_m is self-adjoint for
delta-hat (all Hecke operators are), so H^1 splits orthogonally into its local components and the pairing is
perfect on each. **Action:** add that sentence. Confidence: high, as reported.

### 37. Section 1.2: the placement of the G_{Q_p} superscript in the definition of Tam_p

The display reads as Fitt(H^1(I_p, M)_tor)^{G_{Q_p}}, that is, as invariants of an ideal. What is meant is
the Fitting ideal of the invariants: Fitt_{Z_l}( (H^1(I_p, M)_tor)^{G_{Q_p}} ). **Action:** move the
parenthesis. Notation only.

### 38. Lemma lem:ddt417: orders versus lengths

The lemma is stated for an arbitrary DVR O but counts #O/Delta and #(O/eta)^d, which are finite only when
the residue field is finite. For O = Z_l (the only case used) this is fine. **Action:** state it with
lengths, or for O with finite residue field. Low importance.

## Book-internal consistency (continued)

### B2. Jordan-Holder is proved in both Chapter 3 and Chapter 4

Chapter 3 needs Jordan-Holder for the length of a module over a local ring and proves it (the proof works
over any ring); PLAN.md and the Chapter 4 outline also place it in Chapter 4. **Action:** keep the proof in
Chapter 3 and let Chapter 4 cite it for composition factors of representations.

## From the Chapter 8 outline (curves, Jacobians, cup product, correspondences)

Source: `outlines/ch08_curves.md`, final section. Point 39 was also checked independently by the
orchestrating session; points 40 and 41 are as reported by the outline agent.

### 39. Lemma lem:hecke is always an equality: the multiplicity-one hypothesis in Theorem thm:main is not needed (SIGNIFICANT)

For the X_0(N)-optimal curve E, the kernel of J_0(N) -> E is connected, so phi_*: H_1(X_0(N), Z) -> H_1(E, Z)
is surjective and the image of phi^*: H^1(E, Z_l) -> H^1(X_0(N), Z_l) is a saturated rank-two sublattice
on which the Hecke algebra acts through phi_f. Hence it is exactly M_{f,lambda} = H^1(X_0(N), Z_l)[wp].
By the projection formula, the cup product on it is <phi^* a, phi^* b> = <a, phi_* phi^* b> = deg(phi_E) <a, b>_E,
and the cup product on H^1(E, Z) is unimodular. The pairing delta-hat composes the cup product with w_N,
which acts on M_{f,lambda} by the Atkin-Lehner sign of f, plus or minus 1. So the Gram determinant of
delta-hat on M_{f,lambda} is (deg phi_E)^2 up to a unit, and

    v_lambda(eta^empty_{f,lambda}) = v_l(deg phi_E)    for every l not dividing 2N, with no freeness hypothesis.

Consequences, if DFG04's eta is normalised as the paper describes it (Section 4.1):

* Lemma lem:hecke becomes v_l(deg phi_E) = v_l(eta^empty) unconditionally; the comparison with r_E is then
  the theorem of Agashe-Ribet-Stein.
* The identity (eq:identity) of Theorem thm:main holds **with equality** whenever l is not in S_f: the
  phrase "with equality when H^1(X_0(N), Z_l)_m is free over T_m" can be dropped, and Remark rem:free is not
  needed for it.
* Step 4 of the proof of Theorem thm:quant likewise needs no freeness (apply the same argument to the
  optimal curve in the class of g); this partly answers point 24.

This is a classical fact in another guise (the modular degree is the index computed from the intersection
pairing on the image of H^1(E)). **Action:** state it as a lemma, which both simplifies and strengthens
the paper. Confidence: high for the mathematics (checked twice); medium on the exact normalisation of
eta in DFG04, which should be checked against DFG04 Sections 1.6 and 1.7 before the paper is changed.

**Status update (from the Chapter 20 outline): CONFIRMED against DFG04.** The agent read the published
DFG04 (Ann. Sci. ENS 37 (2004), Numdam) and checked the five items of point 56: all hold in the form the paper
needs. So point 39 stands with DFG04's own eta: Lemma lem:hecke is an equality, and (eq:identity) of Theorem
thm:main is an equality whenever l is not in S_f. See point 73.

### 40. Supplement to point 26: M_{f,lambda} for the optimal curve, exactly

For the optimal curve, phi^* identifies M_{f,lambda} with H^1(E, Z_l) = Hom(T_l E, Z_l), which is
T_l E(-1) as a G_Q-module (via the Weil pairing). This is an equality, not just a homothety, and needs no
irreducibility of rhobar. Since ad is insensitive to dualising and twisting, A_f = ad T in the paper is
right. Confidence: high, as reported.

### 41. Remark rem:free: the Tate module versus H^1 as Hecke modules (expository)

Identifying T_l J_0(N) with H^1(X_0(N), Z_l) as Hecke modules uses Poincare duality composed with w_N; the
resulting identification is not Galois-equivariant. Freeness over T_m still transfers. **Action:** one
clarifying clause. Low importance.

## Book-internal consistency (continued)

### B3. Chapter 21 outline, items A4.4 and A4.6, need updating

A4.4 still says the other local factors lie in the annihilator (corrected to the kernel in point 35), and
A4.6 says M_{f,lambda} is homothetic to T_l E, contradicting its own A4.1 and points 26 and 40. Both must be
fixed when Chapter 21 is written; point 39 also changes how A4 should present Lemma lem:hecke.

### B4. The symbol * is overloaded

Chapter 3's outline uses * for adjoints, Chapter 4 and the paper use it for Pontryagin duals, and Chapter 8
needs it for pullbacks of divisors and cohomology. The Chapter 8 outline uses A^dagger for adjoints.
**Action:** Appendix B must fix one convention for the whole book.

### B5. The Chapter 3 outline lists Chapter 8 as a user of Gorenstein rings

It is not; the users are Chapters 14 and 20. Fix when Chapter 3 is written.

## From the Chapter 7 outline (local fields, inertia, Weil-Deligne representations)

Source: `outlines/ch07_local.md`, final section. Point 42 was also checked independently by the
orchestrating session. Point 43 is an unverified observation, recorded as an open question.

### 42. Lemma lem:tamfactor, proof: the nonsplit case needs eps kappa, not kappa, in the corner

The proof writes the action of G_{Q_q} on T as [[chi_l eps, kappa], [0, eps]] with kappa the Kummer class of
the Tate parameter. For this to be a homomorphism the corner c must satisfy
c(gh) = chi_l eps(g) c(h) + c(g) eps(h). The Kummer cocycle satisfies kappa(gh) = kappa(g) + chi_l(g) kappa(h),
so c = kappa works only when eps is trivial, while c = eps kappa always works: the nonsplit curve is the
Tate curve twisted by eps, and [[chi_l, kappa], [0, 1]] tensor eps = [[chi_l eps, eps kappa], [0, eps]].
**Action:** write eps kappa. Nothing changes: eps is trivial on inertia, so the inertia computation is
untouched, and at Frobenius c' only changes by the sign eps(Frob), which does not affect v_l(c').
Confidence: high (checked twice).

### 43. Proposition prop:forms: the exception (type IV or IV* at 2, l = 3) is a theorem (SETTLED)

The proof of Lemma lem:euler uses q >= 5 only to know that the image of inertia is cyclic and tame. For
types IV and IV* at q = 2 this holds too, so the exception in Proposition prop:forms disappears.

Proof (from the Chapter 11 outline, checked by the orchestrating session): for additive reduction at q
not equal to l, the formal group and the additive group G_a have no l-torsion and E_0(Q_q^ur) is
l-divisible, so E[l^k]^{I_q} is isomorphic to the l^k-torsion of the geometric component group. For types
IV and IV* the component group is Z/3, so inertia fixes a line of E[3]; its determinant is trivial on
inertia, so its image in GL_2(F_3) is unipotent of order 3. Reduction mod 3 is injective on finite
subgroups of GL_2(Z_3) (the kernel of GL_2(Z_3) -> GL_2(F_3) is torsion-free), so the image of inertia on
T_3 E is cyclic of order 3, prime to 2, hence tame; for potentially good reduction the image is the same
for every l not equal to 2. The computation of Lemma lem:euler then gives the invariant line of ad V with
Frobenius eigenvalue chi_{-3}(2) = -1, so P_2(X) = 1 + 2X and e_3(E, 2) = v_3(3/2) = 1.

Consequences: Proposition prop:forms holds with no exception, and case (a) of Theorem thm:qual extends
from q >= 5 to q = 2 (the Serre conductor of rhobar_{E,3} has exponent 1 at 2). Checked on all 4,750
curves of conductor below 10,000 with type IV or IV* at 2 (inertia mod 3 of order 3 with a fixed line,
f_2 = 2; P_2 = 1 + 2X on more than 60 sampled curves with PARI). **Action:** replace the exception and the
appeal to the 92,812 curves by this argument. Confidence: high (checked twice).

## Book-internal consistency (continued)

### B6. PLAN.md states the Weil-Deligne relation in the geometric form

PLAN.md, Chapter 7 entry, writes "Frob N Frob^{-1} = p^{-1} N", which is the relation for the geometric
Frobenius. The book's Frob is arithmetic, for which Frob N Frob^{-1} = p N. The Chapter 7 outline states
both forms and fixes the book's convention: Frob arithmetic, Phi = Frob^{-1} geometric, and
L(V, s) = det(1 - Phi q^{-s} | V^I)^{-1}.

### B7. Chapter 21 outline, convention C2(b) and item A2.7

C2(b) still contains the slip of B1, and it gives det(1 - Phi p^{-s} | V_l E)^{-1} as the Euler factor of
E. With the geometric Frobenius that is L_p(E, s + 1); the Euler factor L_p(E, s) comes from the dual
V_l E^vee = H^1. Item A2.7, step (1), repeats the kappa versus eps kappa issue of point 42. Fix both when
Chapter 21 is written.

## From the Chapter 9 outline (elliptic curves over fields)

Source: `outlines/ch09_ellcurves.md`, final section. Point 45 was also checked independently by the
orchestrating session; point 44 is as reported by the outline agent. Both are expository. The Chapter 9
outline proves point 17 in full (its item 9.8) and corrected the curve in point 15.

### 44. Section sec:eis: "3Cs.1.1, the split Cartan image" is the wrong description

3Cs.1.1 is the order-2 subgroup {diag(1, 1), diag(1, -1)} of the split Cartan subgroup: the image exactly
when E[3] = Z/3 + mu_3. The full split Cartan image has the label 3Cs. **Action:** say "the subgroup of the
split Cartan subgroup that fixes a point", or simply "E[3] = Z/3 + mu_3". Confidence: high, as reported
(checked against ecdata's image labels).

### 45. Lemma lem:twist (ii), proof: the cubic of the twisted model (addendum to point 29)

For the twist y^2 = x^3 + q* a_2 x^2 + (q*)^2 a_4 x + (q*)^3 a_6, the cubic that Tate's algorithm produces
after removing powers of q is T^3 + e a_2 T^2 + e^2 a_4 T + e^3 a_6 = T^3 + e a_2 T^2 + a_4 T + e a_6, with
e = q*/q = plus or minus 1, not T^3 + a_2 T^2 + a_4 T + a_6. Its roots are e times those of the original
cubic, so "distinct roots modulo q" is unaffected. **Action:** write the cubic with e, or note the sign.
Confidence: high (checked twice).

## Book-internal consistency (continued)

### B8. Curve-level twists within isogeny classes

Point 15 (now corrected) and parts of the Chapter 21 outline pair the wrong curves within an isogeny class.
The twist of 11a1 by -11 is 121d2 (type I_5^*); 121d1 is the twist of 11a3 (type I_1^*). The twist of 11a1
by -7 is 539d2, and the twist of 121a1 by -11 is 121c2. Every quantity used at l = 3 depends only on the
class, so no conclusion changes, but Chapter 21 must name the right curves.

### B9. Chapter 21 convention C2(b) (extends B1 and B7)

The Euler factor det(1 - Phi p^{-s} | V_l E)^{-1} with Phi geometric is L_p(E, s + 1); L_p(E, s) comes from
the dual H^1 or from the arithmetic Frobenius on V_l E. Fix when Chapter 21 is written.

## From the Chapter 12 outline (modular forms and modular curves)

Source: `outlines/ch12_modforms.md`, final section. No errors in the paper were found in this area. The
agent installed PARI/GP 2.17 through the Python package cypari2, so PARI is now available in this
environment for later checks.

### 46. Optional strengthening: the congruences in the Example of Section 3 hold for every n

The Example after the proof of Theorem thm:qual checks the congruences between 121a1 and the twist of 11a1,
539c1 and the twist of 11a1, and 980i1 and the twist of 20a1, for primes p below 500 or 1000, excluding a few
primes. In each case both forms lie in the same space S_2(Gamma_0(N)), so Sturm's bound (22, 112 and 336
respectively) turns the finite check into a proof of the congruence for every n, including the excluded
primes. **Action:** optional; say "for all n, by Sturm's bound". Confidence: high, as reported (checked
with PARI's mfsturm).

## Book-internal consistency (continued)

### B10. The Manin constant was on the wrong side of the Zagier-Watkins formula (fixed)

PLAN.md (Chapter 14 scope) and the Chapter 9 outline wrote deg phi_E = 4 pi^2 <f, f> / (c^2 vol(Lambda_E)).
With phi^* omega_E = c 2 pi i f dz, integrating |phi^* omega_E|^2 over X_0(N) gives
deg phi_E vol(Lambda_E) = c^2 4 pi^2 <f, f>, so c^2 belongs in the numerator. Check: in class 11a the degree-5
parametrisation of 11a3 has volume ratio 25, so c = 5. Both files are now corrected. No number in the paper
changes, since c = 1 for optimal curves of the tables. The Chapter 12 outline also verified the formula
numerically for 11a1, 20a1, 37a1, 99a1 and 121a1 with the unnormalised Petersson product (PARI's
mfpetersson divides by the index of Gamma_0(N)).

### B11. "S_2(Gamma_0(N); Z) is a lattice" is in both the Chapter 12 and Chapter 13 scopes

Resolved by the Chapter 12 outline: Chapter 12 states Shimura's integral-basis theorem and proves its
consequences; Chapter 13 cites them and proves the perfect pairing with the Hecke algebra.

### B12. Chapter 21 outline, item A3.2

It contains a sentence about adjoints that corrects itself midway; clean it up when Chapter 21 is written.

## From the Chapter 11 outline (Galois representations of elliptic curves)

Source: `outlines/ch11_galrep.md`, Part 7. The agent's first point settled point 43 (rewritten above).
Point 47 was also checked independently by the orchestrating session; points 48 and 49 are as reported,
checked by the agent with PARI on Cremona's tables below conductor 10,000.

### 47. The hypothesis l not in S_f is automatic for l >= 5 not dividing N, given E[l] irreducible

If l >= 5, l does not divide N and E[l] is irreducible, then rhobar is absolutely irreducible on
Gal(Qbar/Q(sqrt(l*))). Otherwise rhobar = rhobar tensor chi_{l*}; restrict to inertia at l, where E has good
reduction: in the ordinary case rhobar|I_l has characters {omega, 1}, in the supersingular case {omega_2,
omega_2^l}, and chi_{l*}|I_l = omega^{(l-1)/2}. Matching the twisted characters with the untwisted ones
forces l = 3 in both cases. For l = 3 the hypothesis fails exactly for image 3Ns, whose curves are
ordinary at 3. So, for l not dividing 2N, "l not in S_f" is equivalent to "E[l] irreducible and h_l(E) = 0".
Consequences: the clause in Section sec:forms about curves "induced from Q(sqrt(l*)) with l >= 5, which we
did not single out" concerns only curves with l dividing N; the hypothesis of Theorem thm:main can be
restated more simply. Probably known in the literature; no citation found yet. Confidence: high (checked
twice).

### 48. Section sec:anomaly: the observations on 3Ns curves are theorems

Every curve with image 3Ns has a prime p other than 3 at which inertia acts through a cyclic group of order 4;
for p >= 5 this means type III or III* with p = 1 or 11 mod 12, and in every case e_3(E, p) >= 1. Every
multiplicative prime other than 3 has 3 dividing n_p. Checked on all 120 3Ns curves below conductor
10,000 (100 with such a prime p >= 5, the other 20 with p = 2). **Action:** state these as a proposition
instead of as observations. Confidence: high, as reported.

### 49. Remark rem:types: "lowers the conductor exponent" (addendum to point 22)

The statement is true for the Serre conductor exponent of rhobar_{E,3}, but not for the conductor of E in
the type II case. **Action:** say "the Serre conductor exponent of rhobar_{E,3}". Confidence: high, as
reported.

## Book-internal consistency (continued)

### B13. Stale hedges on type IV at 2 and on chi_{l*} for l >= 5

The Chapter 7 and Chapter 21 outlines still treat the type IV at 2 case as open (now settled, point 43).
Point 6 and the Chapter 21 outline say "rhobar = rhobar tensor chi_{l*} can occur" for l >= 5 without noting
that this needs l to divide N (point 47). PLAN.md's Chapter 11 entry repeats the paper's flawed finiteness
argument for h_l (point 5). Fix when those chapters are written.

### B14. Bibliography keys planned in several chapters (decision)

SerreTate68 is planned in the Chapter 7, 9 and 11 bib files. main.tex reads all chapter bib files, so a key
defined twice gives a BibTeX "Repeated entry" error. **Decision:** any reference needed by more than one
chapter goes into refs.bib, not into a chapter bib file. Writers must check refs.bib and the other chapter
bib files before adding a key.

### B15. Possible overlap between Chapters 10 and 11 on the Tate curve

Chapter 11 uses the Tate curve as a black box from Chapter 10 and proves Lemma lem:tamagawa-exp from it.
When the Chapter 10 outline lands, check that it does not also prove lem:tamagawa-exp.

## From the Chapter 10 outline (reduction, Kodaira types, Tate curves)

Source: `outlines/ch10_reduction.md`. The outline gives a second, independent proof of point 43 (via the
conductor: types IV and IV* at 2 have conductor exponent 2, by Dokchitser-Dokchitser 2015, Theorem 3.1,
hence tame reduction, and the inertia image is cyclic of order exactly 3), checked on all 14,431 curves of
these types below conductor 30,000. Point 50 was also checked independently by the orchestrating session
with PARI; points 51 to 53 are as reported.

### 50. Remark rem:wild and Section sec:wild: "a type II at 2 has P_2 = 1 and e_3 = 0" is false in general

PARI, checked by the orchestrating session:

| Curve | Type at 2 | P_2(X) | e_3(E, 2) | modular degree |
|-|-|-|-|-|
| 336f1 | II | 1 + 2X | 1 | 24 |
| 1232l1 | II* | cubic, -8X^3 - 4X^2 + 2X + 1 | 2 | 288 = 2^5 3^2 |

Among optimal non-CM curves below conductor 10,000 (outline agent's count): type II at 2 has P_2 = 1 for
1,092 curves, 1 + 2X for 371 and a cubic for 74; type II* has 514, 74 and 191. Likewise "a type I_n^* at 2
with potentially good reduction has a cubic P_2" holds only in a minority of cases (876 with P_2 = 1, 111
cubic, 8 with 1 + 2X). (Correction from the memo: these counts are for conductor below 5,000; below
10,000 they are 2,043 with P_2 = 1, 269 cubic, 22 with 1 + 2X, and the potentially good share is 58%, not 61%.) The paper's rule and tables use PARI's factor at 2, so **no theorem or count changes**;
only the illustrative sentences are wrong, and 1232l1 is a nice example where the bound of Theorem thm:main
at l = 3 is attained by the prime 2 alone. **Action:** replace the two sentences by "the Kodaira type at 2
does not determine P_2; for instance ...". Confidence: high (checked twice).

### 51. Optional: the type exchanges also hold at q = 3

The exchanges II <-> IV*, III <-> III*, IV <-> II* under the twist by Q(sqrt(-3)) also hold at q = 3, with
the conductor exponent unchanged; true for all 5,122 such pairs below conductor 10,000. Lemma lem:twist (ii)
states them only for q >= 5. Optional strengthening; one step of the sketched proof needs a reference.

### 52. Appendix: the PARI Kodaira codes n + 4 and -(n + 4) are valid only for n >= 1

I_0 has code 1 and I_0^* has code -1, not 4 and -4. Low importance.

### 53. Definition def:terms is for q != l, but (eq:rule) and rule(E, l) use t_l at q = l

For example 726a1 at q = l = 3. **Action:** extend the definition of t_l(E, q) to q = l (the formula
v_l(-v_q(j_E)) makes sense there), or say so. Expository.

## Book-internal consistency (continued)

### B16. Errors and leftovers in other outlines found by the Chapter 10 outline

* Chapter 7 outline, Exercise 10 and its verification log: the coefficient of j^{-3} in q(j) is 750420, not
  356652 (q = j^{-1} + 744 j^{-2} + 750420 j^{-3} + ...).
* Chapter 11 item 2.2 duplicates Chapter 10 item 4.5 (E[l^k]^I = Phig[l^k]); Chapter 11 should cite 4.5.
* Chapters 7 and 21 still treat type IV at 2 as open, and Chapter 7 allows order 6 there, which never
  happens. Chapter 21 item A2.6 repeats the false "type II at 2 has P_2 = 1" (point 50).
* PLAN.md's "Kraus's conditions at 2 and 3" are Kraus 1989 (Acta Arith. 54), not Kraus90. PLAN.md's key
  TateAlgorithm does not exist; the algorithm is Tate75 in refs.bib.
* Following B14, SerreTate68, DokDok15, KramerTunnell82, Lorenzini10 and Papadopoulos93 belong in refs.bib.

## From the Chapter 15 outline (Galois representations of modular forms, level lowering)

Source: `outlines/ch15_modgalrep.md`, final section. Point 54 was also checked independently by the
orchestrating session with PARI; point 55 is as reported. Both are low importance. The outline adds a worked
example for case (a) of Theorem thm:qual at q = 2 (point 43): 52a1 has type IV* at 2, its mod 3 Serre
conductor is 26, and g = f_26b - f_26b(2z) is congruent to f_52a mod 3. On the tables, all 1,051 curves
labelled "1" below conductor 10,000 with type IV or IV* at 2, 3 not dividing N, and mod 3 image neither
reducible nor 3Ns have 3 dividing the modular degree.

### 54. Theorem thm:qual, case (c): "f' = f tensor chi is a newform on Gamma_0(N/q)" (companion to point 20)

E has type I_n^* at q, so a_q(f) = 0 and f tensor chi has a_q = 0. But E' = E^(q) is multiplicative at q,
so its newform has a_q = plus or minus 1. Hence f tensor chi is the q-depletion of f_{E'}, not f_{E'}.
Check: 539c1 twisted by -7 is in class 77c, and 77c1 has type I_3 at 7 with a_7 = -1 (PARI). **Action:**
write f' = f_{E'}; the step h != f then follows by strong multiplicity one, as in point 20. Confidence: high
(checked twice).

### 55. Remark after the Example in Section 3: the obstruction at q = 3 is q = l, not wildness

The remark says the data show the conclusion "at q = 3 in cases (a) and (b), where Lemma lem:IV does not
apply because the ramification is wild". In those cases q = l = 3, so 3 divides N and the curves are outside
Theorem thm:qual anyway. **Action:** say "where q = l". Expository.

## Book-internal consistency (continued)

### B17. Who proves Lemma lem:crit (decision)

PLAN.md's Chapter 14 entry says Chapter 14 or 20, its Chapter 15 entry says 15, and the Chapter 21 outline
says both 15 and 20. **Decision:** Chapter 15 proves lem:crit in full (its outline Section 8); Chapter 14
states the congruence number and cites it; Chapter 20 restates it. The Chapter 14 agent has been told.

### B18. Further items for the Chapter 21 revision pass and for refs.bib

* Chapter 21 item A3.5, case (c), repeats point 54 and its h != f argument contradicts itself; item A1.10
  still states case (a) of thm:qual for q >= 5 only (point 43).
* Chapter 11 says Chapter 15 proves DDT Theorem 3.15; Chapter 15 states it and proves only the
  specialisation to rhobar_{E',l}.
* By decision B14, Rohrlich94 and Deligne73 (planned by Chapter 7) and Livne89 (planned by Chapter 11)
  belong in refs.bib. The twist of 20a1 by -7 is 980g2 (addition to B8).

## From the Chapter 14 outline (modular curves over Q, Jacobians, the modular degree)

Source: `outlines/ch14_moddeg.md`, Section 9 and final section. The outline proves point 39 in full (its
items 9.1 to 9.5). Point 57 is as reported by the outline agent (data checked; the exact published
statement of Calegari-Emerton not checked).

### 56. Refinement of point 39: what it proves, and the checklist against DFG04

From the outline's Section 9:

* For the optimal curve and **every** prime l, the pairing delta-hat on M_{f,l} = phi_E^* H^1(E, Z_l) has
  ideal of values deg(phi_E) Z_l and Gram determinant deg(phi_E)^2. No irreducibility of rhobar and no
  multiplicity one is used. Corollary: deg(phi_E) divides r_E at every prime (with Chapter 3's algebra).
* Lemma lem:hecke is therefore an equality, the identity (eq:identity) of Theorem thm:main is an equality
  whenever l is not in S_f, and Step 4 of Theorem thm:quant needs no freeness. Remark (2) after Theorem
  thm:quant still needs multiplicity one, because the depleted form g^S is not attached to an optimal
  quotient.
* Example: at 99a1 and l = 3 (outside the paper's hypotheses since 3 divides N), deg = 4 and r = 12, so the
  inequality of Lemma lem:ddt417 is strict and H^1(X_0(99), Z_3)_m is not free over T_m.

**Checklist before changing the paper** (what DFG04 must be confirmed to say):
1. that their integral structure is H^1(X_0(N), Z_l), and not the trivial-character part of a
   Gamma_1(N)-type cohomology (in which case the pairing scales by #(Z/N)^x/{1, -1}, which l can divide);
2. that their "interior" cohomology is H^1(X_0(N)) (proved in the outline);
3. that [UwU]omega is w_N with no scalar, and how H^2_c is normalised (elliptic points of order 3 matter
   at l = 3);
4. that M_{f,lambda} is the kernel lattice, not the projection lattice;
5. that eta is the ideal of values of the pairing on M_{f,lambda}.

### 57. Section sec:two: the paraphrase of Calegari-Emerton fails for CM curves

The paper says a curve of odd modular degree has at most two odd bad primes and a rational 2-torsion point
or prime conductor. 27a1 and 243b1 have odd modular degree, torsion Z/3 (no 2-torsion) and non-prime
conductor; both have CM (j = 0). So either the published theorem excludes CM curves or has extra cases, and
the paraphrase should say so. **Action:** check the exact statement of CalegariEmerton09 and add the
hypothesis or exceptions. Confidence: high on the data, medium on the published statement.

### 58. A second example for the remark on l dividing N

726a1 has congruence number r = 1584 = 11 * 144 and modular degree 144 (computed with PARI), so it is a
second instance where r and deg differ, at l = 11 (121 divides 726). It could be added next to 99A1.
Optional.

## Book-internal consistency (continued)

### B19. Items from the Chapter 14 outline

* The Chapter 21 outline's dependency diagram and hypothesis table still route the equality in thm:main
  through Remark rem:free (superseded by points 39 and 56).
* The Chapter 9 and 21 outlines say r(99A1) was "not recomputed" or "as cited"; it is now recomputed (12),
  and they can cite Chapter 14.
* Chapter 15's item 2.6(ii) duplicates point 40; Chapter 14 proves it (item 9.1), Chapter 15 cites it.
* DeligneRapoport73, KatzMazur85, Ogg73 and Kenku are needed by more than one chapter and belong in refs.bib
  (B14); the existing key Ogg is Ogg's 1967 paper, not the 1973 paper on cusps.
* PLAN.md's Chapter 14 entry has an unfinished "Mazur: c | ..." placeholder and still says lem:crit is
  proved "here or in Chapter 20" (decided in B17: Chapter 15).
* Ribet-Takahashi is stated in both Chapters 14 and 15; keep the statement in Chapter 14 and cite it.
* Chapter 20 should cite Chapter 14's items 9.3, 9.5, 9.6 and 10.3 rather than re-derive them.

## From the Chapter 13 outline (Hecke operators, newforms, twists)

Source: `outlines/ch13_hecke.md`, final section. No errors in the paper were found in this area. The points
below are optional strengthenings and one expository fix, as reported by the outline agent with PARI checks.
The agent also computed the Hecke algebra over Z at ten levels from 11 to 539 (rank d and a perfect pairing of
determinant plus or minus 1 at every one) and recomputed r(99a1) = 12 against degree 4, as in the paper.

### 59. Optional: Step 1 of the proof of Theorem thm:quant is an equality

The twist map iota sends f to g^S and maps f^perp into the T-stable complement of g^S, and conversely, so
v_l(r_E) = v_l(eta^Hecke(g^S)), not just >=. Matches the computed Hecke congruence modules at level 539 (orders
288 and 504) at every prime. Confidence: high, as reported.

### 60. Optional: the restriction q >= 5 in Theorem thm:quant is not needed

The argument works for every odd q in S of type I_0^* or I_n^* (the twist lemma for I_n <-> I_n^* and I_0 <->
I_0^* holds for every odd q). PARI's Euler factor P_3 agrees with the twist formula on all 1,100 curves
checked, and the bound held in all 388 cases with type I_0^* at 3. **Action:** replace q >= 5 by q odd, after
checking the Euler-factor formula at q = 3 in the proof. Confidence: high, as reported.

### 61. Theorem thm:quant, Step 1: use the T-stable complement, not the Petersson complement

"The proof of Lemma lem:crit carried out for g^S" must use the complement of the g^S-line that is stable under
the full Hecke algebra (the sum of the other generalised eigenspaces). The Petersson orthogonal complement is
not T-stable when U_p is involved (shown at level 44), so the two differ. The paper's text says "the
T-stable complement", which is right; the book must not substitute the Petersson one. Expository.

### 62. A third example where r and deg differ

539d1 has congruence number r = 504 against modular degree 72 (the gap is at 7, with 7^2 dividing 539),
next to 99a1 (r = 12, deg 4) and 726a1 (point 58). r(121a) = r(121c) = 6. Optional.

## Book-internal consistency (continued)

### B20. Items from the Chapter 13 outline

* The twist of 20a by -7 is class 980g, not 980i: the paper's 980i1 congruence is between 980i1 and the
  twist of 20a1, which is a different newform. The paper is right; outlines must not identify the two.
* PLAN.md's Chapter 13 scope uses k both for the weight and for the exponent in the T_{p^k} recursion.
* Li75 and Rankin39 are needed by Chapters 13, 15 and 19 and belong in refs.bib (B14), after checking their
  bibliographic data.

## From the Chapter 17 outline (Galois cohomology, Selmer structures)

Source: `outlines/ch17_galcoh.md`, final section. Its first point is now an addendum to point 7 above.
The outline also checks the identification of c' with PARI on 77c1, 791a1, 1577a1 and 11a1.

### 63. Lemma lem:dfg21: the hypothesis H^0(Q, V^D) = 0 is automatic here

The paragraph after the lemma shows H^0(Q_p, V^D) = 0 at every p in Sigma (the local Euler factor is
nonzero), which already gives H^0(Q, V^D) = 0; surjectivity onto H^0(Q, W^D)^* uses exactly that fact. So
in the paper's setting only H^1_f(Q, V^D) = 0 needs DFG04 Theorem 2.7. Observation, low importance.

## Book-internal consistency (continued)

### B21. Items from the Chapter 17 outline

* The Chapter 3 outline (8.3(vi)) assigns the Cartier duals T^D, W^D to Chapter 18; Chapter 17 needs them
  first (local duality). Read "Chapters 17 and 18".
* SerreGaloisCoh (planned for bib/ch16.bib) is cited by Chapters 16 and 17 and belongs in refs.bib (B14);
  MazurRubin04 too if Chapter 18 cites it.
* Chapter 21 item A2.7, step (7), drops eps in "c' = kappa_u(Frob)"; its commentary "no such map" must be
  softened per the addendum to point 7.

## From the Chapter 18 outline (Bloch-Kato Selmer groups, Tamagawa factors)

Source: `outlines/ch18_blochkato.md`. Point 64 was checked by the orchestrating session for l >= 5; the
l = 3 case and points 65 to 68 are as reported by the outline agent (PARI checks on Cremona's tables below
conductor 10,000, including 52,896 brute-force checks of the formula of Lemma lem:tamfactor and 101,336 checks
that Tam(T) is the l-part of c_q, all without mismatch).

### 64. Open question 3, first half, answered: Tam_q(ad T) is trivial at potentially good additive primes

For q != l, l odd, and E with potentially good additive reduction at q, v_l(Tam_q(ad T)) = 0. Argument:
inertia acts on M = ad T through a finite group H of order dividing 24, with kernel K. Inflation-restriction
gives 0 -> H^1(H, M) -> H^1(I, M) -> Hom(K, M)^H, and Hom(K, M) factors through the tame pro-l quotient Z_l(1)
of K, so it is torsion-free; H^1(H, M) is killed by #H. For l >= 5, l does not divide #H, so H^1(I, M) is
torsion-free and the Tamagawa factor is trivial (checked by the orchestrating session). For l = 3, the agent
shows ad T is free over Z_3[C_3] for the 3-part of H (explicit basis), so H^1(H, M) has no 3-torsion. At
potentially multiplicative primes the formula of Lemma lem:tamfactor applies to the Tate parameter (point 18).
Consequence: (eq:identity) becomes fully explicit, and the excess of v_l(deg) over the explicit bound is
exactly the Selmer length (the second half of Open question 3). Data below conductor 10,000 at l = 3: the excess
is never negative and is 0 for 8,688 of 13,203 curves. **Action:** state this as a lemma in Section 4 and
reduce Open question 3 to the Selmer group. Confidence: high (l >= 5 checked twice; l = 3 as reported).

### 65. Abstract: the Tamagawa sentence omits the condition l | n_q and says "by one"

The abstract says the Tamagawa factor formula "raises the bound by one whenever a Steinberg prime q = 1 mod l
has a Tate parameter whose unit part is an l-th power". By Lemma lem:tamfactor the extra term is
min(v_l(n), v_l(q - 1), v_l(c)), which needs l | n_q and can exceed one. **Action:** add "with l | n_q" and
write "by at least one". Confidence: high.

### 66. Abstract: "the Bloch-Kato Selmer group of ad V_l E" should be of ad T tensor Q_l/Z_l

The length is that of H^1_f(Q, ad T tensor Q_l/Z_l), as in Theorem thm:main; the Selmer group of the Q_l-vector
space ad V_l E is zero under the hypothesis (DFG04 Theorem 2.7). Minor; confidence high.

### 67. Remark rem:ns and Section 1.3 rest on H^1_f(Q, V^D) = 0 for 3Ns curves, which is not known there

The corrected exact sequence of Remark rem:ns needs H^0(Q, V^D) = H^1_f(Q, V^D) = 0. The first is automatic
(point 63); the second is DFG04 Theorem 2.7, which is proved only for l not in S_f, and 3Ns curves are exactly
the case l = 3 in S_f. The remark is phrased conditionally ("whenever"), but Section 1.3 presents the
correction term as what the lemma produces. **Action:** say explicitly that the vanishing of H^1_f(Q, V^D) for
these curves is assumed, or cite a result proving it. Confidence: medium-high.

### 68. Section sec:tam can include I_n^* primes, and "exactly where" overstates

The Tamagawa factor formula applies at potentially multiplicative additive primes too (point 18), so the test
of Section sec:tam can include primes of type I_n^*. "The extra divisibility is exactly where the Tamagawa
factor exceeds l^{t_l}" overstates what the data show (the Selmer length also contributes). Optional.
The agent's counts below conductor 10,000: at l = 3, 1,050 curves, equality rises from 56.8% to 68.0% with the
refined bound; at l = 5, 252 curves, equality from 203 to 220; no violations once CM curves are excluded
(CM curves carry no mod 3 image label in Cremona's galrep file, and four of them fail if not removed).

### Open check Q1: does DFG04 cover l = 3 in weight 2?

Whether DFG04's Theorem 3.7 covers l = 3 for weight 2, given the Fontaine-Laffaille range needed for the
adjoint. To be checked against DFG04 together with the checklist of point 56.

## Book-internal consistency (continued)

### B22. Items from the Chapter 18 outline

* PLAN.md's Chapter 18 entry repeats the misplaced parenthesis of point 37 and treats additive Tamagawa
  factors as unknown (superseded by point 64).
* PLAN.md uses V^* for the linear dual, which clashes with ^* for the Pontryagin dual (B4); the Chapter 18
  outline uses V^vee for the linear dual. Appendix B must fix this.
* The Chapter 21 outline (A1.3, A2.7, A4.10) and the Chapter 3 outline (line 106) should cite Chapter 18's
  items for Tam_p, lem:fpr and lem:tamfactor.
* The paper's wording "the torsion of H^1(Q_p, T^D)" is right and must not be simplified: H^1(Q_p, T^D) is
  infinite at I_0^* primes and at primes with cyclic inertia where chi(p) = 1.
* 791a1 is a clean example where the Tamagawa excess is needed for equality; rule(E, l) gives [1, 1] for 121a1
  and [2, 2] for 726a1, as in the paper.

## From the Chapter 19 outline (L-functions, the adjoint, Euler factors)

Source: `outlines/ch19_lfunctions.md`. Point 69 (its example) was also checked independently by the
orchestrating session with PARI; the rest is as reported, with PARI checks: Lemma lem:euler agrees with
lfunsympow on all 117,232 pairs (curve, bad prime q >= 5) below conductor 10,000; the Petersson formula holds
to about 1e-15 on 15 curves; rule(E, l) gives [1, 1] for 121a1 and [2, 2] for 726a1.

### 69. Remark rem:wild and Section sec:wild: the shape of P_q at every prime, and the prime 2 at l = 5

At every bad prime q, including 2 and 3, P_q(X) is one of four shapes: 1 - X (multiplicative), the I_0^* cubic
(1 - qX)(1 - (a^2 - 2q)X + q^2 X^2) of a quadratic twist with good reduction at q, 1 - cqX with c = plus or
minus 1 (cyclic inertia of order 3, 4 or 6 with an invariant line), or 1. Every cubic factor below conductor
10,000 (1,143 at q = 2, 2,283 at q = 3) is the I_0^* formula for such a twist; this also confirms point 60.
(Corrected after the memo: an earlier version gave the linear factor as 1 - X. Since L(Sym^2 f, s) =
L(ad f, s - 1), P_q(X) = (1 - alpha^2 X)(1 - qX)(1 - beta^2 X); for 592c1, q = 2, a = -2, this is
1 - 2X + 4X^2 - 8X^3, as PARI gives.)

Consequences:

* 1232l1 is 77a1 twisted by chi_{-4}, and a_2(77a1) = 0, which explains e_3(E, 2) = 2 (point 50).
* The prime 2 can contribute at l = 5: 592c1 is 37a1 twisted by chi_{-4} (type II* at 2, cubic P_2,
  e_5(E, 2) = 1, modular degree 80 = 2^4 * 5; checked with PARI). So the paper's "for l = 5, 7 no term is
  needed at q = l or at q = 2, 3 beyond Definition def:terms" is right (the term is in def:terms), but the
  reader should not infer that 2 never contributes at l >= 5.
* "Potentially good in about half of the cases" for type I_n^* at 2 is 58% below conductor 10,000 (61% below 5,000).

**Action:** replace the case-by-case remarks on 2 and 3 by this classification. Confidence: high.

### 70. Addendum to point 30: the exact relation with the Rankin series

sum a_n^2 n^{-s} = zeta^(N)(s - 1) L^nv(Sym^2 f, s) / zeta^(N)(2s - 2) exactly, with no correction at the bad
primes; equivalently Shimura's series gives the naive function on the nose:
L^nv(Sym^2 f, s) = zeta^(N)(2s - 2) sum a_{n^2} n^{-s}. **Action (refines point 30):** the Introduction can say
"the naive adjoint L-function, zeta^(N)(2s - 2) sum a_{n^2} n^{-s} (Shimura)". Confidence: high.

### 71. Optional: an exact degree formula makes the role of the Euler factors explicit

Combining the Petersson formula <f, f> = N L^nv(Sym^2 f, 2) / (8 pi^3) (valid at every level) with
Zagier-Watkins gives deg phi_E = N L^nv(ad f, 1) / (2 pi vol(Lambda_E)). Writing B_E for the same expression
with the true L-value, v_l(deg phi_E) = v_l(B_E) + sum_q e_l(E, q) unconditionally, and the inequality
(eq:thm) is equivalent to v_l(B_E) >= sum_q t_l(E, q). Checked exactly on 19 curves. The attribution of the
Petersson formula to DFG04 Lemma 2.12 is not checked. Optional; confidence high on the formula.

### 72. Section 1.1: delta_p and the formula for L_p are wrong at p = l

"delta_p = 2, 1, 0 for good, multiplicative, additive reduction" and L_p = det(1 - Frob p^{-s} | A_f^{I_p})^{-1}
are the definitions for p != l; at p = l one uses D_cris. Harmless, since the paper only uses them at p != l.
Low importance.

## Book-internal consistency (continued)

### B23. Items from the Chapter 19 outline

* PLAN.md's Chapter 19 entry wrote the naive function as L(f x f, s)/zeta_N(2s - 2); it is
  L(f x f, s)/zeta^(N)(s - 1) with L(f x f, s) = zeta^(N)(2s - 2) sum a_n^2 n^{-s}. Fixed in PLAN.md. The entry
  also repeats the false claims of points 15 (e_l twist-invariant) and 50 (type II at 2 has P_2 = 1).
* The Chapter 2 outline's question 11.6(f) is answered: 539d1 has type I_0^* at 7 with E' = 11a3, e_3 = 2 and
  modular degree 72.
* By B14, Rankin39, Deligne73, Tate79, Rohrlich94, SerreTate68 and Shimura75 belong in refs.bib.

## From the Appendix B outline (notation and conventions)

Source: `outlines/chB_notation.md`. It fixes sixteen book-wide conventions (B-C1 to B-C16) and lists every
place where an outline disagrees with them: 48 entries (20 required, 28 cosmetic) plus 7 in PLAN.md. The
writer of each chapter must apply the required entries for that chapter; the entry IDs in the appendix outline
are stable even where line numbers drift. No new points about the paper.

### B24. Book-wide conventions now fixed (summary; details in the Appendix B outline)

* Frob arithmetic, Phi = Frob^{-1} geometric; L-factors use Phi, cohomology uses Frob; in chapters that also
  use Neron component groups Phi_q (10, 11, 21, 22) the geometric Frobenius is written Frob_q^{-1}.
* alpha, beta are the eigenvalues of the arithmetic Frobenius on V_l E and of the geometric one on H^1; hence
  L_p(V, s) = L_p(E, s + 1) (resolves B1, B7, B9).
* Duals: ^vee linear dual, ^* Pontryagin dual, ^D Kummer dual = ^vee(1), ^dagger adjoint of an operator; ^* after
  a map is a pullback (resolves B4, B22).
* A_f is always the adjoint; Shimura's abelian variety is J_f. Depletion is f^Sigma or f^{p}, never f^(p) (the
  superscript (q) is for twists). phi_f is the eigencharacter, varphi a map of curves.
* chi_l with a letter subscript is cyclotomic; a numerical subscript always means a quadratic character chi_d
  (chi_{-3}, chi_{-11}); the cyclotomic character at 3 is chi_3^cyc. The paper's chi_q = chi_{q*} is allowed
  only with the letter q (point 32).
* Manin constant written c_E, with deg phi_E vol(Lambda_E) = 4 pi^2 c_E^2 <f, f> (B10); Petersson product
  unnormalised; L(Sym^2 f, s) = L(ad f, s - 1) with a normalisation table.

### B25. Disagreements that matter most (required changes)

* Chapter 21 outline, convention C2(b) and its opening: still the B1/B7/B9 slip, and Frob_p used for the
  geometric Frobenius; also kappa instead of eps kappa in the Tate matrix.
* Chapter 4 outline names the arithmetic Frobenius Phi, inverting the book's convention.
* Chapters 14 and 15 use A_f for the abelian variety (Chapter 15 also for the adjoint).
* Chapter 11 uses Phi_q both for the component group and for the geometric Frobenius.
* Chapters 3, 15, 21 write adjoints with ^*; Chapter 21 also linear duals.
* Chapters 13 and 15 write depletion as h^(p).
* Chapters 5, 7, 11, 17, 21 use a bare numerical chi_3.
* Open choices left to the author: the stricter chi_{q*}-everywhere rule (about 40 extra edits), and the sign
  convention c_E > 0 for the Manin constant.

## From the Chapter 20 outline (congruence ideals, DFG04): the DFG04 checklist is settled

Source: `outlines/ch20_congruence.md`, Parts 7 and 8. The agent downloaded and read the published DFG04 from
Numdam. Point 74 was also checked independently by the orchestrating session; the DFG04 readings are as
reported by the agent, with the definitions quoted by number in the outline.

### 73. Point 56 and open check Q1 are settled: point 39 holds for DFG04's eta, and DFG04 covers l = 3

Point 56's checklist, item by item:
1. Integral structure: DFG04 define it as the image of the U_0(N)-invariants of the compactly supported
   cohomology of the full-level curve, not literally as H^1(X_0(N), Z_l). It agrees with H^1(X_0(N), Z_l) at
   non-Eisenstein maximal ideals, which is all the paper uses (the definitions are certain; that the comparison
   cokernel is Eisenstein in general is the agent's sketch, medium-high).
2. Interior cohomology is H^1(X_0(N)): confirmed.
3. The operator is the Atkin-Lehner involution with no scalar (N^{k-2} = 1 in weight 2); the pairing is the cup
   product on X_0(N) times 1/2, a unit for l odd: confirmed.
4. M_f = M(N, psi)_![I_f], the kernel lattice for the full Hecke algebra: confirmed.
5. eta is defined through the image of the second exterior power, i.e. the ideal of values: confirmed.

Q1: S_f in DFG04 (31) excludes only the primes dividing N k! (= 2N in weight 2) and the residually induced case.
The local condition at l is defined through extensions of short objects (DFG04 Proposition 2.2, Corollary 2.3,
needing only l > 2), and the condition 2 <= k <= l - 1 holds at l = 3. So DFG04 Theorem 3.7 covers l = 3 in
weight 2.

All DFG04 numbers the paper cites are correct (Theorems 0.1, 0.2, 2.7, 2.15, 3.7; Proposition 1.4(c); Lemmas
2.1, 2.12; (31), (57); p. 708; Sections 1.5.3, 1.6.1, 1.6.2, 1.7.2, 1.7.3, 1.8.2, 2.1; (13), (14)). DFG04
Lemma 2.12 gives the Petersson norm with the naive L-value, and DFG04 use the geometric Frobenius (confirming
point 11). **Caution:** a 2025 arXiv version of DFG04 (arXiv:2512.02348) uses different numbering; cite the
published version.

**Action for the paper:** Theorem thm:main can state (eq:identity) as an equality whenever l is not in S_f,
with the proof of point 39 replacing the multiplicity-one argument; reword the Section 4.1 description of the
integral structure and mention the factor 1/2. Confidence: high.

### 74. Theorem thm:quant: the first inequality is an equality whenever l is not in S_f

Apply the identity (eq:identity), now an equality (point 73), to E and to E_S. The twist does not change ad T,
so the Selmer groups agree; the Tamagawa factors agree (trivial at I_0^* primes by point 64, and at I_n^*
primes E_S is multiplicative with the same Tate parameter); and the only difference in the Euler terms is
sum over q in S of e_l(E, q). Hence v_l(deg phi_E) = v_l(deg phi_{E_S}) + sum_{q in S} e_l(E, q), with no
multiplicity-one hypothesis. This supersedes the second bullet of point 56 and the claims in the Chapter 14,
15 and 21 outlines that the equality needs multiplicity one. Data: equality holds in all 25,477 (curve, l)
pairs below conductor 10,000 (including 15,607 pairs with 3 in S and 8 with image 3Ns), and Theorem thm:twist
case (c) holds with equality in all 14,876 pairs. **Action:** state the equality in Theorem thm:quant (under
l not in S_f) and drop the multiplicity-one caveat in the remark after it. Confidence: high (argument checked
twice, data agree).

### 75. Lemma lem:dfg21: the paper's hypothesis is a sufficient form of DFG04's

Expository; the paper's statement is correct as a special case.

## Book-internal consistency (continued)

### B26. Items from the Chapter 20 outline

* Chapter 14 (9.5(c), 10.4(b)), Chapter 15 (10.4) and Chapter 21 (A4.16) say the equality in thm:quant still
  needs multiplicity one; point 74 removes this.
* Chapters 14, 18, 19 and 21 mark DFG04 facts as "not checked against DFG04"; they can now cite the Chapter 20
  outline's Part 7.
* Chapter 13 item 7.4 cites DFG04 Section 1.5.3 for f^Sigma; it is in Section 1.7.3.
* PLAN.md cites "DDT Theorem 5.3"; unverified.
* By B14, DiamondTaylor94 belongs in refs.bib; Diamond96, Lenstra95 and DFG04long go in bib/ch20.bib.

## From the Chapter 22 outline (computation, data, protocol)

Source: `outlines/ch22_computation.md`, Parts 7 and 8. The agent reproduced the paper's checks on all 38,042
optimal curves with N < 10,000 with PARI 2.17.2: no violation of (eq:rule), (eq:main), (eq:twist), Conjecture
conj:eis or the Tamagawa refinement; rule(E, l) gives the paper's values on 121a1 and 726a1; ns3 agrees with
Cremona's 3Ns label on every non-CM curve; ellmoddegree agrees with Cremona's degphi file on all 38,042 curves.
Point 76 was also checked independently by the orchestrating session; the rest is as reported.

### 76. Section sec:eis: two factual slips about deficits D = 2

* The paper says the seventeen curves with E[3] = Z/3 + mu_3 (image 3Cs.1.1) and D = 2 all have torsion Z/3.
  14a1 has image 3Cs.1.1, torsion Z/6, types I_6 at 2 and I_3 at 7, modular degree 1, so D = 2 with torsion
  Z/6. (Checked with PARI and Cremona's galrep file.)
* "With a rational point of order 3 and mod 3 image of Borel type, D <= 1" is literally false: 714i1 (torsion
  Z/9, image 3B.1.1, modular degree 1080 = 2^3 3^3 5, D = 2) and 6942n1 (torsion Z/9, image 3B.1.1, degree
  65664 = 2^7 3^3 19, D = 2). The paper's next clause names the order-9 case as the other source of D = 2, so
  this is a wording slip: say "without a point of order 9". (Checked with PARI.)

Neither affects Conjecture conj:eis, whose bound holds on all curves checked. **Action:** correct both
sentences. Confidence: high (checked twice).

### 77. Protocol: the correction term h_l was never blind-tested

The out-of-table set (the only data generated before Conjecture conj:euler was formulated) contains no 3Ns
curve, so the correction term h_3(E) was fitted on and only confirmed by data already seen. The paper also does
not state the blind status of the out-of-table curves for (eq:twist). **Action:** say so in Section sec:data.
Confidence: high, as reported.

### 78. rule(E, l) must be run on the optimal curve, and it is not meant for Eisenstein primes

rule gives wrong-looking answers when misused: 990h1 gives [4, 3] while 990h3, the optimal curve of the class,
gives [3, 3]; 11a1 at l = 5 (Eisenstein) gives [0, 1]; 11a3 at l = 5 gives [-1, 0]. **Action:** state in the
appendix that E must be the optimal curve and E[l] irreducible. Low importance.

### 79. Section sec:sharp: what the calibration statistic shows

The agent reproduces the calibration on N < 10,000: 14,275 violations expected under independence, 0 observed
(70.3% of the curves with a positive bound, against the paper's 69.7% on the working set); a permutation null
gives about 7,600. The figure depends on the reference population, and it shows that the statement is strong
(far from vacuous), not that it is valid. The odd-part statistic (the paper's 1.85%) is 17.1% on N < 10,000,
so it is strongly range-dependent. Optional: say so.

### 80. Minor computational remarks

* ellmoddegree needs at most about 32 MB in PARI 2.17.2 (the paper says a few hundred MB, true for 2.15 at
  larger conductors). Low importance.
* The number of 3Ns violations of (eq:thm) depends on whether the q = l terms are included (36 or 24 below
  conductor 10,000); the paper's text does not say which reading it used.

## Book-internal consistency (continued)

### B27. Items from the Chapter 22 outline

* PLAN.md and the Chapter 11 and 21 outlines name the modular-degree file alldegphi; in the ecdata repository it
  is degphi. Cremona's files contain no per-prime Kodaira symbols; PARI recomputes them.
* PLAN.md's ellinit(E, q) reduces mod q; the q-adic curve needs ellinit(E, O(q^k)). ellsearch needs the elldata
  package, not installed here.
* Feller68, Wasserman04 and RHB06 are in bib/chA.bib but cited by Chapter 22; by B14 they move to refs.bib.
* Appendix A and Chapter 21 item A6.1 call (eq:twist) blind-tested without the caveat of point 77; Chapter 21
  item A6.10 repeats the slips of point 76.

## Findings from writing Chapter 10 (pilot, 16 October 2026)

### 81. Open question 6 of the revised paper is settled (twists at q = 3)
The exchanges II<->IV*, III<->III*, IV<->II* under the twist by Q(sqrt(-3)) hold at q = 3 with the conductor exponent
unchanged, given only the Ogg-Saito formula: chi_{-3} is tame, so the Swan conductor and f_3 are unchanged; v_3(Delta_min)
shifts by 6 mod 12; for potentially good types 1 <= m <= 9, so v_3(Delta_min) lies in [f, f+8] on both sides, forcing
m -> m +/- 6; I_n^* (n >= 1) at odd p is potentially multiplicative and excluded. Hence the max formula for w_l(E,q) in
Section 1.4 also holds at q = 3. Proved as Proposition prop:reduction:twist-at-3; checked on all 5,122 pairs below
conductor 10,000. Confidence: high (given Ogg-Saito). Importance: medium (removes an open question).

### 82. PARI's Tate parameter at q = 2 when v_2(j) = -1
PARI/GP 2.17.2: ellinit(E, O(2^k)).tate[3] returns q_E^5 instead of q_E for every curve with v_2(j) = -1 (1,262 of 1,262
pairs below conductor 3,000; e.g. 208a1, 832c1, 14a6, 26a3); it agrees with the q(j) series for nu >= 2 at 2 and at all
odd primes. No count in the paper changes (its rule uses valuation(j,q), and the extra Tamagawa term at 2 vanishes since
v_l(q-1) = 0), but Sections sec:tam / sec:data ("We computed the Tate parameters with PARI") should say how q = 2 was
handled. Chapter 10 carries warn:reduction:pari-tate; Chapter 22 must carry the same warning.

### 83. The 58% in Remark rem:wild names no population
Below conductor 10,000, 2,340 of 4,037 pairs (58%) among curves numbered 1 are potentially good at 2; over all curves
it is 5,935 of 9,667 (61%). Memo E9 attributes 61% to conductor < 5,000; on the full table below 10,000 61% is the
all-curves figure. The paper should name the population. (Curves numbered 1 are the optimal curves below 10,000 except
class 990h, whose optimal curve is 990h3; 990h is multiplicative at 2 and does not enter the count.)

### 84. Section 1: which rows of the table hold at q = 2 (expository)
After the table in Section 1 the revised paper says "The rows I_n, I_n^* and I_0^* hold at every odd q != l". Lemma
lem:euler gives the I_n row at every q != l, including q = 2. Suggested wording: "the row I_n at every q != l, the
rows I_n^* and I_0^* at every odd q != l". Low importance (found while writing Chapter 2).

### 85. Lemma lem:h0: "is cyclic" before finiteness (expository)
In the proof of lem:h0 (v2), "H^0(Q,W^D), a submodule of (Q_l/Z_l)^3 with l-torsion of rank at most one, is cyclic" is
said before finiteness is known. Such a module is finite cyclic or isomorphic to Q_l/Z_l, which is not cyclic; the
determinant step that follows shows every element has order at most l, so the proof is complete. Suggested wording:
"is finite cyclic or isomorphic to Q_l/Z_l; the determinant argument below shows it is finite". Found writing
Chapter 4, confirmed by its reviewer.

### 86. Lemma lem:ddt417: two steps of the proof (expository)
(a) "Since L is torsion-free and wp cap I = 0, the sum L[wp] + L[I] is direct": this follows from wp cap I = 0 only
after an unstated rank argument (I != 0 and wp has corank one, so wp + I has finite index and contains a nonzero
scalar). The operative reason is that pi(t) = t + (pi(t) - t) lies in wp + I and is nonzero, so an element killed by
wp and by I is killed by pi(t). (b) The converse inclusion shows only t y = 0 for one t in I; concluding y in L[I]
needs I = O t, which holds because pi restricted to I is injective (wp cap I = 0) with image eta, or the argument run
with every s in I. Left and right orthogonals are mixed (harmless: both equal L[I]). Found writing Chapter 3,
confirmed by its reviewer. (A third proposed point, that lem:crit needs the rank of T/(I+J) stated, was judged not a
gap: the paper's "cyclic, of order r'" already asserts finiteness, which is equivalent to phi_f(J) != 0.)

### 87. Paragraph after Lemma lem:IV: freeness of T_3E is not tied to q >= 5 (expository)
The paragraph after lem:IV (v2) says "For q>=5 the order 3 is also the semistability defect ... and T_3E is then free of
rank one over Z_3[X]/(X^2+X+1)", which reads as if the freeness needs q >= 5. It holds at every q != 3 where the image
of inertia has order 3, q = 2 included: lem:IV gives a cyclic image of order 3 in SL_2(Z_3), so sigma^2+sigma+1 = 0 on
T_3E, and T_3E is free of rank one over Z_3[zeta_3] (Chapter 6, cor:ant:z3zeta3modules). Only the identification with
Kraus's semistability defect needs q >= 5. The paper itself uses the freeness at q = 2 in lem:tamadd. Suggested fix:
move "T_3E is free of rank one ..." out of the q >= 5 sentence. Found writing Chapter 6, confirmed by its reviewer.

### B28. Items from writing Chapter 10
* Cremona's ecdata files used here have no per-prime Kodaira symbols or Tamagawa numbers (only the product in allbsd);
  the paper's Section sec:data sentence should be checked against the full ecdata repository (Chapter 22).
* In PARI 2.17.2, ellglobalred(E)[5] gives [f,k,0,c], not [f,k,[u,r,s,t],c]; only elllocalred returns the change of
  variables.
* Kraus89 moved from bib/ch10.bib to refs.bib (B14: the paper's Open question 6 and Chapters 21, 22 cite it).
* The Lorenzini10 reference for Theorem 7.7 at p = 2 is unverified (taken from Praveen26); the chapter says so.

### B29. Items from writing Chapter 1

* Matrix J: the paper (prop:ns, sec:anomaly; note_v2.tex near line 538) writes J for [[0,1],[-1,0]]; the first
  draft of Chapter 1 used [[0,-1],[1,0]]. Settled by decision D5 (PLAN.md 7.5, 16 October 2026): the book uses the
  paper's J. Chapter 1 has been converted (w = sigma J, J = m_{-i}, a^2 = J, the eigenvalue of J on the line of
  (i,1) is -i, and the Q_8 basis is i = J, j = [[1,-1],[-1,-1]], k = ij with u i u^{-1} = k, all checked in PARI);
  the outlines of Chapters 1, 4 (C6, 8.2: eigenvector v = (1,i)^t for psi(J) = i) and 11 (C5) follow it.
* Dickson's theorem (thm:groups:dickson) is stated for odd l only, since Chapter 1 defines Cartan subgroups only
  for odd q; part (a) for l = 3 is proved (prop:groups:gl23subgroups). The groups of order 8 are proved in full
  (outline had a sketch), by a new normal-form lemma lem:groups:normalform.
* Chapter 1 credits lem:tamfactor to ch:blochkato and lem:h0 to ch:galrep, following PLAN.md.
* The writer flagged citation locations taken from memory and not checked against the books (for the final
  bibliography pass): Serre72 Section 2, Props 15 and 16 (Dickson); Lang Ch. XIII Sec. 8 (simplicity of PSL_2);
  Dummit-Foote Sec. 6.2 (simple group of order 168) and the Dummit-Foote section numbers in the Notes; Huppert67
  Ch. II Sec. 8; Munkres00 Thm 37.3 (Tychonoff). Sutherland's labels (3Cs.1.1, 3B.1.1, 3B.1.2, ...) and the
  standard models were not re-checked against Sutherland16's own tables.
* New single-chapter bib keys in bib/ch01.bib: Huppert67, Munkres00 (with Dickson1901). If a later chapter cites
  any of them, move it to refs.bib (B14).
* PGL_2(F_5) = S_5 is sketched by the action on the cosets of a subgroup of order 24 (machine-checked), not by the
  outline's route; the 16-row subgroup table of GL_2(F_3) is from a computer enumeration, rechecked by the writer.

### B30. Items from writing Chapter 2

* chi_D is used only for fundamental discriminants D, as in B-C6(b); for any other discriminant the Kronecker symbol
  (D/.) is written out (so (-12/.) is chi_{-3} made imprimitive modulo 12, and the symbol chi_{-12} is not used).
  Components of a Dirichlet character are written chi^{(p)}, chi^{(i)} (B-C6(a) reserves chi_p for the cyclotomic
  character); chi_0 is the principal character. Later chapters should follow the same rules.
* Outline 9.6(iii) and Exercise 14 were wrong: for q = 3 mod 4, n -> (q/n) is not a Dirichlet character on all of Z;
  it agrees with chi_{4q} = chi_{-4} chi_{q*} on odd n only, and (q/(4q+2)) = -(q/2). The chapter proves this.
* refs.bib key Koblitz is the elliptic curves and modular forms book, not Koblitz's p-adic book; valuations, the
  product formula and Ostrowski are cited to SerreCourse Ch. II and Neukirch Ch. II.3 instead.
* Rigour raised above the outline in several places (Zorn for maximal ideals, R[x] a UFD, primitivity of chi_D for
  fundamental D, the imprimitive Gauss sum); 6.5(v) is stated for an element of order 3 (or dividing 4) in any group,
  which is what lem:IV and lem:euler use.
* Book section numbers in the Notes (Dummit-Foote, Ireland-Rosen, Cohen 1.4 and 5.1, Lang, Neukirch, Serre) are
  pointers not verified against printed editions; the chapter says so.
* The lem:crit paperlink takes T tensor Q = Q x T' as given and points to ch:hecke; Chapter 13 must prove it.

### B31. Items from writing Chapter 3

* Jordan-Holder is proved for modules of finite length over any ring (B2); Nakayama, the cyclicity criterion
  (prop:modules:dvr-modules(v)) and the Gram criterion (prop:modules:gram, now over any commutative ring) are there for
  Chapter 4 and later chapters.
* Outline errors corrected: 7.5(vi) Fitting counterexample (k[x]/(x^2) with M = R has Fitt(R) = 0, equality holds;
  replaced by R = Z[x], M = R/(4,x)); 9.6(iii) needs rank T/a + rank T/b = rank T (a = b = 0 is a counterexample
  without it), automatic in lem:crit. Dual numbers written k[x]/(x^2) (B-C15(k) reserves epsilon).
* lem:ddt417 is stated in length form in rem:modules:ddt417-preview and proved in ch:congruence, which carries the D1
  Commentary; Chapter 3 points to it.
* In Chapter 3, lem:crit's letters appear only in quotations (I = ker phi_f, J = Ann_T(f^perp) = Ann_T(I)); the generic
  ideals of prop:modules:algebra-duality are a, b; elsewhere I = Ann_T(wp) (B-C13(c)).
* Book theorem and section numbers in the Notes are unverified pointers, and the chapter says so.
* Remaining minor points from the check, left for a later pass: ex-cofinite(b) wording of the dual map; ex-gram-index(c)
  should mention the automorphism w as well as the factor 1/2.
* Length 2,529 lines (about 2,357 without the card), above the 2,200 guideline after cutting 9 restating exercises (D2).

### B32. Items from writing Chapter 4

* rem:reps:mod-l-galois(ii): the Clifford equivalence (hypothesis of thm:main fails iff rhobar = rhobar tensor chi_{l*}
  iff rhobar is induced from H) needs rhobar irreducible; for rhobar reducible the hypothesis fails trivially, and
  1 + chibar_l (l >= 5) shows the equivalence is false without irreducibility. Later chapters (11, 21) must keep it.
* At l = 3, invariants fail to commute with reduction only for elements of order 3 acting on T; for order 6, and on
  ad T, they commute.
* prop:reps:twist-length(iii) is proved without completeness of O and without a finite residue field.
* Outline corrections: with D5, the eigenvector of J for psi(J) = i is (1,i)^t; the density theorem is proved, so
  Brauer-Nesbitt holds over any field and 2.3(iv) over every field; 5.3(i) needs no char != 2; a genuine counterexample
  over F_9 to 5.3(ii) replaces the outline's C_4 example; 9.3 is proved for every q prime to m; 9.4(v) proved.
* Notation: the characters of an extension in Ribet's lemma and prop:reps:nonsplit-line are eta_1, eta_2 (recorded in
  Appendix B, B-C15(h)); uniformiser varpi; Section 9 writes h = diag(1,-1), gamma for kernel elements, nu = u - 1.
* Remaining minor points from the check, left for a later pass: prop:reps:twist-length(iii) should state that X^G is
  isomorphic to K/O when h is infinite (the paperlink uses it; proof: varpi M_{m+1} = M_m); lambda_0..lambda_3 in the
  D_4/Q_8 character table clash with eigenvalues lambda_i elsewhere in the chapter (cosmetic).
* Chapter 4 relies on Chapter 6 (ch:ant) for T free of rank one over Z_l[g] and T/3T = Z_3[zeta_3]/(pi^2), and on
  ch:local for roots of unity in Q_l and tameness at q >= 5.

### B33. Items from writing Chapter 5

* New lemma lem:galois:nonempty-limit (an inverse limit over a directed set of nonempty finite sets is nonempty); Chapter
  6 cites it through ch:galois. thm:galois:algebraic-closure(d): every F-embedding Fbar -> Fbar is an automorphism.
* cor:galois:congruent-ap(d): for a newform h of weight 2 on Gamma_0(M) and l odd, a_p(h) = a_p(E) mod lambda on a set of
  density one gives rhobar_h = rhobar_{E,l} tensor k when rhobar_{E,l} is irreducible (given ch:modgalrep). The paper's
  "rhobar_g = rhobar, that is, a_p(g) = a_p(f) mod lambda" is (c) in one direction and (d) in the other.
* The paper's ns3 function returns 1 exactly for image N_s(F_3), for every E/Q; checked by the reviewer on all 64,687
  curves below conductor 10,000 (120 labelled 3Ns by Cremona's galrep file, plus 26 CM curves galrep leaves unlabelled).
* The outline's y^2 = x^3-6x-8 is 6912d1 (image 3Ns); 726a1 has psi_3 = (x^2-x-74)(3x^2+8x+20).
* Sketches upgraded to proofs: Artin-Schreier (b), the Kappe-Warren C4/D4 test, no small subgroups in GL_n(C),
  disc(x^n-a), disc(Phi_l), disc(R_f) = disc(f). Notation: Frob_q (never phi_q), E_lambda for the l-adic coefficient
  field, b(sigma), u(sigma) in the Kummer propositions.
* Assigned elsewhere by the outlines: inertia and tame inertia (Chapter 1 points to ch:galois and ch:local; only Chapter
  7 has it); chibar_l(Frob_p) = p mod l is a black box here, proved in Chapter 6; det rhobar_{E,l} = chibar_l is
  Chapter 9 (Weil pairing).
* Unverified pointers added: Lang VI.9 (Artin-Schreier), Lang XI (real closed fields), Lang IV.6 (symmetric
  polynomials).

### B34. Items from writing Chapter 6

* prop:ant:latticefree: T free of rank one over Z_l[g] for g with characteristic polynomial Phi_m, m in {3,4,6}, any odd
  l (Chapter 4 needs orders 4 and 6 as well as 3); prop:ant:commutant needs characteristic polynomial X^2+X+1 (resp.
  X^2+1), not just sigma^2+sigma+1 = 0.
* The tame statement cor:ant:frobsigma holds at every q with rho(I_q) of order prime to q, q = 2 and 3 included; the
  tame relation itself is only sketched here and must be proved in Chapter 7, with D_p = G_{Q_p}, prop:ant:otimesZl and
  Z_3[zeta_3] as the ring of integers of Q_3(sqrt(-3)).
* How the paper uses Chebotarev and CM: in v2, prop:ns and lem:h0 get rhobar = rhobar tensor chi_{-3} from Ind psi by
  Frobenius reciprocity; the trace criterion (3 | a_p for p = 2 mod 3, prop:ant:twistdetect) and the CM theorem are the
  book's, used for the original version of lem:h0 and for the Chapter 5 example. The original sec:anomaly check was
  "some p < 1223 inert in Q(sqrt(-3)) has 9 not dividing a_p", for h_3 <= 1.
* The level-23 Hecke algebra T = Z[T_2] = Z[theta] is now proved in Chapter 6 (ex:ant:level23); Chapter 3 cites it.
  Chapter 3's remark that its DVR criterion (e) is "used only in ch:ant" is no longer accurate (Chapter 6 uses (a)).
* Notation: geometric Frobenius written Frob_p^{-1} (Phi_n are cyclotomic polynomials here), declared in
  conv:ant:conventions(e); (1+sqrt d)/2 is theta_d; integral bases beta_i; the paper's D written prod_{q in S} q.
* Chapter 9 must supply the Galois action on CM endomorphisms (exercise ex:ant:ex-cm points there).
