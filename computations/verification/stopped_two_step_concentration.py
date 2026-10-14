"""Bounded independent controls for diagonal extensions and deterministic weights.
Exact rationals/residues; no probability simulation or BGS certificate.
Timeout 90 s, one worker, memory <=1 GiB. All dimensions <=16.
"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import json
import sympy as sp

w = sp.Symbol('w')

@lru_cache(None)
def integrals(a,terms):
    q=w/(1-a*w);qc=1/(w-a)
    expr=sp.cancel(sum(count*(x+q*t)*(x+qc*t)*(y+q*z)*(y+qc*z) for (x,t,y,z),count in terms))
    delta=sp.cancel(expr-sp.Rational(1,16))
    result=[]
    for power in [1,2]:
        f=sp.cancel(delta**power/w)
        result.append(sp.simplify(sp.residue(f,w,0)+sp.residue(f,w,a)))
    return tuple(result)


def exact_diagonal():
    n=16
    s=sp.Matrix(n,n,lambda i,j:sp.Rational((-1)**((int(i)&int(j)).bit_count()),4))
    assert s*s.T==sp.eye(n)
    delta=sp.Rational(1,16);k=sp.Rational(1,16);p3=k
    cases=[]
    for i,j in [(0,0),(3,3),(0,3)]:
        mean=second=0
        for e in range(n):
            if e in [i,j]:continue
            counts=Counter((s[i,l],s[i,e]*s[e,l],s[l,j],s[l,e]*s[e,j]) for l in range(n) if l!=e)
            terms=tuple(sorted(counts.items()))
            first,raw=integrals(s[e,e],terms);mean+=first/n;second+=raw/n
            for phase in [1,-1,sp.I,-sp.I]:
                q=phase/(1-s[e,e]*phase)
                new=sum(sp.expand_complex((x+q*t)*sp.conjugate(x+q*t)*(y+q*z)*sp.conjugate(y+q*z))*count for (x,t,y,z),count in terms)
                inc=sp.simplify(new-k)
                assert inc**2 <=sp.Integer(32)**2*delta**3
        mean=sp.simplify(mean);second=sp.simplify(second)
        rhs=(-k/2+5*p3+2*delta*sp.Rational(1,16))/n
        assert mean <=rhs
        assert second <=2600*delta**2*(k+p3)/n
        cases.append({'pair':[i,j],'mean_increment':str(mean),'raw_second_moment':str(second)})
    return {'dimension':n,'delta':str(delta),'port_phase_integral_cases':cases,'distinct_cached_integrands':integrals.cache_info().currsize}


def weights():
    b,m=20,16;a=F(4,3);forcing=F(7,5);beta=forcing/a
    cases=[]
    for stop_kind,stop_old in [('none',None),('endpoint',19),('global_crossing',18)]:
        y={b:F(9,5)};xi={};slack={};active=True
        for v in range(b,m,-1):
            if active:
                xi[v]=F((-1)**v,13)
                slack[v]=F(1,100*v)
                y[v-1]=(1-a/v)*y[v]+forcing/v+xi[v]-slack[v]
                if v==stop_old:active=False
            else:
                xi[v]=F(0);slack[v]=F(0)
                y[v-1]=(1-a/v)*y[v]+forcing/v
        for u in range(b,m-1,-1):
            initial=F(1)
            for v in range(u+1,b+1):initial*=1-a/v
            random=lost=F(0)
            for v in range(u+1,b+1):
                factor=F(1)
                for r in range(u+1,v):factor*=1-a/r
                random+=factor*xi[v];lost+=factor*slack[v]
            assert y[u]==beta+initial*(y[b]-beta)+random-lost
            assert y[u]<=beta+initial*y[b]+random
        cases.append({'stopping_convention':stop_kind,'old_crossing_size':stop_old,'exact_telescoping_targets':b-m+1})
    # factorial domination in the exponential-martingale proof.
    fact=2
    for k in range(2,51):
        if k>2:fact*=k
        assert fact>=2*3**(k-2)
    return {'recurrence_cases':cases,'factorial_controls_through':50,'non_claim':'The recurrence controls do not model unitary feedback or prove a tail bound.'}



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = {'claim': 'BGS-TRACE-079', 'exact_unitary':exact_diagonal(),'exact_weights':weights(),'non_claim':'Finite algebra and phase integrals; no asymptotic probability proof.'}
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
