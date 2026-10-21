"""Independent exact checks of the Round 11 Pell/Magnus audit.

The all-r proof is reconstructed in r11_resolvent_audit_arithmetic.md.
These selected finite checks diagnose signs, coefficients and alias counts.
They do not numerically evaluate the prescribed kicked-map spectrum.
"""

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "r11_arithmetic_pell_magnus.md"
EXPECTED_SOURCE = "83fef65536de1e5528ad8e4d5eebf39a2b42d7da4217274a32c1e4e6dc7707d5"

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def conj(a):
    return a[0], -a[1]

def sq(a):
    return a[0]**2 + a[1]**2

def cv(v):
    return 3*v[0]+2*v[1], 4*v[0]+3*v[1]

def sig(v, w):
    return v[1]*w[0]-v[0]*w[1]

def pell(r):
    x, y = 1, 0
    for _ in range(r):
        x, y = x+2*y, x+y
    return x, y

# Independent input: displayed coefficient table, rather than the author's
# convolution construction of the symbol.
row = {
    1: (F(1,20),-F(1,200)), 2: (F(0),-F(1,400)),
    5: (F(0),-F(1,800)), 6: (-F(1,40),-F(1,400)),
    7: (F(9,20),F(0)), 8: (-F(1,40),F(1,400)),
    9: (F(0),F(1,800)),
}
modes = {}
for k, a in row.items():
    modes[k,0] = a
    modes[-k,0] = conj(a)
rcoef = {0:F(1), 1:F(1,2), -1:F(1,2), 6:-F(1,4),
         -6:-F(1,4), 7:-F(1,2), -7:-F(1,2),
         8:-F(1,4), -8:-F(1,4)}
for k, a in rcoef.items():
    modes[k,1] = -3*a/1000, -4*a/1000
    modes[k,-1] = -3*a/1000, 4*a/1000
assert len(modes) == 32 and (0,0) not in modes
assert all(modes[-k,-l] == conj(a) for (k,l),a in modes.items())
L0 = sum((sq(a) for (k,l),a in modes.items() if l == 0), F(0))
C0 = sum(map(sq,modes.values()), F(0))
first_hits = {(v,cv(v)) for v in modes if cv(v) in modes}
assert first_hits == {((1,-1),(1,1)),((-1,1),(-1,-1))}
C1 = (F(0),F(0))
for v,w in first_hits:
    C1 = add(C1,mul(modes[v],conj(modes[w])))
assert L0 == F(66015,160000)
assert C0 == F(66033,160000)
assert C1 == (-F(7,2000000),0)
assert C0+2*C1[0] == F(1650797,4000000)
assert 2*L0**2-C0**2 == F(4355603361,25600000000)
assert 4*sq(modes[7,0])*sq(modes[0,1]) == F(81,4000000)
assert all(sig(cv(v),cv(w)) == sig(v,w) for v,w in product(modes,repeat=2))

# Exact modular Weyl phases and the Egorov kernel phase.
phase_cases = 0
for n in (3,5,35):
    half, eighth = pow(2,-1,n), pow(8,-1,n)
    vals = sorted({0,1,2,n-1})
    for a,b,ap,bp,x in product(vals,repeat=5):
        lhs = b*(x+half*a)+bp*(x+a+half*ap)
        rhs = (b+bp)*(x+half*(a+ap))+half*(a*bp-b*ap)
        assert (lhs-rhs) % n == 0
        phase_cases += 1
    def kernel(x,y):
        return -eighth*(3*x*x-2*x*y+3*y*y)
    for a,b,x,y in product(vals,repeat=4):
        aa,bb = 3*a+4*b, 2*a+3*b
        lhs = kernel(x,y-a)+b*(y-half*a)
        rhs = bb*(x+half*aa)+kernel(x+aa,y)
        assert (lhs-rhs) % n == 0
        phase_cases += 1
    for v,w in product(modes,repeat=2):
        h = sig(v,w)
        assert (2*half*h-h) % n == 0
        k,l = v
        kp,lp = w
        rephase = 2*half*h+n*(k*l+kp*lp-(k+kp)*(l+lp))-h
        assert rephase % (2*n) == 0
        phase_cases += 1

# Rational margins suffice uniformly once y >= 10^9.
threshold = 10**9
assert pell(25) == (1855077841,1311738121)
assert pell(25)[1] > threshold
quadratic_margin = F(threshold**2,61440)-1520*threshold-5122-162
quadratic_derivative = F(threshold,30720)-1520
linear_margin = F(threshold,1520)-5122-162
same_type_margin = F(threshold,80)-F(32,threshold)-18
old_collision_margin = F(2*5741,75)-F(15,5741)-18
assert min(quadratic_margin,quadratic_derivative,linear_margin,
           same_type_margin,old_collision_margin) > 0

reports = []
for r in (11,13,25,27,31):
    x,y = pell(r)
    n,c,d = x*y,x*x+2*y*y,2*r
    assert x*x-2*y*y == -1 and n % 2 == 1
    assert c % x == 1 and c % y == y-1
    assert c*c-8*n*n == 1
    layers = []
    current = {(v[0]%n,v[1]%n):v for v in modes}
    for _ in range(d):
        layers.append(current)
        current = {((3*a+2*b)%n,(4*a+3*b)%n):v
                   for (a,b),v in current.items()}
    assert current == layers[0]
    actual = set()
    for lag in range(1,d):
        for image,v in layers[lag].items():
            if image in layers[0]:
                actual.add((lag,v,layers[0][image]))
    expected = {(1,(1,-1),(1,1)),(1,(-1,1),(-1,-1)),
                (d-1,(1,1),(1,-1)),(d-1,(-1,-1),(-1,1))}
    assert actual == expected
    record = {"r":r,"N":n,"two_mode_collision_count":len(actual)}
    if r >= 25:
        images = set()
        seed_reports = []
        for eps,eta in product((-1,1),repeat=2):
            v0,w0 = (7*eps,0),(0,eta)
            target = (v0[0]%n,(c*w0[1])%n)
            hits = set()
            # Both orders and equal-time cases are checked independently.
            for i,j in product(range(d),repeat=2):
                for image,v in layers[i].items():
                    rem = ((target[0]-image[0])%n,(target[1]-image[1])%n)
                    if rem in layers[j]:
                        hits.add((i,j,v,layers[j][rem]))
            assert hits == {(0,r,v0,w0),(r,0,w0,v0)}
            seed_reports.append({"eps":eps,"eta":eta,"ordered_decompositions":2,
                                 "equal_time_decompositions":0})
            z = target
            for _ in range(d):
                images.add(z)
                z = ((3*z[0]+2*z[1])%n,(4*z[0]+3*z[1])%n)
        assert len(images) == 8*r and (0,0) not in images
        assert 8*r*F(81,4000000) == F(81*r,500000)
        assert 8*r*F(81,4000000)/4 == F(81*r,2000000)
        record.update({"seeds":seed_reports,"distinct_shifted_indices":len(images)})
    reports.append(record)

source_hash = sha256(SOURCE.read_bytes()).hexdigest()
assert source_hash == EXPECTED_SOURCE
result = {
    "status":"PASS: exact selected checks; universal proof is in the audit",
    "source_sha256":source_hash,
    "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
    "phase_cases":phase_cases,
    "constants":{"L0":str(L0),"C0":str(C0),"C1":str(C1[0]),
                 "variance":str(C0+2*C1[0]),
                 "fourth_lower":str(2*L0**2-C0**2)},
    "rational_threshold_margins":{
        "quadratic":str(quadratic_margin),"quadratic_derivative":str(quadratic_derivative),
        "isotropic_linear":str(linear_margin),"same_type":str(same_type_margin),
        "r11_two_mode":str(old_collision_margin)},
    "finite_pell_checks":reports,
    "scope":"No U_N eigenvalues or spectral statistics were computed.",
}
out = BASE / "r11_resolvent_arithmetic_checks.json"
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
