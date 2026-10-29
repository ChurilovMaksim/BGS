"""Checks for the referee-requested fixes of Line C (REPORT.md v2). Deterministic, exact where stated.
 F1  Theorem 6 constants: C_m = m! * sum_rho |W(rho)|, Hadamard threshold 4^m, informativeness threshold (C_m/2m^2)^2.
 F2  Small m: E|Tr U^1|^2 = 1, E|Tr U^2|^2 = 2 - 1/p, E|Tr U^3|^2 = 6 - 9/p + 4/p^2 (symbolic, and brute force with literal M_N).
 F3  Square-class dependence (Theorem 1 remark): brute force with F_c, c = 4^{-1} (square) and c = nu*4^{-1} (nu non-square).
 F4  c_1, c_2 vs COE (2m^3), parsed from the expansion logs; deviation and its size in the tau-scaling variable.
 F5  Independent brute-force anchor for the threshold check: m=7, p=7 (literal M_N, 7^7 paths) vs Prop. 2 exact value.
Prints PASS/FAIL per item and a final PASS line."""
import sys, os, re, math, itertools
from fractions import Fraction
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from gauss_exact import w_coeffs, set_partitions
from symbolic import expansion
from threshold_check import exact_per_prime, DATA

ALL = []
def check(name, cond):
    ALL.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name); sys.stdout.flush()

def eN(N, t): return np.exp(2j*np.pi*(t % N)/N)
def MN(N):  # literal repository kernel (bgs-recon/code/model.py)
    x = np.arange(N)[:, None]; y = np.arange(N)[None, :]
    return eN(N, (-pow(8, -1, N)*(3*x*x - 2*x*y + 3*y*y)) % N)/np.sqrt(N)
def Fc(N, c):
    x = np.arange(N)[:, None]; y = np.arange(N)[None, :]
    return eN(N, (c*x*y) % N)/np.sqrt(N)

def brute_E(M, m):
    """E_theta|Tr(D_theta M)^m|^2 = sum over occupation multisets of |sum_{x in class} K(x)|^2 (exact up to float)."""
    N = M.shape[0]
    X = np.array(list(itertools.product(range(N), repeat=m)), dtype=np.int64)
    K = np.ones(len(X), complex)
    for j in range(m): K *= M[X[:, j], X[:, (j+1) % m]]
    Xs = np.sort(X, axis=1); code = np.zeros(len(X), np.int64)
    for j in range(m): code = code*N + Xs[:, j]
    u, inv = np.unique(code, return_inverse=True); c = np.zeros(len(u), complex); np.add.at(c, inv, K)
    return float(np.sum(np.abs(c)**2))

# ---------- F1
print('F1  Theorem 6 constants')
w = w_coeffs(12)
print(' w(1..6) =', [str(w[n]) for n in range(1, 7)])
check('w(1..5) = 1, -1/2, 2/3, -11/8, 19/5', [w[n] for n in range(1, 6)] == [1, Fraction(-1, 2), Fraction(2, 3), Fraction(-11, 8), Fraction(19, 5)])
# sum_rho |W(rho)| via exponential formula: sum_m S_m t^m/m! = exp(sum_n |w(n)| t^n/n!)
def sumabsW(m):
    # recurrence for exponential generating function: S_m = sum_{k=1}^m C(m-1,k-1) |w(k)| S_{m-k}
    S = [Fraction(1)]
    for M in range(1, m+1):
        S.append(sum(math.comb(M-1, k-1)*abs(w[k])*S[M-k] for k in range(1, M+1)))
    return S[m]
# cross-check the recurrence against direct enumeration for m <= 7
for m in range(1, 8):
    direct = Fraction(0)
    for rho in set_partitions(m):
        W = Fraction(1)
        for b in range(max(rho)+1): W *= abs(w[rho.count(b)])
        direct += W
    assert direct == sumabsW(m)
check('sum|W| recurrence = direct enumeration (m <= 7)', True)
print(' m |  C_m = m! sum|W|  | 4^m        | 8^m        | (C_m/2m^2)^2 = p beyond which C_m p^-3/2 < 2m^2/p')
rows = {}
for m in range(3, 13):
    C = math.factorial(m)*sumabsW(m); thr = (C/(2*m*m))**2
    rows[m] = (C, thr)
    print(f' {m:2d} | {float(C):17.6g} | {4**m:10d} | {8**m:10.3g} | {float(thr):.3g}')
check('C_5 = 3651', rows[5][0] == 3651)
check('(C_m/2m^2)^2 > 4^m for all 5 <= m <= 12 (explicit bound uninformative at the Hadamard threshold)', all(rows[m][1] > 4**m for m in range(5, 13)))
print(' m=3,4: informative from p > (C_m/|c_1|)^2 =', float((rows[3][0]/9)**2), float((rows[4][0]/24)**2), '(below 4^m)')
check('Hadamard: prod_B 4|B| <= 4^m, since 4k <= 4^k for k >= 1 (k <= 64)', all(4*k <= 4**k for k in range(1, 65)))

# ---------- F2
print('F2  small m')
for m, want in [(1, {0: 1}), (2, {0: 2, -1: -1}), (3, {0: 6, -1: -9, -2: 4})]:
    E, _ = expansion(m)
    got = {int(e): co for (e, odd, D), co in E.items()}
    check(f'symbolic m={m}: {want}', got == {k: Fraction(v) for k, v in want.items()} and all(D == 1 and not odd for (e, odd, D) in E))
for p in (5, 7, 11, 13):
    A, B = exact_per_prime(2, p)
    b = brute_E(MN(p), 2)
    check(f'm=2 p={p}: Prop.2 exact = {A} = 2-1/p; brute(literal M_N) = {b:.15f}', A == 2 - Fraction(1, p) and B == 0 and abs(b - float(A)) < 1e-12)
for p in (5, 7, 11, 13):
    A, B = exact_per_prime(3, p)
    check(f'm=3 p={p}: Prop.2 exact = {A} = 6-9/p+4/p^2', A == 6 - Fraction(9, p) + Fraction(4, p*p) and B == 0)
check('m=1 p=7: brute = 1', abs(brute_E(MN(7), 1) - 1) < 1e-12)

# ---------- F3
print('F3  square class of the cross coefficient (p = 1 mod 4 flips the sqrt(p) terms)')
def nonsq(p): return next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
for p, m in [(13, 4), (5, 4), (7, 4), (11, 4), (13, 5)]:
    c = pow(4, -1, p); c2 = c*nonsq(p) % p
    e1 = brute_E(Fc(p, c), m); e2 = brute_E(Fc(p, c2), m); eM = brute_E(MN(p), m)
    A, B = exact_per_prime(m, p)
    s = math.sqrt(p) if p % 4 == 1 else 0.0
    ok = abs(eM - e1) < 1e-11 and abs(e1 - float(A + B*Fraction(0)) - float(B)*s) < 1e-11 and abs(e2 - (float(A) - float(B)*s)) < 1e-11
    print(f' p={p} m={m}: E(square c)={e1:.13f} E(non-square c)={e2:.13f} E(literal M_N)={eM:.13f}; exact = {A} + ({B})*sqrt(p)  [sign of sqrt term flips]')
    check(f'square-class flip p={p} m={m}', ok)
A, B = exact_per_prime(4, 13)
check('p=13 m=4: E = 14033/2197 + 8 sqrt(13)/2197 (square class); non-square gives 14033/2197 - 8 sqrt(13)/2197', A == Fraction(14033, 2197) and B == Fraction(8, 2197))

# ---------- F4
print('F4  c_1(m), c_2(m) against COE; tau-scaling size of the deviation')
def parse(path):
    out = {}
    with open(path) as f:
        cur = None
        for line in f:
            mm = re.match(r'^m=(\d+)', line)
            if mm: cur = int(mm.group(1)); out.setdefault(cur, {}); continue
            if line.startswith('decomposition'): cur = None; continue
            mm = re.match(r'\s*p\^\s*(\S+)\s+(eps\*)?\(\s*(-?\d+)/p\)\s*:\s*(\S+)', line)
            if mm and cur is not None:
                out[cur][(Fraction(mm.group(1)), bool(mm.group(2)), int(mm.group(3)))] = Fraction(mm.group(4))
    return out
L = DATA
data = parse(os.path.join(L, 'symbolic_m1_7.log'))
for m in (8, 9, 10): data.update(parse(os.path.join(L, f'engine_m{m}.log')))
for m in (11, 12): data.update(parse(os.path.join(L, f'engine_m{m}_def2.log')))
# consistency: engine logs for m=6,7 equal python symbolic for those orders
for m in (6, 7):
    eng = parse(os.path.join(L, f'engine_m{m}.log'))[m]
    check(f'engine_m{m}.log == symbolic_m1_7.log (all orders) for m={m}', eng == data[m])
print(' m | c1   | COE c1 | c2 (trivial char) + characters | COE 2m^3 | delta = c2-2m^3 | delta/m^2 | c2/m^3')
dev = []
for m in range(3, 13):
    T = data[m]
    c1 = T.get((Fraction(-1), False, 1), 0)
    c2 = T.get((Fraction(-2), False, 1), 0)
    ch = {D: v for (e, o, D), v in T.items() if e == -2 and D != 1}
    c32 = sum(v for (e, o, D), v in T.items() if e == Fraction(-3, 2))
    assert c32 == 0 and not any(e == Fraction(-3, 2) for (e, o, D) in T)
    d = c2 - 2*m**3
    if d != 0 or ch: dev.append(m)
    print(f' {m:2d} | {str(c1):5s}| {-2*m*m:6d} | {str(c2):6s} {ch if ch else ""} | {2*m**3:5d} | {str(d):6s} | {float(d)/m**2:+.3f} | {float(c2)/m**3:.4f}')
    if m >= 5: check(f'c1({m}) = -2m^2', c1 == -2*m*m)
check('c1(3) = -9, c1(4) = -24', data[3][(Fraction(-1), False, 1)] == -9 and data[4][(Fraction(-1), False, 1)] == -24)
check('no p^-3/2 term for m <= 12', True)
check('c2 != 2m^3 exactly at m in {5,6,8,9,12} among 5..12 (m=3,4 also differ)', [m for m in dev if m >= 5] == [5, 6, 8, 9, 12])
check('c2(12) = 3480, 2*12^3 = 3456', data[12][(Fraction(-2), False, 1)] == 3480 and 2*12**3 == 3456)
print(' NOTE: at m=5, (5/p)=-1 gives c2-2m^3 = -85 = -3.4 m^2, so the v1 bound "<= 3m^2" was false; corrected to 3.4 m^2')
check('|c2 - 2m^3| <= 3.4m^2 for 5 <= m <= 12 (incl. the (5/p) term at m=5); <= 0.7m^2 for m >= 8; <= 2m for m >= 10', all(abs(data[m][(Fraction(-2), False, 1)] - 2*m**3) <= 2*m for m in range(10, 13)) and all(abs(data[m][(Fraction(-2), False, 1)] - 2*m**3) <= 0.7*m*m for m in range(8, 13)) and all(abs(data[m][(Fraction(-2), False, 1)] - 2*m**3) + sum(abs(v) for (e, o, D), v in data[m].items() if e == -2 and D != 1) <= 3.4*m*m for m in range(5, 13)))
print(' In K(tau) = E/p with tau = m/p, the deviation contributes delta(m)/p^3 = (delta/m^2) * tau^2 / p,')
print(' i.e. O(tau^2/p) -> 0 at fixed tau IF |delta| = O(m^2) persists (observed only for m <= 12; not proved).')

# ---------- F5
print('F5  brute-force anchor: m=7, p=7, literal M_N (823543 paths)')
A, B = exact_per_prime(7, 7)
b = brute_E(MN(7), 7)
check(f'm=7 p=7 brute = {b:.13f} vs Prop.2 exact {A} = {float(A):.13f}', abs(b - float(A)) < 1e-10 and B == 0)

print('PASS' if all(ALL) else 'FAIL', f'({sum(ALL)}/{len(ALL)} checks)')
