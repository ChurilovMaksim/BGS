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
ORIGINAL_COMPARE = historical.compare
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
    expected['mathematics/actual_charge_radial_resolvent.md']='mathematics/fixed-map/actual_charge_radial_resolvent.md'
    # Wave 3 (c): the live fixed-map file was rephrased by phase 3
    # ('Self-review only' -> 'Author check only'), so it no longer matches
    # the pinned digest (eccca8...). The pinned bytes survive verbatim in
    # the Wave 2 archive copy (same bytes the RC gate resolves to); the
    # live file is deliberately NOT reverted. The bindings file carries the
    # identical resolution, and sealed_source_bytes requires exact equality.
    expected['mathematics/actual_charge_radial_shell.md']='archive/evidence/research_checkpoint_20261007/pinned/mathematics_actual_charge_radial_shell.md'
    expected['mathematics/fixed_map_path_model.md']='mathematics/fixed-map/fixed_map_path_model.md'
    expected['mathematics/four_branch_parametrix.md']='mathematics/fixed-map/four_branch_parametrix.md'
    expected['mathematics/fractional_hamming_cancellation.md']='mathematics/fixed-map/fractional_hamming_cancellation.md'
    expected['mathematics/literal_fixed_word_freeness.md']='mathematics/fixed-map/literal_fixed_word_freeness.md'
    expected['mathematics/literal_growing_word_window.md']='mathematics/fixed-map/literal_growing_word_window.md'
    # final-polish-1 (2026-11-01): commit 3f1858b6 (2026-10-28) repaired two
    # relative links in the live fixed-map copy, so it no longer matches the
    # pinned digest (3a589f...). The pinned bytes survive verbatim in the
    # schur_reduction pinned tree (same tree as the governance files above);
    # the live file is deliberately NOT reverted, exactly as for radial_shell.
    expected['mathematics/position_chain_mixing.md']='archive/evidence/schur_reduction_20261007/raw/review/pinned/BGS/mathematics/position_chain_mixing.md'
    expected['mathematics/reversed_path_decay.md']='mathematics/fixed-map/reversed_path_decay.md'
    expected['mathematics/onestep_charge_gap.md']='mathematics/fixed-map/onestep_charge_gap.md'
    # Wave 5 (2026-10-25): the fourteen-note trace-bridge move. Six
    # wave2-pinned notes relocated byte-identically to mathematics/
    # trace-bridge/ (pins unchanged); the two link-blocked notes
    # (balanced_pair, global_switch) resolve to their pre-move pinned
    # bytes, exactly as radial_shell does above. The wave2 scoped
    # bindings are deliberately NOT rewritten: their source fields are
    # logical keys into the sealed inputs dict, resolved here.
    expected['mathematics/bosonic_body_radial_translation.md']='mathematics/trace-bridge/bosonic_body_radial_translation.md'
    expected['mathematics/compact_phase_pair_identity.md']='mathematics/trace-bridge/compact_phase_pair_identity.md'
    expected['mathematics/complex_microscopic_phase_source_bounds.md']='mathematics/trace-bridge/complex_microscopic_phase_source_bounds.md'
    expected['mathematics/global_bosonic_body_coercivity.md']='mathematics/trace-bridge/global_bosonic_body_coercivity.md'
    expected['mathematics/real_absorption_body_coercivity.md']='mathematics/trace-bridge/real_absorption_body_coercivity.md'
    expected['mathematics/uniform_phase_pair_abel_bound.md']='mathematics/trace-bridge/uniform_phase_pair_abel_bound.md'
    expected['mathematics/balanced_pair_schur_reduction.md']='archive/evidence/research_checkpoint_20261007/pinned/mathematics_balanced_pair_schur_reduction.md'
    expected['mathematics/global_switch_transfer.md']='archive/evidence/research_checkpoint_20261007/pinned/mathematics_global_switch_transfer.md'
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


# Declared historical-pin translation for the rounding task ONLY (Wave 3, R1).
# The rounding checker only HASHES these files (rounding_review/
# check_companions.py: pins = {p: digest(ROOT/p)}); it never parses their
# content, and the mask/norm/split science is computed self-contained.
# The sealed expected pins are the 7-Oct-2026 bytes; the scoped pins are the
# current live-file hashes. The drift is the phase-2 move plus link-path
# translation, not a scientific change: for 3 of the 4 keys the sealed bytes
# survive verbatim in-tree (paths below) and differ from the live files only
# by link translations (verified by diff); the onestep sealed bytes are NOT
# recoverable anywhere in the tree, so that leg rests on the hash-only
# checker plus the within-policy numeric diagnostics alone, and this is
# stated, not hidden. The translation touches ONLY the comparison copy:
# raw expected/observed payloads are preserved, and the receipt records the
# true sealed pins plus this table. Any key outside this table, any sealed
# pin differing from the declared value, or any scoped pin differing from
# the runtime snapshot pin still fails closed below.
HISTORICAL_PIN_TRANSLATION = {
    # Sealed bytes survive at archive/evidence/charge_strengthening_20261007/
    # raw/author/inputs/18_microscopic_rounding_control.md (and the review
    # companion copy); live file differs only by fixed-map link translations.
    'mathematics/microscopic_rounding_control.md': (
        '68a0b67c6aaba5e5d1c6cb21cc4874a2a11e6e497b481e2212c821bde34c6889',
        '55480480a7914840160a8612d729a2abf1fc45af755a449997a53da9e8c638e9'),
    # Sealed bytes survive at evidence/research_checkpoint_20261007/raw/
    # bgs_astra_signed_boundary/inputs/11_fractional_hamming_cancellation.md;
    # live file differs only by relative-link translations.
    'mathematics/fractional_hamming_cancellation.md': (
        '10fd5b3e5d14d54c7d2b3ad2ace7b9d474a47f142b5a87e35fcf73b894ecaeb5',
        'bff2ecfde870b6ba39a5401debb0577cb8211e0d93981643565d934548e0abc3'),
    # Sealed bytes survive at evidence/wave2_checked_20261007/raw/
    # actual_one_pinch/packet/sources/mathematics/global_switch_transfer.md;
    # live file differs by exactly one link translation.
    'mathematics/global_switch_transfer.md': (
        '09662a4e6f81688a38c36be8429069f2e697377939f730a6dbf44e9b7b469f90',
        '127779b36d3bc3f74945716e03a64c629694fd3bfdf956adbac9f1c2f1651340'),
    # Sealed bytes NOT recoverable in-tree (full-tree hash scan, Wave 2
    # scoping): this leg rests on the hash-only checker plus the 19
    # within-policy numeric diagnostics, not on audited old bytes.
    'mathematics/onestep_charge_gap.md': (
        '15d713759394c52cf16665719e970189ef6dab9044e08e5b54bbb29243cfa747',
        '880efd145ccad9418213d6eed5450ad6783f7d24bce99713b830ee1d13c3ebe7'),
}


def portable_compare(expected, observed, task, context):
    """Preserve v1 comparison except the declared rounding pin translation.

    For the rounding task only, translate the expected manifest's
    source_pins for exactly the HISTORICAL_PIN_TRANSLATION keys from the
    sealed pins to the runtime scoped pins, in a deep copy. The v1
    comparator then validates the translated pins against the snapshot
    pins and the observed pins exactly as before; no expected value, no
    numeric diagnostic, and no other provenance field is touched. The
    returned receipt restores the TRUE sealed pins as expected provenance
    and records the translation, so the manifest shows both what was
    sealed and what the comparison projected.
    """
    if task.get('name') != 'rounding' or task.get('domain') != 'rounding':
        return ORIGINAL_COMPARE(expected, observed, task, context)
    if 'source_pins' not in task.get('provenance_fields', {}):
        return ORIGINAL_COMPARE(expected, observed, task, context)
    import copy as _copy
    expected_cmp = _copy.deepcopy(expected)
    observed_cmp = _copy.deepcopy(observed)
    historical.require(
        'snapshot_pins' in context,
        'rounding pin translation needs the runtime snapshot pins')
    historical.require(
        type(expected_cmp.get('source_pins')) is dict and
        type(observed_cmp.get('source_pins')) is dict,
        'rounding source pin map missing')
    sealed_pins = dict(expected_cmp['source_pins'])
    for key, (sealed, scoped) in HISTORICAL_PIN_TRANSLATION.items():
        historical.require(
            sealed_pins.get(key) == sealed,
            'undeclared historical pin translation: ' + key)
        historical.require(
            context['snapshot_pins'].get(key) == scoped,
            'scoped pin moved for translated key: ' + key)
        historical.require(
            observed_cmp['source_pins'].get(key) == scoped,
            'observed pin differs from scoped pin: ' + key)
        expected_cmp['source_pins'][key] = scoped
    changed = [k for k in sealed_pins
               if sealed_pins[k] != expected_cmp['source_pins'][k]]
    historical.require(
        sorted(changed) == sorted(HISTORICAL_PIN_TRANSLATION),
        'pin translation scope changed')
    details = ORIGINAL_COMPARE(expected_cmp, observed_cmp, task, context)
    details['expected_provenance']['source_pins'] = sealed_pins
    details['historical_pin_translation'] = {
        key: {'sealed_pin': sealed, 'scoped_pin': scoped,
              'comparison': 'declared_historical_pin_translation_v1',
              'raw_payloads_preserved': True}
        for key, (sealed, scoped) in HISTORICAL_PIN_TRANSLATION.items()}
    return details


@contextmanager
def portable_comparison_scope():
    historical.require(
        historical.compare_numeric_diagnostics is ORIGINAL_NUMERIC_COMPARE,
        'historical numeric comparator already overridden')
    historical.require(
        historical.compare is ORIGINAL_COMPARE,
        'historical provenance comparator already overridden')
    historical.compare_numeric_diagnostics = portable_numeric_compare
    historical.compare = portable_compare
    try:
        yield
    finally:
        historical.compare_numeric_diagnostics = ORIGINAL_NUMERIC_COMPARE
        historical.compare = ORIGINAL_COMPARE


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
