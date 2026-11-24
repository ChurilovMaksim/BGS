"""Numerical diagnostics of the Fourier bound, independent of the proof."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fourth_order.bgs_packet_check import orbit, value

P = 7


def weights(m, cutoff):
    d = np.fft.fftfreq(m)*m
    d = np.rint(d).astype(int)
    mask = np.abs(d)>cutoff
    f = np.zeros(m,complex)
    f[mask] = 1/(m*(-np.expm1(-2j*np.pi*d[mask]/m)))
    return d,np.fft.fft(f)


def progression_diagnostic():
    ratios=[]
    for k in (3,4,6,8):
        m=3*P**(k-1)
        divisors={P**a for a in range(k)}|{3*P**a for a in range(k)}
        for cutoff in (2, min(m//4,k**3)):
            d,f=weights(m,cutoff)
            envelope=np.minimum(1,m/(cutoff*np.maximum(1,np.abs(d))))
            assert np.max(np.abs(f)/envelope)<4
            val=0.0
            for divisor in divisors:
                mass=np.sum(abs(f.reshape(-1,divisor))**2,axis=0)
                val=max(val,float(np.max(mass)/(1+m/(divisor*cutoff))))
            assert val<4
            ratios.append(val)
    return max(ratios)


def same_orbit_diagnostic():
    results=[]
    for k in (2,3,4,5,6):
        n,powers=orbit(k)
        m=len(powers)
        cutoff=min(m//4,4*k)
        d,f=weights(m,cutoff)
        w=np.empty(m)
        nonzero=d!=0
        w[~nonzero]=2.5
        w[nonzero]=1/(2*m*np.sin(np.pi*np.abs(d[nonzero])/m)-0.4)
        w[np.abs(d)>cutoff]=0
        fw=abs(np.fft.fft(w))**2
        vals=np.array([value(x-1,k) for x in powers])
        suffix=np.array([np.sum(fw[vals>=s]) for s in range(k+1)])
        signed=np.sum(abs(f)**2*suffix[k-vals])/m
        unsigned=np.sum(fw*suffix[k-vals])/m
        assert signed<=unsigned
        results.append((k,round(float(signed),5),round(float(unsigned),5)))
    return results


if __name__ == "__main__":
    print("Largest normalized progression mass in the numerical test:",
          round(progression_diagnostic(),6))
    print("Depth, signed weighted closure, positive weighted closure:")
    print(same_orbit_diagnostic())
