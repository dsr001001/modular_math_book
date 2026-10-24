# Open items for the note and the book (24 October 2026)

Not for readers of the book: a working list for the author.

## 1. Protocol paragraph of the note (Section sec:data), pending the author's check
Evidence from the commit history of dsr001001/mcptrial (ecmine), UTC:
- 4 Oct 19:16-19:25: eq:main found on the working set; first hold-out runs (incl. a twist check on the hold-out).
- 6 Oct 18:41: checker on hold-out and the new extension range; 0 violations of eq:main and of the old twisted rule.
- 6 Oct 19:29 (4b64dc7): eq:twist replaces the "all but the largest" rule; scripts/step7_twist2.py run on work, hold-out and extension in the same commit. The record says the change came from separating q = 2 from odd q on the working set.
- 6 Oct 19:36: final out-of-table set (893 curves, with degrees).
- 10 Oct 06:45 (1962d7a): Euler-factor rule v1, from working-set minima; run on all four ranges: 200 / 42 / 22 violations (l = 3, work / hold-out / ext), 0 out of table.
- 10 Oct 08:50 (f43bade): v2, PARI factors at every bad prime (terms at 2 and 3); 364 / 68 / 43 violations (the Ns curves, absorbed by h_3), 0 out of table.

Consequences:
- Q1. The out-of-table curves were run through rule v1 before the terms at 2 and 3 were fixed; they never failed and prompted no change, but they were not unseen. "Blind test" overstates it.
- Q2. eq:twist was written after the hold-out counts of eq:main were known, and was evaluated on hold-out and extension in the same commit. "Then tested once on the hold-out and the extension" is not supported by the record.

Proposed wording (to adopt unless the session transcripts of 6 and 10 October show otherwise):
- eq:twist "was formulated on the working set after the hold-out and extension counts of (eq:main) were known, and evaluated on all three ranges together; the hold-out and extension are a confirmation for it, not a blind test."
- the out-of-table curves "were generated before the rule was formulated and were run through each version of it as it was formulated; no version failed on them and they prompted no change, so they are an independent confirmation rather than a strictly blind test."
Then update the protocol remarks of Chapter 22 and the reading of Section 6.1 in Chapter 21.

A question to put to the session that did the work (if its transcript is available) is in the conversation of 24 October; it asks, for eq:twist and for the terms at 2 and 3, which outputs on the hold-out, extension and out-of-table sets were displayed before each formulation.

## 2. Table wording in the note
- tab:isolated: the column headers say "weight 1/2/3", but in the untwisted rows the columns count primes (only the caption says so).
- tab:counts: the caption does not say what the "curves" column counts (all optimal curves of the range, not the population of tab:uniform).
- tab:iso: the caption says "The same holds at l = 5 and 7", but only l = 3 is printed; print those rows (results/step9_euler_l5.txt, step9_euler_l7.txt) or point to the files.
- The four twisted rows of tab:isolated could not be checked against the repository: their source parquet files are git-ignored.

## 3. Repository documentation (dsr001001/mcptrial, cannot be pushed from the book session)
- ecmine/README.md says paper/tables/euler_uniform.tex comes from step10_make_table.py; it comes from step11_tw_boundary.py (as HANDOFF.md says). euler_iso3.tex was copied by hand from step9_euler_l3.txt.

## 4. References to check against the originals
- Diamond-Flach-Guo 2004: page numbers for Sections 1.2.2, 1.2.3, 1.4.1, 1.4.2, Lemma 1.1, Proposition 1.3, (5), and the "sufficiently small" paragraph before Lemma 1.2 (used in the proof of Proposition prop:integral and the pairing constant); arXiv numbering of the long version.
- Brown, Cohomology of Groups: theorem numbers for Shapiro's lemma (III.6) and Hochschild-Serre (VII.6).
- Grothendieck 1957 (Tohoku), Chapter V: the equivariant Leray spectral sequence as used.
- Pollack-Weston journal pages; Ligozat 1975 (CM at 27); Calegari-Emerton (arXiv numbering).
- A published proof of Sha(11a1)[5] = 0.

## 5. Mathematics to have checked by a specialist
- The proof of Proposition prop:integral (integral comparison of the DFG integral structure with H^1(X_0(M),Z)): in particular the reading of DFG's definitions in Section 1.4.1, the Hecke action of their Proposition 1.3 including U_p, and the use of the statement before their Lemma 1.2.
- The exact pairing constant: the note proves (u/2) with u an l-adic unit, which is all it needs; the exact value 1/2 is not proved (a naive count gives an N-dependent constant, so DFG's normalisation of the target needs a careful reading).
- No human expert has yet read the book line by line.

## 6. From the third review (comprehensive audit, 24 October)
Done: Theorem thm:qual(c) now says n >= 1 (I_0^* was not excluded; the proof and the data need n >= 1); a forward pointer to the definition of S_f (Section sec:dfgthm) where it is first named.
Repository (dsr001001/mcptrial, not pushable from here):
- results/repro.log records a failed clean-clone run (scripts/conj_check.py not found from the working directory, summaries then "DIFFERS"); repro_check2.log is a later checker-only rerun. Fix the path, rerun the full clean clone, and replace the log.
- scripts/repro_run.sh ends the PARI feature step with "; true", which masks failures; run under set -euo pipefail and check row counts and checksums after each stage.
Optional clarity edits suggested for the note (not errors):
- a one-page dependency diagram for Theorem thm:main (prop:integral -> prop:pullback -> DFG Thm 3.7, Prop 1.4(c), Lemma 2.1 -> local FPR formula -> local terms), hypotheses beside each arrow;
- in prop:integral, a small diagram H^1_c(Y_0) -> H^1(X_0) -> H^1(Y_0) and one sentence on why the comparison over C gives equality of lattices (torsion-free, pi^* injective);
- in Section sec:dfgthm, say explicitly that the local group used is the torsion of H^1(Q_q,T^D), finite under H^0(Q_q,V^D)=0;
- before the local table, state the normalisations X = q^{-s}, P_q, and that the naive denominator is 1 at additive primes;
- for the Ns case, label separately: proved (h_3 = 1), conditional (on H^1_f(Q,V^D) = 0), and empirical (weights at q = l = 3).
