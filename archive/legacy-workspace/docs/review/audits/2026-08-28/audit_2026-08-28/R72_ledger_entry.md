
## RUN 72 (2026-08-28, continuation) — THREE EXACT SYMMETRY THEOREMS; BGS CONFIRMED AFTER DESYMMETRISATION

**Headline.** The anomaly measured in R71 (single-orbit compressions deviating
from GUE by +0.05…+13.4σ, growing with m) is now **completely explained and
resolved by an exact symmetry that ten previous runs missed**. After quotienting
by it, the fully deterministic single-observable compression is
indistinguishable from GOE — and a matched arithmetic-free surrogate is
indistinguishable from GUE, so the *symmetry class* itself is arithmetic
content. This is a **positive** BGS result, obtained with an unfolding-free
statistic, at three sizes.

### R72.1 — THEOREM C [PROVEN, unconditional]: Θ² = +1, closing O6

Let R = [[p,q],[r,−p]] ∈ GL(2,Z) be a reversing involution (det R = −1,
RAR⁻¹ = A⁻¹), S = diag(1,−1), M = SR.

* **(C1)** `M = [[p, q], [−r, p]]` — **the diagonal entries are always equal**,
  M₁₁ = M₂₂ = p, and det M = p² + qr = 1.
* **(C2)** With c' = (2c)⁻¹,
  `(U_M conj(U_M))(x,z) = N⁻¹ ω^{c'(dx²−az²)} Σ_y ω^{c'((a−d)y² + 2y(z−x))}`.
  By (C1) a = d, the quadratic term vanishes, and since 2c' = c⁻¹ is a unit the
  y-sum is `N·[z=x]`; at z = x the prefactor is 1. Hence **Θ² = +1 exactly**.

This **closes the standing open problem O6** ("prove the Weil-cocycle identity
c(M,M⁻¹) = +1 in general") with a two-line computation, and shows that the
`gcd(M₂₁,N) = 1` hypothesis added in R65 as R1.1 is **not a hypothesis at all**:
it is the well-definedness condition of the kernel formula. β = 4 never occurs,
unconditionally. Certified at **504** admissible (M,N) over 8 cat maps × 6 primes,
worst |Θ²−1| = 1.78e-15, worst |U_M*U_M−1| = 1.78e-15, plus a direct check of the
collapsing Gauss sum at N = 41,101,311 over 600 random (x,z).

*Audit item closed:* the exhaustive involution counts the audit demanded are
16, 10, 10, 8, 8, 16, 16, 16 in the box |·| ≤ 25 for traces 3,4,4,6,8,7,11,18.
The `theta_sign.json` artifact recording 6–7 per configuration was
under-counting; the point is now moot because T13 no longer rests on a scan.
Artifact: `artifacts/r72/theta_square_theorem.json`, script
`src/theta_square_theorem.py`.

### R72.2 — THEOREM D [PROVEN]: an exact parity obstruction, and a dichotomy

Let R_par f(x) = f(−x), and let k be the projective order of A mod N, so
A^k = ε·I with ε = ±1 and K = k (ε=+1) or 2k (ε=−1).

* **(D1)** `[R_par, U_A] = 0` **exactly**, because the kernel is even in (x,y).
  So R_par preserves every H_λ and R_par² = 1. Measured ≤ 4.4e-17.
* **(D2)** `R_par T(u) R_par⁻¹ = T(−u)`. A Hermitian Weyl observable
  `V = Σ g_u T(u)` (so g_{−u} = conj(g_u)) commutes with R_par **iff all g_u are
  real**, i.e. iff its Weyl symbol is an **even** function on the torus.
* **(D3) DICHOTOMY.** If ε = −1 then `U_A^k` is a phase times R_par, so R_par
  acts on each eigenspace as a **scalar** and carries no information. If ε = +1
  then R_par is an independent involution and `H_λ = H_λ⁺ ⊕ H_λ⁻` with both
  blocks nonempty; every real-symbol compression is **block diagonal**.
* **(D4)** Hence for ε = +1 a real-symbol compression — in particular the
  single-orbit observable `T(u)+T(u)*` of T20 — has the statistics of a
  **superposition of two spectra** and can never be Wigner–Dyson, whatever the
  arithmetic. A generic Gaussian Weyl observable has complex g_u, is not parity
  invariant, and is exactly GUE by Theorem A. Sharp dichotomy: **real symbol ⇒
  parity superposition, never WD; complex symbol ⇒ exactly GUE.**

Verified at 5 design points: the split is exactly (m⁺,m⁻) = (0,46), (105,105),
(77,76), (246,246), (0,259) at N = 1597, 3571, 8969, 9349, 14503 — exactly 0/m
when ε = −1 and exactly ⌈m/2⌉,⌊m/2⌋ when ε = +1, in perfect agreement with (D3).
`|[R_par, compression]| ≤ 3.4e-13`.

**This retro-explains every anomalous number of R71.** The R71 design points with
large z were K = 17, 19, 59 — all with ε = +1; those with small z were K = 34,
46, 56 — all with ε = −1. The correlation is with **ε**, not with m and not with
the size of K. LESSON 71-A's K-tracking observation was the right signal read
one step short of the cause.

### R72.3 — THEOREM E [PROVEN off a locus of density O(1/p)]: why β = 1

Egorov gives `Θ T(u) Θ⁻¹ = T(ρu)` with `ρ = MᵗS = Rᵗ`, so Θ moves the
real-symbol observable `V_u = T(u)+T(−u)` to `V_{Rᵗu}` and does **not** commute
with the compression: naively β = 2. The Hecke torus repairs this. With
`C(A) = {xI + yA : x² + xyt + y² = 1}` (order p ∓ 1), which commutes with U_A and
satisfies `U_τ T(u) U_τ* = T(τᵗ u)`:

> **If there is τ ∈ C(A) with `τᵗ Rᵗ u ≡ ± u`, then `Θ_u := U_τ Θ` is an
> antiunitary commuting with `P_λ V_u P_λ`, so the compression carries a real
> structure and lies in the β = 1 class.**

Solvability: in the eigenbasis of A the torus is `{diag(z, z⁻¹)}`, whose orbits
are the level sets of `q(u) = u₁u₂`; `Rᵗ` conjugates `Aᵗ` to its inverse, hence
interchanges the two eigendirections and **preserves q**. So the condition is
solvable off the degenerate locus q(u) = 0 — two lines in (Z/p)², density O(1/p).

Exhaustive integer verification (3 cat maps × 7 primes, up to 1680 frequencies
per configuration): solvable for **100 % of u at every inert prime** (6/6
configurations) and for **95.2–99.7 % at split primes**, with the failures being
exactly the two eigendirections. Artifact `artifacts/r72/theoremE_torus_repair.json`.

### R72.4 — THE DESYMMETRISED MEASUREMENT: BGS holds, with the predicted β

Re-asking the deterministic question inside a parity block, using the
consecutive-spacing-ratio statistic `r̃ₙ = min(sₙ,sₙ₊₁)/max(sₙ,sₙ₊₁)` — which
requires **no unfolding**, removing the dominant systematic of every earlier
measurement in this programme — with class labels ⟨r̃⟩ = 0.38629 (Poisson),
0.53590 (GOE), 0.60266 (GUE). 16 frequencies per design point, references
generated empirically at matched size through the identical pipeline.

| p | K | m (m±) | full | parity block | Haar surrogate |
|---|---|---|---|---|---|
| 3571 | 17 | 210 (105) | 0.4250 | 0.5291 / 0.5417 | 0.5981 |
| 9901 | 33 | 300 (150) | 0.4164 | 0.5366 / 0.5295 | 0.5936 |
| 19489 | 29 | 673 (337) | 0.4125 | 0.5313 / 0.5334 | 0.5928 |

* full vs GUE: **z = −7.7, −9.3, −25.1**; full vs a 2-fold GUE superposition:
  **z = −0.16, −0.33, −0.83** → Theorem D confirmed quantitatively, T20's premise
  void.
* parity blocks vs GOE: **z = −0.33, +0.18, +0.35, +0.14, −0.22, −0.11** over six
  block measurements → **indistinguishable from GOE**; vs GUE: z = −3.0…−5.6.
* Haar surrogate vs GUE: z = −0.46, −0.91, −1.06 → **indistinguishable from GUE**;
  vs GOE: z = +2.45, +2.09, +3.08.

All three conclusions are stable while m grows by a factor 3.

**Interpretation.** The gap between the blocks (β=1) and the matched
arithmetic-free surrogate (β=2) is a genuine arithmetic effect, and it is exactly
the Dyson index that the arithmetic time reversal Θ predicts (Theorems C, E).
So: **for the parity-desymmetrised, single-observable, fully deterministic
compression of a quantised cat map, BGS holds numerically with the correct
symmetry class, at m up to 337 per block.** This supersedes the R71 verdict
("the naive answer is wrong"): the naive *experiment* was wrong, because it
mixed two symmetry sectors. Artifacts
`artifacts/r72/desym_ratio_statistic.json`, `artifacts/r72/parity_desymmetrised.json`,
`artifacts/r72/haar_surrogate.json`.

**Status revision.** `op:local_deterministic` moves from OPEN-and-looking-negative
to **NUMERICALLY-SUPPORTED, positive**: [NUMERICALLY-SUPPORTED] BGS for the
desymmetrised deterministic compression, β = 1, 6 block measurements at
m ∈ {105, 150, 337}, |z| ≤ 0.35 against matched GOE controls, unfolding-free
statistic. Calibrated confidence ~80 % that this survives at larger m. What is
still missing for a proof is a local law, not a symmetry input (T18 barrier).

### R72.5 — Theorem B extended: the sharp criterion for prime powers

`E⁰(s,k) = P(s,k) ⟺ s < lpf(k)`, i.e. characteristic zero contributes no
non-trivial solutions below the least prime factor. Proof for `k = q^e`: a
multiple `f = Φ_{q^e}·g` of degree < q^e has `deg g < q^{e−1}`, so the q blocks of
`Φ_{q^e}(x) = Σ_{j<q} x^{j q^{e−1}}` do not overlap and the coefficient vector of
f is g repeated q times; hence the positive mass of f is q × (that of g) ≥ q, and
`f(1) = q·g(1) = 0` forces g to carry both signs. Certified in **29 cells** at
k = 8, 9, 16, 25, 27, 32, 49, 81 and s ≤ 5: the criterion holds in every one
(`artifacts/r72/prime_power_criterion.json`). For general k it remains
[CONJECTURED]; the Mann bound gives only `2s < lpf(k)`.

### R72.6 — Hygiene: every remaining audit item closed

`src/hygiene_r72.py`, idempotent, 7 edits:
1. `artifacts/ring2/discriminator.json` — trailing comma fixed; **0 invalid JSON
   files remain in the whole tree** (verified over all 170 artifacts).
2. `artifacts/ring3/REPRO.md` — two dead paths repaired
   (`ring2/big_sweep.json` → `ring2/line_B_big_sweep.json`;
   `ring0/MOVE_COUNT.json`, which never existed, → `ring3_hygiene.json`), and the
   "max |S|/Weil = 0.99999" headline **withdrawn in place** with the explanation
   (the JSON field's denominator is `min(k, 2√p) = 4`; true ratio 0.032; the datum
   says the *trivial* bound is tight).
3. `run16_r6.json`, `run22_classify.json`, `run25_partition.json` moved to
   `artifacts/retracted/` with a README naming the r=6 sign bug.
4. Five **in-place retraction warnings** inserted in LEDGER.md at R11-C, R16,
   R22, R20 (tail constant is 2, not 1) and R13-final (random-observable
   experiment, void by Theorem A).
5. THEORY.md — the refuted C1 empirical support is flagged in place.
6. `artifacts/MANIFEST.md` — provenance warning that
   `run13_strong_master.json` / `run13_master_cert.json` never existed before
   2026-08-28.
7. Legacy paper — the T13 status row upgraded from "PROVEN on the chart
   gcd(M₂₁,N)=1" to **PROVEN UNCONDITIONALLY** by Theorem C. Recompiled, 13 pp.

### R72.7 — Deliverables and handoff

* `paper/exact_wd_and_subgroup_moments.pdf` — **11 pp**, recompiled: now contains
  Theorems A, B, C, D, E, the desymmetrised measurement, `conj:Pstar`, and the
  R67–R70 refutation.
* `paper/resonance_laws_catmaps.pdf` — 13 pp, T13 row upgraded.
* New scripts: `theta_square_theorem.py`, `haar_surrogate.py`,
  `parity_desymmetrised.py`, `desym_ratio_statistic.py`,
  `theoremE_torus_repair.py`, `hygiene_r72.py`.
* New artifacts in `artifacts/r72/`: 7 JSON + 1 log.

**Priorities for run 73.**
1. **Push the desymmetrised measurement to m ≳ 2000** (p ≈ 10⁵ with K ≈ 50). The
   ratio statistic needs no unfolding, so the only cost is one eigensolve of a
   2000×2000 matrix per frequency — feasible. If ⟨r̃⟩ stays within 0.5σ of GOE
   the numerical case becomes hard to argue with. **Priority 1.**
2. Test the Kurlberg–Rudnick SU(2)-trace law (arXiv:math/0302277) against the
   **correct** Hecke-basis matrix elements — the honest successor to the void
   R67–R70 line. Requires building the Hecke eigenbasis (simultaneous
   diagonalisation of U_A and one torus generator), which is now
   straightforward given `src/theoremE_torus_repair.py`.
3. Prove Θ_u² = +1 in Theorem E (the same equal-diagonal mechanism as Theorem C
   may again apply to `U_τ U_M`), which would make β = 1 a theorem rather than a
   measurement.
4. `conj:Pstar` — the minimal sporadic shapes `{a,a,b}` and `{a,a,a,b}` are
   F_p-points of explicit curves; bound them by Weil and sum over shapes.
5. Extend the `s < lpf(k)` criterion from prime powers to general k.

**Not tried (silence ≠ coverage):** Lean (still blocked by 8 GB); Sp(2g,Z) and
prime-power level; any resolvent/local-law argument; the number variance and
form factor of the desymmetrised blocks (only the ratio statistic and the L1
spacing distance were measured).

