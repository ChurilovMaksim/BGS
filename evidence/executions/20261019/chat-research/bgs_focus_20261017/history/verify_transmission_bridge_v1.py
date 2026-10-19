#!/usr/bin/env python3
"""Exact finite independent checks; not an asymptotic proof certificate."""
from __future__ import annotations

import json
from math import comb
import platform
import sys

import sympy as s


def zero(x):
    assert s.cancel(s.expand_complex(x)) == 0, x


def eq(a, b):
    zero(a - b)


def abs2(x):
    return s.cancel(x * s.conjugate(x))


def rat_residue(expr, w, p):
    """Rational Taylor division at an EXACT rational pole."""
    n, d = s.fraction(s.cancel(expr))
    pn, pd = s.Poly(n, w).shift(p), s.Poly(d, w).shift(p)
    order = 0
    while pd.nth(order) == 0:
        order += 1
    if order == 0:
        return s.S.Zero
    coeff = []
    for k in range(order):
        val = pn.nth(k) - sum(pd.nth(order+j) * coeff[k-j]
                             for j in range(1, k+1))
        coeff.append(s.cancel(val / pd.nth(order)))
    return coeff[-1]


def kernel_checks():
    w, z, x = s.symbols('w z x')
    checks = 0
    for st, rr in [(s.Rational(3, 5), s.Rational(4, 5)),
                   (s.Rational(5, 13), s.Rational(12, 13))]:
        t = st**2
        y = t*w / (2*w-rr*(w*w+1))
        # Independent 2x2 closed-eigenvector weights, integrated in phase
        # difference. Their interior pole differs from the feedback pole.
        nz2 = rr**2*(2-w-1/w)/(4-rr**2*(2+w+1/w))
        for k in range(1, 9):
            reference = s.cancel(st**k * s.legendre(k-1, 1/st) / 2**k)
            direct = rat_residue(y**k/w, w, (1-st)/rr)
            eq(direct, reference)
            poly = s.Poly(s.expand(((1+z)*(1-z)**k
                                   +(1-z)*(1+z)**k)/2**(k+1)), z)
            assert all(power[0] % 2 == 0 for power, _ in poly.terms())
            val = sum(coef*nz2**(power[0]//2)
                      for power, coef in poly.terms())
            eigen_average = (rat_residue(val/w, w, s.S.Zero)
                             +rat_residue(val/w, w, (1-st)/(1+st)))
            eq(eigen_average, reference)
            checks += 2
    for k in range(1, 17):
        expr = s.cancel(2*x*x**k*s.legendre(k-1, 1/x)/2**k)
        eq(s.integrate(expr, (x, 0, 1)), s.Rational(2, (k+1)*(k+2)))
        checks += 1
    # Direct density pushforward and its uniform transmission mixture.
    y, t, h = s.symbols('y t h', positive=True)
    # beta(3/2,1/2)=pi/2: substitute t=h*u to verify the Abel integral.
    u = s.symbols('u', positive=True)
    eq(s.integrate(s.sqrt(u)/s.sqrt(1-u), (u, 0, 1)), s.pi/2)
    eq((4*y*(1-y))/(2*y), 2*(1-y))
    checks += 2
    return {"exact_checks": checks, "kernel_and_eigenvector_powers": [1, 8],
            "uniform_mixture_powers": [1, 16],
            "independent_closed_eigenvector_model": "2x2 real rotation, uniform row phases"}


def unitary(n):
    u = s.eye(n)
    phases = [s.Rational(3, 5)+s.I*s.Rational(4, 5),
              s.Rational(5, 13)+s.I*s.Rational(12, 13)]
    k = 0
    for i in range(n):
        for j in range(i+1, n):
            g = s.eye(n)
            g[i, i] = g[j, j] = s.Rational(3, 5)
            g[i, j] = s.Rational(4, 5)*phases[k % len(phases)]
            g[j, i] = -s.conjugate(g[i, j])
            u = (g*u).applyfunc(s.expand_complex)
            k += 1
    return u


def closure_checks():
    count, schur, delay = 0, 0, 0
    phases = [s.Rational(3, 5)+s.I*s.Rational(4, 5),
              s.Rational(-5, 13)+s.I*s.Rational(12, 13), -s.I, -1]
    for n in range(2, 5):
        U = unitary(n)
        assert (U*U.adjoint()).applyfunc(s.simplify) == s.eye(n)
        for i in range(n):
            E = [a for a in range(n) if a != i]
            D = s.diag(*(phases[a] for a in E))
            inv = (s.eye(n-1)-D*U.extract(E, E)).inv()
            X = (inv*D*U.extract(E, [i])).applyfunc(s.cancel)
            H = s.cancel(U[i, i]+(U.extract([i], E)*X)[0])
            eq(abs2(H), 1)
            psi = s.zeros(n, 1)
            psi[i] = 1
            for pos, a in enumerate(E):
                psi[a] = X[pos]
            fullphases = phases[:n]
            fullphases[i] = s.conjugate(H)
            assert (s.diag(*fullphases)*U*psi-psi).applyfunc(s.cancel) == s.zeros(n, 1)
            Q = 1+sum(abs2(z) for z in X)
            eq(1/Q, 1/sum(abs2(z) for z in psi))
            Xdot = s.I*inv*X
            Hdot = s.I*H+(U.extract([i], E)*Xdot)[0]
            eq(-s.I*s.conjugate(H)*Hdot, Q)
            delay += 1
            for j in E:
                A = [i, j]
                F = [a for a in E if a != j]
                S = U.extract(A, A)
                if F:
                    DF = s.diag(*(phases[a] for a in F))
                    S += U.extract(A, F)*(s.eye(len(F))-DF*U.extract(F,F)).inv()*DF*U.extract(F,A)
                S = S.applyfunc(s.cancel)
                assert (S*S.adjoint()).applyfunc(s.cancel) == s.eye(2)
                expected = phases[j]*S[1,0]/(1-phases[j]*S[1,1])
                eq(X[E.index(j)], expected)
                eq(abs2(S[0,1]), abs2(S[1,0]))
                eq(abs2(S[1,0])+abs2(S[1,1]), 1)
                schur += 1
            count += 1
    return {"matrix_sizes": [2,3,4], "source_closures": count,
            "scalar_delay_derivatives": delay,
            "ordered_pair_schur_closures": schur,
            "coefficient_domain": "Q(i), exact symbolic rational arithmetic"}


def finite_sampling_checks():
    x, y = s.symbols('x y')
    count = 0
    for weights in [[s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)],
                    [s.Rational(1,10),s.Rational(2,10),s.Rational(3,10),
                     s.Rational(4,10)], [s.S.Zero,s.Rational(1,3),s.Rational(2,3)]]:
        n = len(weights)
        for f in [lambda y:y, lambda y:y**2, lambda y:y/(1+y)]:
            direct = sum(weights[i]*f(weights[j]/(weights[i]+weights[j]))
                         for i in range(n) for j in range(n)
                         if i != j and weights[i])/(n-1)
            paired = sum(n*weights[i]*f(weights[j]/(weights[i]+weights[j]))
                         for i in range(n) for j in range(n)
                         if weights[i])/(n*n)
            eq(direct, n*paired/(n-1)-f(s.Rational(1,2))/(n-1))
            count += 1
    return {"weight_vectors": 3, "exact_without_replacement_checks": count}


def main():
    result = {"status":"passed", "python":platform.python_version(),
              "sympy":s.__version__, "kernels":kernel_checks(),
              "closures":closure_checks(), "sampling":finite_sampling_checks(),
              "non_claims":["No asymptotic eigenvector-intensity theorem.",
                            "Not a complete proof certificate of spectral averaging.",
                            "No physical or phase-ensemble BGS conclusion."]}
    with open(sys.argv[1], 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
