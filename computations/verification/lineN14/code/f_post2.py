"""N14 post-processing of c2_mid.jsonl (N13-F3 fix) -- same formulas as N13 f_post.py (W=(r_A r_B)^3 in ball arithmetic, h=1 uses single_eps,
s=-1 uses the + single), certified for the CORE FUNCTIONAL [CA-fp].  usage: f_post2.py [jsonl] [out]"""
import json, sys
from flint import acb, arb
src=sys.argv[1] if len(sys.argv)>1 else '/workspace/bgs-lineN/N14/logs/c2_mid.jsonl'
dst=sys.argv[2] if len(sys.argv)>2 else '/workspace/bgs-lineN/N14/logs/f_post2.json'
rows=[json.loads(l) for l in open(src)]
def ball(w):
    re=w['re']; im=w['im']; return acb(arb((re[0]+re[1])/2,(re[1]-re[0])/2),arb((im[0]+im[1])/2,(im[1]-im[0])/2))
def W(r): return (ball(r['A'])*ball(r['B']))**3
S={}
for r in rows:
    if r['kind']=='single': S[(r['name'],0)]=W(r)
    if r['kind']=='single_eps': S[(r['name'],1)]=W(r)
tp=arb(0); np_=0; ts=arb(0); ns=0; worst=[]; byG={}
for r in rows:
    if r['kind'] not in ('pair','short'): continue
    i,j=r['name'].split('+'); Wij=W(r)
    if r['kind']=='pair':
        d=abs(Wij-S[(i,0)]*S[(j,r['h'])]); tp+=d; np_+=1; worst.append((float(d.upper()),r['name'],r['h'],r['s'],r['G']))
        byG[r['G']]=byG.get(r['G'],0)+float(d.upper())
    else: ts+=abs(Wij); ns+=1
worst.sort(reverse=True)
out=dict(n_rows=len(rows),singles={f'{k[0]}|h{k[1]}':float(abs(v).upper()) for k,v in S.items()},coded_pairs=np_,
         coded_sum_abs_dev_upper=float(tp.upper()),coded_sum_abs_dev_mid=float(tp.mid()),short_types=ns,short_sum_abs_upper=float(ts.upper()),
         dev_by_G=byG,top=worst[:8])
print(json.dumps(out,indent=1)); json.dump(out,open(dst,'w'),indent=1)
