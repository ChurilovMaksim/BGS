"""Package this checkpoint; never mutates the BGS snapshot or prior roots."""
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WORK = ROOT.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    inputs = ROOT / 'inputs'
    inputs.mkdir(exist_ok=True)
    prior = WORK / 'bgs_attempt_20261018'
    bindings = []
    for filename in ['secular_hierarchy_ru.md', 'bilinear_seed_classification_ru.md',
                     'target_ru.md', 'research_checkpoint.json']:
        source = prior / filename
        destination = inputs / filename
        shutil.copyfile(source, destination)
        assert source.read_bytes() == destination.read_bytes()
        bindings.append({'source':str(source), 'copy':str(destination.relative_to(ROOT)),
                         'sha256':sha(source)})
    write_json(ROOT / 'source_bindings.json', {
        'parent_archive': str(prior / 'BGS_trace_laws_20261018.zip'),
        'parent_archive_sha256': sha(prior / 'BGS_trace_laws_20261018.zip'),
        'prior_proofs':bindings,
        'relation':'Extension of fixed traces to polynomial windows; no change of the original targets'
    })
    baseline = json.loads((WORK / 'bgs_focus_20261016' / 'repo_before.json').read_text())
    repo = WORK / 'BGS'
    current = {str(p.relative_to(repo)):sha(p) for p in sorted(repo.rglob('*')) if p.is_file()}
    integrity = {'baseline_count':len(baseline), 'current_count':len(current),
                 'added':sorted(set(current)-set(baseline)),
                 'missing':sorted(set(baseline)-set(current)),
                 'changed':sorted(k for k in set(current)&set(baseline) if current[k]!=baseline[k]),
                 'git_directory_present':(repo / '.git').exists()}
    integrity['unchanged'] = not (integrity['added'] or integrity['missing'] or integrity['changed'])
    write_json(ROOT / 'repo_integrity.json', integrity)
    assert integrity['unchanged'] and len(current) == 716

    runs = {}
    for folder in ('run','generic_run','completion_run'):
        manifest = json.loads((ROOT / folder / 'manifest.json').read_text())
        result = json.loads((ROOT / folder / 'result.json').read_text())
        assert manifest['run']['status'] == 'completed' and result['status'] == 'passed'
        runs[folder] = {'manifest_sha256':sha(ROOT / folder / 'manifest.json'),
                        'result_sha256':sha(ROOT / folder / 'result.json'),
                        'execution_status':manifest['run']['status'],
                        'finite_assertion_status':result['status'],
                        'runtime_seconds':manifest['run']['runtime_seconds']}
    write_json(ROOT / 'research_checkpoint.json', {
        'checkpoint':'BGS-BOUNDARY-20261018', 'date':'2026-10-18',
        'parent_checkpoint':'bgs_attempt_20261018/research_checkpoint.json',
        'parent_checkpoint_sha256':sha(prior / 'research_checkpoint.json'),
        'goal_status':{'full_BGS':'open', 'original_two_channel_limit':'open',
                       'general_ET_to_half':'open', 'admissible_counterexample':'not obtained'},
        'resolved_claims':[
            {'id':'SYM-POLY-MIXED', 'statement':'Long-cycle mixed moments have explicit error at L=o(N^(1/5))',
             'evidence':'proved', 'review':'author self-review', 'proof':'polynomial_trace_window_ru.md'},
            {'id':'GEN-POLY-MIXED', 'statement':'Generic fixed b bilinear seeds have explicit error at L=o(N^(1/(6b)))',
             'evidence':'proved', 'review':'author self-review', 'proof':'generic_bilinear_window_ru.md'},
            {'id':'FULL-OPEN-DISK', 'statement':'Corresponding characteristic polynomials converge in law in Hol(|z|<1)',
             'evidence':'proved', 'review':'author self-review',
             'restriction':'Fixed compact sets only; determinant second-moment convergence on the full disk not claimed'},
            {'id':'GAUSS-MAJORANT-BARRIER', 'statement':'Positive Gaussian majorant grows exponentially at c sqrt(N), c>e',
             'evidence':'proved', 'review':'author self-review', 'proof':'gaussian_comparison_boundary_ru.md'}
        ],
        'routes':[
            {'id':'rank-and-occupation-comparison', 'outcome':'partial theorem',
             'changed_decision':'Factorial counting replaced by principal-minor and matching encodings',
             'target':'Explicit growing trace laws for specified finite-field matrices'},
            {'id':'direct-analytic-tail', 'outcome':'partial theorem',
             'changed_decision':'Full open disk now reached by direct tails, not analytic continuation',
             'target':'Fixed-compact characteristic-polynomial convergence'},
            {'id':'positive-majorant-Heisenberg-extension', 'outcome':'refuted for this mechanism',
             'scope':'No bound on Gaussian majorant alone can approximate the physical ramp up to order N'},
            {'id':'literature-transfer', 'outcome':'no applicable theorem imported',
             'scope':'Tanner gives a conjecture; checked Wigner SFF hypotheses do not match DS Fourier data'}
        ],
        'continuation':{
            'unchanged_goal':'Microscopic universality and the original two-channel target',
            'first_missing_implication':'Uniform circular-phase cancellation at powers comparable to N',
            'do_not_repeat':'Do not extend the positive Gaussian bound to N; B1--B3 exclude that route alone',
            'candidate_next_work':'Retain exact occupation factorial corrections and unitary identities before absolute values',
            'open_disk_warning':'N-dependent z approaching the circle requires a new uniform estimate',
            'write_scope':'Scratch research only; BGS and remote repository remain paused'
        },
        'runs':runs, 'repo_integrity':integrity, 'priority_status':'not established',
        'new_subagents':0
    })
    excluded = {'BGS_mesoscopic_20261018.zip','archive_summary.json','SHA256SUMS'}
    files = [p for p in sorted(ROOT.rglob('*')) if p.is_file()
             and p.name not in excluded and not any(part.startswith('_save_helpers') for part in p.relative_to(ROOT).parts)]
    (ROOT / 'SHA256SUMS').write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in files))
    files.append(ROOT / 'SHA256SUMS')
    archive = ROOT / 'BGS_mesoscopic_20261018.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path in sorted(files):
            info = zipfile.ZipInfo(str(path.relative_to(ROOT)), date_time=(2026,10,18,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info,path.read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(files)
        for name in z.namelist():
            assert z.read(name) == (ROOT / name).read_bytes()
    summary = {'filename':archive.name, 'sha256':sha(archive), 'size_bytes':archive.stat().st_size,
               'members':len(files), 'crc_and_all_member_bytes_verified':True,
               'repo_unchanged':integrity['unchanged'], 'runs':runs}
    write_json(ROOT / 'archive_summary.json',summary)
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
