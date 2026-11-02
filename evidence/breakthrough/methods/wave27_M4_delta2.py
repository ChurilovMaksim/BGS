"""Wave 27, task 1 (v2): rigorous delta check at (108,3).
For each pair in a group, keep only (eps,s) candidates whose pi matches
class multisets mod 27; for those, record normalized eta digits
(a1, nu1, tau2) and rigid shifts delta. Exact arithmetic.
"""
from collections import Counter

MOD = 81
def mul(x, y): return ((x[0]*y[0] + 2*x[1]*y[1]) % MOD, (x[0]*y[1] + x[1]*y[0]) % MOD)
def tr(x): return (2*x[0]) % MOD
def conj(x): return (x[0], (-x[1]) % MOD)
def inv(x):
    n = (x[0]*x[0] - 2*x[1]*x[1]) % MOD
    ni = pow(n, -1, MOD)
    return ((x[0]*ni) % MOD, ((-x[1]*ni) % MOD))
def mod3(x): return (x[0] % 3, x[1] % 3)

ALPHA = (3, 2)
pw = [(1, 0)]
for _ in range(200):
    pw.append(mul(pw[-1], ALPHA))
GAMMA_INV = conj(pw[4])

M = 108
seqs = {}
for a in range(81):
    for b in range(81):
        A = (a, b)
        seqs[A] = [tr(mul(A, pw[i])) for i in range(M)]
groups = {}
for A, y in seqs.items():
    groups.setdefault(tuple(sorted(y)), []).append(A)

def class_multis_mod(y, m):
    return [tuple(sorted((y[i] % m) for i in range(M) if i % 4 == r)) for r in range(4)]

cm27 = {A: class_multis_mod(seqs[A], 27) for A in seqs}

def class_data(A):
    out = []
    for r in range(4):
        C = mul(A, pw[r])
        out.append((C, C[1] % 3 == 0))
    return out
cdata = {A: class_data(A) for A in seqs}

def rigid_info(C):
    if C[1] % 3 != 0:
        return None
    c = C[0] % 3
    X, Y = C[0] % 9, C[1] % 9
    C1 = (((X - c)//3) % 3, (Y//3) % 3)
    y1 = C1[1]
    Cx, Cy = C[0] % 27, C[1] % 27
    T1 = (2*(3*Cx + 2*Cy)) % 27
    T1p = (T1//3) % 9
    t1 = T1p % 3
    T2 = (2*(2*X + 12*Y)) % 9
    t2 = T2 % 3
    if t2 == 0:
        return ("degenerate", c, y1, t1, t2)
    a0 = (2 - t1*pow(t2, -1, 3)) % 3
    S = (a0*T1p + (a0*(a0-1)//2)*T2) % 9
    rigid = (tr(C) + 9*S) % 81
    return ("rigid", c, y1, t1, t2, a0, S, rigid)

n_pair = 0
n_valid_cand = 0
n_pair_with_valid = 0
a1_dist = Counter()
nu1_tau2_dist = Counter()
delta_dist = Counter()
delta_nonzero_examples = []
rigid_match_bad = 0
rigid_match_checked = 0
for key, As in groups.items():
    for i in range(len(As)):
        A = As[i]
        if A[0] % 3 == 0 and A[1] % 3 == 0:
            continue
        coll_r = [r for r in range(4) if cdata[A][r][1]]
        if not coll_r:
            continue
        for j in range(len(As)):
            if i == j:
                continue
            Aprime = As[j]
            n_pair += 1
            pair_has_valid = False
            for eps in (1, -1):
                Ae = A if eps == 1 else conj(A)
                for s in range(108):
                    if mod3(mul(Ae, pw[s])) != mod3(Aprime):
                        continue
                    # pi: class r' of A' matches class pi(r') of A
                    if eps == 1:
                        pi = [ (r + s) % 4 for r in range(4) ]
                    else:
                        pi = [ (-r - s) % 4 for r in range(4) ]
                    # level-3 per-class check mod 27
                    ok27 = all(cm27[Aprime][r] == cm27[A][pi[r]] for r in range(4))
                    if not ok27:
                        continue
                    pair_has_valid = True
                    n_valid_cand += 1
                    base = mul(Ae, pw[s])
                    ratio = mul(Aprime, inv(base))
                    eta = (((ratio[0]-1)//3) % 27, (ratio[1]//3) % 27)
                    eta0 = (eta[0] % 3, eta[1] % 3)
                    if (2*eta0[0]) % 3 != 0:
                        print("UNEXPECTED Tr(eta0)!=0", A, Aprime, eps, s)
                        continue
                    k = eta0[1]
                    gk = (1, 0)
                    for _ in range(k):
                        gk = mul(gk, GAMMA_INV)
                    one_p_eta = ((1 + 3*eta[0]) % 81, (3*eta[1]) % 81)
                    prod = mul(gk, one_p_eta)
                    etaN = (((prod[0]-1)//3) % 27, (prod[1]//3) % 27)
                    e1 = ((etaN[0]//3) % 3, (etaN[1]//3) % 3)
                    e2 = (((etaN[0] - 3*e1[0])//9) % 3, ((etaN[1] - 3*e1[1])//9) % 3)
                    if eps == -1:
                        e1 = conj(e1); e2 = conj(e2)
                    a1 = e1[0]; nu1 = e1[1]; tau2 = (2*e2[0]) % 3
                    a1_dist[a1] += 1
                    nu1_tau2_dist[(nu1, tau2)] += 1
                    # deltas + rigid matching under pi
                    for r in coll_r:
                        C, _ = cdata[A][r]
                        ri = rigid_info(C)
                        if ri[0] != "rigid":
                            continue
                        _, c, y1, t1, t2, a0, S, rigid = ri
                        delta = (nu1*(y1 + c*a0) + c*tau2) % 3
                        delta_dist[delta] += 1
                        if delta != 0 and len(delta_nonzero_examples) < 5:
                            delta_nonzero_examples.append((A, Aprime, eps, s, r, delta, (a1, nu1, tau2)))
                        # rigid value of A' in class pi^{-1}(r): class r' with pi(r')=r
                        rp = [x for x in range(4) if pi[x] == r][0]
                        Cp, _ = cdata[Aprime][rp]
                        rip = rigid_info(Cp)
                        rigid_match_checked += 1
                        if rip[0] != "rigid" or rip[-1] != (rigid + 27*delta) % 81:
                            rigid_match_bad += 1
            if pair_has_valid:
                n_pair_with_valid += 1
print("pairs (unit A, coll):", n_pair)
print("pairs with >=1 valid (mod-27 pi) candidate:", n_pair_with_valid)
print("valid candidates:", n_valid_cand)
print("a1 (real part of eta1) distribution:", dict(a1_dist))
print("(nu1, tau2) distribution:", dict(nu1_tau2_dist))
print("delta distribution (valid candidates only):", dict(delta_dist))
print("rigid matching checked:", rigid_match_checked, " bad:", rigid_match_bad)
print("nonzero delta examples:", delta_nonzero_examples)
