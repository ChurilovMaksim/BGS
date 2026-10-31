"""Line L, check of the L2-unitarity identities [N]:
 (U0) sum_{x in O} |A(x)|^2 = 1,  A(x) = sum_{alpha_n = x} w(n),  w(n) = Phihat(n) e(-nu0 P(n)/2h)
 (Uh) sum_{c in O/h} |A(c)|^2 = 1   (equivalently sum_{beta mod h} |Zhat(beta/h)|^2 = h^2)
 and the level-q values sum_{c in O/q}|A(c)|^2 for q | h.
Brute force over |n_j| <= L (truncation error ~ 1 - (sum_{|n|<=L}|J_n|^2)^m)."""
import sys, math, itertools, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata, pell
from scipy.special import jv
m=int(sys.argv[1]); L=int(sys.argv[2]); nu0=int(sys.argv[3]) if len(sys.argv)>3 else None
d=mdata(m); h=d['h']; yp=d['yp']; M=2*h
if nu0 is None:
    # resonant (2,8): 8 nu = 2 mod 2h, nu odd unit
    nu0=next(x for x in range(1,M,2) if (8*x-2)%M==0)
xs=[pell(k) for k in range(m)]
psi=[yp*xs[k][0]-2*h*xs[k][1] for k in range(m)]
gh={n:(1j**n)*jv(n,1.8) for n in range(-L,L+1)}
# lambda^i = X_i + Y_i sqrt2 : pell gives x_d + 2 y_d sqrt2 -> (X,Y)=(x_d, 2 y_d)
lamc=[(xs[k][0],2*xs[k][1]) for k in range(m)]
A={}
tot2=0.0
for n in itertools.product(range(-L,L+1),repeat=m):
    P=sum(psi[abs(i-j)]*n[i]*n[j] for i in range(m) for j in range(m))
    w=np.prod([gh[t] for t in n])*np.exp(-2j*np.pi*((nu0*P)%M)/M)
    a=sum(n[i]*lamc[i][0] for i in range(m)); b=sum(n[i]*lamc[i][1] for i in range(m))
    A[(a,b)]=A.get((a,b),0)+w
    tot2+=abs(w)**2
Z=sum(A.values())
U0=sum(abs(v)**2 for v in A.values())
print(f"m={m} h={h} nu0={nu0} L={L} sum|w|^2={tot2:.12f} |Z|^2={abs(Z)**2:.6e}")
print(f"U0 = sum_x |A(x)|^2 = {U0:.12f}")
def lev(q):
    B={}
    for (a,b),v in A.items():
        k=(a%q,b%q); B[k]=B.get(k,0)+v
    return sum(abs(v)**2 for v in B.values())
divs=[q for q in range(2,h+1) if h%q==0]
for q in divs:
    s=lev(q); print(f"level q={q}: sum_c|A(c mod q)|^2 = {s:.12f}   |Z|^2/q^2={abs(Z)**2/q**2:.6e}")
