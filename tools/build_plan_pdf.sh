#!/usr/bin/env bash
# Build docs/book_plan.pdf: overview, PLAN.md, all chapter outlines, Appendix B outline.
# Requires pandoc and TeX Live (see tools/setup_env.sh).
set -u
cd "$(dirname "$0")/.."
W=build/plan
mkdir -p "$W"
conv() { pandoc "$1" -f markdown+tex_math_dollars-raw_tex+pipe_tables -t latex --top-level-division=chapter -o "$2"; }
conv docs/plan_front.md "$W/front.tex"
conv PLAN.md "$W/plan.tex"
: > "$W/outlines.tex"
for f in outlines/ch[0-9][0-9]_*.md outlines/chB_*.md; do
  b=$(basename "$f" .md); conv "$f" "$W/$b.tex"; echo "\\input{$b.tex}" >> "$W/outlines.tex"
done
cat > "$W/book_plan.tex" <<'TEX'
\documentclass[10pt,oneside]{book}
\input{preamble.tex}
\usepackage{calc}
\usepackage{fvextra}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\setlength{\emergencystretch}{3em}
\sloppy
\title{From First Courses to the Modular Degree\\[1ex]\large Book plan and chapter outlines}
\author{}
\date{15 October 2026}
\begin{document}
\maketitle
\tableofcontents
\input{front.tex}
\part{The master plan}
\input{plan.tex}
\part{Chapter outlines}
\input{outlines.tex}
\end{document}
TEX
export TEXINPUTS="$(pwd)/$W:$(pwd):"
( cd "$W" && pdflatex -interaction=nonstopmode book_plan.tex > pass1.log 2>&1; pdflatex -interaction=nonstopmode book_plan.tex > pass2.log 2>&1; pdflatex -interaction=nonstopmode book_plan.tex > pass3.log 2>&1 )
grep -c '^!' "$W/book_plan.log"
grep -o 'Output written on .*' "$W/book_plan.log"
cp "$W/book_plan.pdf" docs/book_plan.pdf 2>/dev/null && echo "copied to docs/book_plan.pdf"
