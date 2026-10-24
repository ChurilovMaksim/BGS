# Original ordered two-pair channel: logarithmic-loss gap

**Claim ID:** `BGS-FM-020`. **Base:** `fa007c498fe116a814a90aa3215cfd65b1f2a154`.
Dependencies: mathematics/fixed-map/collective_diffusion_gap.md, D5–D8 and D17–D19. This proof does not use D2 or alter the noise law. Status: project analytic proof with independent internal audit. See [review](../../archive/record/original_channel_gap_review_20261006.md) and [programme](../../archive/record/original_channel_gap_program_20261006.md).

## Statement
For every odd N>=3, write ell_N=1+log N and lambda_N=(1024 ell_N)^(-2). For every u>=0 and every unitary U, the original m=1 channel satisfies

  ||exp(-u A_N) exp(-u B_N) Q_N|| <= 1 - (1-exp(-2u lambda_N))/50.

Consequently the unit-circle singular gap after multiplication by Ad(U tensor U) is at least (1-exp(-2u lambda_N))/50. For u_N=N^(-alpha), 0<alpha<1, this displayed lower bound is asymptotic to u_N/(25*1024^2 ell_N^2), and hence dominates N^(-1). This is an auxiliary common-noise two-copy statement, not deterministic BGS or noise removal.

## 1. Uniform low-eigenvalue count
Let A_kappa be D6's restriction to one N²-dimensional total-Weyl block. Let P_A project onto its exact kernel, and let R_A=1_(0,lambda](A_kappa). We prove

  rank R_A <= 4 N sqrt(lambda) (1+log N)                         (1)

for every lambda>0, uniformly in kappa. The same holds for B.

Set k to the centered representative of kappa_a, theta=pi k/(2N). Apply D8's translation and gauge, and diagonalize the b-shift. The coordinate y and twisted Fourier coordinate eta run over the same centered N-point grid: integral if k even, half-integral if k odd. The eigenvalues of A are exactly

  E(y,eta)=8N²[cos²(theta) sin²(pi y/N) sin²(pi eta/N)
                   +sin²(theta) cos²(pi y/N) cos²(pi eta/N)].   (2)

The Fourier shift eigenvalues are exp(2pi i eta/N), with the antiperiodic half-integer twist when k is odd. Since cos²(theta)>=1/2 and |sin(pi t/N)|>=2|t|/N on the centered interval, E<=lambda implies

  |y eta| <= R := N sqrt(lambda)/8.                           (3)

For nonzero y and eta, the number of admissible eta for each y is <=4R/|y|. Indeed either there are none, or a centered integral/half-integral grid has at most 4t nonzero points with |eta|<=t. Also

  sum_(y != 0) 1/|y| <=4(1+log N).

For the integral grid this follows from twice the harmonic sum. For the half-integral grid, the two possible points of absolute value 1/2 contribute at most 4; the remaining terms are bounded by 2 integral_(1/2)^(N/2) dx/x=2 log N: each tail term 1/(r+1/2), r>=1, is bounded by the integral on [r-1/2,r+1/2], and overcounting the unmatched endpoint is harmless. Thus the sum is <=4+2 log N<=4(1+log N). Thus the number of nonaxis modes is <=16R(1+log N)=2N sqrt(lambda)(1+log N).

If k is odd, neither grid contains zero and this completes the count. If k=0, the axes y=0 or eta=0 are exactly the kernel and are excluded from R_A.

It remains to count axes for nonzero even k. Here |k|>=2 and |sin(theta)|>=|k|/N. At y=0, (2) gives E>=8 k² cos²(pi eta/N). Put d=N/2-|eta|, a positive half-integer. Since cos(pi eta/N)=sin(pi d/N)>=2d/N,

  E>=32 k² d²/N².

Thus d<=D=N sqrt(lambda)/(sqrt(32)|k|). The number of centered integer eta satisfying this is <=4D: if D<1/2 there are none, and otherwise each endpoint contributes at most D+1/2<=2D. The eta=0 axis has the same bound. Their union therefore has at most 8D= sqrt(2) N sqrt(lambda)/|k| <=N sqrt(lambda) modes. Double-counting their intersection only makes this upper bound safer. Adding to the nonaxis count proves (1), with room to spare.

## 2. Low-spectral projection angle
Let Pi_A=P_A+R_A=1_[0,lambda_N](A_kappa) and analogously Pi_B. Since (1) gives rank R_A,rank R_B<=N/256, while the exact kernels have rank at most 2N-1, all required cross terms can be estimated.

In the original D6 coordinates an eigenbasis of A is delta_a tensor Fourier_j, and one of B is Fourier_i tensor delta_b. Every overlap has absolute value 1/N. Consequently for spectral projections onto any subsets of these bases,

  ||E F|| <= ||E F||_HS = sqrt(rank(E) rank(F))/N.              (4)

This applies to P_A,R_A,P_B,R_B even when eigenvalues have multiplicity, by choosing these explicit diagonalizing bases. The bases need not be those used in the count.

On Q_N within each block, D19 gives ||P_A P_B Q_N||<=N^(-1/2); the product is zero outside kappa=0. Every spectral projection reduces Q_N, because the two common invariants lie in both exact kernels. Expanding Pi_A Pi_B into four terms and using (4) on the three terms containing R gives

  ||Pi_A Pi_B Q_N|| <= N^(-1/2)+2 sqrt(2/256)+1/256
                    <=1/sqrt(3)+sqrt(2)/8+1/256 <4/5.        (5)

Therefore, on Q_N,

  2I-Pi_A-Pi_B >= (1/5) I.                                  (6)

For completeness, if projections E,F have ||EF||<=c on this reducing space, the map x -> (Ex,Fx) has squared norm <=1+c: its product with its adjoint has diagonal identity operators on ran E and ran F and off-diagonal blocks EF and FE. Thus E+F<=(1+c)I, proving (6).

All bounds are uniform in kappa, hence extend to the direct sum.

## 3. Ordered product loss
Set F=exp(-uA_N), G=exp(-uB_N), and a=1-exp(-2u lambda_N). Spectral calculus and (6) imply, on Q_N,

  (I-F²)+(I-G²) >= a(2I-Pi_A-Pi_B) >= a I/5.                (7)

For unit x in Q_N put beta=1-||FGx||². Both 1-||Gx||² and ||(I-F²)^(1/2)Gx||² are <=beta. Also ||(I-G)x||²<=1-||Gx||²<=beta. Since ||(I-F²)^(1/2)||<=1, the triangle inequality gives ||(I-F²)^(1/2)x||<=2sqrt(beta). Substituting x in (7) gives a/5<=5beta, or beta>=a/25. Therefore

  ||FG Q_N||<=sqrt(1-a/25)<=1-a/50.

Collective conjugation by U tensor U is unitary and reducing on Q_N, so it leaves this norm unchanged. The reverse triangle inequality gives the stated singular gap, uniformly on the unit circle and also for I-z C with |z|<=1.

## Scope and originality check
The kernel-angle mechanism D19 is existing project work. The additional step is the uniform low-eigenvalue count and its mutually-unbiased-basis angle estimate. No world-priority claim is made. The [bounded primary-source comparison](../../literature/original_channel_gap_sources_20261006.md) credits alternating diagonal twirls, Brownian moment generators and standard Fourier-projection uncertainty; none of its checked theorems is imported into this proof. This keeps exactly the original m=1 law, unlike D20's refined regulator; it does not control quenched powers, higher-copy sectors, nonlinear determinant functionals, or the deterministic signed Heisenberg trace sum.
