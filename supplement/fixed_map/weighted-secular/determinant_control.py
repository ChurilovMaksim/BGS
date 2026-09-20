"""Exact controls and finite checks for the determinant-ratio route.

The counterexample is an abstract deleted clock, not the frozen Anosov
quantization. Polynomial identities use integer/rational arithmetic.
"""
from fractions import Fraction
from itertools import combinations
import json
from math import factorial
from pathlib import Path
import numpy as np
from weighted_probe import model

HERE = Path(__file__).resolve().parent


def exact_deleted_clock(n):
    # (1-z)P(z)=1-z^(N+1), P(z)=sum_(k=0)^N z^k.
    coefficients = [1]*(n+1)
    product = [0]*(n+2)
    for k, c in enumerate(coefficients):
        product[k] += c
        product[k+1] -= c
    assert product == [1]+[0]*n+[-1]
    # Newton recursion reconstructs every trace up to four periods exactly.
    traces = [n]
    for m in range(1, 4*(n+1)+1):
        if m <= n:
            value = -m*coefficients[m]-sum(coefficients[m-j]*traces[j] for j in range(1, m))
        else:
            value = -sum(coefficients[k]*traces[m-k] for k in range(1, n+1))
        traces.append(value)
        assert value == (n if m % (n+1) == 0 else -1)
    # Rational generating-function check: summing the trace squares over
    # one repeated period gives r/(1-r)+(N^2-1)r^(N+1)/(1-r^(N+1)).
    r = Fraction(2, 3)
    by_period = sum(Fraction(traces[m]**2)*r**m for m in range(1, n+2))/(1-r**(n+1))
    closed = r/(1-r)+(n*n-1)*r**(n+1)/(1-r**(n+1))
    assert by_period == closed
    return {'N': n, 'integer_polynomial_and_Newton_checks': 'passed',
            'rational_Abel_identity': 'passed'}


def ratio_and_abel(n, epsilon):
    energies, b = model(n)
    u = np.exp(1j*epsilon*energies)[:, None]*b
    eigenvalues = np.linalg.eigvals(u)
    s = 1.0
    r = np.exp(-s/n)
    # Mixed derivative of the ratio is computed using matrix resolvents,
    # independently of the eigenvalue-based infinite geometric sum.
    quadrature_count = 256*n
    total = 0.
    for theta in 2*np.pi*np.arange(quadrature_count)/quadrature_count:
        z = np.exp(1j*theta)
        h = np.trace(z*u@np.linalg.inv(np.eye(n)-r*z*u))
        total += abs(h/n)**2/quadrature_count
    liouville = eigenvalues[:, None]*eigenvalues.conj()[None, :]
    exact_abel = float(np.real(np.sum(r*r*liouville/(1-r*r*liouville)))/n**2)
    error = abs(r*r*total-exact_abel)
    assert error < 2e-12
    return {'N': n, 'auxiliary_epsilon': epsilon, 's': s,
            'resolvent_quadrature': total, 'exact_geometric_Abel_sum': exact_abel,
            'identity_error': error,
            'scope': 'floating identity check; not a trace comparison'}


def limiting_control():
    rows = []
    for n in [31, 127, 511, 2047, 8191]:
        for s in [0.5, 1.0, 2.0]:
            t = 2*s/n
            actual = (1/np.expm1(t)+(n*n-1)/np.expm1(t*(n+1)))/n**2
            clock_limit = 1/np.expm1(2*s)
            cue_limit = -np.expm1(-2*s)/(4*s*s)
            rows.append({'N': n, 's': s, 'clock_Abel': float(actual),
                         'clock_limit': float(clock_limit), 'CUE_limit': float(cue_limit)})
    return rows


def cue_ratio_quadrature():
    # Independent Weyl-density quadrature for the finite CUE ratio formula.
    # Low dimensions only; this checks normalization/conjugation, not BGS.
    a, b, c, d = 0.2+0.04j, 0.3-0.02j, 0.4+0.03j, 0.1-0.01j
    rows = []
    for n, count in [(1, 64), (2, 64), (3, 40)]:
        indices = np.indices((count,)*n).reshape(n, -1)
        roots = np.exp(2j*np.pi*indices/count)
        density = np.ones(roots.shape[1])/factorial(n)
        for i, j in combinations(range(n), 2):
            density *= abs(roots[i]-roots[j])**2
        observable = np.prod((1-c*roots)/(1-a*roots), axis=0)*np.prod(
            (1-d*roots.conj())/(1-b*roots.conj()), axis=0)
        quadrature = np.mean(density*observable)
        reference = 1+(a-c)*(b-d)/(1-a*b)*sum((c*d)**q for q in range(n))
        error = float(abs(quadrature-reference))
        assert abs(np.mean(density)-1) < 1e-13
        assert error < 1e-12
        rows.append({'N': n, 'grid_per_angle': count, 'formula_error': error})
    return rows


if __name__ == '__main__':
    result = {'exact_controls': [exact_deleted_clock(n) for n in [2, 3, 9, 31, 127]],
              'ratio_checks': [ratio_and_abel(n, e) for n, e in [(5, 0.17), (9, 2.4)]],
              'finite_CUE_ratio_checks': cue_ratio_quadrature(),
              'limiting_control': limiting_control()}
    (HERE/'determinant_control.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'exact_controls': result['exact_controls'], 'ratio_checks': result['ratio_checks'],
                      'finite_CUE_ratio_checks': result['finite_CUE_ratio_checks']}))
