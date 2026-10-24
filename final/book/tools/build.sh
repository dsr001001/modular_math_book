#!/usr/bin/env bash
# Build the whole book into build/main/main.pdf.
set -u
cd "$(dirname "$0")/.."
mkdir -p build/main
export TEXINPUTS=".:$(pwd):"
export BIBINPUTS=".:$(pwd):$(pwd)/bib:"
latexmk -pdf -interaction=nonstopmode -output-directory=build/main main.tex > build/main/latexmk.out 2>&1
STATUS=$?
LOG=build/main/main.log
echo "=== main.tex: latexmk exit status $STATUS ==="
grep -n -A3 '^!' "$LOG" | head -60
echo "--- undefined references / citations ---"
grep -n -E "Reference .* undefined|Citation .* undefined|multiply defined" "$LOG" | head -60
grep -o "Output written on .*" "$LOG" | tail -1
exit $STATUS
