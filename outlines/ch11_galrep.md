# Chapter 11: Galois representations of elliptic curves (`ch:galrep`, `chapters/ch11_galrep.tex`)

Stage 1 line-up. Part III (Curves and elliptic curves). Target length 2,775 lines of LaTeX (card excluded; see Part 3),
inside the 2,800 lines that PLAN.md Section 7.3 allows for this chapter.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the
Chapter 2 to 9 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference
(book and chapter or section; a theorem number only where the outline author is sure, otherwise the section, and
numbers marked "(verify)" must be checked before they are printed); the paper's use by its `\label` names, or
"background". Every computation quoted below (3-division polynomials, image labels, inertia images per Kodaira type,
Euler factors at 2, congruences, Serre conductors, the structure of the 3Ns curves, the Eisenstein data) was checked
with PARI/GP 2.15 through `cypari2` in `/tmp/ch11` against Cremona's `ecdata` files `allcurves`, `galrep`,
`degphi` for conductors below 10,000 (verification log, Part 6.6).

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
  $E(K)/E_0(K)\simeq\Phi_p(k)$, Kodaira types and Tate's algorithm, the component groups $\Phi_q(\bar\F_q)$ by type,
  conductor exponents and Ogg's formula, the semistable reduction theorem, the Tate curve with its Galois module
  $E_{\mathsf q}[\ell^t]$ (statement), Kraus's semistability defect $12/\gcd(v_q(\Delta),12)$ for $q\ge5$, Lemma lem:twist (i), (ii)
  and Remark rem:wild. **Chapter 11 uses all of these as black boxes with `\Cref{ch:reduction}` and proves the
  representation-theoretic consequences.** If the Chapter 10 outline proves the Galois-theoretic consequences of the
  Tate curve itself (the matrix shape, Lemma lem:tamagawa-exp), Chapter 11 keeps them anyway, because PLAN.md puts
  Lemma lem:tamagawa-exp here; the Chapter 10 writer should then only state them.
* **Chapter 15** proves Galois representations of newforms, local-global compatibility, states the optimal-level theorem in
  general (DDT Theorem 3.15) and proves only its specialisation to $\bar\rho_{E',\ell}$, with the trivial-nebentypus argument
  (important_notes.md B18), Ribet's level lowering, Lemma lem:old and Theorem
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
  $\Phig_q=\Phi_q(\bar\F_q)$ the geometric component group of the Neron model (the paper's macro `\Phig`), $c_q=\#\Phi_q(\F_q)$, which
  divides $\#\Phig_q$; the group scheme $\Phi_q$ is always written with an argument, never as a bare $\Phi_q$ (Appendix B, B-C11(b)).
  Kodaira symbols as in PLAN.md 7.1.
* **C3 (Frobenius).** As in Chapter 7 (L3) and Chapter 9 (C5): $\Frob_p$ is an **arithmetic** Frobenius; $\Frob_p^{-1}$ is
  the geometric one, written $\Frob_p^{-1}$ and never $\Phi_p$ in this chapter, where $\Phi_q(\cdot)$ is the component group (Appendix B,
  B-C2(b)); group-theoretic statements (conjugation, the Tate matrices) use $\Frob_p$; $L$-factors use $\Frob_p^{-1}$
  and are Chapter 19's. On $V_\ell E$ at a good prime the arithmetic Frobenius has characteristic polynomial $X^2-a_pX+p$,
  roots $\alpha,\beta$; the geometric one has $\alpha^{-1},\beta^{-1}$; on $\ad V$ both give $\alpha/\beta,1,\beta/\alpha$
  (important_notes.md B1). The relation on tame inertia is $\Frob\,t\,\Frob^{-1}=t^{q}$. The letter $\Phi$ is used in this chapter
  only for the component group, always with an argument ($\Phi_q(\F_q)$, $\Phi_q(\bar\F_q)$) or as $\Phig_q$; the geometric Frobenius is
  always $\Frob^{-1}$ or $\Frob_q^{-1}$.
* **C4 (characters).** $\chi_\ell$ is the $\ell$-adic cyclotomic character, $\bar\chi_\ell$ its reduction; $\chi_d$ the quadratic
  character of $\Q(\sqrt d)$; $q^*=(-1)^{(q-1)/2}q$ and $\chi_{q^*}$, the quadratic character of conductor $q$ (the paper writes $\chi_q$; the book never does, decision D3); $\ell^*$ likewise. Where $\chi_3$ could
  mean either, write $\chi_3^{\mathrm{cyc}}$ or $\chi_{-3}$ (important_notes.md point 32); $\bar\chi_3=\chi_{-3}$. $\omega=\bar\chi_\ell|_{I_\ell}$ and
  $\omega_2$ are the fundamental characters (5.2).
* **C5 (standard matrices).** As Chapter 1, 6.2 and Chapter 4, C6: $J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ (the paper's $J$; decision D5),
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
one-dimensional torus, and $E/E_0\simeq\Phi_p(k')$ of bounded order (Chapter 10); then $\#E(K^{\mathrm{ur}})[m]\le m\cdot\#\Phi_p(\bar k)$ for $m$ prime to
$p$, contradicting $E[m]\subset E(K^{\mathrm{ur}})$ of order $m^2$ for large $m$. (e), (f): semistable reduction theorem (Chapter 10)
plus (a) to (d) over a finite extension, and the Tate shape 3.2. Reference: Serre-Tate 1968, Section 1, Theorem 1 and
Section 2 (`SerreTate68`, in `refs.bib` by decision B14, see Part 6.5); SilvermanAEC VII.7 (Theorem 7.1, verify). Paper: Section 1.1
($\delta_p$), Lemma lem:tamagawa-exp, Lemma lem:IV ("potentially good", "finite image"), Lemma lem:old ("$\bar\rho_h$ unramified"),
the optimal-level paragraph ("$N(\bar\sigma)$ is prime to every prime at which $\bar\sigma$ is unramified").

**2.2 `lem:galrep:component-invariants`** (lemma; R: proved in Chapter 10, its item 4.5 `prop:reduction:component-invariants`, which this
item restates and cites with `\Cref{ch:reduction}` instead of proving again: important_notes.md B16). Let $q\ne\ell$ be primes, $E/\Q_q$ with bad reduction,
$\Phig_q=\Phi_q(\bar\F_q)$, $k\ge1$. (i) If the reduction is additive, there is a $\Gal(\bar\F_q/\F_q)$-equivariant isomorphism
$$E[\ell^k]^{I_q}\ \simeq\ \Phig_q[\ell^k];$$
in particular $E(\Q_q)[\ell^\infty]\simeq\Phi_q(\F_q)[\ell^\infty]$. (ii) If the reduction is multiplicative, there is an exact sequence of
$\Gal(\bar\F_q/\F_q)$-modules $0\to\mu_{\ell^k}\otimes\varepsilon\to E[\ell^k]^{I_q}\to\Phig_q[\ell^k]\to0$, with $\Phig_q\simeq\Z/n_q$ and $\varepsilon$ the
unramified character of 3.2 (trivial for split reduction). (iii) Consequently, for $\ell$ odd,
$\dim_{\F_\ell}E[\ell]^{I_q}$ is: $1+[\ell\mid n_q]$ for $\mathrm I_{n}$, $n\ge1$; $1$ for $\mathrm{IV}$, $\mathrm{IV}^*$ if $\ell=3$; $0$ for every other additive
type (the orders of $\Phig_q$ for additive types are $1,2,3,4$: Chapter 10). Proof (in Chapter 10, 4.5; recalled here in one paragraph only): for each finite unramified $K'/\Q_q$ with
residue field $k'$: $E(K')/E_0(K')\simeq\Phi_q(k')$ (Neron model and Hensel, Chapter 10), $E_1(K')$ is a $\Z_q$-module, hence uniquely
$\ell$-divisible, and $E_0(K')/E_1(K')\simeq\tilde E_{\mathrm{ns}}(k')$, which is $k'^+$ (additive: uniquely $\ell$-divisible) or $k'^\times$ (split over
large enough $k'$); the snake lemma for multiplication by $\ell^k$, and the union over $K'$, since $E[\ell^k]^{I_q}=E[\ell^k](\Q_q^{\mathrm{ur}})$.
Reference: the argument is the one in Serre-Tate 1968, Section 1; SilvermanAEC VII.6 and VII.7 (verify); ATAEC IV.9 for
$E(K)/E_0(K)\simeq\Phi_q(k)$. Paper: Lemma lem:IV (second proof, 4.3), Remark rem:types ("$E[3]^{I_q}=0$", 4.5), Lemma lem:tamagawa-exp
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
ring are $\ell^t$-th powers (Hensel), so this holds iff $\ell^t\mid v_q(q_E)=n_q$ (Chapter 7, 6.2(v)). Proof 2: 2.2(ii) with $\Phig_q\simeq\Z/n_q$
gives (ii), and $E[\ell^t]^{I_q}=E[\ell^t]$ iff $\min(t,v_\ell(n_q))=t$. Reference: SilvermanATAEC V; Chapter 7, 6.2. Paper: Lemma
lem:tamagawa-exp, Section 1.5 ("$t_q=v_\ell(n_q)=t_\ell(E,q)$ whether or not the reduction is split"), Remark rem:ko(2), Theorem thm:qual
(c), Lemma lem:old (the two cases $p\,\|\,N$), the optimal-level paragraph ($N(\bar\rho)$ prime to $q$ iff $\ell\mid n_q$).

**3.4 `prop:galrep:potmult`** (proposition; P given Chapter 10). Let $q\ne\ell$ ($q=2$ allowed) and let $E$ have additive, potentially
multiplicative reduction at $q$ ($v_q(j)<0$). Then there is a ramified quadratic character $\chi$ of $G_{\Q_q}$ such that $E\otimes\chi$ has
multiplicative reduction over $\Q_q$, and $\rho|_{G_{\Q_q}}\simeq\rho'\otimes\chi$ with $\rho'$ of the shape 3.2 for a Tate parameter of valuation
$-v_q(j)$. For $q$ odd one may take $\chi=\chi_{q^*}|_{G_{\Q_q}}$; then $E^{(q)}$ has type $\mathrm I_n$, $n=-v_q(j)$, and $E$ has type $\mathrm I_n^*$
(Chapter 10, Lemma lem:twist (ii)). Consequences: $\rho(I_q)=\{\chi(\sigma)\begin{psmallmatrix}1&nt_\ell(\sigma)\\0&1\end{psmallmatrix}\}$ is
$\pm$(unipotent), infinite; $V^{I_q}=0$ ($\delta_q=0$); $\ad V\simeq\ad V'$ as $G_{\Q_q}$-modules, so $(\ad V)^{I_q}$ is a line on which $\Frob_q$
acts by $q$; $\rho\bmod\ell^t$ is ramified at $q$ for every $t\ge1$, while $(\rho\otimes\chi)\bmod\ell^t$ is unramified iff $\ell^t\mid v_q(j)$; the
conductor exponent is $2a(\chi)$: $2$ for $q$ odd, $4$ or $6$ for $q=2$ (Chapter 7, 9.3(ii)). At $q=2$ the index $m$ of the
Kodaira symbol $\mathrm I_m^*$ need not equal $-v_2(j)$, and a symbol $\mathrm I_m^*$ at $2$ can also occur with potentially good reduction
(Definition def:terms; Remark rem:wild; Chapter 10). Reference: SilvermanATAEC V.5 (verify); Chapter 7, 7.6, 9.3. Paper:
Definition def:terms ($t_\ell$ via $v_q(j)$, $\mathrm I_n^*$ at $2$), Lemma lem:euler (type $\mathrm I_n^*$: "$V=V'\otimes\chi_{q^*}$ with $V'$ Steinberg"),
Lemma lem:twist (iii) (conductor exponent $2$ of the ramified twist), the proof of Theorem thm:main (the $\mathrm I_n^*$ primes; this
item covers $q=2$, which the paper's argument via Lemma lem:twist does not: important_notes.md point 18), Theorem thm:qual (c),
Remark rem:types.

**3.5 `cor:galrep:delta`** (corollary; P). $\delta_p=\dim V^{I_p}$ is $2$, $1$, $0$ according as $E$ has good, multiplicative or additive
reduction at $p\ne\ell$ (3.1, 3.2; for additive reduction 2.3(ii) and 3.4), and the conductor exponent is
$f_p=2-\delta_p+\operatorname{sw}_p(V)$ (Ogg-Saito: the conductor of Chapter 10 equals the Artin conductor of $V_\ell E$; stated, Chapter 7, 8.4).
Paper: Section 1.1 ("$\delta_p=2,1,0$ for good, multiplicative, additive reduction"), Definition def:terms (naive factor),
Theorem thm:dfg14, Section 4.1 ($M^\Sigma$).

### Section 4. Additive potentially good reduction: the image of inertia by Kodaira type

**4.1 `thm:galrep:additive-shapes`** (theorem; P given Kraus's theorem (Chapter 10, R) and Chapters 4, 6, 7). Let $q\ge5$, $\ell\ne q$,
and let $E$ have additive potentially good reduction at $q$. Then $\rho(I_q)=\langle g\rangle$ is cyclic, $g\in\SL_2(\Zl)$,
and, with $\sigma$ denoting an element with $\sigma^2+\sigma+1=0$ and $\tau$ one with $\tau^2=-1$:

| type | $v_q(\Delta_{\min})$ | $\#\rho(I_q)$ | generator | $(\ad V)^{I_q}$ | action of $\Frob_q$ on $(\ad V)^{I_q}$ |
|-|-|-|-|-|-|
| $\mathrm I_0^*$ | 6 | 2 | $-1$ | $\ad V$ | that of $\ad V_\ell E^{(q)}$ (unramified; eigenvalues $\alpha'/\beta',1,\beta'/\alpha'$) |
| $\mathrm{IV}$, $\mathrm{IV}^*$ | 4, 8 | 3 | $\sigma$ | $\Ql(2\sigma+1)$ | $\chi_{-3}(q)$ |
| $\mathrm{III}$, $\mathrm{III}^*$ | 3, 9 | 4 | $\tau$ | $\Ql\tau$ | $\chi_{-4}(q)$ |
| $\mathrm{II}$, $\mathrm{II}^*$ | 2, 10 | 6 | $-\sigma$ | $\Ql(2\sigma+1)$ | $\chi_{-3}(q)$ |

In every case $V^{I_q}=0$, $f_q=2$ (tame), $\rho(\Frob_q)\,g\,\rho(\Frob_q)^{-1}=g^q$ for every lift, the action on the line is the same for the
arithmetic and the geometric Frobenius, $(2\sigma+1)^2=-3$ ("the line spanned by $\sqrt{-3}$"), and $\End_{I_q}(T)=\Zl[g]\simeq\Zl\otimes\Z[\zeta_3]$
(resp. $\Zl\otimes\Z[i]$), $\End_{I_q}(V)=\Ql\otimes\Q(\zeta_3)$ (resp. $\Ql\otimes\Q(i)$), which is not a field when $\ell\equiv1\pmod3$ (resp. $\pmod4$)
(important_notes.md point 12). For $\mathrm I_0^*$: $\rho\otimes\chi_{q^*}$ is unramified at $q$ and equals $\rho_{E^{(q)},\ell}$, $E^{(q)}$ having good reduction.
For $\mathrm{III}$, $\mathrm{III}^*$ the line is spanned by $\tau$ itself, which is diagonal only over $\Ql(i)$ (important_notes.md point 34). Proof:
order from Kraus (2.3(iv)); cyclic and tame (Chapter 7, 5.6), generated by $g$ with $g^m=1$, $\det g=1$, so $g=-1$, $\sigma$, $\tau$, $-\sigma$ (Chapter
4, 9.3); the commutant and its trace-zero line (Chapter 4, 9.2; Chapter 6, 4.10); $\Frob\,g\,\Frob^{-1}=g^q$ (Chapter 7, 5.6; Chapter 6,
3.12), so conjugation acts on $2\sigma+1$ by $+1$ iff $q\equiv1\pmod3$ ($2\sigma^2+1=-(2\sigma+1)$) and on $\tau$ by $+1$ iff $q\equiv1\pmod4$; the
geometric Frobenius gives the same sign because $q^{-1}\equiv q\pmod{12}$; $\rho|_{I_q}=\chi_{q^*}|_{I_q}$ in the $\mathrm I_0^*$ case because $I_q$ has a
unique character of order $2$. This is the "inertia images and invariants" part of Lemma lem:euler; the factors
$L_q(A_f,s)$ and $e_\ell(E,q)$ are computed from it in Chapter 19 (and the shapes, conductors and $L$-factors of the Weil-Deligne
side are Chapter 7, 9.2, 9.4). Reference: Kraus90; Serre-Tate 1968, Section 2; Chapters 4, 6, 7. Paper: Lemma lem:euler (all
additive rows), Lemma lem:IV, Remark rem:types, the table of Section 1. Verified: for each type, $12$ curves of
conductor below $10{,}000$ with surjective mod $3$ image and a prime $q\ge5$ of that type: the ramification index of $q$ in the
$3$-division field and the existence of an inertia-fixed $3$-torsion point agree with the table and with 4.5 (Part 6.6).

**4.2 `rem:galrep:kraus-from-components`** (remark; P given 2.2 and 2.3, as an exercise). At $q\ge5$ the dictionary "type $\mapsto$
order of $\rho(I_q)$" of 4.1 also follows from the component groups alone: for $g$ of order $m\in\{2,3,4,6\}$ in $\SL_2(\Zl)$, the fixed
spaces of $\bar g$ on $E[2]$ and $E[3]$ are: $m=2$: $E[2]$ and $0$; $m=3$: $0$ and a line; $m=4$: a line and $0$; $m=6$: $0$ and $0$ (reduce $g$
modulo $2$ and $3$; $\tau\not\equiv1\pmod2$ because $(1+2X)^2=-1$ has no solution in $M_2(\Z_2)$). Comparing with $\Phig_q[2]$, $\Phig_q[3]$ via 2.2 and
the independence of $\ell$ in 2.3(i) gives $\mathrm I_0^*\mapsto2$ ($\Phig_q[2]=(\Z/2)^2$), $\mathrm{IV},\mathrm{IV}^*\mapsto3$, $\mathrm{III},\mathrm{III}^*\mapsto4$, $\mathrm{II},\mathrm{II}^*\mapsto6$.
This is a second route to Kraus's table that uses only the component groups; present it as Exercise 7, not as the proof.
Paper: background for Lemma lem:IV and Remark rem:types.

**4.3 `lem:galrep:IV`** (lemma, the paper's Lemma lem:IV; P, two proofs). Let $q\ge5$ be a prime at which $E$ has type $\mathrm{IV}$ or
$\mathrm{IV}^*$. Then the image of $I_q$ in $\Aut(T_3E)$ is cyclic of order $3$, its image in $\Aut(E[3])$ is a nontrivial unipotent
subgroup, $E[3]^{I_q}$ is a line, $\bar\rho_{E,3}$ is tamely ramified at $q$, and the Serre conductor of $\bar\rho_{E,3}$ has exponent $1$ at $q$.
Proof A (the paper's, every step expanded): Kraus gives order $3$ (2.3(iv)); tame as $3\ne q$, hence cyclic, generated by $\sigma$ with
$\det\sigma=\chi_3^{\mathrm{cyc}}(\sigma)=1$ ($I_q$ fixes $\mu_3$), so by Cayley-Hamilton $\sigma^2+\sigma+1=0$ on $T$; $T$ is a module over
$\Z_3[X]/(X^2+X+1)\simeq\Z_3[\zeta_3]$ with $X$ acting as $\sigma$ (important_notes.md point 13), a DVR with uniformiser $\pi=1-\zeta_3$, residue
field $\F_3$ (Chapter 6, 4.7); torsion-free of $\Z_3$-rank $2$, hence free of rank one (Chapter 6, 4.8); $E[3]=T/3T\simeq\Z_3[\zeta_3]/(\pi^2)$
with $\sigma-1$ acting as $-\pi$, nonzero with square zero: a nontrivial unipotent with fixed line $\pi\Z_3[\zeta_3]/(\pi^2)$; Serre
exponent $\dim E[3]-\dim E[3]^{I_q}+\operatorname{sw}=2-1+0=1$. Proof B (component groups; works for every prime $q\ne3$): $E[3]^{I_q}\simeq\Phig_q[3]=\Z/3$
(2.2(i)) is a line; $I_q$ acts nontrivially on $E[3]$ (otherwise $\Phig_q[3]\supseteq(\Z/3)^2$); the elements of $\SL_2(\F_3)$ fixing a
nonzero vector form a group $\mathrm U$ of order $3$ (Chapter 1, 5.6), so $\bar\rho(I_q)=\mathrm U$; $\rho(I_q)$ is finite (potentially good: types
$\mathrm{IV}$, $\mathrm{IV}^*$ have $v_q(j)\ge0$, Chapter 10) and injects into $\GL_2(\F_3)$ (2.3(ii)), so $\rho(I_q)$ is cyclic of order $3$, tame. Reference:
Kraus90; Chapter 6, 4.7, 4.8; Chapter 4, 9.4. Paper: Lemma lem:IV; Theorem thm:qual (a), (b) ("By Lemma lem:IV the Serre
conductor $M=N(\bar\rho)$ has exponent exactly $1$ at $q$, so $M\mid N/q$"). Example: 121c1 (type $\mathrm{IV}$ at $11$) has
$N(\bar\rho_{121c1,3})=11$ and $\bar\rho_{121c1,3}\simeq\bar\rho_{11a1,3}$ (6.3).

**4.4 `prop:galrep:IV-at-2`** (proposition; P; new, settles important_notes.md point 43). Let $E/\Q$ have Kodaira type $\mathrm{IV}$ or
$\mathrm{IV}^*$ at $2$. Then: (i) for every odd prime $\ell$, $\rho_{E,\ell}(I_2)$ is cyclic of order $3$, hence tamely ramified, and
$E[3]^{I_2}$ is a line; (ii) $f_2(E)=2$, i.e. $4\,\|\,N$, and $v_2(\Delta_{\min})=4$ (type $\mathrm{IV}$) or $8$ (type $\mathrm{IV}^*$), by Ogg's formula;
(iii) the Serre conductor of $\bar\rho_{E,3}$ has exponent $1$ at $2$; (iv) $(\ad V)^{I_2}=\Ql(2\sigma+1)$ and $\Frob_2$ acts on it by
$\chi_{-3}(2)=-1$ (it inverts $\sigma$ since $2\equiv-1\pmod3$), so $L_2(A_f,s)^{-1}=1+2^{-s}$, $L_2(\Sym f,s)^{-1}=1+2\cdot2^{-s}$, i.e.
$P_2(X)=1+2X$, and $e_\ell(E,2)=v_\ell(1+\tfrac12)=v_\ell(3/2)$, which is $1$ for $\ell=3$ and $0$ for $\ell\ge5$. Proof: Proof B of 4.3 at
$q=2$ gives (i) for $\ell=3$; 2.3(i) transfers the group to every odd $\ell$; (ii) $f_2=\operatorname{codim}V^{I_2}+\operatorname{sw}=2+0$ and Ogg
$f=v(\Delta)+1-m$ with $m=3$, $7$ components; (iii) as in 4.3; (iv) as in 4.1, the order-$3$ image being a quotient of tame inertia on
which $\Frob_2$ acts by squaring (Chapter 7, 5.4, 5.6), and Chapter 19's normalisation $L_2(\Sym f,s)=L_2(A_f,s-1)$. Consequences for
the paper: the case excepted in Proposition prop:forms ($\ell=3$, type $\mathrm{IV}$ or $\mathrm{IV}^*$ at $2$) is covered, so (eq:main) and
(eq:twist) hold under the hypothesis of Theorem thm:main with no exception; "PARI's factor at $2$ is $1+2X$ for every one of them"
and the value $e_3=1$ of Remark rem:wild are theorems; and the argument of Theorem thm:qual (a) applies verbatim at $q=2$ (with
$3\nmid N$), the Serre conductor having exponent $1$ at $2$ while $4\,\|\,N$. Verified: all $4{,}750$ curves of conductor below $10{,}000$
with type $\mathrm{IV}$ ($2{,}094$) or $\mathrm{IV}^*$ ($2{,}656$) at $2$ have $\bar\rho_{E,3}(I_2)$ of order $3$ with a fixed line, $f_2=2$, $v_2(\Delta_{\min})=4$,
resp. $8$, and $v_2(j)\ge0$; $60$ of them sampled with `lfunsympow`: $P_2(X)=1+2X$ every time. Reference: Chapter 10 (types, Ogg),
2.2, 2.3. Paper: Proposition prop:forms, Remark rem:wild, Section sec:wild, Theorem thm:qual (a), Definition def:terms.

**4.5 `prop:galrep:mod3-inertia`** (proposition and table; P; the paper's Remark rem:types in corrected, complete form). Let $q\ge5$
and $\ell=3$. The image $\bar\rho_{E,3}(I_q)$, the fixed space, the Serre exponent $a_q(\bar\rho_{E,3})$ and the effect of the twist by $\chi_{q^*}$
(which exchanges the types as in Lemma lem:twist (ii), Chapter 10) are:

| type at $q$ | $\bar\rho(I_q)$ generated by | order | $\dim E[3]^{I_q}$ | $a_q(\bar\rho_{E,3})$ | $f_q(E)$ | $a_q(\bar\rho_{E^{(q)},3})$ |
|-|-|-|-|-|-|-|
| $\mathrm I_0$ | $1$ | 1 | 2 | 0 | 0 | 2 |
| $\mathrm I_n$, $3\nmid n$ | unipotent $\ne1$ | 3 | 1 | 1 | 1 | 2 |
| $\mathrm I_n$, $3\mid n$ | $1$ | 1 | 2 | 0 | 1 | 2 |
| $\mathrm I_n^*$, $3\nmid n$ | $-$(unipotent $\ne1$) | 6 | 0 | 2 | 2 | 1 |
| $\mathrm I_n^*$, $3\mid n$ | $-1$ | 2 | 0 | 2 | 2 | 0 |
| $\mathrm I_0^*$ | $-1$ | 2 | 0 | 2 | 2 | 0 |
| $\mathrm{II}$, $\mathrm{II}^*$ | $-$(unipotent $\ne1$) | 6 | 0 | 2 | 2 | 1 |
| $\mathrm{III}$, $\mathrm{III}^*$ | $\bar\tau$, $\bar\tau^2=-1$ ($X^2+1$ irreducible over $\F_3$) | 4 | 0 | 2 | 2 | 2 |
| $\mathrm{IV}$, $\mathrm{IV}^*$ | unipotent $\ne1$ | 3 | 1 | 1 | 2 | 2 |

So: (a) $E[3]^{I_q}=0$ and $a_q(\bar\rho_{E,3})=2=f_q$ for **every** additive type other than $\mathrm{IV}$, $\mathrm{IV}^*$ (including $\mathrm I_0^*$, $\mathrm{III}$,
$\mathrm{III}^*$), and the vanishing of $E[3]^{I_q}$ holds also at $q=2$ (2.2); (b) the twist by $\chi_{q^*}$ lowers the Serre exponent of $\bar\rho_{E,3}$
exactly for $\mathrm{II}$, $\mathrm{II}^*$, $\mathrm I_n^*$ and $\mathrm I_0^*$, and lowers the conductor exponent of $E$ itself exactly for $\mathrm I_n^*$ and $\mathrm I_0^*$
($\mathrm{II}\leftrightarrow\mathrm{IV}^*$ keeps $f_q=2$). The paper's remark lists (a) only for "the last two cases" ($\mathrm{II}$, $\mathrm{II}^*$, $\mathrm I_n^*$) and
omits $\mathrm I_0^*$ from (b); its phrase "lowers the conductor exponent" is right for $\bar\rho_{E,3}$, not for $E$, in the $\mathrm{II}$ case
(important_notes.md point 22). For $\ell\ge5$ ($q\ge5$, $q\ne\ell$): every additive type has $E[\ell]^{I_q}=0$ and $a_q(\bar\rho_{E,\ell})=2$, and
$\mathrm I_n$ has exponent $0$ or $1$ according as $\ell\mid n$ or not. Proof: reduce the generators of 4.1, 3.2, 3.4 modulo $3$ (Chapter 4, 9.4;
reduction is injective on finite subgroups, and a unipotent $\begin{psmallmatrix}1&n\\0&1\end{psmallmatrix}$ is trivial mod $3$ iff $3\mid n$); or
read $\dim E[3]^{I_q}$ off 2.2; exponents from 6.2. Verified on samples of every row (Part 6.6). Paper: Remark rem:types, Theorem
thm:qual (why only (a), (b), (c)), Lemma lem:IV, the optimal-level paragraph.

**4.6 `rem:galrep:wild-inertia`** (remark; R/S). At $q=2,3$ the type does not determine $\rho(I_q)$ (2.3(iii)): at $q=2$ the image can be
$Q_8$ or $\SL_2(\F_3)$ (wild, absolutely irreducible, so $(\ad V)^{I_2}=0$ and the factor is $1$), cyclic of order $4$ or $6$ with a wild
part, or cyclic of order $3$ (only for types $\mathrm{IV}$, $\mathrm{IV}^*$, by 4.4; the converse need not hold); at $q=3$ an image of order $3$
is wild. What survives at every $q\ne\ell$: 2.2 ($E[\ell]^{I_q}\simeq\Phig_q[\ell]$ for additive reduction) and 6.2. Observed at $q=2$ (conductor
below $10{,}000$, samples of $40$ per type, surjective mod $3$ image): for $\mathrm{II}$, $\mathrm{II}^*$, $\mathrm{III}$, $\mathrm{III}^*$, $\mathrm I_0^*$ and
potentially good $\mathrm I_m^*$ the least common multiple of the ramification indices of $2$ in the fields of definition of the
$3$-torsion points is $2$, $4$, $6$ or $8$ (image of order $2$, $4$, $6$, or $8$ or $24$); always $E[3]^{I_2}=0$. The Euler factors at $2$ and $3$ are PARI's (Chapter 19, 22); Remark rem:wild itself is Chapter 10's.
Paper: Remark rem:wild, Section sec:wild, Definition def:terms ($\mathrm I_n^*$ at $2$).

### Section 5. The representation at $\ell$ when $E$ has good reduction at $\ell$

**5.1 `thm:galrep:good-at-l`** (theorem; P for (i) given Chapter 10, R for (ii), (iii)). Let $\ell\nmid N$. (i) For every $k$, $E[\ell^k]$ is
the generic fibre of the finite flat group scheme $\mathcal E[\ell^k]$ over $\Zl$ ($\mathcal E$ the Neron model, an elliptic curve over
$\Zl$); so $\bar\rho|_{D_\ell}$ is "finite" (flat), "good" in the sense of DDT Theorem 3.15. (ii) $V_\ell E|_{G_{\Q_\ell}}$ is crystalline with
Hodge-Tate weights $0$ and $1$, and the crystalline Frobenius on $D_{\mathrm{cris}}$ has characteristic polynomial $X^2-a_\ell X+\ell$ (Fontaine;
see Berger's survey; Chapter 18 uses this). (iii) The Serre weight of $\bar\rho_{E,\ell}$ (when irreducible) is $2$ (Serre87, Section
2, verify; Edixhoven92). If $E$ has multiplicative reduction at $\ell$ the weight is $2$ or $\ell+1$ according as $\ell\mid v_\ell(\Delta)$ or not
(stated for orientation only; the paper never needs $\ell\mid N$ in a proof). Reference: SilvermanAEC VII; Serre87; Edixhoven92;
Berger. Paper: the optimal-level paragraph ("the restriction to $D_\ell$ comes from the finite flat group scheme $E'[\ell]$ and is
good"), Theorem thm:main (crystalline at $\ell$, through DFG04; Chapter 18).

**5.2 `def:galrep:fundamental-characters`** (definition and proposition; P given Chapter 7, 5.3). The tame inertia $I_\ell^{\mathrm t}$ of
$\Q_\ell$; $\omega=\omega_1\colon I_\ell\to\mu_{\ell-1}\subset\F_\ell^\times$, $\sigma\mapsto\sigma(\ell^{1/(\ell-1)})/\ell^{1/(\ell-1)}\bmod\mathfrak m$, equal to $\bar\chi_\ell|_{I_\ell}$; $\omega_2\colon I_\ell\to\F_{\ell^2}^\times$,
$\sigma\mapsto\sigma(\ell^{1/(\ell^2-1)})/\ell^{1/(\ell^2-1)}\bmod\mathfrak m$, of order $\ell^2-1$, with $\omega_2^{\ell+1}=\omega$; conjugation by $\Frob_\ell$ sends $\omega_2$ to
$\omega_2^\ell$, so $\omega_2$ does not extend to $G_{\Q_\ell}$, and $\Ind_{G_{\Q_{\ell^2}}}^{G_{\Q_\ell}}$ of an extension of $\omega_2$ is irreducible. Reference: Serre72,
Section 1 (fundamental characters; verify the numbering). Paper: Lemma lem:old (case $p=\ell$, "the restriction to $D_\ell$
irreducible").

**5.3 `thm:galrep:deligne-fontaine`** (theorem; S for $E$, R in general). Let $\ell$ be odd and $\ell\nmid N$. (i) If $\ell\nmid a_\ell$ (ordinary):
$$\bar\rho|_{D_\ell}\simeq\begin{pmatrix}\bar\chi_\ell\,\mu(a_\ell^{-1})&*\\0&\mu(a_\ell)\end{pmatrix},\qquad\bar\rho|_{I_\ell}\simeq\begin{pmatrix}\omega&*\\0&1\end{pmatrix},$$
where $\mu(x)$ is the unramified character with $\Frob_\ell\mapsto x\bmod\ell$ (connected-etale sequence of $\mathcal E[\ell]$: the etale quotient is
$\tilde E[\ell]$, on which $\Frob_\ell$ acts by the unit root of $X^2-a_\ell X+\ell$, congruent to $a_\ell$). (ii) If $\ell\mid a_\ell$ (supersingular; then
$a_\ell=0$ for $\ell\ge5$ by Hasse): $\bar\rho|_{I_\ell}\otimes\F_{\ell^2}\simeq\omega_2\oplus\omega_2^\ell$ and $\bar\rho|_{D_\ell}$ is irreducible (Serre72, Section 1,
the formal group of height $2$; verify the proposition number). (iii) Hence $a_\ell\bmod\ell$ is determined by $\bar\rho|_{D_\ell}$: it is $0$ if
$\bar\rho|_{D_\ell}$ is irreducible, and otherwise it is the eigenvalue of $\Frob_\ell$ on the unique unramified one-dimensional quotient
(unique because $\omega\ne1$ for $\ell$ odd). The same holds for a newform $h$ of weight $2$, level prime to $\ell$, coefficients in $\mathcal O$,
with $a_\ell(h)\bmod\lambda$ (Deligne in the ordinary case, Fontaine in the supersingular case; Edixhoven92, Section 2, as cited by the
paper; the newform version is Chapter 15's). Reference: Serre72, Section 1; Edixhoven92, Section 2. Paper: Lemma lem:old (case
$p=\ell$: "the residue class of $a_\ell$ is determined by the restriction to $D_\ell$"). Example: $a_3(121\mathrm{c}1)=2\equiv-1=a_3(11\mathrm a1)\pmod3$,
both ordinary at $3$, as $\bar\rho_{121c1,3}\simeq\bar\rho_{11a1,3}$ requires.

**5.4 `cor:galrep:ordinary`** (corollary; P given 5.3). Let $\ell$ be odd and $\ell\nmid N$. (i) If $\bar\rho_{E,\ell}$ is reducible, $E$ is ordinary at
$\ell$ and the two characters of $\bar\rho^{\mathrm{ss}}$ restrict to $I_\ell$ as $\omega$ and $1$. (ii) If $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$, then $\ell=3$ and $E$
is ordinary at $3$. Proof of (ii): $\chi_{\ell^*}|_{I_\ell}=\omega^{(\ell-1)/2}$ (Chapter 5, galois:sqrt-lstar); in the ordinary case
$\{\omega,1\}=\{\omega^{(\ell+1)/2},\omega^{(\ell-1)/2}\}$ as multisets of characters of $I_\ell$ forces $\omega^{(\ell+1)/2}=1$, i.e. $\ell-1\mid(\ell+1)/2$, i.e. $\ell=3$;
in the supersingular case $\omega^{(\ell-1)/2}=\omega_2^{(\ell^2-1)/2}=-1$ and $\{\omega_2,\omega_2^\ell\}=\{-\omega_2,-\omega_2^\ell\}$ would need $\omega_2^{\ell-1}=-1$, i.e.
$\ell+1\mid(\ell-1)/2$, impossible. Verified: every curve of conductor below $10{,}000$ with a Borel or split Cartan label at
$\ell\in\{3,5,7,13,37\}$, $\ell\nmid N$, has $\ell\nmid a_\ell$ ($4{,}571$ pairs); the $62$ curves with image 3Ns and $3\nmid N$ all have $3\nmid a_3$.
Paper: Section sec:eis (background), the hypothesis of Theorem thm:main (8.2, 8.6).

### Section 6. Conductors of mod $\ell$ representations

**6.1 `def:galrep:serre-conductor`** (definition and proposition; P). For a continuous $\bar\sigma\colon G_\Q\to\GL_n(\bar\F_\ell)$ and $p\ne\ell$: the
Artin exponent $a_p(\bar\sigma)=\dim\bar\sigma-\dim\bar\sigma^{I_p}+\operatorname{sw}_p(\bar\sigma)$ (the definitions of Chapter 7, 8.3(v), applied to the finite
image), and the Serre conductor $N(\bar\sigma)=\prod_{p\ne\ell}p^{a_p(\bar\sigma)}$, prime to $\ell$ by definition. Properties: $a_p=0$ iff $\bar\sigma$ is
unramified at $p$ (so $N(\bar\sigma)$ is prime to every prime at which $\bar\sigma$ is unramified); invariant under extension of scalars
and under twisting by characters unramified at $p$; additive in short exact sequences only for the $\operatorname{sw}$ part.
Serre weight $k(\bar\sigma)$: definition by reference (Serre87, Section 2; Edixhoven92). Reference: Serre87, Section 1.2
(verify). Paper: the optimal-level paragraph ("$N(\bar\sigma)$ is the Serre conductor"), Lemma lem:IV, Remark rem:types,
Theorem thm:qual.

**6.2 `prop:galrep:serre-conductor-E`** (proposition; P given 2.2, 3.3, 3.5 and Ogg-Saito). Let $p\ne\ell$. Then
$$a_p(\bar\rho_{E,\ell})=f_p(E)-\dim_{\F_\ell}\Phi_p(\bar\F_p)[\ell].$$
Hence $N(\bar\rho_{E,\ell})$ divides the prime-to-$\ell$ part of $N$, with $v_p(N(\bar\rho))=v_p(N)$ unless $\ell\mid\#\Phi_p(\bar\F_p)$; explicitly: $0$ at good
$p$; $0$ or $1$ at multiplicative $p$ according as $\ell\mid n_p$ or not; at additive $p$ and $\ell$ odd, $f_p-1$ if $\ell=3$ and the type is $\mathrm{IV}$
or $\mathrm{IV}^*$, and $f_p$ otherwise; in particular $\bar\rho_{E,\ell}$ ($\ell$ odd) is ramified at every additive prime $p\ne\ell$. Proof: the wild
inertia $P_p$ acts on $T$ through a finite $p$-group (Chapter 7, 5.7), of order prime to $\ell$, so the fixed spaces of its ramification
subgroups commute with reduction (Chapter 4, 3.2(ii)) and $\operatorname{sw}_p(\bar\rho)=\operatorname{sw}_p(V)$; then $f_p=2-\delta_p+\operatorname{sw}_p(V)$ (3.5) and
$\dim E[\ell]^{I_p}=\delta_p+\dim\Phig_p[\ell]$ (2.2, 3.3). Reference: Carayol89 (divisibility, for modular forms); Livne 1989, "On the
conductors of mod $\ell$ Galois representations coming from modular forms", J. Number Theory 31 (add to `bib/ch11.bib` after
checking); Serre87, Section 4 (examples for elliptic curves; verify). Paper: the optimal-level paragraph ("$N(\bar\rho_{E',\ell})$ divides
the conductor of $E'$ [Carayol89]"), Theorem thm:qual (a), (b), (c) (the level $M$), Lemma lem:IV, Remark rem:types, Lemma
lem:old (hypothesis "$p\nmid M$ for every $p\,\|\,N$ at which $\bar\rho$ is unramified").

**6.3 `ex:galrep:serre-conductor-examples`** (worked example; P, all data recomputed). $\ell=3$: 11a1 ($\mathrm I_5$): $N(\bar\rho)=11$. 121c1
($\mathrm{IV}$ at $11$, $f_{11}=2$): $N(\bar\rho)=11$, and $a_p(121\mathrm c1)\equiv a_p(11\mathrm a1)\pmod3$ for all $p<2000$, $p\ne3,11$: $\bar\rho_{121c1,3}\simeq\bar\rho_{11a1,3}$. 121a1
($\mathrm{II}$ at $11$): $N(\bar\rho)=121$; its twist by $\chi_{-11}$ is 121c2 ($\mathrm{IV}^*$): $N=11$; $a_p(121\mathrm a1)\equiv\chi_{-11}(p)a_p(11\mathrm a1)\pmod3$ ($p<2000$). 77c1
($\mathrm I_3$ at $7$, $\mathrm I_2$ at $11$): $N(\bar\rho)=11$, $\bar\rho_{77c1,3}\simeq\bar\rho_{11a1,3}$ ($p<2000$). 539c1 ($\mathrm I_3^*$ at $7$): $v_7(N(\bar\rho))=2$; twist by $\chi_{-7}$
gives 77c1. 726a1 ($\mathrm I_6$ at $2$, $\mathrm I_3$ at $3=\ell$, $\mathrm{III}$ at $11$): $N(\bar\rho)=11^2$. 6912d1 ($\mathrm{III}$ at $2$ with $f_2=8$, $\mathrm{II}$ at $3=\ell$):
$N(\bar\rho)=2^8$. $\ell=5$: 11a1: $N(\bar\rho_{11a1,5})=1$ ($5\mid n_{11}$; $E[5]\simeq\Z/5\oplus\mu_5$). 980i1 ($\mathrm{IV}^*$ at $2$, $\mathrm I_1$ at $5=\ell$, $\mathrm I_5^*$ at $7$): twist by
$\chi_{-7}$ is 140b1 ($\mathrm I_5$ at $7$), $N(\bar\rho_{140b1,5})=4$, and $a_p(140\mathrm b1)\equiv a_p(20\mathrm a1)$, $a_p(980\mathrm i1)\equiv\chi_{-7}(p)a_p(20\mathrm a1)\pmod5$
($p<1224$, $p\ne2,5,7$); but $5\mid N$ here, so this
illustrates the mechanism, not Theorem thm:qual (important_notes.md point 21). Paper: the Example of Section 3, Theorem
thm:qual.

### Section 7. The images of $\bar\rho_{E,\ell}$

**7.1 `thm:galrep:open-image`** (theorem; R). (i) (Serre) If $E/\Q$ has no CM, $\rho_{E,\ell}(G_\Q)$ is open in $\GL_2(\Zl)$ for every $\ell$, and
$\bar\rho_{E,\ell}$ is surjective for all but finitely many $\ell$. (ii) If $E$ has CM by an order in $K$ and $\ell$ is unramified in $K$, the
image of $\bar\rho_{E,\ell}$ lies in the normaliser of a Cartan subgroup, split or nonsplit according as $\ell$ splits or is inert in
$K$, and is not contained in the Cartan subgroup itself. (iii) (Mazur, Chapter 9, 9.6) A Borel image occurs only for
$\ell\in\{2,3,5,7,11,13,17,19,37,43,67,163\}$. (iv) Whether $\ell>37$ forces surjectivity for non-CM $E$ (Serre's uniformity question) is
open; say so in one sentence without further claims. Reference: Serre72 (cite sections; the main theorem numbers to be
verified); Mazur78. Paper: background for Proposition prop:ns ("without complex multiplication"), Section sec:data ("the
images of the mod $\ell$ Galois representations"), Conjecture conj:eis.

**7.2 `prop:galrep:image-constraints`** (proposition; P from Chapter 1, 5.10 and 1.1). Let $\ell$ be odd and $H=\bar\rho_{E,\ell}(G_\Q)$. Then
$\det H=\F_\ell^\times$ and $H$ contains an element conjugate to $\operatorname{diag}(1,-1)$. Hence $H\not\subset\SL_2(\F_\ell)$, $H\not\subset C_{ns}(\F_\ell)$ (the only
involution of $C_{ns}(\F_\ell)\simeq\F_{\ell^2}^\times$ is $-1$, of determinant $1$), and by Dickson either $H=\GL_2(\F_\ell)$ (if $\ell\mid\#H$ and $H$ is not in a
Borel subgroup: then $H\supseteq\SL_2(\F_\ell)$ and $\det H=\F_\ell^\times$), or $H$ lies in a Borel subgroup ($\bar\rho$ reducible), or in the normaliser
of a split or nonsplit Cartan subgroup but not in the Cartan subgroup when $\bar\rho$ is irreducible, or $H$ has exceptional
projective image $A_4$, $S_4$ or $A_5$. Do not call $N_s$ maximal: $N_s(\F_3)\subset N_{ns}(\F_3)$ and $N_s(\F_5)$ lies in a subgroup with projective
image $S_4$ (important_notes.md point 2). Paper: Proposition prop:ns (first step), background.

**7.3 `thm:galrep:mod3-images`** (theorem and table; P for the list, data for occurrence). For **every** $E/\Q$, CM or not, the image
$H=\bar\rho_{E,3}(G_\Q)$ is conjugate to exactly one of the eight subgroups below; in particular never to $C_{ns}(\F_3)$ (3Cn) or to a
subgroup of $\SL_2(\F_3)$. Proof: $H$ has surjective determinant and contains an element of determinant $-1$ and trace $0$ (7.2); by
Chapter 1, 6.10 and 6.9 the subgroups of $\GL_2(\F_3)$ with surjective determinant fall into nine conjugacy classes, and exactly
one of them, $C_{ns}(\F_3)$, has no such element. The orbit pattern on the four lines is the factorisation pattern of $\psi_3$ (Chapter
9, 4.5; Chapter 5, galois:quartic-on-lines). Occurrence: the examples. Counts: curves of conductor below $10{,}000$ in `ecdata`
($64{,}687$ curves; "CM" are the $462$ CM curves, for which `ecdata`'s `galrep` file lists no label when the image is the one
forced by CM; those were classified here from $\psi_3$):

| label | order | $H$ (Chapter 1 models) | arithmetic meaning | $\psi_3$ over $\Q$ | $\Gal(\psi_3)$ | non-CM | CM | example |
|-|-|-|-|-|-|-|-|-|
| (surjective) | 48 | $\GL_2(\F_3)$ | generic | irreducible | $S_4$ | 53,760 | 0 | 11a1 |
| 3Nn | 16 | $N_{ns}(\F_3)$ | irreducible, $\bar\rho\simeq\bar\rho\otimes\chi_K$, $K\ne\Q(\sqrt{-3})$ | irreducible | $D_4$ | 218 | 184 | 245a1 |
| 3Ns | 8 | $N_s(\F_3)$ | irreducible, $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ | two quadratics | $V_4$ | 120 | 26 | 726a1, 338d1, 6912d1 |
| 3B | 12 | $\mathrm B(\F_3)$ | stable line, character $\ne1,\chi_{-3}$ | linear times cubic | $S_3$ | 4,072 | (154 unlabelled Borel) | 50b1, 539a1 |
| 3B.1.1 | 6 | $\begin{psmallmatrix}1&*\\0&*\end{psmallmatrix}$ | rational point of order $3$, $E[3]$ non-split | linear times cubic | $S_3$ | 2,772 | 39 | 20a1, 14a4 |
| 3B.1.2 | 6 | $\begin{psmallmatrix}*&*\\0&1\end{psmallmatrix}$ | $\mu_3\subset E[3]$, $E[3]/\mu_3\simeq\Z/3$, non-split | linear times cubic | $S_3$ | 2,772 | 39 | 20a3, 14a3 |
| 3Cs | 4 | $C_s(\F_3)$ | $E[3]\simeq\psi\oplus\psi\chi_{-3}$, $\psi$ quadratic $\ne1,\chi_{-3}$ | two linear times quadratic | $C_2$ | 249 | 18 | 539a2, 98a3 |
| 3Cs.1.1 | 2 | $\{\operatorname{diag}(1,\pm1)\}$ | $E[3]\simeq\Z/3\oplus\mu_3$ | two linear times quadratic | $C_2$ | 262 | 2 | 14a1, 19a1, 26a1 |

(The CM column: $26$ curves with $j=-32768$ or $8000$ give 3Ns, $184$ give 3Nn, $154$ with $j\in\{0,54000,-12288000\}$ have an unlabelled Borel
image, and the CM curves with labels are counted in their rows.) Remarks to make: 3B.1.1 and 3B.1.2 are exchanged by
$3$-isogeny and by the twist by $\chi_{-3}$ (1.3), and occur in equal numbers; the curves with a rational point of order $3$ are exactly
those labelled 3B.1.1 or 3Cs.1.1 ($2{,}811+264$, a data check of the labels); 3Cs.1.1 is **not** the split Cartan subgroup but its
subgroup of order $2$ (important_notes.md point 44); $N_s(\F_3)\subset N_{ns}(\F_3)$ (point 2); 3Nn is also dihedral (induced from the field
cut out by $\bar\rho^{-1}(C_{ns})$), which is why the hypothesis of Theorem thm:main excludes "induced from $\Q(\sqrt{-3})$", not
"dihedral" (Chapter 4, 8.3). Reference: Chapter 1; Zywina15 (the list for non-CM curves; the book proves it directly);
Sutherland16 (labels). Paper: Proposition prop:ns, Section sec:anomaly, Section sec:eis, Conjecture conj:eis, Section sec:data,
the appendix (`ns3`).

**7.4 `conv:galrep:labels`** (convention; R for the general scheme, data for the check). Sutherland's label of a subgroup of
$\GL_2(\F_\ell)$: $\ell$, then the type of the smallest standard overgroup ($\mathrm B$, $\mathrm{Cs}$, $\mathrm{Cn}$, $\mathrm{Ns}$, $\mathrm{Nn}$, or the
exceptional $\mathrm{A4}$, $\mathrm{S4}$, $\mathrm{A5}$), then optional numerical suffixes identifying the subgroup; surjective images carry no
label. Give the general rule by reference only (Sutherland16, Section 6; verify), and use the intrinsic descriptions of 7.3 in
every statement (important_notes.md point 3: the labels were checked here against `ecdata`, which uses Sutherland's labels:
3B.1.1 is exactly the rational-$3$-torsion case, 3B.1.2 its isogenous partner, 3Cs.1.1 the case $E[3]\simeq\Z/3\oplus\mu_3$, 3Ns the $2+2$
factorisation, 3Nn the irreducible $\psi_3$ with group $D_4$; and 5B.1.1 for 11a3, torsion $\Z/5$, 5B.1.2 for 11a2, 5Cs.1.1 for 11a1,
$E[5]\simeq\Z/5\oplus\mu_5$). Labels occurring at $\ell=5,7,11,13$ for conductor below $10{,}000$ (from `galrep`; the writer may print this as a
table): $\ell=5$: 5B, 5B.1.1, 5B.1.2, 5B.1.3, 5B.1.4, 5B.4.1, 5B.4.2, 5Cs.1.1, 5Cs.1.3, 5Cs.4.1, 5Nn, 5Ns, 5Ns.2.1, 5S4; $\ell=7$: 7B,
7B.1.1 to 7B.1.6, 7B.2.1, 7B.2.3, 7B.6.1 to 7B.6.3, 7Ns, 7Ns.2.1, 7Ns.3.1, 7Ns.6.1.2; $\ell=11$: 11B.1.3 to 11B.1.8, 11B.10.3 to 11B.10.5,
11Nn.1.4; $\ell=13$: 13B, 13B.3.1, 13B.3.2, 13B.4.1, 13B.4.2, 13B.5.1, 13B.5.2, 13Ns.5.1.4. Paper: Section sec:anomaly (3Ns), Section sec:eis
(3Cs.1.1, 3B.1.1), Section sec:data.

**7.5 `thm:galrep:zywina`** (theorem; R). For non-CM $E/\Q$ and $\ell\in\{2,3,5,7,11,13\}$, Zywina15 lists the subgroups of $\GL_2(\F_\ell)$ that
occur as $\bar\rho_{E,\ell}(G_\Q)$, up to conjugacy, together with the corresponding families of $j$-invariants (for $\ell=13$ the
list depended on rational points of certain modular curves; say only that later work settled them, without a reference
unless one is checked). The book needs only $\ell=3$, which 7.3 proves. Reference: Zywina15, Section 1 (theorem numbers not
checked, important_notes.md point 4). Paper: Proposition prop:ns (the citation of Zywina15), Section sec:data.

**7.6 `rem:galrep:computing-images`** (remark; S). How images are computed: (a) $\ell=3$: factor $\psi_3$ (PARI `elldivpol(E,3)`,
`factor`), compute $\Gal(\psi_3)$ (`polgalois`) and the $3$-torsion (`elltors`); 7.3 then determines the image (the appendix's `ns3`
tests the $2+2$ pattern, which detects $N_s(\F_3)$ exactly when $E[3]$ is irreducible); (b) in general, characteristic polynomials of
$\bar\rho(\Frob_p)$ modulo $\ell$ for many $p$ and Chebotarev statistics (Sutherland's algorithm, R: Sutherland16), division
polynomials, and Zywina's $j$-invariant families; (c) the `galrep` files of `ecdata`. Verified here: for all $64{,}687$ curves of
conductor below $10{,}000$ the pattern of $\psi_3$ and $\Gal(\psi_3)$ agree with the `galrep` label as in 7.3. Paper: Section sec:data ("The
mod 3 images of the tables were checked against the factorisation of the 3-division polynomial"), the appendix (`ns3`),
Section sec:anomaly; Chapter 22.

### Section 8. Absolute irreducibility over $\Q(\sqrt{\ell^*})$, Proposition prop:ns and Lemma lem:h0

**8.1 `prop:galrep:dihedral`** (proposition; P from Chapter 4, 6.6; Chapter 5, galois:index-two-restriction; Chapter 6, 6.4). Let $\ell$ be
odd, $\bar\rho=\bar\rho_{E,\ell}$ irreducible and $K$ a quadratic field. The following are equivalent: (a) $\bar\rho|_{G_K}$ is not absolutely
irreducible; (b) $\bar\rho\simeq\bar\rho\otimes\chi_K$ (over $\F_\ell$, equivalently over $\bar\F_\ell$); (c) $\bar\rho\otimes\bar\F_\ell\simeq\Ind_{G_K}^{G_\Q}\psi$ for a character
$\psi$ of $G_K$; (d) $a_p(E)\equiv0\pmod\ell$ for all (equivalently almost all) primes $p\nmid N\ell$ inert in $K$. When they hold, every
isomorphism $\bar\rho\to\bar\rho\otimes\chi_K$ has trace $0$ and $H^0(\Q,\ad\bar\rho\otimes\chi_K)$ is a line. For $K=\Q(\sqrt{\ell^*})$ condition (a) is the
failure of the hypothesis of Theorem thm:main. Paper: Theorem thm:main hypothesis, $S_f$ (DFG04 (31)), Theorem thm:qual,
Proposition prop:ns, Lemma lem:h0.

**8.2 `thm:galrep:lstar-automatic`** (theorem; P given 5.3; new in this form, see Part 7). Let $\ell$ be odd, $\ell\nmid N$, and $\bar\rho_{E,\ell}$
irreducible. If $\ell\ge5$, then $\bar\rho_{E,\ell}$ is absolutely irreducible on $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$. If $\ell=3$ and $\bar\rho_{E,3}$ is not
absolutely irreducible there (image $N_s(\F_3)$), then $E$ is ordinary at $3$. Proof: 8.1 and 5.4(ii). Verified: among the curves of
conductor below $10{,}000$, those with an $\ell$Ns or $\ell$Nn label, $\ell\ge5$, for which $a_p\equiv0\pmod\ell$ at every $p<870$, $p\nmid N\ell$, inert in
$\Q(\sqrt{\ell^*})$, are $24$ curves (5Ns.2.1, 7Ns.2.1, 7Ns.3.1, 7Ns.6.1.2), all with $\ell\mid N$; the $28$ curves with 5Ns, 5Nn or 7Ns and
$\ell\nmid N$ are dihedral for another quadratic field. Paper: Theorem thm:main (hypothesis), Section sec:forms ("the curves whose mod
$\ell$ representation is induced from $\Q(\sqrt{\ell^*})$ with $\ell\ge5$, which we did not single out": all of them have $\ell\mid N$), DDT
Theorem 3.15 as quoted in Section 3 (its extra hypothesis matters only at $\ell=3$).

**8.3 `prop:galrep:ns`** (proposition, the paper's Proposition prop:ns; P, in the corrected form). Let $E/\Q$ (with or without CM:
important_notes.md point 9) have $E[3]$ irreducible. Then the image $H$ of $\bar\rho_{E,3}$ is conjugate to $\GL_2(\F_3)$, $N_{ns}(\F_3)$ or
$N_s(\F_3)$; $\bar\rho_{E,3}$ is absolutely irreducible on $\Gal(\Qbar/\Q(\sqrt{-3}))$ unless $H\sim N_s(\F_3)$; in that case
$\bar\rho_{E,3}\otimes\F_9\simeq\Ind\psi$ for a character $\psi$ of $G_{\Q(\sqrt{-3})}$ of order $4$ with values in $\F_9^\times$ (the restriction is irreducible but
not absolutely irreducible over $\F_3$: important_notes.md point 33), $\bar\rho_{E,3}\simeq\bar\rho_{E,3}\otimes\chi_{-3}$ over $\F_3$, $H^0(\Q,\ad\bar\rho_{E,3}(1))$ is a
line, and $h_3(E)=1$ (8.5). The $3$-division polynomial is a product of two irreducible quadratics in $\Q[x]$ in the $N_s$ case and irreducible
in the other two. Proof (the paper's, every step expanded): (1) $\bar\rho(G_{\Q(\sqrt{-3})})=H\cap\SL_2(\F_3)$
(1.1(ii)); (2) the list (7.3 with $E[3]$ irreducible); (3) determinant-one subgroups $\SL_2(\F_3)$, $Q_8$, $C_4=\langle J\rangle$ (Chapter 1, 6.7);
(4) $\SL_2(\F_3)$ and $Q_8$ act absolutely irreducibly: "non-abelian and faithful" is not enough (a Borel subgroup is both), the
missing step is Chapter 1, 5.7 (commutator subgroups) or Chapter 4, 3.7 (Maschke for $Q_8$): important_notes.md point 1;
(5) $C_4$ is abelian, $X^2+1$ irreducible over $\F_3$, eigenvalues $\pm i\in\F_9$, so $\bar\rho|_{G_{\Q(\sqrt{-3})}}\otimes\F_9=\psi\oplus\psi^{-1}$ (Chapter 4, 2.5, 8.2);
(6) Frobenius reciprocity and Clifford theory (Chapter 4, 6.2, 6.6; Chapter 5, galois:index-two-restriction): $\bar\rho\otimes\F_9\simeq\Ind\psi$
and $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$, the isomorphism descending to $\F_3$ (Chapter 4, 1.4(ii)); (7) $H^0$ and $h_3$ by 8.5; (8) lines and roots
of $\psi_3$ (Chapter 9, 4.5; Chapter 1, 6.8). Examples: 726a1: $\psi_3=(x^2-x-74)(3x^2+8x+20)$; 6912d1 ($y^2=x^3-6x-8$, Chapter 5's
example): $\psi_3=3(x^2-4x-2)(x^2+4x+6)$; 338d1; 11a1: $\psi_3=3x^4-4x^3-60x^2-237x-21$ irreducible, $\operatorname{disc}=-3^3\cdot11^{10}$, group $S_4$.
Paper: Proposition prop:ns and its proof in Section sec:boundary, Section sec:anomaly, Remark rem:ns, Conjecture conj:euler,
the appendix (`ns3`).

**8.4 `prop:galrep:ns-structure`** (proposition; P; new in this form, see Part 7). Let $E/\Q$ (CM allowed) have $\bar\rho_{E,3}(G_\Q)\sim N_s(\F_3)$,
and let $K_1$, $K_2$ be the splitting fields of the two quadratic factors of $\psi_3$ (the fixed fields of $\bar\rho^{-1}(C_s)$ and
$\bar\rho^{-1}(\{\pm1,\pm w\})$). (i) $K_1$, $K_2$, $\Q(\sqrt{-3})$ are the three quadratic subfields of the splitting field of $\psi_3$, which is
biquadratic (Chapter 5, galois:quartic-on-lines (e)). (ii) For every prime $p\ne3$, $\bar\rho(I_p)\subseteq C_4=N_s(\F_3)\cap\SL_2(\F_3)=\langle J\rangle$.
Consequently every multiplicative prime $p\ne3$ has $3\mid n_p$ (so $t_3(E,p)\ge1$), every prime $p\ge5$ of type $\mathrm I_n^*$ has $3\mid n$, no
prime $p\ge5$ has type $\mathrm{II}$, $\mathrm{II}^*$, and no prime $p\ne3$ has type $\mathrm{IV}$, $\mathrm{IV}^*$. (iii) Let $R$ be the set of primes
$p\ne3$ ramified in $K_1$. Then $R$ is also the set of primes $p\ne3$ ramified in $K_2$, it equals $\{p\ne3:\bar\rho(I_p)=C_4\}$, and it is
nonempty (the only quadratic field unramified outside $3$ is $\Q(\sqrt{-3})$). For $p\in R$, $\rho_{E,\ell}(I_p)$ is cyclic of order $4$ for every
odd $\ell\ne p$ (a $\pm$unipotent has order $1,2,3,6$ or $\infty$, so the reduction is potentially good; then 2.3); if $p\ge5$, $p$ has type
$\mathrm{III}$ or $\mathrm{III}^*$; conversely every prime $p\ge5$ of type $\mathrm{III}$ or $\mathrm{III}^*$ lies in $R$. (iv) For $p\in R$, $\Frob_p$ acts on
$(\ad V)^{I_p}=\Ql\tau$ by $\chi_{-3}(p)$ ($\bar\rho(\Frob_p)$ commutes with $J$ iff it lies in $C_4$ iff $\det=p\equiv1\pmod3$), so
$L_p(A_f,s)^{-1}=1-\chi_{-3}(p)p^{-s}$ and $e_3(E,p)=v_3(p-\chi_{-3}(p))\ge1$; for $p\ge5$ comparison with 4.1 ($\chi_{-4}(p)$) gives
$\chi_{-4}(p)=\chi_{-3}(p)$, i.e. $p\equiv1$ or $11\pmod{12}$; for $p=2$: $P_2(X)=1+2X$, $e_3(E,2)=1$. (v) $a_p(E)\equiv0\pmod3$ for every prime $p\nmid3N$
with $p\equiv2\pmod3$ (8.1(d)). (vi) If $3\nmid N$, $E$ is ordinary at $3$ (8.2). (vii) $h_3(E)=1$ (8.5). Verified on all $120$ non-CM curves
with image 3Ns of conductor below $10{,}000$: for $100$ of them $R$ contains primes $p\ge5$, exactly the type $\mathrm{III}$, $\mathrm{III}^*$ primes $\ge5$,
all $\equiv1$ or $11\pmod{12}$; for the other $20$ (classes 3840h, k, o, r, 4864b, c, o, p, 6912d, f, j, l, p, r, v, x) the only prime of $R$ is
$2$, of type $\mathrm{III}$ or $\mathrm{III}^*$ with $f_2=8$ and $\bar\rho(I_2)$ cyclic of order $4$; every multiplicative prime $p\ne3$ has $3\mid n_p$; no type
$\mathrm{II}$, $\mathrm{II}^*$ at $p\ge5$ and no $\mathrm{IV}$, $\mathrm{IV}^*$ at $p\ne3$; $a_p\equiv0\pmod3$ for $p\equiv2\pmod3$, $p<410$; $3\nmid a_3$ whenever $3\nmid N$; Euler
factors $1+11X$ (726a1 at $11$), $1-13X$ (338d1 at $13$), $1+2X$ (3840h1, 3840h2, 4864b1, 4864c1, 6912d1, 6912j1 at $2$). Paper: Section
sec:anomaly ("every $\Ns$ curve of the tables has a prime of type $\mathrm{III}$ or $\mathrm{III}^*$ with a positive term $e_3$"; "the residue
classes ... are $q\equiv1$ and $q\equiv11\pmod{12}$ ..., with some $q=2$"; "the violation involves a prime $p\equiv-1\pmod3$ with
$t_3(E,p)\ge1$"), the appendix ("for 726a1 ... the type $\mathrm{III}$ term and the correction cancelling"), Remark rem:ns, Conjecture
conj:euler.

**8.5 `lem:galrep:h0`** (lemma, the paper's Lemma lem:h0 in corrected form; P). Let $\ell$ be odd, $\bar\rho=\bar\rho_{E,\ell}$ irreducible ($E$ with or
without CM), $W^D=\ad T(1)\otimes\Ql/\Zl$ (Chapter 18's notation; $T^D=\Hom(\ad T,\Zl(1))\simeq\ad T(1)$ via the trace form for $\ell$ odd, Chapter 4,
7.6). Then: (i) $H^0(\Q,W^D)[\ell^k]=H^0(\Q,\ad(T/\ell^k)(1))=\Hom_{G_\Q}(T/\ell^k,(T/\ell^k)(1))$, every such map having trace $0$ automatically
($\End(T)(1)=\ad T(1)\oplus\Zl(1)$ and $H^0(\Q,\mu_{\ell^k})=0$); (ii) $H^0(\Q,W^D)\simeq\Z/\ell^h$ is finite and cyclic, with $h=h_\ell(E)$ the largest $k\ge0$
such that $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$ (Chapter 4, 10.5, using absolute irreducibility, 1.4(i)); (iii) $h_\ell(E)=0$ for every
$\ell\ge5$, and $h_3(E)\le1$, with $h_3(E)=1$ iff $\bar\rho_{E,3}\simeq\bar\rho_{E,3}\otimes\chi_{-3}$ iff $\bar\rho_{E,3}$ is not absolutely irreducible on
$\Gal(\Qbar/\Q(\sqrt{-3}))$ iff the image is $N_s(\F_3)$; (iv) $h_\ell$ is invariant under quadratic twists and prime-to-$\ell$ isogenies
(1.3). Proof of (iii): an isomorphism modulo $\ell^k$ gives $\chi_\ell^2\equiv1\pmod{\ell^k}$ on $G_\Q$ by determinants, and $\chi_\ell(G_\Q)=\Zl^\times$, so
$\ell^k=3$ (Chapter 5, galois:twist (c); Chapter 2, 5.5); for $\ell=3$, $k=1$: $\bar\chi_3=\chi_{-3}$ and 8.1, 8.3. Remarks for the text: (a) the paper's
sentence "for $E$ without complex multiplication it is finite" and its reason ("$\rho\simeq\rho\otimes\chi_\ell$ would force $a_p=0$ at all primes
inert in $\Q(\sqrt{\ell^*})$") confuse $\chi_\ell$ with $\chi_{\ell^*}$ (important_notes.md point 5); the determinant argument replaces it and needs
no CM hypothesis; CM by $\Q(\sqrt{\ell^*})$ forces $\ell\mid N$ anyway (point 14; Chapter 9, 6.5). (b) The criterion for $h_\ell(E)>0$ is
$\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$, not $\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ (point 6); for $\ell\ge5$ the latter can hold only if $\ell\mid N$ (8.2). (c) The numerical
check of Section sec:anomaly ("some prime $p<1223$ inert in $\Q(\sqrt{-3})$ has $9\nmid a_p$") is valid but superfluous: $h_3(E)\ge2$ would give
$a_p\equiv pa_p\pmod9$ by traces, and $p-1$ is a unit mod $3$ for $p\equiv2\pmod3$, so $9\mid a_p$ at every such $p\nmid3N$; the determinant argument of (iii)
excludes $h_3(E)\ge2$ for all $E$ at once. (d) "Irreducible" must be read as
"absolutely irreducible" in the Clifford step (point 10); for $\bar\rho_{E,\ell}$ they agree (1.4(i)). Paper: Lemma lem:h0, Conjecture conj:euler
($h_\ell(E)$), Section 1.3, Proposition prop:ns, Remark rem:ns, Section sec:anomaly ("$h_3(E)=1$ for every $\Ns$ curve"), the proof of
Theorem thm:main ($H^0(\Q,W^D)=0$), the appendix (`ns3` as the correction term); Chapter 18 restates it.

**8.6 `cor:galrep:Sf`** (corollary; P). Let $\ell$ be odd and $\ell\nmid N$. The following are equivalent: (a) $\ell\notin S_f$ (DFG04 (31): $\ell\nmid2N$
and $\bar\rho|_{\Gal(\Qbar/\Q(\sqrt{\ell^*}))}$ absolutely irreducible); (b) $E[\ell]$ is irreducible and $h_\ell(E)=0$; (c) $E[\ell]$ is irreducible and, if
$\ell=3$, the image of $\bar\rho_{E,3}$ is not $N_s(\F_3)$. So the hypothesis of Theorem thm:main reads "$\ell\nmid2N$, $E[\ell]$ irreducible, and not
($\ell=3$ and image 3Ns)", the extra hypothesis of Theorem thm:qual at $\ell=3$ is "image not 3Ns", and in the range $\ell\nmid N$ the
failure of the hypothesis is the vanishing-or-not of $h_\ell(E)$. Proof: 8.1, 8.2, 8.5. Data: $62$ curves with image 3Ns and $3\nmid N$ below
conductor $10{,}000$ are the only failures at $\ell=3$ with $3\nmid N$ and $E[3]$ irreducible. Paper: Theorem thm:main, Theorem thm:qual, Section
4.2 ($S_f$), Section sec:forms, Remark rem:ns, Conjecture conj:euler (the two hypotheses "$\ell\notin S_f$" and "$h_\ell=0$" coincide when $\ell\nmid N$).

### Section 9. The Eisenstein case

**9.1 `prop:galrep:reducible`** (proposition; P given 2.2, 3.2, 5.3 and Kronecker-Weber, Chapter 6, 5.5). Let $\ell$ be odd, $\ell\nmid N$, and
$E[\ell]$ reducible. (i) $\bar\rho^{\mathrm{ss}}=\psi_1\oplus\psi_2$ with $\psi_1\psi_2=\bar\chi_\ell$ (Chapter 9, 5.2(iii)); (ii) $E$ is ordinary at $\ell$ and
$\{\psi_1|_{I_\ell},\psi_2|_{I_\ell}\}=\{\omega,1\}$ (5.4(i)); (iii) $\psi_1$, $\psi_2$ are unramified at every multiplicative prime ($\bar\rho(I_q)$ is unipotent
there, 3.2); (iv) if $E$ is semistable, $\{\psi_1,\psi_2\}=\{1,\bar\chi_\ell\}$, so $a_p\equiv1+p\pmod\ell$ for all $p\nmid N\ell$, and $E$ or a curve $\ell$-isogenous
to it has a rational point of order $\ell$ (the sub is $\Z/\ell$ or $\mu_\ell$; in the second case $E/\mu_\ell$ contains $E[\ell]/\mu_\ell\simeq\Z/\ell$).
Proof of (iv): a character of $G_\Q$ with values in $\bar\F_\ell^\times$ unramified outside $\ell$ factors through $\Gal(\Q(\zeta_{\ell^m})/\Q)$ and has
order prime to $\ell$, hence is a power of $\bar\chi_\ell$ determined by its restriction to $I_\ell$. Verified: every curve of conductor
below $10{,}000$ with a Borel or split Cartan label at $\ell\in\{3,5,7\}$, $\ell\nmid N$, $N$ square-free ($1{,}315$, $158$, $26$ curves) has $a_p\equiv1+p\pmod\ell$
for all $p<282$, $p\nmid N\ell$. Reference: Serre72, Section 5 (verify); Mazur77 for the prime-level case. Paper: Section sec:eis,
Conjecture conj:eis (torsion as the controlling invariant), Open question 4, background for "Eisenstein".

**9.2 `prop:galrep:eis-labels`** (proposition; P, with data). For $\ell=3$: 3B.1.1 iff $E$ has a rational point of order $3$ and $E[3]$ is not
split; 3Cs.1.1 iff $E[3]\simeq\Z/3\oplus\mu_3$; 3B.1.2 iff $\mu_3\subset E[3]$ with quotient $\Z/3$, non-split; the twist by $\chi_{-3}$ exchanges 3B.1.1 and
3B.1.2 (1.3); so $3\mid\#E(\Q)_{\mathrm{tors}}$ iff the label is 3B.1.1 or 3Cs.1.1. Restatement of Chapter 9, 9.8 (important_notes.md point 17):
if $E$ has no CM and image 3Cs.1.1, then $E(\Q)$ has no point of order $9$; so in Conjecture conj:eis
$v_3(\#E(\Q)_{\mathrm{tors}})+[E[3]\simeq\Z/3\oplus\mu_3]\le2$, and the bound $D\le2$ follows from the first bound. For $\ell=5$: 5Cs.1.1 iff $E[5]\simeq\Z/5\oplus\mu_5$
(11a1), 5B.1.1 iff a rational point of order $5$ with $E[5]$ non-split (11a3). Data: $2{,}811$ curves 3B.1.1 and $264$ curves 3Cs.1.1 are
exactly the curves of conductor below $10{,}000$ with $3\mid\#E(\Q)_{\mathrm{tors}}$; the $264$ curves 3Cs.1.1 have torsion of order $3$ or $6$
(Chapter 9). Paper: Section sec:eis ("the split Cartan image 3Cs.1.1": wrong description, point 44; "We have not proved that the
two cannot coexist": point 17), Conjecture conj:eis.

**9.3 `rem:galrep:eisenstein`** (remark; R, pointers). Reducible $\bar\rho$ means: $T_\ell$ of curves in the isogeny class are not
homothetic (Chapter 4, 10.4: the lattices of $\ell$-isogenous curves), the maximal ideal of the Hecke algebra attached to $(f,\ell)$
is Eisenstein (Chapter 14), multiplicity one and the theorems of Diamond, Flach and Guo are unavailable, and the
modular degree can lose the local divisibility (the deficit $D$ of Conjecture conj:eis). Why the hypothesis "$E[\ell]$
irreducible" appears in Theorem thm:quant, Conjecture conj:euler and Proposition prop:forms. Paper: Section sec:eis, Conjecture
conj:eis, Open question 4.

### Section 10. Serre's conjecture for $\bar\rho_{E,\ell}$ and the optimal level

**10.1 `thm:galrep:optimal-level`** (theorem; R, with the elliptic-curve inputs P). (i) (Serre's conjecture, Khare and Wintenberger;
stated) Every odd irreducible $\bar\sigma\colon G_\Q\to\GL_2(\bar\F_\ell)$ arises from a newform of weight $k(\bar\sigma)$, level $N(\bar\sigma)$ and character determined
by $\det\bar\sigma$. (ii) (The form used by the paper: Ribet, Carayol, Diamond; DDT Theorem 3.15, as quoted in Section 3) Let $\ell$ be odd
and $E'/\Q$ with $\ell\nmid N(E')$ and $\bar\rho=\bar\rho_{E',\ell}$ irreducible, and if $\ell=3$ with image not $N_s(\F_3)$ (8.6). Then there are a newform $g$ of
weight $2$ on $\Gamma_0(N(\bar\rho))$ and a prime $\lambda\mid\ell$ of its coefficient field with $\bar\rho_{g,\lambda}\simeq\bar\rho\otimes\bar\F_\ell$, i.e. $a_p(g)\equiv a_p(E')\pmod\lambda$
for all $p\nmid\ell N(E')$. Elliptic-curve inputs proved here: $\bar\rho$ is modular of level $N(E')$ (modularity, Chapter 14), odd (1.1(iii)),
good at $\ell$ (5.1(i), so $\delta(\bar\rho)=0$), of weight $2$ (5.1(iii)), with $\det\bar\rho=\bar\chi_\ell$ (1.1(ii)) and $N(\bar\rho)$ given by 6.2. That the
nebentypus is trivial is proved in Chapter 15; the theorem itself (Ribet's level lowering, Carayol, Diamond) is stated there, not
proved (Chapter 15 proves only the specialisation to $\bar\rho_{E',\ell}$; important_notes.md B18). Reference: DDT Theorem 3.15
(as cited by the paper; verify); Ribet90; Carayol89; Diamond95; Serre87; KhareWintenberger. Paper: the optimal-level paragraph
of Section 3, Theorem thm:qual cases (a), (b), (c).

**10.2 `ex:galrep:level-lowering`** (worked example; P for the data). The congruences of the Example of Section 3 read through
4.5 and 6.2: 121c1 (type $\mathrm{IV}$ at $11$, $\deg\varphi=6$): $N(\bar\rho_{121c1,3})=11$, $g=f_{11a}$; 121a1 (type $\mathrm{II}$, $\deg\varphi=6$): twist by $\chi_{-11}$ into class 121c,
then 11a, $a_p(121\mathrm a1)\equiv\chi_{-11}(p)a_p(11\mathrm a1)\pmod3$; 77c1 ($\mathrm I_3$ at $7$, $\deg\varphi=6$): $N(\bar\rho_3)=11$, $77\mathrm c1\equiv11\mathrm a1\pmod3$; 539c1 ($\mathrm I_3^*$ at $7$,
$\deg\varphi=288=2^5\cdot3^2$): twist by $\chi_{-7}$ is class 77c, then 11a; 980i1 ($\mathrm I_5^*$ at $7$, $\deg\varphi=2880$) at $\ell=5$: twist 140b1, then
20a1, with $5\mid N$ (illustration only). All congruences checked for $p<2000$ ($p<1224$ for $\ell=5$); modular degrees from `degphi`.
Paper: Section 3, Example; Theorem thm:qual.

## 3. Section plan with target line counts

Lines of LaTeX, card excluded (PLAN.md 7.3: up to 2,800 for this chapter). Items per section: 4, 3, 5, 6, 4, 3, 6, 6, 3, 2
(42 items).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2, stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | Section 1.1; hypothesis of thm:main and $S_f$; lem:tamagawa-exp; lem:IV; rem:types; lem:euler (inertia half); lem:old (local analysis); optimal-level paragraph; prop:ns; lem:h0; sec:anomaly; sec:eis; conj:eis; prop:forms and rem:wild (type IV at 2); def:terms, rem:ko | 55 |
| 1 | The representations $\rho_{E,\ell}$ and $\bar\rho_{E,\ell}$ | conventions C1 to C6 as `convention` environments; 1.1 to 1.4; `paperlink` for Section 1.1 and for "irreducible" (point 10) | 180 |
| 2 | Neron-Ogg-Shafarevich, component groups and inertia invariants | 2.1 to 2.3, with the full proof of 2.1 (a) to (d) and of 2.2; `warning` that 2.2 is for additive and multiplicative reduction separately | 250 |
| 3 | Good and multiplicative reduction | 3.1 to 3.5; the Tate matrices in display; both proofs of lem:tamagawa-exp; `paperlink` for lem:tamagawa-exp (point 8), lem:tamfactor (point 42), thm:main's $\mathrm I_n^*$ step (point 18) | 300 |
| 4 | Additive potentially good reduction | 4.1 to 4.6; the shapes table and the mod $3$ table (`booktabs`); both proofs of lem:IV; 4.4 with its consequences for prop:forms; `paperlink` for lem:IV (point 13), rem:types (point 22), lem:euler (points 12, 34), rem:wild (point 43) | 380 |
| 5 | The representation at $\ell$ | 5.1 to 5.4; fundamental characters; the ordinary and supersingular cases; `paperlink` for lem:old ($p=\ell$) | 190 |
| 6 | Conductors of mod $\ell$ representations | 6.1 to 6.3; the formula $a_p=f_p-\dim\Phig_p[\ell]$ with proof; the examples table | 200 |
| 7 | The images of $\bar\rho_{E,\ell}$ | 7.1 to 7.6; the mod $3$ image table (may be split in two: group data and arithmetic data); labels at $\ell=5,7,11,13$ as a small table; `paperlink` for sec:anomaly, sec:eis (point 44), sec:data | 320 |
| 8 | Absolute irreducibility over $\Q(\sqrt{\ell^*})$; prop:ns; lem:h0 | 8.1 to 8.6; the full proofs of prop:ns (points 1, 9, 33) and lem:h0 (points 5, 6, 10, 14); 8.2 and 8.4 with their data | 400 |
| 9 | The Eisenstein case | 9.1 to 9.3; `paperlink` for conj:eis and sec:eis (points 17, 44) | 160 |
| 10 | Serre's conjecture and the optimal level | 10.1, 10.2; the Example of Section 3 as a table | 140 |
| 11 | Exercises | the 16 exercises of Part 4.2 | 150 |
| 12 | Notes and references | Serre-Tate, Serre72, Serre87, Kraus90, Zywina15, Sutherland16, Edixhoven92, Carayol89, Livne, DDT, Silverman; which numbers were cited and which only by section | 50 |
| | **total** | | **2,775** |

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| $\rho_{E,\ell}\colon G_\Q\to\Aut(T_\ell E)$, $\bar\rho_{E,\ell}$, continuity | 1.1 |
| $\det\rho_{E,\ell}=\chi_\ell$ (Weil pairing); $\det\bar\rho_{E,3}=\chi_{-3}$ cuts out $\Q(\sqrt{-3})$ | 1.1(ii) |
| complex conjugation has determinant $-1$ and trace $0$ | 1.1(iii), 1.4(i) |
| Neron-Ogg-Shafarevich (unramified iff good; potentially good iff finite inertia image) | 2.1, 2.3 |
| local representation at a good prime ($X^2-a_pX+p$) | 3.1 |
| multiplicative prime: Tate curve, extension of $\varepsilon$ by $\varepsilon\chi_\ell$, Kummer class in the corner, non-split; DDT Theorem 3.1(e) | 3.2 |
| the paper's Lemma lem:tamagawa-exp in full, split and nonsplit | 3.3 |
| additive potentially good, $q\ge5$: inertia cyclic of order $2,3,4,6$ (Kraus), eigenvalues | 2.3, 4.1, 4.2 |
| the paper's Lemma lem:IV in full | 4.3 (and 4.4 at $q=2$) |
| the paper's Remark rem:types in full | 4.5 |
| potentially multiplicative additive reduction ($\rho=\rho'\otimes\chi_{q^*}$) | 3.4 |
| at $\ell$: finite flat, crystalline; Deligne-Fontaine description; $a_\ell\bmod\ell$ determined by $\bar\rho|_{D_\ell}$ | 5.1, 5.2, 5.3, 5.4 |
| Artin conductor and Serre conductor; $N(\bar\rho_{E,\ell})\mid N$ (Carayol); prime to unramified primes | 6.1, 6.2, 6.3 |
| Serre's open image theorem | 7.1 |
| classification of images for non-CM $E/\Q$ (Zywina, $\ell=3,5,7,11,13$); labels 3B, 3B.1.1, 3Cs.1.1, 3Ns, 3Nn, 3Cs, 3Cn | 7.2, 7.3, 7.4, 7.5 |
| reducible representations and rational isogenies; Eisenstein case; $\Z/3\oplus\mu_3$ as 3Cs.1.1 | 1.4(ii), 9.1, 9.2, 9.3 |
| irreducible versus absolutely irreducible (complex conjugation, $\ell$ odd) | 1.4(i) |
| absolute irreducibility on $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$, dihedral and induced case | 8.1, 8.2, 8.6 |
| the paper's Proposition prop:ns in full | 8.3 (with 7.3, 8.4) |
| the paper's Lemma lem:h0 in full ($h_\ell(E)$, $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$, finiteness: corrected) | 8.5 |
| semisimplification and Brauer-Nesbitt for $\bar\rho_{E,\ell}$ ($a_p\bmod\ell$ on a density-one set) | 1.4(iii) |
| Serre's conjecture for $\bar\rho_{E,\ell}$ (optimal level, weight $2$, level $N(\bar\rho)$) | 10.1, 10.2 |
| Galois representation of a quadratic twist | 1.3 |
| computing mod $\ell$ images (division polynomials, Sutherland's algorithm) | 7.6 |
| Section 6 row: $\rho_{E,\ell}$, $\bar\rho$, $T$, $V$, $E[\ell]$, absolute irreducibility, restriction to $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$ | 1.1, 1.4, 8.1, 8.2, 8.6 |
| Section 6 row: normaliser of a split Cartan, 3Ns, $\GL_2(\F_3)$ and subgroups, orbits on lines | 7.2, 7.3, 8.3, 8.4 |
| Section 6 row: $h_\ell(E)$, $\bar\rho\simeq\bar\rho\otimes\chi$ | 8.1, 8.5 |
| Section 6 row: $3$-division polynomial and its factorisation pattern | 7.3, 7.6, 8.3 |
| Section 6 row: Eisenstein case, rational $\ell$-isogeny, $\Z/3+\mu_3$, torsion | 9.1, 9.2, 9.3 |
| Section 6 row: level lowering, Serre conductor, Serre's conjecture | 6.1, 6.2, 6.3, 10.1, 10.2 |
| Section 6 row: image of inertia at additive primes, unipotent elements, $\Z_3[\zeta_3]$ | 2.2, 4.1, 4.3, 4.4, 4.5 |
| Section 6 row: Deligne-Fontaine description of $\bar\rho$ at $\ell$ | 5.2, 5.3 |
| Section 6 row: DDT Theorem 3.1(e), local structure at multiplicative primes | 3.2, 3.3 |
| Section 6 row: finite flat group schemes, "good at $\ell$" | 5.1 |
| hook: Section 1.1 ($V$, $T$, $\rho$, $\bar\rho$, $A_f=\ad V$, $\delta_p=\dim V^{I_p}$) | 1.1, 1.2, 3.5 |
| hook: Theorem thm:main hypothesis ($\ell\notin S_f$) | 1.4, 8.1, 8.2, 8.6 |
| hook: Lemma lem:tamagawa-exp | 3.3 |
| hook: Lemma lem:IV | 4.3, 4.4 |
| hook: Remark rem:types | 4.5 |
| hook: Lemma lem:euler (inertia images and invariants) | 3.2(v), 3.4, 4.1, 4.4(iv), 8.4(iv) |
| hook: Lemma lem:old (local analysis at $p=\ell$, at $p\,\|\,N$ ramified or unramified, at $p\nmid\ell N$) | 5.3, 3.3, 3.2(iii), 1.4(iii) |
| hook: the optimal-level paragraph of Section 3 | 5.1, 6.1, 6.2, 10.1 |
| hook: Proposition prop:ns | 7.3, 8.3 |
| hook: Lemma lem:h0 | 8.5 |
| hook: Section sec:anomaly | 7.3, 8.4, 8.5 |
| hook: Section sec:eis | 7.3, 9.1, 9.2 |
| hook: Conjecture conj:eis | 9.2, 9.3 |
| also: Definition def:terms ($t_\ell$ from $v_q(j)$; $\mathrm I_n^*$ at $2$), Section 1.5 and Remark rem:ko(2) (Tamagawa exponent) | 3.3(i), 3.4 |
| also: Proposition prop:forms, Remark rem:wild, Section sec:wild (type $\mathrm{IV}$ at $2$) | 4.4, 4.6 |
| also: Theorem thm:qual and the Example of Section 3 | 4.3, 4.5, 6.2, 6.3, 10.1, 10.2 |
| also: proof of Theorem thm:main (the $\mathrm I_n^*$ primes, including $q=2$) | 3.4 |
| also: Lemma lem:twist, Theorem thm:quant ($\ad T$ unchanged by twists) | 1.3, 3.4 |
| also: Section sec:data, Section sec:forms, the appendix (`ns3`) | 7.6, 8.2, 8.6 |
| also: Remark rem:ns, Conjecture conj:euler ($h_\ell$, $w_3$ untouched) | 8.4, 8.5, 8.6 |

### 4.2 Exercises (Section 11 of the chapter), graded from easy to harder

1. Show that for $\ell$ odd $\rho_{E,\ell}(c)$ is conjugate in $\GL_2(\Zl)$ to $\operatorname{diag}(1,-1)$, and deduce that $\bar\rho_{E,\ell}$ is irreducible iff
   absolutely irreducible. Why does the argument fail for $\ell=2$?
2. Check the paper's claim (Lemma lem:tamagawa-exp) on 11a1 and 11a3: $n_{11}=5$, resp. $1$; show that $\bar\rho_{11a1,5}$ is unramified at $11$
   ($E[5]\simeq\Z/5\oplus\mu_5$) while $\bar\rho_{11a3,5}$ is ramified at $11$, and compute $\#E[5^t]^{I_{11}}$ for both.
3. Prove the hard direction of the criterion of Neron, Ogg and Shafarevich from $E_0/E_1\simeq\tilde E_{\mathrm{ns}}$, $E_1$ pro-$p$ and the finiteness of $E/E_0$.
4. Prove Lemma 2.2: for additive reduction at $q\ne\ell$, $E[\ell^k]^{I_q}\simeq\Phi_q(\bar\F_q)[\ell^k]$. Deduce that the $\ell$-part of $c_q$ is $\#E(\Q_q)[\ell^\infty]$ when
   the reduction is additive (compare the final check in the proof of Lemma lem:tamfactor).
5. Check the paper's claim (Lemma lem:IV) for 121c1: type $\mathrm{IV}$ at $11$; show $N(\bar\rho_{121c1,3})=11$ and verify $a_p(121\mathrm c1)\equiv a_p(11\mathrm a1)\pmod3$ for
   $p<100$, including $p=3$ (both ordinary at $3$).
6. Check the paper's claim (Remark rem:wild) that a curve of type $\mathrm{IV}$ at $2$ has $P_2(X)=1+2X$ and $e_3(E,2)=1$: prove it with Lemma 2.2 at
   $q=2$ and Theorem 2.3, and check it on 20a1 and 980i1 (type $\mathrm{IV}^*$ at $2$) with `lfunsympow`.
7. Derive Kraus's table for $q\ge5$ ($\mathrm I_0^*\mapsto2$, $\mathrm{IV},\mathrm{IV}^*\mapsto3$, $\mathrm{III},\mathrm{III}^*\mapsto4$, $\mathrm{II},\mathrm{II}^*\mapsto6$) from the component groups,
   Lemma 2.2 at $\ell=2$ and $\ell=3$, and the independence of $\ell$ (Remark 4.2).
8. Check the paper's claim (Remark rem:types) row by row (table 4.5): for each additive type at $q\ge5$ compute $\bar\rho_{E,3}(I_q)$, $E[3]^{I_q}$, the
   Serre exponent, and the exponent after twisting by $\chi_{q^*}$. Which types does the paper's remark omit?
9. Show that $C_{ns}(\F_\ell)$ is never the image of $\bar\rho_{E,\ell}$ for $\ell$ odd, and that the image never lies in $\SL_2(\F_\ell)$.
10. Check the paper's claim (Proposition prop:ns) for 726a1: factor $\psi_3$, identify the three quadratic subfields $\Q(\sqrt{33})$, $\Q(\sqrt{-11})$,
    $\Q(\sqrt{-3})$, deduce the image $N_s(\F_3)$, and check $a_p\equiv0\pmod3$ for the primes $p\equiv2\pmod3$, $p<60$, $p\ne2,11$.
11. Check the paper's claim (Section sec:anomaly) that $h_3(E)=1$ for every curve with image 3Ns, using Lemma 8.5 only; then show that the
    paper's numerical test ("$9\nmid a_p$ for some inert $p<1223$") also excludes $h_3(E)\ge2$, and why it is not needed.
12. Prove Proposition 8.4(iii), (iv): a curve with image 3Ns has a prime $p\ne3$ with cyclic inertia of order $4$, and $e_3(E,p)\ge1$ there. Check on
    726a1 ($p=11$), 338d1 ($p=13$) and 6912d1 ($p=2$).
13. Let $\ell\ge5$ and $\ell\nmid N$. Using the fundamental characters, show that $\bar\rho_{E,\ell}\not\simeq\bar\rho_{E,\ell}\otimes\chi_{\ell^*}$. Find in `ecdata` a curve with image 5Ns
    and $5\nmid N$, and determine the quadratic field from which its mod $5$ representation is induced.
14. Let $E$ be semistable, $\ell$ odd, $\ell\nmid N$, $E[\ell]$ reducible. Show $a_p\equiv1+p\pmod\ell$ for $p\nmid N\ell$ and that $E$ or an $\ell$-isogenous curve has a
    rational point of order $\ell$. Check on 14a1 and 26a1 at $\ell=3$.
15. Check the paper's claim (Section sec:eis) that 3Cs.1.1 is "the split Cartan image": identify the images of 14a1 and of 539a2 and show the
    claim is a misdescription.
16. Compute $N(\bar\rho_{E,3})$ from the formula $a_p=f_p-\dim\Phig_p[3]$ for 539c1, 77c1, 726a1 and 6912d1, and $N(\bar\rho_{E,5})$ for 980i1 and 140b1;
    say which of the Section 3 congruences of the paper these explain.

## 5. Dependencies and forward pointers

Results from earlier chapters used here (by chapter label only, `\Cref{ch:...}`):
* Chapter 1 (`ch:groups`): models and subgroups of $\GL_2(\F_3)$ (6.2 to 6.6), the three images (6.7), orbit dichotomy (6.8), elements of
  determinant $-1$ and trace $0$ (6.9), labels as subgroups (6.10), unipotent elements and their order (5.6), commutator lemma (5.7),
  Cartan subgroups and normalisers (5.8, 5.9), Dickson (5.10), $1+\ell M_2(\Zl)$ pro-$\ell$ and torsion-free (7.4).
* Chapter 2 (`ch:rings`): $\F_9=\F_3[i]$, $\chi_{-3}$, $\chi_{-4}$ and their values, $q^*$, $a^2\equiv1\pmod{\ell^k}$ for all units iff $\ell^k=3$ ($\ell$ odd) (5.5).
* Chapter 3 (`ch:modules`): DVRs, lattices, Nakayama, cyclic modules over a DVR, the snake lemma.
* Chapter 4 (`ch:reps`): 2.4, 2.5, 3.2(ii), 3.6, 3.7, 5.2, 5.3, 6.2, 6.6, 6.7, 7.2, 7.4, 7.6, 8.1 to 8.5, 9.1 to 9.4, 10.1 to 10.5, 11.1.
* Chapter 5 (`ch:galois`): galois:continuous-reps, galois:cyclotomic-character, galois:complex-conjugation, galois:restriction,
  galois:index-two-restriction, galois:twist, galois:l-adic-kummer, galois:quartic-on-lines, galois:frobenius-on-lines,
  galois:chebotarev-brauer-nesbitt, galois:congruent-ap, galois:sqrt-lstar.
* Chapter 6 (`ch:ant`): Frobenius and inertia in $G_\Q$ (3.7, 3.10), the finite tame relation (3.11, 3.12), $\Z_3[\zeta_3]$ (4.7, 4.8),
  $\Zl[\zeta_3]$ (4.9), the commutant (4.10), Kronecker-Weber (5.5), the twist detector (6.4), CM (6.5).
* Chapter 7 (`ch:local`): $\Q_q^{\mathrm{ur}}$ and unramified base change (4.2, 4.4), tame character and tame relation (5.3, 5.4), Frobenius fixing
  roots (5.5), finite tame images (5.6), wild images (5.7), Kummer classes on inertia (6.2), quadratic characters of $\Q_q$ (6.3),
  Weil-Deligne representations and $\mathrm{sp}(2)$ (7.2 to 7.6), invariants, Swan and Artin conductors (8.1, 8.3, 8.4), the shapes (9.1 to 9.5).
* Chapter 8 (`ch:curves`): only through Chapter 9.
* Chapter 9 (`ch:ellcurves`): Weierstrass data (1.1 to 1.6), $\psi_3$ (4.4 to 4.6), Weil pairing, $T_\ell E$, $\rho$, $\det$, complex conjugation (5.1
  to 5.7), CM (6.3 to 6.5), curves over $\F_q$ (8.3, 8.6), torsion, isogenies, $\Z/\ell\oplus\mu_\ell$, no cyclic $27$-isogeny, prime-to-$\ell$
  isogenies (9.3 to 9.10), twists (10.1 to 10.6), labels (12.1).
* Chapter 10 (`ch:reduction`, outlined in parallel): minimal models, reduction types, $E_0$, $E_1$, formal groups, $E(K)/E_0(K)\simeq\Phi_p(k)$ (Neron
  model, Hensel), Kodaira types and component groups, Tate's algorithm, conductor exponents and Ogg's formula, the semistable
  reduction theorem, the Tate curve and $E_{\mathsf q}[\ell^t]$, Kraus's theorem, Lemma lem:twist (i), (ii), Remark rem:wild. Items 2.1 to 2.3, 3.2 to
  3.5, 4.1 to 4.6, 6.2 depend on these; they are black boxes here, cited with `\Cref{ch:reduction}`.

Black boxes imported from later chapters (stated with a forward `\Cref`, never used in the proof of a numbered result of
this chapter except where said): modularity and the Hecke algebra (Chapters 13, 14; only in 10.1 and 9.3); the Galois
representations of newforms and the optimal-level theorem in general (Chapter 15; only in 1.4(iii), 5.3(iii), 10.1); crystalline
representations and Bloch-Kato conditions (Chapter 18; only in 5.1(ii)); $L$-factors in the symmetric-square normalisation and
$e_\ell(E,q)$ (Chapter 19; only in 4.4(iv) and 8.4(iv), which use the definition $L_q(A_f,s)=\det(1-\Frob_q^{-1}q^{-s}\mid(\ad V)^{I_q})^{-1}$, with the geometric Frobenius $\Frob_q^{-1}$ (never $\Phi_q$ here, B-C2(b)) and
$L_q(\Sym f,s)=L_q(A_f,s-1)$ as conventions).

Forward pointers (chapters that use this one):
* Chapter 14 (`ch:moddeg`): reducible $\bar\rho$ and the Eisenstein ideal (9.1 to 9.3); $\ell\nmid2N$, $\bar\rho$ irreducible in Remark rem:free (1.4).
* Chapter 15 (`ch:modgalrep`): 1.4(iii) (congruences give isomorphic residual representations), 3.2 and 3.3 (the cases $p\,\|\,N$ of Lemma
  lem:old), 5.3 (the case $p=\ell$), 6.1 and 6.2 (Serre conductor, $N(\bar\rho)\mid N$), 4.3, 4.5 (Serre exponents in Theorem thm:qual), 8.6 (the
  hypothesis at $\ell=3$ of DDT Theorem 3.15), 10.1, 10.2.
* Chapter 16 (`ch:cohomology`): 3.2 (the Tate shape, unipotent and pro-$\ell$ action of inertia; motivation for its model).
* Chapter 17 (`ch:galcoh`): 3.2 (the Kummer class $\varepsilon\kappa$ in the corner).
* Chapter 18 (`ch:blochkato`): 3.2, 3.4 (inputs of Lemma lem:tamfactor, including $q=2$ for important_notes.md point 18), 5.1 (crystalline at
  $\ell$), 8.5 (Lemma lem:h0, restated there in Selmer language), 8.6 ($\ell\notin S_f$), 2.2 (the $\ell$-part of $c_q$ at additive primes).
* Chapter 19 (`ch:lfunctions`): 3.1, 3.2(v), 3.4, 4.1, 4.4, 4.6, 8.4(iv) (the inputs of Lemma lem:euler and Remark rem:wild; Chapter 19 computes
  the factors and $e_\ell$).
* Chapter 20 (`ch:congruence`): 8.5, 8.6 (the hypothesis of Theorem thm:main and the vanishing of $H^0(\Q,W^D)$), 3.4 (the $\mathrm I_n^*$ step at
  $q=2$), 1.3 (twists in Theorem thm:quant), 4.4 (Proposition prop:forms without exception).
* Chapter 21 (`ch:paper`): 3.3, 4.3, 4.4, 4.5, 8.3, 8.4, 8.5, 8.6, 9.2 (the tour must use the corrected statements of 4.5 and 8.5 and may
  shorten its proofs of lem:tamagawa-exp, lem:IV, rem:types, prop:ns, lem:h0 by pointing here).
* Chapter 22 (`ch:computation`): 7.3, 7.4, 7.6 (`ns3`, `elldivpol`, `galrep` labels and the CM caveat), 4.4 (the factor $1+2X$ at $2$),
  6.2.

## 6. Notes for the writer

### 6.1 Conventions to typeset (Section 1, as `convention` environments)
* C1 to C7 of Part 1. Name the Frobenius every time in a display ($\Frob_q$ arithmetic, $\Frob_q^{-1}$ geometric); the Tate matrices
  and the conjugation actions use $\Frob_q$; the "action on $(\ad V)^{I_q}$" in 4.1 is the same for both, except at multiplicative
  primes (3.2(v): $q$ versus $q^{-1}$), which is exactly important_notes.md point 11.
* Macros: `\ad` is $\operatorname{ad}^0$, `\Sym` is $\operatorname{Sym}^2$, `\Ns` prints 3Ns, `\Phig` is the geometric component group (the paper's
  notation); use `\Phig_q` for $\Phi_q(\bar\F_q)$ throughout (C2; Appendix B, B-C11(b)). There is no `\O` macro: write `\mathcal{O}`.
* Labels: `def:galrep:...`, `thm:galrep:...`, `lem:galrep:...`, `prop:galrep:...`, `ex:galrep:...`, `rem:galrep:...`, `conv:galrep:...`,
  `cor:galrep:...`; the paper's lemmas proved here get the paper's name in the optional argument, e.g.
  `\begin{lemma}[the paper's Lemma lem:IV]\label{lem:galrep:IV}`.

### 6.2 Pitfalls
* **The paper's lemmas in corrected form.** State Lemma lem:h0 as 8.5 (not "for $E$ without CM it is finite"), Proposition prop:ns as 8.3
  (no CM hypothesis, $\Ind\psi$ over $\F_9$, the commutator step), Remark rem:types as 4.5 (complete grouping). In a `paperlink` quote the
  paper's sentence and the correction; never silently change the paper's statement.
* **Component group lemma (2.2).** It is for $q\ne\ell$ and distinguishes additive from multiplicative reduction; for good reduction
  $E[\ell^k]^{I_q}=E[\ell^k]$. It uses $\Phi_q(\bar\F_q)$, not $c_q=\#\Phi_q(\F_q)$; the Frobenius-invariant version gives $E(\Q_q)[\ell^\infty]$ only for additive
  reduction. Prove it through finite unramified extensions (the union over them is $\Q_q^{\mathrm{ur}}$, which is not complete).
* **Type IV at 2 (4.4).** The proof needs only Lemma 2.2, the fact that types $\mathrm{IV}$, $\mathrm{IV}^*$ are potentially good ($v_2(j)\ge0$; Chapter 10),
  and the injectivity of reduction on finite subgroups of $\GL_2(\Z_3)$. Do not invoke Kraus at $q=2$. The conclusion is about types
  $\mathrm{IV}$ and $\mathrm{IV}^*$ only: types $\mathrm{II}$, $\mathrm{III}$ at $2$ have various inertia groups (4.6).
* **Tame versus $q\ge5$.** "Tame since $q\ne3$" (Lemma lem:IV) means: the image has order $3$, prime to $q$. At $q=2$ an image of order $3$ is tame;
  at $q=3$ it is wild. Say "the order is prime to $q$", not "$q\ge5$", where that is what is used.
* **The corner of the Tate matrix is $\varepsilon\kappa$** (important_notes.md point 42); $\varepsilon(\Frob_q)=a_q(E)$; on inertia $\varepsilon=1$.
* **$n_q$ versus the index of a Kodaira symbol.** $n_q=v_q(\Delta_{\min})=-v_q(j)$ at a multiplicative prime; at a potentially multiplicative additive
  prime use $-v_q(j)$; at $q=2$ the index $m$ of $\mathrm I_m^*$ is not $-v_2(j)$ in general (3.4).
* **Irreducible and absolutely irreducible.** For $\bar\rho_{E,\ell}$, $\ell$ odd, they agree (1.4(i)); for its restriction to $G_{\Q(\sqrt{\ell^*})}$ they do not
  (the 3Ns case: $C_4$ on $\F_3^2$ is irreducible, not absolutely irreducible). Never write "$\bar\rho|_{G_{\Q(\sqrt{-3})}}$ is reducible" in the 3Ns case.
* **Dihedral is not the excluded case.** 3Nn images are dihedral (induced from another quadratic field) and satisfy the hypothesis of
  Theorem thm:main; only "induced from $\Q(\sqrt{\ell^*})$" is excluded. For $\ell\ge5$, $\ell\nmid N$, that never happens (8.2).
* **$\chi_\ell$ versus $\chi_{\ell^*}$.** $\bar\chi_\ell=\chi_{\ell^*}$ only for $\ell=3$; $h_\ell$ concerns $\bar\chi_\ell$, the hypothesis of Theorem thm:main concerns $\chi_{\ell^*}$
  (important_notes.md points 5, 6).
* **Labels.** Always give the intrinsic description with a label; 3Cs.1.1 is not the split Cartan subgroup (point 44); 3B.1.1 versus
  3B.1.2 depends on a convention, fixed here by the data (rational point of order $3$ for 3B.1.1). `ecdata`'s `galrep` files omit the
  label when the image is the one forced by CM (Part 6.6): say so wherever counts are quoted.
* **$N_s(\F_3)$ is not maximal** (point 2); do not import the large-$\ell$ picture of maximal subgroups.
* **Serre conductor versus conductor.** $a_p(\bar\rho)\le f_p$ with the defect $\dim\Phig_p[\ell]$ (6.2); a twist can lower one and not the other (4.5(b)).
* **Supersingular at $\ell$.** For $\ell\ge5$, $\ell\mid a_\ell$ means $a_\ell=0$ (Hasse); for $\ell=3$, $a_3\in\{0,\pm3\}$. The inertia description in 5.3(ii) is
  over $\F_{\ell^2}$.
* **Theorem numbers.** Only cite numbers marked as sure: none in this outline is fully sure except those the paper itself
  cites (DDT Theorem 3.15, DDT Theorem 3.1(e), Edixhoven92 Section 2, Zywina15 and Sutherland16 by name); everything marked
  "(verify)" must be checked or replaced by a section reference (SilvermanAEC VII.7 Theorem 7.1; Serre-Tate 1968 Theorem 1 and
  Section 2 corollaries; Serre72 propositions on fundamental characters and Section 5; Serre87 Sections 1.2, 2, 4; Sutherland16
  Section 6).

### 6.3 What to leave to other chapters
* Chapter 1: the group theory of $\GL_2(\F_3)$ and Dickson's theorem (cite).
* Chapter 4: all representation theory (Clifford, Brauer-Nesbitt, induced representations over $\F_9$, the length lemma 10.5, the
  shapes on $V$ and $\ad V$); here only the Galois input.
* Chapter 5: continuity, complex conjugation, restriction and index-two arguments, Chebotarev, Kummer cocycles.
* Chapter 6: $\Z_3[\zeta_3]$, the commutant and $\chi_{-3}(q)$, $\chi_{-4}(q)$ actions, CM and $a_p=0$.
* Chapter 7: tame inertia and the tame relation, Kummer classes on inertia, Weil-Deligne representations, $L$-factors, Swan and Artin
  conductors, the shapes table (its Kodaira column is supplied by 3.2, 3.4, 4.1, 4.4 here).
* Chapter 9: $\psi_3$, Weil pairing, isogenies, torsion, the no-$27$-isogeny proof (restated in 9.2 by `\Cref`), twists of models.
* Chapter 10: minimal models, Tate's algorithm, Kodaira types, component groups, Ogg's formula, the Tate curve itself, Kraus's theorem,
  Lemma lem:twist (i), (ii), Remark rem:wild. Chapter 11 does not reprove Kraus; it proves what follows from it.
* Chapter 15: newforms, local-global compatibility, the optimal-level theorem in general and its proof, Lemma lem:old and Theorem
  thm:qual (here only the local inputs and the elliptic-curve specialisation).
* Chapter 18: Lemma lem:tamfactor and the Selmer-group reading of Lemma lem:h0; Chapter 19: $L_q(A_f,s)$, $P_q$, $e_\ell(E,q)$, Lemma lem:euler in
  full; Chapter 22: PARI usage.

### 6.4 How each relevant point of important_notes.md is handled
* **Point 1** (prop:ns, "non-abelian and faithful"): 8.3 step (4) supplies the commutator step (Chapter 1, 5.7) or Maschke for $Q_8$ (Chapter 4,
  3.7); `paperlink`.
* **Point 5** (lem:h0 finiteness; $h_\ell\le1$): 8.5 states and proves the corrected lemma ($h_\ell=0$ for $\ell\ge5$, $h_3\le1$, with or without CM);
  remark (a); Exercise 11.
* **Point 6** (criterion for $h_\ell>0$ uses $\bar\chi_\ell$): 8.5 remark (b), with the sharpening of 8.2 ($\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ for $\ell\ge5$ needs
  $\ell\mid N$).
* **Point 8** (lem:tamagawa-exp: notation, "up to units"): 3.3 proof 1 written with $q_E$ and the two separate steps; Chapter 7, 6.2(v).
* **Point 9** (prop:ns: CM hypothesis unused): 8.3 and 7.3 are stated for every $E/\Q$; data include the $26$ CM curves with image $N_s(\F_3)$.
* **Point 10** (irreducible versus absolutely irreducible in lem:old and lem:h0): 1.4(i), (iii); 8.5 remark (d).
* **Point 11** (geometric versus arithmetic Frobenius): C3, 3.2(v), 4.1 (same sign for both), 4.4(iv); the $L$-factors are Chapter 19's.
* **Point 14** (CM by $\Q(\sqrt{\ell^*})$ forces $\ell\mid N$): 8.5 remark (a), citing Chapter 9, 6.5 and Chapter 6, 6.5(vi); not needed for the proof.
* **Point 17** ($\Z/3\oplus\mu_3$ and a point of order $9$ cannot coexist): 9.2 restates Chapter 9, 9.8 in label language.
* **Point 22** (rem:types grouping): 4.5, the complete table, with the addendum on "conductor of $E$" versus "Serre conductor" (Part 7, N4).
* **Point 33** ($\Ind\psi$ over $\F_9$): 8.3 statement and step (6); Chapter 4, 8.2.
* **Point 34** (types $\mathrm{III}$, $\mathrm{III}^*$: the line is spanned by $\tau$): 4.1.
* **Point 42** (corner $\varepsilon\kappa$): 3.2.
* **Point 44** (3Cs.1.1 is not the split Cartan image): 7.3, 7.4, 9.2; Exercise 15.
* **B1** (on $V_\ell E$ the arithmetic Frobenius has eigenvalues $\alpha,\beta$): C3 and 3.1.
* Also: point 2 (7.2, 7.3), point 3 (7.4: labels checked against `ecdata`), point 4 (7.5: Zywina by section), point 12 (4.1), point 13 (4.3),
  point 18 (3.4 covers $q=2$), point 21 (6.3, 10.2: 980i1 illustrates only), point 27 (1.3(iii)), point 32 (C4), point 43 (**settled**:
  4.4).

### 6.5 References and bibliography
`SilvermanAEC`, `SilvermanATAEC`, `SerreAbelian`, `Serre72`, `Serre87`, `Kraus90`, `Zywina15`, `Sutherland16`, `Edixhoven92`, `Carayol89`,
`Ribet90`, `Diamond95`, `DDT`, `KhareWintenberger`, `Mazur77`, `Mazur78`, `Berger`, `ecdata`, `PARI` are in `refs.bib`. Add to `refs.bib`, not
`bib/ch11.bib`, since both are needed by more than one chapter (decision B14; important_notes.md B16, B18; complete entries, checked
against the sources): `SerreTate68` (J.-P. Serre and J. Tate, "Good reduction of abelian varieties", Ann. of
Math. 88 (1968), 492-517) and `Livne89` (R. Livne, "On the conductors of mod $\ell$ Galois representations coming from modular forms",
J. Number Theory 31 (1989), 133-141; check the pages). **Coordinate `SerreTate68` (settled by decision B14: it goes into `refs.bib`):** the Chapter 7 outline adds the same key to
`bib/ch07.bib` and the Chapter 9 outline plans the same work for `bib/ch09.bib`; `main.tex` reads every chapter bib, so a duplicated key
gives a BibTeX "Repeated entry" error in the full build, while `tools/build_chapter.sh 11` reads only `refs.bib` and `bib/ch11.bib`
(Part 7, B2).

### 6.6 Verification log (computations done for this outline)

Scripts `/tmp/ch11/scripts/` (`ec.py`, `inert.py`, `t1.py` to `t10.py`), PARI/GP 2.15 through `cypari2`; data `allcurves`, `galrep`,
`degphi` for conductors $0$ to $9{,}999$ ($64{,}687$ curves) from the `ecdata` GitHub repository.
* Mod $3$ images (7.3, 7.6): for every curve, the factorisation pattern of `elldivpol(E,3)`, `polgalois` of irreducible $\psi_3$, and
  $3\mid\#E(\Q)_{\mathrm{tors}}$, against the `galrep` label. Exact agreement with the table of 7.3; the only unlabelled non-surjective cases are
  the $462$ CM curves ($j\in\{0,1728,-3375,8000,-32768,54000,287496,-884736,-12288000,16581375,-884736000,-147197952000\}$), classified
  from $\psi_3$ (26 with $2+2$, 184 with $D_4$, 154 with a rational root and no label).
* Inertia mod $3$ (2.2, 4.1, 4.5, 4.6): for a prime $q$ of $E$, the fields $\Q(P)$ of the $3$-torsion points (degree up to $8$, from the
  factors of $\psi_3$ of the short model and $y^2=f(x)$ via `rnfequation`), `nfinit([pol,[q]])`, `idealprimedec`; the order of $\bar\rho(I_q)$ is the
  l.c.m. of the ramification indices when tame, and $E[3]^{I_q}\ne0$ iff some prime above $q$ has $e=1$. At $q\ge5$, $12$ curves per type with
  surjective image: $\mathrm I_0^*$: $2$, no fixed point; $\mathrm{II}$, $\mathrm{II}^*$: $6$, none; $\mathrm{III}$, $\mathrm{III}^*$: $4$, none; $\mathrm{IV}$, $\mathrm{IV}^*$: $3$, a fixed
  line; $\mathrm I_n$: $3$ or $1$ as $3\nmid n$ or $3\mid n$, fixed; $\mathrm I_n^*$: $6$ or $2$, none; conductor exponents $2,2,2,2,1,2$. At $q=2$, $40$ per type:
  as in 4.6.
* Type $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ (4.4): all $4{,}750$ curves; $\bar\rho(I_2)$ of order $3$ with a fixed line, $f_2=2$, $v_2(\Delta_{\min})=4$, resp. $8$,
  $v_2(j)\ge0$; `lfunsympow(E,2)` and `lfuneuler(S,2)` on $60$ of them and on 20a1, 980i1, 140b1: $P_2(X)=1+2X$.
* 3Ns curves (8.2, 8.4): all $120$; Kodaira types at all bad primes (`ellglobalred`), $a_p\bmod3$ for $p\equiv2\pmod3$ among the first $80$ primes,
  $a_3\bmod3$, Euler factors at the type $\mathrm{III}$ primes for 726a1, 338d1, 3840h1, 3840h2, 4864b1, 4864c1, 6912d1, 6912j1, and the inertia
  computation at those primes ($\bar\rho(I_p)$ cyclic of order $4$).
* $\ell\ge5$ dihedral images (8.2): every curve with an $\ell$Ns or $\ell$Nn label, $\ell\ge5$: test of $a_p\equiv0\pmod\ell$ at the first $150$ primes inert in
  $\Q(\sqrt{\ell^*})$ and not dividing $N\ell$; the label lists of 7.4.
* Eisenstein (5.4(i), 9.1): every curve with a Borel or split Cartan label at $\ell$, $\ell\nmid N$: $\ell\nmid a_\ell$ ($4{,}571$ pairs); square-free $N$: $a_p\equiv1+p$
  for the first $60$ primes.
* Examples (6.3, 10.2): data of 11a1, 11a2, 11a3, 121a1, 121c1, 121c2, 121d1, 121d2, 77c1, 539c1, 980i1, 140b1, 726a1, 6912d1, 338d1,
  99a1, 20a1, 14a1 (models, conductors, Kodaira codes, discriminants, $j$, modular degrees, labels); congruences 121c1 versus 11a1,
  121a1 versus $\chi_{-11}\cdot$11a1, 77c1 versus 11a1, 539c1 versus $\chi_{-7}\cdot$77c1 mod $3$ for the first $300$ primes; 140b1 versus 20a1
  and 980i1 versus $\chi_{-7}\cdot$20a1 mod $5$ for the first $200$ primes; $y^2=x^3-6x-8$ has conductor $6912$ and is 6912d1, $a_5=3$.
* Not verified: anything beyond conductor $10{,}000$; the theorem numbers of the cited books and papers; the general definition of
  Sutherland's labels against Sutherland16 itself (only against `ecdata`'s use of them).

## 7. Points for important_notes.md

### 7.1 New points about the paper (not among points 1 to 45 and B1 to B9; each checked as stated)

**N1. Proposition prop:forms, Remark rem:wild, Section sec:wild: the type $\mathrm{IV}$, $\mathrm{IV}^*$ case at $2$ is a theorem (settles
important_notes.md point 43).** Location: Proposition prop:forms ("except possibly when $\ell=3$ and $E$ has type $\mathrm{IV}$ or $\mathrm{IV}^*$
at $2$, where they hold as soon as $e_3(E,2)\ge1$ ... PARI's factor at $2$ is $1+2X$ for every one of them"), Remark rem:wild, Section
sec:wild. Problem: the paper leaves as an exception, verified only numerically, a case that has a short proof. Fix: for additive
reduction at $q\ne\ell$, $E[\ell]^{I_q}\simeq\Phi_q(\bar\F_q)[\ell]$ (the prime-to-$q$ torsion of $E_0(\Q_q^{\mathrm{ur}})$ is trivial and $E_0$ is $\ell$-divisible);
types $\mathrm{IV}$, $\mathrm{IV}^*$ have $\Phig_2\simeq\Z/3$ and potentially good reduction, so $E[3]^{I_2}$ is a line, $\bar\rho_{E,3}(I_2)$ is the unipotent group of
order $3$, and $\rho_{E,\ell}(I_2)$ is cyclic of order $3$ for every odd $\ell$ (finite subgroups of $\GL_2(\Z_3)$ inject mod $3$; independence of $\ell$,
Serre-Tate). The image is tame, Frobenius at $2$ inverts it ($2\equiv-1\bmod3$), and the proof of Lemma lem:euler for types
$\mathrm{IV}$, $\mathrm{IV}^*$ applies verbatim: $L_2(A_f,s)^{-1}=1+2^{-s}$, $P_2(X)=1+2X$, $e_3(E,2)=v_3(3/2)=1$ (and $e_\ell(E,2)=0$ for $\ell\ge5$). So
Proposition prop:forms holds with no exception under the hypothesis of Theorem thm:main (and under Conjecture conj:euler with
$h_\ell=0$). Also $f_2=2$, and the Serre conductor of $\bar\rho_{E,3}$ has exponent $1$ at $2$, so the proof of Theorem thm:qual (a) works at $q=2$ as
well (with $3\nmid N$, $\bar\rho$ irreducible and not 3Ns): its hypothesis "$q\ge5$" can be weakened to "$q\ne3$" in case (a). Confidence: high
(proof above, item 4.4; all $4{,}750$ curves with type $\mathrm{IV}$ or $\mathrm{IV}^*$ at $2$ and conductor below $10{,}000$ checked: inertia mod $3$ of order $3$
with a fixed line, $f_2=2$; $P_2=1+2X$ on more than $60$ of them, including 20a1 and 980i1). Importance: medium (removes an exception from a proposition).

**N2. Theorem thm:main and Section sec:forms: for $\ell\ge5$, $\ell\nmid N$, the hypothesis on $\Q(\sqrt{\ell^*})$ is implied by irreducibility.**
Location: the hypothesis of Theorem thm:main (and the abstract), Section 4.2 ($S_f$), Section sec:forms ("the hypothesis of Theorem
thm:main fails ... for the curves whose mod $\ell$ representation is induced from $\Q(\sqrt{\ell^*})$ with $\ell\ge5$, which we did not single
out"). Problem: not an error, an unstated simplification. If $\ell\nmid N$ and $\bar\rho_{E,\ell}\simeq\bar\rho_{E,\ell}\otimes\chi_{\ell^*}$, restrict to inertia at $\ell$:
$\chi_{\ell^*}|_{I_\ell}=\omega^{(\ell-1)/2}$, while $\bar\rho|_{I_\ell}^{\mathrm{ss}}$ is $\omega\oplus1$ (ordinary) or $\omega_2\oplus\omega_2^\ell$ (supersingular); comparing the
characters forces $\ell=3$ and ordinary reduction at $3$. Hence for $\ell\nmid 2N$: $\ell\notin S_f$ iff $E[\ell]$ is irreducible and, if $\ell=3$, the
image is not 3Ns (equivalently $h_\ell(E)=0$). The curves "induced from $\Q(\sqrt{\ell^*})$ with $\ell\ge5$" in Section sec:forms all have $\ell\mid N$,
so they are already among the curves with $\ell\mid N$; and the 3Ns curves with $3\nmid N$ are ordinary at $3$. Fix: state the hypothesis of
Theorem thm:main as "$\ell\nmid2N$, $E[\ell]$ irreducible, and the image of $\bar\rho_{E,3}$ not the normaliser of a split Cartan subgroup if $\ell=3$", with
this argument (or a reference, if DFG04 or DDT record it), and delete or reword the "did not single out" clause. Confidence: high (the
inertia description is Serre72, Section 1; data: the $24$ curves below conductor $10{,}000$ with $\bar\rho_{E,\ell}\simeq\bar\rho_{E,\ell}\otimes\chi_{\ell^*}$, $\ell\ge5$, all have
$\ell\mid N$; all $62$ curves with image 3Ns and $3\nmid N$ have $3\nmid a_3$). Possibly known in the literature; not stated in the paper.

**N3. Section sec:anomaly: the observations on the 3Ns curves are theorems.** Location: Section sec:anomaly ("Conversely every $\Ns$ curve
of the tables has a prime of type $\mathrm{III}$ or $\mathrm{III}^*$ with a positive term $e_3$"; "The residue classes of the type $\mathrm{III}$ primes
of the violating curves are $q\equiv1$ and $q\equiv11\pmod{12}$ in comparable numbers, with some $q=2$"), and the appendix (726a1: "the type
$\mathrm{III}$ term and the correction cancelling"). Problem: presented as data; they follow from the image. If $\bar\rho_{E,3}(G_\Q)=N_s(\F_3)$, then
for $p\ne3$ the image of $I_p$ lies in $N_s\cap\SL_2(\F_3)=C_4$; the quadratic fields $K_1$, $K_2$ of the two factors of $\psi_3$ differ from $\Q(\sqrt{-3})$, so
some prime $p\ne3$ ramifies in them, and exactly at such $p$ the image of inertia is cyclic of order $4$ (types $\mathrm{III}$, $\mathrm{III}^*$ when
$p\ge5$; every type $\mathrm{III}$, $\mathrm{III}^*$ prime $p\ge5$ is of this kind); $\bar\rho(\Frob_p)$ commutes with the image of inertia iff its determinant
$p$ is $1$ mod $3$, which forces $\chi_{-4}(p)=\chi_{-3}(p)$, i.e. $p\equiv1$ or $11\pmod{12}$, and $e_3(E,p)=v_3(p-\chi_{-3}(p))\ge1$; at $p=2$ the same argument
gives $P_2=1+2X$ and $e_3(E,2)=1$. Also every multiplicative prime $p\ne3$ of a 3Ns curve has $3\mid n_p$ (so $t_3(E,p)\ge1$), and no prime $p\ge5$ has
type $\mathrm{II}$, $\mathrm{II}^*$, no prime $p\ne3$ type $\mathrm{IV}$, $\mathrm{IV}^*$. Fix: add a sentence or a short proposition in Section sec:boundary (item 8.4 of
the Chapter 11 outline). Confidence: high (proof; all $120$ 3Ns curves below conductor $10{,}000$ agree: $100$ have type $\mathrm{III}$ or
$\mathrm{III}^*$ primes $\ge5$, all $\equiv1$ or $11\pmod{12}$, the other $20$ have cyclic inertia of order $4$ at $2$, of Kodaira type $\mathrm{III}$ or $\mathrm{III}^*$
there, with $P_2=1+2X$). The Kodaira type at $2$ of such a prime is not determined by the argument (observed: $\mathrm{III}$ or $\mathrm{III}^*$ with
$f_2=8$). Importance: low to medium (explains the anomaly section; strengthens Remark rem:ns).

**N4. Remark rem:types, last sentence (addendum to important_notes.md point 22): "these are the types whose twist by $\chi_q$ lowers
the conductor exponent".** Problem: for $\mathrm{II}$, $\mathrm{II}^*$ the twist (to $\mathrm{IV}^*$, $\mathrm{IV}$) does not lower the conductor exponent of $E$
(both are $2$); it lowers the Serre exponent of $\bar\rho_{E,3}$ (from $2$ to $1$). For $\mathrm I_n^*$ and $\mathrm I_0^*$ both exponents drop. Fix: "whose twist by
$\chi_{q^*}$ lowers the Serre conductor exponent of $\bar\rho_{E,3}$ at $q$: $\mathrm{II}$, $\mathrm{II}^*$, $\mathrm I_n^*$, and also $\mathrm I_0^*$" (the last omission is point 22 /
Chapter 21's N8). Confidence: high (table 4.5). Importance: low (expository).

No other new problem was found in this chapter's area. Checked and found correct (beyond the points already recorded): Lemma
lem:tamagawa-exp (both directions, split and nonsplit; also by the component-group route); Lemma lem:IV (statement and proof,
modulo point 13); the inertia descriptions in Lemma lem:euler for $q\ge5$ (orders, generators, Frobenius signs; modulo points 11, 12,
34); Remark rem:types for the types it lists; the list of images and the orbit argument in Proposition prop:ns (modulo points 1, 9,
33); the trace-zero argument and the length description in Lemma lem:h0 (modulo points 5, 6, 10); the claims of the optimal-level
paragraph ("good" at $\ell$, $N(\bar\rho)\mid N$, prime to unramified primes); the local analysis in Lemma lem:old at $p=\ell$ and at $p\,\|\,N$
("both non-split because $\bar\rho$ is ramified": by 3.3(iii)); the numerical check of Section sec:anomaly (valid, see 8.5 remark (c));
Section sec:eis's labels 3B.1.1 and 3Cs.1.1 as used (modulo point 44); the congruences of the Example of Section 3.

### 7.2 Book-internal inconsistencies

* **B1. PLAN.md, Chapter 11 entry: "finiteness for non-CM curves via $a_p=0$ at inert primes".** PLAN.md repeats the paper's argument
  for Lemma lem:h0, which important_notes.md point 5 shows to be wrong (it confuses $\chi_\ell$ with $\chi_{\ell^*}$). This outline follows point 5
  (item 8.5); PLAN.md need not change, but the Chapter 11 writer must not follow its wording. (Likewise PLAN.md's Chapter 11 entry
  lists rem:types in the paper's incomplete grouping; item 4.5 gives the complete one.)
* **B2. The bibliography key `SerreTate68`.** The Chapter 7 outline adds it to `bib/ch07.bib`, the Chapter 9 outline plans "Serre-Tate
  1968" for `bib/ch09.bib`, and this chapter needs it in `bib/ch11.bib` (Chapter 10 will too). `main.tex` reads all chapter bib files, so
  one key in several files is a "Repeated entry" error in the full build, while each standalone build (`tools/build_chapter.sh`) reads
  only `refs.bib` and its own file. Action for the orchestrator: decide once (an exception adding the entry to `refs.bib`, or a rule
  that only the first chapter defines a shared key and the full build is the reference).
* **B3. Chapter 7 outline, item 9.5(ii) and its point N2; Chapter 21 outline, items A1.8 and A2.6.** They treat the cyclicity of the
  inertia image for types $\mathrm{IV}$, $\mathrm{IV}^*$ at $2$ as an unverified assumption and keep the exception of Proposition prop:forms. Item 4.4
  proves it; the Chapter 7, 19 and 21 writers should cite `\Cref{ch:galrep}` and drop the hedge.
* **B4. important_notes.md point 6 and the Chapter 21 outline, A1.5 commentary.** Both say that for $\ell\ge5$ "$\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ can occur
  (the case excluded by $S_f$)". True only when $\ell\mid N$ (item 8.2); in the range $\ell\nmid N$ of Theorem thm:main it never occurs. Not a
  contradiction, but the Chapter 21 writer should add "(only when $\ell\mid N$)".
* **B5. Chapter 10 and Chapter 11 on the Tate curve.** PLAN.md gives Chapter 10 the statement of $E_q[\ell^t]$ and Chapter 11 its
  representation-theoretic consequences (Lemma lem:tamagawa-exp). If the Chapter 10 outline (written in parallel) also proves the
  matrix shape or Lemma lem:tamagawa-exp, one of the two must cite the other; this outline keeps both proofs of lem:tamagawa-exp
  here, as PLAN.md requires.
* **B6. Chapter 4 outline, table 9.3, and Chapter 7 outline, table 9.4: the "Kodaira types" column.** Both defer it to Chapters 10 and
  11; it is supplied by items 3.2, 3.4, 4.1, 4.4 here and agrees with both tables (no conflict). The mod $3$ column of Chapter 4's table
  ("$\mathrm I_n$: $1$ if $3\nmid n$, $2$ if $3\mid n$") agrees with 2.2 and 4.5.
* **B7. Counts of mod 3 images.** The Chapter 9 outline quotes "the $264$ curves of conductor below $10{,}000$ with image 3Cs.1.1"; this
  outline splits them as $262$ non-CM plus $2$ CM (27a1 and 27a3), consistent; Chapter 22 should quote counts with the CM caveat of
  7.3 (`galrep` omits the labels forced by CM).
