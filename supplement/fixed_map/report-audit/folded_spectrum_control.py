"""A simple-spectrum control for the proposed resonance bootstrap.

This constructs abstract spectra, not quantizations of the fixed smooth map.
The proof and its exact scope are in folded_spectrum_control.md.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import jv

alpha, c = .5, .5
rows = []
n, pell_f = 1, 0
for K in range(1, 14):
    n, pell_f = n+2*pell_f, n+pell_f
    if K < 5 or K % 2 == 0:
        continue
    rho = K
    t = np.arange(n, dtype=float)/n
    theta = t+alpha*np.sin(2*np.pi*rho*t)/(2*np.pi*rho)
    gaps = n*np.diff(np.r_[theta,theta[0]+1])
    assert gaps.min() >= 1-alpha-1e-9
    assert gaps.max() <= 1+alpha+1e-9
    L = math.floor(c*n/rho)
    modes = np.arange(1,min(L,65))
    amplitudes = np.exp(2j*np.pi*(rho*modes[:,None])*theta[None,:]).mean(axis=1)
    continuum = (-1.)**modes*jv(modes,alpha*modes)
    error = float(np.max(abs(amplitudes-continuum)))
    assert error<1e-10
    energy = float(2*np.sum((1-modes/L)*abs(amplitudes)**2))
    short = np.exp(2j*np.pi*np.arange(1,rho)[:,None]*theta[None,:]).mean(axis=1)
    rows.append({"N":n,"rho":rho,"L":L,"alpha":alpha,"c":c,
                 "fejer_energy_through_mode_64":energy,
                 "proven_limit":1/math.sqrt(1-alpha*alpha)-1,
                 "maximum_amplitude_error_against_bessel":error,
                 "maximum_short_normalized_trace":float(np.max(abs(short))),
                 "minimum_unfolded_gap":float(gaps.min()),
                 "maximum_unfolded_gap":float(gaps.max()),
                 "tail_scope":"Analytic proof controls omitted modes; computed energy is the stated partial nonnegative sum"})
result={"status":"completed","rows":rows,
        "scope":"Abstract simple spectra with uniformly bounded local moments; not a fixed-map BGS counterexample"}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(rows,indent=2))
