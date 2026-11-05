if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, hashlib, pathlib, subprocess
R = pathlib.Path('.'); E = 'evidence/executions/20261105/h5_ceiling'; V = 'computations/verification/h5_ceiling'
NOTE = 'evidence/research/20261105_h5_ceiling/NOTE.md'; LEAN = 'formalization/Bgs/H5CeilingArith.lean'
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
files = [str(p) for p in sorted(R.glob(f'{V}/**/*')) if p.is_file() and '__pycache__' not in str(p)]
files += [LEAN, NOTE] + [str(p) for p in sorted(R.glob(E + '/**/*')) if p.is_file() and p.name != 'receipt.json' and '__pycache__' not in str(p)]
C = {c['id']: c for c in json.load(open('record/claims.json'))['claims']}
base = subprocess.check_output(['git', 'merge-base', 'HEAD', 'origin/main']).decode().strip()
A = json.load(open(f'{V}/logs/h5_arith.json')); D = json.load(open(f'{V}/logs/h5_density.json')); L = json.load(open(f'{V}/logs/thmL_sanity.json'))
NEW = ('BGS-TRACE-348', 'BGS-TRACE-349', 'BGS-TRACE-350', 'BGS-TRACE-351')
rec = {'schema': 'bgs-h5-ceiling-integration-receipt-v1', 'base': f'ChurilovMaksim/BGS origin/main {base[:8]}', 'branch': 'h5-ceiling-arith', 'prepared_on': '2026-11-05',
 'source': 'research pass research1105 (AUDIT_H5A.md section 1.3, BYPASS.md sections 1.1-1.4; code/audit_h5a s1-s7, logs/audit_h5a; not committed); every registered statement re-derived and re-checked at integration',
 'ids': {i: C[i]['state'] for i in NEW},
 'next_free_id_check': 'origin/main 3995d691 ends at BGS-TRACE-347; open PR branches #83, #84, #85 register no id above BGS-TRACE-336',
 'convention_check': 'h_n = (eps^n + epsbar^n)/2 = a_n, as BGS-TRACE-342 / Bgs.H6LemmaW (Lean a_eq_h6, all n) and = u_{(p-1)/2} of BGS-TRACE-344 (h5_arith.py, odd primes p <= 1500)',
 'unchanged_claims': {'BGS-TRACE-342': 'proved, not edited (strictly weaker than TRACE-348)', 'BGS-TRACE-303': 'open', 'BGS-TRACE-325': 'conditional', 'BGS-TRACE-206': 'open'},
 'review': 'no independent referee; the integrator re-derived every proof (REPORT_H5_CEILING.md) and the Lean module proves TRACE-348..350 in general',
 'reruns': {
   'python': f"{A['versions']['python']}, numpy {A['versions']['numpy']}, sympy {A['versions']['sympy']}, mpmath {A['versions']['mpmath']} (venv /workspace/venv_audit); OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1",
   'h5_arith': {'command': f'python {V}/code/h5_arith.py', 'log': f'{V}/logs/h5_arith.json', 'primes_q_lt_1e7': A['A_congruences']['primes_q_tested'], 'hits': A['A_congruences']['total_hits'],
                'violations': len(A['A_congruences']['violations_mod_2p']) + len(A['A_congruences']['violations_mod_8']), 'gcd_pairs': A['B_coprime']['pairs_checked'],
                'sophie_germain_count_5_1500': A['C_sophie_germain']['count_5_to_1500'], 'product_formula_max_rel_err': A['D_product_formula']['max_relative_error'], 'seconds': A['seconds']},
   'h5_density': {'command': f'python {V}/code/h5_density.py', 'log': f'{V}/logs/h5_density.json', 'all': D['all'], 'ranges': D['ranges'],
                  'agrees_with_research1105_s7_row_by_row': True, 'note': 'research note only, [CA + N] against a heuristic [H]; not registered'},
   'thmL_sanity': {'command': f'python {V}/code/thmL_sanity.py', 'log': f'{V}/logs/thmL_sanity.json', 'rows': len(L['rows']),
                   'M_ge_8_over_pi2_theta_every_row': L['observed_above_8_over_pi2_theta_every_row'], 'rows_below_bare_4theta_minus_1': L['rows_below_bare_4theta_minus_1'],
                   'note': 'research note only, [N]; Theorem L is not registered'}},
 'lean': {'files': [LEAN], 'theorems_printed': 9, 'sorry': False, 'native_decide': False, 'axioms': 'propext, Classical.choice, Quot.sound (a_eq_h6: propext only)',
   'build': f'{E}/lake_build_H5CeilingArith.log', 'scope': 'one build: lake build Bgs.H5CeilingArith (2841 jobs, all but the new module replayed), packages linked to /workspace/lineNgas/repo/formalization/.lake/packages; no new Mathlib cache; no full Bgs build',
   'not_formalized': 'BGS-TRACE-351 (product formula); the finite counts (25 p, 28,203 pairs) are Python checks only'},
 'metadata_snapshot': 'not refreshed: the new claims have no external dependencies and no older claim depends on them, so no external-reference impact set changes',
 'research_note': NOTE,
 'checks': f'{E}/checks/', 'sha256': {f: sh(f) for f in files}}
open(E + '/receipt.json', 'w').write(json.dumps(rec, indent=1, ensure_ascii=False) + '\n'); print(len(files))
