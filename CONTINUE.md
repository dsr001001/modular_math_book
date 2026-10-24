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
| Findings about the paper | 112 points plus book-internal notes (B1 to B42) | `important/important_notes.md` (full record) |
| Memo for the paper's author | done | `important/paper_memo.md` (final, reconciled) |
| Revised paper with the stronger results | done (32 pages), needs the author's review | `paper/note_v2.tex`, `docs/note_v2.pdf`, change log `paper/CHANGES_v2.md` |
| Preface | written (needs a final update) | `frontmatter/preface.tex` |
| Appendix A (prerequisites) | written (994 lines, compiles) | `chapters/chA_prereq.tex` |
| Chapter 10 (pilot) | written, three review rounds, 2,344 lines, 48 pages | `chapters/ch10_reduction.tex` |
| Chapter 1 (groups) | done: lean pipeline (run wf_b06051c4-f4c), one review (1 major, 12 minor, all fixed), check clean, 1,844 lines, 43 pages; cost see human | `chapters/ch01_groups.tex` |
| Chapter 2 (rings) | done: lean pipeline by hand (interactive session), one review (3 major, 14 minor, all fixed), check (1 major, 6 minor), second fix; 2,170 lines, 47 pages | `chapters/ch02_rings.tex` |
| Chapter 3 (modules) | done: lean pipeline by hand, review (1 blocking, 18 minor, all fixed), check (6 minor; 4 fixed, 2 in B31); 2,529 lines, 58 pages | `chapters/ch03_modules.tex` |
| Chapter 4 (reps) | done: lean pipeline by hand, review (1 blocking, 2 major, 11 minor, all fixed), check (3 minor, in B32); 2,053 lines, 45 pages | `chapters/ch04_reps.tex` |
| Chapter 5 (galois) | done: lean pipeline by hand, review (1 major, 10 minor, all fixed), check (3 minor, fixed); 2,089 lines, 49 pages | `chapters/ch05_galois.tex` |
| Chapter 6 (ant) | done: lean pipeline by hand, review (1 major, 12 minor, all fixed), check (5 minor, fixed); 1,851 lines, 43 pages | `chapters/ch06_ant.tex` |
| Chapter 7 (local) | done: lean pipeline by hand, review (3 major, 13 minor), check (1 blocking from the fix, 3 minor), second fix; 2,219 lines, 52 pages | `chapters/ch07_local.tex` |
| Chapter 8 (curves) | done: lean pipeline by hand, review (1 blocking, 2 major, 12 minor), check (2 major, 2 minor), second fix; 1,988 lines, 50 pages | `chapters/ch08_curves.tex` |
| Chapter 9 (ellcurves) | done: lean pipeline by hand, review (4 blocking, 3 major, 13 minor), check (5 minor); 2,234 lines, 52 pages | `chapters/ch09_ellcurves.tex` |
| Chapter 11 (galrep) | done: lean pipeline by hand, review (7 major, 9 minor), check (5 minor); 2,050 lines, 48 pages | `chapters/ch11_galrep.tex` |
| Chapters 12 to 15 (Part IV) | done: lean pipeline by hand | `chapters/ch12_modforms.tex` to `ch15_modgalrep.tex` |
| Chapters 16 to 19 (Part V) | done: draft all, one review each, one fix pass | `chapters/ch16_cohomology.tex` to `ch19_lfunctions.tex` |
| Chapters 20, 22, Appendix B | done: draft, one review each, one fix pass | `chapters/ch20_congruence.tex`, `ch22_computation.tex`, `chB_notation.tex` |
| Full-book pass (step 4) | done: full book builds (1,045 pages, Chapter 21 a placeholder), no undefined references, no duplicate labels or BibTeX warnings, 12 overfull boxes only in the preface; all 21 cross-chapter items fixed | `important/fullbook_pass_list.txt` |
| Step 5 (sources) | done for DFG04, RT97, Takahashi01 (note B42); remaining flags listed there | `important/important_notes.md` |
| Chapter 21 (the paper) | done: draft, one review, one fix pass; errata E1 to E38 | `chapters/ch21_paper.tex` |
| Book status | **complete**: 22 chapters, Appendices A and B, preface; 1,187 pages; final build clean. Open items: a published proof of Sha(11a1)[5] = 0; Ligozat75 (CM at 27) unchecked; Pollack-Weston journal pages; arXiv long-version numbering of DFG04; human expert reading not yet done | `build/main/main.pdf` |

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
> `CONTINUE.md`, then `PLAN.md` Sections 7.5 and 9. Run `tools/setup_env.sh`. Then write Chapter 1 with the
> workflow in `tools/workflows/write_chapters.js` in lean mode (`args.lean: true`), commit and push, and stop to
> show me its length and what it cost (`/cost`) before writing more chapters.

The pilot (Chapter 10) is done; see PLAN.md Section 9 for what it taught and what it cost.

## 4. Small tasks to do first (before or with the pilot)

All three are done (16 October 2026 session): the outlines use chi_{q*} throughout (chi_q only in quotations of the paper), Appendix B states D3, Chapter 18 cites point 73, and Appendix A has all its sections.

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

The book is planned at about 49,000 lines of LaTeX (roughly 1,100 to 1,400 pages). The pilot (Chapter 10,
2,344 lines) cost about USD 31 to 35 on Opus 5.5 with the full pipeline, almost all of it context re-read on
every tool call. Budget mode (`args.lean: true`) is expected to cost about USD 12 to 18 per chapter. Details
and priorities under a fixed budget: PLAN.md Section 9.

## 8. Open items that need a human or a source check

From `important/paper_memo.md` Section E: the comparison of DFG04's integral structure with
H^1(X_0(N), Z_l) at non-Eisenstein ideals (medium-high confidence); the published theorem number in
Calegari-Emerton; Sutherland's image labels against Sutherland16; Zywina's theorem numbers; and every new proof in the revised paper, which the author must review.

For the revised paper (`paper/CHANGES_v2.md` ends with the full list), check most carefully:
* Proposition prop:pullback, which relies on DFG04's integral structure agreeing with H^1(X_0(N), Z_l) at
  non-Eisenstein maximal ideals (only sketched; memo item E1);
* the new proofs of Lemma lem:tamadd, Proposition prop:Sf, Lemma lem:IV at q = 2, Proposition prop:shapes,
  the equality step in Theorem thm:quant, and Proposition prop:ns-structure (ii) when 3 | N (a new argument of
  the revising agent, not in the memo);
* the citation for the cyclic 27-isogeny in Proposition prop:no9 (Ligozat, Kenku, without theorem numbers);
* the six tables in `paper/tables/`, which are placeholders and must be replaced by the real tables;
* the new sentences in the statement on the use of an AI system.

## 9. Running on Claude Console API credit

The work so far ran in Claude Code on the web (claude.ai). To run it on Console API credit instead:

1. On a Linux machine (or WSL on Windows; `tools/setup_env.sh` uses apt, so on a Mac install MacTeX, pandoc,
   poppler and `pip install cypari2` by hand), install Claude Code and sign in with the Console account
   (`claude`, then choose the Anthropic Console login), or export `ANTHROPIC_API_KEY` with a key from the Console.
2. In the Console, set a spend limit on the workspace the key belongs to (for example USD 100), so a run cannot
   overspend.
3. `git clone` the repository, `git checkout claude/textbook-paper-prerequisites-clhh5a`, run
   `tools/setup_env.sh`, start `claude` in the repository and paste the prompt of Section 3.
4. Use budget mode (`args.lean: true`), one chapter at a time at first. Type `/cost` after each chapter and
   record the figure in PLAN.md Section 9. If the Workflow tool is not available, ask Claude to run the same
   stages with sub-agents, using the prompts in `tools/workflows/write_chapters.js` (lean variant).
5. Commit and push after every chapter, so nothing is lost if the session ends.

With USD 100, expect about 5 to 7 chapters in budget mode; start with Part I (Chapters 1 to 4).

## final/ (2026-10-24)

`final/paper/note.tex` (corrected note, 35 pp) and `final/book/` (book aligned with it as a single version: all chapters re-quoted verbatim against the note, version history and errata removed, Chapter 21 recast as a guided reading, preface rewritten). Final book: 1,179 pages, clean build, 0 overfull boxes, no undefined references; PDF at `final/book/build/main/main.pdf`. Still needed from the author: the six data tables of the note (placeholders), the sec:data extension-range fact, and answers to the two protocol questions in Chapter 22 (were out-of-table degrees seen while fixing the terms at 2 and 3; was eq:twist fixed before the hold-out counts of eq:main were seen).
