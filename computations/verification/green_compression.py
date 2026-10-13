#!/usr/bin/env python3
"""Bounded algebraic controls for TRACE-077; not an asymptotic proof.

Exact arithmetic: SymPy rationals. Numerical diagnostics: complex128.
No Monte Carlo probability or actual-map trajectory claim. Run with one BLAS
thread; dimensions <=96 and four feedback steps, memory <1 GiB, timeout 90 s.
"""
from __future__ import annotations

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
import json
from pathlib import Path
import numpy as np
import sympy as sp


def exact_controls():
    n = 5
    one = sp.ones(n) / n
    cycle = sp.zeros(n)
    swap = sp.eye(n)
    for i in range(n):
        cycle[i, (i + 1) % n] = 1
    swap[0, 0] = swap[1, 1] = 0
    swap[0, 1] = swap[1, 0] = 1
    p = sp.Rational(4, 5) * one + cycle / 8 + swap * sp.Rational(3, 40)
    assert p * p.T != p.T * p  # deliberately nonnormal, not only nonsymmetric
    g = (sp.eye(n) - p + one).inv() - one
    m = g - sp.eye(n) + one
    cases = 0
    for retained in [[0, 2, 4], [1, 3], [4], list(range(n))]:
        deleted = [i for i in range(n) if i not in retained]
        u = len(retained)
        pc = p.extract(retained, retained)
        if deleted:
            pc += p.extract(retained, deleted) * (sp.eye(len(deleted)) - p.extract(deleted, deleted)).inv() * p.extract(deleted, retained)
        j = sp.ones(u) / u
        q = sp.eye(u) - j
        gc = (sp.eye(u) - pc + j).inv() - j
        assert gc == q * g.extract(retained, retained) * q
        assert gc - q == q * m.extract(retained, retained) * q
        if u == 3:
            assert gc != g.extract(retained, retained)  # reject missing centering
        cases += 1
    h = sp.Matrix([[1, sp.Rational(2, 7)], [sp.Rational(-1, 9), 1]])
    x = sp.Matrix([[sp.Rational(1, 31), sp.Rational(-1, 23)], [sp.Rational(1, 37), 0]])
    hp = (h.inv() - x).inv()
    assert h*x != x*h
    assert hp == h + h*x*h + h*x*h*x*hp
    assert hp != h + h*x*h + h*x*x*h*hp  # reject interchanged interior factors
    return {'nonnormal_compressions': cases, 'ordered_resolvent': 'exact', 'negative_controls_rejected': 2}


def green(p):
    n = len(p)
    j = np.ones((n, n)) / n
    return np.linalg.inv(np.eye(n) - p + j) - j, np.eye(n) - j


def numerical_controls():
    n = 96
    ids = list(range(n))
    ii = np.arange(n)
    s = np.exp(2j*np.pi*np.outer(ii, ii)/n) / np.sqrt(n)
    angle = .09
    r = np.eye(n)
    for i in range(0, n, 2):
        r[i:i+2, i:i+2] = [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    s = s @ r
    g, q = green(abs(s)**2)
    initial = g-q
    z = np.zeros((n, n), complex)
    drift = np.zeros_like(z)
    rows = []
    for theta in [.31, 1.07, 2.19, 4.03]:
        p = abs(s)**2
        delta = float(p.max())
        assert delta <= 1/32
        port = int(np.argmax(np.sum(p*p, axis=0)))  # depends on current past
        keep = [i for i in range(len(s)) if i != port]
        a = s[port, port]
        c, b = s[keep, port], s[port, keep]
        aa = s[np.ix_(keep, keep)]
        pc = p[np.ix_(keep, keep)] + np.outer(abs(c)**2, abs(b)**2)/(1-abs(a)**2)
        gc, qu = green(pc)
        w = np.exp(1j*theta)
        sn = aa + np.outer(c, b)*w/(1-a*w)
        gn, _ = green(abs(sn)**2)
        xi = abs(sn)**2-pc
        linear = gc@xi@gc
        rem = gc@xi@gc@xi@gn
        inv_error = float(np.linalg.norm(gn-gc-linear-rem, 2))
        deleted_label = ids[port]
        ids = [ids[i] for i in keep]
        z[np.ix_(ids, ids)] += linear
        drift[np.ix_(ids, ids)] += rem
        embedded_q = np.zeros((n, n))
        embedded_q[np.ix_(ids, ids)] = qu
        full_m = np.zeros((n, n), complex)
        full_m[np.ix_(ids, ids)] = gn-qu
        tel_error = float(np.linalg.norm(full_m-embedded_q@(initial+z+drift)@embedded_q, 2))
        assert inv_error < 2e-12 and tel_error < 2e-12
        assert np.linalg.norm(xi, 2) <= 8*delta
        assert np.linalg.norm(linear, 2) <= 18*delta
        assert np.linalg.norm(rem, 2) <= 432*delta**2
        rows.append({'retained': len(ids), 'deleted_original_label': deleted_label,
                     'old_delta': delta, 'inverse_residual_op': inv_error, 'telescoping_residual_op': tel_error})
        s = sn
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = {'claim': 'BGS-TRACE-077', 'exact': exact_controls(), 'numerical': numerical_controls(),
              'non_claim': 'Finite controls do not prove probability bounds, early entry survival or BGS.'}
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
