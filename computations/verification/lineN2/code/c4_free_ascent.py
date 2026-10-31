"""N2 (C4) [N]: unconstrained JSR proxy: coordinate ascent of ||L_{tau_{k-1}}...L_{tau_0}||^{1/k} over arbitrary twist
sequences on (1/NT)Z, from several starts (constant 1/2, random). usage: c4_free_ascent.py K0 r K beta N0 NT k nstart"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
K0=int(sys.argv[1]); r=float(sys.argv[2]); K=int(sys.argv[3]); beta=float(sys.argv[4]); N0=int(sys.argv[5])
NT=int(sys.argv[6]); k=int(sys.argv[7]); nst=int(sys.argv[8])
Bn={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=beta); Bn[n]=V
ns=np.array(sorted(Bn)); Bst=np.stack([Bn[n] for n in ns]); w0=wk1(2.0,0); w=np.array([w0(int(n)) for n in ns])
Ls=np.stack([np.tensordot(w*np.exp(2j*np.pi*ns*t/NT),Bst,axes=1) for t in range(NT)]); d=Ls.shape[1]
def val(seq):
    P=np.eye(d,dtype=complex)
    for t in seq: P=Ls[t]@P
    return float(np.linalg.norm(P,2))**(1/k)
rng=np.random.default_rng(3); res=[]
starts=[[NT//2]*k]+[[int(x) for x in rng.integers(0,NT,k)] for _ in range(nst)]
for s in starts:
    seq=list(s); best=val(seq); imp=True; sweeps=0
    while imp and sweeps<6:
        imp=False; sweeps+=1
        for i in range(k):
            # prefix/suffix products for speed
            Pre=np.eye(d,dtype=complex)
            for t in seq[:i]: Pre=Ls[t]@Pre
            Suf=np.eye(d,dtype=complex)
            for t in seq[i+1:]: Suf=Ls[t]@Suf if False else Suf
            Suf=np.eye(d,dtype=complex)
            for t in seq[i+1:]: Suf=Ls[t]@Suf
            vals=[float(np.linalg.norm(Suf@Ls[t]@Pre,2))**(1/k) for t in range(NT)]
            tb=int(np.argmax(vals))
            if vals[tb]>best+1e-12: best=vals[tb]; seq[i]=tb; imp=True
    res.append(dict(start=('const' if s==starts[0] else 'rand'),val=best,seq=seq))
    print(json.dumps(res[-1]),flush=True)
json.dump(dict(k=k,NT=NT,res=res,const=val([NT//2]*k)),open(f'logs/c4_free_ascent_k{k}_NT{NT}.json','w'),indent=1)
