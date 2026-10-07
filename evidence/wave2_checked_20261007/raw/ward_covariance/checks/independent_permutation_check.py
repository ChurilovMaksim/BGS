"""Exhaustive formal graph checks, independent of the author verifier."""
from itertools import permutations
import json

cov=[]; mixed=[]
for m in range(3,9):
    edge={(i,(i+1)%m) for i in range(m)}; tested=0; tied=0
    for sig in permutations(range(m)):
        edge2={(sig[i],sig[(i+1)%m]) for i in range(m)}
        if edge==edge2: continue
        available=edge-edge2
        if sig[0]==0:
            available={e for e in available if 0 not in e}; tied+=1
        assert available
        a,b=min(available)
        # Exactly one original edge and, optionally, one reversed second edge
        # can involve both selected formal variables.
        assert [e for e in edge if set(e)=={a,b}]==[(a,b)]
        both=[e for e in edge2 if set(e)=={a,b}]
        assert both in ([],[(b,a)])
        tested+=1
    cov.append(dict(m=m,nonrotations=tested,coincident_marks=tied))
    if m<=7:
        tested=0; boundary=0
        for u in range(1,m):
            for sig in permutations(range(m)):
                segments=[sig[:u],sig[u:]]
                es={(s[i],s[(i+1)%len(s)]) for s in segments for i in range(len(s))}
                available=edge-es; assert available
                a,b=min(available)
                both=[e for e in es if set(e)=={a,b}]
                assert both in ([],[(b,a)])
                tested+=1
                if u in (1,m-1): boundary+=1
        mixed.append(dict(m=m,all_splits_permutations=tested,loop_boundary_cases=boundary))
assert sum(x['nonrotations'] for x in cov)==46197
print(json.dumps(dict(status='pass',covariance_controls=cov,mixed_cycle_controls=mixed),indent=2))
