# Chapter 04: Representations of finite groups and the mod l world (`ch:reps`, `chapters/ch04_reps.tex`)

Stage 1 line-up. Part I (Algebra). Target length 2,120 lines of LaTeX (card excluded; see Part 3), inside the
1,000 to 2,200 range of PLAN.md Section 7.3.

Rigour tags: **P** = proved here, **S** = proof sketched here, **R** = stated; reference. Item format, as in the
Chapter 1, 2 and 5 outlines: number, label-ready name, kind, tag; the precise statement with all hypotheses; reference
(book and chapter or section; a theorem number only where sure); the paper's use by its `\label` names, or
"background". Every computation quoted below was checked by hand and by short Python/sympy scripts in `/tmp/ch04`
(verification log, Part 7).

## 0. What this chapter is for

The paper uses representation theory in eight places, and the chapter is built around them.

1. **Proposition prop:ns.** For the image $N_s(\F_3)$: the determinant-one subgroup $C_4$ acts on $\F_9^2$ as
   $\psi\oplus\psi^{-1}$ with $\psi$ of order $4$; Frobenius reciprocity gives $\bar\rho\otimes\F_9\simeq\Ind\psi$; an
   induced representation is invariant under the twist by the character of the index-two subgroup, so
   $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$; the other two images ($\GL_2(\F_3)$, $N_{ns}(\F_3)$) have absolutely irreducible
   determinant-one subgroups ($\SL_2(\F_3)$, $Q_8$). The chapter proves all of this as statements about the standard
   representations of the subgroups of $\GL_2(\F_3)$ (Section 8), using Chapter 1 for the group theory.
2. **Lemma lem:h0.** "Trace-zero $G_\Q$-maps $\bar\rho\to\bar\rho\otimes\bar\chi_\ell$" (that is,
   $H^0(\ad\bar\rho\otimes\bar\chi_\ell)$ as $\Hom_G(V,V\otimes\chi)$ with trace zero, and $\Hom_G(V,W)=(V^\vee\otimes W)^G$);
   Schur ("a nonzero such map is an isomorphism"); the determinant comparison; the trace-zero lemma
   ($\tr\phi=\chi(g)\tr\phi$); Clifford theory for an index-two subgroup ("$\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ iff
   induced iff not absolutely irreducible on the subgroup"); the length $h_\ell(E)$ as "the largest $k$ with
   $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$", which is a statement about lattices (Section 10).
3. **Lemma lem:IV, Remark rem:types, Lemma lem:euler.** Cyclic groups of order $2,3,4,6$ and (minus) unipotent
   elements acting on a rank-two space or lattice: eigenvalues, fixed spaces on $V$ and on $\ad V$, the commutant
   $k[\sigma]$ and its trace-zero line, reduction modulo $\ell$ (an element of order $3$ in characteristic $0$ becomes a nontrivial unipotent
   modulo $3$), the failure of Maschke's theorem behind "$E[3]^{I_q}$ is a line while
   $T^{I_q}=0$".
4. **Lemma lem:old.** Brauer-Nesbitt in characteristic $\ell$ (characteristic polynomials, not traces), the
   absolute irreducibility needed to pass from equal semisimplifications to an isomorphism over a common finite
   field (important_notes.md point 10), and "a non-split extension of two characters has a unique stable line".
5. **Section 4.2 and Lemma lem:fpr.** $A=\ad T$; the trace form and the self-duality of $\ad T$ for $\ell$ odd, so
   $T^D=\Hom(A,\Zl(1))\simeq A(1)$; homothetic lattices (and dual lattices, point 26) have the same adjoint; the
   homothety lemma ("all stable lattices homothetic when the reduction is irreducible").
6. **Lemma lem:tamfactor.** The basis $e=e_1\otimes e_2^\vee$, $h$, $f$ of $\ad T$ and the formulas for the
   adjoint action of a unipotent and of an upper triangular matrix.
7. **Section 1.1 and the Introduction.** $A_f=\ad V$, the eigenvalues $\alpha/\beta,1,\beta/\alpha$ of $\ad$ of a
   matrix with eigenvalues $\alpha,\beta$, and $\ad\rho\simeq\Sym\rho\otimes\det^{-1}$, which underlies
   $L_p(\Sym f,s)=L_p(A_f,s-1)$.
8. **The hypothesis of Theorem thm:main** ("absolutely irreducible on $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$"), $S_f$, and
   DDT Theorem 3.15: absolute irreducibility, the distinct-eigenvalue criterion (complex conjugation), restriction
   to an index-two subgroup, the dihedral case of Dickson's classification read as "induced".

Split with the neighbouring chapters (decided here; each decision is repeated in Part 5 and Part 6):
* **Chapter 1** proves the group theory of $\GL_2(\F_3)$: the models $J,\sigma,w,u,a$, the 55 subgroups, orbits on
  lines, the three images of its 6.7, unipotent and minus-unipotent elements as group elements (its 5.6), the
  commutator argument of its 5.7, $1+\ell M_2(\Zl)$ torsion-free (its 7.4), Dickson for $\GL_2(\F_\ell)$ (its 5.10).
  Chapter 4 cites these and adds only the representation-theoretic reading (Section 8 and 9). The alternative proof
  of absolute irreducibility for $Q_8$ by Maschke (item 3.7) is new here and complements Chapter 1's 5.7.
* **Chapter 2** supplies $\F_9=\F_3[i]$, finite fields, orthogonality for characters of finite abelian groups and
  Dirichlet characters, and $a^2\equiv1\pmod{\ell^k}$ for all units iff $\ell^k=3$ (its 5.5).
* **Chapter 3** (being outlined in parallel; PLAN.md split) supplies modules over rings, $\Hom$ and $\otimes$,
  Nakayama, DVRs and $\Zl$, finitely generated modules over a DVR (torsion-free implies free; cyclic iff the
  $\lambda$-torsion has length at most one), saturation, perfect pairings and Gram determinants, Pontryagin
  duality, generalised eigenspaces of a single operator. Chapter 4 uses these for $\mathcal{O}[G]$-lattices and does not
  redo them. **Jordan-Holder** is proved in Chapter 3 (for modules of finite length over any ring, where it is first
  needed for lengths over a local ring) and is cited here (item 3.4), which adds only the reading for $k[G]$- and
  $\mathcal{O}[G]$-modules (composition factors of representations): decision B2 of important_notes.md, PLAN.md 7.5.
* **Chapter 5** proves the profinite and Galois forms: continuity, existence of stable lattices for compact
  images (its galois:continuous-reps (c)), Chebotarev plus Brauer-Nesbitt (its galois:chebotarev-brauer-nesbitt,
  galois:congruent-ap), the cyclotomic determinant argument (its galois:twist (c)), complex conjugation (its
  galois:complex-conjugation (d)), restriction to $G_{\Q(\sqrt{\ell^*})}$ (its galois:index-two-restriction).
  **Decision:** Chapter 4 proves, for an arbitrary group, Brauer-Nesbitt (5.2), the distinct-eigenvalue criterion
  (2.4), Clifford theory for index two (6.6), the trace-zero lemma (7.2), independence of $\bar\rho^{ss}$ from the
  lattice and the homothety lemma (10.2, 10.3); Chapter 5 cites them and adds only continuity and the Galois
  input. In particular Chapter 5's galois:reduction-ss and galois:complex-conjugation (d) become one-line
  applications of 10.2, 10.3 and 2.4 (the Chapter 5 writer should cite, not reprove).
* **Chapter 6** proves the arithmetic of $\Z_\ell[\zeta_3]$ and $\Z_\ell[i]$ (its 4.7, 4.8, 4.9), the freeness of a lattice
  over $\Z_\ell[\sigma]$ and the Frobenius action $\chi_{-3}(q)$, $\chi_{-4}(q)$ on the invariant line (its 4.10 (iii) to
  (v)), and the twist detector by traces at inert primes (its 6.4). **Decision:** Chapter 4 proves the commutant
  lemma and the trace-zero line (9.2), which Chapter 6's 4.10 (i), (ii) cites ("Chapter 4 or linear algebra"), and
  states the $\Z_\ell[\zeta_3]$-module structure with a forward pointer to Chapter 6 (9.4 (v)); it gives an elementary
  proof of the mod $3$ unipotence of an order-$3$ element (9.4 (ii)) that does not need the DVR.
* **Chapter 11** proves the paper's Lemma lem:IV, Remark rem:types, Proposition prop:ns and Lemma lem:h0 as statements
  about elliptic curves; Chapter 4 supplies their representation-theoretic cores (8.5, 9.4, 10.6) and never
  mentions Kodaira types except in `paperlink` environments and in the shape table of 9.3, where the assignment
  type to shape is a black box from Chapters 10 and 11.
* **Chapter 18** uses the trace form and the self-duality of $\ad T$ (7.6) for $T^D=A(1)$ and adds the Tate twist
  and Pontryagin-dual statements; **Chapter 19** uses $\ad\simeq\Sym\otimes\det^{-1}$ (7.5) for the $L$-function
  normalisations.

## 1. Global conventions fixed in this chapter

* **C1 (representations).** $G$ is a group (finite unless said otherwise; many statements hold for any group and
  are marked "any $G$"), $k$ a field, $R$ a commutative ring. A representation is a homomorphism
  $\rho\colon G\to\GL(V)$ with $V$ a finite-dimensional $k$-vector space (or a free $R$-module of finite rank), i.e. a
  left $k[G]$-module of finite dimension. Matrices act on column vectors on the left (Chapter 1, C1). "$G$-map" =
  "intertwiner" = $k[G]$-linear map; $\Hom_G(V,W)$; $V\simeq W$ means isomorphic as representations.
* **C2 (duals).** The linear dual is $V^\vee=\Hom_k(V,k)$ with $(g\lambda)(v)=\lambda(g^{-1}v)$, i.e. the matrix
  $\rho(g^{-1})^{t}$ in the dual basis $e_i^\vee$. The symbol $^*$ is reserved for Pontryagin duals (Chapter 3, the
  paper's Lemma lem:dfg21) and is not used for linear duals; PLAN.md's "$V^*\otimes W$" is written $V^\vee\otimes W$.
* **C3 (adjoints).** $\End_k(V)=V\otimes V^\vee$ with $g\cdot x=\rho(g)x\rho(g)^{-1}$. The full adjoint is written
  $\End(V)$ (or $\Ad V$, macro `\Ad`); the trace-zero adjoint is the paper's $\ad V$ (macro `\ad`, which already
  contains the superscript $0$: never write `\ad`). $\Sym V$ (macro `\Sym`, which already contains the exponent
  $2$) is the symmetric square. Matrix units $E_{ij}=e_i\otimes e_j^\vee$; for $\dim V=2$ the basis of $\ad V$ is the
  paper's $e=E_{12}=e_1\otimes e_2^\vee$, $h=E_{11}-E_{22}$, $f=E_{21}=e_2\otimes e_1^\vee$ (as in Chapter 16).
* **C4 (characters and twists).** A *character* of $G$ with values in $R$ is a homomorphism $\chi\colon G\to R^\times$;
  $R(\chi)$ is $R$ with $G$ acting through $\chi$, and $M(\chi)=M\otimes_RR(\chi)$, $\rho\otimes\chi$. In Section 4 only,
  "the character of $V$" is the trace function, written $\tr_V$ (never $\chi_V$, to avoid a clash with the paper's
  $\chi_{-3}$, $\chi_\ell$). Galois Tate twists $M(1)=M(\chi_\ell)$ are Chapter 5's and 18's notation.
* **C5 (fields).** $\bar k$ is an algebraic closure; $V_K=K\otimes_kV$. $\F_9=\F_3[i]$ with $i^2=-1$ (Chapter 2).
  "Absolutely irreducible" means $V_{\bar k}$ irreducible (2.3).
* **C6 (standard models).** $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $\sigma=\operatorname{diag}(1,-1)$,
  $w=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $u=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $a=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ and the
  subgroups $C_s,N_s,C_{ns},N_{ns},Q_8,C_4=\langle J\rangle,\mathrm B,\mathrm U$ of $\GL_2(\F_3)$ are those of Chapter 1, 6.2. The
  paper's generator $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ is $J^{-1}$. $\psi\colon C_4\to\F_9^\times$ is $\psi(J)=i$.
  **Clash:** the matrix $\sigma=\operatorname{diag}(1,-1)$ of Chapter 1 and the generator $\sigma$ of inertia of order
  $3$ in the paper (Lemmas lem:IV, lem:euler). In Sections 8 the matrix keeps Chapter 1's name; in Section 9 the
  order-$3$ element is written $\sigma$ as in the paper, and the matrix $\operatorname{diag}(1,-1)$ is written $h$ (it is
  the basis vector $h$ of $\ad V$ viewed as a matrix). Say this in a `convention` environment.
* **C7 (lattices).** $\mathcal{O}$ is a discrete valuation ring with uniformiser $\lambda$, fraction field $K$, residue field
  $k=\mathcal{O}/\lambda$; in the paper $\mathcal{O}=\Zl$ (or the ring of integers of a finite extension of $\Ql$), $\lambda=\ell$. A
  lattice in a $K$-vector space $V$ of dimension $n$ is a finitely generated $\mathcal{O}$-submodule spanning $V$ (free of rank
  $n$, Chapter 3). Two lattices $L,L'$ are homothetic if $L'=cL$ for some $c\in K^\times$ (equivalently $L'=\lambda^mL$,
  $m\in\Z$).
* **C8 (no Frobenius here).** The chapter never uses Frobenius elements. Where the paper's Frobenius appears (9.1
  (iv), 9.3) it is an abstract $F\in\GL(V)$ with $FgF^{-1}=g^q$ (the arithmetic convention of Chapter 5, C2,
  and Chapter 7); the geometric Frobenius $F^{-1}$ gives the inverse eigenvalues (important_notes.md point 11).
* **C9 (typography).** PLAN.md Section 7.2: no dash ligatures, ASCII source, labels `...:reps:...`; "Jordan-Holder",
  "Brauer-Nesbitt", "Frobenius reciprocity" with plain hyphens; tables with `booktabs`.

________________________________________________________________________________

## 2. Line-up of the core results, in teaching order

### Section 1. Representations over a field

**1.1 `def:reps:representation`** (definition and examples; P). Let $G$ be a group and $k$ a field. A representation
of $G$ over $k$ is a homomorphism $\rho\colon G\to\GL(V)$, $V$ a finite-dimensional $k$-vector space; equivalently a
$k[G]$-module structure on $V$. After a choice of basis, $\rho\colon G\to\GL_n(k)$; two matrix representations are
isomorphic iff they are conjugate by one $P\in\GL_n(k)$. Degree $n=\dim V$, kernel, faithful. Examples: the trivial
representation $\mathbf 1$; one-dimensional representations = characters $\chi\colon G\to k^\times$ (they factor through
$G^{\mathrm{ab}}$); the permutation representation $k[X]$ of a $G$-set $X$, the regular representation $k[G]$; the
standard representation of a subgroup $H\le\GL_2(k)$ on $k^2$; inflation along a homomorphism $G\to G'$ (so a
representation of a finite quotient of a profinite group is one of the group, Chapter 5). RHB link (one sentence):
RHB's representations are the case $k=\C$, $G$ finite. Reference: Serre, Linear representations, Chapter 1;
Dummit-Foote Section 18.1. Paper: background ($V$, $T$, $\rho$, $\bar\rho$ of Section 1.1 are representations of $G_\Q$).

**1.2 `def:reps:constructions`** (definition and proposition; P). Subrepresentation (a $G$-stable subspace),
quotient, direct sum, tensor product ($g(v\otimes w)=gv\otimes gw$), dual $V^\vee$ (C2), $\Hom_k(V,W)$ with
$(g\phi)(v)=g\,\phi(g^{-1}v)$, invariants $V^G$, determinant $\det\rho=\wedge^n\rho$. Facts: $\tr(g\mid V^\vee)=
\tr(g^{-1}\mid V)$; $\tr(g\mid V\otimes W)=\tr(g\mid V)\tr(g\mid W)$; $\det(V\otimes\chi)=\chi^n\det V$; $V^{\vee\vee}\simeq V$;
$(V\otimes W)^\vee\simeq V^\vee\otimes W^\vee$. For $\dim V=2$: the alternating form $\omega(x,y)=\det[x\,|\,y]$ satisfies
$\omega(gx,gy)=\det(g)\omega(x,y)$, so $v\mapsto\omega(v,-)$ is an isomorphism $V\otimes\det^{-1}\simeq V^\vee$, i.e.
$V^\vee\simeq V\otimes\det^{-1}$. Reference: Serre, Linear representations, Sections 1.4 to 1.6. Paper: Section 4.2
(dual lattices, important_notes.md point 26; via 7.7), lem:tamfactor ($e_2^\vee$).

**1.3 `prop:reps:homG`** (proposition; P). For finite-dimensional $V,W$ (or free $R$-modules of finite rank) the map
$V^\vee\otimes W\to\Hom(V,W)$, $\lambda\otimes w\mapsto(v\mapsto\lambda(v)w)$, is a $G$-isomorphism, and
$\Hom_G(V,W)=\Hom(V,W)^G=(V^\vee\otimes W)^G$. In particular $\End(V)^G=\End_G(V)$ and, for a character $\chi$,
$(\End(V)\otimes\chi)^G=\Hom_G(V,V\otimes\chi)$. Reference: Serre, Section 2.2 (in characteristic $0$; the proof is
characteristic-free). Paper: Lemma lem:h0 ("the $\ell$-torsion of $H^0(\Q,W^D)$ is $H^0(\Q,\ad\bar\rho\otimes\bar\chi_\ell)$,
the space of trace-zero $G_\Q$-maps"), Proposition prop:ns ($H^0(\Q,\ad\bar\rho(1))\ne0$), Lemma lem:tamfactor (the
basis $e_1\otimes e_2^\vee$).

**1.4 `prop:reps:scalars`** (proposition; P for (i) to (iii), R for (iv)). Let $K/k$ be a field extension. (i)
$\Hom_{K[G]}(V_K,W_K)=K\otimes_k\Hom_{k[G]}(V,W)$; in particular $\dim_K\Hom_{K[G]}(V_K,W_K)=\dim_k\Hom_{k[G]}(V,W)$ and
$(V_K)^G=K\otimes_kV^G$ (the $G$-maps are the solutions of a homogeneous linear system with coefficients in $k$).
(ii) If $V,W$ are irreducible over $k$ and $V_K\simeq W_K$, then $V\simeq W$ (a nonzero $K$-map gives a nonzero $k$-map,
which is an isomorphism by Schur 2.2(i)). (iii) If $V$ is absolutely irreducible (2.3) and $W$ is any representation
with $W_K\simeq V_K$, then $W\simeq V$ (same argument: $W_K$ is irreducible, so is $W$). (iv) (Noether-Deuring) For
arbitrary finite-dimensional $V,W$, $V_K\simeq W_K$ implies $V\simeq W$. Reference: Curtis-Reiner, Section 29 (add
`CurtisReiner` to `bib/ch04.bib`). Paper: Proposition prop:ns (the isomorphism $\bar\rho\otimes\F_9\simeq\Ind\psi$ lives over
$\F_9$; $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ descends to $\F_3$ by (ii); see Part 8, point N1), Lemma lem:old ("over a
common finite field", important_notes.md point 10).

### Section 2. Irreducibility, Schur's lemma, absolute irreducibility

**2.1 `def:reps:irreducible`** (definition and examples; P). $V\ne0$ is irreducible (simple) if its only
subrepresentations are $0$ and $V$; indecomposable if it is not a direct sum of two nonzero subrepresentations;
reducible otherwise. Irreducible implies indecomposable, not conversely (3.3). For $\dim V=2$: $V$ is irreducible iff
no line of $k^2$ is $G$-stable iff $\rho(G)$ lies in no Borel subgroup of $\GL_2(k)$ (Chapter 1, 5.5). Examples:
every one-dimensional representation; the standard representation of $\GL_2(\F_q)$, of $N_s(\F_3)$, of $C_4=\langle J\rangle$
on $\F_3^2$ (irreducible: $X^2+1$ has no root in $\F_3$); $\mathrm U=\langle u\rangle$ and $\mathrm B$ on $\F_3^2$ are reducible.
Reference: Serre, Section 1.4. Paper: Proposition prop:ns ("acting irreducibly on $\F_3^2$"), Theorem thm:qual and
Lemma lem:old (hypothesis "$\bar\rho$ irreducible").

**2.2 `thm:reps:schur`** (theorem, Schur's lemma in both forms; P). Let $V,W$ be irreducible representations of any
group $G$ over any field $k$. (i) Every $G$-map $V\to W$ is $0$ or an isomorphism; $D=\End_G(V)$ is a division algebra
of finite dimension over $k$. (ii) If $k$ is algebraically closed, $\End_G(V)=k$, and $\dim\Hom_G(V,W)=1$ if $V\simeq W$,
$0$ otherwise. (iii) The conclusions of (ii) hold over any $k$ when $V$ and $W$ are absolutely irreducible (by 1.4(i)).
(iv) Consequences: if $V$ is absolutely irreducible, the centre $Z(G)$ acts through scalars (a central character);
every absolutely irreducible representation of an abelian group is one-dimensional; for an irreducible $V$ of an
abelian group, $\End_G(V)$ is a field. Reference: Serre, Section 2.2 (Proposition 4, characteristic $0$); Lang,
Chapter XVII, Section 1. Paper: Lemma lem:h0 ("a nonzero such map is an isomorphism, $\bar\rho$ being irreducible"; and
the one-dimensionality of $\Hom_G(\bar\rho,\bar\rho\otimes\bar\chi_\ell)$ behind "$H^0$ is cyclic"), Proposition prop:ns
("the third is abelian, hence absolutely reducible"), Lemma lem:old.

**2.3 `def:reps:absirr`** (definition and proposition; P for (i) to (iii), S for (iv)). $V$ is absolutely irreducible
if $V_{\bar k}$ is irreducible. (i) $V$ is absolutely irreducible iff the map $k[G]\to\End_k(V)$ is surjective (the
image of $\bar k[G]$ is $\bar k\otimes_k$ (image of $k[G]$), and over $\bar k$ irreducibility is equivalent to surjectivity
by Burnside's theorem 5.1(b); the writer may move 5.1 into this section); hence $V_K$ is irreducible for every
extension $K/k$. (ii) Absolutely irreducible implies irreducible and $\End_G(V)=k$. (iii) In dimension $2$: $V$ is
absolutely irreducible iff $\rho(G)$ fixes no line of $\bar k^2$, iff $\rho(G)$ is not conjugate in $\GL_2(\bar k)$ into the
upper triangular group. (iv) If $k$ is finite or of characteristic $0$ (perfect), an irreducible $V$ is absolutely
irreducible iff $\End_G(V)=k$. (Sketch: over a perfect field $V_{\bar k}$ is semisimple (stated, Curtis-Reiner Section
29); a semisimple module with endomorphism ring $\bar k$ is irreducible; and $\End_G(V_{\bar k})=\bar k\otimes\End_G(V)$ by
1.4(i).) Reference: Curtis-Reiner, Section 29; Serre, Section 12.1; Lang, Chapter XVII, Section 3. Paper: the
hypothesis of Theorem thm:main, Theorem thm:qual, DDT Theorem 3.15 and $S_f$ ("absolutely irreducible when restricted
to $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$"), Proposition prop:ns, Lemma lem:h0.

**2.4 `prop:reps:distinct-eigenvalues`** (proposition, the distinct-eigenvalue criterion; P). Let $G$ be any group,
$V$ a representation over $k$ of dimension $n$, and suppose some $g\in G$ (or some element of the image of $k[G]$)
acts on $V$ with $n$ distinct eigenvalues in $k$. Then every $G$-stable subspace of $V_{\bar k}$ is a sum of eigenlines
of $g$, all of which are defined over $k$; hence it is $U_{\bar k}$ for a $G$-stable subspace $U\subset V$. In particular
$V$ is irreducible iff it is absolutely irreducible. Special case ($n=2$, $\operatorname{char}k\ne2$): if some $c\in G$
has $\rho(c)^2=1$ and $\det\rho(c)=-1$ (eigenvalues $1\ne-1$), irreducible and absolutely irreducible coincide. Proof:
a subspace stable under a diagonalisable operator with distinct eigenvalues is the sum of the eigenlines it meets
(Vandermonde). Reference: elementary. Paper: Lemmas lem:h0 and lem:old ("irreducible" there must mean absolutely
irreducible; for $\bar\rho_{E,\ell}$, $\ell$ odd, complex conjugation supplies $c$: important_notes.md point 10),
Proposition prop:ns ("contain an element of determinant $-1$ and trace $0$"); applied to $G_\Q$ in Chapter 5
(galois:complex-conjugation (d)) and Chapter 11, which cite this item.

**2.5 `ex:reps:c4`** (worked example; P). $C_4=\langle J\rangle$ acting on $\F_3^2$: irreducible (2.1), not absolutely
irreducible. $\End_{C_4}(\F_3^2)=\F_3[J]\simeq\F_3[X]/(X^2+1)\simeq\F_9$, a field of dimension $2$ (consistent with 2.3(iv)
and 2.2(iv)). Over $\F_9=\F_3[i]$: $J(1,-i)^t=i(1,-i)^t$ and $J(1,i)^t=-i(1,i)^t$, so $\F_9^2=\psi\oplus\psi^{-1}$ with
$\psi(J)=i$, a character of order $4$; $\psi^{-1}=\psi^3$ is the Frobenius conjugate of $\psi$ (the two summands are
exchanged by $x\mapsto x^3$ on coordinates). Contrast: $\mathrm U=\langle u\rangle$ on $\F_3^2$ fixes exactly one line and is
not a direct sum (3.3); $C_{ns}(\F_3)\simeq\F_9^\times$ is irreducible, not absolutely irreducible, with $\End=\F_9$.
Reference: computation (Part 7). Paper: Proposition prop:ns ("$\bar\rho|_{\Gal(\Qbar/\Q(\sqrt{-3}))}\otimes\F_9=\psi\oplus\psi^{-1}$
for a character $\psi$ of order $4$").

### Section 3. Semisimplicity, Maschke, Jordan-Holder

**3.1 `prop:reps:semisimple`** (definition and proposition; P). For a $k[G]$-module $V$ of finite dimension (any $G$)
the following are equivalent: (a) $V$ is a sum of irreducible subrepresentations; (b) $V$ is a direct sum of
irreducible subrepresentations; (c) every subrepresentation has a $G$-stable complement. Such $V$ is *semisimple*;
subrepresentations and quotients of semisimple representations are semisimple. Isotypic decomposition
$V=\bigoplus_SV_S$ over the isomorphism classes $S$ of irreducibles, $V_S\simeq S^{m_S}$, $m_S$ the multiplicity; if
$S$ is absolutely irreducible, $m_S=\dim\Hom_G(S,V)$. Reference: Lang, Chapter XVII, Section 2; Serre, Section 2.6.
Paper: background (Brauer-Nesbitt, semisimplifications).

**3.2 `thm:reps:maschke`** (theorem, Maschke; P). (i) Let $G$ be finite and $\operatorname{char}k\nmid\#G$. Then every
finite-dimensional representation of $G$ over $k$ is semisimple. Proof: if $\pi$ is a $k$-linear projection onto a
stable $U$, then $\pi'=\frac1{\#G}\sum_g g\pi g^{-1}$ is a $G$-equivariant projection onto $U$. (ii) (Integral form.) Let
$R$ be a commutative ring with $\#G\in R^\times$ and $M$ an $R[G]$-module. Then $e_G=\frac1{\#G}\sum_gg$ is an idempotent
projector onto $M^G$, $M=M^G\oplus(1-e_G)M$ as $R[G]$-modules, and for every ideal $I$, $(M/IM)^G=M^G/IM^G$. In particular
for $R=\Zl$, $\ell\nmid\#G$ and $T$ a $\Zl[G]$-lattice: $(T/\ell T)^G=T^G/\ell T^G$, so invariants commute with reduction.
Reference: Serre, Section 1.3 (Theorem 1). Paper: Lemma lem:euler and Remark rem:types (for $\ell\ge5$ the finite
inertia images of order $2,3,4,6$ have order prime to $\ell$, so their invariants on $T$ and on $\ad T$ reduce well; at
$\ell=3$ this fails, 9.4), Proposition prop:ns ($Q_8$ and $C_4$ have order prime to $3$).

**3.3 `ex:reps:maschke-fails`** (worked examples; P). (a) $\mathrm U=\langle u\rangle\simeq C_3$ on $\F_3^2$: the line $\F_3e_1$ is
stable and has no stable complement ($u$ fixes exactly one line, Chapter 1, 5.6); $\F_3^2$ is indecomposable, not
semisimple, with composition factors $\mathbf1,\mathbf1$. (b) The regular representation $\F_p[C_p]\simeq\F_p[x]/(x-1)^p$ is
uniserial with the single composition factor $\mathbf1$ of multiplicity $p$. (c) For an infinite group Maschke fails even
in characteristic $0$: $\Z$ acting on $\Ql^2$ through $\begin{pmatrix}1&n'\\0&1\end{pmatrix}$, $n'\ne0$, is not semisimple (the shape of
tame inertia at a multiplicative prime). (d) $\mathrm B(\F_3)$ on $\F_3^2$ is indecomposable with $\End_{\mathrm B}=\F_3$:
"$\End_G(V)=k$" does not imply irreducibility without semisimplicity. Paper: Lemma lem:IV (the image of $I_q$ mod $3$ is
example (a)), Lemma lem:tamfactor and Lemma lem:euler type $\mathrm I_n$ (example (c)), Conjecture conj:eis (Borel
images).

**3.4 `thm:reps:jordan-holder`** (theorem, Jordan-Holder; R: proved in Chapter 3, cited with `\Cref{ch:modules}`, decision B2). Let $A$ be any ring (here $k[G]$ or $\mathcal{O}[G]$) and $M$ an
$A$-module of finite length (for instance a finite-dimensional representation, or a finite $\mathcal{O}[G]$-module). Then $M$
has a composition series $0=M_0\subset M_1\subset\dots\subset M_r=M$ with simple quotients, and the multiset of
isomorphism classes of the quotients $M_i/M_{i-1}$ (the composition factors, with multiplicity) and the length $r$
are independent of the series. Not proved here: Chapter 3 proves it (by induction on the minimal length of a composition
series, comparing two series through $M_{r-1}\cap M'_{s-1}$); this item only restates it for $k[G]$- and $\mathcal{O}[G]$-modules. Reference: Lang, Chapter III (composition series); Dummit-Foote Section 3.4 (for
groups; the module case is identical). Paper: background (semisimplification in Lemma lem:old; lengths of finite
$\Zl$-modules in Theorem thm:main, through Chapter 3).

**3.5 `def:reps:semisimplification`** (definition and proposition; P for (i), (ii); R for (iii)). (i) The
semisimplification $V^{ss}=\bigoplus_iM_i/M_{i-1}$ of a finite-dimensional representation is well defined up to
isomorphism (3.4); $V^{ss}\simeq V$ iff $V$ is semisimple; $(\cdot)^{ss}$ is additive in short exact sequences. (ii)
$\det(X-g\mid V)=\det(X-g\mid V^{ss})$ and $\tr(g\mid V)=\tr(g\mid V^{ss})$ for all $g$ (block triangular form). (iii)
If $k$ is perfect, $(V^{ss})_K\simeq(V_K)^{ss}$ for every algebraic extension $K/k$ (irreducible representations stay
semisimple under extension of scalars; Curtis-Reiner, Section 29). Paper: Lemma lem:old ("$\bar\rho_h\simeq\bar\rho$" via
semisimplifications), Chapter 5 galois:reduction-ss (cites 10.2).

**3.6 `prop:reps:nonsplit-line`** (proposition; P). Let $V$ be $2$-dimensional with a stable line $L$, $G$ acting on
$L$ by $\chi_1$ and on $V/L$ by $\chi_2$; in a basis $e_1\in L$, $e_2$: $\rho=\begin{pmatrix}\chi_1&b\\0&\chi_2\end{pmatrix}$ with
$b(gh)=\chi_1(g)b(h)+b(g)\chi_2(h)$. (i) $V$ is semisimple iff $V\simeq\chi_1\oplus\chi_2$ iff $V$ has a second stable line
iff there is $c\in k$ with $b(g)=c(\chi_1(g)-\chi_2(g))$ for all $g$ (a coboundary; Chapter 16 for the cohomological
reading). (ii) If $V$ is not semisimple (a non-split extension), $L$ is its unique stable line; hence for two
non-split extensions $V$, $V'$ (with sub-characters $\chi_1,\chi_1'$ and quotient characters $\chi_2,\chi'_2$), every
isomorphism $V\simeq V'$ maps $L$ onto $L'$, so $\chi_1=\chi'_1$ and $\chi_2=\chi'_2$. (iii) If $\chi_1\ne\chi_2$ and $V$ is
semisimple, $V$ has exactly two stable lines. Reference: elementary. Paper: Lemma lem:old (case $p\,\|\,N$, $\bar\rho$
ramified: "a non-split extension of two characters has a unique stable line, so the isomorphism ... matches the
sublines and hence the quotients"), Lemma lem:tamagawa-exp and Lemma lem:tamfactor (the matrix shape
$\begin{psmallmatrix}\chi_\ell\varepsilon&\kappa\\0&\varepsilon\end{psmallmatrix}$).

**3.7 `prop:reps:dim2-absirr`** (proposition; P). Let $\rho\colon G\to\GL_2(k)$. (i) If $\rho(G)$ is abelian, $\rho$ is
absolutely reducible (commuting operators on $\bar k^2$ have a common eigenvector). (ii) If $\rho(G)$ is finite of order
prime to $\operatorname{char}k$ and $\rho$ is absolutely reducible, then $\rho_{\bar k}\simeq\chi_1\oplus\chi_2$ (Maschke) and
$\rho(G)$ is abelian. Hence: a finite non-abelian subgroup of $\GL_2(k)$ of order prime to $\operatorname{char}k$ acts
absolutely irreducibly on $k^2$. (iii) If $H\le G$ and $\rho|_H$ is absolutely irreducible, so is $\rho$. (iv) Applied to
$\GL_2(\F_3)$: $Q_8$ (non-abelian, order $8$ prime to $3$) acts absolutely irreducibly on $\F_3^2$; so do $\SL_2(\F_3)$,
$N_{ns}(\F_3)$, $\GL_2(\F_3)$ (they contain $Q_8$) and $N_s(\F_3)\simeq D_4$ (non-abelian of order $8$); $C_4$ and
$C_{ns}(\F_3)$ (abelian) do not. The Borel subgroup $\mathrm B(\F_3)$ is non-abelian and faithful but reducible: its order
$12$ is divisible by $3$, so (ii) does not apply. Reference: elementary. Paper: Proposition prop:ns ("The first two act
absolutely irreducibly on $\F_3^2$ (they are non-abelian and act faithfully)"): (ii) supplies the missing step of
important_notes.md point 1 in the form "non-abelian, of order prime to $3$" for $Q_8$, and (iii) for $\SL_2(\F_3)\supset Q_8$;
it complements the commutator argument of Chapter 1, 5.7.

### Section 4. Characters in characteristic zero (brief)

**4.1 `def:reps:trace-character`** (definition and proposition; P). The trace function $\tr_V(g)=\tr\rho(g)$ is a class
function; $\tr_V(1)=\dim V$; $\tr_{V\oplus W}=\tr_V+\tr_W$; $\tr_{V\otimes W}=\tr_V\tr_W$; $\tr_{V^\vee}(g)=\tr_V(g^{-1})$, which for
$k=\C$ and $G$ finite is $\overline{\tr_V(g)}$ (eigenvalues are roots of unity). Reference: Serre, Section 2.1. RHB
link: this is RHB's "character". Paper: background.

**4.2 `thm:reps:orthogonality`** (theorem; P for (i), (ii); S for (iii); R for (iv)). $G$ finite, $k=\C$, $\langle\phi,\psi\rangle=
\frac1{\#G}\sum_g\phi(g)\overline{\psi(g)}$. (i) For irreducible $V,W$: $\langle\tr_V,\tr_W\rangle=1$ if $V\simeq W$ and $0$
otherwise. (ii) $\dim\Hom_G(V,W)=\langle\tr_V,\tr_W\rangle$; $V$ is irreducible iff $\langle\tr_V,\tr_V\rangle=1$; two
representations with the same character are isomorphic. (iii) The irreducible characters form an orthonormal
basis of the class functions; their number is the number of conjugacy classes; $\sum(\dim V_i)^2=\#G$. (iv) Each
$\dim V_i$ divides $\#G$. Proofs: (i), (ii) by averaging (Schur 2.2 applied to $\frac1{\#G}\sum g\phi g^{-1}$); (iii) by
the regular representation and the centre of $\C[G]$. The abelian case is Chapter 2's orthogonality of Dirichlet
characters (its 10.2). Reference: Serre, Chapter 2 (Theorems 3 to 7, Corollaries). RHB link: RHB's orthogonality
theorems and character tables. Paper: background.

**4.3 `cor:reps:traces-char0`** (corollary; P). If $\operatorname{char}k=0$, $G$ any group, two semisimple
finite-dimensional representations with the same trace functions are isomorphic. (Proof in 5.2: in characteristic $0$
the multiplicities are traces of suitable elements of $k[G]$.) Paper: background ($\ell$-adic representations,
Chapter 5's galois:chebotarev-brauer-nesbitt in characteristic $0$).

**4.4 `ex:reps:tables`** (worked example; P). Character tables of $C_n$ (Chapter 2), $D_4$ and $Q_8$. The last two
tables coincide (classes $\{1\},\{r^2\},\{r^{\pm1}\},\{s,sr^2\},\{sr,sr^3\}$ against $\{1\},\{-1\},\{\pm i\},\{\pm j\},\{\pm k\}$;
four characters of degree $1$ and one of degree $2$) although $D_4\not\simeq Q_8$ (Chapter 1, 2.5). The degree-$2$
representation of $D_4$ is defined over $\Q$; that of $Q_8$ is not defined over $\R$ (Frobenius-Schur indicator $-1$,
stated), but its reduction modulo $3$ is the representation of $Q_8\subset\SL_2(\F_3)$ on $\F_3^2$ of Chapter 1, 6.2
(over a finite field every absolutely irreducible representation is defined over the field of its traces, stated;
Serre, Section 12.1 for the characteristic-zero obstruction). Paper: background ($N_s(\F_3)\simeq D_4$ and $Q_8$ in
Proposition prop:ns).

**4.5 `ex:reps:traces-fail`** (worked example and remark; P). In characteristic $p$ traces do not determine
semisimple representations: for $G=C_2=\{1,s\}$ over $\F_3$, $\mathbf1^{\oplus3}$ and $\operatorname{sgn}^{\oplus3}$ both have trace
$3\equiv0$ at $1$ and $\pm3\equiv0$ at $s$, but $\det(X-s)$ is $(X-1)^3$, respectively $(X+1)^3$. Remark: if $n<p$
(or $p=0$), the traces of $g,g^2,\dots,g^n$ determine $\det(X-g)$ by Newton's identities, so traces suffice for
representations of dimension less than $p$; for $n=2$ and $p\ne2$ the trace and the determinant determine the
characteristic polynomial. Paper: Lemma lem:old (Brauer-Nesbitt is applied with characteristic polynomials, which for
$\dim2$ and equal determinants $\bar\chi_\ell$ amounts to $a_p(h)\equiv a_p(f)\pmod\lambda$).

### Section 5. Brauer-Nesbitt

**5.1 `thm:reps:burnside`** (theorem, the density theorem of Jacobson and Burnside; R, with the proof of (b) sketched).
Let $G$ be any group, $S_1,\dots,S_r$ pairwise non-isomorphic irreducible finite-dimensional representations over $k$,
$D_i=\End_G(S_i)$. (a) The image of $k[G]\to\prod_i\End_k(S_i)$ is $\prod_i\End_{D_i}(S_i)$. (b) If $k$ is algebraically
closed, the image is $\prod_i\End_k(S_i)$; in particular for every $i$ there is $x\in k[G]$ acting on $S_i$ as a projector
of rank one and on every $S_j$, $j\ne i$, as $0$. Reference: Lang, Chapter XVII, Section 3 (density theorem and
Burnside's theorem); Curtis-Reiner, Section 27. Paper: background (used in 2.3 and 5.2).

**5.2 `thm:reps:brauer-nesbitt`** (theorem, Brauer-Nesbitt; P given 5.1). Let $G$ be any group, $k$ any field, and
$V_1,V_2$ finite-dimensional representations of $G$ over $k$ with $\det(X-\rho_1(g))=\det(X-\rho_2(g))$ in $k[X]$ for every
$g\in G$. Then $V_1$ and $V_2$ have the same composition factors with multiplicities, i.e. $V_1^{ss}\simeq V_2^{ss}$. If
$\operatorname{char}k=0$, or if $\dim V_1,\dim V_2<\operatorname{char}k$, equality of the traces $\tr\rho_1(g)=\tr\rho_2(g)$ for all
$g$ suffices. Proof (to be given in full): (0) replace $V_i$ by $V_i^{ss}$ (3.5(ii)). (1) Reduction to $k=\bar k$: for
non-isomorphic irreducible $S,S'$ over $k$, 5.1(a) gives $x\in k[G]$ acting as $1$ on $S$ and $0$ on $S'$, so $S_{\bar k}$
and $S'_{\bar k}$ have no common composition factor; hence the composition factors of $V_{\bar k}$ determine those of
$V$. (2) Over $\bar k$ write $V_1=A\oplus B$, $V_2=A\oplus C$ with $B,C$ semisimple without common irreducible
constituent; cancelling in the factorial ring $\bar k[X]$ gives $\det(X-g\mid B)=\det(X-g\mid C)$ for all $g$. (3)
Traces agree on $G$, hence on $\bar k[G]$ by linearity; with the rank-one elements of 5.1(b), the multiplicity of each
irreducible $S$ satisfies $m_S(B)\equiv m_S(C)$ in $\bar k$; as one of them is $0$, both are divisible by
$p=\operatorname{char}k$ (and are $0$ if $p=0$, which ends the proof). (4) So $B\simeq B'^{\oplus p}$, $C\simeq C'^{\oplus p}$,
$\det(X-g\mid B)=\det(X-g\mid B')^p$, and $f\mapsto f^p$ is injective on $\bar k[X]$; so $B',C'$ satisfy the hypothesis with
smaller dimension, and induction gives $B'=C'=0$. Reference: Curtis-Reiner, Section 30 (the theorem of Brauer and
Nesbitt); the proof above follows the standard one (also in DDT, Section 1, for Galois representations, cited without
number). Paper: Lemma lem:old ("$\bar\rho_h\simeq\bar\rho$ by Chebotarev and Brauer-Nesbitt"); Chapter 5's
galois:chebotarev-brauer-nesbitt and galois:congruent-ap, Chapter 15.

**5.3 `cor:reps:bn-consequences`** (corollary; P). (i) If $\dim V_1=\dim V_2=2$, $\operatorname{char}k\ne2$ and
$\det\rho_1=\det\rho_2$, then $\tr\rho_1=\tr\rho_2$ on $G$ implies $V_1^{ss}\simeq V_2^{ss}$. (ii) Let $k\subset k'$ be fields, $V_1$
over $k$ and $V_2$ over $k'$ with $\det(X-\rho_1(g))=\det(X-\rho_2(g))$ for all $g$. If $V_1\otimes_kk'$ is irreducible (for
example if $V_1$ is absolutely irreducible), then $V_2\simeq V_1\otimes_kk'$ (no semisimplicity of $V_2$ is assumed: $V_2^{ss}$ is
irreducible of full dimension, so $V_2$ is irreducible). If $V_1$ is only irreducible over $k$, the conclusion can fail:
$C_4$ on $\F_3^2$ (2.5) and $\psi\oplus\psi^{-1}$ over $\F_9$ have the same characteristic polynomials. Paper: Lemma lem:old (the
residual representation $\bar\rho_h$ lives over the residue field of the coefficient ring of $h$, $\bar\rho$ over $\F_\ell$;
(ii) with $\bar\rho$ absolutely irreducible gives $\bar\rho_h\simeq\bar\rho\otimes k'$: important_notes.md point 10), Section 3
of the paper ("that is, $a_p(g)\equiv a_p(f)\pmod\lambda$").

### Section 6. Restriction, induction, Frobenius reciprocity, Mackey, Clifford

**6.1 `def:reps:induction`** (definition and proposition; P). Let $H\le G$ have finite index $m$, $W$ a representation of $H$
over $k$ (or an $R[H]$-module). $\Res^G_HV$ is $V$ viewed as an $H$-module. $\Ind_H^GW=k[G]\otimes_{k[H]}W$; with coset
representatives $G=\bigsqcup_{i=1}^ms_iH$ it is $\bigoplus_is_i\otimes W$, and if $gs_i=s_jh$ then $g(s_i\otimes w)=s_j\otimes hw$;
$\dim\Ind W=m\dim W$. Equivalently (finite index) the module of maps $f\colon G\to W$ with $f(hx)=hf(x)$, $G$ acting by
right translation. Trace formula (any field): $\tr(g\mid\Ind W)=\sum_{i:\,s_i^{-1}gs_i\in H}\tr(s_i^{-1}gs_i\mid W)$. Index two:
if $H$ has index $2$ and $s\notin H$, then $\tr(h\mid\Ind W)=\tr(h\mid W)+\tr(s^{-1}hs\mid W)$ for $h\in H$ and $\tr(g\mid\Ind W)=0$
for $g\notin H$; for a character $\psi$ of $H$, in the basis $1\otimes1$, $s\otimes1$: $h\mapsto\operatorname{diag}(\psi(h),\psi^s(h))$
with $\psi^s(h)=\psi(s^{-1}hs)$, and $s\mapsto\begin{pmatrix}0&\psi(s^2)\\1&0\end{pmatrix}$. Reference: Serre, Sections 3.3, 7.1, 7.2.
Paper: Proposition prop:ns ($\Ind\psi$), Lemma lem:h0 ("induced from $\Gal(\Qbar/\Q(\sqrt{-3}))$"); Chapter 6's 6.4 and 6.5
use the trace formula.

**6.2 `thm:reps:frobenius-reciprocity`** (theorem, Frobenius reciprocity; P). For $H\le G$ of finite index, $W$ a
representation of $H$ and $V$ of $G$ (over a field or a commutative ring), there are natural isomorphisms
$\Hom_G(\Ind_H^GW,V)\simeq\Hom_H(W,\Res_HV)$ and $\Hom_G(V,\Ind_H^GW)\simeq\Hom_H(\Res_HV,W)$. In characteristic $0$ for finite
$G$: $\langle\tr_{\Ind W},\tr_V\rangle_G=\langle\tr_W,\tr_{\Res V}\rangle_H$. Reference: Serre, Section 7.2 (Theorem 13).
Paper: Proposition prop:ns ("$\bar\rho\simeq\Ind\psi$ by Frobenius reciprocity": a nonzero $H$-map $\psi\to\Res\bar\rho_{\F_9}$
gives a nonzero $G$-map $\Ind\psi\to\bar\rho_{\F_9}$, surjective as $\bar\rho_{\F_9}$ is irreducible, hence an isomorphism by
dimensions).

**6.3 `prop:reps:projection-formula`** (proposition; P). For $H\le G$ of finite index: (i)
$\Ind_H^G(W\otimes\Res_HU)\simeq\Ind_H^GW\otimes U$; in particular, for a character $\chi$ of $G$ trivial on $H$,
$\Ind W\otimes\chi\simeq\Ind W$. (ii) $\Ind_H^G\mathbf1=k[G/H]$; for $H$ of index $2$ and $\operatorname{char}k\ne2$,
$\Ind_H^G\mathbf1\simeq\mathbf1\oplus\chi_H$, $\chi_H$ the character with kernel $H$. (iii) Transitivity, additivity, compatibility
with duals and with extension of scalars. Reference: Serre, Section 7.2. Paper: Proposition prop:ns ("so
$\bar\rho\simeq\bar\rho\otimes\chi_{-3}$"), Lemma lem:h0.

**6.4 `thm:reps:mackey`** (theorem; R for (a), S for (b), P for (c)). (a) (Mackey's formula) For $H,K\le G$ of finite
index, $\Res_K\Ind_H^GW\simeq\bigoplus_{s\in K\backslash G/H}\Ind^K_{K\cap sHs^{-1}}W^s$, $W^s(x)=W(s^{-1}xs)$. (b) (Mackey's
irreducibility criterion, characteristic $0$, $G$ finite) $\Ind_H^GW$ is irreducible iff $W$ is irreducible and for every
$s\in G\setminus H$ the representations $W^s$ and $W$ of $H_s=sHs^{-1}\cap H$ have no common irreducible constituent. (c)
(Index two, any characteristic.) Let $H\le G$ have index $2$, $s\notin H$, $W$ an absolutely irreducible representation
of $H$. Then $\Res_H\Ind W\simeq W\oplus W^s$, and $\Ind W$ is absolutely irreducible iff $W_{\bar k}\not\simeq W^s_{\bar k}$. Proof of
(c): if $W\not\simeq W^s$, the only $H$-submodules of $W\oplus W^s$ over $\bar k$ are $0$, $W$, $W^s$ and the sum, and $s$ swaps the two
summands, so no proper nonzero $G$-submodule exists; if $W\simeq W^s$, $\End_G(\Ind W_{\bar k})=\Hom_H(W,W\oplus W^s)$ has
dimension $2$ over $\bar k$ (6.2), so $\Ind W_{\bar k}$ is not irreducible (Schur 2.2(ii)). Reference: Serre, Sections 7.3, 7.4.
Paper: Proposition prop:ns ($\Ind\psi$ is irreducible since $\psi^s=\psi^{-1}\ne\psi$), Lemma lem:h0.

**6.5 `thm:reps:clifford`** (theorem, Clifford; P). Let $N\trianglelefteq G$ have finite index and $V$ an irreducible
representation of $G$ over any field. Then $\Res_NV$ is semisimple, its irreducible constituents form one $G$-orbit
under $W\mapsto W^g$, and they all occur with the same multiplicity. Proof: for an irreducible $N$-submodule $W$,
$\sum_ggW$ is a nonzero $G$-submodule, hence $V$, and a sum of irreducibles $gW\simeq W^{g^{-1}}$ is semisimple (3.1).
Reference: Curtis-Reiner, Section 49; Serre, Section 8.1. Paper: background for 6.6.

**6.6 `thm:reps:clifford-index-two`** (theorem, Clifford theory for an index-two subgroup; P). Let $G$ be any group,
$H\le G$ of index $2$, $s\in G\setminus H$, $\chi_H\colon G\to\{\pm1\}$ the character with kernel $H$, $k$ a field with
$\operatorname{char}k\ne2$, and $V$ an absolutely irreducible representation of $G$ of dimension $n$. Exactly one of the
following holds. (A) $\Res_HV$ is absolutely irreducible; then $V\not\simeq V\otimes\chi_H$, and $\Ind_H^G\Res_HV\simeq
V\oplus(V\otimes\chi_H)$. (B) $\Res_HV$ is not absolutely irreducible; then $n=2d$, there is an absolutely irreducible
representation $W$ of $H$ over $\bar k$ of dimension $d$ with $W\not\simeq W^s$, $\Res_HV_{\bar k}\simeq W\oplus W^s$,
$V_{\bar k}\simeq\Ind_H^GW$, and $V\simeq V\otimes\chi_H$ over $k$. Moreover $V\simeq V\otimes\chi_H$ iff (B) holds; in that case
$\Hom_G(V,V\otimes\chi_H)$ is a line over $k$, spanned by an isomorphism $\phi$ with $\phi^2\in k^\times$ and $\tr\phi=0$, whose
eigenspaces over $\bar k$ are $W$ and $W^s$. For $n=2$: (B) iff $V_{\bar k}\simeq\Ind_H^G\psi$ for a character $\psi$ of $H$
with $\psi^s\ne\psi$. Proof: (A) an isomorphism $V\to V\otimes\chi_H$ commutes with $H$, so is a scalar (Schur), forcing
$\chi_H=1$; the induced statement is 6.3(i), (ii). (B) by Clifford 6.5 over $\bar k$ the constituents of $\Res_H$ are
conjugate, so at least two of dimension $d$, whence $n\ge2d$; Frobenius reciprocity 6.2 gives a surjection
$\Ind W\to V_{\bar k}$, so $n\le2d$; hence equality, $V_{\bar k}\simeq\Ind W$, and $W\not\simeq W^s$ by 6.4(c); $V\simeq V\otimes\chi_H$ by
6.3(i) over $\bar k$ and descent 1.4(iii). Finally $\phi^2\in\End_G(V)=k$, and $\tr\phi=0$ by 7.2. Reference: Serre,
Section 8.2 (characteristic $0$); the argument is characteristic-free once $\operatorname{char}k\ne2$. Paper: Lemma lem:h0
("for $\ell=3$ and $\bar\rho$ irreducible, $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ holds if and only if $\bar\rho$ is induced from
$\Gal(\Qbar/\Q(\sqrt{-3}))$, that is, if and only if its restriction there is not absolutely irreducible": correct for
$\bar\rho$ absolutely irreducible, point 10, with "induced" read over $\bar\F_3$, point N1 of Part 8), Proposition prop:ns,
the hypothesis of Theorem thm:main and $S_f$; Chapter 5's galois:index-two-restriction is this theorem plus continuity.

**6.7 `prop:reps:dihedral`** (proposition; P). Let $\operatorname{char}k\ne2$ and $\rho\colon G\to\GL_2(k)$ absolutely irreducible
with finite projective image $P(\rho)\subset\PGL_2(\bar k)$. (i) $P(\rho)$ is not cyclic (a group whose image modulo scalars
is cyclic is abelian; 3.7(i)). (ii) The following are equivalent: $P(\rho)$ is dihedral of order $2m$, $m\ge2$ (with
$D_2=V_4$); $\rho\simeq\rho\otimes\chi$ for some character $\chi$ of order $2$; $\rho_{\bar k}\simeq\Ind_H^G\psi$ for some subgroup $H$ of
index $2$. (iii) The characters $\chi\ne1$ with $\rho\simeq\rho\otimes\chi$ correspond bijectively to the cyclic subgroups of index
$2$ of $P(\rho)$ (via $H=\ker\chi$ = the preimage): exactly one if $m\ge3$, exactly three if $P(\rho)\simeq V_4$. Proof: if
$\rho_{\bar k}=\Ind\psi$, in the basis of 6.1 $\rho(H)$ is diagonal and $\rho(G\setminus H)$ antidiagonal, so $P(\rho)$ is a cyclic
group (image of $H$ in the diagonal torus modulo scalars) extended by an involution acting by inversion; conversely
the preimage $H$ of a cyclic subgroup of index $2$ has abelian image, so $\Res_H\rho$ is absolutely reducible (3.7(i)) and
6.6(B) applies. Reference: elementary; Serre72, Section 2 for the dihedral case of Dickson's list. Paper: Proposition
prop:ns and Section sec:anomaly (the projective image of $N_s(\F_3)$ is $V_4$, so its representation is induced in three
ways, one of them from the determinant-one subgroup, 8.2), the hypothesis of Theorem thm:main (for $N_{ns}(\F_3)$, with
projective image $D_4$, the representation is induced from $C_{ns}(\F_3)$, not from the determinant-one subgroup, 8.3; so
"dihedral" alone is not the excluded case: the hypothesis singles out the field $\Q(\sqrt{\ell^*})$), Dickson 11.2.

### Section 7. Twisting, the adjoint, the trace-zero lemma, the symmetric square, the trace form

**7.1 `prop:reps:twist`** (proposition; P). Let $\chi\colon G\to k^\times$ (or $R^\times$) be a character. (i)
$\tr(\rho\otimes\chi)(g)=\chi(g)\tr\rho(g)$; $\det(X-(\rho\otimes\chi)(g))=\det(X-\chi(g)\rho(g))$; $\det(\rho\otimes\chi)=\chi^n\det\rho$. (ii) $V$
is (absolutely) irreducible iff $V\otimes\chi$ is; $\Hom_G(V\otimes\chi,W\otimes\chi)=\Hom_G(V,W)$; $(V\otimes\chi)^\vee=V^\vee\otimes\chi^{-1}$;
$\Res_{\ker\chi}(V\otimes\chi)=\Res_{\ker\chi}V$. (iii) $\End(V\otimes\chi)=\End(V)$ as representations (the same space with the
same action), hence $\ad(V\otimes\chi)=\ad V$. (iv) If $V\simeq V\otimes\chi$ then $\chi^n=1$ on $G$ (determinants); for $n=2$,
$\chi^2=1$. Reference: elementary. Paper: Lemma lem:twist and Theorem thm:twist (twisting; the Galois statement
$\rho_{E^{(d)},\ell}=\rho_{E,\ell}\otimes\chi_d$ is Chapter 9), Lemma lem:h0 ("comparing determinants it forces
$\bar\chi_\ell^2=1$"), proof of Theorem thm:main ("$\ad T$ is unchanged by the twist"), Lemma lem:euler (types
$\mathrm I_n^*$, $\mathrm I_0^*$: $\ad V=\ad V'$).

**7.2 `lem:reps:trace-zero`** (lemma, the trace-zero lemma; P). Let $\phi\colon V\to V\otimes\chi$ be a $G$-map, i.e.
$\phi\rho(g)=\chi(g)\rho(g)\phi$ for all $g$. Then $(1-\chi(g))\tr\phi=0$ for every $g\in G$, since
$\tr\phi=\tr(\rho(g)^{-1}\phi\rho(g))=\chi(g)\tr\phi$. Hence $\tr\phi=0$ if $\chi\ne1$ (over a field), or, over a ring $R$, if
$1-\chi(g)\in R^\times$ for some $g$. If moreover $V$ is absolutely irreducible, $\Hom_G(V,V\otimes\chi)$ has dimension at most
one and a nonzero element is an isomorphism (Schur 2.2). Reference: elementary. Paper: Lemma lem:h0 ("an isomorphism
$\phi\colon\bar\rho\to\bar\rho\otimes\chi_{-3}$ has trace $0$, since $\tr\phi=\tr(\bar\rho(g)^{-1}\phi\bar\rho(g))=\chi_{-3}(g)\tr\phi$"), Proposition
prop:ns; Chapter 5's galois:twist (b) and Chapter 6's 6.5 cite it.

**7.3 `def:reps:adjoint`** (definition and proposition; P). $\End(V)=V\otimes V^\vee$ with $g\cdot x=\rho(g)x\rho(g)^{-1}$; $\ad V$
its trace-zero part (C3). (i) If $n=\dim V$ is invertible in $k$ (or in $R$), $\End(V)=k\cdot1\oplus\ad V$ as representations,
$x=\frac{\tr x}{n}1+(x-\frac{\tr x}{n}1)$; for $n=2$ this needs $\operatorname{char}k\ne2$ ($\ell$ odd). (ii) If $\rho(g)$ has eigenvalues
$\lambda_1,\dots,\lambda_n$ in $\bar k$, then $\Ad\rho(g)$ has eigenvalues $\lambda_i/\lambda_j$ on $\End(V)$; for $n=2$ it has $\lambda_1/\lambda_2$, $1$,
$\lambda_2/\lambda_1$ on $\ad V$, and $\det(X-\Ad\rho(g)\mid\ad V)=(X-1)\bigl(X^2-(\tr(g)^2/\det g-2)X+1\bigr)$. (iii) Formulas in the basis
$e,h,f$ (C3; checked symbolically, Part 7): $\Ad\operatorname{diag}(x,y)=\operatorname{diag}(x/y,1,y/x)$; for $t=\begin{pmatrix}1&n'\\0&1\end{pmatrix}$:
$(t-1)e=0$, $(t-1)h=-2n'e$, $(t-1)f=n'h-n'^2e$; for $F=\begin{pmatrix}\varepsilon q&c'\\0&\varepsilon\end{pmatrix}$: $Fe F^{-1}=qe$,
$FhF^{-1}=h-2c'\varepsilon^{-1}e$, $FfF^{-1}=q^{-1}f+c'\varepsilon^{-1}q^{-1}h-c'^2\varepsilon^{-2}q^{-1}e$. Reference: elementary. Paper: Section 1.1
($A_f=\ad V$), the eigenvalues $\alpha/\beta,1,\beta/\alpha$ in Lemma lem:euler and Chapter 19, Lemma lem:tamfactor (the three formulas
for $t$ and the action of $F$ on $e$ and $h$; with $\varepsilon=\pm1$, $\varepsilon^{-1}=\varepsilon$ as the paper writes); Chapter 16 cites these.

**7.4 `prop:reps:H0-twisted-adjoint`** (proposition; P). Let $V$ be a representation over $k$ (or a free $R$-module of rank
$n$ with $R$ local) and $\chi$ a character. (i) $(\End V\otimes\chi)^G=\Hom_G(V,V\otimes\chi)$ (1.3). (ii) If $n$ is invertible,
$(\End V\otimes\chi)^G=(\ad V\otimes\chi)^G\oplus R(\chi)^G$ and $(\ad V\otimes\chi)^G=\{\phi\in\Hom_G(V,V\otimes\chi):\tr\phi=0\}$. (iii) If $\chi\ne1$
(over $R$ local: if the reduction $\bar\chi$ of $\chi$ to the residue field is nontrivial), then $R(\chi)^G=0$, so every $G$-map
$V\to V\otimes\chi$ has trace $0$ and $(\ad V\otimes\chi)^G=\Hom_G(V,V\otimes\chi)$ (agreeing with 7.2). (iv) If $V$ is absolutely irreducible
and $n$ is invertible: $(\ad V)^G=0$; and for $\chi\ne1$, $(\ad V\otimes\chi)^G\ne0$ iff $V\simeq V\otimes\chi$, in which case it is a line.
Reference: elementary. Paper: Lemma lem:h0 ("the $\ell$-torsion of $H^0(\Q,W^D)$ is $H^0(\Q,\ad\bar\rho\otimes\bar\chi_\ell)$, the space of
trace-zero $G_\Q$-maps $\bar\rho\to\bar\rho\otimes\bar\chi_\ell$"; by (iii) the trace condition is automatic, as Chapter 21's A4.11
step (2) observes with $\mu_{\ell^k}(\Q)=0$), Proposition prop:ns ("$H^0(\Q,\ad\bar\rho_{E,3}(1))\ne0$").

**7.5 `prop:reps:sym2`** (proposition; P). Let $\dim V=2$ with basis $e_1,e_2$, $\omega(x,y)=\det[x\,|\,y]$, and $\Sym V$ the
symmetric square (quotient of $V\otimes V$ by $x\otimes y-y\otimes x$), with basis $e_1^2,e_1e_2,e_2^2$; if $\rho(g)$ has eigenvalues
$\lambda,\mu$, then $\Sym\rho(g)$ has $\lambda^2,\lambda\mu,\mu^2$. (i) The map $\Xi\colon\Sym V\to\ad V$, $\Xi(xy)(v)=\omega(v,x)y+\omega(v,y)x$, is
well defined, lands in trace zero, and satisfies $\Xi(g\cdot m)=\det(g)\,\rho(g)\Xi(m)\rho(g)^{-1}$, so it is a $G$-map
$\Sym V\otimes\det^{-1}\to\ad V$. In coordinates $\Xi(e_1^2)=-2e$, $\Xi(e_1e_2)=h$, $\Xi(e_2^2)=2f$; so $\Xi$ is an isomorphism iff
$2$ is invertible (over $\Z$ its image has index $4$; over $\Zl$ it is an isomorphism of lattices iff $\ell$ is odd). (ii)
Hence $\ad\rho\simeq\Sym\rho\otimes\det^{-1}$ and $\Sym\rho\simeq\ad\rho\otimes\det$; and, for $\operatorname{char}k\ne2$, $V\otimes V\simeq\Sym V\oplus\det$
and $V\otimes V^\vee\simeq\ad V\oplus\mathbf1$. (iii) (Normalisations; Galois input from Chapters 9, 18, 19.) With $V=V_\ell E$,
$\det=\chi_\ell$: $\Sym V\simeq\ad V(1)$ and $\Sym(V^\vee)\simeq\ad V(-1)$; the classical $L(\Sym f,s)$ is the $L$-function of
$\Sym(V^\vee)=\Sym H^1$, whence $L_p(\Sym f,s)=L_p(A_f,s-1)$ (Chapter 19 for the $L$-factors). Reference: elementary;
Fulton-Harris style computation. Paper: Section 1.1 ("In the normalisation of the symmetric square,
$L_p(\Sym f,s)=L_p(A_f,s-1)$"), the Introduction (Flach's theorem on $\Sym f$; Rankin-Shimura), Chapters 18, 19.

**7.6 `prop:reps:trace-form`** (proposition; P). Let $T$ be free of rank $n$ over a commutative ring $R$ with a $G$-action.
(i) $B(x,y)=\tr(xy)$ on $\End_R(T)$ is $G$-invariant ($B(gxg^{-1},gyg^{-1})=B(x,y)$) and perfect (the matrix units satisfy
$B(E_{ij},E_{kl})=\delta_{jk}\delta_{il}$, a permutation Gram matrix of determinant $\pm1$). (ii) For $n=2$ the Gram matrix of $B$ on $\ad T$
in the basis $e,h,f$ is $\begin{pmatrix}0&0&1\\0&2&0\\1&0&0\end{pmatrix}$, of determinant $-2$: $B$ is perfect on $\ad T$ iff $2\in R^\times$. (iii) Hence
for $R=\Zl$, $\ell$ odd, and $A=\ad T$: $x\mapsto B(x,-)$ is a $G$-isomorphism $A\simeq A^\vee=\Hom_{\Zl}(A,\Zl)$, and for every
character $\chi\colon G\to\Zl^\times$, $\Hom_{\Zl}(A,\Zl(\chi))\simeq A(\chi)$; likewise with $\Ql$ and $\Ql/\Zl$ coefficients (via Chapter 3).
For $\ell=2$ the image of $A$ in $A^\vee$ has index $2$. Reference: elementary (Gram determinants: Chapter 3). Paper:
Section 4.2 ("$T^D=\Hom(A,\Zl(1))\simeq A(1)$ (via the trace form)", with $\chi=\chi_\ell$; this is where $\ell$ odd enters), Lemma
lem:h0 ($W^D=\ad T(1)\otimes\Ql/\Zl$), Lemma lem:fpr; Chapter 18 cites this item.

**7.7 `prop:reps:adjoint-invariance`** (proposition; P). (i) $\ad(V\otimes\chi)=\ad V$ (7.1(iii)). (ii) $x\mapsto-x^{t}$ (the
negative transpose, $x^t\in\End(V^\vee)$) is a $G$-isomorphism $\ad V\simeq\ad(V^\vee)$, and also $\End V\simeq\End(V^\vee)$ (either sign
works for modules; $-x^t$ also respects brackets). (iii) Let $L\subset V$ be an $\mathcal{O}$-lattice and $L'=cL$, $c\in K^\times$. Then
$\End_\mathcal{O}(L')=\End_\mathcal{O}(L)$ and $\ad L'=\ad L$ inside $\End_K(V)$, where $\ad L=\End_\mathcal{O}(L)\cap\ad V$; and under (ii) $\ad(L^\vee)$
corresponds to $\ad L$, $L^\vee=\Hom_\mathcal{O}(L,\mathcal{O})$. (iv) Consequently a lattice homothetic to $L$, to $L^\vee$, or to a twist $L\otimes\chi$
has the same adjoint lattice as $L$, up to these canonical identifications. Reference: elementary. Paper: Section 4.2
("the lattice $M_{f,\lambda}$ of DFG04 and $T_\ell E$ are homothetic when $\bar\rho$ is irreducible, so their adjoints coincide": by
10.3 and (iv), with $M_{f,\lambda}$ homothetic to the dual of $T_\ell E$, important_notes.md point 26), proof of Theorem thm:main
(type $\mathrm I_n^*$), Theorem thm:quant Step 3 ("$A_g=A_f$").

### Section 8. $\GL_2(\F_3)$ and its subgroups on $\F_3^2$ and $\F_9^2$

**8.1 `prop:reps:gl23-table`** (proposition and table; P, the table checked by computer, Part 7). For the standard models
(C6) acting on $\F_3^2$ by the standard representation $\rho$ (and on $\F_9^2$ after extension of scalars):

| $H$ | order | $\det$ onto $\F_3^\times$ | irreducible over $\F_3$ | absolutely irreducible | $\dim\End_H$ | $\dim(\ad\rho)^H$ | $\dim\Hom_H(\rho,\rho\otimes\det)$ (trace-zero part) | $\rho\simeq\rho\otimes\det$ | projective image |
|-|-|-|-|-|-|-|-|-|-|
| $\GL_2(\F_3)$ | 48 | yes | yes | yes | 1 | 0 | 0 (0) | no | $S_4$ |
| $\SL_2(\F_3)$ | 24 | no | yes | yes | 1 | 0 | 1 (0) | ($\det=1$) | $A_4$ |
| $N_{ns}(\F_3)$ | 16 | yes | yes | yes | 1 | 0 | 0 (0) | no | $D_4$ |
| $Q_8$ | 8 | no | yes | yes | 1 | 0 | 1 (0) | ($\det=1$) | $V_4$ (normal) |
| $N_s(\F_3)$ | 8 | yes | yes | yes | 1 | 0 | 1 (1) | **yes** | $V_4$ (not normal) |
| $C_{ns}(\F_3)$ | 8 | yes | yes | no | 2 | 1 | 0 (0) | no | $C_4$ |
| $C_4=\langle J\rangle$ | 4 | no | yes | no | 2 | 1 | 2 (1) | ($\det=1$) | $C_2$ |
| $C_s(\F_3)$ | 4 | yes | no | no | 2 | 1 | 2 (2) | yes | $C_2$ |
| $\mathrm B(\F_3)$ | 12 | yes | no | no | 1 | 0 | 1 (1) | no | $S_3$ |
| $\mathrm U$ | 3 | no | no | no | 2 | 1 | 2 (1) | ($\det=1$) | $C_3$ |

Remarks to be made in the text: for the subgroups of $\SL_2(\F_3)$ the twist by $\det$ is trivial; $\End_{\mathrm B}=\F_3$ although
$\mathrm B$ is reducible (3.3(d)); the trace-zero intertwiner for $\mathrm B$ is $e$ (not invertible). Reference: Chapter 1, 6.3 to
6.6 for the groups; computation. Paper: Proposition prop:ns, Lemma lem:h0, Section sec:anomaly, Remark rem:ns.

**8.2 `prop:reps:ns3-induced`** (proposition; P). Let $\rho$ be the standard representation of $N_s(\F_3)=\langle J,\sigma\rangle$
(Chapter 1, 6.5) and $C_4=\langle J\rangle=N_s(\F_3)\cap\SL_2(\F_3)$. (i) $\rho$ is absolutely irreducible (3.7(iv)), but
$\Res_{C_4}\rho\otimes\F_9\simeq\psi\oplus\psi^{-1}$, $\psi(J)=i$, with eigenvectors $v=(1,-i)^t$ and $\sigma v=(1,i)^t$ (2.5); $\psi^\sigma=\psi^{-1}\ne\psi$
since $\sigma J\sigma^{-1}=J^{-1}$. (ii) In the basis $(v,\sigma v)$ of $\F_9^2$, $\rho(J)=\operatorname{diag}(i,-i)$ and $\rho(\sigma)=w$, which is the matrix
form of $\Ind_{C_4}^{N_s}\psi$ of 6.1 (with $s=\sigma$, $\sigma^2=1$); so $\rho\otimes\F_9\simeq\Ind_{C_4}^{N_s}\psi$, as Frobenius reciprocity
6.2 also shows. Over $\F_3$, $\rho$ is *not* induced from a character of $C_4$ ($\Res_{C_4}\rho$ is irreducible over $\F_3$).
(iii) $\rho\simeq\rho\otimes\det$ over $\F_3$, with intertwiner $\phi=J$: $J\rho(g)=\det(g)\rho(g)J$ for all $g$ (check on $J$ and $\sigma$:
$J\sigma=-\sigma J$); $\tr J=0$, $J^2=-1$, and the eigenlines of $J$ over $\F_9$ are the two summands of (i), as 6.6(B)
predicts. (iv) The projective image is $V_4$ (Chapter 1, 6.11), so by 6.7(iii) $\rho\simeq\rho\otimes\chi$ for each of the three
characters $\chi$ of $N_s(\F_3)/\{\pm1\}$: their kernels are $C_4$ ($\chi=\det$, intertwiner $J$), $C_s(\F_3)$ (intertwiner
$\sigma$) and $\{\pm1,\pm w\}$ (intertwiner $w$). (v) $(\ad\rho\otimes\det)^{N_s}=\F_3J$, a line; $(\ad\rho)^{N_s}=0$. Reference:
computation (Part 7). Paper: Proposition prop:ns ("In the third case $\bar\rho|_{\Gal(\Qbar/\Q(\sqrt{-3}))}\otimes\F_9=\psi\oplus\psi^{-1}$ for a
character $\psi$ of order $4$, and $\bar\rho\simeq\Ind\psi$ by Frobenius reciprocity, so $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ and
$H^0(\Q,\ad\bar\rho(1))\ne0$"; the isomorphism with $\Ind\psi$ is over $\F_9$, point N1), Lemma lem:h0, Section sec:anomaly,
Remark rem:ns; Chapter 5's Exercise 12 (the three quadratic subfields correspond to (iv)).

**8.3 `prop:reps:nns3`** (proposition; P). Let $\rho$ be the standard representation of $N_{ns}(\F_3)=\langle a,\sigma\rangle$
(Chapter 1, 6.6). (i) $\rho$ and $\Res_{Q_8}\rho$ are absolutely irreducible (3.7(iv)); $Q_8=N_{ns}(\F_3)\cap\SL_2(\F_3)$. (ii)
$\rho\not\simeq\rho\otimes\det$: an isomorphism $\phi$ gives $\phi\rho(g)\phi^{-1}=\det(g)\rho(g)$, so taking traces
$\tr\rho(g)=0$ whenever $\det g=-1$ (characteristic $\ne2$), but the four elements of order $8$ and determinant $-1$ have trace $\pm1$;
$(\ad\rho\otimes\det)^{N_{ns}}=0$. (iii) Nevertheless the projective image is $D_4$, so $\rho$ is dihedral (6.7): over $\F_9$,
$C_{ns}(\F_3)\simeq\F_9^\times$ acts with the eigencharacters $\theta$, $\theta^3$, $\theta(a)=1+i$ of order $8$, $\theta^\sigma=\theta^3\ne\theta$, and
$\rho\otimes\F_9\simeq\Ind_{C_{ns}}^{N_{ns}}\theta$; $\rho\simeq\rho\otimes\chi_{ns}$ for the character $\chi_{ns}$ with kernel $C_{ns}(\F_3)$, and for no other
nontrivial character. Reference: computation. Paper: Proposition prop:ns (the image $N_{ns}(\F_3)$: "the first two act
absolutely irreducibly"), Section sec:anomaly ("no curve with image ... $N_{ns}(\F_3)$ violates"), and the reading of the
hypothesis of Theorem thm:main: "dihedral" is not the excluded case, "induced from $\Q(\sqrt{-3})$" is.

**8.4 `prop:reps:gl23-sl23`** (proposition; P). The standard representations of $\SL_2(\F_3)$ and $\GL_2(\F_3)$ are absolutely
irreducible (they contain $Q_8$; 3.7(iii), (iv)); $\GL_2(\F_3)$: $\rho\not\simeq\rho\otimes\det$ (elements of order $8$ as in 8.3(ii)),
$(\ad\rho\otimes\det)^{\GL_2}=0$; projective images $A_4$, $S_4$ (exceptional in Dickson's list, 11.2). Paper: Proposition
prop:ns (the image $\GL_2(\F_3)$, the "generic" case).

**8.5 `thm:reps:three-images`** (theorem, the representation-theoretic core of Proposition prop:ns; P). Let $H\le\GL_2(\F_3)$
be conjugate to $\GL_2(\F_3)$, $N_{ns}(\F_3)$ or $N_s(\F_3)$ (by Chapter 1, 6.7, these are exactly the subgroups with surjective
determinant, no stable line, and an element of determinant $-1$ and trace $0$), $H_1=H\cap\SL_2(\F_3)$ (of index $2$, the kernel
of $\det|_H$), and $\rho$ the standard representation. The following are equivalent: (a) $H$ is conjugate to $N_s(\F_3)$; (b)
$\Res_{H_1}\rho$ is not absolutely irreducible; (c) $\rho\simeq\rho\otimes\det$; (d) $(\ad\rho\otimes\det)^H\ne0$; (e)
$\rho\otimes\F_9\simeq\Ind_{H_1}^H\psi$ for a character $\psi$ of $H_1$ of order $4$; (f) $H_1$ is abelian. When they fail,
$(\ad\rho\otimes\det)^H=0$; when they hold, $(\ad\rho\otimes\det)^H$ is the line spanned by a trace-zero isomorphism. Proof: (b), (c),
(e) are equivalent by 6.6 with $\chi_H=\det$ ($\det$ has kernel $H_1$ and values $\pm1$); (c) iff (d) by 7.4(iv); (a) iff (b) iff (f)
by 8.2 to 8.4 (or by 3.7). Reference: proved here from Chapter 1. Paper: Proposition prop:ns (with Chapter 5:
$\det\bar\rho_{E,3}=\chi_{-3}=\bar\chi_3$ cuts out $\Q(\sqrt{-3})$, so $\bar\rho(G_{\Q(\sqrt{-3})})=H_1$), Lemma lem:h0 for $\ell=3$, the
hypothesis of Theorem thm:main at $\ell=3$, Section sec:anomaly; Chapter 11 assembles the elliptic-curve statement.

### Section 9. Unipotent elements and cyclic groups of order 2, 3, 4, 6 on rank-two spaces and lattices

**9.1 `prop:reps:unipotent-invariants`** (proposition; P). Let $k$ be a field, $V=k^2$, $u\in\GL_2(k)$ unipotent with $u\ne1$
(so $u=1+n'e$ in a suitable basis, $n'\ne0$; Chapter 1, 5.6), and $\varepsilon\in k^\times$. (i) $V^u=\ker(u-1)=\operatorname{im}(u-1)$ is a
line; if $\varepsilon\ne1$, $V^{\varepsilon u}=0$ (in particular for "minus a unipotent", $\varepsilon=-1$, $\operatorname{char}k\ne2$). (ii) If
$\operatorname{char}k\ne2$: $(\ad V)^u=(\ad V)^{\varepsilon u}=k\,(u-1)=k\,e$, a line (by the formulas of 7.3(iii): $(t-1)h=-2n'e$,
$(t-1)f=n'h-n'^2e$); in characteristic $2$ it is the plane $ke+kh$. The same holds for the group generated by $u$ (or by
$\varepsilon u$), and for a group acting through $\langle\varepsilon\rangle\times\langle u\rangle$ with $\varepsilon$ scalar. (iii) If $F\in\GL_2(k)$
satisfies $FuF^{-1}=u^q$ ($q\in\Z$; or $q\in\Zl$ when $u$ lies in a pro-$\ell$ group, Chapter 7), then $F$ preserves
$(\ad V)^u$ and acts on it by $q$: $F(u-1)F^{-1}=u^q-1=q(u-1)$ since $(u-1)^2=0$. Then $F^{-1}$ acts by $q^{-1}$. Reference:
elementary; Chapter 1, 5.6 for the group facts. Paper: Lemma lem:IV ("its image in $\Aut(E[3])$ is a nontrivial unipotent
subgroup ... $E[3]^{I_q}$ is a line"), Remark rem:types ("minus a unipotent", "a ramified quadratic character times a
unipotent": $E[3]^{I_q}=0$), Lemma lem:euler type $\mathrm I_n$ ("$(\ad V)^{I_q}$ is a line with eigenvalue $q^{-1}$": by (iii), the
eigenvalue is $q$ for the arithmetic Frobenius and $q^{-1}$ for the geometric one, important_notes.md point 11), Lemma
lem:tamfactor ($(t-1)M=n'(\Zl e\oplus\Zl h)$ for $\ell$ odd, worked over $\Zl$ in Chapter 16).

**9.2 `lem:reps:commutant`** (lemma; P). Let $k$ be a field and $x\in\End_k(V)$, $\dim V=n$, whose characteristic polynomial
has $n$ distinct roots in $\bar k$ (more generally, whose minimal polynomial equals its characteristic polynomial). Then
the commutant $\{y\in\End_k(V):xy=yx\}$ is $k[x]\simeq k[X]/(\det(X-x))$, of dimension $n$. For $n=2$ and $x$ not scalar: the
commutant is $k\cdot1\oplus k\cdot x$, and (if $\operatorname{char}k\ne2$) its trace-zero part is the line spanned by $2x-\tr x$. Examples:
for $\sigma$ with $\sigma^2+\sigma+1=0$ the line is $k(2\sigma+1)$, with $(2\sigma+1)^2=-3$ ("the line spanned by $\sqrt{-3}$"); for $\tau$ with
$\tau^2=-1$ it is $k\tau$. The commutant is a field iff $\det(X-x)$ is irreducible over $k$: for $k=\Ql$ and $\sigma$ of order $3$,
iff $\ell\not\equiv1\pmod3$. Reference: elementary linear algebra (cyclic vectors). Paper: Lemma lem:euler ("the invariants form
the line spanned by $\sqrt{-3}\in\Z_\ell[\zeta_3]\simeq\End_{I_q}(V)$": the correct statement is $\End_{I_q}(V)=\Ql[\sigma]\simeq\Ql\otimes\Q(\zeta_3)$,
$\End_{I_q}(T)=\Zl[\sigma]$, important_notes.md point 12; types $\mathrm{III},\mathrm{III}^*$: the line $k\tau$); Chapter 6's 4.10 (i),
(ii) cites this item and adds the Frobenius action and the integral form.

**9.3 `prop:reps:cyclic-shapes`** (proposition and table; P for the linear algebra; the column "Kodaira types" is a
black box from Chapters 10 and 11). Let $K$ be a field and $g\in\SL_2(K)$ of finite order $m\in\{2,3,4,6\}$ with
$\operatorname{char}K\nmid m$. Then $g=-1$ if $m=2$; otherwise $g$ has distinct eigenvalues $\zeta,\zeta^{-1}$, $\zeta$ a primitive $m$-th root
of unity, and characteristic polynomial $\Phi_m$: $X^2+X+1$, $X^2+1$, $X^2-X+1$ for $m=3,4,6$; for $m=6$, $g=-\sigma$ with $\sigma=-g$
of order $3$. (Proof: $g^m=1$ with $X^m-1$ separable, so $g$ is diagonalisable over $\bar K$; $\det g=1$ pairs the eigenvalues;
$g\ne\pm1$ for $m\ge3$.) Fixed spaces, with 9.1 and 9.2 (checked over $\Q$ and over $\F_3$, Part 7):

| shape of the image of inertia | Kodaira types at $q\ge5$ (Ch. 10, 11) | $\dim V^I$ | $\dim(\ad V)^I$ | generator of $(\ad V)^I$ | action of $F$ ($FgF^{-1}=g^q$) on it | mod $3$: $\dim(T/3T)^I$ |
|-|-|-|-|-|-|-|
| trivial | $\mathrm I_0$ | 2 | 3 | all of $\ad V$ | eigenvalues $\alpha/\beta,1,\beta/\alpha$ (7.3(ii)) | 2 |
| $\{\pm1\}$ | $\mathrm I_0^*$ | 0 | 3 | all of $\ad V$ | as for the twist $E'$ (7.1(iii)) | 0 |
| unipotent $u\ne1$ (infinite) | $\mathrm I_n$, $n\ge1$ | 1 | 1 | $e$ | $q$ (9.1(iii)) | 1 if $3\nmid n$, 2 if $3\mid n$ |
| $\varepsilon u$, $\varepsilon$ ramified quadratic | $\mathrm I_n^*$ | 0 | 1 | $e$ | $q$ | 0 |
| order 3 | $\mathrm{IV}$, $\mathrm{IV}^*$ | 0 | 1 | $2\sigma+1$ | $\chi_{-3}(q)$ (Chapter 6, 4.10) | 1 (9.4(ii)) |
| order 4 | $\mathrm{III}$, $\mathrm{III}^*$ | 0 | 1 | $\tau$ | $\chi_{-4}(q)$ (Chapter 6, 4.10) | 0 |
| order 6 ($-\sigma$) | $\mathrm{II}$, $\mathrm{II}^*$ | 0 | 1 | $2\sigma+1$ | $\chi_{-3}(q)$ (Chapter 6, 4.10) | 0 |

The degree of $L_q(A_f,s)^{-1}$ is $\dim(\ad V)^I$ ($3,3,1,1,1,1,1$) and $\delta_q=\dim V^I$ ($2,0,1,0,0,0,0$). The eigenvalue $q$ in rows
3 and 4 is for the arithmetic normalisation; the geometric Frobenius gives $q^{-1}$, which is the paper's $1-q^{-1-s}$.
Reference: Serre-Tate and Kraus90 for the shapes (Chapters 10, 11). Paper: Lemma lem:euler (every row), the table of
Section 1, Definition def:terms ($\delta_p$), Lemma lem:IV, Remark rem:types (last column; the complete version is
important_notes.md point 22), Theorem thm:qual (a), (b), (c).

**9.4 `prop:reps:reduction-cyclic`** (proposition; P for (i) to (iv), R (forward) for (v)). Let $\ell$ be a prime,
$T=\Zl^2$, $g\in\SL_2(\Zl)$ of finite order $m\in\{2,3,4,6\}$, $\bar g$ its reduction modulo $\ell$. (i) If $\ell\nmid m$: $\bar g$ has
order $m$ (the kernel $1+\ell M_2(\Zl)$ of reduction is pro-$\ell$, Chapter 1, 7.4), $\Phi_m\bmod\ell$ is separable, and by 3.2(ii)
$(T/\ell T)^g=T^g/\ell T^g$ and $(\ad T/\ell)^g=(\ad T)^g/\ell$: invariants commute with reduction. (ii) $\ell=3$, $m=3$: $\bar g$ is a
nontrivial unipotent (reduction is injective on finite subgroups for $\ell$ odd, Chapter 1, 7.4(iii); an element of order $3$
of $\GL_2(\F_3)$ is unipotent, Chapter 1, 5.6(ii)); so $(T/3T)^g$ is a line although $T^g=0$, and $\dim T/3T-\dim(T/3T)^g=1$.
Invariants do not commute with reduction (Maschke fails, 3.3(a)); on $\ad T$ they still do here: $(\ad T)^g=\Z_3(2g+1)$ and
$2g+1\not\equiv0\pmod3$ spans $(\ad T/3)^g$. (iii) $\ell=3$, $m=6$: $\bar g=-\bar u$ with $\bar u$ a nontrivial unipotent, $(T/3T)^g=0$. (iv)
$\ell=3$, $m=4$: $\bar g$ has characteristic polynomial $X^2+1$, irreducible over $\F_3$, eigenvalues $\pm i\in\F_9$, $(T/3T)^g=0$; $m=2$:
$\bar g=-1$, $(T/3T)^g=0$. (v) (Chapter 6, 4.8 to 4.10(v).) $T$ is free of rank one over $\Zl[g]\simeq\Zl[X]/(\Phi_m)$, i.e. over
$\Zl[\zeta_3]$ ($m=3,6$) or $\Zl[i]$ ($m=4$), $\ell$ odd; for $\ell=3$, $m=3$: $T/3T\simeq\Z_3[\zeta_3]/(\pi^2)$, $\pi=1-\zeta_3$, which is the
paper's route to (ii). Reference: Chapter 1 and Chapter 6. Paper: Lemma lem:IV (the algebraic content: the image of $I_q$
in $\Aut(T_3E)$ cyclic of order $3$ with determinant $1$ gives a nontrivial unipotent mod $3$ and a fixed line; the paper's
notation slip is important_notes.md point 13), Remark rem:types (iii), (iv), Theorem thm:qual (a), (b) (Serre conductor
exponent $1$ for $\mathrm{IV}$, $\mathrm{IV}^*$), Lemma lem:euler ($\ell\ge5$ versus $\ell=3$).

### Section 10. Representations over $\Zl$: lattices, reduction, homothety

**10.1 `def:reps:lattice`** (definition and proposition; P). Conventions C7. A $G$-stable lattice $L\subset V$ gives
$\rho_L\colon G\to\GL(L)\simeq\GL_n(\mathcal{O})$, conjugate in $\GL_n(K)$ to $\rho$. (i) Any two lattices satisfy $\lambda^aL\subset L'\subset\lambda^{-b}L$
for some $a,b\ge0$. (ii) If $G$ is finite, $L=\sum_{g\in G}\rho(g)L_0$ is a $G$-stable lattice for any lattice $L_0$; more generally
whenever the stabiliser of $L_0$ has finite index in $G$ (the compact and continuous case is Chapter 5, galois:continuous-reps
(c)). (iii) If $L$ is stable, so are $\lambda^mL$, $L^\vee=\Hom_\mathcal{O}(L,\mathcal{O})\subset V^\vee$, $L\otimes\mathcal{O}(\chi)$ for $\chi\colon G\to\mathcal{O}^\times$, $\End_\mathcal{O}(L)$ and
$\ad L=\End_\mathcal{O}(L)\cap\ad V$; $\ad L$ is a direct summand of $\End_\mathcal{O}(L)$ (kernel of the split surjection $\tr$), so
$\ad L/\lambda^m\ad L=\ad(L/\lambda^mL)$. Reference: Serre, Abelian l-adic representations, Chapter I; Chapter 3 for lattices.
Paper: Section 1.1 ($T=T_\ell E\subset V=V_\ell E$), Section 4.2 ($M_{f,\lambda}$, $A=\ad T$), Lemma lem:h0 ($W^D[\ell^k]=\ad(T/\ell^k)(1)$).

**10.2 `prop:reps:reduction-ss`** (proposition; P). For a stable lattice $L$, $\bar\rho_L$ is the representation on $L/\lambda L$ over
$k$, and $\rho\bmod\lambda^m$ the one on $L/\lambda^mL$. (i) $\det(X-\bar\rho_L(g))$ is the reduction of $\det(X-\rho(g))\in\mathcal{O}[X]$, independent
of $L$. (ii) Hence (Brauer-Nesbitt 5.2) $\bar\rho_L^{ss}$ does not depend on $L$; it is written $\bar\rho^{ss}$. (iii) If $\bar\rho_L$ is
irreducible for one $L$ then $\bar\rho_{L'}\simeq\bar\rho_L$ for every stable $L'$ (5.3(ii) with $k'=k$). Reference: Serre, Abelian
l-adic representations, Chapter I; DDT, Section 1. Paper: Section 1.1 ($\bar\rho$), Lemma lem:old; Chapter 5's
galois:reduction-ss is this item plus continuity.

**10.3 `thm:reps:homothety`** (theorem, the homothety lemma, which PLAN.md calls Ribet's lemma; P). If $\bar\rho_L$ is
irreducible, every $G$-stable lattice $L'\subset V$ is homothetic to $L$: $L'=\lambda^mL$ for a unique $m\in\Z$. Proof: by 10.1(i)
replace $L'$ by $\lambda^{-m}L'$ with $m$ maximal such that $\lambda^{-m}L'\subset L$; then the image of $L'$ in $L/\lambda L$ is a nonzero
stable subspace, hence everything, so $L'+\lambda L=L$ and $L'=L$ by Nakayama (Chapter 3). Reference: standard (Serre,
Abelian l-adic representations, Chapter I; the converse direction is Ribet76, Section 2, see 10.4). Paper: Section 4.2
("$M_{f,\lambda}$ ... and $T_\ell E$ are homothetic when $\bar\rho$ is irreducible": applied to $M_{f,\lambda}$ and $T_\ell E^\vee$ inside
$V_\ell E^\vee$, important_notes.md point 26, then 7.7); Chapter 15 (comparison of $\rho_{f,\lambda}$ with $\rho_{E,\ell}$).

**10.4 `ex:reps:nonhomothetic`** (worked example and theorem; P for (i), R for (ii)). (i) Let $G\subset\GL_2(\Zl)$ be upper
triangular, containing $t=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. $L=\Zl e_1\oplus\Zl e_2$ and $L'=\Zl e_1\oplus\ell\Zl e_2$ are both stable and
not homothetic; $\bar\rho_L$ is a non-split extension (3.6: $\bar t$ is a nontrivial unipotent), while in the basis $e_1,\ell e_2$
of $L'$ the matrix of $g=\begin{pmatrix}a&b\\0&d\end{pmatrix}$ is $\begin{pmatrix}a&\ell b\\0&d\end{pmatrix}$, so $\bar\rho_{L'}$ is the direct sum
of the two characters: same semisimplification (10.2), different reductions. (Elliptic-curve analogue: two
$\ell$-isogenous curves, Chapters 9 and 11.) (ii) (Ribet's lemma.) If $V$ is irreducible of dimension $2$ and $\bar\rho^{ss}\simeq
\chi_1\oplus\chi_2$, then there is a stable lattice whose reduction is a non-split extension with sub-character $\chi_1$ (and
one with sub-character $\chi_2$). Reference: Ribet76, Section 2. Paper: background (the Eisenstein case: Section
sec:eis and Conjecture conj:eis concern reducible $\bar\rho$, where lattices are not unique up to homothety).

**10.5 `prop:reps:twist-length`** (proposition; P). Let $G$ be any group, $T$ free of rank $n$ over $\mathcal{O}$ with a $G$-action such
that $\bar T=T/\lambda T$ is absolutely irreducible, and $\chi\colon G\to\mathcal{O}^\times$ a character. For $m\ge1$ put
$M_m=\Hom_G(T/\lambda^m,(T/\lambda^m)(\chi))$. (i) $M_m$ is a cyclic $\mathcal{O}$-module, isomorphic to $\mathcal{O}/\lambda^j$ for some $j\le m$:
its $\lambda$-torsion is $\Hom_G(\bar T,\bar T(\bar\chi))$ (maps with image in $\lambda^{m-1}T/\lambda^mT\simeq\bar T$), of dimension at most one by
Schur 2.2, and an $\mathcal{O}$-module of finite length with $\lambda$-torsion of length at most one is cyclic (Chapter 3). (ii) An
element $\phi\in M_m$ with $\lambda^{m-1}\phi\ne0$ is an isomorphism $T/\lambda^m\simeq(T/\lambda^m)(\chi)$: $\lambda^{m-1}\phi\ne0$ means $\phi\bmod\lambda\ne0$, a
nonzero map of irreducible representations of the same dimension, hence surjective, and $\phi$ is surjective by
Nakayama, hence bijective (finite sets of the same size, or ranks). (iii) Let $X=\End_\mathcal{O}(T)(\chi)\otimes_\mathcal{O} K/\mathcal{O}$. Then
$X[\lambda^m]=\End(T/\lambda^m)(\chi)$, $X^G[\lambda^m]=M_m$, and $X^G$ is either $\mathcal{O}/\lambda^h$ with $h=\max\{m:T/\lambda^m\simeq(T/\lambda^m)(\chi)\}$, or
$K/\mathcal{O}$ when such isomorphisms exist for every $m$, in which case $T\simeq T(\chi)$ (an inverse limit of nonempty finite sets is
nonempty). (iv) If $n$ is invertible in $\mathcal{O}$ and $\bar\chi\ne1$, the same holds for $\ad T(\chi)\otimes K/\mathcal{O}$ (7.4(iii)). (v) If
$T/\lambda^m\simeq(T/\lambda^m)(\chi)$ then $\chi^n\equiv1\pmod{\lambda^m}$ on $G$ (determinants, 7.1(iv)). For $n=2$, $\mathcal{O}=\Zl$, $\ell$ odd, and $\chi$ with
$\chi(G)=\Zl^\times$ (the cyclotomic character, Chapter 5): $x^2\equiv1\pmod{\ell^m}$ for all $x\in\Zl^\times$ forces $\ell^m=3$ (Chapter 2,
5.5), so $h=0$ for $\ell\ge5$ and $h\le1$ for $\ell=3$. Reference: elementary. Paper: Lemma lem:h0 (the length $h_\ell(E)$ "is
the largest $k$ such that $\rho\bmod\ell^k\simeq(\rho\otimes\chi_\ell)\bmod\ell^k$" and its finiteness: (iii) and (v) give the corrected
statement of important_notes.md point 5, with absolute irreducibility as in point 10), Conjecture conj:euler,
Remark rem:ns, Section sec:anomaly ($h_3(E)\le1$ without the numerical check); Chapter 11 applies it with $G=G_\Q$,
$\chi=\chi_\ell$, Chapter 18 with the Pontryagin-dual language.

### Section 11. The mod $\ell$ world: a foretaste, and Dickson's list

**11.1 `rem:reps:mod-l-galois`** (remark with a dictionary; P for the translations, the Galois inputs cited). For
$\bar\rho\colon G_\Q\to\GL_2(\F_\ell)$ continuous (finite image, Chapter 5), $\ell$ odd: (i) complex conjugation $c$ has
$\bar\rho(c)^2=1$, $\det\bar\rho(c)=-1$ (Chapters 5, 9), so irreducible iff absolutely irreducible (2.4); (ii) the hypothesis of
Theorem thm:main concerns $\Res_H\bar\rho$ for the index-two subgroup $H=G_{\Q(\sqrt{\ell^*})}$, and by 6.6 it fails iff
$\bar\rho\simeq\bar\rho\otimes\chi_{\ell^*}$ iff $\bar\rho\otimes\bar\F_\ell$ is induced from $H$; (iii) Lemma lem:h0 concerns
$\bar\rho\simeq\bar\rho\otimes\bar\chi_\ell$ (7.4, 10.5), which needs $\bar\chi_\ell^2=1$, i.e. $\ell=3$, where $\bar\chi_3=\chi_{-3}=\det\bar\rho$ and 8.5
applies; for $\ell\ge5$ the two conditions differ (important_notes.md points 5 and 6). (iv) A dictionary table: $V$, $T$,
$\rho$, $\bar\rho$, $\rho\bmod\ell^k$, $A_f=\ad V$, $A=\ad T$, $T^D=\Hom(A,\Zl(1))\simeq A(1)$, $W=A\otimes\Ql/\Zl$, $W^D$, each with the item of
this chapter that constructs it. Paper: Theorem thm:main hypothesis, $S_f$, Lemma lem:h0, Proposition prop:ns, Section
1.3 (point 6).

**11.2 `thm:reps:dickson`** (theorem; R; restated from Chapter 1, 5.10 in projective form). Let $\ell$ be a prime and
$P\le\PGL_2(\F_\ell)$. If $\ell\mid\#P$, then $P$ contains $\PSL_2(\F_\ell)$ or fixes a point of $\PP^1(\F_\ell)$. If $\ell\nmid\#P$, then $P$
is cyclic, dihedral (including $V_4$), or isomorphic to $A_4$, $S_4$ or $A_5$. Representation-theoretic reading for an
absolutely irreducible $\bar\rho$ with projective image $P$ (6.7): cyclic is impossible; dihedral means induced from an
index-two subgroup; exceptional and "large" ($P\supseteq\PSL_2$) images are not induced. At $\ell=3$: $\GL_2(\F_3)\mapsto S_4$,
$N_{ns}(\F_3)\mapsto D_4$, $N_s(\F_3)\mapsto V_4$ (8.1); $N_s(\F_3)$ is not maximal (important_notes.md point 2). Reference: Serre72,
Section 2; Chapter 1, 5.10. Paper: background for Proposition prop:ns (Zywina's list), $S_f$.

________________________________________________________________________________

## 3. Section-by-section plan with target line counts

Line counts are lines of LaTeX, card excluded (PLAN.md Section 7.3: 1,000 to 2,200). Items per section: 4, 5, 7, 5,
3, 7, 7, 5, 4, 5, 2 (54 items).

| section | title | contents | target lines |
|-|-|-|-|
| (starred) | Core results at a glance | the card: every item of Part 2, stated as above, with tag and `\Cref` | (excluded) |
| (starred) | Where the paper uses this chapter | prop:ns; lem:h0 (with the corrected reading); lem:IV, rem:types, lem:euler; lem:old; Section 4.2, lem:fpr; lem:tamfactor; Section 1.1 and $\Sym$; hypothesis of thm:main, $S_f$, DDT 3.15; conj:euler, rem:ns, sec:anomaly | 40 |
| 1 | Representations over a field | conventions C1 to C9 as `convention` environments; 1.1 to 1.4; one sentence on RHB | 150 |
| 2 | Irreducibility, Schur's lemma, absolute irreducibility | 2.1 to 2.5; `paperlink` for the hypothesis of thm:main and for lem:h0 / lem:old (point 10) | 190 |
| 3 | Semisimplicity, Maschke, Jordan-Holder | 3.1 to 3.7; `paperlink` for lem:IV (3.3(a)), lem:old (3.6), prop:ns (3.7, point 1) | 200 |
| 4 | Characters in characteristic zero | 4.1 to 4.5; the tables of $D_4$ and $Q_8$ (`booktabs`); one paragraph on RHB; `warning` on traces in characteristic $p$ | 130 |
| 5 | Brauer-Nesbitt | 5.1 to 5.3, with the full proof of 5.2; `paperlink` for lem:old | 140 |
| 6 | Restriction, induction, Frobenius reciprocity, Mackey, Clifford | 6.1 to 6.7; `paperlink` for prop:ns and lem:h0 (induced over $\F_9$, point N1) | 240 |
| 7 | Twisting, the adjoint, the symmetric square, the trace form | 7.1 to 7.7; the $e,h,f$ formulas in a displayed array; `paperlink` for lem:h0, lem:tamfactor, Section 4.2 (point 26), Section 1.1 ($L_p(\Sym f,s)=L_p(A_f,s-1)$) | 210 |
| 8 | $\GL_2(\F_3)$ and its subgroups on $\F_3^2$ and $\F_9^2$ | 8.1 to 8.5; the table of 8.1 (`booktabs`, landscape-free: split into two tables if needed); `paperlink` for prop:ns, sec:anomaly | 200 |
| 9 | Unipotent elements and cyclic groups of order $2,3,4,6$ | 9.1 to 9.4; the shape table of 9.3; `paperlink` for lem:IV, rem:types, lem:euler | 180 |
| 10 | Representations over $\Zl$: lattices, reduction, homothety | 10.1 to 10.5; `paperlink` for Section 4.2 and lem:h0 ($h_\ell(E)$, point 5) | 200 |
| 11 | The mod $\ell$ world and Dickson's list | 11.1, 11.2; the dictionary table | 70 |
| 12 | Exercises | the 17 exercises of Part 4.2 | 130 |
| 13 | Notes and references | Serre (Linear representations; Abelian l-adic representations), Curtis-Reiner, Lang, Dummit-Foote, Serre72, Ribet76, DDT; which numbers were cited; RHB Chapter 29 | 40 |
| | **total** | | **2,120** |

________________________________________________________________________________

## 4. Coverage table and exercises

### 4.1 Coverage: PLAN.md scope, Section 6 map rows and paper hooks to line-up items

| PLAN.md scope item, Section 6 row, or paper hook | line-up items |
|-|-|
| representations of a finite group over a field (any characteristic) | 1.1, 1.2, 1.3, 1.4 |
| subrepresentations | 1.2, 2.1 |
| irreducibility | 2.1, 2.2 |
| absolute irreducibility (irreducible after extending scalars to the algebraic closure) | 2.3, 2.4, 2.5, 3.7 |
| Schur's lemma in both forms | 2.2 |
| characters and the character table in characteristic zero (brief, RHB connection) | 4.1, 4.2, 4.3, 4.4 |
| Maschke's theorem and its failure in characteristic dividing the group order | 3.2, 3.3, 9.4(ii) |
| semisimple versus non-semisimple modules | 3.1, 3.3, 3.6 |
| Jordan-Holder theorem and composition factors | 3.4, 3.5 |
| Brauer-Nesbitt (characteristic polynomials, not traces, in characteristic $\ell$) | 4.5, 5.1, 5.2, 5.3, 10.2 |
| restriction and induction | 6.1, 6.3 |
| Frobenius reciprocity | 6.2 |
| Mackey's criterion for irreducibility of induced representations | 6.4 |
| Clifford theory for index two (restriction irreducible or two conjugate characters; $\rho\simeq\rho\otimes\operatorname{sgn}$ iff induced) | 6.5, 6.6, 6.7 |
| twisting by one-dimensional characters | 7.1 |
| the trace of an isomorphism $\rho\to\rho\otimes\chi$ is zero when $\chi$ is nontrivial | 7.2, 7.4(iii) |
| the adjoint $\End V$ and $\ad V$ | 7.3, 7.7 |
| $\Sym$ and $\ad\rho=\Sym\rho\otimes\det^{-1}$ for $\dim2$ | 7.5 |
| $\Hom_G(V,W)=(V^\vee\otimes W)^G$; $H^0(\ad\rho\otimes\chi)$ as trace-zero $\Hom_G(\rho,\rho\otimes\chi)$ | 1.3, 7.4 |
| the trace form and the self-duality of $\ad$ for $\ell$ odd | 7.6 |
| representations of $\GL_2(\F_3)$ and its subgroups on $\F_3^2$ and $\F_9^2$; $C_4\subset N_s(\F_3)$ acts as $\psi\oplus\psi^{-1}$, $N_s(\F_3)$ as $\Ind\psi$ | 2.5, 3.7, 8.1, 8.2, 8.3, 8.4, 8.5 |
| unipotent and minus-unipotent elements and their fixed spaces | 9.1, 3.3(a), 9.4(ii), (iii) |
| cyclic groups of order $2,3,4,6$ on rank-two $\Zl$-lattices: eigenvalues, the $\Zl[\zeta_3]$-module structure, invariants on the adjoint | 9.2, 9.3, 9.4 |
| $G$-stable lattices, reduction mod $\ell$, homothety | 10.1, 10.2, 10.3, 10.4 |
| Ribet's lemma (irreducible reduction forces all stable lattices homothetic) | 10.3 (and the converse lemma of Ribet, 10.4(ii)) |
| irreducible versus absolutely irreducible for mod $\ell$ Galois representations (foretaste); the criterion via an element with distinct eigenvalues | 2.4, 11.1 |
| Dickson's list (stated, from Chapter 1) | 11.2, 6.7 |
| Section 6 row: $\rho_{E,\ell}$, $\bar\rho$, $T$, $V$, absolute irreducibility, restriction to $\Gal(\Qbar/\Q(\sqrt{\ell^*}))$ | 1.1, 2.3, 2.4, 6.6, 10.1, 10.2, 11.1 |
| Section 6 row: adjoint $\ad V$, $\Sym$, trace form, $A_f(1)=\Hom(A_f,\Zl(1))$ | 7.3, 7.5, 7.6, 7.7, 10.1(iii) |
| Section 6 row: $N_s$, 3Ns, $\GL_2(\F_3)$ and subgroups, orbits on lines | 8.1 to 8.5 (orbits: Chapter 1) |
| Section 6 row: $h_\ell(E)$, $\bar\rho\simeq\bar\rho\otimes\chi$ | 7.2, 7.4, 10.5, 6.6 |
| Section 6 row: induced representations, Frobenius reciprocity, characters of order $4$ | 6.1, 6.2, 6.4(c), 8.2 |
| Section 6 row: image of inertia on $T_\ell E$ at additive primes, unipotent elements, $\Z_3[\zeta_3]$ | 9.1, 9.3, 9.4 |
| Section 6 row: Chebotarev, Brauer-Nesbitt | 5.2, 5.3, 10.2 (Chebotarev: Chapter 5) |
| hook: Proposition prop:ns (induced representations, $\psi$ of order $4$, Frobenius reciprocity, $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$) | 1.4(ii), 2.5, 3.7, 6.2, 6.3, 6.4(c), 6.6, 6.7, 7.4, 8.1 to 8.5 |
| hook: Lemma lem:h0 (trace-zero isomorphisms, $\ad\bar\rho\otimes\chi$, the length $h_\ell$) | 1.3, 2.2, 2.4, 6.6, 7.1(iv), 7.2, 7.4, 10.5 |
| hook: Lemma lem:IV (eigenvalues of inertia, $\Z_3[\zeta_3]$, unipotent mod $3$) | 3.3(a), 9.1, 9.3, 9.4 |
| hook: Lemma lem:euler (invariants on the adjoint, the trace-zero line, $\End_{I_q}$) | 7.3(ii), 9.1(iii), 9.2, 9.3, 3.2(ii) |
| hook: Remark rem:types (minus unipotent, order $2$ and $4$ mod $3$) | 9.1(i), 9.3, 9.4(iii), (iv) |
| hook: Lemma lem:old (Brauer-Nesbitt plus Chebotarev gives $\bar\rho_h\simeq\bar\rho$; unique stable line) | 1.4, 3.6, 5.2, 5.3(ii), 10.2 |
| hook: Section 4.2 (homothetic lattices $M_{f,\lambda}$ and $T_\ell E$; $A=\ad T$; $T^D=\Hom(A,\Zl(1))\simeq A(1)$) | 7.6, 7.7, 10.1, 10.3 |
| hook: $A_f=\ad V$ and the trace form $A_f(1)=\Hom(A_f,\Zl(1))$ | 7.3, 7.6 |
| also: Lemma lem:tamfactor (basis $e,h,f$, adjoint action of $t$ and of $\rho(\Frob)$) | 7.3(iii), 9.1, 3.6 |
| also: Section 1.1 ($L_p(\Sym f,s)=L_p(A_f,s-1)$; eigenvalues $\alpha/\beta,1,\beta/\alpha$) | 7.3(ii), 7.5 |
| also: proof of Theorem thm:main and Theorem thm:quant ($\ad T$ unchanged by twists) | 7.1(iii), 7.7 |
| also: Conjecture conj:euler, Remark rem:ns, Section sec:anomaly ($h_\ell(E)$, image 3Ns) | 8.2, 8.5, 10.5 |
| also: the hypothesis of Theorem thm:main, Theorem thm:qual, DDT 3.15, $S_f$ | 2.3, 2.4, 6.6, 6.7, 8.5, 11.1 |

### 4.2 Exercises (Section 12 of the chapter), graded from easy to harder

1. Show that $C_4=\langle J\rangle$ acting on $\F_3^2$ is irreducible but not absolutely irreducible, that its commutant is a field
   with $9$ elements, and decompose $\F_9^2$ into eigenlines.
2. Prove that every absolutely irreducible representation of a finite abelian group is one-dimensional, and give an
   irreducible two-dimensional representation of $C_8$ over $\F_3$.
3. Show that the standard representation of $\mathrm U=\langle u\rangle$ on $\F_3^2$ is indecomposable but not irreducible, and that
   $\F_p[C_p]$ is uniserial. Why does this not contradict Maschke's theorem?
4. Give two non-isomorphic semisimple representations of $C_2$ over $\F_3$ with the same trace function. Show that for
   two-dimensional representations with the same determinant in characteristic $\ne2$, traces suffice.
5. Check the paper's claim (Proposition prop:ns) that the determinant-one subgroup $C_4$ of $N_s(\F_3)$ acts on $\F_9^2$ as
   $\psi\oplus\psi^{-1}$ with $\psi$ of order $4$, and that the standard representation of $N_s(\F_3)$ over $\F_9$ is isomorphic to
   $\Ind_{C_4}^{N_s}\psi$: find the basis $(v,\sigma v)$ explicitly. Show that over $\F_3$ it is not induced from a character of $C_4$.
6. Check the paper's claim (Proposition prop:ns) that $Q_8$ and $\SL_2(\F_3)$ act absolutely irreducibly on $\F_3^2$, by
   Maschke's theorem (3.7) rather than by commutators; explain why "non-abelian and faithful" is not enough for the
   Borel subgroup $\mathrm B(\F_3)$.
7. Show that the standard representation of $N_s(\F_3)$ is isomorphic to its twist by each of the three nontrivial
   characters of $N_s(\F_3)/\{\pm1\}$, with intertwiners $J$, $\sigma$, $w$. Show that the standard representation of
   $N_{ns}(\F_3)$ is induced from $C_{ns}(\F_3)$ but not isomorphic to its twist by $\det$.
8. Check the paper's claim (Lemma lem:h0) that an isomorphism $\phi\colon\bar\rho\to\bar\rho\otimes\chi_{-3}$ has trace $0$; show more
   generally that $(\ad V\otimes\chi)^G=\Hom_G(V,V\otimes\chi)$ for every nontrivial $\chi$ when $\dim V$ is invertible.
9. Let $H\le G$ have index $2$ and $V$ be absolutely irreducible of dimension $2$, $\operatorname{char}k\ne2$. Prove directly that
   $V\simeq V\otimes\chi_H$ iff $\tr\rho(g)=0$ for all $g\notin H$, and deduce that the standard representation of $\GL_2(\F_3)$ is not
   isomorphic to its twist by $\det$.
10. Prove $\ad V\simeq\Sym V\otimes\det^{-1}$ for $\dim V=2$ by the explicit map $\Xi$ of 7.5, and show that over $\Z$ the image of
    $\Sym\Z^2$ has index $4$ in $\ad\Z^2$. Deduce the eigenvalues $\alpha/\beta$, $1$, $\beta/\alpha$ from $\alpha^2,\alpha\beta,\beta^2$.
11. Compute the Gram matrix of the trace form on $\ad\Zl^2$ in the basis $e,h,f$, and check the paper's identification
    $T^D=\Hom(A,\Zl(1))\simeq A(1)$ (Section 4.2) for $\ell$ odd. What goes wrong for $\ell=2$?
12. Check the formulas of Lemma lem:tamfactor: for $t=1+n'e$, $(t-1)e=0$, $(t-1)h=-2n'e$, $(t-1)f=n'h-n'^2e$; and for
    $F=\begin{pmatrix}\varepsilon q&c'\\0&\varepsilon\end{pmatrix}$ with $\varepsilon=\pm1$, $FeF^{-1}=qe$, $FhF^{-1}=h-2c'\varepsilon e$.
13. For each of $g=-1$, $g$ of order $3$, $4$, $6$ in $\SL_2(\Z)$, $g=u$ and $g=-u$, compute $\dim V^g$ and $\dim(\ad V)^g$ over $\Q$ and
    over $\F_3$, and check the paper's claims in Lemma lem:IV and Remark rem:types about $E[3]^{I_q}$.
14. Let $FuF^{-1}=u^q$ with $u\ne1$ unipotent. Show that $F$ acts on $(\ad V)^u$ by $q$, and explain why the paper's
    factor $1-q^{-1-s}$ at a multiplicative prime requires the geometric Frobenius (important_notes.md point 11).
15. Show that for a finite group of order prime to $\ell$ invariants commute with reduction modulo $\ell$, and that this
    fails for $g\in\SL_2(\Z_3)$ of order $3$ (Lemma lem:IV), although it holds for the invariants of $\ad$.
16. In $\Ql^2$ with the upper triangular group, exhibit two stable lattices that are not homothetic and whose reductions
    are non-isomorphic but have the same semisimplification. Prove the homothety lemma 10.3.
17. Let $T$ be a free $\Zl$-module of rank $2$ with an action of $G$ such that $T/\ell T$ is absolutely irreducible, and
    $\chi\colon G\to\Zl^\times$ surjective. Show that $\Hom_G(T/\ell^m,(T/\ell^m)(\chi))$ is cyclic and that the length of
    $H^0(G,\ad T(\chi)\otimes\Ql/\Zl)$ is at most $1$, and is $0$ unless $\ell=3$ (the corrected Lemma lem:h0, important_notes.md
    point 5).

________________________________________________________________________________

## 5. Dependencies and forward pointers

Results from other chapters used here (by chapter label only):
* Chapter 1 (`ch:groups`): the standard models and the class and subgroup tables of $\GL_2(\F_3)$ (its 6.1 to 6.6), the
  three images (its 6.7), projective images (its 6.11), unipotent and minus-unipotent elements (its 5.6), Borel
  subgroups and the commutator lemma (its 5.5, 5.7), Cartan subgroups and normalisers (its 5.8, 5.9), $1+\ell M_2(\Zl)$
  pro-$\ell$ and torsion-free for $\ell$ odd (its 7.4), index-two subgroups (its 1.6), $D_4$, $Q_8$, $SD_{16}$ (its 2.4 to 2.6),
  Dickson (its 5.10). Chapter 4 must use, not redo, these.
* Chapter 2 (`ch:rings`): $\F_9=\F_3[i]$, finite fields and their Frobenius, characters of finite abelian groups and
  orthogonality (its 10.2), cyclotomic polynomials $\Phi_m$, $a^2\equiv1\pmod{\ell^k}$ (its 5.5).
* Chapter 3 (`ch:modules`): modules, $\Hom$, $\otimes$, exact sequences; Nakayama; DVRs, $\Zl$, lattices (finitely generated
  torsion-free modules over a DVR are free); cyclicity criterion for finite-length modules over a DVR; saturated
  submodules and direct summands; Gram determinants and perfect pairings; $\Ql/\Zl$ and $T\otimes\Ql/\Zl$; Pontryagin duality
  (only in remarks).
* Background (PLAN.md Section 2): linear algebra (eigenvalues, diagonalisation, cyclic vectors, Vandermonde), RHB's
  representation theory of finite groups (Chapter 29 of RHB, 3rd edition).

Black boxes imported from later chapters (stated with a forward `\Cref`, never used in the proof of a numbered result
of this chapter): Galois representations, continuity, complex conjugation, $\det\bar\rho_{E,\ell}=\bar\chi_\ell$ (Chapters 5, 9,
11), the assignment of inertia shapes to Kodaira types (Kraus; Chapters 10, 11), the Frobenius action $\chi_{-3}(q)$,
$\chi_{-4}(q)$ on the invariant lines and the $\Zl[\zeta_3]$-module structure (Chapter 6), Tate twists and $L$-factors
(Chapters 18, 19). They appear only in `paperlink` environments, in the "Kodaira types" and "action of $F$" columns
of the table of 9.3, in 9.4(v), 7.5(iii) and 11.1.

Forward pointers (chapters that use this one):
* Chapter 5 (`ch:galois`): 2.4 (complex conjugation criterion), 5.2 and 5.3 (Chebotarev plus Brauer-Nesbitt,
  congruent $a_p$), 6.6 (galois:index-two-restriction), 7.1(iv) and 7.2 (galois:twist), 10.1 to 10.3
  (galois:reduction-ss).
* Chapter 6 (`ch:ant`): 9.2 (its 4.10 (i), (ii)), 6.1 trace formula and 7.2 (its 6.4, 6.5), 5.2 (via Chapter 5).
* Chapter 7 (`ch:local`): 3.3(c) and 9.1 (unipotent tame inertia, Weil-Deligne shapes), 9.3 (finite inertia of order
  $2,3,4,6$).
* Chapter 9 (`ch:ellcurves`): twists $\rho\otimes\chi_d$ (7.1); $V^\vee\simeq V\otimes\det^{-1}$ and the Weil pairing (1.2).
* Chapter 11 (`ch:galrep`): 2.4, 3.6, 6.6, 7.4, 8.5 (Proposition prop:ns), 9.1, 9.3, 9.4 (Lemma lem:IV, Remark rem:types),
  10.5 (Lemma lem:h0), 11.1.
* Chapter 13 (`ch:hecke`): twisting (7.1) on the Galois side of the Atkin-Li theorem (motivation only).
* Chapter 15 (`ch:modgalrep`): 3.6 (unique stable line in Lemma lem:old), 5.3 (Lemma lem:old), 10.2, 10.3, 7.7
  ($M_{f,\lambda}$ versus $T_\ell E$).
* Chapter 16 (`ch:cohomology`): 1.3, 7.3 ($E_{ij}$, the basis $e,h,f$, the conjugation action), 9.1, 3.6 (extensions and
  cocycles), 3.2(ii) (cohomology of groups of order prime to $\ell$ is the same averaging).
* Chapter 17 (`ch:galcoh`): 7.6 (duals), 3.2(ii).
* Chapter 18 (`ch:blochkato`): 7.6 (self-duality of $\ad$, $T^D\simeq A(1)$), 7.7, 10.1(iii), 10.5 ($h_\ell(E)$).
* Chapter 19 (`ch:lfunctions`): 7.3(ii) (eigenvalues of $\ad$), 7.5 ($\ad\simeq\Sym\otimes\det^{-1}$ and the shift
  $L(\Sym f,s)=L(A_f,s-1)$), 9.3 (degrees of the local factors).
* Chapter 20 (`ch:congruence`): 7.7 and 10.3 (lattices $M_{f,\lambda}$).
* Chapters 21, 22 (`ch:paper`, `ch:computation`): 8.1 to 8.5 (the `ns3` test, image 3Ns), 9.3 (Lemma lem:euler), 10.5.

________________________________________________________________________________

## 6. Notes for the writer

Conventions to fix (Section 1 of the chapter, as `convention` environments): C1 to C9 of Part 1. In addition:
* Macros: `\ad` is $\operatorname{ad}^0$ and `\Sym` is $\operatorname{Sym}^2$ (both already carry the superscript). Write the full
  adjoint as `\End(V)` or `\Ad V`. There is no `\O` macro: write `\mathcal{O}`. `\Ind`, `\Res`, `\tr`, `\Hom`, `\End`, `\GL`,
  `\SL`, `\PGL` exist. `\Res` is restriction here, never the resultant.
* Use the paper's basis $e,h,f$ of $\ad V$ (C3) and the matrices of C6; keep the paper's $\sigma$ for the order-$3$ element of
  Section 9 and rename Chapter 1's $\operatorname{diag}(1,-1)$ there (C6).
* Characters: $\chi$, $\psi$, $\theta$ for one-dimensional representations; $\tr_V$ for trace functions. The paper's
  $\chi_\ell$ (cyclotomic) and $\chi_q$ (quadratic; the book's $\chi_{q^*}$, decision D3) appear only in `paperlink`s (Chapter 2, C5, and important_notes.md
  point 32).
* Rigour tags on the card exactly as in Part 2. Theorem numbers are cited only where marked as sure: Serre, Linear
  representations, Theorem 1 (Maschke), Proposition 4 (Schur), Theorem 13 (Frobenius reciprocity) were recalled from
  memory and should be checked, otherwise cite sections (1.3, 2.2, 7.2). Curtis-Reiner and Lang are cited by section
  only. `CurtisReiner` is not in `refs.bib`: add it to `bib/ch04.bib` (Curtis and Reiner, Representation theory of finite
  groups and associative algebras, Interscience 1962). RHB's chapter number (29 in the 3rd edition) should be checked.

Pitfalls:
* **Traces versus characteristic polynomials.** In characteristic $\ell$, Brauer-Nesbitt needs characteristic polynomials
  (4.5); for $\dim2$ with equal determinants (the paper's situation, $\det=\bar\chi_\ell$) traces suffice (5.3(i)). Say both.
* **Irreducible versus absolutely irreducible.** Every place where the paper says "irreducible" and then uses Schur in
  the form $\End=k$, Clifford theory, or Brauer-Nesbitt over a larger field, absolute irreducibility is what is needed
  (important_notes.md point 10). For $\bar\rho_{E,\ell}$ the two coincide by 2.4 (complex conjugation). The example to show:
  $C_4$ on $\F_3^2$ (2.5), and 5.3(ii)'s counterexample.
* **"Induced" over which field.** $\bar\rho_{E,3}$ with image $N_s(\F_3)$ is induced from $G_{\Q(\sqrt{-3})}$ only after extending
  scalars to $\F_9$; over $\F_3$ its restriction to $G_{\Q(\sqrt{-3})}$ is irreducible (8.2(ii); Part 8, point N1). The twist
  isomorphism $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ does hold over $\F_3$ (1.4(ii)).
* **Absolute irreducibility of $Q_8$ and $\SL_2(\F_3)$** (important_notes.md point 1). Give both proofs: Chapter 1's
  commutator lemma and 3.7 (non-abelian of order prime to $3$, then containment). Do not "correct" the paper in the
  text; supply the step in a `paperlink`.
* **$N_s(\F_3)$ itself is absolutely irreducible**; only its determinant-one subgroup is not. Never write "the image
  $N_s(\F_3)$ is reducible". Its representation is induced in three ways (projective image $V_4$), and the representation
  of $N_{ns}(\F_3)$ is also induced (from $C_{ns}$); the hypothesis of Theorem thm:main excludes only "induced from
  $\Q(\sqrt{\ell^*})$" (6.7, 8.3).
* **Maschke over $\Zl$.** Invariants commute with reduction only when the group order is prime to $\ell$ (3.2(ii)); the
  paper's Lemma lem:IV is exactly the failure at $\ell=3$ (9.4(ii)). The elementary proof of 9.4(ii) (Chapter 1, 7.4(iii)
  and 5.6(ii)) does not need $\Z_3[\zeta_3]$; give it, and point to Chapter 6 for the paper's route.
* **Mackey in characteristic $p$.** The general criterion 6.4(b) is a characteristic-$0$ statement ($\End=k$ does not imply
  irreducible without semisimplicity, 3.3(d)); only the index-two case 6.4(c) is needed and it holds in every
  characteristic for absolutely irreducible $W$.
* **Clifford 6.6 needs $\operatorname{char}k\ne2$** (so that $\chi_H\ne1$ and $\Ind\mathbf1=\mathbf1\oplus\chi_H$), and absolute irreducibility
  of $V$.
* **The splitting $\End V=k\oplus\ad V$, the isomorphism $\ad\simeq\Sym\otimes\det^{-1}$ and the perfectness of the trace form on
  $\ad$ all need $2$ invertible** ($\ell$ odd); give the index-$4$ and index-$2$ computations over $\Z$ and $\Z_2$ (7.5, 7.6).
* **Twist direction for $\Sym$.** $\Sym V_\ell E\simeq\ad V(1)$ but the classical $L(\Sym f,s)$ is that of $\Sym(V^\vee)\simeq\ad V(-1)$,
  whence $L_p(\Sym f,s)=L_p(A_f,s-1)$. Keep 7.5(iii) as a remark with pointers; the $L$-factor bookkeeping is Chapter 19's.
  (Cross-outline note: Chapter 21's item C2 says that on $V_\ell E$ the geometric Frobenius has eigenvalues $\alpha,\beta$; on
  $V_\ell E$ it is the arithmetic Frobenius that has eigenvalues $\alpha,\beta$, and the geometric one has $\alpha^{-1},\beta^{-1}$; the
  statement is right for $V_\ell E^\vee=H^1$. This does not affect any number in the paper.)
* **Frobenius conventions** (important_notes.md point 11). This chapter never uses Frobenius; 9.1(iii) and 9.3 state the
  eigenvalue for an abstract $F$ with $FgF^{-1}=g^q$ (arithmetic) and note that $F^{-1}$ (geometric) gives the inverse.
* **Name of 10.3.** PLAN.md calls the homothety statement "Ribet's lemma"; in the literature Ribet's lemma usually means
  the converse construction 10.4(ii). Call 10.3 "the homothety lemma" and mention both names once.
* **Dual lattices** (important_notes.md point 26). $M_{f,\lambda}$ of DFG04 sits in $H^1$, dual to the Tate module; 10.3 gives
  homothety with $T_\ell E^\vee$, and 7.7 identifies the adjoints. State 7.7(iv) in exactly this form.
* **$h_\ell(E)$** (important_notes.md point 5). Prove 10.5 for an abstract group and character; do not reproduce the
  paper's CM sentence. The application to $G_\Q$ and $\chi_\ell$ ($h_\ell=0$ for $\ell\ge5$, $h_3\le1$) is one line with Chapter 5's
  $\chi_\ell(G_\Q)=\Zl^\times$ and Chapter 2's 5.5.
* **$\End_{I_q}$** (important_notes.md point 12): state 9.2 for $V$ with field coefficients and point to Chapter 6 for $T$
  and $\Zl[\zeta_3]$; $\Zl[\zeta_3]$ is not a domain for $\ell\equiv1\pmod3$.
* Typography (PLAN.md 7.2): no dash ligatures; "Jordan-Holder" without diacritics in the source is acceptable, or
  `H\"older`; tables with `booktabs`; the wide table of 8.1 may be split into two.

What to leave to other chapters:
* Chapter 1: all group theory of $\GL_2(\F_3)$ (subgroups, orders, orbits on lines, the three images, commutators,
  maximality), Dickson's proof; this chapter only cites.
* Chapter 3: modules, Nakayama, DVRs, lattices, Gram determinants, Pontryagin duality, lengths over a DVR.
* Chapter 5: continuity, profinite groups, existence of lattices for compact images, Chebotarev, complex conjugation,
  the cyclotomic character and the determinant argument for $\chi_\ell$, the field $\Q(\sqrt{\ell^*})$.
* Chapter 6: $\Zl[\zeta_3]$, $\Zl[i]$ as rings, freeness of $T$ over $\Zl[\sigma]$, the Frobenius action $\chi_{-3}(q)$, $\chi_{-4}(q)$
  on the invariant lines, the twist detector at inert primes, CM.
* Chapter 11: Lemma lem:IV, Remark rem:types, Proposition prop:ns, Lemma lem:h0 as statements about elliptic curves, the
  Kodaira-type to inertia-shape dictionary (with Chapter 10, Kraus), the Serre conductor.
* Chapters 16 to 19: cohomology ($H^1$ of cyclic groups, extensions as $H^1$), Tate twists, Bloch-Kato, $L$-factors.

How the important_notes.md points in this chapter's area are handled:
* **Point 1** (prop:ns, "non-abelian and faithful"): 3.7 gives the Maschke proof for $Q_8$ (order prime to $3$) and
  containment for $\SL_2(\F_3)$; the Borel counterexample is 3.7(iv); Exercise 6. Chapter 1's 5.7 is cited as the
  alternative.
* **Point 5** (lem:h0, finiteness and $h_\ell\le1$): 10.5 (cyclicity, the length as the largest $m$ with $T/\ell^m\simeq(T/\ell^m)(\chi)$,
  the determinant constraint); Exercise 17; the Galois specialisation is one sentence pointing to Chapters 5 and 11.
* **Point 10** (lem:old and lem:h0, "irreducible" should be "absolutely irreducible"): 2.4 (distinct eigenvalues), 5.3(ii)
  (with the $C_4$ counterexample showing why), 6.6 (Clifford needs absolute irreducibility), 1.4 (common finite field).
* **Point 12** (lem:euler, $\End_{I_q}(V)$ versus $\End_{I_q}(T)$): 9.2 states the commutant over a field, with the
  remark that it is a field iff $\ell\not\equiv1\pmod3$; 9.4(v) points to Chapter 6 for the integral statement.
* **Point 26** (Section 4.2, $M_{f,\lambda}$ homothetic to the dual of $T_\ell E$): 7.7 and 10.3; the `paperlink` of Section 10 says
  "homothetic to the dual of $T_\ell E$; the adjoints are canonically identified".
* Also touched: point 11 (9.1(iii), 9.3: arithmetic versus geometric eigenvalue), point 13 (9.4: write $\Z_3[X]/(X^2+X+1)$),
  point 22 (9.3 last column and 9.4: the complete mod-$3$ picture), point 2 (11.2: $N_s(\F_3)$ not maximal), point 6 (11.1(iii)),
  and the new points N1, N2 of Part 8.

________________________________________________________________________________

## 7. Verification log (computations done for this outline)

All scripts were short Python/sympy programs in `/tmp/ch04` (`gl23.py`, `sym.py`).
* $\GL_2(\F_3)$ enumerated (48 elements) with $\F_9=\F_3[i]$ arithmetic; the subgroups $\GL_2$, $\SL_2$, $N_{ns}$, $Q_8$, $N_s$, $C_4$, $C_{ns}$,
  $C_s$, $\mathrm B$, $\mathrm U$, $\{\pm1\}\times\mathrm U$ generated from the models C6 (orders $48,24,16,8,8,4,8,4,12,3,6$). For each: the number of
  stable lines over $\F_3$ and over $\F_9$ ($0,0$ for $\GL_2,\SL_2,N_{ns},Q_8,N_s$; $0,2$ for $C_4$, $C_{ns}$; $2,2$ for $C_s$; $1,1$ for
  $\mathrm B$, $\mathrm U$, $\{\pm1\}\times\mathrm U$); $\dim\End_H$, $\dim(\ad\rho)^H$, $\dim\Hom_H(\rho,\rho\otimes\det)$ and its trace-zero part, the existence of
  an invertible intertwiner $\rho\to\rho\otimes\det$, and the order of the projective image: the table of 8.1.
* $N_s(\F_3)$: $\rho\simeq\rho\otimes\chi$ for the three characters with kernels $C_4$, $C_s$, $\{\pm1,\pm w\}$ (invertible intertwiners found);
  with $X=[v\,|\,\sigma v]$, $v=(1,-i)^t$: $X^{-1}JX=\operatorname{diag}(i,-i)$, $X^{-1}\sigma X=w$ (8.2(ii)); the elements of determinant $-1$ of
  $N_s(\F_3)$ all have trace $0$, those of $N_{ns}(\F_3)$ and $\GL_2(\F_3)$ have traces $0,\pm1$, the nonzero ones exactly the
  elements of order $8$. $N_{ns}(\F_3)\simeq N_{ns}\otimes\chi_{ns}$ for the character with kernel $C_{ns}$ (invertible intertwiner
  found).
* Symbolic (sympy): $\Ad(g)\Xi=\Xi\,\Sym(g)\det(g)^{-1}$ for general $g$ with $\Xi(e_1^2)=-2e$, $\Xi(e_1e_2)=h$, $\Xi(e_2^2)=2f$; the Gram
  matrix of $\tr(xy)$ on $e,h,f$ and its determinant $-2$; $(t-1)e=0$, $(t-1)h=-2n'e$, $(t-1)f=n'h-n'^2e$ for $t=\begin{pmatrix}1&n'\\0&1\end{pmatrix}$;
  $\Ad\begin{pmatrix}\varepsilon q&c'\\0&\varepsilon\end{pmatrix}$ on $e,h,f$ (7.3(iii)); $\Ad\operatorname{diag}(x,y)=\operatorname{diag}(x/y,1,y/x)$.
* For $g\in\{-1,\begin{pmatrix}0&-1\\1&-1\end{pmatrix},J,\begin{pmatrix}1&-1\\1&0\end{pmatrix},u,-u\}$: orders $2,3,4,6,\infty,\infty$, characteristic polynomials
  $(X+1)^2$, $X^2+X+1$, $X^2+1$, $X^2-X+1$, $(X-1)^2$, $(X+1)^2$; $\dim V^g=0,0,0,0,1,0$ and $\dim(\ad V)^g=3,1,1,1,1,1$ over $\Q$, with
  generators $2\sigma+1$ (orders $3$ and $6$, up to a factor $2$), $J$ (order $4$), $e$ ($\pm u$); over $\F_3$: $\dim V^g=0,1,0,0,1,0$ and
  $\dim(\ad V)^g=3,1,1,1,1,1$ (the table of 9.3 and 9.4).
* By hand: the Brauer-Nesbitt example 4.5; $\Xi(e_1^2)$, $\Xi(e_1e_2)$, $\Xi(e_2^2)$ from the formula of 7.5; the matrix of $\Ind\psi$ in 6.1;
  the intertwiners $J$, $\sigma$, $w$ of 8.2 (via $J\sigma=-\sigma J$, $wJ=-Jw$, $w\sigma=-\sigma w$); $\theta(a)=1+i$, $\theta(a)^3=1-i$ (8.3); the
  determinant obstruction $x^2\equiv1\pmod{\ell^m}$ for all units only for $\ell^m=3$ ($\ell$ odd).

________________________________________________________________________________

## 8. Points for important_notes.md

New points in this chapter's area, not among the 32 already recorded. Both are expository; neither changes a result.

**N1. Proposition prop:ns, proof ("$\bar\rho\simeq\Ind\psi$"), and Lemma lem:h0, proof ("induced from
$\Gal(\Qbar/\Q(\sqrt{-3}))$"): the induction lives over $\F_9$, not over $\F_3$.**
Location: Section 5, proof of Proposition prop:ns, third case; Section 4.2, proof of Lemma lem:h0, the sentence "For
$\ell=3$ and $\bar\rho$ irreducible, $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ holds if and only if $\bar\rho$ is induced from
$\Gal(\Qbar/\Q(\sqrt{-3}))$". Problem: $\psi$ takes values in $\F_9^\times$ (order $4$), and in the $N_s(\F_3)$ case the restriction of
$\bar\rho$ to $G_{\Q(\sqrt{-3})}$ is irreducible over $\F_3$ (its image $C_4=\langle J\rangle$ has no stable $\F_3$-line, $X^2+1$ being
irreducible over $\F_3$). So $\bar\rho$ is not induced from a character of $G_{\Q(\sqrt{-3})}$ over $\F_3$; only
$\bar\rho\otimes\F_9\simeq\Ind\psi$ holds. Fix: write "$\bar\rho\otimes\F_9\simeq\Ind\psi$ by Frobenius reciprocity, so
$\bar\rho\otimes\F_9\simeq(\bar\rho\otimes\chi_{-3})\otimes\F_9$, hence $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ (a $G_\Q$-map between absolutely
irreducible representations defined over $\F_3$ exists over $\F_3$ as soon as it exists over $\F_9$)", and in Lemma lem:h0
"induced from $\Gal(\Qbar/\Q(\sqrt{-3}))$ after extension of scalars to $\bar\F_3$". Confidence: high (the $\F_3$-irreducibility of
$C_4$ and the explicit isomorphism over $\F_9$ were checked by computer, Part 7). Importance: low (expository; the
conclusion $\bar\rho\simeq\bar\rho\otimes\chi_{-3}$ over $\F_3$ is correct).

**N2. Lemma lem:euler, proof, types $\mathrm{III},\mathrm{III}^*$: "the invariant line of $\ad V$ is spanned by the diagonal
element".** Location: Section 2, proof of Lemma lem:euler. Problem: for $\ell\equiv3\pmod4$ the generator $\tau$ of the image of
inertia (eigenvalues $\pm i$) has no eigenvectors over $\Ql$, so there is no "diagonal element" in $\ad V$ over $\Ql$; the
invariant line of $\ad V$ is $\Ql\tau$ (9.2), which is diagonal, equal to $i\operatorname{diag}(1,-1)$, only in an eigenbasis over
$\Ql(i)$. The Frobenius eigenvalue on the line is $\chi_{-4}(q)$ either way ($F\tau F^{-1}=\tau^q=\chi_{-4}(q)\tau$), so nothing changes.
This is the order-$4$ companion of important_notes.md point 12. Fix: "the invariant line of $\ad V$ is spanned by $\tau$
itself (diagonal in an eigenbasis over $\Ql(i)$), on which Frobenius acts by $\chi_{-4}(q)$, since $\tau^q=\chi_{-4}(q)\tau$".
Confidence: high. Importance: low.

No other new problem was found in this chapter's area. Checked and found correct: the trace-zero computation in
Lemma lem:h0; "a nonzero such map is an isomorphism" (given absolute irreducibility, point 10); the list of
determinant-one subgroups and the orbit statement in Proposition prop:ns (Chapter 1); $\psi$ of order $4$ and
$\psi^{-1}=\psi^\sigma$; "the third is abelian, hence absolutely reducible"; the $e,h,f$ formulas and the action of $\rho(\Frob)$ on
$e,h$ in Lemma lem:tamfactor (with $\varepsilon^{-1}=\varepsilon$); "$T^D=\Hom(A,\Zl(1))\simeq A(1)$ via the trace form" (needs $\ell$ odd,
which the paper assumes); "$\ad T$ is unchanged by the twist"; "a non-split extension of two characters has a unique
stable line" in Lemma lem:old; the eigenvalues $\zeta_3^{\pm1}$ and the $\Z_3[\zeta_3]$ argument of Lemma lem:IV (modulo point 13);
"$L_p(\Sym f,s)=L_p(A_f,s-1)$" against 7.5(iii).
