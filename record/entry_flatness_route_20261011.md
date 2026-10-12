# Entry-flatness route: the exact variance and a classical obstruction

**Later result, 12 October:** the
[unitary two-step obstruction](../mathematics/unitary_two_step_obstruction_20261012.md)
proves the same failure inside the genuine unistochastic class. The
classical example below retains its original scope; its suggested static
unitary repair is now ruled out. Evolution from the maintained initial
map and all-time flatness probability remain open.

Research outcome from main `b126cfb18f445b82358fc156632873082ac22503`,
11 October 2026. This route concerns the missing probability of all-time
entry flatness in TRACE-060/073. It has not proved that probability.

## The directly tested mechanism

For a surviving entry the exact feedback update is
S'_ij=S_ij+q S_ie S_ej, with E_w q=0 and E_w|q|²=1/d_e.
The unscaled entry, frozen when either label is removed, is a complex
martingale. Uniform-coordinate selection gives the exact conditional
second moment of its increment:

\[
 \mathbb E(|\Delta S_{ij}|^2\mid\mathcal F_u)
 =\frac1u\sum_{e\notin\{i,j\}}
       \frac{P_{ie}P_{ej}}{1-P_{ee}},\qquad P_{ij}=|S_{ij}|^2.
\]

On a pre-exit flatness barrier delta_u=K log(2N)/u, bistochasticity
improves the crude delta_u² estimate to delta_u/[u(1-delta_u)].
The cumulative bracket down to size v is therefore at most
C K log(2N)/v. This is the same scale as the square of the requested
amplitude threshold. Direct bounded-variation Freedman from this estimate
does not give the vanishing failure probability needed for a uniform
live-entry union. This is a failure of that estimate to close the barrier,
not a disproof of the desired event or of other martingale methods.

A possible replacement would control the two-step kernel P² entrywise.
An intensity singular gap by itself does not provide that control, even
when it tends to zero and the entry bound already holds.

## An exact doubly stochastic obstruction

Choose integers n>=3 and 1<=b<=n-2, two distinct indices i,j, and a set
B of b indices disjoint from them. Put r_k=1/b on B and zero elsewhere.
Define the nonnegative n-by-n matrix P by

\[
 P_{ij}=0,\quad P_{i\ell}=r_\ell\ (\ell\ne j),\quad
 P_{kj}=r_k\ (k\ne i),\quad
 P_{k\ell}=\frac{(1-r_k)(1-r_\ell)}{n-2}\ (k\ne i,\ell\ne j).
\]

Both row and column sums equal one. In a non-special row, for example,
sum_(ell!=j)(1-r_ell)=n-2, so its sum is r_k+(1-r_k)=1.
The largest entry is exactly 1/b, and

\[
 (P^2)_{ij}=1/b,
 \|P-J_n\|_{HS}^2
 =\frac2b+\frac{(n-3+1/b)^2}{(n-2)^2}-1
 \le\frac3b.
\]

The last inequality follows by writing the middle numerator as
(n-2)-(1-1/b). Thus the centered operator norm is at most sqrt(3/b).
Take b=floor(n/log(2n)). The entry bound is O(log n/n), the centered
singular gap tends to zero, but n(P²)_ij=n/b diverges like log n.
Consequently these two classical inputs do not imply (P²)_ij=O(1/n).
The example also rejects an additional factor of the singular norm in a
universal bound |(P-J)²_ij|<=C ||P-J|| max(P_kl).

This construction is **doubly stochastic only**. It is not asserted to
be unistochastic, to arise in the random Schur process, or to refute BGS.
The later unitary theorem shows that unitarity alone does not remove this
obstruction. A proof for the maintained process must use additional
information about its states or their evolution. A random-phase correlation
argument remains unexecuted at this missing step. The route is open at
that narrower implication; the elementary gap-only shortcut is ruled out.
