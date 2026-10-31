"""N11 [P mod model-form]: robustness of |1+X| >= 1 under perturbations |R'-R|<=te, |w'-w*|<=to of the gas parameters
X = 2[e^{pR'}(sinh(2pw')+1)-1].  Lower bound LB(p) = max(caseA, caseB) on |1+X|-1 (see REPORT_N11 §3).
Outputs, for t on a grid (te=to=t and te=2t,to=t etc.), min over odd p in [3, PMAX] of LB(p)/ (8p*Re(w*+c0)) and the
p beyond which caseA alone is >= its value at PMAX and increasing (monotone: both factors increasing in p)."""
import math, json, numpy as np
ws=complex(3.43579708677916e-4,1.9579583160123678e-4); R=complex(6.184977715347842e-05,-1.9431217694966584e-05)
c0=complex(2.9866e-5,-6.599e-6); lin1=8*(ws+c0).real
def caseA(p,te,to):
    a=2*p*(ws.real-to)
    if a<=0: return -1e9
    return 2*math.exp(p*(R.real-te))*(math.sinh(a)-1)-2
def caseB(p,te,to):
    U=p*(abs(R)+te); V=2*p*(abs(ws)+to)
    lin=p*(R.real-te)+2*p*(ws.real-to)
    err=U*U*math.exp(U)/2+V**3*math.cosh(V)/6+U*math.exp(U)*math.sinh(V)
    return 2*(lin-err)          # lower bound on Re X  (and |1+X|-1 >= Re X when Re X>=0... used only if >0)
import cmath
def caseC(p,te,to):   # exact nominal value minus rigorous Lipschitz perturbation bound
    Xn=2*(cmath.exp(p*R)*(cmath.sinh(2*p*ws)+1)-1)
    ch=math.cosh(2*p*(ws.real+to)); eR=math.exp(p*R.real)
    pert=2*(eR*(math.expm1(p*te))*(ch+1)+eR*2*p*to*ch)
    return abs(1+Xn)-1-pert
def LB(p,te,to): return max(caseA(p,te,to),caseB(p,te,to),caseC(p,te,to))
out=[]
PMAX=20001
for (fe,fo) in [(1,1),(2,1),(1,0)]:
    for t in [0,1e-5,2e-5,5e-5,1e-4,1.5e-4,2e-4,2.5e-4]:
        te,to=fe*t,fo*t
        ps=range(3,PMAX+1,2); vals=[LB(p,te,to) for p in ps]; rel=[v/(lin1*p) for v,p in zip(vals,ps)]
        i=int(np.argmin(rel)); ok=all(v>0 for v in vals)
        # beyond PMAX: caseA increasing if R.real-te>-2(ws.real-to) and sinh term >1
        grow=(R.real-te)+2*(ws.real-to)>0 and caseA(PMAX,te,to)>0
        r=dict(te=te,to=to,all_positive=ok,min_rel=rel[i],p_at_min=list(ps)[i],min_abs=min(vals),caseA_pos_from=next((p for p in ps if caseA(p,te,to)>0),None),caseA_at_PMAX=caseA(PMAX,te,to),tail_grows=grow)
        out.append(r); print(json.dumps(r))
json.dump(out,open('/workspace/bgs-lineN/N11/logs/r_robust.json','w'),indent=1)
