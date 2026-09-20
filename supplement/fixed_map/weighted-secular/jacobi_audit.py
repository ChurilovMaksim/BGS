"""Independent trigonometric/Jacobi assembly of the frozen raw generator.

For odd N coprime to 7 the off-diagonal r factor has exactly one zero,
so reordering and a phase gauge give an irreducible real Jacobi matrix.
This certifies neither simplicity nor statistics of exp(i epsilon A) M.
"""
import json
from math import gcd
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal
from weighted_probe import model, principal_minors, close_pairs

HERE = Path(__file__).resolve().parent


def independent_model(n):
    assert n % 2 and gcd(n, 7) == 1
    x = np.arange(n)
    angle = 2*np.pi*x/n
    r = (1-np.cos(7*angle))*(1+np.cos(angle))
    diagonal = np.cos(7*angle)+r/10+r*np.sin(angle)/100-0.1
    midpoint = (x+(n+1)//2) % n
    angle_mid = 2*np.pi*midpoint/n
    positive = (1-np.cos(7*angle_mid))*(1+np.cos(angle_mid))/200
    order = ((n+1)//2+x) % n
    assert positive[order[-1]] == 0.
    off = positive[order[:-1]]
    assert off.min() > 0.
    energy, real_vectors = eigh_tridiagonal(diagonal[order], off, lapack_driver='stev')
    gauge = ((-3+4j)/5)**x
    vectors = np.empty((n, n), complex)
    vectors[order, :] = gauge[:, None]*real_vectors
    # Root-of-unity table: direct modular Gaussian kernel, no reuse of
    # the coefficient builder or its matrix assembly.
    roots = np.exp(2j*np.pi*np.arange(n)/n)/np.sqrt(n)
    inverse8 = pow(8, -1, n)
    m = np.array([[roots[(-inverse8*(3*i*i-2*i*j+3*j*j)) % n]
                   for j in range(n)] for i in range(n)])
    return energy, vectors.conj().T@m@vectors


def audit(n):
    a, b = model(n)
    a2, b2 = independent_model(n)
    f, w = principal_minors(a, b, n//2)
    f2, w2 = principal_minors(a2, b2, n//2)
    # The spectrum is simple in both computations; principal minors are
    # invariant under arbitrary phases chosen for generator eigenvectors.
    energy_error = float(np.max(abs(a-a2)))
    frequency_error = float(np.max(abs(f-f2)))
    weight_error = float(np.max(abs(w-w2)))
    assert energy_error < 1e-12
    assert frequency_error < 2e-11
    assert weight_error < 1e-9
    comparisons = []
    for t in [0., 1., 100.]:
        rows = close_pairs(f, w*np.exp(1j*t*n*f), [1/n, 1/n**2], control_count=0)
        rows2 = close_pairs(f2, w2*np.exp(1j*t*n*f2), [1/n, 1/n**2], control_count=0)
        for r, s in zip(rows, rows2):
            assert r['unordered_close_pairs'] == s['unordered_close_pairs']
            error = abs(r['signed_offdiagonal_sum']-s['signed_offdiagonal_sum'])
            assert error < 2e-7
            comparisons.append({'t': t, 'width': r['width'], 'signed_sum_error': error,
                                'pair_count_agrees': True})
    result = {'N': n, 'generator_eigenvalue_error': energy_error,
              'subset_frequency_error': frequency_error,
              'principal_minor_error': weight_error, 'windows': comparisons,
              'scope': 'two floating implementations; no interval or asymptotic certificate'}
    (HERE/f'jacobi_N{n}.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    for n in [15, 19, 23]:
        audit(n)
