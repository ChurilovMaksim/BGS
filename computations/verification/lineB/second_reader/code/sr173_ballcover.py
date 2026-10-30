"""Second reader: exact check that t9_cert.coef_bounds' eta-balls (24 per interval) cover [1, 81.57406988332305].
t9 builds eta = arb(float(mid), float(half)*(1+1e-12)+1e-30); arb rounds the radius UP, so using the float radius is a
sufficient (conservative) test.  Exact rational arithmetic."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json
from fractions import Fraction as Fr
iv=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'b1_intervals.json')))
M=24; balls=[]; worst=None; indiv_fail=0
for i,(e0,e1) in enumerate(iv):
    edges=[Fr(e0)+(Fr(e1)-Fr(e0))*k/M for k in range(M+1)]
    for k in range(M):
        lo,hi=edges[k],edges[k+1]
        mid=Fr(float((lo+hi)/2)); rad=Fr(float((hi-lo)/2)*(1+1e-12)+1e-30)
        a,b=mid-rad,mid+rad; balls.append((a,b,i,k))
        slack=min(lo-a,b-hi)
        if slack<0: indiv_fail+=1
        if worst is None or slack<worst[0]: worst=(slack,i,k)
balls.sort(key=lambda t:t[0])
cur=Fr(1); gaps=[]
assert balls[0][0]<=1
for a,b,i,k in balls:
    if a>cur: gaps.append((float(cur),float(a),i,k))
    cur=max(cur,b)
print(json.dumps(dict(n_balls=len(balls),subintervals_not_individually_covered=indiv_fail,
      worst_individual_slack=float(worst[0]),worst_at=(worst[1],worst[2]),
      union_gaps=gaps,union_upper_end=float(cur),covers_to_81_574=cur>=Fr(81574,1000))))
# per-interval: does the union of the interval's OWN 24 balls cover [e0,e1]?
own_fail=[]
for i,(e0,e1) in enumerate(iv):
    bb=sorted([(a,b) for a,b,j,k in balls if j==i]); cur=Fr(e0)
    if bb[0][0]>cur: own_fail.append((i,'left',float(bb[0][0]-cur)))
    for a,b in bb:
        if a>cur: own_fail.append((i,'inner',float(a-cur)))
        cur=max(cur,b)
    if cur<Fr(e1): own_fail.append((i,'right',float(Fr(e1)-cur)))
print(json.dumps(dict(intervals_whose_own_balls_miss_a_sliver=own_fail)))
