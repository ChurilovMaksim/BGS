"""Static count updates in README.md / README.ru.md (hand-maintained pages, not generated) and the CHANGELOG entry for BGS-TRACE-348..351."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
COMMON = [('registered_claims-430-', 'registered_claims-434-'), ('proved-346-success', 'proved-350-success'), ('Lean_4-193_modules', 'Lean_4-194_modules'),
          ('| **430** | **346 / 17 / 24 / 42 / 1** |', '| **434** | **350 / 17 / 24 / 42 / 1** |'), ('| 11 | 8 / 0 / 3 / 0 / 0 |', '| 15 | 12 / 0 / 3 / 0 / 0 |'),
          ('TRACE-337..347.', 'TRACE-337..351.'), ('| proved | 346 |', '| proved | 350 |'), ('| **430** | |', '| **434** | |'), ('2458 ', '2479 ')]
EN = COMMON + [('registered 430 precisely scoped claims; 346 are proved', 'registered 434 precisely scoped claims; 350 are proved'),
  ('176 non-open claims link Lean 4 files, out of 193 modules', '179 non-open claims link Lean 4 files, out of 194 modules'),
  ('holds 193 modules under', 'holds 194 modules under'),
  ('$K_p$ factorisations and the H7* scope at three included crossings |', '$K_p$ factorisations and the H7* scope at three included crossings; arithmetic of $h_p$ (sharpened Lemma W, coprimality, the $2p+1$ family, product formula) |'),
  ('was built alone ([log](evidence/executions/20261105/h7_scope/lake_build_H7KpArith.log); 2 jobs)',
   'was built alone ([log](evidence/executions/20261105/h7_scope/lake_build_H7KpArith.log); 2 jobs), and so was `Bgs.H5CeilingArith` ([log](evidence/executions/20261105/h5_ceiling/lake_build_H5CeilingArith.log))')]
RU = COMMON + [('зарегистрировала 430 точно ограниченных утверждений; 346 доказаны', 'зарегистрировала 434 точно ограниченных утверждения; 350 доказаны'),
  ('176 неоткрытых утверждений ссылаются на файлы Lean 4 из 193 модулей', '179 неоткрытых утверждений ссылаются на файлы Lean 4 из 194 модулей'),
  ('содержит 193 модуля', 'содержит 194 модуля'),
  ('область действия H7* на трёх включённых пересечениях |', 'область действия H7* на трёх включённых пересечениях; арифметика $h_p$ (усиленная лемма W, взаимная простота, семейство $2p+1$, формула произведения) |')]
for f, R in (('README.md', EN), ('README.ru.md', RU)):
    t = open(f, encoding='utf-8').read()
    for o, n in R:
        assert t.count(o) == 1, (f, o, t.count(o)); t = t.replace(o, n)
    open(f, 'w', encoding='utf-8').write(t)
f = 'CHANGELOG.md'; t = open(f, encoding='utf-8').read(); h = '# Scientific changelog\n\n'; assert t.startswith(h)
entry = ("## 2026-11-05 — H5 structural-ceiling arithmetic (BGS-TRACE-348..351 proved; no existing state changed)\n\n"
 "Elementary arithmetic of h_p = (ε^p + ε̄^p)/2 from the research pass research1105, re-derived and re-checked at integration "
 "([REPORT_H5_CEILING](computations/verification/h5_ceiling/REPORT_H5_CEILING.md), [receipt](evidence/executions/20261105/h5_ceiling/receipt.json)). "
 "BGS-TRACE-348 [P]: every prime q | h_p (p an odd prime) has q ≡ 1 (mod 2p) and q ≡ ±1 (mod 8), sharpening Lemma W (TRACE-342, not edited). "
 "BGS-TRACE-349 [P]: gcd(h_p, h_p′) = 1 for distinct odd primes. BGS-TRACE-350 [P]: p ≡ 3 (mod 4) and 2p + 1 prime imply 2p + 1 | h_p, "
 "with least prime factor exactly 2p + 1 (25 such p in [5, 1500]). BGS-TRACE-351 [P]: h_n = ∏_{k=1}^{(n−1)/2}(6 − 2cos(2πk/n)) for odd n "
 "(80-digit check, not in Lean). New Lean module `Bgs.H5CeilingArith` (general proofs of TRACE-348..350, Mathlib, no `sorry`, no `native_decide`; built alone). "
 "No independent referee. Research note [evidence/research/20261105_h5_ceiling/NOTE.md](evidence/research/20261105_h5_ceiling/NOTE.md) (not registered): "
 "the ceiling of H5(a) stands; the Mersenne-type density heuristic [H] is matched in aggregate (38.0% vs 36.9%, p ≤ 1500) [CA + N]. "
 "H5 (TRACE-303) stays open, Theorem R♯-mod v5 (TRACE-325) stays conditional, nothing is claimed about R′ (TRACE-206).\n\n")
open(f, 'w', encoding='utf-8').write(h + entry + t[len(h):]); print('ok')
