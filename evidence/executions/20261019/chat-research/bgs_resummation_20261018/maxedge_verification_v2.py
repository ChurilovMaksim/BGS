import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

target=Path(sys.argv[1])
H=150
powers=[[1]]
for h in range(1,H+1):
    old=powers[-1];out=[0]*(len(old)+3)
    for j,c in enumerate(old):
        for k in range(4):out[j+k]+=c
    powers.append(out)

def W(h,g):
    q=2*h+4*g
    return F(q*math.factorial(2*h-1)*(-1)**(h-g),4**h*math.factorial(g)*math.factorial(h-g))

def core_sum(m,h):
    total=F(0)
    for g in range(h+1):
        q=2*h+4*g
        if m>=q:total+=W(h,g)*F(m,q)*math.comb(m-q+2*h-1,2*h-1)
    return total

def positive_coeff(m,h):
    if m<2*h:return F(0)
    s=sum(c*math.comb(m-h-j-1,h-1) for j,c in enumerate(powers[h]) if m>=2*h+j)
    return F((-1)**h*math.factorial(2*h-1)*m*s,4**h*math.factorial(h))

checks=0
for m in range(2,121):
    for h in range(1,m//2+1):
        a=core_sum(m,h);b=positive_coeff(m,h)
        assert a==b
        assert (-1)**h*b>=0
        assert abs(b)<=math.comb(2*h-1,h)*m**h
        checks+=1

old=json.loads(Path('dependencies/h2_core_table.json').read_text())
rows=old['open_core_histograms']
expected={4:F(3,4),8:F(-3),12:F(9,4)}
for p in old['primes']:
    got={r['q']:F(r['histogram12'][4],12) for r in rows if r['p']==p and r['q']>=4 and r['histogram12'][4]}
    assert got==expected,(p,got)
assert {2*h+4*g:W(h,g) for h in [2] for g in range(h+1)}==expected

def mul_linear(poly,a):
    out=[F(0)]*(len(poly)+1)
    for i,c in enumerate(poly):out[i]+=a*c;out[i+1]+=c
    return out

def evaluate(poly,x):
    v=F(0)
    for c in reversed(poly):v=v*x+c
    return v

polys={}
for h in range(1,11):
    poly=[F(0)]*(2*h+1)
    for g in range(h+1):
        term=[F((-1)**(h-g),4**h*math.factorial(g)*math.factorial(h-g))]
        term=mul_linear(term,0)
        for j in range(2*h-1):term=mul_linear(term,-4*g-1-j)
        for i,c in enumerate(term):poly[i]+=c
    while poly and poly[-1]==0:poly.pop()
    assert len(poly)-1==h
    assert poly[-1]==(-1)**h*math.comb(2*h-1,h)
    for value in [6*h,6*h+1,8*h+7]:assert evaluate(poly,value)==positive_coeff(value,h)
    polys[str(h)]=[str(x) for x in poly]

comparisons=[]
for N in [100,1000,10000]:
    for ratio in [F(1,10),F(1,5)]:
        mm=int(N*ratio);stop=min(H,mm//2)
        value=sum((positive_coeff(mm,h)/N**h for h in range(1,stop+1)),F(0))
        tail=F(0) if stop==mm//2 else (4*ratio)**(stop+1)/(2*(1-4*ratio))
        limit=(1/math.sqrt(1+4*float(ratio))-1)/2
        comparisons.append({'N':N,'m':mm,'ratio':str(ratio),'H':stop,
                            'partial_sum':float(value),'certified_absolute_tail_upper':float(tail),
                            'limit_comparison':limit,'difference_from_limit':float(value)-limit})

result={'status':'passed_exact_finite_checks','versions':{'python':sys.version.split()[0],'arithmetic':'Python standard library integers and fractions.Fraction'},
        'exact_identity_cases':checks,'h2_crosscheck_fields':old['primes'],
        'h2_weights':{str(k):str(v) for k,v in expected.items()},
        'stable_polynomials':polys,'heisenberg_sector_values':comparisons,
        'scope':'Only e=2h sector; asymptotic proof and classification are separate.'}
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
