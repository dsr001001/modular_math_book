"""Wild local factors at q = 2 and q = 3 for a fixed sample of curves: the polynomial P_q(X) with
L_q(Sym^2 f, s) = P_q(q^{-s})^{-1}, from PARI's lfunsympow / lfuneuler (the same calls as scripts/step10_sym2_euler.py),
the value P_q(q^{-2}) as an exact rational and the Euler terms e_l(E,q) = v_l(P_q(q^{-2})) for l = 3, 5, 7
(paper, Definition def:terms; a_q = 0 at an additive prime, so the naive factor is 1). One row per curve and additive q.

Sample (fixed; rows sorted by conductor, class, curve number, q):
  (a) "paper": every curve of the tables named in ../paper/note.tex (list PAPER_CURVES below, with explicit a-invariants;
      the class 54a is taken whole, since the paper names the types of its three curves), kept if it has additive
      reduction at 2 or at 3;
  (b) "rule": every X_0(N)-optimal curve (ecdata opt_man flag 1) of conductor N < 2000 without complex multiplication
      (j not one of the 13 rational CM j-invariants) with 4 | N or 9 | N, i.e. additive reduction at 2 or at 3.
For each row it also checks the shape of P_q against Proposition prop:shapes (i)-(iv) of the paper, with an independent
check of shape (ii) through a quadratic twist of good reduction at q, and the statements of the paper at q = 2, 3.

Usage (from final/pipeline):
  python3 scripts/wild_euler_samples.py [ECDATA_DIR] > samples/wild_euler_q23.log
writes samples/wild_euler_q23.csv. ECDATA_DIR defaults to ../../data/ecdata (Cremona's ecdata files for N < 10000 at the
pinned commit, fetched by ../../tools/setup_env.sh). Without it only part (a) is computed, from the a-invariants below
(PARI's elldata is not used: it is not installed with the PARI of the reference environment). Exit status 1 if any check fails.
"""
import csv, hashlib, io, os, sys, platform
from fractions import Fraction
import importlib.metadata
import cypari2

pari = cypari2.Pari()
pari.allocatemem(600_000_000)

OUT_CSV = "samples/wild_euler_q23.csv"
NMAX = 2000
ELLS = (3, 5, 7)
CM_J = {0, 1728, -3375, 8000, -32768, 54000, 287496, -884736, -12288000, 16581375, -884736000,
        -147197952000, -262537412640768000}

# Curves named in ../paper/note.tex (Cremona labels), with their a-invariants from ecdata allcurves (commit 25cec5e).
# Only those with additive reduction at 2 or 3 produce rows; the others are listed so that the selection is visible.
PAPER_CURVES = {
    "11a1": [0, -1, 1, -10, -20], "14a1": [1, 0, 1, 4, -6], "20a1": [0, 1, 0, 4, 4], "26b1": [1, -1, 1, -3, 3],
    "27a1": [0, 0, 1, 0, -7], "37a1": [0, 0, 1, -1, 0], "52a1": [0, 0, 0, 1, -10], "54a1": [1, -1, 0, 12, 8],
    "54a2": [1, -1, 0, -123, -667], "54a3": [1, -1, 0, -3, 3], "77a1": [0, 0, 1, 2, 0], "77c1": [1, 1, 0, 4, 11],
    "99a1": [1, -1, 1, -2, 0], "121a1": [1, 1, 1, -30, -76], "121b1": [0, -1, 1, -7, 10],
    "121d1": [0, -1, 1, -40, -221], "121d2": [0, -1, 1, -1250, 31239], "126a1": [1, -1, 1, -5, -7],
    "140b1": [0, 0, 0, 32, 212], "243b1": [0, 0, 1, 0, 2], "256a1": [0, 1, 0, -3, 1], "256d1": [0, -1, 0, -3, -1],
    "275b1": [0, 1, 1, -8, 19], "336f1": [0, 1, 0, -1, 2], "539c1": [1, 0, 1, 170, -3237],
    "539d1": [0, 1, 1, -16, -66], "592c1": [0, 0, 0, -16, -16], "714i1": [1, 0, 0, 108, 11664],
    "726a1": [1, 1, 0, -35, -51], "726f1": [1, 1, 1, -4298, 46487], "980i1": [0, 0, 0, 1568, -72716],
    "990h1": [1, -1, 1, -96608, -11533373], "990h3": [1, -1, 1, -1568, -4669], "1089e1": [0, 0, 1, -66, -212],
    "1184f1": [0, 0, 0, -1048, 13040], "1232l1": [0, 0, 0, 32, -16], "1748e1": [0, 0, 0, -3061, -65491],
    "1936f1": [0, 1, 0, -117, -541], "2178b1": [1, -1, 0, -38682, -1293836], "2178h1": [1, -1, 1, -320, 1059],
    "2304c1": [0, 0, 0, -30, -56], "2304k1": [0, 0, 0, -30, 56], "3025a1": [0, 1, 1, -183, 919],
    "3840h1": [0, 1, 0, -11, -711], "3840k1": [0, 1, 0, -315, 2025], "3840o1": [0, -1, 0, -11, 711],
    "3840r1": [0, -1, 0, -315, -2025], "5070h1": [1, 1, 0, -3795912, -2743222464],
    "5070p1": [1, 1, 1, -22461, -1257261], "5808y1": [0, 1, 0, -68768, -3112716], "5808z1": [0, 1, 0, -568, 2132],
    "5929a1": [0, 1, 1, -359, -2810], "6400f1": [0, -1, 0, -83, 287], "6400r1": [0, 1, 0, -83, -287],
    "6942n1": [1, 0, 0, -210177, 37101321], "7744a1": [0, 1, 0, -29, 53], "7744s1": [0, -1, 0, -29, -53],
}

# PARI calls, as GP commands (the Python code below makes the same calls through cypari2, as step10_sym2_euler.py does).
GP_COMMANDS = [
    "E = ellinit(ainvs)",
    "G = ellglobalred(E)            \\\\ conductor, Kodaira codes, Tamagawa numbers",
    "R = elllocalred(E, q)          \\\\ [f_q, Kodaira code, change of model, c_q]",
    "vj = valuation(E.j, q)         \\\\ v_q(j); 'inf' when j = 0",
    "L = lfunsympow(E, 2)",
    "P = 1/lfuneuler(L, q)          \\\\ P_q(x), integer coefficients; coefficients = Vecrev(P)",
    "subst(P, x, 1/q^2)             \\\\ P_q(q^-2), exact rational",
    "valuation(subst(P, x, 1/q^2), l)   \\\\ e_l(E,q), l = 3, 5, 7, l != q",
    "Et = ellminimalmodel(ellinit(elltwist(E, D))); elllocalred(Et, q)[1]; ellap(Et, q)   \\\\ D = -4, 8, -8 (q = 2), D = -3 (q = 3)",
    "1/lfuneuler(lfunsympow(ellinit(ainvs), 2), q)   \\\\ cross-check, the string form used in scripts/selftest.py",
]


def kodaira(code):
    c = int(code)
    if c == 1: return "I0"
    if c == -1: return "I0*"
    if c > 4: return f"I{c - 4}"
    if c < -4: return f"I{-c - 4}*"
    return {2: "II", 3: "III", 4: "IV", -2: "II*", -3: "III*", -4: "IV*"}[c]


def split_label(lab):
    i = 0
    while lab[i].isdigit(): i += 1
    j = i
    while lab[j].isalpha(): j += 1
    return int(lab[:i]), lab[i:j], int(lab[j:])


def sortkey(lab):
    n, c, k = split_label(lab)
    return (n, len(c), c, k)


def vrat(x, l):
    x = Fraction(x)
    def v(n):
        n, k = abs(n), 0
        while n % l == 0: n //= l; k += 1
        return k
    return v(x.numerator) - v(x.denominator)


def polystr(co):
    terms = []
    for k, c in enumerate(co):
        if c == 0: continue
        mono = "" if k == 0 else ("X" if k == 1 else f"X^{k}")
        if k == 0: t = str(c)
        elif c == 1: t = mono
        elif c == -1: t = "-" + mono
        else: t = f"{c}{mono}"
        terms.append(t)
    s = "+".join(terms).replace("+-", "-")
    return s or "0"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_ecdata(d):
    """a-invariants of every curve with N < NMAX, and the set of optimal labels, from opt_man (same a-invariants as allcurves)."""
    ai, opt = {}, set()
    for line in open(os.path.join(d, "opt_man.00000-09999")):
        f = line.split()
        if int(f[0]) >= NMAX: continue
        lab = f"{f[0]}{f[1]}{f[2]}"
        ai[lab] = [int(x) for x in f[3].strip("[]").split(",")]
        if f[4] == "1": opt.add(lab)
    return ai, opt


def twist_check(E, q, coeffs):
    """Shape (ii) independently: a quadratic twist E' with good reduction at q; returns (D, a_q(E'), predicted coefficients)."""
    for D in ((-4, 8, -8) if q == 2 else (-3,)):
        Et = pari.ellminimalmodel(pari.ellinit(pari.elltwist(E, D)))
        if int(pari.elllocalred(Et, q)[0]) == 0:
            a = int(pari.ellap(Et, q))
            b = a * a - 2 * q          # (1 - qX)(1 - bX + q^2 X^2)
            return D, a, [1, -b - q, q * b + q * q, -q ** 3]
    return None, None, None


def shape_of(coeffs, q):
    """Shape of Proposition prop:shapes read off the coefficients alone ('?' if none fits)."""
    if coeffs == [1]: return "iv", None
    if coeffs == [1, -1]: return "i", None
    if len(coeffs) == 2 and coeffs[1] in (q, -q): return "iii", -coeffs[1] // q
    if len(coeffs) == 4:
        # (1 - qX)(1 - bX + q^2X^2) = 1 - (b+q)X + (qb+q^2)X^2 - q^3X^3, b = a^2 - 2q, a integer, a^2 <= 4q
        b = -coeffs[1] - q
        if coeffs[2] == q * b + q * q and coeffs[3] == -q ** 3:
            a2 = b + 2 * q
            a = int(round(a2 ** 0.5)) if a2 >= 0 else -1
            if a >= 0 and a * a == a2 and a2 <= 4 * q: return "ii", a
    return "?", None


def main():
    ecdir = sys.argv[1] if len(sys.argv) > 1 else "../../data/ecdata"
    have_ec = os.path.exists(os.path.join(ecdir, "opt_man.00000-09999"))
    ai, opt = (load_ecdata(ecdir) if have_ec else ({}, set()))
    failures = []
    def fail(msg):
        failures.append(msg); print("FAIL", msg)

    # check the hard-coded a-invariants against ecdata where available
    if have_ec:
        allc = {}
        for line in open(os.path.join(ecdir, "allcurves.00000-09999")):
            f = line.split(); allc[f"{f[0]}{f[1]}{f[2]}"] = [int(x) for x in f[3].strip("[]").split(",")]
        for lab, a in PAPER_CURVES.items():
            if allc.get(lab) != a: fail(f"a-invariants of {lab} differ from ecdata allcurves: {allc.get(lab)} vs {a}")

    sample = {}   # label -> (ainvs, reasons)
    for lab, a in PAPER_CURVES.items(): sample[lab] = (a, ["paper"])
    nrule = 0
    for lab in opt:
        N = split_label(lab)[0]
        if N % 4 and N % 9: continue
        E = pari.ellinit(ai[lab])
        if int(pari.denominator(E.j())) == 1 and int(E.j()) in CM_J: continue
        nrule += 1
        if lab in sample: sample[lab][1].append("rule")
        else: sample[lab] = (ai[lab], ["rule"])

    rows = []
    for lab in sorted(sample, key=sortkey):
        a, why = sample[lab]
        E = pari.ellinit(a)
        G = pari.ellglobalred(E)
        N = int(G[0])
        if N != split_label(lab)[0]: fail(f"{lab}: PARI conductor {N}")
        L = pari.lfunsympow(E, 2)
        jj = E.j()
        cm = int(pari.denominator(jj)) == 1 and int(jj) in CM_J
        gkod = {int(p): int(r[1]) for p, r in zip(G[3][0], G[4])}   # G[3] = factor(N), G[4] = local data in that order
        for q in (2, 3):
            if N % (q * q): continue
            R = pari.elllocalred(E, q)
            fq, code, cq = int(R[0]), int(R[1]), int(R[3])
            if gkod.get(q) != code: fail(f"{lab} q={q}: ellglobalred and elllocalred Kodaira codes differ")
            vj = "inf" if jj == 0 else int(pari.valuation(jj, q))
            # step10_sym2_euler.py method
            P = 1 / pari.lfuneuler(L, q)
            co = [int(c) for c in pari.Vec(pari.Pol(P))][::-1]
            # cross-check: GP string form (selftest.py)
            P2 = pari(f"1/lfuneuler(lfunsympow(ellinit({a}), 2), {q})")
            if not bool(pari(f"({P}) == ({P2})")): fail(f"{lab} q={q}: lfuneuler string form differs: {P2}")
            aq = int(pari.ellap(E, q))
            if aq != 0: fail(f"{lab} q={q}: a_q = {aq} at an additive prime")
            val = sum(Fraction(c, q ** (2 * k)) for k, c in enumerate(co))
            if Fraction(str(pari.subst(P, "x", Fraction(1, q * q)))) != val: fail(f"{lab} q={q}: P(q^-2) mismatch")
            e = {l: ("" if l == q else vrat(val, l)) for l in ELLS}
            shp, par = shape_of(co, q)
            D, at, pred = twist_check(E, q, co)
            pot_mult = vj != "inf" and vj < 0
            notes = []
            if shp == "?": notes.append("no shape fits")
            if shp == "i" and not pot_mult: notes.append("shape (i) but v_q(j) >= 0")
            if pot_mult and shp != "i": notes.append("v_q(j) < 0 but not shape (i)")
            if shp == "ii":
                if pred is None: notes.append("shape (ii) but no quadratic twist with good reduction at q")
                elif pred != co: notes.append(f"shape (ii) but twist D={D} gives {polystr(pred)}")
            if shp in ("iii", "iv") and pred is not None:
                notes.append(f"shape ({shp}) but twist D={D} has good reduction at q")
            # e_l from the formula of the shape
            for l in ELLS:
                if l == q: continue
                if shp == "i": f = vrat(q * q - 1, l)
                elif shp == "ii": f = vrat(q - 1, l) + vrat((q + 1) ** 2 - par * par, l)
                elif shp == "iii": f = vrat(q - par, l)
                elif shp == "iv": f = 0
                else: continue
                if f != e[l]: notes.append(f"e_{l} {e[l]} != shape formula {f}")
            for n in notes: fail(f"{lab} q={q}: {n}")
            rows.append(dict(label=lab, sample="+".join(why), ainvs=str(a).replace(" ", ""), N=N, cm=int(cm), q=q,
                             cond_exp=fq, kodaira=kodaira(code), kodaira_code=code, tamagawa=cq, v_q_j=vj, a_q=aq,
                             P_coeffs=",".join(map(str, co)), P_poly=polystr(co), P_at_q_minus2=str(val),
                             e_3=e[3], e_5=e[5], e_7=e[7], shape=shp,
                             shape_param=("" if par is None else par),
                             twist_D=("" if D is None else D), twist_a=("" if at is None else at),
                             shape_check="ok" if not notes else "; ".join(notes)))

    # ------------------------------------------------------------------ statements of the paper at q = 2, 3
    by = {(r["label"], r["q"]): r for r in rows}
    def expect(lab, q, kod=None, poly=None, el=None, shape=None):
        r = by.get((lab, q))
        if r is None: fail(f"{lab} q={q}: no row"); return
        got = [r["kodaira"], r["P_coeffs"]]
        ok = True
        if kod is not None and r["kodaira"] not in (kod if isinstance(kod, tuple) else (kod,)): ok = False
        if poly is not None and r["P_coeffs"] != poly: ok = False
        if shape is not None and r["shape"] != shape: ok = False
        for l, v in (el or {}).items():
            if r[f"e_{l}"] != v: ok = False
        msg = (f"{lab} q={q}: type {r['kodaira']}, P_q = {r['P_poly']}, P_q(q^-2) = {r['P_at_q_minus2']}, "
               f"e_3,e_5,e_7 = {r['e_3']},{r['e_5']},{r['e_7']}, v_q(j) = {r['v_q_j']}, shape ({r['shape']})")
        print(("ok   " if ok else "FAIL ") + msg)
        if not ok: failures.append(msg)

    print("Named examples of the paper (Remark rem:wild, Lemma lem:IV, Example ex:qual, Proposition prop:ns-structure, Sections sec:boundary, sec:anomaly, sec:data)")
    expect("336f1", 2, "II", "1,2", {3: 1})                                  # rem:wild
    expect("1232l1", 2, "II*", "1,2,-4,-8", {3: 2})                         # rem:wild: (1-2X)(1+2X)^2
    expect("592c1", 2, "II*", "1,-2,4,-8", {5: 1})                          # rem:wild: (1-2X)(1+4X^2)
    expect("52a1", 2, "IV*", "1,2", {3: 1})                                 # ex:qual (a), lem:IV
    for lab in ("256a1", "256d1", "2304c1", "2304k1", "6400f1", "6400r1"):  # prop:ns-structure (ii) and sec:boundary, R = {2}: type III, P_2 = 1+2X
        expect(lab, 2, "III", "1,2", {3: 1})
    for lab in ("2178b1", "2178h1"):                                         # sec:anomaly: t_3(E,3) = 1 from I_n^* at 3
        expect(lab, 3, None, "1,-1", shape="i")
    t54 = sorted(by[(l, 3)]["kodaira"] for l in ("54a1", "54a2", "54a3"))
    ok = t54 == sorted(["IV*", "II*", "II"])
    print(("ok   " if ok else "FAIL ") + f"54a: types at 3 {[(l, by[(l, 3)]['kodaira']) for l in ('54a1', '54a2', '54a3')]}"
          f", paper IV*, II*, II; P_3: {[(l, by[(l, 3)]['P_poly']) for l in ('54a1', '54a2', '54a3')]}")
    if not ok: failures.append("54a types")
    for lab in ("121a1", "726a1"):
        n = split_label(lab)[0]
        print(f"info {lab}: N = {n}, no additive reduction at 2 or 3 (no row)")

    iv2 = [r for r in rows if r["q"] == 2 and r["kodaira"] in ("IV", "IV*")]
    bad = [r["label"] for r in iv2 if r["P_coeffs"] != "1,2"]
    print(("ok   " if not bad else "FAIL ") + f"type IV/IV* at 2 has P_2 = 1+2X (Lemma lem:IV): {len(iv2) - len(bad)} of {len(iv2)} rows"
          + (f"; exceptions {bad}" if bad else ""))
    if bad: failures.append("IV at 2")

    # ------------------------------------------------------------------ write
    hdr = io.StringIO()
    hdr.write("# Wild local factors of Sym^2 at q = 2, 3; written by scripts/wild_euler_samples.py (see samples/README.md)\n")
    hdr.write(f"# PARI {'.'.join(map(str, pari.version()))} via cypari2 {importlib.metadata.version('cypari2')}, "
              f"Python {platform.python_version()}\n")
    if have_ec:
        hdr.write(f"# input: Cremona ecdata (commit 25cec5ecfec8b9f016eb1631ac633194c2bed39f), "
                  f"opt_man.00000-09999 sha256 {sha(os.path.join(ecdir, 'opt_man.00000-09999'))}, "
                  f"allcurves.00000-09999 sha256 {sha(os.path.join(ecdir, 'allcurves.00000-09999'))}\n")
    else:
        hdr.write("# input: ecdata absent; only the curves named in the paper (a-invariants in the script)\n")
    hdr.write(f"# sample: 'paper' = curves named in ../paper/note.tex with additive reduction at 2 or 3; 'rule' = every optimal "
              f"non-CM curve with N < {NMAX} and 4|N or 9|N ({nrule} curves)\n")
    hdr.write("# PARI commands (GP form; ainvs and q from the row; P_q(X) with L_q(Sym^2 f,s) = P_q(q^-s)^-1):\n")
    for c in GP_COMMANDS: hdr.write(f"#   {c}\n")
    hdr.write("# e_l = v_l(P_q(q^-2)) for l != q (empty for l = q); a_q = 0, naive factor 1 (Definition def:terms)\n")
    hdr.write("# shape = Proposition prop:shapes (i)-(iv); shape_param = a for (ii), c for (iii); twist_D, twist_a = quadratic "
              "twist by the discriminant D (field Q(sqrt D)) with good reduction at q and its a_q, if one exists among the D tried\n")
    os.makedirs("samples", exist_ok=True)
    with open(OUT_CSV, "w", newline="") as fh:
        fh.write(hdr.getvalue())
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), lineterminator="\n")
        w.writeheader(); w.writerows(rows)

    # ------------------------------------------------------------------ summary
    from collections import Counter
    print(f"\nrows: {len(rows)} (curves: {len({r['label'] for r in rows})}; q=2: {sum(r['q'] == 2 for r in rows)}, "
          f"q=3: {sum(r['q'] == 3 for r in rows)}); rule sample {nrule} curves; "
          f"paper-named curves with a row: {len({r['label'] for r in rows if 'paper' in r['sample']})}")
    print(f"shape mismatches: {sum(r['shape_check'] != 'ok' for r in rows)}")
    print("\nrule sample, count by (q, Kodaira type, shape, P_q):")
    def kgroup(k):
        if k.startswith("I") and k not in ("II", "II*", "III", "III*", "IV", "IV*", "I0", "I0*"):
            return "In*" if k.endswith("*") else "In"
        return k
    cnt = Counter((r["q"], kgroup(r["kodaira"]), r["shape"], r["P_poly"] if r["shape"] != "ii" else "cubic")
                  for r in rows if "rule" in r["sample"])
    for k in sorted(cnt, key=lambda t: (t[0], t[1], t[2], t[3])):
        print(f"  q={k[0]}  {k[1]:5s} ({k[2]:>3s})  {k[3]:12s} {cnt[k]}")
    print(f"\nchecks failed: {len(failures)}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
