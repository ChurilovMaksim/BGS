"""Exact rational endpoints for the audited finite Pell covering corollary.

This is not a replay of the archived fixed-kick certificates and says nothing
about an infinite sequence of dimensions at fixed nonzero coupling.
"""

from fractions import Fraction

TAU_ORIGINAL = Fraction(1, 10**80)
TAU_ENDPOINT = Fraction(206, 125) * TAU_ORIGINAL


def pell_real_part(index: int) -> int:
    """Integer real coefficient of (1 + sqrt(2))**index."""
    h, v = 1, 0
    for _ in range(index):
        h, v = h + 2 * v, h + v
    if h * h - 2 * v * v != (-1) ** index or h % 2 != 1:
        raise ValueError(f"unexpected Pell arithmetic at index {index}")
    return h


def check() -> None:
    # Machin's formula and alternating arctangent bounds.
    pi_low = Fraction(157, 50)
    pi_high = Fraction(22, 7)
    a_lo = Fraction(1, 5) - Fraction(1, 3 * 5**3)
    a_hi = a_lo + Fraction(1, 5**6)
    b_hi = Fraction(1, 239)
    b_lo = b_hi - Fraction(1, 3 * 239**3)
    if not pi_low < 16 * a_lo - 4 * b_hi < 16 * a_hi - 4 * b_lo < pi_high:
        raise ValueError("Machin rational pi enclosure failed")
    rayleigh_lower = 1 - pi_high**2 / 36 + pi_low**4 / 1800 - pi_high**6 / 141120
    if not rayleigh_lower > Fraction(3, 4):
        raise ValueError("Sine2 Rayleigh lower bound failed")
    print("Sine2: Rayleigh lower bound > 3/4; hit probability > 4/5")

    for tau, k, cover, expected_lower, threshold in (
        (TAU_ENDPOINT, 197, Fraction(1, 700), Fraction(68303, 3200), Fraction(21)),
        (TAU_ENDPOINT, 203, Fraction(7, 25), Fraction(1289, 89600), Fraction(1, 100)),
        (TAU_ORIGINAL, 197, Fraction(1, 1200), Fraction(29327, 800), Fraction(36)),
        (TAU_ORIGINAL, 203, Fraction(17, 100), Fraction(4633, 54400), Fraction(2, 25)),
    ):
        n = pell_real_part(k)
        if n < 15:
            raise ValueError("the diagonal moment bound used here requires N >= 15")
        expanded_cover = k * (Fraction(2000, n) + Fraction(52, 157) * tau * n)
        if not expanded_cover < cover:
            raise ValueError(f"covering budget failed at k={k}, tau={tau}")
        h_min = Fraction(1, 4)
        coefficient = Fraction(99, 100) ** 2 / cover - 1
        if not coefficient * h_min > Fraction(51, 100):
            raise ValueError(f"lower bound not increasing for H >= 1/4 at k={k}")
        lower = (coefficient * h_min**2 - Fraction(51, 100) * h_min) / 2
        if not lower == expected_lower > threshold:
            raise ValueError(f"defect threshold failed at k={k}, tau={tau}")
        print(f"tau/tau_original={tau / TAU_ORIGINAL}, k={k}: "
              f"cover < {cover}; defect >= {lower} > {threshold}")
    print("PASS (exact rational arithmetic; finite Pell dimensions only)")


if __name__ == "__main__":
    check()
