# N12 adapted norm — reusable artefact (gap (a) δ_int, gap (b) D1/D2)
Built 2026-10-31 (UTC+5) by Line N12. Labels: [CA-float] = rigorous modulo IEEE-754 rounding bounds stated in the script; [N] = numerics.

## Object
- Operator: sector-4 Line F/N6 Galerkin core operator A(t) = Σ_n w_4(n) e(n t) M_n (dim 495), `code/a_ops.py` (cache `logs/a_ops.npz`,
  built from N6 `cert_core` arb blocks; max entry radius RAD, D·RAD = 4.0e-17; Galerkin→true perturbation Pert = 1.90e-9 [CA, n_cert]).
- Slow twists: w_a(n) = w_4(n)·e(n(a−4)/8), so sector a at twist τ equals A(τ + (a−4)/8). The full Z is slow at b ∈ {0,¼,½,¾}
  through sector a_b = 4 − 8b (mod 8), i.e. **all four slow fixed twists use the same operator A0 = A(0)** — one norm serves all.
  (Inside sector 4, A(¼) has radius 0.877, A(½) 0.574: not slow.)
- Dominant eigenpair: s = 1.35724 − 1.35164i (|s| = 1.91546), Φ, ψ (ψΦ = 1), residuals ≤ 7e-15. Next |eigenvalue|/|s| = 0.380.

## Norm (`code/f_adapted.py kap omega tau0`, default kap = 0.45, omega = 1)
‖v‖_H² = v*Hv,  H = ω ψ̄ψᵀ + Q̃*PQ̃,  Q̃ = I − Φψᵀ,  P = Σ_j kap^{−2j}(Bʲ)*Bʲ  (Stein), B = Q̃A0Q̃/s.  ‖v‖_H = ‖Tv‖₂ (T = Cholesky factor, saved).
File: `logs/adapted_norm_t0.0_k0.45.npz` (T, H, P, Phi, psi, s, kap, omega, Qt) + `.json` (constants).

## Certified properties (`adapted/verify_adapted.py`, ALL_OK, η = 1e-8) [CA-float]
| | statement | value |
|---|---|---|
| V1 | c_lo‖v‖₂ ≤ ‖v‖_H ≤ c_hi‖v‖₂ | c_lo = 0.7208, c_hi = 15.18, **cond = 21.06** |
| V2 | ‖A0/s‖_H ≤ 1+η | margin 2.0e-8 vs float err 3.1e-10 |
| V3 | ‖Q̃‖_H ≤ 1+η, ‖(A0/s)Q̃‖_H ≤ kap(1+η) | **off-dominant contraction 0.45 in ONE step, constant 1** (margin 0.10 vs 5e-11) |
| V4 | Galerkin→true additive error in H-norm, relative to |s| | 2.1e-8 |
| Lip | ‖(A(t)−A(0))/s‖_H ≤ Lip_H·|t| | **Lip_H = 167.2** (2-norm analogue 484; old Cpow·2πN₁/|μ| ≈ 6e6) |
Numerical (not certified) power profile: ‖(A0/s)ⁿQ̃‖_H/0.45ⁿ = 0.998, 0.950, 0.817, …, 0.177 (n = 12); i.e. true rate 0.38.

## Per-stay bound D2 (replaces Cpow·exp(Cpow·2πN₁Σδ/μ*)) [P given V1–V4]
For a stay of length ℓ at a slow twist b with offsets δ_i = |τ_i − b|, write L_i/s = M + E_i, M = A0/s, ‖E_i‖_H ≤ e_i := min(Lip_H δ_i, N_H(δ_i)+1). Then
- ‖∏L_i/s‖₂ ≤ cond·∏_i N_H(δ_i)·(1+3e-8)^ℓ ≤ 21.06·exp(167.2·Σδ_i)·(1+3e-8)^ℓ;
- gap splitting ∏(M+E_i) = Π + MˡQ̃ + R, ‖MˡQ̃‖_H ≤ 0.45ˡ, ‖R‖_H ≤ ∏(1+e_i) − 1;  (one-step contraction ⇒ no transient constant).
- N_H(t) = ‖A(t)/s‖_H tabulated by `adapted/stepnorm_table.py` (grid 1/4096, cell add-on Lip_H/8192 = 0.0204).
  Spot values: N_H(1/8) = 2.84, N_H(1/4) = 2.18, N_H(3/8) = 1.44, N_H(1/2) = 1.47.

## Reuse
`python code/f_adapted.py 0.45 1.0 0.0 && python adapted/verify_adapted.py && python adapted/stepnorm_table.py 4096`
(venv /workspace/bgs-lineN/.venv; ~1 min + ~10 s + ~15 min on 1 core). Other kap: smaller kap (≥0.39) → larger cond; kap 0.45 is a compromise.
For D1 cone fields: use T to map to Euclidean coordinates (ṽ = Tv); all step maps become T A(t) T⁻¹/s with ‖·‖₂ = N_H(t).

## Quadratic step bound near the slow twist (`adapted/quad_stepbound.py`, logs/quad_stepbound.json) [CA-float form, P-sketch argument]
ψᵀE₁Φ = 1e-16 (|μ(t)| stationary at t = 0), so the first-order term vanishes. With v = aΦ + q (H-orthogonal), E₁ = A′(0)/s,
b₁ = ‖Q̃E₁Φ‖_H = 32.71, c₁ = ‖ψᵀE₁Q̃‖_{H*} = 1.391, b₂ = ‖Q̃E₁Q̃‖_H = 12.49, L₂ = (2π)²Σn²|w_n|‖M_n‖_H/|s| = 4977:
  N_H(t) ≤ σ_max[[√(1+t²|ε₀|²), t c₁],[t b₁, 0.45 + t b₂]] + L₂t²/2  ⇒  **N_H(t) ≤ 1 + 3.19e3·t²** for |t| ≤ 1/256 (measured: 1 + 602t²).
**D2 consequence:** a stay with offsets δ_i costs ‖∏L_i/s‖₂ ≤ 21.06·∏_i min(1 + 3.19e3δ_i², N_H-table(δ_i) + 0.0204).
For geometric offsets δ_k = θλ^{−k} (θ = 1/16) the product is ≈ 2.3 per stay end ⇒ K_stay = O(10²), replacing Cpow·exp(Cpow·2πN₁Σδ/μ*).
