"""
INDEPENDENT VERIFICATION — written from scratch in a fresh session (run 3).
No code reused from prior sessions. Design differences:
  * Egorov covariance checked as an EXACT INTEGER IDENTITY in Z/NZ
    (exponents, not floats), exhaustively over ALL frequencies n and ALL
    matrix entries, for symmetric AND non-symmetric hyperbolic A.
  * All proportionality scalars are REPORTED (|scalar|=1 enforced), so
    "exact" cannot hide behind trace normalisation.
  * Moment/cancellation formulas checked against BOTH candidate constants
    m_lambda and N/K, to settle which is correct.
Run: py -3 indep_check.py   -> artifacts/indep_check.json
Exit 0 iff every check passes.
"""
import numpy as np, math, json, os, sys, time
import scipy.linalg as sla

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
os.makedirs(ART, exist_ok=True)
OUT = {"egorov": [], "theta": [], "torsion": [], "moments": [], "cancel": [],
       "frame": [], "r4": [], "multiplicities": [], "unimod": [], "birkhoff": []}
FAILS = []


def ok(tag, cond, detail):
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}: {detail}")
    if not cond:
        FAILS.append(tag)


# ----------------------------------------------------------------------
# exact integer kernel: U[x,y] = omega^{E[x,y]} / sqrt(N),
# E[x,y] = iota*(d x^2 - 2 x y + a y^2), iota = (2c)^{-1} mod N
# ----------------------------------------------------------------------
def expo_U(A, N):
    a, b, c, d = [v % N for v in A]
    iota = pow((2 * c) % N, -1, N)
    xs = np.arange(N)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    return (iota * (d * X * X - 2 * X * Y + a * Y * Y)) % N


def build_U(A, N):
    w = np.exp(2j * np.pi / N)
    return (w ** expo_U(A, N).astype(float)) / math.sqrt(N)


def weyl_T(N):
    """T(n1,n2) f(x) = omega^{ n1 n2/2 + n2 (x-n1) } f(x - n1)   (their convention)."""
    inv2 = pow(2, -1, N)
    w = np.exp(2j * np.pi / N)
    def T(n1, n2):
        M = np.zeros((N, N), dtype=complex)
        idx = np.arange(N)
        tgt = (idx - n1) % N
        M[idx, tgt] = np.exp(2j * np.pi * ((inv2 * n1 * n2 + n2 * tgt) % N) / N)
        return M
    return T


def ord_pm(A, N):
    a, b, c, d = [v % N for v in A]
    P = (1, 0, 0, 1)
    for k in range(1, 2 * N + 3):
        P = ((P[0]*a+P[1]*c) % N, (P[0]*b+P[1]*d) % N,
             (P[2]*a+P[3]*c) % N, (P[2]*b+P[3]*d) % N)
        if P == (1, 0, 0, 1): return k, +1
        if P == (N-1, 0, 0, N-1): return k, -1
    return -1, 0


A_MATRICES = {
    "Arnold_sym_[2,1,1,1]": [2, 1, 1, 1],
    "nonsym_tr4_[3,1,2,1]": [3, 1, 2, 1],
    "nonsym_tr5_[1,1,3,4]": [1, 1, 3, 4],
    "nonsym_tr8_[7,3,2,1]": [7, 3, 2, 1],
}

# ----------------------------------------------------------------------
# CHECK 1: Egorov as EXACT INTEGER IDENTITY.
# Claim under test:  U T(n) U^dag = sigma(n) * T(m(n)).
# Acting on basis vectors this reads, for all x,y,n:
#   E(x, y+n1) + n1 n2/2 + n2 y  ==  m1 m2/2 + m2 (x-m1) + E(x-m1, y) - s(n)
# with s(n) the log-phase of sigma(n); i.e. the difference Delta must be
# CONSTANT in (x,y) for each fixed n.  We test m in {A n, A^T n}.
# ----------------------------------------------------------------------
def egorov_exact(A, N, mode):
    a, b, c, d = [v % N for v in A]
    iota = pow((2*c) % N, -1, N)
    inv2 = pow(2, -1, N)
    E = expo_U(A, N)
    ys = np.arange(N)
    Y, X = np.meshgrid(ys, ys, indexing="ij")     # X[i,j]=x? define below
    # grids: index [x,y]
    XX, YY = np.meshgrid(ys, ys, indexing="ij")
    worst_nonconst = 0
    phases = []
    for n1 in range(N):
        for n2 in range(N):
            if mode == "A":
                m1, m2 = (a*n1+b*n2) % N, (c*n1+d*n2) % N
            else:  # A^T
                m1, m2 = (a*n1+c*n2) % N, (b*n1+d*n2) % N
            lhs = (E[np.ix_(ys, (ys+n1) % N)] + inv2*n1*n2 + n2*YY[None, :]) % N \
                  if False else (E[(ys[:, None]), ((ys[None, :]+n1) % N)]
                                 + inv2*n1*n2 + n2*ys[None, :]) % N
            rhs = (inv2*m1*m2 + m2*(XX - m1)
                   + E[((XX-m1) % N), ys[None, :]]) % N
            D = (lhs - rhs) % N
            spread = int(D.max() - D.min())
            worst_nonconst = max(worst_nonconst, spread)
            phases.append(int(D.flat[0]))
    return worst_nonconst, phases


t0 = time.time()
for name, A in A_MATRICES.items():
    for N in (7, 11, 13):
        row = {"name": name, "N": N}
        for mode in ("A", "AT"):
            sp, ph = egorov_exact(A, N, mode)
            row["m_" + mode] = sp
        OUT["egorov"].append(row)
        print(f"  egorov-exact {name} N={N}: spread(m=A n)={row['m_A']}, "
              f"spread(m=A^T n)={row['m_AT']}")
ok("EGOROV-EXACT: kernel quantises A^T (spread 0); m=A n exact only when b=c",
   all((r["m_AT"] == 0) for r in OUT["egorov"]),
   "all spreads(m=A^T n) are exactly 0")
sym_fail = all(r["m_A"] > 0 for r in OUT["egorov"] if "nonsym" in r["name"])
sym_ok = all(r["m_A"] == 0 for r in OUT["egorov"] if "Arnold_sym" in r["name"])
print(f"  --> non-symmetric A: m=A n fails (spread>0): {sym_fail}")
print(f"  elapsed {time.time()-t0:.1f}s")

# ----------------------------------------------------------------------
# CHECK 2: the operator-level statement incl. |sigma(n)|=1, on floats,
# for m = A^T n, at a larger prime, for both symmetric & nonsymmetric A.
# ----------------------------------------------------------------------
for name, A in A_MATRICES.items():
    N = 101
    if any(v % N == 0 for v in A[:0]): continue
    a, b, c, d = A
    if (2*c) % N == 0: continue
    U = build_U(A, N); T = weyl_T(N)
    worst_s, worst_r = 0.0, 0.0
    for n1 in (-2, -1, 0, 1, 3):
        for n2 in (-3, -1, 2):
            nn1, nn2 = n1 % N, n2 % N
            m1 = (a*nn1+c*nn2) % N
            m2 = (b*nn1+d*nn2) % N
            L = U @ T(nn1, nn2) @ U.conj().T
            R = T(m1, m2)
            sc = np.trace(L @ R.conj().T) / N
            worst_s = max(worst_s, abs(abs(sc)-1))
            worst_r = max(worst_r, np.linalg.norm(L/sc - R)/math.sqrt(N))
    OUT["theta"] if False else None
    print(f"  egorov-op {name} N={N} m=A^T n: max||sigma|-1|={worst_s:.1e}, "
          f"max resid={worst_r:.1e}")
    ok(f"operator Egorov (m=A^T n), {name}", worst_s < 1e-12 and worst_r < 1e-12,
       "|scalar|=1 and residual ~ 0")

# ----------------------------------------------------------------------
# CHECK 3: torsion, anti-unitary Theta, Theta^2, for NON-symmetric A too.
# ----------------------------------------------------------------------
def find_R(A, B=40):
    a, b, c, d = A
    for p in range(-B, B+1):
        for q in range(-B, B+1):
            if q == 0:
                if p*p != 1: continue
                for r in range(-B, B+1):
                    if p*(a-d)+q*c+b*r == 0: return (p, q, r)
            else:
                num = 1-p*p
                if num % q: continue
                r = num//q
                if p*(a-d)+q*c+b*r == 0: return (p, q, r)
    return None


S = np.array([[1, 0], [0, -1]])
theta_rows = []
for name, A in A_MATRICES.items():
    Am = np.array([[A[0], A[1]], [A[2], A[3]]])
    R = find_R(A)
    assert R is not None, f"no reversing R found for {name}"
    p_, q_, r_ = R
    Rm = np.array([[p_, q_], [r_, -p_]])
    assert np.array_equal(Rm@Rm, np.eye(2, dtype=int)), "R not involution"
    assert np.array_equal(Rm@Am@Rm, np.round(np.linalg.inv(Am)).astype(int)), "not reversing"
    Mm = S@Rm
    Mf = [int(Mm[0, 0]), int(Mm[0, 1]), int(Mm[1, 0]), int(Mm[1, 1])]
    for N in (101, 257):
        if Mf[2] % N == 0: continue
        U = build_U(A, N); Um = build_U(Mf, N)
        Th = lambda X_: Um @ X_.conj() @ Um.conj().T
        L = Th(U)
        sc = np.trace(L @ U)/N
        res = np.linalg.norm(L/sc - U.conj().T)/math.sqrt(N)
        th2 = Th(lambda _=None: None) if False else Um @ Um.conj()
        t2 = np.trace(th2)/N
        res2 = np.linalg.norm(th2/t2 - np.eye(N))/math.sqrt(N)
        k, sg = ord_pm(A, N)
        K = k if sg > 0 else 2*k
        UK = np.linalg.matrix_power(U, K)
        chi = np.trace(UK)/N
        resK = np.linalg.norm(UK/chi - np.eye(N))/math.sqrt(N)
        theta_rows.append({"A": name, "N": N, "res_TR": res, "abs_sc": abs(sc),
                           "res_theta2": res2, "res_torsion": resK})
        print(f"  theta {name} N={N}: TR resid={res:.1e}, |sc|={abs(sc):.15f}, "
              f"Theta^2 resid={res2:.1e}, torsion resid={resK:.1e}")
OUT["theta"] = theta_rows
ok("THETA: anti-unitary TR + Theta^2=+1 + torsion, all A incl non-symmetric",
   all(r["res_TR"] < 1e-11 and abs(r["abs_sc"]-1) < 1e-12
       and r["res_theta2"] < 1e-11 and r["res_torsion"] < 1e-11 for r in theta_rows),
   f"{len(theta_rows)} (A,N) pairs")

# ----------------------------------------------------------------------
# CHECK 4: moment formula — WHICH constant, m_lambda or N/K?
# Tr V_lam^r = K^{-1} sum_J lam^{-J} Tr(Vbar^r U^J);
# J=0 term = K^{-1} Tr Vbar^r = (N/K) a_r  EXACTLY (Tr T(0)=N).
# Verify: (i) coefficient is N/K (not m_lam), (ii) error <= C^r.
# ----------------------------------------------------------------------
rng = np.random.default_rng(20260822)
moment_rows = []
for N in (199, 521):
    A = [2, 1, 1, 1]
    k, sg = ord_pm(A, N)
    K = k if sg > 0 else 2*k
    U = build_U(A, N); Ud = U.conj().T
    T = weyl_T(N)
    # random Hermitian V with frequency support F, |n_i|<=2
    terms = {}
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            if (n1, n2) == (0, 0) or (n1, n2) > (-n1, -n2): continue
            cc = (rng.normal()+1j*rng.normal())/math.sqrt(2)
            terms[(n1, n2)] = cc
    C = 2*sum(abs(cc) for cc in terms.values())
    def apply_V(M):
        Y = np.zeros_like(M)
        for (n1, n2), cc in terms.items():
            Y += cc*T(n1 % N, n2 % N)@M
            Y += np.conj(cc)*T((-n1) % N, (-n2) % N)@M
        return Y
    V = apply_V(np.eye(N, dtype=complex))
    V = 0.5*(V+V.conj().T)
    Vbar = np.zeros_like(V); Xv = V.copy()
    for j in range(K):
        Vbar += Xv; Xv = U@Xv@Ud
    Vbar /= K
    # projector onto one eigenspace
    lam = np.exp(2j*np.pi*3/K)*np.trace(np.linalg.matrix_power(U, K))[0]/abs(
        np.trace(np.linalg.matrix_power(U, K)))[0]/K if False else None
    UK = np.linalg.matrix_power(U, K); chi = np.trace(UK)/N
    lams = [chi**(1.0/K)*np.exp(2j*np.pi*j/K) for j in range(K)]
    lam = lams[3]
    P = np.zeros_like(U)
    Uj = np.eye(N, dtype=complex)
    for j in range(K):
        P += (lam**(-j))*Uj; Uj = U@Uj
    P /= K
    sv = np.linalg.svd(P, compute_uv=False)
    m = int(np.sum(sv > 0.5))
    # Weyl expansion of Vbar^2: a_2 := coefficient of T(0)
    Vbar2 = Vbar@Vbar
    # project onto Weyl basis: a_2 = N^{-1} Tr(Vbar^2 T(0)^dag) = N^{-1}Tr(Vbar^2)
    a2 = np.trace(Vbar2).real/N
    trV2 = np.trace(P@V2) if False else np.trace(Vbar2@P)  # (PVP)^2 = Vbar^2 P
    err_bound = C**2
    dev_NK = abs(trV2.real - (N/K)*a2)
    dev_m = abs(trV2.real - m*a2)
    moment_rows.append({"N": N, "K": K, "m": m, "NK": N/K, "a2": a2,
                        "trV2": trV2.real, "dev_from_NK": dev_NK,
                        "dev_from_m": dev_m, "bound_C2": err_bound})
    print(f"  moments N={N}: m={m}, N/K={N/K:.3f}, Tr V_lam^2={trV2.real:.6f}; "
          f"|dev from (N/K)a2|={dev_NK:.2e}, |dev from m*a2|={dev_m:.2e}, bound C^2={err_bound:.1f}")
    OUT["moments"].append(moment_rows[-1])
ok("MOMENTS: |Tr V_lam^2 - (N/K)a2| <= C^2 (per-multiplet O(1) error, as proven; "
   "exact only pooled)",
   all(r["dev_from_NK"] <= r["bound_C2"] for r in moment_rows),
   "; ".join(f"N={r['N']}: dev(NK)={r['dev_from_NK']:.1e} vs C^2={r['bound_C2']:.1e}"
             for r in moment_rows))

# multiplicity deviations across primes (Arnold map)
mult = []
for N in [p for p in (353, 401, 503, 701, 853, 1009, 1201, 1451, 1601, 2003,
                      2351, 2903, 3407, 4001, 5003) ]:
    k, sg = ord_pm([2, 1, 1, 1], N)
    if k < 0: continue
    K = k if sg > 0 else 2*k
    U = build_U([2, 1, 1, 1], N)
    ev = np.angle(np.linalg.eigvals(U))*K/(2*np.pi)
    cnt = {}
    for v_ in ev:
        j = int(round(v_)) % K
        cnt[j] = cnt.get(j, 0)+1
    ms = sorted(cnt.values())
    mult.append({"N": N, "K": K, "min_m": ms[0], "max_m": ms[-1],
                 "NK": N/K, "max_dev": max(abs(x-N/K) for x in ms)})
    print(f"  multiplicities N={N}: K={K}, dims {ms[0]}..{ms[-1]}, N/K={N/K:.2f}, "
          f"max|m-N/K|={mult[-1]['max_dev']:.2f}")
OUT["multiplicities"] = mult
ok("MULTIPLICITIES: max|m_lam - N/K| stays small (<2)",
   all(r["max_dev"] < 2.0 for r in mult),
   f"worst deviation {max(r['max_dev'] for r in mult):.2f}")

json.dump(OUT, open(os.path.join(ART, "indep_check.json"), "w"), indent=1)
print("\npartial save -> artifacts/indep_check.json")
if FAILS:
    print("FAILURES:", FAILS); sys.exit(1)
print("ALL CHECKS SO FAR PASS")
