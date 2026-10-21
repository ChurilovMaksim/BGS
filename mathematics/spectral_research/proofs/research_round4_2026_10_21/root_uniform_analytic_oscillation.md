> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/root_uniform_analytic_oscillation.md`. Embedded SHA256: `5eaae7946e30df2507a870535ec46c2dbc2bce07cc96c8b85366772cab590d31`.
> [Thematic guide](../../topics/classical_trace.md).

# Uniform oscillation of translated analytic phase differences

21 October 2026. Root-owned proof, independent of the WKB construction.

This note proves an auxiliary estimate directly. It does not prove the original
spectral-statistics limit. Its intended application must separately establish
that the exact prescribed kick has the asserted oscillatory Weyl symbol with a
uniform error. No such symbol representation is assumed to follow merely from
classical mixing.

## 1. Statement

Let S be a fixed real analytic real-valued function on the two-dimensional
unit torus. Assume that both Fourier coefficients

$$
\widehat S(1,0)\ne0,\qquad \widehat S(0,1)\ne0.
\tag{1.1}
$$

For a torus translation z let eta(z) be its Euclidean distance to the integer
lattice, using representatives in [-1/2,1/2]^2. For each z let a_z be a C^1
amplitude on the torus, not necessarily continuous as a function of z, with

$$
\sup_z\|a_z\|_{C^1}\le A.
$$

There are an integer M>=1 and a finite constant C, depending only on S and on
the choice of equivalent C^1 norm, such that for every lambda>=1 and every z,

$$
\boxed{
\left|\int_{\mathbb T^2}a_z(x)
 e^{i\lambda(S(x+z)-S(x))}\,dx\right|
\le C A(1+\lambda\eta(z))^{-1/M}.
}
\tag{1.2}
$$

No assertion that M is a small or numerically useful integer is made. It is a
single finite integer for this fixed S, uniformly over all translations and all
lambda. Put epsilon=1/M, so 0<epsilon<=1.

For every integer d>=1, its grid consequence is

$$
\boxed{
\frac1{d^2}\sum_{\substack{z\in(d^{-1}\mathbb Z/\mathbb Z)^2\\z\ne0}}
\left|\int a_z(x)e^{i\lambda(S(x+z)-S(x))}\,dx\right|
\le C' A\lambda^{-\epsilon}.
}
\tag{1.3}
$$

The constant C' is independent of d. Thus it is unnecessary to replace every
nonzero distance by 1/d; averaging the integrable singularity eta^-epsilon is
stronger.

## 2. A compact family including zero-translation directions

Write z=r omega, where |omega|=1, r=eta(z), and take the compact parameter set

$$
\mathcal K=\{(r,\omega):0\le r\le1/\sqrt2,
\ |\omega|=1,\ |r\omega_j|\le1/2\ (j=1,2)\}.
$$

Define

$$
F_{r,\omega}(x)=\int_0^1\omega\cdot\nabla S(x+s r\omega)\,ds.
\tag{2.1}
$$

For r>0 this equals [S(x+r omega)-S(x)]/r. At r=0 it equals
omega dot grad S. This family is continuous into every C^j space, and each
member is real analytic in x. It is mean zero.

Let c_0=min(|S_hat(1,0)|,|S_hat(0,1)|)>0. On [-1/2,1/2],

$$
|e^{2\pi iu}-1|=2|\sin\pi u|\ge4|u|.
$$

Therefore, for r>0,

$$
\max_{j=1,2}|\widehat F_{r,\omega}(e_j)|
\ge4c_0\max_j|\omega_j|\ge2\sqrt2\,c_0.
\tag{2.2}
$$

The same lower bound follows at r=0 by continuity (the exact factor there is
2 pi). In particular, no member of this compact family is constant.

For every parameter kappa in K and every x, at least one derivative of positive
order of F_kappa at x is nonzero. Otherwise its real analytic power series at
x would be constant, and analytic continuation on the connected torus would
make F_kappa constant everywhere, contradicting (2.2).

The open sets on which a specified positive-order derivative has magnitude
greater than 1/n, with n a positive integer, cover the compact product
K x T^2. A finite subcover yields finite M>=1 and c>0 such that

$$
\max_{1\le|\alpha|\le M}|\partial^\alpha F_\kappa(x)|\ge c
\qquad(\kappa\in\mathcal K,\ x\in\mathbb T^2).
\tag{2.3}
$$

This is an existence proof of a uniform finite order, rather than an assumption
of a uniform order inferred from individual nonconstancy.

## 3. Reduction to finitely many directions and patches

For a fixed order m the polynomial v -> D_v^m F(x) is homogeneous of degree
m in the two components of v. Its coefficients are the order-m partial
derivatives times binomial factors. Evaluating it at the m+1 distinct unit
directions proportional to (1,j), 0<=j<=m, gives an invertible Vandermonde
system. Consequently there is a constant B_m such that

$$
\max_{|\alpha|=m}|\partial^\alpha F(x)|
\le B_m\max_{0\le j\le m}|D_{v_{m,j}}^mF(x)|.
\tag{3.1}
$$

Combining the finitely many systems, (2.3), and continuity, one can cover
K x T^2 by finitely many product neighborhoods O_j x B_j, where B_j is a small
coordinate ball, and on each neighborhood one selected directional derivative
of order m_j in {1,...,M} has magnitude at least a fixed c'>0.

Here are details of localization that ensure uniform amplitude bounds. Refine
the finite cover by product neighborhoods with closures inside the original
ones. Choose nonnegative continuous parameter cutoffs supported in O_j, and
nonnegative smooth coordinate cutoffs supported inside B_j, positive on the
smaller neighborhoods. The sum of their products is bounded below on the
compact product. Dividing each product by this sum gives a partition of unity
whose derivatives in x of any fixed order are uniformly bounded. Smoothness in
the parameter is not needed. For each parameter, multiplying a_z by this
partition leaves a bounded number of amplitudes with uniformly bounded C^1
norms, each supported strictly inside its coordinate ball.

In coordinates along the selected unit direction and its perpendicular, the
intersection with a ball is an interval. Each localized integral is thus an
integral of one-dimensional oscillatory integrals along those intervals.
The interval lengths and transverse ranges are uniformly bounded. The phase
derivative of order m_j is bounded below by c' on the entire interval, and all
phase derivatives of each fixed order are uniformly bounded by compactness.

## 4. The one-dimensional estimate, proved here

Suppose phi is real on an interval and |phi^(m)|>=c'>0. For m>=2, set
g=phi' and r=m-1. For eta>0, the sublevel estimate is

$$
|\{x:|g(x)|\le\eta\}|\le C_r(\eta/c')^{1/r}.
\tag{4.1}
$$

To verify it, let the measure of that set be L>0. Choose r+1 ordered points of
the set at successively separated measure quantiles; by small approximation if
necessary their neighboring distances can be made at least L/[2(r+2)]. The
mean-value theorem for divided differences, obtained by applying Rolle's
theorem r times after subtracting the interpolation polynomial, says that their
order-r divided difference is g^(r)(xi)/r! for some intermediate xi. Its
absolute value is at least c'/r!. On the other hand the interpolation formula
and |g|<=eta at all selected points bound that divided difference by

$$
\frac{\eta}{\delta^r}\sum_{j=0}^r\frac1{j!(r-j)!}
=\frac{2^r\eta}{r!\delta^r},
\qquad\delta=L/[2(r+2)].
$$

This gives (4.1), and passing to the approximate quantile limit removes any
endpoint selection issue.

Rolle's theorem also shows that g' has at most r-1 distinct zeros, because
g^(r) never vanishes. Hence the complement of the sublevel set can be split
into at most 2r intervals on each of which g is monotone, of one sign, and has
absolute value greater than eta. Integration by parts on these intervals gives
for a C^1 amplitude A_0

$$
\left|\int_{|g|>\eta}A_0 e^{i\nu\phi}\right|
\le\frac{C_r}{\nu\eta}
\left(\|A_0\|_\infty+\|A_0'\|_1\right).
\tag{4.2}
$$

In this calculation the term involving g'/g^2 has integral at most a constant
times 1/eta on each monotonicity interval. Boundary terms obey the same bound.
On the sublevel set use (4.1) and the supremum norm of the amplitude. Choosing
eta=(c')^(1/m) nu^(-(m-1)/m) yields

$$
\left|\int A_0 e^{i\nu\phi}\right|
\le C_m(c'\nu)^{-1/m}
\left(\|A_0\|_\infty+\|A_0'\|_1\right).
\tag{4.3}
$$

For m=1, direct integration by parts works since |phi'|>=c'; its term
containing phi'' is bounded using the fixed upper bound on that derivative and
the interval length. This proves a bound C nu^-1 with the same amplitude
norm. No monotonicity hypothesis on phi' is needed in that case.

Apply these estimates to the finite localization in Section 3, with
nu=lambda eta(z) and F as phase. If nu>=1, then nu^(-1/m_j)<=nu^(-1/M).
Integrating over the bounded transverse range and summing the finite
partition proves (1.2). If nu<1, the absolute integral bound proves the same
statement after increasing C. This includes z=0.

## 5. Uniform grid summation

Represent each nonzero grid translation by j/d with centered integer
coordinates. On a shell max(|j_1|,|j_2|)=m there are at most C m points, and
eta(j/d)>=m/d. Since epsilon=1/M<=1<2,

$$
\begin{aligned}
\frac1{d^2}\sum_{z\ne0}\eta(z)^{-\epsilon}
&\le C d^{\epsilon-2}\sum_{1\le m\le d/2+1}m^{1-\epsilon}\\
&\le C_\epsilon.
\end{aligned}
\tag{5.1}
$$

The case d=1 has an empty sum. Bound (1.2) is at most
C A lambda^-epsilon eta^-epsilon for nonzero z. Equation (5.1) proves (1.3).

## 6. Precise prospective consequence for the kick

If, and only if a separate argument proves uniformly in all z and N that

$$
\frac1N\operatorname{Tr}(E_N^*T_zE_NT_z^*)
=\int a_{z,N}(x)e^{i(2\pi N)(S(x+z)-S(x))}\,dx+O(N^{-1}),
$$

with S satisfying (1.1) and uniformly bounded C^1 amplitudes, then averaging
over the character subgroup and retaining the exact identity contribution
gives

$$
\frac1N\left\|\sum_\chi P_\chi E_NP_\chi\right\|_{\rm HS}^2
\le d^{-2}+C N^{-\epsilon}.
$$

This last display is a consequence to be used only after the independent
exact-quantization and uniform-remainder argument is supplied. The analytic
oscillation estimate (1.2) and its grid average (1.3) are proved independently
above.
