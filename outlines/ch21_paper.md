# Chapter 21. Reading the paper: a guided tour (label `ch:paper`, file `chapters/ch21_paper.tex`)

Stage 1 line-up, third revision (14 October 2026). Target length: at most 2,800 lines of LaTeX (PLAN.md 7.3 allows this
for Chapter 21), card excluded; the section plan in Section 4 totals 2,795.

The chapter is a commentary on the paper in the paper's order. Every item below is either (A) a statement of the paper
restated precisely in the book's shared notation, (B) a convention the reader must fix to read the paper, or (C) a device
of the tour (dependency diagram, hypothesis table, list of imported statements, worked verifications). Rigour tags follow
PLAN.md 3: the paper's own lemmas are *proved here* with every compressed step expanded; the imported theorems are *stated;
reference* with the exact numbering; the long arguments reproduced from the paper (the assembly of Theorem thm:main, Steps 1
to 4 of Theorem thm:quant) are *proved here* because every ingredient is a card entry of an earlier chapter. Where an
earlier chapter proves a paper lemma in full, the tour still walks through the paper's proof but cites that chapter's item
for routine verifications (writer note W3).

Frobenius convention (fixed in item C2, binding Appendix B conventions B-C2 and B-C3). The book's `Frob_p` is ALWAYS the
arithmetic Frobenius: it acts on `mu_{l^k}` by `zeta -> zeta^p`, so `chi_l(Frob_p) = p`. The geometric Frobenius is
`Phi_p = Frob_p^{-1}`; because this chapter also uses the component groups `Phig_q` of the paper (B-C11), it writes the
geometric Frobenius at a named prime as `Frob_q^{-1}` (B-C2(b)) and never as `Phi_q`. (a) Group theory and cohomology use
`Frob`: the relation `Frob^{-1} t Frob = t^{q^{-1}}`, the conjugation action of `G/I` on `H^1(I, M)`, unramified cohomology
`H^1_ur = M^I/(Frob - 1)M^I`, the Tate matrices of Lemma lem:tamfactor. (b) `L`-factors use the geometric Frobenius:
`L_p(M, s) = det(1 - Frob_p^{-1} p^{-s} | M^{I_p})^{-1}` for `p != l`, the convention of DFG04 Section 1.7.2 (verified
against the published text: Chapter 20 outline, Part 7.3). The two are forced by the paper itself: at a Steinberg prime the
inertia-invariant line of `ad V_l E` carries the arithmetic eigenvalue `q` (computed in Lemma lem:tamfactor: `Ad(rho(Frob)) e
= q e`) and the paper's factor is `1 - q^{-1-s}`, which needs the geometric eigenvalue `q^{-1}`; and `L_p(A_f(1), 0) = L_p(A_f,
1)` (Lemma lem:fpr) holds because `Frob_p^{-1}` acts on `Z_l(1)` by `p^{-1}`. On `V_l E` the arithmetic Frobenius has the
eigenvalues `alpha, beta` (roots of `X^2 - a_p X + p`) and the geometric one has `alpha^{-1}, beta^{-1}`, a different set; on
`ad V` both have `alpha/beta, 1, beta/alpha` (B-C3). So the convention is invisible at good primes and on the lines where
Frobenius acts by `chi_{-3}(q), chi_{-4}(q) = +-1`, and visible exactly at multiplicative primes. (This is important_notes.md
point 11 with B1, B7, B9; DFG04 use the geometric Frobenius, Chapter 20 Part 7.3, confirming point 11. The book states the
convention once, in C2, and repeats it in a one-line Commentary at Lemma lem:euler, Lemma lem:tamfactor and the paragraph
after Lemma lem:dfg21.)

How the commentary is marked. Wherever the paper's text is wrong, imprecise or has a gap, the item carries a paragraph
**Commentary** (typeset as a `warning` environment titled "Commentary") with three parts: what the paper says; the correct
statement; how the book presents it. Every point 1 to 80 of important/important_notes.md about the paper is placed, in its
final state (with all addenda, corrections and settlements applied), at the item it concerns; Part C is the index. A point
that is a theorem the book proves elsewhere is cited by that chapter's item number. Points 15 to 28 were found by the first
version of this outline (its N1 to N14); the old labels are not used any more.

Status of this file. First written in two sessions (A0 to A4.10, then the rest); revised in this third session to apply
Appendix B (conventions B-C1 to B-C16 and the Chapter 21 entries F1, F2, T1, T2, D5, D6, X5, L6 of its Part 3), the
book-internal notes B1, B3, B7, B8, B9, B12, B13, B16, B18, B19, B21, B25, B26, B27, and points 29 to 80 with the settlements
of points 39 (confirmed via 56 and 73), 43 and 74. The list of changes is writer note W1.


## Part A. Core results, in teaching order

### A0. Conventions and standing notation (Section 21.1 of the chapter)

**C1 `conv-standing`** (convention; *stated*; reference: the paper, Section 1 and Section 1.1; DFG04 1.7.2; Appendix B,
B-C1, B-C10, B-C12, B-C13; paper use: everywhere).
Statement. Throughout, `E/Q` is an elliptic curve of conductor `N`, `X_0(N)`-optimal in its isogeny class, `varphi_E :
X_0(N) -> E` its modular parametrisation (curly `varphi` for maps of curves) and `deg varphi_E` its modular degree; `f = f_E in
S_2(Gamma_0(N))` is the newform with `a_p(f) = a_p(E)` for all `p`; `phi_f : T -> Z`, `T_n -> a_n(f)`, its eigencharacter
(upright `phi`); `l` is an odd prime; `V = V_l E`, `T = T_l E`, `rho = rho_{E,l} : G_Q -> Aut(T) = GL_2(Z_l)`, `rho bar = rho mod
l` on `E[l]`; `A = ad T` and `A_f = ad V` are the trace-zero adjoints (the macro `\ad` already contains the superscript `0`;
`A_f` is never an abelian variety: Shimura's quotient attached to `f` is `J_f`, B-C12); `delta_p = dim V^{I_p}` equals `2, 1, 0`
for good, multiplicative, additive reduction at `p != l` (at `p = l` the paper's formulas are not used, point 72); `v_l` is
the `l`-adic valuation with `v_l(l) = 1`, extended to `Q^x` and to ideals of `Z_l`, and for a class `c in Z/l^m`, `v_l(c) :=
min(v_l(c~), m)` (B-C10); `length` means `Z_l`-length. `q` denotes a bad prime (`q | N`), `p` any prime. The Hecke algebra `T`
is the full one: the subring of `End S_2(Gamma_0(N))` generated over `Z` by all `T_n`, `n >= 1`, including `U_p` for `p | N`.
`E^{(q)}` is the quadratic twist of `E` by `Q(sqrt(q*))`, `q* = (-1)^{(q-1)/2} q`; `E_S = E tensor chi_S`. Depletion is `f^Sigma`,
`f^{p}`, `f^S` (never a parenthesised superscript, which is reserved for twists, B-C13(e)). The Manin constant is `c_E`;
`c_q = #Phi_q(F_q)` is the Tamagawa number; the class of the unit part of the Tate parameter is `c(u)` (B-C14); a bare `c` is
not used in the book's own text. Characters (B-C6): `chi_l` with a letter subscript is the `l`-adic cyclotomic character and `chi bar_l` its
reduction; a numerical subscript always means the quadratic character `chi_d` of `Q(sqrt(d))` (`chi_{-3}`, `chi_{-4}`, `chi_{-7}`, `chi_{-11}`); the
cyclotomic character at `3` is `chi_3^cyc`; the quadratic character of conductor `q` is `chi_{q*}`, never `chi_q` (PLAN.md 7.5, decision D3).
**Commentary (important_notes.md point 32).** The paper uses `chi_q` for the quadratic character of conductor `q` and `chi_l` for the
cyclotomic character, so `chi_3` is ambiguous, and it names one character both `chi_11` and `chi_{-11}`. Notation only; the book follows
the rule just stated and writes `chi_{q*}` and `chi_{-11}`.

**C2 `conv-frobenius`** (convention; *stated*; reference: Appendix B, B-C2, B-C3, B-C7; DFG04 1.1.1 and 1.7.2 (verified,
Chapter 20 outline 7.3); Serre, Abelian l-adic representations, I.2; `\Cref{ch:local}` 4.3 and 5.4, `\Cref{ch:ant}` 3.7,
`\Cref{ch:lfunctions}` 7.4; paper use: Section 1.1, Definition def:terms, Lemma lem:euler, Lemma lem:tamfactor, the paragraph
after Lemma lem:dfg21, Lemma lem:fpr).
Statement. (a) `Frob_p` (arithmetic) is an element of a decomposition group `D_p = G_{Q_p}` inducing `x -> x^p` on the residue
field, well defined modulo `I_p` and up to conjugation; `chi_l(Frob_p) = p`; with `t` a topological generator of the pro-`l`
part of tame inertia, `Frob t Frob^{-1} = t^p`, equivalently `Frob^{-1} t Frob = t^{p^{-1}}` (exponent in `Z_l`;
`\Cref{ch:local}` 5.4). (b) The geometric Frobenius is `Phi_p = Frob_p^{-1}`; in this chapter it is written `Frob_p^{-1}`
(B-C2(b), because `Phig_q` denotes component groups). For a `G_{Q_p}`-representation `M` on a finite-dimensional `Q_l`-space,
`p != l`: `L_p(M, s) = det(1 - Frob_p^{-1} p^{-s} | M^{I_p})^{-1}`. On `V = V_l E` at a good prime `p`, the ARITHMETIC Frobenius
has characteristic polynomial `X^2 - a_p X + p`, eigenvalues `alpha, beta` (`alpha + beta = a_p`, `alpha beta = p`), and the
geometric one has `alpha^{-1} = beta/p`, `beta^{-1} = alpha/p`: not the same set. The geometric Frobenius has the eigenvalues
`alpha, beta` on the dual `V^vee = H^1(E_Qbar, Q_l) = V(-1)`. Hence `L_p(E, s) = (1 - a_p p^{-s} + p^{1-2s})^{-1} = L_p(V^vee, s)`,
while `L_p(V, s) = L_p(E, s + 1)` (B-C3(c)). On `A_f = ad V` at a good prime both Frobenii have the eigenvalues `alpha/beta, 1,
beta/alpha`, an inversion-stable set, so `L_p(A_f, s)^{-1} = (1 - (alpha/beta) p^{-s})(1 - p^{-s})(1 - (beta/alpha) p^{-s})`
in either convention; at a multiplicative prime the arithmetic Frobenius acts on `(ad V)^{I_q}` by `q` and the geometric one by
`q^{-1}`, and only the latter gives the paper's `1 - q^{-1-s}`. (c) `L(Sym f, s) = L(ad f, s - 1)`, so `L_p(Sym f, s) = L_p(A_f, s
- 1)`; `L_q(Sym f, s) = P_q(q^{-s})^{-1}` defines `P_q in Z[X]`, and `L_q(A_f, 1)^{-1} = P_q(q^{-2})`; PARI's `lfunsympow(E, 2)`
returns `L(Sym f, s)` in this normalisation at every prime, and `lfuneuler(S, q)` is `1/P_q(x)` as a rational function of `x =
q^{-s}` (verified in PARI 2.17.2: `lfuneuler(S, 11) = 1/(11*x + 1)` for 121a1, `\Cref{ch:computation}` R2). (d) `L_p(M(1), s) =
L_p(M, s + 1)`, so `L_p(A_f(1), 0) = L_p(A_f, 1)`.

**C3 `conv-duals`** (convention; *stated*; reference: Appendix B, B-C4, B-C5, B-C12(b); DFG04 Section 2.1 and (57);
`\Cref{ch:modules}` 8.1 to 8.3, `\Cref{ch:reps}` 7.6, 7.7, `\Cref{ch:blochkato}` 2.3, 2.4; paper use: Section 4.2, Lemma
lem:dfg21, Lemma lem:fpr, Lemma lem:h0).
Statement. One symbol for each kind of dual: `M^vee = Hom(M, Z_l)` (linear dual; for representations the contragredient),
`X^* = Hom_cont(X, Q_l/Z_l)` (Pontryagin dual; the paper's `*` in Lemma lem:dfg21), `M^D = Hom(M, Z_l(1)) = M^vee(1)` (Kummer
dual), `A^dagger` (adjoint of an operator for a pairing); a star after the name of a MAP is a pullback (`varphi_E^*`). `Z_l(1) =
T_l mu = lim mu_{l^k}`, with `Frob_p` acting by `p`; `M(1) = M tensor Z_l(1)`. For `A = ad T`: `W = A tensor Q_l/Z_l`, `T^D =
Hom(A, Z_l(1))`, `V^D = T^D tensor Q_l`, `W^D = V^D/T^D`. For `l` odd the trace form `(x, y) -> tr(xy)` on `ad T` is perfect and
`G_Q`-equivariant (`\Cref{ch:reps}` 7.6), so `T^D = A(1)` and `W^D = ad T(1) tensor Q_l/Z_l`, the module whose `H^0` defines
`h_l(E)`; `H^0(Q, W^D)[l] = H^0(Q, ad rho bar tensor chi bar_l)`. `ad` is insensitive to duals and twists: `ad(T^vee) = ad T =
ad(T(n)) = ad(T tensor chi)` (`\Cref{ch:reps}` 7.7), so `ad M_{f,lambda} = ad T_l E` although `M_{f,lambda} = T_l E(-1)` (A4.1).

### A1. The paper's abstract and Section 1: the local terms and the statements (Sections 21.2 to 21.4)

**A1.0 `abstract-and-introduction`** (reading guide (the abstract and the first two paragraphs of Section 1); *stated*,
with the corrected formulas *proved* in the chapters cited; reference: Zagier85, Watkins02, ARS12 Theorem 2.2, Hida81,
DFG04 Lemma 2.12 (verified, Chapter 20 outline 7.3), Flach92; `\Cref{ch:moddeg}` 7.3, 8.3, `\Cref{ch:lfunctions}` 8.2 to 8.4;
paper use: abstract, Section 1).
Content. The abstract states (eq:thm), describes `e_l` and `t_l`, names the inputs (DFG04, FPR94, ARS12, the Tamagawa factor
at a multiplicative prime), the identity (eq:identity), the twisting statements, the 3Ns boundary and the data. The
introduction recalls the Petersson-norm route to the degree (Zagier, Watkins: `deg varphi_E vol(Lambda_E) = 4 pi^2 c_E^2 <f, f>`
with `c_E^2` in the NUMERATOR and the unnormalised Petersson product, B-C8, B-C9, important_notes.md B10; `\Cref{ch:moddeg}`
7.3), the special value `L(Sym f, 2)` (DFG04 Lemma 2.12 gives `<f, f>` with the NAIVE value, `\Cref{ch:lfunctions}` 8.3), ARS
(`deg varphi_E | r_E`, equal `p`-valuations for `p^2` not dividing `N`), and the naive versus true adjoint `L`-function.
**Commentary (important_notes.md points 30 and 70).** The paper says the naive adjoint `L`-function is "the Euler product of
`sum a_n(f)^2 n^{-s}`". That is the Rankin series, which differs by a factor at every good prime: `sum a_n^2 n^{-s} =
zeta^{(N)}(s - 1) L^nv(Sym f, s)/zeta^{(N)}(2s - 2)` exactly, with no correction at the bad primes. Correct statement: the naive
function is `L^nv(Sym f, s) = zeta^{(N)}(2s - 2) sum a_{n^2} n^{-s}` (Shimura's series), or is defined by its local factors as
Section 1.1 does. The book quotes the paper's sentence, prints the identity, and cites `\Cref{ch:lfunctions}` 8.2 for the proof.
**Commentary (important_notes.md point 71, optional strengthening).** Combining `<f, f> = N L^nv(Sym f, 2)/(8 pi^3)` with
Zagier-Watkins gives `deg varphi_E = N L^nv(ad f, 1)/(2 pi vol(Lambda_E))` for optimal `E` (`c_E = 1` in Cremona's range);
writing `B_E` for the same expression with the true `L`-value, `v_l(deg varphi_E) = v_l(B_E) + sum_q e_l(E, q)` unconditionally,
and (eq:thm) is equivalent to `v_l(B_E) >= sum_q t_l(E, q)`. This makes the role of the omitted factors visible in one line.
The book states it as a remark with a pointer to `\Cref{ch:lfunctions}` 8.4 and its table 12.1 (the attribution of the
Petersson formula to DFG04 Lemma 2.12 is verified, Chapter 20 outline 7.3).
**Commentary (important_notes.md points 25, 65, 66; and 24, 39, 77 for the abstract, discussed at their items).** The
abstract (i) says the bound is an equality "when multiplicity one holds at level `N`": the book proves it is an equality
whenever `l` is not in `S_f` (A1.4); (ii) calls the Euler terms of types `I_0^*`, `I_n^*` "elementary": only Step 1 of the
twisting argument is (A1.11); (iii) says the Tamagawa factor formula "raises the bound by one whenever a Steinberg prime `q = 1
mod l` has a Tate parameter whose unit part is an `l`-th power": the condition `l | n_q` is missing, and the raise is `min(v_l(n),
v_l(q - 1), v_l(c(u)))`, "by at least one" (point 65; A2.7, A4.13); (iv) speaks of "the Bloch-Kato Selmer group of `ad V_l E`": it
is that of `ad T tensor Q_l/Z_l`, the `Q_l`-space version being `0` under the hypothesis (point 66; DFG04 Theorem 2.7); (v)
says the corrected inequality holds "for every optimal curve of conductor at most 500000" and that 3Ns curves fail "in a third
of the cases": the statement concerns non-CM curves with `E[l]` irreducible, optimality is known for every class only up to
`400000` (and for `359,009` classes beyond), and the failure rates are `31%, 23%, 18%` on the three ranges (point 25). The book
quotes the abstract once in Section 21.2 with these five corrections in a list.

**A1.1 `def-terms`** (definition; *stated* (it is the paper's Definition def:terms, with the corrections of points 15 and
53); reference: paper Definition def:terms; `\Cref{ch:lfunctions}` 9.1, 9.5, `\Cref{ch:ellcurves}` 10.7; paper use: Definition
def:terms, Theorem thm:main, Conjecture conj:euler, appendix).
Statement. For a bad prime `q != l`:
`e_l(E, q) = v_l( L_q(A_f, 1)^{-1} / L_q^nv(A_f, 1)^{-1} ) = v_l( P_q(q^{-2}) / (1 - a_q(E)^2 q^{-2}) )`,
where `L_q^nv(A_f, s) = L_q(A_f, s)` if `delta_q > 0` and `= 1` if `delta_q = 0`; and, for EVERY bad prime `q` (including `q = l`,
as (eq:rule) and `rule(E, l)` use it), `t_l(E, q) = v_l(-v_q(j_E))` if `v_q(j_E) < 0`, `= 0` otherwise.
Facts attached: `e_l(E, q) = 0` at a multiplicative prime (naive = true); at an additive prime `a_q(E) = 0`, so `e_l = v_l(P_q(q^{-2}))`;
`e_l(E, q)` is a finite nonnegative integer (`P_q(q^{-2})` is a nonzero element of `Z[1/q]`, `\Cref{ch:lfunctions}` 9.6);
`t_l(E, q) = v_l(n)` for type `I_n` at any `q` and for `I_n^*` at odd `q` (`v_q(j) = -n`); at `q = 2` a symbol `I_m^*` may have
`-v_2(j) != m`, or `v_2(j) >= 0` (potentially good), and then `t_l = 0` (`\Cref{ch:reduction}` 7.7, 9.4). Twist behaviour: `t_l(E,
q)` and the true factor `L_q(A_f, s)` are invariant under every quadratic twist (`j` and `ad V` are unchanged); `e_l(E, q)` is
invariant under twists unramified at `q`, and under twists ramified at `q` that keep the reduction potentially good of type
`II, III, IV` or a dual (`a_q = 0` on both sides); it is NOT invariant when the twist moves `q` between multiplicative and
`I_n^*`, or between good and `I_0^*`.
**Commentary (important_notes.md point 15, as corrected; B8).** The paper ends the definition "Both terms are invariant under
quadratic twist". False for `e_l` at the twisting prime: 11a1 has type `I_5` at `11` and `e_3(11a1, 11) = 0`; its twist by `-11`
is 121d2 (class 121d), of type `I_5^*` at `11`, with `e_3 = v_3(11^2 - 1) = 1` (the curve 121d1 is the twist of 11a3, type `I_1^*`,
same `e_3`); and 11a1 twisted by `-7` is 539d2, in the class 539d whose optimal curve 539d1 has type `I_0^*` at `7` and `e_3(539d1,
7) = v_3(6) + v_3(64 - 4) = 2`, where 11a1 has no term at `7`. The change of `e_l` under such twists is exactly what Theorem
thm:quant exploits. Correct statement: as in the Facts above. The book states the corrected invariance in the definition and
uses these pairs (curve-level identifications from `\Cref{ch:reduction}` 8.5).
**Commentary (important_notes.md point 53).** Definition def:terms is stated for `q != l`, but (eq:rule) sums `t_l(E, q)` over all
`q | N` and `rule(E, l)` adds `t` at `q = l` (726a1 at `q = l = 3`: `t_3(E, 3) = v_3(3) = 1`). The book defines `t_l(E, q)` for every bad
`q` by the same formula, as above.

**A1.2 `prop-table`** (proposition; *proved here* (it is Lemma lem:euler, proved in Section 21.6); reference: paper table of
Section 1; `\Cref{ch:lfunctions}` 9.3, 10.1, `\Cref{ch:rings}` 11.4, 11.5; paper use: the table, Lemma lem:euler, Theorem
thm:qual, Theorem thm:quant Step 3).
Statement. Let `q >= 5` be a bad prime, `q != l`, `chi_{-3}` and `chi_{-4}` the quadratic characters of `Q(sqrt(-3))` and `Q(i)`
(`chi_{-3}(q) = 1` iff `q = 1 mod 3`; `chi_{-4}(q) = 1` iff `q = 1 mod 4`), `E'` the twist of `E` by `Q(sqrt(q*))`, and for type `I_0^*`
let `alpha, beta` be the roots of `X^2 - a_q(E') X + q`. Then:
`I_n`: `L_q(A_f, s)^{-1} = 1 - q^{-1-s}`, `e_l = 0`;
`I_n^*`: `L_q(A_f, s)^{-1} = 1 - q^{-1-s}`, `e_l = v_l(q^2 - 1)`;
`II, II^*, IV, IV^*`: `L_q(A_f, s)^{-1} = 1 - chi_{-3}(q) q^{-s}`, `e_l = v_l(q - chi_{-3}(q))`;
`III, III^*`: `L_q(A_f, s)^{-1} = 1 - chi_{-4}(q) q^{-s}`, `e_l = v_l(q - chi_{-4}(q))`;
`I_0^*`: `L_q(A_f, s)^{-1} = (1 - (alpha/beta) q^{-s})(1 - q^{-s})(1 - (beta/alpha) q^{-s})`, `e_l = v_l(q - 1) + v_l((q + 1)^2 - a_q(E')^2)`.
Remark for the book (important_notes.md point 69): at EVERY bad `q`, including `2` and `3`, `P_q(X)` has one of four shapes:
`1 - X` (potentially multiplicative), the `I_0^*` cubic `(1 - qX)(1 - (a'^2 - 2q)X + q^2 X^2)` with `a'` the trace of a quadratic twist
with good reduction at `q`, `1 - c q X` with `c = +-1` (cyclic inertia of order `3, 4` or `6` with an invariant line), or `1`
(`\Cref{ch:lfunctions}` 10.1). The table is the case `q >= 5` of this classification. PARI agrees with the table on all `67,745`
pairs (optimal curve, bad `q >= 5`) below conductor `10,000` (`\Cref{ch:computation}` R4).

**A1.3 `def-tamagawa-factor`** (definition; *stated; reference*; reference: FPR94 I.4.2.2, DFG04 p. 708 (verified, Chapter 20
outline 7.3); `\Cref{ch:blochkato}` 7.1, 7.3, 9.3; paper use: Section 1.2, Theorem thm:main, Lemma lem:tamfactor, Lemma lem:fpr).
Statement. For a prime `p != l` and a `G_{Q_p}`-stable `Z_l`-lattice `M`, `Tam_p(M) = Fitt_{Z_l}( (H^1(I_p, M)_tor)^{G_{Q_p}} )`,
the Fitting ideal of the `G_{Q_p}`-invariants of the torsion of `H^1(I_p, M)` (`G_{Q_p}/I_p` acts by conjugation); it is an
ideal `l^v Z_l` and `v_l(Tam_p(M))` means `v`. For `M = T_l E` it is the `l`-part of `c_p(E)`; for `M = ad T` it is `Z_l` at a good
prime and, by the theorem of `\Cref{ch:blochkato}` 9.3 (important_notes.md point 64), at every potentially good additive prime
too; at a potentially multiplicative prime its valuation is given by Lemma lem:tamfactor (A2.7, `\Cref{ch:blochkato}` 8.4). The
Bloch-Kato Selmer group `H^1_f(Q, ad T tensor Q_l/Z_l)` is the one of DFG04 Section 2.1 (`\Cref{ch:blochkato}` 6.1, 6.6).
**Commentary (important_notes.md point 37).** The paper's display `Fitt_{Z_l}(H^1(I_p, M)_tor)^{G_{Q_p}}` reads as the invariants
of an ideal; what is meant (and what FPR94 and DFG04 mean, though DFG04 p. 708 prints the same superscript) is the Fitting
ideal of the invariants. Notation only; the book moves the parenthesis (B-C10).

**A1.4 `thm-main`** (theorem; *proved here* in Section 21.11 in the strengthened form (equality), as an assembly of A4.* (the
assembly is proved; its inputs DFG04 3.7, 2.7, Proposition 1.4(c), Lemma 2.1, FPR94, ARS12 are stated with references; the
equality uses the theorem of `\Cref{ch:moddeg}` 9.3); reference: the paper, Theorem thm:main; `\Cref{ch:congruence}` 9.1;
paper use: Theorem thm:main).
Statement as in the paper. Let `E` be `X_0(N)`-optimal and `l` an odd prime with `l` not dividing `2N` such that `rho bar_{E,l}`
restricted to `Gal(Qbar/Q(sqrt(l*)))`, `l* = (-1)^{(l-1)/2} l`, is absolutely irreducible. Then
(eq:identity) `v_l(deg varphi_E) >= length_{Z_l} H^1_f(Q, ad T tensor Q_l/Z_l) + sum_{q | N} v_l(Tam_q(ad T)) + sum_{q | N} e_l(E, q)`,
with equality when `H^1(X_0(N), Z_l)_m` is free over `T_m`; in particular
(eq:thm) `v_l(deg varphi_E) >= sum_{q | N} e_l(E, q) + sum_{q | N} t_l(E, q)`.
Statement as the book gives it (important_notes.md points 39, 56, 73; `\Cref{ch:congruence}` 9.1). Same hypotheses. Then
(eq:identity) holds WITH EQUALITY, with no multiplicity-one hypothesis, and the Tamagawa terms are explicit: `0` at good and at
potentially good primes, `t_l(E, q) + min(t_l(E, q), v_l(q - 1), v_l(c(u_q)))` at potentially multiplicative primes, `q = 2`
included (`\Cref{ch:blochkato}` 9.4). So `length H^1_f(Q, W) = v_l(deg varphi_E) - B^expl_l(E)`, the excess of the degree over an
explicit local bound; and (eq:thm) follows.
Reading of the hypotheses (the hypothesis table B2): for `l` not dividing `2N`, "`rho bar` absolutely irreducible
on `Gal(Qbar/Q(sqrt(l*)))`" is `l` not in `S_f` (DFG04 (31), verified), and it is equivalent to "`E[l]` irreducible and not (`l =
3` and image `N_s(F_3)`)" (important_notes.md point 47; `\Cref{ch:galrep}` 8.2, 8.6): for `l >= 5` not dividing `N` it is automatic
once `E[l]` is irreducible.
**Commentary (important_notes.md points 39, 56, 73).** What the paper says: "with equality when `H^1(X_0(N), Z_l)`, localised
..., is free over the localised Hecke algebra" (also in the abstract, and Remark rem:free supplies freeness). Correct
statement: for the optimal curve, `M_{f,lambda} = varphi_E^* H^1(E, Z_l)` and the projection formula gives the pairing
`hat delta_!` on it the ideal of values `deg varphi_E Z_l` (`\Cref{ch:moddeg}` 9.1 to 9.3); DFG04's integral structure, operator,
kernel lattice and `eta` are exactly the ones this computation needs (the five items of point 56, verified against the
published DFG04: `\Cref{ch:congruence}` Part 7.1, point 73); so `v_lambda(eta^empty_{f,lambda}) = v_l(deg varphi_E)` for every `l`
not dividing `2N` with `rho bar` irreducible, and (eq:identity) is an equality whenever `l` is not in `S_f`. How the book
presents it: Theorem 21.x is stated with equality; the paper's freeness clause is quoted in a Commentary; Remark rem:free is
explained (A4.5) but used for nothing in the proof.

**A1.5 `conj-euler`** (conjecture; *stated* (a conjecture of the paper, with its evidence in Section 6); reference: paper
Conjecture conj:euler; `\Cref{ch:blochkato}` 12.2, `\Cref{ch:computation}` 9.2; paper use: Conjecture conj:euler, Section
sec:data, appendix).
Statement. Let `E` be `X_0(N)`-optimal without CM, `l` an odd prime with `E[l]` irreducible, and `h_l(E) = length_{Z_l} H^0(Q,
ad T(1) tensor Q_l/Z_l)`. Then
(eq:rule) `v_l(deg varphi_E) >= sum_{q | N, q != l} e_l(E, q) + sum_{q | N} t_l(E, q) + [l = 3] w_3(E) - h_l(E)`,
where `w_3(E) = 1` for the types `II, IV, III^*` at `3`, `2` for `II^*, IV^*`, `0` for `III, I_0^*`, and `w_3(E) = 0` when `3` does not
divide `N` or the reduction at `3` is potentially multiplicative. Here `e_l(E, q)` at `q = 2, 3` is Definition def:terms with PARI's
`P_q`, and `t_l(E, q)` at `q = l` is as extended in A1.1. Facts (theorems, A4.11): `h_l(E) = 0` for every `l >= 5`; `h_3(E) <= 1`,
with `h_3(E) = 1` exactly when the image of `rho bar_{E,3}` is `N_s(F_3)` (label 3Ns), for every `E` with `rho bar` irreducible,
CM or not. So the correction is `1` exactly on the 3Ns curves and `0` otherwise.
**Commentary (important_notes.md point 6 and B13).** The paper (paragraph after the conjecture, and the first sentence of
Section 1.3) says `h_l(E)` "is positive exactly when `rho bar = rho bar tensor chi_{l*}`" and speaks of "a correction term when the
representation is induced from `Q(sqrt(l*))`". Correct statement: the criterion is `rho bar = rho bar tensor chi bar_l`
(residual cyclotomic character), which forces `l = 3`, where `chi bar_3 = chi_{-3}`; for `l >= 5` the condition `rho bar = rho bar
tensor chi_{l*}` can hold only when `l | N` (point 47, `\Cref{ch:galrep}` 8.2), and `h_l(E) = 0` regardless. The book writes:
"`h_l(E)` is positive exactly when `l = 3` and `rho bar_{E,3}` is induced from `Q(sqrt(-3))`, that is, when the image is 3Ns".
**Commentary (important_notes.md point 67).** The paper presents the correction term as "the term that Lemma 2.1 of DFG04
produces". That identification (Remark rem:ns) needs `H^1_f(Q, V^D) = 0` for 3Ns curves, which DFG04 Theorem 2.7 proves only for
`l` not in `S_f`, and 3Ns curves at `l = 3` are exactly in `S_f`. The book says that the derivation is conditional on this
vanishing (A5.2), which is predicted by the Bloch-Kato conjecture and not proved by the paper.

**A1.6 `def-component-groups-and-weights`** (definition; *stated* with the orders proved in `\Cref{ch:reduction}` 5.1, 8.4;
reference: Silverman ATAEC IV.9; paper use: Section 1.4, (eq:main), (eq:twist), Proposition prop:forms, Conjecture conj:eis).
Statement. For a bad prime `q`, `Phig_q = Phi_q(Fbar_q)` (B-C11(b)); `#Phig_q = n` for `I_n`; `1` for `II, II^*`; `2` for `III, III^*`;
`3` for `IV, IV^*`; `4` for `I_0^*` and `I_n^*`. The Tamagawa number `c_q = #Phi_q(F_q)` divides `#Phig_q`; the paper's statements are
about `Phig_q`. For odd `q`, `E^{(q)}` has the same Kodaira type as `E` at every `p != q`, and at `q` the types are exchanged `I_n
<-> I_n^*`, `I_0 <-> I_0^*` (every odd `q`), `II <-> IV^*`, `IV <-> II^*`, `III <-> III^*` (`q >= 5`; the latter three also hold at `q
= 3` with the conductor exponent unchanged, important_notes.md point 51, an optional strengthening checked on `5,122` pairs,
`\Cref{ch:reduction}` 8.3). Twist-symmetrised weight: `w_l(E, q) = v_l(n)` if the type is `I_n`, or `I_n^*` with `q` odd; `= 1` if
`l = 3` and the type is `IV` or `IV^*`, or `II` or `II^*` with `q` odd; `= 0` otherwise. Then `w_l(E, q) = max( v_l(#Phig_q(E)),
v_l(#Phig_q(E^{(q)})) )` for `q >= 5` (`\Cref{ch:reduction}` 8.4), and `w_l(E, 2) = v_l(#Phig_2(E))`.

**A1.7 `ineq-main-twist`** (statement; *stated* (inequalities found and tested in Section sec:forms, proved under the
hypothesis of Theorem thm:main by Proposition prop:forms); paper use: Section 1.4, Section sec:forms, Conjecture conj:eis).
Statement. (eq:main) `v_l(deg varphi_E) >= sum_{q | N} v_l(#Phig_q)`; (eq:twist) `v_l(deg varphi_E) >= sum_{q | N} w_l(E, q)`. Since
`w_l(E, q) >= v_l(#Phig_q)` termwise, (eq:twist) implies (eq:main).

**A1.8 `prop-forms`** (proposition; *proved here*, with no exception; reference: paper Proposition prop:forms;
`\Cref{ch:galrep}` 4.4, `\Cref{ch:reduction}` 6.8; paper use: Proposition prop:forms).
Statement as in the paper: under the hypothesis of Theorem thm:main, (eq:main) and (eq:twist) hold, except possibly when `l =
3` and `E` has type `IV` or `IV^*` at `2`, where they hold as soon as `e_3(E, 2) >= 1`; the same under Conjecture conj:euler with
`h_l(E) = 0`; for all `92,812` working-set curves of type `IV` or `IV^*` at `2`, `P_2(X) = 1 + 2X`.
Statement as the book gives it (important_notes.md point 43, SETTLED): under the hypothesis of Theorem thm:main, and under
Conjecture conj:euler with `h_l(E) = 0`, (eq:main) and (eq:twist) hold with no exception.
Proof plan (termwise comparison of (eq:twist) with (eq:thm), resp. (eq:rule)): type `I_n`: `t_l = v_l(n) = w_l`; `I_n^*`, `q` odd:
`t_l = v_l(n) = w_l`; `I_n^*` at `q = 2`: `w_l(E, 2) = v_l(4) = 0`; `q >= 5` of type `II, II^*, IV, IV^*`, `l = 3`: `e_3 = v_3(q - chi_{-3}(q))
>= 1 = w_3` because `q = chi_{-3}(q) mod 3`; `l >= 5`: both `0`; `q = 3`, these types, `l = 3`: `w_3(E) >= 1 = w_3(E, 3)` (only under
(eq:rule): in Theorem thm:main `3` does not divide `N`); `q = 2`, type `II, II^*`: `w_l(E, 2) = 0`; `q = 2`, type `IV, IV^*`, `l = 3`: `w_3(E, 2)
= 1 <= e_3(E, 2) = 1` by the theorem of `\Cref{ch:galrep}` 4.4; types `III, III^*, I_0^*`: `w_l = 0`. All other terms are `>= 0`.
**Commentary (important_notes.md point 43).** The paper leaves the case `l = 3`, type `IV` or `IV^*` at `2`, as an exception covered
by data (`92,812` curves with `P_2 = 1 + 2X`). It is a theorem: for additive reduction at `q != l` the `l`-power torsion fixed by
inertia is the `l`-power torsion of `Phig_q` (`\Cref{ch:reduction}` 4.5), which for types `IV, IV^*` is `Z/3`, so inertia fixes a line
of `E[3]` and acts through a unipotent of order `3`; reduction mod `3` is injective on finite subgroups of `GL_2(Z_3)`, so the
image of `I_2` on `T_3 E` is cyclic of order `3`, tame, and the same for every odd `l`; Lemma lem:euler's computation then gives
the invariant line of `ad V` with Frobenius eigenvalue `chi_{-3}(2) = -1`, `P_2(X) = 1 + 2X`, `e_3(E, 2) = v_3(3/2) = 1`
(`\Cref{ch:galrep}` 4.4; a second proof via the conductor in `\Cref{ch:reduction}` 6.8, Dokchitser-Dokchitser). The book
replaces the exception and the count by this argument and records the data (`3,226` optimal curves below `10,000` with type `IV`
or `IV^*` at `2`, all `P_2 = 1 + 2X`, `\Cref{ch:computation}` R4) as a check.

**A1.9 `history-tamagawa-exponent`** (theorem (statements of Ribet-Takahashi, Pollack-Weston, Kim-Ota); *stated; reference*;
references: RibetTakahashi97, Takahashi01, Pasten, PollackWeston11, KimOta Theorem 1.1 and Definition 2.12 (as cited);
`\Cref{ch:moddeg}` 12.2, `\Cref{ch:modgalrep}` 11.1 to 11.4, `\Cref{ch:congruence}` 10.2; paper use: Section 1.5, Remark rem:ko(2)).
Statement. (i) Ribet-Takahashi: for `N = N^+ N^-` with `N^-` a product of an even number of distinct primes and `E` optimal, the
ratio of `deg varphi_E` to the degree of the parametrisation by the Shimura curve of discriminant `N^-` is `prod_{q | N^-} n_q` up to
primes `l` at which `E[l]` is reducible (precise hypotheses in the cited papers; Pasten controls the error). (ii) The Tamagawa
exponent at `q`: the largest `t` with `rho_{E,l} mod l^t` unramified at `q`; for multiplicative `q` it is `v_l(n_q) = t_l(E, q)`
(Lemma lem:tamagawa-exp). (iii) Kim-Ota Theorem 1.1 (as in A4.13). Theorem thm:main contains the inequality `v_l(deg varphi_E) >=
sum_{q || N} t_l(E, q)` for every multiplicative prime, including `q = +-1 mod l` and `l = 3`, but not Kim-Ota's equality.

**A1.10 `thm-qual`** (theorem; *proved here* in Section 21.9, with case (a) extended to `q = 2`; reference: paper Theorem
thm:qual; `\Cref{ch:modgalrep}` 9.1, 9.2; paper use: Theorem thm:qual, Section sec:proof).
Statement as the book gives it. Let `E/Q` have conductor `N`, `l` an odd prime not dividing `N` with `rho bar_{E,l}` irreducible
and, if `l = 3`, absolutely irreducible on `Gal(Qbar/Q(sqrt(-3)))` (equivalently image not 3Ns, `\Cref{ch:galrep}` 8.6). Let `q != l`
be a prime at which `E` has additive reduction of one of the kinds (a) type `IV` or `IV^*`, `l = 3`, and `q >= 5` OR `q = 2`; (b)
type `II` or `II^*`, `q >= 5`, `l = 3`; (c) type `I_n^*` with `l | n`, `q` odd. Then `l` divides the modular degree of the
`X_0(N)`-optimal curve in the isogeny class of `E`. (For `l >= 5` only irreducibility of `rho bar` is used.)
**Commentary (important_notes.md point 43, B18).** The paper states case (a) for `q >= 5` only. Lemma lem:IV holds at `q = 2` for
types `IV, IV^*` (A1.8 Commentary; `\Cref{ch:galrep}` 4.4(iii): the Serre conductor of `rho bar_{E,3}` has exponent `1` at `2`
while `4 || N`), so the proof of case (a) applies verbatim at `q = 2` (with `3` not dividing `N`). Worked example: 52a1 (type `IV^*` at
`2`, Serre conductor `26`, `g = f_{26b} - f_{26b}(2z)` congruent to `f_{52a}` mod `3`, `deg varphi = 3`; `\Cref{ch:modgalrep}` 6.6, 9.4);
all `1,051` such optimal curves below conductor `10,000` with mod `3` image neither reducible nor 3Ns have `3 | deg varphi`. The book
states the extended theorem and marks the extension as the book's.

**A1.11 `thm-quant`** (theorem; *proved here* in Section 21.13, with `q` odd in place of `q >= 5` and with the equality clause;
reference: paper Theorem thm:quant; `\Cref{ch:congruence}` 12.1 to 12.6; paper use: Theorem thm:quant, Section sec:twisting).
Statement as in the paper. Let `l` be an odd prime with `l` not dividing `2N` and `E[l]` irreducible, `S` the set of primes `q >= 5`
at which `E` has type `I_0^*` or `I_n^*`, `E_S` the twist of `E` by `chi_S = prod_{q in S} chi_{q*}`. Then `v_l(deg varphi_E) >= v_l(r_{E_S}) +
sum_{q in S} e_l(E, q) >= sum_{q in S} e_l(E, q)`.
Statement as the book gives it. (i) The same with `S` the set of ODD primes of type `I_0^*` or `I_n^*` (important_notes.md point
60: the twist lemma for `I_n <-> I_n^*` and `I_0 <-> I_0^*` holds at every odd `q`, `l != 3` is automatic when `3 in S` since `3` then
divides `N`, and PARI's `P_3` agrees with the twist formula on all `1,100` curves checked; `\Cref{ch:congruence}` 12.1, 12.4). (ii)
(important_notes.md point 74) If moreover `l` is not in `S_f`, the first inequality is an EQUALITY: `v_l(deg varphi_E) = v_l(r_{E_S})
+ sum_{q in S} e_l(E, q)`, with no multiplicity-one hypothesis (`\Cref{ch:congruence}` 12.6).
Reading: the outer inequality uses Steps 1 to 3 and the integrality of `eta^empty_g`; the middle term uses Step 4, which needs no
freeness at level `N_S` (point 39: Lemma lem:hecke is an equality for the optimal curve of the class of `E_S`).
**Commentary (important_notes.md point 24, revised by 39).** The abstract calls this "an elementary twisting argument". Only
Step 1 (transport of congruences along the twist) is elementary; Step 2 is Lemma lem:ddt417 and Step 3 is DFG04 Proposition
1.4(c) (Ihara's lemma). The old worry that the middle term needs multiplicity one at level `N_S` is removed by point 39 (Step 4).
The book's wording: "by a twisting argument combined with the formula of Diamond, Flach and Guo for the variation of the
congruence ideal".
**Commentary (important_notes.md point 74).** The paper's sentence after the theorem ("the first inequality is then an equality
when multiplicity one holds at both levels") and Remark (2) after the proof ask for multiplicity one. Correct statement: apply
the identity (eq:identity), now an equality (A1.4), to `E` and to the optimal curve of the class of `E_S`: `ad T` is unchanged by the
twist, so the Selmer groups agree; the Tamagawa factors agree (trivial at `I_0^*` primes by point 64, equal at `I_n^*` primes since
`E_S` is multiplicative there with the same Tate parameter); the Euler sums differ by exactly `sum_{q in S} e_l(E, q)`. Data: equality
in all `25,477` pairs (curve, `l`) below conductor `10,000` with `S` nonempty, including `15,607` pairs with `3 in S` and the `8`
pairs with image 3Ns, which lie outside the theorem (`\Cref{ch:congruence}` 12.6). The book states the equality as part of the
theorem.

**A1.12 `prop-ns`** (proposition; *proved here* in Section 21.14, in the corrected form; reference: paper Proposition prop:ns;
`\Cref{ch:galrep}` 8.3, 8.4, `\Cref{ch:groups}` 5.7, 6.3, 6.7, 6.8, `\Cref{ch:reps}` 6.2, 6.6, 8.2, `\Cref{ch:galois}`
galois:quartic-on-lines; paper use: Proposition prop:ns, Section sec:anomaly, Conjecture conj:euler).
Statement (book's form). Let `E/Q` (with or without CM) have `E[3]` irreducible. Then the image `H` of `rho bar_{E,3}` is conjugate to
`GL_2(F_3)`, `N_ns(F_3)` or `N_s(F_3)`; `rho bar_{E,3}` is absolutely irreducible on `Gal(Qbar/Q(sqrt(-3)))` unless `H ~ N_s(F_3)`; in
that case `rho bar_{E,3} tensor F_9 = Ind psi` for a character `psi` of order `4` of `G_{Q(sqrt(-3))}` with values in `F_9^x`, `rho
bar_{E,3} = rho bar_{E,3} tensor chi_{-3}` over `F_3`, `H^0(Q, ad rho bar_{E,3}(1))` is a line, and `h_3(E) = 1`. The `3`-division polynomial
is a product of two irreducible quadratics in the `N_s` case and irreducible in the other two.
Commentary (points 1, 2, 4, 9, 33, 48): see A5.1, where the proof is walked through. In short: the "non-abelian and faithful"
step needs the commutator argument (point 1); `N_s(F_3)` is not maximal (point 2); Zywina15 and Dickson are cited by section
(point 4) and the list of images is proved directly; "without CM" is not used (point 9); "induced" holds over `F_9` only (point
33); and the main observations of Section sec:anomaly about 3Ns curves are theorems (point 48, `\Cref{ch:galrep}` 8.4).
Data check: among the `38,042` optimal curves below conductor `10,000`, `ns3` (two quadratic factors) agrees with Cremona's 3Ns
label on all `37,853` non-CM curves (`90` each), and is `1` on `13` CM curves (121b1, 256a1, ...; `j = -32768` or `8000`)
(`\Cref{ch:computation}` R5).

**A1.13 `conj-eis`** (conjecture; *stated*, with the bound `D <= 2` *proved here* from the first bound; reference: paper
Conjecture conj:eis; `\Cref{ch:ellcurves}` 9.8, `\Cref{ch:galrep}` 9.2, `\Cref{ch:moddeg}` 11; paper use: Conjecture conj:eis,
Section sec:eis, Open question 4).
Statement. Let `E` be optimal, not CM, with a rational `l`-isogeny, `l` odd, and `D = sum_{q | N} v_l(#Phig_q) - v_l(deg varphi_E)` the
deficit of (eq:main). Then `D <= v_l(#E(Q)_tors) + [E[3] = Z/3 + mu_3]`, and `D <=` the number of curves in the isogeny class of `E`
with a rational point of order `l`. In particular `D <= 0` without rational `l`-torsion, `D <= 1` for `l >= 5`, `D <= 2` for `l = 3`.
**Commentary (important_notes.md point 17).** The paper says that a point of order `9` and `E[3] = Z/3 + mu_3` "do not occur
together in the tables" and, not having proved it, that `D <= 2` "is part of the conjecture". They cannot occur together for
non-CM `E` (proved in `\Cref{ch:ellcurves}` 9.8): with `phi: E -> E' = E/mu_3` and its dual `phi^`, the subgroup `(phi^)^{-1}(<P>)` of `E'`
has order `27`, is rational, and does not contain `E'[3]` (since `phi^(E'[3]) = mu_3` is not in `<P>`), so it is cyclic; a rational
cyclic `27`-isogeny forces CM (`\Cref{ch:ellcurves}` 9.6(iii)). So `D <= 2` follows from the first bound and Mazur's theorem;
likewise `D <= 1` for `l = 5, 7` and `D <= 0` for `l >= 11`. The book proves this and states only the first two bounds as
conjectural.
**Commentary (important_notes.md points 3 and 44).** Section sec:eis calls 3Cs.1.1 "the split Cartan image". 3Cs.1.1 is the
order-`2` subgroup `{diag(1, +-1)}` of the split Cartan subgroup, the image exactly when `E[3] = Z/3 + mu_3`; the full split Cartan
image is 3Cs (`\Cref{ch:groups}` 6.10, `\Cref{ch:galrep}` 9.2). The labels 3Ns, 3Cs.1.1, 3B.1.1 were checked against Cremona's
`galrep` file (consistent with the intrinsic descriptions: 3B.1.1 and 3Cs.1.1 exactly the curves with rational `3`-torsion), not
yet against the tables of Sutherland16 (`\Cref{ch:galrep}` 7.4). The book uses the intrinsic description everywhere.

### A2. The paper's Section 2: local invariants (Sections 21.5 to 21.7)

**A2.1 `lem-tamagawa-exp`** (lemma; *proved here*; reference: Silverman ATAEC V.3 and V.5, DDT Theorem 3.1(e);
`\Cref{ch:reduction}` 7.4, 7.5, `\Cref{ch:galrep}` 3.2, 3.3 (two proofs); paper use: Lemma lem:tamagawa-exp, Theorem thm:qual
case (c), Section 1.5, Remark rem:ko).
Statement. Let `q` be a prime of multiplicative reduction, `n_q = v_q(Delta_E) = -v_q(j_E)`, and `l != q` a prime. Then `rho_{E,l} mod l^t`
is unramified at `q` iff `l^t | n_q`; this holds for split and for nonsplit reduction.
Expanded proof: over the unramified quadratic extension `K` of `Q_q` (or `Q_q` itself if split) `E` is the Tate curve `E_{q_E}`,
`v_q(q_E) = n_q`; `I_q = I_K`. `E_{q_E}[l^t]` is generated by `mu_{l^t}` and an `l^t`-th root of `q_E`; `I_q` fixes `mu_{l^t}` (`l != q`) and moves
the root by the Kummer cocycle. By Kummer theory over `Q_q^ur` (which contains `mu_{l^t}`), inertia acts trivially iff `q_E` is an
`l^t`-th power in `Q_q^ur`; units of its valuation ring are `l^t`-th powers (Hensel, `l != q`), so this holds iff `l^t | v_q(q_E) = n_q`.
**Commentary (important_notes.md point 8).** The paper's proof calls the Tate parameter `u` (Lemma lem:tamfactor uses `u` for its
unit part) and says "an `l^t`-th power in `Q_q^ur` up to units", which mixes two statements. No mathematical error. The book names
the Tate parameter `q_E` (B-C14) and writes the two steps separately as above.

**A2.2 `lem-IV`** (lemma; *proved here*; reference: Kraus90; `\Cref{ch:ant}` 4.7, 4.8 (`Z_3[zeta_3]` is a DVR with uniformiser
`pi = 1 - zeta_3`), `\Cref{ch:reduction}` 6.6, `\Cref{ch:galrep}` 4.3, 4.4; paper use: Lemma lem:IV, Theorem thm:qual (a), (b),
Remark rem:types).
Statement. Let `q >= 5` be a prime at which `E` has type `IV` or `IV^*`. Then the image of `I_q` in `Aut(T_3 E)` is cyclic of order
`3`, its image in `Aut(E[3])` is a nontrivial unipotent subgroup, `E[3]^{I_q}` is a line, `rho bar_{E,3}` is tamely ramified at `q`,
and the Serre conductor of `rho bar_{E,3}` has exponent `1` at `q`. (The same holds at `q = 2`: `\Cref{ch:galrep}` 4.4, A1.8.)
Expanded proof: `v_q(Delta_min) in {4, 8}`; Kraus: the image of `I_q` on `T_l E` (any `l != q`) has order `12/gcd(v_q(Delta), 12) = 3`; tame
since `q != 3`, so cyclic, generated by `sigma` of order `3` with `det sigma = chi_3^cyc(sigma) = 1` (the cyclotomic character at `3`
is trivial on inertia at `q != 3`; B-C6(a)); eigenvalues primitive cube roots of unity; `sigma^2 + sigma + 1 = 0` on `T` (Cayley-
Hamilton); `T` is a torsion-free module over `Z_3[X]/(X^2 + X + 1) = Z_3[zeta_3]` with `X` acting as `sigma`, a DVR with uniformiser
`pi = 1 - zeta_3`, `pi^2 = -3 zeta_3`, residue field `F_3`; rank `2` over `Z_3` forces `T` free of rank one; `E[3] = T/3T = Z_3[zeta_3]/(pi^2)`
with `sigma` acting as `zeta_3 = 1 - pi`; so `sigma - 1` acts as `-pi`, nonzero with square `0` there: a nontrivial unipotent; fixed
line `pi Z_3[zeta_3]/(pi^2)`; conductor exponent `2 - 1 + 0 = 1`.
**Commentary (important_notes.md point 13).** The paper writes "`Z_3[sigma]/(sigma^2 + sigma + 1) = Z_3[zeta_3]`"; `Z_3[sigma]` already
satisfies the relation. The intended statement is `Z_3[X]/(X^2 + X + 1)` with `sigma` acting as `X`. Notation only.

**A2.3 `rem-types`** (proposition (the paper's Remark rem:types, in corrected and complete form); *proved here* (three lines
of linear algebra mod `3`, the table of `\Cref{ch:galrep}` 4.5 cited); reference: Kraus90; paper use: Remark rem:types,
Theorem thm:qual (why only (a), (b), (c))).
Statement (book's form, `q >= 5`, `l = 3`): (a) `E[3]^{I_q} = 0` and the Serre conductor exponent of `rho bar_{E,3}` at `q` is `2 = f_q(E)` for
EVERY additive type other than `IV, IV^*`: the generator of inertia acts mod `3` as `-1` (`I_0^*`, and `I_n^*` with `3 | n`), as `tau` with
`tau^2 = -1` (`III, III^*`), or as `-u` with `u` a nontrivial unipotent (`II, II^*`, and `I_n^*` with `3` not dividing `n`); none fixes a
vector. (b) The twist by `chi_{q*}` lowers the Serre exponent of `rho bar_{E,3}` exactly for `II, II^*` (to `1`), `I_n^*` (to `1`, or `0` if `3 |
n`) and `I_0^*` (to `0`); it lowers the conductor exponent of `E` itself exactly for `I_n^*` and `I_0^*` (`II <-> IV^*` keeps `f_q = 2`).
**Commentary (important_notes.md points 22 and 49).** The paper states (a) only "in the last two cases" (`II, II^*, I_n^*`) and
omits `I_0^*` from (b) (point 22); and its phrase "these are the types whose twist by `chi_q` lowers the conductor exponent" is right
for the Serre conductor of `rho bar_{E,3}`, not for the conductor of `E`, in the type `II` case (point 49). Nothing downstream
depends on this. The book states the complete version above and explains separately why `I_0^*` is not in Theorem thm:qual (A3.5).

**A2.4 `lem-twist`** (lemma; (i), (ii) *proved here*; (iii) *stated; reference* Atkin-Li Theorem 3.1; reference:
`\Cref{ch:reduction}` 8.1, 8.2, 8.3, 5.4, `\Cref{ch:hecke}` 9.2, `\Cref{ch:modgalrep}` 3.8, `\Cref{ch:local}` 9.3; paper use: Lemma
lem:twist, Section 1.4, Lemma lem:euler, Theorem thm:qual (b), (c), Theorem thm:main (`I_n^*` primes), Theorem thm:twist, Theorem
thm:quant).
Statement. Let `q` be odd, `chi = chi_{q*}` (the paper's `chi_q`; B-C6(c)), `E^{(q)}` the twist of `E` by `chi`.
(i) At every `p != q`, `E` and `E^{(q)}` have the same Kodaira type, the same `Phig_p` and the same conductor exponent.
(ii) If `E` has type `I_n` at `q` (`n >= 0`) then `E^{(q)}` has type `I_n^*` at `q` and conversely, with the same `n`. If `q >= 5` and `E`
has type `II, III, IV` at `q` then `E^{(q)}` has type `IV^*, III^*, II^*` respectively, and conversely. The conductor exponent of
`E^{(q)}` at `q` is `2` when additive and `1` when of type `I_n`, `n >= 1`.
(iii) (Atkin-Li) Let `g` be a newform of weight `2` on `Gamma_0(M)` with `q^2` not dividing `M`. Then `g tensor chi = sum chi(n) a_n(g) q^n`
is a newform on `Gamma_0(lcm(M, q^2))`.
Expanded proof of (i): `chi` is unramified at `p`, so `E` and `E^{(q)}` become isomorphic over an unramified extension of `Q_p`, and
type, `Phig_p`, conductor exponent are invariant under unramified base change (`\Cref{ch:reduction}` 4.3). (ii): the twist by `q*`
of a minimal model has a model with `c_4' = (q*)^2 c_4`, `c_6' = (q*)^3 c_6`, `Delta' = (q*)^6 Delta`, `j' = j` (model `y^2 = x^3 + q* a_2 x^2 +
(q*)^2 a_4 x + (q*)^3 a_6`). Potentially multiplicative: `v_q(j) < 0`, type `I_n` or `I_n^*` with `n = -v_q(j)` according as the reduction is
multiplicative or additive, and a ramified quadratic twist exchanges them. `I_0 <-> I_0^*`: for the twisted model the cubic
produced by Tate's algorithm after removing powers of `q` is `T^3 + e a_2 T^2 + a_4 T + e a_6`, `e = q*/q = +-1`, whose roots are `e` times
those of `T^3 + a_2 T^2 + a_4 T + a_6`, so "distinct roots mod `q`" (the criterion for `I_0^*`, `\Cref{ch:reduction}` 5.4) is unaffected;
conversely a type `I_0^*` curve at odd `q` has such a model, and its twist is good. `q >= 5`, potentially good: the type is read off
`v_q(Delta_min) in {0, 2, 3, 4, 6, 8, 9, 10}`; twisting adds `6`, and the model is minimal iff the result is `< 12`, else subtract `12`.
Conductor exponents: `2` for the additive side of each listed exchange, since the reduction becomes semistable over a tamely
ramified quadratic extension (also at `q = 3`). (iii) reference; for `q || M` the local component is an unramified twist of
Steinberg, whose twist by a ramified quadratic character has conductor exponent `2` (`\Cref{ch:local}` 9.3(ii)).
**Commentary (important_notes.md points 29 and 45).** The paper writes the invariants of the twist as `q^2 c_4, q^3 c_6, q^6 Delta`
(those of the twist by `q`, which differs from the twist by `q*` in the sign of `c_6` when `q = 3 mod 4`) and the twisted cubic as
`T^3 + a_2 T^2 + a_4 T + a_6` (the correct cubic carries the sign `e`). Only `q`-adic valuations and the distinctness of roots are used, so
the argument is unaffected. The book writes `q*` and the cubic with `e`.
**Commentary (important_notes.md point 28).** "The conductor exponents are the standard ones for `q` odd (tame)": at `q = 3` a
general additive curve can be wild (exponent up to `5`). For the exchanges the lemma lists the additive side has exponent `2`, as
above. The book restricts the sentence.
**Commentary (important_notes.md point 51, optional).** The exchanges `II <-> IV^*`, `III <-> III^*`, `IV <-> II^*` also hold at `q = 3`, with
the conductor exponent unchanged (all `5,122` pairs below conductor `10,000`, `\Cref{ch:reduction}` 8.3, `\Cref{ch:computation}`
R9); the paper states them for `q >= 5` only and needs no more. The book mentions it in one sentence, without proof.

**A2.5 `lem-euler`** (lemma; *proved here* (the computation of `(ad V)^{I_q}` and its Frobenius eigenvalue in each case; Chapter
19 proves it in its own language, `\Cref{ch:lfunctions}` 9.3); reference: Kraus90; `\Cref{ch:local}` 9.2 to 9.4,
`\Cref{ch:galrep}` 3.2, 4.1, `\Cref{ch:ant}` 4.9, `\Cref{ch:reps}` 7.3, 7.7; paper use: Lemma lem:euler, the table, Theorem thm:quant
Step 3, Lemma lem:fpr).
Statement: as A1.2.
Expanded proof plan. General principle: `L_q(A_f, s)^{-1} = prod (1 - lambda q^{-s})` over the eigenvalues `lambda` of the GEOMETRIC
Frobenius `Frob_q^{-1}` on `(ad V)^{I_q}` (C2(b)); a good prime has eigenvalues `alpha/beta, 1, beta/alpha` in either convention.
`I_n`: in a basis `e_1, e_2` of `T`, `rho|_{G_{Q_q}} = (chi_l eps, eps kappa; 0, eps)` (arithmetic Frobenius, corner `eps kappa`, B-C14);
inertia acts through `t` with `t e_1 = e_1`, `t e_2 = e_2 + n' e_1`, `n' != 0`; on `ad V` (basis `e = e_1 tensor e_2^vee`, `h = e_1 tensor
e_1^vee - e_2 tensor e_2^vee`, `f = e_2 tensor e_1^vee`) `(t - 1)e = 0`, `(t - 1)h = -2n' e`, `(t - 1)f = n' h - n'^2 e`, so `(ad V)^{I_q} = Q_l
e`. The arithmetic Frobenius sends `e` to `q e`, so the geometric one acts by `q^{-1}` and `L_q(A_f, s)^{-1} = 1 - q^{-1-s}`; the naive
factor at `s = 1` is `1 - a_q^2 q^{-2} = 1 - q^{-2}` (`a_q^2 = 1`), so `e_l = 0`. (The same line is `ker N` of the Weil-Deligne
representation `sp(2)` twisted by an unramified character, `\Cref{ch:local}` 9.3(i).)
**Commentary (important_notes.md point 11).** The paper says "a line with eigenvalue `q^{-1}`" without naming the Frobenius,
and computes with the arithmetic one in Lemma lem:tamfactor. The eigenvalue is `q` for the arithmetic and `q^{-1}` for the
geometric Frobenius; the table is right with the geometric one, which is DFG04's convention (verified). The book says
"geometric" here and "arithmetic" in A2.7.
`I_n^*`: `V = V' tensor chi_{q*}`, `V'` Steinberg, `ad V = ad V'`, same true factor, but `a_q = 0` so the naive factor is `1` and `e_l = v_l(1 -
q^{-2}) = v_l(q^2 - 1)`. `II, II^*, IV, IV^*`: image of `I_q` cyclic of order `3` or `6` generated by `sigma` or `-sigma`, eigenvalues
`zeta_3^{+-1}`; on `ad V` the sign disappears; `End_{I_q}(T) = Z_l[sigma] = Z_l tensor Z[zeta_3]` and `End_{I_q}(V) = Q_l tensor Q(zeta_3)` (a
field if `l = 2 mod 3`, `Q_l x Q_l` if `l = 1 mod 3`; `\Cref{ch:ant}` 4.9); `(ad V)^{I_q}` is its trace-zero part, the line spanned by `2
sigma + 1` (square `-3`; it plays the role of `sqrt(-3)`). The arithmetic Frobenius acts on `<sigma>` by `sigma -> sigma^q` (`\Cref{ch:local}`
5.4), so it centralises `sigma` if `q = 1 mod 3` and inverts it if `q = 2 mod 3`, acting on `2 sigma + 1` by `chi_{-3}(q) = +-1` (as `2
sigma^2 + 1 = -(2 sigma + 1)`); a sign is its own inverse, so the geometric Frobenius acts by the same `chi_{-3}(q)`; `L_q(A_f, s)^{-1} = 1 -
chi_{-3}(q) q^{-s}` and `e_l = v_l(1 - chi_{-3}(q) q^{-1}) = v_l(q - chi_{-3}(q))`. `III, III^*`: image of order `4` generated by `tau`, `tau^2 =
-1`, eigenvalues `+-i`; `End_{I_q}(V) = Q_l tensor Q(i)`; the invariant line of `ad V` is spanned by `tau` itself (it commutes with `tau`
and has trace `0`); Frobenius acts on it by `tau -> tau^{+-1}`, i.e. by `chi_{-4}(q)`; `e_l = v_l(q - chi_{-4}(q))`.
**Commentary (important_notes.md point 12).** The paper writes "`sqrt(-3) in Z_l[zeta_3] = End_{I_q}(V)`". Correct: `End_{I_q}(T) =
Z_l tensor Z[zeta_3]` and `End_{I_q}(V) = Q_l tensor Q(zeta_3)`, which is not a field when `l = 1 mod 3`. The argument only needs the
element `2 sigma + 1` and the action of Frobenius through `Gal(Q(zeta_3)/Q)`, so it is unaffected.
**Commentary (important_notes.md point 34).** For types `III, III^*` the paper speaks of "the diagonal element"; when `l = 3 mod 4`, `i`
is not in `Q_l`, `tau` is not diagonalisable over `Q_l`, and there is no diagonal element. The invariant line is spanned by `tau`, on
which Frobenius acts by `chi_{-4}(q)` as the paper says. The book writes `tau`.
`I_0^*`: `V = V' tensor chi_{q*}`, `V'` unramified with arithmetic Frobenius eigenvalues `alpha, beta` (those of `E'`, `alpha + beta = a_q(E')`,
`alpha beta = q`); `ad V = ad V'` unramified with eigenvalues `alpha/beta, 1, beta/alpha`; `L_q(A_f, 1)^{-1} = (1 - alpha/(beta q))(1 -
1/q)(1 - beta/(alpha q)) = ((q - 1)/q) ((q + 1)^2 - a^2)/q^2` with `a = a_q(E')` (`\Cref{ch:rings}` 11.4); `e_l = v_l(q - 1) + v_l((q + 1)^2 - a^2)`.
Pitfalls for the writer: `alpha/beta` lies in `Q_l(alpha)`, the product is rational; `chi_{-3}(q) = (q/3) = (-3/q)`.
The paper's closing sentence ("confirmed against PARI's `lfunsympow` on every curve of the tables") is reproduced on all `67,745`
pairs below conductor `10,000` (`\Cref{ch:computation}` R4).

**A2.6 `rem-wild`** (remark (the paper's Remark rem:wild), in corrected form; *stated* with PARI-verified values; reference:
`\Cref{ch:lfunctions}` 10.1, 10.2, `\Cref{ch:galrep}` 4.4, 4.6, `\Cref{ch:reduction}` 9.2 to 9.4, `\Cref{ch:computation}` 6.6;
paper use: Remark rem:wild, Conjecture conj:euler, Section sec:wild, Proposition prop:forms).
Statement (book's form). At `q = 2, 3` the Kodaira type does not determine `L_q(A_f, s)`; what does is the shape of `rho(I_q)`
(`\Cref{ch:lfunctions}` 10.1): `P_q` is `1 - X`, the `I_0^*` cubic of a quadratic twist with good reduction, `1 - c q X` (`c = +-1`), or `1`.
Definition def:terms applies verbatim with PARI's factor. Type `IV` or `IV^*` at `2`: `P_2(X) = 1 + 2X` and `e_3(E, 2) = v_3(3/2) = 1`, a
THEOREM (A1.8). Type `II` at `2`: all four shapes occur; for instance 336f1 has `P_2 = 1 + 2X`, `e_3 = 1`, `deg 24`; type `II^*` at `2`: 1232l1
(`= 77a1 tensor chi_{-4}`) has the cubic `(1 - 2X)(1 + 2X)^2`, `e_3(E, 2) = v_3(9/8) = 2`, `deg 288 = 2^5 3^2`, the bound at `l = 3` attained by the
prime `2` alone; 592c1 (`= 37a1 tensor chi_{-4}`) has `(1 - 2X)(1 + 4X^2)`, `e_5(E, 2) = v_5(5/8) = 1`, `deg 80`: the prime `2` can contribute at
`l = 5`. Type `I_m^*` at `2`: potentially good in `61%` of the pairs below conductor `10,000` (`5,935` of `9,667`), and then `P_2 = 1` for
`5,073`, `1 + 2X` for `146`, a cubic (with `a' = +-1`, contributing nothing at odd `l`) for `716`; `t_l(E, 2) = 0` in that case. At `q = l` the
Euler factor is not the relevant quantity; the weights `w_3` of Conjecture conj:euler are empirical.
**Commentary (important_notes.md points 50 and 69; B16).** The paper says "a type `II` at `2` has `P_2 = 1` and `e_3 = 0`" and "a type `I_n^*`
at `2` has potentially good reduction in about half of the cases, with a cubic `P_2`". Both are false as general statements:
below conductor `10,000` type `II` at `2` has `P_2 = 1` for `1,092` curves, `1 + 2X` for `371` and a cubic for `74` (type `II^*`: `514`, `74`, `191`),
with 336f1 and 1232l1 as counterexamples; and the cubic is a minority shape for potentially good `I_m^*` at `2`. Correct statement: the
type at `2` does not determine `P_2`; the four shapes and their meaning are as above. No theorem or count of the paper changes,
since the rule and tables use PARI's factor. The book replaces the two sentences by "the Kodaira type at `2` does not determine `P_2`;
for instance ..." and gives the classification with a pointer to `\Cref{ch:lfunctions}` 10.1. "A type `IV` at `2` has `P_2 = 1 + 2X`"
is kept, as a theorem.

**A2.7 `lem-tamfactor`** (lemma; *proved here*, every step, in corrected form; reference: FPR94 I.4.2.2, DFG04 p. 708 (verified),
DDT Theorem 3.1(e); `\Cref{ch:blochkato}` 8.1 to 8.5 (the lemma proved there), `\Cref{ch:galcoh}` 5.1 to 5.5 (the identification
of `c'`), `\Cref{ch:cohomology}` model-computation, frobenius-on-h1-inertia, `\Cref{ch:modules}` 7.6; paper use: Lemma
lem:tamfactor, Theorem thm:main (eq:thm), Remark rem:ko(1), Section sec:tam, Open question 3).
Statement (book's notation, B-C14). Let `q` be a prime of multiplicative reduction, `n = n_q = v_q(Delta_E)`, `l` an odd prime, `l != q`,
`T = T_l E`, `M = ad T`. Let `q_E in Q_q^x` be the Tate parameter (`v_q(q_E) = n`), `u = q_E q^{-n} in Z_q^x` its unit part, `u bar in F_q^x` its
reduction, and `c(u)` the class of `u bar` in `F_q^x/(F_q^x)^{l^{v_l(q-1)}}`, a cyclic group of order `l^{v_l(q-1)}` identified with
`Z/l^{v_l(q-1)}` by a choice of generator; `v_l(c(u))` does not depend on the choice and is read as in B-C10 (so `v_l(0) = v_l(q - 1)`), and
`v_l(c(u)) >= k` iff `u bar` is an `l^k`-th power in `F_q^x`, for `k <= v_l(q - 1)`. Then `H^1(I_q, M)_tor = (Z/l^{v_l(n)})^2` and
`v_l(Tam_q(ad T)) = v_l(n) + min( v_l(n), v_l(q - 1), v_l(c(u)) )`.
In particular `v_l(Tam_q(ad T)) >= t_l(E, q)`, with equality unless `q = 1 mod l`, `l | n` and `u bar` is an `l`-th power in `F_q^x`.
Expanded proof, the exact facts invoked:
(1) [`\Cref{ch:galrep}` 3.2, `\Cref{ch:reduction}` 7.5; DDT 3.1(e)] Over the unramified quadratic extension `E` is a Tate curve; `T` has a
basis `e_1, e_2` in which `G = G_{Q_q}` acts by `rho(g) = (chi_l(g) eps(g), eps(g) kappa(g); 0, eps(g))`, `eps` unramified of order `<= 2` with
`eps(Frob) = a_q(E)`, `kappa` the Kummer cocycle of `q_E` in `H^1(G, Z_l(1)) = lim Q_q^x/(Q_q^x)^{l^k}`. The corner is `eps kappa`: the
nonsplit curve is the Tate curve twisted by `eps`, and `(chi_l, kappa; 0, 1) tensor eps = (chi_l eps, eps kappa; 0, eps)`.
(2) [`\Cref{ch:local}` 5.3, 6.2] `I = I_q` acts through its maximal pro-`l` tame quotient `Z_l(1)`, generated by `t`; `kappa|_I = n` times the
tame character and `eps|_I = 1`, so `t e_1 = e_1`, `t e_2 = e_2 + n' e_1` with `v_l(n') = v_l(n)` (one may take `n' = n`, `\Cref{ch:galcoh}` 5.4(ii)).
(3) [`\Cref{ch:cohomology}` cohomology-through-pro-l-quotient, procyclic-compact] The kernel of `I -> <t>` has order prime to `l`, so
inflation-restriction gives `H^1(I, M') = H^1(<t>, M') = M'/(t - 1)M'` via `c -> c(t)`, for every finitely generated `Z_l`-module `M'`.
(4) [computation] In the basis `e, h, f` of `M = ad T`: `(t - 1)e = 0`, `(t - 1)h = -2n' e`, `(t - 1)f = n' h - n'^2 e`; `2` is a unit, so `(t -
1)M = n'(Z_l e + Z_l h)`, `H^1(I, M) = (Z_l/n') e bar + (Z_l/n') h bar + Z_l f bar`, torsion `(Z/l^{v_l(n)})^2`.
(5) [`\Cref{ch:cohomology}` conjugation-action, frobenius-on-h1-inertia] `G/I` acts by `(sigma . c)(i) = sigma c(sigma^{-1} i sigma)`; with
`Frob^{-1} t Frob = t^{q^{-1}}` (C2(a), ARITHMETIC Frobenius) and `c(t^k) = k c(t)` modulo `(t - 1)M`, the arithmetic Frobenius acts on `M/(t
- 1)M` as `q^{-1} Ad(rho(Frob))`.
(6) [computation] `rho(Frob) = (eps q, c'; 0, eps)` with `eps = eps(Frob) = +-1` and `c' = eps(Frob) kappa(Frob)`; `Ad` sends `e -> q e`, `h -> h - 2
c' eps e`; so on the torsion `e bar -> e bar` and `h bar -> q^{-1}(h bar - 2 c' eps e bar)`. Fixed points `x e bar + y h bar`: `(q - 1) y = 0` and `c' y =
0` in `Z/l^{v_l(n)}`; `l^{v_l(n)}` choices of `x`, `l^{min(v_l(n), v_l(q-1), v_l(c'))}` of `y`; the Fitting ideal of this finite group has
valuation `v_l(n) + min(v_l(n), v_l(q - 1), v_l(c'))` (`\Cref{ch:modules}` 7.6).
(7) [`\Cref{ch:galcoh}` 5.1 to 5.4] Identify `c'`. Write `q_E = q^n u`, so `kappa = n kappa_q + kappa_u` as cocycles (product system of
roots). Since `q != l`, inertia acts trivially on `Z_l(1)`, so `H^1(G/I, Z_l(1)^I) = Z_l(1)/(q - 1) = F_q^x tensor Z_l`; and since `q` is a
canonical uniformiser, `H^1(Q_q, Z_l(1)) = Z_l kappa_q + H^1_ur` canonically (`\Cref{ch:galcoh}` 5.3). Projection onto the unramified summand
along `kappa_q` sends `[kappa]` to `[kappa_u]`, the class of `u bar` in `F_q^x tensor Z_l`: this is the precise meaning of the paper's "image of
`kappa` in `H^1(G/I, Z_l(1)^I)`". For the Frobenius lift that fixes a compatible system of `l`-power roots of `q` (possible since
`Q_q(q^{1/l^infty})` is totally ramified), `kappa_q(Frob) = 0` and `c' = eps(Frob) kappa_u(Frob)`, which is `c(u)` up to a unit (the sign
`eps(Frob)` does not change the valuation). For another lift `Frob t^k` the corner becomes `c' + eps q k n'` (compute `rho(Frob t^k)`), and
another choice of roots changes `kappa` by a coboundary; so in general `c'` is well defined only modulo `(n', q - 1) Z_l`, which does not
change `min(v_l(n), v_l(q - 1), v_l(c'))`. Hence the minimum equals `min(v_l(n), v_l(q - 1), v_l(c(u)))`.
(8) [`\Cref{ch:blochkato}` 7.1; FPR94 I.4.2.2 as recalled in DFG04 p. 708] `Tam_q(M) = Fitt((H^1(I, M)_tor)^G)`.
(9) Check for `M = T`: `H^1(I, T)_tor = (Z/l^{v_l(n)}) e_1 bar` with `Frob` acting by `q^{-1} eps q = eps`; invariants all of it if split, `0`
if nonsplit (`l` odd): `v_l(Tam_q(T)) = v_l(c_q(E))`, as the paper says (`\Cref{ch:blochkato}` 7.6; checked on `101,336` pairs).
(10) The "in particular": `t_l(E, q) = v_l(n)`; the extra term is `>= 1` iff `v_l(n) >= 1`, `v_l(q - 1) >= 1` and `v_l(c(u)) >= 1`; it is `0` at `q = 2`
and does not depend on whether the reduction is split (`\Cref{ch:blochkato}` 8.3).
**Commentary (important_notes.md point 42; B7, T1).** The paper writes the corner of the Tate matrix as `kappa`. For a homomorphism
the corner `c` must satisfy `c(gh) = chi_l eps(g) c(h) + c(g) eps(h)`, which `kappa` does only when `eps` is trivial; `eps kappa` always works.
Correct statement: corner `eps kappa`, as in (1). Nothing changes: `eps` is trivial on inertia, and at Frobenius `c'` changes by the
sign `eps(Frob)`. The book writes `eps kappa` and `c' = eps(Frob) kappa(Frob)`.
**Commentary (important_notes.md point 7 with its addendum; B21).** The paper says "`c'` is the image of `kappa` in `H^1(G/I,
Z_l(1)^I)` ... well defined modulo `q - 1`". The phrase has a precise meaning via the splitting given by the uniformiser `q` (step (7));
what is imprecise is that `c'` is a cocycle VALUE, equal to `eps(Frob)` times that image only for the Frobenius lift fixing a compatible
system of `l`-power roots of `q`, and in general well defined only modulo `(n, q - 1)`, not modulo `q - 1`. The conclusion is unaffected.
The book keeps the paper's phrase, adds "via the splitting given by the uniformiser `q`", and states the indeterminacy.
**Commentary (important_notes.md point 11).** The matrix `rho(Frob) = (eps q, c'; 0, eps)` and the relation `Frob^{-1} t Frob =
t^{q^{-1}}` are for the ARITHMETIC Frobenius (B-C2(c)); the book says so in this proof, while the `L`-factors of A2.5 use the
geometric one.
**Commentary (important_notes.md points 23 and 31; T2).** The paper's `c` (and the `c_q` of Section sec:tam) collides with the
Tamagawa number `c_q`, and "the class of `u` in `F_q^x`" should be "of the reduction of `u`", with `v_l(0)` read as `v_l(q - 1)`. The book
writes `c(u)` (or `c(u_q)`) in its own text and keeps `c` only inside quotations of the paper.
Worked values (PARI-checked, `\Cref{ch:blochkato}` 8.5, `\Cref{ch:computation}` R3, 6.8): 791a1 at `7` (`I_3`, `u bar = 6 = -1`, a cube:
`v_3(Tam) = 2`, `t_3 = 1`); 539c1 at `7` (`I_3^*`, same `q_E` as 77c1, `u bar = 5`, not a cube: `v_3(Tam) = 1`); 1577a1 at `19` (`u bar = 8`, a cube, not
a ninth power: extra `1`); 11a1 at `11`, `l = 5` (`u bar = 10 = -1`, a fifth power: `v_5(Tam) = 2`, but `E[5]` reducible: the lemma applies, the
theorem does not). The formula was also checked exhaustively for `l = 3, 5` (`52,896` brute-force checks, `\Cref{ch:blochkato}` Part 6.6).

### A3. The paper's Section 3: proof of Theorem thm:qual (Sections 21.8 to 21.9)

**A3.1 `def-congruence-number`** (definition; *stated*; reference: ARS12 Section 2 and Theorem 2.2 (as cited); `\Cref{ch:hecke}`
4.3, 11.2, `\Cref{ch:moddeg}` 8.1, 8.3, 8.5, 9.4, 10.3; paper use: Section 1, Section 3 preamble, Lemma lem:crit, Lemma lem:hecke,
Theorem thm:twist).
Statement. `r_E` (for `E` optimal of level `N`, newform `f`) is the largest integer `r` such that `f = g mod r` coefficientwise for some
`g in S_2(Gamma_0(N); Z)` orthogonal to `f` for the Petersson product. Agashe-Ribet-Stein Theorem 2.2: `deg varphi_E | r_E`, and
`v_p(deg varphi_E) = v_p(r_E)` for every prime `p` with `p^2` not dividing `N`. (The divisibility is reproved in `\Cref{ch:moddeg}` 9.4 from
the projection formula, and the equality for `l` not dividing `2N` with `E[l]` irreducible in `\Cref{ch:moddeg}` 10.3.)
Examples (all recomputed, `\Cref{ch:moddeg}` 8.5, `\Cref{ch:hecke}` 11.2; important_notes.md B19, points 58, 62): 99a1 (ARS12's
99A1, `N = 3^2 11`): `deg = 4`, `r = 12`, the gap at `3` with `3^2 | N`, the congruence `f_{99a} = f_{99b} = f_{99d} mod 3` beyond the Sturm
bound; 726a1: `deg = 144`, `r = 1584 = 11 * 144`, the gap at `11` with `11^2 | 726`; 539d1: `deg = 72`, `r = 504`, the gap at `7` with `7^2 |
539`; 88a1: `deg 8`, `r = 16`. In every other computed case the two agree, also at primes `p` with `p^2 | N` (121a1, 539c1, 980i1).

**A3.2 `lem-crit`** (lemma; *proved here* (the tour follows the paper's proof line by line; the full proof is
`\Cref{ch:modgalrep}` 8.2, decision B17; `\Cref{ch:moddeg}` 8.2 and `\Cref{ch:congruence}` 3.4 restate it); reference: Ribet83
Theorem 2.2, AU96 Lemma 2.1, ARS12 Section 3 (as cited); `\Cref{ch:hecke}` 4.1, 5.2 to 5.4, `\Cref{ch:modules}` 5.8, 9.6; paper use:
Lemma lem:crit, Lemma lem:old, Lemma lem:hecke, Theorem thm:twist, Theorem thm:quant Step 1).
Statement. Let `phi_f : T -> Z`, `I = ker phi_f`, `J = Ann_T(f^perp)`. Then `T/(I + J)` is cyclic of order `r_E`; equivalently `r_E` generates
the congruence ideal `phi_f(J) = phi_f(Ann_T I)`. Consequently, if `g in S_2(Gamma_0(N)) tensor Qbar` is a normalised eigenform for all of
`T`, orthogonal to `f`, with coefficients in the ring of integers `O` of a number field, and `lambda | l` with `a_n(g) = a_n(f) mod lambda`
for every `n`, then `l | r_E`. The same over `Z_l` with the `l`-part of `r_E`. (In this lemma `I` and `J` are the paper's letters; in Lemma
lem:ddt417 the paper's `I` is the annihilator, B-C13(c).)
Expanded proof steps: (1) `T tensor Q = Q x T'` with `T'` faithful on `f^perp`. The `f`-line and `f^perp` are `T`-stable: for `(n, N) =
1`, `T_n` is self-adjoint for the Petersson product (`\Cref{ch:hecke}` 5.2); for `p | N`, `U_p^dagger = w_N U_p w_N^{-1}` (`\Cref{ch:hecke}`
5.3), and `f` is an eigenvector of `w_N`; so `f` is an eigenvector of every `T_n^dagger`, and the orthogonal complement of a line stable
under all `T_n` and all `T_n^dagger` is `T`-stable (`\Cref{ch:hecke}` 5.4). Hence `I = T cap (0 x T')`, `J = T cap (Q x 0)`, `I cap J = 0`,
`T/(I + J) = Z/phi_f(J)`, cyclic of order `r'`. (2) The pairing `S_2(Gamma_0(N); Z) x T -> Z`, `(g, t) -> a_1(tg)`, is perfect
(`\Cref{ch:hecke}` 4.1); the forms killed by `I` are `Z f`, those killed by `J` are `L = f^perp cap S_2(Gamma_0(N); Z)`. (3) Dualising `T -> T/I x
T/J` (cokernel `T/(I + J)`) gives `[S_2(Z) : Z f + L] = r'`. (4) `S_2(Z)/(Z f + L)` embeds in `Q f/Z f`, so it is cyclic, generated by `h` with
projection `f/r'`; `r' h = f + g_0` gives `r' <= r_E`, and a congruence modulo `r_E` gives an element of order `r_E`, so `r_E | r'`. (5) `phi_g`
kills `J` and `phi_g = phi_f mod lambda`, so `I + J` lies in the maximal ideal `ker(T -> O/lambda)` and `l | r_E`. (6) Over `Z_l` verbatim.
**Commentary (B12, D5; book-internal, not about the paper).** The first version of this item wrote adjoints with a star and
contained a sentence that corrected itself midway. The paper's own sentence ("`f` is an eigenvector of the adjoints of the `T_n` as
well") is right; the book justifies it by the clean statement of step (1), with adjoints written `T_n^dagger`, `U_p^dagger` (B-C4(d)).

**A3.3 `lem-old`** (lemma; *proved here* (the five prime-by-prime cases; full proof `\Cref{ch:modgalrep}` 8.3); reference:
Atkin-Lehner Theorem 3, Edixhoven92 Section 2, DDT Theorem 3.1(e) (as cited); `\Cref{ch:hecke}` 6.3, 6.4, 7.1, 7.2, 7.4,
`\Cref{ch:modgalrep}` 4.2, `\Cref{ch:galois}` galois:chebotarev-brauer-nesbitt, `\Cref{ch:reps}` 3.7, 5.2; paper use: Lemma lem:old,
cases (a), (b), (c)).
Statement. Let `h` be a newform of weight `2` on `Gamma_0(M)`, `M | N`, `h != f`, coefficients in `O`, and `lambda | l` with `a_p(h) = a_p(f) mod
lambda` for all `p` not dividing `l N`. Assume `p` does not divide `M` for every `p || N` at which `rho bar` is unramified. Then, after
enlarging `O` and `lambda`, the span of the `h(dz)`, `d | N/M`, contains an eigenform `g` as in Lemma lem:crit; so `l | r_E`.
Expanded proof: as in the paper, with the `U_p`-structure of the old span from `\Cref{ch:hecke}` 7.1, 7.2 (eigenvalues `alpha_p, beta_p`
and `0`, the eigenvectors `h - beta_p h(pz)`, `h - alpha_p h(pz)` and the depleted forms; `U_p` is not semisimple when `0` is repeated,
`\Cref{ch:hecke}` 7.3), and the five cases: `p` not dividing `l N`; `p = l` (Deligne-Fontaine via Edixhoven: `a_l mod lambda` is determined
by `rho bar|_{D_l}`, `\Cref{ch:modgalrep}` 4.2); `p^2 | N` (`a_p(f) = 0`; Atkin-Lehner Theorem 3; `mu_p = 0`); `p || N` unramified (one of
`alpha_p, beta_p` is congruent to `a_p(f)`, via DDT 3.1(e): eigenvalues `a_p(f) p`, `a_p(f)` of `rho bar(Frob_p)`); `p || N` ramified (non-split
extensions have a unique stable line).
**Commentary (important_notes.md point 10).** "`rho bar_h = rho bar` by Chebotarev and Brauer-Nesbitt, `rho bar` being irreducible":
irreducibility gives only equal semisimplifications over a common finite field. Insert "hence absolutely irreducible, complex
conjugation having distinct eigenvalues `+1` and `-1`" (`\Cref{ch:reps}` 3.7, `\Cref{ch:galrep}` 1.4) and "over a common finite extension
of `F_l`".

**A3.4 `thm-optimal-level`** (theorem; *stated; reference*; reference: DDT Theorem 3.15 (Ribet90, Carayol89, Diamond95, as
cited); `\Cref{ch:modgalrep}` 6.2, 6.4, 6.5, `\Cref{ch:galrep}` 6.1, 6.2, 10.1; paper use: the optimal-level paragraph of Section 3,
cases (a), (b), (c), the remark after the example).
Statement. Let `l` be odd and `sigma bar : G_Q -> GL_2(Fbar_l)` irreducible and modular, absolutely irreducible on `Gal(Qbar/Q(sqrt(-3)))`
if `l = 3`. Then `sigma bar` arises from a newform of weight `2` and level `N(sigma bar) l^{delta(sigma bar)}` with nebentypus of order prime
to `l`, `N(sigma bar)` the Serre conductor and `delta(sigma bar) = 0` when `sigma bar|_{D_l}` is good. Corollary (`\Cref{ch:modgalrep}` 6.5): for
`sigma bar = rho bar_{E',l}` with `E'` of conductor prime to `l`, `sigma bar` arises from a newform on `Gamma_0(N(sigma bar))`. Also `N(rho bar_{E',l})
| N(E')` (Carayol), and `N(sigma bar)` is prime to the primes where `sigma bar` is unramified. Case `q || N`, unramified at `q`: Ribet's theorem
(`\Cref{ch:modgalrep}` 6.2).

**A3.5 `proof-thm-qual`** (theorem (proof of Theorem thm:qual, cases (a), (b), (c)); *proved here*; reference: paper Section
sec:proof; `\Cref{ch:modgalrep}` 9.2, 9.3, 2.7, 3.8, `\Cref{ch:hecke}` 6.3, 9.2; paper use: Theorem thm:qual).
Notation (B-C13(d)): `f^chi` is the newform twist (`rho_{f^chi} = rho_f tensor chi`), `f tensor chi = sum chi(n) a_n(f) q^n` the naive twist,
and `f tensor chi` is the `q`-depletion of `f^chi`; `(g tensor chi) tensor chi = g^{q}`, the `q`-depletion of `g`.
Common start: `r = r_{E_0}`; as `l` does not divide `N`, `v_l(deg varphi_{E_0}) = v_l(r)`, so it suffices to produce `h` as in Lemma lem:old.
Case (a): `q^2 || N`, `l = 3`, `q >= 5` or `q = 2`; Lemma lem:IV (A2.2; at `q = 2` A1.8) gives `v_q(N(rho bar)) = 1`, so `M = N(rho bar) | N/q`;
the optimal-level theorem gives `g` on `Gamma_0(M)` with `rho bar_g = rho bar`; take `h = g` (`h != f` by levels); `p` does not divide `M`
whenever `rho bar` is unramified at `p`; Lemma lem:old gives `3 | r`.
Case (b): `q^2 || N`, `l = 3`, type `II/II^*` at `q >= 5`; `chi = chi_{q*}`, `E' = E^{(q)}` of type `IV^*/IV` at `q`, the same types elsewhere,
conductor `N`; its newform is `f_{E'} = f^chi`, and here `f^chi = f tensor chi` because `a_q(f^chi) = 0` (`q^2 | N`); this is NOT Atkin-Li,
which needs `q^2` not dividing the level. `rho bar tensor chi` satisfies the hypotheses (irreducibility and the condition over `Q(sqrt(-3))`
are twist-invariant). Lemma lem:IV for `E'`: `M = N(rho bar tensor chi)` has `v_q(M) = 1`, `M | N/q`; the optimal-level theorem gives `g` on
`Gamma_0(M)` with `a_p(g) = chi(p) a_p(f) mod lambda`, `p` not dividing `3N`; as `q || M`, `h = g^chi` is a newform on `Gamma_0(Mq)` (Atkin-Li),
`Mq | N`, `a_p(h) = chi(p)^2 a_p(f) = a_p(f) mod lambda`. `h != f`: if `h = f` then `f tensor chi = h tensor chi = g^{q}`, so the newforms `f_{E'}`
and `g` have the same `a_p` for all `p != q`, hence `f_{E'} = g` by strong multiplicity one (`\Cref{ch:hecke}` 6.3), contradicting the levels
`N != M`. Hypothesis of Lemma lem:old: as in the paper. `3 | r`.
Case (c): type `I_n^*` at odd `q != l`, `l | n`, `q^2 || N`; `E' = E^{(q)}` has type `I_n` at `q`, conductor `N/q`; `f = (f_{E'})^chi = f_{E'} tensor
chi` (Atkin-Li, `q || N/q`), while `f tensor chi = f_{E'}^{q}` is the `q`-depletion of `f_{E'}`, not a newform (`a_q(f_{E'}) = +-1`); so the paper's
`f'` must be read as `f_{E'} = f^chi`. Lemma lem:tamagawa-exp for `E'`: `rho bar tensor chi` is unramified at `q` (`l | n`), so `M = N(rho bar tensor
chi)` is prime to `q`, `M | N/q^2`; Ribet's theorem gives `g` on `Gamma_0(M)` with `a_p(g) = chi(p) a_p(f) mod lambda`; `h = g^chi` is a newform on
`Gamma_0(M q^2)`, `M q^2 | N`, congruent to `f` at `p` not dividing `l N`. `h != f`: if `h = f` then `g^{q} = h tensor chi = f tensor chi = f_{E'}^{q}`, so
`g = f_{E'}` by strong multiplicity one, of levels `M != N/q`. `l | r`.
**Commentary (important_notes.md points 20 and 54; B18).** In cases (b) and (c) the paper argues "`h != f`: otherwise `g = h tensor chi
= f tensor chi = f'`". But `h tensor chi` is the `q`-depletion of `g`, not `g` (point 20); and in case (c) the paper's "`f' = f tensor chi` is a
newform of weight `2` on `Gamma_0(N/q)`" is false, since `E'` is multiplicative at `q` and its newform has `a_q = +-1` while `f tensor chi` has
`a_q = 0` (point 54; check: 539c1 twisted by `-7` is 77c1, type `I_3` at `7`, `a_7 = -1`). The conclusion `h != f` is right, by strong
multiplicity one as above. The book writes `f' = f_{E'} = f^chi` and gives the corrected one-line argument; the first version of this
outline repeated the slip and argued case (c) inconsistently (B18), which is now removed.
Why `I_0^*` (and `I_n^*` with `l` not dividing `n`) is not in Theorem thm:qual (one sentence in the book; `\Cref{ch:modgalrep}` 9.3): the
lowered form may be `f_{E'}` itself, and then `h = f`; Theorem thm:quant reaches these terms by level raising instead.

**A3.6 `example-abc`** (example; worked verification with PARI and Sturm's bound; reference: paper Example after case (c);
`\Cref{ch:modgalrep}` 9.4, `\Cref{ch:modforms}` 11.3, 11.5, `\Cref{ch:reduction}` 8.5, `\Cref{ch:computation}` 6.1, 6.3, 6.4; paper use:
the example of Section 3).
Statement (the paper's three congruences, with the curve-level identifications corrected per B8 and B20). (b) 121a1 (type `II`
at `11`): its twist by `-11` is 121c2 (type `IV^*`; the optimal curve 121c1 of that class has type `IV`), whose mod `3` representation has
Serre conductor `11` and is that of 11a1; `f_{11a} tensor chi_{-11}` is the newform of the class 121d (121d2 is the twist of 11a1, type `I_5^*`;
121d1 the twist of 11a3); `f_{121a} = f_{121d} mod 3` for EVERY `n` (both in `S_2(Gamma_0(121); Z)`, Sturm bound `22`); `deg varphi_{121a1} = 6`,
`e_3(E, 11) = v_3(12) = 1`, bound attained. (c) at `l = 3`: 539c1, type `I_3^*` at `7`; its twist by `-7` is 77c1 (conductor `77`, `I_3` at `7`);
`f_{11a} tensor chi_{-7}` is the newform of the class 539d (539d2 is the twist of 11a1); `f_{539c} = f_{539d} mod 3` for every `n` (Sturm bound
`112`); `deg = 288 = 2^5 3^2`; `e_3(E, 7) = v_3(48) = 1`, `t_3(E, 7) = 1`, bound `2`, attained. (c) at `l = 5`: 980i1, type `I_5^*` at `7`; its twist by
`-7` is 140b1 (`I_5` at `7`); the twist of 20a1 by `-7` is 980g2 and `f_{20a} tensor chi_{-7}` is the newform of the class 980g, NOT 980i; the
congruence is `f_{980i} = f_{980g} mod 5` for every `n` (Sturm bound `336`); `deg = 2880 = 2^6 3^2 5`.
PARI values (`\Cref{ch:computation}` R1): `rule(121a1, 3) = [1, 1]`; `rule(539c1, 3) = [2, 2]`; `rule(980i1, 3) = [2, 2]` (with `e_3(E, 2) = 1`
from type `IV^*` at `2`, a theorem, and `e_3(E, 7) = 1`); `rule(980i1, 5) = [1, 1]` (`t_5(E, 7) = 1`). Level-raising conditions visible:
`a_7(11a1) = -2`, `(7 + 1)^2 - 4 = 60`, divisible by `3`; `a_7(20a1) = 2`, `60` divisible by `5`.
**Commentary (important_notes.md point 46, optional strengthening).** The paper checks the congruences for `p < 500` or `p < 1000`,
excluding a few primes. Both sides lie in the same `S_2(Gamma_0(N); Z)`, so Sturm's bound (`22`, `112`, `336`) turns the finite check
into a proof for every `n`, the excluded primes included (`\Cref{ch:modforms}` 11.5). The book says "for all `n`, by Sturm's bound".
**Commentary (important_notes.md point 21).** `5 | 980`, so the 980i1 example is outside the hypothesis `l` not dividing `N` of
Theorem thm:qual (and of Theorem thm:main): it illustrates the congruence mechanism of case (c), not the theorem; the level of `g` is
`20 = 4 * 5` because `rho bar_{140b1,5}` is not finite at `5` (`\Cref{ch:modgalrep}` 9.4(iii)). The book says so and points to the
remark after the example.
**Commentary (B8, B20; book-internal).** The first version of this outline paired curves within classes loosely (121d1 for the
twist of 11a1; "twist of 11a by `-7`" for 539d1). The class-level statements are right, and every quantity at `l = 3` depends only on
the class; the book names the curves as above, from `\Cref{ch:reduction}` 8.5.

**A3.7 `rem-l-divides-N`** (example (the paper's remark on `l | N` and 99A1); *stated*, with recomputed data; reference: ARS12
Table 1; `\Cref{ch:modgalrep}` 9.5, `\Cref{ch:moddeg}` 8.5, 9.7; paper use: the remark after the example).
Statement. `l` not dividing `N` is used (i) in the optimal-level theorem (`delta = 0`, weight `2`), (ii) in Lemma lem:old at `p = l`, (iii) to
pass from `r` to `deg varphi`, where only `l^2` not dividing `N` is needed and cannot be dropped: 99A1 (`N = 9 * 11`) has `deg = 4`, `r = 12`
(both recomputed, `\Cref{ch:moddeg}` 8.5 and `\Cref{ch:hecke}` 11.2, important_notes.md B19); further instances 726a1 (`r = 1584`, `deg 144`,
gap at `11`, point 58) and 539d1 (`r = 504`, `deg 72`, gap at `7`, point 62). At 99a1 and `l = 3`, `H^1(X_0(99), Z_3)_m` is not free over `T_m`
(`\Cref{ch:moddeg}` 9.7). The data show the conclusion of Theorem thm:qual for curves with `l || N` or `l^2 | N`.
**Commentary (important_notes.md point 55).** The paper adds that the data show the conclusion "at `q = 3` in cases (a) and (b),
where Lemma lem:IV does not apply because the ramification is wild". In those cases `q = l = 3`, so `3 | N` and the curves are outside
Theorem thm:qual in any case; the obstruction is first that `q = l` (inertia at `3` acts on `T_3 E` through an infinite group), and
only secondarily wildness. The book says "where `q = l`".

### A4. The paper's Section 4: the congruence ideal and the adjoint Selmer group (Sections 21.10 to 21.13)

**A4.1 `constr-dfg-lattice`** (construction; *stated; reference* (the objects of DFG04 read for weight `2`, trivial character;
DFG04 Sections 1.5.3, 1.6.1, 1.6.2, 1.7.3, 1.8.2, (13), (14) verified against the published text, `\Cref{ch:congruence}` 7.1, 7.3);
reference: DDT Section 4.4; `\Cref{ch:curves}` 10.3, `\Cref{ch:moddeg}` 3.4, 4.4, 9.1, `\Cref{ch:congruence}` 5.1 to 5.4,
`\Cref{ch:modules}` 9.4; paper use: Section 4.1, Lemma lem:hecke, Theorem thm:quant Step 2).
Statement. Let `f` be a newform of weight `2` on `Gamma_0(M)` with rational coefficients, `lambda = l` not dividing `2M`, `Sigma` a finite set of
primes. `M^Sigma = M prod_{p in Sigma} p^{delta_p}`, `f^Sigma = sum_{(n, Sigma) = 1} a_n(f) q^n` the `Sigma`-depleted form (DFG04 Section 1.7.3;
`\Cref{ch:hecke}` 7.4), an eigenform of the full Hecke algebra of level `M^Sigma` with `U_p f^Sigma = 0` for `p in Sigma`. The integral structure
`M(M^Sigma, 1)_{!,lambda}` agrees with `H^1(X_0(M^Sigma), Z_l)` after localisation at the non-Eisenstein maximal ideals (A4.1
Commentary). `M_{f^Sigma,lambda} = H^1(X_0(M^Sigma), Z_l)[ker phi_{f^Sigma}]`, the kernel lattice (saturated, free of rank `2`). For `Sigma` empty
and `f = f_E`, `E` optimal: `M_{f,lambda} = varphi_E^* H^1(E, Z_l) = Hom(T_l E, Z_l) = T_l E(-1)` exactly, as `G_Q`-lattices, with no
irreducibility hypothesis (`\Cref{ch:moddeg}` 9.1; important_notes.md point 40), and `ad M_{f,lambda} = ad T_l E` (C3). The pairing
`hat delta_!(x, y) = <x, w y>` is the cup product composed with the Atkin-Lehner involution `w = w_{M^Sigma}` (DFG04's `[UwU]_omega` in weight
`2`, with no scalar, `N^{k-2} = 1`); it is perfect and alternating, and every `T_n` and `U_p` is self-adjoint for it, because `w T_n w^{-1}` is the
cup-product adjoint `T_n^dagger` (`\Cref{ch:moddeg}` 3.3, 3.4). Alternating: `w` preserves the cup product, so `<y, w x> = <w y, x> = -<x, w y>`.
The naive `Sigma`-finite congruence ideal `eta^Sigma_{f,lambda}` is the ideal of values of `hat delta_!` on `M_{f^Sigma,lambda}` (DFG04: the image of
`wedge^2`, verified); equivalently the Gram determinant on a basis is `(eta^Sigma_{f,lambda})^2` up to a unit (a rank-two alternating form has
Gram matrix `(0, a; -a, 0)`, `\Cref{ch:modules}` 9.4).
**Commentary (important_notes.md points 26, 40; B3, D6).** Section 4.2 of the paper says "the lattice `M_{f,lambda}` of DFG04 and `T_l E`
are homothetic when `rho bar` is irreducible". They live in dual representations (`V_l E^vee` versus `V_l E`, determinants `chi_l^{-1}`
and `chi_l`; DFG04 (18): the geometric Frobenius on `M_{f,lambda}` has the characteristic polynomial of `H^1`, verified). Correct
statement: for the optimal curve `M_{f,lambda} = varphi_E^* H^1(E, Z_l) = T_l E(-1) = (T_l E)^vee`, an equality, and for any curve of the class
the dual of `T_l E` up to homothety when `rho bar` is irreducible; the conclusion "their adjoints coincide" holds because `ad(T^vee) = ad T
= ad(T(-1))`. The book states it this way.
**Commentary (important_notes.md point 73, item 1 and item 3).** The paper says "The integral structure `M(M^Sigma, 1)_{!,lambda}` is
`H^1(X_0(M^Sigma), Z_l)`". DFG04 define it as the image of the `U_0(N)`-invariants of compactly supported cohomology of the full-level
curve; it agrees with `H^1(X_0(M^Sigma), Z_l)` after localisation at non-Eisenstein maximal ideals, which is all the paper uses
(definitions certain; the Eisenstein nature of the comparison cokernel in general is the Chapter 20 outline's sketch, medium-high).
DFG04's pairing is the cup product on `X_0(N)` times `1/2`, a unit for `l` odd. The book rewords the sentence accordingly and
mentions the factor `1/2` (`\Cref{ch:congruence}` 5.2, 5.3).

**A4.2 `thm-dfg14`** (theorem; *stated; reference*; reference: DFG04 Proposition 1.4(c) (verified, `\Cref{ch:congruence}` 7.3);
`\Cref{ch:congruence}` 6.1 to 6.4, `\Cref{ch:modgalrep}` 7.2 to 7.4, `\Cref{ch:lfunctions}` 9.7; paper use: Theorem thm:dfg14,
proof of Theorem thm:main, Theorem thm:quant Step 3, the remark after Theorem thm:quant).
Statement. If `rho bar_f` is irreducible (and `l` does not divide `2M`, DFG04's standing hypothesis of Section 1.7.3), then
`eta^Sigma_{f,lambda} = eta^empty_{f,lambda} prod_{p in Sigma} L_p^nv(A_f, 1)^{-1}`. Reading: additive `p in Sigma`: factor `1`; good `p`: Wiles's
level-raising factor `(1 - (alpha/beta) p^{-1})(1 - p^{-1})(1 - (beta/alpha) p^{-1}) = ((p - 1)/p)((p + 1)^2 - a_p^2)/p^2`; multiplicative `p`: `1 - p^{-2}`.
Proof idea: Ihara's lemma (`\Cref{ch:modgalrep}` 7.4) and the degeneracy maps; one paragraph, with reference.

**A4.3 `lem-ddt417`** (lemma; *proved here* in corrected form (full proof `\Cref{ch:congruence}` 4.3); reference: DDT Lemma 4.17
(inequality half, as cited); `\Cref{ch:modules}` 5.5, 9.2, 9.3, 11.1, 11.3, 11.6; paper use: Lemma lem:ddt417, Lemma lem:hecke, Theorem
thm:quant Step 2).
Statement. Let `O` be a DVR with finite residue field (or state it with lengths), `T` a commutative `O`-algebra, finite and free as an
`O`-module, acting on an `O`-module `L` free of finite rank with a perfect `O`-bilinear pairing for which every element of `T` is
self-adjoint; `pi : T -> O` a surjective homomorphism, `wp = ker pi`, `I = Ann_T(wp)`, `eta = pi(I)`; suppose `L[wp]` is free of rank `d` with
Gram determinant `Delta != 0`. Then `eta^d subset Delta O`, i.e. `d v(eta) >= v(Delta)`, with equality if `L` is free over `T`.
Expanded proof: (0) If `eta = 0` there is nothing to prove. (1) `wp cap I = 0`: take `t in I` with `pi(t)` a generator of `eta`; for `x in wp cap
I`, `t x = 0` (`t` kills `wp`) and `(pi(t) - t) x = 0` (`pi(t) - t in wp`, `x` kills `wp`), so `eta x = 0` and `x = 0`, `T` being torsion-free. Hence
`L[wp] cap L[I] = 0`. (2) For `x in L`, `t x in L[wp]` and `(pi(t) - t) x in L[I]`, so `Q = L/(L[wp] + L[I])` is killed by `eta`. (3) `L[wp]` is
saturated, so `L -> Hom(L[wp], O)` is onto with kernel `L[wp]^perp` (`\Cref{ch:modules}` 9.2). (4) `L[wp]^perp = L[I]` (self-adjointness, as in
the paper). (5) `Q = coker(L[wp] -> Hom(L[wp], O))`, of length `v(Delta)` (`\Cref{ch:modules}` 9.3), generated by `d` elements and killed by
`eta`: `v(Delta) <= d v(eta)`. (6) If `L = T^d` then `Q = (T/(wp + I))^d = (O/eta)^d` (`Ann(I) = wp`, by the same decomposition).
**Commentary (important_notes.md point 19, as corrected).** The paper's proof begins "Since `L` is torsion-free and `wp cap I = 0`"
without proving `wp cap I = 0`. The reason is NOT that `T` is reduced (the full Hecke algebra can have nilpotents: `U_2` at level `88` on
the span of `f_11(z), f_11(2z), f_11(4z), f_11(8z)`, `\Cref{ch:hecke}` 7.3, 11.1); it is the two-line argument of step (1), valid when `eta !=
0`, the case `eta = 0` being trivial. The book adds those two lines.
**Commentary (important_notes.md point 38).** The lemma is stated for an arbitrary DVR but counts `#O/Delta` and `#(O/eta)^d`, finite
only for a finite residue field; for `O = Z_l`, the only case used, this is fine. The book states it with lengths (B-C10).

**A4.4 `lem-hecke`** (lemma; *proved here* in the strengthened form (equality); reference: ARS12 Theorem 2.2 (as cited);
`\Cref{ch:moddeg}` 9.3 to 9.5, `\Cref{ch:congruence}` 5.6, `\Cref{ch:modules}` 10.3; paper use: Lemma lem:hecke, proof of Theorem
thm:main, Theorem thm:quant Step 4).
Statement as in the paper. Let `E` be `X_0(N)`-optimal, `l` odd with `l` not dividing `2N` and `rho bar` irreducible, `m` the maximal ideal of
`T_l = T tensor Z_l` containing `l` and `ker phi_f`. Then `v_l(deg varphi_E) = v_l(r_E) >= v_lambda(eta^empty_{f,lambda})`, with equality if
`H^1(X_0(N), Z_l)_m` is free over `T_m`.
Statement as the book gives it (important_notes.md points 39, 56, 73; `\Cref{ch:moddeg}` 9.5). For `E` optimal and `l` odd with `l`
not dividing `N`: `v_l(deg varphi_E) = v_l(r_E) = v_l(ideal of values of hat delta_! on H^1(X_0(N), Z_l)[ker phi_f])`, with no
irreducibility and no freeness hypothesis; when moreover `l` does not divide `2N` and `rho bar` is irreducible, this ideal is DFG04's
`eta^empty_{f,lambda}` (their integral structure agrees with `H^1(X_0(N), Z_l)` at the non-Eisenstein `m`, A4.1), so `v_l(deg varphi_E) =
v_lambda(eta^empty_{f,lambda})`.
Expanded proof: (1) `v_l(deg) = v_l(r_E)`: ARS12 Theorem 2.2 (`l^2` does not divide `N`). (2) The ideal of values of `hat delta_!` on
`M_{f,lambda} = varphi_E^* H^1(E, Z_l)` is `deg varphi_E Z_l`: by the projection formula `<varphi^* a, varphi^* b> = <a, varphi_* varphi^* b> = deg
varphi_E <a, b>_E`, the cup product on `E` is unimodular, and `w_N` acts on `M_{f,lambda}` by the Atkin-Lehner sign `+-1` (`\Cref{ch:moddeg}` 9.2,
9.3). (3) This is DFG04's `eta^empty_{f,lambda}` (A1.4 Commentary). The paper's route, kept as a remark: `r_E Z_l = phi_f(Ann_T ker phi_f) Z_l`
(Lemma lem:crit); `T_l = prod T_{m'}`; the congruence ideal can be computed in `T_m`; Lemma lem:ddt417 with `L = H^1(X_0(N), Z_l)_m`, which
gives `>=` and needs freeness for `=`.
**Commentary (important_notes.md point 35; B3).** The paper says "the other local factors of `T tensor Z_l` are killed by `phi_f` and lie
in the annihilator". They lie in the KERNEL `ker phi_f = wp`, not in `Ann(wp)` in general (if `e'` is the idempotent of another local
factor, `e' wp = wp cap T_{m'}`, usually nonzero). The conclusion is right: `phi_f` factors through the projection to `T_m`, and the
annihilator of `wp` decomposes along the idempotents, `Ann(wp)` being the annihilator of `wp_m` inside `T_m`. The book writes this
(`\Cref{ch:modules}` 10.3).
**Commentary (important_notes.md point 36).** Applying Lemma lem:ddt417 to `L = H^1(X_0(N), Z_l)_m` needs the pairing to be perfect on
the `m`-component: the idempotent `e_m` is self-adjoint (all Hecke operators are), so `H^1` splits orthogonally into its local components
and the pairing is perfect on each. One sentence in the book.
**Commentary (important_notes.md point 39).** The inequality and the freeness clause are superseded by the equality above; the
book prints the paper's argument as a remark and proves the equality.

**A4.5 `rem-free`** (proposition (the paper's Remark rem:free); *proof sketched here*; reference: Tilouine97, Ribet-Stein Theorem
3.5, Mazur77 (as cited); `\Cref{ch:moddeg}` 10.1 to 10.4, 11.3, `\Cref{ch:congruence}` 5.7, `\Cref{ch:modules}` 11.4, 11.5; paper use:
Remark rem:free).
Statement. For `l` not dividing `2N` and `m` non-Eisenstein, `J_0(N)[m]` is two-dimensional over `T/m` (Ribet-Stein Theorem 3.5 for `J_1(N)`,
the exception "Serre weight `l`" not occurring in weight `2` with `l` not dividing `N`, and `J_0(N)[m] -> J_1(N)[m']` injective because its
kernel lies in the Shimura subgroup, which is Eisenstein); hence `T_m` is Gorenstein and `H^1(X_0(N), Z_l)_m = T_m^2` (Tilouine;
`\Cref{ch:moddeg}` 10.3). Consequence: equality in Lemma lem:ddt417 for `L = H^1(X_0(N), Z_l)_m`, an independent proof of `v_l(r_E) = v_l(deg
varphi_E)` at such `l`.
Role after the corrections: none in the proof of Theorem thm:main (A4.4) and none in the equality of Theorem thm:quant (A4.16, point
74). It explains WHY Hecke and cohomological congruence ideals agree in the paper's range, and it fails for `l | N` (99a1 at `l = 3`:
`H^1(X_0(99), Z_3)_m` is not free, `\Cref{ch:moddeg}` 9.7).
**Commentary (important_notes.md point 41).** Identifying `T_l J_0(N)` with `H^1(X_0(N), Z_l)` as Hecke modules uses Poincare duality
composed with `w_N`; this identification is not Galois-equivariant, but freeness over `T_m` transfers. One clarifying clause.

**A4.6 `setup-dfg-selmer`** (definition; *stated; reference*; reference: DFG04 Section 2.1 and (31) (verified,
`\Cref{ch:congruence}` 7.1 to 7.3); `\Cref{ch:blochkato}` 6.3, 6.6, 10.1, `\Cref{ch:galrep}` 8.6; paper use: Section 4.2, Theorem
thm:dfg37, Theorem thm:dfg27, Lemma lem:dfg21, Lemma lem:h0, Remark rem:ns).
Statement. `f = f_E`, `Sigma = {q : q | N}`, `lambda = l` not dividing `2N`, `A = A_{f,lambda} = ad T` (equal to `ad M_{f,lambda}`, `M_{f,lambda}` being
`T_l E(-1)`, the dual of `T_l E`, A4.1), `W = A tensor Q_l/Z_l`, `T^D = Hom(A, Z_l(1)) = A(1)` (trace form), `V^D = T^D tensor Q_l`, `W^D = V^D/T^D`.
`H^1_f(Q, W)` is the Bloch-Kato Selmer group; `H^1_Sigma(Q, W)` has no condition at `p in Sigma`, the Bloch-Kato condition at `l`, and the
unramified condition elsewhere (DFG04 use `H^1_ur` outside `Sigma cup {l}`, the same for `Sigma` containing the primes dividing `N`). `S_f =
{lambda : lambda | Nk!` (that is `2N` for `k = 2`), or `M bar_{f,lambda}` is not absolutely irreducible on `G_F`, `F = Q(sqrt(l*))}` (DFG04 (31),
verified); the hypothesis of Theorem thm:main is `l` not in `S_f`.
Fact (important_notes.md point 47; `\Cref{ch:galrep}` 8.2, 8.6): for `l` not dividing `2N`, `l` not in `S_f` iff `E[l]` is irreducible and
`h_l(E) = 0`, iff `E[l]` is irreducible and not (`l = 3` and image 3Ns). For `l >= 5` not dividing `N`, a dihedral `rho bar` induced from
`Q(sqrt(l*))` is impossible (restrict to inertia at `l`: the characters `{omega, 1}` (ordinary) or `{omega_2, omega_2^l}` (supersingular)
cannot be permuted by the twist by `chi_{l*}|_{I_l} = omega^{(l-1)/2}` unless `l = 3`); for `l = 3` the failure is exactly image 3Ns, and
those curves are ordinary at `3`.
**Commentary (important_notes.md point 26; B3).** The first version of this item repeated "homothetic to `T_l E`"; corrected as in A4.1.

**A4.7 `thm-dfg37`** (theorem; *stated; reference*; reference: DFG04 Theorem 3.7 = Theorem 0.2 (verified, including `l = 3`,
`\Cref{ch:congruence}` 7.2, 7.4, 7.5); `\Cref{ch:congruence}` 7.3, 8.1 to 8.5, `\Cref{ch:blochkato}` 14.5; paper use: Theorem thm:dfg37,
proof of Theorem thm:main, Remark rem:ns, Open question 2).
Statement. If `l` is not in `S_f`, then `H^1_Sigma(Q, W)` is finite, of length `v_lambda(eta^Sigma_{f,lambda})`. (DFG04 Theorem 3.7: for a finite
set `Sigma` not containing `l` such that `M_{f,lambda}` is minimally ramified outside `Sigma`; Theorem 0.2: for `Sigma` containing the primes
dividing `N`, `lambda` not in `S_f` and not dividing any prime of `Sigma`; the set of primes dividing `N` qualifies.) Idea: Taylor-Wiles;
`H^1_Sigma` is dual to the cotangent space of `R_Sigma`, `R_Sigma = T_Sigma` complete intersection, and the numerical criterion identifies the
length with the congruence ideal (`\Cref{ch:congruence}` 8.5).
**Commentary (important_notes.md point 73, open check Q1; B26).** The first version marked "covers `l = 3`?" as unchecked. Settled:
`S_f` excludes only `lambda | 2N` and the residually induced case; the local condition at `l` is defined through extensions of short
objects (DFG04 Proposition 2.2, Corollary 2.3, needing only `l > 2`), the Taylor-Wiles conditions `2 <= k <= l - 1` hold at `l = 3` for
`k = 2`, and the extra condition at `3` (absolute irreducibility on `G_{Q(mu_3)}`) is the `S_f` condition. So Theorem thm:main at `l = 3`
(with `3` not dividing `N`, image not 3Ns) has its Taylor-Wiles input.

**A4.8 `thm-dfg27`** (theorem; *stated; reference*; reference: DFG04 Theorem 2.7 (verified: "Conjecture 2.6 holds for `A_f` and `B_f
= A_f(1)` if `lambda` is not in `S_f`"); `\Cref{ch:blochkato}` 10.2, 3.3; paper use: Theorem thm:dfg27, proof of Theorem thm:main).
Statement. If `l` is not in `S_f`, then `H^0(Q, V^D) = H^1_f(Q, V^D) = 0` (and the same for `A tensor Q_l`).
**Commentary (important_notes.md point 63).** The vanishing of `H^0(Q, V^D)` is automatic here: `H^0(Q_p, V^D) = 0` at every `p in Sigma`,
since the local Euler factor `L_p(A_f, 1)^{-1}` is nonzero (`\Cref{ch:blochkato}` 3.3, `\Cref{ch:galcoh}` 10.3(b)). So only `H^1_f(Q, V^D) = 0` is
needed from DFG04 Theorem 2.7. Observation, one sentence.

**A4.9 `lem-dfg21`** (lemma; *proved here* given Chapter 17's abstract comparison (`\Cref{ch:galcoh}` 10.3, 10.4;
`\Cref{ch:blochkato}` 10.4); reference: DFG04 Lemma 2.1 (verified); paper use: Lemma lem:dfg21, proof of Theorem thm:main, Remark
rem:ns, Conjecture conj:euler).
Statement. Suppose `H^0(Q, V^D) = H^1_f(Q, V^D) = 0`, and let `Sigma` be a nonempty finite set of primes containing every `p != l` at which
`W` is ramified. Put `H^1_f(Q_p, T^D) = iota^{-1} H^1_f(Q_p, V^D)`, `iota : H^1(Q_p, T^D) -> H^1(Q_p, V^D)`. Then there is an exact sequence
`0 -> H^1_f(Q, W) -> H^1_Sigma(Q, W) -> sum_{p in Sigma cup {infty}} H^1_f(Q_p, T^D)^* -> H^0(Q, W^D)^* -> 0`, `*` the Pontryagin dual.
(Here `iota` is the map `T -> V` on cohomology; the twist map of Theorem thm:twist is written `iota_S` in this chapter, B-C15(c).)
Attached facts (the paragraph after the lemma): for `p in Sigma`, `H^1_f(Q_p, V^D) = H^1_ur(Q_p, V^D) = (V^D)^{I_p}/(Frob_p - 1)` vanishes because
`det(1 - Frob_p^{-1} | (V^D)^{I_p}) = L_p(A_f(1), 0)^{-1} = L_p(A_f, 1)^{-1} != 0`; so `H^1_f(Q_p, T^D)` is the TORSION of `H^1(Q_p, T^D)`, a finite
group (the paper's wording is right and must not be simplified: `H^1(Q_p, T^D)` itself is infinite at `I_0^*` primes and at primes with cyclic
inertia where `chi(p) = 1`, important_notes.md B22). At `infty`, `H^1(R, T^D)` is killed by `2`, so `H^1_f(R, T^D) = 0` for `l` odd
(`\Cref{ch:galcoh}` 6.4).
Proof idea (Greenberg-Wiles / Poitou-Tate): compare "Bloch-Kato everywhere" with "no condition on `Sigma`"; the cokernel maps to `sum_{p in
Sigma} H^1(Q_p, W)/H^1_f(Q_p, W)`, dual to `sum H^1_f(Q_p, T^D)` by local duality; the defect is the dual Selmer group of `T^D` with strict
conditions at `Sigma`, whose divisible part vanishes by `H^1_f(Q, V^D) = 0` and whose finite part is `H^0(Q, W^D)`.
**Commentary (important_notes.md point 11).** "`det(1 - Frob_p | (V^D)^{I_p}) = L_p(A_f, 1)^{-1}`" holds with the GEOMETRIC Frobenius;
with the arithmetic one the determinant at a multiplicative prime is `1 - q^2`, a different number with the same valuation. The
book writes `Frob_p^{-1}`.
**Commentary (important_notes.md point 75).** DFG04's hypothesis is that `Sigma` contain every prime where `H^1_f(Q_p, W) !=
H^1_ur(Q_p, W)`; the paper's "every `p != l` at which `W` is ramified" implies it. The paper's statement is a correct special case.

**A4.10 `lem-fpr`** (lemma; first identity *proved here*; second identity *proved here* for the elliptic-curve adjoint and
*stated; reference* in general; reference: FPR94 I.4.2.2, DFG04 proof of Theorem 2.15 and (57) (verified: (57) is
`Tam^0_p(M_lambda) = Tam^0_p(M^D_lambda)` for `p != l`, general); `\Cref{ch:blochkato}` 7.2 to 7.5, 3.5, `\Cref{ch:lfunctions}` 9.6,
`\Cref{ch:cohomology}` inflation-restriction, procyclic-compact, lengths-in-exact-sequences; paper use: Lemma lem:fpr, proof of
Theorem thm:main, Remark rem:ns).
Statement. For `p in Sigma`, `Fitt_{Z_l} H^1_f(Q_p, T^D) = L_p(A_f, 1)^{-1} Tam_p(T^D)` and `Tam_p(T^D) = Tam_p(A)`; `L_p(A_f, 1)^{-1} = L_p(A_f(1),
0)^{-1}` is a nonzero `l`-adic integer, of valuation `e_l(E, p)` at an additive prime and `v_l(1 - p^{-2})` at a multiplicative one.
Expanded proof of the first identity (`\Cref{ch:blochkato}` 7.4): inflation-restriction with `G/I = Zhat` gives `0 -> X^I/(Frob - 1)X^I ->
H^1(G, X) -> H^1(I, X)^{G/I} -> 0` for `X = T^D`; `Frob - 1` is injective on `X^I` (the determinant is the nonzero Euler factor; geometric and
arithmetic give the same valuation) and the quotient is finite of length `v_l(L_p(A_f, 1)^{-1})`; taking torsion and adding lengths
gives the identity (`Fitt = l^{length}` for finite modules). Integrality: `P_p` has integral coefficients and `p^{-2}` is an `l`-adic unit.
The second identity: both sides are Fitting ideals of the Frobenius invariants of the same finite module `H^1(I, A)_tor`, with the action
twisted by `chi_l(Frob)`; DFG04 (57) in general, and for the adjoint of `E` directly: at potentially good primes both are `Z_l`
(`\Cref{ch:blochkato}` 9.3), at potentially multiplicative primes the count of A2.7 gives the same number for both (`\Cref{ch:blochkato}` 7.5).

**A4.11 `lem-h0`** (lemma; *proved here* in the corrected form; reference: `\Cref{ch:galrep}` 8.5 (proved there), 8.1, 8.3,
`\Cref{ch:blochkato}` 10.3, `\Cref{ch:reps}` 6.6, 10.5; paper use: Lemma lem:h0, proof of Theorem thm:main, Conjecture conj:euler,
Proposition prop:ns, Section sec:anomaly).
Statement as in the paper. Let `l` be odd with `rho bar` irreducible. Then `H^0(Q, W^D)` is finite, and it vanishes iff `rho bar` is not
isomorphic to `rho bar tensor chi bar_l`. For `l >= 5` it always vanishes; for `l = 3` it vanishes iff `rho bar_{E,3}` is absolutely irreducible on
`Gal(Qbar/Q(sqrt(-3)))`. Its length `h_l(E)` is the largest `k` such that `rho mod l^k = (rho tensor chi_l) mod l^k`, and for `E` without CM it
is finite.
Statement as the book gives it (points 5, 14). Same hypotheses, `E` with or without CM. Then `h_l(E) = 0` for every `l >= 5`, and
`h_3(E) <= 1` with equality iff `rho bar_{E,3} = rho bar_{E,3} tensor chi_{-3}` iff the image is `N_s(F_3)`.
Expanded proof. (1) `rho bar` is absolutely irreducible (irreducible, `l` odd, complex conjugation has distinct eigenvalues `+1, -1`).
(2) `H^0(Q, W^D)[l^k] = Hom_{G_Q}(T/l^k, (T/l^k)(1))`: `End(T)(1) = ad T(1) + Z_l(1)` and `H^0(Q, mu_{l^k}) = 0`, so no trace condition is needed. (3)
`k = 1`: a nonzero map is an isomorphism (Schur) and the space has dimension at most one; so `H^0(Q, W^D)` is cyclic, `Z/l^h`. (4) A
generator of `H^0[l^k]` is an isomorphism `rho mod l^k -> (rho tensor chi_l) mod l^k` (Nakayama), and conversely. (5) Determinants: such an
isomorphism gives `chi_l^2 = 1 mod l^k` on `G_Q`; `chi_l(G_Q) = Z_l^x`, so `l = 3`, `k = 1` (`4` is not `1 mod 9`). (6) `l = 3`: `chi bar_3 = chi_{-3}`; an
isomorphism `rho bar -> rho bar tensor chi_{-3}` exists iff `rho bar` is induced from `G_{Q(sqrt(-3))}` (over `F_9`) iff the image is `N_s(F_3)`
(Clifford theory for an index-two subgroup, `\Cref{ch:reps}` 6.6; Proposition prop:ns).
**Commentary (important_notes.md point 5).** The paper's finiteness sentence ("`rho = rho tensor chi_l` would force `a_p = 0` at all
primes inert in `Q(sqrt(l*))`") confuses the cyclotomic character `chi_l` with the quadratic character `chi_{l*}`: `rho = rho tensor chi_l`
is impossible for every `E` (it would give `p a_p = a_p`). The correct statement is (5), stronger and elementary, with no CM
hypothesis. Consequence for Section sec:anomaly: "`h_3(E) <= 1` because some prime `p < 1223` inert in `Q(sqrt(-3))` has `9` not dividing `a_p`"
is replaced by "`h_3(E) <= 1` by Lemma lem:h0" (the numerical check is valid but unnecessary). (B13: PLAN.md's Chapter 11 entry repeats
the flawed argument; this chapter must not.)
**Commentary (important_notes.md point 14).** Even read with `chi_{l*}`, the CM alternative cannot occur when `l` does not divide `N`: CM
by `Q(sqrt(l*))` needs class number one, so `l in {3, 7, 11, 19, 43, 67, 163}`, and the prime ramified in the CM field divides `N`. Moot by
point 5; one sentence.
**Commentary (important_notes.md point 10).** The Clifford step needs ABSOLUTE irreducibility; step (1) supplies it.

**A4.12 `proof-thm-main`** (theorem (the proof of Theorem thm:main, Section 4.3 of the paper), in the strengthened form;
*proved here* as an assembly; every input is a card entry: Lemma lem:hecke (A4.4), Theorem thm:dfg14 (A4.2), Theorem thm:dfg37 (A4.7),
Theorem thm:dfg27 (A4.8), Lemma lem:dfg21 (A4.9), Lemma lem:h0 (A4.11), Lemma lem:fpr (A4.10), Definition def:terms (A1.1), Lemma
lem:tamfactor (A2.7), Lemma lem:twist (A2.4); reference: `\Cref{ch:congruence}` 9.1, 9.2, `\Cref{ch:blochkato}` 8.4, 9.3, 9.4, 11.1;
paper use: Theorem thm:main, (eq:identity), (eq:thm)).
The steps, each with the hypothesis it uses.
Step 1 (degree to congruence ideal; uses optimality and `l` not dividing `2N`): `v_l(deg varphi_E) = v_lambda(eta^empty_{f,lambda})` (A4.4, an
EQUALITY; no freeness).
Step 2 (vary `Sigma`; uses `rho bar` irreducible): `v(eta^empty) = v(eta^Sigma) - sum_{p in Sigma} v_l(L_p^nv(A_f, 1)^{-1})`; only multiplicative
primes contribute, each `v_l(1 - p^{-2}) = v_l(p^2 - 1)`.
Step 3 (Taylor-Wiles; uses `l` not in `S_f`): `v(eta^Sigma) = length H^1_Sigma(Q, W)`.
Step 4 (compare Selmer groups; uses `l` not in `S_f` through Theorem thm:dfg27 (only `H^1_f(Q, V^D) = 0`, point 63), `l` odd, Lemma lem:h0):
`length H^1_Sigma = length H^1_f(Q, W) + sum_{p in Sigma} length H^1_f(Q_p, T^D)`.
Step 5 (local terms; uses `p != l`): `length H^1_f(Q_p, T^D) = v_l(L_p(A_f, 1)^{-1}) + v_l(Tam_p(A))`.
Step 6 (assemble; cancellation): (eq:identity) with EQUALITY; the Euler sum is `sum_{p | N} e_l(E, p)` (naive = true at multiplicative `p`, naive
`= 1` at additive `p`).
Step 7 (explicit Tamagawa terms, and (eq:thm)): `v_l(Tam_p(ad T)) = 0` at good and at potentially good primes (point 64,
`\Cref{ch:blochkato}` 9.3); `= t_l(E, p) + min(t_l(E, p), v_l(p - 1), v_l(c(u_p)))` at every potentially multiplicative `p`, INCLUDING an
`I_n^*` prime at `p = 2`: over `Q_p`, `E` is a quadratic twist of a Tate curve with parameter of valuation `-v_p(j)`, `ad T|_{G_{Q_p}}` is
unchanged, and Lemma lem:tamfactor applies (it needs only `p != l`, `l` odd), with `n = -v_p(j)`, not the index of the Kodaira symbol
(`\Cref{ch:blochkato}` 8.4). Dropping `length H^1_f >= 0` and the `min` gives (eq:thm).
**Commentary (important_notes.md point 18).** For the `I_n^*` primes the paper uses "the curve `E_{\{p\}}` of Lemma lem:twist", which is
defined for odd `p` only, while Theorem thm:main allows `2 | N`; at `p = 2` with `v_2(j) < 0` the term `t_l(E, 2)` can be positive. The
argument is local and goes through as in Step 7. The book states Step 7 for every potentially multiplicative `p`, `p = 2` included;
the paper's `E_{\{p\}}` is the book's `E^{(p)}`.
**Commentary (important_notes.md points 39, 56, 73, 64).** The paper's proof gives `>=` in Step 1 and "equality in the free case";
the book's Step 1 is an equality (A4.4), so (eq:identity) is an equality for `l` not in `S_f`. With point 64 every Tamagawa term is explicit,
so the identity reads `length H^1_f(Q, W) = v_l(deg varphi_E) - B^expl_l(E)`: the Selmer length is COMPUTED from the degree. Examples
(`\Cref{ch:blochkato}` 11.3, `\Cref{ch:congruence}` 9.4; `l = 3`, `3` not dividing `N`, `E[3]` irreducible, image not 3Ns): 121a1 (`e_3 = 1`, `deg
6`): Selmer length `0`; 791a1 (explicit bound `2` thanks to the Tamagawa excess at `7`, `deg 144`): `0`; 1184f1 (bound `2`, `deg 1728`): `1`;
1748e1 (bound `3`, `deg 3240`): `1`.
Rigour: the assembly is *proved here*; DFG04 Theorems 3.7, 2.7, Proposition 1.4(c), Lemma 2.1, (57), FPR94, ARS12 are *stated;
reference*.

**A4.13 `rem-ko`** (remark (the paper's Remark rem:ko); (1) *proved here* from A2.7 and A4.12; (2) *stated; reference* KimOta Theorem
1.1 and Definition 2.12 (as cited); `\Cref{ch:congruence}` 10.1, 10.2, `\Cref{ch:modgalrep}` 11.4, `\Cref{ch:blochkato}` 8.3; paper use:
Remark rem:ko, Section sec:tam, Section 1.5).
Statement. (1) At a multiplicative prime `q = 1 mod l` with `l | n` and `u bar` an `l`-th power in `F_q^x`, `v_l(Tam_q(ad T)) >= t_l(E, q) + 1`;
precisely the excess is `min(v_l(n), v_l(q - 1), v_l(c(u)))`, and by A4.12 it raises the bound by exactly that amount for `l` not in `S_f`,
also at potentially multiplicative additive primes. (2) Kim-Ota: for `N = N^+ N^-`, `N^-` square-free, `l >= 5`, `l` not dividing `N`, `l` not in
`S_f`, `rho bar` ramified at every `q | N^-` with `q = +-1 mod l`: `ord_lambda eta_f(N) = ord_lambda eta_f(N^+, N^-) + sum_{q | N^-} t_f(q)`; so `v_l(r_E) >=
sum_{q | N^-} t_l(E, q)`, which (eq:thm) contains without `l >= 5` and `q != +-1 mod l`; the equality is theirs. Expansion: check that Kim-Ota's
`eta_f(N)` is the Hecke congruence ideal (then `= r_E Z_l`); if cohomological, A4.4 gives the same value at `l` not dividing `N`.
**Commentary (important_notes.md points 65 and 23).** As in the abstract, the paper's "(1) ... raises the bound accordingly" is right
with the condition `l | n`, and the raise can exceed one (only if `l^2 | n` and `l^2 | q - 1`); the class is `c(u)`, not `c_q`.

**A4.14 `thm-twist`** (theorem (the paper's Theorem thm:twist); *proved here* (full proof `\Cref{ch:congruence}` 11.2); reference:
Atkin-Li, Shimura71 by section (level of a twist); `\Cref{ch:hecke}` 6.3, 8.2, 9.1, 9.3, `\Cref{ch:modgalrep}` 10.1, 10.2,
`\Cref{ch:ellcurves}` 10.4, 10.6; paper use: Theorem thm:twist, Section sec:twisting, Theorem thm:quant Step 1).
Statement. Let `E/Q` have conductor `N`, `S` a set of odd primes, `D = prod_{q in S} q`, `chi_S = prod_{q in S} chi_{q*}`, `E_S = E tensor chi_S` of
conductor `N_S`. If `q^2 | N` for every `q in S` and `lcm(N_S, D^2) | N`, then `r_{E_S} | r_E`; if moreover `lcm(N, D^2) | N_S`, then `r_{E_S} = r_E`.
Expanded proof (the twist map is written `iota_S` in this chapter, B-C15(c), L6). (1) `iota_S : h -> h tensor chi_S` maps `S_2(Gamma_0(N_S))`
into `S_2(Gamma_0(lcm(N_S, D^2))) subset S_2(Gamma_0(N))`, preserves integrality, intertwines `T_p` with `chi_S(p) T_p` for `p` not dividing
`D N_S`, and kills the coefficients at multiples of `D` (`\Cref{ch:hecke}` 9.1). (2) `iota_S(g) = f` for `g = f_{E_S}`: both multiplicative,
`a_p(f) = chi_S(p) a_p(g)` for `p` not dividing `D` (the twist is unramified there), `a_{q^k}(f) = 0` for `q in S` (`q^2 | N`). (3) `g^perp`, the
`T`-stable complement of the `g`-line (the sum of the generalised eigenspaces of the other systems; at level `N_S`, where `g` is new, it
equals the Petersson complement, `\Cref{ch:hecke}` 8.2), is mapped into `f^perp` (strong multiplicity one, `\Cref{ch:hecke}` 6.3). (4) A
congruence `g = h mod r`, `h in g^perp` integral, gives `f = iota_S(h) mod r`, so `r | r_E`. (5) Under the second hypothesis the roles exchange.
Hypothesis check: (a) `I_n^*` at each `q in S`: `N_S = N/D`; (b) `I_0^*`: `N_S = N/D^2`; (c) `II, III, IV` or a dual at `q >= 5`: `N_S = N`,
equality (`\Cref{ch:modgalrep}` 10.2). Worked instances (degrees from Cremona's `degphi` file, congruence numbers from
`\Cref{ch:hecke}` 11.2, 11.3): (c) 121a1 and 121c1: `r = 6 = 6`; (a) 539c1 (`deg 288`) and 77c1 (`deg 6`), `r(77c) = 6 | 288 = r(539c)`; 980i1 (`deg
2880`) and 140b1 (`deg 60`); 121d1 (`deg 24`) and 11a3 (class 11a, `deg 1`); (b) 539d1 (`deg 72`, `r = 504`) and 11a3 (class 11a, `r = 1`).
The paper's data paragraph: "On the working set, for the `157,938` pairs (curve, prime of type `I_n^*`) and the `292,580` pairs (curve, prime
of potentially good additive type), `v_l(deg varphi_E) >= v_l(deg varphi_{E_q})` holds for `l in {3, 5, 7, 11, 13}`, `l^2` not dividing `N`, with
no exception, with equality in every pair of case (c) and strict inequality only in case (b), where the difference is the Euler term of
Theorem thm:quant."
**Commentary (important_notes.md point 16).** "Strict inequality only in case (b)" contradicts Theorem thm:quant, which predicts a gap
of `e_l(E, q) = v_l(q^2 - 1)` in case (a) too. Instances at `l = 3` (`3` not dividing `N`, `E[3]` irreducible): 539c1 versus 77c1 (`v_3`: `2`
versus `1`), 980i1 versus 140b1 (`2` versus `1`), 121d1 versus 11a3 (`1` versus `0`). Reproduced below conductor `10,000`
(`\Cref{ch:computation}` 11.7): case (a) `24,373` triples, strict in `2,779`; case (b) `8,348`, strict in `1,308`; case (c) `19,554`, all equal (and
`14,876` pairs with equality, `\Cref{ch:congruence}` 11.3). Correct sentence: "strict inequality in cases (a) and (b), the difference being
exactly the Euler term of Theorem thm:quant when `l` is not in `S_f`" (A4.16). The book quotes the paper and prints the corrected sentence.

**A4.15 `proof-thm-quant`** (theorem (proof of Theorem thm:quant, Steps 1 to 4), with `q` odd; *proved here*, with DFG04
Proposition 1.4(c) as a stated input (full proof `\Cref{ch:congruence}` 12.2 to 12.5); reference: paper Section sec:twisting;
`\Cref{ch:hecke}` 7.1, 7.2, 7.4, 8.1, 8.3, 9.3, `\Cref{ch:modules}` 10.3, `\Cref{ch:moddeg}` 6.4, 9.3, 9.5; paper use: Theorem thm:quant).
Set-up. `f = f_E`, `g = f_{E_S}` of level `N_S`, `S` the odd primes of type `I_0^*` or `I_n^*`, `D = prod_{q in S} q`, `O = Z_l`. By Lemma lem:twist,
`E_S` is good at the `I_0^*` primes (`delta_q(g) = 2`) and multiplicative at the `I_n^*` primes (`delta_q(g) = 1`), so `N_S^S = N`: the depleted
form `g^S` lives at level `N`, its generalised eigenspace is the line `C g^S` (`\Cref{ch:hecke}` 7.4(iv)), and `iota_S(g^S) = iota_S(g) = f`.
Step 1 (transport of congruences; elementary). `T` the full Hecke algebra of level `N`, `pi : T -> Z` the eigencharacter of `g^S`, `m` the
maximal ideal of `T_l` containing `ker pi` and `l`; `U_q in m` for `q in S`. Every `U_q`-eigenvalue on `S_2(Gamma_0(N))` is `0`, `+-1` or a root of
`X^2 - aX + q`, hence `0` or an `l`-adic unit (`\Cref{ch:hecke}` 7.2); so the `m`-component is `C g^S` plus generalised eigenspaces of systems
with `U_q = 0` from newforms `h != g`. The proof of Lemma lem:crit over `Z_l`, run for `g^S` with the `T`-STABLE complement of the `g^S`-line,
shows that `l^{v(eta^Hecke(g^S))}` is the largest `l^t` with `g^S = h mod l^t`, `h` integral in that complement; project by `e_m`
(`\Cref{ch:hecke}` 8.3); apply `iota_S`, which lands in `f^perp`. So `v_l(r_E) >= v_l(eta^Hecke(g^S))`.
Step 2 (Hecke versus cohomological ideal): Lemma lem:ddt417 with `L = H^1(X_0(N), Z_l)_m` (pairing perfect on the `m`-part, point 36),
`L[wp] = M_{g^S,lambda}` of rank `2` with Gram determinant `(eta^S_{g,lambda})^2`: `v(eta^Hecke(g^S)) >= v(eta^S_{g,lambda})`, no freeness needed.
Step 3 (DFG04 Proposition 1.4(c) for `g`; `rho bar_g = rho bar tensor chi_S` irreducible, `l` not dividing `2N_S`): `v(eta^S_g) = v(eta^empty_g) + sum_{q
in S} e_l(E, q)`, because `A_g = A_f`, `delta_q(g) >= 1` (naive factor = true factor), and the true factor of `A_f` at `q` is the one `f` omits. At
`q = 3` the values are the twist formulas `L_3(A_f, 1)^{-1} = (2/3)(16 - a_3(E')^2)/9` (`I_0^*`) and `8/9` (`I_n^*`), checked against PARI (point 60).
Step 4 (level `N_S`): `v(eta^empty_g) = v_l(deg varphi_{E_S^opt}) = v_l(r_{E_S})` by A4.4 for the optimal curve of the class of `E_S` (point 39:
NO freeness; `v_l(deg)` is a class invariant as `E_S[l]` is irreducible, `\Cref{ch:moddeg}` 6.4, `\Cref{ch:ellcurves}` 9.9). With `v_l(deg
varphi_E) = v_l(r_E)` this proves the first inequality; the second because `r_{E_S}` is an integer.
**Commentary (important_notes.md point 61).** "The proof of Lemma lem:crit carried out for `g^S`" must use the complement of the
`g^S`-line stable under the full Hecke algebra; the Petersson orthogonal complement is not `T`-stable when `U_p` is involved (level
`44`). The paper's text says "the `T`-stable complement", which is right; the book must not substitute the Petersson one.
**Commentary (important_notes.md point 59, optional).** Step 1 is an equality: `iota_S` sends `f` to `g^S` and `f^perp` into the
`T`-stable complement of `g^S`, and conversely, so `v_l(r_E) = v_l(eta^Hecke(g^S))` (`\Cref{ch:congruence}` 12.3; at level `539` the Hecke
congruence modules of the two depleted forms have orders `288` and `504`, equal to `r(539c)` and `r(539d)`, `\Cref{ch:hecke}` 11.3(d)).
**Commentary (important_notes.md point 60).** The restriction `q >= 5` is not needed: the argument works for every odd `q in S` (the
twist lemma for `I_n <-> I_n^*`, `I_0 <-> I_0^*` holds at every odd `q`); the bound held in all `388` cases with type `I_0^*` at `3`. The book
states the theorem with `q` odd and marks the extension as the book's.
**Commentary (important_notes.md points 24 and 39).** Without point 39 the middle term needed multiplicity one at level `N_S`
(Lemma lem:hecke gives only `v_l(r_{E_S}) >= v(eta^empty_g)`, the wrong direction); with point 39 it does not. The outer inequality never
needed it. Steps 2 and 3 are not elementary (A1.11).
Worked checks (`\Cref{ch:congruence}` 12.6, `\Cref{ch:hecke}` 11.3; Cremona degrees): at `l = 3`: 539c1: `2 = v_3(r_{77c}) + v_3(48) = 1 + 1`;
980i1: `2 = v_3(r_{140b}) + v_3(48) = 1 + 1`; 121d1: `1 = 0 + v_3(120)`; 539d1: `v_3(72) = 2 = 0 + v_3(6) + v_3(60)`. All equalities, as A4.16
predicts. "`E[l]` irreducible" cannot be dropped: 539d1 at `l = 5` has `e_5 = v_5(6) + v_5(60) = 1` but `v_5(72) = 0` (image 5B.4.1); 539a1 (`I_2^*` at
`7`, image 3B) has `e_3 = 1` and `v_3(320) = 0`; 98a1 (`I_1^*` at `7`, `E[3]` reducible) has `e_3 = 1`, `deg 16`.

**A4.16 `rem-after-quant`** (remark (the remark after the proof of Theorem thm:quant), with (2) in the strengthened form; (1), (3)
*proved here*, (2) *proved here* from A4.12; reference: `\Cref{ch:congruence}` 12.6, 12.7; paper use: the remark after Theorem
thm:quant).
Statement. (1) Theorem thm:quant is the twist-and-lower argument of Section sec:proof read the other way: the level is raised from
`N_S` to `N`, at the price of the level-raising Euler factors. For `l = 3` a single `I_n^*` prime `q >= 5` forces `3 | deg varphi_E` (`3 | q^2 - 1`), and
so does an `I_0^*` prime with `q = 1 mod 3`; neither needs the hypothesis on `Q(sqrt(-3))`, neither is in Theorem thm:qual. (2) If `l` is not in
`S_f`, then `v_l(deg varphi_E) = v_l(r_{E_S}) + sum_{q in S} e_l(E, q)`, and every inequality in the chain of Steps 1 to 4 is an equality (in
particular `v(eta^Hecke(g^S)) = v(eta^S_{g,lambda})`, a freeness-type statement for the depleted form obtained without multiplicity
one). Proof: (eq:identity), an equality (A4.12), for `E` and for the optimal curve of the class of `E_S` (`l` not in `S_{f_{E_S}}`: twisting
preserves absolute irreducibility over `Q(sqrt(l*))`); the Selmer groups coincide (`ad T` twist-invariant); the Tamagawa factors
coincide (trivial at `I_0^*` primes by point 64; at `I_n^*` primes `E_S` is multiplicative with the same Tate parameter); the Euler sums
differ by exactly `sum_{q in S} e_l(E, q)` (outside `S` the twist is unramified; at `q in S`, `E_S` is good or multiplicative and contributes `0`).
(3) Step 1 fails for `II, IV, III` and duals: the twist does not lower the level, `f` is its own depletion, Theorem thm:dfg14 gives no factor;
these terms come only through Theorem thm:dfg37, i.e. with `l` not in `S_f`, and Section sec:anomaly shows the hypothesis cannot be dropped
(3Ns curves fail through a type `III` term).
**Commentary (important_notes.md point 74; B26).** The paper's (2) concludes "the first inequality of Theorem thm:quant is an equality
when `H^1(X_0(N), Z_l)_m` is free, that is, under multiplicity one at level `N`". Correct statement: equality whenever `l` is not in `S_f`, with
no multiplicity-one hypothesis (proof above). Data: equality in all `25,477` pairs below conductor `10,000` (`15,607` with `3 in S`), and also
in the `8` pairs with image 3Ns, which lie outside the theorem. The first version of this item (and `\Cref{ch:moddeg}` 9.5(c), 10.4(b),
`\Cref{ch:modgalrep}` 10.4) said the equality still needs multiplicity one; that claim is withdrawn.

### A5. The paper's Section 5: the boundary of the hypothesis (Section 21.14)

**A5.1 `proof-prop-ns`** (proposition (proof of Proposition prop:ns); *proved here* (full proof `\Cref{ch:galrep}` 8.3); reference:
Zywina15 (by section, point 4); `\Cref{ch:groups}` 5.7, 6.3, 6.5 to 6.8, `\Cref{ch:reps}` 1.4, 2.5, 6.2, 6.6, 8.2, `\Cref{ch:galois}`
galois:quartic-on-lines, galois:index-two-restriction, `\Cref{ch:ellcurves}` 4.5; paper use: Proposition prop:ns, Section sec:anomaly,
Conjecture conj:euler).
Statement: A1.12.
Expanded proof, step by step. (1) `det rho bar_{E,3} = chi bar_3 = chi_{-3}` (Weil pairing) cuts out `Q(sqrt(-3))`, so `rho bar(G_{Q(sqrt(-3))}) = H
cap SL_2(F_3)`. (2) Possible `H`: `E[3]` irreducible, `det` surjective, and `H` contains `rho bar(c)` of determinant `-1` and trace `0`; pure group
theory (enumeration of the `55` subgroups of `GL_2(F_3)`, `\Cref{ch:groups}` 6.3, 6.7) leaves `GL_2(F_3)` (`48`), `N_ns(F_3)` (`16`,
semidihedral), `N_s(F_3)` (`8`, dihedral); the nonsplit Cartan `C_ns(F_3) = F_9^x` is excluded (its elements of determinant `-1` have order `8`,
hence nonzero trace). (3) Determinant-one subgroups: `SL_2(F_3)`, `Q_8`, `C_4 = <J>`, `J = (0, 1; -1, 0)`. (4) `SL_2(F_3)` and `Q_8` act absolutely
irreducibly. (5) `C_4` is abelian; `X^2 + 1` is irreducible over `F_3`, so the restriction to `G_{Q(sqrt(-3))}` is irreducible over `F_3` but not
absolutely irreducible: over `F_9` it is `psi + psi^{-1}` with `psi` of order `4`, values in `F_9^x` (`\Cref{ch:reps}` 2.5). (6) Frobenius
reciprocity: `rho bar tensor F_9 = Ind psi`; a representation induced from an index-two subgroup is invariant under the twist by that
subgroup's character, so `rho bar tensor F_9 = (rho bar tensor chi_{-3}) tensor F_9`, and the isomorphism descends to `F_3` (`\Cref{ch:reps}`
1.4(ii)); hence `H^0(Q, ad rho bar(1)) != 0` and `h_3(E) = 1` (A4.11). (7) Lines: the four roots of `psi_3` are the `x`-coordinates of the four
lines of `E[3]`; `N_s(F_3)` has two orbits of size two, `N_ns(F_3)` and `GL_2(F_3)` are transitive; `psi_3` has no rational root (`E[3]`
irreducible); so `psi_3` is (leading coefficient `3`) times two irreducible quadratics in the first case and irreducible otherwise.
Examples: 726a1, `psi_3 = (x^2 - x - 74)(3x^2 + 8x + 20)` (PARI); 6912d1 (`y^2 = x^3 - 6x - 8`), `3(x^2 - 4x - 2)(x^2 + 4x + 6)`; 11a1, irreducible with group
`S_4`.
Where the hypotheses enter: "`E[3]` irreducible" in (2) and (7); "without CM" nowhere.
**Commentary (important_notes.md point 1).** The paper justifies (4) by "they are non-abelian and act faithfully". Not enough (a Borel
subgroup is non-abelian, faithful and reducible). Missing step: a subgroup fixing a line over `Fbar_3` lies in a Borel subgroup, so its
commutator subgroup lies in the unipotent radical, abelian of exponent `3` (`\Cref{ch:groups}` 5.7); `Q_8` has commutator subgroup `{+-1}`
(not unipotent) and `SL_2(F_3)` has commutator subgroup `Q_8` (not abelian). The book inserts this sentence.
**Commentary (important_notes.md point 33).** "`rho bar = Ind psi`" and "induced from `Gal(Qbar/Q(sqrt(-3)))`" are statements over `F_9`:
the restriction is irreducible over `F_3`, and `psi` takes values in `F_9`. Write `rho bar tensor F_9 = Ind psi`; the isomorphism `rho bar = rho bar
tensor chi_{-3}` then descends to `F_3`, as in (6).
**Commentary (important_notes.md point 2).** With the standard models (`\Cref{ch:groups}` 6.2), `N_s(F_3)` lies in `N_ns(F_3)` with index two,
and `N_s(F_5)` in a subgroup of order `96` with image `S_4` in `PGL_2(F_5)`. The paper does not claim maximality; the book warns readers
importing the large-`l` picture not to call `N_s` maximal at `l = 3, 5`.
**Commentary (important_notes.md point 4).** The theorem numbers in Zywina15 (list of mod `3` images) and Serre72 (Dickson) are cited
by section; step (2) is proved directly, so nothing depends on them.
**Commentary (important_notes.md point 9).** "Without complex multiplication" is not used: the list in (2) follows from the surjective
determinant, irreducibility and complex conjugation. CM curves with `3` split in the CM field have image in `N_s(F_3)` and `2 + 2`
factorisation (121b1, CM by `Q(sqrt(-11))`; `13` CM optimal curves below conductor `10,000` have `ns3 = 1`). The book drops the hypothesis.

**A5.2 `rem-ns`** (remark (the paper's Remark rem:ns); the displayed identity *proved here* CONDITIONALLY from Lemma lem:dfg21, Lemma
lem:fpr, Lemma lem:h0; the 3Ns structure *proved here* from `\Cref{ch:galrep}` 8.4; data *stated*; reference: `\Cref{ch:blochkato}`
12.1 to 12.3, `\Cref{ch:congruence}` 13.1, 13.2; paper use: Remark rem:ns, Conjecture conj:euler, Open question 2).
Statement. When `l = 3` and the image is `N_s(F_3)`, Theorem thm:dfg37 does not apply, but IF `H^1_f(Q, V^D) = 0` the sequence of Lemma
lem:dfg21 gives `length H^1_Sigma = length H^1_f(Q, W) + sum_{p in Sigma}(v_l(L_p(A_f, 1)^{-1}) + v_l(Tam_p(A))) - h_3(E)`, with `h_3(E) = 1`
(`H^0(Q, V^D) = 0` is automatic, point 63). If `v(eta^Sigma) = length H^1_Sigma` still held, (eq:identity) would hold with `h_3(E)` subtracted:
the shape of Conjecture conj:euler. Data: `h_3(E) = 1` for every 3Ns curve; (eq:thm) fails for `31%, 23%, 18%` of them on the three ranges,
always by exactly one, never for another curve.
Structure of 3Ns curves (important_notes.md point 48; `\Cref{ch:galrep}` 8.4, theorems): for every prime `p != 3`, `rho bar(I_p) subset C_4`;
so every multiplicative `p != 3` has `3 | n_p` (`t_3(E, p) >= 1`), no `p >= 5` has type `II, II^*`, no `p != 3` has type `IV, IV^*`; the set `R` of
primes `p != 3` with `rho bar(I_p) = C_4` is nonempty, and for `p in R` the image of inertia on `T_l E` is cyclic of order `4`, `p >= 5` has type
`III` or `III^*`, `e_3(E, p) = v_3(p - chi_{-3}(p)) >= 1` with `chi_{-4}(p) = chi_{-3}(p)`, i.e. `p = 1` or `11 mod 12`; for `p = 2 in R`, `P_2 = 1 + 2X`;
`a_p = 0 mod 3` for `p = 2 mod 3` not dividing `3N`; if `3` does not divide `N`, `E` is ordinary at `3`.
**Commentary (important_notes.md point 67).** The paper's remark is phrased conditionally ("whenever"), but Section 1.3 presents the
correction term as what Lemma 2.1 of DFG04 produces. The needed vanishing `H^1_f(Q, V^D) = 0` (equivalently `H^1_f(Q, ad V_3 E) = 0`) is
DFG04 Theorem 2.7, proved only for `l` not in `S_f`; 3Ns curves are exactly `l = 3` in `S_f`. The book states the identity as conditional
on this vanishing (predicted by the Bloch-Kato conjecture), and cites no later result unless checked.
**Commentary (important_notes.md point 48).** Section sec:anomaly reports as observations that every 3Ns curve has a type `III` or
`III^*` prime with positive `e_3`, that the residue classes are `1` and `11 mod 12` (with some `q = 2`), and that each violation involves a
prime `p = -1 mod 3` with `t_3(E, p) >= 1`. The first two are theorems (structure above), checked on all `120` non-CM 3Ns curves below
conductor `10,000` (`100` with such a prime `p >= 5`, `20` with `p = 2`); the third is explained in part (every multiplicative prime `p != 3`
of a 3Ns curve has `t_3(E, p) >= 1`) and observed for all `36` violators below `10,000` (`\Cref{ch:computation}` 11.3), but that every violator
has such a prime `p = -1 mod 3` is not proved. The book states the first two as a proposition and the third as an observation.

### A6. The paper's Section 6: the computations (Sections 21.15 to 21.17)

General note for all of A6. The paper's tables are `\input` from files `tables/*.tex` that are NOT in this repository. The book
describes each table from its caption and the numbers quoted in the text, and never invents table entries. Every count of the
paper is *stated* (attributed to the paper). The book's own reproduction on conductor below `10,000` (`38,042` optimal curves, PARI/GP
2.17.2, Cremona's `ecdata` files; `\Cref{ch:computation}` Section 11 and Part 7) is quoted beside the paper's numbers where it helps,
always labelled as the book's, with the warning that rates fall with `N` and are not comparable across ranges (`\Cref{ch:computation}`
11.8). Chapter 22 covers PARI, `ecdata` and the protocol; here the tour explains what each statement means and what it tests.

**A6.1 `data-protocol`** (data description; *stated*; reference: Cremona97, `ecdata` commit `25cec5e`, PARI 2.15, Sutherland16;
`\Cref{ch:computation}` 4.1, 4.3, 9.1, 9.2; paper use: Section sec:data, Section 6.1).
Content. Tables: every curve of conductor below `500000` with modular degrees, isogeny classes, torsion, mod `l` images (Sutherland's
labels); the per-prime Kodaira symbols and Tamagawa numbers are recomputed with PARI from the `a`-invariants (Cremona's files contain
none; the modular-degree file is `degphi`, not `alldegphi`, important_notes.md B27). Optimality determined for every class with `N <=
400000` and for `359,009` further classes up to `500000` (curve number `1` is not always optimal: 990h3, not 990h1, is the optimal curve of
990h, `\Cref{ch:computation}` R0). Ranges: working set (`N <= 300000`), hold-out, extension, out-of-table set. Order of discovery as in the
paper.
Test status, read off the paper (the book prints `\Cref{ch:computation}` 9.2 as a table): (eq:main) and Conjecture conj:eis: found on the
working set, blind-tested once on the hold-out, then on the extension. (eq:twist): replaced a weaker form on the working set and was
"tested once" on hold-out and extension; it is blind only if it was fixed before the hold-out was opened for (eq:main), which the text
does not say, and the paper does not state the blind status of the out-of-table curves for it. Conjecture conj:euler (the Euler terms
and the weights `w_3`): hold-out and extension are a confirmation only; the out-of-table curves, generated before the rule was formulated,
are its blind test. The correction term `h_l`: never blind-tested, since the out-of-table set contains no 3Ns curve. The III-free form: a
reformulation chosen after the 3Ns exceptions. Lemmas lem:euler, lem:twist, Proposition prop:forms, `h_3 = 1`: theorems; the data are
checks of computations.
**Commentary (important_notes.md point 77; B27).** The paper does not say that the correction term `h_l` was fitted on, and only
confirmed by, data already seen, nor the blind status of the out-of-table curves for (eq:twist). The first version of this item (and
Appendix A) called (eq:twist) blind-tested without this caveat. Correct statement: as above. The book adds both caveats.
**Commentary (important_notes.md point 25).** "Every optimal curve of conductor at most `500000`" (abstract) means the classes where
optimality is known; the extension counts are over the `359,009` determined classes.

**A6.2 `table-uniform`** (how to read Table tab:uniform; *stated*; `\Cref{ch:computation}` 11.1; paper use: Section 6.2).
Columns (from the caption): for each range and `l in {3, 5, 7, 11, 13}`: curves with `E[l]` irreducible, not CM, positive bound in (eq:rule);
violations (all zero); equality rate; violations when `h_l` is dropped (all 3Ns curves at `l = 3`); the "III-free" rule (type `III, III^*` terms
omitted, no correction): positive bounds, violations, equality rate. Reading: the III-free rule has no exception because the 3Ns
failures always involve a type `III` term (A5.2: a theorem). Book's small range (`N < 10,000`, `l = 3`): `33,851` curves, `20,317` with a positive
bound, `0` violations, equality `71.0%`, `36` violations without `h`, III-free `20,127` positive, `0` violations.
**Commentary (important_notes.md point 80, second item).** The number of 3Ns violations "when the correction term is dropped" depends
on whether the terms at `q = l` (the `t_l(E, l)` and `w_3`) are included: below conductor `10,000` it is `36` with them and `24` with (eq:thm) read
literally (terms at `q != l` only; 726a1 then has bound `2` and no violation). The paper does not say which reading its counts use. The
book states the reading it uses (with the `q = l` terms, as `rule(E, 3, 1)` without `ns3`) and gives both numbers.

**A6.3 `calibration`** (data argument (Section sec:sharp); *stated*, arithmetic *checked here*; `\Cref{ch:computation}` 10.1 to 10.6;
paper use: Section sec:sharp).
Content. Among `366,151` working-set curves with `E[3]` irreducible, not CM and bound `0`, `53.2%` have `3` not dividing `deg varphi_E`; under
independence the `867,578` curves with a positive bound would give about `605,000` violations (`69.7%` of them); there are none. Equality rates
`57.5%, 75.6%, 84.1%, 91.6%, 92.4%` at `l = 3, 5, 7, 11, 13`; mean excess `0.63` at `l = 3`. Odd part of the degree: equal to `prod l^{b_l}` for `1.85%`
of `1,226,216` curves. Expansion: (1) the null model `sum_E P(v < b(E))` from the bound-0 population; the `v = 0` part alone gives at least `0.532 x
867,578 = 461,551`. (2) Book's range: `14,275` expected (`70.3%`), `0` observed; a stratified permutation null gives about `7,600`; the reference
population changes the number by a factor of two, the conclusion not at all. (3) Under Theorem thm:main (now an equality) the excess
over the explicit bound IS the Selmer length (A4.12); the paper's "plus the excess of the Tamagawa factors over `t_l`" is the same
statement with the Tamagawa excess counted separately.
**Commentary (important_notes.md point 79).** The calibration shows that the statement is strong (far from vacuous), not that it is
valid: on the working set the rule was fitted, so validity rests on the blind tests (A6.1). The expected count depends on the reference
population, and the odd-part statistic is strongly range-dependent (`1.85%` on the working set, `17.1%` below `10,000`). The book says so.

**A6.4 `tamagawa-test`** (data (Section sec:tam); *stated*, percentages *checked*; `\Cref{ch:blochkato}` 13.1, 13.2,
`\Cref{ch:computation}` 11.5; paper use: Section sec:tam, Remark rem:ko(1), Lemma lem:tamfactor).
Content. At a prime of type `I_n` with `l | n` and `q = 1 mod l` the bound is raised by `min(v_l(n), v_l(q - 1), v_l(c(u)))`. `l = 3`: `46,222` curves,
`12,095` with a positive extra term (total `12,125`), no exception, equality from `45.0%` to `60.6%`; `l = 5`: `10,940`, `1,646`, equality `67.0%` to
`78.7%`. Book's range (only `I_n` primes, as the paper): `l = 3`: `989` curves, equality `55.6%` to `66.9%`; with `I_n^*` primes included: `1,050` curves,
`56.8%` to `68.0%`; no violation. Reading: given the equality (A4.12), a violation is impossible, and the proportion of equality is the
proportion of curves with `H^1_f(Q, W) = 0`; the test checks the Tamagawa term of the identity.
**Commentary (important_notes.md points 23, 68).** `c_q` here is the class `c(u)` of Lemma lem:tamfactor, not the Tamagawa number (point
23). The test can include potentially multiplicative additive (`I_n^*`) primes, where the formula also applies (point 68, A4.12 Step
7); and "the extra divisibility of the modular degree is exactly where the Tamagawa factor of the adjoint exceeds `l^{t_l}`" overstates:
the Selmer length also contributes extra divisibility. The book rewords both.

**A6.5 `isolated-terms`** (data (Section sec:iso, Table tab:iso); *stated*; `\Cref{ch:computation}` 11.4; paper use: Section sec:iso).
Content. Working-set curves with exactly one additive prime `q >= 5`, `q != l`, and no multiplicative prime with `l | n`: in every cell (type,
`e_l(E, q)`), for `l = 3, 5, 7`, the minimum of `v_l(deg)` equals `e_l`, and for `I_n^*` the excess over `e_l` has minimum `v_l(n)`; cells with `e = 0`
(`III`: `5,534`; `I_0^*`: `5,394`) have minimum `0`; `I_0^*` up to `e = 6`. Multiplicative primes alone: `min(v_l(deg) - v_l(n)) = 0` for every `v_l(q^2 -
1) <= 6`. Two primes of type `II/II^*`: `9 | deg` for all `2,502` curves, and never via a congruence with the own twist. Book's range: the same
pattern in every cell. Reading Table tab:iso: rows Kodaira type, columns `e_3(E, q)`, entries minimum (number of curves).

**A6.6 `corollary-forms`** (data (Section sec:forms, Table tab:counts); *stated*; `\Cref{ch:computation}` 11.2; paper use: Section
sec:forms, Proposition prop:forms, Conjecture conj:eis).
Content. Positive bounds and violations (none) of (eq:main) and (eq:twist) per range and `l`; Eisenstein column. Equality rates (eq:twist)
`39.4%, 71.1%, 81.2%, 91.5%` at `l = 3, 5, 7, 13`; (eq:main) `36.9%, 69.7%, 80.4%, 91.2%`; the rule bounds `867,578` curves instead of `705,563` at `l = 3`.
Where the hypothesis of Theorem thm:main fails on the working set: `1,170` 3Ns curves; curves with `l | N`; "the curves whose mod `l`
representation is induced from `Q(sqrt(l*))` with `l >= 5`, which we did not single out".
**Commentary (important_notes.md point 47).** That last class consists only of curves with `l | N`: for `l >= 5` not dividing `N` and `E[l]`
irreducible, `l` is automatically not in `S_f` (A4.6). The book says so.
**Commentary (important_notes.md point 43).** With A1.8, Proposition prop:forms has no exception, so the zero violations of (eq:main)
and (eq:twist) under the hypothesis are predicted by a theorem; the data test them outside it.

**A6.7 `ns3-boundary`** (data (Section sec:anomaly, Table tab:ns); *stated*, with the theoretical parts *proved here* (A4.11, A5.1,
A5.2); `\Cref{ch:computation}` 11.3, `\Cref{ch:galrep}` 8.4; paper use: Section sec:anomaly, Remark rem:ns, Conjecture conj:euler).
Content. (eq:thm) with all types and no correction: `364, 68, 43, 0` violations on the four ranges, all at `l = 3`, all 3Ns curves (each with
`psi_3` = two quadratics); none by `GL_2(F_3)` or `N_ns(F_3)` curves. Every 3Ns curve has a type `III/III^*` prime with positive `e_3`; the
inequality fails for `31%, 23%, 18%` of them, always by one; the violation involves a prime `p = -1 mod 3` with `t_3(E, p) >= 1`. `h_3(E) = 1` for
every 3Ns curve. Type `III` primes of violators: `q = 1` and `q = 11 mod 12` in comparable numbers, some `q = 2`. Book's range: `90` optimal non-CM
3Ns curves, all with a positive type `III` term (`74` at a prime `q >= 5`, `16` at `q = 2`: conductors `3840`, `4864`, `6912`), `36` violators with the `q =
l` terms (`24` without), residues `1` (`12`), `11` (`20`), `q = 2` (`4`), shortfall always `1`; every violator has a prime `p = -1 mod 3` with `t_3(E, p) >= 1`.
Example: 726a1 (B4).
**Commentary (important_notes.md point 5, second half).** "`h_3(E) <= 1` because some prime `p < 1223` inert in `Q(sqrt(-3))` has `9` not dividing
`a_p`" is replaced by "`h_3(E) <= 1` by Lemma lem:h0" (A4.11 step (5)).
**Commentary (important_notes.md point 48).** The observations on the type `III` primes and their residues mod `12` are theorems
(A5.2); the book states them as such and keeps the counts as illustration.
**Commentary (important_notes.md point 80).** Which reading of (eq:thm) the counts use: see A6.2.
**Commentary (important_notes.md point 3).** 3Ns is checked against Cremona's `galrep` labels (`ns3` agrees on all non-CM curves below
`10,000`); the definition against Sutherland16 is still to be checked; the book always gives the intrinsic description.

**A6.8 `wild-primes`** (data (Section sec:wild, Table tab:isolated); *stated*, with the explanations *proved* (A1.8, A2.6); reference:
`\Cref{ch:lfunctions}` 10.1, 10.2, `\Cref{ch:computation}` 6.6, R5; paper use: Section sec:wild, Remark rem:wild, Conjecture
conj:euler, Proposition prop:forms).
Content. Table tab:isolated: minima of `v_3(deg)` by additive type and number of primes (untwisted rows), and by total weight of (eq:twist)
(twisted rows). Findings: `2` contributes nothing through `II, II^*` for `14,182` of the `44,672` curves whose only candidate is such a prime, and
nothing through `I_n^*` with `3 || n` (with `9 | n` the minimum is `1`); explained by Definition def:terms with PARI's factor; with the weights of
(eq:twist) at `2` counted as if `2` were odd, (eq:twist) fails thousands of times per range; with Definition def:terms never. At `q = 3`,
potentially good, `l = 3`: minima `1` for `II, IV, III^*`, `2` for `II^*, IV^*`, `0` for `III, I_0^*`: the weights `w_3` (reproduced exactly in the book's
range, `\Cref{ch:computation}` R5). For `l = 5, 7` nothing beyond Definition def:terms is needed.
**Commentary (important_notes.md points 50 and 69).** The paper explains the minima by "a type `II` at `2` has `P_2 = 1` and `e_3 = 0`", which
is false in general (A2.6); the correct explanation is that `P_2` depends on the shape of the inertia image, not on the type, and that
`P_2 = 1` is the most frequent shape for type `II` at `2`. The sentence "For `l = 5, 7` no term is needed at `q = l` or at `q = 2, 3` beyond
Definition def:terms" is right (the term is in def:terms), but the reader must not infer that `2` never contributes at `l >= 5`: 592c1 has
`e_5(E, 2) = 1` (A2.6). "A type `IV` or `IV^*` at `2` has `e_3 = 1`" is a theorem (A1.8).
**Commentary (important_notes.md point 53).** "A type `I_n^*` at `2` has `t_3 = v_3(-v_2(j))` when potentially multiplicative" uses
`-v_2(j)`, not the index of the symbol, as A1.1 defines it.

**A6.9 `out-of-table`** (data (Section sec:oot, Table tab:oot); *stated*; `\Cref{ch:ellcurves}` 9.10, `\Cref{ch:computation}` 9.1;
paper use: Section sec:oot).
Content. Curves with prescribed local types and `500000 < N <= 4 x 10^6` (families with a type `IV/IV^*` prime, with two or three type `II`
primes, mixed types, random), kept if the isogeny class is trivial (so optimal and `E[l]` irreducible for every `l`, `\Cref{ch:ellcurves}`
9.10) and not CM; degrees by `ellmoddegree`. None has image 3Ns; Conjecture conj:euler and both corollary forms hold for all `893`;
equality in (eq:rule) for `52.5%` of the `828` with a positive bound at `l = 3` (`435` curves).
**Commentary (important_notes.md point 77).** This is the blind test of the Euler terms of the rule, and only of them: with no 3Ns curve
among the `893`, the correction term `h_l` was never blind-tested (A6.1).

**A6.10 `eisenstein`** (data and conjecture (Section sec:eis); *stated*, with `D <= 2` *proved* (A1.13); reference:
`\Cref{ch:galrep}` 9.1 to 9.3, `\Cref{ch:moddeg}` 11.1 to 11.5, `\Cref{ch:computation}` 11.6; paper use: Section sec:eis, Conjecture
conj:eis, Open question 4).
Content. Working set, `l = 3`: `75,430` optimal non-CM curves with a rational `3`-isogeny, `67,845` with a positive bound in (eq:main), `2,777` with
`D > 0`, `D = 2` for `22` (`17` with `E[3] = Z/3 + mu_3`, `5` with a point of order `9`). No curve without a rational `3`-torsion point has a deficit. None
of the `2,065` curves with `N <= 400000` and image 3Cs.1.1 has a point of order `9`; the `18` optimal curves with a point of order `9` have image
3B.1.1. Torsion bound attained with `D > 0` in `2,773` cases. `l = 5, 7`: `D <= 1`, only with rational `l`-torsion (`192` and `18` cases). Against
(eq:twist) the deficit is not controlled by torsion, so the conjecture is stated for (eq:main) only. Book's range: `4,002` Eisenstein curves,
`431` with `D > 0`, `D = 2` for `14` (twelve with image 3Cs.1.1, two with a point of order `9`: 714i1, 6942n1), no violation.
**Commentary (important_notes.md point 76; B27).** Two descriptive sentences are false as written: (i) the curves with `E[3] = Z/3 + mu_3`
and `D = 2` are said to have torsion `Z/3`, but 14a1 (image 3Cs.1.1, torsion `Z/6`, types `I_6` at `2` and `I_3` at `7`, `deg 1`) has `D = 2`; (ii) "with
a rational point of order `3` and mod `3` image of Borel type, `D <= 1`" is false for curves with a point of order `9`: 714i1 (torsion `Z/9`, image
3B.1.1, `deg 1080 = 2^3 3^3 5`, `D = 2`) and 6942n1 (torsion `Z/9`, `deg 65664 = 2^7 3^3 19`, `D = 2`). The paper's next clause names the order-`9` case
as the other source of `D = 2`, so (ii) is a wording slip: "without a point of order `9`". Neither affects Conjecture conj:eis. The first
version of this item repeated both slips; the book corrects them.
**Commentary (important_notes.md point 17).** "We have not proved that the two cannot coexist": they cannot (A1.13); `D <= 2` is a theorem
given the first bound.
**Commentary (important_notes.md point 44).** "The split Cartan image 3Cs.1.1": 3Cs.1.1 is the subgroup `{diag(1, +-1)}`, i.e. `E[3] = Z/3 +
mu_3`; the split Cartan image is 3Cs (A1.13).
Expansion for the book: what "Eisenstein" means (reducible `rho bar`, maximal ideal containing `T_p - 1 - p`), why Section 4 fails
there (Ihara's lemma, Lemma lem:hecke's non-Eisenstein `m`, DFG04), the role of rational torsion and the cuspidal subgroup (Mazur77),
and the small examples 539a1 (image 3B, `I_2^*` at `7`, `e_3 = 1`, `v_3(320) = 0`, while (eq:main) holds) and 11a1 at `l = 5` (`rule(E, 5) = [0, 1]`, a
fifth-power unit part, `D = 1 = v_5(#E(Q)_tors)`; `\Cref{ch:computation}` 6.7): in the Eisenstein case the additive Euler terms do not
contribute reliably.

### A7. The paper's Section 7: the prime 2 (Section 21.18)

**A7.1 `prime-two`** (data and literature (Section sec:two); *stated; reference*: Watkins02, Dummigan06, CalegariEmerton09,
Yazdani11, CaroPasten22, HatleyKundu, BKP; `\Cref{ch:moddeg}` 12.3, 12.4, `\Cref{ch:computation}` R9; paper use: Section sec:two, Open
question 5).
Content. For working-set optimal curves without a rational `2`-isogeny and not CM: `v_2(deg) >= sum_{q || N} v_2(n_q) + #{q : type III, III^*, I_0^*
or I_n^*}` with no exception (`964,432`, `325,510`, `313,741` curves); counting `I_0^*` with weight `2` fails (`123, 26, 20`). Isolated minima: `III, III^*,
I_n^*` contribute `3`, `II, IV, I_0^*` contribute `1`, "in line with" Calegari-Emerton. Not reconciled with the literature or with Euler factors at
`l = 2` (outside DFG04). Book's range: the inequality holds on all `25,086` curves; with `I_0^*` counted twice it fails `6` times.
What the book says: `l = 2` is outside every theorem of the paper (`l` odd is used in Lemma lem:tamfactor, the trace form, the real
place, `S_f`); this section is data plus pointers; Watkins's conjecture stated precisely (`\Cref{ch:moddeg}` 12.3).
**Commentary (important_notes.md point 57).** The paper paraphrases Calegari-Emerton as "a curve of odd modular degree has at most two
odd bad primes and a rational `2`-torsion point or prime conductor". 27a1 and 243b1 have odd modular degree, torsion `Z/3` and non-prime
conductor; both have CM (`j = 0`). So the published theorem excludes CM curves or has extra cases; the paraphrase must say so. The book
copies the statement from CalegariEmerton09 with its exact hypotheses (`\Cref{ch:moddeg}` 12.4, still to be checked against the source).

### A8. Open questions (Section 21.18)

**A8.1 `open-questions`** (list; *stated*, with the book's partial answers; `\Cref{ch:congruence}` 13.2, 13.3, `\Cref{ch:blochkato}`
9.3 to 9.5, 12.3; paper use: Open questions 1 to 5).
(1) Extend Theorem thm:main to `l | N`, identifying `w_3` with a local term at `l`. Book: at `l | N` Step 1 fails (`r_E != deg` possible: 99a1, 726a1,
539d1), Step 3 fails (`l in S_f`; Fontaine-Laffaille needs `l` not dividing `N`), and the Euler factor at `q = l` is not the relevant local
quantity; what would replace it is a local deformation condition at `l` (`\Cref{ch:congruence}` 13.3). (2) Prove the corrected identity
of Remark rem:ns for 3Ns curves. Book: two inputs are missing, `H^1_f(Q, ad V_3 E) = 0` (point 67) and Taylor-Wiles for a residual
representation induced from `Q(sqrt(-3))`; the data (failures by exactly one; equality of Theorem thm:quant in the `8` 3Ns pairs) are
consistent with it. (3) Compute `Tam_q(ad T)` at additive primes and the Selmer length. Book (important_notes.md point 64): the first
half is ANSWERED: `Tam_q(ad T)` is trivial at every potentially good prime (`\Cref{ch:blochkato}` 9.3), and at potentially multiplicative
primes it is given by Lemma lem:tamfactor (A4.12 Step 7); with the equality of A4.12 the Selmer length is then `v_l(deg varphi_E) -
B^expl_l(E)`, computed curve by curve (below `10,000`, at `l = 3`: excess `0, 1, 2, 3, >= 4` for `8,688`, `3,288`, `942`, `248`, `37` of `13,203` curves,
never negative); what remains is to explain that length. (4) The Eisenstein deficit and the cuspidal subgroup (Mazur77;
`\Cref{ch:moddeg}` 11). (5) Section sec:two and Watkins's conjecture.
**Commentary (important_notes.md point 64).** Open question 3 is half answered; the book says which half and reduces the question to
the Selmer group.

### A9. The appendix: reproducibility and the function `rule(E, l)` (Section 21.19)

**A9.1 `pari-rule`** (construction (the paper's `scripts/euler_rule.gp`); *explained line by line*, outputs verified in PARI/GP
2.17.2; reference: PARI manual (`ellglobalred`, `elllocalred`, `lfunsympow`, `lfuneuler`, `ellmoddegree`, `elldivpol`, `factor`);
`\Cref{ch:reduction}` 5.5, `\Cref{ch:lfunctions}` 11.1, 11.2, `\Cref{ch:computation}` 5.1 to 5.4, 6.1 to 6.7, R1, R2; paper use: the
appendix).
Line by line (`rule(E, l, {iii = 0})`): (1) `R = ellglobalred(E)`: `[N, [u,r,s,t], c, faN, L]`; `P = R[4][,1]` the bad primes; `K = R[5]` the
`elllocalred` data `[f_p, kod, [u,r,s,t], c_p]`, so `K[i][2]` is the Kodaira code at `P[i]`. (2) `S = lfunsympow(E, 2)`: `L(Sym f, s)`, with `L_p(Sym f,
s) = L_p(A_f, s - 1)`; `b` the bound, `j = E.j`. (3) Loop over bad `q`: `k` the code, `vj = valuation(j, q)`. (4) If `q != l`: `F = 1/lfuneuler(S, q)` is
`P_q(x)` (verified: `lfuneuler(S, 11) = 1/(11*x + 1)` for 121a1); `r = P_q(q^{-2}) = L_q(A_f, 1)^{-1}`; if `k >= 5` (type `I_n`, `n >= 1`) divide by the naive
factor `1 - q^{-2}`, so `r = 1`, `e = 0`; at additive `q` the naive factor is `1`; `e = v_l(r)` unless the type is `III` or `III^*` (`abs(k) == 3`) and
`iii = 0`: Definition def:terms verbatim. (5) If `q == l = 3`: `e = w_3(E)` (codes `4, 2, -3` give `1`; `-4, -2` give `2`; others `0`). (6) `t = v_l(-vj)` if
`vj < 0`, at every bad `q`, `q = l` included (A1.1). (7) `b += e + t`. (8) If `iii` and `l = 3`, subtract `ns3(E)` (the correction `h_3(E)`, which is `1`
exactly for image 3Ns, A4.11, A5.1). (9) Return `[v_l(ellmoddegree(E)), b]`.
`ns3(E)`: factor `psi_3 = elldivpol(E, 3)` over `Q` (PARI drops the content `3`); true iff two irreducible factors, the first of degree `2`
(pattern `2 + 2`). For non-CM curves with `E[3]` irreducible this is image 3Ns (A1.12 data check).
Modes: `rule(E, l)` is the "III-free" bound without correction; `rule(E, l, 1)` is (eq:rule).
Verified outputs (PARI/GP 2.17.2, `\Cref{ch:computation}` R1): 121a1 `[1, 1]` (both modes); 726a1 `[2, 2]` in both modes, the type `III`
term and the correction cancelling; 539c1 `[2, 2]` at `l = 3`; 980i1 `[2, 2]` at `l = 3` and `[1, 1]` at `l = 5`; 99a1 `[0, 0]`; 336f1 `[1, 1]`; 1232l1 `[2,
2]`; 592c1 `[1, 1]` at `l = 5`; 11a1 `[0, 1]` at `l = 5` (Eisenstein). The paper ran PARI 2.15; the book's runs are 2.17.2 (W6).
Points the book must make. (a) `ellmoddegree(E)` returns the degree of the modular parametrisation of the GIVEN model (for a
non-optimal curve, not the paper's quantity): 990h1 gives `[4, 3]` while the optimal 990h3 gives `[3, 3]`; 11a3 at `l = 5` gives `[-1, 0]`. (b)
`valuation(j, q)` of `j = 0` is `+oo`, so `t = 0`. (c) The test `abs(k) != 3` excludes `III` and `III^*` at `q != l`, while at `q = l = 3` the `III^*` weight
`w_3 = 1` is counted even when `iii = 0` (it is not an Euler term). (d) The PARI codes `n + 4`, `-(n + 4)` are valid for `n >= 1` only (A9.2).
**Commentary (important_notes.md point 78).** `rule` gives wrong-looking answers when misused: on a non-optimal curve (990h1: `[4, 3]`;
990h3, the optimal curve of the class, `[3, 3]`; 11a3 at `l = 5`: `[-1, 0]`) and at an Eisenstein prime (11a1 at `l = 5`: `[0, 1]`). The appendix should
say that `E` must be the optimal curve and `E[l]` irreducible (and, for the statement of Conjecture conj:euler, `E` without CM). The book
says so.
**Commentary (important_notes.md point 80, first item).** "`ellmoddegree` needs `parisizemax` of a few hundred megabytes for
conductors in the thousands": in PARI 2.17.2 at most about `32` MB suffices below conductor `10,000` (true for 2.15 at larger conductors).
Low importance; one clause.

**A9.2 `kodaira-codes`** (convention; *stated*; reference: PARI manual (`elllocalred`), `\Cref{ch:reduction}` 5.5, Appendix B
B-C11(c); paper use: the appendix).
Table (PARI code: Kodaira symbol, `#Phig`, conductor exponent at `q >= 5`, `v_q(Delta_min)` at `q >= 5`): `1`: `I_0`, `1`, `0`, `0`; `n + 4` (`n >= 1`): `I_n`,
`n`, `1`, `n`; `2`: `II`, `1`, `2`, `2`; `3`: `III`, `2`, `2`, `3`; `4`: `IV`, `3`, `2`, `4`; `-1`: `I_0^*`, `4`, `2`, `6`; `-(n + 4)` (`n >= 1`): `I_n^*`, `4`, `2`, `n + 6`; `-2`:
`II^*`, `1`, `2`, `10`; `-3`: `III^*`, `2`, `2`, `9`; `-4`: `IV^*`, `3`, `2`, `8`. (Hence `k >= 5` detects multiplicative reduction.)
**Commentary (important_notes.md point 52).** The paper's list "`n + 4` for `I_n`, `-(n + 4)` for `I_n^*`" is valid for `n >= 1` only; `I_0` is `1`
and `I_0^*` is `-1`, not `4` and `-4` (which are `IV` and `IV^*`). Low importance; the table above is the correction.

**A9.3 `reproducibility`** (description; *stated*; `\Cref{ch:computation}` 12.1, 12.2; paper use: the appendix's first and last
paragraphs, the statement on the use of an AI system).
Content: the repository and directory named in the paper (scripts for Euler factors, the rule, the boundary, the Tamagawa test, the
corollary forms; pinned data commit; rerun from a clean clone reproduced Table tab:counts; Lemma lem:twist(ii) checked on `4,577` random
pairs; Lemma lem:euler against `lfunsympow` on every curve). The book lists these as the paper's claims and does not reproduce the
scripts (the contents of the repository were not inspected); the book's own reproduction is `\Cref{ch:computation}` Part 7 (Lemma
lem:twist on `85,848` pairs, Lemma lem:euler on `67,745`, `ellmoddegree` against Cremona's `degphi` file on all `38,042` optimal curves below
`10,000`, no mismatch). The statement on the use of an AI system is part of the paper; the tour mentions it in one sentence in Section
21.1 (how the paper was produced, and that every count can be rerun), with no further commentary.

## Part B. Devices of the tour (Sections 21.20 and 21.21)

### B1. Dependency diagram of the paper's results, as corrected (Section 21.20)

To be drawn as a `tikzcd` or plain `tabular` diagram (no colour needed). Arrows mean "is used in the proof of". Imported statements in
square brackets; the book's additions (results the paper does not have, which change the structure) are marked `(book)`.

```
[Kraus90]                                         => lem:IV (q >= 5); rem:types
[Neron component groups; Ch. 10, 4.5] (book)      => lem:IV at q = 2 (Ch. 11, 4.4) => prop:forms (no exception); thm:qual (a) at q = 2
lem:IV                                            => thm:qual (a), (b)
[Tate curve; DDT 3.1(e)]                          => lem:tamagawa-exp
lem:tamagawa-exp                                  => thm:qual (c); rem:ko(2); Section 1.5
[Tate's algorithm, Silverman IV.9]                => lem:twist (i), (ii)
[Atkin-Li 3.1]                                    => lem:twist (iii)
lem:twist                                         => lem:euler; thm:qual (b), (c); thm:twist; thm:quant
[Kraus90] + lem:twist                             => lem:euler => table of Section 1 => def:terms (values of e_l)
lem:euler                                         => thm:quant Step 3; prop:forms
[FPR94 I.4.2.2] + [Ch. 16, 17 cohomology]         => lem:tamfactor (all potentially multiplicative q, q = 2 included)
[Ch. 18, 9.3: Tam trivial at pot. good q] (book)  => explicit Tamagawa terms in eq:identity; Open question 3 (first half)
lem:tamfactor                                     => thm:main Step 7 (eq:thm); rem:ko(1); sec:tam
[Ribet83 2.2; AU96 2.1]                           => lem:crit
lem:crit                                          => lem:old; lem:hecke (paper's route); thm:twist; thm:quant Step 1
[Edixhoven92; Atkin-Lehner 3; DDT 3.1(e); Chebotarev; Brauer-Nesbitt] => lem:old
lem:old + [DDT 3.15] + [ARS12 2.2]                => thm:qual
[DDT 4.17] = lem:ddt417                           => thm:quant Step 2 (and the paper's route to lem:hecke)
[projection formula; Ch. 14, 9.1 to 9.3] (book) + [DFG04 Part 7 checklist] => lem:hecke WITH EQUALITY (no freeness)
[ARS12 2.2] + lem:hecke                           => thm:main Step 1; thm:quant Step 4
[Tilouine97; RibetStein 3.5] => rem:free          => (no longer used by any proof; explains Hecke = cohomological ideals)
[DFG04 Prop 1.4(c)] = thm:dfg14                   => thm:main Step 2; thm:quant Step 3
[DFG04 Thm 3.7 = 0.2] = thm:dfg37                 => thm:main Step 3
[DFG04 Thm 2.7] = thm:dfg27                       => H^1_f(Q, V^D) = 0 in lem:dfg21 (H^0(Q, V^D) = 0 is automatic)
[DFG04 Lemma 2.1] = lem:dfg21                     => thm:main Step 4; rem:ns (conditionally)
[FPR94; DFG04 2.15, (57)] = lem:fpr               => thm:main Step 5; rem:ns
[Clifford theory; group theory of GL_2(F_3)]      => prop:ns <=> lem:h0 => thm:main Step 4; conj:euler (h_l); sec:anomaly
[inertia at l: Ch. 11, 5.3, 8.2] (book)           => "l not in S_f" automatic for l >= 5, l not dividing N, E[l] irreducible
thm:main (equality)                               => prop:forms => (eq:main), (eq:twist) under the hypothesis
thm:twist                                         => thm:quant (inequality)
thm:main (equality) for E and for E_S (book)      => thm:quant with EQUALITY for l not in S_f (remark (2), point 74)
lem:dfg21 + lem:fpr + lem:h0 + [H^1_f(Q, V^D) = 0, assumed] => rem:ns => conj:euler (the correction term)
[Ch. 9, 9.8: no rational cyclic 27-isogeny] (book) => conj:eis: D <= 2 is a theorem given the first bound
data (Section 6)                                  => conj:euler (w_3, h_l); conj:eis (first bound); sec:two
```

The three spines: (i) local: lem:tamagawa-exp, lem:IV, lem:twist, lem:euler, lem:tamfactor (with the two additions on type `IV` at `2`
and Tamagawa factors at potentially good primes); (ii) congruences: lem:crit, lem:old, optimal level, thm:qual; (iii) Selmer:
lem:hecke (now an equality, through the projection formula, not through rem:free), thm:dfg14, thm:dfg37, thm:dfg27, lem:dfg21,
lem:fpr, lem:h0, thm:main. Theorem thm:quant uses (i) and (ii), and from (iii) only thm:dfg14, lem:ddt417 and lem:hecke; it never uses
thm:dfg37, which is why its inequality needs no hypothesis on `Q(sqrt(l*))`; its EQUALITY uses thm:main for `E` and `E_S`, hence `l` not in
`S_f`. Multiplicity one (rem:free) feeds nothing.

### B2. Hypothesis table, as corrected (Section 21.20)

Aligned with `\Cref{ch:congruence}` 9.3.

| hypothesis | where it is used | what fails without it |
|-|-|-|
| `l` odd | Lemma lem:tamfactor (`2` a unit in `(t - 1)M`); trace form `T^D = A(1)`; real place (`H^1(R, T^D) = 0`); `S_f` contains `2`; Lemma lem:h0 (complex conjugation gives absolute irreducibility; the determinant argument); optimal-level theorem (DDT 3.15 is for odd `l`); Lemma lem:old at `p = l` | everything in Sections 2 to 4 at `l = 2`; Section sec:two shows a different `2`-adic pattern (types `III, III^*, I_n^*` weigh `3`, `I_0^*` weighs `1`), and Watkins's conjecture brings in the rank |
| `l` not dividing `N` (and `l^2` not dividing `N`) | ARS12 Theorem 2.2 (only `l^2` not dividing `N`); DFG04 (`l` not in `S_f`; Fontaine-Laffaille at `l`); Lemma lem:old at `p = l`; optimal-level theorem (`delta = 0`, weight `2`, trivial nebentypus); Lemmas lem:euler, lem:fpr, lem:tamfactor (`q != l`) | 99a1 (`N = 9 * 11`): `deg = 4`, `r = 12` (recomputed), so `r_E` and the degree differ at `l = 3`, and `H^1(X_0(99), Z_3)_m` is not free; 726a1 (`r = 1584`, `deg 144`, at `11`); 539d1 (`r = 504`, `deg 72`, at `7`); at `q = l = 3` the Euler factor is replaced by the empirical weights `w_3`; no theorem covers `l | N`, though the data show (eq:rule) there |
| `rho bar` absolutely irreducible on `Gal(Qbar/Q(sqrt(l*)))` (`l` not in `S_f`) | DFG04 Theorem 3.7 (Taylor-Wiles) and Theorem 2.7 (`H^1_f(Q, V^D) = 0`); Lemma lem:h0 (`h_l = 0`); optimal-level theorem at `l = 3` (Theorem thm:qual); the equality in Theorem thm:quant | for `l >= 5`, `l` not dividing `N`, nothing beyond `E[l]` irreducible: the condition is AUTOMATIC (point 47); at `l = 3` it fails exactly for image 3Ns, where (eq:thm) fails for `31%, 23%, 18%` of the curves, by exactly one (726a1: bound `3` with the `q = l` terms, `v_3(deg) = 2`); the correction `h_3(E) = 1` repairs it conditionally (Remark rem:ns). Theorem thm:quant's inequality does not need it |
| `rho bar` irreducible (weaker; implied by the previous) | Theorem thm:dfg14 (Ihara's lemma); the non-Eisenstein `m` (DFG04's integral structure agrees with `H^1(X_0(N), Z_l)` there); Lemma lem:old (Brauer-Nesbitt); Theorem thm:quant; Theorem thm:qual | Eisenstein case: 539a1 (image 3B, `I_2^*` at `7`): `e_3 = 1`, `v_3(deg) = 0`; 539d1 at `l = 5` (image 5B.4.1, `I_0^*` at `7`): `e_5 = 1`, `v_5(deg) = 0`; 98a1 (`I_1^*` at `7`, `E[3]` reducible); only the weaker (eq:main) survives, with the torsion-controlled deficit of Conjecture conj:eis (20a1: `D = 1 = v_3(#E(Q)_tors)`; 14a1: `D = 2`) |
| `X_0(N)`-optimality | ARS12; the definition of `deg varphi_E`; Lemma lem:hecke's equality (`M_{f,lambda} = varphi_E^* H^1(E)` needs the optimal map); `rule` (`ellmoddegree` of the given model) | nothing at `l` when `E[l]` is irreducible: the curves of the class are linked by isogenies of degree prime to `l`, so `v_l(deg)`, `v_l(n_q)`, `e_l`, `t_l`, `ad T` and `h_l` are class invariants (point 27; `\Cref{ch:ellcurves}` 9.9, `\Cref{ch:moddeg}` 6.4); it matters for Conjecture conj:eis and for `rule` (990h1 gives `[4, 3]`, the optimal 990h3 `[3, 3]`) |
| multiplicity one (`H^1(X_0(N), Z_l)_m` free over `T_m`) | in the paper: the equality in (eq:identity) (via Lemma lem:ddt417 in Lemma lem:hecke) and the equality in Theorem thm:quant (remark (2)); in the book: NOWHERE | nothing: (eq:identity) is an equality for `l` not in `S_f` by the projection formula (points 39, 56, 73), Theorem thm:quant's middle term needs no freeness (point 39) and its equality follows from (eq:identity) (point 74). Freeness does hold in the paper's range (Remark rem:free) and fails for `l | N` (99a1 at `3`) |

The book adds one sentence under the table: for `l` not dividing `2N`, the hypotheses of Theorem thm:main are those of DFG04's Theorem 0.1
for weight `2` and trivial character, i.e. "`E[l]` irreducible and not (`l = 3` and image 3Ns)", plus optimality, which is harmless at `l`.

### B3. Statements imported from the literature, with the paper's numbering (Section 21.20)

Rule for the book (PLAN.md 3): numbers are given as the paper cites them. "Verified" means checked against the published source by an
outline agent (for DFG04: the Chapter 20 outline, Part 7, read from the published text, Ann. Sci. Ec. Norm. Sup. (4) 37 (2004), 663-727);
"as cited" means taken from the paper and not checked; the writer verifies these before printing or replaces them by section
references listed in the Notes. **Warning:** a 2025 arXiv version of DFG04 (arXiv:2512.02348, a longer text dated "August 2001, with minor
update December 2025") uses DIFFERENT numbering (its Sections 1.1 to 3.5 do not match the published 1.1 to 3.2); every DFG04 number in the
paper and the book refers to the published version, and the book's bibliography entry must say so.

| citation (as in the paper) | exact content used | where in the paper | book item | status |
|-|-|-|-|-|
| DFG04 Theorem 0.1 (= Theorem 2.15) | Bloch-Kato conjecture for `A_f`, `A_f(1)` at `lambda` not in `S_f` | Section 1.2 | A1.4, B2 | verified |
| DFG04 Theorem 0.2 (= Theorem 3.7) | `H^1_Sigma` has length `v_lambda(eta^Sigma)` for `Sigma` containing the primes dividing `N`, `lambda` not in `S_f` | Section 4.2 | A4.7 | verified |
| DFG04 Theorem 2.7 | `H^0 = H^1_f = 0` for `A_f` and `B_f = A_f(1)`, `lambda` not in `S_f` | Theorem thm:dfg27 | A4.8 | verified |
| DFG04 Theorem 3.7 | length of `H^1_Sigma(Q, W)` is `v_lambda(eta^Sigma)`, `Sigma` finite, `l` not in `Sigma`, minimally ramified outside `Sigma`; covers `l = 3` in weight `2` | Theorem thm:dfg37 | A4.7 | verified |
| DFG04 Proposition 1.4(c) | `eta^Sigma = eta^empty prod L_p^nv(A_f, 1)^{-1}` for `M bar_{f,lambda}` irreducible | Theorem thm:dfg14 | A4.2 | verified |
| DFG04 Lemma 2.1 | the four-term sequence (DFG04's hypothesis on `Sigma` is implied by the paper's) | Lemma lem:dfg21 | A4.9 | verified |
| DFG04 Theorem 2.15 (proof) | FPR local formula `Fitt H^1_f(Q_p, M) = L_p(M, 0)^{-1} Tam^0_p(M)` | Lemma lem:fpr | A4.10 | verified |
| DFG04 (31) | `S_f = {lambda : lambda | Nk!, or M bar_{f,lambda} not abs. irreducible on G_{Q(sqrt(l*))}}` | Section 4.2 | A4.6 | verified |
| DFG04 (57) | `Tam^0_p(M) = Tam^0_p(M^D)`, `p != l`, general | Lemma lem:fpr | A4.10 | verified; multiplicative case also by hand (Exercise 8) |
| DFG04 p. 708 | `Tam^0_p(M) = Fitt(H^1(I_p, M)_tor)^{G_{Q_p}}` (same misplaced superscript as the paper, point 37) | Section 1.2, Lemma lem:tamfactor | A1.3 | verified |
| DFG04 Lemma 2.12 | `<f, f>` with the NAIVE value `L^nv(A_f, 1)` (from Hida81 Theorem 5.1) | Section 1 | A1.0 | verified |
| DFG04 Sections 1.1.1, 1.5.3, 1.6.1, 1.6.2, 1.7.2, 1.7.3, 1.8.2, 2.1; (13), (14), (18), (22) | geometric Frobenius; the operator `[UwU]_omega = w_N`; kernel lattice; ideal of values; self-adjointness; `H^1_Sigma`; `M_{f,lambda}` dual of the Tate module | Sections 1.1, 4.1, 4.2 | C2, A4.1, A4.6 | verified (the integral structure agrees with `H^1(X_0(N), Z_l)` at non-Eisenstein `m`) |
| DDT Theorem 3.1(e) | local structure at a multiplicative prime | Lemma lem:old, Lemma lem:tamfactor | A2.7, A3.3 | as cited |
| DDT Theorem 3.15 | optimal level for odd `l`, with the `Q(sqrt(-3))` condition at `l = 3` | Section 3 | A3.4 | as cited |
| DDT Lemma 4.17 | numerical criterion; inequality half used | Lemma lem:ddt417 | A4.3 | as cited |
| DDT Section 4.4 | Hecke adjoints and the twisted pairing | Section 4.1 | A4.1 | as cited |
| FPR94 I.4.2.2 | `Tam_p(M) = Fitt((H^1(I_p, M)_tor)^{G_{Q_p}})` for `p != l` | Section 1.2, Lemmas lem:tamfactor, lem:fpr | A1.3, A2.7, A4.10 | as cited (DFG04's recollection verified) |
| ARS12 Theorem 2.2 | `deg varphi_E | r_E`; equal `p`-valuations when `p^2` does not divide `N` | Sections 1, 3, Lemma lem:hecke | A3.1, A4.4 | as cited; the divisibility reproved in `\Cref{ch:moddeg}` 9.4 |
| ARS12 Section 2; Section 3; Table 1 | abc connection; perfect pairing; 99A1 with `deg 4`, `r = 12` | Sections 1, 3 | A3.1, A3.7, B4 | `deg(99a1) = 4` and `r(99a1) = 12` both recomputed (`\Cref{ch:moddeg}` 8.5, `\Cref{ch:hecke}` 11.2) |
| Atkin-Li Theorem 3.1 | twist of a newform of level `M`, `q^2` not dividing `M`, is new of level `lcm(M, q^2)` | Lemma lem:twist(iii) | A2.4 | as cited |
| Atkin-Lehner Theorem 3 | `a_p = 0` for a newform with `p^2 | M` | Lemma lem:old | A3.3 | as cited |
| Ribet83 Theorem 2.2; AU96 Lemma 2.1 | perfect pairing `S_2(Gamma_0(N); Z) x T -> Z` | Lemma lem:crit | A3.2 | as cited (the pairing is proved in `\Cref{ch:hecke}` 4.1) |
| Ribet-Stein Theorem 3.5 | multiplicity one for `J_1(N)[m]`, exception Serre weight `l` | Remark rem:free | A4.5 | as cited |
| Kim-Ota Theorem 1.1; Definition 2.12 | `ord eta_f(N) = ord eta_f(N^+, N^-) + sum t_f(q)`; the Tamagawa exponent | Remark rem:ko(2), Section 1.5 | A1.9, A4.13 | as cited |
| Kraus90 | order of the image of inertia `12/gcd(v_q(Delta), 12)` for `q >= 5` | Lemmas lem:IV, lem:euler | A2.2, A2.5 | no number cited |
| Zywina15 | possible mod 3 images | Proposition prop:ns | A5.1 | by section (point 4); the list is proved directly |
| Sutherland16 | labels 3Ns, 3Cs.1.1, 3B.1.1 | Sections 1.3, sec:anomaly, sec:eis | A6.7, A6.10 | consistent with Cremona's `galrep` (checked); definitions against the source still to check (point 3) |
| Silverman ATAEC IV.9; V.3, V.5 | Tate's algorithm; Tate curves and their twists | Sections 1.4, 2 | A1.6, A2.1, A2.4 | standard |
| Edixhoven92 Section 2 | `rho bar|_{D_l}` determines `a_l mod lambda` | Lemma lem:old | A3.3 | as cited |
| Carayol89; Ribet90; Diamond95 | Serre conductor divides `N`; level lowering | Section 3 | A3.4 | as cited |
| Tilouine97 | `J_0(N)[m]` two-dimensional implies Gorenstein and freeness | Remark rem:free | A4.5 | as cited |
| CalegariEmerton09 | odd modular degree | Section sec:two | A7.1 | as cited; the paraphrase fails for CM curves (point 57) |
| Mazur77; Watkins02; Zagier85; Cremona97; Flach92; Hida81; the `l = 2` literature | context | Sections 1, 6, 7, Open questions | A1.0, A1.9, A7.1, A8.1 | as cited |

### B4. Worked verifications of the numerical examples (Section 21.21)

All values below are PARI-verified (PARI/GP 2.17.2 through cypari2) or recomputed exactly, as recorded in important_notes.md and in
the outlines cited: Kodaira types and local data from `ellglobalred`; `P_q` from `lfuneuler(lfunsympow(E, 2), q)`; modular degrees from
`ellmoddegree`, agreeing with Cremona's `degphi` file on all `38,042` optimal curves below `10,000`; congruence numbers by the lattice
method (`\Cref{ch:moddeg}` 8.5, `\Cref{ch:hecke}` 11.2); Tate data from `ellinit(E, O(q^30))` (`\Cref{ch:computation}` 3.5; `ellinit(E, q)`
reduces mod `q` and is not the `q`-adic curve, important_notes.md B27); images from Cremona's `galrep` file and `elldivpol`. The writer
prints each verification as a short table with the source item cited.

1. **121a1** `[1,1,1,-30,-76]`. Type `II` at `11` (local data `[2, 2, 1]`); `P_11(X) = 1 + 11X`, `P_11(11^{-2}) = 12/11`, `e_3(E, 11) = v_3(12/11) = 1`
   (`chi_{-3}(11) = -1`); `t_3 = 0`; bound `1`; `deg = 6`, `r = 6`: attained; `rule(E, 3) = [1, 1]` in both modes; `B^main_3 = 0`, `B^tw_3 = 1` (the curve
   on which (eq:twist) is strictly stronger than (eq:main)). Twist by `-11`: 121c2 (type `IV^*`); the optimal curve 121c1 of that class has type
   `IV`, `deg 6`, `r = 6` (case (c) of Theorem thm:twist with equality). `f_{121a} = f_{121d} = f_{11a} tensor chi_{-11} mod 3` for every `n` (Sturm bound
   `22`). Mod `3` image surjective. Theorem thm:main applies (`3` does not divide `121`): `H^1_f(Q, ad T_3 tensor Q_3/Z_3) = 0` (A4.12).
2. **539c1** `[1,0,1,170,-3237]`. Types `I_3^*` at `7` (code `-7`), `I_2` at `11` (code `6`); `P_7 = 1 - X`, `P_7(7^{-2}) = 48/49`, `e_3(E, 7) = 1`, `t_3(E, 7) =
   1`, `t_3(E, 11) = 0`; bound `2`; `deg = 288 = 2^5 3^2`, `r = 288`: attained; `rule(E, 3) = [2, 2]`, `rule(E, 5) = [0, 0]`. Tate data at `7`: same `q_E` as
   77c1, `u bar = 5`, not a cube mod `7`, so no Tamagawa excess. Twist by `-7`: 77c1 (`I_3` at `7`, `a_7 = -1`, `deg 6 = r`); Theorem thm:quant: `v_3(288) =
   2 = v_3(6) + v_3(48)`, equality (A4.16). `f_{539c} = f_{539d} = f_{11a} tensor chi_{-7} mod 3` for every `n` (Sturm bound `112`); 539d2 is the twist of
   11a1. Level raising `11 -> 77` at `7`: `a_7(11a1) = -2`, `(7 + 1)^2 - 4 = 60 = 0 mod 3`. Mod `3` image surjective.
3. **980i1** `[0,0,0,1568,-72716]`. Types `IV^*` at `2` (code `-4`), `I_1` at `5`, `I_5^*` at `7` (code `-9`); `deg = 2880 = 2^6 3^2 5`, `r = 2880`. At `l = 3`
   (`3` does not divide `N`, image surjective): `P_2 = 1 + 2X`, `e_3(E, 2) = v_3(3/2) = 1` (a theorem, A1.8), `e_3(E, 7) = v_3(48/49) = 1`, bound `2 = v_3(2880)`;
   `rule(E, 3) = [2, 2]`; Theorem thm:quant with `S = {7}`: `E_S = 140b1` (also `IV^*` at `2`: `-7 = 1 mod 8`, so `chi_{-7}` is trivial on `G_{Q_2}`),
   `deg 60`, `2 = v_3(60) + v_3(48)`, equality. At `l = 5` (`5 | N`: outside the theorems): `t_5(E, 7) = 1`, `e_5 = 0` everywhere, `rule(E, 5) = [1, 1]`;
   the congruence is `f_{980i} = f_{980g} = f_{20a} tensor chi_{-7} mod 5` for every `n` (Sturm bound `336`); the twist of 20a1 by `-7` is 980g2, not a
   curve of class 980i (B20); `a_7(20a1) = 2`, `64 - 4 = 60 = 0 mod 5`.
4. **726a1** `[1,1,0,-35,-51]`. Local data `2`: `[1, 10, 2]` (`I_6`), `3`: `[1, 7, 1]` (`I_3`), `11`: `[2, 3, 2]` (`III`); image 3Ns, `psi_3 = (x^2 - x -
   74)(3x^2 + 8x + 20)`, `ns3 = 1`; `deg = 144 = 2^4 3^2`, `r = 1584 = 11 * 144` (gap at `11`, `11^2 | 726`). Breakdown at `l = 3` (`rule_terms`): `q = 2`: `P_2 = 1
   - X`, `e = 0`, `t = v_3(6) = 1`; `q = 3 = l`: `w_3 = 0`, `t = v_3(3) = 1`; `q = 11`: `P_11 = 1 + 11X`, `e_3 = v_3(12/11) = 1` (counted only with `iii = 1`).
   `rule(E, 3) = [2, 2]`; `rule(E, 3, 1) = 2 + 1 - 1 = 2`: `[2, 2]`, the cancellation the paper describes. Without the correction the bound is `3 > 2`:
   a violation by one, involving `p = 2 = -1 mod 3` with `t_3(E, 2) = 1`. With (eq:thm) read literally (terms at `q != 3` only) the bound is `2` and
   there is no violation (A6.2). `3 | N`, so Theorem thm:main does not apply at `l = 3` in any case.
5. **99A1** = Cremona 99a1 `[1,-1,1,-2,0]`. `N = 3^2 11`; type `III` at `3` (code `3`, `v_3(j) = 9`), `I_1` at `11`; `deg = 4`, `r = 12` (recomputed: the
   congruence `f_{99a} = f_{99b} = f_{99d} mod 3` beyond the Sturm bound `24`); `rule(E, 3) = [0, 0]` (`w_3 = 0` for type `III` at `3`; PARI's `P_3 = 1 + 3X`
   is not used at `q = l`). `v_3(deg) = 0 < 1 = v_3(r)`, allowed by ARS12 since `9 | N`; `H^1(X_0(99), Z_3)_m` is not free over `T_m` (`\Cref{ch:moddeg}` 9.7).
   No violation of Conjecture conj:euler at `l = 3` (mod `3` image surjective).
6. Further examples used in the book (same sources):
   **121d1** `[0,-1,1,-40,-221]` (`I_1^*` at `11`, twist of 11a3; `deg 24 = r`): `e_3 = v_3(120) = 1 = v_3(24)`; with 11a1 and 121d2 shows that `e_l` is
   not twist invariant (A1.1); Theorem thm:quant: `1 = 0 + 1`. **539d1** `[0,1,1,-16,-66]` (twist of 11a3 by `-7`, `I_0^*` at `7`, `deg 72`, `r = 504`):
   `P_7 = (1 - 7X)(1 + 10X + 49X^2)`, `e_3 = v_3(6) + v_3(60) = 2 = v_3(72)`; `e_5 = 1` but `v_5(72) = 0`, image 5B.4.1 (Eisenstein at `5`); `r` and `deg`
   differ at `7` (`7^2 | 539`). **539a1** (`I_2^*` at `7`, image 3B, `deg 320`): `e_3 = 1`, `v_3(deg) = 0`. **52a1** (`IV^*` at `2`, `I_2` at `13`, `deg 3`):
   `e_3(E, 2) = 1`; case (a) of Theorem thm:qual at `q = 2` (Serre conductor `26`, `g = f_{26b} - f_{26b}(2z)`). **336f1** (`II` at `2`, `P_2 = 1 + 2X`,
   `deg 24`, `rule(E, 3) = [1, 1]`), **1232l1** (`II^*` at `2`, `P_2 = (1 - 2X)(1 + 2X)^2`, `e_3(E, 2) = 2`, `deg 288`, `rule(E, 3) = [2, 2]`), **592c1**
   (`II^*` at `2`, `P_2 = (1 - 2X)(1 + 4X^2)`, `e_5(E, 2) = 1`, `deg 80`, `rule(E, 5) = [1, 1]`): the type at `2` does not determine `P_2`. **791a1**
   (`I_3` at `7`, `u bar = 6` a cube: Tamagawa excess `1`; explicit bound `2 = v_3(144)`, Selmer length `0`); **1184f1** (explicit bound `2`, `deg
   1728`, Selmer length `1`); **1748e1** (explicit bound `3`, `deg 3240`, Selmer length `1`). **20a1** (`IV^*` at `2`, `I_2` at `5`, torsion `Z/6`,
   image 3B.1.1, `deg 1`): `D = v_3(3) - 0 = 1 = v_3(#E(Q)_tors)`. **14a1** (image 3Cs.1.1, torsion `Z/6`, `I_6` at `2`, `I_3` at `7`, `deg 1`): `D = 2`.
   **714i1** (torsion `Z/9`, image 3B.1.1, `deg 1080`, `D = 2`). **11a1** at `l = 5` (image 5Cs.1.1, `rule(E, 5) = [0, 1]`, `u bar = 10` a fifth power,
   `v_5(Tam_11(ad T)) = 2`, `D = 1`): outside every theorem. **990h1/990h3** (`rule` `[4, 3]` versus `[3, 3]`: run `rule` on the optimal curve).

Arithmetic checks (all consistent): the `I_0^*` identity `(1 - alpha/(beta q))(1 - 1/q)(1 - beta/(alpha q)) = (q - 1)((q + 1)^2 - a^2)/q^3`; `e_3` for
`P_2 = 1 + 2X` is `v_3(3/2) = 1`; the sec:tam percentages (`45.05%`, `60.59%`, `67.03%`, `78.70%`); `364/1,170 = 31.1%`; `17 + 5 = 22`; `435/828 = 52.5%`;
`14,182/44,672 = 31.7%`; `0.532 x 867,578 = 461,551`.

## Part C. Where each point of important_notes.md is handled (Section 21.22)

The chapter's Section 21.22 "Corrections to the paper used in this book" is a `longtable` with one line per point about the paper:
paper location, the problem in one sentence, the book's statement (final state), the item. Status: E = error in a statement or proof
(the result survives unless said), G = gap, X = expository or notation, S = strengthening or new theorem, D = data or wording about
data, C = confirmation (no change). Every point is in its final state: addenda, corrections and settlements are applied.

| point | paper location | final state | status | handled at |
|-|-|-|-|-|
| 1 | proof of prop:ns, "non-abelian and faithful" | commutator argument added | G | A5.1, A1.12 |
| 2 | context of prop:ns | `N_s(F_3)` not maximal (index 2 in `N_ns(F_3)`) | X | A5.1 |
| 3 | Sutherland labels | consistent with `galrep`; check against Sutherland16 | X | A1.13, A6.7, A6.10, B3 |
| 4 | Zywina15, Dickson | cited by section; list proved directly | X | A5.1, B3 |
| 5 | lem:h0 finiteness; sec:anomaly `p < 1223` | determinant argument: `h_l = 0` (`l >= 5`), `h_3 <= 1`, CM allowed | E | A4.11, A6.7, A1.5 |
| 6 | Section 1.3: `chi_{l*}` | criterion is `rho bar = rho bar tensor chi bar_l`, forcing `l = 3` | E | A1.5 |
| 7 (+ addendum) | lem:tamfactor, "image of `kappa`" | meaningful via the splitting by `q`; `c'` defined mod `(n, q - 1)` | X | A2.7 step (7) |
| 8 | lem:tamagawa-exp, `u` | Tate parameter `q_E`; two steps separated | X | A2.1 |
| 9 | prop:ns "without CM" | not used; dropped | X | A5.1 |
| 10 | lem:old, lem:h0: "irreducible" | "absolutely irreducible" (complex conjugation) | G | A3.3, A4.11 |
| 11 | Frobenius conventions | `L`-factors geometric, lem:tamfactor arithmetic (DFG04 geometric, verified) | X | C2, A2.5, A2.7, A4.9, A4.10 |
| 12 | lem:euler, `End_{I_q}(V)` | `Q_l tensor Q(zeta_3)`, `T`-version `Z_l tensor Z[zeta_3]` | X | A2.5 |
| 13 | lem:IV, `Z_3[sigma]/(...)` | `Z_3[X]/(X^2 + X + 1)` | X | A2.2 |
| 14 | lem:h0, CM alternative | impossible when `l` does not divide `N`; moot | X | A4.11 |
| 15 (corrected) | def:terms, twist invariance | true for `t_l`, false for `e_l` at the twisting prime (11a1/121d2) | E | A1.1 |
| 16 | after thm:twist, "strict only in case (b)" | strict in (a) and (b) | D | A4.14 |
| 17 | conj:eis, sec:eis, `D <= 2` | a theorem (no rational cyclic 27-isogeny) | S | A1.13, A6.10 |
| 18 | proof of thm:main, `I_n^*` at `2` | local argument covers `q = 2` | G | A4.12 Step 7 |
| 19 (corrected) | lem:ddt417, `wp cap I = 0` | two-line proof (not "T reduced") | G | A4.3 |
| 20 | thm:qual (b), (c), `h != f` | `h tensor chi` is the depletion of `g`; strong multiplicity one | E | A3.5 |
| 21 | example 980i1 | `5 | 980`: illustrates the congruence only | X | A3.6 |
| 22 | rem:types | complete grouping (all additive types but `IV, IV^*`; `I_0^*` lowers) | X | A2.3 |
| 23 | sec:tam, `c_q` | class `c(u)`, not the Tamagawa number | X | A2.7, A6.4 |
| 24 (revised by 39) | abstract, "elementary" | only Step 1 elementary; no multiplicity one needed | X | A1.0, A1.11, A4.15 |
| 25 | abstract, ranges and "a third" | precise ranges; `31%, 23%, 18%` | D | A1.0, A6.1 |
| 26 | Section 4.2, homothety | `M_{f,lambda}` is the dual of `T_l E` | X | A4.1, A4.6 |
| 27 | optimality | irrelevant at `l` when `E[l]` irreducible | C | B2 |
| 28 | lem:twist proof, "tame" | right only for the listed exchanges | X | A2.4 |
| 29 | lem:twist (ii), invariants by `q` | write `q*` | X | A2.4 |
| 30 | intro, naive `L` as Rankin series | Rankin series differs; use Shimura's series | E | A1.0 |
| 31 | lem:tamfactor, class of `u` | of the reduction of `u`; `v_l(0) = v_l(q - 1)` | X | A2.7 |
| 32 | `chi_q` versus `chi_l` (paper) | `chi_{q*}`, never `chi_q` (D3); numerical `chi_d`; `chi_3^cyc` | X | C1, A2.2 (B-C6) |
| 33 | prop:ns, lem:h0, "Ind psi" | over `F_9`; descends to `F_3` | X | A5.1, A1.12 |
| 34 | lem:euler, "diagonal element" | the invariant line is spanned by `tau` | X | A2.5 |
| 35 | lem:hecke, "annihilator" | the other factors lie in the kernel | E | A4.4 |
| 36 | lem:hecke, thm:quant Step 2 | pairing perfect on the `m`-component (self-adjoint `e_m`) | G | A4.4, A4.15 |
| 37 | Section 1.2, `Tam_p` parenthesis | Fitting ideal of the invariants | X | A1.3 |
| 38 | lem:ddt417, orders | lengths, or finite residue field | X | A4.3 |
| 39 (confirmed by 56, 73) | thm:main, lem:hecke, rem:free | `v_l(deg) = v(eta^empty)`; (eq:identity) an equality for `l` not in `S_f` | S | A1.4, A4.4, A4.12, B1, B2 |
| 40 | Section 4.2 | `M_{f,lambda} = varphi_E^* H^1(E) = T_l E(-1)` exactly | S | A4.1 |
| 41 | rem:free | `T_l J_0(N)` versus `H^1`: not Galois-equivariant; freeness transfers | X | A4.5 |
| 42 | lem:tamfactor, corner `kappa` | corner `eps kappa` | E | A2.7, A2.5 |
| 43 (settled) | prop:forms exception; thm:qual (a) | a theorem: `P_2 = 1 + 2X` for `IV, IV^*` at `2`; (a) extends to `q = 2` | S | A1.8, A1.10, A2.2, A2.6, A3.5 |
| 44 | sec:eis, "split Cartan image 3Cs.1.1" | 3Cs.1.1 is `E[3] = Z/3 + mu_3`; split Cartan is 3Cs | X | A1.13, A6.10 |
| 45 | lem:twist (ii), the cubic | cubic with the sign `e = q*/q` | X | A2.4 |
| 46 | example of Section 3 | congruences for all `n` by Sturm's bound | S | A3.6 |
| 47 | Theorem thm:main hypothesis; sec:forms | `l` not in `S_f` automatic for `l >= 5`, `l` not dividing `N`, `E[l]` irreducible | S | A1.4, A4.6, A6.6, B2 |
| 48 | sec:anomaly observations | theorems about 3Ns curves | S | A5.2, A6.7 |
| 49 | rem:types, "conductor exponent" | of `rho bar_{E,3}`, not of `E`, for type `II` | X | A2.3 |
| 50 | rem:wild, sec:wild, type `II` at `2` | false in general (336f1, 1232l1) | E | A2.6, A6.8 |
| 51 | lem:twist (ii) at `q = 3` | the exchanges hold at `q = 3` too (optional) | S | A2.4, A1.6 |
| 52 | appendix, codes | `n + 4`, `-(n + 4)` only for `n >= 1` | X | A9.2 |
| 53 | def:terms versus (eq:rule), `rule` | `t_l` defined at `q = l` too | X | A1.1, A6.8 |
| 54 | thm:qual (c), `f' = f tensor chi` | `f' = f_{E'} = f^chi`; `f tensor chi` is its depletion | E | A3.5 |
| 55 | remark after the example, "wild" | the obstruction is `q = l` | X | A3.7 |
| 56 | refinement of 39; checklist | all five items verified (73) | C | A1.4, A4.1, A4.4 |
| 57 | sec:two, Calegari-Emerton | paraphrase fails for CM curves (27a1, 243b1) | E | A7.1 |
| 58 | remark on `l | N` | 726a1: `r = 1584`, `deg 144` | S | A3.1, A3.7 |
| 59 | thm:quant Step 1 | an equality (optional) | S | A4.15 |
| 60 | thm:quant, `q >= 5` | `q` odd suffices | S | A1.11, A4.15 |
| 61 | thm:quant Step 1 | the `T`-stable complement, not the Petersson one (paper right) | C | A4.15 |
| 62 | remark on `l | N` | 539d1: `r = 504`, `deg 72` | S | A3.1, A3.7 |
| 63 | lem:dfg21 | `H^0(Q, V^D) = 0` automatic | X | A4.8, A4.12 |
| 64 | Open question 3 | `Tam_q(ad T)` trivial at potentially good primes: first half answered | S | A1.3, A4.12, A8.1 |
| 65 | abstract, rem:ko(1) | needs `l | n_q`; raises by at least one | E | A1.0, A4.13 |
| 66 | abstract, `ad V_l E` | Selmer group of `ad T tensor Q_l/Z_l` | X | A1.0 |
| 67 | rem:ns, Section 1.3 | conditional on `H^1_f(Q, V^D) = 0` for 3Ns curves | G | A1.5, A5.2, A8.1 |
| 68 | sec:tam | `I_n^*` primes can be included; "exactly where" overstates | X | A6.4 |
| 69 | rem:wild, sec:wild | four shapes of `P_q` at every `q`; `2` can contribute at `l = 5` | S | A1.2, A2.6, A6.8 |
| 70 | intro (addendum to 30) | exact Rankin relation; Shimura's series | X | A1.0 |
| 71 | intro (optional) | `v_l(deg) = v_l(B_E) + sum e_l` | S | A1.0 |
| 72 | Section 1.1, `delta_p`, `L_p` at `p = l` | definitions for `p != l`; harmless | X | C1 |
| 73 | point 56 and Q1 | settled: DFG04 confirms; covers `l = 3`; arXiv numbering differs | C | A1.4, A4.1, A4.7, B3 |
| 74 | remark (2) after thm:quant | equality for `l` not in `S_f`, no multiplicity one | S | A1.11, A4.16, B1, B2 |
| 75 | lem:dfg21 hypothesis | a sufficient form of DFG04's | C | A4.9 |
| 76 | sec:eis, two sentences | 14a1 (torsion `Z/6`); order-9 curves have `D = 2` | D | A6.10 |
| 77 | sec:data, protocol | `h_l` never blind-tested; (eq:twist) status unstated | D | A6.1, A6.9 |
| 78 | appendix, `rule` | run on the optimal curve, `E[l]` irreducible | X | A9.1 |
| 79 | sec:sharp | shows strength, not validity; range-dependent | D | A6.3 |
| 80 | appendix memory; 3Ns counts | 32 MB in 2.17.2; `36` versus `24` | D | A9.1, A6.2, A6.7 |

Book-internal notes (not about the paper; they do not go into Section 21.22 but are applied in this outline):
B1, B7, B9, B25 (Frobenius in C2 and the opening: C2, opening paragraph, A2.5, A2.7, A4.9); B3 (A4.4 kernel, A4.6 dual: A4.4, A4.6);
B8 and B20 (twist pairs at curve level: A1.1, A3.6, A4.14, B4); B12 (A3.2 sentence: A3.2); B13 (type `IV` at `2`, `chi_{l*}` for `l >= 5`: A1.5,
A1.8, A2.6, A4.6); B16 (A2.6 false claim: A2.6); B18 (A3.5 case (c), A1.10: A3.5, A1.10); B19 (dependency diagram and hypothesis table
through rem:free; `r(99A1)`: B1, B2, A3.1, A3.7, B4); B21 (A2.7 step (7) `eps`, "no such map": A2.7); B22 (cite Chapter 18 items; the
"torsion of `H^1(Q_p, T^D)`" wording: A1.3, A2.7, A4.9, A4.10); B24 (conventions: C1 to C3); B25 (duals `^vee`, adjoints `^dagger`, `chi_3`
numerical: C3, A3.2, A2.2); B26 (A4.16 multiplicity one; "not checked against DFG04": A4.16, B3, A4.7); B27 (`alldegphi`; A6.1 blind
caveat; A6.10 slips: A6.1, A6.10, B4); B17 (lem:crit proved in Chapter 15: A3.2). Appendix B Part 3 entries: F1 (opening), F2 (C2(b)),
T1 (A2.5, A2.7 corner), T2 (A2.7 `c(u)`), D5 (A3.2), D6 (A4.1), X5 (A2.2 `chi_3^cyc`), L6 (A4.14 `iota_S`).

## 4. Section-by-section plan with target line counts

Lines of LaTeX. PLAN.md 7.3 allows Chapter 21 up to 2,800 lines; the total below (card excluded) is 2,795. The card ("Core results at
a glance") lists every A-item with its rigour tag (about 65 entries) and is excluded from the count as for every chapter. Compared with
the first plan (2,770): 21.2 grows by 30 (A1.0, the abstract corrections), 21.20 by 10 (the corrected diagram and table), 21.21 by 20
(PARI-verified data), 21.22 by 60 (80 points instead of 26), 21.1, 21.18 and 21.24 by 5 each (`+135`); to compensate, 21.3, 21.5, 21.6, 21.13
(the equality shortens Step 4 and the remark), 21.15, 21.16 and 21.23 lose 10 each, 21.8 loses 20 (lem:crit and lem:old are proved in
Chapter 15 and only walked through here), and the opening paragraph, 21.12, 21.17 and 21.19 lose 5 each (`-110`; the small-range
reproductions are cited from Chapter 22, not reprinted). Net `+25`.

| section | title | contents (items) | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | every A-item, stated as above, tagged, with `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | one paragraph: "all of it"; how to read the tour alongside the paper | 25 |
| 21.1 | Conventions and how to read the tour | C1, C2 (Frobenius, B-C2, B-C3), C3 (duals, B-C4); how Commentaries are marked; one sentence on the AI statement (A9.3) | 95 |
| 21.2 | The abstract, the introduction and the local terms | A1.0 (with the five corrections of the abstract), A1.1, A1.2, A1.3 | 140 |
| 21.3 | The theorem, the conjecture, the component-group forms | A1.4 (equality; reading of the hypotheses), A1.5, A1.6, A1.7, A1.8 (no exception) | 140 |
| 21.4 | History and the statements without the hypothesis | A1.9, A1.10 (with `q = 2`), A1.11 (with `q` odd and equality), A1.12, A1.13 (with `D <= 2` proved) | 110 |
| 21.5 | Tate curves and inertia | A2.1, A2.2, A2.3 | 100 |
| 21.6 | Twists and the omitted Euler factors | A2.4, A2.5, A2.6 (corrected Remark rem:wild) | 150 |
| 21.7 | The Tamagawa factor at a multiplicative prime | A2.7, every step, with the corner `eps kappa`, the identification of `c'` and the check for `M = T` | 130 |
| 21.8 | The congruence criterion and oldforms | A3.1, A3.2, A3.3 | 110 |
| 21.9 | Level lowering and the proof of Theorem thm:qual | A3.4, A3.5, A3.6 (Sturm, curve-level twists), A3.7 | 150 |
| 21.10 | Congruence ideals; the modular degree as a congruence ideal | A4.1, A4.2, A4.3, A4.4 (equality), A4.5 | 150 |
| 21.11 | The adjoint Selmer group and the proof of Theorem thm:main | A4.6 to A4.13 (Step 7 with explicit Tamagawa terms) | 190 |
| 21.12 | Twist monotonicity | A4.14 (with the data paragraph and its correction) | 75 |
| 21.13 | Theorem thm:quant and its equality | A4.15, A4.16 | 140 |
| 21.14 | The boundary of the hypothesis | A5.1, A5.2 (conditional identity; structure of 3Ns curves) | 90 |
| 21.15 | The computations I: data, protocol, the rule, calibration | A6.1 (test-status table), A6.2, A6.3 | 100 |
| 21.16 | The computations II: Tamagawa factors, isolated terms, corollary forms | A6.4, A6.5, A6.6 | 80 |
| 21.17 | The computations III: 3Ns, wild primes, out of table, Eisenstein | A6.7, A6.8, A6.9, A6.10 | 115 |
| 21.18 | The prime 2 and the open questions | A7.1, A8.1 (Open question 3 half answered) | 65 |
| 21.19 | The appendix: the function `rule(E, l)` | A9.1 (listing, line-by-line table, verified outputs), A9.2, A9.3 | 95 |
| 21.20 | The map of the paper | B1 (corrected diagram), B2 (corrected hypothesis table), B3 (imported statements with statuses and the arXiv warning) | 160 |
| 21.21 | Worked verifications | B4 | 120 |
| 21.22 | Corrections to the paper used in this book | Part C table (80 lines) with a short introduction | 120 |
| 21.23 | Exercises | Section 6 below (18 exercises) | 100 |
| 21.24 | Notes and references | which numbers were verified (DFG04 against the published text), which are as cited (B3), the arXiv warning, sources and software for the data | 45 |
| | **total** | | **2795** |

## 5. Coverage table: every label and section of the paper

| paper label or section | items |
|-|-|
| abstract | A1.0 (corrections: points 24, 25, 39, 65, 66), A1.4, A1.11, A6.1, A6.9 |
| Section 1 (introduction, Petersson norm, ARS, naive versus true) | A1.0 (points 30, 70, 71), C1, A1.1, A3.1, A1.9 |
| Section 1.1 "The local terms" (`V, T, rho, A_f, delta_p, L_p, L_p^nv`, PARI) | C1, C2, C3, A1.1 |
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
| thm:quant | A1.11, A4.15, A4.16 |
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
| important_notes.md points 1 to 80 | Part C |

## 6. Exercises (Section 21.23)

Graded from routine to harder; most are "check the paper's claim that ...". Data for the curves are in B4; point counting by hand
or with a short program, or PARI, is allowed (the book says which).

1. Check that 121a1 `= [1,1,1,-30,-76]` has type `II` at `11` and `e_3(E, 11) = 1`: compute `Delta`, `c_4`, `j`, and `11 - chi_{-3}(11)`; compare
   with `deg varphi_E = 6`.
2. Check that the twist of 121a1 by `-11` has the same `j` and `v_11(Delta) = 8`, hence type `IV^*` (Lemma lem:twist(ii)); explain why the
   optimal curve 121c1 of the twisted class has type `IV` instead.
3. Check `a_p(121a1) = chi_{-11}(p) a_p(11a1) mod 3` for `p < 30`, `p != 3, 11`, by counting points; then use Sturm's bound to prove
   `f_{121a} = f_{121d} mod 3` for every `n`.
4. For 539c1 check the types `I_3^*` at `7` and `I_2` at `11`, the bound `e_3 + t_3 = 2` and its attainment (`deg = 288`). Identify the twist by `-7`
   (77c1, `deg 6`) and check Theorem thm:quant with equality.
5. Check the paper's sentence that strict inequality `v_l(deg varphi_E) > v_l(deg varphi_{E_q})` occurs "only in case (b)" against 539c1/77c1,
   980i1/140b1 and 121d1/11a3 at `l = 3`. Which case are they in? Deduce the corrected statement from Theorem thm:quant and its equality.
6. Show that `e_l(E, q)` is not invariant under quadratic twist by comparing 11a1 and 121d2 at `q = 11`, and 11a1 and 539d2 at `q = 7`. Prove
   the corrected invariance statement of A1.1.
7. For 539d1 (type `I_0^*` at `7`) compute `e_3(E, 7)` and `e_5(E, 7)` from `a_7(11a1) = -2`, compare with `deg = 72`, and explain the behaviour at
   `l = 5`. Do the same for 539a1 at `l = 3`.
8. Lemma lem:tamfactor in coordinates: for `l = 3`, `n = 9`, `q = 19` and each class `c in Z/9`, count the Frobenius-fixed points of `(Z/9) e + (Z/9)
   h` under `e -> e`, `h -> q^{-1}(h - 2 c eps e)` and check the formula. Then twist the action by `chi_l(Frob) = q` and show the count is unchanged
   (`Tam_q(A(1)) = Tam_q(A)`).
9. Check that `(chi_l eps, kappa; 0, eps)` is a homomorphism only if `eps` is trivial, and that `(chi_l eps, eps kappa; 0, eps)` always is
   (important_notes.md point 42). Check the paper's "as a check" for `M = T`.
10. Check the identity `(1 - alpha/(beta q))(1 - 1/q)(1 - beta/(alpha q)) = (q - 1)((q + 1)^2 - a^2)/q^3`, and prove that for type `IV` at `2`, `P_2(X) = 1 + 2X`
    and `e_3(E, 2) = 1` (A1.8).
11. Prove the sharp form of Lemma lem:h0: if `rho mod l^k = (rho tensor chi_l) mod l^k` then `chi_l^2 = 1 mod l^k` on `G_Q`; deduce `h_l(E) = 0` for `l >= 5`
    and `h_3(E) <= 1`. Where does the paper's own argument go wrong?
12. Check the table of `w_l(E, q) = max(v_l(#Phig_q(E)), v_l(#Phig_q(E^{(q)})))` for all Kodaira types at `q >= 5`, and the proof of Proposition
    prop:forms case by case, with no exception.
13. Prove that a non-CM elliptic curve over `Q` cannot have both `E[3] = Z/3 + mu_3` and a rational point of order `9`. Deduce `D <= 2` in
    Conjecture conj:eis from its first bound. Check `D = 2` for 14a1 and for 714i1.
14. For 726a1 determine the types at `2, 3, 11`, factor `psi_3`, and simulate `rule(E, 3)` and `rule(E, 3, 1)` by hand, recovering `[2, 2]`. Count
    the bound of (eq:thm) without correction in both readings (with and without the terms at `q = l`).
15. Lemma lem:ddt417: prove `wp cap I = 0` when `eta != 0` by the two-line argument of A4.3, and show that `U_2` at level `88` has a nonzero
    nilpotent part, so "`T` reduced" is not the reason.
16. The degree as a congruence ideal: for `E` optimal, use the projection formula to show that the ideal of values of `<x, w_N y>` on
    `varphi_E^* H^1(E, Z_l)` is `deg varphi_E Z_l`; check that the Gram determinant of a rank-two alternating form is the square of a
    generator of its ideal of values.
17. Check the calibration arithmetic of Section sec:sharp: the bound-zero proportion `53.2%` alone predicts at least `461,000` violations
    among `867,578` bounded curves; explain what further information gives `605,000`, and why the figure measures strength, not validity.
18. 99A1: check `N = 9 * 11` and type `III` at `3`; explain why `deg = 4`, `r = 12` does not contradict ARS12, why `H^1(X_0(99), Z_3)_m` is not free,
    and why Conjecture conj:euler at `l = 3` is not violated (`w_3 = 0`).

## 7. Notes for the writer

W1. Changes made in the third session (this revision), by part. Opening and C2: Frobenius convention rewritten per B-C2, B-C3 (F1,
F2; B1, B7, B9, B25): `Frob` always arithmetic, the geometric one written `Frob_p^{-1}` (`Phi_p` in Appendix B), the eigenvalues `alpha, beta`
belong to the arithmetic Frobenius on `V_l E`, and `L_p(V_l E, s) = L_p(E, s + 1)`. C1, C3: notation per B-C1, B-C4, B-C6, B-C10, B-C12 to B-C14
(duals `^vee`, `^*`, `^D`, adjoints `^dagger`, `c(u)`, `c_E`, `J_f`, depletion `f^Sigma`). A1.0 new (abstract and introduction: points 24, 25, 30,
65, 66, 70, 71, B10). A1.1: point 15 in corrected form (121d2), point 53. A1.3: points 37, 64. A1.4: equality (points 39, 56, 73), the
reading of the hypothesis (point 47). A1.5: points 6, 67, B13. A1.6: point 51. A1.8: no exception (point 43, B13). A1.10: case (a) at
`q = 2` (B18). A1.11: `q` odd (point 60), equality (point 74), point 24 revised. A1.12: points 33, 48 added. A1.13: points 17, 44, 3. A2.2:
`chi_3^cyc` (X5). A2.3: points 22, 49. A2.4: points 28, 29, 45, 51. A2.5: corner `eps kappa`, points 11, 12, 34, 69. A2.6 rewritten (points 50,
69, 43; B16). A2.7: corner `eps kappa` (point 42, T1, B7), step (7) with `eps` and the softened Commentary (point 7 addendum, B21), `c(u)` (T2,
points 23, 31). A3.1: `r(99A1)` recomputed (B19), points 58, 62. A3.2: lem:crit proved in Chapter 15 (B17), adjoints `^dagger`, the
self-correcting sentence replaced (D5, B12). A3.5: points 20, 54, case (c) argument repaired (B18), case (a) at `q = 2`. A3.6: Sturm (point
46), curve-level twists (B8, B20), PARI outputs. A3.7: point 55, data recomputed. A4.1: `M_{f,lambda} = T_l E(-1)` (points 26, 40; D6, B3),
point 73 items 1 and 3. A4.3: point 19 as corrected, point 38. A4.4: equality; kernel not annihilator (point 35, B3); point 36. A4.5: role
reduced to none; point 41. A4.6: dual of `T_l E` (B3), point 47. A4.7: covers `l = 3` (Q1, point 73). A4.8: point 63. A4.9: `iota` versus
`iota_S` (L6), points 11, 75, B22 wording. A4.10: verified (57). A4.12: equality, explicit Tamagawa terms (point 64), point 18. A4.13:
points 23, 65. A4.14: `iota_S`, point 16 with data. A4.15: points 24, 39, 59, 60, 61. A4.16: equality (point 74, B26). A5.1: point 33. A5.2:
points 48, 67. A6.1: test-status table, point 77 (B27), `degphi` (B27), point 25. A6.2: point 80. A6.3: point 79. A6.4: points 23, 68.
A6.6: points 43, 47. A6.7: points 48, 80. A6.8: points 50, 53, 69. A6.9: point 77. A6.10: point 76 (B27), points 17, 44. A7.1: point 57.
A8.1: point 64 (Open question 3 half answered). A9.1: verified outputs, points 78, 80. A9.2: point 52. B1, B2 rebuilt (B19; points 39,
47, 74). B3: DFG04 statuses "verified" with the arXiv warning (B26; point 73). B4: PARI-verified data. Part C: points 1 to 80. Section 4:
plan adjusted. Section 9: the first version's N1 to N14 are important_notes.md points 15 to 28.
W2. Chapter numbers are written `\Cref{ch:slug}`: 1 `ch:groups`, 2 `ch:rings`, 3 `ch:modules`, 4 `ch:reps`, 5 `ch:galois`, 6 `ch:ant`, 7
`ch:local`, 8 `ch:curves`, 9 `ch:ellcurves`, 10 `ch:reduction`, 11 `ch:galrep`, 12 `ch:modforms`, 13 `ch:hecke`, 14 `ch:moddeg`, 15
`ch:modgalrep`, 16 `ch:cohomology`, 17 `ch:galcoh`, 18 `ch:blochkato`, 19 `ch:lfunctions`, 20 `ch:congruence`, 22 `ch:computation`. The
item numbers cited in this outline ("`\Cref{ch:moddeg}` 9.3") are those of the outlines as of 14 October 2026; in the LaTeX they become
`\Cref{ch:moddeg}` only (PLAN.md 7.1) until the cross-reference pass of PLAN.md 8.4 upgrades them to theorem labels. Environments:
`theorem`, `lemma`, `proposition` for the paper's results with the paper's names in the optional argument (`\begin{lemma}[the paper's
Lemma lem:tamfactor]`); labels with the prefix `paper` (`lem:paper:tamfactor`, `thm:paper:main`). Commentaries are `warning` environments
titled "Commentary"; `paperlink` is not needed here. The paper's labels are quoted as text, never `\ref`'d.
W3. Restating versus re-proving. Where another chapter proves a paper result in full (Chapter 10: lem:twist (i), (ii); Chapter 11:
lem:tamagawa-exp, lem:IV and its extension to `q = 2`, rem:types, prop:ns, lem:h0; Chapter 14: lem:hecke in the strengthened form (9.3,
9.5); Chapter 15: lem:crit (decision B17), lem:old, thm:qual; Chapter 18: lem:tamfactor, lem:fpr, the additive Tamagawa factors; Chapter
19: lem:euler; Chapter 20: lem:ddt417, thm:main, thm:twist, thm:quant and its equality), this chapter still walks through the paper's
proof line by line (PLAN.md requires it) but shortens routine verifications by citing the chapter; it must not contradict those
chapters. Where those outlines are older than the settlements (`\Cref{ch:moddeg}` 9.5(c), 10.4(b), 9.6 and `\Cref{ch:modgalrep}` 10.4 still
say the equality in Theorem thm:quant needs multiplicity one, or that the DFG04 normalisation is unchecked), this chapter follows
points 73 and 74 and `\Cref{ch:congruence}` 12.6, Part 7 (important_notes.md B26).
W4. Frobenius. State C2 once; in every proof say which Frobenius is meant. Never write `rho(Frob) = (eps q, c'; 0, eps)` and `L_q = det(1 -
Frob_q^{-1} q^{-s})` in the same paragraph without the adjectives. Never write `Phi_q` for a Frobenius in this chapter (it would clash with
`Phig_q`).
W5. Data. The paper's tables are not in the repository: describe them from their captions and the numbers in the text only, and
attribute every number to the paper. The book's own small-range numbers come from `\Cref{ch:computation}` (Section 11, Part 7),
`\Cref{ch:blochkato}` 13.1, `\Cref{ch:galrep}` 8.4 and are always labelled as such, with the range.
W6. PARI. Every output printed in this chapter was obtained with PARI/GP 2.17.2 (`\Cref{ch:computation}` R1 to R9); the paper used 2.15.
State the version once. `lfuneuler(S, q)` returns `1/P_q(x)`; `ellinit(E, q)` reduces mod `q` (use `ellinit(E, O(q^k))` for the `q`-adic curve);
`ellmoddegree` returns the degree for the given model; `ellsearch` needs the `elldata` package. Cremona's modular-degree file is
`degphi`; the files contain no per-prime Kodaira symbols.
W7. References. B3 lists every imported statement with its status. The DFG04 numbers are verified against the published version;
cite that version, and add a sentence in the Notes that arXiv:2512.02348 numbers differently. Verify before printing: ARS12 Theorem 2.2,
Kim-Ota Theorem 1.1 and Definition 2.12 (and whether their `eta_f(N)` is the Hecke congruence ideal), Ribet-Stein Theorem 3.5, FPR94
I.4.2.2, Edixhoven92 Section 2, Atkin-Li Theorem 3.1, Atkin-Lehner Theorem 3, DDT 3.1(e), 3.15, 4.17, CalegariEmerton09 (point 57),
Sutherland16 (point 3). Bibliography keys follow decision B14 (a key needed by more than one chapter goes in `refs.bib`).
W8. Pitfalls. (a) `chi_{q*}`, never `chi_q`, for the quadratic character of conductor `q` (D3); numerical subscripts are quadratic characters `chi_d` (`chi_{-7}(2) = +1`, `chi_{-11}(2)
= -1`); the cyclotomic character at `3` is `chi_3^cyc` (B-C6). (b) `t_l` at `q = 2` uses `-v_2(j)`, not the index of the symbol `I_n^*`. (c) Theorem
thm:qual needs `l` not dividing `N`; 980i1 is outside it at `l = 5`. (d) In Theorem thm:quant the book allows every odd `q in S`; say that the
paper has `q >= 5`. (e) Lemma lem:twist(ii)'s conductor statement at `q = 3` holds for the listed exchanges only. (f) Do not call `N_s(F_3)`
maximal. (g) "Optimal" is Cremona's curve number `1` except 990h (990h3) below `10,000`, and is known for every class only up to `400000`.
(h) The twist map is `iota_S`; `iota` is `H^1(T) -> H^1(V)`. (i) `f tensor chi` (naive twist) versus `f^chi` (newform twist). (j) Never
identify the class 980g (the twist of 20a) with 980i.
W9. Style. Short sentences; each section opens with a paragraph saying which part of the paper it covers. No dashes (write
"Diamond-Flach-Guo" with a plain hyphen, ranges "1 to 4"). ASCII only in the source.
W10. Length control. If the chapter runs long, shorten 21.15 to 21.17 (data) first, then the restatements of statements proved in
Chapters 11, 14, 15, 18 to 20; never shorten 21.11, 21.13, 21.20 or 21.22.

## 8. Dependencies and verification log

### 8.1 Dependencies on Chapters 1 to 20 and 22 (by label; item numbers as cited in Part A)

* `ch:groups`: 5.7 (Borel commutator), 6.2, 6.3, 6.5 to 6.8, 6.10 (subgroups of `GL_2(F_3)`, orbits on lines, labels) (A5.1, A1.12, A1.13).
* `ch:rings`: 9.5, 9.6, 10.5 (Kronecker symbols, `q*`, the paper's characters), 11.4, 11.5 (the `I_0^*` identity, local terms) (A1.1, A1.2, A2.5).
* `ch:modules`: 5.5, 5.8, 7.6, 9.2 to 9.6, 10.3, 11.1, 11.3 to 11.6 (saturation, Fitting ideals, Gram determinants, alternating forms, idempotents,
  congruence ideals, Gorenstein) (A2.7, A4.1, A4.3, A4.4, A4.5).
* `ch:reps`: 1.4, 2.5, 3.7, 5.2, 6.2, 6.6, 7.3, 7.6, 7.7, 8.2, 10.5 (absolute irreducibility, Brauer-Nesbitt, Clifford, induction, adjoint, trace
  form) (A3.3, A4.11, A5.1, C3).
* `ch:galois`: galois:quartic-on-lines, galois:index-two-restriction, galois:chebotarev-brauer-nesbitt, galois:sqrt-lstar,
  galois:kummer-finite-field (A3.3, A5.1, A2.7).
* `ch:ant`: 3.7 (Frobenius convention), 4.7 to 4.9 (`Z_3[zeta_3]`, `Z_l tensor Z[zeta_3]`) (A2.2, A2.5, C2).
* `ch:local`: 4.3, 5.3, 5.4, 6.2, 9.2 to 9.4 (Frobenius convention, tame character and relation, Kummer class on inertia, local shapes) (A2.1,
  A2.5, A2.7, C2).
* `ch:curves`: 10.3, 11.5 (cup product, projection formula) (A4.1, A4.4).
* `ch:ellcurves`: 4.5, 9.6, 9.8 to 9.10, 10.4, 10.6, 10.7 (division polynomial, no cyclic 27-isogeny, prime-to-`l` isogenies, trivial classes,
  twists) (A1.1, A1.13, A4.14, A5.1, A6.9, B2).
* `ch:reduction`: 4.3, 4.5, 5.1, 5.4, 5.5, 6.6, 6.8, 7.4, 7.5, 7.7, 8.1 to 8.5, 9.2 to 9.4 (component groups, Tate's algorithm, codes, Kraus, type `IV`
  at `2`, Tate curves, twists, wild primes) (A1.1, A1.6, A1.8, A2.1 to A2.6, A9.2).
* `ch:galrep`: 1.4, 3.2, 3.3, 4.3 to 4.6, 6.1, 6.2, 7.4, 8.1 to 8.6, 9.1 to 9.3 (A1.4, A1.8, A1.12, A2.2, A2.3, A4.6, A4.11, A5.1, A5.2).
* `ch:modforms`: 11.3, 11.5 (Sturm, the paper's congruences for all `n`) (A3.6).
* `ch:hecke`: 4.1, 5.2 to 5.4, 6.3, 7.1 to 7.4, 8.1 to 8.3, 9.1 to 9.3, 11.1 to 11.3 (perfect pairing, adjoints, strong multiplicity one, old
  spaces, depletion, twists, congruence numbers) (A3.1 to A3.5, A4.14, A4.15).
* `ch:moddeg`: 3.3, 3.4, 6.4, 8.1 to 8.5, 9.1 to 9.7, 10.1 to 10.4, 11, 12.3, 12.4 (A3.1, A4.1, A4.4, A4.5, A6.10, A7.1).
* `ch:modgalrep`: 2.7, 3.8, 4.2, 6.2, 6.4 to 6.6, 7.2 to 7.4, 8.2, 8.3, 9.1 to 9.5, 10.1, 10.2, 11.1 to 11.4 (A1.9, A1.10, A3.2 to A3.7).
* `ch:cohomology`: inflation-restriction, conjugation-action, cohomology-through-pro-l-quotient, procyclic-compact, model-computation,
  frobenius-on-h1-inertia, lengths-in-exact-sequences (A2.7, A4.10).
* `ch:galcoh`: 5.1 to 5.5, 6.4, 10.3, 10.4 (A2.7, A4.8, A4.9).
* `ch:blochkato`: 3.3, 6.1, 6.3, 6.6, 7.1 to 7.6, 8.1 to 8.5, 9.1 to 9.5, 10.1 to 10.5, 11.1, 11.3, 12.1 to 12.3, 13.1, 13.2, 14.5 (A1.3, A2.7, A4.6 to
  A4.12, A5.2, A6.4, A8.1).
* `ch:lfunctions`: 7.4, 8.2 to 8.4, 9.1, 9.3, 9.5 to 9.7, 10.1, 10.2, 11.1, 12.1 (A1.0 to A1.2, A2.5, A2.6, A6.8).
* `ch:congruence`: 3.4, 4.3, 5.2 to 5.7, 6.2, 7.1 to 7.5, 8.5, 9.1 to 9.4, 10.1, 10.2, 11.2, 11.3, 12.1 to 12.7, 13.1 to 13.3, Part 7 (A1.4, A1.11,
  A4.1 to A4.16, A5.2, A8.1, B2, B3).
* `ch:computation` (comes after this chapter; forward references by `\Cref{ch:computation}` only): 3.5, 4.1, 4.3, 5.1 to 5.4, 6.1 to 6.8,
  9.1, 9.2, 10.1 to 10.6, 11.1 to 11.8, 12.1, R0 to R9 (A6, A9, B4). Chapter 21 explains what each statement means and tests; Chapter 22
  explains how to run it.

### 8.2 Verification log

First sessions (kept): Python 3 with sympy and Cremona's `ecdata` files for `N < 10,000` (`allcurves`, `degphi`, `galrep`): Weierstrass
invariants and Kodaira types of the example curves; `a_p` by point counting for `p < 1000`; the congruences of the paper's example; the
`2 + 2` factorisation of `psi_3` exactly for the `90` non-CM optimal 3Ns curves; label consistency of 3B.1.1, 3Cs.1.1; exhaustive checks of the
Tamagawa formula for `l = 3, 5`.
This revision: no new computation was run; every number added was taken from the PARI-verified records cited at its item
(important_notes.md and the outlines of Chapters 10, 11, 13, 14, 15, 18, 19, 20, 22), and the arithmetic of each quoted example was rechecked
by hand (`v_3(2880) = 2`, `v_3(1728) = 3`, `v_3(3240) = 4`, `v_3(9/8) = 2`, `v_5(5/8) = 1`, `1584 = 11 * 144`, `504/72 = 7`, the line counts of Section 4).
Not verified here: the paper's large-range counts; the theorem numbers marked "as cited" in B3; the definitions of Sutherland's labels
against Sutherland16; the exact statement of CalegariEmerton09.

## 9. Points for important_notes.md

The first version's points N1 to N14 are important_notes.md points 15 to 28 (N1 = 15, ..., N14 = 28) and are no longer listed here. This
revision found no new point about the paper. Book-internal items found while revising (for the orchestrator):

R1. Appendix B: B-C2(b) says that in Chapter 21 the geometric Frobenius at a named prime is written `Frob_q^{-1}`, never `Phi_q`, while the
Part 3 entry F1 for Chapter 21 says "write `Phi_p`" in the opening paragraph. This outline follows B-C2(b) (`Frob_p^{-1}`) and names `Phi_p` once
as Appendix B's symbol for the same element; Appendix B Part 3, F1, should be reworded accordingly.
R2. `\Cref{ch:moddeg}` 9.5(c), 9.6, 10.4(b) and `\Cref{ch:modgalrep}` 10.4 still carry the pre-settlement claims (multiplicity one needed for the
equality in Theorem thm:quant; the DFG04 normalisation "to be checked"); `\Cref{ch:blochkato}` 9.4, 11.2, 11.3 say "subject to the DFG04
checklist". All are superseded by points 73 and 74 (already recorded as B26); listed here so the Chapter 14, 15, 18 writers apply them.
R3. Item numbers of the other outlines are cited throughout Part A; any renumbering of those outlines must be propagated here.
