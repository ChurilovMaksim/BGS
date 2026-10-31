"""Commutant of the finite state factors {A_n} (16 reachable states x 3-cycle with d=7 twist); isotypic idempotents; E J E vs E."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach, taus7, finite
m=int(sys.argv[1]); a=int(sys.argv[2]); cls=sys.argv[3]
P=g2params(m,a,8); idx,tg=reach(P,60); cyc=None if cls=='none' else taus7(*[int(t) for t in cls.split(':')])
NS=len(idx)*(1 if cyc is None else 3)
def Amat(n):
    A=np.zeros((NS,NS),complex)
    for (o,i,ph8,tw) in finite(P,idx,tg,n,cyc): A[o,i]+=np.exp(-2j*np.pi*ph8/8)*np.exp(2j*np.pi*n*tw/7)
    return A
As=[Amat(n) for n in range(56)]
I=np.eye(NS); G=np.zeros((NS*NS,NS*NS),complex)
for A in As:
    Mx=np.kron(I,A)-np.kron(A.T,I); G+=Mx.conj().T@Mx
w,v=np.linalg.eigh(G); null=v[:,w<1e-9]
print('NS',NS,'commutant dim',null.shape[1])
Ys=[null[:,i].reshape(NS,NS,order='F') for i in range(null.shape[1])]
print('commutative? ',max(np.linalg.norm(X@Y-Y@X) for X in Ys for Y in Ys))
# simultaneous diagonalisation via random element
rng=np.random.default_rng(1); Y=sum(rng.normal()*Yi for Yi in Ys)
ew,ev=np.linalg.eig(Y)
# cluster eigenvalues
cl=[]
for i,z in enumerate(ew):
    for c in cl:
        if abs(ew[c[0]]-z)<1e-6: c.append(i); break
    else: cl.append([i])
J=np.zeros((NS,NS)); u=np.array([1.0 if (cyc is None or s%3==0) else 0 for s in range(NS)]); J[0,:]=u
print('clusters',[len(c) for c in cl])
for c in cl:
    # spectral idempotent for this cluster: E = sum over projections
    Vc=ev[:,c]; W=np.linalg.inv(ev)[c,:]; E=Vc@W
    EJE=E@J@E; tr=np.trace(E@J)
    # is EJE a multiple of E?
    lam=tr/np.trace(E); err=np.linalg.norm(EJE-lam*E)
    print('rank',len(c),'tr(EJ)',np.round(tr,12),'EJE-cE err',err)
