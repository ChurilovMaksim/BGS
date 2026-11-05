# Wave 17, task 1 — D1a consequences at m=12

## Verdict

- **Bsym_Γ(supp) at m=12, exact: 383766967/16008300 ≈ 23.973** (new;
  vs 15.299 at m=8). Method below.
- The phase cancellation does **not** break **(B1)**: (B1) is
  combinatorial and φ̂-free. On the exhibited fiber,
  (fiber,w)-classes = orbits (sorted(w) distinct across its 3
  orbits), so it contributes 432 to both numerators. In general
  Bsym_w ≥ Bsym_Γ, with equality ⟺ P_w on support — still open at
  m=12 (gluing-split census gap, see below). So (B1) is unbroken
  wherever checked, unproven in full.
- The cancellation **does** break **(B2)**, at both D1 steps, on this
  single fiber: pair-sum term 0 ≠ fiber average 1296 ≠ w-average 432
  (contributions in Bsym units, i.e. divided by |supp|).
- **O′ is FALSE at m=12 (new).** O′ = "no split fiber meets supp".
  The wave-16 fiber is split (3 orbits) and fully in support.
  Wave 5's survival of O′ at m=12 only meant the killer pair was
  off-support; this fiber kills it.
- Cancellation is systematic in s, not an s=1 accident: |Σφ̂|² ≈ 10⁻³⁵
  (≈ 0) at s = 1, 13, 17, 19, 23, 29, 31, 37 (all coprime to D),
  vs the fiber-constant prediction 1.349×10⁻⁵.

## Numbers

- |supp| = 96,049,800 = D/16 (product of component supports:
  8·81·25·49·121; agrees with D/|V4|).
- Σ_{y∈supp} |Γy| = 2,302,601,802, hence Bsym_Γ =
  383766967/16008300 ≈ 23.973. Computation: global orbit size =
  24/|∩ component stabilizers| (CRT), aggregated over component
  stabilizer types (2/17/7/5/13 distinct supported stabilizers at
  q = 128/81/25/49/121). Sanity: 24 − 23.973 = 0.027, i.e. almost all
  supported points have trivial stabilizer (orbit 24).
- Wave-16 fiber: 36 points, 3 orbits of 12, 36/36 in support.
  Per orbit exactly one sorted(w), pairwise distinct across orbits
  → classes = orbits here. Mechanism of the lift: the fixed
  other-component points are D₁₂-invariant (stabilizer 24, i.e.
  constant vectors), except q=128's (stabilizer 12).
- Coherent vs incoherent on the fiber: |Σφ̂|² ≈ 1.1×10⁻³⁵ vs
  |F|²·16/D = 1.349×10⁻⁵; Σ|φ̂|² = 3.748×10⁻⁷ = 36·16/D.

## Why D1a and D1b fail at m=12

Let R = Σ_F |Σ_{ξ∈F} φ̂|² / Σ_ξ |φ̂|², the pair sum's surviving
term (ω = 1 inside fibers, wave 7). By the triangle inequality,
|Σ_{ξ∈F} φ̂|² ≤ |F|²·16/D for F ⊆ supp, so R ≤ Bsym_fiber always,
with **strict** inequality at m=12: the wave-16 fiber gives 0
instead of 1296·16/D, a deficit of 1296/|supp| ≈ 1.35×10⁻⁵.
Hence the D1a aggregate identity R = Bsym_fiber is false at m=12.
D1b (Bsym_fiber = Bsym_w on support) fails on the same fiber:
1296 vs 432, a gap of 864/|supp| ≈ 9.0×10⁻⁶. Globally at m=12:
Bsym_Γ ≤ Bsym_w < Bsym_fiber, both inequalities strict in the
second place (and the first is strict unless P_w holds on support).

## No rescue term inside the pair-sum framework

The orbit-sum term Σ_O |Σ_{ξ∈O} φ̂|² / Σ|φ̂|² equals Bsym_Γ
exactly (φ̂ is constant on orbits), but the pair sum cannot
produce it: ω is a function of mode sums, hence constant on
fibers (wave-7 ω-blindness), so cross-orbit pairs inside a fiber
survive into the pair sum and cancel. (B2) would need a new
derivation that accounts for within-fiber cancellation — e.g. a
theorem that split fibers in support always cancel fully, plus a
recomputation of R (not Bsym_w) as the limit value. Route (b)'s
claimed limit value Bsym_w is wrong at m=12 in D1a/D1b form.

## Open gaps (unchanged by this task)

- Full census of split fibers in support at m=12 (gluing splits
  beyond the (128,25) pairing unsearched); exact Bsym_w(supp)
  at m=12; P_w on support at m=12.
- No partial fiber is involved anywhere: all lifts are FULL/EMPTY.

## Files

- Script: [wave17_d1a_m12.py](wave17_d1a_m12.py)
- Numbers: `wave17_d1a_m12_result.json` (not in repository)
- Inputs: wave16_d1a_targeted.py, wave16_d1a_m12_phi.py (CRT machinery).
- Repository untouched; no Lean build.
