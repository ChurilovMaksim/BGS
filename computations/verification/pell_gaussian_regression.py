#!/usr/bin/env python3
"""Exact Pell arithmetic and independent numerical odd-observable checks.

These execution checks do not prove microscopic BGS or the general limit.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import mpmath as mp
import numpy as np
import sympy as sp


def pell(k: int) -> tuple[int, int]:
    n, f = 1, 0
    for _ in range(k):
        n, f = n+2*f, n+f
    return n, f


def design(k: int) -> tuple[int, int, int, list[int]]:
    if k < 3 or k % 2 == 0 or not sp.isprime(k):
        raise ValueError('K must be an odd prime')
    n, f = pell(k)
    assert n*n-2*f*f == -1
    s = pow(f, -1, n)
    assert s*s % n == 2
    h = (3+2*s) % n
    powers = [pow(h, j, n) for j in range(k)]
    assert pow(h, k, n) == 1 and len(set(powers)) == k
    assert all(math.gcd(x-1, n) == 1 for x in powers[1:])
    assert all(math.gcd(x+1, n) == 1 for x in powers)
    assert (n-1) % (2*k) == 0
    return n, f, h, powers


def block(k: int, sector: int) -> np.ndarray:
    """Reference assembly of the scaled odd cosine-observable block."""
    n, f, _h, powers = design(k)
    dim = (n-1)//(2*k)
    if dim > 2000:
        raise ValueError('reference dense assembler is limited to dimension 2000')
    index = np.full(n, -1, dtype=np.int64)
    value = np.zeros(n, dtype=complex)
    orbit = 0
    for representative in range(1, n):
        if index[representative] >= 0:
            continue
        for exponent, h in enumerate(powers):
            x = representative*h % n
            z = np.exp(-2j*np.pi*sector*exponent/k)/math.sqrt(2*k)
            assert index[x] < 0 and index[-x % n] < 0
            index[x], value[x] = orbit, z
            index[-x % n], value[-x % n] = orbit, -z
        orbit += 1
    assert orbit == dim
    x = np.arange(2, n, dtype=np.int64)
    q = (-f) % n
    phase = np.exp(2j*np.pi*((q*(x-pow(2, -1, n))) % n)/n)
    m = np.zeros((dim, dim), dtype=complex)
    np.add.at(m, (index[x], index[x-1]), value[x].conj()*value[x-1]*phase)
    assert np.max(np.abs(m-m.conj().T)) < 2e-12
    return math.sqrt(k/2)*(m+m.conj().T)


def phase_data(k: int) -> dict:
    n, f, _h, powers = design(k)
    mp.mp.dps = 70
    lam = 3+2*mp.sqrt(2)
    terms = []
    for d in range(1, (k+1)//2):
        pd = pell(2*d)[1]
        assert (-f*(powers[d]-pow(powers[d], -1, n))+2*pd) % n == 0
        terms.append(4*mp.pi*mp.mpf(pd)/n)
    l1 = 2*sum(abs(mp.exp(1j*t)-1) for t in terms)
    bound = 2*mp.sqrt(2)*mp.pi/(1-lam**(-k))
    assert l1 <= bound and bound < 9
    sk = (1+2*sum(mp.cos(t) for t in terms))/k
    central4 = mp.mpf(n)/(n-1)*(2+sk-mp.mpf(3)/(2*k))
    return {'K':k, 'N':str(n), 'F':str(f), 'phase_l1':float(l1),
            'phase_bound':float(bound), 'S_K':float(sk),
            'central_fourth_moment':float(central4),
            'fourth_remainder_bound':float(mp.mpf(8)*k**3/(n-1)),
            'fourth_cutoff_valid':bool(lam**(mp.mpf(k)/4)*(1-lam**(-k))**2 > 64)}


def constant() -> dict:
    mp.mp.dps = 70
    lam = 3+2*mp.sqrt(2)
    a = 4*mp.pi/(mp.sqrt(2)*(1+mp.sqrt(2)))
    j = 30
    value = mp.mpf(3)/2+2*sum(1-mp.cos(a*lam**(-ell)) for ell in range(j))
    tail = a*a*lam**(-2*j)/(1-lam**(-2))
    return {'gamma_decimal':mp.nstr(value, 60), 'terms':j,
            'analytic_tail_bound':mp.nstr(tail, 10),
            'rounding_scope':'70-decimal arithmetic; analytic tail is bounded separately, not an interval rounding certificate'}


def report() -> dict:
    out = {'producer':'computations/verification/pell_gaussian_regression.py',
           'scope':'Exact integer Pell/unit checks and numerical finite odd observable blocks; not microscopic BGS or a formal proof of the general limit.',
           'constant':constant(), 'spectral_checks':[], 'phase_checks':[]}
    for k in (3, 5, 7, 11):
        n, _f, _h, _powers = design(k)
        p = phase_data(k)
        for j in sorted({0, 1, k-1}):
            x = block(k, j)
            eigenvalues = np.linalg.eigvalsh(x)
            moments = {str(m):float(np.mean(eigenvalues**m)) for m in (1,2,3,4,6)}
            x2 = x@x
            assert abs(moments['2']-float(np.trace(x2).real/len(x))) < 1e-10
            assert abs(moments['4']-float(np.vdot(x2,x2).real/len(x))) < 1e-9
            odd_bound = 2**1.5*k**1.5/(n-1)
            assert abs(moments['1']) <= odd_bound+1e-10
            if p['fourth_cutoff_valid']:
                assert abs(moments['4']-p['central_fourth_moment']) <= p['fourth_remainder_bound']+1e-10
            out['spectral_checks'].append({'K':k,'N':n,'sector':j,'dimension':len(x),
                                          'factorization':{str(a):int(b) for a,b in sp.factorint(n).items()},
                                          'moments':moments})
    for k in (3,5,7,11,13,17,19,23,31,47,101,251,503):
        out['phase_checks'].append(phase_data(k))
    return out


def figure(data: dict, destination: Path) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    rows = [r for r in data['phase_checks'] if r['K'] >= 17]
    k = np.asarray([r['K'] for r in rows])
    center = np.asarray([r['central_fourth_moment'] for r in rows])
    error = np.asarray([r['fourth_remainder_bound'] for r in rows])
    gamma = float(data['constant']['gamma_decimal'])
    fig, ax = plt.subplots(figsize=(7.6,4.6))
    ax.errorbar(k, center, yerr=error, fmt='o', capsize=3,
                label='Central word sum, rigorous noncentral bound')
    curve = np.geomspace(k[0], k[-1], 250)
    ax.plot(curve, 3-gamma/curve, label=r'$3-\gamma/K$')
    ax.axhline(3, linestyle='--', label='Gaussian fourth moment')
    ax.set_xscale('log')
    ax.set_xlabel('Odd prime period K')
    ax.set_ylabel('Normalized fourth moment')
    ax.set_title('Pell-period cosine-observable blocks')
    ax.legend(loc='lower right', fontsize=8)
    ax.grid(alpha=.2)
    fig.tight_layout()
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, dpi=170)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--figure', type=Path)
    args = parser.parse_args()
    data = report()
    text = json.dumps(data, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')
    if args.figure:
        figure(data, args.figure)


if __name__ == '__main__':
    main()
