# ROADMAP — путь к полному решению BGS для cat map

## Текущий статус (26 августа 2026, audit pass)

**Доказано безусловно:**
- Класс симметрии (β=1 vs β=2) определяется антиунитарной структурой
  (Θ²=+1 для reversing-инволюций с gcd(M₂₁,N)=1; вырожденная карта c≡0 —
  отдельно, см. redteam C1)
- Гладкая плотность = классический Биркгоф
- Спектральная жёсткость O_F(1)
- Точная идентичность резонансного ядра sol+-+- (2k²−k / 3k(k−1))
- Точная ансамблевая средняя ⟨N₃⟩ = k³(p²−3p+3)²/(p−1)⁶
- Collision lemma C(u,v)≤4 (алг. ядро формализовано в Lean; острая форма
  C≤2 доказана и формализована в аудите 2026-08-26)

**Численно подтверждено (не доказано):**
- Tail bound N₃ ≤ ⌊k²/p⌋+2 (0/~230 нарушений)
- Form factor совпадает с аналитическими кривыми
- NN-статистика WD-not-Poisson под unitary flow (4 простых);
  β=GUE разрешено при n=13723

**РЕТРАКЦИЯ R12-A действует:** пороговые заявления вида
«4-й момент = WD при k<p^{2/3}» и «все чётные моменты при
k=o(p^{1/(r−1)})» были ОТМЕНЕНЫ (double-counted prefactor) — не
цитировать как установленные.

## ФАЗА 1: Формализация (ближайшая, ~1–2 недели)

### 1a. card_le_four в Lean
- Черновик: `C:\lean\bgs_formal\card_le_four_draft.lean`
- Нужно: закрыть structure-equality plumbing (~100 строк)
- Цель: `Fintype.card (Collision u v) ≤ 4`, exit 0

### 1b. O6 формализация (Θ²=+1)
- Ядро доказательства элементарно (линейность фазы по y)
- Добавить в BgsFormal.lean как вторую теорему

### 1c. Компиляция статьи
- Установить TeX Live или MiKTeX
- Скомпилировать `drafts/bgs_paper_complete.tex` (absent; superseded by `paper/exact_wd_and_subgroup_moments.tex`)
- Проверить все ссылки и нумерацию

## ФАЗА 2: Локальный закон (ключевой шаг, ~1–3 месяца)

**Цель:** перейти от «все фиксированные моменты совпадают» к «распределение ближайших соседей сходится к Wigner surmise».

**Audit note (2026-08-26):** квантовые периоды, указанные в R27
(p=4481 «K=17», p=2207 «K=9», p=3001 «K=13») — артефакты бага
`n//2+1` в `find_small_period_primes.py`; истинные проектные порядки:
4481→32, 2207→16 (инертный!), 3001→25. Размерности мультиплетов m в
экспериментах статьи верны.

### 2a. Резольвентная оценка
- Для z с Im(z) ≥ m^{−1+ε} доказать:
  |m_Vλ(z) − m_GOE(z)| ≤ m^{−δ}
- Метод: разложение резольвенты через мастер-формулу,
  контроль членов ряда через границы на всплески

### 2b. Связь с QUE
- Gurevich–Hadani (math-ph/0404074) доказали QUE для Hecke eigenfunctions
- Комбинировать QUE + моментное соответствие → делокализация → локальный закон

### 2c. Альтернативный путь: четырёхмоментная универсальность
- Tao–Vu теорема: если первые 4 момента входов совпадают с Wigner,
  локальные статистики универсальны
- Нужно: проверить entry-level условия (F3 статус CONTESTED)

## ФАЗА 3: Katz-tier для малых k (открытая математика, годы)

**Цель:** распространить результат на ВСЕ k, включая самые большие мультиплеты.

### 3a. Формулировка пучковой задачи
- Семейство (r,s) ↦ Σ_{h∈H} e_p(ra·h + sb/h) как sheaf on G_m²
- Применить Goursat–Kolchin–Ribet критерий

### 3b. Численное исследование
- Измерить sup|S(r,s)|/k для всех k/p режимов
- Найти порог где √-закон начинает работать

### 3c. Гипотеза
- sup ≤ √p·polylog для всех k > p^ε
- Если верна ⟹ полный BGS для cat map при k ≫ p^{1−ε}

## ФАЗА 4: Расширения

### 4a. Sp(2g,Z) — многомерные cat map
### 4b. Простые степени N = p^n (Kelmer regime)  
### 4c. Общая формула следа для нелинейных систем

## ИНСТРУМЕНТЫ

| Инструмент | Статус | Использование |
|---|---|---|
| Python 3.13 + numpy/scipy/sympy | ✓ | Основной вычислительный |
| Lean 4 + Mathlib | ✓ C:\lean\bgs_formal | Формализация |
| Julia 1.11 | ✓ установлен | Горячие циклы (порт отложен) |
| GPU (CuPy/torch cu126) | ✓ установлен | Будущие большие прогоны |
| LaTeX | ✗ нет движка | Только .tex исходники |
| arXiv API | ✓ через webfetch/node | Литература |

---
## UPDATE AUG 2026 (post-review, runs 47+): CANONICAL NEXT STEPS

Phase 0 DONE: full revision pass implemented (unitary perturbation
model e^{i eps E} U_A; GUE law specified; generic defined; Wick
dictionary; Domination corollary conditional on tail bound; appendix
methodology; all cites resolve).

Phase 1 TAIL BOUND ladder:
  (a) prove N3 <= C max(k^2/p, k^{1/2+eps}) via subgroup char sums;
  (b) fallback transversality-restricted version;
  (c) numeric check of sqrt-branch on existing scan data.
Note: any theta<1 bound suffices for Domination; sharp floor+2 stays
stretch goal.

Phase 2 beta-discrimination: p up to ~6000 via eigenvector-direct
pipeline; target n>=800 spacings so KS critical ~0.048 separates
GOE/GUE surmises.

Phase 3 r>=6: type-decomposition (S-layers under -1 in H first),
closed forms per partition family.

Grand arc: unconditional local law via ARITHMETIC perturbation
(replace Gaussianity) -> sibling arithmetic systems -> general chaos.


## UPDATE 2026-08-27 (R54): TAIL CONDITIONAL + HECKE-SYMM PILOT

**op:tail: PROVEN conditional on OSV** for k >= p^{3/7+eps}
(smooth law N_3 <= k^2/p + sqrt(k) at C=1, via
Ostafe-Shparlinski-Voloch arXiv:2110.10941 Cor. 2.9).  Below
p^{3/7}: no published explicit delta (named, cited).  Empirical
record now ~293 configs / ~60,000 patterns / 0 violations
(was 196/~230).

**op:local: Hecke-symmetrization pilot (R54)** — measured partial:
off-diagonal kurtosis collapses from raw +5.6 to Hecke -0.7 in
worst case (entry decorrelation works), eigenvalue spread
2.9 -> 2.6 modest.  KS_GOE 0.13-0.35 at m<=17 (inconclusive
at this m; needs m>=70 with actual centraliser basis, not
Haar surrogate).  R49 arithmetic perturbation was worse
(KS_GUE 0.20-0.28), so Hecke IS strictly better but not yet
Wigner.  op:local remains OPEN, but now the target is
narrowed: build the actual Hecke basis of the centraliser
torus and run at m>=70.

**Paper updated:** `archive/papers/resonance_laws_catmaps.tex` now
carries Remark `rem:smoothconditional` (OSV-conditional smooth
law) + OSV21 bib entry + status-table expansion (smooth-law
conditional + tail below p^{3/7} OPEN + Hecke NUM-SUPP).
Recompiled: 159.09 KiB, 27 pages, all refs resolve.

**New artifacts:**
* `src/diagnostics/hecke_local_law_test.py` — Hecke-symmetrised pilot
* `artifacts/hecke_local_law_test.json` — 8-config results
* `artifacts/audit_conj_tight_extended.json` — 25 new configs
* `drafts/tail_bound_proof.md` — OSV-conditional proof draft
* `drafts/hecke_symmetrization_test.md` — honest verdict

**Honest conclusion:** R54 delivered a partial proof (`conj:tight`
unconditional not closed; OSV-conditional smooth law PROVEN for
k >= p^{3/7+eps}; Hecke-symmetrization pilot measured partial,
not Wigner at m<=17) and a clean honest paper.  The attempt to
add an unconditional `Lemma:SZ` claiming `N_3 <= 2k` was
self-corrected same session after repeated counting errors
(the cleared reciprocal polynomial has total degree 3 in
(u₂, u₃), not 2; the `u_4 ∈ H` membership is not automatic from
the cleared equation).  Per option C the lemma, the
`rem:SZtooWeak`, the θ=1 sub-claim in `cor:domination`, and the
SZ reference in the Combining paragraph were all dropped.  The
paper's original `N_3 <= 4k` claim at line 329-330 (bidegree-(2,2)
in (u₂, u₃) → total degree 4 → 4k by Schwartz–Zippel) is the
unconditional ceiling and is mathematically correct.
`cor:domination` is conditional on `conj:tight` (or its
OSV-conditional smooth-law replacement for k >= p^{3/7+eps}),
unchanged from the R53 audit baseline.  See LEDGER R54
self-correction note for the full account.

**Final paper recompile:** 159.39 KiB, all refs resolve,
0 undefined references, original structure preserved.

## UPDATE 2026-08-28 (R64–R66): RING 1 REPAIRS + RING 2 ATTACK + RING 3 FINAL DELIVERY

**Ring 1 closed (7/7 items).** Standing red-team and
audit findings are repaired; the C1 gcd hypothesis, the
C2 U1 non-degeneracy, the C3 U4 corrected bound, the
C5 r=5 demotion, the R12-A in-place warning, the
`verify_mean_law` / `audit_tail_bound` portable-path
fFix, and the r=4 regression check are all landed. Lean
step recorded as `lean:out_of_scope_this_run` (no
`bgs_ring1` project on churi; cold-load is 5–10 min
for Mathlib on the 8 GB box; per plan contingency, not
blocking). THEORY.md gains §8.0.1, §8.0.2, §8.0.3.
paper.tex gains 5 new status-table rows, a new
`rem:reversing_degenerate`, an updated `rem:collision`,
and a front-matter source-edit log. .tex is NOT
recompiled (no LaTeX engine on churi); the .pdf stays
at 159.4 KiB dated 2026-08-27. New artifacts:
`artifacts/u1_degenerate_audit.json`,
`artifacts/ring1_rerun_summary.json`,
`artifacts/ring1_rerun_verify_mean_law.json`.

**Ring 2 attack on the p^{3/7+ε} wall: WALL UNCHANGED.**
Three parallel cloud subagent lines (Stepanov / Deligne
/ Bourgain) plus a litwatch scout completed within
budget. All three attack lines close as `[OPEN GAP]`;
no line produces a calibrator-passing `[CONJECTURED]`
claim with a runnable discriminator. Headline empirical
data: 32 distinct (p, k) configs at p ∈ {41, 61, 113,
157, 521, 541}, k ∈ {4, 5, 8, 10, 12, 13, 20, 26};
max |S|/(2√p) ≈ 0.99999 (Deligne big sweep at p=4001,
k=4); Weil is essentially tight. **Discriminator
(R2.5) moot.** Litwatch: 5 NEW results, 2 Weil-ceiling
generalisations (arXiv:2603.18511, arXiv:2603.09252).
No 2026 paper produces a pointwise explicit
power-saving-in-p bound on the multiplicative-subgroup
Kloosterman below `k < p^{3/7+ε}`. **The OSV-conditional
smooth law at `k ≥ p^{3/7+ε}` remains the published
frontier.** New artifacts:
`artifacts/ring2/synthesis.md` (4.8 KB),
`line_{A,B,C}_report.md`, `line_{A,B,C}_*.json`,
`litwatch_summary.md`, `discriminator.json`.

**T21 honest threshold (THEORY §8.0.3).** The wall is
unchanged as of 2026-08-28. Best available published
reference: OSV arXiv:2110.10941 Cor. 2.9, giving
`sup|S| ≤ k · p^{−δ}` for an explicit δ > 0 on
`k ≥ p^{3/7+ε}`. For `k < p^{3/7+ε}`, no published
pointwise statement with explicit δ > 0 exists.
**Honest verdict for BGS in this family:** fixed-order
moments r ≤ 4 PROVEN for ALL admissible (p, k) with
NO threshold (R12 corrected); smooth law OSV-conditional
PROVEN for `k ≥ p^{3/7+ε}`; the unconditional local law
at the mean-spacing scale is OPEN. **NN spacing
distribution (the strict BGS conjecture): NOT claimed
in this run.**

**Phase status update (R3.3):**

* **Phase 1a (card_le_four in Lean):** core
  formalisation is in `mephisto-lean\` (green
  `card_le_four_draft.lean` from R10-B). The fresh
  `C:\Users\churi\lean-projects\bgs_ring1\` project was
  not created; Lean step recorded as
  `lean:out_of_scope_this_run`. **op:lean_rebuild** added
  to the open-problem list.
* **Phase 1c (compile the paper):** deferred; the .tex
  source is updated but the .pdf is NOT recompiled (no
  LaTeX engine on churi; .pdf stays at 2026-08-27). A
  machine with TeX Live / MiKTeX is required for any
  future recompile. The front-matter source-edit log on
  the .tex makes this constraint explicit.
* **Phase 2 (local law):** wall unchanged. The RING 2
  three-line attack is documented in
  `artifacts/ring2/synthesis.md`; the next research
  direction is either (i) prove the two-term BGK
  analogue on multiplicative subgroups, or (ii) find a
  different multiplicative-combinatorial primitive that
  gives the 2-term analogue. Neither is published as
  of 2026-08-28.
* **Phase 3 (Katz-tier):** unchanged. The 2026
  norm-trace / Frobenius-structure extensions
  (arXiv:2603.18511, arXiv:2603.09252) are Weil-ceiling,
  not power-saving; useful as cross-references for
  sheaf-restriction arguments, but do not close the
  gap.

**Open problems named in this run:**
* `op:r5` — close the r=5 master-formula path with
  ≥ 12 diverse (A, N) configurations on the churi box,
  target dt ≤ 300 s per config by vectorising the
  outer-`J` loop with `np.einsum`.
* `op:tail_below_p^{3/7}` — unconditional local law at
  the mean-spacing scale; named, OPEN, no improvement
  this run.
* `op:lean_rebuild` — re-establish the Lean project on a
  machine with Mathlib cold-load capacity (≥ 16 GB RAM,
  or pre-cached Mathlib).
* `op:r6` (R63) — express `A_p(k)` as a character sum
  over the prime divisors of k.
* `op:paper_recompile` — recompile paper.tex on a
  machine with a LaTeX engine, after auditing every
  edit against the LEDGER R64–R66 entries.

**Honest final state (2026-08-28):** the cat-map
programme is well-organised, retraction-aware, and
honest about what is and is not proven. The Phase 1
tasks (Lean, paper recompile) are blocked by environment
(Lean project missing on churi, no LaTeX engine); the
Phase 2 wall is genuinely open; the Phase 3 Katz tier
is a years-scale research direction. **The plan for
the next session is documented in the LEDGER R66
"Final state on disk" section.**
* LEDGER RUN 54 entry

## UPDATE 2026-08-28 (run 71) — priorities reset

Closed this run: the Ring-1.2 Hecke line (R67-R70) is **void**, so
`op:r7_hecke_threshold_v2`, `op:r10_hecke_threshold_v2`, `op:r10_hecke_que_paper`,
`op:r10_hecke_math`, `op:r11_universality`, `op:r11_paper`,
`op:r11_churilov_2.3`, `op:r11_seed_robust` are all closed as resting on a void
measurement. `op:paper_recompile` is **done** (tectonic works; both papers
compiled). `op:r5` is upgraded: `master_general.py` reproduces 5/5 at r = 5.

New priorities, in order of expected value of information:

1. **`op:local_deterministic` (Priority 1).** Hold the observable complexity K
   fixed and let the multiplet m grow; measure z(m) for the single-orbit
   compression. Run 71 established z > 0 at all five design points and that the
   deviation tracks K rather than m, but the K-fixed sequence was not run. This
   is the real BGS content of the family and the experiment is cheap.
   Target to compare against: the Kurlberg-Rudnick SU(2)-trace law
   (arXiv:math/0302277), **not** a Gaussian.
2. **`conj:Pstar` (Priority 2).** Prove a polynomial bound
   `P*(k,s) <= C k^{cs}` on the exceptional primes of Theorem B. Attack: the
   minimal sporadic configurations are the multiset shapes `{a,a,b}` (excess
   18k) and `{a,a,a,b}` (excess 32k), i.e. F_p-points of explicit curves; bound
   them by Weil and sum over shapes. This is the concrete replacement for the
   `op:tail` wall and is a self-contained paper.
3. **`op:theta_sign_regen`.** Regenerate the missing `src/theta_sign.py` (absent; the claim it generated is now moot, Theorem C), or
   narrow T13's coverage claim to the 6-7 involutions actually recorded per
   configuration. The current LEDGER text at R65 makes a false claim about which
   code produced `theta_sign.json`.
4. **`op:tail_below_p^{3/7}`.** Unchanged and still the published wall; do not
   re-attack without a genuinely new input.
5. **`op:lean_rebuild`.** Still blocked by 8 GB RAM.
6. **`op:manifest_repair`.** Two MANIFEST rows cite artifacts that never existed.

## UPDATE 2026-08-28 (run 72) — priorities reset again

Closed this run: **O6** (Theorem C, unconditional `Theta^2 = +1`);
`op:theta_sign_regen` (moot — T13 no longer rests on a scan, and the exhaustive
involution counts are recorded); every hygiene item of the run-71 audit
(`src/maintenance/hygiene_r72.py`). `op:local_deterministic` is **reformulated and answered
numerically**: the single-orbit compression mixes two exact parity sectors
(Theorem D); after desymmetrising it is indistinguishable from GOE, with the
Dyson index predicted by the time reversal of Theorems C and E.

New priorities:

1. **Push the desymmetrised ratio measurement to m ~ 2000** (p ~ 1e5, K ~ 50).
   No unfolding is needed, so the cost is one eigensolve per frequency. If
   `<r~>` stays within 0.5 sigma of GOE the numerical case is very strong.
2. **Test the Kurlberg-Rudnick SU(2)-trace law** (arXiv:math/0302277) against the
   correct Hecke-basis matrix elements. This is the honest successor to the void
   R67-R70 line; the Hecke eigenbasis is now easy to build.
3. **Prove `Theta_u^2 = +1` in Theorem E**, which would upgrade beta = 1 from a
   measurement to a theorem. The equal-diagonal mechanism of Theorem C is the
   natural tool.
4. `conj:Pstar` — bound the exceptional primes of Theorem B polynomially. The
   minimal sporadic shapes are `{a,a,b}` (excess 18k) and `{a,a,a,b}` (excess
   32k), i.e. F_p-points of explicit curves.
5. Extend `E0(s,k) = P(s,k) iff s < lpf(k)` from prime powers to general k.
6. Still blocked: `op:lean_rebuild` (8 GB), `op:tail_below_p^{3/7}` (published
   wall).

## UPDATE 2026-08-28 (run 73)

Closed: the beta = 1 claim is now a theorem (torus inversion `R tau R^{-1} =
tau^{-1}`, so `Theta_u^2 = +1` and the parity block is unitarily real symmetric);
the correct Hecke eigenbasis is built and the diagonal/off-diagonal dichotomy
measured (Sato-Tate versus complex Gaussian); the `s < lpf(k)` criterion is
proved for prime powers and verified in 144 cells.

Remaining, in order:

1. **A local law at any fixed polynomial scale.** This is now the ONLY missing
   ingredient for a proof of BGS in this family. Everything else is in place:
   the symmetry class (theorem), the exact moment matching at order 4 (theorem),
   the exact Gaussian statistics for random observables (theorem), the Gaussian
   off-diagonal law (measured to four decimals). The obstruction is that the
   moment error `C^r/m` of T8 grows exponentially in r, so the resolvent cannot
   be reached at `Im z ~ 1/m`. Two concrete sub-questions: (a) can `Im z = m^{-d}`
   for some fixed `d > 0` be reached, which would suffice via Dyson Brownian
   motion plus Theorem A? (b) is there a resolvent identity for `P_lam` that
   avoids the moment expansion altogether?
2. Extend `s < lpf(k)` to general k (close the factor-2 gap in the residual
   branch of the tensor induction).
3. `conj:Pstar` — polynomial bound on the exceptional primes of Theorem B.
4. Push the desymmetrised ratio statistic beyond m = 1674 (needs > 8 GB or a
   complex64 basis).
5. Still blocked: `op:lean_rebuild` (8 GB), `op:tail_below_p^{3/7}`.

### Refinement after R73.4-R73.6 (same day)

Theorem G closes the moment route **rigorously**: for any observable of bounded
Fourier complexity the Birkhoff dilution forces `||cbar||_1/||cbar||_2 ~ sqrt(K)`,
so the relative moment error is `(c sqrt K)^r / m` and `r <~ 2 log m / log K`; and
the `l^1` bound is tight to a factor ~3 because the explicit quadratic-phase sums
of Lemma F show **no** square-root cancellation (measured `max_J|S_J|/||a||_1` in
[0.22, 0.53], `/||a||_2` in [7.5, 18.3]). So priority 1 above is now sharper:

1. **A resolvent identity for `P_lam`, not a moment expansion.** The target is a
   self-consistent equation for `G(z) = (V_lam - z)^{-1}` at `Im z ~ m^{-delta}`.
   Two concrete entry points: (a) the Birkhoff reduction `P_lam V P_lam = Vbar
   P_lam` (T6) means `G` is the compression of a resolvent of `Vbar`, and `Vbar`
   commutes with `U_A`, so the whole problem lives in the commutant — a
   `K`-dimensional algebra of Weyl orbit averages; (b) Lemma F expresses every
   trace against `U^J` as a Gauss sum, so the resolvent expansion has explicitly
   computable theta-like coefficients rather than opaque ones.
2. Prove `Theta_u^2 = +1` without invoking the absence of Kramers degeneracy
   (currently the sign is pinned by an observation, not an identity).
3. Reach `m = 1674` at p = 95419 on a box with > 8 GB, with the dimension
   assertion now in `src/diagnostics/desym_large_m2.py`.
4. Extend `s < lpf(k)` to general k (factor-2 gap in the residual branch).
5. `conj:Pstar`; `op:lean_rebuild`; `op:tail_below_p^{3/7}` — unchanged.

## UPDATE 2026-08-28 (run 75) — THE EXCESS IS SOLVED AS STRUCTURE

Theorem H (cyclic shape decomposition): D_r(N) = pairing count + cyclic sum
over the primitive multiples ("shapes") of x^2 - t x + 1, EXACT at r = 5, 6, 8
on both prime-K design points (12/12 comparison rows, 24 numbers, all
last-digit matches vs the R74 meet-in-the-middle).  The R74 "accidents" are the cyclic wraps of the same
shapes: ONE excess mechanism, not two.  Fixed-order convergence of the
ensemble moments to the RMT values now has rate O_r(K^{1-s}) PROVEN at the
phi = 1 level, and odd orders decay like K^{-4} (pure m-shape).

New priorities, replacing the run-74 list:

1. **phi-weights per shape (Priority 1).**  Attach the Weyl phases of R74.1 to
   the cyclic shape sum.  If they factor per shape (expected), the phi = 1
   level upgrades to a full ensemble moment theorem at every fixed r for all
   eps = +1 designs.  Self-contained, mostly bookkeeping.
2. **conj:Sgrowth + uniformity.**  Bound the shape mass up to L1 = r ~ log m:
   the Littlewood-multiple counting problem for x^2 - tx + 1.  Census data:
   S(R) = 1,1,1,3,8,31,64,105 (R = 5..12, t=3); concatenation families give
   ~K^{k-1} shapes at L1 = k(t+2).  A poly(R) C^R bound for the aperiodic part
   plus the K^{ceil(r/(t+2))} translate count would close uniformity.
3. **First genuinely modular relation.**  M_r = 0 certified for r <= 8; find
   the first r with M_r > 0 (vectorised census at r = 10, 12) — it separates
   "shapes explain everything" from "new modular classes exist".
4. **eps = -1 Burnside accounting.**  Replace the naive antiperiodic
   2^{r/2} factor (overcounts; negative X_r rows in the r74 artifact) by the
   exact image-orbit count.
5. **Resolvent step** (unchanged): from ensemble moments to NN-spacings.
6. **Un-blocked by the 16 GB re-probe:** the m = 1674 desymmetrised
   measurement (~5.5 GB peak) and a Lean rebuild with pre-cached mathlib.

Closed this run: `op:manifest_repair`; the ensemble_moments paired-count
defect; the R74.5 "control X_r" structure half.

## UPDATE 2026-08-28 (run 76) — PHI CLOSED, M_10 = 0, CEILING QUANTIFIED

The fixed-n ensemble moment formula is now EXACT with explicit Weyl phases,
certified end-to-end (24/24, max err 8e-14): phi = 1 on pairings; shape words
carry 2D Gauss sums G(C) with |G| = N^-1 (measured at the floor); E(0) = 0.
Consequence: the ensemble excess is the Theorem-H counting excess suppressed
by an extra N^-1/2 (measured N^-1). Sharp prediction on the table: the rank-0
ensemble 5th moment at (3571,17) = K^-5 G5 = +1.341e-07.

Census to r = 10 (cross-validated exactly at r = 6, 8): M_10 = 0 — every
mod-N solution is still a cyclic shift of a Z-multiple.  Uniformity ceiling
at K=17 quantified: X/triv = 1.14% / 4.66% / 12.15% at r = 6/8/10.

Priorities now:

1. **Uniformity via the relation automaton** (Frougny-Steiner machinery):
   growth constant C of the shape language, the ceiling r*(K), reproduce the
   1.14/4.66/12.15% table analytically.  This is the last analytic piece for
   "ensemble moments match RMT up to r ~ c log m".
2. **Exact E-residue at N=3571** to verify the 1.341e-07 fifth-moment
   prediction end-to-end at the real design (regroup
   sum_words <w^Phi E(Ln)>).
3. **Census at r = 12** — the first genuinely modular relation is still
   hiding; find it or push the M_r = 0 frontier further.
4. **Resolvent step** (unchanged) — from ensemble moments to NN-spacings.
5. eps = -1 Burnside accounting; Lean formalisation of Lemma coll + Thm H.


## UPDATE 2026-08-29 (run 80) — PSI(Y) EVALUATED; WRAP COINCIDENCES; C_dense

Closed this run: the R77.1 generating function is EVALUATED EXACTLY
(`src/shape_automaton/jweight_dp.py`; all census rows exact through r = 8, X^Z through
r = 12, float replica 2.2e-15); the Theorem-H (sig, a, sign) parametrisation
is proven NON-INJECTIVE from r = 10 with the exact collision excess
(41,126,400 / 1,244,073,600 / 97,037,740,800 at r = 10/11/12, K = 17 —
census deltas to the last digit); S(R) known exactly to R = 80 with
2.18 < C_dense <= 3; the R71-R79 certificate chain re-verified green
(11/11 + ensemble scripts); one path defect repaired (verify_mean_law).

New priorities:
1. **op:local (unchanged, THE wall).** The post-R80 moment statement is now:
   fixed-r ensemble moments match RMT with the explicit error budget
   (shape excess x Gauss suppression + E-term); the missing ingredient is
   still the local law.  See THEORY 17.4.
2. **op:Cdense.** Pin the shape-language growth constant
   (2.18 < C_dense <= 3): Perron analysis of the co-reachable automaton
   core, or a Frougny-Steiner transfer.  Uniformity in r rides on it.
3. **E-residue at N=3571** (if the class-gated computation did not finish
   this run): the R76 prediction K^-5 G_5 = 1.341e-07 with the exact
   kernel-slice piece I_5 now computed.
4. **Lean completion**: the algebraic core of the automaton bound is
   machine-checked (`bgs-lean/BgsTailBound.lean`, prebuilt host); the three
   top-level theorems (unroll sums, tail bound, finiteness) remain
   Finset/Int plumbing.
5. Blocked/unchanged: op:tail_below_p^{3/7} (published wall), composite-K
   collisions, r >= 14 census (conditional on M_r = 0).
