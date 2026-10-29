import sys, json, time, pickle
sys.path.insert(0,'/workspace/audit/lineC/code')
from sym import *
m=int(sys.argv[1]); maxk2=int(sys.argv[2]) if len(sys.argv)>2 else 2*m
t0=time.time()
terms,bydr=run_engine(m,0,maxk2,raw=True)
pickle.dump((terms,bydr),open(f'/workspace/audit/lineC/logs/sym_m{m}_k{maxk2}.pkl','wb'))
print(f"# m={m} maxk2={maxk2} time={time.time()-t0:.1f}s")
ex=expansion(terms)
for (k2,cls),dd in ex.items():
    if k2<=maxk2: print(f"p^-{k2/2:g} [p={cls} mod 4]: {fmt(dd)}")
print("# (d,r,D) decomposition (coefficient of p^-(d+r/2) eps^r (D/p))")
for k in sorted(bydr):
    if bydr[k]!=0: print("  ",k,bydr[k])
