"""Independent full-ordered-tensor controls; no candidate code imported.

Haar removal uses the SVD of ALL slot-permutation matrices, including the
linearly dependent m>N case. Sector normalization uses a second SVD.
The claimed rank-one Haar/Gram formula is only tested, never used to build Q.
"""
import itertools
import json
import math
import time
from pathlib import Path
import numpy as np

def tensor_power(a, m):
    r = np.ones((1, 1), complex)
    for _ in range(m):
        r = np.kron(r, a)
    return r

def column_basis(a):
    u, s, _ = np.linalg.svd(a, full_matrices=False)
    rank = np.count_nonzero(s > 1e-10 * s[0])
    return (u[:, :rank], s)

def setup(n, m):
    states = np.array(list(itertools.product(range(n), repeat=m)))
    index = {tuple(x): k for k, x in enumerate(states)}
    size = len(states)
    contrasts = np.vstack([np.eye(n - 1), -np.ones(n - 1)])
    f, _ = np.linalg.qr(contrasts)
    pairs = list(itertools.combinations_with_replacement(range(n - 1), 2))
    raw = []
    for a, b in pairs:
        entries = np.zeros(size)
        for r, s in itertools.combinations(range(m), 2):
            entries += f[states[:, r], a] * f[states[:, s], b] if a == b else (f[states[:, r], a] * f[states[:, s], b] + f[states[:, r], b] * f[states[:, s], a]) / np.sqrt(2)
        raw.append(np.diag(entries).ravel())
    raw = np.stack(raw, axis=1) / np.sqrt(math.comb(m, 2) * n ** (m - 2))
    perms = []
    for p in itertools.permutations(range(m)):
        dest = [index[tuple(x[list(p)])] for x in states]
        a = np.zeros((size, size))
        a[dest, np.arange(size)] = 1
        perms.append(a.ravel())
    haar_basis, _ = column_basis(np.stack(perms, axis=1))
    removed = haar_basis @ (haar_basis.conj().T @ raw)
    centered = raw - removed
    q, _ = column_basis(centered)
    rr = np.array([a == b for a, b in pairs], float)
    claimed_gram = np.eye(len(pairs)) - np.outer(rr, rr) / (n * n - 1)
    gram_error = np.linalg.norm(centered.conj().T @ centered - claimed_gram)
    counts = np.stack([np.bincount(x, minlength=n) for x in states])
    balanced = np.all(counts[:, None] == counts[None, :], axis=2)
    cycle = np.array([index[tuple(np.roll(x, 1))] for x in states])
    cyc_error = max((np.linalg.norm(q[:, k].reshape(size, size)[np.ix_(cycle, cycle)] - q[:, k].reshape(size, size)) for k in range(q.shape[1])))
    add = []
    for a in range(n - 1):
        vals = f[states, a].sum(axis=1)
        add.append(np.diag(vals).ravel() / np.sqrt(m * n ** (m - 1)))
    add = np.stack(add, axis=1)
    if not q.shape[1] == n * (n - 1) // 2:
        raise RuntimeError('Exact/diagnostic check failed at source line 71')
    if not (gram_error < 1e-10 and cyc_error < 1e-10):
        raise RuntimeError('Exact/diagnostic check failed at source line 72')
    if not np.linalg.norm(q.conj().T @ add) < 1e-10:
        raise RuntimeError('Exact/diagnostic check failed at source line 73')
    if not np.linalg.norm(haar_basis.conj().T @ centered) < 1e-10:
        raise RuntimeError('Exact/diagnostic check failed at source line 74')
    if not np.linalg.norm(centered.reshape(size, size, -1)[~balanced]) < 1e-10:
        raise RuntimeError('Exact/diagnostic check failed at source line 75')
    return (q, add, balanced, cycle, f, dict(N=n, m=m, ordered_hilbert_dimension=size, full_replica_dimension=size ** 2, permutation_count=math.factorial(m), full_haar_span_rank=haar_basis.shape[1], sector_dimension=q.shape[1], true_gram_residual=float(gram_error), same_cycle_fixed_residual=float(cyc_error)))

def trace_on(columns, ut, cycle):
    size = ut.shape[0]
    return sum((np.vdot(columns[:, k].reshape(size, size), (ut @ columns[:, k].reshape(size, size) @ ut.conj().T)[np.ix_(cycle, cycle)]) for k in range(columns.shape[1])))

def run(n, m, rng):
    q, add, mask, cycle, f, result = setup(n, m)
    unitaries = [('identity', np.eye(n)), ('cyclic_permutation', np.roll(np.eye(n), 1, axis=0))]
    for k in range(2):
        u, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
        unitaries.append((f'complex_QR_{k}', u))
    result['unitary_controls'] = []
    for name, u in unitaries:
        ut = tensor_power(u, m)
        p = abs(u) ** 2
        t = f.T @ p @ f
        formula = 0.5 * (np.trace(t) ** 2 + np.trace(t @ t)) + np.linalg.norm(t) ** 2 / (n * (n - 1)) - 1 / n
        direct = trace_on(q, ut, cycle)
        additive = trace_on(add, ut, cycle)
        power_trace = np.trace(np.linalg.matrix_power(u, m))
        local_diag = ut[cycle, np.arange(n ** m)]
        replica_direct = np.sum(local_diag[:, None] * local_diag[None, :].conj())
        row = dict(name=name, direct_quadratic_trace=[float(direct.real), float(direct.imag)], formula=float(formula), trace_residual=float(abs(direct - formula)), additive_trace_residual=float(abs(additive - np.trace(t))), full_replica_trace_residual=float(abs(replica_direct - abs(power_trace) ** 2)), stochastic_nonsymmetry=float(np.linalg.norm(p - p.T)), stochastic_nonnormality=float(np.linalg.norm(p @ p.T - p.T @ p)))
        if not max((row[k] for k in ['trace_residual', 'additive_trace_residual', 'full_replica_trace_residual'])) < 1e-09:
            raise RuntimeError('Exact/diagnostic check failed at source line 115')
        result['unitary_controls'].append(row)
    if n % 2:
        j, k = np.meshgrid(np.arange(n), np.arange(n), indexing='ij')
        phase = -pow(8, -1, n) * (3 * j * j - 2 * j * k + 3 * k * k) % n
        met = np.exp(2j * np.pi * phase / n) / np.sqrt(n)
        mt = tensor_power(met, m)
        source = np.stack([(mask * (mt.conj().T @ q[:, k].reshape(n ** m, n ** m) @ mt)).ravel() for k in range(q.shape[1])], axis=1)
        vals = np.linalg.eigvalsh(source.conj().T @ source)
        expected = np.sort([0.0] * ((n - 1) ** 2 // 2) + [1 / n ** 2] + [1 / n] * ((n - 3) // 2))
        residual = float(np.max(abs(vals - expected)))
        addsource = max((np.linalg.norm(mask * (mt.conj().T @ add[:, k].reshape(n ** m, n ** m) @ mt)) for k in range(add.shape[1])))
        if not (residual < 1e-10 and addsource < 1e-10):
            raise RuntimeError('Exact/diagnostic check failed at source line 130')
        result['source_squared_singular_values'] = vals.tolist()
        result['source_spectrum_residual'] = residual
        result['additive_metaplectic_source_norm'] = float(addsource)
    return result

def run_all():
    start = time.perf_counter()
    rng = np.random.default_rng(621407)
    rows = [run(n, m, rng) for n, m in [(3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (5, 2), (5, 3), (9, 2)]]
    out = dict(arithmetic='float64/complex128; diagnostic controls, not asymptotic proof', randomness='NumPy default_rng seed 621407; two independent complex QR controls per pair', construction='All slot permutations for full Haar projection; direct SVD for sector orthonormalization', runs=rows, runtime_seconds=time.perf_counter() - start)
    return out
