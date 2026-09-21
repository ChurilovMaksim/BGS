#!/usr/bin/env python3
"""Exact integer regression for periodic counts in the frozen-map classical sum rule."""
from __future__ import annotations
import json, math
import sympy as sp

S=sp.Matrix([[3,4],[2,3]])
I=sp.eye(2)

def main():
    rows=[]
    for m in range(1,81):
        fixed=abs(int((S**m-I).det()))
        # eigenvalue recurrence: a_m=lambda^m+lambda^-m, a_0=2,a_1=6
        a0,a1=2,6
        if m==0: tracepow=a0
        elif m==1: tracepow=a1
        else:
            for _ in range(2,m+1): a0,a1=a1,6*a1-a0
            tracepow=a1
        assert fixed==tracepow-2
        primitive=sum(int(sp.mobius(m//d))*abs(int((S**d-I).det())) for d in sp.divisors(m))
        assert primitive % m == 0 and primitive >= 0
        rows.append({"m":m,"fixed":fixed,"primitive_orbits":primitive//m})
    print(json.dumps({"status":"PASS","scope":"Exact integer periodic-count regression only; the analytic Ruelle trace theorem is external.","rows_checked":len(rows),"last":rows[-1]},indent=2))
if __name__=="__main__":main()
