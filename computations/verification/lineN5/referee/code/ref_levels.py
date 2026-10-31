"""Referee [N]: divisor structure of h_m (m = 3p) relative to h_p: which other included levels d | h_m (d <= sqrt h) lie below h_p
and are not multiples of h_p or equal to 7 (candidates that could offset the level-h_p deviation)."""
import sys, json, math
sys.path.insert(0,'/workspace/bgs-lineI/code'); from law import mdata
from sympy import factorint, divisors
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
out=[]
for p in [int(t) for t in sys.argv[1].split(',')]:
    h=mdata(3*p)['h']; q=hp(p); rest=h//q; f=factorint(rest); fq=factorint(q)
    divs=[int(d) for d in divisors(h) if d>1 and int(d)*int(d)<=h]
    below=[d for d in divs if d<q and d%q!=0 and d!=7]
    rec=dict(p=p,h_m_digits=len(str(h)),h_p=str(q),h_p_factors={str(k):v for k,v in fq.items()},cofactor_factors={str(k):v for k,v in f.items()},
             n_included_divisors=len(divs),other_levels_below_h_p=[str(d) for d in below][:40],n_other_below=len(below),
             h_p_times_sum_1_over_d=float(sum(1/int(d) for d in below)*int(q)))
    out.append(rec); print(json.dumps(rec),flush=True)
json.dump(out,open('logs/ref_levels.json','w'),indent=1)
