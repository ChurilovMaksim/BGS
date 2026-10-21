#!/usr/bin/env python3
"""Integer regression checks for the r12_full_product analytic note.

These checks do not compute eigenvalues, use a surrogate kick, or test
an asymptotic spectral statistic. All matrix and lattice arithmetic is
over Python integers.
"""
from hashlib import sha256
from pathlib import Path
import json
import math


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INPUTS = (
    "research_round12_2026_10_21/round12_target_checkpoint.md",
    "research_round11_2026_10_21/r11_arithmetic_pell_magnus.md",
    "research_round8_2026_10_21/r8_weyl_quantitative_band_escape.md",
    "research_round8_2026_10_21/r8_weyl_explicit_linear_degree_corollary.md",
    "research_round3_2026_10_21/arithmetic_flat_packet_obstruction_test.md",
    "research_round2_2026_10_20/fermionic_quantitative_pressure.md",
)


def multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def mpow(a, n):
    b = ((1, 0), (0, 1))
    while n:
        if n & 1:
            b = multiply(b, a)
        a = multiply(a, a)
        n >>= 1
    return b


def pell(r):
    x, y = 1, 0
    for _ in range(r):
        x, y = x + 2 * y, x + y
    return x, y


def short_aliases(x, y, c):
    """Enumerate all aliases of l1 norm <= x, without quadratic search."""
    n = x * y
    result = []
    for w in range(-x, x + 1):
        bound = x - abs(w)
        # v=-c*w+k*n must satisfy -bound <= v <= bound.
        k0 = -((-c * w + bound) // n)  # ceil((c*w-bound)/n)
        k1 = (c * w + bound) // n
        for k in range(k0, k1 + 1):
            v = -c * w + k * n
            assert abs(v) <= bound
            if v or w:
                result.append((v, w))
    return sorted(result)


def main():
    rows = []
    for r in range(3, 104, 2):
        x, y = pell(r)
        n = x * y
        c = x * x + 2 * y * y
        assert x * x - 2 * y * y == -1
        assert x % 2 == y % 2 == n % 2 == 1
        assert math.gcd(x, y) == 1
        assert y < x < 2 * y
        assert c % x == 1
        assert c % y == y - 1
        assert (c * c) % n == 1
        assert mpow(((3, 2), (4, 3)), r) == ((c, 2 * n), (4 * n, c))
        b1 = ((x + y) // 2, (x - y) // 2)
        b2 = ((x - y) // 2, (x + y) // 2)
        assert b1[0] * b2[1] - b1[1] * b2[0] == n
        v, w = b1
        assert v + w == x
        assert v + c * w == n * (2 * y - x)
        # Exhaustive in a fixed finite p,q box: check the CRT parametrization
        # and exact l1 identity, including both allowed parity classes.
        for p in range(-8, 9):
            for q in range(-8, 9):
                if (p - q) % 2:
                    continue
                vv, ww = (x * p + y * q) // 2, (x * p - y * q) // 2
                assert (vv + c * ww) % n == 0
                assert abs(vv) + abs(ww) == max(x * abs(p), y * abs(q))
        row = {
            "r": r,
            "N_digits": len(str(n)),
            "pell_crt_word_identities": True,
            "basis_determinant_N": True,
            "parametrization_box": [-8, 8],
        }
        if r <= 9:
            actual = short_aliases(x, y, c)
            expected = sorted((b1, b2, tuple(-t for t in b1),
                               tuple(-t for t in b2)))
            assert actual == expected
            assert all(abs(vv) + abs(ww) == x for vv, ww in actual)
            row["all_nonzero_aliases_l1_at_most_x"] = actual
            row["x"] = x
            row["y"] = y
            row["N"] = n
        rows.append(row)
    data = {
        "status": "all integer assertions passed",
        "scope": {
            "odd_pell_indices": [3, 103],
            "number_of_indices": len(rows),
            "shortest_alias_complete_enumeration_indices": [3, 5, 7, 9],
            "spectral_statistics_computed": False,
            "Bessel_or_large_N_asymptotics_numerically_verified": False,
        },
        "input_sha256": {
            str(p): sha256((ROOT / p).read_bytes()).hexdigest() for p in INPUTS
        },
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": rows,
    }
    dest = HERE / "r12_full_product_exact_checks.json"
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": data["status"], "indices": len(rows),
                      "report": str(dest), "scope": data["scope"]}, indent=2))


if __name__ == "__main__":
    main()
