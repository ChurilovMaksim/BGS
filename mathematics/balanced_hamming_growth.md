# Charge-balance counting refinement and exact new-sector size

7 October 2026. This adds to the frozen candidate `candidate_v1.md` (SHA-256 `2ce67b8d33b574e5b245affd49f6592a9636b6075e4c288af8e718cc27c9404f`) without changing its bytes or relying on a stronger analytic input. This addendum was independently reviewed with the hierarchy.

## Better growing-radius constant

In a balanced list ((a_1,b_1),...,(a_s,b_s)), the multisets of a and b labels agree. Choose the a list in at most N^s ways, then obtain the b list by some permutation of that list, in at most s! ways. Repeated labels only decrease the number of distinct b lists; ignoring a_i!=b_i enlarges the count. Therefore

 b_N(s)<=s! N^s,
 L=sum_(s<=r) binom(m,s)b_N(s)
   <=sum_(s<=r) (m)_s N^s
   <=(r+1)(mN)^r.                                             (8)

The exact balanced projector and the norm bound (1) are unchanged. On aN<=m<=bN and r<=kappa N/log N,

 log L<=(2kappa+o(1))N.

Thus every kappa<gamma_a/2, and every c<gamma_a-2kappa, is valid in candidate (3). Here gamma_a=min{a log(1/rho),1/160} and rho=sqrt(159/160), exactly as before. In particular every r_N=o(N/log N) has sector decay at any fixed exponent c<gamma_a. There is no claim for a positive fraction of m.

## Exact dimension on the contributing support

The top-support raw subspace K has dimension

 d_r=sum_(s<=r) binom(m,s)b_N(s)(N-1)^(m-s),                   (9)

because each balanced marker-color choice leaves m-s independent traceless-diagonal factors. Whenever L a_(m-2r)<1, the centered inclusion on that support is injective, so its range has the same dimension. The top-support piece of the new orthogonal sector Q_r consequently has dimension d_r-(N-1)^m. At r=2 it is exactly

 binom(m,2) N(N-1)^(m-1).

This is a genuinely larger sector than the ordered diagonal, with every balanced single-swap coherence included before centering. The full Q_r also contains proper-support pieces, whose cyclic trace vanishes exactly. Formula (9) is a dimension statement, not an estimate for the remaining high-Hamming sector.

## Finite controls and boundaries

The separate `checks_network.py` controls the fully color-summed two-stage contraction in N=2,m=5,r=2 and N=3,m=3,r=2. The N=3 case has rank-two traceless-diagonal local factors, so it does not accidentally reduce every local projection to rank one. The exact b_N(s) counts for N=2,3,4 and 0<=s<=4 obey (8); its general proof is the elementary multiset argument above.

All claims retain the same literal actual U_N, fixed coupling, inherited singular bound and Haar tail. The rightmost projector in candidate (7), the off-charge contribution, the plateau and higher factorial hierarchy remain open.
