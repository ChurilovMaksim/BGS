# Referee independent check of Lemma K3 (exact rationals; A bounds from arb)
import math, itertools, json
from fractions import Fraction as Fr
from flint import arb, ctx
ctx.prec=200
Aarb=arb('0.84431').acos()/arb.pi()
Alo=Fr(arb(Aarb.lower()).mid().str(60,radius=False)) if False else None
# exact rational lower/upper bounds: use man_exp
def arb_to_fr(x):
    m,e=x.man_exp(); m=int(m); e=int(e); return Fr(m)*Fr(2)**e
Alo=arb_to_fr(arb(Aarb.lower())); Ahi=arb_to_fr(arb(Aarb.upper()))
assert Alo<=Ahi and Ahi-Alo<Fr(1,10**50)
print('A in [%.15f, %.15f]'%(float(Alo),float(Ahi)))
def units_gap(bp,g,r):
    # max cyclic gap of {v mod bp: gcd(v,bp)=1, v=r mod g}
    V=[v for v in range(r,bp,g) if math.gcd(v,bp)==1]
    if not V: return None
    G=max([V[i+1]-V[i] for i in range(len(V)-1)]+[V[0]+bp-V[-1]])
    return G
fails=set(); minmargin=(Fr(1),None)
for bp in range(447,6001):
    g=math.gcd(56,bp)
    for r in range(g):
        if math.gcd(r,g)!=1: continue
        G=units_gap(bp,g,r)
        if G is None or not (Fr(G,bp)<Alo):
            if G is None or Fr(G,bp)>=Alo: fails.add(bp)
            continue
        mg=Alo-Fr(G,bp)
        if mg<minmargin[0]: minmargin=(mg,(bp,r,G))
print('fails',sorted(fails),' min passing margin A-G/b\' =',float(minmargin[0]),minmargin[1])
# sieve sets exact
SMALL=[3,5,11,13,17,19]
assert Fr(2,22) < Alo-Fr(1,23)
cand=[]
for k in range(0,len(SMALL)+1):
    for S in itertools.combinations(SMALL,k):
        R=math.prod(S); F=Fr(2**k*R, math.prod(l-1 for l in S))
        if F+1>=Alo*R: cand.append((S,F))
bmax=max(56*(F+1)/Alo for S,F in cand)
print('sieve sets',[(S,str(F)) for S,F in cand],' bmax',float(bmax))
# also check: all b' failing in a larger exact range? extend to 12000 quickly for 'fails' only (sanity)
# fraction test with enclosure: recompute enclosure independently below if file present
E=json.load(open('/workspace/bgs-lineJ/J3/logs/rat_excl.json'))
L=Fr(math.nextafter(E['interval'][0],-math.inf)); H=Fr(math.nextafter(E['interval'][1],math.inf))
live=[]
for bp in sorted(fails):
    for b in ([bp] if bp%3 else [])+[3*bp]:
        for a in range(math.floor(L*b)-1, math.ceil(H*b)+2):
            if L<=Fr(a,b)<=H: live.append((bp,b,a))
print('fractions with denominators b for failing b\' in enclosure:',live)
# extra: smallest denominator in [L,H] by brute force up to 1339
best=None
for b in range(1,1340):
    a=math.ceil(L*b)
    if Fr(a,b)<=H: best=(a,b); break
print('first denom with fraction in enclosure (brute):',best)
