"""Untwisted 16-state automaton: commutant isotypics, rank-1 sector vectors f, scalars a_chi(n) = <f|A_n|f>, c_chi = <f|0><u|f>."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach, taus7, finite
m=int(sys.argv[1]); a=int(sys.argv[2])
P=g2params(m,a,8); idx,tg=reach(P,60); NS=len(idx)
print('params',P,'states',idx)
def Amat(n):
    A=np.zeros((NS,NS),complex)
    for (o,i,ph8,tw) in finite(P,idx,tg,n,None): A[o,i]+=np.exp(-2j*np.pi*ph8/8)
    return A
As=[Amat(n) for n in range(8)]
I=np.eye(NS); G=np.zeros((NS*NS,NS*NS),complex)
for A in As:
    Mx=np.kron(I,A)-np.kron(A.T,I); G+=Mx.conj().T@Mx
w,v=np.linalg.eigh(G); null=v[:,w<1e-9]; Ys=[null[:,i].reshape(NS,NS,order='F') for i in range(null.shape[1])]
rng=np.random.default_rng(1); Y=sum(rng.normal()*Yi for Yi in Ys); Y=(Y+Y.conj().T)  # hermitian generic element
ew,ev=np.linalg.eigh(Y)
cl=[]
for i,z in enumerate(ew):
    if cl and abs(ew[cl[-1][0]]-z)<1e-6: cl[-1].append(i)
    else: cl.append([i])
u=np.ones(NS)
for c in cl:
    F=ev[:,c]; E=F@F.conj().T
    cchi=np.trace(E@np.outer(np.eye(NS)[0],u))
    s='rank %d c=%s'%(len(c),np.round(cchi,12))
    if len(c)==1:
        f=F[:,0]; f=f/f[np.argmax(abs(f))]*abs(f[np.argmax(abs(f))])
        an=[complex(np.vdot(f,As[n]@f)) for n in range(8)]
        s+=' a(n)/2pi: '+str([round((np.angle(x)/(2*np.pi))%1*8,6) for x in an])+' |a|'+str(round(min(abs(x) for x in an),12))
        s+='\n   f='+str(np.round(f*4,6).tolist())
    else:
        s+=' |E e0|=%.3g |E u|=%.3g'%(np.linalg.norm(E[:,0]),np.linalg.norm(E@u))
    print(s)
