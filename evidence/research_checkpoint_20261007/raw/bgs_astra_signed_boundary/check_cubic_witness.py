#!/usr/bin/env python3
"""Exact finite controls only; no asymptotic numerical assertion.
All arithmetic is integer or fractions.Fraction; fail-closed without assert.
"""
import argparse, hashlib, json, math, platform, resource, time
from fractions import Fraction as F
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS, (768*1024**2,768*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(90,90))

def require(x,msg):
    if not x: raise RuntimeError(msg)

def isprime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))

def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,F(0))+v
        if out[k]==0:del out[k]
    return out

def multiply(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            n=tuple(x+y for x,y in zip(k,l));out[n]=out.get(n,F(0))+v*w
    return {k:v for k,v in out.items() if v}

def matmul(a,b):
    N=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(N)),F(0)) for j in range(N)] for i in range(N)]

def energy(p):return sum((v*v for v in p.values()),F(0))

def occupation_check(U,max_m,name):
    N=len(U);zero=(0,)*N
    require(matmul(U,list(map(list,zip(*U))))==[[F(i==j) for j in range(N)] for i in range(N)],name+' unitary')
    P=[[({zero:F(1)} if i==j else {}) for j in range(N)] for i in range(N)]
    X=[[{tuple(int(k==i) for k in range(N)):U[i][j]} if U[i][j] else {} for j in range(N)] for i in range(N)]
    rows=[]
    for m in range(1,max_m+1):
        P=[[sum_poly([multiply(P[i][k],X[k][j]) for k in range(N)]) for j in range(N)] for i in range(N)]
        tr=sum_poly([P[i][i] for i in range(N)]);B=energy(tr)
        for j in range(N):
            derivative={n:F(n[j])*v for n,v in tr.items() if n[j]}
            require(derivative=={n:m*v for n,v in P[j][j].items()},f'{name} derivative identity {m},{j}')
        E=sum((sum(nj*nj for nj in n)*v*v for n,v in tr.items()),F(0))
        diagE=sum((energy(P[j][j]) for j in range(N)),F(0))
        require(E==m*m*diagE,f'{name} derivative Parseval {m}')
        require(m*B<=E<=m*m*N,f'{name} gradient inequalities {m}')
        require(B<=m*N,f'{name} occupation bound {m}')
        rows.append({'m':m,'B':str(B),'gradient_energy':str(E),'diagonal_energy':str(diagE),'monomials':len(tr)})
    return rows

def sum_poly(polys):
    out={}
    for p in polys:out=add(out,p)
    return out

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--inject-failure',action='store_true');args=parser.parse_args()
    if args.inject_failure:require(False,'deliberate failure')
    modular=[]
    for p in [5,11,17,23,29]:
        require(isprime(p) and p%3==2,'prime scope')
        cubes=[pow(j,3,p) for j in range(p)];require(len(set(cubes))==p,'cubic permutation')
        # Exact Fourier-square character sum histogram: all nontrivial row
        # pairs have every root exponent once, while reflected pairs are constant.
        for j in range(p):
            for l in range(p):
                freq=(cubes[j]+cubes[l])%p;hist=[0]*p
                for k in range(p):hist[freq*cubes[k]%p]+=1
                require(hist==([p]+[0]*(p-1) if l==(-j)%p else [1]*p),'Fourier square character histogram')
        pairs=0; cubic=0; quadratic=0
        for c in range(1,p):
            for j in range(p):
                for l in range(p):
                    if j==l:continue
                    a=(cubes[j]-cubes[l])%p;b=(cubes[(j+c)%p]-cubes[(l+c)%p])%p
                    require(a and b,'nonzero row coefficients')
                    coeff=[(-b*c**3)%p,(-3*b*c*c)%p,(-3*b*c)%p,(a-b)%p]
                    require(coeff[2]!=0,'nonzero quadratic coefficient')
                    degree=3 if coeff[3] else 2
                    cubic+=degree==3;quadratic+=degree==2;pairs+=1
                    for k in [0,1,2,p-1]:
                        lhs=(a*k**3-b*(k+c)**3)%p;rhs=sum(co*k**r for r,co in enumerate(coeff))%p
                        require(lhs==rhs,'charge TT* phase polynomial')
                    # Every nonzero shift of a cubic has nonzero quadratic
                    # leading coefficient; for a quadratic the shift is linear.
                    for h in range(1,p):
                        lead=(degree*coeff[degree]*h)%p
                        require(lead!=0,'differenced leading coefficient')
        modular.append({'p':p,'row_pairs':pairs,'cubic_phases':cubic,'quadratic_phases':quadratic,'fourier_square_histograms':p*p})
    U=[[F(x,9) for x in row] for row in [[7,-4,-4],[-4,1,-8],[-4,-8,1]]]
    cycle=[[F(j==(i+1)%3) for j in range(3)] for i in range(3)]
    # Two disjoint 2-cycles demonstrate sharpness m=2,N=4 exactly.
    cycles2=[[F(j==(i^1)) for j in range(4)] for i in range(4)]
    occupation={'rational_dense_N3':occupation_check(U,6,'dense'), 'cycle_N3':occupation_check(cycle,6,'cycle3'), 'two_cycles_N4':occupation_check(cycles2,4,'cycles2')}
    require(occupation['two_cycles_N4'][1]['B']=='8','sharp occupation bound')
    result={'status':'passed','arithmetic':'integers and rational fractions; no floating tolerance','modular':modular,'occupation':occupation,'asymptotic_claim':'not numerically tested; see proof','python':platform.python_version()}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
