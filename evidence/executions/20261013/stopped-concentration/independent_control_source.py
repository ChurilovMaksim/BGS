"""Exact finite controls for a read-only independent mathematical audit.

This is not a proof of the universal stopped or asymptotic theorem.  It
checks four ordered pairs, including two diagonals, in one exactly
orthogonal 64 x 64 rational matrix.  Circle moments through degree (4,4)
are computed independently by residues.  Five rational circle phases per
surviving port check the full direct Schur update against the expansion.
"""

from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json


N = 64
DEN = 520
M = [[1 if (i & j).bit_count() % 2 == 0 else -1 for j in range(N)]
     for i in range(N)]
# S = R (H_64/8) C, with rational planar rotations.  Keeping a common
# denominator permits an independent integer Gram check.
for i in range(32):
    j = i + 32
    sign = 1 if i % 3 else -1
    a, b = M[i][:], M[j][:]
    M[i] = [5*x - sign*12*y for x, y in zip(a, b)]
    M[j] = [sign*12*x + 5*y for x, y in zip(a, b)]
for first in list(range(16)) + list(range(32, 48)):
    second = first + 16
    sign = 1 if first % 5 else -1
    for row in M:
        a, b = row[first], row[second]
        row[first] = 3*a + sign*4*b
        row[second] = -sign*4*a + 3*b
assert all(sum(M[i][k]*M[j][k] for k in range(N))
           == (DEN*DEN if i == j else 0)
           for i in range(N) for j in range(N))
S = [[Q(z, DEN) for z in row] for row in M]
P = [[z*z for z in row] for row in S]
delta = max(max(row) for row in P)
assert delta <= Q(1, 16)
assert all(sum(row) == 1 for row in P)
assert all(sum(P[i][j] for i in range(N)) == 1 for j in range(N))


def moment(a, p, q):
    """E[q_feedback^p conjugate(q_feedback)^q], for real a, exactly.

    For p,q >=1, integrate w^(p-1)/[(1-aw)^p(w-a)^q].
    The only interior pole is w=a, and Leibniz differentiates order q-1.
    Pure analytic and anti-analytic positive moments are zero.
    """
    if p == q == 0:
        return Q(1)
    if p == 0 or q == 0:
        return Q(0)
    eta = 1-a*a
    ans = Q(0)
    for j in range(min(p-1, q-1)+1):
        h = q-1-j
        ans += (Q(comb(q-1, j)*factorial(p-1)*factorial(p+h-1),
                  factorial(q-1)*factorial(p-1-j)*factorial(p-1))
                * a**(p-1-j+h) / eta**(p+h))
    return ans


MOM = [{(p, q): moment(S[e][e], p, q)
        for p in range(5) for q in range(5)} for e in range(N)]
PHASES = [(Q(1),Q(0)), (Q(-1),Q(0)), (Q(0),Q(1)),
          (Q(0),Q(-1)), (Q(3,5),Q(4,5))]
PAIRS = [(0,0),(17,17),(0,17),(31,47)]


def feedback_q(a, phase):
    c, s = phase
    den = (1-a*c)**2+(a*s)**2
    return ((c-a)/den, s/den)


def intensity_update(base, gain, q):
    re, im = q
    return (base+re*gain)**2+(im*gain)**2


checks = []
direct_cases = 0
for i, j in PAIRS:
    kij = sum(P[i][k]*P[k][j] for k in range(N))
    kcol = [sum(P[e][k]*P[k][j] for k in range(N)) for e in range(N)]
    p3 = sum(P[i][e]*kcol[e] for e in range(N))
    sums = {name:Q(0) for name in ["r2","A2","B2","C2","D2","F2"]}
    exact_mean = Q(0)
    exact_second = Q(0)
    squared_port_bound = Q(0)
    worst_range_squared_ratio = Q(0)
    frozen = set((i,j))
    for e in range(N):
        r = P[i][e]*P[e][j]
        A = B = C = D = F = Q(0)
        for k in range(N):
            if k == e:
                continue
            x, y = P[i][k], P[k][j]
            alpha = S[i][e]*S[e][k]*S[i][k]
            beta = S[k][e]*S[e][j]*S[k][j]
            b, d = P[i][e]*P[e][k], P[k][e]*P[e][j]
            A += y*alpha+x*beta
            B += x*d+y*b+2*alpha*beta
            C += alpha*beta
            D += alpha*d+beta*b
            F += b*d
        # The coefficients are extended to endpoint ports only for
        # nonnegative sum bounds.  Their actual frozen increment is zero.
        for name, value in [("r2",r),("A2",A),("B2",B),
                            ("C2",C),("D2",D),("F2",F)]:
            sums[name] += value*value
        # Compare squared pointwise coefficient bounds without roots.
        assert A*A <= 4*delta*delta*kij
        assert C*C <= delta**3*kij
        assert D*D <= 4*delta**5
        assert F <= delta**3 and r <= delta*delta
        # B bound includes a square root, so bound its coherent part.
        T1 = sum(P[i][k]*P[k][e]*P[e][j] for k in range(N) if k != e)
        T2 = sum(P[k][j]*P[i][e]*P[e][k] for k in range(N) if k != e)
        H = (B-T1-T2)/2
        assert T1 <= delta*delta and T2 <= delta*delta
        assert H*H <= delta**3*kij
        if e in frozen:
            continue
        co = {(0,0):-r,(1,0):A,(0,1):A,(1,1):B,
              (2,0):C,(0,2):C,(2,1):D,(1,2):D,(2,2):F}
        exact_mean += sum(v*MOM[e][pq] for pq,v in co.items())
        exact_second += sum(v*z*MOM[e][(p+t,q+h)]
                            for (p,q),v in co.items()
                            for (t,h),z in co.items())
        squared_port_bound += (r+4*abs(A)+4*abs(B)+8*abs(C)
                               +16*abs(D)+16*F)**2
        for phase in PHASES:
            qre, qim = feedback_q(S[e][e], phase)
            qabs2 = qre*qre+qim*qim
            direct = -kij
            for k in range(N):
                if k == e:
                    continue
                pik = intensity_update(S[i][k],S[i][e]*S[e][k],(qre,qim))
                pkj = intensity_update(S[k][j],S[k][e]*S[e][j],(qre,qim))
                direct += pik*pkj
            expanded = (-r+2*qre*A+qabs2*B
                        +2*(qre*qre-qim*qim)*C
                        +2*qre*qabs2*D+qabs2*qabs2*F)
            assert direct == expanded
            # S3 checked exactly by squaring its nonnegative RHS.
            assert direct*direct <= 32**2*delta**3
            worst_range_squared_ratio = max(worst_range_squared_ratio,
                                             direct*direct/(32**2*delta**3))
            direct_cases += 1
    assert sums["r2"] <= delta*delta*kij
    assert sums["A2"] <= 10*delta*delta*kij
    assert sums["B2"] <= 6*delta*delta*p3+12*delta*delta*kij
    assert sums["C2"] <= delta*delta*kij
    assert sums["D2"] <= 4*delta**3*p3
    assert sums["F2"] <= delta**4*kij
    assert exact_mean <= -kij/2+5*p3+2*delta*P[i][j]
    assert exact_second <= 2600*delta*delta*(kij+p3)
    assert squared_port_bound <= 2598*delta*delta*(kij+p3)
    checks.append({"pair":[i,j],"frozen_ports":len(frozen),
                   "surviving_ports":N-len(frozen),
                   "all_coefficient_sum_bounds":True,
                   "exact_phase_drift_bound":True,
                   "exact_raw_second_moment_bound":True,
                   "phase_drift":str(exact_mean/N),
                   "second_moment":str(exact_second/N),
                   "worst_sampled_S3_squared_ratio":float(worst_range_squared_ratio)})

# Independent exact checks of the endpoint constants used analytically.
c_cap = 2*Q(1,16)/(1-Q(1,16))**2 + Q(1,16)*(1+Q(1,16))/(1-Q(1,16))**3
d_cap = 4/(1-Q(1,16)) + 2*Q(1,16)/(1-Q(1,16))**2
assert c_cap == Q(752,3375) and c_cap < Q(1,2)
assert d_cap == Q(992,225) and d_cap < 5
assert 8+25*Q(1,2)+32*Q(1,4)+16*Q(1,8) == Q(61,2) < 32
assert 6*(1+160+192+64+256*Q(1,4)**2) == 2598 < 2600
assert 6*(96+1024*Q(1,4)) == 2112 < 2600

receipt = {
    "scope":"exact finite controls only; no universal or asymptotic certification",
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "arithmetic":"Python Fraction; integer Gram check; exact rational circle residues",
    "matrix_size":N,"common_denominator":DEN,"unitarity_exact":True,
    "delta":str(delta),"delta_cap":str(Q(1,16)),
    "ordered_pairs":PAIRS,"diagonal_pairs":2,
    "phase_choices":[[str(c),str(s)] for c,s in PHASES],
    "direct_port_pair_phase_cases":direct_cases,
    "endpoint_cases_are_frozen_and_excluded_from_actual_moment_sum":True,
    "checks":checks,"all_assertions_passed":True,
    "exclusions":["other unitary matrices and other pairs","universal phase range",
                  "stochastic trajectories and first-crossing frequency",
                  "asymptotic concentration and BGS"],
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({key:receipt[key] for key in ["scope","script_sha256","arithmetic",
                 "matrix_size","delta","direct_port_pair_phase_cases",
                 "all_assertions_passed"]},indent=2))
print("receipt:",target)
