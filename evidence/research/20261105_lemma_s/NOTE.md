# Research note: bad divisor levels, Lemma S and the Binet generator (5 November 2026)

**Registry change: BGS-TRACE-352..355 only** (three proved, one conditional). This note records the research pass
`research1105b` (question: are the bad divisor levels of R′, BGS-BGS-001 / BGS-TRACE-206, harmless without
cancellation?) and its independent internal referee audit, and states which parts were registered. The proofs and the
integration checks are in
[REPORT_LEMMA_S.md](../../../computations/verification/lemma_s/REPORT_LEMMA_S.md); the receipt is
[evidence/executions/20261105/lemma_s/receipt.json](../../executions/20261105/lemma_s/receipt.json).

**Files (copied unchanged; not edited).**
- `source/REPORT.md` — the research report (research1105b, main @ 6f69baa1), with `source/code/` and `source/logs/`.
  The binary arrays `logs/lvl/`, `logs/prop/` and `logs/val/` (about 9 MB of `.npz` plus their metadata) are **not**
  copied; the numbers quoted from them are [N] and are not registered.
- `REFEREE.md` — the independent internal referee audit (hostile reading, not external), with its code and outputs in
  `referee/`.

**Tags.** [P] proof · [P-sketch] sketch with named gaps · [CA] exact or exhaustive computation · [N] floating-point
numerics · [H] heuristic · [C] conjecture.

## 1. What is registered (referee-confirmed, corrected statements)

| Id | Statement | Referee | Status |
|---|---|---|---|
| BGS-TRACE-352 | Lemma S: on a cross line, G(cεⁿ) + G(cε^{n+p}) ≥ √max(d₊, d₋) for every class c ∉ 𝔞̄_{−σ}; on the axis sub-line 0 ≠ c ∈ 𝔞̄_{−σ} only G ≥ √min(d₊, d₋); max(d₊, d₋) ≥ √h_p needs squarefree h_p (conditional on H6) | item 1, CONFIRMED with scope gap | proved [P]; [CA] exhaustive p = 11, 13, 17 + sampled exact ω=3 at p = 37; Lean partial |
| BGS-TRACE-353 | Polymer gap: f ∉ (η₊η₋) ⟹ K > log_ε min(d₊, d₋) − 2 log_ε A − 1.214 (exact constant log_ε(ε²/2) = 1.21356) | item 2, CONFIRMED, constant made explicit | proved [P]; [CA]; Lean partial |
| BGS-TRACE-354 | Binet generator: N(η_s) = +h_p and (η_s) is the Binet-line lattice in Z[ζ_p]; in Z[x]/(x^p − 1) the lattice is (η_s) + (Φ_p) and (η_s) has index 2h_p | item 4, CONFIRMED with precision gap | proved [P]; [CA] p ≤ 73; Lean partial |
| BGS-TRACE-355 | H5(b) cross lines: a uniform bound \|X_line\| ≤ C e^{−cp}, C ≤ 1, c ≥ 0.058 fits the idealised V5/TRACE-333 room at p = 1409 and 3307 (rooms recomputed on main, not taken from PR #85) | item 3: source constant 0.048 WRONG; corrected | conditional; constant [CA]; not in Lean |

## 2. What is not registered

- **Source §0.4 / §5 "no hypothesis on P⁻(h_p) is needed for the vacuum part".** Holds only off the axis sub-line; on
  0 ≠ c ∈ 𝔞̄_{−σ} the smallest-prime ceiling returns through √min(d₊, d₋) (referee item 1). Recorded in TRACE-352.
- **Source §4.4 c > 0.048.** Wrong (w_max(3307) = 231, not 228; the room; the binding prime 1409). Replaced by TRACE-355 (rooms recomputed from V5/TRACE-333 on main).
- **Source §5.3: seam-polymer decay r < ε^{−0.99} ≈ 0.418, the vacuum estimate e^{−cp} with c ≈ ln(1/r)/4, and the
  bridged-part estimate poly(p)·min^{−γ}.** [C]/[H]; the data are borderline (0.33–0.48 per ε-site). Not registered.
  Moreover (referee) no uniform e^{−cp} cross-line bound follows from §4 for lines with small min(d₊, d₋), so the
  hypothesis of TRACE-355 is open and not supplied by TRACE-352/353.
- **Corollary S′** (window-length dictionary) [P-sketch]; the multi-window case [C].
- **§2 no-go table, §3 numerics.** [P no-go] statements and [N] data are recorded here only. The referee reproduced the
  p = 11 numbers (Dev/main 0.0338759 over ii + ui + iu; |X|/ℓ1 = 0.348 / 0.621 on cross lines at p = 11 / 13;
  max|u| 2.24e−7 / 1.93e−6 vs 3.96e−4) with two corrections: "exact" excludes the uu class (honest form
  Dev/main = 0.03389 ± O(1e−5) [N + H]), and the per-line rows of `logs/seam_profile_p1{1,3}.json` depend on the orbit
  representatives kept and should not be quoted per line.
- **Typo corrections from the referee:** ⟨E⟩ for ρ = (−2, 8) is 0.016478 − 0.008186i; Dev/(φm) at level h_p, p = 11, is
  0.0700.

## 3. Status of the programme items touched

H5 (BGS-TRACE-303) stays **open**; H6 (BGS-TRACE-304) stays **open**; Theorem R♯-mod v5 (BGS-TRACE-325) stays
**conditional**; frozen R′ (BGS-TRACE-206) stays open and is not refuted. No existing claim is edited. The source
report's conclusion that bad levels are 1–3 orders below the gas at every computed composite h_p is [N] and is not a
bound at p ≥ 1409.
