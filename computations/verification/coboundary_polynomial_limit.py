#!/usr/bin/env python3
"""FLOW-011 finite controls; not a stochastic/asymptotic certificate.

Exact rational exponent and partition checks; seeded complex128
covariance, Sylvester derivative, projected-noise and drift diagnostics.
No simulation of the polynomial step count; no Heisenberg/BGS estimate.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.linalg import expm, solve_sylvester


def hermitian_basis(n):
    """Real HS-orthonormal basis of the traceless Hermitian space."""
    matrices = []
    for j in range(1, n):
        diagonal = np.zeros(n)
        diagonal[:j] = 1 / np.sqrt(j * (j + 1))
        diagonal[j] = -j / np.sqrt(j * (j + 1))
        matrices.append(np.diag(diagonal).astype(complex))
    for j in range(n):
        for k in range(j + 1, n):
            a = np.zeros((n, n), complex)
            a[j, k] = a[k, j] = 1 / np.sqrt(2)
            matrices.append(a)
            a = np.zeros((n, n), complex)
            a[j, k], a[k, j] = 1j / np.sqrt(2), -1j / np.sqrt(2)
            matrices.append(a)
    basis = np.array(matrices)
    gram = np.einsum("aij,bji->ab", basis, basis).real
    assert np.max(np.abs(gram - np.eye(n*n - 1))) < 1e-15
    assert np.max(np.abs(np.trace(basis, axis1=1, axis2=2))) < 1e-15
    return basis


def covariance(u, basis, du=None):
    """Matrix of B=N C on a fixed real traceless Hermitian basis."""
    n = len(u)
    us = u.conj().T
    u2, us2 = u @ u, us @ us
    q = np.trace(u2) / n
    trace2 = np.einsum("ij,aji->a", u2, basis)
    traces2 = np.einsum("ij,aji->a", us2, basis)
    image = basis - (q * (us @ basis @ us) +
                     q.conjugate() * (u @ basis @ u)) / 2
    image += (trace2[:, None, None] * us2 +
              traces2[:, None, None] * u2) / (2*n)
    matrix = np.einsum("aij,bji->ab", basis, image)
    assert np.max(np.abs(matrix.imag)) < 3e-14
    matrix = matrix.real
    assert np.max(np.abs(matrix-matrix.T)) < 3e-14
    if du is None:
        return matrix
    dus = du.conj().T
    du2, dus2 = du @ u + u @ du, dus @ us + us @ dus
    dq = np.trace(du2) / n
    derivative = -(dq*(us @ basis @ us) +
        q*(dus @ basis @ us + us @ basis @ dus) +
        dq.conjugate()*(u @ basis @ u) +
        q.conjugate()*(du @ basis @ u + u @ basis @ du)) / 2
    dt2 = np.einsum("ij,aji->a", du2, basis)
    dts2 = np.einsum("ij,aji->a", dus2, basis)
    derivative += (dt2[:, None, None]*us2 + trace2[:, None, None]*dus2 +
                   dts2[:, None, None]*u2 + traces2[:, None, None]*du2) / (2*n)
    dm = np.einsum("aij,bji->ab", basis, derivative)
    assert np.max(np.abs(dm.imag)) < 3e-14
    return matrix, dm.real


def coefficients(u, basis, du=None):
    n = len(u)
    us, u2, us2 = u.conj().T, u @ u, u.conj().T @ u.conj().T
    m1, q, r = (np.trace(np.linalg.matrix_power(u, j))/n for j in (1, 2, 3))
    d = 1-abs(q)**2
    assert abs(q) < .6
    cov = covariance(u, basis, du)
    bmat = cov[0] if du is not None else cov
    eigenvalues, eigenvectors = np.linalg.eigh(bmat)
    assert eigenvalues[0] >= 1-abs(q)-3e-13
    assert eigenvalues[-1] <= 2+abs(q)+3e-13
    root = (eigenvectors*np.sqrt(eigenvalues)) @ eigenvectors.T
    k = np.einsum("ba,bij->aij", root/np.sqrt(n), basis)
    fa = 1j*np.einsum("aij,ji->a", k, u)/n
    w = (fa + q*fa.conjugate())/d
    jmat = 1j*(w[:, None, None]*us - w.conjugate()[:, None, None]*u)
    l = k+jmat
    v, zeta = np.sum(abs(w)**2), np.sum(w*w)
    tmat = np.einsum("a,aij->ij", w.conjugate(), k)
    kappa = 2j*np.trace(tmat @ u2)/n
    h0 = kappa + r*zeta.conjugate()
    b = (h0+q*h0.conjugate())/d
    api = (1j*b*us - 1j*b.conjugate()*u + tmat @ u +
           tmat.conj().T @ us + .5j*zeta*us2 -
           .5j*zeta.conjugate()*u2)
    qk = np.sum(k @ k, axis=0)
    qk_formula = np.eye(n) - (q*m1.conjugate()*us +
                              q.conjugate()*m1*u)/2
    ql = np.sum(l @ l, axis=0)
    ql_formula = (qk_formula + 2j*(tmat.conj().T @ us-tmat @ u) +
                  2*v*np.eye(n)-zeta*us2-zeta.conjugate()*u2)
    q_error = max(np.linalg.norm(qk-qk_formula),
                  np.linalg.norm(ql-ql_formula))
    assert q_error < 3e-13
    assert np.linalg.norm(api-api.conj().T) < 3e-13
    drift = -.5*ql_formula @ u + 1j*api @ u
    noise = 1j*l @ u
    result = {"noise": noise, "drift": drift, "root": root,
              "q_error": float(q_error), "q": float(abs(q)), "B": bmat}
    if du is None:
        return result
    dus, du2 = du.conj().T, du @ u+u @ du
    dq = np.trace(du2)/n
    dd = -2*np.real(q.conjugate()*dq)
    droot = solve_sylvester(root, root, cov[1])
    dk = np.einsum("ba,bij->aij", droot/np.sqrt(n), basis)
    dfa = 1j*np.einsum("aij,ji->a", dk, u)/n
    dfa += 1j*np.einsum("aij,ji->a", k, du)/n
    dw = (dfa+dq*fa.conjugate()+q*dfa.conjugate())/d-w*dd/d
    dj = 1j*(dw[:, None, None]*us+w[:, None, None]*dus -
        dw.conjugate()[:, None, None]*u-w.conjugate()[:, None, None]*du)
    dnoise = 1j*((dk+dj) @ u+l @ du)
    result.update({"dnoise": dnoise, "droot": droot, "dB": cov[1]})
    return result


def partitions(n):
    if n == 0:
        yield []
        return
    for p in partitions(n-1):
        yield p+[[n-1]]
        for j in range(len(p)):
            yield [block+[n-1] if j == i else block.copy()
                   for i, block in enumerate(p)]


def exact_controls():
    a, beta = Fraction(26, 3), Fraction(2, 3)
    assert 4*a-beta == 34
    assert 9-a-beta == -Fraction(1, 3)
    assert 10-2*a-beta == -8
    assert 4-a == -Fraction(14, 3)
    assert beta/2 == 1-beta == Fraction(1, 3)
    bell = []
    for j, count in enumerate((1, 2, 5, 15, 52, 203), start=1):
        ps = list(partitions(j))
        assert len(ps) == count
        for p in ps:
            assert sorted(x for block in p for x in block) == list(range(j))
            assert sum(len(block) for block in p) == j
        bell.append({"derivative_order": j, "partitions": len(ps),
                     "dimension_exponent": j})
    polynomial = {0: 1}
    for _ in range(6):
        nxt = {}
        for power, coefficient in polynomial.items():
            if power:
                nxt[power-1] = nxt.get(power-1, 0)+power*coefficient
            nxt[power+1] = nxt.get(power+1, 0)-coefficient
        polynomial = {k: v for k, v in nxt.items() if v}
    assert polynomial == {0: -15, 2: 45, 4: -15, 6: 1}
    return {"epsilon_exponent": str(a), "time_exponent": str(beta),
            "step_count_exponent": 34, "weak_linear_exponent": "-1/3",
            "weak_quadratic_exponent": -8,
            "exit_error_exponent": "-14/3", "Bell_partitions": bell,
            "Gaussian_sixth_derivative_coefficients": polynomial}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    seed = 20261004
    rng = np.random.default_rng(seed)
    rows = []
    step = 2e-5
    for n in (3, 5, 7, 9, 13):
        basis = hermitian_basis(n)
        theta = 2*np.pi*np.arange(n)/n
        fourier = np.exp(2j*np.pi*np.outer(np.arange(n), np.arange(n))/n)/np.sqrt(n)
        for kind in ("clock", "warped"):
            angles = theta if kind == "clock" else theta+.14*np.sin(theta)+.2*np.sin(2*theta)
            u = fourier @ np.diag(np.exp(1j*angles)) @ fourier.conj().T
            directions = []
            for z in (u @ u+(u @ u).conj().T,
                      (u @ u-(u @ u).conj().T)/1j):
                z = z-np.trace(z)*np.eye(n)/n
                if np.linalg.norm(z) > 1e-12:
                    directions.append(z/np.linalg.norm(z))
            for _ in range(2):
                z = np.einsum("a,aij->ij", rng.normal(size=n*n-1), basis)
                directions.append(z/np.linalg.norm(z))
            for idx, direction in enumerate(directions):
                du = 1j*direction @ u
                center = coefficients(u, basis, du)
                plus = coefficients(expm(1j*step*direction) @ u, basis)
                minus = coefficients(expm(-1j*step*direction) @ u, basis)
                finite_noise = (plus["noise"]-minus["noise"])/(2*step)
                finite_drift = (plus["drift"]-minus["drift"])/(2*step)
                noise_error = np.linalg.norm(finite_noise-center["dnoise"])
                drift_norm = np.linalg.norm(finite_drift)
                assert noise_error < 2e-7
                db_ratio = np.linalg.norm(center["dB"])/np.sqrt(n)
                noise_norm = np.linalg.norm(center["dnoise"])
                assert db_ratio < 30 and noise_norm < 30 and drift_norm < 30
                rows.append({"N": n, "spectrum": kind, "direction": idx,
                    "abs_m2": center["q"], "B_derivative_HS_over_sqrt_N": float(db_ratio),
                    "projected_noise_derivative_HS": float(noise_norm),
                    "drift_central_difference_HS": float(drift_norm),
                    "noise_finite_difference_error": float(noise_error),
                    "exact_contraction_floating_error": center["q_error"]})
    report = {"status": "PASS", "claim_id": "BGS-FLOW-011", "seed": seed,
        "arithmetic": "exact rational/integer controls and complex128 diagnostics",
        "software": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_controls": exact_controls(), "matrix_cases": rows,
        "coverage": {"N": [3, 5, 7, 9, 13], "spectra": ["clock", "warped"],
            "directions": "two trace-aligned and two seeded Hermitian directions per spectrum",
            "central_difference_step": step, "noise_tolerance": 2e-7,
            "drift_diagnostic": "central differences only; no derivative-error certification"},
        "non_claims": ["No asymptotic extrapolation or uniform derivative certificate",
            "No stochastic semigroup simulation", "No polynomial step-count simulation",
            "No analytic Lean proof", "No deterministic BGS theorem"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": report["status"], "matrix_cases": len(rows),
        "exact_partitions": 278, "maximum_noise_error":
        max(row["noise_finite_difference_error"] for row in rows)}))


if __name__ == "__main__":
    main()
