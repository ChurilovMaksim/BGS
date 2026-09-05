#!/usr/bin/env python3
"""Finite controls for general_hyperbolic_prime_spectra.md.

Integer matrix identities and unit tests use exact Python integers. Quantum
spectra use NumPy double precision and are explicitly not interval certificates.
The source's existence is not an execution certificate. A report is written
only if every requested check actually finishes successfully.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

Matrix = tuple[tuple[int, int], tuple[int, int]]
IDENTITY: Matrix = ((1, 0), (0, 1))


def mul(a: Matrix, b: Matrix, modulus: int | None = None) -> Matrix:
    values = tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                         for j in range(2)) for i in range(2))
    if modulus is not None:
        values = tuple(tuple(x % modulus for x in row) for row in values)
    return values  # type: ignore[return-value]


def power(a: Matrix, exponent: int, modulus: int | None = None) -> Matrix:
    if exponent < 0:
        raise ValueError('nonnegative exponent required')
    answer = IDENTITY
    while exponent:
        if exponent & 1:
            answer = mul(answer, a, modulus)
        a = mul(a, a, modulus)
        exponent //= 2
    return answer


def det(a: Matrix) -> int:
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def shifted(a: Matrix, scalar: int) -> Matrix:
    return ((a[0][0]+scalar, a[0][1]), (a[1][0], a[1][1]+scalar))


def inverse(a: Matrix) -> Matrix:
    if det(a) != 1:
        raise ValueError('determinant one required')
    return ((a[1][1], -a[0][1]), (-a[1][0], a[0][0]))


def is_prime(k: int) -> bool:
    return k >= 2 and all(k % p for p in range(2, math.isqrt(k)+1))


def design(trace: int, period: int) -> tuple[int, int]:
    if trace <= 2 or period <= 3 or not is_prime(period):
        raise ValueError('require trace>2 and an odd prime period>3')
    if (trace-2) % period == 0:
        raise ValueError('period must not divide trace-2')
    m = (period-1)//2
    u, v = 0, 1
    for _ in range(m):
        u, v = v, trace*v-u
    n = u+v
    residue = pow(trace-2, (period-1)//2, period)
    c = 1 if residue == 1 else -1
    assert residue in (1, period-1)
    assert n % 2 == 1 and (n-c) % (2*period) == 0
    assert n % period == c % period
    return n, c


def matrices(trace: int) -> list[Matrix]:
    a: Matrix = ((trace-1, trace-2), (1, 1))
    transforms: list[Matrix] = [IDENTITY, ((1, 1), (0, 1)), ((1, 0), (2, 1))]
    result = [mul(mul(p, a), inverse(p)) for p in transforms]
    if trace == 6:
        result += [((3, 2), (4, 3)), ((3, 4), (2, 3))]
    return result


def exact_checks() -> dict:
    rows = []
    for trace in range(3, 13):
        for k in (5, 7, 11, 13, 17, 23, 31):
            if (trace-2) % k == 0:
                continue
            n, c = design(trace, k)
            for a in matrices(trace):
                assert det(a) == 1 and a[0][0]+a[1][1] == trace
                left = shifted(power(a, k), -1)
                middle = mul(power(a, (k-1)//2), shifted(a, -1))
                right = tuple(tuple(n*x for x in row) for row in middle)
                assert left == right
                assert power(a, k, n) == IDENTITY
                for j in range(1, k):
                    aj = power(a, j, n)
                    assert math.gcd(det(shifted(aj, -1)), n) == 1
                    assert math.gcd(det(shifted(aj, 1)), n) == 1
                rows.append({'trace': trace, 'K': k, 'N': str(n), 'matrix': a,
                             'sign': c, 'uniform_parity': 'odd' if c == 1 else 'even',
                             'dimension': str((n-c)//2),
                             'root_multiplicity': str((n-c)//(2*k))})
    # A mixed split/nonsplit composite example, using Euler's criterion.
    assert 23*43 == design(4, 11)[0]
    assert pow(12, 11, 23) == 1
    assert pow(12, 21, 43) == 42
    # Negative control: this excluded design has a genuine nonunit determinant.
    bad: Matrix = ((6, 5), (1, 1))
    assert math.gcd(det(shifted(bad, -1)), 55) == 5
    try:
        design(7, 5)
    except ValueError:
        pass
    else:
        raise AssertionError('excluded period divisor was not rejected')
    return {'case_count': len(rows), 'cases': rows,
            'mixed_CRT_example': {'N': 989, 'factors': [23, 43],
                                  'discriminant': 12, 'quadratic_characters': [1, -1]},
            'excluded_design_negative_control': {'trace': 7, 'K': 5, 'N': 55,
                                                 'gcd_det_A_minus_I': 5}}


def finite_quantum_checks() -> list[dict]:
    import numpy as np

    def weyl(n: int, a: int, b: int, invariant: bool) -> np.ndarray:
        x = np.arange(n, dtype=np.int64)
        a0, b0 = a % n, b % n
        exponent = (a0*(x-b0*pow(2, -1, n))) % n
        refinement = a*b+(a+b if invariant else 0)
        values = ((-1)**(refinement % 2))*np.exp(2j*np.pi*exponent/n)
        answer = np.zeros((n, n), dtype=complex)
        answer[x, (x-b0) % n] = values
        return answer

    def parity_basis(n: int, sign: int) -> np.ndarray:
        d = (n-1)//2
        p = np.zeros((n, d+(sign == 1)), dtype=complex)
        start = 0
        if sign == 1:
            p[0, 0] = 1
            start = 1
        for j in range(1, d+1):
            p[j, j-1+start] = 1/math.sqrt(2)
            p[n-j, j-1+start] = sign/math.sqrt(2)
        return p

    def multiplicities(matrix: np.ndarray, k: int) -> tuple[list[int], float]:
        eigenvalues = np.linalg.eigvals(matrix)
        labels = np.rint(np.angle(eigenvalues)*k/(2*np.pi)).astype(int) % k
        roots = np.exp(2j*np.pi*labels/k)
        residual = float(np.max(abs(eigenvalues-roots)))
        assert residual < 3e-9
        return np.bincount(labels, minlength=k).tolist(), residual

    reports = []
    for trace, k in ((3, 5), (4, 5), (5, 5), (6, 5),
                     (3, 7), (4, 7), (6, 7)):
        n, c = design(trace, k)
        a = matrices(trace)[0]
        x = np.arange(n, dtype=np.int64)
        xx, yy = x[:, None], x[None, :]
        exponent = ((a[0][0]*xx*xx-2*xx*yy+a[1][1]*yy*yy)*pow(2, -1, n)) % n
        u = np.exp(2j*np.pi*exponent/n)/math.sqrt(n)
        unitarity = float(np.max(abs(u@u.conj().T-np.eye(n))))
        assert unitarity < 3e-11
        covariance_errors = []
        for v in ((1, 0), (0, 1), (1, 1), (2, -1)):
            av = (a[0][0]*v[0]+a[0][1]*v[1], a[1][0]*v[0]+a[1][1]*v[1])
            error = float(np.max(abs(u@weyl(n, *v, True)@u.conj().T-
                                     weyl(n, *av, True))))
            assert error < 3e-11
            covariance_errors.append(error)
        old_refinement_negative_control = None
        if trace == 3:
            v = (0, 1)
            av = (a[0][1], a[1][1])
            error = float(np.max(abs(u@weyl(n, *v, False)@u.conj().T-
                                     weyl(n, *av, False))))
            assert error > 1.9
            old_refinement_negative_control = error
        uk = np.linalg.matrix_power(u, k)
        scalar = np.trace(uk)/n
        scalar_error = float(np.max(abs(uk-scalar*np.eye(n))))
        assert scalar_error < 3e-10
        u *= np.exp(-1j*np.angle(scalar)/k)
        reflected_trace = np.sum(u[(-x) % n, x])
        character_label = int(np.rint(np.angle(reflected_trace)*k/(2*np.pi))) % k
        u *= np.exp(-2j*np.pi*character_label/k)
        worst_trace = 0.0
        current = np.eye(n, dtype=complex)
        for j in range(k):
            if j:
                current = current@u
            error_r = abs(np.sum(current[(-x) % n, x])-1)
            error_u = abs(np.trace(current)-(n if j == 0 else c))
            worst_trace = max(worst_trace, float(error_r), float(error_u))
        assert worst_trace < 3e-8
        base = (n-c)//k
        full, full_residual = multiplicities(u, k)
        assert full == [base+c]+[base]*(k-1)
        parity_reports = []
        for sign in (-1, 1):
            p = parity_basis(n, sign)
            block = p.conj().T@u@p
            observed, residual = multiplicities(block, k)
            expected = [base//2+(c+sign)//2]+[base//2]*(k-1)
            assert observed == expected
            parity_reports.append({'parity': 'even' if sign == 1 else 'odd',
                                   'dimension': block.shape[0],
                                   'root_multiplicities': observed,
                                   'eigenvalue_root_residual': residual})
        reports.append({'trace': trace, 'K': k, 'N': n, 'sign': c,
                        'unitarity_entry_error': unitarity,
                        'covariance_entry_errors': covariance_errors,
                        'old_refinement_negative_control': old_refinement_negative_control,
                        'power_scalar_entry_error': scalar_error,
                        'largest_trace_identity_error': worst_trace,
                        'full_root_multiplicities': full,
                        'full_eigenvalue_root_residual': full_residual,
                        'parity_spectra': parity_reports})
    return reports


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--exact-only', action='store_true')
    args = parser.parse_args()
    result = {'producer': Path(__file__).name,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python': platform.python_version(),
              'scope': 'Exact finite arithmetic and optional floating-point Weyl/spectral controls; not an asymptotic or external priority certificate.',
              'exact': exact_checks()}
    if not args.exact_only:
        import numpy as np
        result['numpy'] = np.__version__
        result['quantum_checks'] = finite_quantum_checks()
    result['status'] = 'PASS'
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
