"""N14 (A) finite part [CA-fp, core functional]: re-evaluate every class of a_enum.jsonl with j<=Jc through the c2_mid chain
(midpoint + rigorous H-norm error), giving upper bounds |r|+rad and hence certified sum_bad |w| per shell (same polymer rule as a_post).
Core->true conversion (composite windows) not included (open, as for the replay)."""
import sys, json
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import c2_mid as M
Jc=int(sys.argv[1]); rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl')]
OUT='/workspace/bgs-lineN/N14/logs/a_cert.jsonl'; import os
done=set()
if os.path.exists(OUT):
    for l in open(OUT): r=json.loads(l); done.add((r['a'],r['b']))
with open(OUT,'a') as f:
    for r in rows:
        if r['j']>Jc or (r['a'],r['b']) in done: continue
        w=M.window(2*r['a'],2*r['b'])
        up=(w[0]['abs_up']*w[1]['abs_up'])**3
        f.write(json.dumps(dict(j=r['j'],a=r['a'],b=r['b'],zr=r['zr'],absw_up=up,rArB2_up=(w[0]['abs_up']*w[1]['abs_up'])**2,rad=[w[0]['rad'],w[1]['rad']],absw_float=r['absw']))+'\n'); f.flush()
print('done')
