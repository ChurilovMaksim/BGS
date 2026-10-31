"""Referee float cross-check of N13 Lip_H, L2, Nsum (definitions: sum_n |w_4(n)| (2pi|n|)^k ||M_n||_H / |s|, k=1,2,0) and of the
claim that the certified c_n dominate the float H-norms of M_n."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); T=z['T']; Ti=np.linalg.inv(T); s=complex(z['s'])
B=json.load(open('/workspace/bgs-lineN/N13/logs/b_arb.json'))
NS=list(A.NS); C0=np.array(A.COEF0)   # COEF0 = w_4(n) (sector-4 weights)
nh={int(n):np.linalg.norm(T@M@Ti,2) for n,M in zip(NS,A.MS)}
w={int(n):abs(c) for n,c in zip(NS,C0)}
Lip=sum(w[n]*2*np.pi*abs(n)*nh[n] for n in nh)/abs(s); L2=sum(w[n]*(2*np.pi*n)**2*nh[n] for n in nh)/abs(s); Ns=sum(w[n]*nh[n] for n in nh)/abs(s)
dom=all(B['Mn_H'][str(n)]['c']>=nh[n]*(1-1e-9) for n in nh)
out=dict(Lip_float=Lip,L2_float=L2,Nsum_float=Ns,Lip_cert=B['Lip_H'],L2_cert=B['L2'],Nsum_cert=B['Nsum'],cn_dominate_float=dom,
         max_rel_cn_over_float=max(B['Mn_H'][str(n)]['c']/nh[n] for n in nh))
print(out); json.dump(out,open('logs/ref_lip_float.json','w'),indent=1)
