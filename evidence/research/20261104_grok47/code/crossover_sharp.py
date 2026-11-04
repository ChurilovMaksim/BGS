#!/usr/bin/env python3
"""Gas-vs-Robin crossover at a given delta_eff. mpmath, 80 digits.

Independent of V5/code/crossover_v5.py. Same mathematical inputs:
  b = (1 + R) exp(-delta), R = 6.234e-4 (lower bound used as an exact decimal input),
  G(p) = (2 b^p - 1)^2 - 1,
  K_p = 4 h_p^2 + 3, h_p the NSW recurrence h_1-slot = 7, h_3 = 7, h_5 = 41, ...
  Robin 1984 Thm 2: sigma(n)/n < exp(gamma) log log n + 0.6483 / log log n for n >= 3.
  I_p <= robin(log K_p) - ? The project uses robin(L) = e^gamma log L + 0.6483/log L - 1
  with L = log K_p, i.e. an upper bound for sigma(K_p)/K_p - 1.

Envelope: log K_p <= (2p+1) log eps, checked on a prime set.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80
OUTDIR = Path(__file__).resolve().parents[1] / "logs"

R = mp.mpf("6.234e-4")
GAM = mp.euler
EPS = 1 + mp.sqrt(2)
LNE = mp.log(EPS)


def h(p: int) -> int:
    a, b = 1, 7
    for _ in range((p - 1) // 2 - 1):
        a, b = b, 6 * b - a
    return b


def lnK(p: int) -> mp.mpf:
    K = 4 * h(p) ** 2 + 3
    return mp.log(K)


def robin(L: mp.mpf) -> mp.mpf:
    return mp.e ** GAM * mp.log(L) + mp.mpf("0.6483") / mp.log(L) - 1


def env_L(p: int) -> mp.mpf:
    return (2 * p + 1) * LNE


def G(p: int, delta: mp.mpf) -> mp.mpf:
    lnb = mp.log1p(R) - delta
    x = mp.e ** (p * lnb)
    return (2 * x - 1) ** 2 - 1


def primes_upto(n: int):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def run(delta_str: str):
    delta = mp.mpf(delta_str)
    # sanity: envelope dominates ln K on a sample
    sample = [5, 7, 11, 13, 31, 101, 1009, 1409, 3307]
    env_ok = all(lnK(p) <= env_L(p) for p in sample)
    primes = [p for p in primes_upto(6000) if p >= 1000]
    first_int = next(p for p in range(800, 6000) if G(p, delta) > robin(env_L(p)))
    first_prime = next(p for p in primes if G(p, delta) > robin(lnK(p)))
    viol = [p for p in primes if p >= first_prime and p <= 5000 and not (G(p, delta) > robin(lnK(p)))]
    # monotonicity at first_int: G' > env'
    lnb = mp.log1p(R) - delta
    x = mp.e ** (first_int * lnb)
    Gp = 4 * x * (2 * x - 1) * lnb
    # d/dp robin((2p+1) ln eps) = (e^gamma / L - 0.6483 /(L^2 log? wait)
    # robin(L) = e^g log L + 0.6483/log(L) - 1, L=(2p+1) lne
    # d robin/dp = d robin/dL * dL/dp
    # d robin/dL = e^g / L + 0.6483 * (-1)/(log(L)^2) * (1/L)
    #            = e^g / L - 0.6483 /(L log(L)^2)
    L = env_L(first_int)
    dRdL = mp.e ** GAM / L - mp.mpf("0.6483") / (L * (mp.log(L) ** 2))
    Ep = dRdL * (2 * LNE)
    return {
        "delta": delta_str,
        "env_sample_ok": env_ok,
        "first_int_envelope": first_int,
        "first_prime_exact": first_prime,
        "violations_primes_to_5000": viol,
        "Gprime": str(Gp),
        "envprime": str(Ep),
        "mono_ok": bool(Gp > Ep),
        "G_at_first_prime": str(G(first_prime, delta)),
        "robin_at_first_prime": str(robin(lnK(first_prime))),
    }


def main():
    deltas = sys.argv[1:] or ["3.4962e-4", "5.0313e-6"]
    rows = []
    for d in deltas:
        r = run(d)
        rows.append(r)
        print(d, r["first_int_envelope"], r["first_prime_exact"], r["mono_ok"], r["violations_primes_to_5000"])
    (OUTDIR / "crossover_sharp.json").write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
