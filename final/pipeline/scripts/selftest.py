"""Self-test that runs without the ecdata download (needs python3 with pandas and cypari2 only).

(a) Loads scripts/euler_rule.gp into PARI through cypari2 (no reimplementation) and evaluates rule(E, l) on curves for
    which ../paper/note.tex states the result or the data that fix it; checks ellmoddegree against the degree printed
    in the paper, and PARI's symmetric-square Euler factor at 2 against the polynomials given in the paper.
(b) Checks that the printed tables in tables/ agree with the committed result files in results/:
      tab:uniform  tables/euler_uniform.tex  vs results/step11_summary.csv
      tab:counts   tables/counts.tex         vs results/check_{work,holdout,ext,oot}_summary.csv
      tab:ns       tables/ns3.tex            vs results/step11_ns3.csv
      tab:iso      tables/euler_iso3.tex     vs results/step9_euler_l3.txt
      tab:isolated tables/isolated3.tex      untwisted rows vs results/step6_u1_fit_work.txt (the four twisted rows are
                                             computed from results/step7_twist2_work_l3.parquet, which is not committed)
      tab:oot      tables/oot.tex            vs results/oot_1.tsv, results/oot_2.tsv (deduplicated as in oot_convert.py)
(c) Checks that the body of each of these six tables appears verbatim (up to whitespace) in ../paper/note.tex.

Usage (from final/pipeline):  python3 scripts/selftest.py | tee results/selftest.log
Exit status 0 if every check passes, 1 otherwise."""
import os, re, sys, glob
import pandas as pd
import cypari2

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FAIL = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok: FAIL.append(name)
def skip(name, why): print(f"[SKIP] {name}  ({why})")
def num(s): return int(s.replace(",", "").replace("{,}", "").strip())

# ---------------------------------------------------------------- (a) the rule on single curves
pari = cypari2.Pari(); pari.allocatemem(400_000_000)
print("PARI version:", ".".join(map(str, pari.version())), "| cypari2", __import__("importlib.metadata").metadata.version("cypari2"),
      "| pandas", pd.__version__)
pari('read("scripts/euler_rule.gp")')
# label, a-invariants (Cremona's tables), l, iii, expected rule output, degree printed in the paper, source in the paper
CASES = [
    ("121a1",  "[1,1,1,-30,-76]",           3, 0, [1, 1], 6,    "app:repro: rule(ellinit([1,1,1,-30,-76]),3) returns [1, 1]"),
    ("539c1",  "[1,0,1,170,-3237]",         3, 0, [2, 2], 288,  "thm:qual examples (c): deg = 2^5 3^2, e_3(E,7) = t_3(E,7) = 1, both attained"),
    ("539d1",  "[0,1,1,-16,-66]",           3, 0, [2, 2], 72,   "sec:quant: deg 72, type I_0* at 7 with e_3(E,7) = 2; no violation, so bound = 2"),
    ("1232l1", "[0,0,0,32,-16]",            3, 0, [2, 2], 288,  "rem:wild: e_3(E,2) = 2, deg 288, bound attained by the prime 2 alone"),
    ("592c1",  "[0,0,0,-16,-16]",           5, 0, [1, 1], 80,   "rem:wild: e_5(E,2) = 1, deg 80 = 2^4 5; no violation, so bound = 1"),
    ("726a1",  "[1,1,0,-35,-51]",           3, 0, [2, 2], 144,  "app:repro: rule(E,3) returns [2, 2]"),
    ("726a1",  "[1,1,0,-35,-51]",           3, 1, [2, 2], 144,  "app:repro: rule(E,3,1) returns [2, 2]"),
    ("990h1",  "[1,-1,1,-96608,-11533373]", 3, 0, [4, 3], None, "app:repro: 990h1 (not optimal) returns [4, 3]"),
    ("990h3",  "[1,-1,1,-1568,-4669]",      3, 0, [3, 3], None, "app:repro: the optimal curve 990h3 returns [3, 3]"),
    ("11a1",   "[0,-1,1,-10,-20]",          5, 0, [0, 1], 1,    "app:repro: 11a1 at the Eisenstein prime 5 returns [0, 1]"),
]
print("\n(a) scripts/euler_rule.gp on curves of the paper")
for lab, ai, l, iii, exp, deg, src in CASES:
    got = [int(x) for x in pari(f"rule(ellinit({ai}), {l}, {iii})")]
    check(f"rule({lab}, l={l}{', iii=1' if iii else ''}) = {got}, expected {exp}", got == exp, src)
    if deg is not None and iii == 0:
        d = int(pari(f"ellmoddegree(ellinit({ai}))"))
        check(f"ellmoddegree({lab}) = {d}, paper {deg}", d == deg)
# P_2 of Sym^2 as stated in rem:wild (L_2(Sym^2 f, s) = P_2(2^-s)^-1)
for lab, ai, poly in [("336f1", "[0,1,0,-1,2]", "1+2*x"), ("1232l1", "[0,0,0,32,-16]", "(1-2*x)*(1+2*x)^2"),
                      ("592c1", "[0,0,0,-16,-16]", "(1-2*x)*(1+4*x^2)")]:
    P = pari(f"1/lfuneuler(lfunsympow(ellinit({ai}), 2), 2)")
    check(f"P_2({lab}) = {P}, paper {poly}", bool(pari(f"({P}) == ({poly})")))

# ---------------------------------------------------------------- (b) printed tables vs committed result files
print("\n(b) tables/ against results/")
SETNAME = {"working set": "work", "hold-out": "holdout", "extension": "ext", "out of table": "oot"}
def rows(path):
    """Data rows of a tabular as lists of stripped cells (rules and header excluded); first cell carried forward."""
    out, cur = [], None
    body = open(path).read().split("\\end{tabular}")[0]
    for line in body.splitlines():
        line = line.strip()
        if not line.endswith("\\\\"): continue
        cells = [c.strip() for c in line[:-2].split("&")]
        out.append(cells)
    return out
def pct(x): return float(x.replace("\\%", ""))

# tab:uniform
S = pd.read_csv("results/step11_summary.csv")
n_ok, bad = 0, []
cur = None
for c in rows("tables/euler_uniform.tex")[1:]:
    if c[0]: cur = SETNAME[c[0]]
    r = S[(S.set == cur) & (S.l == int(c[1]))].iloc[0]
    fr = [x.strip() for x in c[7].split("/")]
    ok = (num(c[2]) == r.curves and num(c[3]) == r.bound_pos and int(c[4]) == r.viol and abs(pct(c[5]) - 100 * r["eq"]) <= 0.05 + 1e-9
          and int(c[6]) == r.viol_full and num(fr[0]) == r.noIII_pos and int(fr[1]) == r.viol_noIII and abs(pct(fr[2]) - 100 * r.eq_noIII) <= 0.05 + 1e-9)
    n_ok += ok
    if not ok: bad.append((cur, c[1]))
check(f"tab:uniform  tables/euler_uniform.tex vs results/step11_summary.csv: {n_ok} of {len(S)} rows agree", n_ok == len(S) and not bad, f"mismatch {bad}" if bad else "")

# tab:counts
n_ok, n_rows, bad = 0, 0, []
cur = None
SC = {k: pd.read_csv(f"results/check_{k}_summary.csv").set_index("l") for k in ("work", "holdout", "ext", "oot")}
for c in rows("tables/counts.tex")[1:]:
    if c[0]: cur = SETNAME[c[0].split(",")[0]]
    r = SC[cur].loc[int(c[1])]; n_rows += 1
    eis = [x.strip() for x in c[7].split("/")]
    ok = (num(c[2]) == r.curves and num(c[3]) == r.non_eis_with_bound and num(c[4]) == r.non_eis_with_bound2
          and int(c[5]) == r.viol_conj1 and int(c[6]) == r.viol_conj2 and num(eis[0]) == r.eis_with_bound and int(eis[1]) == r.viol_conj3)
    n_ok += ok
    if not ok: bad.append((cur, c[1]))
expect = sum(int(SC[k].index.isin([3, 5, 7, 11, 13]).sum()) for k in SC)
check(f"tab:counts   tables/counts.tex vs results/check_*_summary.csv: {n_ok} of {expect} rows agree", n_ok == expect == n_rows and not bad, f"mismatch {bad}" if bad else "")

# tab:ns
NS = pd.read_csv("results/step11_ns3.csv").set_index("set")
n_ok, bad = 0, []
for c in rows("tables/ns3.tex")[1:]:
    r = NS.loc[SETNAME[c[0]]]
    m = re.match(r"(\d+) \((\d+)\\%\)", c[3]); h = c[5].split(" of "); q = [int(x) for x in c[6].split("/")]; sh = c[7].split(" of ")
    ok = (num(c[1]) == r.ns3 and num(c[2]) == r.ns3_with_III_term and int(m.group(1)) == r.ns3_failing
          and int(m.group(2)) == round(100 * r.ns3_failing / max(r.ns3, 1)) and int(c[4]) == r.non_ns3_failing
          and num(h[0]) == r.h_eq_1 and num(h[1]) == r.ns3 and q == [r.III_q_1mod12, r.III_q_11mod12, r.III_q_2]
          and int(sh[0]) == r.shortfall_1 and int(sh[1]) == r.exceptions)
    n_ok += ok
    if not ok: bad.append(c[0])
check(f"tab:ns       tables/ns3.tex vs results/step11_ns3.csv: {n_ok} of {len(NS)} rows agree", n_ok == len(NS) and not bad, f"mismatch {bad}" if bad else "")

# tab:iso
iso, ty = {}, None
txt = open("results/step9_euler_l3.txt").read().split("by type and euler term:")[1].split("\n\n")[0]
for line in txt.splitlines()[2:]:
    p = line.split()
    if len(p) == 6: ty = p[0]; p = p[1:]
    if len(p) == 5: iso[(ty, int(p[0]))] = (int(float(p[2])), int(float(p[1])))     # (min V, n)
TEXTY = {r"$\mathrm{II}$": "II", r"$\mathrm{II}^*$": "II*", r"$\mathrm{IV}$": "IV", r"$\mathrm{IV}^*$": "IV*", r"$\mathrm{III}$": "III",
         r"$\mathrm{III}^*$": "III*", r"$\mathrm{I}_0^*$": "I0*", r"$\mathrm{I}_n^*$": "In*"}
n_ok, n_cells, bad = 0, 0, []
for c in rows("tables/euler_iso3.tex")[2:]:
    t = TEXTY[c[0]]
    for e in (1, 2, 3, 4):
        mn, n = c[2 * e - 1], c[2 * e]; n_cells += 1
        ok = (mn == "--" and n == "--" and (t, e) not in iso) or ((t, e) in iso and (int(mn), num(n)) == iso[(t, e)])
        n_ok += ok
        if not ok: bad.append((t, e))
check(f"tab:iso      tables/euler_iso3.tex vs results/step9_euler_l3.txt: {n_ok} of {n_cells} cells agree", n_ok == n_cells and not bad, f"mismatch {bad}" if bad else "")

# tab:isolated (untwisted rows; same parsing as make_tables.py)
fit = {}
for line in open("results/step6_u1_fit_work.txt"):
    m = re.match(r"^\s*(\S+)\s+x(\d): n=\s*(\d+)\s+min V = (\d+)", line)
    if m: fit.setdefault(m.group(1), {})[int(m.group(2))] = (int(m.group(4)), int(m.group(3)))
    if line.startswith("################ l = 2"): break
NAME = {"IV (any $q$)": "IV", "IV$^*$ (any $q$)": "IV*", "III (any $q$)": "III", "III$^*$ (any $q$)": "III*", r"$\mathrm{I}_0^*$ (any $q$)": "I0*"}
n_ok, n_cells, bad, twisted = 0, 0, [], 0
for c in rows("tables/isolated3.tex")[1:]:
    if c[0] not in NAME: twisted += 1; continue
    t = NAME[c[0]]
    for k in (1, 2, 3):
        n_cells += 1; m = re.match(r"(\d+) \(([\d,]+)\)", c[k])
        ok = (c[k] == "--" and k not in fit.get(t, {})) or (m is not None and (int(m.group(1)), num(m.group(2))) == fit[t].get(k))
        n_ok += ok
        if not ok: bad.append((t, k))
check(f"tab:isolated tables/isolated3.tex untwisted rows vs results/step6_u1_fit_work.txt: {n_ok} of {n_cells} cells agree", n_ok == n_cells == 15 and not bad, f"mismatch {bad}" if bad else "")
skip(f"tab:isolated {twisted} twisted rows", "computed from results/step7_twist2_work_l3.parquet, git-ignored and not committed")

# tab:oot (same reading and deduplication as oot_convert.py, same aggregation as make_tables.py)
recs = []
for f in sorted(glob.glob("results/oot_*.tsv")):
    for line in open(f):
        a, N, kod, tam, deg, fam, t = line.rstrip("\n").split("\t"); recs.append((a, int(N), fam, float(t)))
d = pd.DataFrame(recs, columns=["label", "N", "family", "seconds"]).drop_duplicates(subset=["label"])
want = [[fam, f"{len(g):,}", f"{int(g.N.max()):,}", f"{g.seconds.median():.1f}"] for fam, g in d.groupby("family")]
want.append(["all", f"{len(d):,}", f"{int(d.N.max()):,}", f"{d.seconds.median():.1f}"])
got = rows("tables/oot.tex")[1:]
check(f"tab:oot      tables/oot.tex vs results/oot_*.tsv: {len(d)} unique curves, {sum(a == b for a, b in zip(got, want))} of {len(want)} rows agree", got == want)

# ---------------------------------------------------------------- (c) tables/ vs the printed paper
print("\n(c) tables/ against ../paper/note.tex")
NOTE = "../paper/note.tex"
if not os.path.exists(NOTE):
    skip("tables in note.tex", f"{NOTE} not found")
else:
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    paper = norm(open(NOTE).read())
    for lab, f in [("tab:uniform", "euler_uniform.tex"), ("tab:iso", "euler_iso3.tex"), ("tab:counts", "counts.tex"),
                   ("tab:ns", "ns3.tex"), ("tab:isolated", "isolated3.tex"), ("tab:oot", "oot.tex")]:
        body = norm(open(f"tables/{f}").read())
        check(f"{lab:12s} tables/{f} appears verbatim in {NOTE}", body in paper)

print(f"\nselftest: {'ALL CHECKS PASSED' if not FAIL else str(len(FAIL)) + ' CHECK(S) FAILED'}")
sys.exit(1 if FAIL else 0)
