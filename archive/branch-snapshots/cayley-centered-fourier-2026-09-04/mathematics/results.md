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

so the mixed collision energy is a nonzero additive-difference energy of

`A=c(H \ {1})`.

Also `c(h^-1)=-c(h)`, producing the forced central-symmetry baseline

`(K-1)(2K-5)`.

## 6. Prime-order characteristic-zero rigidity — EXACT

Let `K` be an odd prime. Chowla's rational linear independence theorem for

`cot(pi*a/K), 1 <= a <= (K-1)/2`,

combined with `c(exp(2*pi*i*j/K))=-i cot(pi*j/K)`, identifies the complex Cayley set with a rational cross-polytope. The only characteristic-zero equal-difference collisions are

- identity `(r,s)=(i,j)`;
- central-inversion swap `(r,s)=(-j,-i)` modulo `K`.

No finite enumeration in `K` is needed for this statement.

## 7. Square structure of collision resultants — EXACT + FINITE-REGRESSION

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

This is useful worst-case structure, but not the main polynomial-scale mechanism.

## 8. Fibonacci obstruction to norm-only arguments — EXACT

The collision

`c(h^2)-c(h)=c(h)-c(h^-1)`

is equivalent, away from `h=+-1`, to

`h^2+3h+1=0`.

For every odd prime `K`,

> `Res(Phi_K(X),X^2+3X+1)=F_K^2`.

Thus the full cleared collision norm on this slice is `K^3 F_K^2`. Since `F_K` grows exponentially, no uniform polynomial bound on the total resultant square factor can produce the desired mixed theorem.

## 9. Fibonacci/Lucas almost-Sidon structure — EXACT + FINITE-CERTIFICATE

On the quadratic slice,

`5 c(h)^2=1`,

`F_n c(h^n)=L_n c(h)`.

Over `Q`, define

`S_N={+-L_n/F_n : 1<=n<=N}`.

Carmichael/Yabuta primitive-divisor separation plus an exact finite residue gives

> for every `N>=3`, the nonzero difference energy of `S_N` is
> `2N(4N-3)+32`.

The residual range through index `12` is independently kernel-checked in Lean. The excess over the centrally symmetric forced baseline is exactly `32`, independent of `N`.

## 10. A 28-digit exact exceptional-prime witness — FINITE-CERTIFICATE

At

`K=131`,

`p=F_131=1066340417491710595814572169`,

an explicit Lucas certificate proves that `p` is prime, and

`h=188706367382658195937453923`

has exact order `131` and satisfies `h^2+3h+1=0 mod p`.

Independent Python arbitrary-precision and C++20 multiprecision audits give

`energy = 33442`,

`forced baseline = 33410`,

`excess = 32`,

`max nonzero difference multiplicity = 4`.

This demonstrates that very large exceptional split primes are compatible with nearly minimal total energy.

## 11. Direct polynomial-scale Cayley energy — EXACT + FINITE-REGRESSION

No primality assumption on `K` is needed here. Let `p` be odd, `H<=F_p^*` have order `K`, and `A=c(H\{1})`.

For

`r(t)=#{(a,b) in A^2:a+b=t}`,

the equation `c(x)+c(y)=t` is exactly

`P_t(x,y)=(2-t)xy+t(x+y)-(2+t)=0`.

Every fiber is absolutely irreducible in odd characteristic because the bilinear determinant is `-4`.

Vyugin--Makarychev Theorem 2, with its source hypotheses checked against the primary arXiv PDF, gives for

`100<K<p^(3/4)/3`

and `t notin {0,-2}`

`r(t)<=32 K^(2/3)`.

The exceptional fibers satisfy `r(0)=K-1` and `r(-2)<=K-1`. Hence

> `E_+(A)<34 K^(8/3)`.

Equivalently

> `sum_t C_H(t)^2 < 34 K^(8/3)`.

After the exact coefficient `2(p-2)` in the fourth-moment decomposition is propagated through the repository variance normalization,

> `Var_{t!=0}(2(p-2)C_H(t)) < 136 p K^(8/3)`.

This is the first uniform pointwise polynomial-scale mixed theorem in the project.

See [`cayley_direct_energy.md`](cayley_direct_energy.md).

## 12. Correct centered-energy target and exact Fourier structure — EXACT / OPEN

For any `A subset F_p`, with unnormalized additive Fourier transform,

`E_+(A)=|A|^4/p + 1/p sum_{q!=0}|1_Ahat(q)|^4`.

Thus a global raw statement `E_+(A)=O(K^2)` is not the correct target: the density term is unavoidable.

For the Cayley image the sharp pointwise target is

> `E_+(A)=(K-1)^4/p + O(K^(2+o(1)))`,

or equivalently

> `sum_{q!=0}|1_Ahat(q)|^4 << p K^(2+o(1))`.

This remains **OPEN**.

The exact character decomposition and Gram matrix are recorded in
[`cayley_centered_energy.md`](cayley_centered_energy.md), together with the equivalent one-parameter unipotent PGL2 and shifted-product formulations.

## 13. Shifted-product relation and its exact obstruction — EXACT

For `t!=2`, put `lambda=t/(2-t)`. The sum fiber factorizes so that on `P_t=0`,

`(x+lambda)(y+lambda)=(1+lambda)^2`.

Thus each Cayley fiber is one distinguished product class in `H+lambda`.

Moreover,

`sum_lambda E_x(H+lambda)=K^4-E_+(H)+p(2K^2-K)`.

Known near-quadratic total multiplicative-energy bounds for shifted subgroups do not by themselves control the square-sum of the moving distinguished class.

## 14. Global split-prime collision-mass budget — EXACT + FINITE-REGRESSION

For odd prime subgroup order `K`, define

`Delta_K(p)=sum_{d!=0}r_{A-A}(d)^2-(K-1)(2K-5)`

for split primes `p==1 mod K`.

Simultaneous exponent scaling partitions all non-forced collision quadruples into

`N_K=K^3-5K^2+6K+1`

free Galois orbits. A normalized orbit contributes at most the corresponding split-prime valuation of its resultant. Using

`Res(Phi_K,P_q)=K^3 M_q^2`

and the coefficient norm gives

> `sum_{p==1 mod K} Delta_K(p) log p`
> `<= (K^3-5K^2+6K+1)((K-1)log12-3logK)`.

Thus the total non-forced collision mass over all split primes has a deterministic `O(K^4)` logarithmic budget, with explicit tail/sparsity corollaries.

See [`cayley_resultant_mass_budget.md`](cayley_resultant_mass_budget.md).

## 15. Cayley Fourier transform is the full twisted-Jacobi trace — EXACT + FINITE-REGRESSION

Let `S=H^perp`, `m=(p-1)/K`, and let `J_S(q)` be the full annihilator twisted-Jacobi matrix in the maintained convention. Define

`M_S(q)=e_p(-q/2) J_S(q)/(p-1)`.

Then for every `r in F_p`,

> `1_Ahat(r)=K Tr M_S(2r)`.

This is an ordinary diagonal trace identity. It uses no cyclic manipulation of noncommutative matrix words and is unrelated to the retracted historical R86/R87 trace shortcut.

Consequently

`sum_q |Tr M_S(q)|^2 = p(K-1)/K^2`,

`sum_q |Tr M_S(q)|^4 = p E_+(A)/K^4`,

and `Tr M_S(0)=(K-1)/K`.

An independent finite regression compares the maintained Jacobi matrix directly with Cayley Fourier values at `(53,13)`, `(199,11)` and sampled `(461,23)`.

See [`cayley_jacobi_trace_average.md`](cayley_jacobi_trace_average.md).

## 16. Double-averaged quadratic mixed excess — EXACT

Fix `0<theta<1/3`, set `Q=X^theta`, and define

`D_theta(X)={(K,p): K,p prime, Q/2<K<=Q, X/2<p<=X, p==1 mod K}`.

Bombieri--Vinogradov, the prime number theorem and partial summation give

`|D_theta(X)| ~ [log(2)/(2 theta)] X/(log X)^2`.

Combining this denominator with the exact global resultant mass budget gives

> `1/|D_theta(X)| sum_(K,p in D_theta(X)) Delta_K(p)/K^2`
> `<<_theta X^(3theta-1) -> 0`.

Hence for every fixed `eta>0`, the proportion of pairs with

`Delta_K(p)>=eta K^2`

tends to zero. Equivalently, asymptotically almost every dyadic split design has

`sum_t C_H(t)^2=(K-1)(2K-5)+o(K^2)`

in pair-density.

The theorem holds throughout `theta<1/3`; in the BGS-moment subrange `theta<1/4`, it lies uniformly inside `K=o(p^(1/4))`. This is a **double-average/almost-all statement**, not a pointwise centered-energy theorem.

## 17. Double-averaged full-trace fourth-moment ratio — EXACT

Let `mu_2,mu_4` be the nonzero-frequency second and fourth moments of `Tr M_S(q)`, and set

`kappa(K,p)=mu_4/mu_2^2`.

The trace is real because `A=-A`. From the exact trace moments,

`|kappa(K,p)-3| << Delta_K(p)/K^2 + 1/K + K^2/p`.

Therefore over `D_theta(X)`, for every fixed `0<theta<1/3`,

> `1/|D_theta(X)| sum |kappa(K,p)-3|`
> `<<_theta X^(3theta-1)+X^(-theta)+X^(2theta-1) -> 0`.

Thus the **ordinary full normalized Jacobi trace** has the real-Gaussian second/fourth moment ratio in this double average.

This is not a CLT, not a parity/desymmetrized-block statement, and not a local eigenvalue-statistics theorem.

## 18. Matching audit and fixed-K exceptional sets — FINITE-CERTIFICATE

The 720 integer matching systems have ranks `30` (rank 2), `240` (rank 3), `450` (rank 4); the maximal-minor gcd audit permits an additional rank drop only in characteristic 2.

Complete maintained cyclotomic resultant enumerations are promoted for exactly

`E_11={23,67,89}`

and

`E_13={53,79,131,157,313}`.

At `(p,K)=(461,23)` the exact mixed Cayley collision energy is `1190`, the forced baseline is `902`, and the excess is `288`.

## 19. Off/off elliptic organization — DRAFT

Historical symbolic calculations organize the remaining off/off fluctuation by a non-isotrivial genus-one/elliptic pencil and exhibit candidate bad fibers and same-`j` relations. These calculations are structural evidence, not a current theorem certificate.

The target

`O(K^2 p + K^4 sqrt(p) + K^4)`

and regime `K=o(p^(1/4))` remain theorem-draft conclusions until the projective model, bad fibers, twists/isogenies, sheaf irreducibility/complexity, affine boundary and exact correlation-theorem hypotheses are all closed.

## 20. Earlier finite foundations — SCOPED

- Lean finite level-set/orbit/freeness facts at `p=199, K=11`;
- Lean branch-scale identities at the same design;
- maintained finite twisted-Jacobi scalar and q-curve regressions;
- correct antiunitary eigenspace-preservation logic on its audited scope;
- historical shape/relation evidence retained only in Git history, while all-orders Catalan/arcsine claims remain unpromoted because the historical word-trace reduction had an unresolved rewrite case.

See [`earlier_foundations.md`](earlier_foundations.md).

## 21. Numerical GOE comparisons — NUMERICAL ONLY

The maintained spectral code diagonalizes the full complex Hermitian matrix `M+M^*`. The spacing record reports only a descriptive empirical-CDF distance to the Wigner surmise. The matched window-count record is not stationary number variance. Neither carries inferential pass/fail semantics.

A reconstruction-era implementation briefly projected `M+M^*` to its entrywise real part before diagonalization; the numerical evidence was regenerated after that bug was found. No exact result depended on those floating-point records.

## 22. BGS local statistics — OPEN

Nothing above proves microscopic BGS/GOE eigenphase statistics for the arithmetic cat-map family. A local-law/comparison mechanism remains a separate open bridge. Rigorous BGS results do exist for special model classes such as mixing quantum graphs under their own hypotheses; they are not transferable to this family without a new argument.
