"""Referee: (a) exact level-q X_q,Y_q at p=11, q=353 (own lambda-orbit reduction, own twists tau_i = Tr(lam^i beta)/q; TW law from N6 twb);
(b) exact kappa at level h=8119 (N6 member rule) and max mixed weights |kappa|/n per class type; check |H_d| counts."""
import os; os.environ.setdefault('OMP_NUM_THREADS','1')
import sys, json, numpy as np, math
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, nu_rho, TW, mdata
p=11; m=3*p; md=mdata(m); hm=md['h']; yp=md['yp']; h_,nu0=nu_rho(m,1)
def Srule(d):
    S=[]
    for j in range(1,d):
        nu=nu0+2*hm*j//d
        if nu%d==0: continue
        S.append((j*yp)%d)
    return S
out={}
# (b) kappa at level 8119
H=8119; S0=Srule(H); out['n_rule_8119']=len(S0); out['nonunits_in_rule']=sum(1 for t in S0 if math.gcd(t,H)!=1)
S=[t for t in S0 if math.gcd(t,H)==1]; n=len(S); out['n_units_8119']=n
# CRT-product alternative
S353=Srule(353); S23=Srule(23); out['n353,n23']=[len(S353),len(S23)]
tinv=np.array([pow(t,-1,H) for t in S],dtype=np.int64); u=np.arange(H,dtype=np.int64)
kap=np.zeros(H,complex)
for i in range(0,n,500): kap+=np.exp(2j*np.pi*((np.outer(tinv[i:i+500],u))%H)/H).sum(0)
mix353=[x for x in range(H) if x%353==0 and x%23!=0]; mix23=[x for x in range(H) if x%23==0 and x%353!=0]
out['max_w_iso353_unit23']=float(max(abs(kap[x]) for x in mix353)/n); out['max_w_iso23_unit353']=float(max(abs(kap[x]) for x in mix23)/n)
out['bound_2w_2d_over_h']={'d353':4*353/H,'d23':4*23/H}; out['2/(q_u-2)']={'q23':2/21,'q353':2/351}
# |H_d| exact: #beta mod h with N=0 mod d and unit mod h/d
def cnt(d,q):
    a=np.arange(d); Nd=(a[:,None]**2-2*a[None,:]**2)%d; c1=int((Nd==0).sum())
    b=np.arange(q); Nq=(b[:,None]**2-2*b[None,:]**2)%q; c2=int((Nq!=0).sum()); return c1*c2
out['H353']=cnt(353,23); out['H23']=cnt(23,353); out['2h^2/d']={'353':2*H*H/353,'23':2*H*H/23}
print(out,flush=True)
# (a) level q=353
q=353; tw=TW(m,nu0,L=8,K=16)
def lam(b): return ((3*b[0]+4*b[1])%q,(2*b[0]+3*b[1])%q)
def taus(b):
    o=[]; x=b
    for i in range(m): o.append(((2*x[0])%q)/q); x=lam(x)
    return o
seen=np.zeros((q,q),bool); reps=[]; L=[]
for a in range(q):
    for b in range(q):
        if seen[a,b]: continue
        x=(a,b); c=0
        while not seen[x]: seen[x]=True; c+=1; x=lam(x)
        reps.append((a,b)); L.append(c)
Z=np.zeros(len(reps),complex); T=[taus(r) for r in reps]
for i in range(0,len(reps),32): Z[i:i+32]=Zbatch(tw,T[i:i+32])
Z0=Z[reps.index((0,0))]; Sq=Srule(q); nq=len(Sq)
kq={x:sum(np.exp(2j*np.pi*((pow(t,-1,q)*x)%q)/q) for t in Sq) for x in range(q)}
X=0;Y=0
for (a,b),c,z in zip(reps,L,Z):
    if (a,b)==(0,0): continue
    Nn=(a*a-2*b*b)%q; r=z/Z0
    if Nn==0: X+=c*r
    else: Y+=c*kq[Nn]*r/nq
out.update(q=q,n_orbits=len(reps),nq=nq,Xq=[X.real,X.imag],Yq=[Y.real,Y.imag],one_plus_X_plus_Y=abs(1+X+Y))
print(out); json.dump(out,open('logs/ref_levelq.json','w'),indent=1)
