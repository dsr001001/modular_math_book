# Chapter 21. Reading the paper: a guided tour (label `ch:paper`, file `chapters/ch21_paper.tex`)

Stage 1 line-up. Target length: up to 2,800 lines (PLAN.md 7.3 allows this for Chapter 21), card excluded.

The chapter is a commentary on the paper in the paper's order. Every item below is either (A) a statement of
the paper restated precisely in the book's shared notation, (B) a convention the reader must fix to read the
paper, or (C) a device of the tour (dependency diagram, hypothesis table, list of imported statements, worked
verifications). Rigour tags follow PLAN.md 3: the paper's own lemmas are *proved here* with every compressed
step expanded; the imported theorems are *stated; reference* with the exact numbering; the long arguments
reproduced from the paper (the assembly of Theorem thm:main, Steps 1 to 4 of Theorem thm:quant) are *proved
here* because every ingredient is a card entry of an earlier chapter.

Frobenius convention used throughout (fixed in item C2). Two Frobenii occur in the paper and the convention
must be stated once and for all. (a) In every GROUP-THEORETIC statement (the relation `Frob^{-1} t Frob =
t^{q^{-1}}`, the conjugation action of `G/I` on `H^1(I, M)`, the matrix `rho(Frob)` in Lemma lem:tamfactor)
`Frob` is the ARITHMETIC Frobenius: it acts on `mu_{l^k}` by `zeta -> zeta^q`, and `chi_l(Frob_p) = p`.
(b) In every L-FACTOR, `L_p(M, s) = det(1 - Frob_p p^{-s} | M^{I_p})^{-1}` with `Frob_p` the GEOMETRIC
Frobenius `= Frob_arith^{-1}`, which is the convention of DFG04 1.7.2 and of Bloch-Kato. The two are forced
by the paper itself: at a Steinberg prime the inertia-invariant line of `ad V_l E` carries the arithmetic
eigenvalue `q` (computed in Lemma lem:tamfactor: `Ad(rho(Frob)) e = q e`) and the paper's factor is `1 -
q^{-1-s}`, so the `L`-factor uses `q^{-1}`, the geometric eigenvalue; and `L_p(A_f(1), 0) = L_p(A_f, 1)`
(Lemma lem:fpr) holds because the geometric Frobenius acts on `Z_l(1)` by `p^{-1}`, so `L_p(M(1), s) =
L_p(M, s + 1)`. At a good prime the eigenvalues `alpha/beta, 1, beta/alpha` on `ad V` are inversion-symmetric
and the convention is invisible there; so are `chi_{-3}(q), chi_{-4}(q) = +-1`. `H^1_ur(Q_p, M) =
M^{I_p}/(Frob_p - 1)M^{I_p}` is the same group for either Frobenius.

---

## Part A. Core results, in teaching order

### A0. Conventions and standing notation (Section 21.1 of the chapter)

**C1 `conv-standing`** (convention; *stated*; reference: the paper, Section 1 and Section 1.1; DFG04 1.7.2;
paper use: everywhere).
Statement. Throughout, `E/Q` is an elliptic curve of conductor `N`, `X_0(N)`-optimal in its isogeny class,
`varphi_E : X_0(N) -> E` its modular parametrisation and `deg varphi_E` its modular degree; `f = f_E in
S_2(Gamma_0(N))` is the newform with `a_p(f) = a_p(E)` for all `p`; `l` is an odd prime; `V = V_l E`,
`T = T_l E`, `rho = rho_{E,l} : G_Q -> Aut(T) = GL_2(Z_l)`, `rho bar = rho mod l` on `E[l]`; `A_f = ad V`
is the trace-zero adjoint (`ad` means `ad^0` in the paper and the book); `delta_p = dim V^{I_p}` equals `2, 1,
0` for good, multiplicative, additive reduction at `p`; `v_l` is the `l`-adic valuation with `v_l(l) = 1`,
extended to `Q^x` and to ideals of `Z_l`; `length` means `Z_l`-length. `q` denotes a bad prime (`q | N`),
`p` any prime. The Hecke algebra `T` is the subring of `End S_2(Gamma_0(N))` generated over `Z` by all `T_n`,
`n >= 1`, including `U_p` for `p | N`.

**C2 `conv-frobenius`** (convention; *stated*; reference: DFG04 1.7.2, Serre's Abelian l-adic
representations I.2, Chapter 7 and 19 cards; paper use: Definition def:terms, Lemma lem:euler, Lemma
lem:tamfactor, the paragraph after Lemma lem:dfg21, Lemma lem:fpr).
Statement. (a) `Frob_p` (arithmetic) is a lift to `G_{Q_p}` of `x -> x^p` on the residue field, well defined
modulo `I_p`; `chi_l(Frob_p) = p`; in `Gal(Q_p^{tame}/Q_p)`, with `t` a topological generator of the pro-`l`
part of tame inertia (`t(p^{1/l^k}) = zeta_{l^k} p^{1/l^k}` for a compatible system of roots of unity and of
roots of `p`), `Frob t Frob^{-1} = t^p`, equivalently `Frob^{-1} t Frob = t^{p^{-1}}` (exponent in `Z_l`).
(b) For a `G_Q`-module `M` (lattice or `Q_l`-space) and `p != l`, `L_p(M, s) = det(1 - Frob_p^{geom} p^{-s} |
M^{I_p})^{-1}`, `Frob_p^{geom} = Frob_p^{-1}`; for `M = V_l E` and `p` good this is `(1 - a_p p^{-s} +
p^{1-2s})^{-1}` with `det(1 - Frob^{geom} X | V) = (1 - alpha X)(1 - beta X)`, `alpha beta = p`, `alpha +
beta = a_p` (on `V_l E` the geometric Frobenius has eigenvalues `alpha, beta`; the arithmetic one has `p/alpha =
beta`, `p/beta = alpha`: the same set, so for the elliptic curve itself the distinction is again invisible).
On `A_f = ad V` at a good prime the eigenvalues are `alpha/beta, 1, beta/alpha`. (c) `L_p(Sym f, s) =
L_p(A_f, s - 1)`; `L_q(Sym f, s) = P_q(q^{-s})^{-1}` defines `P_q in Q[X]`, and `L_q(A_f, 1)^{-1} = P_q(q^{-2})`;
PARI's `lfunsympow(E, 2)` returns `P_q` in this normalisation at every prime, `lfuneuler(S, q)` gives
`1/P_q(X)`. (d) `L_p(M(1), s) = L_p(M, s + 1)`, so `L_p(A_f(1), 0) = L_p(A_f, 1)`.

**C3 `conv-duals`** (convention; *stated*; reference: DFG04 Section 2.1 and (57); Chapter 18 card; paper use:
Section 4.2, Lemma lem:dfg21, Lemma lem:fpr, Lemma lem:h0).
Statement. `Z_l(1) = T_l mu = lim mu_{l^k}` with `Frob_p` acting by `p`; `M(1) = M tensor Z_l(1)`. For `A =
ad T` put `W = A tensor Q_l/Z_l`, `T^D = Hom_{Z_l}(A, Z_l(1))`, `V^D = T^D tensor Q_l`, `W^D = V^D/T^D`. For `l`
odd the trace form `(x, y) -> tr(xy)` on `ad T` is a perfect `G_Q`-equivariant pairing, so `T^D = A(1)` and
`W^D = ad T(1) tensor Q_l/Z_l`, which is the module whose `H^0` defines `h_l(E)`. `H^0(Q, W^D)[l] = H^0(Q, ad
rho bar tensor chi_l bar)`.

### A1. The paper's Section 1: the local terms and the statements (Sections 21.2 to 21.4)

**A1.1 `def-terms`** (definition; *stated* (it is the paper's Definition def:terms); reference: paper
Definition def:terms; paper use: Definition def:terms, Theorem thm:main, Conjecture conj:euler, appendix).
Statement. For a bad prime `q != l`:
`e_l(E, q) = v_l( L_q(A_f, 1)^{-1} / L_q^{nv}(A_f, 1)^{-1} ) = v_l( P_q(q^{-2}) / (1 - a_q(E)^2 q^{-2}) )`,
where `L_q^{nv}(A_f, s) = L_q(A_f, s)` if `delta_q > 0` and `= 1` if `delta_q = 0`, and
`t_l(E, q) = v_l(-v_q(j_E))` if `v_q(j_E) < 0`, `= 0` otherwise.
Facts attached: `e_l(E, q) = 0` at a multiplicative prime (there `delta_q = 1`, so naive = true); at an
additive prime `a_q(E) = 0` so the denominator is `1` and `e_l = v_l(P_q(q^{-2}))`; `t_l(E, q) = v_l(n)` for
type `I_n` at any `q` and for `I_n^*` at odd `q`, since there `v_q(j) = -n`; a type `I_n^*` at `q = 2` may have
`v_2(j) >= 0` (potentially good) and then `t_l = 0`; both terms are invariant under quadratic twist (`e_l`
because `ad V` is unchanged by a twist and `a_q(E)^2` is unchanged when `q` is not the twisting prime, and at the
twisting prime both sides are read from `ad V`; `t_l` because `j` is unchanged).

**A1.2 `prop-table`** (proposition; *proved here* (it is Lemma lem:euler, proved in Section 21.6); reference:
paper table of Section 1; Chapter 19 card; paper use: the table, Lemma lem:euler, Theorem thm:qual, Theorem
thm:quant Step 3).
Statement. Let `q >= 5` be a bad prime, `q != l`, `chi_{-3}` and `chi_{-4}` the quadratic characters of
`Q(sqrt(-3))` and `Q(i)` (`chi_{-3}(q) = 1` iff `q = 1 mod 3`; `chi_{-4}(q) = 1` iff `q = 1 mod 4`), `E'` the
twist of `E` by `Q(sqrt(q*))`, `q* = (-1)^{(q-1)/2} q`, and for type `I_0^*` let `alpha, beta` be the roots of
`X^2 - a_q(E') X + q`. Then:
`I_n`: `L_q(A_f, s)^{-1} = 1 - q^{-1-s}`, `e_l = 0`;
`I_n^*`: `L_q(A_f, s)^{-1} = 1 - q^{-1-s}`, `e_l = v_l(q^2 - 1)`;
`II, II^*, IV, IV^*`: `L_q(A_f, s)^{-1} = 1 - chi_{-3}(q) q^{-s}`, `e_l = v_l(q - chi_{-3}(q))`;
`III, III^*`: `L_q(A_f, s)^{-1} = 1 - chi_{-4}(q) q^{-s}`, `e_l = v_l(q - chi_{-4}(q))`;
`I_0^*`: `L_q(A_f, s)^{-1} = (1 - (alpha/beta) q^{-s})(1 - q^{-s})(1 - (beta/alpha) q^{-s})`,
`e_l = v_l(q - 1) + v_l((q + 1)^2 - a_q(E')^2)`.

**A1.3 `def-tamagawa-factor`** (definition; *stated; reference*; reference: FPR94 I.4.2.2, DFG04 p. 708;
Chapter 18 card; paper use: Section 1.2, Theorem thm:main, Lemma lem:tamfactor, Lemma lem:fpr).
Statement. For a prime `p != l` and a `G_{Q_p}`-stable `Z_l`-lattice `M` (free of finite rank, continuous
action), `Tam_p(M) = Fitt_{Z_l}( (H^1(I_p, M)_{tor})^{G_{Q_p}} )`, the Fitting ideal over `Z_l` of the
`G_{Q_p}`-invariants of the torsion subgroup of `H^1(I_p, M)` (`G_{Q_p}/I_p` acts on `H^1(I_p, M)` by
conjugation); it is an ideal `l^{v} Z_l` of `Z_l` and `v_l(Tam_p(M))` means `v`. For `M = T_l E` it is the
`l`-part of the Tamagawa number `c_p(E)`; for `M = ad T` at a prime of good reduction it is `Z_l` (valuation
`0`); at a multiplicative prime its valuation is given by Lemma lem:tamfactor. The Bloch-Kato Selmer group
`H^1_f(Q, ad T tensor Q_l/Z_l)` is the one of DFG04 Section 2.1 (Chapter 18): classes unramified at every
`p != l` (image in `H^1(I_p, W)` zero, more precisely in the image of `H^1_f(Q_p, V)`), crystalline at `l`,
no condition at infinity for `l` odd.

**A1.4 `thm-main`** (theorem; *proved here* in Section 21.11 as an assembly of A4.* (the assembly is proved;
its inputs DFG04 3.7, 2.7, Prop. 1.4, Lemma 2.1, FPR94 are stated with references); reference: the paper,
Theorem thm:main; paper use: Theorem thm:main).
Statement. Let `E` be `X_0(N)`-optimal and `l` an odd prime with `l` not dividing `2N` such that
`rho bar_{E,l}` restricted to `Gal(Qbar/Q(sqrt(l*)))`, `l* = (-1)^{(l-1)/2} l`, is absolutely irreducible. Then
(eq:identity) `v_l(deg varphi_E) >= length_{Z_l} H^1_f(Q, ad T tensor Q_l/Z_l) + sum_{q | N} v_l(Tam_q(ad T))
+ sum_{q | N} e_l(E, q)`,
with equality when `H^1(X_0(N), Z_l)_m` is free over `T_m`, `m` the maximal ideal of `T tensor Z_l` attached
to `(f, l)` (generated by `l` and the `T_n - a_n(f)`). In particular
(eq:thm) `v_l(deg varphi_E) >= sum_{q | N} e_l(E, q) + sum_{q | N} t_l(E, q)`.
Reading of the hypotheses (item C5 below): `l` odd and `l` not dividing `2N` and absolute irreducibility over
`Q(sqrt(l*))` together say `l` is not in the exceptional set `S_f` of DFG04 (31).

**A1.5 `conj-euler`** (conjecture; *stated* (it is a conjecture of the paper, with its evidence in Section 6);
reference: paper Conjecture conj:euler; paper use: Conjecture conj:euler, Section sec:data, appendix).
Statement. Let `E` be `X_0(N)`-optimal without CM, `l` an odd prime with `E[l]` irreducible, and
`h_l(E) = length_{Z_l} H^0(Q, ad T(1) tensor Q_l/Z_l)`. Then
(eq:rule) `v_l(deg varphi_E) >= sum_{q | N, q != l} e_l(E, q) + sum_{q | N} t_l(E, q) + [l = 3] w_3(E) -
h_l(E)`,
where `w_3(E)` is defined when `3 | N` and the reduction at `3` is potentially good: `w_3(E) = 1` for the
types `II, IV, III^*` at `3`, `2` for `II^*, IV^*`, `0` for `III, I_0^*`; and `w_3(E) = 0` when `3` does not
divide `N` or the reduction at `3` is (potentially) multiplicative. Here `e_l(E, q)` at the wild primes `q
= 2, 3` is Definition def:terms with PARI's factor `P_q`. Facts: `h_l(E) = 0` under the hypothesis of Theorem
thm:main (Lemma lem:h0); `h_l(E) > 0` iff `rho bar = rho bar tensor chi_{l*}`, which for `l = 3` means image
`N_s(F_3)` (label 3Ns); then `h_3(E) = 1` for every such curve of the tables (Section sec:anomaly).

**A1.6 `def-component-groups-and-weights`** (definition; *stated* with the orders proved in Chapter 10;
reference: Silverman ATAEC IV.9 (Tate's algorithm), Chapter 10 card; paper use: Section 1.4, (eq:main),
(eq:twist), Proposition prop:forms, Conjecture conj:eis).
Statement. For a bad prime `q`, `Phig_q = Phi_q(Fbar_q)` is the group of components of the special fibre of
the Neron model of `E` at `q` over `Fbar_q`; `#Phig_q = n` for `I_n`; `1` for `II, II^*`; `2` for `III,
III^*`; `3` for `IV, IV^*`; `4` for `I_0^*` and `I_n^*`. The Tamagawa number `c_q = #Phi_q(F_q)` counts only
the `F_q`-rational components; the paper's statements are about `Phig_q`. For odd `q`, `E^{(q)}` is the
quadratic twist of `E` by `Q(sqrt(q*))`; it has the same Kodaira type as `E` at every prime `p != q`, and at
`q` the types are exchanged `I_n <-> I_n^*` and `I_0 <-> I_0^*` (every odd `q`), `II <-> IV^*`, `IV <->
II^*`, `III <-> III^*` (`q >= 5`) (Lemma lem:twist). The twist-symmetrised weight is
`w_l(E, q) = v_l(n)` if the type at `q` is `I_n`, or `I_n^*` with `q` odd; `= 1` if `l = 3` and the type is
`IV` or `IV^*`, or `II` or `II^*` with `q` odd; `= 0` otherwise. Then
`w_l(E, q) = max( v_l(#Phig_q(E)), v_l(#Phig_q(E^{(q)})) )` for `q >= 5`, and `w_l(E, 2) = v_l(#Phig_2(E))`.
(Check of the max formula: `I_n`/`I_n^*` give `max(v_l(n), v_l(4)) = v_l(n)` for `l` odd; `II <-> IV^*` give
`max(v_l(1), v_l(3)) = [l = 3]`; `III <-> III^*` give `v_l(2) = 0`; `I_0 <-> I_0^*` give `0`.)

**A1.7 `ineq-main-twist`** (definition/statement; *stated* (conjectural inequalities, tested in Section
sec:forms, proved under the hypothesis of Theorem thm:main by Proposition prop:forms); reference: paper (eq:main),
(eq:twist); paper use: Section 1.4, Section sec:forms, Conjecture conj:eis).
Statement. (eq:main) `v_l(deg varphi_E) >= sum_{q | N} v_l(#Phig_q)`; (eq:twist) `v_l(deg varphi_E) >=
sum_{q | N} w_l(E, q)`. Since `w_l(E, q) >= v_l(#Phig_q)` termwise, (eq:twist) implies (eq:main).

**A1.8 `prop-forms`** (proposition; *proved here*; reference: paper Proposition prop:forms; paper use:
Proposition prop:forms).
Statement. Under the hypothesis of Theorem thm:main, (eq:main) and (eq:twist) hold, except possibly when `l =
3` and `E` has type `IV` or `IV^*` at `2`, where they hold as soon as `e_3(E, 2) >= 1`; the same holds under
Conjecture conj:euler when `h_l(E) = 0`. For all `92,812` working-set curves of type `IV` or `IV^*` at `2`,
PARI's factor at `2` is `P_2(X) = 1 + 2X`, so `e_3(E, 2) = v_3(1 + 2/4) = v_3(3/2) = 1`.
Proof plan (termwise comparison of (eq:twist) with (eq:thm), resp. (eq:rule)): type `I_n`: `t_l = v_l(n) =
w_l`; `I_n^*`, `q` odd: `t_l = v_l(n) = w_l`; `I_n^*` at `q = 2`: `w_l(E, 2) = v_l(4) = 0`; `q >= 5` of type
`II, II^*, IV, IV^*`, `l = 3`: `e_3 = v_3(q - chi_{-3}(q)) >= 1 = w_3` because `q = chi_{-3}(q) mod 3` (both
are `1` if `q = 1 mod 3` and `-1 = 2` if `q = 2 mod 3`); `l >= 5`: both `0`; `q = 3`, these types, `l = 3`:
`w_3(E) >= 1 = w_3(E, 3)` by definition of the weights (this is where (eq:rule) rather than (eq:thm) is
needed: in Theorem thm:main `3` does not divide `N`, so the case does not arise); `q = 2`, type `II, II^*`:
`w_l(E, 2) = 0`; `q = 2`, type `IV, IV^*`, `l = 3`: `w_3(E, 2) = 1`, the excepted case, covered when `e_3(E, 2)
>= 1`; types `III, III^*, I_0^*`: `w_l = 0` for odd `l`. All other terms of (eq:thm), (eq:rule) are `>= 0`
(the `e_l` are valuations of `l`-adic integers by Lemma lem:fpr, the `t_l` are `>= 0`, `h_l = 0`).

**A1.9 `history-tamagawa-exponent`** (theorem (statements of Ribet-Takahashi, Pollack-Weston, Kim-Ota);
*stated; reference*; references: RibetTakahashi97, Takahashi01, Pasten, PollackWeston11, KimOta Theorem 1.1
and Definition 2.12; Chapter 14 and 15 cards; paper use: Section 1.5, Remark rem:ko(2)).
Statement. (i) Ribet-Takahashi: for `N = N^+ N^-` with `N^-` a product of an even number of distinct primes
and `E` optimal, the ratio of `deg varphi_E` to the degree of the parametrisation of `E` by the Shimura curve
of discriminant `N^-` is `prod_{q | N^-} n_q` up to primes `l` at which `E[l]` is reducible (precise
hypotheses in the cited papers; Pasten controls the error). (ii) The Tamagawa exponent at a prime `q`:
`t_q = ` the largest `t` with `rho_{E,l} mod l^t` unramified at `q`; for multiplicative `q`, `t_q = v_l(n_q) =
t_l(E, q)` (Lemma lem:tamagawa-exp). (iii) Kim-Ota Theorem 1.1: for `N = N^+ N^-`, `N^-` square-free, `l >= 5`,
`l` not dividing `N`, `l` not in `S_f`, and `rho bar` ramified at every `q | N^-` with `q = +-1 mod l`,
`ord_lambda eta_f(N) = ord_lambda eta_f(N^+, N^-) + sum_{q | N^-} t_f(q)`, where `eta_f(N^+, N^-)` is the
congruence ideal in the `N^-`-new quotient of the Hecke algebra and `t_f(q)` is the Tamagawa exponent. Since
`eta_f(N^+, N^-)` is an integral ideal this gives `v_l(r_E) >= sum_{q | N^-} t_l(E, q)`; Theorem thm:main
contains this inequality for every multiplicative prime without the conditions `l >= 5`, `q != +-1 mod l`,
but not the equality.

**A1.10 `thm-qual`** (theorem; *proved here* in Section 21.8; reference: paper Theorem thm:qual; paper use:
Theorem thm:qual, Section sec:proof).
Statement. Let `E/Q` have conductor `N`, `l` an odd prime not dividing `N` with `rho bar_{E,l}` irreducible
and, if `l = 3`, absolutely irreducible on `Gal(Qbar/Q(sqrt(-3)))`. Let `q != l` be a prime at which `E` has
additive reduction of one of the kinds (a) type `IV` or `IV^*`, `q >= 5`, `l = 3`; (b) type `II` or `II^*`,
`q >= 5`, `l = 3`; (c) type `I_n^*` with `l | n`, `q` odd. Then `l` divides the modular degree of the
`X_0(N)`-optimal curve in the isogeny class of `E`. (For `l >= 5` only irreducibility of `rho bar` is used.)

**A1.11 `thm-quant`** (theorem; *proved here* in Section 21.13; reference: paper Theorem thm:quant; paper use:
Theorem thm:quant, Section sec:twisting).
Statement. Let `l` be an odd prime with `l` not dividing `2N` and `E[l]` irreducible, `S` the set of primes
`q >= 5` at which `E` has type `I_0^*` or `I_n^*`, `E_S` the twist of `E` by `prod_{q in S} chi_q`. Then
`v_l(deg varphi_E) >= v_l(r_{E_S}) + sum_{q in S} e_l(E, q) >= sum_{q in S} e_l(E, q)`, where `r_{E_S}` is the
congruence number of (the optimal curve in the class of) `E_S` at its level `N_S`. Under the hypothesis of
Theorem thm:main the first inequality is an equality when multiplicity one (freeness) holds at level `N`.

**A1.12 `prop-ns`** (proposition; *proved here* in Section 21.14; reference: paper Proposition prop:ns;
Zywina15; Chapter 1, 4, 11 cards; paper use: Proposition prop:ns, Section sec:anomaly, Conjecture conj:euler).
Statement. Let `E/Q` be without CM with `E[3]` irreducible. Then `rho bar_{E,3}` is absolutely irreducible on
`Gal(Qbar/Q(sqrt(-3)))` unless its image is conjugate to the normaliser `N_s(F_3)` (order `8`) of a split
Cartan subgroup of `GL_2(F_3)`; in that case `rho bar_{E,3} = rho bar_{E,3} tensor chi_{-3}`, `H^0(Q, ad rho
bar_{E,3}(1)) != 0` and `h_3(E) >= 1`. The `3`-division polynomial (degree `4`) then factors over `Q` as a
product of two irreducible quadratics, and otherwise (image `GL_2(F_3)` or `N_ns(F_3)`) it is irreducible.

**A1.13 `conj-eis`** (conjecture; *stated*; reference: paper Conjecture conj:eis; Section sec:eis; Chapter 9,
11, 14 cards; paper use: Conjecture conj:eis, Section sec:eis, Open question 4).
Statement. Let `E` be optimal, not CM, with a rational `l`-isogeny, `l` odd, and `D = sum_{q | N} v_l(#Phig_q)
- v_l(deg varphi_E)` the deficit of (eq:main). Then `D <= v_l(#E(Q)_tors) + [E[3] = Z/3 + mu_3]`, and `D <=`
the number of curves in the isogeny class of `E` with a rational point of order `l`. In particular `D <= 0`
when `E` has no rational `l`-torsion point, `D <= 1` for `l >= 5`, `D <= 2` for `l = 3` (a point of order `9`
and the image `Z/3 + mu_3`, label 3Cs.1.1, do not occur together in the tables; this coexistence is not
excluded by a proof, so `D <= 2` is part of the conjecture).

### A2. The paper's Section 2: local invariants (Sections 21.5 to 21.7)

**A2.1 `lem-tamagawa-exp`** (lemma; *proved here*; reference: Silverman ATAEC V.3 and V.5 (Tate curve),
DDT Theorem 3.1(e), Chapter 10 and 11 cards; paper use: Lemma lem:tamagawa-exp, Theorem thm:qual case (c),
Section 1.5, Remark rem:ko).
Statement. Let `q` be a prime of multiplicative reduction, `n_q = v_q(Delta_E)` (`= -v_q(j_E)`), and `l != q`
a prime. Then `rho_{E,l} mod l^t` is unramified at `q` iff `l^t | n_q`; this holds for split and for nonsplit
reduction.
Expanded proof: over `K = ` the unramified quadratic extension of `Q_q` (nonsplit case; `K = Q_q` in the split
case) `E` is isomorphic to the Tate curve `E_u` with `u in Q_q^x`, `v_q(u) = n_q`; `I_q = I_K` is unchanged.
`E_u[l^t] = {zeta^a u^{b/l^t}}` (mod `u^Z`) is generated by `mu_{l^t}` and a chosen `l^t`-th root `u^{1/l^t}`;
`I_q` acts trivially on `mu_{l^t}` (`l != q`) and sends `u^{1/l^t}` to `zeta^{c(sigma)} u^{1/l^t}` with `c`
the Kummer cocycle, which is trivial on inertia iff `u` is an `l^t`-th power in `Q_q^{ur,x}` times a unit, iff
`l^t | v_q(u) = n_q` (units of `Q_q^{ur}` are `l^t`-th powers since `Fbar_q^x` is `l`-divisible and Hensel).

**A2.2 `lem-IV`** (lemma; *proved here*; reference: Kraus90 (semistability defect), Chapter 6 (`Z_3[zeta_3]`
is a DVR with uniformiser `pi = 1 - zeta_3`), Chapter 7, 11 cards; paper use: Lemma lem:IV, Theorem thm:qual
cases (a), (b), Remark rem:types).
Statement. Let `q >= 5` be a prime at which `E` has type `IV` or `IV^*`. Then the image of `I_q` in
`Aut(T_3 E)` is cyclic of order `3`, its image in `Aut(E[3])` is a nontrivial unipotent subgroup, `E[3]^{I_q}`
is a line, `rho bar_{E,3}` is tamely ramified at `q`, and the Serre conductor of `rho bar_{E,3}` has exponent
`1` at `q`.
Expanded proof: `v_q(Delta_min) in {4, 8}`; Kraus: order of image of `I_q` on `T_l E` (any `l != q`) is
`12/gcd(v_q(Delta), 12) = 3`; tame since `q != 3`, so cyclic, generated by `sigma` of order `3` and `det sigma
= chi_3(sigma) = 1` (cyclotomic character trivial on inertia at `q != 3`); eigenvalues primitive cube roots
of unity; `sigma^2 + sigma + 1 = 0` on `T`; `T` is a torsion-free module over `Z_3[sigma]/(sigma^2 + sigma + 1)
= Z_3[zeta_3]`, a DVR with uniformiser `pi = 1 - zeta_3`, `pi^2 = -3 zeta_3`, residue field `F_3`; rank-2 over
`Z_3` forces `T = Z_3[zeta_3]` free of rank one; `E[3] = T/3T = Z_3[zeta_3]/(pi^2)` with `sigma = zeta_3 = 1 -
pi`, nontrivial unipotent (`pi != 0` mod `pi^2`, `(1 - pi)^3 = 1 mod pi^2`... in fact `= 1 - 3pi + ... = 1`
mod `3`), fixed line `pi Z_3[zeta_3]/(pi^2)`; conductor exponent `dim E[3] - dim E[3]^{I_q} + Swan = 2 - 1 +
0 = 1`.

**A2.3 `rem-types`** (proposition (the paper's Remark rem:types); *proof sketched here*; reference: Kraus90,
Chapter 10, 11 cards; paper use: Remark rem:types, Theorem thm:qual (why only (a), (b), (c))).
Statement. For `q >= 5` and the other additive types the image of `I_q` mod `3` is not unipotent: it has order
`2` (`I_0^*`, defect `2`) or `4` (`III, III^*`, defect `4`), or it is `-1` times a nontrivial unipotent (`II,
II^*`, defect `6`), or it is a ramified quadratic character times a unipotent (`I_n^*`: `rho = rho' tensor
chi_q` with `rho'` of type `I_n`). In the last two cases `E[3]^{I_q} = 0` and the Serre conductor exponent of
`rho bar_{E,3}` at `q` is `2`, equal to the conductor exponent of `E`; these are the types whose twist by
`chi_q` lowers the conductor exponent (to `1` for `I_n^*` with `n >= 1`, and `II <-> IV^*` keeps `2` but makes
Lemma lem:IV applicable).

**A2.4 `lem-twist`** (lemma; (i), (ii) *proved here*; (iii) *stated; reference* Atkin-Li Theorem 3.1;
reference: Chapter 10 card (Tate's algorithm, minimal models, twists), Chapter 13 card (Atkin-Li), Chapter 7
(Steinberg twists); paper use: Lemma lem:twist, Section 1.4, Lemma lem:euler, Theorem thm:qual (b), (c),
Theorem thm:main (I_n^* primes), Theorem thm:twist, Theorem thm:quant).
Statement. Let `q` be odd, `chi = chi_q` the quadratic character of conductor `q` (the character of
`Q(sqrt(q*))`), `E^{(q)}` the twist of `E` by `chi`.
(i) At every `p != q`, `E` and `E^{(q)}` have the same Kodaira type, the same `Phig_p` and the same conductor
exponent.
(ii) If `E` has type `I_n` at `q` (`n >= 0`) then `E^{(q)}` has type `I_n^*` at `q` and conversely, same `n`.
If `q >= 5` and `E` has type `II, III, IV` at `q` then `E^{(q)}` has type `IV^*, III^*, II^*` respectively,
and conversely. The conductor exponent of `E^{(q)}` at `q` is `2` when additive and `1` when of type `I_n`,
`n >= 1` (`0` for `I_0`).
(iii) (Atkin-Li) Let `g` be a newform of weight `2` on `Gamma_0(M)` with `q^2` not dividing `M`. Then `g
tensor chi = sum chi(n) a_n(g) q^n` is a newform of weight `2` on `Gamma_0(M')`, `M' = lcm(M, q^2)`: `M' =
M q^2` if `q` does not divide `M`, `M' = M q` if `q || M`.
Expanded proof of (i): `chi` is unramified at `p`, so `E` and `E^{(q)}` are isomorphic over the unramified
quadratic extension `Q_p(sqrt(q*))` (or already over `Q_p`), and type, `Phig_p`, conductor exponent are
invariant under unramified base change (Neron model commutes with etale base change). (ii): the twist of a
minimal model `(a_1, ..., a_6)` has a model with `c_4' = q^2 c_4`, `c_6' = q^3 c_6`, `Delta' = q^6 Delta`,
`j' = j` (model `y^2 = x^3 + q* a_2 x^2 + q*^2 a_4 x + q*^3 a_6` after completing the square, `q` odd).
Potentially multiplicative: `v_q(j) < 0`, type `I_n` or `I_n^*` with `n = -v_q(j)` according as multiplicative
or additive, and a ramified quadratic twist exchanges them (the twist of a Tate curve by a ramified character
is additive; the twist of `I_n^*` by the same character is a Tate curve again). `I_0 <-> I_0^*`: Tate's
algorithm criterion (cubic `T^3 + a_2 T^2 + a_4 T + a_6` with distinct roots mod `q` and `q | a_i`-shape
gives `I_0^*`); conversely a type `I_0^*` curve at odd `q` has such a model, so its twist is good. `q >= 5`,
potentially good: type determined by `v_q(Delta_min) in {0, 2, 3, 4, 6, 8, 9, 10}` for `I_0, II, III, IV,
I_0^*, IV^*, III^*, II^*`; twisting adds `6`, minimal iff `< 12`, else subtract `12`: `2 -> 8`, `3 -> 9`, `4
-> 10`, `8 -> 14 - 12 = 2`, `9 -> 3`, `10 -> 4`, `0 -> 6`, `6 -> 0`. Conductor exponents tame for `q` odd.
(iii) reference; in the case `q || M` the local component of `g` at `q` is an unramified twist of Steinberg,
whose twist by a ramified quadratic character has conductor exponent `2` (Chapter 7), so `M' = Mq`.

**A2.5 `lem-euler`** (lemma; *proved here* (the computation of `(ad V)^{I_q}` and Frobenius eigenvalues in
each case, Chapter 19 does the same in its own language; Chapter 21 walks through the paper's proof);
reference: Kraus90, Chapter 7, 11, 15, 19 cards; paper use: Lemma lem:euler, the table, Theorem thm:quant
Step 3, Lemma lem:fpr).
Statement: as A1.2.
Expanded proof plan. General principle: `L_q(A_f, s)^{-1} = prod (1 - lambda q^{-s})` over the eigenvalues
`lambda` of `Frob_q` on `(ad V)^{I_q}`, normalised so that a good prime has eigenvalues `alpha/beta, 1,
beta/alpha`. `I_n`: local component Steinberg (unramified twist); `rho|_{G_{Q_q}} = (chi_l eps, kappa; 0, eps)` in a
basis `e_1, e_2` (C2(a), arithmetic). Inertia acts through `t` with `t e_1 = e_1`, `t e_2 = e_2 + n' e_1`,
`n' != 0`; on `ad V` (basis `e = E_{12}`, `h = E_{11} - E_{22}`, `f = E_{21}`) one has `(t - 1)e = 0`, `(t -
1)h = -2n' e`, `(t - 1)f = n' h - n'^2 e`, so `(ad V)^{I_q} = Q_l e`. Conjugation by `rho(Frob) = (eps q, c';
0, eps)` sends `e` to `q e` (matrix computation `g E_{12} g^{-1} = q E_{12}`), so the GEOMETRIC Frobenius has
eigenvalue `q^{-1}` on `(ad V)^{I_q}` and `L_q(A_f, s)^{-1} = 1 - q^{-1} q^{-s} = 1 - q^{-1-s}` (C2(b)). The
naive factor is `1 - a_q^2 q^{-2}` at `s = 1` with `a_q^2 = 1`, i.e. `1 - q^{-2} = L_q(A_f, 1)^{-1}`, so `e_l =
0`. (Same conclusion from the Weil-Deligne picture of Chapter 7: `ad(sp(2))` has `ker N` of dimension... the
writer may give this as a remark only.)
`I_n^*`: `V = V' tensor chi_q`, `V'` Steinberg, `ad V
= ad V'`, same factor, but `a_q = 0` so naive factor `1`, `e_l = v_l(1 - q^{-2}) = v_l(q^2 - 1)`. `II, II^*,
IV, IV^*`: image of `I_q` cyclic of order `3` or `6` generated by `sigma` or `-sigma`, eigenvalues
`zeta_3^{+-1}`; on `ad V` the sign disappears; `End_{I_q}(V) = Z_l[zeta_3]` (`V` is free of rank one over
`Q_l(zeta_3)` as `I_q`-module); `(ad V)^{I_q} = ` trace-zero part of `End_{I_q}(V)`, the line spanned by
`sqrt(-3) = zeta_3 - zeta_3^{-1} = 2 zeta_3 + 1`; `Frob_q` normalises the image of inertia and acts on
`<sigma>` by `sigma -> sigma^q` (the relation `Frob t Frob^{-1} = t^q`), so it centralises `sigma` if `q = 1 mod
3` and inverts it if `q = 2 mod 3`; conjugation by `Frob` on `End_{I_q}(V)` is a ring automorphism of
`Z_l[zeta_3]` which is the identity or the conjugation `zeta_3 -> zeta_3^{-1}`, so it acts on `sqrt(-3)` by
`+1` resp. `-1`, that is by `chi_{-3}(q)`; `L_q(A_f, s)^{-1} = 1 - chi_{-3}(q) q^{-s}`; `a_q = 0` so `e_l =
v_l(1 - chi_{-3}(q) q^{-1}) = v_l(q - chi_{-3}(q))`. `III, III^*`: order `4`, eigenvalues `+-i`, `End_{I_q}(V)
= Z_l[i]`, invariant line spanned by `i` (the diagonal element `diag(i, -i)` in an eigenbasis), `Frob` acts
by `i -> i^q`, i.e. by `chi_{-4}(q)`; `e_l = v_l(q - chi_{-4}(q))`. `I_0^*`: `V = V' tensor chi_q`, `V'`
unramified with eigenvalues `alpha, beta` of `Frob_q` (those of `E'`, `alpha + beta = a_q(E')`, `alpha beta =
q`); `ad V = ad V'` unramified, eigenvalues `alpha/beta, 1, beta/alpha`; `L_q(A_f, 1)^{-1} = (1 - alpha/(beta
q))(1 - 1/q)(1 - beta/(alpha q))`; algebra: `(1 - alpha/(beta q))(1 - beta/(alpha q)) = 1 - (alpha^2 +
beta^2)/(alpha beta q) + 1/q^2 = 1 - (a^2 - 2q)/q^2 + 1/q^2 = ((q + 1)^2 - a^2)/q^2` with `a = a_q(E')`;
times `(q - 1)/q`; `e_l = v_l(q - 1) + v_l((q + 1)^2 - a^2)` (for `l != q`).
Pitfall for the writer: `alpha/beta` is in general not in `Q_l`; the eigenvalues live in `Q_l(alpha)`; the
product is rational. Also `chi_{-3}(q) = (q/3)` (Legendre) `= (-3/q)` by reciprocity.

**A2.6 `rem-wild`** (example (the paper's Remark rem:wild); *stated* with worked PARI values; reference:
paper Remark rem:wild, Chapter 19 and 22 cards; paper use: Remark rem:wild, Conjecture conj:euler, Section
sec:wild, Proposition prop:forms).
Statement. At `q = 2, 3` the Kodaira type does not determine `L_q(A_f, s)`, but Definition def:terms applies
verbatim with PARI's factor: a type `IV` at `2` has `P_2(X) = 1 + 2X`, so `e_3(E, 2) = v_3(1 + 2 * 2^{-2}) =
v_3(3/2) = 1`; a type `II` at `2` has `P_2 = 1` and `e_3 = 0`; a type `I_n^*` at `2` has potentially good
reduction in about half the cases, then `P_2` is a cubic and `t_l(E, 2) = 0`. At `q = l` the Euler factor is
not the relevant quantity; the weights `w_3` of Conjecture conj:euler are empirical.

**A2.7 `lem-tamfactor`** (lemma; *proved here*, every step; reference: FPR94 I.4.2.2, DFG04 p. 708, DDT
Theorem 3.1(e), Chapters 3, 7, 16, 17, 18 cards; paper use: Lemma lem:tamfactor, Theorem thm:main (eq:thm),
Remark rem:ko(1), Section sec:tam, Open question 3).
Statement. Let `q` be a prime of multiplicative reduction, `n = n_q = v_q(Delta_E)`, `l` an odd prime, `l !=
q`, `T = T_l E`, `M = ad T`. Let `q_E in Q_q^x` be the Tate parameter (`v_q(q_E) = n`), `u = q_E q^{-n}` its
unit part, and `c in Z/l^{v_l(q-1)}` the class of `u` in `F_q^x/(F_q^x)^{l^{v_l(q-1)}}` (a cyclic group of
order `l^{v_l(q-1)}`, identified with `Z/l^{v_l(q-1)}` by a choice of generator), so that `v_l(c) >= k` iff
`u` is an `l^k`-th power in `F_q^x`, for `k <= v_l(q - 1)`. Then `H^1(I_q, M)_{tor} = (Z/l^{v_l(n)})^2` and
`v_l(Tam_q(ad T)) = v_l(n) + min( v_l(n), v_l(q - 1), v_l(c) )`.
In particular `v_l(Tam_q(ad T)) >= t_l(E, q)`, with equality unless `q = 1 mod l`, `l | n` and `u` is an
`l`-th power in `F_q^x`.
Expanded proof, the exact facts invoked (each is a card entry of the chapter named):
(1) [Ch. 11, DDT 3.1(e)] over the unramified quadratic extension `E` is a Tate curve; `T` has a basis `e_1, e_2`
with `G = G_{Q_q}` acting by `(chi_l eps, kappa; 0, eps)`, `eps` unramified of order `<= 2`, `kappa in H^1(G,
Z_l(1)) = lim Q_q^x/(Q_q^x)^{l^k}` the Kummer class of `q_E`.
(2) [Ch. 7] `I = I_q` acts on `T` through its maximal pro-`l` tame quotient `Z_l(1)`, generated by `t`; the
restriction of the Kummer class of `q_E` to `I` is `v_q(q_E) = n` times the tame character, so `t e_1 = e_1`,
`t e_2 = e_2 + n' e_1` with `n' = n * (unit)`, `v_l(n') = v_l(n)`.
(3) [Ch. 16] the kernel of `I -> <t>` has trivial pro-`l` quotient (it is `P_q x prod_{l' != l} Z_{l'}(1)`), so
`H^1(ker, M') = 0` for `M'` a `Z_l`-module of finite type and inflation-restriction gives `H^1(I, M') =
H^1(<t>, M')`; and for the procyclic group `<t> = Z_l` acting continuously on a finitely generated
`Z_l`-module `M'`, `H^1(<t>, M') = M'/(t - 1)M'` via `c -> c(t)`.
(4) [Ch. 3/16, computation] basis `e = e_1 tensor e_2^vee`, `h = e_1 tensor e_1^vee - e_2 tensor e_2^vee`,
`f = e_2 tensor e_1^vee` of `M = ad T`; `t` acts on `ad T` by conjugation; `(t - 1)e = 0`, `(t - 1)h = -2n'
e`, `(t - 1)f = n' h - n'^2 e`; since `2` is a unit, `(t - 1)M = n'(Z_l e + Z_l h)`; so `H^1(I, M) =
(Z_l/n') e bar + (Z_l/n') h bar + Z_l f bar`, torsion `(Z/l^{v_l(n)})^2`.
(5) [Ch. 16] `G/I` acts on `H^1(I, M)` by `(sigma . c)(i) = sigma c(sigma^{-1} i sigma)`; with
`Frob^{-1} t Frob = t^{q^{-1}}` (C2(a)) and `c(t^k) = k c(t)` mod `(t - 1)M` (cocycle identity `c(t^k) = (1 +
t + ... + t^{k-1}) c(t)`), the arithmetic Frobenius acts on `M/(t - 1)M` as `q^{-1} Ad(rho(Frob))`.
(6) [computation] `rho(Frob) = (eps q, c'; 0, eps)` (`eps = eps(Frob) = +-1`, `c' = kappa(Frob)`); `Ad` sends
`e -> q e`, `h -> h - 2 c' eps e` (compute `g h g^{-1}`); so on `H^1(I, M)_{tor}`: `e bar -> q^{-1} q e bar = e
bar`, `h bar -> q^{-1}(h bar - 2 c' eps e bar)`. Fixed points `x e bar + y h bar` (`x, y in Z/l^{v_l(n)}`):
need `q^{-1} y = y` and `x - 2 c' eps q^{-1} y = x`, i.e. `(q - 1) y = 0` and `c' y = 0` in `Z/l^{v_l(n)}`;
`x` free: `l^{v_l(n)}` choices; `y`: `l^{min(v_l(n), v_l(q-1), v_l(c'))}` choices. The invariants form a group
`Z/l^{v_l(n)} + Z/l^{min(...)}`, whose Fitting ideal has valuation `v_l(n) + min(v_l(n), v_l(q - 1), v_l(c'))`
[Ch. 3: Fitting ideal of a finite `Z_l`-module is `l^{length}`].
(7) [Ch. 17] `c'` is the image of `kappa` in `H^1(G/I, Z_l(1)^I) = H^1(<Frob>, Z_l(1)) = Z_l(1)/(q - 1) =
Z/l^{v_l(q-1)}`, which by Kummer theory is the class of the unit part `u` of `q_E` in `F_q^x tensor Z_l`,
well defined modulo `q - 1`: so `v_l(c') = v_l(c)` in the stated sense (`min(v_l(c'), v_l(q - 1)) = min(v_l(c),
v_l(q-1))`).
(8) [Ch. 18] `Tam_q(M) = Fitt(H^1(I, M)_{tor}^G)` is FPR94 I.4.2.2 as recalled in DFG04 p. 708.
(9) Check for `M = T`: `(t - 1)T = n' Z_l e_1`, `H^1(I, T) = (Z_l/n') e_1 bar + Z_l e_2 bar`, torsion `(Z/l^{v_l(n)})
e_1 bar`, `Frob` acts by `q^{-1} * eps q = eps`; invariants: all of it if `eps = 1` (split), the `2`-torsion
(trivial, `l` odd) if `eps = -1`; so `v_l(Tam_q(T)) = v_l(n)` split, `0` nonsplit: the `l`-part of `c_q(E) = n`
(split) or `1 or 2` (nonsplit). Consistent.
(10) The "in particular": `t_l(E, q) = v_l(n)`; the extra term is `>= 1` iff `v_l(n) >= 1`, `v_l(q - 1) >= 1`
and `v_l(c) >= 1`.

### A3. The paper's Section 3: proof of Theorem thm:qual (Sections 21.8 to 21.9)

**A3.1 `def-congruence-number`** (definition; *stated* (definitions of the paper and of ARS12 Section 2);
reference: ARS12 Section 2 and Theorem 2.2, Chapter 13, 14 cards; paper use: Section 1, Section 3 preamble,
Lemma lem:crit, Lemma lem:hecke, Theorem thm:twist).
Statement. `r_E` (for `E` optimal of level `N`, newform `f`) is the largest integer `r` such that `f = g mod r`
coefficientwise for some `g in S_2(Gamma_0(N); Z)` orthogonal to `f` for the Petersson product. `T` is the
full Hecke algebra of level `N` (C1). Agashe-Ribet-Stein Theorem 2.2: `deg varphi_E | r_E`, and `v_p(deg
varphi_E) = v_p(r_E)` for every prime `p` with `p^2` not dividing `N`. (Example 99A1: `N = 9 * 11`, `deg = 4`,
`r = 12`, `v_3` differs; this is why `l` not dividing `N`, or at least `l^2` not dividing `N`, is needed to
pass from `r_E` to `deg varphi_E`.)

**A3.2 `lem-crit`** (lemma; *proved here* (expanded; Chapter 15 and 20 also prove it; the tour follows the
paper's proof line by line); reference: Ribet83 Theorem 2.2, AU96 Lemma 2.1, ARS12 Section 3, Chapter 3, 13
cards; paper use: Lemma lem:crit, Lemma lem:old, Lemma lem:hecke, Theorem thm:twist, Theorem thm:quant Step 1).
Statement. Let `phi_f : T -> Z`, `T_n -> a_n(f)`, `I = ker phi_f`, `J = Ann_T(f^perp)`. Then `T/(I + J)` is
cyclic of order `r_E`; equivalently `r_E` generates the congruence ideal `phi_f(J) = phi_f(Ann_T I)`.
Consequently, if `g in S_2(Gamma_0(N)) tensor Qbar` is a normalised eigenform for all of `T`, orthogonal to
`f`, with coefficients in the ring of integers `O` of a number field, and `lambda | l` is a prime of `O` with
`a_n(g) = a_n(f) mod lambda` for every `n >= 1`, then `l | r_E`. The same holds with `Z` replaced by `Z_l`
and `r_E` by its `l`-part.
Expanded proof steps: (1) `T tensor Q = Q x T'`, `T'` faithful on `f^perp` (`f`-line and `f^perp` are
`T`-stable: `f` is an eigenvector of the adjoints `T_n^*` too, since `T_n^* = w_N T_n w_N` for `n` prime to
`N`... the writer should use: for `(n, N) = 1`, `T_n` is self-adjoint; for `p | N`, `U_p^* = w_N U_p w_N` and
`f` is an eigenvector of `w_N`); so `I = T cap (0 x T')`, `J = T cap (Q x 0)`, `I cap J = 0`, `J = Ann_T I`,
`T/(I + J) = Z/phi_f(J)`, cyclic of order `r'`. (2) The pairing `S_2(Gamma_0(N); Z) x T -> Z`, `(g, t) -> a_1(t
g)`, is perfect [Ch. 13]; under it the forms killed by `I` are `Z f` and the forms killed by `J` are `L =
f^perp cap S_2(Gamma_0(N); Z)`. (3) Dualising `T -> T/I x T/J` (cokernel `T/(I + J)`) gives `[S_2(Z) : Z f +
L] = r'`. (4) `S_2(Z)/(Z f + L)` embeds in `Q f/Z f` by projection along `f^perp`, so it is cyclic, generated
by a form `h` with projection `f/r'`; `r' h = f + g_0`, `g_0 in L`, so `f = -g_0 mod r'` and `r' <= r_E`;
conversely `f = g_1 mod r_E` with `g_1 in L` gives the integral form `(f - g_1)/r_E` of order `r_E` in the
quotient, so `r_E | r'`. Hence `r_E = r'`. (5) `phi_g` kills `J` (`g in f^perp`) and `phi_g = phi_f mod lambda`
on all of `T`, so `phi_g(I) subset lambda`; `I + J subset ker(T -> O/lambda)`, a maximal ideal of residue
characteristic `l`; so `l | #T/(I + J) = r_E`. (6) Over `Z_l` verbatim, the pairing stays perfect after
tensoring.

**A3.3 `lem-old`** (lemma; *proved here* (expanded, the five prime-by-prime cases); reference: Atkin-Lehner
Theorem 3, Edixhoven92 Section 2, DDT Theorem 3.1(e), Chapters 4, 5, 11, 13, 15 cards; paper use: Lemma
lem:old, cases (a), (b), (c)).
Statement. Let `h` be a newform of weight `2` on `Gamma_0(M)`, `M | N`, `h != f`, coefficients in `O`, and
`lambda | l` a prime of `O` with `a_p(h) = a_p(f) mod lambda` for all primes `p` not dividing `l N`. Assume
`p` does not divide `M` for every prime `p || N` at which `rho bar` is unramified. Then, after enlarging `O`
and `lambda`, the span of the `h(dz)`, `d | N/M`, contains an eigenform `g` as in Lemma lem:crit; consequently
`l | r_E`.
Expanded proof: the `T`-stable span `V` of the `h(dz)` is orthogonal to `f` [Ch. 13: old space orthogonal to
newforms; for `M = N`, distinct newforms are orthogonal]; action of `T_n`, `(n, N) = 1`, by `a_n(h)`; `U_p` for
`p | M` with `v_p(M) = v_p(N)` by `a_p(h)`; for `p | N/M`, `e_p = v_p(N/M)`, on the span of `h(p^j z)`, `0 <=
j <= e_p`: `U_p h(p^j z) = h(p^{j-1} z)` (`j >= 1`), `U_p h = a_p(h) h - p h(pz)` (`p` not dividing `M`),
`U_p h = a_p(h) h` (`p | M`); eigenvalues: roots `alpha_p, beta_p` of `X^2 - a_p(h) X + p`, plus `0` if `e_p
>= 2` (`p` not dividing `M`); `a_p(h)`, plus `0` if `e_p >= 1` (`p | M`); eigenvectors: `h - beta_p h(pz)`, `h
- alpha_p h(pz)`, `h`, and for `0`: `h - a_p(h) h(pz) + p h(p^2 z)` (`p` not dividing `M`), `h - a_p(h) h(pz)`
(`p || M`), `h` itself (`p^2 | M`, where `a_p(h) = 0`); `V` is the tensor product of the local spans and `T`
is commutative, so for each choice of `mu_p` there is a common eigenform `g`, normalised `a_1(g) = 1`;
congruence for all `n` follows from multiplicativity, `a_{p^k} = a_p^k` for `p | N`, and the recursion
`a_{p^{k+1}} = a_p a_{p^k} - p a_{p^{k-1}}` for `p` not dividing `N`. Cases: `p` not dividing `l N`: by
hypothesis; hence `rho bar_h = rho bar` (Chebotarev + Brauer-Nesbitt, `rho bar` irreducible). `p = l`:
weight `2`, level prime to `l`; Deligne-Fontaine (Edixhoven Section 2): `a_l mod lambda` is determined by
`rho bar|_{D_l}` (`0` if irreducible, else the Frobenius eigenvalue on the unramified quotient); so `a_l(h) =
a_l(f) mod lambda`. `p^2 | N`: `a_p(f) = 0`; if `v_p(M) = v_p(N)` then `a_p(h) = 0` (Atkin-Lehner Theorem
3); else `e_p >= 1` (and `>= 2` if `p` not dividing `M`) so `0` is available: `mu_p = 0`. `p || N`, `rho bar`
unramified at `p`: `p` not dividing `M`, `e_p = 1`, `mu_p in {alpha_p, beta_p}`; `rho|_{D_p}` is an
extension of unramified `eps` by `eps chi_l` with `eps(Frob_p) = a_p(f) = +-1` (DDT 3.1(e)), so `rho
bar(Frob_p)` has eigenvalues `a_p(f) p, a_p(f)`; `rho bar_h = rho bar` unramified at `p` with `p` not
dividing `M` gives `X^2 - a_p(h) X + p = (X - a_p(f) p)(X - a_p(f)) mod lambda`, so one of `alpha_p, beta_p`
is `= a_p(f)` modulo a prime above `lambda` in `O[alpha_p]`: take it. `p || N`, `rho bar` ramified at `p`:
then `p | M` (else `rho bar_h` unramified at `p`), `v_p(M) = 1`, `a_p(g) = a_p(h) = +-1`; both `rho bar|_{D_p}`
and `rho bar_h|_{D_p}` are non-split extensions of an unramified character by its `chi_l bar`-twist with
Frobenius eigenvalue `a_p(f)`, resp. `a_p(h)`, on the unramified quotient; a non-split extension of two
characters has a unique stable line, so the isomorphism matches sublines and quotients: `a_p(h) = a_p(f) mod
lambda`.

**A3.4 `thm-optimal-level`** (theorem; *stated; reference*; reference: DDT Theorem 3.15 (Ribet90, Carayol89,
Diamond95), Carayol89 for `N(rho bar) | N(E)`, Chapter 11, 15 cards; paper use: Section 3 (the
optimal-level paragraph), cases (a), (b), (c), the remark after the example).
Statement. Let `l` be odd and `sigma bar : G_Q -> GL_2(Fbar_l)` irreducible and modular, absolutely
irreducible on `Gal(Qbar/Q(sqrt(-3)))` if `l = 3`. Then `sigma bar` arises from a newform of weight `2` and
level `N(sigma bar) l^{delta(sigma bar)}` with nebentypus of order prime to `l`, where `N(sigma bar)` is the
Serre conductor (prime to `l`) and `delta(sigma bar) = 0` when `sigma bar|_{D_l}` is good (arises from a
finite flat group scheme over `Z_l`). Corollary used by the paper: for `sigma bar = rho bar_{E',l}` with
`E'/Q` of conductor prime to `l` (and `sigma bar` irreducible, absolutely irreducible over `Q(sqrt(-3))` if `l
= 3`), `sigma bar` arises from a newform of weight `2` on `Gamma_0(N(sigma bar))`: `rho bar|_{D_l}` comes
from `E'[l]`, hence is good; `det sigma bar = chi_l bar` forces the nebentypus (trivial mod `lambda`, order
prime to `l`) to be trivial. Also: `N(rho bar_{E',l})` divides the conductor of `E'` (Carayol), and
`N(sigma bar)` is prime to every prime at which `sigma bar` is unramified. Case `q || N`, `sigma bar`
unramified at `q`: this is Ribet's level-lowering theorem (Ribet90).

**A3.5 `proof-thm-qual`** (theorem (proof of Theorem thm:qual, cases (a), (b), (c)); *proved here*; reference:
paper Section sec:proof; paper use: Theorem thm:qual).
Case (a): `q^2 || N`, `l = 3`; Lemma lem:IV gives `v_q(N(rho bar)) = 1`, so `M = N(rho bar) | N/q`;
optimal-level theorem gives `g` on `Gamma_0(M)` with `rho bar_g = rho bar`, i.e. `a_p(g) = a_p(f) mod lambda`
for `p` not dividing `3N`; `h = g`, `M < N`, and `p` not dividing `M` whenever `rho bar` is unramified at `p`;
Lemma lem:old gives `3 | r`. Case (b): `q^2 || N`, `l = 3`, type `II/II^*`; `chi = chi_q`, `E' = E^{(q)}` has
type `IV^*/IV` at `q`, same types elsewhere (Lemma lem:twist (i), (ii)), conductor `N`, newform `f' = f
tensor chi` on `Gamma_0(N)` (Atkin-Li, or directly from `rho_{E'} = rho tensor chi` and modularity); `rho bar
tensor chi` satisfies the hypotheses (irreducibility and absolute irreducibility over `Q(sqrt(-3))` are
invariant under twisting by a character); Lemma lem:IV for `E'`: `v_q(N(rho bar tensor chi)) = 1`, `M |
N/q`; optimal-level theorem gives `g` on `Gamma_0(M)` with `a_p(g) = chi(p) a_p(f) mod lambda`, `p` not
dividing `3N`; `q || M` (exponent exactly `1`), so `h = g tensor chi` is a newform on `Gamma_0(Mq)`, `Mq | N`
(Lemma lem:twist (iii)); `a_p(h) = chi(p)^2 a_p(f) = a_p(f) mod lambda` for `p` not dividing `3N`; `h != f`
(else `g = h tensor chi = f tensor chi = f'` of level `N > M`); hypothesis of Lemma lem:old: `p || N`
unramified for `rho bar` implies `p != q`, `rho bar tensor chi` unramified at `p`, `p` not dividing `M`, so `p`
not dividing `Mq`; Lemma lem:old gives `3 | r`. Case (c): type `I_n^*` at odd `q != l`, `l | n`, `q^2 || N`;
`E' = E^{(q)}` has type `I_n` at `q`, conductor `N/q`; `f' = f tensor chi` on `Gamma_0(N/q)` with `q || N/q`;
Lemma lem:tamagawa-exp for `E'`: `rho bar tensor chi` unramified at `q` (as `l | n`); `M = N(rho bar tensor
chi)` prime to `q`, `M | N/q^2`; optimal-level theorem (Ribet's case) gives `g` on `Gamma_0(M)` with `a_p(g) =
chi(p) a_p(f) mod lambda`, `p` not dividing `l N`; `q` not dividing `M` so `h = g tensor chi` is a newform on
`Gamma_0(M q^2)`, `M q^2 | N`; congruent to `f` at `p` not dividing `l N`; `h != f` (else `g = f'` of level
`N/q != M`); hypothesis of Lemma lem:old as in (b); `l | r`. Finally `v_l(deg varphi_{E_0}) = v_l(r)` because
`l` does not divide `N` (ARS12 Theorem 2.2).

**A3.6 `example-abc`** (example; worked verification; reference: paper Example after case (c); Cremona
tables, LMFDB; paper use: the example of Section 3, Section 7.3 of PLAN (worked verifications)).
Statement. (b) 121a1 (`[1,1,1,-30,-76]`, type `II` at `11`, `v_11(Delta) = 2`... the writer checks with PARI):
twist by `-11` is in class 121c, type `IV^*` at `11`; its mod `3` representation has Serre conductor `11` and is
congruent to the form of 11a1; `f_{11a} tensor chi_{-11}` is the form of 121d; `a_p(121a1) = chi_{-11}(p)
a_p(11a1) mod 3` for all `p != 3, 11` (checked `p < 500`); `deg varphi_{121a1} = 6`, `e_3(E, 11) = v_3(11 -
chi_{-3}(11)) = v_3(11 + 1) = 1` (`11 = 2 mod 3`), bound `1`, attained (`v_3(6) = 1`). (c), `l = 3`: 539c1
(`539 = 7^2 * 11`), type `I_3^*` at `7`; twist by `-7` has conductor `77`, type `I_3` at `7`; `a_p(539c1) =
chi_{-7}(p) a_p(11a1) mod 3`, `p != 3, 7, 11` (checked `p < 1000`); `deg = 2^5 * 3^2`; `e_3(E, 7) = v_3(7^2
- 1) = v_3(48) = 1`, `t_3(E, 7) = v_3(3) = 1`, bound `2 = v_3(deg)`, attained. (c), `l = 5`: 980i1 (`980 = 2^2
* 5 * 7^2`), type `I_5^*` at `7`; twist by `-7` has conductor `140`, type `I_5` at `7`; `a_p(980i1) =
chi_{-7}(p) a_p(20a1) mod 5`, `p != 2, 5, 7` (checked `p < 1000`); `deg = 2^6 * 3^2 * 5`; `e_5(E, 7) = v_5(48)
= 0`, `t_5(E, 7) = v_5(5) = 1`, bound `1 = v_5(deg)`. Note: here `5 | N`, so Theorem thm:main does not apply
(`l | N`), but Theorem thm:qual (c) applies since it only needs `l` not dividing... CAUTION: Theorem thm:qual
requires `l` not dividing `N`, and `5 | 980`. The paper lists 980i1 as an example of the congruence, not of
the theorem; the writer must say so explicitly (the remark after the example says the data show the
conclusion also when `l || N`).

**A3.7 `rem-l-divides-N`** (example (the paper's remark on `l | N` and 99A1); *stated*; reference: ARS12
Table 1; paper use: the remark after the example).
Statement. `l` not dividing `N` is used (i) in the optimal-level theorem (`delta = 0`, weight `2`), (ii) in
Lemma lem:old at `p = l`, (iii) to pass from `r` to `deg varphi`, where only `l^2` not dividing `N` is needed
and cannot be dropped: 99A1 (`N = 9 * 11`) has `deg = 4`, `r = 12`. The data show the conclusion of Theorem
thm:qual for every curve with `l || N` or `l^2 | N` and a prime of one of the three kinds, and also at `q = 3`
in cases (a), (b) where Lemma lem:IV does not apply (wild).

### A4. The paper's Section 4: the congruence ideal and the adjoint Selmer group (Sections 21.10 to 21.13)

**A4.1 `constr-dfg-lattice`** (construction; *stated; reference* (the objects of DFG04 read for weight 2,
trivial character); reference: DFG04 1.5.3, 1.6.2, 1.7.3, (13), (14), 1.6.1, 1.8.2; DDT 4.4; Chapter 8, 13,
14, 20 cards; paper use: Section 4.1, Lemma lem:hecke, Theorem thm:quant Step 2).
Statement. Let `f` be a newform of weight `2` on `Gamma_0(M)` with rational coefficients, `lambda = l` a prime
not dividing `2M`, `Sigma` a finite set of primes. `M^Sigma = M prod_{p in Sigma} p^{delta_p}` (`delta_p = 2,
1, 0` for `p` good, multiplicative, additive for `f`), `f^Sigma = sum_{(n, Sigma) = 1} a_n(f) q^n`, the
`Sigma`-depleted form, an eigenform of the full Hecke algebra of level `M^Sigma` with `U_p f^Sigma = 0` for
`p in Sigma` (Lemma lem:old's depleted forms). `M(M^Sigma, 1)_{!, lambda} = H^1(X_0(M^Sigma), Z_l)` with its
Hecke action (all `T_n`, `U_p`). `M_{f^Sigma, lambda} = ` the sublattice of `H^1(X_0(M^Sigma), Z_l)` killed by
`ker(phi_{f^Sigma})`, `phi_{f^Sigma} : T(M^Sigma) -> Z`; it is free of rank `2` over `Z_l`; for `Sigma` empty
it is homothetic to `T_l E` (dually `T_l E(-1)`, same `ad`) when `rho bar` is irreducible [Ch. 4, 15: Ribet's
lemma on lattices]. The pairing `delta hat_!` is the cup product composed with the Atkin-Lehner involution
`w_{M^Sigma}` (for weight `2` and trivial character the operator `[U w U] omega` of DFG04 (13), (14) is
`w_{M^Sigma}`): `delta hat_!(x, y) = <x, w y>`; it is perfect and alternating on `H^1(X_0(M^Sigma), Z_l)`,
and every `T_n` and `U_p` is self-adjoint for it because `w T_n w^{-1}` is the cup-product adjoint of `T_n`
[Ch. 14]. The naive `Sigma`-finite congruence ideal `eta^Sigma_{f, lambda} subset Z_l` is the ideal of
values of `delta hat_!` on `M_{f^Sigma, lambda} x M_{f^Sigma, lambda}`; equivalently the Gram determinant of
`delta hat_!` on a basis of `M_{f^Sigma, lambda}` is `(eta^Sigma_{f, lambda})^2` up to a unit (a rank-two
alternating form has Gram matrix `(0, a; -a, 0)` with `a` a generator of the ideal of values, determinant
`a^2`).

**A4.2 `thm-dfg14`** (theorem; *stated; reference*; reference: DFG04 Proposition 1.4(c); Chapter 15, 19, 20
cards; paper use: Theorem thm:dfg14, proof of Theorem thm:main, Theorem thm:quant Step 3, the remark after
Theorem thm:quant).
Statement. If `rho bar_f` is irreducible (and `l` does not divide `2M`), then `eta^Sigma_{f, lambda} =
eta^empty_{f, lambda} prod_{p in Sigma} L_p^{nv}(A_f, 1)^{-1}` (as ideals of `Z_l`; the factors are nonzero
`l`-adic integers). Reading: additive `p in Sigma` (`delta_p = 0`): factor `1`, level unchanged, ideal
unchanged; good `p`: factor `(1 - (alpha/beta) p^{-1})(1 - p^{-1})(1 - (beta/alpha) p^{-1}) = ((p - 1)/p)
((p + 1)^2 - a_p^2)/p^2`, Wiles's level-raising factor; multiplicative `p`: factor `1 - p^{-2}`.

**A4.3 `lem-ddt417`** (lemma; *proved here* (expanded; Chapter 20 also proves it); reference: DDT Lemma
4.17 (inequality half), Chapter 3 card (saturation, Gram determinant, `L[wp]^perp = L[I]`); paper use: Lemma
lem:ddt417, Lemma lem:hecke, Theorem thm:quant Step 2).
Statement. Let `O` be a DVR, `T` a commutative `O`-algebra, finite and free as an `O`-module, acting on an
`O`-module `L` free of finite rank with a perfect `O`-bilinear pairing `< , >` for which every element of `T`
is self-adjoint; `pi : T -> O` a surjective `O`-algebra homomorphism, `wp = ker pi`, `I = Ann_T(wp)`, `eta =
pi(I)`; suppose `L[wp] = {x : wp x = 0}` is free of rank `d` over `O` with Gram determinant `Delta != 0`. Then
`eta^d subset Delta O`, i.e. `d v(eta) >= v(Delta)`, with equality if `L` is free over `T`.
Expanded proof: (1) `wp cap I = 0` (`T` is `O`-torsion-free, `pi` surjective: if `x in wp cap I` then `x^2
in wp I = 0`, and ... the writer gives the standard argument: `T tensor Frac(O) = Frac(O) x T'` with `wp
tensor Frac = 0 x T'` and `I tensor Frac = Frac(O) x 0`), so `L[wp] cap L[I] = 0` as `L` is torsion-free. (2)
Pick `t in I` with `pi(t)` generating `eta`; for `x in L`: `t x in L[wp]` (as `wp I = 0`) and `(pi(t) - t) x
in L[I]` (as `s (pi(t) - t) in wp cap I = 0` for `s in I`, since `pi(s(pi(t) - t)) = pi(s)(pi(t) - pi(t)) = 0`
and `s(pi(t) - t) in I`); so `pi(t) L subset L[wp] + L[I]` and `Q = L/(L[wp] + L[I])` is killed by `eta`.
(3) `L[wp]` is saturated (`L/L[wp]` embeds in `prod_{s in wp} L` via `x -> (s x)`, torsion-free); so `L ->
Hom(L[wp], O)`, `y -> <., y>`, is surjective [Ch. 3: perfect pairing and saturated sublattice] with kernel
`L[wp]^perp`. (4) `L[wp]^perp = L[I]`: for `y in L[I]`, `x in L[wp]`, `pi(t) <x, y> = <t x, y> = <x, t y> = 0`
and `pi(t) != 0`, so `<x, y> = 0`; conversely if `y perp L[wp]` then for all `z in L`, `<t y, z> = <y, t z> =
0` since `t z in L[wp]`, so `t y = 0` by perfectness, and the same for every `t' in I` (replace `t` by `t'`:
`<t' y, z> = <y, t' z> = 0` as `t' z in L[wp]`), so `y in L[I]`. (5) Hence `Q = coker(L[wp] -> Hom(L[wp],
O))`, of order `#O/Delta` [Ch. 3: Gram determinant], generated by `d` elements (`Hom(L[wp], O)` is free of
rank `d`) and killed by `eta`: `#O/Delta <= #(O/eta)^d`, i.e. `v(Delta) <= d v(eta)`. (6) If `L = T^d` then
`L[wp] = (T[wp])^d`, `L[I] = (T[I])^d`, `T[wp] = Ann(wp) = I`, `T[I] = Ann(I) = wp` (double annihilator in a
reduced finite free algebra: the writer should justify or cite DDT), so `Q = (T/(wp + I))^d = (O/eta)^d`.

**A4.4 `lem-hecke`** (lemma; *proved here*; reference: ARS12 Theorem 2.2, paper Lemma lem:crit, Lemma
lem:ddt417, Chapter 3, 14, 20 cards; paper use: Lemma lem:hecke, proof of Theorem thm:main, Theorem thm:quant
Step 4).
Statement. Let `E` be `X_0(N)`-optimal, `l` odd with `l` not dividing `2N` and `rho bar` irreducible, `m`
the maximal ideal of `T_l = T tensor Z_l` containing `l` and `ker phi_f`. Then `v_l(deg varphi_E) = v_l(r_E)
>= v_lambda(eta^empty_{f, lambda})`, with equality if `H^1(X_0(N), Z_l)_m` is free over `T_m`.
Expanded proof: `v_l(deg) = v_l(r_E)` (ARS12 2.2, `l^2` not dividing `N`); `r_E Z_l = phi_f(Ann_T ker
phi_f) Z_l` (Lemma lem:crit over `Z_l`); `T_l = prod T_{m'}` [Ch. 3, 20] and the factors `m' != m` are killed
by `phi_f` and lie in `Ann(ker phi_f)`, so the congruence ideal is computed in `T_m`; apply Lemma lem:ddt417
with `O = Z_l`, `T = T_m`, `pi = phi_f`, `L = H^1(X_0(N), Z_l)_m` (free of finite rank over `Z_l`, with the
perfect alternating pairing `delta hat_!` restricted to the `m`-part: the writer must note that the
decomposition `H^1 tensor Z_l = sum_{m'} H^1_{m'}` is orthogonal for `delta hat_!` because `T` is
self-adjoint, so the restricted pairing is still perfect), `L[wp] = M_{f, lambda}`, `d = 2`, `Delta =
(eta^empty)^2` up to a unit: `2 v_l(r_E) >= 2 v_lambda(eta^empty)`, equality if `L` free.

**A4.5 `rem-free`** (proposition (the paper's Remark rem:free); *proof sketched here*; reference: Tilouine97,
Ribet-Stein Theorem 3.5, Mazur77 (Shimura subgroup), Chapter 14, 20 cards; paper use: Remark rem:free, Theorem
thm:main (equality clause), Theorem thm:quant Step 4 and remark (2)).
Statement. If `J_0(N)[m]` is two-dimensional over `T/m` then `T_m` is Gorenstein and `T_l J_0(N)_m =
H^1(X_0(N), Z_l)_m` (dual) is free of rank `2` over `T_m` (Tilouine); and `J_0(N)[m]` is two-dimensional for
`l` not dividing `2N` and `rho bar` irreducible: Ribet-Stein Theorem 3.5 gives it for `J_1(N)[m']`, the only
exception there having Serre weight `l`, which does not occur in weight `2` with `l` not dividing `N`; and
`J_0(N)[m] -> J_1(N)[m']` (pull-back) is injective because its kernel lies in the Shimura subgroup, which is
Eisenstein (so not supported at the non-Eisenstein `m`). Hence `v_l(deg varphi_E) = v_lambda(eta^empty_{f,
lambda})` under the hypotheses of Lemma lem:hecke; only the inequality is needed for (eq:thm).

**A4.6 `setup-dfg-selmer`** (definition; *stated; reference*; reference: DFG04 2.1, (31); Chapter 17, 18
cards; paper use: Section 4.2, Theorem thm:dfg37, Theorem thm:dfg27, Lemma lem:dfg21, Lemma lem:h0, Remark
rem:ns).
Statement. `f = f_E`, `Sigma = {q : q | N}`, `lambda = l` not dividing `2N`, `A = A_{f, lambda} = ad T` (the
adjoint of `M_{f, lambda}`, which is homothetic to `T_l E` for `rho bar` irreducible, so `ad M_{f,lambda} = ad
T_l E`), `W = A tensor Q_l/Z_l`, `T^D = Hom(A, Z_l(1)) = A(1)` (trace form), `V^D = T^D tensor Q_l`, `W^D =
V^D/T^D`. `H^1_f(Q, W)` is the Bloch-Kato Selmer group; `H^1_Sigma(Q, W)` is the subgroup of `H^1(Q, W)` of
classes with no condition at `p in Sigma`, the Bloch-Kato condition at `l`, and unramified at all other
primes; `H^1_f(Q, W) subset H^1_Sigma(Q, W)`. `S_f = {lambda : lambda | 2N, or rho bar_f restricted to
`Gal(Qbar/Q(sqrt(l*)))` is not absolutely irreducible}` (DFG04 (31)); the hypothesis of Theorem thm:main is `l
not in S_f`.

**A4.7 `thm-dfg37`** (theorem; *stated; reference*; reference: DFG04 Theorem 3.7 (and Theorem 0.2); Chapter
18, 20 cards; paper use: Theorem thm:dfg37, proof of Theorem thm:main, Remark rem:ns, Open question 2).
Statement. If `l` not in `S_f`, then `H^1_Sigma(Q, W)` is finite, of `Z_l`-length `v_lambda(eta^Sigma_{f,
lambda})`. (DFG04 state it for a finite set `Sigma` of primes not containing `l` such that `M_{f, lambda}` is
minimally ramified outside `Sigma`; the set of primes dividing `N`, outside of which `rho` is unramified,
qualifies; this is Theorem 0.2 of DFG04.) Idea: Taylor-Wiles; `H^1_Sigma` is the dual of the cotangent
space of the deformation ring `R_Sigma`, `R_Sigma = T_Sigma` complete intersection, and the numerical criterion
identifies the length with the congruence ideal [Ch. 20].

**A4.8 `thm-dfg27`** (theorem; *stated; reference*; reference: DFG04 Theorem 2.7; paper use: Theorem thm:dfg27,
proof of Theorem thm:main).
Statement. If `l` not in `S_f`, then `H^0(Q, V^D) = 0` and `H^1_f(Q, V^D) = 0` (and the same for `A tensor
Q_l`): the adjoint Bloch-Kato Selmer group with `Q_l`-coefficients vanishes.

**A4.9 `lem-dfg21`** (lemma; *stated; reference* with the proof idea from Chapter 17 (Greenberg-Wiles /
Poitou-Tate comparison of two Selmer structures); reference: DFG04 Lemma 2.1; Chapter 17 card; paper use:
Lemma lem:dfg21, proof of Theorem thm:main, Remark rem:ns, Conjecture conj:euler).
Statement. Suppose `H^0(Q, V^D) = H^1_f(Q, V^D) = 0`, and let `Sigma` be a nonempty finite set of primes
containing every `p != l` at which `W` is ramified. Put `H^1_f(Q_p, T^D) = iota^{-1} H^1_f(Q_p, V^D)`, `iota :
H^1(Q_p, T^D) -> H^1(Q_p, V^D)`. Then there is an exact sequence
`0 -> H^1_f(Q, W) -> H^1_Sigma(Q, W) -> sum_{p in Sigma cup {infty}} H^1_f(Q_p, T^D)^* -> H^0(Q, W^D)^* -> 0`,
`*` the Pontryagin dual.
Attached facts (the paragraph after the lemma, *proved here* from Chapter 17): for `p in Sigma`, `H^1_f(Q_p,
V^D) = H^1_ur(Q_p, V^D) = (V^D)^{I_p}/(Frob_p - 1)` vanishes because `det(1 - Frob_p | (V^D)^{I_p}) =
L_p(A_f(1), 0)^{-1} = L_p(A_f, 1)^{-1} != 0` (C2(b), (d): geometric Frobenius; a nonzero rational number);
hence `H^1_f(Q_p, T^D) = iota^{-1}(0) = H^1(Q_p, T^D)_{tor}`, a finite group. At `infty`: `H^1(R, T^D)` is
killed by `2`, so `H^1_f(R, T^D) = 0` for `l` odd.

**A4.10 `lem-fpr`** (lemma; *stated; reference* (sketch from Chapter 18); reference: FPR94 I.4.2.2, DFG04
proof of Theorem 2.15 and (57); Chapter 18 card; paper use: Lemma lem:fpr, proof of Theorem thm:main, Remark
rem:ns).
Statement. For `p in Sigma`, `Fitt_{Z_l} H^1_f(Q_p, T^D) = L_p(A_f, 1)^{-1} * Tam_p(T^D)` (product of ideals
of `Z_l`), and `Tam_p(T^D) = Tam_p(A)` (DFG04 (57)); here `L_p(A_f, 1)^{-1} = L_p(A_f(1), 0)^{-1}` is a
nonzero rational number which is an `l`-adic integer, of valuation `e_l(E, p)` at an additive prime and
`v_l(1 - p^{-2})` at a multiplicative one. Sketch: `H^1(Q_p, T^D)_{tor}` sits in `0 -> H^1_ur-part -> ... ->
H^0(Q_p, W^D)/div -> 0`, the orders being the Euler factor (from `H^0(Q_p, W^D) = (W^D)^{G}` whose order is
`v_l det(1 - Frob | (V^D)^{I})` when `(V^D)^{I}`-coinvariants are controlled) and the Tamagawa factor [Ch.
18, following FPR94 I.4 and DFG04 2.15].

**A4.11 `lem-h0`** (lemma; *proved here* (Chapter 11 proves it too; the tour follows the paper); reference:
Chapter 4, 5, 9, 11 cards; paper use: Lemma lem:h0, proof of Theorem thm:main, Conjecture conj:euler,
Proposition prop:ns, Section sec:anomaly).
Statement. Let `l` be odd with `rho bar` irreducible. Then `H^0(Q, W^D) = H^0(Q, ad T(1) tensor Q_l/Z_l)` is
finite, and it vanishes iff `rho bar` is not isomorphic to `rho bar tensor chi_l bar`. For `l >= 5` it always
vanishes; for `l = 3` it vanishes iff `rho bar_{E,3}` is absolutely irreducible on `Gal(Qbar/Q(sqrt(-3)))`.
Its length `h_l(E)` is the largest `k` such that `rho mod l^k = (rho tensor chi_l) mod l^k`, and for `E`
without CM it is finite.
Expanded proof: `H^0(Q, W^D)[l] = H^0(Q, ad rho bar tensor chi_l bar) = ` trace-zero `G_Q`-maps `rho bar ->
rho bar tensor chi_l bar` [Ch. 4: `Hom_G(V, W) = (V^* tensor W)^G`]; nonzero map is an isomorphism (`rho bar`
irreducible, Schur); determinants: `det rho bar = chi_l bar = det(rho bar tensor chi_l bar) = chi_l bar^3`,
so `chi_l bar^2 = 1`, which for the mod `l` cyclotomic character (of order `l - 1`) forces `l - 1 | 2`, `l =
3`, `chi_3 bar = chi_{-3}`; conversely an isomorphism `phi : rho bar -> rho bar tensor chi_{-3}` has trace
`0`: `tr phi = tr(rho bar(g)^{-1} phi rho bar(g)) = chi_{-3}(g) tr phi` for all `g`, take `g` with `chi_{-3}(g)
= -1`. For `l = 3`, `rho bar irreducible`: `rho bar = rho bar tensor chi_{-3}` iff `rho bar` is induced from
`Gal(Qbar/Q(sqrt(-3)))` iff its restriction there is not absolutely irreducible [Ch. 4: Clifford theory for
index `2`]. `l^k`-torsion: `H^0(Q, W^D)[l^k] = H^0(Q, ad(T/l^k)(1))`, trace-zero maps `rho mod l^k -> (rho
tensor chi_l) mod l^k`, and the same argument (with care: a trace-zero map that is not an isomorphism mod
`l`...; the writer should argue via the `l`-torsion already being isomorphisms) gives `h_l(E) = max k`.
Finiteness: `rho = rho tensor chi_l` would give `a_p = chi_l(p)... ` precisely `tr rho(Frob_p) = chi_{l*}(p)
tr rho(Frob_p)` for the quadratic character of `Q(sqrt(l*))` (the only quadratic character through which
`chi_l`-twist equality can hold is `chi_{l*}` since `det` forces `chi^2 = 1`; for the `l`-adic statement the
isomorphism `rho = rho tensor chi` with `chi` quadratic ramified only at `l` means `chi = chi_{l*}`), so `a_p =
0` at all primes inert in `Q(sqrt(l*))`, which forces CM by `Q(sqrt(l*))` [Ch. 9, 11]; so for non-CM `E`,
`h_l(E) < infinity`.
