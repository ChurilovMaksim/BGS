"""N15 (2) explicit Kotecky-Preiss weight for the per-site bad-polymer gas [CA-fp numbers on the j<=12 finite part; tail term from Lemma D].
Polymer gamma = bad cluster word (a_post rule, internal zero-runs < g0), exclusion length l(gamma) = span(gamma) + g0 (gamma excludes every
polymer starting within l(gamma) sites to its left or l(gamma') to its right).  Activity |w(gamma)| <= absw_up (a_cert3), factor 2 per site
(class mod +-eps^Z, sign).  KP (Kotecky-Preiss 1986, 1D form) with a(gamma) = a*l(gamma):
   sum_{gamma' not~ gamma} |w(gamma')| e^{a l(gamma')} <= l(gamma) S0(a) + S1(a) <= a l(gamma)   for all gamma
   <=  S0(a) + S1(a)/l_min <= a,     S0(a) = 2 sum_{anchored} |w| e^{a l},  S1(a) = 2 sum |w| l e^{a l},  l_min = 1 + g0.
Conclusion: per-site log-correction |f_bad| <= S0(a) (cluster sum anchored at a site <= |w|e^{a(gamma)} summed).  usage: kp.py certjsonl"""
import sys, json, math, collections
rows=[json.loads(l) for l in open(sys.argv[1])]
span={(r['a'],r['b']):r['span'] for r in map(json.loads,open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl'))}
MODEL={(1,0),(0,1),(2,0),(0,2)}
TAIL=1.56e-8          # Lemma D tail of 2 sum_{j>12} |w| (N14 sec.6, referee-confirmed)
out={}
for g0 in (2,3,4,5,6):
    bad=[(r['absw_up'],span[(r['a'],r['b'])]+g0) for r in rows if (r['a'],r['b']) not in MODEL and r['zr']<g0]
    lmax=max(l for _,l in bad); jmax_ratio=max(span[(r['a'],r['b'])]/max(1,r['j']) for r in rows)
    def S(a):
        s0=2*sum(w*math.exp(a*l) for w,l in bad); s1=2*sum(w*l*math.exp(a*l) for w,l in bad)
        # tail j>12: spans <= jmax_ratio*j + g0; weight with l e^{a l}, l <= (jmax_ratio+1)*j crude per-shell factor bounded via geometric decay
        lt=jmax_ratio*13+g0; s0+=TAIL*math.exp(a*lt)*2; s1+=TAIL*(lt+2/(1-0.28))*math.exp(a*lt)*2   # [P-sketch] tail weighting
        return s0,s1
    a=1e-6
    for _ in range(50):
        s0,s1=S(a); a=1.05*(s0+s1/(1+g0))
    s0,s1=S(a); ok=s0+s1/(1+g0)<=a
    out[g0]=dict(a=a,S0=s0,S1=s1,kp_ok=ok,l_max_finite=lmax,span_per_j_max=jmax_ratio,A_bad_KP=s0,A_bad_plain=2*sum(w for w,_ in bad)+TAIL)
    print(g0,out[g0])
json.dump(out,open('/workspace/bgs-lineN/N15/logs/kp_'+sys.argv[1].split('/')[-1].replace('.jsonl','')+'.json','w'),indent=1)
