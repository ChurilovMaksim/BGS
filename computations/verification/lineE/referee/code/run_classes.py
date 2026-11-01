"""Run class sums for kick in {k1,full}, eta, list of m; save |Z(nu*)|^2, |Z(-nu*)|^2, F, and top residues."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import sys,time,json,numpy as np; sys.path.insert(0,'.')
from aud import *
kick=sys.argv[1]; eta=float(sys.argv[2]); ms=[int(x) for x in sys.argv[3].split(',')]
C=K1 if kick=='k1' else fullkick()
for m in ms:
    t0=time.time(); T=classes(C,eta,m); Z2=Zabs2_all(T,m); d=data(m); h=d['h']
    F=float(np.mean(list(Z2.values()))); ns=nustar(m); nm=nustar(m,-1)
    top=sorted(Z2.items(),key=lambda kv:-kv[1])[:6]
    toprep=[(nu,(pow(nu,-1,h)-h),z) for nu,z in top]     # second entry: N mod h, as negative offset
    r=dict(kick=kick,eta=eta,m=m,h=h,phi_units=len(Z2),F=F,F_over_2m=F/(2*m),Z2_nustar=Z2[ns],Z2_minus=Z2[nm],
           F_excl_pm=float((sum(Z2.values())-Z2[ns]-Z2[nm])/len(Z2)),top=[(int(a),int(b),float(c)) for a,b,c in toprep],secs=time.time()-t0)
    np.save(f'../logs/T_{kick}_eta{eta}_m{m}.npy',T)
    print(json.dumps(r),flush=True); open('../logs/classes.jsonl','a').write(json.dumps(r)+'\n')
