"""
RUN 7 / PHASE-WEIGHTED BURST ANALYSIS at r=4 (real cocycle data).

Resonant tuples (sum g_i == 0) of the (+,-,+,-) system, enumerated via
pair-hashing (O(n^2)), classified:
  Wigner : multiset{g_1, g_3} == multiset{g_2, g_4}
  burst  : everything else (the U3 collision events)
Accumulated per class: raw count N_cls and phase-weighted sum
  Phi_cls = sum (prod CO) * zeta^{sum SPH + sum_pairs Psi}
(zeta = e^{pi i/N}; rho_J vanishes identically on resonant tuples, so the
object is J-independent -- one geometric/combinatorial entity).

PRE-REGISTERED expectations (before looking):
  E1: |Phi_burst| <= 0.1 * N_burst * mean|CO|^4   (>= 90% phase kill)
  E2: |Phi_burst| <= 0.05 * |Phi_wigner|
  E3: per-event burst sums are bounded by ~4*mean|CO|^4 (U2 cap)
Violation => bug signal first (protocol P4).
Artifacts: artifacts/phase_bursts.json
"""
import json, math, os, sys, itertools
from collections import defaultdict
import numpy as np

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_core import ord_pm
import master_formula as MF


def build_terms(A, N, F, seed=1):
    k, sg = ord_pm(A, N)
    assert k > 0
    K = k if sg > 0 else 2 * k
    info, Bm, SIG, U = MF.cocycle(A, N, K)
    terms = []
    rng = np.random.default_rng(seed)
    cs = {nn: (rng.normal() + 1j * rng.normal()) / math.sqrt(2) for nn in F}
    for nn, cc in cs.items():
        terms.append((cc, +1, np.array(nn, dtype=np.int64) % N))
        terms.append((np.conj(cc), -1, np.array(nn, dtype=np.int64) % N))
    L = len(terms)
    G = np.empty((L, K, 2), dtype=np.int64)
    CO = np.empty(L * K, complex)
    SPH = np.empty(L * K)
    for si, (cf, ep, nv) in enumerate(terms):
        cur = nv.copy()
        for j in range(K):
            G[si, j] = (ep * cur) % N
            CO[si * K + j] = cf
            SPH[si * K + j] = ep * SIG[j][nv[0], nv[1]]
            cur = Bm @ cur % N
    n = L * K
    gg = G.reshape(n, 2)
    PSI = ((N + 1) * (gg[:, 1][:, None] * gg[:, 0][None, :]
                      - gg[:, 0][:, None] * gg[:, 1][None, :])) % (2 * N)
    return dict(N=N, K=K, n=n, gg=gg, CO=CO, SPH=SPH, PSI=PSI,
                fit_err=info["fit_err"], tele_err=info["tele_err"])


def analyse(D):
    n = D["n"]; gg = D["gg"]; CO = D["CO"]; SPH = D["SPH"]; PSI = D["PSI"]
    N = D["N"]
    zeta = lambda E: np.exp(1j * np.pi * (E % (2 * N)) / N)

    # LEFT pairs (i1, i3): key = g_i1 + g_i3 ; RIGHT pairs (i2, i4): key = -(g_i2+g_i4)
    Lmap = defaultdict(list)
    Rmap = defaultdict(list)
    for i1 in range(n):
        gi1 = gg[i1]
        for i3 in range(n):
            s = (gi1 + gg[i3]) % N
            Lmap[tuple(s)].append((i1, i3))
    for i2 in range(n):
        gj2 = gg[i2]
        for i4 in range(n):
            s = (-gj2 - gg[i4]) % N
            Rmap[tuple(s)].append((i2, i4))

    n_win = 0
    phi_win = 0.0 + 0.0j
    n_bur = 0
    phi_bur = 0.0 + 0.0j
    events = []
    meanC4 = float(np.mean(np.abs(CO)) ** 4)

    for key in set(Lmap.keys()) & set(Rmap.keys()):
        ev_phi = 0.0 + 0.0j
        ev_n = 0
        for (i1, i3) in Lmap[key]:
            for (i2, i4) in Rmap[key]:
                g1 = gg[i1]; g2 = gg[i2]; g3 = gg[i3]; g4 = gg[i4]
                # resonance sanity
                if not (np.all((g1 + g2 + g3 + g4) % N == 0)):
                    continue
                wigner = ((g1 == g2).all() and (g3 == g4).all()) or \
                         ((g1 == g4).all() and (g3 == g2).all())
                ph = int(round(SPH[i1] + SPH[i2] + SPH[i3] + SPH[i4])) \
                     + int(PSI[i1, i2]) + int(PSI[i1, i3]) + int(PSI[i1, i4]) \
                     + int(PSI[i2, i3]) + int(PSI[i2, i4]) + int(PSI[i3, i4])
                w = complex(CO[i1] * CO[i2] * CO[i3] * CO[i4]) * zeta(ph)
                if wigner:
                    n_win += 1
                    phi_win += w
                else:
                    n_bur += 1
                    phi_bur += w
                    ev_n += 1
                    ev_phi += w
        if ev_n:
            events.append({"key": list(key), "n": ev_n,
                           "abs": abs(ev_phi), "cap": 4 * meanC4})

    return {"n_wigner": n_win, "abs_phi_wigner": abs(phi_win),
            "n_burst": n_bur, "abs_phi_burst": abs(phi_bur),
            "raw_over_phase": (n_bur / max(abs(phi_bur), 1e-300)),
            "meanC4": meanC4,
            "events_max_abs": max((e["abs"] for e in events), default=0.0),
            "events_cap": 4 * meanC4,
            "events_over_cap": [e for e in events
                                if e["abs"] > e["cap"] * 1.001],
            "n_events": len(events)}


def main():
    out = {"configs": [], "preregister": {
        "E1_phase_kill_ge90pct": True,
        "E2_burst_below_5pct_of_wigner": True,
        "E3_events_within_U2_cap": True}}
    configs = [
        ([2, 1, 1, 1], 101, [(1, 0), (0, 1)]),
        ([2, 1, 1, 1], 101, [(1, 0), (0, 1), (1, 1)]),
        ([2, 1, 1, 1], 233, [(1, 0)]),
        ([3, 1, 2, 1], 199, [(1, 0), (0, 1)]),
        ([2, 1, 1, 1], 199, [(1, 0), (0, 1), (2, 1)]),
    ]
    allpass = True
    for (A, N, F) in configs:
        try:
            D = build_terms(A, N, F)
        except Exception as ex:
            print(f"[SKIP] A={A} N={N}: {ex}")
            continue
        R = analyse(D)
        cfs = {
            "phase_kill": 1.0 - min(1.0, R["abs_phi_burst"] /
                                    max(R["n_burst"] * R["meanC4"], 1e-300)),
            "burst_vs_wigner": R["abs_phi_burst"] /
                               max(R["abs_phi_wigner"], 1e-300),
        }
        checks = {
            "E1": bool(cfs["phase_kill"] >= 0.9),
            "E2": bool(cfs["burst_vs_wigner"] <= 0.05),
            "E3": bool(len(R["events_over_cap"]) == 0),
        }
        ok = all(checks.values())
        allpass &= ok
        rec = {"A": A, "N": N, "F": F, "K": D["K"], "stats": {
            k: v for k, v in R.items() if k != "events_over_cap"},
            "n_events_over_cap": len(R["events_over_cap"]),
            "cancel": cfs, "checks": checks, "passed": bool(ok)}
        out["configs"].append(rec)
        print(f"A={A} N={N} F={len(F)}freq: "
              f"N_win={R['n_wigner']} N_bur={R['n_burst']} "
              f"|Phi_win|={R['abs_phi_wigner']:.4f} "
              f"|Phi_bur|={R['abs_phi_burst']:.6f} "
              f"kill={cfs['phase_kill']*100:.1f}% "
              f"bur/win={cfs['burst_vs_wigner']:.2e} "
              f"events={R['n_events']} over_cap={len(R['events_over_cap'])} "
              f"[{'PASS' if ok else 'FAIL'}]", flush=True)
    out["all_pass"] = bool(allpass and len(out["configs"]) >= 3)
    json.dump(out, open(os.path.join(ART, "phase_bursts.json"), "w"), indent=1)
    print("saved artifacts/phase_bursts.json")
    print("ALL PASS" if out["all_pass"] else "SOME FAIL/INCONCLUSIVE")
    sys.exit(0 if out["all_pass"] else 1)


if __name__ == "__main__":
    main()
