"""N14: exact window twist sequences (mpmath, N8/N13 core convention, KK padding) and the integer digit (carry-letter) words
D_t = -(d_t - 6 d_{t-1} + d_{t-2}) (in (1/4)Z; = 0 wherever |d| < 1/16 on three consecutive sites).  d = G*D (Green kernel)."""
import mpmath as mp, math
mp.mp.dps=34
S2=mp.sqrt(2); LAM=3+2*S2
def red(x): return x-mp.floor(x+mp.mpf(1)/2)
def seeds(ea,eb):
    zA=(mp.mpf(2*eb)/8, mp.mpf(ea)/8); fu=-ea+2*eb; fv=ea-eb; zB=(-mp.mpf(2*fv)/8,-mp.mpf(fu)/8); return zA,zB
def core(z,KK=18):
    e1=z[0]+z[1]*S2; e2=z[0]-z[1]*S2
    L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(LAM))))
    return [float(red(e1*LAM**j)) if j<=0 else float(red(-e2*LAM**(-j))) for j in range(-(KK+L1),KK+L2+1)]
def digits(ds):
    return [round(-4*(ds[t]-6*ds[t-1]+ds[t-2]))/4 for t in range(2,len(ds))]
def word(ds):
    D=digits(ds); nz=[i for i,x in enumerate(D) if x!=0]
    if not nz: return [],0
    w=D[nz[0]:nz[-1]+1]
    runs=[];r=0
    for x in w:
        if x==0: r+=1
        else:
            if r: runs.append(r)
            r=0
    return w,(max(runs) if runs else 0)
if __name__=='__main__':
    def mulq(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
    for e in [(2,0),(0,2),(4,0),(0,4),(8,0),(200,140),(1156,816),(34,24),(6,4),(12,0),(6,0),(10,0)]:
        out=[]
        for z in seeds(*e): w,mr=word(core(z,6)); out.append((w,mr))
        print(e,out)
def core_t(z,KK=6):
    e1=z[0]+z[1]*S2; e2=z[0]-z[1]*S2
    L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(LAM))))
    return {j:(float(red(e1*LAM**j)) if j<=0 else float(red(-e2*LAM**(-j)))) for j in range(-(KK+L1),KK+L2+1)}
def eps_word(ea,eb,KK=6):
    """eps-chain twists tau_k (k=2t: A_t ; k=2t-1: -B_t) and integer letters E_k=-(tau_k-2tau_{k-1}-tau_{k-2})."""
    zA,zB=seeds(ea,eb); A=core_t(zA,KK); B=core_t(zB,KK)
    ks=sorted(set([2*t for t in A]+[2*t-1 for t in B]))
    tau={}
    for k in range(ks[0],ks[-1]+1):
        if k%2==0: tau[k]=A.get(k//2,0.0)
        else: tau[k]=-B.get((k+1)//2,0.0)
    E={k:-(tau[k]-2*tau[k-1]-tau[k-2]) for k in range(ks[0]+2,ks[-1]+1)}
    return tau,E
def eps_digits(ea,eb,KK=6,tol=1e-6):
    tau,E=eps_word(ea,eb,KK)
    nz=[k for k in sorted(E) if abs(E[k])>tol]
    if not nz: return [],0,0
    w=[E[k] for k in range(nz[0],nz[-1]+1)]
    gaps=[b-a-1 for a,b in zip(nz,nz[1:])]
    return w,(max(gaps) if gaps else 0),nz[0]
