"""Referee [N]: independent re-test of the N9/N10 'gas' (multi-bump) picture at new p with exact twists.
Points x = z + e*gamma/(8q), gamma = x_{k+1} + y_k sqrt2 (Binet), membership on the isotropic line checked exactly.
Classes at z=1/4: e = 2*alpha, alpha = 1 (family), 1 + s*beta*lam^g (two-bump), 1 + s1 lam^g1 + s2 lam^g2 (three-bump);
z=0: e = 2sqrt2 (c0), e = 4 (c4).  r = Zhat/Z via N6 twb (L=8, K=16), sg=+1 convention.  usage: p"""
import os; os.environ.setdefault('OMP_NUM_THREADS','4'); os.environ.setdefault('OPENBLAS_NUM_THREADS','4')
import sys, json, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, nu_rho, TW
p=int(sys.argv[1]); m=3*p; k=(p-1)//2
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
q=xy(p)[0]; g0=(xy(k+1)[0],xy(k)[1])
def mul(a,b): return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def lpow(g):
    r=(1,0)
    for _ in range(g): r=mul(r,(3,2))
    return r
def add(*xs): return (sum(x[0] for x in xs),sum(x[1] for x in xs))
def sc(s,a): return (s*a[0],s*a[1])
def in_Ovee_scaled(v,s):
    a=Fr(4*v[1],s); b=Fr(4*v[0],2*s); return a.denominator==1 and b.denominator==1
def point(z8,e):
    ug=mul(e,g0); u=(q*z8[0]+ug[0],q*z8[1]+ug[1])
    if not in_Ovee_scaled(u,8): return None
    v=(int(Fr(4*u[1],8)),int(Fr(4*u[0],16)))
    if (v[0]**2-2*v[1]**2)%q: return None
    seq=[]; a=u
    for i in range(m):
        seq.append(((2*a[0])%(8*q))/(8*q)); a=mul((3,2),a); a=(a[0]%(32*q),a[1]%(32*q))
    return seq
Z4=(2,0); Z0=(0,0)
classes=[('fam',Z4,(2,0))]
for beta,bn in [((0,1),'r2'),((2,0),'2')]:
    for s in (1,-1):
        for g in (5,6,7,8,10,12,14):
            if g>k-3: continue
            classes.append((f'two_{bn}_s{s}_g{g}',Z4,sc(2,add((1,0),sc(s,mul(beta,lpow(g)))))))
for (g1,g2) in [(4,9),(5,12),(6,15),(7,18),(8,20)]:
    if g2>k-2: continue
    for s1,s2 in [(1,1),(-1,1)]:
        classes.append((f'tri_{g1}_{g2}_{s1}{s2}',Z4,sc(2,add((1,0),sc(s1,lpow(g1)),sc(s2,lpow(g2))))))
classes+= [('c0',Z0,(0,2)),('c4',Z0,(4,0))]
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Zr=Zbatch(tw,[[0.0]*m])[0]
names=[];T=[]
for name,z,e in classes:
    s=point(z,e)
    if s is None: print('not on line:',name,flush=True); continue
    names.append(name); T.append(s)
Z=[]
for i in range(0,len(T),32): Z+=list(Zbatch(tw,T[i:i+32]))
r={n:complex(z/Zr) for n,z in zip(names,Z)}
# convention: make family = w* with Im>0 (sg=+1) by conjugating if needed
conj = r['fam'].imag<0
if conj: r={n:v.conjugate() for n,v in r.items()}
ws=r['fam']
out=dict(p=p,q_digits=len(str(q)),w_star=[ws.real,ws.imag],conjugated=conj,rows=[])
for n,v in r.items():
    row=dict(name=n,r=[v.real,v.imag],absr=abs(v))
    if n.startswith('two'): row['phi']=[(v/ws).real,(v/ws).imag]
    if n.startswith('tri'): row['ratio_to_wstar3']=[(v/ws**3).real,(v/ws**3).imag]
    out['rows'].append(row); print(json.dumps(row),flush=True)
json.dump(out,open(f'logs/ref_gas_p{p}.json','w'),indent=1)
