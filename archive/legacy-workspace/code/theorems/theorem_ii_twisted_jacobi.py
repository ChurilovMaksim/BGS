"""
Run 82j: THE FAMILY IN CLOSED FORM -- matrix elements as twisted Jacobi sums.
===========================================================================
After Theorem I (R82.2) and the certified normal form (R82.10), BGS for this
family is a local law for a single matrix `M_q` whose entries are the Hecke-basis
matrix elements of a Weyl operator.  This run derives those entries in closed
form and verifies the derivation against the workspace's own matrices.

DERIVATION (split prime; conventions read off src/catmap_independent.py).
Conjugating by an element of SL_2(Z/N) we may take the cat map diagonal,
`A' = diag(a, a^{-1})` with `a^2 - t a + 1 = 0` and `ord(a) = K`.  Then:

  * the centraliser torus is `T = {diag(u, u^{-1})}`, its invariant form is
    `Q'(n) = n_1 n_2`, and the Weil operators act by dilation,
        (U_u psi)(x) = leg(u) psi(u^{-1} x),      leg = Legendre symbol,
    so the HECKE BASIS is literally the multiplicative characters,
        f_chi(x) = chi(x)/sqrt(N-1)  (x != 0),  f_chi(0) = 0,
    with `U_u f_chi = leg(u) chi(u)^{-1} f_chi`;
  * a `U_{A'}`-eigenspace is `{chi : chi(a) = const}`, of dimension
    `m = (N-1)/K`; parity is `R = U_{-1}`, so `R f_chi = leg(-1) chi(-1) f_chi`
    and the parity blocks are the even / odd characters, `m_+- = m/2`;
  * with the workspace convention
        (T(n)psi)(x) = e_N(n_2 x - n_1 n_2 / 2) psi(x - n_1),
    which satisfies `T(-n) = T(n)^*` exactly, and writing `q = n_1 n_2`,
        <f_chi | T(n) | f_psi>
          = e_N(-q/2) . conj(chi)(n_1) psi(n_1) . J(chi, psi; q) / (N-1),
        J(chi, psi; q) = sum_{x != 0, 1} conj(chi)(x) psi(x-1) e_N(q x).

`J` is a TWISTED JACOBI SUM (a Jacobi sum with an additive twist), bounded by
Weil/Deligne by `2 sqrt N` for nontrivial characters.  Two consequences are
immediate and were previously only measured:

  * the modulus `|<f_chi|T(n)|f_psi>| = |J(chi,psi;q)|/(N-1)` depends on `n`
    ONLY through `q` -- Theorem I, now with an explicit reason;
  * the `n`-dependence inside a level set is the coboundary
    `conj(chi)(n_1) psi(n_1) = theta_chi conj(theta_psi)` -- exactly the
    diagonal conjugation certified in R82.10.

VERIFICATION performed here: build `M_q = C + C^*` from the `J` sums alone (no
N x N linear algebra, no randomised eigenbasis) and compare its SPECTRUM with
the spectra computed by the workspace pipeline, over the exhaustive q-curve
stored in artifacts/r82/q_curve_N*.npz.  The two models are related by
`q_workspace = c . q'` for one constant `c` fixed by the conjugating matrix, so
the test is: does the closed-form mu_4 curve coincide with the measured one
after the single rescaling `q -> q/c`?

Output: artifacts/r82/closed_form.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

T_TRACE = 3


def sqrt_mod(a, p):
    """all square roots of a mod p (p odd prime)."""
    a %= p
    if a == 0:
        return [0]
    if pow(a, (p - 1) // 2, p) != 1:
        return []
    if p % 4 == 3:
        r = pow(a, (p + 1) // 4, p)
        return sorted({r, (-r) % p})
    # Tonelli-Shanks
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t = t * c % p
        r = r * b % p
    return sorted({r, (-r) % p})


def multiplicative_order(a, p):
    x, k = a % p, 1
    while x != 1:
        x = x * a % p
        k += 1
        if k > p:
            return None
    return k


def primitive_root(p):
    from sympy import factorint
    fac = list(factorint(p - 1))
    g = 2
    while True:
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
            return g
        g += 1


def build_closed_form(N, K, a, k0, parity_odd, qs):
    """Spectra of M_{q'} for the closed-form model, for each q' in `qs`."""
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    # characters chi_k with k = k0 mod K, and the requested parity (k odd/even)
    ks = np.array([k for k in range(N - 1)
                   if k % K == k0 % K and (k % 2 == 1) == parity_odd],
                  dtype=np.int64)
    m = len(ks)
    xs = np.array([x for x in range(N) if x != 0 and x != 1], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    # W[i, x] = conj(chi_{k_i})(x),  V[j, x] = chi_{k_j}(x-1)
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    Vv = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
    out = {}
    for qp in qs:
        ph = np.exp(2j * np.pi * (qp * xs % N) / N)
        Jm = (W * ph) @ Vv.T                      # J[i, j]
        C = np.exp(-2j * np.pi * (pow(2, N - 2, N) * qp % N) / N) * Jm / (N - 1)
        M = C + C.conj().T
        ev = np.linalg.eigvalsh(M)
        e = ev - ev.mean()
        s2 = (e ** 2).mean()
        e = e / np.sqrt(s2)
        out[int(qp)] = {"m": m, "s2": float(s2), "mu4": float((e ** 4).mean()),
                        "mu6": float((e ** 6).mean()),
                        "tr2": float((ev ** 2).sum())}
    return out, m


def main():
    out = {"script": "src/r82j_closed_form.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, K in ((199, 11), (3571, 17)):
        t0 = time.time()
        roots = [r for r in sqrt_mod(T_TRACE * T_TRACE - 4, N)]
        assert roots, "not split"
        inv2 = pow(2, N - 2, N)
        cands = [(T_TRACE + r) * inv2 % N for r in roots]
        a = None
        for c in cands:
            if multiplicative_order(c, N) == K:
                a = c
                break
        assert a is not None, (N, K, cands,
                              [multiplicative_order(c, N) for c in cands])
        print(f"=== N={N} K={K}: a = {a}, ord(a) = "
              f"{multiplicative_order(a, N)} ({time.time()-t0:.1f} s)", flush=True)

        d = np.load(os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), "artifacts", "r82",
            f"q_curve_N{N}.npz"))
        q_meas, mu4_meas = d["q"].astype(int), d["mu4"]
        meas = dict(zip(q_meas.tolist(), mu4_meas.tolist()))

        # probe a handful of q' and, for each (k0, parity), find the scale c
        # such that mu4_closed(q') == mu4_measured(c q') for ALL probes
        probes = [1, 2, 3, 5, 7]
        best = None
        for parity_odd in (True, False):
            for k0 in range(K):
                cf, m = build_closed_form(N, K, a, k0, parity_odd, probes)
                if m != len([1 for k in range(N - 1)
                             if k % K == k0 % K and (k % 2 == 1) == parity_odd]):
                    continue
                # candidate scales from the first probe
                v0 = cf[probes[0]]["mu4"]
                cand = [qq for qq, vv in meas.items() if abs(vv - v0) < 1e-8]
                for c in cand:
                    ok = all(abs(cf[p]["mu4"] -
                                 meas.get((c * p) % N, np.nan)) < 1e-8
                             for p in probes)
                    if ok:
                        best = (parity_odd, k0, c, m)
                        break
                if best:
                    break
            if best:
                break
        row = {"N": N, "K": int(K), "a": int(a)}
        if best is None:
            print("  *** no (k0, parity, scale) reproduces the measured curve",
                  flush=True)
            row["match"] = False
            out["designs"].append(row)
            continue
        parity_odd, k0, c, m = best
        print(f"  MATCH: parity_odd={parity_odd}, k0={k0}, scale c={c}, m={m}",
              flush=True)

        # full-curve verification
        allq = sorted(meas)
        cf, _ = build_closed_form(N, K, a, k0, parity_odd,
                                  [(pow(c, N - 2, N) * qq) % N for qq in allq])
        dev = []
        for qq in allq:
            qp = (pow(c, N - 2, N) * qq) % N
            dev.append(abs(cf[qp]["mu4"] - meas[qq]))
        dev = np.array(dev)
        print(f"  FULL CURVE: {len(allq)} level sets, max |mu4_closed - "
              f"mu4_measured| = {dev.max():.3e}, mean {dev.mean():.3e} "
              f"({time.time()-t0:.0f} s)", flush=True)
        row.update({"match": True, "parity_odd": bool(parity_odd), "k0": int(k0),
                    "scale_c": int(c), "m_plus": int(m),
                    "levels_checked": len(allq),
                    "max_abs_dev_mu4": float(dev.max()),
                    "mean_abs_dev_mu4": float(dev.mean())})
        out["designs"].append(row)

    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "closed_form.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
