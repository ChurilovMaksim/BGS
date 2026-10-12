# Conditional clock law at every fixed order, 11 October 2026

The [all-fixed-order theorem](../mathematics/conditional_clock_universality_20261011.md)
extends TRACE-060 from the preceding fourth-order checkpoint. For every
fixed L it controls all incoming/outgoing diagonal powers through L, their
off-diagonal entries and every mixed entry S(uT/N)^r, uniformly down to
ceil(log(2N)^(1+kappa)). The statement is an intersection-probability bound
on the all-time entry-flat event. It does not bound the probability of that
event or condition phase averages on a future good event.

Two original finite-word assertions were false. An omitted retained endpoint
in an even alternating diagonal word has a leading contribution. It is
compensated by the two-boundary word after lower diagonal moments are
replaced by their references. The remaining positive-gap count gives the
coefficient k/q in the triangular forcing. Also, two-boundary interior words
need not contain a small lower clock endpoint. Their complete raw second
moments instead use an averaged product of two scattering intensities.
The [review packet](../evidence/executions/20261011/clock-universality/README.md)
preserves the uncorrected input and records both repairs. The general
local-envelope closure uses fixed p chosen after fixed L, with predictable
stops and complete crossing states. It is not a growing-order theorem.

The resulting [full-depth measure](../mathematics/full_depth_clock_measure_20261011.md)
is explicit. For x=u/N it has continuous density
sqrt((b_x-h)(h-a_x))/(2 pi h(h-x)), where
a_x=3-x-2 sqrt(2(1-x)), b_x=3-x+2 sqrt(2(1-x)),
and an atom (2-1/x)delta_x when x>1/2. Its moments solve the triangular
clock evolution. At x=0 the moments are the known Schröder sequence;
the known inverse-Jacobi family provides an exact reference comparison,
without proving freeness of any actual matrices.

Independently of entry flatness, the embedding product yields
T_u=I+X_u*X_u, rank(T_u-I)≤N-u, and thus a finite empirical atom at x
of mass at least (2-1/x)_+. The reference saturates this lower bound.
No equality of finite rank for an arbitrary starting unitary is claimed.

Finite controls reproduce reference polynomial identities through order
eight in exact arithmetic. Forty high-precision quadratures also include
the atom and the critical x=1/2 density. Their manifests distinguish the
exact identities from numerical diagnostics and from the analytic proof.
The fourth-order packet retains its separate Python, C++ and Wolfram scopes.
No new Lean proof of the stochastic induction is asserted.

The [entry-flatness outcome](entry_flatness_route_20261011.md) prevents a
specific shortcut: small centered singular norm plus small entries of a
doubly stochastic matrix need not give an O(1/u) two-step transition
kernel. That classical witness is not claimed unistochastic. The direct
amplitude martingale bracket also fails to provide a vanishing all-path
union estimate at the required scale from flatness alone.

All-time entry-flatness probability, typical complete physical TRACE-055
cavity hypotheses, scalar microscopic identification, signed TRACE-005
and global deterministic BGS remain open. The accepted clock result removes
the fixed-order equality induction from that list; it does not remove the
remaining probability or microscopic implications.
