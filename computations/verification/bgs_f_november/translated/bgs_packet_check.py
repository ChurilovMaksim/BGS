"""Verify the finite Fourier identities and spectral-filter inequalities."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
from itertools import product
import json
import sys

import numpy as np
from scipy.linalg import expm, schur

def multiply_label(u, v, n):
    phase = pow(2,-1,n)*(u[0]*v[1]-u[1]*v[0]) % n
    return phase, tuple((a+b) % n for a,b in zip(u,v))

def arithmetic_check(d, multiplier):
    n = d*d*multiplier
    h = n//d
    labels = list(product(range(d), repeat=2))
    for u, v in product(labels, repeat=2):
        phase, index = multiply_label(tuple(h*a for a in u),tuple(h*b for b in v),n)
        assert phase == 0 and index == tuple(h*((a+b)%d) for a,b in zip(u,v))
    return len(labels)**2

def weyl(a,b,n):
    mat = np.zeros((n,n),dtype=complex)
    x = np.arange(n)
    mat[x,(x+a)%n] = np.exp(2j*np.pi*((b*(x+pow(2,-1,n)*a))%n)/n)
    return mat

def sample(n,d,ell):
    x,y = np.indices((n,n))
    m = np.exp(2j*np.pi*((-pow(8,-1,n)*(3*x*x-2*x*y+3*y*y))%n)/n)/np.sqrt(n)
    q = np.arange(n)/n
    r=lambda t: (1-np.cos(14*np.pi*t))*(1+np.cos(2*np.pi*t))
    a=np.diag(np.cos(14*np.pi*q)-.1+r(q)*(.1+.01*np.sin(2*np.pi*q))).astype(complex)
    xx=np.arange(n)
    link=(-3-4j)*r(((xx+pow(2,-1,n))%n)/n)/1000
    a[xx,(xx+1)%n]+=link
    a[(xx+1)%n,xx]+=link.conjugate()
    u=expm(.71j*a)@m
    labels=list(product(range(d),repeat=2))
    weights=np.array([[np.exp(-2j*np.pi*((chi[0]*v[0]+chi[1]*v[1])%d)/d)
                       for v in labels] for chi in labels])
    mats=np.array([weyl((n//d)*s,(n//d)*t,n) for s,t in labels])
    proj=np.einsum('ab,bij->aij',weights,mats)/(d*d)
    err=abs(proj.sum(axis=0)-np.eye(n)).max()
    identity=np.eye(d*d)
    # Products check the defining algebra without choosing a sector basis.
    for i,j in product(range(d*d),repeat=2):
        err=max(err,abs(proj[i]@proj[j]-identity[i,j]*proj[i]).max())
    err=max(err,abs(np.trace(proj,axis1=1,axis2=2)-n/(d*d)).max())
    for power in [0,1,3,n,n+1,2*n]:
        z=np.linalg.matrix_power(u,power)
        p=np.trace(z)
        zc=np.einsum('aij,ji->a',proj,z)
        zv=np.einsum('aij,ij->a',mats.conjugate(),z)/n
        energy=(abs(zc-p/(d*d))**2).sum()/n**2
        err=max(err,abs(energy-(abs(zv[1:])**2).sum()/(d*d)))
        cross=abs(zc.sum())**2-(abs(zc)**2).sum()
        err=max(err,abs(cross-((1-d**-2)*abs(p)**2-energy*n*n))/n**2)
    assert err<1e-12
    eigen, basis=schur(u,output='complex')
    phases=np.angle(eigen.diagonal())
    angles=phases[:,None]-phases[None,:]
    packet=np.array([basis.conjugate().T@v@basis/np.sqrt(n) for v in mats[1:]])
    flat=packet.reshape(len(packet),-1).T
    angles=angles.reshape(-1)
    gaps=[]
    max_filter_error=0.
    for theta in [0,.19,1.3,-2.11]:
        coefficients=np.exp(1j*(angles[:,None]-theta)*np.arange(ell)).mean(axis=1)
        filter_sq=np.linalg.norm(coefficients[:,None]*flat,ord=2)**2
        compression=np.max([np.linalg.norm(flat.conj().T@(
            np.exp(1j*angles*j)[:,None]*flat),ord=2) for j in range(1,ell)])
        sector=abs(np.angle(np.exp(1j*(angles-theta))))<=1/ell
        sector_sq=np.linalg.norm(flat[sector],ord=2)**2
        max_filter_error=max(max_filter_error,filter_sq-1/ell-compression,
                             sector_sq*np.cos(1)**2-filter_sq)
        gaps.append(float(sector_sq))
    assert max_filter_error<1e-12
    return dict(N=n,d=d,filter_length=ell,identity_error=float(err),
                filter_violation=float(max_filter_error),projector_norms_squared=gaps)

def linear_return_checks():
    exact = 0
    for exponent in range(2,13):
        n = 7**exponent
        modulus = n*7
        def multiple(x,y):
            return tuple(tuple(sum(x[i][k]*y[k][j] for k in range(2))%modulus
                               for j in range(2)) for i in range(2))
        for a in range(1,exponent):
            for u in (1,2,6,8,49+3):
                power=3*u*7**(exponent-a-1)
                result=((1,0),(0,1))
                base=((3,4),(2,3))
                while power:
                    if power&1:
                        result=multiple(result,base)
                    base=multiple(base,base)
                    power//=2
                difference=[[result[i][j] - (i==j) for j in range(2)] for i in range(2)]
                scale=7**(exponent-a)
                assert all(v%scale==0 for row in difference for v in row)
                quot=[[v//scale for v in row] for row in difference]
                assert (quot[0][0]*quot[1][1]-quot[0][1]*quot[1][0])%7!=0
                exact+=1
    checks=[]
    for n,s,torsion in ((49,3,7),(343,3,49),(343,21,7)):
        x,y=np.indices((n,n))
        matrix=np.exp(2j*np.pi*((-pow(8,-1,n)*(3*x*x-2*x*y+3*y*y))%n)/n)/np.sqrt(n)
        power=np.linalg.matrix_power(matrix,s)
        shifts=np.arange(n)
        weights=abs(np.fft.fft(power[x,(x+y)%n],axis=0).T)/n
        valid=(shifts%(n//torsion)==0)
        want=(valid[:,None]&valid[None,:])/torsion
        error=abs(weights-want).max()
        assert error<1e-11
        checks.append(dict(N=n,s=s,support=torsion**2,amplitude_error=float(error)))
    return exact,checks

def main():
    exact = sum(arithmetic_check(d,s) for d in (3,5,7,9,11) for s in (1,3,5))
    diagnostics = [sample(n,d,t) for n,d,t in ((9,3,4),(25,5,5),(49,7,6))]
    powers, linear=linear_return_checks()
    data=dict(exact_products=exact, exact_7_adic_orders=powers, diagnostics=diagnostics,
              linear_diagnostics=linear)
    if "--verify" in sys.argv:
        target=json.loads((Path(__file__).resolve().parent/'data/checks.json').read_text())
        assert exact == target['exact_products']
        assert powers == target['exact_7_adic_orders']
        for x,y in zip(linear,target['linear_diagnostics'],strict=True):
            assert (x['N'],x['s'],x['support']) == (y['N'],y['s'],y['support'])
        for x,y in zip(diagnostics,target['diagnostics'],strict=True):
            assert (x['N'],x['d'],x['filter_length']) == (y['N'],y['d'],y['filter_length'])
            assert np.max(np.abs(np.array(x['projector_norms_squared'])
                                 - np.array(y['projector_norms_squared']))) < 1e-11
        print('Arithmetic phases, sector identities and spectral filters verified.')
    else:
        print(json.dumps(data,indent=2))
if __name__=='__main__':
    main()
