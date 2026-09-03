# Current mathematical core

## 1. Character convention

Let `N` be an odd prime and let `H=<a>` be a subgroup of `F_N^*` of order `K`.  Let `S=H^perp` be the annihilator subgroup of multiplicative characters, with `m=|S|=(N-1)/K`.

For multiplicative characters `chi, psi` and nonzero additive frequency `q`, use

`J(chi,psi;q) = sum_{x != 0,1} conjugate(chi(x)) psi(x-1) e_N(qx)`.

The active Python kernels implement this convention explicitly.

## 2. Exact even-moment factorization

For an integer `s>=1`, define

`A_{2s,S}(q) = sum_{chi,psi in S} |J(chi,psi;q)|^(2s)`.

Expand `J^s conjugate(J)^s` with variables `x_1,...,x_s` and `y_1,...,y_s`.  The character factor is

`chi(prod y_r / prod x_r) * psi(prod(x_r-1) / prod(y_r-1))`,

up to inversion of the first quotient, which is immaterial because `H` is a subgroup.  Orthogonality on the annihilator gives

`sum_{chi in S} chi(z) = m` if `z in H`, and `0` otherwise.

Applying this once for `chi` and once for `psi` yields the exact identity

`A_{2s,S}(q) = m^2 Sigma_{2s}(q)`,

where `Sigma_{2s}` is the additive exponential sum over tuples satisfying the two product constraints

`prod x_r / prod y_r in H`,
`prod(x_r-1) / prod(y_r-1) in H`.

This is an algebraic reduction, not an asymptotic estimate.  Its difficulty grows with the dimension of the constraint variety.  The `s=1` reduction and the `s=2` (`k=4`) factorization are independently checked in the active verification suite; the fourth-moment case is also reproduced in C++ at `N=23,53`.

## 3. Exact k=2 geometry

At `s=1`, the off-diagonal constraint set admits the explicit `(u,v)` parametrization used by the verified `k=2` script.  The finite counts at the audited designs agree with `(K-1)(K-2)`.

## 4. k=4 key-table geometry

At `s=2`, the pair key

`(x,y) -> (x/y, (x-1)/(y-1))`

reduces the four-variable constraint to an H-coupled pair-pair count.  At `N=53,K=13`, the independently reproduced variety size is `423879`.  This gives a useful exact finite model for the fluctuation energy, but the asymptotic cross-correlation estimate remains open.

## 5. Möbius fibers and the M1 obstruction

The historical fiber map is

`v_d(u) = ((d-1)u+1)/(d+1-u)`.

Its projective matrix has determinant `d^2`, so the map itself degenerates at `d=0`.  There `v_0(u)=1` away from the removable singularity.  Therefore semi-trivial twists have an `N-2` contribution on that fiber and cannot satisfy a uniform `O(sqrt(N))` bound without an exceptional-fiber decomposition.

Furthermore, if `F_tau=A_tau*A_tau`, then

`||sum_tau F_tau||_2^2 = sum_tau ||F_tau||_2^2 + sum_{tau != sigma} <F_tau,F_sigma>`.

The second term is numerically nonzero and is part of the theorem to be controlled.

## 6. Character order and the perfect-power condition

Write `N-1=K m`, choose a primitive root `g`, and write `a=g^ell` with `ord(a)=K`. Then `gcd(ell,N-1)=m`, and `chi_k(a)=1` is equivalent to `K | k`. Thus the annihilator group is `S={chi_(Kj): j mod m}` and its natural generator `rho=chi_K` has order `m`.

For a twist pair `(rho^r,rho^s)`, the generic Möbius-fiber integrand can be written as `rho(u^r v_d(u)^s)`. On a generic fiber the divisor has coefficients `r,-r,s,-s` at four distinct points. Divisibility of all valuations by `m` therefore forces `r=s=0`. The special fibers `d=1` and `d=-1` still force the trivial pair; `d=0` collapses `v_d` to `1` and leaves exactly the exceptional family `r=0`, `s` arbitrary. Details are in `research/notes/m1_mobius_fibers.md`.

This repairs the old group-order confusion (`K` versus `m`) and isolates the exceptional fiber, but the cross-Gram cancellation estimate remains open.

## 7. What remains

The current theorem-level frontier is not another finite identity.  It is a uniform analytic estimate for the full cross-Gram assembly, with exceptional fibers separated exactly and generic finite-field bounds applied under verified hypotheses.
