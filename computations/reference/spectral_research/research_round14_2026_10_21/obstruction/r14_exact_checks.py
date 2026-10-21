"""Exact bookkeeping checks for the Round 14 spectral-orbit barrier.

This script does not simulate the original tiny kick and does not test H_diag.
The asymptotic assertions are proved in the companion Markdown file.
"""

from fractions import Fraction
from pathlib import Path
import hashlib
import json


def mm(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def mp(a, exponent):
    result = ((1, 0), (0, 1))
    while exponent:
        if exponent & 1:
            result = mm(result, a)
        a = mm(a, a)
        exponent //= 2
    return result


def valuation(n, p):
    count = 0
    while n and n % p == 0:
        n //= p
        count += 1
    return count


S = ((3, 4), (2, 3))
assert mp(S, 3) == ((99, 140), (70, 99))
pell_samples = []
for r in range(1, 60):
    power = mp(S, r)
    assert power[0][1] % 4 == 0
    n = power[0][1] // 4
    t = power[0][0]
    assert power == ((t, 4 * n), (2 * n, t))
    assert t * t - 8 * n * n == 1
    assert n % 2 == r % 2
    twice = mp(S, 2 * r)
    if n > 1:
        assert twice[0][0] % n == 1
        assert twice[1][1] % n == 1
        assert twice[0][1] % n == 0
        assert twice[1][0] % n == 0
    if r in (3, 5, 7, 9):
        pell_samples.append({"r": r, "N_r": n, "v7_N_r": valuation(n, 7)})

seven_tower = []
for s in range(5):
    r = 3 * 7**s
    power = mp(S, r)
    n = power[0][1] // 4
    assert valuation(n, 7) == s + 1
    seven_tower.append(
        {"s": s, "r": r, "v7_N_r": valuation(n, 7), "N_bit_length": n.bit_length()}
    )

for H in range(2, 200):
    z = 1 + 2 * sum((Fraction(H - j, H) ** 2 for j in range(1, H)), Fraction())
    assert z == Fraction(2 * H**2 + 1, 3 * H)
    assert z >= Fraction(2 * H, 3)
    # The proof uses this deliberately relaxed first-moment bound.
    assert Fraction(3, 2 * H) + Fraction(3, 32 * H) < Fraction(2, H)

root = Path(__file__).resolve().parent
report = root / "r14_original_spectral_orbit_barrier.md"
result = {
    "status": "exact bookkeeping passed; no original H_diag claim",
    "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
    "pell_samples": pell_samples,
    "seven_tower": seven_tower,
    "fejer_normalization_checked_for_H": [2, 199],
    "proof_lower_liminf_logN_times_d": "pi*log(3+2*sqrt(2))/4",
    "physical_parameter_changed": False,
    "tiny_kick_eigendecompositions_used": False,
}
(root / "r14_exact_checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
