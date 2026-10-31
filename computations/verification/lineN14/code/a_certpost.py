"""N14: certified finite part of A_bad from a_cert.jsonl [CA-fp, core functional]: 2*sum |w|_up over bad clusters (a_post rule) with j<=Jc."""
import json, collections
rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/a_cert.jsonl')]
MODEL={(1,0),(0,1),(2,0),(0,2)}; out={}
Jc=max(r['j'] for r in rows); complete=collections.Counter(r['j'] for r in rows)
for g0 in (2,3,4,5,6):
    S=collections.defaultdict(float)
    for r in rows:
        if (r['a'],r['b']) in MODEL or r['zr']>=g0: continue
        S[r['j']]+=r['absw_up']
    out[g0]=dict(A_bad_cert=2*sum(S.values()),per_shell=dict(S))
    print('g0',g0,'certified 2*sum|w|_up = %.5e'%(2*sum(S.values())))
out['shell_counts']=dict(complete); out['max_rel_rad']=max(max(r['rad'])/max(1e-300,(r['absw_float'])**(1/6)) for r in rows)
print('classes',len(rows),'shells',dict(complete))
json.dump(out,open('/workspace/bgs-lineN/N14/logs/a_certpost.json','w'),indent=1)
