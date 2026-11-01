"""N20 [CA-fp: c3_mid radii (IEEE std model + libm <= 1 ulp); the exponent factor in arb]: certified shell sums
S2_up(j) = sum_{shell j, bad at g0} (|r_A|_up |r_B|_up)^2 and Sw_up(j) = sum |w|_up, and the shell-law constant
C_cert(j) = S2_up(j) / 2^{j(1-beta)},  beta = 2 ln(1/rho)/ln(lam), for rho = 0.2726 (N14 a_need convention, ~rho(K)) and 0.28.
Sources: N15 a_cert3.jsonl (j <= 12) + N20 a_cert_ext*.jsonl (j = 13, 14 if complete).  usage: shell_law.py
v2: summation inflation 1+1e-11 (referee minor; 8487 terms * 2^-53 ~ 9.4e-13)."""
import json, glob, collections, math
from flint import arb, ctx
ctx.prec=128
MODEL={(1,0),(0,1),(2,0),(0,2)}
rows={}
for l in open('/workspace/bgs-lineN/N15/logs/a_cert3.jsonl'):
    r=json.loads(l); rows[(r['a'],r['b'])]=(r['j'],r['zr'],r['rArB2_up'],r['absw_up'])
for f in glob.glob('/workspace/bgs-lineN/N20/logs/a_cert_ext*.jsonl'):
    for l in open(f):
        r=json.loads(l)
        if r.get('coded'): rows.setdefault((r['a'],r['b']),(r['j'],r['zr'],None,None)); continue
        rows[(r['a'],r['b'])]=(r['j'],r['zr'],r['rArB2_up'],r['absw_up'])
lam=3+2*arb(2).sqrt(); out={'shells':{}}
cnt=collections.Counter(v[0] for v in rows.values())
for g0 in (4,):
    S2=collections.defaultdict(float); Sw=collections.defaultdict(float); nb=collections.Counter()
    for ab,(j,zr,s2,w) in rows.items():
        if ab in MODEL or zr>=g0: continue
        S2[j]+=s2; Sw[j]+=w; nb[j]+=1
    for j in sorted(S2):
        rec=dict(n_classes=cnt[j],n_bad=nb[j],S2_up=S2[j]*(1+1e-11),Sw_up=Sw[j]*(1+1e-11))
        for rho in ('0.2726','0.28'):
            beta=2*(1/arb(rho)).log()/lam.log(); fac=(arb(2).log()*j*(1-beta)).exp()
            rec['C_cert_rho'+rho]=float((arb(rec['S2_up'])/fac).upper())
        out['shells'][j]=rec; print(j,rec)
json.dump(out,open('../logs/shell_law_v2.json','w'),indent=1)
