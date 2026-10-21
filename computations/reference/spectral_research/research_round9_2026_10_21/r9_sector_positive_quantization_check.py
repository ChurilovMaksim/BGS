"""Finite convention checks for Section 7; not asymptotic evidence.

Uses only the Python standard library. The proof is in
r9_sector_continuous_symbol_stability.md. This independently constructs
the coherent frame from the original modular-midpoint T_N action.
"""

from cmath import exp
from math import floor, pi, sqrt


def phase(n, t):
    return exp(2j * pi * (t % n) / n)


def apply_t(n, a, b, vector):
    half = pow(2, -1, n)
    return [
        phase(n, b * (x + half * a)) * vector[(x + a) % n]
        for x in range(n)
    ]


def packet(n):
    radius = floor(sqrt(n))
    center = lambda x: x if x <= n // 2 else x - n
    return [
        (1 / sqrt(2 * radius + 1)) if abs(center(x)) <= radius else 0j
        for x in range(n)
    ]


def frame_character(n, k, l):
    phi = packet(n)
    result = [[0j] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            state = apply_t(n, a, b, phi)
            coefficient = phase(n, -k * a + l * b) / n
            for x in range(n):
                for y in range(n):
                    result[x][y] += coefficient * state[x] * state[y].conjugate()
    return result


def predicted_character(n, k, l):
    phi = packet(n)
    sign = (-1) ** (k * l)
    adjoint_phi = [sign * z for z in apply_t(n, -l, -k, phi)]
    chi = sum(phi[x].conjugate() * adjoint_phi[x] for x in range(n))
    half = pow(2, -1, n)
    matrix = [[0j] * n for _ in range(n)]
    for x in range(n):
        matrix[x][(x + l) % n] = chi * sign * phase(n, k * (x + half * l))
    return matrix


def entry_error(left, right):
    return max(
        abs(left[x][y] - right[x][y])
        for x in range(len(left))
        for y in range(len(left))
    )


def main():
    frequencies = [(0, 0), (1, 1), (2, -1), (-3, 2), (7, -5)]
    for n in (3, 5, 9, 15):
        errors = [
            entry_error(frame_character(n, k, l), predicted_character(n, k, l))
            for k, l in frequencies
        ]
        maximum = max(errors)
        assert maximum < 2e-12, (n, maximum)
        print(f"N={n:2d}: maximum entry error {maximum:.3e}; all signs accepted")
    print("PASS: original modular midpoint, composite dimensions, and aliased frequencies.")


if __name__ == "__main__":
    main()
