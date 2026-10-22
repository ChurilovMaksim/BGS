#!/usr/bin/env python3
"""Independent exact-rational controls; no sampled nonlinear phase surrogate.

All pass/fail decisions use integers/Fraction. Decimal logarithms are display
only. Finite cycles cover m=1..24 and support, but do not prove, periodization.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json
from decimal import Decimal, localcontext

OUT = Path(__file__).resolve().parent
BASE = Path('/workspace/shared/bgs_paired_box_cancellation')
TARGET = BASE / 'transversality_and_measure.md'
EXPECTED = '2bddd915330543828c5637ea966f8b2081ce79208655c4632342b3f351391ee9'
checks = []
def check(name, condition, detail=''):
    assert condition, name
    checks.append({'name': name, 'passed': True, 'detail': detail})
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
check('frozen target hash', sha(TARGET) == EXPECTED)
slo = F(1414213562373095, 10**15)
shi = F(1414213562373096, 10**15)
check('rational enclosure for sqrt(2)', slo*slo < 2 < shi*shi)
llo, lhi = 3+2*slo, 3+2*shi
beta = F(29,5)
eta = F(1,10**70)+F(1,10**110)
check('beta below lambda below seven', 1 < beta < llo < lhi < 7)
check('eta inequalities', 0 < eta < F(2,10**70) < F(1,36) < F(1,16))
Lbound = (lhi+beta)/(slo*(llo-beta))
check('infinite beta Green norm below 300', Lbound < 300, str(Lbound))
check('nonlinear Hessian beta norm below 14 eta', 2*(1+beta) < 14)
check('resolvent at most 301', 300/(1-4200*eta) <= 301)
check('resolvent difference constant', 301*14*300 == 1264200)
check('G E constant', 301*14 == 4214)
period = 600*beta/(beta-1)
check('nonzero period sum constant', period == 725)
check('defect beta locality constant', 4214*725 <= 4*10**6)
holder_bound = 2*lhi/(llo-beta)+2*beta/(beta-1)
check('Holder split constant below 500', holder_bound < 500, str(holder_bound))
check('Holder final constant below 2e7', 301*32*500*4 < 2*10**7)
check('positive mass and negative off-diagonals', 1-4*eta > 0 and F(1,4)-eta > 0)
check('one-neighbour propagation factor at least 1/7', (F(1,4)-eta)/(F(3,2)+2*eta) >= F(1,7))
check('inverse Holder prefactor identity', F(4,7)/16 == F(1,28))

# Exact cat Green first column obtained by solving K_m v=e_0 over Q.
def inverse_first_column(m):
    A = [[F(0) for _ in range(m+1)] for __ in range(m)]
    for i in range(m):
        A[i][i] += F(3,2)
        A[i][(i-1)%m] -= F(1,4)
        A[i][(i+1)%m] -= F(1,4)
    A[0][m] = 1
    for i in range(m):
        pivot = A[i][i]
        A[i] = [x/pivot for x in A[i]]
        for j in range(m):
            if j == i: continue
            a = A[j][i]
            A[j] = [x-a*y for x,y in zip(A[j],A[i])]
    return [r[-1] for r in A]
cycles = []
for m in range(1,25):
    v = inverse_first_column(m)
    weighted = sum(beta**min(j,m-j)*v[j] for j in range(m))
    assert all(x > 0 for x in v)
    assert sum(v) == 1
    assert weighted < 300
    if m == 1: assert v == [1]
    if m == 2: assert v == [F(3,4),F(1,4)]
    cycles.append({'m':m,'weighted_norm':str(weighted),'unweighted_row_sum':'1'})
check('finite beta-weighted Green controls', len(cycles)==24, 'Exact Q arithmetic, m=1..24 including repeated neighbours.')

with localcontext() as ctx:
    ctx.prec=60
    lam=Decimal(3)+Decimal(2)*Decimal(2).sqrt()
    displays={'alpha_beta':str((Decimal(29)/5).ln()/lam.ln()),
              'gamma':str(lam.ln()/Decimal(7).ln()),
              'p_star':str(Decimal(7).ln()/lam.ln())}
paths=[TARGET, BASE/'winding_defect_locality.md', BASE/'independent_review/review.md',
       Path('/workspace/shared/BGS/mathematics/four_branch_parametrix.md'),
       Path('/workspace/shared/BGS/mathematics/fixed_map_path_model.md')]
record={'arithmetic':'Exact integers and fractions for all assertions; decimal exponents display only',
        'checks':checks,'finite_cycles':cycles,'decimal_display_only':displays,
        'source_hashes':{str(p):sha(p) for p in paths},
        'scope':'Constants and finite linear Green matrices only; no claim of nonlinear or asymptotic certification by computation.'}
(OUT/'check_results.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'passed_exact_checks':len(checks),'finite_cycles':len(cycles),'displays':displays},indent=2))
