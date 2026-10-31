"""N2 (C3) [N]: unconstrained JSR proxy of the 1-parameter family {L_tau : tau in R/Z} (lifted V operator, sector 0):
beam search over twist sequences tau_i in (1/NT)Z, keep top-B products by norm; report max ||prod||^{1/k};
compare with max_tau rho(L_tau).  usage: c3_free_jsr.py K0 r K beta N0 NT B kmax"""
import sys, math, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
K0=int(sys.argv[1]); r=float(sys.argv[2]); K=int(sys.argv[3]); beta=float(sys.argv[4]); N0=int(sys.argv[5])
NT=int(sys.argv[6]); B=int(sys.argv[7]); kmax=int(sys.argv[8])
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns])
w0=wk1(2.0,0); w=np.array([w0(int(n)) for n in ns])
Ls=[np.tensordot(w*np.exp(2j*np.pi*ns*t/NT),Bst,axes=1) for t in range(NT)]
rhos=[float(max(abs(np.linalg.eigvals(L)))) for L in Ls]
print(json.dumps(dict(max_rho_tau=max(rhos),argmax=int(np.argmax(rhos)),rhos=[round(x,4) for x in rhos])),flush=True)
beam=[(1.0,np.eye(Ls[0].shape[0],dtype=complex),())]
out=[]
for k in range(1,kmax+1):
    cand=[]
    for _,P,seq in beam:
        for t in range(NT):
            Q=Ls[t]@P; cand.append((float(np.linalg.norm(Q,2)),Q,seq+(t,)))
    cand.sort(key=lambda c:-c[0]); beam=cand[:B]
    const=float(np.linalg.norm(np.linalg.matrix_power(Ls[NT//2],k),2))**(1/k)
    out.append(dict(k=k,free_sup=beam[0][0]**(1/k),const_half=const,seq=beam[0][2][-12:]))
    print(json.dumps(out[-1]),flush=True)
json.dump(dict(rhos=rhos,beam=out),open(f'logs/c3_free_jsr_K0{K0}_r{r}_K{K}_NT{NT}_B{B}.json','w'),indent=1)
