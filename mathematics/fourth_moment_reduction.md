# Exact fourth-moment pair-key reduction

**Status: EXACT**, with independent finite Python/C++ regression checks.

## Pair keys

For `x,y in F_p \ {0,1}`, define

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

If `x != y`, then `u,v notin {0,1}`, `u != v`, and inversion gives

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`, and `d=(u-1)(v-1)/(v-u)`.

The sign in the first two denominators matters: it follows directly from `(u-v)y=1-v`. The diagonal `x=y` collapses to `(u,v,d)=(1,1,0)` with multiplicity `p-2`.

## Coupling two keys

Let `H <= F_p^*` have order `K`. Two collapsed keys couple when `u1*u2 in H` and `v1*v2 in H`. Let `B(t)` be the weighted number of ordered coupled pairs with `d1+d2=t`.

Splitting by whether each key is diagonal gives

`B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}`.

The coefficient 2 is essential: diagonal/off and off/diagonal are distinct ordered classes.

The exact class total is

`|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K`.

## Fourier identity

Character orthogonality gives, in the active normalization,

`sum_{chi,psi} |J(chi,psi;q)|^4 = m^2 sum_t B(t)e_p(qt)`.

Finite Fourier orthogonality therefore determines the nonzero-frequency mean and centered second moment from `B(0)`, the total mass and the `L^2` energy of `B`. No random-matrix independence assumption enters.

## Verification

- fast exact anchors: `computations/verification/current_regression.py`;
- independent implementation: `computations/cpp/fourth_moment_pair_key_verifier.cpp`;
- promoted finite record: `evidence/certificates/fourth_moment_factorization.json`.

The current promoted JSON contains only quantities independently checked by the active C++ verifier. Historical heuristic `B(0)` error-bound subrecords were removed from the promoted evidence and remain available only in Git history.

## What this does not prove

The reduction identifies the fluctuation problem but does not bound the off/off energy `O(t)` uniformly. That remaining step is the elliptic-pencil draft in `elliptic_pencil.md`.
