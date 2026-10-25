# Exact radial translation and a deliberately limited tail consequence

This note only translates the proved scalar-body inequality. It does not identify an auxiliary positive integral with the full balanced phase observable.

Let z_j denote the centered disk entries in report.md, so sum z_j=0, and set

psi_j=z_j/sqrt(1-|z_j|^2).

Then z_j=psi_j/sqrt(1+|psi_j|^2), and

H=sum_j log(1+|psi_j|^2),
exp(-S)<=product_j (1+|psi_j|^2)^(-c),
c=1/(2K^2)>0.

The exact radial slice is sum_j psi_j/sqrt(1+|psi_j|^2)=0. It is not sum psi_j=0. Thus the earlier nonlinear-slice counterexample is respected, not erased by this theorem. The common Mobius center must move when one imposes a different slice.

For an individual unconstrained complex coordinate, the ordinary radial Jacobian is

d^2 z=(1+|psi|^2)^(-2)d^2 psi.

This individual-coordinate identity must not be multiplied as though the N centered coordinates were independent. A constrained change of variables has its own determinant.

There is a simple rigorously bounded **auxiliary** centered disk integral. Let

Omega_N={(z_1,...,z_(N-1)): |z_j|<1, |sum_(j<N) z_j|<1},
z_N=-sum_(j<N)z_j.

With ordinary coordinate Lebesgue measure product_(j<N)d^2z_j, for any L>=0,

integral_(Omega_N, H>=L) exp(-S) product d^2z_j
 <= exp(-cL/2) [pi/(1+c/2)]^(N-1).

Indeed on H>=L, exp(-S)<=exp(-cL/2)exp(-cH/2), omit the final factor (1-|z_N|^2)^(c/2)<=1, enlarge to the full (N-1)-fold disk, and use integral_disk(1-|z|^2)^(c/2)d^2z=pi/(1+c/2).

This is an explicit noncompact-height tail bound for a specified positive scalar integral. It carries a dimension-dependent volume factor and supplies no normalizing lower bound. It does not include the ordinary collective-coordinate Jacobian (9), super-Berezinian, fermion-generated factors, microscopic sources, or boundary contributions of the full observable. Consequently it is not a full integral/tail theorem for the balanced sector.
