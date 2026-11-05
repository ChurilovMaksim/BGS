if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, hashlib, pathlib, subprocess
R = pathlib.Path('.'); E = 'evidence/executions/20261105/h7_scope'; V = 'computations/verification/h7_scope'
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
files = [str(p) for p in sorted(R.glob(f'{V}/**/*')) if p.is_file() and '__pycache__' not in str(p)]
files += ['formalization/Bgs/H7KpArith.lean'] + [str(p) for p in sorted(R.glob(E + '/**/*')) if p.is_file() and p.name != 'receipt.json' and '__pycache__' not in str(p)]
C = {c['id']: c for c in json.load(open('record/claims.json'))['claims']}
base = subprocess.check_output(['git', 'merge-base', 'HEAD', 'origin/main']).decode().strip()
enc = json.load(open(f'{V}/logs/h7_multidisc_enclose.json'))
kr = json.load(open(f'{E}/referee/mine/krawczyk_d34.json'))[0]
kl = json.load(open(f'{E}/referee/mine/krawczyk_l7_21_l7_13_l7_01.json'))
ka = json.load(open(f'{V}/logs/kp_arith.json'))
rec = {'schema': 'bgs-h7-scope-integration-receipt-v1', 'base': f'ChurilovMaksim/BGS origin/main {base[:8]}', 'branch': 'h7-scope-integration', 'prepared_on': '2026-11-05',
 'source': 'draft PR #85, branch research-grok46-1104, commit b8e91215, evidence/research/20261104_grok47/ (proofs h7_h8.md, h7_rates.md, h7_multidisc.md, h7_scope.md; code; logs); original HASHES.txt kept as ' + f'{V}/logs/pr85_HASHES.txt',
 'ids': {i: C[i]['state'] for i in ('BGS-TRACE-344', 'BGS-TRACE-345', 'BGS-TRACE-346', 'BGS-TRACE-347')},
 'next_free_id_check': 'origin/main 5d67f21c ends at BGS-TRACE-343; open PR branches #83, #84, #85 register no id >= 344',
 'unchanged_claims': {'BGS-TRACE-305': 'open (not edited; no amendment entry needed)', 'BGS-TRACE-325': 'conditional (not edited)', 'BGS-TRACE-206': 'open'},
 'referee': f'{E}/referee/AUDIT.md (hostile referee, 2026-11-05; nothing WRONG)',
 'referee_fixes_applied': ['1b: Lemma 3 excludes q = 2 (K_p odd)', '2d: d = 4663 at p = 7 (included, order 21, not searched); eighteen open conductors',
   '3c: newton_enclose error sums in arb; directed one-ulp float conversion', '4a: vertex-only wording; edge and trace-vs-radius [N]',
   '4c: TRACE-325 attribution; hypotheses needed at infinitely many primes; p_thr >= 1409 > 29', '4d: (i)-(iii)',
   'reproducibility: hard-coded /workspace sys.path replaced by file-relative paths (author code and referee krawczyk.py); __debug__ guard in every script'],
 'reruns': {
   'python': '3.13.5, python-flint 0.9.0 (arb), sympy 1.14.0, mpmath 1.3.0, numpy 2.3.5, scipy 1.17.0; OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1; 1 CPU',
   'kp_arith': {'command': f'python {V}/code/kp_arith.py', 'primes_checked_5_to_1999': ka['lemma_check_primes_5_to_1999'], 'orders_3p': len(ka['orders_included_conductors'])},
   'h7h8': {'command': f'python {V}/code/h7h8.py', 'log_identical_to_pr85': True},
   'h7_rates_self_test': {'command': f'python {V}/code/h7_rates.py self-test', 'log': f'{V}/logs/rerun/h7_rates_self_test.out', 'passed': True},
   'h7_rates_enclose': {'command': f'python {V}/code/h7_rates.py enclose --d D --bx BX --by BY --sectors 0 --squares 4 --out {V}/logs/rerun/orbit_D.json', 'logs': f'{V}/logs/rerun/orbit_*.json'},
   'h7_multidisc_enclose': {'command': f'python {V}/code/h7_multidisc_cert.py enclose', 'log': f'{V}/logs/h7_multidisc_enclose.json', 'pr85_log': f'{V}/logs/pr85_original/h7_multidisc_enclose.json',
      'orbits': {o['name']: {'lo': o['newton']['lo'], 'hi': o['newton']['hi'], 'h': o['newton']['h'], 'error_sums': o['newton'].get('error_sums')} for o in enc['orbits']},
      'tail_eps_hi': enc['tail']['eps_hi'], 'all_crossings_above_Tprime': all(o['newton']['lo'] > 1.42785 for o in enc['orbits'] if o['d'] != 7)},
   'referee_krawczyk': {'command': f'python {E}/referee/mine/krawczyk.py l7_21 l7_13 l7_01; ... d34', 'audit_run_logs': f'{E}/referee/mine/audit_run/',
      'd3437426497': [kr['rate_lo_f'], kr['rate_hi_f']], 'level7': {x['name']: [x['rate_lo_f'], x['rate_hi_f']] for x in kl}},
   'referee_ints': {'commands': [f'python {E}/referee/ints.py', f'python {E}/referee/ints2.py'], 'logs': [f'{E}/referee/ints.out', f'{E}/referee/ints2.out']}},
 'not_rerun': 'h7_rates.py survey/certify/wide/rays/rays-ext/rays-deep/climb and h7_multidisc.py float scans: logs are the PR #85 runs (code bytes differ only by the assertion guard, relative paths, the 4663 comment/constant/self-test and the arb error sums in newton_enclose)',
 'lean': {'files': ['formalization/Bgs/H7KpArith.lean'], 'theorems': 7, 'sorry': False, 'native_decide': False, 'axioms': 'none, except propext for seven_dvd_K_5 and seven_dvd_K_31 (Nat dvd decidability)',
   'build': f'{E}/lake_build_H7KpArith.log', 'scope': 'one build: lake build Bgs.H7KpArith (2 jobs), packages linked to /workspace/lineNgas/repo/formalization/.lake/packages; no new Mathlib cache; no full Bgs build'},
 'metadata_snapshot': 'evidence/source_metadata/registry_metadata_20261105_h7scope.json (transitive impact sets of 9 records gain BGS-TRACE-347 only)',
 'checks': f'{E}/checks/', 'sha256': {f: sh(f) for f in files}}
open(E + '/receipt.json', 'w').write(json.dumps(rec, indent=1, ensure_ascii=False) + '\n'); print(len(files))
