# How to continue this project

This file tells a new Claude Code conversation (or a human) how to pick up the textbook where it stands on
15 October 2026. Read it first, then `PLAN.md`.

## 1. Where things stand

| Item | State | File |
|-|-|-|
| Master plan, conventions, binding decisions | done | `PLAN.md` (decisions in Section 7.5) |
| Outlines of all 22 chapters and Appendix B | done, reviewed for consistency | `outlines/chNN_slug.md`, `outlines/chB_notation.md` |
| Plan and outlines as one PDF | done (649 pages) | `docs/book_plan.pdf`, rebuilt by `tools/build_plan_pdf.sh` |
| Bibliography | done, verified, 203 entries, no duplicates | `refs.bib` (shared), `bib/chNN.bib` (single-chapter) |
| Findings about the paper | 80 points plus book-internal notes | `important/important_notes.md` (full record) |
| Memo for the paper's author | done | `important/paper_memo.md` (final, reconciled) |
| Revised paper with the stronger results | see `paper/CHANGES_v2.md` | `paper/note_v2.tex`, `docs/note_v2.pdf` |
| Preface | written (needs a final update) | `frontmatter/preface.tex` |
| Appendix A (prerequisites) | partly written (complex analysis, group theory and statistics sections missing) | `chapters/chA_prereq.tex` |
| Chapters 1 to 22, Appendix B | **not yet written** | `chapters/` |

The original paper is `note_Oct10_7pm.tex`. Labels in the revised paper are the same.

## 2. Setting up a new session

The container of a new cloud session starts empty except for the repository. Run once:

```
git checkout claude/textbook-paper-prerequisites-clhh5a
tools/setup_env.sh
```

This installs TeX Live, pandoc and poppler, the Python package cypari2 (PARI/GP), and downloads Cremona's
ecdata files for conductor below 10,000 into `data/ecdata/` (git-ignored). It ends with a smoke test that
builds Appendix A. Outlines sometimes mention `/tmp/ch09/data`: that was the old location of the same files;
use `data/ecdata/`.

## 3. Prompt to start the new conversation

Paste this as the first message:

> Continue the textbook in this repository, on branch `claude/textbook-paper-prerequisites-clhh5a`. Read
> `CONTINUE.md`, then `PLAN.md`. Run `tools/setup_env.sh`. Then do the pilot: write Chapter 10 with the
> workflow in `tools/workflows/write_chapters.js`, commit and push, and stop to show me the result, its
> length and what it cost before writing more chapters.

(Replace Chapter 10 by another chapter if preferred; see Section 5.)

## 4. Small tasks to do first (before or with the pilot)

1. **Character notation (decision D3).** Convert the remaining `chi_q` (quadratic character of conductor q)
   in the outlines to `chi_{q*}`; keep `chi_l` only for the cyclotomic character. About 40 occurrences. Update
   convention B-C11 in `outlines/chB_notation.md` to match D3.
2. **Chapter 18 outline**: replace the hedge "subject to point 56" by a citation of point 73 (settled).
3. **Appendix A**: write the missing sections (complex analysis, group and representation theory as in
   Riley-Hobson-Bence, probability and statistics) to 400 to 800 lines more; it compiles with
   `tools/build_chapter.sh A`.

## 5. Writing the chapters

**Pilot first.** Write one chapter end to end, look at it, measure its length and cost, and adjust the process
before writing the rest. Recommended pilot: Chapter 10 (proofs, tables, Kodaira symbols, PARI-checkable
examples and paper links, middle difficulty). Alternatives: Chapter 1 (easiest) or Chapter 20 (hardest).

**The workflow.** `tools/workflows/write_chapters.js` runs, for each chapter given in `args.chapters`:
one agent writes the chapter from its outline (compiling with `tools/build_chapter.sh NN` and linting with
`tools/lint.py`); a sceptical mathematical reviewer and an editorial reviewer read it in parallel; a fixer
applies their findings; the mathematical review repeats until no serious finding remains (at most three
rounds). In Claude Code:

```
Workflow({ scriptPath: "tools/workflows/write_chapters.js",
           args: { chapters: [ { num: "10", slug: "reduction",
                                 title: "Elliptic curves over local fields: reduction, Kodaira types, Tate curves" } ] } })
```

Chapter numbers, slugs and titles are in `PLAN.md` Section 4 and in the chapter list at the front of
`docs/book_plan.pdf`. Run three chapters at a time. Without the Workflow tool, run the same four stages by
hand with sub-agents, using the prompts in the script.

**Order after the pilot**: Part I (Chapters 1 to 4), Part II (5 to 7), Part III (8 to 11), Part IV (12 to 15),
Part V (16 to 19), Part VI (20, then 21 and 22 last, since they cite every other chapter's items), then
Appendix B from its outline, then the preface update.

**After each batch**: commit and push; append any new problem found in the paper to
`important/important_notes.md` (and, if significant, to `important/paper_memo.md`); record any book-wide
decision in `PLAN.md` Section 7.5.

**Integration at the end**: build the whole book with `tools/build.sh`; upgrade chapter-level cross-references
in Chapters 21 and 22 to item-level labels; run a completeness check against the paper; re-verify the
bibliography.

## 6. Rules every chapter must follow

All are in `PLAN.md` Section 7; the essentials:

* No em dash or en dash in any form, never `---` or `--` (outside BibTeX page ranges); ASCII-only source.
* One file per chapter; no macros defined in chapters; labels `kind:slug:name`; cross-chapter references only
  `\Cref{ch:slug}`.
* Each chapter opens with "Core results at a glance" (precise statements) and "Where the paper uses this
  chapter", and ends with Exercises and Notes and references.
* Conventions of Appendix B (`outlines/chB_notation.md`, B-C1 to B-C16) are binding: Frob arithmetic,
  Phi = Frob^{-1} geometric, L-factors use Phi; duals `^vee`, `^*`, `^D`, adjoint `^dagger`; `J_f` for the
  abelian variety, `A_f` for the adjoint.
* Decisions D1 to D4 (`PLAN.md` 7.5): state the book's stronger results as theorems; length is a guideline,
  not a cap (online reference book); quadratic characters `chi_{q*}`; Manin constant `c_E > 0`.
* Never repeat an error of the paper listed in `important/paper_memo.md`.

## 7. Cost and size

The book is planned at about 49,000 lines of LaTeX (roughly 1,100 to 1,400 pages). Each outline was produced
by one agent in about 25 minutes; writing a chapter with two reviews and up to three fix rounds will take
several agents per chapter. Measure the pilot before committing to the rest.

## 8. Open items that need a human or a source check

From `important/paper_memo.md` Section E: the comparison of DFG04's integral structure with
H^1(X_0(N), Z_l) at non-Eisenstein ideals (medium-high confidence); the published theorem number in
Calegari-Emerton; Sutherland's image labels against Sutherland16; Zywina's theorem numbers; the twist
exchanges at q = 3 (need a reference); and every new proof in the revised paper, which the author must review.
