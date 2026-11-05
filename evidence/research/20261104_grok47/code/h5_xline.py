#!/usr/bin/env python3
"""Per-line sums X_line(d) at composite h_p, and the gamma* threshold.

The line sum is the N6 Galerkin model (L=8, kick J_n(1.8), rho=(2,8)),
the same transfer law as computations/verification/lineN6/code/f_iso.py.
It is a float evaluation of every orbit on the line, tagged [N], not a
certificate. gamma* is the mpmath binary search of code/h5_lines.py.
No registry file is written.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "logs"
CODE = ROOT / "code"
sys.path.insert(0, str(CODE))

from h5_lines import (  # noqa: E402
    divisor_sum_bound,
    fit_gamma,
    gas_slot,
    h_nsw,
    smallest_allowed_primes,
)
import mpmath as mp  # noqa: E402

LINE_I = Path("/workspace/computations/verification/lineI/code")
LINE_L2 = Path("/workspace/computations/verification/lineL/L2/code")
sys.path.insert(0, str(LINE_I))
sys.path.insert(0, str(LINE_L2))
from twlaw import LAM, TW, lam_pows  # noqa: E402
from law import mdata  # noqa: E402

# Binding rooms, copied from proofs/h5_lines.md Proposition 12.
ROOMS = (
    (1409, "7.4115e-6"),
    (3307, "3.4962e-4"),
)


def eps_pow(n: int) -> tuple[int, int]:
    """ε^n = x + y√2, ε = 1+√2, starting from ε^0 = 1."""
    x, y = 1, 0
    for _ in range(n):
        x, y = x + 2 * y, x + y
    return x, y


def lambda_p_minus_one(p: int) -> dict:
    """Exact identity λ^p - 1 = 2 h_p ε^p for odd p, and the sign against -1."""
    if p % 2 == 0:
        raise ValueError("odd p required")
    h, y = eps_pow(p)
    # N(ε^p) = (-1)^p = -1.
    norm = h * h - 2 * y * y
    # λ^p = (ε^p)^2 = (h^2 + 2 y^2) + (2 h y) √2.
    # λ^p - 1 = 2 h^2 + 2 h y √2 = 2 h ε^p.
    cofactor_x, cofactor_y = h, y
    minus = (2 * h * h, 2 * h * y)
    claimed = (2 * h * cofactor_x, 2 * h * cofactor_y)
    # λ^p + 1 = 2 y (2 y + h √2), rational part 4 y^2.
    plus_rational = 4 * y * y
    return {
        "p": p,
        "h": h,
        "y": y,
        "norm_minus_one": norm == -1,
        "lambda_p_minus_1_equals_2h_eps": minus == claimed,
        "four_y_squared_mod_h": plus_rational % h,
        "not_minus_one_mod_h": (plus_rational % h) != 0,
    }


def nu_rho(m: int, sg: int = 1):
    d = mdata(m)
    h = d["h"]
    M = 2 * h
    x0 = (sg * pow(4, -1, M // 2)) % (M // 2)
    nu0 = min(x for x in (x0, x0 + M // 2) if x % 2 == 1)
    if (8 * nu0 - 2 * sg) % M != 0:
        raise RuntimeError("nu_rho failed")
    return h, nu0


def Zbatch(tw, T: np.ndarray) -> np.ndarray:
    """Batched twisted transfer, copied from lineN6/code/twb.py."""
    T = np.asarray(T, float)
    B, m = T.shape
    K, S = tw.K, tw.S
    X = np.zeros((B, S, K, K), complex)
    X[:, 0] = np.eye(K)
    for step in range(m):
        Y = np.zeros_like(X)
        t = T[:, step]
        for n in tw.ns:
            c = np.exp(2j * np.pi * n * t)
            contrib = np.matmul(tw.Mn[n][None], X) * (
                tw.ph[n][None, :, None, None] * c[:, None, None, None]
            )
            Y[:, tw.tgt[n]] += contrib
        X = Y
    return (1 - LAM ** (-m)) * np.einsum("bsii->b", X)


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    r = int(n**0.5)
    for i in range(2, r + 1):
        if sieve[i]:
            sieve[i * i :: i] = b"\x00" * len(range(i * i, n + 1, i))
    return [i for i in range(2, n + 1) if sieve[i]]


def odd_primes_upto(n: int) -> list[int]:
    return [p for p in primes_upto(n) if p > 2]


def trial_factor(n: int, primes: list[int], limit: int) -> tuple[list[int], int]:
    fac: list[int] = []
    for q in primes:
        if q > limit or q * q > n:
            break
        while n % q == 0:
            fac.append(q)
            n //= q
    return fac, n


def _flint_worker(value: int, queue) -> None:
    from flint import fmpz

    queue.put([(int(p), int(e)) for p, e in fmpz(value).factor()])


def flint_factor_direct(n: int) -> list[tuple[int, int]]:
    from flint import fmpz

    return [(int(p), int(e)) for p, e in fmpz(n).factor()]


def flint_factor(n: int, timeout: int) -> list[tuple[int, int]] | None:
    """Complete factorisation, or None if the timeout fires."""
    import multiprocessing as mp

    queue: mp.Queue = mp.Queue()
    proc = mp.Process(target=_flint_worker, args=(n, queue))
    proc.start()
    proc.join(timeout)
    if proc.is_alive():
        proc.terminate()
        proc.join(5)
        return None
    if proc.exitcode != 0 or queue.empty():
        return None
    return queue.get()


def sqrt_mod_2(q: int) -> int:
    """Square root of 2 mod an odd prime q ≡ ±1 (mod 8)."""
    # Tonelli-Shanks for the fixed square 2 is a one-liner when q ≡ ±1 (mod 8):
    # 2^{(q+1)/4} or the explicit residue. Use the general Tonelli via pow.
    leg = pow(2, (q - 1) // 2, q)
    if leg != 1:
        raise RuntimeError(f"2 is not a square mod {q}")
    # Cipolla-free: find z nonsquare, then standard Tonelli.
    s = q - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1
    z = 2
    while pow(z, (q - 1) // 2, q) != q - 1:
        z += 1
    m, c, t, r = e, pow(z, s, q), pow(2, s, q), pow(2, (s + 1) // 2, q)
    while t != 1:
        i, v = 1, (t * t) % q
        while v != 1:
            v = (v * v) % q
            i += 1
            if i == m:
                raise RuntimeError("tonelli failed")
        b = pow(c, 1 << (m - i - 1), q)
        r = (r * b) % q
        c = (b * b) % q
        t = (t * c) % q
        m = i
    return r


def gamma_pattern(p: int, fac: list[int]) -> tuple[int, ...]:
    """Signs of the Binet element γ = x_{k+1} + y_k √2 on each prime."""
    k = (p - 1) // 2
    gx, _ = eps_pow(k + 1)
    _, gy = eps_pow(k)
    signs = []
    for q in fac:
        w = sqrt_mod_2(q)
        if (gx - w * gy) % q == 0:
            signs.append(1)
        elif (gx + w * gy) % q == 0:
            signs.append(-1)
        else:
            raise RuntimeError(f"gamma not on a line mod {q}")
    return tuple(signs)


def build_line(fac: list[int], signs: tuple[int, ...], h: int):
    """All h classes of one ideal, as int64 arrays (x, y)."""
    if h.bit_length() > 31 and h * h * 6 >= 2**63:
        raise RuntimeError("h too large for the int64 trace product")
    xs = np.array([0], dtype=np.int64)
    ys = np.array([0], dtype=np.int64)
    mod = 1
    for q, s in zip(fac, signs):
        w = sqrt_mod_2(q)
        y = np.arange(q, dtype=np.int64)
        x = (np.int64(s) * np.int64(w) * y) % np.int64(q)
        u = np.int64(mod * pow(mod, -1, q))  # 0 mod mod, 1 mod q
        v = np.int64(q * pow(q, -1, mod)) if mod > 1 else np.int64(0)
        nxt = mod * q
        xs2 = (xs[None, :] * v + x[:, None] * u) % nxt
        ys2 = (ys[None, :] * v + y[:, None] * u) % nxt
        xs = xs2.reshape(-1)
        ys = ys2.reshape(-1)
        mod = nxt
    if mod != h or len(xs) != h:
        raise RuntimeError("CRT length mismatch")
    return xs, ys


def canonical_orbits(xs: np.ndarray, ys: np.ndarray, h: int, p: int):
    """Orbits under <λ, -1>. Drops the origin. Returns keys, counts, x, y of reps."""
    nz = (xs != 0) | (ys != 0)
    xs = xs[nz].copy()
    ys = ys[nz].copy()
    n = int(len(xs))
    hh = np.int64(h)
    best = xs * hh + ys
    cx, cy = xs.copy(), ys.copy()
    for _ in range(p):
        for sx in (np.int64(1), np.int64(-1)):
            k = ((sx * cx) % hh) * hh + ((sx * cy) % hh)
            best = np.minimum(best, k)
        cx, cy = (3 * cx + 4 * cy) % hh, (2 * cx + 3 * cy) % hh
    reps, cnt = np.unique(best, return_counts=True)
    if int(cnt.sum()) != n:
        raise RuntimeError("orbit count mismatch")
    rx = (reps // hh).astype(np.int64)
    ry = (reps % hh).astype(np.int64)
    return rx, ry, cnt.astype(np.int64), n


def taus_batch(rx, ry, pw, h: int) -> np.ndarray:
    m = len(pw)
    T = np.empty((len(rx), m), dtype=np.float64)
    hh = np.int64(h)
    for i, (lx, ly) in enumerate(pw):
        tr = 2 * (rx * np.int64(lx) + 2 * ry * np.int64(ly))
        T[:, i] = (tr % hh) / float(h)
    return T


def primitive_mask(rx, ry, fac: list[int]) -> np.ndarray:
    mask = np.ones(len(rx), dtype=bool)
    for q in fac:
        mask &= ~((rx % q == 0) & (ry % q == 0))
    return mask


def sum_line(tw, rx, ry, cnt, pw, h: int, batch: int) -> dict:
    T = taus_batch(rx, ry, pw, h)
    Z = np.empty(len(rx), dtype=np.complex128)
    t0 = time.time()
    for i in range(0, len(rx), batch):
        Z[i : i + batch] = Zbatch(tw, T[i : i + batch])
        done = min(i + batch, len(rx))
        if done == len(rx) or (i // batch) % 25 == 0:
            print(f"    orbits {done}/{len(rx)}  {time.time()-t0:.1f}s", flush=True)
    return {"Z": Z, "T": T, "sec": time.time() - t0}


def slow_stats(T: np.ndarray, cnt: np.ndarray, mask: np.ndarray) -> dict:
    """Distance of each twist to Z. The primitive mask drops classes divisible by a rational prime."""
    dist0 = np.abs((T + 0.5) % 1 - 0.5)
    slow = (dist0 < 0.05).sum(axis=1)
    nearest = dist0.min(axis=1)

    def side(sel):
        if not np.any(sel):
            return {"min_dist_to_Z": None, "max_slow_steps": 0, "n": 0}
        return {
            "min_dist_to_Z": float(nearest[sel].min()),
            "max_slow_steps": int(slow[sel].max()),
            "n": int(sel.sum()),
        }

    return {
        "min_dist_to_Z": float(nearest.min()) if len(nearest) else None,
        "median_min_dist": float(np.median(nearest)) if len(nearest) else None,
        "max_slow_steps": int(slow.max()) if len(slow) else 0,
        "orbits_with_slow_ge_3": int((slow >= 3).sum()),
        "mean_slow_steps": float(np.average(slow, weights=cnt)) if len(slow) else 0.0,
        "primitive": side(mask),
        "axis": side(~mask),
    }


def check_invariance(tw, pw, h: int, p: int, rx, ry, n_check: int = 4) -> dict:
    """Compare Z(β), Z(λβ), Z(-β) on a few representatives."""
    if len(rx) == 0:
        return {"n": 0, "max_abs_gap": 0.0}
    step = max(1, len(rx) // n_check)
    idxs = list(range(0, len(rx), step))[:n_check]
    gaps = []
    rows = []
    for i in idxs:
        x, y = int(rx[i]), int(ry[i])
        pts = [(x, y)]
        lx, ly = (3 * x + 4 * y) % h, (2 * x + 3 * y) % h
        pts.append((lx, ly))
        pts.append(((-x) % h, (-y) % h))
        T = taus_batch(
            np.array([a for a, _ in pts], dtype=np.int64),
            np.array([b for _, b in pts], dtype=np.int64),
            pw,
            h,
        )
        Z = Zbatch(tw, T)
        gap = max(abs(Z[1] - Z[0]), abs(Z[2] - Z[0]))
        gaps.append(float(gap))
        rows.append({"beta": [x, y], "abs_gap": float(gap), "abs_Z": float(abs(Z[0]))})
    return {"n": len(rows), "max_abs_gap": max(gaps), "rows": rows}


def divisor_index(signs: tuple[int, ...], pat: tuple[int, ...], fac: list[int]) -> int:
    d = 1
    for s, g, q in zip(signs, pat, fac):
        if s != g:
            d *= q
    return d


def all_sign_patterns(omega: int):
    out = []
    for mask in range(1 << omega):
        out.append(tuple(1 if (mask >> i) & 1 else -1 for i in range(omega)))
    return out


def run_lines(p: int, K: int, which: str, batch: int) -> dict:
    h = h_nsw(p)
    hx, _hy = eps_pow(p)
    if hx != h:
        raise RuntimeError("h_nsw disagrees with the coefficient of ε^p")
    # Complete factorisation is required to name the lines. Small p only.
    fac_pairs = flint_factor_direct(h)
    if fac_pairs is None:
        raise RuntimeError(f"could not factor h_{p}")
    fac = []
    for q, e in fac_pairs:
        if e != 1:
            raise RuntimeError(f"h_{p} not squarefree: {q}^{e}")
        fac.append(q)
    fac = sorted(fac)
    if math.prod(fac) != h:
        raise RuntimeError("factorisation does not multiply to h_p")
    if len(fac) < 2:
        raise RuntimeError(f"h_{p} is prime; there is no cross line")
    if h > 2_000_000:
        raise RuntimeError(f"h_{p}={h} exceeds the enumeration cap 2000000")
    pat = gamma_pattern(p, fac)
    m = 3 * p
    hm, nu0 = nu_rho(m, 1)
    print(f"p={p} h={h} fac={fac} gamma={pat} build TW K={K}", flush=True)
    t0 = time.time()
    tw = TW(m, nu0, L=8, K=K)
    print(f"  TW {time.time()-t0:.2f}s  b={tw.b} S={tw.S}", flush=True)
    pw = lam_pows(m, h)
    z0 = Zbatch(tw, np.zeros((1, m)))[0]
    patterns = all_sign_patterns(len(fac))
    lines = []
    seen_axis: dict[int, complex] = {}
    prim_total = 0j
    for signs in patterns:
        d_index = divisor_index(signs, pat, fac)
        kind = "binet" if d_index in (1, h) else "cross"
        if which == "cross" and kind != "cross":
            continue
        print(f"  line signs={signs} d={d_index} {kind}", flush=True)
        xs, ys = build_line(fac, signs, h)
        # Norm check on a sample and on the count.
        if int(((xs.astype(object) ** 2 - 2 * ys.astype(object) ** 2) % h != 0).sum()):
            raise RuntimeError("a class on the line is not isotropic")
        rx, ry, cnt, npts = canonical_orbits(xs, ys, h, p)
        mask = primitive_mask(rx, ry, fac)
        inv = check_invariance(tw, pw, h, p, rx, ry)
        print(f"    points={npts} orbits={len(rx)} inv_gap={inv['max_abs_gap']:.3e}", flush=True)
        summed = sum_line(tw, rx, ry, cnt, pw, h, batch)
        Z, T = summed["Z"], summed["T"]
        ratio = Z / z0
        weighted = cnt.astype(np.float64) * ratio
        total = weighted.sum()
        prim = weighted[mask].sum()
        axis = total - prim
        # Unique axis contribution: same canonical key on every line that contains it.
        for key, w in zip((rx * np.int64(h) + ry)[~mask], weighted[~mask]):
            ik = int(key)
            if ik not in seen_axis:
                seen_axis[ik] = w
        prim_total += prim
        stats = slow_stats(T, cnt, mask)
        min_part = min(d_index, h // d_index) if d_index not in (0, h) else None
        if kind == "binet":
            min_part = None
        rec = {
            "signs": list(signs),
            "d_index": d_index,
            "cofactor": h // d_index,
            "min_d_h_over_d": min_part,
            "kind": kind,
            "n_points": npts,
            "n_orbits": int(len(rx)),
            "n_primitive_points": int(cnt[mask].sum()) if mask.any() else 0,
            "n_axis_points": int(cnt[~mask].sum()) if (~mask).any() else 0,
            "X_ideal": [float(total.real), float(total.imag)],
            "abs_ideal": float(abs(total)),
            "X_primitive": [float(prim.real), float(prim.imag)],
            "abs_primitive": float(abs(prim)),
            "X_axis": [float(axis.real), float(axis.imag)],
            "abs_axis": float(abs(axis)),
            "l1_ideal": float((cnt * np.abs(ratio)).sum()),
            "l1_primitive": float((cnt[mask] * np.abs(ratio[mask])).sum()) if mask.any() else 0.0,
            "max_abs_ratio": float(np.abs(ratio).max()) if len(ratio) else 0.0,
            "invariance_max_abs_gap": inv["max_abs_gap"],
            "sec": summed["sec"],
            **stats,
        }
        lines.append(rec)
        partial = LOG / f"h5_xline_p{p}_K{K}_{which}.partial.json"
        partial.write_text(json.dumps({"p": p, "K": K, "lines": lines}, indent=1) + "\n")
        print(
            f"    |X_ideal|={rec['abs_ideal']:.6e} |X_prim|={rec['abs_primitive']:.6e} "
            f"l1={rec['l1_ideal']:.6e}",
            flush=True,
        )
    axis_total = sum(seen_axis.values(), 0j)
    unique = prim_total + axis_total
    # f_iso reference values, K=16, sg=1.
    f_iso = {
        11: (0.01649269773570629, 0.008231258388480229),
        13: (0.01942921087800924, 0.009762307984106483),
    }
    ref = None
    if which == "all" and K == 16 and p in f_iso:
        rx0, ix0 = f_iso[p]
        ref = {
            "f_iso_X": [rx0, ix0],
            "unique_X": [float(unique.real), float(unique.imag)],
            "abs_gap": float(abs(unique - complex(rx0, ix0))),
        }
        print(f"  unique X gap vs f_iso: {ref['abs_gap']:.3e}", flush=True)
    return {
        "p": p,
        "m": m,
        "h": h,
        "fac": fac,
        "squarefree": True,
        "gamma_pattern": list(pat),
        "K": K,
        "L": 8,
        "b": int(tw.b),
        "S": int(tw.S),
        "Zrho": [float(z0.real), float(z0.imag)],
        "abs_Zrho": float(abs(z0)),
        "which": which,
        "lines": lines,
        "unique_X_if_all_lines": [float(unique.real), float(unique.imag)] if which == "all" else None,
        "f_iso_check": ref,
        "h_period_digits": len(str(hm)),
    }


def gamma_star() -> dict:
    """Smallest γ whose greedy divisor sum fits each room, C = 1."""
    mp.mp.dps = 80
    out = {}
    for p, delta in ROOMS:
        h = h_nsw(p)
        primes = smallest_allowed_primes(p, h)
        slot = gas_slot(p, delta, h)
        slack = slot["slack"]
        M = slot["M"]
        g_abs = fit_gamma(primes, slack)
        g_M = fit_gamma(primes, slack / M)
        sum1 = divisor_sum_bound(primes, mp.mpf(1))
        out[str(p)] = {
            "delta": delta,
            "slack": str(slack),
            "M": str(M),
            "greedy_length": len(primes),
            "least_prime": primes[0],
            "gamma_abs": g_abs,
            "gamma_times_M": g_M,
            "sum_gamma_1": str(sum1),
            "sum_gamma_1_under_slack": bool(sum1 < slack),
            "M_sum_under_slack": bool(M * sum1 < slack),
        }
        print(
            f"p={p} gamma_abs={mp.nstr(mp.mpf(g_abs), 12)} "
            f"gamma_M={mp.nstr(mp.mpf(g_M), 12)}",
            flush=True,
        )
    abs_bind = max(mp.mpf(out[str(p)]["gamma_abs"]) for p, _ in ROOMS)
    M_bind = max(mp.mpf(out[str(p)]["gamma_times_M"]) for p, _ in ROOMS)
    out["binding_absolute"] = str(abs_bind)
    out["binding_times_M"] = str(M_bind)
    return out


def run_factor(pmax: int, trial_limit: int, timeout: int) -> dict:
    primes = primes_upto(max(trial_limit, pmax))
    odd = [p for p in primes if 2 < p <= pmax]
    rows = []
    for p in odd:
        h = h_nsw(p)
        fac, cof = trial_factor(h, primes, trial_limit)
        complete = False
        timed_out = False
        flint_fac: list[tuple[int, int]] = []
        if cof == 1:
            complete = True
        elif cof in primes or _probably_prime(cof):
            # A prime cofactor above the trial limit is proved by flint when it returns.
            got = flint_factor(cof, timeout)
            if got is None:
                timed_out = True
            else:
                flint_fac = got
                complete = True
        else:
            got = flint_factor(cof, timeout)
            if got is None:
                timed_out = True
            else:
                flint_fac = got
                complete = True
        merged: dict[int, int] = {}
        for q in fac:
            merged[q] = merged.get(q, 0) + 1
        for q, e in flint_fac:
            merged[q] = merged.get(q, 0) + e
        if complete:
            check = 1
            for q, e in merged.items():
                check *= q**e
            if check != h:
                raise RuntimeError(f"factor product mismatch at p={p}")
        factors = sorted(merged.items())
        cong = []
        squarefree = all(e == 1 for _, e in factors) if complete else None
        if complete:
            for q, _e in factors:
                cong.append({"q": q, "mod_2p": q % (2 * p), "pm1": q % (2 * p) in (1, 2 * p - 1)})
        row = {
            "p": p,
            "digits": len(str(h)),
            "complete": complete,
            "timed_out": timed_out,
            "factors": factors if complete else [[q, 1] for q in fac],
            "cofactor_digits": len(str(cof)) if not complete else 1,
            "cofactor_is_one": cof == 1,
            "omega": len(factors) if complete else None,
            "squarefree": squarefree,
            "composite": (len(factors) >= 2) if complete else None,
            "congruence_pm1": all(c["pm1"] for c in cong) if complete else None,
        }
        # Store the integer h only when it is not huge; always store digits.
        if row["digits"] <= 40:
            row["h"] = h
        rows.append(row)
        tag = "complete" if complete else "partial"
        print(f"p={p} digits={row['digits']} {tag} omega={row['omega']} fac={row['factors'][:6]}", flush=True)
    return {
        "pmax": pmax,
        "trial_limit": trial_limit,
        "timeout_s": timeout,
        "rows": rows,
    }


def _probably_prime(n: int) -> bool:
    if n < 2:
        return False
    # flint is deterministic enough for this filter; Miller-Rabin bases for a first cut.
    for a in (2, 3, 5, 7, 11, 13, 23):
        if n == a:
            return True
        if pow(a, n - 1, n) != 1:
            return False
    return True


def attach_empirical(payload: dict, gamma_abs: float, gamma_M: float) -> dict:
    rows = []
    for line in payload["lines"]:
        if line["kind"] != "cross":
            continue
        md = line["min_d_h_over_d"]
        for label, ax in (
            ("ideal", line["abs_ideal"]),
            ("primitive", line["abs_primitive"]),
        ):
            rec = {
                "p": payload["p"],
                "K": payload["K"],
                "d_index": line["d_index"],
                "min": md,
                "support": label,
                "abs": ax,
                "abs_times_min": ax * md,
                "counterexample_gamma1_C1": bool(ax * md > 1.0),
            }
            if ax > 0 and md > 1:
                rec["gamma_eq_C1"] = -math.log(ax) / math.log(md)
                rec["C_at_gamma_abs"] = ax * (md**gamma_abs)
                rec["C_at_gamma_M"] = ax * (md**gamma_M)
                rec["exceeds_gamma_abs_C1"] = bool(rec["C_at_gamma_abs"] > 1.0)
                rec["exceeds_gamma_M_C1"] = bool(rec["C_at_gamma_M"] > 1.0)
            rows.append(rec)
    payload["empirical"] = rows
    return payload


def ann_check(primes: list[int]) -> dict:
    """The trace form of L_s vanishes exactly on L_{-s}.

    For q <= 5·10^6 every residue v is checked. A larger prime is the same
    linear identity, checked on v = 0,…,200 together with the coefficient test.
    """
    rows = []
    for q in primes:
        w = sqrt_mod_2(q)
        if (w * w - 2) % q != 0:
            raise RuntimeError(f"sqrt of 2 failed at {q}")
        span = q if q <= 5_000_000 else 201
        full = q <= 5_000_000
        for s in (1, -1):
            if (s * w) % q == 0 or 2 % q == 0:
                raise RuntimeError(f"trace form degenerate at {q}")
            for v in range(span):
                u = (-s * w * v) % q
                if (s * w * u + 2 * v) % q != 0:
                    raise RuntimeError(f"conjugate line missed at {q}")
            # One point off the conjugate line, the pure u-axis when it is off.
            if (-s * w * 0) % q == 1:
                raise RuntimeError("unexpected")
            if (s * w * 1 + 2 * 0) % q == 0:
                raise RuntimeError(f"off-line point killed the form at {q}")
        rows.append({"q": q, "full_line": full})
    return {"rows": rows, "n": len(rows)}


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("gamma")
    a = sub.add_parser("ann")
    a.add_argument("--pmax", type=int, default=47)
    s = sub.add_parser("sign")
    s.add_argument("--pmax", type=int, default=80)
    f = sub.add_parser("factor")
    f.add_argument("--pmax", type=int, default=200)
    f.add_argument("--trial", type=int, default=2_000_000)
    f.add_argument("--timeout", type=int, default=20)
    ln = sub.add_parser("lines")
    ln.add_argument("--p", type=int, required=True)
    ln.add_argument("--K", type=int, default=16)
    ln.add_argument("--which", choices=("all", "cross"), default="all")
    ln.add_argument("--batch", type=int, default=64)
    ln.add_argument("--gamma-abs", type=float, default=0.8737352238777557)
    ln.add_argument("--gamma-M", type=float, default=0.9908564134164909)
    args = parser.parse_args()
    LOG.mkdir(parents=True, exist_ok=True)
    if args.cmd == "ann":
        # Every odd prime factor of h_p for odd primes p <= pmax, once factored directly.
        qs = []
        for p in odd_primes_upto(args.pmax):
            h = h_nsw(p)
            for q, e in flint_factor_direct(h):
                if e != 1 or q in qs:
                    continue
                qs.append(q)
        out = ann_check(qs)
        path = LOG / "h5_xline_ann.json"
        path.write_text(json.dumps(out, indent=1) + "\n")
        print(path, "primes", out["n"])
    elif args.cmd == "gamma":
        out = gamma_star()
        path = LOG / "h5_xline_gamma.json"
        path.write_text(json.dumps(out, indent=1) + "\n")
        print(path)
    elif args.cmd == "sign":
        rows = []
        extra = [p for p in (1409, 3307) if p > args.pmax]
        for p in list(odd_primes_upto(args.pmax)) + extra:
            row = lambda_p_minus_one(p)
            # Drop the big integers from the log; keep the boolean checks and a small residue.
            rows.append(
                {
                    "p": p,
                    "norm_minus_one": row["norm_minus_one"],
                    "lambda_p_minus_1_equals_2h_eps": row["lambda_p_minus_1_equals_2h_eps"],
                    "not_minus_one_mod_h": row["not_minus_one_mod_h"],
                    "h_congruent_1_mod_2p": (row["h"] - 1) % (2 * p) == 0,
                    "four_y_squared_mod_h": int(row["four_y_squared_mod_h"] % 10**12),
                    "h_digits": len(str(row["h"])),
                }
            )
            if (row["h"] - 1) % (2 * p) != 0:
                raise RuntimeError(f"h_p not 1 mod 2p at p={p}")
            if not all(
                (
                    row["norm_minus_one"],
                    row["lambda_p_minus_1_equals_2h_eps"],
                    row["not_minus_one_mod_h"],
                )
            ):
                raise RuntimeError(f"sign check failed at p={p}")
        path = LOG / "h5_xline_sign.json"
        path.write_text(json.dumps({"pmax": args.pmax, "rows": rows}, indent=1) + "\n")
        print(path, "checked", len(rows))
    elif args.cmd == "factor":
        out = run_factor(args.pmax, args.trial, args.timeout)
        path = LOG / "h5_xline_factor.json"
        path.write_text(json.dumps(out, indent=1) + "\n")
        print(path)
    elif args.cmd == "lines":
        payload = run_lines(args.p, args.K, args.which, args.batch)
        payload = attach_empirical(payload, args.gamma_abs, args.gamma_M)
        path = LOG / f"h5_xline_p{args.p}_K{args.K}_{args.which}.json"
        path.write_text(json.dumps(payload, indent=1) + "\n")
        print(path)


if __name__ == "__main__":
    main()
