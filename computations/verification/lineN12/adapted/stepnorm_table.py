"""Table of single-step adapted norms N_H(t) = ||A(t)/s||_H, t = j/NG (sector-4 total phase convention: slow at t=0;
sector a at twist tau equals this operator at t = tau + (a-4)/8, so every slow fixed twist b in {0,1/4,1/2,3/4} of the full Z
corresponds to t=0 for the sector a_b = 4-8b mod 8). Cell bound: sup_{|t-t_j|<=1/(2NG)} N_H <= N_H(t_j) + Lip_H/(2NG).
Usage: python stepnorm_table.py [NG=4096] [npz]."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
NG=int(sys.argv[1]) if len(sys.argv)>1 else 4096
f=sys.argv[2] if len(sys.argv)>2 else '/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'
z=np.load(f); T=z['T']; s=complex(z['s']); Ti=np.linalg.inv(T)
lip=json.load(open(f.replace('.npz','.json')))['Lip_H']
TM=np.array([T@Mk@Ti for Mk in A.MS])/s
tab=[]
for j in range(NG//2+1):
    t=j/NG; c=A.COEF0*np.exp(2j*np.pi*A.NS*t)
    tab.append(float(np.linalg.norm(np.tensordot(c,TM,1),2)))
    if j%256==0: print(j,t,tab[-1],flush=True)
json.dump(dict(NG=NG,Lip_H=lip,cell_add=lip/(2*NG),N_H=tab,note='symmetric: N_H(-t)=N_H(t) checked numerically at 1/8'),
          open(f.replace('.npz',f'_stepnorm_NG{NG}.json'),'w'))
