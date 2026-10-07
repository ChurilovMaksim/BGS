# Candidate ordinary centering of the compact sectors

7 October 2026. Author calculation only; independent review deferred. This is NOT included among the accepted results in the checkpoint. It records the nearly complete geometric continuation without delaying the reviewed source result.

For a fixed sector of the compact functional, let B be the set of k sites integrated on the unit circle; the other N-k sites are integrated over the open disk. At N>=3, almost every such configuration has a unique a in the disk with

w_i=(z_i-a)/(1-conjugate(a)z_i),    sum_i w_i=0.

The same potential as in the accepted interior gauge is

F_z(a)=sum_i log|1-conjugate(a)z_i|^2-N log(1-|a|^2).

It is proper whenever no boundary point occurs with multiplicity at least N/2. Indeed near a boundary point of multiplicity h the worst radial divergence is (N-2h)log(1/(1-|a|)); away from those points the coefficient is N. For almost every boundary-sector configuration at N>=3, boundary points are distinct, so h<=1<N/2. The geodesic Hessian is 2 sum_i[1-Re(exp(-2i theta)w_i^2)], positive unless all points are boundary points on the same antipodal pair. That exceptional configuration is measure zero. Thus the minimizer is unique and its critical equation is the displayed centering equation.

At a centered tuple the real derivative of sum_i w_i with respect to a is

[-N da+(sum_i w_i^2)d conjugate(a)]/(1-|a|^2),

so the Faddeev-Popov determinant is [N^2-|sum_i w_i^2|^2]/(1-|a|^2)^2. Insert the identity obtained by integrating this determinant against the ordinary two-dimensional delta of sum_i m_a(z_i). Then change each coordinate z_i=(a+w_i)/(1+conjugate(a)w_i). Its fixed-a Jacobian is

(1-|a|^2)/|1+conjugate(a)w_i|^2 on a circle,
(1-|a|^2)^2/|1+conjugate(a)w_i|^4 on a disk.

Consequently a compact-sector integral of g(z) becomes its integral over a and w with delta^(2)(sum_i w_i), the original normalized circle/disk measures in w, ordinary d^2a, and the weight

[N^2-|sum_i w_i^2|^2](1-|a|^2)^(2N-k-2)
 / [ product_(i not in B)|1+conjugate(a)w_i|^4
     product_(i in B)|1+conjugate(a)w_i|^2 ].

The two-dimensional delta uses Euclidean normalization. Odd variables have already been extracted in the compact representation, so this is an ordinary change of variables of each exact coefficient function; it is not a claimed super-Berezinian. The coefficient functions and all source factors must still be carried through the map.

Real boundary exceptions matter: at N=2 with one circle point and one strict disk point, no interior centering can exist because their transformed moduli are one and less than one. With two distinct circle points, the centered antipodal pair has a nonunique one-parameter family of centers. The N=1 circle sector also has no interior center. These small strata remain in their original exact compact form. For the actual odd N>=3 family the almost-everywhere construction avoids them.

A fresh reviewer should check the global coarea/normalization statement and the almost-everywhere boundary properness before using this candidate. Even if accepted, it does not turn the compact sector into the positive interior measure controlled by the scalar coercivity theorem; signed coefficient cancellation is still required.
