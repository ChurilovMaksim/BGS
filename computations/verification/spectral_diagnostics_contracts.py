#!/usr/bin/env python3
"""Bounded float64 method-invariant checks; no asymptotic spectral claim."""
import importlib.util
from pathlib import Path
import sys
from unittest.mock import patch
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('spectral_under_test', ROOT/'computations/analysis/spectral_diagnostics.py')
m = importlib.util.module_from_spec(spec); sys.modules[spec.name] = m; spec.loader.exec_module(m)


def rejects(fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except ValueError:
        return
    raise AssertionError(f'invalid input accepted by {fn.__name__}')


def main():
    x = m.sector_eigenvalues(3571, 17, 2469, 1)
    legacy = m.unfold_polynomial(x)
    assert np.count_nonzero(np.diff(legacy) < 0) == 3
    assert abs(np.min(np.diff(legacy)) + .8672741671) < 1e-7
    rejects(m.forward_window_count_variance, legacy, [2])
    for factor in [.5, 1., 2.]:
        for edge in [0., .05, .1]:
            u = m.unfold_monotone(x, factor, edge)
            assert np.all(np.diff(u) > 0)
            g = m.normalized_gaps(x, factor, edge)
            assert abs(g.mean()-1) < 1e-12
            assert np.std(g) > .1  # Not rank-CDF constant gaps.
            np.testing.assert_allclose(u, m.unfold_monotone(7*x+3, factor, edge), atol=1e-12)
            np.testing.assert_allclose(u, m.unfold_monotone(x[::-1], factor, edge))
    for bad in [[], [1,2,3], [0,1,2,np.nan], [0,1,2,np.inf], [[1,2],[3,4]], [1]*4]:
        rejects(m.unfold_monotone, bad)
    for f in [0, -1, np.nan, np.inf]:
        rejects(m.unfold_monotone, x, f)
    for e in [-.1, .5, np.nan]:
        rejects(m.unfold_monotone, x, edge_fraction=e)
    rejects(m.unfold_monotone, np.arange(4.), edge_fraction=.49)
    for bad in [[1,0,2], [1,np.nan], []]:
        rejects(m.forward_window_count_variance, bad, [1])
    rejects(m.forward_window_count_variance, [0,1], [0])
    with patch.object(m, 'unfold_monotone', return_value=np.array([0., 2., 1., 3.])):
        rejects(m.normalized_gaps, np.arange(4.))
    tied = m.unfold_monotone(np.array([0., 0., 1., 4.]))
    assert tied[0] == tied[1] and np.all(np.diff(tied) >= 0)
    for a,b,status in [([1],[2],'insufficient_replicates'), ([1],[1,2],'insufficient_replicates'),
                       ([1,1],[2,2],'zero_spread'), ([1,1],[1,1],'zero_spread')]:
        row = m.descriptive_difference(a,b)
        assert row['descriptive_standardized_difference'] is None
        assert row['standardized_difference_status'] == status
    row = m.descriptive_difference([1,3],[2,4])
    assert abs(row['descriptive_sem_scale'] - np.sqrt(2)) < 1e-12
    assert abs(row['descriptive_standardized_difference'] - 1/np.sqrt(2)) < 1e-12
    one = m.matched_window_design(199,11,139,[1],[2,3],1,20260901)
    assert all(r['descriptive_standardized_difference'] is None for r in one['rows'])
    rejects(m.matched_window_design,199,11,139,[],[2],1,1)
    rejects(m.matched_window_design,199,11,139,[1],[2],0,1)
    print('spectral method invariants and negative regressions: PASS')

if __name__ == '__main__':
    main()
