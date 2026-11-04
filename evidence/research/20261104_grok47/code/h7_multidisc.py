"""Multi-disc vertex operator of TRACE-223, at a general conductor.

The one-step operator is the Line I / Line J lifted transfer operator on the
vertex discs, with the G2 automaton replaced by the sector scalar e(a n/8)
(TRACE-221) and the twist kept as the scalar e(n tau):

    (L_t Phi)_c = sum_n ghat(n) e(C n^2/2) e(n t) (M_{n,c} C_{n,c} Phi)_{c'}

    c' = round((c+n)/lambda),  C = -c0 on the b=8, a=+2 family,
    ghat(n) = i^n J_n(1.8), monomials u^k orthonormal in H^2 of the disc
    of radius rho centered at the integer c.

The per-step rate of a twist orbit is the spectral radius of the period
product, to the power 1/period. At level 7 this is the matrix whose
eigenvalues TRACE-223 certifies. The rank-40 single-disc family is a
different Galerkin of the same composition operator.

Commands
    python3 h7_multidisc.py calibrate
    python3 h7_multidisc.py orbits

The ball enclosure is h7_multidisc_cert.py. These two commands are float scans.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np
from scipy.special import jv

sys.path.insert(0, "/workspace/computations/verification/lineI/code")
from law import C0, LAM  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")
T_PRIME = 1.42785


def ghat_table(nmax: int) -> dict[int, complex]:
    out = {}
    for n in range(-nmax, nmax + 1):
        out[n] = (1j**n) * jv(n, 1.8)
    return out


def round_image(c: int, n: int, lam: float) -> tuple[int, float]:
    """j = round((c+n)/lambda), dl = (c+n)/lambda - j. lambda is irrational, so
    (c+n)/lambda is never a half-integer. Reject a float that lands too close."""
    val = (c + n) / lam
    j = int(math.floor(val + 0.5))
    dl = val - j
    if abs(abs(dl) - 0.5) < 1e-8:
        raise RuntimeError(f"rounding ambiguous at c={c}, n={n}, val={val}")
    if abs(dl) >= 0.5:
        raise RuntimeError(f"round failed at c={c}, n={n}")
    return j, dl


def build_letters(k0: int, rho: float, K: int, nmax: int):
    """Finite-section letters. Returns ns, matrices of shape (2*nmax+1, dim, dim),
    and the list of integer centres. A letter block that lands outside |c|<=k0
    is omitted here; tails.py bounds that omission."""
    lam = LAM
    C = float(-C0)
    centers = list(range(-k0, k0 + 1))
    index = {c: i for i, c in enumerate(centers)}
    dim = len(centers) * K
    gh = ghat_table(nmax)
    ns = list(range(-nmax, nmax + 1))
    # factorials
    fact = [1.0]
    for i in range(1, K + 1):
        fact.append(fact[-1] * i)
    lamp = [1.0]
    for i in range(1, K + 1):
        lamp.append(lamp[-1] / lam)
    mats = []
    n_kept = 0
    n_out = 0
    for n in ns:
        Mbig = np.zeros((dim, dim), dtype=complex)
        z = 2j * np.pi * C * n * rho
        # multiplication by exp(z u) in the monomial basis, shared by every disc
        # exp(z u) = sum z^m u^m/m!, so the monomial matrix is I on the diagonal.
        mult = np.eye(K, dtype=complex)
        zp = 1.0 + 0j
        for m in range(1, K):
            zp *= z / m
            for jj in range(0, K - m):
                mult[jj + m, jj] = zp
        phase_quad = np.exp(2j * np.pi * C * n * n / 2.0)
        for c in centers:
            j, dl = round_image(c, n, lam)
            if j not in index:
                n_out += 1
                continue
            n_kept += 1
            B = dl / rho
            comp = np.zeros((K, K), dtype=complex)
            if abs(B) < 1e-18:
                for jj in range(K):
                    comp[jj, jj] = lamp[jj]
            else:
                for k in range(K):
                    term = B**k  # jj = 0
                    comp[0, k] = term
                    for jj in range(1, k + 1):
                        term *= (k - jj + 1) / jj * (1.0 / lam) / B
                        comp[jj, k] = term
            block = (mult @ comp) * np.exp(2j * np.pi * C * n * c)
            r0 = index[c] * K
            q0 = index[j] * K
            Mbig[r0 : r0 + K, q0 : q0 + K] += block
        mats.append(Mbig * (gh[n] * phase_quad))
    meta = dict(k0=k0, rho=rho, K=K, nmax=nmax, dim=dim, n_kept=n_kept, n_out=n_out, centers=centers)
    return np.array(ns), np.stack(mats), meta


def L_of(ns, mats, t: float) -> np.ndarray:
    w = np.exp(2j * np.pi * ns * (t % 1.0))
    return np.tensordot(w, mats, axes=(0, 0))


def lambda_powers(d: int) -> list[tuple[int, int]]:
    x, y = 1, 0
    out = []
    for _ in range(d + 2):
        out.append((x % d, y % d))
        x, y = (3 * x + 4 * y) % d, (2 * x + 3 * y) % d
        if (x % d, y % d) == (1, 0):
            return out
    raise RuntimeError(f"no return mod {d}")


def twists(d: int, bx: int, by: int, pw) -> list[int]:
    return [(2 * (bx * x + 2 * by * y)) % d for (x, y) in pw]


def product_rate(ns, mats, phases: list[float]) -> float:
    dim = mats.shape[1]
    Q = np.eye(dim, dtype=complex)
    log_scale = 0.0
    for t in phases:
        Q = L_of(ns, mats, t) @ Q
        nrm = np.linalg.norm(Q, ord="fro")
        if nrm > 1e6 or nrm < 1e-6:
            Q /= nrm
            log_scale += math.log(nrm)
    ev = np.linalg.eigvals(Q)
    m = max(abs(z) for z in ev)
    return math.exp((math.log(m) + log_scale) / len(phases))


def orbit_phases(d: int, bx: int, by: int, a: int) -> list[float]:
    pw = lambda_powers(d)
    return [((a / 8.0) + tw / d) % 1.0 for tw in twists(d, bx, by, pw)]


def one_step_radius(ns, mats, t: float) -> float:
    ev = np.linalg.eigvals(L_of(ns, mats, t))
    return max(abs(z) for z in ev)


def calibrate():
    """Level-7 targets: sector 0 at phase 0 should see mu*, and the two
    published orbits should see the TRACE-223 discs."""
    rows = []
    for K, k0, nmax in ((20, 3, 12), (30, 4, 14), (40, 5, 16)):
        t0 = time.time()
        ns, mats, meta = build_letters(k0, 1.2, K, nmax)
        r0 = one_step_radius(ns, mats, 0.0)
        # class (2,1), sector 4; class (1,3), sector 6. Representatives as in
        # the level-7 self-test of h7_rates.py: (2,1) sector 4 and (1,3) sector 6.
        r21 = product_rate(ns, mats, orbit_phases(7, 2, 1, 4))
        r13 = product_rate(ns, mats, orbit_phases(7, 1, 3, 6))
        row = dict(K=K, k0=k0, nmax=nmax, dim=meta["dim"], mu_star=r0, rate_2_1=r21, rate_1_3=r13, seconds=round(time.time() - t0, 2))
        print(row, flush=True)
        rows.append(row)
    return rows


ORBITS = [
    ("level7_2_1", 7, 2, 1, 4),
    ("level7_1_3", 7, 1, 3, 6),
    ("d3437426497", 3437426497, -208, 0, 0),
    ("d24061985479", 24061985479, 227, 227, 0),
    ("d2735635252619983", 2735635252619983, -89, 0, 0),
]


def orbits():
    rows = []
    grid = ((16, 2, 10), (24, 3, 12), (30, 4, 14), (36, 5, 16))
    for K, k0, nmax in grid:
        t0 = time.time()
        ns, mats, meta = build_letters(k0, 1.2, K, nmax)
        print("built", meta, "in", round(time.time() - t0, 2), flush=True)
        for name, d, bx, by, a in ORBITS:
            t1 = time.time()
            rate = product_rate(ns, mats, orbit_phases(d, bx, by, a))
            row = dict(name=name, d=d, beta=[bx, by], sector=a, K=K, k0=k0, nmax=nmax, dim=meta["dim"], rate=rate, above=rate > T_PRIME, seconds=round(time.time() - t1, 2))
            print(row, flush=True)
            rows.append(row)
    return rows


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "calibrate"
    os.makedirs(LOG_DIR, exist_ok=True)
    if cmd == "calibrate":
        rows = calibrate()
        json.dump(rows, open(os.path.join(LOG_DIR, "h7_multidisc_calibrate.json"), "w"), indent=1)
    elif cmd == "orbits":
        rows = orbits()
        json.dump(rows, open(os.path.join(LOG_DIR, "h7_multidisc_orbits.json"), "w"), indent=1)
    else:
        raise SystemExit(f"unknown command {cmd}")


if __name__ == "__main__":
    main()
