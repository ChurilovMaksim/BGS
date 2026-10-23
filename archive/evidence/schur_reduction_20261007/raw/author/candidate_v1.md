# Exact scalar Schur-energy reduction of the full balanced pair target

7 October 2026. Author candidate; independent review pending. Canonical read-only base observed at opening: `d37c92e563d10d25bb1d6ab85bedffc1f160f773`. All new artifacts are outside BGS. No full BGS theorem, phase-ensemble universality theorem, publication, or priority claim.

## Result and contract

For an arbitrary fixed unitary U of dimension N, the entire independent-coordinate-phase pair transform has an exact decomposition into N nonnegative scalar Schur energies, (8). This includes arbitrary powers, all coordinate repetitions, and the Heisenberg plateau. An equivalent three-radius dilogarithm criterion, (12), avoids differentiating an unproved limiting formula. These are full-target reductions, not finite-diagram estimates.

A boundary scalar scattering marginal can actually be evaluated: after eliminating all but one coordinate, it is exactly the Poisson-kernel law with parameter U_jj. Thus the prescribed map's entrywise flatness already yields asymptotic uniformity of that marginal. This does not estimate its microscopic radial derivative; the cyclic-permutation control proves that even an exactly uniform marginal and exact mean delay N are insufficient.

One radial scattering elimination has an exact conditional intensity update. Its fourth moment exposes a phase-sensitive rectangular coherence (16), and the next intensity update contains an unclosed random ratio. These formulas give the first precise obstruction to replacing the evolving random Schur matrices by their averaged classical intensities.

The actual family remains exactly U_N=exp(i 10^(-80) N A_N)M_N at all odd dimensions, in `mathematics/fixed_map_path_model.md`. The phase integrals below represent the exact balanced projector; they are not a change to the deterministic target. The full deterministic off-charge defect remains separate. FM-021 supplies max|U_ij|^2=O(1/N), limsup||P-J||<=10^-64 and the eventual bound 1/2; FM-022 supplies ||Q||->0. Neither is asserted to propagate through Schur elimination. The accepted fractional-Hamming theorem controls a small balanced centered range; nothing below substitutes its separate 0.49m off-charge bound for a large balanced bound.

## 1. Analytic logarithm and a coordinate martingale

Fix any coordinate ordering, identify its first k coordinates with S_k, and let D_k=diag(zeta_1,...,zeta_k), with independent normalized uniform phases. For |z|<1 put

 L_k(z)=log det(I_k-z D_k U_(S_k,S_k)), L_0=0.                 (1)

The logarithm is the analytic branch zero at z=0. Every compression has norm at most one, so the determinant is nonzero in the open disk. Moreover its logarithm is an absolutely, locally uniformly convergent power series in the coordinate variables z zeta_i. Integrating unrevealed variables sets them to zero. Consequently

 E[L_N(z) | zeta_1,...,zeta_k]=L_k(z).                       (2)

One elementary justification avoids any logarithm branch ambiguity: use -sum_(m>=1) z^m Tr[(D U)^m]/m, which converges uniformly on every closed smaller disk, and retain exactly the words using only the revealed coordinates.

Write the k-th principal compression in block order (k,S_(k-1)) as

 [a  b]
 [c  d],

and define

 h_k(z)=a+z b D_(k-1)(I-z d D_(k-1))^(-1)c,
 f_k(z)=z h_k(z).                                          (3)

These functions depend only on the previous k-1 phases. The determinant Schur identity, with det(I-AB)=det(I-BA), gives

 L_k(z)-L_(k-1)(z)=log(1-zeta_k f_k(z)).                    (4)

No inverses at boundary spectral points are used.

The block matrix T=[a,bD;c,dD] is a contraction. Set y=(I-zdD)^(-1)c. Then T(1,zy)=(h_k,y), so

 1-|h_k(z)|^2 >= (1-|z|^2)||y||^2 >=0.                    (5)

Thus |f_k(z)|<=|z|<1 uniformly in all phases. At k=N the block matrix is unitary and the first inequality is equality. For real r this gives the useful exact identity

 1-r^2|h_N(r)|^2=(1-r^2)(1+r^2||y||^2).                   (6)

## 2. Exact dilogarithm and positive Schur-energy formulas

Write B_N(m)=E|Tr[(D U)^m]|^2. Global phase invariance makes different positive powers orthogonal. Martingale increments are orthogonal as well. Integrating zeta_k in (4), by its uniformly convergent scalar Taylor series, yields

 E[L_N(z) conjugate(L_N(w))]
 =sum_(k=1)^N E Li_2(f_k(z) conjugate(f_k(w))).             (7)

Here Li_2(t)=sum_(n>=1)t^n/n^2 on |t|<1. In particular every summand of the equal-radius formula lies between 0 and pi^2/6. This is an ordinary compact-torus integral; there are no supersymmetric/noncompact domains or finite-diagram truncations.

Differentiating on smaller disks is legitimate for every fixed N. Apply z partial_z and conjugate(w) partial_conjugate(w), or directly differentiate each increment (4) before integrating zeta_k. For 0<r<1 the result is

 sum_(m>=1) r^(2m) B_N(m)
 =sum_(k=1)^N E [r^2 |h_k(r)+r h_k'(r)|^2
                         /(1-r^2 |h_k(r)|^2)].             (8)

Each term is nonnegative. No factor 1/m, 1/N, or replica dimension is missing. Setting r=exp(-s/N), the full balanced Abel target is exactly

 N^(-2) sum_k E [r^2 |h_k(r)+r h_k'(r)|^2
                         /(1-r^2 |h_k(r)|^2)]
 -> (1-exp(-2s))/(4s^2), for every s>0.                    (9)

The benchmark includes every m>N. The positive-measure Laplace implication already proved in `supplement/fixed_map/weighted-secular/determinant_boundary.md` applies after expectation. In detail, use the positive measure mu_N=N^(-2)sum_(m>=1)B_N(m)delta_(m/N), tilt by exp(-2s0 t), and push forward by x=exp(-t). Values at s0+n/2 give every Hausdorff moment on [0,1], including total mass; polynomial approximation yields the required compact-weight convergence. Thus (9) would prove every positive compact-band balanced pair comparison, not just a stable band. The converse compact-to-Abel statement in that source uses a compact majorant through frequency zero and a Fejer tail bound; it is not being claimed from positive bands bounded away from zero alone. It would leave the deterministic nonzero-charge comparison and higher factorial orders open.

An independent uniform random reveal order may be averaged in (7)-(9) without changing their left sides. The first k revealed labels then form a uniform k-subset. This is an exact exchangeability device, not an assumption that the evolving scattering entries are independent, Haar-distributed, or flat.

## 3. A derivative-free equivalent closure criterion

Define

 G_N(s)=sum_k E Li_2(exp(-2s/N)|h_k(exp(-s/N))|^2)
       =sum_(m>=1) B_N(m) exp(-2sm/N)/m^2.

It follows exactly that G_N''(s)=4 N^(-2)sum_m B_N(m)exp(-2sm/N). In particular G_N'' is nonnegative and decreasing. For 0<h<s set

 Delta_h G_N(s)=G_N(s+h)+G_N(s-h)-2G_N(s).                  (10)

Then (9) for every s>0 is equivalent to the following bounded-integrand scalar assertion for every 0<h<s:

 Delta_h G_N(s) -> D(s,h),                                (11)

 D(s,h)=integral_0^infinity [min(t,1)/t^2] exp(-2st)
                         [2cosh(2ht)-2] dt.                (12)

The integrand has a removable issue at zero and decays at infinity because s>h. Formula (11), after inserting the defining sum for G_N, consists of three radii and N dilogarithms each bounded by pi^2/6. In fact every individual k contribution to Delta_h is nonnegative. To see this, expand the k-th logarithmic increment as -sum_m z^m[Tr((D_k U_k)^m)-Tr((D_(k-1)U_(k-1))^m)]/m. The bracket is homogeneous of total phase degree m, so different m are orthogonal under simultaneous rotation of the first k phases. Its squared norm is therefore a positive exponential series in s, hence convex. The subtraction is across the three radii, not a need for cancellation across k. Boundedness of each dilogarithm alone still supplies no convergence of the N-term sum.

Proof of equivalence: the exact identity

 Delta_h G_N(s)=integral_(-h)^h (h-|u|)G_N''(s+u) du

shows necessity by locally bounded dominated convergence; monotonicity supplies local bounds once (9) holds. For sufficiency, for s>2h, monotonicity gives

 Delta_h G_N(s+h)/h^2 <= G_N''(s)
                    <= Delta_h G_N(s-h)/h^2.              (13)

Take lower and upper limits in N using (11), then h down to zero. Both bounds converge to (1-exp(-2s))/s^2. Divide by four to obtain (9). This proves the limiting derivative without an interchange justified merely by formal differentiation.

## 4. Exactly what one scattering elimination controls

Partition a current contraction as S=[A b;c a]. For a fresh uniform phase zeta and a fixed radial parameter 0<r<=1, eliminate its last coordinate:

 S'=A+(r zeta)/(1-r zeta a) b c.                            (14)

For r<1 this is always defined. At r=1, assume |a|<1; degenerate unitary decoupling cases have bc=0 and are handled by their trivial reduction. Every eliminated coordinate retains the same original radial r. One must not replace later S' by a unitary when r<1.

Writing P_uv=|S_uv|^2, the exact conditional mean is

 E_zeta |S'_uv|^2=P_uv + r^2 P_u,last P_last,v
                                     /(1-r^2 P_last,last). (15)

At r=1 this is the classical stochastic-complement formula conditional on the current random S. Averaging one more elimination produces E[P_uk P_kv/(1-r^2P_kk)], not the ratio of expectations. This random denominator and the joint numerator are the first unclosed step.

For a particular entry put A0=A_uv, x=b_u c_v, t=|a|^2, d0=1-r^2 t. Exact scalar phase integration gives

 E_zeta |S'_uv|^4
 =|A0|^4+4r^2 |A0|^2|x|^2/d0
  +4r^4 |x|^2 Re(conjugate(A0) x conjugate(a))/d0^2
  +r^4 |x|^4(1+r^2 t)/d0^3.                               (16)

The third term is phase-sensitive rectangular coherence. It cannot be reconstructed from intensities alone. It is not the same observable as the original reverse matrix Q_uv=U_uv conjugate(U_vu). The formula is proved by expanding f=r zeta x/(1-r zeta a), using E f=E f^2=0,

 E|f|^2=r^2|x|^2/d0,
 E[f|f|^2]=r^4 |x|^2 x conjugate(a)/d0^2,
 E|f|^4=r^4 |x|^4(1+r^2t)/d0^3.

These exact identities identify the necessary joint control. They do not prove that (16)'s coherence survives asymptotically or that universality fails.

## 5. A solved boundary marginal and why it does not solve the radial target

Keep coordinate j and eliminate all other coordinates at unit-modulus phases. The effective scalar is

 H_j(zeta)=U_jj+U_j,S D_S(I-U_SS D_S)^(-1)U_S,j,
 S={1,...,N} minus {j}.                                    (17)

For almost every phase vector the denominator is nonzero. Indeed it is a nonzero trigonometric polynomial with constant coefficient 1, whose zero set has Haar measure zero (one-variable polynomial zeros and induction/Fubini prove this). The Schur complement of a unitary with unitary feedback is unitary, so |H_j|=1 almost everywhere.

For all variables inside the polydisk the transfer function is bounded by one, by the energy proof (5) with diagonal feedback. Its holomorphic moments have the mean-value property and constant term U_jj^p. Radial dominated convergence therefore gives

 E H_j^p=U_jj^p, p>=0.                                    (18)

Together with conjugation these are every Fourier coefficient of a measure on the unit circle, so the exact law is the Poisson kernel centered at U_jj:

 density(theta)=(1-|U_jj|^2)/|exp(i theta)-U_jj|^2

relative to dtheta/(2pi), whenever |U_jj|<1. When |U_jj|=1 the law is its point mass. The explicit bound

 sup_theta |density(theta)-1| <= 2|U_jj|/(1-|U_jj|)         (19)

shows that the actual FM-021 flatness makes this entire boundary marginal uniform at O(N^(-1/2)), uniformly in j, at a non-effective startup threshold. This conclusion is genuinely obtained for the prescribed map, but it concerns a boundary marginal, not (9).

Control: for the cyclic-permutation unitary C_N with N>=2, all proper prefix compressions in the natural cycle order are strictly triangular, hence h_k=0 for k<N, and

 h_N(z)=z^(N-1) product_(j<N) zeta_j.

The boundary scalar is exactly uniform, its total angular delay for f_N=z h_N is exactly N, and all positive moments in (18) agree with U_NN=0. Nevertheless (8) gives exactly

 N^(-2)sum_m exp(-2sm/N) B_N(m)=1/(exp(2s)-1),              (20)

because B_N(m)=N^2 if N divides m and zero otherwise. This differs from (9). The control violates the actual flatness/mixing hypotheses; it falsifies only closure from the boundary scalar law/mean delay. It does not refute those hypotheses jointly or the actual BGS target.

## 6. All principal-minor moduli still do not determine the phase form factor

This strengthens the location of the preexisting determinant-covariance boundary within the independent-coordinate-phase model itself. Let

 U_+= (1/3)[[1,1+sqrt(3),1-sqrt(3)],
            [1-sqrt(3),1,1+sqrt(3)],
            [1+sqrt(3),1-sqrt(3),1]],
 U_-=I_3-(2/3)11^T.

Both are real orthogonal. Their determinants are +1 and -1. Every singleton principal minor equals 1/3; every two-element principal minor equals +1/3 and -1/3, respectively. Hence for every subset I their principal-minor squared moduli are identical. Consequently they have identical complete multivariate phase-averaged characteristic-polynomial covariance, not merely identical degree-aggregated covariances.

Yet direct degree-two Newton expansion gives

 E|Tr[(D U_+)^2]|^2=17/27,
 E|Tr[(D U_-)^2]|^2=65/27.                                (21)

Indeed the x_i^2 coefficients are 1/9 for both, while each x_i x_j coefficient is -4/9 or +8/9. Summing their squared moduli proves (21). This is a finite exact witness to loss of the phases of minors. It is not an asymptotic family satisfying FM-021/FM-022, and it is not offered as such. It does not duplicate the earlier deleted-clock witness's probability space.

## 7. Actual remaining input and research disposition

The route remains OPEN at (9), equivalently (11)-(12). A concrete sufficient next theorem is a microscopic joint radial law or direct summed energy bound for the evolving scalar Schur functions, after random-order revelation. Equations (15)-(16) specify the first two conditional moments that such a theorem must retain. The pointwise boundary marginal (18) is already solved and cannot replace the radial law.

No bound on the evolving Schur entries, random denominators, their joint coherences, or the sum in (11) has been derived from FM-021/FM-022. The accepted low-Hamming centered trace estimate does not by itself provide one. The unresolved step is not a nonlinear supersymmetric gauge change or summability of fixed diagrams: the scalar representation is exact globally in the open disk. Its difficult boundary layer is now an explicit ordinary positive resolvent observable.

Prior checks: searched canonical mathematics, record, literature, and the resolvent-flow supplement for martingale/dilogarithm/scalar Schur phase identities; no matching reduction was found in that searched corpus. Read the existing occupation recurrence, deleted-clock determinant-covariance boundary, balanced phase source audit and domain addendum. Newton identities, Schur complements, scalar phase integration, Poisson kernels and martingale orthogonality are standard tools; no world novelty is claimed. No imported graph universality theorem or new external theorem is a dependency. The one-dimensional Poisson-kernel conclusion is the standard analytic-inner-function/harmonic-measure consequence reconstructed here, not a novelty claim. The cyclic-permutation clock is a standard control. A short web discovery check returned no additional load-bearing theorem and is not an exhaustive literature audit.


## 8. Executed verification and frozen handoff

`checks.py` uses exact Q(i), Q(sqrt(3)), and rational symbolic residues. It checks 18 logarithmic increment coefficient identities and 18 independently expanded positive-energy coefficient identities at N=3 and powers 1 through 6; six literal Schur determinants and six contraction-energy losses at r=1/3,2/3; one unit-circle scalar-inner identity; three independent contour-residue second/fourth-moment pairs; all eight principal-minor pairs in the 3x3 witness; and 38 cycle powers at N=2,3,5,7. All checks passed. No actual fixed-tau finite matrix was numerically approximated.

The bounded run uses a 70-second wall limit, 60-second CPU limit, 2 GiB address-space limit, one CPU affinity and single-thread library settings. `run_checks.py` records exact commands, source hashes before/after, runtime, exit state and output hashes in `execution_manifest.json`. `source_manifest.json` pins the read source files, including the inherited accepted fractional-Hamming review and synthesis. These finite controls verify the stated algebra only; they do not prove the N-limit or supply independent review of this candidate.

Status for a fresh reviewer: audit (1)-(19), especially the derivative-free sufficiency (13), the coefficient m/N normalization in (8)-(12), the bounded-polydisk-to-boundary step in (18), and the r^4 coherence coefficient in (16). The scalar radial limit (9)/(11) is explicitly OPEN and must not be promoted with the exact identities.
