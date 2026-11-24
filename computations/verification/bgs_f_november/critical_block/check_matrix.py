"""Check the limiting-block building blocks against the finite matrices."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, p_log, rho_at, split
from split_law.bgs_packet_check import SELECTED
from split_law.check_matrix import TAME_EXP, char_value, pred
from critical_block.bgs_packet_check import common_phase, cross_phase, delta_at

P = 7
SITES = (0,1,3,7)


def predicted_cross(ell,h,k,gap):
    new_h=(h+gap)%3
    include_depth_one=gap%7 in (0,3,4)
    modes=SELECTED if include_depth_one else SELECTED[:3]
    output=np.zeros(2,complex)
    for mode in modes:
        depth=int(mode==(0,7))
        factors=[]
        for label in (mode,(-mode[0],-mode[1])):
            phase,c,x,y=cross_phase(label,ell,k,gap)
            gauss=(np.sum(np.exp(2j*np.pi*(c*np.arange(P)**2%P)/P))/np.sqrt(P)
                   if (k-depth)%2 else 1)
            tame=new_h*TAME_EXP[y%P]-h*TAME_EXP[x%P]
            factors.append(gauss*np.exp(2j*np.pi*(phase/P**k+tame/3)))
        omega=np.exp(2j*np.pi*(common_phase(ell,k,gap)/P**k+gap/3))
        assert np.allclose(factors[0]*factors[1],omega,atol=1e-11)
        c=complex(*COEFFICIENTS[mode])/4000
        coeff=np.array([c,np.conj(c)])
        output+=(P/3)*P**(depth/2)*(coeff*factors[0]+np.conj(coeff)*factors[1])
    return output


def check(k,check_cayley):
    n=P**k
    rho=rho_at(k)
    x=np.arange(n)
    units=x%P!=0
    plus=np.isin(x%P,list(SQUARES))
    logs=np.array([p_log(int(j),k) if units[j] else 0 for j in x])
    tame=np.array([TAME_EXP.get(j%P,0) for j in x])
    modes=[]
    for mode,(a,b) in COEFFICIENTS.items():
        shift,freq=split(mode,rho,n)
        target=(x+shift)%n
        mult=(a+1j*b)/4000*np.exp(2j*np.pi*((freq*(x+shift*pow(2,-1,n)))%n)/n)
        modes.append((target,mult))

    for ell,h in product((3,10,24),range(3)):
        basis=[]
        predicted=np.zeros((2*len(SITES),2*len(SITES)),complex)
        for i,r in enumerate(SITES):
            ll=ell+r*delta_at(k)
            hh=(h+r)%3
            chi=np.exp(2j*np.pi*((ll*logs)%n/n+hh*tame/3))/np.sqrt(3*n/P)
            basis.extend((chi*plus,chi*(units&~plus)))
            predicted[2*i:2*i+2,2*i:2*i+2]=np.diag(pred(ll,hh,k))
        for i,j in combinations(range(len(SITES)),2):
            r,s=SITES[i],SITES[j]
            pair=predicted_cross(ell+r*delta_at(k),(h+r)%3,k,s-r)
            predicted[2*i:2*i+2,2*j:2*j+2]=np.diag(pair)
            predicted[2*j:2*j+2,2*i:2*i+2]=np.diag(np.conj(pair))

        V=np.stack(basis,axis=1)
        assert np.allclose(V.conj().T@V,np.eye(V.shape[1]),atol=2e-12)
        applied=sum((mult[:,None]*V[target] for target,mult in modes),np.zeros_like(V))
        block=np.sqrt(n)*(V.conj().T@applied)
        assert np.allclose(block,predicted,atol=2e-10)

        # The gauge, computed directly from the common phase, makes each edge real.
        site_phase=np.array([np.exp(2j*np.pi*(common_phase(ell,k,r)/n+r/3))
                             for r in SITES])
        gauge=np.repeat(np.exp(-.5j*np.angle(site_phase)),2)
        real_block=np.conj(gauge[:,None])*block*gauge[None,:]
        assert np.max(abs(np.imag(real_block)))<1e-10

    if check_cayley:
        A=np.zeros((n,n),complex)
        for target,mult in modes:
            A[x,target]+=mult
        inv_gamma=pow((3+2*rho)%n,-1,n)
        M=np.eye(n)[inv_gamma*x%n]
        values,vecs=eigh(A)
        t=.6/np.sqrt(n)
        U=((vecs*np.exp(1j*t*values))@vecs.conj().T)@M
        T=(vecs*np.tan(.5*t*values))@vecs.conj().T
        z=char_value(inv_gamma,3,0,k)*np.exp(.137j/n)
        identity=np.eye(n)
        resolvent=np.linalg.inv(M+z*identity)
        lhs=(identity-1j*T)@(U-z*identity)@resolvent/1j
        rhs=((M-z*identity)@resolvent)/1j+T
        assert np.allclose(lhs,rhs,atol=2e-11)
        assert np.allclose(rhs,rhs.conj().T,atol=2e-11)

if __name__=="__main__":
    check(3,True)
    check(4,False)
    print("Four-site blocks, coherent real gauge, and exact Cayley identity agree with direct matrices.")
