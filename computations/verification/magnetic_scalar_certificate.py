#!/usr/bin/env python3
"""Independent one-dimensional polynomial certificate, not a BGS proof."""
from pathlib import Path
import json
import sys
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations/python'))
from bgs.magnetic_quotient import word_histogram,canonical_histogram,orbit_matrix


def main():
    base=[-1,-1,1,0,0,1,-1]
    power=[1,0,0,0,0,0,0]
    rows=[]
    for m in range(1,7):
        power=[sum(power[j]*base[(t-j)%7] for j in range(7)) for t in range(7)]
        expected=[2*(c-power[-1]) for c in power]
        observed=canonical_histogram(7,word_histogram(7,(1,2,4),m))
        assert observed==expected,(m,observed,expected)
        rows.append({'m':m,'canonical_histogram':observed})
    assert rows[0]['canonical_histogram']==[0,0,4,2,2,4,0]
    for q in range(1,7):
        z=np.exp(2j*np.pi*q/7)
        scalar=(z*z+z**5-z-z**6-1)/3
        assert abs(orbit_matrix(7,(1,2,4),q)[0,0]-scalar)<1e-12
    print(json.dumps({'producer':'computations/verification/magnetic_scalar_certificate.py',
      'scope':'Exact cyclic convolution versus signed Weyl words, plus a floating scalar-matrix check.',
      'histograms':rows},indent=2))
if __name__=='__main__':main()
