# Memo on "Local factors of the adjoint L-function and the l-adic valuations of the modular degree"

To: D. Soni (author)
Re: `note_Oct10_7pm.tex`, points collected while outlining a textbook on the paper
Date: 14 October 2026

Labels below are the LaTeX labels of the source (`thm:main`, `lem:tamfactor`, ...). "Checked twice" means the argument was checked independently by two readers. "Re-verified" means recomputed for this memo with PARI/GP 2.17 (cypari2) against Cremona's `ecdata` files for conductor below 10,000. Every curve-level example quoted here was re-verified; the log is at the end.

## Summary

The most important items:

1. **(A1)** For the optimal curve, the congruence ideal $\eta^\emptyset_{f,\lambda}$ of DFG04 is exactly $\deg\varphi_E\,\mathbb{Z}_\ell$, by the projection formula. So (eq:identity) is an **equality** whenever $\ell\notin S_f$, with no multiplicity-one hypothesis. The normalisation has been checked against the published DFG04.
2. **(A2)** $\mathrm{Tam}_q(\mathrm{ad}^0T)$ is trivial at every potentially good additive prime. With A1 this makes (eq:identity) fully explicit: $v_\ell(\deg\varphi_E)$ equals the Selmer length plus explicit local terms. This answers the first half of Open question 3.
3. **(A3)** The first inequality of `thm:quant` is an equality whenever $\ell\notin S_f$, again without multiplicity one.
4. **(A4, A5)** For $\ell\ge5$, $\ell\nmid N$ and $E[\ell]$ irreducible, $\ell\notin S_f$ holds automatically. The type IV/IV* at 2 exception in `prop:forms` is a theorem, so `prop:forms` holds with no exception.
5. **(B1, B2, B3)** Three false statements:
   * $e_\ell$ is not twist invariant (`def:terms`).
   * Strict inequality also occurs in case (a), not "only in case (b)", after `thm:twist`.
   * The criterion for $h_\ell>0$ must use $\bar\chi_\ell$, not $\chi_{\ell^*}$.
6. **(B4, B6, B7)** Three factual statements about data or the literature are false as written:
   * "type II at 2 has $P_2=1$" (336f1, 1232l1).
   * Two slips in `sec:eis` (14a1, 714i1, 6942n1).
   * The Calegari-Emerton paraphrase. Their Theorem 1.1 has a CM case (N = 27, 32, 49, 243), and the prime-conductor case needs supersingularity at 2.
7. **(C1, C2)** Two gaps:
   * The finiteness argument in `lem:h0` is wrong. It confuses $\chi_\ell$ with $\chi_{\ell^*}$. A two-line determinant argument gives the stronger $h_\ell=0$ for $\ell\ge5$ and $h_3\le1$.
   * `rem:ns` silently needs $H^1_f(\mathbb{Q},V^D)=0$ for 3Ns curves, which DFG04 does not provide there.
8. **(A6, A7)** Two observations in the paper are actually theorems:
   * The 3Ns structure seen in `sec:anomaly`.
   * The bound $D\le2$ in `conj:eis`.

Counts: **A: 12** strengthenings, **B: 10** errors, **C: 14** gaps, **D: 17** expository fixes, **E: 9** open checks. No curve example failed re-verification. One formula in the source notes was itself wrong and is corrected here (A9).

## A. Strengthenings and new results

**A1. (eq:identity) is an equality for every $\ell\notin S_f$; multiplicity one is not needed**
- *Where:* `thm:main` ("with equality when $H^1(X_0(N),\mathbb{Z}_\ell)$, localised ..., is free"), `lem:hecke`, `rem:free`, abstract ("when multiplicity one holds at level N equals").
- *New statement (paste as a lemma before `lem:hecke`):* Let $E$ be $X_0(N)$-optimal and $\ell$ odd. Then $\varphi_E^*\colon H^1(E,\mathbb{Z}_\ell)\to H^1(X_0(N),\mathbb{Z}_\ell)$ has saturated image $M_{f,\lambda}=H^1(X_0(N),\mathbb{Z}_\ell)[\ker\phi_f]$. Moreover $\langle\varphi^*a,\varphi^*b\rangle_{X_0(N)}=\deg\varphi_E\,\langle a,b\rangle_E$. Hence, for $\ell\nmid 2N$ and $\bar\rho$ irreducible, $v_\lambda(\eta^\emptyset_{f,\lambda})=v_\ell(\deg\varphi_E)$.
- *Proof:*
  1. By optimality the kernel of $J_0(N)\to E$ is connected. So $\varphi_*\colon H_1(X_0(N),\mathbb{Z})\to H_1(E,\mathbb{Z})$ is surjective, and the image of $\varphi^*$ is saturated.
  2. The Hecke algebra acts on that image through $\phi_f$, and the image has rank 2. So the image is the kernel lattice $M_{f,\lambda}$.
  3. The projection formula gives $\varphi_*\varphi^*=\deg\varphi_E$. The cup product on $H^1(E)$ is unimodular.
  4. DFG04's pairing is $\tfrac12\cdot$(cup product)$\circ w_N$ in weight 2, and $w_N$ acts on $M_{f,\lambda}$ by $\pm1$. So its ideal of values is $\deg\varphi_E\,\mathbb{Z}_\ell$. That ideal is DFG04's $\eta$.
- *Consequences:*
  - `lem:hecke` becomes an equality; ARS is used only to identify the result with $v_\ell(r_E)$.
  - In `thm:main`, replace "with equality when ... free over the localised Hecke algebra" by "with equality". The abstract's "bounded below by, and when multiplicity one holds at level N equals" becomes "equals".
  - `rem:free` is no longer needed for `thm:main`.
- *Evidence:* argument checked twice. The DFG04 checklist (integral structure, interior cohomology, the operator $[UwU]\omega=w_N$ with no scalar, the kernel lattice, $\eta$ as ideal of values) was checked against the published Ann. Sci. ENS text. Contrast: the Hecke-side inequality of `lem:ddt417` can be strict. At 99a1 and $\ell=3$ (outside the hypotheses, $3\mid N$), $\deg=4$ and $r=12$, so the localised $H^1$ is not free there. Re-verified.
- *Confidence:* high. One residual point is in E1.

**A2. $\mathrm{Tam}_q(\mathrm{ad}^0T)$ is trivial at potentially good additive primes; (eq:identity) becomes explicit**
- *Where:* `thm:main` proof ("$v_\ell(\mathrm{Tam}_p(\mathrm{ad}T))\ge0$ at an additive prime"), Open question 3.
- *New lemma:* Let $q\ne\ell$, $\ell$ odd, and let $E$ have potentially good additive reduction at $q$. Then $v_\ell(\mathrm{Tam}_q(\mathrm{ad}^0T))=0$.
- *Proof:*
  1. Inertia acts on $M=\mathrm{ad}^0T$ through a finite quotient $H$, of order dividing 24, with kernel $K$.
  2. Inflation-restriction gives $0\to H^1(H,M)\to H^1(I_q,M)\to\mathrm{Hom}(K,M)^H$. The last group is torsion-free, since $\mathrm{Hom}(K,M)$ factors through the tame pro-$\ell$ quotient $\mathbb{Z}_\ell(1)$.
  3. So the torsion of $H^1(I_q,M)$ lies in $H^1(H,M)$. That group is killed by $\#H$, hence is 0 for $\ell\ge5$.
  4. For $\ell=3$, restrict to a 3-Sylow $C_3=\langle\sigma\rangle$. Here $\sigma$ has determinant 1, so $T$ is free of rank one over $\mathbb{Z}_3[\zeta_3]$ (as in `lem:IV`), and $H^1(C_3,\mathrm{ad}^0T)=0$.
- *Explicit identity (for $\ell\notin S_f$, combining A1, A2 and `lem:tamfactor`):*
  $$v_\ell(\deg\varphi_E)=\mathrm{len}\,H^1_f(\mathbb{Q},\mathrm{ad}^0T\otimes\mathbb{Q}_\ell/\mathbb{Z}_\ell)+\sum_{q\mid N}e_\ell(E,q)+\sum_{q:\,v_q(j)<0}\Bigl(t_\ell(E,q)+\min\bigl(t_\ell(E,q),v_\ell(q-1),v_\ell(c(u_q))\bigr)\Bigr).$$
  Here $u_q$ is the unit part of the Tate parameter determined by $j_E$. At a prime of type $\mathrm{I}_n^*$ (including $q=2$), apply `lem:tamfactor` to the local quadratic twist that is multiplicative; $\mathrm{ad}^0T$ is unchanged (see C3).
  Open question 3 then reduces to the Selmer group alone.
- *Evidence:*
  - $\ell\ge5$: checked twice.
  - $\ell=3$: the agent gave an explicit basis. For this memo, $H^1(C_3,\mathrm{ad}^0T)=0$ was recomputed in PARI (Smith form of the coboundaries inside the norm kernel is $[1,1]$).
  - Data below 10,000 at $\ell=3$: the excess over the explicit bound is never negative, and is 0 for 8,688 of 13,203 curves (as reported).
- *Confidence:* high.

**A3. `thm:quant`: the first inequality is an equality when $\ell\notin S_f$**
- *Where:* `thm:quant`; Remark (2) after its proof ("is an equality when $H^1(X_0(N),\mathbb{Z}_\ell)_\mathfrak{m}$ is free, that is, under multiplicity one at level N"); Step 4.
- *New statement:* If in addition $\ell\notin S_f$, then $v_\ell(\deg\varphi_E)=v_\ell(\deg\varphi_{E_S})+\sum_{q\in S}e_\ell(E,q)$.
- *Proof:* apply A1 to $E$ and to $E_S$.
  - $\mathrm{ad}^0T$ is unchanged by the twist, so $\ell\notin S_f$ for $E_S$ and the Selmer groups agree.
  - Tamagawa factors at $q\in S$:
    - $\mathrm{I}_0^*$ primes: trivial by A2, and $E_S$ is good there.
    - $\mathrm{I}_n^*$ primes: $E_S$ is multiplicative with the same Tate parameter.
  - At $q\notin S$ the local representations differ by an unramified twist, so the Tamagawa factors and the Euler terms are the same.
  - The only remaining difference is $\sum_{q\in S}e_\ell(E,q)$.
- *Further simplifications:*
  - Step 4 of the proof needs no freeness: apply A1 to the optimal curve in the class of $g$.
  - Step 1 is in fact an equality, $v_\ell(r_E)=v_\ell(\eta^{\mathrm{Hecke}}(g^S))$, because $\iota$ maps each complement into the other (as reported; see E5).
- *Evidence:* argument checked twice.
  - Re-verified ($\ell=3$, all with $E[3]$ surjective and $3\nmid N$):

    | pair | $v_3$ of degrees | difference | $e_3$ |
    |-|-|-|-|
    | 539c1 / 77c1 | 2 / 1 | 1 | $e_3(7)=1$ |
    | 980i1 / 140b1 | 2 / 1 | 1 | $e_3(7)=1$ |
    | 121d1 / 11a1 | 1 / 0 | 1 | $e_3(11)=1$ |
    | 539d1 / 11a1 | 2 / 0 | 2 | $e_3(7)=2$ ($\mathrm{I}_0^*$) |

  - As reported: equality in all 25,477 (curve, $\ell$) pairs below 10,000, and in all 14,876 pairs of case (c) of `thm:twist`.
- *Confidence:* high (Step 1 equality: medium, E5).

**A4. $\ell\notin S_f$ is automatic for $\ell\ge5$, $\ell\nmid N$, $E[\ell]$ irreducible**
- *Where:* hypothesis of `thm:main` and the abstract; `sec:forms` ("curves whose mod $\ell$ representation is induced from $\mathbb{Q}(\sqrt{\ell^*})$ with $\ell\ge5$, which we did not single out").
- *Statement:* For $\ell\nmid 2N$, $\ell\notin S_f$ is equivalent to: $E[\ell]$ irreducible, and, if $\ell=3$, the mod 3 image is not $N_s(\mathbb{F}_3)$ (equivalently $h_\ell(E)=0$).
- *Proof:* suppose $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ and restrict to $I_\ell$, where $\chi_{\ell^*}=\omega^{(\ell-1)/2}$ and the reduction is good.
  - Ordinary case: $\{\omega,1\}=\{\omega^{(\ell+1)/2},\omega^{(\ell-1)/2}\}$ forces $(\ell-1)\mid(\ell+1)/2$, so $\ell\le3$.
  - Supersingular case: $\{\omega_2,\omega_2^\ell\}$ twisted by $\omega_2^{(\ell^2-1)/2}$ never returns to itself.
  - For $\ell=3$ use `prop:ns`. Irreducible implies absolutely irreducible, because complex conjugation has distinct eigenvalues $\pm1$.
- *Consequence:* the clause in `sec:forms` concerns only curves with $\ell\mid N$. Say so, or delete it.
- *Evidence:* checked twice. Probably known; no citation found.
- *Confidence:* high.

**A5. The type IV / IV* at 2 exception in `prop:forms` is a theorem; case (a) of `thm:qual` holds at $q=2$**
- *Where:* `prop:forms` ("except possibly when $\ell=3$ and E has type IV or IV* at 2 ... holds for all 92,812 curves"); `thm:qual`(a) ("$q\ge5$").
- *New argument:*
  1. For additive reduction at $q\ne\ell$, the formal group and $\mathbb{G}_a$ have no $\ell$-torsion, and $E_0(\mathbb{Q}_q^{ur})$ is $\ell$-divisible. So $E[\ell^k]^{I_q}\simeq\Phi^{geom}_q[\ell^k]$.
  2. For types IV, IV* this is $\mathbb{Z}/3$, so inertia fixes a line of $E[3]$. Its determinant is trivial on inertia, so the image is unipotent of order 3.
  3. Reduction is injective on finite subgroups of $GL_2(\mathbb{Z}_3)$. So the image of $I_2$ on $T_3E$ is cyclic of order 3: tame, and the same for every $\ell\ne2$.
  4. The computation of `lem:euler` then gives Frobenius eigenvalue $\chi_{-3}(2)=-1$ on $(\mathrm{ad}V)^{I_2}$. Hence $P_2(X)=1+2X$ and $e_3(E,2)=1$.
- *Fix:* In `prop:forms`, delete "except possibly ... $e_3(E,2)\ge1$" and the last sentence, and cite the argument. In `thm:qual`(a) write "$q\ge5$ or $q=2$". The Serre conductor exponent of $\bar\rho_{E,3}$ at 2 is 1, and the proof of case (a) is unchanged.
- *Evidence:*
  - Checked twice. A second proof uses the conductor exponent 2 at 2 (Dokchitser-Dokchitser 2015, Thm 3.1).
  - Re-verified: all 3,194 optimal non-CM curves below 10,000 with type IV or IV* at 2 have $P_2=1+2X$.
  - Worked example, re-verified: 52a1 (type IV* at 2, $\deg=3$) satisfies $f_{52a}\equiv f_{26b}-f_{26b}(2z)\pmod 3$ for all $n$. This was checked to $n=200$; the Sturm bound is 14, and $a_2(26b1)=1$.
- *Confidence:* high.

**A6. The 3Ns observations of `sec:anomaly` are theorems**
- *Where:* `sec:anomaly` ("Conversely every $\mathrm{3Ns}$ curve of the tables has a prime of type III or III* with a positive term $e_3$").
- *New proposition:* Let $E[3]$ be irreducible with image $N_s(\mathbb{F}_3)$.
  - (i) Every prime $p\ne3$ with $v_p(j)<0$ has $3\mid v_p(j)$, so $t_3(E,p)\ge1$.
  - (ii) If $3\nmid N$, there is a prime $p\ne3$ at which inertia acts on $T_3E$ through a cyclic group of order 4. For any such $p$, $e_3(E,p)=v_3(p-\chi_{-3}(p))\ge1$. If $p\ge5$, it has type III or III* and $p\equiv\pm1\pmod{12}$.
- *Proof:*
  - (i): Potentially multiplicative inertia acts through $\pm1$ times a unipotent. A unipotent of order 3 does not lie in $N_s(\mathbb{F}_3)$, which has order 8.
  - (ii), existence: The determinant-one image is $C_4=\langle\tau\rangle$, cut out over $\mathbb{Q}(\sqrt{-3})$ by an order-4 character $\psi$ (over $\mathbb{F}_9$). If all inertia images lay in $\{\pm1\}$, then $\psi^2$ would be unramified; since $h(\mathbb{Q}(\sqrt{-3}))=1$, $\psi$ would have order at most 2. At 3 with good reduction the image of $I_3$ has order at most 2 (ordinary, since $N_s$ has no element of order 8) and dies on $I_{(\sqrt{-3})}$. So some $p\ne3$ has inertia image containing $\tau$.
  - (ii), value of $e_3$: That image is cyclic of order 4 (finite, injecting mod 3 into $C_4$), and $(\mathrm{ad}V)^{I_p}=\langle\tau\rangle$. Frobenius has determinant $p$ mod 3. It centralises $\tau$ if $p\equiv1\pmod3$ and inverts it if $p\equiv2$, since the elements of determinant $-1$ in $N_s$ are reflections. So it acts on the line by $\chi_{-3}(p)$.
  - (ii), tame primes: For $p\ge5$ the relation $\mathrm{Frob}\,\tau\,\mathrm{Frob}^{-1}=\tau^p$ gives $p\equiv\pm1\pmod{12}$, and the type is III or III* (defect 4).
- *Evidence:* my derivation (checked once), consistent with the notes' report. Re-verified on all 90 optimal 3Ns curves below 10,000:
  - (i) holds for every curve.
  - Every curve has such a prime: 74 have one of type III/III* with $p\ge5$ and $p\equiv1$ or $11\pmod{12}$; 16 only at $p=2$, of type III or III* there, with $P_2=1+2X$. This includes the 28 curves with $3\mid N$.
- *Confidence:* high for (i) and for (ii) with $3\nmid N$. The case $3\mid N$ is data only, see E4.

**A7. $D\le2$ in `conj:eis` is provable: the two sources of a deficit 2 cannot coexist**
- *Where:* `conj:eis`; `sec:eis` ("We have not proved that the two cannot coexist, so the bound $D\le2$ is part of the conjecture").
- *Proof (paste):*
  1. Suppose $E[3]\simeq\mathbb{Z}/3\oplus\mu_3$ and $P\in E(\mathbb{Q})$ has order 9. Let $\phi\colon E\to E'=E/\mu_3$, and compose $\hat\phi\colon E'\to E$ with $E\to E/\langle P\rangle$.
  2. The kernel has order 27 and is Galois stable. It contains $E'[3]$ only if $\hat\phi(E'[3])=\ker\phi=\mu_3$ lies in $\langle P\rangle$. But $\langle P\rangle\cap E[3]$ is the rational line $\mathbb{Z}/3\ne\mu_3$.
  3. So $E'$ has a rational cyclic 27-isogeny, which over $\mathbb{Q}$ forces CM.
  4. Hence for non-CM $E$, $D\le2$ is a consequence of the first bound of the conjecture, not an extra conjectural input.
- *Evidence:* checked twice.
- *Confidence:* high.

**A8. The restriction $q\ge5$ in `thm:quant` can be relaxed to $q$ odd**
- *Where:* `thm:quant` ("the set of primes $q\ge5$ at which E has type $\mathrm{I}_0^*$ or $\mathrm{I}_n^*$").
- *Argument:*
  - The proof uses only $V=V'\otimes\chi_q$ and the exchanges $\mathrm{I}_n\leftrightarrow\mathrm{I}_n^*$, $\mathrm{I}_0\leftrightarrow\mathrm{I}_0^*$, which hold for every odd $q$.
  - At $q=3$, Tate's algorithm for $\mathrm{I}_0^*$ (with 2 invertible) gives the twisted model of good reduction directly, so type $\mathrm{I}_0^*$ at 3 is tame.
  - The hypothesis $\ell\nmid2N$ excludes $\ell=3$ when $3\in S$.
- *Fix:* replace "$q\ge5$" by "$q$ odd", and in `lem:euler` note that the $\mathrm{I}_n^*$ and $\mathrm{I}_0^*$ rows hold for every odd $q$.
- *Evidence (as reported):* PARI's $P_3$ agrees with the twist formula on 1,100 curves; the bound held in all 388 cases with $\mathrm{I}_0^*$ at 3; every cubic $P_3$ below 10,000 (2,283) is the $\mathrm{I}_0^*$ formula.
- *Confidence:* high.

**A9. The shape of $P_q$ at every bad prime, including 2 and 3**
- *Where:* `rem:wild`, `sec:wild`.
- *Statement:* at every bad prime $q\ne\ell$, $P_q(X)$ (where $L_q(\mathrm{Sym}^2f,s)=P_q(q^{-s})^{-1}$) is one of four shapes:
  - $1-X$ (multiplicative);
  - $(1-qX)(1-(a^2-2q)X+q^2X^2)$, with $a=a_q$ of a quadratic twist with good reduction at $q$;
  - $1-cqX$ with $c=\pm1$ (inertia cyclic of order 3, 4 or 6 with an invariant line);
  - $1$.
- *Note:* the source notes wrote the cubic as $(1-X)(\dots)$; PARI shows the linear factor is $1-qX$.
- *Examples (re-verified):*
  - 1232l1 is 77a1 twisted by $\chi_{-4}$, with $a_2(77a1)=0$. So $P_2=(1-2X)(1+2X)^2=1+2X-4X^2-8X^3$ and $e_3(E,2)=2$.
  - 592c1 is 37a1 twisted by $\chi_{-4}$, with $a_2=-2$. So $P_2=(1-2X)(1+4X^2)$, $e_5(E,2)=1$ and $\deg=80=2^4\cdot5$. The prime 2 can contribute at $\ell=5$.
  - 539d1 at 7 (twist of 11a3, $a_7=-2$): $P_7=1+3X-21X^2-343X^3$, $e_3=2$.
- *Fix:* replace the case-by-case sentences on 2 and 3 in `rem:wild` and `sec:wild` by this classification. Keep "for $\ell=5,7$ no term is needed ... beyond Definition `def:terms`", but add that the term at 2 can be positive (592c1).
- *Evidence:* as reported, all 1,143 cubic factors at 2 and 2,283 at 3 below 10,000 are of the second shape. The examples were re-verified.
- *Confidence:* high.

**A10. An exact degree formula**
- *Where:* new remark after `thm:main` or in the introduction (the Petersson-norm paragraph).
- *Statement:* $\deg\varphi_E=\dfrac{N\,L^{nv}(\mathrm{ad}^0f,1)}{2\pi\,\mathrm{vol}(\Lambda_E)}$, from $\langle f,f\rangle=N\,L^{nv}(\mathrm{Sym}^2f,2)/(8\pi^3)$ (DFG04 Lemma 2.12, naive L-value, confirmed) and $\deg\varphi_E\,\mathrm{vol}(\Lambda_E)=4\pi^2c_E^2\langle f,f\rangle$ with $c_E=1$.
  - Let $B_E$ be the same expression with the true L-value. Then $v_\ell(\deg\varphi_E)=v_\ell(B_E)+\sum_qe_\ell(E,q)$ unconditionally.
  - So (eq:thm) is equivalent to $v_\ell(B_E)\ge\sum_qt_\ell(E,q)$.
- *Evidence:* re-verified to 30 digits for 11a1, 121a1, 539d1, 1232l1 and 726a1 (values 1, 6, 72, 288, 144). Reported exact on 19 curves.
- *Confidence:* high.

**A11. Sturm turns the Example's congruence checks into proofs**
- *Where:* the Example after the proof of `thm:qual` ("checked for $p<500$", "for $p<1000$").
- *Fix:* both forms of each pair lie in the same $S_2(\Gamma_0(N))$. So "for all $n$, by Sturm's bound (22, 112, 336 for $N=121, 539, 980$)", including the excluded primes.
- *Evidence:* re-verified for all $n\le400$ (121, 539) and $n\le1000$ (980), and `mfsturm` returns 22, 112, 336:
  - 121a1 against 121d1 (the class of $f_{11a}\otimes\chi_{-11}$), mod 3;
  - 539c1 against $f_{11a}\otimes\chi_{-7}$ (class 539d), mod 3;
  - 980i1 against $f_{20a}\otimes\chi_{-7}$ (class 980g), mod 5.
- *Confidence:* high.

**A12. Small optional additions**
- *Optimality at $\ell$:* if $E[\ell]$ is irreducible, all isogenies in the class have degree prime to $\ell$, so $v_\ell$ of the degree of the parametrisation does not depend on which curve is used. One sentence in Section 1. High.
- *More examples where $r_E\ne\deg\varphi_E$ (next to 99A1 in the Remark after the Example):*
  - 726a1: $r=1584$, $\deg=144$, gap 11, with $11^2\mid726$;
  - 539d1: $r=504$, $\deg=72$, gap 7, with $7^2\mid539$.

  Re-verified by computing the congruence module in PARI; 99a1 gives $r=12$, $\deg=4$. High.
- *Type exchanges at $q=3$:* $\mathrm{II}\leftrightarrow\mathrm{IV}^*$, $\mathrm{III}\leftrightarrow\mathrm{III}^*$, $\mathrm{IV}\leftrightarrow\mathrm{II}^*$ under the twist by $\mathbb{Q}(\sqrt{-3})$ also hold at $q=3$, with the conductor exponent unchanged. Data: 5,122 pairs below 10,000, as reported. One step needs a reference. Medium (E6).

## B. Errors: statements false as written

**B1. $e_\ell$ is not invariant under quadratic twist**
- *Where:* `def:terms`, last sentence: "Both terms are invariant under quadratic twist."
- *Problem:* true for $t_\ell$, false for $e_\ell$ when the twist is ramified at $q$ and changes the type. For example, 11a1 has type $\mathrm{I}_5$ at 11 and $e_3=0$, while its twist by $\chi_{-11}$ (121d2) has type $\mathrm{I}_5^*$ and $e_3=v_3(120)=1$. The true adjoint factor is twist invariant; the naive one is not.
- *Fix:* "The term $t_\ell$ is invariant under quadratic twist, and $e_\ell(E,q)$ under twists unramified at $q$."
- *Evidence:* checked twice; the curves were re-verified.
- *Confidence:* high.

**B2. Strict inequality is not "only in case (b)"**
- *Where:* paragraph after `thm:twist` ("with equality in every pair of case (c) and strict inequality only in case (b), where the difference is the Euler term of Theorem `thm:quant`").
- *Problem:* `thm:quant` predicts a gap $e_\ell(E,q)=v_\ell(q^2-1)$ in case (a) too. At $\ell=3$ that gap is at least 1 for every $q\ne3$. Counterexamples, re-verified ($v_3$ of the degrees): 539c1 against 77c1, 2 against 1; 980i1 against 140b1, 2 against 1; 121d1 against 11a1, 1 against 0.
- *Fix:* rerun the count and write "with equality in every pair of case (c), and, in cases (a) and (b), difference exactly the Euler term of Theorem `thm:quant`". A3 makes the last part a theorem when $\ell\notin S_f$.
- *Confidence:* high.

**B3. The criterion for $h_\ell(E)>0$ uses the wrong character**
- *Where:* Section 1.3 "Beyond the hypotheses": "positive exactly when $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$". The opening sentence: "a correction term when the representation is induced from $\mathbb{Q}(\sqrt{\ell^*})$".
- *Problem:* `lem:h0` uses $\bar\chi_\ell$, which equals $\chi_{\ell^*}$ only for $\ell=3$. For $\ell\ge5$ one always has $h_\ell=0$, while $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ can occur (only when $\ell\mid N$, by A4).
- *Fix:* "is positive exactly when $\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$, which forces $\ell=3$, where $\bar\chi_3=\chi_{-3}$". Also "a correction term when $\ell=3$ and the representation is induced from $\mathbb{Q}(\sqrt{-3})$".
- *Confidence:* high (checked twice).

**B4. "A type II at 2 has $P_2=1$" and the companion claims at 2 are false**
- *Where:* `rem:wild` ("a type II at 2 has $P_2=1$ and $e_3=0$, and a type $\mathrm{I}_n^*$ at 2 has potentially good reduction in about half of the cases, with a cubic $P_2$"); `sec:wild` ("a type II at 2 has $P_2=1$ and $e_3=0$").
- *Counterexamples (re-verified):*
  - 336f1: type II at 2, $P_2=1+2X$, $e_3=1$, $\deg=24$.
  - 1232l1: type II* at 2, $P_2=1+2X-4X^2-8X^3$, $e_3=2$, $\deg=288$. Here the bound of `thm:main` at $\ell=3$ is attained by the prime 2 alone.
- *Counts* (re-verified, optimal non-CM curves below 10,000):

  | type at 2 | $P_2=1$ | $P_2=1+2X$ | cubic $P_2$ |
  |-|-|-|-|
  | II | 1,092 | 371 | 74 |
  | II* | 514 | 74 | 191 |
  | potentially good $\mathrm{I}_n^*$ ($n\ge1$) | 2,043 | 22 | 269 |

  For $\mathrm{I}_n^*$ at 2 there are 2,334 potentially good curves against 1,697 potentially multiplicative, so 58% are potentially good.
- *Fix:* "At 2 the Kodaira type does not determine $P_2$: for instance 336f1 (type II) has $P_2=1+2X$, and 1232l1 (type II*) has a cubic $P_2$ and $e_3=2$." For $\mathrm{I}_n^*$ write "potentially good in a little over half of the cases, usually with $P_2=1$". Rules, tables and counts use PARI's factor and do not change.
- *Confidence:* high.

**B5. Frobenius conventions are mixed**
- *Where:* Section 1.1 ($L_p(A_f,s)=\det(1-\mathrm{Frob}_pp^{-s}\mid A_f^{I_p})^{-1}$), proof of `lem:euler` ("a line with eigenvalue $q^{-1}$"), proof of `lem:tamfactor` ($\rho(\mathrm{Frob})=\begin{psmallmatrix}\varepsilon q&c'\\0&\varepsilon\end{psmallmatrix}$).
- *Problem:* the table, `lem:euler`, PARI's factors, $L_p(A_f,1)=L_p(A_f(1),0)$ in `lem:fpr`, and DFG04 all use the geometric Frobenius. `lem:tamfactor` uses the arithmetic one. Both computations are right in their own convention.
- *Fix:* say "geometric Frobenius" in Section 1.1 and in the proof of `lem:euler`, and "arithmetic Frobenius" in the proof of `lem:tamfactor`. No number changes.
- *Confidence:* high (checked twice; DFG04's convention confirmed).

**B6. Three slips in `sec:eis`**
- *Where:* `sec:eis`.
- *Problems (re-verified):*
  - "seventeen curves, all of rank 0 and torsion $\mathbb{Z}/3$" is false: 14a1 has image 3Cs.1.1, torsion $\mathbb{Z}/6$, types $\mathrm{I}_6$ at 2 and $\mathrm{I}_3$ at 7, and $\deg=1$, so $D=2$.
  - "With a rational point of order 3 and mod 3 image of Borel type, $D\le1$" is false:
    - 714i1: torsion $\mathbb{Z}/9$, 3B.1.1, $\deg=1080=2^3 3^3 5$, $D=5-3=2$;
    - 6942n1: torsion $\mathbb{Z}/9$, 3B.1.1, $\deg=65664=2^7 3^3 19$, $D=2$.
  - "the split Cartan image `3Cs.1.1`": 3Cs.1.1 is the order-2 subgroup $\{1,\mathrm{diag}(1,-1)\}$ of the split Cartan subgroup; the full split Cartan image is 3Cs.
- *Fix:* "torsion $\mathbb{Z}/3$ or $\mathbb{Z}/6$"; "and of Borel type, without a point of order 9, $D\le1$"; "(the image `3Cs.1.1` ...)", or simply "$E[3]\simeq\mathbb{Z}/3\oplus\mu_3$". `conj:eis` is unaffected.
- *Confidence:* high.

**B7. The paraphrase of Calegari-Emerton is incomplete**
- *Where:* `sec:two` ("the theorem of Calegari and Emerton that a curve of odd modular degree has at most two odd bad primes and a rational 2-torsion point or prime conductor").
- *Problem:* 27a1 ($\deg=1$) and 243b1 ($\deg=9$) have odd degree, torsion $\mathbb{Z}/3$ and non-prime conductor; both have CM ($j=0$), re-verified. The theorem (arXiv math/0503359, Theorem 1.1) reads: if $E$ has odd modular degree then
  1. $N$ has at most two odd prime factors;
  2. $E$ has even analytic rank;
  3. either (a) $E$ has a rational 2-torsion point, or (b) $N$ is prime, $E$ is supersingular at 2 and $E(\mathbb{R})$ is connected, or (c) $E$ has CM and $N\in\{27,32,49,243\}$.
- *Fix:* "at most two odd bad primes, and either a rational 2-torsion point, or prime conductor with supersingular reduction at 2 and $E(\mathbb{R})$ connected, or CM with $N\in\{27,32,49,243\}$" (E3 for the published numbering).
- *Confidence:* high.

**B8. The naive adjoint L-function is not the Euler product of $\sum a_n^2n^{-s}$**
- *Where:* Introduction, paragraph 2: "the Euler product of $\sum a_n(f)^2n^{-s}$".
- *Problem:* exactly, $\sum a_n^2n^{-s}=\zeta^{(N)}(s-1)\,L^{nv}(\mathrm{Sym}^2f,s)/\zeta^{(N)}(2s-2)$. At a good prime the Rankin series has an extra factor $1+p^{1-s}$.
- *Fix:* "the naive one: $L^{nv}(\mathrm{Sym}^2f,s)=\zeta^{(N)}(2s-2)\sum a_{n^2}(f)n^{-s}$ (Shimura), which has the true local factor ...". Alternatively, refer to the local definition of Section 1.1.
- *Evidence:* checked twice, by local computation at good, multiplicative and additive primes.
- *Confidence:* high.

**B9. `rem:types` groups the additive types wrongly**
- *Where:* `rem:types` ("In the last two cases $E[3]^{I_q}=0$ and the Serre conductor ... has exponent 2 ...; these are the types whose twist by $\chi_q$ lowers the conductor exponent").
- *Problem:* at $q\ge5$, $E[3]^{I_q}=0$ and the Serre exponent is 2 for *all* additive types except IV, IV*, including $\mathrm{I}_0^*$, III and III*. Twisting by $\chi_q$ lowers the Serre conductor exponent of $\bar\rho_{E,3}$ for $\mathrm{I}_0^*$, $\mathrm{I}_n^*$, II and II*, but lowers the conductor of $E$ only for $\mathrm{I}_0^*$ and $\mathrm{I}_n^*$. For II and II* the twist has type IV*, IV and the same conductor.
- *Fix:* "For all these types $E[3]^{I_q}=0$ and the Serre conductor of $\bar\rho_{E,3}$ has exponent 2 at $q$. The twist by $\chi_q$ lowers that exponent for $\mathrm{I}_0^*$, $\mathrm{I}_n^*$, $\mathrm{II}$, $\mathrm{II}^*$; it lowers the conductor of $E$ only for $\mathrm{I}_0^*$ and $\mathrm{I}_n^*$."
- *Confidence:* high.

**B10. Abstract: four inaccurate phrases**
- *Tamagawa factors:* "raises the bound by one whenever a Steinberg prime $q\equiv1\pmod\ell$ has a Tate parameter whose unit part is an $\ell$-th power". By `lem:tamfactor` the extra term is $\min(v_\ell(n),v_\ell(q-1),v_\ell(c))$, which needs $\ell\mid n_q$ and can exceed 1. Fix: "with $\ell\mid n_q$ ... by at least one". High.
- *Selmer group:* "the length of the Bloch-Kato Selmer group of $\mathrm{ad}^0V_\ell E$". That group is 0 here (DFG04 Thm 2.7); the length is that of $H^1_f(\mathbb{Q},\mathrm{ad}^0T\otimes\mathbb{Q}_\ell/\mathbb{Z}_\ell)$. High.
- *"by an elementary twisting argument":* the proof of `thm:quant` uses DFG04 Prop. 1.4(c) and `lem:ddt417`. After A1 it needs no multiplicity one, but it is not elementary. Fix: "by a twisting argument and the level-raising formula of Diamond, Flach and Guo". High.
- *Scope and rates:* "for every optimal curve of conductor at most 500000" (optimality is determined up to 400000 and for 359,009 classes beyond), and "in a third of the cases" (the rates are 31%, 23%, 18%). Reword. Medium.

## C. Gaps in proofs

**C1. `lem:h0`: the finiteness argument is wrong; the true bound is $h_\ell\le1$**
- *Where:* `lem:h0` proof ("the finiteness from the fact that $\rho\simeq\rho\otimes\chi_\ell$ would force $a_p=0$ at all primes inert in $\mathbb{Q}(\sqrt{\ell^*})$ ..."); statement ("for E without complex multiplication it is finite"); `sec:anomaly` ("$h_3(E)\le1$ because some prime $p<1223$ ...").
- *Problem:* the argument confuses the cyclotomic $\chi_\ell$ with $\chi_{\ell^*}$. In fact $\rho\simeq\rho\otimes\chi_\ell$ is impossible for every $E$, since it would give $pa_p=a_p$.
- *Fix (paste):*
  1. Absolute irreducibility makes the $\ell$-torsion of $H^0(\mathbb{Q},W^D)$ at most a line, so the group is cyclic.
  2. An element of exact order $\ell^k$ lifts to an isomorphism $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$.
  3. Determinants give $\chi_\ell^2\equiv1\bmod\ell^k$ on $G_\mathbb{Q}$. Since $\chi_\ell(G_\mathbb{Q})=\mathbb{Z}_\ell^\times$, this forces $\ell=3$ and $k=1$.
  4. Hence $h_\ell(E)=0$ for $\ell\ge5$, and $h_3(E)\le1$ with equality iff $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$, for every $E$ with $\bar\rho$ irreducible, CM or not.

  Drop "for E without complex multiplication". In `sec:anomaly` write "$h_3(E)\le1$ by Lemma `lem:h0`"; the numerical check is no longer needed.
- *Side remark:* for $\ell\nmid N$ the CM alternative cannot occur anyway, since CM by $\mathbb{Q}(\sqrt{\ell^*})$ forces $\ell\mid N$. This is medium-high and now moot.
- *Confidence:* high (checked twice).

**C2. `rem:ns` and Section 1.3 assume $H^1_f(\mathbb{Q},V^D)=0$ for 3Ns curves**
- *Where:* `rem:ns` ("still does whenever $H^0(\mathbb{Q},V^D)=H^1_f(\mathbb{Q},V^D)=0$"); Section 1.3 ("the correction is the term that Lemma 2.1 of DFG04 produces").
- *Problem:*
  - $H^0(\mathbb{Q},V^D)=0$ is automatic, because the paragraph after `lem:dfg21` shows $H^0(\mathbb{Q}_p,V^D)=0$ at $p\in\Sigma$. So in the paper's setting only $H^1_f(\mathbb{Q},V^D)=0$ needs DFG04 Thm 2.7.
  - That theorem is proved only for $\ell\notin S_f$, and 3Ns curves are exactly the case $\ell=3\in S_f$.
- *Fix:* state in `rem:ns` and in Section 1.3 that the vanishing of $H^1_f(\mathbb{Q},V^D)$ is assumed for these curves (or cite a proof). Note in `lem:dfg21` or after it that $H^0(\mathbb{Q},V^D)=0$ is automatic.
- *Confidence:* medium-high.

**C3. `thm:main` proof: a prime of type $\mathrm{I}_n^*$ at $q=2$ is not covered**
- *Where:* last sentences of the proof of `thm:main` ("the curve $E_{\{p\}}$ of Lemma `lem:twist` is multiplicative ...").
- *Problem:* `lem:twist` is for odd $q$, but at $q=2$ a potentially multiplicative $\mathrm{I}_n^*$ prime can have $t_\ell(E,2)>0$.
- *Fix (paste):* "At an additive prime $p$ with $v_p(j)<0$ (any $p$, including $p=2$), $E/\mathbb{Q}_p$ is a quadratic twist of the Tate curve $E_{q_E}$ over $\mathbb{Q}_p$. The $G_{\mathbb{Q}_p}$-module $\mathrm{ad}^0T$ is unchanged by the twist, so `lem:tamfactor` applied to $E_{q_E}$ gives $v_\ell(\mathrm{Tam}_p(\mathrm{ad}^0T))\ge t_\ell(E,p)$." This is local, needs no global twist, and also replaces the $E_{\{p\}}$ argument at odd $p$.
- *Confidence:* high.

**C4. `lem:ddt417`: $\wp\cap I=0$ is used without proof**
- *Where:* proof of `lem:ddt417` ("Since L is torsion-free and $\wp\cap I=0$").
- *Problem:* this is not "because $\mathbb{T}$ is reduced". The full Hecke algebra can have nilpotents: $U_2$ at level 88 on the span of $f_{11}(d z)$, $d\mid8$, has a Jordan block at 0.
- *Fix (paste):* "Take $t\in I$ with $\pi(t)$ generating $\eta$. For $x\in\wp\cap I$, $tx=0$ (as $t$ kills $\wp$) and $(\pi(t)-t)x=0$ (as $\pi(t)-t\in\wp$ and $x$ kills $\wp$). So $\pi(t)x=0$, and $x=0$ if $\eta\ne0$, $\mathbb{T}$ being torsion-free. If $\eta=0$ the lemma is trivial."
- *Also:* the lemma counts $\#\mathcal{O}/\Delta$, which is finite only for a finite residue field. State it with lengths, or for $\mathcal{O}=\mathbb{Z}_\ell$.
- *Confidence:* high.

**C5. `lem:hecke`: the other local factors lie in the kernel, not the annihilator; perfectness on the $\mathfrak{m}$-part**
- *Where:* proof of `lem:hecke` ("the other local factors of $\mathbb{T}\otimes\mathbb{Z}_\ell$ are killed by $\phi_f$ and lie in the annihilator"); also Step 2 of `thm:quant`.
- *Fix:*
  - "lie in the kernel $\wp$, and since $\phi_f$ factors through $\mathbb{T}_\mathfrak{m}$ and $\mathrm{Ann}(\wp)$ decomposes along the idempotents, the congruence ideal is computed in $\mathbb{T}_\mathfrak{m}$".
  - Add: "The idempotent $e_\mathfrak{m}$ is self-adjoint for $\hat\delta_!$, so $H^1(X_0(N),\mathbb{Z}_\ell)$ splits orthogonally into its local components and the pairing is perfect on each."
- *Confidence:* high.

**C6. `lem:tamfactor`: the corner must be $\varepsilon\kappa$, not $\kappa$**
- *Where:* proof of `lem:tamfactor`, $\begin{psmallmatrix}\chi_\ell\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$.
- *Problem:* the cocycle condition $c(gh)=\chi_\ell\varepsilon(g)c(h)+c(g)\varepsilon(h)$ holds for $c=\varepsilon\kappa$, not for $c=\kappa$ when $\varepsilon\ne1$. The nonsplit curve is the Tate curve twisted by $\varepsilon$.
- *Fix:* write $\varepsilon\kappa$. Nothing else changes: $\varepsilon$ is trivial on inertia, and $c'$ changes by the sign $\varepsilon(\mathrm{Frob})$.
- *Confidence:* high (checked twice).

**C7. `lem:tamfactor`: what $c'$ is, and its indeterminacy**
- *Where:* proof of `lem:tamfactor` ("$c'$ is the image of $\kappa$ in $H^1(G/I,\mathbb{Z}_\ell(1)^I)$ ... well defined modulo $q-1$"); statement ("the class of $u$ in $\mathbb{F}_q^\times/\dots$").
- *Fix:*
  - Add "via the splitting $H^1(\mathbb{Q}_q,\mathbb{Z}_\ell(1))=\mathbb{Z}_\ell\kappa_q\oplus H^1_{ur}$ given by the uniformiser $q$". The projection of $\kappa$ is the class of $u$.
  - $c'$ is a cocycle value. It equals $\varepsilon(\mathrm{Frob})$ times that class for the Frobenius lift fixing a compatible system of $\ell$-power roots of $q$; in general it is well defined only modulo $\ell^{\min(v_\ell(n),v_\ell(q-1))}$, which does not affect the minimum.
  - In the statement write "the reduction of $u$", and read $v_\ell(0)$ as $v_\ell(q-1)$.
  - The conclusion is unaffected.
- *Evidence:* the identification of $c'$ was checked with PARI on 77c1, 791a1, 1577a1 and 11a1 (as reported).
- *Confidence:* high.

**C8. "irreducible" must be "absolutely irreducible" in three places**
- *Where:*
  - `prop:ns` proof: "they are non-abelian and act faithfully". A Borel subgroup is also non-abelian and faithful.
  - `lem:old`: Brauer-Nesbitt only gives $\bar\rho_h^{ss}\simeq\bar\rho^{ss}$.
  - `lem:h0`: the Clifford-theory step.
- *Fix:*
  - In `prop:ns`: "a subgroup of $GL_2(\overline{\mathbb{F}}_3)$ fixing a line lies in a Borel subgroup, so its commutator subgroup is abelian of exponent 3. The commutator subgroups $\{\pm1\}$ of $Q_8$ and $Q_8$ of $SL_2(\mathbb{F}_3)$ are not."
  - In `lem:old` and `lem:h0`, add after "irreducible": "(hence absolutely irreducible, complex conjugation having distinct eigenvalues $\pm1$)". Also add "over a common finite extension of $\mathbb{F}_\ell$" after $\bar\rho_h\simeq\bar\rho$.
- *Confidence:* high.

**C9. $\bar\rho\simeq\mathrm{Ind}\,\psi$ holds only over $\mathbb{F}_9$**
- *Where:* `prop:ns` proof and `lem:h0` ("induced from $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}(\sqrt{-3}))$").
- *Problem:* $\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ has irreducible characteristic polynomial $X^2+1$ over $\mathbb{F}_3$, so $\psi$ takes values in $\mathbb{F}_9$.
- *Fix:* write $\bar\rho\otimes\mathbb{F}_9\simeq\mathrm{Ind}\,\psi$. The isomorphism $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ then descends to $\mathbb{F}_3$, since Hom spaces commute with field extension.
- *Confidence:* high (checked twice).

**C10. `thm:qual`, cases (b) and (c): two twists are depletions, not newforms**
- *Where:*
  - Case (b): "otherwise $g=h\otimes\chi=f\otimes\chi=f'$".
  - Case (c): "$f'=f\otimes\chi$ is a newform of weight 2 on $\Gamma_0(N/q)$", and "$g=h\otimes\chi$ would otherwise equal $f'$".
- *Problem:* $h\otimes\chi$ is the $q$-depletion of $g$, since $a_q(h)=0$. In (c), $f\otimes\chi$ has $a_q=0$, but $f_{E'}$ is multiplicative at $q$ with $a_q=\pm1$. Example: 539c1 twisted by $-7$ is 77c1, with $a_7=-1$ (re-verified).
- *Fix:* define $f'=f_{E'}$, with $a_p(f')=\chi(p)a_p(f)$ for $p\ne q$. For $h\ne f$: if $h=f$ then $g$ and $f'$ have the same $a_p$ for $p\nmid qN$, so $g=f'$ by strong multiplicity one, contradicting $M\ne$ level of $f'$.
- *Confidence:* high.

**C11. Protocol: the correction term $h_\ell$ was never blind-tested**
- *Where:* `sec:data` ("they are a confirmation and not a blind test for Conjecture `conj:euler`; the out-of-table curves ... are").
- *Problem:* the out-of-table set contains no 3Ns curve (`sec:oot` says so), so $h_3$ was fitted on, and only confirmed by, data already seen. The blind status of the out-of-table set for (eq:twist) is not stated either.
- *Fix:* add one sentence on each. Also say which reading of (eq:thm) the 3Ns violation counts use: with or without the $q=\ell$ terms. Below 10,000 the two readings give 36 and 24 violations (as reported).
- *Confidence:* high.

**C12. `lem:twist` proof: three slips**
- *Where:* proof of (ii).
- *Problems and fixes:*
  - "$q^2c_4,q^3c_6,q^6\Delta$" are the invariants of the twist by $q$, not by $q^*$. Write $(q^*)^2c_4$, $(q^*)^3c_6$, $(q^*)^6\Delta$. Only $q$-adic valuations are used.
  - The cubic of the twisted model after removing powers of $q$ is $T^3+ea_2T^2+a_4T+ea_6$, with $e=q^*/q=\pm1$; its roots are $e$ times the original ones.
  - "The conductor exponents are the standard ones for q odd (tame)" holds only for the exchanges listed. At $q=3$ a general additive curve can be wild.
- *Confidence:* high.

**C13. `lem:euler` proof: two slips**
- *Where:* types II/IV ("$\mathbb{Z}_\ell[\zeta_3]\simeq\mathrm{End}_{I_q}(V)$"), types III/III* ("the diagonal element").
- *Fix:*
  - Write $\mathrm{End}_{I_q}(T)=\mathbb{Z}_\ell\otimes\mathbb{Z}[\zeta_3]$. It is not a field for $\ell\equiv1\pmod3$.
  - Replace "the diagonal element" by "$\tau$", the generator of the inertia image. There is no diagonal form over $\mathbb{Q}_\ell$ when $\ell\equiv3\pmod4$; $\tau$ has trace 0 and spans the invariant line.
- *Confidence:* high.

**C14. Section 4.2: $M_{f,\lambda}$ is $H^1(E,\mathbb{Z}_\ell)$, the dual of $T_\ell E$**
- *Where:* "the lattice $M_{f,\lambda}$ of DFG04 and $T_\ell E$ are homothetic".
- *Fix:* "$\varphi_E^*$ identifies $M_{f,\lambda}$ with $H^1(E,\mathbb{Z}_\ell)=\mathrm{Hom}(T_\ell E,\mathbb{Z}_\ell)\simeq T_\ell E(-1)$ (A1). The adjoint is insensitive to dualising and twisting, so $A=\mathrm{ad}^0T$." This needs no irreducibility.
- *Confidence:* high.

## D. Expository and notational fixes

1. `lem:tamagawa-exp`: the proof calls the Tate parameter $u$, which clashes with $u=q_Eq^{-n}$ in `lem:tamfactor`. Call it $q_E$. Replace "an $\ell^t$-th power in $\mathbb{Q}_q^{ur}$ up to units" by "an $\ell^t$-th power in $\mathbb{Q}_q^{ur}$ (units are, by Hensel), i.e. $\ell^t\mid n_q$".
2. `sec:tam` uses $c_q$ for the class of $u$, while $c_q$ is the Tamagawa number elsewhere. Rename it $c(u)$.
3. Section 1.2: the parenthesis in $\mathrm{Tam}_p$ is misplaced. Write $\mathrm{Fitt}_{\mathbb{Z}_\ell}\bigl((H^1(I_p,M)_{tor})^{G_{\mathbb{Q}_p}}\bigr)$.
4. `lem:IV`: "$\mathbb{Z}_3[\sigma]/(\sigma^2+\sigma+1)$" should be $\mathbb{Z}_3[X]/(X^2+X+1)$.
5. `prop:ns`: the hypothesis "without complex multiplication" is not used, and the list of three images follows from the determinant, irreducibility and complex conjugation without Zywina. Drop it, or say it is not needed.
6. Example after `thm:qual`: 980i1 has $5\mid N$, so it illustrates the congruence, not the theorem. Say so.
7. Remark after the Example: "at $q=3$ in cases (a) and (b), where Lemma `lem:IV` does not apply because the ramification is wild". The obstruction is $q=\ell$. Write "where $q=\ell$".
8. Notation: $\chi_q$ (quadratic) and $\chi_\ell$ (cyclotomic) collide at 3, and the same character is called $\chi_{11}$ and $\chi_{-11}$. Use $\chi_{q^*}$ for the quadratic character.
9. `def:terms` is for $q\ne\ell$, but (eq:rule) and `rule(E,l)` use $t_\ell$ at $q=\ell$ (726a1 at 3). Extend the definition of $t_\ell$ to $q=\ell$.
10. Section 1.1: $\delta_p$ and the formula for $L_p$ are the definitions for $p\ne\ell$; at $p=\ell$ one uses $D_{cris}$. Add "for $p\ne\ell$".
11. Section 4.1: DFG04's integral structure is the image of the $U_0(N)$-invariants of compactly supported cohomology of the full-level curve, not literally $H^1(X_0(N),\mathbb{Z}_\ell)$. The two agree at non-Eisenstein $\mathfrak{m}$. Also, the pairing is the cup product times $1/2$, a unit for odd $\ell$. Reword (see E1).
12. `lem:dfg21`: the paper's hypothesis is a sufficient special case of DFG04's. Optionally say so.
13. `rem:free`: after A1 it is not needed for `thm:main`. If kept, note that identifying $T_\ell J_0(N)$ with $H^1(X_0(N),\mathbb{Z}_\ell)$ as Hecke modules uses Poincare duality composed with $w_N$, which is not Galois equivariant; freeness still transfers.
14. `sec:tam`: primes of type $\mathrm{I}_n^*$ can be included (C3).
    - Below 10,000 (as reported): at $\ell=3$, 1,050 curves, equality rises from 56.8% to 68.0%; at $\ell=5$, 252 curves, from 203 to 220; no violation once CM curves are excluded.
    - "Exactly where the Tamagawa factor ... exceeds" overstates, since the Selmer length also contributes. Write "the extra divisibility predicted by the Tamagawa factor is always present".
15. Appendix: the Kodaira codes $n+4$, $-(n+4)$ are valid for $n\ge1$; $\mathrm{I}_0$ is 1 and $\mathrm{I}_0^*$ is $-1$.
    - Say that `rule` must be run on the optimal curve with $E[\ell]$ irreducible. Re-verified: 990h1 gives `[4, 3]` while the optimal 990h3 gives `[3, 3]`; 11a1 at $\ell=5$ gives `[0, 1]`.
    - `ellmoddegree` needs about 32 MB in PARI 2.17 (the "few hundred megabytes" is for 2.15 at larger conductors).
16. `sec:sharp`: the calibration count shows the statement is strong (far from vacuous), not that it is valid. The odd-part statistic is range dependent: 1.85% on the working set, 17.1% below 10,000 (as reported). Optionally say so.
17. After `lem:h0` is fixed (C1), simplify "for $E$ without complex multiplication" in Section 1.3 and `sec:anomaly` accordingly.

## E. Open items to check

**E1. DFG04 integral structure versus $H^1(X_0(N),\mathbb{Z}_\ell)$**
- *What to check:* that the comparison map has Eisenstein cokernel, so that the two agree after localising at a non-Eisenstein $\mathfrak{m}$. This is what A1 needs.
- *Where:* DFG04, the definition of the integral structure in \S1.5 and \S1.6.
- *Status:* the definitions are certain; the comparison is a sketch. Medium-high.

**E2. DFG04 renumbering**
- A 2025 arXiv version (arXiv:2512.02348) uses different numbering. All numbers cited in the paper (Thms 0.1, 0.2, 2.7, 2.15, 3.7; Prop. 1.4(c); Lemmas 2.1, 2.12; (13), (14), (31), (57); p. 708; \S\S1.5.3, 1.6.1, 1.6.2, 1.7.2, 1.7.3, 1.8.2, 2.1) were confirmed against the published Ann. Sci. ENS 37 (2004). Make sure the bibliography entry points to that version.
- DFG04 Theorem 3.7 does cover $\ell=3$ in weight 2, since $S_f$ excludes only $\ell\mid2N$ and the induced case.

**E3. Calegari-Emerton**
- The statement in B7 was read from arXiv math/0503359 (Theorem 1.1). Confirm the theorem number and wording in the published version cited as `CalegariEmerton09`.

**E4. A6(ii) when $3\mid N$**
- When $3\mid N$, the proof does not exclude the order-4 inertia occurring only at 3. Data says it never does: 28 of 28 optimal curves below 10,000; 120 curves in all classes as reported.
- Either restrict the proposition to $3\nmid N$ or find an argument.
- At $p=2$, the Kodaira type of the order-4 inertia prime is III or III* in all 16 cases. This is not proved, but it is not needed for $e_3\ge1$.

**E5. Step 1 of `thm:quant` as an equality (A3)**
- Reported with a computation at level 539 (congruence modules of orders 288 and 504), not double-checked. Medium.
- For reference, my computation gives $r=288$ for 539c1 and $r=504$ for 539d1.

**E6. Type exchanges at $q=3$ (A12)**
- One step of the sketched proof needs a reference (for example Kraus 1989 or Dokchitser-Dokchitser). Medium.

**E7. Sutherland labels**
- 3Ns, 3Cs.1.1 and 3B.1.1 are used as in Cremona's `galrep` file, and are consistent with the intrinsic checks: 14a1 has 3Cs.1.1 with a rational 3-torsion point; the 3Ns curves have the division polynomial factoring as two quadratics.
- Check them against the tables of Sutherland16 before relying on the row/column convention, which swaps 3B.1.1 and 3B.1.2.

**E8. Theorem numbers**
- Insert theorem numbers for Zywina15 (the list of mod 3 images) and for Dickson's classification if cited. The textbook outlines could not confirm them.

**E9. Statistics to rerun on the paper's own ranges**
- The share of potentially good $\mathrm{I}_n^*$ at 2 (B4): 58% below 10,000 by my count; the source notes' 61% matches conductor below 5,000.
- The equality rates after `thm:twist` (B2).
- The 3Ns violation count under a stated reading (C11).

## F. Additions from writing the chapters

* **F1 (Chapter 10; strengthening; important_notes point 81).** Open question 6 of the revised paper is settled:
  under the twist by Q(sqrt(-3)) the types exchange II<->IV*, III<->III*, IV<->II* at q = 3 with f_3 unchanged,
  given only the Ogg-Saito formula; so the max formula for w_l(E,q) of Section 1.4 holds at q = 3. Proved in
  Chapter 10 (prop:reduction:twist-at-3); checked on all 5,122 pairs below conductor 10,000. This replaces the
  "need a reference" of item E for the twist exchanges at q = 3.
* **F2 (Chapter 10; data protocol; point 82).** PARI 2.17.2 returns q_E^5 for ellinit(E, O(2^k)).tate[3] when
  v_2(j) = -1. No count changes, but Sections sec:tam and sec:data should say how q = 2 was handled.
* **F3 (Chapter 10; expository; point 83).** Remark rem:wild's 58% is the share among curves numbered 1; over all
  curves it is 61%. Name the population.

* **F4 (Chapter 11; correction; point 90).** sec:boundary: "28 of them with 3 | N" should be 44 (of the 90 non-CM
  optimal curves with image Ns below 10,000), and the count omits 13 optimal CM curves with image N_s(F_3)
  (j = -32768, 8000). Items A6 and E4 above repeat "28"; E4's check is 44 of 44.
* **F5 (Chapter 11; correction, minor; point 91).** sec:forms: the 1,170 failures at l = 3 are the non-CM ones; CM
  curves with j in {-32768, 8000}, 3 not dividing N, also fail (20 below 10,000).
* **F6 (Chapter 9; expository; points 92, 93).** sec:data should say whether the extension-range test used only
  classes with determined optimality (w_3 is not proved class-invariant); prop:no9 should cite Ligozat75 as the
  primary source for cyclic 27-isogenies.

* **F7 (Chapter 13; correction; point 94).** rem:afterquant (2): "open" is contradicted; r_E divides
  eta^Hecke(g^S) as integers, so Step 1 is an equality under thm:quant's hypotheses. E5 upgraded to settled.

* **F8 (Chapter 19; correction; point 95).** rem:wild: 1,143 and 2,283 are all-curve counts; over optimal non-CM curves
  534 and 1,308; "of shape (ii)" is automatic.
* **F9 (Chapter 18; expository; points 96, 97).** lem:tamfactor proof: q^{-1}Ad rho(Frob), not q^{-1}rho(Frob); lem:dfg21
  needs "l not in Sigma" for the paragraph after it.

## Re-verification log

| curve | what was checked | result |
|-|-|-|
| 336f1 | type II at 2, $P_2$, $e_3$, degree | II, $1+2X$, 1, 24 |
| 1232l1 | type at 2, $P_2$, degree, twist | II*, $1+2X-4X^2-8X^3$, 288, $=77a1\otimes\chi_{-4}$, $a_2(77a1)=0$, `rule` = `[2, 2]` |
| 592c1 | type at 2, $P_2$, degree, twist | II*, $1-2X+4X^2-8X^3$, $80=2^4\cdot5$, $=37a1\otimes\chi_{-4}$, `rule` at 5 = `[1, 1]` |
| 14a1 | image, torsion, types, degree | 3Cs.1.1, $\mathbb{Z}/6$, $\mathrm{I}_6$ at 2, $\mathrm{I}_3$ at 7, 1 ($D=2$) |
| 714i1 | torsion, image, degree, $D$ | $\mathbb{Z}/9$, 3B.1.1, 1080, $D=2$ |
| 6942n1 | torsion, image, degree, $D$ | $\mathbb{Z}/9$, 3B.1.1, 65664, $D=2$ |
| 27a1 | degree, torsion, $j$ | 1, $\mathbb{Z}/3$, 0 (CM) |
| 243b1 | degree, torsion, $j$ | 9, $\mathbb{Z}/3$, 0 (CM) |
| 77c1 | type at 7, $a_7$, twist | $\mathrm{I}_3$, $-1$, $=539c1\otimes\chi_{-7}$ |
| 99a1 | degree, congruence number | 4, 12 |
| 726a1 | degree, $r$, image, type at 11, `rule` | 144, 1584, 3Ns, III, `[2, 2]` both ways |
| 539d1 | degree, $r$, type at 7, $e_3$, twist | 72, 504, $\mathrm{I}_0^*$, 2, twist by $-7$ is 11a3 |
| 52a1 | type at 2, $P_2$, degree, congruence | IV*, $1+2X$, 3, $\equiv f_{26b}-f_{26b}(2z)\bmod3$ ($n\le200$), $a_2(26b1)=1$ |
| 121a1, 539c1, 980i1 | degrees, Example congruences | 6, 288, 2880; all $n$ to 400/400/1000 |
| 121d1/11a1, 980i1/140b1 | $v_3$ of degrees | 1/0, 2/1 |
| 11a1 twists | by $-11$ and $-7$ | 121d2 ($\mathrm{I}_5^*$), 539d2; 11a3 by $-11$ is 121d1 ($\mathrm{I}_1^*$) |

Population checks below 10,000 (optimal curves):
- IV/IV* at 2: 3,194 curves, all with $P_2=1+2X$.
- $P_2$ by type at 2: see B4.
- 3Ns structure: 90 curves, see A6.
- Exact degree formula: 5 curves, see A10.
- $H^1(C_3,\mathrm{ad}^0T)=0$: see A2.
