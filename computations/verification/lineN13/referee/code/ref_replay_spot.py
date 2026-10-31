"""Referee spot-check of N13 c_replay.jsonl: recompute selected windows in float (numpy, a_ops cache = N6 cert_core, verified earlier)
with own twist generation (mpmath, 50 digits) and own seed algebra; check float r lies inside (or within 1e-12 of) the stored arb box."""
import sys, json, numpy as np, mpmath as mp
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
mp.mp.dps=50
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); s=complex(z['s']); Phi=z['Phi'].astype(complex); psi=z['psi'].astype(complex)
S2=mp.sqrt(2); LAM=3+2*S2; KK=18
def red(x): return x-mp.floor(x+mp.mpf(1)/2)
def window(ea,eb):
    zA=(mp.mpf(2*eb)/8,mp.mpf(ea)/8); fu=-ea+2*eb; fv=ea-eb; zB=(-mp.mpf(2*fv)/8,-mp.mpf(fu)/8); out=[]
    for zu,zv in (zA,zB):
        e1=zu+zv*S2; e2=zu-zv*S2
        L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(LAM))))
        v=Phi.copy()
        for j in range(-(KK+L1),KK+L2+1):
            d=red(e1*LAM**j) if j<=0 else red(-e2*LAM**(-j))
            v=A.Amat(float(d))@v/s
        out.append(complex(psi@v/(psi@Phi)))
    return out
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N13/logs/c_replay.jsonl')]
pick=[r for r in rows if r['k'] in (0,3,5,9)]+[r for r in rows if r['kind']=='pair' and r['name']=='odd+odd' and r['G'] in (3,4,9,15)][:8]+[r for r in rows if r['kind']=='pair' and r['name']!='odd+odd'][:3]
res=[]
for r in pick:
    w=window(*r['e']); rec=dict(k=r['k'],kind=r['kind'],name=r['name'],h=r['h'],s=r['s'],G=r['G'])
    for lab,x in zip('AB',w):
        b=r[lab]; inside=(b['re'][0]-1e-12<=x.real<=b['re'][1]+1e-12) and (b['im'][0]-1e-12<=x.imag<=b['im'][1]+1e-12)
        rec[lab]=dict(float=[x.real,x.imag],inside=inside,rad=b['rad'])
    res.append(rec); print(rec,flush=True)
json.dump(res,open('logs/ref_replay_spot.json','w'),indent=1)
print('ALL_INSIDE',all(r['A']['inside'] and r['B']['inside'] for r in res))
