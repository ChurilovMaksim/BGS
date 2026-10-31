"""N15 (2b) [N estimate]: vector-chain form of the core->true conversion.  Replaces the operator sub-product sup GA (which with
H-product bounds makes the N8 lemma vacuous: E ~ 0.03-38 per window, logs/conv_replay.jsonl) by forward/backward chain norms
f_k = ||prod_{<=k} X Phi~||, b_k = ||psi~ prod_{>k} X|| (first-order expansion of prod(X+E_k)):  
  E_est = [2 dPi (1+Xn/|s|) max_k b_k f_k  +  n Fs (1+Xn/|s|)^2 max_k b_k f_k] / |psi~.Phi~|   (higher orders O(Fs^2) negligible).
Not a proof: the lifted-operator (T0') bookkeeping of the N6 lemma must be redone in vector form."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F, digits as Dg
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); s=complex(z['s']); Phi=z['Phi'].astype(complex); psi=z['psi'].astype(complex)
N8=json.load(open('/workspace/bgs-lineN/N8/logs/n8_cert_fam.json')); dPi=N8['dPi']; Xn=N8['Xn']; Fs=N8['Pert']/abs(s); g=1+Xn/abs(s)
sc=F.s/s   # fastops normalises by its own s (equal to 1e-15)
def est(ds):
    v=Phi.copy(); fs=[np.linalg.norm(v)]
    for d in ds: v=F.step(v,d)*sc; fs.append(np.linalg.norm(v))
    w=psi.copy(); bs=[np.linalg.norm(w)]
    for d in reversed(ds): w=F.stepT(w,d)*sc; bs.append(np.linalg.norm(w))
    bs=bs[::-1]; m=max(fs[k]*bs[k] for k in range(len(fs)))
    return (2*dPi*g+len(ds)*Fs*g*g)*m/abs(psi@Phi), m
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/c2_mid.jsonl')]
out=[]
for r in rows:
    e=[]
    for zz in Dg.seeds(*r['e']): E,m=est(Dg.core(zz,18)); e.append((E,m))
    out.append(dict(k=r['k'],kind=r['kind'],name=r['name'],h=r['h'],s=r['s'],G=r['G'],EA=e[0][0],EB=e[1][0],mA=e[0][1],mB=e[1][1]))
json.dump(out,open('/workspace/bgs-lineN/N15/logs/conv_est.json','w'))
# effect on delta_int: widen c2_mid boxes by E_est and rerun the N14 f_post2 formulas
for r,o in zip(rows,out):
    for W,E in (('A',o['EA']),('B',o['EB'])):
        m=(sum(r[W]['re'])/2,sum(r[W]['im'])/2); R=r[W]['rad']+E; r[W]['re']=[m[0]-R,m[0]+R]; r[W]['im']=[m[1]-R,m[1]+R]
open('/workspace/bgs-lineN/N15/logs/c2_true_est.jsonl','w').write(''.join(json.dumps(r)+'\n' for r in rows))
print('singles E_A:',[('%s %.2e'%(o['name'],o['EA'])) for o in out[:10]]); print('max E over pairs %.2e'%max(max(o['EA'],o['EB']) for o in out))
