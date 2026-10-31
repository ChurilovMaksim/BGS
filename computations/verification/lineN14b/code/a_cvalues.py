"""N14b pre-flight [N/P-sketch bookkeeping]: index exponent c delivered by each argument, the d-range it covers,
and which h_p (p <= PMAX) are covered asymptotically ([N] illustration; e^{o(p)} prefactors ignored)."""
import math, json, sys
from sympy import factorint, isprime
mu=1.9154732; lam=3+2*math.sqrt(2); eps=1+math.sqrt(2)
Lfree=1.9656353; r2=1.0529012; Lam=Lfree          # C' inputs [CA]
cp=(1.2744/mu)**3                                  # 0.2945 per p-step
need=-math.log(eps*cp)                              # 0.3411: need c*theta*ln(lam) < need
cstar=need/(0.5*math.log(lam))                      # c for theta=1/2: 0.387
g0=None
args={
 'A_trivial_index_loss':1.0,
 'B_coarser_separation_sup_leftover_true_norm': math.log(Lfree**3/(Lam*r2))/math.log(lam),
 'B2_same_with_PropE_majorant_sup_g0': math.log(5.56/r2)/math.log(lam),
 'C_min_shift_pressure_theta_half_fixedpoint_lower': (0.5*math.log(mu**6/lam)-math.log(1.4055))/(0.5*math.log(lam)),
}
rows={}
for k,c in args.items():
    th=need/(c*math.log(lam)); rows[k]=dict(c=c,theta_max=min(th,0.5),d_max_base=lam**min(th,0.5))
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 80
cls=[]
cB=args['B_coarser_separation_sup_leftover_true_norm']; thB=need/(cB*math.log(lam)); thA=need/math.log(lam)
for p in [q for q in range(5,PMAX+1) if isprime(q)]:
    h=hp(p); f=factorint(h); qs=sorted(f)
    if len(qs)==1 and f[qs[0]]==1: cls.append((p,'prime',None)); continue
    dmax=h//qs[0]                                   # largest proper divisor = largest possible iso part
    th=math.log(dmax)/(p*math.log(lam))
    cls.append((p,'composite', dict(factors=[str(q) for q in qs],theta_max_iso=th,covered_A=th<thA,covered_B=th<thB)))
out=dict(c_star=cstar,need=need,args=rows,classification=cls)
print(json.dumps(rows,indent=1))
for c in cls: print(c)
json.dump(out,open('logs/a_cvalues.json','w'),indent=1)
