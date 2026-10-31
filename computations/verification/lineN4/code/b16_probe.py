"""N4 (B16) [N]: (+-2,16) families, Line F space.  Twist-uniform majorant: ||sum_n w_n e(n tau) B_n (x) A_{B,n}|| <= || sum_n |w_n| |B_n| (x) P_{B,n} ||
(entrywise absolute values; A_{B,n} monomial with unimodular entries, P its permutation pattern; |B_n| entrywise abs of the Galerkin block,
which does not depend on the sign of the multiplier coefficient C = -4 a c0/16).  Also reports the plain twisted norm max over tau (R=I)
for a few blocks, and the untwisted spectral radius.  usage: b16_probe.py typ K0 rho K N0"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, C0
from scipy.special import jv
typ=sys.argv[1]; K0=int(sys.argv[2]); r=float(sys.argv[3]); K=int(sys.argv[4]); N0=int(sys.argv[5])
J=json.load(open('/workspace/bgs-lineJ/J3/logs/blocks16_exact.json'))
acts={}
for case,v in J['cases'].items():
    for bi,bb in enumerate(v['blocks']): acts.setdefault(json.dumps(bb['act'],sort_keys=True),[]).append((case,bi))
B={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=0.0,coef=C0/2); X=V if typ=='V' else E
    if np.abs(X).max()>0: B[n]=X
w=lambda n: abs(jv(n,1.8))
res=[]
for key,members in acts.items():
    act=json.loads(key); d=list(B.values())[0].shape[0]
    M=np.zeros((2*d,2*d))
    for n,Bn in B.items():
        P=np.eye(2) if act[str(n%16)]['perm']==[0,1] else np.array([[0,1],[1,0]])
        M+=w(n)*np.kron(np.abs(Bn),P)   # ordering: lattice (x) internal
    nrm=float(np.linalg.norm(M,2)); res.append(dict(members=members[:3],abs_majorant=nrm))
    print(json.dumps(res[-1]),flush=True)
out=dict(typ=typ,K0=K0,rho=r,K=K,N0=N0,max_abs_majorant=max(x['abs_majorant'] for x in res),res=res)
json.dump(out,open(f'logs/b16_probe_{typ}_K0{K0}_K{K}.json','w'),indent=1); print('MAX',out['max_abs_majorant'])
