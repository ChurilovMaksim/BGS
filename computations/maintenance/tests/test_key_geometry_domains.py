"""Independent small-field domain and representative-invariance regressions.

Run directly against this checkout. The oracle
enumerates original ordered quadruples with Python integers and independently
finds inverses; it does not use either distribution routine or its validator.
These finite checks assert no asymptotic or BGS universality result.
"""
from __future__ import annotations

from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "python"))
from bgs import key_geometry as kg


def oracle(prime, subgroup):
    inverse = {x: next(y for y in range(1, prime) if x*y % prime == 1)
               for x in range(1, prime)}
    histogram = [0] * prime
    classes = dict(off_to_off=0, diagonal_to_off=0,
                   off_to_diagonal=0, diagonal_to_diagonal=0)
    for x in range(2, prime):
        for y in range(2, prime):
            for z in range(2, prime):
                for w in range(2, prime):
                    if x*z*inverse[y]*inverse[w] % prime not in subgroup:
                        continue
                    if (x-1)*(z-1)*inverse[y-1]*inverse[w-1] % prime not in subgroup:
                        continue
                    histogram[(x-y+z-w) % prime] += 1
                    left = "diagonal" if x == y else "off"
                    right = "diagonal" if z == w else "off"
                    classes[left + "_to_" + right] += 1
    return histogram, classes


class KeyGeometryDomainTests(unittest.TestCase):
    def distributions(self, prime, subgroup):
        return (
            ("fast", lambda: kg.fast_difference_distribution(prime, subgroup)),
            ("direct", lambda: kg.direct_difference_distribution(
                prime, subgroup, kg.explicit_key_table(5))),
        )

    def test_invalid_subgroups_rejected_independently(self):
        invalid = (
            np.array([0, 1]), np.array([1, 5]), np.array([0]),
            np.array([], dtype=int), np.array([1, 6]), np.array([4]),
            np.array([1, 2]), np.array([[1, 4]]), np.array(1),
            np.array([1.0, 4.0]), np.array([1.2, 4.2]),
            np.array(["1", "4"]), np.array([True]),
            np.array([1, False], dtype=object), np.array([1, None], dtype=object),
            np.array([1, 4j]), [1, 4], (1, 4),
        )
        for subgroup in invalid:
            for name, call in self.distributions(5, subgroup):
                with self.subTest(subgroup=repr(subgroup), implementation=name):
                    with self.assertRaises(ValueError):
                        call()

    def test_invalid_prime_domains(self):
        for prime in (True, False, 0, -5, 2, 9, 15, 5.0, 5.5, "5", None):
            for name, call in self.distributions(prime, np.array([1, 4])):
                with self.subTest(prime=prime, implementation=name):
                    with self.assertRaises(ValueError):
                        call()

    def test_representatives_against_original_quadruple_oracle(self):
        # Every subgroup at each small odd prime, constructed independently by
        # exhaustive cyclic generation rather than kg.subgroup_elements.
        for prime in (3, 5, 7, 11):
            subgroups = set()
            for generator in range(1, prime):
                values = {pow(generator, exponent, prime) for exponent in range(prime-1)}
                subgroups.add(tuple(sorted(values)))
            for canonical in sorted(subgroups):
                expected, expected_classes = oracle(prime, set(canonical))
                variants = (
                    np.array(canonical), np.array(canonical[::-1]),
                    np.array([v+prime for v in canonical]),
                    np.array([v-prime*3 for v in canonical]),
                    np.array([v+prime*((-1)**i)*10**80 for i,v in enumerate(canonical)], dtype=object),
                    np.array(canonical, dtype=np.uint64),
                )
                for subgroup in variants:
                    for name, call in (
                        ("fast", lambda: kg.fast_difference_distribution(prime, subgroup)),
                        ("direct", lambda: kg.direct_difference_distribution(
                            prime, subgroup, kg.explicit_key_table(prime))),
                    ):
                        with self.subTest(prime=prime, subgroup=repr(subgroup), implementation=name):
                            result, classes = call()
                            self.assertEqual(result.tolist(), expected)
                            self.assertEqual(classes, expected_classes)
                            self.assertEqual(classes, kg.expected_coupling_classes(prime, len(canonical)))

    def test_reported_example_and_input_unchanged(self):
        for values in ([1, 4], [1, 9], [6, 9], [-4, -1]):
            subgroup = np.array(values)
            before = subgroup.copy()
            for _, call in self.distributions(5, subgroup):
                self.assertEqual(call()[0].tolist(), [15, 1, 2, 2, 1])
                np.testing.assert_array_equal(subgroup, before)

    def test_canonical_validator_output(self):
        original = np.array([9, 6, -100000000000000000001], dtype=object)
        # -100000000000000000001 is also residue 4: duplicates are rejected
        # after normalization rather than accepted as distinct representatives.
        with self.assertRaises(ValueError):
            kg._validate_subgroup_array(5, original)
        normalized = kg._validate_subgroup_array(np.int64(5), np.array([9, 6]))
        np.testing.assert_array_equal(normalized, [4, 1])
        self.assertEqual(normalized.dtype, np.dtype(np.int64))
        self.assertEqual(kg.fast_difference_distribution(np.int64(5), normalized)[0].tolist(),
                         [15, 1, 2, 2, 1])

    def test_integer_helper_contracts(self):
        np.testing.assert_array_equal(kg.subgroup_elements(np.int64(5), np.int64(9), np.int64(2)), [1,4])
        self.assertEqual(kg.key_difference(np.int64(5), np.int64(2), np.int64(3)), 2)
        for value in (True, 2.0, "2", None):
            with self.subTest(value=value):
                for call in (
                    lambda: kg.subgroup_elements(5, 4, value),
                    lambda: kg.subgroup_elements(5, value, 2),
                    lambda: kg.key_difference(5, value, 3),
                    lambda: kg.expected_coupling_classes(5, value),
                    lambda: kg.variety_count_formula(5, value),
                ):
                    with self.assertRaises(ValueError):
                        call()


if __name__ == "__main__":
    unittest.main()
