#!/usr/bin/env python3
"""Exact ε-digit span of classes α ∈ ℤ[√2] / ±ε^ℤ.

Digits are the integer failures of the recurrence τ_k = 2 τ_{k-1} + τ_{k-2}
on τ_k = red(σ_+(μ) ε^k), μ = (√2/4) α. All comparisons are integer (isqrt).

Cross-check: computations/verification/lineN14/code/digits.py (mpmath, dps=80).

Writes logs/span_audit.json.
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "logs" / "span_audit.json"
sys.path.insert(0, str(Path("/workspace/computations/verification/lineN14/code")))

# ε = 1+√2, ε^n = p_n + q_n √2
def eps_pow(n: int) -> tuple[int, int]:
    if n < 0:
        # ε ε̄ = -1 and ε̄ = 1-√2, so ε^{-1} = -ε̄ = -1+√2.
        # ε^{-m} = (-ε̄)^m = (-1)^m (p_m - q_m √2), where ε^m = p_m + q_m √2.
        p, q = eps_pow(-n)
        sign = 1 if ((-n) % 2 == 0) else -1
        return sign * p, -sign * q
    p, q = 1, 0  # ε^0
    for _ in range(n):
        p, q = p + 2 * q, p + q
    return p, q


def isqrt(n: int) -> int:
    return int(math.isqrt(n))


def floor_lin(p: int, q: int) -> int:
    """floor(p + q √2)."""
    if q >= 0:
        s = isqrt(2 * q * q)
        # s = floor(q √2): s^2 ≤ 2q^2 < (s+1)^2, and equality s = q√2 iff q=0
        return p + s
    qp = -q
    s = isqrt(2 * qp * qp)
    # q√2 = -qp√2 ∈ (-s-1, -s], so p+q√2 ∈ [p-s-1, p-s) if qp√2 ≠ s
    # qp√2 > s for qp>0, hence p+q√2 < p-s and > p-s-1, floor = p-s-1
    return p - s - 1


def cmp_abs_theta(A: int, B: int, half_num: int = 2) -> int:
    """Sign of |σ_+(μ ε^k)| - 1/2, where α ε^k = A + B √2 and σ_+(μ ε^k) = (2B + A √2)/4.

    Returns -1, 0, +1 for |θ| < 1/2, =, >.
    |2B + A √2| ? 2.
    """
    # δ = 2B + A √2; compare |δ| with 2
    # |δ|^2 ? 4, but δ^2 = (2B)^2 + 2 A^2 + 4 A B √2 = (4B^2+2A^2) + (4AB) √2
    # Compare δ^2 with 4 = 4 + 0√2.
    u = 4 * B * B + 2 * A * A - 4
    v = 4 * A * B
    # sign of u + v √2, then if δ^2 - 4 has that sign. δ^2-4 = u + v√2.
    return sign_lin(u, v)


def sign_lin(u: int, v: int) -> int:
    """Sign of u + v √2: -1, 0, +1."""
    if u == 0 and v == 0:
        return 0
    if v == 0:
        return 1 if u > 0 else -1
    if u >= 0 and v > 0:
        return 1
    if u <= 0 and v < 0:
        return -1
    # opposite signs: compare u^2 ? 2 v^2
    lhs = u * u
    rhs = 2 * v * v
    if lhs > rhs:
        return 1 if u > 0 else -1
    if lhs < rhs:
        return 1 if v > 0 else -1
    # |u| = |v|√2, impossible for v≠0 unless both 0, so lhs==rhs cannot happen
    # unless u=v=0 already handled. If it happens, the number is 0 only if both 0.
    return 0


def alpha_eps(a: int, b: int, k: int) -> tuple[int, int]:
    """(α ε^k) = A + B √2, α = a + b √2."""
    p, q = eps_pow(k)
    # (a+b√2)(p+q√2) = ap+2bq + (aq+bp)√2
    return a * p + 2 * b * q, a * q + b * p


def theta_integer_part(A: int, B: int) -> int:
    """n = floor(θ + 1/2) with θ = (2B + A √2)/4.

    floor( (2B+2 + A √2)/4 ) = floor(2B+2 + A √2) // 4.
    """
    return floor_lin(2 * B + 2, A) // 4


def trace_T(A: int, B: int) -> int:
    """θ + θ̄ = B, since μ ε^k = B/2 + (A/4)√2 and the rational trace is B.
    α ε^k = A+B√2, (√2/4)(A+B√2) = B/2 + (A/4)√2, sum of embeddings = B.
    """
    return B


def digits_of(a: int, b: int, k_lo: int, k_hi: int) -> dict[int, int]:
    ns = {}
    for k in range(k_lo, k_hi + 1):
        A, B = alpha_eps(a, b, k)
        ns[k] = theta_integer_part(A, B)
    E = {}
    for k in range(k_lo + 2, k_hi + 1):
        E[k] = ns[k] - 2 * ns[k - 1] - ns[k - 2]
    return E


def support_bounds(a: int, b: int) -> tuple[int, int, int]:
    """Return (K_left, K_right, Nabs).

    K_left = min {k : |θ_k| ≥ 1/2}, K_right = max {k : |θ̄_k| ≥ 1/2}.
    θ̄_k = T_k - θ_k, |θ̄| ≥ 1/2 iff |θ_k - T_k| ≥ 1/2.
    Since |θ θ̄| = |N|/8, |θ̄_k| = |N|/(8|θ_k|).
    """
    N = a * a - 2 * b * b
    Nabs = abs(N)
    # search window from the size of the embeddings
    # |σ_+| = |a+b√2|, log scale ~ log(|σ|)/log ε
    # safe window: |k| ≤ log2(|N|+2)*2 + 20
    span_guess = int(math.log2(Nabs + 1) * 3 + 30)
    K_left = None
    K_right = None
    # |θ̄_k| ≥ 1/2 iff |θ_k| ≤ |N|/4, because |θ θ̄|=|N|/8 so |θ̄|≥1/2 ⇔ |θ|≤|N|/4.
    # And |θ_k| ≥ 1/2.
    # θ_k grows by ε each step, so scan a window.
    for k in range(-span_guess, span_guess + 1):
        A, B = alpha_eps(a, b, k)
        c = cmp_abs_theta(A, B)
        if c >= 0 and K_left is None:
            K_left = k
        # |θ̄|≥1/2: θ̄ = T - θ = B - θ, |B - θ|≥1/2.
        # θ = (2B + A√2)/4, B - θ = B - B/2 - (A/4)√2 = B/2 - (A/4)√2 = (2B - A√2)/4
        # |2B - A√2| ? 2. Sign of |(2B) + (-A)√2| - 2, same cmp with A' = -A? 
        # cmp_abs_theta uses |2B + A√2|?2. For conjugate we need |2B - A√2| = |-2B + A√2|.
        # Pass A_conj = -A, B_conj = B? |2B + (-A)√2| = |2B - A√2|. Yes.
        cbar = cmp_abs_theta(-A, B)
        if cbar >= 0:
            K_right = k
    if K_left is None or K_right is None:
        raise RuntimeError(f"no threshold for {(a,b)} N={N}")
    return K_left, K_right, Nabs


def span_from_E(E: dict[int, int]) -> tuple[int, int, int, list[int]]:
    nz = sorted(k for k, v in E.items() if v != 0)
    if not nz:
        return 0, 0, 0, []
    return nz[-1] - nz[0] + 1, nz[0], nz[-1], [E[k] for k in range(nz[0], nz[-1] + 1)]


def in_fundamental(a: int, b: int) -> bool:
    """1 ≤ σ_+/|σ_-| < λ, σ_+>0, N≠0. Exact."""
    N = a * a - 2 * b * b
    if N == 0:
        return False
    Nabs = abs(N)
    # σ_+ = a+b√2 > 0
    if sign_lin(a, b) <= 0:
        return False
    # σ_+^2 ? |N| and ? λ|N|
    # σ_+^2 = a^2+2b^2 + 2ab √2
    # |N| ≤ σ_+^2  ⇔  0 ≤ (a^2+2b^2 - Nabs) + 2ab √2
    # σ_+^2 < λ |N| = |N|(3+2√2) = 3 Nabs + 2 Nabs √2
    # σ_+^2 - λ|N| = (a^2+2b^2 - 3 Nabs) + (2ab - 2 Nabs) √2 < 0
    if sign_lin(a * a + 2 * b * b - Nabs, 2 * a * b) < 0:
        return False
    if sign_lin(a * a + 2 * b * b - 3 * Nabs, 2 * a * b - 2 * Nabs) >= 0:
        return False
    return True


def enumerate_classes(J: int) -> list[tuple[int, int, int]]:
    """All fundamental-domain (a,b) with 1 ≤ |N| < 2^{J+1}. Shell j = floor(log2|N|)."""
    X = 1 << (J + 1)
    # σ_+ < sqrt(λ |N|) < sqrt(λ X), |b| ≤ (σ_++|σ_-|)/(2√2) < (sqrt(λ X)+sqrt(X))/√2
    # safe: |a|,|b| ≤ floor(sqrt(2*λ*X))+3
    # λ<6, so sqrt(12 X)
    B = isqrt(12 * X) + 5
    out = []
    for b in range(-B, B + 1):
        # a near ± b√2, |a^2 - 2b^2| < X
        # a^2 < 2b^2 + X
        amax = isqrt(2 * b * b + X) + 2
        # also fundamental domain forces σ_+ = O(sqrt(X))
        for a in range(-amax, amax + 1):
            Nabs = abs(a * a - 2 * b * b)
            if Nabs == 0 or Nabs >= X:
                continue
            if in_fundamental(a, b):
                out.append((a, b, Nabs))
    return out


def mp_word(a: int, b: int):
    import mpmath as mp
    import digits as Dg
    mp.mp.dps = 80
    # e = 2α
    w, g, k0 = Dg.eps_digits(2 * a, 2 * b, KK=8, tol=1e-8)
    return w, g, k0


def main():
    t0 = time.time()
    # --- identity checks on model classes (N14 §1.2 words) ---
    models = {
        (1, 0): "odd",
        (0, 1): "sq2",
        (2, 0): "two",
        (0, 2): "2sq2",
        (4, 0): "four",
    }
    model_report = {}
    for (a, b), name in models.items():
        # reduce to fundamental domain by multiplying by ε^{±1} until in domain
        aa, bb = a, b
        for _ in range(12):
            if in_fundamental(aa, bb):
                break
            # multiply by ε: (a+b√2)(1+√2) = a+2b + (a+b)√2
            aa, bb = aa + 2 * bb, aa + bb
        Kl, Kr, Nabs = support_bounds(aa, bb)
        E = digits_of(aa, bb, Kl - 3, Kr + 5)
        span, first, last, word = span_from_E(E)
        mw, mg, mk0 = mp_word(aa, bb)
        model_report[name] = {
            "rep": [aa, bb],
            "N": Nabs,
            "K_left": Kl,
            "K_right": Kr,
            "span": span,
            "word": word,
            "mp_word": [int(round(x)) for x in mw],
            "mp_span": len(mw),
            "mp_zr": mg,
            "match": word == [int(round(x)) for x in mw],
        }

    # --- exhaustive audit ---
    J = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    classes = enumerate_classes(J)
    # cross-check mpmath on |N|<2^10 (j≤9)
    mism = []
    defects = []  # span - log(|N|/2)/log(eps)
    logeps = math.log(1 + math.sqrt(2))
    max_defect = -1e9
    min_defect = 1e9
    worst = None
    best = None
    violations_plus3 = []
    endpoint_fail = []  # E at K_left or theoretical last is zero
    by_shell = {}
    n_match = 0
    n_mp = 0
    for (a, b, Nabs) in classes:
        j = Nabs.bit_length() - 1  # floor(log2 Nabs)
        Kl, Kr, _ = support_bounds(a, b)
        E = digits_of(a, b, Kl - 4, Kr + 6)
        # outside predicted support, digits must vanish
        outside = [k for k, v in E.items() if v != 0 and (k < Kl or k > Kr + 2)]
        span, first, last, word = span_from_E(E)
        # predicted upper: span ≤ (Kr - Kl) + 3, and Kr-Kl ≤ log(|N|/2)/log ε
        # use high-precision comparison via arb later; here float with a slack flag
        if Nabs == 1:
            log_term = math.log(0.5) / logeps
        else:
            log_term = math.log(Nabs / 2) / logeps
        defect = span - log_term
        if defect > max_defect:
            max_defect = defect
            worst = {"a": a, "b": b, "N": Nabs, "j": j, "span": span, "defect": defect, "word": word[:40], "Kl": Kl, "Kr": Kr, "first": first, "last": last}
        if defect < min_defect:
            min_defect = defect
            best = {"a": a, "b": b, "N": Nabs, "j": j, "span": span, "defect": defect, "Kl": Kl, "Kr": Kr}
        slack = (Kr - Kl + 3) - span
        if outside:
            violations_plus3.append({"a": a, "b": b, "N": Nabs, "outside": outside[:8], "Kl": Kl, "Kr": Kr, "slack": slack})
        if slack != (1 if Nabs == 2 else 0):
            endpoint_fail.append({"a": a, "b": b, "N": Nabs, "slack": slack, "span": span, "Kl": Kl, "Kr": Kr, "first": first, "last": last})
        # endpoint nonvanishing
        if E.get(Kl, 0) == 0 or (Kr + 2 >= Kl and E.get(Kr + 2, 0) == 0 and E.get(Kr + 1, 0) == 0 and E.get(Kr, 0) == 0):
            endpoint_fail.append({"a": a, "b": b, "N": Nabs, "Kl": Kl, "Kr": Kr, "E_Kl": E.get(Kl), "E_Kr": E.get(Kr), "E_Kr1": E.get(Kr + 1), "E_Kr2": E.get(Kr + 2)})
        rec = by_shell.setdefault(j, {"n": 0, "max_defect": -1e9, "min_defect": 1e9, "max_span": 0})
        rec["n"] += 1
        rec["max_defect"] = max(rec["max_defect"], defect)
        rec["min_defect"] = min(rec["min_defect"], defect)
        rec["max_span"] = max(rec["max_span"], span)
        if j <= 11:
            n_mp += 1
            mw, mg, mk0 = mp_word(a, b)
            mw_i = [int(round(x)) for x in mw]
            if mw_i != word:
                # words may differ by a global shift of the index origin; compare the sequence
                mism.append({"a": a, "b": b, "N": Nabs, "exact": word, "mp": mw_i})
            else:
                n_match += 1
        if len(violations_plus3) > 20:
            break

    # prove Kr-Kl ≤ log bound by exact arb comparison on the worst few and a global exact check
    # Exact: ε^{Kr-Kl} ≤ |N|/2   ? from the proof it's ≤, i.e. we check
    # (|N|/8) * ε^{Kl-Kr} ≥ 1/4, i.e. |N| ε^{Kl-Kr} ≥ 2.
    # We certify max over classes of (span) vs the real bound using flint balls.
    from flint import arb, ctx

    ctx.prec = 200
    eps = 1 + arb(2).sqrt()
    log_eps = eps.log()

    def ball_defect(span: int, Nabs: int):
        # span - log(|N|/2)/log ε
        return arb(span) - (arb(Nabs) / 2).log() / log_eps

    # recompute max/min defect as arb upper/lower to certify the float champion
    # (float is only used to pick candidates; the certificate is the arb max over ALL classes)
    # Doing arb for every class at J=16 (~0.6*2^16 ~ 40k) is fine.
    max_upper = None
    min_lower = None
    n_span_gt = 0
    # span ≤ log(|N|/2)/log ε + 3  iff  span - log < 3 or ≤ 3?
    # We certify the strict inequality defect < 4 and defect > -1, whatever the data says,
    # by tracking arb enclosures of every defect.
    cert_max = arb("-1e9")
    cert_min = arb("1e9")
    n_fail_support = len(violations_plus3)
    # second pass for arb cert — classes already enumerated
    for (a, b, Nabs) in classes:
        Kl, Kr, _ = support_bounds(a, b)
        E = digits_of(a, b, Kl - 4, Kr + 6)
        span, first, last, word = span_from_E(E)
        dball = ball_defect(span, Nabs)
        if dball > cert_max:
            cert_max = dball
        if dball < cert_min:
            cert_min = dball

    out = {
        "J": J,
        "n_classes": len(classes),
        "seconds": round(time.time() - t0, 3),
        "models": model_report,
        "mp_compared": n_mp,
        "mp_match": n_match,
        "mp_mismatch_n": len(mism),
        "mp_mismatch_sample": mism[:8],
        "support_violations": violations_plus3[:8],
        "n_support_violations": n_fail_support,
        "n_endpoint_fail": len(endpoint_fail),
        "endpoint_fail_sample": endpoint_fail[:8],
        "float_max_defect": max_defect,
        "float_min_defect": min_defect,
        "worst": worst,
        "best": best,
        "cert_defect_upper": str(cert_max.upper()),
        "cert_defect_lower": str(cert_min.lower()),
        "by_shell": {str(k): by_shell[k] for k in sorted(by_shell)},
    }
    LOG.write_text(json.dumps(out, indent=1))
    print(json.dumps({k: out[k] for k in (
        "J", "n_classes", "seconds", "mp_compared", "mp_match", "mp_mismatch_n",
        "n_support_violations", "n_endpoint_fail", "float_max_defect", "float_min_defect",
        "cert_defect_upper", "cert_defect_lower")}, indent=1))
    print("worst", worst)
    print("best", best)
    print("models", json.dumps(model_report, indent=1)[:2000])


if __name__ == "__main__":
    main()
