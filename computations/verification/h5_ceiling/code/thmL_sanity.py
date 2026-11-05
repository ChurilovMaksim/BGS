#!/usr/bin/env python3
"""[N] Sanity check of the leading terms of Theorem L (AUDIT_H5A section 5.4; NOT a registered claim) on prime levels.

For an odd prime p and a prime q | h_p (q <= QMAX), the ideal of norm q is pure (eps^p = +-1 in the field O/q), and the
characters of O/q are x -> e(a phi(x)/q), a in F_q, phi(a + b sqrt2) = a + b s with s^2 = 2 (mod q).  So
    M(q) = max_{a != 0} |eta(a)|,   eta(a) = sum_{m < p} e(a * phi(lambda)^m / q),
is the quantity of Theorem L.  We report M/p next to the leading terms (4/pi^2) theta, (8/pi^2) theta (pure case) and
4 theta - 1, theta = log_lambda(q)/p.  The O(sqrt p) and O(log p) error terms of the theorem are not explicit, so this is
a consistency check of orders of magnitude only, not a verification of the theorem.  Output: ../logs/thmL_sanity.json.
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, math, pathlib, sys
import numpy as np
from sympy import factorint, primerange, sqrt_mod

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "thmL_sanity.json"
QMAX, PMAX = 12_000_000, 61
LAM = 3 + 2 * math.sqrt(2)


def h(p):
    a, b = 1, 1
    for _ in range(p - 1):
        a, b = b, 2 * b + a
    return b


def main():
    rows = []
    for p in primerange(3, PMAX + 1):
        for q in sorted(factorint(h(p))):
            if q > QMAX:
                continue
            s = int(sqrt_mod(2, q)); lam = (3 + 2 * s) % q
            orb = [pow(lam, m, q) for m in range(p)]
            assert pow(lam, p, q) == 1 and lam != 1
            M = 0.0
            for a0 in range(1, q, 1 << 18):
                a = np.arange(a0, min(q, a0 + (1 << 18)), dtype=np.int64)
                acc = np.zeros(len(a), dtype=complex)
                for x in orb:
                    acc += np.exp(2j * np.pi * ((a * x) % q) / q)
                M = max(M, float(np.abs(acc).max()))
            th = math.log(q) / (p * math.log(LAM))
            rows.append(dict(p=p, q=q, theta=round(th, 5), M_over_p=round(M / p, 5), lead_4_pi2=round(4 / math.pi ** 2 * th, 5),
                             lead_8_pi2=round(8 / math.pi ** 2 * th, 5), lead_4theta_m1=round(4 * th - 1, 5), two_theta=round(2 * th, 5)))
            print(rows[-1], flush=True)
    ok8 = all(r['M_over_p'] >= r['lead_8_pi2'] for r in rows)
    below = [(r['p'], r['q']) for r in rows if r['M_over_p'] < r['lead_4theta_m1']]
    OUT.write_text(json.dumps(dict(schema='bgs-h5-thmL-sanity-v1', QMAX=QMAX, PMAX=PMAX, rows=rows,
                                   observed_above_8_over_pi2_theta_every_row=ok8,
                                   rows_below_bare_4theta_minus_1=below,
                                   note_4theta_minus_1='the bound (4 theta - 1 - o(1)) p is asymptotic; at these small p the o(1) term is not small',
                                   versions=dict(python=sys.version.split()[0], numpy=np.__version__),
                                   non_claims='numerical [N]; error terms not explicit; Theorem L is not registered'), indent=1) + "\n")
    print('M/p >= (8/pi^2) theta in every row:', ok8, len(rows), '; rows below bare 4 theta - 1:', below)


if __name__ == "__main__":
    main()
