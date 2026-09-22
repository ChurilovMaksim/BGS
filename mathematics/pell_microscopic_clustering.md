---
title: "Microscopic clustering under subcritical kicks: a spectral concentration criterion"
author: "BGS research programme"
date: "5 September 2026"
---

# Status and scope

This is a project proof, not a claim of priority or a complete Lean formalization. The principal conclusion concerns the individual eigenphases of the actual kicked propagator, without folding or assigning perturbed levels to old eigenspaces. It is a negative local-statistics theorem in a shrinking-kick regime, not a proof or disproof of the conventional fixed-system BGS conjecture. The classical kick amplitude tends to zero with the quantization parameter. Global unfolding here means normalization by the mean spacing of the whole odd spectrum; an additional local-density or clusterwise unfolding is a different question.

The only matrix estimate imported is the explicitly proved finite normal-form inequality in [the Floquet note](pell_floquet_normal_form.md). The spacing and pair-count consequences below have independent finite geometric proofs. No Gaussian limit is needed for these negative conclusions.

# 1. A deterministic finite concentration criterion

Write the circle as R/Z, with distance dist(x,y)=min over integers l of |x-y-l|. Let theta_1,...,theta_d be an arbitrary multiset of d points, including multiplicities, and let L_K={j/K:0<=j<K}. Define

    a^2 = (1/d) sum_l dist(theta_l,L_K)^2.

Order the points cyclically and define globally unfolded nearest-neighbour spacings

    S_l = d (theta_(l+1)-theta_l),  theta_(d+1)=theta_1+1.

For x>0 also define the ordered microscopic pair count

    R_2(x) = (1/d) #{(l,m): l!=m, d dist(theta_l,theta_m)<=x}.

**Lemma 1.** For every 0<w<1/(2K),

    (1/d) #{l:S_l>x} <= 2 a^2/w^2 + K/d + 2Kw/x.             (1)

Put g=max(0,1-a^2/w^2). Then

    R_2(x) >= g^2/(K/d+2Kw/x)-1.                            (2)

**Proof.** Take the K disjoint circular arcs of half-width w about L_K. At most d a^2/w^2 points lie outside them. At most twice this number of nearest-neighbour gaps touch a point outside the arcs. Among remaining gaps, at most K leave an arc, including a possible long wraparound gap with both endpoints in the same arc. All other gaps are contained in the arcs, whose total length is 2Kw. At most 2dKw/x such gaps can have length exceeding x/d. Dividing by d proves (1).

There are at least dg points inside the arcs. Partition each arc into at most 1+2wd/x half-open subarcs of length at most x/d, assigning endpoints to one cell only. The total number M of cells is at most K+2dKw/x. If n_j are the numbers of good points in these cells and G=sum n_j, then all ordered pairs in the same cell are counted in R_2(x). Cauchy--Schwarz gives

    d R_2(x) >= sum_j n_j(n_j-1) >= G^2/M-G.

Now G>=dg, G<=d and M/d<=K/d+2Kw/x. This proves (2). The construction works across the coordinate cut of the circle, by parametrizing each arc separately. End of proof.

**Corollary 2.** Suppose K=K_d, K/d tends to zero and rho=Ka tends to zero. Then the empirical spacing measures converge weakly on [0,infinity) to a point mass at zero, and R_2(x) tends to infinity for every fixed x>0.

More quantitatively, if rho>0 and rho^(2/3)<1/2, choose w=rho^(2/3)/K in (1). Then

    (1/d) #{l:S_l>x} <= K/d+(2+2/x)rho^(2/3).                (3)

If 0<rho<1/4, choose w=2a in (2), so g>=3/4, to obtain

    R_2(x) >= (9/16)/(K/d+4rho/x)-1.                        (4)

If a=0, all points lie on L_K, there are at most K nonzero cyclic spacings, and Cauchy--Schwarz directly gives R_2(x)>=d/K-1. These observations cover that degenerate case without division by a. Since all S_l are nonnegative, (3) implies weak convergence to the point mass at zero. It does not imply convergence of the means: the mean spacing is exactly one for every d, and the rare long gaps carry that mean.

# 2. Spectral matching and the lattice-distance estimate

Use the Pell construction of the Floquet note: K is an odd prime at least 11,

    alpha=1+sqrt(2),  N+F sqrt(2)=alpha^K,  d=(N-1)/2,
    U_0^K=I,  U_epsilon=exp(i epsilon B) U_0,
    B=W(-F,1)+W(-F,1)^*,
    Bbar=(1/K)sum_(j=0)^(K-1) U_0^j B U_0^(-j).

All operators under comparison act on the odd subspace. The finite normal form supplies a unitary V_epsilon with

    ||V_epsilon U_epsilon V_epsilon^* - exp(i epsilon Bbar)U_0||_(2,-)
        <= 12 epsilon^2/sqrt(K).                            (5)

Here ||A||_(2,-)^2=Tr_-(A^*A)/d. It is a normalized Hilbert--Schmidt estimate, not an operator-norm eigenvalue perturbation bound.

For completeness, the required eigenvalue matching is elementary. If U and V are unitary with eigenvalues u_l,v_m and orthonormal eigenvectors e_l,f_m, the matrix |<e_l,f_m>|^2 is doubly stochastic. Expanding the Hilbert--Schmidt norm gives

    ||U-V||_(2,-)^2 = (1/d)sum_(l,m) |<e_l,f_m>|^2 |u_l-v_m|^2.

A doubly stochastic matrix is a convex combination of permutation matrices. This follows by Hall's condition and successive subtraction of a positive perfect matching. Hence there is a matching of the two eigenvalue multisets whose mean squared chord distance is no larger than the displayed norm. No eigenvalue simplicity is required. Circle distance in R/Z is at most one quarter of chord distance, because 2 sin(pi t)>=4t for 0<=t<=1/2.

Since Bbar commutes with U_0, choose simultaneous eigenvectors. If b_l is the Bbar eigenvalue on such a vector, the associated eigenvalue of exp(i epsilon Bbar)U_0 differs from a K-th root of unity by angular distance in R/Z at most |epsilon b_l|/(2pi). Thus the RMS distance a of the actual U_epsilon eigenphases from L_K obeys

    a <= (1/4)(12 epsilon^2/sqrt(K))
         + |epsilon|/(2pi) sqrt(Tr_-(Bbar^2)/d).             (6)

There is a direct finite bound on the remaining second moment. The 2K Weyl indices in sum_j B_j are distinct, because 1-h^j and 1+h^j are units in the Pell construction. Full-space Weyl orthogonality therefore gives

    Tr(Bbar^2)/N=2/K.

Positivity and restriction to the odd subspace yield

    Tr_-(Bbar^2)/d <= (N/d)(2/K)=4N/[K(N-1)].

Consequently (6) proves the explicit estimate

    a <= A_K(epsilon)
      := [3 epsilon^2 + (|epsilon|/pi)sqrt(N/(N-1))]/sqrt(K).
                                                                    (7)

Define Rho_K=K A_K(epsilon). Equations (3) and (4) remain valid with rho replaced by Rho_K: one can use arcs chosen from the upper bound A_K directly. The matching is only an intermediate proof device. No individual eigenvalue labelling is asserted as a physical invariant.

# 3. Microscopic theorem for the kicked propagator

**Theorem 3.** Let K tend to infinity through odd primes, let N be the corresponding Pell modulus, and let epsilon_K be any real sequence with

    |epsilon_K|sqrt(K) -> 0.

On the entire odd subspace, take every eigenvalue of U_(epsilon_K,N), including multiplicity, and normalize nearest-neighbour spacings by the global mean 1/d_N. Then

    (1/d_N)sum_l delta_(S_l)  ==>  delta_0,                  (8)
    R_(2,K)(x) -> infinity  for every fixed x>0.             (9)

**Proof.** N grows exponentially in K, so K/d_N tends to zero. Formula (7) gives

    Rho_K = sqrt(K)[3 epsilon_K^2
                    + (|epsilon_K|/pi)sqrt(N/(N-1))] -> 0.

Apply Corollary 2, including its a=0 case. This proves both conclusions. End of proof.

For an explicit nonzero sequence, epsilon_K=1/K satisfies the theorem. The bound (3) then gives O_x(K^(-1/3)+K/d_N) for the mass of spacings above any fixed x, while (4) gives an Omega_x(sqrt(K)) lower bound for the normalized number of close ordered pairs. These are conservative rigorous bounds, not assertions of optimal asymptotics.

The theorem concerns the original propagator spectrum. Unlike a folded-phase Gaussian law it detects clustering at the microscopic mean-spacing scale. Unlike an isolated-cluster perturbation lemma it needs no operator-norm separation of the old eigenspaces and does not require epsilon_K K^(3/2) to tend to zero. Neither conclusion follows from a global Gaussian density alone; the input is concentration near the K-point spectral lattice and the fact K/d_N tends to zero.

# 4. Interpretation and remaining route

Equations (8)--(9) rule out convergence to a nondegenerate globally unfolded nearest-neighbour law with level repulsion in this particular shrinking-kick family. They also show why normalized Hilbert--Schmidt control can be adequate for a negative microscopic result although it is far too weak, by itself, to prove positive microscopic universality.

This does not contradict a BGS assertion for a fixed classically perturbed map with its symmetries correctly resolved. With the semiclassical convention exp(i action/hbar), our quantum epsilon corresponds to a classical kick amplitude of order epsilon/N; both the scale and its N-dependence are part of the theorem. The odd restriction is the stated spectral space, not a claim that every conceivable arithmetic symmetry has been resolved. Extra local unfolding or deletion of multiplicities must not be silently inserted into (8).

The general concentration lemma, the finite normal form, the wrapped-Gaussian critical law, and the present collapse theorem should therefore be kept as distinct claims. Positive BGS still requires a route at nonvanishing classical perturbation strength, appropriate symmetry resolution, and Heisenberg-scale joint trace control. A proof of this obstruction is not evidence that those harder estimates have been established.

# 5. Reproducible checks

The companion verification checks (1)--(2) for finite circle multisets using exact rational or integer arithmetic, including repeated points, seam-crossing arcs, uniform grids, concentrated points and adversarial configurations. The C++ implementation uses cleared-denominator integer inequalities rather than repeating floating-point spectral calculations. These finite checks test implementation and constants; Lemma 1 supplies the general proof.

Expected companion paths after integration:

- computations/verification/spectral_lattice_clustering.py
- computations/cpp/spectral_lattice_clustering.cpp
- evidence/certificates/spectral_lattice_clustering.json

Compilation and execution status must be recorded separately from the proof status. No unexecuted check may be promoted to a verified certificate.
