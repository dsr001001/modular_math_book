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
M^{I_p}/(Frob_p - 1)M^{I_p}` is the same group for either Frobenius. (This is important_notes.md point 11; the
book states the convention once, in C2, and repeats it in a one-line Commentary at Lemma lem:euler, Lemma
lem:tamfactor and the paragraph after Lemma lem:dfg21.)

How the commentary is marked. Wherever the paper's text is wrong, imprecise or has a gap, the item carries a
paragraph **Commentary** (to be typeset as a `warning` environment titled "Commentary") with three parts: what the
paper says; the correct statement; how the book presents it. The 14 points of important/important_notes.md are
all placed at their items (the index is Part C below); the points found while preparing this outline are in
Section 9 at the end and are also marked at their items as "Commentary (new)".

Status of this file. Parts A0 to A4.10 were written in a first session and corrected in a second one (the list of
corrections is in Section 7, writer note W1); A4.11 to the end were written in the second session.


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
`v_2(j) >= 0` (potentially good) and then `t_l = 0`. Twist behaviour (corrected, see the Commentary): `t_l(E, q)`
is invariant under every quadratic twist (`j` is unchanged); `e_l(E, q)` is invariant under a quadratic twist
that is unramified at `q`, and under a twist ramified at `q` that keeps the reduction at `q` additive and
potentially good of type `II, III, IV` or a dual (`a_q = 0` on both sides, `ad V` unchanged); it is NOT
invariant when the twist moves `q` between multiplicative and `I_n^*`, or between good and `I_0^*`.
**Commentary (new, Section 9 point N1).** The paper says (end of Definition def:terms) "Both terms are invariant
under quadratic twist". This is false for `e_l` at the twisting prime: 11a1 has type `I_5` at `11` and
`e_3(11a1, 11) = 0`, while its twist by `-11` (class 121d, type `I_1^*` at `11` for 121d1) has `e_3 = v_3(11^2 - 1)
= v_3(120) = 1`; and 11a1 twisted by `-7` is 539d1 (type `I_0^*` at `7`) with `e_3(539d1, 7) = v_3(6) + v_3(64 -
4) = 2`, where 11a1 has no term at `7`. The change of `e_l` under such twists is exactly what Theorem thm:quant
exploits. The true local factor `L_q(A_f, s)` is twist invariant (`ad` is); the naive factor is not, and `e_l`
is their ratio. The book states the corrected invariance in the definition and refers to this example.

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
thm:main (Lemma lem:h0); `h_l(E) > 0` iff `rho bar = rho bar tensor chi bar_l` (residual cyclotomic
character), which forces `l = 3` (where `chi bar_3 = chi_{-3}`), and for `l = 3` means image `N_s(F_3)` (label
3Ns); then `h_3(E) = 1` exactly (Lemma lem:h0 as corrected in A4.11: `h_l(E) = 0` for `l >= 5` and `h_3(E) <= 1`
always), not only "for every such curve of the tables".
**Commentary (important_notes.md point 6).** The paper (paragraph after Conjecture conj:euler, and the first
sentence of Section 1.3) says `h_l(E)` "is positive exactly when `rho bar = rho bar tensor chi_{l*}`" and speaks
of "a correction term when the representation is induced from `Q(sqrt(l*))`". For `l >= 5` this is wrong: `rho
bar = rho bar tensor chi_{l*}` can happen (dihedral case, excluded by `S_f`), but `h_l(E) = 0` always for `l >=
5`. The criterion is `rho bar = rho bar tensor chi bar_l`, and `chi bar_l = chi_{l*}` only for `l = 3`. The book
states: "`h_l(E)` is positive exactly when `l = 3` and `rho bar_{E,3}` is induced from `Q(sqrt(-3))`", and notes
that for `l >= 5` the dihedral curves carry no correction in (eq:rule) (the paper reports no violation among
them, Section sec:forms).

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

**A1.10 `thm-qual`** (theorem; *proved here* in Section 21.9; reference: paper Theorem thm:qual; paper use:
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
Reading: the outer inequality `v_l(deg varphi_E) >= sum_{q in S} e_l(E, q)` needs no multiplicity one at all
(A4.15, Step 4); the middle term `v_l(r_{E_S})` needs multiplicity one at level `N_S` (Remark rem:free).
**Commentary (new, Section 9 point N10).** The abstract calls this "an elementary twisting argument". Only Step 1
(transport of congruences along the twist) is elementary; Steps 2 to 4 use DFG04 Proposition 1.4(c) (Ihara's
lemma), Lemma lem:ddt417 and, for the middle term, multiplicity one. The book says so.

**A1.12 `prop-ns`** (proposition; *proved here* in Section 21.14; reference: paper Proposition prop:ns;
Zywina15; Chapter 1, 4, 11 cards; paper use: Proposition prop:ns, Section sec:anomaly, Conjecture conj:euler).
Statement. Let `E/Q` be without CM with `E[3]` irreducible. Then `rho bar_{E,3}` is absolutely irreducible on
`Gal(Qbar/Q(sqrt(-3)))` unless its image is conjugate to the normaliser `N_s(F_3)` (order `8`) of a split
Cartan subgroup of `GL_2(F_3)`; in that case `rho bar_{E,3} = rho bar_{E,3} tensor chi_{-3}`, `H^0(Q, ad rho
bar_{E,3}(1)) != 0` and `h_3(E) >= 1`. The `3`-division polynomial (degree `4`) then factors over `Q` as a
product of two irreducible quadratics, and otherwise (image `GL_2(F_3)` or `N_ns(F_3)`) it is irreducible.
Commentary (important_notes.md points 1, 2, 4, 9): see A5.1, where the proof is walked through; in short, the
"non-abelian and faithful" step needs the commutator argument (point 1), `N_s(F_3)` is not maximal (it lies in
`N_ns(F_3)` with index 2, point 2), Zywina15 is cited by section only (point 4), and "without complex
multiplication" is not used (point 9). Data check made for this outline: among the 38,042 optimal curves of
conductor below 10,000, every non-CM curve whose 3-division polynomial factors as `2 + 2` carries Sutherland's
label 3Ns in ecdata (90 curves), every 3Nn and every surjective curve has it irreducible, and the only other `2 + 2`
cases are CM curves (for instance 121b1, CM by `Q(sqrt(-11))`, in which `3` splits).

**A1.13 `conj-eis`** (conjecture; *stated*; reference: paper Conjecture conj:eis; Section sec:eis; Chapter 9,
11, 14 cards; paper use: Conjecture conj:eis, Section sec:eis, Open question 4).
Statement. Let `E` be optimal, not CM, with a rational `l`-isogeny, `l` odd, and `D = sum_{q | N} v_l(#Phig_q)
- v_l(deg varphi_E)` the deficit of (eq:main). Then `D <= v_l(#E(Q)_tors) + [E[3] = Z/3 + mu_3]`, and `D <=`
the number of curves in the isogeny class of `E` with a rational point of order `l`. In particular `D <= 0`
when `E` has no rational `l`-torsion point, `D <= 1` for `l >= 5`, `D <= 2` for `l = 3`.
**Commentary (new, Section 9 point N3).** The paper says that a point of order `9` and the image `Z/3 + mu_3`
(label 3Cs.1.1) "do not occur together in the tables" and that, not having proved it, `D <= 2` is "part of the
conjecture" (Section sec:eis). They cannot occur together for a non-CM curve: if `E[3] = Z/3 + mu_3` and `P in
E(Q)` has order `9`, then `3P` spans the `Z/3` (the only rational points of `E[3]`), `phi: E -> E' = E/mu_3` and its
dual `phi^` (kernel `phi(E[3])`, with `phi^(E'[3]) = mu_3`), and `K = (phi^)^{-1}(<P>)` is a rational subgroup of
`E'` of order `27` not containing `E'[3]` (because `mu_3` is not in `<P>`), hence cyclic. So `E'` has a rational
cyclic `27`-isogeny; the only non-cuspidal rational point of `X_0(27)` has `j = -2^15 3 5^3` (CM by the order of
discriminant `-27`), so `E'` and `E` would have CM. Hence, given the first bound, `D <= 2` for `l = 3` follows
from Mazur's torsion theorem (`v_3(#E(Q)_tors) <= 2`, and `= 1` when `E[3] = Z/3 + mu_3` since `mu_3` has no
rational points); likewise `D <= 1` for `l = 5, 7` (no rational point of order `25` or `49`) and `D <= 0` for `l
>= 11`. The book proves this as a proposition in Section 21.17 and states only the first bound as conjectural.
Label check (important_notes.md point 3): in the ecdata `galrep` files (Sutherland's labels) for `N < 10,000`
every curve labelled 3B.1.1 or 3Cs.1.1 has a rational point of order `3`, every 3B.1.2, 3B, 3Cs, 3Nn, 3Ns curve
has none, and no 3Cs.1.1 curve has a point of order `9`; this is consistent with the paper's use of 3B.1.1
(rational `3`-torsion, Borel image), 3Cs.1.1 (`E[3] = Z/3 + mu_3`) and 3Ns, but the definitions must still be
checked against Sutherland16 itself.

### A2. The paper's Section 2: local invariants (Sections 21.5 to 21.7)

**A2.1 `lem-tamagawa-exp`** (lemma; *proved here*; reference: Silverman ATAEC V.3 and V.5 (Tate curve),
DDT Theorem 3.1(e), Chapter 10 and 11 cards; paper use: Lemma lem:tamagawa-exp, Theorem thm:qual case (c),
Section 1.5, Remark rem:ko).
Statement. Let `q` be a prime of multiplicative reduction, `n_q = v_q(Delta_E)` (`= -v_q(j_E)`), and `l != q`
a prime. Then `rho_{E,l} mod l^t` is unramified at `q` iff `l^t | n_q`; this holds for split and for nonsplit
reduction.
Expanded proof: over `K = ` the unramified quadratic extension of `Q_q` (nonsplit case; `K = Q_q` in the split
case) `E` is isomorphic to the Tate curve `E_{q_E}` with Tate parameter `q_E in Q_q^x`, `v_q(q_E) = n_q`;
`I_q = I_K` is unchanged. `E_{q_E}[l^t]` (inside `Kbar^x/q_E^Z`) is generated by `mu_{l^t}` and a chosen
`l^t`-th root `q_E^{1/l^t}`; `I_q` acts trivially on `mu_{l^t}` (`l != q`) and sends `q_E^{1/l^t}` to
`zeta^{c(sigma)} q_E^{1/l^t}` with `c` the Kummer cocycle. By Kummer theory over `Q_q^ur` (which contains
`mu_{l^t}`), `c|_{I_q} = 0` iff `q_E` is an `l^t`-th power in `Q_q^ur`; the units of its valuation ring are
`l^t`-th powers (Hensel, `l != q`, residue field `Fbar_q` with `Fbar_q^x` `l`-divisible), so this holds iff
`l^t | v_q(q_E) = n_q`.
**Commentary (important_notes.md point 8).** The paper's proof calls the Tate parameter `u`, while Lemma
lem:tamfactor uses `u` for its unit part `q_E q^{-n}`, and it says "an `l^t`-th power in `Q_q^ur` up to units",
which mixes two statements. No mathematical error. The book names the Tate parameter `q_E` throughout and
writes the two steps separately as above.

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
of unity; `sigma^2 + sigma + 1 = 0` on `T` (Cayley-Hamilton: char poly `X^2 - tr X + det = X^2 + X + 1`); `T` is
a torsion-free module over the subring `Z_3[sigma]` of `End(T)`, and `Z_3[sigma] = Z_3[X]/(X^2 + X + 1) =
Z_3[zeta_3]` (`X^2 + X + 1` is the minimal polynomial of `sigma`, which is not a scalar), a DVR with uniformiser
`pi = 1 - zeta_3`, `pi^2 = -3 zeta_3`, residue field `F_3` (Chapter `ch:ant`); rank `2` over `Z_3` forces `T`
free of rank one over `Z_3[zeta_3]`; `E[3] = T/3T = Z_3[zeta_3]/(pi^2)` with `sigma` acting as `zeta_3 = 1 - pi`;
so `sigma - 1` acts as `-pi`, which is nonzero on `Z_3[zeta_3]/(pi^2)` and has square `pi^2 = 0` there: a
nontrivial unipotent; fixed line `ker(pi) = pi Z_3[zeta_3]/(pi^2)`; conductor exponent `dim E[3] - dim
E[3]^{I_q} + Swan = 2 - 1 + 0 = 1`.
**Commentary (important_notes.md point 13).** The paper writes "`Z_3[sigma]/(sigma^2 + sigma + 1) = Z_3[zeta_3]`";
`Z_3[sigma]` already satisfies the relation. The intended statement is `Z_3[sigma] = Z_3[X]/(X^2 + X + 1)`. The
book writes it this way; notation only.

**A2.3 `rem-types`** (proposition (the paper's Remark rem:types); *proof sketched here*; reference: Kraus90,
Chapter 10, 11 cards; paper use: Remark rem:types, Theorem thm:qual (why only (a), (b), (c))).
Statement. For `q >= 5` and the other additive types the image of `I_q` mod `3` is not unipotent: it has order
`2` (`I_0^*`, defect `2`) or `4` (`III, III^*`, defect `4`), or it is `-1` times a nontrivial unipotent (`II,
II^*`, defect `6`), or it is a ramified quadratic character times a unipotent (`I_n^*`: `rho = rho' tensor
chi_q` with `rho'` of type `I_n`). In the last two cases `E[3]^{I_q} = 0` and the Serre conductor exponent of
`rho bar_{E,3}` at `q` is `2`, equal to the conductor exponent of `E`; these are the types whose twist by
`chi_q` lowers the conductor exponent (to `1` for `I_n^*` with `n >= 1`, and `II <-> IV^*` keeps `2` but makes
Lemma lem:IV applicable).
Correct complete statement (proved here, it is three lines of linear algebra mod `3`): for every additive type
at `q >= 5` other than `IV, IV^*`, `E[3]^{I_q} = 0` and the Serre conductor exponent of `rho bar_{E,3}` at `q` is
`2`: the generator of inertia acts mod `3` as `-1` (`I_0^*`), as an element `tau` with `tau^2 = -1` (`III,
III^*`), as `-u` with `u` unipotent (`II, II^*`, and `I_n^*` up to the quadratic character), and none of these
has a fixed vector. The twist by `chi_q` lowers the Serre conductor exponent of `rho bar_{E,3}` for `II, II^*`
(to `1`), for `I_n^*` (to `1`, or `0` if `3 | n`) and for `I_0^*` (to `0`); not for `III, III^*`.
**Commentary (new, Section 9 point N8).** The paper's grouping suggests that `E[3]^{I_q} = 0` and exponent `2`
hold only "in the last two cases" and that only those types have a conductor-lowering twist; both statements are
also true for `I_0^*` (and the first for `III, III^*`). Nothing downstream depends on this: Theorem thm:qual does
not treat `I_0^*` because the lowered form may be `f tensor chi_q` itself (A3.5). The book states the complete
version above.

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
**Commentary (new, Section 9 point N14, minor).** The paper's proof of (ii) ends "The conductor exponents are the
standard ones for `q` odd (tame)". At `q = 3` additive reduction can be wild (exponent up to `5`); for the exchanges
listed at `q = 3` (`I_n <-> I_n^*`, `I_0 <-> I_0^*`) the exponent is `2` because quadratic characters of `Q_3` are
tamely ramified. The book says this.

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
0`. (Optional remark: the same line is `ker N` on `ad` of the Weil-Deligne representation `sp(2)` twisted by
an unramified character, Chapter `ch:local`; the writer may add this in one sentence, without proof.)
**Commentary (important_notes.md point 11).** The paper says "a line with eigenvalue `q^{-1}`" without naming
the Frobenius, and computes with the arithmetic one in Lemma lem:tamfactor. The eigenvalue is `q` for the
arithmetic and `q^{-1}` for the geometric Frobenius; the table is right with the geometric one (C2). The book
says "geometric" here and "arithmetic" in A2.7.
`I_n^*`: `V = V' tensor chi_q`, `V'` Steinberg, `ad V
= ad V'`, same factor, but `a_q = 0` so naive factor `1`, `e_l = v_l(1 - q^{-2}) = v_l(q^2 - 1)`. `II, II^*,
IV, IV^*`: image of `I_q` cyclic of order `3` or `6` generated by `sigma` or `-sigma`, eigenvalues
`zeta_3^{+-1}`; on `ad V` the sign disappears; `End_{I_q}(T) = Z_l[sigma] = Z_l tensor_Z Z[zeta_3]` and
`End_{I_q}(V) = Q_l[sigma] = Q_l tensor_Q Q(zeta_3)` (a field if `l = 2 mod 3`, the product `Q_l x Q_l` if `l = 1
mod 3`; `T` is free of rank one over `Z_l[sigma]`, Chapter `ch:ant`); `(ad V)^{I_q} = ` trace-zero part of
`End_{I_q}(V)`, the line spanned by `2 sigma + 1` (whose square is `-3`; it plays the role of `sqrt(-3) = zeta_3 -
zeta_3^{-1} = 2 zeta_3 + 1`); `Frob_q` normalises the image of inertia and acts on
`<sigma>` by `sigma -> sigma^q` (the relation `Frob t Frob^{-1} = t^q`), so it centralises `sigma` if `q = 1 mod
3` and inverts it if `q = 2 mod 3`; conjugation by `Frob` on `End_{I_q}(V)` is the ring automorphism of
`Q_l[sigma]` fixing `sigma` or sending `sigma -> sigma^{-1} = sigma^2`, so it acts on `2 sigma + 1` by
`+1` resp. `-1` (as `2 sigma^2 + 1 = -(2 sigma + 1)`), that is by `chi_{-3}(q)`; `L_q(A_f, s)^{-1} = 1 - chi_{-3}(q)
q^{-s}`; `a_q = 0` so `e_l = v_l(1 - chi_{-3}(q) q^{-1}) = v_l(q - chi_{-3}(q))`. `III, III^*`: order `4`, generator
`tau` with `tau^2 = -1`, eigenvalues `+-i`, `End_{I_q}(V) = Q_l[tau] = Q_l tensor Q(i)`, invariant line spanned by
`tau` (the "diagonal element" `diag(i, -i)` of the paper, in an eigenbasis over `Q_l(i)`), `Frob` acts by `tau ->
tau^q`, i.e. by `chi_{-4}(q)`; `e_l = v_l(q - chi_{-4}(q))`.
**Commentary (important_notes.md point 12).** The paper writes "`sqrt(-3) in Z_l[zeta_3] = End_{I_q}(V)`". The
correct statements are `End_{I_q}(T) = Z_l[sigma] = Z_l tensor Z[zeta_3]` and `End_{I_q}(V) = Q_l tensor Q(zeta_3)`,
which is not a field (nor `Z_l[zeta_3]`) when `l = 1 mod 3`. The argument only needs the element `2 sigma + 1`
and the action of Frobenius through `Gal(Q(zeta_3)/Q)`, so it is unaffected; the book writes the correct ring and
works with `2 sigma + 1` and `tau`.
`I_0^*`: `V = V' tensor chi_q`, `V'`
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
(7) [Ch. 5, 7, 17] Identify `c'`. Write `q_E = q^n u` with `u` a unit, so `kappa = n kappa_q + kappa_u` in
`H^1(G, Z_l(1))`. The class `kappa_u` is unramified: it is inflated from the class of `u` in `H^1(G/I, Z_l(1)) =
Z_l(1)/(q - 1) = F_q^x tensor Z_l` (Kummer theory over `F_q` plus Hensel), and `kappa_u(Frob)` is that class. Choose
the lift `Frob` that fixes a compatible system of `l`-power roots of `q` (possible since `Q_q(q^{1/l^infty})` is
totally ramified); then `kappa_q(Frob) = 0` and `c' = kappa_u(Frob)` is the class `c` of `u` up to a unit. For
another lift or another cocycle, `c'` changes by an element of `(n', q - 1) Z_l` (computation: `rho(Frob t^k)` has
upper-right entry `c' + eps q k n'`), which does not change `min(v_l(n), v_l(q - 1), v_l(c'))`. Hence the
minimum equals `min(v_l(n), v_l(q - 1), v_l(c))`.
**Commentary (important_notes.md point 7).** The paper says "`c'` is the image of `kappa` in `H^1(G/I,
Z_l(1)^I)`". There is no such map (inflation goes the other way, and `kappa` is not inflated: its restriction to
`I` is `n` times the tame character), and `c' = kappa(Frob)` depends on the lift of `Frob` and on the cocycle.
The conclusion of the lemma is unaffected. The book gives the decomposition `kappa = n kappa_q + kappa_u` and the
indeterminacy argument above.
**Commentary (important_notes.md point 11).** The matrix `rho(Frob) = (eps q, c'; 0, eps)` and the relation
`Frob^{-1} t Frob = t^{q^{-1}}` are for the ARITHMETIC Frobenius; the book says so in this proof.
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
hypothesis; hence `rho bar_h = rho bar` over a common finite extension of `F_l` (Chebotarev + Brauer-Nesbitt give
equal semisimplifications; `rho bar` is absolutely irreducible because it is irreducible and complex
conjugation has the distinct eigenvalues `+1, -1`, `l` odd; so both are semisimple and isomorphic).
**Commentary (important_notes.md point 10).** The paper writes "`rho bar_h = rho bar` by Chebotarev and
Brauer-Nesbitt, `rho bar` being irreducible"; irreducibility alone gives only equal semisimplifications. The
book inserts "hence absolutely irreducible (complex conjugation)" and "over a common finite extension of `F_l`".
`p = l`:
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
tensor chi` on `Gamma_0(N)` (by modularity of `E'`, which has conductor `N`; Atkin-Li in the form of Lemma
lem:twist(iii) does not apply since `q^2 | N`; the equality `f_{E'} = f tensor chi` holds coefficientwise because
both have `a_n = 0` for `q | n`); `rho bar
tensor chi` satisfies the hypotheses (irreducibility and absolute irreducibility over `Q(sqrt(-3))` are
invariant under twisting by a character); Lemma lem:IV for `E'`: `v_q(N(rho bar tensor chi)) = 1`, `M |
N/q`; optimal-level theorem gives `g` on `Gamma_0(M)` with `a_p(g) = chi(p) a_p(f) mod lambda`, `p` not
dividing `3N`; `q || M` (exponent exactly `1`), so `h = g tensor chi` is a newform on `Gamma_0(Mq)`, `Mq | N`
(Lemma lem:twist (iii)); `a_p(h) = chi(p)^2 a_p(f) = a_p(f) mod lambda` for `p` not dividing `3N`; `h != f`
(if `h = f` then `f' = f tensor chi = h tensor chi = g tensor chi tensor chi`, which is the `q`-depleted form of
`g`, so the newforms `f'` and `g` have the same `a_p` for all `p` not dividing `qN`, hence `f' = g` by strong
multiplicity one, contradicting levels `N != M`); hypothesis of Lemma lem:old: `p || N`
unramified for `rho bar` implies `p != q`, `rho bar tensor chi` unramified at `p`, `p` not dividing `M`, so `p`
not dividing `Mq`; Lemma lem:old gives `3 | r`. Case (c): type `I_n^*` at odd `q != l`, `l | n`, `q^2 || N`;
`E' = E^{(q)}` has type `I_n` at `q`, conductor `N/q`; `f' = f tensor chi` on `Gamma_0(N/q)` with `q || N/q`;
Lemma lem:tamagawa-exp for `E'`: `rho bar tensor chi` unramified at `q` (as `l | n`); `M = N(rho bar tensor
chi)` prime to `q`, `M | N/q^2`; optimal-level theorem (Ribet's case) gives `g` on `Gamma_0(M)` with `a_p(g) =
chi(p) a_p(f) mod lambda`, `p` not dividing `l N`; `q` not dividing `M` so `h = g tensor chi` is a newform on
`Gamma_0(M q^2)`, `M q^2 | N`; congruent to `f` at `p` not dividing `l N`; `h != f` (if `h = f` then `f' = f
tensor chi` is the `q`-depleted form of `g`; but `a_q(f') = +-1` (multiplicative) while the depleted form has
`a_q = 0`; or: strong multiplicity one gives `f' = g`, of levels `N/q != M`); hypothesis of Lemma lem:old as in
(b); `l | r`. Finally `v_l(deg varphi_{E_0}) = v_l(r)` because `l` does not divide `N` (ARS12 Theorem 2.2).
**Commentary (new, Section 9 point N6).** In cases (b) and (c) the paper argues "`h != f`: otherwise `g = h
tensor chi = f tensor chi = f'`". But `h tensor chi = (g tensor chi) tensor chi` is the `q`-depletion of `g`, not
`g` (here `a_q(g) != 0` in general: `g` is multiplicative at `q` in case (b), and `q` does not divide its level
in case (c)). The conclusion is right, by strong multiplicity one as above; the book writes the one-line fix.
Why `I_0^*` is not in Theorem thm:qual (worth one sentence in the book): for type `I_0^*` the same construction
gives `M | N/q^2`, but then `g` may be `f' = f tensor chi = f_{E'}` itself (level `N/q^2` can equal `M`), and
then `h = g tensor chi = f' tensor chi = f` (both have `a_n = 0` for `q | n`), so Lemma lem:old does not apply;
the argument gives nothing. Theorem thm:quant handles `I_0^*` through the level-raising factor instead.

**A3.6 `example-abc`** (example; worked verification; reference: paper Example after case (c); Cremona
tables, LMFDB; paper use: the example of Section 3, Section 7.3 of PLAN (worked verifications)).
Verified for this outline (Python point counts and the ecdata files; Part B4 has the full list): 121a1 `=
[1,1,1,-30,-76]` has `Delta = -11^2`, `v_11(c_4) = 1`, `j = -24729001` (`v_11(j) = 1`), so type `II` at
`11`. Its twist by `-11` is 121c2 `= [1,1,0,-3632,82757]` (same `j`,
`Delta = -11^8`, type `IV^*`); note that 121c1 (the optimal curve of the class, `Delta = -11^4`) has type `IV`, so
the paper's "lies in the class 121c and has type `IV^*`" refers to 121c2. 
Statement. (b) 121a1 (type `II` at `11`):
twist by `-11` is in class 121c, type `IV^*` at `11`; its mod `3` representation has Serre conductor `11` and is
congruent to the form of 11a1; `f_{11a} tensor chi_{-11}` is the form of 121d; `a_p(121a1) = chi_{-11}(p)
a_p(11a1) mod 3` for all `p != 3, 11` (checked `p < 500`); `deg varphi_{121a1} = 6`, `e_3(E, 11) = v_3(11 -
chi_{-3}(11)) = v_3(11 + 1) = 1` (`11 = 2 mod 3`), bound `1`, attained (`v_3(6) = 1`). (c), `l = 3`: 539c1
(`539 = 7^2 * 11`), type `I_3^*` at `7`; twist by `-7` has conductor `77`, type `I_3` at `7`; `a_p(539c1) =
chi_{-7}(p) a_p(11a1) mod 3`, `p != 3, 7, 11` (checked `p < 1000`); `deg = 2^5 * 3^2`; `e_3(E, 7) = v_3(7^2
- 1) = v_3(48) = 1`, `t_3(E, 7) = v_3(3) = 1`, bound `2 = v_3(deg)`, attained. (c), `l = 5`: 980i1 (`980 = 2^2
* 5 * 7^2`), type `I_5^*` at `7`; twist by `-7` has conductor `140`, type `I_5` at `7`; `a_p(980i1) =
chi_{-7}(p) a_p(20a1) mod 5`, `p != 2, 5, 7` (checked `p < 1000`); `deg = 2^6 * 3^2 * 5`; `e_5(E, 7) = v_5(48)
= 0`, `t_5(E, 7) = v_5(5) = 1`, bound `1 = v_5(deg)`.
**Commentary (new, Section 9 point N7).** `5 | 980` (and `5 | 20`, `5 | 140`), so the 980i1 example is outside
the hypothesis `l` not dividing `N` of Theorem thm:qual, and of Theorem thm:main; it illustrates the congruence
mechanism of case (c), not the theorem. The paper presents it under "(c) at `l = 5`" without saying so. The book
says it explicitly and points to the remark after the example (the data show the conclusion also when `l || N`).
Also verified here: the twist of 539c1 by `-7` is the class 77c (`a_p(539c1) = chi_{-7}(p) a_p(77c1)` for all `p <
1000`, `p != 2, 7, 11`; 77c1 `= [1,1,0,4,11]`, `Delta = -7^3 11^2`, `deg = 6`); the twist of 980i1 by `-7` is the
class 140b (140b1 `= [0,0,0,32,212]`, `deg = 60`); `f_{11a} tensor chi_{-11}` is the form of 121d; the three
congruences of the example hold for all `p < 1000` outside the stated primes (and also at `p = 2` for 121a1 and
539c1); the level-raising conditions are visible: `a_7(11a1) = -2` and `(7 + 1)^2 - 4 = 60`, divisible by `3`;
`a_7(20a1) = 2`, and `60` is divisible by `5`.

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
it is, as a `G_Q`-lattice, isomorphic to `Hom(T_l E, Z_l) = T_l E(-1)` up to homothety when `rho bar` is
irreducible (all `G_Q`-stable lattices in an irreducible residual situation are homothetic [Ch. 4, 15: Ribet's
lemma on lattices]; `H^1` is dual to the Tate module of `J_0(N)`), and `ad` of either is `ad T_l E`.
**Commentary (new, Section 9 point N12, minor).** Section 4.2 of the paper says "`M_{f,lambda}` and `T_l E` are
homothetic". They live in dual representations (`V_l E^*` versus `V_l E`, determinants `chi_l^{-1}` and `chi_l`);
the correct statement is "homothetic to the dual of `T_l E`", and the conclusion "their adjoints coincide" holds
because `ad(T^*) = ad(T)` (via `x -> -x^t`) and `ad(T(-1)) = ad(T)`. The book states it this way.
Why `delta hat_!` is alternating (the paper only asserts it): `w = w_{M^Sigma}` is an automorphism of the curve,
so it preserves the cup product, `<w x, w y> = <x, y>`; hence `<y, w x> = <w y, w w x> = <w y, x> = -<x, w y>`,
the pairing is antisymmetric, and on a torsion-free module this gives `<x, w x> = 0`.
The pairing `delta hat_!` is the cup product composed with the Atkin-Lehner involution
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
Expanded proof: (0) If `eta = 0` there is nothing to prove; assume `eta != 0`. (1) `wp cap I = 0`. Write
`K = Frac(O)`; `T tensor K` is a finite product of local Artinian `K`-algebras and `pi_K` factors through one of
them, `A`. If `A != K`, then `I tensor K = Ann(wp tensor K)` is contained in (socle of `A`) `x 0`, which lies in the
maximal ideal of `A`, so `pi(I) = 0`, contrary to (0). So `A = K`, `T tensor K = K x T'`, `wp tensor K = 0 x T'`,
`I tensor K = K x 0`, and `wp cap I = 0` (`T` is torsion-free). Hence `L[wp] cap L[I] = 0`: an element killed by
`wp + I` is killed by `pi(t) in wp + I` (with `t` as in (2): `pi(t) = t - (t - pi(t))`, `t - pi(t) in wp`), and
`L` is torsion-free. (2)
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
`L[wp] = (T[wp])^d`, `L[I] = (T[I])^d`, `T[wp] = Ann(wp) = I`, `T[I] = Ann(I) = wp`, so `Q = (T/(wp + I))^d =
(O/eta)^d`. Proof of `Ann(I) = wp` in the situation of (1): inside `T tensor K = K x T'`, `Ann(I) = T cap (0 x T')`,
and `T cap (0 x T') = ker(pi) = wp` since `pi` is the first projection restricted to `T`.
**Commentary (new, Section 9 point N5, minor).** The paper's proof begins "Since `L` is torsion-free and `wp cap
I = 0`". The equality `wp cap I = 0` is not proved and is false in the lemma's stated generality: for `T =
O[epsilon]/(epsilon^2)` acting on `L = O` through `epsilon -> 0`, with `<x, y> = xy` and `pi(epsilon) = 0`, one has `wp
= I = O epsilon`. The statement survives because in every such case `eta = 0` (argument (1)), and in the paper's
applications `T` acts faithfully on `L`, where `wp cap I = 0` also follows from `Delta != 0` (for `x in wp cap
I`, `x L` lies in `L[wp] cap L[wp]^perp = 0`). The book adds step (0) and the argument (1).

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
killed by `2`, so `H^1_f(R, T^D) = 0` for `l` odd. Why `H^1(Q_p, T^D)_tor = iota^{-1}(0)`: the kernel of
`H^1(Q_p, T^D) -> H^1(Q_p, V^D) = H^1(Q_p, T^D) tensor Q_l` is the torsion (`H^1(Q_p, T^D)` is finitely
generated over `Z_l`, Chapter `ch:galcoh`).
Where the hypotheses enter: `H^0(Q, V^D) = 0` and `H^1_f(Q, V^D) = 0` (Theorem thm:dfg27, i.e. `l` not in `S_f`)
make the dual Selmer group with `Q_l` coefficients vanish, so the only global correction term is `H^0(Q,
W^D)^*`; `l` odd kills the archimedean term; `Sigma` must contain the primes where `W` ramifies (all primes of bad
reduction except possibly the `I_0^*` primes, where `ad V` is unramified; they are in `Sigma` anyway).
Proof idea for the book (Chapter `ch:galcoh` card, Greenberg-Wiles / Poitou-Tate): compare the Selmer structures
"Bloch-Kato everywhere" and "no condition on `Sigma`"; the cokernel of `H^1_f(Q, W) -> H^1_Sigma(Q, W)` maps into
`sum_{p in Sigma} H^1(Q_p, W)/H^1_f(Q_p, W)`, which is dual to `sum H^1_f(Q_p, T^D)` by Tate local duality, and the
defect of surjectivity is measured by the dual Selmer group of `T^D` with the strict conditions at `Sigma`, whose
divisible part vanishes by `H^1_f(Q, V^D) = 0` and whose finite part is `H^0(Q, W^D)`; this is the four-term
sequence. *Stated; reference* (DFG04 Lemma 2.1); the book gives this paragraph as a sketch.
**Commentary (important_notes.md point 11).** "`det(1 - Frob_p | (V^D)^{I_p}) = L_p(A_f, 1)^{-1}`" holds with the
geometric Frobenius (with the arithmetic one the determinant at a multiplicative prime is `1 - q^2`, a different
number with the same `l`-adic valuation). The book says "geometric" here.

**A4.10 `lem-fpr`** (lemma; first identity *proved here* (it is elementary for `p != l`, given Chapters `ch:cohomology`
and `ch:galcoh`); second identity `Tam_p(T^D) = Tam_p(A)` *stated; reference* DFG04 (57), with the multiplicative
case checked by hand (Exercise 8); reference: FPR94 I.4.2.2, DFG04 proof of Theorem 2.15 and (57); Chapters 16,
17, 18 cards; paper use: Lemma lem:fpr, proof of Theorem thm:main, Remark rem:ns).
Statement. For `p in Sigma`, `Fitt_{Z_l} H^1_f(Q_p, T^D) = L_p(A_f, 1)^{-1} * Tam_p(T^D)` (product of ideals of
`Z_l`), and `Tam_p(T^D) = Tam_p(A)`; here `L_p(A_f, 1)^{-1} = L_p(A_f(1), 0)^{-1}` is a nonzero rational number
which is an `l`-adic integer, of valuation `e_l(E, p)` at an additive prime and `v_l(1 - p^{-2})` at a
multiplicative one.
Expanded proof of the first identity (the book's own, replacing the first session's sketch). Put `G = G_{Q_p}`,
`I = I_p`, `X = T^D`. (1) Inflation-restriction with `G/I = Zhat` (cohomological dimension one, so `H^2(G/I, -) = 0`
on these modules) gives `0 -> H^1(G/I, X^I) -> H^1(G, X) -> H^1(I, X)^{G/I} -> 0`. (2) `H^1(G/I, X^I) = X^I/(Frob
- 1)X^I` (procyclic group, Chapter `ch:cohomology`); since `det(1 - Frob | X^I tensor Q_l) = L_p(A_f(1), 0)^{-1} !=
0` (geometric Frobenius; the arithmetic one gives the same valuation), `Frob - 1` is injective on `X^I` and the
quotient is finite of order `l^{v_l(L_p(A_f, 1)^{-1})}`. (3) Take torsion in (1): the left term is finite, so a
torsion class of `H^1(I, X)^{G/I}` lifts to a class some multiple of which lies in a finite group, hence to a
torsion class: `0 -> X^I/(Frob - 1) -> H^1(G, X)_tor -> (H^1(I, X)_tor)^{G/I} -> 0`. (4) Lengths add, and for a
finite `Z_l`-module `Fitt = l^{length}` (Chapter `ch:modules`); the right term has Fitting ideal `Tam_p(X)` by
definition (A1.3). (5) `H^1_f(Q_p, T^D) = H^1(Q_p, T^D)_tor` (A4.9). The valuation statements: at an additive
prime `L_p^{nv} = 1`, so `v_l(L_p(A_f, 1)^{-1}) = e_l(E, p)` by Definition def:terms; at a multiplicative one
`L_p(A_f, 1)^{-1} = 1 - p^{-2}` (A2.5); integrality: `P_p(X)` has `l`-integral coefficients and `p^{-2}` is an
`l`-adic unit.
The second identity: `Tam_p(A(1))` and `Tam_p(A)` are Fitting ideals of the Frobenius invariants of the same
finite module `H^1(I, A)_tor` with the Frobenius action twisted by `chi_l(Frob)` (inertia acts trivially on
`Z_l(1)` as `p != l`). They have the same order in general (DFG04 (57), via local duality); in the multiplicative
case a direct count (Exercise 8) gives `l^{v_l(n) + min(v_l(n), v_l(q - 1), v_l(c))}` for both (checked by computer
for `l = 3, 5`, `v_l(n) <= 2`, all primes `q < 200`, all classes `c`, both signs `eps`).
Where the hypotheses enter: `p != l` (inertia acts on `Z_l(1)` trivially; `H^1_f = H^1_ur`); `L_p(A_f, 1) !=
infinity`, i.e. no eigenvalue `1` of Frobenius on `(V^D)^I` (weights).

**A4.11 `lem-h0`** (lemma; *proved here* in the corrected form (Chapter `ch:galrep` proves it too); reference:
Chapter 4, 5, 9, 11 cards; paper use: Lemma lem:h0, proof of Theorem thm:main, Conjecture conj:euler,
Proposition prop:ns, Section sec:anomaly).
Statement as in the paper. Let `l` be odd with `rho bar` irreducible. Then `H^0(Q, W^D) = H^0(Q, ad T(1) tensor
Q_l/Z_l)` is finite, and it vanishes iff `rho bar` is not isomorphic to `rho bar tensor chi bar_l`. For `l >= 5`
it always vanishes; for `l = 3` it vanishes iff `rho bar_{E,3}` is absolutely irreducible on `Gal(Qbar/Q(sqrt(-3)))`.
Its length `h_l(E)` is the largest `k` such that `rho mod l^k = (rho tensor chi_l) mod l^k`, and for `E` without
CM it is finite.
Statement as the book gives it (sharper; important_notes.md points 5 and 14). Same hypotheses. Then `h_l(E) = 0`
for every `l >= 5`, and `h_3(E) <= 1` with equality iff `rho bar_{E,3} = rho bar_{E,3} tensor chi_{-3}` iff the
image of `rho bar_{E,3}` is `N_s(F_3)` (Proposition prop:ns), for every `E` with `rho bar` irreducible, CM or not.
Expanded proof. (1) `rho bar` is absolutely irreducible (irreducible, `l` odd, complex conjugation has distinct
eigenvalues `+1, -1`: a stable line over `Fbar_l` would be an eigenline of `c`, defined over `F_l`, and the two
eigenlines of `c` cannot both be stable unless `rho bar` is reducible over `F_l`; Chapter `ch:galrep`). (2) `G_Q`-maps
`T/l^k -> (T/l^k)(1)`: `Hom(T, T)(1) = ad T(1) + Z_l(1)` (trace splitting, `2` invertible) and `H^0(Q, Z/l^k(1)) =
mu_{l^k}(Q) = 0`, so `H^0(Q, W^D)[l^k] = H^0(Q, ad(T/l^k)(1)) = Hom_{G_Q}(T/l^k, T/l^k(1))`; no trace condition is
needed. (3) `k = 1`: a nonzero `G_Q`-map `rho bar -> rho bar tensor chi bar_l` is an isomorphism (Schur, absolute
irreducibility) and the space of such maps has dimension at most one; so `H^0(Q, W^D)` is cyclic, `Z/l^h` with `h =
h_l(E)` (or `0`), hence finite. (4) If `phi` generates `H^0[l^k] = Z/l^k` (`k <= h`), then `l^{k-1} phi != 0`, so
`phi mod l != 0`, so `phi mod l` is an isomorphism, so `phi` is an isomorphism `rho mod l^k -> (rho tensor chi_l) mod
l^k` (Nakayama); conversely such an isomorphism has order `l^k`. Hence `h = max{k : rho mod l^k = (rho tensor chi_l)
mod l^k}`. (5) Determinants: an isomorphism mod `l^k` gives `chi_l = chi_l^3`, i.e. `chi_l^2 = 1` modulo `l^k` on `G_Q`.
As `chi_l(G_Q) = Z_l^x`, this forces `x^2 = 1 mod l^k` for every `l`-adic unit `x`: for `k = 1` this needs `l - 1 |
2`, i.e. `l = 3`; for `l = 3, k = 2` it fails at `x = 2` (`4 != 1 mod 9`). So `h_l(E) = 0` for `l >= 5` and `h_3(E)
<= 1`. (6) `l = 3`, `k = 1`: `chi bar_3 = chi_{-3}`; an isomorphism `rho bar -> rho bar tensor chi_{-3}` exists iff
`rho bar` is induced from `G_{Q(sqrt(-3))}` iff its restriction there is not absolutely irreducible (Clifford theory
for an index-two subgroup, applied to the absolutely irreducible `rho bar`; Chapter `ch:reps`); by Proposition prop:ns
this is the image `N_s(F_3)`. The paper's trace argument (`tr phi = chi_{-3}(g) tr phi`) shows every such
isomorphism has trace zero; with (2) it is not needed.
**Commentary (important_notes.md point 5).** The paper's last sentence ("for `E` without complex multiplication it
is finite", because "`rho = rho tensor chi_l` would force `a_p = 0` at all primes inert in `Q(sqrt(l*))`")
confuses the cyclotomic character `chi_l` with the quadratic character `chi_{l*}`: `rho = rho tensor chi_l` is
impossible for every `E` (it would give `p a_p = a_p` at good `p`). The correct statement is (5), which is stronger
and elementary. Consequence for Section sec:anomaly: "`h_3(E) <= 1` because some prime `p < 1223` inert in
`Q(sqrt(-3))` has `9` not dividing `a_p`" is replaced by "`h_3(E) <= 1` by Lemma lem:h0" (the numerical check is
valid but unnecessary). The book proves the sharp form and mentions the paper's route in one sentence.
**Commentary (important_notes.md point 14).** Even read with `chi_{l*}`, the CM alternative cannot occur in the
range of Theorem thm:main: CM by `Q(sqrt(l*))` needs that field imaginary of class number one, so `l in {3, 7, 11,
19, 43, 67, 163}`, and the prime ramified in the CM field divides the conductor, so `l | N`. The book records this in
a footnote-sized remark; with point 5 it is moot.
**Commentary (important_notes.md point 10).** The equivalence in (6) is Clifford theory for an ABSOLUTELY irreducible
representation; the paper says "irreducible". Step (1) supplies the upgrade.

**A4.12 `proof-thm-main`** (theorem (the proof of Theorem thm:main, Section 4.3 of the paper); *proved here* as an
assembly; every input is a card entry: Lemma lem:hecke (A4.4), Theorem thm:dfg14 (A4.2), Theorem thm:dfg37 (A4.7),
Theorem thm:dfg27 (A4.8), Lemma lem:dfg21 (A4.9), Lemma lem:h0 (A4.11), Lemma lem:fpr (A4.10), Definition def:terms
(A1.1), Lemma lem:tamfactor (A2.7), Lemma lem:twist (A2.4); Chapters 18, 20 cards; paper use: Theorem thm:main,
(eq:identity), (eq:thm)).
The steps, each with the hypothesis it uses.
Step 1 (degree to Hecke congruence ideal; uses `X_0(N)`-optimality, `l^2` not dividing `N`, `rho bar` irreducible):
`v_l(deg varphi_E) = v_l(r_E) >= v_lambda(eta^empty_{f, lambda})`, equality if `H^1(X_0(N), Z_l)_m` is free over
`T_m` (Lemma lem:hecke; Remark rem:free says this holds).
Step 2 (vary `Sigma`; uses `rho bar_f` irreducible, `l` not dividing `2N`): `Sigma = {q | N}`; Theorem thm:dfg14
gives `v(eta^empty) = v(eta^Sigma) - sum_{p in Sigma} v_l(L_p^{nv}(A_f, 1)^{-1})`. Only multiplicative primes
contribute, each `v_l(1 - p^{-2})`; at additive primes `L_p^{nv} = 1`; `M^Sigma = N prod_{q || N} q`.
Step 3 (Selmer length; uses `l` not in `S_f`, the hypothesis of Theorem thm:main, through DFG04 Theorem 3.7, which
is Taylor-Wiles): `v(eta^Sigma) = length H^1_Sigma(Q, W)`.
Step 4 (compare Selmer groups; uses `l` not in `S_f` through Theorem thm:dfg27, `l` odd at `infty`, and Lemma lem:h0
for `H^0(Q, W^D) = 0`): the four-term sequence of Lemma lem:dfg21 has last term `0`, so `length H^1_Sigma =
length H^1_f(Q, W) + sum_{p in Sigma} length H^1_f(Q_p, T^D)` (the `infty` term is `0`).
Step 5 (local terms; uses `p != l` for `p in Sigma`, i.e. `l` not dividing `N`): Lemma lem:fpr gives `length
H^1_f(Q_p, T^D) = v_l(L_p(A_f, 1)^{-1}) + v_l(Tam_p(A))`.
Step 6 (assemble): `v(eta^empty) = length H^1_f(Q, W) + sum_p v_l(Tam_p(ad T)) + sum_p v_l( L_p(A_f, 1)^{-1} /
L_p^{nv}(A_f, 1)^{-1} )`, and the last sum is `sum_{p | N} e_l(E, p)` (Definition def:terms): at multiplicative `p`
the naive factor equals the true one (cancellation), at additive `p` it is `1`. With Step 1 this is (eq:identity).
Step 7 ((eq:thm) from (eq:identity)): drop the Selmer length (`>= 0`); at multiplicative `p`, `v_l(Tam_p(ad T)) >=
t_l(E, p)` (Lemma lem:tamfactor); at additive `p` of type other than `I_n^*`, `t_l(E, p) = 0` unless `p = 2` with
`v_2(j) < 0` (see the Commentary), and `v_l(Tam_p) >= 0`; at `p` of type `I_n^*`, `ad T` is unchanged by the
quadratic twist that makes the reduction multiplicative, so `v_l(Tam_p(ad T)) >= v_l(-v_p(j)) = t_l(E, p)` by
Lemma lem:tamfactor applied to the twist.
**Commentary (new, Section 9 point N4).** For Step 7 the paper uses "the curve `E_{p}` of Lemma lem:twist",
i.e. the twist by `chi_p`; Lemma lem:twist is for odd `p` only, but Theorem thm:main allows `2 | N`, and a curve
with additive, potentially multiplicative reduction at `2` (Kodaira symbol `I_n^*` at `2`, `v_2(j) < 0`) has
`t_l(E, 2) = v_l(-v_2(j))`, possibly positive. The argument is purely local and goes through: over `Q_2`, `E` is
the quadratic twist of a Tate curve with parameter of valuation `-v_2(j)` (Silverman ATAEC V.5), `ad T|_{G_{Q_2}}`
is unchanged by the twist, and the proof of Lemma lem:tamfactor applies verbatim at `q = 2` (it needs only `q !=
l`, `l` odd). The book states Step 7 for "potentially multiplicative additive `p`, including `p = 2`", with this
local argument, and uses `n = -v_p(j)`, not the index of the Kodaira symbol (which differs at `2`, Section sec:wild).
Notation: the paper's `E_{\{p\}}` is the book's `E^{(p)}`.
Rigour: the assembly is *proved here*; DFG04 Theorem 3.7, Theorem 2.7, Proposition 1.4(c), Lemma 2.1, (57),
FPR94, ARS12 are *stated; reference*.

**A4.13 `rem-ko`** (remark (the paper's Remark rem:ko); (1) *proved here* from A2.7 and A4.12; (2) *stated;
reference* KimOta Theorem 1.1 and Definition 2.12; paper use: Remark rem:ko, Section sec:tam, Section 1.5).
Statement. (1) At a multiplicative prime `q = 1 mod l` with `l | n` and unit part of the Tate parameter an `l`-th
power in `F_q^x`, `v_l(Tam_q(ad T)) >= t_l(E, q) + 1`, and (eq:identity) raises the bound of (eq:thm) by
`min(v_l(n), v_l(q - 1), v_l(c))`. (2) Kim-Ota: for `N = N^+ N^-`, `N^-` square-free, `l >= 5`, `l` not dividing
`N`, `l` not in `S_f`, and `rho bar` ramified at every `q | N^-` with `q = +-1 mod l`: `ord_lambda eta_f(N) =
ord_lambda eta_f(N^+, N^-) + sum_{q | N^-} t_f(q)`, `eta_f(N^+, N^-)` the congruence ideal in the `N^-`-new quotient,
`t_f(q)` the Tamagawa exponent (= `t_l(E, q)` by Lemma lem:tamagawa-exp). As `eta_f(N^+, N^-)` is integral,
`v_l(r_E) >= sum_{q | N^-} t_l(E, q)`, which (eq:thm) contains without `l >= 5` and `q != +-1 mod l`; the equality is
theirs.
Expansion for the book: identify `ord_lambda eta_f(N)` with `v_l(r_E)` (Lemma lem:crit: the Hecke congruence ideal
of `f` in the full Hecke algebra of level `N`; the writer checks that Kim-Ota's `eta_f(N)` is this ideal and not a
cohomological one; if cohomological, Lemma lem:hecke gives the comparison).
Chapters: `ch:moddeg`, `ch:modgalrep`, `ch:congruence`.

**A4.14 `thm-twist`** (theorem (the paper's Theorem thm:twist, twist monotonicity); *proved here*; reference: Atkin-Li
(levels of twists; a textbook reference for the level `lcm(M, D^2)` is Shimura71, Chapter 3, cited by section;
the writer checks the exact proposition), Lemma
lem:crit, strong multiplicity one (Chapter `ch:hecke`); paper use: Theorem thm:twist, Section sec:twisting, Theorem
thm:quant Step 1).
Statement. Let `E/Q` have conductor `N`, `S` a set of odd primes, `D = prod_{q in S} q`, `chi_S = prod_{q in S}
chi_q`, `E_S = E tensor chi_S` of conductor `N_S`. If `q^2 | N` for every `q in S` and `lcm(N_S, D^2) | N`, then
`r_{E_S} | r_E`; if moreover `lcm(N, D^2) | N_S`, then `r_{E_S} = r_E`.
Expanded proof. (1) `iota : h -> h tensor chi_S = sum chi_S(n) a_n(h) q^n` maps `S_2(Gamma_0(N_S))` into
`S_2(Gamma_0(lcm(N_S, D^2)))` (twist of level `M` by a character of conductor `D` with `chi_S^2` trivial lands in
level `lcm(M, D^2)`; reference), hence into `S_2(Gamma_0(N))`; it preserves integrality (`chi_S(n) in {0, +-1}`) and
intertwines `T_p` with `chi_S(p) T_p` for `p` not dividing `D N_S`. (2) `iota(g) = f` for `g = f_{E_S}`:
coefficients at `n` prime to `D` agree (`a_p(f) = chi_S(p) a_p(g)`, multiplicativity, the recursion with
`chi_S(p)^2 = 1`, and at `p | N` not in `S` the twist is unramified so `a_p` changes by `chi_S(p)`); at `n` divisible
by some `q in S` both are `0` (`a_{q^k}(f) = 0` as `q^2 | N`). (3) `g^perp` (the Petersson complement of the newform
`g` at level `N_S`) is the sum of the generalised eigenspaces of the other `T_p`-systems (`p` not dividing `N_S`),
each differing from that of `g` at infinitely many `p` (strong multiplicity one). `iota` sends such a space into the
generalised eigenspace of the twisted system, which differs from that of `f` at infinitely many `p`, hence lies in
`f^perp` (same reasoning at level `N`). (4) `g = h mod r` with `h in g^perp` integral gives `f = iota(g) = iota(h)
mod r` with `iota(h) in f^perp` integral, so `r | r_E` (definition of `r_E`, or Lemma lem:crit). With `r = r_{E_S}`
this is the first claim; under the second hypothesis the roles of `E` and `E_S` can be exchanged (`E = (E_S)_S`).
Hypothesis check (the paper's (a), (b), (c), verified here): (a) `I_n^*` at each `q in S`: `N_S = N/D`,
`lcm(N/D, D^2) = N`; (b) `I_0^*`: `N_S = N/D^2`, `lcm = N`; (c) `II, III, IV` or a dual, `q >= 5`: `N_S = N`, both
hypotheses, equality. Worked instances (verified with Cremona's `alldegphi`): (c) 121a1 (`II` at `11`) and 121c1
(class of the twist, `IV/IV^*`): `deg = 6` and `6`; (a) 539c1 (`I_3^*` at `7`, `deg 288`) and 77c1 (`deg 6`); 980i1
(`I_5^*`, `deg 2880`) and 140b1 (`deg 60`); 121d1 (`I_1^*` at `11`, `deg 24`) and 11a1 (`deg 1`); (b) 539d1 (`I_0^*` at
`7`, `deg 72`) and 11a1 (`deg 1`).
The paper's data paragraph. "On the working set, for the 157,938 pairs (curve, prime of type `I_n^*`) and the
292,580 pairs (curve, prime of potentially good additive type), `v_l(deg varphi_E) >= v_l(deg varphi_{E_q})` holds for
`l in {3, 5, 7, 11, 13}`, `l^2` not dividing `N`, with no exception, with equality in every pair of case (c) and
strict inequality only in case (b), where the difference is the Euler term of Theorem thm:quant."
**Commentary (new, Section 9 point N2).** "Strict inequality only in case (b)" contradicts Theorem thm:quant and the
paper's own example. For a single `I_n^*` prime `q >= 5` and `l = 3` (not dividing `N`, `E[3]` irreducible),
Theorem thm:quant gives `v_3(deg varphi_E) >= v_3(r_{E_q}) + v_3(q^2 - 1) >= v_3(deg varphi_{E_q}) + 1`, a strict
inequality in case (a). Instances: 539c1 versus 77c1 (`v_3`: `2` versus `1`), 980i1 versus 140b1 (`2` versus `1`),
121d1 versus 11a1 (`1` versus `0`); all three curves have surjective mod `3` image and `3` does not divide `N`. The
sentence should read "strict inequality only in cases (a) and (b), where the difference is at least the Euler term
of Theorem thm:quant". The book quotes the corrected sentence and uses the three pairs as examples. (Whether the
paper's count itself is right cannot be checked here; only the summary sentence is inconsistent.)
Rigour: *proved here*; the level of a twist is *stated; reference*.

**A4.15 `proof-thm-quant`** (theorem (proof of Theorem thm:quant, Steps 1 to 4); *proved here*, with DFG04
Proposition 1.4(c) and Remark rem:free as stated inputs; reference: paper Section sec:twisting; Chapters 3, 13, 14, 20
cards; paper use: Theorem thm:quant).
Set-up. `f = f_E`, `g = f_{E_S}` of level `N_S`, `D = prod_{q in S} q`, `Sigma = S`, `O = Z_l`. By Lemma lem:twist,
`E_S` is good at the `I_0^*` primes of `S` (`delta_q = 2`) and multiplicative at the `I_n^*` primes (`delta_q = 1`),
so `N_S^Sigma = N_S prod_{q in S} q^{delta_q} = N`: the `S`-depleted form `g^S` lives at level `N`, and `iota(g^S) =
f` (twisting kills the coefficients at multiples of `D`, so `iota(g) = iota(g^S)`).
Step 1 (transport of congruences; elementary; uses `l != q` for `q in S`, strong multiplicity one, Lemma lem:crit
over `Z_l`). `T` = full Hecke algebra of level `N`, `pi : T -> Z` the eigencharacter of `g^S`, `m` the maximal ideal
of `T_l` containing `ker pi` and `l`; `U_q in m` for `q in S` (`pi(U_q) = 0`). (i) The `pi`-generalised eigenspace in
`S_2(Gamma_0(N)) tensor Qbar` is the line of `g^S`: the forms with the `T_p`-eigenvalues of `g` (`p` not dividing
`N`) are the span of the `g(dz)`, `d | N/N_S`; on it, for `q in S`, `U_q` has characteristic polynomial `X(X - a_q(g))`
on `<g, g(qz)>` (`I_n^*` case) or `X(X^2 - a_q(g) X + q)` on `<g, g(qz), g(q^2 z)>` (`I_0^*` case), so the eigenvalue `0`
has multiplicity one, with eigenvector the depleted form. (ii) Every `U_q`-eigenvalue on forms of level dividing `N`
is either `0` or an `l`-adic unit (`+-1`; roots of `X^2 - aX + q`, whose product is `q`; `a_q(h) = 0` when `q^2` divides
the level), so the generalised eigenforms whose eigencharacter is congruent to `pi` mod `m` have `U_q`-eigenvalue
`0` for `q in S`; the other stabilisations of `g` are not in the `m`-part. (iii) Hence the `m`-component of
`S_2(Gamma_0(N); Z_l)` is the line of `g^S` plus generalised eigenspaces of systems coming from newforms `h != g` of
level dividing `N`. (iv) For `h'` in such a space, `iota(h') in S_2(Gamma_0(N))` (`lcm(N, D^2) = N`) lies in the
generalised eigenspace of `chi_S(p) a_p(h)`, which differs from the system of `f` at infinitely many `p`; so `iota(h')
in f^perp`. (v) Lemma lem:crit over `Z_l`, run for `g^S` (its generalised eigenspace is a line, so `T tensor Q = Q x
T'` again and the proof goes through with "T-stable complement" in place of "Petersson complement"): `l^{v(eta^Hecke(g^S))}`
is the largest `l^t` with `g^S = h mod l^t`, `h` integral in the `T`-stable complement of the `g^S`-line. (vi) Apply
the idempotent `e_m in T_l` to `h`: `e_m h = e_m g^S = g^S mod l^t`, `e_m h` integral, in the complement, and in the
`m`-part. (vii) `f = iota(g^S) = iota(e_m h) mod l^t` with `iota(e_m h) in f^perp` integral, so `v_l(r_E) >=
v_l(eta^Hecke(g^S))`.
Step 2 (Hecke versus cohomological ideal; Lemma lem:ddt417 with `L = H^1(X_0(N), Z_l)_m`, the pairing `delta hat_!`
of A4.1, `pi`; `L[wp] = M_{g^S, lambda}` of rank `2`, Gram determinant `(eta^S_{g,lambda})^2` up to a unit; no
freeness needed): `v_l(eta^Hecke(g^S)) >= v_lambda(eta^S_{g, lambda})`.
Step 3 (DFG04 Proposition 1.4(c) for `g`: `rho bar_g = rho bar tensor chi_S` irreducible, `l` not dividing `2N_S`):
`v(eta^S_g) = v(eta^empty_g) + sum_{q in S} v_l(L_q^{nv}(A_g, 1)^{-1}) = v(eta^empty_g) + sum_{q in S} e_l(E, q)`,
because `A_g = A_f` (`ad` is twist invariant), `g` has `delta_q >= 1` at `q in S` (so its naive factor is the true
one), and the true factor of `A_f` at `q` is the one `f` omits (`a_q(f) = 0`); values from Lemma lem:euler.
Step 4 (level `N_S`; uses multiplicity one at level `N_S`, Remark rem:free): `v(eta^empty_g) = v_l(r_{E_S})`
(Lemma lem:hecke for `E_S` in the free case). Then `v_l(deg varphi_E) = v_l(r_E)` (`l` not dividing `N`) gives the
first inequality; the second because `r_{E_S}` is an integer.
Commentary for the reader (not an error): without Remark rem:free, Lemma lem:hecke only gives `v_l(r_{E_S}) >=
v(eta^empty_g)`, the wrong direction for the middle term; but `v(eta^empty_g) >= 0` (an integral ideal) still gives the
outer inequality `v_l(deg varphi_E) >= sum_{q in S} e_l(E, q)` with no multiplicity-one input. The book proves the
outer inequality first and then the refinement.
Worked checks (Cremona degrees; B4): 539c1 (`l = 3`): `2 >= v_3(r_{77c}) + v_3(48) = 1 + 1`, equality; 980i1 (`l =
3`): `2 >= v_3(r_{140b}) + 1 = 1 + 1`, equality; 121d1 (`l = 3`): `1 >= 0 + v_3(120) = 1`, equality; 539d1 (`l = 3`):
`v_3(72) = 2 >= 0 + (v_3(6) + v_3(64 - 4)) = 2`, equality. The hypothesis "`E[l]` irreducible" cannot be dropped:
539d1 at `l = 5` has `e_5 = v_5(6) + v_5(60) = 1` but `v_5(72) = 0`, and its mod `5` image is Borel (5B.4.1); 539a1
(`I_2^*` at `7`, mod `3` image 3B) has `e_3 = v_3(48) = 1` and `v_3(320) = 0`.

**A4.16 `rem-after-quant`** (remark (the remark after the proof of Theorem thm:quant); (1), (3) *proved here*, (2)
*proved here* given (eq:identity) and Remark rem:free; paper use: the remark after Theorem thm:quant).
Statement. (1) Theorem thm:quant is the twist-and-lower argument of Section sec:proof read the other way: the level
is raised from `N_S` to `N`, the price is the level-raising Euler factor. For `l = 3` a single `I_n^*` prime `q >= 5`
(`3 | n` or not) forces `3 | deg varphi_E` (`v_3(q^2 - 1) >= 1` for every `q >= 5`), and so does an `I_0^*` prime
with `q = 1 mod 3` (`v_3(q - 1) >= 1`); neither needs the hypothesis on `Q(sqrt(-3))`, and neither is in Theorem
thm:qual. (2) Under the hypothesis of Theorem thm:main, (eq:identity) for `E` and `E_S` gives `v(eta^empty_f) =
v(eta^empty_g) + sum_{q in S} e_l(E, q)`: the Selmer groups and Tamagawa factors coincide (same `ad T`); at an `I_n^*`
prime the term `e_l(E, q) = v_l(q^2 - 1)` appears for `E` and `0` for `E_S` (multiplicative); at an `I_0^*` prime `q`
is good for `E_S` and `Tam_q(ad T) = 1` for both (`ad V` is unramified at `q`, so `H^1(I_q, ad T)` is torsion-free);
at other primes `e_l` is the same for `E` and `E_S` (twist unramified there). So the first inequality is an equality
when `H^1(X_0(N), Z_l)_m` is free (and multiplicity one at `N_S`), which Remark rem:free asserts. (3) Step 1 fails
for `II, IV, III` and duals: the twist does not lower the level, `f` is its own depletion, Theorem thm:dfg14 gives no
factor; these terms come only through Theorem thm:dfg37, i.e. with the hypothesis on `Q(sqrt(l*))`, and Section
sec:anomaly shows it cannot be dropped there (3Ns curves, whose violations involve a type `III` term).
Chapters: `ch:congruence`, `ch:hecke`.

### A5. The paper's Section 5: the boundary of the hypothesis (Section 21.14)

**A5.1 `proof-prop-ns`** (proposition (proof of Proposition prop:ns); *proved here*; reference: Zywina15 (cited by
section only, important_notes.md point 4), Chapter 1 card (subgroups of `GL_2(F_3)`, orbits on lines), Chapter 4
(induction, Frobenius reciprocity, absolute irreducibility), Chapter 5 (quartic on lines), Chapter 9 (3-division
polynomial), Chapter 11 card; paper use: Proposition prop:ns, Section sec:anomaly, Conjecture conj:euler).
Statement: A1.12.
Expanded proof, step by step. (1) `det rho bar_{E,3} = chi bar_3 = chi_{-3}` (Weil pairing) cuts out `Q(sqrt(-3))`, so
`rho bar(G_{Q(sqrt(-3))}) = H cap SL_2(F_3)`, `H` the image. (2) Possible `H`: `E[3]` irreducible, `det` surjective, and
`H` contains `rho bar(c)`, an element of determinant `-1` and trace `0`. Pure group theory (Chapter 1, by enumeration of
the 55 subgroups of `GL_2(F_3)`) leaves exactly `GL_2(F_3)` (order 48), `N_ns(F_3)` (order 16, semidihedral) and
`N_s(F_3)` (order 8, dihedral); the nonsplit Cartan `C_ns(F_3) = F_9^x` (cyclic of order 8) is excluded because its
elements of determinant `-1` have order `8`, hence nonzero trace. (The paper cites Zywina15 for the list; the book
proves it.) (3) Determinant-one subgroups: `SL_2(F_3)`, `Q_8`, and `C_4 = <(0, 1; -1, 0)>`. (4) `SL_2(F_3)` and `Q_8`
act absolutely irreducibly on `F_3^2`; `C_4` is abelian with eigenvalues `+-i` in `F_9`, so over `F_9` it splits as
`psi + psi^{-1}`, `psi` of order `4`. (5) In the third case, Frobenius reciprocity gives a nonzero map `rho bar tensor
F_9 -> Ind psi`, an isomorphism by dimension and irreducibility, so `rho bar = Ind psi` and `rho bar tensor chi_{-3} =
rho bar` (a representation induced from an index-two subgroup is invariant under the twist by the character of that
subgroup); hence `H^0(Q, ad rho bar(1)) != 0` (A4.11 step (3)) and `h_3(E) >= 1`, in fact `h_3(E) = 1` by A4.11 step (5).
(6) Lines: the four roots of `psi_3` are the `x`-coordinates of the four lines of `E[3]` (`x(P) = x(Q)` iff `Q = +-P`), so
the Galois action on roots is the action of `H` on `P^1(F_3)`; `N_s(F_3)` has two orbits of size two (the two Cartan
lines; the two others), `N_ns(F_3)` and `GL_2(F_3)` are transitive; `psi_3` has no rational root (`E[3]` irreducible);
so `psi_3 = ` (leading coefficient `3`) times two irreducible quadratics in the first case and is irreducible otherwise.
Where the hypotheses enter: "`E[3]` irreducible" in (2) and (6); "without CM" nowhere (point 9 below).
**Commentary (important_notes.md point 1).** The paper justifies (4) by "they are non-abelian and act faithfully".
That is not enough (a Borel subgroup of `GL_2(F_3)` is non-abelian, faithful and reducible). Missing step: a subgroup
fixing a line over `Fbar_3` lies in a Borel subgroup, so its commutator subgroup lies in the unipotent radical, hence is
abelian of exponent `3`; `Q_8` has commutator subgroup `{+-1}` (not unipotent) and `SL_2(F_3)` has commutator subgroup
`Q_8` (not abelian). The book inserts this sentence.
**Commentary (important_notes.md point 2).** With the standard models, `N_s(F_3)` lies in `N_ns(F_3)` with index two
(and `N_s(F_5)` in a subgroup of order 96 with image `S_4` in `PGL_2(F_5)`). The paper does not claim maximality;
the book warns readers who import the large-`l` picture that `N_s` is not maximal at `l = 3, 5`.
**Commentary (important_notes.md point 4).** The exact theorem number in Zywina15 for the list of mod 3 images (and in
Serre72 for Dickson's classification) could not be confirmed; cite by section, and note that (2) is proved directly.
**Commentary (important_notes.md point 9).** "Without complex multiplication" is not used; CM curves with `3` split in
the CM field have image in `N_s(F_3)` and `2 + 2` factorisation (121b1, CM by `Q(sqrt(-11))`, is an example found in
the check reported in A1.12). The book drops the hypothesis or notes that it is unnecessary.

**A5.2 `rem-ns`** (remark (the paper's Remark rem:ns); the displayed identity *proved here* from Lemma lem:dfg21,
Lemma lem:fpr, Lemma lem:h0 under the stated hypothesis; the rest is *stated* (data); paper use: Remark rem:ns,
Conjecture conj:euler, Open question 2).
Statement. When `l = 3` and the image is `N_s(F_3)`, Theorem thm:dfg37 does not apply, but if `H^0(Q, V^D) =
H^1_f(Q, V^D) = 0` the sequence of Lemma lem:dfg21 gives `length H^1_Sigma(Q, W) = length H^1_f(Q, W) + sum_{p in
Sigma} (v_l(L_p(A_f, 1)^{-1}) + v_l(Tam_p(A))) - h_l(E)`. If `v(eta^Sigma) = length H^1_Sigma(Q, W)` still held, then
(eq:identity) would hold with `h_l(E)` subtracted: the shape of Conjecture conj:euler. Data: `h_3(E) = 1` for every
3Ns curve; (eq:thm) fails for `31%`, `23%`, `18%` of them on the three ranges, always by exactly one, and never for any
other curve.
Steps for the book: (1) `H^0(Q, V^D) = 0` is automatic (weights: `Hom_{G_Q}(V, V(1)) = 0`); (2) `H^1_f(Q, V^D) = 0`
is the hypothesis, proved by DFG04 Theorem 2.7 only for `l` not in `S_f`; the book says that in the dihedral case it
is an input not supplied by the paper (the writer may mention, without relying on it, that later work on adjoint
Selmer groups covers more cases; cite only if a precise reference is checked); (3) the last term of the four-term
sequence has length `h_3(E) = 1`; (4) arithmetic: lengths in an exact sequence of finite groups alternate.
Chapters: `ch:blochkato`, `ch:galcoh`, `ch:congruence`.

### A6. The paper's Section 6: the computations (Sections 21.15 to 21.17)

General note for all of A6. The paper's tables are `\input` from files `tables/*.tex` that are NOT in this repository
(only `note_Oct10_7pm.tex` is). The book describes each table from its caption and from the numbers quoted in the
text; it must not invent table entries. Every count in A6 is *stated* (data of the paper); the book's own checks are
the small-range ones of B4 and Section 8.2. Chapter `ch:computation` covers PARI, ecdata and the protocol; here the
tour explains what each statement means and what it tests.

**A6.1 `data-protocol`** (data description; *stated*; reference: Cremona97, ecdata commit `25cec5e`, PARI 2.15,
Sutherland16; Chapter `ch:computation`; paper use: Section sec:data, Section 6.1).
Content. Tables: every curve of conductor below `500000` with Kodaira symbols, Tamagawa numbers, modular degrees,
isogeny classes, torsion, mod `l` images (Sutherland's labels). Optimality determined for every class with `N <=
400000` and for `359,009` further classes up to `500000`. Ranges: working set `N <= 300000`, hold-out `300000 < N <=
400000`, extension `400000 < N <= 500000`, out-of-table set (Section sec:oot). Order of discovery: (eq:main) and
Conjecture conj:eis found on the working set, then tested once on the hold-out, then on the extension; (eq:twist)
replaced a weaker form on the working set and was then tested once on hold-out and extension; the Euler-factor rule
came last (minima by Kodaira type, then the terms at `2`, `3` fixed by PARI's factors, then tested on all four
ranges); the correction `h_l(E)` was identified last, from the exceptions. Hence: blind test for (eq:main), (eq:twist),
Conjecture conj:eis; only a confirmation for Conjecture conj:euler on the hold-out and the extension; the out-of-table
curves, generated before the rule was formulated, are its blind test. Recomputations: Kodaira types and discriminant
exponents with PARI from the `a`-invariants; Euler factors with `lfunsympow`, `lfuneuler`; Tate parameters with
`ellinit` over `Q_q`; fifteen modular degrees with `ellmoddegree`; mod 3 images checked against `psi_3`.
What the book adds. (1) The meaning of "pre-registered": statement fixed before the data it is tested on were
looked at. (2) Which statement had which kind of test (a three-row table: statement, found on, tested blind on).
(3) A caution: optimality beyond `400000` is partial, so the extension tests use the classes where it is known.
(4) The protocol caveat stated by the paper itself (the rule is not blind-tested on the hold-out).
**Commentary (new, Section 9 point N11, minor).** The abstract says the corrected inequality holds "for every optimal
curve of conductor at most 500000"; the statement (Conjecture conj:euler) concerns curves with `E[l]` irreducible and
without CM, and optimality above `400000` is known only for part of the classes. The book quotes the precise range.

**A6.2 `table-uniform`** (how to read Table tab:uniform; *stated*; paper use: Section 6.2).
Columns (from the caption): for each range and `l in {3, 5, 7, 11, 13}`: number of curves with `E[l]` irreducible,
not CM, positive bound in (eq:rule); violations (all zero); equality rate; violations when `h_l` is dropped (all 3Ns
curves at `l = 3`); and the "III-free" rule (type `III, III^*` terms omitted, no correction): positive bounds,
violations, equality rate. Reading: the III-free rule holds for every curve without any correction because the
3Ns violations always involve a type `III` term (A6.7); dropping the correction while keeping the type `III` terms
produces exactly the 3Ns violations. The weights `w_3` at `q = l = 3` only sharpen the bound.

**A6.3 `calibration`** (data argument (Section sec:sharp); *stated* with the arithmetic *checked here*; paper use:
Section sec:sharp; Chapter `ch:computation` for the statistics).
Content. Among `366,151` working-set curves with `E[3]` irreducible, not CM and bound `0`, `53.2%` have `3` not
dividing `deg varphi_E`. If `v_3(deg varphi_E)` were independent of the local data, the `867,578` curves with a positive
bound would give about `605,000` violations; there are none. Equality rates `57.5%, 75.6%, 84.1%, 91.6%, 92.4%` at `l =
3, 5, 7, 11, 13`; mean excess `0.63` at `l = 3`. Under Theorem thm:main the excess is the Selmer length plus the excess of
the Tamagawa factors over `t_l`. The odd part of `deg varphi_E` equals `prod l^{b_l}` (`b_l` the right side of
(eq:twist)) for only `1.85%` of `1,226,216` optimal non-CM curves with no odd isogeny; the quotient is most often `9, 3,
15, 45, 27, 21`.
Expansion for the book. (1) The null model: `P(v_3(deg) < b)` estimated from the bound-0 population, summed over the
bounded curves. (2) Sanity check done here: the `v = 0` part alone gives at least `0.532 * 867,578 = 461,551` expected
violations; the paper's `605,000` (that is `69.7%` of the bounded curves) also counts `v = 1 < b = 2` etc., so it is
plausible; the exact figure needs the distribution of bounds (PARI and the data). (3) What it shows: the bound is not
a tautology of the size of degrees; what it does not show: independence is a crude null, and the zero count is
evidence for the inequality, not a proof. (4) Equality rates and mean excess are descriptive.

**A6.4 `tamagawa-test`** (data (Section sec:tam); *stated*, percentages *checked here*; paper use: Section sec:tam,
Remark rem:ko(1), Lemma lem:tamfactor).
Content. At a prime `q` of type `I_n` with `l | n` and `q = 1 mod l` the bound is raised by `min(v_l(n), v_l(q - 1),
v_l(c_q))`; tested on working-set curves satisfying the hypothesis of Theorem thm:main with such a prime. `l = 3`:
`46,222` curves, `12,095` with a positive extra term (total extra `12,125`), no exception, equality rises from
`20,822` (`45.0%`) to `28,007` (`60.6%`). `l = 5`: `10,940` curves, `1,646` with positive extra term, equality from
`7,333` (`67.0%`) to `8,610` (`78.7%`). Percentages recomputed: `45.05%`, `60.59%`, `67.03%`, `78.70%`: consistent.
Reading: this tests (eq:identity) (the Tamagawa term), not only (eq:thm).
**Commentary (new, Section 9 point N9, notation).** Here `c_q` denotes the class `c` of Lemma lem:tamfactor at `q` (the
unit part of the Tate parameter modulo `l`-power powers), while Section 1.4 uses `c_q` for the Tamagawa number
`#Phi_q(F_q)`. The book writes `c(q)` or `c_{u,q}` for the class.

**A6.5 `isolated-terms`** (data (Section sec:iso, Table tab:iso); *stated*; paper use: Section sec:iso).
Content. Working-set curves with exactly one additive prime `q >= 5`, `q != l`, and no multiplicative prime with `l | n`:
minimum of `v_l(deg varphi_E)` by Kodaira type and by `e_l(E, q)`; for `l = 3, 5, 7` the minimum equals `e_l` in every
cell, and every curve has `v_l >= e_l`; for `I_n^*` the excess over `e_l` has minimum exactly `v_l(n)` (the `t_l` term).
Cells with `e = 0` (`III`: `5,534` curves, `I_0^*`: `5,394`) have minimum `0`; for `I_0^*` the term runs up to `e = 6`.
Multiplicative primes: for a single multiplicative `q` with `l | n` and no additive prime, `min(v_l(deg) - v_l(n)) = 0`
for every `v_l(q^2 - 1) <= 6` (no Euler term at multiplicative primes, as Definition def:terms predicts). Two primes of
type `II/II^*`: `9 | deg` for all `2,502` such curves, and `f` is never congruent to its own twist by the character
ramified at both primes (`0` of `2,502`).
Reading Table tab:iso: rows = Kodaira type; columns = value of `e_3(E, q)`; entries = minimum of `v_3(deg)` (number of
curves). The table is at `l = 3`; the text says the same holds at `l = 5, 7`.

**A6.6 `corollary-forms`** (data (Section sec:forms, Table tab:counts); *stated*; paper use: Section sec:forms,
Proposition prop:forms, Conjecture conj:eis).
Content. For each range and small `l`: curves (optimal, non-CM, `E[l]` irreducible) with positive right side in
(eq:main) and in (eq:twist), violations (none); Eisenstein curves with positive bound and violations of Conjecture
conj:eis (none). Equality rates for (eq:twist): `39.4%, 71.1%, 81.2%, 91.5%` at `l = 3, 5, 7, 13`; for (eq:main):
`36.9%, 69.7%, 80.4%, 91.2%`; the rule bounds `867,578` curves instead of `705,563` at `l = 3`. Where the hypothesis of
Theorem thm:main fails on the working set: `1,170` 3Ns curves; curves with `l | N` (`455,707` of the `913,244` pairs
`(E, l)` with a positive multiplicative bound at `l = 3`, `175,798` at `l >= 5`); dihedral curves at `l >= 5`, not
singled out. None violates (eq:rule).
Reading Table tab:counts: columns "(eq:main) > 0", "viol.", "(eq:twist) > 0", "viol.", Eisenstein column; rows: ranges
times `l`.

**A6.7 `ns3-boundary`** (data (Section sec:anomaly, Table tab:ns); *stated*, with the theoretical parts *proved here*
(A4.11, A5.1); paper use: Section sec:anomaly, Remark rem:ns, Conjecture conj:euler).
Content. (eq:thm) with all types and no correction: `364, 68, 43, 0` violations on the four ranges, all at `l = 3`, all
3Ns curves, each with `psi_3 = ` two quadratics; no `GL_2(F_3)` or `N_ns(F_3)` curve violates. Every 3Ns curve has a
prime of type `III/III^*` with positive `e_3`; the inequality fails for `31%, 23%, 18%` of them, always by one; the
violation involves a prime `p = -1 mod 3` with `t_3(E, p) >= 1`. `h_3(E) = 1` for every 3Ns curve, `0` for the others.
Type `III` primes of violating curves: `q = 1` and `q = 11 mod 12` in comparable numbers, some `q = 2`.
Expansion for the book. (1) `364/1,170 = 31.1%`: consistent with the working-set count of A6.6. (2) Why `q = 1, 11 mod
12`: `e_3(E, q) = v_3(q - chi_{-4}(q)) > 0` iff (`q = 1 mod 4` and `q = 1 mod 3`) or (`q = 3 mod 4` and `q = 2 mod 3`).
(3) Check made here on `N < 10,000` (ecdata): of the `90` optimal 3Ns curves, `74` have a type `III/III^*` prime `q >= 5`
(residues of these primes mod 12: `11` (42 times), `1` (32), `5` (6)); every curve has at least one with `q = 1, 11 mod
12` or else has `2^8 || N` (`16` curves: conductors 3840, 4864, 6912), where `e_3(E, 2)` must come from PARI's factor.
Consistent with the paper's statement; the `q = 2` cases need PARI. Example: 726a1 (B4).
**Commentary (important_notes.md point 5, second half).** "`h_3(E) <= 1` because some prime `p < 1223` inert in
`Q(sqrt(-3))` has `9` not dividing `a_p`" is replaced by "`h_3(E) <= 1` by Lemma lem:h0 (A4.11 step (5))".
**Commentary (important_notes.md point 3).** The label 3Ns must be checked against Sutherland16; the ecdata usage is
consistent with "normaliser of a split Cartan subgroup" (the `2 + 2` check of A1.12).
Reading Table tab:ns: columns from the caption: curves with image 3Ns (optimal, non-CM, `E[3]` irreducible); how many
have a positive type `III` term; violations of (eq:thm); violations by other curves; how many have `h_3 = 1`; residue
classes mod 12 of the type `III` primes of the violators (or `q = 2`); shortfall (always `1`).

**A6.8 `wild-primes`** (data (Section sec:wild, Table tab:isolated); *stated*; paper use: Section sec:wild, Remark
rem:wild, Conjecture conj:euler (the weights `w_3`), Proposition prop:forms).
Content. Table tab:isolated (kept from the earlier version): at `l = 3`, untwisted rows give the minimum of `v_3(deg)`
over working-set curves with no multiplicative `q` with `3 | n_q` and all additive primes of one Kodaira type, by type
and number of primes; twisted rows give the minimum over curves whose only contribution to (eq:twist) comes from
primes of the given type, at odd `q` or at `q = 2`, by total weight. Findings: `2` contributes nothing through `II,
II^*` (`v_3(deg) = 0` for `14,182` of `44,672` curves whose only candidate is such a prime) and nothing through `I_n^*`
with `3 || n`, though with `9 | n` the minimum is `1`. Explained by Definition def:terms with PARI's factor: `II` at `2`
has `P_2 = 1`, `e_3 = 0`; `IV, IV^*` at `2` have `e_3 = 1`; `I_n^*` at `2` has `t_3 = v_3(-v_2(j))` when potentially
multiplicative, `0` otherwise, and the symbol's `n` is not `-v_2(j)`. With the weights of (eq:twist) at `2` counted as if
`2` were odd, (eq:twist) fails thousands of times per range; with Definition def:terms never. At `q = 3`, potentially
good, `l = 3`: minima `1` for `II, IV, III^*`, `2` for `II^*, IV^*`, `0` for `III, I_0^*`: these are the weights `w_3`,
outside Theorem thm:main (`l | N`), not derived from an Euler factor. For `l = 5, 7` nothing extra is needed.
Expansion for the book: the worked value `P_2(X) = 1 + 2X` gives `e_3 = v_3(1 + 2/4) = v_3(3/2) = 1` (checked), and its
meaning (one inertia-invariant line in `ad V` with geometric Frobenius eigenvalue `-1`, as for type `IV` at `q >= 5`
with `chi_{-3}(2) = -1`: `L_2(A_f, s)^{-1} = 1 - chi_{-3}(2) 2^{-s}`, so `L_2(Sym f, s)^{-1} = 1 - chi_{-3}(2)
2^{-(s-1)} = 1 + 2 * 2^{-s}`, i.e. `P_2(X) = 1 + 2X`; this is an analogy that explains the value, not a proof at
the wild prime `2`). A worked example at `q = 2` with
`v_2(j) < 0` and type `I_n^*` (`n != -v_2(j)`) needs PARI (writer to supply).

**A6.9 `out-of-table`** (data (Section sec:oot, Table tab:oot); *stated*; paper use: Section sec:oot).
Content. Curves with prescribed local types and `500000 < N <= 4 * 10^6` (families with a type `IV/IV^*` prime, with
two or three type `II` primes, mixed types, random curves), kept if the isogeny class is trivial (so optimal, and
`E[l]` irreducible for every `l`) and not CM; modular degrees by `ellmoddegree`. None has image 3Ns; Conjecture
conj:euler and both corollary forms hold for all `893`; equality in (eq:rule) for `52.5%` of the `828` with a positive
bound at `l = 3` (that is `435` curves; `435/828 = 52.54%`). This is the blind test of the rule (A6.1).
Expansion: why a trivial isogeny class gives optimality and irreducibility (Chapter `ch:ellcurves`: a reducible
`E[l]` gives a rational `l`-isogeny).

**A6.10 `eisenstein`** (data and conjecture (Section sec:eis); *stated*, with the bound `D <= 2` *proved here* from the
first bound (A1.13); paper use: Section sec:eis, Conjecture conj:eis, Open question 4).
Content. Working set, `l = 3`: `75,430` optimal non-CM curves with a rational `3`-isogeny, `67,845` with a positive bound
in (eq:main), `2,777` with positive deficit `D`, `D = 2` for `22` (`17` with `E[3] = Z/3 + mu_3`, image 3Cs.1.1, all rank
`0`, torsion `Z/3`; `5` with a point of order `9`). No curve without rational `3`-torsion has a deficit; with a
rational `3`-torsion point and Borel image, `D <= 1`. None of the `2,065` curves with `N <= 400000` and image 3Cs.1.1 has a
point of order `9`; the `18` optimal curves with a point of order `9` have image 3B.1.1. Torsion bound attained with
`D > 0` in `2,773` cases. `l = 5, 7`: deficits at most `1`, only with rational `l`-torsion (`192` and `18` cases). Against
(eq:twist) the deficit is not controlled by torsion (`1,148`, `189`, `39` curves at `l = 3`; `141` at `l = 5`), so the
conjecture is stated for (eq:main) only.
**Commentary (new, Section 9 point N3).** "We have not proved that the two cannot coexist": they cannot, for non-CM
curves (A1.13). The book replaces the sentence by the proof and keeps only the first bound of Conjecture conj:eis as
conjectural.
**Commentary (important_notes.md point 3).** Labels 3Cs.1.1 and 3B.1.1: consistent with ecdata (A1.13); to be checked
against Sutherland16.
Expansion for the book: what "Eisenstein" means (reducible `rho bar`, maximal ideal containing `T_p - 1 - p`), why the
methods of Section 4 fail (Ihara's lemma, multiplicity one, Lemma lem:hecke all need `rho bar` irreducible), the role
of rational torsion and of the cuspidal subgroup (Mazur77), and an example from the small range: 539a1 (image 3B,
type `I_2^*` at `7`) has `e_3 = 1` but `v_3(deg) = v_3(320) = 0`, while (eq:main) holds (`v_3(4) + v_3(1) = 0`): in the
Eisenstein case the additive Euler terms do not contribute reliably.

### A7. The paper's Section 7: the prime 2 (Section 21.18)

**A7.1 `prime-two`** (data and literature (Section sec:two); *stated; reference*: Watkins02 (conjecture `2^{rank} |
deg`), Dummigan06, CalegariEmerton09, Yazdani11, CaroPasten22, HatleyKundu, BKP; Chapter `ch:moddeg`; paper use:
Section sec:two, Open question 5).
Content. For working-set optimal curves without a rational `2`-isogeny and not CM: `v_2(deg varphi_E) >= sum_{q || N}
v_2(n_q) + #{q : type III, III^*, I_0^* or I_n^*}` with no exception on the three ranges (`964,432`, `325,510`, `313,741`
curves); counting `I_0^*` with weight `2 = v_2(#Phig_q)` fails (`123, 26, 20` exceptions). Isolated minima suggest
`III, III^*, I_n^*` contribute `3` each and `II, IV, I_0^*` `1` each, in line with Calegari-Emerton (odd modular degree
forces at most two odd bad primes and a rational `2`-torsion point or prime conductor). Not reconciled with the
literature or with Euler factors at `l = 2` (outside DFG04).
What the book says: `l = 2` is outside every theorem of the paper (`l` odd is used in Lemma lem:tamfactor, the
trace form, the real place, DFG04's `S_f`); this section is data plus pointers. The writer states Watkins's conjecture
precisely and Calegari-Emerton in the form given in their paper (check the statement against the source).

### A8. Open questions (Section 21.18)

**A8.1 `open-questions`** (list; *stated*; paper use: Open questions 1 to 5).
(1) Extend Theorem thm:main to `l | N`, identifying `w_3` with a local term at `l` (book: what replaces the Euler
factor at `l` is a condition on `rho|_{D_l}`; DFG04 needs `l` not dividing `N` for Fontaine-Laffaille). (2) Prove the
corrected identity of Remark rem:ns for 3Ns curves, i.e. `v(eta^Sigma) = length H^1_Sigma(Q, W)` without the
hypothesis on `Q(sqrt(-3))` in the dihedral case. (3) Compute `Tam_q(ad T)` at additive primes and the Selmer length,
to account for the excess curve by curve (book: for `I_n^*` primes Lemma lem:tamfactor already applies through the
twist (A4.12 Step 7); the open cases are the potentially good types). (4) Identify the Eisenstein deficit with an
invariant of the Eisenstein ideal (cuspidal subgroup, Mazur77). (5) Reconcile Section sec:two with the literature
on Watkins's conjecture and Euler factors at `l = 2`.
For each, the tour names the chapter where the relevant notions live (`ch:congruence`, `ch:blochkato`, `ch:moddeg`).

### A9. The appendix: reproducibility and the function `rule(E, l)` (Section 21.19)

**A9.1 `pari-rule`** (construction (the paper's `scripts/euler_rule.gp`); *explained line by line*; reference: PARI
manual (`ellglobalred`, `elllocalred`, `lfunsympow`, `lfuneuler`, `ellmoddegree`, `elldivpol`, `factor`); Chapters
`ch:reduction` (Kodaira codes), `ch:lfunctions` (`P_q`), `ch:computation`; paper use: the appendix).
Line by line (`rule(E, l, {iii = 0})`):
(1) `R = ellglobalred(E)`: `[N, [u,r,s,t], c, faN, L]`; `P = R[4][,1]` the bad primes (first column of the
factorisation of `N`); `K = R[5]` the list of `elllocalred` outputs `[f_p, kod, [u,r,s,t], c_p]`, so `K[i][2]` is the
Kodaira code at `P[i]`. (2) `S = lfunsympow(E, 2)`: the symmetric square `L`-function in the motivic normalisation
`L(Sym f, s)`, with `L_p(Sym f, s) = L_p(A_f, s - 1)`. `b` the bound, `j = E.j`. (3) Loop over bad `q`: `k` the code,
`vj = valuation(j, q)`. (4) If `q != l`: `F = 1/lfuneuler(S, q)` is `P_q(x)` (PARI's `lfuneuler` returns the Euler
factor as a rational function in `x = q^{-s}`, i.e. `1/P_q(x)`; the writer checks this convention in PARI 2.15); `r =
P_q(q^{-2}) = L_q(A_f, 1)^{-1}`; if `k >= 5` (type `I_n`, `n >= 1`) divide by the naive factor `1 - q^{-2}`, so `r = 1`
and `e = 0`; at additive `q` the naive factor is `1` (`a_q = 0`); `e = v_l(r)` unless the type is `III` or `III^*`
(`abs(k) == 3`) and `iii = 0`. This is Definition def:terms verbatim. (5) If `q == l`: no Euler term; for `l = 3`, `e =
w_3(E)`: `1` for codes `4` (`IV`), `2` (`II`), `-3` (`III^*`); `2` for `-4` (`IV^*`), `-2` (`II^*`); `0` otherwise (`III`,
`I_0^*`, and the potentially multiplicative codes, where `w_3 = 0`). For `l >= 5` nothing. (6) `t = v_l(-vj)` if `vj < 0`
(Tamagawa exponent at every bad `q`, including `q = l`), else `0`. (7) `b += e + t`. (8) After the loop, if `iii` and
`l = 3`, subtract `ns3(E)` (the correction `h_3(E)`, which is `1` exactly for image 3Ns by A4.11 and A5.1; for `l >= 5`
`h_l = 0`). (9) Return `[v_l(ellmoddegree(E)), b]`.
`ns3(E)`: factor `psi_3 = elldivpol(E, 3)` over `Q`; true iff there are exactly two irreducible factors and the first
has degree `2`, i.e. the pattern `2 + 2` (patterns `1 + 3`, `1 + 1 + 2` and `4` give false whatever the order PARI lists
factors in). By A5.1 and the check of A1.12, for non-CM curves with `E[3]` irreducible this is image 3Ns.
Reading the two modes: `rule(E, l)` is the "III-free" bound without correction (A6.2); `rule(E, l, 1)` is (eq:rule).
Points the book must make. (a) `ellmoddegree(E)` returns the modular degree of the given model divided by the square
of its Manin constant; for the optimal curve this is `deg varphi_E` (Manin constant `1`, checked in Cremona's range);
on a non-optimal curve the output is not the paper's quantity (the writer checks the PARI 2.15 manual entry and
whether the return value is an integer or a pair in that version). (b) `valuation(j, q)` of `j = 0` is `+oo`, so `t =
0`, as it should. (c) The test `abs(k) != 3` excludes both `III` (code `3`) and `III^*` (code `-3`) at `q != l`, but at
`q = l = 3` the `III^*` weight `w_3 = 1` is counted even when `iii = 0`; this matches "leaves the type `III` terms out"
because `w_3` is not an Euler term. (d) Worked runs (hand-simulated in B4): 121a1 gives `[1, 1]`; 726a1 gives `[2, 2]`
in both modes.

**A9.2 `kodaira-codes`** (convention; *stated*; reference: PARI manual (`elllocalred`), Chapter `ch:reduction`; paper
use: the appendix).
Table (PARI code: Kodaira symbol, `#Phig`, conductor exponent at `q >= 5`, `v_q(Delta_min)` at `q >= 5`):
`1`: `I_0` (good; never in `ellglobalred`'s bad list), `1`, `0`, `0`; `n + 4` (`n >= 1`): `I_n`, `n`, `1`, `n`; `2`: `II`,
`1`, `2`, `2`; `3`: `III`, `2`, `2`, `3`; `4`: `IV`, `3`, `2`, `4`; `-1`: `I_0^*`, `4`, `2`, `6`; `-(n + 4)` (`n >= 1`):
`I_n^*`, `4`, `2`, `n + 6`; `-2`: `II^*`, `1`, `2`, `10`; `-3`: `III^*`, `2`, `2`, `9`; `-4`: `IV^*`, `3`, `2`, `8`. (The
paper's list "`n + 4` for `I_n`, `-(n + 4)` for `I_n^*`" is for `n >= 1`; `I_0^*` is `-1` and `I_0` is `1`, which is
why `k >= 5` detects multiplicative reduction.)

**A9.3 `reproducibility`** (description; *stated*; paper use: the appendix's first and last paragraphs, the AI
statement).
Content: the repository and directory named in the paper (scripts for Euler factors, the rule, the boundary, the
Tamagawa test, the corollary forms; pinned data commit; rerun from a clean clone reproduced Table tab:counts; Lemma
lem:twist(ii) checked on `4,577` random pairs; Lemma lem:euler against `lfunsympow` on every curve). The book lists
these as the paper's claims and does not reproduce the scripts. The statement on the use of an AI system is part of
the paper; the tour mentions it in one sentence in Section 21.1 (it tells the reader how the paper was produced and
that every count can be rerun), with no further commentary.

## Part B. Devices of the tour (Sections 21.20 and 21.21)

### B1. Dependency diagram of the paper's results (Section 21.20)

To be drawn in the book as a `tikzcd` or a plain `tabular` diagram (no colour needed). Arrows mean "is used in the
proof of". Imported statements in square brackets.

```
[Kraus90]                                   => lem:IV
lem:IV                                      => thm:qual (a), (b); rem:types
[Tate curve; DDT 3.1(e)]                    => lem:tamagawa-exp
lem:tamagawa-exp                            => thm:qual (c); rem:ko(2); Section 1.5
[Silverman IV.9, Tate's algorithm]          => lem:twist (i), (ii)
[Atkin-Li 3.1]                              => lem:twist (iii)
lem:twist                                   => lem:euler; thm:qual (b), (c); thm:twist; thm:quant; thm:main Step 7
[Kraus90] + lem:twist                       => lem:euler => table of Section 1 => def:terms (values of e_l)
lem:euler                                   => thm:quant Step 3; prop:forms
[FPR94 I.4.2.2] + [cohomology, Ch. 16, 17]  => lem:tamfactor
lem:tamfactor                               => thm:main (eq:thm); rem:ko(1); sec:tam
[Ribet83 2.2; AU96 2.1]                     => lem:crit
lem:crit                                    => lem:old; lem:hecke; thm:twist; thm:quant Step 1
[Edixhoven92; Atkin-Lehner 3; DDT 3.1(e); Chebotarev; Brauer-Nesbitt] => lem:old
lem:old + [DDT 3.15 (Ribet90, Carayol89, Diamond95)] + [ARS12 2.2] => thm:qual
[DDT 4.17] = lem:ddt417                     => lem:hecke; thm:quant Step 2
[ARS12 2.2] + lem:crit + lem:ddt417         => lem:hecke
[Tilouine97; RibetStein 3.5; Shimura subgroup] => rem:free => equality in thm:main; thm:quant Step 4
[DFG04 Prop 1.4(c)] = thm:dfg14             => thm:main Step 2; thm:quant Step 3
[DFG04 Thm 3.7 = 0.2] = thm:dfg37           => thm:main Step 3
[DFG04 Thm 2.7] = thm:dfg27                 => hypotheses of lem:dfg21 (thm:main Step 4)
[DFG04 Lemma 2.1] = lem:dfg21               => thm:main Step 4; rem:ns
[FPR94; DFG04 2.15, (57)] = lem:fpr         => thm:main Step 5; rem:ns
[Clifford theory; Zywina15] => prop:ns <=> lem:h0 => thm:main Step 4; conj:euler (h_l); sec:anomaly
thm:main                                    => prop:forms => (eq:main), (eq:twist) under the hypothesis
thm:twist                                   => thm:quant => remark after thm:quant
lem:dfg21 + lem:fpr + lem:h0                => rem:ns => conj:euler (the correction term)
data (Section 6)                            => conj:euler (w_3, h_l); conj:eis; sec:two
```

The three "spines" the book highlights: (i) local: lem:tamagawa-exp, lem:IV, lem:twist, lem:euler, lem:tamfactor;
(ii) congruences: lem:crit, lem:old, optimal level, thm:qual; (iii) Selmer: lem:hecke, thm:dfg14, thm:dfg37,
thm:dfg27, lem:dfg21, lem:fpr, lem:h0, thm:main. Theorem thm:quant uses (i) and (ii), and from (iii) only thm:dfg14,
lem:ddt417 and lem:hecke (with rem:free for its middle term); it never uses thm:dfg37, which is why it needs no
hypothesis on `Q(sqrt(l*))`.

### B2. Hypothesis table (Section 21.20)

| hypothesis | where it is used | what fails without it |
|-|-|-|
| `l` odd | Lemma lem:tamfactor (`2` a unit in `(t - 1)M`); trace form `T^D = A(1)`; real place (`H^1(R, T^D) = 0`); `S_f` contains `2`; Lemma lem:h0 (complex conjugation gives absolute irreducibility, the determinant argument); optimal-level theorem (DDT 3.15 is for odd `l`); Lemma lem:old at `p = l` (Edixhoven's description) | everything in Sections 2 to 4 at `l = 2`; Section sec:two shows the `2`-adic pattern is different (types `III, III^*, I_n^*` weigh `3`, `I_0^*` weighs `1`, not `2`), and Watkins's conjecture brings in the rank |
| `l` not dividing `N` (and `l^2` not dividing `N`) | ARS12 Theorem 2.2 (`v_l(deg) = v_l(r_E)` needs only `l^2` not dividing `N`); DFG04 (`l` not in `S_f`; crystalline at `l`, Fontaine-Laffaille); Lemma lem:old at `p = l`; optimal-level theorem (`delta = 0`, weight 2, trivial nebentypus); Lemma lem:euler and Lemma lem:fpr (`q != l`); Remark rem:free (Serre weight `l` excluded) | 99A1 (`N = 9 * 11`): `deg = 4`, `r = 12`, so the passage from `r_E` to the degree fails at `l = 3`; at `q = l = 3` the Euler factor is replaced by the empirical weights `w_3` (Section sec:wild, Open question 1); no theorem covers `l | N`, though the data show (eq:rule) there |
| `rho bar` absolutely irreducible on `Gal(Qbar/Q(sqrt(l*)))` (`l` not in `S_f`) | DFG04 Theorem 3.7 (Taylor-Wiles patching) and Theorem 2.7 (vanishing of `H^1_f(Q, V^D)`); Lemma lem:h0 (`H^0(Q, W^D) = 0` at `l = 3`); optimal-level theorem at `l = 3` (Theorem thm:qual) | at `l = 3`, image 3Ns: (eq:thm) fails for `31%, 23%, 18%` of the 3Ns curves, by exactly one (726a1 is the worked example: bound `3`, `v_3(deg) = 2`); the correction `h_3(E) = 1` repairs it (Remark rem:ns). Theorem thm:quant does not need it (only `E[l]` irreducible) |
| `rho bar` irreducible (weaker; implied by the previous) | Theorem thm:dfg14 (Ihara's lemma); Lemma lem:hecke (non-Eisenstein `m`); Remark rem:free (multiplicity one); Lemma lem:old (Brauer-Nesbitt); Theorem thm:quant; Theorem thm:qual | Eisenstein case: 539a1 (image 3B, `I_2^*` at `7`): `e_3 = 1`, `v_3(deg) = 0`; 539d1 at `l = 5` (Borel image 5B.4.1, `I_0^*` at `7`): `e_5 = 1`, `v_5(deg) = 0`; only the weaker (eq:main) survives, with the torsion-controlled deficit of Conjecture conj:eis (20a1: `D = 1 = v_3(#E(Q)_tors)`) |
| `X_0(N)`-optimality | ARS12 (`deg varphi_E | r_E` is for the optimal curve); the definition of `deg varphi_E` | nothing at `l` when `E[l]` is irreducible: all curves of the class are linked by isogenies of degree prime to `l` (a cyclic isogeny of degree divisible by `l` would give a rational `l`-isogeny), and the minimal parametrisation of a non-optimal `E'` is `psi o varphi_E`, so `v_l(deg)` is a class invariant, as are `v_l(n_q)` and the `e_l`; the hypothesis matters for Conjecture conj:eis (rational `l`-isogenies), and for `ellmoddegree`, which computes the degree of the given model (A9.1) |
| multiplicity one (`H^1(X_0(N), Z_l)_m` free over `T_m`) | equality in (eq:identity) (Lemma lem:hecke via Lemma lem:ddt417); Step 4 of Theorem thm:quant (middle term `v_l(r_{E_S})`, at level `N_S`); remark (2) after Theorem thm:quant | only equalities: (eq:identity) becomes an inequality; Theorem thm:quant keeps `v_l(deg) >= sum e_l` but loses the term `v_l(r_{E_S})`; Remark rem:free asserts freeness under `l` not dividing `2N` and `rho bar` irreducible, so in the paper's range nothing is lost |

The book adds one sentence under the table: the hypotheses of Theorem thm:main are those of DFG04's Theorem 0.1 for
weight 2 and trivial character (`l` not in `S_f`), plus optimality, which is harmless at `l`.

### B3. Statements imported from the literature, with the paper's numbering (Section 21.20)

Rule for the book (PLAN.md 3): numbers are given as the paper cites them; the writer verifies each against the source
before printing it; any number that cannot be verified is replaced by a section reference and listed in the chapter's
Notes. "Verified" below means: checked for this outline; "as cited" means: taken from the paper, not checked.

| citation (as in the paper) | exact content used | where in the paper | book item | status |
|-|-|-|-|-|
| DFG04 Theorem 0.1 | Tamagawa number conjecture for the adjoint motive of `f` at `lambda` not in `S_f` | Section 1.2 (the hypothesis is theirs) | A1.4, B2 | as cited |
| DFG04 Theorem 0.2 | `H^1_Sigma(Q, W)` finite of length `v_lambda(eta^Sigma)` (the form of Theorem 3.7 used) | Section 4.2 | A4.7 | as cited |
| DFG04 Theorem 2.7 | `l` not in `S_f` implies `H^0(Q, V^D) = H^1_f(Q, V^D) = 0` | Theorem thm:dfg27 | A4.8 | as cited |
| DFG04 Theorem 3.7 | length of `H^1_Sigma(Q, W)` equals `v_lambda(eta^Sigma)`, `Sigma` finite, `l` not in `Sigma`, `M_{f,lambda}` minimally ramified outside `Sigma` | Theorem thm:dfg37 | A4.7 | as cited |
| DFG04 Proposition 1.4(c) | `eta^Sigma = eta^empty prod_{p in Sigma} L_p^{nv}(A_f, 1)^{-1}` for `rho bar_f` irreducible | Theorem thm:dfg14 | A4.2 | as cited |
| DFG04 Lemma 2.1 | the four-term exact sequence | Lemma lem:dfg21 | A4.9 | as cited |
| DFG04 Theorem 2.15 (proof) | recollection of the FPR local formula | Lemma lem:fpr | A4.10 | as cited |
| DFG04 (31) | definition of `S_f` | Section 4.2 | A4.6 | as cited; check whether it contains a condition on `l` relative to the weight (vacuous for `k = 2`, `l` odd) |
| DFG04 (57) | `Tam_p(T^D) = Tam_p(A)` | Lemma lem:fpr | A4.10 | as cited; multiplicative case verified here (Exercise 8) |
| DFG04 p. 708 | definition of `Tam_p` recalled | Section 1.2, Lemma lem:tamfactor | A1.3 | as cited |
| DFG04 Lemma 2.12; Sections 1.5.3, 1.6.1, 1.6.2, 1.7.2, 1.7.3, 1.8.2, 2.1; (13), (14) | Petersson norm and `L(Sym f, 2)`; lattices, pairing, conventions, Selmer groups | Sections 1, 1.1, 4.1, 4.2 | C2, A4.1, A4.6 | as cited |
| DDT Theorem 3.1(e) | local structure at a multiplicative prime: extension of unramified `eps` by `eps chi_l`, `eps(Frob_p) = a_p` | Lemma lem:old, Lemma lem:tamfactor | A2.7, A3.3 | as cited |
| DDT Theorem 3.15 | optimal level (Ribet, Carayol, Diamond) for odd `l`, with the `Q(sqrt(-3))` condition at `l = 3` | Section 3 | A3.4 | as cited |
| DDT Lemma 4.17 | numerical criterion; inequality half used | Lemma lem:ddt417 | A4.3 | as cited |
| DDT Section 4.4 | Hecke adjoints and the twisted pairing | Section 4.1 | A4.1 | as cited |
| FPR94 I.4.2.2 | `Tam_p(M) = Fitt((H^1(I_p, M)_tor)^{G_{Q_p}})` for `p != l` | Section 1.2, Lemma lem:tamfactor, Lemma lem:fpr | A1.3, A2.7, A4.10 | as cited |
| ARS12 Theorem 2.2 | `deg varphi_E | r_E`; equal `p`-valuations when `p^2` does not divide `N` | Sections 1, 3, Lemma lem:hecke | A3.1 | as cited (the writer checks 2.1 versus 2.2) |
| ARS12 Section 2; Section 3; Table 1 | abc connection; perfect pairing; 99A1 with `deg 4`, `r = 12` | Sections 1, 3 | A3.1, A3.7, B4 | `deg(99a1) = 4` verified (ecdata); `r = 12` as cited |
| Atkin-Li Theorem 3.1 | twist of a newform of level `M` with `q^2` not dividing `M` by `chi_q` is new of level `lcm(M, q^2)` | Lemma lem:twist(iii) | A2.4 | as cited |
| Atkin-Lehner Theorem 3 | `a_p = 0` for a newform with `p^2 | M` | Lemma lem:old | A3.3 | as cited |
| Ribet83 Theorem 2.2 | perfect pairing `S_2(Gamma_0(N); Z) x T -> Z` | Lemma lem:crit | A3.2 | as cited |
| AU96 Lemma 2.1 | the same pairing (Abbes-Ullmo) | Lemma lem:crit | A3.2 | as cited |
| Ribet-Stein Theorem 3.5 | multiplicity one for `J_1(N)[m]`, exception Serre weight `l` | Remark rem:free | A4.5 | as cited |
| Kim-Ota Theorem 1.1; Definition 2.12 | `ord eta_f(N) = ord eta_f(N^+, N^-) + sum t_f(q)`; the Tamagawa exponent | Remark rem:ko(2), Section 1.5 | A1.9, A4.13 | as cited |
| Kraus90 | order of the image of inertia `12/gcd(v_q(Delta), 12)` for `q >= 5` | Lemma lem:IV, Lemma lem:euler | A2.2, A2.5 | no number cited |
| Zywina15 | possible mod 3 images | Proposition prop:ns | A5.1 | by section (point 4); the book proves the list directly |
| Sutherland16 | image labels 3Ns, 3Cs.1.1, 3B.1.1, ... | Sections 1.3, sec:anomaly, sec:eis | A6.7, A6.10 | usage consistent with ecdata (checked); definitions to check (point 3) |
| Silverman ATAEC IV.9 | Tate's algorithm, component groups | Sections 1.4, 2 | A1.6, A2.4 | as cited |
| Edixhoven92 Section 2 | `rho bar|_{D_l}` determines `a_l mod lambda` (weight 2, level prime to `l`) | Lemma lem:old | A3.3 | as cited |
| Carayol89; Ribet90; Diamond95 | Serre conductor divides `N`; level lowering | Section 3 | A3.4 | as cited |
| Tilouine97 | `J_0(N)[m]` two-dimensional implies Gorenstein and freeness | Remark rem:free | A4.5 | as cited |
| Mazur77; Watkins02; Zagier85; Cremona97; Flach92; Hida81; CalegariEmerton09 and the `l = 2` literature | context | Sections 1, 6, 7, Open questions | A1.9, A7.1, A8.1 | as cited |

### B4. Worked verifications of the numerical examples (Section 21.21)

All values below were recomputed for this outline (Python: discriminants, `j`, Kodaira types at `q >= 5` from
`v_q(Delta)` and `v_q(j)` of the minimal model, at `q = 2, 3` with a hand-coded Tate algorithm; `a_p` by point
counting; modular degrees, images and torsion read from Cremona's ecdata files). Items marked PARI need `lfunsympow`
(Euler factor at a wild prime) or `ellmoddegree`/`mfinit` and were not recomputed.

1. **121a1** `[1,1,1,-30,-76]`. `Delta = -11^2`, `v_11(c_4) = 1`, `v_11(j) = 1`: type `II` at `11`. `chi_{-3}(11) = -1`
   (`11 = 2 mod 3`), so `e_3(E, 11) = v_3(11 + 1) = v_3(12) = 1`; `t_3 = 0`; bound `1`. `deg = 6` (ecdata), `v_3 = 1`:
   attained. `rule(E, 3)`: `P_11(X) = 1 + 11X` (from `L_11(A_f, s)^{-1} = 1 + 11^{-s}`), `P_11(11^{-2}) = 12/11`, `v_3 =
   1`: output `[1, 1]` (hand simulation; PARI for the actual run). Twist by `-11`: 121c2 `[1,1,0,-3632,82757]`, same `j
   = -24729001`, `Delta = -11^8`, type `IV^*`; 121c1 (optimal, `deg 6`) has type `IV`. Congruence `a_p(121a1) =
   chi_{-11}(p) a_p(11a1) mod 3`: verified for all `p < 1000`, `p != 3, 11` (including `p = 2`, where `chi_{-11}(2) =
   -1`). `f_{11a} tensor chi_{-11} = f_{121d}`: verified (`a_p(121d1) = chi_{-11}(p) a_p(11a1)`, `p < 1000`, `p != 2,
   11`). Mod 3 image of 121a1: surjective (ecdata lists only 11B.1.6).
2. **539c1** `[1,0,1,170,-3237]`. `Delta = -7^9 11^2`, `v_7(j) = -3`, `v_11(j) = -2`: types `I_3^*` at `7`, `I_2` at
   `11`. `e_3(E, 7) = v_3(48) = 1`, `t_3(E, 7) = v_3(3) = 1`, `t_3(E, 11) = v_3(2) = 0`; bound `2`; `deg = 288 = 2^5
   3^2`: attained. Twist by `-7`: class 77c (77c1 `[1,1,0,4,11]`, `Delta = -7^3 11^2`, types `I_3, I_2`, `deg 6`);
   `a_p(539c1) = chi_{-7}(p) a_p(77c1)` for all `p < 1000`, `p != 2, 7, 11`; congruence `a_p(539c1) = chi_{-7}(p)
   a_p(11a1) mod 3` for all `p < 1000`, `p != 3, 7, 11` (also at `p = 2`). Level raising `11 -> 77` at `7`: `a_7(11a1) =
   -2`, `(7 + 1)^2 - 4 = 60 = 0 mod 3`. Theorem thm:quant: `v_3(288) = 2 >= v_3(r_{77c}) + v_3(48) = 1 + 1`. Mod 3
   image surjective (ecdata: 2B only).
3. **980i1** `[0,0,0,1568,-72716]`. `Delta = -2^8 5 7^11`, `v_7(j) = -5`: type `I_5^*` at `7`; `I_1` at `5`; at `2`
   potentially good (`v_2(j) = 19`), type `IV^*` (Tate's algorithm, this outline). `deg = 2880 = 2^6 3^2 5`. At `l = 5`
   (`5 | N`: outside the theorems): `t_5(E, 7) = 1`, `e_5(E, 7) = v_5(48) = 0`, `e_5(E, 2) = v_5(P_2(1/4))` (PARI; `0` if
   `P_2 = 1 + 2X` as for every type `IV/IV^*` at `2` in the working set), bound `1 = v_5(2880)`. At `l = 3` (`3` does
   not divide `N`, image surjective): `e_3(E, 7) = v_3(48) = 1`, `e_3(E, 2) = 1` if `P_2 = 1 + 2X` (PARI), bound `2 =
   v_3(2880)`. Twist by `-7`: class 140b (140b1 `[0,0,0,32,212]`, `deg 60`), `a_p(980i1) = chi_{-7}(p) a_p(140b1)`,
   `p < 1000`, `p != 2, 5, 7`; congruence with `chi_{-7} tensor f_{20a}` mod 5 verified for `p < 1000`, `p != 2, 5, 7`;
   `a_7(20a1) = 2`, `64 - 4 = 60 = 0 mod 5`.
4. **726a1** `[1,1,0,-35,-51]`. `Delta = 2^6 3^3 11^3`, `v_2(j) = -6`, `v_3(j) = -3`, `v_11(c_4) = 1`: types `I_6` at `2`,
   `I_3` at `3`, `III` at `11`. Image 3Ns (ecdata); `psi_3 = (x^2 - x - 74)(3x^2 + 8x + 20)` (verified). `deg = 144 = 2^4
   3^2`. Hand simulation of `rule(E, 3)`: `q = 2`: code `10`, `e = 0` (multiplicative), `t = v_3(6) = 1`; `q = 3 = l`:
   code `7`, `w = 0`, `t = v_3(3) = 1`; `q = 11`: code `3`, skipped; `b = 2`: `[2, 2]`. `rule(E, 3, 1)`: `q = 11` adds
   `e_3 = v_3(11 - chi_{-4}(11)) = v_3(12) = 1` (`P_11 = 1 + 11X`), then `ns3 = 1` is subtracted: `b = 2`: `[2, 2]`, the
   cancellation the paper describes. Without the correction the bound is `3 > 2`: a violation by one, involving `p =
   2 = -1 mod 3` with `t_3(E, 2) = 1`, as Section sec:anomaly says. (`3 | N`, so Theorem thm:main does not apply to
   726a1 at `l = 3` in any case.)
5. **99A1** = Cremona 99a1 `[1,-1,1,-2,0]`. `N = 9 * 11`, `Delta = 3^3 11`, `v_3(j) = 9`: type `III` at `3` (Tate's
   algorithm), `I_1` at `11`. `deg = 4` (ecdata, also the paper); `r = 12` from ARS12 Table 1 (not recomputed: needs
   the integral Hecke module of `S_2(Gamma_0(99))`, e.g. PARI's `mfinit`). `v_3(deg) = 0 < 1 = v_3(r)`, allowed by
   ARS12 because `9 | N`. Consistency with Conjecture conj:euler at `l = 3` (mod 3 image surjective): `w_3 = 0` for type
   `III` at `3`, `t_3(E, 11) = 0`: bound `0`, no violation.
6. Extra examples used in the book (all verified the same way): **121d1** `[0,-1,1,-40,-221]` (`I_1^*` at `11`,
   `deg 24`): `e_3 = v_3(120) = 1 = v_3(24)`; with 11a1 shows that `e_l` is not twist invariant (A1.1). **539d1**
   `[0,1,1,-16,-66]` (twist of 11a by `-7`, same `j` as 11a3, `Delta = 7^6 11`, type `I_0^*` at `7`, `deg 72 = 2^3 3^2`):
   `e_3 = v_3(7 - 1) + v_3(64 - a_7(11a1)^2) = 1 + 1 = 2 = v_3(72)`; `e_5 = 0 + 1 = 1` but `v_5(72) = 0`, image 5B.4.1
   (Eisenstein at `5`). **539a1** `[0,-1,1,-4377,-110013]` (`I_2^*` at `7`, `I_1` at `11`, image 3B, `deg 320`): `e_3 = 1`,
   `v_3(deg) = 0`. **539b1** `[0,0,1,98,-86]` (`I_2^*` at `7`, `I_1` at `11`, surjective, `deg 192 = 2^6 3`): `e_3 = 1 =
   v_3(deg)`. **20a1** `[0,1,0,4,4]` (`IV^*` at `2`, `I_2` at `5`, torsion `Z/6`, image 3B.1.1, `deg 1`): deficit of
   (eq:main) at `l = 3` is `D = v_3(3) + v_3(2) - 0 = 1 = v_3(#E(Q)_tors)`, Conjecture conj:eis with equality.

Arithmetic checks of other claims (all consistent): `e_3` for type `IV` at `2` is `v_3(3/2) = 1`; the `I_0^*`
identity `(1 - alpha/(beta q))(1 - 1/q)(1 - beta/(alpha q)) = (q - 1)((q + 1)^2 - a^2)/q^3` (symbolic); the Tamagawa
formula of Lemma lem:tamfactor (exhaustive count, A4.10); sec:tam percentages; `364/1,170 = 31.1%`; `17 + 5 = 22`;
`435/828 = 52.5%`; `14,182/44,672 = 31.7%`.

## Part C. Where each point of important_notes.md is handled (Section 21.22)

The chapter has a short Section 21.22 "Corrections to the paper used in this book", a table with one line per point:
paper location, the problem in one sentence, the book's statement, the item. The line-up items carrying the
Commentary are:

| point | paper location | handled at |
|-|-|-|
| 1 | proof of Proposition prop:ns ("non-abelian and faithful") | A5.1 (also flagged at A1.12) |
| 2 | `N_s(F_3)` not maximal (context of Proposition prop:ns) | A5.1, A1.12 |
| 3 | Sutherland labels 3Ns, 3Cs.1.1, 3B.1.1 | A1.13, A6.7, A6.10 (ecdata consistency check recorded) |
| 4 | citations by section (Zywina15, Dickson) | A5.1, B3 |
| 5 | Lemma lem:h0 finiteness argument; `h_l(E) <= 1` | A4.11 (proof), A6.7 (Section sec:anomaly), A1.5 |
| 6 | Section 1.3: `chi_{l*}` versus `chi bar_l` in the criterion for `h_l(E) > 0` | A1.5 |
| 7 | Lemma lem:tamfactor: "image of `kappa` in `H^1(G/I, Z_l(1)^I)`" | A2.7 step (7) |
| 8 | Lemma lem:tamagawa-exp: notation `u`, "up to units" | A2.1 |
| 9 | Proposition prop:ns: "without CM" unused | A5.1, A1.12 |
| 10 | Lemma lem:old and Lemma lem:h0: "irreducible" should be "absolutely irreducible" | A3.3, A4.11 |
| 11 | geometric versus arithmetic Frobenius | C2 (convention), A2.5 (type `I_n`), A2.7 (Lemma lem:tamfactor), A4.9 (paragraph after Lemma lem:dfg21), A4.10 |
| 12 | Lemma lem:euler: `End_{I_q}(V)` | A2.5 |
| 13 | Lemma lem:IV: `Z_3[sigma]/(sigma^2 + sigma + 1)` | A2.2 |
| 14 | Lemma lem:h0: CM alternative impossible when `l` does not divide `N` | A4.11 |

The new points of this outline (Section 9, N1 to N12) are added to the same table in the book, marked "found
while writing this book".

## 4. Section-by-section plan with target line counts

Lines of LaTeX. PLAN.md 7.3 allows Chapter 21 up to 2,800 lines; the total below (card excluded) is 2,770. The card
("Core results at a glance") lists every A-item with its rigour tag; for this chapter the card is long (about 60
entries) and is excluded from the count as for every chapter.

| section | title | contents (items) | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | every A-item, stated as above, tagged, with `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | one paragraph: "all of it"; how to read the tour alongside the paper; the tour's labels are the paper's labels | 30 |
| 21.1 | Conventions and how to read the tour | C1, C2 (Frobenius), C3 (duals); how Commentaries are marked; one sentence on the AI statement (A9.3) | 90 |
| 21.2 | The local terms | A1.1 (with the corrected twist invariance), A1.2, A1.3 | 110 |
| 21.3 | The theorem, the conjecture, the component-group forms | A1.4 (reading of hypotheses), A1.5, A1.6, A1.7, A1.8 (proof of prop:forms) | 150 |
| 21.4 | History and the statements without the hypothesis | A1.9, A1.10, A1.11, A1.12, A1.13 (statement; the proof that `D <= 2` is given in 21.17) | 110 |
| 21.5 | Tate curves and inertia | A2.1, A2.2, A2.3 | 110 |
| 21.6 | Twists and the omitted Euler factors | A2.4, A2.5, A2.6 | 160 |
| 21.7 | The Tamagawa factor at a multiplicative prime | A2.7, every step, with the worked check for `M = T` | 130 |
| 21.8 | The congruence criterion and oldforms | A3.1, A3.2, A3.3 | 130 |
| 21.9 | Level lowering and the proof of Theorem thm:qual | A3.4, A3.5, A3.6 (with the verified data), A3.7 | 150 |
| 21.10 | Congruence ideals, the numerical criterion, multiplicity one | A4.1, A4.2, A4.3, A4.4, A4.5 | 150 |
| 21.11 | The adjoint Selmer group and the proof of Theorem thm:main | A4.6 to A4.13 | 190 |
| 21.12 | Twist monotonicity | A4.14 (with the data paragraph and its correction) | 80 |
| 21.13 | The proof of Theorem thm:quant | A4.15, A4.16 | 150 |
| 21.14 | The boundary of the hypothesis | A5.1, A5.2 | 90 |
| 21.15 | The computations I: data, protocol, the rule, calibration | A6.1, A6.2, A6.3 | 110 |
| 21.16 | The computations II: Tamagawa factors, isolated terms, corollary forms | A6.4, A6.5, A6.6 | 90 |
| 21.17 | The computations III: 3Ns, wild primes, out of table, Eisenstein | A6.7, A6.8, A6.9, A6.10 | 120 |
| 21.18 | The prime 2 and the open questions | A7.1, A8.1 | 60 |
| 21.19 | The appendix: the function `rule(E, l)` | A9.1 (listing plus line-by-line table), A9.2, A9.3 | 100 |
| 21.20 | The map of the paper | B1 (diagram), B2 (hypothesis table), B3 (imported statements) | 150 |
| 21.21 | Worked verifications | B4 | 100 |
| 21.22 | Corrections to the paper used in this book | Part C table plus N1 to N12 | 60 |
| 21.23 | Exercises | Section 6 below (18 exercises) | 110 |
| 21.24 | Notes and references | which numbers were verified, which are as cited (B3), sources for the data | 40 |
| | **total** | | **2770** |

## 5. Coverage table: every label and section of the paper

| paper label or section | items |
|-|-|
| abstract | A1.4, A1.11, A6.1, A6.9 (and the corrections N10, N11) |
| Section 1 (introduction, Petersson norm, ARS, naive versus true) | C1, A1.1, A3.1, A1.9 |
| Section 1.1 "The local terms" (`V, T, rho, A_f, delta_p, L_p, L_p^{nv}`, PARI) | C1, C2, C3, A1.1 |
| def:terms | A1.1 |
| the table of Section 1 | A1.2, A2.5 |
| Section 1.2 "The theorem" (`Tam_p`, Bloch-Kato Selmer group) | A1.3, A1.4 |
| thm:main, eq:identity, eq:thm | A1.4, A4.12 |
| Section 1.3 "Beyond the hypotheses" | A1.5 |
| conj:euler, eq:rule | A1.5, A5.2, A6.2, A9.1 |
| Section 1.4 "Local component groups", eq:main, eq:twist | A1.6, A1.7 |
| prop:forms | A1.8, A6.6 |
| Section 1.5 "History ..." | A1.9 |
| thm:qual | A1.10, A3.5 |
| thm:quant | A1.11, A4.15 |
| prop:ns | A1.12, A5.1 |
| conj:eis | A1.13, A6.10 |
| sec:local | A2.1 to A2.7 |
| lem:tamagawa-exp | A2.1 |
| lem:IV | A2.2 |
| rem:types | A2.3 |
| lem:twist | A2.4 |
| lem:euler | A2.5 |
| rem:wild | A2.6, A6.8 |
| lem:tamfactor | A2.7 |
| sec:proof | A3.1 to A3.7 |
| lem:crit | A3.2 |
| lem:old | A3.3 |
| optimal-level paragraph of Section 3 | A3.4 |
| cases (a), (b), (c) | A3.5 |
| the example (121a1, 539c1, 980i1) | A3.6, B4 |
| the remark after the example (`l | N`, 99A1) | A3.7, B4 |
| sec:quant | A4.1 to A4.16 |
| sec:dfg | A4.1 |
| thm:dfg14 | A4.2 |
| lem:ddt417 | A4.3 |
| lem:hecke | A4.4 |
| rem:free | A4.5 |
| Section 4.2 "The theorem of Diamond, Flach and Guo" (set-up, `S_f`) | A4.6 |
| thm:dfg37 | A4.7 |
| thm:dfg27 | A4.8 |
| lem:dfg21 and the paragraph after it | A4.9 |
| lem:fpr | A4.10 |
| lem:h0 | A4.11 |
| Section 4.3 "Proof of Theorem thm:main" | A4.12 |
| rem:ko | A4.13 |
| sec:twisting, thm:twist and the data paragraph after it | A4.14 |
| proof of thm:quant (Steps 1 to 4) | A4.15 |
| the remark after the proof of thm:quant | A4.16 |
| sec:boundary (proof of prop:ns) | A5.1 |
| rem:ns | A5.2 |
| sec:data, Section 6.1 "Data and protocol" | A6.1 |
| Section 6.2 "The rule on whole ranges", tab:uniform | A6.2 |
| sec:sharp | A6.3 |
| sec:tam | A6.4 |
| sec:iso, tab:iso | A6.5 |
| sec:forms, tab:counts | A6.6 |
| sec:anomaly, tab:ns | A6.7 |
| sec:wild, tab:isolated | A6.8 |
| sec:oot, tab:oot | A6.9 |
| sec:eis | A6.10 |
| sec:two | A7.1 |
| Open questions 1 to 5 | A8.1 |
| appendix "Reproducibility", `rule`, `ns3`, Kodaira codes | A9.1, A9.2, A9.3 |
| statement on the use of an AI system | A9.3 (one sentence in 21.1) |
| PLAN.md extras: dependency diagram; hypothesis table; imported statements; worked verifications | B1; B2; B3; B4 |
| important_notes.md points 1 to 14 | Part C |

## 6. Exercises (Section 21.23)

Graded from routine to harder; most are "check the paper's claim that ...". Data for the curves are in B4; point
counting by hand or with a short program is allowed (the book says which).

1. Check the paper's claim that 121a1 `= [1,1,1,-30,-76]` has type `II` at `11` and `e_3(E, 11) = 1`: compute
   `Delta`, `c_4`, `j`, and `11 - chi_{-3}(11)`; compare with `deg varphi_E = 6`.
2. Check that the twist of 121a1 by `-11` has the same `j` and `v_11(Delta) = 8`, hence type `IV^*` (Lemma
   lem:twist(ii)); explain why the optimal curve 121c1 of the twisted class has type `IV` instead.
3. Check the paper's claim that `a_p(121a1) = chi_{-11}(p) a_p(11a1) mod 3` for the primes `p < 30`, `p != 3, 11`, by
   counting points.
4. For 539c1, check the types `I_3^*` at `7` and `I_2` at `11`, the bound `e_3 + t_3 = 2`, and its attainment
   (`deg = 288`). Identify the twist by `-7` (class 77c, `deg 77c1 = 6`) and check Theorem thm:quant with equality.
5. Check the paper's claim after Theorem thm:twist that strict inequality `v_l(deg varphi_E) > v_l(deg varphi_{E_q})`
   occurs "only in case (b)" against the pairs 539c1/77c1, 980i1/140b1 and 121d1/11a1 at `l = 3`. Which case are
   they in? Deduce the corrected statement from Theorem thm:quant.
6. Show that `e_l(E, q)` is not invariant under quadratic twist by comparing 11a1 and 121d1 at `q = 11`, and 11a1 and
   539d1 at `q = 7`. Prove the corrected invariance statement of A1.1.
7. For 539d1 (type `I_0^*` at `7`, twist of 11a by `-7`) compute `e_3(E, 7)` and `e_5(E, 7)` from `a_7(11a1) = -2`,
   compare with `deg = 72`, and explain the behaviour at `l = 5` (which hypothesis of Theorem thm:quant fails?). Do the
   same for 539a1 at `l = 3`.
8. Lemma lem:tamfactor in coordinates: for `l = 3`, `n = 9`, `q = 19` and each class `c in Z/9`, count the
   Frobenius-fixed points of `(Z/9) e + (Z/9) h` under `e -> e`, `h -> q^{-1}(h - 2 c eps e)` and check the formula
   `v_l(n) + min(v_l(n), v_l(q - 1), v_l(c))`. Then twist the Frobenius action by `chi_l(Frob) = q` and show the number
   of fixed points is unchanged (the identity `Tam_q(A(1)) = Tam_q(A)` of Lemma lem:fpr in this case).
9. Check the paper's "as a check" at the end of Lemma lem:tamfactor: for `M = T`, `Tam_q(T)` is the `l`-part of `c_q(E)`
   in the split and in the nonsplit case.
10. Check the identity `(1 - alpha/(beta q))(1 - 1/q)(1 - beta/(alpha q)) = (q - 1)((q + 1)^2 - a^2)/q^3` (`alpha beta =
    q`, `alpha + beta = a`), and the value `e_3 = v_3(1 + 2/4) = 1` for `P_2(X) = 1 + 2X` (Remark rem:wild).
11. Prove the sharp form of Lemma lem:h0: if `rho mod l^k = (rho tensor chi_l) mod l^k` then `chi_l^2 = 1 mod l^k` on
    `G_Q`; deduce `h_l(E) = 0` for `l >= 5` and `h_3(E) <= 1`. Where does the paper's own argument go wrong?
12. Check the table of `w_l(E, q) = max(v_l(#Phig_q(E)), v_l(#Phig_q(E^{(q)})))` for all Kodaira types at `q >= 5`, and
    the proof of Proposition prop:forms case by case.
13. Prove that a non-CM elliptic curve over `Q` cannot have both `E[3] = Z/3 + mu_3` and a rational point of order
    `9` (construct a rational cyclic `27`-isogeny and use the rational points of `X_0(27)`). Deduce that `D <= 2` in
    Conjecture conj:eis follows from its first bound.
14. For 726a1 `= [1,1,0,-35,-51]`: determine the Kodaira types at `2, 3, 11`, factor `psi_3`, and simulate `rule(E,
    3)` and `rule(E, 3, 1)` by hand (with `P_11(X) = 1 + 11X`), recovering the paper's `[2, 2]`. Show that (eq:thm)
    without correction would fail by one, and identify the prime `p = -1 mod 3` with `t_3(E, p) >= 1`.
15. Lemma lem:ddt417: show that for `T = O[epsilon]/(epsilon^2)` acting on `L = O` by `epsilon -> 0` one has `wp cap I != 0`;
    prove in general that `wp cap I != 0` forces `eta = 0`.
16. Check that the pairing `<x, w_N y>` on `H^1(X_0(N), Z)` is alternating and that every `T_n` and `U_p` is
    self-adjoint for it, given that `w_N T w_N` is the cup-product adjoint of `T`. Show that the Gram determinant of
    a rank-two alternating form is the square of a generator of its ideal of values.
17. Check the arithmetic of the calibration (Section sec:sharp): show that the bound-zero proportion `53.2%` alone
    predicts at least `461,000` violations among `867,578` bounded curves, and explain what further information is
    needed to reach the paper's `605,000`.
18. 99A1: check `N = 9 * 11` and the type `III` at `3`; explain why `deg = 4`, `r = 12` does not contradict ARS12, and
    why Conjecture conj:euler at `l = 3` is not violated (`w_3 = 0`).

## 7. Notes for the writer

W1. Corrections made in this session to the first-session text (A0 to A4.10): A1.1 twist invariance of `e_l`
(false as stated, new N1); A1.5 `chi_{l*}` replaced by `chi bar_l` (point 6); A1.10 section number; A1.11 reading of
which parts need multiplicity one (N10); A1.12 Commentary pointer and data check; A1.13 the bound `D <= 2` is
provable (N3); A2.1 notation `q_E` (point 8); A2.2 `Z_3[X]/(X^2 + X + 1)` and a cleaned unipotence argument (point 13);
A2.3 complete statement (N8); A2.5 geometric Frobenius (point 11), the ring `End_{I_q}` (point 12), a garbled
sentence about `sp(2)` replaced; A2.7 step (7) rewritten (point 7) and the arithmetic Frobenius named (point 11);
A3.3 absolute irreducibility (point 10); A3.5 the `h != f` step (N6), the remark on Atkin-Li in case (b), the reason
`I_0^*` is not in Theorem thm:qual; A3.6 data verified, 121c2 versus 121c1, 980i1 outside the hypotheses (N7);
A4.1 homothety (N12) and why the pairing is alternating; A4.3 steps (0), (1), (6) (N5); A4.9 proof idea and the
geometric Frobenius; A4.10 replaced (the old sketch of the exact sequence was imprecise; the first identity is now
proved); A4.11 replaced (the old text reproduced the paper's faulty finiteness argument, point 5). The horizontal
rule (three hyphens) after the convention paragraph was removed (typography).
W2. Chapter numbers in the first-session items ("Chapter 7 card" and so on) are to be written as `\Cref{ch:slug}`:
1 `ch:groups`, 2 `ch:rings`, 3 `ch:modules`, 4 `ch:reps`, 5 `ch:galois`, 6 `ch:ant`, 7 `ch:local`, 8 `ch:curves`, 9
`ch:ellcurves`, 10 `ch:reduction`, 11 `ch:galrep`, 12 `ch:modforms`, 13 `ch:hecke`, 14 `ch:moddeg`, 15 `ch:modgalrep`, 16
`ch:cohomology`, 17 `ch:galcoh`, 18 `ch:blochkato`, 19 `ch:lfunctions`, 20 `ch:congruence`, 22 `ch:computation`.
Environments. Use `theorem`, `lemma`, `proposition` for the paper's results with the paper's names in the optional
argument, e.g. `\begin{lemma}[the paper's Lemma lem:tamfactor]`; labels `lem:paper:tamfactor`, `thm:paper:main`, etc.
(prefix `paper`). Commentaries are `warning` environments titled "Commentary"; `paperlink` is not needed in this
chapter (everything is the paper). The paper's labels are quoted in text as "Lemma lem:tamfactor" (typewriter or
plain), never `\ref`'d (the paper is not part of the book).
W3. Restating versus re-proving. Where another chapter proves a paper lemma in full (Chapter 11: lem:IV, prop:ns,
lem:h0; Chapter 15: lem:crit, lem:old, thm:qual; Chapter 18: lem:tamfactor; Chapter 19: lem:euler; Chapter 20:
lem:ddt417, lem:hecke, thm:main, thm:twist, thm:quant), Chapter 21 still walks through the paper's proof line by
line (PLAN.md requires it) but may shorten routine verifications by pointing to the chapter (`\Cref{ch:...}`); it must
not contradict those chapters. In particular the corrected Lemma lem:h0 (A4.11) and the twist-invariance correction
(A1.1) must be the versions used everywhere; tell the Chapter 11, 19, 20 writers.
W4. Frobenius. State C2 once; in every proof say which Frobenius is meant. Never write `rho(Frob) = (eps q, c'; 0,
eps)` and `L_q = det(1 - Frob q^{-s})` in the same paragraph without the adjectives.
W5. Data. The paper's tables are not in the repository: describe them from their captions and the numbers in the
text only. Every number quoted from the paper is attributed to the paper. The book's own small-range checks (B4, and
the `N < 10,000` checks of A1.12, A1.13, A6.7) can be reported as such, with the method.
W6. PARI. The hand simulations of `rule` in B4 must be confirmed with PARI 2.15 before printing the outputs as
PARI outputs; in particular `lfuneuler`'s return convention (Euler factor `1/P_q(x)` as a rational function in `x`),
`ellglobalred`'s output format in 2.15, `ellmoddegree`'s return type (integer versus `[deg, error]` in some versions)
and the Manin-constant caveat. Things needing PARI (not installed for this outline): `P_2` for 980i1 (expected `1 +
2X`, type `IV^*` at `2`), the full `rule` outputs, `r(99a1) = 12`, any Euler factor at `q = 2, 3`.
W7. References. B3 lists every imported statement with its status. Verify before printing: ARS12 Theorem 2.2 (versus
2.1), DFG04 (31) (exact form of `S_f`; any weight condition is vacuous for `k = 2`), DFG04 (57), Kim-Ota Theorem 1.1 and
Definition 2.12 (and whether their `eta_f(N)` is the Hecke congruence ideal), Ribet-Stein Theorem 3.5, FPR94 I.4.2.2,
Edixhoven92 Section 2, Atkin-Li Theorem 3.1, Atkin-Lehner Theorem 3. Silverman ATAEC V.5 (twists of Tate curves) and
IV.9 (Tate's algorithm) are standard. For the level of a twist (`lcm(M, D^2)`) cite Atkin-Li or Shimura71 by section.
W8. Pitfalls. (a) `chi_q` is `chi_{q*}`, the character of `Q(sqrt(q*))`, conductor `q`; `chi_{-7}(2) = +1`,
`chi_{-11}(2) = -1` (Kronecker symbol at `2`). (b) `t_l` at `q = 2` uses `-v_2(j)`, not the index of the symbol `I_n^*`.
(c) Theorem thm:qual needs `l` not dividing `N`; 980i1 is outside it. (d) In Theorem thm:quant, `S` contains only
primes `q >= 5`. (e) Lemma lem:twist(ii)'s conductor statement at `q = 3` is right for the listed exchanges (`I_n <->
I_n^*`, `I_0 <-> I_0^*`: exponent `2` for the additive side, as quadratic characters of `Q_3` are tame) but not for
arbitrary additive curves at `3` (wild exponents up to `5`); say so in one line. (f) The `I_0 <-> I_0^*` exchange at
`q = 3` uses the twist by `3` or `-3`; they differ by an unramified twist, so both work. (g) Do not call `N_s(F_3)`
maximal. (h) "Optimal" is Cremona's label `1` only up to `400000` and for the classes where it was checked.
W9. Style. Short sentences; each section opens with a paragraph saying which part of the paper it covers. No dashes
(write "Diamond-Flach-Guo" with a plain hyphen, ranges "1 to 4"). ASCII only in the source.
W10. Length control. If the chapter runs long, shorten 21.15 to 21.17 (data) first, then the restatements of
statements already proved in Chapters 11, 15, 18 to 20; never shorten 21.11, 21.13, 21.20 or 21.22.

## 8. Dependencies and verification log

### 8.1 Dependencies on Chapters 1 to 20 and 22 (by label)

* `ch:groups`: subgroups of `GL_2(F_3)`, normalisers of Cartan subgroups, orbits on lines (A5.1); `N_s` not maximal.
* `ch:rings`: valuations of rationals, `l`-th powers in `F_q^x`, Kronecker symbols, `chi_{-3}, chi_{-4}, chi_q` (A1.1,
  A1.2, A2.7).
* `ch:modules`: Fitting ideals and lengths, saturation, Gram determinants, finite free algebras, idempotents, Pontryagin
  duality (A2.7, A4.3, A4.4, A4.9, A4.10, A4.15).
* `ch:reps`: absolute irreducibility, Schur, Brauer-Nesbitt, Clifford theory for index two, induction and Frobenius
  reciprocity, `ad` and the trace form (A3.3, A4.11, A5.1, C3).
* `ch:galois`: Chebotarev, Kummer theory, `Q(sqrt(l*))`, quartics on lines (A2.1, A2.7, A3.3, A5.1).
* `ch:ant`: `Z_3[zeta_3]`, `Z_l tensor Z[zeta_3]`, Frobenius and inertia, geometric versus arithmetic (A2.2, A2.5, C2).
* `ch:local`: tame inertia, `Frob t Frob^{-1} = t^q`, Kummer theory over `Q_q^ur`, Steinberg twists (A2.1, A2.5, A2.7).
* `ch:curves`: `H^1(X_0(N), Z)`, cup product, correspondences and adjoints (A4.1).
* `ch:ellcurves`: Weierstrass invariants, twists, division polynomials, CM, isogenies (A2.4, A5.1, A1.13, B2).
* `ch:reduction`: Tate's algorithm, Kodaira types, component groups, Tate curves, Kraus, PARI codes (A1.6, A2.1 to A2.4,
  A9.2).
* `ch:galrep`: `rho_{E,l}`, local structure at bad primes, images mod 3, Lemma lem:IV, Proposition prop:ns, Lemma lem:h0
  (A2.2, A2.3, A4.11, A5.1).
* `ch:modforms`: `S_2(Gamma_0(N))`, Petersson product, Atkin-Lehner involutions (A3.1, A4.1).
* `ch:hecke`: Hecke algebra, newforms, strong multiplicity one, oldforms and `U_p`, depleted forms, Atkin-Li, the
  perfect pairing, twisting (A3.2, A3.3, A4.14, A4.15).
* `ch:moddeg`: optimal curves, modular degree, congruence number, ARS, multiplicity one, Gorenstein, Eisenstein ideal,
  Watkins, Calegari-Emerton (A3.1, A4.4, A4.5, A6.10, A7.1).
* `ch:modgalrep`: Galois representations of newforms, local-global compatibility, level lowering (DDT 3.15),
  Edixhoven's description at `l`, Lemma lem:crit, Lemma lem:old, Theorem thm:qual (A3.3 to A3.6).
* `ch:cohomology`: inflation-restriction, procyclic cohomology, conjugation action of `G/I` (A2.7, A4.10).
* `ch:galcoh`: Kummer classes, unramified cohomology, local duality, comparison of Selmer structures (A2.7, A4.9).
* `ch:blochkato`: Bloch-Kato Selmer groups, `H^1_Sigma`, `Tam_p`, DFG04 Theorems 0.1, 0.2, 2.7, Lemma 2.1, FPR (A1.3,
  A4.6 to A4.10, A5.2).
* `ch:lfunctions`: true and naive local factors, `P_q`, `lfunsympow` normalisation, Lemma lem:euler (A1.1, A1.2, A2.5,
  A2.6).
* `ch:congruence`: DFG lattices and ideals, Theorem thm:dfg14, Lemma lem:ddt417, Lemma lem:hecke, Theorem thm:main
  assembly, Theorem thm:twist, Theorem thm:quant, Kim-Ota (A4.1 to A4.16).
* `ch:computation` (Chapter 22, which comes after this one): PARI usage, ecdata, the statistical protocol, `rule(E, l)`
  in practice (A6, A9). Chapter 21 explains what each statement means and tests; Chapter 22 explains how to run it.
  Forward references to Chapter 22 are by `\Cref{ch:computation}` only.

### 8.2 Verification log (computations for this outline)

Python 3 with sympy, scripts in `/tmp/ch21/py`; Cremona's ecdata files `allcurves`, `alldegphi`, `galrep` for `N <
10,000`, downloaded for this purpose (used as data only).
* Weierstrass invariants, `Delta`, `c_4`, `j` and their valuations for 11a1, 20a1, 121a1, 121c1, 121c2, 121d1, 539a1,
  539b1, 539c1, 539d1, 77a1, 77b1, 77c1, 980i1, 140a1, 140b1, 726a1, 99a1 (values in B4).
* Kodaira types: at `q >= 5` from `v_q(Delta)` and `v_q(j)` of the (minimal) Cremona model; at `q = 2, 3` with a
  hand-coded Tate algorithm (it reproduces the known types of 121a1, 121c2, 121d1, 539c1, 539d1, 726a1); new values: 99a1
  type `III` at `3`, 980i1 and 20a1 type `IV^*` at `2`.
* `a_p` by point counting for `p < 1000`; congruences of the paper's example (all hold, also at `p = 2` where
  included); exact twist relations 121a1/121c1, 11a1/121d1, 539c1/77c1, 980i1/140b1; `a_7(11a1) = -2`, `a_7(20a1) = 2`.
* Modular degrees from `alldegphi`: 11a1 `1`, 20a1 `1`, 77c1 `6`, 99a1 `4`, 121a1 `6`, 121c1 `6`, 121d1 `24`, 140b1 `60`, 539a1
  `320`, 539b1 `192`, 539c1 `288`, 539d1 `72`, 726a1 `144`, 980i1 `2880`.
* `psi_3` factorisations (sympy) for all `38,042` optimal curves with `N < 10,000`: pattern `2 + 2` exactly for the `90`
  curves labelled 3Ns among non-CM curves; irreducible for all 3Nn and surjective curves; reducible patterns for Borel and
  split Cartan images; the remaining non-irreducible cases are CM curves.
* Label consistency: 3B.1.1 and 3Cs.1.1 curves have a rational point of order `3`; 3B.1.2, 3B, 3Cs, 3Nn, 3Ns curves have
  none; no 3Cs.1.1 curve has a point of order `9` (`N < 10,000`).
* 3Ns curves `N < 10,000`: type `III/III^*` primes `q >= 5` and residues mod 12 (A6.7).
* Lemma lem:tamfactor: exhaustive fixed-point counts for `l = 3, 5`, `v_l(n) = 1, 2`, all primes `q < 200`, all `c` mod
  `l^2`, `eps = +-1`, with and without the twist by `Z_l(1)`: no mismatch with the formula.
* Symbolic checks: the `I_0^*` factor identity; `(t - 1)e, (t - 1)h, (t - 1)f` and `Ad(rho(Frob))` on `e, h` (A2.7).
* Arithmetic of the paper's percentages (A6.3, A6.4, A6.7, A6.9) and of the example valuations.
* Not verified (needs PARI or other software, or the sources): any `P_q` at `q = 2, 3`; `rule` outputs as PARI runs;
  `r(99a1) = 12`; all large-range counts of Section 6; the theorem numbers marked "as cited" in B3.

## 9. Points for important_notes.md

New points found while preparing this outline, not among the 14 already recorded. Each was checked as stated; the
numerical ones use Cremona's ecdata files and short Python computations (Section 8.2).

N1. **Definition def:terms, last sentence: "Both terms are invariant under quadratic twist."** Problem: false for
`e_l(E, q)` at the twisting prime when the twist changes multiplicative reduction into type `I_n^*` (or good into
`I_0^*`): 11a1 (`I_5` at `11`) has `e_3(11a1, 11) = 0`, its twist by `-11` (class 121d, type `I_n^*` at `11`, e.g.
`I_1^*` for 121d1) has `e_3 = v_3(120) = 1`; 11a1 twisted by `-7` is 539d1 (type `I_0^*` at `7`) with `e_3 = 2`. Theorem thm:quant rests precisely on
this change. Fix: "The term `t_l` is invariant under quadratic twist; so is `L_q(A_f, s)`, and `e_l(E, q)` is invariant
under twists unramified at `q` and under twists that keep the reduction at `q` potentially good of type `II, III,
IV` or a dual." Confidence: high.

N2. **Paragraph after Theorem thm:twist: "with equality in every pair of case (c) and strict inequality only in case
(b)".** Problem: contradicts Theorem thm:quant (and the paper's own example). For a single `I_n^*` prime `q >= 5` at
`l = 3` (`3` not dividing `N`, `E[3]` irreducible), Theorem thm:quant gives `v_3(deg varphi_E) >= v_3(deg
varphi_{E_q}) + v_3(q^2 - 1) > v_3(deg varphi_{E_q})`. Instances in case (a): 539c1 (`deg 288`) versus 77c1 (`deg 6`);
980i1 (`2880`) versus 140b1 (`60`); 121d1 (`24`) versus 11a1 (`1`); all with surjective mod 3 image. Fix: "strict
inequality only in cases (a) and (b), where the difference is at least the Euler term of Theorem thm:quant". (If the
sentence was meant to describe something else, it needs rewording; the count itself could not be checked.)
Confidence: high.

N3. **Conjecture conj:eis and Section sec:eis: "We have not proved that the two cannot coexist, so the bound `D <= 2`
is part of the conjecture."** Problem: the coexistence of `E[3] = Z/3 + mu_3` and a rational point `P` of order `9`
is impossible for non-CM `E`: with `phi: E -> E/mu_3` and its dual `phi^`, the subgroup `(phi^)^{-1}(<P>)` of `E/mu_3`
has order `27`, is rational, and does not contain `(E/mu_3)[3]` (its image under `phi^` would contain `mu_3`, which is
not in `<P>`), so it is cyclic; a rational cyclic `27`-isogeny forces `j = -2^15 3 5^3` (the only non-cuspidal
rational point of `X_0(27)`), a CM value. Fix: replace the sentence by this argument; then `D <= 2` (and `D <= 1` for `l
= 5, 7`, `D <= 0` for `l >= 11`) follows from the first bound and Mazur's torsion theorem. Confidence: high (the
`X_0(27)` fact is classical; the group theory was checked by hand).

N4. **Proof of Theorem thm:main, last sentences (the `I_n^*` primes in (eq:thm)).** Problem: the paper uses "the curve
`E_{p}` of Lemma lem:twist", which is defined only for odd `p`, while Theorem thm:main allows `2 | N`; at `p = 2` with
additive, potentially multiplicative reduction (`v_2(j) < 0`) the term `t_l(E, 2) = v_l(-v_2(j))` can be positive and is
not covered. The conclusion holds: the argument is local (over `Q_2`, `E` is a quadratic twist of a Tate curve, `ad T`
is unchanged, and the proof of Lemma lem:tamfactor works for `q = 2` since it needs only `q != l` and `l` odd). Fix: say
"at a prime `p` of additive, potentially multiplicative reduction (type `I_n^*` at odd `p`, or at `p = 2` with `v_2(j)
< 0`), `ad T|_{G_{Q_p}}` is that of a Tate curve with parameter of valuation `-v_p(j)`, and Lemma lem:tamfactor applies".
Also `E_{\{p\}}` is not the notation of Lemma lem:twist (`E^{(p)}`). Confidence: high (gap in the write-up, not in the
result).

N5. **Lemma lem:ddt417, proof, first sentence: "Since `L` is torsion-free and `wp cap I = 0`".** Problem: `wp cap I =
0` is not justified and fails in the stated generality (`T = O[epsilon]/(epsilon^2)` acting on `L = O` through `epsilon
-> 0`, `pi(epsilon) = 0`: `wp = I = O epsilon`). The lemma survives: if `wp cap I != 0` then the factor of `T tensor K`
through which `pi` factors is not a field and `eta = pi(I) = 0`, so there is nothing to prove; in the applications `T`
acts faithfully and `wp cap I = 0` also follows from `Delta != 0`. The equality clause uses `Ann_T(I) = wp`, which
holds in the same situation. Fix: add "If `eta = 0` there is nothing to prove; otherwise ..." with the two-line
argument. Confidence: high (minor).

N6. **Proof of Theorem thm:qual, cases (b) and (c): "`h != f`: otherwise `g = h tensor chi = f tensor chi = f'`".**
Problem: `h tensor chi = (g tensor chi) tensor chi` is the `q`-depleted form of `g`, not `g` (`a_q(g) = +-1` in case
(b), and `q` does not divide the level of `g` in case (c)). Fix: "otherwise `f' = f tensor chi` and `g` are newforms
with the same `a_p` for all `p` not dividing `qN`, so `f' = g` by strong multiplicity one, which is impossible as their
levels differ". Confidence: high (trivial fix).

N7. **The example after case (c) of Section 3, "(c) at `l = 5`: 980i1".** Problem: `5 | 980` (also `5 | 20` and `5 |
140`), so the example is outside the hypothesis `l` not dividing `N` of Theorem thm:qual; it illustrates the congruence,
not the theorem. Fix: add "(here `l | N`, so this illustrates the mechanism only; compare the remark below)".
Confidence: high. (All three congruences of the example were verified for `p < 1000`.)

N8. **Remark rem:types.** Problem (minor): it suggests that `E[3]^{I_q} = 0` and Serre conductor exponent `2` hold only
for `II, II^*, I_n^*`, and that only these types have a conductor-lowering twist. In fact `E[3]^{I_q} = 0` and exponent
`2` hold for every additive type at `q >= 5` except `IV, IV^*` (including `I_0^*, III, III^*`), and the twist of `I_0^*`
also lowers the exponent (to `0`). Fix: state it for all additive types other than `IV, IV^*`, and list `I_0^*` among the
types whose twist lowers the conductor (explaining separately why `I_0^*` is not in Theorem thm:qual: the lowered form
may be `f tensor chi_q` itself). Confidence: high.

N9. **Section sec:tam: "`v_l(c_q) >= k` means that the unit part of the Tate parameter at `q` is an `l^k`-th power".**
Problem (notation): `c_q` is the Tamagawa number in Section 1.4 and in `rule`'s data; here it is the class `c` of Lemma
lem:tamfactor. Fix: write `c(q)` or "the class `c` of Lemma lem:tamfactor at `q`". Confidence: high (cosmetic).

N10. **Abstract ("the terms of the types `I_0^*` and `I_n^*` still hold, by an elementary twisting argument") and
Theorem thm:quant, Step 4.** Problem (expository): only Step 1 is elementary; Steps 2 to 4 use DFG04 Proposition
1.4(c) (Ihara's lemma), Lemma lem:ddt417 and, for the middle term `v_l(r_{E_S})`, multiplicity one at level `N_S`
(Remark rem:free): without freeness Lemma lem:hecke gives `v_l(r_{E_S}) >= v(eta^empty_g)`, the wrong direction.
Worth saying: the outer inequality `v_l(deg varphi_E) >= sum_{q in S} e_l(E, q)` needs no multiplicity one, because
`eta^empty_g` is integral. Fix: "by a twisting argument combined with the formula of Diamond, Flach and Guo for the
variation of the congruence ideal", and add the remark on the outer inequality. Confidence: high.

N11. **Abstract: "the inequality holds with no exception ... for every optimal curve of conductor at most 500000" and
"violate it, by exactly one, in a third of the cases".** Problem (expository): the statement concerns curves with
`E[l]` irreducible and without CM, optimality is known only for `N <= 400000` and part of the classes above, and the
failure rate of 3Ns curves is `31%, 23%, 18%` on the three ranges (a third only on the working set). Fix: say "every
optimal non-CM curve with `E[l]` irreducible in the tables" and "in `18%` to `31%` of the cases". Confidence: medium
(the wording may be intended loosely).

N12. **Section 4.2: "the lattice `M_{f,lambda}` of DFG04 and `T_l E` are homothetic when `rho bar` is irreducible".**
Problem (minor): `M_{f,lambda}` sits in `H^1(X_0(N), Z_l)`, dual to the Tate module, so it is homothetic to the dual
`Hom(T_l E, Z_l) = T_l E(-1)` (determinants `chi_l^{-1}` versus `chi_l`), not to `T_l E` itself, unless DFG04 normalise
`M_{f,lambda}` as the dual; the conclusion (equal adjoints) is unaffected since `ad(T^*) = ad(T) = ad(T(-1))`. Fix:
"homothetic to `T_l E` or its dual, according to the normalisation; in either case their adjoints coincide".
Confidence: medium-high (depends on DFG04's normalisation of `M_{f,lambda}`, not rechecked).

N13. **Observation (not an error): `X_0(N)`-optimality is not needed for the `l`-adic statements when `E[l]` is
irreducible.** All curves of the isogeny class are joined by isogenies of degree prime to `l`, the minimal
parametrisation of a non-optimal curve is the optimal one followed by such an isogeny, and `v_l(n_q)`, `e_l`, `t_l` are
class invariants; so Theorem thm:main, Theorem thm:qual and Conjecture conj:euler hold for every curve of the class
once they hold for the optimal one. The paper could say so in one line (it matters only in the Eisenstein case).
Confidence: high.

N14. **Lemma lem:twist, proof of (ii): "The conductor exponents are the standard ones for `q` odd (tame)."** Problem
(minor): at `q = 3` additive reduction can be wildly ramified (exponents up to `5`). For the exchanges actually
listed at `q = 3` (`I_n <-> I_n^*`, `I_0 <-> I_0^*`) the exponent of the additive side is `2`, because quadratic
characters of `Q_3` are tamely ramified and the Tate module of a Tate curve or of a good curve is tame at `3`. Fix: "for
these types the reduction becomes semistable over a tamely ramified quadratic extension, so the exponent is `2`".
Confidence: high.

Also for the record (not new; consistent with the 14 points): the data checks of A1.12, A1.13, A6.7 found no
inconsistency with the paper's statements about 3Ns, 3Cs.1.1, 3B.1.1 and the type `III` primes of 3Ns curves for `N <
10,000`.
