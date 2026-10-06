#!/usr/bin/env python3
"""Exact Fourier Gram identities and rational soft-mode Rayleigh quotients.

The rate is proved analytically in temporal_resonance.tex. Plotted Rayleigh
quotients are upper bounds on the smallest eigenvalue, not fitted eigenvalues.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sympy as s
from extremal_resonance import (filter_apply, autocorrelation, bracket, transport,
                               orbit_sums, gm, gc, det, mv, power)

def polynomial_power(t,q):
    p=[1]
    for _ in range(q):
        out=[0]*(len(p)+2)
        for i,a in enumerate(p):
            for j,b in enumerate([1,-t,1]): out[i+j]+=a*b
        p=out
    return p

def symbol_coefficients(t,q):
    z=s.symbols('z'); d=4*q
    F=s.expand((2-z-1/z)**(2*q)*(t*t-2-z-1/z)**(2*q))
    return {j:int(F.coeff(z,j)) for j in range(-d,d+1)}

def rayleigh(n,q,coeff):
    x=[j**(2*q)*(n+1-j)**(2*q) for j in range(1,n+1)]
    numerator=sum(a*b*coeff.get(i-j,0) for i,a in enumerate(x) for j,b in enumerate(x))
    denominator=sum(a*a for a in x)
    return Fraction(numerator,denominator)

def gram_check(a,q):
    t=abs(a[0]+a[3]);p=polynomial_power(t,q);d=2*q
    g0={(1,0):(1,0),(-1,0):(1,0)};g=filter_apply(a,g0,p)
    lags=list(range(d+1,d+7));b=autocorrelation(p)
    rows=[orbit_sums(a,bracket(g,transport(a,g,r))) for r in lags]
    for i,r in enumerate(lags):
        for j,k in enumerate(lags):
            exact=sum(gm(z,gc(rows[j].get(v,(0,0))))[0] for v,z in rows[i].items())
            expected=0
            for ell in range(max(1,r-d,k-d),min(r+d,k+d)+1):
                D=det((1,0),mv(power(a,ell),(1,0)))
                expected+=4*D*D*b[abs(ell-r)]*b[abs(ell-k)]
            assert exact==expected
    return {'A':a,'q':q,'lags':lags,'entry_checks':len(lags)**2}

def main():
    if not __debug__: raise RuntimeError('Assertions must be enabled')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path);ap.add_argument('--figure',type=Path)
    args=ap.parse_args()
    z,t,c,si,lam=s.symbols('z t c si lam')
    P=z*z-t*z+1
    assert s.expand(P*P.subs(z,1/z)-(z+1/z-t)**2)==0
    expr=((lam+1/lam)*(c-1))**2+((lam-1/lam)*si)**2-(2-2*c)*((lam-1/lam)**2+2-2*c)
    assert s.expand(expr).subs(si**2,1-c*c).expand()==0
    checks=[gram_check(a,q) for a in [(3,-1,1,0),(-3,1,-1,0),(6,-1,1,0),(-6,1,-1,0)] for q in [1,2,3]]
    data=[]
    for q in [1,2,3]:
        cf=symbol_coefficients(3,q)
        for n in [8,16,32,64,128,256,512]:
            f=rayleigh(n,q,cf);assert f>0
            data.append({'q':q,'n':n,'numerator':str(f.numerator),'denominator':str(f.denominator),
                         'rayleigh_quotient':float(f),'scaled_by_n_power':float(f*n**(4*q))})
    result={'status':'PASS','scope':'exact Fourier Gram identities and exact rational trial-vector quotients',
            'symbolic_identities':2,'gram_configurations':len(checks),'gram_entry_checks':sum(x['entry_checks'] for x in checks),
            'rational_rayleigh_quotients':len(data),'gram_checks':checks,'rayleigh_data':data,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    if args.figure:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,ax=plt.subplots(figsize=(7,4.8))
        for q in [1,2,3]:
            rows=[r for r in data if r['q']==q];base=rows[0]['rayleigh_quotient']
            ax.loglog([r['n'] for r in rows],[r['rayleigh_quotient']/base for r in rows],marker='o',label=f'q={q}: trial Rayleigh quotient')
        ax.set_xlabel('Number of temporal lags n');ax.set_ylabel('Rayleigh quotient / value at n=8')
        ax.set_title('Collective soft modes: exact rational trial vectors')
        ax.legend();ax.grid(True,which='both',alpha=0.25);fig.tight_layout()
        args.figure.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.figure,dpi=180);plt.close(fig)
    print(json.dumps({k:v for k,v in result.items() if k not in ['gram_checks','rayleigh_data']},indent=2))

if __name__=='__main__':main()
