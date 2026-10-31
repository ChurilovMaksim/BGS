"""[N] (±2,16) automaton (G2 law, b=16): commutant isotypics, rank-1 sectors f with A_n f = a(n) f, c = <f|e0><u|f>."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach
m=int(sys.argv[1]); a=int(sys.argv[2]); b=16
P=g2params(m,a,b); idx,tg=reach(P,80); NS=len(idx); pos={s:j for j,s in enumerate(idx)}
print('params',P,'NS',NS)
def Amat(n):
    A=np.zeros((NS,NS),complex)
    for s in idx:
        u=s//b; ph=(P['k']*((P['psi0']*n*n+2*n*u)%b))%b; A[pos[tg(s,n)],pos[s]]+=np.exp(-2j*np.pi*ph/b)
    return A
As=[Amat(n) for n in range(b)]
assert all(np.allclose(Amat(n),As[n%b]) for n in range(-20,21))
I=np.eye(NS); G=np.zeros((NS*NS,NS*NS),complex)
for A in As:
    Mx=np.kron(I,A)-np.kron(A.T,I); G+=Mx.conj().T@Mx
w,v=np.linalg.eigh(G); null=v[:,w<1e-8]; print('commutant dim',null.shape[1])
Ys=[null[:,i].reshape(NS,NS,order='F') for i in range(null.shape[1])]
rng=np.random.default_rng(1); Y=sum(rng.normal()*Yi for Yi in Ys); Y=Y+Y.conj().T
ew,ev=np.linalg.eigh(Y); cl=[]
for i,z in enumerate(ew):
    if cl and abs(ew[cl[-1][0]]-z)<1e-6: cl[-1].append(i)
    else: cl.append([i])
u=np.ones(NS); e0=np.zeros(NS); e0[pos[0]]=1; tot=0
for c in cl:
    F=ev[:,c]; E=F@F.conj().T; cchi=np.vdot(u,E@e0); tot+=cchi
    s='rank %d |c|=%.6f'%(len(c),abs(cchi))
    if len(c)==1:
        f=F[:,0]; an=[np.vdot(f,As[n]@f) for n in range(b)]
        res=max(np.linalg.norm(As[n]@f-an[n]*f) for n in range(b))
        s+=' eig-res %.1e a(n)*16/2pi: %s'%(res,[round((np.angle(x)/(2*np.pi))%1*b,4) for x in an])
    print(s)
print('sum c',tot)
