#!/usr/bin/env python3
"""Exact rational controls of the NEW algebra, not a proof of analytic limits.
Tests repeated endpoints at m=1,2, full Wick contractions, covariance
variation, literal-winding endpoint labels, and raw Weyl parity counting.
"""
from functools import lru_cache
import hashlib, json
from pathlib import Path
import sympy as s
OUT=Path(__file__).resolve().parent

def pairings(indices):
    if not indices:
        yield ()
        return
    a=indices[0]
    for j in range(1,len(indices)):
        for rest in pairings(indices[1:j]+indices[j+1:]):
            yield ((a,indices[j]),)+rest

def wick(indices,G):
    return sum((s.prod(G[a,b] for a,b in p) for p in pairings(tuple(indices))),s.S.Zero)

def wick_prime_pairings(indices,G,DG):
    ans=s.S.Zero
    for p in pairings(tuple(indices)):
        for k,(a,b) in enumerate(p):
            ans += DG[a,b]*s.prod(G[c,d] for j,(c,d) in enumerate(p) if j!=k)
    return ans

def wick_prime_price(indices,G,DG):
    # Price's 1/2 trace(DG E Hess) identity, after collecting ordered derivatives.
    ans=s.S.Zero
    for i in range(len(indices)):
        for j in range(i+1,len(indices)):
            rem=tuple(v for k,v in enumerate(indices) if k not in (i,j))
            ans+=DG[indices[i],indices[j]]*wick(rem,G)
    return ans

cases=[]; winding=[]
S=s.Matrix([[3,4],[2,3]])
for m in range(1,13):
    P=s.zeros(m)
    for j in range(m): P[j,(j+1)%m]+=1
    K=(6*s.eye(m)-P-P.T)/4
    G=K.inv()
    assert all(sum(G[j,k] for k in range(m))==1 for j in range(m))
    xp=G[:,0]
    delta=s.Matrix([xp[0],(xp[1%m]-3*xp[0])/4])
    assert delta==(S**m-s.eye(2)).inv()*s.Matrix([0,1])
    assert delta[1]==-s.Rational(1,2)
    winding.append({'m':m,'delta_q':str(delta[0]),'delta_p':str(delta[1])})
    # Uniform sparse local K' induced by a localized derivative x'.
    KP=s.zeros(m)
    for j in range(m):
        inds=[j,(j+1)%m]
        local=s.Matrix([[s.Rational(2*j+1,31),s.Rational(1,37)],
                        [s.Rational(1,37),s.Rational(j+3,41)]])/(j+1)
        for a in range(2):
            for b in range(2):
                KP[inds[a],inds[b]]+=local[a,b]*(xp[j]+xp[(j+1)%m])
    GP=-G*KP*G
    assert G*KP+GP*K==s.zeros(m)
    samples=[]
    # All local Q degrees, all local W odd-odd endpoint choices.
    for j in range(m):
        ends=(j,(j+1)%m)
        samples += [(),(ends[0],)*2,(ends[1],)*4,(ends[0],ends[1])]
        for k in range(m):
            f=(k,(k+1)%m)
            samples += [(ends[0],f[1]),(ends[0],)*3+(f[1],),
                        (ends[0],)+(f[1],)*3,
                        (ends[0],ends[1],ends[1],f[0],f[0],f[1])]
    for indices in samples:
        assert wick_prime_pairings(indices,G,GP)==wick_prime_price(indices,G,GP)
    cases.append({'m':m,'wick_variation_checks':len(samples),
                  'Kprime_entry_l1':str(sum(abs(x) for x in KP)),
                  'Gprime_entry_l1':str(sum(abs(x) for x in GP))})

# General Weyl parity: amplitude derivative order a; midpoint-factor count v;
# phase increments of h-grade k have symbol moment order k+1 and one i.
# coefficient i-power = factors - total moments = -total h-grade.
parity=0
for a in range(9):
    for v in range(9-a):
        for p1 in range(9-a-v):
            for p2 in range((8-a-v-p1)//2+1):
                for p3 in range((8-a-v-p1-2*p2)//3+1):
                    grade=a+v+p1+2*p2+3*p3
                    factors=v+p1+p2+p3
                    moments=a+2*v+2*p1+3*p2+4*p3
                    assert factors-moments == -grade
                    parity+=1

report={'arithmetic':'exact SymPy rational/integer',
        'scope':'m=1..12; repeated endpoint aliases retained; Weyl grades <=8 with phase grades <=3',
        'nonclaims':'Does not test the actual analytic amplitudes numerically or prove an asymptotic theorem, bounded classical mass, equidistribution, or the full signed sum.',
        'weyl_parity_checks':parity,'wick_variation_cases':cases,'unit_winding_labels':winding,
        'total_wick_checks':sum(c['wick_variation_checks'] for c in cases)}
(OUT/'quantum_first_loop_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'weyl_parity_checks':parity,'total_wick_checks':report['total_wick_checks'],'m_range':[1,12]}))
