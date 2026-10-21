> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_determinant_braun_haake_and_contraction_audit.md`. Embedded SHA256: `979cdac97772c3a10d6b186c13f066677d8d4bcf2f0bc05f4a300609f5af67f9`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Braun--Haake applicability and the concrete determinant contraction attempt

21 October 2026. Branch `/root/r9_spectral_determinant`.

## 1. Source checked and exact scope

The primary source was read as raw original PDF text, not as its abstract
or an AI summary:

P. Braun and F. Haake, *Chaotic maps and flows: Exact Riemann--Siegel
lookalike for spectral fluctuations*, arXiv:1206.4222v1, June 2012;
published in *Journal of Physics A* **45** (2012), 425101,
[DOI 10.1088/1751-8113/45/42/425101](https://doi.org/10.1088/1751-8113/45/42/425101).
The [original manuscript](https://arxiv.org/abs/1206.4222v1), pages
5--9 and 14--15, was retrieved through alphaXiv on 21 October 2026.

The following short source map records the relevant published steps.

| Location | What the paper does |
|---|---|
| Section 2, (9)--(15) | Gives exact self-inversiveness, a finite numerator, and infinite reciprocal expansions. |
| Section 3, (16)--(22) | Introduces determinant ratios; the center average retains equal total Fourier degree. A second offset-window average is discussed. |
| Section 4.2, (27) | Keeps action-matched terms and assigns Gaussian factorial multiplicities to the diagonal approximation. |
| Section 4.2, (30)--(32) | Evaluates that approximation and obtains the finite-dimensional CUE expression. |
| Section 4.3, page 9 | Defers a full cancellation proof for the map corrections. |
| Section 6, page 14 | Reports cancellation in six computed diagram orders and leaves all orders to future work. |

The exact finite CUE expression is therefore the value of the evaluated
diagonal model. These passages do not supply a uniform remainder for
the original deterministic family at times proportional to $N$.
The conclusion here is about applicability of this specific paper;
it is not a claim about the absence of every later result.

## 2. The precise distinction between center averaging and action matching

This elementary computation is independent of the paper. Write
$p_n(U)=\operatorname{Tr}U^n$. Under the single random center phase,
equivalently under $U\mapsto e^{i\alpha}U$,
$$
 \int_0^{2\pi}\prod_{n\ge1}
 p_n(e^{i\alpha}U)^{u_n}
 \overline{p_n(e^{i\alpha}U)}^{v_n}\,
 \frac{d\alpha}{2\pi}
 =\mathbf1_{\sum_n n(u_n-v_n)=0}
  \prod_{n\ge1}p_n(U)^{u_n}\overline{p_n(U)}^{v_n},
 \tag{2.1}
$$
for finitely supported nonnegative integer sequences $u,v$.
The proof is integration of the one Fourier character
$e^{i\alpha\sum_n n(u_n-v_n)}$.

Equation (2.1) does not impose $u_n=v_n$ for every $n$.
For instance $p_1^2\overline{p_2}$ survives it unchanged.
It also does not impose equality of the individual classical orbits
within a trace product. Such selection requires an estimate of the
complete remaining oscillatory sum.

Even the Gaussian factorial rule cannot hold term by term under this
one-dimensional rotation. For a fixed $n$, its second and fourth
moments are exactly $|p_n|^2$ and $|p_n|^4$. If the former tends
to a positive value $v$, the latter tends to $v^2$, rather than
the Gaussian value $2v^2$. This does not contradict the desired
weighted spectral limit: that limit sums over many frequencies before
taking its asymptotic value. It excludes a termwise replacement as its
proof.

Suppose the physical diagonal weights for the original map have been
estimated at every time with a summable error. This controls the
weights of terms that were retained after action matching. It supplies
no estimate for the terms discarded between (2.1) and that matching.
Correcting a diagonal subprincipal phase has the same logical scope:
it improves the amplitude of an already specified orbit contribution,
but does not average its principal action against distinct orbits.

## 3. Why the full determinant autocorrelation is still insufficient

The companion theorem
`r9_determinant_exact_cue_detdet_counterexample.md` proves, without a
semiclassical assumption, that the deleted clock has exactly the full
CUE determinant autocorrelation for every dimension and every pair of
complex arguments. It simultaneously has a nonzero fixed pair defect
and a shifted-lattice local limit. Its inverse-determinant moment at
radius $e^{-s/N}$ is bounded, while the CUE value grows as $N/(2s)$.

The addendum `r9_determinant_nonzero_minors_addendum.md` shows that
all zero physical minors and all finite-order returns can be removed
while preserving those conclusions and making the determinant
autocorrelation error smaller than every inverse power of $N$.
Thus the discarded information is not recovered by either exact
self-inversiveness or qualitative nonvanishing at algebraic parameters.

## 4. An actual attempt using the concrete generator and both denominators

The following bounds are for the precise original matrices, all odd
$N$, with no change in $\tau$. They record why a direct perturbative
control of the mixed ratios fails to yield an asymptotic estimate.
They are not presented as a universality result.

### 4.1 Uniform norm bound for the prescribed $A_N$

Put $t=2\pi q$. The exact trigonometric identities are
$$
 r(q)=1+\cos t-\cos7t-\tfrac12\cos8t-\tfrac12\cos6t,
$$
$$
 r(q)\sin t
 =\sin t+\tfrac12\sin2t-\tfrac12\sin8t+
  \tfrac12\sin6t-\tfrac14\sin9t+\tfrac14\sin5t.
$$
The Fourier coefficient absolute sum of
$\cos7t+r/10-1/10$ is $11/10$. That of
$r\sin t/100$ is $3/100$, and that of
$r\cos(2\pi p-\alpha_0)/100$ is $4/100$.
Every quantized Fourier monomial is unitary, including after modular
aliasing. Hence the triangle inequality proves
$$
 \boxed{\|A_N\|\le\frac{117}{100}\quad\text{for all odd }N.}
 \tag{4.1}
$$

### 4.2 The common-center determinant ratio

Let $U_N(t)=e^{itNA_N}M_N$, with real $t$, and
$D_t(z)=\det(I-zU_N(t))$, $|z|<1$. The determinant does not
vanish in this disk because $U_N(t)$ is unitary.
Its logarithm is uniquely specified by $\log D_t(0)=0$.
Differentiating the finite determinant gives
$$
 \partial_t\log D_t(z)
 =-iNz\operatorname{Tr}
   \bigl((I-zU_N(t))^{-1}A_NU_N(t)\bigr).
 \tag{4.2}
$$
The resolvent bound $\|(I-zU)^{-1}\|\le(1-|z|)^{-1}$
follows directly from the convergent geometric series, or from the
spectral theorem. Integrating (4.2) and using (4.1) yields the actual
uniform bound
$$
 \boxed{\left|\log\frac{D_\tau(z)}{D_0(z)}\right|
 \le\frac{117}{100}\frac{\tau N^2|z|}{1-|z|}.}
 \tag{4.3}
$$
In particular the bound controls the reciprocal as well as the direct
determinant. At $|z|=e^{-s/N}$, however, its right side is
$O_s(\tau N^3)$. Fixed $\tau=10^{-80}$ does not make it tend to
zero. Bounds for products or quotients of finitely many such
determinants inherit this problem. Replacing $\tau$ by a vanishing
sequence would change the problem and is not used here.

### 4.3 The complete weighted pair sum under the same direct estimate

Duhamel's formula and unitarity give
$$
 \eta_N:=\|U_N(\tau)-M_N\|
 \le\min\{2,(117/100)\tau N\}.
$$
The telescoping identity for powers gives
$\|U_N(\tau)^m-M_N^m\|\le m\eta_N$. Therefore
$$
 \bigl||\operatorname{Tr}U_N(\tau)^m|^2-
        |\operatorname{Tr}M_N^m|^2\bigr|
 \le2mN^2\eta_N.
 \tag{4.4}
$$
For any fixed bounded weight $w$ supported in $[0,B]$,
$$
 \frac1{N^2}\left|\sum_{m\ge1}w(m/N)
   \left(|\operatorname{Tr}U_N(\tau)^m|^2-
         |\operatorname{Tr}M_N^m|^2\right)\right|
 \le2\|w\|_\infty\eta_N\sum_{m\le BN}m.
 \tag{4.5}
$$
This bound is $O_{B,w}(\tau N^3)$ before saturation and supplies
no $o(1)$ result at fixed $\tau$. The conclusion is limited:
these direct estimates fail; it does not follow that the actual
oscillatory quantity is large.

## 5. The exact missing contraction

The finite matrix formulation can be made without any semiclassical
trace approximation. On matrices with the Hilbert--Schmidt product,
put $\mathcal W_N=\operatorname{Ad}U_N$. Let $\Pi$ be physical
coordinate-diagonal projection, $O=I-\Pi$, and write
$$
 \mathcal W_N=\begin{pmatrix}P&B\\ C&S\end{pmatrix},
 \qquad
 \mathfrak F(z)=zP+z^2B(I-zS)^{-1}C.
$$
For $|z|<1$, block elimination gives
$$
 \det(I-z\mathcal W_N)
 =\det(I-zS)\det(I-\mathfrak F(z)).
 \tag{5.1}
$$
All inverses exist: $S$ is a contraction, and the full matrix is
invertible, which also makes the Schur complement invertible.
Logarithmic differentiation yields
$$
 \sum_{m\ge1}z^m|\operatorname{Tr}U_N^m|^2
 =z\operatorname{Tr}\bigl(S(I-zS)^{-1}\bigr)
  +z\operatorname{Tr}\bigl((I-\mathfrak F(z))^{-1}
                                \mathfrak F'(z)\bigr).
 \tag{5.2}
$$
This identity was already proved in the earlier return branch; it is
recorded here only to specify exactly which contraction remains
uncontrolled. For the Abel pair test at $z=e^{-2s/N}$, the missing
estimate is
$$
 \frac z{N^2}\left[
 \operatorname{Tr}\bigl(S(I-zS)^{-1}\bigr)
 +\operatorname{Tr}\bigl((I-\mathfrak F(z))^{-1}
                                  \mathfrak F'(z)\bigr)
 -\frac{1-z^N}{(1-z)^2}\right]\longrightarrow0.
 \tag{5.3}
$$
The CUE term is exact because
$\sum_{m\ge1}\min(m,N)z^m=z(1-z^N)/(1-z)^2$.
No separate estimate of either trace on the right of (5.2) implies
the signed cancellation in (5.3). Likewise its value at $z=1$,
where defined by a limiting identity, does not control its variation
in a layer of width $1/N$.

Equation (5.3) is still weaker than the required hierarchy of all
fixed compact Fourier-band tests and all fixed orders. Even proving
it would not finish the user's task. For the original fixed test
$b_*$, the first missing assertion remains the exact weighted
pair estimate from the Round 8 ledger; neither (4.3), (4.5), nor the
determinant identities prove it.

## 6. Outcome of this branch

The new proved result is the determinant-autocorrelation obstruction,
including its all-minors strengthening. The paper's hypotheses have
been checked far enough to identify a precise unproved transition,
rather than importing its diagonal answer as a theorem for $U_N$.
The concrete original-generator ratio attempt has been carried through
with its actual $N$-dependence and fails to provide decay. No hidden
random-phase assumption, exchange of an unbounded Fourier band with
a limit, or uniform-in-time semiclassical error is introduced.

The original $H_{\rm diag}$ and the original local limit remain
unproved and undisproved in this branch.
