"""N13 post-processing of the arb replay (c_replay.jsonl): for the CORE FUNCTIONAL r~ (certified enclosures):
 coded pairs: |W_ij - W_i W_j| <= upper(|W_ij - W_i W_j|) with W = (r_A r_B)^3 in ball arithmetic (singles from the same replay; h=1 uses single_eps,
 sign s=-1 uses the + single (r(-e)=r(e) checked on the replay data where available));  short types: upper |W|.
 Reports totals over the types done so far.  Conversion core-functional -> true weight: NOT included (open, see REPORT_N13 sec 3)."""
import json
from flint import acb, arb
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N13/logs/c_replay.jsonl')]
def ball(win): 
    re=win['re']; im=win['im']
    return acb(arb((re[0]+re[1])/2,(re[1]-re[0])/2),arb((im[0]+im[1])/2,(im[1]-im[0])/2))
def W(r): return (ball(r['A'])*ball(r['B']))**3
S={}; 
for r in rows:
    if r['kind']=='single': S[(r['name'],0)]=W(r)
    if r['kind']=='single_eps': S[(r['name'],1)]=W(r)
tot_pair=arb(0); n_pair=0; tot_short=arb(0); n_short=0; worst=[]
for r in rows:
    if r['kind'] not in ('pair','short'): continue
    i,j=r['name'].split('+')
    if (i,0) not in S or (j,r['h']) not in S: continue
    Wij=W(r)
    if r['kind']=='pair':
        d=abs(Wij-S[(i,0)]*S[(j,r['h'])]); tot_pair+=d; n_pair+=1; worst.append((float(d.upper()),r['name'],r['h'],r['s'],r['G']))
    else:
        tot_short+=abs(Wij); n_short+=1
worst.sort(reverse=True)
out=dict(n_rows=len(rows),singles={f'{k[0]}|h{k[1]}':float(abs(v).upper()) for k,v in S.items()},
         coded_pairs_done=n_pair,coded_sum_abs_dev_upper=float(tot_pair.upper()),short_done=n_short,short_sum_abs_upper=float(tot_short.upper()),top=worst[:8])
print(json.dumps(out,indent=1)); json.dump(out,open('/workspace/bgs-lineN/N13/logs/f_post.json','w'),indent=1)
