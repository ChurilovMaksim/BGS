# Transfer of the Laplace functional and fixed Δ_k to the phase model

Scope: exactly the repo-model reading of the §16 re-base. The literal §16
model of the external document is NOT claimed here: its identification with
the repo model is pending gap R1 (written dictionary incl. explicit P₂/P₃
matching). TRACE-005 and BGS-001 remain OPEN: this note proves a reduction,
not a local law. For the external document's verification status, see the
repo record note `record/external_trace005_auxiliary_20261024.md`.


Let N be odd, τ = 10⁻⁸⁰ fixed, U_N = e^{iτNA_N}M_N as in the fixed-map
formulation. Let F_N^{(J)} be the repo order-J parametrix
(`mathematics/fixed-map/four_branch_parametrix.md` §2 for J = 1;
`mathematics/fixed-map/factorial_wkb_reduction.md` (BGS-TRACE-017) §6 for
general J), with

‖U_N(t) − F_N^{(J)}(t)‖_op ≤ C_J h^{J+1/2},  h = 1/N,

and let V_N^{(J)} be its polar unitarisation (unitary, ‖U_N − V_N^{(J)}‖ ≤
2‖U_N − F_N^{(J)}‖ for large odd N). Notation: the repo notes denote the
approximant itself by V_N; here F_N^{(J)} is that approximant and V_N^{(J)}
its polar unitarisation. The four branches, Hamilton–Jacobi phases
and gluing identities are those of `four_branch_parametrix.md` §2.

## Theorem A (Laplace functional)

For every fixed f ≥ 0 ∈ C_c¹, the full Laplace functional of U_N is transferred
to the single model V_N^{(1)} with error O_f(N⁻¹ᐟ²):

|L_N^{U}(f) − L_N^{V^{(1)}}(f)| = O_f(N⁻¹ᐟ²) → 0,

where L_N(f) = ∫₀¹ exp(−Σⱼ f_N(θⱼ − α)) dα with a single common shift
(recovered from the Lemma 6 proof of the external §16), and f_N(t) =
Σ_ℓ f(N(t+ℓ)) is the N-rescaled test function. The constant depends
on f only through ‖f′‖₁ (and the model constant in the parametrix error).
The same V⁽¹⁾ works for every fixed f. Proof: two-amplitude parametrix
(O_op(h^{3/2})) + polar doubling + the eigenangle-matching lemma (§16 Lemma 6,
(16.1)): (N/π)·arcsin(ε_N/2)·‖f′‖₁ with ε_N = O(N⁻³ᐟ²).

## Theorem B (fixed-k Δ_k)

Fix k ≥ 2 and admissible b (Schwartz, ≥ 0, sup < 1). For any fixed R ≥ k,
the model V⁽ᴿ⁾ transfers Δ_k with error

|Δ_{k,N}^{U}(b) − Δ_{k,N}^{V^{(R)}}(b)| = O_{k,b,R}(N^{k−R−1/2}),

in particular O(N⁻¹ᐟ²) at R = k. Proof: TRACE-017 eq. (18) gives
ε_{N,R} = O_R(N^{−R−1/2}); the §16 (16.14) tuple count is ≤ N^k; (16.15)
assembles the error. The k = 2 trace-form pair sum transfers by the elementary
power-telescoping check of §16.4.

## What is NOT claimed

- No uniformity in k or b beyond "fixed first"; no uniformity in R (the infinite
  series is never summed); startup is noneffective (BGS-FM-021's N₀,
`mathematics/fixed-map/position_chain_mixing.md`); τ is fixed;
  N is odd; no N-dependent tests.
- No single fixed R transfers all k by this method: the exponent k − R − 1/2 is
  structural (N^k tuples × N^{−R−1/2} operator error), identically present in
  TRACE-017 eq. (14). A diverging bound for k > R means "no conclusion", not a
  refutation. The full Laplace functional does not yield Δ_k.
- The phase model's own Sine₂ law is open: the uniform-in-word-length oscillatory
  estimate at m ≍ N and the negative coherent correction −δ* are not proved here.
  This note is a reduction of the TRACE-005 target from U_N to the phase model.
- The literal §16 model of the external document (its S_ν, b_{r,ν}, ℒ₁, 𝒜_j) is
  identified with the repo model only up to the pending written dictionary (gap
  R1: symbol-convention clash, transport signs, explicit P₂/P₃ matching). Until
  R1 is closed, cite this note for the repo-model transfer, not for the external
  document's literal model.
- No §9 intensity bound is used: the input consumed is the parametrix chain
  (FM-021's dependencies), not BGS-FM-021's intensity conclusions (‖P−J‖, C = 5,
  ρ = 1/2; `mathematics/trace-bridge/actual_body_coercivity_constants.md`). §9's gaps U11 (Abel step) and U12 (10⁶⁰ bound) are bypassed, not
  closed, by this route.

## Numerical sanity (not part of the proof)

At N = 51, 101, 151, 201, 301, the model V_N^{(1)} rebuilt from the closed-form
t = 0 Taylor data reproduces the Laplace functional's τ-derivative to
|D_N| ≤ 1.4×10⁻⁶ (worst at N = 101, finite-difference confirmed) against an
O(N⁻¹ᐟ²) envelope of 0.06–0.14, with residual scaling max|R|·N^{5/2} ≈ 37
constant. The N⁻¹ᐟ² rate itself is not confirmed from this range (measured
D_N is non-monotone and far below the bound); one unexplained numerical
observation (S ≈ 0.188 at N = 101, ≈ 0 elsewhere, matched by both models) is
left open and does not affect the transfer. The numerical tables underlying this section are retained in the re-base
verification package (not part of this repository); the numbers above are
self-contained.
