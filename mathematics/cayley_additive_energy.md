# Mixed pair-key term as Cayley additive energy

**Status: EXACT for the reduction; EXACT FINITE ALGEBRA for the audited fixed-`K` exceptional-prime sets.**

Let `H <= F_p^*` have odd prime order `K`, and let `A=c(H\{1})` with `c(h)=(h+1)/(h-1)`.

## Exact identity

For distinct `u,v in H\{1}`,

`d(u,v)=(u-1)(v-1)/(v-u)=2/(c(u)-c(v))`.

Consequently the nonzero multiplicities of the mixed histogram `C_H(t)` are the nonzero difference multiplicities of `A`, up to the bijection `x -> 2/x`. Therefore

`sum_t C_H(t)^2 = sum_{x!=0} r_{A-A}(x)^2 = E_+(A)-|A|^2`.

The inversion identity `c(h^-1)=-c(h)` gives `A=-A`. These symmetry collisions are forced and define the baseline used by the finite certificates.

The same multiplicity has the PGL2 intersection description

`r_{A-A}(x)=#{h in H\{1}: ((2-x)h+x)/(2+x-xh) in H\{1}}`.

The active exact verifier checks this identity directly on every representative finite-field design below.

## Characteristic-zero matching classification

After writing subgroup elements as powers of a primitive `K`-th root and clearing denominators, equality of two Cayley differences becomes equality of two six-term multisets. There are `6!=720` possible matchings.

The exact integer-linear classification is `30` rank-2, `240` rank-3 and `450` rank-4 systems. The gcd of maximal nonzero minors shows that the only possible additional rank drop occurs in characteristic `2`. For odd `K`, every admissible positive-dimensional characteristic-zero kernel is the identity or inversion-swap symmetry; the remaining low-rank systems force a forbidden zero or diagonal.

## Fixed-K bad reduction primes

For a non-forced system, the cleared collision polynomial is a nonzero element of the `K`-th cyclotomic field. A finite-field collision can therefore appear only at rational primes dividing its cyclotomic norm. Normalizing one exponent by scaling makes the enumeration finite.

The exact resultant computation gives

`E_11={23,67,89}`

from 793 normalized non-forced quadruples and 8 distinct nonzero norms, and

`E_13={53,79,131,157,313}`

from 1431 quadruples and 14 distinct norms.

The CI producer recomputes these resultants from scratch: `computations/verification/mixed_cayley_energy.py`.

The same script cross-checks the prediction in both directions:

- `(53,13)`: exceptional, excess `208>0`;
- `(67,11)`: exceptional, excess `48>0`;
- `(199,11)`: non-exceptional, excess `0`;
- `(521,13)`: non-exceptional, excess `0`.

The previous historical verifier accepted an expected exceptional prime without requiring observed excess. The active verifier deliberately closes that regression loophole.

## Non-uniformity witness

At `(p,K)=(461,23)`, `sum_t C_H(t)^2=1190` while the forced baseline is `902`. The excess `288` proves that “only the forced baseline” is not a uniform-in-`K` statement.

## Scope

For each fixed odd prime `K`, the cyclotomic argument yields only finitely many bad reduction primes. Nothing here supplies a useful bound uniform in growing `K`, and no part of this argument proves BGS local statistics.
