# Wave 47x, task E (follow-up) — exact pattern proof for the third rotation
# family R3: A=((2048,512),(0,4)) vs Ap=((0,512),(1,5)),
# pis = {PI1=(1,2,3,0), PI2=(3,2,1,0)}. Convention (Theorem B):
# joints under pi  <=>  Ap class-r = A class-pi[r] for all r.
# A mixed bases (x,y)=(b5,b7) [M1, value (0,2)], M2 bases = L(x,y) with
#   L  = ((1,543),(34,576));
# Ap mixed bases (x',y')=(b'0,b'2) [F1', value (0,2)], F2' bases = Lp(x',y')
#   Lp = ((576,34),(543,1)).
# Triple: T1: {x^2,y^2}={x'^2,y'^2} (8 patterns); T2: sum/prod of squares.
# PI1 legs (non-swap: first legs auto): Lp1^2=L1^2, Lp2^2=L2^2.
# PI2 legs (swap: first legs auto): Lp2^2=L1^2, Lp1^2=L2^2.
# Homogeneous legs automatic: PI1/PI2 in pis + fiber-value triple matching
# (homogeneous fibers single-class on both sides).
MOD = 577
L = ((1, 543), (34, 576))
Lp = ((576, 34), (543, 1))
def lcompose(f, S):
    return ((f[0]*S[0][0]+f[1]*S[1][0]) % MOD, (f[0]*S[0][1]+f[1]*S[1][1]) % MOD)
def sq(f):
    return ((f[0]*f[0]) % MOD, (2*f[0]*f[1]) % MOD, (f[1]*f[1]) % MOD)
def qadd(f, g): return tuple((a+b) % MOD for a, b in zip(f, g))
def qsub(f, g): return tuple((a-b) % MOD for a, b in zip(f, g))
def qmul(f, g):
    a, b, c = f; d, e, h = g
    return ((a*d) % MOD, (a*e+b*d) % MOD, (a*h+b*e+c*d) % MOD,
            (b*h+c*e) % MOD, (c*h) % MOD)
X, Y = (1, 0), (0, 1)
X2, Y2 = sq(X), sq(Y)
L1f, L2f = L[0], L[1]
L1s, L2s = sq(L1f), sq(L2f)
Lp1f, Lp2f = Lp[0], Lp[1]
print("L1^2 =", L1s, " L2^2 =", L2s, " sum =", qadd(L1s, L2s), " prod =", qmul(L1s, L2s))
print("Lp1^2 =", sq(Lp1f), " Lp2^2 =", sq(Lp2f))
patterns = []
for swap in (0, 1):
    for s1 in (1, MOD-1):
        for s2 in (1, MOD-1):
            if swap == 0:
                S = ((s1, 0), (0, s2)); name = f"(x',y')=({'+' if s1==1 else '-'}x,{'+' if s2==1 else '-'}y)"
            else:
                S = ((0, s1), (s2, 0)); name = f"(x',y')=({'+' if s1==1 else '-'}y,{'+' if s2==1 else '-'}x)"
            patterns.append((name, S, swap))
def is_zero_q(q): return q == (0, 0, 0)
def quad_at0(q, var):
    return q[2] if var == 'x' else q[0]
all_covered = True
for name, S, swap in patterns:
    xp, yp = lcompose(X, S), lcompose(Y, S)
    Lp1c, Lp2c = lcompose(Lp1f, S), lcompose(Lp2f, S)
    Lp1s, Lp2s = sq(Lp1c), sq(Lp2c)
    T2sum = qsub(qadd(L1s, L2s), qadd(Lp1s, Lp2s))
    T2prod = qsub(qmul(L1s, L2s), qmul(Lp1s, Lp2s))
    if swap == 0:
        legs = [qsub(Lp1s, L1s), qsub(Lp2s, L2s)]
        cand = "PI1"
    else:
        legs = [qsub(Lp2s, L1s), qsub(Lp1s, L2s)]
        cand = "PI2"
    legs_ok = all(is_zero_q(l) for l in legs)
    sublocus = None
    if T2sum[0] == 0 and T2sum[2] == 0 and T2sum[1] != 0:
        ok_x0 = all(quad_at0(l, 'x') == 0 for l in legs)
        ok_y0 = all(quad_at0(l, 'y') == 0 for l in legs)
        sublocus = (T2sum[1], ok_x0, ok_y0)
    if legs_ok:
        verdict = f"{cand} identically"
    elif sublocus and sublocus[1] and sublocus[2]:
        verdict = f"T2sum forces xy=0 (coeff {sublocus[0]}); {cand} on both subloci"
    elif sublocus:
        verdict = f"PARTIAL: T2sum forces xy=0, subloci x0:{sublocus[1]} y0:{sublocus[2]}"
    else:
        verdict = "NOT COVERED"
    if "NOT COVERED" in verdict or "PARTIAL" in verdict: all_covered = False
    print(f"{name} [{cand}]: T2sum={T2sum} T2prod={T2prod} legs={legs} -> {verdict}")
print("ALL PATTERNS COVERED:", all_covered)
