#!/usr/bin/env python3
"""[CA + N] Least prime factor of h_p below B = 10^8 for all primes 5 <= p <= 1500, and the Mersenne-type heuristic.

Independent re-implementation of research1105 code/audit_h5a/s7_smallfactors.py (BYPASS.md section 1.4):
  * divisibility test: lambda^p = (3 + 2 sqrt2)^p = 1 in Z[sqrt2]/q, which is equivalent to q | h_p for odd q
    because lambda^p - 1 = 2 h_p eps^p exactly and eps, 2 are units mod q (s7 tests the rational part of eps^p instead);
  * candidates: primes q <= B with q = 1 (mod 2p) and q = +-1 (mod 8); this presieve is justified by BGS-TRACE-348 [P]
    and was checked without presieve for q < 10^7 in h5_arith.py;
  * "good below B": h_p has no prime factor q <= B with q < h_p (h_p itself prime and <= B counts as good, as in s7);
  * heuristic [H]: Pr(no factor <= B) ~ prod over candidate q of (1 - 2p/(q - 1)); the reported number is the mean of
    this product over the p in each range.
The heuristic is a model, not a theorem; the comparison is numerical evidence only.  Output: ../logs/h5_density.json.
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, pathlib, sys, time
import numpy as np
from sympy import primerange

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "h5_density.json"
B, P = 10**8, 1500


def lam_pow_is_one(p, Q):
    rx = np.ones_like(Q); ry = np.zeros_like(Q); bx = np.full_like(Q, 3); by = np.full_like(Q, 2); e = p
    while e:
        if e & 1:
            rx, ry = (rx * bx % Q + 2 * (ry * by % Q)) % Q, (rx * by % Q + ry * bx % Q) % Q
        bx, by = (bx * bx % Q + 2 * (by * by % Q)) % Q, (2 * (bx * by % Q)) % Q
        e >>= 1
    return (rx == 1) & (ry == 0)


def h(p):
    a, b = 1, 1
    for _ in range(p - 1):
        a, b = b, 2 * b + a
    return b


def main():
    t0 = time.time()
    sv = np.ones(B + 1, dtype=bool); sv[:2] = False
    for i in range(2, int(B ** .5) + 1):
        if sv[i]:
            sv[i * i::i] = False
    rows = []
    for p in primerange(5, P + 1):
        q = np.arange(2 * p + 1, B + 1, 2 * p, dtype=np.int64)
        q = q[sv[q]]
        q = q[(q % 8 == 1) | (q % 8 == 7)]
        hit = [int(x) for x in q[lam_pow_is_one(p, q)]]
        hp = h(p)
        assert all(hp % x == 0 for x in hit)
        with np.errstate(divide='ignore'):  # q = 2p + 1 gives the factor 0 (it always divides, TRACE-350)
            heur = float(np.exp(np.sum(np.log1p(-2.0 * p / (q - 1.0)))))
        proper = [x for x in hit if x < hp]
        rows.append(dict(p=p, factors_le_B=hit, good_below_B=not proper, heur=heur, h_bits=hp.bit_length()))
    def summ(sub):
        return dict(n=len(sub), good=sum(r['good_below_B'] for r in sub), frac_good=round(sum(r['good_below_B'] for r in sub) / len(sub), 4),
                    heur_mean=round(float(np.mean([r['heur'] for r in sub])), 4))
    ranges = {f'{lo}-{hi}': summ([r for r in rows if lo <= r['p'] < hi]) for lo, hi in ((5, 200), (200, 500), (500, 1000), (1000, 1501))}
    hist = {}
    for r in rows:
        k = len([x for x in r['factors_le_B'] if x < 2 ** 200]); hist[k] = hist.get(k, 0) + 1
    res = dict(schema='bgs-h5-ceiling-density-v1', B=B, P=P, all=summ(rows), ranges=ranges, factor_count_histogram=dict(sorted(hist.items())),
               good_p=[r['p'] for r in rows if r['good_below_B']], certified_bad=sum(1 for r in rows if not r['good_below_B']),
               rows=rows, versions=dict(python=sys.version.split()[0], numpy=np.__version__), seconds=round(time.time() - t0, 1),
               non_claims='finite exact divisibility below 10^8 plus a heuristic model [H]; nothing about the density of good p is proved')
    OUT.write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps({k: res[k] for k in ('all', 'ranges', 'factor_count_histogram', 'certified_bad', 'seconds')}))


if __name__ == "__main__":
    main()
