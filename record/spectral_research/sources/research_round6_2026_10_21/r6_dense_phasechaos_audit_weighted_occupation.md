> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_dense_phasechaos_audit_weighted_occupation.md`. Embedded SHA256: `624b63471ed09768bf88c353b26fb8f9d049dac1b0b6765cac0e0b0825729c1e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit of the all-order weighted occupation bound

21 October 2026. Reviewer: /root/r6_dense_unmarking.

## Source and verdict

Reviewed source:
research_round6_2026_10_21/root_all_orders_weighted_occupation_bound.md,
SHA-256
843da22fde6f586adbbdec0fe51b17875456477ed0f78dcb4f5b0115e87f919d.

The arc input was read in full, not inferred from its audit:
research_round6_2026_10_21/r6_occupation_minami_band_tail.md,
SHA-256
99a6c1b0b6c63a132be7ff1a43c7dbed1cd8321c181ee416f9c61f6601da2032.

**Verdict: proved as written.** I found no missing independence,
mixed-interval hypothesis, root multiplicity, or transfer assumption
in the weighted theorem. This is an independent reconstruction of the
argument, not a formal verification certificate.

## Reconstruction from definitions

Let the independent row phases multiply an arbitrary finite unitary
matrix $U$. Common-phase invariance makes the periodically unfolded
eigenvalue law stationary. Each scaled unit interval therefore has
count $Y_j$ with mean 1. For $N\ge2$, it projects injectively onto
a connected arc of normalized length $1/N$, up to endpoints, and
fixed endpoints have zero spectral probability.

The arc theorem's resampling argument applies to precisely that
connected arc. Its pointwise step is
$$
(X_I)_k\le
\sum_v\mu_{v,\theta}(I)(X_I^{(v)})_{k-1},
$$
where the second factor does not depend on the old phase
$\theta_v$. Conditional one-coordinate spectral averaging of the
first factor is consequently legitimate. The result is
$$
\mathbb E(Y_j)_k\le1,\qquad
\mathbb E e^{sY_j}\le e^{e^s-1}.
$$
These estimates make no claim about joint distributions of different
interval counts; those counts are in fact periodic in $j$ for each
sample.

For the nonnegative Schwartz function $b$, let
$\beta_j=\sup_{[j,j+1]}b$, $B_b=\sum_j\beta_j$. Schwartz decay
implies $B_b<\infty$, and half-open unit intervals give pointwise
$$
X_b\le\sum_j\beta_jY_j.
$$
The right side is finite almost surely by Tonelli, since its mean is
$B_b$. If $B_b>0$, the numbers $\beta_j/B_b$ are probability
weights. Countable Jensen gives the moment-generating bound using
only the one-interval estimates. Its finite approximation is valid:
place the unused probability weight at zero, then pass to the limit
monotonically on both sides.

The same argument with $x^k$, together with
$$
m^k=\sum_{r=0}^k S(k,r)(m)_r,
$$
gives $\mathbb EX_b^k\le \mathfrak B_k B_b^k$. The identity follows
by classifying functions by the size of their image, so the Bell
constant has the stated normalization.

Periodization gives $X_b=\sum_a b_N(\vartheta_a)$ exactly. The
nonnegative distinct-index terms occur $k!$ times in $X_b^k$;
therefore the elementary symmetric polynomial is bounded by
$X_b^k/k!$. Integrating the global shift adds no new law, because
simultaneously shifting all row phases preserves product Haar
measure. This proves
$$
0\le\overline M_{k,N}(U;b)
\le\frac{\mathfrak B_k B_b^k}{k!}.
$$
The cases $k=0$, $k=1$, $k>N$, and $B_b=0$ agree with the
definitions. Nonnegative exponential-series rearrangement gives the
summable majorant $e^{e^{B_b}-1}$.

## Exact occupation extraction

For compactly supported $\widehat b$, the Fourier sum is finite,
as is its partition expansion into traces. Positive trace powers
contribute the departure occupation phase $z^{d(x)}$, negative
powers contribute its conjugate, and a block with trace power zero
is exactly $p_0=N$ with no phase. Orthogonality on the coordinate
torus therefore keeps precisely equality of the aggregate positive
and negative occupation vectors. Every partition coefficient and
Fourier weight remains unchanged. This is the full constant
coefficient of the stated finite functional, with its internal
signed cancellations, rather than a selected subset of terms.

## Scope

The envelope constant is $B_b$, as stated, and has not been
replaced by $\int b$. The moment-generating bound indeed supplies
uniform integrability of every fixed weighted local count power
in the auxiliary process. It does not supply a limit for the
constant coefficient, control the complementary Fourier modes at
the original phase vector, or imply $H_{\rm diag}$.

No source file was changed during this audit. No numerical
experiment is a logical input to the verdict.
