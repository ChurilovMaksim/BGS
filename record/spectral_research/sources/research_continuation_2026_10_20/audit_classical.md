> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_continuation_2026_10_20/audit_classical.md`. Embedded SHA256: `fe317398241fdb95ed181cae11a4114c609e8a21eebcc472688879aaf6d8b44d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit of the classical trace and pair diagonal

Date: 20 October 2026.

## Verdict and the one scope correction

The proof in `classical_trace_and_pair_diagonal.md` is valid for its stated near-cat map and for the pair tests with compact Fourier support. In particular, the unbounded diagonal weights do not cause a gap: the finite-compression argument justifies the trace identity without using an unbounded similarity transformation on all of `L^2`.

The one necessary scope clarification is that formulas (20)–(21) use a fixed test `b` for which `hat b` has compact support. The same-orbit estimate is uniform for `m<=BN`; its bound `exp(Cmh^2)` alone does not justify an infinite tail for an arbitrary non-bandlimited Schwartz test. At the author's request this clarification has been added to Section 5 of the source file. It applies in particular to the explicit `b_*` used in the problem.

The claimed conclusion remains a reduction of the pair problem. It does not prove the signed different-orbit cancellation, `H_diag`, or Sine_2.

## 1. Quantitative classical estimates

The finite Fourier support `|k|+|l|<=9` and Fourier coefficient sum below two give, in the strip of width `0.01`,

$$
2(2\pi)9e^{2\pi(0.01)9}<300,
\qquad
2(2\pi)^2 9^2e^{2\pi(0.01)9}<20000.
$$

The matrix

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}
$$

takes a coordinate strip of width `0.001` into one of width `0.007`. The remaining width is vastly larger than the displacement of the Hamiltonian flow over `|t_*|<2*10^{-81}`. Thus the global analytic bound

$$
\Psi(x)=Lx+v(x),\qquad \|v\|<10^{-78}
$$

on that strip has the stated numerical margin. Derivative bounds used for the cones have much more room than is needed.

In eigen-coordinates, if the derivative perturbation has norm `delta<10^{-70}`, a vector with `|s|<=|u|/10` satisfies

$$
|u'|\ge(\lambda-1.1\delta)|u|>5|u|,
\qquad
\frac{|s'|}{|u'|}
\le\frac{\rho/10+1.1\delta}{\lambda-1.1\delta}<\frac1{10}.
$$

The sign of the unstable coordinate is preserved. The analogous inverse-cone argument constructs the stable line. Consequently every periodic unstable multiplier is positive and at least `5^m`; area preservation gives the reciprocal stable multiplier. This verifies the nondegeneracy and multiplier estimates for every period.

## 2. All-period fixed-point count

For the cyclic real action, the unperturbed Hessian is exactly

$$
-\frac14(6I-R-R^{-1}),
$$

with spectrum in `[-2,-1]`. For `m=1`, the two cyclic shifts both equal the identity and the Hessian is `-1`. For `m=2`, the two coincident off-diagonal contributions add, giving diagonal entries `-3/2` and off-diagonal entries `1/2`. Thus the low-period cases require no exception.

Each row of the perturbed Hessian receives contributions from only two neighboring edges. The uniform small second derivatives therefore give a row-sum, hence operator-norm, perturbation bound independent of `m` and of the winding `n`. Strict negative definiteness is global. The action tends to minus infinity quadratically at infinity after allowing its winding-dependent linear terms, so it has exactly one critical point for every integer winding pair.

The critical equations match the momenta on adjacent edges. The boundary equation gives exactly `Psi^m x=x+n`. Changing the initial lift by an integer vector `w` changes `n` by `(L^m-I)w`. Conversely, two critical trajectories with winding representatives in the same such class differ by that lift, by uniqueness. Since `L^m-I` is invertible, no extra lift with unchanged winding is possible.

This proves the bijection with the finite quotient and hence

$$
\#\operatorname{Fix}\Psi^m
=|\det(L^m-I)|
=\lambda^m+\lambda^{-m}-2<\lambda^m.
$$

No appeal to a qualitative structural-stability theorem is needed for this count.

For every fixed point,

$$
W_m(x)=\frac{\Lambda_m(x)^{-1}}
{(1-\Lambda_m(x)^{-1})^2}
\le\frac{25}{16}5^{-m}<2\cdot5^{-m}.
$$

## 3. The weighted classical operator

The coordinates in the source obey

$$
u(L^Tk)=\lambda u(k),\qquad s(L^Tk)=\rho s(k),
$$

and

$$
K(k)=|u(k)|+|s(k)|
=\max(|k_q|,|k_p|/\sqrt2).
$$

In particular, `|k|_1<=3K(k)` and `K(k)>=1/sqrt(2)` for every nonzero integer vector.

The linear weighted operator is a weighted permutation, since `L^T` is an automorphism of the integer lattice. Its nonconstant column multipliers have modulus

$$
\exp\{-a_0[(\lambda-1)|u(k)|+(1-\rho)|s(k)|]\}.
$$

Their sum is finite, and their supremum on nonzero indices is below `exp(-a_0/2)`. Thus the asserted trace-class property and operator-norm bound for the linear operator are both correct.

For the nonlinear difference, write `d=n-L^Tk`. The change in the exponent defining the weight is at most

$$
a_0(|u(d)|+|s(d)|)\le a_0|d|_1.
$$

The contour shift by `-i sign(d_j)/2000` is inside the available analytic strip and gives `exp(-pi*a_0*|d|_1)`. The remaining coefficient is bounded by

$$
2\pi|k|_1\varepsilon e^{2\pi|k|_1\varepsilon}
\le20\varepsilon K(k)e^{6\pi\varepsilon K(k)}.
$$

The last exponential is absorbed by the slack between `(1-rho)a_0K` and `a_0K/2`. Since `pi-1>2`, this proves the source's bound

$$
|(\mathcal R-\mathcal R_0)_{nk}|
\le20\varepsilon K(k)e^{-a_0K(k)/2}e^{-2a_0|d|_1}.
$$

The two stated geometric-series estimates are conservative. For example, if `c=a_0/6`, the first sum is bounded by

$$
2\left(\sum_{j\in\mathbb Z}e^{-c|j|}\right)
\left(\sum_{j\in\mathbb Z}|j|e^{-c|j|}\right),
$$

and elementary bounds for the two factors give a constant below the claimed `13824*a_0^{-3}`. The second sum is `coth(a_0)^2<4*a_0^{-2}`. Their product, including the factor twenty, is below `10^22*epsilon` at `a_0=10^{-3}`.

Absolute summability of all matrix entries gives a trace-class operator directly by a sum of rank-one matrix units. No boundedness of the unweighted diagonal conjugator is used.

Area preservation makes both off-constant parts of the constant row and constant column vanish. Thus the exact block decomposition is valid. Numerically,

$$
e^{-0.0005}+10^{-56}<0.999501
<1-\frac1{8000}=\vartheta.
$$

This verifies the explicit spectral-gap constant. For each positive integer `m`,

$$
|\operatorname{Tr}\mathcal R_\perp^m|
\le\|\mathcal R_\perp\|_1\vartheta^{m-1}.
$$

The trace-norm constant is finite and independent of `m` and `N`. Its possibly large numerical size does not change the asymptotic assertion.

## 4. Why the finite-compression trace identification is valid

Let `P_R` increase strongly to the identity through finite Fourier projections, and let `D_R` be the diagonal matrix of the positive weights in that finite-dimensional range. Exactly in that finite range,

$$
P_R\mathcal RP_R
=D_R(P_RC_\Psi P_R)D_R^{-1}.
$$

Therefore the diagonal entries of every fixed positive power agree. This is a legitimate finite-dimensional similarity statement, even though the corresponding infinite diagonal operator need not be bounded or have a bounded inverse.

Because `mathcal R` is trace class,

$$
P_R\mathcal RP_R\longrightarrow\mathcal R
\quad\hbox{in trace norm}.
$$

A telescoping product identity then gives trace-norm convergence of every fixed power. On the unweighted side, `||P_R C_Psi P_R||<=1` and `P_R C_Psi P_R -> C_Psi` strongly, so fixed powers converge strongly to `C_{Psi^m}`. Taking a fixed diagonal coefficient on both sides proves

$$
(\mathcal R^m)_{kk}
=\int_{\mathbb T^2}e^{2\pi i k\cdot(\Psi^m x-x)}\,dx.
$$

Now multiply by `exp(-eta|k|^2)` and sum. The diagonal of a trace-class operator is absolutely summable, so the left side tends to its trace. The right side is the integral of the positive periodic heat kernel applied to `Psi^m x-x` modulo the integer lattice. The zeros are finite and nondegenerate. On a small neighborhood of each zero, an inverse-function change of variables gives its Jacobian factor; away from all zeros, the heat kernel tends uniformly to zero. This proves

$$
\operatorname{Tr}\mathcal R^m
=\sum_{x\in\operatorname{Fix}\Psi^m}
|\det(D\Psi^m(x)-I)|^{-1}.
$$

Thus the classical trace identity, including its explicit exponential remainder, is rigorously established.

## 5. The same-orbit contribution and summation at m of order N

This step uses the exact cyclic scalar law from the global sector proof: the full amplitude `A_{m,N}(x)` must be identical at all points of the same geometric orbit. Once that exact law is supplied, the combinatorial factor in the diagonal contribution is precisely the primitive period `d(x)`, rather than automatically `m`.

The number of points with a proper period dividing `m` is at most `m lambda^{m/2}`. Since `m-d(x)<=m` and `W_m<=2*5^{-m}`,

$$
\left|\sum_xd(x)W_m(x)-mQ_m\right|
\le2m^2(\sqrt\lambda/5)^m.
$$

The Gaussian modulus lemma gives

$$
|A_{m,N}(x)|^2
=\Lambda_m(x)^{-1}e^{\xi_{m,N}(x)},
\qquad |\xi_{m,N}(x)|\le Cmh^2.
$$

Also,

$$
\Lambda_m^{-1}=W_m(1-\Lambda_m^{-1})^2,
\qquad
|\Lambda_m^{-1}-W_m|\le2\cdot5^{-m}W_m.
$$

For `m<=BN` and sufficiently large `N`, `exp(Cmh^2)-1=O_B(mh^2)`. Since `Q_m` is uniformly bounded and `d(x)<=m`, these formulas give

$$
D_{m,N}
=m+O_B(m^2h^2)+O(m^2\vartheta^m).
$$

All other exponential bases occurring in this calculation, including `sqrt(lambda)/5` and `1/5`, are below the chosen `vartheta`, so this common remainder is valid.

With `h=(2pi N)^{-1}` and compactly supported smooth `w`,

$$
\frac1{N^2}\sum_{m\le BN}m^2h^2=O_B(N^{-1}),
\qquad
\frac1{N^2}\sum_{m\ge1}m^2\vartheta^m=O(N^{-2}).
$$

The main sum is a Riemann sum for `integral u w(u) du`. This checks the source's summed estimate at Heisenberg-scale periods, with error `O_w(N^{-1})`.

Replacing the exact trace by the periodic top-band sum introduces only

$$
\bigl||p_m|^2-|\mathcal P_m|^2\bigr|
\le4N(0.421)^m+4(0.421)^{2m},
$$

because `|p_m|<=N`. Its weighted normalized sum is `O_b(N^{-1})`. The resulting formula for the signed different-orbit contribution and its necessary negative plateau correction is therefore correct.

The explicit convolution estimate for `b_*` also checks: the integration interval has length `1/4`, both arguments lie in `[1/2,7/8]`, and division by `2I^2<=8/e^2` gives

$$
\widehat b_*(u)\ge e^{-98/15}/32
\quad (5/4\le u\le3/2).
$$

The stated lower bound `e^{-196/15}/16384` on the required plateau correction follows. It is not a lower bound on the actual pair discrepancy.

## 6. Exact adjoint and multi-copy attempt

The exact finite-dimensional adjoint operator is

$$
V_N=U_N\otimes\overline{U_N},
\qquad
|p_{m,N}|^2=\operatorname{Tr}V_N^m.
\tag{6.1}
$$

This is a unitary operator on a space of dimension `N^2`. Its spectrum consists of the phase differences of the spectrum of `U_N`. Its fixed space is the commutant of `U_N`, of dimension at least `N`, with equality if the eigenvalues are simple.

There is an exact corresponding two-copy cocycle over `Psi x Psi`, with local kernels `K_h(x) tensor overline{K_h(y)}`. The one-copy rank-one splitting gives four exact components: top/top, top/transverse, transverse/top, and transverse/transverse. Their mixed products vanish by the one-copy identities.

This construction does not itself add cancellation among different periodic orbits. Let `g=1.0002`, `b=0.174`, and `d=0.209`. After summing absolute values over the fewer than `lambda^{2m}` periodic pairs and including the scalar `lambda^{-m}`, the first transverse components are bounded at best by a constant times

$$
(\lambda g b)^m,
\qquad \lambda b=1.014146319\ldots>1.
\tag{6.2}
$$

At the exact unperturbed Gaussian value the critical factor is `lambda*rho=1`. Thus this obstruction is not merely an unfortunate numerical choice: the first tensor transverse bands are marginal at the linear model. The two-transverse component has factor `lambda b^2<1` and can decay.

This does **not** invalidate the already proved pair error estimate. That estimate first factors the independent one-copy sums and uses `|p_m|<=N`, rather than summing the two-copy error terms absolutely. It does show that an additional tensorization followed by the same absolute-value argument does not control the signed top/top different-orbit sum.

## 7. A finite-dimensional obstruction to norm contraction

Suppose `P` is any orthogonal projection of rank `N` in the `N^2`-dimensional adjoint space, and put `Q=I-P`. For a unitary `V`, define

$$
E_m=\bigcap_{j=0}^{m}V^{-j}\operatorname{Ran}Q.
$$

Each subspace has codimension `N`, so

$$
\dim E_m\ge N^2-(m+1)N.
\tag{7.1}
$$

On `E_m`, all inserted projections act as the identity along the first `m` steps:

$$
(QVQ)^m v=V^m v,\qquad v\in E_m.
$$

Since `QVQ` is a contraction, this proves the sharp obstruction

$$
\boxed{\ \|(QVQ)^m\|=1\quad\text{for }m\le N-2.\ }
\tag{7.2}
$$

In fact,

$$
\|(QVQ)^m\|_2^2\ge N^2-(m+1)N.
\tag{7.3}
$$

An equivalent proof uses the positive defect identity on `Ran Q`, for `T=QVQ`:

$$
Q-T^{*m}T^m
=\sum_{j=0}^{m-1}T^{*j}(Q-T^*T)T^j,
\qquad
Q-T^*T=QV^*PVQ.
$$

Its rank is at most `mN`. If `P` is the actual commutant projection, then `P` commutes with `V`; the complement is invariant and the norm remains one for every `m`.

Thus removing `N` candidate diagonal states cannot yield the proposed uniform operator-norm damping before time `N`. A successful mechanism must exploit signed or frequency-averaged traces, not a norm bound of this kind.

## 8. A genuine rank/trace inequality, and the gap it leaves

Finite dimension does give a controlled averaged statement. For every unitary `U` and every positive integer `T`, the Fejer kernel, or equivalently the Gram matrix of `I,U,...,U^T`, gives

$$
\boxed{
\sum_{m=1}^{T}\left(1-\frac{m}{T+1}\right)|p_m|^2
\ge\frac{(T+1)N-N^2}{2}.
}
\tag{8.1}
$$

To see the rank proof, the Gram matrix `G_{jk}=Tr(U^{j-k})`, `0<=j,k<=T`, is positive semidefinite and has rank at most `N`, since all powers are simultaneously diagonal. Therefore

$$
\operatorname{Tr}G^2
\ge\frac{(\operatorname{Tr}G)^2}{N}
=(T+1)^2N.
$$

Expanding its left side by `j-k` yields (8.1). Alternatively, the positive Fejer kernel summed over eigenvalue differences has at least its `N` diagonal contributions.

This is not the CUE form factor. If `T/N -> B>=1`, the normalized right side tends to `(B-1)/2`. In contrast, the normalized sum with `|p_m|^2` replaced by `min(m,N)` tends to

$$
\int_0^B(1-u/B)\min(u,1)\,du
=\frac{B-1}{2}+\frac{1}{6B}.
\tag{8.2}
$$

The unresolved gap is of order `N^2` before normalization and equals the nonzero number `1/(6B)` afterward. For integer `B`, equally spaced clock eigenvalues asymptotically attain the rank lower bound rather than (8.2). Arbitrarily small generic perturbations remove exact scalar returns and zero traces while preserving these finite-window limits. Thus those qualitative arithmetic exclusions do not fill the gap.

The inequality is a real consequence of finite rank, but it does not supply the needed signed periodic-orbit cancellation.

## 9. A concrete quantitative barrier at microscopic phase separations

The exact adjoint formula localizes the remaining difficulty. Write the eigenvalues as `exp(2pi i theta_j)`, with `theta_j` in the circle, and put

$$
S_N(w)=\frac1{N^2}\sum_{m\ge1}w(m/N)|p_m|^2,
\qquad w=|\widehat b_*|^2.
$$

The inverse Fourier transform of `w` is the autocorrelation of `b_*`. Because `b_*` is real, even, and nonnegative, this function, denoted `check w`, is nonnegative everywhere and `check w(0)>0`.

Poisson summation gives the exact identity

$$
2S_N(w)+w(0)
=\frac1N\sum_{j,k=1}^N\sum_{\ell\in\mathbb Z}
\check w\bigl(N(\theta_j-\theta_k+\ell)\bigr).
\tag{9.1}
$$

Choose a fixed `a>0` for which `check w(t)>=check w(0)/2` on `|t|<=a`. Let

$$
M_N(a)=\#\{(j,k):j\ne k,\ \|\theta_j-\theta_k\|_{\mathbb R/\mathbb Z}\le a/N\}.
$$

All terms on the right of (9.1) are nonnegative. The spectral diagonal and these near-coincident pairs give

$$
\boxed{
S_N(w)\ge
\frac{\check w(0)-w(0)}2
+\frac{\check w(0)}{4N}M_N(a).
}
\tag{9.2}
$$

Thus even boundedness of the desired pair statistic requires the new quantitative estimate

$$
M_N(a)=O(N).
\tag{9.3}
$$

The correct Sine_2 limit requires much more, namely the appropriate limiting weighted microscopic difference measure. But (9.3) is a concrete weaker barrier already not obtained from the current classical gap, transverse cocycle, or arithmetic nonvanishing results.

Here is an explicit demonstration of the limitation of rank and trace constraints. It is a countermodel to that proposed mechanism, not to the specified quantization. Along odd squares `N=M^2`, take `M` equally spaced spectral clusters, each containing `M` eigenvalues:

$$
\theta_{a,b}=a/M+\epsilon_{a,b},
\qquad 0\le a,b<M,
\qquad |\epsilon_{a,b}|\le N^{-4}.
$$

Choose the perturbations generically and distinctly. They can avoid every exact scalar return and every zero power trace: these are countably many proper analytic conditions on the perturbations. The empirical spectral measures still approach uniform measure. For each fixed positive `m`, and even uniformly for `m=O(log N)`, the traces tend to zero.

Before perturbation, `p_m=N` if `M` divides `m`, and `p_m=0` otherwise. For `m<=BN`, the perturbation changes a trace by at most

$$
2\pi m\sum_{a,b}|\epsilon_{a,b}|\le2\pi B N^{-2}.
$$

Consequently,

$$
S_N(w)=\sum_{r\ge1}w(r/M)+o(1)
=M\int_0^\infty w(u)\,du+O(1).
\tag{9.4}
$$

This grows like `sqrt N`, despite unitarity, the dimension constraints, simple eigenvalues, no exact scalar returns, nonzero traces, and uniform macroscopic spectral distribution. Here `M_N(a)` is of order `N^{3/2}`. The example also respects any mere boundedness requirement on each fixed-time trace.

Therefore the exact multi-copy and finite-rank identities alone do not even prove the weaker boundedness prerequisite (9.3), let alone the required signed limit for `b_*`.

## 10. What was and was not gained by this attempt

The adjoint construction gives exact finite-dimensional formulas and exposes two useful barriers: a rank obstruction to operator-norm damping before time `N`, and a microscopic pair-count requirement for any bounded `b_*` statistic. The Fejer inequality is a genuine controlled averaged consequence of finite rank, but its gap from the CUE prediction remains nonzero at the time scale of interest.

At the level of available bounds, unitarity gives `|p_m|^2<=N^2`, whereas the desired averaged form factor is of order `N` per relevant time. An additional factor of `N` in averaged cancellation is needed even to reach the expected scale, followed by identification of its limiting coefficient. The one-copy trace formula already forces enormous cancellation relative to the sum of absolute periodic-orbit weights; it does not supply this further averaged factor.

No new proof of the required different-orbit cancellation was obtained from this mechanism. A next valid advance must prove a quantitative trace average or a microscopic spectral-pair bound for this particular deterministic sequence of quantum maps. Referring only to classical mixing, unitarity, absence of exact revivals, or an unsupported norm contraction would not meet that requirement.
