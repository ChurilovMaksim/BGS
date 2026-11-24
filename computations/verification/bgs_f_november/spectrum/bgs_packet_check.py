"""Exact arithmetic for stationary phase and algebraic spectral rigidity."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research.coefficients import raw_symbol

P = 7
SQUARES = {1, 2, 4}
S = (3, 4, 2, 3)
IDENTITY = (1, 0, 0, 1)
COEFFICIENTS = raw_symbol()


def multiply(a, b, modulus):
    return tuple(
        sum(a[2 * i + h] * b[2 * h + j] for h in range(2)) % modulus
        for i, j in product(range(2), repeat=2)
    )


def power(a, exponent, modulus):
    result = IDENTITY
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        exponent //= 2
    return result


def rho_at(k):
    rho = 3
    modulus = P
    for _ in range(1, k):
        rho, = [rho + digit * modulus for digit in range(P)
                if ((rho + digit * modulus)**2 - 2) % (P * modulus) == 0]
        modulus *= P
    return rho


def split(label, rho, modulus):
    a, b = label
    return ((a + rho * b) % modulus,
            (a - rho * b) * pow(-2 * rho, -1, modulus) % modulus)


def p_log(x, k):
    modulus = P**k
    z = (pow(x, 6, modulus) - 1) % modulus
    acc = 0
    # Terms j >= 2k have valuation j - v_7(j) >= k.
    for j in range(1, 2*k):
        unit, divider = j, 1
        while unit % P == 0:
            unit //= P
            divider *= P
        term, remainder = divmod(pow(z, j), divider)
        assert remainder == 0
        acc += (-1)**(j+1) * (term % modulus) * pow(unit, -1, modulus)
    return acc * pow(6, -1, modulus) % modulus


def stationary_at(k):
    """Table of stationary points and critical phases for primitive labels."""
    modulus = P**k
    rho = rho_at(k)
    iv = pow(2, -1, modulus)
    logs = {x: p_log(x, k) for x in range(1, modulus) if x % P}
    table = defaultdict(list)
    for label, (_, imaginary) in COEFFICIENTS.items():
        a, b = split(label, rho, modulus)
        if a % P == 0:
            assert b % P == 0 and label in [(0, -7), (0, 7)]
            assert imaginary == 0
            continue
        assert b % P
        for x in logs:
            if x % P not in SQUARES:
                continue
            y = (x + a) % modulus
            if y not in logs:
                continue
            channel = "diagonal" if y % P in SQUARES else "offdiagonal"
            if channel == "diagonal" and not imaginary:
                continue
            ell = b * x * y * pow(a, -1, modulus) % modulus
            phase = (b * (x + a * iv) + ell * (logs[y] - logs[x])) % modulus
            table[ell, channel].append((label, x, phase))
    return table


def phase_witnesses():
    table = stationary_at(3)
    rows = {}
    for ell in range(1, P**3):
        if ell % P in (0, 4):
            continue
        candidates = []
        for channel in ["diagonal", "offdiagonal"]:
            stationary = table[ell, channel]
            phase_counts = Counter(phase for _, _, phase in stationary)
            for label, x, phase in stationary:
                if phase_counts[phase] != 1 or phase % P == 0:
                    continue
                assert all((2 * z + split(v, 3, P)[0]) % P
                           for v, z, h in stationary if h % P == phase % P)
                candidates.append((channel, label, x, phase))
        assert candidates, ell
        rows[str(ell)] = sorted(candidates)[0]

    degenerate = stationary_at(1)
    assert not degenerate[4, "diagonal"]
    assert {label for label, _, _ in degenerate[4, "offdiagonal"]} == {
        (0, -6), (0, 1), (0, 8)
    }
    assert len(degenerate[4, "offdiagonal"]) == 3
    centers = {}
    for label, x, phase in degenerate[4, "offdiagonal"]:
        a, b = split(label, rho_at(2), P**2)
        assert (2*x+a) % P == 0 and phase == 0
        centers[str(label)] = (-a*b*pow(4, -1, P**2)) % P**2
    assert len(set(centers.values())) == 3
    assert all(value % P == 4 for value in centers.values())
    return rows, centers



def depth_witnesses():
    """Test separation of the two singular values, and the depth-two block."""
    modulus = P**3
    inv_two = pow(2, -1, modulus)
    norm_multiplier = pow(-2*rho_at(3), -1, modulus)
    aggregated = defaultdict(lambda: [0, 0])
    for (a, b), (real, imaginary) in COEFFICIENTS.items():
        if (-a-3*b) % P in SQUARES:
            key = a*a - 2*b*b
            aggregated[key][0] += real
            aggregated[key][1] += imaginary
    assert len(aggregated) == 11 and all(any(c) for c in aggregated.values())

    logs = {x: p_log(x, 3) for x in range(1, modulus) if x % P}
    deep_phase = {}
    shallow_phase = {}
    for norm in aggregated:
        q = norm*norm_multiplier % modulus
        deep_phase[norm] = -q*inv_two % modulus
        for z in logs:
            x = (P*z-1) % modulus
            mu = q*z*x % modulus
            assert (mu, norm) not in shallow_phase
            shallow_phase[mu, norm] = (q*(-inv_two+P*z)
                                            + P*mu*(logs[z]-logs[x])) % modulus

    witnesses = {}
    disjoint = {}
    for mu in logs:
        sign = {q: (mu*pow(q*norm_multiplier, -1, P)) % P in SQUARES for q in aggregated}
        opposing = [(q, r) for q, r in product(sorted(aggregated), repeat=2)
                    if sign[q] != sign[r]]
        determinant = [(q, r) for q, r in combinations_with_replacement(sorted(aggregated), 2)
                       if sign[q] == sign[r]
                       and sum(x*y for x, y in zip(aggregated[q], aggregated[r]))]
        for depth in (1, 2):
            phase = {q: (shallow_phase[mu, q] if depth == 1 else deep_phase[q])
                     for q in aggregated}
            oppose_terms = [((phase[q]-phase[r]) % modulus, q, r) for q, r in opposing]
            det_terms = [((phase[q]+phase[r]) % modulus, q, r) for q, r in determinant]
            result = []
            for terms in (oppose_terms, det_terms):
                counts = Counter(t[0] for t in terms)
                result.append(min(t for t in terms if counts[t[0]] == 1))
            witnesses[str(depth), str(mu)] = result
        if mu < P:
            trace = {(q-r) % P**2 for q, r in product(aggregated, repeat=2) if sign[q] == sign[r]}
            quartic = [((q+r-u-v) % modulus, (q, r), (u, v))
                       for (q, r), (u, v) in product(determinant, repeat=2)]
            counts = Counter(t[0] for t in quartic)
            witness = 115, (-162, -162), (-97, 1)
            assert witness in quartic and counts[115] == 1 and 115 % P**2 not in trace
            disjoint[str(mu)] = witness
    rows = {":".join(key): value for key, value in witnesses.items()}
    return {
        "determinant_and_offdiagonal": rows,
        "disjoint_depth_two": disjoint,
        "aggregated_coefficients": dict(sorted(aggregated.items())),
    }

def orbit_curvature():
    aggregates = defaultdict(lambda: [0, 0])
    for (a, b), (real, imaginary) in COEFFICIENTS.items():
        depth = int(a % P == b % P == 0)
        div = P**depth
        norm = (a*a - 2*b*b) // div**2
        square = (a//div + 3*(b//div)) % P in SQUARES
        z = aggregates[depth, norm, square]
        z[0] += real
        z[1] += imaginary
    assert len(aggregates) == 24
    c = Fraction(sum(P**d * (r*r+i*i) for (d, _, _), (r, i) in aggregates.items()),
                 4000**2)
    assert c == Fraction(11370883, 4000000)
    return {
        "C": str(c),
        "primitive_nonzero": sum(r != 0 or i != 0 for (d, _, _), (r, i) in aggregates.items() if not d),
        "groups": [(*key, *value) for key, value in sorted(aggregates.items())],
    }


def sparse_binary_power(x, tame, imaginary):
    """Expand in the basis 1, zeta_3, i, i*zeta_3."""
    tame %= 3
    tame_terms = [(tame, 1)] if tame < 2 else [(0, -1), (1, -1)]
    for residual_tame, z in tame_terms:
        yield residual_tame + 2 * imaginary, x*z


def exact_first_order(k):
    modulus = P**k
    lower = P**(k-1)
    rho = rho_at(k)
    logs = {x: p_log(x, k) for x in range(1, modulus) if x % P}
    exponents = {pow(3, j, P): j % 3 for j in range(6)}
    prepared = []
    iv = pow(2, -1, modulus)
    for label, (real, imaginary) in COEFFICIENTS.items():
        a, b = split(label, rho, modulus)
        for x in logs:
            if x % P not in SQUARES:
                continue
            y = (x+a) % modulus
            if y not in logs:
                continue
            standard_phase = b * (x + a*iv) % modulus
            log = (logs[y]-logs[x]) % modulus
            tame = (exponents[y % P] - exponents[x % P]) % 3
            channel = "diagonal" if y % P in SQUARES else "offdiagonal"
            prepared.append((channel, standard_phase, log, tame,
                             real if channel == "offdiagonal" else 0, imaginary))
    classifications = defaultdict(lambda: [0, 0])
    for ell, h in product(range(lower), range(3)):
        if ell % P == 0:
            continue
        basis_coeff = defaultdict(int)
        for channel, phase, log, tame, real, imaginary in prepared:
            exponent = (phase+ell*log) % modulus
            if exponent < 6*lower:
                roots = [(exponent, 1)]
            else:
                roots = [(exponent % lower + j*lower, -1) for j in range(6)]
            for e, sign in roots:
                for i, coeff in sparse_binary_power(real, h*tame, 0):
                    basis_coeff[channel, e, i] += sign*coeff
                for i, coeff in sparse_binary_power(imaginary, h*tame, 1):
                    basis_coeff[channel, e, i] += sign*coeff
        classifications[ell % P][int(any(basis_coeff.values()))] += 1
    return dict(sorted(classifications.items()))


def inert_primes():
    primes = []
    for p in range(3, 1000, 2):
        if any(p % d == 0 for d in range(3, isqrt(p)+1, 2)):
            continue
        if pow(2, (p-1)//2, p) != p-1:
            continue
        order = next(h for h in range(1, p+2) if power(S, h, p) == IDENTITY)
        if order == p+1 and power(S, order, p*p) != IDENTITY:
            primes.append(p)
    assert primes[:3] == [3, 5, 11]
    return primes


def summary():
    assert (Fraction(5) + Fraction(3, 16)) / 6 == Fraction(83, 96)
    assert Fraction(36, 49) * Fraction(83, 96) == Fraction(249, 392)
    assert Fraction(8, 3) - Fraction(249, 392) == Fraction(2389, 1176)
    ratio = Fraction(1, 7)
    base = Fraction(2389, 1176)
    first_depth = Fraction(18, 49)*12*ratio
    second_depth = Fraction(18, 49)*28*ratio**2
    later_depths = Fraction(18, 49)*ratio**3*(52/(1-ratio)+32*ratio/(1-ratio)**2)
    assert base - first_depth - second_depth - later_depths == Fraction(64549, 57624)
    assert Fraction(249, 392)+Fraction(72, 49)*ratio/(1-ratio) == Fraction(345, 392)
    table, degenerate = phase_witnesses()
    checks = {}
    for k in (2, 3):
        checks[k] = exact_first_order(k)
    assert checks[2] == {ell: ([3, 0] if ell in (4, 6) else [0, 3])
                         for ell in range(1, 7)}
    assert checks[3] == {ell: ([12, 9] if ell == 4 else [0, 21])
                         for ell in range(1, 7)}
    return {
        "verified_inert_primes_under_1000": inert_primes(),
        "stationary_witnesses_mod_343": table,
        "degenerate_centers_mod_49": degenerate,
        "small_7_powers_unsplit_split_first_order": checks,
        "exact_curvature": orbit_curvature(),
        "higher_depth": depth_witnesses(),
        "limiting_fraction_split_doublets": "83/96",
        "asymptotic_simple_levels_lower_fraction": "345/392",
        "asymptotic_plateau_upper": "64549/57624",
    }


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = summary()
    path = ROOT / "spectrum/data/checks.json"
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.verify:
        assert encoded == path.read_text()
        print("Exact phase witnesses, small cyclotomic matrices, curvature, and inert orders verified.")
    else:
        path.write_text(encoded)
        print("Wrote", path)
