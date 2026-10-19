#!/usr/bin/env python3
"""Independent exact residues, positive path coefficients and sharp clock controls."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb,factorial
import json,platform,sys
import sympy as s
from exact_unitaries import Q


def circle_conj(x,z):
    return s.conjugate(x).subs(s.conjugate(z),1/z)


def square(x,z):
    return s.cancel(x*circle_conj(x,z))


def rat_residue(expr,z,p):
    n,d=s.fraction(s.cancel(expr))
    pn,pd=s.Poly(n,z,extension=s.I).shift(p),s.Poly(d,z,extension=s.I).shift(p)
    order=0
    while pd.nth(order)==0:order+=1
    if not order:return s.S.Zero
    coeff=[]
    for k in range(order):
        coeff.append(s.cancel((pn.nth(k)-sum(pd.nth(order+j)*coeff[k-j]
                      for j in range(1,k+1)))/pd.nth(order)))
    return coeff[-1]


def seed_residues():
    z=s.symbols('z');I=s.I
    W=s.Matrix([[1,1,1,1],[1,I,-I,-1],[1,-1,-1,1],[1,-I,I,-1]])/2
    assert W*W.adjoint()==s.eye(4)
    B=s.Matrix(4,4,lambda i,j:W[i,j]*s.conjugate(W[j,i]))
    ev=B.eigenvals()
    assert ev=={(2+s.sqrt(2))/4:1,(2-s.sqrt(2))/4:1,s.sqrt(2)/4:1,-s.sqrt(2)/4:1}
    rows=[]
    for a in range(4):
        for b in range(4):
            if a==b:continue
            e,f=[j for j in range(4) if j not in [a,b]]
            keep=[a,b,f]
            Qm=s.Matrix(3,3,lambda i,j:s.cancel(W[keep[i],keep[j]]
                       +z*W[keep[i],e]*W[e,keep[j]]/(1-z*W[e,e])))
            g=s.cancel(square(Qm[0,1],z)+square(Qm[0,2],z)*square(Qm[2,1],z)/(1-square(Qm[2,2],z)))
            n,d=s.fraction(g/z)
            poles=s.solve(d,z)
            inside=[]
            for p in poles:
                cmp=s.simplify(p*s.conjugate(p)-1)
                assert cmp.is_real and cmp.is_zero is False,(a,b,p,cmp)
                if cmp.is_negative:inside.append(p)
                else:assert cmp.is_positive,(a,b,p,cmp)
            value=s.simplify(sum(s.residue(g/z,z,p) for p in inside))
            rows.append({'a':a,'b':b,'mean_exact':str(value),
                         'inside_poles_exact':[str(p) for p in inside]})
    values=[s.Rational(r['mean_exact']) for r in rows]
    assert values.count(s.Rational(8,15))==4 and values.count(s.Rational(1,2))==8
    assert sum(values)/12==s.Rational(23,45)
    return {'unitarity_exact':True,'B_spectrum_exact':[str(v) for v in ev],
            'ordered_pairs':rows,'uniform_pair_mean_exact':'23/45'}


def poly_mul(a,b,L):
    out=defaultdict(Q)
    for alpha,x in a.items():
        for beta,y in b.items():
            gamma=tuple(i+j for i,j in zip(alpha,beta))
            if sum(gamma)<=L:out[gamma]=out[gamma]+x*y
    return dict(out)


def path_checks():
    ii=Q(F(0),F(1));one=Q(F(1))
    W=[[one,one,one,one],[one,ii,-ii,-one],
       [one,-one,-one,one],[one,-ii,ii,-one]]
    W=[[z/2 for z in row] for row in W]
    coeff={(0,0):W[0][1]}
    correction=None
    for L in range(1,9):
        grouped=defaultdict(Q)
        classical=F(0)
        for word in product([2,3],repeat=L):
            amp=W[0][word[0]]
            for x,y in zip(word,word[1:]):amp=amp*W[x][y]
            amp=amp*W[word[-1]][1]
            alpha=(word.count(2),word.count(3))
            grouped[alpha]=grouped[alpha]+amp
            classical+=amp.abs2()
        quantum=sum(c.abs2() for c in grouped.values())
        assert quantum<=factorial(L)*classical
        assert classical==F(1,4)*F(1,2)**L
        coeff.update(grouped)
        if L==2:
            x=[W[0][e]*W[e][1].conj() for e in [2,3]]
            B=[[W[e][f]*W[f][e].conj() for f in [2,3]] for e in [2,3]]
            signed=sum(x[e]*B[e][f]*x[f].conj() for e in range(2) for f in range(2))
            diag=sum(W[e][e].abs2()*W[0][e].abs2()*W[e][1].abs2() for e in [2,3])
            assert Q(quantum-classical)==signed-diag
            correction=str(quantum-classical)
    power={(0,0):Q(F(1))}
    rows=[]
    for k in range(1,7):
        power=poly_mul(power,coeff,8)
        low=[]
        for L in range(9):
            energy=sum(c.abs2() for alpha,c in power.items() if sum(alpha)<=L)
            base=sum(c.abs2() for alpha,c in coeff.items() if sum(alpha)<=L)
            assert energy<=base
            assert energy<=F(1,4)*sum(factorial(j) for j in range(L+1))
            low.append(str(energy))
        rows.append({'k':k,'cumulative_low_degree_energies_exact':low})
    return {'internal_lengths':[1,8],'power_k':[1,6],
            'cooperon_L2_correction_exact':correction,'powers':rows}


def sharp_clock_checks():
    z=s.symbols('z');r=s.Rational(3,5)
    inner=(z-r)/(1-r*z)
    rows=[]
    for k in range(1,13):
        for kind,f in [('inner',inner),('noninner',(inner-1)/2)]:
            integrand=s.cancel(circle_conj(f**k,z)*s.diff(f**k,z))
            val=s.simplify(rat_residue(integrand,z,r))
            expected=s.Integer(k) if kind=='inner' else s.Rational(k*comb(2*k,k),2*4**k)
            assert val==expected and val<=k
            rows.append({'k':k,'kind':kind,'Dirichlet_energy_exact':str(val)})
    return {'degree_one_cavity':'Blaschke factor (z-3/5)/(1-3z/5)',
            'cases':rows,'sharp_linear_k_saturation':True}


def main():
    out={'status':'passed','python':platform.python_version(),'sympy':s.__version__,
         'seed':seed_residues(),'paths':path_checks(),'clock':sharp_clock_checks(),
         'non_claims':['No asymptotic transmission counterexample.',
                       'Finite checks do not certify the all-N analytic results.']}
    with open(sys.argv[1],'w') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'status':'passed','pair_mean':'23/45','ordered_pairs':12,
                      'path_lengths':[1,8],'clock_cases':len(out['clock']['cases'])},sort_keys=True))


if __name__=='__main__':main()
