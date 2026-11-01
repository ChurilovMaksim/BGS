# referee lineN21b: independent arb recomputation of the N15 KP criterion (g0=2..6) from N15 a_cert3.jsonl + N14 spans,
# formulas of N15 kp.py (polymer exclusion length l = span+g0; S0 = 2 sum |w| e^{a l}, S1 = 2 sum |w| l e^{a l}; tail 1.56e-8 weighted
# with l_t = 2*13+g0), and the budget/positivity statements with delta_true = 5.0313e-6.  delta does not enter the KP inequality.
import json, sys
from flint import arb, ctx
ctx.prec=80
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/a_cert3.jsonl')]
span={(r['a'],r['b']):r['span'] for r in map(json.loads,open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl'))}
MODEL={(1,0),(0,1),(2,0),(0,2)}; TAIL=arb('1.56e-8')
jr=max(span[(r['a'],r['b'])]/max(1,r['j']) for r in rows)
def S(a,g0):
    a=arb(a); bad=[(arb(r['absw_up']),span[(r['a'],r['b'])]+g0) for r in rows if (r['a'],r['b']) not in MODEL and r['zr']<g0]
    s0=2*sum((w*(a*l).exp() for w,l in bad),arb(0)); s1=2*sum((w*l*(a*l).exp() for w,l in bad),arb(0))
    lt=jr*13+g0; s0+=TAIL*(a*lt).exp()*2; s1+=TAIL*(lt+arb(2)/(1-arb('0.28')))*(a*lt).exp()*2
    return s0,s1
out={}
A={2:'2.329124e-6',3:'3.952295e-6',4:'5.93e-6',5:'8.005618e-6',6:'1.031499e-5'}
for g0,a in A.items():
    s0,s1=S(a,g0); lhs=s0+s1/(1+g0)
    out[g0]=dict(a=a,S0=float(s0.upper()),S1=float(s1.upper()),lhs=float(lhs.upper()),kp_ok=bool(lhs<arb(a)),kp_margin=float((arb(a)/lhs).lower()))
    print(g0,out[g0])
RL=arb('6.234e-4'); dt=arb('5.0313e-6'); S0=arb(out[4]['S0'])
out['budget']=dict(Abad_plus_delta=float((S0+dt).upper()),ratio_ReL=float((RL/(S0+dt)).lower()),leftover=float((RL-S0-dt).lower()),
     ln1pReL_minus=float(((1+RL).log()-S0-dt-arb('1.56e-8')).lower()),fails_200=bool(S0+dt>RL/200),
     old_v4=float((RL/(S0+arb('5.14476e-7'))).lower()),N16=float((RL/(S0+arb('2.470e-6'))).lower()))
print(out['budget']); json.dump(out,open('../logs/ref_kp.json','w'),indent=1)
