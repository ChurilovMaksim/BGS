"""Finite checks of the odd-N circular Dyson clock kernel.

complex128; deterministic Fourier/biorthogonal comparisons.
This does not prove an asymptotic statement and does not simulate BGS.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
from numpy.polynomial.legendre import leggauss

def alias_kernel(n, t, x, y, phase=0., rmax=12):
    ell = np.arange(-(n-1)//2, (n-1)//2+1)
    r = np.arange(-rmax, rmax+1)
    k = ell[:, None] + n*r[None, :]
    weight = np.exp(-t*(k*k-ell[:, None]**2)/(2*n))
    psi = np.einsum('lr,lry->ly', weight,
        np.exp(1j*k[:, :, None]*y[None, None, :]
               -1j*n*r[None, :, None]*phase))/(2*np.pi)
    return np.exp(-1j*x[:, None]*ell[None, :])@psi

def heat_biorthogonal_kernel(n, t, x, y, phase=0., cutoff=200):
    ell = np.arange(-(n-1)//2, (n-1)//2+1)
    a = phase + 2*np.pi*np.arange(n)/n
    k = np.arange(-cutoff, cutoff+1)
    # phi_l=e^{-ilx}; q_a(y) is the periodic scalar heat kernel.
    gram = np.exp(-t*ell[:, None]**2/(2*n)-1j*ell[:, None]*a[None, :])
    heat = (np.exp(-1j*a[:, None]*k[None, :])
            *np.exp(-t*k[None, :]**2/(2*n)))@np.exp(1j*k[:, None]*y[None, :])/(2*np.pi)
    dual = np.linalg.solve(gram.T, heat)
    return np.exp(-1j*x[:, None]*ell[None, :])@dual

def residual_sum(n, t, rmax=50):
    ell=np.arange(-(n-1)//2,(n-1)//2+1)
    return sum(np.sum(np.exp(-t*(2*r*n*ell+r*r*n*n)/(2*n)))
               for r in range(-rmax,rmax+1) if r)/n

def run():
    worst=0.
    for n in [3,5,9,15]:
        for c in [1.,3.,10.]:
            t=c/n
            x=np.array([.03,.44,1.8,4.1])
            y=np.array([.21,.94,2.7,5.2])
            ka=alias_kernel(n,t,x,y,.123)
            kb=heat_biorthogonal_kernel(n,t,x,y,.123)
            err=np.max(abs(ka-kb))
            assert err<2e-11
            worst=max(worst,err)
            residual=residual_sum(n,t)
            assert residual<=3/(n*t)
    result={'independent_kernel_cases':12,'max_error':float(worst)}

    # A compact local window; N t = sqrt(N) grows in this illustrative table.
    rows=[]
    uv=np.linspace(-1,1,13)
    for n in [31,101,301,1001]:
        t=n**(-.5)
        a=.381
        k=(2*np.pi/n)*alias_kernel(n,t,a+2*np.pi*uv/n,a+2*np.pi*uv/n)
        sine=np.sinc(uv[:,None]-uv[None,:])
        rows.append({'N':n,'t':t,'kernel_error':float(np.max(abs(k-sine))),
                     'alias_majorant':float(residual_sum(n,t))})
    result['local_kernel_checks']=rows
    result['hole_quadratures']=[]

    # Independent quadrature of a limiting observable: sine-process hole on [0,1].
    for q in [24,48,96]:
        nodes,weights=leggauss(q)
        nodes=(nodes+1)/2
        weights=weights/2
        op=np.sqrt(weights[:,None]*weights[None,:])*np.sinc(nodes[:,None]-nodes[None,:])
        sign,logdet=np.linalg.slogdet(np.eye(q)-op)
        assert sign>0
        result['hole_quadratures'].append({'quadrature_order':q,'sine_hole_length_one':float(np.exp(logdet))})

    # Analytic truncation majorant for r>=13 at the smallest Nt=1.
    # Each side contributes at most exp(-r(r-1)/2), uniformly in odd N.
    ratio=np.exp(-13.)
    alias_tail=2*np.exp(-13*12/2)/(1-ratio)
    assert alias_tail<1e-32
    result['omitted_alias_tail_bound']=float(alias_tail)
    result['status']='PASS'
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run()
    result.update({'python':platform.python_version(),'numpy':np.__version__,
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Odd-N heat/Gram comparisons, finite local kernels, illustrative quadrature; not a universality certificate.',
       'resource_caps':{'max_local_N':1001,'max_Gram_N':15,'heat_cutoff':200,'alias_rmax':12,'max_quadrature':96}})
    data=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(data)
    print(data,end='')

if __name__=='__main__':
    main()
