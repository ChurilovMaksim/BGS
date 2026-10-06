#!/usr/bin/env python3
"""Independent bounded regression oracles; no asymptotic spectral claims.

Checks use explicit failures so optimized Python cannot remove the tests.
"""
import importlib.util
from pathlib import Path
import sys
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('spectral_edge_test', ROOT/'computations/analysis/spectral_diagnostics.py')
m = importlib.util.module_from_spec(spec); sys.modules[spec.name] = m; spec.loader.exec_module(m)
from bgs.jacobi import jacobi_matrix, dlog_table, annihilator_indices, require_supported_prime, MAX_VECTORIZED_PRIME
from bgs.finite_field import (primitive_root, require_odd_prime, is_prime,
                              distinct_prime_factors, multiplicative_order)


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def rejects(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError(f'invalid input accepted: {fn.__name__} {args}')


def brute_window(levels, width):
    # Deliberately independent: full scan per anchor, with geometric predicates.
    counts = [sum(1 for point in levels if anchor <= point < anchor + width)
              for anchor in levels]
    mean = sum(counts) / len(counts)
    return sum((n - mean)**2 for n in counts) / len(counts)


def scalar_jacobi(p, dlog, chars, q):
    # Exact Python modular multiplication, independent scalar summation.
    return np.array([[sum(np.exp(2j*np.pi*((-int(k)*int(dlog[x]) + int(l)*int(dlog[x-1]))/(p-1)
                                          + (int(q)*x % p)/p)) for x in range(2,p))
                      for l in chars] for k in chars])


def main():
    for dtype in [int, np.int32, np.int64, np.uint32, np.uint64]:
        check(is_prime(dtype(199)), 'integer primality input')
        check(not is_prime(dtype(200)), 'integer composite input')
        check(distinct_prime_factors(dtype(198)) == [2, 3, 11], 'integer factor input')
        check(primitive_root(dtype(199)) == primitive_root(199), 'integer root input')
        check(multiplicative_order(dtype(139), dtype(199)) == 11, 'integer order input')
        require_odd_prime(dtype(199))
    for bad in [True, np.bool_(True), 199., np.float64(199), '199', np.array(199)]:
        for fn in [is_prime, require_odd_prime, distinct_prime_factors, primitive_root]:
            rejects(fn, bad)
        rejects(multiplicative_order, bad, 199)
        rejects(multiplicative_order, 139, bad)
    p=199; c=m.build_sector_context(p,11,139); d=dlog_table(p,primitive_root(p))
    j=lambda q:jacobi_matrix(p,11,139,d,c.character_indices,q)
    base=j(1); hbase=m.hermitian_matrix(c,1)
    for q in [1+199*2**50, 1-199*2**50, 1+199*10**100, 1-199*10**100, np.int64(1), np.uint64(1)]:
        check(np.array_equal(j(q),base),'Jacobi residue equivalence')
        check(np.array_equal(m.hermitian_matrix(c,q),hbase),'Hermitian residue equivalence')
    for q in [0,1,-1,7,198]:
        np.testing.assert_allclose(j(q),scalar_jacobi(p,d,c.character_indices,q),rtol=1e-11,atol=1e-11)
    for bad in [True,np.bool_(False),1.0,np.float64(1),'1',1+0j,None,np.array(1)]:
        rejects(j,bad); rejects(m.hermitian_matrix,c,bad)
        rejects(require_odd_prime,bad)
    for args in [(199.,11,139),(199,11.,139),(199,11,139.),(True,11,139)]:
        rejects(m.build_sector_context,*args)
    rejects(require_supported_prime,MAX_VECTORIZED_PRIME+1)
    rejects(dlog_table,MAX_VECTORIZED_PRIME+1,2)
    rejects(m.build_sector_context,MAX_VECTORIZED_PRIME+1,1,1)
    rejects(dlog_table,p,2.)
    for chars in [c.character_indices.astype(float),[[11]],np.array([True]),np.array([2**70],dtype=object)]:
        rejects(jacobi_matrix,p,11,139,d,chars,1)
    for bad_d in [d.astype(float), d.reshape(1,-1),np.full(p,2**62,dtype=np.int64)]:
        rejects(jacobi_matrix,p,11,139,bad_d,c.character_indices,1)
    rng=np.random.default_rng(20261006)
    cases=[[0,0,1,2],[0,0,0,0],[0,1,1,2,2,2],[0,1,2,3],[0,0,.5,1,1,2]]
    cases += [np.sort(rng.integers(-5,6,size=n)).tolist() for n in range(2,35)]
    cases += [m.unfold_monotone(np.array([0.,0.,1.,2.])).tolist()]
    for levels in cases:
        for width in [.25,.5,1,2,3,20]:
            got=m.forward_window_count_variance(levels,[width])[width]
            check(abs(got-brute_window(levels,width))<1e-12,'geometric window oracle')
    check(m.forward_window_count_variance([0,0,1,2],[1])[1]==.25,'reported tie counterexample')
    print('spectral integer and independent geometric window regressions: PASS')

if __name__=='__main__':
    main()
