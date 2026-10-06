#!/usr/bin/env python3
"""Exact finite loop-reduction checks. Requires SymPy; no asymptotic claim.

Run with --output PATH to save a receipt; default is stdout only.
--inject-failure is reserved for verifying fail-closed test behavior.
Importing this module is silent and has no side effects.
"""
import argparse
import json
from pathlib import Path


class CheckFailure(RuntimeError):
    """A required exact identity failed."""


def require_equal(actual, expected, label):
    import sympy as sp
    difference = actual - expected
    entries = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
    if any(sp.simplify(entry) != 0 for entry in entries):
        raise CheckFailure(label)


def partial_trace_second(matrix, n):
    import sympy as sp
    if matrix.shape != (n*n, n*n):
        raise ValueError('Partial trace input shape must equal (n*n,n*n).')
    return sp.Matrix(n, n, lambda a, b: sum(matrix[a*n+j, b*n+j] for j in range(n)))


def run_checks(inject_failure=None):
    import sympy as sp
    I = sp.I
    z = [sp.Integer(1), (3+4*I)/5, (-5+12*I)/13]
    n, q, cut = len(z), sp.Rational(1,4), 2
    p = lambda a: sum(v**a for v in z)
    full = [sp.simplify(sum(q*v/u/(1-q*v/u) for u in z)) for v in z]
    short = [sp.simplify(sum(q**a*p(-a)*v**a for a in range(1,cut+1))) for v in z]
    long = [sp.simplify(a-t) for a,t in zip(full,short)]
    cubic_long = sp.simplify(sum(sum(sum((q*v/u)**(cut+1)/(1-q*v/u)*(q*v/t)**(cut+1)/(1-q*v/t) for u in z) for t in z) for v in z)/n**3)
    require_equal(sum(f*f for f in long)/n**3, cubic_long + (1 if inject_failure=='cubic' else 0), 'long cubic geometric identity')
    require_equal(sum(a*a for a in full)-sum(f*f for f in long), sum(2*t*f+t*t for t,f in zip(short,long)), 'once-counted overlap')
    require_equal((sum(full)-sum(long))/n**2, sum(q**a*p(a)*p(-a) for a in range(1,cut+1))/n**2 + (1 if inject_failure=='pair' else 0), 'pair normalization')
    # Independent nondiagonal tensor inverse, ordinary unnormalized partial trace.
    n = 2
    h = sp.Matrix([[3,4],[4,-3]])/5
    vals = [sp.Integer(1),(3+4*I)/5]
    u = sp.simplify(h*sp.diag(*vals)*h.T)
    require_equal(u*u.conjugate().T,sp.eye(n),'unitary fixture')
    x = sp.kronecker_product(u,u.conjugate())
    tensor_resolvent = (q*x)**(cut+1)*(sp.eye(n*n)-q*x).inv()
    f = partial_trace_second(tensor_resolvent,n)
    diagonal = [sp.simplify(sum((q*v/w)**(cut+1)/(1-q*v/w) for w in vals)) for v in vals]
    expected_f = h*sp.diag(*diagonal)*h.T
    require_equal(f, expected_f + (sp.eye(n) if inject_failure=='tensor' else sp.zeros(n)), 'unnormalized nondiagonal partial trace')
    require_equal(sp.trace(f*f),sum(a*a for a in diagonal),'algebraic square trace')
    return {'schema':'bgs-loop-reductions-finite-v1','arithmetic':'exact rational complex / SymPy','checks':6,'all_passed':True,'fixtures':{'diagonal_n':3,'nondiagonal_n':2,'q':'1/4','K':2},'boundary':'Finite algebra only; actual long-long residual and all-order hierarchy remain open.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--inject-failure',choices=['pair','cubic','tensor'],help='Test-only intentional corruption; must exit nonzero.')
    args = parser.parse_args(argv)
    try:
        result = run_checks(args.inject_failure)
    except (CheckFailure,ValueError) as exc:
        parser.exit(2,'CHECK FAILED: '+str(exc)+'\n')
    text = json.dumps(result,indent=2)+'\n'
    if args.output is not None:
        args.output.write_text(text)
    print(text,end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
