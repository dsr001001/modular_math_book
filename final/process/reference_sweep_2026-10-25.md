# Reference sweep of the note (25 October 2026)

Scope: the 51 works cited in final/paper/note.tex (143 citations, 74 with a pinpoint). For each work, the bibliographic data were checked against an authoritative source (journal or DOI page, numdam, arXiv, author pages), and each pinpoint against the text where a copy was reachable (local PDFs of DFG04, Flach92, Kenku, PollackWeston, RibetTakahashi97, Takahashi01; open-access texts online). Done by four AI agents in parallel; fixes applied only where a source was opened. Paywalled or blocked texts are listed as unverified below, not guessed.

## Changes made (note, book, claim ledger)
- DFG04: "(5), Proposition 1.3" (full-level curve and the GL_2(Z/N) action) replaced by Sections 1.2.1, 1.3.2. "None of this depends on N" restricted to the c and ! lattices (DFG 1.4.1, p. 679). Proposition prop:integral: the l-adic identification is stated for l not dividing 2M^Sigma, the primes at which DFG define the lambda-adic realisation; the Betti form holds for every l. Theorem dfg14 states l not dividing 2M explicitly. Hecke action cited to Section 1.6.1. DOI added; bib note that the numbering is that of the Annales version (the 2025 repost arXiv:2512.02348 is numbered differently). All other 50 DFG locators confirmed against the published text (pages 666-723).
- KimOta: Theorem 1.1 and Definition 2.12 replaced by Theorem 1.3 and Definition 1.15 (arXiv v4 numbering); DOI.
- ARS12: r_E is defined in Section 1 and the perfect pairing is stated in Section 4.1 of the authors' version (Theorem 2.2 and Table 1 confirmed there); bib note says which version is meant; editors and DOI added. The exponent N^{2+eps} is not in ARS: the sentence now speaks of "a suitable polynomial bound" (Frey, Murty).
- Hida81 Theorem 5.1 added as the source of the exact normalisation of <f,f> (it is what DFG Lemma 2.12 cites); title corrected to "Congruences of cusp forms ...".
- AtkinLi78: lemma (iii) cites "Theorem 3.1 and p. 228" (the case q not dividing M).
- Zywina15: pinpoint Theorem 1.2, Propositions 1.14 and 1.16.
- PARI: version 2.15.4 (2023), as the project asks; text says 2.15.4.
- X_0(27): the 27-isogeny on the CM curve is checked with PARI ellisomat.
- Cremona labels: "as in Cremona97 and ecdata" (the printed tables stop at N = 1000).
- Metadata: Kraus90 unconfirmed issue number removed; HatleyKundu now published, Ann. Math. Que. 50 (2026) 143-165; Ogg issue 1; PollackWeston11 numbering is the same in the published version; DOIs added for DFG04, KimOta, ARS12, AtkinLi78, CalegariEmerton09, CaroPasten22, DokDok15, Dummigan06, HatleyKundu, Ligozat75, Ogg, Pasten (and appendix credit), PollackWeston11, RibetTakahashi97, Saito88, Serre72, Sturm87, Sutherland16, Takahashi01, Watkins02, Zagier85.

## Confirmed against the text
DFG04 (all remaining locators), Flach92 Thm 1, Kenku Thm 1, PollackWeston11 Thm 6.11 and Conj. 1.4, RibetTakahashi97 Thm 1, Takahashi01 Cor. 3.4-3.5, AU96 Lemme 2.1, CalegariEmerton09 Thm 1.1, DokDok15 Thm 5.4(1), Zywina15, Watkins02 eq. (1-1), Zagier85 Section 1, ARS12 Thm 2.2 and Table 1 (authors' version), FPR94 I.4.2.2 (as used in DFG pp. 708-709).

## Still unverified (texts not reachable from here)
- DDT: Thm 3.1(e), Thm 3.15, Section 4.4, Lemma 4.17. The 2007 online copy titles Section 4.4 "Proof of theorem 3.36", which may not match the cup-product citation; Lemma 4.17 may be in the commutative-algebra chapter. Check against the 1997 printed version.
- Edixhoven92 Section 2 (Deligne and Fontaine on rho-bar at l): other sources point to Section 6 (6.8 for Fontaine).
- Ribet90: the hypotheses of the theorem used for the twisted level-lowering step.
- RibetStein Theorem 3.5 (online version differs slightly from the printed one).
- ARS12: section numbers in the printed Springer chapter.
- SerreTate68 Sections 1, 2; Serre72 Section 1 (other papers cite Props. 11, 12); SilvermanATAEC IV.9 for the extension of Phi by E_0; Carayol89; Kraus89, Kraus90 (content, end page 385 or 386); Tilouine97; Pasten (the error-term claim); Ligozat75 (identification of the CM point; the 27-isogeny itself is checked in PARI); Shimura75; Sutherland16 label section.
- KimOta: numbering of the published version.
- Data sources for 726a1 and 539d1 in Remark (they are ecdata curves; not from ARS).

## Follow-up, same day: the five priority texts (supplied by the author)
- DDT (revised version of 9 Sept 2007, Darmon's page): Thm 3.1(e) on p. 86 confirmed (rho|G_p = (chi.eps, *; 0, chi), chi(Frob_p) = a_p, p || N, p != l); Thm 3.15 on p. 92 confirmed as quoted (l odd, Q(sqrt-3) condition at 3, level N(rho)l^delta, nebentypus order prime to l; delta = 0 when good); Section 4.4, though titled "Proof of theorem 3.36", contains the pairing via w_* and the cup product, (4.4.2), with Hecke operators self-adjoint, so the citation stands; Lemma 4.17 on p. 126 confirmed (the note proves the inequality itself and does not use DDT's reducedness). Bib note records the version.
- Edixhoven92 (published): Theorem 2.5 (Deligne) and 2.6 (Fontaine) are in Section 2, p. 567; Fontaine's proof is in Section 6. Locator sharpened to Theorems 2.5, 2.6.
- Ribet90 (published, OCR of the scan): Theorem 1.1 (Main Theorem): rho irreducible mod l >= 3, modular of level N with trivial character, p || N, rho finite at p; then modular of level N/p if p != 1 mod l or l does not divide N. The note's use (case (c)) has l not dividing N; the citation now says Theorem 1.1 and names that hypothesis.
- RibetStein (authors' online version, not the printed one): Theorem 3.5 in Section 3.3.2 confirmed; the exception requires k(rho) = l together with three other conditions, so it cannot occur for weight 2 and l odd prime to the level, as the note says. Bib note records the version.
- ARS12 (authors' version "current.pdf", the same one used by the sweep): Theorem 2.2, Table 1 (99A1: 4, 12), r_E in Section 1, perfect pairing in Section 4.1 confirmed. The printed chapter was not supplied.
Remaining: printed numbering of RibetStein and ARS12 (the authors' versions may differ slightly), and the priority 2 and 3 items.

## Follow-up: Brown, Cohomology of Groups (supplied by the author)
- Shapiro's lemma is III.(6.2) (Section III.6); the Hochschild-Serre spectral sequence of a group extension is VII.(6.3) (Section VII.6). The book's Brown locators were checked against the table of contents and statements: I.5, III.1, III.6, III.8 (conjugation acts trivially, 8.1/8.3), III.9 (transfer), IV.3 (extensions), V.3 (cup products), VI.4 (Tate cohomology), VI.7 (duality theorem), VII.6: all correct.
- The spectral sequence used in Step 1 of the proof of Proposition prop:integral, H^p(G, H^q_c) => H_{G,c}, is not the Hochschild-Serre sequence of a group extension; the note no longer calls it that. Its cellular form is Brown VII.(7.2) (from (5.1)), and the cellular form of the equivariant Leray sequence is VII.(7.7), with stalks by Shapiro's lemma as in VII.(7.6). The note now cites Shapiro III.(6.2), Grothendieck 1957 Chapter V for the sheaf-theoretic versions, and adds a parenthetical cellular version (relative cohomology of the compactified curve modulo its cusps, a G-CW structure with cells fixed pointwise by their stabilisers), which rests on Brown alone. The book (Chapter 20) adds the same pointer.
- Grothendieck 1957 Chapter V is now needed only as an alternative reference; the cellular route through Brown suffices.

## Follow-up: priority 2 texts (supplied by the author)
- AtkinLi78 (published): p. 228 states that F twisted by chi of conductor M prime to N is a newform of level NM^2; Theorem 3.1 (p. 228), with alpha = 0, beta = 1, Q = q, Q' = q^2 > Q and cond(eps_Q chi) = q = max(q^alpha, q^beta), gives exact level q^2 M when q || level. Lemma (iii) confirmed for both cases.
- Serre72 (OCR of the scan): Section 1.11, Proposition 11 (good ordinary reduction: inertia acts on the kernel line by the fundamental character of level 1 and trivially on the quotient) and Proposition 12 (good supersingular reduction, e = 1: fundamental character of level 2, image a nonsplit Cartan). Locator sharpened to Section 1.11, Propositions 11 and 12. Book locators also confirmed: Section 2, Propositions 15 and 16; Section 5.6 (the groups Phi_p, with the cases p = 2, 3).
- Hida81 (published): title "Congruences of cusp forms and special values of their zeta functions" (as now in refs.bib); Theorem 5.1 (p. 247): L(k, f, psi-bar) = 2^{2k} pi^{k+1} ((k-1)!)^{-1} {delta(N) N N(psi) phi(N/N(psi))}^{-1} (f,f)_{Gamma_1(N)}, delta(N) = 2 or 1 according as N <= 2 or not; consistent with DFG Lemma 2.12 and with the note's formula.
- SerreTate68 (OCR of the scan): Section 1, Lemma 2 (inertia invariants of A_m map isomorphically to the special fibre); Section 2, Theorem 2: (i) potentially good reduction iff the image of inertia is finite; (ii) then the kernel is independent of l and the character has values in Z independent of l. Note locators sharpened to Theorem 2(i), 2(ii).
- SilvermanATAEC: IV.9 Corollary 9.2(b) (E(K)/E_0(K) = component group for K Henselian, used with K = Q_q^ur) and Table 4.1 (component counts) in IV.9; Ogg's formula IV.11 (11.1); Tate curve twist V.5 (Lemma 5.2, Theorem 5.3, Corollary 5.4). Note locators sharpened to IV.9 Corollary 9.2 and IV.9 Table 4.1.
