#!/usr/bin/env python3
"""Independent bounded exact controls; no analytic-limit certification.

Uses complex nonsymmetric Gaussian-rational unitary fixtures. Assertions use
explicit exceptions and remain active under python -O. Row-major vectorization
is implemented independently from the matrix slice loops.
"""
import hashlib
import json
from pathlib import Path
import sys
import time
import sympy as s

start = time.monotonic()
checks = []

def require(ok, name, category):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append({'name': name, 'category': category})

def same(A, B):
    return all(s.expand(z) == 0 for z in A-B)

def vec(A):
    return s.Matrix([A[i,j] for i in range(A.rows) for j in range(A.cols)])

def frame(U):
    n = U.rows
    out = s.zeros(n*n,n)
    for c in range(n):
        for y in range(n):
            row = (y+c) % n
            # A_c^*: entry (y,row) is conjugate(U[row,y]).
            out[y*n+row,c] = s.conjugate(U[row,y])
    return out

def fixture(n, seed=0):
    v = s.Matrix([j+1+s.I*(1+(j+seed)%3) for j in range(n)])
    w = s.Matrix([n-j+s.I*((j+2*seed)%2) for j in range(n)])
    Hv = s.eye(n)-2*v*v.conjugate().T/(v.conjugate().T*v)[0]
    Hw = s.eye(n)-2*w*w.conjugate().T/(w.conjugate().T*w)[0]
    return s.simplify(Hv*s.diag(*[s.I**(j+seed) for j in range(n)])*Hw)

for n in (3,5):
    U = fixture(n)
    C, CT = frame(U), frame(U.T)
    J = s.zeros(n*n)
    for i in range(n):
        for j in range(n):
            J[j*n+i,i*n+j] = 1
    P = s.zeros(n)
    for c in range(n):
        P[(-c)%n,c] = 1
    R = s.kronecker_product(s.eye(n), U.T)
    LT = s.kronecker_product(U.T, s.eye(n))
    require(same(U.conjugate().T*U,s.eye(n)), f'unitary complex fixture N={n}', 'fixture')
    require(not same(U,U.T), f'nonsymmetric fixture N={n}', 'fixture')
    require(same(J.conjugate().T*J,s.eye(n*n)), f'J HS-unitary N={n}', 'transpose')
    require(same(J*J,s.eye(n*n)), f'J involution N={n}', 'transpose')
    X = s.Matrix(n,n,lambda i,j: (i+1)+s.I*(2*j-i))
    require(same(J*vec(s.I*X),s.I*vec(X.T)), f'J complex-linear N={n}', 'transpose')
    require(same(J*C,CT*P), f'J frame slice-flip N={n}', 'transpose')
    require(same(J*R,LT*J), f'J right-left intertwiner N={n}', 'transpose')
    for r in range(4):
        require(same(C.conjugate().T*(R**r)*C,
                     P*CT.conjugate().T*(LT**r)*CT*P),
                f'right overlap transpose identity N={n} r={r}', 'transpose')
    B = fixture(n,seed=1)
    for r in range(4):
        Xr = B*(U**r)
        direct = s.Matrix([sum(U[(y+c)%n,y]*Xr[y,(y+c)%n]
                              for y in range(n)) for c in range(n)])
        require(same(C.conjugate().T*vec(Xr),direct),
                f'fixed-B right frame traces N={n} r={r}', 'prefix')
        require(same((R**r)*vec(B),vec(Xr)),
                f'fixed-B right orbit N={n} r={r}', 'prefix')
    L = 3
    synthesis = s.Matrix.hstack(*[(R.conjugate().T**j)*C for j in range(L)])
    gram = synthesis.conjugate().T*synthesis
    for j in range(L):
        for k in range(L):
            power = R**(j-k) if j>=k else R.conjugate().T**(k-j)
            require(same(gram[j*n:(j+1)*n,k*n:(k+1)*n],C.conjugate().T*power*C),
                    f'right fixed-block Gram N={n} j={j} k={k}', 'prefix')

for r in range(1,17):
    xs = s.symbols(f'x0:{r}')
    c,d = s.symbols('c d')
    var = list(xs)+[c,d]
    end = xs[0]+c-d
    pairs = [(xs[0]+c,xs[0]),(xs[0]+c,end)]
    pairs += [(xs[j],xs[j+1] if j+1<r else end) for j in range(r)]
    cat = lambda x,y,a: -(3*x*x-2*x*(y+a)+3*(y+a)**2)/8
    coefficients = [1,-1]+[1]*r
    phi = sum(sign*cat(x,y,0) for sign,(x,y) in zip(coefficients,pairs))
    phiT = sum(sign*cat(y,x,j%4) for j,(sign,(x,y)) in enumerate(zip(coefficients,pairs)))
    require(same(s.hessian(phiT,var),s.hessian(phi,var)),
            f'all cat Hessian blocks unchanged after transpose r={r}', 'cat')

root = Path(__file__).resolve().parent
report = {'status':'passed','python_optimization':sys.flags.optimize,
          'arithmetic':'exact Gaussian rational and SymPy polynomial',
          'check_count':len(checks),'transpose_check_count':sum(x['category']=='transpose' for x in checks),
          'checks':checks,'elapsed_seconds':time.monotonic()-start,
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'N=3,5 nonsymmetric complex rational unitaries; transpose algebra, fixed-B frame and L=3 Gram; cat full Hessians r=1..16. No candidate packet tests and no analytic-limit certificate.'}
out = root/('transpose_checks_optimized.json' if sys.flags.optimize else 'transpose_checks.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','check_count','transpose_check_count','python_optimization','elapsed_seconds','scope')},indent=2))
