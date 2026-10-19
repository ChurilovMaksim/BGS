"""Repair v1's Python empty-sum division while preserving executed v1 bytes."""
import math
import sys
from fractions import Fraction as F
import verify_signed_rank as base


def exact_phase_cumulants(bound):
    f=[F(1,math.factorial(n)**2) for n in range(bound+1)]
    log=[F(0)]
    for n in range(1,bound+1):
        log.append(f[n]-sum((k*log[k]*f[n-k] for k in range(1,n)),F(0))/n)
    a=[log[n]*math.factorial(n) for n in range(bound+1)]
    kappa=[a[n]*math.factorial(n) for n in range(bound+1)]
    assert all(x.denominator==1 for x in kappa)
    assert kappa[1:6]==[1,-1,4,-33,456]
    return a,[int(x) for x in kappa]


if __name__=='__main__':
    base.phase_cumulants=exact_phase_cumulants
    base.main(sys.argv[1])
