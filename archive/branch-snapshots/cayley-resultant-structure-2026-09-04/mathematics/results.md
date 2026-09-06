# Current results and exact scope

This is the concise authoritative index of current mathematical claims.
[`../record/claim_ledger.md`](../record/claim_ledger.md) is the repository-wide status authority.

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

so the mixed collision energy is a nonzero additive-difference energy of `A=c(H \ {1})`. Also `c(h^-1)=-c(h)`, producing the forced central-symmetry baseline

`(K-1)(2K-5)`.

## 6. Prime-order characteristic-zero rigidity — EXACT

Let `K` be an odd prime. Chowla's rational linear independence theorem for

`cot(pi*a/K), 1 <= a <= (K-1)/2`,

combined with `c(exp(2*pi*i*j/K))=-i cot(pi*j/K)`, identifies the complex Cayley set with a rational cross-polytope. The only characteristic-zero equal-difference collisions are therefore

- identity `(r,s)=(i,j)`;
- central-inversion swap `(r,s)=(-j,-i)` modulo `K`.

No finite enumeration in `K` is needed for this statement.

## 7. Square structure of every collision resultant — EXACT + FINITE-REGRESSION

For the cleared collision polynomial `P_{i,j,r,s}` and prime cyclotomic polynomial `Phi_K`,

`(X-1)^3 | P(X)`.

Writing `P=(X-1)^3 Q` and `T=i+j+r+s`, one has

`Q(X^-1)=X^(3-T) Q(X)`.

After a root-of-unity twist, `Q(zeta_K)` lies in the maximal real subfield of `Q(zeta_K)`. Consequently

> `Res(Phi_K,P)=K^3 M^2` for some integer `M`.

For a non-forced finite-field collision at a prime `p` with `K | p-1`, one has `p!=K` and therefore `p | M`. Since `||P||_1<=12`,

`K^3 p^2 <= |Res(Phi_K,P)| <= 12^(K-1)`.

Hence

> if `K^3 p^2 > 12^(K-1)`, every collision is forced and the mixed energy is exactly `(K-1)(2K-5)`.

This improves the earlier worst-case cutoff by a square root. Exact normalized resultants through `K=11` independently regress the `K^3 * square` structure.

## 8. Fibonacci collision slice — EXACT

The explicit exponent relation

`c(h^2)-c(h)=c(h)-c(h^-1)`

is equivalent (away from the excluded `h=+-1`) to

`h^2+3h+1=0`.

For every odd prime `K`,

> `Res(Phi_K(X), X^2+3X+1)=F_K^2`.

Thus the full cleared collision resultant on this slice is

`K^3 F_K^2`.

Because `F_K` grows exponentially, there is **no** uniform polynomial bound `|M|<=K^C` for the square factor in Section 7. A polynomial-scale mixed-term theorem cannot be obtained by bounding the total resultant norm alone.

For a prime `p` with `K | p-1`, this slice has a non-forced finite-field collision iff `p | F_K`.

## 9. Fibonacci/Lucas almost-Sidon structure — EXACT + FINITE-CERTIFICATE

On the quadratic slice, `5 c(h)^2=1` and

`F_n c(h^n)=L_n c(h)`.

Over `Q`, define

`S_N={+-L_n/F_n : 1<=n<=N}`.

Using

`x_m+x_n=2F_(m+n)/(F_m F_n)`,

`|x_m-x_n|=2F_|m-n|/(F_m F_n)`,

and Carmichael's primitive-divisor theorem for Fibonacci numbers, all new relations beyond the bounded range are excluded. The exact bounded residue is kernel-checked in `formalization/Bgs/FibonacciRatioSmall.lean`. The result is

> for every `N>=3`, the nonzero difference energy of `S_N` is
> `2N(4N-3)+32`.

Thus the entire rational model exceeds its centrally symmetric forced baseline by only the constant `32`.

## 10. A 28-digit exact exceptional-prime witness — FINITE-CERTIFICATE

At

`K=131`,

`p=F_131=1066340417491710595814572169`,

an explicit complete Lucas primality certificate proves that `p` is prime, and

`h=188706367382658195937453923`

satisfies `h^2+3h+1=0 mod p` and has exact order `131`.

Independent Python arbitrary-precision and C++20 multiprecision audits give

`energy = 33442`,

`forced baseline = 33410`,

`excess = 32`,

`max nonzero difference multiplicity = 4`.

This shows that non-forced collisions can survive at very large split primes; nevertheless their total energy can remain extremely close to the forced minimum. The correct growing-`K` target is therefore a **uniform energy bound**, not a universal zero-excess theorem.

## 11. Matching audit and audited fixed-K exceptional sets — FINITE-CERTIFICATE

The 720 integer matching systems have ranks `30` (rank 2), `240` (rank 3), `450` (rank 4); the maximal-minor gcd audit permits an additional rank drop only in characteristic 2.

Complete maintained cyclotomic resultant enumerations are promoted for exactly

`E_11={23,67,89}`

and

`E_13={53,79,131,157,313}`.

These remain exact fixed-`K` refinements, not a substitute for a growing-`K` energy theorem.

## 12. Earlier below-cutoff witness — FINITE-CERTIFICATE

At `(p,K)=(461,23)` the exact mixed Cayley collision energy is `1190`, the forced baseline is `902`, and the excess is `288`.

## 13. Off/off elliptic organization — DRAFT

Historical symbolic calculations organize the remaining off/off fluctuation by a non-isotrivial genus-one/elliptic pencil and exhibit candidate bad fibers and same-`j` relations. These calculations are structural evidence, not a current theorem certificate.

The target

`O(K^2 p + K^4 sqrt(p) + K^4)`

and regime `K=o(p^(1/4))` remain theorem-draft conclusions until the projective model, bad fibers, twists/isogenies, sheaf irreducibility/complexity, affine boundary and the exact correlation-theorem hypotheses are all closed.

## 14. Earlier finite foundations — SCOPED

- Lean finite level-set/orbit/freeness facts at `p=199, K=11`;
- Lean branch-scale identities at the same design;
- maintained finite twisted-Jacobi scalar and q-curve regressions;
- correct antiunitary eigenspace-preservation logic on its audited scope;
- historical shape/relation evidence retained only in Git history, while all-orders Catalan/arcsine claims remain unpromoted because the historical word-trace reduction had an unresolved rewrite case.

See [`earlier_foundations.md`](earlier_foundations.md).

## 15. Numerical GOE comparisons — NUMERICAL ONLY

The maintained spectral code diagonalizes the full complex Hermitian matrix `M+M^*`. The spacing record reports only a descriptive empirical-CDF distance to the Wigner surmise. The matched window-count record is not stationary number variance. Neither carries inferential pass/fail semantics.

A reconstruction-era implementation briefly projected `M+M^*` to its entrywise real part before diagonalization; the numerical evidence was regenerated after that bug was found. No exact result depended on those floating-point records.

## 16. BGS local statistics — OPEN

Nothing above proves microscopic BGS/GOE eigenphase statistics for the arithmetic cat-map family. A local-law/comparison mechanism remains a separate open bridge. Rigorous BGS results do exist for special model classes such as mixing quantum graphs under their own hypotheses; they are not transferable to this family without a new argument.
