"""
RUN 4 / M1 (final): MASTER MOMENT FORMULA WITH ALL PHASES.

    Tr(V_lambda^r) = (N/K) a_r
                     + (1/K) sum_{J=1}^{K-1} lambda^{-J} * S_J,
    S_J = K^{-r} * sum_{ordered signed-frequency tuples}
          (prod coeff) * zeta^{ sum_i eps_i Q_{j_i}(n_i)
                                + sum_{i<l} Psi(g_i,g_l) }
          * rho_J( (sum_i g_i) mod N ),

  g_i = eps_i B^{j_i} n_i  (B = A^T),
  Psi_d(g,h) = (N+1)(g2 h1 - g1 h2) mod 2N   [machine-established product rule],
  zeta = e^{pi i/N};  rho_J(v) := Tr(T(v) U^J)/Tr(U^J)  (|rho_J(v)| = 1, exact
  table; empirically piecewise quadratic -- NOT globally quadratic).

Ingredients machine-verified:
  (V1) sigma_1 = zeta^{Q_1}, Q_1 exactly-fitted quadratic; exhaustive/random.
  (V2) telescoping Q_j(n) = Q_{j-1}(B n) + ... verified vs direct matrices.
  (V3) rho_J unimodular for all v, all J (T7), tabulated exactly.
  (V4) MASTER identity vs direct traces: |Re lhs - Re rhs| and |Im rhs| small.
"""
import numpy as np, json, os, time, math
from fractions import Fraction
from catmap_core import U_cat, ord_pm

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
RES = {"sigma": [], "rho": [], "master": [], "cancel": []}


# ------------------------------------------------------------------ utils --
def weyl_matrix(n1, n2, N):
    """Exactly catmap_core.weyl convention:
    T(n1,n2) = w^{b2 n1 n2} X^{n1} Z^{n2},  (T psi)(x) = w^{b2 n1n2 + n2(x-n1)}
    psi(x-n1);  entry [x, (x-n1)%N] = w^{n2*x - b2*n1*n2}."""
    w = np.exp(2j * np.pi / N)
    b2inv = pow(2, -1, N)
    xs = np.arange(N)
    sh = np.zeros((N, N), dtype=complex)
    sh[xs, (xs - n1) % N] = 1.0
    return (w ** ((n2 * xs - b2inv * n1 * n2) % N))[:, None] * sh


def to_exp(z, N):
    E = np.rint(np.angle(z) * N / np.pi).astype(np.int64) % (2 * N)
    err = float(np.max(np.abs(np.exp(1j * np.pi * E / N) - z)))
    return E, err


def solve_exact(rows, rhs):
    M = [[Fraction(x) for x in r] + [Fraction(v)] for r, v in zip(rows, rhs)]
    n = len(rhs)
    for col in range(n):
        piv = next((i for i in range(col, n) if M[i][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for i in range(n):
            if i != col and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[col])]
    return [M[i][n] for i in range(n)]


def circ_dev(pred, truth, N):
    return float(np.max(np.abs(((np.asarray(pred) - np.asarray(truth) + N)
                                % (2 * N)) - N)))


# ------------------------------------------------------------ cocycle ------
def cocycle(A, N, K):
    a, b, c, d = A
    Bm = np.array([[a % N, c % N], [b % N, d % N]])
    U = U_cat(A, N)

    def sigma_direct(j, n1, n2):
        Uj = np.linalg.matrix_power(U, j)
        x, y = int(n1), int(n2)
        for _ in range(j):
            x, y = (Bm[0, 0] * x + Bm[0, 1] * y) % N, \
                   (Bm[1, 0] * x + Bm[1, 1] * y) % N
        sc = np.trace((Uj @ weyl_matrix(int(n1), int(n2), N) @ Uj.conj().T)
                      @ weyl_matrix(x, y, N).conj().T) / N
        return sc

    pts = []
    for (n1, n2) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        sc = sigma_direct(1, n1, n2)
        assert abs(abs(sc) - 1) < 1e-9
        E, _ = to_exp(np.array([sc]), N)
        pts.append([[n1 * n1, n1 * n2, n2 * n2, 1], int(E[0])])
    sol = solve_exact([p[0] for p in pts], [p[1] for p in pts])
    assert sol is not None and all(s.denominator <= 64 for s in sol)
    fl = [float(s) for s in sol]
    Q1 = lambda x, y: fl[0] * x * x + fl[1] * x * y + fl[2] * y * y + fl[3]
    rng = np.random.default_rng(5)
    mx = 0.0
    for _ in range(120):
        n1, n2 = int(rng.integers(0, N)), int(rng.integers(0, N))
        mx = max(mx, abs(np.exp(1j * np.pi * (Q1(n1, n2) % (2 * N)) / N)
                         - sigma_direct(1, n1, n2)))
    n1g, n2g = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    acc = np.zeros((N, N))
    SIG = np.zeros((K, N, N))
    for j in range(1, K):
        acc = (acc + Q1(n1g, n2g)) % (2 * N)
        n1g, n2g = (Bm[0, 0] * n1g + Bm[0, 1] * n2g) % N, \
                   (Bm[1, 0] * n1g + Bm[1, 1] * n2g) % N
        SIG[j] = acc
    ms = 0.0
    for _ in range(12):
        j = int(rng.integers(1, K))
        n1, n2 = int(rng.integers(0, N)), int(rng.integers(0, N))
        ms = max(ms, abs(np.exp(1j * np.pi * SIG[j][n1, n2] / N)
                         - sigma_direct(j, n1, n2)))
    return dict(fit=[str(s) for s in sol], fit_err=mx, tele_err=ms), Bm, SIG, U


# ------------------------------------------------------- trace phase -------
def rho_tables(N, K, U):
    xs = np.arange(N)
    w = np.exp(2j * np.pi / N)
    b2inv = pow(2, -1, N)
    RH = np.zeros((K, N, N))
    unimod = True
    UJ = U.copy()
    for J in range(1, K):
        t0 = np.trace(UJ)
        # DG[v1, x] = UJ[(x - v1) % N, x]
        idx = (xs[None, :] - xs[:, None]) % N          # [v1, x]
        DG = UJ[idx, xs[None, :]]
        F = N * np.fft.ifft(DG, axis=1)       # sum_x w^{+v2 x}  (exact DFT)
        vals = (w ** ((-b2inv * xs[:, None] * xs[None, :]) % N)) * F
        E, err = to_exp(vals / t0, N)
        if err > 1e-7 or abs(abs(t0) - 1) > 1e-8:
            unimod = False
        RH[J] = E
        UJ = UJ @ U
    return RH, unimod


# ------------------------------------------------------ master assembly ----
def master_validate(A, N, K, U, Bm, SIG, RH, r, F, seed=1):
    rng = np.random.default_rng(seed)
    cs = {n: (rng.normal() + 1j * rng.normal()) / math.sqrt(2) for n in F}
    V = np.zeros((N, N), dtype=complex)
    for n, cc in cs.items():
        V += cc * weyl_matrix(n[0] % N, n[1] % N, N)
        V += np.conj(cc) * weyl_matrix((-n[0]) % N, (-n[1]) % N, N)
    Xv, Vbar = V.copy(), np.zeros_like(V)
    for _ in range(K):
        Vbar += Xv
        Xv = U @ Xv @ U.conj().T
    Vbar /= K
    a_r = float(np.real(np.trace(np.linalg.matrix_power(Vbar, r)))) / N

    terms = []
    for n, cc in cs.items():
        terms.append((cc, +1, np.array(n, dtype=np.int64) % N))
        terms.append((np.conj(cc), -1, np.array(n, dtype=np.int64) % N))
    L = len(terms)
    G = np.empty((L, K, 2), dtype=np.int64)
    CO = np.empty(L * K, dtype=complex)
    SPH = np.empty(L * K)                    # eps_i Q_{j_i}(n_i) exponent
    for si, (cf, ep, nv) in enumerate(terms):
        cur = nv.copy()
        for j in range(K):
            G[si, j] = (ep * cur) % N        # eps * B^j n
            CO[si * K + j] = cf
            SPH[si * K + j] = ep * SIG[j][nv[0], nv[1]]
            cur = Bm @ cur % N               # advance B for next j
    n = L * K
    gg = G.reshape(n, 2)
    # Weyl product rule (machine-established, exhaustive):
    #   T(g)T(h) = zeta^{Psi_d(g,h)} T(g+h),
    #   Psi_d(g,h) = (N+1)*(g2*h1 - g1*h2)  mod 2N.
    PSI = ((N + 1) * (gg[:, 1][:, None] * gg[:, 0][None, :]
                      - gg[:, 0][:, None] * gg[:, 1][None, :])) % (2 * N)
    UPSI = np.exp(1j * np.pi * PSI / N)
    usum2 = (gg[:, None, :] + gg[None, :, :]) % N         # [n,n,2]

    def S_of_J(J):
        rho = RH[J]
        UJ = np.linalg.matrix_power(U, J)
        t0ph = np.trace(UJ) / abs(np.trace(UJ))
        if r == 2:
            u = usum2.reshape(-1, 2)
            ph = SPH[:, None] + SPH[None, :] + PSI
            val = np.sum(CO[:, None] * CO[None, :] * UPSI
                         * np.exp(1j * np.pi
                                  * rho[u[:, 0], u[:, 1]].reshape(n, n) / N)
                         ) * t0ph
            return complex(val) / K ** r
        if r == 3:
            ph2 = SPH[:, None] + SPH[None, :] + PSI
            base2 = CO[:, None] * CO[None, :]              # no pair phase here
            u2 = usum2
            tot = 0.0 + 0j
            for c3 in range(n):
                u3 = (u2 + gg[c3][None, None, :]) % N
                ph3 = (ph2 + SPH[c3]
                       + PSI[:, c3][:, None] + PSI[:, c3][None, :])
                val = np.sum(base2 * CO[c3]
                             * np.exp(1j * np.pi * (ph3 % (2 * N)) / N)
                             * np.exp(1j * np.pi
                                      * rho[u3[:, :, 0], u3[:, :, 1]] / N))
                tot += val
            tot = tot * t0ph
            return complex(tot) / K ** r
        if r == 4:
            # honest quadruple loop, vectorized over (a,b) per (c,d):
            # pairs (a,c),(b,c) absorbed into qc; (a,d),(b,d) into rd;
            # (a,b) into PSI inside qc; (c,d) scalar.
            B2 = CO[:, None] * CO[None, :]
            sphAB = (SPH[:, None] + SPH[None, :] + PSI) % (2 * N)
            eAB = np.exp(1j * np.pi * sphAB / N)
            qcB_all = []
            for c in range(n):
                qc = eAB * np.exp(1j * np.pi
                                  * ((PSI[:, c][:, None]
                                      + PSI[:, c][None, :]) % (2 * N)) / N)
                qcB_all.append(qc * B2)
            tot = 0.0 + 0j
            for c in range(n):
                qcB = qcB_all[c]
                for d in range(n):
                    gd = (gg[c] + gg[d]) % N
                    uu = (usum2 + gd[None, None, :]) % N
                    rv = np.exp(1j * np.pi
                                * rho[uu[:, :, 0], uu[:, :, 1]] / N)
                    rd = np.exp(1j * np.pi * (PSI[:, d] % (2 * N)) / N)
                    scal = (complex(CO[c]) * complex(CO[d])
                            * np.exp(1j * np.pi
                                     * ((float(SPH[c]) + float(SPH[d])
                                         + int(PSI[c, d])) % (2 * N)) / N))
                    tot += scal * np.sum(qcB * np.outer(rd, rd) * rv)
            tot = tot * t0ph
            return complex(tot) / K ** r
        raise ValueError

    SJs = []
    cancel = []
    for J in range(1, K):
        SJ = S_of_J(J)
        SJs.append(SJ)
        mf = float(np.sum(np.abs(CO)) ** r) / K ** r
        cancel.append(dict(J=int(J), absS=abs(SJ), meanfield=mf))
    UK = np.linalg.matrix_power(U, K)
    lam0 = (np.trace(UK) / N) ** (1.0 / K)
    rows = []
    Vr = np.linalg.matrix_power(Vbar, r)
    for jj in (0, 1, 2):
        lam = lam0 * np.exp(2j * np.pi * jj / K)
        Pl = np.zeros_like(U)
        Uj = np.eye(N, dtype=complex)
        for j in range(K):
            Pl += (lam ** (-j)) * Uj
            Uj = U @ Uj
        Pl /= K
        sv = np.linalg.svd(Pl, compute_uv=False)
        m = int(np.sum(sv > 1e-6 * sv.max()))
        lhs = float(np.real(np.trace(Vr @ Pl)))
        rhs = (N / K) * a_r + (1.0 / K) * sum(
            (lam ** (-JJ)) * SJ for JJ, SJ in enumerate(SJs, start=1))
        rhs_re, rhs_im = float(np.real(rhs)), float(np.imag(rhs))
        rows.append(dict(lam_idx=jj, m=m, lhs=lhs, rhs=rhs_re,
                         err_re=abs(lhs - rhs_re), err_im=abs(rhs_im)))
    return rows, cancel


def main():
    t0 = time.time()
    print("=== M1 master moment formula (table-rho version) ===")
    configs = [
        ([2, 1, 1, 1], 101, 2, [(1, 0), (0, 1)]),
        ([2, 1, 1, 1], 101, 3, [(1, 0), (0, 1)]),
        ([2, 1, 1, 1], 101, 3, [(1, 0), (0, 1), (1, 1), (2, 1)]),
        ([2, 1, 1, 1], 199, 3, [(1, 0), (0, 1), (1, 1), (2, 1)]),
        ([2, 1, 1, 1], 521, 4, [(1, 0)]),
        ([2, 1, 1, 1], 101, 4, [(1, 0)]),
        ([2, 1, 1, 1], 199, 4, [(1, 0)]),
        ([2, 1, 1, 1], 521, 4, [(1, 0)]),
        ([3, 1, 2, 1], 101, 3, [(1, 0), (0, 1)]),
        ([3, 1, 2, 1], 101, 4, [(1, 0)]),
    ]
    cache, allpass = {}, True
    for (A, N, r, F) in configs:
        key = (tuple(A), N)
        if key not in cache:
            k, sg = ord_pm(A, N)
            assert k > 0
            K = k if sg > 0 else 2 * k
            info, Bm, SIG, U = cocycle(A, N, K)
            RH, unimod = rho_tables(N, K, U)
            ok_struct = info["fit_err"] < 1e-9 and info["tele_err"] < 1e-9 \
                and unimod
            RES["sigma"].append(dict(A=A, N=N, K=K, **info))
            RES["rho"].append(dict(A=A, N=N, K=K, unimod=unimod))
            print(f"[{'PASS' if ok_struct else 'FAIL'}] structure A={A} N={N} "
                  f"K={K}: sigma fit={info['fit_err']:.1e} "
                  f"tele={info['tele_err']:.1e} rho_unimod={unimod} "
                  f"({time.time()-t0:.0f}s)")
            allpass &= ok_struct
            cache[key] = dict(K=K, U=U, Bm=Bm, SIG=SIG, RH=RH)
        C = cache[key]
        rows, cancel = master_validate(A, N, C["K"], C["U"], C["Bm"], C["SIG"],
                                       C["RH"], r, F)
        ok = bool(rows and
                  all(rr["err_re"] < 1e-6 * max(1.0, abs(rr["lhs"])) and
                      rr["err_im"] < 1e-6 * max(1.0, abs(rr["lhs"]))
                      for rr in rows))
        allpass &= ok
        mf = float(np.mean([abs(c["absS"]) / c["meanfield"] for c in cancel]))
        RES["master"].append(dict(A=A, N=N, r=r, K=C["K"], rows=rows,
                                  passed=ok))
        RES["cancel"].append(dict(A=A, N=N, r=r, mean_absS_over_mf=mf))
        print(f"[{'PASS' if ok else 'FAIL'}] master r={r} A={A} N={N}: " +
              " ".join(f"err=({rr['err_re']:.1e},{rr['err_im']:.1e})"
                       f"[lhs={rr['lhs']:.3f}]" for rr in rows) +
              f"  <|S|>/mf={mf:.2e} ({time.time()-t0:.0f}s)")
    json.dump(RES, open(os.path.join(ART, "master_formula.json"), "w"),
              indent=1, default=str)
    print("saved artifacts/master_formula.json")
    print("ALL PASS" if allpass else "SOME FAIL")


if __name__ == "__main__":
    main()
