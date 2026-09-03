"""
CALIBRATION GATE for the streaming pipeline (run-5 campaign).

Validates, against the independently verified full-matrix constructions
(the code path behind run-2/3 results):

  G1  sparse Weyl application == explicit T(n) matrices (same coefficients);
  G2  Theta-action identity  Theta V Theta^dag = U_M conj(V(U_M conj(.)))
      holds operator-wise (residual ~ machine eps);
  G3  the Theta-symmetrised observable is exactly Theta-invariant;
  G4  streaming eigenspace (QR path) reproduces the full-projector spectrum
      of the SAME multiplet to spectral accuracy;
  G5  the compression of the Theta-invariant observable has vanishing
      imaginary part in the Theta-adapted (real) basis -- the GOE witness
      used by run-2 T4.

Run: py -3 src/calibrate_stream.py     exit 0 iff all gates pass.
"""
import math, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fast_weil import FastWeil, U_explicit
from catmap_core import ord_pm, U_cat, weyl
from campaign import make_observable, eigenspace_qr

PASS = []


def ok(tag, cond, detail):
    PASS.append((tag, bool(cond), detail))
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}: {detail}")


def build_terms(L, seed):
    rng = np.random.default_rng(seed)
    terms = []
    for n1 in range(-L, L + 1):
        for n2 in range(-L, L + 1):
            if (n1, n2) == (0, 0) or (n1, n2) > (-n1, -n2):
                continue
            terms.append((n1, n2, (rng.normal() + 1j * rng.normal()) / math.sqrt(2)))
    return terms


def apply_terms_sparse(N, terms, X):
    b2 = pow(2, -1, N)
    xs = np.arange(N, dtype=np.int64)
    ramp = np.exp(2j * np.pi * (xs % N) / N)

    def T(n1, n2, X):
        n1 %= N; n2 %= N
        Y = np.roll(X, n1, axis=0)
        ph = np.exp(2j * np.pi * (((b2 * n1 * n2 - n1 * n2) % N) / N))
        return ph * np.exp(2j * np.pi * ((n2 * xs) % N) / N)[:, None] * Y

    Y = np.zeros_like(X)
    for (n1, n2, c) in terms:
        Y += c * T(n1, n2, X) + np.conj(c) * T(-n1, -n2, X)
    return Y


def main():
    A = [2, 1, 1, 1]
    N = 199
    k, s = ord_pm(A, N); K = k if s > 0 else 2 * k
    L = 4
    seed = 29

    # ---- G1: sparse vs explicit Weyl operators --------------------------
    Tfull = weyl(N)
    terms = build_terms(L, seed)
    rngX = np.random.default_rng(3)
    X = (rngX.normal(size=(N, 3)) + 1j * rngX.normal(size=(N, 3))) / math.sqrt(2)
    Ysp = apply_terms_sparse(N, terms, X)
    Yex = np.zeros_like(X)
    for (n1, n2, c) in terms:
        Yex += c * Tfull(n1 % N, n2 % N) @ X + np.conj(c) * Tfull((-n1) % N, (-n2) % N) @ X
    e1 = np.linalg.norm(Ysp - Yex) / np.linalg.norm(Yex)
    ok("G1 sparse Weyl apply == explicit matrices", e1 < 1e-12, f"rel={e1:.2e}")

    # ---- full-matrix observables ----------------------------------------
    Vg_full = np.zeros((N, N), complex)
    for (n1, n2, c) in terms:
        Vg_full += c * Tfull(n1 % N, n2 % N) + np.conj(c) * Tfull((-n1) % N, (-n2) % N)
    Vg_full = 0.5 * (Vg_full + Vg_full.conj().T)

    Um = U_cat([1, 0, 1, 1], N)

    def th_op(Zmat_or_vec):                 # anti-linear action on columns
        return Um @ np.conj(Zmat_or_vec)

    def Vth_apply(Xfull):
        return th_op(Vg_full @ th_op(Xfull))

    Xc = (rngX.normal(size=(N, 2)) + 1j * rngX.normal(size=(N, 2)))
    Vth_mat_num = Vth_apply(np.eye(N))       # column-wise reconstruction
    # closed form: Theta V Theta^dag psi = Um conj( V( conj(Um^dag psi) ) )
    #   => matrix = Um @ conj(V) @ Um^dag     (Theta^2=+1 makes Th^dag=Th)
    Vth_cf = Um @ np.conj(Vg_full) @ Um.conj().T
    e2 = np.linalg.norm(Vth_mat_num - Vth_cf) / np.linalg.norm(Vth_mat_num)
    ok("G2 Theta V Theta^dag = Um conj(V) Um (operator identity)", e2 < 1e-12,
       f"rel={e2:.2e}")

    Vsym_full = 0.5 * (Vg_full + Vth_cf)
    res_th = np.linalg.norm(th_op(Vsym_full @ th_op(np.eye(N))) - Vsym_full) / \
        np.linalg.norm(Vsym_full)
    ok("G3 Theta-invariance of symmetrised observable", res_th < 1e-12,
       f"rel={res_th:.2e}")

    # ---- streaming counterparts -----------------------------------------
    apply_V, apply_Vsym = make_observable(N, Lfreq=L, seed=seed)
    # NOTE: make_observable builds its own term list with the same seed/L ->
    # identical coefficients to `terms` (same generation order).
    e3 = np.linalg.norm(apply_V(X) - Vg_full @ X) / np.linalg.norm(Vg_full @ X)
    ok("G3b streaming generic V == full V", e3 < 1e-12, f"rel={e3:.2e}")
    e4 = np.linalg.norm(apply_Vsym(X) - Vsym_full @ X) / np.linalg.norm(Vsym_full @ X)
    ok("G3c streaming Theta-sym V == full V_sym", e4 < 1e-12, f"rel={e4:.2e}")

    # ---- G4: streaming eigenspace spectrum vs full projector -------------
    F = FastWeil(A, N)
    U = U_cat(A, N)
    v = np.zeros(N, complex); v[0] = 1.0
    for _ in range(K):
        v = F.apply(v)
    chi = v[0]
    lam0 = chi ** (1.0 / K)
    lam = lam0
    nvec = int(1.25 * (N / K) + 40)
    Bs, m, resid = eigenspace_qr(F, lam, K, N, nvec, seed=11)
    # full projector
    P = np.eye(N, dtype=complex)
    cur = P.copy()
    acc = P.copy()
    for j in range(1, K):
        cur = U @ cur
        acc += (lam ** (-j)) * cur
    Pf = acc / K
    Vl_full = Pf @ (Vg_full @ Pf)
    ev_all = np.linalg.eigvalsh(0.5 * (Vl_full + Vl_full.conj().T))
    tol = 1e-9 * max(1.0, np.abs(ev_all).max())
    ev_ref = np.sort(ev_all[np.abs(ev_all) > tol])
    ev_str = np.sort(np.linalg.eigvalsh(Bs.conj().T @ Vg_full @ Bs))
    dev = max(abs(ev_ref - ev_str)) if len(ev_ref) == len(ev_str) else float("inf")
    ok("G4 streaming spectrum == full projector spectrum", dev < 1e-8,
       f"m={m}, resid={resid:.1e}, max|dev|={dev:.2e}")

    # ---- G5: real structure witness for the Theta-invariant V ------------
    # Theta-adapted basis inside H_lam: W = B^dag Um conj(B); Q=W^{1/2};
    # compression of Vsym in basis BQ must be real symmetric.
    Wm = Bs.conj().T @ Um @ Bs.conj()
    import scipy.linalg as sla
    Qh = sla.sqrtm(Wm)
    C = Bs @ Qh
    Vs_c = C.conj().T @ (Vsym_full @ C)
    imr = np.linalg.norm(Vs_c.imag) / np.linalg.norm(Vs_c)
    ok("G5 real structure: Im(Vsym_compression)/||.|| ~ 0", imr < 1e-10,
       f"ratio={imr:.2e}")
    # generic-V control: in the SAME adapted basis it should NOT be real
    Vg_c = Bs.conj().T @ (Vg_full @ Bs)
    Vg_ad = Qh.conj().T @ Vg_c @ Qh
    imr_g = np.linalg.norm(Vg_ad.imag) / np.linalg.norm(Vg_ad)
    ok("G5b control: generic V not real in adapted basis", imr_g > 0.05,
       f"ratio={imr_g:.2e}")

    print("\n" + "=" * 60)
    n_ok = sum(1 for _, o, _ in PASS if o)
    print(f"CALIBRATION: {n_ok}/{len(PASS)} gates PASS")
    print("=" * 60)
    sys.exit(0 if n_ok == len(PASS) else 1)


if __name__ == "__main__":
    main()
