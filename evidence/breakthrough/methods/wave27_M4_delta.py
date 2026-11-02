"""Wave 27, task 1: compute normalized twists and rigid-block shifts delta
at (108,3) mod 81. Exact integer arithmetic. No repo touch, no Lean.
"""
from collections import Counter

MOD = 81
def add(x, y): return ((x[0]+y[0]) % MOD, (x[1]+y[1]) % MOD)
def mul(x, y): return ((x[0]*y[0] + 2*x[1]*y[1]) % MOD, (x[0]*y[1] + x[1]*y[0]) % MOD)
def tr(x): return (2*x[0]) % MOD
def conj(x): return (x[0], (-x[1]) % MOD)
def inv(x):
    # x unit mod 81: x^{-1} = conj(x)/N(x); N(x) unit mod 81
    n = (x[0]*x[0] - 2*x[1]*x[1]) % MOD
    ni = pow(n, -1, MOD)
    return ((x[0]*ni) % MOD, ((-x[1]*ni) % MOD))

ALPHA = (3, 2)
pw = [(1, 0)]
for _ in range(200):
    pw.append(mul(pw[-1], ALPHA))
GAMMA = pw[4]            # (10,3)
GAMMA_INV = conj(GAMMA)  # N(gamma)=1
U27 = (3, 1)             # u = (gamma-1)/3 mod 27
# u mod 9 for T2: u^2 mod 9
U9 = (0, 1)  # u mod 3 = sqrt2; but we need u mod 9: (3,1) mod 9
U_mod9 = (3, 1)
U2_mod9 = mul((3 % 9, 1), (3 % 9, 1))  # careful: mul is mod 81; do mod 9 by hand
U2_mod9 = ((3*3 + 2*1*1) % 9, (3*1 + 1*3) % 9)
print("u^2 mod 9 =", U2_mod9)

M = 108
seqs = {}
for a in range(81):
    for b in range(81):
        A = (a, b)
        seqs[A] = [tr(mul(A, pw[i])) for i in range(M)]
groups = {}
for A, y in seqs.items():
    groups.setdefault(tuple(sorted(y)), []).append(A)

def class_multis(y):
    return [tuple(sorted(y[i] for i in range(M) if i % 4 == r)) for r in range(4)]

# per-class data for each A: for each class r, C_r, collapsed?, digits
def class_data(A):
    out = []
    for r in range(4):
        C = mul(A, pw[r])
        # collapsed iff sqrt2-coeff of C == 0 mod 3
        coll = (C[1] % 3 == 0)
        out.append((C, coll))
    return out

# precompute class data
cdata = {A: class_data(A) for A in seqs}

def rigid_info(C):
    """For collapsed C, return (c, y1, t1, t2, a0, D_a0, kappa_a0, rigid_value)
    or None if not collapsed. Uses mod-81 C. t1 = T1' mod 3, t2 = T2 mod 3.
    T1 = Tr(C*u) mod 27, u=(3,1) mod 27; T2 = Tr(C*u^2) mod 9."""
    if C[1] % 3 != 0:
        return None
    c = C[0] % 3
    # C1 = (C - c)/3 mod 3: need C mod 9
    X, Y = C[0] % 9, C[1] % 9
    # C = c + 3*C1 mod 9 with C1 in R/3; c as element of F3 lifted 0..2
    C1 = (((X - c)//3) % 3, (Y//3) % 3)
    y1 = C1[1]
    # T1 mod 27: C mod 27 times u=(3,1) mod 27, trace
    Cx, Cy = C[0] % 27, C[1] % 27
    # (Cx + Cy s)(3 + s) = 3Cx + 2Cy + (Cx + 3Cy) s ; Tr = 2*(3Cx+2Cy)
    T1 = (2*(3*Cx + 2*Cy)) % 27
    assert T1 % 3 == 0, (C, T1)
    T1p = (T1//3) % 9
    t1 = T1p % 3
    # T2 mod 9: C mod 9 times u^2=(2,6) mod 9
    # (X + Y s)(2 + 6 s) = 2X + 12Y + (6X + 2Y) s ; Tr = 2*(2X+12Y) mod 9
    T2 = (2*(2*X + 12*Y)) % 9
    t2 = T2 % 3
    if t2 == 0:
        return ("degenerate", c, y1, t1, t2)
    # a0 = 1/2 - t1/t2 mod 3 ; 1/2 mod 3 = 2
    a0 = (2 - t1*pow(t2, -1, 3)) % 3
    # Rigid value: Phi_C(j) = Tr(C) + 9*D_a + 27*b*L_a mod 81 with
    # D_a = a*T1' + a(a-1)/2*T2 mod 9 (T1' = T1p mod 9, T2 mod 9).
    # At a = a0, L_a = 0, so the value is Tr(C) + 9*D_a0 (no 27-digit:
    # the T3 term vanishes for collapsed C since Tr(C*u^3) = 0 mod 3).
    S = (a0*T1p + (a0*(a0-1)//2)*T2) % 9
    rigid = (tr(C) + 9*S) % 81
    return ("rigid", c, y1, t1, t2, a0, S, rigid)

# sanity: rigid value must be the unique mult-9 value in the class multiset
sanity_bad = 0
sanity_checked = 0
for A in list(seqs)[:500]:
    y = seqs[A]
    for r in range(4):
        C, coll = cdata[A][r]
        if not coll:
            continue
        ri = rigid_info(C)
        if ri[0] != "rigid":
            continue
        cm = Counter(y[i] for i in range(M) if i % 4 == r)
        m9 = [v for v, cnt in cm.items() if cnt == 9]
        sanity_checked += 1
        if m9 != [ri[-1]]:
            sanity_bad += 1
            if sanity_bad < 5:
                print("SANITY FAIL", A, r, "rigid", ri[-1], "mult9", m9)
print("rigid sanity checked:", sanity_checked, " bad:", sanity_bad)

# Now twists: for each pair in each group, candidates (eps, s mod 108)
# with A' == A^eps * alpha^s (mod 3). Normalize eta0=0 via gamma shifts.
# Report delta distribution for collapsed classes.
def mod3(x):
    return (x[0] % 3, x[1] % 3)

alpha_mod3 = [mod3(pw[s]) for s in range(4)]
delta_counter = Counter()
pair_with_coll = 0
pair_all_delta_zero = 0
pair_some_cand_zero = 0
pair_no_cand_zero = 0
examples_nonzero = []
for key, As in groups.items():
    for i in range(len(As)):
        A = As[i]
        if A[0] % 3 == 0 and A[1] % 3 == 0:
            continue  # divisible case: induction, skip
        # collapsed classes of A
        coll_r = [r for r in range(4) if cdata[A][r][1]]
        if not coll_r:
            continue
        for j in range(len(As)):
            if i == j:
                continue
            Aprime = As[j]
            pair_with_coll += 1
            # candidates
            cands = []
            for eps in (1, -1):
                Ae = A if eps == 1 else conj(A)
                for s in range(108):
                    if mod3(mul(Ae, pw[s])) == mod3(Aprime):
                        cands.append((eps, s))
            # for each candidate compute normalized eta and deltas
            cand_zero_flags = []
            for (eps, s) in cands:
                Ae = A if eps == 1 else conj(A)
                base = mul(Ae, pw[s])
                ratio = mul(Aprime, inv(base))
                # ratio should be 1 mod 3
                if mod3(ratio) != (1, 0):
                    continue
                # eta = (ratio - 1)/3 mod 27
                eta = (((ratio[0]-1)//3) % 27, (ratio[1]//3) % 27)
                # eta0 = eta mod 3; level-3 constraint is Tr(eta0)==0
                eta0 = (eta[0] % 3, eta[1] % 3)
                if (2*eta0[0]) % 3 != 0:
                    cand_zero_flags.append((False, eps, s, "bad-eta0"))
                    continue
                nu0 = eta0[1]  # eta0 = nu0 * sqrt2
                k = nu0  # gamma^{-k} kills eta0 (u = sqrt2 mod 3)
                # gamma^{-k} * (1+3 eta) mod 81, then (.-1)/3 mod 27
                gk = (1, 0)
                for _ in range(k):
                    gk = mul(gk, GAMMA_INV)
                one_p_eta = ((1 + 3*eta[0]) % 81, (3*eta[1]) % 81)
                prod = mul(gk, one_p_eta)
                etaN = (((prod[0]-1)//3) % 27, (prod[1]//3) % 27)
                assert etaN[0] % 3 == 0 and etaN[1] % 3 == 0
                # digits: etaN = 3*eta1 + 9*eta2 (eta1, eta2 in R/3)
                e1 = ((etaN[0]//3) % 3, (etaN[1]//3) % 3)
                e2 = (((etaN[0] - 3*e1[0])//9) % 3, ((etaN[1] - 3*e1[1])//9) % 3)
                if eps == -1:
                    # effective twist is conjugate: nu1 -> -nu1, tau2 same
                    e1 = conj(e1)
                    e2 = conj(e2)
                nu1 = e1[1]
                tau2 = (2*e2[0]) % 3
                # deltas for collapsed classes of A
                deltas = {}
                for r in coll_r:
                    C, _ = cdata[A][r]
                    ri = rigid_info(C)
                    if ri[0] != "rigid":
                        deltas[r] = "degenerate"
                        continue
                    _, c, y1, t1, t2, a0 = ri[0], ri[1], ri[2], ri[3], ri[4], ri[5]
                    delta = (nu1*(y1 + c*a0) + c*tau2) % 3
                    deltas[r] = delta
                    delta_counter[delta] += 1
                allzero = all(v == 0 for v in deltas.values())
                cand_zero_flags.append((allzero, eps, s, deltas))
            # only candidates with Tr(eta0)==0 count as level-3 alignments
            good = [f for f in cand_zero_flags if f[3] != "bad-eta0"]
            if any(f[0] is True for f in good):
                pair_some_cand_zero += 1
            else:
                pair_no_cand_zero += 1
                if len(examples_nonzero) < 5:
                    examples_nonzero.append((A, Aprime, good[:3]))
            if good and all(f[0] is True for f in good):
                pair_all_delta_zero += 1
print("pairs with collapsed A:", pair_with_coll)
print("delta distribution (over collapsed classes, all candidates):", dict(delta_counter))
print("pairs with SOME candidate all-delta-zero:", pair_some_cand_zero)
print("pairs with ALL candidates all-delta-zero:", pair_all_delta_zero)
print("pairs with NO candidate all-delta-zero:", pair_no_cand_zero)
for ex in examples_nonzero:
    print("NONZERO EX:", ex)
