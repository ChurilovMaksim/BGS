---
title: "The full bounded recurrence window and a two-scale spectral limit"
author: "WoW research programme"
date: "5 September 2026"
---

# Status

Project proof extending the finite normal form in [the Floquet note](pell_floquet_normal_form.md). This is a recurrence-scale one-eigenvalue statement, not a two-eigenvalue correlation theorem or microscopic BGS. No priority claim or general Lean formalization is made.

# 1. Definitions

Use the Pell family and odd-space normalized trace tau_-=Tr_-/d_N, with d_N=(N-1)/2. Write U_epsilon=exp(i epsilon B)U_0, U_0^K=I, Bbar=K^(-1)sum_j U_0^j B U_0^(-j), and X_K=sqrt(K/2)Bbar. Let tau be fixed and epsilon=tau/sqrt(2K). The finite comparison proved in the Floquet note gives, for every integer t,

    |tau_-(U_epsilon^t)-tau_-(exp(i t epsilon Bbar)U_0^t)|
        <= 12 |t| epsilon^2/sqrt(K).                         (1)

The same note proves M_(2r,K)=tau_-(X_K^(2r)) -> (2r-1)!! for each fixed r. These are separate inputs; no characteristic-function convergence rate beyond them is assumed.

# 2. Uniform nonresonant twisted moments

For 1<=s<K and every finite Weyl index v, the full trace of W(v)U_0^s has modulus one. Indeed its affine fixed-point equation has a unique solution because 1-h^s is a unit modulo N. The parity-inserted trace has modulus one for the same reason with 1+h^s. Therefore

    |tau_-(W(v)U_0^s)| <= 1/d_N.                            (2)

The expression means the parity-projected full trace; individual W(v) need not preserve the odd subspace. Its use in expansions of parity-preserving sums is legitimate by linearity.

There are (2K)^l Weyl words in X_K^l, each with coefficient modulus (2K)^(-l/2). Equation (2) consequently implies, uniformly in 1<=s<K,

    |tau_-(X_K^l U_0^s)| <= (2K)^(l/2)/d_N.                 (3)

This estimate is valid over the composite Pell ring and does not invoke prime-field character-sum cancellation.

# 3. The resonance comb

**Theorem 1.** For every fixed C>0 and real tau,

    sup_{|t|<=CK, K does not divide t} |tau_-(U_epsilon^t)| -> 0,      (4)

whereas, for each fixed integer m,

    tau_-(U_epsilon^(mK)) -> exp(-m^2 tau^2/2).              (5)

**Proof.** It suffices to treat t>=0 and use adjoints for negative times. Write t=mK+s, with 1<=s<K, and put u=t tau/K. Then |u|<=A=C|tau| and exp(i t epsilon Bbar)=exp(i u X_K).

For each positive integer r, Taylor's integral remainder on the real axis gives the global scalar inequality

    |exp(iux)-sum_(l=0)^(2r-1) (iux)^l/l!|
        <= |u x|^(2r)/(2r)!.

Since X_K and U_0 commute, spectral calculus bounds the normalized trace of the remainder times U_0^s by A^(2r)M_(2r,K)/(2r)!. Inserting (3) into the polynomial part and using (1) yields the explicit finite bound

    |tau_-(U_epsilon^t)|
      <= 6C tau^2/sqrt(K)
         + (1/d_N)sum_(l=0)^(2r-1) (A sqrt(2K))^l/l!
         + A^(2r)M_(2r,K)/(2r)!.                           (6)

For fixed r the first two terms tend to zero, because d_N grows exponentially in K. The limiting upper bound of the last term is

    A^(2r)(2r-1)!!/(2r)! = A^(2r)/(2^r r!),

which tends to zero as r tends to infinity. The order of limits is first K and then r; no growing-order moment estimate is inserted. This proves the uniform statement (4). Statement (5) is the resonance law already obtained from the normal form and the Gaussian moment limit. End of proof.

The theorem resolves the entire bounded time window t/K, not just isolated prescribed off-resonant times. It gives no uniform statement for |t|/K tending to infinity.

# 4. A two-scale one-eigenvalue measure

Write the actual eigenvalues of U_epsilon as exp(i theta_l), with theta_l in R/(2pi Z). Define a probability measure on the product of two circles by

    nu_K=(1/d_N)sum_l delta_(exp(i theta_l),exp(i K theta_l)).

**Corollary 2.** The measures nu_K converge weakly to

    Haar measure on the first circle
        times the wrapped-normal law with parameter tau on the second.   (7)

**Proof.** The Fourier coefficient with fixed integer indices (a,b) is tau_-(U_epsilon^(a+bK)). If a is nonzero, K does not divide a+bK for all sufficiently large K, and its absolute time is at most (|a|+|b|+1)K. Thus (4) gives limit zero. If a=0, (5) gives exp(-b^2 tau^2/2). These are precisely the Fourier coefficients of the product measure in (7). Density of trigonometric polynomials on the compact two-torus proves weak convergence. End of proof.

For tau=0 the second factor is the point mass at 1. For tau nonzero it has the wrapped-normal density stated in the Floquet note. The global original eigenphase is therefore asymptotically uniform while its recurrence-scale position has a nonuniform law, and these two coordinates become independent in the limiting one-eigenvalue measure.

This is NOT independence of distinct eigenvalues. The measure samples the same eigenvalue at two scales. It must not be described as a two-point correlation limit or a proof of local Poisson/GOE/CUE statistics.

# 5. Relation to the microscopic obstruction

The separate [clustering theorem](pell_microscopic_clustering.md) applies when epsilon_K sqrt(K) tends to zero. It establishes collapse of globally unfolded nearest-neighbour spacings and divergence of microscopic close-pair counts. Here tau is fixed and the recurrence spectrum is nontrivial. The two results distinguish subcritical clustering from the critical mesoscopic resonance law without asserting a locally universal critical spectrum.

The critical quantum kick corresponds to a vanishing classical kick. A fixed nonzero classical perturbation and Heisenberg-scale joint trace estimates remain outside both results. Finite experiments should retain off-resonant and resonant traces separately, including visible finite-size deviations, rather than fitting a Gaussian curve to all times.
