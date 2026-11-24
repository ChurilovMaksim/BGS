# Coherent histories on a separated torsion grid

**Registry:** BGS-TRACE-357.

**Status:** supplementary analytic result from the 22 November packet,
for the unchanged [fixed family](../../fixed_map_resolvent_frontier.md).
See the [full proof](BGS_Histories.tex) and its
[finite checks](../../../../computations/verification/bgs_f_november/histories/check.py).
This result is about short history amplitudes and their centered
overlaps with powers, not the scalar Heisenberg trace law.

## Statement

Take odd `L>=3` with `L^2|N` and let `P_chi` be the rank-`N/L^2`
character projections of the exact `L^2`-element Weyl translation
group. Write `D=L^2`, `d_L=16+ceil(log(L)/log(5))`,
`tr_N=Tr/N` and `P_chi^t=U_N^t P_chi U_N^(-t)`.
Group the time grid of step `d_L` into `s` disjoint blocks of
`q` observations, with `(sq-1)d_L<=T_N` and
`T_N=floor(c log log log N)` for sufficiently small fixed `c>0`.
The nontrivial growing-grid statements use `d_L<=T_N`.

For a history `gamma=(chi_0,...,chi_(q-1))`, let
`C_gamma` be the product of the corresponding transported
projections, in increasing time order from left to right.
With `H=D^q` and `eps_N=exp(-(log N)^(3/4))`, the normalized
Hilbert–Schmidt products satisfy

```math
\operatorname{tr}_N\big((C_\delta^{[b]})^* C_\gamma^{[b]}\big)
  =H^{-1}\mathbf 1_{\delta=\gamma}+O(\epsilon_N),
\qquad
\operatorname{tr}_N\big((C_\delta^{[b']})^* C_\gamma^{[b]}\big)
  =H^{-2}+O(\epsilon_N)\quad(b'\ne b).
```

The constants are uniform over the admissible histories. For any
`Z` commuting with `U_N` and any single block,

```math
H\sum_\gamma\left|
 \operatorname{tr}_N(C_\gamma^*Z)
      -H^{-1}\operatorname{tr}_N Z \right|^2
\le \frac{1+O(sH^2\epsilon_N)}s\|Z\|_{2,N}^2.
```

In particular the estimate with `Z=U_N^(-m)`, after conjugation,
is uniform in `m`, with no restriction to short powers.
For fixed `L`, one can let both `q` and `s` grow sufficiently
slowly so that in any eigenbasis, the laws of these sequential
observations approach the uniform law in average total variation.
In particular convergence holds on a subset of density tending
to one. The version valid through **all** odd `N` uses products
of separated Weyl labels (no equal-rank character projections
unless `L^2|N`).

## Mechanism and proof dependencies

1. The lattice cocycle vanishes on the torsion subgroup
   when `L^2|N`. Exact expansion of the character projections
   reduces the Gram identities to traces of Weyl words at
   distinct times or with one increasing-then-decreasing
   palindrome. At a common peak, adjacent labels can be merged;
   discard an identically zero label and repeat. For the identity
   term the remaining labels must cancel in matching time pairs;
   character orthogonality then gives exactly the main terms.
2. For the nonidentity terms, the two unstable Fourier probes
   of the inverse linearizing conjugacy
   `H_lin^(-1)=id+k` lie at `B^T e_1, B^T e_2`;
   each has modulus above `10^(-4) tau` after applying the
   unstable covector. These estimates follow from Fourier
   coefficients of the physical kick and the stable/unstable
   geometric-series solution of the conjugacy equation,
   with a quantified remainder (source §9). At time `t`
   a nonzero torsion displacement has unstable oscillation
   at least `10^(-5) tau lambda^t/L` in linearized
   coordinates, where `lambda=3+2 sqrt(2)`. Any earlier
   time has upper bound `1000 tau lambda^t`.
   The spacing `d_L` makes the last nonzero label,
   when it is unique at its time, dominate every earlier
   label combined. The same argument using the stable probes
   at `e_1,e_2` works for reversed time. This is the input
   for the two-block product of positive history effects
   used in the eigenstate assertion.
3. The reduced canonical word is therefore not uniformly
   close to the identity, by a fixed multiple of `tau`.
   If the total observed time is `T`, it is analytic on
   a tube of width `r_0 K^(-4T)` for fixed `K>1`.
   Jensen counting of zeros, Blaschke factors and Harnack's
   bound on complex lines give a sublevel bound of the form
   `C_tau exp(C_tau K^(4T)) eps^exp(-C_tau K^(4T))`
   for displacements no larger than `eps`. To make this a
   trace bound, average conjugations by Fourier Weyl operators
   with indices of size at most `R=floor(N^(1/32))`. The
   normalized trace is unchanged; Egorov, Weyl composition
   and the normalized Hilbert–Schmidt norm replace the average
   by the `L^2` norm of two normalized Dirichlet factors of
   the displacement coordinates, up to power-decaying errors.
   Away from the sublevel set at `eps=R^(-1/2)`, one factor
   is small. The triple-log window makes the remaining
   sublevel bound at most `eps_N` after taking square roots.
4. Center and scale each history by
   `sqrt(H)(C_gamma-H^(-1)I)`. Their joint Gram matrix is
   block-diagonal up to norm `O(sH^2 eps_N)`; the main
   block is the identity minus the constant vector line.
   Commutation with `U_N` makes the inner products with
   `Z` equal over blocks. Bessel's inequality gives the
   factor `1/s`. For the positive history effects
   `C_gamma^* C_gamma`, the reversed-time argument gives
   separated-block product trace `H^(-2)+O(eps_N)`.
   Averaging the effects over the blocks and discarding
   off-diagonal entries in any eigenbasis gives a total
   variation bound controlled by
   `sqrt(H/s+O(H^2 eps_N))`. For fixed `L`, take
   `q` logarithmic in the number of available grid sites
   with a small coefficient, and take `s` of order the
   number of grid sites divided by `q`.

## Separation from the scalar pair problem

This goes beyond the one-step transfer question addressed by
[FM-023](../../../spectral-obstructions/arithmetic_translation_exclusion.md)
in a different direction. It is compatible with the
[18 November exact interference obstruction](../../torsion_interference_vertical_outliers_20261118.md):
that result concerns complete consecutive histories and
nonvanishing cross terms at exact arithmetic returns, whereas
the present estimates concern sparse separated blocks and
centered Hilbert–Schmidt products.

The all-power inequality leaves the common scalar
`tr_N(U_N^m)` undetermined. Its error accumulated in the
band of the original pair test is `O(N/s)`, not `o(1)`.
The packet includes exact comparison counterexamples:

- Cyclically shift `B` factors of `(C^D)^(tensor B)`.
  Short observations land on different tensor factors and
  satisfy the Gram identities **exactly**, but the unitary is
  scalar at multiples of `B` and the pair defect diverges.
- With `D=9` and `B` a power of three, modifying the phases
  along permutation cycles can assign the spectrum to a
  uniform clock of fixed multiplicity `b_0`. This preserves
  the coordinate observation histories and gives zero
  positive traces for `m<N/b_0`. Determinant-preserving
  independent algebraic angle perturbations of size
  `O(N^(-3))` make the spectrum simple and yield
  multiplicative independence modulo algebraic factors
  apart from the determinant relation, via
  Lindemann–Weierstrass. The local limit is still the
  shifted multiple clock and not Sine₂, even though the
  perturbed traces below `N/b_0` are now `O(N^(-1))`.

The abstract examples do **not** have the prescribed BGS
propagator and do not refute its local limit. Finite tests, some
at a larger test kick, check formulas and normalizations, not
the asymptotic statement at the frozen kick.
