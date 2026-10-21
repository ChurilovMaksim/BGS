> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_center_phase_c17_bound.md`. Embedded SHA256: `992f35db1916f680083fe304caa3001bc71720e2a864f28ea3513f080b5340c5`.
> [Thematic guide](../../topics/classical_trace.md).

# Explicit C17 closeness of the exact center phase

21 October 2026. Supplement to `counter_one_step_pinching_hs.md`, frozen SHA-256 `a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`.

This note supplies a numerical derivative bound that was not needed for the qualitative finite-type argument in the frozen source. It does not alter that source. A separate coefficient-extractor calculation may use this bound to obtain a specified finite type and a numerical power exponent; that additional extractor calculation is not assumed here.

Use exactly the notation of Sections 1--2 of the source: `rho=10^(-3)`, `t_0=10^(-10)`, `t=tau/(2pi)`, and `S_t` is the analytic center action constructed from the exact Hamilton--Jacobi characteristics. Then

$$
\boxed{
\sum_{|\alpha|\le17}
\left\|\partial^\alpha\left(\frac{S_t}{t}-a\right)\right\|_\infty
<\frac1{100000}<\frac1{4000}.
}
\tag{1}
$$

The supremum in (1) is on the real two-dimensional torus, and the sum runs over all two-dimensional multiindices of total order at most 17. Thus this bound also holds for the maximum-derivative convention for the `C^17` norm.

## Proof

The source bounds the complex Hamiltonian flow on the tube of width `2rho`, with initial points in the tube of width `rho`, by

$$
\|\Phi_s-y\|_\infty\le200s,
\qquad
\left\|D\left(\frac{\Phi_s-y}{2}\right)\right\|
\le10^4s\le10^{-6},\qquad 0\le s\le t_0.
$$

The fixed-point inverse of the midpoint map therefore works on the larger strip of width `3rho/4` as well: the ball of radius `200s` about such an endpoint lies inside the strip of width `rho`, since

$$
3\rho/4+200t_0=0.00075002<0.001=\rho.
$$

The contraction factor and all flow bounds are unchanged. Consequently `S_s` is holomorphic on this common strip and there

$$
\|\nabla S_s\|_\infty\le200s.
$$

The exact Hamilton--Jacobi equation is

$$
\partial_sS_s(x)=a(x-J\nabla S_s(x)/2).
$$

For each complex endpoint in the strip of width `3rho/4`, the argument on its right differs by at most `100s` in each coordinate. The whole segment connecting these two points lies in the strip of width `2rho`, where the source's direct Fourier estimate gives each partial derivative of `a` magnitude at most 200. The complex mean-value integral thus gives

$$
|\partial_s S_s(x)-a(x)|\le4\cdot10^4s,
\qquad
\left|\frac{S_t(x)}t-a(x)\right|\le2\cdot10^4t.
\tag{2}
$$

Apply Cauchy's estimate on a polydisk of radius `3rho/4` about a real point, taking a limiting sequence of smaller radii if necessary. For every multiindex `alpha`,

$$
\left|\partial^\alpha\left(S_t/t-a\right)\right|
\le\alpha!\left(\frac4{3\rho}\right)^{|\alpha|}
2\cdot10^4t.
\tag{3}
$$

There are `(18*19)/2=171` two-dimensional multiindices of total order at most 17. Each has `alpha!<=17!`; also `4/(3rho)=4000/3>1` and `t=10^(-80)/(2pi)<10^(-80)`. Summing (3) therefore bounds the left side of (1) by

$$
171\cdot17!\left(\frac{4000}{3}\right)^{17}
20000\cdot10^{-80}
=\frac{75942437322752}{46927928924560546875}
<\frac1{100000}.
\tag{4}
$$

The final strict rational inequality follows by cross-multiplication. This proves (1) for the exact phase, with the original fixed `tau`.

