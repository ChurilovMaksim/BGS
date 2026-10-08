# Bohigas–Giannoni–Schmit research programme

**The fixed-strength deterministic microscopic BGS problem remains open.**
This repository develops exact arithmetic structure, signed trace reductions,
quantum return laws, controlled noisy comparisons, analytic inequalities and
finite certificates. Each result states its model and its remaining boundary.

[Русская версия](README.ru.md) · [Research brief](RESEARCH.md) ·
[Theorem index](mathematics/results.md) · [Claim ledger](record/claim_ledger.md)

## The problem and the maintained model

BGS asks when the local spectral statistics of a classically chaotic quantum
system follow the random-matrix law appropriate to its symmetries. A precise
claim needs a semiclassical family, symmetry reduction, unfolding, and tests
at every fixed correlation order. Arithmetic and conjugacy exceptions must
be addressed in that formulation.

The maintained nonlinear toral map uses odd N≥3, the ordinary Weyl convention,
S=[[3,4],[2,3]], and the fixed propagator

$$U_N=e^{i\tau N A_N}M_N,\qquad \tau=10^{-80}.$$

The exact symbol, metaplectic matrix, exceptional dimensions and symmetry
conventions are specified in [the frozen-model proof](mathematics/fixed_map_resolvent_frontier.md).
The coupling stays fixed in this target. A necessary/reference pair test is

$$N^{-2}\sum_{n\ge1}e^{-2sn/N}|\operatorname{Tr}U_N^n|^2
\longrightarrow\frac{1-e^{-2s}}{4s^2},\qquad s>0.$$

The complete target is the **signed Heisenberg-scale factorial joint-trace
comparison** for every fixed order and compact smooth Fourier weight
([TRACE-005](mathematics/open_questions.md#b-prove-heisenberg-scale-desymmetrized-joint-trace-estimates)). Its modulus is
outside the complete sum. Pair control, short-time traces, phase averages,
noise limits and global observable laws have their own scopes.

## Latest proved continuation: 8 October 2026

[The research checkpoint](record/research_checkpoint_20261008.md) audits the
latest attached manuscript, supplies complete proofs and records unresolved
inputs. Three results are integrated:

| Result | Exact conclusion | Boundary |
|---|---|---|
| [TRACE-053: max-entry phase memory](mathematics/max_entry_phase_channel.md) | For uniform coordinate phases reused at every return, channel error ≤(n!−1)√δ+n!n(n−1)δ; averaged traceless eigenbasis pinching is O(log log(1/δ)/log(1/δ)) under an intensity singular gap | Channel operator norm does not evaluate the microscopic superoperator trace |
| [TRACE-054: sharp matrix inner jets](mathematics/sharp_inner_jet.md) | For rational matrix inner F=zG, the right-weighted second-jet energy has optimal universal leading coefficient 4/3, improving the submitted 13/3; smooth localization includes its exact derivative penalty | A physical cubic-delay moment and stochastic covariance still need separate proofs |
| [TRACE-056: direct real-flow scalar transport](mathematics/phase_channel_real_flow.md) | Eigenphase matching and normally absorbed scalar-source L1 comparison along a real unitary flow, including each fixed source derivative | The anisotropic physical source, mixed products and scalar endpoint law are separate obligations |

The submitted TRACE-055 polylogarithmic deep-source hierarchy is
**verification-pending**. Its joint delay barriers, killed moment and
physical-source covariance/continuation have not been reconstructed. Even
that hierarchy would require identification of its actual scalar cavity law.
The [source review](literature/phase_channel_jet_sources_20261008.md) makes no
external-priority or prize-level claim.

## Established families and the remaining spectral gap

The fixed-model programme includes actual position-chain mixing and cyclic
path control (FM-021), reverse-cyclic suppression (FM-022), the odd-dimensional
common-commutant classification with the N=7 exception (FM-024), selected
weighted and ordered-diagonal factorial sectors (TRACE-019/020), and scoped
balanced/offcharge low-switch removal (TRACE-021).
The complete unmasked convex insertion hierarchy is proved in
[TRACE-028](mathematics/right_frame_unmasked_pinch_hierarchy.md);
[TRACE-029](mathematics/convex_pinch_weak_noise_and_deconvolution.md) gives
bounded-u signed stability and an actual unsigned logarithmic obstruction.

The unresolved work is the actual complete balanced microscopic law,
signed marked/high-switch and undamped comparison, the absorbed Ward overlap,
and every-fixed-order TRACE-005 hierarchy. New subsidiary proofs change these
obligations only where an explicit theorem supplies the needed input.
[The obligation board](mathematics/open_questions.md) keeps exact statements.

Parallel families cover Cayley finite-field geometry, Pell/Floquet dynamics,
return laws, resonance and cohomology, locality, spectral obstructions, and
information-theory applications. [Thematic reading paths](mathematics/topics/README.md)
state their hypotheses and dependencies.

## Reading and reproduction

The scientific authority is [the claim ledger](record/claim_ledger.md), followed
by [stable claim metadata](record/claims.json) and the canonical mathematical
proof files. [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md) resolves disagreements.
The single maintained publication root is
[manuscript/BGS_unified.tex](manuscript/BGS_unified.tex).

The new continuation has independent internal proof reconstruction, a compact
[execution packet](evidence/executions/20261008/phase-channel-jet/README.md),
Python orientation/quadrature controls, exact C++ occupation counts, Wolfram
identity checks, and an aggregate Lean 4.33.1 build of all 20 active modules.
The new Lean lemmas certify coefficient arithmetic; the analytic proofs and
BGS are not formalized. Older native-evaluation certificates retain their
explicit trust boundary.

```sh
python computations/verification/phase_channel_jet.py
c++ -std=c++20 -O2 -Wall -Wextra -Werror computations/cpp/phase_occupation_jet_verifier.cpp -o /tmp/bgs-occupation
/tmp/bgs-occupation
(cd formalization && lake build)
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

[Computation guide](computations/README.md) · [Formalization scope](formalization/README.md) ·
[Manuscript build](manuscript/README.md) · [Reader background](docs/reader_guide.en.md)

Historical evidence is indexed and retained with its original provenance.
The 8 October review is scoped; it does not certify every earlier proof or
report a full rerun of all historical verifiers.
