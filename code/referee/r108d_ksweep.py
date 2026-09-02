r"""R108d -- THE K-SWEEP: the true empirical law of the k=4 coupled energy.

For a spread of split primes N (5 QR mod N) with design element
a = (3+sqrt(5))/2 mod N of order K, compute exactly:

  - E_c (H-coupled), E_unc, delta_full = E_c/(E_unc/m^4) - 1
  - cross-term share: (m^4 E_c - E_unc - sum_nontriv)/E_unc
  - nontriv pair share: sum_nontriv/E_unc
  - delta_half for the H_+ = H.<-1> coupling (K odd only)
  - delta_odd: the twisted odd-coset energy (desymmetrised sector model):
        B_odd = (1/m_+^2) sum_{(j1,j2) both odd} (A_j1j2 * A_j1j2)
        delta_odd = E_odd * m_+^4 / E_unc - 1
  - per-fiber Weil margin: max |A_psi(d)|/sqrt(N), nontriv pairs, d != 0
  - the DIRECT BGS quantities from B: mean_q Sigma_4, std_q Sigma_4,
    rel_4 = std/mean, and Z_0 = B(0).

Memory discipline (post-restart): H3 built as int64 in halves then cast
to int32; A stored as complex64; histogram deleted before per-pair pass.
Incremental JSON saves with resume.
"""
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108d_ksweep.log")
JSON_PATH = os.path.join(OUT_DIR, "r108d_ksweep.json")

sys.path.insert(0, HERE)
from r108_k4_independent import (  # noqa: E402
    build_keys, discrete_log_table as dlog_table,
    multiplicative_order, primitive_root,
)

_t0 = time.time()


def log(msg):
    print(str(msg), flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True


def sqrt_mod(n, p):
    rs = []
    for r in range(p):
        if r * r % p == n % p:
            rs.append(r)
            if len(rs) == 2:
                break
    return rs


def factor(n):
    fs = {}
    while n % 2 == 0:
        fs[2] = fs.get(2, 0) + 1
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            fs[f] = fs.get(f, 0) + 1
            n //= f
        f += 2
    if n > 1:
        fs[n] = fs.get(n, 0) + 1
    return fs


def order_fast(a, p, fac):
    o = p - 1
    for q, e in fac.items():
        while o % q == 0 and pow(a, o // q, p) == 1:
            o //= q
    return o


def find_designs(max_n=12500, mem_cap=2.0e8):
    """Split primes with design (3+sqrt5)/2; one per K, preferring larger N."""
    by_k = {}
    fac_cache = {}
    for N in range(1009, max_n, 2):
        if not is_prime(N) or N % 5 not in (1, 4):
            continue
        rs = sqrt_mod(5, N)
        if not rs:
            continue
        inv2 = pow(2, N - 2, N)
        fac = fac_cache.setdefault(N, factor(N - 1))
        for r in rs:
            a = (3 + r) * inv2 % N
            K = order_fast(a, N, fac)
            m = (N - 1) // K
            if m * m * N > mem_cap or m < 2:
                continue
            rec = (N, a, K, m, m * m * N)
            if K not in by_k or rec[4] > by_k[K][4]:
                by_k[K] = rec
    return sorted(by_k.values(), key=lambda t: (t[2], t[0]))


def pipeline(N, a, want_half=True):
    K = multiplicative_order(a, N)
    m = (N - 1) // K
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ell = int(dlog[a])
    assert ell % m == 0
    u, v, d, mult = build_keys(N)
    c1 = (dlog[u] % m).astype(np.int32)
    c2 = (dlog[v] % m).astype(np.int32)
    flat = (c1.astype(np.int64) * m + c2) * N + d
    H3 = np.zeros(m * m * N, dtype=np.int64)
    mid = m // 2
    for lo, hi in ((0, mid), (mid, m)):
        sel = (c1 >= lo) & (c1 < hi)
        if not sel.any():
            continue
        f = ((c1[sel] - lo).astype(np.int64) * m * N
             + c2[sel] * N + d[sel])
        part = np.bincount(
            f, weights=mult[sel].astype(np.float64), minlength=(hi - lo) * m * N
        )
        H3[lo * m * N : hi * m * N] += part.astype(np.int64)
        del part, f
    H3 = H3.reshape(m, m, N).astype(np.int32)  # halve histogram memory
    c_counts = H3.sum(axis=(0, 1))
    chat = np.fft.fft(c_counts.astype(np.float64))
    E_unc = float(np.sum(np.abs(chat) ** 4) / N)

    mp = m * m
    A = np.empty((mp, N), dtype=np.complex64)  # 1e-7 rel precision, ample
    CH = 512
    for d0 in range(0, N, CH):
        d1 = min(d0 + CH, N)
        Af = np.fft.fft2(H3[:, :, d0:d1], axes=(0, 1))
        A[:, d0:d1] = Af.reshape(mp, d1 - d0).astype(np.complex64)
    del H3  # free histogram memory

    j1 = np.arange(mp) // m
    j2 = np.arange(mp) % m
    odd_mask = (j1 % 2 == 1) & (j2 % 2 == 1)
    nontriv_mask = np.ones(mp, dtype=bool)
    nontriv_mask[0] = False
    half_mask = (j1 % 2 == 0) & (j2 % 2 == 0)

    # NOTE on masks under the fft2 (-) sign convention: index j corresponds
    # to character chi_{K(-j mod m)}; parity of j is preserved, so the
    # even/odd coset masks are exactly right, and (0,0) is the trivial pair.
    Ah2_full = np.zeros(N, dtype=np.complex128)
    Ah2_odd = np.zeros(N, dtype=np.complex128)
    Ah2_half = np.zeros(N, dtype=np.complex128)
    E_pair = np.empty(mp, dtype=np.float64)
    maxA = 0.0
    PCH = 2048
    for p0 in range(0, mp, PCH):
        p1 = min(p0 + PCH, mp)
        blk = A[p0:p1, :].astype(np.complex128)
        Ah = np.fft.fft(blk, axis=1)
        E_pair[p0:p1] = (np.abs(Ah) ** 4).sum(axis=1) / N
        sq = Ah**2
        Ah2_full += sq.sum(axis=0)
        if odd_mask[p0:p1].any():
            Ah2_odd += sq[odd_mask[p0:p1]].sum(axis=0)
        if half_mask[p0:p1].any():
            Ah2_half += sq[half_mask[p0:p1]].sum(axis=0)
        if nontriv_mask[p0:p1].any():
            bn = blk[nontriv_mask[p0:p1]][:, 1:]
            maxA = max(maxA, float(np.max(np.abs(bn))))
    del A

    Bf = np.fft.ifft(Ah2_full / mp)
    B = Bf.real
    E_c = float(np.sum(B**2))
    Bo = np.fft.ifft(Ah2_odd / max(1, int(odd_mask.sum()))).real
    E_odd = float(np.sum(np.abs(Bo) ** 2))
    E_triv = float(E_pair[0])
    nontriv_sum = float(E_pair[1:].sum())
    cross = mp * mp * E_c - (E_unc + nontriv_sum)

    # Sigma_4 statistics from B (q in F_N^*)
    qv = np.arange(1, N)
    ph = np.exp(2j * np.pi * np.outer(qv, np.arange(N)) / N)
    S4 = (ph @ B).real
    mean_S4 = float(S4.mean())
    std_S4 = float(S4.std())

    out = dict(
        K=K, m=m, E_c=E_c, E_unc=E_unc, E_triv=E_triv,
        nontriv_share=nontriv_sum / E_unc,
        cross_share=cross / E_unc,
        delta_full=E_c / (E_unc / mp**2) - 1,
        max_E_nontriv=float(E_pair[1:].max()),
        maxA_over_sqrtN=maxA / math.sqrt(N),
        mean_S4=mean_S4, std_S4=std_S4,
        rel4=std_S4 / mean_S4 if mean_S4 else float("nan"),
        Z0=float(B[0]),
        imag_err=float(np.max(np.abs(Bf.imag))),
    )
    if want_half and K % 2 == 1:
        Bh = np.fft.ifft(Ah2_half / max(1, int(half_mask.sum()))).real
        E_half = float(np.sum(Bh**2))
        m_plus = m // 2
        out["delta_half"] = E_half / (E_unc / m_plus**4) - 1
        out["delta_odd"] = E_odd / (E_unc / m_plus**4) - 1
        out["m_plus"] = m_plus
    return out


def main():
    log("R108d K-sweep (curated): true law of the k=4 coupled energy")
    curated = [
        (199, 139),    # paper design K=11
        (3571, 2469),  # paper design K=17 (m=210)
        (2161, None), (6709, None), (3001, None), (2521, None),
        (4481, None), (4021, None), (4969, None), (7879, None),
        # (10711, None) dropped in R108: build_keys meshgrid needs ~7.3GB
        # at N~10711 (memory-guard kill); chunked construction is future
        # work if the N>1e4 regime is needed.
        (5081, None), (1511, None), (9521, None),
        (5881, None), (6871, None), (5281, None),
        # (12391, None) dropped: same memory reason (~9.8GB).
        (1229, None),
    ]
    all_des = {t[0]: t for t in find_designs()}
    designs = []
    for N, a in curated:
        if a is not None:
            K = multiplicative_order(a, N)
            designs.append((N, a, K, (N - 1) // K))
        elif N in all_des:
            designs.append(all_des[N][:4])
    for N, a, K, m in designs:
        log(f"  N={N} K={K} m={m}")
    rows = {}
    if os.path.exists(JSON_PATH):
        try:
            rows = json.load(open(JSON_PATH))
            log(f"resuming with {len(rows)} completed designs")
        except Exception:
            rows = {}
    for N, a, K, m in designs:
        key = f"N{N}_K{K}"
        if key in rows:
            log(f"=== {key} already done, skip")
            continue
        log(f"=== {key} a={a} ===")
        try:
            r = pipeline(N, a)
        except Exception as exc:  # keep sweep alive
            log(f"  FAILED: {exc}")
            continue
        rows[key] = dict(N=N, a=a, **r)
        with open(JSON_PATH, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=1, default=float)  # incremental save
        log(f"  delta_full={r['delta_full']*100:+.2f}%  "
            f"cross/E_unc={r['cross_share']:.4f}  "
            f"nontriv/E_unc={r['nontriv_share']:.2e}")
        if "delta_half" in r:
            log(f"  delta_half={r['delta_half']*100:+.2f}%  "
                f"delta_odd={r['delta_odd']*100:+.2f}%")
        log(f"  maxA/sqrtN={r['maxA_over_sqrtN']:.2f}  "
            f"rel4={r['rel4']:.4f}  Z0={r['Z0']:.0f}  "
            f"meanS4={r['mean_S4']:.1f}")
    log(f"WROTE {JSON_PATH} ({time.time() - _t0:.1f}s)")


if __name__ == "__main__":
    main()
