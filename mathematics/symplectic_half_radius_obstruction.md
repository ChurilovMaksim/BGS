# Half-radius obstruction even with reverse-kernel decay

Separate author addendum, 7 October 2026. No canonical edit and no actual-map counterexample. Independently reviewed; see record/half_radius_obstruction_review.md. This strengthens the explicit one-step Fourier Hamming-threshold witness, not the current fractional-Hamming theorem.

## Prior scope and exact new distinction

The project already proves that coordinate flatness, the FM021-type position gap and FM022-type reverse-kernel decay are insufficient as abstract universality criteria: `BGS/mathematics/spectral-obstructions/microscopic_rounding_control.md`, Sections1,5–6, preserves those properties while violating a fixed pair target. `isospectral_clock_moment_control.md` provides a different all-copy channel obstruction. Those results are credited; no new general insufficiency or priority claim is made.

A targeted search of current mathematics and historical records for symplectic Fourier, flat/Hermitian involution and reversed-kernel variants found no occurrence of this exact construction. The specific additional statement here is an explicit flat Hermitian involution whose literal offcharge Hamming trace at radius m/2 is order N, despite reverse-kernel norm N^(-1/2).

## Claim

Let n>=3 be odd, N=n², G=(Z/nZ)², and

 omega(x,y)=x_1 y_2-x_2 y_1,
 H_(x,y)=N^(-1/2) exp(2pi i omega(x,y)/n).

Then

 H*=H, H²=I, |H_(x,y)|²=1/N,
 ||Q_H||op=N^(-1/2),   Q_H(x,y)=H_(x,y)conjugate(H_(y,x)).   (S1)

For every even m>=4, the candidate's literal offcharge Hamming projector satisfies

 Tr_E[R O_(m/2) Ad(H^tensor m)]>=2(N-1)(1-1/N).             (S2)

At m=4 the value is exactly2(N-1). Thus the one-step position norm is zero and the reverse kernel decays to zero along odd square dimensions, while the offcharge half-radius trace does not decay. The spectrum of H lies in {+1,-1}, with multiplicities (N+sqrt(N))/2 and (N-sqrt(N))/2.

## Matrix identities

Alternation gives conjugate(H_(y,x))=H_(x,y), so H is Hermitian. The finite-character identity

 N^(-1)sum_(y in G) exp(2pi i omega(x-z,y)/n)=1_(x=z)

shows H²=I; the symplectic form is nondegenerate for every n, including composite n. The flatness claim is immediate.

Since2 is invertible modulo odd n, the matrix

 H^(2)_(x,y)=N^(-1/2) exp(2pi i 2omega(x,y)/n)

is another Hermitian unitary. Therefore Q_H=N^(-1/2)H^(2), proving its exact norm. Finally Tr H=N/sqrt(N)=sqrt(N), which, with H²=I, proves the stated multiplicities.

## Exact half-radius trace

Use p=P_D0, q=P_O, A=Ad(H)|_V as in the frozen candidate. Flatness gives pAp=0. In a cyclic word with at most m/2 q slots, every nonalternating pattern contains adjacent p slots and has zero trace. The two alternating patterns are the only survivors. Since A²=I,

 Tr[R F_(m/2) A^tensor m]=2(N-1)                            (S3)

on top traceless support. Exact total-charge balance is imposed by the same torus integral as in the candidate. With D_z=Ad(Z)|_V and Z=diag(z_x) for independent uniform unit phases, the balanced alternating trace is

 2 integral Tr_(D0)[(p A D_z A p)^(m/2)] dz.                (S4)

The compressed matrix in (S4) is P_(H Z H)-J. Its entries depend only on x-y:

 (H Z H)_(x,y)=N^(-1)sum_(u in G) z_u exp(2pi i omega(x-y,u)/n).

Consequently P_(H Z H) is convolution on G. Up to the irrelevant sign/bijection of Fourier indexing, its nonconstant eigenvalues are

 a_k(z)=N^(-1)sum_(u in G) z_u conjugate(z_(u-k)),  k!=0.

Thus its q-th traceless trace is sum_(k!=0) a_k(z)^q, where q=m/2>=2. For each nonzero k,

 |a_k|<=1,   integral |a_k|² dz=1/N.

The second identity follows from the same exponent-multiset cancellation as in the Fourier obstruction, and does not require k to have prime order. Hence

 |integral a_k^q dz|<=integral |a_k|^q dz<=1/N.             (S5)

In fact integral a_k^q dz is nonnegative real: expanding a_k^q gives a sum of unit-character monomials with the same positive coefficient N^(-q), and the torus integral selects their zero exponent terms. Therefore the quantity in (S4) lies between0 and2(N-1)/N. Subtract it from (S3), using O=(I-Pi)F, to prove (S2). Proper support pieces vanish exactly as in the candidate.

For m=4, q=2. A zero exponent monomial in a_k² would require two directed k-edges to form a closed balanced multigraph, forcing2k=0 (or k=0). In an odd group neither is possible for k!=0. Thus all integral a_k² vanish and (S4)=0, proving the exact value2(N-1).

## Boundary

This construction changes the operator and its coordinate index set. It is not the frozen quantizer, does not preserve its exact arithmetic/parametrix data, and has gross two-point spectral degeneracy. It sharpens only the abstract data limitation already known from project rounding: adding reverse-kernel decay to one-step flatness/gap still does not control the literal half-Hamming sector uniformly over all unitaries.

The new input suggested by this witness is actual quantum-power compression: p Ad(H)^2 p=I_D0. A hypothetical bound on p Ad(U_N)^k p concerns |U_N^k|², not (|U_N|²)^k. No such hypothesis is imported into the frozen fractional-Hamming theorem, and no theorem pushing the actual radius beyond half is asserted.
