# Current working theory

This document is the active dependency graph after the 2026-09-03 full-repository audit.  The detailed historical notebook remains in `docs/THEORY_FULL_PRE_REBUILD.md` and `archive/legacy-workspace/THEORY.md`; those documents are research provenance and contain superseded theorem labels.

## 1. Rank-1 computational reduction

For the split-prime cat-map design, the working Hecke basis is represented by multiplicative characters.  The current computational kernel encodes matrix elements through twisted Jacobi sums

`J(chi, psi; q) = sum_{x != 0,1} conj(chi)(x) psi(x-1) e_N(qx)`.

The load-bearing implementation is `code/math/twisted_jacobi.py`, with lower-level character/coset primitives in `code/math/jacobi.py`.  The R82 preserved data and independent new-prime scalar regression are reproducible finite-N checks.  Historical theorem labels are not themselves proof certificates.

## 2. Exact `k=2` fluctuation layer

For the annihilator coset `S`, the checked reduction is

`A_S(q) = m^2 ((N-2) + S_off(q))`,

with an off-diagonal constraint set `P` satisfying exactly

`|P| = (K-1)(K-2)`

at the audited finite designs.  The direct implementation is `code/verification/h3_k2_exact_reduction.py`; the corresponding formal source is `formal/Bgs/K2Reduction.lean`.  This layer does not require the later M1/Möbius-fiber claim.

## 3. Spectral evidence

The desymmetrised matrices exhibit GOE-like nearest-neighbour spacing at retained designs and matched GOE number variance at `N=19489,K=29`.  These are numerical targets/falsifiers.  They do not replace a limiting analytic fluctuation or local-law argument.  The historical `N=95419` ratio-vs-spacing test is quarantined because it compared a gap-ratio statistic with the ordinary spacing CDF.

## 4. Exact energy object at the M1 boundary

Write the twist-pair pieces as `A_tau`.  The load-bearing energy is

`|| sum_tau A_tau ||^2`

and expands as

`sum_tau ||A_tau||^2 + sum_{tau != sigma} <A_tau, A_sigma>`.

A valid proof may remove the cross sum only after proving the relevant orthogonality, covariance cancellation, or a quantitative bound strong enough after summation.  The historical M1 argument did not establish this step.

## 5. The R86 trace-fluctuation shortcut is not available

The preserved R86/R87 draft tries to reduce the local-law problem through moments of `M_q=C_q+C_q^*`.  Its first displayed expansion applies the scalar binomial theorem to two matrices without a commutation theorem.  In general all words in `C_q` and `C_q^*` must be retained with their order.  Its subsequent adjacent-pair independence claim is also unproved.  Therefore that draft cannot be used as a bridge around M1.

## 6. Correct M1 task

A repaired M1 must:

1. fix one additive/multiplicative Fourier normalisation;
2. derive the exact twist-pair expansion before estimating;
3. keep every ordered cross-twist term until a theorem removes or bounds it;
4. prove the divisor/character statement excluding perfect-power degeneracies wherever the finite-field estimate requires it;
5. state explicitly which of `N`, `K`, and the sector dimension vary;
6. sum every bound with the true number of twists and the true normalisation;
7. produce a remainder that actually tends to zero in the stated asymptotic regime;
8. use the existing finite-N computations only as calibration/falsifiers.

Until those checkpoints are met, M1 is `OPEN GAP`.

## 7. Higher moments and rank-2 material

The repository contains many useful finite-N higher-moment identities, automaton experiments, and rank-2/Sp4 computations.  Exact finite-design identities may be used as lemmas about those finite designs, but no historical `[PROVEN]` string should be silently promoted into an asymptotic theorem.  In particular the rank-2 diagonal/coset identities at `N=53` are calibration points for a possible general mechanism, not a completed M4/general-BGS argument.

A downstream route is legitimate only if it proves an estimate independent of the invalid M1/R86 promotions and states its assumptions on its own terms.
