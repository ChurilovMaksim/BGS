"""N8b: factorizations of h_p and K'=(K_p)/7 (K_p = h_{3p}/h_p) for small p (sympy, [N] factoring, exact)."""
import json, sys
from sympy import factorint, primerange
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
out=[]
for p in primerange(5,int(sys.argv[1])):
    h=xy(p)[0]; H=xy(3*p)[0]; K=H//h; assert H%h==0
    fh=factorint(h); fk=factorint(K)
    rec=dict(p=p,h=str(h),fh={str(a):b for a,b in fh.items()},fK={str(a):b for a,b in fk.items()})
    print(p, fh, fk, flush=True); out.append(rec)
json.dump(out,open('logs/a_fact.json','w'),indent=0)
