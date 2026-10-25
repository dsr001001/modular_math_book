# Final versions

* `paper/note.tex`: the research note "Local factors of the adjoint L-function and the l-adic valuations of the
  modular degree" (D. Soni). Build: `cd final/paper && latexmk -pdf note.tex`.
* `book/`: the companion book *From First Courses to the Modular Degree*, aligned with the note. Build:
  `final/book/tools/build.sh` (output `final/book/build/main/main.pdf`).
* `pipeline/`: the computations behind the note's Section 6 and its six data tables: scripts, result files,
  the tables as printed, a self-test, a checksum manifest and a hardened reproduction script. Start with
  `pipeline/README.md`. Data: Cremona's `ecdata` tables at a pinned commit, downloaded by the scripts (1.2 GB, not
  committed).
* `claims/`: a machine-readable ledger of the paper's claims (`claims.csv`, `claims.yaml`): for each numbered
  statement, table and named example, its status (proved, imported, conjectural, empirical, computed), where the book
  treats it, the script and output behind it, and the level of computational evidence; `claims/scripts/check_claims.py`
  validates it against the paper, the book and the pipeline.
* `process/how_we_went_about_this.pdf`: how the work was done from the 15 October hand-over onwards; the planning
  session (11 to 15 October: plan, outlines, findings, version 2 of the note) has its own report,
  `../docs/how_we_went_about_this_planning_session.pdf`. This one covers the book, the final note, the pipeline and its
  full rerun.
* `TODO.md`: open items for the author (not part of the book or the paper).

The working copies at the repository root (`paper/`, `chapters/`, `important/`) keep the full history of the review.
