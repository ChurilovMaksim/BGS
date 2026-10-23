"""Exact independent controls; no fitting and no claim of formal verification.

Python uses symmetric congruence/Schur complements, C++ uses row elimination.
Here all set partitions are generated, not just defects zero through two.
Both the cycle-count generating identity and all four d mod 4 cases are checked.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def partitions(n):
    if not n:
        yield ()
        return
    for previous in partitions(n-1):
        yield previous + ((n-1,),)
        for i, block in enumerate(previous):
            yield previous[:i] + (block+(n-1,),) + previous[i+1:]


def alpha(n):
    values = [Fraction(0)] * (n+1)
    for m in range(1,n+1):
        values[m] = Fraction(1,factorial(m)) - sum(
            comb(m-1,k-1)*values[k]/factorial(m-k) for k in range(1,m))
    return values


def quadratic_normal_form(matrix,p):
    """Congruence diagonalization: returns rank and determinant square class."""
    a = [[v%p for v in row] for row in matrix]
    r, character = 0, 1
    while a:
        pivot = next((i for i in range(len(a)) if a[i][i]),None)
        if pivot is None:
            pair = next(((i,j) for i in range(len(a)) for j in range(i+1,len(a))
                         if a[i][j]),None)
            if pair is None:
                break
            i,j = pair
            for c in range(len(a)):
                a[i][c] = (a[i][c]+a[j][c])%p
            for b in range(len(a)):
                a[b][i] = (a[b][i]+a[b][j])%p
            pivot = i
        a[0],a[pivot] = a[pivot],a[0]
        for row in a:
            row[0],row[pivot] = row[pivot],row[0]
        q = a[0][0]
        assert q
        chi = pow(q,(p-1)//2,p)
        character *= 1 if chi==1 else -1
        inverse = pow(q,-1,p)
        a = [[(a[i][j]-a[i][0]*inverse*a[0][j])%p
              for j in range(1,len(a))] for i in range(1,len(a))]
        r += 1
    return r,character


def quotient(matrix,blocks,p):
    labels = {i:j for j,b in enumerate(blocks) for i in b}
    out = [[0]*len(blocks) for _ in blocks]
    for i,row in enumerate(matrix):
        for j,v in enumerate(row):
            out[labels[i]][labels[j]] = (out[labels[i]][labels[j]]+v)%p
    return out


def cycle_difference(cycle,p):
    n = len(cycle)
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        j = (i+1)%n
        a[i][j] += 1
        a[j][i] += 1
        a[cycle[i]][cycle[j]] -= 1
        a[cycle[j]][cycle[i]] -= 1
    half = pow(2,-1,p)
    return [[v*half%p for v in row] for row in a]


def active_identity(maximum=8):
    checked = 0
    for n in range(maximum+1):
        ps = list(partitions(n))
        for k in range(n+1):
            actual = defaultdict(int)
            for blocks in ps:
                h = n-len(blocks)
                g = k-sum(any(i<k for i in b) for b in blocks)
                w = 1
                for b in blocks:
                    w *= factorial(len(b)-1)
                actual[g,h-g] += w
            expected = {(0,0):1}
            for j in range(n):
                new = defaultdict(int,expected)
                for (g,t),w in expected.items():
                    new[g+(j<k),t+(j>=k)] += j*w
                expected = dict(new)
            assert {x:v for x,v in actual.items() if v} == {
                x:v for x,v in expected.items() if v},(n,k)
            checked += 1
    return checked


def full_polynomials(n,p,cutoff=None):
    values = alpha(n)
    ps = []
    for blocks in partitions(n):
        if cutoff is not None and 2*(n-len(blocks))>cutoff:
            continue
        w = Fraction(1)
        for b in blocks:
            w *= values[len(b)]
        ps.append((blocks,n-len(blocks),w))
    polynomials = [defaultdict(lambda: [Fraction(0),Fraction(0)]) for _ in range(4)]
    checks,diagrams = 0,0
    units = [(1,0),(0,1),(-1,0),(0,-1)]
    for tail in permutations(range(1,n)):
        matrix = cycle_difference((0,)+tail,p)
        rank,_ = quadratic_normal_form(matrix,p)
        active = {i for i,row in enumerate(matrix) if any(row)}
        assert len(active)<=4*rank
        assert all((i-1)%n in active or (i+1)%n in active for i in active)
        active_runs=sum((i-1)%n not in active for i in active)
        assert 2*active_runs<=len(active) and active_runs<=2*rank
        if cutoff is not None and rank>cutoff:
            continue
        for blocks,h,w in ps:
            g = len(active)-sum(bool(active.intersection(b)) for b in blocks)
            pulled = quotient(matrix,blocks,p)
            if cutoff==4 and h==2 and any(v for row in pulled for v in row):
                continue
            r,chi = quadratic_normal_form(pulled,p)
            assert 2*g+r>=rank
            if g==0:
                assert r==rank
            checks += 1
            phase = ((r if p%4==3 else 0)+(2 if chi==-1 else 0))%4
            e = 2*h+r
            if cutoff is not None and e>cutoff:
                continue
            for residue in range(4):
                real,imag = units[phase*residue%4]
                polynomials[residue][e][0] += n*w*real
                polynomials[residue][e][1] += n*w*imag
            diagrams += 1
    result = []
    for residue,poly in enumerate(polynomials):
        assert all(v[1]==0 for v in poly.values()),(n,p,residue,poly)
        coefficients = {str(e):str(v[0]) for e,v in sorted(poly.items()) if v[0]}
        result.append({'p':p,'n':n,'d_mod_4':residue,'coefficients':coefficients,
                       'variable':'x=N^(-1/2)','diagrams':diagrams,
                       'exponent_cutoff':cutoff})
    return result,checks


def rank_three_matrix_control():
    matrix = cycle_difference((0,2,4,1,3),5)
    rank,character = quadratic_normal_form(matrix,5)
    assert rank==3 and character==1
    assert all(sum(matrix[i][j]*j for j in range(5))%5==0 for i in range(5))
    pair_ranks=[]
    for a in range(5):
        for b in range(a+1,5):
            blocks=tuple([(a,b)]+[(i,) for i in range(5) if i not in (a,b)])
            r,_ = quadratic_normal_form(quotient(matrix,blocks,5),5)
            assert r==3
            pair_ranks.append(r)
    return {'p':5,'n':5,'rank':rank,'determinant_character':character,
            'pair_restriction_ranks':pair_ranks,'gaussian_phase':'positive'}


def main():
    cpp = json.loads((ROOT/'next_order_results.json').read_text())
    polynomials=[]
    rank_checks=0
    for p in (3,5,7):
        for n in range(3,7):
            cases,checks = full_polynomials(n,p)
            rank_checks += checks
            polynomials += cases
            target = next(c for c in cpp['cases'] if c['n']==n and c['p']==p)
            for e in range(5):
                assert Fraction(cases[0]['coefficients'].get(str(e),'0')) == Fraction(
                    target['coefficient_numerators'][e],12),(p,n,e)
    for n in (7,8,9):
        cases,checks = full_polynomials(n,3,cutoff=4)
        rank_checks += checks
        polynomials += cases
        target = next(c for c in cpp['cases'] if c['n']==n and c['p']==3)
        for e in range(5):
            assert Fraction(cases[0]['coefficients'].get(str(e),'0')) == Fraction(
                target['coefficient_numerators'][e],12),(3,n,e)
    # Independent comparison with the previous d=1 mod 4 computation.
    earlier = {3:4,4:42,5:165,6:390}
    for n,c in earlier.items():
        case = next(q for q in polynomials if q['p']==3 and q['n']==n and q['d_mod_4']==1)
        assert Fraction(case['coefficients']['4'])==c
    arithmetic = rank_three_matrix_control()
    for residue in range(4):
        case = next(q for q in polynomials if q['p']==5 and q['n']==5 and q['d_mod_4']==residue)
        assert Fraction(case['coefficients']['3'])==10
    data={'all_passed':True,'active_identity_cases':active_identity(),
          'rank_defect_diagrams_checked':rank_checks,'polynomials':polynomials,
          'rank_three_control':arithmetic,
          'scope':'Exact finite checks. General results rely on the separate proof, not these computations.'}
    (ROOT/'independent_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'active_identity_cases':data['active_identity_cases'],
                     'rank_defect_diagrams_checked':rank_checks,'polynomials':len(polynomials)}))


if __name__=='__main__':
    main()
