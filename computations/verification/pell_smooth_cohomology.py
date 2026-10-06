#!/usr/bin/env python3
"""Exact Fourier-orbit reduction and independent smooth-resonance falsifiers.

The analytic C-infinity theorem is proved in the companion note, not by
these finite tests. Rational orbit coefficients, dense numerical matrices,
and floating-point Weyl moments are reported separately.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import subprocess
import numpy as np

Vec = tuple[int, int]
Poly = dict[Vec, Q]  # coefficient of exp(2pi i v.x)+exp(-2pi i v.x)
ROOT = Path(__file__).resolve().parents[2]


def T(v: Vec) -> Vec:
    a,b=v
    return 3*a+2*b, 4*a+3*b


def Ti(v: Vec) -> Vec:
    a,b=v
    return 3*a-2*b, -4*a+3*b


def sign_quad(p: int, q: int) -> int:
    """Exact sign of p+q*sqrt(2), without a floating comparison."""
    if q == 0: return (p>0)-(p<0)
    if p == 0: return (q>0)-(q<0)
    if p>0 and q>0: return 1
    if p<0 and q<0: return -1
    d=p*p-2*q*q
    return ((d>0)-(d<0)) * (1 if p>0 else -1)


def positive(v: Vec) -> Vec:
    if v==(0,0): raise ValueError('mean-zero nonzero Fourier modes required')
    return v if sign_quad(v[1],v[0])>0 else (-v[0],-v[1])


def clean(p: Poly) -> Poly:
    out=defaultdict(Q)
    for v,c in p.items(): out[positive(v)]+=Q(c)
    return {v:c for v,c in out.items() if c}


def orbit(v: Vec) -> tuple[Vec,int]:
    """v=+/- T^j r, with |Norm psi(r)| <= psi(r)^2 < lambda^2 |Norm|."""
    v=positive(v); a,b=v; norm=abs(b*b-2*a*a); j=0
    if norm==0: raise AssertionError('sqrt(2) is irrational')
    while sign_quad(b*b+2*a*a-norm,2*a*b)<0:
        a,b=T((a,b)); j-=1
    while sign_quad(b*b+2*a*a-17*norm,2*a*b-12*norm)>=0:
        a,b=Ti((a,b)); j+=1
    return (a,b),j


def advance(v: Vec, j: int) -> Vec:
    for _ in range(abs(j)): v=T(v) if j>0 else Ti(v)
    return v


def shift(p: Poly) -> Poly:
    return clean({T(v):c for v,c in p.items()})


def combine(*pairs: tuple[Q,Poly]) -> Poly:
    out=defaultdict(Q)
    for a,p in pairs:
        for v,c in p.items(): out[positive(v)]+=a*c
    return {v:c for v,c in out.items() if c}


def reduction(p: Poly) -> tuple[Poly,Poly,Q]:
    """Return h,g,sigma^2 with p=h+g-Cg, by finite orbit summation."""
    chains=defaultdict(lambda:defaultdict(Q))
    for v,c in clean(p).items():
        r,j=orbit(v); chains[r][j]+=c
    h={}; g=defaultdict(Q)
    for r,chain in chains.items():
        amplitude=sum(chain.values(),Q())
        if amplitude: h[r]=amplitude
        chain[0]-=amplitude
        running=Q()
        for j in range(min(chain),max(chain)+1):
            running+=chain[j]
            if running: g[positive(advance(r,j))]+=running
        assert running==0
    g=clean(g)
    assert clean(p)==combine((Q(1),h),(Q(1),g),(Q(-1),shift(g)))
    sigma=2*sum((a*a for a in h.values()),Q())
    return h,g,sigma


def full(p: Poly) -> Poly:
    out={}
    for v,c in clean(p).items(): out[v]=out[(-v[0],-v[1])]=c
    return out


def second_over_pi(g: Poly) -> Poly:
    """h/pi=-Omega(g,Cg); h={g,Cg}/(4pi), with usual x,y bracket."""
    out=defaultdict(Q)
    for v,a in full(g).items():
        for w,b in full(shift(g)).items():
            determinant=v[0]*w[1]-v[1]*w[0]
            out[(v[0]+w[0],v[1]+w[1])]-=determinant*a*b
    assert out.pop((0,0),Q())==0
    for v,c in out.items(): assert c==out.get((-v[0],-v[1]),Q())
    return {v:c for v,c in out.items() if c and sign_quad(v[1],v[0])>0}


def pell(k: int) -> tuple[int,int]:
    n,f=1,0
    for _ in range(k): n,f=n+2*f,n+f
    return n,f


def samples() -> dict[str,Poly]:
    v=(1,0); w=(0,1)
    g={v:Q(1),w:Q(1,2),(1,1):Q(-1,3)}
    return {
        'single':{v:Q(1)},
        'same_orbit_sum':{v:Q(1),T(v):Q(1)},
        'coboundary':{v:Q(1),T(v):Q(-1)},
        'two_orbits':{v:Q(1),w:Q(1)},
        'triangle':{v:Q(1),w:Q(1),(1,1):Q(1)},
        'mixed_generator':g,
        'mixed_coboundary':combine((Q(1),g),(Q(-1),shift(g))),
        'mixed_second_over_pi':second_over_pi(g),
    }


def exact_checks() -> dict:
    count=0
    for a in range(-12,13):
        for b in range(-12,13):
            if (a,b)==(0,0): continue
            r,j=orbit((a,b))
            assert positive(advance(r,j))==positive((a,b))
            for t in (-7,-1,0,2,8):
                rr,jj=orbit(advance((a,b),t))
                assert rr==r and jj==j+t
            count+=1
    p=samples(); info=[]
    for name,poly in p.items():
        h,g,sigma=reduction(poly)
        assert reduction(combine((Q(1),poly),(Q(1),{(9,8):Q(2)}),
                                 (Q(-1),shift({(9,8):Q(2)}))))[2]==sigma
        info.append({'name':name,'sigma_squared':str(sigma),'mode_count':len(poly),
                     'canonical_modes':[[*v,str(c)] for v,c in sorted(h.items())],
                     'coboundary_modes':[[*v,str(c)] for v,c in sorted(g.items())]})
    assert {x['name']:x['sigma_squared'] for x in info}['same_orbit_sum']=='8'
    assert reduction(p['coboundary'])[2]==0
    assert reduction(p['triangle'])[2]==6
    for a,b in ((1,0),(0,1),(1,1),(2,-3)):
        h0=second_over_pi({(a,b):Q(1)})
        assert reduction(h0)[2]==16*(b*b-2*a*a)**2
    # Both signs and the characteristic field norm identities are exact.
    return {'orbit_cases':count,'rows':info,'single_generator_quartic_controls':4}


def modular_atoms(p: Poly,k: int) -> tuple[int,dict[Vec,Q]]:
    n,_=pell(k); out=defaultdict(Q)
    for v,c in clean(p).items():
        for _ in range(k):
            a,b=v; coeff=c*((-1)**(a*b % 2))
            out[(a % n,b % n)]+=coeff
            out[(-a % n,-b % n)]+=coeff
            v=T(v)
    return n,{v:c for v,c in out.items() if c}


def weyl_moments(p: Poly,k: int) -> dict:
    import cmath
    n,atoms=modular_atoms(p,k); half=pow(2,-1,n)
    conv=defaultdict(complex)
    for v,a in atoms.items():
        for w,b in atoms.items():
            exponent=((v[0]*w[1]-v[1]*w[0])*half) % n
            if exponent>n//2: exponent-=n
            phase=cmath.exp(2j*math.pi*(exponent/n))
            conv[((v[0]+w[0]) % n,(v[1]+w[1]) % n)]+=float(a*b)/k*phase
    second=conv.get((0,0),0j)
    third=sum(z*float(atoms.get((-v[0] % n,-v[1] % n),Q()))
              for v,z in conv.items())/math.sqrt(k)
    fourth=sum(abs(z)**2 for z in conv.values())
    l1=2*sum(abs(float(a)) for a in p.values())
    return {'K':k,'N':str(n),'full_second':float(second.real),
            'full_third':float(third.real),'full_fourth':float(fourth),
            'odd_fourth_center':float(n/(n-1)*fourth),
            'odd_fourth_tail_bound':float(k*k*l1**4/(n-1)),
            'rounding_scope':'complex double evaluation, analytic parity-tail bound is separate'}


def dense_checks() -> list[dict]:
    from pell_floquet_regression import weyl,hermitian_exponential
    out=[]
    for k in (3,5,7):
        n,f=pell(k); s=pow(f,-1,n); h=(3+2*s) % n
        # Change physical Fourier coordinates by M^{-1}; no scalar phase is lost.
        half=pow(2,-1,n)
        mi=((-s % n,-1 % n),(half,-pow(2*s,-1,n) % n))
        def matrix(p):
            ans=np.zeros((n,n),complex)
            for (a,b),c in clean(p).items():
                va=(mi[0][0]*a+mi[0][1]*b) % n
                vb=(mi[1][0]*a+mi[1][1]*b) % n
                z=weyl(n,va,vb)*((-1)**(a*b % 2))
                ans+=float(c)*(z+z.conj().T)
            return ans
        d=(n-1)//2; pr=np.zeros((n,d)); ids=np.arange(1,d+1)
        pr[ids,ids-1]=1/math.sqrt(2);pr[n-ids,ids-1]=-1/math.sqrt(2)
        ufull=np.eye(n,dtype=complex)[(h*np.arange(n)) % n]; u=pr.T@ufull@pr
        for name,p in samples().items():
            if name=='mixed_second_over_pi': continue
            hpoly,gpoly,sigma=reduction(p)
            b,hh,gg=[pr.T@matrix(poly)@pr for poly in (p,hpoly,gpoly)]
            assert np.max(abs(b-hh-gg+u@gg@u.conj().T))<3e-10
            assert np.max(abs(pr.T@matrix(shift(p))@pr-u@b@u.conj().T))<3e-10
            avg=np.zeros_like(b); z=b.copy()
            for _ in range(k): avg+=z/k;z=u@z@u.conj().T
            vals=np.linalg.eigvalsh(math.sqrt(k)*avg)
            if sigma==0: assert max(abs(vals))<1e-9
            eps=.4/math.sqrt(k)
            kicked=hermitian_exponential(b,eps)@u
            tr=np.trace(np.linalg.matrix_power(kicked,k))/d
            out.append({'K':k,'name':name,'sigma_squared':str(sigma),
                        'odd_second':float(np.mean(vals**2)),
                        'odd_third':float(np.mean(vals**3)),
                        'odd_fourth':float(np.mean(vals**4)),
                        'actual_recurrence_trace':[float(tr.real),float(tr.imag)],
                        'limiting_trace':math.exp(-.5*.4**2*float(sigma))})
        # Independently test the smooth commutator asymptotic and sign.
        g=samples()['mixed_generator']; a=pr.T@matrix(g)@pr; dd=u@a@u.conj().T
        h0=pr.T@matrix(second_over_pi(g))@pr
        err=np.linalg.norm(a@dd-dd@a+(2j*math.pi/n)*h0,2)
        bound=0.
        for v,av in full(g).items():
            for w,bv in full(shift(g)).items():
                om=abs(v[0]*w[1]-v[1]*w[0])
                bound+=float(abs(av*bv))*(math.pi*om/n)**3/3
        assert err<=bound+1e-9
        out.append({'K':k,'commutator_cubic_remainder':float(err),
                    'Fourier_bound':float(bound)})
    return out


def report(cpp: Path|None) -> dict:
    exact=exact_checks()
    if cpp:
        rows=json.loads(subprocess.check_output([str(cpp.resolve())],text=True))
        expected=[{'a':a,'b':b,'r':list(orbit((a,b))[0]),'j':orbit((a,b))[1]}
                  for a in range(-12,13) for b in range(-12,13) if (a,b)!=(0,0)]
        assert rows==expected
    moments=[]
    for k in (11,17,31,61,101):
        for name in ('single','same_orbit_sum','coboundary','two_orbits','triangle'):
            row=weyl_moments(samples()[name],k);row['name']=name
            sigma=reduction(samples()[name])[2]
            row['sigma_squared']=str(sigma)
            # Exact absence of cohomology after averaging, also modulo N.
            assert abs(row['full_second']-float(sigma))<1e-9
            if name=='coboundary': assert row['full_fourth']==0
            moments.append(row)
    return {'producer':'computations/verification/pell_smooth_cohomology.py',
            'scope':'Exact rational Fourier cohomology and optional independent C++ orbit classification; finite dense and Weyl-moment numerical falsifiers. Not a proof of the C-infinity limits, a priority claim, or certified floating-point intervals.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'cpp_cross_check':bool(cpp),'exact':exact,'moments':moments,
            'dense':dense_checks(),'status':'PASS'}



def sampled_traces(k: int, name: str, probes: int=8) -> list[dict]:
    """Actual sparse kicked propagators; RMS sampling and rounding are separate."""
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import expm_multiply
    if k not in (11,13) or probes<2:
        raise ValueError('extended reference uses K=11 or 13 and at least two probes')
    n,f=pell(k); root=pow(f,-1,n); h=(3+2*root) % n
    mi=((-root % n,-1 % n),(pow(2,-1,n),-pow(2*root,-1,n) % n))
    if name=='second_order':
        generator=samples()['mixed_generator']
        poly=combine((Q(1),generator),(Q(-1),shift(generator)))
        gamma=math.pi**2*float(reduction(second_over_pi(generator))[2])
        epsilon=math.sqrt(n/(math.sqrt(k)*math.sqrt(gamma)))
        variance=1.
    else:
        poly=samples()[name];epsilon=.4/math.sqrt(k)
        variance=.4**2*float(reduction(poly)[2])
    x=np.arange(n,dtype=np.int64); op=csr_matrix((n,n),dtype=complex)
    for (a,b),coef in clean(poly).items():
        aa=(mi[0][0]*a+mi[0][1]*b) % n
        bb=(mi[1][0]*a+mi[1][1]*b) % n
        exponent=(aa*(x-bb*pow(2,-1,n))) % n
        values=((-1)**(a*b % 2))*np.exp(2j*np.pi*exponent/n)
        z=csr_matrix((values,(x,(x-bb) % n)),shape=(n,n))
        op+=float(coef)*(z+z.conj().T)
    d=(n-1)//2;seed=20260905+k
    rng=np.random.default_rng(seed)
    coefficients=(1j)**rng.integers(0,4,size=(d,probes))
    z=np.zeros((n,probes),complex)
    ids=np.arange(1,d+1)
    z[ids]=coefficients/math.sqrt(2);z[n-ids]=-coefficients/math.sqrt(2)
    initial=z.copy(); rows=[]
    for step in range(1,2*k+1):
        z=expm_multiply((1j*epsilon)*op,z[(h*x) % n],traceA=0.)
        if step % k==0:
            estimates=np.sum(initial.conj()*z,axis=0)/d
            drift=float(max(abs(np.sum(abs(z)**2,axis=0)/d-1)))
            assert drift<1e-8
            rows.append({'K':k,'N':n,'name':name,'m':step//k,'epsilon':epsilon,
                         'trace_real':float(estimates.mean().real),
                         'trace_imag':float(estimates.mean().imag),
                         'limit':math.exp(-.5*(step//k)**2*variance),
                         'probes':probes,'seed':seed,'complex_RMS_bound':1/math.sqrt(d*probes),
                         'norm_drift':drift,
                         'scope':'actual sparse exponential propagation; unbiased exact-unitary probe estimator; RMS is stochastic, no certified numerical rounding bound'})
    return rows


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cpp',type=Path);p.add_argument('--output',type=Path)
    p.add_argument('--exact-only',action='store_true')
    p.add_argument('--extended',action='store_true');p.add_argument('--probes',type=int,default=4)
    p.add_argument('--max-k',type=int,choices=(11,13),default=11)
    a=p.parse_args(); data=exact_checks() if a.exact_only else report(a.cpp)
    if a.extended:
        data['sampled_traces']=[]
        data['extended_complete']=False
        for k in (11,13):
            if k>a.max_k: continue
            for name in ('same_orbit_sum','coboundary','triangle','second_order'):
                data['sampled_traces'].extend(sampled_traces(k,name,a.probes))
                if a.output:
                    a.output.parent.mkdir(parents=True,exist_ok=True)
                    a.output.write_text(json.dumps(data,indent=2)+'\n')
                print('completed sparse check',k,name,flush=True)
        data['extended_complete']=True
    text=json.dumps(data,indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
    else: print(text,end='')

if __name__=='__main__': main()
