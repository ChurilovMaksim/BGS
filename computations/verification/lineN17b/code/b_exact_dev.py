"""N17b (2) [N, exact float data]: frozen TRACE-206 decomposition W'_m = phi^-1 sum_nonres(|Z|^2-RMT) + phi^-1 sum_{rho,d incl} Dev_d(rho)
(TRACE-213) from the exact all-unit |Z_m(nu)|^2 tables (Line E/G T arrays, k1 kick), per level d and primary rho, with level class.
Members: processed in increasing d (as Line I base.get): M_d = {nu: B nu == A mod 2h/d} minus earlier resonant. usage: b_exact_dev.py m..."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/audit/pr60/computations/verification/lineI/code')
from base import load_T, Z2_all, PSTAR
from law import mdata
from sympy import divisors, factorint
def hp_of(m):
    if m%3: return None
    p=m//3; x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
out=[]
for m in map(int,sys.argv[1:]):
    h=mdata(m)['h']; nu,Z=Z2_all(load_T('k1',m),m); phi=len(nu); RMT=4*m-m*m/h
    ds=[d for d in divisors(h) if 1<d and d*d<=h]; hp=hp_of(m)
    res=np.zeros(phi,bool); rows=[]; ResF=0.0
    for (A,B) in PSTAR['k1']:
        pidx=np.nonzero((B*nu-A)%(2*h)==0)[0]
        if len(pidx)==0: continue
        res[pidx]=True; Z0=Z[pidx[0]]; ResF+=Z0-RMT
        for d in ds:
            if Z0/d/d<4*m: rows.append(dict(rho=[A,B],d=d,included=False)); continue
            mem=((B*nu-A)%(2*h//d)==0)&~res; res|=mem; ResF+=mem.sum()*(Z0/d/d-RMT)
            dev=float((Z[mem]-Z0/d/d).sum()); floor=-mem.sum()*Z0/d/d
            cls=None
            if hp:
                cls='hp' if d==hp else ('hp-div' if hp%d==0 else ('inherited' if d%hp==0 else ('K' if (h//hp)%d==0 else 'mixed')))
            rows.append(dict(rho=[A,B],d=int(d),cls=cls,included=True,n_d=int(mem.sum()),Zrho2=float(Z0),Dev=dev,Dev_over_phim=dev/phi/m,
                             floor_over_phim=float(floor)/phi/m,mainterm_over_phim=float(mem.sum()*Z0/d/d)/phi/m))
    NR=float((Z[~res]-RMT).sum())/phi; F=float(Z.mean()); Resv=ResF/phi
    Wp=(F-RMT-Resv); Wsum=NR+sum(r['Dev'] for r in rows if r['included'])/phi
    r=dict(m=m,h=int(h),h_fac={str(k):v for k,v in factorint(h).items()},hp=hp,phi=phi,RMT=RMT,Wprime_over_m=Wp/m,
           check_decomp=(Wsum-Wp)/m,NR_over_m=NR/m,rows=rows)
    out.append(r)
    print(f"m={m} h={h} {factorint(h)} W'/m={Wp/m:+.4f} (decomp err {r['check_decomp']:.1e}) NR/m={NR/m:+.4f}",flush=True)
    for x in rows:
        if x['included']: print(f"   rho={x['rho']} d={x['d']:>7} {x['cls']} n_d={x['n_d']} Dev/(phi m)={x['Dev_over_phim']:+.4e} floor={x['floor_over_phim']:+.3e} main={x['mainterm_over_phim']:.3e}")
        else: print(f"   rho={x['rho']} d={x['d']} EXCLUDED")
json.dump(out,open('logs/b_exact_dev.json','w'),indent=1)
