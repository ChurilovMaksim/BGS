# Wave 21, task 2 — Claim 175 restated as a diagonal-model theorem

**Status of this note.** A precise statement, not a new theorem and not a
Lean formalisation. It instantiates the bridge theorem that *is* proved
in main (`nAverageTup_units`, conditional on `hEquidistUnits`) with the
objects that G4b identifies, and names exactly what is *not* claimed.
Nothing here touches the repository; Lean was not built.

**Sources, all via the GitHub connector at HEAD
`d87dce0d9277579568edfee6cffecbc96ea61024`:** Bridge
`3373aa6b…`, Units `ae0e303d…`, Tsum `dc17b0dc…`, Derand
`01fa6e63…`, NAverage `8b2ce39c…`, TraceStatement `4287d8c1…`,
Expand `3f04d691…`. Import path is flat `Bgs.LineBDerand`
(namespace inside: `Bgs.LineB.Derand`).

## 0. Why a restatement is needed

`hTrU` in the bridge mentions no actual kick at all: it only says an
abstract trace function `TrU` agrees on the window with the tsum trace
`((kickMatInf N ĝ * catMat N (a N)) ^ m).trace`. And
"kickMatInf = the actual kick" is **false** as an equality with the
full fixed propagator `UN N = exp (i·τ·N • AN N) * MN N`
(TraceStatement), where `AN N` is the Weyl quantization of the full
32-mode symbol (`l ∈ {−1,0,1}`, `fCoeff` with `l = ±1` rows
`rCoeff k · (−3 ∓ 4i)/1000`), `τ = 1/10^80`, and `UN N` is not
diagonal. Regime gap, with no scaling argument in main: at `N ~ 100`,
`τN ≈ 10⁻⁷⁸` (perturbative), while the diagonal model below runs at
`η = O(1)` free. So the honest 175 is a theorem about the diagonal
model kick. Transfer to TRACE-005 is open (§4).

## 1. Objects (all definitions verbatim from main, except `ĝ_η`, `D_η`)

Fix `m ≥ 2`, `η ∈ ℝ`. Let `f_diag(θ) = Σ_{|k|≤9} fCoeff(k, 0)·e(kθ)`
be the `l = 0` row of `TraceStatement.fCoeff` (real-valued: `c(0,−k) =
conj c(0,k)`, proved from the formula in wave 11 task 4). Let
`ĝ_η(k) = ∫₀¹ exp(iη·f_diag(θ))·e(−kθ) dθ` be its continuum Fourier
coefficients (exponential decay by the wave-11 strip estimate, so
`s0 := Σ' ‖ĝ_η k‖ < ∞` and `s2 := Σ' k²‖ĝ_η k‖ < ∞`).

- **Diagonal kick.** `Tsum.kickValInf N ĝ x = ∑' k, ĝ k * chi N
  ((k : ZMod N) * x)`, `kickMatInf N ĝ = Matrix.diagonal
  (kickValInf N ĝ)`. G4b (waves 11–12, analytic): `kickValInf N ĝ_η x
  = exp(iη·f_diag(x.val/N))` for every `x : ZMod N`. Write `D_{η,N}`
  for this diagonal matrix.
- **Cat matrix.** `catMat N a` (`Expand`): `N^{-1/2}·χ_N(a·(3x²−2xy+3y²))`,
  with `a N` satisfying `2 * (a N) * (−4) = 1`, i.e. `a = −8⁻¹` in
  `ZMod N`. Under `Fin N ≃ ZMod N` transport, `catMat N a = MN(N)`
  (formula-identical, wave 12 task 3; `MN` is `model.py`'s matrix).
- **Diagonal-model trace.** `TrU_diag N :=
  ((D_{η,N} * catMat N (a N)) ^ m).trace`. Because `TrU_diag` is
  *defined* as the tsum trace, the bridge's `hTrU` holds for it by
  definition — it is not an extra hypothesis in this restatement.
- **Window and profile.** `W := NAverage.window X (Dm m).toNat =
  (Ioc ⌊X⌋₊ ⌊2X⌋₊).filter (Coprime · (Dm m).toNat)`, i.e. `X < N ≤ 2X`
  with `gcd(N, Dm) = 1`. `Ztup m ĝ ν = ∑' n : Fin m → ℤ, phiFun m ĝ n *
  phaseTup m ν n` with `phaseTup m ν n =
  e(−ν.val·yp m·NmZ m n / gp m)`; `Btup m ĝ ν = ‖Ztup m ĝ ν‖²`;
  `nuAvgUnits (B) = (∑ u : (ZMod (gp m))ˣ, B u) / φ(gp m)`.

## 2. Theorem (175-diagonal)

Assume: `2 ≤ m`; `1 < X`; `W.Nonempty`; `Summable (k ↦ k²‖ĝ_η k‖)`;
`C' := π·m·s2·s0^(m−1) ≤ X`; and `hEquidistUnits` in the bridge's
form, i.e. for every inverse-residue sequence `ν` (`ν N · N = 1` in
`ZMod (gp m)` on `W`):

```
|winAvg W (fun N => Btup m ĝ_η (ν N)) − nuAvgUnits (Btup m ĝ_η)|
  ≤ D · min (s0^(2m)) Deff / X.
```

Then:

```
|winAvg W (fun N => ‖TrU_diag N‖²) − nuAvgUnits (Btup m ĝ_η)|
  ≤ ((2·s0^m + 1) · C') / X + D · min (s0^(2m)) Deff / X.
```

**The `hEquidistUnits` input, supplied analytically (not in Lean).**
With `S := φ(gp)·nuAvgUnits`-scale window error (wave-5 assembly),
the G3 bound (wave 6, analytic) is `S ≤ gp·2·d1·R(gp)`, proved at
`m = 3/4/5/6` as `S ≤ 784/9216/26896/627200` against thresholds
`Deff·φ(D)/2` with margins `2.6×/1.5×/102×/52×`, valid for **all real
`η`**. It yields `hEquidistUnits` in two forms: (B) `|diff| ≤
(2S/ρ)/X` at `X ≥ 2R` (`ρ = φ(R)/R`), and (C) `|diff| ≤ D_m·Deff/X` at
`X ≥ ⌈X₀⌉`, `X₀ = D·Deff·φ(R)/(Deff·φ(D) − S)`, provided
`S < Deff·φ(D)` (exact `X₀`: `14.15/6.04/82.01/70.00` at `m = 3/4/5/6`).
The first error term is the bridge's Lean-proved pointwise term
(`traceHenceTup` + `pointwiseTup`); only the `hEquidistUnits` factor
is analytic.

**`m = 1` (separate, from `nAverageM1_units` + `nuAvgUnits_one`).**
`gp 1 = 2`, units `= {1}`, `nuAvgUnits (Btup 1 ĝ) = Btup 1 ĝ 1`, and
the window mean equals the units mean; G4b at `m = 1` gives
`Z_all(0) = ∑' ĝ_η`, `Z_all(1) = ∑' (−1)^k ĝ_η(k)`.

## 3. Status of each ingredient

| Ingredient | Status |
|---|---|
| `traceHenceTup`, `nAverageTup_units` (conditional), `Ztup_norm_le`, window lemmas | Proved in main (Lean) |
| G4b: duality `Ztup = Z_all`, norm class `gp ∣ 8y_m`, `kickValInf = exp(iηf_diag)`, `catMat = MN` | Proved analytically (waves 11–12), not in Lean |
| G3 S-bound; `hEquidistUnits` assembly from it | Proved analytically (waves 5–6), not in Lean |
| This restatement as a Lean theorem | Not formalised; it is an instantiation, not a new proof |

## 4. Explicitly NOT claimed

1. **No full propagator.** Nothing here is a statement about
   `Tr((UN N)^m)`, about `exp(iτN·A_N)` vs `D_{η,N}`, or about any
   relation between `τN` and `η = O(1)`.
2. **No TRACE-005, no spectrum, no CUE/Sine₂.** No spectral
   conclusion follows from a window average of `‖Tr‖²`.
3. **No exact constant as a theorem.** The `≈2π` bridge-constant
   discrepancy is a separate `henceTup` issue; the bound above keeps
   the bridge's first error term as stated.
4. **No discrete-grid coefficients.** The statement uses continuum
   `ĝ_η`; substituting N-grid coefficients needs aliasing bookkeeping
   (`Σ_{j≠0} ĝ_{k+jN}`), explicitly avoided here.
5. **No uniformity in `η` beyond the per-`η` bound.** The S-bound
   holds for all real `η`, but `s0, s2` depend on `η`; the bound is
   per-`η` unless `s0, s2` are bounded uniformly, which is not shown.
6. **No claim about `s`-dependence or the limit `X → ∞` beyond the
   stated `1/X` bound at fixed `X`.** The limit reading of 152
   (`B2′`: `lim(Bsym_fiber − Δ)`) is separate (wave 19 task 2).

## 5. What would close transfer to TRACE-005 (G4c, open)

An estimate comparing `exp(iτN·A_N)` with `D_{η,N}` (including the
`l = ±1` rows) plus a regime relation between `τN` and `η`, neither
of which exists in main. Until G4c is done, 175-as-proved is exactly
the theorem of §2, and any citation of 175 for the full fixed map
over-claims by exactly that step.
