# Mixed pair-key term as Cayley additive energy

**Status: EXACT for the reduction and the prime-order cutoff below; FINITE-CERTIFICATE for the audited `K=11,13` exact exceptional sets.**

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

## Uniform prime-order characteristic-zero rigidity — EXACT

Let `K` be an odd prime and `zeta=exp(2*pi*i/K)`. For `1 <= j <= K-1`,

`c(zeta^j) = -i cot(pi*j/K)`.

Chowla's theorem states that

`cot(pi*a/K), 1 <= a <= (K-1)/2`,

are linearly independent over `Q`; Kai Wang's 1982 extension reproduces this prime case as Theorem A and extends it to more general moduli and derivatives. See the exact references in `literature/bibliography.md`.

Write `b_a=cot(pi*a/K)` for `1<=a< K/2`. Every nonzero-index cotangent is exactly one of the vertices `+b_a` or `-b_a`. By Chowla's linear independence, a relation

`cot(pi*i/K)-cot(pi*j/K) = cot(pi*r/K)-cot(pi*s/K)`

is equivalent to the same relation among vertices of the rational cross-polytope `{+e_a,-e_a}`.

The needed cross-polytope lemma is elementary. If `x,y,u,v` are vertices in `{+e_a,-e_a}` with `x!=y`, `u!=v` and

`x-y=u-v`,

then `x+v=u+y`. If `x+v=0`, then `v=-x` and also `u=-y`, giving the central-inversion swap `(u,v)=(-y,-x)`. If `x+v!=0`, a nonzero sum of two cross-polytope vertices determines its unordered pair of summands uniquely; hence `{x,v}={u,y}`. The alternative `x=y` is excluded, so `(u,v)=(x,y)`.

Therefore every characteristic-zero Cayley-difference collision is forced:

- identity: `(r,s)=(i,j)`;
- central-inversion swap: `(r,s)=(-j,-i)` modulo `K`.

No enumeration in `K` is required for this characteristic-zero statement.

## Explicit finite-field exceptional-prime cutoff — EXACT

For nonzero pairwise-domain indices `i!=j`, `r!=s`, set

```text
P_{i,j,r,s}(X)
 = X^(r+s+i) - X^(r+s+j) - X^(r+i+j) + 2 X^(r+j) - X^r
   + X^(s+i+j) - 2 X^(s+i) + X^s + X^i - X^j.
```

The exponents may be reduced modulo `K` when evaluating at a `K`-th root. Direct clearing of the four Cayley denominators gives the exact identity

```text
2 P_{i,j,r,s}(X)
 = (c(X^r)-c(X^s)-c(X^i)+c(X^j))
   (X^r-1)(X^s-1)(X^i-1)(X^j-1).
```

After collecting equal monomials, `||P||_1 <= 12`.

If the quadruple is non-forced, the characteristic-zero rigidity above gives `P(zeta) != 0`. Since the prime cyclotomic polynomial `Phi_K` is irreducible over `Q`,

`R=Res(Phi_K,P)`

is a nonzero integer. Because `Phi_K` is monic and its roots are `zeta^a`, `1<=a<=K-1`,

```text
|R| = product_{a=1}^{K-1} |P(zeta^a)| <= 12^(K-1).
```

Now let `p` be a rational prime with `K | (p-1)`, and let `h in F_p^*` have exact order `K`. A non-forced finite-field collision would give `P(h)=0`. Since also `Phi_K(h)=0`, the two integer polynomials have a common root modulo `p`, so

`p | Res(Phi_K,P)=R`.

Consequently every rational prime supporting a non-forced collision satisfies

`p <= 12^(K-1)`.

Equivalently:

> **Uniform cutoff theorem.** If `K` is an odd prime, `K | (p-1)`, and `p > 12^(K-1)`, then every Cayley-difference collision in `A=c(H\{1})` is forced by identity or central inversion.

Let `n=|A|=K-1`. There are exactly `n` ordered antipodal pairs `(a,-a)`, each fixed by the inversion swap. The remaining `n(n-2)` ordered nonzero pairs form two-element inversion-swap orbits. Hence above the cutoff

```text
sum_t C_H(t)^2
 = n + 4 * n(n-2)/2
 = n(2n-3)
 = (K-1)(2K-5).
```

This closes a genuine growing-`K` part of the mixed-term problem: the exact forced-baseline formula holds whenever

`K-1 < log(p)/log(12)`.

The cutoff is exponential in `K`; it is therefore far weaker than the polynomial-scale regime needed to match the draft off/off target `K=o(p^(1/4))`. Improving `12^(K-1)` to a substantially smaller arithmetic obstruction, or avoiding a uniform mixed-term bound in the eventual local-statistics argument, remains open.

## Cyclotomic exceptional primes: audited exact values

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

## Non-uniformity witness below the uniform cutoff

At `(p,K)=(461,23)`, `sum_t C_H(t)^2=1190` while the forced baseline is `902`. The excess `288` is an exact warning against extrapolating the exact baseline to all fields at a fixed or growing `K`. It is fully compatible with the cutoff theorem, because `461 < 12^22`.

## Scope

The new cutoff is a uniform theorem for every odd prime subgroup order `K`; it does not enumerate the exceptional primes below `12^(K-1)` and does not control the mixed term in the desired `K=o(p^(1/4))` regime. The complete exact exceptional sets currently computed remain only `K=11` and `K=13`.