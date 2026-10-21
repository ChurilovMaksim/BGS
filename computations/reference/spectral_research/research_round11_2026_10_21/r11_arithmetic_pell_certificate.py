"""Exact Fourier/Pell certificate for Round 11.

This script does not compute the spectrum of U_N or assert H_diag.
The all-r collision proof and the noncommutative limits are in the note.
All finite identities below use integer arithmetic and Fraction, except
the explicitly labelled optional decimal value of a limiting moment.
"""

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_name("r11_arithmetic_pell_certificate.json")
ZERO = (F(0), F(0))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def put(poly, v, a):
    poly[v] = add(poly[v], a)


def cv(v):
    k, l = v
    return (3 * k + 2 * l, 4 * k + 3 * l)


def sigma(v, w):
    # This is the symplectic form for W(k,l)=T(l,k).
    return v[1] * w[0] - v[0] * w[1]


def pell(r):
    x, y = 1, 0
    for _ in range(r):
        x, y = x + 2 * y, x + y
    return x, y


# Original symbol f-1/10, with the modular Weyl convention of the task.
# In particular the l=+/-1 coefficients are NOT shifted by (-1)^k.
rcoef = {0: F(1), 1: F(1, 2), -1: F(1, 2),
         6: -F(1, 4), -6: -F(1, 4),
         7: -F(1, 2), -7: -F(1, 2),
         8: -F(1, 4), -8: -F(1, 4)}
c = defaultdict(lambda: ZERO)
put(c, (7, 0), (F(1, 2), F(0)))
put(c, (-7, 0), (F(1, 2), F(0)))
put(c, (0, 0), (-F(1, 10), F(0)))
for k, z in rcoef.items():
    put(c, (k, 0), (z / 10, F(0)))
    put(c, (k + 1, 0), (F(0), -z / 200))
    put(c, (k - 1, 0), (F(0), z / 200))
    put(c, (k, 1), (-3 * z / 1000, -z / 250))
    put(c, (k, -1), (-3 * z / 1000, z / 250))
c = {v: z for v, z in c.items() if z != ZERO}
assert len(c) == 32
assert (0, 0) not in c
assert all(c[(-k, -l)] == conj(z) for (k, l), z in c.items())
assert max(abs(v[0]) for v in c) == 9
assert max(abs(v[1]) for v in c) == 1

L = sum((norm2(z) for (k, l), z in c.items() if l == 0), F(0))
C0 = sum((norm2(z) for z in c.values()), F(0))
C1z = ZERO
integer_hits = []
for v, z in c.items():
    if cv(v) in c:
        integer_hits.append((v, cv(v)))
        C1z = add(C1z, mul(z, conj(c[cv(v)])))
assert set(integer_hits) == {((1, -1), (1, 1)),
                             ((-1, 1), (-1, -1))}
assert C1z[1] == 0
C1 = C1z[0]
variance = C0 + 2 * C1
mixed_lower = 2 * L ** 2 - C0 ** 2
assert L == F(66015, 160000)
assert C0 == F(66033, 160000)
assert C1 == -F(7, 2000000)
assert variance == F(1650797, 4000000)
assert mixed_lower > 0

finite_collisions = []
finite_additive_uniqueness = []
for r in range(3, 42, 2):
    x, y = pell(r)
    n = x * y
    cr = x * x + 2 * y * y
    assert x * x - 2 * y * y == -1
    assert cr % x == 1 % x and cr % y == (-1) % y
    assert cr * cr % n == 1
    hits = []
    for v in sorted(c):
        k, l = v
        for j in range(1, 2 * r):
            k, l = (3 * k + 2 * l) % n, (4 * k + 3 * l) % n
            w = ((k + n // 2) % n - n // 2,
                 (l + n // 2) % n - n // 2)
            if w in c:
                hits.append({"lag": j, "source": list(v),
                             "target": list(w)})
    if r >= 5:
        expected = [
            {"lag": 1, "source": [1, -1], "target": [1, 1]},
            {"lag": 1, "source": [-1, 1], "target": [-1, -1]},
            {"lag": 2 * r - 1, "source": [1, 1], "target": [1, -1]},
            {"lag": 2 * r - 1, "source": [-1, -1], "target": [-1, 1]},
        ]
        key = lambda h: (h["lag"], h["source"], h["target"])
        assert sorted(hits, key=key) == sorted(expected, key=key)
    if r >= 7:
        # The all-r injectivity proof is CRT and bounded coordinates.
        images = {((v[0] + cr * w[0]) % n,
                   (v[1] + cr * w[1]) % n)
                  for v in c for w in c}
        assert len(images) == len(c) ** 2
    finite_collisions.append({"r": r, "x": x, "y": y, "N": n,
                              "lag_set": sorted({h["lag"] for h in hits}),
                              "hit_count": len(hits), "hits": hits})
    if r >= 5:
        orbit_rows = []
        current = {(k % n, l % n): (k, l) for k, l in c}
        for j in range(2 * r):
            orbit_rows.append(current)
            current = {((3 * k + 2 * l) % n, (4 * k + 3 * l) % n): v
                       for (k, l), v in current.items()}
        seed_reports = []
        seed_orbit_images = set()
        for eps in (-1, 1):
            for eta in (-1, 1):
                v0, w0 = (7 * eps, 0), (0, eta)
                target = (v0[0] % n, (cr * w0[1]) % n)
                decompositions = []
                for i in range(2 * r):
                    for j in range(i + 1, 2 * r):
                        for image, v in orbit_rows[i].items():
                            remainder = ((target[0] - image[0]) % n,
                                         (target[1] - image[1]) % n)
                            if remainder in orbit_rows[j]:
                                decompositions.append([i, j, list(v),
                                                       list(orbit_rows[j][remainder])])
                assert decompositions == [[0, r, list(v0), list(w0)]]
                seed_reports.append({"v0": list(v0), "w0": list(w0),
                                     "decompositions": decompositions})
                z = target
                for j in range(2 * r):
                    seed_orbit_images.add(z)
                    z = ((3 * z[0] + 2 * z[1]) % n,
                         (4 * z[0] + 3 * z[1]) % n)
        assert len(seed_orbit_images) == 8 * r
        finite_additive_uniqueness.append({"r": r, "seed_reports": seed_reports,
                                           "distinct_seed_orbit_images": 8 * r})

# The coefficients of the exact fourth mixed moment as a finite cosine sum.
weights = defaultdict(F)
for v, z in c.items():
    for w, t in c.items():
        weights[sigma(v, w)] += norm2(z) * norm2(t)
assert sum(weights.values(), F(0)) == C0 ** 2
assert all(weights[h] == weights[-h] for h in weights)
assert weights[0] >= L ** 2
assert weights[7] + weights[-7] >= F(81, 2000000)

decimal = None
try:
    import mpmath as mp
    mp.mp.dps = 70
    mf = lambda z: mp.mpf(z.numerator) / z.denominator
    fourth = sum(mf(z) * mp.cos(4 * mp.pi * mp.sqrt(2) * h)
                 for h, z in weights.items())
    commutator = 2 * (mf(C0 ** 2) - fourth)
    explicit_comm_lower = mf(F(81, 500000)) * mp.sin(14 * mp.pi * mp.sqrt(2)) ** 2
    decimal = {
        "status": "illustrative high-precision evaluation, not used by the proofs",
        "fourth_mixed_limit": mp.nstr(fourth, 55),
        "normalized_commutator_HS_squared_limit": mp.nstr(commutator, 55),
        "eight_pair_commutator_lower_limit": mp.nstr(explicit_comm_lower, 55),
    }
except ImportError:
    pass

read_inputs = [
    "research_history_frozen/master_before_round11.md",
    "research_round10_2026_10_21/r10_arithmetic_stationary_rational_test.md",
    "research_round10_2026_10_21/r10_mixed_shrinking_isospectral_noise.md",
    "research_round4_2026_10_21/counter_subpolynomial_comb_quantitative.md",
    "research_round4_2026_10_21/counter_no_exact_scalar_powers.md",
    "research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md",
    "research_round2_2026_10_20/root_exact_pressure_variance.md",
    "research_round2_2026_10_20/root_exact_pressure_variance.py",
    "research_round2_2026_10_20/fermionic_quantitative_pressure.md",
    "research_round3_2026_10_21/phase_planck_hole_time_scale_test.md",
]
hashes = {name: sha256((ROOT / name).read_bytes()).hexdigest()
          for name in read_inputs}
assert hashes[read_inputs[0]] == "fe0812b16e1e559d596e8e848dea5d21cea6cf81aec05f39da7d44fc4bb6d45a"
result = {
    "status": "PASS: exact arithmetic and finite checks; not H_diag",
    "symbol": "original f-1/10, W(k,l)=T(l,k), no ordinary-symbol shift",
    "support": [{"mode": list(v), "real": str(z[0]), "imag": str(z[1])}
                for v, z in sorted(c.items())],
    "constants": {"L": str(L), "C0": str(C0), "C1": str(C1),
                  "sigma_A_squared": str(variance),
                  "fourth_mixed_uniform_lower": str(mixed_lower)},
    "fourth_cosine_weights": {str(h): str(z) for h, z in sorted(weights.items())},
    "finite_collisions": finite_collisions,
    "finite_additive_uniqueness": finite_additive_uniqueness,
    "decimal": decimal,
    "input_sha256": hashes,
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"status": result["status"], "constants": result["constants"],
                  "finite_r": [v["r"] for v in finite_collisions],
                  "decimal": decimal, "output": str(OUT)},
                 ensure_ascii=False, indent=2))
