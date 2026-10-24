# Off/off elliptic pencil: superseded route and current theorem

**Status: SUPERSEDED-HISTORICAL.**  The former `DRAFT` in this file has now
been replaced by the corrected theorem in
[`offoff_elliptic_spike_theorem.md`](offoff_elliptic_spike_theorem.md).
This file is retained to make the proof-history and the load-bearing correction
explicit.

## 1. Where the pencil enters

The exact fourth-moment distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

The pure off/off term `O(t)` decomposes into parameter classes indexed by
`lambda=(h1,h2) in H^2`.  In Cayley coordinates a generic class is a
one-parameter genus-one pencil.

The historical route correctly identified non-isotrivial elliptic geometry and
the need for square-root correlations between the associated `R^1` trace
sheaves, but it missed one essential singular fiber.

## 2. The missing reducible fiber

For a generic parameter class write

```text
alpha=c(h1), beta=c(h2),
d=alpha-beta.
```

At

```text
t_lambda=2/d
```

the cleared cubic does not merely acquire an ordinary singularity: it factors
into two affine lines.  After the exact valid-domain exclusions, the fiber has

```text
O_lambda(t_lambda)=2p-8.
```

Thus every generic class carries an `O(p)` spike.  Parameter classes with the
same Cayley difference `alpha-beta` place those spikes at the same `t`.
Their coherent second moment is controlled by the additive energy of

```text
A=c(H\{1}).
```

This invalidates the old unconditional target

```text
O(K^2p+K^4 sqrt(p)+K^4)
```

unless an additional quadratic Cayley-energy hypothesis is supplied.

## 3. Corrected theorem

After extracting the reducible spike, the remaining generic fibers are governed
by uniformly bounded-conductor, geometrically irreducible rank-two elliptic
trace sheaves.  Their finite singular support recovers the generic parameter
up to the exact involution

```text
(h1,h2) <-> (h2^(-1),h1^(-1)).
```

Grothendieck--Lefschetz plus Deligne's Riemann Hypothesis then gives
square-root complete correlations outside those `O(K^2)` same/involution
pairs.  The `O(K)` non-generic parameter strata are handled directly.

The resulting theorem is

```text
Var_{t!=0} O(t)
 << p E_+(c(H\{1}))
    +K^2p
    +K^4 sqrt(p)
    +K^4.
```

See `offoff_elliptic_spike_theorem.md` for the exact discriminant, the
`2p-8` line count, singular-support classification, special strata, source
hypotheses and verification producer.

## 4. Consequence in the current pointwise range

The maintained direct Cayley theorem gives

```text
E_+(c(H\{1}))<34K^(8/3)
```

for `100<K<p^(3/4)/3`.  Hence

```text
Var O
 << pK^(8/3)+K^4 sqrt(p)+K^2p+K^4.
```

In particular, for `K=o(p^(1/4))`,

```text
Var O << pK^(8/3).
```

The former elliptic/sheaf obstruction has therefore collapsed onto the same
pointwise Cayley additive-energy problem that controls the mixed layer.

## 5. What remains open

The sharp pointwise target is

```text
E_+(c(H\{1}))
 =(K-1)^4/p+O(K^(2+o(1))).
```

No verified theorem currently removes the remaining `K^(2/3)` loss in every
split reduction.  Even if this pointwise energy target and the full fourth
moment are completed, a microscopic BGS/GOE local eigenphase law remains a
separate local-statistics/comparison problem.
