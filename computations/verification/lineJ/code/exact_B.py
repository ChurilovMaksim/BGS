"""[P]-check (exact integer arithmetic) of the ingredients of B_C = c0F (c+_C - conj c-_C) W+_C:
 (1) sector constants in Z[zeta8] (from sectors_exact.json, c_times16 in basis 1,z,z^2,z^3): for every case
     c^{(case,+2)}_a = +conj c^{(case,-2)}_{a+4} for a in {2,6};  c^{(case,+2)}_a = -conj c^{(case,-2)}_{a+4} for a in {0,4}.
 (2) W_C(m,rho) * 7^4 as exact elements of Z[zeta7] (exponent histograms): W(m,-2) = conj W(m,+2), W_{2:1} != 0, W_{0:1} != 0,
     for every residue m mod 168 (m = 3 mod 6), using exact member sets; periodicity m -> m+168 checked on 3 periods.
Output logs/exact_B.json"""
import json, sys, hashlib, math
sys.path.insert(0,'/workspace/bgs-lineJ/code'); sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from law import mdata
sec=json.load(open('logs/sectors_exact.json'))['cases']
def conj8(v): return [v[0],-v[3],-v[2],-v[1]]
ok1={}
for case in (9,15,21,27):
    for a in (0,2,4,6):
        cp=sec[f'{case},2']['c'][str(a)]['c_times16']; cm=sec[f'{case},-2']['c'][str((a+4)%8)]['c_times16']
        s=+1 if a in (2,6) else -1
        ok1[f'{case},{a}']=(cp==[s*x for x in conj8(cm)])
assert all(ok1.values()), ok1
d=7
Nm=lambda x,y:(x*x-2*y*y)%d
def orbit(bx,by):
    o=set(); x,y=bx,by
    for i in range(3):
        o.add((x%7,y%7)); o.add((-x%7,-y%7)); x,y=(3*x+4*y)%7,(2*x+3*y)%7
    return o
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']; orb={c:orbit(*map(int,c.split(':'))) for c in cls}
def Ghist(t,bx,by):   # G_t(beta) = sum_gamma e(-(t Nm gamma + Tr(beta gamma))/d), Tr = 2(bx gx + 2 by gy)
    H=[0]*d
    for gx in range(d):
        for gy in range(d): H[(-(t*Nm(gx,gy)+2*(bx*gx+2*by*gy)))%d]+=1
    return H
def mul(A,B):
    C=[0]*d
    for i in range(d):
        for j in range(d): C[(i+j)%d]+=A[i]*B[j]
    return C
def conj7(A): return [A[(-k)%d] for k in range(d)]
def iszero(A): return len(set(A))==1     # sum c_k z^k = 0 in Z[zeta7] iff all c_k equal
def members(m,a):
    D=mdata(m); h=D['h']; yp=D['yp']
    nu0=next(x for x in [((a//2)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    return sorted((j*yp)%d for j in range(1,d) if math.gcd((nu0+(2*h//d)*j)%(2*h),2*h)==1)
def Wex(m,a):
    ts=members(m,a); out={}
    for c in cls:
        T=[0]*d
        for t in ts:
            g0=conj7(Ghist(t,0,0))
            for (bx,by) in orb[c]: T=[x+y for x,y in zip(T,mul(g0,Ghist(t,bx,by)))]
        out[c]=T
    return ts,out
res={}
for j in range(3,168,6):
    tsp,Wp=Wex(j+168,2); tsm,Wm=Wex(j+168,-2)
    for k in (2,3):
        tq,Wq=Wex(j+168*k,2); assert tq==tsp and Wq==Wp
    norm=lambda A:[x-min(A) for x in A]
    for c in cls: assert norm(Wm[c])==norm(conj7(Wp[c])), (j,c)
    nz={c:not iszero(Wp[c]) for c in cls}
    assert nz['2:1'] and nz['0:1']
    res[j]=dict(members_plus=tsp,members_minus=tsm,nonzero=nz,W21_hist=Wp['2:1'])
out=dict(code_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),sector_relations=ok1,residues=res,result='ALL EXACT CHECKS PASSED')
json.dump(out,open('logs/exact_B.json','w'),indent=1); print('ALL EXACT CHECKS PASSED', {j:(r['members_plus'],r['nonzero']['1:3']) for j,r in res.items()})
