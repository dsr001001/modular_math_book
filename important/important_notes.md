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

### 43. Open question: is the exception in Proposition prop:forms (type IV or IV* at 2, l = 3) provable?

The proof of Lemma lem:euler uses q >= 5 only to know that the image of inertia is cyclic and tame. If for
types IV and IV* at q = 2 the image of inertia on T_3 E is cyclic of order 3 or 6 (tame, since 3 is not 2),
the same computation applies: the invariant line of ad V has Frobenius eigenvalue chi_{-3}(2) = -1, so
P_2(X) = 1 + 2X and e_3(E, 2) = v_3(3/2) = 1. That is exactly what PARI gives for all 92,812 such curves in
the working set, and it would turn the exception in Proposition prop:forms into a theorem.

**Not verified:** at q = 2 the image of inertia for potentially good reduction can also be non-abelian
(of order 8 or 24), and whether types IV and IV* at 2 force a cyclic image of order 3 or 6 has to be checked
against Kraus90. **Action:** check Kraus's classification at 2; if confirmed, prove the case. Confidence:
open.

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
