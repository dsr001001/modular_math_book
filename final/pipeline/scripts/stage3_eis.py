"""Stage 3, item 1: the counts of Section sec:eis of ../paper/note.tex (the Eisenstein deficit D of Conjecture conj:eis).

Definitions as in scripts/conj_check.py: for an optimal non-CM curve E with a rational l-isogeny (l | max_isogeny_degree),
   G = sum_q v_l(#Phi_q(F_q-bar)) (bound of eq:main),  V = v_l(deg phi),  D = G - V,
   torsion bound  = v_l(#E(Q)_tors) + [l = 3 and image 3Cs.1.1],
   class bound    = number of curves of the isogeny class with a rational point of order l.
The galrep labels of the tables are dotted below N = 400000 and dotless above (3Cs11, 3B11); both spellings are matched here.
Usage: python3 scripts/stage3_eis.py  -> results/stage3_eis.txt (stdout), results/stage3_eis_D2.csv"""
import re, numpy as np, pandas as pd

def vl(x, l):
    v = 0; x = int(x)
    while x > 0 and x % l == 0: x //= l; v += 1
    return v
GEOM = {1: 1, 2: 1, -2: 1, 3: 2, -3: 2, 4: 3, -4: 3, -1: 4}
def geom(k): return k - 4 if k >= 5 else (4 if k <= -5 else GEOM[k])
NM = 500001; spf = np.arange(NM)
for i in range(2, int(NM ** 0.5) + 1):
    if spf[i] == i:
        sl = spf[i * i::i]; sl[sl == np.arange(i * i, NM, i)] = i
def primes(n):
    out = []
    while n > 1:
        p = int(spf[n]); out.append(p)
        while n % p == 0: n //= p
    return out
CS = r"\b3Cs(?:\.1\.1|11)\b"; B11 = r"\b3B(?:\.1\.1|11)\b"
cur = pd.read_parquet("data/curves.parquet", columns=["label", "class_label", "N", "torsion", "torsion_structure", "galrep_images", "optimal", "rank", "is_cm"])
gal = cur.galrep_images.fillna("")
print("dotted vs dotless 3Cs.1.1 labels: 3Cs.1.1", int(gal.str.contains(r"\b3Cs\.1\.1\b").sum()), " 3Cs11", int(gal.str.contains(r"\b3Cs11\b").sum()),
      " (dotless labels only for N > 400000:", int(cur[gal.str.contains(r"\b3Cs11\b|\b3B11\b")].N.min()), ")")
res = {}
for tag in ("work", "holdout", "ext"):
    opt = pd.read_parquet(f"results/optimal_{tag}.parquet").set_index("label")
    opt = opt[~opt.is_cm.astype(bool)]
    for l in (3, 5, 7):
        e = opt[opt.max_isogeny_degree.astype("int64") % l == 0].copy()
        G = []
        for N, kod in zip(e.N, e.kodaira):
            ks = list(map(int, re.findall(r"-?\d+", str(kod)))); G.append(sum(vl(geom(k), l) for k in ks))
        e["G"] = G; e["V"] = [vl(x, l) for x in e.moddeg.astype("int64")]; e["D"] = e.G - e.V
        e["vT"] = [vl(x, l) for x in e.torsion.astype("int64")]
        g = e.galrep_images.fillna("")
        e["Cs"] = g.str.contains(CS).astype(int) if l == 3 else 0
        e["B11"] = g.str.contains(B11).astype(int) if l == 3 else 0
        e["lab3"] = [" ".join(s for s in str(x).split() if s.startswith("3")) for x in g]
        cls = cur[cur.class_label.isin(e.index.str.replace(r"\d+$", "", regex=True))]
        ncls = (cls.torsion.astype("int64") % l == 0).groupby(cls.class_label).sum()
        e["n_tors_class"] = ncls.reindex(e.index.str.replace(r"\d+$", "", regex=True)).fillna(0).astype(int).to_numpy()
        e["tb"] = e.vT + e.Cs
        e["rank"] = cur.set_index("label")["rank"].reindex(e.index).to_numpy(); e["torsion_structure"] = cur.set_index("label").torsion_structure.reindex(e.index).astype(str).to_numpy()
        res[(tag, l)] = e
        pos = e[e.D > 0]
        print(f"\n== {tag} l={l}: eis non-CM {len(e)}; G>0 {int((e.G > 0).sum())}; D>0 {len(pos)}; D distribution (D>0) {pos.D.value_counts().sort_index().to_dict()}")
        print(f"   violations of D <= vT + [Cs]: {int((e.D > e.tb).sum())};  of D <= #class curves with l-torsion point: {int((e.D > e.n_tors_class).sum())}")
        print(f"   D>0 without a rational l-torsion point: {int(((e.vT == 0) & (e.D > 0)).sum())}")
        print(f"   torsion bound attained with D>0 (D == vT + [Cs] > 0): {int(((e.D == e.tb) & (e.D > 0)).sum())};  class bound attained with D>0: {int(((e.D == e.n_tors_class) & (e.D > 0)).sum())}")
        if l == 3:
            borel = e[(e.vT == 1) & (e.Cs == 0)]
            print(f"   point of order 3, not 3Cs.1.1, no point of order 9: {len(borel)} curves, max D {borel.D.max()}  (labels {borel.lab3.value_counts().to_dict()})")
            d2 = e[e.D == 2]
            print(f"   D = 2: {len(d2)};  with 3Cs.1.1: {int(d2.Cs.sum())};  with a point of order 9: {int((d2.vT == 2).sum())};  9-torsion curves' labels: {d2[d2.vT == 2].lab3.value_counts().to_dict()}")
            print(f"   D = 2 and 3Cs.1.1: ranks {d2[d2.Cs == 1]['rank'].value_counts().to_dict()}, torsion {d2[d2.Cs == 1].torsion_structure.astype(str).value_counts().to_dict()}")
            print("   D = 2 curves:"); print(d2[["N", "moddeg", "kodaira", "torsion_structure", "lab3", "rank", "G", "V", "D"]].to_string())
            if tag == "work": d2.reset_index()[["label", "N", "moddeg", "kodaira", "torsion_structure", "lab3", "rank", "G", "V", "D"]].to_csv("results/stage3_eis_D2.csv", index=False)
            for lab in ("14a1", "714i1", "6942n1"):
                if lab in e.index: r = e.loc[lab]; print(f"   {lab}: deg {r.moddeg} kodaira {r.kodaira} torsion {r.torsion_structure} {r.lab3} D={r.D}")
# the two sources never combine
csall = cur[gal.str.contains(CS)]
for nmax in (400000, 500000):
    s = csall[csall.N <= nmax]
    print(f"\nall curves with 3Cs.1.1 (either spelling), N <= {nmax}: {len(s)}; with 9 | #torsion: {int((s.torsion.astype('int64') % 9 == 0).sum())}; torsion structures {s.torsion_structure.astype(str).value_counts().to_dict()}; optimal: {int((s.optimal == 1).sum())}")
nine = cur[(cur.torsion.astype("int64") % 9 == 0)]
for nm, s in [("all curves N<500000", nine), ("optimal (flag) N<=300000", nine[(nine.optimal == 1) & (nine.N <= 300000)]),
              ("optimal (flag) N<=400000", nine[(nine.optimal == 1) & (nine.N <= 400000)]), ("optimal (flag) N<500000", nine[nine.optimal == 1])]:
    lab = [" ".join(t for t in str(x).split() if t.startswith("3")) for x in s.galrep_images]
    print(f"curves with a point of order 9, {nm}: {len(s)}; non-CM {int((~s.is_cm.astype(bool)).sum())}; 3-labels {pd.Series(lab).value_counts().to_dict()}")
# summary counts for l = 5, 7 (paper: 192 and 18 in the working set)
for l in (5, 7):
    e = res[("work", l)]
    print(f"work l={l}: D>0 {int((e.D > 0).sum())}, all with vT>0: {bool((e[e.D > 0].vT > 0).all())}, max D {e.D.max()}")
tot = sum(int(((r.D == r.tb) & (r.D > 0)).sum()) for (t, l), r in res.items())
print("torsion bound attained with D>0, all three ranges, l = 3, 5, 7:", tot,
      {f"{t}/l{l}": int(((r.D == r.tb) & (r.D > 0)).sum()) for (t, l), r in res.items()})
