# Final recovery and integration audit — 21 September 2026

Base lineage: main \(d75b7cb04b60cd780a8d4ac8da62225e1c91477e\), recovery PR #16 commit \(1c4da1e381d5e48ce6b58618a439ac46d8aa7181\), then the 21 September integration commit.

This record distinguishes recovery, mathematical status, computational replay, and Git publication. It is not an independent referee report.

## 1. Conversation handoff recovered

The final conversation artifact was BGS_final_handoff_20260921.zip:

- bytes: 123387;
- SHA-256: 032e965cd39a12d2a19f5520fad84fdb305043ef2717e8e8adeac79a34e02c01;
- root manifest: 54 files;
- root and nested SHA-256 manifests: all entries matched in the integration audit.

The handoff was built on the same scientific tree as PR #16. Its local commit label differed, but the recorded tree was \(1b2a9c49511d8e6f2889302d02a55584b79c3151\), identical to the PR #16 head tree. The integration therefore extends PR #16 rather than replacing or rebasing its recovery work.

## 2. Late mathematical results promoted

The previously unpublished late checkpoints are now represented by maintained notes:

1. fixed_model_moment_control_and_transfer.md:
   stronger low-order moment interval; exact repeated-clock falsifier for one-upper loop tests at one height; simple-spectrum persistence; growing-amplitude RMS transfer.
2. three_orientation_resolvent_barrier.md:
   the conditional three-orientation barrier with explicit coefficient \(1/64\).
3. fixed_model_symmetry_theorem.md:
   exact raw-to-midpoint Weyl dictionary for the frozen generator; trivial \(C^1\) centralizer, no \(C^1\) reversor, and non-affine-conjugacy for the actual classical map.
4. fixed_model_pell_crossover.md:
   full-symbol odd-Pell Gaussian crossover with exact variance \(1650797/4000000\), giving the necessary condition \(|\epsilon_K|\sqrt K\to\infty\) for CUE pair behavior in that family.
5. fourier_line_resonance_coercivity.md:
   sharp coercivity on the complete Fourier-line class; exact \(H^2\) constant \(\sqrt{(T-2)/(T+2)}\), equal to \(1/\sqrt2\) for the project matrix in its stated convention; \(H^{3/2}\) positivity for \(|\operatorname{tr}A|\ge6\).
6. local_jet_resonance_obstruction.md:
   an exact local polynomial coboundary showing why fixed-point Taylor jets alone cannot solve the global analytic resonance obligation.

The fixed-\(\tau\) BGS conjecture remains open. None of these statements is promoted to a universal microscopic random-matrix law.

## 3. Independent replay performed during integration

Before promotion, every supplied Python verifier was rerun from a clean temporary copy with bytecode disabled and single-threaded BLAS. All six passed:

- growing-transfer: 18 general finite inequalities and 6 Pell matrix comparisons;
- moment-controls: symbolic recursion through order 20, 6 repeated-clock cases, 3 simple splitting controls, 18 moment inequalities;
- three-orientation: exact symbolic identities plus 21 finite spectral cases; maximum reported identity error about \(3.1\times10^{-14}\);
- fixed-model symmetries: exact rational/symbolic certificates and finite matrix dictionary checks at \(N=19,41,81,161\);
- full-symbol crossover: exact variance \(1650797/4000000\), sparse and dense finite controls;
- Fourier-line rigidity: 750 exact orbit identities, 520 recurrence checks, sharpness fixtures, positive \(H^{3/2}\) interval, and the local jet negative control.

The original saved Wolfram outputs were hash-verified as part of the handoff manifests but were not freshly executed in this environment. They are supporting cross-checks, not a substitute for the proofs.

## 4. Old pull-request disposition

### PR #11

Its projective-Bezout verifier is byte-identical to the current maintained copy. The proof and claim-ledger material have later corrected/expanded versions. No scientific file needs resurrection.

### PR #14

Fifteen scientific files are byte-identical to the current tree. The remaining absent paths are obsolete dedicated workflows, one-shot publisher/integrator scripts, and standalone manuscript/PDF surfaces deliberately retired by the single-manuscript consolidation. The mathematical coboundary content is already maintained.

### PR #15

Thirteen scientific files are byte-identical to the current tree. Its missing files are the obsolete dedicated workflow, one-shot publisher, and standalone section. The fixed-strength locality proof, robustness theorem, verifier, evidence summary, and Lean kernel are already present.

### PR #13

This branch must not be merged wholesale. The independent 5 September audit falsified its claim that every triple resultant filter equals \(p\): for example \(K=43,p=173\) gives \(865=5p\). The necessary divisibility direction survives.

The valid inverse core has subsequently been superseded by cleaner exact statements already on main: inverse reflection \(I_{-1}=2\deg\gcd(E,O)\), the pair-sum perfect-square factorization, the translated half-degree resultant, and scalar shift-resultant support. The draft branch remains recoverable by Git history and is now explicitly recorded in branch-snapshot provenance. Its obsolete standalone files are not reintroduced into the maintained surface.

### PR #16

PR #16 is direct ancestry of this integration. Its 27-file recovery is preserved intact and is the base of the final 21 September work.

## 5. Canonical manuscript and CI repair

A complete readback shows that manuscript/unified_sections/fixed_map_frontier.tex was already included near the end of WoW_unified.tex. An earlier partial view of the long master file was misleading; no claim of a missing frontier input is retained.

The actual CI asymmetry was narrower: the independent manuscript workflow checked both return-section and fixed-map synchronization, while the main scientific workflow checked only the return sections before building. The integration adds sync_fixed_map_section.py --check to the main workflow and inserts the separate 21 September publication summary immediately after the already-present fixed-map frontier.

## 6. Verification boundary

The six recovered Python verifiers passed locally as described above. A compact maintained regression gate was added for the load-bearing exact identities. The GitHub Actions runs before this integration had failed before execution, with no usable step/log payload; they did not constitute mathematical test failures.

The environment used for this recovery still has no local Lean/Lake executable. Existing Lean source status is therefore unchanged: source-level audit only unless a later CI run actually compiles it.

The remaining mathematical bottleneck is still a model-specific Heisenberg-scale estimate for the frozen operator: either mixed-resolvent defect decay at all required orders or an equally strong direct joint-trace comparison. Classical symmetry exclusion, positive resonance variance, weak-kick crossover obstructions, and finite regressions do not supply that estimate.


## Post-integration forensic continuation

A later same-day audit obtained older 14--16 September Library artifacts that
were not available in the original handoff archive.  This does not invalidate
the recovery above, but it means this record is no longer the last word on
historical completeness.  The authoritative continuation is
[verified_state_reconciliation_20260921.md](verified_state_reconciliation_20260921.md).

That reconciliation recovered the raw-Weyl Heisenberg path-escape theorem,
the exact/19-adic direct-attack results and the one-shear antiunitary no-go,
while also preserving the later retraction of the v9 two-frequency Bourgain
shortcut and the correction of the historical blanket “CUE contraction
sector = min(m,N)” assertion.  The later refinement below repairs its ramp
part while leaving the plateau and post-cyclic residual open.


### Recovered ramp/history refinement

The same forensic pass subsequently reconstructed two further layers from the
16 September verified working state, but only after repairing their chronology
against the later gauge/source audits.

The one-step unistochastic argument was not discarded wholesale.  Its old
non-pairing curvature witness used the pre-gauge midpoint symbol and failed
after the raw-to-midpoint correction.  A new witness at q0=1/7 restores the
argument for the corrected physical symbol; the resulting exact cyclic
skeleton supplies the CUE ramp below the plateau.  This does not evaluate the
post-cyclic residual or the plateau.

The audit also recovered exact finite-dimensional Parseval history
normalization, two-sided Hilbert--Schmidt stopping-time gluing, literal
segment-reconnection tensors, and an elementary absolute envelope for the
standard unitary encounter coefficients.  These narrow the complete-matching
all-order problem to genuine partner localization/uniform quantum domination;
they are not represented as a completed partner-orbit theorem.

The maintained status authority is therefore the combination of
`record/verified_state_reconciliation_20260921.md`,
`record/claim_ledger.md`, and `record/retractions.md`, rather than any
historical dossier label.
