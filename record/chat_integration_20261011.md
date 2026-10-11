# Checked research integration, 11 October 2026

## Result and remaining global problem

The main new deterministic conclusion is maximal microscopic stability of
the complete common-origin local point process under a fixed smooth observable
flow. If A_T is the T-step Heisenberg time average and v=||A_T||F/sqrt(N),

$$E_\phi\sup_{|x|\le R}d_L(\Xi_N(x),\Xi_N(0))
\le Rv/\pi+C^2R^2(T-1)/(2\pi N).$$

The maintained frozen map supplies v=O((log N)^(-1/2)) for each fixed smooth
exactly centered symbol, so every R=o(sqrt(log N)) is allowed. The time-average
endpoint transfer itself is prior corpus work; the maximal path and growing
interval are the strengthening. A common random observation origin is part
of the statement. It neither evaluates the initial local law nor removes the
noise used for Dyson relaxation.

The phase-channel counterpart gives maximal full point-process transport
under endpoint flatness and gap, on R^2 loglog(1/delta)/log(1/delta)->0.
Normal-source transport extends to every fixed Lp, derivative and mixed
product; physical anisotropic transport is only asserted in L2. These proofs
were independently audited internally, including eigenspace multiplicities,
random-past conditioning, topology, constants and growing-interval errors.

## Complete disposition of the retained branches

| Stable claim | State | Authoritative source | Exact boundary |
| --- | --- | --- | --- |
| BGS-TRACE-057 | PROVED | [Arbitrary-source phase covariance](../mathematics/source_covariance_20261011.md) | The arbitrary complex source bound is an exact contraction theorem; it does not identify a microscopic reference law. |
| BGS-TRACE-058 | PROVED | [Integrable all-order phase absorption](../mathematics/integrable_phase_absorption_20261011.md) | Every fixed Lp absorption bound and Abel continuity; no uniformity as p grows and no local-law identification. |
| BGS-TRACE-059 | PROVED | [Anisotropic physical-source transport](../mathematics/physical_source_transport_20261011.md) | Phase-independent positive clock, trace m, bounded normalized second moment, endpoint flatness and gap. L2 scalar comparison and fixed derivatives only; no higher physical-source mixed moments or actual-cavity hypotheses. |
| BGS-TRACE-060 | CONDITIONAL | [Joint incoming and outgoing delay bootstrap](../mathematics/delay_bootstrap_20261011.md) | Conditional on all-time entry flatness down to log(2N)^20 (or stated log(2N)^(5+kappa) scale). Joint delay barriers and killed second/third upper bounds; probability of flatness and equality moment laws are not proved. |
| BGS-TRACE-061 | PROVED | [Finite frame identities, Stiefel threshold and clock-basis obstruction](../mathematics/fresh_phase_average_20261011.md) | Exact finite controls and the specified Haar-frame comparison model. A constructed clock/basis obstruction at one phase point is not a typical phase-ensemble or literal-map counterexample. |
| BGS-TRACE-062 | PROVED | [Flat completion with arbitrary clock law](../mathematics/flat_completion_20261011.md) | Constructed flat unitary completions and a prescribed mean-one clock law; no independently sampled phase-ensemble violation and no change-free counterexample to the maintained quantization. |
| BGS-TRACE-063 | PROVED | [Global noncommuting ordinary-body coercivity](../mathematics/nonlinear_coercivity_20261011.md) | Strict matrix balls, intensity singular gap, exact determinant defect and source derivatives. Ordinary-body coercivity alone does not control the entire graded integral. |
| BGS-TRACE-064 | PROVED | [Sharp maximal-torus contraction for compact simple groups](../mathematics/torus_contraction_20261011.md) | Central L2 functions under Haar sampling, sharp 1/(h+1) variance factor. A chosen deterministic scattering matrix and circular symmetric spaces require separate statements. |
| BGS-TRACE-065 | PROVED | [Signed finite-field cycle and collision calculus](../mathematics/coherence_form_factor_20261011.md) | Explicit finite-field Fourier scattering with reused independent phases. Leading ramp n=o(N^(1/8)); symmetric first correction n=o(N^(1/9)), not N^(1/7), not Heisenberg times. Dihedral occupation sector alone does not provide the plateau. |
| BGS-TRACE-066 | PROVED | [Birthday rank law and thinned collision limit](../mathematics/previous_rank_results_20261011.md) | Recovered proof of the rank/collision coupling, specified Poisson TV bound and stated CLT window. An unsaved proposed N^(1/7) correction is explicitly unconfirmed; no variance asymptotic inferred from L1 coupling. |
| BGS-TRACE-067 | PROVED | [Sharp balanced Laurent Jack coefficient bound](../mathematics/jack_coefficient_theorem_20261011.md) | All alpha>0, nonzero balanced signatures and K>=1: ratio at most 1/(N+alpha K); unique sharp highest-root mode. External priority is not established. |
| BGS-TRACE-068 | PROVED | [Frozen circular phase laws in the three symmetry classes](../mathematics/phase_contraction_20261011.md) | Haar circular background frozen once, randomness then only in compatible phases; spectral L2 functions, paired CSE phases and half trace. Full conditional weak Sine-beta limit in probability over the background. No prescribed deterministic-background theorem or Sine-limit rate. |
| BGS-TRACE-069 | PROVED | [All-order critical CSE trace limit](../mathematics/exact_cumulants_20261011.md) | Growing n/N->1, d=o(N), logarithmic critical variance, every fixed cumulant and mixed moment, conditional Gaussian law. Second/fourth cumulants are prior HSW formulas; no independent-block interpretation or external novelty certificate. |
| BGS-TRACE-070 | PROVED | [Complete CUE and CSE form-factor curves](../mathematics/form_factor_curve_20261011.md) | Mean L2(0,T) convergence of the ceil(N*tau) interpolation and all-time individual CSE MSE control. No expected temporal supremum; floor interpolation with n=0 is excluded. The limiting curves are prior work. |
| BGS-TRACE-071 | PROVED | [Maximal phase point-process paths and all fixed normal-source products](../mathematics/laplace_path_transport_20261011.md) | Full centered point-process path comparison on R^2 loglog(1/delta)/log(1/delta)->0; all fixed normal-source Lp products and derivatives. Random clock is conditioned on the phase-independent past. No initial law, no Lp norm of a continuous supremum, no higher physical-source product assertion. |
| BGS-TRACE-072 | PROVED | [Deterministic maximal microscopic observable flow](../mathematics/deterministic_path_transport_20261011.md) | Finite-N maximal path bound under one common observation origin. Actual-map growing interval o(sqrt(log N)) uses FM-018 mixing/Egorov and a fixed smooth exactly centered symbol. The time-average endpoint mechanism is prior corpus work; the initial law and BGS remain open. |

The stronger all-moment bootstrap, fourth-delay law and Schröder clock-law
induction are retained under [research_candidates/20261011](research_candidates/20261011/README.md).
Exact phase-feedback words were checked; the full asymptotic induction is not
promoted. The killed second/third moments are upper bounds, not equality laws.
No probability for the all-time entry-flatness event has been established.

## Corrections and prior overlap

- The rigorous symmetric first-collision window retained here is n=o(N^(1/9)).
  A proposed n=o(N^(1/7)) checkpoint lacks a recoverable proof and is unconfirmed.
- Haake--Sommers--Weber already proved the recovered CUE variance, CSE second
  and fourth cumulants, and limiting form-factor curves. The all-order critical
  derivation and frozen compatible-phase statements have their own proof scope;
  worldwide priority remains unestablished.
- CSE uses N paired phases and a half trace, not 2N independent phases.
- Mean L2 convergence of an entire form-factor curve does not imply a temporal
  supremum bound. The interpolation is ceil(N*tau); floor creates a spurious
  n=0 cell. The logarithmic critical peak is L2-integrable.
- The sharp compact-group result concerns central Haar functions. The circular
  orthogonal and symplectic statements use their separate spherical-function
  proof, not a substitution of Haar SO or Sp.
- General nuclear-norm spectral transport is already a corollary of FLOW-015
  and FM-007; it is not advertised as a new mechanism. Operator-norm o(1)
  perturbations can change microscopic laws in other families.
- Flat clock completions and same-ensemble clock examples change the quantum
  family or inspect one phase point. They do not refute the literal fixed map.

## Scope of review and execution

The full current remote tree was materialized and every one of its 4294 Git
blobs checked byte for byte before editing. Parallel editorial changes through
8 October were preserved. Original inputs, failed development controls,
successful bounded Python/C++ receipts, Wolfram sources and receipts, and Lean
drafts are preserved in the [dated packet](../evidence/executions/20261011/chat-research/README.md).
New executions and formal compilation are recorded separately after integration.
An old receipt is never rewritten to make it appear to cover new source paths.

This is internal mathematical review, not external refereeing. Finite exact
controls establish their enumerated cases, not the asymptotic theorems.
The complete signed Heisenberg TRACE-005, actual balanced phase law, deterministic
noise removal and general BGS conjecture remain open.

The original complex-source proof is a hash-pinned Wave2 input. Its dated pending-review header and early filename are retained as historical bytes; the current accepted review status is TRACE-023 in the ledger, reaffirmed by the 11 October source audit. Its status is not inferred from that old header. The current uniform Abel source is uniform_phase_pair_abel_bound.md.

An exact Walsh-clock control in the maximal deterministic proof has c_N(k)=0 for every 1<=k<N and v_N,T^2=1/T, yet its initial local process is an exact translated lattice. This is an abstract even-dimensional family, not a smooth observable quantization of the maintained Anosov map. It pinpoints why fixed-time observable decorrelation and maximal local stability cannot identify the missing initial spectral law.

The current claim integration epoch registers TRACE-057–072 explicitly. The historical Wave2 external leaf is retained as an exact-byte baseline, and its 39 original contracts are compared field by field against the extended registry. The new seven dependencies belong to this review, not to the earlier sealed proof audits. Five negative controls reject historical byte changes, locator changes and undeclared additions.

The new time-average estimate obeys |v_T(V,B)-v_T(U,B)|<=C(T-1)||V-U||op. The prior microscopic-rounding family therefore retains every fixed smooth observable's logarithmic maximal-path conclusion while violating its fixed signed CUE pair target. This extends the explicit insufficiency test to the combined coarse controls and maximal paths. The rounding construction is prior corpus work and changes the exact propagator; no literal-map counterexample is claimed.

## Final execution coverage

The corrected complete Python/C++ workspace run passed **217/217** checks, with identical before/after source fingerprints. The maintenance suite passed **236 tests**. All **24 C++ targets** were freshly compiled in Release mode. Bibliographic audit passed **416 mutation controls** and matched all **46** source identities. Lean compiled **23 active modules / 26 Lake jobs** at its finite algebraic scope; the new Mathlib draft remains uncompiled. Wolfram independently checked the finite integer Walsh matrices and rational window identity. Exact circular controls, full run outcomes, source hashes, corrected failures and compilation logs are in the [fresh execution packet](../evidence/executions/20261011/chat-research/fresh/README.md).

The complete workspace receipt covers the source snapshot recorded in its source_manifest. After that run, only documentation, proof exposition, claim proof-path metadata, whitespace policy for immutable engine logs and newly promoted receipts were edited; executable verifier sources, C++ sources and Lean sources did not change. Those final editorial changes are checked separately and the remote CI verifies the final committed tree. No execution result is a certificate of the analytic BGS conjecture.

The final manuscript has **284 pages**, with the new chapter pages 278–281 visually inspected. Both the preceding and final build receipts retain their actual TeX source hashes; the final build includes the rounding-continuity corollary.
