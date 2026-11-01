"""N20 sec.3 [CA: python-flint arb ball arithmetic for every transcendental step; finite parts are the CA-fp values of N15/N20]:
conditional bookkeeping  H1-shell(C, J0)  ==>  KP (H3) with explicit a, per-site A_bad^KP and remaining budget.
H1-shell(C,J0):  S2(j) := sum_{shell j, bad} |r_A r_B|^2 <= C * 2^{j(1-beta)},  beta = 2 ln(1/rho)/ln(lam), rho = 0.28, all j > J0.
Tail (per site, factor 2):  T0 = 2 sum_{j>J0} sum|w| e^{a l} <= 2 C^{3/2} e^{a g0} sum_{j>J0} (q e^{2a})^j,      q = 2^{(3/2)(1-beta)}
                            T1 = 2 sum_{j>J0} sum|w| l e^{a l} <= 2 C^{3/2} e^{a g0} sum_{j>J0} (2j+g0) (q e^{2a})^j
 (l3<=l2: sum|w| <= S2^{3/2} per shell [P, Lean l3_le_l2];  l(gamma) = span + g0 <= 2j + g0 for j >= 5 [P-sketch, sec.3]).
KP: S0 + S1/(1+g0) <= a with S0 = S0fin + T0, S1 = S1fin + T1 (S0fin, S1fin at the given a from the certified finite part).
usage: tail_kp.py   (writes ../logs/tail_kp_v2.json)
v2 (referee lineN20 fix 1): delta_true <= 5.0313e-6 (N21 v2, all G) in budget_left and in the half-budget threshold;
(Float sums here were already inflated by 1e-9; the 1+1e-11 minor fix is in shell_law.py.)  C_needed is computed at a = 0 (no e^{a(2j+g0)} factor), N14 a_need convention."""
DT="5.0313e-6"
import json, math, sys
from flint import arb, ctx
ctx.prec=200
lam=3+2*arb(2).sqrt(); rho=arb('0.28')
beta=2*(1/rho).log()/lam.log(); q=(arb(2).log()*arb(1.5)*(1-beta)).exp()
print('beta',beta.str(12),'q',q.str(12))
# certified finite part rows (absw_up, span, j, zr): N15 a_cert3 (j<=12) + N20 a_cert_ext (j=13..15 if present)
span={}
for l in open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl'):
    r=json.loads(l); span[(r['a'],r['b'])]=r['span']
rows=[]
for l in open('/workspace/bgs-lineN/N15/logs/a_cert3.jsonl'):
    r=json.loads(l); rows.append((r['absw_up'],span[(r['a'],r['b'])],r['j'],r['zr'],(r['a'],r['b'])))
import os
import glob; ext_shells={}
for EXT in glob.glob('/workspace/bgs-lineN/N20/logs/a_cert_ext*.jsonl'):
    for l in open(EXT):
        r=json.loads(l)
        if r.get('coded'): continue
        rows.append((r['absw_up'],r['span'],r['j'],r['zr'],(r['a'],r['b'])))
MODEL={(1,0),(0,1),(2,0),(0,2)}
def fin(J0,g0,a):
    s0=s1=0.0
    for w,sp,j,zr,ab in rows:
        if j>J0 or ab in MODEL or zr>=g0: continue
        l=sp+g0; s0+=2*w*math.exp(a*l); s1+=2*w*l*math.exp(a*l)
    # float sums of <= 2e4 positive terms: relative rounding <= 2e4*2^-53 < 1e-11; inflate by 1e-9
    return arb(s0)*(1+arb('1e-9')), arb(s1)*(1+arb('1e-9'))
def tail(C,J0,g0,a):
    r=q*(2*arb(a)).exp(); J=J0+1
    g=r**J/(1-r); gj=r**J*(J-(J-1)*r)/(1-r)**2         # sum_{j>=J} r^j,  sum_{j>=J} j r^j
    pref=2*arb(C)**arb(1.5)*(arb(a)*g0).exp()
    return pref*g, pref*(2*gj+g0*g)
def solve(C,J0,g0):
    a=1e-6
    for _ in range(200):
        s0,s1=fin(J0,g0,a); t0,t1=tail(C,J0,g0,a); need=(s0+t0+(s1+t1)/(1+g0)).upper()
        a=float(need)*1.02
    s0,s1=fin(J0,g0,a); t0,t1=tail(C,J0,g0,a); S0=s0+t0; S1=s1+t1; lhs=S0+S1/(1+g0)
    return dict(C=C,J0=J0,g0=g0,a=a,S0fin=float(s0.upper()),S1fin=float(s1.upper()),T0=float(t0.upper()),T1=float(t1.upper()),
                S0=float(S0.upper()),S1=float(S1.upper()),KP_lhs=float(lhs.upper()),KP_ok=bool(lhs<arb(a)),
                budget_left=float((arb('6.234e-4')-S0-arb(DT)).lower()))
out=dict(beta=[float(beta.lower()),float(beta.upper())],q=[float(q.lower()),float(q.upper())],
         n_rows=len(rows),shells=sorted(set(r[2] for r in rows)),cases=[])
Jmax=max(r[2] for r in rows)
for J0 in sorted(set([12,13,Jmax])):
    for C in (0.082,0.04,4.4e-4*2,4.4e-4):
        res=solve(C,J0,4); out['cases'].append(res); print(res,flush=True)
# C_needed(J0) for 'tail <= half the remaining budget' (a_need convention) and for 'T0 <= 1e-6'
for J0 in sorted(set([12,13,14,Jmax])):
    r=q; J=J0+1; g=r**J/(1-r)
    half=(arb('6.234e-4')-arb(DT))/2
    for tgt in (half,arb('1e-6')):
        Cn=(arb(tgt)/(2*g))**(arb(2)/3); out.setdefault('C_needed',{})[f'J0={J0},T0<={float(tgt.upper()):.6g}']=float(Cn.lower())
print(out['C_needed'])
json.dump(out,open('../logs/tail_kp_v2.json','w'),indent=1)
