# External auxiliary results for the fixed quantum map (Oct 22–24 2026)

Source: independent work by an external agent on the standalone
TRACE-005 task text, without repository access. This note records what
was verified, with scope labels. It proves no local law and changes no
claim status: TRACE-005 and BGS-001 remain open.

## Verified exact algebra (independent recomputation, no gaps found)

- Algebraic specialization lemma (Lindemann–Weierstrass application):
  degenerate eigenvalues harmless; coincident exponents grouped before
  applying LW. Applies to A_N ∈ Q(i,ζ_N) and M_N.
- No exact scalar returns (Thm 1): Tr(A_N R_N) = 9/10 exactly; Tr(A_N)/N
  exact for all odd N, including the N = 7 exception A_7 = (9/10)I.
- Weyl-normalizer commutant (Thm 2): full |c|^2 table verified;
  ρ = (99+20i)/101 is not a root of unity (ρ+ρ⁻¹ = 198/101 non-integer).
  Repo overlap: these are BGS-FM-010, and Thm 2 is subsumed by proved
  FM-024; recorded here as independent corroboration, not as new claims.
- Kick structure at composite sizes; nonvanishing of all traces
  (|Tr M^m|^2 = |ker(S^m − I)|); exact long-trace arithmetic (plus sign
  in (33.2) confirmed, minus sign refuted); Schur-complement and scalar
  first-return bounds. One notation note: the correct forward-order
  diagonal is diag(e^{−iα₀s}), not diag(e^{iα₀s}) as literally written.
- Parametric dynamics: exact trace equations; commutator HS-norm
  asymptotics κ/N² with κ = 252116.6667717927 exactly; onset N ≳ 3500–5000
  (numerically: 88% of κ at N = 1001, 99.5% at N = 5001). Closure for a
  local law is missing.

## Conditional transfer to an explicit phase model (§16) — CONDITIONAL

The document transfers the full Laplace functional (under one model V⁽¹⁾,
error O_f(N⁻¹ᐟ²)) and each FIXED Δ_k (under a k-dependent model V⁽ᴿ⁾,
R ≥ k, error O(N^{k−R−1/2})) to an explicit phase model (four §9 phases +
transport amplitudes + polar unitarization, deterministic, same τ).
Uniformity holds only for fixed k, b, f; no single model transfers all
Δ_k. The phase model's own Sine₂ law remains open: operator-norm
closeness gives no estimate for long-word alternating sums at m ≍ N.
STATUS: CONDITIONAL on the §9 intensity proof, whose gaps are listed in
§4 below. This transfer is the document's largest genuinely new item and
the reason this note exists; it is NOT a repo theorem.

## Results already in the repo (recorded for provenance, not re-claimed)

- Intensity bounds max|U_N|² ≤ 5/N, ‖P_N − J_N‖ ≤ 1/2: repo BGS-FM-021
  (mathematics/fixed-map/position_chain_mixing.md) + constants note
  (mathematics/actual_body_coercivity_constants.md, C = 5, ρ = 1/2).
  The document's §9 proof of the same bounds has gaps (see §4); its
  sharper limsup ≤ e^{2τ} − 1 is therefore also conditional.
- Diagonal-sum corollary Σ|D_m − m| ≤ 28 + 800/N: same FM-021 ingredients;
  the summed closed form is new as written but conditional on §9.
- Equal-edge-multiplicity exponential contributions at m = 3(N−1)/2:
  repo BGS-TRACE-088 (mathematics/trace-bridge/equal_edge_occupation.md)
  is stronger (rate ≈ 0.195 vs log 2/750 ≈ 0.00092); TRACE-093 gives the
  exact rate. The document's every-third-step route is weaker.
- Antiunitary exclusion: repo BGS-FM-009
  (mathematics/fixed-map/frozen_common_antireversor_certificate.md)
  covers ALL odd N ≠ 7. The document's §28 threshold (φ(N) > 64540,
  N > 4,165,411,600), improved in verification to all odd N > 137,445
  (degree ≤ 56700 / 8100; sieve-verified), is a document-level
  improvement only and is conditional on §28's reduction, which was not
  fully checked. "Up to phase" adds nothing (phase cancels in BŪB⁻¹).

## Failed routes logged (negative results, useful as guardrails)

N²-dimension counting (§32), time-averaging (§34), Pell first-return
countermoves (§35, conditional, initial segment only), quantitative use of
τ-algebraicity (§19), determinant-route insufficiency (§§22, 24, 29–30
as method limits). §30's C_N counterexample (distinct microscopic limits
under the same locally uniform disk limit) is new as written and delimits
what disc methods can show.

## Gap list carried forward (§9, binding for any §9-based claim)

Amplitude-derivative bounds for the O(N⁻³ᐟ²) remainder; the
variable-denominator Abel step in Lemma 9.12; the 10⁶⁰ second-derivative
bound (count incoherent as written, but any bound below ~10⁷⁷ closes the
τ-window); gluing preservation at t ≠ 0 (uniqueness class, mod-4 branch
identification); the (9.5) 4-term identity needs the 16-case residue
check, not the "completing the square mod 8" sentence. No explicit N₁/N₂
follows from §9 as written.

## Status restatement (recorded 2026-10-24, task text itself frozen)

The standalone task text `record/remaining_breakthrough_task_20261021.md`
is preserved unchanged as given to the external agent. The current
position, recorded here rather than by editing that text, is:

- The intensity premise for the original matrices is discharged
  in-repo by BGS-FM-021 (`mathematics/fixed-map/position_chain_mixing.md`)
  with the constants note
  (`mathematics/actual_body_coercivity_constants.md`, C = 5, rho = 1/2).
  The document's own §9 proof of the same bounds is NOT used for this:
  it has open gaps (see §4 of the gap list above).
- The remaining target is unchanged in substance: the Y-sum limit
  -> -delta_* for the first pair test (k = 2), then all fixed orders
  k >= 3. The §16 transfer, if re-based on FM-021's proved parametrix,
  would reduce the k = 2 target to the phase model V_N^(2); that
  re-basing is queued as the next step, and the uniform-in-word-length
  oscillatory asymptotic for V_N^(2) is the located next problem.
- TRACE-005 and BGS-001 remain OPEN. No claim status changes.
