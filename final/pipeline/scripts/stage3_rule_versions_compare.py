"""Stage 3, item 10: compare the outputs of scripts/stage3_rule_versions.py under two PARI versions, and the per-curve
PARI feature rows (scripts/pari_features.gp) of the block 00000-09999 under the two versions.
Usage: python3 scripts/stage3_rule_versions_compare.py <a.csv> <b.csv> [<curves_a.tsv> <curves_b.tsv> <ap_a.tsv> <ap_b.tsv>]"""
import sys, re, pandas as pd
a, b = pd.read_csv(sys.argv[1]), pd.read_csv(sys.argv[2])
print("versions:", a.pari.iloc[0], "vs", b.pari.iloc[0], " curves:", len(a), len(b))
m = a.merge(b, on="label", suffixes=("_a", "_b"))
cols = [c for c in a.columns if c not in ("label", "pari")]
for c in cols: print(f"   {c:8s} differing curves: {int((m[c + '_a'] != m[c + '_b']).sum())}")
o = pd.read_parquet("results/optimal_work.parquet", columns=["label", "moddeg", "max_isogeny_degree", "is_cm"]).set_index("label")
d = a.set_index("label").join(o)
print("   ellmoddegree vs table:", int((d.deg == d.moddeg.astype("int64")).sum()), "of", len(d))
def vl(x, l):
    v = 0
    while x % l == 0: x //= l; v += 1
    return v
for l in (3, 5, 7, 11, 13):
    s = d[(d.max_isogeny_degree.astype("int64") % l != 0) & ~d.is_cm.astype(bool)]
    V = s.deg.map(lambda x: vl(int(x), l))
    print(f"   l={l}: curves {len(s)}, rule(E,l,1) positive {int((s[f'b{l}_iii'] > 0).sum())} violations {int((V < s[f'b{l}_iii']).sum())}; rule(E,l) positive {int((s[f'b{l}'] > 0).sum())} violations {int((V < s[f'b{l}']).sum())}")
if len(sys.argv) > 3:
    for x, y in ((sys.argv[3], sys.argv[4]), (sys.argv[5], sys.argv[6])):
        A, B = open(x).read().splitlines(), open(y).read().splitlines()
        nd = sum(p != q for p, q in zip(A, B))
        # columns that may legitimately differ in the last digits: floating logs; compare all other fields exactly
        def strip(r): f = r.split("\t"); return [g for i, g in enumerate(f) if not ("." in g and re.fullmatch(r"-?[\d.E+-]+", g))]
        ne = sum(strip(p) != strip(q) for p, q in zip(A, B))
        print(f"{x} vs {y}: lines {len(A)} / {len(B)}; byte-identical lines differ: {nd}; differing in a non-float field: {ne}")
