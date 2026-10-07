# Separate author self-audit and independent-review questions

This is self-review of `actual_fixed_lag_overlap.md`, not independent review. No new agents were started during the resumed task. The claimed analytic result is a candidate pending the parent's review.

## Checks of the final argument

1. **Object and orientation.** Derived the displacement-slice frame and K_r entry formula from ordinary Hilbert-Schmidt products. The orbit vector is U^n/sqrt(N), with left multiplication by U. The slice index is row minus column, explicitly the negative of the source charge label in a complete sum; source masks are unchanged. Exact complex rational controls at N=3,5 verify the entry formula, this sign/orientation, orthogonal columns and K_-r=K_r*. They do not rerun the native generator/twirl audit.
2. **No long-time approximation.** The WKB expansion is used only for each fixed lag r inside a block-Gram estimate. The resulting bound holds uniformly over the starting time because the tested orbit vector has norm one. The order of limits is N->infinity at fixed block length, then block length->infinity. No uniformity of C_r in r is assumed.
3. **Error normalization.** The inherited one-step operator remainder is O(N^-3/2). Displacement-slice synthesis has error O(N^-1), and fixed-power telescoping is performed in operator norm before branch expansion. Stationary phase converts r internal sums and r+2 kernels into N^-1 charge-matrix entries; the O(N^-2) entry remainder costs O(N^-1) in operator norm.
4. **Hessian geometry.** The cyclic internal Hessian has spectrum in [-2,-1], including r=1,2. The external mixed vectors have squared norm at most 1/8, so a Schur complement stays in [1/8,1/4] before perturbation. The entire actual Hessian has uniformly small row-sum perturbation; this estimate is independent of fixed r because each variable touches only a bounded number of links. During drafting, the coefficient count for the exceptional second factor was corrected from four to five; the final 64 eta bound retains margin. Exact Jacobian-envelope checks through r=16 agree with the final count.
5. **Lattice boundaries and aliases.** Smooth internal cutoffs are inserted using the periodicity of the FULL sampled parametrix, before expanding its nonperiodic individual branches. Poisson summation retains all integer aliases. Strong concavity gives a unique global critical point for each alias, finitely many aliases near the common compact support, and summable nonstationary tails. Linear aliases leave the full Hessian unchanged. The final TT* phase increments are below 1/3, bounded away from all integers; endpoint terms in column summation by parts are included.
6. **Literal model.** The source provides the raw odd-N four-branch identity and Hamilton-Jacobi evolution for the physical half-shifted symbol. The actual tau=10^-80 yields the stated C^2 phase bound. No visible rescaling of tau, diagonal-kick replacement, arithmetic-dimension restriction, or noise change is used.
7. **Scope of conclusion.** Positivity is used only for the untwisted one-pinch sum. The occupation-subtracted corollary uses the new annealed theorem supplied by the parent (manifest recorded in `source_bindings.json`), not a discarded occupation constraint. Hamming and high-switch masks are not covered. Complete pair and higher factorial limits are not inferred.

## Most important questions for an independent reviewer

- Does the inherited parametrix, including a_1, have exactly the sampled periodicity and global Hessian bounds used in Sections 3 and 6? The relevant source sections are reproduced in the packet.
- Independently derive the phase (11), the cyclic Hessian (12), and boundary vectors (16), including r=1,2 and every branch's affine shifts.
- Check that the cutoff-before-expansion construction, finite-alias stationary phase and uniform O(N^-2) entry remainder are sufficient for operator-norm convergence. In particular, test stationary points crossing the cutoff boundary.
- Check the all-starting-time block-Gram argument and its N^-2 compact-band normalization independently of the author's conclusion.
- Confirm that only the supplied one-pinch annealed statement is needed for the signed corollary, and that no consequence for general masks or T16 has been smuggled in.

## Finite evidence boundary

`check_overlap.py` uses exact Gaussian rationals, symbolic differentiation and rational inequalities, with explicit non-assert checks. Normal and optimized runs each record 129 passing checks. The finite ranges are N=3,5 and r=1,...,16 as detailed in their JSON reports. These executions neither certify the inherited WKB input nor prove stationary phase or the N-limit. No new Lean/C++ build or analytic formalization is claimed.
