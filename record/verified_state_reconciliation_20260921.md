# Reconciliation of the 14--16 September BGS working dossiers

Date: 21 September 2026.

Purpose: reconstruct the material present in the earlier BGS working conversation that was not represented cleanly in the 20--21 September repository handoff. This is a status crosswalk, not a priority claim and not a claim that every historical line is correct.

## Recovered source artifacts

| Artifact | SHA-256 | Disposition |
|---|---|---|
| BGS_full_resolution_dossier_v7(1).md | 49c4298eadbd13d7cf561a5282471e6d800e1f02433bd6e82db8c52a1845f56f | path-escape/rank core recovered after raw-Weyl repair; classical-symbol layer superseded |
| BGS_full_resolution_dossier_v9.md | 6ba8a60962417221e04a40623eb6ec2be600a0c2142867f53ae1fe0fa4638b6b | arithmetic derivations retained only where independently repaired; two-frequency Bourgain closure rejected |
| BGS_direct_attack_v11.md | 42f5e7ce844d7584115ce48fea7c5f3138c2a3af827cda12798cc9186ae21e0d | authoritative historical correction for v9; one-shear and 19-adic results promoted |
| BGS_verified_state(1).md | d38bcd35482a288251f981cf97ba6f68978ac811b5a92579f2cf52c9540fbfe4 | 11,033-line referee-style working state; used as a map of claims and retractions, not imported wholesale |
| bgs_v7_verification.py | 913bbd1519c438d08c4a0bee72c75e05fe20c79e9a62f66159aab1203cdb2f46 | freshly rerun: PASS |
| bgs_v9_arithmetic_checks.py | 338e4528dd1bc5269d8b730dea207b193f002619b4fa236b89916e2fc24b3ed2 | freshly rerun: PASS; its incomplete sums are diagnostics only |
| bgs_v10_direct_checks.py | 3c1a3999f5def76c483b6dab85ad5a28f198744e64ba3a8ef7b67ddd47a6c724 | freshly rerun: PASS |
| bgs_v11_padic_checks.py | 8b8916fec7b813437a69d6005af86a6f9652337285f8f5f8378ace2b09d62a57 | freshly rerun: PASS |

The historical files themselves are not vendored as competing sources of truth. Maintained statements were rewritten against the current raw operator and current claim vocabulary.

## v7: what survives

The old v7 classical model treated the raw modular Weyl generator as though it had the same ordinary midpoint symbol. The later dictionary shows that this is false: the p-dependent term acquires a q -> q+1/2 shift. The v7 fixed-point and symmetry layer is therefore superseded by the current fixed-model symmetry theorem.

The Hilbert--Schmidt path argument is different. In the raw gauge an extra sign occurs in Weyl multiplication, but commutator magnitudes, support radius and coefficient magnitudes are unchanged. The exact path-escape proof has therefore been reconstructed directly in the correct gauge and is maintained in mathematics/fixed_map_weyl_path_escape.md. It includes the microhop bound, near-sector theorem, multiscale escape and the all-characteristic rank >= s/25 lemma.

This resolves two items that the 16 September state labelled UNVERIFIED only because the proof dossier was then unavailable: the final-map Chernoff/multiscale proof and the induced-matching rank proof are now present and independently replayed.

## v9: explicit quarantine

v9 correctly derived a two-frequency hyperbolic phase of the form A lambda^j + B lambda^-j on split primes, but used a Bourgain result as if large multiplicative order supplied the required uniform two-frequency incomplete single-sum bound. The 15 September v11 source audit found that the cited theorem did not imply that statement.

The v9 two-frequency theorem and its sliding-variable / BCD2 corollary therefore remain RETRACTED. Passing finite scripts that print sample incomplete sums do not repair the missing theorem.

A second correction is independent: v7--v9 referred to an “exact CUE contraction sector” and assigned it the value min(m,N). For the final two-directional deterministic map that sub-sum was never explicitly defined and evaluated. The label is not a theorem. Even perfect control of a separately named connected remainder would not finish pair BGS without this signed main-term calculation.

## v11: promoted direct results

Three components survive the audit and are now maintained:

1. the exact antiunitary no-go for every q-only kick when the metaplectic upper-right entry is invertible modulo N;
2. exact order, orbit and Parseval theory on N=19^k;
3. the pointwise O(N^(2/3) log N) hyperbolic incomplete-sum theorem, using Cluckers' analytic non-archimedean van der Corput theorem after an explicit fixed-power derivative rescaling.

See mathematics/one_shear_antiunitary_no_go.md and mathematics/hyperbolic_19adic_dephasing.md.

## Why the 16 September state is not copied into main

The large BGS_verified_state.md is valuable because it already distinguished PROVEN, OPEN, RETRACTED and UNVERIFIED items. It was nevertheless a living working document, and later work changed several statuses.

Most importantly, its shadow-history route was subsequently re-audited in mathematics/shadow_tube_history_bridge.md: the symbolic filling bound is proved, the geometric periodic-pair statement is conditional on an explicit equidistribution input, and an exact finite-state example shows that tiny positive history mass can coexist with a growing coherent trace. Those later qualifications govern.

Likewise the old redesigned-symbol and report-summary claims are governed by the 19 September report audit, not by earlier screenshots or working labels.

## Other historical attachments

research-summary (1).md is an early summary, not a theorem ledger. Its unitarity-only resonance suppression, zero-higher-order CUE target and unrestricted symmetry language were corrected by the maintained report audit.

kicked_cat_sine_kernel.md is retained only as a historical diagnostic. Its “all k reduce to k=2” shortcut is false, its Anosov justification is incomplete, and its antiunitary tests are not exhaustive. No theorem from that attachment is silently imported here.

## Updated frontier

The recovered path theorem removes one ambiguity: nontrivial Heisenberg paths cannot spend almost all their time in small Weyl modes. On N=19^k, a deterministic pointwise cancellation bound is also available for free hyperbolic time phases.

What remains open is the signed insertion problem: prove that the complete fixed-map tensor/path expansion exposes enough summable nonresonant variables, while explicitly evaluating the surviving signed main sector as the CUE triangular form factor. The loop-equation route in the current fixed-map chapter is an alternative sufficient formulation of the same microscopic cancellation difficulty.


## Additional recovered result: all-time classical stability

The verified state also contained a classical theorem that survives the
later symbol repair.  The corrected physical map is still real-analytic,
area-preserving, Anosov and topologically conjugate to S.  Jézéquel's
analytic Ruelle trace formula therefore gives the all-time
stability-weighted periodic-point sum 1+O(rho_cl^m), while topological
conjugacy gives the exact cat periodic counts.  This is now maintained in
mathematics/fixed_map_classical_sum_rule.md.  It is a classical input, not a
quantum form-factor estimate.


## Selective-authority rule for the remaining 16 September state

The 16 September working state contains many later labels such as
`[PROVEN]` for logarithmic FIO blocks, Hilbert-valued Dolgopyat transfer,
quantum cylinders, Naimark dilation, shadow tubes and encounter localization.
Those historical labels are **not** imported wholesale into the current claim
ledger.  The document was a living internal state, and later 17--20 September
audits changed the status of several of those routes.

This reconciliation promotes only results that were independently
re-derived/replayed here or already have a later maintained proof:
raw-Weyl path escape and rank, the repaired one-step ramp, the 19-adic
direct theorem, one-shear no-go, the classical stability sum, exact
history/reconnection identities and the universal encounter coefficient
envelope.  All other old `[PROVEN]` labels remain historical until a
separate current-source audit promotes them.

In particular, the later maintained shadow-tube audit continues to govern
over the old TUBE-SAT label, and no Naimark/cylinder/Dolgopyat chain is treated
as a completed BGS bridge merely because the working state used that label.
