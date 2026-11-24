"""Independent finite-matrix check of both averaged Fourier trace identities."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from spectrum.bgs_packet_check import rho_at, split

N = 49
M = 21
RHO = rho_at(2)
GAMMA = (3+2*RHO)%N
INVERSE_TWO = pow(2,-1,N)


def linear_basis():
    seen = set()
    columns = []
    indices = []
    for start in range(N):
        if start in seen:
            continue
        orbit = []
        x = start
        while x not in seen:
            orbit.append(x)
            seen.add(x)
            x = GAMMA*x%N
        for j in range(len(orbit)):
            column = np.zeros(N,complex)
            column[orbit] = np.exp(-2j*np.pi*j*np.arange(len(orbit))/len(orbit))/np.sqrt(len(orbit))
            columns.append(column)
            indices.append(j*M//len(orbit))
    return np.array(columns).T, np.array(indices)


def weyl(label):
    a,b = label
    x = np.arange(N)
    out = np.zeros((N,N),complex)
    out[x,(x+a)%N] = np.exp(2j*np.pi*((b*(x+a*INVERSE_TWO))%N)/N)
    return out


def trace_word(word):
    summand_a = summand_b = phase = 0
    for (a,b),time in word:
        a = a*pow(GAMMA,time,N)%N
        b = b*pow(GAMMA,-time,N)%N
        phase = (phase+INVERSE_TWO*(summand_a*b-summand_b*a))%N
        summand_a = (summand_a+a)%N
        summand_b = (summand_b+b)%N
    return 0 if summand_a or summand_b else N*np.exp(2j*np.pi*phase/N)


def neg(label):
    return -label[0],-label[1]


def fourier(lhs, rhs, label1, label2, paired):
    lf, rf = np.fft.fft(lhs), np.fft.fft(rhs)
    rfstar = np.fft.fft(np.conj(rhs))
    if paired:
        operators = (label1, label2, neg(label2), neg(label1))
    else:
        operators = (label1, neg(label1), label1, neg(label1))
    output = 0j
    for a,b,c in product(range(M),repeat=3):
        d = (-a-b-c)%M
        t = trace_word(zip(operators,(0,a,a+b,a+b+c)))
        if paired:
            wt = rf[a]*lf[b]*rfstar[c]*lf[d]
        else:
            wt = lf[a]*lf[b]*lf[c]*lf[d]
        output += wt*t
    return output/M**4


def direct(lhs,rhs,basis,phase_indices,label1,label2,paired):
    a = basis.conj().T@weyl(label1)@basis
    b = basis.conj().T@weyl(label2)@basis
    norms = []
    for j in range(M):
        diagonal = np.sqrt(lhs[(phase_indices-j)%M])
        if paired:
            f = rhs[(phase_indices-j)%M]
            matrix = diagonal[:,None]*((a*f[None,:])@b)*diagonal[None,:]
            norms.append(np.linalg.norm(matrix,'fro')**2)
        else:
            matrix = diagonal[:,None]*a*diagonal[None,:]
            squares = matrix.conj().T@matrix
            norms.append(np.linalg.norm(squares,'fro')**2)
    return float(np.mean(norms))


if __name__ == "__main__":
    basis, phases = linear_basis()
    rad = 0.4
    d = np.arange(M)
    distance = np.minimum(d,M-d)
    positive = np.where(d==0,1/rad,1/(2*M*np.sin(np.pi*distance/M)-rad))
    near = np.where(distance<=3,positive,0)
    far = np.zeros(M,complex)
    support = distance>3
    far[support] = 1/(M*(1-np.exp(-2j*np.pi*d[support]/M)))
    labels = [split(v,RHO,N) for v in [(0,1),(0,7),(1,0)]]
    for x in labels:
        assert np.allclose(direct(near,far,basis,phases,x,x,False),
                           fourier(near,far,x,x,False),rtol=1e-10,atol=1e-12)
    for x,y in product(labels,repeat=2):
        assert np.allclose(direct(near,far,basis,phases,x,y,True),
                           fourier(near,far,x,y,True),rtol=1e-10,atol=1e-12)
    print("The fourth Schatten moment and signed quadratic identity match direct matrices at N=49.")
