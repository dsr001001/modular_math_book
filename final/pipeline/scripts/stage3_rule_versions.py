"""Stage 3, item 10: the checks below conductor 10,000 under two PARI versions. Run with an interpreter whose cypari2 bundles
the PARI version to test. For every optimal curve with N < 10000 (38,042): ellmoddegree, and for l = 3, 5, 7, 11, 13 the
bound of scripts/euler_rule.gp, rule(E, l) and rule(E, l, 1) (ellmoddegree computed once per curve), plus ns3(E).
Writes one CSV per PARI version; scripts/stage3_rule_versions_compare.py compares two of them.
Usage: <python> scripts/stage3_rule_versions.py <out.csv>"""
import sys, time, pandas as pd, cypari2
pari = cypari2.Pari(); pari.allocatemem(800_000_000)
ver = ".".join(map(str, pari.version()))
import os, tempfile
src = open("scripts/euler_rule.gp").read().replace("[valuation(ellmoddegree(E), l), b];", "b;").replace("S = lfunsympow(E, 2)", "S = SYM")
assert "S = SYM" in src   # lfunsympow(E, 2) computed once per curve (global SYM), not once per call
tmp = os.path.join(tempfile.mkdtemp(), "euler_rule_bound.gp"); open(tmp, "w").write(src)   # rule() returning the bound only
pari(f'read("{tmp}")')
pari("""one(a) = my(E = ellinit(a), d = ellmoddegree(E)); SYM = lfunsympow(E, 2); concat([d, ns3(E)], concat(vector(5, i, rule(E, [3,5,7,11,13][i])), vector(5, i, rule(E, [3,5,7,11,13][i], 1))))""")
o = pd.read_parquet("results/optimal_work.parquet", columns=["label", "N", "moddeg"]); o = o[o.N < 10000]
ai = pd.read_parquet("data/curves.parquet", columns=["label", "ainvs"]).set_index("label").ainvs
t0 = time.time(); rows = []
for lab in o.label:
    r = pari(f"one({ai[lab]})"); rows.append([lab] + [int(x) for x in r])
    if len(rows) % 5000 == 0: print(f"  {len(rows)} curves, {time.time() - t0:.0f} s", flush=True)
cols = ["label", "deg", "ns3"] + [f"b{l}" for l in (3, 5, 7, 11, 13)] + [f"b{l}_iii" for l in (3, 5, 7, 11, 13)]
d = pd.DataFrame(rows, columns=cols); d["pari"] = ver
d.to_csv(sys.argv[1], index=False)
tab = o.set_index("label").moddeg.astype("int64")
print(f"PARI {ver}: {len(d)} curves in {time.time() - t0:.0f} s; ellmoddegree == table degree: {int((d.set_index('label').deg == tab).sum())}")
