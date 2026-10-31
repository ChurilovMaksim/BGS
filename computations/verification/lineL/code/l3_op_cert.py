"""Line L, Theorem OP_abs certificate [CA, arb ball arithmetic].
Bounds I_k = int_{T^2} ||P_k(y)||_HS^2 dy for the TRUE k1 lattice-lifted twisted families (Line F/J lattices, full alphabet),
WITHOUT using cancellation:
  I_k <= C_pair * S_k,   S_k = sum_{v in Z^k, sum_j v_j lam^j = 0} prod_j rho_j(v_j),
  rho_j(d) = sum_a |J_a(1.8)||J_{a-d}(1.8)| exp(tau_j(|a|+|a-d|)),  tau_j = 2 pi c rho lam^-j + beta lam^-(k-j),
  C_pair = NS * coth(beta(1-lam^-k)) * exp(2 beta (dev+1)) / (1-theta^2),  theta = (rho lam^-k + dev)/rho.
S_k: v=(X^2-6X+1)E; carry automaton on |e|<=E0 (exact enumeration in arb) + tilted tail bound for max|e|>E0:
  |e_j| <= C0g sum_i |v_i| lam^-|j+1-i|  (Green's function, C0g = 1/(lam-1/lam)), so
  tail <= sum_j exp(-t (E0+1)/C0g) prod_i A(tau_i + t lam^-|j+1-i|)^2,  A(s) = sum_a |J_a| e^{s|a|}.
Also A_k-bound (l1 Fourier mass of f_k): C_pair * prod_j A(tau_j)^2.
usage: l3_op_cert.py fam typ k rho beta E0 t [NS]   fam in {8,16} (c = C0 or C0/2), typ in {V,E} (dev 0.6036.. or 0.1036..)"""
import sys, json, math, time
from flint import arb, ctx
ctx.prec=128
fam=sys.argv[1]; typ=sys.argv[2]; k=int(sys.argv[3]); rho=arb(sys.argv[4]); beta=arb(sys.argv[5]); E0=int(sys.argv[6]); t=arb(sys.argv[7])
NS=int(sys.argv[8]) if len(sys.argv)>8 else (1 if fam=='8' else 64)
lam=3+2*arb(2).sqrt(); C0=1/(lam-1/lam); pi=arb.pi(); x=arb('1.8')
c=C0 if fam=='8' else C0/2
dev=(lam/(2*(lam-1))) if typ=='V' else (1/(2*(lam-1)))
AM=60
J=[abs(x.bessel_j(arb(a))) for a in range(AM+1)]          # |J_{-a}|=|J_a|
def jt(s):   # upper bound sum_{|a|>AM} |J_a| e^{s|a|}  using |J_a(x)|<=(x/2)^a/a!
    q=(x/2)*s.exp(); term=q**(AM+1)/arb(AM+1).gamma()
    ratio=q/(AM+2); assert ratio.upper()<1
    return 2*term/(1-ratio)
def A(s):
    return J[0]+2*sum((J[a]*(s*a).exp() for a in range(1,AM+1)),arb(0))+jt(s)
taus=[2*pi*c*rho*lam**(-j)+beta*lam**(-(k-j)) for j in range(k)]
def rho_j(d,tau):
    s=arb(0)
    for a in range(-AM,AM+1):
        b=a-d
        if -AM<=b<=AM: s+=J[abs(a)]*J[abs(b)]*(tau*(abs(a)+abs(b))).exp()
    # tail: pairs with |a|>AM or |b|>AM
    s+=2*jt(tau)*A(tau)
    return s
theta=(rho*lam**(-k)+dev)/rho; assert theta.upper()<1
coth=lambda z:(z.exp()+(-z).exp())/(z.exp()-(-z).exp())
Cpair=NS*coth(beta*(1-lam**(-k)))*(2*beta*(dev+1)).exp()/(1-theta*theta)
t0=time.time()
DV=8*E0+2
# distinct tau classes: compute rho_j table per position (positions far from both ends share ~ same value; compute all, k small)
R=[{d:rho_j(d,taus[j]) for d in range(-DV,DV+1)} for j in range(k)]
es=range(-E0,E0+1)
vec={(0,0):arb(1)}
for j in range(k):
    new={}
    free = j<=k-3
    for (a,b),val in vec.items():
        for e in (es if free else [0]):
            d=e-6*b+a
            if abs(d)>DV: continue
            key=(b,e); new[key]=new.get(key,arb(0))+val*R[j][d]
    vec=new
Sbox=vec.get((0,0),arb(0))
Q0=(E0+1)/C0
tail=arb(0)
for j in range(k-2):
    pr=arb(1)
    for i in range(k): pr*=A(taus[i]+t*lam**(-abs(j+1-i)))**2
    tail+=(-t*Q0).exp()*pr
Sk=Sbox+tail
Ik=Cpair*Sk
Akb=Cpair*math.prod([1]) if False else Cpair
for j in range(k): Akb*=A(taus[j])**2
rate=(Ik.upper().log()/(2*k)).exp()
out=dict(fam=fam,typ=typ,k=k,rho=sys.argv[4],beta=sys.argv[5],E0=E0,t=sys.argv[7],NS=NS,
         Cpair=str(Cpair.upper()),Sbox=str(Sbox.upper()),tail=str(tail.upper()),Sk=str(Sk.upper()),Ik_upper=str(Ik.upper()),
         Ik_rate_upper=str(rate.upper()),Ak_upper=str(Akb.upper()),log10_Ak=float((Akb.upper().log()/arb(10).log()).mid()),
         Sk_rate=float(((Sk.upper()).log()/k).exp().mid()),sec=round(time.time()-t0,1))
print(json.dumps(out),flush=True)
json.dump(out,open(f'/workspace/bgs-lineL/logs/l3_op_{fam}{typ}_k{k}_r{sys.argv[4]}_b{sys.argv[5]}_E{E0}_t{sys.argv[7]}.json','w'),indent=1)
