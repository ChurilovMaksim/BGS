# Exact coherence memory and its singular-norm plateau

**Stable claim:** BGS-TRACE-082. **State:** PROJECT PROOF + INDEPENDENT
INTERNAL RECONSTRUCTION, 14 October 2026.
M1--M2 are self-contained finite-dimensional statements; M3 uses
the constructed family of BGS-TRACE-081. This is not a BGS theorem.
The full analytic operator argument is not formally certified.

Let \(N\ge2\), let \(U\) be unitary on \(\mathbb C^N\), and give
\(M_N(\mathbb C)\) its Hilbert--Schmidt inner product. Write
\(\mathcal D\) for the orthogonal diagonal projection,
\(\mathcal Q=I-\mathcal D\), and \(\mathcal T(X)=UXU^*\).
Identify the diagonal subspace with \(\mathbb C^N\).
Then \(\mathcal D\mathcal T\mathcal D\) is exactly \(P(U)\)
with entries \(|U_{ij}|^2\). Put
\[
\mathcal E=\mathcal Q\mathcal T\mathcal Q,\qquad
\mathcal L=\mathcal D\mathcal T\mathcal Q,\qquad
\mathcal C=\mathcal Q\mathcal T\mathcal D,
\]
with their indicated diagonal/off-diagonal domains.

## M1. Exact return memory

For \(|z|<1\), as an operator on the diagonal subspace,
\[
\mathcal D(I-z\mathcal T)^{-1}\mathcal D
 =\left[I-zP-z^2\mathcal L
       (I-z\mathcal E)^{-1}\mathcal C\right]^{-1}.
\]
The lower-right block is invertible because \(\mathcal E\) is a
contraction. The full resolvent is invertible because \(\mathcal T\)
is unitary. Ordinary block elimination proves the identity with exactly
these orders of multiplication. No factor commutation or phase
independence is used.

Equivalently, start \(X_0\) diagonal and put
\(a_n=\mathcal D\mathcal T^nX_0\),
\(c_n=\mathcal Q\mathcal T^nX_0\). The block recurrence gives \(c_0=0\) and
\[
a_{n+1}=Pa_n+\sum_{s=0}^{n-1}
         \mathcal L\mathcal E^{\,n-1-s}\mathcal C a_s .
\]
The terms \(\mathcal L\mathcal E^r\mathcal C\) retain coherent return
memory. \(P^n\) describes projection away of coherence after every
step; \(\mathcal D\mathcal T^n\mathcal D\) describes unmeasured unitary
evolution. These operators need not agree. They do agree for particular
unitaries, including diagonal and monomial matrices.

## M2. Universal exact singular-norm plateau

For every unitary \(U\) and each integer \(0\le r<N\),
\[
\|\mathcal E^r\|_{\mathrm{HS}\to\mathrm{HS}}=1.
\]
For \(r=0\) this is the identity on a nonzero space. For \(r\ge1\),
work in the complex trace-zero space of dimension \(N^2-1\).
For each time \(j\), the constraint
\(\mathcal D\mathcal T^jX=0\) has codimension at most \(N-1\):
\(\mathcal T\) preserves trace and trace-zero diagonal matrices
have dimension \(N-1\). Therefore the space satisfying these constraints
at \(j=0,\ldots,r\) has dimension at least
\[
N^2-1-(r+1)(N-1)=(N-1)(N-r)>0.
\]
Choose nonzero \(X\) there. Both \(X\) and \(\mathcal T^jX\) are
off diagonal for \(j\le r\). Induction gives
\(\mathcal E^jX=\mathcal T^jX\) for \(j\le r\).
Thus \(\|\mathcal E^rX\|_{\rm HS}=\|X\|_{\rm HS}\).
Contractivity supplies the reverse inequality.
No premise about \(P\) or coordinate reversal is used.

This rules out a strictly contracting one-step singular-norm bound
for the unaveraged coherence block and norm-power decay before time
\(N\). It does not rule out a spectral-radius bound, contraction at
larger times, cancellation of \(\mathcal L\mathcal E^r\mathcal C\),
or control of specific signed/observed sources. The equality of norms
does not assert nondecay for every source.

## M3. Observed returns despite perfect intensity mixing

For the explicit \(A_k,U_k=A_kE_k\) of
[TRACE-081](flat_spectrum_obstruction.md), put
\(t_k=N_k-4p_k\). Then \(A_k^{t_k}=I\) and
\(\|U_k^{t_k}-I\|\le t_k\epsilon_k\). Left/right multiplication
on Hilbert--Schmidt space has norm bounded by the respective matrix
operator norms, so
\[
\|\mathcal T^{t_k}-I\|_{\mathrm{HS}\to\mathrm{HS}}
       \le2t_k\epsilon_k.
\]
Compressing to the diagonal space yields
\[
\bigl\||U_k^{t_k}|^{\circ2}-I_{N_k}\bigr\|_{2\to2}
       \le2t_k\epsilon_k,\qquad
\bigl\||U_k^{t_k}|^{\circ2}-P(U_k)^{t_k}\bigr\|_{2\to2}
       \ge1-2t_k\epsilon_k .
\]
Here the modulus square is entrywise, while \(P(U_k)^{t_k}=J\).
The last inequality uses \(\|I-J\|=1\).
Observed coherent return memory can therefore have order-one norm
at Heisenberg times even when \(P\) resets centered diagonal data
exactly in one step.

## Boundary and verification

Block resolvent elimination and finite-dimensional observability are
classical mechanisms; no priority claim is made. The obstruction concerns
the full unaveraged Hilbert--Schmidt coherence block. It excludes no
properly delimited averaged ensemble theorem, source cancellation
theorem or BGS system class. The unchanged fixed-map microscopic signed
source remains unestimated.

The core mathematical proof above is separate from exact finite checks
and from any finite arithmetic Lean kernel. No operator-norm, complex
linear-algebra, discriminant, asymptotic or BGS statement is asserted
to follow from compiling a numerical dimension budget.

[Independent audit and maintained-transfer check](../../archive/evidence/executions/20261014/spectrum-coherence/README.md)
separate the original prose correction from the proof of M1--M3.
The [Python verifier](../../computations/verification/spectrum_coherence_controls.py)
checks exact finite block identities and an N=2 endpoint with nonzero
coherence block but its square zero. A separate
[C++ replay](../../computations/cpp/coherence_memory_verifier.cpp) uses Gaussian
integers for that endpoint. The
[Lean kernel](../../formalization/Bgs/CoherenceBudget.lean) proves only positivity
of the numerical product (N-1)(N-r) under N>=2 and r<N; compilation
status and printed axioms belong to the actual execution receipt.
Neither the complex dimension argument nor the operator norm theorem
is formally certified by that arithmetic kernel.
