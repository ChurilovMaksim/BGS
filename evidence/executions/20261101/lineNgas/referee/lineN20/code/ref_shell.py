"""referee lineN20: independent recomputation of |r_A|,|r_B| for sampled classes (incl. j=13,14).
Own twists: sigma1(mu) lam^t mod 1 for ALL t (mpmath 60 digits; no use of the sigma2 branch => also tests Lemma P0),
mu_A=(sqrt2/4)alpha, mu_B=-eps^{-1} mu_A (Lemma J); own operator application: sparse COO in extended precision (clongdouble).
Compare with the CA-fp upper bounds abs_up in the logs: need abs_up >= |r|_ref and abs_up/|r|_ref - 1 small."""
import sys, json, random, numpy as np, mpmath as mp
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
mp.mp.dps=60; S2=mp.sqrt(2); LAM=3+2*S2; EPS=1+S2
LD=np.clongdouble
co=[]
for k in range(len(A.NS)):
    M=A.MS[k]; r,c=np.nonzero(M); co.append((r,c,M[r,c].astype(LD)))
C0=(A.COEF0.astype(LD))/LD(F.s); NSl=A.NS.astype(np.longdouble)
Phi=F.Phi.astype(LD); psi=F.psi.astype(LD); D=len(Phi)
pi=np.longdouble(mp.nstr(mp.pi,25))
def step(v,d):
    out=np.zeros(D,LD); dl=np.longdouble(mp.nstr(d,25))
    for k,(r,c,val) in enumerate(co):
        ph=C0[k]*np.exp(LD(2j)*pi*NSl[k]*dl)
        np.add.at(out,r,ph*val*v[c])
    return out
def red(x): return x-mp.floor(x+mp.mpf(1)/2)
def twists(mu,KK=18):  # mu = (p,q): p + q sqrt2
    e1=mu[0]+mu[1]*S2; e2=mu[0]-mu[1]*S2
    L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(LAM))))
    return [red(e1*LAM**j) for j in range(-(KK+L1),KK+L2+1)]
def r_of(ds):
    v=Phi.copy()
    for d in ds: v=step(v,d)
    return complex(psi@v/(psi@Phi))
def cls(a,b):
    muA=(mp.mpf(b)/2,mp.mpf(a)/4)              # (sqrt2/4)(a+b sqrt2)
    # mu_B = -(sqrt2-1) mu_A
    p,q=muA; muB=(-(-p+2*q), -(p-q))            # (sqrt2-1)(p+q sqrt2) = (-p+2q) + (p-q) sqrt2
    return abs(r_of(twists(muA))),abs(r_of(twists(muB)))
rows=[]
for f in ['a_cert_ext.jsonl','a_cert_ext_j14_s0.jsonl','a_cert_ext_j14_s1.jsonl','a_cert_ext_j14_s2.jsonl']:
    rows+=[json.loads(l) for l in open('/workspace/bgs-lineN/N20/logs/'+f)]
rows=[r for r in rows if not r.get('coded')]
old=[json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/a_cert3.jsonl')]
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 20)
r13=[r for r in rows if r['j']==13]; r14=[r for r in rows if r['j']==14]
# include the largest-weight classes of j=13,14 plus random ones, and two old shells
samp=sorted(r13,key=lambda r:-r['rArB2_up'])[:2]+random.sample(r13,3)+sorted(r14,key=lambda r:-r['rArB2_up'])[:2]+random.sample(r14,3)
samp+=[r for r in random.sample(old,2)]
out=[]
for r in samp:
    A_,B_=cls(r['a'],r['b'])
    up=r.get('absA_up'); upB=r.get('absB_up')
    if up is None: up=upB=None
    rec=dict(j=r['j'],a=r['a'],b=r['b'],refA=A_,refB=B_,rArB2_ref=(A_*B_)**2,rArB2_up=r['rArB2_up'],
             ok=(A_*B_)**2<=r['rArB2_up'],rel=r['rArB2_up']/(A_*B_)**2-1)
    if up is not None: rec.update(absA_up=up,absB_up=upB)
    print(json.dumps(rec),flush=True); out.append(rec)
json.dump(out,open('../logs/ref_shell.json','w'),indent=1)
