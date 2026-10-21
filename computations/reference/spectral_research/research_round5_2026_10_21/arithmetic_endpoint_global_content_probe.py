"""Exact bounded discriminator for a proposed good-place argument.

For endpoint Fourier minors at N=7*n, test whether the determinant is
divisible by 5 in the entire ring Z[zeta_N]. Such a result would mean
that every primitive-root embedding vanishes modulo 5. Non-discovery
in a finite run is not a theorem about arbitrary n or all minor sizes.

All determinant coefficients and reductions are computed as integers;
NumPy is used only for bounded integer permutation sums.
"""
import argparse
from functools import lru_cache
from itertools import permutations
import numpy as np
from arithmetic_endpoint_minor_probe import bounded_compositions, endpoint_sets
from arithmetic_endpoint_mod5_certificate import integer_division, remainder


@lru_cache(None)
def cyclotomic(N):
    polynomial = [-1] + [0] * (N - 1) + [1]
    for divisor in range(1, N):
        if N % divisor == 0:
            polynomial, rest = integer_division(polynomial, list(cyclotomic(divisor)))
            assert rest == []
    return tuple(polynomial)


@lru_cache(None)
def permutation_data(k):
    assert k <= 9
    array = np.array(list(permutations(range(k))), dtype=np.int64)
    inversion_count = sum(array[:, i] > array[:, j]
                          for i in range(k) for j in range(i + 1, k))
    return array, inversion_count % 2 == 0


def determinant_polynomial(rows, columns, N):
    permutation_array, positive = permutation_data(len(rows))
    matrix = np.asarray(columns, dtype=np.int64)[permutation_array]
    exponent = (matrix @ np.asarray(rows, dtype=np.int64)) % N
    coefficients = np.bincount(exponent[positive], minlength=N)
    coefficients -= np.bincount(exponent[~positive], minlength=N)
    return coefficients.tolist()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--max-total", type=int, default=7)
    args = parser.parse_args()
    assert args.n % 5 and args.n % 7
    N = 7 * args.n
    phi = list(cyclotomic(N))
    for k in range(2, args.max_total + 1):
        tested = 0
        bad = []
        for counts in bounded_compositions(k, 7, args.n):
            rows, columns = endpoint_sets(args.n, counts)
            D = determinant_polynomial(rows, columns, N)
            tested += 1
            if remainder(D, phi, 5) == []:
                _, integral_remainder = integer_division(D, phi)
                bad.append((counts, rows, columns, integral_remainder))
                print("ALL-PLACE ZERO REDUCTION:", "N=", N, "k=", k,
                      "counts=", counts, "rows=", rows, "cols=", columns,
                      "integer Phi_N remainder=", integral_remainder, flush=True)
                break
        print("N=", N, "k=", k, "tested=", tested,
              "all-place zero reductions found=", len(bad), flush=True)
        if bad:
            break


if __name__ == "__main__":
    main()
