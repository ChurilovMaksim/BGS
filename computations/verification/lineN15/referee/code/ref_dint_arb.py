"""Referee lineN15: delta_int from N15 c3_mid boxes, own arb code (rectangle -> arb balls with outward rounding via arb from endpoints)."""
import json
from flint import arb, acb, ctx
ctx.prec=120
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/c3_mid.jsonl')]
def iv(a,b): return arb(a).union(arb(b))          # exact endpoints, union => contains [a,b]
def box(w): return acb(iv(*w['re']),iv(*w['im']))
def W(r): z=box(r["A"])*box(r["B"]); return z**3
S={(r['name'],0 if r['kind']=='single' else 1):W(r) for r in rows if r['kind'] in ('single','single_eps')}
t=arb(0); n=0; minrad=min(min(r['A']['rad'],r['B']['rad']) for r in rows)
for r in rows:
    if r['kind']!='pair': continue
    i,j=r['name'].split('+'); t+=abs(W(r)-S[(i,0)]*S[(j,r['h'])]); n+=1
out=dict(n_pairs=n,delta_int_upper=float(t.upper()),mid=float(t.mid()),min_rad=minrad)
print(out); json.dump(out,open('logs/ref_dint_arb.json','w'),indent=1)
