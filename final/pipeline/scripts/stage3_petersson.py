"""Stage 3, item 9: Remark rem:degree of ../paper/note.tex. With c_E = 1,
   deg phi = N L^nv(ad f, 1) / (2 pi vol(Lambda_E)),   L^nv(ad f,1) = L^nv(Sym^2 f, 2) = L(Sym^2 f, 2) prod_{q^2 | N} P_q(q^-2),
L(Sym^2 f, s) = lfunsympow(E, 2), P_q from lfuneuler, vol(Lambda_E) = |Im(conj(w1) w2)| from E.omega (covolume of the period lattice of the
minimal model). Computed at 60 significant digits; reports the number of agreeing digits with the tables' degree.
Usage: python3 scripts/stage3_petersson.py -> results/stage3_petersson.txt (stdout)"""
import time, cypari2
pari = cypari2.Pari(); pari.allocatemem(800_000_000); pari.set_real_precision(60)
CURVES = {"11a1": ([0, -1, 1, -10, -20], 1), "121a1": ([1, 1, 1, -30, -76], 6), "539d1": None, "1232l1": None, "726a1": None}
import pandas as pd
c = pd.read_parquet("data/curves.parquet", columns=["label", "ainvs", "moddeg"]).set_index("label")
for lab in CURVES: CURVES[lab] = (c.ainvs[lab], int(c.moddeg[lab]))
pari("default(realprecision, 60)")
pari("""pet(a) = my(E = ellminimalmodel(ellinit(a)), N = ellglobalred(E)[1], S = lfunsympow(E, 2), L2 = lfun(S, 2), c = 1, w = E.omega);
  foreach(factor(N)[,1], q, if(N % q^2 == 0, c *= subst(1/lfuneuler(S, q), x, 1/q^2)));
  [N, N * L2 * c / (2 * Pi * abs(imag(conj(w[1]) * w[2]))), E.area];""")
for lab, (ai, deg) in CURVES.items():
    t0 = time.time()
    N, val, area = pari(f"pet({ai})")
    err = abs(val - deg); digits = -pari.log(err / deg) / pari.log(10) if err != 0 else 60
    print(f"{lab}: N={N} table deg {deg}; formula {str(val)[:50]}; |rel err| {float(err / deg):.2e}; agreeing digits ~{float(digits):.1f}; {int(pari.bitprecision(val))} bits; {time.time() - t0:.1f} s", flush=True)
