"""
LARGE-SCALE TEST at multiplicity ~600 using the FFT-based propagator.
Finds primes with very small ord_N(A) (hence very large multiplicity m = N/K),
builds a few eigenspaces by streaming the projector, and measures the statistics
of the compression against matched controls.
"""
import numpy as np, math, json, os, sys, time
from sympy.ntheory import isprime, factorint
from fast_weil import FastWeil

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def matmod(X, Y, p):
    return ((X[0]*Y[0]+X[1]*Y[2]) % p, (X[0]*Y[1]+X[1]*Y[3]) % p,
            (X[2]*Y[0]+X[3]*Y[2]) % p, (X[2]*Y[1]+X[3]*Y[3]) % p)


def powmod(A, e, p):
    R = (1, 0, 0, 1); B = tuple(x % p for x in A)
    while e:
        if e & 1: R = matmod(R, B, p)
        B = matmod(B, B, p); e >>= 1
    return R


def ord_pm_fast(A, p):
    """least k with A^k = +-I mod p, using divisors of p-1 or p+1."""
    I = (1, 0, 0, 1); mI = ((p-1) % p, 0, 0, (p-1) % p)
    for base in (p-1, p+1, 2*(p-1), 2*(p+1)):
        if powmod(A, base, p) not in (I, mI): continue
        divs = [1]
        for q, e in factorint(base).items():
            divs = [d*q**i for d in divs for i in range(e+1)]
        for k in sorted(set(divs)):
            r = powmod(A, k, p)
            if r == I: return k, +1
            if r == mI: return k, -1
    return -1, 0


def unfold(vals):
    x = np.sort(np.asarray(vals, float)); n = len(x)
    cnt = np.arange(1, n+1)-0.5
    deg = min(12, max(5, n//40))
    u = np.polyval(np.polyfit(x, cnt, deg), x)
    s = np.diff(u); s = s[s > 0]
    return s/s.mean(), u


def L1_table(s, bins=80, smax=4.0):
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
                beta=beta, n=int(len(s)))


def nvar(us, Ls):
    out = {}
    for L in Ls:
        vals = []
        for u in us:
            if len(u) < 5*L: continue
            lo, hi = u.min(), u.max()-L
            if hi <= lo: continue
            st = np.linspace(lo, hi, 80)
            vals.append(np.var([np.sum((u >= t) & (u < t+L)) for t in st]))
        if vals: out[L] = float(np.mean(vals))
    return out


def weyl_apply_factory(N, L, seed=29):
    rng = np.random.default_rng(seed)
    terms = []
    for n1 in range(-L, L+1):
        for n2 in range(-L, L+1):
            if (n1, n2) == (0, 0) or (n1, n2) > (-n1, -n2): continue
            terms.append((n1, n2, (rng.normal()+1j*rng.normal())/math.sqrt(2)))
    b2 = pow(2, -1, N); xs = np.arange(N, dtype=np.int64)
    def T(n1, n2, X):
        n1 %= N; n2 %= N
        Y = np.roll(X, n1, axis=0)
        ph = np.exp(2j*np.pi*(((b2*n1*n2) % N)/N))*np.exp(-2j*np.pi*(((n1*n2) % N)/N))
        return ph*np.exp(2j*np.pi*((n2*xs) % N)/N)[:, None]*Y
    def apply_V(X):
        Y = np.zeros_like(X)
        for (n1, n2, c) in terms:
            Y += c*T(n1, n2, X) + np.conj(c)*T(-n1, -n2, X)
        return Y
    return apply_V, terms


def eigenspace(F, lam, K, N, nvec, seed=11):
    rng = np.random.default_rng(seed)
    W = (rng.normal(size=(N, nvec))+1j*rng.normal(size=(N, nvec)))/math.sqrt(2)
    Acc = W.copy(); cur = W
    for j in range(1, K):
        cur = F.apply(cur)
        Acc = Acc + (lam**(-j))*cur
    Acc /= K
    Q, sv, _ = np.linalg.svd(Acc, full_matrices=False)
    m = int(np.sum(sv > 1e-6*sv.max()))
    B = Q[:, :m]
    resid = np.linalg.norm(F.apply(B) - lam*B)/math.sqrt(max(m, 1))
    return B, m, float(resid)


def run(p, A=(2, 1, 1, 1), Mrev=(1, 0, 1, 1), Lfreq=5, n_lam=3, Ls=(1, 2, 4, 8, 16, 32)):
    t0 = time.time()
    k, s = ord_pm_fast(list(A), p); K = k if s > 0 else 2*k
    F = FastWeil(A, p); Fm = FastWeil(Mrev, p)
    e = np.zeros(p, complex); e[0] = 1.0
    v = e.copy()
    for _ in range(K): v = F.apply(v)
    chi = v[0]
    lam0 = chi**(1.0/K)
    m_pred = p/K
    nvec = int(1.25*m_pred+40)
    print(f"p={p}  ord={k} sign={s:+d}  K={K}  m_pred={m_pred:.0f}  nvec={nvec}  |chi|={abs(chi):.4f}")
    apply_V, _ = weyl_apply_factory(p, Lfreq)
    pools = {"sym": [], "gen": []}; unfs = {"sym": [], "gen": []}; dims = []
    for jj in range(n_lam):
        lam = lam0*np.exp(2j*np.pi*jj/K)
        B, m, resid = eigenspace(F, lam, K, p, nvec, seed=11+jj)
        if m < 50 or resid > 1e-6:
            print(f"   lam#{jj}: m={m} resid={resid:.1e}  (skipped)"); continue
        dims.append(m)
        # Theta-conjugate basis: E = conj(Um^dag B) = conj( (Fm^dag) B )
        # Fm^dag B = conj(Fm.apply(conj(B)))  since Fm is unitary with real-kernel structure
        FmB = Fm.apply(B.conj()).conj()          # = conj(Um) B ... use exact adjoint below
        # exact adjoint: U^dag X = conj( U conj(X) ) only if U symmetric; verify instead:
        E = np.conj(FmB)
        Vg = B.conj().T @ apply_V(B); Vg = 0.5*(Vg+Vg.conj().T)
        Ve = np.conj(E.conj().T @ apply_V(E)); Ve = 0.5*(Ve+Ve.conj().T)
        Vs = 0.5*(Vg+Ve)
        for tag, Mx in (("gen", Vg), ("sym", Vs)):
            ev = np.linalg.eigvalsh(0.5*(Mx+Mx.conj().T))
            sp, u = unfold(ev)
            pools[tag].append(sp); unfs[tag].append(u)
        print(f"   lam#{jj}: m={m} resid={resid:.1e}  ({time.time()-t0:.0f}s)")
    out = dict(p=p, ord=k, sign=s, K=K, dims=dims)
    for tag in ("sym", "gen"):
        if not pools[tag]: continue
        t = L1_table(np.concatenate(pools[tag]))
        t["nvar"] = nvar(unfs[tag], Ls)
        out[tag] = t
        print(f"   [{tag}] n={t['n']:5d} L1 GOE={t['L1_goe']:.4f} GUE={t['L1_gue']:.4f} "
              f"Poi={t['L1_poisson']:.4f} beta={t['beta']:.2f}")
        print(f"          Sigma^2: " + "  ".join(f"L{L}={x:.3f}" for L, x in t["nvar"].items()))
    out["elapsed"] = time.time()-t0
    return out


def controls(m, reps, Ls=(1, 2, 4, 8, 16, 32), seed=7):
    rng = np.random.default_rng(seed); res = {}
    for name in ("GOE", "GUE", "Poisson"):
        pool = []; unfs = []
        for _ in range(reps):
            if name == "GUE":
                Z = (rng.normal(size=(m, m))+1j*rng.normal(size=(m, m)))/math.sqrt(2)
                ev = np.linalg.eigvalsh((Z+Z.conj().T)/2)
            elif name == "GOE":
                Z = rng.normal(size=(m, m)); ev = np.linalg.eigvalsh((Z+Z.T)/2)
            else:
                ev = np.sort(rng.uniform(0, 1, m))
            sp, u = unfold(ev); pool.append(sp); unfs.append(u)
        t = L1_table(np.concatenate(pool)); t["nvar"] = nvar(unfs, Ls)
        res[name] = t
        print(f"  {name:8s} L1 GOE={t['L1_goe']:.4f} GUE={t['L1_gue']:.4f} Poi={t['L1_poisson']:.4f}"
              f" beta={t['beta']:.2f}\n           Sigma^2: " +
              "  ".join(f"L{L}={x:.3f}" for L, x in t["nvar"].items()))
    return res


if __name__ == "__main__":
    print("scanning large primes for very small ord (large multiplicity)...")
    cands = []
    for p in [9349, 28657, 3010349, 514229, 24476221, 1346269]:
        if not isprime(p): continue
        k, s = ord_pm_fast([2, 1, 1, 1], p); K = k if s > 0 else 2*k
        cands.append((p/K, p, k, s, K))
    cands.sort(reverse=True)
    for r, p, k, s, K in cands:
        print(f"   p={p:9d} ord={k:6d} sign={s:+d} K={K:6d}  m={r:9.1f}")
    target = [c for c in cands if 300 <= c[0] <= 1200]
    res = []
    for r, p, k, s, K in target[:1]:
        res.append(run(p))
    m0 = int(np.median(res[0]["dims"])) if res else 600
    print(f"\nCONTROLS at m={m0}, 3 reps:")
    ctl = controls(m0, 3)
    json.dump(dict(runs=res, controls=ctl, m=m0),
              open(os.path.join(ART, "largescale.json"), "w"), indent=1)
    print("saved artifacts/largescale.json")
