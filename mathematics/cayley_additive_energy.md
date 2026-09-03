# Mixed pair-key term as Cayley additive energy

**Status: EXACT for the reduction; FINITE-CERTIFICATE for the audited `K=11,13` cyclotomic exceptional sets.**

Let `H <= F_p^*` have odd prime order `K`, and set `A=c(H\{1})` with `c(h)=(h+1)/(h-1)`.

## Exact reduction

For distinct `u,v in H\{1}`,

`d(u,v)=(u-1)(v-1)/(v-u)=2/(c(u)-c(v))`.

Thus the nonzero multiplicities of `C_H(t)` equal the nonzero difference multiplicities of `A` up to the permutation `x -> 2/x`, and

`sum_t C_H(t)^2 = E_+(A)-|A|^2`.

Since `c(h^-1)=-c(h)`, `A=-A`; the resulting central-symmetry collisions give the forced baseline `(K-1)(2K-5)` used by the finite verifier.

The same multiplicity can be written as a PGL2 intersection count

`r_{A-A}(x)=#{h in H\{1}: ((2-x)h+x)/(2+x-xh) in H\{1}}`.

## Integer matching classification

Clearing a Cayley-difference collision and matching the six terms produces `6!=720` integer linear systems. Their characteristic-zero ranks are 30 of rank 2, 240 of rank 3, and 450 of rank 4. The gcds of maximal nonzero minors show that an additional rank drop can occur only in characteristic 2. The admissible positive-dimensional low-rank kernels are identity/inversion-swap symmetries; the others force forbidden zero/diagonal configurations.

This classification is recomputed by `computations/verification/mixed_cayley_energy.py`.

## Cyclotomic exceptional primes: audited values

For a specified prime `K`, a normalized non-forced collision gives a cyclotomic algebraic integer. If it is nonzero, finite-field collisions can occur only at rational primes dividing its norm. The repository performs the complete normalized nonvanishing/resultant enumeration for:

`E_11={23,67,89}`

from 793 normalized non-forced quadruples and 8 distinct nonzero norms, and

`E_13={53,79,131,157,313}`

from 1431 quadruples and 14 distinct nonzero norms.

The active verifier also checks the prediction in both directions on representative fields:

- `(53,13)`: exceptional, excess 208;
- `(67,11)`: exceptional, excess 48;
- `(199,11)`: non-exceptional, excess 0;
- `(521,13)`: non-exceptional, excess 0.

The historical verifier had a one-way regression loophole: an expected exceptional prime could pass without requiring observed excess. The current verifier requires `exceptional <=> excess>0` on these audited designs.

## Non-uniformity witness

At `(p,K)=(461,23)`, `sum_t C_H(t)^2=1190` while the forced baseline is `902`. The excess `288` is an exact warning against extrapolating the `K=11,13` pattern uniformly in growing `K`.

## Scope

The cyclotomic mechanism explains why a fixed specified `K` leads to finitely many bad reductions once the relevant collision polynomials are proved nonzero. The current repository explicitly computes the complete exceptional sets only for `K=11` and `K=13`; it does not claim an explicit or useful uniform bound for arbitrary growing `K`.
