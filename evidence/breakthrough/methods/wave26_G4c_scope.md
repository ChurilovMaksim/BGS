# Wave 26, task 4 — G4c scoped: the transfer estimate, regimes, verdict

**Status.** Scoping note, not a theorem about the full propagator.
Computation at N = 101 from `g4/common/model.py` (= TraceStatement
definitions, connector-pinned at d87dce0); script
`wave26_G4c_compute.py`. Repository untouched; no Lean built.

## 0. The two operators (exact, from main)

- Full: `U_N = exp(iτN·A_N)·M_N`, `τ = 1/10^80` FIXED (TraceStatement:
  "not sent to 0 with N"); `A_N = Σ fCoeff(k,l)·weylT_N(l,k)`, 32 modes,
  `l ∈ {−1,0,1}`; `M_N = catMat` under transport (G4b).
- Diagonal model: `D_{η,N} = diag(exp(iη·f_diag(x/N)))`, `f_diag` = l = 0
  row `Σ_{|k|≤9} fCoeff(k,0)e(kθ)`, real; G4b: `kickValInf N ĝ_η` is
  exactly this.
- `A_N` structure (verified at N = 101): Hermitian; `diag(A_N) =
  f_diag(x/N)` EXACTLY (max diff 4.2e-15); off-diagonal band `l = ±1`
  only, entries `Σ_k rCoeff(k)(−3∓4i)/1000 · phase`, `|entry| ≤ 0.02`;
  `‖A_N‖ ≤ Σ|c_{kl}| = 1.151`.

## 1. G4c as ONE estimate

`δ(N,η) := ‖exp(iτN·A_N) − D_{η,N}‖`. Then `‖U_N − D_{η,N}M_N‖ = δ`
(`M_N` unitary). Propagation: `‖X^m − Y^m‖ ≤ m‖X−Y‖` (unitary
telescoping), `|Tr X − Tr Y| ≤ N‖X−Y‖`, so the window-average
squared-trace transfer error is `≤ 2mN²δ` unconditionally, and
`≤ 2mNTδ` if `|Tr| ≤ T` on the window (bridge scale `T = O(1)`,
since `Btup = O(s0^m)`). Everything below is about `δ`.

## 2. Numbers at N = 101

| Quantity | Value |
|---|---|
| `‖A‖`, `‖A_off‖`, ratio | 1.076299, 0.032685, 0.0304 |
| max band entry, band RMS | 0.019025, 0.007537 |
| `f_diag` range on grid | [−1.076, 0.900] |
| `θ = τN`, `θ‖A‖` | 1.01e-78, 1.087e-78 |
| `‖D_1 − I‖`, hence `‖U_full − U_diag(η=1)‖` | 1.025092 ± 1.1e-78 |
| matched `η=θ`: `‖exp − D_θ‖` vs signal `‖exp − I‖` | 3.30e-80 vs 1.087e-78 (rel. 3.04%) |
| floor, ANY diagonal `D`: `‖exp(iθA) − D‖ ≥ θ·0.019025 − O(θ²)` | 1.92e-80 |
| `θ=1` (i.e. `N~10^80`): `min_η ‖exp(iA) − D_η‖` at `η=1.00`; `‖U−diag(U)‖` | 0.032631; 0.032633 |
| averages, m=3 (dlib): `F(0)`, `F(0.5)`, `F(1)` | 1.000000, 1.087125, 1.342517 |

## 3. Regimes — verdict

- **R1, feasible N, fixed η ≠ 0: NO approximation (proof).**
  `δ ≥ ‖D_η − I‖ − θ‖A‖`, and `‖D_η − I‖ = 2max_x|sin(ηf_x/2)| →
  2max_θ|sin(ηf(θ)/2)| > 0` for every fixed `η ≠ 0` (`f` nonconstant
  continuous ⇒ its range is an interval, cannot sit in `2πℤ/η`).
  So `δ = O(1)`. The averages themselves differ too: full `≈ F(0) = 1`,
  diagonal `= F(η)` (0.3425 apart at m=3, η=1). G4c in this form is FALSE.
- **R2, matched η(N) ≲ τN: approximation HOLDS but is VACUOUS.**
  `δ ≈ τN‖A_off‖`; average transfer error `≲ 2mN²τN‖A_off‖`,
  negligible for `N ≪ 10^26` (crude) / `10^39` (sharp). But the target
  is `F(η) = 1 + O(η²) ≈ 1 + O(τ²N²)` (~1e-156 at N=101), far below the
  bridge's `1/X` term for any feasible `X`; and the relative operator
  error stays 3.04% — the `l=±1` rows are never captured.
- **R2′, τN ≪ η(N) → 0** (e.g. `η = N^{-1/2}`): `δ ≈ ‖D_η − I‖ ~
  η‖f‖ ≫ θ` — no approximation; content still tends to `F(0) = 1`.
- **R3, θ ~ 1, N ~ 10^80: infeasible AND obstructed.** No numerics
  exist at such windows; the diagonal floor 0.0326 is a symbol
  property, independent of N (band entries do not vanish with N);
  η-tuning cannot beat it (min over η computed). Transfer unproven
  and infeasible as a regime.
- **Conclusion: NO regime makes the η=O(1) diagonal model approximate
  the full propagator.** The only regime with a good diagonal
  approximation (η~τN) has negligible content.

## 4. The honest transfer (what actually goes through)

`U_N = M_N + O(τN)` in operator norm (`‖exp(iθA) − I‖ ≤ θ‖A‖`).
Hence the full-propagator 175-average equals the cat-map average up
to `O(mN²θ)` crude (≈6.6e-74 at N=101, m=3). And the cat-map case IS
the bridge theorem at `ĝ_0`: `kickMatInf(ĝ_0) = I` (since `ĝ_0 = δ`),
`Ztup ≡ 1`, `Btup ≡ 1`, `nuAvgUnits = 1`, G3 holds for all real η
including 0. So transfer = (a) kick negligible (trivial, above) +
(b) cat-map average (bridge at η=0) — and NEITHER step uses the
η=O(1) diagonal model. The diagonal model and the full propagator
have DIFFERENT 175-limits (`F(η)` vs 1); no estimate bridges them at
fixed η. Caveat: (a)+(b) give only the window average of `‖Tr‖²`;
TRACE-005 needs spectral input beyond that (wave-21 §4.2), a further
open step even after G4c is correctly scoped.

## 5. What would change the verdict

- `τ` N-dependent with `τN ~ 1` at feasible N: re-scope R3 (but τ is
  fixed at 1e-80 in main).
- A banded (not diagonal) model including the `l=±1` rows: removes
  the 3.04% relative error — but then it is not the bridge's
  `kickMatInf`, and 175 needs restating.
- Nothing else: the O(1) gap at fixed η is a theorem (R1), not a
  missing estimate.
