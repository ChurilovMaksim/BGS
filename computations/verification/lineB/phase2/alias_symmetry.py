"""Exact classification of affine symmetries of the aliased symbol on n-torsion:
f(a*theta + b) = f(theta) for all theta in (1/n)Z/Z, a in (Z/n)^x, b in {0,1/4,1/2,3/4} with n*b integer (b must be a fixed point of S).
Exact arithmetic in Q(i) (coefficients x800 are Gaussian integers). Such a symmetry forces S(a xi + b) = S(xi) for every periodic
orbit xi of order | n: a 'symmetry-induced' coincidence."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','common'))
from audit46_core import cEx
from math import gcd
c={k:(int(cEx(k,0)[0]*800),int(cEx(k,0)[1]*800)) for k in range(-9,10) if cEx(k,0)!=(0,0)}
print('c_k*800 (Gaussian integers):',c)
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
I4=[(1,0),(0,1),(-1,0),(0,-1)]   # i^t
res=[]
for n in range(1,401):
    C={}
    for k,v in c.items():
        r=k%n; a=C.get(r,(0,0)); C[r]=(a[0]+v[0],a[1]+v[1])
    C={r:v for r,v in C.items() if v!=(0,0)}
    syms=[]
    for a in range(n if n>1 else 1):
        if n>1 and gcd(a,n)!=1: continue
        for t in range(4):              # b = t/4, need n*b integer i.e. 4 | n*t
            if (n*t)%4: continue
            # f(a th + b) = sum_r C_r e(r b) e(r a th): coefficient at s=r*a is C_r * i^{r t}
            D={}
            for r,v in C.items():
                s=(r*a)%n if n>1 else 0; w=mul(v,I4[(r*t)%4]); x=D.get(s,(0,0)); D[s]=(x[0]+w[0],x[1]+w[1])
            D={s:v for s,v in D.items() if v!=(0,0)}
            if D==C: syms.append((a if n>1 else 1,f'{t}/4'))
    nontriv=[s for s in syms if s!=(1,'0/4')]
    if nontriv: res.append((n,len(syms),nontriv[:6]))
for n,cnt,ex in res: print(f'n={n}: |Sym|={cnt} nontrivial e.g. {ex}')
print('n with nontrivial symmetry (n<=400):',[r[0] for r in res])
