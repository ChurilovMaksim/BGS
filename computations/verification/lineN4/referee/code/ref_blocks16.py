"""Referee: J3 blocks16_exact.json properties used by N4 (orthogonal equal-norm f1,f2; monomial actions; permutation patterns)."""
import json, collections
d=json.load(open('/workspace/bgs-lineJ/J3/logs/blocks16_exact.json'))
pats=collections.Counter(); bad=0; nb=0; acts=set()
for case,v in d['cases'].items():
    for b in v['blocks']:
        nb+=1
        s1,s2=set(b['f1']),set(b['f2'])
        if s1&s2 or len(s1)!=len(s2): bad+=1
        pat=tuple(tuple(b['act'][str(r)]['perm']) for r in range(16)); pats[pat]+=1
        acts.add(tuple((tuple(b['act'][str(r)]['perm']),tuple(b['act'][str(r)]['exps'])) for r in range(16)))
        for r in range(16):
            P=b['act'][str(r)]['perm']; assert sorted(P)==[0,1]
print('cases',len(d['cases']),'blocks',nb,'f1/f2 disjoint & equal size violations',bad)
for p,c in pats.items(): print('pattern parity', 'id on even r' if p[0]==(0,1) else 'swap on even r', 'count',c, 'is swap^(r+PAR):', all(p[r]==((0,1) if (r+(0 if p[0]==(0,1) else 1))%2==0 else (1,0)) for r in range(16)))
print('distinct actions',len(acts))
import cmath
z=lambda e: cmath.exp(2j*cmath.pi*e/16)
worst=0; normdiff=0
for case,v in d['cases'].items():
    for b in v['blocks']:
        f1={int(k):z(e) for k,e in b['f1'].items()}; f2={int(k):z(e) for k,e in b['f2'].items()}
        ip=sum(f1[k].conjugate()*f2[k] for k in f1 if k in f2)
        worst=max(worst,abs(ip)); normdiff=max(normdiff,abs(len(f1)-len(f2)))
print('max |<f1,f2>| =',worst,' max | |f1|^2-|f2|^2 | =',normdiff)
ex=[(len(b['f1']),len(b['f2']),len(set(b['f1'])&set(b['f2']))) for v in d['cases'].values() for b in v['blocks']]
import collections; print(collections.Counter(ex))
