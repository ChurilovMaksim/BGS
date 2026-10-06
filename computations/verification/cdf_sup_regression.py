#!/usr/bin/env python3
"""Regression for both one-sided limits of the empirical CDF."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations/python'))
spec=importlib.util.spec_from_file_location('diagnostic_under_test',ROOT/'computations/analysis/spectral_diagnostics.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
def main():
    x=math.sqrt(-4*math.log(.2)/math.pi)
    assert abs(m.empirical_cdf_sup_distance(np.array([x]))-.8)<1e-12
    assert abs(m.empirical_cdf_sup_distance(np.array([x,x]))-.8)<1e-12
    assert m.empirical_cdf_sup_distance(np.array([0.]))==1.
    for bad in [[],[float('nan')],[float('inf')],[-1.]]:
        try:m.empirical_cdf_sup_distance(np.array(bad))
        except ValueError:pass
        else:raise AssertionError(('invalid gap sample accepted',bad))
    print('empirical CDF left/right jump regression: PASS')
if __name__=='__main__':main()
