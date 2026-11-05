"""Write evidence/executions/20261105/lemma_s/receipt.json (hashes of every new file of this integration). Run from the repository root."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, hashlib, pathlib, subprocess
R = pathlib.Path('.'); E = 'evidence/executions/20261105/lemma_s'; V = 'computations/verification/lemma_s'
NOTE = 'evidence/research/20261105_lemma_s'; LEAN = 'formalization/Bgs/LemmaSArith.lean'
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
files = [str(p) for p in sorted(R.glob(f'{V}/**/*')) if p.is_file() and '__pycache__' not in str(p)]
files += [LEAN] + [str(p) for p in sorted(R.glob(f'{NOTE}/**/*')) if p.is_file() and '__pycache__' not in str(p)]
files += [str(p) for p in sorted(R.glob(E + '/**/*')) if p.is_file() and p.name != 'receipt.json' and '__pycache__' not in str(p)]
C = {c['id']: c for c in json.load(open('record/claims.json'))['claims']}
base = subprocess.check_output(['git', 'merge-base', 'HEAD', 'origin/main']).decode().strip()
S = json.load(open(f'{V}/logs/lemmaS_exact.json')); P = json.load(open(f'{V}/logs/polymer_const.json'))
T = json.load(open(f'{V}/logs/eta_check.json')); H = json.load(open(f'{V}/logs/h5b_const.json'))
NEW = ('BGS-TRACE-352', 'BGS-TRACE-353', 'BGS-TRACE-354', 'BGS-TRACE-355')
cross = [r for r in S['rows'] if r['kind'] == 'cross']
rec = {'schema': 'bgs-lemma-s-integration-receipt-v1', 'base': f'ChurilovMaksim/BGS origin/main {base[:8]}', 'branch': 'lemma-s-binet', 'prepared_on': '2026-11-05',
 'source': 'research pass research1105b (REPORT.md section 4, code/, logs/) and its independent internal referee audit (REFEREE.md, referee/); copied unchanged to ' + NOTE + ' (binary logs/lvl, logs/prop, logs/val not copied)',
 'registered': 'only the referee-CONFIRMED items 1, 2, 4 and the corrected item 3, in the referee\'s corrected statements; nothing tagged [N]/[H]/[C] in the source, no r < 0.418 threshold, no estimate U',
 'ids': {i: C[i]['state'] for i in NEW},
 'next_free_id_check': 'origin/main 6f69baa1 ends at BGS-TRACE-351; open PR branches #83, #84, #85 register no id above BGS-TRACE-336',
 'unchanged_claims': {'BGS-TRACE-303': 'open (H5)', 'BGS-TRACE-304': 'open (H6)', 'BGS-TRACE-325': 'conditional (Theorem R#-mod v5)', 'BGS-TRACE-206': 'open (frozen R\')', 'BGS-TRACE-342': 'proved, not edited'},
 'dependency_note': 'TRACE-352 max(d_+, d_-) >= sqrt(h_p) is conditional on H6 (TRACE-304), stated in title and boundary but not a graph edge (the lemma itself does not use H6); TRACE-355 depends on TRACE-342 (w_max) and uses the V5/TRACE-333 idealised room recomputed on main; its target H5 (TRACE-303) is not a prerequisite',
 'reruns': {
   'python': '3.13.5, numpy 2.5.4, sympy 1.14.0, mpmath 1.3.0 (venv /workspace/venv7); OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1',
   'lemmaS_exact': {'command': f'python {V}/code/lemmaS_exact.py', 'log': f'{V}/logs/lemmaS_exact.json', 'primes': [11, 13, 17], 'cross_lines': len(cross), 'all_cross_ok': S['all_cross_ok'],
                    'Q_over_sqrtD': sorted({round(r['Q_over_sqrtD'], 5) for r in cross}), 'axis_min_G': sorted({round(r['axis_min_G'], 4) for r in cross}), 'seconds': S['seconds']},
   'polymer_const': {'command': f'python {V}/code/polymer_const.py', 'log': f'{V}/logs/polymer_const.json', 'constant': P['log_eps_eps2_over_2'], 'all_below': P['all_below'],
                     'max_ratio': max(r['max_ratio'] for r in P['rows'])},
   'eta_check': {'command': f'python {V}/code/eta_check.py', 'log': f'{V}/logs/eta_check.json', 'resultant_primes': len(T['A_resultants']), 'closed_form_bad': len(T['B_closed_form']['bad']),
                 'lines_ok_p_le_43': all(r['ok'] for r in T['C_lines']), 'word_index_2h_ok': all(r['ok'] for r in T['D_word_index'])},
   'lemmaS_exact_p37': {'command': f'python {V}/code/lemmaS_exact_p37.py', 'log': f'{V}/logs/lemmaS_exact_p37.json',
                       'note': 'omega=3 sample check; exhaustive infeasible; exact integer tests + 25% margin'},
   'h5b_const': {'command': f'python {V}/code/h5b_const.py', 'log': f'{V}/logs/h5b_const.json', 'rows': [{k: r[k] for k in ('p', 'wmax', 'c_room_wmax', 'c0058_C1_fits')} for r in H['rows']],
                 'room_input': 'recomputed from THEOREM_DRAFT_v5 / BGS-TRACE-333 on main (R=6.234e-4, delta 7.4115e-6 at 1409, 3.4962e-4 at 3307)'}},
 'lean': {'files': [LEAN], 'theorems_printed': 17, 'sorry': False, 'native_decide': False, 'decide_kernel': 'h103, h59 (2 h_103 + 1 < 2^131, 2^75 < 2 h_59)',
   'axioms': 'propext, Classical.choice, Quot.sound (mul_le_max_sq: propext only)', 'build': f'{E}/lake_build_LemmaSArith.log',
   'scope': 'one build: lake build Bgs.LemmaSArith (2748 jobs, only the new module compiled; imports Mathlib only), packages linked to /workspace/lineNgas/repo/formalization/.lake/packages; no new Mathlib cache; no full Bgs build',
   'coverage': {'BGS-TRACE-352': 'partial (height/norm inequalities)', 'BGS-TRACE-353': 'partial (norm bound, logarithmic form, constant)',
                'BGS-TRACE-354': 'partial (norm as product over all conjugates, every odd prime p; not Algebra.norm, not the lattice/index argument)', 'BGS-TRACE-355': 'none'}},
 'metadata_snapshot': 'not refreshed: the new claims have no external dependencies; TRACE-342 has none transitively; no older claim depends on them (bibliographic_metadata_audit --self-test passes)',
 'research_note': NOTE + '/NOTE.md', 'checks': f'{E}/checks/', 'sha256': {f: sh(f) for f in files}}
open(E + '/receipt.json', 'w').write(json.dumps(rec, indent=1, ensure_ascii=False) + '\n'); print(len(files))
