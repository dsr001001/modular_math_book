#!/usr/bin/env bash
# Compile one chapter on its own, with the shared preamble and bibliography.
# Usage: tools/build_chapter.sh NN        (NN = 01 ... 22, A, B)
# Output: build/chNN/chapter.pdf and build/chNN/chapter.log; exit status 0 iff no LaTeX errors
# and no undefined references or citations.
set -u
cd "$(dirname "$0")/.."
NN="$1"
FILE=$(ls chapters/ch${NN}_*.tex 2>/dev/null | head -1)
if [ -z "$FILE" ]; then echo "no file chapters/ch${NN}_*.tex"; exit 2; fi
BASE=$(basename "$FILE" .tex)
OUT="build/ch${NN}"
mkdir -p "$OUT"
# Register the labels of every other chapter (so that \Cref{ch:slug} resolves) by stepping the
# chapter counter without typesetting anything; the real chapter is \input at its own position.
SLUGS=(groups rings modules reps galois ant local curves ellcurves reduction galrep modforms hecke moddeg modgalrep cohomology galcoh blochkato lfunctions congruence paper computation)
APPS=(prereq notation)
BEFORE=""; AFTER=""
if [[ "$NN" =~ ^[0-9]+$ ]]; then
  CUR=$((10#$NN))
  for i in "${!SLUGS[@]}"; do
    k=$((i+1)); s=${SLUGS[$i]}
    if [ $k -lt $CUR ]; then BEFORE+="\\refstepcounter{chapter}\\label{ch:$s}"; fi
    if [ $k -gt $CUR ]; then AFTER+="\\refstepcounter{chapter}\\label{ch:$s}"; fi
  done
  AFTER+="\\appendix"
  for s in "${APPS[@]}"; do AFTER+="\\refstepcounter{chapter}\\label{ch:$s}"; done
else
  for s in "${SLUGS[@]}"; do BEFORE+="\\refstepcounter{chapter}\\label{ch:$s}"; done
  BEFORE+="\\appendix"
  case "$NN" in
    A) AFTER="\\refstepcounter{chapter}\\label{ch:notation}" ;;
    B) BEFORE+="\\refstepcounter{chapter}\\label{ch:prereq}" ;;
  esac
fi
SETUP="$BEFORE"
BIBS="refs"
if [ -f "bib/ch${NN}.bib" ]; then BIBS="refs,bib/ch${NN}"; fi
cat > "$OUT/chapter.tex" <<EOF
\\documentclass[11pt]{book}
\\input{preamble.tex}
\\begin{document}
$SETUP
\\input{$FILE}
$AFTER
\\bibliographystyle{amsplain}
\\bibliography{$BIBS}
\\end{document}
EOF
export TEXINPUTS=".:$(pwd):"
export BIBINPUTS=".:$(pwd):$(pwd)/bib:"
export BSTINPUTS=".:"
# latexmk runs pdflatex and bibtex as often as needed
latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory="$OUT" "$OUT/chapter.tex" > "$OUT/latexmk.out" 2>&1
STATUS=$?
LOG="$OUT/chapter.log"
echo "=== build/ch${NN}: latexmk exit status $STATUS ==="
if [ -f "$LOG" ]; then
  echo "--- LaTeX errors (lines starting with '!') ---"
  grep -n -A3 '^!' "$LOG" | head -80
  echo "--- undefined references / citations / multiply defined labels ---"
  grep -n -E "Reference .* undefined|Citation .* undefined|multiply defined|There were undefined" "$LOG" | head -60
  echo "--- overfull boxes (count) ---"
  grep -c "Overfull" "$LOG"
  echo "--- page count ---"
  grep -o "Output written on .*" "$LOG" | tail -1
fi
UNDEF=$(grep -c -E "Reference .* undefined|Citation .* undefined|multiply defined" "$LOG" 2>/dev/null || true)
if [ "$STATUS" -ne 0 ]; then echo "RESULT: FAIL (LaTeX error)"; exit 1; fi
if [ "${UNDEF:-0}" -ne 0 ]; then echo "RESULT: FAIL (undefined references or citations)"; exit 1; fi
echo "RESULT: OK"
exit 0
