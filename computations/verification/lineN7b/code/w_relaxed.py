"""N7b copy of bgs-lineL/code/l4_const.py; ONLY change: relaxed target 1.42785.
Line L: explicit constants for unconditional Theorem W [CA, arb].
For family (fam,typ) and k: I_k bound (same as l3_op_cert), A_k bound, eta, c_k=(eta/(6 A_k))^2,
T_k(q) <= Cpair * exp(-2 s sqrt q) prod_j A(tau_j + s w_j)^2, w_j = a lam^j + lam^-j / a, a = lam^{-(k-1)/2}
(since |N(alpha_v)| <= X Y <= ((aX+Y/a)/2)^2, X=sum|v_j|lam^j, Y=sum|v_j|lam^-j, |v_j|<=|n_j|+|n'_j|),
q0 = least (grid) q with T_k(q0) <= eta.  eta = (((1-delta/2) target)^{2k} - I_k)/3 with delta = delta_max/2.
usage: l4_const.py fam typ k rho beta E0 t"""
import sys, json, math
from flint import arb, ctx
ctx.prec=128
fam,typ=sys.argv[1],sys.argv[2]; k=int(sys.argv[3]); rho=arb(sys.argv[4]); beta=arb(sys.argv[5]); E0=int(sys.argv[6]); t=arb(sys.argv[7])
NS=1 if fam=='8' else 64
target=arb('1.9154712')*(3+2*arb(2).sqrt())**(-arb(1)/6)  # N7b: RELAXED per-level target mu*_lo*lam^(-1/6) (N6 Thm R#); only change
lam=3+2*arb(2).sqrt(); C0=1/(lam-1/lam); pi=arb.pi(); x=arb('1.8')
c=C0 if fam=='8' else C0/2
dev=(lam/(2*(lam-1))) if typ=='V' else (1/(2*(lam-1)))
AM=200
J=[abs(x.bessel_j(arb(a))) for a in range(AM+1)]
def jt(s):
    q=(x/2)*s.exp(); term=q**(AM+1)/arb(AM+1).gamma(); ratio=q/(AM+2); assert ratio.upper()<1
    return 2*term/(1-ratio)
def A(s): return J[0]+2*sum((J[a]*(s*a).exp() for a in range(1,AM+1)),arb(0))+jt(s)
taus=[2*pi*c*rho*lam**(-j)+beta*lam**(-(k-j)) for j in range(k)]
def rho_j(d,tau):
    s=arb(0)
    for a in range(-AM,AM+1):
        b=a-d
        if -AM<=b<=AM: s+=J[abs(a)]*J[abs(b)]*(tau*(abs(a)+abs(b))).exp()
    return s+2*jt(tau)*A(tau)
theta=(rho*lam**(-k)+dev)/rho; assert theta.upper()<1
coth=lambda z:(z.exp()+(-z).exp())/(z.exp()-(-z).exp())
Cpair=NS*coth(beta*(1-lam**(-k)))*(2*beta*(dev+1)).exp()/(1-theta*theta)
DV=8*E0+2
R=[{d:rho_j(d,taus[j]) for d in range(-DV,DV+1)} for j in range(k)]
vec={(0,0):arb(1)}
for j in range(k):
    new={}
    for (a,b),val in vec.items():
        for e in (range(-E0,E0+1) if j<=k-3 else [0]):
            d=e-6*b+a
            if abs(d)>DV: continue
            new[(b,e)]=new.get((b,e),arb(0))+val*R[j][d]
    vec=new
Sbox=vec.get((0,0),arb(0)); Q0=(E0+1)/C0; tail=arb(0)
for j in range(k-2):
    pr=arb(1)
    for i in range(k): pr*=A(taus[i]+t*lam**(-abs(j+1-i)))**2
    tail+=(-t*Q0).exp()*pr
Ik=(Cpair*(Sbox+tail)).upper()
Ak=Cpair
for j in range(k): Ak*=A(taus[j])**2
Ak=Ak.upper()
rate=(Ik.log()/(2*k)).exp()
ok=bool(rate.upper()<target.lower())
out=dict(fam=fam,typ=typ,k=k,rho=sys.argv[4],beta=sys.argv[5],E0=E0,t=sys.argv[7],Ik=float(Ik.mid()),rate=float(rate.upper().mid()),OP=ok)
if ok:
    dmax=1-rate/target; delta=dmax/2
    eta=((((1-delta/2)*target)**(2*k))-Ik)/3; eta=eta.lower()
    ck=(eta/(6*Ak))**2
    a=lam**(-arb(k-1)/2); w=[a*lam**j+lam**(-j)/a for j in range(k)]
    def logT(s,lq):  # log of T_k bound at q=10^lq
        pr=Cpair.log()
        for j in range(k): pr+=2*A(taus[j]+s*w[j]).log()
        return pr-2*s*(arb(10)**(arb(lq)/2))
    # find q0 on grid of log10 q, optimizing s on a grid
    smax=float((1/w[0]).mid()); best=None
    for lq10 in range(0,4000):
        lq=lq10/10
        ss=[smax*f for f in (0.05,0.1,0.2,0.3,0.5,0.7,1,1.5,2,2.5,3)]
        if any((logT(arb(s),lq)).upper()<eta.log().lower() for s in ss): best=lq; break
    out.update(delta=float(delta.mid()),eta=float(eta.mid()),log10_Ak=float((Ak.log()/arb(10).log()).mid()),
               log10_ck=float((ck.log()/arb(10).log()).mid()),log10_q0=best,
               log10_p_nonvacuous=float(((2/ck).log()/arb(10).log()).mid()))
print(json.dumps(out),flush=True)
