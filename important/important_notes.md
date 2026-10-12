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
