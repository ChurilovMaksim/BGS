# Exact coherence memory and its singular-norm plateau

Candidate companion to the abstract flat-spectrum obstruction. The statements
below are finite-dimensional identities/obstructions, not a BGS theorem.
No independent audit has yet been recorded for this companion.

Let N >= 2, let U be unitary on C^N, and give M_N(C) its Hilbert--Schmidt
inner product. Write D for the orthogonal diagonal projection, Q=I-D,
and T(X)=UXU*. Identify the diagonal subspace with C^N.
Then D T D is exactly P(U) with entries |U_ij|^2.
Put E=Q T Q on the off-diagonal subspace, L=D T Q and C=Q T D.

## M1. The exact return-memory identity

For |z|<1 the compressed resolvent is
\[
D(I-zT)^{-1}D
 =\bigl[I-zP-z^2L(I-zE)^{-1}C\bigr]^{-1}
\]
as an operator on the diagonal subspace. The lower-right block is invertible
because E is a contraction. The full resolvent is invertible because T is
unitary. Ordinary block elimination proves the identity with exactly these
orders of multiplication. No factor commutation or phase independence is used.

Equivalently, start X_0 diagonal, write a_n=D T^n X_0 and c_n=Q T^n X_0.
The block recurrence gives c_0=0 and
\[
a_{n+1}=P a_n+\sum_{s=0}^{n-1} L E^{n-1-s} C a_s .
\]
The terms L E^r C are the retained coherent return memory. P^n describes
the experiment which projects away coherences after each step; D T^n D
describes unmeasured unitary evolution. They are different operators.

## M2. Universal exact singular-norm plateau through N-1

For every unitary U and each integer 0<=r<N,
\[
\|E^r\|_{HS\to HS}=1.
\]
For r=0 this is the nonzero-space identity. For r>=1, work in the
trace-zero space of dimension N^2-1. For each time j, the constraint
D T^j X=0 has codimension at most N-1: T preserves trace and the
trace-zero diagonal space has dimension N-1. Hence the space of X
such that D T^j X=0 for j=0,...,r has dimension at least
\[
N^2-1-(r+1)(N-1)=(N-1)(N-r)>0.
\]
Choose nonzero X there. X is off diagonal and T^j X remains off diagonal
for every j<=r. Induction gives E^j X=T^j X for j<=r, so
||E^r X||_HS=||X||_HS. The reverse bound follows from contractivity.
No assumption on P or on a coordinate reversal matrix enters this proof.

This refutes a dimension-independent, strictly contracting singular-norm
bound for the unaveraged off-diagonal block, and any norm-power estimate
claiming decay before r=N. It does not rule out a spectral-radius bound,
contraction at larger times, cancellation of L E^r C, or control of
specified observed/signed sources. In particular ||E^r||=1 is not
asserted to imply that every source has nondecaying memory.

## M3. Order-one observed coherent returns despite P=J

For the explicit A_k and U_k=A_k E_k of O1--O5 in the separate candidate,
at t_k=N_k-4p_k we have A_k^{t_k}=I and
||U_k^{t_k}-I||<=t_k epsilon_k. Conjugation therefore satisfies
\[
\|T^{t_k}-I\|_{HS\to HS}\le 2t_k\epsilon_k.
\]
Compression gives
\[
\bigl\||U_k^{t_k}|^{\circ2}-I_{N_k}\bigr\|_{2\to2}
 \le2t_k\epsilon_k,\qquad
\bigl\||U_k^{t_k}|^{\circ2}-P(U_k)^{t_k}\bigr\|_{2\to2}
 \ge1-2t_k\epsilon_k .
\]
Here the modulus square is entrywise, while P(U_k)^{t_k}=J.
The second inequality uses ||I-J||=1 for N_k>=2.
Thus some observed coherent return memory remains of order one at
Heisenberg times, even though the one-step intensity matrix resets
centered diagonal data exactly.

Block-resolvent memory elimination and finite-dimensional observability
are classical mechanisms. No priority claim is made. The purpose is to
identify which proposed norm-gap route cannot close the signed hierarchy.
The actual fixed-map microscopic signed source remains unestimated.
