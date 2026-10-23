#!/usr/bin/env python3
"""Exact controls of the positive Bernstein/occupation probability law."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb,factorial
import json,platform,sys
import sympy as s
from exact_unitaries import Q
from verify_transmission_appendix import rat_residue,circle_conj,poly_mul


def two_variable_low_degrees():
    one=Q(F(1));ii=Q(F(0),F(1))
    W=[[one,one,one,one],[one,ii,-ii,-one],
       [one,-one,-one,one],[one,-ii,ii,-one]]
    W=[[x/2 for x in row] for row in W]
    f={(0,0):W[0][1]};g={(0,0):W[1][1]}
    for L in range(1,9):
        ff=defaultdict(Q);gg=defaultdict(Q)
        for word in product([2,3],repeat=L):
            tail=one
            for x,y in zip(word,word[1:]):tail=tail*W[x][y]
            tail=tail*W[word[-1]][1]
            alpha=(word.count(2),word.count(3))
            ff[alpha]=ff[alpha]+W[0][word[0]]*tail
            gg[alpha]=gg[alpha]+W[1][word[0]]*tail
        f.update(ff);g.update(gg)
    unit={(0,0):one};fp=[unit];gp=[unit]
    for k in range(1,7):
        fp.append(poly_mul(fp[-1],f,8));gp.append(poly_mul(gp[-1],g,8))
    rows=[]
    for K in range(1,7):
        q=[[F(0) for _ in range(9)] for _ in range(K+1)]
        for k in range(K+1):
            coefficients=poly_mul(fp[k],gp[K-k],8)
            for alpha,c in coefficients.items():q[k][sum(alpha)]+=comb(K,k)*c.abs2()
        assert sum(row[0] for row in q)==F(1,2)**K
        cumulative=[]
        for L in range(9):
            mass=sum(sum(row[:L+1]) for row in q)
            base=sum(c.abs2() for a,c in f.items() if sum(a)<=L)+sum(c.abs2() for a,c in g.items() if sum(a)<=L)
            assert mass<=base<=F(1,2)*sum(factorial(j) for j in range(L+1))
            assert mass<=1
            cumulative.append(str(mass))
        rows.append({'K':K,'low_degree_cumulative_mass_exact':cumulative})
    return {'max_internal_degree':8,'max_K':6,'source':'second column of explicit S4 Schur function',
            'nonnegative_tensor_weights_exact':True,'Hardy_contraction_exact':True,'cases':rows}


def one_variable_full_law():
    z=s.symbols('z');r=s.Rational(3,5);b=(z-r)/(1-r*z)
    f=(b-1)/2;g=(b+1)/2
    rows=[]
    for K in range(1,11):
        masses=[];energies=[]
        for k in range(K+1):
            h=s.cancel(f**k*g**(K-k))
            integrand=s.cancel(h*circle_conj(h,z)/z)
            mass=s.simplify(rat_residue(integrand,z,s.S.Zero)+rat_residue(integrand,z,r))
            energy=s.simplify(rat_residue(s.cancel(circle_conj(h,z)*s.diff(h,z)),z,r))
            masses.append(comb(K,k)*mass);energies.append(comb(K,k)*energy)
            assert mass>=0 and energy>=0
        assert s.simplify(sum(masses))==1
        assert s.simplify(sum(energies))==s.Rational(K,2)
        assert s.simplify(sum(s.Rational(k,K)*mass for k,mass in enumerate(masses)))==s.Rational(4,5)
        rows.append({'K':K,'Bernstein_marginal_exact':[str(x) for x in masses],
                     'total_clock_exact':str(sum(energies)),'mean_B_over_K_exact':'4/5'})
    return {'matrix_inner':'Hadamard_2 diag((z-3/5)/(1-3z/5),1) Hadamard_2',
            'internal_dimension':1,'full_mass_and_clock_exact':True,
            'nonuniform_negative_control_mean_T':'4/5','cases':rows}


def main():
    out={'status':'passed','python':platform.python_version(),'sympy':s.__version__,
         'two_variable':two_variable_low_degrees(),'one_variable':one_variable_full_law(),
         'non_claims':['No large-N phase-path mass has been evaluated.',
                       'Finite exact controls do not certify the abstract Wasserstein approximation proof.']}
    with open(sys.argv[1],'w') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'status':'passed','two_variable_K':[1,6],'one_variable_K':[1,10],
                      'nonuniform_mean_exact':'4/5'}))


if __name__=='__main__':main()
