#!/usr/bin/env bash
# Set up a fresh container to build and write the book.
# Installs TeX Live, pandoc and poppler, the Python PARI bindings (cypari2), and downloads
# Cremona's ecdata files for conductor below 10,000 into data/ecdata (git-ignored).
# Usage: tools/setup_env.sh        (takes a few minutes; run once per container)
set -u
cd "$(dirname "$0")/.."
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq --no-install-recommends \
  texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-science \
  texlive-fonts-recommended texlive-bibtex-extra lmodern fonts-lmodern latexmk biber \
  pandoc poppler-utils > /tmp/setup_apt.log 2>&1 || { echo "apt failed, see /tmp/setup_apt.log"; exit 1; }
mktexlsr > /dev/null 2>&1
pip install -q cypari2 || pip install -q --break-system-packages cypari2
python3 -c "import cypari2; p=cypari2.Pari(); print('PARI', p('default(version)'))"
mkdir -p data/ecdata
# Pinned to the ecdata commit the paper and the book use (Chapter 22); checksums in tools/ecdata.sha256.
COMMIT=25cec5ecfec8b9f016eb1631ac633194c2bed39f
fetch() {  # fetch <repo path> <local file>
  [ -s "$2" ] && return
  for wait in 0 2 4 8 16 32; do
    sleep $wait
    curl -sS -f -m 120 -o "$2" "https://raw.githubusercontent.com/JohnCremona/ecdata/$COMMIT/$1" && break
  done
  [ -s "$2" ] && echo "downloaded $2" || echo "FAILED $2"
}
for d in allcurves allbsd allisog alllabels degphi galrep alldegphi curvedata classdata opt_man; do
  fetch "$d/$d.00000-09999" "data/ecdata/$d.00000-09999"
done
fetch "docs/file-format.txt" "data/ecdata/file-format.txt"
(cd data/ecdata && sha256sum -c --quiet ../../tools/ecdata.sha256) && echo "ecdata checksums OK" || echo "ecdata CHECKSUM MISMATCH"
echo "smoke test:"; tools/build_chapter.sh A | tail -1
