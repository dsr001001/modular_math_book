# Appendix B: Notation, conventions and index of symbols (`ch:notation`, `chapters/chB_notation.tex`)

Stage 1 output for Appendix B. Target length of the LaTeX appendix: 400 to 800 lines (PLAN.md Section 7.3); the plan in
Part 4 aims at about 750.

This file is the **specification of the book-wide conventions**. Part 1 fixes every convention that more than one chapter
needs, each as a boxed statement (to be typeset as a `convention` environment) with its reason and the chapters it
binds. Part 2 is the index of symbols. Part 3 lists every place where an outline (Chapters 1 to 19 and 21, as they stand
on 14 October 2026) disagrees with Part 1, with the change needed. Part 4 is the section plan of the appendix and the
notes for its writer. Part 5 records what could not be settled here.

Sources read: PLAN.md (in full, in particular the Appendix B entry and Section 7), the paper `note_Oct10_7pm.tex` (in
full), `important/important_notes.md` (in full; the book-internal notes B1 to B23 and points 5, 6, 7, 11, 23, 26, 29,
30, 32, 37, 40, 42, 52, 70), and the outlines `outlines/ch01_groups.md` to `outlines/ch21_paper.md`: their global
convention sections and writer notes in full, their item lists, and every line found by a systematic search for
`Frob`, `\Phi`, `^*`, `^\vee`, `dagger`, `chi_`, `c^2`, `Petersson`, `\omega`, `A_f`, `\varphi`, `\phi`, `\pi`,
`h^{(p)}`, `n+4` (the search scripts and their raw output were kept in the session scratchpad; the counts are in Part 3).
Chapters 20 (`ch:congruence`) and 22 (`ch:computation`) are being outlined at the same time; their symbols are taken
from PLAN.md and the paper and cited by chapter label only.

How items are cited. "ch:local 5.4" is item 5.4 of the Chapter 7 outline; Chapters 5 and 16 name items by label stems
("ch:galois galois:cyclotomic-character", "ch:cohomology model-setting"); Chapter 21 by its A-numbers and C1 to C3; a
convention of an outline by its own name ("ch:rings C5", "ch:local L3", "ch:reduction R4"). "B-C4" is convention 4 of
Part 1 below. In the LaTeX appendix the item numbers are replaced by `\Cref{ch:slug}` only (PLAN.md 7.1).

Typography of this file: ASCII; LaTeX in `$...$` as in the other outlines; no dash ligatures of any kind; table rules
with single hyphens.

________________________________________________________________________________

## Part 1. Book-wide conventions

Each convention has: the **boxed statement** (to be typeset verbatim, up to LaTeX markup, as a `convention` environment
in the appendix, and quoted or cited by the chapters), the **reason**, the **chapters bound**, and the **changes**
(pointers to Part 3). Where an outline already fixed the convention, the source is named; nothing below contradicts a
decision recorded in important_notes.md.

### B-C1. Letters for primes, and the collisions of $q$ and $\ell$

> **Convention B-C1.** $p$, $q$, $\ell$ denote primes. $\ell$ is the coefficient prime (odd in every use of the paper);
> $q$ is a bad prime of $E$ ($q\mid N$); $p$ is any prime. $\ell^*=(-1)^{(\ell-1)/2}\ell$ and $q^*=(-1)^{(q-1)/2}q$ for odd
> $\ell$, $q$. The letter $q$ also denotes: the size of a finite field $\F_q$ (Chapters 1, 2, 7, 9: when not prime, Chapter 9
> writes $\mathfrak q$); the variable $q=e^{2\pi iz}$ of $q$-expansions (Chapters 12, 13, 14); the variable of the Tate curve,
> written $\mathsf q$ (Chapter 10). The Tate parameter of $E$ is always $q_E$, never $u$ and never $\mathsf q$ alone. A chapter that
> uses two of these meanings says so in its first convention box and never puts two of them in one display.

Reason: the paper uses $q$ for bad primes and for $q$-expansions; Chapters 1, 2, 7, 10, 12 each found the collision
independently (ch:groups C4, ch:rings C2, ch:local L1, ch:reduction R1, ch:modforms C1). Chapters bound: all.
Changes: none (all outlines comply).

### B-C2. Frobenius: arithmetic $\Frob$, geometric $\Phi$

> **Convention B-C2 (Frobenius).**
> (a) $\Frob_p$ (or $\Frob$ when the prime is clear) is an **arithmetic** Frobenius at $p$: an element of a decomposition
> group $D_p\simeq G_{\Q_p}$ inducing $x\mapsto x^p$ on the residue field, well defined modulo $I_p$ and up to conjugation.
> It acts on $\mu_n$ ($p\nmid n$) by $\zeta\mapsto\zeta^p$, so $\chi_\ell(\Frob_p)=p$ for $\ell\ne p$. For a finite field $\F_q$,
> $\Frob_q\in\Gal(\overline\F_q/\F_q)$ is $x\mapsto x^q$.
> (b) $\Phi_p=\Frob_p^{-1}$ (or $\Phi$) is the **geometric** Frobenius. An eigenvalue $\lambda$ of $\Frob$ is the eigenvalue
> $\lambda^{-1}$ of $\Phi$. Where component groups $\Phi_q(\cdot)$ (B-C11) occur in the same chapter (Chapters 10, 11, 21, 22),
> the geometric Frobenius at a named prime is written $\Frob_q^{-1}$, never $\Phi_q$; $\Phi$ without subscript is always the
> geometric Frobenius of a local field. $\Frob^{\mathrm{geom}}$, $\Frob^{\mathrm{arith}}$ and "$\Frob_p$, the geometric
> one" are not used.
> (c) **Group theory and cohomology use $\Frob$**: the tame relation, conjugation actions on $H^1(I_p,-)$, unramified
> cohomology $H^1_{\mathrm{ur}}=M^{I}/(\Frob-1)M^{I}$, the Tate matrices of Lemma lem:tamfactor, Frobenius on Kummer
> classes. This binds Chapters 4, 5, 6, 7, 11, 16, 17, 18 and the commentary of Chapter 21.
> (d) **$L$-factors use $\Phi$**: for a representation $M$ of $G_{\Q_p}$ on a finite-dimensional $\Q_\ell$-space ($p\ne\ell$),
> $$L_p(M,s)=\det\bigl(1-\Phi_p\,p^{-s}\bigm|M^{I_p}\bigr)^{-1},$$
> so $L_p(\Q_\ell(1),s)=(1-p^{-1-s})^{-1}$ and $L_p(M(n),s)=L_p(M,s+n)$. The paper's $L_p(A_f,s)$ (Section 1.1), the table of
> Section 1, the proof of Lemma lem:euler, Lemma lem:fpr and the sentence "$\det(1-\Frob_p\mid(V^D)^{I_p})=L_p(A_f,1)^{-1}$"
> after Lemma lem:dfg21 are read with $\Phi$; the proof of Lemma lem:tamfactor is read with $\Frob$ (important_notes.md
> point 11). DFG04 1.7.2 uses the geometric convention for $L$-factors.
> (e) **The tame relation.** For a topological generator $t$ of the tame (or pro-$\ell$ tame) inertia quotient of $G_{\Q_q}$:
> $$\Frob\,t\,\Frob^{-1}=t^{q},\qquad\text{equivalently}\qquad\Frob^{-1}t\,\Frob=t^{q^{-1}}\ (q^{-1}\in\Z_\ell),\qquad\Phi\,t\,\Phi^{-1}=t^{q^{-1}}.$$
> The paper's "$\Frob^{-1}t\Frob=t^{q^{-1}}$" is the second form, with the arithmetic Frobenius.
> (f) **The Weil-Deligne relation.** With $\|w\|=q^{d(w)}$, $w|_{K^{\mathrm{ur}}}=\Frob^{d(w)}$ (so $\|\Frob\|=q$, $\|\Phi\|=q^{-1}$,
> $\|w\|=\chi_\ell(w)$ for $\ell\ne p$), a Weil-Deligne representation $(r,N)$ satisfies
> $$r(w)\,N\,r(w)^{-1}=\|w\|\,N,\quad\text{that is}\quad r(\Frob)\,N\,r(\Frob)^{-1}=q\,N,\quad r(\Phi)\,N\,r(\Phi)^{-1}=q^{-1}N.$$
> (PLAN.md's "$\Frob N\Frob^{-1}=p^{-1}N$" is the geometric form with the wrong name, important_notes.md B6.)
> (g) **Frobenius endomorphisms and the Artin map.** The $q$-power Frobenius morphism of a curve or abelian variety over
> $\F_q$ is $\pi_q$ (or $\pi$); it acts on $\overline\F_q$-points as $\Frob_q$ and on $T_\ell$ as $\Frob_q$; its dual isogeny
> (Verschiebung) is $\hat\pi_q=q\pi_q^{-1}$. The Eichler-Shimura relation reads $(T_p)_*=\pi_p+\hat\pi_p$ on $J_0(N)_{\F_p}$. The
> local Artin map sends a uniformiser to an arithmetic Frobenius (ch:ant 5.6, ch:local 6.5); sources that send it to the
> geometric one (Deligne) are flagged where cited.

Reason: (a) to (e) are the decisions of ch:galois C2, ch:ant 3.7, ch:local L3, L4, L6, 4.3, 5.4, 8.2, ch:galrep C3,
ch:cohomology (opening conventions and writer note 2), ch:galcoh C2, ch:blochkato C3, ch:lfunctions C2, C3, and
important_notes.md points 11, B6. The only new decisions are the clash rule in (b) (the paper's $\Phi_q$ is the component
group, B-C11) and the notation $\pi_q$, $\hat\pi_q$ in (g), which removes $V=pF^{-1}$ (clash with $V=V_\ell E$) from Chapter 14 and
$\phi_q$ (clash with $\phi_f$, $\varphi_E$) from Chapters 8 and 9.
Chapters bound: 4 to 11, 14 to 19, 21, 22.
Changes: Part 3, entries F1 to F9, and P1, P2, P5 (PLAN.md).

### B-C3. Which Frobenius has the eigenvalues $\alpha$, $\beta$

> **Convention B-C3.** Let $E/\Q$ have good reduction at $p\ne\ell$, $V=V_\ell E$, $a_p=p+1-\#\tilde E(\F_p)$, and let $\alpha,\beta$ be
> the roots of $X^2-a_pX+p$ (so $\alpha+\beta=a_p$, $\alpha\beta=p$, $|\alpha|=|\beta|=\sqrt p$).
> (a) On $V=V_\ell E$ the **arithmetic** Frobenius has characteristic polynomial $X^2-a_pX+p$, eigenvalues $\alpha,\beta$; the
> geometric one has $\alpha^{-1}=\beta/p$, $\beta^{-1}=\alpha/p$ (a different set).
> (b) On $V^\vee=H^1(E_{\overline\Q},\Q_\ell)\simeq V(-1)$ the **geometric** Frobenius has eigenvalues $\alpha,\beta$ (and trace $a_p$).
> (c) Hence $L_p(E,s)=(1-a_pp^{-s}+p^{1-2s})^{-1}=L_p(V^\vee,s)$, while $L_p(V,s)=L_p(E,s+1)$. The same holds for
> $\rho_{f,\lambda}$ normalised by $\det(X-\rho_{f,\lambda}(\Frob_p))=X^2-a_p(f)X+p$: $L_p(f,s)=L_p(V_\lambda(f),s-1)$.
> (d) On $\ad V$ both Frobenii have the eigenvalues $\alpha/\beta,1,\beta/\alpha$ (an inversion-stable set), so the good factor
> $L_p(A_f,s)^{-1}=(1-\frac\alpha\beta p^{-s})(1-p^{-s})(1-\frac\beta\alpha p^{-s})$ does not depend on the convention; neither do the
> lines on which Frobenius acts by $\chi_{-3}(q)$ or $\chi_{-4}(q)=\pm1$. It does at a multiplicative prime: on $(\ad V)^{I_q}$
> the arithmetic Frobenius acts by $q$, the geometric one by $q^{-1}$, and only the latter gives the paper's $1-q^{-1-s}$.
> (e) In Lemma lem:old the paper's $\alpha_p,\beta_p$ are the roots of $X^2-a_p(h)X+p$ for the newform $h$; they are the $U_p$
> eigenvalues of the $p$-stabilisations $h-\beta_ph(pz)$, $h-\alpha_ph(pz)$ (ch:hecke 7.1).

Reason: important_notes.md B1, B7, B9; ch:ellcurves C5, 5.7; ch:local 8.2(v); ch:galrep C3; ch:modgalrep C2;
ch:blochkato C3; ch:lfunctions C2; ch:curves C7. Chapters bound: 6, 7, 8, 9, 11, 13, 14, 15, 18, 19, 21.
Changes: Part 3, F1, F2 (Chapter 21, convention C2(b)), F5.

### B-C4. Duals, adjoints, pullbacks

> **Convention B-C4 (one symbol for each kind of dual).**
> (a) **Linear dual** $M^\vee=\Hom_R(M,R)$ ($R=\Z$, $\Z_\ell$, $\mathcal O$, $\Q_\ell$, a field); for a representation, the
> contragredient $V^\vee$ with $(g\lambda)(v)=\lambda(g^{-1}v)$. Never $M^*$, never $M'$.
> (b) **Pontryagin dual** $X^*=\Hom_{\mathrm{cont}}(X,\Q_\ell/\Z_\ell)$ (or $\Hom(X,\Q/\Z)$ for a finite group), for $X$ finite,
> compact (finitely generated over $\Z_\ell$) or discrete $\ell$-primary. This is the paper's ${}^*$ in Lemma lem:dfg21.
> (c) **Kummer (Cartier) dual** $M^D$: for a lattice or vector space, $M^D=\Hom(M,\Z_\ell(1))=M^\vee(1)$ (resp. $\Hom(V,\Q_\ell(1))$);
> for a finite or discrete $\ell$-primary module, $M^D=\Hom(M,\mu_{\ell^\infty})=M^*(1)$. Hence $V^D=V^\vee(1)$ and $W^D=T^*(1)$ for
> $W=T\otimes\Q_\ell/\Z_\ell$. In the paper (Section 4.2) and in Chapters 18, 20, 21 the symbols $T^D,V^D,W^D$ are built from the
> **adjoint** lattice $A=\ad T$: $T^D=\Hom(A,\Z_\ell(1))\simeq A(1)$, not $\Hom(T_\ell E,\Z_\ell(1))$ (index, entry $T^D$).
> (d) **Adjoint of an operator** $A$ for a pairing $\langle\ ,\ \rangle$: $A^\dagger$, defined by $\langle Ax,y\rangle=\langle x,A^\dagger y\rangle$
> (Petersson product, cup product, abstract perfect pairings alike). Never $A^*$.
> (e) **Pullback and pushforward** along a morphism or correspondence: $\varphi^*$, $\varphi_*$, $\mathcal C^*$, $\mathcal C_*$, and for
> $t\in\T$ the two actions $t^*$ (on $H^1$, $S_2$, $H^0(\Omega^1)$) and $t_*$ (on $H_1$, $J_0(N)$, $T_\ell J_0(N)$) of ch:moddeg C2. A
> star after the name of a **map** is a pullback; a star after the name of a **module** is a Pontryagin dual. Every other
> star is one of the fixed exceptions listed in the index (Kodaira symbols $\mathrm{II}^*$ etc., $q^*$, $\ell^*$, $\mathfrak H^*$,
> $E_2^*$, the dual Selmer structure $\mathcal L^*$ of ch:galcoh 8.2).
> (f) **Transpose** of a matrix: $A^{\mathsf T}$ (ch:modules C8) or $A^t$; of a correspondence: $\mathcal C^t$ (ch:curves C4).
> **Dual isogeny**: $\hat\varphi$; dual abelian variety: $A^\vee$ (so $E^\vee=E$ via the principal polarisation).

Reason (important_notes.md B4, B22). The current usage:

| outline | linear dual | Pontryagin dual | Kummer dual | adjoint of an operator | pullback |
|-|-|-|-|-|-|
| ch:modules (3) | $M^\vee$ (C3) | $M^*$ (8.1, 8.2) | $T^D$ (C3) | $A^*$ (9.5) | none |
| ch:reps (4) | $V^\vee$ (C2) | reserved $^*$ | none | none | none |
| ch:curves (8) | $M^\vee$ (C5) | none | none | $A^\dagger$ (C4) | $\varphi^*$ (C4) |
| ch:ellcurves (9) | $V_\ell E^\vee$ | none | none | none | $\varphi^*$ |
| ch:modforms (12) | none | none | none | $U_p^\dagger$ | $\gamma^*$ |
| ch:hecke (13) | none | none | none | $t^\dagger$ (C6) | none |
| ch:moddeg (14) | $M^\vee$ (C3) | in `paperlink` only | none | $A^\dagger$ (C3) | $^*$ (C3) |
| ch:modgalrep (15) | $\rho^\vee$ (C2) | none | none | $T_n^*$ (8.1, line 495) | $\phi^*$ |
| ch:cohomology (16) | none | $A^*$ | none | none | $(f,\varphi)^*$ |
| ch:galcoh (17) | $T^\vee$ (C3) | $A^*$ (C3) | $M^*(1)$, $T^D=T^\vee(1)$ (C3) | none | none |
| ch:blochkato (18) | $M^\vee$ (C2) | $X^*$ (C2) | $M^D=M^\vee(1)$ (C2) | none | $\varphi_E^*$ |
| ch:lfunctions (19) | $V_\ell E^\vee$ | none | none | none | none |
| ch:paper (21) | `V_l E^*`, `T^*` (lines 678, 680, 1894) | `^*` | `T^D` | `T_n^*` (line 518) | none |
| PLAN.md | $V^*$ (Chapters 4, 14, 18 entries) | $^*$ | $V^D=V^*(1)$ | none | $\varphi^*$, $\Frob_p^*$ |

Every outline but three already writes $^\vee$ for linear duals and $^*$ for Pontryagin duals; four use $\dagger$ for
adjoints against three that use $^*$; pullbacks by $^*$ are universal and standard (the Manin constant, the modular
parametrisation, Hecke correspondences) and cannot be renamed without rewriting Chapters 8, 9, 12, 14. So the choice
above (linear $^\vee$, Pontryagin $^*$, Kummer $^D$, adjoint $^\dagger$, pullback $^*$ on maps) costs: Chapter 3 (adjoints in
9.5 and its writer note; $V^*\otimes W$ in 5. Dependencies), Chapter 15 (one line), Chapter 21 (four lines), PLAN.md
(three entries). Any other choice costs more: adjoints by $^*$ would change Chapters 8, 12, 13, 14; linear duals by $^*$
would change eleven outlines. Changes: Part 3, D1 to D9.

### B-C5. Tate twists, Hodge-Tate weights and other signs

> **Convention B-C5.**
> (a) $\Z_\ell(1)=T_\ell\mu=\varprojlim_k\mu_{\ell^k}$ (transition maps $\zeta\mapsto\zeta^\ell$), on which $G_K$ acts through $\chi_\ell$;
> $\Z_\ell(n)=\Z_\ell(1)^{\otimes n}$, $\Z_\ell(-1)=\Hom(\Z_\ell(1),\Z_\ell)$, and $M(n)=M\otimes_{\Z_\ell}\Z_\ell(n)$ for every $n\in\Z$; $\Q_\ell/\Z_\ell(1)=\mu_{\ell^\infty}$.
> So $\Frob_p$ acts on $\Z_\ell(1)$ by $p$, $\Phi_p$ by $p^{-1}$, and $L_p(M(n),s)=L_p(M,s+n)$.
> (b) The Weil pairing (Silverman's $e_m$, ch:ellcurves C7) gives $\wedge^2T_\ell E\simeq\Z_\ell(1)$, $\det\rho_{E,\ell}=\chi_\ell$,
> $T_\ell E\simeq(T_\ell E)^\vee(1)$, and $H^1(E,\Z_\ell)=(T_\ell E)^\vee\simeq T_\ell E(-1)$; for a curve $X$,
> $H^1_{\mathrm{et}}(X,\Z_\ell)\simeq T_\ell J(X)(-1)$ (ch:curves 11.8).
> (c) **Hodge-Tate weights**: $\Q_\ell(1)$ has Hodge-Tate weight $+1$; so $V_\ell E$ has weights $\{0,1\}$, $\ad V$ has $\{-1,0,1\}$,
> $V^D=\ad V(1)$ has $\{0,1,2\}$, $V_\ell E^\vee$ has $\{-1,0\}$ (ch:blochkato C4). Sources with the opposite sign are flagged
> where cited.
> (d) Other fixed signs: the cup product $\langle\alpha,\beta\rangle=\int_X\alpha\wedge\beta$ with the complex orientation (ch:curves C6;
> the paper needs only sign-invariant properties); the Kummer map $\delta(a)(\sigma)=\sigma(\alpha)/\alpha$, $\alpha^n=a$ (ch:galcoh C6);
> the conjugation action $(\sigma\cdot c)(h)=\sigma\,c(\sigma^{-1}h\sigma)$ of $G/H$ on $H^n(H,M)$, verbatim the paper's (ch:cohomology
> writer note 1); the slash operator $(f|_k\gamma)(z)=(\det\gamma)^{k/2}(cz+d)^{-k}f(\gamma z)$ (ch:modforms C3) and
> $W_N=\begin{psmallmatrix}0&-1\\N&0\end{psmallmatrix}$ (ch:modforms C4).

Reason: ch:galois C6, ch:galcoh C3, ch:blochkato C2, C4, ch:curves 11.8, ch:ellcurves 5.5, ch:local 8.2. Chapters
bound: 5, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 21. Changes: none in the outlines (all comply); the writers of
Chapters 18 and 20 must check DFG04's and Bloch-Kato's sign of the Hodge-Tate weight before quoting a dimension formula.

### B-C6. Characters: $\chi_\ell$, $\chi_d$, $\chi_{q^*}$

> **Convention B-C6 (characters).**
> (a) $\chi_\ell\colon G_\Q\to\Z_\ell^\times$ is the $\ell$-adic **cyclotomic** character, $\sigma(\zeta)=\zeta^{\chi_\ell(\sigma)}$ on $\mu_{\ell^\infty}$;
> $\bar\chi_\ell\colon G_\Q\to\F_\ell^\times$ its reduction; $\omega_\ell\colon a\mapsto a\bmod\ell$ the Dirichlet character that corresponds to
> $\bar\chi_\ell$ (ch:rings C5). A letter subscript ($\chi_\ell$, $\chi_p$) always means the cyclotomic character. At a
> numerical prime the cyclotomic character is written $\chi_3^{\mathrm{cyc}}$, $\chi_5^{\mathrm{cyc}}$; its reduction $\bar\chi_3$ (with the bar)
> is unambiguous, quadratic characters never carrying a bar.
> (b) For a non-square $d\in\Q^\times$, $\chi_d$ is the **quadratic** character of $\Q(\sqrt d)$, $\sigma(\sqrt d)=\chi_d(\sigma)\sqrt d$; as a
> Dirichlet character it is the Kronecker symbol $\bigl(\frac D\cdot\bigr)$, $D$ the discriminant of $\Q(\sqrt d)$, of conductor $|D|$.
> A **numerical** subscript always means $\chi_d$ with $d$ written with its sign: $\chi_{-3}$, $\chi_{-4}$, $\chi_{-7}$, $\chi_{-11}$,
> $\chi_5$, $\chi_{13}$. The paper's $\chi_{11}$ is written $\chi_{-11}$; the symbols $\chi_3$, $\chi_7$, $\chi_{11}$ are not used.
> (c) For an odd prime $q$, the quadratic character of conductor $q$ is $\chi_{q^*}$, the character of $\Q(\sqrt{q^*})$
> ($\chi_d$ with $d=q^*$ the discriminant), **never** $\chi_q$. The paper's $\chi_q$ appears only when the paper is quoted
> (B.5 and Part 4, item 4), followed by the book's $\chi_{q^*}$. A letter subscript $\chi_\ell$ is reserved for the $\ell$-adic
> cyclotomic character, and $\chi_3^{\mathrm{cyc}}$ is written where a number is needed (PLAN.md 7.5, decision D3, which replaces
> the earlier allowance for the paper's $\chi_q$). Never write $\chi_\ell$ for a quadratic
> character: $\chi_{\ell^*}=\bar\chi_\ell^{(\ell-1)/2}$ is the quadratic character of $\Q(\sqrt{\ell^*})$, and $\chi_{\ell^*}=\bar\chi_\ell$ iff
> $\ell=3$, where $\bar\chi_3=\chi_{-3}$ (important_notes.md points 5, 6, 32).
> (d) $\chi_S=\prod_{q\in S}\chi_{q^*}$ for a finite set $S$ of odd primes, of conductor $D=\prod_{q\in S}q$. $\varepsilon$ is an
> unramified character of $G_{\Q_q}$ of order at most $2$ (the Tate data, B-C14), with $\varepsilon(\Frob_q)=a_q(E)$ at a
> multiplicative prime. $\psi$ is the character of order $4$ of Proposition prop:ns, with values in $\F_9^\times$.
> (e) A Dirichlet character $\chi$ is also the Galois character with $\chi(\Frob_p)=\chi(p)$ for $p\nmid\operatorname{cond}\chi$
> (arithmetic Frobenius; ch:ant 5.7, ch:modgalrep C3).

Reason: the paper names one character $\chi_{11}$ and $\chi_{-11}$ and uses $\chi_3$ both ways (point 32). Rule (b) and (c)
together name every quadratic character by its discriminant (decision D3, PLAN.md 7.5): Chapters 2, 13, 18, 19 already wrote
$\chi_{q^*}$, and the paper's $\chi_q$ in Chapters 5, 7, 9, 10, 11, 15, 21 (and elsewhere) has been converted to $\chi_{q^*}$. Only
seven lines use a numerical $\chi_3$ in the book's own text. Chapters bound: 2, 4, 5, 6, 7, 9, 10, 11, 13, 15, 17, 18, 19, 21, 22. Changes: Part 3, X1 to X5.

### B-C7. Normalisations of the adjoint and symmetric square $L$-functions

> **Convention B-C7.** Let $f$ be a newform of weight $2$ on $\Gamma_0(N)$, $V=V_\lambda(f)$ (for $f=f_E$, $V=V_\ell E$), $A_f=\ad V$.
> $$L(\ad f,s)=L(A_f,s)=\prod_pL_p(A_f,s),\qquad L(\Sym f,s)=\prod_pL_p(\operatorname{Sym}^2V^\vee,s)=L(\ad f,s-1),$$
> with $L_p$ as in B-C2(d) ($p\ne\ell$; at $p=\ell$ through $D_{\mathrm{cris}}$, or with $V_{\ell'}$ for $\ell'\ne p$). So $L_p(\Sym f,s)=L_p(A_f,s-1)$, and
> the special values are $L(\Sym f,2)=L(\ad f,1)$. $P_q(X)\in\Z[X]$ is defined by $L_q(\Sym f,s)=P_q(q^{-s})^{-1}$; hence
> $P_q(q^{-2})=L_q(A_f,1)^{-1}$. The **naive** factor is $L_p^{\nv}(A_f,s)=L_p(A_f,s)$ if $\delta_p=\dim V^{I_p}>0$ and $1$ if $\delta_p=0$
> (equivalently $L_p^{\nv}(A_f,s)^{-1}=1-a_p(f)^2p^{-1-s}$ for $p\mid N$); $L^{\nv}$ is their product. The normalisations of the
> sources:
>
> | object | source | equals | functional equation | point used |
> |-|-|-|-|-|
> | $L(\ad f,s)$, $L(\ad M_f,s)$ | the paper; DFG04 1.7.2 | $L(A_f,s)$ | $s\leftrightarrow1-s$ | $s=1$ |
> | $L(s,\pi_f,\operatorname{Ad})$ | Gelbart-Jacquet (unitary) | $L(A_f,s)$ (weight $k$: $L(\operatorname{Sym}^2,s+k-1)$) | $s\leftrightarrow1-s$ | $s=1$ |
> | $L(\Sym f,s)$ | the paper; PARI `lfunsympow(E,2)`; Watkins02 | $L(A_f,s-1)$ | $s\leftrightarrow3-s$ | $s=2$ |
> | Shimura's series $\zeta^{(N)}(2s-2)\sum a_{n^2}n^{-s}$ | Shimura75 | $L^{\nv}(A_f,s-1)$ | via the above | |
> | Rankin series $D(f,s)=\sum a_n^2n^{-s}$ | Rankin39 | $\zeta^{(N)}(s-1)L^{\nv}(\Sym f,s)/\zeta^{(N)}(2s-2)$ | none | |
>
> The Rankin series is never called $L(\Sym f,s)$ (important_notes.md points 30, 70). $e_\ell(E,q)=v_\ell\bigl(L_q(A_f,1)^{-1}/
> L_q^{\nv}(A_f,1)^{-1}\bigr)=v_\ell\bigl(P_q(q^{-2})/(1-a_q^2q^{-2})\bigr)$ (Definition def:terms).

Reason: ch:lfunctions C4, C5, C6, 7.4 (whose table this is, with the rows marked "verify" there still to be checked
against DFG04 and Watkins02); ch:reps 7.5(iii); ch:local 9.5; ch:blochkato 14.1; ch:paper C2(c). All outlines agree.
Chapters bound: 4, 7, 13, 15, 18, 19, 20, 21, 22. Changes: none in the outlines; PLAN.md Chapter 19 entry already fixed
(B23).

### B-C8. The Petersson product

> **Convention B-C8.** For $f,g\in S_k(\Gamma_0(N))$,
> $$\langle f,g\rangle=\int_{\Gamma_0(N)\backslash\mathfrak H}f(z)\overline{g(z)}\,y^k\,\frac{dx\,dy}{y^2},$$
> **unnormalised** (not divided by the index or the volume), linear in the first variable; in weight $2$,
> $\langle f,g\rangle=\frac i2\int_{X_0(N)}\omega_f\wedge\overline{\omega_g}$ with $\omega_f=f(z)\,dz$. PARI's `mfpetersson` returns
> $\langle f,g\rangle/\mu(N)$, $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]=N\prod_{p\mid N}(1+p^{-1})$; other books divide by
> $\operatorname{vol}(\Gamma_0(N)\backslash\mathfrak H)=\pi\mu(N)/3$. Never quote a number without its normalisation.

Reason: ch:modforms C5 (checked numerically on five curves, 10.4), ch:hecke C6, ch:moddeg C4, ch:lfunctions C9;
important_notes.md B10. Chapters bound: 12, 13, 14, 19, 21, 22. Changes: none (all comply).

### B-C9. The Manin constant and the formula of Zagier and Watkins

> **Convention B-C9.** For a modular parametrisation $\varphi\colon X_0(N)\to E$ (sending $\infty$ to $O$) and the Neron
> differential $\omega_E$ of a global minimal model, $\varphi^*\omega_E=c_\varphi\cdot2\pi i\,f(z)\,dz=c_\varphi\,f(q)\,dq/q$; the **Manin constant**
> of the optimal curve is $c_E=c_{\varphi_E}$. The sign of $\omega_E$ is chosen so that $c_E>0$; Manin's conjecture reads $c_E=1$.
> Then, with the product of B-C8,
> $$\deg\varphi\cdot\operatorname{vol}(\Lambda_E)=4\pi^2c_\varphi^2\,\langle f,f\rangle,\qquad\operatorname{vol}(\Lambda_E)=\tfrac i2\int_{E(\C)}\omega_E\wedge\bar\omega_E,$$
> **$c^2$ in the numerator** of $\deg\varphi_E=4\pi^2c_E^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$ (important_notes.md B10; check: the
> degree-$5$ parametrisation of 11a3 has $c_\varphi=5$). The Manin constant is never written as a bare $c$ in the book's own
> text ($c$ alone is taken by the paper's class in Lemma lem:tamfactor, B-C14, and $c_q$ by Tamagawa numbers).

Reason: ch:moddeg C4, 7.1, 7.3; ch:modforms 10.1, B1; ch:lfunctions 8.4. The sign normalisation $c_E>0$ is new: Chapter 14
writes "$c_E$ well defined up to sign" and Chapters 14 and 19 write "$c_E=\pm1$"; only $c_E^2$ enters any formula, so
nothing changes but the wording. Chapters bound: 9, 12, 14, 18, 19, 21, 22. Changes: Part 3, M1 to M5.

### B-C10. Valuations, lengths, orders, Fitting ideals

> **Convention B-C10.** $v_\ell$ is the $\ell$-adic valuation on $\Q$ (and on $\Q_\ell$), normalised by $v_\ell(\ell)=1$, with
> $v_\ell(0)=+\infty$; for a nonzero ideal $\ell^a\Z_\ell$, $v_\ell(\ell^a\Z_\ell)=a$; for a DVR $\mathcal O$ with uniformiser $\varpi$,
> $v(\varpi)=1$, and the paper's $v_\lambda$ for $\lambda=\ell$ is $v_\ell$. For a class $c\in\Z/\ell^m$, $v_\ell(c):=\min(v_\ell(\tilde c),m)$ (so the
> paper's "$v_\ell(0)$" in Lemma lem:tamfactor reads $v_\ell(q-1)$). "**Length**" without subscript means $\Z_\ell$-length,
> $\len=\len_{\Z_\ell}$, and $\len(\Z_\ell/\ell^a)=a$; for finite $\Z_\ell$-modules $\#X=\ell^{\len X}$. Orders $\#\mathcal O/\Delta$ are
> used only for $\mathcal O$ with finite residue field (important_notes.md point 38); otherwise lengths. $\Fitt_{\Z_\ell}(X)=\ell^{\len X}\Z_\ell$
> for finite $X$. $\Tam_p(M)=\Fitt_{\Z_\ell}\bigl((H^1(I_p,M)_{\mathrm{tor}})^{G_{\Q_p}}\bigr)$: the Fitting ideal **of the invariants**
> (important_notes.md point 37).

Reason: PLAN.md Appendix B entry; ch:rings C3; ch:modules C2, C6; ch:galcoh C4; ch:blochkato C5, C6. Chapters
bound: all from 2 on. Changes: none in the outlines; PLAN.md Chapter 18 entry (the misplaced parenthesis, B22).

### B-C11. Kodaira symbols, component groups, PARI codes

> **Convention B-C11.**
> (a) Kodaira symbols are typeset $\mathrm I_0,\mathrm I_n,\mathrm{II},\mathrm{III},\mathrm{IV},\mathrm I_0^*,\mathrm I_n^*,\mathrm{IV}^*,\mathrm{III}^*,\mathrm{II}^*$ (PLAN.md 7.1); "type
> $\mathrm I_n$" assumes $n\ge1$ unless $\mathrm I_0$ is meant; at $q=2$ the index $m$ of a symbol $\mathrm I_m^*$ need not be $-v_2(j)$ and
> the reduction may be potentially good (ch:reduction 9.4).
> (b) $\Phi_q$ is the component group of the special fibre of the Neron model of $E$ at $q$, a finite etale group scheme over
> $\F_q$; it is always written **with an argument**: $\Phi_q(\F_q)$, $\Phi_q(\overline\F_q)$. The **geometric component group**
> $\Phi_q(\overline\F_q)$ is $\Phig_q$ (the paper's macro `\Phig`), and $\Phig_q[\ell^k]$, $\#\Phig_q$ are written with it; the **Tamagawa
> number** is $c_q=\#\Phi_q(\F_q)=[E(\Q_q):E_0(\Q_q)]$, which divides $\#\Phig_q$. A bare "$\Phi_q$" for a group is not used. The
> group $\Gal(L/K^{\mathrm{ur}})$ measuring the semistability defect is $G_{\mathrm{ss}}$ (ch:reduction R6), never $\Phi$.
> (c) PARI's Kodaira codes (`elllocalred(E,p)[2]`, the paper's `K[i][2]`): $1$ for $\mathrm I_0$; $n+4$ for $\mathrm I_n$ and $-(n+4)$ for
> $\mathrm I_n^*$ **for $n\ge1$ only**; $-1$ for $\mathrm I_0^*$; $2,3,4$ for $\mathrm{II},\mathrm{III},\mathrm{IV}$ and $-2,-3,-4$ for $\mathrm{II}^*,\mathrm{III}^*,\mathrm{IV}^*$
> (important_notes.md point 52; the paper's appendix states "$n+4$" without $n\ge1$). Codes appear only in tables,
> `lstlisting` and `paperlink` environments.
> (d) Conductor exponent $f_p=f_p(E)$, Swan conductor $\operatorname{sw}_p(E)$; the letter $\delta_p$ is reserved for $\dim V^{I_p}$.

Reason: ch:reduction R3, R4, R5, R6, 4.2, 4.4, 5.5; ch:lfunctions C8; ch:paper A9.2; the clash of $\Phi_q$ with the
geometric Frobenius (B-C2(b)) and with the semistability group. Chapters bound: 10, 11, 14, 19, 21, 22.
Changes: Part 3, K1 (Chapter 11), K2 (Chapter 15), P4 (PLAN.md, the codes).

### B-C12. The adjoint, the symmetric square, the paper's $A$, $A_f$, and the abelian variety $J_f$

> **Convention B-C12.**
> (a) For a representation $V$ (or lattice $T$), $\End(V)=V\otimes V^\vee$ with $g\cdot x=\rho(g)x\rho(g)^{-1}$ is written $\End(V)$ or
> $\operatorname{Ad}V$; the **trace-zero adjoint** is $\ad V$ (the paper's macro `\ad`, which already contains the superscript $0$:
> never `\ad`); $\Sym V$ (macro `\Sym`, exponent included) is the symmetric square. For $\dim V=2$ the basis of $\ad V$ is
> $e=e_1\otimes e_2^\vee$, $h=e_1\otimes e_1^\vee-e_2\otimes e_2^\vee$, $f=e_2\otimes e_1^\vee$ (ch:reps C3; the paper's Lemma lem:tamfactor).
> $\ad V\simeq\Sym V\otimes\det^{-1}$ and, for $\ell$ odd, the trace form makes $\ad T$ self-dual, $\ad T\simeq(\ad T)^\vee$.
> (b) The paper's objects: $V=V_\ell E$, $T=T_\ell E$, $\rho=\rho_{E,\ell}$, $\bar\rho$; $A=\ad T$, $A_f=\ad V=A\otimes\Q_\ell$, $W=A\otimes\Q_\ell/\Z_\ell$,
> $T^D=\Hom(A,\Z_\ell(1))\simeq A(1)$, $V^D=T^D\otimes\Q_\ell$, $W^D=V^D/T^D=\ad T(1)\otimes\Q_\ell/\Z_\ell$. $\ad$ is insensitive to duals and twists:
> $\ad(T^\vee)\simeq\ad T=\ad(T(n))=\ad(T\otimes\chi)$, so $\ad M_{f,\lambda}=\ad T_\ell E$ although $M_{f,\lambda}\simeq T_\ell E(-1)$ (points 26, 40).
> (c) **$A_f$ is the adjoint, never an abelian variety.** The quotient $J_0(N)/I_fJ_0(N)$ attached to a newform $f$ (Shimura's
> $A_f$) is written $J_f$, with the quotient map $\pi_f\colon J_0(N)\to J_f$; for rational $f$, $J_f=E_f$ is the optimal curve of
> the class.

Reason: the paper's $A_f$ (Section 1.1) is the adjoint; PLAN.md's Chapter 14 entry and the Chapter 14 and 15 outlines use
Shimura's $A_f$ for the abelian variety, and Chapter 15 uses both meanings (its 2.1 and 3.7). Renaming the abelian variety
touches two outlines; renaming the paper's adjoint is not allowed (PLAN.md 7.1: the paper's notation is the book's).
Chapters bound: 4, 11, 14, 15, 18, 19, 20, 21. Changes: Part 3, A1 to A3, P5.

### B-C13. Hecke algebras, eigencharacters, twists and depletion

> **Convention B-C13.**
> (a) $\T=\T_N=\Z[T_n:n\ge1]\subset\End_\C S_2(\Gamma_0(N))$ is the **full** Hecke algebra (the operators $U_p=T_p$ for $p\mid N$
> included); $\T^{(N)}=\Z[T_n:(n,N)=1]$ the anemic one; $\T_\ell=\T\otimes\Z_\ell$; for a maximal ideal $\mathfrak m\ni\ell$,
> $\T_{\mathfrak m}=(\T\otimes\Z_\ell)_{\mathfrak m}$, a direct factor of $\T_\ell$ cut out by an idempotent $e_{\mathfrak m}$ (ch:modules C7).
> (b) $\phi_f\colon\T\to\mathcal O_f$ (upright $\phi$) is the **eigencharacter** of $f$, $T_n\mapsto a_n(f)$; a general system of eigenvalues is
> also written $\phi$. $\varphi$ (curly) is reserved for **maps of curves**: $\varphi_E\colon X_0(N)\to E$, isogenies $\varphi$.
> (c) The paper's two uses of $I$: in Lemma lem:crit $I=\ker\phi_f$ and $J=\Ann_\T(f^\perp)$; in Lemma lem:ddt417 $\wp=\ker\pi$ and
> $I=\Ann_\T(\wp)$. So the $J$ of lem:crit is the $I$ of lem:ddt417 (for $\pi=\phi_f$). The book keeps each lemma's letters inside
> that lemma and writes $\ker\phi_f$ (or $\wp$, or $I_f$ in Chapter 14) and $\Ann_\T(\wp)$ in its own text.
> (d) Twists: for a Dirichlet character $\chi$ of conductor $r$, $f\otimes\chi=\sum\chi(n)a_n(f)q^n$ is the **naive twist** (the paper's
> $f\otimes\chi$ and the map $\iota$ of Theorem thm:twist); $f^\chi$ is the **newform twist** ($\rho_{f^\chi}\simeq\rho_f\otimes\chi$); then
> $f\otimes\chi$ is the $r$-depletion of $f^\chi$ (ch:modgalrep C4). $E^{(d)}=E\otimes\chi_d$ is the quadratic twist of a curve by
> $\Q(\sqrt d)$; $E^{(q)}:=E^{(q^*)}$ for odd $q$ (the paper's); $E_S=E\otimes\chi_S$.
> (e) **Depletion**: $f^\Sigma=\sum_{(n,\Sigma)=1}a_nq^n$ for a set $\Sigma$ of primes (the paper's notation), $f^{\{p\}}$ for one prime,
> $f^S$ for the set $S$. A parenthesised superscript $(p)$, $(q)$, $(d)$ is reserved for **twists** of curves ($E^{(q)}$) and for
> removing Euler factors ($\zeta^{(N)}$, $\T^{(N)}$); it never denotes depletion.
> (f) $W_N=\begin{psmallmatrix}0&-1\\N&0\end{psmallmatrix}$, $w_N$ the involution of $X_0(N)$ and the operator $f\mapsto f|_kW_N$;
> $\varepsilon_N(f)=\pm1$ its eigenvalue on a newform. $\hat\delta_!$ (always with the subscript) is the pairing $\langle x,w_Ny\rangle$
> on $H^1(X_0(N),\Z_\ell)$ (DFG04's $\hat\delta_!$ in weight $2$, trivial character); $M_{f,\lambda}=H^1(X_0(N),\Z_\ell)[\ker\phi_f]$ (with
> $\lambda=\ell$ for rational $f$); $\eta^\Sigma_{f,\lambda}$ its ideal of values on $M_{f^\Sigma,\lambda}$.

Reason: ch:hecke C3 to C8, ch:modgalrep C1, C4, ch:moddeg C2, C3, ch:modules C7; the clash of $h^{(p)}$ with $E^{(q)}$;
the clash of a curly $\varphi$ for eigenvalue systems (ch:hecke C5) and of an upright $\phi$ for the modular parametrisation
(ch:modgalrep 2.6) with the paper's $\phi_f$ and $\varphi_E$. Chapters bound: 3, 12, 13, 14, 15, 20, 21, 22.
Changes: Part 3, H1 to H5.

### B-C14. The Tate data at a prime with $v_q(j)<0$

> **Convention B-C14.** $q\ne\ell$; $q_E\in\Q_q^\times$ the Tate parameter (never $u$); $\nu=v_q(q_E)=-v_q(j_E)$, equal to
> $n=n_q=v_q(\Delta_E)$ at a multiplicative prime; $u=q_Eq^{-\nu}\in\Z_q^\times$ its unit part, $\bar u\in\F_q^\times$ its reduction; $c(u)$
> the class of $\bar u$ in $\F_q^\times/(\F_q^\times)^{\ell^{v_\ell(q-1)}}$ (the paper's $c$ in Lemma lem:tamfactor and $c_q$ in Section
> sec:tam), with $v_\ell(c(u))$ read as in B-C10. $\kappa=\kappa_{q_E}$ the Kummer cocycle of $q_E$, $\kappa=\nu\kappa_q+\kappa_u$ (ch:galcoh 5.3);
> $t$ a topological generator of the pro-$\ell$ tame inertia quotient. In a basis $e_1,e_2$ of $T_\ell E$:
> $$\rho(g)=\begin{pmatrix}\chi_\ell(g)\varepsilon(g)&\varepsilon(g)\kappa(g)\\0&\varepsilon(g)\end{pmatrix},$$
> **with corner $\varepsilon\kappa$**, not $\kappa$ (important_notes.md point 42); $c'=\varepsilon(\Frob)\kappa(\Frob)$ for the arithmetic Frobenius,
> well defined modulo $(n,q-1)\Z_\ell$ (point 7 and its addendum).

Reason: ch:blochkato C6, ch:reduction R1, R4, 7.4, ch:galcoh 5.3, 5.4, ch:local 7.6, ch:cohomology cocycle-in-the-corner;
important_notes.md points 7, 8, 23, 31, 42. Chapters bound: 2, 7, 10, 11, 16, 17, 18, 21, 22. Changes: Part 3, T1, T2
(Chapter 21).

### B-C15. Other letters with several meanings (the rules)

> **Convention B-C15.**
> (a) Uniformisers of local fields and DVRs are $\varpi$ (ch:modules C2, ch:local L1); the paper's $\pi=1-\zeta_3$ (Lemma lem:IV)
> and $\pi\colon\T\to\mathcal O$ (Lemma lem:ddt417) keep their names inside those lemmas; $\pi_f$ is the quotient map to $J_f$;
> $\pi_q$ the Frobenius endomorphism (B-C2(g)).
> (b) $\zeta_n=e^{2\pi i/n}$; a primitive cube root of unity is always $\zeta_3$, never $\omega$ or $\rho$. $\omega$ is a differential:
> $\omega_E$ (Neron or invariant differential), $\omega_f=f(z)\,dz$; $\omega_1,\omega_2$ are periods (Chapters 8, 9); the fundamental
> characters of Chapters 11 and 15 are $\omega$ (level $1$, $=\bar\chi_\ell|_{I_\ell}$) and $\omega_2$ (level $2$), used only there and
> never in a chapter with periods; $\omega_\ell$ is the Dirichlet character of B-C6(a).
> (c) $\iota$ is the twist map of Theorem thm:twist in Chapters 13, 15, 20, 21 and the map $H^1(K,T)\to H^1(K,V)$ in Chapters 17,
> 18, 21 (both are the paper's); a chapter using both writes $\iota_S$ for the twist map.
> (d) $D$: the conductor $\prod_{q\in S}q$ of $\chi_S$ (Theorem thm:twist); the deficit of Conjecture conj:eis; the discriminant of a
> quadratic field (Chapters 2, 5, 6, 9); the quaternion discriminant of a Shimura curve (Chapter 14). $D_p$ is a decomposition
> group, $D_{\mathrm{cris}}$ Fontaine's functor, ${}^D$ the Kummer dual. Each chapter uses at most two of these and says which.
> (e) $\Sigma$ is the paper's finite set of primes; the Shimura subgroup of $J_0(N)$ is $\mathcal S_N$ (not $\Sigma_N$); $S$ is the set of
> primes of Theorem thm:quant, $S_f$ DFG04's exceptional set, $S$ a set of places in $G_{\Q,S}$ (Chapter 17).
> (f) $N$ is the conductor or level; the monodromy operator of a Weil-Deligne representation is $N$ only in Chapters 7, 15
> (local statements); $N_s,N_{ns}$ are normalisers of Cartan subgroups; $\operatorname{Norm}$ is a norm map.
> (g) $\mu_n$ roots of unity; $\mu(N)=[\SL_2(\Z):\Gamma_0(N)]$; $\mu$ an unramified character (Chapter 7) and the $U_p$-eigenvalue choice
> $\mu_p$ of Lemma lem:old are local names.
> (h) $\eta^\Sigma_{f,\lambda}$, $\eta$ congruence ideals; $\eta(z)$ the Dedekind eta function (Chapter 12 only). $\Delta$ the discriminant,
> $\Delta(z)$ the cusp form of level one, $\Delta$ the Gram determinant of Lemma lem:ddt417 (local). $\Lambda_E$ period lattice,
> $\Lambda(\cdot,s)$ completed $L$-functions.
> (i) $t_\ell(E,q)$ (the paper's term) always carries its arguments; the tame character $t_\ell\colon I\to\Z_\ell(1)$ of Chapter 7 is
> written with its domain or an argument $t_\ell(\sigma)$; $t$ alone is a generator of tame inertia.
> (j) $V$ is $V_\ell E$ or a representation; the Verschiebung is $\hat\pi_p$; $V_d\colon h(z)\mapsto h(dz)$ (Chapter 13) and $V_f$ (Chapter 14,
> the $f$-part of $H^1$) are local names. $T$ is $T_\ell E$; $\T$ the Hecke algebra; $T_n$ Hecke operators; the matrix
> $\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$ is $T$ only in Chapter 12, Sections 1 and 2.
> (k) $\varepsilon$: unramified character (B-C14); $\varepsilon_N(f)$ Atkin-Lehner sign; a root number is $w$ or $\varepsilon(\cdot)$ with
> its argument; the non-square of Chapter 1's standard models is $\varepsilon$ only in Chapter 1, Section 5.
> (l) $\delta_p=\dim V^{I_p}$; $\hat\delta_!$ the pairing; $\delta$ a connecting map; $\delta(\bar\sigma)$ the DDT exponent of the optimal
> level theorem (Chapter 15).
> (m) $\psi$: the order-$4$ character (prop:ns); $\psi_m$ division polynomials (Chapter 9); an isogeny $\psi$ (Chapter 14, 7.1).

Reason: the collisions recorded in the index (Part 2). Chapters bound: as named. Changes: Part 3, L1 to L6.

### B-C16. Labels, names and typography

> **Convention B-C16.** Curve labels are Cremona's, as printed by the paper: 11a1 (a curve), 121c (an isogeny class);
> ARS12's 99A1 is Cremona's 99a1; LMFDB labels are written 11.a2. Mod $\ell$ image labels are Sutherland's (3Ns, 3Cs.1.1,
> 3B.1.1, ...; the macro `\Ns` prints 3Ns), always with the intrinsic description; the groups are $N_s(\F_3)$, $N_{ns}(\F_3)$
> (standard models of ch:groups 6.2). "Optimal" means $X_0(N)$-optimal. Double names take plain hyphens (Bloch-Kato,
> Diamond-Flach-Guo, Fontaine-Perrin-Riou, Atkin-Lehner); no dash ligatures anywhere (PLAN.md 7.2).

Changes: none.

________________________________________________________________________________

## Part 2. Index of symbols

One row per symbol. "Defined in" gives the chapter label and the outline item that defines the symbol (or the convention
box that fixes it); where a symbol is defined in one chapter and specialised in another, both are given. Chapters 20 and 22
are cited by label only. "Paper" names the place in the paper where the symbol first occurs. The last column flags every
other meaning the symbol has in the book or in the paper (**clash**) and the rule that resolves it (Part 1). In the LaTeX
appendix the rows are grouped exactly as here, alphabetically inside each group (Latin, then Greek, then decorations).

### 2.1 Numbers, valuations, rings and modules

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $p$, $q$, $\ell$ | primes; $q$ a bad prime, $\ell$ the coefficient prime | ch:rings C2; B-C1 | $q$ also field size, $e^{2\pi iz}$, Tate variable $\mathsf q$ (B-C1) |
| $q^*$, $\ell^*$ | $(-1)^{(q-1)/2}q$, $(-1)^{(\ell-1)/2}\ell$ | ch:rings 9.6; ch:galois galois:sqrt-lstar | star exception (B-C4(e)) |
| $\mathfrak q$ | size of a finite field when not prime | ch:ellcurves C2 | - |
| $\F_q$, $\F_q^\times$, $(\F_q^\times)^{\ell^k}$ | finite field, its units, $\ell^k$-th powers | ch:rings 6.1, 6.2, 7.1 | index $[\F_q^\times:(\F_q^\times)^{\ell^k}]=\ell^{\min(k,v_\ell(q-1))}$ (7.1) |
| $\Z/n$, $(\Z/n)^\times$ | integers mod $n$, units | ch:rings 5.1 | - |
| $\mu_n$, $\mu_n(K)$, $\mu_{\ell^\infty}$ | roots of unity | ch:rings 8.1, C6 | $\mu(N)$ index, $\mu$ characters, $\mu_p$ of lem:old (B-C15(g)) |
| $\zeta_n$ | $e^{2\pi i/n}$ | ch:rings C6 | never $\omega$ or $\rho$ for $\zeta_3$ (B-C15(b)) |
| $\Phi_n(x)$ | $n$-th cyclotomic polynomial | ch:rings 8.2 | **clash**: geometric Frobenius $\Phi$, component group $\Phi_q(\cdot)$; integer subscript and a polynomial argument identify it |
| $\sqrt{-3}$ | $1+2\zeta_3=i\sqrt3$ | ch:rings C6; ch:ant 4.6 | spans $(\ad V)^{I_q}$ for types II, IV (lem:euler) |
| $\Z[i]$, $\Z[\zeta_3]$, $\Z_3[\zeta_3]$ | Gaussian and Eisenstein integers; a DVR | ch:rings 3.4; ch:ant 4.5, 4.7 | - |
| $\pi$ (in lem:IV) | uniformiser $1-\zeta_3$ of $\Z_3[\zeta_3]$ | ch:ant 4.7 | **clash**: $\pi\colon\T\to\mathcal O$ (lem:ddt417), $\pi_f$, $\pi_q$, $3.14159$ (B-C15(a)) |
| $v_p$, $v_\ell$ | $p$-adic valuation, $v_\ell(\ell)=1$ | ch:rings 11.1, C3; B-C10 | $v_\ell(c)$ for $c\in\Z/\ell^m$ (B-C10) |
| $\lvert x\rvert_p$ | $p^{-v_p(x)}$ | ch:rings 11.2 | - |
| $\bigl(\frac ap\bigr)$, $\bigl(\frac an\bigr)$ | Legendre, Jacobi, Kronecker symbols | ch:rings 9.1, 9.4, 9.5, C4 | - |
| $R^\times$ | unit group | ch:rings 1.1 | - |
| $\mathcal O$, $\varpi$, $k$, $K$ | DVR, uniformiser, residue field, fraction field | ch:modules C2, 6.1 | paper's $\mathcal O$ also the integers of a number field (ch:ant 1.2); ch:reps C7 writes $\lambda$ for the uniformiser |
| $\mathcal O_K$, $\mathcal O_f$, $K_f$ | integers of $K$; coefficient field of $f$ and its integers | ch:ant 1.2, 7.1; ch:modgalrep C1 | - |
| $\lambda$ | prime of $\mathcal O_f$ above $\ell$; $\lambda=\ell$ for rational $f$ | ch:ant 7.2; ch:modgalrep C1 | eigenvalues $\lambda$ (local) |
| $v_\lambda$ | valuation of $\lambda$ | ch:ant 7.2 | $=v_\ell$ when $\lambda=\ell$ |
| $\Z_\ell$, $\Q_\ell$, $\Q_\ell/\Z_\ell$ | $\ell$-adic integers, numbers, the divisible group | ch:modules 6.4, 6.5; ch:groups 7.2 | - |
| $\len$, $\len_R$ | length; $\len=\len_{\Z_\ell}$ | ch:modules 7.1, 7.2, C6; B-C10 | - |
| $\Fitt_R(M)$ | Fitting ideal | ch:modules 7.4 to 7.6 | - |
| $\Ann_R(M)$, $M[\mathfrak a]$, $M[\ell^k]$, $M_{\mathrm{tor}}$ | annihilator, $\mathfrak a$-torsion, torsion | ch:modules 7.3, C3, 5.4 | - |
| $\#X$ | order of a finite set | B-C10 | $\#X=\ell^{\len X}$ |
| $L$, $L[\wp]$, $L[I]$ | lattice with perfect pairing; its $\wp$- and $I$-torsion | ch:modules 9.1, 11.3 | $L$-functions $L(\cdot,s)$ |
| saturated | $M/L$ torsion-free | ch:modules 5.5 | - |
| $S^\perp$ | orthogonal of $S$ for a pairing | ch:modules C5, 9.1 | Pontryagin $B^\perp$ (ch:modules 8.1) |
| Gram determinant $\Delta$ | $\det(\langle e_i,e_j\rangle)$; in lem:ddt417 of $L[\wp]$ | ch:modules 9.3; paper lem:ddt417 | **clash**: discriminant $\Delta$, $\Delta(z)$ (B-C15(h)) |
| $\wp$ | $\ker(\pi\colon\T\to\mathcal O)$ | ch:modules 11.1; paper lem:ddt417 | Weierstrass $\wp(z)$ (ch:ellcurves 7.2); Artin-Schreier $\wp$ (ch:galois) |
| $\eta$ | congruence ideal $\pi(\Ann_\T\wp)$ | ch:modules 11.1 | Dedekind $\eta(z)$ (B-C15(h)) |
| $\mathcal O/\eta$ | congruence module $\T/(\wp+\Ann\wp)$ | ch:modules 11.1 | - |
| $\T_{\mathfrak m}$, $e_{\mathfrak m}$, $L_{\mathfrak m}$ | factor of $\T\otimes\Z_\ell$ at $\mathfrak m$, its idempotent, $e_{\mathfrak m}(L\otimes\Z_\ell)$ | ch:modules C7, 10.3, 10.4 | $\T_{(\mathfrak m)}$ algebraic localisation |
| $V(\phi)$ | generalised eigenspace of a system $\phi$ | ch:modules 10.5; ch:hecke C5 | ch:hecke writes $\varphi$ (H1) |
| Gorenstein | $\Hom_{\mathcal O}(\T,\mathcal O)$ free of rank one | ch:modules 11.4 | - |
| $\Hom$, $\otimes$, $\End$ | as usual | ch:modules 3.1, 3.2 | - |

### 2.2 Groups and representations

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $C_n$, $D_n$, $Q_8$, $SD_{16}$, $V_4$ | cyclic, dihedral (order $2n$), quaternion, semidihedral, Klein | ch:groups C3, 2.4 to 2.6 | $D_4$ has order $8$ |
| $\GL_2$, $\SL_2$, $\mathrm{PGL}_2$, $\mathrm{PSL}_2$ | matrix groups | ch:groups 5.1 | - |
| $\mathrm B$, $\mathrm U$ | Borel subgroup, unipotent subgroup | ch:groups 5.5, 5.6 | - |
| $C_s$, $N_s$, $C_{ns}$, $N_{ns}$ | split and nonsplit Cartan subgroups and their normalisers (standard models) | ch:groups 5.8, 6.2 | $N_s(\F_3)\subset N_{ns}(\F_3)$, not maximal (point 2) |
| $J$, $u$, $w$, $a$, $h$ | standard matrices of $\GL_2(\F_3)$ | ch:groups 6.2; ch:reps C6 | $h=\operatorname{diag}(1,-1)$ (ch:groups writes $\sigma$); $w$ also $w_N$, $w_\ell(E,q)$ |
| $\varepsilon$ (Chapter 1) | fixed non-square of $\F_q$ ($-1$ at $q=3$) | ch:groups 5.8 | **clash**: characters $\varepsilon$ (B-C15(k)) |
| $\mathbb P^1(F)$, $[v]$ | lines of $F^2$ | ch:groups C1, 5.3 | - |
| 3Ns, 3Nn, 3Cs, 3Cs.1.1, 3B, 3B.1.1, 3B.1.2 | Sutherland's labels of mod $3$ images | ch:groups 6.10; ch:galrep 7.4 | `\Ns` prints 3Ns (B-C16) |
| $\rho$, $\rho(g)$ | a representation | ch:reps 1.1 | $\rho_{E,\ell}$; ch:modforms C2 uses $\rho=e^{2\pi i/3}$ (L3) |
| $V^\vee$ | contragredient | ch:reps C2; B-C4(a) | - |
| $\Hom_G(V,W)$ | $G$-maps, $=(V^\vee\otimes W)^G$ | ch:reps 1.3 | PLAN.md writes $V^*\otimes W$ (D7) |
| $\tr_V$ | trace function (character) | ch:reps C4, 4.1 | not $\chi_V$ |
| $\rho^{ss}$, $\bar\rho^{ss}$ | semisimplification | ch:reps 3.5 | - |
| $\Ind_H^G$, $\Res$ | induction, restriction | ch:reps 6.1; ch:galois galois:restriction | $\Res$ also cohomological restriction |
| $\psi$ | character of order $4$ of $C_4$ with values in $\F_9^\times$, $\psi(J)=i$ | ch:reps C6, 8.2 | division polynomials $\psi_m$; isogeny $\psi$ (B-C15(m)) |
| $\End V$, $\operatorname{Ad}V$ | full adjoint | ch:reps C3, 7.3 | - |
| $\ad V$, $\ad T$ | trace-zero adjoint (macro `\ad`) | ch:reps 7.3; B-C12 | never `\ad` |
| $\Sym V$ | symmetric square (macro `\Sym`) | ch:reps 7.5 | ch:reps names the map $\Phi\colon\Sym V\to\ad V$ (F3) |
| $e$, $h$, $f$ | basis $e_1\otimes e_2^\vee$, $e_1\otimes e_1^\vee-e_2\otimes e_2^\vee$, $e_2\otimes e_1^\vee$ of $\ad$ | ch:reps C3; ch:cohomology model-setting | $e$ idempotent, $e_\ell$; $h$ newform; $f$ newform (local to lem:tamfactor) |
| trace form | $(x,y)\mapsto\tr(xy)$ on $\ad T$ | ch:reps 7.6 | perfect for $\ell$ odd |
| $\sigma$ | generator of order $3$ of the inertia image (lem:IV, lem:euler) | ch:reps C6, 9.3 | Chapter 1's $\sigma=\operatorname{diag}(1,-1)$ is $h$ elsewhere |
| $\tau$ | generator of order $4$ of the inertia image | ch:reps 9.3 | - |
| homothetic | $L'=cL$ | ch:reps C7, 10.1, 10.3 | - |

### 2.3 Fields, Galois groups, Frobenius, characters

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $\overline\Q$, $G_\Q$, $G_K$ | algebraic closure inside $\C$; absolute Galois groups | ch:galois C1, galois:absolute-galois-group | - |
| $G_{\Q,S}$, $\Q_S$ | Galois group of the maximal extension unramified outside $S$ | ch:galcoh 6.1 | $S$ (B-C15(e)) |
| $c$ (complex conjugation) | an element of order $2$ of $G_\Q$ | ch:galois galois:complex-conjugation | **clash**: $c(u)$, $c_q$, $c_E$ (always decorated) |
| $D_p$, $I_p$, $P_p$ | decomposition, inertia, wild inertia groups at $p$ | ch:ant 3.10; ch:local L2, 5.2 | $D$ (B-C15(d)) |
| $\Frob_p$, $\Frob$ | arithmetic Frobenius | ch:ant 3.7, 3.8; ch:local L3, 4.3; B-C2 | $\Frob^{\mathrm{geom}}$ not used |
| $\Phi_p$, $\Phi$ | geometric Frobenius $\Frob_p^{-1}$ | ch:local L3, 4.3; B-C2(b) | **clash**: component group $\Phi_q(\cdot)$, cyclotomic $\Phi_n$, ch:reps's arithmetic $\Phi$ (F3) |
| $\pi_q$, $\hat\pi_q$ | $q$-power Frobenius endomorphism, Verschiebung | B-C2(g); ch:ellcurves 8.1 | ch:curves $\phi_q$, ch:moddeg $F$, $V$ (F6, F7) |
| $\chi_\ell$, $\bar\chi_\ell$ | $\ell$-adic cyclotomic character, its reduction | ch:galois galois:cyclotomic-character, C4; B-C6(a) | the paper's $\chi_q$, the book's $\chi_{q^*}$ (B-C6(c), D3) |
| $\chi_3^{\mathrm{cyc}}$ | cyclotomic character at a numerical prime | B-C6(a); ch:galrep C4 | - |
| $\omega_\ell$ | Dirichlet character $a\mapsto a\bmod\ell$ | ch:rings C5, 10.5 | fundamental character $\omega$ (B-C15(b)) |
| $\chi_d$ | quadratic character of $\Q(\sqrt d)$ | ch:galois C3, galois:quadratic-characters; ch:rings 9.5 | numerical subscripts always $\chi_d$ (B-C6(b)) |
| $\chi_{-3}$, $\chi_{-4}$ | characters of $\Q(\sqrt{-3})$, $\Q(i)$ | ch:rings 10.5; ch:ant 5.8 | $\chi_{-3}=\bar\chi_3$ |
| $\chi_{q^*}$ | quadratic character of conductor $q$ (the paper writes $\chi_q$; never in the book, D3) | ch:rings C5; ch:galois C3; B-C6(c) | the paper's $\chi_q$ **clashes** with $\chi_\ell$ when $q=\ell$ (point 32) |
| $\chi_{\ell^*}$ | character of $\Q(\sqrt{\ell^*})$, $=\bar\chi_\ell^{(\ell-1)/2}$ | ch:galois C4 | $=\bar\chi_\ell$ iff $\ell=3$ |
| $\chi_S$, $D$ | $\prod_{q\in S}\chi_{q^*}$, its conductor $\prod_{q\in S}q$ | ch:hecke C7; ch:ellcurves 10.6 | $D$ (B-C15(d)) |
| $\varepsilon$ | unramified character of order $\le2$ of $G_{\Q_q}$ | ch:local 7.6; ch:galrep 3.2; B-C14 | $\varepsilon_N(f)$, Chapter 1's non-square |
| $\chi(\Frob_p)=\chi(p)$ | Dirichlet characters as Galois characters | ch:ant 5.7; ch:modgalrep C3 | - |
| $\Z_\ell(1)$, $M(n)$ | Tate module of $\mu$, Tate twists | ch:galois C6; ch:blochkato 2.2; B-C5 | - |
| $\Q(\sqrt{\ell^*})$ | quadratic subfield of $\Q(\zeta_\ell)$ | ch:galois galois:sqrt-lstar; ch:ant 5.3 | - |
| $\Gal(\overline\Q/\Q(\sqrt{\ell^*}))$ | the group on which $\bar\rho$ must be absolutely irreducible | ch:galois galois:restriction | - |
| $\chi_a$, $\kappa_x$ | Kummer character of $a$; Kummer cocycle of $x\in K^\times$ | ch:galois galois:kummer-character, galois:l-adic-kummer; ch:local 6.2 | - |
| $\theta_m$ | tame character $I_K\to\mu_m$ | ch:local 5.3 | $\theta=\rho\vert_{I_q}$ (ch:lfunctions 10.1, local) |
| Artin map | uniformiser to arithmetic Frobenius | ch:ant 5.6; ch:local 6.5 | Deligne's convention opposite (B-C2(g)) |
| $\mathrm{Art}$ | local Artin map | ch:local 6.5 | - |
| density | Dirichlet density | ch:galois galois:density | - |

### 2.4 Local fields and Weil-Deligne representations

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $K$, $\mathcal O_K$, $\mathfrak m_K$, $\varpi_K$, $k_K$, $v_K$ | a $p$-adic field and its data | ch:local L1 | ch:reduction R1 writes $\pi$ for the uniformiser (L1) |
| $\Q_p^{\mathrm{ur}}$, $K^{\mathrm{tame}}$ | maximal unramified, tame extensions | ch:local L2, 4.2 | - |
| $I_K$, $P_K$, $I_K^{(\ell)}$ | inertia, wild inertia, maximal pro-$\ell$ quotient of $I_K$ | ch:local L2, 5.2, 5.3 | - |
| $t_\ell\colon I_K\to\Z_\ell(1)$, $t_\zeta$ | tame character; its $\Z_\ell$-valued version | ch:local 5.3, L5 | **clash**: $t_\ell(E,q)$ (B-C15(i)) |
| $t$ | topological generator of tame (pro-$\ell$) inertia | ch:local 5.3(iii); ch:cohomology tame-inertia-example | - |
| $W_K$, $d(w)$, $\lVert w\rVert$ | Weil group, its degree map, $q^{d(w)}$ | ch:local 7.1, L4 | $W$, $W_N$ |
| $(r,N)$, $\mathrm{WD}(\rho)$ | Weil-Deligne representation | ch:local 7.3, 7.4 | $N$ (B-C15(f)) |
| $\mathrm{sp}(n)$ | special (Steinberg) representation | ch:local 7.5 | - |
| $a(V)$, $\operatorname{sw}(V)$ | Artin conductor exponent, Swan conductor | ch:local 8.3, 8.4 | $a_p$ coefficients |
| $L(V,s)$, $L_p(V,s)$ | local $L$-factor, with $\Phi$ | ch:local 8.2; B-C2(d) | - |
| $\epsilon(r,\psi,dx)$ | local epsilon factor | ch:local 8.5 | - |
| $\Q_p^\times=p^\Z\times\mu_{p-1}\times(1+p\Z_p)$ | structure of $\Q_p^\times$ | ch:local 2.5 | - |
| $\omega$, $\omega_2$ | fundamental characters of levels $1$, $2$ at $\ell$ | ch:galrep 5.2 | **clash**: periods $\omega_1,\omega_2$, differentials (B-C15(b)) |
| $\pi_p$, $\mathrm{WD}_p(f)$ | local component of $f$; its Weil-Deligne representation | ch:modgalrep C5, 3.3 | **clash**: Frobenius endomorphism $\pi_p$ (Chapters 8, 9, 14 only; B-C15(a)) |
| $D_{\mathrm{cris}}$, $B_{\mathrm{cris}}$, $B_{\mathrm{dR}}$, $B_{\mathrm{st}}$ | Fontaine's rings and functor | ch:blochkato 4.1 | - |

### 2.5 Curves, elliptic curves, reduction, Tate curves

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $g$ | genus | ch:curves C2, 5.3 | newform $g$; generator $g$ (local) |
| $\varphi^*$, $\varphi_*$ | pullback, pushforward | ch:curves C4; B-C4(e) | Pontryagin $^*$ on modules |
| $\mathcal C$, $\mathcal C^t$, $\mathcal C^*$, $\mathcal C_*$ | correspondence, transpose, its actions | ch:curves 12.1, 12.2 | - |
| $A^\dagger$ | adjoint for a pairing | ch:curves C4, 12.3; B-C4(d) | ch:modules writes $A^*$ (D1) |
| $H_1(X,\Z)$, $H^1(X,\Z)$, $H^1(X,\Z_\ell)$ | homology, cohomology of a curve | ch:curves 10.1, 10.2 | - |
| $\langle\ ,\ \rangle$ (cup product) | $\int_X\alpha\wedge\beta$ | ch:curves C6, 10.3 | Petersson product (B-C8) |
| $\operatorname{PD}$ | Poincare duality $H^1\to H_1$ | ch:curves C6, 10.3 | - |
| $\operatorname{Pic}^0$, $J(C)$, $T_\ell J$ | Picard group, Jacobian, Tate module | ch:curves 4.2, 11.1, 11.7 | - |
| $\deg\varphi$ | degree of a morphism of curves | ch:curves 6.2 | - |
| $a_1,\dots,a_6$; $b_2,\dots,b_8$; $c_4,c_6$; $\Delta$; $j$ | Weierstrass data | ch:ellcurves 1.1, C3 | $\Delta$, $c$ (B-C15(h)) |
| $\omega_E$ | invariant (Neron) differential $dx/(2y+a_1x+a_3)$ | ch:ellcurves C3; ch:moddeg C4 | $\omega$ (B-C15(b)) |
| $E[m]$, $E(K)$, $E(\Q)_{\mathrm{tors}}$ | torsion, points, torsion subgroup | ch:ellcurves 3.5, 9.1, 9.3 | - |
| $\psi_m$ | division polynomials, $\psi_2=2y+a_1x+a_3$ | ch:ellcurves 4.1 | $\psi$ (B-C15(m)) |
| $e_m$ | Weil pairing (Silverman's) | ch:ellcurves 5.1, C7 | - |
| $\hat\varphi$, $[m]$ | dual isogeny, multiplication by $m$ | ch:ellcurves 3.4, 3.5 | - |
| $T_\ell E$, $V_\ell E$ | Tate module, $T_\ell E\otimes\Q_\ell$ | ch:ellcurves 5.3 | paper's $T$, $V$ (Section 1.1) |
| $\Lambda_E$, $\operatorname{vol}(\Lambda_E)$, $\omega_1,\omega_2$ | period lattice of $\omega_E$, its covolume, periods | ch:ellcurves 7.1, 7.6 | $\omega_2$ (B-C15(b)); PARI `E.area` |
| $\mathfrak H$, $\mathfrak H^*$ | upper half plane, with cusps | ch:modforms C1; ch:ellcurves 7.5 | star exception |
| $a_p(E)$, $a_{\mathfrak q}$ | $p+1-\#\tilde E(\F_p)$ | ch:ellcurves 8.1, 8.6 | $a(V)$ conductor |
| $\alpha$, $\beta$ | roots of $X^2-a_pX+p$ | ch:ellcurves 8.3; B-C3 | arithmetic eigenvalues on $V_\ell E$ |
| $E^{(d)}$, $E^{(q)}$ | quadratic twist by $\Q(\sqrt d)$; by $\Q(\sqrt{q^*})$ | ch:ellcurves 10.1, 10.5; ch:reduction 8.2 | depletion superscripts (H3, H4) |
| $E'$ | twist $E^{(q)}$ of good reduction at an $\mathrm I_0^*$ prime (paper's table); in thm:qual, $E^{(q)}$ | ch:ellcurves 10.5 | - |
| $E_S$, $N_S$ | $E\otimes\chi_S$, its conductor; the paper's $E_{\{p\}}$ (proof of thm:main) and $E_q$ (after thm:twist) are $E^{(p)}$, $E^{(q)}$ | ch:ellcurves 10.6 | the Tate curve is $E_{\mathsf q}$, not $E_q$ (L5) |
| $L(E,s)$, $L_p(E,s)$ | Hasse-Weil $L$-function | ch:ellcurves 11.1; ch:lfunctions 5.1 | $L_p(E,s)=L_p(V_\ell E^\vee,s)$ (B-C3) |
| CM, $j$-invariants | complex multiplication | ch:ellcurves 6.3, 6.4 | - |
| 11a1, 121c, 99A1, 11.a2 | Cremona, ARS12, LMFDB labels | ch:ellcurves 12.1, C6; B-C16 | - |
| minimal model, $\Delta_{\min}$ | (global) minimal Weierstrass model | ch:reduction 1.1, 1.3 | - |
| $E_0(K)$, $E_1(K)$, $\tilde E_{\mathrm{ns}}$ | filtration of $E(K)$; nonsingular points of the reduction | ch:reduction 2.3, 2.4 | $E_0$ also the optimal curve of the class (paper Section 3) |
| $\mathcal E$, $\Phi_q(\cdot)$ | Neron model; its component group scheme | ch:reduction 4.1, 4.2; B-C11(b) | **clash**: $\Phi_p$ geometric Frobenius |
| $\Phig_q$ | geometric component group $\Phi_q(\overline\F_q)$ | ch:reduction R4, 4.2; paper Section 1.4 | ch:galrep writes $\Phi_q$ (K1) |
| $c_q$, $c_p$ | Tamagawa number $\#\Phi_q(\F_q)$ | ch:reduction 4.4 | never for $\#\Phig_q$ or $c(u)$ |
| $\mathrm I_n,\dots,\mathrm{II}^*$ | Kodaira symbols | ch:reduction 5.1; B-C11(a) | - |
| Kodaira code $k$ | PARI's code, `K[i][2]` | ch:reduction 5.5; B-C11(c) | valid formula $\pm(n+4)$ only for $n\ge1$ |
| $m_p$ | number of components of the special fibre | ch:reduction 6.2 | - |
| $f_p$, $N$ | conductor exponent, conductor $\prod p^{f_p}$ | ch:reduction 6.1, 6.4 | $f$ newform; $N$ monodromy |
| $\operatorname{sw}_p(E)$ | wild part of $f_p$ | ch:reduction R5 | - |
| $G_{\mathrm{ss}}$, $e$ | semistability group, defect $12/\gcd(v_p(\Delta),12)$ | ch:reduction R6, 6.5, 6.6 | never $\Phi_K$ |
| $E_{\mathsf q}$, $\mathsf q$ | Tate curve, its parameter variable | ch:reduction 7.1 | $q$ (B-C1) |
| $q_E$ | Tate parameter of $E$ | ch:reduction 7.4; B-C14 | never $u$ |
| $n$, $n_q$ | $v_q(\Delta_E)=v_q(q_E)$ at a multiplicative prime | ch:galrep C2; paper lem:tamagawa-exp | - |
| $\nu$ | $v_q(q_E)=-v_q(j_E)$ | ch:blochkato C6; B-C14 | - |
| $u$, $\bar u$ | unit part $q_Eq^{-\nu}$, its reduction | ch:reduction 7.4; B-C14 | the paper's lem:tamagawa-exp calls $q_E$ "$u$" (point 8) |
| $c(u)$ | class of $\bar u$ in $\F_q^\times/(\F_q^\times)^{\ell^{v_\ell(q-1)}}$ | ch:rings 7.2; ch:reduction 7.4; ch:blochkato C6 | paper's $c$, $c_q$ (point 23) |
| $w_\ell(E,q)$ | twist-symmetrised weight | ch:reduction 8.4; ch:paper A1.6 | $w_N$, $w$ |

### 2.6 Galois representations of elliptic curves and of newforms

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $\rho=\rho_{E,\ell}$, $\bar\rho=\bar\rho_{E,\ell}$ | action of $G_\Q$ on $T_\ell E$, on $E[\ell]$ | ch:ellcurves 5.4; ch:galrep 1.1, C1 | - |
| $\rho\bmod\ell^k$ | action on $E[\ell^k]=T/\ell^kT$ | ch:galois C5; ch:galrep C1 | - |
| $V$, $T$ | $V_\ell E$, $T_\ell E$ (paper Section 1.1) | ch:galrep C1 | $V_d$, $V_f$, Verschiebung (B-C15(j)); $T$ matrix, $\T$ |
| $A$, $A_f$ | $\ad T$, $\ad V$ | ch:galrep C1; B-C12(b) | **clash**: Shimura's abelian variety, renamed $J_f$ (A1, A2) |
| $\delta_p$ | $\dim V^{I_p}$: $2,1,0$ for good, multiplicative, additive $p\ne\ell$ | ch:galrep 3.5; ch:local 8.1 | defined for $p\ne\ell$ only (point 72) |
| absolutely irreducible | irreducible over $\bar k$ | ch:reps 2.3 | - |
| $N(\bar\rho)$, $k(\bar\rho)$ | Serre conductor, Serre weight | ch:galrep 6.1; ch:modgalrep 5.1 | - |
| $\delta(\bar\sigma)$ | DDT's exponent at $\ell$ in the optimal level theorem | ch:modgalrep 6.4 | $\delta_p$, $\hat\delta_!$ (B-C15(l)) |
| $\bar\sigma$ | a mod $\ell$ representation in DDT 3.15 | ch:modgalrep 6.4 | - |
| $\rho_{f,\lambda}$, $\bar\rho_{f,\lambda}$, $V_\lambda(f)$ | Galois representation of a newform | ch:modgalrep 2.1 | normalised by $\det(X-\rho(\Frob_p))=X^2-a_pX+p$ |
| $h_\ell(E)$ | length of $H^0(\Q,\ad T(1)\otimes\Q_\ell/\Z_\ell)$ | ch:galrep 8.5; ch:blochkato 10.3 | $h_\ell(E)=0$ for $\ell\ge5$, $h_3\le1$ (point 5) |
| $S_f$ | DFG04's exceptional set: $\lambda\mid2N$ or $\bar\rho$ not absolutely irreducible on $G_{\Q(\sqrt{\ell^*})}$ | ch:galrep 8.6; ch:blochkato 10.1 | $S$, $S_2$ |
| $D_\ell$ | decomposition group at $\ell$ | ch:ant 3.10 | - |
| $\iota$ ($T\to V$) | $H^1(K,T)\to H^1(K,V)$ | ch:galcoh C4 | **clash**: twist map $\iota$ (B-C15(c)) |

### 2.7 Modular forms, Hecke algebras, modular curves, the modular degree

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $\Gamma_0(N)$, $\Gamma_1(N)$, $\Gamma(N)$ | congruence subgroups | ch:modforms 3.1 | - |
| $\mu(N)$ | $[\SL_2(\Z):\Gamma_0(N)]=N\prod_{p\mid N}(1+p^{-1})$ | ch:modforms C7 | $\mu_n$ (B-C15(g)) |
| $\nu_2(N)$, $\nu_3(N)$, $\nu_\infty(N)$ | elliptic points, cusps | ch:modforms C7, 4.3 | $\nu$ (B-C14) |
| $Y_0(N)$, $X_0(N)$, $X_1(N)$ | modular curves | ch:modforms 5.1, 5.2; ch:moddeg 2.1 | - |
| $q=e^{2\pi iz}$ | $q$-expansion variable | ch:modforms C1 | $q$ prime (B-C1) |
| $f\vert_k\gamma$ | slash operator with $(\det\gamma)^{k/2}$ | ch:modforms C3, 6.1; B-C5(d) | - |
| $M_k$, $S_k$, $S_2(\Gamma_0(N))$, $S_2(N;A)$ | modular and cusp forms; integral forms | ch:modforms 6.2, 11.1, C6; ch:hecke C1 | - |
| $a_n(f)$ | $n$-th coefficient at $\infty$ | ch:modforms C6 | - |
| $\langle f,g\rangle$ | Petersson product, unnormalised | ch:modforms C5, 10.1; B-C8 | cup product |
| $f^\perp$ | Petersson orthogonal complement | ch:modforms 10.3; ch:hecke 5.4 | not the $\T$-stable complement when $U_p$ is involved (point 61) |
| $E_k$, $\Delta(z)$, $j(z)$, $\eta(z)$ | Eisenstein series, discriminant form, $j$, Dedekind eta | ch:modforms 7.1, 7.2, 9.1 | $\Delta$, $\eta$ (B-C15(h)) |
| $B_k(N)$ | Sturm bound | ch:modforms C7, 11.3 | $B_E$ |
| $W_N$, $w_N$, $W_d$ | Atkin-Lehner matrix and involution | ch:modforms C4, 12.1 | $w$ |
| $\varepsilon_N(f)$ | eigenvalue of $w_N$ on a newform | ch:hecke 10.2; ch:moddeg 9.2 | - |
| $T_n$, $T_p$, $U_p$ | Hecke operators; $U_p=T_p$ for $p\mid N$ | ch:hecke C3, 2.4 | level-dependence $T_p^{(M)}$ |
| $[\Gamma\alpha\Gamma]_k$ | double coset operator | ch:hecke C2, 2.1 | - |
| $\T$, $\T_N$, $\T^{(N)}$, $\T_\ell$, $\T_A$ | full Hecke algebra, anemic algebra, scalar extensions | ch:hecke C4, 3.1; B-C13(a) | - |
| $\phi_f$ | eigencharacter $\T\to\mathcal O_f$ | ch:hecke 3.2, 3.4; ch:modgalrep C1 | ch:hecke C5 writes $\varphi$ (H1) |
| $I$, $J$ (lem:crit) | $\ker\phi_f$, $\Ann_\T(f^\perp)$ | ch:modgalrep 8.2; B-C13(c) | **clash**: $I=\Ann\wp$ in lem:ddt417; $I_p$ inertia |
| $I_f$ | $\ker\phi_f$ (Chapter 14) | ch:moddeg 5.1 | - |
| $r_E$, $r$ | congruence number | ch:moddeg 8.1; ch:modgalrep 8.1 | - |
| $f^\Sigma$, $f^{\{p\}}$, $f^S$ | depletion | ch:hecke C8, 7.4; B-C13(e) | not $h^{(p)}$ (H3, H4) |
| $M^\Sigma$ | $M\prod_{p\in\Sigma}p^{\delta_p}$, level of $f^\Sigma$ | ch:hecke 7.4; paper Section 4.1 | - |
| $V_d$ | $h(z)\mapsto h(dz)$ | ch:hecke C3 | $V$ |
| $f\otimes\chi$, $f^\chi$ | naive twist, newform twist | ch:hecke 9.1; ch:modgalrep C4, 2.7 | - |
| $\iota$ | twist map $h\mapsto h\otimes\chi_S$ | ch:hecke 9.1; ch:modgalrep 10.1 | $\iota$ of Chapter 17 (B-C15(c)) |
| $L(f,s)$ | $L$-function of a newform | ch:hecke 10.1 | - |
| $\alpha_p$, $\beta_p$, $\mu_p$ | roots of $X^2-a_p(h)X+p$; chosen $U_p$-eigenvalue (lem:old) | ch:hecke 7.1; ch:modgalrep 8.3 | B-C3(e) |
| $J_0(N)$, $J_1(N)$ | Jacobians | ch:moddeg 4.1 | - |
| $t^*$, $t_*$ | the two Hecke actions (on $H^1$, on $H_1$) | ch:moddeg C2, 4.2 | pullback star (B-C4(e)) |
| $J_f$, $\pi_f$, $E_f$ | $J_0(N)/I_fJ_0(N)$, the quotient map; the elliptic curve for rational $f$ | ch:moddeg 5.1 (written $A_f$ there); B-C12(c) | renamed (A1) |
| $\varphi_E$, $\deg\varphi_E$ | modular parametrisation, modular degree (macro `\degphi`) | ch:moddeg 6.1, 6.2 | ch:modgalrep writes $\phi$ (H2) |
| $E_0$ | the optimal curve of the class (paper Section 3) | ch:modgalrep 2.6 | $E_0(K)$ |
| $c_\varphi$, $c_E$ | Manin constants | ch:moddeg 7.1; B-C9 | never bare $c$ |
| $\hat\delta_!$ | $\langle x,w_Ny\rangle$ on $H^1(X_0(N),\Z_\ell)$ | ch:moddeg 3.4; B-C13(f) | ch:moddeg writes $\hat\delta$ (H5) |
| $M_{f,\lambda}$, $M_{f^\Sigma,\lambda}$ | $H^1(X_0(M^\Sigma),\Z_\ell)[\ker\phi_{f^\Sigma}]$, rank two | ch:moddeg 4.4, 9.1; paper Section 4.1 | ch:moddeg writes $M_{f,\ell}$ (H5) |
| $\mathfrak m$ | maximal ideal of $\T\otimes\Z_\ell$ attached to $(f,\ell)$ | ch:moddeg 10.1 | $\mathfrak m_K$ |
| $I_{\mathrm{Eis}}$, $C_N$, $\mathcal S_N$ | Eisenstein ideal, cuspidal subgroup, Shimura subgroup | ch:moddeg 11.1 to 11.3 | ch:moddeg writes $\Sigma_N$ (L4) |
| $\delta_D$ | degree of the Shimura curve parametrisation (Ribet-Takahashi) | ch:moddeg 12.2 | - |

### 2.8 Cohomology, Selmer groups, Tamagawa factors

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $C^n(G,M)$, $Z^1$, $B^1$ | inhomogeneous cochains, cocycles, coboundaries | ch:cohomology inhomogeneous-cochains, h0-h1 | $C_n$ cyclic group |
| $H^n(G,M)$, $H^n(K,M)$ | (continuous) group and Galois cohomology | ch:cohomology continuous-cohomology, galois-cohomology-convention; ch:galcoh 1.1 | types (D), (C), (V) of coefficients |
| $\hat H^n$ | Tate cohomology | ch:cohomology tate-cohomology | - |
| $\Res$, $\Inf$, $\Cor$ | restriction, inflation, corestriction | ch:cohomology res-inf-cor | - |
| $(\sigma\cdot c)(h)=\sigma c(\sigma^{-1}h\sigma)$ | conjugation action of $G/H$ on $H^n(H,M)$ | ch:cohomology conjugation-action; B-C5(d) | - |
| $n'$ | $v_\ell(n')=v_\ell(n)$, the unipotent entry of $\rho(t)$ | ch:cohomology model-setting | - |
| $\kappa$, $\kappa_q$, $\kappa_u$ | Kummer cocycle of $q_E$, of $q$, of $u$ | ch:galcoh 1.5, 5.3; B-C14 | $\kappa$ bijection of ch:ellcurves 2.3 (local) |
| $c'$ | $\varepsilon(\Frob)\kappa(\Frob)$, well defined modulo $(n,q-1)$ | ch:galcoh 5.4; ch:cohomology frobenius-on-h1-inertia | - |
| $H^1_{\mathrm{ur}}(\Q_p,M)$ | $\ker(H^1(\Q_p,M)\to H^1(I_p,M))=M^{I_p}/(\Frob-1)M^{I_p}$ | ch:galcoh 4.1, 4.2 | macro `\Hur` |
| $T$, $V$, $W$ | lattice, $T\otimes\Q_\ell$, $T\otimes\Q_\ell/\Z_\ell$ | ch:galcoh C4 | in the paper $W=A\otimes\Q_\ell/\Z_\ell$ (B-C12(b)) |
| $T^D$, $V^D$, $W^D$ | Kummer duals: $\Hom(T,\Z_\ell(1))$ etc.; **in the paper and Chapters 18, 20, 21 built from $A=\ad T$** | ch:galcoh C3, 2.1; ch:blochkato C2, 2.3, 6.6 | **clash**: paper's $T^D$ is $A^D$, not $(T_\ell E)^D$ |
| $M^*(1)$ | $\Hom(M,\mu_{\ell^\infty})$ for finite or discrete $M$, $=M^D$ | ch:galcoh C3 | - |
| $\mathrm{Sel}_n(E/\Q)$, $\Sha$ | $n$-Selmer group, Shafarevich-Tate group | ch:galcoh 7.3 | - |
| $\mathcal L$, $\mathcal L^*$, $H^1_{\mathcal L}$ | Selmer structure, dual structure, Selmer group | ch:galcoh 8.1, 8.2 | star exception (B-C4(e)) |
| $\mathcal L^\Sigma$, $\mathcal L_\Sigma$ | relaxed and strict at $\Sigma$ | ch:galcoh 8.2 | - |
| $H^1_f(\Q_p,M)$, $H^1_f(\Q,M)$ | Bloch-Kato local conditions and Selmer groups | ch:blochkato 5.1, 5.2, 6.1 | macro `\Hf` |
| $H^1_g$, $H^1_e$ | other Bloch-Kato conditions | ch:blochkato 5.1 | - |
| $H^1_\Sigma(\Q,W)$ | $\Sigma$-imprimitive Selmer group of DFG04 2.1 | ch:blochkato 6.3, 6.6 | - |
| $\Tam_p(M)$ | $\Fitt_{\Z_\ell}((H^1(I_p,M)_{\mathrm{tor}})^{G_{\Q_p}})$ | ch:blochkato 7.1; B-C10 | point 37 (placement of the invariants) |
| $\Sigma$ | the paper's finite set of primes (in thm:main, the primes dividing $N$) | ch:galcoh C5; ch:blochkato C1 | $\mathcal S_N$; in thm:quant $\Sigma=S$ |
| $G_\R$, $H^1(\R,M)$ | the real place | ch:galcoh C1, 6.4 | killed by $2$ |
| $X^*$ | Pontryagin dual | ch:modules 8.1, 8.2; B-C4(b) | pullback stars on maps |
| $\ad M_f$ | the adjoint motive | ch:blochkato 14.1 | - |

### 2.9 $L$-functions and the paper's local terms

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $\zeta(s)$, $\zeta^{(N)}(s)$ | Riemann zeta; with the factors at $p\mid N$ removed | ch:lfunctions 3.1, 3.2 | $\zeta_n$ roots of unity |
| $L(s,\chi)$, $\zeta_K(s)$ | Dirichlet and Dedekind $L$-functions | ch:lfunctions 3.3, 3.4 | - |
| $\Gamma_\R$, $\Gamma_\C$ | $\pi^{-s/2}\Gamma(s/2)$, $2(2\pi)^{-s}\Gamma(s)$ | ch:lfunctions 2.3, 7.2 | $\Gamma_0(N)$ |
| $L_p(M,s)$ | $\det(1-\Phi_pp^{-s}\mid M^{I_p})^{-1}$ | ch:lfunctions 4.1, C3; ch:local 8.2; B-C2(d) | - |
| $L(\ad f,s)$, $L(A_f,s)$ | adjoint $L$-function | ch:lfunctions 6.1, C4; B-C7 | - |
| $L(\Sym f,s)$ | symmetric square, $=L(\ad f,s-1)$ | ch:lfunctions 6.1, C4; B-C7 | never the Rankin series |
| $L_p^{\nv}$, $L^{\nv}$ | naive factors and naive $L$-function (macro `\nv`) | ch:lfunctions 8.1, C6; B-C7 | - |
| $D(f,s)$ | Rankin series $\sum a_n(f)^2n^{-s}$ | ch:lfunctions C4, 8.2 | $D$ (B-C15(d)) |
| $P_q(X)$ | $L_q(\Sym f,s)=P_q(q^{-s})^{-1}$ | ch:lfunctions C5 | - |
| $e_\ell(E,q)$ | $v_\ell(P_q(q^{-2})/(1-a_q^2q^{-2}))$, the omitted Euler factor | ch:lfunctions 9.1; ch:paper A1.1 | not twist-invariant (point 15) |
| $t_\ell(E,q)$ | $v_\ell(-v_q(j_E))$ if $v_q(j_E)<0$, else $0$ | ch:lfunctions 9.1; ch:paper A1.1 | tame character $t_\ell$ (B-C15(i)); extended to $q=\ell$ (point 53) |
| $t_q$, $t_f(q)$ | Tamagawa exponent (Kim-Ota): largest $t$ with $\rho\bmod\ell^t$ unramified at $q$ | ch:modgalrep 11.1 | $=t_\ell(E,q)$ at multiplicative $q$ |
| $N_{\ad}$ | conductor of $A_f$ | ch:lfunctions 7.2 | - |
| $\Lambda(\ad f,s)$ | completed adjoint $L$-function | ch:lfunctions 7.1 | $\Lambda_E$ |
| $B_E$ | $N\,L(\ad f,1)/(2\pi\operatorname{vol}(\Lambda_E))$ | ch:lfunctions 8.4 | $B_k(N)$ |
| $\varepsilon$ (root number) | sign of a functional equation | ch:lfunctions 7.1; ch:hecke 10.2 | $\varepsilon$ characters (B-C15(k)) |

### 2.10 Congruence ideals and the theorems of Diamond, Flach and Guo (Chapter 20, outlined in parallel)

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $\pi\colon\T\to\mathcal O$, $\wp$, $I=\Ann_\T\wp$, $\eta=\pi(I)$ | the data of lem:ddt417 | ch:modules 11.1, 11.3; ch:congruence | **clash**: $I$ of lem:crit (B-C13(c)); $\pi$ (B-C15(a)) |
| $d$, $\Delta$, $Q$ | rank of $L[\wp]$, its Gram determinant, $L/(L[\wp]\oplus L[I])$ | ch:modules 11.3; ch:congruence | $\Delta$ discriminant |
| $M(M^\Sigma,1)_{!,\lambda}$ | DFG04's integral structure, $=H^1(X_0(M^\Sigma),\Z_\ell)$ | ch:congruence; paper Section 4.1 | - |
| $\eta^\Sigma_{f,\lambda}$, $\eta^\emptyset_{f,\lambda}$ | naive $\Sigma$-finite congruence ideal; level $N$ | ch:congruence; paper Section 4.1 | $\eta(z)$ |
| $\eta^{\mathrm{Hecke}}(g^S)$ | congruence ideal of $g^S$ in $\T$ | ch:hecke 4.3; ch:congruence | - |
| $R_\Sigma$, $\T_\Sigma$ | deformation ring, Hecke algebra of Taylor-Wiles | ch:congruence; ch:modgalrep 11.5 | - |
| $g$, $g^S$ | $f_{E_S}$, its $S$-depletion (thm:quant) | ch:modgalrep 10.1; ch:congruence | genus $g$ |
| $N_S^\Sigma$ | $N_S\prod_{q\in S}q^{\delta_q(g)}=N$ | ch:modgalrep 10.1 | - |

### 2.11 The paper's named quantities, statements and data

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $w_3(E)$ | weight of the prime $3$ in Conjecture conj:euler | ch:paper A1.5 | $w_\ell(E,q)$ |
| $D$ (conj:eis) | deficit $\sum_qv_\ell(\#\Phig_q)-v_\ell(\deg\varphi_E)$ | ch:paper A1.13 | $D$ (B-C15(d)) |
| $[\,\cdot\,]$ | Iverson bracket ($1$ if true, $0$ if false) | ch:paper A1.5, A1.13 | - |
| $\mathrm{(eq{:}main)}$, $\mathrm{(eq{:}twist)}$, $\mathrm{(eq{:}rule)}$, $\mathrm{(eq{:}identity)}$, $\mathrm{(eq{:}thm)}$ | the paper's displayed inequalities | ch:paper A1.4, A1.5, A1.7 | cited by these names |
| $E[3]\simeq\Z/3\oplus\mu_3$ | the image 3Cs.1.1 | ch:galrep 9.2; ch:ellcurves 9.7 | not "the split Cartan image" (point 44) |
| working set, hold-out, extension, out-of-table | the four data ranges | ch:computation; ch:paper A6.1 | - |

### 2.12 Computation (Chapter 22, outlined in parallel)

| symbol | meaning | defined in | conflicts and notes |
|-|-|-|-|
| `rule(E, l, iii)` | the paper's function returning $[v_\ell(\deg\varphi_E),\text{bound}]$ | ch:computation; ch:lfunctions 11.2; ch:paper A9.1 | - |
| `ns3(E)` | $1$ iff $\psi_3$ factors as two quadratics | ch:computation; ch:paper A9.1 | the correction $h_3$ |
| `R[4]`, `R[5]`, `K[i][2]` | `ellglobalred` output: bad primes, local data, Kodaira code | ch:computation; ch:reduction 5.5 | B-C11(c) |
| `lfunsympow(E,2)`, `lfuneuler` | $L(\Sym f,s)$ and $1/P_q(x)$, $x=q^{-s}$ | ch:lfunctions C5, 11.1 | normalisation B-C7 |
| `mfpetersson` | Petersson product divided by $\mu(N)$ | ch:modforms C5 | B-C8 |
| `E.area` | $\operatorname{vol}(\Lambda_E)$ | ch:lfunctions C9 | - |
| `ellmoddegree`, `elldivpol`, `ellinit` | modular degree, division polynomial, curve | ch:computation | - |
| `ecdata` files | Cremona's tables (allcurves, alldegphi, ...) | ch:computation | - |

### 2.13 Decorations and operators

| decoration | meaning | defined in | conflicts and notes |
|-|-|-|-|
| $M^\vee$ | linear dual | B-C4(a) | - |
| $X^*$ | Pontryagin dual (modules) | B-C4(b) | pullback $\varphi^*$ (maps); exceptions in B-C4(e) |
| $M^D$ | Kummer dual $M^\vee(1)$ or $M^*(1)$ | B-C4(c) | $D$ |
| $A^\dagger$ | adjoint of an operator | B-C4(d) | - |
| $\varphi^*$, $\varphi_*$ | pullback, pushforward | B-C4(e) | - |
| $A^{\mathsf T}$, $\mathcal C^t$ | transpose | B-C4(f) | - |
| $\hat\varphi$, $\hat\pi_q$ | dual isogeny | B-C4(f) | $\hat\delta_!$, $\hat H$ |
| $M(n)$ | Tate twist | B-C5(a) | - |
| $\rho^{ss}$ | semisimplification | ch:reps 3.5 | - |
| $\bar\rho$, $\bar\chi_\ell$, $\bar u$ | reduction mod $\ell$ (or mod $q$) | ch:galois C5 | complex conjugate $\bar z$ |
| $M^G$, $M^{I_p}$ | invariants | ch:cohomology h0-h1 | - |
| $f^\Sigma$ | depletion | B-C13(e) | - |
| $(\cdot)^{(N)}$ | with the factors at $N$ removed; anemic | B-C13(e) | - |
| $E^{(d)}$ | twist of a curve | B-C13(d) | - |
| $f^\chi$, $f\otimes\chi$ | newform twist, naive twist | B-C13(d) | - |
| $S^\perp$, $f^\perp$ | orthogonal complement | ch:modules C5; ch:modforms 10.3 | - |
| $\mathrm{II}^*$ etc., $q^*$, $\ell^*$, $\mathfrak H^*$, $E_2^*$, $\mathcal L^*$ | the fixed exceptions to B-C4(e) | B-C4(e) | - |
| $(\cdot)_{\mathrm{tor}}$ | torsion submodule | ch:modules C3 | - |
| $[\ell\mid n]$ | Iverson bracket | ch:paper A1.13 | - |

Number of index rows: 2.1: 35, 2.2: 23, 2.3: 25, 2.4: 15, 2.5: 44, 2.6: 14, 2.7: 39, 2.8: 23, 2.9: 16, 2.10: 8, 2.11: 6,
2.12: 8, 2.13: 19; in all 275 rows, carrying 490 symbol entries (the math or code items of the first column; several rows carry two to six related symbols).

________________________________________________________________________________

## Part 3. Where the outlines disagree with Part 1

Found by searching every outline for `Frob`, `\Phi`, `^*` (with the Kodaira symbols, $q^*$, $\ell^*$ filtered out), `^\vee`,
`dagger`, `chi_`, `c^2`, `Petersson`, and then for the clashes these searches revealed (`\omega`, `A_f`, `\phi`,
`\varphi`, `\pi`, `h^{(p)}`, `\Sigma_N`, `E_q`, `iota`, `n+4`). Line numbers refer to the outline files as of
14 October 2026. "Required" means the outline as written would put a wrong or ambiguous formula into the book;
"cosmetic" means the outline is correct but uses a symbol that Part 1 reserves for something else. The searches for
`c^2` (the Zagier-Watkins formula) and `Petersson` (the normalisation) found **no disagreement**: every outline that
states the formula puts $c^2$ in the numerator (ch:ellcurves line 82, ch:modforms 10.x and B1, ch:moddeg C4 and 7.3,
ch:blochkato 14.7, ch:lfunctions 8.4) and every outline that fixes the Petersson product uses the unnormalised one with
PARI's division by $\mu(N)$ (ch:modforms C5, ch:hecke C6, ch:moddeg C4, ch:lfunctions C9). The searches for the $L(\Sym f,s)$
normalisation, the Tate twist, $v_\ell$, "length" and the tame relation likewise found no disagreement.

### 3.1 By outline

**ch02_rings.md** (`ch:rings`)
* F9 (cosmetic). 6.3 `prop:rings:frobenius`, line 340: "$\phi\colon x\mapsto x^p$" for the Frobenius automorphism of $\F_q$.
  Write $\Frob_p$ (B-C2(a)); $\phi$ is the eigencharacter $\phi_f$ elsewhere.
* D8 (cosmetic). 10.3 and 10.4, lines 522 and 537 to 538: "$\chi^*$" for the primitive character inducing $\chi$. Write
  $\chi^{\mathrm{prim}}$ (B-C4(e): a star on a character is not one of the fixed exceptions).
* L2 (cosmetic). C6, line 90, and 3.4 (and about forty further uses): "$\omega=\zeta_3$". Write $\zeta_3$ (B-C15(b)); if the writer
  keeps $\omega$ for the Eisenstein integers, the chapter's convention box must say that $\omega$ is local to Chapter 2.

**ch03_modules.md** (`ch:modules`)
* D1 (required). 9.5 `prop:modules:adjoint`, lines 592 to 599: the adjoint is written $A^*$ ("$A^*=G^{-1}A^{\mathsf T}G$",
  "$(AB)^*=B^*A^*$", "$A^*=wAw^{-1}$", "$w^*=w$"). Write $A^\dagger$ throughout (B-C4(d)).
* D2 (required). Section 6, notes for the writer ("Three duals"), lines 972 to 974: "The adjoint of an operator is $A^*$
  (9.5)". Replace by $A^\dagger$ and add "($^*$ is the Pontryagin dual only)".
* D3 (cosmetic). Section 5, dependencies, line 944: "$\Hom_G(V,W)=(V^*\otimes W)^G$". Write $V^\vee$.

**ch04_reps.md** (`ch:reps`)
* F3 (required). C8, lines 121 to 122; 9.1(iii), lines 602 to 604; table 9.3, header of the last-but-one column, line 629;
  Exercise 14, line 851; Section 6, line 962; Section 8, line 1053: the **arithmetic** Frobenius is called $\Phi$ ("an abstract
  $\Phi\in\GL(V)$ with $\Phi g\Phi^{-1}=g^q$"; "the geometric Frobenius $\Phi^{-1}$"). This inverts the book's convention. Write $F$
  for the abstract arithmetic Frobenius (as ch:ant 3.12 does) and $F^{-1}$ for the geometric one.
* F3, second half (cosmetic). 7.5 `prop:reps:sym2`, lines 498 to 500; Exercise 10, line 843; verification log, lines 1018 and
  1025: the isomorphism $\Sym V\otimes\det^{-1}\to\ad V$ is called $\Phi$. Rename it $\Xi$ (any letter not taken; $\Psi$ is used by
  ch:moddeg 4.3).

**ch05_galois.md** (`ch:galois`)
* X1 (required). `galois:quadratic-characters` (b), line 532: "$\chi_{-3}=\chi_{-1}\chi_3$" with $\chi_3$ the character of $\Q(\sqrt3)$,
  while the paper's $\chi_3$ is $\chi_{-3}$. Use an example without a numerical $\chi_3$, for instance $\chi_{-15}=\chi_{-3}\chi_5$, or write
  $\chi_{-3}=\chi_{-4}\chi_{12}$.
* X2 (required). Exercise 14 (in the section plan), line 789: "$(\rho\otimes\chi_3)\bmod9$" with the cyclotomic character. Write
  $\chi_3^{\mathrm{cyc}}$ (B-C6(a)).
* Lines 212, 539, 542, 753 used the paper's $\chi_q$ with the letter $q$: converted to $\chi_{q^*}$ under B-C6(c) (decision D3), as is C3.

**ch07_local.md** (`ch:local`)
* X3 (cosmetic). 13.2 (pitfalls), line 974: "the tame $\chi_3=\chi_{-3}$". Write $\chi_{-3}$.
* Lines 359 ("$\chi_p(I_p)=\Z_p^\times$", cyclotomic at $p$ with a letter subscript) and 520 to 535 (now $\chi_{q^*}$, decision D3) comply.
* L4 states the Weil-Deligne relation in both forms; it is the reference for B-C2(f). No change.

**ch08_curves.md** (`ch:curves`)
* F6 (cosmetic). 6.5 `prop:curves:separability-frobenius`, lines 347 to 350: the $q$-power Frobenius morphism is $\phi_q$. Write
  $\pi_q$ (B-C2(g)).
* A3 (required). 11.8, line 604: "$\rho_{f,\lambda}$ via $T_\ell$ of $A_f$". Write $J_f$ (B-C12(c)).
* D9 (cosmetic). C4, lines 88 to 89 and Part 7, lines 1018 to 1019: the remark "Chapter 3 writes $A^*$ for the adjoint" becomes
  stale after D1; replace by "as in Appendix B".

**ch09_ellcurves.md** (`ch:ellcurves`)
* F4 (cosmetic). C5, line 116, and 8.1 `def:ellcurves:frobendo`, line 502: the arithmetic Frobenius of $G_{\F_{\mathfrak q}}$ is
  "$\phi_{\mathfrak q}$". Write $\Frob_{\mathfrak q}$; keep $\pi$ for the Frobenius endomorphism ($\pi_{\mathfrak q}$ when the field must be shown).
* F5 (cosmetic). Section 6, line 974, and Part 8 (B1 extension), line 1074: "$\Frob^{\mathrm{arith}}$", "$\Frob^{\mathrm{geom}}$". Write $\Frob_p$
  and $\Phi_p$. (The mathematics there is right and is the source of B-C3.)
* M4 (cosmetic). Section 0, line 82: "$\degphi=4\pi^2c^2\langle f,f\rangle/\operatorname{vol}(\Lambda_E)$" with a bare $c$. Write $c_E$.
* C5's "$\det(1-\Frob_p\,p^{-s}\mid V_\ell E)^{-1}$ with the arithmetic Frobenius" is a correct identity (B-C3(c)); keep it, and add
  the book's form $L_p(E,s)=L_p(V_\ell E^\vee,s)$ with $\Phi_p$ next to it.

**ch10_reduction.md** (`ch:reduction`)
* L1 (cosmetic). R1, line 93: the uniformiser is $\pi$ ("$\mathfrak m=\pi\mathcal O$", "$v(\pi)=1$"). Write $\varpi$ (B-C15(a)), as Chapters 3 and 7.
* L5 (cosmetic). Lines 43, 61, 747, 750, 856: "$E_q$", "$E_q[\ell^t]$" for the Tate curve, while R1 and 7.1 fix $E_{\mathsf q}$. Write
  $E_{\mathsf q}$ (the paper's $E_q$ is a twist, index entry $E_S$). The same cross-reference phrase occurs in ch:galois line 826,
  ch:local line 993, ch:ellcurves line 938, ch:galrep lines 89 and 831: change there too.
* R3 to R6 and 5.5 are the source of B-C11. No other change.

**ch11_galrep.md** (`ch:galrep`)
* K1 (required). C2, line 115: "$\Phi_q=\Phi_q(\bar\F_q)$ the geometric component group of the Neron model (the paper's $\Phig_q$),
  $c_q=\#\Phi_q(\F_q)$" defines $\Phi_q$ as a group and then evaluates it at $\F_q$. Write "$\Phig_q=\Phi_q(\bar\F_q)$". Then in 2.2
  (lines 203 to 210: "$\Phi_q[\ell^k]$", "$\Phi_q\simeq\Z/n_q$"), 4.6 (line 393), 6.2 (lines 452 to 458: "$a_p(\bar\rho_{E,\ell})=f_p-\dim\Phi_p[\ell]$"),
  the section plan (line 705), the exercises (line 805) and the pitfalls (line 896) write $\Phig_q[\ell^k]$, $\Phig_p[\ell]$, $\#\Phig_q$; keep
  $\Phi_q(\F_q)$ and $\Phi_q(\bar\F_q)$ where they occur (lines 876, 992).
* F8 (required). Section 5, line 838: "$L_q(A_f,s)=\det(1-\Phi_qq^{-s}\mid(\ad V)^{I_q})^{-1}$" in the chapter where $\Phi_q$ is the
  component group. Write $\Frob_q^{-1}$ (B-C2(b); C3 of this very outline says so).
* X5 (cosmetic). 4.3 or its proof, line 334: "$\det\sigma=\chi_3(\sigma)=1$" (cyclotomic). Write $\chi_3^{\mathrm{cyc}}$ or $\chi_\ell$ with $\ell=3$.
* L5: lines 89, 831 (above).

**ch12_modforms.md** (`ch:modforms`)
* L3 (cosmetic). C2, line 85: "$\rho=e^{2\pi i/3}$". Write $\zeta_3$ ($\rho$ is the Galois representation). The matrix $T=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$
  of the same line may stay (B-C15(j)) if the chapter says it is local to Sections 1 and 2.
* M3 (cosmetic). 10.x, line 507; 4.2 of the exercises, line 734; Section 6.1, lines 805 to 806; Part 7 B1, line 951: the Manin
  constant is a bare $c$. Write $c_\varphi$ (general parametrisation) or $c_E$ (optimal curve), B-C9.

**ch13_hecke.md** (`ch:hecke`)
* H1 (cosmetic). C5, line 102: a system of eigenvalues and its generalised eigenspace are $\varphi$, $V(\varphi)$; 8.3, lines 460 to 461
  mix $\varphi$ and $\phi$. Write $\phi$, $V(\phi)$ (B-C13(b)); $\varphi$ is the modular parametrisation.
* H3 (required). C8, line 112 ("$h^{(p)}=h^{\{p\}}$") and 7.1, lines 374 to 375 ("$h^{(p)}=h-a_ph(pz)+p^{k-1}h(p^2z)$"): depletion by a
  parenthesised superscript, which the book reserves for twists $E^{(q)}$. Write $h^{\{p\}}$ only (B-C13(e)).

**ch14_moddeg.md** (`ch:moddeg`)
* A1 (required). 1.1 (line 24), 5.1 (lines 240 to 242: "$A_f:=J_0(N)/I_fJ_0(N)$", "$\pi_f\colon J_0(N)\to A_f$", "$A_f=:E_f$"), 5.2
  (line 252: "$T_\ell A_f$"), the coverage table (line 717), Section 5 (line 831), Section 6.2 (line 857): the abelian variety is $A_f$,
  the paper's adjoint. Write $J_f$ (B-C12(c)).
* F7 (required). C5, line 77, and 5.2, lines 249 to 253: "$F$ the Frobenius endomorphism, $V=pF^{-1}$ the Verschiebung",
  "$(T_p)_*=F+V$", "$F^2-T_pF+p=0$". $V$ is $V_\ell E$ in the paper. Write $\pi_p$, $\hat\pi_p=p\pi_p^{-1}$, $(T_p)_*=\pi_p+\hat\pi_p$.
* M1 (cosmetic). 7.1 (lines 356 to 358, "$c_E$ well defined up to sign"), 7.2 (ii), (iii) and 7.3 (line 372, "$c_E=\pm1$"), 11.4: fix
  the sign of $\omega_E$ by $c_E>0$ and write $c_E=1$ (B-C9).
* L4 (cosmetic). 11.3 `def:moddeg:shimura-subgroup` and line 604 (four occurrences): the Shimura subgroup is $\Sigma_N$, while $\Sigma$
  is the paper's set of primes. Write $\mathcal S_N$.
* H5 (cosmetic). $\hat\delta$ without the subscript (17 occurrences, from 3.4 on) and $M_{f,\ell}$ (22 occurrences, C6 and Section 9):
  the paper writes $\hat\delta_!$ and $M_{f,\lambda}$. Write the paper's symbols, with "$\lambda=\ell$" said once (C6 already says it).

**ch15_modgalrep.md** (`ch:modgalrep`)
* A2 (required). 1.1 (line 26), 1.2 (lines 87, 89), 2.1 (lines 150 to 155: "$A_f=J_0(N)/I_fJ_0(N)$", "$A_f$ is an abelian variety"),
  2.6 (line 196, "$A_f=E_0$"), 4.1 (lines 338 to 339, "$A_f$ has good reduction at $\ell$", "$A_f[\ell^k]$"), the coverage table (line 755),
  Section 5 (line 873), Section 6.3 (line 935): the abelian variety is $A_f$, while 3.7 (line 311, "$A_g=A_f$") uses the paper's
  adjoint. Write $J_f$ for the abelian variety.
* D4 (required). 8.1 `def:modgalrep:congruence-number`, line 495: "$f$ is an eigenvector of the adjoints $T_n^*$, since $T_n^*=T_n$
  for $(n,N)=1$ and $U_p^*=w_NU_pw_N$". Write $T_n^\dagger$, $U_p^\dagger$.
* H2 (required). 1.1 (line 32), 2.6 (lines 196 to 201: "$\phi=\varphi_{E_0}$", "$\phi^*H^1(E_0,\Z_\ell)$", "$\phi_*$"), 6.4 (line 948): the
  modular parametrisation is an upright $\phi$, the letter of the eigencharacter $\phi_f$ (C1 of the same outline). Write $\varphi_{E_0}$.
* H4 (required). C4, lines 117 to 118 ("$h^{(q)}$", "$h^{(S)}$", "$f\otimes\chi=(f^\chi)^{(r)}$"), 1.1 (line 135), 10.1 (lines 653 to 654,
  663 to 664: "$(g^{\chi_S})^{(S)}$", "$\iota(g^{(S)})$"), Exercise 2 (line 812), writer note (line 893): depletion by a parenthesised
  superscript. Write $h^{\{q\}}$, $h^S$, and $(f^\chi)^{\Sigma(r)}$ with $\Sigma(r)$ the set of primes dividing $r$ (B-C13(e)).
* K2 (cosmetic). Section 1.2, line 73 ("$\dim\Phi_p[\ell]$") and 6.x, line 615 ("$\ell$-torsion in $\Phi_q$"): write $\Phig_p[\ell]$, $\Phig_q$.
  Line 379 ("$\Phi_p(\bar\F_p)[\ell]$") complies.

**ch17_galcoh.md** (`ch:galcoh`)
* X4 (cosmetic). 14.4, line 908 ("$\chi_3\chi_{-3}\not\equiv1\pmod9$") and Part 15, line 963 ("$\chi_3(\sigma)=4$"): cyclotomic
  character at $3$ written $\chi_3$. Write $\chi_3^{\mathrm{cyc}}$.
* C3 ("the Kummer dual $M^*(1)$") agrees with B-C4(c); the dual Selmer structure $\mathcal L^*$ (8.2) is a listed exception. No change.

**ch18_blochkato.md** (`ch:blochkato`)
* M5 (cosmetic). 14.7, line 676: "$4\pi^2c^2\langle f,f\rangle$". Write $c_E^2$.
* C2, C3, C4, C6 are the sources of B-C4(c), B-C2, B-C5(c), B-C14. No other change.

**ch19_lfunctions.md** (`ch:lfunctions`)
* M2 (cosmetic). 8.4, lines 349 to 351, and Section 5, line 724: "$c_E=\pm1$". Write $c_E=1$ (B-C9).
* C2 to C9 are the sources of B-C2, B-C3, B-C7, B-C8, B-C11(c). No other change.

**ch21_paper.md** (`ch:paper`)
* F1 (required). Opening paragraph, lines 17 to 18: "In every L-FACTOR, `L_p(M, s) = det(1 - Frob_p p^{-s} | M^{I_p})^{-1}` with
  `Frob_p` the GEOMETRIC Frobenius `= Frob_arith^{-1}`". The book's $\Frob_p$ is always arithmetic. Write `Phi_p` there.
* F2 (required). C2(b), lines 62 to 66: "`Frob_p^{geom}`", "for `M = V_l E` and `p` good this is `(1 - a_p p^{-s} + p^{1-2s})^{-1}`",
  "`det(1 - Frob^{geom} X | V) = (1 - alpha X)(1 - beta X)`", "on `V_l E` the geometric Frobenius has eigenvalues `alpha, beta`;
  the arithmetic one has `p/alpha = beta` ... the same set". All wrong (important_notes.md B1, B7, B9). Replace by B-C3: on $V_\ell E$
  the arithmetic Frobenius has $\alpha,\beta$, the geometric $\alpha^{-1},\beta^{-1}$ (not the same set); $(1-a_pp^{-s}+p^{1-2s})^{-1}=L_p(V_\ell E^\vee,s)=L_p(E,s)$,
  while $L_p(V_\ell E,s)=L_p(E,s+1)$; write $\Phi_p$ for the geometric Frobenius.
* T1 (required). A2.5, line 385, and A2.7, lines 450 and 466: the Tate matrices with corner `kappa`. Write `eps kappa` (B-C14;
  point 42, B7), and in step (6) `c' = eps(Frob) kappa(Frob)`.
* T2 (cosmetic). A2.7, line 477 (and the other book-text uses of a bare `c`, `v_l(c)`): write `c(u)`; keep `c` inside quotations
  of the paper (point 23, B-C14).
* D5 (required). A3.2, lines 518 to 519: "`T_n^* = w_N T_n w_N`", "`U_p^* = w_N U_p w_N`" for adjoints. Write `T_n^dagger`, `U_p^dagger`;
  and replace the self-correcting sentence (B12) by the clean statement of ch:hecke 5.2, 5.3.
* D6 (required). A4.1 commentary, lines 678 and 680, and Section 9 N12, line 1894: "`V_l E^*`", "`ad(T^*)`" for **linear** duals. Write
  `V_l E^vee`, `ad(T^vee)`.
* X5 (cosmetic). A2.2 (or its proof), line 309: "`chi_3(sigma) = 1`" with the cyclotomic character. Write `chi_3^{cyc}`.
* L6 (cosmetic). A4.9 (lines 795 to 803) uses `iota` for `H^1(Q_p, T^D) -> H^1(Q_p, V^D)` and A4.14 (lines 954 to 965) for the
  twist map. Write `iota_S` for the twist map in this chapter (B-C15(c)).
* The writer note W4 (line 1713) already asks for the adjectives; with F1, F2 the symbols carry them.

**ch01_groups.md, ch06_ant.md, ch16_cohomology.md**: no disagreement. (ch:ant writes the geometric Frobenius as $\Frob_p^{-1}$,
which B-C2(b) allows; ch:groups's $\varepsilon$ and $\sigma$ are local and already renamed by Chapters 4 and 11.)

### 3.2 PLAN.md (not an outline; for the orchestrator)

* P1. Chapter 7 entry: "$\Frob N\Frob^{-1}=p^{-1}N$". Write "$\Phi N\Phi^{-1}=p^{-1}N$, equivalently $\Frob N\Frob^{-1}=pN$" (B6, B-C2(f)).
* P2. Chapter 18 and Chapter 19 entries: "$L_p(V,s)=\det(1-\Frob_pp^{-s}\mid V^{I_p})^{-1}$ (... the Frobenius here is geometric or
  arithmetic: fix the convention ...)". Write $\Phi_p$ (B-C2(d)).
* P3. Chapter 4 entry "$\Hom_G(V,W)=(V^*\otimes W)^G$", Chapter 14 entry "$J_0(N)(\C)=S_2(\Gamma_0(N))^*/H_1(X_0(N),\Z)$", Chapter 18
  entry "duals $V^*=\Hom(V,\Q_\ell)$ and ... $V^D=V^*(1)$": write $^\vee$ (B-C4(a)). Also D7.
* P4. Chapter 10 and Chapter 22 entries: "$n+4$ for $\mathrm I_n$, $-(n+4)$ for $\mathrm I_n^*$": add "for $n\ge1$; $\mathrm I_0^*$ is $-1$" (B-C11(c)).
* P5. Chapter 14 entry: "the abelian variety $A_f$ attached to a newform" (write $J_f$) and "the Eichler-Shimura relation
  $T_p=\Frob_p+\Frob_p^*$" (write $(T_p)_*=\pi_p+\hat\pi_p$, B-C2(g)).
* P6. Chapter 18 entry: "$\Tam_p(T)=\Fitt_{\Z_\ell}(H^1(I_p,T)_{\mathrm{tors}})^{G_{\Q_p}}$": the invariants go inside (point 37, B22).
* P7. Appendix B entry: its list names "$c$"; the book has $c_q$ (Tamagawa number), $c(u)$ (class of the unit part), $c'$ and
  $c_E$ (Manin constant), never a bare $c$.

### 3.3 Counts

| outline | required | cosmetic | entries |
|-|-|-|-|
| ch01_groups | 0 | 0 | none |
| ch02_rings | 0 | 3 | F9, D8, L2 |
| ch03_modules | 2 | 1 | D1, D2, D3 |
| ch04_reps | 1 | 1 | F3 (both halves) |
| ch05_galois | 2 | 0 | X1, X2 |
| ch06_ant | 0 | 0 | none |
| ch07_local | 0 | 1 | X3 |
| ch08_curves | 1 | 2 | A3, F6, D9 |
| ch09_ellcurves | 0 | 3 | F4, F5, M4 |
| ch10_reduction | 0 | 2 | L1, L5 |
| ch11_galrep | 2 | 2 | K1, F8, X5, L5 |
| ch12_modforms | 0 | 2 | L3, M3 |
| ch13_hecke | 1 | 1 | H3, H1 |
| ch14_moddeg | 2 | 3 | A1, F7, M1, L4, H5 |
| ch15_modgalrep | 4 | 1 | A2, D4, H2, H4, K2 |
| ch16_cohomology | 0 | 0 | none |
| ch17_galcoh | 0 | 1 | X4 |
| ch18_blochkato | 0 | 1 | M5 |
| ch19_lfunctions | 0 | 1 | M2 |
| ch21_paper | 5 | 3 | F1, F2, T1, D5, D6, T2, X5, L6 |
| total | 20 | 28 | 48 entries (plus 7 in PLAN.md) |

By theme: Frobenius 10 entries (F1 to F9, with F3 in two halves), duals and adjoints 9 (D1 to D9), characters 6 (X1 to X5,
X5 in two outlines), Manin constant 5 (M1 to M5), component groups 2 (K1, K2), the abelian variety $A_f$ 3 (A1 to A3), Hecke
notation 5 (H1 to H5), Tate data 2 (T1, T2), other letters 7 (L1 to L6, L5 in two outlines). Per searched pattern: `Frob` 6
(F1, F2, F4, F5, F8, F9 and P1, P2), `\Phi` 4 (F3, F8, K1, K2), `^*` 7 (D1 to D6, D8), `^\vee` 1 (D6), `dagger` 2 (D4, D5,
both "write dagger"), `chi_` 5 (X1 to X5), `c^2` 0 (M3 to M5 concern the letter, not the formula), `Petersson` 0.

________________________________________________________________________________

## Part 4. Section plan for `chapters/chB_notation.tex` and notes for the writer

### 4.1 Section plan (target 750 lines of LaTeX; PLAN.md allows 400 to 800)

The appendix has no card of core results (it states no theorems), no exercises, and no "Where the paper uses this
chapter" section in the usual form; instead its first section says how to use it. It does have a short "Notes and
references" section. Labels: `\label{ch:notation}` on the chapter, `sec:notation:...`, `conv:notation:...`,
`tab:notation:...`.

| section | content | source here | lines |
|-|-|-|-|
| B.1 How to use this appendix | one paragraph: the conventions bind every chapter; the index gives the chapter where each symbol is defined (`\Cref{ch:slug}` only, no theorem numbers, PLAN.md 7.1); the paper's notation is the book's; where the paper is ambiguous the book's reading is given | opening of this file | 20 |
| B.2 Letters, primes, valuations, lengths | `convention` boxes B-C1, B-C10; a five-line table of the meanings of $q$ | B-C1, B-C10 | 35 |
| B.3 Frobenius | B-C2 and B-C3 as two `convention` boxes; one `warning` box "Where the paper uses which Frobenius" (Section 1.1, table, lem:euler, lem:fpr, after lem:dfg21: geometric; lem:tamfactor: arithmetic); the dictionary table (arithmetic eigenvalue $\lambda$ = geometric $\lambda^{-1}$; $V_\ell E$, $V_\ell E^\vee$, $\ad V$, $\Z_\ell(1)$, the Steinberg line) | B-C2, B-C3 | 80 |
| B.4 Duals, adjoints, pullbacks, twists | B-C4 and B-C5 as `convention` boxes; a table "symbol / meaning / example in the paper" for $^\vee$, $^*$, $^D$, $^\dagger$, $\varphi^*$, $(n)$; the list of fixed exceptions to the star rule | B-C4, B-C5 | 60 |
| B.5 Characters | B-C6 as a box, with the table of the paper's characters ($\chi_{-3}$, $\chi_{-4}$, $\chi_{q^*}$ (the paper's $\chi_q$), $\chi_{\ell^*}$, $\chi_\ell$, $\bar\chi_\ell$, $\omega_\ell$, $\chi_S$, $\varepsilon$, $\psi$: field cut out, conductor, value at $p$) | B-C6; ch:rings 10.5; ch:ant 5.8 | 40 |
| B.6 $L$-functions, Petersson product, Manin constant | B-C7 (with its table of normalisations), B-C8, B-C9; a `warning` on the Rankin series and on PARI's `mfpetersson` | B-C7 to B-C9 | 60 |
| B.7 Local data at a bad prime | B-C11 (Kodaira symbols, $\Phi_q$, $\Phig_q$, $c_q$, PARI codes as a ten-row table), B-C14 (Tate data and the Tate matrix with corner $\varepsilon\kappa$) | B-C11, B-C14 | 50 |
| B.8 Adjoint, Hecke algebras, twists, depletion | B-C12, B-C13; the dictionary of the two uses of $I$ (lem:crit, lem:ddt417) as a three-line table | B-C12, B-C13 | 45 |
| B.9 Index of symbols | Part 2 as `longtable`s (four columns: symbol, meaning, chapter, see also), grouped as 2.1 to 2.13, every row kept; the "conflicts" column shortened to "see also" pointers to B.2 to B.8 and B.10; item numbers of the outlines dropped | Part 2 | 300 |
| B.10 Letters with several meanings | B-C15 as one table (letter, meanings, where, rule) | B-C15 | 35 |
| B.11 Notes and references | which sources use which conventions (Deligne73 and Tate79 for $\lVert\cdot\rVert$; DFG04 1.7.2; Bloch-Kato and FPR94 write $V^*(1)$ for $V^D$; Silverman's Weil pairing; Diamond-Shurman's slash; Shimura75, Gelbart-Jacquet; PARI manual); B-C16 | B-C16 and the references named in Part 1 | 25 |
| total | | | 750 |

The index dominates: 275 rows of Part 2 at one LaTeX line each, plus thirteen group headings and the `longtable`
preambles, give about 300 lines; the boxes are therefore kept to their statements, with the reasons reduced to one
sentence and a pointer to the chapter that proves the identity. If the total exceeds 800 lines, merge index rows that
differ only in decoration (as $\Gamma_0(N)$, $\Gamma_1(N)$, $\Gamma(N)$ already are) rather than dropping symbols.

### 4.2 Notes for the writer

1. **Wording of the boxes.** The boxed statements of Part 1 are final; the writer only converts them to LaTeX (macros of
   `preamble.tex`: `\Frob`, `\ad`, `\Sym`, `\nv`, `\Tam`, `\Fitt`, `\len`, `\Phig`, `\Ns`, `\degphi`, `\Zl`, `\Ql`, `\Qlmod`,
   `\Hom`, `\End`, `\Ann`, `\Hf`, `\Hur`). There is no macro for the geometric Frobenius: write `\Phi_p`. Do not define new
   macros (PLAN.md 7.1).
2. **Cross-references.** Only `\Cref{ch:slug}`. The item numbers of Part 2 are for the orchestrator and the chapter writers;
   once the chapters exist, the cross-reference pass of PLAN.md Section 8, step 4, may replace them by precise labels.
3. **Chapters 20 and 22.** Their outlines are being written in parallel. When they land, check that they use $\pi$, $\wp$,
   $I=\Ann\wp$, $\eta^\Sigma_{f,\lambda}$, $\hat\delta_!$, $M_{f,\lambda}$, $J_f$ (not $A_f$), `rule(E, l, iii)`, the Kodaira codes with $n\ge1$,
   $c(u)$ and $\Phi_p$ as here, and add their item numbers to Part 2.
4. **Paper quotations.** Inside `paperlink` environments and verbatim quotations the paper's own symbols stand ($\chi_q$ for the book's $\chi_{q^*}$, decision D3; $c$,
   $c_q$ in sec:tam, $\chi_{11}$, $E_{\{p\}}$, "$\Frob_p$" in Section 1.1), followed by the book's reading in brackets.
5. **Do not "fix" the paper's numbers.** No number in the paper changes under any convention of Part 1 (points 11, B1, B10).
   The appendix says so once, in B.3.
6. **Typography.** No dash ligatures, ASCII source, tables with `booktabs` and `longtable` (check that `longtable` is loaded
   by `preamble.tex`; if not, split B.9 into several `tabular` environments, since chapters may not load packages).
7. **What not to put in the appendix.** Proofs (the boxes cite the chapters that prove the identities: $L_p(M(1),s)=L_p(M,s+1)$
   is ch:local 8.2, $\ad V\simeq\Sym V\otimes\det^{-1}$ is ch:reps 7.5, the Zagier-Watkins identity is ch:moddeg 7.3).

________________________________________________________________________________

## Part 5. What could not be settled here

1. **DFG04's own conventions.** B-C2(d) and B-C7 assume DFG04 1.7.2 uses the geometric Frobenius and $L(\ad M_f,s)$ with the
   value at $s=1$, as the Chapter 7, 19 and 21 outlines report; nobody has checked the text (Chapter 19 marks its table row
   "verify"). Likewise the Hodge-Tate sign of DFG04 and Bloch-Kato (B-C5(c)) and the checklist of important_notes.md point 56.
2. **The sign of the Manin constant.** B-C9 fixes $c_E>0$ by choosing the sign of $\omega_E$. This is a book decision, harmless
   (only $c_E^2$ enters), but the literature states Manin's conjecture as $c_E=\pm1$ or $c_E=1$ depending on whether $\omega_E$ is
   normalised; the Chapter 14 writer must phrase the cited results accordingly.
3. **Fundamental characters $\omega,\omega_2$ versus periods $\omega_1,\omega_2$.** Kept both (B-C15(b)) because they never meet in one
   chapter as the outlines stand; if Chapter 11 or 15 ends up mentioning periods, rename the fundamental characters
   $\theta_{\ell-1}$, $\theta_{\ell^2-1}$ (Serre's notation, which is Chapter 7's $\theta_m$).
4. **The paper's $\chi_q$.** Resolved by decision D3 (PLAN.md 7.5): the stricter rule is adopted, $\chi_{q^*}$ everywhere in the
   book's own text (as Chapters 2, 13, 18, 19 already did), and the outlines of Chapters 5, 6, 7, 9, 10, 11, 15, 17, 21 have been
   converted. The paper's $\chi_q$ survives only inside quotations of the paper (Part 4, item 4).
5. **Two uses of $I$ and of $\iota$ in the paper.** B-C13(c) and B-C15(c) keep the paper's letters locally rather than renaming
   them, because Chapter 21 must quote the paper verbatim. If the paper itself is revised, the cleanest fix is $J$ for
   $\Ann_\T(\wp)$ in lem:ddt417 and $\iota_S$ for the twist map.
6. **Line numbers.** Part 3 cites lines of the outlines as they stand on 14 October 2026; the Chapter 20 and 22 outlines and
   any revision of the others will shift them. The entry identifiers (F1, D1, ...) are stable.
7. **Reading.** The outlines were read through their convention sections, item lists, writer notes and every line matched by
   the searches listed at the head of Part 3; prose paragraphs that matched none of the patterns were not all read line by
   line, so a disagreement phrased without any of the searched symbols could have been missed.
