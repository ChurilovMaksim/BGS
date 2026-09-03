# Cayley energy and exceptional reductions

For `h!=1` define `c(h)=(h+1)/(h-1)`. Direct algebra gives

`d(u,v)=(u-1)(v-1)/(v-u)=2/(c(u)-c(v))`.

Thus the mixed distribution `C_H` is the nonzero additive-difference representation function of `A=c(H\{1})`, up to the bijective relabelling `Delta -> 2/Delta`. Consequently

`sum_t C_H(t)^2 = E^+(A)-|A|^2`.

Since `c(h^-1)=-c(h)`, for odd `K` one has `A=-A` and `0 notin A`. The involution `(a,b)->(-b,-a)` forces the baseline

`(K-1)(2K-5)`.

For odd prime `K`, clearing denominators in a Cayley-difference collision gives a sparse cyclotomic relation. The active exact classification checks all `6!=720` exponent matchings. Over `Q` their ranks are 30 of rank 2, 240 of rank 3 and 450 of rank 4; maximal minors can lose rank only in characteristic 2. After discarding zero-exponent and diagonal degeneracies, the only positive-dimensional collision families are identity and inversion-swap.

Reduction modulo `N` may nevertheless create extra collisions. After Galois normalization, let `P_{1,j,r,s}` denote a non-forced collision polynomial and define the fixed-`K` exceptional set from prime divisors of the nonzero resultants `Res(Phi_K,P_{1,j,r,s})` that are congruent to 1 modulo `K`.

The active gate fully enumerates

`E_11={23,67,89}`,
`E_13={53,79,131,157,313}`.

For `N notin E_K`,

`sum_t C_H(t)^2=(K-1)(2K-5)`

and hence the mixed M1 term `2(N-2)C_H(t)` has standard deviation `O(K sqrt(N))`.

This statement is **fixed-K**. It is not a uniform theorem for growing `K`. The exact negative control `(N,K)=(461,23)` gives

`sum_t C_H(t)^2=1190`,

while the forced baseline is `902`; hence this level is exceptional for `K=23`. The regression `experiments/verification/verify_cayley_anchor_k23.py` permanently checks this point so the fixed-`K` qualifier cannot silently disappear again.
