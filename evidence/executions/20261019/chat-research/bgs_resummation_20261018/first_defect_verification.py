import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

P1={4:F(1,2),5:F(1,2)}
P2={3:F(2,9),6:F(1,36),7:F(-17,12),9:F(1,6),10:F(1,2),11:F(1,2)}

def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=c.get(i+j,F(0))+x*y
    return {i:x for i,x in c.items() if x}

def add(a,b):
    c=dict(a)
    for i,x in b.items():c[i]=c.get(i,F(0))+x
    return {i:x for i,x in c.items() if x}

def scale(a,x):return {i:v*x for i,v in a.items() if v*x}

def primitive_numerator(h):
    out={}
    for j,p in [(1,P1),(2,P2)]:
        if h<j:continue
        n=h-j
        factor=F(math.factorial(2*h-2),math.factorial(2*j-2)*4**n*math.factorial(n))
        power={2*n+4*g:F(math.comb(n,g)*(-1)**(n-g)) for g in range(n+1)}
        out=add(out,scale(mul(p,power),factor))
    return out

def rational_coeff(numerator,denominator_power,m):
    return m*sum((v*math.comb(m-q+denominator_power-1,denominator_power-1)
                 for q,v in numerator.items() if m>=q),F(0))

def main(destination):
    assert sum(P2.values())==0 and sum(q*v for q,v in P2.items())==F(35,12)
    Q2={};running=F(0)
    for q in range(max(P2)+1):
        running+=P2.get(q,F(0))
        if running:Q2[q]=running
    assert not running and sum(Q2.values())==F(-35,12)
    L=sum(abs(x) for x in Q2.values())

    first=json.loads(Path('dependencies/h1_core_table.json').read_text())
    for p in sorted({r['p'] for r in first['cores']}):
        got={r['q']:F(r['multiplicity'])*(1-F(r['collapse_pairs'],2))/r['q']
             for r in first['cores'] if r['p']==p and r['common_edges']==1}
        assert got==P1,(p,got)
    second=json.loads(Path('dependencies/h2_core_table.json').read_text())
    primitive=json.loads(Path('primitive_run/result.json').read_text())
    for p in second['primes']:
        got={r['q']:F(r['histogram12'][3],12*r['q']) for r in second['open_core_histograms']
             if r['p']==p and r['histogram12'][3]}
        assert got==primitive_numerator(2)
        gotprim={r['q']:F(r['primitive12'],12*r['q']) for r in primitive['rows']
                 if r['p']==p and r['primitive12']}
        assert gotprim==P2

    H=150;powers=[{0:F(1)}]
    for h in range(1,H+1):powers.append(mul(powers[-1],{0:F(1),1:F(1),2:F(1),3:F(1)}))
    def reduced(m,h):
        n=h-1;fac=F(math.factorial(2*n),4**n*math.factorial(n))*(-1)**n
        result=rational_coeff(scale({q+2*n:v for q,v in mul(P1,powers[n]).items()},fac),h,m)
        if h>=2:
            n=h-2;fac=F(math.factorial(2*n+2),2*4**n*math.factorial(n))*(-1)**n
            result+=rational_coeff(scale({q+2*n:v for q,v in mul(Q2,powers[n]).items()},fac),h,m)
        return result

    identities=0
    for m in range(3,81):
        for h in range(1,(m+1)//2+1):
            direct=rational_coeff(primitive_numerator(h),2*h-1,m)
            value=reduced(m,h)
            assert direct==value
            bound=math.comb(2*h-2,h-1)*(1+L*(h-1)/2)*m**h
            assert abs(value)<=bound
            identities+=1

    def multiply_linear(poly,a):
        out=[F(0)]*(len(poly)+1)
        for i,v in enumerate(poly):out[i]+=a*v;out[i+1]+=v
        return out
    polynomials={}
    for h in range(1,9):
        out=[F(0)]*(2*h+1)
        for q,v in primitive_numerator(h).items():
            term=[v/F(math.factorial(2*h-2))]
            term=multiply_linear(term,0)
            for j in range(2*h-2):term=multiply_linear(term,-q+2*h-2-j)
            for i,vv in enumerate(term):out[i]+=vv
        while out and not out[-1]:out.pop()
        assert len(out)==h+1
        assert out[-1]==(-1)**(h-1)*math.comb(2*h-2,h-1)*(1+F(35,24)*(h-1))
        polynomials[str(h)]=[str(v) for v in out]

    comparisons=[]
    for N in [100,1000,10000]:
        for ratio in [F(1,10),F(1,5)]:
            m=int(N*ratio);stop=min(H,(m+1)//2)
            val=sum((reduced(m,h)/N**h for h in range(1,stop+1)),F(0))
            r=4*ratio;a=L/2
            tail=F(0) if stop==(m+1)//2 else ratio*r**stop*((1+a*stop)/(1-r)+a*r/(1-r)**2)
            t=float(ratio);limit=t/math.sqrt(1+4*t)-35*t*t/(12*(1+4*t)**1.5)
            comparisons.append({'N':N,'m':m,'H':stop,'partial_sum':float(val),'certified_absolute_tail_upper':float(tail),
                                'limit_comparison':limit,'difference_from_limit':float(val)-limit})
    data={'status':'passed_exact_finite_checks','coefficient_domain':'integers and fractions.Fraction',
          'identity_cases':identities,'Q2_l1':str(L),'primitive_P2':{str(k):str(v) for k,v in P2.items()},
          'stable_polynomials':polynomials,'heisenberg_values':comparisons,
          'scope':'Formulas checked, asymptotic theorem proved separately. Higher-order diagram prediction gets a separate direct cycle/partition check.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))

if __name__=='__main__':main(sys.argv[1])
