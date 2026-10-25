# Open items for the note and the book (24 October 2026)

Not for readers of the book: a working list for the author.

## 1. Protocol paragraph of the note (Section sec:data)
Resolved (25 October): the note adopts neutral wording (eq:twist formulated after the hold-out/extension counts of eq:main, a confirmation there; out-of-table curves evaluated with each version of the rule, an independent confirmation), and Chapters 21, 22, A and the reviewers' route follow it.
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
- Done (24 October): the four twisted rows of tab:isolated, whose source parquet files are git-ignored, were regenerated from the pinned data by the full rerun (tables/isolated3.tex byte-identical; item 7).

## 3. Repository documentation (dsr001001/mcptrial, cannot be pushed from the book session)
- ecmine/README.md says paper/tables/euler_uniform.tex comes from step10_make_table.py; it comes from step11_tw_boundary.py (as HANDOFF.md says). euler_iso3.tex was copied by hand from step9_euler_l3.txt.

## 4. References to check against the originals
Sweep done 25 October (process/reference_sweep_2026-10-25.md): metadata of all 51 works checked, DFG04 locators all checked against the Annales text, fixes applied to the note, the book and the ledger. DDT, Edixhoven92, Ribet90, RibetStein and ARS12 checked against texts supplied by the author (same day; see the follow-up section of the sweep record). Decision (25 October): RibetStein, ARS12, DDT and KimOta are cited with the numbering of the online versions named in refs.bib. Still to check: SerreTate68, Serre72, Silverman IV.9, Carayol89, Kraus89/90, Tilouine97, Pasten, Ligozat75 (CM point), KimOta published numbering.
Brown checked (25 October): Shapiro III.(6.2), Hochschild-Serre VII.(6.3); Step 1 of prop:integral now has a cellular version resting on Brown VII.(7.2), (7.7), so Grothendieck 1957 Chapter V is optional. Also still: a published proof of Sha(11a1)[5] = 0.
Priority 2 done (25 October): AtkinLi78, Serre72, Hida81, SerreTate68, SilvermanATAEC checked against the texts; locators sharpened. Remaining: Kraus89, Kraus90, Carayol89, Tilouine97, Pasten, Ligozat75, Sutherland16, Shimura75, Shimura76; a published proof of Sha(11a1)[5] = 0.

## 5. Mathematics to have checked by a specialist
- The proof of Proposition prop:integral (integral comparison of the DFG integral structure with H^1(X_0(M),Z)): in particular the reading of DFG's definitions in Section 1.4.1, the Hecke action of their Proposition 1.3 including U_p, and the use of the statement before their Lemma 1.2.
- The exact pairing constant: the note proves (u/2) with u an l-adic unit, which is all it needs; the exact value 1/2 is not proved (a naive count gives an N-dependent constant, so DFG's normalisation of the target needs a careful reading).
- No human expert has yet read the book line by line.

## 6. From the third review (comprehensive audit, 24 October)
Done: Theorem thm:qual(c) now says n >= 1 (I_0^* was not excluded; the proof and the data need n >= 1); a forward pointer to the definition of S_f (Section sec:dfgthm) where it is first named.
Repository (dsr001001/mcptrial, not pushable from here):
- results/repro.log records a failed clean-clone run (scripts/conj_check.py not found from the working directory, summaries then "DIFFERS"); repro_check2.log is a later checker-only rerun. Fix the path, rerun the full clean clone, and replace the log. In final/pipeline: done by the full rerun of 24 October (item 7; logs in final/pipeline/results/rerun_20261024/); mcptrial itself is untouched.
- scripts/repro_run.sh ends the PARI feature step with "; true", which masks failures; run under set -euo pipefail and check row counts and checksums after each stage. In final/pipeline: done (hardened copy, item 7).
Optional clarity edits suggested for the note (not errors):
- a one-page dependency diagram for Theorem thm:main (prop:integral -> prop:pullback -> DFG Thm 3.7, Prop 1.4(c), Lemma 2.1 -> local FPR formula -> local terms), hypotheses beside each arrow;
- in prop:integral, a small diagram H^1_c(Y_0) -> H^1(X_0) -> H^1(Y_0) and one sentence on why the comparison over C gives equality of lattices (torsion-free, pi^* injective);
- in Section sec:dfgthm, say explicitly that the local group used is the torsion of H^1(Q_q,T^D), finite under H^0(Q_q,V^D)=0;
- before the local table, state the normalisations X = q^{-s}, P_q, and that the naive denominator is 1 at additive primes;
- for the Ns case, label separately: proved (h_3 = 1), conditional (on H^1_f(Q,V^D) = 0), and empirical (weights at q = l = 3).

## 7. Pipeline (final/pipeline, copied from mcptrial/ecmine at f57c783; mcptrial left untouched)
Done: paths fixed, repro_run.sh hardened (fails on any error or count mismatch), reproduce_tables.sh added, README/PROVENANCE/ENVIRONMENT/requirements, self-test (passes here), MANIFEST.sha256. The README slip of item 3 is corrected in this copy.
Done (24 October):
- Full rerun, end to end, in this repository (2 cores, 7 GB; PARI 2.17.2 via cypari2, with scripts/gp_cypari2_standin.py in place of gp): stage 1 (pinned download, 3,064,705 curves; PARI features; feature table; 1,311,066 / 429,936 / 359,009 optimal curves; check_{work,holdout,ext}_summary.csv byte-identical; the script was killed for memory while writing results/check_work_perl.parquet, and the checker was run per range) and stage 2 (every regenerated summary and table file byte-identical, selftest passed). Logs in final/pipeline/results/rerun_20261024/; README section "Full rerun".
- The appendix's clean-clone sentence is replaced in the note by "The whole pipeline was rerun from the pinned data with PARI/GP 2.17.2 and reproduced every committed result summary and Tables ... byte for byte."; claims ledger, Chapter 21, Chapter 22 and the reviewer's route follow it.
- PARI version comparison: PARI 2.15.4 (cypari2 2.2.0, Python 3.12) and 2.17.2 agree on all 38,042 optimal curves below 10,000 (ellmoddegree, ns3, both forms of the rule for l = 3..13; pari_features.gp byte-identical on the block 00000-09999); results/stage3_versions.txt.
Still to do:
- Minor: the galrep labels above conductor 400,000 have no dots (3Cs11, 3B11) and scripts/conj_check.py (likewise step6_*, step7_eis_proxy.py) matches only 3Cs.1.1, so on the extension the split-Cartan term of conj:eis is 0 for the one optimal 3Cs11 curve. This only weakens the bound and does not affect the committed results; match both spellings (as scripts/stage3_eis.py does) and rerun the extension checker when convenient.
- tab:excess (conductor < 10,000) is produced by the book's own scripts (Chapter 22), not by any script in final/pipeline.
- Package versions of the original runs were not recorded; requirements.txt gives the versions that work here.

## 8. Audit items 1-15 (24 October, evening)
Done: clarity edits 1-11 in the note (dependency table, prop:integral diagram, normalisations, Ns status, thm:quant Steps 2 and 4 and the equality, Frobenius sentence, status notes in table captions, the two congruence statements kept apart); reviewer's route in the book (front matter); claim ledger final/claims/ with evidence levels; wild Euler-factor sample final/pipeline/samples/.
Found by the ledger and corrected in the note: Section sec:forms read 455,707 as the l=3 pairs with l | N; in results/step6_u1c_work.txt it is all l=3 pairs (not split by 3 | N).
Done (24 October, stage 3 of the full rerun; final/pipeline/results/stage3_summary.md): the numbers stated in the paper with no committed result file were recomputed from the pinned data (the Eisenstein deficit counts, the working-set minima at q=3 defining w_3, the twist-pair counts 157,938 and 292,580, the extension exceptions of Section 7, the whole-table check of lem:euler against lfunsympow, a sample of 63 degrees in place of the unnamed fifteen, the mod 3 image check, the PARI 2.15 vs 2.17.2 comparison, the 30-digit check of rem:degree, the degree of 6942n1; the twisted rows of tab:isolated by stage 2). 21 of 23 reproduced; two wording corrections made in the note:
- sec:two: 19, not 20, exceptions on the extension (the 20th, 401291a1, lies in a class whose optimal curve is not determined in the tables);
- sec:eis: the 18 curves with a point of order 9 up to conductor 400,000 are all curves, optimal or not (14 optimal), not "18 optimal curves".
The ledger marks these rows "regenerated". Still open from the ledger: the data sentence of Remark 3.4 (P-rem:after-ex:qual, "quoted"; its congruence numbers are recomputed in the book).
