import json, math, os
import numpy as np
from sympy import isprime

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
p = 4099
while not isprime(p):
    p += 1

# rebuild table (same as cchi_scaling)
xs = np.arange(1, p, dtype=np.int64)
inv = np.array([pow(int(x), p - 2, p) for x in xs], dtype=np.int64)
KT = np.zeros((p, p), dtype=np.complex128)
for s in range(p):
    vec = np.zeros(p, dtype=np.complex128)
    if s == 0:
        vec[1:] = 1.0
    else:
        vec[1:] = np.exp(2j * np.pi * (s * inv % p) / p)
    KT[s, :] = np.conj(np.fft.fft(np.conj(vec)))
print("table rebuilt")

us = np.arange(1, p)

def C_exact(lams, mus):
    cols = [((lam * us) % p) for lam in lams]
    total = 0.0 + 0.0j
    absacc = 0.0
    for v in range(1, p):
        row = KT[v]
        prod = row[cols[0]] * row[cols[1]] * row[cols[2]] * row[cols[3]]
        total += prod.sum()
        absacc += float(np.abs(prod).sum())
    return total, absacc

cases = {
    "generic1": [(1, 1), (2, 3), (5, 7), (11, 13)],
    "generic2": [(17, 19), (23, 29), (31, 37), (41, 43)],
    "generic3": [(101, 377), (211, 89), (5, 2003), (4093, 17)],
    "degenerate": [(3, 5), (3, 5), (3, 5), (3, 5)],
    "semidegenerate": [(3, 5), (3, 5), (7, 11), (13, 17)],
}
out = {}
print("EXACT correlation sums:")
for name, quads in cases.items():
    lams = [q[0] for q in quads]; mus = [q[1] for q in quads]
    tot, ab = C_exact(lams, mus)
    rec = {"absC": float(abs(tot)), "sum_abs_terms": ab,
           "cancel_factor": float(ab / max(abs(tot), 1e-300)),
           "absC_over_p3": float(abs(tot) / p ** 3)}
    out[name] = rec
    print(f"{name:15s}: |C|={abs(tot):.4e}  sum|terms|={ab:.4e}  "
          f"cancellation={rec['cancel_factor']:8.1f}x  |C|/p^3={rec['absC_over_p3']:.3f}")

json.dump({"p": p, "exact": out},
          open('artifacts/cchi_exact.json', 'w'), indent=1)
print("saved artifacts/cchi_exact.json")
