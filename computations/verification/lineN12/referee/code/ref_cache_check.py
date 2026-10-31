"""Referee N12: check N12's float cache a_ops.npz (MS, COEF0, RAD) against the N6 cert_core arb blocks (read-only import)."""
import sys, json, time, numpy as np
t0=time.time()
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); import cert_core as C
c=np.load('/workspace/bgs-lineN/N12/logs/a_ops.npz',allow_pickle=True); NS=list(c['NS']); MS=c['MS']; COEF0=c['COEF0']
D=C.D; K=C.K; MSr=np.zeros_like(MS); rad=0.0
for (c2,n),(j2,Mx) in C.blocks.items():
    k=NS.index(n); i0=C.idx[c2]*K; j0=C.idx[j2]*K
    for i in range(K):
        for j in range(K):
            z=Mx[i,j]; MSr[k,i0+i,j0+j]+=complex(float(z.real.mid()),float(z.imag.mid())); rad=max(rad,float(z.real.rad())+float(z.imag.rad()))
wd=max(abs(complex(float(C.wa(4,int(n)).real.mid()),float(C.wa(4,int(n)).imag.mid()))-COEF0[k]) for k,n in enumerate(NS))
out=dict(max_abs_diff_MS=float(np.abs(MSr-MS).max()),RAD=rad,RAD_cache=float(c['RAD']),wdiff=float(wd),D=D,nblocks=len(C.blocks),secs=round(time.time()-t0))
print(json.dumps(out)); json.dump(out,open('logs/ref_cache_check.json','w'))
