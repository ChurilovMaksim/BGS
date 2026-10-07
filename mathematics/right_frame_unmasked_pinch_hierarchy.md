# BGS-TRACE-028: actual right frame and complete unmasked pinch hierarchy

This is the separately independently accepted continuation of TRACE-024. It preserves the unchanged literal odd-N fixed-tau=10^-80 quantization, physical midpoint half-shift, centering, ordinary HS space and row-minus-column slice reindexing. The original ZIP and author's 222-control checker were inaccessible and were not replayed. Four authorized Markdown exports were byte/hash verified; fresh independent controls, rather than unavailable author receipts, support this acceptance.

Put (A_c)_(y+c,y)=U_(y+c,y), C e_c=A_c*, R_U X=XU, T=Ad(U), D=sum_c P_c T P_c and D0=D|I^perp. For each fixed integer r>=1,

    ||C* R_U^r C||<=C_r sqrt(log(2N)/N).

The exact transpose identity uses a complex-linear transpose and c->-c permutation; inherited left-frame analytic geometry is checked for the transposed kernel rather than silently substituted for right multiplication. Constants depend on fixed r; there is no growing-r rate or effective startup. For any arbitrary N-dependent unitary B, fixed throughout the averaged coherent run,

    F_n(B)=(1/N)sum_b |Tr(U^n K_b B)|², K_b=Z_b U Z_b*,
    sum_(n=A)^(A+M-1) F_n(B)<=N[M gamma_(L,N)+C_flat L].

The interval start and B are arbitrary. Uniformity over fixed B does not permit an uncontrolled n-dependent B_n.

For occupation phases theta, T_theta=Ad(Z_theta U), D_theta=V_theta D and

    G_j(n;theta)=Tr_H[D_theta T_theta^n1 ... D_theta T_theta^nj],
    A_(j,N,m)(theta)=binom(m-1,j-1)^(-1)sum_(sum n_i=m-j)G_j(n;theta).

Every gap n_i>=0, repeated coordinate, repeated modulation and periodic word remains included. The rooted slot sum is exactly S_(j,N,m)=binom(m,j)A_(j,N,m). For every fixed j>=1 and bounded positive compact-band weight, the N^-2 weighted bands of A vanish both at theta=0 and after exact phase averaging, hence for signed occupation subtraction. Raw composition sums have normalization N^(-(j+1)); raw rooted-slot sums have N^(-(j+2)). No raw arbitrary-weight coefficient bound at N^-2 is asserted. The untwisted A estimate separately holds uniformly for j_N=o(N).

The NEW ordinary Schatten statement is

    ||D0||_(S3)^3=o(N),

from accepted compactness, ||D0||<=1 and ||D||_(S2)^2<=C_flat N. For EVERY j>=3 word,

    |G_j(n;theta)-1|<=||D0||_(S3)^3=N eta_N, eta_N->0,

uniformly in theta, all gaps and j, including growing j. The scalar identity contribution 1 is retained exactly. Three S3 factors and bounded remaining factors are essential; this is not a compactness-only j=1,2 bound. Combining the actual/annealed first two insertion orders with that tail closes every complete UNMASKED convex insertion mixture whose nonnegative insertion mass is <=1, uniformly for every z_N in [0,1], including logarithmic typical insertion counts.

Thus the complete actual and annealed insertion corrections in

    Tr_H[z_N T_theta+(1-z_N)D_theta]^m
      =z_N^m |Tr(Z_theta U)^m|² + insertion correction

have vanishing N^-2 bounded compact-band aggregates. This identifies their signed unmasked correction relative to the scalar-damped original occupation difference; it does not estimate the undamped zero-insertion spectrum.

[Exact exported proof](../evidence/wave3_checked_20261007/raw/right_overlap/authorized_exports/right_overlap_and_unmasked_insertions.md), (1)-(23); [fresh independent review](../evidence/wave3_checked_20261007/raw/right_overlap/independent_review.md). The right-frame, fixed-B, exact slot multiplicities, separated annealed bounded-factor extension and S3 tail are accepted together. The author's unavailable 222-control suite is not certified. Independent controls retain their bounded exact scope and never establish analytic limits by extrapolation.

Closed: complete unmasked separated and convex insertion hierarchy at the stated normalizations. OPEN: Hamming/high-switch coefficient extraction, source weights/derivatives and rates, masked separated sums, marked-switch boundary T16, undamped zero-insertion/deconvolution comparison, absorbed microscopic Ward (13), balanced microscopic law, TRACE-005, higher factorial comparison and deterministic BGS. No growing-r stationary phase, aggregate rate, practical startup, priority or formalization claim.
