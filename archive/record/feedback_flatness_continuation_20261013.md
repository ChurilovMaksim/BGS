# Closing the feedback flatness probability

TRACE-080 proves a probability statement that was missing in the previous
deterministic-start feedback programme. Its hypotheses are explicit:
initial intensity at most C0/N, centered intensity singular norm at most
1/100, uniform retained ports and fresh independent uniform phases.
It controls the complete trajectory down to
`ceil(log(2N)^(4+kappa))`, with failure `O(log(2N)^(-1-kappa))`.

The decisive move is to control whole row and column fourth-power energies.
Their coherent forcing is bounded by the intensity singular norm times
their own centered energy, yielding a restoring drift at every depth.
These energy bounds control the complete three-step kernel. The all-pair
two-step drift/variance then closes its concentration, including the
diagonal; its bracket finally controls individual entry amplitudes.
All four arguments use one old-state stopping mask and retain the whole
first new crossing. Their exceptional events are combined by a union
bound, without conditioning on future flatness or endpoint survival.

TRACE-079 is the separately reviewed scalar concentration theorem used
in this chain. Its standalone shrinking-Green corollary has a reached
deep-range conclusion, not a survival probability. TRACE-080 adds the
row/column mechanism and proves survival under its smaller initial-gap
hypothesis. These are different scientific statements.

The clock theorem is used with `kappa_clock=3+kappa`, so its cutoff exactly
matches the new trajectory theorem. Every fixed clock order and the uniform
empirical weak law are now unconditional on that range for this startup
class. The reference atom and pathwise rank bound retain their original
meaning, without a new finite-N atomic equality. A separate reversal
corollary requires its initial channel norm to tend to zero. Named eventual
FM-021/FM-022 inputs supply the actual odd-N fixed-coupling application;
neither is re-audited in full here and no effective startup is claimed.

The original deterministic microscopic spectral law is still unevaluated.
The scalar physical-source reference, signed Ward/balanced identification,
TRACE-005 and BGS remain OPEN. Smaller general cutoffs, growing clock orders
and edge laws are also outside the new conclusion. Closing this auxiliary
probability premise is not a proof of spectral universality.

[Canonical probability proof](../mathematics/unconditional_feedback_flatness_20261013.md),
[canonical concentration proof](../mathematics/two_step_stopped_concentration_20261013.md),
and [independent audit/evidence](../evidence/executions/20261013/global-feedback-flatness/README.md)
separate the analytic argument, named internal inputs and exact/floating
finite controls. Classical Bernstein/Freedman and smooth Schatten methods
are credited; mathematical priority is not established.
