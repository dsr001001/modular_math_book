#!/usr/bin/env python3
# Minimal stand-in for the gp binary, backed by the PARI library through cypari2.
# Supports what the pipeline uses: `gp -q [-s SIZE]` reading GP code from stdin.
import sys, cypari2
args = sys.argv[1:]; size = 256 * 10**6
if "-s" in args:
    v = args[args.index("-s") + 1].upper(); mult = {"K":10**3,"M":10**6,"G":10**9}
    size = int(float(v[:-1]) * mult[v[-1]]) if v[-1] in mult else int(v)
if "--version-short" in args:
    print(cypari2.Pari().version()); sys.exit(0)
pari = cypari2.Pari(); pari.allocatemem(size, silent=True) if 'silent' in pari.allocatemem.__doc__ else pari.allocatemem(size)
code = sys.stdin.read()
try:
    r = pari(code)
except Exception as e:
    print("  ***   " + str(e), file=sys.stderr); sys.exit(1)
