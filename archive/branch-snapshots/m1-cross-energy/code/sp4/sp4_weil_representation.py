"""M4a — Sp4 Weil representation infrastructure (RUN 103, started).

Membership checks verified: the Weyl element w = [[0,I],[-I,0]] and the
diagonal D = diag(u1, u2, u1^-1, u2^-1) are symplectic mod N.

The G0 test object (next session): the Hecke kernel
    <f_chi | T_D | f_psi>
for f_chi multiplicative characters of the two torus factors — the
rank-2 twisted Jacobi sum, the Sp_4 analogue of Theorem II.  The
Schrodinger model: functions on X = (Z/N)^2 with
    (omega(D) f)(x) = psi(mu(x)) f(D|_X^{-1} x),
mu(x) the quadratic form mu(x) = ((u1 - u1^{-1}) x1^2 +
(u2 - u2^{-1}) x2^2)/2 (the 4D analogue of the cat-map phase).

This file currently provides: Sp_4 membership, the generators
(w, U(t) unipotents, D diagonal), and the quadratic-form helper.
The Weil action itself is deferred to the next session (needs the
half-form corrections done carefully — the 2D cat map took several
correction rounds; see LESSON 80-E on eigenspace assertions).
"""

import numpy as np


def sp4_check(M, N):
    J = np.array([[0, 0, 1, 0], [0, 0, 0, 1],
                  [-1, 0, 0, 0], [0, -1, 0, 0]])
    return np.array_equal((M.T @ J @ M) % N, J % N)


def weyl_element(N):
    return np.array([[0, 0, 1, 0], [0, 0, 0, 1],
                     [-1, 0, 0, 0], [0, -1, 0, 0]])


def unipotent(t11, t12, t22, N):
    """U(t) = [[I2, t],[0, I2]] with t = [[t11,t12],[t12,t22]] symmetric."""
    return np.array([[1, 0, t11, t12],
                     [0, 1, t12, t22],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]) % N


def diagonal(u1, u2, N):
    return np.diag([u1, u2,
                    pow(u1, N - 2, N), pow(u2, N - 2, N)])


def quad_form_mu(u1, u2, N):
    """mu(x) coefficients: ((u_i - u_i^{-1})/2) x_i^2 with 1/2 = inv 2."""
    inv2 = pow(2, N - 2, N)
    c1 = ((u1 - pow(u1, N - 2, N)) % N) * inv2 % N
    c2 = ((u2 - pow(u2, N - 2, N)) % N) * inv2 % N
    return c1, c2


if __name__ == "__main__":
    N = 53
    assert sp4_check(weyl_element(N), N)
    assert sp4_check(diagonal(2, 3, N), N)
    assert sp4_check(unipotent(1, 0, 1, N), N)
    print("Sp4 membership: w, D, U(t) all verified at N = 53")
    print("mu coefficients for D = diag(2,3,...):",
          quad_form_mu(2, 3, N))
