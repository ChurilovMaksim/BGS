# G4b remainders: kickValInf Fourier series, catMat = MN, m = 1 bookkeeping

**Status: analytic proofs (not Lean theorems). Repository untouched; no
`lake build` run. Definitions fetched from current main via the GitHub
connector only, pinned at HEAD `d87dce0d9277579568edfee6cffecbc96ea61024`
(PR #76). G4c (diagonal model vs full fixed propagator) is explicitly
OUT of scope and is not smuggled in anywhere below.**

## 0. Sources pinned at d87dce0 (connector fetch, this task)

| File | Blob SHA |
|---|---|
| `formalization/Bgs/LineBTsum.lean` | `dc17b0dc3ac4cb05c15f030b1520652f22602107` |
| `formalization/Bgs/LineBExpand.lean` | `3f04d691166d04fce336c4b460f26ada2b63a502` |
| `formalization/Bgs/LineBGauss.lean` | `ea645aaf81209e27da7b85a5340f64a6ad13d29c` |
| `formalization/Bgs/LineBTraceFormula.lean` | `f724568a24eb32f6ab39cfe8d76cdccfc5bf6c73` |
| `formalization/Bgs/LineBNAverageBridge.lean` | `3373aa6b3e73363913cf2d110bb2d8edab74bfa2` |
| `formalization/Bgs/LineBNAverageM1.lean` | `545b23c7a523e5fda3e8d3b953a6a8a24960827a` |
| `formalization/Bgs/LineBNAverageUnits.lean` | `ae0e303d7a587dee86d0c8729ba121186d40789f` |
| `computations/verification/lineB/common/model.py` | `ee6296abf76e7a7901132e3ce704ce5baaed3800` |

dlib's `Orbits` definitions are as pinned in wave 11 task 4 at the same
HEAD (`dlib.py` `af79ab79…`); they were not re-fetched here because
nothing in this task touches the orbit side except through the
wave-11 duality (D), which is cited, not re-proved.

Definitions used, in the sources' own notation:

- `e(t) = Complex.exp (2 * π * I * t)` (`TraceFormula`, line 1120),
  so `e` is 1-periodic: `e(t + n) = e(t)` for `n ∈ ℤ`.
- `chi N u = e (u.val / N)` (`Gauss.chi`); `chi` is an additive
  character: `chi N (u + v) = chi N u * chi N v` (`Gauss.chi_add`,
  in main), `chi N 0 = 1`, `star (chi N u) = chi N (-u)`.
- `kickValInf N ĝ x = ∑' k : ℤ, ĝ k * chi N ((k : ZMod N) * x)`
  (`Tsum`), `kickMatInf N ĝ = Matrix.diagonal (kickValInf N ĝ)`.
- `catMat N a x y = (√N : ℂ)⁻¹ * chi N (a * (3x² − 2xy + 3y²))`
  (`Expand`).
- `phaseTup m ν n = e (−ν.val * yp m * NmZ m n / gp m)` (`Bridge`).
- `Ztup m ĝ ν = ∑' n, phiFun m ĝ n * phaseTup m ν n`,
  `Btup m ĝ ν = ‖Ztup m ĝ ν‖²` (`Bridge`).
- `nuAvgUnits B = (∑ u : (ZMod g')ˣ, B u) / φ(g')` (`Units`).
- `model.py`: `MN(N)[x,y] = eN(N, ph)/√N`,
  `ph = (−inv8·(3x² − 2xy + 3y²)) mod N`, `inv8 = 8⁻¹ mod N`,
  `eN(N,t) = exp(2πi·(t mod N)/N)`;
  `fCoeff(k,0)` = the l = 0 row, `f_diag(θ) = Σ_k fCoeff(k,0)·e(kθ)`.
- `ĝ_η(k) = ∫₀¹ exp(iη·f_diag(θ))·e(−kθ) dθ` (continuum
  coefficients, as in wave 11 §4; never dlib's discrete `ghat()`).

Wave-11 inputs cited (not re-proved): the strip estimate for `ĝ_η`
(`Σ_k |ĝ_η(k)| < ∞`, `Σ_k k²|ĝ_η(k)| < ∞`, Fourier series of
`g_η(θ) = exp(iη·f_diag(θ))` absolutely and uniformly convergent to
`g_η`); the duality (D) `μ(β) = Σ_{n:[v(n)]=[β]} Φ(n)`; the norm
class (N) `yp·NmZ(n) ≡ yp·Nm(β) [MOD gp]`; the profile identity (P)
`Ztup m ĝ_η ν = Z_all^dlib(m,η)(ν.val)`, `Btup = |Z_all|²`.

## 1. (i) kickValInf is the Fourier series of the diagonal kick

**Theorem.** Let `N ≥ 1`, `x : ZMod N`, `η ∈ ℝ`, and `ĝ_η` the
continuum coefficients above. Then

```
kickValInf N ĝ_η x = exp(iη · f_diag(x.val / N)),
```

where `x.val / N` is the rational `x.val / N` cast to `ℝ`
(`f_diag` is 1-periodic, so the choice of representative mod 1
is irrelevant). Consequently

```
kickMatInf N ĝ_η = Matrix.diagonal (fun x => exp(iη · f_diag(x.val / N))),
```

which is dlib's diagonal kick `D_η = diag(exp(iη·f_diag(x/N)))`
under the index transport `Fin N ≃ ZMod N` (see §2 for the
transport; the diagonal value at `x` is the statement).

*Proof.*

**Step 1 — summability.** By the wave-11 §4 strip estimate,
`Σ_k |ĝ_η(k)| < ∞` (in fact `Σ_k k²|ĝ_η(k)| < ∞`, the Bridge's
hypothesis). Hence `Tsum.summable_kick` (already in main, from
`‖chi‖ = 1`) gives that the tsum defining `kickValInf` exists
and is the limit of finite partial sums.

**Step 2 — character bookkeeping.** Claim:
`chi N ((k : ZMod N) * x) = e(k * x.val / N)` for all `k : ℤ`.

Indeed, `(k : ZMod N) = k • (1 : ZMod N)` (integer cast is
`zsmul` by `1`) and `x = x.val • (1 : ZMod N)` (nat cast of the
representative; `ZMod.natCast_val`-type fact), so in the ring
`ZMod N`,
`(k : ZMod N) * x = (k * x.val) • (1 : ZMod N)`.
Since `chi N` is an additive character (`chi_add` in main),
`u ↦ chi N u` is a group homomorphism `(ZMod N, +) → ℂˣ`, so
`chi N (t • 1) = chi N 1 ^ t` for `t ∈ ℤ` (for `t < 0` this is
the inverse, i.e. `chi N (-u) = (chi N u)⁻¹`, consistent with
`chi_conj`/`‖chi‖ = 1` in main).
And `chi N 1 = e(1/N)`: for `N ≥ 2`, `(1 : ZMod N).val = 1`;
for `N = 1`, `ZMod 1` is trivial, both sides are `1`
(`e(1) = 1` by 1-periodicity). Hence
`chi N ((k : ZMod N) * x) = e(1/N)^(k * x.val)
= exp(2πi · k * x.val / N) = e(k * x.val / N)`.

This is the only bookkeeping step, and it is the step the
wave-11 note flagged: it uses the homomorphism property of
`chi`, not a `val`-of-product computation, so no `mod N`
subtleties for negative `k` arise (they are absorbed by
`e`'s 1-periodicity).

**Step 3 — Fourier inversion.** By Step 2,

```
kickValInf N ĝ_η x = ∑' k : ℤ, ĝ_η(k) * e(k * θ),
θ = x.val / N,
```

absolutely convergent (Step 1, `|e| = 1`). By the wave-11 §4
uniform-convergence result, the Fourier series of the analytic
1-periodic function `g_η(θ) = exp(iη·f_diag(θ))` converges
absolutely and uniformly to `g_η(θ)` at every `θ`. Hence the
sum equals `g_η(θ) = exp(iη·f_diag(x.val / N))`. ∎

*Scope notes.*

- `N = 0` is excluded, and harmlessly: `ZMod 0 ≃ ℤ`, and
  `chi 0 u = e(u.val / 0) = e(0) = 1` degenerates, while the
  bridge only ever uses `N ≥ 2` with `[NeZero N]` (and `hTrU`
  requires `[NeZero N]`). No bridge statement is lost.
- The statement is for continuum `ĝ_η`. Substituting discrete
  N-grid coefficients changes the left side by the aliasing
  sum `Σ_{j≠0} ĝ_{k+jN}` (wave-10 item 6); that bookkeeping is
  avoided here by using continuum coefficients, exactly as in
  wave 11.
- `η` is arbitrary real; constants in the §4 estimates depend
  on `η`, uniformly on compact `η`-intervals, so (i) holds for
  every real `η` individually, as G4 requires.
- No break was found: (i) is proved, modulo the cited wave-11
  §4 estimates (which are themselves proved there from the
  strip Cauchy estimate) and the `chi_add` lemma already in
  main.

## 2. (ii) catMat = MN, under exactly the bridge hypothesis

**Theorem.** Let `N ≥ 1` with `gcd(N, 8) = 1` (in particular every
bridge-window `N`, since `gcd(N, Dm m) = 1` and `Dm m` is even),
and let `a : ZMod N` satisfy the bridge hypothesis
`2 * a * (-4) = 1` in `ZMod N`. Then, after reindexing by the
equivalence `Fin N ≃ ZMod N` (Mathlib `ZMod.finEquiv`, with
`(finEquiv i).val = i.val`), the Lean matrix `catMat N a`
equals `model.py`'s `MN(N)` entrywise.

*Proof.* The bridge hypothesis gives `-8 * a = 1` in `ZMod N`
(`2 * a * (-4) = -8a` by ring), i.e. `a = -8⁻¹` in `ZMod N`.
Transport indices: write `x, y : ZMod N` as `x = (i : ZMod N)`,
`y = (j : ZMod N)` with `i = x.val`, `j = y.val` (this is what
`finEquiv` does). Then Lean's entry is

```
catMat N a x y = (√N : ℂ)⁻¹ * chi N (a * (3x² − 2xy + 3y²)).
```

The `ZMod N` element `a * (3x² − 2xy + 3y²)` has `val` equal to
`((-inv8) * (3i² − 2ij + 3j²)) mod N`, i.e. exactly `model.py`'s
`ph` (since `a = -inv8` and the polynomial is computed mod `N`
on both sides). Hence, by the definition of `chi`,
`chi N (a * (3x² − 2xy + 3y²)) = e(ph / N) = exp(2πi·ph/N)`,
and `ph ∈ [0, N)` so `model.py`'s `(ph mod N)` is `ph` itself:
this is `eN(N, ph)`. Finally `(√N : ℂ)⁻¹ = 1/√N`, matching
`MN`'s `/np.sqrt(N)`. ∎

*Precise scope — the identification is conditional, and that
conditionality is the content.*

- Without the hypothesis `2*a*(-4) = 1`, `catMat N a` is the
  `a`-general cat matrix, while `model.py`'s `MN` hardcodes
  `a = -8⁻¹`. So "catMat = MN" is true for the bridge's `a`,
  not for arbitrary `a`. This is not a gap: the bridge always
  carries exactly this hypothesis (`hTrU`, `henceTup`,
  `traceHenceTup` all assume it).
- For even `N`, `8⁻¹ mod N` does not exist: `model.py`'s
  `pow(8, -1, N)` raises, and `-8a = 1` is impossible in
  `ZMod N`. The two sides fail in the same place, consistently.
  Bridge-window `N` are odd (coprime to even `Dm`), so the
  case needed is exactly the case where both sides exist.
- No sign error: `model.py`'s `ph` uses `-inv8`, and the bridge
  hypothesis forces `a = -inv8`, not `+inv8`. (Had the bridge
  used `2*a*4 = 1`, the identification would have failed by a
  sign; it does not.)
- No break was found: (ii) is proved, conditional on the
  bridge hypothesis as stated.

## 3. (iii) m = 1 bookkeeping — complete, mostly already in main

The following are already proved in main (cited, not re-proved):

- `Dm 1 = 4`, `gp 1 = 2`, `yp 1 = 1` (`NAverageM1.dm_one`,
  `gp_one`, `yp_one`, by `decide`).
- Window: `gcd(N, 4) = 1`, hence `N` odd, hence
  `(N : ZMod (gp 1)) = 1` (`window_cast_eq_one`), hence the
  inverse residue is constant: `ν N = 1` for every window `N`
  (`window_nu_eq_one`).
- Profile values (`Ztup_one_eq`, `Ztup_one_zero`,
  `Ztup_one_one`, from `NmZ 1 n = (n 0)²`, `yp 1 = 1`,
  `gp 1 = 2`, and parity of squares):
  `Ztup 1 ĝ 0 = ∑' k : ℤ, ĝ k`,
  `Ztup 1 ĝ 1 = ∑' k : ℤ, ĝ k * (-1)^k`.
- Units mean (`Units.nuAvgUnits_two`, `nuAvgUnits_one`):
  `(ZMod 2)ˣ = {1}`, `φ(2) = 1`, so
  `nuAvgUnits (Btup 1 ĝ) = Btup 1 ĝ 1`.
- Window mean = units mean at `m = 1`
  (`Units.winAvg_units_one`): since `ν N = 1` on the whole
  window and the only unit is `1`, the window average of
  `Btup 1 ĝ (ν N)` equals `nuAvgUnits (Btup 1 ĝ)` exactly
  (gap `0`, as in wave-1's `nAverageM1_units`).

*New check in this task: the wave-11 duality (D) at m = 1
reproduces exactly these values on the dlib side.*

The wave-11 duality proof does not use `m ≥ 2` anywhere: the
Fourier expansion, the pairing, and the character orthogonality
all work for `m = 1`. The only `m = 1`-specific computation is
the class map, done here: `D = Dm 1 = 4`,
`G = ℤ²/(L − I)ℤ²` (det `L − I = −4`), `S(ξ) = f_diag(θ₀(ξ))`
(single term), `v(n) = n₀·e1` for `n : Fin 1 → ℤ`, and

```
cls([v(n)]) = yp · Nm(v(n)) mod gp = n₀² mod 2 = parity of n₀,
```

since `yp 1 = 1`, `gp 1 = 2`, `Nm(a, 0) = a²`. Hence, with
absolute convergence from wave-11 §4,

```
A₀^tup = Σ_{k even} ĝ_η(k),  A₁^tup = Σ_{k odd} ĝ_η(k),
Z_all(0) = A₀ + A₁ = ∑' ĝ_η,
Z_all(1) = A₀ − A₁ = ∑' (-1)^k ĝ_η(k),
```

exactly `Ztup_one_zero`/`Ztup_one_one` with `ĝ = ĝ_η`.
Therefore `Btup 1 ĝ_η ν = |Z_all(ν)|²` for `ν ∈ {0, 1}`,
the dlib units mean `F₁(η) = |Z_all(1)|²` equals
`nuAvgUnits (Btup 1 ĝ_η) = Btup 1 ĝ_η 1`, and the window mean
equals the same value (since `ν N = 1`).

*Distinction to preserve (already in main, M1 §4–§5):*
`nuAvg` over ALL residues at `m = 1` is
`(Btup 1 ĝ 0 + Btup 1 ĝ 1) / 2` (`nuAvg_one_eq`), which is NOT
`nuAvgUnits = Btup 1 ĝ 1`. G4's target is `nuAvgUnits`, so
there is no conflict — but anyone quoting "the m = 1
average" must say which average. The `hEquidist`-in-bridge-form
counterexample at `m = 1` (gap `2` for `ĝ₀ = 1` on `{0,1}`)
concerns `nuAvg`, not `nuAvgUnits`, and is unaffected.

*Scope notes.*

- (i) and (ii) are `m`-independent, so they apply at `m = 1`
  unchanged (window `N` odd, `a`-hypothesis as in §2).
- The M1 module's `hTrU` analogue uses the `TraceM1` manual
  Gauss step rather than the general tsum Gauss step; that is
  a main-internal fact and is not a G4b concern — G4b items
  (i)–(iii) do not depend on which Gauss step produced the
  hence-form.
- No break was found: (iii) is complete. The only remaining
  `m = 1` caveat in wave 11 was "explicit values should be
  checked separately" — they now are, and they match.

## 4. What this closes, and what it does not

**G4b is now fully closed as an analytic argument:**
wave-11 duality (D) + norm class (N) + profile identity (P),
plus (i) kickValInf Fourier series, (ii) catMat = MN under
the bridge hypothesis, (iii) m = 1 bookkeeping — for all
`m ≥ 1` and all real `η`, with `ĝ = ĝ_η` continuum
coefficients. Hence G3's bound on `S` applies to the bridge's
`S` for the diagonal model kick.

**Still open (unchanged, not closed here):**

- G4c: diagonal model kick vs full fixed propagator `UN N`
  (non-diagonal Weyl quantization, l = ±1 rows,
  `τ = 10⁻⁸⁰` vs `η = O(1)`). The assembly proves
  hEquidistUnits for the diagonal model kick only until G4c
  is done or 175 is restated as a diagonal-model theorem.
- G1 (radical draft elaboration), G2 (units draft), G5
  (exact constant as a theorem) — separate items.
- Lean formalisation of all of the above: this note, like
  wave 11 task 4, is a complete analytic argument with all
  steps named, not a formalisation. A Lean version would
  still need the `chi` homomorphism computation of §1 Step 2
  (already partly in main via `chi_add`), the strip estimate,
  finite-group character orthogonality, and the SNF dual-grid
  parametrisation.

## 5. Numerical spot-checks (evidence only, not part of the proof)

Script: `numerics/wave12_task3_G4b_check.py` (uses `model.py`'s
`fCoeff(k,0)` row only; continuum `ĝ_η` by FFT on a 8192-point
grid — a numerical approximation to the continuum coefficients,
good enough for a spot-check at the 1e-6 level).

- (i) `η = 2.5`, `N = 101`, `x = 37`: truncated kick sum
  `Σ_{|k|≤60} ĝ_η(k)·e(kx/N)` vs `exp(iη·f_diag(x/N))` —
  error `2.26e-05`, dominated by FFT-grid aliasing and the
  `K = 60` truncation (a sign/convention error would leave
  an O(1) residue), not by any convention error.
- (ii) `N = 101`, `a = -inv8 mod N = 63`: Lean-formula entries
  `(1/√N)·e(a·(3x²−2xy+3y²)/N)` vs `model.py` `MN(N)` on
  200 random entries — max error `0.0` exactly.
