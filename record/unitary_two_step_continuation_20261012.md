# The static gap shortcut fails already for unitary intensities

Research outcome, 12 October 2026, following clock commit
853bca79423cb1462926592609c911154ca486bd.

[TRACE-074](../mathematics/unitary_two_step_obstruction_20261012.md)
strengthens the preceding doubly stochastic obstruction to genuine
unistochastic matrices. Two rank-one corrections impose a matching sparse
row and column on a Haar unitary. The remaining completion is Haar on two
fixed orthogonal complements. The correction has rank at most two and
Hilbert--Schmidt norm at most \(2\sqrt2\).

The proof constructs, for every sufficiently large \(n\), a unitary \(S_n\)
with intensity \(P_n=|S_n|^2\), such that
\[
 \max P_n\le8\log(2n)/n,\quad
 \|P_n-J_n\|_{\rm op}\le n^{-1/8}
       +16\sqrt{\log(2n)/n}\to0,\quad
 (P_n^2)_{ij}=1/\lfloor n/\log(2n)\rfloor.
\]
The global intensity norm misses a selected logarithmic two-step peak.
The exact one-step fresh-phase Schur variance at that pair is consequently
\(\sim\log(2n)/n^2\), despite the static hypotheses.

The corrected positive estimate contains \(\rho^{h-2}\):
\[
 |(P^h)_{ij}-1/n|\le
 \rho^{h-2}
 \sqrt{(\sum_kP_{ik}^2-1/n)(\sum_kP_{kj}^2-1/n)},\qquad h\ge2.
\]
It is sharp at \(h=2\) for the prescribed row and column. Our sequence
has uniform three-step mixing at relative error \(o(1)\), while its
two-step peak diverges relative to \(1/n\). Therefore three-step mixing
alone does not supply the two-step kernel in the entry bracket.

The [review and execution packet](../evidence/executions/20261012/unitary-two-step/README.md)
preserves the original 11 October candidate, independent reconstruction,
final maintained-file review and finite-control hashes. Four exact rational
orthogonal fixtures and one complex rank-one primitive are separate from
six floating QR diagnostics. A timed-out preliminary complex fixture was
replaced with explicitly narrower exact coverage; the failure is retained.

The [primary-source comparison](../literature/unitary_two_step_sources_20261012.md)
credits the established Haar unistochastic ensemble and distinguishes its
observables from the centered fourth moment derived here. Priority is
not established.

This closes the suggested **static unitary** repair of the earlier
classical obstruction. It neither constructs a trajectory from the
maintained map nor refutes its flatness event. The missing implication is
control of evolving two-step row--column correlations or their accumulated
effect. TRACE-055, signed TRACE-005, deterministic BGS and all-time
entry-flatness probability remain open.
