# Lines N2–N4 integration (31 October 2026, UTC+5)

Base: `origin/main` 3c7ac4a6 (merge of PR #65). Branch: `line-N2N4`. Source note: `mathematics/fixed-map/lineN2N4_inherited_level.md`.

## Packets
* `computations/verification/lineN2/`: author reports `REPORT_N2.md`, `REPORT_N2_v2.md`, `REPORT_N2_v3.md`, `NOTES_N2.md`, code, logs,
  manifests `SHA256_N2.txt`, `SHA256_N2_v2.txt` (+ `.sha256`), referee files under `referee/`. New integration manifest
  `SHA256_N2_v3.txt` (N4-F7).
* `computations/verification/lineN3/`: `REPORT_N3.md`, `REPORT_N3_v2.md`, `NOTES_N3.md`, code, logs, `SHA256_N3.txt` (+ `.sha256`),
  `referee/`; integration manifest `SHA256_N3_v2.txt` (N4-F7); `logs/LARGE_FILES.md`.
* `computations/verification/lineN4/`: the author's `REPORT_N4.md` (unchanged, sha256 6b8684a3…), **`REPORT_N4_v2.md`** (written at
  integration), `NOTES_N4.md`, code, logs, `SHA256_N4.txt` (+ `.sha256`), `referee/`, and `integration_checks/`.
* Every copied file is byte-identical to `/workspace/bgs-lineN/N{2,3,4}` and `/workspace/audit/lineN{2,3,4}` (`diff -rq`).
  Manifests: `manifests.log`.
* **Large binaries.** `.npy` files up to 1 MiB are committed (16 author files plus 18 integration x/y/d vectors). Of the five larger
  files, **`lineN3/logs/g_R_V_final.npy` (3.9 MB) is committed**. It is the extremal norm R that N4's [CA] 8V certificate
  (`lineN4/code/b_arb_cert.py`) reads, and the Adam search that made it is not bit-reproducible. The other four are left out:
  * `R_identity_320.npy` = `np.eye(320, complex128)`;
  * `g_R_V_K04_K55_NT25_cert2.npy` is a byte duplicate of the final matrix;
  * `g_R_V_phase1.npy` and its duplicate `…NT24_cert.npy` are a phase-1 iterate.

  Their sha256 and how to regenerate them are in `lineN3/logs/LARGE_FILES.md` and `receipt.json`. These four are the only `FAILED open`
  lines of `SHA256_N3.txt` in `manifests.log`.
* Not copied: Line N5 (`/workspace/bgs-lineN/N5`, not yet refereed), `.venv`, `__pycache__`.

## REPORT_N4_v2.md (integration errata, §7)
* N4-F1: the gauge corollary is exact up to a unimodular scalar.
* N4-F2: "the isotropic analysis applies verbatim at 7·h_p" is labelled [H].
* N4-F3: the block count is 16 cases × 8 = 128 blocks, with 16 distinct actions and 2 patterns.
* N4-F4: d_squarefree is [N] evidence only, and Theorem C′ is an implication for p with h_p squarefree.
* N4-F5: an exact Z[ζ₁₆] inner-product and norm check, `integration_checks/blocks16_exact_inner.py` → BLOCKS16_EXACT_OK. It covers 64
  blocks with disjoint supports and 64 with identical supports.
* N4-F6: κ, C and the 2p count are p-independent.
* N4-F7: manifests for N2 v3 and N3 v2 in their own directories. Their hashes equal SHA256_N4 lines 55–56.
* N4-F8: D = diag(√(x/y)) from the stored float x and y. `integration_checks/b16_schur_xy.py` is the author's script with the J3 path set
  to the repo copy and two `np.save` lines added (`b16_schur_xy.diff`). It reproduces all six Schur runs bit for bit, with x and y
  stored; `check_schur_xy.py` → SCHUR_XY_OK.
* N4-F9: Line L §5(b) is cited as BGS-TRACE-253.
* **I-1:** for 16V, f + π = 2.9413895663 + 3.9·10⁻⁸ = 2.94138961, which is above the author's and the referee's 2.9413896. The referee's
  Lean line `(2.9413896:ℚ) ≤ 2.9413896` left out the penalty. The registered bound is **2.9413897** (Lean `lam16V_rounding`,
  `assembly`). The rate (Λr₂)^{1/3} = 1.4578840 < 1.45789 is unchanged.
* **I-2 (owner instruction, Line N5):** N4 §3.3–§3.4 rest on a wrong premise (one slow window of length ≈ p/2). The superseded numbers
  are not registered: G ≤ 1.547, 1.4468, and 1.2426 / 1.0672 / 0.9165. The referee's Lean `remainder_rates` and `leading_fails` are left
  out of `Bgs.LineN4`.
* **I-3:** the 7·h_p unit points are not registered (N5 has an unrefereed [P] upgrade).

## Claims (record/claims.json, hand-edited by `add_claims.py`; scripts kept outside the tree)
New ids 286–298: 11 proved and 2 open (287, the Ω-hypothesis; 298, the isotropic part at q ∣ h_p), each open id with a closure condition.

How the owner's registry list maps to ids:
* four Λ bounds → 295;
* Theorem C′ → 296, stated as "for every prime p with h_p squarefree and p ≥ p₀", not as a hypothesis on an open claim;
* N2 Theorem A → 286, a proved implication like TRACE-257. Its antecedent is the open 287, which is not a dependency, and Theorem K (240)
  is not a dependency either;
* Theorems B and C → 288 and 289; Prop E → 290;
* Lemma I / I₁₆ → 294; gauge lemma → 297 (up to a unimodular scalar);
* isotropic Lemmas 1.1 and 1.2 → 291 and 292; C3 → 293;
* C1 → the widened 222; the 266 widening as instructed;
* open "isotropic part at q ∣ h_p", generic → 298.

The isotropic item at 7·h_p is folded into 298, so there is no separate id. **C2** is not a new id: it stays a condition of the open 276,
whose closure condition is now reduced to C2. Not registered, per the owner's update: the remainder rates, the "leading term G ≤ 1.547"
open item, the 7·h_p unit points, the 16D = 1 family and its shares, and anything from N5.

Amendments (states unchanged):
* 222: scope widened to every τ ∈ R/Z and non-autonomous products. The justification is the twist-free proof, RK: (C, a, τ) ↦ (−C, a−4, τ),
  and the referee's "C1 is proved by the proof of TRACE-222".
* 266: widened to any odd c with ord_c λ = p (the proof uses only the period and cyclicity), with a new dependency on 277.
* 276: C1 and C3 proved, C2 open, new dependency on 293.
* 206 epoch annotation.
* 206 and 239 stay open, and 240 stays conditional.

Registered numbers are rounded upward (bounds) or checked below the target (rates) from the committed logs by
`integration_checks/lineN2N4_checks.py` → LINE_N2N4_CHECKS_OK. Theorem C′ uses the N4 [CA] values. The 8E rate is 0.80266, not N3's
[CA*] 1.20428, and the 8V margin is δ ≥ 0.0071.

## PR #65 evidence: iso_coverage.py (owner note about the process killed at 19:25)
* The committed `computations/verification/lineN/integration_checks/iso_coverage.log` (mtime 17:58:44 UTC+5, before commit b09ae6e3 at
  18:09) was written by a complete run of the committed float script (sha256 df8767b1…). It ends with the totals line and
  ISO_COVERAGE_OK, which are printed only after the whole grid loop has finished. That loop includes log10 p ∈ {500, 10³, 10⁴, 10⁶, 10⁹},
  so the p = 10^{10^9} point is included.
* Rerun on this branch: 26 s, **byte-identical** output (`integration_reruns/iso_coverage_rerun_pr65.log`).
* The process killed at 19:25 is therefore not the run behind the committed log. Most likely it was a leftover copy of the earlier mpmath
  version, which timed out during PR #65 and was replaced by the float version. No #65 evidence text needs correction.
* One precision note: for log10 p > 400 the grid has 2001 points per (p, τ) plus the case boundaries. "All p" rests on the analytic case
  split (Part 1), not on the grid. The #65 wording ("analytic case split for all p + grid 10^264.5..10^400 and larger p") already says
  this.

## Gate and Lean
* `lineN4/integration_checks/proved_deps_gate_N2N4.py`: strict for 244–298 → GATE_OK. The #64 and #65 gates also pass.
* `Bgs.LineN2Arith`, `Bgs.LineN3Arith`, `Bgs.LineN4Arith`: the referee files sit inside `Bgs.LineN{2,3,4}` namespaces with
  `#print axioms` for every theorem (8 + 9 + 6). LineN4 differs from the referee file in three ways: the I-1 correction, two theorems
  removed, and two added (`unit_rates_registered`, `lemI16_V`). `lake exe cache get` and `lake build Bgs` exit 0 (8841 jobs). Axioms are
  propext, Classical.choice and Quot.sound only, with no sorry and no native_decide.
