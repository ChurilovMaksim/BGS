#!/usr/bin/env python3
"""Finite integer regression for the unitary encounter absolute envelope."""
from __future__ import annotations
from fractions import Fraction
from math import comb
import json

def main():
    rows=[]
    for k in range(1,100):
        lhs=sum(comb(k+v-1,v)*comb(k-1,v-1) for v in range(1,k+1))
        vand=comb(3*k-2,k)
        assert lhs<=vand
        assert Fraction(vand,1)<=Fraction(27,4)**k
        rows.append({"k":k,"sum":lhs,"vandermonde_bound":vand})
    print(json.dumps({"status":"PASS","scope":"Finite integer regression of the combinatorial envelope only; source recursion/order-by-order cancellation is external.","rows_checked":len(rows),"last_k":rows[-1]["k"]},indent=2))
if __name__=="__main__":main()
