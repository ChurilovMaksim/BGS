# Current results and exact scope

This is the short authoritative index of mathematical claims. Historical files may contain stronger language; `record/claim_ledger.md` is the repository-wide status authority.

## 1. Pair-key geometry — EXACT

For odd prime `p` and `x,y in F_p\{0,1}`, set `u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`. Off the diagonal the map is bijective onto `u,v in F_p^*\{1}`, `u!=v`, with

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`, `d=(u-1)(v-1)/(v-u)`.

The diagonal collapses to `(1,1,0)` with multiplicity `p-2`.

## 2. Fourth-moment pair-key distribution — EXACT + FINITE-CERTIFICATE

For `H <= F_p^*`, `|H|=K`, the corrected distribution satisfies

`B(t)=O(t)+2(p-2) C_H(t)+(p-2)^2 1_{t=0}`

and

`|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K`.

The active C++ verifier independently checks the geometry, coupling totals, twist collapse at feasible sizes, and the fourth-moment Fourier factorization on the promoted designs.

## 3. Fourier mean/variance identity — EXACT

Character orthogonality converts the fourth-moment character sum to the finite Fourier transform of `B`. The nonzero-frequency mean and centered second moment are therefore finite Fourier identities; no probabilistic independence assumption is used.

## 4. Mixed term via Cayley transform — EXACT

For `c(h)=(h+1)/(h-1)` on `H\{1}`,

`d(u,v)=2/(c(u)-c(v))`,

so `sum_t C_H(t)^2 = E_+(c(H\{1}))-(K-1)^2`. Also `c(h^-1)=-c(h)`, producing the forced central-symmetry baseline.

## 5. Integer matching audit and audited cyclotomic exceptional sets — FINITE-CERTIFICATE

The 720 integer matching systems have ranks `30` (rank 2), `240` (rank 3), `450` (rank 4); their maximal-minor gcds permit an additional rank drop only in characteristic 2. The low-rank kernels are classified into forbidden zero/diagonal, identity, and inversion-swap types.

For a specified odd prime `K`, the cyclotomic reduction mechanism yields a finite exceptional set once the normalized non-forced collision polynomials are known to be nonzero in `Q(zeta_K)`. The active repository carries the complete resultant enumeration for exactly the audited values

`E_11={23,67,89}` and `E_13={53,79,131,157,313}`.

The general fixed-`K` mechanism is useful structure, but no explicit exceptional set for arbitrary growing `K` is promoted without running/proving the corresponding nonvanishing and resultant analysis.

## 6. Explicit non-uniformity witness — FINITE-CERTIFICATE

At `(p,K)=(461,23)` the exact mixed Cayley collision energy is `1190`; the forced baseline is `902`, so the excess is `288`. This blocks a naive uniform-in-`K` extrapolation from `K=11,13`.

## 7. Off/off elliptic organization — DRAFT

The remaining off/off fluctuation can be organized by a non-isotrivial genus-one/elliptic pencil. The target `O(K^2 p + K^4 sqrt(p) + K^4)` and regime `K=o(p^(1/4))` remain theorem-draft conclusions until the projective model, bad fibers, twists/isogenies, sheaf irreducibility/complexity, affine boundary, and exact correlation-theorem hypotheses are closed.

## 8. Earlier finite foundations — SCOPED

- Lean finite level-set/orbit/freeness facts at `p=199, K=11`;
- Lean branch-scale identities at the same design;
- finite twisted-Jacobi scalar and moment regressions at recorded designs;
- correct antiunitary eigenspace-preservation logic on the audited chart;
- finite shape/relation data retained for regression, while all-orders Catalan/arcsine claims remain unpromoted because the historical word-trace reduction has an unresolved rewrite case.

See `earlier_foundations.md`.

## 9. Numerical GOE comparisons — NUMERICAL ONLY

The spacing file reports descriptive empirical CDF distance to the Wigner surmise; the historical IID-KS pass label was removed. The matched window-count file is not standard stationary number variance and carries no two-sigma pass label.

## 10. BGS local statistics — OPEN

Nothing above proves microscopic BGS/GOE eigenphase statistics. A local-law/comparison mechanism for the structured arithmetic family remains a separate open bridge.
