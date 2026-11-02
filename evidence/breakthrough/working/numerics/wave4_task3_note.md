# Wave 4, task 3 — exact constant for hEquidistUnits, actual kick (numerical only, not a proof)

## Sources (pinned HEAD, via GitHub connector only)

- HEAD pinned: `6dbcc7a0ed38d780ff7643bdb55917a9bc5efed1` (PR #75).
  NOTE: current main HEAD has since moved to `d87dce0d…` (PR #76, Lean batch 2);
  the files below were re-verified at the pinned ref, not at the new HEAD.
- `computations/verification/lineB/common/model.py`, SHA `ee6296ab…`:
  `rCoeff`/`fCoeff`, diagonal coefficients `c(0,k)`, `|k|≤9`.
- `computations/verification/lineB/phase1/dlib.py`, SHA `af79ab79…`:
  `Orbits` (SNF orbit sums, `cls = yp·Nm mod gp`, `Z_all`, `F`).
- `formalization/Bgs/LineBDerand.lean`, SHA `01fa6e63…`: `Dm`, `gp`.
- `formalization/Bgs/LineBNAverageUnits.lean`, SHA `ae0e303d…`:
  `nuAvgUnits` = mean over `(Z/gp)^×` of `Btup`.
- `formalization/Bgs/LineBNAverageBridge.lean`, SHA `3373aa6b…`:
  the ≈2π factor in this file (header lines ~60–61, §4 lines ~421–423) is
  between the bridge's pointwise first-error constant
  `(2·s0^m+1)·π·m·s2·s0^{m−1}` and 175's `m·s2·s0^{2m−1}`
  (ratio `π·(2+s0^{−m}) ≈ 2π`). It is NOT a prediction for
  `X·|winAvg − nuAvgUnits|`, which is the hEquidist (second, window) error.

## Definitions used

- `Btup(ν) = |Z_all(η)[ν]|²` for `ν ∈ (Z/gp)^×` (dlib limit profile, same as wave 3 task 2).
- `nuAvgUnits = mean_ν Btup(ν)`, `S = φ(gp)·nuAvgUnits`.
- `W_X = {X < N ≤ 2X, gcd(N,D)=1}`, `ν_N = N^{−1} mod gp`,
  `winAvg(X) = mean_{N∈W_X} Btup(ν_N)`, `diff(X) = winAvg − nuAvgUnits`.
- `η ∈ {0.5, 1, 2, 5, 10, 25, 50, 100, 200}` (project grid from wave 3 task 2).
- `X ∈ {10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000}`,
  plus a dense grid `10000–30000 step 1000` and `40000–100000 step 10000`
  for selected (m, η).
- `s0_f = Σ_k |c(0,k)| = 1.110998` (coefficients of `f` itself, from model.py).
- `s0_exp(η) = Σ_k |Fourier coeff of exp(iηf)|`, FFT grid 16384, verified
  unchanged at grids 4096 and 65536 (η=10: 9.9619; η=200: 47.1063).

## Verdict: X·|diff| does NOT stabilize to a limit

It is a bounded oscillation whose band does not shrink from X=10⁴ to X=10⁵.
On the dense grid it cycles through a small repertoire of values that recur
at larger X (e.g. m=3, η=10: {0, 2.4, 3.2, 7.8, 11.1, 17.4, 19.7};
m=6, η=200: {0, 61.2, 88.3, 134.0, 146.1, 149.4, 280.1}).
Mechanism: `X·|diff| = (X/|W|)·|Σ_ν dev_ν(X)·Btup(ν)|` with count deviations
`dev_ν = c_ν − |W|/φ(gp)` bounded (`max|dev| ≤ 0.98` over all X, m here,
consistent with the C2 spread ≤ 1) and determined by X modulo the small
moduli, while `X/|W| → 1/ρ`. Hence there is no single limit, only a
supremum over residue patterns — an (m, η)-dependent number with no closed
form among the candidates below. The X+D test moves X·|diff| by ≤ ~0.01
(m=6: 61.176 → 61.168 → 61.167), i.e. the oscillation is essentially a
function of X mod small moduli plus a slowly drifting prefactor, not a
decaying transient.

## Supremum table (over the X grid, all η; dense-grid maxima in brackets)

| m | D·Deff | 4·gp·s0_f^{2m} | max sup X·|diff| (η) | sup/2π | sup/(D·Deff) | sup/(4gp·s0_f^{2m}) | S/ρ at that η |
|---|--------|---------------|-------------|--------|--------------|---------------------|------------------|
| 3 | 9604 | 105.3 | 31.14 (η=25) | 4.96 | 3.2·10⁻³ | 0.296 | 84.1 |
| 4 | 82944 | 445.7 | 67.70 (η=10) | 10.77 | 8.2·10⁻⁴ | 0.152 | 408.6 |
| 5 | 11303044 | 939.7 | 333.20 (η=2) [dense 312.46] | 53.03 | 2.9·10⁻⁵ | 0.355 | 1402.5 |
| 6 | 192080000 | 3960.7 | 280.09 (η=200) | 44.58 | 1.5·10⁻⁶ | 0.071 | 3266.8 |

Sup over η ranges: m=3: 1.41–31.14; m=4: 5.02–67.70; m=5: 48.71–333.20; m=6: 46.62–280.09.

## Comparison with the three candidates

- **2π (≈6.283): NO.** X·|diff| is 0.2×–53× 2π depending on (m, η, X);
  it is not ≈2π, and no (m, η) has its whole band at 2π. (The bridge's
  genuine ≈2π factor belongs to the pointwise first error term, see above.)
- **D_m·Deff: NO, by 3–6 orders of magnitude.** The Deff branch is a valid
  but extremely loose upper bound for the actual kick (consistent with
  wave 3 task 2's ≥46× S-route margin; here the slack is far larger because
  the observed constant is the deviation-weighted sum, not S/ρ).
- **4·gp·s0^{2m}: ambiguous — and with s0_f, invalid as a derivation.**
  - With `s0_f` (coefficients of `f`): the number 4·gp·s0_f^{2m} happens
    to sit 3–14× above the observed sup, BUT the bound it comes from is
    false for this profile: `Btup ≤ s0_f^{2m}` fails, since
    `S/(φ(gp)·s0_f^{2m})` reaches 3.97 (m=3), 4.54 (m=4), 6.21 (m=5),
    4.31 (m=6). `s0_f` is not the bridge's s0 for the kick `exp(iηf)`.
  - With the consistent `s0_exp(η)`: `4·gp·s0_exp^{2m}` ranges from
    8.1·10² (m=3, η=0.5) to 1.3·10²³ (m=6, η=200) — a valid trivial bound
    (`|Z| ≤ Σ|φ| = s0_exp^m`) but vacuous, 10⁵–10²⁰ times the observed sup.
- **Sharpest honest bound among those computed:** the deviation bound
  `X·|diff| ≤ (X·maxdev/|W|)·Σ_ν|Btup(ν)−nuAvg|`. Observed maxima are
  0.10–0.56 of it (dense grid), i.e. it overestimates by 2–10× because the
  count deviations and the Btup profile are not aligned. The exact
  constant is `sup_X (1/ρ)·|Σ_ν dev_ν(X)·(Btup(ν)−nuAvg)|`, computable
  numerically per (m, η) but not equal to any of 2π, D·Deff, 4·gp·s0^{2m}.

## Cross-checks

- `nuAvg` reproduces the wave 3 task 2 table to 4 decimals for all (m, η).
- Brute-force averaging over N (no count aggregation) reproduces the
  count-based X·|diff| exactly at the three test points
  (m=5, η=2, X=20000: 281.70; m=6, η=200, X=50000: 280.09;
  m=3, η=10, X=10000: 11.08).
- Count deviations: `max|c_ν − |W|/φ| ≤ 0.98` over the whole grid.

## Files

- Script: `wave4_task3_exact_constant.py`, log `wave4_task3.log`,
  results `wave4_task3_results.json`.
- Dense-grid script: `wave4_task3_dense.py`, log `wave4_task3_dense.log`,
  results `wave4_task3_dense.json`.
- This note: `wave4_task3_note.md` (all under `~/workspace/bgs-breakthrough/numerics/`).

Repository untouched; Lean not built. Numerical result only, not a proof.
