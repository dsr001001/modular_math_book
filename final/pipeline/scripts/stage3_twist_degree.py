"""Stage 3, item 2: the data of Theorem thm:twist of ../paper/note.tex, extending scripts/step9_twist_degree.py.
(A) For every working-set optimal curve E and every odd bad prime q of additive type, E^(q) = twist by q* = (-1)^((q-1)/2) q,
    E^(q)_0 the optimal curve of its isogeny class (looked up in the tables by a-invariants of the minimal model).
    Cases: (a) I_n* at q, (b) I_0* at q, (c) II, III, IV or a dual at q (q >= 5 in the paper).
    For l in {3,5,7,11,13} with l^2 not dividing N: count violations of v_l(deg E) >= v_l(deg E^(q)_0), and in case (c)
    the pairs with inequality. Counts are given for q >= 5 (as in step9_twist_degree.py) and for q = 3 separately.
(B) Below conductor 10,000: S = odd primes of type I_0* or I_n*, E_S = E twisted by prod q*, for l in {3,...,13} with
    l not dividing N and E[l] irreducible (l not dividing max_isogeny_degree): compare v_l(deg E) - v_l(deg E_S,0) with
    sum_{q in S} e_l(E,q), e_l from PARI's P_q (results/sym2_work_*.parquet). Population variants are reported.
Usage: python3 scripts/stage3_twist_degree.py -> results/stage3_twist_degree.txt (stdout), results/stage3_twist_degree_viol.csv"""
import re, glob, time, numpy as np, pandas as pd, cypari2
pari = cypari2.Pari(); pari.allocatemem(400_000_000)
opt = pd.read_parquet("results/optimal_work.parquet").set_index("label")
allc = pd.read_parquet("data/curves.parquet", columns=["label", "class_label", "ainvs", "moddeg", "optimal", "N"])
optdeg = allc[allc.optimal == 1].set_index("class_label").moddeg.astype("int64")
lookup = dict(zip(allc.ainvs.str.replace(" ", ""), allc.class_label))
ainvs = allc.set_index("label").ainvs.reindex(opt.index)
del allc
def vl(x, l):
    v = 0; x = int(x)
    while x > 0 and x % l == 0: x //= l; v += 1
    return v
NM = int(opt.N.max()) + 1; spf = np.arange(NM)
for i in range(2, int(NM ** 0.5) + 1):
    if spf[i] == i:
        sl = spf[i * i::i]; sl[sl == np.arange(i * i, NM, i)] = i
def primes(n):
    out = []
    while n > 1:
        p = int(spf[n]); out.append(p)
        while n % p == 0: n //= p
    return out
def twist_class(E, d):
    Et = pari.ellminimalmodel(pari.elltwist(E, d))
    return lookup.get("[" + ",".join(str(Et[i]) for i in range(5)) + "]")
L = (3, 5, 7, 11, 13)
def case(k): return "a" if k <= -5 else ("b" if k == -1 else "c")
st = {}
viol = []
t0 = time.time()
for idx, (lab, r) in enumerate(opt.iterrows()):
    ks = list(map(int, re.findall(r"-?\d+", str(r.kodaira)))); N = int(r.N); d = int(r.moddeg)
    E = None
    for q, k in zip(primes(N), ks):
        if q == 2 or k == 1 or k >= 5: continue      # skip q = 2 and the types I_0, I_n
        c = case(k); key = (c, "q>=5" if q >= 5 else "q=3")
        s = st.setdefault(key, {"pairs": 0, "found": 0, "pairs_l": 0, "viol_ge": 0, "neq": 0})
        s["pairs"] += 1
        if E is None: E = pari.ellinit(pari(ainvs[lab]))
        cl = twist_class(E, q if q % 4 == 1 else -q)
        if cl is None: continue
        s["found"] += 1; dq = int(optdeg[cl])
        for l in L:
            if N % (l * l) == 0: continue
            s["pairs_l"] += 1; v, vq = vl(d, l), vl(dq, l)
            if v < vq: s["viol_ge"] += 1; viol.append((lab, q, k, c, l, v, vq, cl))
            if v != vq: s["neq"] += 1
    if idx % 200000 == 0: print(f"  ... {idx} curves, {time.time() - t0:.0f} s", flush=True)
print("(A) working set, pairs (curve, odd additive prime q); pairs_l = (curve, q, l) with l^2 not dividing N and the twist class found")
print(pd.DataFrame(st).T.sort_index().to_string())
for qq in ("q>=5", "q=3"):
    a = st.get(("a", qq), {}); bc = {k: st.get((x, qq), {}).get(k, 0) for x in ("b", "c") for k in ("pairs",)}
    print(f"  {qq}: I_n* pairs {a.get('pairs')}; potentially good additive pairs (I0* + II..IV*) {st.get(('b', qq), {}).get('pairs', 0) + st.get(('c', qq), {}).get('pairs', 0)}; case (c) only {st.get(('c', qq), {}).get('pairs', 0)}")
pd.DataFrame(viol, columns=["label", "q", "kod", "case", "l", "v", "vq", "twist_class"]).to_csv("results/stage3_twist_degree_viol.csv", index=False)
print("violations of v_l(deg E) >= v_l(deg E^(q)_0):", len(viol))

# (B) below 10,000: difference against the Euler term
sym = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob("results/sym2_work_*.parquet"))])
small = opt[opt.N < 10000]
sym = sym[sym.label.isin(small.index)].set_index(["label", "q"]).P
def enum(P, q):
    c = [int(x) for x in P.split(",")]; dg = len(c) - 1
    return sum(ci * q ** (2 * (dg - i)) for i, ci in enumerate(c))
rows = []
for lab, r in small.iterrows():
    ks = list(map(int, re.findall(r"-?\d+", str(r.kodaira)))); N = int(r.N)
    S = [q for q, k in zip(primes(N), ks) if q != 2 and (k == -1 or k <= -5)]
    if not S: continue
    D = 1
    for q in S: D *= q if q % 4 == 1 else -q
    cl = twist_class(pari.ellinit(pari(ainvs[lab])), D)
    if cl is None: rows.append((lab, None, None, None, None, None, None)); continue
    for l in L:
        if N % l == 0: continue
        eu = sum(vl(enum(sym[(lab, q)], q), l) for q in S)
        rows.append((lab, l, int(r.max_isogeny_degree) % l != 0, bool(r.is_cm), vl(int(r.moddeg), l) - vl(int(optdeg[cl]), l), eu, cl))
b = pd.DataFrame(rows, columns=["label", "l", "irred", "cm", "diff", "euler", "twist_class"])
print(f"\n(B) N < 10000, S nonempty: curves {b.label.nunique()}, twist class not found: {int(b.l.isna().sum())}")
b = b.dropna(subset=["l"])
for nm, s in [("E[l] irreducible, incl. CM", b[b.irred]), ("E[l] irreducible, not CM", b[b.irred & ~b.cm.astype(bool)]), ("all l not dividing N", b)]:
    print(f"   {nm}: pairs {len(s)}; diff == euler: {int((s['diff'] == s.euler).sum())}; diff != euler: {int((s['diff'] != s.euler).sum())}")
    print("      mismatches:", s[s['diff'] != s.euler].head(10).to_dict("records"))
