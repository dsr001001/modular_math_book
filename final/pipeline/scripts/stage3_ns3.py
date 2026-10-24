"""Stage 3, item 7: the mod 3 image labels of the tables against the factorisation of the 3-division polynomial
(Proposition prop:ns, the function ns3 of scripts/euler_rule.gp), on every optimal non-CM curve with N < 500000
(work, holdout, ext). For each curve: the factor degrees of elldivpol(E, 3) and, when it is irreducible, the order of its
Galois group (polgalois). ns3(E) = 1 iff psi_3 factors as two quadratics (two factors, the first of degree 2), exactly as
in euler_rule.gp. Compared with the galrep labels 3Ns and 3Nn (dotted or dotless spelling).
Usage: python3 scripts/stage3_ns3.py -> results/stage3_ns3.txt (stdout), results/stage3_ns3_disagree.csv"""
import time, pandas as pd, cypari2
pari = cypari2.Pari(); pari.allocatemem(400_000_000)
pari("""ns3info(v) = vector(#v, i, my(E = ellinit(v[i]), F = factor(elldivpol(E, 3))[,1], d = vecsort(apply(poldegree, F~)));
   [#F, poldegree(F[1]), if(#F == 1, polgalois(F[1])[1], 0), d])""")
rows = []
for tag in ("work", "holdout", "ext"):
    t0 = time.time()
    o = pd.read_parquet(f"results/optimal_{tag}.parquet", columns=["label", "is_cm", "galrep_images"])
    o = o[~o.is_cm.astype(bool)]
    ai = pd.read_parquet("data/curves.parquet", columns=["label", "ainvs"]).set_index("label").ainvs.reindex(o.label)
    labs = o.label.tolist(); A = ai.tolist()
    B = 4000
    for s in range(0, len(labs), B):
        res = pari("ns3info([%s])" % ",".join(A[s:s + B]))
        for lab, r in zip(labs[s:s + B], res):
            rows.append((tag, lab, int(r[0]), int(r[1]), int(r[2]), "+".join(str(int(x)) for x in r[3])))
    print(f"{tag}: {len(labs)} curves, {time.time() - t0:.0f} s", flush=True)
d = pd.DataFrame(rows, columns=["set", "label", "nfac", "deg1", "galord", "degs"])
gal = pd.concat([pd.read_parquet(f"results/optimal_{t}.parquet", columns=["label", "galrep_images"]) for t in ("work", "holdout", "ext")]).set_index("label").galrep_images.fillna("")
d["lab3"] = [" ".join(s for s in gal[l].split() if s.startswith("3")) for l in d.label]
d["Ns_label"] = d.lab3.str.contains(r"\b3Ns\b"); d["Nn_label"] = d.lab3.str.contains(r"\b3Nn\b")
d["ns3"] = (d.nfac == 2) & (d.deg1 == 2)
d["D4"] = (d.nfac == 1) & (d.galord == 8)
for tag, s in list(d.groupby("set")) + [("all", d)]:
    print(f"\n== {tag}: curves {len(s)}")
    print("   ns3 (two quadratics) vs label 3Ns:"); print(pd.crosstab(s.ns3, s.Ns_label).to_string())
    print("   psi_3 irreducible with Galois group of order 8 (D4) vs label 3Nn:"); print(pd.crosstab(s.D4, s.Nn_label).to_string())
print("\nfactor-degree pattern by 3-label (all ranges):")
print(pd.crosstab(d.lab3.replace("", "(none)"), d.degs + "/" + d.galord.astype(str)).to_string())
dis = d[(d.ns3 != d.Ns_label) | (d.D4 != d.Nn_label)]
dis.to_csv("results/stage3_ns3_disagree.csv", index=False)
print("\ndisagreements (either test):", len(dis)); print(dis.head(30).to_string())
