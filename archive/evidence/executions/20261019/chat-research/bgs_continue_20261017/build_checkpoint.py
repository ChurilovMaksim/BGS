#!/usr/bin/env python3
"""Build the continuation's evidence index and deterministic archive, outside BGS."""
from pathlib import Path
import hashlib
import json
import zipfile

root=Path(__file__).resolve().parent
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def write(name,data):
    (root/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

inputs=json.loads((root/'proof_inputs.json').read_text())
for item in inputs['inputs']:
    assert digest(root/item['copy_path'])==item['sha256'],item
stars=json.loads((root/'star_run/result.json').read_text())
current=json.loads((root/'current_run/result.json').read_text())
assert stars['status']==current['status']=='passed'
for run in ('star','current'):
    manifest=json.loads((root/(run+'_run/manifest.json')).read_text())
    assert manifest['run']['status']=='completed'
integrity=json.loads((root/'repo_integrity.json').read_text())
assert integrity['unchanged'] and integrity['current_files']==716
sources=['uniform_heisenberg_path_current.md','tensor_path_current_limit.md',
         'rare_star_heisenberg.md','self_review.md','progress_ru.md',
         'remaining_task_ru.md','literature_scope.md']
write('proof_bindings.json',{
    'proofs':[{'path':name,'sha256':digest(root/name)} for name in sources],
    'base':inputs['base_checkpoint'],
    'finite_runs':[{'path':run+'_run/manifest.json',
                    'sha256':digest(root/(run+'_run/manifest.json')),
                    'scientific_result_sha256':digest(root/(run+'_run/result.json'))}
                   for run in ('star','current')],
    'interpretation':'Finite evidence supports the specified identities, not a BGS certificate.'})
write('evidence_summary.json',{
    'star':{'status':stars['status'],'cases':len(stars['finite_enumeration']),
            'rooted_words':stars['total_words_enumerated'],
            'signs_exact':stars['exact_sign_tests']},
    'current':{'status':current['status'],
               'rational_cases':len(current['rational_inner_cases']),
               'rational_identities':sum(x['identities'] for x in current['rational_inner_cases']),
               'polynomial_cases':current['polynomial_cases']},
    'manifest_validation':'Both v2 records validated with current input/output hashes.',
    'repo':integrity,
    'review':'Adversarial author self-review; no independent or formal certification.'})
write('research_checkpoint.json',{
    'checkpoint_id':'BGS-CONTINUE-20261017-TENSOR-CURRENT-STAR',
    'date':'2026-10-17','base':inputs['base_checkpoint'],
    'requested_goal':'Full BGS; live concrete obligation is the original two-channel phase model.',
    'goal_state':'open','two_port_mean_limit':'open',
    'claims':[
        {'id':'CONTINUE-TENSOR-CURRENT-FIXED-20261017',
         'state':'working_proof_self_reviewed','source':'tensor_path_current_limit.md',
         'input':'Finite unitary Schur transfer; no G.',
         'boundary':'Fixed colligation K->infinity; optional higher moments have explicit inputs.'},
        {'id':'CONTINUE-UNIFORM-FULL-CLOCK-20261017',
         'state':'conditional_working_proof_self_reviewed',
         'source':'uniform_heisenberg_path_current.md',
         'input':'Fixed-level TV compactness TC; prior R/G is a sufficient working input.',
         'boundary':'Any K_N->infinity; all positive averaged clock coordinates; no Haar identification.'},
        {'id':'CONTINUE-RARE-STAR-20261017',
         'state':'working_proof_self_reviewed','source':'rare_star_heisenberg.md',
         'input':'Classical all-m Ginibre moment formula; exact circular entry expansion.',
         'boundary':'Auxiliary Wick probability and iid nonunitary matrices only.'}],
    'routes':[
        {'mechanism':'One-step finite-channel recursion / Haar terminator',
         'state':'open_at_identification',
         'outcome':'Existing phase-sensitive cubic and cavity correlations are not eliminated by G.',
         'untried_next':'A new bound retaining coherent conditional directions, not a classical replacement.'},
        {'mechanism':'Positive tensor occupations and coherent sampling',
         'state':'partial_theorem_checkpoint',
         'outcome':'Fixed-mark uniform transfer and full averaged clock transfer proved under TC.',
         'remaining':'Identify endpoint marginal of (T_N,J_N); finite histogram e_N remains unestimated.'},
        {'mechanism':'Unrestricted exponential transfer from Wick Poisson collisions',
         'state':'refuted_at_stated_scope',
         'outcome':'Explicit star sector produces divergent exponential moments above its threshold.',
         'not_ruled_out':'A restricted small-tilt regime or tail-controlled entry class.',
         'resumption':'Prove an upper tail/rate with the exact star lower bound retained.'},
        {'mechanism':'Critical radial transform of the positive full path clock',
         'state':'open_at_evaluation',
         'outcome':'Exact interior formula (19) and conditional limit (20) established.',
         'remaining':'Evaluate the deterministic model at rho=exp(-lambda/[2K_N(N-2)]).',
         'next_check':'Match the actual physical-source product and its initial law before using prior source comparisons.'}],
    'next_obligation':'Prove e_N->0 for the positive finite Bernstein weights, or directly identify T_N from the exact cavity law.',
    'files':'README.md','repo_integrity':'repo_integrity.json',
    'not_performed':['Repository edits/commit/push','New subagents','Lean compilation',
                     'External referee or global priority verification']})

excluded={'BGS_continuation_20261017.zip','archive_summary.json','SHA256SUMS'}
paths=sorted(p for p in root.rglob('*') if p.is_file()
             and p.name not in excluded
             and not any(part.startswith('_save_helpers') or part=='__pycache__'
                         for part in p.relative_to(root).parts))
(root/'SHA256SUMS').write_text(''.join(digest(p)+'  '+str(p.relative_to(root))+'\n' for p in paths))
paths.append(root/'SHA256SUMS')
archive=root/'BGS_continuation_20261017.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as out:
    for path in sorted(paths):
        info=zipfile.ZipInfo(str(path.relative_to(root)),date_time=(2026,10,17,12,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644 << 16
        out.writestr(info,path.read_bytes())
with zipfile.ZipFile(archive) as check:
    assert check.testzip() is None
    assert len(check.infolist())==len(paths)
    for item in check.infolist():
        assert check.read(item.filename)==(root/item.filename).read_bytes()
summary={'files':len(paths),'bytes':archive.stat().st_size,'sha256':digest(archive),
         'CRC':'passed','member_byte_comparison':'passed'}
write('archive_summary.json',summary)
print(json.dumps(summary))
