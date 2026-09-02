# Current working theory

This document contains the active dependency graph after the 2026-09-02 rebuild. The full historical derivation remains under `archive/legacy-workspace/THEORY.md`.

## 1. Rank-1 computational reduction

For the split-prime cat-map design, the working Hecke basis is represented by multiplicative characters. The current computational kernel encodes matrix elements through twisted Jacobi sums

`J(chi, psi; q) = sum_{x != 0,1} conj(chi)(x) psi(x-1) e_N(qx)`.

The load-bearing implementation is `code/math/twisted_jacobi.py`; the lower-level character-coset matrix primitives are in `code/math/jacobi.py`.

What is currently certified computationally is the reproduction of the preserved R82 data at the audited designs. The existence of old theorem labels in the archive is not itself a proof certificate.

## 2. Exact k=2 fluctuation layer

For the annihilator coset `S`, the checked reduction is

`A_S(q) = m^2 ((N-2) + S_off(q))`,

with an off-diagonal constraint set `P` satisfying exactly

`|P| = (K-1)(K-2)`.

The direct computation is in `code/verification/h3_k2_exact_reduction.py`; the corresponding formal source is `formal/Bgs/K2Reduction.lean`.

This layer does not require the later M1/Möbius-fiber asymptotic claim.

## 3. Spectral evidence

The retained GOE spacing and matched number-variance calculations are numerical evidence for the desymmetrised sector. They are useful targets and falsifiers, but they do not replace an analytic local-law/fluctuation argument. The flawed historical N=95419 ratio-vs-spacing comparison is quarantined and is not part of this evidence set.

## 4. The exact energy object at the M1 boundary

Let the twist-pair contributions be denoted schematically by `A_tau`. The load-bearing energy is

`|| sum_tau A_tau ||^2`

and therefore expands as

`sum_tau ||A_tau||^2 + sum_{tau != sigma} <A_tau,A_sigma>`.

A valid proof may remove the second sum only after establishing the relevant orthogonality or cancellation. The archived M1 argument did not supply that step.

## 5. Correct asymptotic task

A repaired M1 must fix one Fourier convention; write the full twist expansion before estimating; retain every cross-twist term until a theorem removes or bounds it; state explicitly which of `N`, `K`, and `m` vary; prove a remainder that actually tends to zero; prove the nontrivial-character/perfect-power exclusion where required; and use finite-N computations only as falsifiers/calibration.

Until this is done, M1 is `OPEN GAP`.

## 6. Downstream work

Higher layers, local-law assembly and rank-2 analogues may be explored, but no argument may silently import the historical M1 conclusion. If a downstream route proves an independent estimate, that estimate must be stated and checked on its own assumptions.
