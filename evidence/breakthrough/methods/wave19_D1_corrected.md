# Wave 19, task 2 — Corrected D1 derivation: pair sum = fiber term − cancellation term

## 0. Status

This replaces the D1a/D1b chain of the 152 route-(b) assembly
(wave 13, task 4), which wave 17–18 refuted at m = 12 in both steps.
Nothing here is a Lean theorem; repository untouched, no Lean build.
Sources: wave 16 (split fiber on support, φ̂ phases),
wave 17 task 1 (Bsym_Γ at m = 12, D1a/D1b failure),
wave 18 task 1 (exact Bsym_w, Bsym_fiber, R at m = 12),
wave 18 task 2 (P_w census at m = 12).

## 1. Setup

Let N = |supp|, averages over supp. On supp, φ̂ satisfies the
modulus dichotomy |φ̂|² = 16/D (validated exactly at m = 12,
error ≤ 7×10⁻²³ on split points) and φ̂ is constant on Γ-orbits
(reindexing argument; numerically 2×10⁻¹⁹ at m = 12).
The pair sum's surviving term (ω = 1 inside fibers, wave 7) is

  R = Σ_F |Σ_{ξ∈F} φ̂|² / Σ_ξ |φ̂|²,

the sum over fibers F. Assume supp is a union of fibers
(evidence: exhaustive to m = 10, wave 15; all lifts FULL/EMPTY,
wave 16), so F ∩ supp = F and the denominator is N·16/D.

## 2. The decomposition (exact, per fiber)

For a fiber F with Γ-orbits O₁,…,O_k, write φ̂ ≡ φ_j on O_j,
|φ_j|² = 16/D, θ_j = arg φ_j. Then

  |Σ_{ξ∈F} φ̂|² = (16/D)·|Σ_j |O_j|·e^{iθ_j}|².

If F is unsplit (k = 1), this is |F|²·16/D: the fiber term.
In general, define the per-fiber deficit

  Δ_F = |F|² − |Σ_j |O_j|·e^{iθ_j}|²
      = 2·Σ_{j<k} |O_j||O_k|·(1 − cos(θ_j − θ_k)) ≥ 0,

using |Σ a_j e^{iθ_j}|² = Σ a_j² + 2Σ_{j<k} a_j a_k cos(θ_j−θ_k).
Δ_F = 0 iff all orbit phases on F agree mod 2π. Summing over fibers:

  **R = Bsym_fiber − Δ,   Δ = (1/N)·Σ_{split F} Δ_F,**
  Bsym_fiber = (1/N)·Σ_F |F|².

This is the corrected D1a. The old D1a (R = Bsym_fiber) is the
special case Δ = 0; the old D1b (Bsym_fiber = Bsym_w) is a
separate, also false, identification — Bsym_w never appears in
this derivation, and no step equates R with Bsym_w.

## 3. Verification at m = 12 (exact)

N = 96,049,800 = D/16. Split fibers in support: 762, mass
35,952 points, Σ|F|² = 1,713,888, coherent total
Σ|Σ_j |O_j|e^{iθ_j}|² = 1,695,744 (integer, s-independent),
so ΣΔ_F = 18,144 and Δ = 18,144/N = 0.000189.

| quantity | exact | float |
|---|---|---|
| Bsym_Γ | 383766967/16008300 | 23.97299944 |
| Bsym_w | 383795287/16008300 | 23.97476853 |
| R | 383907271/16008300 | 23.98176390 |
| Bsym_fiber | 76782059/3201660 | 23.98195280 |

Check: 23.98195280 − 0.000189 = 23.98176390 = R. ✓
Ordering: Bsym_Γ < Bsym_w < R < Bsym_fiber; R − Bsym_w = 0.0070.
Spot check on the wave-16 fiber: 3 orbits of 12, phases 120°
apart: Δ_F = 2·3·144·(1 − cos 120°) = 1296 = |F|², coherent 0. ✓
Only 5 of the 762 split fibers fully cancel (sizes 72, 36, 72,
72, 36); the rest are nearly aligned — deficit is 1.06% of the
split aligned total, hence R sits just 0.00019 below Bsym_fiber.
R is identical at s = 1 and s = 13 (per fiber to 1.7×10⁻¹¹).

## 4. Verification at m = 8 (deficit 0)

All 39 split fibers are off-support, so no split fiber meets
supp, Δ = 0, and R = Bsym_fiber. On support, fibers = orbits
(no split) and (fiber,w)-classes = orbits (P_w holds on support
at m = 8), so Bsym_fiber = Bsym_w = Bsym_Γ = 318335/20808
≈ 15.298683199, reproducing the wave-14 D1a aggregate identity
(to 4×10⁻¹⁴). The old chain is therefore correct at m = 8 and
fails exactly where split fibers enter support.

## 5. The corrected limit reading (B2′)

The pair sum tracks R, not Bsym_w and not Bsym_fiber:
limit value (if the limit exists) = lim (Bsym_fiber − Δ).
At m = 12 this is 23.98176390, not 23.97476853 (Bsym_w) and not
23.98195280 (Bsym_fiber). Any future 152 derivation must
carry Δ explicitly: it is a sum over split fibers in support
of orbit-size products times phase-misalignment factors
(1 − cos(θ_j − θ_k)) — phase data, not combinatorics.

## 6. What remains unproved for (B2′) — precise list

1. **Supp is a union of fibers, in general.** Only verified to
   m = 10 and on lifts (FULL/EMPTY); needed for F ∩ supp = F.
2. **φ̂ constant on Γ-orbits, in general.** Reindexing argument
   sketched, numerically 2×10⁻¹⁹ at m = 12; needs a proof.
3. **Modulus dichotomy |φ̂|² = 16/D on support, in general.**
   Validated numerically at m = 8, 12; needs a proof.
4. **Control of Δ in the limit — the hard item.** No theorem
   that Δ → 0, that Δ has a limit, or that split-fiber phases
   are anything but arbitrary: Δ/N at m = 12 is 0.00019
   (small but nonzero), and its m → ∞ behaviour is open.
   The s-independence of R (checked at s = 1, 13 only) also
   needs a general explanation.
5. **D1c unchanged:** the passage from finite-m R to the
   strong-kick limit (limit over residues) is still open.
6. **G4c unchanged:** transfer from the diagonal model kick to
   the full fixed propagator is still open; without it (B2′)
   is a statement about the diagonal model only.
7. **152-full remainder unchanged:** hSepC, J0 ensemble, N-step
   hN for true Psi_m, finite-vs-torus Fix identification,
   symmetry of c, support-independence of s.
8. **P_w is dead as a separator:** it fails on support at
   m = 12 (152 failing fibers, all gluing splits, wave 18
   task 2); Bsym_w is not the limit value at any m where
   split fibers meet support with misaligned phases.
9. **Lean formalisation** of the whole corrected chain, with
   sorryAx = 0 and re-verification against the then-current
   main HEAD.

## 7. Files

- This note: wave19_D1_corrected.md
- Inputs: wave18_bsymw_m12.md, wave18_Pw_m12_census.md,
  wave17_d1a_m12.md, wave16_d1a_targeted.md, wave13_152_assembly.md
