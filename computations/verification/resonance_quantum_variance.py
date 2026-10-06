#!/usr/bin/env python3
"""Exact finite Weyl/Green--Kubo variance comparison, with Gaussian integers.

No dense quantum matrix, trigonometric rounding or random-matrix assumption is
used. The finite non-aliasing condition is checked before equality is asserted.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random
from resonance_nondegeneracy_certificate import orbit_forms, step
from resonance_hessian_obstruction import add,conj,mul,scale,absolute_squared,row_gamma

def pell(k):
    n,f=1,0
    for _ in range(k):n,f=n+2*f,n+f
    return n,f

def power_rows(h):
    u=(1,0);v=(0,1)
    for _ in range(h):u=step(u);v=step(v)
    return abs(u[0])+abs(v[0]),abs(u[1])+abs(v[1])

def raw_bracket(modes,z):
    coeff={}
    for v,a in zip(modes,z):coeff[v]=a;coeff[(-v[0],-v[1])]=conj(a)
    raw=defaultdict(lambda:(0,0))
    for u,a in coeff.items():
        for v,b in coeff.items():
            w=step(v);det=u[0]*w[1]-u[1]*w[0]
            if det:
                k=(u[0]+w[0],u[1]+w[1])
                raw[k]=add(raw[k],scale(-det,mul(a,b)))
    return {v:c for v,c in raw.items() if c!=(0,0)}

def quantum_square(raw,k,n):
    total=defaultdict(lambda:(0,0))
    for v,c in raw.items():
        w=v
        for _ in range(k):
            key=(w[0]%n,w[1]%n)
            sign=1 if (w[0]*w[1])%2==0 else -1
            total[key]=add(total[key],scale(sign,c));w=step(w)
        assert (w[0]-v[0])%(2*n)==0 and (w[1]-v[1])%(2*n)==0
    return Fraction(sum(absolute_squared(c) for c in total.values()),k)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();rng=random.Random(2026090602);records=[]
    for radius,k in ((1,9),(3,11),(8,13),(8,17)):
        modes,rows=orbit_forms(radius);n,f=pell(k);h=(k-1)//2
        r1,r2=power_rows(h);M=8*radius
        threshold=M*M*(4+4*r1+2*r2)
        assert n*n>threshold
        for trial in range(3):
            z=[(rng.randrange(-2,3),rng.randrange(-2,3)) for _ in modes]
            raw=raw_bracket(modes,z)
            assert max(max(abs(a),abs(b)) for a,b in raw)<=M
            reference=row_gamma(rows,z);observed=quantum_square(raw,k,n)
            assert observed==reference and reference>0
            records.append({'R':radius,'K':k,'N':n,'trial':trial,'N_squared':n*n,
                            'nonaliasing_upper_bound':threshold,
                            'raw_bracket_frequencies':len(raw),
                            'Gamma_over_pi_squared':reference,'weyl_trace_over_pi_squared':str(observed)})
    radius=2;k=3;n,_=pell(k);modes,rows=orbit_forms(radius)
    z=[(1+(i%2),(-1)**i) for i in range(len(modes))]
    reference=row_gamma(rows,z);observed=quantum_square(raw_bracket(modes,z),k,n)
    assert observed!=reference
    result={'status':'PASS','producer':'computations/verification/resonance_quantum_variance.py',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'checks':records,'small_modulus_negative_control':{'R':radius,'K':k,'N':n,
                  'Gamma_over_pi_squared':reference,'finite_quantum_trace_over_pi_squared':str(observed)},
            'scope':'Exact Gaussian-integer Weyl coefficient norms on the full space. Not a dense eigenspectrum, a quantum commutator equality at finite N, or a BGS theorem.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','exact_quantum_cases':len(records),'negative_control':result['small_modulus_negative_control']},indent=2))
if __name__=='__main__':main()
