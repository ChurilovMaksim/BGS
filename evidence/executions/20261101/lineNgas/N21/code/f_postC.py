"""N21 (A2): post-processing of the Lemma C boxes, N14 f_post2 formulas verbatim (W = (r_A r_B)^3 in arb ball arithmetic, h=1 uses
single_eps, s=-1 uses the + single).  Singles come from the G <= 15 replay; pairs from the replay (G <= 15) and from the G >= 16
extension.  Output: coded sum |dev| upper for G <= 15 and dev_by_G (upper) for every G.  [CA-fp boxes, arb post-processing]"""
import json, sys, glob
from flint import acb, arb
rows=[json.loads(l) for f in sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_replay_p*.jsonl')) for l in open(f)]
ext=[json.loads(l) for f in sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_ext_16_60_p*.jsonl')) for l in open(f)]
def ball(w):
    re=w['re']; im=w['im']; return acb(arb((re[0]+re[1])/2,(re[1]-re[0])/2),arb((im[0]+im[1])/2,(im[1]-im[0])/2))
def W(r): return (ball(r['A'])*ball(r['B']))**3
S={}
for r in rows:
    if r['kind']=='single': S[(r['name'],0)]=W(r)
    if r['kind']=='single_eps': S[(r['name'],1)]=W(r)
assert len(S)==10
tp=arb(0); np_=0; ts=arb(0); ns=0; byG={}; cntG={}; tmid=arb(0)
for r in rows+ext:
    if r['kind'] not in ('pair','short'): continue
    i,j=r['name'].split('+'); Wij=W(r)
    if r['kind']=='pair':
        d=abs(Wij-S[(i,0)]*S[(j,r['h'])]); G=r['G']
        byG[G]=byG.get(G,arb(0))+d; cntG[G]=cntG.get(G,0)+1   # v2 (referee F8): arb accumulation
        if G<=15: tp+=d; np_+=1
    else: ts+=abs(Wij); ns+=1
out=dict(n_replay_rows=len(rows),n_ext_rows=len(ext),singles={f'{k[0]}|h{k[1]}':float(abs(v).upper()) for k,v in S.items()},
         coded_pairs_G_le_15=np_,coded_sum_abs_dev_upper_G_le_15=float(tp.upper()),short_types=ns,short_sum_abs_upper=float(ts.upper()),
         dev_by_G={str(k):float(byG[k].upper()) for k in sorted(byG)},count_by_G={str(k):cntG[k] for k in sorted(cntG)})
print(json.dumps(out,indent=1)); json.dump(out,open(sys.argv[1] if len(sys.argv)>1 else '/workspace/bgs-lineN/N21/logs/f_postC.json','w'),indent=1)
