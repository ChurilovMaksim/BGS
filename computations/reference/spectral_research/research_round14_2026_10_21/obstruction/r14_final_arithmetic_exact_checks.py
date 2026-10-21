#!/usr/bin/env python3
"""Exact arithmetic for the final original-family tau/Pell attempt.

Only integer modular powers and rational Fourier coefficients are used.
No floating point tau replacement or spectral simulation occurs.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
S = (3, 4, 2, 3)
IDENTITY = (1, 0, 0, 1)

def mul(A, B, modulus=None):
    a,b,c,d=A
    e,f,g,h=B
    out=(a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)
    return tuple(x % modulus for x in out) if modulus else out

def mpow(A, n, modulus=None):
    out=IDENTITY
    while n:
        if n & 1:
            out=mul(out,A,modulus)
        A=mul(A,A,modulus)
        n >>= 1
    return out

def vp(n,p):
    assert n
    k=0
    while n % p == 0:
        k += 1
        n //= p
    return k

assert mpow(S,3)==(99,140,70,99)
certificates=[]
for s in range(13):
    for t in (0,1,2,10,79,80):
        r=3*5**t*7**s
        for p,e in ((5,t+1),(7,s+1)):
            modulus=p**(e+1)
            entry=mpow(S,r,modulus)[1]
            assert vp(entry,p)==e
        certificates.append({"s":s,"t":t,"r_bits":r.bit_length(),
                             "v5_N":t+1,"v7_N":s+1,
                             "tauN_denominator_2_exponent":80,
                             "tauN_denominator_5_exponent":max(79-t,0)})

rcoef={0:F(1)}
for k,c in [(1,F(1,2)),(7,F(-1,2)),(6,F(-1,4)),(8,F(-1,4))]:
    rcoef[k]=rcoef[-k]=c

def conv(A,B):
    out={}
    for k,a in A.items():
        for l,b in B.items():
            out[k+l]=out.get(k+l,F(0))+a*b
    return {k:a for k,a in out.items() if a}

factor=conv({14:F(1),7:F(-2),0:F(1)},
            {2:F(1),1:F(2),0:F(1)})
factor={k-8:-a/4 for k,a in factor.items()}
assert factor==rcoef
r2=conv(rcoef,rcoef)
assert min(r2)==-16 and max(r2)==16
assert r2[0]==F(9,4)

def grid_mean(M):
    return sum(a for k,a in r2.items() if k % M == 0)

means=[]
for a in range(2,9):
    M=7**a
    average=grid_mean(M)
    primitive=(M*average-(M//7)*grid_mean(M//7))/(M-M//7)
    assert average==F(9,4)
    assert primitive==(F(21,8) if a==2 else F(9,4))
    means.append({"a":a,"grid_average_r_squared":str(average),
                  "primitive_average_r_squared":str(primitive)})

d=[3,-1,2,-4,0,5,-5]
n=F(5)
N=7*n
mean=sum(d)/F(7)
left=n*n/N*sum(F(a-b)**2 for a in d for b in d)
right=2*n*sum((F(a)-mean)**2 for a in d)
assert left==right
report={"status":"passed",
        "scope":"Original Pell congruences and original hopping coefficient identities; no H2 bound.",
        "joint_valuation_cases":len(certificates),
        "certificates":certificates,
        "r_squared_Fourier_constant":str(r2[0]),
        "seven_primary_means":means,
        "block_commutator_identity_both_sides":str(left)}
(ROOT/"r14_final_arithmetic_exact_checks.json").write_text(
    json.dumps(report,indent=2)+"\n")
print(json.dumps({k:v for k,v in report.items() if k!="certificates"},indent=2))

