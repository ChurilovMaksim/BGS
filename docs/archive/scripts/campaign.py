"""
RUN 5 CAMPAIGN — mean-spacing-scale statistics from pooled arithmetic multiplets.

Reuses the validated pipeline of largescale.py (FFT propagator, projector
eigenspaces by streaming, matched RMT controls) with three upgrades:

  C1  memory-aware PRIME SCAN: targets m = N/K in [m_lo, m_hi] subject to
      the RAM budget 16*N*(1.25*m+40) <= budget_bytes;
  C2  QR-based orthonormal basis extraction (rank from |R_ii| cut) instead
      of a full SVD -- avoids the second copy of the tall matrix;
  C3  chunked, resumable runs: after every prime the pooled state is dumped
      to artifacts/campaign_state.json; a crash loses at most one prime.

PRE-REGISTRATION (written before any measurement, see preregister.json):
  P1  Theta-invariant observable -> beta in [0.70,1.35], L1(GOE)<L1(GUE);
  P2  generic observable        -> beta in [1.55,2.10], L1(GUE)<L1(GOE);
  P3  Sigma^2(32) <= 1.6 x GOE/GUE control and <= Poisson/10;
  P4  any violated prediction is treated as a BUG SIGNAL first (replicate,
      debug) and only then as a discovery.
"""
import json, math, os, sys, time
import numpy as np
from sympy.ntheory import isprime, factorint
from fast_weil import FastWeil

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from largescale import (matmod, powmod, ord_pm_fast, unfold, L1_table, nvar,
                        weyl_apply_factory, controls)


# ------------------------------------------------------------------ scan ---
def scan_primes(A, plo, phi, m_lo=400, m_hi=2500, budget_bytes=6.0e9,
                max_hits=24):
    hits = []
    for p in range(plo, phi):
        if not isprime(p):
            continue
        k, s = ord_pm_fast(list(A), p)
        if k <= 0:
            continue
        K = k if s > 0 else 2 * k
        m = p / K
        if not (m_lo <= m <= m_hi):
            continue
        nvec = int(1.25 * m + 40)
        if 16 * p * nvec > budget_bytes:
            continue
        hits.append((p, k, s, K, m))
        if len(hits) >= max_hits:
            break
    return hits


# ------------------------------------------------------- eigenspace (QR) ---
def eigenspace_qr(F, lam, K, N, nvec, seed=11):
    rng = np.random.default_rng(seed)
    W = (rng.normal(size=(N, nvec)) + 1j * rng.normal(size=(N, nvec))) / math.sqrt(2)
    Acc = W.copy()
    cur = W
    for j in range(1, K):
        cur = F.apply(cur)
        Acc += (lam ** (-j)) * cur
    Acc /= K
    Q, R = np.linalg.qr(Acc)
    dg = np.abs(np.diag(R))
    m = int(np.sum(dg > 1e-6 * dg.max()))
    B = Q[:, :m]
    resid = float(np.linalg.norm(F.apply(B) - lam * B) / math.sqrt(max(m, 1)))
    del Acc, Q, R
    return B, m, resid


# ------------------------------------------------------ Theta-sym V -------
def make_observable(p, Lfreq=4, seed=29):
    """returns apply_V (generic) and apply_Vsym = (V + Theta V Theta^dag)/2.
    Theta = U_M o conj with M = S*R the standard reversing choice; for the
    Arnold map M = [[1,0],[1,1]].  Uses ONLY operator calculus:
        Theta V Theta^dag X = U_M conj( V( U_M conj(X) ) ).
    The resulting observable is exactly Theta-invariant, so its compression
    into any eigenspace carries the real structure -> beta=1 class."""
    apply_V, terms = weyl_apply_factory(p, Lfreq, seed=seed)
    Mrev = (1, 0, 1, 1)
    Fm = FastWeil(Mrev, p)

    def apply_Vth(X):
        return Fm.apply(np.conj(apply_V(Fm.apply(np.conj(X)))))

    def apply_Vsym(X):
        return 0.5 * (apply_V(X) + apply_Vth(X))

    return apply_V, apply_Vsym


# ------------------------------------------------------------ one prime ----
def run_prime(p, A=(2, 1, 1, 1), Lfreq=4, n_lam=4,
              Ls=(1, 2, 4, 8, 16, 32, 64)):
    t0 = time.time()
    k, s = ord_pm_fast(list(A), p)
    K = k if s > 0 else 2 * k
    F = FastWeil(A, p)
    v = np.zeros(p, complex); v[0] = 1.0
    for _ in range(K):
        v = F.apply(v)
    chi = v[0]
    lam0 = chi ** (1.0 / K)
    m_pred = p / K
    nvec = int(1.25 * m_pred + 40)
    print(f"[campaign] p={p} ord={k} sign={s:+d} K={K} m_pred={m_pred:.0f} "
          f"nvec={nvec} |chi|={abs(chi):.6f}", flush=True)
    apply_V, apply_Vsym = make_observable(p, Lfreq=Lfreq, seed=29)
    pools = {"sym": [], "gen": []}
    unfs = {"sym": [], "gen": []}
    dims = []
    for jj in range(n_lam):
        lam = lam0 * np.exp(2j * np.pi * jj / K)
        B, m, resid = eigenspace_qr(F, lam, K, p, nvec, seed=11 + jj)
        if m < 60 or resid > 1e-6:
            print(f"   lam#{jj}: m={m} resid={resid:.1e} (skipped)", flush=True)
            continue
        dims.append(m)
        VB = apply_V(B)
        Vg = B.conj().T @ VB
        del VB
        VSB = apply_Vsym(B)
        Vsym = B.conj().T @ VSB
        del VSB, B
        Vg = 0.5 * (Vg + Vg.conj().T)
        Vsym = 0.5 * (Vsym + Vsym.conj().T)
        for tag, Mx in (("gen", Vg), ("sym", Vsym)):
            ev = np.linalg.eigvalsh(Mx)
            sp, u = unfold(ev)
            pools[tag].append(sp); unfs[tag].append(u)
        print(f"   lam#{jj}: m={m} resid={resid:.1e} ({time.time()-t0:.0f}s)",
              flush=True)
    out = dict(p=p, ord=k, sign=s, K=K, dims=dims, chi_abs=float(abs(chi)))
    out["spacings"] = {tag: [sp.tolist() for sp in pools[tag]]
                       for tag in ("sym", "gen")}
    out["unfs"] = {tag: [u.tolist() for u in unfs[tag]]
                   for tag in ("sym", "gen")}
    for tag in ("sym", "gen"):
        if not pools[tag]:
            continue
        t = L1_table(np.concatenate(pools[tag]))
        t["nvar"] = nvar(unfs[tag], Ls)
        out[tag] = t
        print(f"   [{tag}] n={t['n']} L1GOE={t['L1_goe']:.4f} "
              f"L1GUE={t['L1_gue']:.4f} L1Poi={t['L1_poisson']:.4f} "
              f"beta={t['beta']:.2f}", flush=True)
        print("          Sigma^2: " +
              "  ".join(f"L{L}={x:.3f}" for L, x in t["nvar"].items()),
              flush=True)
    out["elapsed"] = time.time() - t0
    return out


# ------------------------------------------------------------------ main ---
def main():
    t_start = time.time()
    state_path = os.path.join(ART, "campaign_state.json")
    pre_path = os.path.join(ART, "campaign_preregister.json")
    only_idx = int(sys.argv[1]) if len(sys.argv) > 1 else None

    # ---- PRE-REGISTRATION (before touching data) --------------------------
    pre = {
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "P1_sym_beta": [0.70, 1.35], "P1_sym_order": "L1_goe < L1_gue",
        "P2_gen_beta": [1.55, 2.10], "P2_gen_order": "L1_gue < L1_goe",
        "P3_nvar64": "<= min(1.6*control_nvmax, poisson_nvmax/10)",
        "P4_surprise_protocol": "treat violation as bug first",
        "A": [2, 1, 1, 1], "observable_L": 4,
        "pipeline": "streaming FFT + QR eigenspace + Theta-invariant "
                    "observable (calibrated by calibrate_stream.py 8/8)",
    }
    if not os.path.exists(pre_path):
        json.dump(pre, open(pre_path, "w"), indent=1)
        print("pre-registration written:", pre_path)
    else:
        pre = json.load(open(pre_path))

    # ---- PRIME SCAN --------------------------------------------------------
    print("\n[scan] Arnold map, primes in [30343, 120000], m in [350,2600]")
    hits = scan_primes((2, 1, 1, 1), 30343, 120000, 350, 2600,
                       budget_bytes=6.0e9, max_hits=12)
    for (p, k, s, K, m) in hits:
        print(f"   p={p:7d} ord={k:5d}{s:+d} K={K:5d} m={m:7.1f}")
    if not hits:
        print("no admissible primes found"); sys.exit(1)

    picks = hits[:5]

    # ---- STATE -------------------------------------------------------------
    if os.path.exists(state_path):
        state = json.load(open(state_path))
    else:
        m_ref = int(np.median([h[4] for h in picks]))
        ctl = controls(m_ref, reps=6, Ls=(1, 2, 4, 8, 16, 32, 64))
        state = {"runs": [], "controls": ctl, "preregister": pre}
        json.dump(state, open(state_path, "w"), indent=1)
        print("controls computed and saved")

    done_ps = {r["p"] for r in state["runs"]}
    todo = [(i, h) for i, h in enumerate(picks) if h[0] not in done_ps]
    if only_idx is not None:
        todo = [(i, h) for (i, h) in todo if i == only_idx]
    if not todo:
        print("nothing to do (all picks already in state)")
    for (i, (p, k, s, K, m)) in todo:
        try:
            r = run_prime(p)
        except MemoryError:
            print(f"[campaign] p={p}: MemoryError, skipped", flush=True)
            continue
        state["runs"].append(r)
        json.dump(state, open(state_path, "w"), indent=1)
        print(f"[campaign] state saved ({len(state['runs'])} runs, "
              f"{time.time()-t_start:.0f}s elapsed)", flush=True)

    # ---- POOLED VERDICT (across all primes) --------------------------------
    print("\n[campaign] POOLED verdict:", flush=True)
    pooled_stats = {}
    for tag in ("sym", "gen"):
        sp_all, u_all = [], []
        for r in state["runs"]:
            for sp, u in zip(r.get("spacings", {}).get(tag, []),
                             r.get("unfs", {}).get(tag, [])):
                sp_all.append(np.asarray(sp)); u_all.append(np.asarray(u))
        if not sp_all:
            continue
        t = L1_table(np.concatenate(sp_all))
        t["nvar"] = nvar(u_all, (1, 2, 4, 8, 16, 32, 64))
        pooled_stats[tag] = t
        print(f"   [{tag}] TOTAL levels={t['n']} L1GOE={t['L1_goe']:.4f} "
              f"L1GUE={t['L1_gue']:.4f} beta={t['beta']:.2f}")
        print("          Sigma^2: " +
              "  ".join(f"L{L}={x:.3f}" for L, x in t["nvar"].items()))
    state["pooled"] = pooled_stats

    ok_all = True
    checks = []
    c = state["controls"]
    def g(d, key):
        return d.get(key, d.get(str(key)))
    sym_p, gen_p = pooled_stats.get("sym"), pooled_stats.get("gen")
    cgoe = max(c["GOE"]["nvar"].values())
    cpoi = max(c["Poisson"]["nvar"].values())
    checks_rows = []
    for r in state["runs"]:
        sym, gen = r.get("sym"), r.get("gen")
        if not (sym and gen):
            continue
        c1 = pre["P1_sym_beta"][0] <= sym["beta"] <= pre["P1_sym_beta"][1] \
            and sym["L1_goe"] < sym["L1_gue"]
        c2 = pre["P2_gen_beta"][0] <= gen["beta"] <= pre["P2_gen_beta"][1] \
            and gen["L1_gue"] < gen["L1_goe"]
        nv = g(sym["nvar"], 64)
        c3 = nv is not None and nv <= 1.6 * cgoe and nv <= cpoi / 10
        checks_rows.append({"p": r["p"], "P1": bool(c1), "P2": bool(c2),
                            "P3": bool(c3)})
        ok_all &= (c1 and c2 and c3)
        print(f"   p={r['p']}: P1={c1} P2={c2} P3={c3}")
    if sym_p and gen_p:
        C1 = pre["P1_sym_beta"][0] <= sym_p["beta"] <= pre["P1_sym_beta"][1] \
            and sym_p["L1_goe"] < sym_p["L1_gue"]
        C2 = pre["P2_gen_beta"][0] <= gen_p["beta"] <= pre["P2_gen_beta"][1] \
            and gen_p["L1_gue"] < gen_p["L1_goe"]
        nvp = g(sym_p["nvar"], 64)
        C3 = nvp is not None and nvp <= 1.6 * cgoe and nvp <= cpoi / 10
        checks_rows.append({"pooled": True, "P1": bool(C1), "P2": bool(C2),
                            "P3": bool(C3)})
        ok_all &= (C1 and C2 and C3)
        print(f"   POOLED: P1={C1} P2={C2} P3={C3} "
          f"(GOE ctl nvmax={cgoe:.3f}, Poisson={cpoi:.3f})")
    state["checks"] = checks_rows
    state["prereg_all_pass"] = bool(ok_all)
    json.dump(state, open(state_path, "w"), indent=1)
    print(f"\nPREREGISTERED PREDICTIONS: {'ALL PASS' if ok_all else 'VIOLATION(S)'}")
    print(f"total elapsed {time.time()-t_start:.0f}s")


if __name__ == "__main__":
    main()
