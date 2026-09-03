# Off/off elliptic pencil: current theorem draft

**Status: DRAFT.** This file records the strongest route that survived the pair-key repair. It deliberately separates algebra already checked from steps that still require publication-grade proof.

## 1. Where the pencil enters

The corrected fourth-moment distribution is

`B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}`.

The mixed term is controlled for fixed `K` by `cayley_additive_energy.md`. The unresolved contribution is the centered energy of the off/off term `O(t)`.

After the pair-key and subgroup substitutions, the relevant fibers can be organized as a one-parameter family of genus-one curves. Historical symbolic work produced an explicit quartic/Weierstrass model, a rational `j`-map, reducible exceptional fibers and same-`j` parameter symmetries. Those calculations are useful structure, but they are not by themselves a correlation theorem.

## 2. Structural information that survived audit

The surviving calculations support the following scoped facts:

1. the generic fiber has genus one after the recorded birational reduction;
2. the computed `j`-invariant is nonconstant, so the candidate family is non-isotrivial on the generic locus;
3. finitely many explicitly visible parameter values produce degenerate or reducible fibers;
4. the computed `j`-map has nontrivial same-`j` symmetries that must be quotiented or treated as exceptional correlation strata;
5. the affine model deletes boundary points, so projective trace estimates require an explicit boundary correction rather than a silent application of a projective theorem.

The detailed pre-consolidation calculation remains recoverable from Git history. No claim here treats a historical CAS transcript as a proof.

## 3. Intended correlation step

The target is a square-root correlation estimate for trace functions of the family, schematically

`sum_t a_lambda(t) conjugate(a_mu(t)) = O(sqrt(p))`

outside a controlled exceptional relation between `lambda` and `mu`.

A legitimate proof needs more than non-isotriviality. At minimum it must establish, for the actual sheaves used in the finite-field family:

- a smooth projective model on an explicitly stated open base;
- the complete discriminant/bad-fiber locus, including characteristic exceptions;
- purity and lissity on that base;
- geometric irreducibility of the relevant `R^1` sheaf;
- a uniform conductor/ramification bound;
- classification of geometric isomorphisms up to the twists actually present;
- exclusion or explicit accounting of separable and inseparable isogenies;
- treatment of the deleted affine boundary;
- the exact hypotheses of the chosen correlation theorem.

Function-field Tate/isogeny results of Zarhin and quantitative sheaf technology of Sawin/Forey/Fresán/Kowalski are relevant tools, not automatic black boxes. The repository does not currently claim their hypotheses have all been verified for this pencil.

## 4. Target estimate, not yet theorem

If the correlation step above is established with the required uniformity, the existing combinatorics lead to the restricted target

`O(K^2 p + K^4 sqrt(p) + K^4)`.

The error is then lower order relative to the natural main scale in the regime `K=o(p^(1/4))`.

Until the geometric/sheaf obligations are closed, both this estimate and the `p^(1/4)` regime remain conditional theorem-draft conclusions.

## 5. What would still remain

Even a completed off/off estimate would be a moment/fluctuation theorem. A microscopic BGS/GOE local eigenphase law requires a separate local-law or comparison mechanism for the structured arithmetic matrix family. The repository treats that bridge as a different open problem rather than smuggling it into the elliptic argument.
