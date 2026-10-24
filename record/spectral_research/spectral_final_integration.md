# Final spectral research corpus: integration and mathematical review

**Later scoped update:** the TRACE-109/110 qualifications below were closed in the
[22 October review](trace_closure.md). This dated record preserves the earlier verdict.

Date: 21 October 2026. Review provenance: direct reconstruction and author
self-review in this session. No independent external referee or new Lean
formalization. **The original fixed-coupling pair defect, all-order hierarchy
and BGS remain open.** Source preservation is complete for the supplied
bytes; semantic proof review has the bounded scope stated below.

## 1. Input, completeness and scientific organization

Final attachment: `Spectral_research_master (3).md`, **8,849,820 bytes**,
262,600 newline-terminated lines, SHA256
`b035e30034b20c60a8ced1d28a072767c1ea7afc5deaeea545aa20730e1948cb`.
The previously reviewed attachment (2), SHA256
`10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef`,
occurs once byte-exactly inside this final source. Rounds 13 and 14 are added.
Comparison base: main `2dccc8fc4e562cff0742e5ef2bdb589148bb6b1c`.
The local working tree is an authenticated partial overlay, not a full clone.

The edition has **535 source units**, including nested legacy sources:

| Material | Units | Reading location |
|---|---:|---|
| Author proofs, exact countertests and unsuccessful research attempts | 179 | [Thematic proof edition](../../mathematics/spectral_research/README.md) |
| Author/internal audits, reports, checkpoints and research records | 222 | `record/spectral_research/sources/`, indexed by topic |
| Reference code | 76 | [Reference program guide](../../computations/reference/spectral_research/README.md) |
| Author execution receipts, data and editorial patches | 56 | `evidence/executions/20261021/spectral-final/author/` |
| Expanded historical book containers | 2 | Front matter plus individual leaf sources, not a duplicate primary monograph |

There are 403 Markdown sources in all. The ten topic pages provide a scientific
account and individual source links. The [catalog](catalog.json)
maps original paths, source hashes, current paths and review statuses.
[Section inventories](sections/README.md) locate the arguments
within each source. The [proof review matrix](review_matrix.md)
distinguishes adoption from preservation. Failed routes and limitations are
retained as research outcomes, rather than silently discarded.

All original master bytes are independently recoverable from six ordered
compressed parts. Each source has an exact slice of that master, so a reading
projection cannot destroy provenance. The rebuild/check tool verifies every
slice, target and projection hash without needing the user attachment.

## 2. Current adoption and dependency closure

| Unit | Current disposition | Decisive scope |
|---|---|---|
| Physical single-kick decay, earlier round 12 | TRACE-106, previously integrated | The maintained positive-square localization strengthens $1/25$ to $1/9$; original mixed powers are not covered |
| Polynomial approximation | TRACE-107, previously integrated | Every fixed factorial order; one approximation sequence, all aliases, adjoint convention for a nonunitary approximant |
| Four-sheet diagonal return and quartic coefficient | [TRACE-108](../../mathematics/fixed-map/coordinate_return_quartic.md), analytic proof reconstructed and self-reviewed | Exact modular normalization, finite-time phase/transport, cross-sheet aliases, explicit quartic coefficient and fixed-coupling remainder |
| Protected actions and one-step trace | Source fully read; action checks replayed | Trace asymptotic retains the older plane-amplitude/odd-sector construction; not promoted as a fully independently closed input |
| Whole protected-sector removal | Source fully read; implication checked | From $|Q_m|\le20(83/200)^m$, weighted pair removal is $O(N^{-1})$ with cross terms; the uniform exact-sector bound retains its older analytic construction |
| Inserted trace and two-copy obstruction | [TRACE-109](../../mathematics/inserted_trace_coboundary_20261021.md), conditional asymptotic application | Projection and superoperator identities proved for arbitrary multiplicities; no differentiation of an uncontrolled trace remainder |
| Spectral orbit distance | [TRACE-110](../../mathematics/spectral_orbit_distance_20261021.md), conditional | Exact scalar-root and phase-count lemmas; quantitative application requires the original uniform physical trace bound (T) |
| Full weighted initial gradient/Hessian | [TRACE-111](../../mathematics/pell_weighted_curvature_20261021.md), analytic proof reconstructed and self-reviewed | All weighted times and off-clock terms included; no moving eigenvalue branches; composite Pell dimensions |
| Early inflection and analytic window | TRACE-111 continuation | Positivity forces positive curvature by $O((\log N)^3/N^2)$; entire continuation uses inverse powers; fixed-$\tau$ value remains unknown |
| Round 13 coefficient-square resummation test | Direct exact countertest checked | Auxiliary $K=M^*$ has flat Weyl coefficients and uniform single-kick spectrum but $KM=I$; not a physical counterexample |
| Round 14 full weighted residual | Direct signed decomposition and error budgets checked | Off-rotation sum must produce a negative plateau constant; actual original cancellation not proved |
| Final arithmetic attempt | Direct valuation/hopping/commutator derivations checked; exact check replayed | Does not turn seven-adic depth or rational $\tau N$ into a physical spectral cluster |
| Hierarchy-to-process step | Existing TRACE-086 retained | Every fixed order and every fixed band suffice; no extra local UI premise |

This is not a blanket certification of the 179 source proofs or the 222
internal review records. The older all-time analytic amplitude/cocycle/pressure
chain and historical spectral-simplicity branches are preserved with their
hypotheses and author review history. Their existence or a later author
verdict does not automatically certify their full dependency closure here.
No new “proved” status is inferred from a finite PASS.

## 3. Corrections and six historical source-version exceptions

Of 535 explicitly declared source hashes, 529 reproduce the declared original
hash byte-for-byte. Six included legacy revisions differ from their earlier
declared hashes; their actual uploaded bytes, actual hashes and archive offsets
are preserved. This is a version qualification, not evidence of a false theorem.

| Historical source | Treatment |
|---|---|
| `research_round2_2026_10_20/adversarial_oldspace_audit.md` | Preserve included revision and its actual hash; master documents an earlier form-feed/TeX repair |
| `research_round2_2026_10_20/fermionic_pseudoorbit_cutoff.md` | Preserve included revision; original declared hash not recovered |
| `research_round2_2026_10_20/fermionic_resolvent_frame.md` | Preserve included revision; original declared hash not recovered |
| `research_round2_2026_10_20/fermionic_twisted_pressure.md` | Preserve included revision; master documents an earlier backspace/TeX repair |
| `research_round2_2026_10_20/fermionic_weyl_return_windows.md` | Preserve included revision; original declared hash not recovered |
| `research_round4_2026_10_21/root_exact_identities_and_closure.md` | Included revision repairs a missing backslash in a sum; reversing that repair reproduces its historical hash |

The Markdown reading projection converts explicit legacy math delimiters
outside code, replaces unsupported `psmallmatrix` by `pmatrix`, and groups
two repeated-argument tuples before indexing. The initial projection exposed
19 KaTeX errors. Correct conversion also protects TeX row spacings such as
`\\[4pt]`; these must not be treated as opening display delimiters.
After repair, all explicit imported mathematical segments parse. Fifty master source-ID links and the original source-relative program/data links
are redirected to the individual edition targets. Original
code and archived source bytes are unchanged. No browser rendering of every
historical page is claimed.

## 4. Actual computational verification

**56 research Python checks pass at their stated finite scope.** Eleven
document builders are retained but not executed as proof checks. Wolfram
sources and their historical responses are retained; no Wolfram kernel was
run here. There is no new Lean or C++ compilation claim in this integration.

The first pass had 49 successful runs out of 55 selected checks. The six
failures were missing historical snapshots, a required CLI argument or a
pre-editorial source hash. All six were replayed with explicit contexts.
The separately inspected exact unipotent checker adds 186,042 finite assertions.

The maintained disposable-workspace replay reproduces all 56 checks from the
source archive. Its first packaged run passed 55/56 because `mpmath` was absent
from that interpreter's default import path. With the documented dependency
path supplied, the complete packaged replay passes. Both receipts are retained.
The coordinate audit runs against its exact pre-editorial input hash, restored
by reversing the recorded carriage-return patch; it is not claimed to have
checked a different hash. The global endpoint probe is only `--n 3 --max-total 3`.

All original assert-based scripts run with assertions enabled. The additional
maintained Hessian verifier also passes under `python3 -O`, using explicit
exceptions: three artificial repeated-clock cases compare direct matrix
derivatives to the block identity with errors below $6\cdot10^{-14}$.
Those examples validate finite algebra, not the Pell asymptotic lower bound.

Resource limits, commands, inputs, exclusions, initial errors, retries and
fresh output are in the [execution packet](../../evidence/executions/20261021/spectral-final/README.md).
Source, math parsing, build and visual checks have separate recorded coverage.

## 5. Results outside this attachment and current remaining task

The prior main already contains the strengthened single-kick exponent and
the all-order polynomial estimate, their complete proofs, verifier, claim
IDs and manuscript section. They are linked from the new research hub rather
than duplicated as new discoveries. The earlier closure without separate UI,
the 16--19 October phase/Abel/Gaussian/Wick work, and the
[20 October toolchain record](../../archive/evidence/executions/20261020/toolchain-followup/README.md)
remain in their dated sections. This edition preserves those baseline blobs.

The previous handoff task relied on repository pointers for its closure audit.
The [new independent task](../remaining_breakthrough_task_20261021.md) supplies
the full matrices, Fourier conventions, every-order target, CUE reference,
finite Laplace comparison, first pair defect, exact signed residual and the
limits of the new curvature results. It requires no file access.

The substantive open quantity is still the complete signed Heisenberg-scale
comparison for the unchanged deterministic propagator. No proof of its pair
limit, fixed-test physical countersequence or all-order law has been obtained.
