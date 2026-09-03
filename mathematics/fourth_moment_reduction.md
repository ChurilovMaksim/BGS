# Exact fourth-moment pair-key reduction

**Status: EXACT**, with independent finite Python/C++/Lean regression checks.

## Pair keys

Let `p` be an odd prime. For `x,y in F_p \ {0,1}`, define

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

If `x != y`, then `u,v in F_p^* \ {1}`, `u != v`, and

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`,
`d=(u-1)(v-1)/(v-u)`.

Conversely those formulas recover a unique admissible off-diagonal `(x,y)` from
every `u,v in F_p^* \ {1}` with `u != v`. The diagonal `x=y` collapses to the
single key `(u,v,d)=(1,1,0)` with multiplicity `p-2`.

The sign in the inverse denominators is load-bearing: `(u-v)y=1-v`.

## Exact constrained-pair count

Let `H <= F_p^*` have order `K`. Imposing the two subgroup constraints on an
off-diagonal pair is exactly the condition

`u,v in H \ {1}`, `u != v`.

The pair-key bijection therefore gives the general identity

`#P_2=(K-1)(K-2)`.

This is an **EXACT** count for every odd prime `p` and subgroup `H` in the
stated setup. `formalization/Bgs/PairKeySecondMoment.lean` is an additional
finite certificate at `(p,K)=(53,13)`; it is not the source of the general
proof.

## Coupling two collapsed keys

Give each collapsed key its multiplicity `n_r`. Two ordered keys couple when
`u_r u_s in H` and `v_r v_s in H`. Let `B(t)` be their
multiplicity-weighted difference-sum distribution:

`B(t)=sum_{r,s} n_r n_s 1_H(u_r u_s) 1_H(v_r v_s) 1_{d_r+d_s=t}`.

Splitting by whether either key is the weighted diagonal gives

`B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}`.

The coefficient `2` is essential: diagonal/off and off/diagonal are distinct
ordered classes.

The exact total coupled count is

`|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K`.

## Character orthogonality and finite Fourier moments

Let `S=H^perp` be the multiplicative-character annihilator of `H`. Then

`m=|S|=(p-1)/K`.

With the maintained twisted-Jacobi convention,

`sum_{chi,psi in S} |J(chi,psi;q)|^4 = m^2 Sigma4(q)`,

where

`Sigma4(q)=sum_t B(t)e_p(qt)`.

(Changing the Fourier sign convention conjugates the transform and does not
change the real mean/variance identities below.)

Write

`V=sum_t B(t)`, `Z=B(0)`.

Finite Fourier orthogonality gives the exact nonzero-frequency mean

`E_{q!=0} Sigma4(q)=(p Z-V)/(p-1)`,

and Parseval gives the exact variance identity

`Var_{q!=0} Sigma4(q)=p Var_{t!=0} B(t)`.

Thus the target fluctuation scale for `Sigma4` is equivalent to a concrete
`L^2`-fluctuation problem for `B`; no probabilistic independence assumption
enters this reduction.

## Verification

- fast exact anchors and API contracts:
  `computations/verification/current_regression.py`;
- independent exhaustive implementation:
  `computations/cpp/fourth_moment_pair_key_verifier.cpp`;
- finite Lean checks:
  `formalization/Bgs/PairKeySecondMoment.lean` and
  `formalization/Bgs/PairKeyFourthMoment.lean`;
- promoted finite record:
  `evidence/certificates/fourth_moment_factorization.json`.

The promoted JSON contains only quantities checked by maintained code.
Superseded heuristic error-bound subrecords remain only in Git history.

## What this does not prove

The reduction isolates the fluctuation problem but does not yet bound the
centered off/off energy uniformly. That is the theorem-draft elliptic route in
[`elliptic_pencil.md`](elliptic_pencil.md), and even its completion would still
leave the microscopic BGS bridge open.
