"""Stage 3, item 4: the minima of v_3(deg phi) at q = 3 that define the weights w_3 (Section sec:wild of ../paper/note.tex).
Population (as in scripts/step9_euler.py, with q = 3 in place of q >= 5): working-set optimal curves with E[3] irreducible,
not CM (the rows of results/step7_twist2_work_l3.parquet), whose only additive prime is q = 3, of potentially good type
(II, II*, III, III*, IV, IV*, I0*), and with no multiplicative 3-contribution (column mult = 0). Variant (b): in addition
every other term of the rule vanishes (e + tam = 0 in results/step10_rule_work_l3.parquet).
Usage: python3 scripts/stage3_w3.py  -> results/stage3_w3.txt (stdout)"""
import pandas as pd
d = pd.read_parquet("results/step7_twist2_work_l3.parquet", columns=["V", "mult"])
lp = pd.read_parquet("results/local_primes.parquet", columns=["label", "q", "type", "set"]); lp = lp[(lp.set == "work") & lp.label.isin(d.index)]
add = lp[lp.type != "In"]; nadd = add.groupby("label").size()
one = add[add.label.isin(nadd[nadd == 1].index) & (add.q == 3)].set_index("label")[["type"]]
j = one.join(d, how="inner"); j = j[(j.mult == 0) & (j.type != "In*")]
r = pd.read_parquet("results/step10_rule_work_l3.parquet", columns=["e", "tam", "wl"])
j = j.join(r)
W3 = {"II": 1, "II*": 2, "III": 0, "III*": 1, "IV": 1, "IV*": 2, "I0*": 0}
print("working set, E[3] irreducible, not CM, single additive prime q = 3 (potentially good), no multiplicative 3-part")
for name, s in [("(a)", j), ("(b) other rule terms zero", j[(j.e + j.tam) == 0])]:
    print(name)
    g = s.groupby("type").V.agg(n="size", min="min", n_at_min=lambda v: int((v == v.min()).sum()))
    g["paper_w3"] = g.index.map(W3); g["rule_wl"] = s.groupby("type").wl.max()
    print(g.loc[[t for t in W3 if t in g.index]].to_string())
