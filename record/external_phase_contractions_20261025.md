# External auxiliary results: phase contractions and arithmetic leakage (Oct 25, 2026) — DRAFT RECORD NOTE, staging only

Source: independent work by an external agent, without repository access
(document "Фиксированная квантовая карта: новое продолжение",
2026-10-25, 816 lines, 9 sections). This note records what was verified,
with scope labels. It proves no local law and changes no claim status:
TRACE-005 and BGS-001 remain open. Verification package:
`~/workspace/bgs_rework_exec/phase_contractions_verify/` (four independent
streams, exact recomputations kept).

## Verified negative results (proved, new as statements)

- **Shift-4 row correlation does not vanish under restriction (§§1–2).**
  For the χ-weighted row correlation at the fixed shift 4, the bound
  ‖…‖ ≥ 1/4 − 200τ > 0 holds for all odd N ≥ 3 at the repo's fixed
  τ = 10⁻⁸⁰ (in fact 1/4 − 2·10⁻⁷⁸). The proof uses only the T-commutator,
  M-conjugation, the A_N Fourier support (|k| ≤ 9, |l| ≤ 1, Σ‖c‖ =
  √101/50 + 19/20 ≈ 1.151) and an exact Duhamel integral; no τN ≪ 1, no
  stationary phase, no per-word sum is used. The level-set corollary
  (11) is proved but existential: the set F_{N,x} depends on N and x,
  and no specific path class is evaluated. Scope: this closes the
  universal-restricted-vanishing route (restrict first, then use
  full-row orthogonality). It says nothing about the full Y-sum, whose
  sign and magnitude (VN2-MAIN) remain open. Wording note: the A_N
  symbol is repo-g (= §9-a), not §1-f; the bound is unaffected.
- **Arithmetic-subspace leakage does not survive the kick (§6).**
  At N = 361r (r odd), for the standard arithmetic subspace Ran P_N
  (support on multiples of 19, constant on fibres), the one-step average
  leakage satisfies ‖P_N U_N P_N‖²_HS/r → 1/361 and
  ‖Q_N U_N P_N‖²_HS/r → 360/361 as r → ∞, at fixed τ = 10⁻⁸⁰.
  The embedding is exact (M_N J_N = J_N M_r, M_N acts on the subspace as
  the same map at size r), and the whole subspace is exactly not
  preserved: P_N A_N P_N = 0, P_N A_N² P_N = (66033/160000)P_N.
  Scope (read exactly): average over a basis of Ran P_N only; no
  per-vector claim, no operator-norm bound < 1, no Δ₂ statement, no
  Tr U_N^m at m ≍ N. Feasible-N leakage is ≈ 0, consistent with the
  VN2 crossover hierarchy — the limit lives at r → ∞, far beyond
  feasible N. This is a negative result about inheritance mechanisms,
  not a step toward TRACE-005 or BGS-001.

## Negative applicability checks (proved, no new theorem)

- **Quantum-graph transfer (§4):** no o(1) transfer of the
  Gnutzmann–Altland functional is obtained. Their R₂ uses a k-average
  traded for B independent phases; the repo Δ₂ functional has fixed τ,
  fixed N, and no average at all (and the repo Laplace functional only
  a single common shift). Precision note: Gnutzmann–Altland do treat
  individual graphs, but only under k-averaging; the mismatch stands.
- **One-step data do not close the second return (§7.1):** with
  U_N = [[B,C],[D,E]], P_NU_N²P_N = B² + CD exactly, and unitarity does
  not determine the cross term. The V₁/V₂ toy (first-return squared
  norm 1/361 both; second-return squared norms 1 vs 1/361²) makes the
  insufficiency visible; it is not a model of U_N.
- **Weyl-sum precision (§7.2) and time-smoothing (§8):** both report
  failure, correctly. O(N³) summands mean per-term o(1) is a factor N
  short of what Δ₂ needs; the v/N → 0 family and m ≍ N iterations are
  uncontrolled — the same missing uniformities as VN2-LEMMA's
  alias-control sub-gap. Time-smoothing concentrates the kernel at
  scale 1/N and does not replace local spectral control.

## Results already in the repo (recorded for provenance, not re-claimed)

- **Spectral simplicity at 7∤N (§9):** the theorem is BGS-FM-008
  (proved, strictly stronger: all square minors nonzero, simplicity of
  every power U_N(t)^m, all characteristic coefficients nonzero,
  |Tr U^m|² transcendental). §9's §§9.3–9.5 proof route (eigenvector
  minors + Cauchy–Binet unique-minimum term) is verified correct but
  adds no repo-level result; its §9.2 Jacobi-form derivation has a gap
  as a standalone text (the form itself is repo-proved as FM-005).
  Scope, stated exactly: simple is U_N(t) (and A_N as a step); M_N alone
  is not shown simple; §9.1 is FALSE at N = 7, not merely unproved
  (A₇ = (9/10)I exactly); §9 gives no eigenvalue-gap bound, no local
  law, and no input to asymptotics at m ≍ N.

## What this document does NOT do

It does not prove TRACE-005, BGS-001, any Δ_{k,N} limit, any Sine₂
statement, or the −δ\* correction; it does not close VN2-LEMMA, VN2-J,
X4, or R-L6. Its §§3, 5, 6.7 and 8 say so explicitly, and verification
agrees. No section repeats a previously refuted claim as a proof; the
guardrails for future work (per-term/per-word routes, κ-family
uniformity, non-rotation cancellation, k-averaged transfer smuggling,
external §§9–10 intensity bounds as input, V⁽¹⁾-based routes) are listed
in the verification report.

## Landing verification (parent, 2026-10-25, HEAD 90c3b18)

Live-main greps performed before landing on the fresh 90c3b18 snapshot:
"361r", "multiples of 19", "J_N M" / "M_N J", "19²" — no hits in
mathematics/ or record/ (bare "361" hits are unrelated: a DOI suffix and
a hash); "arithmetic subspace" — no hits; "row correlation" / "shift-4" —
no hits; BGS-FM-008 live row confirmed proved ("Total nonvanishing of
frozen metaplectic minors and qualitative fixed-time spectral
simplicity"). Landing condition (1) of the draft is thereby discharged;
conditions (2) scope labels kept and (3) no registry change stand.

## Landing conditions (parent decision)

This note is staging only. Before landing: (1) run a live-main grep for
"361", "J_N", "arithmetic subspace" and for any §2-equivalent bound to
confirm the "not found in repo" verdicts against current main; (2) keep
every scope label above attached — without them the §2 bound and the
§6 limit are easy to misread as progress on the local law; (3) no
registry change follows from this note under any reading.
