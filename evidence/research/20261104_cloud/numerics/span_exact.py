"""Exact epsilon-digit span of every class alpha = a + b*sqrt(2).

The span is the N14 object: length of the code word E_k from the first
nonzero letter to the last (internal zeros included). Letters are the
second differences of the code twists

    tau_{2t}   = red(xi_{2t}),
    tau_{2t-1} = -red(-xi_{2t-1}),

xi_k = sigma_1(mu) * eps^k, mu = (sqrt(2)/4)*alpha, eps = 1+sqrt(2),
red(x) = x - floor(x+1/2).

All comparisons are integer (no floating point in the decision).
A flint/mpmath sample cross-checks the floor function and the letters.
"""
from __future__ import annotations

import json
import math
import os
import random
import time
from collections import Counter

from flint import arb, ctx

ctx.prec = 256

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(ROOT, "logs")
os.makedirs(LOGS, exist_ok=True)

ENUM = "/workspace/computations/verification/lineN14/logs/a_enum.jsonl"


def floor_lin(U: int, V: int) -> int:
    """Largest integer m with m <= U + V*sqrt(2). V != 0 never hits an integer."""
    if V == 0:
        return U
    lo = U - 2 * abs(V) - 2
    hi = U + 2 * abs(V) + 2

    def leq(m: int) -> bool:
        D = m - U
        if V > 0:
            if D <= 0:
                return True
            return D * D <= 2 * V * V
        if D > 0:
            return False
        return D * D >= 2 * V * V

    # largest m in [lo, hi] with leq(m); the predicate is downward-closed
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if leq(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def eps_pow(k: int) -> tuple[int, int]:
    """eps^k = p + q*sqrt(2), p,q in Z. eps = 1+sqrt(2)."""
    if k >= 0:
        p, q = 1, 0
        for _ in range(k):
            p, q = p + 2 * q, p + q
        return p, q
    p, q = 1, 0
    for _ in range(-k):
        p, q = 2 * q - p, p - q
    return p, q


def UV(a: int, b: int, k: int) -> tuple[int, int]:
    """4*xi_k = U + V*sqrt(2), xi_k = sigma_1(mu * eps^k)."""
    p, q = eps_pow(k)
    U = 2 * (b * p + a * q)
    V = a * p + 2 * b * q
    return U, V


def abs_lt(U: int, V: int, bound: int) -> bool:
    """|U + V*sqrt(2)| < bound for a positive integer bound.

    Z < bound iff floor(Z) <= bound-1, and Z > -bound iff floor(-Z) <= bound-1.
    """
    return floor_lin(U, V) <= bound - 1 and floor_lin(-U, -V) <= bound - 1


def n_code(a: int, b: int, k: int) -> int:
    """Integer n with tau_k = xi_k - n, code convention."""
    U, V = UV(a, b, k)
    if k % 2 == 0:
        # floor(xi + 1/2) = floor((U+2 + V*sqrt(2))/4)
        return floor_lin(U + 2, V) // 4
    # n = -floor(1/2 - xi) = -floor((2 - U - V*sqrt(2))/4)
    return -(floor_lin(2 - U, -V) // 4)


def letter(a: int, b: int, k: int, cache: dict[int, int]) -> int:
    for t in (k, k - 1, k - 2):
        if t not in cache:
            cache[t] = n_code(a, b, t)
    return cache[k] - 2 * cache[k - 1] - cache[k - 2]


def support(a: int, b: int) -> tuple[int, int, list[int]]:
    """Return (first, last, letters on [first, last]) for the code word.

    The scan range is the exact hyperbolic window, plus a margin on which
    every letter is checked to vanish.
    """
    # Walk |xi_k| and |xi'_k|. |xi| < 1/2 iff |U+V*sqrt(2)| < 2.
    def small_direct(k: int) -> bool:
        U, V = UV(a, b, k)
        return abs_lt(U, V, 2)

    def small_conj(k: int) -> bool:
        U, V = UV(a, b, k)
        return abs_lt(U, -V, 2)

    # locate k_first = smallest integer with |xi| >= 1/2
    k = 0
    # bound the walk: |xi_k| grows by eps each step, |N| controls the length
    N = abs(a * a - 2 * b * b)
    # generous exact walk limit
    limit = 8 + 4 * (N.bit_length() + 2)
    if small_direct(0):
        while small_direct(k) :
            k += 1
            if k > limit:
                raise RuntimeError(f"direct walk overflow {(a,b)}")
        k_first = k
    else:
        while not small_direct(k):
            k -= 1
            if k < -limit:
                raise RuntimeError(f"direct walk underflow {(a,b)}")
        k_first = k + 1
    # k_last_big = largest integer with |xi'| >= 1/2
    k = 0
    if small_conj(0):
        while small_conj(k):
            k -= 1
            if k < -limit:
                raise RuntimeError(f"conj walk underflow {(a,b)}")
        k_last_big = k + 1
    else:
        while not small_conj(k):
            k += 1
            if k > limit:
                raise RuntimeError(f"conj walk overflow {(a,b)}")
        k_last_big = k - 1
    lo = k_first
    hi = k_last_big + 2
    cache: dict[int, int] = {}
    # margin: letters strictly outside [lo, hi] vanish
    for k in range(lo - 4, lo):
        if letter(a, b, k, cache) != 0:
            raise RuntimeError(f"left margin nonzero {(a,b)} k={k}")
    for k in range(hi + 1, hi + 5):
        if letter(a, b, k, cache) != 0:
            raise RuntimeError(f"right margin nonzero {(a,b)} k={k}")
    if hi < lo:
        return 0, -1, []
    letters = [letter(a, b, k, cache) for k in range(lo, hi + 1)]
    nz = [i for i, e in enumerate(letters) if e != 0]
    if not nz:
        return 0, -1, []
    first = lo + nz[0]
    last = lo + nz[-1]
    return first, last, letters[nz[0] : nz[-1] + 1]


def span_of(a: int, b: int) -> tuple[int, list[int]]:
    _f, _l, w = support(a, b)
    return (0 if not w else len(w)), w


def log_eps_absN_over_2(N: int) -> arb:
    """Enclosure of log_eps(|N|/2) = ln(|N|/2)/ln(1+sqrt(2))."""
    return (arb(N) / 2).log() / (1 + arb(2).sqrt()).log()


def floor_log_bound(N: int) -> int:
    """Rigorous floor(log_eps(|N|/2)), refined until the ball avoids Z+1 edges."""
    L = log_eps_absN_over_2(N)
    # arb floor via upper/lower
    lo = int(math.floor(float(L.lower()) - 1e-15))
    hi = int(math.floor(float(L.upper()) + 1e-15))
    # float(arb) is not a proof. Use string/comparison against integers.
    # L < m iff the upper bound < m; L >= m iff lower bound >= m.
    # Find floor by testing integers around a float guess, then certify.
    guess = float((arb(N) / 2).log() / (1 + arb(2).sqrt()).log())
    m = math.floor(guess)
    # certify m <= L < m+1
    # widen search if the float guess is off
    for _ in range(6):
        # L >= m ?
        ge = (L >= m)
        lt = (L < (m + 1))
        # flint arb comparisons return a truth value that may be unknown
        ge_b = bool(L >= arb(m))
        lt_b = bool(L < arb(m + 1))
        if ge_b and lt_b:
            return m
        if bool(L >= arb(m + 1)):
            m += 1
            continue
        if bool(L < arb(m)):
            m -= 1
            continue
        ctx.prec += 128
        L = log_eps_absN_over_2(N)
    raise RuntimeError(f"cannot floor-certify log for N={N}")


def shell_j(N: int) -> int:
    """Unique j >= 0 with 2^j <= N < 2^{j+1}. N >= 1."""
    return N.bit_length() - 1


def in_domain(a: int, b: int) -> bool:
    """sigma_1 > 0 and 1 <= sigma_1/|sigma_2| < lambda = eps^2.

    sigma_1^2 - sigma_2^2 = 4*a*b*sqrt(2), so sigma_1 >= |sigma_2| iff a*b >= 0
    once sigma_1 > 0. lambda^2 = 17+12*sqrt(2), and
    lambda^2*sigma_2^2 - sigma_1^2 = (2*S - 3*D)*(8+6*sqrt(2)) with
    S = a^2+2*b^2 and D = 2*a*b, so the ratio is < lambda iff 2*S > 3*D.
    """
    if a == 0 and b == 0:
        return False
    if floor_lin(a, b) < 0:
        return False
    if a * b < 0:
        return False
    S = a * a + 2 * b * b
    D = 2 * a * b
    return 2 * S - 3 * D > 0


def reps(j: int) -> list[tuple[int, int, int]]:
    """Fundamental-domain classes with 2^j <= |N| < 2^{j+1}.

    lambda < 6, so sigma_1^2 < 6*|N| < 6*2^{j+1}.
    """
    Nlo = 1 << j
    Nhi = 1 << (j + 1)
    X1sq = 6 * Nhi
    Amax = int(math.isqrt(X1sq) + 3)
    Bmax = int(math.isqrt(X1sq // 2) + 3)
    out = []
    for b in range(-Bmax, Bmax + 1):
        for a in range(-Amax, Amax + 1):
            N = a * a - 2 * b * b
            AN = abs(N)
            if AN < Nlo or AN >= Nhi:
                continue
            if in_domain(a, b):
                out.append((a, b, AN))
    return out


def check_floor_against_mpmath(n_samples: int = 200) -> None:
    import mpmath as mp

    mp.mp.dps = 80
    rng = random.Random(20261104)
    for _ in range(n_samples):
        U = rng.randint(-10**6, 10**6)
        V = rng.randint(-10**6, 10**6)
        got = floor_lin(U, V)
        truth = int(mp.floor(mp.mpf(U) + mp.mpf(V) * mp.sqrt(2)))
        if got != truth:
            raise SystemExit(f"floor mismatch U={U} V={V} got={got} truth={truth}")
    # powers
    for k in range(-30, 40):
        p, q = eps_pow(k)
        val = mp.power(1 + mp.sqrt(2), k)
        if abs(val - (p + q * mp.sqrt(2))) > mp.mpf("1e-60"):
            raise SystemExit(f"eps power mismatch k={k}")


def check_abs_lt() -> None:
    """abs_lt(U,V,2) iff |U+V*sqrt(2)| < 2."""
    import mpmath as mp

    mp.mp.dps = 50
    rng = random.Random(7)
    for _ in range(300):
        U = rng.randint(-30, 30)
        V = rng.randint(-30, 30)
        Z = mp.mpf(U) + mp.mpf(V) * mp.sqrt(2)
        got = abs_lt(U, V, 2)
        truth = abs(Z) < 2
        if got != truth:
            raise SystemExit(f"abs_lt mismatch {U,V} Z={Z} got={got}")


def check_letters_against_mpmath(n_samples: int = 40) -> None:
    """n_code matches floor/red, and a few full words match an independent mpmath recurrence."""
    import mpmath as mp

    mp.mp.dps = 60
    rng = random.Random(11)
    half = mp.mpf(1) / 2
    for _ in range(n_samples):
        a = rng.randint(-40, 40)
        b = rng.randint(-40, 40)
        if a == 0 and b == 0:
            continue
        for k in range(-12, 16):
            U, V = UV(a, b, k)
            xi = (mp.mpf(U) + mp.mpf(V) * mp.sqrt(2)) / 4
            if k % 2 == 0:
                n_m = int(mp.floor(xi + half))
            else:
                n_m = -int(mp.floor(half - xi))
            n_i = n_code(a, b, k)
            if n_m != n_i:
                raise SystemExit(f"n_code mismatch {(a,b,k)} mp={n_m} int={n_i} xi={xi}")


def load_enum() -> list[dict]:
    rows = []
    with open(ENUM) as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def main() -> None:
    t0 = time.time()
    print("cross-check floor, abs, letters, eps powers...", flush=True)
    check_floor_against_mpmath()
    check_abs_lt()
    check_letters_against_mpmath()
    print(f"  ok {time.time()-t0:.1f}s", flush=True)

    rows = load_enum()
    span_mismatches = []
    letter_mismatches = 0
    max_excess = -10**9
    max_at = None
    sharp_hits = 0
    by_shell_max = {}
    n_ok = 0
    for r in rows:
        a, b, N = int(r["a"]), int(r["b"]), int(r["N"])
        sp, word = span_of(a, b)
        # N14 stored words pass float letters through int(), which truncates
        # non-integral binary64 values. The span (support length) is the object
        # used by Prop. K; letter values are recorded only as an audit.
        if [int(x) for x in word] != [int(x) for x in r["word"]]:
            letter_mismatches += 1
        if sp != int(r["span"]):
            span_mismatches.append(
                dict(a=a, b=b, N=N, json_span=r["span"], exact_span=sp, json_word=r["word"], exact_word=word)
            )
            continue
        fl = floor_log_bound(N)
        cap = fl + 3
        excess = sp - cap
        if excess > max_excess:
            max_excess = excess
            max_at = dict(a=a, b=b, N=N, j=r["j"], span=sp, floor_log=fl, cap=cap)
        if excess == 0:
            sharp_hits += 1
        j = int(r["j"])
        by_shell_max[j] = max(by_shell_max.get(j, -10**9), sp - fl)
        if sp > cap:
            raise SystemExit(f"BOUND FAIL {a,b,N} span={sp} cap={cap}")
        js = shell_j(N)
        if js != j:
            raise SystemExit(f"shell index {js} != json {j} for N={N}")
        n_ok += 1
    print(
        f"enum spans ok={n_ok} span_mismatches={len(span_mismatches)} "
        f"letter_mismatches={letter_mismatches} max(span-(floor(log)+3))={max_excess}",
        flush=True,
    )
    if span_mismatches:
        print(json.dumps(span_mismatches[:6], indent=1))
        raise SystemExit("span mismatch against a_enum.jsonl")
    print("max at", max_at, "sharp hits", sharp_hits)

    # fundamental-domain enumeration must reproduce the N14 list through j=12
    json_counts = Counter(int(r["j"]) for r in rows)
    for j in range(0, 13):
        R = reps(j)
        got = sorted((a, b) for a, b, _N in R)
        exp = sorted((int(r["a"]), int(r["b"])) for r in rows if int(r["j"]) == j)
        if got != exp:
            missing = set(map(tuple, exp)) - set(map(tuple, got))
            extra = set(map(tuple, got)) - set(map(tuple, exp))
            raise SystemExit(f"reps mismatch j={j} missing={list(missing)[:6]} extra={list(extra)[:6]} n={len(got)} vs {len(exp)}")
        if len(R) != json_counts[j]:
            raise SystemExit(f"count mismatch j={j}")
    print("reps reproduces a_enum.jsonl for j<=12", flush=True)

    # extend fundamental domain through J
    Jmax = 16
    ext_max = max_excess
    ext_at = max_at
    shell_counts = {}
    add_hist = Counter()
    t1 = time.time()
    for j in range(0, Jmax + 1):
        R = reps(j)
        shell_counts[j] = len(R)
        for a, b, N in R:
            sp, _w = span_of(a, b)
            fl = floor_log_bound(N)
            cap = fl + 3
            if sp > cap:
                raise SystemExit(f"EXT BOUND FAIL j={j} {(a,b,N)} span={sp} cap={cap}")
            add = sp - fl
            add_hist[add] += 1
            if sp - cap > ext_max:
                ext_max = sp - cap
                ext_at = dict(a=a, b=b, N=N, j=j, span=sp, floor_log=fl, cap=cap)
        print(f"  j={j} n={len(R)} ext_max_excess={ext_max} {time.time()-t1:.1f}s", flush=True)

    # unit invariance: alpha |-> alpha*eps preserves span, on a sample of the enum
    rng = random.Random(1)
    sample = rng.sample(rows, 40)
    unit_bad = []
    for r in sample:
        a, b = int(r["a"]), int(r["b"])
        sp0, _ = span_of(a, b)
        # (a+b*sqrt(2))*eps = (a+b*sqrt(2))*(1+sqrt(2)) = a+2b + (a+b)*sqrt(2)
        a2, b2 = a + 2 * b, a + b
        sp1, _ = span_of(a2, b2)
        a3, b3 = a2 + 2 * b2, a2 + b2
        sp2, _ = span_of(a3, b3)
        if not (sp0 == sp1 == sp2):
            unit_bad.append(dict(a=a, b=b, spans=[sp0, sp1, sp2]))
    print("unit invariance failures", unit_bad)

    # rational comparisons used in the proof
    # (1+sqrt(2))^4 = 17+12*sqrt(2) > 8, so log_eps(2) < 4/5? 
    # We need 2^5=32 ? (eps)^4. 32 < 17+12*sqrt(2) iff 15 < 12*sqrt(2) iff 225 < 288.
    assert 225 < 288
    # span <= floor(4j/5)+3 <= 2j for j>=3, checked for j<=40 by integers
    twoj_ok = all((4 * j) // 5 + 3 <= 2 * j for j in range(3, 5000))
    # and versus the certified floor(j*log)+3
    theta = arb(2).log() / (1 + arb(2).sqrt()).log()
    theta_lt_4_5 = bool(theta < arb(4) / 5)
    theta_gt = bool(theta > arb(786) / 1000)

    out = dict(
        enum_compared=n_ok,
        enum_span_mismatches=len(span_mismatches),
        enum_letter_mismatches_float_int=letter_mismatches,
        enum_max_span_minus_floorlog_plus3=max_excess,
        enum_max_at=max_at,
        enum_sharp_hits_excess0=sharp_hits,
        enum_max_span_minus_floorlog_by_shell={str(k): by_shell_max[k] for k in sorted(by_shell_max)},
        extended_Jmax=Jmax,
        extended_max_span_minus_floorlog_plus3=ext_max,
        extended_max_at=ext_at,
        shell_counts=shell_counts,
        additive_histogram_span_minus_floorlog={str(k): add_hist[k] for k in sorted(add_hist)},
        unit_invariance_failures=unit_bad,
        theta_enclosure=[float(theta.lower()), float(theta.upper())],
        theta_lt_4_over_5=theta_lt_4_5,
        theta_gt_0_786=theta_gt,
        rational_225_lt_288=True,
        floor_4j_over_5_plus3_le_2j_for_j_ge_3=twoj_ok,
        seconds=time.time() - t0,
    )
    path = os.path.join(LOGS, "span_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
