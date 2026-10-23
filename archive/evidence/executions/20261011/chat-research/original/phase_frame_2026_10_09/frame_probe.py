"""Bounded exploratory controls for exact Schur phase mobility.

Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 frame_probe.py.
No conditional-law or universality claim follows from these finite samples.
"""
import json
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import schur

SEED = 202610091
rng = np.random.default_rng(SEED)


def haar(n):
    z = (rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)))/np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q*(np.diag(r)/np.abs(np.diag(r)))[None, :]


def fourier(n, broken):
    j = np.arange(n)
    columns = (j**3 % n) if broken else j
    assert len(np.unique(columns)) == n
    return np.exp(2j*np.pi*j[:, None]*columns[None, :]/n)/np.sqrt(n)


def hermitian_coordinates(rows):
    """Tr-orthonormal real coordinates of rank-one row*row projectors."""
    n, m = rows.shape
    columns = [np.abs(rows[:, a])**2 for a in range(m)]
    for a in range(m):
        for b in range(a+1, m):
            z = rows[:, a].conj()*rows[:, b]
            columns.extend([np.sqrt(2)*z.real, np.sqrt(2)*z.imag])
    return np.stack(columns, axis=1)


def cavity(w, m):
    n = len(w)
    order = rng.permutation(n)
    w = w[np.ix_(order, order)]
    e = n-m
    l = np.linalg.solve(np.eye(e)-w[:e, :e], w[:e, e:])
    s = w[e:, e:] + w[e:, :e]@l
    k = np.concatenate([l, np.eye(m)], axis=0)
    return s, l, k


def measure(s, l, k):
    n, m = k.shape
    t = k.conj().T@k
    h = (m/n)*t
    alpha = float(np.trace(h).real/m)
    st, v = schur(s, output='complex')
    angles = np.angle(np.diag(st)) % (2*np.pi)
    order = np.argsort(angles)
    angles, v = angles[order], v[:, order]
    p = np.abs(k@v)**2
    weights = np.einsum('ij,ij->i', k.conj(), k).real
    ash = (m/n)*(p.T@(p/weights[:, None]))
    direct = (np.abs(v)**2).T@(np.abs(v)**2)
    hv = v.conj().T@h@v
    gaps = np.diff(np.r_[angles, angles[0]+2*np.pi])*m/(2*np.pi)
    overlap = m*ash[np.arange(m), np.roll(np.arange(m), -1)]
    overlap_direct = m*direct[np.arange(m), np.roll(np.arange(m), -1)]
    # Right logarithmic retained directions are rows of S, not rows of I.
    rows = np.concatenate([l, s], axis=0)/np.sqrt(weights[:, None])
    x = hermitian_coordinates(rows)
    frame = (m/n)*(x.T@(weights[:, None]*x))
    hi, hz = np.linalg.eigh(h)
    hinvhalf = (hz*(1/np.sqrt(hi))[None, :])@hz.conj().T
    whitened_rows = rows@hinvhalf
    white_norms = np.sum(np.abs(whitened_rows)**2, axis=1)
    whitened_rows /= np.sqrt(white_norms[:, None])
    xw = hermitian_coordinates(whitened_rows)
    fw = (m/n)*(xw.T@((weights*white_norms)[:, None]*xw))
    eye_vector = np.r_[np.ones(m), np.zeros(m*m-m)]
    target = (np.eye(m*m)+np.outer(eye_vector, eye_vector))/(m+1)
    # A separate projector formula for the same frame energy; no spectral basis.
    out_b = np.concatenate([l, s], axis=0)
    projection = out_b@np.linalg.solve(t, out_b.conj().T)
    leverage = np.diag(projection).real
    frame_energy = float(np.sum(np.abs(projection)**4/(leverage[:, None]*leverage[None, :])))
    white_eigenvalues = np.linalg.eigvalsh(fw)
    checks = {
        'unitarity': float(np.linalg.norm(s.conj().T@s-np.eye(m))),
        'eigenvector_residual': float(np.linalg.norm(s@v-v@np.diag(np.exp(1j*angles)))),
        'row_sum': float(np.max(np.abs(ash.sum(axis=1)-np.diag(hv).real))),
        'weighted_frame_trace': float(abs(np.trace(frame)-np.trace(h).real)),
        'white_first_moment': float(np.linalg.norm((m/n)*(whitened_rows.conj().T@((weights*white_norms)[:, None]*whitened_rows))-np.eye(m))),
        'projector_frame_energy': float(abs(frame_energy-np.trace(fw@fw))),
        'frame_energy_defect': float(abs(frame_energy-2*m/(m+1)-np.linalg.norm(fw-target)**2)),
    }
    assert max(checks.values()) < 2e-8, checks
    return {
        'alpha': alpha,
        'clock_m2': float(np.trace(h@h).real/m),
        'clock_eigenbasis_diagonal_rms': float(np.linalg.norm(np.diag(hv).real-alpha)/np.sqrt(m)),
        'unwhitened_frame_relative_op_error': float((m+1)*np.linalg.norm(frame-target, ord=2)),
        'whitened_frame_relative_op_error': float((m+1)*np.linalg.norm(fw-target, ord=2)),
        'mobility_frobenius_error_times_m': float(m*np.linalg.norm(ash-(np.eye(m)+np.ones((m,m)))/(m+1))),
        'white_frame_numerical_rank': int(np.sum(white_eigenvalues>1e-9)),
        'white_frame_energy_defect': frame_energy-2*m/(m+1),
        'adjacent_clock_square': np.abs(hv[np.arange(m), np.roll(np.arange(m), -1)])**2,
        'gaps': gaps, 'overlap': overlap, 'overlap_direct': overlap_direct,
        'checks': checks,
    }


def summarize(records, n, m, model):
    scalar_keys = [k for k in records[0] if k not in ('gaps', 'overlap', 'overlap_direct', 'adjacent_clock_square', 'checks')]
    result = {'N': n, 'm': m, 'model': model, 'samples': len(records)}
    result['means'] = {k: float(np.mean([r[k] for r in records])) for k in scalar_keys}
    result['checks_max'] = {k: max(r['checks'][k] for r in records) for k in records[0]['checks']}
    gaps = np.concatenate([r['gaps'] for r in records])
    adaptive = np.concatenate([r['overlap'] for r in records])
    ordinary = np.concatenate([r['overlap_direct'] for r in records])
    clock = np.concatenate([r['adjacent_clock_square'] for r in records])
    result['gap_bins'] = []
    for lo, hi in [(0, .5), (.5, 1), (1, 1.5), (1.5, float('inf'))]:
        mask = (gaps>=lo)&(gaps<hi)
        result['gap_bins'].append({'lo': lo, 'hi': None if np.isinf(hi) else hi, 'count': int(mask.sum()),
            'adaptive_overlap': float(np.mean(adaptive[mask])) if mask.any() else None,
            'ordinary_overlap': float(np.mean(ordinary[mask])) if mask.any() else None,
            'adjacent_clock_square': float(np.mean(clock[mask])) if mask.any() else None})
    return result


def main():
    outputs = []
    # Every N is prime and 2 mod 3, so the cubic column map is a permutation.
    for n, m, count in [(101, 4, 48), (197, 4, 48), (389, 4, 48), (197, 8, 32), (389, 8, 32)]:
        for model in ('haar', 'broken_fourier', 'symmetric_fourier'):
            fixed = None if model == 'haar' else fourier(n, model == 'broken_fourier')
            records = []
            for _ in range(count):
                u = haar(n) if fixed is None else fixed
                w = np.exp(2j*np.pi*rng.random(n))[:, None]*u
                records.append(measure(*cavity(w, m)))
            result = summarize(records, n, m, model)
            outputs.append(result)
            print(json.dumps(result, ensure_ascii=False), flush=True)
    payload = {'seed': SEED, 'arithmetic': 'complex128, exploratory',
        'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__,
        'thread_caps': {'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'},
        'non_claim': 'Binned means are not the conditional covariance given all eigenangles; no BGS or limiting-law proof.',
        'results': outputs}
    Path(__file__).with_name('frame_probe_results.json').write_text(json.dumps(payload, indent=2)+'\n')


if __name__ == '__main__':
    main()
