# Fixed-map conversation import audit — 25 September 2026

## Scope

Compared the available 24 September fixed-map continuation against the clean
repository revision `f6eb912` before editing. The audit focused on concrete
identities and proofs, not on attempts to solve the terminal BGS problem.

## Results already maintained

The conversation's seven-cut reduction, all-minor/simple-spectrum theorem,
common-antireversor certificate, exact nonvanishing/scalar-return result, and
effective gap floor are already represented by `BGS-FM-007` through
`BGS-FM-011` and their linked reviews. Their boundaries were preserved; no
duplicate theorem or stronger status was added.

## Results integrated

| Result | Repository disposition | Exact boundary |
|---|---|---|
| Pair Abel sum as an adjoint-Laplacian resolvent | Added as `BGS-RES-006` in `mathematics/fixed_map_resolvent_frontier.md`. The Poisson-kernel identity is exact, and replacing the hyperbolic argument by $s$ has error at most $2\cosh(2s/N)/(3N)$. | Any $N\times N$ unitary. Equivalence of the pair and scalar-resolvent limits; no model-specific convergence. |
| Universal clock floor | Added as `BGS-TRACE-007`, with the exact Cohn--Kumar dependency in `literature/external_dependencies.json`. | $L_N(s)\ge(e^{2s}-1)^{-1}$, attained by a regular $N$-gon. The CUE target lies strictly above the floor; no uniform model-specific gap is proved. |
| Depolarizing regularization | Added to the noise section of the maintained frontier: $L_{\eta,N}(s)=L_N(s+N\eta/2)+\rho_N$, with $0\le\rho_N\le(2Ns)^{-1}$. | Exact for every unitary and $\eta\ge0$. The parameter shift leaves the fixed-$s$ trace problem unresolved. |
| Eigenphase motion | Added with proof in `mathematics/frozen_spectral_flow_controls.md`. | Local on intervals of simple spectrum; no uniform estimate near collisions and no global labeling claim. |
| Powers of the kicked map | Corrected to the ordered product of conjugated kicks. The suggested collapse to one exponential is retracted for odd $7\nmid N$, already at $m=2$, including the maintained algebraic coupling. | Uses `BGS-FM-008` and `EXT-POPESCU-2023`; the argument leaves dimensions divisible by 7 above 7 unclassified. |
| Legendre-character control | Added with a self-contained construction $e^{itA}D=e^{itB}De^{-itB}$. Its spectrum is always a clock although the generator has zero diagonal and flat off-diagonal magnitudes. | A separate prime-dimensional toy family, not the maintained BGS propagator; its Abel sum is $(e^{2s}-1)^{-1}$, not the CUE value. |

## Not promoted

The compressed `c_53` huge-dimension estimate came without its exact
recurrence, trace lower-bound derivation, or a reproducible definition and
calculation of the cited pair test. The quoted commutator-limit constant came
without the complete Fourier support, orbit coefficients, summation domain,
or proof. These snippets do not support mathematical promotion; no
asymptotic theorem is inferred from them.

## Current frontier

The pair Abel target remains open for the prescribed frozen family. The
exact resolvent representation and universal lower floor do not estimate
`Tr(U_N^m)` at $m\asymp N$, and the isospectral control is not a counterexample
for that family. `BGS-TRACE-005` and `BGS-BGS-001` remain open.
