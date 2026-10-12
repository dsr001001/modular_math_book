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
e_3(E, 11) = 0; its twist by chi_{-11} (class 121d) has type I_1^* at 11, so e_3 = v_3(11^2 - 1) = 1. The true
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

It holds because T is reduced (T tensor Q is a product of fields) and I = Ann(wp). **Action:** add one line.

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
