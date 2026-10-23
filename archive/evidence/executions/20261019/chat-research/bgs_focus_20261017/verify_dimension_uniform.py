#!/usr/bin/env python3
"""Independent finite checks of rank/moment and marked first-exit mechanisms."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial, isqrt
import json
import platform
import sys

from exact_unitaries import Q


def falling(n,k):
    return factorial(n)//factorial(n-k)


def matadd(a,b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]


def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def power_trace(a,p):
    n=len(a)
    v=[[int(i==j) for j in range(n)] for i in range(n)]
    for _ in range(p):
        v=mul(v,a)
    return sum(v[i][i] for i in range(n))


def martingale_checks():
    def increment(prefix,sign,step):
        active=4-step
        a=[[0]*4 for _ in range(4)]
        adapt=sum((k+1)*v for k,v in enumerate(prefix))
        for i in range(active):
            for j in range(i,active):
                val=sign*(1+((i+2*j+adapt)%3))
                a[i][j]=a[j][i]=val
        return a
    bounds=[]
    for step in range(4):
        mx=max(sum(x*x for row in increment(prefix,1,step) for x in row)
               for prefix in product([-1,1],repeat=step))
        bounds.append(isqrt(mx)+int(isqrt(mx)**2<mx))
    moment_rows=[]
    for p in [4,6,8,10,12]:
        terminal=0
        trajectories=[]
        for signs in product([-1,1],repeat=4):
            a=[[0]*4 for _ in range(4)]
            maxima=0
            for step,sign in enumerate(signs):
                plus=increment(signs[:step],1,step)
                minus=increment(signs[:step],-1,step)
                assert matadd(plus,minus)==[[0]*4 for _ in range(4)]
                assert all(plus[i][j]==0 for i in range(4) for j in range(4)
                           if i>=4-step or j>=4-step)
                a=matadd(a,increment(signs[:step],sign,step))
                val=power_trace(a,p)
                assert val>=0
                maxima=max(maxima,val)
            terminal+=val
            trajectories.append(maxima)
        mean=F(terminal,16)
        bound=p**p*sum(x*x for x in bounds)**(p//2)
        assert mean<=bound
        max_cases=0
        for eta in range(1,25):
            prob=F(sum(v>=eta**p for v in trajectories),16)
            assert prob*eta**p<=mean
            max_cases+=1
        moment_rows.append({"p":p,"E_trace_exact":str(mean),
                            "moment_bound_exact":str(bound),
                            "maximal_threshold_checks":max_cases})
    coeff_checks=0
    for p in range(4,66,2):
        assert sum(F(comb(p,j),p**j) for j in range(2,p+1))<1
        for r in [F(0),F(1,10),F(1,2),F(1),F(2),F(10)]:
            assert all(r**j<=r*r+r**p for j in range(2,p+1))
            assert (1+r*r)**(p//2)-1>=r*r+r**p
            coeff_checks+=1
    return {"adapted_noncommuting_paths":16,"support_sizes":[4,3,2,1],
            "integer_Schatten_majorants":bounds,"moments":moment_rows,
            "binomial_and_induction_checks":coeff_checks,
            "scope":"Exact finite martingales; asymptotic matrix estimate is proved analytically."}


def bad_sets(prefix,survivors):
    if not prefix:
        return (),()
    code=sum((i+1)*(a+1) for i,a in enumerate(prefix))
    rows=tuple(a for a in survivors if code%7 in [0,1,3]
               and (a+code)%3==0)
    pairs=tuple((a,b) for a in survivors for b in survivors if a!=b
                and code%11 in [1,4,7] and (a+2*b+code)%5==0)
    return rows,pairs


def marked_first_exit_checks():
    cases,prefixes,compatible,firsts=0,0,0,0
    for n in range(3,8):
        for u in range(2,n+1):
            k=n-u
            left_rows=left_pairs=right_rows=right_pairs=F(0)
            for prefix in permutations(range(n),k):
                survivors=tuple(a for a in range(n) if a not in prefix)
                for d in [1,2]:
                    mark_weight=F(1,falling(n,d)*falling(n-d,k))
                    assert falling(u,d)*mark_weight==F(1,falling(n,k))
                    compatible+=falling(u,d)
                rows,pairs=bad_sets(prefix,survivors)
                earlier=False
                for l in range(k):
                    pp=prefix[:l]
                    ss=tuple(a for a in range(n) if a not in pp)
                    rr,qq=bad_sets(pp,ss)
                    if rr or qq:
                        earlier=True
                        break
                if not earlier and (rows or pairs):
                    firsts+=1
                    full_weight=F(1,falling(n,k))
                    left_rows+=full_weight*len(rows)
                    left_pairs+=full_weight*len(pairs)
                    right_rows+=u*F(len(rows),n*falling(n-1,k))
                    right_pairs+=falling(u,2)*F(len(pairs),falling(n,2)*falling(n-2,k))
                prefixes+=1
            assert left_rows==right_rows and left_pairs==right_pairs
            cases+=1
    assert firsts>0
    return {"N_range":[3,7],"terminal_depths":"2..N","depth_cases":cases,
            "deletion_prefixes":prefixes,"compatible_ordered_marks":compatible,
            "first_crossing_prefixes":firsts,
            "exact_identity":"E[number of bad retained marks at first exit] = (u)_d times protected-mark first-exit probability"}


def feedback_normalization_checks():
    n=16
    S=[[Q(F(1 if (i&j).bit_count()%2==0 else -1,4)) for j in range(n)]
       for i in range(n)]
    for i in range(n):
        for j in range(n):
            assert sum(S[i][k]*S[j][k].conj() for k in range(n))==Q(F(i==j))
    phases=[Q(F(1)),Q(F(-1)),Q(F(0),F(1)),Q(F(3,5),F(4,5))]
    data=[]
    oldR=F(1,n)
    oldK=F(1,n)
    for e in range(n):
        for w in phases:
            keep=[a for a in range(n) if a!=e]
            q=w/(1-S[e][e]*w)
            T=[[S[a][b]+q*S[a][e]*S[e][b] for b in keep] for a in keep]
            P=[[z.abs2() for z in row] for row in T]
            assert all(sum(row)==1 for row in P)
            assert all(sum(col)==1 for col in zip(*P))
            dr=F(0) if e==0 else sum(p*p for p in P[keep.index(0)])-oldR
            dk={}
            for j in [0,1]:
                if e in [0,j]:
                    dk[j]=F(0)
                else:
                    a,b=keep.index(0),keep.index(j)
                    dk[j]=sum(P[a][k]*P[k][b] for k in range(n-1))-oldK
            data.append((e,dr,dk))
    results=[]
    fullR=sum(dr for _,dr,_ in data)/len(data)
    protR=sum(dr for e,dr,_ in data if e!=0)/(len(phases)*(n-1))
    assert protR==F(n,n-1)*fullR
    ey_protected=-oldR+(n-1)*protR
    assert ey_protected==-oldR+n*fullR
    for j in [0,1]:
        endpoints={0,j}
        d=len(endpoints)
        for power in [1,2]:
            full=sum(dk[j]**power for _,_,dk in data)/len(data)
            prot=sum(dk[j]**power for e,_,dk in data if e not in endpoints)/(len(phases)*(n-d))
            assert prot==F(n,n-d)*full
        ey=-oldK+(n-1)*sum(dk[j] for e,_,dk in data if e not in endpoints)/(len(phases)*(n-d))
        assert ey==-oldK+F(n-1,n-d)*n*sum(dk[j] for _,_,dk in data)/len(data)
        results.append({"source":0,"target":j,"protected_labels":d})
    return {"unitary":"Walsh Hadamard U(16), max P=1/16, P=J",
            "exact_feedback_states":len(data),"phase_measure":"four prescribed circle phases; not Haar quadrature",
            "protected_pair_checks":results,"row_rescaling_exact":str(ey_protected),
            "scope":"Port-normalization and scaled drift algebra only; no claim to reverify Haar-phase one-step inequalities by finite quadrature."}


def main():
    result={"status":"passed","python":platform.python_version(),
            "martingale":martingale_checks(),"marks":marked_first_exit_checks(),
            "feedback":feedback_normalization_checks(),
            "non_claims":["Finite tests do not certify the analytic theorem.",
                          "The old local one-step inputs retain their project proof status.",
                          "No fixed-dimensional entrance, microscopic law or BGS claim."]}
    with open(sys.argv[1],'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps({"status":"passed","marked_prefixes":result['marks']['deletion_prefixes'],
                      "first_exits":result['marks']['first_crossing_prefixes'],
                      "feedback_states":result['feedback']['exact_feedback_states'],
                      "martingale_powers":[r['p'] for r in result['martingale']['moments']]},sort_keys=True))


if __name__=='__main__':
    main()
