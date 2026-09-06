# Current results and exact scope

This is the concise authoritative index of current mathematical claims.
[`../record/claim_ledger.md`](../record/claim_ledger.md) is the
repository-wide status authority.

## 1. Pair-key geometry — EXACT

For odd prime `p` and `x,y in F_p \ {0,1}`, set

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

Off the diagonal the map is bijective onto
`u,v in F_p^* \ {1}`, `u != v`, with

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`,
`d=(u-1)(v-1)/(v-u)`.

The diagonal collapses to `(1,1,0)` with multiplicity `p-2`.

## 2. Constrained pair count — EXACT

For `H <= F_p^*`, `|H|=K`, the off-diagonal subgroup constraints become exactly

`u,v in H \ {1}`, `u != v`.

Hence the number of admissible ordered constrained pairs is `(K-1)(K-2)`.

The Lean module `PairKeySecondMoment.lean` independently certifies the finite design `(p,K)=(53,13)`; the general count follows directly from the bijection.

## 3. Fourth-moment pair-key distribution — EXACT + FINITE-CERTIFICATE

For the corrected weighted key table,

`B(t)=O(t)+2(p-2) C_H(t)+(p-2)^2 1_{t=0}`

and

`|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K`.

The maintained C++ verifier independently checks the corrected finite geometry, coupling totals and Fourier-factorization anchors; Python and Lean supply separate finite checks.

## 4. Character/Fourier collapse — EXACT

Let `S=H^perp` and `m=|S|=(p-1)/K`. In the maintained convention,

`sum_{chi,psi in S}|J(chi,psi;q)|^4 = m^2 Sigma4(q)`,

`Sigma4(q)=sum_t B(t)e_p(qt)`.

With `V=sum_t B(t)` and `Z=B(0)`,

`E_{q!=0} Sigma4(q)=(pZ-V)/(p-1)`

and

`Var_{q!=0} Sigma4(q)=p Var_{t!=0} B(t)`.

These are finite identities; no probabilistic independence assumption is used.

## 5. Mixed term via Cayley transform — EXACT

For `c(h)=(h+1)/(h-1)` on `H \ {1}`,

`d(u,v)=2/(c(u)-c(v))`,

so the mixed collision energy is a nonzero additive-difference energy of `A=c(H \ {1})`. Also `c(h^-1)=-c(h)`, producing the forced central-symmetry baseline.

## 6. Uniform prime-order Cayley cutoff — EXACT + FINITE-REGRESSION

Let `K` be an odd prime and `K | p-1`. Chowla's rational linear independence theorem for

`cot(pi*a/K), 1 <= a <= (K-1)/2`,

combined with `c(exp(2*pi*i*j/K))=-i cot(pi*j/K)`, implies that the only characteristic-zero equal-difference collisions in the Cayley set are the identity and the central-inversion swap.

Clearing denominators gives a ten-term polynomial `P` with coefficient `L1` norm at most `12`. For every non-forced quadruple `P` is nonzero at a primitive `K`-th root of unity, so

`0 < |Res(Phi_K,P)| <= 12^(K-1)`.

A non-forced collision modulo `p` forces `p` to divide this resultant. Therefore

> if `p > 12^(K-1)`, every collision is forced and
> `sum_t C_H(t)^2 = (K-1)(2K-5)` exactly.

This is a genuine uniform growing-`K` theorem, but it only gives a logarithmic regime `K=O(log p)`. It does not yet reach the polynomial regime relevant to the off/off draft.

`computations/verification/cayley_uniform_cutoff_regression.py` independently checks the cleared polynomial identity, coefficient norm, exhaustive non-forced resultants for `K=3,5,7`, and representative finite fields above the cutoff. Those finite checks are regression evidence, not the source of the universal proof.

## 7. Matching audit and audited exceptional sets — FINITE-CERTIFICATE

The 720 integer matching systems have ranks `30` (rank 2), `240` (rank 3), `450` (rank 4); the maximal-minor gcd audit permits an additional rank drop only in characteristic 2.

Complete maintained cyclotomic resultant enumerations are promoted for exactly

`E_11={23,67,89}`

and

`E_13={53,79,131,157,313}`.

The repository checks representative generic and exceptional finite reductions independently in Python, C++ and Lean. This remains a computer-assisted exact fixed-`K` refinement below the uniform cutoff, not a replacement for the theorem in Section 6.

## 8. Explicit below-cutoff witness — FINITE-CERTIFICATE

At `(p,K)=(461,23)` the exact mixed Cayley collision energy is `1190`, the forced baseline is `902`, and the excess is `288`. This does not contradict Section 6 because `461 < 12^22`.

## 9. Off/off elliptic organization — DRAFT

Historical symbolic calculations organize the remaining off/off fluctuation by a non-isotrivial genus-one/elliptic pencil and exhibit candidate bad fibers and same-`j` relations. These calculations are structural evidence, not a current theorem certificate.

The target

`O(K^2 p + K^4 sqrt(p) + K^4)`

and regime `K=o(p^(1/4))` remain theorem-draft conclusions until the projective model, bad fibers, twists/isogenies, sheaf irreducibility/complexity, affine boundary and the exact correlation-theorem hypotheses are all closed.

## 10. Earlier finite foundations — SCOPED

- Lean finite level-set/orbit/freeness facts at `p=199, K=11`;
- Lean branch-scale identities at the same design;
- maintained finite twisted-Jacobi scalar and q-curve regressions;
- correct antiunitary eigenspace-preservation logic on its audited scope;
- historical shape/relation evidence retained only in Git history, while all-orders Catalan/arcsine claims remain unpromoted because the historical word-trace reduction had an unresolved rewrite case.

See [`earlier_foundations.md`](earlier_foundations.md).

## 11. Numerical GOE comparisons — NUMERICAL ONLY

The maintained spectral code diagonalizes the full complex Hermitian matrix `M+M^*`. The spacing record reports only a descriptive empirical-CDF distance to the Wigner surmise. The matched window-count record is not stationary number variance. Neither carries inferential pass/fail semantics.

A reconstruction-era implementation briefly projected `M+M^*` to its entrywise real part before diagonalization; the numerical evidence was regenerated after that bug was found. No exact result depended on those floating-point records.

## 12. BGS local statistics — OPEN

Nothing above proves microscopic BGS/GOE eigenphase statistics for the arithmetic cat-map family. A local-law/comparison mechanism remains a separate open bridge. Rigorous BGS results do exist for special model classes such as mixing quantum graphs under their own hypotheses; they are not transferable to this family without a new argument.