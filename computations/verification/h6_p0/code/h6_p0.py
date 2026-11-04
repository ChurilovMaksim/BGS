"""P4 (1) [P + CA, arb ball arithmetic]: explicit p0 for Theorem C' (unit points at h_p), all constants computed.
Chain (see REPORT_P4.md §1):  E_{G_p}|Tr(J M^3)| <= ||J|| * ||M||_op * ||M||_HS^2,
  ||M||_op <= C_I kF Lam^{p-4}  (Lemma I + N4 [CA]),   ||M||_HS^2 <= Hmax^4 * exp(S^hat phi(y)),  phi=(1/k)log(a+f_k), a=1,
  E_{G_p} e^{S^hat phi} <= B_eps e^{p w(eps)} Int e^{S^hat phi}   (Bowen, ball |v_u|<=eps lam^{-(p-1+k)}, |v_s|<=eps),
  Int e^{S^hat phi} <= (xmax/x0) r2^p  (Hoelder over residues + Prop E; xmax/x0 = 1 logged by r2_cert_x0.py).
Requirement:  w_max(p) log 2 + log K(p) < p log kappa,  kappa = T^3/(r2(k) Lam).
usage: h6_p0.py  -> logs/h6_p0.json"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import os as _os
HERE=_os.path.dirname(_os.path.abspath(__file__)); LOGS=_os.path.join(_os.path.dirname(HERE),'logs')
import json, math, sys
from flint import arb, ctx
ctx.prec=128
LAM=3+2*arb(2).sqrt(); E0U=1+arb(2).sqrt(); C0=1/(LAM-1/LAM); X=arb("1.8"); PI=arb.pi()  # E0U = fundamental unit eps_u (report: eps_u; eps = Bowen radius)
NB=80
J=[abs(X.bessel_j(n)) for n in range(NB+1)]
def fact(m): return arb(math.factorial(m))
def lettersum(c, power=0):
    """rigorous upper bound of sum_{n in Z} |J_n(1.8)| e^{c|n|} |n|^power  (|J_n(x)|<=(x/2)^n/n!)."""
    s=J[0] if power==0 else arb(0)
    for n in range(1,NB+1): s+=2*J[n]*(c*n).exp()*arb(n)**power
    q=X*c.exp()/2  # tail n>NB: term_n <= q^n n^power/n!, ratio <= q(1+1/n)^power/(n+1) <= 1/2
    t=(q**(NB+1))*arb(NB+1)**power/fact(NB+1)
    return s+4*t
def upper(x): return arb(x.upper())
# family data: O1 space, F space, per-step disc offset, multiplier constant, NS, target T, Lam [CA,N4], kappa_F [N3/N4]
FAM={
 '8V': dict(o1=('0.75','0.25'),F=('1.2','2.5'),off='V',km=C0,NS=1,T='1.28359',Lam='1.9656353',kF='4036',typ='V',Rc='4'),
 '8E': dict(o1=('0.2','0.3'),F=('0.8','2.5'),off='E',km=C0,NS=1,T='1.28359',Lam='0.4915932',kF='4.3e4',typ='E',Rc='3.5'),
}
# Referee fixes (audit/p4 §2, §3b): Line F weight e^{-beta(|c|-Rc)_+} vs e^{-beta|c|} costs e^{beta Rc}
# (Rc=K0=4 for V, K0-1/2=3.5 for E, lineF/code/cert_lift.py l.20; beta=2.5), and A_J <= 4/3 (both signs rho=(+-2,8)).
BETA=arb('2.5'); LOGAJ=(arb(4)/3).log()
def offset(typ): return arb('0.5') if typ=='V' else 1/(2*LAM)
def onestep(a,b,typ,km):
    """bound on ||L_tau||: H(rho_a,beta_a) -> H(rho_b,beta_b), uniform in tau; None if not admissible."""
    ra,ba=a; rb,bb=b
    th=(rb/LAM+offset(typ))/ra
    if not (th<1) or not (ba/LAM<=bb): return None
    return arb(6).sqrt()/(1-th**2).sqrt()*(ba/2).exp()*lettersum(2*PI*km*rb+ba/LAM)
def twostep(a,b,typ,km):
    best=None
    for i in range(1,80):
        for j in range(1,60):
            m=(arb(i)/20, arb(j)/20)
            s1=onestep(a,m,typ,km)
            if s1 is None: continue
            s2=onestep(m,b,typ,km)
            if s2 is None: continue
            v=s1*s2
            if best is None or v.upper()<best[0].upper(): best=(v,(i/20,j/20))
    return best
def consts(fam):
    d=FAM[fam]; o1=tuple(arb(x) for x in d['o1']); F=tuple(arb(x) for x in d['F'])
    inn=twostep(o1,F,d['typ'],d['km']); out=twostep(F,o1,d['typ'],d['km'])
    S=onestep(o1,o1,d['typ'],d['km'])
    return dict(CI=upper(inn[0]*out[0]),CI_in=upper(inn[0]),mid_in=inn[1],CI_out=upper(out[0]),mid_out=out[1],
                S=upper(S) if S is not None else None)
def hs_consts(fam,k):
    d=FAM[fam]; rho,beta=(arb(x) for x in d['o1'])
    dev=LAM/(2*(LAM-1)) if d['typ']=='V' else 1/(2*(LAM-1))
    theta=(rho*LAM**(-k)+dev)/rho; bb=beta*(1-LAM**(-k)); tanh=(bb.exp()-(-bb).exp())/(bb.exp()+(-bb).exp())
    Cpair=d['NS']/tanh*(2*beta*(dev+1)).exp()/(1-theta**2)
    logPA2=arb(0); W=arb(0)
    for j in range(k):
        tau=2*PI*d['km']*rho*LAM**(-j)+beta*LAM**(-(k-j))
        A=lettersum(tau); A1=lettersum(tau,1)
        logPA2+=2*A.log(); W+=2*A1/A*(LAM**(j-k)+LAM**(-j))
    logLp=Cpair.log()+logPA2+W.log()           # log of L' >= sum_g |c_g|(|s1 g| lam^{-k} + |s2 g|)
    return dict(Cpair=Cpair,logsupf=Cpair.log()+logPA2,logLp=logLp)
def r2tab():
    t={}
    for l in open(LOGS+'/r2_cert_x0.jsonl'):
        r=json.loads(l); assert r['x0_lower']==1.0 and r['xmax']==1.0
        t[(r['fam'],r['k'])]=arb(r['r2_upper'])
    return t
L2=arb(2).log(); LE=E0U.log()
def wbar(P1,P2):
    """max w with (P1-1)^w w! <= eps^P2 (certified upper bound: returns w s.t. f(w+1)>B is certified)."""
    lp=arb(P1-1).log(); B=P2*LE
    f=lambda w: w*lp+arb(w+1).lgamma()
    lo,hi=0,1
    while not (f(hi)>B): hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if f(m)>B: hi=m
        else: lo=m
    return hi-1
def make(fam,k,c,h,r2):
    d=FAM[fam]; Lam=arb(d['Lam']); kF=arb(d['kF']); T=arb(d['T'])
    lk=(T**3/(r2*Lam)).log()
    CIk=c['CI']*kF
    # Hmax = max_{0<=l<=k-1} min(max(1,S)^l, CI kF Lam^{l-4} (l>=5))
    S=max(c['S'],arb(1),key=lambda x:x.upper()) if c['S'] is not None else None
    def logH(l):
        opts=[]
        if S is not None: opts.append(l*S.log())
        if l>=5: opts.append(CIk.log()+(l-4)*Lam.log())
        return min(opts,key=lambda x:x.upper()) if opts else None
    logHmax=max((logH(l) for l in range(k)),key=lambda x:x.upper())
    c1log=(2*PI).log()+h['logLp']-arb(k).log()        # log c1, c1 = 2 pi L'/(k a), a=1
    K1=LOGAJ+BETA*arb(d['Rc'])+CIk.log()-4*Lam.log()+4*logHmax+(k-1)*LAM.log()-(2*arb(2).sqrt()).log()+2*(c1log-L2)+2  # + 2 log p - 2log(1-lam^-p)
    def logK(p,plo): return K1+2*arb(p).log()-2*(1-LAM**(-plo)).log()
    return lk,K1,logK,logHmax,c1log
def certify(fam,k,c,h,r2,X):
    lk,K1,logK,logHmax,c1log=make(fam,k,c,h,r2)
    def ok_int(P1,P2): return bool(wbar(P1,P2)*L2+logK(P2,P1) < P1*lk)
    # candidate p0: least p with pointwise condition on a doubling/bisection
    lo,hi=3,3
    while not ok_int(hi,hi): hi*=2
    lo=hi//2
    while hi-lo>1:
        m=(lo+hi)//2
        if ok_int(m,m): hi=m
        else: lo=m
    p0=hi
    # cover [p0,X] by intervals (adaptive split); if a single point fails, raise p0 past it and restart
    while True:
        stack=[(p0,X)]; bad=None; n=0
        while stack:
            a,b=stack.pop(); n+=1
            if ok_int(a,b): continue
            if a==b: bad=a; break
            m=(a+b)//2; stack.append((m+1,b)); stack.append((a,m))
        if bad is None: break
        p0=bad+1
    # analytic tail p>=X
    cp=(lk-(K1+2*arb(X).log()-2*(1-LAM**(-X)).log())/X)/L2
    tail=bool(cp>0) and bool(arb(X-1).log()+(cp*X).log()-1 > LE/cp) and bool(K1+2>0)
    return dict(fam=fam,k=k,r2=float(r2.upper()),log_kappa=float(lk.lower()),K1=float(K1.upper()),
                logHmax=float(logHmax.upper()),log_c1=float(c1log.upper()),p0=p0,X=X,intervals=n,tail_ok=tail,
                wbar_at_p0=wbar(p0,p0),logK_at_p0=float(logK(p0,p0).upper()))
if __name__=='__main__':
    t=r2tab(); res={}
    for fam in ['8V','8E']:
        c=consts(fam); print(fam,{k:(str(v) if not isinstance(v,arb) else v.str(8)) for k,v in c.items()},flush=True)
        res[fam]=dict(consts={k:(float(v.upper()) if isinstance(v,arb) else v) for k,v in c.items()},rows=[])
        for k in sorted({kk for (f,kk) in t if f==fam}):
            h=hs_consts(fam,k)
            XT=10**10
            row=certify(fam,k,c,h,t[(fam,k)],XT); row.update(Cpair=float(h['Cpair'].upper()),logsupf=float(h['logsupf'].upper()),logLp=float(h['logLp'].upper()))
            print(json.dumps(row),flush=True); res[fam]['rows'].append(row)
    json.dump(res,open(LOGS+'/h6_p0.json','w'),indent=1)
