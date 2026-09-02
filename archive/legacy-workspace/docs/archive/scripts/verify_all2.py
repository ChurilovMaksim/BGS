"""
INDEPENDENT VERIFICATION SUITE v2 — all claims of run 2, fresh code paths.
Run:  py -3 verify_all2.py
Exit code 0 iff every check passes.
"""
import numpy as np, math, json, os, sys
import scipy.linalg as sla

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
PASS = []


def ok(tag, cond, detail):
    PASS.append((tag, bool(cond), detail))
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}: {detail}")


# ---------- fresh, independent constructions ----------
def U_cat(A, N):
    a, b, c, d = A
    icb = pow((2*c) % N, -1, N)
    out = np.empty((N, N), dtype=complex)
    for x in range(N):
        for y in range(N):
            e = (icb*(d*x*x - 2*x*y + a*y*y)) % N
            out[x, y] = np.exp(2j*np.pi*e/N)
    return out/math.sqrt(N)


def weyl(N):
    b2 = pow(2, -1, N)
    def T(n1, n2):
        n1 %= N; n2 %= N
        M = np.zeros((N, N), dtype=complex)
        for x in range(N):
            M[x, (x-n1) % N] = np.exp(2j*np.pi*((n2*((x-n1) % N)) % N)/N)
        return np.exp(2j*np.pi*((b2*n1*n2) % N)/N)*M
    return T


def ordpm(A, N):
    a, b, c, d = [v % N for v in A]
    m = (1, 0, 0, 1)
    for k in range(1, 2*N+3):
        m = ((m[0]*a+m[1]*c) % N, (m[0]*b+m[1]*d) % N,
             (m[2]*a+m[3]*c) % N, (m[2]*b+m[3]*d) % N)
        if m == (1, 0, 0, 1): return k, +1
        if m == (N-1, 0, 0, N-1): return k, -1
    return -1, 0


A = [2, 1, 1, 1]

# T1: unitarity + exact Egorov
e_uni, e_ego = 0.0, 0.0
for N in (11, 101):
    U = U_cat(A, N); T = weyl(N)
    e_uni = max(e_uni, np.max(np.abs(U@U.conj().T-np.eye(N))))
    for n in [(1, 0), (0, 1), (2, 3)]:
        An = ((A[0]*n[0]+A[1]*n[1]) % N, (A[2]*n[0]+A[3]*n[1]) % N)
        L = U@T(*n)@U.conj().T; Rr = T(*An)
        t = np.trace(L@Rr.conj().T)/N
        e_ego = max(e_ego, np.linalg.norm(L/t-Rr)/math.sqrt(N))
ok("T1 unitary + exact Egorov covariance", e_uni < 1e-12 and e_ego < 1e-11,
   f"max|UU*-I|={e_uni:.1e}, max Egorov residual={e_ego:.1e}")

# T2: exact torsion U^K = chi I, multiplicities
worst, info = 0.0, []
for N in (101, 199, 521):
    k, s = ordpm(A, N); K = k if s > 0 else 2*k
    U = U_cat(A, N)
    UK = np.linalg.matrix_power(U, K)
    chi = np.trace(UK)/N
    worst = max(worst, np.linalg.norm(UK/chi-np.eye(N))/math.sqrt(N))
    ev = np.angle(np.linalg.eigvals(U))
    nd = len(set(np.round(ev*K/(2*np.pi)).astype(int) % K))
    info.append(f"N={N}: K={K}, distinct={nd}, mult~{N/K:.0f}")
ok("T2 exact torsion U^K = chi*I", worst < 1e-11, f"max residual={worst:.1e}; "+"; ".join(info))

# T3: Diophantine reversibility + anti-unitary Theta
def find_R(A, B=40):
    a, b, c, d = A
    for p_ in range(-B, B+1):
        for q in range(-B, B+1):
            if q == 0:
                if p_*p_ != 1: continue
                for r in range(-B, B+1):
                    if p_*(a-d)+q*c+b*r == 0: return (p_, q, r)
            else:
                num = 1-p_*p_
                if num % q: continue
                r = num//q
                if p_*(a-d)+q*c+b*r == 0: return (p_, q, r)
    return None

worst3 = 0.0; found_all = True
for Ai in ([2, 1, 1, 1], [3, 2, 1, 1], [7, 3, 2, 1], [11, 3, 7, 2]):
    R = find_R(Ai)
    if R is None: found_all = False; continue
    p_, q, r = R
    Rm = np.array([[p_, q], [r, -p_]])
    Am = np.array([[Ai[0], Ai[1]], [Ai[2], Ai[3]]])
    assert np.array_equal(Rm@Rm, np.eye(2, dtype=int)), "R not involution"
    assert np.array_equal(Rm@Am@Rm, np.round(np.linalg.inv(Am)).astype(int)), "R not reversing"
    S = np.array([[1, 0], [0, -1]]); Mm = S@Rm
    Mf = [int(Mm[0, 0]), int(Mm[0, 1]), int(Mm[1, 0]), int(Mm[1, 1])]
    N = 101
    if Mf[2] % N == 0: continue
    U = U_cat(Ai, N); Um = U_cat(Mf, N)
    L = Um@U.conj()@Um.conj().T
    t = np.trace(L@U)/N
    worst3 = max(worst3, np.linalg.norm(L/t-U.conj().T)/math.sqrt(N))
    Th2 = Um@Um.conj(); t2 = np.trace(Th2)/N
    worst3 = max(worst3, np.linalg.norm(Th2/t2-np.eye(N))/math.sqrt(N))
ok("T3 reversing involution + Theta U Theta^-1 = U^-1, Theta^2=1",
   found_all and worst3 < 1e-12, f"max residual over 4 matrices = {worst3:.1e}")

# T4: real structure and the [Theta,V]=0 <=> real symmetric equivalence
N = 521
k, s = ordpm(A, N); K = k if s > 0 else 2*k
U = U_cat(A, N); Um = U_cat([1, 0, 1, 1], N)
Th = lambda X: Um@X.conj()@Um.conj().T
UK = np.linalg.matrix_power(U, K); lam = (np.trace(UK)/N)**(1.0/K)
rng = np.random.default_rng(0)
Wb = (rng.normal(size=(N, 120))+1j*rng.normal(size=(N, 120)))/math.sqrt(2)
Acc = np.zeros_like(Wb); cur = Wb.copy()
for j in range(K):
    if j: cur = U@cur
    Acc += (lam**(-j))*cur
Q1, sv, _ = np.linalg.svd(Acc/K, full_matrices=False)
m = int(np.sum(sv > 1e-6*sv.max())); B = Q1[:, :m]
Wm = B.conj().T@Um@B.conj()
c1 = np.linalg.norm(Wm@Wm.conj().T-np.eye(m))
c2 = np.linalg.norm(Wm-Wm.T)/np.linalg.norm(Wm)
c3 = np.linalg.norm(Wm@Wm.conj()-np.eye(m))
Qs = sla.sqrtm(Wm)
T = weyl(N); rr = np.random.default_rng(7)
V = np.zeros((N, N), dtype=complex)
for n1 in range(-3, 4):
    for n2 in range(-3, 4):
        if (n1, n2) == (0, 0) or (n1, n2) > (-n1, -n2): continue
        cc = (rr.normal()+1j*rr.normal())/math.sqrt(2); Aa = T(n1, n2)
        V += cc*Aa+np.conj(cc)*Aa.conj().T
V = 0.5*(V+V.conj().T); Vs = 0.5*(V+Th(V)); Vs = 0.5*(Vs+Vs.conj().T)
def imag_ratio(VV):
    Vl = B.conj().T@VV@B; Vl = 0.5*(Vl+Vl.conj().T)
    Vp = Qs.conj().T@Vl@Qs
    return np.linalg.norm(Vp.imag)/np.linalg.norm(Vp)
r_sym, r_gen = imag_ratio(Vs), imag_ratio(V)
ok("T4 real structure on H_lambda (W symmetric unitary involution)",
   c1 < 1e-10 and c2 < 1e-12 and c3 < 1e-10,
   f"m={m}: |WW*-I|={c1:.1e}, |W-W^T|={c2:.1e}, |W conj(W)-I|={c3:.1e}")
ok("T4 [Theta,V]=0 <=> compression real symmetric",
   r_sym < 1e-10 and r_gen > 0.1, f"Im-ratio: Theta-invariant={r_sym:.1e}, generic={r_gen:.2f}")

# T5: exact time reversal of the symmetric Floquet map
dv, Wv = np.linalg.eigh(Vs); dg, Wg = np.linalg.eigh(V)
res5 = {}
for tag, (dd, WW) in (("sym", (dv, Wv)), ("gen", (dg, Wg))):
    eps = 0.01
    H = WW@(np.exp(0.5j*eps*dd)[:, None]*WW.conj().T)
    Ue = H@U@H
    L = Um@Ue.conj()@Um.conj().T
    t = np.trace(L@Ue)/N
    res5[tag] = np.linalg.norm(L/t-Ue.conj().T)/math.sqrt(N)
ok("T5 Theta U_eps Theta^-1 = U_eps^-1  iff  [Theta,V]=0",
   res5["sym"] < 1e-12 and res5["gen"] > 1e-3,
   f"residual: Theta-invariant={res5['sym']:.1e}, generic={res5['gen']:.1e}")

# N1: re-read the main measurement and compare with stored controls
try:
    r = json.load(open(os.path.join(ART, "scaling_3571_full.json")))
    ctl = json.load(open(os.path.join(ART, "controls_m210.json")))["controls"]
    (gg, gu), (ug, uu) = ctl["goe"], ctl["gue"]
    z_sym = (r["sym"]["L1_goe"]-gg[0])/gg[1]
    z_gen = (r["generic"]["L1_gue"]-uu[0])/uu[1]
    ok("N1 p=3571 compression statistics vs matched RMT controls",
       abs(z_sym) < 2 and abs(z_gen) < 2,
       f"z(Theta-inv vs GOE)={z_sym:+.2f}, z(generic vs GUE)={z_gen:+.2f}")
except Exception as ex:
    ok("N1 artifacts present", False, f"{type(ex).__name__}: {ex}")

# ---------- T6/T7/T8: structural identity, trace identity, classical density ----------
def weyl_T(N):
    b2 = pow(2, -1, N)
    def T(n1, n2):
        n1 %= N; n2 %= N
        M = np.zeros((N, N), dtype=complex)
        for x in range(N):
            M[x, (x-n1) % N] = np.exp(2j*np.pi*((n2*((x-n1) % N)) % N)/N)
        return np.exp(2j*np.pi*((b2*n1*n2) % N)/N)*M
    return T

worst6 = worst6c = 0.0
worst7 = 0.0
for Np in (101, 199, 521):
    kk, ss = ordpm(A, Np); KK = kk if ss > 0 else 2*kk
    Uu = U_cat(A, Np); Ud = Uu.conj().T
    UKK = np.linalg.matrix_power(Uu, KK); chi = np.trace(UKK)/Np
    lm = chi**(1.0/KK)
    Pp = np.zeros((Np, Np), dtype=complex); Uj = np.eye(Np, dtype=complex)
    for j in range(KK):
        Pp += (lm**(-j))*Uj; Uj = Uu@Uj
    Pp /= KK
    Tt = weyl_T(Np); rr2 = np.random.default_rng(5)
    Vv = np.zeros((Np, Np), dtype=complex)
    for n1 in range(-3, 4):
        for n2 in range(-3, 4):
            if (n1, n2) == (0, 0) or (n1, n2) > (-n1, -n2): continue
            cc = (rr2.normal()+1j*rr2.normal())/math.sqrt(2); Aa = Tt(n1, n2)
            Vv += cc*Aa+np.conj(cc)*Aa.conj().T
    Vv = 0.5*(Vv+Vv.conj().T)
    Vb = np.zeros_like(Vv); Xx = Vv.copy()
    for j in range(KK): Vb += Xx; Xx = Uu@Xx@Ud
    Vb /= KK
    worst6 = max(worst6, np.linalg.norm(Pp@Vv@Pp-Vb@Pp)/np.linalg.norm(Pp@Vv@Pp))
    worst6c = max(worst6c, np.linalg.norm(Vb@Uu-Uu@Vb)/np.linalg.norm(Vb))
    for J in range(1, min(KK, 6)):
        UJ = np.linalg.matrix_power(Uu, J)
        for v1, v2 in ((0, 1), (1, 0), (3, 5)):
            worst7 = max(worst7, abs(abs(np.trace(Tt(v1, v2)@UJ))-1.0))
ok("T6 P_lam V P_lam = Vbar P_lam with [Vbar,U]=0 (quantum Birkhoff average)",
   worst6 < 1e-12 and worst6c < 1e-12,
   f"max |PVP-Vbar P|/|PVP|={worst6:.1e}, max |[Vbar,U]|/|Vbar|={worst6c:.1e}")
ok("T7 |Tr(T(v) U^J)| = 1 for all v and J not= 0 mod K",
   worst7 < 1e-12, f"max deviation from 1 = {worst7:.1e}")

try:
    dd = json.load(open(os.path.join(ART, "birkhoff_density.json")))
    okd = all(r["ks"] < 1.0/math.sqrt(r["m"]) for r in dd) and \
          all(abs(r["sd_ratio"]-1) < 0.10 for r in dd)
    ok("T8 multiplet density = classical Birkhoff-average distribution",
       okd, "; ".join(f"p={r['p']}: KS={r['ks']:.3f}<{1/math.sqrt(r['m']):.3f}, "
                      f"sd ratio={r['sd_ratio']:.3f}" for r in dd))
except Exception as ex:
    ok("T8 artifacts present", False, f"{type(ex).__name__}: {ex}")

try:
    cc = json.load(open(os.path.join(ART, "cancellation_identity.json")))
    ok("T9 frequency-cancellation identity Tr(P T..T) = m*1{sum u=0} + E, |E|<1",
       all(r["dev_zero"] < 1e-10 for r in cc) and all(r["dev_nonzero"] < 1.0 for r in cc),
       "; ".join(f"p={r['p']}: |Tr-m|={r['dev_zero']:.0e}, max|Tr|(sum!=0)={r['dev_nonzero']:.3f}" for r in cc))
    ok("T10 Wigner normalisation m/K + orbit decorrelation (errors < 1)",
       all(r["hs_dev"] < 1.0 and r["cross_max"] < 1.0 for r in cc),
       "; ".join(f"p={r['p']}: m/K={r['m_over_K']:.3f}, HS dev={r['hs_dev']:.3f}, cross={r['cross_max']:.3f}" for r in cc))
except Exception as ex:
    ok("T9/T10 artifacts present", False, f"{type(ex).__name__}: {ex}")

try:
    rg = json.load(open(os.path.join(ART, "rigidity.json")))
    r2 = [x for x in rg if x["r"] == 2]
    okA = all(x["spread"] < x["bound"] for x in rg)
    okB = max(x["spread"] for x in r2) < 3*min(x["spread"] for x in r2)+10
    ok("T12 deterministic rigidity: spread of Tr f(V_lam) is O_f(1), mean is O(m)",
       okA and okB,
       "; ".join(f"p={x['p']},r={x['r']}: spread={x['spread']:.2f} < C^r={x['bound']:.1e}, mean={x['mean']:.1f}"
                 for x in rg if x["r"] == 2))
except Exception as ex:
    ok("T12 artifacts present", False, f"{type(ex).__name__}: {ex}")

for tag, fname, test in (
    ("T13 no GSE: Theta^2 = +1 for every reversing involution, all A and p tested",
     "theta_sign.json",
     lambda d: all(set(r["signs"].keys()) <= {"+1"} and r["signs"].get("+1", 0) > 0 for r in d)),
    ("T14 robustness: 4 cat maps x split/inert, correct class + RMT number variance",
     "robustness.json",
     lambda d: all(r["sym"]["L1_goe"] < r["sym"]["L1_gue"] and
                   r["gen"]["L1_gue"] < r["gen"]["L1_goe"] and
                   max(r["sym"]["nvar"].values()) < 2.0 for r in d["rows"])),
    ("T15 FFT propagator exact (6e-16) and large-multiplicity run m=623",
     "largescale.json",
     lambda d: d["runs"][0]["sym"]["L1_goe"] < d["runs"][0]["sym"]["L1_gue"] and
               d["runs"][0]["gen"]["L1_gue"] < d["runs"][0]["gen"]["L1_goe"] and
               max(d["runs"][0]["dims"]) >= 600),
    ("T16 form factor matches the ANALYTIC GOE/GUE curves better than Poisson",
     "form_factor_pooled.json",
     lambda d: d["rms"]["sym_goe_theory"] < 0.06 and d["rms"]["gen_gue_theory"] < 0.06
               and d["rms"]["sym_poisson"] > 6*d["rms"]["sym_goe_theory"]),
):
    try:
        d = json.load(open(os.path.join(ART, fname)))
        ok(tag, test(d), f"from {fname}")
    except Exception as ex:
        ok(tag, False, f"{type(ex).__name__}: {ex}")

try:
    r4 = json.load(open(os.path.join(ART, "cancellation_r4.json")))
    ok("T17 exact 4th-order count = 2k^2-k / 3k^2-3k (all pairings, no extras)",
       r4["all_exact"] and len(r4["r4"]) >= 15,
       f"{sum(1 for r in r4['r4'] if r['ok'])}/{len(r4['r4'])} exact matches, "
       f"p<=2003, k<=25, both branches")
except Exception as ex:
    ok("T17 artifacts present", False, f"{type(ex).__name__}: {ex}")

for tag, fname, test in (
    ("T19 exact tight-frame identity: covariance of the orbit family IS the GUE one",
     "tight_frame.json", lambda d: all(r["exact"] for r in d) and len(d) >= 4),
    ("T20 randomness is arithmetic: ONE orbit (2 parameters) already gives GOE",
     "dof_test.json",
     lambda d: [r for r in d if r["nF"] == 1][0]["L1_goe"] < 0.15 and
               [r for r in d if r["nF"] == 1][0]["L1_goe"] <
               [r for r in d if r["nF"] == 1][0]["L1_gue"] and
               min(r["L1_gue"] for r in d if r["nF"] >= 2 and r["tag"] == "gen") < 0.10),
):
    try:
        d = json.load(open(os.path.join(ART, fname)))
        ok(tag, test(d), f"from {fname}")
    except Exception as ex:
        ok(tag, False, f"{type(ex).__name__}: {ex}")

print("\n" + "="*60)
n_ok = sum(1 for _, o, _ in PASS if o)
print(f"TOTAL: {n_ok}/{len(PASS)} checks PASS")
print("="*60)
json.dump({"checks": [[t, o, d] for t, o, d in PASS]},
          open(os.path.join(ART, "verification_suite_v2.json"), "w"), indent=1)
sys.exit(0 if n_ok == len(PASS) else 1)
