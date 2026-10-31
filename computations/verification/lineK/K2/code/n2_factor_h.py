"""N2 [N/P-check]: prime factors of h_p and of the primitive part of h_{3p} for small primes p (where factoring is feasible),
classified by rank and by size class relative to p^2 (Weil range ~ c p^2) and L_m.  Shows which levels lie in the open range."""
import sympy, json, math, sys, signal
def h(m):
    a,b=1,1  # (1+sqrt2)^1
    x,y=1,0
    for _ in range(m): x,y=x+2*y,x+y
    return x   # h_m = Re (1+sqrt2)^m  (odd m: h^2 - 2U^2 = -1 ... )
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)
rows=[]
for p in [p for p in sympy.primerange(5,80)]:
    m=3*p; H=h(m); res=dict(p=p,m=m,log10_h=round(math.log10(H),1))
    try:
        signal.alarm(120); F=sympy.factorint(H); signal.alarm(0)
    except TO:
        res['factored']=False; rows.append(res); print(res,flush=True); continue
    lev=[]
    for q,e in sorted(F.items()):
        if q==7: lev.append(dict(q=7,e=int(e),cls='7')); continue
        lg=math.log(q)/math.log(p)
        lev.append(dict(q=str(q),e=int(e),log_p_q=round(lg,2),qm1_mod_2p=int((q-1)%(2*p)),
                        cls=('Weil(<p^2)' if q<p*p else ('mid(p^2..sqrt h)' if q*q<=H else 'not included (>sqrt h)'))))
    res['factored']=True; res['levels']=lev; rows.append(res); print(json.dumps(res),flush=True)
json.dump(rows,open('logs/n2_factor_h.json','w'),indent=1)
