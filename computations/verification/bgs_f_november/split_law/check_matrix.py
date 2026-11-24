"""Independent matrix checks of the stationary response and phase displacement."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import eigvals

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, p_log, rho_at, split
from split_law.bgs_packet_check import SELECTED, data_at

P = 7
TAME_EXP = {pow(3,j,P):j%3 for j in range(6)}


def char_value(x,ell,h,k):
    return np.exp(2j*np.pi*(ell*p_log(x,k)%(P**k)/(P**k)+h*TAME_EXP[x%P]/3))


def pred(ell,h,k):
    values=np.zeros(2)
    for mode in SELECTED:
        phase,c,ratio,depth,_=data_at(mode,ell,k)
        if (k-depth)%2:
            gu=np.sum(np.exp(2j*np.pi*(c*np.arange(P)**2%P)/P))/np.sqrt(P)
        else:
            gu=1
        g=gu*np.exp(2j*np.pi*(phase/(P**k)+h*TAME_EXP[ratio]/3))
        coef=complex(*COEFFICIENTS[mode])/4000
        values+=2*(P/3)*P**(depth/2)*np.real(g*np.array([coef,np.conj(coef)]))
    return values


def matrices(k,full):
    n=P**k
    rho=rho_at(k)
    units=np.arange(n)%P!=0
    plus=np.isin(np.arange(n)%P,list(SQUARES))
    residues=np.arange(n)
    logs=np.array([p_log(int(x),k) if units[x] else 0 for x in residues])
    tame=np.array([TAME_EXP.get(x%P,0) for x in residues])
    modes=[]
    for v,(real,imag) in COEFFICIENTS.items():
        a,b=split(v,rho,n)
        y=(residues+a)%n
        w=(real+1j*imag)/4000*np.exp(2j*np.pi*((b*(residues+a*pow(2,-1,n)))%n)/n)
        modes.append((y,w))
    output={}
    for ell,h in product((3,10,17,24),range(3)):
        chi=np.exp(2j*np.pi*((ell*logs)%n/n+h*tame/3))
        chi/=np.sqrt(3*n/P)
        basis=np.stack((chi*plus,chi*(units&~plus)),axis=1)
        image=sum((w[:,None]*basis[y,:] for y,w in modes),np.zeros_like(basis))
        compression=np.sqrt(n)*(basis.conj().T@image)
        values=pred(ell,h,k)
        assert np.allclose(compression,np.diag(values),atol=2e-10)
        output[ell,h]=values
    if full:
        gamma=(3+2*rho)%n
        inv_gamma=pow(gamma,-1,n)
        A=np.zeros((n,n),complex)
        for y,w in modes:
            A[residues,y]+=w
        assert np.max(abs(A-A.conj().T))<1e-12
        # exp(itA) times the dilation in split coordinates, up to common phase.
        t=2e-6
        a,Q=np.linalg.eigh(A)
        exponential=(Q*np.exp(1j*t*a))@Q.conj().T
        backward=inv_gamma*residues%n
        M=np.eye(n)[backward]
        spectrum=eigvals(exponential@M)
        max_error=0.
        for (ell,h),values in output.items():
            node=char_value(inv_gamma,ell,h,k)
            angles=np.angle(spectrum/node)
            actual=np.sort(np.sqrt(n)*angles[np.argsort(abs(angles))[:2]]/t)
            max_error=max(max_error,float(np.max(abs(actual-np.sort(values)))))
        assert max_error<5e-4
        print("Maximum error in scaled true doublet displacement at N=343:",
              round(max_error,8))


if __name__=="__main__":
    matrices(3,True)
    matrices(4,False)
    print("Exact stationary-phase formulas match direct compressions at N=343 and N=2401.")
