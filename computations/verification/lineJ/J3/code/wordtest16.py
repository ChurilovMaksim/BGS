"""[N, float, 1e-12] random-word test of the (a,16) block read-out: <u|A_w|e0> (64-state automaton) = sum_B tr(A_{B,w} J_B), all 16 cases."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach
J=json.load(open('logs/blocks16_exact.json'))['cases']; b=16; rng=np.random.default_rng(1)
def zc(v): return complex(sum(v[i]*np.exp(2j*np.pi*i/16) for i in range(8)))
worst=0
for key,C in J.items():
    m,a=map(int,key.split(',')); P=g2params(m,a,b); idx,tg=reach(P,80); NS=len(idx); pos={s:j for j,s in enumerate(idx)}
    An=[]
    for n in range(b):
        A=np.zeros((NS,NS),complex)
        for s in idx:
            u=s//b; ph=(P['k']*((P['psi0']*n*n+2*n*u)%b))%b; A[pos[tg(s,n)],pos[s]]=np.exp(-2j*np.pi*ph/b)
        An.append(A)
    uu=np.ones(NS); e0=np.zeros(NS); e0[0]=1; nrm=C['norm2']
    def Bm(B,n):
        A=B['act'][str(n%16)]; M=np.zeros((2,2),complex)
        for i in (0,1): M[A['perm'][i],i]=np.exp(2j*np.pi*A['exps'][i]/16)
        return M
    for trial in range(200):
        w=rng.integers(-20,21,size=rng.integers(1,40))
        X=np.eye(NS)
        for n in w: X=An[n%16]@X
        full=uu@X@e0
        bl=0
        for B in C['blocks']:
            Y=np.eye(2)
            for n in w: Y=Bm(B,n)@Y
            Jm=np.array([[zc(B['J_times_nrm'][j][k])/nrm for k in range(2)] for j in range(2)])
            bl+=np.trace(Y@Jm)
        worst=max(worst,abs(full-bl))
    print(key,'worst so far',worst,flush=True)
print('MAX ABS DIFF',worst, 'PASS' if worst<1e-9 else 'FAIL')
