#!/usr/bin/env python3
"""Exact multiorbit quartic and sum-of-squares certificate on the first box.

The polynomial identity is checked coefficientwise over integers, not by
sampling. Additional C++ comparisons are finite independent controls.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from collections import defaultdict
import hashlib
from itertools import product
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sympy as sp
from pell_sharp_coercivity_check import orbit_key,step


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cpp',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    a,b,c,d=variables=sp.symbols('a b c d',real=True)
    frequencies=((0,1),(1,-1),(1,0),(1,1))
    orbit=defaultdict(lambda:sp.Integer(0))
    for i,v in enumerate(frequencies):
        for j,w0 in enumerate(frequencies):
            w=step(w0)
            determinant=v[0]*w[1]-v[1]*w[0]
            if not determinant: continue
            coefficient=determinant*variables[i]*variables[j]
            for sign in (-1,1):
                key=orbit_key((v[0]+sign*w[0],v[1]+sign*w[1]))
                orbit[key]-=sign*coefficient
    orbit={k:sp.expand(p) for k,p in orbit.items() if sp.expand(p)!=0}
    actual=sp.expand(2*sum(p*p for p in orbit.values()))
    expected=(16*a**4+104*a*a*b*b+8*a*a*b*d+140*a*a*c*c+104*a*a*d*d
              +16*b**4+200*b*b*c*c+608*b*b*d*d+4*b*c*c*d
              +64*c**4+200*c*c*d*d+16*d**4)
    assert sp.Poly(actual-expected,*variables).is_zero
    sos=(48*c**4+108*a*a*c*c+68*a*a*(b*b+d*d)+4*(a*b+a*d)**2
         +166*c*c*(b*b+d*d)+2*(b*c+c*d)**2+576*b*b*d*d)
    assert sp.Poly(actual-16*(a*a+b*b+c*c+d*d)**2-sos,*variables).is_zero
    rows=[]
    for values in product((-1,0,1),repeat=4):
        if not any(values): continue
        result=int(actual.subs(dict(zip(variables,values))))
        assert result>=16*sum(x*x for x in values)**2
        rows.append([*values,result])
    witness_frequencies=((0,1),(0,2),(0,3),(1,-3),(1,-2),(1,-1),(1,1),(1,2),
                         (1,3),(2,-2),(2,-1),(2,0),(2,1),(2,2),(3,-1),(3,1))
    witness_coefficients=(-5,-7,4,1,5,-10,10,-5,-1,2,2,-6,2,2,1,-1)
    sums=defaultdict(int)
    for v,x in zip(witness_frequencies,witness_coefficients):
        for w0,y in zip(witness_frequencies,witness_coefficients):
            w=step(w0);determinant=v[0]*w[1]-v[1]*w[0]
            if not determinant:continue
            for sign in (-1,1):
                sums[orbit_key((v[0]+sign*w[0],v[1]+sign*w[1]))]-=sign*x*y*determinant
    witness_gamma=2*sum(x*x for x in sums.values())
    witness_c0=sum(x*x for x in witness_coefficients)
    assert witness_gamma==1890144 and witness_c0==396
    ratio=Fraction(witness_gamma,4*witness_c0*witness_c0)
    assert ratio==Fraction(6563,2178) and ratio<4
    cpp_status='NOT_RUN'
    if args.cpp:
        observed=json.loads(subprocess.check_output([str(args.cpp.resolve())],text=True,timeout=25))
        assert observed['four_mode_rows']==rows
        assert observed['radius_three_Gamma_over_pi_squared']==witness_gamma
        cpp_status='PASS'
    report={'status':'PASS','scope':'Exact coefficientwise quartic/SOS identity with analytic orbit classification; 80 independent finite C++ controls when requested. Not positive BGS.',
            'producer':'computations/verification/pell_four_mode_coercivity.py',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'frequencies':frequencies,'quartic':str(actual),'sos':str(sos),
            'orbit_polynomials':[[list(k),str(p)] for k,p in sorted(orbit.items())],
            'integer_rows':rows,'cpp_crosscheck':cpp_status,
            'radius_three_witness':{'frequencies':witness_frequencies,'coefficients':witness_coefficients,
              'Gamma_over_pi_squared':witness_gamma,'C0':witness_c0,'Gamma_over_pi_squared_L2_fourth':str(ratio),
              'nonzero_orbit_sums':[[list(k),int(v)] for k,v in sorted(sums.items()) if v]}}

    text=json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else: print(text,end='')

if __name__=='__main__':main()
