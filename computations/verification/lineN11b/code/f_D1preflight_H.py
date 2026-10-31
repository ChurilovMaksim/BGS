"""N11b [N]: D1 pre-flight in the N12 adapted coordinates v~ = T v (steering 2026-11-01): k-block norms
  g_k(y) = |s| * || prod_{i<k} T A(tau_i) T^{-1}/s ||_2^{1/k}
for random twist-pair points y whose k-step orbit avoids the CLOSED theta-box of (0,0) (sector-4 convention, as N9b a_per),
plus the same along the max periodic orbits.  A rigorous k-block D1 needs sup over ALL cells (+Lipschitz add-on); this is a scaled sample.
usage: f_D1preflight_H.py NS theta"""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
NS=int(sys.argv[1]); TH=float(sys.argv[2]); KS=(1,2,4,8,12,16)
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); T=z['T']; s=complex(z['s']); Ti=np.linalg.inv(T)
TM=np.array([T@Mk@Ti for Mk in A.MS])/s
M=lambda t: np.tensordot(A.COEF0*np.exp(2j*np.pi*A.NS*t),TM,1)
def td(x): x=x%1.0; return min(x,1-x)
inbox=lambda y: max(td(y[0]),td(y[1]))<=TH
step=lambda y: np.array([y[1],(6*y[1]-y[0])%1])
rng=np.random.default_rng(11); res={str(k):[] for k in KS}; t0=time.time(); worst={}
done=0
while done<NS:
    y=rng.random(2); orb=[y]
    for i in range(max(KS)): orb.append(step(orb[-1]))
    if any(inbox(o) for o in orb[:max(KS)+1]): continue
    P=np.eye(495,dtype=complex); kk=0
    for k in KS:
        while kk<k: P=M(orb[kk][0])@P; kk+=1
        g=abs(s)*np.linalg.norm(P,2)**(1/k); res[str(k)].append(g)
        if g>worst.get(str(k),(0,))[0]: worst[str(k)]=(g,list(y))
    done+=1
    if done%25==0: print(done,{k:round(max(v),4) for k,v in res.items()},round(time.time()-t0),flush=True)
out=dict(NS=NS,theta=TH,box='closed, (0,0) only, sector-4',max={k:max(v) for k,v in res.items()},median={k:float(np.median(v)) for k,v in res.items()},
         worst=worst,Tprime=1.4279,Gamma_per_1_8=1.2624)
print(json.dumps(out)); json.dump(out,open(f'logs/f_D1preflight_H_th{TH}.json','w'),indent=1)
