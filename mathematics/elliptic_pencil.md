# Off/off elliptic family: exact structure and proof obligations

The pure off/off contribution `O(t)` can be organized, after Cayley coordinates, by a bounded-degree family of plane cubics. On the generic smooth locus the fibers are elliptic curves.

Current symbolic work supports a nonconstant generic `j`-invariant, a degree-12 generic `j`-map, a bounded discriminant/boundary divisor, an involutive same-`j` symmetry, and reducible fibers at Cayley-difference parameters already visible in the mixed term.

These computations are structural evidence, not yet an unconditional variance theorem.

## Obligation A: algebraic certificate

Before promotion, the project needs a publication-grade derivation or machine-readable certificate for:

1. projective/Weierstrass models on every chart;
2. discriminant and `j` map, including cancellations and characteristic exclusions;
3. the complete bad-parameter set;
4. the exact same-`j` correspondence;
5. no-isogeny/non-isomorphism for distinct generic parameters, including quadratic twists and inseparable exceptional cases after reduction;
6. reduction of every exceptional fiber to the already-controlled mixed term or to an explicitly bounded finite remainder.

A characteristic-zero modular-curve argument is only part of this obligation; it must be connected carefully to reduction modulo `N`.

## Obligation B: uniform trace-sheaf correlation

For the rank-2 lisse sheaves attached to the family, the chosen quasi-orthogonality theorem must be applied with its actual hypotheses checked:

1. purity and normalization;
2. geometric irreducibility and monodromy;
3. uniform conductor/complexity;
4. geometric non-isomorphism for every off-diagonal parameter pair being summed;
5. treatment of duals, constant twists and relevant rank-one twists;
6. deleted/bad points and boundary contribution;
7. a constant uniform in `N` and in the allowed parameter range.

Modern joint-family work on elliptic curves supports this architecture but also shows why these hypotheses cannot be replaced by the phrase “standard sheaf theory.”

## Conditional consequence

If A and B hold with uniform constants, the centered generic fiber traces have diagonal contribution `O(N)` and off-diagonal correlation `O(sqrt(N))`. Summing over `O(K^2)` parameters gives schematically

`Var_{t!=0} O(t) << K^2 N + K^4 sqrt(N) + K^4`.

Together with the mixed Cayley bound, this yields

`Var_{t!=0} B(t)=O(K^2 N)`

in the preliminary regime `K=o(N^(1/4))`, outside the relevant fixed-`K` exceptional reductions, and therefore

`std_{q!=0} Sigma4(q)=O(NK)`.

This is a **conditional restricted M1 statement**, not a theorem in the current repository.

Even after it is closed, a separate argument is required to pass from fourth-moment concentration to microscopic GOE/GUE eigenphase statistics.
