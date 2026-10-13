# Chapter 11: Galois representations of elliptic curves (`ch:galrep`, `chapters/ch11_galrep.tex`)

Stage 1 line-up. Part III (Curves and elliptic curves). Target length 2,770 lines of LaTeX (card excluded; see Part 3),
inside the 2,800 lines that PLAN.md Section 7.3 allows for this chapter.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the
Chapter 2 to 9 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference
(book and chapter or section; a theorem number only where the outline author is sure, otherwise the section, and
numbers marked "(verify)" must be checked before they are printed); the paper's use by its `\label` names, or
"background". Every computation quoted below (3-division polynomials, image labels, inertia images per Kodaira type,
Euler factors at 2, congruences, Serre conductors, the structure of the 3Ns curves, the Eisenstein data) was checked
with PARI/GP 2.15 through `cypari2` in `/tmp/ch11` against Cremona's `ecdata` files `allcurves`, `galrep`,
`alldegphi` for conductors below 10,000 (verification log, Part 6.6).

## 0. What this chapter is for

### 0.1 Purpose

The paper works throughout with $\rho=\rho_{E,\ell}$ on $T=T_\ell E$ and its reduction $\bar\rho$ on $E[\ell]$. Every statement it makes
about these representations, as opposed to the algebra of the representations (Chapter 4), the field theory
(Chapters 5 to 7) or the geometry of the curve (Chapters 9, 10), is collected and proved here. Concretely the
chapter must deliver:

1. **The local representation at every prime $p\ne\ell$, by reduction type.** Neron-Ogg-Shafarevich; the Tate-curve
   shape at a multiplicative prime (DDT Theorem 3.1(e) for elliptic curves, with the corner $\varepsilon\kappa$ of
   important_notes.md point 42); the paper's **Lemma lem:tamagawa-exp proved in full**; the potentially multiplicative
   additive case at every $q$, including $q=2$ (needed for important_notes.md point 18); the image of inertia at a
   potentially good additive prime by Kodaira type (the "inertia images and invariants" half of **Lemma lem:euler**);
   $\delta_p=\dim V^{I_p}$ of Section 1.1.
2. **The mod 3 inertia picture.** The paper's **Lemma lem:IV and Remark rem:types proved in full**, Remark rem:types in its
   corrected, complete form (important_notes.md point 22), and a new uniform tool: for additive reduction at $q\ne\ell$,
   $E[\ell^k]^{I_q}\simeq\Phi_q(\bar\F_q)[\ell^k]$ (item 2.2). The tool gives a second proof of Lemma lem:IV valid at every
   $q\ne3$ and **settles important_notes.md point 43**: at $q=2$, types $\mathrm{IV}$, $\mathrm{IV}^*$ have cyclic inertia
   image of order $3$, so $P_2(X)=1+2X$ and $e_3(E,2)=1$ are theorems and the exception in Proposition prop:forms
   disappears (item 4.4).
3. **The representation at $\ell$** (good reduction): finite flatness, the Deligne-Fontaine description, the determination
   of $a_\ell\bmod\ell$ by $\bar\rho|_{D_\ell}$; this is the local analysis at $p=\ell$ in **Lemma lem:old**.
4. **Conductors.** The Serre conductor $N(\bar\rho)$, the formula $a_p(\bar\rho_{E,\ell})=f_p(E)-\dim_{\F_\ell}\Phi_p(\bar\F_p)[\ell]$ (item
   6.2), hence $N(\bar\rho)\mid N$; this is what the **optimal-level paragraph of Section 3** and cases (a), (b), (c) of
   Theorem thm:qual need.
5. **Images.** Serre's open image theorem (stated), the complete list of mod $3$ images for every $E/\Q$ proved from
   the group theory of Chapter 1 (item 7.3), Sutherland's labels checked against `ecdata`, Zywina's lists (stated).
6. **The hypothesis of Theorem thm:main.** Absolute irreducibility on $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$; the paper's
   **Proposition prop:ns proved in full** (corrected as in important_notes.md points 1, 9, 33); the paper's **Lemma
   lem:h0 proved in full in its corrected form** ($h_\ell(E)=0$ for $\ell\ge5$, $h_3(E)\le1$, with or without CM;
   points 5, 6, 10, 14); and a new observation: for $\ell\ge5$, $\ell\nmid N$, irreducibility already implies absolute
   irreducibility on $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$ (item 8.2), so $\ell\notin S_f$ iff $E[\ell]$ is irreducible and, for
   $\ell=3$, the image is not $N_s(\F_3)$ (item 8.6).
7. **Section sec:anomaly.** The structure of the curves with image 3Ns (item 8.4): every such curve has a prime
   $p\ne3$ with cyclic inertia of order $4$ (type $\mathrm{III}$ or $\mathrm{III}^*$ when $p\ge5$, with $p\equiv1$ or
   $11\pmod{12}$), at which $e_3(E,p)\ge1$; the paper reports this as an observation on the tables.
8. **Section sec:eis and Conjecture conj:eis.** Reducible $\bar\rho$: the semisimplification, ordinarity at $\ell$, the
   label dictionary 3B.1.1, 3B.1.2, 3Cs.1.1 (important_notes.md point 44), and the restatement of Chapter 9's proof that
   $\Z/3\oplus\mu_3$ and a rational point of order $9$ cannot coexist (point 17).
9. **Serre's conjecture for $\bar\rho_{E,\ell}$** in the optimal-level form the paper uses (statement, with the
   elliptic-curve inputs proved here; the general theory is Chapter 15).

### 0.2 Split with the neighbouring chapters (decided here, consistent with PLAN.md Section 4 and the written outlines)

* **Chapter 1** proves the group theory of $\GL_2(\F_3)$: the 55 subgroups, the three irreducible images with surjective
  determinant and an element of determinant $-1$, trace $0$ (its 6.7), orbits on lines (6.8), Sutherland's labels as
  intrinsic subgroups (6.10), Dickson (5.10), $1+\ell M_2(\Zl)$ torsion-free for $\ell$ odd (7.4). Chapter 11 cites these and
  adds which of them occur for $E/\Q$ and why.
* **Chapter 4** proves the representation theory: distinct-eigenvalue criterion (2.4), unique stable line of a
  non-split extension (3.6), Brauer-Nesbitt (5.2, 5.3), Clifford theory for index two (6.6, 6.7), the trace-zero lemma
  and $H^0(\ad V\otimes\chi)$ (7.2, 7.4), the $\GL_2(\F_3)$ table and the representation-theoretic core of Proposition prop:ns
  (8.1 to 8.5), unipotent and cyclic shapes and their fixed spaces on $V$ and $\ad V$ (9.1 to 9.4), lattices, homothety
  and the length lemma behind $h_\ell$ (10.1 to 10.5). Chapter 11 never reproves these; it supplies the Galois and
  elliptic-curve inputs (which group, which character, which Kodaira type).
* **Chapter 5** proves continuity, the cyclotomic character, complex conjugation and "irreducible iff absolutely
  irreducible" for $\det\bar\rho(c)=-1$ (galois:complex-conjugation (d)), restriction to $G_{\Q(\sqrt{\ell^*})}$
  (galois:restriction, galois:index-two-restriction), Chebotarev plus Brauer-Nesbitt (galois:chebotarev-brauer-nesbitt,
  galois:congruent-ap), the determinant obstruction $\chi_\ell^2\not\equiv1$ (galois:twist (c)), the quartic-on-lines
  proposition and the example $y^2=x^3-6x-8$ (6912d1). Chapter 11 applies them.
* **Chapter 6** proves Frobenius elements, the finite-level tame relation (3.11, 3.12), $\Z_3[\zeta_3]$ as a DVR and
  $T\simeq\Z_3[\zeta_3]$ (4.7, 4.8), the commutant and the Frobenius action $\chi_{-3}(q)$, $\chi_{-4}(q)$ (4.10), the twist
  detector by traces at inert primes (6.4), CM and $a_p=0$ (6.5), Kronecker-Weber (5.5).
* **Chapter 7** proves the local field theory: tame character and $\Frob\,t\,\Frob^{-1}=t^q$ (5.3, 5.4), finite tame images
  are cyclic (5.6), wild images (5.7), Kummer classes on inertia (6.2), Weil-Deligne representations, $\mathrm{sp}(2)$, the
  Tate shape (7.6), invariants, $L$-factors, Swan and Artin conductors (8.1 to 8.4), and the shapes table 9.4, whose
  Kodaira column it leaves as a black box to Chapters 10 and 11. **Chapter 11 supplies that column as theorems** (items
  3.2, 3.4, 4.1, 4.4) and does not repeat the Weil-Deligne or $L$-factor computations.
* **Chapter 9** proves $\rho$, $\bar\rho$, $\det\rho=\chi_\ell$, complex conjugation (5.1 to 5.6), division polynomials and
  $\psi_3$ (4.4 to 4.6), CM (6.5), rational isogenies, $\Z/\ell\oplus\mu_\ell$ and the no-$27$-isogeny argument (9.5 to 9.9),
  twists $\rho\otimes\chi_d$ (10.3), and the easy half of Neron-Ogg-Shafarevich (8.6).
* **Chapter 10** (outlined in parallel) proves minimal models, reduction types, $E_0$, $E_1$ and the formal group,
  $E(K)/E_0(K)\simeq\Phi(k)$, Kodaira types and Tate's algorithm, the component groups $\Phi_q(\bar\F_q)$ by type,
  conductor exponents and Ogg's formula, the semistable reduction theorem, the Tate curve with its Galois module
  $E_q[\ell^t]$ (statement), Kraus's semistability defect $12/\gcd(v_q(\Delta),12)$ for $q\ge5$, Lemma lem:twist (i), (ii)
  and Remark rem:wild. **Chapter 11 uses all of these as black boxes with `\Cref{ch:reduction}` and proves the
  representation-theoretic consequences.** If the Chapter 10 outline proves the Galois-theoretic consequences of the
  Tate curve itself (the matrix shape, Lemma lem:tamagawa-exp), Chapter 11 keeps them anyway, because PLAN.md puts
  Lemma lem:tamagawa-exp here; the Chapter 10 writer should then only state them.
* **Chapter 15** proves Galois representations of newforms, local-global compatibility, the optimal-level theorem in
  general (DDT Theorem 3.15) with the trivial-nebentypus argument, Ribet's level lowering, Lemma lem:old and Theorem
  thm:qual. Chapter 11 supplies the elliptic-curve inputs (local structure at $p\mid N$ and at $\ell$, Serre conductor,
  finite flatness, Serre weight) and states Serre's conjecture for $\bar\rho_{E,\ell}$; the Deligne-Fontaine description
  is proved (sketched) here for $E$ and quoted for newforms in Chapter 15.
* **Chapters 16, 18, 19, 20.** Chapter 16 has the cohomology of the Tate shape (it imports the shape from here);
  Chapter 18 proves Lemma lem:tamfactor and restates Lemma lem:h0 (proved here) in Selmer language; Chapter 19
  computes $L_q(A_f,s)$ and $e_\ell(E,q)$ (Lemma lem:euler in full) from the inertia images proved here; Chapter 20 uses
  $\ell\notin S_f$ through item 8.6.
* **Chapters 21, 22** use the card: the tour cites items 3.3, 4.3, 4.5, 8.3, 8.5; the computation chapter uses 7.3, 7.6
  (`ns3`, `elldivpol`).

## 1. Global conventions fixed in this chapter

* **C1 (objects).** $E/\Q$ is given by a global minimal model, conductor $N$; $\ell$ is a prime, odd unless said otherwise;
  $T=T_\ell E$, $V=T\otimes\Ql$, $\rho=\rho_{E,\ell}\colon G_\Q\to\Aut_{\Zl}(T)\simeq\GL_2(\Zl)$, $\rho\bmod\ell^k$ the action on
  $E[\ell^k]=T/\ell^kT$, $\bar\rho=\bar\rho_{E,\ell}$ on $E[\ell]$; $A=\ad T$, $A_f=\ad V$ (trace zero, the paper's macro `\ad`).
  $\delta_p=\dim V^{I_p}$. These are Chapter 9's objects (C1 there) and the paper's (Section 1.1).
* **C2 (local data).** For a prime $q$: $D_q\simeq G_{\Q_q}$ and $I_q$ via a fixed embedding $\Qbar\to\Qbar_q$ (Chapter 6, 3.10);
  $f_q=f_q(E)$ the conductor exponent; $n_q=v_q(\Delta_{\min})$ at a multiplicative prime; $q_E\in\Q_q^\times$ the Tate parameter,
  $v_q(q_E)=-v_q(j)$, and $u=q_Eq^{-v_q(q_E)}$ its unit part (important_notes.md point 8: the Tate parameter is never called $u$);
  $\Phi_q=\Phi_q(\bar\F_q)$ the geometric component group of the Neron model (the paper's $\Phig_q$), $c_q=\#\Phi_q(\F_q)$.
  Kodaira symbols as in PLAN.md 7.1.
* **C3 (Frobenius).** As in Chapter 7 (L3) and Chapter 9 (C5): $\Frob_p$ is an **arithmetic** Frobenius; $\Phi_p=\Frob_p^{-1}$ is
  the geometric one; group-theoretic statements (conjugation, the Tate matrices) use $\Frob_p$; $L$-factors use $\Phi_p$
  and are Chapter 19's. On $V_\ell E$ at a good prime the arithmetic Frobenius has characteristic polynomial $X^2-a_pX+p$,
  roots $\alpha,\beta$; the geometric one has $\alpha^{-1},\beta^{-1}$; on $\ad V$ both give $\alpha/\beta,1,\beta/\alpha$
  (important_notes.md B1). The relation on tame inertia is $\Frob\,t\,\Frob^{-1}=t^{q}$. Do not use $\Phi$ for both the geometric
  Frobenius and the component group in one display: write $\Phi_q$ for the component group only with the subscript and
  $\Frob^{-1}$ for the geometric Frobenius where a clash is possible.
* **C4 (characters).** $\chi_\ell$ is the $\ell$-adic cyclotomic character, $\bar\chi_\ell$ its reduction; $\chi_d$ the quadratic
  character of $\Q(\sqrt d)$; $q^*=(-1)^{(q-1)/2}q$ and, as in the paper, $\chi_q:=\chi_{q^*}$; $\ell^*$ likewise. Where $\chi_3$ could
  mean either, write $\chi_3^{\mathrm{cyc}}$ or $\chi_{-3}$ (important_notes.md point 32); $\bar\chi_3=\chi_{-3}$. $\omega=\bar\chi_\ell|_{I_\ell}$ and
  $\omega_2$ are the fundamental characters (5.2).
* **C5 (standard matrices).** As Chapter 1, 6.2 and Chapter 4, C6: $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$,
  $w=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$, $u=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$, the subgroups
  $C_s,N_s,C_{ns},N_{ns},\mathrm B,\mathrm U,Q_8,C_4=\langle J\rangle$ of $\GL_2(\F_3)$. The paper's $\sigma$ is an element of order $3$ in the
  image of inertia (Lemmas lem:IV, lem:euler); the matrix $\operatorname{diag}(1,-1)$ is written $h$ here, as in Chapter 4.
* **C6 (labels).** Sutherland's labels (3B, 3B.1.1, 3B.1.2, 3Cs, 3Cs.1.1, 3Ns, 3Nn, ...) as in `ecdata` and the paper,
  always accompanied in the text by the intrinsic description (7.3, 7.4). "Surjective" has no label. Curve labels are
  Cremona's (Chapter 9, C6).
* **C7 (typography).** PLAN.md 7.2: no dash ligatures ("Neron-Ogg-Shafarevich", "Deligne-Fontaine", "Serre-Tate",
  "Khare-Wintenberger", ranges "1 to 8"); ASCII source; labels `...:galrep:...`; the line-up names below are the label
  stems.

## 2. Line-up of the core results, in teaching order

### Section 1. The representations $\rho_{E,\ell}$ and $\bar\rho_{E,\ell}$: recap, twists, irreducibility

**1.1 `def:galrep:rho`** (definition and proposition, recap; P with the proofs cited). For $E/\Q$ and a prime $\ell$: $T$, $V$,
$\rho$, $\rho\bmod\ell^k$, $\bar\rho$ as in C1. (i) $\rho$ is continuous; the field cut out by $\rho\bmod\ell^k$ is $\Q(E[\ell^k])$
(Chapter 9, 5.4; Chapter 5, galois:continuous-reps). (ii) $\det\rho=\chi_\ell$ (Weil pairing, Chapter 9, 5.2, 5.3); so
$\Q(\zeta_\ell)\subset\Q(E[\ell])$, $\det\bar\rho=\bar\chi_\ell$ is surjective onto $\F_\ell^\times$, and $\bar\rho(G_{\Q(\sqrt{\ell^*})})=\{g\in\bar\rho(G_\Q):\det g\in(\F_\ell^\times)^2\}$
(Chapter 5, galois:restriction (c)). For $\ell=3$: $\bar\chi_3=\chi_{-3}$, the field cut out by $\det\bar\rho_{E,3}$ is $\Q(\sqrt{-3})$ and
$\bar\rho_{E,3}(G_{\Q(\sqrt{-3})})=\bar\rho_{E,3}(G_\Q)\cap\SL_2(\F_3)$. (iii) For $\ell$ odd and $c$ a complex conjugation, $\rho(c)$ is
conjugate in $\GL_2(\Zl)$ to $\operatorname{diag}(1,-1)$ ($T=T^{c=1}\oplus T^{c=-1}$, both of rank one, as $2\in\Zl^\times$ and $\det\rho(c)=-1$);
so $\bar\rho(c)$ has determinant $-1$ and trace $0$ (Chapter 9, 5.6). (iv) $\rho$ is unramified outside $N\ell$ (2.1 below).
Reference: SilvermanAEC III.7 and III.8; SerreAbelian I.1. Paper: Section 1.1 ($V$, $T$, $\rho$, $\bar\rho$), Proposition prop:ns
("$\det\bar\rho_{E,3}=\chi_{-3}$ cuts out $\Q(\sqrt{-3})$"; "an element of determinant $-1$ and trace $0$ (complex conjugation)"),
Lemma lem:h0, the hypothesis of Theorem thm:main.

**1.2 `conv:galrep:notation`** (convention). C1 to C6 of Part 1 typeset as `convention` environments, with the
dictionary arithmetic/geometric Frobenius (C3) and the warning on $\chi_3$ (C4). Paper: Section 1.1, Lemma lem:euler,
Lemma lem:tamfactor (important_notes.md points 8, 11, 32, B1).

**1.3 `prop:galrep:twist-isogeny`** (proposition; P). Let $E/\Q$, $\ell$ odd. (i) (Chapter 9, 10.3, cited.) For $d\in\Q^\times$,
$\rho_{E^{(d)},\ell}\simeq\rho_{E,\ell}\otimes\chi_d$; hence $\ad\rho_{E^{(d)},\ell}\simeq\ad\rho_{E,\ell}$, the projective images of $\bar\rho_{E^{(d)},\ell}$ and
$\bar\rho_{E,\ell}$ coincide, and irreducibility of $E[\ell]$ is twist-invariant. (ii) Effect on the mod $3$ labels (item 7.3):
twisting by $\chi_{-3}$ exchanges 3B.1.1 and 3B.1.2 and fixes every other label; twisting by $\chi_d$ with
$d\notin\{1,-3\}\bmod\Q^{\times2}$ sends 3B.1.1 and 3B.1.2 to 3B and 3Cs.1.1 to 3Cs, and fixes 3Ns, 3Nn and the surjective
image. (Proof: $\operatorname{diag}(1,\chi_{-3})\otimes\chi_d=\operatorname{diag}(\chi_d,\chi_d\chi_{-3})$;
$\begin{psmallmatrix}1&*\\0&\chi_{-3}\end{psmallmatrix}\otimes\chi_{-3}=\begin{psmallmatrix}\chi_{-3}&*\\0&1\end{psmallmatrix}$; the
property $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ is twist-invariant, which keeps 3Ns and 3Nn apart although $N_s(\F_3)\subset N_{ns}(\F_3)$
(important_notes.md point 2); $\GL_2(\F_3)$ has a unique subgroup of index $2$, $\SL_2(\F_3)$, whose projective image is $A_4\ne S_4$.)
(iii) (Chapter 9,
9.9, cited.) If $E[\ell]$ is irreducible, all curves of the isogeny class have isomorphic $T_\ell$, hence the same $\rho$, $\bar\rho$,
image label at $\ell$, $\ad T$ and $h_\ell(E)$ (important_notes.md point 27). Reference: elementary. Paper: Lemma lem:twist,
Theorem thm:qual (b), (c) ($\bar\rho\otimes\chi$ satisfies the hypotheses since $\bar\rho$ does), Theorem thm:quant ($\ad T$ unchanged),
the proof of Theorem thm:main ($\mathrm I_n^*$ primes), Section sec:eis.

**1.4 `prop:galrep:irreducibility`** (proposition; P, from Chapters 4, 5, 9). Let $\ell$ be odd. (i) $\bar\rho_{E,\ell}$ is irreducible
iff it is absolutely irreducible (1.1(iii) and Chapter 4, 2.4: a stable line of $\bar\F_\ell^2$ is an eigenline of $\bar\rho(c)$, and both
eigenlines are $\F_\ell$-rational). (ii) $\bar\rho_{E,\ell}$ is reducible iff $E$ has a rational $\ell$-isogeny (Chapter 9, 9.5); for $\ell=3$
iff $\psi_3$ has a rational root. (iii) (Chebotarev and Brauer-Nesbitt, Chapter 5, galois:congruent-ap.) $\bar\rho^{\mathrm{ss}}$ is
determined by $a_p(E)\bmod\ell$ for $p$ in any set of density one with $p\nmid N\ell$; if $\bar\rho$ is irreducible, $\bar\rho$ itself is. If $h$ is a
newform of weight $2$ with coefficients in $\mathcal O$, $\lambda\mid\ell$, $k=\mathcal O/\lambda$, and $a_p(h)\equiv a_p(E)\pmod\lambda$ for a density-one set of
$p$, then $\bar\rho_{h,\lambda}\simeq\bar\rho_{E,\ell}\otimes_{\F_\ell}k$ when $\bar\rho_{E,\ell}$ is irreducible (absolute irreducibility, (i), is what makes this
work: important_notes.md point 10). Reference: as cited. Paper: Lemma lem:old (case $p\nmid\ell N$: "$\bar\rho_h\simeq\bar\rho$ by Chebotarev
and Brauer-Nesbitt, $\bar\rho$ being irreducible"), Lemma lem:h0 ("irreducible" means absolutely irreducible), Theorem thm:quant,
Conjecture conj:euler ("$E[\ell]$ irreducible").

### Section 2. Neron-Ogg-Shafarevich, component groups and inertia invariants

**2.1 `thm:galrep:nos`** (theorem, the criterion of Neron, Ogg and Shafarevich; P for (a) to (d), S for (e), (f)). Let $K/\Q_p$ be
finite, $E/K$, $\ell\ne p$. The following are equivalent: (a) $E$ has good reduction; (b) $I_K$ acts trivially on $T_\ell E$; (c) $I_K$ acts
trivially on $E[m]$ for every $m$ prime to $p$; (d) $I_K$ acts trivially on $E[m]$ for infinitely many $m$ prime to $p$. Moreover
(e) $E$ has potentially good reduction iff $\rho_{E,\ell}(I_K)$ is finite, for one (equivalently every) $\ell\ne p$; (f) $E$ has
potentially multiplicative reduction ($v_K(j)<0$) iff $\rho_{E,\ell}(I_K)$ is infinite, and then $\rho_{E,\ell}(I_K)$ contains a unipotent
element $\ne1$ (3.2, 3.4). For $E/\Q$: $\rho_{E,\ell}$ is unramified at $p\ne\ell$ iff $p\nmid N$. Proof: (a)$\Rightarrow$(c) is Chapter 9, 8.6
(reduction is injective on prime-to-$p$ torsion); (d)$\Rightarrow$(a): over $K^{\mathrm{ur}}$ (through finite unramified $K'$), if $E$ had
bad reduction then $E(K')\supset E_0(K')\supset E_1(K')$ with $E_1$ pro-$p$, $E_0/E_1\simeq\tilde E_{\mathrm{ns}}(k')$ equal to $k'^+$ or a
one-dimensional torus, and $E/E_0\simeq\Phi(k')$ of bounded order (Chapter 10); then $\#E(K^{\mathrm{ur}})[m]\le m\cdot\#\Phi$ for $m$ prime to
$p$, contradicting $E[m]\subset E(K^{\mathrm{ur}})$ of order $m^2$ for large $m$. (e), (f): semistable reduction theorem (Chapter 10)
plus (a) to (d) over a finite extension, and the Tate shape 3.2. Reference: Serre-Tate 1968, Section 1, Theorem 1 and
Section 2 (add `SerreTate68` to `bib/ch11.bib`, see Part 6.5); SilvermanAEC VII.7 (Theorem 7.1, verify). Paper: Section 1.1
($\delta_p$), Lemma lem:tamagawa-exp, Lemma lem:IV ("potentially good", "finite image"), Lemma lem:old ("$\bar\rho_h$ unramified"),
the optimal-level paragraph ("$N(\bar\sigma)$ is prime to every prime at which $\bar\sigma$ is unramified").

**2.2 `lem:galrep:component-invariants`** (lemma; P given Chapter 10). Let $q\ne\ell$ be primes, $E/\Q_q$ with bad reduction,
$\Phi_q=\Phi_q(\bar\F_q)$, $k\ge1$. (i) If the reduction is additive, there is a $\Gal(\bar\F_q/\F_q)$-equivariant isomorphism
$$E[\ell^k]^{I_q}\ \simeq\ \Phi_q[\ell^k];$$
in particular $E(\Q_q)[\ell^\infty]\simeq\Phi_q(\F_q)[\ell^\infty]$. (ii) If the reduction is multiplicative, there is an exact sequence of
$\Gal(\bar\F_q/\F_q)$-modules $0\to\mu_{\ell^k}\to E[\ell^k]^{I_q}\to\Phi_q[\ell^k]\to0$, with $\Phi_q\simeq\Z/n_q$. (iii) Consequently, for $\ell$ odd,
$\dim_{\F_\ell}E[\ell]^{I_q}$ is: $1+[\ell\mid n_q]$ for $\mathrm I_{n}$, $n\ge1$; $1$ for $\mathrm{IV}$, $\mathrm{IV}^*$ if $\ell=3$; $0$ for every other additive
type (the orders of $\Phi_q$ for additive types are $1,2,3,4$: Chapter 10). Proof: for each finite unramified $K'/\Q_q$ with
residue field $k'$: $E(K')/E_0(K')\simeq\Phi_q(k')$ (Neron model and Hensel, Chapter 10), $E_1(K')$ is a $\Z_q$-module, hence uniquely
$\ell$-divisible, and $E_0(K')/E_1(K')\simeq\tilde E_{\mathrm{ns}}(k')$, which is $k'^+$ (additive: uniquely $\ell$-divisible) or $k'^\times$ (split over
large enough $k'$); the snake lemma for multiplication by $\ell^k$, and the union over $K'$, since $E[\ell^k]^{I_q}=E[\ell^k](\Q_q^{\mathrm{ur}})$.
Reference: the argument is the one in Serre-Tate 1968, Section 1; SilvermanAEC VII.6 and VII.7 (verify); ATAEC IV.9 for
$E/E_0\simeq\Phi$. Paper: Lemma lem:IV (second proof, 4.3), Remark rem:types ("$E[3]^{I_q}=0$", 4.5), Lemma lem:tamagawa-exp
(second proof, 3.3), Remark rem:wild and Proposition prop:forms (type $\mathrm{IV}$ at $2$, 4.4), the final check in the proof of
Lemma lem:tamfactor (the $\ell$-part of $c_q$; Chapter 18), the Serre conductor formula 6.2. Verified: at $q=2$ and $q\ge5$, for
Kodaira types sampled from every class (Part 6.6), $E[3]^{I_q}\ne0$ exactly for $\mathrm I_n$ and $\mathrm{IV}$, $\mathrm{IV}^*$.

**2.3 `thm:galrep:serre-tate`** (theorem; R, with (ii) and (iv) P). Let $E/\Q_q$ have potentially good reduction and $\ell\ne q$.
(i) (Serre-Tate) The kernel of $\rho_{E,\ell}|_{I_q}$ is $I_L=\Gal(\Qbar_q/L)$ with $L=\Q_q^{\mathrm{ur}}(E[m])$ for any $m\ge3$ prime to $q$; $L$ is the
smallest extension of $\Q_q^{\mathrm{ur}}$ over which $E$ acquires good reduction. So $\rho_{E,\ell}(I_q)\simeq\Gal(L/\Q_q^{\mathrm{ur}})$ does not depend on
$\ell$, and the characteristic polynomial of $\rho_{E,\ell}(\sigma)$, $\sigma\in I_q$, lies in $\Z[X]$ and does not depend on $\ell$. (ii)
$\rho_{E,\ell}(I_q)\subset\SL_2(\Zl)$ ($\chi_\ell$ is trivial on $I_q$), and for $\ell$ odd reduction modulo $\ell$ is injective on it
($1+\ell M_2(\Zl)$ is torsion-free, Chapter 1, 7.4); a finite subgroup of $\SL_2(\Ql)$ with a nonzero fixed vector is trivial, so
$V^{I_q}=0$ unless the reduction is good. (iii) (Kraus, Serre-Tate) $\rho_{E,\ell}(I_q)$ is cyclic of order $1,2,3,4$ or $6$ if $q\ge5$; one
of these or $C_3\rtimes C_4$ (order $12$) if $q=3$; one of these or $Q_8$ or $\SL_2(\F_3)$ if $q=2$. (iv) For $q\ge5$ it is tame (order
prime to $q$), hence cyclic (Chapter 7, 5.6), and its order is $12/\gcd(v_q(\Delta_{\min}),12)$ (Kraus's theorem, proved or stated in
Chapter 10; cite it, do not reprove). Reference: Serre-Tate 1968, Section 2 (theorem and corollary numbers: verify);
Kraus90 (cite the paper; theorem numbers not checked). Paper: Lemma lem:IV ("the semistability defect ... for any
$\ell\ne q$"), Lemma lem:euler ("the image of $I_q$ in $\Aut V$ is cyclic of order $3$ or $6$"), Remark rem:types, Remark rem:wild.

### Section 3. Good and multiplicative reduction; Lemma lem:tamagawa-exp

**3.1 `prop:galrep:good`** (proposition; P, citing Chapter 9, 8.6 and 2.1). Let $p\nmid N\ell$. Then $\rho$ is unramified at $p$, the
arithmetic Frobenius has characteristic polynomial $X^2-a_pX+p$ on $V$ (roots $\alpha,\beta$), the geometric one $X^2-\frac{a_p}pX+\frac1p$; on
$\ad V$ both act with eigenvalues $\alpha/\beta,1,\beta/\alpha$; $\delta_p=2$; $\bar\rho(\Frob_p)$ has characteristic polynomial $X^2-a_pX+p\bmod\ell$,
and for $\ell=3$ its orbit pattern on the four lines is the factorisation pattern of $\psi_3\bmod p$ for $p\nmid3\operatorname{disc}\psi_3$
(Chapter 5, galois:frobenius-on-lines). Reference: SilvermanAEC VII.7. Paper: Section 1.1, the table of Section 1
($\alpha$, $\beta$ for $E'$), Theorem thm:dfg14 (level-raising factor), Lemma lem:old (case $p\,\|\,N$ unramified:
"$X^2-a_p(h)X+p$").

**3.2 `thm:galrep:tate-shape`** (theorem; P given Chapter 10's Tate curve and Chapter 5's Kummer cocycle). Let $q$ be a prime of
multiplicative reduction, $\ell\ne q$, $\varepsilon\colon G_{\Q_q}\to\{\pm1\}$ the unramified character with $\varepsilon(\Frob_q)=a_q(E)$ ($+1$ split, $-1$
nonsplit), and $\kappa$ a Kummer cocycle of $q_E$ (Chapter 5, galois:l-adic-kummer), written in $\Zl$ after fixing a generator of
$\Zl(1)$. There is a $\Zl$-basis $e_1,e_2$ of $T$ in which
$$\rho(g)=\begin{pmatrix}\chi_\ell(g)\varepsilon(g)&\varepsilon(g)\kappa(g)\\0&\varepsilon(g)\end{pmatrix}\qquad(g\in G_{\Q_q}),$$
($T\simeq T_\ell E_{q_E}\otimes\varepsilon$; the corner is $\varepsilon\kappa$, important_notes.md point 42). Consequences: (i) on $I_q$,
$\rho(\sigma)=\begin{psmallmatrix}1&n_q\,t_\ell(\sigma)\\0&1\end{psmallmatrix}$ ($\kappa|_{I_q}=v_q(q_E)\,t_\ell$, Chapter 7, 6.2), a unipotent action through the
maximal pro-$\ell$ quotient of $I_q$, with infinite image; (ii) $V^{I_q}=\Ql e_1$, so $\delta_q=1$, and $\Frob_q$ acts on it by $a_q(E)q$;
(iii) $\Ql e_1$ is the unique $G_{\Q_q}$-stable line of $V$ (non-split extension of $\varepsilon$ by $\varepsilon\chi_\ell$, Chapter 4, 3.6);
(iv) the Weil-Deligne representation is $\mathrm{sp}(2)\otimes\mu_\varepsilon$, conductor exponent $1$ (Chapter 7, 7.6, 9.3); (v)
$(\ad V)^{I_q}=\Ql e$, $e=e_1\otimes e_2^\vee$, on which $\Frob_q$ acts by $q$ (and the geometric Frobenius by $q^{-1}$; Chapter 4, 9.1(iii)),
so $\dim(\ad V)^{I_q}=1$. Reference: SilvermanATAEC V.3 and V.5 (Tate curve); SerreAbelian IV, Appendix A.1 (verify); DDT
Theorem 3.1(e) as cited by the paper (the elliptic-curve case of a theorem on newforms; letter and number not checked).
Paper: Lemma lem:tamagawa-exp, Lemma lem:tamfactor (the matrices, $te_2=e_2+n'e_1$, $v_\ell(n')=v_\ell(n)$), Lemma lem:euler (type
$\mathrm I_n$), Lemma lem:old (cases $p\,\|\,N$), Section 1.1 ($\delta_q=1$); Chapter 16 imports the shape.

**3.3 `lem:galrep:tamagawa-exp`** (lemma, the paper's Lemma lem:tamagawa-exp; P, two proofs). Let $q$ be a prime of multiplicative
reduction, $n_q=v_q(\Delta_E)$, and $\ell\ne q$ a prime. Then $\rho_{E,\ell}\bmod\ell^t$ is unramified at $q$ iff $\ell^t\mid n_q$; this holds for split
and nonsplit reduction. Supplements: (i) the Tamagawa exponent $t_q:=\max\{t:\rho\bmod\ell^t\text{ unramified at }q\}$ (Kim and Ota) equals
$v_\ell(n_q)=v_\ell(-v_q(j))=t_\ell(E,q)$; (ii) $\#E[\ell^t]^{I_q}=\ell^{\,t+\min(t,v_\ell(n_q))}$; (iii) if $\ell\nmid n_q$, $\bar\rho|_{D_q}$ is ramified, a non-split
extension of $\varepsilon$ by $\varepsilon\bar\chi_\ell$ with a unique stable line, and $\bar\rho(I_q)$ has order $\ell$; (iv) if $\ell\mid n_q$, $\bar\rho|_{D_q}$ is
unramified and $\bar\rho(\Frob_q)$ has eigenvalues $a_q(E)q$ and $a_q(E)$ modulo $\ell$. Proof 1 (the paper's, expanded; important_notes.md
point 8): over the unramified quadratic extension (or $\Q_q$ if split) $E\simeq E_{q_E}$, which does not change $I_q$; $E[\ell^t]$ is
generated by $\mu_{\ell^t}$ and an $\ell^t$-th root of $q_E$ in $\Qbar_q^\times/q_E^{\Z}$; $I_q$ fixes $\mu_{\ell^t}$, and by Kummer theory over
$\Q_q^{\mathrm{ur}}$ (which contains $\mu_{\ell^t}$, $q\ne\ell$) it fixes $q_E^{1/\ell^t}$ iff $q_E$ is an $\ell^t$-th power in $\Q_q^{\mathrm{ur}}$; units of its valuation
ring are $\ell^t$-th powers (Hensel), so this holds iff $\ell^t\mid v_q(q_E)=n_q$ (Chapter 7, 6.2(v)). Proof 2: 2.2(ii) with $\Phi_q\simeq\Z/n_q$
gives (ii), and $E[\ell^t]^{I_q}=E[\ell^t]$ iff $\min(t,v_\ell(n_q))=t$. Reference: SilvermanATAEC V; Chapter 7, 6.2. Paper: Lemma
lem:tamagawa-exp, Section 1.5 ("$t_q=v_\ell(n_q)=t_\ell(E,q)$ whether or not the reduction is split"), Remark rem:ko(2), Theorem thm:qual
(c), Lemma lem:old (the two cases $p\,\|\,N$), the optimal-level paragraph ($N(\bar\rho)$ prime to $q$ iff $\ell\mid n_q$).

**3.4 `prop:galrep:potmult`** (proposition; P given Chapter 10). Let $q\ne\ell$ ($q=2$ allowed) and let $E$ have additive, potentially
multiplicative reduction at $q$ ($v_q(j)<0$). Then there is a ramified quadratic character $\chi$ of $G_{\Q_q}$ such that $E\otimes\chi$ has
multiplicative reduction over $\Q_q$, and $\rho|_{G_{\Q_q}}\simeq\rho'\otimes\chi$ with $\rho'$ of the shape 3.2 for a Tate parameter of valuation
$-v_q(j)$. For $q$ odd one may take $\chi=\chi_q|_{G_{\Q_q}}$; then $E^{(q)}$ has type $\mathrm I_n$, $n=-v_q(j)$, and $E$ has type $\mathrm I_n^*$
(Chapter 10, Lemma lem:twist (ii)). Consequences: $\rho(I_q)=\{\chi(\sigma)\begin{psmallmatrix}1&nt_\ell(\sigma)\\0&1\end{psmallmatrix}\}$ is
$\pm$(unipotent), infinite; $V^{I_q}=0$ ($\delta_q=0$); $\ad V\simeq\ad V'$ as $G_{\Q_q}$-modules, so $(\ad V)^{I_q}$ is a line on which $\Frob_q$
acts by $q$; $\rho\bmod\ell^t$ is ramified at $q$ for every $t\ge1$, while $(\rho\otimes\chi)\bmod\ell^t$ is unramified iff $\ell^t\mid v_q(j)$; the
conductor exponent is $2a(\chi)$: $2$ for $q$ odd, $4$ or $6$ for $q=2$ (Chapter 7, 9.3(ii)). At $q=2$ the index $m$ of the
Kodaira symbol $\mathrm I_m^*$ need not equal $-v_2(j)$, and a symbol $\mathrm I_m^*$ at $2$ can also occur with potentially good reduction
(Definition def:terms; Remark rem:wild; Chapter 10). Reference: SilvermanATAEC V.5 (verify); Chapter 7, 7.6, 9.3. Paper:
Definition def:terms ($t_\ell$ via $v_q(j)$, $\mathrm I_n^*$ at $2$), Lemma lem:euler (type $\mathrm I_n^*$: "$V=V'\otimes\chi_q$ with $V'$ Steinberg"),
Lemma lem:twist (iii) (conductor exponent $2$ of the ramified twist), the proof of Theorem thm:main (the $\mathrm I_n^*$ primes; this
item covers $q=2$, which the paper's argument via Lemma lem:twist does not: important_notes.md point 18), Theorem thm:qual (c),
Remark rem:types.

**3.5 `cor:galrep:delta`** (corollary; P). $\delta_p=\dim V^{I_p}$ is $2$, $1$, $0$ according as $E$ has good, multiplicative or additive
reduction at $p\ne\ell$ (3.1, 3.2; for additive reduction 2.3(ii) and 3.4), and the conductor exponent is
$f_p=2-\delta_p+\operatorname{sw}_p(V)$ (Ogg-Saito: the conductor of Chapter 10 equals the Artin conductor of $V_\ell E$; stated, Chapter 7, 8.4).
Paper: Section 1.1 ("$\delta_p=2,1,0$ for good, multiplicative, additive reduction"), Definition def:terms (naive factor),
Theorem thm:dfg14, Section 4.1 ($M^\Sigma$).
