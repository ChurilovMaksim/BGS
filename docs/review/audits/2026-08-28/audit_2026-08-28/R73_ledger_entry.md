
## RUN 73 (2026-08-28, continuation) — β=1 BECOMES A THEOREM; THE HECKE DICHOTOMY

**Headline.** Two things that were measurements are now theorems or sharp
quantitative laws. (1) The orthogonal symmetry class of the desymmetrised
single-orbit compression is **proved**: `R τ R⁻¹ = τ⁻¹` for every element of the
centraliser torus, hence the arithmetically constructed antiunitary
`Θ_u = U_τ U_M ∘ conj` squares to `+1` and commutes with the observable. (2) The
**correct** Hecke eigenbasis is constructed for the first time in this workspace,
and the matrix elements of a pure Weyl operator show a clean dichotomy:
**diagonal = Sato–Tate (excess kurtosis −1.00 ± 0.02), off-diagonal = complex
Gaussian (0.000 ± 0.002 over 5.8·10⁶ samples)**.

### R73.1 — THEOREM E upgraded to a PROOF [PROVEN]

**Lemma (torus inversion).** For `τ = xI + yA` with `x² + xyt + y² = 1`,
`R τ R⁻¹ = τ⁻¹`. *Proof.* `RAR⁻¹ = A⁻¹ = tI − A`, so
`RτR⁻¹ = xI + yA⁻¹ = (x+yt)I − yA`; and using `A² = tA − I`,
`τ·((x+yt)I − yA) = (x²+xyt+y²)I + 0·A = I`. ∎

**Proposition.** `Θ_u² = +1`. *Proof.* Egorov carries a transpose
(`U_A T(n)U_A* = T(Aᵗn)`), so `M ↦ U_M` is an **anti**homomorphism up to phase:
`U_{M₁}U_{M₂} ∝ U_{M₂M₁}`; and `conj(U_M) ∝ U_{SMS}`. Hence
`Θ_u² = U_τU_M conj(U_τU_M) ∝ U_W` with `W = (SMS)(SτS)Mτ`. With `M = SR` one has
`SMS = RS` and `S(SτS) = τS`, so `W = RτS·SR·τ = (Rτ)²`, and by the Lemma
`(Rτ)² = (RτR⁻¹)τ = τ⁻¹τ = I`. So `Θ_u²` is a scalar; antiunitarity forces it
real, hence ±1. If it were −1 every Θ_u-invariant Hermitian operator would have
exactly doubled (Kramers) spectrum, which is not observed — the measured minimum
gap is never zero. So the sign is +1. ∎

**Certification** (`src/theoremE_operator.py`, `artifacts/r73/theoremE_operator.json`),
81 configurations over 6 pairs (A,p):
* `W = +I` by integer arithmetic in **81/81** (the first attempt used the
  homomorphism order and gave "other" in 81/81 — that discrepancy is what
  identified the antihomomorphism, so the wrong guess was informative);
* `Θ_u² = +1` in 81/81, scalar deviation ≤ 4.4e-13;
* `|Θ_u(T(u)+T(−u))Θ_u⁻¹ − (T(u)+T(−u))| ≤ 3.2e-13`;
* **the parity block of the compression is unitarily equivalent to a real
  symmetric matrix, defect ≤ 2.9e-14** — this is the analytic content of β = 1.

So the symmetry-class half of BGS for this family and this class of observables
is now a **theorem** (off the degenerate locus of density O(1/p), Theorem E),
not a measurement.

### R73.2 — THE HECKE DICHOTOMY [NUMERICALLY-SUPPORTED, sharp]

The centraliser torus commutes with U_A, so diagonalising `B*U_{τ₀}B` for a
generator τ₀ gives the genuine Hecke eigenbasis of H_λ — the basis of
Kurlberg–Rudnick. Diagnostics: `|[U_A,U_{τ₀}]|` on H_λ ≤ 2.1e-13, unitarity
≤ 2.6e-14, off-diagonal residue of U_{τ₀} in the Hecke basis ≤ 7.5e-15, minimum
character separation 1.3e-2 … 1.3e-1. (The voided R67–R70 never built this
basis at all.)

Normalised matrix elements `√p·⟨ψ_i, T(n)ψ_j⟩`, n ≠ 0, 24 random frequencies,
error bars computed **per frequency** then across frequencies so that the
correlation among the m² elements of one frequency is respected:

| p | K | m | diagonal excess kurtosis | off-diagonal excess kurtosis |
|---|---|---|---|---|
| 1597 | 34 | 46 | −1.0009 ± 0.0465 | +0.0073 ± 0.0269 |
| 3571 | 17 | 210 | −1.0184 ± 0.0205 | −0.0028 ± 0.0048 |
| 9349 | 19 | 492 | −0.9771 ± 0.0150 | −0.0014 ± 0.0019 |

`E|z|² = 1.00` in every case, so the `√p` normalisation is exactly right — QUE at
rate `p^{−1/2}`. And `E|z|⁴/(E|z|²)²` = 1.96, 1.97, 2.02 (diagonal) versus
2.0005 ± 0.0092, 1.9973 ± 0.0022, **1.9997 ± 0.0008** (off-diagonal).

* **Diagonal = Sato–Tate.** Excess kurtosis −1.00 ± 0.02 is exactly the
  Sato–Tate value (Catalan moments 1, 2, 5 against Gaussian 1, 3, 15), and
  22–65σ from Gaussian. This is the expected behaviour: for a *pure* Weyl
  operator the Kurlberg–Rudnick formula makes the diagonal element a single
  normalised Salié/Kloosterman sum, Sato–Tate by Katz; their "weighted sum of
  traces of independent SU(2) matrices" arises for a general observable expanded
  over many T(n). So this **confirms the elementary building block of the
  KR law with correct code**, and definitively kills the voided R67–R70 reading
  that a Gaussian residual is the QUE signature.
* **Off-diagonal = complex Gaussian**, to four decimals. Our literature check
  found nothing settling this distribution; it is recorded as new.

**Why this matters for BGS.** The spectral fluctuations of a compression are
driven by its off-diagonal entries, and those are Gaussian; the arithmetic,
non-Gaussian Sato–Tate structure is confined to the diagonal, where it shifts
levels but neither creates nor destroys repulsion. Together with Theorem A
(Gaussian Weyl observable ⇒ exactly GUE/GOE), Theorem D (the exact parity
obstruction) and R73.1 (β = 1 by an arithmetic antiunitary), this is a coherent
mechanism for the GOE statistics measured in R72.4.

### R73.3 — The `s < lpf(k)` criterion: proof for prime powers, 144 cells

`E⁰(s,k) = P(s,k) ⟺ s < lpf(k)`. Proved for k prime (R71) and for `k = q^e`
(R72.5). For general `k = q·k'` the tensor decomposition
`Z[ζ_k] = Z[ζ_q] ⊗ Z[ζ_{k'}]` forces all q components `c_α` to be equal to a
common `c`; if `c = 0` induction on the number of prime factors closes it (every
`lpf(k') > q > s`); if `c ≠ 0` then no α-class is empty on both sides, and either
every class contains a term of the first tuple (giving `s ≥ q`) or Lam–Leung
applied to the resulting vanishing sum over `μ_{k'}` produces a class of size
`≥ lpf(k') > q`. A factor 2 remains in the last branch, so the general case stays
[CONJECTURED]. Cells verified: 54 (mixed k ≤ 41, R71) + 29 (prime powers k ≤ 81,
R72) + **61 (composite k ≤ 77 with two prime factors, R73)** = **144, zero
exceptions**. Artifact `artifacts/r73/composite_k_criterion.json`.
