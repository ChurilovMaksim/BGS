# Frontier pass — 2026-09-04

## Objective

The unchanged long-range closure target is a rigorous Bohigas--Giannoni--Schmit universality theorem at microscopic spectral scale for a natural deterministic class of classically chaotic quantum systems, with symmetries explicitly desymmetrized and all limiting regimes stated.

This pass does **not** claim that target is closed.

## Repository authority

`record/claim_ledger.md` remains the repository-wide claim authority.  Historical commits and exploratory notes can contain stronger language and must not override it.  `record/retractions.md` remains binding for invalidated routes.

## Re-audited load-bearing chain

The following currently survives this pass:

1. the pair-key and fourth-moment reductions;
2. the Cayley additive-energy identity;
3. prime-order characteristic-zero collision rigidity;
4. the square resultant structure `Res(Phi_K,P)=K^3 M^2`;
5. the pointwise Stepanov/Vyugin--Makarychev bound
   `E_+(c(H\{1}))<34K^(8/3)` in its stated range;
6. the exact weighted split-prime excess budget;
7. the ordinary full-annihilator Jacobi trace identity and its exact second/fourth moments;
8. the double-averaged `theta<1/3` quadratic-excess theorem.

The primary PDF of the Vyugin--Makarychev source was re-read at the theorem statement because text extraction can lose the equality bar in the hypothesis `deg P(x,0)>=1`.  The maintained bilinear Cayley fiber has degree exactly one, so this source hypothesis is material and satisfied.

## New exact result from this pass

`mathematics/cayley_exact_baseline_density.md` proves:

> For fixed `0<theta<1/2`, if `B_theta(X)` is the subset of dyadic split designs
> `K~X^theta`, `p~X`, `p==1 mod K` with non-forced Cayley excess
> `Delta_K(p)>0`, then
>
> ```text
> |B_theta(X)| <<_theta X^(5theta)/(log X)^2,
> |B_theta(X)|/|D_theta(X)| <<_theta X^(5theta-1).
> ```
>
> Hence for every fixed `0<theta<1/5`, asymptotically almost every design has
> `Delta_K(p)=0` **exactly**, and therefore
>
> ```text
> E_+(c(H\{1}))=3(K-1)(K-2)
> ```
>
> exactly.

This is stronger than the previous density-one `o(K^2)` excess statement on the smaller exponent range.  The proof is a deterministic corollary of the weighted resultant budget plus integrality of `Delta_K(p)`, with Bombieri--Vinogradov/PNT used only to count the ambient dyadic designs.

No novelty claim beyond the repository is made here until an exact-statement literature search is completed.

## Independent algebra/computation checks in this pass

Small exact computations were used adversarially, not as proof:

- the maintained Lucas--Fibonacci rational-energy formula was spot-checked on several `N`;
- finite-field Cayley excess was recomputed for small split pairs, including nonzero-excess controls;
- non-forced collision symmetries were inspected to test whether every bad reduction necessarily carries a growing orbit multiplicity.

The last check supports only a negative design conclusion: the readily visible symmetries give at most constant-factor multiplicity and therefore do not by themselves improve the new `theta=1/5` exponent threshold.

## Literature status checked in this pass

Fresh searches were run for rigorous BGS results, quantum graphs, arithmetic cat maps, and Möbius/subgroup incidence estimates.

- A complete rigorous BGS-type theorem is known in special quantum-graph limits under classical mixing assumptions (Pluhař--Weidenmüller).
- Semiclassical field-theory/periodic-orbit arguments provide deep universality mechanisms but are not being promoted here to a general mathematical theorem for smooth deterministic chaotic Hamiltonians.
- Linear quantum cat maps carry arithmetic symmetries and exceptional spectral/eigenfunction phenomena, so a raw undecomposed cat map is not a safe generic BGS model.
- General incidence bounds for Möbius hyperbolae are geometrically relevant to the Cayley energy problem, but the transformations occurring here form a highly concentrated conjugated unipotent one-parameter family.  No verified black-box application was found that removes the current pointwise `K^(2/3)` loss.

A failed search is not a proof of novelty or impossibility.

## Current closure gaps

### G1 — pointwise centered Cayley energy

Target:

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

The current unconditional pointwise exponent is `8/3` in the stated Stepanov range.  Generic incidence machinery has not yet been verified to exploit the special subgroup/character structure strongly enough.

### G2 — off/off elliptic correlation

The maintained draft scale

```text
O(K^2 p+K^4 sqrt(p)+K^4)
```

still has unresolved elliptic/sheaf obligations.  This route must be checked source-by-source before promotion.

### G3 — local-statistics bridge

Moment identities for a full ordinary trace, even an exact Gaussian fourth-moment ratio, do not imply microscopic GOE/COE eigenphase statistics.  A genuine bridge needs control of an appropriate hierarchy (e.g. spectral form factor/correlation functions or a resolvent/point-process observable) in a symmetry-resolved ensemble/family.

### G4 — arithmetic desymmetrization/model choice

Any BGS theorem for cat-map-derived systems must state which arithmetic symmetries are removed, which family/perturbation is taken, and the order of semiclassical/family limits.  Otherwise arithmetic degeneracies can masquerade as failure of universality.

## Highest-information next attacks

1. **Resultant-budget compression.**  Seek algebraic dependence/shared factors among normalized orbit resultants.  Improving the total `K^(4+o(1))` logarithmic budget immediately improves both the `theta<1/3` average-excess and `theta<1/5` exact-baseline thresholds.
2. **Character-spectral attack on centered energy.**  Diagonalize the torus/unipotent correlation operator in multiplicative characters and seek cancellation after summing characters, rather than applying termwise square-root bounds.
3. **Elliptic pencil audit.**  Determine the precise bad-parameter locus, geometric monodromy, conductor bounds, and whether Deligne/Katz machinery actually supplies the desired off/off average.
4. **Local-statistics observable.**  Replace the full-trace fourth moment by a quantity whose convergence genuinely implies a point-process statement; identify the minimal all-orders or mesoscopic estimate needed.
5. **Exact-statement novelty search.**  Search the new density-one exact-baseline theorem under equivalent language (Möbius image of subgroup, Sidon-type energy, split reductions, cyclotomic resultants) before any external novelty claim.

## Non-claims

- BGS is not solved here.
- No Fields/Nobel-level claim is made.
- No finite computation is promoted to a universal theorem.
- No Lean theorem was claimed compiled in this pass.
- No general smooth-Anosov universality theorem was found in the searches performed, but absence from these searches is not a proof that no relevant result exists.
