"""Finite checks of an exact determinant route, not evidence of BGS.

No independence of the actual phases is assumed. Auxiliary exponents test
identities away from zero; the original tau is also checked at tiny N.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from fractions import Fraction
from decimal import Decimal, localcontext
from itertools import combinations, product
from math import comb
from pathlib import Path
import importlib.util
import json

import numpy as np

HERE = Path(__file__).resolve().parent


def frozen_matrices(n):
    path = HERE.parent/'algebraic-return/exact_coefficients.py'
    spec = importlib.util.spec_from_file_location('coefficients', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    coeff = module.frozen_coefficients()
    coeff.pop((0, 0))
    x = np.arange(n, dtype=np.int64)
    matrix = np.zeros((n, n), dtype=complex)
    for (a, b), (re, im) in coeff.items():
        phase = (b*(x+pow(2, -1, n)*a)) % n
        matrix[x, (x+a) % n] += complex(float(re), float(im))*np.exp(2j*np.pi*phase/n)
    assert np.linalg.norm(matrix-matrix.conj().T) < 1e-12
    phase = (-pow(8, -1, n)*(3*x[:, None]**2-2*x[:, None]*x[None, :]+3*x[None, :]**2)) % n
    cat = np.exp(2j*np.pi*phase/n)/np.sqrt(n)
    return (matrix+matrix.conj().T)/2, cat


def checks(n):
    a, m = frozen_matrices(n)
    eigenvalues, q = np.linalg.eigh(a)
    b = q.conj().T@m@q
    # The centering need not equal Tr(A)/N in small aliased dimensions;
    # determinant identities do not need that equality.
    subsets = []
    for k in range(n+1):
        row = []
        for indices in combinations(range(n), k):
            minor = np.linalg.det(b[np.ix_(indices, indices)]) if indices else 1+0j
            row.append((indices, sum(eigenvalues[list(indices)]), minor))
        subsets.append(row)
    errors = []
    for epsilon in (n*1e-80, 0.17, 2.4):
        u = np.exp(1j*epsilon*eigenvalues)[:, None]*b
        direct = np.poly(np.linalg.eigvals(u))
        expanded = np.array([(-1)**k*sum(minor*np.exp(1j*epsilon*frequency)
                                        for _, frequency, minor in row)
                             for k, row in enumerate(subsets)])
        cb = np.max(abs(direct-expanded))
        self_inverse = np.max(abs(expanded[::-1]-expanded[-1]*expanded.conj()))
        power = np.eye(n, dtype=complex)
        traces = [complex(n)]
        for _ in range(n):
            power = power@u
            traces.append(np.trace(power))
        newton = max(abs(k*expanded[k]+sum(expanded[k-j]*traces[j]
                                          for j in range(1, k+1))) for k in range(1, n+1))
        assert max(cb, self_inverse, newton) < 1e-9
        errors.append({'epsilon': epsilon,
                       'kick_below_floating_resolution': abs(epsilon) < 1e-15,
                       'Cauchy_Binet': float(cb),
                       'self_inversive': float(self_inverse), 'Newton': float(newton)})
    # Exact degree argument: the two-point grid in each independent phase
    # integrates differences of 0/1 subset characters. Floating evaluation
    # is an independent finite check, not a phase average of the fixed map.
    phase_mean = np.zeros(n+1)
    for signs in product((-1, 1), repeat=n):
        u = np.array(signs)[:, None]*b
        phase_mean += abs(np.poly(np.linalg.eigvals(u)))**2/2**n
    diagonal_sum = np.array([sum(abs(minor)**2 for _, _, minor in row) for row in subsets])
    grid_error = np.max(abs(phase_mean-diagonal_sum))
    assert grid_error < 1e-9
    return {'N': n, 'identity_errors': errors, 'phase_grid_error': float(grid_error),
            'independent_phase_mean_abs_coefficient_squared': diagonal_sum.tolist(),
            'CUE_mean_abs_coefficient_squared_each_k': 1,
            'scope': 'finite algebra checks only; auxiliary phase grid is a different ensemble'}


def subset_frequency_bound():
    f0 = Fraction(593, 500)
    rows = []
    for n in (41, 239, 1393, 10001):
        k = n//2
        count = comb(n, k)
        # All k-subset sums lie in [-k F0,k F0]. Either an exact collision
        # occurs or the smallest distinct-index pair separation is at most:
        bound = 2*k*f0/(count-1)
        horizon = n**10
        # sinc(x) >= 1-x^2/6 for real x. At least one subset character
        # has its interval-average modulus at least this lower bound.
        loss_bound = (horizon*bound)**2/6
        if n >= 239:
            assert loss_bound < Fraction(1, 10000)
        # Store useful exact rational values, avoiding gigantic C(N,k) text.
        def display(q):
            with localcontext() as ctx:
                ctx.prec = 14
                return format(Decimal(q.numerator)/Decimal(q.denominator), '.7E')
        rows.append({'N': n, 'k': k, 'subset_count_bits': count.bit_length(),
                     'frequency_gap_upper_display': display(bound),
                     'averaging_exponent_horizon': horizon,
                     'interval_character_modulus_loss_upper_display': display(loss_bound),
                     'loss_less_than_1e_minus_4_exact': loss_bound < Fraction(1, 10000)})
    return rows


if __name__ == '__main__':
    data = {'status': 'checks passed, BGS route not closed',
            'dense': [checks(n) for n in (5, 9)],
            'pigeonhole_exact_rational_evaluations': subset_frequency_bound(),
            'warning': 'Pigeonhole concerns uniform character control, not the weighted determinant sum.'}
    (HERE/'checks.json').write_text(json.dumps(data, indent=2)+'\n')
    for row in data['dense']:
        print(json.dumps({'N': row['N'], 'errors': row['identity_errors'],
                          'phase_grid_error': row['phase_grid_error']}))
    print('Exact rational subset-frequency scale checks: PASS')
