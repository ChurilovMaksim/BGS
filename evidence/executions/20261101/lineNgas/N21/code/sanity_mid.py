"""N21 sanity [N]: midpoint (float core-chain) interaction |W_ij - W_i W_j| per G vs the certified bounds (box f_postC, analytic tail_DT)."""
import json, glob
rows=[json.loads(l) for f in sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_replay_p*.jsonl'))+sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_ext_16_60_p*.jsonl')) for l in open(f)]
def W(r): a=complex(*r['A']['mid']); b=complex(*r['B']['mid']); return (a*b)**3
S={}
for r in rows:
    if r['kind']=='single': S[(r['name'],0)]=W(r)
    if r['kind']=='single_eps': S[(r['name'],1)]=W(r)
mid={}; cnt={}
for r in rows:
    if r['kind']!='pair': continue
    i,j=r['name'].split('+'); d=abs(W(r)-S[(i,0)]*S[(j,r['h'])]); mid[r['G']]=mid.get(r['G'],0)+d; cnt[r['G']]=cnt.get(r['G'],0)+1
box=json.load(open('/workspace/bgs-lineN/N21/logs/f_postC.json'))['dev_by_G']
tl=json.load(open('/workspace/bgs-lineN/N21/logs/tail_DT_40_200.json'))['T_by_G']
out={}
for G in sorted(mid):
    out[G]=dict(n=cnt[G],mid=mid[G],box=box.get(str(G)),analytic=tl.get(str(G)))
    print(G,cnt[G],'mid %.3e'%mid[G],'box %s'%('%.3e'%box[str(G)] if str(G) in box else '-'),'analytic %s'%('%.3e'%tl[str(G)] if str(G) in tl else '-'))
json.dump(out,open('/workspace/bgs-lineN/N21/logs/sanity_mid.json','w'),indent=1)
