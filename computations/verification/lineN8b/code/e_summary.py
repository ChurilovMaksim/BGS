"""N8b [N]: summary of b_cline runs. For each run: h-rank, amplification A = h_p/c (weight of a level-c point relative to an h_p point),
rel_abs/rel_signed (pattern sum over family term, both conjugate lines, Lin weights), and per top class the effective decay exponent
beta_eff = -log(|r|/|w*|)/log(N(e)/4), N(e) = (h_M/c)*depth  (h_M = h_p for c|h_p, h_{3p} for c|K_p), |w*| = 3.955e-4."""
import json, math
from sympy import factorint
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x
lam=3+2*math.sqrt(2); W=3.955e-4
rows=[]
for l in open('logs/b_cline.jsonl'):
    d=json.loads(l); p=d['p']; c=d['c']; hp=xy(p); H=xy(3*p)
    rk='p' if hp%c==0 else ('3p' if (H//hp)%c==0 else 'mixed')
    hM=hp if rk=='p' else H
    A=hp/c
    be=[]
    for t in d['top'][:6]:
        if t['absr']<=t['floor']*3 or t['depth']==0: continue
        Ne=(hM/c)*t['depth']
        if Ne>4: be.append(-math.log(t['absr']/W)/math.log(Ne/4))
    rows.append((p,c,rk,d['line'],d['mode'],d['classes'],A,d['rel_abs'],d['rel_abs_upper'],d['rel_signed'],min(be) if be else None,d['top'][0]['depth'] if d['top'] else None,d['top'][0]['absr'] if d['top'] else None))
rows.sort()
print('%3s %16s %4s %9s %10s %5s %9s %9s %9s %10s %6s %5s %9s'%('p','c','rank','line','mode','cls','h_p/c','rel_abs','rel_up','rel_sgn','b_min','dep','|r|top'))
for r in rows:
    print('%3d %16d %4s %9s %10s %5d %9.2e %9.2e %9.2e %+10.2e %6s %5s %9.2e'%(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],'%.2f'%r[10] if r[10] else '-',r[11],r[12]))
json.dump(rows,open('logs/e_summary.json','w'))
