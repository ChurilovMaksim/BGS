"""N13 (A) [N, Monte Carlo]: shell-by-shell first and second moments of single-class window weights for DEEP classes.
Seeds e = 2 alpha (bg 1/4) or 2 sqrt2 alpha (bg 0), alpha in O with |N(alpha)| in [2^j, 2^{j+1}), one representative per
lam-orbit (fundamental domain 1 <= |e1/e2| < lam), sign classes merged. Window weights r_A, r_B (N12 float sector-4 operator, KK=18),
class weight |w| = |r_A r_B|^3.  Output per shell: exact count N_j of representatives (enumerated), sample mean of |w|, |w|^2, |r_A|^2,
estimated shell sum S1 = N_j E|w|, CS bound sqrt(N_j * N_j E|w|^2) and max |w| in sample.  usage: e_shell.py jmin jmax step nsamp seed"""
import sys, json, math, random, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
import mpmath as mp
mp.mp.dps=60
A0,s,Phi,psi=A.spectral()
S2=mp.sqrt(2); LAM=3+2*S2; KK=18; lamf=float(LAM); r2=math.sqrt(2)
def red(x): y=x-mp.floor(x+mp.mpf(1)/2); return float(y)
def seeds(e):
    ea,eb=e; zA=(mp.mpf(2*eb)/8, mp.mpf(ea)/8); fu=-ea+2*eb; fv=ea-eb; zB=(-mp.mpf(2*fv)/8,-mp.mpf(fu)/8); return zA,zB
def core(z):
    e1=z[0]+z[1]*S2; e2=z[0]-z[1]*S2
    L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(LAM))))
    return [red(e1*LAM**j) if j<=0 else red(-e2*LAM**(-j)) for j in range(-(KK+L1),KK+L2+1)]
def weight(ds):
    v=Phi.astype(complex)
    for d in ds: v=(A.Amat(d)@v)/s
    return complex(psi@v)
def reps(j):   # alpha=(a,b): N=a^2-2b^2, fundamental domain for multiplication by lam, up to sign: 1<=|x1/x2|<lam, x1=a+b r2 >0
    lo,hi=2**j,2**(j+1); out=[]
    # |x1 x2| = N in [lo,hi), x1/|x2| in [1,lam) => x1 in [sqrt(N), sqrt(N lam))
    X1max=math.sqrt(hi*lamf)
    for b in range(-int(X1max)-2,int(X1max)+3):
        for sgn2 in (1,-1):
            pass
    # brute force on a,b with x1 in range
    B=int(X1max/r2)+2
    for b in range(-B,B+1):
        amin=int(math.floor(-X1max))-2; amax=int(math.ceil(X1max))+2
        for a in range(amin,amax+1):
            x1=a+b*r2; x2=a-b*r2
            if x1<=0 or x2==0: continue
            N=abs(a*a-2*b*b)
            if not (lo<=N<hi): continue
            q=x1/abs(x2)
            if 1<=q<lamf: out.append((a,b))
    return out
jmin,jmax,step,ns,seed=map(int,sys.argv[1:6]); random.seed(seed)
res=[]
for j in range(jmin,jmax+1,step):
    for bg in ('q','0'):
        R=reps(j); Nj=len(R); smp=random.sample(R,min(ns,Nj))
        ws=[];ra=[];
        for (a,b) in smp:
            e=(2*a,2*b) if bg=='q' else (4*b,2*a)     # 2 alpha  or  2 sqrt2 alpha = 2sqrt2(a+b sqrt2) = 4b + 2a sqrt2
            zA,zB=seeds(e); rA=weight(core(zA)); rB=weight(core(zB))
            ws.append(abs(rA*rB)**3); ra.append(abs(rA)**2)
        ws=np.array(ws); m1=ws.mean(); m2=(ws**2).mean()
        row=dict(j=j,bg=bg,N_j=Nj,n=len(smp),E_w=m1,E_w2=m2,E_rA2=float(np.mean(ra)),S1_est=Nj*m1,CS=math.sqrt(Nj*Nj*m2),max_w=float(ws.max()),
                 se_S1=Nj*ws.std()/math.sqrt(len(ws)))
        res.append(row); print(json.dumps(row),flush=True)
        json.dump(res,open(f'/workspace/bgs-lineN/N13/logs/e_shell_{jmin}_{jmax}_{step}.json','w'),indent=1)
