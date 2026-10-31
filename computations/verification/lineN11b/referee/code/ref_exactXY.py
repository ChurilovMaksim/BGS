"""Referee N11b [N]: independent exact level-h_p decomposition for prime h_p (p=5,7).
Own twist map (tau_i = 2*Re(lambda^i beta)/d mod 1, Re = rational coefficient), own orbit reduction (lambda-shift only, which is
exact by cyclicity of the trace; NO sign/conjugation identification), own kappa. Inputs reused: the TW law (twb.Zbatch/TW/nu_rho/mdata)
and the N6 definition of S_d (members t = j*yp mod d, j=1..d-1, excluding nu0 + floor(2hj/d) = 0 mod d).
Also tests numerically whether Zhat is invariant under beta -> -beta and beta -> conj(beta) (used by N11b's reduction)."""
import os; os.environ.setdefault('OMP_NUM_THREADS','1')
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, nu_rho, TW, mdata
p=int(sys.argv[1]); m=3*p
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
d=hp(p); md=mdata(m); h=md['h']; yp=md['yp']
h_,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16)
def lam(b): return ((3*b[0]+4*b[1])%d,(2*b[0]+3*b[1])%d)
def taus(b):
    out=[]; x=b
    for i in range(m): out.append(((2*x[0])%d)/d); x=lam(x)
    return out
# lambda-orbits
seen=np.zeros((d,d),bool); reps=[]; orb=[]
for a in range(d):
    for b in range(d):
        if seen[a,b]: continue
        o=[]; x=(a,b)
        while not seen[x]:
            seen[x]=True; o.append(x); x=lam(x)
        reps.append((a,b)); orb.append(o)
Z=np.zeros(len(reps),complex); T=[taus(r) for r in reps]
for i in range(0,len(reps),32): Z[i:i+32]=Zbatch(tw,T[i:i+32])
Z0=Z[reps.index((0,0))]
S=[]
for j in range(1,d):
    nu=nu0+2*h*j//d
    if nu%d==0: continue
    S.append((j*yp)%d)
n=len(S)
def kap(u): return sum(np.exp(2j*np.pi*((pow(t,-1,d)*u)%d)/d) for t in S)
K={u:kap(u) for u in range(d)}
X=0; Y=0; A=np.zeros(d,complex); sabs=0
for (a,b),o,z in zip(reps,orb,Z):
    r=z/Z0; u=(a*a-2*b*b)%d; L=len(o); A[u]+=L*z
    if (a,b)==(0,0): continue
    if u==0: X+=L*r
    else: Y+=L*K[u]*r/n; sabs+=L*abs(r)
dev=0.0
for t in S:
    ph=np.array([np.exp(2j*np.pi*((pow(t,-1,d)*u)%d)/d) for u in range(d)]); dev+=(abs((ph*A).sum())**2-abs(Z0)**2)/d**2
main=n*abs(Z0)**2/d**2
# invariance tests on a sample of reps
rng=np.random.default_rng(1); idx=rng.choice(len(reps),min(40,len(reps)),replace=False)
neg=[(-reps[i][0]%d,-reps[i][1]%d) for i in idx]; cj=[(reps[i][0],(-reps[i][1])%d) for i in idx]
Zn=Zbatch(tw,[taus(b) for b in neg]); Zc=Zbatch(tw,[taus(b) for b in cj])
inv_neg=float(max(abs(Zn[k]-Z[i])/abs(Z0) for k,i in enumerate(idx))); inv_conj=float(max(abs(Zc[k]-Z[i])/abs(Z0) for k,i in enumerate(idx)))
res=dict(p=p,d=d,n=n,n_orbits=len(reps),kappa_unit_max=float(max(abs(K[u]) for u in range(1,d))),X=[X.real,X.imag],Y=[Y.real,Y.imag],
         one_plus_X=abs(1+X),one_plus_X_plus_Y=abs(1+X+Y),CS_lower=abs(1+X+Y)**2-1,Dev_over_main=dev/main,sum_abs_r_unit=sabs,
         invariance_neg_max_rel=inv_neg,invariance_conj_max_rel=inv_conj)
print(json.dumps(res)); json.dump(res,open(f'logs/ref_exactXY_p{p}.json','w'),indent=1)
