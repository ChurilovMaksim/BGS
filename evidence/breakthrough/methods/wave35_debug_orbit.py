"""Debug: TM orbit vs direct row orbit for one split fiber at (21,2401)."""
import sys
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import (Dm, snf_kernel, gamma_perms, lex_canon,
                                 group_ids)
m, q, p, f = 21, 2401, 7, 2
mod = 49
pts = snf_kernel(m, q)
fib = group_ids(np.sort(pts, axis=1))
perms = gamma_perms(m)
canon = lex_canon(pts, perms, chunk=500)
gam = group_ids(canon)
# find a split fiber
for fi in range(int(fib.max()) + 1):
    idx = np.where(fib == fi)[0]
    opf = len(set(gam[idx].tolist()))
    if opf > 1:
        print("fiber", fi, "size", len(idx), "orbits", opf)
        rep = pts[idx[0]]
        print("rep row:", rep.tolist())
        # row orbit via perms directly
        orb_rows = set()
        for pr in perms:
            orb_rows.add(tuple(rep[list(pr)].tolist()))
        print("direct row orbit size:", len(orb_rows))
        # trace model C for rep: row = 49 * w, w0 = rep[0]/49, w1 = rep[1]/49
        assert all(v % 49 == 0 for v in rep)
        w0 = int(rep[0]) // 49; w1 = int(rep[1]) // 49
        inv2 = pow(2, -1, mod); inv8 = pow(8, -1, mod)
        a = (w0 * inv2) % mod; b = ((w1 - 6 * a) * inv8) % mod
        print("C = ", (a, b), " C mod 7 =", (a % 7, b % 7))
        # alpha powers mod 49
        A = [(1, 0)]
        for _ in range(m):
            x, y = A[-1]
            A.append(((3 * x + 4 * y) % mod, (2 * x + 3 * y) % mod))
        print("alpha^21 mod 49 =", A[21], " alpha^3 mod 49 =", A[3])
        orbC = set()
        for j in range(m):
            aj, bj = A[j]
            orbC.add(((a * aj + 2 * b * bj) % mod, (a * bj + b * aj) % mod))
            orbC.add(((a * aj - 2 * b * bj) % mod, (-a * bj + b * aj) % mod))
        print("TM C-orbit size:", len(orbC))
        # is conj(C) in shift orbit?
        conj = (a, (-b) % mod)
        shifts = set()
        for j in range(m):
            aj, bj = A[j]
            shifts.add(((a * aj + 2 * b * bj) % mod, (a * bj + b * aj) % mod))
        print("conj in shifts:", conj in shifts)
        # rows from TM orbit C's vs direct orbit rows
        tm_rows = set()
        for (ca, cb) in orbC:
            tr = []
            for j in range(m):
                aj, bj = A[j]
                tr.append((49 * (2 * (ca * aj + 2 * cb * bj) % mod)) % q)
            tm_rows.add(tuple(tr))
        print("rows from TM orbit:", len(tm_rows), " direct orbit rows:", len(orb_rows))
        print("tm_rows == orb_rows:", tm_rows == orb_rows)
        break
