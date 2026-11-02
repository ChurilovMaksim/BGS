# G4: the identification, stated precisely (Wave 10, task 3)

**Status: formulation only. Nothing in this note is proved. The repository was
not touched; Lean was not built. All main definitions below were fetched from
current main via the GitHub connector only, pinned at HEAD
`d87dce0d9277579568edfee6cffecbc96ea61024` (PR #76).**

## 0. Sources pinned (blob SHAs at d87dce0)

| File | Blob SHA (prefix) |
|---|---|
| `formalization/Bgs/LineBNAverageBridge.lean` | `3373aa6b…` |
| `formalization/Bgs/LineBNAverageUnits.lean` | `ae0e303d…` |
| `formalization/Bgs/LineBNAverage.lean` | `8b2ce39c…` |
| `formalization/Bgs/LineBExpand.lean` | (fetched, see `g4/expand.lean`) |
| `formalization/Bgs/LineBTsum.lean` | `dc17b0dc…` |
| `formalization/Bgs/LineBTraceFormula.lean` | `f724568a…` |
| `formalization/Bgs/LineBDerand.lean` | `01fa6e63…` |
| `formalization/Bgs/TraceStatement.lean` | `4287d8c1…` |
| `formalization/Bgs/LineBGauss.lean` (`chi`) | (via search; `chi N u = e(u.val / N)`) |
| `computations/verification/lineB/common/model.py` | `ee6296ab…` |
| `computations/verification/lineB/phase1/dlib.py` | `af79ab79…` |

Working copies of the fetched files are in `~/workspace/bgs-breakthrough/g4/`
(`bridge.lean`, `units.lean`, `naverage.lean`, `expand.lean`, `tsum.lean`,
`traceformula.lean`, `derand.lean`, `tracestmt.lean`, `common/model.py`,
`phase1/dlib.py`). They are connector downloads, not repo edits.

## 1. What hTrU actually states — and what it does NOT state

In `LineBNAverageBridge.lean`, theorem `traceHenceTup` (and identically in
`nAverageTup`, `nAverageTup_decay`), the hypothesis is, verbatim in content:

```
(hTrU : ∀ N ∈ NAverage.window X (Dm m).toNat, ∀ [NeZero N],
  TrU N = ((Tsum.kickMatInf N ĝ * catMat N (a N)) ^ m).trace)
```

with `(ha : ∀ N ∈ window …, 2 * (a N) * (-4) = 1)`, `m ≥ 2`, `1 < X`, and
`Summable fun k : ℤ => (k : ℝ)^2 * ‖ĝ k‖`. The Bridge §5 comment says why
`TrU` is abstract: the trace `((kickMatInf * catMat)^m).trace` needs a
`Fintype (ZMod N)` instance, i.e. `[NeZero N]`, which cannot be synthesized
for a bound `N` in a theorem statement, so the theorems are stated for an
abstract agreeing `TrU`.

**Crucial point: hTrU mentions no actual kick at all.** It identifies an
abstract trace function with the trace of the Lean tsum model
(`kickMatInf * catMat`). The identification of that tsum model with any real
quantum kick is a further, unstated step — that further step is G4. Anyone
quoting hTrU as "the kick identification" is over-claiming by exactly one
level. (In `LineBNAverageUnits.lean` the m = 1 analogue uses
`kickMatInf` without the `Tsum.` prefix — same object, different open
namespace — and `TrU N = ((kickMatInf N ĝ * catMat N (a N)) ^ 1).trace`.)

## 2. Btup in the bridge (Lean side)

`LineBNAverageBridge.lean` §3, verbatim in content:

- `phaseTup m ν n = e((-(ν.val : ℝ)) * (yp m : ℝ) * (NmZ m n : ℝ) / (gp m : ℝ))`,
  where `e(t) = exp(2πi t)`, `ν : ZMod (gp m)`, `n : Fin m → ℤ`.
- `Ztup m ĝ ν = ∑' n : Fin m → ℤ, phiFun m ĝ n * phaseTup m ν n`.
- `phiFun m ĝ n = ∏ r : ZMod m, ĝ (n (zmodFinEquiv m r))` (product of the
  abstract Fourier datum `ĝ : ℤ → ℂ` over the m cycle positions).
- `Btup m ĝ ν = ‖Ztup m ĝ ν‖ ^ 2` (a real number).
- `NmZ m n = ∑ i, ∑ j, (n i * n j) * pellX (dist m i j)` with
  `dist m i j = |i - j|` (linear, not cyclic), i.e. `NmZ(n) = Nm(α_n)` for
  `α_n = ∑ j, n_j λ^j`, `λ = 3 + 2√2`.
- `gp m = (pellX m - 1).toNat / gcd((pellX m - 1).toNat, (pellY m).toNat)`,
  `yp m = (pellY m).toNat / gcd(…)`, from `LineBDerand.lean`.
- The `‖TrM‖²` factor of the older `NAverage.Bprof` (`Bprof TrM Z ν =
  ‖TrM‖² * ‖Z ν‖²`) is dropped in `Btup`, legitimately inside Lean because
  `henceTup` proves `‖TrM_N‖ = 1` for every `N` (`‖(catMat N a ^ m).trace‖ = 1`).

Three structural facts about the Lean side:

1. **There is no η in Btup/Ztup.** `ĝ` is an abstract datum; η is
   suppressed entirely. Any identification with a concrete kick must first
   say which `ĝ` — that is G4a below.
2. **Ztup is zero-phase.** The full tsum trace formula (`Tsum.phaseFun`)
   is `e(Qnum / Dm / N) * phase0Fun`, and `phaseTup` is exactly the
   zero-phase factor (`phase0Fun_eq_phaseTup`: the tsum zero-phase at `b`
   equals `phaseTup` at `ν = b % gp`). The `Qnum` phase is NOT part of
   Ztup; its effect is bounded separately in `henceTup` by
   `π·m·s2·s0^{m-1}/N`. So G4 is a zero-phase identification; the Qnum
   phase is an error term, not part of G4.
3. **Ztup is an infinite tsum over tuples**, not a finite sum. The older
   `NAverage.Zfun` is the finite analogue (sum over a finite `S ⊂ ℤ` of
   `Phi n * phase …`); the passage finite → tsum is done inside Lean
   (`Tsum.trace_tendsto`, `mode_sum_tendsto`) and is not part of G4.

The averaging side: `NAverage.window X D = (Ioc ⌊X⌋₊ ⌊2X⌋₊).filter
(Coprime · D)`; `winAvg W f = (∑ N ∈ W, f N) / W.card`;
`nuAvg B = (∑ ν : ZMod g', B ν) / g'` (all residues);
`nuAvgUnits B = (∑ u : (ZMod g')ˣ, B u) / φ(g')` (units only).
G3's `S` is `∑_{ν ∈ units} Btup(ν) = φ(gp) · nuAvgUnits(Btup)`.

## 3. Z_all in dlib (computation side)

`computations/verification/lineB/phase1/dlib.py`, class `Orbits(m)`:

- `CK = {k : fCoeff(k, 0) for k ∈ [-9, 9]}` — **only the l = 0 row** of the
  symbol. `f_diag(θ) = Σ_k CK[k] · e(kθ)`, real-valued (the file asserts
  `|Im| < 1e-12` on a grid; reality is a numerical check there, a lemma to
  prove from the `fCoeff(k, 0)` formula in Lean).
- `S(xi) = Σ_{j=0}^{m-1} f_diag(θ_j(xi))` over the orbit points
  `θ_j(xi) = ⟨L^j e1, xi⟩`, `xi ∈ G^ = (L^m - I)^{-T} ℤ² / ℤ²`,
  `L = [[0,-1],[1,6]]` (multiplication by λ in basis `{1, λ}`).
  The orbit grid has `D = d1·d2 = Dm` points, where `(d1, d2)` is the
  Smith normal form of `L^m - I` (the file asserts `d1·d2 = Dm(m)`).
- `Phi(η) = exp(i·η·S)` (a function on the `d1 × d2` grid).
- `μ = FFT2(Phi) / D` (Fourier coefficients of `Phi` over the dual grid).
- `cls(β) = (yp mod gp) · ((A² + 6AB + B²) mod gp) mod gp`, where
  `(A, B) = P · (b1, b2)` is the SNF representative of the dual class
  `β` (`(L^m - I) = P · diag(d1, d2) · Q`), and `Nm(a, b) = a² + 6ab + b²`.
- `A_r = Σ_{β : cls(β) = r} μ(β)` (class sums, `r ∈ ℤ/gp`).
- `Z_all(η)(ν) = Σ_r A_r · e(-ν·r / gp)` for `ν = 0, …, gp-1`
  (implemented as `np.fft.fft(Acls)`), and
  `F(η) = mean_{ν ∈ units} |Z_all(ν)|²`.

Notes that matter:

- `Z_all` is an **exact finite computation** (FFT over `D` points). It does
  **not** use `dlib.ghat()` (continuum Fourier coefficients of
  `exp(iηf_diag)` via FFT on `L = 4096` points, docstring: "aliasing ~
  superexp small"). `ghat()` is a separate routine; the aliasing question
  belongs to G4a (which `ĝ`?), not to `Z_all` itself.
- `Z_all` has no `TrM` factor and no `Qnum` phase either — it is the
  "limit object" of the source, i.e. the same zero-phase, ratio-like
  level as `Ztup`. That is why a direct equality is even plausible.
- `f_diag` is the l = 0 row only. The full symbol has l = ±1 rows
  (`fCoeff(k, ±1) = rCoeff(k)·(-3 ∓ 4i)/1000`); they do not enter `dlib`
  at all. See §5, point (iii).

## 4. Where the two definitions differ (difference table)

| Aspect | Lean `Btup` | dlib `|Z_all|²` | Status |
|---|---|---|---|
| Sum | Infinite tsum over tuples `n : Fin m → ℤ`, weight `∏ ĝ(n_j)` | Finite FFT over `D` orbit points, then dual class sums | Bridge needed (G4b) |
| Kick datum | Abstract `ĝ : ℤ → ℂ`, no η | Concrete `η ∈ ℝ`, `f_diag` (l = 0 only) | Identification needed (G4a) |
| Class | `yp · NmZ(n) mod gp`, `NmZ(n) = Nm(α_n)` | `yp · Nm(β) mod gp`, `Nm(β) = a² + 6ab + b²` for SNF rep. | Equality mod gp is a lemma (G4b, §4) |
| Phase | `e(-ν·yp·NmZ/gp)`, `ν.val ∈ {0,…,gp-1}` | `e(-ν·r/gp)`, `ν ∈ {0,…,gp-1}` | **Match verbatim** (same sign, same `e`, same `gp/yp`) |
| Residues | Defined on all `ν ∈ ZMod gp`; assembly uses units mean | Defined on all `ν`; `F` uses units mean | Match; G4 needs equality on all `ν` (class identity gives it) |
| Normalization | `‖Ztup‖²`, `‖TrM‖ = 1` proved | `\|Z_all\|²`, no `TrM` | Match if class identity holds with `μ` normalized by `1/D` (numerically confirmed §6, unproved) |
| Qnum phase | Absent (zero-phase); bounded separately by `π·m·s2·s0^{m-1}/N` | Absent | Match at zero-phase level; not part of G4 |
| Cat matrix | `catMat N a`, `a` with `2·a·(-4) = 1`, entries `N^{-1/2}·χ_N(a(3x²-2xy+3y²))` | `MN(N)`, entries `e_N(-8⁻¹(3x²-2xy+3y²))/√N` | **Match** (same formula; only index types differ: `Fin N` vs `ZMod N`) |
| Character | `chi N u = e(u.val / N)` | `e(x) = exp(2πi x)` sampled at `x/N` | Match |
| η regime | None (abstract) | Free `η = O(1)` | Regime gap vs fixed map (§5) |

## 5. The three "actual kicks" — G4c is not an identification

There are three different objects in main that could be called "the kick",
and they are not equal to each other:

1. **Lean tsum kick** `kickMatInf N ĝ = Matrix.diagonal (kickValInf N ĝ)`,
   `kickValInf N ĝ x = ∑' k : ℤ, ĝ k * chi N ((k : ZMod N) * x)`.
   Diagonal by construction, for abstract `ĝ`.
2. **dlib diagonal kick** `D_η = diag(exp(i·η·f_diag(x/N)))`, `η = O(1)` free,
   l = 0 row only. This is what `Z_all`/`F(η)` are about.
3. **Full fixed propagator** `UN N = NormedSpace.exp((i·τ·N) • AN N) * MN N`
   (`TraceStatement.lean`, blob `4287d8c1…`), `τ = 1/10^80`,
   `AN N = Σ_{k,l} fCoeff(k, l) • weylT N (l, k)` over the full 32-mode
   symbol (`l ∈ {-1, 0, 1}`, `k ∈ [-9, 9]`), i.e. a Weyl quantization
   that is **not diagonal** in position basis.

Consequences, stated bluntly:

- "kickMatInf = the actual kick" is **false as an equality with (3)**:
  the matrix exponential of a non-diagonal `A_N` is not diagonal, and
  the l = ±1 rows do not disappear. At best, (1) with `ĝ = ĝ_η` equals
  (2) (see G4a/G4b); reaching (3) from (2) needs a truncation estimate
  for the l = ±1 terms — a separate analytic step, not an identification.
- **Regime gap:** at `N ~ 100`, the fixed coupling gives `τ·N ≈ 10⁻⁷⁸`
  (perturbative regime), while dlib numerics run at `η = O(1)`. Results
  proved for (2) at `η = O(1)` do not transfer to (3) without a scaling
  argument that does not exist in main. This is the same gap flagged in
  wave 3 (M02 step 0) and wave 5 (task 3): the θ-ensemble
  `exp(iηV_θ)·M_N` is a fourth object, random, usable only as error
  control, never as the target.
- The honest target of 175 as formalized may therefore be the diagonal
  model kick (2), with the relation to TRACE-005's `U_N` left as a
  separate open step. G4 must not be stated in a way that smuggles that
  step in.

## 6. Numerical evidence for G4b (not a proof)

Test (script `wave10_task3_G4_check.py`, using the connector-fetched
`g4/phase1/dlib.py` copy): for `m = 3`, compare the tuple class sums
`A_r^tup = Σ_{n : yp·NmZ(n) ≡ r} ∏_j ĝ_η(n_j)` (tuples truncated to
`|n_j| ≤ K`, `ĝ_η` = continuum Fourier coefficients of `exp(iηf_diag)`
via FFT on 16384 points) against dlib's `A_r` (exact finite orbit FFT).

| η | K = 14 | K = 26/32 | K = 45/60/75 |
|---|---|---|---|
| 1.0 | max diff 0.082 | 0.0094 (K=26), 0.00088 (K=32) | — |
| 5.0 | 1.27 | — | 0.206 (K=45), 0.021 (K=60), 0.0013 (K=75) |
| 10.0 | — | — | 2.54 (K=45), 0.92 (K=60), 0.45 (K=75, still decreasing) |

The identity holds in the `K → ∞` limit numerically; the required `K`
scales like the bandwidth `≈ η · max|f'|/(2π) ≈ 7.1·η` (stationary-phase
scale for `exp(iηf)`), which explains the slow convergence at large η
and why a small-`K` test looks like a failure. This is evidence for
G4b, not a proof, and it uses `ĝ = ĝ_η` (continuum coefficients) —
the discrete N-grid coefficients would differ by aliasing
`ĝ_k^{disc,N} = Σ_j ĝ_{k+jN}^{cont}` and must not be substituted silently.

## 7. G4 stated as a theorem to be proved

**Theorem G4 (NOT proved).** Fix `m ≥ 2` (the case `m = 1` is stated
separately below). Let `f_diag(θ) = Σ_{|k| ≤ 9} c(0, k)·e(kθ)` with
`c(0, k) = fCoeff(k, 0)` from `TraceStatement.lean` (equivalently
`model.py`'s `fCoeff(k, 0)`), and assume `f_diag` is real-valued, i.e.
`c(0, -k) = conj(c(0, k))` for all `k` (a lemma from the `fCoeff`
formula, not an assumption to hide). For every real `η`, let
`ĝ_η : ℤ → ℂ` be the continuum Fourier coefficients of
`θ ↦ exp(i·η·f_diag(θ))` on `ℝ/ℤ`, i.e.
`ĝ_η(k) = ∫_0^1 exp(i·η·f_diag(θ))·e(-kθ) dθ`. Assume
`Summable fun k : ℤ => (k : ℝ)^2 * ‖ĝ_η k‖` (in fact `ĝ_η` decays
exponentially, since `f_diag` is a trigonometric polynomial). Then:

(a) **Profile identity.** For every `ν : ZMod (gp m)`,
   `Ztup m ĝ_η ν = Z_all^{dlib}(m, η)(ν.val)` as complex numbers, hence
   `Btup m ĝ_η ν = |Z_all^{dlib}(m, η)(ν.val)|²` as reals.
   In particular `nuAvgUnits (Btup m ĝ_η) = F_m(η)` (dlib's `F`), and
   `S := Σ_{ν ∈ (ZMod gp)ˣ} Btup m ĝ_η ν = φ(gp) · F_m(η)`, so that
   G3's proved bound on `S` applies to the bridge's `S`.

(b) **Kick-matrix identity (diagonal model).** For every odd `N` with
   `gcd(N, (Dm m).toNat) = 1` and every `a : ZMod N` with
   `2·a·(-4) = 1`: `kickMatInf N ĝ_η = Matrix.diagonal
   (fun x : ZMod N => exp(i·η·f_diag(x.val / N)))`, i.e.
   `kickValInf N ĝ_η x = exp(i·η·f_diag(x.val / N))` for all `x`;
   and `catMat N a` equals `model.py`'s `MN(N)` under the index
   transport `Fin N ≃ ZMod N`.

**m = 1 (separate).** `gp 1 = 2`, `yp 1 = 1`; `Ztup 1 ĝ 0 = ∑' ĝ`,
`Ztup 1 ĝ 1 = ∑' (-1)^k ĝ k` (proved in `LineBNAverageM1.lean`); the
orbit side has `D = 4`, `d1·d2 = 4`. G4(a) at `m = 1` is the same
statement with these explicit values, to be checked separately (the
only unit mod 2 is `1`, so `nuAvgUnits = Btup 1 ĝ_η 1`).

**Explicitly NOT part of G4:** any equality involving the full fixed
propagator `UN N` (see §5). That is G4c, a separate analytic step:
bound `‖(exp(iτN·A_N) - diag(exp(iη·f_diag)))·M_N‖` in a regime that
relates `τ·N` to `η`, or state 175 as a theorem about the diagonal
model kick (2) only. Until G4c is done, the assembly proves
hEquidistUnits for the diagonal model kick, not for TRACE-005's `U_N`.

## 8. Sub-identifications, in order of difficulty (easiest first)

1. **catMat = MN.** Formula-identical (`N^{-1/2}`, `a = -8⁻¹`,
   `3x² - 2xy + 3y²`, `χ_N`). Only work: the `Fin N ≃ ZMod N` index
   transport and the `finZ`/`val` bookkeeping. Easy.
2. **Phase/sign/gp/yp conventions.** Both sides use
   `e(-ν·yp·Nm/gp)` with `ν.val ∈ {0,…,gp-1}` and the identical
   `gp`/`yp` formulas from `Derand`. A short lemma, no content:
   check `e` is the same `exp(2πi·)` on both sides (Lean `e` from
   `TraceFormula`, dlib `e(x) = exp(2πi x)`) and that `ν.val` matches
   the integer index of `Z_all`. Easy.
3. **kickValInf = exp(iη·f_diag(·/N)) given ĝ_η.** Fourier series of
   the analytic function `exp(iηf_diag)` evaluated at `x/N`: needs
   uniform convergence from exponential decay of `ĝ_η` (f_diag is a
   trig polynomial, so `exp(iηf_diag)` is analytic; decay rate
   worsens with `|η|`, which is why the bandwidth in §6 grows like
   `7.1·η`). Standard analysis, moderate.
4. **Norm class well-defined mod gp.** The dlib class uses an SNF
   representative `(A, B) = P·b`; the Lean class uses `NmZ(n)` of the
   tuple. Needed lemma: if `v' = v + (L^m - I)w` then
   `Nm(v') ≡ Nm(v) [MOD gp]`. Proof sketch (to be completed): the
   difference is `Tr(v·conj((L^m-I)w)) + Nm((L^m-I)w)`; the second term
   is divisible by `Dm` hence by `gp`; the first is
   `2((x_m-1)u - 2y_m·v')` for some integers `u, v'`, and
   `gp | 4·gcd(x_m-1, y_m)` follows from `(x_m-1)(x_m+1) = 8y_m²` plus
   the 2-adic valuations (`v₂(gp) = 1` for odd `m`,
   `2 + v₂(y_m)` for even `m`, from wave 3) — the odd-prime part from
   `gp | 8g`, the 2-part from the valuations. Moderate (Pell arithmetic).
5. **Tuple ↔ orbit duality (the heart of G4b).** Show
   `μ(β) = Σ_{n : v(n) ≡ β} ∏_j ĝ_η(n_j)` where
   `v(n) = Σ_j n_j·L^j·e1 ∈ ℤ²`, via orbit orthogonality
   `(1/D)·Σ_{xi} e(Σ_j n_j·θ_j(xi) - ⟨β, xi⟩) = 1` iff `v(n) ≡ β`
   in `(L^m-I)`-classes, else `0`; then group by class using (4) to get
   `A_r^tup = A_r^dlib` for all `r`, hence (a) by finite Fourier
   inversion over `ℤ/gp`. Needs: the orbit parametrization
   `θ_j(xi) = ⟨L^j e1, xi⟩`, `L^m`-periodicity, SNF coordinates, and
   the class-sum grouping. Hard, but purely algebraic/Fourier — no
   analysis beyond absolute convergence of the tuple sum
   (`(Σ|ĝ_η|)^m < ∞`).
6. **Decay/aliasing bookkeeping for ĝ_η.** If anyone substitutes
   discrete N-grid coefficients for continuum `ĝ_η`, the aliasing
   error `Σ_{j≠0} ĝ_{k+jN}` must be bounded (it is superexponentially
   small for fixed `η` as `N → ∞`, but not zero). Avoided by stating
   G4 with continuum `ĝ_η` and proving (3) instead. Moderate; do not
   let it be silently skipped.
7. **m = 1 bookkeeping.** Explicit `Ztup` values, `gp = 2`, units = `{1}`.
   Easy but separate; the general-m argument's `m ≥ 2` hypotheses
   (Gauss bridge) do not cover it.
8. **G4c: diagonal model vs full fixed map (hardest, and possibly the
   wrong target).** Estimate the difference between
   `exp(iτN·A_N)` (full 32-mode Weyl quantization, `τ = 10⁻⁸⁰`) and
   `diag(exp(iη·f_diag))`, and relate the regimes `τ·N` vs `η = O(1)`.
   This is not an identification at all: it is an approximation
   theorem with a regime that must be chosen (fixed `η`? `η = τ·N`?
   `η → 0`?). If it cannot be done, the honest conclusion is that
   175 (as assembled) is a theorem about the diagonal model kick, and
   its transfer to TRACE-005 is open. This item must not be merged
   into items 1–7, and must not be "proved" by renaming `η`.

## 9. What G4 does not give (even if 1–7 are proved)

- It does not close G1 (radical draft, wave 8 revision), G2 (units
  draft), or G5 (exact constant as a theorem) — those are separate.
- It does not give the spectrum, CUE/Sine₂, or TRACE-005: a window
  average of `|Tr|²` is not a spectral statistic, and the diagonal
  model kick is not the fixed propagator (G4c).
- It does not fix the `≈2π` constant discrepancy in the bridge's
  first error term (that is the `henceTup` constant, separate from G4).
- It does not cover `η` outside the dlib grid as a theorem unless the
  proofs in (3) and (5) are uniform in `η` — they should be (analytic
  in `η`), but uniformity must be checked, not assumed; the G3 bound
  already holds for all real `η` analytically, so G4 should be stated
  for all real `η` too.

## 10. Files

- This note: `numerics/wave10_task3_G4_identification.md`.
- Numeric check: `numerics/wave10_task3_G4_check.py` (imports the
  connector-fetched `g4/phase1/dlib.py` copy; compares tuple class
  sums against dlib class sums at `m = 3`).
- Fetched main files: `g4/*.lean`, `g4/common/model.py`,
  `g4/phase1/dlib.py` (connector downloads at d87dce0, working copies
  only).
