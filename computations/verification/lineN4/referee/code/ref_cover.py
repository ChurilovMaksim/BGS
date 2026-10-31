"""Referee: independent exact coverage of [0,1] by the 8V accepted cells (own label parser), plus stats."""
import json,sys
from fractions import Fraction as Fr
NC0=400; cells=[]
for f in sys.argv[1:]:
    for l in open(f):
        d=json.loads(l)
        if d['kind']=='cell': cells.append(d)
def iv(lab):
    k=0
    while k<len(lab) and lab[k].isdigit(): k+=1
    i=int(lab[:k]); a=Fr(i,NC0); w=Fr(1,NC0)
    for ch in lab[k:]:
        assert ch in 'LR'; w/=2; a+= w if ch=='R' else 0
    return a,a+w
I=sorted(iv(c['lab']) for c in cells)
ok = I[0][0]==0 and I[-1][1]==1 and all(I[j][1]==I[j+1][0] for j in range(len(I)-1))
for c in cells:
    a,b=iv(c['lab']); assert abs(float((a+b)/2)-c['tc'])<1e-15 and abs(float((b-a)/2)-c['h'])<1e-15
top=sorted(cells,key=lambda c:-c['bound'])[:5]
print('cells',len(cells),'exact tiling of [0,1] (no gaps/overlaps):',ok,'labels distinct',len({c['lab'] for c in cells})==len(cells))
print('max bound',max(c['bound'] for c in cells),'max n0',max(c['n0'] for c in cells),'splits-depth',max(len(c['lab'].rstrip('0123456789')) for c in cells))
print('how',{h:sum(c['how']==h for c in cells) for h in 'FS'})
for c in top: print(c)
