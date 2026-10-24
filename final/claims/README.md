# Claim ledger for the paper

A machine-readable list of what `../paper/note.tex` (*Local factors of the adjoint L-function and the l-adic valuations
of the modular degree*) claims, how each claim is supported, and where the book (`../book/chapters/`) and the pipeline
(`../pipeline/`) treat it. Nothing in `../paper` or `../book` was edited to build it.

| file | content |
|---|---|
| `claims.csv` | the ledger: UTF-8, comma-separated, one header row, 14 columns, 124 rows |
| `claims.yaml` | the same rows in the same order (a list of mappings; every value a double-quoted string) |
| `scripts/check_claims.py` | the validator (below) |

## Rows

- **Statements** (`P-`, 49 rows; kind `statement`, except `P-ex:qual`, kind `example`): every numbered statement of the paper (definition, theorem, proposition, lemma,
  corollary, conjecture, example, and every remark that asserts something, the two unlabeled remarks included), plus the
  five key displays `eq:identity`, `eq:thm`, `eq:rule`, `eq:main`, `eq:twist`.
- **Computational claims** (`C-`, 56 rows): every table (`tab:excess`, `tab:uniform`, `tab:iso`, `tab:counts`, `tab:ns`,
  `tab:isolated` split into its untwisted and twisted rows, `tab:oot`) and each counted statement in the text of
  Sections 1, 6 and 7. A few counted statements outside those sections are included because they are of the same kind:
  the data paragraph after `thm:twist`, the level-539 sentence after `lem:step1`, the counts after
  `prop:ns-structure`, the PARI check in the proof of `lem:euler`, the 30-digit check in `rem:degree`, open questions 2
  and 6, and the appendix's two checks.
- **Named examples** (`X-`, 19 rows, kind `example`): 121a1, 539c1, 539d1, 1232l1, 592c1, 336f1, 726a1, 990h1, 990h3, 11a1, 121d2, 52a1,
  980i1, 99a1, 1184f1, 1748e1, 14a1, 714i1, 6942n1 (and the CM pair 27a1, 243b1 inside `C-sec:two:cm-odd`).

## Columns

| column | content |
|---|---|
| `id` | stable identifier: `P-<paper label>` for a statement; `C-<paper label>` for a table, `C-<anchor label>:<slug>` for a sentence; `X-<Cremona label>` for a curve. The unlabeled remarks are `P-rem:after-ex:qual` (Remark 3.4) and `P-rem:after-prop:integral` (Remark 4.2). |
| `kind` | `statement`, `computation` or `example` |
| `paper_label` | a `\label` of `note.tex`: the statement's own label, or for a sentence the label of the enclosing (sub)section, table, equation or statement (the anchor) |
| `paper_page` | the page of `paper_label` in `note.aux` (`\newlabel`). For an anchor this is the page where the anchor starts; when the sentence itself is on another page of `note.pdf`, `notes` says so |
| `short_statement` | a faithful paraphrase, at most 200 characters, ASCII notation (`l` for ell, `deg phi` for the modular degree, `x` for tensor) |
| `hypotheses` | for a statement its hypotheses; for a computation the population and range |
| `status` | see below |
| `imported_from` | citation key of `../paper/refs.bib` and item (e.g. `DFG04 Theorem 3.7`), for imported statements and for the published results a proof uses; numbering as cited by the paper (Ch.21 records which were compared with the published text) |
| `book_location` | `;`-separated items `<chapter label> <book label>`: the book's own statement or paperlink of the result (found by searching the chapters for environments and paperlinks naming the paper label), then the Ch.21 tour entry |
| `script` | `;`-separated paths under `final/pipeline` (`scripts/...`), or `book:<name>` for a script the book prints or names in Chapter 22 (`sessions.gp`, `table_small.gp`, `compute.py`, `common.py`, `tam.py`, `moddeg_check.py`); the book's scripts are not files of this repository |
| `output` | `;`-separated result files under `final/pipeline` (`results/`, `tables/`, `samples/`) |
| `evidence` | for computational rows only (kind computation or example, or status computed or empirical); see below |
| `human_review` | `not yet` for every row: no row has been reviewed by the author |
| `notes` | what the evidence consists of, caveats, cross-references to other rows |

### Status vocabulary

| status | meaning |
|---|---|
| `proved-in-paper` | the paper gives a proof (possibly using published results listed in `imported_from`) |
| `proved-in-book` | the paper asserts it without proof and the book proves it (`P-def:terms` properties, `P-rem:types`) |
| `imported` | the paper cites it without proof (`thm:dfg14`, `thm:dfg37`, `thm:dfg27`, `lem:dfg21`, `lem:fpr`, `rem:free`, `rem:ko`) |
| `conjectural` | stated as a conjecture or as a conditional derivation whose hypotheses are open (`conj:euler`, `eq:rule`, `conj:eis`, `rem:ns`) |
| `empirical` | a regularity supported only by data and not explained (`eq:main`, `eq:twist` outside `prop:forms`, `rem:oq1`, the weights `w_3`, the `p = -1 mod 3` pattern, the 2-adic minima) |
| `computed` | a finite fact established by computation: a count on a stated range, a table entry, a value for a named curve |

### Evidence vocabulary

| evidence | meaning, as applied here |
|---|---|
| `quoted` | the number is only stated in the paper: no committed result file contains it and nothing in this repository reproduced it |
| `saved-output` | the number agrees with a committed file under `final/pipeline/results`, `tables` or `samples`, checked by `scripts/selftest.py` (tables) or by reading the file; the computation behind it was not rerun here |
| `regenerated` | rerun in this repository: the full rerun of the pipeline from the pinned data on 2026-10-24 (PARI 2.17.2; stages 1 and 2 reproduced every committed summary and table file byte for byte, stage 3 recomputed the numbers without a committed source; `../pipeline/README.md`, section "Full rerun"), `scripts/selftest.py` and `scripts/wild_euler_samples.py`, and the book's own recomputations below conductor 10,000 (Chapters 18, 20, 21, 22) |
| `independently-recomputed` | an independent implementation agreed with the claim |

Rules used:

- **One level per row, the weakest that covers the whole claim.** Where part of a sentence is in a committed file and
  part is not, the row takes the lower level and `notes` says which part is supported (e.g. `C-sec:iso:minima`: the l = 3
  file was regenerated, the l = 5, 7 files were not, so the row is `saved-output`).
- **The large-range computations were rerun.** A row over the working set, hold-out or extension is `regenerated` when
  the full rerun of 2026-10-24 reproduced the result file behind it byte for byte (stages 1 and 2:
  `results/check_*_summary.csv`, `step10_rule_*`, `step11_*`, `step12_work.csv`, `step9_euler_l3.txt`,
  `step7_twist2_*.txt`, the configuration lines of `step6_u1_fit_work.txt` and the table files; logs in
  `../pipeline/results/rerun_20261024/`) or when stage 3 recomputed its numbers (`../pipeline/results/stage3_*`,
  summary `stage3_summary.md`). Rows resting on files of the exploratory stage that the rerun does not regenerate
  (`step7_equality2_work.txt`, `step7_twist_test.txt`, `step6_u1c_work.txt`, `step9_euler_l{5,7}.txt`) stay
  `saved-output`. `results/repro_check2.log` records an earlier rerun of stage 1 in the source repository; it is
  mentioned in `notes`, not counted.
- **Stage 3 recomputed what the paper states and the rest of the pipeline does not record.** Two of its results differ from
  the earlier wording of the paper, which `../paper/note.tex` corrects: 19, not 20, exceptions on the extension in
  `C-sec:two:I0star`, and the 18 curves with a point of order 9 in `C-sec:eis:deficits` are all curves, optimal or not.
  For `C-sec:data:moddeg15` the fifteen curves are not named, so a sample of 63 curves stands in for them; for
  `C-lem:euler:pari` the recomputed population is the optimal curves of the three in-table ranges.
- **The book's runs below 10,000 are `regenerated`, not `independently-recomputed`.** The book's Chapter 22 code is
  separate from the pipeline scripts, but the paper's AI statement says that its checks below conductor 10,000 were
  worked out while writing the book, so the book's run is plausibly the source of those printed numbers. The single
  `independently-recomputed` row is `C-sec:data:ellmoddegree`, whose claim is itself the agreement of two independent
  implementations (PARI's `ellmoddegree` against Cremona's `degphi`), rerun by the book on all 38,042 curves.
- A book reproduction of an *analogue* on a smaller range (e.g. Table `tab:uniform` below 10,000) does not raise the
  level of a large-range row; it is mentioned in `notes`.

Counts (from `scripts/check_claims.py`):

| | |
|---|---|
| by kind | statement 48, computation 56, example 20 |
| by status | proved-in-paper 30, proved-in-book 2, imported 7, conjectural 4, empirical 6, computed 75 |
| by evidence | regenerated 73, saved-output 6, quoted 1, independently-recomputed 1, none (non-computational statements) 43 |

## Points for review

- `C-sec:forms:hypothesis`: in `../pipeline/results/step6_u1c_work.txt` the 913,244 pairs split as 281,739 (l >= 5,
  l not dividing N) + 175,798 (l >= 5, l | N) + 455,707 (l = 3, all pairs). The file does not separate the l = 3 pairs by
  whether 3 | N, so it does not support the paper's reading of 455,707 as pairs where the hypothesis fails because l | N.
- The one row that stays `quoted`: `P-rem:after-ex:qual` (its closing data sentence has no committed output; the
  congruence numbers in it were recomputed in the book).
- Rows that stay `saved-output` because their result files come from exploratory scripts outside the rerun:
  `C-sec:sharp:oddpart`, `C-sec:forms:equality` (`step7_equality2.py`), `C-sec:iso:two-II` (`step7_twist_test.py`),
  `C-sec:forms:hypothesis` (`step6_u1c.py`), `C-sec:iso:minima` (`step9_euler.py` at l = 5, 7), and
  `C-app:repro:twist-lemma` (`twist_lemma_check.gp`, PARI 2.15.4 output, not rerun).
- `C-tab:excess` is written by no pipeline script; its only recorded computation is the book's Chapter 18.
- `P-rem:after-prop:integral` is marked `proved-in-paper` on the strength of a sketch; no book proof was traced.

## How it was built

By reading `../paper/note.tex` in full, `../pipeline/README.md`, `ENVIRONMENT.md`, `PROVENANCE.md`,
`results/selftest.log`, `samples/README.md`, Chapters 21 and 22 of the book (and the passages of Chapters 18 and 20 that
recompute paper numbers), and by searching the committed result files for each printed number. Book locations were found
by searching all chapters for environments whose title, or paperlinks whose text, names the paper label. Pages were
taken from `../paper/note.aux` (compiled 2026-10-24, not older than `note.tex`); the sentence pages in `notes` from
`pdftotext` of `../paper/note.pdf`. The rows were written by hand into `claims.csv`; `claims.yaml` is generated from it.

## How to check it

```
python3 final/claims/scripts/check_claims.py               # from the repository root, or with any working directory
python3 final/claims/scripts/check_claims.py --write-yaml  # after editing claims.csv
python3 final/claims/scripts/check_claims.py --compile     # recompile note.tex (latexmk) into a temporary directory first
```

The validator checks that every `paper_label` is a `\label` of `note.tex` and that `paper_page` equals its page in
`note.aux` (recompiling into a temporary directory when `note.aux` is older than `note.tex`; the paper directory is not
written to), that every book location names a chapter label and a label defined in that chapter's file, that every
script and output path exists under `final/pipeline` (and every `book:` script is named in the book), that `status` and
`evidence` are in their vocabularies and present exactly when required, that `imported_from` is filled for imported
rows, that each `short_statement` has at most 200 characters, and that `claims.yaml` equals `claims.csv`. It prints the
counts above and exits nonzero on any failure. It needs Python 3 (PyYAML optional, used as a cross-check) and, only
when the aux is stale, `latexmk`.
