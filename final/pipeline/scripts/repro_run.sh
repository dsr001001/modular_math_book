#!/usr/bin/env bash
# Stage 1 of the reproduction: from Cremona's ecdata (pinned commit) to the checker summaries of Table tab:counts.
#   1. download the pinned ecdata snapshot into data/raw (scripts/download_ecdata.sh; skips files already present)
#   2. PARI/GP pass over every allcurves file (scripts/pari_features.gp) -> data/pari/{curves,ap}.*.tsv
#   3. python3 scripts/build_features.py -> data/curves.parquet, data/ap.parquet
#   4. the optimal curves of the three in-table ranges -> results/optimal_{work,holdout,ext}.parquet
#   5. python3 scripts/conj_check.py on each range -> results/check_{work,holdout,ext}_{summary.csv,perl.parquet}
#   6. diff of the regenerated summaries against the committed ones (copied to the run directory before step 5)
# Row counts are checked after every stage; any failure or difference ends the run with a nonzero exit status.
# Usage (from anywhere):  bash scripts/repro_run.sh
# Environment: GP (gp binary, default gp), PYTHON (default python3), JOBS (parallel gp processes, default 2).
# Log and reference copies: logs/repro_run_<UTC time>/ under the pipeline directory.
set -euo pipefail

PIPE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PIPE"
GP=${GP:-gp}; PYTHON=${PYTHON:-python3}; JOBS=${JOBS:-2}
RUN="$PIPE/logs/repro_run_$(date -u +%Y%m%dT%H%M%SZ)"; mkdir -p "$RUN/ref"
LOG="$RUN/repro_run.log"
exec > >(tee -a "$LOG") 2>&1
die() { echo "[repro] FAILED: $*"; exit 1; }
say() { echo "[repro] $(date -u +%H:%M:%S) $*"; }

# Expected counts (../paper/note.tex, Section sec:data and Table tab:counts)
N_CURVES=3064705            # curves of conductor below 500000 in the pinned tables
N_CLASSES=2164260           # isogeny classes (rows of data/ap.parquet)
N_WORK=1311066; N_HOLDOUT=429936; N_EXT=359009
ECDATA_SHA=25cec5ecfec8b9f016eb1631ac633194c2bed39f

say "pipeline directory: $PIPE"
say "log: $LOG"
command -v "$GP" > /dev/null || die "gp binary '$GP' not found (PARI/GP is required for scripts/pari_features.gp)"
say "gp version: $(echo 'print(version())' | "$GP" -q)"
"$PYTHON" -c "import numpy, pandas, pyarrow; print('[repro] python', __import__('sys').version.split()[0], 'numpy', numpy.__version__, 'pandas', pandas.__version__, 'pyarrow', pyarrow.__version__)"

# reference copies of the committed summaries, taken before anything is overwritten
for s in work holdout ext; do cp "results/check_${s}_summary.csv" "$RUN/ref/"; done

# 1. data
say "download (pinned ecdata $ECDATA_SHA)"
bash scripts/download_ecdata.sh data/raw > "$RUN/download.log" 2>&1 || die "download_ecdata.sh exited nonzero (see $RUN/download.log)"
[ "$(cat data/raw/ECDATA_COMMIT)" = "$ECDATA_SHA" ] || die "data/raw/ECDATA_COMMIT is not $ECDATA_SHA"
for d in allcurves allgens allbsd alldegphi opt_man intpts 2adic galrep allisog; do
  n=$(find "data/raw/$d" -maxdepth 1 -type f -size +0 | wc -l)
  [ "$n" -eq 50 ] || die "data/raw/$d has $n non-empty files, expected 50"
done
# download_ecdata.sh reports failed files as "FAIL <url>" and does not stop; iwasawa exists upstream only below 150000.
# Failures are tolerated only for files that build_features.py does not read (checked by the counts above).
awk '/^FAIL/ { if ($0 ~ /\/iwasawa\//) i++; else { n++; if (n <= 20) print "    " $0 } }
     END { printf "[repro] download failures: %d iwasawa (expected), %d other\n", i, n }' "$RUN/download.log"
n=$(cat data/raw/allcurves/allcurves.* | wc -l)
[ "$n" -eq "$N_CURVES" ] || die "allcurves has $n rows, expected $N_CURVES"
say "download done: allcurves rows $n"

# 2. PARI features (write() appends, so old outputs are removed first)
mkdir -p data/pari; rm -f data/pari/curves.*.tsv data/pari/ap.*.tsv
pari_block() {
  local f=$1 r=${1#allcurves.} out
  out=$(printf 'infile="data/raw/allcurves/%s"; outc="data/pari/curves.%s.tsv"; outa="data/pari/ap.%s.tsv"; read("scripts/pari_features.gp"); print("PARI_BLOCK_OK")\n' \
        "$f" "$r" "$r" | "$GP" -q -s 256M 2>&1) || { echo "[repro] gp exited nonzero on $f"; printf '%s\n' "$out"; return 1; }
  printf '%s\n' "$out" | sed '/Warning/d; /^PARI_BLOCK_OK$/d'
  grep -q '^PARI_BLOCK_OK$' <<< "$out" || { echo "[repro] gp did not complete $f"; return 1; }
}
export -f pari_block; export GP
say "PARI features ($JOBS parallel gp processes)"
ls data/raw/allcurves/ | xargs -P "$JOBS" -I{} bash -c 'pari_block "$1" || exit 255' _ {} || die "PARI feature pass"
n=$(cat data/pari/curves.*.tsv | wc -l); [ "$n" -eq "$N_CURVES" ] || die "data/pari/curves.*.tsv has $n rows, expected $N_CURVES"
n=$(cat data/pari/ap.*.tsv | wc -l);     [ "$n" -eq "$N_CLASSES" ] || die "data/pari/ap.*.tsv has $n rows, expected $N_CLASSES"
say "PARI features done: $N_CURVES curves, $N_CLASSES classes"

# 3. feature table
say "build_features.py"
"$PYTHON" scripts/build_features.py 2>&1 | sed '/Warning/d'
"$PYTHON" - "$N_CURVES" "$N_CLASSES" <<'EOF'
import sys, pyarrow.parquet as pq
nc, na = (pq.ParquetFile(f).metadata.num_rows for f in ("data/curves.parquet", "data/ap.parquet"))
print(f"[repro] data/curves.parquet rows {nc}, data/ap.parquet rows {na}")
sys.exit(0 if (nc, na) == (int(sys.argv[1]), int(sys.argv[2])) else "[repro] FAILED: row counts of the feature tables")
EOF

# 4. optimal curves of the three ranges (Section sec:data: optimality known for every class up to 400000 and for
#    359,009 classes in the extension range, which is restricted to those)
"$PYTHON" - "$N_WORK" "$N_HOLDOUT" "$N_EXT" <<'EOF'
import os, sys, pandas as pd
cols = ["label", "N", "moddeg", "kodaira", "tamagawa_list", "max_isogeny_degree", "is_cm", "torsion", "galrep_images", "optimal", "optimal_known"]
df = pd.read_parquet("data/curves.parquet", columns=cols); opt = df[df.optimal == 1]
os.makedirs("results", exist_ok=True); bad = []
for (name, d), want in zip([("work", opt[opt.N <= 300000]), ("holdout", opt[(opt.N > 300000) & (opt.N <= 400000)]),
                            ("ext", opt[(opt.N > 400000) & (opt.N <= 500000) & opt.optimal_known])], map(int, sys.argv[1:])):
    d.drop(columns=["optimal", "optimal_known"]).to_parquet(f"results/optimal_{name}.parquet", index=False)
    print(f"[repro] optimal {name}: {len(d)} (expected {want})")
    if len(d) != want: bad.append(name)
sys.exit(f"[repro] FAILED: optimal-curve counts {bad}" if bad else 0)
EOF

# 5. checker
for s in work holdout ext; do
  say "conj_check.py $s"
  "$PYTHON" scripts/conj_check.py "results/optimal_$s.parquet" --out "results/check_$s" 2>&1 | sed '/Warning/d'
done

# 6. comparison with the committed summaries
fail=0
for s in work holdout ext; do
  if diff -u "$RUN/ref/check_${s}_summary.csv" "results/check_${s}_summary.csv"; then
    say "results/check_${s}_summary.csv IDENTICAL to the committed version"
  else
    say "results/check_${s}_summary.csv DIFFERS from the committed version (kept in $RUN/ref)"; fail=1
  fi
done
[ "$fail" -eq 0 ] || die "regenerated summaries differ from the committed ones"
say "OK: all counts and summaries reproduced. Next: bash scripts/reproduce_tables.sh"
