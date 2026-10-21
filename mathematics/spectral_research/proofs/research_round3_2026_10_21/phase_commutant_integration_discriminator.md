> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_commutant_integration_discriminator.md`. Embedded SHA256: `df3c9b16210c64341f804ff28a0dd30beb366a0610016168edcb72fab5f0052a`.
> [Thematic guide](../../topics/closure.md).

# Exact commutant retention: the remaining coefficients still contain every phase gap

Research continuation, 21 October 2026.

**Status.** This is a discriminating calculation for the full-phase transfer route. It proves an exact formula for integrating the global phase, with every pole sector retained, and identifies the precise place where a commutant-only argument becomes circular. It does not establish $H_{\rm diag}$, a counterexample for the specified family, or an asymptotic estimate for the remaining coefficients.

The actual-family input available separately is
$\mu_N=O(1/\log N)$ and
$\operatorname{Tr}(\mathcal P_N\mathcal D_N)=O(N/\log N)$, proved independently of the old all-time orbit formula in
*phase_logtime_dispersion_and_missing_modes.md*.
The formulas below do not need this input until Section 4.

## 1. A complete global-phase integration

Let $U$ be any $N$-dimensional unitary with eigenvalues
$\lambda_1,\ldots,\lambda_N$. For
$|a|,|b|<1$, $b\ne0$, and arbitrary numerator parameters $c,d$, define

$$
\Omega_U(a,c;b,d)=
\oint_{|z|=1}
 \prod_{j=1}^N
 \frac{(1-cz\lambda_j)(1-dz^{-1}\lambda_j^{-1})}
      {(1-az\lambda_j)(1-bz^{-1}\lambda_j^{-1})}
 \frac{dz}{2\pi iz}.
\tag{1}
$$

This is exactly the single global-angle average. It contains no independent averaging over eigenvalues, matrix entries, classical trajectories, or dimensions.

Suppose first that all $\lambda_j$ are distinct. Rewrite the advanced factor as
$(z-d\lambda_j^{-1})/(z-b\lambda_j^{-1})$.
The poles inside the contour are $0$ and $b\lambda_j^{-1}$.
The residue at $0$ is $(d/b)^N$. At $b\lambda_j^{-1}$, elementary cancellation gives

$$
\boxed{
\begin{aligned}
\Omega_U(a,c;b,d)
={}&(d/b)^N\\
&+(1-d/b)\sum_{j=1}^N
 \left[\prod_{k\ne j}
 \frac{1-(d/b)\lambda_j/\lambda_k}
      {1-\lambda_j/\lambda_k}\right]
 \left[\prod_{k=1}^N
 \frac{1-bc\,\lambda_k/\lambda_j}
      {1-ab\,\lambda_k/\lambda_j}\right].
\end{aligned}}
\tag{2}
$$

Every one of the $N$ pole sectors is present. No saddle expansion, separation of eigenvalues, or asymptotic argument is used. Formula (2) extends continuously through coincident eigenvalues after summing its terms; alternatively the repeated poles can be evaluated directly. The separately displayed residues are not claimed to be uniformly conditioned as eigenvalues approach one another.

## 2. The exact pair coefficient after retaining all sectors

At the matched sources $c=a,d=b$, every product in square brackets in (2) equals $1$, whereas its prefactor $1-d/b$ vanishes. Differentiating once in each numerator source therefore gives the particularly simple exact identity

$$
\boxed{\displaystyle
\left.\partial_c\partial_d\Omega_U(a,c;b,d)
\right|_{c=a,\ d=b}
=\sum_{j,k=1}^N
 \frac{\lambda_k/\lambda_j}
      {1-ab\,\lambda_k/\lambda_j}.}
\tag{3}
$$

To check the sign and normalization, the derivative of the outer prefactor is $-1/b$, and the derivative in $c$ of the second product at matched sources is
$-b\sum_k(\lambda_k/\lambda_j)/(1-ab\lambda_k/\lambda_j)$.

A second proof of (3) requires no simple-spectrum assumption. Differentiate (1) at matched sources and expand each resolvent in its absolutely convergent geometric series. Integration in $z$ keeps equal powers and yields, with $r=ab$,

$$
\left.\partial_c\partial_d\Omega_U\right|_{\rm matched}
=\sum_{n\ge0}r^n|\operatorname{Tr}U^{n+1}|^2
=\frac1r\sum_{m\ge1}r^m|\operatorname{Tr}U^m|^2.
\tag{4}
$$

For $r=0$, the first series in (4) defines the continuous value. Absolute convergence follows from
$|\operatorname{Tr}U^m|\le N$ and $|r|<1$.

Thus the exact full integration retains the gap factors
$1-r\lambda_k/\lambda_j$ inside each sector. It does not replace those factors by a universal scalar.

Let
$d_U=\sum_\lambda(\dim E_\lambda)^2$ be the rank of the commutant. Splitting the pairs in (3) into equal and unequal eigenvalues gives

$$
r\,\partial_c\partial_d\Omega_U|_{\rm matched}
=\frac{r\,d_U}{1-r}
+\sum_{\lambda_j\ne\lambda_k}
 \frac{r\,\lambda_k/\lambda_j}
      {1-r\,\lambda_k/\lambda_j}.
\tag{5}
$$

The first term is the exact commutant contribution. The second term retains every unequal spectral phase difference. Its terms need not be positive even when $0<r<1$. Any argument that discards it has already discarded the nontrivial pair statistic.

At $r_N=e^{-2s/N}$, and if the spectrum is simple, the normalized first term tends to $1/(2s)$. The CUE target is instead

$$
\frac{1-e^{-2s}}{4s^2}.
$$

Consequently, even knowing and integrating all $N$ fixed directions exactly leaves a nonzero order-one correction to determine. For a family with multiplicities one must retain the exact factor $d_{U_N}/N$, rather than silently replacing it by $1$.

## 3. What the corresponding Schur complement does and does not accomplish

Let $\mathcal C=\operatorname{Ad}_U$ on
$\mathcal V=M_N(\mathbb C)$, let $\mathcal P$ project onto its full commutant, and put $\mathcal Q=I-\mathcal P$. These are reducing projections for $\mathcal C$. Therefore

$$
(I-r\mathcal C)^{-1}
=\frac{\mathcal P}{1-r}
 +\mathcal Q(I-r\mathcal C|_{\operatorname{Ran}\mathcal Q})^{-1}
      \mathcal Q.
\tag{6}
$$

The off-diagonal Schur blocks vanish exactly. Thus a Schur complement with respect to the **true** commutant does not generate a new effective interaction that could determine the gap statistic. It simply retains the resolvent of $\mathcal C$ on unequal spectral pairs. Its eigenvalues are already
$(1-r\lambda_j/\lambda_k)^{-1}$, for
$\lambda_j\ne\lambda_k$.

By contrast, splitting into matrices diagonal in the coordinate basis and their orthogonal complement does have nonzero Schur blocks. If $\mathcal D$ is coordinate-diagonal projection and $\mathcal E=I-\mathcal D$, then

$$
\mathcal D(I-r\mathcal C)^{-1}\mathcal D
=
\left[
 I_{\mathcal D}
-r\mathcal D\mathcal C\mathcal D
-r^2\mathcal D\mathcal C\mathcal E
 (I_{\mathcal E}-r\mathcal E\mathcal C\mathcal E)^{-1}
 \mathcal E\mathcal C\mathcal D
\right]^{-1}.
\tag{7}
$$

All inverses in (7) exist for $|r|<1$, because the compressions of the unitary $\mathcal C$ are contractions and the full operator is invertible. Formula (7) is the ordinary finite-dimensional block inverse.

The first compressed block is represented by the stochastic matrix
$(|U_{xy}|^2)_{x,y}$. The self-energy in (7), however, contains the complementary quantum resolvent; it is not controlled merely by mixing of this stochastic matrix. Replacing it by zero would be an additional approximation, for which (7) supplies no error bound.

## 4. A family-specific slow-complement consequence

The actual-family coordinate delocalization theorem gives a quantitative reason that the complement in (7) cannot be assigned a uniform inverse bound at $r\to1$.

Here is an elementary general lemma. Suppose
$\mathcal C$ is unitary, its fixed-space projection is $\mathcal P$ of rank $d$, and $\mathcal D$ is any orthogonal projection. Put
$\mathcal E=I-\mathcal D$ and
$\kappa=\operatorname{Tr}(\mathcal P\mathcal D)$.
For $0<\epsilon<1$, the compression
$I_{\mathcal E}-r\mathcal E\mathcal C\mathcal E$, $0<r<1$,
has at least

$$
d-\kappa/\epsilon
$$

singular values, interpreted by rounding down to an integer, at most

$$
(1-r)+r\sqrt{\epsilon/(1-\epsilon)}.
\tag{8}
$$

Proof: restrict $\mathcal P\mathcal D\mathcal P$ to
$\operatorname{Ran}\mathcal P$. It is positive, has trace $\kappa$, and has at most $\kappa/\epsilon$ eigenvalues exceeding $\epsilon$. On the complementary subspace $W\subset\operatorname{Ran}\mathcal P$,

$$
\|\mathcal D X\|^2\le\epsilon\|X\|^2,\qquad
\|\mathcal E X\|^2\ge(1-\epsilon)\|X\|^2.
$$

The map $X\mapsto\mathcal E X$ is injective on $W$. Since $\mathcal C X=X$,

$$
(I_{\mathcal E}-\mathcal E\mathcal C\mathcal E)\mathcal E X
=\mathcal E\mathcal C\mathcal D X.
$$

Its norm is at most $\sqrt\epsilon\|X\|$, so on the subspace
$\mathcal E W$ the operator norm is at most
$\sqrt{\epsilon/(1-\epsilon)}$.
Adding the term $(1-r)I_{\mathcal E}$ proves the bound on that subspace. The minimum-maximum characterization of singular values proves (8).

For the specified $U_N$, Section 9 of
*phase_logtime_dispersion_and_missing_modes.md* proves
$\kappa_N\le N\mu_N$ and $d_N\ge N$.
For fixed $0<\delta<1$, choose

$$
\epsilon_N=\frac{N\mu_N}{\delta d_N}
 \le\mu_N/\delta,
$$

which lies in $(0,1)$ for sufficiently large $N$. The compression appearing in (7), at $r_N=e^{-2s/N}$, has at least
$(1-\delta)d_N$ singular values bounded by

$$
O_{s,\delta}((\log N)^{-1/2}).
\tag{9}
$$

This is an actual-family obstruction to a uniformly bounded inverse on the coordinate-off-diagonal complement. It does not locate the eigenvalues of that generally nonnormal compression and does not evaluate the order-$N$ pair statistic.

## 5. Outcome of this route

The complete integration calculation and the exact reducing decomposition agree:

- Retaining the true commutant is possible, but its universal-looking contribution is only the equal-phase part.
- The unequal-phase coefficients survive the integration with their original gap denominators.
- Replacing the true commutant by coordinate-diagonal fields loses almost all its rank mass for the specified family.
- The complementary coordinate field space contains order $N$ slowly invertible directions; assigning it a fixed gap contradicts (9).

These observations eliminate a specific circular use of supersymmetric or Schur-complement reduction. They supply no error estimate allowing the remaining gap denominators to be replaced by their CUE values. The missing signed finite-Fourier trace sums from the original problem remain missing.

The determinant ratio (1) is also the exact generating function used by M. R. Zirnbauer, *Pair Correlations of Quantum Chaotic Maps from Supersymmetry*, https://arxiv.org/pdf/chao-dyn/9812023 , Section 3. The residue proof above is elementary and does not rely on its later ensemble-averaged approximation.

