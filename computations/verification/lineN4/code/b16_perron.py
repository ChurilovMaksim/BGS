"""N4 (B16) [N]: Perron root of the twist-uniform abs majorant M_B = sum_n |w_n| |B_n| (x) P_{B,n} (Schur test => inf_D ||D^-1 X(tau) D|| <= rho(M_B)).
usage: b16_perron.py typ K0 rho K N0 beta"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, C0
from scipy.special import jv
typ=sys.argv[1]; K0=int(sys.argv[2]); r=float(sys.argv[3]); K=int(sys.argv[4]); N0=int(sys.argv[5]); be=float(sys.argv[6])
J=json.load(open('/workspace/bgs-lineJ/J3/logs/blocks16_exact.json'))
acts={}
for case,v in J['cases'].items():
    for bi,bb in enumerate(v['blocks']): acts.setdefault(json.dumps(bb['act'],sort_keys=True),[]).append((case,bi))
B={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=be,coef=C0/2); X=V if typ=='V' else E
    if np.abs(X).max()>0: B[n]=np.abs(X)
w=lambda n: abs(jv(n,1.8))
S=sum(w(n)*Bn for n,Bn in B.items()); print('scalar abs majorant: norm',np.linalg.norm(S,2),'perron',max(abs(np.linalg.eigvals(S))))
mx=0
for key,members in acts.items():
    act=json.loads(key); M=sum(w(n)*np.kron(Bn, np.eye(2) if act[str(n%16)]['perm']==[0,1] else np.array([[0,1],[1,0]])) for n,Bn in B.items())
    pr=max(abs(np.linalg.eigvals(M))); mx=max(mx,pr)
print('max perron over blocks',mx)
