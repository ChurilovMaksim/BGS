"""Audit weighted windows and distinguish parameter motion from random phases.

All phase centres below are auxiliary finite experiments. The original
tau=10^-80 is not resolved at these small dimensions.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
from pathlib import Path
import numpy as np
from weighted_probe import model, principal_minors, close_pairs

HERE = Path(__file__).resolve().parent


def brute_check():
    a, b = model(9)
    frequency, weights = principal_minors(a, b, 4)
    weights = weights*np.exp(1j*1.23*frequency)
    widths = [0.0, 1/81, 1/9, 1e3]
    fast = close_pairs(frequency, weights, widths, control_count=0)
    errors = []
    for width, row in zip(widths, fast):
        mask = np.tril(abs(frequency[:, None]-frequency[None, :]) <= width, -1)
        signed = float(2*np.real(np.sum((weights[:, None]*weights.conj()[None, :])[mask])))
        absolute = float(2*np.sum((abs(weights[:, None])*abs(weights[None, :]))[mask]))
        variance = float(2*np.sum((abs(weights[:, None]*weights[None, :])**2)[mask]))
        err = max(abs(row['signed_offdiagonal_sum']-signed),
                  abs(row['absolute_offdiagonal_sum']-absolute),
                  abs(row['independent_phase_standard_deviation']**2-variance))
        assert row['unordered_close_pairs'] == int(mask.sum())
        assert err < 2e-12
        errors.append(err)
    # Explicit coincident frequencies, a zero weight, negative/complex phases.
    frequency = np.array([-1., 0., 0., 1., 2.])
    weights = np.array([1, 2j, -3, 0, 4-1j])
    row = close_pairs(frequency, weights, [0.], control_count=0)[0]
    assert row['unordered_close_pairs'] == 1
    assert row['signed_offdiagonal_sum'] == 0
    assert row['absolute_offdiagonal_sum'] == 12
    assert abs(row['independent_phase_standard_deviation']**2-72) < 1e-12
    return {'max_error': max(errors), 'coincident_frequency_control': 'passed'}


def centres(n):
    a, b = model(n)
    frequency, weights = principal_minors(a, b, n//2)
    rows = []
    for t in [0., 0.1, 1., 10., 100.]:
        epsilon = t*n
        moved = weights*np.exp(1j*epsilon*frequency)
        window = close_pairs(frequency, moved, [1/n, 1/n**2], control_count=0)
        expanded = (-1)**(n//2)*np.sum(moved, dtype=np.clongdouble)
        u = np.exp(1j*epsilon*a)[:, None]*b
        direct = np.poly(np.linalg.eigvals(u))[n//2]
        residual = float(abs(expanded-direct))
        assert residual < 2e-8
        rows.append({'auxiliary_t': t, 'epsilon': epsilon,
                     'coefficient_absolute_squared': float(abs(expanded)**2),
                     'direct_coefficient_residual': residual, 'windows': window})
    return {'N': n, 'rows': rows}


if __name__ == '__main__':
    result = {'brute_audit': brute_check(),
              'finite_centres': [centres(n) for n in [15, 19, 23]],
              'scope': 'finite window sums; no claim about the frozen tau asymptotic'}
    (HERE/'center_checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['brute_audit']), flush=True)
    for block in result['finite_centres']:
        print(json.dumps({'N': block['N'], 'rows': [
            {'t': r['auxiliary_t'], 'c2': r['coefficient_absolute_squared'],
             'S_1_over_N': r['windows'][0]['signed_offdiagonal_sum'],
             'S_1_over_N2': r['windows'][1]['signed_offdiagonal_sum'],
             'phase_null_sd_1_over_N': r['windows'][0]['independent_phase_standard_deviation']}
            for r in block['rows']]}), flush=True)
