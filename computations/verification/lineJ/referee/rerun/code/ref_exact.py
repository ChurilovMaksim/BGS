"""Referee independent checks (exact): (A) sector law <u|A_{n_k}..A_{n_1}|e0> = sum_a c_a e(a sum n /8) on random words, exact
in Z[zeta8]; (B) |W_C| in arb from exact Z[zeta7] histograms vs assemble doubles, closed form (12/49)|cos(.)|; (C) member-set /
W periodicity over many periods; (D) h odd, h < lam^{m/2}/2."""
import sys, json, math, random
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach, finite
from law import mdata
from flint import arb, acb, ctx
ctx.prec=200
sec=json.load(open('/workspace/bgs-lineJ/logs/sectors_exact.json'))['cases']
# ---- (A)
def zv(e): e%=8; v=[0]*8; v[e]=1; return v           # group-ring Z[C8] (then reduce z^4=-1 at the end)
def red(v): return [v[0]-v[4],v[1]-v[5],v[2]-v[6],v[3]-v[7]]
random.seed(7); badA=0; nA=0
for case in (9,15,21,27):
  for a in (2,-2):
    P=g2params(case,a,8); idx,tg=reach(P,60); NS=len(idx)
    A={n:{i:(o,(-ph)%8) for (o,i,ph,tw) in finite(P,idx,tg,n,None)} for n in range(8)}
    cs={int(k):v['c_times16'] for k,v in sec[f'{case},{a}']['c'].items()}   # 16 c_a in basis 1,z,z2,z3
    for trial in range(400):
        L=random.randint(1,12); word=[random.randrange(8) for _ in range(L)]
        # vector starting at e0 (state index 0), monomial propagation
        s=0; ex=0
        for n in word: o,e=A[n][s]; ex+=e; s=o
        lhs=[0]*8; lhs[ex%8]+=16     # 16 * <u|X|e0>  (u = all ones)
        rhs=[0]*8
        S=sum(word)
        for sa,c in cs.items():
            for i in range(4):          # c * z^{sa*S}
                rhs[(i+sa*S)%8]+=c[i]
        nA+=1
        if red(lhs)!=red(rhs): badA+=1
print('(A) random-word sector law checks:',nA,'failures:',badA)
# ---- (B)
eB=json.load(open('/workspace/bgs-lineJ/logs/exact_B.json'))['residues']
asm=json.load(open('/workspace/bgs-lineJ/logs/assemble.json'))['residues']
z7=[acb(arb(2*k)/7).exp_pi_i() for k in range(7)]
worst=arb(0); outB=[]
for r in asm:
    j=r['residue']; H=eB[str(j)]['W21_hist']
    Wv=sum((z7[k]*H[k] for k in range(7)),acb(0))/arb(7)**4
    Wa=abs(Wv)
    rel=abs(Wa-r['W21'])/Wa; worst=arb.max(worst,rel)
    outB.append((j,Wa.str(12),r['W21']))
print('(B) max rel diff |W21| arb vs assemble double:',worst.str(5),' (margin used 1e-9)')
print('    distinct |W21|:',sorted(set(x[1] for x in outB)))
for v in ('12/49*cos(pi/7)','12/49*cos(2pi/7)','12/49*cos(3pi/7)','6/49'):
    pass
print('    12/49 cos(k pi/7), k=1,2,3:',[(arb(12)/49*(arb.pi()*k/7).cos()).str(12) for k in (1,2,3)],' 6/49=',(arb(6)/49).str(12))
# ---- (C)
def members(m,a):
    D=mdata(m); h=D['h']; yp=D['yp']
    nu0=next(x for x in [((a//2)*pow(4,-1,h))%h+s*h for s in (0,1)] if x%2==1)
    return tuple(sorted((j*yp)%7 for j in range(1,7) if math.gcd((nu0+(2*h//7)*j)%(2*h),2*h)==1))
badC=0; nC=0; badD=0
ref={}
for j in range(3,168,6):
    for a in (2,-2): ref[(j,a)]=members(j+168,a)
for k in range(0,16):
    for j in range(3,168,6):
        m=j+168*k
        if m<9: continue
        for a in (2,-2):
            nC+=1
            if members(m,a)!=ref[(j,a)]: badC+=1
        D=mdata(m); h=D['h']
        if h%2==0 or not (4*h*h < (3+2*arb(2).sqrt())**m): badD+=1
print('(C) member sets m=j+168k, k<=15:',nC,'checks, mismatches',badC,';  (D) h odd & h<lam^{m/2}/2 failures:',badD)
