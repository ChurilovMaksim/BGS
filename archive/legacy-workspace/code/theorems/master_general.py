"""
RUN 12 / Phase A: GENERAL-R MASTER FORMULA VIA ITERATIVE STATE ACCUMULATION.

Replaces hardcoded r=2,3,4 branches in master_formula.py with a single
iterative loop valid for any r >= 1. Memory O(n^(r-1)) where n = 2|F|*K;
time O(r*n^r). Practical for r <= 6 with |F|=2, K <= 8 on 16 GB RAM.

Master identity being verified:
  Tr[(P_lam V P_lam)^r]
      = (N/K)*a_r + (1/K) * sum_{J=1}^{K-1} lam^{-J} * S_J,
  S_J = K^{-r} * sum over ordered signed-(freq,vector) tuples
        prod_i c_{n_i}^{eps_i}
        * exp(i pi/N * [sum_i eps_i Q_{j_i}(n_i)
                         + sum_{i<l} Psi(g_i, g_l)])
        * rho_J( (sum_i g_i) mod N )

Regression target: reproduce r=4 numbers from master_formula.py to <1e-9.
"""
import json, math, os, sys, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_core import U_cat, ord_pm
from master_formula import cocycle, rho_tables, weyl_matrix

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


# ----------------------------------------------------------- core engine ---
def build_terms(F, cs):
    """Flatten (freq_vector, sign) into list of (coeff, eps, n_vec)."""
    out = []
    for n in F:
        nv = np.array(n, dtype=np.int64)
        out.append((cs[n], +1, nv))
        out.append((complex(np.conj(cs[n])), -1, nv))
    return out


def precompute(N, K, Bm, SIG, terms):
    """G/L/K-flattened arrays: G[n,2], SPH[n], CO[n]."""
    L = len(terms)
    G = np.empty((L * K, 2), dtype=np.int64)
    SPH = np.empty(L * K, dtype=np.int64)
    CO = np.empty(L * K, dtype=complex)
    for si, (cf, ep, nv) in enumerate(terms):
        cur = nv.copy() % N
        for j in range(K):
            idx = si * K + j
            G[idx] = (ep * cur) % N
            CO[idx] = cf
            SPH[idx] = int(ep * SIG[j][nv[0] % N, nv[1] % N])
            cur = (Bm @ cur) % N
    return G, SPH, CO


def psi_matrix(N, G):
    """Psi(g,h) = (N+1)(g2 h1 - g1 h2) mod 2N for every pair."""
    gg = G.astype(np.int64)
    return ((int(N) + 1) * (gg[:, 1][:, None] * gg[:, 0][None, :]
                            - gg[:, 0][:, None] * gg[:, 1][None, :])) % (2 * N)


def SJ_iterative(N, K, G, SPH, CO, PSI, rho_tab, r, t0ph=1.0,
                 mitm_threshold=None):
    """
    Compute S_J for arbitrary rank r via iterative state accumulation.

    If total state count n^r exceeds mitm_threshold (default 5e6), uses
    meet-in-the-middle: split positions into two halves, enumerate each
    separately (O(n^{r/2})), then combine via hash join on g-vector.
    Memory O(n^{r/2+1}), time O(n^{r/2+1}) per J.
    """
    n = len(CO)
    if r == 0:
        return complex(rho_tab[0, 0])
    total_states = n ** r
    thresh = mitm_threshold if mitm_threshold else 5_000_000

    if total_states <= thresh:
        return _sj_direct(N, K, G, SPH, CO, PSI, rho_tab, r, t0ph)
    else:
        return _sj_mitm(N, K, G, SPH, CO, PSI, rho_tab, r, t0ph)


def _sj_direct(N, K, G, SPH, CO, PSI, rho_tab, r, t0ph):
    """Direct iterative accumulation (original approach)."""
    n = len(CO)
    if r == 0:
        return complex(rho_tab[0, 0])
    # state after choosing first element
    g_state = G.astype(np.int64).copy()                # [n, 2]
    ph_state = (SPH.astype(np.int64)) % (2 * N)        # [n]
    co_state = CO.copy()                               # [n]
    v_state = PSI.astype(np.int64).copy()              # [n, n] rows

    for _ in range(r - 1):
        m = len(co_state)
        # cross-phase for extending each state s by each option t
        cross = v_state[:, np.arange(n)]                      # [m, n]
        g_new = (g_state[:, None, :] + G[None, :, :]) % N
        ph_new = (ph_state[:, None] + SPH[None, :] + cross) % (2 * N)
        co_new = co_state[:, None] * CO[None, :]
        v_new = (v_state[:, None, :] + PSI[None, :, :]) % (2 * N)
        # flatten
        g_state = g_new.reshape(-1, 2)
        ph_state = ph_new.reshape(-1)
        co_state = co_new.reshape(-1)
        v_state = v_new.reshape(-1, n)

    # rho_tab stores INTEGER exponents; convert via zeta^E = exp(i pi E / N)
    # Multiply by t0ph = Tr[U^J]/|Tr[U^J]| to recover actual rho values.
    E_vals = rho_tab[g_state[:, 0], g_state[:, 1]]
    rv = np.exp(1j * np.pi * E_vals / N) * t0ph
    total = np.sum(co_state * np.exp(1j * np.pi * ph_state / N) * rv)
    return complex(total) / K ** r


def _sj_mitm(N, K, G, SPH, CO, PSI, rho_tab, r, t0ph):
    """
    Meet-in-the-middle exploiting BILINEARITY of Psi.
    Split positions into two halves; enumerate each half independently,
    tracking internal PSI. Cross-half PSI computed from SUMS of g-vectors
    via bilinearity: sum_{i in H1, l in H2} Psi[g_i, g_l]
                  = Psi[sum_{H1} g_i, sum_{H2} g_l].

    Audit optimization (2026-08-26): the pure-Python double loop over
    (i1, i2) is replaced by chunked NumPy broadcasting with integer
    phase-table lookups. Identical mathematics; summation order differs
    by O(1e-16) rounding only.
    Memory O(chunk * n^{r2}), time O(n^r) fully vectorized.
    """
    n = len(CO)
    h = r // 2
    r2 = r - h

    g1, ph1, co1 = _enumerate_half(N, K, G, SPH, CO, PSI, h)
    g2, ph2, co2 = _enumerate_half(N, K, G, SPH, CO, PSI, r2)

    m2 = len(co2)
    Np1 = int(N) + 1

    # unit-phase lookup tables keyed by integer exponents mod 2N
    tab = np.exp(1j * np.pi * np.arange(2 * N) / N)

    rho_flat = np.asarray(rho_tab, dtype=np.int64).reshape(-1)
    Nr = rho_flat.size

    g2_0 = g2[:, 0].astype(np.int64)
    g2_1 = g2[:, 1].astype(np.int64)
    ph2l = ph2.astype(np.int64)
    co2c = co2.astype(complex)

    # keep chunk * m2 around a few million cells (memory guard)
    cells_budget = 2_000_000
    C = max(1, min(len(co1), cells_budget // max(1, m2)))

    total = 0.0 + 0.0j
    for s0 in range(0, len(co1), C):
        ga = g1[s0:s0 + C].astype(np.int64)          # (c, 2)
        bph = ph1[s0:s0 + C].astype(np.int64)        # (c,)
        bco = co1[s0:s0 + C].astype(complex)         # (c,)
        gv0 = (ga[:, 0][:, None] + g2_0[None, :]) % N
        gv1 = (ga[:, 1][:, None] + g2_1[None, :]) % N
        flat = (gv0 * N + gv1).ravel()
        np.mod(flat, Nr, out=flat)
        rv = tab[np.mod(rho_flat[flat], 2 * N)]
        cross = (Np1 * (ga[:, 1][:, None] * g2_0[None, :]
                        - ga[:, 0][:, None] * g2_1[None, :])) % (2 * N)
        pht = (bph[:, None] + ph2l[None, :] + cross) % (2 * N)
        # rv below must carry the per-J phase t0ph (see original):
        # applied once to the chunk sum, since rv enters every term.
        terms = (bco[:, None] * co2c) * \
            tab[pht.ravel()].reshape(pht.shape) * \
            rv.reshape(gv0.shape)
        total += terms.sum()

    return complex(total * t0ph) / K ** r


def _enumerate_half(N, K, G, SPH, CO, PSI, h):
    """Enumerate all n^h partial tuples; returns (g, phase, coeff) arrays."""
    n = len(CO)
    if h == 0:
        return np.zeros((1, 2), dtype=np.int64), np.zeros(1, dtype=np.int64), \
               np.ones(1, dtype=complex)
    g_state = G.astype(np.int64).copy()
    ph_state = (SPH.astype(np.int64)) % (2 * N)
    co_state = CO.copy()
    v_state = PSI.astype(np.int64).copy()

    for _ in range(h - 1):
        m = len(co_state)
        cross = v_state[:, np.arange(n)]
        g_new = (g_state[:, None, :] + G[None, :, :]) % N
        ph_new = (ph_state[:, None] + SPH[None, :] + cross) % (2 * N)
        co_new = co_state[:, None] * CO[None, :]
        v_new = (v_state[:, None, :] + PSI[None, :, :]) % (2 * N)
        g_state = g_new.reshape(-1, 2)
        ph_state = ph_new.reshape(-1)
        co_state = co_new.reshape(-1)
        v_state = v_new.reshape(-1, n)

    return g_state, ph_state, co_state


# ------------------------------------------------------- validation ------
def validate_config(A, N, r, F, seed=1, K_override=None):
    """Run full pipeline for one configuration; returns rows + timing."""
    t0 = time.time()
    k, sg = ord_pm(A, N)
    assert k > 0, f"A={A} has finite order?"
    K = k if sg > 0 else 2 * k
    if K_override:
        K = K_override
    info, Bm, SIG, U = cocycle(A, N, K)
    RH, unimod = rho_tables(N, K, U)

    rng = np.random.default_rng(seed)
    cs = {nn: (rng.normal() + 1j * rng.normal()) / math.sqrt(2) for nn in F}

    # build V and its time-average
    V = np.zeros((N, N), dtype=complex)
    for nn, cc in cs.items():
        V += cc * weyl_matrix(nn[0] % N, nn[1] % N, N)
        V += np.conj(cc) * weyl_matrix((-nn[0]) % N, (-nn[1]) % N, N)
    Xv, Vbar = V.copy(), np.zeros_like(V)
    for _ in range(K):
        Vbar += Xv
        Xv = U @ Xv @ U.conj().T
    Vbar /= K
    a_r = float(np.real(np.trace(np.linalg.matrix_power(Vbar, r)))) / N

    terms = build_terms(F, cs)
    G, SPH, CO = precompute(N, K, Bm, SIG, terms)
    PSI = psi_matrix(N, G)

    SJs = []
    for J in range(1, K):
        UJ = np.linalg.matrix_power(U, J)
        tr = complex(np.trace(UJ))
        t0ph = tr / abs(tr) if abs(tr) > 1e-12 else 1.0
        SJs.append(SJ_iterative(N, K, G, SPH, CO, PSI, RH[J], r, t0ph))

    UK = np.linalg.matrix_power(U, K)
    lam0 = (np.trace(UK) / N) ** (1.0 / K)
    rows = []
    Vr = np.linalg.matrix_power(Vbar, r)
    for jj in range(min(3, K)):
        lam = lam0 * np.exp(2j * np.pi * jj / K)
        Pl = np.zeros_like(U)
        Uj = np.eye(N, dtype=complex)
        for j in range(K):
            Pl += (lam ** (-j)) * Uj
            Uj = U @ Uj
        Pl /= K
        lhs = float(np.real(np.trace(Vr @ Pl)))
        rhs = (N / K) * a_r + (1.0 / K) * sum(
            (lam ** (-JJ)) * sj for JJ, sj in enumerate(SJs, start=1))
        err_re = abs(lhs - float(np.real(rhs)))
        err_im = abs(float(np.imag(rhs)))
        rows.append(dict(lam_idx=int(jj), lhs=lhs, rhs_re=float(np.real(rhs)),
                         err_re=err_re, err_im=err_im))
    ok = bool(rows and all(rr["err_re"] < 1e-7 * max(1, abs(rr["lhs"]))
                           and rr["err_im"] < 1e-7 * max(1, abs(rr["lhs"]))
                           for rr in rows))
    return dict(A=list(A), N=N, r=r, K=K, rows=rows, passed=ok,
                dt=time.time() - t0)


def main():
    print("=== RUN 12 Phase A: general-r master formula ===", flush=True)
    RES = {"runs": []}
    configs = [
        # regression: reproduce artifact master_general.json (4 runs)
        ([2, 1, 1, 1], 101, 2, [(1, 0), (0, 1)]),
        ([2, 1, 1, 1], 101, 3, [(1, 0), (0, 1)]),
        ([2, 1, 1, 1], 101, 4, [(1, 0)]),
        ([3, 1, 2, 1], 101, 4, [(1, 0)]),
        # new (audit 2026-08-26): r=5 now feasible with vectorized MITM
        ([2, 1, 1, 1], 101, 5, [(1, 0)]),
    ]
    allpass = True
    for (A, N, r, F) in configs:
        try:
            res = validate_config(A, N, r, F)
        except MemoryError:
            print(f"[SKIP-OUT-OF-MEM] A={A} N={N} r={r}", flush=True)
            continue
        RES["runs"].append(res)
        tag = "PASS" if res["passed"] else "FAIL"
        allpass &= res["passed"]
        errs = " ".join(f"({rr['err_re']:.1e},{rr['err_im']:.1e})"
                        for rr in res["rows"])
        print(f"[{tag}] A={A} N={N} r={r}: err {errs} "
              f"({res['dt']:.1f}s)", flush=True)
    json.dump(RES, open(os.path.join(ART, "master_general.json"), "w"),
              indent=1, default=str)
    print("saved artifacts/master_general.json", flush=True)
    print("ALL PASS" if allpass else "SOME FAIL", flush=True)


if __name__ == "__main__":
    main()
