"""Exact arithmetic certificate and floating diagnostics for block memory.

Run from the repository root with OPENBLAS_NUM_THREADS=1 python
build/block-memory/verify.py. No conclusion is based on a floating comparison.
The large fixed-tau example is checked with Fraction, without a large matrix.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as Q
import importlib.util
import json
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALPHA = Q(43, 125)
F0 = Q(593, 500)


def pell(k):
    n, f = 1, 0
    for _ in range(k):
        n, f = n + 2 * f, n + f
    assert n * n - 2 * f * f == (-1) ** k
    return n, f


def prime(k):
    return k >= 2 and all(k % d for d in range(2, isqrt(k) + 1))


def matmul(a, b, n):
    return tuple(sum(a[2*i+l]*b[2*l+j] for l in range(2)) % n
                 for i in range(2) for j in range(2))


def coefficients():
    # The input has an independent comparison against frozen_sharp_return.py
    # in ../algebraic-return/coefficient_checks.json.
    src = HERE.parent / 'algebraic-return/exact_coefficients.py'
    spec = importlib.util.spec_from_file_location('exact_coefficients', src)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    coeff = module.frozen_coefficients()
    assert coeff.pop((0, 0)) == (Q(1, 10), Q(0))
    assert len(coeff) == 32
    for label, z in coeff.items():
        assert coeff[(-label[0], -label[1])] == (z[0], -z[1])
    assert max(abs(a)+abs(b) for a, b in coeff) == 9
    assert coeff[(0, 7)] == coeff[(0, -7)] == (Q(9, 20), Q(0))
    remainder = sum(abs(x)+abs(y) for v, (x, y) in coeff.items()
                    if v not in ((0, 7), (0, -7)))
    assert remainder == Q(143, 500)
    assert sum(abs(x)+abs(y) for x, y in coeff.values()) == F0
    assert Q(9, 20)*Q(7, 5)-remainder == ALPHA
    return coeff


def decimal(q):
    with localcontext() as ctx:
        ctx.prec = 45
        return str(Decimal(q.numerator)/Decimal(q.denominator))


def rational(q):
    return {'exact': str(q), 'decimal_display': decimal(q)}


def exact_checks():
    coefficients()
    rows = []
    for k in (5, 7, 11, 13, 17, 19, 41, 199):
        assert prime(k)
        n, f = pell(k)
        a = (1, 0, 0, 1)
        coprime_determinants = []
        for j in range(1, k+1):
            a = matmul(a, (3, 4, 2, 3), n)
            if j < k:
                determinant = (a[0]-1)*(a[3]-1)-a[1]*a[2]
                coprime_determinants.append(gcd(determinant, n))
        assert a == (1, 0, 0, 1)
        assert set(coprime_determinants) == {1}
        if k >= 13:
            assert n >= 144*k*k
        rows.append({'K': k, 'N': n, 'S_power_K_identity': True,
                     'all_nontrivial_fixed_spaces_zero': True,
                     'large_N_hypothesis': n >= 144*k*k})

    # A real failure when prime K is dropped: exactly 49 fixed Weyl labels.
    n, _ = pell(9)
    a = (1, 0, 0, 1)
    for _ in range(3):
        a = matmul(a, (3, 4, 2, 3), n)
    fixes = sum(((a[0]-1)*x+a[1]*y) % n == 0
                and (a[2]*x+(a[3]-1)*y) % n == 0
                for x in range(n) for y in range(n))
    assert fixes == 49
    assert gcd((a[0]-1)*(a[3]-1)-a[1]*a[2], n) == 7

    # Rational checks of all chosen constants.
    assert Q(16, 1)/ALPHA**2 < 144
    assert 144*ALPHA**2 > F0**2
    assert ALPHA**2/32 > Q(1, 300)
    assert Q(9, 110) < ALPHA/2
    assert Q(15, 11)**2 < 2
    k = 199
    n, f = pell(k)
    epsilon = Q(n, 10**80)
    eta = epsilon**2/300
    rho = k*epsilon*F0
    assert epsilon < Q(1, 10) and rho < Q(1, 4)
    retention = 1-4*rho**2
    pi_upper = Q(1, k)+Q(1, n)
    # exp(-n*eta) <= 1/(1+n*eta); there is no floating exponential.
    markov_error = 1/(1+n*eta)
    discrepancy = retention-pi_upper-markov_error
    assert retention > Q(9987680352, 10**10)
    assert discrepancy > Q(9937, 10000)
    invariant_weight = (1-2*rho**2)**2
    memory_error = (1+1/invariant_weight)/n
    memory_lower = eta-memory_error
    assert memory_lower > 0
    assert memory_error/eta < Q(15, 10**66)
    return {
        'evidence': 'integer and Fraction computations; no floating decisions',
        'centered_terms': 32, 'F0': str(F0), 'alpha': str(ALPHA),
        'arithmetic_rows': rows,
        'composite_period_negative_control': {
            'K': 9, 'N': 1393, 'j': 3, 'fixed_labels': fixes,
            'trace_modulus': 7,
            'meaning': 'the prime-period twisted trace bound fails'},
        'fixed_tau_instance': {
            'K': k, 'N': n, 'F': f, 'tau': '1/10^80',
            'epsilon': rational(epsilon), 'K_epsilon_F0': rational(rho),
            'closed_retention_lower_all_integer_times': rational(retention),
            'N_eta': rational(n*eta),
            'pi_upper': rational(pi_upper),
            'markov_TV_upper_for_m_ge_N': rational(markov_error),
            'closed_vs_markov_TV_lower_for_m_ge_N': rational(discrepancy),
            'TV_strictly_greater_than_0.9937': True,
            'invariant_compression_lower': rational(invariant_weight),
            'Abel_memory_error_at_z_1_minus_1_over_N': rational(memory_error),
            'Abel_memory_error_divided_by_eta': rational(memory_error/eta),
            'Abel_memory_contrast_lower_at_Heisenberg_scale': rational(memory_lower),
            'scope': 'one finite dimension at actual fixed tau; not an asymptotic BGS counterexample'}}


def dense_checks(k, epsilon=0.03):
    import numpy as np
    from scipy.linalg import schur

    n, _ = pell(k)
    coeff = coefficients()
    x = np.arange(n, dtype=np.int64)
    phase = (-pow(8, -1, n)*(3*x[:, None]**2-2*x[:, None]*x[None, :]
                                +3*x[None, :]**2)) % n
    raw = np.exp(2j*np.pi*phase/n)/np.sqrt(n)
    identity = np.eye(n, dtype=complex)
    scalar = np.trace(np.linalg.matrix_power(raw, k))/n
    m = np.exp(-1j*np.angle(scalar)/k)*raw

    def weyl(a, b):
        out = np.zeros((n, n), dtype=complex)
        out[x, (x+a) % n] = np.exp(2j*np.pi*((b*(x+pow(2, -1, n)*a)) % n)/n)
        return out

    a = sum(complex(float(re), float(im))*weyl(*v)
            for v, (re, im) in coeff.items())
    hermitian_error = np.linalg.norm(a-a.conj().T, 2)
    assert hermitian_error < 1e-12
    a = (a+a.conj().T)/2
    omega = np.exp(2j*np.pi/k)
    powers = [identity]
    for _ in range(1, k):
        powers.append(powers[-1]@m)
    bases, projectors, dimensions = [], [], []
    for r in range(k):
        p = sum(omega**(-r*j)*powers[j] for j in range(k))/k
        p = (p+p.conj().T)/2
        values, vectors = np.linalg.eigh(p)
        w = vectors[:, values > 0.5]
        bases.append(w)
        projectors.append(w@w.conj().T)
        dimensions.append(w.shape[1])
    dimensions = np.array(dimensions)
    w = np.column_stack(bases)
    slices = [slice(int(sum(dimensions[:r])), int(sum(dimensions[:r+1])))
              for r in range(k)]
    basis_error = np.linalg.norm(w.conj().T@w-identity, 2)
    assert basis_error < 1e-11 and sum(dimensions) == n
    eig, vec = np.linalg.eigh(a)
    d = (vec*np.exp(1j*epsilon*eig))@vec.conj().T
    b = d-identity

    def probabilities(operator_in_block_basis):
        return np.array([[np.linalg.norm(operator_in_block_basis[r, s], 'fro')**2
                          /dimensions[j] for j, s in enumerate(slices)]
                         for r in slices])

    t = probabilities(w.conj().T@d@w)
    pi = dimensions/n
    assert np.max(abs(t.sum(axis=0)-1)) < 1e-11
    assert np.max(abs(t@pi-pi)) < 1e-11
    u = d@m
    triangular, z = schur(u, output='complex')
    eigenvalues = np.diag(triangular)
    schur_error = np.linalg.norm(u-(z*eigenvalues)@z.conj().T, 2)
    assert schur_error < 1e-11
    z_in_blocks = w.conj().T@z
    theta = np.angle(eigenvalues)
    closed_bound = 1-4*(k*epsilon*float(F0))**2
    observations = []
    for time in sorted(set([1, n, *np.unique(np.rint(np.geomspace(2, 500000, 55)).astype(int))])):
        closed_u = (z_in_blocks*np.exp(1j*int(time)*theta))@z_in_blocks.conj().T
        c = probabilities(closed_u)
        markov = np.linalg.matrix_power(t, int(time))
        # Powering a floating stochastic matrix propagates a small column drift.
        drift = float(np.max(abs(markov.sum(axis=0)-1)))
        assert drift < 1e-7
        tv = 0.5*np.sum(abs(c-markov), axis=0)
        observations.append({
            'm': int(time), 'min_closed_diagonal': float(np.diag(c).min()),
            'max_markov_diagonal': float(np.diag(markov).max()),
            'min_TV_closed_vs_markov': float(tv.min()),
            'max_markov_TV_to_pi': float((0.5*np.sum(abs(markov-pi[:, None]), axis=0)).max()),
            'markov_column_drift': drift})
        assert np.diag(c).min() >= closed_bound-1e-8
        if time == 1:
            assert abs(c-t).max() < 1e-11

    charge_masses, edge_errors = [], []
    bb = w.conj().T@b@w
    aa = w.conj().T@a@w
    for charge in range(1, k):
        mass_a = sum(np.linalg.norm(aa[slices[(s+charge) % k], slices[s]], 'fro')**2
                     for s in range(k))/n
        mass_b = sum(np.linalg.norm(bb[slices[(s+charge) % k], slices[s]], 'fro')**2
                     for s in range(k))/n
        charge_masses.append(float(np.sqrt(k*mass_a)))
        assert np.sqrt(k*mass_a) >= float(ALPHA)-1e-10
        assert np.sqrt(k*mass_b) >= float(ALPHA)*epsilon/2-1e-10
        for s in range(k):
            r = (s+charge) % k
            edge_errors.append(abs(t[r, s]*dimensions[s]-n*mass_b/k))
    assert max(edge_errors) <= 2*epsilon**2+1e-10
    cov_error = max(np.linalg.norm(m@weyl(*v)@m.conj().T
                        -weyl(3*v[0]+4*v[1], 2*v[0]+3*v[1]), 2)
                    for v in ((1, 0), (0, 1), (0, 7)))
    trace_error = max(abs(abs(np.trace(weyl(*v)@powers[j]))-1)
                      for v in ((0, 0), (0, 7), (1, 1)) for j in range(1, k))
    assert cov_error < 1e-11 and trace_error < 1e-10

    # Ordinary (unnormalized) Hilbert--Schmidt isometry. These are the
    # P_s/sqrt(d_s) vectors expressed in the eigenmatrix basis of Ad_U.
    jmat = np.column_stack([(z.conj().T@p@z/np.sqrt(dimensions[s])).reshape(-1)
                            for s, p in enumerate(projectors)])
    assert np.linalg.norm(jmat.conj().T@jmat-np.eye(k), 2) < 1e-11
    adjoint_phases = np.exp(1j*(theta[:, None]-theta[None, :])).reshape(-1)
    f_coarse = t*np.sqrt(dimensions[None, :]/dimensions[:, None])
    assert np.linalg.norm(jmat.conj().T@(adjoint_phases[:, None]*jmat)-f_coarse, 2) < 1e-11
    rho = k*epsilon*float(F0)
    c_lower = (1-2*rho*rho)**2
    # Cluster matching is valid only under the smallness condition here.
    cluster_labels = np.abs(np.exp(1j*theta)[:, None]-omega**np.arange(k)[None, :]).argmin(axis=1)
    assert np.array_equal(np.bincount(cluster_labels, minlength=k), dimensions)
    q_projectors = [z[:, cluster_labels == s]@z[:, cluster_labels == s].conj().T
                    for s in range(k)]
    overlaps = np.array([[np.trace(p@q).real/np.sqrt(dimensions[r]*dimensions[s])
                          for s, q in enumerate(q_projectors)]
                         for r, p in enumerate(projectors)])
    assert np.linalg.norm(np.eye(k)-overlaps, 2) <= 2*rho*rho+1e-10
    assert np.linalg.svd(overlaps, compute_uv=False)[-1]**2 >= c_lower-1e-10
    memory_rows = []
    for time in (n, 5000, 500000):
        abel_z = 1-1/time
        g_compressed = jmat.conj().T@(jmat/(1-abel_z*adjoint_phases[:, None]))
        inverse_g = np.linalg.inv(g_compressed)
        self_energy = np.eye(k)-abel_z*f_coarse-inverse_g  # z^2 K(z)
        error = np.linalg.norm(self_energy-(np.eye(k)-f_coarse), 2)
        bound = (1-abel_z)*(1+1/c_lower)
        assert np.linalg.norm(inverse_g, 2) <= (1-abel_z)/c_lower+1e-10
        assert error <= bound+1e-10
        memory_rows.append({'Abel_time': time, 'z': abel_z,
                            'memory_difference_from_I_minus_F': float(error),
                            'proved_error_upper': bound})
    return {
        'evidence': 'floating diagnostics only, not certification',
        'K': k, 'N': n, 'epsilon': epsilon,
        'original_fixed_tau': False,
        'large_N_hypothesis_for_proved_Doeblin_constant': n >= 144*k*k,
        'retention_smallness_hypothesis': k*epsilon*float(F0) <= 0.25,
        'dimensions': dimensions.tolist(),
        'errors': {'covariance': float(cov_error), 'twisted_trace': float(trace_error),
                   'block_basis_unitarity': float(basis_error),
                   'Schur_diagonalization': float(schur_error),
                   'edge_expansion_max_remainder': float(max(edge_errors))},
        'minimum_sqrt_K_charge_A_norm': min(charge_masses),
        'observed_Doeblin_coefficient': float((t/pi[:, None]).min()),
        'closed_diagonal_rigorous_lower_bound': closed_bound,
        'pi_max': float(pi.max()), 'observations': observations,
        'memory': {'invariant_compression_proved_lower': c_lower,
                   'observed_cluster_overlap_min_singular_squared': float(np.linalg.svd(overlaps, compute_uv=False)[-1]**2),
                   'Abel_checks': memory_rows}}


def plot(rows):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    row = rows[-1]
    obs = row['observations']
    fig, ax = plt.subplots(figsize=(8.2, 4.8), layout='constrained')
    times = [o['m'] for o in obs]
    ax.semilogx(times, [o['min_closed_diagonal'] for o in obs],
                color='#1a628b', lw=2, label='Closed evolution: minimum block return')
    ax.semilogx(times, [o['max_markov_diagonal'] for o in obs],
                color='#d77425', lw=2, label='Repeated reset: maximum block return')
    ax.axhline(row['pi_max'], color='#606872', ls=':', label='Largest stationary block mass')
    ax.set(xlabel='Number of quantum steps', ylabel='Probability', ylim=(-0.02, 1.04),
           title=f"Coherent memory survives coarse Markov mixing\nN={row['N']}, K={row['K']}, epsilon={row['epsilon']} (finite diagnostic)")
    ax.legend(loc='center left', frameon=False, fontsize=9)
    ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(HERE/'block_memory.png', dpi=180)
    fig.savefig(HERE/'block_memory.svg')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact-only', action='store_true')
    args = parser.parse_args()
    exact = exact_checks()
    (HERE/'exact_certificate.json').write_text(json.dumps(exact, indent=2)+'\n')
    print('Exact arithmetic and fixed-tau finite certificate: PASS')
    if not args.exact_only:
        rows = [dense_checks(5), dense_checks(7)]
        (HERE/'dense_diagnostics.json').write_text(json.dumps(rows, indent=2)+'\n')
        plot(rows)
        for row in rows:
            print(json.dumps({'N': row['N'], 'K': row['K'], 'errors': row['errors'],
                              'last_observation': row['observations'][-1]}))
