"""N11b [N]: k-block norms g_k in v~=Tv along the top periodic orbits of N9b a_per (outside closed theta-box), k = multiples of n up to 48.
Shows the transient overhead of the adapted norm vs the true orbit rate (rate = lower bound for Gamma_out)."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
TH=float(sys.argv[1])
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); T=z['T']; s=complex(z['s']); Ti=np.linalg.inv(T)
TM=np.array([T@Mk@Ti for Mk in A.MS])/s
M=lambda t: np.tensordot(A.COEF0*np.exp(2j*np.pi*A.NS*t),TM,1)
out=[]
for l in open('/workspace/bgs-lineN/N9b/logs/a_per_a4.jsonl'):
    o=json.loads(l); n=o['n']
    for t in o['top']:
        if t[1]<=TH: continue
        x0,x1,D=t[3]; taus=[]
        for _ in range(n): taus.append(x0/D); x0,x1=x1,(6*x1-x0)%D
        Ms=[M(x) for x in taus]; ev=np.linalg.eigvals(np.linalg.multi_dot(Ms[::-1]) if n>1 else Ms[0]); row_rate495=abs(s)*abs(ev).max()**(1/n); P=np.eye(495,dtype=complex); row=dict(n=n,rate=t[0],rate_N12op=row_rate495,dist=t[1],taus=taus,g={})
        for k in range(1,49):
            P=Ms[(k-1)%len(Ms)]@P
            if k in (1,2,4,8,12,16,24,32,48): row['g'][k]=abs(s)*np.linalg.norm(P,2)**(1/k)
        out.append(row); print(n,round(t[0],4),round(row_rate495,4),t[1],{k:round(v,4) for k,v in row['g'].items()},flush=True)
        if sum(1 for r in out if r['n']==n)>=3: break
json.dump(out,open(f'logs/g_D1perorb_H_th{TH}.json','w'),indent=1)
