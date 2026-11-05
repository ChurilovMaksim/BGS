"""Static count/abstract updates in README.md / README.ru.md (hand-maintained pages, not generated), the abstract template
in computations/maintenance/render_results.py, and the CHANGELOG entry for BGS-TRACE-352..355. Run from the repository root."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
COMMON = [('registered_claims-434-', 'registered_claims-438-'), ('proved-350-success', 'proved-353-success'), ('Lean_4-194_modules', 'Lean_4-195_modules'),
          ('| **434** | **350 / 17 / 24 / 42 / 1** |', '| **438** | **353 / 17 / 25 / 42 / 1** |'), ('| 15 | 12 / 0 / 3 / 0 / 0 |', '| 19 | 15 / 0 / 4 / 0 / 0 |'),
          ('TRACE-337..351.', 'TRACE-337..355.'), ('| proved | 350 |', '| proved | 353 |'), ('| conditional | 24 |', '| conditional | 25 |'), ('| **434** | |', '| **438** | |'), ('2479 ', '2524 ')]
EN = COMMON + [('registered 434 precisely scoped claims; 350 are proved', 'registered 438 precisely scoped claims; 353 are proved'),
  ('179 non-open claims link Lean 4 files, out of 194 modules', '182 non-open claims link Lean 4 files, out of 195 modules'),
  ('holds 194 modules under', 'holds 195 modules under'),
  ('(VIII) Four integrations on 4–5 November:', '(VIII) Five integrations on 4–5 November:'),
  ('pairwise coprimality of the $h_p$, the $2p+1$ family and a product formula; H5 stays open). Every status',
   'pairwise coprimality of the $h_p$, the $2p+1$ family and a product formula; H5 stays open), and Lemma S on the cross lines of composite $h_p$ with the polymer gap lemma, '
   'the Binet lattice generator $\\eta_s$ ($N(\\eta_s)=h_p$) and a conditional cross-line constant for H5(b) (BGS-TRACE-352..355, referee-confirmed results of a research pass on bad divisor levels; '
   'Lemma S gives only $\\sqrt{\\min(d_+,d_-)}$ on its axis sub-line, $\\max(d_+,d_-)\\ge\\sqrt{h_p}$ is conditional on H6, H5 stays open and Theorem R♯-mod v5 stays conditional). Every status'),
  ('arithmetic of $h_p$ (sharpened Lemma W, coprimality, the $2p+1$ family, product formula) |',
   'arithmetic of $h_p$ (sharpened Lemma W, coprimality, the $2p+1$ family, product formula); Lemma S, polymer gap, Binet generator $\\eta_s$, conditional H5(b) constant |'),
  ('and so was `Bgs.H5CeilingArith` ([log](evidence/executions/20261105/h5_ceiling/lake_build_H5CeilingArith.log))',
   'and so were `Bgs.H5CeilingArith` ([log](evidence/executions/20261105/h5_ceiling/lake_build_H5CeilingArith.log)) and `Bgs.LemmaSArith` ([log](evidence/executions/20261105/lemma_s/lake_build_LemmaSArith.log))')]
RU = COMMON + [('зарегистрировала 434 точно ограниченных утверждения; 350 доказаны', 'зарегистрировала 438 точно ограниченных утверждений; 353 доказаны'),
  ('179 неоткрытых утверждений ссылаются на файлы Lean 4 из 194 модулей', '182 неоткрытых утверждения ссылаются на файлы Lean 4 из 195 модулей'),
  ('содержит 194 модуля', 'содержит 195 модулей'),
  ('(VIII) Четыре интеграции 4–5 ноября:', '(VIII) Пять интеграций 4–5 ноября:'),
  ('семейство $2p+1$ и формула произведения; H5 остаётся открытой). Все статусы',
   'семейство $2p+1$ и формула произведения; H5 остаётся открытой), а также лемма S на перекрёстных линиях составного $h_p$ с леммой о полимерном зазоре, '
   'образующая $\\eta_s$ решётки Бине ($N(\\eta_s)=h_p$) и условная константа перекрёстных линий для H5(b) (BGS-TRACE-352..355, подтверждённые рефери результаты исследования плохих уровней делителей; '
   'на осевой подлинии лемма S даёт лишь $\\sqrt{\\min(d_+,d_-)}$, оценка $\\max(d_+,d_-)\\ge\\sqrt{h_p}$ условна по H6, H5 остаётся открытой, теорема R♯-mod v5 остаётся условной). Все статусы'),
  ('формула произведения) |', 'формула произведения); лемма S, полимерный зазор, образующая Бине $\\eta_s$, условная константа H5(b) |'),
  ('как и `Bgs.H5CeilingArith` ([журнал](evidence/executions/20261105/h5_ceiling/lake_build_H5CeilingArith.log))',
   'как и `Bgs.H5CeilingArith` ([журнал](evidence/executions/20261105/h5_ceiling/lake_build_H5CeilingArith.log)) и `Bgs.LemmaSArith` ([журнал](evidence/executions/20261105/lemma_s/lake_build_LemmaSArith.log))')]
for f, R in (('README.md', EN), ('README.ru.md', RU)):
    t = open(f, encoding='utf-8').read()
    for o, n in R:
        assert t.count(o) == 1, (f, o, t.count(o)); t = t.replace(o, n)
    open(f, 'w', encoding='utf-8').write(t)
f = 'computations/maintenance/render_results.py'; t = open(f, encoding='utf-8').read()
o = ("'is not refuted**; and four integrations on 4–5 November 2026 (Phase VIII, BGS-TRACE-337..351: the span theorem, the '\n"
     "      'explicit H6 threshold with Lemma W, the H7* scope and the arithmetic of h_p). ")
n = ("'is not refuted**; and five integrations on 4–5 November 2026 (Phase VIII, BGS-TRACE-337..355: the span theorem, the '\n"
     "      'explicit H6 threshold with Lemma W, the H7* scope, the arithmetic of h_p, and Lemma S with the polymer gap lemma, the Binet '\n"
     "      'lattice generator and a conditional H5(b) cross-line constant). ")
assert t.count(o) == 1; t = t.replace(o, n); open(f, 'w', encoding='utf-8').write(t)
f = 'CHANGELOG.md'; t = open(f, encoding='utf-8').read(); h = '# Scientific changelog\n\n'; assert t.startswith(h)
entry = ("## 2026-11-05 — Lemma S, polymer gap, Binet generator (BGS-TRACE-352..354 proved, BGS-TRACE-355 conditional; no existing state changed)\n\n"
 "Integration of the results of the research pass research1105b (bad divisor levels of R′) that its independent internal referee confirmed, "
 "in the referee's corrected statements ([REPORT_LEMMA_S](computations/verification/lemma_s/REPORT_LEMMA_S.md), "
 "[receipt](evidence/executions/20261105/lemma_s/receipt.json), research note with the report and the referee audit "
 "[evidence/research/20261105_lemma_s/NOTE.md](evidence/research/20261105_lemma_s/NOTE.md)). "
 "BGS-TRACE-352 [P]: Lemma S — on a cross line, G(cεⁿ) + G(cε^{n+p}) ≥ √max(d₊, d₋) for every class c off the axis sub-line 𝔞̄_{−σ}; "
 "on that sub-line only G ≥ √min(d₊, d₋) holds; max(d₊, d₋) ≥ √h_p needs squarefree h_p and is conditional on H6 (TRACE-304); exhaustive check p = 11, 13, 17 and sampled exact omega=3 at p = 37. "
 "BGS-TRACE-353 [P]: polymer gap lemma, K > log_ε min(d₊, d₋) − 2 log_ε A − 1.214. "
 "BGS-TRACE-354 [P]: N(η_s) = +h_p and (η_s) is the Binet-line lattice in Z[ζ_p]; in Z[x]/(x^p − 1) (η_s) has index 2h_p (exact resultants p ≤ 73). "
 "BGS-TRACE-355 (conditional, constant [CA]): a uniform bound |X_line| ≤ Ce^{−cp} on every cross line with C ≤ 1, c ≥ 0.058 fits the idealised room at p = 1409 and 3307 "
 "(the source's c > 0.048 was wrong; rooms recomputed from V5/TRACE-333 on main, not taken from PR #85). "
 "New Lean module `Bgs.LemmaSArith` (Mathlib, no `sorry`, no `native_decide`; built alone): partial coverage of TRACE-352..354 "
 "(height/norm inequalities; the polymer norm bound and 1.213 < log_ε(ε²/2) < 1.214; Φ_n(±ε)Φ_n(±ε̄) = h_n and the products of η_s and ζ² − 6ζ + 1 over all primitive p-th roots of unity); "
 "TRACE-355 is not in Lean. The seam-decay threshold r < 0.418 and all [N]/[H]/[C] items of the source are not registered. "
 "H5 (TRACE-303) and H6 (TRACE-304) stay open, Theorem R♯-mod v5 (TRACE-325) stays conditional, nothing is claimed about R′ (TRACE-206).\n\n")
open(f, 'w', encoding='utf-8').write(h + entry + t[len(h):]); print('ok')
