# A restoring mechanism beyond the static obstruction

Research outcome, 12 October 2026.

[TRACE-075](../mathematics/two_step_restoring_drift_20261012.md) proves an exact
one-step fresh-phase formula for the two-step intensity kernel \(K=P^2\).
The complete coherent contribution is a weighted pairing of a three-step
path amplitude with the amplitude obtained by swapping its two internal
vertices. Cauchy--Schwarz bounds that contribution by \((P^3)_{ij}\).
The proof keeps both nonzero-deleted-diagonal cubic phase terms.

For an arbitrary unitary input with \(\delta=\max P\le1/16\), choosing a
coordinate uniformly among all \(u\) labels and freezing \(K_{ij}\) if an
endpoint is removed gives
\[
 \mathbb E(\Delta K_{ij}\mid S)
 \le[-K_{ij}/2+5(P^3)_{ij}+2\delta P_{ij}]/u.
\]
The subtraction belongs inside the survivor-coordinate sum. This repairs
one ambiguous averaging sentence in the original candidate; the candidate's
subsequent base-loss calculation had already used the correct convention.

The [unitary obstruction](unitary_two_step_continuation_20261012.md) is
therefore complemented by a positive dynamic result. At those constructed
states \(P_{ij}=0\), \(K_{ij}\sim\log(2u)/u\) and
\((P^3)_{ij}=(1+o(1))/u\). The exact mean satisfies
\[
 \mathbb E(\Delta K_{ij}\mid S)=-(1+o(1))K_{ij}/u.
\]
Thus the static obstruction does not remain an obstruction to the mean
drift: a fresh random elimination tends to restore its selected peak.
The conclusion is about a single conditional mean, not sustained or
high-probability decay.

The main theorem is self-contained finite unitary algebra. TRACE-074 is
an input only to the higher-step comparison and the constructed-state
corollary. [The execution packet](../evidence/executions/20261012/two-step-drift/README.md)
records independent mathematical reconstruction, three exact rational
phase-product residue controls and four ordered pairs in an explicit
64-dimensional unitary with max intensity \(1/50\). Those controls
are not an asymptotic probability proof.

For a general logarithmically flat state, the forcing term also contains
\(\rho(\delta-1/u)/u\), where \(\rho=\|P-J_u\|_{\rm op}\).
We have not bounded \(\rho\log u\) for the maintained evolution, nor proved
the higher-moment and stopped concentration estimates required to control
all entries and times. These are genuine unresolved implications. All-time
flatness probability, full physical TRACE-055, signed TRACE-005 and BGS
remain open. No analytic Lean or priority claim is made.
