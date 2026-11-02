"""WORKING NOTE, not a deliverable, not the project matrix.
Wave 2 task 4: M04/M05 numerical tests on a MODEL perturbed cat map.

Model definitions (fixed before any run, seeds fixed):
- Classical perturbed cat, eps=0.5, area-preserving:
    y1 = y + (eps/(2*pi))*sin(2*pi*x)  (mod 1)
    (x', y') = (2*x + y1, x + y1)      (mod 1)   [A=[[2,1],[1,1]], det=1]
  Trace of derivative in [2.5, 3.5] for eps=0.5, so uniformly hyperbolic.
- Ulam: side S, M=S^2 cells, 4x4 subpoints per cell, row-stochastic P.
  lambda1 = largest |eigenvalue| of P after 1, via scipy sparse eigs.
- Quantum model (MODEL only): Q[j,k]=N^-1/2 exp(2*pi*i*(j^2-j*k+k^2)/N),
  kick eta=5.0, shift s_r uniform[0,1) per realisation,
  U = D^(1/2) Q D^(1/2), D=diag(exp(i*eta*cos(2*pi*(j+s)/N))).
  U is complex symmetric => COE reference:
    K_COE(tau)=2*tau - tau*log(1+2*tau), tau<1.
  K_N(tau) = mean over realisations and over m in window
    m0=round(tau*N), half-width max(3, round(0.02*N)),
    of |Tr U^m|^2/N. SE from per-realisation window means.
- DBM clocks (M05 4.1): U0=diag(exp(2*pi*i*j/N)).
  Step U <- U @ exp(i*sqrt(dt)*G), G=(A+A^H)/2,
    A=(randn + i*randn)/sqrt(2). Substep dt_sub=0.10/N
    (target rotation sqrt(dt_sub)*sqrt(2*N)=0.447 rad).
  T grid: logspace(1e-3/N, 10/N, 9 points).
  <r> per Atas et al.; KS vs GUE Wigner surmise (proxy for CUE spacing CDF,
  computed by numerical integration on s in [0,5]).
  SE from per-realisation means.
"""
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs

rng_global = np.random.default_rng(0)
EPS = 0.5

# ---------- Test A: Ulam ----------
def classical_map(x, y):
    y1 = (y + (EPS/(2*np.pi))*np.sin(2*np.pi*x)) % 1.0
    return (2*x + y1) % 1.0, (x + y1) % 1.0

def ulam_lambda1(S, sub=4):
    # subpoints
    offs = (np.arange(sub)+0.5)/sub
    xs, ys = [], []
    # build point arrays cell by cell (vectorised over cells via mesh)
    ix, iy = np.meshgrid(np.arange(S), np.arange(S), indexing='ij')
    ix = ix.ravel(); iy = iy.ravel()
    src = np.arange(S*S)
    rows, cols, dat = [], [], []
    for a in offs:
        for b in offs:
            x = (ix + a)/S; y = (iy + b)/S
            xp, yp = classical_map(x, y)
            jx = np.minimum((xp*S).astype(int), S-1)
            jy = np.minimum((yp*S).astype(int), S-1)
            dst = jx + S*jy
            rows.append(np.repeat(src, 1)); cols.append(dst)
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    # aggregate counts
    P = sparse.coo_matrix((np.full(len(rows), 1.0/(sub*sub)), (rows, cols)),
                          shape=(S*S, S*S)).tocsr()
    # row sums should be 1
    rs = np.asarray(P.sum(axis=1)).ravel()
    assert np.allclose(rs, 1.0), rs[:5]
    vals, _ = eigs(P, k=8, which='LM', maxiter=20000, tol=1e-6)
    mags = np.sort(np.abs(vals))[::-1]
    return mags

def classical_corr(nmax=16, npts=60000, seed=1):
    rng = np.random.default_rng(seed)
    x = rng.random(npts); y = rng.random(npts)
    f0 = np.cos(2*np.pi*x)
    var = np.mean(f0**2)
    out = [1.0]
    for n in range(1, nmax+1):
        x, y = classical_map(x, y)
        out.append(float(np.mean(np.cos(2*np.pi*x)*f0)/var))
    return np.array(out)

print("TEST A: Ulam, eps=0.5, sub=4x4")
lam = {}
for S in (50, 100, 200):
    mags = ulam_lambda1(S)
    lam[S] = mags[1]
    print(f"  S={S} M={S*S} |lam0|={mags[0]:.6f} |lam1|={mags[1]:.6f} "
          f"|lam2|={mags[2]:.6f} |lam3|={mags[3]:.6f} |lam4|={mags[4]:.6f}")
print(f"  |lam1| change S=50->100: {abs(lam[100]-lam[50]):.4f}, "
      f"100->200: {abs(lam[200]-lam[100]):.4f}")
corr = classical_corr()
print("  classical corr C(n) for cos(2*pi*x), n=0..16:")
print("   " + " ".join(f"{v:.4f}" for v in corr))
lam1f = lam[200]
print(f"  |lam1|^n (S=200) n=25,50,100,200,300: " +
      " ".join(f"{lam1f**n:.2e}" for n in (25, 50, 100, 200, 300)))

# ---------- Test B: quantum form factor, model ----------
def Qmat(N):
    j = np.arange(N)[:, None]; k = np.arange(N)[None, :]
    return np.exp(2j*np.pi*(j*j - j*k + k*k)/N)/np.sqrt(N)

def Kcoe(tau):
    return 2*tau - tau*np.log(1+2*tau)

def testB(N, R, seed):
    rng = np.random.default_rng(seed)
    Q = Qmat(N)
    j = np.arange(N)
    rows = {}
    for tau in (0.25, 0.5, 0.75):
        m0 = int(round(tau*N)); W = max(3, int(round(0.02*N)))
        ms = np.arange(max(1, m0-W), min(N-1, m0+W)+1)
        per_real = []
        for r in range(R):
            s = rng.random()
            dhalf = np.exp(0.5j*5.0*np.cos(2*np.pi*(j+s)/N))
            U = dhalf[:, None]*Q*dhalf[None, :]
            ev = np.linalg.eigvals(U)
            tr = np.sum(ev[:, None]**ms[None, :], axis=0)
            per_real.append(np.mean(np.abs(tr)**2)/N)
        per_real = np.array(per_real)
        kref = float(np.mean([Kcoe(m/N) for m in ms]))
        rows[tau] = (float(np.mean(per_real)),
                     float(np.std(per_real, ddof=1)/np.sqrt(R)) if R > 1 else 0.0,
                     kref, m0, W)
    return rows

print("TEST B: quantum form factor, MODEL Q + eta=5 kick, shift ensemble, COE ref")
for N, R, seed in ((100, 20, 11), (200, 12, 12), (400, 8, 13)):
    rows = testB(N, R, seed)
    for tau in (0.25, 0.5, 0.75):
        K, se, kref, m0, W = rows[tau]
        print(f"  N={N} R={R} tau={tau} m0={m0} W={W} "
              f"K={K:.4f} +- {se:.4f} K_COE={kref:.4f} |dK|={abs(K-kref):.4f} "
              f"|lam1|^m0={lam1f**m0:.2e}")

# ---------- DBM clocks ----------
# GUE-surmise CDF on grid
_s = np.linspace(0, 5, 5001)
_p = (32/np.pi**2)*_s**2*np.exp(-4*_s**2/np.pi)
_cdf = np.concatenate([[0.0], np.cumsum(0.5*(_p[1:]+_p[:-1])*np.diff(_s))])
_cdf = _cdf/_cdf[-1]
def ks_cue(spacings):
    sp = np.sort(spacings)
    F = np.interp(sp, _s, _cdf)
    emp = np.arange(1, len(sp)+1)/len(sp)
    return float(np.max(np.maximum(np.abs(emp-F), np.abs((np.arange(len(sp)))/len(sp)-F))))

def spacing_ratios(phases):
    ph = np.sort(phases % (2*np.pi))
    d = np.diff(np.concatenate([ph, ph[:1]+2*np.pi]))
    d = d/(2*np.pi/len(ph))
    r = np.minimum(d[:-1], d[1:])/np.maximum(d[:-1], d[1:])
    return d, r

def dbm_clocks(N, R, seed):
    rng = np.random.default_rng(seed)
    Ts = np.logspace(np.log10(1e-3/N), np.log10(10/N), 9)
    dt_sub = 0.10/N
    results = []
    for T in Ts:
        pass
    # cumulative evolution per realisation
    acc = {float(T): [] for T in Ts}
    accK = {float(T): [] for T in Ts}
    for r in range(R):
        U = np.diag(np.exp(2j*np.pi*np.arange(N)/N))
        prev = 0.0
        for T in Ts:
            dt_tot = T - prev; prev = T
            nsub = max(1, int(np.ceil(dt_tot/dt_sub)))
            dt = dt_tot/nsub
            sq = np.sqrt(dt)
            for _ in range(nsub):
                A = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/np.sqrt(2)
                G = 0.5*(A + A.conj().T)
                w, V = np.linalg.eigh(G)
                U = U @ (V*np.exp(1j*sq*w)[None, :]) @ V.conj().T
            ev = np.linalg.eigvals(U)
            d, rr = spacing_ratios(np.angle(ev))
            acc[float(T)].append(float(np.mean(rr)))
            accK[float(T)].append([ks_cue(d)] +
                                 [abs(np.sum(ev**m))**2/N for m in (1, 2, 5)])
            # K(1),K(2),K(5) stored separately below via trace? recompute from ev
            # (store in accK as tuple not possible; handled in second pass structure)
        # note: K(m) for clocks computed in a lighter separate loop below
    out = []
    for T in Ts:
        a = np.array(acc[float(T)])
        b = np.array(accK[float(T)])
        out.append((float(T), float(np.mean(a)),
                    float(np.std(a, ddof=1)/np.sqrt(R)) if R > 1 else 0.0) +
                   tuple(float(np.mean(b[:, k])) for k in range(4)) +
                   tuple(float(np.std(b[:, k], ddof=1)/np.sqrt(R)) if R > 1 else 0.0
                         for k in range(4)))
    return out, Ts

def dbm_clocks_K(N, R, seed):
    # Same evolution, but report K(1),K(2),K(5) at final T only is not enough;
    # do a fresh, shorter run recording K at each grid T.
    rng = np.random.default_rng(seed)
    Ts = np.logspace(np.log10(1e-3/N), np.log10(10/N), 9)
    dt_sub = 0.10/N
    rec = {float(T): [] for T in Ts}
    for r in range(R):
        U = np.diag(np.exp(2j*np.pi*np.arange(N)/N))
        prev = 0.0
        for T in Ts:
            dt_tot = T - prev; prev = T
            nsub = max(1, int(np.ceil(dt_tot/dt_sub)))
            dt = dt_tot/nsub; sq = np.sqrt(dt)
            for _ in range(nsub):
                A = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/np.sqrt(2)
                G = 0.5*(A + A.conj().T)
                w, V = np.linalg.eigh(G)
                U = U @ (V*np.exp(1j*sq*w)[None, :]) @ V.conj().T
            ev = np.linalg.eigvals(U)
            rec[float(T)].append([abs(np.sum(ev**m))**2/N for m in (1, 2, 5)])
    out = []
    for T in Ts:
        a = np.array(rec[float(T)])
        out.append((float(T),) + tuple(float(np.mean(a[:, k])) for k in range(3)) +
                   tuple(float(np.std(a[:, k], ddof=1)/np.sqrt(R)) if R > 1 else 0.0 for k in range(3)))
    return out

print("DBM CLOCKS: <r> and KS vs GUE surmise; CUE <r> ref 0.60266, clock <r>=1.0")
for N, R, seed in ((61, 20, 21), (128, 10, 22), (256, 5, 23)):
    out, Ts = dbm_clocks(N, R, seed)
    for (T, mr, se, ks, k1, k2, k5, s_ks, s1, s2, s5) in out:
        print(f"  N={N} R={R} T={T:.6g} <r>={mr:.4f} +- {se:.4f} KS={ks:.4f} +- {s_ks:.4f} "
              f"K1={k1:.4f} +- {s1:.4f} K2={k2:.4f} +- {s2:.4f} K5={k5:.4f} +- {s5:.4f}")
print("DONE")
