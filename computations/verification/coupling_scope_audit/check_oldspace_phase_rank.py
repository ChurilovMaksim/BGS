"""Exact linear and quadratic phase checks for the sevenfold oldspace scope extension.

Computes in Q(zeta_7, i) with the basis zeta_7**r and i*zeta_7**r,
0 <= r <= 5. These are independent because this field is Q(zeta_28),
of degree 12. This check does not test any analytic packet estimates.
"""

from fractions import Fraction


def root_power(exponent: int) -> list[int]:
    r = exponent % 7
    # Phi_7(zeta)=0, hence zeta**6=-sum(zeta**r, 0<=r<=5).
    if r == 6:
        return [-1] * 6
    return [int(j == r) for j in range(6)]


def phase_vector(j: int) -> list[int]:
    """Coordinates of 100*b_j: twice the cosine difference + 20*sin."""
    pos, neg = root_power(j), root_power(-j)
    pos2, neg2 = root_power(2 * j), root_power(-2 * j)
    cosine = [a + b - c - d for a, b, c, d in zip(pos2, neg2, pos, neg)]
    sine = [-10 * (a - b) for a, b in zip(pos, neg)]
    return cosine + sine


def curvature_vector(j: int) -> list[int]:
    """Coordinates of 400*d_j for the relative curvature d_j."""
    pos, neg = root_power(j), root_power(-j)
    pos2, neg2 = root_power(2 * j), root_power(-2 * j)
    one = root_power(0)
    cosine = [1020 * (a + b - 2 * c) for a, b, c in zip(pos, neg, one)]
    sine = [-102 * (a - b) + 57 * (c - d)
            for a, b, c, d in zip(pos, neg, pos2, neg2)]
    return cosine + sine


def rank(vectors: list[list[int]]) -> int:
    """Row rank over Q."""
    rows = [list(map(Fraction, v)) for v in vectors]
    r = 0
    for j in range(len(rows[0])):
        pivot = next((k for k in range(r, len(rows)) if rows[k][j]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        source = rows[r]
        for k in range(r + 1, len(rows)):
            factor = rows[k][j] / source[j]
            if factor:
                rows[k] = [x - factor * y for x, y in zip(rows[k], source)]
        r += 1
        if r == len(rows):
            break
    return r


def check() -> None:
    vectors = [phase_vector(j) for j in range(1, 7)]
    if any(map(sum, zip(*vectors))):
        raise ValueError("the sum of the six phase coefficients is nonzero")
    one = [1] + [0] * 11
    if rank(vectors) != 5 or rank(vectors + [one]) != 6:
        raise ValueError("wrong phase rank or an unexpected rational relation")
    print("PASS: phase rank 5; rank with 1 is 6; only the sum relation survives.")

    curvatures = [curvature_vector(j) for j in range(1, 7)]
    if rank(curvatures) != 6:
        raise ValueError("relative quadratic phase rank is not six")
    print("PASS: relative quadratic phase rank 6.")


if __name__ == "__main__":
    check()
