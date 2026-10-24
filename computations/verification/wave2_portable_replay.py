#!/usr/bin/env python3
"""Wave2 portable successor: authenticated historical replay, basis-invariant split bounds.

All eight archived tasks execute with the original AST adapter, original
assertions, snapshots, source SHA seals, and raw output preservation. Only four
reference-equality diagnostics for Schur-degenerate, *basis-dependent* split
representations use the independently justified norm bounds below.

The historical Wave2 v1 entry point, bindings, evidence and printed reference
remain unchanged and may be executed separately on its original environment.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
import math
from pathlib import Path
import wave2_checked_replay as historical

ORIGINAL_NUMERIC_COMPARE = historical.compare_numeric_diagnostics
ORIGINAL_SOURCE_BYTES = historical.source_bytes
SPLIT_SAMPLES = ((5, 25), (11, 121))
BASIS_FIELDS = ('reverse_norm', 'P_centered_norm')
EXPECTED_TASKS = (
    'echo', 'centering', 'rounding', 'actual_one_pinch',
    'hook_bridge', 'hook_downstream', 'ward_covariance',
    'ward_permutations'
)


def sealed_source_bytes(root=historical.ROOT):
    """Resolve evolved governance paths without changing any historical seal."""
    bindings=historical.strict_json(historical.safe_path(root,historical.BINDINGS).read_bytes())
    historical.require(bindings['schema']=='bgs-wave2-replay-source-bindings-v1',
                       'unknown binding schema')
    resolutions=bindings.get('historical_resolutions',{})
    expected={rel:'archive/evidence/schur_reduction_20261007/raw/review/pinned/BGS/'+rel
              for rel in ('AGENTS.md','SOURCE_OF_TRUTH.md','record/repository_conventions.md')}
    expected['mathematics/microscopic_rounding_control.md']='mathematics/spectral-obstructions/microscopic_rounding_control.md'
    historical.require(resolutions==expected,'unreviewed historical input resolution')
    cached={}
    for rel,digest in bindings['files'].items():
        data=historical.safe_path(root,resolutions.get(rel,rel)).read_bytes()
        historical.require(historical.digest(data)==digest,'changed source: '+rel)
        cached[rel]=data
    historical.require(historical.CONTRACT in cached and historical.INPUTS in cached,
                       'missing contract/input closure')
    return cached


@contextmanager
def sealed_input_scope():
    historical.require(historical.source_bytes is ORIGINAL_SOURCE_BYTES,
                       'historical source loader already overridden')
    historical.source_bytes=sealed_source_bytes
    try:
        yield
    finally:
        historical.source_bytes=ORIGINAL_SOURCE_BYTES


def _split_invariant_bound(row, p, index):
    """Return the proven basis-independent perturbation bound for sample p.

    For p in {5,11}, the coordinatewise cubic map is a permutation of F_p^2
    and A-A^T has determinant four. Hence R(V)=V o conj(V^T) is a
    p^-1-scaled symplectic finite Fourier matrix and ||R(V)||_2=1/p.
    The Schur-product operator inequality gives
      ||R(W)-R(V)||_2 <= 2 ||W-V||_2 <= 2(epsilon+root_error).
    Likewise || |W|^2 - J ||_2 <= 2(epsilon+root_error).
    Numerical slack 2e-12 is explicit; the *original* P-bound and strict
    root-reconstruction bound are checked independently and never enlarged.
    """
    historical.require(type(row) is dict, 'split row is not a dictionary')
    historical.require(type(row.get('p')) is int and row['p'] == p,
                       'unexpected split prime/index')
    historical.require(type(row.get('N')) is int and row['N'] == p*p,
                       'unexpected split dimension')
    historical.require(p in (5, 11) and math.gcd(3, p-1)==1 and (4 % p)!=0,
                       'nonpermuting cubic coordinate or degenerate symplectic form')
    for field in ('epsilon', 'bound', 'root_reconstruction_error',
                  'reverse_norm', 'P_centered_norm'):
        historical.finite_diagnostic(row[field],
                                     f'/floating_split_controls/{index}/{field}')
    eps = row['epsilon']
    bound = row['bound']
    root = row['root_reconstruction_error']
    historical.require(root < 2e-12, 'original strict Schur root bound failed')
    historical.require(eps <= bound + 2e-12,
                       'original split epsilon bound failed')
    historical.require(row['P_centered_norm'] <= 2*bound + 4e-12,
                       'original split P-center bound failed')
    certified = 2*(eps+root)+2e-12
    historical.require(abs(row['reverse_norm']-1/p) <= certified,
                       'basis-invariant reverse Fourier norm bound failed')
    historical.require(row['P_centered_norm'] <= certified,
                       'basis-invariant intensity bound failed')
    return certified


def portable_numeric_compare(expected, observed, task):
    """Preserve v1 comparison except four explicitly named basis variants.

    Receives the comparison-only deep copies from historical.compare().
    Replacing fields in that private projection never alters raw evidence.
    """
    if task.get('name') != 'rounding':
        return ORIGINAL_NUMERIC_COMPARE(expected, observed, task)
    historical.require(task.get('domain') == 'rounding',
                       'portable policy restricted to historical rounding')
    declared = task.get('numeric_diagnostics')
    historical.require(type(declared) is dict and
                       declared == historical.numeric_diagnostic_specs('rounding'),
                       'rounding numeric policy changed or unlisted field')
    historical.require(
        type(expected.get('floating_split_controls')) is list and
        type(observed.get('floating_split_controls')) is list and
        len(expected['floating_split_controls']) ==
        len(observed['floating_split_controls']) == len(SPLIT_SAMPLES),
        'split sample count differs')

    basis_details = {}
    for i, (p, n) in enumerate(SPLIT_SAMPLES):
        erow = expected['floating_split_controls'][i]
        orow = observed['floating_split_controls'][i]
        historical.require(erow.get('N') == n and orow.get('N') == n,
                           'split sample N was changed')
        expected_bound = _split_invariant_bound(erow, p, i)
        observed_bound = _split_invariant_bound(orow, p, i)
        for field in BASIS_FIELDS:
            path = f'/floating_split_controls/{i}/{field}'
            historical.require(path in declared,
                               'undeclared basis-variant diagnostic')
            original = erow[field]
            actual = orow[field]
            basis_details[path] = {
                'comparison': 'basis_invariant_symplectic_fourier_norm_v2',
                'historical_v1_policy': declared[path],
                'expected': original,
                'observed': actual,
                'baseline_reverse_norm': 1/p if field == 'reverse_norm' else 0.0,
                'expected_certified_upper_deviation': expected_bound,
                'observed_certified_upper_deviation': observed_bound,
                'reference_equality_within_v1_tolerance':
                    abs(actual-original) <=
                    declared[path]['absolute_tolerance'] +
                    declared[path]['relative_tolerance']*abs(original),
                'raw_output_preserved': True,
            }
            # Only the comparison projection (not archived/observed raw JSON)
            # is normalized here, for the exact typed v1 comparison below.
            orow[field] = original

    details, relations = ORIGINAL_NUMERIC_COMPARE(expected, observed, task)
    for path, metric in basis_details.items():
        historical.require(path in details, 'missing v1 numeric diagnostic')
        details[path] = metric
    return details, relations


@contextmanager
def portable_comparison_scope():
    historical.require(
        historical.compare_numeric_diagnostics is ORIGINAL_NUMERIC_COMPARE,
        'historical numeric comparator already overridden')
    historical.compare_numeric_diagnostics = portable_numeric_compare
    try:
        yield
    finally:
        historical.compare_numeric_diagnostics = ORIGINAL_NUMERIC_COMPARE


def run(root=historical.ROOT, output=None):
    # An untouched, SHA-sealed v1 implementation and original task sources
    # are mandatory. An edit to the archived comparator makes this fail.
    sealed_source_bytes(root)
    with portable_comparison_scope(), sealed_input_scope():
        result = historical.run(root=root, output=output)

    names = tuple(row['name'] for row in result['tasks'])
    historical.require(names == EXPECTED_TASKS,
                       'portable replay did not execute all eight original tasks')
    roundrow = next(row for row in result['tasks'] if row['name']=='rounding')
    metrics = {
        p: d for p, d in roundrow['numeric_diagnostics'].items()
        if d.get('comparison')=='basis_invariant_symplectic_fourier_norm_v2'
    }
    historical.require(
        len(metrics)==4 and
        set(metrics)=={
            f'/floating_split_controls/{i}/{field}'
            for i in range(2) for field in BASIS_FIELDS
        },
        'portable basis exception scope changed')
    historical.require(result['original_sources_unchanged'] and
                       result['copied_inputs_authenticated'] and
                       result['expected_bytes_cached_before_execution'],
                       'historical Wave2 source/evidence verification failed')
    equal_v1 = all(x['reference_equality_within_v1_tolerance']
                   for x in metrics.values())
    roundrow['scientific_comparison_mode'] = (
        'authenticated_exact_v1_except_four_basis_invariant_schur_split_norms_v2'
    )
    result['schema'] = 'bgs-wave2-portable-replay-v2'
    result['scientific_equality'] = equal_v1
    result['historical_v1_numeric_reference_equality'] = equal_v1
    result['scientific_comparison_mode'] = (
        'strict_typed_exact_and_original_numerical_bounds_'
        'with_four_declared_basis_invariant_schur_split_norms'
    )
    result['historical_wave2_source_modified'] = False
    result['portable_baseline'] = (
        'p^-1 operator norm of finite symplectic Fourier reverse kernel; '
        'two-Lipschitz Schur product on contractions'
    )
    result['portability_scope'] = (
        'All eight authenticated original Wave2 controls, with a mathematical '
        'basis-independent bound in place of four noncanonical Schur-basis '
        'float-to-float equalities only. No new asymptotic result.'
    )
    if output is not None:
        target=Path(output)/'replay_manifest.json'
        target.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-sources',action='store_true')
    parser.add_argument('--output-dir',type=Path)
    args=parser.parse_args()
    if args.check_sources:
        sealed_source_bytes()
        print('Wave2 portable successor: original sealed source closure OK')
    else:
        result=run(output=args.output_dir)
        print('Wave2 portable replay: '+result['status']+
              ' ('+str(len(result['tasks']))+' original tasks, two split samples)')


if __name__ == '__main__':
    main()
