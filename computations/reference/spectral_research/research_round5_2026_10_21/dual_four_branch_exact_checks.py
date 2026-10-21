"""Finite exact arithmetic checks for the four-branch kernel.

This checks the complete root-of-unity cases, not the analytic WKB estimates.
No floating-point eigenvalue calculation or changed kick is involved.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path


def root8(exponent, coefficient=F(1)):
    """Represent coefficient*zeta_8**exponent in Q[zeta_8], zeta_8**4=-1."""
    exponent %= 8
    result = [F(0)] * 4
    result[exponent % 4] = coefficient * (-1 if exponent >= 4 else 1)
    return tuple(result)


def add(vectors):
    vectors = list(vectors)
    return tuple(sum(v[j] for v in vectors) for j in range(4))


def g_exponent(nu, index):
    return [-3 * nu, 0, 4 - 3 * nu, 0][index % 4]


def run():
    checks = 0
    for nu in (1, 3, 5, 7):
        for x in range(8):
            rhs = add(root8(g_exponent(nu, m) + 2 * m * x, F(1, 2))
                      for m in range(4))
            assert rhs == root8(-3 * nu * x * x)
            checks += 1
        for residue in (1, 3, 5, 7):
            if (nu * residue + 1) % 8:
                continue
            for index in range(4):
                assert (g_exponent(nu, index - 3)
                        - g_exponent(nu, index)
                        - (2 * residue * index - 3 * residue)) % 8 == 0
                checks += 1
            for y in range(8):
                for m in range(4):
                    left = g_exponent(nu, m - nu * y)
                    left += 2 * residue * m - 3 * residue + 2 * y
                    right = g_exponent(nu, m - 3 - nu * y)
                    assert (left - right) % 8 == 0
                    checks += 1
    for n in range(3, 1000, 2):
        nu = next(v for v in (1, 3, 5, 7) if (v * n + 1) % 8 == 0)
        inv8 = pow(8, -1, n)
        assert 8 * inv8 == 1 + nu * n
        checks += 1
    # The explicit point used in the interference countercheck.
    shifts = [F(-3, 500), F(-9, 2000), F(3, 500), F(9, 2000)]
    assert shifts[0] < shifts[1] < shifts[3] < shifts[2]
    assert min(abs(a - b) for a in shifts for b in shifts if a != b) == F(3, 2000)
    print(f"PASS: {checks} exact modular/Gauss identities; exact action ordering.")
    target = Path(__file__).with_name("dual_physical_four_branch_kernel.md")
    print("Kernel source SHA256:", sha256(target.read_bytes()).hexdigest())


if __name__ == "__main__":
    run()
