"""Write v5_integration/receipt.json and SHA256_v5_integration.txt (+ .sha256 pin) for the Line N v5 integration.
Run from the repository root. Hashes every file added by the integration (except the receipt, the manifest and its pin)."""
import hashlib, json, subprocess, pathlib
E = pathlib.Path('evidence/executions/20261101/lineNgas/v5_integration')
D = 'computations/verification/lineN_theorem_draft'
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
claims = {c['id']: c for c in json.load(open('record/claims.json'))['claims']}
ids = [299, 300, 301, 302, 318, 322, 323] + list(range(325, 334)) + [335, 336]
roots = [f'{D}/THEOREM_DRAFT_v5.md', f'{D}/THEOREM_DRAFT_v4_to_v5.diff', f'{D}/THEOREM_DRAFT_v5_lineN22_edits.diff', f'{D}/V5',
         f'{D}/integration_checks/proved_deps_gate_v5.py', f'{D}/integration_checks/proved_deps_gate_v5.log',
         'evidence/executions/20261101/lineNgas/N20', 'evidence/executions/20261101/lineNgas/N21',
         'evidence/executions/20261101/lineNgas/referee', str(E),
         'formalization/Bgs/LineN20Arith.lean', 'formalization/Bgs/LineN20TailArith.lean', 'formalization/Bgs/LineN21Arith.lean',
         'evidence/source_metadata/registry_metadata_20261101_lineNv5.json', 'record/audits/metadata_cache_refresh_20261101_lineNv5/report.md']
skip = {str(E / 'receipt.json'), str(E / 'SHA256_v5_integration.txt'), str(E / 'SHA256_v5_integration.txt.sha256')}
files = sorted(f for f in subprocess.run(['git', 'ls-files', '--cached', '--others', '--exclude-standard', *roots],
               capture_output=True, text=True, check=True).stdout.split() if f not in skip)
man = ''.join(f'{sha(f)}  {f}\n' for f in files)
(E / 'SHA256_v5_integration.txt').write_text(man)
(E / 'SHA256_v5_integration.txt.sha256').write_text(f"{hashlib.sha256(man.encode()).hexdigest()}  SHA256_v5_integration.txt\n")
rec = {
  'schema': 'bgs.lineN.v5_integration.receipt/1',
  'date': '2026-11-01',
  'base': 'origin/main 7a0e9c5d (layout precedent: PR #67, merge 3531d83e)',
  'theorem_draft': {'repo_copy': f'{D}/THEOREM_DRAFT_v5.md', 'sha256': sha(f'{D}/THEOREM_DRAFT_v5.md'),
                    'author_original_sha256': '69bdea020f487c4502a24d1165786b6ee684d6c91ff614b05fa00133b8998ae4',
                    'edits': 'referee lineN22 E1-E8 verbatim (THEOREM_DRAFT_v5_lineN22_edits.diff)'},
  'referee': {'final': 'evidence/executions/20261101/lineNgas/referee/lineN22/REPORT.md', 'verdict': 'GO after E1-E12',
              'prior': ['lineN20', 'lineN21', 'lineN21b']},
  'claims': {f'BGS-TRACE-{i:03d}': {'state': claims[f'BGS-TRACE-{i:03d}']['state'],
                                    'dependencies': claims[f'BGS-TRACE-{i:03d}']['dependencies']} for i in ids},
  'errata': ['ERR-065 (proposed BGS-TRACE-334 not registered; authority N21/REPORT_N21_v2.md)'],
  'lean': {'files': ['formalization/Bgs/LineN20Arith.lean', 'formalization/Bgs/LineN20TailArith.lean', 'formalization/Bgs/LineN21Arith.lean'],
           'theorems': 54, 'axioms_subset_of': ['propext', 'Classical.choice', 'Quot.sound'], 'sorry': 0, 'native_decide': 0,
           'toolchain': 'leanprover/lean4:v4.33.1', 'build_log': str(E / 'lake_build_Bgs.log'),
           'build_result': 'Build completed successfully (8862 jobs), exit 0'},
  'proved_deps_gate': {'log': str(E / 'proved_deps_gate_v5.log'), 'result': 'GATE_OK', 'new_violations': 0, 'pre_existing_violations': 7},
  'manifest': {'path': str(E / 'SHA256_v5_integration.txt'), 'sha256': hashlib.sha256(man.encode()).hexdigest(), 'files': len(files)},
}
for k in ['lake_build_Bgs.log', 'lake_build_new_modules.log', 'lake_cache_get.log', 'checks_branch.log', 'checks_main_7a0e9c5d.log',
          'unittests_branch.txt', 'unittests_main_7a0e9c5d.txt', 'proved_deps_gate_v5.log', 'manifests.log', 'README.md', 'EXCLUDED.md']:
    if (E / k).exists(): rec.setdefault('sha256', {})[k] = sha(E / k)
(E / 'receipt.json').write_text(json.dumps(rec, indent=2, ensure_ascii=False) + '\n')
print(len(files), 'files; manifest', rec['manifest']['sha256'])
