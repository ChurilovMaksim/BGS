# Wave 47x, task E — exact pattern proof of the weak form for rotation
# families R1/R2 at q=577. Shared data (from wave47x_rot_maps.py):
#   A fiber-1 bases (x,y); A fiber-2 bases = L(x,y), L^2 = -I.
#   Ap fiber-1 bases (x',y'); Ap fiber-2 bases = Lp(x',y').
#   L  = ((-1,34),(-34,1));  Lp = ((1,34),(34,1))  (mod 577).
# Triple matching: T1: {x^2,y^2} = {x'^2,y'^2} (8 sign/swap patterns S);
#   T2: (L1^2+L2^2, L1^2 L2^2) = (Lp1^2+Lp2^2, Lp1^2 Lp2^2) after composing Lp with S.
# Targets (homogeneous legs automatic by per-fiber-value triple matching):
#   ROT (2,3,0,1): x^2 = y'^2 and L1^2 = Lp2^2 (other legs follow from T1).
#   PI2 (R1: (2,1,0,3); R2: (0,3,2,1)): x^2 = x'^2 and L1^2 = Lp1^2.
MOD = 577
L = ((-1 % MOD, 34), ((-34) % MOD, 1))
Lp = ((1, 34), (34, 1))
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
def is_zero_k(k): return k == (0, 0, 0, 0, 0)
def quad_at0(q, var):
    # x=0 -> cyy ; y=0 -> cxx
    return q[2] if var == 'x' else q[0]
def quart_at0(k, var):
    return k[4] if var == 'x' else k[0]
all_covered = True
for name, S, swap in patterns:
    xp, yp = lcompose(X, S), lcompose(Y, S)
    Lp1c, Lp2c = lcompose(Lp1f, S), lcompose(Lp2f, S)
    Xp2, Yp2 = sq(xp), sq(yp)
    Lp1s, Lp2s = sq(Lp1c), sq(Lp2c)
    T2sum = qsub(qadd(L1s, L2s), qadd(Lp1s, Lp2s))
    T2prod = qsub(qmul(L1s, L2s), qmul(Lp1s, Lp2s))
    # candidate legs: non-swap -> PI2 (x^2=x'^2 auto, need L1^2=Lp1^2, L2^2=Lp2^2);
    # swap -> ROT (x^2=y'^2 auto, need L1^2=Lp2^2, L2^2=Lp1^2).
    if swap == 0:
        legs = [qsub(L1s, Lp1s), qsub(L2s, Lp2s)]
        cand = "PI2"
    else:
        legs = [qsub(L1s, Lp2s), qsub(L2s, Lp1s)]
        cand = "ROT"
    legs_ok = all(is_zero_q(l) for l in legs)
    # T2sum pure-xy form? (0, c, 0) with c != 0 forces xy = 0.
    sublocus = None
    if T2sum[0] == 0 and T2sum[2] == 0 and T2sum[1] != 0:
        # on x=0: legs reduce; on y=0: legs reduce. Need candidate legs on BOTH branches.
        ok_x0 = all(quad_at0(l, 'x') == 0 for l in legs)
        ok_y0 = all(quad_at0(l, 'y') == 0 for l in legs)
        sublocus = (T2sum[1], ok_x0, ok_y0)
    verdict = None
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
