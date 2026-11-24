"""Outward rational bounds for the original pair test and its arithmetic limit."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sys

GRID=7**3*16
Q=1<<44

def down(x):
    return x.numerator*Q//x.denominator

def bump(i):
    if i>=GRID:
        return 0,0
    y=1/(1-F(i*i,GRID*GRID))
    if y>=40:
        assert F(8,3)**40>Q
        return 0,1
    u=y/64
    lo=sum((-u)**j/factorial(j) for j in range(16))
    hi=lo+u**16/factorial(16)
    a,b=down(lo),-down(-hi)
    for _ in range(6):
        a=a*a//Q
        b=(b*b+Q-1)//Q
    return a,b

def convolution(values):
    width=((len(values)*max(values)**2).bit_length()+7)//8
    word=int.from_bytes(b''.join(v.to_bytes(width,'little') for v in values),'little')
    packed=(word*word).to_bytes((2*len(values)-1)*width,'little')
    return [int.from_bytes(packed[i*width:(i+1)*width],'little')
            for i in range(len(values)-1,2*len(values)-1)]+[0]

def bound():
    positive=[bump(i) for i in range(GRID+1)]
    cells=[(min(positive[abs(i)][0],positive[abs(i+1)][0]),
            max(positive[abs(i)][1],positive[abs(i+1)][1])) for i in range(-GRID,GRID)]
    lo,hi=map(list,zip(*cells))
    cl,ch=convolution(lo),convolution(hi)
    slo,shi=sum(lo),sum(hi)
    low_w=lambda idx: F(GRID**2*cl[idx]**2,4*shi**4)
    high_w=lambda idx: F(GRID**2*ch[idx]**2,4*slo**4)
    low_cue=F(sum(min(i,GRID)*cl[i+1]**2 for i in range(2*GRID)), 4*shi**4)
    high_cue=F(sum(min(i+1,GRID)*ch[i]**2 for i in range(2*GRID)), 4*slo**4)
    low_first=low_w(3*GRID//7)
    high_zero=high_w(0)
    assert low_first>F(6854,100000) and high_zero<F(1141,10000) and high_cue<F(2067,100000)
    L=H=F(0)
    for a in range(3):
        q=7**(a+1)
        for u in range(1,(2*q-1)//3+1):
            if u%7:
                assert (3*u*GRID)%q==0
                j=(3*u*GRID)//q
                L+=low_w(j)/7**(2*a)
                H+=high_w(j)/7**(2*a)
    tail=F(49,9*7**3)*high_zero
    low_limit=L-high_cue
    high_limit=H+tail-low_cue
    assert F(84,1000)<low_limit<high_limit<F(87,1000)
    n=7**56
    t=F(n,10**80)
    m=3*n//7
    assert n>10**47 and t<F(1,2)
    assert 64*t*t*m<F(1,10**8)**2
    assert 23**2*m*m*t**3<F(203,1000)**2
    dist=F(204,1000)
    norm_trace=1-dist**2/2
    actual_lower=low_first*norm_trace**2-high_cue-2*high_zero/49
    bounded_gap=1-F(196,1000)-dist**2/2
    assert (F(196,1000)/2)**2>F(1,105)
    assert actual_lower>F(40,1000) and bounded_gap>F(78,100)
    return dict(grid=GRID, upper_dimension=n,
                first_weight_lower=str(low_first), zero_weight_upper=str(high_zero),
                cue_upper=str(high_cue), fixed_kick_pair_lower=str(actual_lower),
                bounded_test_gap_lower=str(bounded_gap),
                weak_pair_limit_lower=str(low_limit), weak_pair_limit_upper=str(high_limit),
                first_weight_lower_decimal=float(low_first), cue_upper_decimal=float(high_cue),
                weak_pair_limit_lower_decimal=float(low_limit), weak_pair_limit_upper_decimal=float(high_limit))

if __name__=='__main__':
    data=bound()
    if '--verify' in sys.argv:
        assert data==json.loads((Path(__file__).resolve().parent/'data/weights.json').read_text())
        print('Rational bounds, finite fixed kick and weak limit verified.')
    else:
        print(json.dumps(data,indent=2))
