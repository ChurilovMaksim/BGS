"""Verify lemma: #solutions in G^n to sum c_i x_i = 0 (all c_i != 0)."""
from itertools import product

def brute(p, coeffs):
    G = range(1, p)
    return sum(1 for pt in product(G, repeat=len(coeffs))
               if sum(c*x for c, x in zip(coeffs, pt)) % p == 0)

def closed_n3(p):
    return (p-1)*(p-2)

def closed_n4_v1(p):
    return (p-1)*(p*p-3*p+3)

for p in (5, 7, 11, 13):
    c3 = brute(p, [1, 1, 1])
    c4 = brute(p, [1, -2, 3, 5 % p if p > 5 else 4])
    print(f"p={p}: n3 brute={c3} closed={closed_n3(p)} "
          f"{'OK' if c3==closed_n3(p) else 'FAIL'} | "
          f"n4 brute={c4} v1={closed_n4_v1(p)} "
          f"{'OK' if c4==closed_n4_v1(p) else 'FAIL'}")
