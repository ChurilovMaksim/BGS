"""J3-F7: generator of logs/blocks16_reps.json (it was produced inline at 06:50 by exactly this code).
Dedupe the 128 (case, block) pairs of logs/blocks16_exact.json by the key (sign a, 2x2 monomial action table for n mod 16):
the builder depends on m only through g2params/reach, which gstates16_block does not use, and C = -4a c0/16 depends only on a."""
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
J=json.load(open('logs/blocks16_exact.json'))['cases']
sig={}
for k,C in J.items():
  a=int(k.split(',')[1])
  for i,B in enumerate(C['blocks']):
    s=(a,json.dumps(B['act'],sort_keys=True)); sig.setdefault(s,[]).append((k,i))
reps=[(v[0][0],v[0][1],len(v)) for v in sig.values()]
json.dump(dict(note='dedupe key (sign a, block action)',reps=reps,members={str(j):v for j,v in enumerate(sig.values())}),open('logs/blocks16_reps.json','w'),indent=1)
print(len(reps),'representatives')
