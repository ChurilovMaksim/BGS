# M1 note — why the historical Möbius fiber is not the exact pair-key image

This note is now an audit note, not the definition of the active M1 object.

## 1. Exact elimination

From the off-diagonal pair-key map

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`,

one obtains

`y=(1-v)/(u-v)`,
`x=u(1-v)/(u-v)`,
`d=(u-1)(v-1)/(v-u)`.

Solving for `v` gives the historical rational graph

`v_d(u)=((d-1)u+1)/(d+1-u)`.

Wolfram symbolic algebra independently reproduces these identities.

## 2. Saturation artifact at (1,1)

The eliminated polynomial relation is satisfied by `(u,v)=(1,1)` for **every** `d`. But at that point the inverse formula is `0/0`; no off-diagonal pair `(x,y)` is represented.

For `d!=0`, the historical graph nevertheless contains `u=1,v=1`. Thus it adds one phantom point of character weight `1` for every twist pair.

At `d=0`, the elimination degenerates in the opposite direction. The exact pair-key table contains the true diagonal record `(1,1)` with multiplicity `N-2`, while the historical graph becomes the line-like sum `v=1` over `u!=1`.

## 3. Exact correction formula

Let `A_hist` be the historical graph amplitude and `A_key` the exact pair-key amplitude. Independent finite computations at `N=53` and `N=199` verify, to floating-point roundoff,

- for every `d!=0` and every twist pair:
  `A_hist(d)=A_key(d)+1`;
- at `d=0`, if the first twist is trivial:
  `A_hist(0)=A_key(0)=N-2`;
- at `d=0`, if the first twist is nontrivial:
  `A_hist(0)=-1` while `A_key(0)=N-2`.

The Fourier-space difference is therefore explicit as well:

- first twist trivial: `(N-1,-1,-1,...,-1)`;
- first twist nontrivial: `(0,-N,-N,...,-N)`.

The updated `experiments/m1/cross_term_energy.py` checks this formula directly.

## 4. Numerical consequence

The normalized historical and correct energies are not the same object:

- `N=53,K=13`: historical `3,682,650,293`; correct `3,410,502,105`;
- `N=199,K=11`: historical `113,859,701,371`; correct `115,589,503,389`.

The correct values equal the independently computed `sum_t B(t)^2`.

Therefore the historical Möbius route cannot be repaired merely by improving its Weil bound or restoring cross terms. Its finite assembly is wrong before the asymptotic estimate begins.

## 5. What remains useful from the old divisor analysis

For the historical graph itself, the projective matrix of `v_d` has determinant/resultant `d^2`, the pole is `u=d+1`, and its character divisor analysis correctly identifies `d=0` as degenerate once the annihilator character order is taken to be `m=(N-1)/K` rather than `K`.

That analysis explains additional failure modes of the old proof, but it is now historical diagnostics only. The active M1 proof works with the exact pair-key distribution `B(t)` in `research/theory.md`.
