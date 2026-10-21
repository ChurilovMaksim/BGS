> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_quantitative_trace_and_sectors.md`. Embedded SHA256: `0a174f5de9d070c31311f4fdfd4ebc58b15df0b6bfd86baf5d6f169a99b2ef6a`.
> [Thematic guide](../../topics/arithmetic.md).

# Quantitative trace decay and mixing of all fixed arithmetic sectors

## Status and target

This note concerns the exact family in the question, with the fixed value
`tau = 10^-80`. It strengthens the fixed-square-divisor overlap calculation in
`arithmetic_oldspace_escape.md` (the final input filename and hash are recorded
in the consolidated manifest). It does not prove spectral universality.

Two assertions are proved here. First, an analytic nonidentity classical map,
together with a fixed-time Egorov estimate for its quantum operator, gives a
power saving for the normalized quantum trace. This uses an elementary
sublevel estimate, not a stationary phase assertion. Second, for every fixed
odd integer `d >= 3`, the exact matrix `U_(d^2 m)` transfers asymptotically the
same mean mass between every pair of the `d^2` canonical arithmetic sectors.
The error is `O_d(N^(-c_d))` for some `c_d > 0`. The constants may depend on `d`
and on the fixed kick. There is no uniform assertion when `d` grows with `N`.

## 1. Elementary torus quantization estimates

For integer `v=(k,l)` use the usual midpoint Weyl operator

$$
W_N(k,l)=(-1)^{kl}T_N(l,k),\qquad
\operatorname{Op}_N(a)=\sum_{v\in\mathbb Z^2}\widehat a(v)W_N(v).
$$

This identity is for all integer indices before reducing them modulo `N`.
The operators `W_N` have norm one, are adjoint under `v -> -v`, and satisfy

$$
W_N(v)W_N(w)
=e^{\pi i\Omega(v,w)/N}W_N(v+w),
\qquad \Omega(v,w)=l k'-k l'.                                      \tag{1}
$$

Indeed, multiply the two shift-and-multiplication operators in coordinates.
The modular-half factor differs from the real-half factor by `(-1)^(kl)`
because `2^(-1)=(N+1)/2` for odd `N`.

Write

$$
|a|_s=\sum_v(1+|v|)^s|\widehat a(v)|.
$$

Termwise use of (1) and `|e^{it}-1| <= |t|` gives

$$
\begin{split}
\|\operatorname{Op}_N(a)\|&\le |a|_0,\\
\|\operatorname{Op}_N(a)\operatorname{Op}_N(b)
       -\operatorname{Op}_N(ab)\|&\le C N^{-1}|a|_1|b|_1,\\
\|[\operatorname{Op}_N(a),\operatorname{Op}_N(b)]\|
       &\le C N^{-1}|a|_1|b|_1.                                  \tag{2}
\end{split}
$$

We also need a Hilbert--Schmidt estimate that remains usable for varying
cutoffs:

$$
\left(N^{-1}\operatorname{Tr}
\operatorname{Op}_N(a)^*\operatorname{Op}_N(a)\right)^{1/2}
\le \|a\|_{L^2}+C N^{-1}|a|_2.                                    \tag{3}
$$

To prove it, note that `N^(-1)Tr W_N(v)^*W_N(w)` vanishes unless
`v-w in N Z^2`, and has modulus one otherwise. The terms `v=w` give
`||a||_2^2`. In every other term at least one of `|v|,|w|` is at least `N/2`.
The total absolute value of these terms is at most

$$
2\left(\sum_{|v|\ge N/2}|\widehat a(v)|\right)|a|_0
\le 8N^{-2}|a|_2^2.
$$

Taking a square root proves (3). Integration by parts in whichever coordinate
of a Fourier index has larger modulus gives

$$
|a|_1\le C\|a\|_{C^5},\qquad |a|_2\le C\|a\|_{C^6}.               \tag{4}
$$

These estimates follow from convergent sums of powers over `Z^2`; all constants
in (1)--(4) are independent of `N`.

## 2. An elementary analytic sublevel estimate

Let `v` be a nonzero, nonnegative, real analytic function on the connected
two-dimensional torus. There are constants `C`, `epsilon_0 > 0`, and a positive
integer `r` such that

$$
\operatorname{vol}\{v\le\epsilon\}\le C\epsilon^{1/r}
\quad(0<\epsilon<\epsilon_0).                                    \tag{5}
$$

Here is a proof, including the finite-order point. At each zero of `v`, some
derivative of finite order is nonzero. Otherwise its convergent Taylor series
would vanish in a neighborhood, and analytic continuation on the connected
torus would make `v` identically zero. A nonzero homogeneous derivative tensor
has a direction in which the corresponding directional derivative is nonzero.
On a sufficiently small rectangle, after a rotation of coordinates, that
derivative has modulus bounded below by a positive constant. Finitely many
such rectangles cover the compact zero set. Away from their union, `v` has a
positive minimum.

For completeness, on an interval on which `|f^(j)| >= c > 0`, the set
`{|f| <= epsilon}` has length at most `C_j(epsilon/c)^(1/j)`. If that set has
length `L`, choose `j+1` points in it with successive distances bounded below
by a fixed multiple of `L/(j+1)` using quantiles of its Lebesgue measure.
The formula for their divided difference bounds its modulus by
`C_j epsilon/L^j`. The repeated mean value theorem identifies the divided
difference with `f^(j)(xi)/j!`, giving the claimed bound. Approximation of the
quantiles from points of the measurable set handles endpoints and sets with
empty interior. Apply this one-dimensional estimate on each parallel line of
each rectangle and integrate in the other variable. Taking the largest of the
finitely many derivative orders proves (5).

No uniform bound on `r` is claimed for arbitrary analytic functions.

## 3. Quantitative trace lemma

**Lemma.** Let `F_N` be unitary. Suppose that a fixed real analytic torus
diffeomorphism `kappa`, different from the identity, satisfies

$$
F_N\operatorname{Op}_N(b)F_N^{-1}
=\operatorname{Op}_N(b\circ\kappa)+O_b(N^{-1})                      \tag{6}
$$

in operator norm for every fixed smooth `b`. Then some constants `C,c>0`
satisfy

$$
|\operatorname{Tr}F_N|/N\le C N^{-c}.                             \tag{7}
$$

It suffices in (6) to assume the estimate for the two fixed coordinate
characters `b_1(q,p)=e^(2 pi i q)` and `b_2(q,p)=e^(2 pi i p)`.

**Proof.** Define

$$
g_j=b_j-b_j\circ\kappa,\quad v=|g_1|^2+|g_2|^2,
\quad\mu_N(a)=N^{-1}\operatorname{Tr}(\operatorname{Op}_N(a)F_N).
$$

The function `v` is analytic and nonzero, and its zero set is exactly
`Fix kappa`. Cyclicity of the finite matrix trace, followed by (6) and (2),
gives, for every smooth, possibly `N`-dependent `a`,

$$
|\mu_N(a g_j)|\le C N^{-1}|a|_1.                                 \tag{8}
$$

In detail,
`Tr Op(a)Op(b_j)F_N - Tr Op(a)F_N Op(b_j)` equals
`Tr [Op(a),Op(b_j)]F_N`. Replace `F_N Op(b_j)` using (6), and replace each
product of two quantizations by the quantization of the product using (2).
The Egorov remainder only involves the fixed `b_j`; its multiplication by
`Op(a)` costs at most `|a|_0`. This proves (8) with no uniform-Egorov hypothesis
for the varying functions `a`.

Choose a fixed smooth scalar cutoff `chi` equal to one on `[0,1]`, equal to zero
on `[2,infinity)`, and between zero and one. For `0<delta<1` put

$$
\chi_\delta=\chi(v/\delta),\qquad
a_{j,\delta}=(1-\chi_\delta)\overline{g_j}/v.
$$

Extend the second formula by zero near `v=0`. Differentiation on the set
`v>=delta`, and (4), show

$$
|a_{j,\delta}|_1+|\chi_\delta|_2\le C\delta^{-6}.                  \tag{9}
$$

For derivatives of order at most five in the first expression, each derivative
can cost at most one further factor `delta^(-1)` in addition to the initial
division by `v`; derivatives of order at most six in the second expression
cost at most `delta^(-6)`. All derivatives of the fixed `g_j,v` are bounded.

Since `sum_j a_(j,delta)g_j=1-chi_delta`, equation (8) gives
`|mu_N(1-chi_delta)| <= C N^(-1)delta^(-6)`. Cauchy--Schwarz for the matrix
trace and (3) give

$$
|\mu_N(\chi_\delta)|
\le\|\chi_\delta\|_2+C N^{-1}|\chi_\delta|_2
\le C\delta^{\beta/2}+C N^{-1}\delta^{-6},\quad\beta=1/r,           \tag{10}
$$

where (5) was used on the support of `chi_delta`. Set
`delta=N^(-2/(12+beta))`. The two terms have the same power, and hence (7)
holds with

$$
c=\frac{\beta}{12+\beta}=\frac1{12r+1}>0.
\qquad\square                                                     \tag{11}
$$

## 4. Application to all arithmetic sectors

Fix an odd `d>=3`; let `N=d^2 m` with odd `m`. The operators

$$
G_N(a,b)=T_N(dm a,dm b),\qquad (a,b)\in (\mathbb Z/d\mathbb Z)^2=:G,
$$

form an ordinary unitary representation of the abelian group `G`. The Weyl
product has no residual phase here because its symplectic product is divisible
by `N`. Its trace is zero except at the identity. Consequently, for every
character `chi` of `G`,

$$
P_{\chi,N}=\frac1{d^2}\sum_{g\in G}\overline{\chi(g)}G_N(g)         \tag{12}
$$

is an orthogonal projector of rank `m`. These `d^2` projectors are mutually
orthogonal and sum to the identity. The trivial character gives the canonical
old subspace with embedding

$$
(J_d\varphi)(dy)=d^{-1/2}\varphi(y\bmod m),\qquad
(J_d\varphi)(x)=0\text{ if }d\nmid x.
$$

Set `E_N=exp(i tau N A_N)`. The fixed-time Egorov and nonidentity arguments
in the companion arithmetic note apply to every word

$$
F_{g,h,N}=G_N(g)E_N^*G_N(h)E_N.                                   \tag{13}
$$

For `(g,h)!=(0,0)` its analytic classical map is not the identity. To recall
the substantive hypotheses: the effective ordinary-Weyl symbol is

$$
a(q,p)=\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10
+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
$$

Its `(1,0)` and `(0,1)` Fourier coefficients are nonzero, so its Hamiltonian
vector field has no nontrivial translation symmetry. If the map in (13) were
the identity, conjugacy of two rational translations by the flow, whose lift
is isotopic to the identity, would force `h=-g`. This can be seen without a
rotation-number theorem: an equality of lifts
`Phi(z+h)=Phi(z)-g+n` can be iterated `d` times and compared with
`Phi(z+dh)=Phi(z)+dh`, giving `h+g=n in Z^2`.
It would then say that the time-`tau/(2 pi)` flow commutes with the translation.
For this finite Fourier vector field that implies the same symmetry of the
vector field: uniformly over translations, the difference of the translated
and original time-`t` flow equals `t(X-X_h)+O(t^2 ||X-X_h||_infinity)`.
The proof uses the variational equation and the finite Fourier bound on
`D(X-X_h)` relative to `||X-X_h||_infinity`; at the stated fixed time its error
constant times `|t|` is strictly less than one. The companion note supplies the
explicit generous constants. Finally, the fixed-time Egorov remainder follows
from (1), `|sin x-x|<=|x|^3/6`, and Duhamel, and is in fact `O_b(N^(-2))`.

There are only finitely many pairs `(g,h)` for fixed `d`. Apply (7) to the
nonidentity pairs and take the minimum of their finitely many positive
exponents. The identity pair contributes exactly `N`. Expanding (12) proves

$$
\boxed{\quad
\frac1m\|P_{\chi,N}E_NP_{\psi,N}\|_{\rm HS}^2
=\frac1{d^2}+O_d(N^{-c_d})\quad}                                  \tag{14}
$$

simultaneously for every pair of characters `chi,psi` and all odd `m` tending
to infinity. Indeed the unnormalized trace is `N/d^4+O_d(N^(1-c_d))`, and
`N/m=d^2`.

The exact cat matrix `M_N` permutes the projectors in (12), since its exact
Egorov action permutes the group indices. Right multiplication by it preserves
the relevant Hilbert--Schmidt norms. Therefore the same conclusion holds for
the actual full matrix:

$$
\boxed{\quad
\frac1m\|P_{\chi,N}U_NP_{\psi,N}\|_{\rm HS}^2
=\frac1{d^2}+O_d(N^{-c_d}).\quad}                                 \tag{15}
$$

## 5. What (15) does and does not say

For any orthonormal basis `e_1,...,e_m` of a fixed source sector, the left side
of (15) is exactly `m^(-1) sum_j ||P_chi U_N e_j||^2`. Thus this is a basis
independent mean transition probability for the original deterministic
operator, not an average over kicks, matrices, or dimensions.

For the old sector the mean escaped mass tends to `1-d^(-2)`. In particular,
the old sector is neither exactly invariant nor asymptotically invariant in
this averaged sense. If the eigenvalues of
`P_psi U_N^*P_chi U_NP_psi` are denoted `s_j^2`, then for each fixed `eta>0`

$$
\frac1m\#\{j:s_j^2\ge\eta\}
\le\frac1{d^2\eta}+O_{d,\eta}(N^{-c_d}).                           \tag{16}
$$

This follows by summing the nonnegative `s_j^2`; it does not bound their
maximum away from one. Equations (14)--(16) do not imply a microscopic
eigenphase-spacing bound and do not evaluate the weighted powers of `U_N`
required by `H_diag`.
