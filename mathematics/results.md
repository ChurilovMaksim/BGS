# Current results and exact scope

This file is the short authoritative index of mathematical claims. It is not a progress diary. A result appears here only if its status and hypotheses can be stated without relying on an obsolete proof route.

## 1. Pair-key geometry — EXACT

Let `p` be an odd prime. For `x,y` in `F_p \ {0,1}`, set

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

Off the diagonal `x != y`, the map `(x,y) -> (u,v)` is a bijection onto `u,v in F_p^* \ {1}` with `u != v`, and

`d(u,v)=(u-1)(v-1)/(v-u)`.

The diagonal `x=y` collapses to the single key `(1,1)`, difference zero, with multiplicity `p-2`. This is the load-bearing replacement for the retracted historical Möbius-fiber parametrization.

## 2. Fourth-moment pair-key distribution — EXACT + FINITE-CERTIFICATE

For a subgroup `H <= F_p^*` of order `K`, the corrected fourth-moment distribution `B(t)` has the exact decomposition

`B(t)=O(t)+2(p-2) C_H(t)+(p-2)^2 1_{t=0}`.

The two ordered mixed classes are separate; omitting either is the historical Run-93.2 factor-of-two error. The total size is

`|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K`.

Independent Python/C++ finite checks cover representative designs and direct small-`p` reconstruction from the original `(x,y)` pairs.

## 3. Fourier mean/variance identity — EXACT

Character orthogonality converts the fourth-moment character sum to the finite Fourier transform of `B`. Consequently the mean and variance over nonzero additive frequencies are determined exactly by `B(0)`, the total mass `sum_t B(t)`, and the centered `L^2` energy of `B(t)` on `t != 0`. No probabilistic independence assumption is used.

See `fourth_moment_reduction.md`.

## 4. Mixed term via Cayley transform — EXACT

For `c(h)=(h+1)/(h-1)` on `H \ {1}`,

`d(u,v)=2/(c(u)-c(v))`.

Thus

`sum_t C_H(t)^2 = E_+(c(H\{1}))-(K-1)^2`,

with the zero-difference diagonal removed. Since `c(h^-1)=-c(h)`, a central-symmetry collision baseline is forced.

## 5. Fixed-K collision classification — EXACT FINITE ALGEBRA

For **odd prime `K`**, the 720 multiset matchings arising from a Cayley difference collision have characteristic-zero ranks

- 30 of rank 2;
- 240 of rank 3;
- 450 of rank 4.

The only prime at which these integer matrices can suffer an additional rank drop is 2. The rank-2/3 kernels are exhausted by invalid zero/diagonal configurations together with the identity and inversion-swap symmetries.

For fixed `K`, every non-forced collision therefore comes from reduction of a nonzero cyclotomic algebraic integer. The active exact producer recomputes the corresponding resultants in CI. In particular,

`E_11={23,67,89}` and `E_13={53,79,131,157,313}`.

These are **fixed-`K`** exceptional-prime sets. They are not evidence for a uniform-in-`K` theorem.

Producer: `computations/verification/mixed_cayley_energy.py`.

## 6. Explicit non-uniformity witness — FINITE-CERTIFICATE

At `(p,K)=(461,23)` the exact mixed Cayley collision energy is `1190`, whereas the forced central-symmetry baseline is `902`. The excess `288` is an explicit warning that the fixed-`K` statement cannot be silently upgraded to a uniform theorem.

## 7. Off/off elliptic organization — DRAFT

After the exact pair-key repair, the remaining off/off fluctuation can be organized by a non-isotrivial genus-one/elliptic pencil. Historical calculations identify a rational `j`-map, bad fibers, same-`j` symmetries and a prospective sheaf-correlation route.

The restricted estimate `O(K^2 p + K^4 sqrt(p) + K^4)` and regime `K=o(p^(1/4))` remain **theorem-draft targets**, not promoted theorems. Missing work includes a publication-grade projective model, complete exceptional-parameter analysis, twist/isogeny classification, and verification of the exact sheaf-theorem hypotheses.

See `elliptic_pencil.md`.

## 8. Earlier finite foundations — FINITE-CERTIFICATE / SCOPED HISTORICAL

The reconstruction retained useful earlier results rather than deleting them:

- at `p=199`, Lean verifies finite level-set counts for `Q(a,b)=a^2-ab-b^2`, order `K=11`, orbit counts and freeness of the cyclic action;
- at the same design, Lean verifies the recorded branch-scale identities `c^2=5 mod 199`;
- finite twisted-Jacobi implementation identities and moment curves are preserved with explicit parameter ranges;
- the antiunitary calculation explains why an eigenvalue sector is preserved under the relevant anti-linear symmetry, but the old global GOE-class conclusion is not promoted beyond the audited chart without a fresh proof.

See `earlier_foundations.md`.

## 9. Numerical GOE comparison — NUMERICAL ONLY

The repository retains finite spacing and matched-GOE window-count diagnostics. Their descriptive distances are useful, but the old `KS pass` and `two-sigma pass` language has been removed: the unfolded gaps/window counts do not satisfy the IID assumptions of those textbook tests.

No numerical file is evidence for a limiting local law.

## 10. BGS local statistics — OPEN

Nothing above proves microscopic BGS/GOE eigenphase statistics for the arithmetic cat-map family. A local-law/comparison mechanism for the structured arithmetic matrix family remains a separate open bridge.
