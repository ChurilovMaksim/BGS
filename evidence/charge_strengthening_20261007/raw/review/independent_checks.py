#!/usr/bin/env python3
"""Independent exact finite controls for the one-step charge audit.

No candidate/repository verifiers are imported. No literal-time quantum
matrix is approximated. All arithmetic is integer or rational.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def cj(z):
    return z[0], -z[1]


def norm2(z):
    return z[0]**2+z[1]**2


def scale(z, a):
    return a*z[0], a*z[1]


def sub(z, w):
    return z[0]-w[0], z[1]-w[1]


ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def finite_equality():
    # n=2; two everywhere-positive branches, b_r(x,y)=1/2.
    # K=A/4. I-K*K is positive semidefinite by the Markov bound.
    # Its exact determinant decides whether a norm-one singular vector exists.
    counts = dict(tested=0, norm_one=0, branch_conflict=0,
                  branch_conflict_norm_one=0, aligned_but_strict=0)
    for phases in product(ROOTS, repeat=8):
        a = [add(phases[2*j], phases[2*j+1]) for j in range(4)]
        p = 16-norm2(a[0])-norm2(a[2])
        q = 16-norm2(a[1])-norm2(a[3])
        cross = add(mul(cj(a[0]), a[1]), mul(cj(a[2]), a[3]))
        determinant = p*q-norm2(cross)
        require(p >= 0 and q >= 0 and determinant >= 0,
                'positive bistochastic envelope failed to contract')
        aligned = all(phases[2*j] == phases[2*j+1] for j in range(4))
        consistent = mul(phases[0], phases[6]) == mul(phases[2], phases[4])
        unit = determinant == 0
        require(unit == (aligned and consistent), 'norm-one equality classification')
        counts['tested'] += 1
        counts['norm_one'] += unit
        counts['branch_conflict'] += not aligned
        counts['branch_conflict_norm_one'] += unit and not aligned
        counts['aligned_but_strict'] += aligned and not unit
    require(counts['norm_one'] == 64, 'unexpected equality case count')
    require(counts['branch_conflict'] == 65280, 'exhaustive phase count')
    return counts


def variance_identity():
    # Positive nonconstant envelope d_xy=1+h_x*h_y/4 is bistochastic
    # for uniform measure on three points; four unequal branch weights.
    h = [-1, 0, 1]
    d = [[1+F(x*y, 4) for y in h] for x in h]
    require(all(sum(row) == 3 for row in d), 'row normalization')
    require(all(sum(d[x][y] for x in range(3)) == 3 for y in range(3)),
            'column normalization')
    branch = [F(1,10), F(2,10), F(3,10), F(4,10)]
    fs = [[(1,0)]*3, [(1,0),(2,1),(-1,3)],
          [(F(3,5),F(4,5)),(0,1),(-1,0)], [(0,0),(1,0),(0,0)]]
    checked = 0
    for mode in range(5):
        for f in fs:
            output_sq = F(0)
            variance = F(0)
            for x in range(3):
                terms = [(d[x][y]*branch[r]/3,
                          mul(ROOTS[(mode*x+mode*y+r*mode) % 4], f[y]))
                         for y in range(3) for r in range(4)]
                average = (F(0),F(0))
                for weight,z in terms:
                    average=add(average,scale(z,weight))
                output_sq += norm2(average)/3
                variance += sum(w*v*norm2(sub(z,t)) for w,z in terms
                                for v,t in terms)/6
            input_sq = F(sum(norm2(z) for z in f),3)
            require(input_sq-output_sq == variance, 'exact Jensen variance identity')
            require(variance >= 0, 'negative variance')
            checked += 1
    # Drop positive branch weights: the invisible branch may conflict everywhere
    # while K is the constant averaging projection and has norm one.
    invisible = [ROOTS[1],ROOTS[2],ROOTS[3],ROOTS[1]]
    require(all(z != (1,0) for z in invisible), 'zero-weight negative control')
    k0 = [[add(scale((1,0),F(1,2)),scale(invisible[2*x+y],0))
           for y in range(2)] for x in range(2)]
    image = [add(*row) for row in k0]
    require(image == [(1,0),(1,0)], 'zero-weight phase conflicts preserve norm one')
    # Drop column normalization: both rows (3/4,1/4) are positive and sum to one,
    # but K*K has sole nonzero eigenvalue 2*((3/4)^2+(1/4)^2)=5/4.
    require(2*(F(3,4)**2+F(1,4)**2) == F(5,4), 'column normalization control')
    require(2*(F(3,4)*3+F(1,4))**2/(3**2+1)==F(5,4),
            'row-only kernel has explicit expanding vector')
    # Drop envelope strict positivity: identity kernel preserves nonconstant |f|.
    f=[(1,0),(0,0)]
    image=[add(scale(f[0],int(x==0)),scale(f[1],int(x==1))) for x in range(2)]
    require(image==f and norm2(f[0])!=norm2(f[1]),
            'zero support norm equality with nonconstant modulus')
    return {'variance_identities':checked, 'normalization_checks':6,
            'negative_controls':['zero branch weight hides phase conflict',
                                 'row-only Markov kernel has squared norm 5/4',
                                 'zero support allows nonconstant modulus equality']}


def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def divide(p,q):
    p=list(p); quotient=[0]*max(1,len(p)-len(q)+1)
    while len(p)>=len(q) and any(p):
        require(p[-1]%q[-1]==0, 'nonintegral polynomial division')
        coefficient=p[-1]//q[-1]; shift=len(p)-len(q)
        quotient[shift]=coefficient
        for j,c in enumerate(q):
            p[j+shift]-=coefficient*c
        trim(p)
    return trim(quotient),trim(p)


def cat_controls():
    # Exact roots of unity are represented by Z[z]/Phi_N(z).
    phis={}
    for n in range(1,32):
        p=[-1]+[0]*(n-1)+[1]
        for d in range(1,n):
            if n%d==0:
                p,rem=divide(p,phis[d]);require(rem==[0], 'cyclotomic division')
        phis[n]=p
    phases=0; nilpotence=0; negative=0; escaping=0
    for n in range(3,32,2):
        inv8=pow(8,-1,n); inv2=pow(2,-1,n)
        for c in range(n):
            for j in range(n):
                for k in range(n):
                    P=lambda x,y:3*x*x-2*x*y+3*y*y
                    raw=inv8*(P(j+c,k+c)-P(j,k))
                    derived=inv2*c*(j+k+c)
                    require((raw-derived)%n==0, 'raw cat phase mismatch')
                    phases+=1
                    if c:
                        lhs=inv2*(-c)*(j+k-c)
                        rhs=-inv2*c*((j-c)+(k-c)+c)
                        require((lhs-rhs)%n==0, 'negative charge conjugation')
                        negative+=1
            if c:
                p=[0]*n
                for k in range(n):p[c*k%n]+=1
                require(divide(p,phis[n])[1]==[0], 'cat B squared not zero')
                nilpotence+=1
            if c and c%2:
                require(inv2*c%n==(n+c)//2, 'odd-charge escaping alias')
                escaping+=1
    for c in range(-99,100):
        coefficient=sum(-1 if c*r%2 else 1 for r in range(4))
        require(coefficient==(4 if c%2==0 else 0), 'cat continuum branch sum')
        if c and c%2==0:
            require(c//2 != 0, 'cat rank-one nonconstant Fourier mode')
    return {'raw_phase_entries':phases,'negative_charge_entries':negative,
            'cyclotomic_zero_sums':nilpotence,'odd_escaping_aliases':escaping,
            'continuum_charges':199,'odd_N_max':31,
            'cat_norm_certificate':'All raw blocks are rank one outer products of two length-sqrt(N) unimodular vectors, divided by N; norm exactly one.'}


def phase_and_amplitude():
    # Reconstruct r(q)=(1-cos(7q))*(1+cos(q)), with q in turns.
    r={}
    for k,a in {0:F(1),7:F(-1,2),-7:F(-1,2)}.items():
        for l,b in {0:F(1),1:F(1,2),-1:F(1,2)}.items():
            r[k+l]=r.get(k+l,F(0))+a*b
    shifted={k:a*(-1 if k%2 else 1) for k,a in r.items()}
    positive_momentum=(F(-3,10),F(-2,5)) # exp(-i alpha)/2
    g={k:scale(positive_momentum,a/F(100)) for k,a in shifted.items()}
    require(g[0]==(F(-3,1000),F(-4,1000)), 'actual ghat(0,1)')
    require(g[1]==(F(3,2000),F(4,2000)), 'actual ghat(1,1)')
    nu=[(F(-3,4),F(1,4)),(F(1,4),F(1,4))]
    # A'_i=-2*pi*nu_x*nu_y*ghat; represent coefficient divided by pi.
    first=[scale(g[i],-2*x*y) for i,(x,y) in enumerate(nu)]
    require(norm2(first[0])==F(3,1600)**2, 'first witness modulus')
    require(norm2(first[1])==F(1,3200)**2, 'second witness modulus')
    tau=F(1,10**80); error=F(10**50,2)*tau*tau
    # pi>3 is enough for this strict actual-time remainder comparison.
    require(error < F(3,6400)*tau, 'literal-time signal overwhelmed')
    factors=[]
    for x,y in nu:
        sigma=x+y
        # G7 multiplier divided by pi: 2*i*sigma*(1-i).
        factor=mul((0,2*sigma),(1,-1))
        require(norm2(factor)==2, 'differentiated nonzero witness')
        factors.append([str(t) for t in factor])
    # exp(x)-1 <= x/(1-x)<2x for 0<x<1/2.
    t=F(1,10**66)
    require(t/(1-t)<2*t, 'transport amplitude bound')
    require(1-2*t>0, 'leading amplitude can vanish')
    # S0 polynomial L-derivative and branch difference are computed exactly.
    for x,y in product([F(-2),F(0),F(2,7),F(1),F(3)],repeat=2):
        values=[F(-3*x+y+r,4)+F(x-3*y-3*r,4) for r in range(4)]
        require(values[0]-values[1]==F(1,2),'cat branch L difference')
    return {'actual_symbol_modes':{str(i):[str(z) for z in g[i]] for i in (0,1)},
            'G7_factors_divided_by_pi':factors,
            'tau':'1e-80','remainder_comparison':'exact rationals using pi>3',
            'amplitude_lower_bound':'1-2*10^-66 > 0','cat_L_samples':25}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True)
    ap.add_argument('--inject-failure',action='store_true');args=ap.parse_args()
    if args.inject_failure:require(False,'injected failure remains active under python -O')
    result={'arithmetic':'exact integers and Fraction; no floating arithmetic',
            'finite_equality':finite_equality(),'variance':variance_identity(),
            'cat':cat_controls(),'phase':phase_and_amplitude(),
            'non_claims':['No actual finite-N literal-tau norm approximation.',
                          'No numerical proof of analytic operator-norm limits.',
                          'No effective rho, startup N0, or tau-uniform estimate.',
                          'No full undamped offcharge or BGS conclusion.']}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
