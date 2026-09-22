# Research route checkpoint — 22 September 2026

Base for the new pass: `ChurilovMaksim/BGS@39d4e01ae6a6b3eb472ab30266b708ca71a70a16`.
Integration was reconciled against later `main@ac94d783f31208ae3916250b4b6381c4a77e65c0`.
The target remains microscopic random-matrix universality for natural
fixed-strength quantizations of chaotic systems, including all symmetry
reduction and unfolding. No route below has reached that target.

## Route tree and actual discriminating steps

| Route | Executed step and evidence | Disposition and next obligation |
|---|---|---|
| Finite signed frequency families | Reconstructed both pair-channel identities, large-gap separation, and common real all-pass factor. Independent internal derivation in `finite_orbit_secondary_review_20260922.md`; exact finite cross-checks in `evidence/20260922/`. | A maintained smooth finite-family theorem, claim `BGS-RES-004`. No family-uniform isolation threshold; arbitrary analytic infinite-orbit positivity stays `BGS-RES-003` OPEN. |
| Arbitrary smooth infinite-orbit extension | Compared with the existing Gevrey bump giving a pointwise-zero bracket, already in `manuscript/unified_sections/temporal_resonance.tex`. | The unrestricted smooth claim is false. The analytic case requires control of cancellations across infinitely many orbit families; truncation with merely strict positive variances is inadequate. |
| All-lag genericity via polynomial perturbation | Compared the proposed exterior-power determinant route against `mathematics/weighted_wiener_resonance.md`. | Already in the corpus. No novelty or duplicate theorem claimed. |
| Hyperbolic fixed-point Hessian obstruction | Compared the proposed quadratic resonant jet mechanism against `mathematics/resonance_nondegeneracy_and_hessian.md`, Section 4; checked `mathematics/local_jet_resonance_obstruction.md`. | The definite quadratic case was already proved. A strict but degenerate quartic local minimum can still have a bracket coboundary; local positivity alone does not settle the analytic torus problem. |
| Heisenberg-time fixed-map mixed loops | Examined `mathematics/fixed_map_resolvent_frontier.md` and its conditional hierarchy. The required residual estimate remains absent. | `BGS-TRACE-005` and terminal `BGS-BGS-001` stay OPEN. A repeated conditional moment calculation is not a model-specific cancellation proof. |
| Clustering to Abel transforms | Proved the positive Poisson-kernel inequality for arbitrary clustered unitary spectra and applied the existing compensated-family pinning theorem. | Exact consequence `BGS-TRACE-006`; no conclusion about the frozen fixed-strength quantization. |
| Clustering to positive-time windows | Constructed distinct macroscopically uniform spectra with collapsed spacing and divergent Abel energy but uniformly vanishing form factor on every positive Heisenberg-time window. | A proposed inference from spectral pinning alone is refuted. Future work must introduce a dynamical input valid for the actual map. |

The finite-orbit extension is a proof within a precise classical subfamily;
the clustered construction is an abstract spectral boundary. Neither supplies
the missing Heisenberg-scale joint-trace comparison. The next decisive
mathematical check is a model-specific estimate on mixed resolvents or all
relevant joint traces for the frozen operator, with every order and compact
Fourier support treated under fixed coupling. Source-level Lean and Wolfram
files are retained with their execution status explicitly stated.
