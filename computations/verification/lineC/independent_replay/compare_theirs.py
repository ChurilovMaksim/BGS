# Compare the report's expansion logs (parsed as data only; no code imported) with this audit's expansions,
# by exact evaluation at many primes. Their line format: "p^ k [eps*]( D/p) : coeff" meaning coeff*p^k*[eps]*(D/p),
# with eps*sqrt(p) = quadratic Gauss sum g (sqrt p or i sqrt p).
import sys, re, pickle
from fractions import Fraction as F
sys.path.insert(0,'/workspace/audit/lineC/code')
from sym import legendre, evaluate
def parse(path, m):
    blocks={}; cur=None
    for line in open(path):
        mm=re.match(r'^m=(\d+)',line)
        if mm: cur=int(mm.group(1)); blocks[cur]=[]; continue
        mm=re.match(r'^\s*p\^\s*(-?\d+(?:/2)?)\s*(eps\*)?\(\s*(-?\d+)/p\)\s*:\s*(-?\d+(?:/\d+)?)',line)
        if mm and cur is not None:
            k=F(mm.group(1)); blocks[cur].append((k, bool(mm.group(2)), int(mm.group(3)), F(mm.group(4))))
    return blocks.get(m)
def eval_theirs(terms,p,kmin=None):
    re_=F(0); sq=F(0); im=F(0)
    for k,eps,D,c in terms:
        if kmin is not None and k<kmin: continue
        chi=legendre(D,p); v=c*chi
        if not eps:
            assert k.denominator==1; re_+=v*F(p)**int(k)
        else:
            # p^k eps = p^(k-1/2) * (eps sqrt p) = p^(k-1/2) g
            e=k-F(1,2); assert e.denominator==1
            if p%4==1: sq+=v*F(p)**int(e)
            else: im+=v*F(p)**int(e)
    return re_,sq,im
primes=[q for q in range(101,1200) if all(q%d for d in range(2,int(q**.5)+1))]
src={3:'symbolic_m1_7.log',4:'symbolic_m1_7.log',5:'symbolic_m1_7.log',6:'symbolic_m1_7.log',7:'symbolic_m1_7.log',
     8:'engine_m8.log',9:'engine_m9.log',10:'engine_m10.log',11:'engine_m11_def2.log',12:'engine_m12_def2.log'}
for m,f in src.items():
    th=parse('/workspace/bgs-lineC/logs/'+f,m)
    if m<=10: mine,_=pickle.load(open(f'logs/sym_m{m}_k{2*m}.pkl','rb')); kmax2=None
    else: mine,_=pickle.load(open(f'logs/sym_m{m}_k5.pkl','rb')); kmax2=5
    ok=True
    for p in primes:
        a,b=evaluate(mine,p,maxk2=kmax2)
        r,s,i=eval_theirs(th,p,kmin=(F(-5,2) if kmax2 else None))
        if i!=0 or (a,b)!=(r,s): ok=False; print("DIFF",m,p,a,b,r,s,i); break
    print(f"m={m}: their expansion ({f}, {len(th)} terms) == audit expansion at {len(primes)} primes in [101,1200]{' (through p^-5/2)' if kmax2 else ' (all orders)'}: {ok}")
