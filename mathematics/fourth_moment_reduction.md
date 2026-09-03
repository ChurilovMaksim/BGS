# Exact fourth-moment pair-key reduction

**Status: EXACT**, with independent finite Python/C++ regression checks.

## Pair keys

For `x,y in F_p \ {0,1}`, define

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

If `x != y`, then `u,v notin {0,1}`, `u != v`, and inversion gives

`y=(1-v)/(v-u)`, `x=u(1-v)/(v-u)`, and `d=(u-1)(v-1)/(v-u)`.

Hence the off-diagonal map is bijective. If `x=y`, every one of the `p-2` allowed diagonal pairs maps to `(u,v,d)=(1,1,0)`; the collapsed diagonal key therefore has multiplicity `p-2`.

This weighted diagonal is essential. Treating it as multiplicity one changes every later moment count.

## Coupling two keys

Let `H <= F_p^*` have order `K`. Two collapsed keys couple when `u1*u2 in H` and `v1*v2 in H`. Let `B(t)` be the weighted number of ordered coupled pairs with `d1+d2=t`.

Splitting by whether each key is diagonal gives

`B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}`.

The coefficient 2 is not optional: diagonal/off and off/diagonal are distinct ordered classes.

The exact class total is

`|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K`.

## Fourier identity

Character orthogonality gives, in the active normalization,

`sum_{chi,psi} |J(chi,psi;q)|^4 = m^2 sum_t B(t)e_p(qt)`,

with `m=(p-1)/K` for the audited annihilator designs. Finite Fourier orthogonality therefore determines the nonzero-frequency mean and centered second moment exactly from `B(0)`, the total mass and the `L^2` energy of `B`. No random-matrix hypothesis enters here.

## Verification

- current finite regression: `computations/verification/current_regression.py`;
- independent C++ implementation: `computations/cpp/fourth_moment_pair_key_verifier.cpp`;
- promoted finite record: `evidence/certificates/fourth_moment_factorization.json`.

Larger-prime anchors use the validated fast pair-key geometry; direct original-pair and explicit-key loops are intentionally restricted to smaller `p`, where they provide an independent implementation check at reasonable cost.

## What this does not prove

The reduction identifies the fluctuation problem but does not bound the off/off energy `O(t)` uniformly. That remaining step is the elliptic-pencil draft in `elliptic_pencil.md`.
