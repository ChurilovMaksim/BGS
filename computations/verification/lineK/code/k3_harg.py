"""K3: removal of H_arg.  Claim: for every b' >= 447 and every unit class r mod g' = gcd(56,b'), the set
V(b',r) = {v mod b' : gcd(v,b')=1, v = r mod g'} has maximal cyclic gap < A*b', A = arccos(0.84431)/pi (arc length in turns).
(a) exact check for 447 <= b' <= BEXACT; (b) for b' > BEXACT the sieve bound gap <= g'*X_t, X_t = floor(2^k n'/phi(n')) + 1
(inclusion-exclusion: any X consecutive t contain >= X phi(n')/n' - 2^k admissible t), n' = part of b' coprime to g',
combined with an exhaustive enumeration of the prime sets for which g'X_t >= A b' is possible (shows all such b' <= BEXACT)."""
import math, json, itertools
from flint import arb, ctx
ctx.prec=100
A_arb=arb('0.84431').acos()/arb.pi(); A=float(A_arb.lower())     # rounded down: safe
BEXACT=6000
def rad_primes(n):
    ps=[]; d=2
    while d*d<=n:
        if n%d==0:
            ps.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: ps.append(n)
    return ps
worst=(0,None); fails=[]
for bp in range(447,BEXACT+1):
    g=math.gcd(56,bp)
    units=[v for v in range(bp) if math.gcd(v,bp)==1]
    for r in range(g):
        if math.gcd(r,g)!=1: continue
        V=[v for v in units if v%g==r]
        if not V: fails.append((bp,r,'empty')); continue
        gaps=[V[i+1]-V[i] for i in range(len(V)-1)]+[V[0]+bp-V[-1]]
        gr=max(gaps)/bp
        if gr>worst[0]: worst=(gr,(bp,r))
        if not gr<A: fails.append((bp,r,gr))
print('A (lower) =',A,' exact range 447..',BEXACT,' worst gap ratio',worst,' fails',fails[:5],flush=True)
# (b) enumeration: primes l >= 3, l != 7 (primes of g' are 2,7). F(S) = prod 2l/(l-1), R = prod l.
# If g'X_t >= A b' with b' >= g'R then F+1 >= A R, i.e. prod 2/(l-1) >= A - 1/R. Enumerate all such S.
# Any set containing a prime l >= 23 has R >= 23 and prod 2/(l-1) <= 2/22 < A - 1/23: impossible. So S is a subset of SMALL.
SMALL=[3,5,11,13,17,19]
assert 2/22 < A-1/23
cand=[]
for k in range(1,len(SMALL)+1):
    for S in itertools.combinations(SMALL,k):
        R=math.prod(S); pf=math.prod(2/(l-1) for l in S); F=pf*R
        if F+1>=A*R: cand.append((S,F,R))
bmax=max([56*(F+1)/A for (S,F,R) in cand]+[56*2/A])
print('prime sets allowing a sieve failure:',[(S,round(F,3)) for S,F,R in cand],' => any failure has b\' <=',bmax,flush=True)
# (c) failing b' (all <= BEXACT): the rational case needs a/b inside the certified enclosure of arg(xi)/2pi with b in {b' (3 not| b'), 3b'};
# exact Fraction test against the outward-rounded enclosure from Line J3 rat_excl (v2).
from fractions import Fraction as Fr
E=json.load(open('../bgs-lineJ/J3/logs/rat_excl.json')); L=Fr(E['interval'][0]); H=Fr(E['interval'][1])
L=Fr(math.nextafter(E['interval'][0],-math.inf)); H=Fr(math.nextafter(E['interval'][1],math.inf))
failb=sorted(set(f[0] for f in fails))
live=[]
for bp in failb:
    for b in ([bp] if bp%3 else [])+[3*bp]:
        a0=math.ceil(L*b); 
        if Fr(a0,b)<=H and math.gcd(a0,b)==1: live.append((bp,b,a0))
        elif Fr(a0,b)<=H: live.append((bp,b,a0,'nonreduced'))
print('failing b\' (exact gap check):',failb)
print('of these, compatible with the certified enclosure of arg xi/2pi:',live)
ok=(bmax<=BEXACT) and not [x for x in live if len(x)==3]
print('K3 CLAIM', 'PROVED (exact + sieve)' if ok else 'NOT PROVED')
json.dump(dict(A_lower=A,BEXACT=BEXACT,worst=worst,fails=fails[:20],sieve_sets=[[list(S),F,R] for S,F,R in cand],bmax=bmax,ok=ok,failing_bprime=failb,live=live),open('logs/k3_harg.json','w'),indent=1)
