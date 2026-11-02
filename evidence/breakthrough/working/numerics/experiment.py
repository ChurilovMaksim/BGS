#!/usr/bin/env python3
"""Spectral statistics for a MODEL frozen toral quantum map.

WARNING -- READ FIRST. This is NOT the BGS project's frozen map.
The project's files (bgs-test-150phase/Bgs/LineDDefs.lean, header)
give U = exp(i*eta*V_theta) * M_N with S = [[3,4],[2,3]] and a trace
formula as a hypothesis (hTrace), but they do NOT give explicit matrix
elements of M_N, nor V_theta, nor Ghat_theta. This script therefore uses
an explicitly stated model matrix (see DESIGN.md):

    Q[j,k] = N^(-1/2) * exp(2*pi*i*(j^2 - j*k + k^2)/N)

with a frozen diagonal kick. Its results calibrate the statistics and
kill false hypotheses; they prove nothing about the project map, and
nothing here is a proof of BGS.

Statistics: nearest-neighbour spacings + ratio r, spectral form factor
K(m) = <|Tr U^m|^2>/N, and (diagnostic only) number variance.
References: Poisson <r> = 0.38629, GOE/COE <r> = 0.53590,
GUE/CUE <r> = 0.60266. Wigner surmises are approximations, not exact
RMT laws (see DESIGN.md).

Only dependency: numpy. Run: python3 experiment.py [--N 61]
[--realizations 20] [--eta 5.0] [--seed 0]
"""

import argparse
import sys

import numpy as np

# Reference values (Atas et al. ratio test; Wigner surmises).
R_POISSON, R_GOE, R_GUE = 0.38629, 0.53590, 0.60266


def build_Q(N):
    """Fourier-like symmetric unitary. Unitarity is checked by caller."""
    j = np.arange(N)[:, None]
    k = np.arange(N)[None, :]
    return np.exp(2j * np.pi * (j * j - j * k + k * k) / N) / np.sqrt(N)


def haar_unitary(rng, N):
    """Haar-distributed unitary via QR of a complex Ginibre matrix."""
    z = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q * (d / np.abs(d))  # fix phases of R so Q is Haar
    return q


def phases(U):
    """Sorted eigenphases in [0, 2*pi)."""
    return np.sort(np.angle(np.linalg.eigvals(U)))


def spacings(th):
    """Normalised circular spacings (mean exactly 1)."""
    N = len(th)
    gaps = np.diff(np.r_[th, th[0] + 2 * np.pi])
    return gaps * N / (2 * np.pi)


def ratios(s):
    """Consecutive-spacing ratios r_i in [0, 1]."""
    a, b = s[:-1], s[1:]
    return np.minimum(a, b) / np.maximum(a, b)


def mean_se(x):
    """Mean and standard error of the mean (1 sigma)."""
    x = np.asarray(x, dtype=float)
    return float(np.mean(x)), float(np.std(x, ddof=1) / np.sqrt(len(x)))


def p_goe(s):
    return (np.pi / 2) * s * np.exp(-np.pi * s * s / 4)


def p_gue(s):
    return (32 / np.pi**2) * s * s * np.exp(-4 * s * s / np.pi)


def p_poisson(s):
    return np.exp(-s)


def form_factor_coe(tau):
    """Exact large-N COE form factor (tau = m/N)."""
    tau = np.asarray(tau, dtype=float)
    out = np.empty_like(tau)
    lo = tau < 1
    out[lo] = 2 * tau[lo] - tau[lo] * np.log(1 + 2 * tau[lo])
    hi = ~lo
    # At tau == 1 the second branch is singular; use the limit value 1.
    t = tau[hi]
    out[hi] = np.where(t == 1.0, 1.0, 2 - t * np.log((2 * t + 1) / (2 * t - 1)))
    return out


def parity_sector_ratios(U):
    """If U commutes with index reversal j -> -j (mod N), split it into
    even/odd parity sectors and return (comm_error, [r_even, r_odd]).
    Returns None when there is no such symmetry. This is trap 3 in
    DESIGN.md: a symmetric frozen kick splits the spectrum, and the
    full-spectrum spacing then looks Poisson-like even when every
    sector is RMT-like."""
    N = U.shape[0]
    P = np.zeros((N, N))
    for i in range(N):
        P[i, (-i) % N] = 1.0
    err = float(np.max(np.abs(U @ P - P @ U)))
    if err > 1e-8:
        return err, None
    evens, odds = [], []
    e = np.zeros(N); e[0] = 1.0; evens.append(e)
    for a in range(1, (N + 1) // 2):
        v = np.zeros(N); v[a] = 1 / np.sqrt(2); v[N - a] = 1 / np.sqrt(2)
        evens.append(v)
        v = np.zeros(N); v[a] = 1 / np.sqrt(2); v[N - a] = -1 / np.sqrt(2)
        odds.append(v)
    B = np.column_stack(evens + odds)
    Ub = B.T @ U @ B
    out = []
    for sl in [slice(0, len(evens)), slice(len(evens), N)]:
        w = np.linalg.eigvals(Ub[sl, sl])
        s = spacings(np.sort(np.angle(w)))
        out.append(float(np.mean(ratios(s))))
    return err, out


def number_variance(th, L, rng, n_arcs=100):
    """Diagnostic only: variance of counts on random arcs of length L
    mean spacings. Arcs overlap, so the naive error is understated;
    do not use this as the deciding test (see DESIGN.md)."""
    N = len(th)
    length = 2 * np.pi * L / N
    extended = np.r_[th, th + 2 * np.pi]
    starts = rng.uniform(0, 2 * np.pi, n_arcs)
    counts = np.array([
        np.searchsorted(extended, s + length) - np.searchsorted(extended, s)
        for s in starts
    ], dtype=float)
    return float(np.var(counts, ddof=1)), float(np.mean(counts))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--N", type=int, default=61, help="matrix size (odd preferred)")
    ap.add_argument("--realizations", type=int, default=20,
                    help="realizations for ensemble variants G, I, CUE")
    ap.add_argument("--eta", type=float, default=5.0, help="frozen kick strength")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    N, R, eta = args.N, args.realizations, args.eta
    if N < 5:
        sys.exit("N must be >= 5")
    rng = np.random.default_rng(args.seed)

    print("MODEL MATRIX ONLY -- not the BGS project map (see DESIGN.md).")
    print(f"N={N}  realizations={R}  eta={eta}  seed={args.seed}\n")

    Q = build_Q(N)
    # --- Self-tests: these must pass, otherwise nothing below is trusted.
    unit_err = float(np.max(np.abs(Q @ Q.conj().T - np.eye(N))))
    sym_err = float(np.max(np.abs(Q - Q.T)))
    print(f"Q unitarity error = {unit_err:.2e}   symmetry error = {sym_err:.2e}")
    assert unit_err < 1e-10 and sym_err < 1e-10, "Q failed its self-test"

    # --- Variants.
    phi_frozen = eta * np.cos(2 * np.pi * np.arange(N) / N)
    D_half = np.diag(np.exp(1j * phi_frozen / 2))
    U_S = D_half @ Q @ D_half  # one frozen system, symmetric -> COE-like
    U_Q = Q                    # no kick: trap control

    def collect(build, n):
        """Return (pooled ratios, pooled spacings, eigs, per-realization <r>).

        Error bars MUST come from per-realization means, not from pooled
        ratios: ratios inside one spectrum are correlated, so
        std(pooled)/sqrt(n_pooled) understates the error for a single
        spectrum and biases it for ensembles too.
        """
        rs, ss, eigs, per_mean = [], [], [], []
        for _ in range(n):
            w = np.linalg.eigvals(build())
            eigs.append(w)
            s = spacings(np.sort(np.angle(w)))
            ss.extend(s.tolist())
            r = ratios(s)
            rs.extend(r.tolist())
            per_mean.append(float(np.mean(r)))
        return rs, ss, eigs, per_mean

    rS, _, _, perS = collect(lambda: U_S, 1)
    rQ, sQ, _, perQ = collect(lambda: U_Q, 1)
    rG, sG, eigsG, perG = collect(
        lambda: np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, N))) @ Q, R)
    rI, sI, _, perI = collect(
        lambda: np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, N))), R)
    rC, _, _, perC = collect(lambda: haar_unitary(rng, N), R)

    print("\n== Spacing ratio <r> ==")
    print("reference: Poisson 0.38629 | GOE/COE 0.53590 | GUE/CUE 0.60266")
    print("SE for ensembles = std(per-realization <r>)/sqrt(R) (1 sigma).")
    print("Single spectra (Q, S) have NO meaningful SE from their own ratios:")
    print("ratios inside one spectrum are correlated; judge one spectrum")
    print("against the spread of per-realization means in its ensemble.")
    print(f"{'variant':<28} {'<r>':>8} {'SE':>8} {'n_r':>6}")
    for name, r, per in [("Q (no kick, trap)", rQ, perQ),
                         ("S (one frozen kick)", rS, perS),
                         ("G (random-kick ensemble)", rG, perG),
                         ("I (diagonal, Poisson by construction)", rI, perI),
                         ("CUE (Haar reference)", rC, perC)]:
        m = float(np.mean(r))
        se = mean_se(per)[1] if len(per) > 1 else float("nan")
        se_s = f"{se:8.3f}" if len(per) > 1 else "     ---"
        print(f"{name:<28} {m:8.3f} {se_s} {len(r):6d}")
    gm, gse = mean_se(perG)
    print(f"G per-realization <r>: mean {gm:.3f}, std {np.std(perG, ddof=1):.3f} "
          f"(this std is the scale for judging ONE frozen spectrum)")
    err, sectors = parity_sector_ratios(U_S)
    if sectors is None:
        print(f"S: no parity symmetry (commutator error {err:.2e})")
    else:
        print(f"S: PARITY SYMMETRY FOUND (commutator error {err:.2e}).")
        print(f"   Full-spectrum <r> = {float(np.mean(rS)):.3f} looks Poisson-like,")
        print(f"   but desymmetrized sectors give <r> = {sectors[0]:.3f} (even) "
              f"and {sectors[1]:.3f} (odd) -- RMT-like.")
        print("   Lesson: never judge a symmetric system by its full spectrum.")
    degen = float(np.mean(np.asarray(sQ) < 1e-6))
    print(f"Q: fraction of spacings < 1e-6 = {degen:.3f} "
          f"(exact ties must be reported, never smoothed away)")

    # --- Spacing histogram vs Wigner surmises (illustration, not the test).
    print("\n== Spacing histogram, G ensemble: observed fraction vs surmise ==")
    bins = np.arange(0.0, 3.25, 0.25)
    hist, _ = np.histogram(sG, bins=bins, density=False)
    hist = hist / len(sG)
    centres = 0.5 * (bins[:-1] + bins[1:])
    print(f"{'s-bin':<12} {'obs':>6} {'Poisson':>8} {'GOE':>6} {'GUE':>6}")
    for c, o in zip(centres, hist):
        # Integrate the density over the bin by midpoint x width (0.25).
        print(f"{c:5.2f}         {o:6.3f} {0.25 * p_poisson(c):8.3f} "
              f"{0.25 * p_goe(c):6.3f} {0.25 * p_gue(c):6.3f}")
    print("(Wigner curves are surmises; judge by <r> and K(m), not by this.)")

    # --- Spectral form factor, G ensemble.
    print("\n== Spectral form factor K(m), G ensemble ==")
    print("Poisson predicts K = 1 at every m; RMT predicts a ramp then plateau.")
    ms = sorted(set([1, 2, 3, 5, 10, 20, N // 2, N, 3 * N // 2]))
    print(f"{'m':>5} {'tau':>6} {'K':>7} {'SE':>7} {'COE':>7} {'Poisson':>8}")
    for m in ms:
        vals = np.array([np.abs(np.sum(w ** m)) ** 2 / N for w in eigsG])
        km, se = mean_se(vals)
        tau = m / N
        print(f"{m:5d} {tau:6.2f} {km:7.3f} {se:7.3f} "
              f"{float(form_factor_coe(np.array([tau]))[0]):7.3f} {1.0:8.3f}")

    # --- Number variance, diagnostic only.
    print("\n== Number variance Sigma^2(L), G ensemble (DIAGNOSTIC ONLY) ==")
    print("Poisson: Sigma^2 = L. RMT: ~ logarithmic in L. Read only for L << N.")
    thG = [np.sort(np.angle(w)) for w in eigsG]
    for L in [1, 2, 5, 10, 20]:
        if L >= N // 2:
            continue
        vs = [number_variance(th, L, rng)[0] for th in thG]
        vm, vse = mean_se(vs)
        print(f"L={L:<3d} Sigma^2 = {vm:6.3f} +- {vse:.3f}   (Poisson: {L})")

    print("\nDone. Numerical output only: this is NOT a proof of BGS,")
    print("and the model matrix is NOT the project frozen map (DESIGN.md).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
