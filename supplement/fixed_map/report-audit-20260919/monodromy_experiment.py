"""Finite experiment for the uploaded f_star, not the frozen 10^-80 model.

Positive cat kernel; physical symbol e(aq+bp) -> W(b,a);
hbar=1/(2*pi*N), U=exp(-2*pi*i*kappa*N*Op(f_star))*M_plus.
No ensemble average or asymptotic conclusion is taken from these dimensions.
"""
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.linalg import eigh, eigvals


def weyl(N, shift, momentum):
    j = np.arange(N)
    W = np.zeros((N, N), complex)
    W[j, (j + shift) % N] = np.exp(2j * np.pi * momentum * (j + shift / 2) / N)
    return W


def symbol():
    # First in Q=2*pi*(q+1/5), then undo the coordinate translation.
    f = {(1, 0): .5, (-1, 0): .5,
         (2, 0): -.25 - 1j * math.sqrt(3) / 4,
         (-2, 0): -.25 + 1j * math.sqrt(3) / 4}
    for a, ca in ((1, -.5j), (-1, .5j)):
        for b, cb in ((1, -.5j*np.exp(1j*np.pi/4)), (-1, .5j*np.exp(-1j*np.pi/4))):
            f[a, b] = ca * cb
    for a in (-2, 2):
        f[a, 2] = -.25j
        f[a, -2] = .25j
    return {v: c*np.exp(2j*np.pi*v[0]/5) for v, c in f.items()}


def main():
    rows = []
    saved_angles = {}
    started = time.monotonic()
    for K, N in ((5, 41), (7, 239), (9, 1393)):
        x = np.arange(N, dtype=np.int64)
        phase = ((3*x[:, None]**2 - 2*x[:, None]*x[None, :] + 3*x[None, :]**2)
                 * pow(8, -1, N)) % N
        M = np.exp(2j * np.pi * phase / N) / math.sqrt(N)
        A = sum(c*weyl(N, b, a) for (a, b), c in symbol().items())
        hermitian_error = float(np.max(abs(A-A.conj().T)))
        assert hermitian_error < 1e-11
        if N == 41:
            # M_plus^* Op(e(aq+bp)) M_plus = Op(e((S^T(a,b)).(q,p))).
            for a, b in ((1, 0), (0, 1), (1, -1)):
                error = np.linalg.norm(M.conj().T@weyl(N, b, a)@M
                                       - weyl(N, 4*a+3*b, 3*a+2*b)) / math.sqrt(N)
                assert error < 1e-11, (a, b, error)
        # Hermitian correction removes only roundoff, before LAPACK's eigensolve.
        values, basis = eigh((A + A.conj().T)/2, check_finite=False)
        L = N // K
        ell = np.arange(1, L)
        weights = 1 - ell / L
        reference = float(2*np.sum(weights*np.minimum(K*ell, N))/N**2)
        for kappa in (1e-4, 4e-4):
            D = (basis * np.exp(-2j*np.pi*kappa*N*values)) @ basis.conj().T
            spectrum = eigvals(D @ M, check_finite=False)
            unit_circle_error = float(np.max(abs(abs(spectrum)-1)))
            assert unit_circle_error < 1e-10
            angles = np.angle(spectrum)
            saved_angles[f'N{N}_kappa{kappa:.4g}'] = angles
            returns = np.exp(1j*K*ell[:, None]*angles[None, :]).mean(axis=1)
            energy = float(2*np.sum(weights*abs(returns)**2))
            # Correct CUE third-trace reference above the Heisenberg boundary.
            modes = np.arange(math.ceil(.71*N), math.floor(.79*N)+1)
            scaled = modes/N
            v = (scaled-.75)/.04
            bump = np.zeros_like(scaled)
            interior = abs(v) < 1
            bump[interior] = np.exp(-1/(1-v[interior]**2))
            pairweights = bump[:, None]*bump[None, :]
            requested = np.unique(np.r_[modes, (modes[:, None]+modes[None, :]).ravel()])
            traces = dict(zip(requested, np.exp(1j*requested[:, None]*angles[None, :]).sum(axis=1)))
            first = np.array([traces[m] for m in modes])
            total = np.array([[traces[a+b].conjugate() for b in modes] for a in modes])
            cubic = np.sum(pairweights*first[:, None]*first[None, :]*total)/(N*pairweights.sum())
            cubic_reference = np.sum(pairweights*(scaled[:, None]+scaled[None, :]-1))/pairweights.sum()
            pair = np.sum(bump*abs(first)**2)/(N*bump.sum())
            pair_reference = np.sum(bump*scaled)/bump.sum()
            rows.append({"K": K, "N": N, "kappa": kappa, "quantum_phase_scale": 2*np.pi*kappa*N,
                         "L": L, "fejer_return_energy": energy,
                         "cue_U_reference_expectation": reference,
                         "unperturbed_cat_energy_exact": L-1,
                         "smoothed_cubic": [float(cubic.real), float(cubic.imag)],
                         "cue_cubic_reference": float(cubic_reference),
                         "smoothed_pair_form_factor": float(pair),
                         "cue_pair_reference": float(pair_reference),
                         "unit_circle_max_error": unit_circle_error,
                         "hermitian_entry_error": hermitian_error})
            Path(__file__).with_suffix('.json').write_text(json.dumps({
                "status": "running", "rows": rows,
                "elapsed_seconds": time.monotonic()-started}, indent=2)+'\n')
            print(json.dumps(rows[-1]), flush=True)
    np.savez_compressed(Path(__file__).with_name('monodromy_eigenangles.npz'), **saved_angles)
    Path(__file__).with_suffix('.json').write_text(json.dumps({
        "status": "completed", "rows": rows,
        "elapsed_seconds": time.monotonic()-started,
        "scope": "f_star finite-dimension diagnostics, not a test at frozen tau=10^-80 and not a universality proof"
    }, indent=2)+'\n')


if __name__ == '__main__':
    main()
