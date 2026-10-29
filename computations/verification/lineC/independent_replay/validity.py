# For m=3..8: compare symbolic expansion (mode 0) evaluated at p with exact per-prime engine values,
# and with brute force for small cases; list primes where they differ.
import sys, pickle
sys.path.insert(0,'/workspace/audit/lineC/code')
from sym import *
from brute_exact import exact
def primes(a,b): return [q for q in range(a,b) if q>2 and all(q%d for d in range(2,int(q**.5)+1))]
for m in range(3,9):
    terms,_=pickle.load(open(f'/workspace/audit/lineC/logs/sym_m{m}_k{2*m}.pkl','rb'))
    bad=[]; checked=[]
    for p in primes(5, 260 if m<=7 else 140):
        try: s=evaluate(terms,p,symbolic=True)
        except ValueError: bad.append((p,'p|D')); continue
        e=evaluate(run_engine(m,p,2*m),p,symbolic=False)
        checked.append(p)
        if s!=e: bad.append(p)
    print(f"m={m}: symbolic == exact per-prime for all primes checked in [{checked[0]},{checked[-1]}] except {bad}", flush=True)
# brute force cross-checks at primes beyond the bad set
for (p,m) in [(19,5),(23,5),(29,5),(31,5),(19,6),(23,6),(29,6),(19,7),(23,7),(19,8)]:
    terms,_=pickle.load(open(f'/workspace/audit/lineC/logs/sym_m{m}_k{2*m}.pkl','rb'))
    b=exact(p,m); s=evaluate(terms,p)
    print(f"brute p={p} m={m}: E = {b[0]} + ({b[1]})sqrt(p) ; symbolic expansion equal: {b==s}", flush=True)
