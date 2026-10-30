"""Summarise the B1 directed-rounding run: coverage, validity, per-interval rho/C, m+ (delta=0.01)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json, glob, math, os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
iv=json.load(open(os.path.join(HERE,'b1_intervals.json')))
rows=[]; missing=[]
for i,(e0,e1) in enumerate(iv):
    f=os.path.join(HERE,'..','logs','b1','out',f'iv_{i:03d}.jsonl')
    if not os.path.exists(f): missing.append(i); continue
    L=[json.loads(l) for l in open(f)]; s=L[-1]; per=L[:-1]
    assert s['summary'] and s['e0']==e0 and s['e1']==e1 and len(per)==4 and sorted(r['a'] for r in per)==[0,1,2,3]
    valid=all(r['valid'] for r in per) and max(r['rho'] for r in per)<1
    rho=max(r['rho'] for r in per); C=sum(r['C'] for r in per)
    mplus=math.ceil(1+math.log(C/0.01)/(-math.log(rho)))
    rows.append(dict(idx=i,e0=e0,e1=e1,valid=valid,rho=rho,C=C,m_plus_0p01=mplus,rho_a0=[r for r in per if r['a']==0][0]['rho'],
                     states=per[0]['states'],src=s.get('source','second-reader run '+s.get('finished','')),secs=s.get('secs')))
done=len(rows); ok=sum(r['valid'] for r in rows)
cont=all(rows[k]['e1']==rows[k+1]['e0'] for k in range(len(rows)-1)) if not missing else False
S=dict(intervals=len(iv),done=done,valid=ok,missing=missing,failures=[r['idx'] for r in rows if not r['valid']],
       coverage=[iv[0][0],iv[-1][1]] if not missing else None,contiguous_closed=cont,
       rho_max=max(r['rho'] for r in rows),rho_min=min(r['rho'] for r in rows),C_max=max(r['C'] for r in rows),
       m_plus_at_eta1=rows[0]['m_plus_0p01'] if rows and rows[0]['idx']==0 else None,
       m_plus_max=max(r['m_plus_0p01'] for r in rows),
       method='audit/derand23/code/t9_cert.py (referee, unmodified; sha256 2dee8e5490d0ebff3a0793ffbdc8dae11281ef6396394c1a7b72a49b9d118947), driver runner.py')
json.dump(dict(summary=S,rows=rows),open(os.path.join(HERE,'..','logs','b1','b1_summary.json'),'w'),indent=1)
with open(os.path.join(HERE,'..','logs','b1','b1_summary.txt'),'w') as f:
    f.write(json.dumps(S)+'\n')
    for r in rows: f.write(f"{r['idx']:3d} {r['e0']:10.5f} {r['e1']:10.5f} valid={r['valid']} rho={r['rho']:.7f} (a=0: {r['rho_a0']:.7f}) C={r['C']:.3e} m+={r['m_plus_0p01']} states={r['states']}\n")
print(json.dumps(S))
