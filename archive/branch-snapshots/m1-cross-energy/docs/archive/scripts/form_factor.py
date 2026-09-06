"""
SPECTRAL FORM FACTOR of the compression --- the canonical BGS observable.

For unfolded levels x_1..x_m (mean spacing 1) we use
    K(tau) = (1/m) | sum_j w(x_j) e^{2 pi i x_j tau} |^2 / <|w|^2 normalisation>,
with a Gaussian window w to suppress the finite-range edge effect, and we compare
against the identical pipeline applied to GOE/GUE/Poisson spectra of the same
dimension and sample count.  Analytic bulk references (connected part):
    GUE:  K(tau) = tau          (tau <= 1),  1 (tau > 1)
    GOE:  K(tau) = 2 tau - tau*ln(1+2tau)   (tau <= 1)
    Poisson: K(tau) = 1
"""
import numpy as np, math, json, os
from perturb_rmt import build_U, ord_pm

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def weyl_T(N):
    b2 = pow(2, -1, N)
    def T(n1, n2):
        n1 %= N; n2 %= N
        M = np.zeros((N, N), dtype=complex)
        for x in range(N):
            M[x, (x-n1) % N] = np.exp(2j*np.pi*((n2*((x-n1) % N)) % N)/N)
        return np.exp(2j*np.pi*((b2*n1*n2) % N)/N)*M
    return T


def unfold(ev):
    x = np.sort(np.asarray(ev, float)); n = len(x)
    cnt = np.arange(1, n+1)-0.5
    deg = min(12, max(5, n//40))
    return np.polyval(np.polyfit(x, cnt, deg), x)


def form_factor(us, taus, frac=0.6):
    """us: list of unfolded level sets. Gaussian window on the central fraction."""
    acc = np.zeros(len(taus)); cnt = 0
    for u in us:
        n = len(u)
        c = 0.5*(u.min()+u.max()); half = frac*0.5*(u.max()-u.min())
        w = np.exp(-0.5*((u-c)/(half/2))**2)
        norm = np.sum(w**2)
        for i, t in enumerate(taus):
            acc[i] += abs(np.sum(w*np.exp(2j*np.pi*u*t)))**2/norm
        cnt += 1
    return acc/cnt


def spectra_catmap(p, A=(2, 1, 1, 1), Mrev=(1, 0, 1, 1), Lfreq=5, nlam=None, seed=29):
    k, s = ord_pm(list(A), p); K = k if s > 0 else 2*k
    U = build_U(list(A), p); Um = build_U(list(Mrev), p)
    UK = np.linalg.matrix_power(U, K); chi = np.trace(UK)/p; lam0 = chi**(1.0/K)
    lams = [lam0*np.exp(2j*np.pi*j/K) for j in range(K)][:(nlam or K)]
    T = weyl_T(p); rr = np.random.default_rng(seed)
    V = np.zeros((p, p), dtype=complex)
    for n1 in range(-Lfreq, Lfreq+1):
        for n2 in range(-Lfreq, Lfreq+1):
            if (n1, n2) == (0, 0) or (n1, n2) > (-n1, -n2): continue
            c = (rr.normal()+1j*rr.normal())/math.sqrt(2)
            Aa = T(n1, n2); V += c*Aa+np.conj(c)*Aa.conj().T
    V = 0.5*(V+V.conj().T)
    Vs = 0.5*(V + Um@V.conj()@Um.conj().T); Vs = 0.5*(Vs+Vs.conj().T)
    rng = np.random.default_rng(3); nv = int(1.4*p/K+40)
    Wb = (rng.normal(size=(p, nv))+1j*rng.normal(size=(p, nv)))/math.sqrt(2)
    Acc = [np.zeros_like(Wb) for _ in lams]; cur = Wb.copy()
    for j in range(K):
        if j: cur = U@cur
        for i, l in enumerate(lams): Acc[i] += (l**(-j))*cur
    out = {"sym": [], "gen": []}; dims = []
    for i, l in enumerate(lams):
        Q, sv, _ = np.linalg.svd(Acc[i]/K, full_matrices=False)
        m = int(np.sum(sv > 1e-6*sv.max())); B = Q[:, :m]
        if m < 40 or np.linalg.norm(U@B-l*B)/math.sqrt(m) > 1e-6: continue
        dims.append(m)
        for tag, VV in (("gen", V), ("sym", Vs)):
            Vl = B.conj().T@VV@B; Vl = 0.5*(Vl+Vl.conj().T)
            out[tag].append(unfold(np.linalg.eigvalsh(Vl)))
    return out, int(np.median(dims)), len(dims)


def controls(m, reps, taus, seed=5):
    rng = np.random.default_rng(seed); res = {}
    for name in ("GOE", "GUE", "Poisson"):
        us = []
        for _ in range(reps):
            if name == "GUE":
                Z = (rng.normal(size=(m, m))+1j*rng.normal(size=(m, m)))/math.sqrt(2)
                ev = np.linalg.eigvalsh((Z+Z.conj().T)/2)
            elif name == "GOE":
                Z = rng.normal(size=(m, m)); ev = np.linalg.eigvalsh((Z+Z.T)/2)
            else:
                ev = np.sort(rng.uniform(0, 1, m))
            us.append(unfold(ev))
        res[name] = form_factor(us, taus)
    return res


if __name__ == "__main__":
    taus = np.linspace(0.02, 1.6, 33)
    p = 3571
    spec, m, nl = spectra_catmap(p)
    print(f"p={p}: m={m}, {nl} multiplets")
    Kg = form_factor(spec["gen"], taus)
    Ks = form_factor(spec["sym"], taus)
    ctl = controls(m, nl, taus)
    goe_ref = np.where(taus <= 1, 2*taus - taus*np.log(1+2*taus), 1.0)
    gue_ref = np.where(taus <= 1, taus, 1.0)
    print("\n  tau    K_sym    K_GOEctl   GOE_th   |   K_gen    K_GUEctl   GUE_th   | K_Poisctl")
    for i in range(0, len(taus), 2):
        print(f" {taus[i]:5.2f}  {Ks[i]:7.4f}  {ctl['GOE'][i]:8.4f} {goe_ref[i]:8.4f}   | "
              f"{Kg[i]:7.4f}  {ctl['GUE'][i]:8.4f} {gue_ref[i]:8.4f}   | {ctl['Poisson'][i]:7.4f}")
    mk = (taus >= 0.1) & (taus <= 0.9)
    d_sym = float(np.sqrt(np.mean((Ks[mk]-ctl['GOE'][mk])**2)))
    d_gen = float(np.sqrt(np.mean((Kg[mk]-ctl['GUE'][mk])**2)))
    d_cross1 = float(np.sqrt(np.mean((Ks[mk]-ctl['GUE'][mk])**2)))
    d_cross2 = float(np.sqrt(np.mean((Kg[mk]-ctl['GOE'][mk])**2)))
    d_poi_s = float(np.sqrt(np.mean((Ks[mk]-ctl['Poisson'][mk])**2)))
    print(f"\n RMS on tau in [0.1,0.9]:")
    print(f"   sym vs GOE control = {d_sym:.4f}   sym vs GUE control = {d_cross1:.4f}"
          f"   sym vs Poisson = {d_poi_s:.4f}")
    print(f"   gen vs GUE control = {d_gen:.4f}   gen vs GOE control = {d_cross2:.4f}")
    json.dump(dict(p=p, m=m, nl=nl, taus=taus.tolist(), K_sym=Ks.tolist(),
                   K_gen=Kg.tolist(), ctl={k: v.tolist() for k, v in ctl.items()},
                   rms=dict(sym_vs_goe=d_sym, sym_vs_gue=d_cross1, gen_vs_gue=d_gen,
                            gen_vs_goe=d_cross2, sym_vs_poisson=d_poi_s)),
              open(os.path.join(ART, "form_factor.json"), "w"), indent=1)
    print("saved artifacts/form_factor.json")
