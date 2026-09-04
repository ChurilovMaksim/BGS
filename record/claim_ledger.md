# Claim ledger

This is the repository-wide status authority. Historical commits can contain
stronger language; this file wins.

## Status vocabulary

- **EXACT** — current algebraic identity/derivation with stated hypotheses.
- **EXACT + EXTERNAL-THEOREM** — exact project derivation whose remaining named input is a verified published theorem with its hypotheses checked in project notation.
- **FINITE-CERTIFICATE** — exact exhaustive or kernel-checked statement at explicit finite parameters.
- **FINITE-REGRESSION** — finite implementation/reference agreement; useful for reproducibility but not a symbolic theorem.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — promising proof route with named unresolved obligations.
- **OPEN** — closure condition not yet achieved.
- **SCOPED-HISTORICAL** — useful earlier result whose safe present scope is narrower than its old label.
- **NOT-PROMOTED** — retained as evidence/conjectural structure but not accepted into the current theorem set.
- **RETRACTED** — false or superseded.

## Active exact chain

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection and diagonal multiplicity `p-2` | **EXACT** | `mathematics/fourth_moment_reduction.md`; Python/C++/Lean finite checks |
| constrained off-diagonal pair count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | immediate from pair-key bijection; `PairKeySecondMoment.lean` checks `(53,13)` |
| finite `k=2` pair-key parametrization at `(53,13)` | **FINITE-CERTIFICATE** | `formalization/Bgs/PairKeySecondMoment.lean` |
| finite `k=4` key multiplicities / `V4` count at `(53,13)` | **FINITE-CERTIFICATE** | `formalization/Bgs/PairKeyFourthMoment.lean` |
| `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | current derivation + independent C++/Python checks |
| character/Fourier fourth-moment collapse and nonzero-frequency mean/variance | **EXACT + FINITE-REGRESSION** | `mathematics/fourth_moment_reduction.md`, C++/Python |
| Cayley identity and additive-energy reduction | **EXACT** | `mathematics/cayley_additive_energy.md` |
| prime-order characteristic-zero Cayley collision classification | **EXACT** | Chowla cotangent independence + elementary cross-polytope lemma in `mathematics/cayley_additive_energy.md` |
| prime-order collision resultant has shape `Res(Phi_K,P)=K^3 M^2` | **EXACT + FINITE-REGRESSION** | real-subfield norm argument in `mathematics/cayley_resultant_structure.md`; exhaustive normalized checks through `K=11` |
| if odd prime `K | p-1` and `K^3 p^2 > 12^(K-1)`, mixed energy is exactly `(K-1)(2K-5)` | **EXACT + FINITE-REGRESSION** | square-resultant theorem + coefficient norm |
| Fibonacci collision slice `Res(Phi_K,X^2+3X+1)=F_K^2` and full collision norm `K^3 F_K^2` | **EXACT + FINITE-REGRESSION** | Binet/Lucas derivation + exact resultant checks through `K=29` |
| rational set `S_N={+-L_n/F_n:1<=n<=N}` has nonzero difference energy `2N(4N-3)+32` for `N>=3` | **EXACT + FINITE-CERTIFICATE** | full proof in `mathematics/fibonacci_ratio_energy_proof.md`, using Yabuta Theorem 3 for the unbounded primitive-divisor step; Python + `FibonacciRatioSmall.lean` close only the bounded residue |
| `(K,p)=(131,F_131)` is a 28-digit prime Fibonacci-slice witness with energy `33442`, baseline `33410`, excess `32` | **FINITE-CERTIFICATE** | complete Lucas primality certificate + independent Python/C++ arbitrary-precision Cayley audits |
| for any odd prime `p` and subgroup `H<=F_p^*` of order `100<K<p^(3/4)/3`, `E_+(c(H\{1}))<34 K^(8/3)` and `sum_t C_H(t)^2<34K^(8/3)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | bilinear fibers + source-exact Vyugin--Makarychev Theorem 2 in `mathematics/cayley_direct_energy.md`; independent C++ finite verifier |
| corresponding mixed centered variance bound `<136 p K^(8/3)` in the repository normalization | **EXACT** | direct energy theorem propagated through the exact mixed coefficient `2(p-2)` |
| centered-energy identity `E_+(A)=|A|^4/p + p^(-1) sum_{q!=0}|1_Ahat(q)|^4` and exact Cayley Fourier/character Gram matrix | **EXACT** | `mathematics/cayley_centered_energy.md` |
| for odd prime `K`, weighted split-prime excess budget `sum_{p==1 mod K} Delta_K(p) log p <= (K^3-5K^2+6K+1)((K-1)log12-3logK)` | **EXACT + FINITE-REGRESSION** | Galois scaling orbits + `p`-adic common-root count + `K^3 M^2` resultant structure in `mathematics/cayley_resultant_mass_budget.md`; exact K=11,13 regression |
| one canonical nonzero-difference polynomial `S_K` classifies all additive split-prime exceptions: `Delta_K(p)>0 iff p|Disc(S_K)` and `Delta_K(p)<=4 v_p(Disc(S_K))` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_difference_discriminant.md`; exact regression for `K=5,7,11,13` |
| ratio-orbit factorization `S_K=prod_[r] F_r`, exact cross-resultant squares, and `|Disc(F_r)|=2^((K-1)^2)K^(K-2)I_r^4` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_ratio_orbit_factorization.md`; symbolic/resultant regression through `K=47` |
| global fourth-power discriminant identity `|Disc(S_K)|=2^((K-1)^4/4) K^((K-1)(K^2-7)/4) J_K^4` | **EXACT + FINITE-REGRESSION** | ratio-orbit theorem and product-discriminant identity; split valuations are multiples of four |
| characteristic-zero multiplicative Cayley rigidity: all product collisions are swap/simultaneous inversion and `E_x(A_K)=4(K-1)(K-2)` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_multiplicative_rigidity.md` |
| one canonical product polynomial classifies all multiplicative split-prime exceptions: `Delta_K^x(p)>0 iff p|Disc(S_K^x)` and `Delta_K^x(p)<=16v_p(Disc(S_K^x))` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_product_discriminant.md`; exact regression `K=5,7,11,13` |
| full-annihilator ordinary trace identity `1_Ahat(r)=K Tr M_S(2r)` and exact trace second/fourth moments | **EXACT + FINITE-REGRESSION** | direct diagonal calculation in `mathematics/cayley_jacobi_trace_average.md`; independent Cayley-Fourier/Jacobi regression |
| for fixed `0<theta<1/3`, dyadic split pairs `K~X^theta`, `p~X` satisfy average `Delta_K(p)/K^2 <<_theta X^(3theta-1)` and therefore almost-all quadratic excess in pair-density | **EXACT + EXTERNAL-THEOREM** | global resultant mass budget + classical Bombieri--Vinogradov + PNT in `mathematics/cayley_jacobi_trace_average.md` |
| full normalized Jacobi trace nonzero-frequency kurtosis has double-average absolute deviation from `3` tending to zero for fixed `0<theta<1/3` | **EXACT** | exact trace moments + previous double-average theorem; this is only a second/fourth moment-ratio statement, not a CLT |
| generic off/off family has one exact reducible spike `O_lambda(2/(alpha-beta))=2p-8`, four additional `I_1` fibers, and singular support recovering the parameter up to `(h1,h2)<->(h2^-1,h1^-1)` | **EXACT + FINITE-REGRESSION** | `mathematics/offoff_elliptic_spike_theorem.md`; symbolic regression and exact anchors `(53,13)`, `(199,11)` |
| corrected off/off variance `Var_{t!=0}O(t) << pE_+(c(H\{1}))+K^2p+K^4 sqrt(p)+K^4` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | spike extraction + Igusa geometric monodromy + Grothendieck--Lefschetz/Deligne quasi-orthogonality; source/hypotheses recorded in `offoff_elliptic_spike_theorem.md` |
| in `100<K<p^(3/4)/3`, off/off variance `<<pK^(8/3)+K^4sqrt(p)+K^2p+K^4`; hence `<<pK^(8/3)` for `K=o(p^(1/4))` | **EXACT + EXTERNAL-THEOREM** | corrected off/off theorem + maintained direct Cayley-energy theorem |
| sharp pointwise centered Cayley target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` (equivalently nonzero Fourier fourth moment `<<pK^(2+o(1))`) | **OPEN** | exact Fourier/character, torus--unipotent, shifted-product, discriminant, multiplicative-rigidity and double-average reductions isolate the gap; no verified pointwise theorem closes the `K^(2/3)` loss |
| 720 matching rank classification; only characteristic-2 extra rank drop | **FINITE-CERTIFICATE** | `computations/verification/mixed_cayley_energy.py` |
| `E_11={23,67,89}` | **FINITE-CERTIFICATE** | complete exact resultants recomputed in CI |
| `E_13={53,79,131,157,313}` | **FINITE-CERTIFICATE** | complete exact resultants recomputed in CI |
| generic/exceptional finite Cayley-energy controls | **FINITE-CERTIFICATE** | independent C++/Python plus `formalization/Bgs/CayleyEnergy.lean` |
| `(p,K)=(461,23)` energy `1190` vs baseline `902` | **FINITE-CERTIFICATE** negative control | C++/Python/Lean |
| microscopic BGS/GOE local eigenphase law | **OPEN** | no current proof; moment closure would still require a separate local-statistics/comparison mechanism |

## Current architecture of the fourth-moment obstruction

The exact pair-key reduction gives

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

The mixed layer and the corrected off/off layer are now controlled by the
**same** pointwise arithmetic quantity

```text
E_+(A),   A=c(H\{1}).
```

For the mixed layer this is exact by the Cayley reduction.  For the off/off
layer the reason is structural: every generic elliptic class has a reducible
fiber at

```text
t_lambda=2/(c(h1)-c(h2)),
```

with exactly `2p-8` valid points.  Equal Cayley differences therefore align
`O(p)` spikes, and their aggregate second moment is bounded by `p E_+(A)`.
After this spike is extracted, the residual elliptic trace sheaves are
quasi-orthogonal at square-root scale.  Hence the former elliptic/sheaf draft
is no longer an independent pointwise obstruction.

The strongest current uniform pointwise bound remains

```text
E_+(A)<34K^(8/3)
```

under `100<K<p^(3/4)/3`.  Consequently in the BGS moment regime
`K=o(p^(1/4))`, both the mixed and off/off contributions are controlled on the
`pK^(8/3)` scale.  The remaining exponent loss is exactly `K^(2/3)` relative
to the natural quadratic collision scale.

The sharp closure target is therefore

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

This target can also be written

```text
E_+((H-1)^(-1))=(K-1)^4/p+O(K^(2+o(1)))
```

because `c(h)=1+2/(h-1)`.  Known near-quadratic multiplicative energy for the
shifted subgroup `H-1` is highly relevant, but no verified reciprocal/cross-
ratio transfer theorem currently turns it into the required additive energy.

## Discriminant structure and what it does not buy

The theorem `Res(Phi_K,P)=K^3M^2` and the canonical difference discriminant
compress exceptional reductions very efficiently.  The ratio-orbit theorem
further proves

```text
|Disc(S_K)|
 =2^((K-1)^4/4)
  K^((K-1)(K^2-7)/4)
  J_K^4.
```

This explains the systematic fourth-power split valuations and reduces all
split additive exceptions to prime divisors of `J_K`.

However, exact computations through `K=47` falsify the early small-`K`
heuristic that the prime-to-`2K` residual discriminant should have only
`O(K^3 log K)` logarithmic size.  Cross-resultants between distinct ratio
orbits retain genuine `K^4`-scale archimedean mass.  Therefore the fourth-power
factorization is a structural theorem, **not** a proof of a `theta<1/4`
pointwise cutoff.  Any future improvement must exploit arithmetic sparsity or
cancellation among eligible split prime divisors, not merely total resultant
height.

The multiplicative Cayley theorem is an independent exact rigidity statement.
It does not imply additive rigidity after finite-field reduction, and the
article does not use such an implication.

## Double-average results

For odd prime `K`, the global resultant mass theorem gives

```text
sum_{p==1 mod K} Delta_K(p) log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

The ordinary-trace identity

```text
1_Ahat(r)=K Tr M_S(2r)
```

is a direct diagonal identity and uses no cyclic manipulation of
noncommutative matrix words; the historical R86/R87 shortcut remains
retracted.

Combining the global `O(K^4)` split-prime budget with Bombieri--Vinogradov
after averaging over prime subgroup orders gives: for fixed
`0<theta<1/3`, prime `K in (X^theta/2,X^theta]` and split prime
`p in (X/2,X]`, the average normalized excess is

```text
O_theta(X^(3theta-1)).
```

Hence the proportion of such split pairs with `Delta_K(p)>=eta K^2` tends to
zero for every fixed `eta>0`.  In the BGS-relevant subrange `theta<1/4` this
lies inside `K=o(p^(1/4))`; the theorem actually extends as a double average
to `theta<1/3`.  This does **not** upgrade the pointwise centered-energy claim.

Via the exact trace moments, the same double average forces the ordinary
full-trace second/fourth moment ratio to the real-Gaussian value `3`.  This is
not a Gaussian distribution theorem, not a parity/desymmetrized block theorem,
and not a local eigenvalue statistic.

## Earlier useful foundations

| Claim | Status | Scope |
|---|---|---|
| torus level-set cardinalities/orbit counts/freeness | **FINITE-CERTIFICATE** | `p=199,K=11`, Lean |
| recorded branch scale `c^2=5 mod 199` | **FINITE-CERTIFICATE** | `p=199`, Lean |
| twisted-Jacobi scalar formula / q-curve moments | **FINITE-REGRESSION** | explicit designs; maintained producer `twisted_jacobi_regression.py` |
| antiunitary eigenspace-preservation logic | **SCOPED-HISTORICAL** | no blanket global GOE-class promotion |
| relation/shape finite counts | **SCOPED-HISTORICAL** | no current theorem dependency; provenance in Git history |
| all-orders Catalan / full-group arcsine package | **NOT-PROMOTED** | unresolved historical word-trace rewrite |
| higher-rank/Sp(2g) exploratory diagnostics | **NOT-PROMOTED** | useful historical tests, but no current general theorem re-certified |

## Numerical records

`evidence/numerical/goe_spacing.json` is a descriptive empirical CDF-distance
record produced from the **full complex Hermitian** sector matrix.  Its
historical IID-KS pass/fail interpretation is withdrawn.

`evidence/numerical/matched_window_count_variance.json` is a descriptive
matched-GOE forward-window statistic.  It is not stationary `Sigma^2(L)` and
is not an inferential pass/fail test.

A reconstruction-era implementation accidentally replaced `M+M^*` by its
entrywise real part before diagonalization.  The numerical records were
regenerated after this was detected; no exact claim depended on those records.

## Retractions and superseded routes

See [`retractions.md`](retractions.md) for mechanisms.  In particular, the
historical Möbius/M4D M1 proof, one-sided mixed counting, ESY-to-BGS shortcut,
noncommutative trace shortcut, Hecke-centering Julia line, `cdense_transfer`,
`sol6`, unsupported Sp(2g) extrapolations, the temporary real-projection
spectral bug, and all-orders promotion from the unresolved word-trace route are
not active results.

Two additional 2026-09-04 corrections are load-bearing:

1. the unconditional historical off/off target
   `O(K^2p+K^4sqrt(p)+K^4)` is **RETRACTED/SUPERSEDED** because it omitted the
   reducible `2p-8` spike.  The corrected theorem is (43) above;
2. the small-`K` heuristic `log|J_K|_(2K)'=O(K^3 log K)` is **RETRACTED** as a
   scaling conjecture after exact larger-`K` cross-resultant tests.  No theorem
   depends on it.

Microscopic BGS/GOE universality remains open even if the full fourth-moment
programme is completed.