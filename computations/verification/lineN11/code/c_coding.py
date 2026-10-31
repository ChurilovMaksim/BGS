"""N11 Lemma C (coding/injectivity of dilute bump configurations) -- explicit constants + exact numerical check.
Types T = {+-1, +-sqrt2, +-2, +-2sqrt2, +-4} (+ conjugate-closed). Positions in eps-units.
c_min = min |beta - beta' eps^{-s}| over (beta,0) != (beta',s), s>=0 (real embedding).
Uniqueness in O for gap>=g0:  c_min > 2 B eps^{-g0} / (1-eps^{-g0}).
Injectivity mod gammabar for |G|+|G'| <= p/G0:  B^2 (1/(1-1/eps))^2 eps^{-G0} < 1/2 (q > eps^p/2 - 1)."""
import math, itertools, random, json
eps=1+math.sqrt(2); B=4.0
T=[1,math.sqrt(2),2,2*math.sqrt(2),4]; T=T+[-t for t in T]
cmin=min(abs(b-bp*eps**(-s)) for b in T for bp in T for s in range(0,12) if not (s==0 and b==bp))
g0=next(g for g in range(1,50) if cmin>2*B*eps**(-g)/(1-eps**(-g)))
G0=next(G for G in range(1,50) if B*B*(1/(1-1/eps))**2*eps**(-G)<0.5)
out=dict(c_min=cmin,g0_eps=g0,G0_eps=G0)
# exact check: random dilute configurations on Z/p (eps-positions), compare residues mod gammabar (exact ints)
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
TY=[(1,0),(0,1),(2,0),(0,2),(4,0)]; TY=TY+[(-a,-b) for a,b in TY]
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
res={}
for p in [29,47,59]:
    k=(p-1)//2; q=xy(p)[0]; gb=(xy(k+1)[0],-xy(k)[1])   # gammabar
    N=gb[0]**2-2*gb[1]**2
    # residue map O -> Z/|N|: alpha -> a + b*s mod N where s = sqrt2 mod gammabar (s = -x/y * ... ) ; find s with s^2=2, gb(s)=0
    x0,y0=gb; inv=pow(y0,-1,abs(N)); s=(-x0*inv)%abs(N); assert (s*s-2)%abs(N)==0
    ep=[1]
    for i in range(2*p): ep.append(ep[-1]*(1+s)%abs(N))
    def resid(cfg): return sum(((a+b*s)*ep[n])%abs(N) for n,(a,b) in cfg)%abs(N)
    seen={}; coll=0; tried=0
    random.seed(p)
    nb=max(1,p//(2*G0))
    for trial in range(200000):
        n=random.randint(1,nb)
        pos=sorted(random.sample(range(p),n))
        if n>1 and min((pos[(i+1)%n]-pos[i])%p for i in range(n))<g0: continue
        cfg=tuple((ps,random.choice(TY)) for ps in pos); r=resid(cfg); tried+=1
        if r in seen and seen[r]!=cfg: coll+=1
        seen[r]=cfg
    res[p]=dict(q=abs(N),max_bumps=nb,configs_tested=tried,distinct=len(seen),collisions=coll)
out['exact_check']=res
print(json.dumps(out,indent=1)); json.dump(out,open('/workspace/bgs-lineN/N11/logs/c_coding.json','w'),indent=1)
