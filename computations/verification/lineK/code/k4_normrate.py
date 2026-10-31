"""K4 [N]: block-norm rates for the toy single-disc Galerkin twisted family L_tau (b=8, same as J3 lyap.py).
R_k := exp( E_{tau_1..tau_k iid U} log||L_{tau_k}...L_{tau_1}||_op / k ),  also (E||.||_HS^2)^{1/(2k)} and sup_tau ||L_tau||.
If R_k < 1.2836 for some k, then on any orbit tau_i = Tr(beta lam^i)/q whose k-tuples are equidistributed (BGK range, q <= p^C)
the product bound ||prod L_{tau_i}|| <= exp(p(log R_k + o(1))) beats the d=7 survivor; this is the order-free norm route."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import kick_ghat, MC, LAM
gh=kick_ghat('k1',2.0,10); K=40; RHO=2.6; c0=1/(LAM-1/LAM); C=-4*2*c0/8
Mn={n:gn*np.exp(2j*np.pi*C*n*n/2)*MC(n,C,RHO,K) for n,gn in gh.items() if abs(gn)>0}
G=1024; grid=np.arange(G)/G
Ls=np.array([sum(np.exp(2j*np.pi*n*t)*M for n,M in Mn.items()) for t in grid])
op=np.array([np.linalg.norm(L,2) for L in Ls]); hs=np.array([np.linalg.norm(L) for L in Ls])
res=dict(sup_op=float(op.max()),R1_op=float(np.exp(np.log(op).mean())),R1_hs2=float(np.sqrt((hs**2).mean())),spec_sup=1.84 )
print(res,flush=True)
rng=np.random.default_rng(11); rows=[]
for k in (2,3,4,6,8,12):
    N=3000; lo=[]; h2=[]
    for _ in range(N):
        P=np.eye(K,dtype=complex)
        for t in rng.integers(G,size=k): P=Ls[t]@P
        lo.append(np.log(np.linalg.norm(P,2))); h2.append(np.linalg.norm(P)**2)
    lo=np.array(lo); r=dict(k=k,R_op=float(np.exp(lo.mean()/k)),R_op_se=float(np.exp(lo.mean()/k)*lo.std()/np.sqrt(N)/k),R_hs2=float(np.mean(h2)**(1/(2*k))))
    rows.append(r); print(r,flush=True)
res['blocks']=rows; res['threshold']=1.2836
json.dump(res,open('logs/k4_normrate.json','w'),indent=1)
