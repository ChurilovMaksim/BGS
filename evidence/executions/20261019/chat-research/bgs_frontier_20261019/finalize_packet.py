"""Audit unchanged evidence and package both research roots without ELF files.

This is a packaging operation, not a mathematical experiment. Run from this
file's parent project directory or by absolute filename. No BGS files are written.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import zipfile

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent
OLD = WORKSPACE / 'bgs_ward_20261019'
PREVIOUS_ARCHIVE = WORKSPACE / 'BGS_resummation_20261019.zip'
PREVIOUS_SHA = 'e206248a66e8e42dc329d411149e60d56f59f33d64e7ced96ed6241774f31f5e'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


def include(path):
    if not path.is_file() or any(x in {'__pycache__', '.git'} for x in path.parts):
        return False
    with path.open('rb') as stream:
        return stream.read(4) != b'\x7fELF'


def main():
    validator_path = Path('/root/.codex/plugins/cache/openai-curated-remote/mathbox/4.0.0/skills/computation-audit/scripts/validate_manifest.py')
    spec = importlib.util.spec_from_file_location('manifest_validator', validator_path)
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    audit = []
    for root in (OLD, HERE):
        for path in sorted(root.glob('*_run/manifest.json')):
            obj = json.loads(path.read_text())
            errors = validator.validate(obj, root=root, manifest_path=path)
            assert not errors, (str(path), errors)
            audit.append({'root': root.name, 'manifest': str(path.relative_to(root)),
                          'sha256': sha(path), 'status': obj['run']['status'],
                          'result': obj['result'], 'validated': True,
                          'runtime_seconds': obj['run']['runtime_seconds']})
    counts = Counter(row['status'] for row in audit)
    assert counts == {'completed': 16, 'timeout': 1}, counts
    assert sum(row['root'] == OLD.name for row in audit) == 11
    baseline = json.loads((WORKSPACE / 'bgs_focus_20261016/repo_before.json').read_text())
    actual = {str(path.relative_to(WORKSPACE / 'BGS')): sha(path)
              for path in (WORKSPACE / 'BGS').rglob('*') if path.is_file()}
    assert actual == baseline and len(actual) == 716
    assert sha(PREVIOUS_ARCHIVE) == PREVIOUS_SHA
    previous_members = 0
    with zipfile.ZipFile(PREVIOUS_ARCHIVE) as archive:
        assert archive.testzip() is None
        for info in archive.infolist():
            if info.is_dir():
                continue
            path = WORKSPACE / info.filename
            assert path.is_file() and path.read_bytes() == archive.read(info.filename), info.filename
            previous_members += 1
    assert previous_members == 104
    write('evidence_audit.json', {
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'validator': {'path': str(validator_path), 'sha256': sha(validator_path)},
        'all_manifests_valid': True, 'statuses': dict(counts), 'runs': audit,
        'repository': {'path': 'BGS', 'files': 716, 'equals_original_baseline': True,
                       'baseline_path': 'bgs_focus_20261016/repo_before.json',
                       'baseline_sha256': sha(WORKSPACE / 'bgs_focus_20261016/repo_before.json'),
                       'written': False, 'commits': False, 'pushes': False},
        'previous_delivery': {'archive': PREVIOUS_ARCHIVE.name, 'sha256': PREVIOUS_SHA,
                              'archive_crc_valid': True, 'distributed_files': previous_members,
                              'all_distributed_bytes_unchanged': True},
        'limits': ['Manifest validation proves recorded input/output integrity, not mathematical completeness',
                   'The timeout is retained and is not counted as a passed mathematical run',
                   'Review is self-review; no independent referee or Lean certificate']})
    proof_files = ['extremal_graphs_ru.md', 'second_defect_complete_ru.md',
                   'defect_two_cluster_gas_ru.md', 'self_review_ru.md']
    write('proof_scope.json', {
        'proof_revisions': {name: sha(HERE / name) for name in proof_files},
        'reviewer': 'author self-review, separate adversarial pass',
        'independent_review': False, 'formal_compilation': False, 'priority_established': False,
        'claims': [
            {'id': 'BGS-SATURATED-GRAPHS-G3-20261019', 'status': 'author_proof_self_review',
             'claim': 'Complete connected saturated support classification e=j+1 for j<=3 over all odd prime fields, with q<=16 for j=3',
             'proof': 'extremal_graphs_ru.md', 'finite_dependencies': ['catalogue_run', 'kernel_run', 'direct_four_run']},
            {'id': 'BGS-OPEN-FOUR-PORT-ZERO-20261019', 'status': 'author_computer_assisted_proof_self_review',
             'claim': 'All 24 connected (j,delta,e)=(3,2,4) open polynomials are central and divisible by 1-z; the physical quotient at 1 is -191/12',
             'proof': 'second_defect_complete_ru.md', 'finite_dependencies': ['kernel_run', 'direct_four_run', 'quartic_run']},
            {'id': 'BGS-COMPLETE-DEFECT-TWO-20261019', 'status': 'author_computer_assisted_proof_self_review',
             'claim': 'Full total-defect-two sector, all original orders and neutral decorations, has the stated limit for 0<tau<1',
             'proof': 'second_defect_complete_ru.md',
             'inherited_dependencies': ['../bgs_ward_20261019/defect_two_branches_ru.md', '../bgs_ward_20261019/p42_resummation_ru.md', '../bgs_ward_20261019/dependencies/companion_resummation_ru.md']},
            {'id': 'BGS-LOCAL-DEFECT-LE2-GAS-20261019', 'status': 'author_computer_assisted_proof_self_review',
             'claim': 'All neutral and arbitrarily many connected clusters of individual defect one or two: exact five-index sum, quartic-exponential limit for 0<tau<1/9, uniform tail and O(N^-1) rate',
             'proof': 'defect_two_cluster_gas_ru.md',
             'finite_dependencies': ['two_port_v2_run', 'quartic_run'],
             'limits': ['Does not include connected clusters of individual defect >=3', 'All corrections normalized to V_m/m', 'The range 1/9 is a sufficient majorant range, not a claimed singularity of the integral']},
            {'id': 'BGS-STABLE-DEGREE-2H-MINUS3-20261019', 'status': 'author_corollary_self_review',
             'claim': 'For each h>=3 and m>8h, the full stable coefficient polynomial has degree <=2h-3; vanishing is not claimed',
             'proof': 'second_defect_complete_ru.md'}],
        'full_goal': {'status': 'open', 'missing': ['all higher individual defects and joint remainder', 'higher mixed trace hierarchy and local statistics', 'transfer to the unchanged frozen family']}})
    inherited_proofs = {str(path.relative_to(OLD)): sha(path) for path in sorted(OLD.rglob('*.md'))}
    write('checkpoint.json', {
        'checkpoint_id': 'BGS-FRONTIER-G3-QUARTIC-20261019',
        'base': {'archive': PREVIOUS_ARCHIVE.name, 'sha256': PREVIOUS_SHA,
                 'previous_unsaved_packet': OLD.name, 'inherited_proof_hashes': inherited_proofs},
        'new_proof_hashes': {name: sha(HERE / name) for name in proof_files},
        'proof_scope_sha256': sha(HERE / 'proof_scope.json'),
        'evidence_audit_sha256': sha(HERE / 'evidence_audit.json'),
        'target': 'Full BGS for the unchanged requested target; auxiliary sector results do not replace it',
        'full_goal_status': 'open', 'repository_policy': 'read-only, no integration/commit/push',
        'live_handoff': 'continuation_ru.md',
        'routes': [
            {'id': 'saturated_graphs_and_open_kernels', 'status': 'open_with_new_partial_theorems',
             'done': 'All j<=3 saturated kernels; complete total defect 2',
             'next': 'Source (3,3,3), then first unknown saturated (4,3,5); general graph Ward identity remains unproved'},
            {'id': 'cluster_resummation', 'status': 'open_with_new_partial_theorem',
             'done': 'All individual defects <=2 in arbitrary counts, uniform for tau<1/9',
             'next': 'Control all further connected types and a single summable remainder'},
            {'id': 'Cauchy_local_transfer', 'status': 'open_deferred',
             'done': 'Local comparison for iid phases and a Hermitian involution',
             'obstruction': 'No matching microscopic universality theorem for the needed fixed dense S established here'},
            {'id': 'generic_cumulant_Ward', 'status': 'open_deferred',
             'done': 'Exact phase-cumulant recursion and zeros of j=2,3 kernels',
             'obstruction': 'No all-order admissible graph surgery preserving ranks and actual weights has been derived'}],
        'counterevidence_to_overclaim': 'Partial L_le2 has coefficient -3 tau^3; missing kernels cannot be assigned by CUE fitting',
        'review': {'self_review': True, 'independent': False, 'lean_compiled': False, 'novelty_established': False}})
    report = WORKSPACE / 'BGS_frontier_result_20261019_ru.md'
    shutil.copyfile(HERE / 'result_ru.md', report)
    files = [path for root in (OLD, HERE) for path in sorted(root.rglob('*'))
             if include(path) and path != HERE / 'inventory.json']
    write('inventory.json', {
        'schema': 1, 'hash_algorithm': 'sha256',
        'scope': 'Both research roots; inventory excludes itself; compiled ELF executables and caches are omitted',
        'files': {str(path.relative_to(WORKSPACE)): {'sha256': sha(path), 'bytes': path.stat().st_size} for path in files},
        'separate_report': {'filename': report.name, 'sha256': sha(report)},
        'source_file_count_excluding_inventory': len(files)})
    files.append(HERE / 'inventory.json')
    archive_path = WORKSPACE / 'BGS_frontier_20261019.zip'
    with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            archive.write(path, str(path.relative_to(WORKSPACE)))
    with zipfile.ZipFile(archive_path) as archive:
        assert archive.testzip() is None
        for path in files:
            assert archive.read(str(path.relative_to(WORKSPACE))) == path.read_bytes()
    print(json.dumps({'status': 'audited_and_packaged', 'successful_runs': counts['completed'],
                      'retained_timeouts': counts['timeout'], 'archive_files': len(files),
                      'archive': str(archive_path), 'archive_sha256': sha(archive_path),
                      'archive_bytes': archive_path.stat().st_size,
                      'report': str(report), 'report_sha256': sha(report),
                      'BGS_files_unchanged': len(actual)}, indent=2))


if __name__ == '__main__':
    main()
