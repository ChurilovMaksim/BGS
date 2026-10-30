"""H1 exploration [N]: spectral radius of the Line G (a,b) partial-trace operators L_{a,b} = sum_n ghat(n) e(C n^2/2) MC_n (x) A_n^{(b)}
(H^2(D_rho) (x) C^{b^2}), k1 kick (|n|<=Lk), for every unit nu mod 2h_m whose reduced lattice vector has b <= Bmax.
Groups nu by operator data (a,b,k mod b); reports spectral radius vs lam^{1/4}=1.5538 and the |Z|^2 of the class sum if available."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineG/code')
from law import mdata, ratrec, kick_ghat, MC, LAM, C0
m=int(sys.argv[1]); Bmax=int(sys.argv[2]); K=int(sys.argv[3]); Lk=int(sys.argv[4])
d=mdata(m); h=d['h']; yp=d['yp']; M=2*h
gh=kick_ghat('k1',2.0,Lk)
rho=1.25*Lk/(LAM-1)+0.5
def op(a,b,k):
    coef=-4*a*C0/b; psi0=yp%b; psi1=(3*yp-2*h)%b; S=b*b
    us=np.arange(S)//b; ws=np.arange(S)%b
    Op=np.zeros((K*S,K*S),complex)
    for n,gn in gh.items():
        Mn=gn*np.exp(2j*np.pi*coef*n*n/2)*MC(n,coef,rho,K)
        ph=np.exp(-2j*np.pi*((k*((psi0*n*n+2*n*us)%b))%b)/b)
        tgt=(((6*us-ws+n*psi1)%b)*b+((us+n*psi0)%b))
        An=np.zeros((S,S),complex); An[tgt,np.arange(S)]=ph   # state s -> tgt(s) with phase
        Op+=np.kron(Mn,An)
    return Op
seen={}
for nu in range(1,M,2):
    if math.gcd(nu,h)!=1: continue
    cands=[(a_,b_) for (a_,b_) in ratrec(nu,M) if 0<b_<=Bmax and abs(a_)<=b_]
    if not cands: continue
    a,b=min(cands,key=lambda t:t[0]**2+t[1]**2)
    k=((b*nu-a)//M)%b
    key=(a,b,k)
    seen.setdefault(key,[]).append(nu)
rows=[]
for (a,b,k),nus in sorted(seen.items(),key=lambda t:(t[0][1],t[0][0])):
    ev=np.linalg.eigvals(op(a,b,k)); r=float(max(abs(ev)))
    rows.append(dict(a=a,b=b,k=k,count=len(nus),nu0=nus[0],N_mod_h=int(pow(nus[0],-1,h)) if math.gcd(nus[0],h)==1 else None,specrad=round(r,4)))
    print(json.dumps(rows[-1]),flush=True)
