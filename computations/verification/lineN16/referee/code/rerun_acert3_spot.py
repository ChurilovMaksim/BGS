"""lineN16: (i) sanity over all a_cert3 rows: absw_up >= absw_float (N14 float |w|); (ii) re-run c3_mid.window on 10 classes, compare absw_up."""
import sys, json
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N15/code'); import c3_mid as M
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/a_cert3.jsonl')]
bad=[r for r in rows if r['absw_up']<r['absw_float']]
mx=max(r['absw_up']/r['absw_float']-1 for r in rows if r['absw_float']>0)
idx=[0,1,7,50,400,1000,2000,3000,4000,len(rows)-1]; out=[]
for i in idx:
    r=rows[i]; w=M.window(2*r['a'],2*r['b']); up=(w[0]['abs_up']*w[1]['abs_up'])**3
    out.append(dict(i=i,j=r['j'],rel=abs(up-r['absw_up'])/r['absw_up']))
res=dict(n=len(rows),n_up_below_float=len(bad),max_rel_excess=mx,spot=out,max_spot_rel=max(o['rel'] for o in out))
json.dump(res,open('/workspace/audit/lineN16/logs/rerun_acert3_spot.json','w'),indent=1); print(res)
