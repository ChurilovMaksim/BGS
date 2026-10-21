> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_weyl_audit_uniform_shrinking_windows.md`. Embedded SHA256: `6e8c0d62252c7027c892b8d13239d80e31c9c28c844f9477a08c68fb6da54a02`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: uniform compressed shrinking windows

Date: 21 October 2026. Auditor: the independent Weyl branch of round 8.

## 1. Frozen object and verdict

The file audited in full is

`r8_return_uniform_shrinking_windows.md`

with SHA-256

`c7329595d2f77c5f14fe0e68dd28204740c7faf1d3527981f2a4a05929cc4d26`.

**Verdict:** no mathematical defect was found in the new argument,
given its explicitly identified round-7 input theorems. The uniform
shrinking-window theorem, the compressed boundary-resolvent theorem,
their stated Schur consequence, and robustness under arbitrary
vanishing operator-norm perturbations follow with the displayed
all-odd quantifiers. No microscopic spectral-statistics theorem follows
from these compressed statements alone; the file correctly states and
tests that limitation.

This is an internal independent proof audit, not publication or formal
verification. The complete proofs of all earlier round-7 results were
not re-audited from scratch here. Their four listed file hashes were
checked and agree exactly with the input table. In addition, the
classical hyperbolicity and quantization portion of the stationary
input was read directly, and the sampling, compactness, and operator
steps used in the new argument were checked independently below.

## 2. Published theorem and the product-system hypothesis

The auditor personally reopened both primary sources:

- [Xia, author's version 2, arXiv:math/0503437v2](https://arxiv.org/pdf/math/0503437v2),
  Theorem 4.2 on pages 7--8 and the standing assumptions on page 1.
- [Official journal record, DOI 10.3934/dcds.2006.15.811](https://www.aimsciences.org/article/doi/10.3934/dcds.2006.15.811).

The source indeed supplies ergodicity for the indicated smoothness,
volume preservation, and Anosov hypotheses. Compactness and
connectedness are part of its manifold setting. The publication record
agrees with the bibliographic identification in the audited file.

The original map $F_+$ is analytic, area preserving, and uniformly
hyperbolic by the named input. The direct-sum stable and unstable
bundles for $F_+\times F_+$ are continuous and invariant, and their
uniform estimates persist in a product norm. The product torus is
compact and connected and the product map preserves smooth product
volume. Therefore the theorem applies to the product itself. This is
the correct way to obtain the weak-mixing consequence used here;
single-system ergodicity alone would not have sufficed.

## 3. Product ergodicity to uniform modulation

For a mean-zero $g\in L^2(\mathbb T^2)$, the tensor
$H(x,y)=g(x)\overline{g(y)}$ belongs to $L^2(\mathbb T^4)$,
has mean zero, and obeys

$$
\langle H,(\mathcal C\otimes\mathcal C)^nH\rangle
=|\langle g,\mathcal C^ng\rangle|^2.
$$

Complex conjugation of one factor is essential and is present.
The mean ergodic assertion follows from the proved range/orthogonal-
complement identity for a unitary, without a mixing-rate hypothesis.
It gives Cesàro decay of the squared correlations.

Expanding the modulated average gives exactly

$$
\left\|T^{-1}\sum_{j=0}^{T-1}e^{-ij\theta}\mathcal C^jg\right\|^2
\le\frac{\|g\|^2}{T}
 +\frac2T\sum_{n=1}^{T-1}|\langle g,\mathcal C^ng\rangle|.
$$

The last quantity tends to zero uniformly in $\theta$, by
Cauchy--Schwarz and the squared-correlation Cesàro limit. Thus no
exchange of a phase supremum with a merely pointwise mean-ergodic
limit is being assumed. On any fixed finite-dimensional space, the
positive operator's norm is at most its trace in an orthonormal basis;
this justifies uniformity over the unit sphere of that space.

## 4. Fixed-time compactness and Fejér domination

For a fixed smooth kernel, approximation uniformly by a finite
trigonometric-polynomial kernel controls both its sampled matrix norm
and its continuous integral-operator norm by the approximation error.
For the polynomial the centered discrete Fourier embedding gives the
exact continuous finite-rank operator once $N$ exceeds the fixed
frequency support. This proves the stated compact norm limit from the
fixed-time kernel input without imposing a restriction on prime
factors of $N$.

The Fejér multiplier is normalized as the squared modulus of the
average of $T$ characters. Its zero-time coefficient is $1/T$,
and its two nonzero-time coefficients yield the factor
$(2/T)(1-n/T)\operatorname{Re}(\cdot)$. These agree with equation
(4.3) in the audited file.

For each fixed $T$, the multiplier tends uniformly to $1$ on
the shrinking central arc, independent of its rotating center. It is
nonnegative on the entire circle. The operator domination in (4.2)
is therefore a legitimate spectral-theorem inequality. It handles
closed endpoints and circular wraps. Removing the scalar coordinate
on both sides gives $R_{n,N}-J_N$ even for a modulated average;
there is no requirement that the modulation equal one.

For fixed $T$, there are only finitely many compact kernels in the
sum. Their embedded quantum approximations converge in norm uniformly
over the modulation angle because every coefficient has a common
finite bound. A growing-time quantum estimate is not hidden here.

## 5. Low/high decomposition and the order of limits

The low-frequency part is correct for each fixed Fourier projection
$E_M$: first pass $N\to\infty$ at fixed $T,M$, then use
uniform modulated classical convergence as $T\to\infty$.
The constant function is annihilated exactly and causes no residual
term.

For the high-frequency part, fix a (possibly different) $T$. The
embedded identity contribution is at most $1/T$. Compactness
makes the tails of the finite compact sum tend uniformly in the
angle to zero as $M\to\infty$. This estimate does not need a
classical mixing time associated with $M$.

The two diagonal-block bounds can be combined because the compressed
spectral projection is positive. If the diagonal-block norms are
$a,b$, positivity gives

$$
|\langle x,Qy\rangle|
\le\sqrt{\langle x,Qx\rangle\langle y,Qy\rangle}
\le\sqrt{ab}\,\|x\|\,\|y\|.
$$

It follows that the norm of the full block operator is at most
$a+b$, exactly as stated. The off-diagonal blocks have not been
discarded. This proves the estimate that is sometimes delicate in
such compactness arguments.

One can present the final quantifier order explicitly. For a target
error choose the high-frequency averaging time $T$ large; then
choose $M$ to make its compact tail small. The separate
low-frequency limit already holds for this fixed $M$, using its
own finite averaging times if needed. Finally take odd $N$ large
enough for these finitely many fixed-time approximations and for
the scalar arc minimum to be close to one. Every positive sequence
$\delta_N\to0$ is allowed. In particular, no lower bound on its
rate is necessary.

## 6. Complex resolvent and Schur complement

The center of the near arc is correctly $-t$, since the denominator
is $1-re^{it}\lambda$. On that arc the scaled multiplier has
modulus at most one. Its compressed norm is bounded by the norm of
the compressed spectral projection through the factorization
$(E\iota_0)^*f(W)(E\iota_0)$. This is valid for a complex
multiplier and avoids an invalid ordering of a nonselfadjoint
resolvent.

On the complement, $r\ge1/2$ and

$$
|1-re^{iu}|^2=(1-r)^2+4r\sin^2(u/2)
\ge2u^2/\pi^2
$$

give the displayed bound. Choosing the arc width
$\sqrt{1-r}$ works for every sequence $r_N\uparrow1$, with
no relation to a power of $N$. The Heisenberg radius follows from
$N(1-e^{-s/N})\to s$.

The blocks in the Schur formula have the correct order:

$$
\mathfrak F(z)=zP+z^2D(I-zS)^{-1}C,
\qquad
\iota^*(I-zW)^{-1}\iota=(I-\mathfrak F(z))^{-1}.
$$

Both inverses exist for $|z|<1$, since $W$ is unitary and
$S$ is a compression with norm at most one. The normalized
identity is a reducing vector and can be removed exactly. Finally,
$\sigma_{\min}(A)=\|A^{-1}\|^{-1}$ converts the uniform
$o(N)$ inverse-norm estimate into the stated divergent
$N\inf_t\sigma_{\min}$. This is a singular-value conclusion,
not an eigenvalue-gap claim for the nonnormal return block.

## 7. Perturbation robustness and adversarial test

The estimate

$$
\|\operatorname{Ad}V^n-\operatorname{Ad}U^n\|_{{\rm HS}\to{\rm HS}}
\le2n\|V-U\|_{\mathrm{op}}
$$

is correct by telescoping physical powers and then conjugations.
It preserves every fixed-time compact limit under arbitrary
$o(1)$ perturbations, so the full proof applies to the perturbed
sequence. There is no attempted norm approximation of the shrinking
spectral projections themselves. The robustness statement is therefore
correct even for perturbations much larger than a mean eigenphase
spacing.

The countermodel input was read for the exact power, flatness, and
trace facts. Its projection compression is
$p^{-1}(I-J)+\mathbf1_{a=0}J$; its arc count is bounded by
$1+p\delta/\pi$; and its compressed resolvent is
$(I-J)/(1-z^p)$. These yield uniform shrinking-window and
scaled-resolvent limits while its unweighted pair sum diverges as
$p/(2s)$. The normalization $N=p^2$, the prefactor $p^{-3}$
in the remaining pair contribution, and the Heisenberg resolvent
scale $p/s$ all check.

This adversarial calculation is decisive for the scope of the new
theorem: a norm bound for the compressed gap projector is not the
unweighted pair statistic. The spectral expansion in §9 of the
audited file correctly retains the weights
$\sum_x|\psi_j(x)|^2|\psi_k(x)|^2$, with multiplicities and
arbitrary bases inside degenerate eigenspaces.

## 8. Outcome

No correction to the audited file is requested. Its claims are
accepted within the explicit prior input dependencies. The unresolved
signed pair functional in its equation (9.4) is still unresolved, and
the all-orders criterion is not weakened by this audit.
