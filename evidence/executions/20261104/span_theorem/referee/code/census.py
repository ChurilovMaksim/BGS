# Independent exact census of the eps-digit span (auditor code; does not import PR code).
import math, json, sys, time
from math import isqrt
J=int(sys.argv[1]) if len(sys.argv)>1 else 16
def sgn(u,v):   # sign of u+v*sqrt2, exact
    if u>=0 and v>=0: return 0 if (u==0 and v==0) else 1
    if u<=0 and v<=0: return -1
    if u>0: return 1 if u*u>2*v*v else -1   # v<0
    return 1 if 2*v*v>u*u else -1           # u<0<v
def floor_s2(U,V):  # floor(U+V*sqrt2) exact
    if V==0: return U
    r=isqrt(2*V*V)  # 2V^2 never square for V!=0
    return U+(r if V>0 else -r-1)
def epspow(k):
    p,q=1,0
    if k>=0:
        for _ in range(k): p,q=p+2*q,p+q
    else:
        for _ in range(-k): p,q=-p+2*q,p-q
    return p,q
PW={}
def pw(k):
    if k not in PW: PW[k]=epspow(k)
    return PW[k]
def nk(a,b,k):
    p,q=pw(k); U=2*(b*p+a*q); V=a*p+2*b*q   # xi=(U+V s2)/4
    if k%2==0: return floor_s2(U+2,V)//4          # floor(xi+1/2)
    else: return -(floor_s2(2-U,-V)//4)          # -floor(1/2-xi)
def word(a,b):
    x1=a+b*math.sqrt(2); x2=a-b*math.sqrt(2); N=abs(a*a-2*b*b)
    kL=math.log(1/(2*abs(x1)*math.sqrt(2)/4))/math.log(1+math.sqrt(2))
    kR=math.log(2*abs(x2)*math.sqrt(2)/4)/math.log(1+math.sqrt(2))
    k0=math.floor(kL)-8; k1=math.ceil(kR)+8
    n={k:nk(a,b,k) for k in range(k0-2,k1+1)}
    # sanity on window edges: n=0 at left edge, n=T at right edge
    for k in range(k0-2,k0+1): assert n[k]==0,(a,b,k)
    for k in range(k1-2,k1+1):
        p,q=pw(k); assert n[k]==b*p+a*q,(a,b,k)
    E={k:n[k]-2*n[k-1]-n[k-2] for k in range(k0,k1+1)}
    nz=[k for k in sorted(E) if E[k]!=0]
    if not nz: return [],0,None
    w=[E[k] for k in range(nz[0],nz[-1]+1)]
    zr=max([y-x-1 for x,y in zip(nz,nz[1:])],default=0)
    return w,zr,nz[0]
def floorlog(N):  # floor(log_eps(N/2)) exact: largest m with eps^m <= N/2 ; i.e. 2*eps^m <= N
    m=-5
    while True:
        p,q=epspow(m+1)
        if sgn(N-2*p,-2*q)>=0: m+=1
        else: return m
def classes(J):
    Nmax=2**(J+1); X=math.isqrt(int(Nmax*5.83))+3
    out=[]
    for b in range(-X,X+1):
        for a in range(-2*X,2*X+1):
            N=abs(a*a-2*b*b)
            if N==0 or N>=Nmax: continue
            if sgn(a,b)<=0: continue           # x1>0
            if a*b<0: continue                 # x1>=|x2|  <=> ab>=0
            s=sgn(a,-b)                        # sign x2
            # x1 < lam*|x2|:  x1 - s*lam*x2 <0 ; lam*x2=(3a-4b)+(2a-3b)s2
            if sgn(a-s*(3*a-4*b), b-s*(2*a-3*b))>=0: continue
            j=N.bit_length()-1
            out.append((j,a,b,N))
    return sorted(out)
t0=time.time(); C=classes(J)
res=[]; FL={}
for j,a,b,N in C:
    w,zr,k0=word(a,b)
    if N not in FL: FL[N]=floorlog(N)
    res.append(dict(j=j,a=a,b=b,N=N,span=len(w),zr=zr,word=w,fl=FL[N]))
from collections import Counter
cnt=Counter(r['j'] for r in res)
exc=Counter(r['span']-r['fl'] for r in res)
viol=[r for r in res if r['span']>r['fl']+3]
theta=math.log(2)/math.log(1+math.sqrt(2))
shellviol=[r for r in res if r['span']>math.floor(r['j']*theta)+3]
viol2j=[r for r in res if r['j']>=2 and r['span']>2*r['j']]
eq=[(r['a'],r['b'],r['N']) for r in res if r['span']==r['fl']+3][:10]
# shell-level sharpness: classes attaining floor(j*theta)+3
shsharp=Counter(r['j'] for r in res if r['span']==math.floor(r['j']*theta)+3)
maxspan={j:max(r['span'] for r in res if r['j']==j) for j in cnt}
json.dump(dict(J=J,counts=dict(sorted(cnt.items())),excess_hist=dict(sorted(exc.items())),n_viol=len(viol),n_shellviol=len(shellviol),
  n_viol_2j_jge2=len(viol2j),first_eq=eq,shell_sharp=dict(sorted(shsharp.items())),maxspan=dict(sorted(maxspan.items())),
  shellcap={j:math.floor(j*theta)+3 for j in sorted(cnt)},secs=time.time()-t0),open(f'/workspace/audit/pr83/AUDIT_code/census_J{J}.json','w'),indent=1)
with open(f'/workspace/audit/pr83/AUDIT_code/census_J{J}.jsonl','w') as f:
    for r in res: f.write(json.dumps(r)+'\n')
print(open(f'/workspace/audit/pr83/AUDIT_code/census_J{J}.json').read())
