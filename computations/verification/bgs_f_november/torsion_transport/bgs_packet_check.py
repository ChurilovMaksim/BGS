"""Audit the bounds, exact symbol, and finite sector conventions in the report."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from argparse import ArgumentParser
from fractions import Fraction as Q
from itertools import product
import json
from math import factorial
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.linalg import eigh

DATA = Path(__file__).with_name("data") / "checks.json"


def rational_checks():
    z, w = sp.symbols("z w")
    cosine = lambda k: (z**k + z**(-k)) / 2
    sine1 = (z-z**-1)/(2*sp.I)
    r = (1-cosine(7))*(1+cosine(1))
    r_mid = (1+cosine(7))*(1-cosine(1))
    phase = (-3+4*sp.I)/5
    g = sp.expand(cosine(7)-sp.Rational(1,10)
        +r*(sp.Rational(1,10)+sine1/100)
        +r_mid*(sp.conjugate(phase)*w+phase/w)/200)
    coefficients = {}
    for term in sp.Add.make_args(g):
        k, l = (int(term.as_powers_dict().get(v,0)) for v in (z,w))
        c = term/(z**k*w**l)
        coefficients[(k,l)] = coefficients.get((k,l),0)+c
    assert coefficients[1,0] == (10-sp.I)/200
    assert coefficients[0,1] == (-3-4*sp.I)/1000
    assert len(coefficients) == 32
    assert all(abs(k)<=9 and abs(l)<=1 and abs(k)+abs(l)<=10
               for k,l in coefficients)
    assert sum(sp.Abs(c) for c in coefficients.values()).evalf(20) < 2
    # pi < 22/7 lets us use the rational series at the larger exponent.
    x = Q(55,7)
    exp_upper = sum(x**j/factorial(j) for j in range(41))
    exp_upper += x**41/factorial(41)/(1-x/42)
    assert exp_upper < 3000
    assert 2*10*exp_upper < 6*10**4
    assert 2*10*exp_upper*Q(440,7) < 4*10**6
    assert 4*factorial(10)**2 < 10**14
    assert factorial(20)*Q(16,3)**20 < 10**33
    assert Q(1,50)-10**62*Q(1,10**80) > Q(1,100)
    gain = Q(1,2560)-Q(161,40*20000)
    assert gain > Q(1,6000)
    assert Q(1,2560)-Q(1,4000) == Q(9,64000)
    assert Q(1,2)-Q(6,32) > Q(1,2560)
    assert 1-Q(8,32) > Q(1,2560)
    return coefficients, str(gain)


def weyl(n, a, b):
    positions = np.arange(n, dtype=np.int64)
    entries = (b*(positions+pow(2,-1,n)*a))%n
    result = np.zeros((n,n),dtype=np.complex128)
    result[positions,(positions+a)%n] = np.exp((2j*np.pi/n)*entries)
    return result


def cat(n):
    x = np.arange(n,dtype=np.int64)[:,None]
    y = x.T
    phase = (-pow(8,-1,n)*(3*x*x-2*x*y+3*y*y))%n
    return np.exp((2j*np.pi/n)*phase)/np.sqrt(n)


def sector_basis(n, l):
    d = n//(l*l)
    unit = np.zeros((n,n),dtype=np.complex128)
    for index,(position_character,shift_character) in enumerate(product(range(l),repeat=2)):
        for j in range(d):
            phases = np.exp(2j*np.pi*shift_character*np.arange(l)/l)/np.sqrt(l)
            rows = position_character+l*j+(n//l)*np.arange(l)
            unit[rows,index*d+j] = phases
    return unit


def norm(matrix):
    return np.linalg.norm(matrix,ord="fro")


def evaluate(n, l, coefficients):
    d = n//(l*l)
    j = np.arange(n)
    a = sum(complex(c)*(-1)**((k*s)%2)*weyl(n,s,k)
            for (k,s),c in coefficients.items())
    assert norm(a-a.conj().T) < 1e-11
    q = (j+0.5)/n + 0.5
    r_mid = (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
    edge = a[j,(j+1)%n]
    assert np.max(np.abs(edge-((-3-4j)/1000)*r_mid)) < 2e-14
    zero_edges = set()
    for x in range(n):
        # An exact edge zero satisfies (2x+1+N)/(2N)=m/7 modulo one.
        if (7*(2*x+1+n))%(2*n)==0:
            zero_edges.add(x)
    assert np.max(np.abs(edge[list(zero_edges)]),initial=0) < 2e-14
    assert all((x+1)%n not in zero_edges for x in zero_edges)

    basis = sector_basis(n,l)
    assert norm(basis.conj().T@basis-np.eye(n)) < 1e-11
    delta = n//l
    shift = weyl(n,delta,0)
    modulation = weyl(n,0,delta)
    assert norm(shift@modulation-modulation@shift) < 1e-11
    for index,(p,q) in enumerate(product(range(l),repeat=2)):
        sector = basis[:,index*d:(index+1)*d]
        assert norm(shift@sector-np.exp(2j*np.pi*q/l)*sector) < 1e-11
        assert norm(modulation@sector-np.exp(2j*np.pi*p/l)*sector) < 1e-11
        a_local = a@sector
        leak = a_local-sector@(sector.conj().T@a_local)
        assert np.linalg.matrix_rank(leak,tol=1e-12)==d

    m = cat(n)
    for source, target in (((1,0),(3,2)), ((0,1),(4,3))):
        assert norm(m@weyl(n,*source)-weyl(n,*target)@m) < 1e-11
    e, v = eigh(a)
    # A larger fixed kick so that a numerical test can resolve the effects.
    k = (v*np.exp(0.008j*n*e))@v.conj().T
    b_k = basis.conj().T@k@basis
    b_m = basis.conj().T@m@basis
    b_u = basis.conj().T@k@m@basis
    def probabilities(b):
        return (abs(b)**2).reshape(l*l,d,l*l,d).sum(axis=(1,3))/d
    pk, pm, pu = (probabilities(b) for b in (b_k,b_m,b_u))
    permutation = pm.argmax(axis=0)
    assert len(set(permutation)) == l*l
    assert np.max(abs(pm[permutation,np.arange(l*l)]-1)) < 1e-11
    assert np.max(np.abs(pu-pk[:,permutation])) < 1e-11
    assert np.max(np.abs(pk.sum(axis=0)-1)) < 1e-11
    assert np.max(np.abs(pk.sum(axis=1)-1)) < 1e-11

    twists = {}
    for s, t in ((1,2),(2,3),(1,1)):
        ws = weyl(n,delta*s,0)
        wt = weyl(n,0,delta*t)
        twists[s,t] = np.trace(ws@k@wt@k.conj().T)/n
    chars = np.array([np.exp(2j*np.pi*q/l) for p,q in product(range(l),repeat=2)])
    mod_chars = np.array([np.exp(2j*np.pi*p/l) for p,q in product(range(l),repeat=2)])
    for (s,t), value in twists.items():
        from_sectors = np.einsum("i,ij,j->",chars**s,pk,mod_chars**t)/(l*l)
        assert abs(value-from_sectors) < 1e-12
    return {
        "N":n,"L":l,"rank":d,"exact_zero_edges":len(zero_edges),
        "largest_return_probability_at_tau_0_008":float(pk.diagonal().max()),
        "smallest_return_probability_at_tau_0_008":float(pk.diagonal().min()),
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--record",action="store_true")
    parser.add_argument("--verify",action="store_true")
    args = parser.parse_args()
    coefficients,gain = rational_checks()
    report = {"relative_gain":gain,"nonzero_fourier_modes":len(coefficients),
              "examples":[evaluate(n,l,coefficients)
                          for n,l in ((9,3),(45,3),(49,7),(147,7),(343,7))]}
    if args.record:
        DATA.write_text(json.dumps(report,indent=2)+"\n")
    if args.verify:
        old = json.loads(DATA.read_text())
        assert report.keys() == old.keys()
        for key in ("relative_gain","nonzero_fourier_modes"):
            assert report[key] == old[key]
        for row, previous in zip(report["examples"],old["examples"],strict=True):
            for key,value in row.items():
                assert abs(value-previous[key])<1e-10
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
