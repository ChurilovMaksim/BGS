#!/usr/bin/env python3
"""Finite exact controls, not a proof of the all-order analytic theorem.
Standard library only. Checks remain active under python -O.
"""
import argparse
import itertools
import json
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p


def divmod_monic(p,q):
    p=trim(p); q=trim(q)
    require(q[-1]==1,'nonmonic divisor')
    out=[0]*max(1,len(p)-len(q)+1)
    while len(p)>=len(q) and p!=[0]:
        k=len(p)-len(q); a=p[-1]; out[k]=a
        for j,b in enumerate(q): p[j+k]-=a*b
        p=trim(p)
    return trim(out),p


def cyclotomics(nmax):
    result={}
    for n in range(1,nmax+1):
        p=[-1]+[0]*(n-1)+[1]
        for d in range(1,n):
            if n%d==0:
                p,r=divmod_monic(p,result[d]); require(r==[0],'cyclotomic division')
        result[n]=p
    return result


def det_fourier(exponents,n):
    # Subset determinant recurrence in Z[x]/(x^n-1), then reduce modulo Phi_n.
    dp={0:[1]+[0]*(n-1)}
    for row,e in enumerate(exponents):
        nxt={}
        for mask,p in dp.items():
            for col in range(n):
                if mask>>col&1: continue
                # Appending this column creates one inversion for each prior larger column.
                sign=(-1)**((mask>>(col+1)).bit_count())
                shift=(e*col)%n
                q=nxt.setdefault(mask|(1<<col),[0]*n)
                for j,a in enumerate(p):q[(j+shift)%n]+=sign*a
        dp=nxt
    return dp[(1<<n)-1]


def residue_sign(exponents,n):
    residues=[e%n for e in exponents]
    if len(set(residues))<n:return 0
    # Denominator ordering n-1,...,0.
    perm=[n-1-r for r in residues]
    return (-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))


def dimension(weight):
    out=Fraction(1)
    for i in range(len(weight)):
        for j in range(i+1,len(weight)):
            out*=Fraction(weight[i]-weight[j]+j-i,j-i)
    require(out.denominator==1,'nonintegral Weyl dimension')
    return out.numerator


def run(max_n=6,height=3,dimension_max_n=100):
    require(3<=max_n<=9,'max-n must be 3..9 (explicit resource cap)')
    require(1<=height<=6,'weight-height must be 1..6')
    require(dimension_max_n>=max_n,'dimension range too small')
    phis=cyclotomics(max_n); counts={'balanced_weights':0,'zero_characters':0,'nonzero_characters':0,'dimension_cases':0}
    for n in range(3,max_n+1):
        den=divmod_monic(det_fourier(list(range(n-1,-1,-1)),n),phis[n])[1]
        require(den!=[0],f'Vandermonde vanished: N={n}')
        for ascending in itertools.combinations_with_replacement(range(-height,height+1),n):
            if sum(ascending):continue
            weight=tuple(reversed(ascending)); exponents=[weight[j]+n-1-j for j in range(n)]
            num=divmod_monic(det_fourier(exponents,n),phis[n])[1]
            sign=residue_sign(exponents,n)
            require(num==trim([sign*a for a in den]),f'character determinant: {n},{weight}')
            dim=dimension(weight)
            require(not any(weight) or dim>=n,f'minimum dimension: {n},{weight}')
            counts['balanced_weights']+=1
            counts['zero_characters' if sign==0 else 'nonzero_characters']+=1
    for n in range(3,dimension_max_n+1):
        adj=dimension((1,)+(0,)*(n-2)+(-1,))
        rs=dimension((2,)+(0,)*(n-2)+(-2,))
        cross=dimension((2,)+(0,)*(n-3)+(-1,-1))
        ra=0 if n==3 else dimension((1,1)+(0,)*(n-4)+(-1,-1))
        require(adj==n*n-1,'adjoint dimension')
        require(rs==n*n*(n-1)*(n+3)//4,'symmetric residual dimension')
        require(ra==n*n*(n+1)*(n-3)//4,'alternating residual dimension')
        require(cross==(n*n-1)*(n*n-4)//4,'cross residual dimension')
        require(2+4*adj+rs+ra+2*cross==n**4,'multiplicity total')
        require(rs+ra==n*n*(n*n-3)//2,'zero multiplicity')
        require(Fraction(1,cross)<=Fraction(1,adj),'exact operator norm maximum')
        counts['dimension_cases']+=1
    # Adversarial controls: duplicate Fourier rows must vanish; corrupt claimed sign must fail.
    n=3; den=divmod_monic(det_fourier([2,1,0],n),phis[n])[1]
    require(divmod_monic(det_fourier([2,2,0],n),phis[n])[1]==[0],'duplicate rows')
    rejected=False
    try:require(den==trim([-a for a in den]),'intentional sign mutation')
    except RuntimeError:rejected=True
    require(rejected,'mutation not rejected')
    return {'status':'PASS','arithmetic':'integer cyclotomic quotient rings and rational Weyl dimensions',
            'scope':{'character_N':[3,max_n],'balanced_dominant_weight_coordinate_bound':height,
                     'dimension_N':[3,dimension_max_n]},'counts':counts,'negative_controls':2,
            'non_claims':['No numerical Haar integration or full moment-channel construction.',
                          'No exhaustive all-k verification or analytic-proof certification.',
                          'No BGS or global priority conclusion.']}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--max-n',type=int,default=6);p.add_argument('--weight-height',type=int,default=3);p.add_argument('--dimension-max-n',type=int,default=100)
    a=p.parse_args(); print(json.dumps(run(a.max_n,a.weight_height,a.dimension_max_n),indent=2,sort_keys=True))
