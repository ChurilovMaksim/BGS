"""Decompose the p^{-1} and p^{-2} coefficients (trivial-character part, large p) by (deficit, rank)."""
import sys, itertools
from fractions import Fraction
from gauss_exact import rho_classes, w_coeffs, form_matrix, diag_Q
from symbolic import sqf
m = int(sys.argv[1])
w = w_coeffs(m); out = {}; cache = {}
for rho, mult in rho_classes(m).items():
    n = max(rho)+1; d = m-n
    if d > 2: continue
    W = Fraction(mult)
    for b in range(n): W *= w[rho.count(b)]
    for perm in itertools.permutations(range(m)):
        word = tuple(rho[perm[j]] for j in range(m))
        B = form_matrix(rho, word, n)
        if B not in cache: cache[B] = diag_Q(B)[:2]
        r, D = cache[B]
        if 2*d + r > 4: continue
        Dp = sqf(((-1)**(r//2))*(2**r)*D) if r > 0 else 1
        key = (2*d+r, d, r, Dp); out[key] = out.get(key, Fraction(0)) + W
for k in sorted(out):
    if out[k]: print(f'm={m} order p^-{Fraction(k[0],2)} deficit={k[1]} rank={k[2]} char=({k[3]}/p): {out[k]}')
