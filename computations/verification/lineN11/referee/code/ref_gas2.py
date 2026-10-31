"""Referee N11 [N]: even/odd numbers of odd bumps on both backgrounds. Derived from lineN10 ref_gas.py.
Referee [N]: independent re-test of the N9/N10 'gas' (multi-bump) picture at new p with exact twists.
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
def epow(n):
    r=(1,0)
    for _ in range(n): r=mul(r,(1,1))
    return r
classes=[('fam',Z4,(2,0)),('c0',Z0,(0,2)),('c4',Z0,(4,0))]
# two odd bumps (any eps-shift n), both backgrounds; three and four odd bumps
for n in (8,10,11,12,14,16,20,24):
    for s in (1,-1):
        e=sc(2,add((1,0),sc(s,epow(n))))
        for zn,z in (('z0',Z0),('z4',Z4)):
            classes.append((f'odd2_{zn}_n{n}_s{s}',z,e))
for ns in [(10,22),(12,26),(14,30)]:
    for s1 in (1,-1):
        e=sc(2,add((1,0),sc(s1,epow(ns[0])),epow(ns[1])))
        for zn,z in (('z0',Z0),('z4',Z4)): classes.append((f'odd3_{zn}_{ns[0]}_{ns[1]}_s{s1}',z,e))
for ns in [(10,22,34),(12,26,40)]:
    e=sc(2,add((1,0),epow(ns[0]),sc(-1,epow(ns[1])),epow(ns[2])))
    for zn,z in (('z0',Z0),('z4',Z4)): classes.append((f'odd4_{zn}_{ns[0]}_{ns[1]}_{ns[2]}',z,e))
# mixed: odd bump + sqrt2 bump on background 0 (expect w* c0)
for n in (12,16,20):
    for s in (1,-1):
        e=add((2,0),sc(s,mul((0,2),epow(n))))
        for zn,z in (('z0',Z0),('z4',Z4)): classes.append((f'oddr2_{zn}_n{n}_s{s}',z,e))
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
    nb={'odd2':2,'odd3':3,'odd4':4}.get(n.split('_')[0])
    if nb: row['ratio_to_wstar_n']=[(v/ws**nb).real,(v/ws**nb).imag]
    if n.startswith('oddr2'): row['ratio_to_wstar_c0']=[(v/(ws*r['c0'])).real,(v/(ws*r['c0'])).imag]
    out["rows"].append(row); print(json.dumps(row),flush=True)
json.dump(out,open(f'logs/ref_gas2_p{p}.json','w'),indent=1)
