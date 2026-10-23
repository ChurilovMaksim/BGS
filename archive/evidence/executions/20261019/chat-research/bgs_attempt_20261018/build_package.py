"""Build a deterministic, complete scientific checkpoint outside BGS."""
import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / 'BGS_trace_laws_20261018.zip'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def eligible(path):
    relative = path.relative_to(ROOT)
    return (path.is_file() and not any(part.startswith('_save_helpers') or part == '__pycache__' for part in relative.parts)
            and path.name not in {ARCHIVE.name, 'archive_summary.json', 'SHA256SUMS'})


def main():
    baseline = ROOT.parent / 'bgs_continue_20261017' / 'research_checkpoint.json'
    parent_archive = baseline.parent / 'BGS_continuation_20261017.zip'
    source = ROOT.parent / 'upload' / 'two_channel_transmission(4).md'
    runs = {}
    for folder in ('run', 'trace_run', 'seed_run', 'seed_run_v2'):
        manifest_path = ROOT / folder / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        result_path = ROOT / folder / 'result.json'
        result = json.loads(result_path.read_text()) if result_path.exists() else None
        runs[folder] = {'execution_status': manifest['run']['status'], 'scientific_status': result.get('status') if result else None, 'manifest_sha256': digest(manifest_path), 'runtime_seconds': manifest['run']['runtime_seconds']}
    assert all(runs[name]['scientific_status'] == 'passed' for name in ('run', 'trace_run', 'seed_run_v2'))
    assert runs['seed_run']['execution_status'] == 'failed'
    integrity = json.loads((ROOT / 'repo_integrity.json').read_text())
    assert not any(integrity[key] for key in ('changed', 'missing', 'added'))
    checkpoint = {
        'checkpoint_id': 'BGS-TRACE-LAWS-20261018',
        'parent': {'checkpoint_path': str(baseline), 'sha256': digest(baseline), 'archive_sha256': digest(parent_archive)},
        'source_context': {'attachment': str(source), 'sha256': digest(source), 'nearest_scope': 'S1--S5, lines 6337--6425; previous joint law only for traces one and two'},
        'original_goal': 'OPEN; full BGS, generic two-port Haar law, and frozen TRACE-005 are not proved',
        'positive_results': [
            {'id': 'LOCAL-FULL-SYMPLECTIC-TRACE-LAW', 'status': 'AUTHOR_PROOF_SELF_REVIEWED', 'proof': 'secular_hierarchy_ru.md', 'scope': 'All fixed mixed moments; explicit O_L(1/N) error; all odd prime-power-square sizes'},
            {'id': 'LOCAL-SECULAR-GENERATING-SERIES', 'status': 'AUTHOR_PROOF_SELF_REVIEWED', 'proof': 'secular_hierarchy_ru.md', 'scope': 'Exact finite rank formula; evaluated coefficient-limit series; safe interior analytic limit'},
            {'id': 'LOCAL-BILINEAR-SEED-CLASSIFICATION', 'status': 'AUTHOR_PROOF_SELF_REVIEWED', 'proof': 'bilinear_seed_classification_ru.md', 'scope': 'All fixed trace moments for generic/symmetric/skew seeds of fixed size; symmetric case excluded from B-gap target'}
        ],
        'routes': [
            {'mechanism': 'Generate external mixing by root-phase commutators', 'outcome': 'Specified mechanism fails: vector fields commute', 'evidence': 'closure_audit_ru.md section 1', 'remaining': 'Emergent invariance using hidden-variable dynamics is not ruled out'},
            {'mechanism': 'Identify zero-absorption law from all strong-absorption asymptotics', 'outcome': 'Specified inference false; positive joint-law countermodel', 'evidence': 'closure_audit_ru.md section 2', 'remaining': 'Actual-model uniform boundary estimates not supplied'},
            {'mechanism': 'Evaluate admissible Fourier families by finite-field phase sums', 'outcome': 'Complete fixed-trace laws and coefficient series proved for the stated family', 'evidence': ['secular_hierarchy_ru.md', 'bilinear_seed_classification_ru.md'], 'remaining': 'Heisenberg observables and two-port transmission are not identified'}
        ],
        'checks': runs,
        'review': {'kind': 'author adversarial self-review', 'file': 'self_review.md', 'independent_referee': False, 'formal_assistant': False, 'literature_priority_verified': False},
        'repo_integrity': integrity,
        'next_unresolved_implication': 'Control microscopic boundary or conditional angular scattering law; neither fixed-degree moments nor analytic interior convergence alone gives it',
        'repo_mutations': False
    }
    (ROOT / 'research_checkpoint.json').write_text(json.dumps(checkpoint, indent=2, ensure_ascii=False) + '\n')
    paths = sorted((path for path in ROOT.rglob('*') if eligible(path)), key=lambda p: str(p.relative_to(ROOT)))
    sums = ''.join(f'{digest(path)}  {path.relative_to(ROOT)}\n' for path in paths)
    (ROOT / 'SHA256SUMS').write_text(sums)
    paths.append(ROOT / 'SHA256SUMS')
    with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in paths:
            info = zipfile.ZipInfo(str(path.relative_to(ROOT)), date_time=(2026, 10, 18, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == {str(path.relative_to(ROOT)) for path in paths}
        assert all(archive.read(str(path.relative_to(ROOT))) == path.read_bytes() for path in paths)
    summary = {'archive': str(ARCHIVE), 'files': len(paths), 'bytes': ARCHIVE.stat().st_size, 'sha256': digest(ARCHIVE), 'crc_and_member_bytes_verified': True}
    (ROOT / 'archive_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
