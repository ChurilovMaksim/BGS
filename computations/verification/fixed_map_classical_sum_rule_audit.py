#!/usr/bin/env python3
import json
import sympy as sp
S=sp.Matrix([[3,4],[2,3]])
I=sp.eye(2)
rows=[]
for m in range(1,81):
    fixed=abs(int((S**m-I).det()))
    a0,a1=2,6
    if m==1: tracepow=a1
    else:
        for _ in range(2,m+1): a0,a1=a1,6*a1-a0
        tracepow=a1
    assert fixed==tracepow-2
    primitive=sum(int(sp.mobius(m//d))*abs(int((S**d-I).det())) for d in sp.divisors(m))
    assert primitive%m==0 and primitive>=0
    rows.append({'m':m,'fixed':fixed,'primitive_orbits':primitive//m})
print(json.dumps({'status':'PASS','rows_checked':len(rows),'last':rows[-1]},indent=2))
