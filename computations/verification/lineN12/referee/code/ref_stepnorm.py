"""Referee N12 [N]: spot-check of the stepnorm table N_H(t) = ||A(t)/s||_H via the generalized eigenproblem (A^*HA, H)
(independent of N12's Cholesky factor T), plus Lip_H-type finite differences and the near-0 quadratic coefficient."""
import os; os.environ.setdefault('OMP_NUM_THREADS','1')
import json, numpy as np, scipy.linalg as sl
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); H=z['H']; s=complex(z['s'])
c=np.load('/workspace/bgs-lineN/N12/logs/a_ops.npz',allow_pickle=True); NS=c['NS']; MS=c['MS']; W=c['COEF0']
def A(t): return np.tensordot(W*np.exp(2j*np.pi*NS*t),MS,1)/s
def NH(t):
    M=A(t); G=M.conj().T@H@M; G=(G+G.conj().T)/2
    return float(np.sqrt(sl.eigh(G,H,eigvals_only=True).max()))
tab=json.load(open('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45_stepnorm_NG4096.json'))['N_H']
rows=[]
for j in [1,2,4,16,64,256,512,588,1024,1536,2048]:
    t=j/4096; v=NH(t); rows.append(dict(t=t,NH_ref=v,NH_table=tab[j],diff=abs(v-tab[j]),quad_coef=(v-1)/t**2))
# max over a fine grid near the claimed max 0.1436
g=[NH(j/4096) for j in range(560,620,4)]
out=dict(rows=rows,max_near_01436=max(g))
print(json.dumps(out,indent=1)); json.dump(out,open('logs/ref_stepnorm.json','w'),indent=1)
