"""Check exact cancellations, norm bounds, and finite examples of the history formulas."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')


from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from math import gcd, isqrt
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).with_name("data") / "checks.json"


def read_torsion_helpers():
    spec = spec_from_file_location("bgs_torsion", ROOT / "torsion_transport" / "bgs_packet_check.py")
    helper = module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper


def time_gap(l):
    ceiling = 0
    power = 1
    while power < l:
        power *= 5
        ceiling += 1
    return 16 + ceiling


def constants(torsion):
    coefficients, _ = torsion.rational_checks()
    bound = Fraction(0)
    for coefficient in coefficients.values():
        square = sp.simplify(coefficient * sp.conjugate(coefficient))
        upper = isqrt((10**12 * int(square.p)) // int(square.q)) + 1
        bound += Fraction(upper, 10**6)
    assert bound < Fraction(6, 5)

    # Squared moduli of the unstable/stable Fourier probes before the
    # conjugacy remainder, with lambda <= 6 for the unstable probe.
    squares = [Fraction(101, 2 * 40000), Fraction(1, 4 * 40000)]
    for square in squares:
        assert square / 36 > Fraction(1, 3000)**2
    tau = Fraction(1, 10**80)
    error_divided_by_tau = 10**8 * tau + Fraction(10**6, 10**40)
    assert Fraction(1, 3000) - error_divided_by_tau > Fraction(1, 10000)

    for l in (3, 5, 7, 9, 45, 343, 1001):
        gap = time_gap(l)
        assert 5**gap >= l * 5**16
        assert Fraction(2000, 5**gap - 1) <= Fraction(1, 2 * 10**5 * l)
        assert Fraction(5**gap, 2 * 10**5 * l) > 100000
    matrix = sp.Matrix([[3, -4], [-2, 3]])
    assert matrix.det() == 1
    eigenvalue = 3 + 2 * sp.sqrt(2)
    unstable = sp.Matrix([[sp.Rational(1, 2), -1 / sp.sqrt(2)]])
    stable = sp.Matrix([[sp.Rational(1, 2), 1 / sp.sqrt(2)]])
    assert sp.simplify(unstable * matrix - eigenvalue * unstable) == sp.zeros(1, 2)
    assert sp.simplify(stable * matrix.inv() - eigenvalue * stable) == sp.zeros(1, 2)
    return str(bound)


def add_mod(a, b, modulus):
    return tuple((x + y) % modulus for x, y in zip(a, b, strict=True))


def reduce_word(word, modulus):
    """Delete identity tags and multiply adjacent entries at equal times."""
    stack = []
    for time, tag in word:
        if stack and stack[-1][0] == time:
            _, previous = stack.pop()
            tag = add_mod(previous, tag, modulus)
        if tag != (0, 0):
            stack.append((time, tag))
    return stack


def cancellation_check():
    """Exhaust length-four words, including products on disjoint blocks."""
    modulus = 3
    labels = tuple(product(range(modulus), repeat=2))
    folded_identities = 0
    disjoint_identities = 0
    for tags in product(labels, repeat=4):
        word = list(zip((0, 1, 1, 0), tags, strict=True))
        cancelled = not reduce_word(word, modulus)
        prediction = (add_mod(tags[0], tags[3], modulus) == (0, 0)
                      and add_mod(tags[1], tags[2], modulus) == (0, 0))
        assert cancelled == prediction
        folded_identities += cancelled
        disjoint = list(zip((0, 1, 3, 2), tags, strict=True))
        disjoint_identities += not reduce_word(disjoint, modulus)

    # Two palindromes with disjoint time blocks and inverse time orientation.
    rng = np.random.default_rng(506)
    for q in (2, 3, 7):
        for _ in range(100):
            left = [tuple(row) for row in rng.integers(0, modulus, size=(q, 2))]
            right = [tuple(row) for row in rng.integers(0, modulus, size=(q, 2))]
            left_inv = [add_mod((0, 0), tuple(-v for v in tag), modulus) for tag in left]
            right_inv = [add_mod((0, 0), tuple(-v for v in tag), modulus) for tag in right]
            word = list(zip((*range(q), *reversed(range(q))),
                            (*left, *reversed(left_inv)), strict=True))
            other = list(zip((*range(q, 2*q), *reversed(range(q, 2*q))),
                             (*right, *reversed(right_inv)), strict=True))
            assert not reduce_word(word + other, modulus)
            idx = q + int(rng.integers(0, q))
            time, tag = other[idx]
            other[idx] = (time, add_mod(tag, (1, 0), modulus))
            result = reduce_word(word + other, modulus)
            assert sum(t == max(x[0] for x in result) for t, _ in result) == 1

    assert folded_identities == 81 and disjoint_identities == 1
    return {"folded_words": 9**4, "folded_identities": folded_identities,
            "disjoint_identities": disjoint_identities}


def history_matrix(projectors):
    n = projectors[0][0].shape[0]
    histories = [np.eye(n, dtype=complex)]
    for row in projectors:
        histories = [prefix @ p for prefix in histories for p in row]
    return np.array(histories)


def actual_map_finite_check(torsion, n, l, q):
    coefficients, _ = torsion.rational_checks()
    a = sum(complex(c) * (-1)**((k*s) % 2) * torsion.weyl(n, s, k)
            for (k, s), c in coefficients.items())
    values, vectors = eigh(a)
    test_strength = 0.008
    kick = (vectors * np.exp(1j * test_strength * n * values)) @ vectors.conj().T
    u = kick @ torsion.cat(n)
    d = n // (l*l)
    base = torsion.sector_basis(n, l)
    projectors = []
    for i in range(l*l):
        sector = base[:, i*d:(i+1)*d]
        projectors.append(sector @ sector.conj().T)
    delta = np.linalg.matrix_power(u, time_gap(l))
    grids = [projectors]
    for _ in range(2*q-1):
        grids.append([delta @ p @ delta.conj().T for p in grids[-1]])
    histories = [history_matrix(grids[i*q:(i+1)*q]) for i in range(2)]
    count = len(histories[0])
    identity = np.eye(n)
    prob_error = 0.0
    for batch in histories:
        assert np.linalg.norm(batch.sum(axis=0) - identity) < 2e-10
        probabilities = batch.conj().transpose(0, 2, 1) @ batch
        prob_error = max(prob_error, float(np.linalg.norm(probabilities.sum(axis=0) - identity)))
    assert prob_error < 2e-10

    transport = np.linalg.matrix_power(delta, q)
    assert np.max(np.abs(histories[1] - transport @ histories[0] @ transport.conj().T)) < 3e-12
    centered = np.concatenate(histories, axis=0) - identity/count
    rows = np.sqrt(count/n) * centered.reshape(2*count, n*n)
    gram_bound = float(np.linalg.norm(rows, ord=2)**2)
    excess = []
    for m in (0, 1, n, 2*n+7):
        power = np.linalg.matrix_power(u, m)
        raw = np.einsum("kij,ji->k", histories[0], power)/n
        scalar = np.trace(power)/n
        error = count*float(np.vdot(raw-scalar/count, raw-scalar/count).real)
        assert abs(error - (count*np.vdot(raw, raw).real-abs(scalar)**2)) < 5e-11
        assert error <= gram_bound/2+1e-10
        excess.append(error)
    return {"N": n, "L": l, "q": q, "finite_test_strength": test_strength,
            "max_probability_identity_error": prob_error,
            "max_observed_trace_variance": max(excess)}


def cyclic_tensor_check():
    dimension = 9
    factors = 4
    n = dimension**factors
    z = np.array([x for x in product(range(dimension), repeat=factors)], dtype=int)
    images = np.roll(z, 1, axis=1)
    weights = dimension**np.arange(factors-1, -1, -1)
    permutation = images@weights
    indices = np.arange(n)
    sample_traces = []
    position = indices.copy()
    for m in range(1, 2*factors+1):
        position = permutation[position]
        trace = int(np.count_nonzero(position == indices))
        assert trace == dimension**gcd(factors, m)
        sample_traces.append(trace)

    paths = (z[:, (0, 1)]@np.array([dimension, 1]))
    second_paths = (z[:, (2, 3)]@np.array([dimension, 1]))
    assert np.all(np.bincount(paths) == n//dimension**2)
    cross = np.bincount(paths*dimension**2 + second_paths, minlength=n)
    assert len(cross) == n and np.all(cross == 1)
    spike_count = sum(m % factors == 0 for m in range(n, 2*n))
    assert spike_count == n//factors
    return {"N": n, "cycle": factors, "sample_exact_traces": sample_traces,
            "exact_scalar_returns_in_Heisenberg_window": spike_count}


def phased_tensor_check():
    """Exact coset allocation for a monomial matrix with clustered clock spectrum."""
    dimension, factors, multiplicity = 9, 3, 9
    n = dimension**factors
    clock_size = n//multiplicity
    digits = np.array(list(product(range(dimension), repeat=factors)), dtype=int)
    weights = dimension**np.arange(factors-1, -1, -1)
    permutation = np.roll(digits, 1, axis=1)@weights
    cycle_sizes = []
    visited = set()
    for index in range(n):
        if index in visited:
            continue
        length = 0
        while index not in visited:
            visited.add(index)
            index = int(permutation[index])
            length += 1
        cycle_sizes.append(length)
    assert sum(cycle_sizes) == n
    slots = np.zeros((multiplicity, clock_size), dtype=bool)
    assigned_roots = Counter()
    for size in sorted(cycle_sizes, reverse=True):
        assert clock_size % size == 0
        spacing = clock_size//size
        layer, anchor = np.argwhere(~slots[:, :spacing])[0]
        roots = [int(anchor)+k*spacing for k in range(size)]
        assert not slots[layer, roots].any()
        slots[layer, roots] = True
        assigned_roots.update(roots)
        # Each assigned root satisfies the corresponding monomial characteristic
        # equation z^size = e^{2 pi i anchor*size / clock_size}.
        assert all((size*(root-anchor)) % clock_size == 0 for root in roots)
    assert slots.all()
    assert len(assigned_roots) == clock_size and set(assigned_roots.values()) == {multiplicity}
    return {"N": n, "factor_cycle_count": {str(k):v for k,v in sorted(Counter(cycle_sizes).items())},
            "clock_points": clock_size, "multiplicity": multiplicity}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    torsion = read_torsion_helpers()
    report = {
        "certified_upper_bound_for_symbol_l1": constants(torsion),
        "word_enumeration": cancellation_check(),
        "finite_actual_formula_examples": [
            actual_map_finite_check(torsion, n, l, q)
            for n, l, q in ((9, 3, 3), (45, 3, 2), (49, 7, 2))
        ],
        "cyclic_tensor_model": cyclic_tensor_check(),
        "phased_tensor_model": phased_tensor_check(),
    }
    if args.record:
        DATA.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    if args.verify:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        assert report.keys() == expected.keys()
        for key, value in report.items():
            if key == "finite_actual_formula_examples":
                for row, old in zip(value, expected[key], strict=True):
                    for field in row:
                        assert abs(row[field]-old[field]) < 1e-9
            else:
                assert value == expected[key]
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
