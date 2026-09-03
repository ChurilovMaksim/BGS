# Current results and exact scope

This is the short authoritative index of mathematical claims.
`../record/claim_ledger.md` is the repository-wide status authority.

## 1. Pair-key geometry — EXACT

For odd prime `p` and `x,y in F_p\{0,1}`, set `u=x/y`,
`v=(x-1)/(y-1)`, `d=x-y`. Off the diagonal the map is bijective onto
`u,v in F_p^*\{1}`, `u!=v`, with

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`,
`d=(u-1)(v-1)/(v-u)`.

The diagonal collapses to `(1,1,0)` with multiplicity `p-2`.

## 2. Fourth-moment pair-key distribution — EXACT + FINITE-CERTIFICATE

For `H <= F_p^*`, `|H|=K`,

`B(t)=O(t)+2(p-2) C_H(t)+(p-2)^2 1_{t=0}`

and

`|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K`.

The maintained C++ verifier independently checks the corrected finite geometry,
coupling totals and Fourier factorization anchors; Python and Lean supply
additional finite checks.

## 3. Fourier mean/variance identity — EXACT

Character orthogonality converts the fourth-moment character sum to the finite
Fourier transform of `B`. With `V=sum_t B(t)` and `Z=B(0)`,

`E_{q!=0} Sigma4(q)=(pZ-V)/(p-1)`

and

`Var_{q!=0} Sigma4(q)=p Var_{t!=0} B(t)`.

No probabilistic independence assumption is used.

## 4. Mixed term via Cayley transform — EXACT

For `c(h)=(h+1)/(h-1)` on `H\{1}`,

`d(u,v)=2/(c(u)-c(v))`,

so the mixed collision energy is a nonzero additive-difference energy of
`c(H\{1})`. Also `c(h^-1)=-c(h)`, producing the forced central-symmetry
baseline.

## 5. Matching audit and audited exceptional sets — FINITE-CERTIFICATE

The 720 integer matching systems have ranks `30` (rank 2), `240` (rank 3),
`450` (rank 4); the maximal-minor gcd audit permits an additional rank drop
only in characteristic 2.

Complete maintained cyclotomic resultant enumerations are promoted for exactly

`E_11={23,67,89}` and `E_13={53,79,131,157,313}`.

The repository now checks representative generic and exceptional finite
reductions independently in Python, C++ and Lean. This strengthens regression
coverage; it does **not** create a uniform-in-growing-`K` theorem.

## 6. Explicit non-uniformity witness — FINITE-CERTIFICATE

At `(p,K)=(461,23)` the exact mixed Cayley collision energy is `1190`, the
forced baseline is `902`, and the excess is `288`. Current Python, C++ and Lean
implementations all contain this anchor.

## 7. Off/off elliptic organization — DRAFT

The remaining off/off fluctuation can be organized by a non-isotrivial
genus-one/elliptic pencil. The target
`O(K^2 p + K^4 sqrt(p) + K^4)` and regime `K=o(p^(1/4))` remain theorem-draft
conclusions until the projective model, bad fibers, twists/isogenies, sheaf
irreducibility/complexity, affine boundary and exact correlation-theorem
hypotheses are closed.

## 8. Earlier finite foundations — SCOPED

- Lean finite level-set/orbit/freeness facts at `p=199, K=11`;
- Lean branch-scale identities at the same design;
- maintained finite twisted-Jacobi scalar and q-curve regressions;
- correct antiunitary eigenspace-preservation logic on its audited scope;
- historical shape/relation evidence retained only in Git history, while
  all-orders Catalan/arcsine claims remain unpromoted because the historical
  word-trace reduction had an unresolved rewrite case.

See `earlier_foundations.md`.

## 9. Numerical GOE comparisons — NUMERICAL ONLY

The spacing file reports a descriptive empirical CDF distance to the Wigner
surmise. The matched window-count file is not stationary number variance.
Neither carries inferential pass/fail semantics.

## 10. BGS local statistics — OPEN

Nothing above proves microscopic BGS/GOE eigenphase statistics. A
local-law/comparison mechanism for the structured arithmetic family remains a
separate open bridge.
