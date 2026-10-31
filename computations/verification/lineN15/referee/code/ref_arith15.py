"""Referee lineN15 arithmetic: (1) N15 constants (gamma_n, kappa_der, KAP, wrap q, KP inequalities, carry alphabet DP);
(2) N17b: Robin crossover with the correct gas form (1+R)^p e^{-p delta} and exact K_p; inclusion threshold m0; CRT 7371/7743/372 sets;
h_{3p}=h_p K_p, 7|K_p, gcd(h_p,K_p)|3; scale 1.1329; eps16 base; Nicolas-Robin exponent."""
import math, json, mpmath as mp
from math import gcd
mp.mp.dps=60; out={}
u=2.0**-53; gam=lambda n: n*u/(1-n*u); cg=lambda n: math.sqrt(2)*gam(n+2)
eps_c=4*u*2*math.pi*30*0.5+16*u; M=53
kd=(1+eps_c)*(1+cg(55))*(1+math.sqrt(2)*gam(2))*(1+gam(M))-1
out['N15']=dict(eps_c=eps_c,kappa_der=kd,KAP=max(1e-13,1.25*kd)+2*u,slack_KAP_minus_needed=max(1e-13,1.25*kd)+2*u-(kd+3*u))
lam=3+2*math.sqrt(2)
def wrap(r): q=(lam*r*r)**1.5; return dict(q=q,ln1q=math.log(1/q),per_loglam=math.log(1/q)/math.log(lam))
out['wrap']={str(r):wrap(r) for r in (0.28,0.28028,0.30)}
kp={2:(2.329124291276331e-06,6.973770084696294e-07,4.5625098068091995e-06),3:(3.952295865958211e-06,1.3186839448201042e-06,9.78162942436991e-06),
    4:(5.932523657266671e-06,2.062874941576436e-06,1.7935737945768633e-05),5:(8.005618654226384e-06,2.8364132688595393e-06,2.8727912696707814e-05),
    6:(1.031499495676512e-05,3.696008860565644e-06,4.289457102114128e-05)}
out['KP']={g:dict(lhs=s0+s1/(1+g),a=a,ok=s0+s1/(1+g)<=a,margin=a-(s0+s1/(1+g))) for g,(a,s0,s1) in kp.items()}
out['KP_budget_g4']=2.062874941576436e-06+5.14476e-7
# carry alphabet: e_t - 6 e_{t-1} + e_{t-2} = v_t, |v|<=60, finitely supported e (start/end at 0,0). max |e| reachable on closed paths
E=15; S=[(a,b) for a in range(-E,E+1) for b in range(-E,E+1)]
def nxt(s): a,b=s; return [(b,c) for c in range(-E,E+1) if abs(c-6*b+a)<=60]
fw={(0,0)}; fr=[(0,0)]
while fr:
    n=[]
    for s in fr:
        for t in nxt(s):
            if t not in fw: fw.add(t); n.append(t)
    fr=n
# backward reachability to (0,0) followed by trailing zeros: need state (a,b) from which (b,0),(0,0) reachable
pred={}
for s in S:
    for t in nxt(s): pred.setdefault(t,[]).append(s)
bw={(0,0)}; fr=[(0,0)]
while fr:
    n=[]
    for t in fr:
        for s in pred.get(t,[]):
            if s not in bw: bw.add(s); n.append(s)
    fr=n
ok=fw&bw
out['carry']=dict(max_abs_e_closed=max(max(abs(a),abs(b)) for a,b in ok),n_pair_states=len(ok),n_values=len({a for a,b in ok}),green_sum=1/4)
# N17b ---------------------------------------------------------------
def xy(n):
    x,y=1,1
    for _ in range(n-1): x,y=x+2*y,x+y
    return x,y
R=6.234e-4; dl=5.14476e-7; g=float(mp.euler)
def G_correct(p): return (2*mp.power(1+R,p)*mp.e**(-p*dl)-1)**2-1
def G_N17b(p): a=6.234e-4-5.14415e-7; return (2*mp.power(1+a,p)-1)**2-1
def Ib(p):
    h,_=xy(p); K=4*h*h+3; L=mp.log(mp.log(K)); return mp.e**g*L+mp.mpf('0.6483')/L-1
first=None; firstN=None; tab={}
for p in range(1200,5001):
    gi=Ib(p); d=G_correct(p)-gi
    if first is None and d>0: first=p
    if first is not None and d<=0: first=('nonmonotone',p)
    if firstN is None and G_N17b(p)-gi>0: firstN=p
    if p in (1289,1385,1386,1399,1500,3000,5000): tab[p]=(float(G_correct(p)),float(gi))
primes_after=[q for q in range(first,first+40) if all(q%r for r in range(2,int(q**.5)+1))][:2]
out['robin']=dict(first_p_correct_form=first,first_p_N17b_form=firstN,table=tab,first_primes_after=primes_after,
                  monotone_checked_to=5000)
# inclusion threshold (TRACE-199 bound), exact
th={}
m0=None
for m in range(13,401,2):
    h,_=xy(m); Zlb=(1-mp.mpf(lam)**(-m))*(mp.mpf('1.9154712')**m-mp.mpf('3012.3'))/2
    okm=Zlb>0 and Zlb**2>=4*m*h
    if okm and m0 is None: m0=m
    if not okm: m0=None
out['threshold_m0_upto399']=m0
# h_{3p}=h_p K_p, 7|K_p, gcd(h_p,K_p)|3 for primes 5..400
pr=[p for p in range(5,401) if all(p%r for r in range(2,int(p**.5)+1))]
okid=True; ok7=True; okg=True
for p in pr:
    hp,_=xy(p); h3,_=xy(3*p); K=4*hp*hp+3
    okid&=(h3==hp*K); ok7&=(K%7==0); okg&=(3%gcd(hp,K)==0)
out['Kp']=dict(identity=okid,seven_divides=ok7,gcd_divides_3=okg,primes=len(pr))
# CRT sets at m=33, d=8119 (levels 23, 353, 8119 of h_33)
m=33; h,yp=xy(m); Mm=2*h; x0=pow(4,-1,h); nu0=min(x for x in (x0,x0+h) if x%2==1)   # rho=(2,8)
assert (8*nu0-2)%Mm==0
d=8119; mem=[];nonunit_nu=[]; unit_t=0
for j in range(1,d):
    nu=(nu0+(Mm//d)*j)%Mm
    if nu%d==0: continue
    if gcd(j,d)==1:
        unit_t+=1
        if gcd(nu,Mm)==1: mem.append(j)
        else: nonunit_nu.append(j)
lv={}
for dd in (23,353):
    lv[dd]=sum(1 for k in range(1,dd) if gcd((nu0+(Mm//dd)*k)%Mm,Mm)==1)
out['CRT']=dict(N6_rule_unit_t=unit_t,TRACE206_members_8119=len(mem),diff=unit_t-len(mem),
                diff_all_nonunit_nu=all(gcd((nu0+(Mm//d)*j)%Mm,Mm)>1 for j in nonunit_nu),n23=lv[23],n353=lv[353])
mu=1.9154712; eps=1+math.sqrt(2)
out['misc']=dict(scale=mu**2/(eps*eps**(1/3)),eps16_base=eps**(1/3)*(1.6355/mu)**2,
                 NR_exponent_p1386=1.5379*(math.log(2)*0+ (3*1386*math.log(eps)-math.log(2)))/math.log(3*1386*math.log(eps)-math.log(2))*math.log(2),
                 Tprime=mu/eps**(1/3), ratio_hp=7371/8119, crt_prod=(21/23)*(351/353))
print(json.dumps(out,indent=1,default=str)); json.dump(out,open('logs/ref_arith15.json','w'),indent=1,default=str)
