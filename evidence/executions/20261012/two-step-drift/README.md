# Exact two-step drift: reviewed proof and bounded controls

[Canonical proof](../../../../mathematics/two_step_restoring_drift_20261012.md)
and [research outcome](../../../../record/two_step_drift_continuation_20261012.md)
state the one-step theorem and its unresolved probability boundary.

- *inputs/two_step_drift_review_input.md* is the original candidate,
  SHA256 ef9bc8eb3c0c2c09f6d1d571dd87f73f94090f6047ab5e788ef78dcaece180dc.
  *review.json* records the independent reconstruction and the required
  frozen-label averaging correction. The raw input remains unchanged.
- *maintained_transfer_review.json* pins the final corrected proof; its
  scope includes the sharper constructed-witness mean asymptotic.
- *finite-controls/manifest.json* is the accepted version-two execution
  record, with four pinned execution inputs. The actual run exited zero
  in 0.768199 seconds with enforced limits of 90 wall seconds, 80 CPU
  seconds, 1 GiB address space, one core and one library thread. Input
  hashes were unchanged, and current-root manifest validation passed.
- *finite-controls/results.json* separates three Gaussian-rational
  phase-product controls from four exact unitary drift controls. The
  phase products use an independent unit-circle residue calculation at
  deleted diagonals \(0,\ 1/3+i/4,\ 2/7-i/5\). The unitary fixture has
  dimension 64, entries equal to an integer times \(\sqrt2/40\), and
  max intensity \(1/50\). All kernel, swap, cubic, quartic and drift-bound
  checks use exact integers and rational arithmetic. The bounded NumPy
  integer matrix products stay strictly below signed 64-bit capacity.
- *local-regression/receipt.json* records three focused workspace
  verifiers, seven assertion-entry policy tests and unchanged hashes for
  all 199 original imported inputs. It is not a fresh full-suite receipt.
- *manuscript-build.json* and *manuscript-visual-review.json* record the
  accepted 291-page build, actual PDF parsing, the post-completion hash
  check and inspection of pages 285--287. Superseded overflow builds and
  the observed truncated artifact retain separate failure records.
- *preceding_commit_ci.json* and *preceding-ci/* belong strictly to clock
  commit 853bca79423cb1462926592609c911154ca486bd. All seven scientific
  jobs and the independent manuscript workflow passed: 220 workspace
  checks, 236 maintenance tests, 25 C++ targets and 26 Lake jobs for the
  23 active Lean modules. Final-source acceptance is checked separately.

The finite checks do not prove the general theorem. The internal reviewer
did not execute those computations and did not audit upstream conditional
clock proofs or the manuscript build. Neither execution nor review proves
higher moments, high-probability or sustained decay, the all-time flatness
event, scalar microscopic identification, BGS, priority or analytic Lean
certification.
