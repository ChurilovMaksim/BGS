"""Independent finite controls; proof of unbounded statements is in audit.md."""
import itertools
import json
import math
import platform
import time
from fractions import Fraction
import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp

def add(poly, key, value):
    poly[key] = sp.expand(poly.get(key, 0) + value)

def symbol():
    R = {0: sp.Integer(1), 1: sp.Rational(1, 2), -1: sp.Rational(1, 2), 7: sp.Rational(-1, 2), -7: sp.Rational(-1, 2), 6: sp.Rational(-1, 4), -6: sp.Rational(-1, 4), 8: sp.Rational(-1, 4), -8: sp.Rational(-1, 4)}
    out = {(7, 0): sp.Rational(1, 2), (-7, 0): sp.Rational(1, 2), (0, 0): sp.Rational(-1, 10)}
    for k, v in R.items():
        add(out, (k, 0), v / 10)
        add(out, (k + 1, 0), v / (200 * sp.I))
        add(out, (k - 1, 0), -v / (200 * sp.I))
        add(out, (k, 1), v * (-1) ** abs(k) * (-3 - 4 * sp.I) / 1000)
        add(out, (k, -1), v * (-1) ** abs(k) * (-3 + 4 * sp.I) / 1000)
    if not all((sp.expand(v - sp.conjugate(out.get((-k, -l), 0))) == 0 for (k, l), v in out.items())):
        raise RuntimeError('Exact/diagnostic check failed at source line 34')
    if not sum((v * R[-k] for k, v in R.items())) == sp.Rational(9, 4):
        raise RuntimeError('Exact/diagnostic check failed at source line 36')
    return out
FOURIER = symbol()

def actual_from_weyl(n):
    A = np.zeros((n, n), complex)
    inv2 = pow(2, -1, n)
    for (k, l), v in FOURIER.items():
        for j in range(n):
            A[j, (j + l) % n] += complex(v) * (-1) ** abs(k * l) * np.exp(2j * np.pi * (k * (j + inv2 * l) % n) / n)
    M = np.array([[np.exp(2j * np.pi * (-pow(8, -1, n) * (3 * j * j - 2 * j * k + 3 * k * k) % n) / n) for k in range(n)] for j in range(n)]) / np.sqrt(n)
    if not np.linalg.norm(A - A.conj().T) < 1e-12:
        raise RuntimeError('Exact/diagnostic check failed at source line 54')
    if not np.linalg.norm(M.conj().T @ M - np.eye(n)) < 1e-12:
        raise RuntimeError('Exact/diagnostic check failed at source line 55')
    return (A, M)

def lift_one(a, slot, m):
    n = len(a)
    return np.kron(np.eye(n ** slot), np.kron(a, np.eye(n ** (m - slot - 1))))

def tensor_control(n, m):
    A, M = actual_from_weyl(n)
    k = (n - 1) // 2
    vertices = ((n + 1) // 2 + np.arange(n)) % n
    phi = np.full(n, -k / n)
    phi[vertices[:k]] += 1
    D = np.diag(phi)
    t2 = float(np.dot(phi, phi))
    tuples = np.array(list(itertools.product(range(n), repeat=m)))
    dim = n ** m
    vals = phi[tuples]
    X = np.diag((np.sum(vals, axis=1) ** 2 - np.sum(vals * vals, axis=1)) / 2)
    index = {tuple(x): j for j, x in enumerate(tuples)}
    P = np.zeros((dim, dim))
    for r, s in itertools.combinations(range(m), 2):
        for col, x in enumerate(tuples):
            y = x.copy()
            y[r], y[s] = (x[s], x[r])
            P[index[tuple(y)], col] += 1 / (4 * n)
        P -= np.eye(dim) / (4 * n * n)
    Y = X - P
    norm2 = np.vdot(Y, Y).real
    expected_norm = math.comb(m, 2) * n ** (m - 2) * (n * n - 1) * (n * n - 2) / (16 * n * n)
    max_invariant = 0.0
    for p in itertools.permutations(range(m)):
        rows = [index[tuple(x[list(p)])] for x in tuples]
        max_invariant = max(max_invariant, abs(Y[rows, np.arange(dim)].sum()))
    counts = np.array([np.bincount(x, minlength=n) for x in tuples])
    balanced = (counts[:, None, :] == counts[None, :, :]).all(axis=2)
    Mt = np.ones((1, 1), complex)
    for _ in range(m):
        Mt = np.kron(Mt, M)
    W = balanced * (Mt.conj().T @ Y @ Mt)
    At = sum((lift_one(A, s, m) for s in range(m)))
    hy, hw = (At @ Y - Y @ At, At @ W - W @ At)
    q = np.vdot(W, W).real / norm2
    e = np.vdot(hy, hy).real / norm2
    e2 = np.vdot(hw, hw).real / norm2
    w = math.cos(7 * math.pi / (2 * n)) ** 4 * math.sin(math.pi / (2 * n)) ** 4 / 2500
    q_formula = (n * n - 3 * n + 3) / (3 * n * (n * n - 2))
    e_formula = 16 * n * w / (n * n - 2)
    B = M.conj().T @ D @ M
    F = abs(B[0, :]) ** 2
    F[0] = 0
    EF = np.sum((F - np.roll(F, 1)) ** 2)
    off = A - np.diag(np.diag(A))
    e2_formula = 32 * n * n * np.vdot(off, off).real * EF / ((n * n - 1) * (n * n - 2))
    if not abs(norm2 - expected_norm) < 1e-09:
        raise RuntimeError('Exact/diagnostic check failed at source line 112')
    if not max_invariant < 1e-11:
        raise RuntimeError('Exact/diagnostic check failed at source line 113')
    if not abs(q - q_formula) < 1e-12:
        raise RuntimeError('Exact/diagnostic check failed at source line 114')
    if not abs(e - e_formula) < 1e-12:
        raise RuntimeError('Exact/diagnostic check failed at source line 115')
    if not abs(e2 - e2_formula) < 1e-12:
        raise RuntimeError('Exact/diagnostic check failed at source line 116')
    if n >= 19:
        if not abs(np.vdot(off, off).real - 9 * n / 80000) < 1e-12:
            raise RuntimeError('Exact/diagnostic check failed at source line 118')
        if not 0 < e_formula < n ** (-5) / 20:
            raise RuntimeError('Exact/diagnostic check failed at source line 119')
        lower = (math.sqrt(q_formula) - 10 ** (-80) * n * math.sqrt(e_formula)) / math.sqrt(e_formula + n ** (-5))
        if not lower >= n * n / 4:
            raise RuntimeError('Exact/diagnostic check failed at source line 121')
    else:
        lower = None
    times = []
    cyclic = [index[tuple(np.roll(x, 1))] for x in tuples]
    for t in [0.0, 0.137]:
        U = expm(1j * t * n * A) @ M
        Ut = np.ones((1, 1), complex)
        for _ in range(m):
            Ut = np.kron(Ut, U)
        image = Ut @ Y @ Ut.conj().T
        actual = np.vdot(Y, image[np.ix_(cyclic, cyclic)]) / norm2
        a = np.trace(D @ U @ D @ U.conj().T) / t2
        formula = ((n * n - 1) * a * a - 1) / (n * n - 2)
        if not abs(actual - formula) < 1e-12:
            raise RuntimeError('Exact/diagnostic check failed at source line 135')
        if not abs(a.imag) < 1e-12:
            raise RuntimeError('Exact/diagnostic check failed at source line 136')
        duhamel = np.linalg.norm(balanced * (Ut.conj().T @ Y @ Ut) - W) / math.sqrt(norm2)
        if not duhamel <= abs(t) * n * math.sqrt(e) + 1e-13:
            raise RuntimeError('Exact/diagnostic check failed at source line 138')
        times.append(dict(t=t, cyclic=float(actual.real), residual=float(abs(actual - formula))))
    return dict(N=n, m=m, dimension=dim, invariant_residual=float(max_invariant), source_ratio=float(q), energy=float(e), second_frame=float(e2), source_inverse_lower_bound=lower, times=times)

def scalar_controls():
    controls = []
    for n in range(3, 202, 2):
        k = (n - 1) // 2
        counts = np.convolve(np.ones(k, dtype=np.int64), np.ones(k, dtype=np.int64))
        E = int(np.dot(counts, counts))
        if not E == (2 * k ** 3 + k) // 3:
            raise RuntimeError('Exact/diagnostic check failed at source line 151')
        t2 = Fraction(n * n - 1, 4 * n)
        t4 = Fraction(E, n * n) - Fraction(k ** 4, n ** 3)
        q = (t4 - t2 * t2 / Fraction(n * n - 1)) / (t2 * t2 * (1 - Fraction(1, n * n - 1)))
        if not q == Fraction(n * n - 3 * n + 3, 3 * n * (n * n - 2)):
            raise RuntimeError('Exact/diagnostic check failed at source line 155')
        if n >= 5:
            if not q >= Fraction(1, 6 * n):
                raise RuntimeError('Exact/diagnostic check failed at source line 157')
        controls.append(n)
    corr_controls = []
    for n in [3, 5, 7, 19, 21, 35, 49, 101, 1001]:
        k = (n - 1) // 2
        phi = np.full(n, -k / n)
        phi[:k] += 1
        power = abs(np.fft.fft(phi) / n) ** 2
        F = power[pow(4, -1, n) * np.arange(n) % n]
        F[0] = 0
        EF = float(np.sum((F - np.roll(F, 1)) ** 2))
        corr = float(np.dot(F, np.roll(F, 1)))
        theta = 2 * np.pi * pow(4, -1, n) / n
        S = k / np.sin(theta / 2) ** 2 - np.sin(k * theta) * np.cos(theta / 2) / (2 * np.sin(theta / 2) ** 3)
        corr_formula = S / n ** 3 - 2 * k * k * np.sin(k * theta / 2) ** 2 / (n ** 4 * np.sin(theta / 2) ** 2)
        if not abs(corr - corr_formula) < 1e-12:
            raise RuntimeError('Exact/diagnostic check failed at source line 172')
        if not 0 <= corr <= 3 / n ** 2:
            raise RuntimeError('Exact/diagnostic check failed at source line 173')
        corr_controls.append(dict(N=n, EF=EF, correlation=corr, formula=float(corr_formula)))
    return dict(exact_fraction_dimensions=controls, correlation_controls=corr_controls)

def run_all():
    started = time.perf_counter()
    out = dict(software=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, sympy=sp.__version__), scope='Exact Gaussian-rational Fourier symbol and Fraction scalar identities; complex128 tensor diagnostics.', tensors=[tensor_control(n, m) for n, m in [(3, 2), (3, 5), (5, 3), (7, 2), (19, 2), (21, 2)]], scalar=scalar_controls())
    out['runtime_seconds'] = time.perf_counter() - started
    return out
