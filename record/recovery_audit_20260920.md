# Recovery audit and research handoff

Date: 20 September 2026. Base: `d75b7cb04b60cd780a8d4ac8da62225e1c91477e`.
Primary verdict: **incomplete, with the fixed-model Heisenberg-scale
cancellation estimate still missing**. This is a scoped self-review,
not a fresh independent audit of the entire mathematical corpus.

## What was actually recovered

The connected repository and the latest clean local checkout agree at the
base revision. Commit `3139f47` already integrated 115 supplementary files,
the fixed-map chapter, computational replay and the new Lean source.
The next commit recorded CI failure before execution. Thus the previous
publication request was substantially completed, despite the earlier chat
describing the work as unpublished. Historical checkpoint prose is not the
current publication status.

Prior-conversation retrieval supplied selected excerpts, not a complete
transcript. The full uploaded `research-summary (1).md`, current proof files,
claim ledger, dated reviews and the actual working copies were read. No
claim is made that every message of the previous conversation was retrieved.

A second, older checkout had an uncommitted patch on snapshot `2ba0d65`.
Fourteen text-source changes were absent from current main. They comprise
Cayley quantifier corrections, a characteristic-two-safe polynomial formula,
elliptic proof clarifications, a separated-cluster estimate and verifier,
and a short-trace counterexample. These amendments have been recovered.
Only the new counterexample was inserted into the trace bridge: its newer
bandlimit-extension theorem and subsequent research must not be overwritten
by the older file. The older regenerated PNG and finite JSON were not copied
as new research; fresh finite evidence is generated from the recovered source.

## Mathematical map

| Layer | Safe conclusion | Missing implication |
|---|---|---|
| General hyperbolic return laws | Project proofs for explicit arithmetic subsequences and stated weak-kick regimes | Transfer to a fixed nonlinear map at Heisenberg times |
| Compensated family | Operator comparison and recovered averaged form-factor obstruction | Does not treat the frozen fixed-strength model |
| Report audit | Corrected CUE references and normalization counterexamples | No spectral universality follows from sparsity alone |
| Algebraic returns | Exclusions with exact hypotheses and finite certificates | Simplicity and return exclusion do not quantify local statistics |
| Determinant ratios | Exact Abel/pair reduction; covariance-only target refuted | Estimate the actual microscopic ratio derivative |
| Mixed loops | Exact finite identities and conditional all-order criterion | Prove mixed residual decay for the prescribed propagator |
| Lean | Historical 16-module builds; new integer kernels in source | Current 17-module compilation remains unverified |

The early uploaded summary must not be used as a theorem ledger. In
particular its unitarity-only resonance suppression loses a dimension
factor, its zero higher-order target disagrees with CUE, and unrestricted
claims about scalar-only unitary symmetries are false. These corrections
already have detailed proofs in the preserved report audit.

## Recovered proof audit

1. **Quantifiers.** A bound `P(K)<=K^(4+o(1))` excludes primes with
   `K<=p^(1/4-epsilon)` for fixed epsilon>0. It need not exclude primes
   with only `K=o(p^(1/4))`: an allowed subpower loss can dominate `p/K^4`.
   An `O(K^4)` bound suffices for that stronger regime. All recovered
   dependent proposal statements now retain this distinction.
2. **Integral polynomial.** Define `2^m F(Z/2)` coefficientwise as
   `sum_j 2^(m-j) f_j Z^j`; the notation then makes sense in characteristic
   two without division. Explicitly require `F` to be monic over `R`.
3. **Cluster bound.** For odd K>=3, D=Kn, n phases per arc of radius
   eta<=1/(4K), and M consecutive times of maximum absolute value L,
   splitting ordered pairs gives

       |mean(|Tr U^ell|^2/D)-n|
         <= 8 pi^2 n L^2 eta^2 + (2D/M) H_((K-1)/2).

   Within-cluster loss uses `1-cos(t)<=t^2/2`. Between-cluster pairs use
   circular separation at least h/(2K) and a geometric sum. The application
   uses constant Riesz-projection ranks along the norm-small homotopy,
   eta<=delta_N/4, N delta_N->0 and K=O(log N). Thus the averaged mean is
   `(d_N/K)(1+o(1))` for the stated compensated family. This remains a
   consequence of the project's parent operator estimate, not a new proof
   of that estimate or a result for fixed classical coupling.
4. **Short-trace control.** For N=2M, the N-clock and the twice-repeated
   M-clock have identical traces for 0<abs(m)<M, but pair tests supported
   in (-1/2,1/2) with value one at zero give respectively 0 and 1.
5. **Elliptic input.** The arithmetic open image contains a congruence
   subgroup; the geometric image contains its commutator because the
   constants quotient is abelian. BLV Lemma 4.1 supplies an open subgroup
   in that commutator. Purity is asserted on the smooth locus; multiplicative
   stalks after normalization have eigenvalues +/-p^(-1/2).

Source verification used the literature-check workflow. BLV
[arXiv:0804.1425v2](https://arxiv.org/html/0804.1425v2), Theorems 1.3--1.4
and Lemma 4.1, was checked directly. The lemma's proof is a sketch referring
to a congruence-subgroup argument; it is an external input, not a new formal
proof here. FKM [arXiv:1210.0851v5](https://arxiv.org/pdf/1210.0851v5),
Lemma 3.5 and its proof, supplies the common-open correlation argument.
The earlier v1 link was unavailable, so the recovered citation is explicitly
pinned to v5. That source uses “pointwise pure” for purity on the lisse
locus; the revised wording clarifies this convention rather than claiming
the source's terminology is wrong. No novelty search or priority result
was undertaken.

## Next mathematical task

Keep the exact raw Weyl model and fixed `tau=10^-80` in
`mathematics/fixed_map_resolvent_frontier.md`. The concrete pair target is

    L_N(s)=N^-2 sum_(m>=1) exp(-2sm/N)|Tr U_N^m|^2
       -> (1-exp(-2s))/(4s^2),  for every s>0.

The full target additionally requires every fixed correlation order.
The mixed-loop hierarchy is one sufficient route. Its first equation
contains the cubic trace sum as well as L_N; it is not a closed equation
for the pair statistic. The second mixed level only yields a conditional
interval, not the CUE value. The next substantive advance must use the
specific deterministic dynamics to estimate these defects, or supply an
equally strong direct trace comparison. Replacing it by independent phases,
same-half-plane tests, short-time mixing, or finite numerical agreement
would leave the central implication unproved.

## Verification boundary

Fresh checks and recovery disposition are recorded in
`evidence/recovery_20260920/`. Structural/source checks and the 115-file
inventory audit passed before edits. Both source-to-TeX synchronization
checks passed. Two selected isolated replays, `resolvent-flow/checks.py`
and `resolvent-flow/low_order.py`, passed at the base revision. The
previous 121/28 execution counts are historical and are not represented
as a fresh full run in this audit.

No local Lean/Lake executable was found. The connected CI job record for
run `35525732662` still has empty step lists and no assigned runner; no
compiler error or successful build can be inferred. Its underlying cause
remains unknown. There is no justification for changing proof code or
downgrading workflow actions based on that record alone.

The recovery is prepared on a research branch because it spans several
scientific layers and the external CI gate has not run. Remote publication
of that branch does not promote it to main or certify the open mathematics.

Final local verification: the recovered cluster verifier passed 36 cluster
fixtures, including maximal permitted arc radius, positive/negative windows
and the single time zero, in addition to its original trace checks.
Repository structure and both TeX synchronization gates passed. The canonical
manuscript build passed its reference/overflow gate: 226 pages, PDF SHA-256
`5d7ccbda16b58fe3874bb389d076a8cf08bf917fbd39e48934c42ad049f9cef4`.
The first elliptic regression invocation lacked SymPy on the new worktree's
Python path; this environment error was resolved using the existing project
dependency directory. Its subsequent mathematical result is recorded in
`evidence/recovery_20260920/elliptic_regression.log`.
