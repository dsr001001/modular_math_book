# Modular Math Book

A modular textbook that takes a reader with a first course in real analysis, a first course in linear
algebra, an introduction to complex analysis, basic statistics and Riley-Hobson-Bence to the point of
reading the research note

> *Local factors of the adjoint L-function and the l-adic valuations of the modular degree*

(the final versions of the paper, the book and the computational pipeline are in `final/`; see `final/README.md`). Each chapter opens with a "Core results at a glance" card so
that an expert can use the book as a refresher.

* `PLAN.md`: the master plan (audience, table of contents, chapter scopes, paper-to-chapter map, writing
  conventions, production process). Read it first.
* `main.tex`, `preamble.tex`: the book; `chapters/chNN_slug.tex`: one file per chapter.
* `outlines/`: the line-up of core results for each chapter, produced before the chapter was written.
* `refs.bib`, `bib/chNN.bib`: bibliography (shared and per chapter).
* `tools/build_chapter.sh NN`: compile one chapter alone; `tools/lint.py`: check conventions;
  `tools/build.sh`: build the whole book into `build/main/main.pdf`.

Build requirements: TeX Live with `latexmk`, `amsmath`, `cleveref`, `enumitem`, `listings`, `microtype`.
