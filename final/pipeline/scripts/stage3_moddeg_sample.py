"""Stage 3, items 6 and 8: ellmoddegree on a deterministic sample of optimal curves against the tables' degrees.
Sample: for each range (work, holdout, ext) and each configuration (a prime of type II, IV, IV*, I_n*, III; multiplicative
reduction only; mod 3 image 3Ns), curves drawn with numpy default_rng(20261024): 3 per configuration (2 for 3Ns), 20 per
range, 60 in all, plus 6942n1, 714i1 and 14a1 (Section sec:eis). Each ellmoddegree call has an alarm of 300 s.
Usage: python3 scripts/stage3_moddeg_sample.py -> results/stage3_moddeg_sample.csv, results/stage3_moddeg_sample.txt (stdout)"""
import re, time, numpy as np, pandas as pd, cypari2
pari = cypari2.Pari(); pari.allocatemem(1_500_000_000)
CONF = [("II", lambda ks, g: 2 in ks), ("IV", lambda ks, g: 4 in ks), ("IV*", lambda ks, g: -4 in ks), ("In*", lambda ks, g: any(k <= -5 for k in ks)),
        ("III", lambda ks, g: 3 in ks), ("mult only", lambda ks, g: all(k >= 5 for k in ks)), ("3Ns", lambda ks, g: re.search(r"\b3Ns\b", g) is not None)]
rng = np.random.default_rng(20261024)
ai = pd.read_parquet("data/curves.parquet", columns=["label", "ainvs"]).set_index("label").ainvs
sample = []
for tag in ("work", "holdout", "ext"):
    o = pd.read_parquet(f"results/optimal_{tag}.parquet", columns=["label", "N", "moddeg", "kodaira", "galrep_images"])
    ks = [list(map(int, re.findall(r"-?\d+", str(k)))) for k in o.kodaira]; g = o.galrep_images.fillna("").tolist()
    for name, f in CONF:
        idx = [i for i in range(len(o)) if f(ks[i], g[i])]
        for i in rng.choice(idx, size=2 if name == "3Ns" else 3, replace=False):
            sample.append((tag, name, o.label.iloc[i], int(o.N.iloc[i]), int(o.moddeg.iloc[i])))
c = pd.read_parquet("data/curves.parquet", columns=["label", "N", "moddeg"]).set_index("label")
for lab in ("6942n1", "714i1", "14a1"): sample.append(("work", "sec:eis", lab, int(c.N[lab]), int(c.moddeg[lab])))
rows = []; T = time.time()
for tag, name, lab, N, deg in sample:
    t0 = time.time()
    r = pari(f"iferr(alarm(300, ellmoddegree(ellinit({ai[lab]}))), e, -1)")
    d = int(r) if r.type() == "t_INT" else -1
    rows.append((tag, name, lab, N, deg, d, d == deg, round(time.time() - t0, 1)))
    print(f"{tag:8s} {name:9s} {lab:12s} N={N:7d} table {deg:12d} ellmoddegree {d:12d} {'OK' if d == deg else 'DIFF/TIMEOUT'} {time.time() - t0:6.1f} s", flush=True)
d = pd.DataFrame(rows, columns=["set", "config", "label", "N", "table_deg", "ellmoddegree", "agree", "seconds"])
d.to_csv("results/stage3_moddeg_sample.csv", index=False)
print(f"\n{len(d)} curves, agree {int(d.agree.sum())}, timeouts {int((d.ellmoddegree == -1).sum())}, total {time.time() - T:.0f} s")
print("6942n1 factorisation:", pari.factor(int(c.moddeg["6942n1"])))
