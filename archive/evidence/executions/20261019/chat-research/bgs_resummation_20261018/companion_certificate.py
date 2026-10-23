import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from first_defect_verification import P1,P2,primitive_numerator,rational_coeff

def trim(a):
    while a and not a[-1]:a.pop()
    return a

def plus(a,b,sign=1):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=sign*x
    return trim(c)

def times(a,b):
    if not a or not b:return []
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def power(a,n):
    out=[1]
    for _ in range(n):out=times(out,a)
    return out

def shift(a,n):return [0]*n+a if a else []

def gaussian_expectation(a,N):
    return sum((v*F(math.factorial(2*k),4**k*math.factorial(k)*N**k) for k,v in enumerate(a)),F(0))

def main(destination):
    # f(z)=(1+y)^5 z^5-(1+y)^4 z^4+y(1+y)^3 z^3+...+y.
    r=lambda k:[math.comb(k,i) for i in range(k+1)]
    a=[r(5),[-v for v in r(4)],shift(r(3),1),shift(r(2),1),shift(r(1),1),[0,1]]
    certificate=[]
    for degree in range(5,0,-1):
        boundaries=[plus(a[0],a[-1],s) for s in (1,-1)]
        for boundary in boundaries:assert boundary and all(v>=0 for v in boundary) and any(v>0 for v in boundary)
        certificate.append({'degree_in_disk_variable':degree,'coefficients':a,'leading_plus_constant':boundaries[0],
                            'leading_minus_constant':boundaries[1],
                            'boundary_degrees':[len(v)-1 for v in boundaries],
                            'first_positive_indices':[next(i for i,x in enumerate(v) if x>0) for v in boundaries]})
        a=[plus(times(a[0],a[i]),times(a[-1],a[degree-i]),-1) for i in range(degree)]

    # Q_y(z)=1-z+y(z^2+z^3+z^4+z^5); exact reciprocal coefficients as polynomials in y.
    M=50;R=[[1]]
    for m in range(1,M+1):
        term=list(R[m-1])
        for k in range(2,6):
            if m>=k:term=plus(term,shift(R[m-k],1),-1)
        R.append(term)
    RR=[];RRR=[]
    for m in range(M+1):
        RR.append([])
        for i in range(m+1):RR[-1]=plus(RR[-1],times(R[i],R[m-i]))
    for m in range(M+1):
        RRR.append([])
        for i in range(m+1):RRR[-1]=plus(RRR[-1],times(RR[i],R[m-i]))
    # Newton power sums of the five companion roots; characteristic coefficients [1,-1,y,y,y,y].
    cs=[[],[-1],[0,1],[0,1],[0,1],[0,1]];S=[[5]]
    for m in range(1,M+1):
        sm=[]
        for j in range(1,min(m-1,5)+1):sm=plus(sm,times(cs[j],S[m-j]),-1)
        if m<=5:sm=plus(sm,[m*x for x in cs[m]],-1)
        # For m>5 the loop above already includes j=5; for m<=5 it excludes the Newton term.
        S.append(sm)
    Q2={};running=F(0)
    for q in range(max(P2)+1):
        running+=P2.get(q,F(0))
        if running:Q2[q]=running
    assert running==0
    cases=0
    for N in (7,19,101):
        for m in range(1,M+1):
            max_direct=F(0)
            for h in range(1,m//2+1):
                for g in range(h+1):
                    if 2*h+4*g>m:continue
                    max_direct+=F(m*math.factorial(2*h-1)*(-1)**(h-g)*math.comb(m-4*g-1,2*h-1),4**h*math.factorial(g)*math.factorial(h-g)*N**h)
            max_companion=(gaussian_expectation(S[m],N)-1)/2
            assert max_direct==max_companion,(N,m,max_direct,max_companion)
            first_direct=sum((rational_coeff(primitive_numerator(h),2*h-1,m)/N**h for h in range(1,(m+1)//2+1)),F(0))
            rational=F(0)
            for q,v in P1.items():
                if m>=q:rational+=v*gaussian_expectation(R[m-q],N)/N
            for q,v in Q2.items():
                if m>=q:rational+=v*gaussian_expectation(RR[m-q],N)/N**2
                for d in range(2,6):
                    if m>=q+d:rational-=4*v*gaussian_expectation(shift(RRR[m-q-d],1),N)/N**2
            assert first_direct==m*rational,(N,m,first_direct,m*rational)
            cases+=1
    data={'status':'passed_exact_certificate','Schur_certificate':certificate,
          'identity_cases':cases,'identity_checks_per_case':2,
          'scope':'Finite exact algebra proves the root bound with the Schur/Rouche induction in the separate proof. Coefficient identities do not replace the analytic limit argument.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='Schur_certificate'}))

if __name__=='__main__':main(sys.argv[1])
