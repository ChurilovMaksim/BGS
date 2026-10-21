> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/root_audit_occupation_minami.md`. Embedded SHA256: `b838ab9ccf7bddd7a779a9a864b236cb0b37030c3b7f3ade667e44ab1a9740e0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Audit of the exact same-occupation time-band estimate

Date: 21 October 2026. Reviewer: root, separate direct mathematical
reconstruction of an agent-authored proof. This is a second-reader audit,
not a formal verification certificate or a claim of fully blind review.

Source reviewed:
research_round6_2026_10_21/r6_occupation_minami_band_tail.md,
SHA256 99a6c1b0b6c63a132be7ff1a43c7dbed1cd8321c181ee416f9c61f6601da2032.
The source was read in full before this audit was written.

## Normalized claim and verdict

For every finite unitary matrix $U$, define
$$
\mathcal O_n(U)=
\sum_{|d|=n}\left|
\sum_{\substack{x_0,\ldots,x_{n-1}\\d(x)=d}}
\prod_{i\pmod n}U_{x_i x_{i+1}}
\right|^2.
$$
For all integers $M\ge1$,
$$
\sum_{n=1}^M\mathcal O_n(U)\le\frac{\pi^2}{4}NM.
$$
The stated exponentially weighted infinite-tail bounds hold, with the
constants and integer roundings in the source.

**Verdict: proved as written.** The conclusions about auxiliary local
count moments and the explicit limitations on transfer to the original
spectral process are also correct.

## Dependency chain and direct checks

1. Expanding $\operatorname{Tr}(D_\theta U)^n$ attaches exactly
   $e^{2\pi i d(x)\cdot\theta}$ to a rooted closed word. Parseval therefore
   extracts the specified original sum with coefficient one. Repeated
   words are not divided by their period. This proves the exact identification
   with $\mathbb E_\theta|\operatorname{Tr}(D_\theta U)^n|^2$.

2. Every positive-power closed word in the matrix element
   $((D_\theta U)^m)_{vv}$ leaves $v$ at least once. Integrating just
   $\theta_v$, with all other phases fixed, annihilates every nonzero
   positive Fourier coefficient. Unitarity supplies the negative
   coefficients by conjugation. Fourier uniqueness for finite measures,
   justified by uniform Fejer approximation of continuous functions,
   proves exact one-coordinate spectral averaging on Borel sets.

3. The rank-one determinant quotient has the sign
   $$
   1-(e^{i\beta}-1)\sum_j\frac{w_j\lambda_j}{z-\lambda_j}
   =e^{i\beta/2}\left(\cos\frac\beta2-i\sin\frac\beta2\,H(z)\right).
   $$
   With $H(e^{i\varphi})=-i\sum_jw_j
   \cot((\varphi-\varphi_j)/2)$, its zero equation is exactly the
   cotangent equation in the source. The left side decreases strictly
   from $+\infty$ to $-\infty$ in each cyclic gap. A spectral
   eigenspace with positive weight contributes one active old eigenvalue;
   its remaining multiplicity is fixed. An eigenspace with zero weight
   is wholly fixed. This proves the required alternating-circle count
   inequality, including degeneracies and the single-active-eigenvalue
   case. A common phase with $\beta=0$ is harmless.

4. If $X$ is the old arc count and $X^{(v)}$ the count after independent
   resampling of $\theta_v$, interlacing gives $X-1\le X^{(v)}$.
   On $X\ge1$, the falling factorial of $X-1$ is nondecreasing;
   on $X=0$, every scalar spectral weight of the arc vanishes.
   Thus
   $$
   (X)_k\le\sum_v\mu_v(I)(X^{(v)})_{k-1}.
   $$
   In each summand $X^{(v)}$ is independent of the *old* $\theta_v$.
   Integrating that old variable first is legitimate and gives $|I|$;
   the replacement vector then has the original product distribution.
   Induction yields $\mathbb E(X)_k\le(N|I|)^k$, and hence
   $\operatorname{Var}X\le N|I|$. All quantities here are finite.

5. Invariance under a common shift of all phases kills Fourier terms
   with unequal total powers. Fejer approximation to the arc indicator
   converges in $L^2$, since counts are at most $N$ and fixed
   endpoints have zero expected mass. Squared Fejer weights increase
   with cutoff. Monotone convergence proves
   $$
   \operatorname{Var}X_I=
   2\sum_{n\ge1}\frac{\sin^2(\pi n|I|)}{\pi^2 n^2}\mathcal O_n(U).
   $$
   At $|I|=1/(2M)$, the lower bound $\sin(\pi n/(2M))\ge n/M$
   gives the constant $\pi^2/4$ in the claim.

6. With $F(m)=\sum_{n\le m}\mathcal O_n(U)$ and $0<q<1$, the exact
   summation-by-parts identity is
   $$
   \sum_{n>L}q^n\mathcal O_n
   =(1-q)\sum_{m>L}q^mF(m)-q^{L+1}F(L).
   $$
   It was recomputed directly by interchanging the absolutely convergent
   sums. The boundary term is nonpositive. Using $F(m)\le(\pi^2/4)Nm$
   proves both the asserted rounded tail and the sharper complete-sum
   estimate. No unproved asymptotic tail of the original squared traces
   is used.

## Scope checks

The proof needs neither flatness of $U$, nor simplicity of its spectrum,
nor a classical mixing estimate. It therefore applies to the original
prescribed matrix in every odd dimension. No exceptional subsequence
or changed value of $\tau$ is introduced.

The bound for falling factorial moments concerns one connected arc.
It is not a domination theorem for mixed-interval correlation densities.
The proof makes no such claim.

The auxiliary law is tight by the uniform interval means. Exponential
count bounds supply uniform integrability. Passing compactly supported
continuous statistics to subsequential limits therefore preserves
intensity one. For intervals, translation invariance and finite
intensity exclude fixed endpoint atoms. These statements are justified
for the auxiliary phase process only.

No numerical calculation is a logical dependency of this proof. The
full target remains open because neither the limiting value of the
bounded occupation sector nor the required full unequal-occupation
sum has been evaluated.
