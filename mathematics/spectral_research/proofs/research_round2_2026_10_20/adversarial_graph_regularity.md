> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_graph_regularity.md`. Embedded SHA256: `3986d215958f6046d4781d1282d2ea92d08c4f68ecba8df275a4a2638d576dcf`.
> [Thematic guide](../../topics/closure.md).

# A precise regularity limitation of the normalized graph construction

Date: 20 October 2026. This is a new auxiliary counterexample, not a counterexample to the given matrix family, H_diag, or the audited all-time trace formula.

## Statement

The following implication is false:

> A trace-class operator cocycle K(x) is analytic in the torus variable x and uniformly within 10^{-4} of K_G; therefore the scalar γ(x) produced by the globally normalized contracting graph is analytic, or even C¹, in x.

Here K_G is exactly the Gaussian reference operator from the all-time construction, with eigenvalues 1,ρ,ρ²,…, ρ=(3+2√2)^{-1}. The counterexample satisfies that same numerical neighborhood condition and uses the same base cat map L. It only tests what follows from the graph argument itself. Additional special structure of the actual propagator could still give more regularity, but that would need a separate proof.

## 1. An analytic cocycle whose right graph is not C¹

Let e_0,e_1 be the first two normalized real eigenvectors of K_G. Write

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\quad
\lambda=3+2\sqrt2,\quad\rho=\lambda^{-1},\quad k=(1,0).
$$

For ε=10^{-6}, define

$$
K(x)=K_G+\varepsilon\cos(2\pi k\cdot x)\,e_1e_0^*.
$$

This is an analytic periodic family of trace-class operators, and
sup_x||K(x)−K_G||_1≤ε. Its normalized invariant right section is

$$
v(x)=e_0+f(x)e_1,
\qquad
f(x)=\varepsilon\sum_{n\ge1}\rho^{n-1}
\cos(2\pi k\cdot L^{-n}x).
$$

The series converges uniformly and ||f||∞≤ε/(1−ρ). Direct substitution gives

$$
f(Lx)=\varepsilon\cos(2\pi k\cdot x)+\rho f(x),
\qquad K(x)v(x)=v(Lx).
$$

Thus v is exactly the graph selected by the contraction, and its scalar γ is 1 in this normalization.

Nevertheless, f is not C¹. Put k_n=(L^{-T})^n k. These are distinct positive integer vectors and

$$
(k_n)_q=\frac{\lambda^n+\rho^n}{2},
\qquad
\widehat f(k_n)=\frac{\varepsilon}{2}\rho^{n-1}.
$$

If ∂_q f were continuous, its Fourier coefficients would tend to zero as |k_n|→∞. Their actual values, determined distributionally from the uniformly convergent Fourier series, would be

$$
2\pi i(k_n)_q\widehat f(k_n)
=\pi i\varepsilon\rho^{n-1}
\frac{\lambda^n+\rho^n}{2}
\longrightarrow\frac{\pi i\varepsilon\lambda}{2}\ne0.
$$

This contradicts the vanishing of Fourier coefficients of a continuous function. That vanishing follows, for example, by uniform approximation by trigonometric polynomials and the bound of each Fourier coefficient by the L¹ norm of the approximation error. Therefore f is not C¹.

The obstruction is exactly the borderline product ρλ=1. Decay of past graph contributions is canceled by growth of their differentiated base frequencies.

## 2. A constant rotation makes the normalized scalar itself non-C¹

The preceding example alone only disproves C¹ regularity of the section, because its scalar happened to be constant. A constant change of basis gives the stronger assertion for γ.

Let θ=10^{-6}, c=cos θ, s=sin θ, and let S be the real unitary rotation

$$
Se_0=ce_0+se_1,\qquad Se_1=-se_0+ce_1,
$$

equal to the identity on their orthogonal complement. Set

$$
K'(x)=SK(x)S^{-1}.
$$

The trace-norm difference from K_G obeys

$$
\|K'(x)-K_G\|_1
\le2(1-\rho)|\sin\theta|+\varepsilon<3\cdot10^{-6}<10^{-4}.
$$

To see the first term directly, on span(e_0,e_1) the difference of the two rotated diagonal matrices has eigenvalues ±(1−ρ)sin θ; all other eigenvalues are zero. The perturbation term is rank one of norm at most ε.

Write g(x)=e_0^*Sv(x)=c−sf(x). Since |f|≤ε/(1−ρ), g is positive and bounded away from zero. The globally normalized invariant section is

$$
v'(x)=\frac{Sv(x)}{g(x)}
=e_0+\frac{s+cf(x)}{c-sf(x)}e_1.
$$

Its transverse component has norm below 3·10^{-6}, so it lies in the same contraction ball used in the all-time proof. Uniqueness of that normalized graph therefore identifies it with the section selected by the graph transform. Its scalar is

$$
\gamma'(x)=\frac{g(Lx)}{g(x)}.
$$

Using the recurrence for f gives

$$
\gamma'(x)-\rho
=\frac{c(1-\rho)-s\varepsilon\cos(2\pi k\cdot x)}{c-sf(x)}.
$$

The numerator and denominator are positive and bounded away from zero. If γ' were C¹, then

$$
f(x)=\frac1s\left[
c-\frac{c(1-\rho)-s\varepsilon\cos(2\pi k\cdot x)}{\gamma'(x)-\rho}
\right]
$$

would be C¹, contradicting Section 1. Thus the normalized scalar is not C¹ although K' is analytic in x and arbitrarily close to K_G.

## 3. What this does and does not obstruct

The example can be made constant in the real parameter h, so uniform finite h-jets do not repair the missing base regularity. It invalidates an automatic inference from the graph estimates to analytic scalar transfer machinery.

Here γ' is a continuous multiplicative coboundary: every periodic product of γ' is exactly 1. This is deliberate. It shows that regularity of a chosen scalar normalization can be worse than that of its periodic data. It does not rule out a separate construction of a better gauge for a particular propagator, and it does not imply that the actual γ_h has this pathology.

The all-time trace proof only requires continuity in the base and uniform finite h-jets, so none of its established conclusions is damaged by this example.
