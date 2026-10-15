# Handoff: continue the textbook from Chapter 2 (Claude Code on a Console account, Opus 5.5)

This file is the first message of a new Claude Code session. It is self-contained: read it in full before
doing anything, then follow it. Written 16 October 2026 at the end of the previous session.

---

## 0. For the human (do this before starting Claude Code)

1. Start Claude Code with Opus 5.5 as the model, signed in with the Console account (or with
   `ANTHROPIC_API_KEY` set to a Console key):

   ```
   claude --model claude-opus-5-5
   ```

   (Or type `/model` in a running session and pick Opus 5.5.) Sub-agents use the session's model.
2. In the Console, set a spend limit on the workspace (for example USD 100), so a run cannot overspend.
3. Give the session access to GitHub so it can pull and push the same repository and branch (for example
   `gh auth login`, or an HTTPS personal access token, or an SSH key). Without push access, the work stays local.
4. Upload or paste this file as the first message. Type `/cost` after each chapter to see what it cost.

---

## 1. The repository and the branch (use exactly these; never create another branch)

* Repository: `https://github.com/dsr001001/modular_math_book`
* Branch: **`claude/textbook-paper-prerequisites-clhh5a`**. All work so far is on it and all further work goes on
  it. Do not create a new branch, do not open a pull request, do not rebase or force-push.

First steps, in a shell:

```
# if the repository is not yet on this machine:
git clone https://github.com/dsr001001/modular_math_book.git
cd modular_math_book
git checkout claude/textbook-paper-prerequisites-clhh5a
git pull origin claude/textbook-paper-prerequisites-clhh5a
tools/setup_env.sh
```

`tools/setup_env.sh` installs TeX Live, pandoc, poppler (via apt, so Debian or Ubuntu or WSL; on a Mac install
MacTeX, pandoc, poppler and `pip install cypari2` by hand and download the ecdata files as the script does),
the Python package cypari2 (PARI/GP), and Cremona's ecdata files for conductor below 10,000 into `data/ecdata/`
(git-ignored). It ends with a smoke test that builds Appendix A and must print `RESULT: OK`.

Before every push: `git pull origin claude/textbook-paper-prerequisites-clhh5a` (merge, never rebase), then
`git push -u origin claude/textbook-paper-prerequisites-clhh5a`; on a network failure retry up to four times
with waits of 2, 4, 8 and 16 seconds.

Commit messages end with the line:
`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`

---

## 2. What the project is

A modular graduate textbook (LaTeX) that takes a reader with first courses in real analysis, linear algebra and
complex analysis, basic statistics and Riley-Hobson-Bence to the point of reading, with full understanding, the
research note "Local factors of the adjoint L-function and the l-adic valuations of the modular degree"
(D. Soni). The original paper is `note_Oct10_7pm.tex`; the revised version with the stronger results is
`paper/note_v2.tex` (same labels; follow the revised version). The book is read online and used by experts as a
reference: every chapter opens with a card of precise statements.

Key files:

| File | What it is |
|-|-|
| `PLAN.md` | master plan: table of contents (Section 4), conventions (7.1 to 7.4), **binding decisions (7.5)**, production process (8), **progress and measured cost (9)** |
| `CONTINUE.md` | status table and how-to (keep it current) |
| `outlines/chNN_slug.md` | the specification of each chapter (all 22 done) |
| `outlines/chB_notation.md` | binding conventions B-C1 to B-C16 (Part 1) and the symbol index (Part 2) |
| `important/paper_memo.md` | corrections and strengthenings of the paper (never repeat a listed error) |
| `important/important_notes.md` | full record of findings (points 1 to 83, book-internal notes B1 to B28) |
| `tools/workflows/write_chapters.js` | the chapter pipeline (write, review, fix, check) |
| `tools/build_chapter.sh NN`, `tools/lint.py`, `tools/build.sh` | build one chapter, lint, build the book |
| `chapters/` | written: `chA_prereq.tex` (Appendix A), `ch10_reduction.tex` (Chapter 10, the pilot) |

---

## 3. Where things stand

| Item | State |
|-|-|
| Outlines of Chapters 1 to 22 and Appendix B, bibliography (refs.bib, bib/chNN.bib), memo, revised paper | done |
| Decision D3 applied to the outlines; Chapter 18 hedge settled by point 73 | done |
| Appendix A (prerequisites) | done, 994 lines, compiles |
| Chapter 10 (pilot) | done: 2,344 lines, 48 pages, compiles, lint clean, three review rounds |
| **Chapter 1** | **not written** (see Section 4, first step) |
| Chapters 2 to 9, 11 to 22, Appendix B, preface update | not written |

Pilot lessons (PLAN.md Section 9): the outline predicts length well (about 2,200 lines per chapter); reviews
found real errors in every round; the full pipeline cost about USD 31 to 35 per chapter on Opus 5.5, almost all
of it context re-read on every tool call, so budget mode (`args.lean: true`) was added, expected USD 12 to 18 per
chapter (not yet measured).

---

## 4. Your task

Write the chapters in this order, **one chapter per run**, starting from Chapter 2:

1. **First check Chapter 1.** If `chapters/ch01_groups.tex` does not exist, ask the human once whether to write
   Chapter 1 first (it was planned before Chapter 2) or to skip it for now; follow the answer.
2. Part I: Chapters 2, 3, 4. Then Part II: 5, 6, 7. Part III: 8, 9, 11 (10 is done). Part IV: 12 to 15. Part V:
   16 to 19. Part VI: 20, then 21 and 22 last (they cite every other chapter's items).
3. Then Appendix B from `outlines/chB_notation.md`, then update `frontmatter/preface.tex`.
4. At the end: build the whole book with `tools/build.sh`; upgrade chapter-level cross-references in Chapters 21
   and 22 to item-level labels; a completeness check of the paper against all the cards; re-verify the
   bibliography.

Chapter numbers, slugs and titles are in `PLAN.md` Section 4 (the outline file names give the slugs:
`outlines/ch02_rings.md` means num "02", slug "rings").

**After the first chapter of this session, stop** and report to the human: lines, pages, review findings, new
paper points, and ask them to type `/cost`. Continue only when they say so. After that, keep going chapter by
chapter, reporting briefly after each, unless the human asks you to stop.

---

## 5. How to write a chapter (the same way as the previous sessions)

**With the Workflow tool** (preferred; the human has opted into multi-agent orchestration for this work):

```
Workflow({ scriptPath: "tools/workflows/write_chapters.js",
           args: { lean: true,
                   repo: "<absolute path of the repository on this machine>",
                   chapters: [ { num: "02", slug: "rings", title: "<title from PLAN.md Section 4>" } ] } })
```

* Always pass `repo` (the script's default is the path of the old cloud container, `/home/user/modular_math_book`).
* `lean: true` is budget mode: each agent reads only what it needs; one combined mathematical and editorial review,
  one fix, one check of the fixes, and a second fix only if the check finds a blocking or major problem. Use it
  unless the human asks for the full pipeline (omit `lean`: two reviews, up to three rounds, about twice the cost).
* One chapter per run while the budget is tight.
* If the session is interrupted, resume with `resumeFromRunId` (finished agents are replayed from cache), and
  first commit whatever partial chapter file exists, as "Work in progress".

**Without the Workflow tool:** run the same stages by hand with sub-agents (Agent tool), one after another,
using the prompt texts in `tools/workflows/write_chapters.js` (the lean variants: `CONTEXT_LEAN`, `writePrompt`,
`combinedReviewPrompt`, `fixPrompt`, `checkPrompt`), with `${REPO}` replaced by the repository path. Sub-agents
never run git; you commit.

**After each chapter (you, not the agents):**

1. Check it yourself: `tools/build_chapter.sh NN` prints `RESULT: OK`; `python3 tools/lint.py chapters/chNN_slug.tex`
   prints clean; look at the first page of `build/chNN/chapter.pdf`.
2. Record the agents' findings: new problems in the paper go to `important/important_notes.md` (next point
   number after 83) and, if significant, to `important/paper_memo.md` Section F; book-internal notes go to the
   "Book-internal consistency" part of important_notes.md (next after B28); book-wide decisions go to
   `PLAN.md` Section 7.5.
3. Bibliography rule B14: a key cited by more than one chapter (or by the paper) belongs in `refs.bib`, never in a
   chapter bib file; never define a key twice.
4. Update the status: the table in `PLAN.md` Section 9 and the table in `CONTINUE.md` Section 1 (chapter, lines,
   pages, review history, cost if the human reported it).
5. Commit and push (Section 1). Never leave work uncommitted at the end of a turn.

---

## 6. Rules every chapter must follow (from PLAN.md Section 7; binding)

* **Typography: no em dash or en dash in any form**, never the characters themselves and never `---` or `--`
  (outside BibTeX page ranges); ASCII-only source. The same holds for every file you write, including notes.
* One file per chapter, `chapters/chNN_slug.tex`; no macros defined in chapters (only those of `preamble.tex`);
  labels `kind:slug:name`; cross-chapter references only `\Cref{ch:slug}`.
* Structure: `\chapter{...}\label{ch:slug}`; "Core results at a glance" (precise statements with rigour tags and
  references); "Where the paper uses this chapter"; the outline's sections with `paperlink` environments;
  Exercises (8 to 20); Notes and references.
* Rigour: full proofs for "proved here"; sketches labelled as sketches with precise references; never present a
  sketch as a proof. Verify every printed computation with PARI (cypari2) and the ecdata files.
* Appendix B conventions B-C1 to B-C16 are binding: Frob arithmetic, Phi = Frob^{-1} geometric, L-factors use
  Phi; duals `^vee`, `^*`, `^D`, adjoint `^dagger`; `J_f` for the abelian variety, `A_f` for the adjoint;
  component groups always with an argument, `\Phig_q` for the geometric one.
* Decisions D1 to D4 (PLAN.md 7.5): D1 state the book's stronger results as the theorems, with a Commentary giving
  the paper's statement; D2 length is a guideline, not a cap (online book), never padding; D3 quadratic
  characters by discriminant, `\chi_{q^*}`, never `\chi_q` (which appears only when quoting the paper), `\chi_\ell`
  is the cyclotomic character; D4 Manin constant `c_E > 0`. Also B2 (Jordan-Holder proved in Chapter 3), B17
  (lem:crit proved in Chapter 15), B14 (bibliography), B24 (Appendix B binding).
* Never repeat an error of the paper listed in `important/paper_memo.md`.
* Known tool facts (from the pilot): PARI 2.17.2 `ellinit(E, O(2^k)).tate` is wrong at q = 2 when v_2(j) = -1
  (use the q(j) series); `ellglobalred(E)[5]` gives `[f,k,0,c]`; the local ecdata files have no per-prime Kodaira
  symbols (recompute with `elllocalred`); data available locally is conductor below 10,000 only, so print every
  count with that range.

---

## 7. Budget

The human has about USD 100 of Console credit. Expected cost in budget mode: about USD 12 to 18 per chapter (to
be confirmed on the first chapter), so about 5 to 7 chapters. Work economically yourself too: do not read
large files in full when a grep will do; delegate reading to the agents; keep your own context small. If the
first chapter costs more than about USD 20, say so and propose cuts before continuing (for example skipping the
check stage for the easiest chapters of Part I).

---

## 8. Open items that need a human (do not try to settle these)

The author must review every new proof in the revised paper (`paper/CHANGES_v2.md` lists them), the six
placeholder tables in `paper/tables/`, and the items of `important/paper_memo.md` Section E. Report anything new
of this kind to the human instead of acting on it.
