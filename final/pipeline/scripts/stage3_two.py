"""Stage 3, item 3: Section sec:two of ../paper/note.tex. For optimal non-CM curves without a rational 2-isogeny
(max_isogeny_degree odd), on the three in-table ranges:
   (w1) v_2(deg) >= sum_{q || N} v_2(n_q) + #{q : type III, III*, I0* or In*}          (paper: no exception)
   (w2) the same with I0* counted with weight 2 = v_2(#Phi_q)                          (paper: 123, 26, 20 exceptions)
Same definitions as scripts/step6_u1_fit.py (l = 2 candidates), computed from the Kodaira codes of results/optimal_<set>.parquet,
so that the extension (which step6_u1_fit.py cannot read: load.py stops at N = 400000) is included.
Usage: python3 scripts/stage3_two.py  -> results/stage3_two.txt (stdout)"""
import re, pandas as pd

def v2(x):
    v = 0; x = int(x)
    while x > 0 and x % 2 == 0: x //= 2; v += 1
    return v
for tag in ("work", "holdout", "ext"):
    o = pd.read_parquet(f"results/optimal_{tag}.parquet")
    o = o[(o.max_isogeny_degree.astype("int64") % 2 == 1) & ~o.is_cm.astype(bool)]
    S, nIII, nI0s, nIns, V = [], [], [], [], []
    for kod, d in zip(o.kodaira, o.moddeg.astype("int64")):
        ks = list(map(int, re.findall(r"-?\d+", str(kod))))
        S.append(sum(v2(k - 4) for k in ks if k >= 5)); nIII.append(sum(abs(k) == 3 for k in ks))
        nI0s.append(sum(k == -1 for k in ks)); nIns.append(sum(k <= -5 for k in ks)); V.append(v2(d))
    d = pd.DataFrame({"label": o.label.to_numpy(), "S": S, "III": nIII, "I0s": nI0s, "Ins": nIns, "V": V})
    w1 = d.S + d.III + d.I0s + d.Ins; w2 = w1 + d.I0s
    print(f"{tag}: curves {len(d)}; (w1) positive {int((w1 > 0).sum())} violations {int((d.V < w1).sum())};"
          f" (w2, I0* weight 2) violations {int((d.V < w2).sum())}; (Ins weight 2) violations {int((d.V < w1 + d.Ins).sum())}")
    bad = d[d.V < w2]
    print("   (w2) exceptions by number of I0* primes:", bad.I0s.value_counts().sort_index().to_dict(), " first:", bad.label.head(8).tolist())
