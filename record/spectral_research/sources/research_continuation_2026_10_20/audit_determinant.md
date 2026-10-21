> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_continuation_2026_10_20/audit_determinant.md`. Embedded SHA256: `b2a95bd8ccbee9c6f2098544dfe062abdeb9335e2205af1eac63341062c8c931`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Audit of the exact dynamical determinant and a bounded nonlinear consequence

Date: 20 October 2026.

## Status

The formulas in `exact_dynamical_determinant.md` are correct, subject to the exact all-time trace theorem that is explicitly their input. The determinant continuation, zero multiplicities, uniform analytic correction, and microscopic resolvent comparison require no statistical assumption.

The same-orbit exponentially weighted limit is also correct. Its remainder can be sharpened from `o(1)` to `O_s(N^{-1})`. The proof is given below without extending a finite-window estimate beyond its justified range.

The analytic correction also gives a uniform comparison of bounded nonlinear functionals. This is a comparison of two exact descriptions of the original deterministic family. It does not evaluate the nonlinear angular average, prove different-orbit cancellation, or give a CUE or Sine_2 limit. The definition of the continued dynamical determinant still uses the complete grouped periodic-orbit trace data.

Write

$$
q=0.421,\qquad p_{m,N}=\mathcal P_{m,N}+E_{m,N},
\qquad |E_{m,N}|\le2q^m,
$$

and let `N` be a sufficiently large allowed odd dimension. All estimates below use this one threshold in `N`, with additional explicitly stated thresholds for a fixed Laplace parameter `s>0`.

## 1. Determinant continuation and the sign of the correction

The initial periodic-orbit growth estimate gives absolute convergence of

$$
\mathcal Z_N(z)=
\exp\left(-\sum_{m\ge1}\frac{\mathcal P_{m,N}}m z^m\right)
$$

in the stated disk of radius `[sqrt(lambda)*1.0002]^{-1}`. In its intersection with the unit disk,

$$
\det(I-zU_N)=
\exp\left(-\sum_{m\ge1}\frac{p_{m,N}}m z^m\right).
$$

Since `P_m=p_m-E_m`, the correction has the plus sign:

$$
\mathcal Z_N(z)=D_N(z)e^{G_N(z)},
\qquad
G_N(z)=\sum_{m\ge1}\frac{E_{m,N}}m z^m.
\tag{1.1}
$$

The last series converges normally in `|z|<q^{-1}`. Its product with the polynomial `D_N` supplies the unique holomorphic continuation of the initially defined function. One does not claim that a single holomorphic logarithm of `Z_N` continues through its zeros.

The coefficient bound gives, throughout that disk,

$$
|G_N(z)|\le-2\log(1-q|z|),
\qquad
|G_N'(z)|\le\frac{2q}{1-q|z|}.
\tag{1.2}
$$

It follows that

$$
(1-q|z|)^2\le|e^{G_N(z)}|
\le(1-q|z|)^{-2}.
$$

The factor is zero-free. Thus `Z_N` has precisely the reciprocal eigenvalues of `U_N` as zeros in this disk, with exactly their original multiplicities. The quotient `Z_N/D_N` at such a zero means its analytic removable extension, namely `exp G_N`.

This is a theorem about the full finite spectrum, but places no new distributional condition on those zeros.

## 2. Resolvents, including at microscopic distance

Direct differentiation gives

$$
\frac{D_N'(z)}{D_N(z)}
=-\operatorname{Tr}\bigl(U_N(I-zU_N)^{-1}\bigr),
$$

so the normalization in the source is correct:

$$
R_N(z)=\frac1N\operatorname{Tr}(I-zU_N)^{-1}
=1-\frac zN\frac{D_N'}{D_N}.
$$

For the dynamical logarithmic derivative,

$$
\mathcal R_N(z)-R_N(z)=-\frac zN G_N'(z).
\tag{2.1}
$$

This difference is holomorphic throughout `|z|<q^{-1}`. The principal parts of the two meromorphic functions agree at every pole, including multiple eigenvalues. Therefore

$$
|\mathcal R_N(z)-R_N(z)|
\le\frac{2q|z|}{N(1-q|z|)}
\tag{2.2}
$$

is independent of the distance to the eigenvalues, wherever the individual meromorphic values are defined. On `|z|<=1`, the upper bound is at most `2q/[N(1-q)]`.

In particular, it remains `O(N^{-1})` at `z=e^{-s/N+2pi i alpha}` uniformly in `alpha`, for every fixed `s>0`. This controls the difference, not the possibly large individual resolvents.

For completeness, averaging the absolute quantum resolvent requires no eigenvalue separation. By the triangle inequality and angular translation invariance,

$$
\int_0^1|R_N(re^{2\pi i\alpha})|\,d\alpha
\le\int_0^1\frac{d\alpha}{|1-re^{2\pi i\alpha}|}
=O\left(1+\log\frac1{1-r}\right).
$$

The final estimate follows from the displayed elementary denominator identity in the source. With `delta=mathcal R_N-R_N`, the inequality

$$
\bigl||R_N-1+\delta|^2-|R_N-1|^2\bigr|
\le2|R_N-1||\delta|+|\delta|^2
$$

then proves the claimed `O_s(log N/N)` bound for the integral of the absolute difference.

The signed integral has the stronger bound from Parseval. To justify the series at radii greater than the original defining radius of `Z_N`, observe that the trace identity and unitarity imply

$$
|\mathcal P_{m,N}|\le N+2q^m.
\tag{2.3}
$$

Thus, throughout `|z|<1`,

$$
\mathcal R_N(z)-1=\frac1N\sum_{m\ge1}\mathcal P_{m,N}z^m,
\qquad
R_N(z)-1=\frac1N\sum_{m\ge1}p_{m,N}z^m.
$$

At every fixed radius below one the series are square summable. Finally,

$$
\bigl||p_m|^2-|\mathcal P_m|^2\bigr|
\le4Nq^m+4q^{2m}
$$

proves an `O(N^{-1})` bound for the normalized signed coefficient sum, even uniformly over all radii `0<r<=1`. Its sign is reversed if the two resolvent squares are subtracted in the reverse order; the asserted bound is unaffected.

## 3. Global same-orbit comparison

Let `D_m^{orb}` be the geometric same-orbit contribution. Write

$$
|\mathcal A_{m,N}(x)|^2
=\Lambda_m(x)^{-1}e^{\xi_{m,N}(x)},
\qquad
|\xi_{m,N}(x)|\le a m/N^2,
$$

where the fixed constant `a` includes the factor `(4pi^2)^{-1}`. Put

$$
C_m=\sum_{x\in\operatorname{Fix}\Psi^m}d(x)\Lambda_m(x)^{-1},
\qquad
B_m=\sum_{x\in\operatorname{Fix}\Psi^m}d(x)W_m(x).
$$

Since `d(x)<=m` and `sum W_m=Q_m<=C_0`,

$$
0\le C_m\le C_0m.
$$

The exponential modulus estimate gives the global bound

$$
|D_m^{orb}-C_m|
\le(e^{a m/N^2}-1)C_m
\le aC_0\frac{m^2}{N^2}e^{a m/N^2}.
\tag{3.1}
$$

Also,

$$
\Lambda_m^{-1}=W_m(1-\Lambda_m^{-1})^2,
\qquad \Lambda_m^{-1}\le5^{-m},
$$

so

$$
|C_m-B_m|\le2C_0m5^{-m}.
\tag{3.2}
$$

The exact fixed-point count and the short-period estimate proved in the classical audit give, for every `m`,

$$
|B_m-mQ_m|\le2m^2\beta^m,
\qquad \beta=\sqrt\lambda/5<\vartheta.
$$

Together with `Q_m=1+O(vartheta^m)`, equations (3.1)–(3.2) imply a useful global version of the finite-window estimate:

$$
\boxed{
|D_m^{orb}-m|
\le C\frac{m^2}{N^2}e^{a m/N^2}
+C m^2\vartheta^m,
\qquad m\ge1.
}
\tag{3.3}
$$

All constants here are independent of `m` and `N`.

## 4. Full exponential weighting with a quantitative error

Fix `s>0` and take `N>=a/s`. Then

$$
e^{-2sm/N}e^{a m/N^2}\le e^{-sm/N}.
$$

Multiplying (3.3) by `N^{-2}e^{-2sm/N}` and summing gives

$$
\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}|D_m^{orb}-m|
\le\frac{C}{N^4}\sum_{m\ge1}m^2e^{-sm/N}
+\frac{C}{N^2}\sum_{m\ge1}m^2\vartheta^m.
$$

The identity `sum m^2 r^m=r(1+r)/(1-r)^3` shows that the first term is `O_s(N^{-1})`; the second is `O(N^{-2})`. The main sum is explicit:

$$
\frac1{N^2}\sum_{m\ge1}m e^{-2sm/N}
=\frac{1}{4N^2\sinh^2(s/N)}
=\frac1{4s^2}+O_s(N^{-2}).
$$

Consequently,

$$
\boxed{
\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}D_m^{orb}
=\frac1{4s^2}+O_s(N^{-1}).
}
\tag{4.1}
$$

This proves, and strengthens, the source's diagonal limit. The constants can be taken uniform for `s` in a fixed compact subset of `(0,infinity)`.

The separate tail estimate in the source is valid as well. If `M=floor(BN)+1` and `r=e^{-s/N}`, then

$$
\sum_{m\ge M}m r^m
=r^M\left(\frac{M}{1-r}+\frac{r}{(1-r)^2}\right).
$$

After division by `N^2`, this is bounded by `C_s(B+1)e^{-sB}` uniformly over sufficiently large `N`. It is a uniform tail estimate for the same-orbit sum only.

The exact finite-dimensional CUE reference sum, if used merely as a reference quantity, is

$$
\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}\min(m,N)
=\frac{1-e^{-2s}}{4N^2\sinh^2(s/N)}
=\frac{1-e^{-2s}}{4s^2}+O_s(N^{-2}).
\tag{4.2}
$$

Indeed, `sum min(m,N)r^m=r(1-r^N)/(1-r)^2`.

Using (4.1), the geometric trace error, and `O_m=|P_m|^2-D_m^{orb}`, the final identity of the source strengthens to

$$
\boxed{
\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}|p_{m,N}|^2
-\frac{1-e^{-2s}}{4s^2}
=\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}\mathcal O_{m,N}
+\frac{e^{-2s}}{4s^2}+O_s(N^{-1}).
}
\tag{4.3}
$$

For each fixed `s` and sufficiently large `N`, these signed different-orbit sums are absolutely convergent after grouping by `m`, since both `|P_m|^2` and `D_m^{orb}` have summable exponential majorants. This does not make their tails uniform in `N`.

In particular, unitarity alone bounds the normalized full quantum tail only by a constant times `N e^{-2sB}`. No interchange of the `N -> infinity` and `B -> infinity` limits for that full tail has been proved. The target limit `-e^{-2s}/(4s^2)` for the weighted different-orbit sum remains unproved.

## 5. A bounded nonlinear functional from the dynamical resolvent

Here is a consequence that does not require a moment expansion or a quadratic tail estimate.

Let `F` be a fixed nonnegative function in `C_c^infinity(R)`, and write

$$
H_F=\int_{\mathbb R}F(x)\,dx,
\qquad
F_N(t)=\sum_{\ell\in\mathbb Z}F(N(t+\ell)).
$$

The true local point statistic is

$$
L_N(F,\alpha)
=\sum_{j=1}^N F_N(\theta_j-\alpha)
=\langle F,\Xi_{N,\alpha}\rangle\ge0.
$$

Its shift-averaged bounded Laplace functional is

$$
\mathscr L_N(F)=\int_0^1e^{-L_N(F,\alpha)}\,d\alpha.
\tag{5.1}
$$

Fix any `s>0`, not necessarily bounded away from zero as `N` varies, and set `r=e^{-s/N}`. Define real functions on the circle

$$
\rho^Q_{N,s}(t)
=2\operatorname{Re}R_N(re^{-2\pi it})-1,
\qquad
\rho^Z_{N,s}(t)
=2\operatorname{Re}\mathcal R_N(re^{-2\pi it})-1.
$$

The first is a positive normalized spectral smoothing:

$$
\rho^Q_{N,s}(t)
=\frac1N\sum_{j=1}^N P_r(t-\theta_j),
\qquad
P_r(t)=\frac{1-r^2}{1-2r\cos(2\pi t)+r^2}.
\tag{5.2}
$$

The Poisson kernel has integral one. By (2.2), uniformly in `t`, `s>0`, and sufficiently large `N`,

$$
|\rho^Z_{N,s}(t)-\rho^Q_{N,s}(t)|
\le\frac{4q}{N(1-q)}.
\tag{5.3}
$$

Set

$$
L^Q_{N,s}(F,\alpha)
=N\int_0^1F_N(t-\alpha)\rho^Q_{N,s}(t)\,dt,
$$

$$
L^Z_{N,s}(F,\alpha)
=N\int_0^1F_N(t-\alpha)\rho^Z_{N,s}(t)\,dt.
$$

The quantum expression is nonnegative. Since `integral_0^1 F_N=H_F/N`, equation (5.3) yields the pointwise estimate

$$
\boxed{
|L^Z_{N,s}(F,\alpha)-L^Q_{N,s}(F,\alpha)|
\le\delta_{N,F},
\qquad
\delta_{N,F}=\frac{4qH_F}{N(1-q)}.
}
\tag{5.4}
$$

This bound does not depend on clustering, on `alpha`, or on the microscopic smoothing parameter `s`.

The real number `L^Z` may be slightly negative, but never below `-delta`. To obtain an exactly bounded dynamical functional, define

$$
\mathscr L^Z_{N,s}(F)
=\int_0^1
\exp\bigl(-\max\{L^Z_{N,s}(F,\alpha),0\}\bigr)\,d\alpha
\in[0,1].
\tag{5.5}
$$

Projection onto `[0,infinity)` is one-Lipschitz, and `exp(-x)` is one-Lipschitz there. Thus (5.4) proves

$$
\left|
\mathscr L^Z_{N,s}(F)
-\int_0^1e^{-L^Q_{N,s}(F,\alpha)}\,d\alpha
\right|\le\delta_{N,F}.
\tag{5.6}
$$

If the positive part is omitted, the unmodified dynamical exponential is bounded above by `exp(delta)`, and the error instead is at most `delta exp(delta)`. No positivity of a dynamical spectral density is assumed.

## 6. Exact real-line smoothing and removal of the regulator

The smoothing in the previous section has an exact unfolded description. Define the Cauchy kernel

$$
\kappa_s(x)=\frac{2s}{s^2+4\pi^2x^2}.
\tag{6.1}
$$

It is nonnegative, has integral one, and under the Fourier convention `hat f(xi)=integral f(x)e^{-2pi i xi x}dx`,

$$
\widehat\kappa_s(\xi)=e^{-s|\xi|}.
\tag{6.2}
$$

For example, this follows by integrating the rational kernel with poles at `plus/minus i s/(2pi)` in the half-plane selected by the sign of `xi`; at zero the integral is one directly.

The periodic function

$$
N\sum_{\ell\in\mathbb Z}\kappa_s(N(t+\ell))
$$

has Fourier coefficient `exp(-s|m|/N)=r^{|m|}`. These are exactly the Fourier coefficients of `P_r`. Consequently,

$$
P_r*F_N=(\kappa_s*F)_N.
\tag{6.3}
$$

The normalizations in (5.2) now give, exactly,

$$
L^Q_{N,s}(F,\alpha)
=L_N(\kappa_s*F,\alpha).
\tag{6.4}
$$

Although `kappa_s*F` is not compactly supported, it is nonnegative and integrable. Its periodization and all averages here are justified by Tonelli's theorem.

The exact intensity identity for uniform shift is

$$
\int_0^1L_N(g,\alpha)\,d\alpha=\int_{\mathbb R}g
$$

for nonnegative integrable `g`. Applying it to the absolute difference of two tests gives

$$
\int_0^1
|L_N(F,\alpha)-L_N(\kappa_s*F,\alpha)|\,d\alpha
\le\|F-\kappa_s*F\|_1.
$$

Both statistics are nonnegative, so the same bound holds for the difference of their Laplace functionals. Combining it with (5.6) proves the nonlinear stability estimate

$$
\boxed{
|\mathscr L_N(F)-\mathscr L^Z_{N,s}(F)|
\le\|F-\kappa_s*F\|_1
+\frac{4q\|F\|_1}{N(1-q)}.
}
\tag{6.5}
$$

The kernels `kappa_s` form an approximate identity as `s -> 0`, so the first error tends to zero. This can be checked directly from

$$
\|F-\kappa_s*F\|_1
\le\int\kappa_s(y)\|F(\cdot-y)-F\|_1\,dy,
$$

using translation continuity in `L^1`, the mass-one property, and the fact that the mass outside any fixed neighborhood of zero tends to zero.

The estimate is uniform in `N`. Therefore any positive sequence `s_N -> 0` is allowed in (6.5). This statement requires neither an eigenvalue-spacing bound nor uniform integrability of a quadratic spectral statistic. It concerns bounded exponentials of nonnegative linear statistics.

The outcome is a controlled nonlinear reduction to the dynamical resolvent. The angular average on the right has not been computed. It remains an average for the same deterministic family, not an average over random matrices.

## 7. A direct unsmoothed form

For the smooth compactly supported test in Section 5, a direct version is also available. Define the grouped signed Fourier-orbit expression

$$
X_{N,F}(\alpha)
=H_F+
\frac2N\operatorname{Re}\sum_{m\ge1}
\widehat F(m/N)\mathcal P_{m,N}e^{-2\pi im\alpha}.
\tag{7.1}
$$

For each fixed `N`, the series converges absolutely and uniformly in `alpha`: use the rapid decay of `hat F` and (2.3). The exact Fourier series of the periodization gives

$$
L_N(F,\alpha)
=H_F+
\frac2N\operatorname{Re}\sum_{m\ge1}
\widehat F(m/N)p_{m,N}e^{-2\pi im\alpha}.
$$

Since `|hat F(xi)|<=H_F`, the all-time trace error proves

$$
|X_{N,F}(\alpha)-L_N(F,\alpha)|
\le\frac{4H_F}{N}\sum_{m\ge1}q^m
=\delta_{N,F}.
\tag{7.2}
$$

Hence

$$
\boxed{
\left|\mathscr L_N(F)-
\int_0^1e^{-\max\{X_{N,F}(\alpha),0\}}\,d\alpha\right|
\le\frac{4q\|F\|_1}{N(1-q)}.
}
\tag{7.3}
$$

This formula avoids both a moment expansion and a smoothing limit. It supplies no estimate of the displayed nonlinear angular average.

The grouping by period in (7.1) is essential. Absolute convergence follows from the already summed bound `|P_m|<=N+2q^m`; it does not justify replacing this by the sum of absolute values of individual periodic-orbit contributions and then interchanging all orbit sums with the infinite sum over `m`.

## 8. Microscopic balanced determinant ratios

The analytic factor has one further useful nonlinear stability property. Fix a compact set of complex unfolded coordinates and let

$$
z_{N,\alpha}(w)=e^{-2\pi i(\alpha+w/N)}.
$$

For bounded `w` and sufficiently large `N`, these points lie in one fixed subdisk of `|z|<q^{-1}`. A uniform derivative bound for `G_N` gives

$$
G_N(z_{N,\alpha}(w))-G_N(z_{N,\alpha}(v))
=O\bigl(|w-v|/N\bigr)
$$

uniformly in `alpha`. Thus, away from vanishing denominators,

$$
\frac{\mathcal Z_N(z(w))/\mathcal Z_N(z(v))}
{D_N(z(w))/D_N(z(v))}
=1+O\bigl(|w-v|/N\bigr).
\tag{8.1}
$$

This is a relative comparison and remains valid when the individual ratios are large. The common zeros and poles are interpreted meromorphically. A fixed product of such ratios has the analogous estimate. More generally, any fixed balanced product of determinant factors within a bounded microscopic neighborhood cancels the constant analytic factor and leaves a multiplicative `1+O(N^{-1})` correction.

This permits transfer of a separately established local determinant-ratio result between the quantum and dynamical descriptions. No such distributional result is supplied by (8.1) itself.

## 9. Why the zero-free correction alone cannot determine the Laplace limit

The uniform zero-free factor controls the difference of two descriptions of the same zeros. It is not, by itself, a restriction on how those zeros are arranged at scale `1/N`.

The countermodels in `audit_classical.md` make this limitation quantitative. Along odd squares `N=M^2`, take `M` nearly equally spaced clusters of `M` eigenvalues, with distinct generic perturbations of size at most `N^{-4}`. Their traces are arbitrarily small for `m=O(log N)`. For larger `m`, the trivial bound `|p_m|<=N` shows that, for all sufficiently large `N`, even the growth estimate

$$
|p_m|\le[\sqrt\lambda(1.0002)]^m
$$

holds for every positive `m`. Set `P_m=p_m`, `E_m=0`. Then `G_N=0`, and every determinant-continuation and correction estimate in Sections 1–2 holds exactly.

Nevertheless, for a fixed compactly supported test `F`, a uniformly shifted microscopic window meets one of these spectral clusters with probability `O(M/N)=O(N^{-1/2})`. Outside that event the statistic is zero. Therefore its bounded Laplace functional tends to one. The perturbations may be chosen to give simple eigenvalues, nonzero power traces, and no exact scalar returns.

These examples are not examples of the specified near-cat quantization and do not disprove its conjectured limit. They show that the abstract factorization, the analytic correction bounds, and those qualitative finite-dimensional facts cannot alone determine that limit. A further estimate using the particular dynamical phase information is required.

## Final audit conclusion

The determinant continuation and microscopic resolvent comparison are established exactly from the all-time trace remainder. The same-orbit exponentially weighted limit strengthens to `1/(4s^2)+O_s(N^{-1})`, with no unjustified tail interchange.

The bounded nonlinear estimates (6.5) and (7.3) are additional unconditional comparisons for the original deterministic family. They provide a route to studying its Laplace functional directly through the complete dynamical trace data, with an explicit uniform error and without assuming moment or clustering bounds. They do not compute that nonlinear average and do not settle `H_diag`, the test `b_*`, or Sine_2.
