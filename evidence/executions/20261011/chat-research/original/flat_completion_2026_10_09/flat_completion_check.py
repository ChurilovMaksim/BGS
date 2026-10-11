"""Controls of the flat interpolation theorem and its exact cavity input.

The proof is in flat_completion.md. Floating checks are not certificates.
No repository imports and no writes outside this research directory.
"""
import json
import os
import platform
import time
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
os.environ.setdefault("OMP_NUM_THREADS", "2")

import numpy as np
import scipy
from scipy.fft import fft, ifft
from scipy.linalg import null_space
from scipy.sparse.linalg import svds

SEED = 86742091


def roots(h):
    values, vectors = np.linalg.eigh(h)
    if values.min() <= 0:
        raise ValueError("positive matrix required")
    return ((vectors * np.sqrt(values)) @ vectors.conj().T,
            (vectors / np.sqrt(values)) @ vectors.conj().T)


def mub_rows(m):
    x = np.arange(m)
    rows = [np.eye(m, dtype=complex)]
    for b in range(m):
        columns = np.stack([
            np.exp(2j * np.pi * (b*x*x+k*x) / m) / np.sqrt(m)
            for k in range(m)], axis=1)
        rows.append(columns.conj().T)
    return np.concatenate(rows)


def cavity_frames(m, r, a):
    base = mub_rows(m)
    shift = np.roll(np.eye(m), 1, axis=0)
    h = np.eye(m) + (a/2)*(shift + shift.T)
    hs, his = roots(h)
    hinv = his @ his
    n = (r+m)*m*(m+1)
    lambdas = np.diag(hinv).real/(r+m)
    mu = float(lambdas.sum())
    assert mu < 1
    theta = .13 + 2*np.pi*np.arange(m)/m
    s = np.diag(np.exp(1j*theta))
    removed = [np.tile(base, (r, 1))*np.sqrt((1-mu)/(r*(m+1)))]
    retained = []
    for j in range(m):
        u = his[:, j]/np.sqrt(hinv[j, j].real)
        rotation = np.column_stack([u, null_space(u.conj()[None, :])])
        rows = base @ rotation.conj().T
        q = lambdas[j]/(m+1)
        removed.append(np.sqrt(q)*rows[1:])
        retained.append(np.exp(1j*theta[j])*np.sqrt(q)*rows[0])
    z0 = np.concatenate([*removed, np.stack(retained)])
    b0 = np.sqrt(n/m)*z0@hs
    l0 = b0[:-m]
    k0 = np.vstack([l0, np.eye(m)])
    c0 = np.sqrt(m/n)*k0@his
    return c0, z0, b0, k0, h, s, mu


def physical_covariance(b):
    n, m = b.shape
    p = np.abs(b)**2
    weights = p.sum(axis=1)
    return (m/n)*(p.T@(p/weights[:, None]))


def white_energy(z):
    """Frame energy via N×m² coordinates, avoiding an N×N Gram."""
    n, m = z.shape
    q = np.sum(np.abs(z)**2, axis=1)
    columns = [np.abs(z[:, j])**2 for j in range(m)]
    for j in range(m):
        for k in range(j+1, m):
            entry = np.conj(z[:, j])*z[:, k]
            columns.extend([np.sqrt(2)*entry.real, np.sqrt(2)*entry.imag])
    coordinate = np.stack(columns, axis=1)/np.sqrt(q[:, None])
    frame = coordinate.T@coordinate
    target = np.eye(m*m)/(m+1)
    target[:m, :m] += 1/(m+1)
    return float(np.linalg.norm(frame-target))


def complete(c0, z0, rng, permute=False):
    n, m = c0.shape
    permutation = rng.permutation(n) if permute else np.arange(n)

    def f(x):
        return fft(x[permutation], axis=0, norm="ortho")

    def fh(x):
        result = np.empty_like(x)
        result[permutation] = ifft(x, axis=0, norm="ortho")
        return result

    for attempt in range(100):
        d = np.exp(2j*np.pi*rng.random(n))
        c, z = d[:, None]*c0, d[:, None]*z0
        aa = f(c)
        g = aa.conj().T@z
        if np.linalg.norm(g, 2) <= .5:
            break
    else:
        raise AssertionError("No admissible phase witness in 100 trials")
    delta, invdelta = roots(np.eye(m)-g.conj().T@g)
    gamma, _ = roots(np.eye(m)-g@g.conj().T)
    y = (z-aa@g)@invdelta
    e = np.column_stack([aa, y])
    jg = np.block([[g, -gamma], [delta, g.conj().T]])
    eh = fh(e)
    transform = jg-np.eye(2*m)
    # The permutation determines column locations in the Fourier matrix.
    inverse_permutation = np.argsort(permutation)
    idx = np.arange(n)
    ff = np.exp(-2j*np.pi*idx[:, None]*inverse_permutation[None, :]/n)/np.sqrt(n)
    phase_t = 0.731
    rank_part = z@c.conj().T
    w0 = ff + (e@transform)@eh.conj().T
    w = np.exp(1j*phase_t)*w0+(1-np.exp(1j*phase_t))*rank_part
    probes = rng.normal(size=(n, 8))+1j*rng.normal(size=(n, 8))
    probes /= np.linalg.norm(probes, axis=0)
    error = {
        "initial_c_stiefel": float(np.linalg.norm(c0.conj().T@c0-np.eye(m))),
        "initial_z_stiefel": float(np.linalg.norm(z0.conj().T@z0-np.eye(m))),
        "orthonormal_patch": float(np.linalg.norm(e.conj().T@e-np.eye(2*m))),
        "julia_unitarity": float(np.linalg.norm(jg.conj().T@jg-np.eye(2*m))),
        "interpolation": float(np.linalg.norm(w@c-z)),
        "unitarity_random_probes": float(np.linalg.norm(w.conj().T@(w@probes)-probes)),
        "fft_dense_agreement": float(np.linalg.norm(ff@c-aa))
    }
    assert max(error.values()) < 3e-9, error
    p = np.abs(w)**2
    centered = p-1/n
    sigma = float(svds(centered, k=1, which="LM", return_singular_vectors=False,
                       random_state=SEED, tol=1e-9)[0])
    absolute_entry_error = float(np.max(np.abs(w-np.exp(1j*phase_t)*ff)))
    epsilon = np.sqrt(n)*absolute_entry_error
    bound = 2*epsilon+epsilon**2
    assert sigma <= bound+1e-10
    assert np.linalg.norm(p.sum(axis=1)-1) < 1e-9
    return w, d, error, {
        "cross_overlap_op": float(np.linalg.norm(g, 2)),
        "row_coherence_constant": float(np.sqrt(n/m)*max(
            np.linalg.norm(c0, axis=1).max(), np.linalg.norm(z0, axis=1).max())),
        "maximum_relative_entry_error": float(epsilon),
        "classical_second_singular_value": sigma,
        "classical_bound_from_entry_error": float(bound),
        "classical_diagonal_mean": float(np.mean(np.diag(p))),
        "phase_draws": attempt+1,
        "permuted_fourier": bool(permute)
    }


def cross_second_moment_control(rng):
    n, m, draws = 32, 3, 12000
    c0 = np.linalg.qr(rng.normal(size=(n, m))+1j*rng.normal(size=(n, m)))[0]
    z0 = np.linalg.qr(rng.normal(size=(n, m))+1j*rng.normal(size=(n, m)))[0]
    idx = np.arange(n)
    ff = np.exp(-2j*np.pi*idx[:, None]*idx[None, :]/n)/np.sqrt(n)
    constant = z0.conj().T@(np.diag(ff)[:, None]*c0)
    exact = np.linalg.norm(constant)**2 + (m*m-np.sum(
        np.sum(np.abs(z0)**2, axis=1)*np.sum(np.abs(c0)**2, axis=1)))/n
    values = []
    for _ in range(draws):
        d = np.exp(2j*np.pi*rng.random(n))
        g = (d[:, None]*z0).conj().T@ff@(d[:, None]*c0)
        values.append(np.linalg.norm(g)**2)
    values = np.asarray(values)
    se = float(values.std(ddof=1)/np.sqrt(draws))
    discrepancy = float(values.mean()-exact)
    assert abs(discrepancy) < 6*se
    return {"N": n, "m": m, "phase_samples": draws,
            "exact_second_moment": float(exact), "sample_second_moment": float(values.mean()),
            "standard_error": se, "discrepancy_standard_errors": discrepancy/se,
            "universal_upper_bound": (m*m+m)/n}


def main():
    started = time.time()
    rng = np.random.default_rng(SEED)
    cases = []
    for m, r in [(3, 30), (5, 25), (7, 49)]:
        c0, z0, b0, k0, h, s, mu = cavity_frames(m, r, .4)
        n = c0.shape[0]
        w, d, errors, mixing = complete(c0, z0, rng, permute=True)
        dr = d[-m:]
        bprime = d[:, None]*b0*dr.conj()[None, :]
        kprime = d[:, None]*k0*dr.conj()[None, :]
        cov0, cov1 = physical_covariance(b0), physical_covariance(bprime)
        errors.update({
            "bottom_identity": float(np.linalg.norm(kprime[-m:]-np.eye(m))),
            "bottom_spectrum": float(np.linalg.norm(bprime[-m:]-s)),
            "full_interpolation": float(np.linalg.norm(w@kprime-bprime)),
            "covariance_preserved": float(np.linalg.norm(cov1-cov0)),
            "white_design": white_energy(z0),
            "clock_conjugacy": float(np.linalg.norm((m/n)*(kprime.conj().T@kprime)
                -dr[:, None]*h*dr.conj()[None, :]))
        })
        # Direct inversion supplements the proof in the first two sizes.
        if n <= 1000:
            inverse_input = np.eye(n-m)-w[:-m, :-m]
            ell = np.linalg.solve(inverse_input, w[:-m, -m:])
            schur = w[-m:, -m:]+w[-m:, :-m]@ell
            errors["direct_schur_spectrum"] = float(np.linalg.norm(schur-s))
            errors["direct_schur_extension"] = float(np.linalg.norm(ell-kprime[:-m]))
            errors["dense_unitarity"] = float(np.linalg.norm(w.conj().T@w-np.eye(n)))
        assert max(errors.values()) < 5e-8, errors
        scaled = (m+1)*cov1-np.eye(m)-np.ones((m, m))
        cases.append({"m": m, "N": n, "r": r, "a": .4, "mixture_mass": mu,
                      "residuals": errors, "mixing": mixing,
                      "scaled_covariance_error_op": float(np.linalg.norm(scaled, 2)),
                      "base_scaled_error_op": .4**2/2*np.cos(np.pi/m),
                      "neighbor_scaled_error": float(scaled[0, 1])})
        print(json.dumps(cases[-1]), flush=True)
        del w
    output = {"seed": SEED, "cases": cases,
              "second_moment_control": cross_second_moment_control(rng),
              "elapsed_seconds": time.time()-started,
              "scope": ["Finite complex128 controls of a separately written proof.",
                        "No uniform phase average or BGS conclusion is inferred.",
                        "m=7 uses interpolation and probe controls, no dense Schur inverse."],
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "scipy": scipy.__version__}}
    here = Path(__file__).resolve().parent
    output_path = here/"flat_completion_check_results.json"
    output_path.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2), flush=True)


if __name__ == "__main__":
    main()
