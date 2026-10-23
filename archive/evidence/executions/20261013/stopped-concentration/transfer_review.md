# Transfer check: maintained stopped concentration, 13 October 2026

**Primary verdict: proved as written.** The independent audit's verdict
transfers to the maintained TRACE-079 text. The formulas, constants,
quantifiers, stopping rules and concentration argument are unchanged.
The explicit startup definition repairs the identified expositional
ambiguity without strengthening the theorem or weakening its stopping
boundary.

## Exact input pins

| Artifact | SHA256 |
|---|---|
| Frozen candidate: `/workspace/scratch/06745ba532e4/research_session/two_step_stopped_concentration_candidate_20261013.md` | `47e365b06fa460e6d503b771b9b336403ee9a6e918e81d4a17b6c6be9a60aec7` |
| Maintained text: `/workspace/scratch/06745ba532e4/research_session/maintained_stopped_concentration_20261013.md` | `d215b3ac0aacb6243db40a61a6bb9530f0375c63cddcb6b5f9194667ceffc0ea` |
| Prior independent audit: `/workspace/scratch/06745ba532e4/research_session/two_step_stopped_concentration_independent_review_20261013.md` | `ac08090b2bd4d2dec0aaf81e9c367ba363b3e632428ef8a7494f6c5d52475e95` |

The frozen hash still matches the original audit input. This is a read-only
transfer check; no repository sources or claims were edited.

## Exact diff and logical check

The unified diff has only three hunks:

1. The candidate header and base description become the stable
   `BGS-TRACE-079` title and internal-review status.
2. `Gamma_b` is explicitly defined by reaching `b` without entry exit and
   satisfying **both** `delta_b<=K0 ell/b` and `max(P_b^3)<=2/b`.
3. A review/verification paragraph adds evidence and prior-structure links
   and explicitly distinguishes exact finite controls from the analytic
   concentration proof and from Lean/C++ certification.

An independent string comparison of the complete mathematical body,
from section 1 through section 5, passed after substituting only the
single `Gamma_b` clarification. Every S1–S16 statement, constant and proof
paragraph is therefore otherwise byte-for-byte unchanged within that body.

Both startup barriers are measurable from the history through `b` and are
already hypotheses of the finite theorem. On the TRACE-077 Green good
event, any entry-admissible reached `b` satisfies the second barrier. The
clarification therefore preserves the original union-bound inclusion:
the desired violation is contained in the Green failure or the auxiliary
scalar concentration failure. It introduces no conditioning on the future
Green good event, future survival, or the eventual retained labels. An
entry exit at or above `b` still leaves the later interval `m<=u<=d<b`
unreached, so the conclusion there is vacuous.

## Scope preserved

The review accepts the same all-pairs stopped bound, including diagonal
pairs, endpoint freezing, the full first crossing and simultaneous exits,
and the same `9/u` corollary on reached depths `m<=u<=d`. It accepts no
matrices after the first entry exit and no estimate for reaching the
range, all-time flatness, deterministic microscopic identification,
TRACE-005 or BGS.

The new verification paragraph is scope-limited and does not make its
finite controls a proof leaf. This transfer check did not rerun those
additional author/root controls or inspect their entire evidence packet;
the independent four-pair exact controls and the analytic proof review
remain recorded separately in the pinned prior audit. The prior-structure
link likewise adds no external concentration theorem dependency: the
scalar exponential estimate is still derived in the mathematical body.

## Actual verification

Read both files, computed their SHA256 hashes, inspected the complete
Python `difflib.unified_diff`, and asserted exact equality of the mathematical
body after the single startup-definition substitution. No new finite
mathematical computation, stochastic simulation, full regression or formal
compilation was required or claimed. No mathematical gap or scope change
was found in the transfer.
