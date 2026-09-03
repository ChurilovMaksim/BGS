# Current mathematical core

This file records the active exact structure. Historical proof objects are kept in `archive/` and are not theorem inputs.

## 1. Character convention

Let `N` be an odd prime, let `H=<a> <= F_N^*` have order `K`, and let

`S = H^perp`

be the annihilator subgroup of multiplicative characters. Its size is

`m = |S| = (N-1)/K`.

For multiplicative characters `chi, psi in S` and additive frequency `q`, use

`J(chi,psi;q) = sum_{x != 0,1} conjugate(chi(x)) psi(x-1) e_N(qx)`.

If `g` is a primitive root, then `S={chi_(Kj): j mod m}`. The natural generator `rho=chi_K` has order `m`, not `K`.

## 2. The exact pair-key table

For ordered pairs `x,y in F_N \ {0,1}`, define

`u = x/y`,
`v = (x-1)/(y-1)`,
`d = x-y`.

The diagonal `x=y` collapses to the single key `(u,v)=(1,1)`, with multiplicity `N-2` and difference `d=0`.

Off the diagonal the map is a bijection onto

`D_off = {(u,v): u,v in F_N^* \ {1}, u != v}`,

and the inverse and difference are

`y = (1-v)/(u-v)`,
`x = u(1-v)/(u-v)`,
`d(u,v) = (u-1)(v-1)/(v-u)`.

Hence the collapsed key table has exactly

`(N-2)(N-3)+1`

records: one weighted diagonal record and `(N-2)(N-3)` unit-weight off-diagonal records.

## 3. Exact k=2 reduction

The `k=2` constraint requires the off-diagonal key itself to lie in `H x H`. Therefore the number of off-diagonal constrained pairs is exactly

`(K-1)(K-2)`.

The active verifier reproduces this reduction independently at the audited finite designs. It is logically independent of the later `k=4` asymptotics.

## 4. The k=4 difference distribution

For key records `r=(u_r,v_r,d_r,n_r)`, define the ordered coupled difference distribution

`B(t) = sum_{r,s} n_r n_s 1_H(u_r u_s) 1_H(v_r v_s) 1_{d_r+d_s=t}`.

Then

`V4 = sum_t B(t)`

is the exact four-variable constraint-variety count,

`Z0 = B(0)`,

and

`E_B = sum_t B(t)^2`

is the exact coupled difference energy.

The active Python and C++ verifiers independently reproduce `B(t)` and its derived invariants at `N=23,53,199,461`.

### 4.1 Exact coupling-class totals

There are four ordered classes. The diagonal-diagonal class is

`(N-2)^2`.

Each ordered diagonal/off-diagonal class has exact size

`(N-2)(K-1)(K-2)`.

For off-diagonal/off-diagonal coupling, fix `(u,v) in D_off`. A partner has the form

`(u',v')=(h1/u,h2/v)`,  `(h1,h2) in H^2`.

It fails to lie in `D_off` only through the three conditions

`h1=u`, `h2=v`, `h1 v = h2 u`.

Summing the resulting inclusion-exclusion over `D_off` gives the exact total

`V_off = K^2 (N-2)(N-3) - 3K(K-1)(N-3) + 2(K-1)(K-2)`.

Consequently

`V4 = V_off + 2(N-2)(K-1)(K-2) + (N-2)^2`

and therefore

`V4 = (K^2+1)N^2 - (6K^2+3K)N + 13K^2 - 3K`.

This is an exact combinatorial identity, not an asymptotic estimate.

## 5. Exact character collapse of the full twist assembly

Define the correct key-table amplitude

`A_(chi,psi)(d) = sum_{r: d_r=d} n_r chi(u_r) psi(v_r)`.

Double character orthogonality gives, for every `t`,

`sum_{chi,psi in S} (A_(chi,psi) * A_(chi,psi))(t) = m^2 B(t)`.

With the unnormalized finite Fourier transform

`f_hat(xi)=sum_d f(d)e_N(-xi d)`,

this is equivalently

`sum_{chi,psi in S} A_hat_(chi,psi)(xi)^2 = m^2 B_hat(xi)`.

Thus the full cross-twist assembly is not an uncontrolled sum of unrelated energies: it collapses exactly to the single key-table object `B`.

The active verifier checks this identity in both time and frequency domains through `N=199`; an independent C++ implementation uses direct DFT/circular convolution rather than NumPy FFT.

## 6. Exact fourth-moment factorization

Expanding `J^2 conjugate(J)^2` and applying character orthogonality twice yields

`sum_{chi,psi in S} |J(chi,psi;q)|^4 = m^2 Sigma_4(q)`,

where

`Sigma_4(q) = sum_t B(t)e_N(qt)`.

More generally, for every fixed `s>=1`, the same argument gives the exact even-moment reduction

`sum_{chi,psi in S} |J(chi,psi;q)|^(2s) = m^2 Sigma_(2s)(q)`

to the corresponding two-product constraint variety. The reduction is exact; estimating the high-dimensional variety is a separate analytic problem.

## 7. Exact mean/variance duality

Write

`V = sum_t B(t)`, `Z = B(0)`, and `Sigma(q)=sum_t B(t)e_N(qt)`.

Averaging over `q != 0` gives exactly

`mean_(q!=0) Sigma(q) = (N Z - V)/(N-1)`.

Let `B_off_mean=(V-Z)/(N-1)`. Since the centered off-zero values sum to zero, finite Fourier orthogonality gives the exact variance identity

`Var_(q!=0) Sigma(q) = N Var_(t!=0) B(t)`.

Therefore

`std_(q!=0) Sigma_4 = O(NK)`

is equivalent to the geometric statement

`std_(t!=0) B(t) = O(K sqrt(N))`.

If the mean is asymptotic to a nonzero constant times `N^2`, this yields relative fluctuation `O(K/N)` and hence concentration whenever `K=o(N)`.

## 8. Structural decomposition of B(t)

Let

`C_H(t) = # {(u,v) in (H\{1})^2 : u!=v, d(u,v)=t}`

and let `O(t)` denote the off-diagonal/off-diagonal coupled contribution. Then exactly

`B(t) = O(t) + 2(N-2) C_H(t) + (N-2)^2 1_{t=0}`.

Because `d(u,v)` is never zero on the off-diagonal `H x H` domain,

`C_H(0)=0`.

This separates the variance problem into an off-off curve family, a lower-dimensional `k=2` collision term, and a deterministic diagonal spike.

## 9. Why the mean has an N^2-scale main term

Inside `O(0)`, the class `(h1,h2)=(1,1)` sends

`(u,v) -> (u^-1,v^-1)`

and satisfies

`d(u^-1,v^-1) = -d(u,v)`.

Hence every off-diagonal key contributes, giving the exact spike

`(N-2)(N-3)`.

Together with the diagonal-diagonal spike `(N-2)^2`, this already produces two deterministic `N^2`-scale contributions to `B(0)`.

For `h1=h2=h!=1`,

`d(u,v)+d(h/u,h/v) = (h-1)(uv-h)/(h(v-u))`,

so the zero-difference condition reduces exactly to `uv=h`. Its valid count is

`N-4-eta(h)`,

where `eta` is the quadratic character of `F_N^*`. For `h1=1,h2!=1` or the reverse, there are no valid zero-difference off-off solutions.

For `h1,h2!=1` and `h1!=h2`, a direct resultant calculation for the `t=0` cubic gives a singularity obstruction proportional to

`h1^5 h2^6 (h1-1)^14 (h1-h2)^4 (h2-1)^18`.

Thus no generic `t=0` parameter is singular. The projective completion is a smooth plane cubic, hence genus one. Removing the finite boundary changes its point count by `O(1)`, so Hasse-Weil gives

`M_(h1,h2)(0)=N+epsilon_(h1,h2)`,
`|epsilon_(h1,h2)| <= 2 sqrt(N)+28`

with the displayed constant coming from a conservative union bound over the boundary lines.

Let

`S_eta=sum_{h in H\{1}} eta(h)`.

Then the deterministic part of `B(0)` is

`B0_det = 2N^2 + K^2 N - 2KN - 8N - 4K + 14 - S_eta`,

and

`B(0)=B0_det + R0`,
`|R0| <= (K-1)(K-2)(2 sqrt(N)+28)`.

Since `S_eta=K-1` when `m` is even and `S_eta=-1` when `m` is odd, the exact mean identity yields

`mean_(q!=0) Sigma_4(q) = 2N^2 + O(KN + N + K^2 sqrt(N))`.

In particular, the mean is asymptotic to `2N^2` whenever `K=o(N^(3/4))`. The algebraic resultant factorization has been independently reproduced by SymPy and Wolfram; it should still be converted into a hand/formal lemma before publication.

## 10. The historical Möbius assembly is not the exact key-table object

Eliminating `(x,y)` from the off-diagonal inverse formulas yields

`v_d(u)=((d-1)u+1)/(d+1-u)`.

But elimination without saturation introduces the point `(u,v)=(1,1)`: it satisfies the eliminated equation for every `d`, while the inverse pair formula is `0/0` there. The historical graph therefore differs from the exact pair-key image.

If `A_hist` denotes the historical graph amplitude and `A_key` the correct key-table amplitude, then the finite computations at `N=53,199` verify the exact correction pattern

- `d!=0`: `A_hist(tau,d)=A_key(tau,d)+1` for every twist pair;
- `d=0`, first twist trivial: `A_hist=A_key=N-2`;
- `d=0`, first twist nontrivial: `A_hist=-1` while `A_key=N-2`.

Equivalently, in Fourier space the difference is `(N-1,-1,...,-1)` when the first twist is trivial and `(0,-N,...,-N)` otherwise.

The old Möbius divisor/perfect-power analysis remains useful as an audit of why the historical proof failed, but it is no longer the active M1 theorem object.

## 11. Off-off curve family and the new analytic frontier

For fixed `(h1,h2) in H^2`, the off-off contribution is governed by

`d(u,v)+d(h1/u,h2/v)=t`.

After clearing denominators this is a plane cubic. Viewed as a quadratic in `v`, its branch quartic has discriminant proportional to

`h1^2 h2^2 (h1-h2)^2 ((h1-1)(h2-1)+t(h1-h2))^4 Q(h1,h2,t)`,

where `Q` is quartic in `t`.

At `t=0`, `Q=16(h1-1)^2(h2-1)^2`, so for `h1,h2!=1` and `h1!=h2` the generic zero-difference cubic is smooth. For general `t`, the visible exceptional strata are therefore finite and explicit: `h1=h2`, the boundary value `t=d(h1,h2)`, and at most four roots of `Q`, together with the separate `h1=1` or `h2=1` cases.

The remaining hard step is an `L^2` cancellation theorem for the sum of these curve-count fluctuations over `H^2`. Candidate machinery includes Deligne/Katz trace-function correlation results, but the required sheaf, conductor, monodromy and exceptional-isomorphism checks have not yet been proved for this family.

## 12. Current theorem target

The active M1 target is now:

1. prove the mean asymptotic for `Sigma_4` from the exact `B(0)` geometry;
2. prove
   `Var_(t!=0) B(t) = O(K^2 N)`
   in an explicit `(N,K)` regime;
3. conclude
   `std Sigma_4 = O(NK)` and relative fluctuation `O(K/N)`;
4. only then feed this concentration estimate into the next spectral/local-law step.

No statement in this section is being promoted to “general BGS proved”.
