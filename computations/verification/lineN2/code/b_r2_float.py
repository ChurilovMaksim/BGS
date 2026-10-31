"""N2 (B) [N]: float exploration of the block-collision rate r_2(k) = (C_pair * rho(prod_j M(rho_j)))^{1/k}
for the Line-L families, carries free across block boundaries (exact collisions of concatenated blocks)."""
import numpy as np, math, json, sys
from scipy.special import jv
LAM=3+2*math.sqrt(2); C0=1/(LAM-1/LAM)
AM=60; J=np.abs(jv(np.arange(AM+1),1.8))
def Jabs(a): a=abs(a); return J[a] if a<=AM else 0.0
def rho_d(d,tau):
    s=0.0
    for a in range(-AM,AM+1):
        b=a-d
        if -AM<=b<=AM: s+=Jabs(a)*Jabs(b)*math.exp(tau*(abs(a)+abs(b)))
    return s
FAM={'8V':(1,0.75,0.25,'V',C0),'8E':(1,0.2,0.3,'E',C0),'16V':(64,0.9,0.3,'V',C0/2),'16E':(64,0.2,0.3,'E',C0/2)}
def letter_mat(tau,E):
    es=range(-E,E+1); st=[(a,b) for a in es for b in es]; idx={s:i for i,s in enumerate(st)}
    n=len(st); T=np.zeros((n,n)); R={d:rho_d(d,tau) for d in range(-8*E-2,8*E+3)}
    for (a,b) in st:
        for e in es:
            d=e-6*b+a
            if d in R: T[idx[(a,b)],idx[(b,e)]]+=R[d]
    return T
def r2(fam,k,E=6):
    NS,rho,beta,typ,c=FAM[fam]
    dev=LAM/(2*(LAM-1)) if typ=='V' else 1/(2*(LAM-1))
    theta=(rho*LAM**(-k)+dev)/rho
    Cpair=NS/math.tanh(beta*(1-LAM**(-k)))*math.exp(2*beta*(dev+1))/(1-theta**2)
    taus=[2*math.pi*c*rho*LAM**(-j)+beta*LAM**(-(k-j)) for j in range(k)]
    cache={}
    def M(t):
        key=round(t,14)
        if key not in cache: cache[key]=letter_mat(t,E)
        return cache[key]
    # log spectral radius of block by power iteration over many blocks
    n=(2*E+1)**2; x=np.ones(n)/n; logs=0.0; nb=40
    for b in range(nb):
        for j in range(k):
            x=M(taus[j])@x
            s=x.sum(); logs+=math.log(s) if b>=nb//2 else 0.0; x/=s
    lr=logs/(nb-nb//2)  # log rho(block w/o Cpair)
    return dict(fam=fam,k=k,Cpair=Cpair,log_block=lr,r2=math.exp((math.log(Cpair)+lr)/k),rate_per_step_noC=math.exp(lr/k))
res=[]
for fam in ['8V','8E','16V','16E']:
    for k in [15,50,100,200,500,1000,2000]:
        d=r2(fam,k); res.append(d); print(json.dumps(d),flush=True)
json.dump(res,open('logs/b_r2_float.json','w'),indent=1)
