> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_weyl_polynomial_obstruction.md`. Embedded SHA256: `4d7a730152f3c051b250d1f512877baedf87a22337eefe6ecb794444a27215e3`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/approximation.md).

# Independent audit: the original kick and sublinear polynomial degree

21 October 2026. Reviewer: signed-return branch, independent of the
Weyl branch that wrote the proof.

**Verdict: the theorem follows from the proof as written. No mathematical
defect found.** This audit concerns the precisely stated bandwidth and
polynomial approximation theorem for the original kick. It does not
upgrade that theorem to any conclusion about $H_{\rm diag}$.

The entire source was read, including all quantization conventions,
the analytic zero-set argument, both norm infima, and the scope
limitations:

- Source: `research_round8_2026_10_21/r8_weyl_sublinear_polynomial_obstruction.md`.
- Frozen SHA-256: `32a014694531ea01284a146334c223a22686de457970bb39e4a5fa39c109c618`.

The checks below are direct symbolic/mathematical checks, not numerical
evidence for an asymptotic limit.

## 1. Modular half, symbol shift, and Weyl multiplication

Taking $2^{-1}=(N+1)/2$ for odd $N$, the phase in the original
$T_N(l,k)$ factors into the ordinary-half phase and $(-1)^{kl}$.
The compensating definition
$\widetilde W_N(k,l)=(-1)^{kl}T_N(l,k)$ therefore gives exactly
$$
 \widetilde W_N(k,l)\psi(x)
 =e^{2\pi ik(x+l/2)/N}\psi(x+l).
$$
This is valid for every integer label. It is not necessary for
$\widetilde W_N$ to be periodic in its labels: retaining all
integer labels preserves the signs when a label is shifted by $N$.

Multiplying two such expressions produces the extra exponent
$\pi i(lk'-kl')/N$. Thus the product law and the sign convention
$\omega((k,l),(k',l'))=lk'-kl'$ in source (3.2) are correct.

Since $W_N(k,l)=(-1)^{kl}\widetilde W_N(k,l)$, the symbol
coefficients for the ordinary-half calculus acquire that same sign.
The original terms with $l=0$ do not change, and the terms with
$l=\pm1$ acquire $(-1)^k$. This is exactly
$r(q+1/2)$, with no shift of $V(q)$ and no change of the phase
$\alpha_0$. The displayed symbol is therefore the symbol of the
exact original $A_N$ for every odd dimension.

The coefficient bounds are valid even if different listed frequencies
coincide at a small dimension: they are bounds on the full-label symbol
before quantization. The original Fourier support lies in
$|k|+|l|\le9$, and the stated triangle-inequality bound is
$1+0.4+0.04+0.1+0.04=1.58<2$.

## 2. Egorov sign and fixed-time error

The commutator coefficient is
$$
 iN\big(e^{\pi i\omega/N}-e^{-\pi i\omega/N}\big)
       =-2N\sin(\pi\omega/N).
$$
For $X=(a_p,-a_q)/(2\pi)$, differentiating the two Fourier
characters gives
$$
 (a_pF_q-a_qF_p)/(2\pi)
       =-2\pi(lk'-kl')a_uF_v
$$
at their product frequency. The quantum and classical signs agree.
In particular the conjugation $E_N(s)\operatorname{Op}_N(F)E_N(s)^*$
corresponds to $F\circ\Phi_s$, as asserted, rather than to the
opposite flow.

The sine remainder is globally bounded by $|x|^3/6$, so there is
no small-label restriction in the error estimate. The finite support
of $a$ and the weighted absolute summability of the Fourier
coefficients of a smooth $F$ make its constant finite. The
suggested decay $(1+|v|^2)^{-4}$ is more than sufficient after the
cubic weight in dimension two.

For the autonomous flow, $F_s=F\circ\Phi_s$ solves
$\partial_sF_s=X\cdot\nabla F_s$. One way to check the equality
with the derivative in the initial variable is to differentiate
$\Phi_s\Phi_t=\Phi_t\Phi_s$ at $t=0$, obtaining
$D\Phi_s(z)X(z)=X(\Phi_s(z))$. The differentiated conjugation in
the proof then has exactly the stated error and integration on the
fixed compact time interval yields $O_F(N^{-2})$.

The trace-product limit is also valid for all odd dimensions. For a
fixed finite list of labels, sufficiently large $N$ rules out any
nonzero total label in $N\mathbb Z^2$; the surviving opposite
labels have phase one. Absolute Fourier approximation and the
normalized trace inequality justify passage to smooth symbols. No
prime-dimension assumption enters this argument.

## 3. Orientation and normalization of the transition measure

Direct expansion gives
$$
 \frac1N\operatorname{Tr}(D_gE_ND_hE_N^*)
 =\frac1N\sum_{x,y}g(x/N)h(y/N)|(E_N)_{xy}|^2.
$$
Using the preceding Egorov sign, its limit is
$\int g(q)h(Q_\tau(q,p))\,dq\,dp$. Thus the proposed
pushforward by $(q,p)\mapsto(q,Q_\tau(q,p))$ has the correct
coordinate order and sign. Calling the first coordinate an initial
or final position would depend on a propagator convention, but the
explicit measure formula is unambiguous and correct.

Unitarity gives total mass one. Products of one-variable Fourier
characters span all trigonometric polynomials on the product torus,
so their convergence and uniform approximation prove weak convergence
for every continuous test. This part of the proof never requires a
limit for a discontinuous or unbounded test.

## 4. A nonzero analytic displacement at the prescribed time

The coefficient of $a$ at $(0,1)$ is
$e^{-i\alpha_0}/200=(-3-4i)/1000$, of modulus $1/200$.
Differentiating in $p$ and dividing by $2\pi$ multiplies it
by $i$, so the first velocity component has the same coefficient
modulus. This supplies a specified nonzero Fourier mode of the
displacement, not a genericity claim.

The derivative constants check directly:
$$
 \|X\|_\infty\le 9\sum|\widehat a|<18,
 \qquad
 \|DX\|_{\infty\to\infty}
 \le2\pi\sum|\widehat a(v)||v|_1^2<324\pi<1100.
$$
Integration gives a displacement at most $18s$, and the first
order remainder is at most
$\int_0^\tau1100\cdot18s\,ds=9900\tau^2$.
The coefficient remainder is bounded by this uniform remainder.
Thus
$$
 |\widehat\delta(0,1)|\ge\tau/200-10000\tau^2
                             \ge\tau/400>0
$$
holds for the exact $\tau=10^{-80}$. Also
$|\delta|\le18\tau<1/2$, which is needed to turn a modular
position equality into an ordinary zero of $\delta$.

The complex strip estimates in the Picard construction are consistent:
$e^{2\pi(1/100)9}<2$, so the stated bounds $36$ and $2100$
hold. The displacement ball stays in the larger strip, and
$36\tau<\rho/2$, $2100\tau<1/2$ make it invariant and
contractive. Uniform limits of the holomorphic iterates yield a
holomorphic displacement on the smaller strip. Periodicity follows
from uniqueness and periodicity of the vector field.

The zero-set proof is sufficient without invoking a general analytic
stratification theorem. Some analytic function
$q\mapsto\partial_p^j\delta(q,0)$ is nonzero, or else analytic
continuation in $p$ would make $\delta$ identically zero. That
nonzero one-variable analytic periodic function has finitely many
zeros. Outside those finitely many values of $q$, the function of
$p$ is a nonzero analytic periodic function and has finitely many
zeros. Fubini's theorem gives a two-dimensional zero set of measure
zero. Consequently the limiting transition measure gives the
position diagonal zero mass.

## 5. Shrinking bands and both approximation infima

For every fixed $\eta>0$, the band of width $d_N$ is contained
eventually in the fixed closed strip of torus width $\eta$, since
$d_N/N\to0$. The closed-set upper bound for weak convergence
then bounds the limiting mass of the shrinking band by the limiting
measure of this fixed strip. Sending $\eta\downarrow0$ uses
continuity from above for a probability measure and the zero mass of
the diagonal. This is the correct order of limits; no uniform
convergence for an $N$-dependent indicator is presumed.

For Hilbert--Schmidt norm, entrywise orthogonality makes band
truncation the exact best approximation among all matrices with that
band support. Its normalized squared error is $1-m_{N,d_N}$.
For operator norm,
$\|C\|_{\rm HS}/\sqrt N\le\|C\|_{\rm op}$ supplies the
same limiting lower bound. The allowed zero matrix supplies the
upper bound one. This proves that the best operator approximation
error tends to one; it does not merely bound a chosen approximation.

The generator has exact cyclic bandwidth one because its shift
labels are $0,\pm1$. A product of $j$ such steps has cyclic
distance at most $j$, including paths across the coordinate wrap.
Therefore every polynomial of degree at most $d_N$ belongs to
the allowed band space. The same lower bound and the zero polynomial
give both polynomial infima. Right multiplication by the unitary
$M_N$ preserves both norms, proving the statement for the full
$U_N$ approximation.

## 6. Scope and remaining original gap

The assertion is a completed obstruction theorem for sublinear
bandwidth approximations of the exact single kick. It allows the
coefficients of the polynomial to depend arbitrarily on $N$, and
it holds along every odd dimension. It does not address degree
$cN$ with fixed $c>0$, and it does not require a proposed
method for a spectral observable to approximate the entire kick in
operator norm.

The proof does not bound the fully summed signed Heisenberg-time
trace statistic. In particular, the pair comparison
$$
 \frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
       \bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\to0
$$
does not follow from this obstruction. The source explicitly
maintains that distinction. No correction to its theorem or proof
is requested by this audit.
