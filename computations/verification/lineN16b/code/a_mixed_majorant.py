"""N16b (2) [N]: averages of the Prop-E majorant F_p(beta)=prod_{i<p} g(Tr(lam^i beta)/h), g(t)=|sum_a |J_a(1.8)| e(at)|^2,
over the MIXED classes  M_q = {beta mod h : N beta = 0 mod q, N beta unit mod h/q}  (h_p = q * q2 two-prime case, general: unit mod all other primes),
enumerated directly on the sublattice  a = r*b mod q  (r^2 = 2 mod q; the conjugate ideal a = -r b is the Galois image, F(beta')=F(beta)).
Also the exact collision mass W0 = sum_{v(lam)=0, len p} prod ghat(v_i) via the carry automaton (|e|<=10, |v|<=40; exact for the majorant).
Outputs E_M, E_M/W0 and c_coll = log(E_M/W0)/log q.  mode 'exact' (all b) or 'sample' (NS random (a,b) on the sublattice).
usage: a_mixed_majorant.py p q mode [NS]"""
import sys, json, math, time, numpy as np, mpmath as mp
from sympy import factorint, sqrt_mod
p=int(sys.argv[1]); q=int(sys.argv[2]); mode=sys.argv[3]; NS=int(sys.argv[4]) if len(sys.argv)>4 else 0
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
h=xy(p)[0]; fac=sorted(factorint(h)); assert h%q==0 and q in fac
others=[f for f in fac if f!=q]
u=np.array([float(abs(mp.besselj(a,1.8))) for a in range(-60,61)]); A=np.arange(-60,61)
GR=1<<16; tg=np.arange(GR)/GR; gg=np.abs(np.exp(2j*np.pi*np.outer(tg,A))@u)**2
ghat={v:float(sum(u[i]*u[i+v] for i in range(len(u)) if 0<=i+v<len(u))) for v in range(-40,41)}
# collision mass W0 via carries: v_j = e_j - 6 e_{j-1} + e_{j-2}, words of length p with v(lam)=0 <-> E of length p-2 (e_{-1}=e_{-2}=0, e_{p-2}.. =0)
E0=10; es=range(-E0,E0+1)
def W0():
    # sequence e_0..e_{p-3} free, e outside = 0; v_j = e_j -6e_{j-1}+e_{j-2} for j=0..p-1
    from collections import defaultdict
    st={(0,0):1.0}
    for j in range(p):
        nst=defaultdict(float)
        for (e2,e1),w in st.items():
            for e in (es if j<=p-3 else [0]):
                v=e-6*e1+e2
                if abs(v)<=40: nst[(e1,e)]+=w*ghat[v]
        st=nst
    return st.get((0,0),0.0)
w0=W0()
r=int(sqrt_mod(2,q))
LA=[1];LB=[0]
for i in range(p-1): a_,b_=LA[-1],LB[-1]; LA.append((3*a_+4*b_)%h); LB.append((2*a_+3*b_)%h)
LA=np.array(LA,dtype=np.int64); LB=np.array(LB,dtype=np.int64)
def Fvals(a,b):
    F=np.ones(len(a))
    for i in range(p):
        t=(2*((a*LA[i])%h+(2*b*LB[i])%h))%h
        F*=gg[(t*GR)//h]
    return F
def mixed(a,b):
    N=(a*a-2*b*b)
    ok=np.ones(len(a),bool)
    for f in others: ok&=(N%f)!=0
    return ok&~((a==0)&(b==0))
t0=time.time(); S=0.0; n=0; mx=0.0
kq=h//q
if mode=='exact':
    K=np.arange(kq,dtype=np.int64)
    CH=max(1,4_000_000//kq)
    for b0 in range(0,h,CH):
        b=np.arange(b0,min(h,b0+CH),dtype=np.int64)
        a=((r*b)%q)[:,None]+q*K[None,:]; bb=np.broadcast_to(b[:,None],a.shape)
        a=a.ravel(); bb=bb.ravel(); ok=mixed(a,bb); a=a[ok]; bb=bb[ok]
        F=Fvals(a,bb); S+=F.sum(); n+=len(F); mx=max(mx,F.max() if len(F) else 0)
else:
    rng=np.random.default_rng(7*p+q)
    while n<NS:
        b=rng.integers(0,h,2_000_000).astype(np.int64); k=rng.integers(0,kq,2_000_000).astype(np.int64)
        a=(r*b)%q+q*k; ok=mixed(a,b); a=a[ok]; b=b[ok]
        F=Fvals(a,b); S+=F.sum(); n+=len(F); mx=max(mx,F.max())
EM=S/n
res=dict(p=p,h=h,q=q,factors=[int(f) for f in fac],mode=mode,n=n,E_M=EM,max_F=mx,W0=w0,ratio_EM_W0=EM/w0,
         c_coll=math.log(EM/w0)/math.log(q),sec=round(time.time()-t0,1))
print(json.dumps(res),flush=True); json.dump(res,open(f'logs/a_mixed_p{p}_q{q}_{mode}.json','w'),indent=1)
