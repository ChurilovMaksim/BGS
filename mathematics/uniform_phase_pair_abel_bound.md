# A dimension-uniform Abel bound from phase spectral averaging

7 October 2026. Author proof, independent review pending. U is an arbitrary deterministic N by N unitary; D has independent uniform U(1) diagonal entries. This is an a priori annealed estimate and does not identify the CUE limit. No flatness, mixing, reversed-gap, or BGS hypothesis is needed.

## Theorem

Put B_N(m)=E|Tr(DU)^m|^2. For every 0<q<1,

0 <= sum_{m>=1} q^m B_N(m) <= N(1+q)/[2(1-q)].                 (A)

Consequently, for every s>0,

F_N(s) := N^-2 sum_{m>=1} exp(-2sm/N) B_N(m)
       <= (1/(2N)) coth(s/N) <= 1/(2s)+1/(2N).                (B)

In particular limsup_N F_N(s)<=1/(2s). The proposed CUE limit is (1-exp(-2s))/(4s^2), strictly more information than this upper bound. Diagonal U gives the Poisson comparison F_N(s)->1/(2s), so no improvement to the CUE value is possible without additional assumptions.

## 1. Conditional spectral averaging

Write V_theta=exp(i theta P_i) V_0, where P_i is the coordinate rank-one projection and the other phases are fixed. For every connected arc A, with normalized length p_A=|A|/(2pi),

integral <i, 1_A(V_theta) i> dtheta/(2pi) = p_A.               (1)

Proof: for every m>=1, <i,V_theta^m i> is a polynomial in exp(i theta) with zero constant coefficient. Every coordinate path starts at row i and therefore visits that row at least once. Its phase integral is zero. The negative Fourier coefficients are conjugates, so the averaged scalar spectral measure has all nonzero Fourier coefficients zero and total mass one; it is normalized Haar measure. Approximation of arc indicators or uniqueness of finite measures gives (1), including arcs with endpoints interpreted consistently. It follows that E N_A=N p_A, where N_A=Tr 1_A(V).

## 2. Cyclic rank-one interlacing

For any two choices theta,theta' and any connected proper arc B,

|N_B(V_theta)-N_B(V_theta')| <= 1.                            (2)

An elementary proof first treats simple spectrum with positive overlap weights. Write the eigenvalues of V_theta' as exp(i phi_j), and w_j=|<i,v_j>|^2>0. The rank-one determinant lemma shows that the eigenvalues of exp(i t P_i)V_theta' away from the old ones solve

sum_j w_j cot((phi-phi_j)/2) = cot(t/2).

The left side is strictly decreasing from +infinity to -infinity in each consecutive cyclic gap. There is exactly one new eigenvalue in each such gap, so the two spectra cyclically interlace and their counts in any connected arc differ by at most one. Zero overlaps, repeated eigenvalues and endpoint cases follow by an arbitrarily small generic approximation; endpoints have zero ensemble probability by (1). The whole-circle case has identical count N.

This is the standard rank-one unitary interlacing mechanism. The argument above proves the finite-matrix form actually used and does not import a localized-operator hypothesis.

## 3. Nested-arc factorial estimate

If A is contained in B and both are connected arcs (the whole circle is allowed), then

E[N_A(N_B-1)] <= N^2 p_A p_B.                                (3)

Indeed,

N_A(N_B-1) = sum_i <i,1_A(V_theta)i> (N_B(V_theta)-1).

Resample only theta_i as an independent uniform theta_i'. By (2), N_B(V_theta)-1<=N_B(V_theta'). Multiply by the nonnegative spectral weight and average. Conditional on all other phases and theta_i', the latter count is independent of theta_i. Formula (1) integrates the weight to p_A. The resampled matrix has the original law and E N_B=Np_B. Summing over i proves (3).

The left side is exactly the expected ordered distinct-eigenvalue count with the first point in A and the second in B: nesting makes the removed diagonal term N_A. Thus its nonnegativity is automatic even when N_B=0.

## 4. Positive layer-cake integration

Let P_r(phi)=(1-r^2)/|1-r exp(i phi)|^2, 0<r<1. Its superlevel sets are connected nested arcs centered at zero, or the whole circle, or empty. Define

Y_r=sum_j P_r(phi_j),

where exp(i phi_j) are the eigenvalues of V. By Tonelli and (3),

E sum_{j!=k} P_r(phi_j)P_r(phi_k)
 = integral_0^infinity integral_0^infinity E[N_{A_t}N_{A_u}-N_{A_t intersect A_u}] dt du
 <= N^2 [integral_0^infinity p_{A_t}dt]^2
 = N^2.                                                       (4)

This is the place where nested arcs matter. No assertion of a pointwise two-point density bound, or a product bound for arbitrary disjoint arcs, is used.

The diagonal term is exact by rotation invariance / spectral averaging:

E sum_j P_r(phi_j)^2 = N integral P_r(phi)^2 dphi/(2pi)
                    = N(1+r^2)/(1-r^2).                       (5)

The ensemble is invariant under multiplying V by a common scalar phase. Since

P_r(phi)=1+sum_{m>=1}r^m(exp(i m phi)+exp(-i m phi)),

orthogonality of distinct total Fourier charges gives

E Y_r^2 = N^2+2 sum_{m>=1} r^(2m) B_N(m).                      (6)

Combining (4)-(6), then setting q=r^2, proves (A). Finally coth x<=1+1/x proves (B).

## 5. Source and measure consequences

For the exact determinant-ratio generating function G_U from compact_projector.md,

ab partial_c partial_d G_U(a,b;c,d)|_{c=a,d=b}
 = sum_{m>=1}(ab)^m B_N(m).

Thus (A) is a genuine uniform bound on the complete differentiated source observable, including every boundary contribution and cancellation. It is not an estimate of the absolute values of the compact projector's individual sectors.

Define the positive measure mu_N=N^-2 sum_{m>=1}B_N(m) delta_{m/N}. Then:

- For every epsilon>0, limsup_N mu_N([0,epsilon])<=e epsilon, by using s=1/(2epsilon) in (B). Thus no subsequential limiting atom can occur at zero.
- For s>0, integral_{t>R} exp(-2st)dmu_N(t) <= exp(-sR) F_N(s/2). Hence the exponentially weighted tail is uniformly small as R increases.
- F_N extends holomorphically to Re s>0 and |F_N(s)|<=1/(2 Re s)+1/(2N). Therefore the family is locally bounded and normal there. Every fixed number of s derivatives is locally uniformly bounded by Cauchy's formula, or directly by positivity.
- If a separate argument establishes the CUE limit on any set with an accumulation point strictly inside Re s>0, normal-family uniqueness can extend that convergence throughout the right half-plane. This is conditional; fixed m trace limits, or an asymptotic expansion as s tends to infinity, do not provide such an accumulation set.

These properties supply tightness and derivative bounds that a microscopic identification argument can use. They do not identify its subsequential limits. Poisson, the CUE candidate, and cyclic-clock controls all satisfy (A).

## 6. Cheap exact controls and scope

N=1: B_1(m)=1, so the left side is q/(1-q), below the upper bound by 1/2.

Diagonal U in any dimension: B_N(m)=N, so the left side is Nq/(1-q), below the bound by N/2. This saturates the limiting upper bound in (B).

A single N-cycle permutation: B_N(m)=N^2 if N divides m, and zero otherwise, so the left side is N^2 q^N/(1-q^N). The claimed inequality is equivalent to 2N q^N <=(1+q)sum_{j=0}^{N-1}q^j, which holds because q^j>=q^(N-1) and 1+q>=2q. Such a clock ensemble has rigid microscopic structure but respects the bound.

These controls rule out interpreting (A) as universality. The actual unchanged BGS matrix inherits the bound simply by being unitary, without using its literal fixed coupling or eventual flatness threshold. The separate deterministic off-charge defect is untouched.
