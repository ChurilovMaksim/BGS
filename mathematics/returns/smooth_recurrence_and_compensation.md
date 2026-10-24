---
title: "Smooth Green--Kubo recurrence and compensated residual kicks"
author: "BGS research programme"
date: "5 September 2026"
---

# Status and conventions

This is a project proof, not an external referee certificate, a priority claim,
or a full Lean formalization. The limits concern fixed multiples of the
arithmetic period. They do not concern fixed nonzero classical perturbations
or positive microscopic BGS universality. Classical Green--Kubo variance,
its Fourier-orbit representation, and the second-order residual-perturbation
mechanism have prior literature, discussed at the end.

Fix
$$
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\quad
 \alpha=1+\sqrt2,\quad\lambda=\alpha^2,\quad
 N+F\sqrt2=\alpha^K,
$$
where K tends through odd primes. Thus N is odd, possibly composite,
$N^2-2F^2=-1$, and $N\asymp\lambda^{K/2}$. The phase-normalized cat
quantization in the existing Pell construction satisfies
$U_0^K=I$ and $U_0W_N(v)U_0^*=W_N(Tv)$. Here
$$
 W_N(a,b)\psi(x)=e_N(a(x-b/2))\psi(x-b)
$$
uses the inverse of 2 modulo N. To quantize a fixed classical Fourier symbol,
use the physical convention
$$
 W_N^{\rm ph}(a,b)=(-1)^{ab}W_N(a,b),\qquad
 A_N(f)=\sum_{v\in\mathbb Z^2}\widehat f(v)W_N^{\rm ph}(v).
$$
For integer indices, including unreduced indices, it obeys
$$
 W_N^{\rm ph}(v)W_N^{\rm ph}(w)
 =e^{\pi i\det(v,w)/N}W_N^{\rm ph}(v+w).
$$
Since $T=I$ modulo 2, the physical sign is constant along a T orbit and
Egorov covariance remains exact. All full-space traces below are normalized
by N. For inversion-even symbols the corresponding statements also hold
on the entire odd subspace, normalized by $(N-1)/2$. A general real symbol
need not preserve this parity subspace.

Define the classical action on symbols by $\mathcal C f(x)=f(T^{\mathsf T}x)$;
then $\mathcal C$ acts on Fourier indices by T. This convention avoids an
implicit transpose change.

# 1. Smooth observable theorem

Let f be real and mean zero. Suppose
$$
 |\widehat f(v)|\leq C_f(1+|v|)^{-p},\qquad p>5.
$$
In particular every $C^6$ observable satisfies a suitable bound with p=6.
For the oriented T orbits O of nonzero integral frequencies put
$$
 \sigma_f^2=\sum_O\left|\sum_{v\in O}\widehat f(v)\right|^2.
$$
The sum is finite, since the Fourier series is absolutely summable. It is
also the absolutely convergent Green--Kubo sum
$$
 \sigma_f^2=\sum_{n\in\mathbb Z}\int_{\mathbb T^2}f(x)
                                      f((T^{\mathsf T})^n x)\,dx.
$$
Indeed Fourier orthogonality groups the double sum by oriented orbits;
its sum of absolute values is at most $\|\widehat f\|_1^2$.

**Theorem 1.** For every fixed real tau and integer m,
$$
 \frac1N\operatorname{Tr}
       \left(e^{i\tau A_N(f)/\sqrt K}U_0\right)^{mK}
       \longrightarrow e^{-m^2\tau^2\sigma_f^2/2}.             \tag{1}
$$
The empirical spectrum of the K-th power therefore tends to the wrapped
normal law of variance $\tau^2\sigma_f^2$. Zero variance means the point
mass at 1. The odd-space version requires inversion-even f.

Here is the full approximation argument, including the dependence on Fourier
support. A finite-support moment theorem by itself is insufficient for (1).

## 1.1. Finite alphabets and structural relations

Identify v=(a,b) with $\beta_v=b+\sqrt2 a$ in $\mathbb Z[\sqrt2]$.
Then $\beta_{Tv}=\lambda\beta_v$. Its nonzero algebraic norm is an integer.
Take S representatives of distinct signed T orbits, and let M>=1 bound the
absolute values of both embeddings of their beta values.

For a signed m-atom modular zero relation, cancel opposite identical atoms
and rotate time labels across a largest gap of the cyclic set of K times.
There are at most m occupied times. The rotated algebraic sum P has degree
at most $K-\lceil K/m\rceil$. Modular vector vanishing implies
$P(\lambda)\in N\mathbb Z[\sqrt2]$. A nonzero norm would have magnitude
at least $N^2$, whereas
$$
 |\operatorname{Norm}P(\lambda)|
       \leq m^2M^2\lambda^{K-\lceil K/m\rceil}.
$$
Thus it lifts to a characteristic-zero relation whenever
$$
 \lambda^{\lceil K/m\rceil}(1-\lambda^{-K})^2>4m^2M^2.        \tag{2}
$$
No inversion of the individual beta values is required.

A gap B with $\lambda^B>m^2M^2$ splits such a relation into two separately
vanishing components. To see this, write
$P=P_{\rm low}+\lambda^{a+B}P_{\rm high}$, with the lower exponents at
most a. If the high part is nonzero, its integer norm and the conjugate
bound mM imply $|P_{\rm high}|\geq1/(mM)$. Cancellation by the low part,
of magnitude at most $mM\lambda^a$, is then impossible. Iteration leaves
components of bounded width. A two-atom component must pair the same signed
orbit at the same relative time; distinct representatives do not admit such
a two-atom relation.

For four atoms choose $\lambda^B>16M^2$ and put D=3B. Once (2) holds for
m=4, every nonzero signed distinct-time pair key has multiplicity at most
$$
 J=[2S(2D+1)]^2.                                               \tag{3}
$$
In a nontrivial collision of two pairs, cancellation leaves one four-atom
component: a split into two two-atom components would be the identical pair.
All its cyclic time labels lie within D of an anchored atom. Each alternate
atom has at most $2S(2D+1)$ choices. This proves (3). The bound is coarse
and deliberately allows structural coincidences; it is not an injectivity
claim.

The resulting moment count gives a joint Gaussian tracial limit for the
orbit sums
$$
 Y_s=(2K)^{-1/2}\sum_{j=0}^{K-1}
                 (W_N(T^jv_s)+W_N(-T^jv_s)).
$$
A nonpaired 2r-word has at most r-1 bounded components, hence
$O_r(K^{r-1})$ assignments, while paired words have order $K^r$.
Each paired orientation contributes the covariance associated with its
Fourier coefficients. Structural triples can occur: the correct general
odd-moment error is $O_m(K^{-1/2})+O_m(K^{m/2}/N)$, not an assertion that
all odd central words vanish. For arbitrary real finite symbols use the
complex-conjugate pair of coefficients at v and -v; their pairing weight is
$2\operatorname{Re}(c\overline d)$. The full variance is the orbit-sum
formula above. Physical Weyl signs are constant on each orbit and cancel
in its covariance.

Crossing phases do not require independence. With
$$
 a_j=\max_{s,t}|e_N(\det(v_s,T^jv_t))-1|,\quad
 c_j=(K-1-2j)/(2K),\quad L=\sum_j a_j,\quad W=K\sum_j|c_j|a_j,
$$
centered Pell representatives and geometric summation give
$$
 L\leq\frac{4\pi M^2}{1-\lambda^{-K}}+\frac{2\pi M^2}{N},\qquad
 W\leq\frac{2\sqrt2\pi M^2}{1-\lambda^{-K}}+\frac{\pi M^2K}{N}.
$$
Both are below $32M^2$ for K>=3. For a fixed pairing each crossing time
difference is uniform; $|\prod z_j-1|\leq\sum|z_j-1|$ bounds the average
phase error by L times the number of crossings divided by K. This completes
the finite-alphabet Wick count. Gaussian moment determinacy and higher even
moment bounds imply convergence of its characteristic function.

## 1.2. Support-dependent normal form

For $Q=\sum_s r_s B_{v_s}$, put
$\overline Q=K^{-1}\sum_j\operatorname{Ad}_{U_0}^jQ$ and
$G=\sum_j c_j\operatorname{Ad}_{U_0}^jQ$. Then
$G-\operatorname{Ad}_{U_0}G=Q-\overline Q$. Write $l=\|r\|_1$.
Weyl orthogonality in the full normalized Hilbert--Schmidt norm and (3)
give
$$
 \|[G,\overline Q]\|_{2,N}^2
 \leq\frac{4J\|r\|_2^4}{K^4}
               \sum_{j=1}^{K-1}(K-j)j^2a_j^2
 \leq\frac{J\|r\|_2^4 L}{K}.
$$
Also $\|[G,Q]\|_{\rm op}\leq4l^2W/K$ and
$\|[Q,\overline Q]\|_{\rm op}\leq4l^2L/K$.
The two-factor Duhamel inequality
$\|e^{ixA}e^{ixD}-e^{ix(A+D)}\|\leq x^2\|[A,D]\|/2$
therefore yields
$$
 \|e^{-ixG}(e^{ixQ}U_0)e^{ixG}-e^{ix\overline Q}U_0\|_{2,N}
 \leq x^2\left[\frac{2l^2(W+L)}K+
                   \frac{\|r\|_2^2\sqrt{JL}}{2\sqrt K}\right]. \tag{4}
$$
For the odd space multiply the Hilbert--Schmidt commutator term by
$\sqrt{2N/(N-1)}$. Do not assume orthogonality of restricted Weyl matrices.
Complex-conjugate Fourier coefficients give the same estimates with their
absolute coefficient norms, up to harmless absolute factors. Estimate (4)
requires no smallness of x times the norm of G.

## 1.3. Growing cutoff and the missing tail argument

Let f_R retain frequencies of Euclidean norm at most R. The number of signed
orbit representatives is $O(R^2)$ and their embedding sizes are at most 2R.
Two frequencies in the same orbit and in this ball have relative time
$O(\log R)$: each beta embedding lies between $1/(2R)$ and 2R in magnitude.
The Euclidean norm squared of $T^t v$ is a convex function of real t,
being of the form $A\lambda^{2t}+B\lambda^{-2t}+C$ with A,B positive.
All intermediate orbit frequencies consequently remain in the ball.

Collecting coefficients along each orbit gives the exact finite decomposition
$f_R=Q_R+g_R-\mathcal Cg_R$. The representative coefficient norm is bounded
by $\|\widehat f\|_1$, while $\|\widehat g_R\|_1=O_f(\log R)$ and all
frequencies still have size O(R). A first-order gauge removes this coboundary
at a K-step cost $O_f(R^2\log^2 R/N)$ when $x=\tau/\sqrt K$.
This follows from the physical Weyl commutator bound
$\|[A_Nh,A_Nk]\|\leq(2\pi/N)\sum|v||w||\widehat h(v)\widehat k(w)|$
and two applications of Duhamel's inequality.

For Q_R, (3) gives $J=O(R^4\log^2R)$ and L,W=O(R^2). Crucially
$\|r\|_2^2\leq\|r\|_1^2=O_f(1)$, not a bound that loses an extra
factor equal to the number of species. Summing (4) over K steps costs
$$
 O_f(R^2/K+R^3\log R/\sqrt K).
$$
The discarded operator tail costs
$O_f(\sqrt K R^{2-p})$. Choose $R=K^{1/(p+1)}$. These errors vanish;
the leading comparison error is
$O_f(K^{-(p-5)/(2(p+1))}\log K)$. For p=6 this is $O_f(K^{-1/14}\log K)$.
This is a normal-form comparison rate, not a rate for the final Gaussian
characteristic-function limit.

It remains to justify a Gaussian law for the averaged growing polynomial.
For a mean-zero h supported in a radius-R ball, once the two-atom lifting
condition holds and log R=o(K), there is the exact identity
$$
 \frac1N\operatorname{Tr}
       \left(\sqrt K\,\overline{A_N(h)}\right)^2
           =\sigma_h^2\leq\|\widehat h\|_1^2.                 \tag{5}
$$
Indeed a modular pair collision lifts to an actual signed orbit relation.
The true relative time is O(log R), unique modulo K, and gives exactly K
time pairs. Physical signs agree on that orbit. Fourier orthogonality then
gives exactly the orbit-sum variance. For odd h use the full-space positive
second moment to bound the restriction by $2N/(N-1)$; exact restricted
orthogonality is unnecessary.

Fix a cutoff L independently of K and apply (5) to h=f_R-f_L. The normalized
Hilbert--Schmidt distance of the two scaled averages is bounded by
$\|\widehat{f-f_L}\|_1$, uniformly for large K. Duhamel bounds the difference
of their characteristic functions by the same quantity times the fixed
Fourier argument. First take K to infinity using the finite-alphabet theorem
for f_L, then L to infinity. Absolute Fourier summability gives
$\sigma_{f_L}^2\to\sigma_f^2$. This proves (1) without applying fixed-alphabet
moment constants to a growing alphabet. Integer Fourier coefficients determine
the limiting measure on the unit circle.

# 2. General residual crossover, with covariance

Let g be real C7, let $d=\mathcal Cg$, and let f be real mean-zero C6. Set
$$
 r_g=\frac1{4\pi}\{g,d\},\qquad
 A=A_N(g),\ D=A_N(d),\ F=A_N(f),\ R=A_N(r_g),
$$
where $\{g,d\}=\partial_1g\partial_2d-\partial_2g\partial_1d$.
The symbol r_g is real, mean zero and C6. Consider the single exponential
$$
 V_{\varepsilon,\eta}=e^{i[\varepsilon(A-D)+\eta F]}U_0.
$$

**Theorem 2.** If $a_K=\sqrt K\eta_K\to a$ and
$t_K=\sqrt K\varepsilon_K^2/N\to t\geq0$, then
$$
 \frac1N\operatorname{Tr}V_{\varepsilon_K,\eta_K}^{mK}
           \longrightarrow e^{-m^2\sigma_{a f+t r_g}^2/2}.     \tag{6}
$$
In particular the variance is
$a^2\sigma_f^2+2at\Gamma(f,r_g)+t^2\sigma_{r_g}^2$, where Gamma is the
polarized Green--Kubo form. It need not have zero mixed term. The odd-space
version requires inversion-even f and g.

For explicit finite control write
$M_j(h)=\sum_v |v|^j|\widehat h(v)|$. All moments used below are finite.
The Fourier series of r_g is
$$
 \widehat r_g(k)=-\pi\sum_{v+w=k}\det(v,w)\widehat g(v)\widehat d(w).
$$
The physical Weyl product and $|\sin x-x|\leq|x|^3/6$ imply
$$
 \|[A,D]+2iR/N\|\leq\frac{\pi^3M_3(g)M_3(d)}{3N^3}.         \tag{7}
$$
Set $H_*=M_2(g)M_1(d)+M_1(g)M_2(d)$,
$L_A=4\pi^2M_1(g)H_*$, and $L_D=4\pi^2M_1(d)H_*$.
Two exact sine bounds give
$\|[A,[A,D]]\|\leq L_A/N^2$ and
$\|[D,[A,D]]\|\leq L_D/N^2$.

For any finite Hermitian A,D and real epsilon the uniform loop inequality is
$$
 \|e^{-i\varepsilon A}e^{i\varepsilon(A-D)}e^{i\varepsilon D}
                       -e^{-\varepsilon^2[A,D]/2}\|
 \leq |\varepsilon|^3
       (\|[A,[A,D]]\|/2+\|[D,[A,D]]\|/6).
$$
For completeness, with Q=[A,D], differentiation of the three-factor loop
has logarithmic derivative
$-\int_0^u\operatorname{Ad}_{e^{-iuA}e^{iv(A-D)}}Q\,dv$.
Compare it with -uQ, the logarithmic derivative of $e^{-u^2Q/2}$.
The conjugation difference is at most
$u\|[A,Q]\|+v\|[A-D,Q]\|$. Integrate over $0\leq v\leq u\leq|\varepsilon|$
and use the triangle inequality. Negative epsilon is covered by replacing
A,D by their negatives. No small-generator hypothesis is used.

Define $C_3=L_A/2+L_D/6$ and $C_2=\pi^3M_3(g)M_3(d)/6$.
Splitting the single mixed exponential, applying this loop estimate,
conjugating F and joining the two effective exponentials give
$$
 \begin{split}
 &\|e^{-i\varepsilon A}V_{\varepsilon,\eta}e^{i\varepsilon A}
                   -e^{i[\eta F+\varepsilon^2R/N]}U_0\|\leq E_N,\\
 E_N={}&C_3|\varepsilon|^3/N^2+C_2\varepsilon^2/N^3\\
 &+\pi M_1(f)(3M_1(g)+M_1(d))|\varepsilon\eta|/N\\
 &+\pi M_1(f)M_1(r_g)|\eta|\varepsilon^2/N^2.                 \tag{8}
 \end{split}
$$
Each step uses a unitarily invariant norm or an operator commutator bound;
there is no expansion whose validity requires small epsilon. If a_K,t_K
are bounded, $KE_N\to0$ (the leading residual term is
$O(K^{1/4}/\sqrt N)$). The effective symbol is
$(a_K f+t_Kr_g)/\sqrt K$. The proof of Theorem 1 is uniform on this bounded
two-dimensional coefficient family. At a fixed Fourier cutoff its Gaussian
variance converges as a_K,t_K converge; the uniform tail argument then applies.
One must not use the invalid crude bound $\sqrt K|a_K-a|$ to handle varying
parameters. This proves (6).

For $g(x)=2\cos(2\pi x_1)$, one obtains exactly
$r_g=4\pi(B_{(2,4)}-B_{(4,4)})$ at the level of classical symbols and
$\sigma_{r_g}^2=64\pi^2$. This recovers the earlier cosine residual scale.
Taking f=r_g instead gives variance $(a+t)^2\sigma_{r_g}^2$ and a genuine
cancellation line a=-t. Thus a sum-of-independent-variances rule is false
for general smooth symbols.

# 3. Explicit compensation and a wider pinning range

Define the different, explicitly compensated family
$$
 V^{\rm comp}_{\varepsilon}
       =e^{i[\varepsilon(A-D)-\varepsilon^2 R/N]}U_0.
$$

**Theorem 3.** For every real epsilon,
$$
 \|e^{-i\varepsilon A}V^{\rm comp}_{\varepsilon}e^{i\varepsilon A}-U_0\|
 \leq C_g|\varepsilon|^3/N^2+D_g\varepsilon^2/N^3,             \tag{9}
$$
where
$C_g=C_3+\pi M_1(r_g)(3M_1(g)+M_1(d))$ and $D_g=C_2$.

In (8) take F=R and eta=-epsilon squared/N. The final two effective
exponentials cancel exactly, so their commutator error is zero, not the
coarse last term in (8). The remaining terms give (9).

If
$$
 |\varepsilon_K|=o(N^{2/3}K^{-1/3}),                           \tag{10}
$$
then K times the right side of (9) tends to zero. Thus all fixed recurrence
traces tend to one. Moreover globally unfolded nearest-neighbour spacings
of the original compensated propagator tend weakly to the point mass at zero,
and every fixed positive microscopic close-pair count diverges. These claims
hold on the full space, or on the odd space when g is inversion-even.

To justify the microscopic step, normal-matrix eigenvalue matching bounds the
RMS chord distance by the normalized Hilbert--Schmidt distance, hence by the
operator norm in (9). Circle distance in R/Z is at most one quarter of chord
distance. If a is RMS distance to the K-root lattice, then Ka tends to zero
and K/dimension tends to zero. The finite concentration inequalities
$$
 d^{-1}\#\{S_l>x\}\leq2a^2/w^2+K/d+2Kw/x,
$$
$$
 R_2(x)\geq(1-a^2/w^2)_+^2/(K/d+2Kw/x)-1
$$
apply for $0<w<1/(2K)$. Their proofs count points in K disjoint arcs and
apply Cauchy--Schwarz to cell occupancies. Taking
$w=(Ka)^{2/3}/K$ for the first and w=2a for the second proves the claims;
a=0 is covered directly by at most K nonzero gaps. Multiplicities are retained.
The mean spacing remains one; weak convergence does not preserve that mean
without uniform integrability.

The larger scale (10) belongs to the compensated family, not to the unchanged
residual kick. In classical action notation, epsilon=N kappa, its symbol is
$\kappa(g-\mathcal Cg)-\kappa^2r_g$, and kappa still tends to zero. Neither
(9) nor (10) supplies fixed-strength BGS or Heisenberg-scale joint traces.

# 4. Verification and prior work

The proofs above are analytic. Exact finite Fourier-tail tests use rational
coefficients and integer physical Weyl signs; writing a negative power of
Python's integer -1 would silently introduce floats and must be avoided.
Independent original-coordinate and quadratic-ring pair enumerations test
structural multiplicities. Finite Hermitian operator tests retain nonzero
mixed third moments and deliberately correlated examples. They do not force
finite spectra to equal their limiting Gaussian distributions.

The finite integer telescoping and parity lemmas in the continuation's Lean
source have a narrower scope. They do not formalize Duhamel, the Fourier-tail
argument, Gaussian limits or microscopic consequences. Compilation and
execution status require actual logs, not source inspection.

Guy Cohen and Jean-Pierre Conze, *Central limit theorem for commutative
semigroups of toral endomorphisms*, arXiv:1304.4556, provide classical
variance and coboundary precedents. Their classical theorem is not a theorem
about the finite quantum propagators here.

Tomaz Prosen and Marko Znidaric, *Quantum Freeze of Fidelity Decay for Chaotic
Dynamics*, Physical Review Letters 94 (2005), 044101,
arXiv:quant-ph/0401142, provide direct precedent for residual perturbations
and second-order commutator dynamics. We do not claim to invent that mechanism.

Greg Kuperberg, *A tracial quantum central limit theorem*, Transactions of
the AMS 357 (2005), 459--471, arXiv:math-ph/0202035, is relevant tracial
precedent. Its independence hypotheses are not silently imposed on this
deterministic array. Commutator-sensitive product bounds are standard matrix
analysis, not a newly invented general Trotter theory.

A full priority review remains unfinished. These project proofs should be
externally checked before any novelty or publication-level significance is
asserted.
