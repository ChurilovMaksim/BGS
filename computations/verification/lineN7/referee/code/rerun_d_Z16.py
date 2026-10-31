"""N7 [CA]: explicit bound |Z_(+-2,16)(m)| <= B16(m) (per rho) from (i) J3 rig_spec 'rest' certificates (all reps except the 8 V untwisted
dominant ones) and (ii) N7 'dom' certificates for those 8 (a_dom16.py): spectrum in {|z-b11|<=r1} u {|z|<0.95}.
||T^{m-1}|| <= r1 (|b11|+r1)^{m-1} fullR1/(1-F1) + R^m fullR2/(1-F2) (Cauchy, two contours); |tr_J T^m| <= (1/2)||T||_1 ||T^{m-1}||;
Z = (1-lam^-m) sum_{8 blocks}[tr_J V^m - tr_J E^m] (J3 assemble16 read-out, TRACE-226 L16).
Outputs: C16 with B16(m) <= C16 * 1.6355^m for all m>=3; m1 = least m=3p beyond which 2 B16^2 <= ... (Sigma_rho|Z_rho|^2 <= 4|Z8|^2);
p16 = least p beyond which the (+-2,16) members at ALL levels (Dev floor, Robin) cost <= delta16 * F_m (delta16 = 0.01)."""
import json, os
from flint import arb, ctx
ctx.prec=128
J3='/workspace/bgs-lineJ/J3'; N7='/workspace/bgs-lineN/N7'
reps=json.load(open(J3+'/logs/blocks16_reps.json')); mem=reps['members']
P=1+arb(2)**-40
def rest(T,r):
    c=json.load(open(f'{J3}/logs/cert/{T}_r{r}_u_b0_rest.json')); B=json.load(open(f'{J3}/data/cert/{T}_r{r}_u.json'))
    assert c['certified'] and c['mode']=='rest'
    R=arb(c['R']); SY=arb(c['SY_R'])*P; kap=arb(c['kappa_str'].split('+/-')[0].strip('[ ]'))+arb('1e-18')
    Xn=arb(B['Xnorm'])*P; F=arb(c['F_R2'])*P; fullR=(kap*SY+1/R)*(1+Xn/R)+1/R
    return [(R,arb(B['trace_norm'])*P/2*fullR/(1-F)*R**-1*R, 'rest')]   # term C*R^m  (||T^{m-1}|| <= R^m fullR/(1-F))
def dom(r):
    c=json.load(open(f'{N7}/logs/dom16_V_r{r}.json')); B=json.load(open(f'{N7}/data/V_r{r}_u.json')); assert c['certified'] and c['mode']=='dom'
    kap=arb(c['kappa_str'].split('+/-')[0].strip('[ ]'))+arb('1e-18'); Xn=arb(B['Xnorm'])*P; tn=arb(B['trace_norm'])*P/2
    r1=arb(c['r1']); R=arb(c['R']); ab=arb(c['mu_abs_upper'])*P   # |b11|+r1
    z1=ab-2*r1  # |b11|-r1 lower: contour points have |z|>=|b11|-r1; fullR uses za=|b11|-r1 as in rig_spec
    f1=(kap*arb(c['Rcore_r1'])*P+1/z1)*(1+Xn/z1)+1/z1; f2=(kap*arb(c['Rcore_R'])*P+1/R)*(1+Xn/R)+1/R
    F1=arb(c['F_R1'])*P; F2=arb(c['F_R2'])*P
    # ||T^{m-1}|| <= r1*ab^{m-1} f1/(1-F1) + R^m f2/(1-F2)  ->  terms C*rate^m
    return [(ab, tn*r1*f1/(1-F1)/ab,'dom'),(R, tn*f2/(1-F2),'domrest')]
DOMS={int(x[len('dom16_V_r'):-5]) for x in os.listdir(N7+'/logs') if x.startswith('dom16_V_r') and x.endswith('.json')}
terms={}
for r,lst in mem.items():
    r=int(r)
    for T in ('V','E'):
        tt=dom(r) if (T=='V' and r in DOMS) else rest(T,r)
        for (case,blk) in lst: terms.setdefault(case,[]).extend(tt)
LAM=3+2*arb(2).sqrt(); EPS=1+arb(2).sqrt()
for case,tt in terms.items():
    assert max(t[0] for t in tt) < arb('1.6355'), (case,[float(t[0].upper()) for t in tt])
def B16(m,case): return (1-LAM**(-m))*sum((C*R**m for R,C,_ in terms[case]),arb(0))
RATE=arb('1.6355')
C16=max(max((sum((C*(R/RATE)**3 if R<RATE else C for R,C,_ in terms[c]),arb(0))) for c in terms).upper() for _ in [0]) if False else None
C16=arb(0)
for c,tt in terms.items():
    s=sum((C for R,C,_ in tt),arb(0))      # since R<=RATE, C R^m <= C RATE^m
    if s>C16: C16=s
mu=arb('1.9154712')
def Z8lo(m): return (1-LAM**(-m))*(mu**m-arb('3012.3'))/2
cases_all=list(terms)
def B16max(m): return max((B16(m,c) for c in cases_all), key=lambda x: float(x.upper()))
out=dict(dom_reps=sorted(DOMS),rate=1.6355,C16=float(C16.upper()),
         max_rates={c:float(max(t[0] for t in tt).upper()) for c,tt in terms.items()})
m=3
while not (2*B16max(m)**2 <= 2*Z8lo(m)**2 and all(2*B16max(mm)**2 <= 2*Z8lo(mm)**2 for mm in range(m,m+60,6))): m+=6
out['m1_sum_rho_le_4Z8sq']=m
# (+-2,16) at all levels: sum_rho sum_d n_d|Z16|^2/d^2 <= 2 B16^2 * (sigma(h_m)/h_m - 1) <= 2 B16^2 (e^gamma lnln h_m + 0.6483/lnln h_m) (Robin 1984, n>=3)
# vs F_m >= 2.06e-3 p |Z8|^2 / h_p (N6 + F5 composite loss, worst case omega(h_p) <= p ln eps/ln(2p-1)), h_p <= eps^p, h_m <= eps^{3p}
EG=arb('1.7810724179901979852')
def ok16(p,delta=arb('0.01')):
    m=3*p; ll=(3*p*EPS.log()).log()
    lhs=2*B16max(m)**2*(EG*ll+arb('0.6483')/ll); rhs=delta*arb('2.06e-3')*p*Z8lo(m)**2/EPS**p
    return lhs<=rhs
p=3
while not all(ok16(pp) for pp in range(p,p+200,2)): p+=2
out['p16_all_levels_delta0.01']=p
print(json.dumps(out,indent=1)); json.dump(out,open('/workspace/audit/lineN7/logs/rerun_d_Z16.json','w'),indent=1)
# referee additions: split constants by rate class, sharp B16 at a few m
dc={}
for c,tt in terms.items():
    dc[c]=dict(C_dom=float(sum((C for R,C,k in tt if k=='dom'),arb(0)).upper()),C_rest=float(sum((C for R,C,k in tt if k!='dom'),arb(0)).upper()),
               max_rest_rate=float(max((R for R,C,k in tt if k!='dom'),key=lambda x: float(x.upper())).upper()))
print('split', json.dumps(dc['3,2']), json.dumps(max(dc.values(),key=lambda v:v['C_dom'])))
for m in (51,57,1017,3495):
    b=B16max(m); print('m',m,'B16/1.6355^m',float((b/RATE**m).upper()),'B16/Z8lo',float((b/Z8lo(m)).upper()))
