"""N11b [N]: unit-gas per-site activity Lambda_U = sum over beta-classes mod lam^Z (both signs, both conjugates = distinct points) of r(beta),
from a_unit_single_p{p}.json; canonical rep = min a^2+2b^2 over lam^{+-k}.  Also A_U = sum |r|, and shell-by-|N| breakdown."""
import json,sys
p=int(sys.argv[1]); D=json.load(open(f'logs/a_unit_single_p{p}.json'))
def can(a,b):
    best=(a*a+2*b*b,a,b); x,y=a,b
    for _ in range(12): x,y=3*x+4*y,2*x+3*y; best=min(best,(x*x+2*y*y,x,y))
    x,y=a,b
    for _ in range(12): x,y=3*x-4*y,-2*x+3*y; best=min(best,(x*x+2*y*y,x,y))
    return best[1:]
cls={}
for row in D['rows']:
    c=can(*row['beta']); cls.setdefault(c,(row['N'],complex(*row['r'])))
L=sum(v[1] for v in cls.values()); A=sum(abs(v[1]) for v in cls.values())
sh={}
for c,(N,r) in cls.items(): s=sh.setdefault(abs(N),[0,0j,0.0]); s[0]+=1; s[1]+=r; s[2]+=abs(r)
top=sorted(cls.items(),key=lambda kv:-abs(kv[1][1]))[:12]
res=dict(p=p,nclasses=len(cls),LambdaU=[L.real,L.imag],absLambdaU=abs(L),AU=A,
  shells={k:dict(n=v[0],sum=[v[1].real,v[1].imag],abs=v[2]) for k,v in sorted(sh.items())},
  top=[dict(beta=list(c),N=v[0],r=[v[1].real,v[1].imag]) for c,v in top])
print(json.dumps(res,indent=0)[:3000]); json.dump(res,open(f'logs/c_LambdaU_p{p}.json','w'),indent=1)
