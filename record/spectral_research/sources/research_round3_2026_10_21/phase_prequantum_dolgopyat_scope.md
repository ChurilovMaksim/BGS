> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/phase_prequantum_dolgopyat_scope.md`. Embedded SHA256: `91215713938e76debb628149d578fca00e3f22a872d98e8e02a42628876640cb`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Prequantum and Dolgopyat estimates: actual weights and the shrinking spectral window

Research continuation, 21 October 2026.

**Status.** Primary theorems were checked against the actual classical map, the quantum amplitude normalization, and the $m\asymp N$ window. They do not provide the needed signed trace-pair estimate. This note records the precise mismatch, together with the executed $N,m$ estimate in the companion Planck-hole note. It is not a new conditional proof of $H_{\rm diag}$.

## 1. The actual geometric setting

Use the ordinary symbol forced by the modular-half Weyl rule:

$$
a(q,p)=\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10
 +r(q+1/2)\cos(2\pi p-\alpha_0)/100.
$$

The physical map is a Hamiltonian flow of time
$-\tau/(2\pi)$ composed with

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
$$

This is a smooth symplectic diffeomorphism $\Psi$ of the torus. Its hyperbolicity follows directly from the small flow derivative and the hyperbolic invariant cones of $L$; the graph construction in the log-time note gives the needed uniform derivative bounds. The preserved form has integral class and torus volume one.

Here the linear canonical relation can be checked directly, including its arithmetic character factors. In the eight-character decomposition of the log-time note,

$$
3x^2-2xy+3y^2\equiv 3(x+y)^2\pmod8.
$$

Consequently the character is a function of $x+y\pmod4$, and only four Fourier terms can be nonzero:

$$
\chi_s(x,y)=\sum_{j=0}^3\gamma_{s,j}
 e^{2\pi i j(x+y)/4}.
$$

Their canonical relations for the ordinary quadratic phase are

$$
(Q,P)=(3q-4p-j,-2q+3p+j).
$$

They all reduce to $L$ on the torus. Thus the finite character decomposition does not introduce different torus maps. The larger 64-term budget used in the log-time estimate remains valid.

The prequantum lift can also be verified explicitly. On

$$
\mathbb R^2\times(\mathbb R/\mathbb Z),\qquad
\eta=du+\tfrac12(q\,dp-p\,dq),\qquad d\eta=dq\wedge dp,
$$

quotient by the deck maps

$$
D_{m,n}(q,p,u)=
\left(q+m,p+n,u+\tfrac12(nq-mp+mn)\right).
$$

Their composition law holds modulo an integer in $u$, and each preserves $\eta$. Since $L$ is symplectic, $(q,p,u)\mapsto(L(q,p),u)$ preserves $\eta$ on the cover. It descends to this quotient because, writing $(m',n')=L(m,n)$, the possible change in the deck constant is $(m'n'-mn)/2$, an integer: $L\equiv I\pmod2$.

For the kick vector field $Y=(-a_p,a_q)/(2\pi)$, define its lifted vector field by

$$
\pi_*\widetilde Y=Y,\qquad
\eta(\widetilde Y)=a/(2\pi).
$$

This definition is global because $a$ is periodic, and

$$
\mathcal L_{\widetilde Y}\eta
=d(a/(2\pi))+\iota_Y(dq\wedge dp)=0.
$$

Its time-$\tau$ flow and the lifted $L$ therefore give a connection-preserving lift of the actual classical composition. This verifies the geometric prequantization setting; it does not identify two different finite quantization procedures without an additional argument.

For a pair with conjugate phase, the geometric base is

$$
\Psi\times\Psi:\mathbb T^2\times\mathbb T^2\longrightarrow
 \mathbb T^2\times\mathbb T^2,
$$

with symplectic form
$\Omega=\omega\oplus(-\omega)$.
The associated line bundle is the product of the original line bundle and its dual. Its $N$-th Fourier component carries the phase difference
$e^{iN(S_x-S_y)}$.
The unstable bundle is $E^u_x\oplus E^u_y$.
The pair diagonal is Lagrangian, because $\Omega$ restricts to zero there.

## 2. The sign of the potential is essential

Let $J_m^u(x)$ denote the unstable Jacobian of $\Psi^m$. At a periodic point in this two-dimensional positive cone, write $\Lambda=J_m^u(x)>1$. Area preservation gives the two eigenvalues $\Lambda,\Lambda^{-1}$, so the exact flat-trace denominator is

$$
|\det(I-D\Psi^m(x))|=\Lambda(1-\Lambda^{-1})^2.
$$

A prequantum transfer operator weighted by a potential $V$ has a numerator $e^{V_m(x)}$. Therefore the leading exponential weight $J_m^u(x)^{-1/2}$ of a quantum orbit corresponds to the reference potential

$$
V_0=\frac12\log J^u,
\tag{1}
$$

not to $V=0$. This compares exponential weights; it does not equate the full individual periodic terms or discard their stable factors. On the product it corresponds to

$$
V_{0,\mathrm{pair}}(x,y)
=\frac12\log J^u(x)+\frac12\log J^u(y).
\tag{2}
$$

Equivalently, an expanding symbolic transfer normalized by its positive leading pressure needs that normalization put back before comparison with the quantum trace. An exponential contraction for the normalized operator cannot be used without accounting for this exponential factor.

This distinction is visible already for the linear map, where $J_m^u=\lambda^m$, $\lambda=3+2\sqrt2$. A factor $\lambda^{-m/2}$ in an unweighted prequantum band is exactly canceled by $e^{mV_0}=\lambda^{m/2}$. In the pair problem both factors are squared.

## 3. What the prequantum band theorem actually estimates

Primary source: F. Faure and M. Tsujii, *Prequantum transfer operator for symplectic Anosov diffeomorphism*, Astérisque 375 (2015); author text
https://arxiv.org/pdf/1206.0282 .

Theorems 1.35--1.37 treat the reference potential through a Grassmann-bundle extension. They leave an outer band asymptotically on the unit circle and separate it from inner bands. Equation (1.52) gives a uniform resolvent bound between bands or outside a fixed neighborhood of the outer band. Theorem 1.36 gives its index and Weyl count. Theorem 1.17 alone does not cover the generally Hölder $V_0$; Remark 1.18 explicitly explains this regularity issue.

Applying the geometry of Section 1 to that setting gives an outer-space scale $N$ on the original torus and $N^2$ on the product. Indeed the tangent bundle of a torus is trivial, so its Todd class is one, and the leading symplectic volume computation is respectively

$$
\int_{\mathbb T^2}e^{N\omega}=N,\qquad
\int_{\mathbb T^4}e^{N\Omega}=N^2
$$

with the symplectic orientation. The gap from an inner band does not separate the $N^2$ product phases from one another inside the outer band.

The specific radial window required by the resolvent form of the pair statistic is

$$
z_N=r_N^{-1}=e^{2s/N}
 =1+\frac{2s}{N}+O_s(N^{-2}).
\tag{3}
$$

For every fixed $\epsilon>0$, (3) lies inside the excluded
$\epsilon$-neighborhood of the unit circle for all large $N$. Thus the resolvent bound quoted above does not apply. Replacing $\epsilon$ by $1/N$ would require new control of both $C_\epsilon$ and $N_\epsilon$; the theorem's fixed-$\epsilon$ quantifiers do not supply it.

There is a second, logically separate, identification obligation. The outer-band quantization constructed in this source is its own geometric quantum operator. It is not declared equal to the exact matrix
$e^{i\tau NA_N}M_N$ merely because the two maps have the same classical canonical relation. No such equality or $o(1)$ error for the present microscopic functional has been proved here.

## 4. Exact amplitude corrections at linear times

The existing exact-cocycle input, in the notation of the old report, has

$$
\gamma_h=\gamma_0+h\gamma_1+O(h^2),
\qquad \gamma_0>0,\quad \gamma_1\in i\mathbb R,
\qquad h=(2\pi N)^{-1}.
$$

Write $\beta=\operatorname{Im}(\gamma_1/\gamma_0)$.
Pointwise expansion of the logarithm gives

$$
\prod_{j=0}^{m-1}\frac{\gamma_h(\Psi^j x)}
                         {\gamma_0(\Psi^j x)}
=
\exp\left(
 ih\sum_{j=0}^{m-1}\beta(\Psi^j x)+O(mh^2)
\right).
\tag{4}
$$

For $m\le BN$, the modulus error in (4) is $1+O_B(N^{-1})$.
The displayed phase correction, however, has only an $O_B(1)$ bound from this expansion. It is not justified to delete it as $o(1)$.
This does not assert that $\beta$ is nonzero or non-coboundary; it identifies what the available estimate permits.

The conjugate product requires the difference of both sums in (4), so the same issue persists between different interior words. Consequently any application of a fixed-potential theorem to only the classical action would first require an estimate for the full $N$-dependent phase cocycle. The exact cocycle must remain in the calculation until that estimate is proved.

## 5. A concrete high-frequency Dolgopyat comparison

A directly relevant discrete-time primary result is D. Dolgopyat,
*On mixing properties of compact group extensions of hyperbolic systems*,
Israel J. Math. 130 (2002), 157--205;
author text https://www.math.umd.edu/~dolgop/extcompfc.pdf .
Theorem 1.1 requires a quantitative Diophantine transitivity condition.
At the symbolic level, Proposition 4.4 bounds representation-frequency powers in the form

$$
\|\mathcal L_\nu^m\|_\nu
\le C|\nu|^{\beta_1}
       (1-|\nu|^{-\beta_2})^m.
\tag{5}
$$

Even before the operator-identification issue, substituting the relevant frequency and time, $|\nu|\asymp N$, $m\asymp N$, turns (5) into

$$
C N^{\beta_1}\exp[-O(N^{1-\beta_2})].
\tag{6}
$$

There is no useful decay at that scale unless the required exponents and normalization are established. In particular qualitative non-coboundarity, or a pressure gap for a different positive operator, does not supply the missing exponent.

A sharper primary comparison is J. Chen and H. Hu,
*The spectral gap for transfer operators of torus extensions over expanding maps*,
https://arxiv.org/pdf/1503.02232 .
Proposition 3.2 gives a frequency-uniform exponential bound when the smooth base is uniformly expanding and the smooth torus cocycle is not an essential coboundary. Here $\Psi\times\Psi$ is an invertible hyperbolic map, not uniformly expanding. A quotient by stable leaves would change the base space, branch boundaries, function spaces, weights, and cocycle regularity. Those hypotheses have not been verified for an operator that retains the exact quantum phase and whose trace equals the desired functional.

These theorems are comparison results, not inputs to a claimed universality proof.

## 6. The executed Planck-hole test

To avoid merely noting the unitary outer band, the companion note
*phase_planck_hole_time_scale_test.md* removes a diagonal tube of width
$cN^{-1/2}$ using an exact finite Weyl tight frame.
Its effect $E_N$ obeys

$$
0\le E_N\le I,\qquad
\operatorname{Tr}E_N=(2\lfloor c\sqrt N\rfloor+1)^2
 =4c^2N+O_c(\sqrt N).
$$

For the exact opened doubled map

$$
\mathcal K_N=\operatorname{Ad}_{U_N}(I-E_N)^{1/2}
$$

that note proves

$$
\|\mathcal K_N^m\|_{\rm op}^2
\ge 1-\frac{m\,\operatorname{Tr}E_N}{N^2}.
\tag{7}
$$

Thus its norm stays close to one at every fixed logarithmic time and bounded below for a fixed positive fraction of the Heisenberg time. A uniform exponential estimate with a polynomial $N$-prefactor cannot hold in the physical norm, or a polynomially equivalent norm, even after this diagonal removal. Arbitrary anisotropic norms require a separate comparison; (7) does not rule out trace-only cancellation.

The attempt to extract that trace cancellation from the positive leakage identity was also performed. It gives only

$$
|\operatorname{Tr}(
 (\operatorname{Ad}_{U_N})^m-\mathcal K_N^m)|
 \le m\,\operatorname{Tr}E_N.
$$

After the actual finite-Fourier sum and $N^{-2}$ normalization, this is $O(N)$, not $o(1)$. No additional cancellation follows from that positive identity.

## 7. Precedent for the exact-integration obstruction

S. Nonnenmacher and M. R. Zirnbauer,
*Det-Det correlations for quantum maps: Dual pair and saddle-point analyses*,
J. Math. Phys. 43 (2002), 2214--2240, DOI 10.1063/1.1462417,
https://www.imo.universite-paris-saclay.fr/~stephane.nonnenmacher/publis/NonnenZirnbauer2002.pdf ,
Sections III and IV, derive the complete saddle sum as a Weyl character expression. The two standard saddles alone have spurious singularities; including all saddles cancels them. Section IV explicitly explains that the resulting exact expression still requires the unknown eigenphases. Section IV C.1 also lists unresolved saddle contributions in the proposed averaged approximation.

This source supports the boundary of the method. It does not supply a proof for an individual deterministic quantum map and does not prove the original problem impossible.

## 8. Precise outcome

The new estimates in this continuation concern the exact $U_N$, and no odd subsequence or perturbation average was introduced. The published spectral-gap results checked here estimate different weights, a different operator class, or a spectral region separated from the required $1/N$ window. Removing only a Planck-width diagonal does not repair the physical operator-norm obstruction. The remaining viable requirement is a genuinely signed trace estimate inside the outer quantum band. That estimate has not been proved in this route.

