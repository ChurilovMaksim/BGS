#!/usr/bin/env python3
"""Exact finite controls for the actual fixed-word freeness proof.

Standard library only. No numerical evaluation of literal tau, asymptotic
experiment, network, or writes unless --output is specified. The finite word
enumeration is a regression, not proof of universal freeness or Egorov.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import argparse
import json


def require(value, label):
    if not value:
        raise RuntimeError(label)


# Rational polynomial coefficients, increasing order.
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def plus(a, b):
    return trim((a[j] if j < len(a) else 0) +
                (b[j] if j < len(b) else 0)
                for j in range(max(len(a), len(b))))


def times(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


ZERO = (0,)
ONE = (1,)
ID = ((ONE, ZERO), (ZERO, ONE))
S = (((3,), (4,)), ((2,), (3,)))
SINVERSE = (((3,), (-4,)), ((-2,), (3,)))


def matmul(a, b):
    return tuple(tuple(plus(times(a[i][0], b[0][j]),
                                 times(a[i][1], b[1][j]))
                       for j in range(2)) for i in range(2))


def spower(n):
    out = ID
    a = S if n >= 0 else SINVERSE
    for _ in range(abs(n)):
        out = matmul(out, a)
    return out


def tpower(n):
    return ((ONE, ZERO), ((0, n), ONE))


def trace(a):
    return plus(a[0][0], a[1][1])


# Gaussian rationals and Laurent polynomials, independently assembled.
def ga(re=0, im=0):
    return (F(re), F(im))


def gadd(a, b):
    return (a[0]+b[0], a[1]+b[1])


def gmul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def gpow(a, n):
    out = ga(1)
    for _ in range(n):
        out = gmul(out, a)
    return out


def lplus(a, b):
    out = dict(a)
    for v, c in b.items():
        out[v] = gadd(out.get(v, ga()), c)
    return {v: c for v, c in out.items() if c != ga()}


def lscale(a, c):
    return {v: gmul(z, c) for v, z in a.items() if gmul(z,c) != ga()}


def ltimes(a, b):
    out = {}
    for (j,k), c in a.items():
        for (l,m), d in b.items():
            v = (j+l,k+m)
            out[v] = gadd(out.get(v,ga()),gmul(c,d))
    return {v: c for v, c in out.items() if c != ga()}


def physical_symbol():
    one = {(0,0):ga(1)}
    c1 = {(1,0):ga(F(1,2)),(-1,0):ga(F(1,2))}
    c7 = {(7,0):ga(F(1,2)),(-7,0):ga(F(1,2))}
    sinq = {(1,0):ga(0,F(-1,2)),(-1,0):ga(0,F(1,2))}
    r = ltimes(lplus(one,lscale(c7,ga(-1))),lplus(one,c1))
    shifted_r = {v:gmul(c,ga((-1)**v[0])) for v,c in r.items()}
    cospa = {(0,1):ga(F(-3,10),F(-4,10)),
             (0,-1):ga(F(-3,10),F(4,10))}
    out = lplus(c7,lscale(r,ga(F(1,10))))
    out = lplus(out,lscale(ltimes(r,sinq),ga(F(1,100))))
    out = lplus(out,lscale(ltimes(shifted_r,cospa),ga(F(1,100))))
    return lplus(out,lscale(one,ga(F(-1,10))))


def normalized_derivative_at_corner(g, dq, dp, q2, p2):
    out = ga()
    for (k,l), c in g.items():
        phase = ga((-1)**(k*q2+l*p2))
        deriv = gmul(gpow(ga(0,k),dq),gpow(ga(0,l),dp))
        out = gadd(out,gmul(c,gmul(phase,deriv)))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--inject-failure',action='store_true')
    args = parser.parse_args()
    g = physical_symbol()
    require(len(g)==32 and (0,0) not in g,'actual centered 32-mode symbol')
    expected = [F(-19606,125),F(-19594,125),F(24306,125),F(24894,125)]
    corners=[]
    for (q2,p2), expected_qq in zip(product((0,1),repeat=2),expected):
        for dq,dp in [(1,0),(0,1),(1,1),(0,2)]:
            require(normalized_derivative_at_corner(g,dq,dp,q2,p2)==ga(),
                    'equilibrium and zero mixed/p-p Hessian')
        qq=gmul(ga(4),normalized_derivative_at_corner(g,2,0,q2,p2))
        require(qq==ga(expected_qq),'exact Hessian coefficient in pi squared')
        corners.append({'q2':q2,'p2':p2,'gqq_over_pi2':str(qq[0])})
    require(-expected[0]/2==F(9803,125),'literal derivative parameter')

    # Complete cyclic block controls for all 1,2,3 blocks with small signed exponents.
    choices=(-2,-1,1,2)
    cyclic_count=0
    for k in (1,2,3):
        for exponents in product(choices,repeat=2*k):
            matrix=ID
            predicted=1
            for a,b in zip(exponents[::2],exponents[1::2]):
                sa=spower(a)
                require(sa[0][1] != ZERO,'nonzero off diagonal for nonzero cat power')
                predicted*=b*sa[0][1][0]
                matrix=matmul(matmul(matrix,sa),tpower(b))
            p=trace(matrix)
            require(len(p)==k+1 and p[-1]==predicted and predicted!=0,
                    'all-block highest trace coefficient')
            cyclic_count+=1

    # Complete freely reduced words through length8, retaining conjugates.
    letters={'q':tpower(1),'Q':tpower(-1),'m':S,'M':SINVERSE}
    inv={'q':'Q','Q':'q','m':'M','M':'m'}
    layer=[('',ID)]
    word_count=0
    for length in range(1,9):
        nxt=[]
        for word,matrix in layer:
            for ch,letter in letters.items():
                if word and ch==inv[word[-1]]:
                    continue
                new=matmul(matrix,letter)
                require(new!=ID,'nonidentity polynomial matrix on reduced word')
                nxt.append((word+ch,new))
                word_count+=1
        layer=nxt
    require(word_count==2*(3**8-1),'exhaustive reduced-word count')

    # Fixed echo polynomial highest term, includes inverse cat powers.
    echoes=[]
    st=matmul(S,tpower(1))
    powered=ID
    for k in range(1,13):
        powered=matmul(powered,st)
        echo=matmul(spower(-k),powered)
        p=trace(echo)
        if k==1:
            require(p==(2,) and echo==tpower(1),'unipotent first echo')
        else:
            coefficient=4**(k-1)*spower(1-k)[0][1][0]
            require(len(p)==k+1 and p[-1]==coefficient!=0,'fixed echo highest coefficient')
        echoes.append({'m':k,'trace_coefficients':list(p)})
    commutator=matmul(matmul(matmul(S,tpower(1)),SINVERSE),tpower(-1))
    require(trace(commutator)==(2,0,16),'shortest commutator trace')
    if args.inject_failure:
        require(False,'deliberate fault injection')
    result={'status':'passed','arithmetic':'exact integer polynomial and rational Gaussian',
            'actual_symbol_modes':len(g),'corner_Hessians':corners,
            'derivative_parameter_over_tau_pi':'9803/125',
            'cyclic_blocks_exhaustive_cases':cyclic_count,
            'reduced_words_through_length8':word_count,
            'fixed_echo_controls':echoes,
            'commutator_trace_coefficients':list(trace(commutator)),
            'scope':'finite algebraic regressions; not analytic/asymptotic certification',
            'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
