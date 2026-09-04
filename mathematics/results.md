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

Now no primality assumption on `K` is needed. Let `p` be odd, `H<=F_p^*` have order `K`, and

`A=c(H\{1})`.

For

`r(t)=#{(a,b) in A^2:a+b=t}`,

the equation `c(x)+c(y)=t` is exactly

`P_t(x,y)=(2-t)xy+t(x+y)-(2+t)=0`.

Every fiber is absolutely irreducible in odd characteristic because for a bilinear polynomial `axy+bx+cy+d` the determinant criterion gives

`ad-bc=-4`.

Vyugin--Makarychev Theorem 2, with its source hypotheses checked against the primary arXiv PDF, therefore gives for

`100<K<p^(3/4)/3`

and `t notin {0,-2}`

`r(t)<=32 K^(2/3)`.

The exceptional fibers satisfy `r(0)=K-1` and `r(-2)<=K-1`. Hence

> `E_+(A)<34 K^(8/3)`.

Equivalently for the mixed collision distribution,

> `sum_t C_H(t)^2 < 34 K^(8/3)`.

After the exact coefficient `2(p-2)` in the fourth-moment decomposition is propagated through the repository variance normalization,

> `Var_{t!=0}(2(p-2)C_H(t)) < 136 p K^(8/3)`.

This is the first uniform polynomial-scale mixed theorem in the project. It applies to every subgroup reduction in the stated range, including cyclotomic/Fibonacci exceptional primes, and does not use a resultant cutoff.

See [`cayley_direct_energy.md`](cayley_direct_energy.md).

## 12. Correct centered-energy target and exact Fourier structure — EXACT / OPEN

For any `A subset F_p`, with unnormalized additive Fourier transform,

`E_+(A)=|A|^4/p + 1/p sum_{q!=0}|1_Ahat(q)|^4`.

Thus a global raw statement `E_+(A)=O(K^2)` is not the correct target: the density term `|A|^4/p` is unavoidable.

For the Cayley image the sharp target is

> `E_+(A)=(K-1)^4/p + O(K^(2+o(1)))`,

or equivalently

> `sum_{q!=0}|1_Ahat(q)|^4 << p K^(2+o(1))`.

This remains **OPEN**.

Let `S=H^perp`, `m=(p-1)/K`. With `y=(h-1)^(-1)`, one has `h=(y+1)/y`, `c(h)=1+2y`, and exactly

`1_Ahat(q)=e_p(q)/m * sum_{chi in S} T_chi(q)`,

`T_chi(q)=sum_{y!=0,-1} chi((y+1)/y)e_p(2qy)`.

The character family has exact Gram matrix

`sum_q T_chi(q) conjugate(T_eta(q)) = p(p-2)` if `chi=eta`, and `-p` otherwise.

This recovers `sum_q|1_Ahat(q)|^2=p(K-1)`, but the desired theorem is an `L^4` statement and needs genuinely joint character-family cancellation.

The same problem has an exact PGL2 form:

`r_{A-A}(t)=#{h in H\{1}:u_t(h) in H\{1}}`,

`u_t(h)=((2-t)h+t)/(2+t-th)`,

where `{u_t}` is a one-parameter unipotent subgroup conjugate to additive translations by the Cayley transform.

See [`cayley_centered_energy.md`](cayley_centered_energy.md).

## 13. Shifted-product relation and its exact obstruction — EXACT

For `t!=2`, put `lambda=t/(2-t)`. The sum fiber factorizes as

`((2-t)x+t)((2-t)y+t)=(2-t)P_t(x,y)+4`,

so on `P_t=0`,

`(x+lambda)(y+lambda)=(1+lambda)^2`.

Thus each Cayley fiber is one distinguished product class in the shifted subgroup `H+lambda`.

Moreover, if `E_x(H+lambda)` is multiplicative energy, then

`sum_lambda E_x(H+lambda)=K^4-E_+(H)+p(2K^2-K)`.

Known near-quadratic total multiplicative-energy bounds for shifted subgroups are relevant but do not, by themselves, control the square-sum of the moving distinguished class. This is the precise obstruction to that natural shortcut.

## 14. Global split-prime collision-mass budget — EXACT + FINITE-REGRESSION

Return to odd prime subgroup order `K` and define the non-forced mixed excess

`Delta_K(p)=sum_{d!=0}r_{A-A}(d)^2-(K-1)(2K-5)`

for split primes `p==1 mod K`.

Simultaneous exponent scaling partitions all non-forced collision quadruples into

`N_K=K^3-5K^2+6K+1`

free Galois orbits. For a normalized orbit `q`, the number of its members that collide modulo `p` is the number of primitive `K`-th roots common to `P_q` and `Phi_K`, hence is at most `v_p(Res(Phi_K,P_q))`.

Using the exact square structure

`Res(Phi_K,P_q)=K^3 M_q^2`

and the fact that a split prime is never `K`, the fixed `K^3` factor carries no collision valuation. The coefficient norm then gives

> `sum_{p==1 mod K} Delta_K(p) log p`
> `<= (K^3-5K^2+6K+1)((K-1)log12-3logK)`.

Thus the entire non-forced collision mass over all split primes has a deterministic `O(K^4)` logarithmic budget. In particular, for `P>=2` and `L>0`,

`sum_{p>=P, p==1 mod K} Delta_K(p) <= N_K C_K/log P`,

`#{p>=P, p==1 mod K:Delta_K(p)>=L} <= N_K C_K/(L log P)`,

where `C_K=(K-1)log12-3logK`.

These are average/sparsity statements, not a pointwise `O(K^2)` theorem. The exact `K=11,13` regression verifies the Galois-orbit/root/valuation mechanism and, on those finite designs, observes equality between summed valuations and direct excess.

See [`cayley_resultant_mass_budget.md`](cayley_resultant_mass_budget.md).

## 15. Matching audit and fixed-K exceptional sets — FINITE-CERTIFICATE

The 720 integer matching systems have ranks `30` (rank 2), `240` (rank 3), `450` (rank 4); the maximal-minor gcd audit permits an additional rank drop only in characteristic 2.

Complete maintained cyclotomic resultant enumerations are promoted for exactly

`E_11={23,67,89}`

and

`E_13={53,79,131,157,313}`.

At `(p,K)=(461,23)` the exact mixed Cayley collision energy is `1190`, the forced baseline is `902`, and the excess is `288`.

## 16. Off/off elliptic organization — DRAFT

Historical symbolic calculations organize the remaining off/off fluctuation by a non-isotrivial genus-one/elliptic pencil and exhibit candidate bad fibers and same-`j` relations. These calculations are structural evidence, not a current theorem certificate.

The target

`O(K^2 p + K^4 sqrt(p) + K^4)`

and regime `K=o(p^(1/4))` remain theorem-draft conclusions until the projective model, bad fibers, twists/isogenies, sheaf irreducibility/complexity, affine boundary and exact correlation-theorem hypotheses are all closed.

## 17. Earlier finite foundations — SCOPED

- Lean finite level-set/orbit/freeness facts at `p=199, K=11`;
- Lean branch-scale identities at the same design;
- maintained finite twisted-Jacobi scalar and q-curve regressions;
- correct antiunitary eigenspace-preservation logic on its audited scope;
- historical shape/relation evidence retained only in Git history, while all-orders Catalan/arcsine claims remain unpromoted because the historical word-trace reduction had an unresolved rewrite case.

See [`earlier_foundations.md`](earlier_foundations.md).

## 18. Numerical GOE comparisons — NUMERICAL ONLY

The maintained spectral code diagonalizes the full complex Hermitian matrix `M+M^*`. The spacing record reports only a descriptive empirical-CDF distance to the Wigner surmise. The matched window-count record is not stationary number variance. Neither carries inferential pass/fail semantics.

A reconstruction-era implementation briefly projected `M+M^*` to its entrywise real part before diagonalization; the numerical evidence was regenerated after that bug was found. No exact result depended on those floating-point records.

## 19. BGS local statistics — OPEN

Nothing above proves microscopic BGS/GOE eigenphase statistics for the arithmetic cat-map family. A local-law/comparison mechanism remains a separate open bridge. Rigorous BGS results do exist for special model classes such as mixing quantum graphs under their own hypotheses; they are not transferable to this family without a new argument.
