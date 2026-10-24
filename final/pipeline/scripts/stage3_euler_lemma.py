"""Stage 3, item 5: Lemma lem:euler of ../paper/note.tex against PARI's lfunsympow on every optimal curve of the tables.
For every optimal curve of the work / holdout / ext ranges (N < 500000) and every bad prime q >= 5, compare PARI's
P_q (results/sym2_<set>_*.parquet, from lfunsympow + lfuneuler) with the polynomial of the table of the lemma:
   I_n: 1 - X;  I_n*: 1 - X;  II, II*, IV, IV*: 1 - chi_{-3}(q) q X;  III, III*: 1 - chi_{-4}(q) q X;
   I_0*: (1 - qX)(1 - (a^2 - 2q) X + q^2 X^2),  a = a_q(E'), E' the twist by q* (good reduction at q).
and e_l(E,q), l = 3, 5, 7 (q != l), from the closed formulas of the table with e_l from P_q (Definition def:terms).
Usage: python3 scripts/stage3_euler_lemma.py [sets...] -> results/stage3_euler_lemma.txt (stdout), results/stage3_euler_lemma_mismatch.csv"""
import sys, re, glob, time, numpy as np, pandas as pd, cypari2
pari = cypari2.Pari(); pari.allocatemem(400_000_000)
sets = sys.argv[1:] or ["work", "holdout", "ext"]
def vl(x, l):
    v = 0; x = int(x)
    if x == 0: return 99
    x = abs(x)
    while x % l == 0: x //= l; v += 1
    return v
def kron(a, q): return 1 if pow(a % q, (q - 1) // 2, q) == 1 else -1
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
def kind(k):
    if k >= 5: return "In"
    if k <= -5: return "In*"
    return {2: "II", -2: "II*", 3: "III", -3: "III*", 4: "IV", -4: "IV*", -1: "I0*"}[k]
def polmul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i + j] += x * y
    return c
ai_all = pd.read_parquet("data/curves.parquet", columns=["label", "ainvs"]).set_index("label").ainvs
mism = []; summ = []
for tag in sets:
    t0 = time.time()
    opt = pd.read_parquet(f"results/optimal_{tag}.parquet", columns=["label", "N", "kodaira"]).set_index("label")
    sym = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob(f"results/sym2_{tag}_*.parquet"))])
    sym = sym[sym.q >= 5].set_index(["label", "q"]).P.to_dict()
    cnt = {}
    for lab, r in opt.iterrows():
        ks = list(map(int, re.findall(r"-?\d+", str(r.kodaira))))
        for q, k in zip(primes(int(r.N)), ks):
            if q < 5: continue
            ty = kind(k); P = [int(x) for x in sym[(lab, q)].split(",")]
            if ty in ("In", "In*"): exp = [1, -1]
            elif ty in ("II", "II*", "IV", "IV*"): exp = [1, -kron(-3, q) * q]
            elif ty in ("III", "III*"): exp = [1, -kron(-1, q) * q]
            else:
                Et = pari.elltwist(pari.ellinit(pari(ai_all[lab])), q if q % 4 == 1 else -q); a = int(pari.ellap(Et, q))
                exp = polmul([1, -q], [1, -(a * a - 2 * q), q * q])
            c = cnt.setdefault(ty, {"pairs": 0, "P_match": 0, "e_match_l3": 0, "e_match_l5": 0, "e_match_l7": 0, "e_pos_l3": 0})
            c["pairs"] += 1; okP = (P == exp); c["P_match"] += okP
            num = sum(ci * q ** (2 * (len(P) - 1 - i)) for i, ci in enumerate(P))        # P_q(q^-2) q^(2 deg)
            for l in (3, 5, 7):
                if q == l: c[f"e_match_l{l}"] += 1; continue
                eP = vl(num, l) - (vl(q * q - 1, l) if ty == "In" else 0)
                if ty == "In": ef = 0
                elif ty == "In*": ef = vl(q * q - 1, l)
                elif ty in ("II", "II*", "IV", "IV*"): ef = vl(q - kron(-3, q), l)
                elif ty in ("III", "III*"): ef = vl(q - kron(-1, q), l)
                else: ef = vl(q - 1, l) + vl((q + 1) ** 2 - a * a, l)
                c[f"e_match_l{l}"] += (eP == ef)
                if l == 3: c["e_pos_l3"] += (ef > 0)
                if eP != ef: mism.append((tag, lab, q, ty, l, eP, ef, sym[(lab, q)]))
            if not okP: mism.append((tag, lab, q, ty, 0, None, None, sym[(lab, q)] + " expected " + ",".join(map(str, exp))))
    d = pd.DataFrame(cnt).T; d.insert(0, "set", tag); summ.append(d)
    print(f"{tag}: {len(opt)} curves, {int(d.pairs.sum())} pairs (curve, bad q >= 5), {time.time() - t0:.0f} s", flush=True)
    print(d.to_string(), flush=True)
s = pd.concat(summ); tot = s.drop(columns="set").groupby(level=0).sum()
print("\nall ranges:"); print(tot.to_string()); print("total pairs", int(tot.pairs.sum()), " P mismatches", int((tot.pairs - tot.P_match).sum()),
      " e mismatches (l=3,5,7)", int(sum((tot.pairs - tot[f"e_match_l{l}"]).sum() for l in (3, 5, 7))))
pd.DataFrame(mism, columns=["set", "label", "q", "type", "l", "e_from_P", "e_formula", "P"]).to_csv("results/stage3_euler_lemma_mismatch.csv", index=False)
