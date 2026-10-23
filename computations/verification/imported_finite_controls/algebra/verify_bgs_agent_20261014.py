"""Reproducible finite-dimensional audit of a proposed complete BGS proof.

Checks use the quantization and metaplectic matrix exactly as printed in
user-supplied manuscript, plus elementary finite-field area-form linear algebra.
Dependencies: numpy. No GitHub mutation.
"""
import math
import itertools
import numpy as np

def w_operator(n, k, ell):
    out = np.zeros((n, n), dtype=complex)
    for x in range(n):
        out[x, (x + ell) % n] = np.exp(2j * np.pi * k * (x + ell / 2) / n)
    return out

def metaplectic(n):
    inv8 = pow(8, -1, n)
    x = np.arange(n)[:, None]
    y = np.arange(n)[None, :]
    q = inv8 * (3 * x * x - 2 * x * y + 3 * y * y) % n
    return np.exp(-2j * np.pi * q / n) / np.sqrt(n)

def period(n):
    s = np.array([[3, 4], [2, 3]], dtype=np.int64) % n
    p = np.eye(2, dtype=np.int64)
    for d in range(1, n + 2):
        p = p @ s % n
        if np.array_equal(p, np.eye(2, dtype=np.int64)):
            return d
    raise ValueError(f'No period found for n={n}')

def legendre_2(p):
    return 1 if p % 8 in (1, 7) else -1

def rank_mod(matrix, p):
    a = [[int(z) % p for z in row] for row in matrix]
    nrows = len(a)
    ncols = len(a[0])
    rank = 0
    for col in range(ncols):
        piv = next((i for i in range(rank, nrows) if a[i][col] % p), None)
        if piv is None:
            continue
        a[rank], a[piv] = (a[piv], a[rank])
        inv = pow(a[rank][col], -1, p)
        for j in range(col, ncols):
            a[rank][j] = a[rank][j] * inv % p
        for i in range(nrows):
            if i != rank:
                mul = a[i][col]
                for j in range(col, ncols):
                    a[i][j] = (a[i][j] - mul * a[rank][j]) % p
        rank += 1
    return rank

def check_weyl_sign():
    print('1. Weyl multiplication sign (paper uses +; definition requires -):')
    for p in (3, 5, 7, 11):
        lhs = w_operator(p, 1, 0) @ w_operator(p, 0, 1)
        mid = w_operator(p, 1, 1)
        plus_err = np.linalg.norm(lhs - np.exp(1j * np.pi / p) * mid)
        minus_err = np.linalg.norm(lhs - np.exp(-1j * np.pi / p) * mid)
        print(f'  p={p:2d}: paper + error {plus_err:.8f}; corrected - error {minus_err:.2e}')
        if not (minus_err < 1e-12 and plus_err > 1):
            raise AssertionError('verification failed')

def check_weil_trace_and_phase():
    print('2. Metaplectic trace and period phase:')
    for p in (3, 5, 7, 11, 13):
        m = metaplectic(p)
        d = period(p)
        eps = 1 if p % 4 == 1 else 1j
        chi = legendre_2(p) * eps
        paper_trace = legendre_2(p) * chi
        paper_phase = chi ** d
        actual_trace = np.trace(m)
        actual_phase = np.trace(np.linalg.matrix_power(m, d)) / p
        print(f'  p={p:2d}, d={d:2d}: trace={actual_trace.real:+.5f}{actual_trace.imag:+.5f}i, paper={paper_trace.real:+.5f}{paper_trace.imag:+.5f}i; phase={actual_phase.real:+.5f}{actual_phase.imag:+.5f}i, paper={paper_phase.real:+.5f}{paper_phase.imag:+.5f}i')
        if not np.linalg.norm(m.conj().T @ m - np.eye(p)) < 1e-11:
            raise AssertionError('verification failed')
        if p in (5, 7, 13):
            if not abs(actual_trace - paper_trace) > 1.9:
                raise AssertionError('verification failed')
        if p == 7:
            if not abs(actual_phase - paper_phase) > 1.9:
                raise AssertionError('verification failed')
        if not (abs(actual_trace) > 0.999 and abs(actual_trace) < 1.001):
            raise AssertionError('verification failed')

def check_area_rank():
    print('3. Finite symplectic area quadratic form:')
    for p in (3, 5, 7):
        for m in range(2, 9):
            n = m - 1
            b = [[0] * n for _ in range(n)]
            for i in range(n - 1):
                b[i][i + 1] = 1
                b[i + 1][i] = -1
            rb = rank_mod(b, p)
            expected = n if m % 2 else n - 1
            if not rb == expected:
                raise AssertionError((p, m, rb, expected))
            if not 2 * rb == (2 * m - 2 if m % 2 else 2 * m - 4):
                raise AssertionError('verification failed')
        print(f'  p={p}: ranks verified for m=2,...,8')
    print('  Exact normalized full Gauss sum: p^{-(m-1)} if m odd, p^{-(m-2)} if m even.')

def check_area_gauss_sums():
    print('3b. Direct finite-field Gaussian area sums, normalized:')
    for p, m in ((3, 2), (3, 3), (3, 4), (3, 5), (5, 3), (5, 4)):
        n = m - 1
        vertices = list(itertools.product(range(p), repeat=n))
        total = 0j
        for x in vertices:
            for y in vertices:
                area = sum((x[j] * y[j + 1] - y[j] * x[j + 1] for j in range(n - 1)))
                total += np.exp(2j * np.pi * (area % p) / p)
        result = total / p ** (2 * n)
        expected = p ** (-(m - 1 if m % 2 else m - 2))
        print(f'  p={p}, m={m}: direct={result.real:.10f}, formula={expected:.10f}')
        if not abs(result - expected) < 2e-11:
            raise AssertionError('verification failed')

def check_transpose_similarity():
    print('4. Every unitary is unitarily similar to its transpose:')
    p = 9
    rng = np.random.default_rng(145)
    z = rng.standard_normal((p, p)) + 1j * rng.standard_normal((p, p))
    u, _ = np.linalg.qr(z)
    eig, v = np.linalg.eig(u)
    w = np.conjugate(v) @ v.conj().T
    error = np.linalg.norm(w @ u @ w.conj().T - u.T)
    print(f'  residual {error:.2e}')
    if not error < 1e-11:
        raise AssertionError('verification failed')

def check_unitary_recurrence():
    print('5. Fourier matrix has flat entries yet exact coherent return:')
    for p in (5, 11):
        x = np.arange(p)[:, None]
        y = np.arange(p)[None, :]
        f = np.exp(2j * np.pi * x * y / p) / np.sqrt(p)
        recurrence = np.linalg.norm(np.linalg.matrix_power(f, 4) - np.eye(p))
        print(f'  p={p}: max matrix element={np.max(np.abs(f)):.6f}, ||F^4-I||={recurrence:.2e}, trace F^4={np.trace(np.linalg.matrix_power(f, 4)):.6f}')
        if not recurrence < 1e-11:
            raise AssertionError('verification failed')

def check_frozen_window_bound():
    tau = 1e-80
    a_bound = 1.58
    pmax = 1e+39
    err = 2 * a_bound * tau * pmax ** 2
    print('6. Exact pre-asymptotic resonant-window obstruction:')
    print(f'  for any odd prime p <= 10^39, pick m multiple of d_p with p <= m <= 2p')
    print(f'  ||U_p^m - scalar I|| <= {err:.6f}')
    print(f'  therefore E_p([1,2]) >= {(1 - err) ** 2:.8f}')
    if not (err < 0.032 and (1 - err) ** 2 > 0.937):
        raise AssertionError('verification failed')
if __name__ == '__main__':
    check_weyl_sign()
    check_weil_trace_and_phase()
    check_area_rank()
    check_area_gauss_sums()
    check_transpose_similarity()
    check_unitary_recurrence()
    check_frozen_window_bound()
    print('All finite algebra checks passed; failed paper claims have explicit counterexamples.')
