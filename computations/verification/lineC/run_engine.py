"""Drive engine.cpp: symbolic large-p expansion of E_theta|Tr U^m|^2 (same output format as symbolic.py)."""
import sys, subprocess, math
from fractions import Fraction
from gauss_exact import rho_classes, w_coeffs
from symbolic import sqf
m = int(sys.argv[1]); NS = int(sys.argv[2]) if len(sys.argv) > 2 else 8
MAXDEF = int(sys.argv[3]) if len(sys.argv) > 3 else 99
cl = [(r, mu) for r, mu in rho_classes(m, MAXDEF if MAXDEF < 99 else None).items()]; w = w_coeffs(m)
if MAXDEF < 99: print(f'# only partitions with deficit <= {MAXDEF}: coefficients valid only for orders p^e with e >= -{MAXDEF}-1/2 (deficit d contributes only at e <= -d)')
inp = ''.join(f'{i} {m} {max(r)+1} ' + ' '.join(map(str, r)) + '\n' for i, (r, mu) in enumerate(cl))
procs = [subprocess.Popen(['./engine', str(s), str(NS)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) for s in range(NS)]
for p in procs: p.stdin.write(inp); p.stdin.close()
E = {}; byclass = {}
for p in procs:
    for line in p.stdout:
        i, r, D, cntm, s0 = map(int, line.split()); cnt = Fraction(cntm, s0)
        rho, mult = cl[i]; n = max(rho)+1
        W = Fraction(mult)
        stab = 1
        for b in range(n): W *= w[rho.count(b)]; stab *= math.factorial(rho.count(b))
        co = W*cnt*stab           # each distinct word = stab permutations sigma
        e = Fraction(2*n - r, 2) - m
        Dp = sqf(((-1)**(r//2))*(2**r)*D) if r > 0 else 1
        key = (e, r % 2, Dp); E[key] = E.get(key, Fraction(0)) + co
        dk = (e, m-n, r, Dp); byclass[dk] = byclass.get(dk, Fraction(0)) + co
    p.wait(); assert p.returncode == 0
print(f'm={m}')
for key in sorted(E, key=lambda k: (-k[0], k[1], k[2])):
    if E[key] == 0: continue
    e, odd, D = key
    print(f'   p^{str(e):>6}  {"eps*" if odd else "    "}({D:>4}/p) : {E[key]}')
print('decomposition of orders >= p^-3 by (deficit, rank):')
for dk in sorted(byclass, key=lambda k: (-k[0], k[1], k[2], k[3])):
    if dk[0] >= -3 and byclass[dk] != 0:
        print(f'   p^{str(dk[0]):>5} deficit={dk[1]} rank={dk[2]} char=({dk[3]}/p): {byclass[dk]}')
