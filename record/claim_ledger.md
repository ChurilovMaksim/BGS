# Claim ledger

This file is the repository-wide status authority.  Historical commits, old
manuscript text and exploratory notes may contain stronger claims; this file
wins.

## Status vocabulary

- **EXACT** — current project derivation with explicit hypotheses.
- **EXACT + EXTERNAL-THEOREM** — the project reduction is exact and the only
  remaining named input is a verified published theorem whose hypotheses have
  been checked in project notation.
- **FINITE-CERTIFICATE** — exhaustive or kernel-checked statement at explicit
  finite parameters.
- **FINITE-REGRESSION** — exact finite implementation/reference agreement; not
  a proof of a universal theorem.
- **NUMERICAL** — descriptive floating-point evidence only.
- **OPEN** — the stated closure condition has not been achieved.
- **SCOPED-HISTORICAL** — useful earlier result retained at a narrower audited
  scope.
- **NOT-PROMOTED** — exploratory structure retained without theorem status.
- **RETRACTED / SUPERSEDED** — false, overclaimed, or replaced by a corrected
  statement.

## Active theorem chain

| Claim | Status | Current support |
|---|---|---|
| pair-key bijection; diagonal multiplicity `p-2` | **EXACT** | `mathematics/fourth_moment_reduction.md` |
| constrained off-diagonal count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | pair-key proof; Lean finite anchor |
| `|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | fourth-moment reduction; Python/C++/Lean |
| character/Jacobi fourth-moment collapse and nonzero-frequency Fourier mean/variance | **EXACT + FINITE-REGRESSION** | `mathematics/fourth_moment_reduction.md` |
| Cayley identity and reduction of the mixed layer to additive energy of `A=c(H\{1})` | **EXACT** | `mathematics/cayley_additive_energy.md` |
| prime-order characteristic-zero additive collision classification | **EXACT** | Chowla cotangent independence + cross-polytope lemma |
| `Res(Phi_K,P)=K^3M^2` for every cleared prime-order collision polynomial | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_resultant_structure.md` |
| no non-forced finite collision if `K^3p^2>12^(K-1)` | **EXACT** | square-resultant theorem + coefficient norm |
| Fibonacci slice `Res(Phi_K,X^2+3X+1)=F_K^2` | **EXACT + FINITE-REGRESSION** | exact Binet/Lucas derivation |
| `S_N={+-L_n/F_n}` has nonzero difference energy `2N(4N-3)+32` for `N>=3` | **EXACT + FINITE-CERTIFICATE** | Yabuta primitive-divisor input + bounded Lean residue |
| `(K,p)=(131,F_131)` 28-digit witness has excess `32` | **FINITE-CERTIFICATE** | Lucas primality certificate + independent Python/C++ audits |
| for `100<K<p^(3/4)/3`, `E_+(A)<34K^(8/3)` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | source-exact Vyugin--Makarychev theorem in `cayley_direct_energy.md` |
| corresponding mixed centered variance `<136pK^(8/3)` | **EXACT** | exact mixed coefficient + direct energy theorem |
| centered identity `E_+(A)=|A|^4/p+p^(-1)sum_{q!=0}|1_Ahat(q)|^4` | **EXACT** | `mathematics/cayley_centered_energy.md` |
| global weighted split-prime budget `sum Delta_K(p)log p <=(K^3-5K^2+6K+1)((K-1)log12-3logK)` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_resultant_mass_budget.md` |
| canonical additive polynomial `S_K`: `Delta_K(p)>0 iff p|Disc(S_K)` and `Delta_K(p)<=4v_p(Disc(S_K))` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_difference_discriminant.md` |
| ratio-orbit factorization, exact cross-resultant squares and one-factor fourth-power discriminants | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_ratio_orbit_factorization.md` |
| global identity `|Disc(S_K)|=2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4` | **EXACT + FINITE-REGRESSION** | ratio-orbit discriminant theorem |
| characteristic-zero multiplicative rigidity and `E_x(A_K)=4(K-1)(K-2)` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_multiplicative_rigidity.md` |
| canonical product polynomial: `Delta_K^x(p)>0 iff p|Disc(S_K^x)` and `Delta_K^x(p)<=16v_p(Disc(S_K^x))` | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_product_discriminant.md` |
| full-annihilator trace identity `1_Ahat(r)=K Tr M_S(2r)` and exact trace moments | **EXACT + FINITE-REGRESSION** | `mathematics/cayley_jacobi_trace_average.md` |
| fixed `0<theta<1/3`: dyadic split-pair average `Delta_K(p)/K^2 <<_theta X^(3theta-1)` | **EXACT + EXTERNAL-THEOREM** | global budget + Bombieri--Vinogradov + PNT |
| fixed `0<theta<1/3`: full-trace fourth/second moment ratio tends to `3` in double-average absolute deviation | **EXACT** | exact trace moments + previous theorem |
| fixed `0<theta<1/2`: bad split designs satisfy `#bad/#all <<_theta X^(5theta-1)` | **EXACT + EXTERNAL-THEOREM** | `mathematics/cayley_exact_baseline_density.md` |
| fixed `0<theta<1/5`: density-one split pairs have `Delta_K(p)=0` exactly and `E_+(A)=3(K-1)(K-2)` | **EXACT + EXTERNAL-THEOREM** | integer excess + global budget + Bombieri--Vinogradov/PNT denominator |
| generic off/off class has exact reducible spike `O_lambda(2/(alpha-beta))=2p-8`, four additional simple finite bad fibers, and parameter recovery up to `(h1,h2)<->(h2^-1,h1^-1)` | **EXACT + FINITE-REGRESSION** | `mathematics/offoff_elliptic_spike_theorem.md` |
| corrected off/off variance `Var_{t!=0}O(t)<<pE_+(A)+K^2p+K^4sqrt(p)+K^4` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | spike extraction + Igusa monodromy + Grothendieck--Lefschetz/Deligne |
| in `100<K<p^(3/4)/3`, corrected off/off variance `<<pK^(8/3)+K^4sqrt(p)+K^2p+K^4`; hence `<<pK^(8/3)` for `K=o(p^(1/4))` | **EXACT + EXTERNAL-THEOREM** | corrected off/off + direct Cayley theorem |
| sharp pointwise target `E_+(A)=(K-1)^4/p+O(K^(2+o(1)))` | **OPEN** | all current formulations isolate the same `K^(2/3)` loss |
| microscopic BGS/GOE local eigenphase law | **OPEN** | no current mean-spacing local-law/comparison mechanism |

## Current obstruction architecture

The exact fourth-moment decomposition is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

Both nontrivial fluctuation layers are now controlled by the same pointwise
quantity

```text
E_+(A),  A=c(H\{1}).
```

For the mixed layer this is the direct Cayley reduction.  For the off/off layer
the mechanism is the exact reducible fiber

```text
t_lambda=2/(c(h1)-c(h2)),
O_lambda(t_lambda)=2p-8.
```

Parameter classes with equal Cayley difference align their `O(p)` spikes, so
their aggregate second moment is controlled by `pE_+(A)`.  After extracting
the spike, the residual rank-two elliptic trace sheaves are uniformly
quasi-orthogonal at square-root scale.  Thus the old elliptic/sheaf gap is no
longer independent.

The strongest current uniform pointwise theorem is

```text
E_+(A)<34K^(8/3)
```

for `100<K<p^(3/4)/3`.  The remaining closure target is

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_{q!=0}|1_Ahat(q)|^4 << pK^(2+o(1)).
```

Because `c(h)=1+2/(h-1)`, the same target may be written for the reciprocal
shifted subgroup `(H-1)^(-1)`.  Known near-quadratic multiplicative energy of
shifted subgroups is relevant, but no verified reciprocal/cross-ratio transfer
theorem currently supplies the required additive bound.

## Discriminant structure: what is proved and what is not

The additive difference discriminant compresses every split-prime exception
into one integer.  The stronger ratio-orbit theorem gives

```text
|Disc(S_K)|
 =2^((K-1)^4/4)
  K^((K-1)(K^2-7)/4)
  J_K^4.
```

This proves fourth-power split valuations.  However exact cross-resultant
computations through `K=47` reject the earlier small-`K` scaling guess that the
prime-to-`2K` residual logarithmic mass should be `O(K^3log K)`: the total
archimedean cross-resultant mass remains genuinely `K^4`-scale.  Therefore the
fourth-power factorization is structural, not a hidden pointwise quadratic
energy theorem.

The multiplicative Cayley theorem is an independent exact rigidity result.  It
does not imply additive rigidity after finite-field reduction and is not used
as if it did.

## Double-average and density-one results

The global budget plus Bombieri--Vinogradov/PNT gives two distinct theorems.

First, for fixed `theta<1/3`,

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1) -> 0.
```

Second, using only that `Delta_K(p)` is a nonnegative integer, for fixed
`theta<1/2`,

```text
#bad/#all <<_theta X^(5theta-1).
```

Hence for `theta<1/5`, asymptotically almost every dyadic split pair has no
non-forced collision at all and

```text
E_+(A)=3(K-1)(K-2)
```

exactly.  These are averaged arithmetic theorems; neither is a pointwise
statement for every split reduction.

The full Jacobi trace identity transfers the additive-energy moments to an
ordinary matrix trace.  The double-average standardized fourth-moment ratio
tends to `3`, but this is neither a central limit theorem nor a local
eigenphase-statistics result.

## Promoted finite certificates / regressions

- finite pair-key and fourth-moment anchors, including `(53,13)`;
- complete additive exceptional sets `E_11={23,67,89}` and
  `E_13={53,79,131,157,313}`;
- negative control `(p,K)=(461,23)` with energy `1190` versus forced nonzero
  baseline `902`;
- the 28-digit Fibonacci witness with exact excess `32`;
- additive/product discriminant regressions;
- ratio-orbit/fourth-power regression through `K=47` for the recorded scaling
  study, with smaller default CI cases;
- exact symbolic and finite anchors for the corrected elliptic `2p-8` spike.

Finite regressions are never promoted to proofs of universal claims.

## Earlier useful foundations

| Claim | Status | Scope |
|---|---|---|
| torus level-set cardinalities/orbit counts/freeness | **FINITE-CERTIFICATE** | `p=199,K=11`, Lean |
| recorded branch scale `c^2=5 mod 199` | **FINITE-CERTIFICATE** | `p=199`, Lean |
| twisted-Jacobi scalar formula / q-curve moments | **FINITE-REGRESSION** | explicit designs |
| antiunitary eigenspace-preservation logic | **SCOPED-HISTORICAL** | no blanket global GOE-class promotion |
| historical relation/shape finite counts | **SCOPED-HISTORICAL** | no current theorem dependency |
| all-orders Catalan / full-group arcsine package | **NOT-PROMOTED** | unresolved historical word-trace rewrite |
| higher-rank/Sp(2g) exploratory diagnostics | **NOT-PROMOTED** | no current general theorem re-certified |

## Numerical records

`evidence/numerical/goe_spacing.json` and
`evidence/numerical/matched_window_count_variance.json` are descriptive
full-complex-Hermitian diagnostics only.  Historical IID-KS/pass-fail language
is withdrawn.  A reconstruction-era accidental real projection was corrected;
no exact theorem depended on those records.

## Retractions and superseded routes

See [`retractions.md`](retractions.md) for mechanisms.  In particular, the
historical Möbius/M4D proof, one-sided mixed counting, ESY-to-BGS shortcut,
noncommutative trace shortcut, Hecke-centering Julia route, unsupported
higher-rank extrapolations and all-orders promotion from the unresolved
word-trace route are not active.

Two current-era corrections are load-bearing:

1. the old unconditional off/off target
   `O(K^2p+K^4sqrt(p)+K^4)` is **RETRACTED / SUPERSEDED** because it omitted
   the exact reducible `2p-8` spike; the corrected theorem contains
   `pE_+(A)`;
2. the small-`K` heuristic that the prime-to-`2K` residual discriminant should
   have only `O(K^3log K)` logarithmic size is **RETRACTED** after larger exact
   ratio-orbit computations.

Microscopic BGS/GOE universality remains open even if the fourth-moment
programme is completed.
