"""
INDEPENDENT VERIFICATION, part 2 — exact identities (machine precision).
  E1  Sum over ALL multiplets:  sum_lam Tr(V_lam^r) = Tr(Vbar^r) = N*a_r
      (exact, because sum_lam P_lam = I).  Machine-zero expected.
  E2  Unimodularity |Tr(T(v) U^J)| = 1 for J not= 0 mod K   [fresh code]
  E3  Cancellation: Tr(P_lam T(u)) = delta_{u,0}*(N/K) + E, |E| < 1
      with the EXACT constant N/K (not m).
  E4  Tight frame: sum_orbits (|O|/K) M_O x* M_O = (N/K) I - (1/K) trace-dir
  E5  NEW multiplicity lemma: m_j - N/K = (1/K) sum_{k=1}^{K-1} unit-phase,
      hence |m_j - N/K| <= (K-1)/K and m_j in {floor(N/K), ceil(N/K)}.
      Verified two ways: (a) direct eigenspace dims vs the DFT formula,
      (b) the bound itself across many primes and several A.
Run: py -3 indep_check2.py
"""
import numpy as np, math, json, os, sys
import scipy.linalg as sla

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
OUT = {}
FAILS = []


def ok(tag, cond, detail):
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}: {detail}")
    if not cond:
        FAILS.append(tag)


def build_U(A, N):
    a, b, c, d = [v % N for v in A]
    iota = pow((2*c) % N, -1, N)
    xs = np.arange(N)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    w = np.exp(2j*np.pi/N)
    return (w ** ((iota*(d*X*X - 2*X*Y + a*Y*Y)) % N).astype(float)) / math.sqrt(N)


def weyl_T(N):
    inv2 = pow(2, -1, N)
    w = np.exp(2j*np.pi/N)
    def T(n1, n2):
        idx = np.arange(N)
        tgt = (idx-n1) % N
        M = np.zeros((N, N), dtype=complex)
        M[idx, tgt] = np.exp(2j*np.pi*((inv2*n1*n2 + n2*tgt) % N)/N)
        return M
    return T


def ord_pm(A, N):
    a, b, c, d = [v % N for v in A]
    P = (1, 0, 0, 1)
    for k in range(1, 2*N+3):
        P = ((P[0]*a+P[1]*c) % N, (P[0]*b+P[1]*d) % N,
             (P[2]*a+P[3]*c) % N, (P[2]*b+P[3]*d) % N)
        if P == (1, 0, 0, 1): return k, +1
        if P == (N-1, 0, 0, N-1): return k, -1
    return -1, 0


# ======================================================================
# E5a: multiplicity lemma — DFT formula vs actual dims, machine precision
# ======================================================================
rows = []
for name, A in (("Arnold", [2, 1, 1, 1]), ("tr4", [3, 1, 2, 1]),
                ("tr8", [7, 3, 2, 1])):
    for N in (199, 401, 1009):
        k, sg = ord_pm(A, N)
        if k < 0 or N % 2 == 0:
            continue
        K = k if sg > 0 else 2*k
        if K > 400:            # keep eigensolver cheap
            continue
        U = build_U(A, N)
        ev, W = np.linalg.eig(U)
        # group eigenphases on the K-grid
        lam0 = np.angle(ev)*K/(2*np.pi)
        cnt = np.zeros(K, dtype=int)
        for v_ in lam0:
            j = int(round(v_)) % K
            cnt[j] += 1
        # power sums p_k = Tr U^k, DFT inversion
        chi = np.trace(np.linalg.matrix_power(U, K))/N
        chi_root = chi**(1.0/K)
        pw = np.array([np.trace(np.linalg.matrix_power(U, kk)) for kk in range(K)])
        g = np.array([pw[kk]/(chi_root**kk) for kk in range(K)])
        m_dft = np.array([abs(sum(g[kk]*np.exp(-2j*np.pi*jj*kk/K)
                                   for kk in range(K)))/K for jj in range(K)])
        dev = float(np.max(abs(m_dft - cnt)))
        bound = (K-1)/K
        maxdev_NK = float(np.max(abs(cnt - N/K)))
        rows.append({"A": name, "N": N, "K": K, "dft_vs_dims": dev,
                     "bound": bound, "max_abs_m_NK": maxdev_NK})
        print(f"  mult {name} N={N}: K={K}, max|DFT-dims|={dev:.2e} "
              f"(must be ~0); max|m-N/K|={maxdev_NK:.3f} <= (K-1)/K={bound:.3f}: "
              f"{maxdev_NK <= bound + 1e-9}")
OUT["multiplicity_lemma"] = rows
ok("E5 MULTIPLICITY LEMMA: DFT formula == dims; |m-N/K| <= (K-1)/K",
   all(r["dft_vs_dims"] < 1e-6 for r in rows) and
   all(r["max_abs_m_NK"] <= r["bound"] + 1e-9 for r in rows),
   f"{len(rows)} (A,N) cases")

# broad sweep of the bound only (cheap: eigenvalues via matrix powers? use eig)
sweep = []
for N in (353, 701, 1601, 2351, 3407, 4001):
    k, sg = ord_pm([2, 1, 1, 1], N)
    if k < 0: continue
    K = k if sg > 0 else 2*k
    U = build_U([2, 1, 1, 1], N)
    ev = np.angle(np.linalg.eigvals(U))*K/(2*np.pi)
    cnt = np.zeros(K, dtype=int)
    for v_ in ev:
        cnt[int(round(v_)) % K] += 1
    md = float(np.max(abs(cnt - N/K)))
    sweep.append({"N": N, "K": K, "max_abs_m_NK": md, "ok": md <= (K-1)/K + 1e-9})
    print(f"  sweep N={N}: K={K}, max|m-N/K|={md:.3f}, floor/ceil only: "
          f"{all(x in (int(N//K), int(math.ceil(N/K))) for x in cnt)}")
OUT["mult_sweep"] = sweep
ok("E5b sweep: dims are exactly floor/ceil(N/K)", all(r["ok"] for r in sweep),
   f"{len(sweep)} primes")

# ======================================================================
# E1: exact pooled moment identity at one prime, r=1..4
# ======================================================================
N = 199
A = [2, 1, 1, 1]
k, sg = ord_pm(A, N); K = k if sg > 0 else 2*k
U = build_U(A, N); Ud = U.conj().T
T = weyl_T(N)
rng = np.random.default_rng(777)
terms = {}
for n1 in range(-2, 3):
    for n2 in range(-2, 3):
        if (n1, n2) == (0, 0) or (n1, n2) > (-n1, -n2): continue
        terms[(n1, n2)] = (rng.normal()+1j*rng.normal())/math.sqrt(2)
V = np.zeros((N, N), dtype=complex)
for (n1, n2), cc in terms.items():
    V += cc*T(n1 % N, n2 % N) + np.conj(cc)*T((-n1) % N, (-n2) % N)
V = 0.5*(V+V.conj().T)
Vbar = np.zeros_like(V); Xv = V.copy()
for j in range(K):
    Vbar += Xv; Xv = U@Xv@Ud
Vbar /= K
UK = np.linalg.matrix_power(U, K); chi = np.trace(UK)/N
lams = [chi**(1.0/K)*np.exp(2j*np.pi*j/K) for j in range(K)]
Ps = []
for lam in lams:
    P = np.zeros_like(U); Uj = np.eye(N, dtype=complex)
    for j in range(K):
        P += (lam**(-j))*Uj; Uj = U@Uj
    P /= K
    sv = np.linalg.svd(P, compute_uv=False)
    assert abs(np.sum(sv > 0.5) - round(np.sum(sv > 0.5))) < 1e-9
    Ps.append((lam, P))
dims = [int(np.sum(np.linalg.svd(P, compute_uv=False) > 0.5)) for _, P in Ps]
print(f"  N={N}: K={K} multiplets, dims sum = {sum(dims)} (should be {N})")

# a_r := T(0)-Weyl coefficient of Vbar^r = N^{-1} Tr Vbar^r
pooled = []
res_max = 0.0
Vbar_pow = np.eye(N, dtype=complex)
for r in range(1, 5):
    Vbar_pow = Vbar_pow@Vbar
    ar = np.trace(Vbar_pow).real/N          # exact coefficient of T(0)
    s = 0.0+0j
    for lam, P in Ps:
        s += np.trace(Vbar_pow@P)           # = Tr V_lam^r by Birkhoff reduction
    resid = abs(s - N*ar)/max(1.0, N*abs(ar))
    res_max = max(res_max, resid)
    print(f"  E1 r={r}: a_r={ar:.6f}, sum_lam Tr V_lam^r={s.real:.6f}"
          f"{s.imag:+.1e}i, N*a_r={N*ar:.6f}, rel resid={resid:.1e}")
    pooled.append({"r": r, "a_r": ar, "rel_resid": resid})
OUT["pooled_moments"] = {"N": N, "K": K, "rows": pooled}
ok("E1 POOLED MOMENTS: sum_lam Tr V_lam^r = N*a_r exactly", res_max < 1e-9,
   f"max rel resid {res_max:.1e}")

# per-multiplet: Tr V_lam^r = (N/K)a_r + O(C^r); verify bound with honest C
C = 2*sum(abs(v_) for v_ in terms.values())
worst_ratio = 0.0
Vbar2 = Vbar@Vbar
a2 = np.trace(Vbar2).real/N
per = []
for (lam, P), mm in zip(Ps, dims):
    t2 = np.trace(Vbar2@P).real
    dev = abs(t2 - (N/K)*a2)
    worst_ratio = max(worst_ratio, dev/C**2)
    per.append({"lam": i if False else None, "m": mm, "Tr2": t2,
                "dev_over_C2": dev/C**2})
OUT["per_multiplet"] = {"worst_dev_over_bound": worst_ratio}
ok("E1b per-multiplet bound |Tr V^2 - (N/K)a2| <= C^2",
   worst_ratio < 1.0, f"worst dev/bound = {worst_ratio:.3f}")

# ======================================================================
# E2/E3: unimodularity + cancellation with EXACT constant N/K
# ======================================================================
worst_uni = 0.0
for J in range(1, min(K, 8)):
    UJ = np.linalg.matrix_power(U, J)
    for v1, v2 in ((0, 0), (0, 1), (1, 0), (5, 7), (13, 2)):
        worst_uni = max(worst_uni, abs(abs(np.trace(T(v1 % N, v2 % N)@UJ))-1.0))
OUT["unimod"] = worst_uni
ok("E2 UNIMODULARITY |Tr T(v)U^J|=1 (incl v=0)", worst_uni < 1e-11,
   f"max dev {worst_uni:.1e}")

# cancellation: Tr(P_lam T(u)) vs delta_{u,0}(N/K)
worst_zero, worst_nonzero = 0.0, 0.0
lam, P = Ps[3]
us = [(0, 0)] + [(n1, n2) for n1 in range(-3, 4) for n2 in range(-3, 4)
                 if (n1, n2) != (0, 0)][::17][:30]
for u in us:
    tr = np.trace(P@T(u[0] % N, u[1] % N))
    if u == (0, 0):
        worst_zero = max(worst_zero, abs(tr - N/K))
    else:
        worst_nonzero = max(worst_nonzero, abs(tr))
OUT["cancel"] = {"dev_zero": worst_zero, "max_nonzero": worst_nonzero}
ok("E3 CANCELLATION |Tr(Plam T(u)) - (N/K)d_{u0}| < 1 for ALL u",
   worst_zero <= (K-1)/K + 1e-9 and worst_nonzero < 1.0,
   f"u=0: |m-(N/K)|={worst_zero:.3f} <= (K-1)/K={(K-1)/K:.3f}; "
   f"u!=0: max|Tr|={worst_nonzero:.3f} < 1")

# ======================================================================
# E4: tight frame with constant N/K
# ======================================================================
Nf = 101
Af = [2, 1, 1, 1]
kf, sgf = ord_pm(Af, Nf); Kf = kf if sgf > 0 else 2*kf
Uf = build_U(Af, Nf)
Tf = weyl_T(Nf)
UKf = np.linalg.matrix_power(Uf, Kf); chif = np.trace(UKf)/Nf
lam = chif**(1.0/Kf)*np.exp(2j*np.pi*1/Kf)
P = np.zeros_like(Uf); Uj = np.eye(Nf, dtype=complex)
for j in range(Kf):
    P += (lam**(-j))*Uj; Uj = Uf@Uj
P /= Kf
sv = np.linalg.svd(P, compute_uv=False)
mm = int(np.sum(sv > 0.5))
Q, _ = np.linalg.qr(P@(np.random.default_rng(3).normal(size=(Nf, mm))+1j*
                       np.random.default_rng(3).normal(size=(Nf, mm))))
B = Q[:, :mm]
assert np.linalg.norm(Uf@B-lam*B)/math.sqrt(mm) < 1e-9

def comp_M(u):
    Tu = Tf(u[0], u[1])
    full = P@Tu@P
    return B.conj().T@full@B

# enumerate orbits of A acting on nonzero frequency vectors
seen = set()
frame_lhs = np.zeros((mm, mm, mm, mm), dtype=complex)
tot_weight = 0.0
for x in range(Nf):
    for y in range(Nf):
        if x == 0 and y == 0: continue
        if (x, y) in seen: continue
        orb = []
        cur = (x, y)
        while cur not in seen and len(orb) <= Kf+2:
            seen.add(cur); orb.append(cur)
            cur = ((Af[0]*cur[0]+Af[1]*cur[1]) % Nf,
                   (Af[2]*cur[0]+Af[3]*cur[1]) % Nf)
        Mo = comp_M(orb[0])
        w = len(orb)/Kf
        frame_lhs += w*np.einsum('ab,cd->abcd', Mo, Mo.conj())
        tot_weight += w
I = np.eye(mm)
RHS = (Nf/Kf)*np.einsum('ac,bd->abcd', I, I) - (1.0/Kf)*np.einsum('ab,cd->abcd', I, I)
err = np.linalg.norm(frame_lhs-RHS)/np.linalg.norm(RHS)
OUT["tight_frame"] = {"N": Nf, "K": Kf, "m": mm, "rel_err": err}
ok("E4 TIGHT FRAME sum_O (|O|/K) MxM* = (N/K) Id - (1/K) swap",
   err < 1e-10, f"m={mm}, rel err {err:.1e}")

json.dump(OUT, open(os.path.join(ART, "indep_check2.json"), "w"), indent=1)
print("\nsaved artifacts/indep_check2.json")
if FAILS:
    print("FAILURES:", FAILS); sys.exit(1)
print("ALL PART-2 CHECKS PASS")
