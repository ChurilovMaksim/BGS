> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_transcendental_eigenvalue_ratios.md`. Embedded SHA256: `334b97d4659d2f29ed22c7615252cdb88e7d2d4c99e1a896083cea993475e0a5`.
> [Thematic guide](../../topics/algebra.md).

# Transcendental ratios and simplicity of every power

Research continuation, 20 October 2026. The parameter and matrices are
exactly those of the question; no averaging is introduced.

## 1. Result

**Theorem.** Let N>=3 be odd with 7 not dividing N, let z be any
nonzero algebraic complex number, and let lambda_i, lambda_j be two
distinct eigenvalues of U_N(z)=exp(izNA_N)M_N. Then

$$
\boxed{\lambda_i/\lambda_j\notin\overline{\mathbb Q}.}
\tag{1.1}
$$

In particular U_N(z)^m has simple spectrum for every nonzero integer
m. For the actual real z=tau=10^(-80), no two eigenangles differ by a
rational number modulo 1. More strongly, their exponentiated difference
is transcendental.

This is an exact nonresonance theorem. It gives no lower bound on how
close a ratio may be to an algebraic number or a root of unity and no
bound on unfolded spectral gaps. H_diag remains unproved.

## 2. The algebraic resultant

The input theorem proves simplicity of A_N and nonvanishing of every
principal minor of M_N in its eigenbasis. Order the eigenvalues as
a_1>...>a_N, and write b_k for the leading k-by-k principal minor in
that basis, with b_0=1. All b_k are nonzero. Its Rouché argument gives
the sharper explicit asymptotics for positive real t:

$$
\lambda_k(e^{tA_N}M_N)
 =e^{ta_k}\left(\frac{b_k}{b_{k-1}}+o(1)\right),
\qquad 1\le k\le N.
\tag{2.1}
$$

For completeness, on setting X=e^(ta_k)Y in the characteristic
polynomial, the unique two largest exponential terms have indices k-1
and k. Their limiting polynomial is a nonzero constant times
Y^(N-k)(b_(k-1)Y-b_k). Rouché's theorem on every sufficiently small
circle about b_k/b_(k-1) first gives one simple root there and then,
by arbitrarily shrinking the circle, gives (2.1).

Fix c in the algebraic numbers with c!=0,1, and define

$$
P_z(X)=\det(XI-U_N(z)),\qquad
R_c(z)=\operatorname{Res}_X\left(P_z(X),c^N P_z(X/c)\right).
\tag{2.2}
$$

The second polynomial is monic with roots c times the eigenvalues of
U_N(z). Since U_N(z) is invertible, R_c(z) vanishes exactly when two
of its eigenvalues satisfy lambda_i=c lambda_j. The case i=j is
impossible because c!=1.

The entries of U_N(z), and hence all coefficients of both polynomials
in (2.2), are finite exponential sums with algebraic coefficients and
algebraic frequencies. The resultant is a polynomial in those
coefficients. Thus R_c is also an algebraic exponential polynomial.

It is not identically zero. Indeed, set z=t/(iN)=-it/N. Equation (2.1)
shows, for i!=j,

$$
\left|\frac{\lambda_i(e^{tA_N}M_N)}
                {\lambda_j(e^{tA_N}M_N)}\right|
 \longrightarrow
 \begin{cases}
 +\infty,&a_i>a_j,\\
 0,&a_i<a_j.
 \end{cases}
\tag{2.3}
$$

Since c is fixed and nonzero, none of these finitely many ratios
equals c for all sufficiently large real t. Therefore R_c is nonzero
at those parameters.

Collect equal frequencies in R_c. The Lindemann--Weierstrass theorem
for distinct algebraic exponents implies that this nonzero exponential
polynomial cannot vanish at a nonzero algebraic z: multiplication of
the distinct algebraic frequencies by that z preserves distinctness
and algebraicity. All hypotheses of the theorem are thus satisfied.
The exact published statement used is Theorem 3.2 of S. A. Popescu,
*A Simple and Self-contained Proof for the Lindemann--Weierstrass
Theorem*,
[DOI 10.1007/978-3-031-51959-8_16](https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16),
also available in the author's
[manuscript, Theorem 3.2](https://arxiv.org/pdf/2306.14352).

This excludes every algebraic c!=0,1 individually, which is exactly
the universal assertion (1.1). The value c=1 is already excluded by
the input simple-spectrum theorem.

## 3. Powers and eigenangles

If U_N(z)^m had a repeated eigenvalue for m!=0, diagonalizability of
the simple-spectrum U_N(z) would give distinct lambda_i, lambda_j
with (lambda_i/lambda_j)^m=1. Their ratio would be an algebraic root
of unity, contradicting (1.1). This works for negative m because all
eigenvalues are nonzero.

For real z, U_N(z) is unitary and lambda_i/lambda_j is the exponential
of 2pi i times the eigenangle difference. A rational difference would
again make that ratio a root of unity. No probabilistic or limiting
argument is involved.

## 4. Frozen input

| File | SHA-256 |
|---|---|
| `arithmetic_padic_jacobi_simplicity.md` | `f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df` |

The input is used only for its explicitly proved nonzero principal
minors, simple spectrum, and large positive real-t Rouché argument.
The new ingredient here is the resultant, which transfers all fixed
algebraic ratio exclusions from complex time to the original exact
algebraic parameter. No claim is made in dimensions divisible by 7.
