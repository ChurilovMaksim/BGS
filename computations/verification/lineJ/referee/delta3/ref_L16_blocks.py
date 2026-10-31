"""Referee check of Lemma L16 step 4 on the AUTHOR's blocks16_exact.json (float, entries are 16th roots of unity):
(i) A_n F_B = F_B Y_{B,n} for all n mod 16 (invariance + stored action), (ii) blocks mutually orthogonal, (iii) u in span,
(iv) J_B recomputed independently as G^-1 F^* e0 alpha^* G equals the stored J (coordinate form), (v) coordinate ||J_B||_2 <= 1/2."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach
J=json.load(open('/workspace/bgs-lineJ/J3/logs/blocks16_exact.json'))['cases']; b=16; z=lambda e: np.exp(2j*np.pi*e/16)
def zc(v): return complex(sum(v[i]*z(i) for i in range(8)))
W=dict(inv=0,orth=0,uspan=0,J=0); Jmax=0
for key,C in J.items():
    m,a=map(int,key.split(',')); P=g2params(m,a,b); idx,tg=reach(P,80); NS=len(idx); pos={s:j for j,s in enumerate(idx)}
    An=[]
    for n in range(b):
        A=np.zeros((NS,NS),complex)
        for s in idx:
            u=s//b; ph=(P['k']*((P['psi0']*n*n+2*n*u)%b))%b; A[pos[tg(s,n)],pos[s]]=np.exp(-2j*np.pi*ph/b)
        An.append(A)
    Fs=[]
    for B in C['blocks']:
        F=np.zeros((NS,2),complex)
        for c,f in enumerate((B['f1'],B['f2'])):
            for s,e in f.items(): F[int(s),c]=z(e)
        Fs.append(F)
        for n in range(16):
            act=B['act'][str(n)]; Y=np.zeros((2,2),complex)
            for i in (0,1): Y[act['perm'][i],i]=z(act['exps'][i])
            W['inv']=max(W['inv'],np.abs(An[n]@F-F@Y).max())
    Fall=np.hstack(Fs); G=Fall.conj().T@Fall; W['orth']=max(W['orth'],np.abs(G-np.diag(np.diag(G))).max())
    uu=np.ones(NS); e0=np.zeros(NS); e0[0]=1
    coef=np.linalg.solve(G,Fall.conj().T@uu); W['uspan']=max(W['uspan'],np.abs(Fall@coef-uu).max())
    for k,(B,F) in enumerate(zip(C['blocks'],Fs)):
        Gb=F.conj().T@F; al=coef[2*k:2*k+2]
        Jr=np.linalg.inv(Gb)@F.conj().T@np.outer(e0,al.conj())@Gb   # tr(Y J) = <u_B|A P_B e0>
        Js=np.array([[zc(B['J_times_nrm'][j][kk])/C['norm2'] for kk in range(2)] for j in range(2)])
        W['J']=max(W['J'],np.abs(Jr-Js).max()); Jmax=max(Jmax,np.linalg.norm(Js,2))
print('max errors',W,'max coordinate ||J_B||_2',Jmax)
print('PASS' if max(W.values())<1e-10 and Jmax<=0.5+1e-12 else 'FAIL')
