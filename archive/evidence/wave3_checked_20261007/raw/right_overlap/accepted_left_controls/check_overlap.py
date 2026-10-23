#!/usr/bin/env python3
"""Bounded exact checks of the new overlap indexing and Hessian bookkeeping.

No floats, randomness, actual-tau numerical extrapolation, or asymptotic
certification. Does not rerun the native worker's generator/twirl audit.
Run normal and -O; require() remains active in both.
"""
import hashlib
import json
from pathlib import Path
import sys
import time
import sympy as s

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
checks = []

def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)

def same(A, B):
    return all(s.expand(v) == 0 for v in A-B)

def fixture(n):
    v = s.Matrix(list(range(1, n+1)))
    w = s.Matrix([n+1-j for j in range(n)])
    Rv = s.eye(n) - 2*v*v.T/(v.T*v)[0]
    Rw = s.eye(n) - 2*w*w.T/(w.T*w)[0]
    return s.simplify(Rv*s.diag(*[s.I**j for j in range(n)])*Rw)

for n in [3, 5]:
    U = fixture(n)
    require(same(U.conjugate().T*U, s.eye(n)), f'unitarity N={n}')
    slices = []
    for c in range(n):
        A = s.zeros(n)
        for y in range(n):
            A[(y+c) % n, y] = U[(y+c) % n, y]
        slices.append(A)
    C = s.Matrix.hstack(*[s.Matrix(list(A.conjugate().T)) for A in slices])
    gram = C.conjugate().T*C
    require(all(gram[c,d] == 0 for c in range(n) for d in range(n) if c != d), f'orthogonal slices N={n}')
    H = s.kronecker_product(U, s.eye(n))  # row-major vectorization
    for r in [0, 1, 2, 3]:
        P = U**r
        K = s.Matrix(n, n, lambda c,d: sum(U[(x+c)%n,x] * s.conjugate(U[(x+c)%n,(x+c-d)%n]) * P[x,(x+c-d)%n] for x in range(n)))
        require(same(K,C.conjugate().T*(H**r)*C), f'overlap indexing N={n} r={r}')
        direct = s.Matrix([s.trace(A*P) for A in slices])
        require(same(direct,C.conjugate().T*s.Matrix(list(P))), f'frame orientation N={n} r={r}')
        require(same(C.conjugate().T*(H.conjugate().T**r)*C, K.conjugate().T), f'negative lag N={n} r={r}')

hessian_data = []
for r in range(1, 17):
    xx = s.symbols(f'x0:{r}')
    c, d = s.symbols('c d')
    var = list(xx)+[c,d]
    end = xx[0]+c-d
    pairs = [(xx[0]+c,xx[0]), (xx[0]+c,end)]
    pairs += [(xx[j], xx[j+1] if j+1<r else end) for j in range(r)]
    S = lambda x,y: -(3*x*x-2*x*y+3*y*y)/8
    phi = S(*pairs[0])-S(*pairs[1])+sum(S(*p) for p in pairs[2:])
    H = s.hessian(phi,xx)
    shift = s.zeros(r)
    for j in range(r):
        shift[j,(j+1)%r] = 1
    H0 = -s.Rational(3,2)*s.eye(r)+(shift+shift.T)/4
    require(same(H,H0), f'cyclic Hessian r={r}')
    require(all(sum(H[j,k] for k in range(r)) == -1 for j in range(r)), f'diagonal margin r={r}')
    v = s.zeros(r,1)
    v[r-1,0] += s.Rational(1,4)
    v[0,0] -= s.Rational(1,4)
    vc = s.Matrix([s.diff(phi,q,c) for q in xx])
    vd = s.Matrix([s.diff(phi,q,d) for q in xx])
    require(same(vc,v) and same(vd,-v) and s.diff(phi,c,d) == s.Rational(1,4), f'boundary mixed vectors r={r}')
    envelope = s.zeros(r+2)
    for p in pairs:
        J = s.Matrix([[abs(s.diff(z,q)) for q in var] for z in p])
        envelope += J.T*s.ones(2)*J
    row_bound = max(sum(envelope[i,j] for j in range(r+2)) for i in range(r+2))
    require(row_bound <= 64, f'perturbation envelope r={r}')
    val = s.diff(phi,c,d)-(vc.T*H.inv()*vd)[0]
    Mr = s.Matrix([[3,4],[2,3]])**r
    require(val == (Mr[0,0]+1)/(4*Mr[0,1]), f'cat Schur mixed r={r}')
    require(s.Rational(1,8) <= val <= s.Rational(1,4), f'cat mixed interval r={r}')
    hessian_data.append({'r':r,'perturbation_row_bound':str(row_bound),'reduced_mixed':str(val)})

# Exact rational slack checks. They support the stated constants, not the
# inherited analytic WKB source or any arbitrary-N stationary-phase theorem.
tau = s.Rational(1,10**80)
eta = s.Rational(1,10**60)
delta = s.Rational(1,10**50)
require(10**10*tau+s.Rational(10**50,2)*tau**2 < eta, 'literal tau Hessian slack')
require(64*eta < delta, 'full Hessian slack')
require(s.Rational(1,8)-5*delta > s.Rational(1,10), 'mixed lower slack')
require(s.Rational(1,4)+5*delta < s.Rational(1,3), 'mixed upper slack')
require(s.Rational(1,3) < s.Rational(1,2), 'TT* alias slack')

report = {
    'status':'passed', 'arithmetic':'exact Gaussian rationals and SymPy polynomial differentiation',
    'python_optimization':sys.flags.optimize, 'check_count':len(checks), 'checks':checks,
    'hessian_cases':hessian_data, 'elapsed_seconds':time.monotonic()-START,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope':'N=3,5 rational unitary indexing; cyclic Hessians r=1..16; literal rational slack. No analytic-limit certification.',
}
out = ROOT / ('checks_optimized.json' if sys.flags.optimize else 'checks.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','check_count','arithmetic','python_optimization','elapsed_seconds','scope']},indent=2))
