> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_explicit_symbol_finite_type16.md`. Embedded SHA256: `1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Explicit finite type 16 for every translated center-phase difference

Date: 21 October 2026.

This is a new, self-contained coefficient-extractor lemma and its application to the exact center phase. It supplies an explicit exponent for the already independently audited one-step HS theorem. It does not change that theorem's frozen source or replace its exact phase by a first-order approximation.

## 1. Exact claim and dependencies

Let `a` be the ordinary real-half symbol of the prescribed `A_N`:

$$
\begin{aligned}
a(q,p)={}&\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10\\
&+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
\end{aligned}
$$

For a nonzero torus translation `z`, let `delta=dist(z,Z^2)`, choose a centered lift in `[-1/2,1/2]^2`, and define

$$
F_z^A(x)=\frac{A(x+z)-A(x)}\delta.
$$

Use the maximum convention

$$
\|A\|_{C^{17},\max}
=\max_{|\alpha|\le17}\|\partial^\alpha A\|_\infty.
$$

**Lemma.** If a real function `A` on the torus satisfies

$$
\|A-a\|_{C^{17},\max}\le1/4000,
\tag{1.1}
$$

then, for every nonzero `z` and every point `x`,

$$
\boxed{\max_{1\le|\alpha|\le16}
|\partial^\alpha F_z^A(x)|>1/2000.}
\tag{1.2}
$$

The normalized family including zero-translation directional limits has the same positive lower bound with a non-strict inequality. No analyticity is needed for the perturbative lemma; `C^17` regularity suffices.

The exact center phase `S_t`, for `t=10^-80/(2pi)`, was constructed in:

- `counter_one_step_pinching_hs.md`, SHA-256 `a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`;
- independently audited in `audit_one_step_pinching_hs.md`, SHA-256 `7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`.

Section 5 below verifies (1.1) for `A=S_t/t` by an explicit rational bound. The independent analytic oscillation proof in `root_uniform_analytic_oscillation.md`, SHA-256 `5eaae7946e30df2507a870535ec46c2dbc2bce07cc96c8b85366772cab590d31`, then applies with the concrete order `16`; its finite-type-to-oscillation step uses only the derivative lower bound established here.

## 2. Two exact differential coefficient extractors

Set

$$
D_q=(2\pi i)^{-1}\partial_q,\qquad
D_p=(2\pi i)^{-1}\partial_p,
$$

so that they act on the Fourier mode `(k,l)` by multiplication by `k,l`.

The pure-`q` support of `a` is

$$
\mathcal K=\{-9,-8,-7,-6,-5,-2,-1,1,2,5,6,7,8,9\}.
$$

Its mixed rows have `l=±1` and `q` support `0,±1,±6,±7,±8`. The half-period shift changes their coefficients but not this support. The two required coefficient magnitudes are

$$
|a_{1,0}|=|1/20-i/200|\ge1/20,
\qquad |a_{0,1}|=|(-3-4i)/1000|=1/200.
\tag{2.1}
$$

Define the one-variable polynomial

$$
P_1(s)=s\prod_{k\in\mathcal K\setminus\{1\}}
\frac{s-k}{1-k}
$$

and the differential operator

$$
\mathcal D_1=(1-D_p^2)P_1(D_q).
\tag{2.2}
$$

The first factor kills both mixed rows. The polynomial `P_1` is one at `s=1`, zero at every other pure frequency, and zero at `s=0`. Therefore

$$
\mathcal D_1a=a_{1,0}e^{2\pi iq}.
\tag{2.3}
$$

It has total derivative order at most `16`: `P_1` has degree `14`, and the `p` factor has degree two. Every nonzero differential monomial has positive order because `P_1` contains a factor `s`.

For the second mode define

$$
\mathcal D_2=\frac{D_p(D_p+1)}2
\prod_{k\in\{1,6,7,8\}}\left(1-\frac{D_q^2}{k^2}\right).
\tag{2.4}
$$

The `p` factor is one at `l=1` and zero at `l=0,-1`. The `q` factor kills every remaining nonzero mixed frequency and is one at `k=0`. Thus

$$
\mathcal D_2a=a_{0,1}e^{2\pi ip}.
\tag{2.5}
$$

Its total order is at most ten, and again every monomial has positive order.

These identities are polynomial identities on the exact finite Fourier support. Translation and differentiation commute, so both remain exact coefficient extractors for every normalized difference `F_z^a`.

## 3. The coefficient-norm budget is 27, not 54

For a polynomial, let its coefficient one-norm be the sum of the absolute values of its coefficients. Submultiplicativity gives

$$
\|P_1\|_{\ell^1}
\le\prod_{k\in\mathcal K\setminus\{1\}}
\frac{1+|k|}{|1-k|}.
$$

Every negative frequency contributes the factor one. The positive frequencies other than one give

$$
3\cdot\frac64\cdot\frac75\cdot\frac86\cdot\frac97\cdot\frac{10}8
=\frac{27}{2}.
$$

The extra factor `1-D_p^2` has coefficient one-norm two. Hence the complete bivariate differential polynomial in (2.2) has coefficient one-norm at most `27`.

For (2.4), the `p` factor has coefficient one-norm one, and the other factors give

$$
\|\mathcal D_2\|_{\ell^1(D_q,D_p)}
\le2\cdot\frac{37}{36}\cdot\frac{50}{49}\cdot\frac{65}{64}
=\frac{60125}{28224}<3.
\tag{3.1}
$$

Since `(2pi)^(-j)<=1` for every positive order `j`, conversion from the formal variables `D_q,D_p` to ordinary partial derivatives does not enlarge either one-norm. If

$$
J_{16}(F;x)=\max_{1\le|\alpha|\le16}|\partial^\alpha F(x)|,
$$

then

$$
|\mathcal D_1F(x)|\le27J_{16}(F;x),\qquad
|\mathcal D_2F(x)|\le3J_{16}(F;x).
\tag{3.2}
$$

As a finite exact arithmetic check, expanding `P_1` with rational coefficients gives its actual one-norm `6409325/3048192`; the full operator norm in formal variables is `6409325/1524096`, below the safe bound `27`. The proof uses the product upper bound, not an incorrect equality of that upper bound with the expanded coefficient norm.

## 4. Uniform nondegeneracy and its `C^17` stability

On the centered interval,

$$
|e^{2\pi iu}-1|=2|\sin\pi u|\ge4|u|.
$$

At least one coordinate of the centered lift of `z` has absolute value at least `delta/sqrt(2)`. If it is the `q` coordinate, (2.1), (2.3), and (3.2) imply

$$
J_{16}(F_z^a;x)
\ge\frac1{27}\frac1{20}\frac{4|z_q|}{\delta}
\ge\frac{\sqrt2}{270}.
$$

If it is the `p` coordinate, (2.1), (2.5), and (3.2) imply

$$
J_{16}(F_z^a;x)
\ge\frac13\frac1{200}\frac{4|z_p|}{\delta}
\ge\frac{\sqrt2}{300}.
$$

These estimates hold at every point: the isolated Fourier exponential has modulus one. In particular,

$$
J_{16}(F_z^a;x)\ge\frac{\sqrt2}{300}>\frac1{1000}.
\tag{4.1}
$$

Now write `A=a+R`. For every multiindex of order at most sixteen,

$$
\partial^\alpha F_z^R(x)
=\int_0^1\frac z\delta\cdot
\nabla\partial^\alpha R(x+uz)\,du.
$$

The Euclidean norm of `z/delta` is one; each of the two gradient components is bounded by `||R||_(C17,max)`. Therefore

$$
|\partial^\alpha F_z^R(x)|
\le\sqrt2\|R\|_{C^{17},\max}\le\frac{\sqrt2}{4000}.
$$

Subtracting this from (4.1), even using its weaker `1/1000` lower bound, gives

$$
J_{16}(F_z^A;x)
>\frac1{1000}-\frac{\sqrt2}{4000}
>\frac1{2000},
$$

because `sqrt(2)<2`. This proves the lemma. The normalized integral representation extends the family continuously, in every needed derivative, to `z=r omega` with `r=0`; taking that limit proves the corresponding directional-derivative bound.

## 5. Certified `C^17` closeness for the exact center action

The phase construction supplies, on the complex tube of width `rho/2=1/2000`, the bounds `||grad S_s||_infty<=200s` and the exact Hamilton–Jacobi equation

$$
\partial_sS_s(x)=a(x-J\nabla S_s(x)/2).
$$

The tube assertion follows directly from the same analytic midpoint inverse used to construct the action. For such an endpoint, the shifted argument differs by at most `100s` in each coordinate and stays inside the width-`2rho` tube. Each partial derivative of `a` has magnitude at most 200 there. The complex mean-value integral, followed by time integration at a fixed endpoint, consequently proves

$$
\left\|S_t/t-a\right\|_{\text{complex strip }\rho/2}
\le2\cdot10^4t.
\tag{5.1}
$$

Take a complex polydisk of radius `1/2500` about a real point; it is strictly inside this strip. Multivariable Cauchy gives, for every `|alpha|<=17`,

$$
\|\partial^\alpha(S_t/t-a)\|_\infty
\le2\cdot10^4t\,\alpha!\,2500^{|\alpha|}
\le2\cdot10^4t\,17!\,2500^{17}.
$$

The exact fixed constant satisfies `t=10^-80/(2pi)<10^-80/6`. Therefore the maximum `C^17` norm is strictly below the explicit rational number

$$
\frac{20000\cdot17!\cdot2500^{17}}{6\cdot10^{80}}
=\frac{28945917}{419430400000}
<\frac1{4000}.
\tag{5.2}
$$

The last comparison is an integer comparison: `28945917*4000=115783668000<419430400000`. Thus the perturbative hypothesis is certified for the original exact `tau` without selecting an unspecified sufficiently small time.

The separate frozen supplement `counter_center_phase_c17_bound.md`, SHA-256 `992f35db1916f680083fe304caa3001bc71720e2a864f28ea3513f080b5340c5`, proves an even stronger sum-of-derivatives bound by using the larger width `3rho/4`. Its midpoint margin and Cauchy calculation were also independently checked: its displayed bound is exactly `75942437322752/46927928924560546875<1/100000`. The simpler maximum-norm bound (5.2) already suffices for the present lemma.

## 6. Explicit oscillatory and pinching exponents

Apply the lemma to `A=S_t/t`. The normalized translate difference for `S_t` has a positive derivative of order at most sixteen, with lower bound at least `t/2000`. This constant is fixed and independent of `N`, `d`, the translation, and the point.

The directional reduction, finite localization, and one-dimensional argument in the raw oscillation proof now apply with `M=16`. In more detail, for each order `m<=16`, evaluating `D_v^mF` in the finitely many directions proportional to `(1,j)`, `0<=j<=m`, gives an invertible Vandermonde system for its mixed derivatives. The compact normalized family has finite derivative bounds and the positive jet bound above, so a finite set of localized intervals has one directional derivative of order at most sixteen bounded below. The divided-difference sublevel estimate and integration by parts give decay of order `nu^(-1/m)`, and hence the common decay `nu^(-1/16)`. The constants depend on the fixed phase, which is allowed.

Consequently, for uniformly `C^1`-bounded amplitudes,

$$
\left|\int a_z(x)e^{i\lambda(S_t(x+z)-S_t(x))}\,dx\right|
\le C\sup_z\|a_z\|_{C^1}
(1+\lambda\operatorname{dist}(z,0))^{-1/16}.
\tag{6.1}
$$

The normalized family at zero is included; the bound for small `lambda dist` follows from the absolute integral bound. The grid average of `dist^-1/16` is uniformly finite in dimension two by the elementary shell count. Combining (6.1) with the exact translation representation and the `O(N^-1)` matrix error already proved for the original kick gives

$$
\boxed{
\left|\sigma_{N,d}^2-d^{-2}\right|\le CN^{-1/16},
\qquad
\sigma_{N,d}\le d^{-1}+CN^{-1/32}.
}
\tag{6.2}
$$

This holds uniformly for all sufficiently large odd `N` and every positive `d` with `d^2|N`. It strengthens the unspecified fixed positive exponent in the frozen one-step theorem. The previously proved all-time correction bound `24W sigma/g` can use (6.2) directly, with the same divisor range and exact original matrices.

The use of `S_t/t` close to `a` certifies finite type only. The oscillatory integrals and the matrix comparison continue to use the exact action `S_t`; there is no replacement of `exp(iS_t/h)` by `exp(ita/h)` and no error proportional to an uncontrolled phase difference divided by `h`.

## 7. Status for independent checking

The coefficient identities, polynomial one-norm bounds, perturbation estimate, and rational `C^17` calculation are proved above. This new supplement should be independently checked before its explicit exponent is promoted in the root report. No claim about full pair universality, the higher factorial orders, or historical priority is made.
