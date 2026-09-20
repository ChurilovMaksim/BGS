"""FFT check in the large quantum-exponent regime; not a BGS simulation."""
import json
import numpy as np
from scipy.special import jv


def run(n,tau=.04):
    eps=tau*n;q=int(np.ceil(np.log(n)))
    assert eps>=16 and q<=eps/2 and q<=n/2 and tau<=1/16
    x=np.arange(n)
    values=np.exp(1j*eps*np.cos(2*np.pi*x/n))
    coeff=np.fft.fft(values)/n
    modes=np.arange(-q,q+1)
    observed=coeff[modes%n]
    continuum=(1j**modes)*jv(modes,eps)
    alias_rounding_error=float(np.max(np.abs(observed-continuum)))
    assert alias_rounding_error<1e-10
    mass=float(np.sum(np.abs(observed)**2))
    upper=32*(2*q+1)/eps+32*(2*q+1)*np.exp(-n/2)
    assert mass<=upper+1e-12
    return dict(N=n,tau=tau,epsilon=eps,Q=q,retained_HS_mass=mass,
                best_HS_approximation_error=float(np.sqrt(1-mass)),
                proved_mass_upper_bound=float(upper),
                FFT_Bessel_discrepancy=alias_rounding_error)


if __name__=='__main__':
    print(json.dumps(dict(rows=[run(2**k-1) for k in (10,12,14,16,18,20)],
                         scope='One-harmonic kick, test coupling .04; no frozen-map or asymptotic numerical proof'),indent=2))
