"""
MAIN EXPERIMENT: first-order degenerate perturbation theory for the quantised
cat map, and the level statistics of the compression P_lambda V P_lambda.

Rationale.  The Egorov-verified propagator satisfies U^k = chi * U_{+-I}
(k = ord_N(A)), hence its spectrum consists of at most 2k points with
multiplicities ~ N/(2k).  A perturbation  U_eps = U exp(i eps V) splits each
degenerate multiplet, and to first order in eps the splitting is the spectrum
of the compression  V_lambda = P_lambda V P_lambda.  If BGS-type universality
has any deterministic mechanism in this family, it must appear here.

Efficiency: the projectors are applied to a random block, never formed.
        P_lambda = (1/K) sum_{j<K} lambda^{-j} U^j,  K = k or 2k.
All K iterates of one block are streamed, updating every accumulator in one pass.
"""
import numpy as np, math, json, os, sys, time

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
os.makedirs(ART, exist_ok=True)


def build_U(A, N, chunk=512):
    a, b, c, d = A
    icb = pow((2*c) % N, -1, N)
    U = np.empty((N, N), dtype=complex)
    xs = np.arange(N, dtype=np.int64)
    for i0 in range(0, N, chunk):
        i1 = min(N, i0+chunk)
        X = xs[i0:i1][:, None]
        Q = (icb*(d*X*X - 2*X*xs[None, :] + a*xs[None, :]**2)) % N
        U[i0:i1, :] = np.exp(2j*np.pi*Q/N)
    U /= math.sqrt(N)
    return U


def weyl_pair(N):
    """Return the Hermitian observable V = cos(2pi x/N)+cos(2pi xi/N) quantised,
       i.e. (T(1,0)+T(1,0)^dag + T(0,1)+T(0,1)^dag)/2, applied as a function."""
    w = np.exp(2j*np.pi/N)
    diagZ = w**np.arange(N)          # multiplication operator (momentum shift)
    def apply(M):
        # (T(1,0)+T(1,0)^dag)/2 : symmetric shift in x ; here rows are x
        S = 0.5*(np.roll(M, 1, axis=0) + np.roll(M, -1, axis=0))
        # (T(0,1)+T(0,1)^dag)/2 = diag(cos(2pi x/N))
        C = np.cos(2*np.pi*np.arange(N)/N)[:, None]*M
        return S + C
    return apply


def ord_pm(A, N):
    a, b, c, d = [v % N for v in A]
    P = (1, 0, 0, 1)
    for k in range(1, 2*N+3):
        P = ((P[0]*a+P[1]*c) % N, (P[0]*b+P[1]*d) % N,
             (P[2]*a+P[3]*c) % N, (P[2]*b+P[3]*d) % N)
        if P == (1, 0, 0, 1): return k, +1
        if P == (N-1, 0, 0, N-1): return k, -1
    return -1, 0


def unfold_spacings(vals, deg=None):
    x = np.sort(np.asarray(vals, float)); n = len(x)
    if n < 16: return np.array([])
    cnt = np.arange(1, n+1)-0.5
    deg = deg or min(9, max(4, n//20))
    u = np.polyval(np.polyfit(x, cnt, deg), x)
    s = np.diff(u); s = s[s > 0]
    return s/s.mean() if len(s) > 8 else np.array([])


def L1_table(s, bins=60, smax=4.0):
    edges = np.linspace(0, smax, bins+1); mid = 0.5*(edges[:-1]+edges[1:])
    h, _ = np.histogram(s, bins=edges, density=True)
    w1 = (np.pi/2)*mid*np.exp(-np.pi*mid*mid/4)
    w2 = (32/np.pi**2)*mid*mid*np.exp(-4*mid*mid/np.pi)
    po = np.exp(-mid)
    mk = (mid > 0.05) & (mid < 3.5); dw = mid[1]-mid[0]
    ms = (mid > 0.03) & (mid < 0.6) & (h > 1e-4)
    beta = float(np.polyfit(np.log(mid[ms]), np.log(h[ms]), 1)[0]) if ms.sum() > 4 else float('nan')
    return dict(L1_goe=float(np.sum(np.abs(h[mk]-w1[mk])*dw)),
                L1_gue=float(np.sum(np.abs(h[mk]-w2[mk])*dw)),
                L1_poisson=float(np.sum(np.abs(h[mk]-po[mk])*dw)),
                beta=beta, n=int(len(s)), hist=h.tolist(), bins=mid.tolist())


def run(p, A=(2, 1, 1, 1), nvec=None, verbose=True):
    t0 = time.time()
    k, s = ord_pm(list(A), p)
    K = k if s > 0 else 2*k
    U = build_U(list(A), p)
    # chi from U^K = chi * I  (or chi*parity when s<0 and K=k)
    v = np.zeros(p, complex); v[0] = 1.0
    wv = v.copy()
    for _ in range(K): wv = U @ wv
    chi = wv[0]
    lams = [chi**(1.0/K)*np.exp(2j*np.pi*j/K) for j in range(K)]
    m_pred = p/K
    nvec = nvec or int(3*m_pred+40)
    rng = np.random.default_rng(11)
    W = (rng.normal(size=(p, nvec))+1j*rng.normal(size=(p, nvec)))/math.sqrt(2)
    Acc = [np.zeros_like(W) for _ in lams]
    cur = W.copy()
    for j in range(K):
        if j: cur = U @ cur
        for i, lam in enumerate(lams):
            Acc[i] += (lam**(-j))*cur
    for i in range(len(lams)): Acc[i] /= K
    if verbose:
        print(f"p={p} ord={k} sign={s:+d} K={K} |chi|={abs(chi):.4f} "
              f"predicted multiplicity={m_pred:.1f} nvec={nvec} (setup {time.time()-t0:.1f}s)")
    Vapply = weyl_pair(p)
    out = []
    pooled = []
    for i, lam in enumerate(lams):
        Uu, sv, _ = np.linalg.svd(Acc[i], full_matrices=False)
        # true rank: the nonzero singular values of a projector applied to a
        # Gaussian block span a factor ~3, the null ones are ~1e-13.
        m = int(np.sum(sv > 1e-6*sv.max()))
        if m < 16: continue
        B = Uu[:, :m]
        resid = np.linalg.norm(U @ B - lam*B)/math.sqrt(m)
        if resid > 1e-6: continue
        Vl = B.conj().T @ Vapply(B)
        Vl = 0.5*(Vl+Vl.conj().T)
        ev = np.linalg.eigvalsh(Vl)
        sp = unfold_spacings(ev)
        if len(sp) < 8: continue
        pooled.append(sp)
        st = L1_table(sp)
        out.append(dict(lam_index=i, dim=m, resid=float(resid), **{kk: st[kk] for kk in
                        ("L1_goe", "L1_gue", "L1_poisson", "beta", "n")}))
        if verbose:
            print(f"   lam#{i:3d}: dim={m:4d} resid={resid:.1e}  "
                  f"L1 GOE={st['L1_goe']:.3f} GUE={st['L1_gue']:.3f} Poi={st['L1_poisson']:.3f} beta={st['beta']:.2f}")
    allsp = np.concatenate(pooled) if pooled else np.array([])
    tot = L1_table(allsp) if len(allsp) else None
    if verbose and tot:
        print(f"  POOLED {len(out)} multiplets, {tot['n']} spacings:  "
              f"L1 GOE={tot['L1_goe']:.4f}  GUE={tot['L1_gue']:.4f}  Poisson={tot['L1_poisson']:.4f}  beta={tot['beta']:.3f}")
    return dict(p=p, ord=k, sign=s, K=K, per_multiplet=out, pooled=tot,
                elapsed=time.time()-t0)


if __name__ == "__main__":
    ps = [int(x) for x in sys.argv[1:]] or [521]
    res = [run(p) for p in ps]
    json.dump(res, open(os.path.join(ART, "perturbation_rmt.json"), "w"), indent=1)
    print("saved artifacts/perturbation_rmt.json")
