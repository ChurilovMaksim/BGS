# G4b: tuple ↔ orbit duality — proof attempt (analytic, not Lean)

**Status: proof attempt, not a Lean theorem. Nothing here is claimed as
proved in Lean. Repository untouched; no `lake build` run. Definitions
below were re-fetched from current main via the GitHub connector only,
pinned at HEAD `d87dce0d9277579568edfee6cffecbc96ea61024` (PR #76).
Local workspace copies in `g4/` were checked to have exactly the same
git blob SHAs as the connector fetch (see §0), so the numerical check
in §8, which imports the `g4` copy, is a check of the same content.**

This note proves item 5 of wave 10 task 3 (the heart of G4b) and the
norm-class lemma (item 4), for `m ≥ 2` and every real `η`. It does NOT
prove the other G4b items (catMat = MN, phase/gp/yp conventions,
kickValInf = exp(iη·f_diag) as a Fourier series — item 3 of wave 10),
nor G4c (diagonal model vs full fixed propagator). Where the argument
below uses a lemma from main, it says so; where it uses a new
computation, the computation is given in full.

## 0. Sources pinned at d87dce0 (connector fetch, this task)

| File | Blob SHA (git blob hash of fetched content) |
|---|---|
| `computations/verification/lineB/phase1/dlib.py` | `af79ab79ff6bb5673651afacebb496711aa2bf02` |
| `computations/verification/lineB/common/model.py` | `ee6296abf76e7a7901132e3ce704ce5baaed3800` |
| `formalization/Bgs/LineBNAverageBridge.lean` | `3373aa6b3e73363913cf2d110bb2d8edab74bfa2` |
| `formalization/Bgs/LineBDerand.lean` | `01fa6e63551542de55cce52cb9fb54c660f89b54` |
| `formalization/Bgs/LineBTsum.lean` | `dc17b0dc3ac4cb05c15f030b1520652f22602107` |
| `formalization/Bgs/LineBTraceFormula.lean` | (NmZ/Qnum/dist definitions, §2) |
| `formalization/Bgs/LineBExpand.lean` | (phiFun, kickVal, catMat) |

Definitions used, in the sources' own notation:

- **Lean tuple side** (`LineBNAverageBridge`, §3; `LineBTraceFormula`):
  `phaseTup m ν n = e(−(ν.val)·(yp m)·(NmZ m n)/(gp m))`,
  `Ztup m ĝ ν = ∑' n : Fin m → ℤ, phiFun m ĝ n · phaseTup m ν n`,
  `phiFun m ĝ n = ∏_{r : ZMod m} ĝ (n (zmodFinEquiv m r))`,
  `NmZ m n = ∑_{i,j} (n_i n_j) · pellX (dist m i j)`, `dist m i j = |i−j|`,
  `gp m = (pellX m − 1).toNat / gcd((pellX m − 1).toNat, (pellY m).toNat)`,
  `yp m = (pellY m).toNat / gcd(…)`, `Dm m = 2·(pellX m − 1)`,
  `pellX/pellY` mutual recursion `x' = 3x + 8y`, `y' = x + 3y`, `(x₀,y₀) = (1,0)`.
- **dlib orbit side** (`dlib.py`, class `Orbits(m)`):
  `Lmat = [[0,−1],[1,6]]` (multiplication by `λ = 3 + 2√2` in basis `{1,λ}`),
  `A = L^m − I`, SNF `A = P·diag(d1,d2)·Q`, `D = d1·d2 = Dm(m)`,
  `CK = {k : fCoeff(k,0), |k| ≤ 9}` (l = 0 row only),
  `f_diag(θ) = Σ_k CK[k]·e(kθ)`, `S(ξ) = Σ_{j=0}^{m−1} f_diag(θ_j(ξ))`,
  `θ_j(ξ) = ⟨L^j e1, ξ⟩`, `Φ(η) = exp(iη·S)`,
  `μ = FFT2(Φ)/D`, `cls(β) = (yp mod gp)·((A²+6AB+B²) mod gp) mod gp`
  for `(A,B) = P·(b1,b2)`, `Z_all(η)(ν) = Σ_r A_r·e(−νr/gp)`,
  `A_r = Σ_{β : cls(β)=r} μ(β)`.
- **Kick datum** (`model.py`): `fCoeff(k,0)` as in §3 below;
  `ĝ_η(k) = ∫₀¹ exp(iη·f_diag(θ))·e(−kθ) dθ` (continuum coefficients;
  dlib's `ghat()` is the FFT approximation to these, aliasing
  "superexponentially small" — the proof below uses the continuum
  coefficients, never the discrete ones).

## 1. Theorem (G4b duality + profile identity)

Fix `m ≥ 2` and `η ∈ ℝ`. Let `f_diag` be the l = 0 row (§3, proved
real-valued), and `ĝ_η` its continuum Fourier coefficients (§4).
For `n : Fin m → ℤ` write `Φ(n) = ∏_{j=0}^{m−1} ĝ_η(n_j)` and
`v(n) = Σ_j n_j·L^j e1 ∈ ℤ²`. For `β ∈ ℤ²` write `[β]` for its class
in `G := ℤ² / Aℤ²`, `A = L^m − I`, and `μ(β)` for dlib's FFT
coefficient at the SNF representative of `[β]` (§5). Then:

**(D) Duality.** `μ(β) = Σ_{n : [v(n)] = [β]} Φ(n)`, the sum being
absolutely convergent.

**(N) Norm class.** If `[v(n)] = [β]` then
`yp·NmZ(n) ≡ yp·Nm(β) [MOD gp]`, where `Nm(β) = A²+6AB+B²` for the
SNF representative `(A,B)` of `[β]`. In particular the dlib class
`cls([β]) := yp·Nm(β) mod gp` is well defined on `G`.

**(P) Profile identity.** For every `ν : ZMod (gp m)`,
`Ztup m ĝ_η ν = Z_all^{dlib}(m, η)(ν.val)` as complex numbers, hence
`Btup m ĝ_η ν = |Z_all^{dlib}(m, η)(ν.val)|²`.

The proof below is self-contained except for: (i) the Lean-side
identity `NmZ(n) = Nm(α_n)` (§2, pair identity — also in main as
`NmR`/`NmZ` material), (ii) standard finite-abelian-group character
orthogonality, (iii) standard Cauchy estimates for Fourier
coefficients of an analytic periodic function (§4).

## 2. The tuple norm is the norm of α_n

Let `λ = 3 + 2√2`, `λ̄ = 3 − 2√2`, so `λ λ̄ = 1`, `λ + λ̄ = 6`,
`λ^k = x_k + 2y_k√2` where `x_k = pellX k`, `y_k = pellY k`
(check: `λ^{k+1} = λ·λ^k = (3+2√2)(x_k + 2y_k√2)
= (3x_k + 8y_k) + (2x_k + 6y_k)√2`, matching Derand's recursion
`x' = 3x + 8y`, `y' = x + 3y` for the halved √2-coefficient).
Put `α_n = Σ_j n_j λ^j ∈ ℤ[λ] ⊂ ℤ[√2]`.

**Pair identity.** For `i, j ≥ 0`,
`λ^i λ̄^j + λ^j λ̄^i = 2·x_{|i−j|}`.
Indeed if `i ≥ j`, `λ^i λ̄^j = λ^{i−j}(λ λ̄)^j = λ^{i−j}` and
`λ^j λ̄^i = λ̄^{i−j}`, whose sum is `λ^{i−j} + λ̄^{i−j} = 2x_{i−j}`;
the case `j ≥ i` is symmetric.

Hence, with `Nm(α) = α·ᾱ`,
`Nm(α_n) = Σ_{i,j} n_i n_j · (λ^i λ̄^j + λ^j λ̄^i)/2
= Σ_{i,j} n_i n_j x_{|i−j|} = NmZ(n)`.
This is exactly Lean's `NmZ`; the Lean side's `dist` is the linear
`|i−j|`, not a cyclic distance, and the identity above is why that
is the right object. Note also: in the basis `{1,λ}`,
`α = a + bλ` has `Nm(α) = a² + 6ab + b²` (since
`(a+bλ)(a+bλ̄) = a² + ab(λ+λ̄) + b²λλ̄ = a² + 6ab + b²`),
and `L^j e1` is precisely the `{1,λ}`-coordinate vector of `λ^j`
(`L e1 = (0,1) ↔ λ`, `L² e1 = (−1,6) ↔ −1 + 6λ = λ²`, induction via
`λ² = 6λ − 1`). So `v(n)` is the `{1,λ}`-coordinate vector of `α_n`,
and `NmZ(n) = Nm(v(n))` in the `a²+6ab+b²` sense as well.

## 3. f_diag is real-valued (from the model.py formula, not assumed)

`fCoeff(k,0) = (1/2 if k = ±7) + rCoeff(k)/10
+ (rCoeff(k−1) − rCoeff(k+1))/(200i) − (1/10 if k = 0)`,
with `rCoeff` real and even: `rCoeff(−k) = rCoeff(k)`
(values: `1` at `0`, `1/2` at `±1`, `−1/2` at `±7`, `−1/4` at `±6,±8`,
else `0`). Conjugation: the first, second and fourth terms are real
and even in `k`; the third term at `−k` is
`(rCoeff(−k−1) − rCoeff(−k+1))/(200i)
= (rCoeff(k+1) − rCoeff(k−1))/(200i)`,
which is the complex conjugate of the third term at `k`
(since `conj(1/i) = −1/i`). Hence `c(0,−k) = conj(c(0,k))` for all `k`,
so `f_diag(θ) = Σ_k c(0,k)e(kθ)` is real-valued for real `θ`.
This is the only place the actual kick coefficients enter the duality
proof — and only through this conjugation symmetry, exactly as in
the G3 bound. (The l = ±1 rows play no role here; they are the G4c
problem, excluded from G4b.)

## 4. Fourier coefficients: absolute convergence (decay lemma)

Let `g_η(θ) = exp(iη·f_diag(θ))`, a 1-periodic analytic function.
`f_diag` is a trigonometric polynomial of degree `≤ 9`, so `g_η`
extends holomorphically to every strip `|Im θ| < t`, with
`|g_η(θ+it)| ≤ exp(|η|·C·e^{18π|t|})` where `C = Σ_k |c(0,k)|`
(a finite constant; `|e(k(θ+it))| = e^{−2πkt} ≤ e^{18π|t|}` for
`|k| ≤ 9`). By Cauchy's estimate on the circle `Im θ = t`,
`|ĝ_η(k)| ≤ exp(|η|·C·e^{18πt} − 2π|k|t)` for every `t > 0`.
Choosing e.g. `t = (log(2+|k|))/(36π)` gives
`|ĝ_η(k)| ≤ exp(|η|·C·√(2+|k|) − (|k|/18)·log(2+|k|))`,
which decays faster than any exponential in `|k|` (in fact
faster than `exp(−c|k|log|k|)` for large `|k|`).
Consequences used below, for every fixed `η` (constants depend on
`η`, uniformly on compact `η`-intervals):
`Σ_k |ĝ_η(k)| < ∞`, `Σ_k k²|ĝ_η(k)| < ∞` (the Bridge's summability
hypothesis), and the Fourier series `Σ_k ĝ_η(k)e(kθ)` converges
absolutely and uniformly to `g_η(θ)` (standard: analytic periodic
functions have absolutely convergent Fourier series; the estimate
above makes it explicit). In particular
`Σ_{n : Fin m → ℤ} ∏_j |ĝ_η(n_j)| = (Σ_k |ĝ_η(k)|)^m < ∞`.

## 5. The orbit side, in SNF coordinates (the pairing check)

Let `A = L^m − I = P·diag(d1,d2)·Q` (dlib's `snf2`, `d1 | d2`,
`D = d1·d2 = |det A| = Dm(m)`; the sign is irrelevant since
`det A = (λ^m−1)(λ̄^m−1) = 2 − 2x_m = −Dm`).
Dual grid: `G^ = A^{−T}ℤ²/ℤ²`, `|G^| = D`, paired with
`G = ℤ²/Aℤ²` by `⟨v, ξ⟩ mod 1` (well defined: if `ξ = A^{−T}w`,
`⟨Av', ξ⟩ = ⟨v', A^Tξ⟩ = ⟨v', w⟩ ∈ ℤ`).

**dlib's parametrisation is exactly this pairing.** dlib indexes
`ξ` by `(k1,k2) ∈ ℤ/d1 × ℤ/d2` and sets
`X = P^{−T}·(k1·(d2/d1), k2) mod d2`, `ξ = X/d2`.
Indeed `ξ = P^{−T}(k1/d1, k2/d2)`, so
`A^T ξ = Q^T·diag(d1,d2)·(k1/d1, k2/d2) = Q^T(k1,k2) ∈ ℤ²`,
so `ξ ∈ G^`; the map `(k1,k2) ↦ ξ` is injective ( `P^{−T}`
unimodular, `(k1/d1,k2/d2)` distinct mod `ℤ²`) and both sides have
`D` elements, hence it is a bijection `ℤ/d1 × ℤ/d2 ≃ G^`.
Moreover `θ_j(ξ) = ⟨L^j e1, ξ⟩`: dlib's `T[j] = ((L^T)^j X)_1`
satisfies `T[j]/d2 = ((L^T)^j ξ)_1 = e1·(L^T)^j ξ = (L^j e1)·ξ`.
The asserted `m`-periodicity `((L^T)^m X ≡ X mod d2)` is the
statement `(L^T)^m ξ ≡ ξ`, i.e. `ξ ∈ G^` is `L^m`-periodic, as it
must be since `A^T ξ ∈ ℤ²` gives `(L^T)^m ξ − ξ = A^T ξ ∈ ℤ²`.
Finally dlib's `μ`: `μ(b1,b2) = (1/D)·Σ_{k1,k2} Φ(k1,k2)
·e(−(k1b1/d1 + k2b2/d2))`, and for `β = P·(b1,b2)`,
`⟨β, ξ⟩ = (Pb)·(P^{−T}u) = b·u = b1k1/d1 + b2k2/d2 mod 1`
with `u = (k1/d1, k2/d2)`. So dlib's `μ(b)` is exactly
`μ(β) = (1/D)·Σ_{ξ∈G^} Φ(ξ)·e(−⟨β,ξ⟩)` with `β = Pb`,
and `b ↦ [Pb]` is an isomorphism `ℤ/d1 × ℤ/d2 ≃ G`
(`v ↦ P^{−1}v mod diag` is its inverse: if `v' = v + P·diag·Qw`
then `P^{−1}v' ≡ P^{−1}v mod diag`).
Two bookkeeping points, both harmless: dlib reduces `(A,B) = Pb`
mod `gp` before forming `Nm`, which does not change `Nm mod gp`
(`Nm` is a polynomial); and `μ`'s index `(b1,b2)` is a
representative of `[β]`, not `β` itself — (D) below is a statement
about classes, and §6 shows `cls` depends only on the class.

## 6. Norm class well defined mod gp (lemma (N))

Let `t = x_m − 1 > 0` (for `m ≥ 1`), `g = gcd(t, y_m)`,
`gp = t/g`, `yp = y_m/g`, so `gcd(gp, yp) = 1` and `gp | t | Dm`
(`Dm = 2t`). Let `α, γ ∈ ℤ[√2]` (the argument below needs only
`γ ∈ ℤ[λ]` for the application, but holds for all `γ ∈ ℤ[√2]`),
`δ = (λ^m − 1)γ`. Claim: `Nm(α + δ) ≡ Nm(α) [MOD gp]`.

*Step 1 — expansion.* `Nm(α+δ) = Nm(α) + Nm(δ) + Tr(α·δ̄)`,
where `Tr(z) = z + z̄ ∈ ℤ` for `z ∈ ℤ[√2]`.

*Step 2 — the norm term.* `Nm(λ^m − 1) = (λ^m−1)(λ̄^m−1) = 2 − 2x_m
= −Dm`, so `Nm(δ) = −Dm·Nm(γ)`, divisible by `Dm` hence by `gp`.

*Step 3 — the trace term.* Write `λ^m − 1 = t + 2y_m√2`
(§2: `λ^m = x_m + 2y_m√2`), `α = a + b√2`, `γ = u + v√2`
(`a,b,u,v ∈ ℤ`). Then `δ̄ = (t − 2y_m√2)(u − v√2)`,
and `Tr(α·δ̄) = 2a(tu + 4y_m v) − 4b(tv + 2y_m u)`
(expanding `(a+b√2)(p+q√2)` has trace `2ap + 4bq`;
here `p = tu + 4y_m v`, `q = −(tv + 2y_m u)`).
Modulo `gp`, `t ≡ 0` (since `gp | t`), so
`Tr(α·δ̄) ≡ −8y_m·(bu − av) [MOD gp]`.
It remains that `gp | 8y_m`. From the Derand norm
`x_m² − 8y_m² = 1` (i.e. `(x_m−1)(x_m+1) = 8y_m²`),
i.e. `t(t+2) = 8y_m²`: substituting `t = g·gp`, `y_m = g·yp`
and cancelling one factor `g` gives `gp·(g·gp + 2) = 8g·yp²`,
so `gp | 8g·yp²`; since `gcd(gp, yp) = 1`, Euclid's lemma gives
`gp | 8g`, hence `gp | 8g·yp = 8y_m`. ∎

Therefore `Nm(α + (λ^m−1)γ) ≡ Nm(α) (mod gp)`.
Application: if `[v(n)] = [β]` in `G`, then (in `{1,λ}`-coordinates)
`v(n) − β_rep = A·w` for some `w ∈ ℤ²`, i.e.
`α_n − β_rep = (λ^m − 1)·γ` for the `γ ∈ ℤ[λ]` with coordinates `w`
(`A` is exactly multiplication by `λ^m − 1` in the `{1,λ}` basis,
since `L` is multiplication by `λ`). Hence
`Nm(α_n) ≡ Nm(β_rep) (mod gp)`, i.e.
`yp·NmZ(n) ≡ yp·Nm(β) (mod gp)`. This is (N), and it shows
`cls([β])` is well defined. (Wave 10's sketch had the same
conclusion with the factor `4·gcd` in place of the `8y_m` step;
the computation above pins the factor: the trace term is
`−8y_m(bu−av) mod gp`, and `gp | 8y_m` is the sharp statement
used. Note the 2-adic content is real: e.g. at `m = 8`,
`v₂(gp) = 5`, and `gp | 8g` is what makes the odd part work;
the proof above does not assume anything about `v₂` beyond the
norm equation.)

## 7. Duality (lemma (D)) and profile identity (P)

Fix `ξ ∈ G^`. By §4, for each `j`,
`g_η(θ_j(ξ)) = Σ_{k∈ℤ} ĝ_η(k)·e(k·θ_j(ξ))` with absolute
convergence, uniformly in `ξ`. Hence
`Φ(ξ) = ∏_{j=0}^{m−1} g_η(θ_j(ξ))
= Σ_{n : Fin m → ℤ} Φ(n)·e(Σ_j n_j·θ_j(ξ))`,
the tuple sum being absolutely convergent with bound
`(Σ_k |ĝ_η(k)|)^m` independent of `ξ` (finite product of
absolutely convergent series; Weierstrass M-test).
Now `Σ_j n_j·θ_j(ξ) = Σ_j n_j⟨L^j e1, ξ⟩
= ⟨Σ_j n_j L^j e1, ξ⟩ = ⟨v(n), ξ⟩ mod 1`, by linearity of the
pairing. Therefore, interchanging the finite `ξ`-sum with the
absolutely convergent tuple sum (dominated by
`(Σ|ĝ_η|)^m`, independent of `ξ`),
```
μ(β) = (1/D)·Σ_{ξ∈G^} Φ(ξ)·e(−⟨β,ξ⟩)
     = Σ_n Φ(n)·(1/D)·Σ_{ξ∈G^} e(⟨v(n)−β, ξ⟩).
```
**Orthogonality.** As `ξ` runs over `G^`, `ξ ↦ e(⟨·, ξ⟩)` runs
over all characters of the finite abelian group `G`:
if `⟨v, ξ⟩ ∈ ℤ` for all `v ∈ ℤ²` then `ξ ∈ ℤ²`, i.e. `ξ = 0`
in `G^`; and `|G^| = D = |G|`. Hence the inner average is `1`
if `v(n) − β ∈ Aℤ²` (i.e. `[v(n)] = [β]`) and `0` otherwise
(standard: a nontrivial character sums to `0` over the group,
by translation invariance). This is exactly the orthogonality
formula in the task statement, and it gives (D):
`μ(β) = Σ_{n : [v(n)]=[β]} Φ(n)`.

**Grouping.** Define tuple class sums
`A_r^tup = Σ_{n : yp·NmZ(n) ≡ r (mod gp)} Φ(n)`
(`r ∈ ℤ/gp`; the partition of `ℤ^m` by `yp·NmZ mod gp` is finite,
each subseries absolutely convergent, so grouping is legitimate).
By (D), summing over classes `c ∈ G` with `cls(c) = r`:
`A_r^{dlib} = Σ_{c : cls(c)=r} μ(β_c)
= Σ_{c : cls(c)=r} Σ_{n : [v(n)]=c} Φ(n)
= Σ_{n : cls([v(n)])=r} Φ(n)`,
and by (N), `cls([v(n)]) = yp·NmZ(n) mod gp`. Hence
`A_r^tup = A_r^{dlib}` for every `r`.

**Fourier inversion over ℤ/gp.** Lean's phase depends only on
`r = yp·NmZ(n) mod gp`: if `yp·NmZ(n) = r + gp·t` then
`e(−ν.val·(yp·NmZ(n))/gp) = e(−ν.val·r/gp)·e(−ν.val·t)
= e(−ν.val·r/gp)` (since `ν.val·t ∈ ℤ`). Grouping the absolutely
convergent tuple sum by `r`:
`Ztup m ĝ_η ν = Σ_r A_r^tup·e(−ν.val·r/gp)`.
dlib's definition is `Z_all(ν) = Σ_r A_r^{dlib}·e(−ν·r/gp)`
(`ν ∈ {0,…,gp−1}` = `ν.val`). With `A_r^tup = A_r^{dlib}`,
`Ztup = Z_all` for every `ν`, and taking `‖·‖²` gives (P):
`Btup m ĝ_η ν = |Z_all^{dlib}(m, η)(ν.val)|²`.
In particular `nuAvgUnits(Btup m ĝ_η) = F_m(η)` (both are the
units mean of the same profile), so G3's bound on
`S = Σ_{ν∈units} Btup(ν) = φ(gp)·F_m(η)` applies to the bridge's
`S` — once G4's remaining items (below) are in place.

## 8. Numerical check (supporting evidence, not part of the proof)

Independent check of (D) at `m = 3`, `η = 1`, per SNF class
`β ∈ ℤ/7 × ℤ/28` (`D = 196`, `gp = 14`, `yp = 5`): dlib's
`μ = FFT2(Φ)/D` against the truncated tuple sum
`Σ_{n ∈ [−K,K]³, [v(n)]=[β]} ∏ ĝ_η(n_j)` with `ĝ_η` from
dlib's `ghat()` (FFT 4096) and `v(n)` via `L^j e1 =
(1,0), (0,1), (−1,6)` and class map `v ↦ P^{−1}v mod (7,28)`:

| K | max over β of \|tuple − dlib μ(β)\| |
|---|---|
| 8 | 0.319 |
| 12 | 0.319 |
| 16 | 0.0463 |
| 20 | 0.0463 |
| 24 | 0.00667 |
| 32 | 0.000480 |
| 40 | 0.0000471 |

The slow start is real, not a convention error: `ĝ_η` has
coefficients up to `0.095` in `13 ≤ |k| ≤ 20` (degree-9 tones
combine) and `0.015` in `21 ≤ |k| ≤ 40`, so truncation at
`K ≤ 20` genuinely leaves a `~0.05` residue; the residue then
falls steadily with `K`, as the proof predicts. Total sums
also converge: truncated tuple total at `K = 40` is
`−0.904085 + 0.427408i` vs dlib `−0.904072 + 0.427380i`.
This check confirms the SNF pairing and class map of §5
(`P^{−1}v mod diag`, FFT sign) — a sign or transpose error
there would have left a fixed, non-vanishing residue instead
of convergence to `0`.

## 9. What remains for G4b, and what this note does NOT do

- **Closed by this note:** duality (D), norm class (N), profile
  identity (P) for the tuple-vs-orbit comparison, for `m ≥ 2`,
  all real `η` (fixed `η`; uniform on compact `η`-intervals by
  the §4 estimates with `η`-dependent constants).
- **Not closed (wave 10 items 1–3, 6–7):** catMat = MN (index
  transport only); phase/sign/gp/yp conventions (already
  verbatim-matching, §0/§7); kickValInf = exp(iη·f_diag(·/N))
  as a Fourier series — note this is a *separate* statement
  from (D): (D) uses `ĝ_η` as continuum coefficients, while
  kickValInf is the tsum `Σ'_k ĝ_η(k)·χ_N(kx)`; its identification
  with `exp(iη·f_diag(x/N))` needs the uniform-convergence
  argument of §4 evaluated at `x/N` plus the `χ_N` bookkeeping,
  and must not be confused with (D); aliasing bookkeeping if
  anyone substitutes discrete N-grid coefficients (avoided here
  by using continuum `ĝ_η`); m = 1 bookkeeping (the argument
  above does not use `m ≥ 2` anywhere except in the G4 statement
  itself — at `m = 1` it gives the same duality with `gp = 2`,
  `D = 4`, but the M1 module's explicit values should still be
  checked separately before claiming m = 1).
- **Explicitly excluded:** G4c — the diagonal model kick (2) vs
  the full fixed propagator `UN N` (non-diagonal Weyl
  quantization, l = ±1 rows, `τ = 10⁻⁸⁰` vs `η = O(1)`).
  Nothing in (D)/(N)/(P) identifies (2) with (3); the assembly
  proves hEquidistUnits for the diagonal model kick only, until
  G4c is done or 175 is restated as a diagonal-model theorem.
- **Lean gap:** this is an analytic proof sketch in the sense of
  a complete mathematical argument with all steps named, but it
  is NOT formalised: a Lean version would need the finite-group
  character orthogonality over `ℤ²/Aℤ²`, the SNF parametrisation
  of `G^`, the strip estimate for `ĝ_η`, and the tuple-sum
  rearrangements, none of which are in main for this statement.

## 10. Possible breaks — checked and found sound

1. *Sign of the pairing / FFT convention.* dlib's `μ = FFT2(Φ)/D`
   uses `e(−(k1b1/d1 + k2b2/d2))`; §5 shows this equals
   `e(−⟨β,ξ⟩)` for `β = Pb`, `ξ = P^{−T}(k1/d1,k2/d2)` — no
   sign error, because `⟨Pb, P^{−T}u⟩ = b·u` exactly.
2. *`{1,λ}` vs `{1,√2}` bases.* `Z[λ]` is the index-2 subring of
   `ℤ[√2]` with even √2-coefficient; `α_n` and all `β`
   representatives lie in `Z[λ]`, and the norm formula
   `a²+6ab+b²` on `{1,λ}`-coordinates agrees with
   `NmZ` on `ℤ[√2]`-coordinates (§2). The norm-class proof
   (§6) works for arbitrary `γ ∈ ℤ[√2]`, so no subring issue
   arises at the application point.
3. *`gp | 8y_m` vs the wave-10 `4·gcd` sketch.* The trace
   computation gives `−8y_m(bu−av) mod gp`, not `4·gcd`;
   `gp | 8y_m` follows from `t(t+2) = 8y_m²` + `gcd(gp,yp) = 1`
   (§6, Step 3). The wave-10 sketch's factor was not sharp;
   this note replaces it with the exact computation.
4. *Truncation vs exactness.* dlib's `S(ξ)` is exact: `θ_j(ξ)`
   are multiples of `1/d2` and `f_diag` is evaluated as a
   trigonometric polynomial at those points, not approximated.
   The only approximations anywhere near this proof are
   dlib's `ghat()` FFT (not used in the proof) and the §8
   numerical check (truncated tuple sums, not the proof).
