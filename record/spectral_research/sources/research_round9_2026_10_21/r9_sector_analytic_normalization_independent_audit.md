> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_sector_analytic_normalization_independent_audit.md`. Embedded SHA256: `0fc9a15bcccab691e2912e64c4d018aba8c822494d00ad848d468fbb5933cd51`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit of the actual analytic scalar normalization

21 October 2026. Auditor: /root/r9_sector_coherence.

## 0. Artifact, accepted claims, and scope

The complete Round 9 root note
research_round9_2026_10_21/root_diagonal_cocycle_normalization.md
was audited at SHA-256
afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921.

**The analytic construction and scalar normalization are accepted in
the stated scope.** For every fixed real trigonometric polynomial,
the note constructs the exact analytic amplitude of the actual
unitary multiplier. It preserves the exact sector/Abel construction.
The first scalar coefficient changes by the asserted additive
function. A single slowly varying sequence through all odd dimensions
then makes the relative scalar error $o(N^{-1})$ uniformly in the
base point and the scalar product error $o(1)$ for every $m\le BN$.

The corresponding varying-generator spectral equivalence is proved
in the companion continuous-symbol note. Its independent audit is
assigned to another branch; this auditor authored that companion
proof and does not present a self-review as independent certification.

There is still no estimate of the full signed orbit error or the
original weighted pair sum. In particular, the result supplies an
equivalent quantization with normalized first scalar correction. It
does not supply a CUE comparison family whose statistics are known.

## 1. Proof inputs actually inspected

Besides reading the complete new root note, this audit read the
load-bearing raw arguments in:

1. the complete original exact-amplitude proof, including the
   characteristic construction, the horizontal-shift identity,
   analytic-scale derivative estimates, and distribution-kernel
   identification;
2. the original odd-trace proof, Sections 7--8, including exponential
   displacement moments, coherent Gaussian bounds, lattice-coset
   unfolding, the one-variable Abel identification, and the common
   $m$-variable Gaussian regulator;
3. the original Gaussian-cocycle proof, including the global graph,
   consecutive mixed-product cancellations, uniform finite jets,
   parity, and the purely imaginary first scalar coefficient;
4. the previous all-time adversarial audit as a cross-check of
   normalizations and scope, not as a replacement for these raw
   derivations.

Thus the conclusion below does not rely on accepting the word
“proved” in a historical status entry.

## 2. Direct check of the weighted shift and exact kernel

Write $h=(2\pi N)^{-1}$ and

$$
 F(Q,q)=-\frac{3Q^2-2Qq+3q^2}{8}+G(Q,q).
$$

The ordinary Weyl operator of frequency $(k,l)$ acts by

$$
 \psi(Q)\longmapsto
 e^{2\pi ik(Q+\pi hl)}\psi(Q+2\pi hl).
$$

Applying it to $e^{iF/h}B$ and removing the same $e^{iF/h}$ gives
a shift of $B$ by $\delta=2\pi hl$ and exponent

$$
 \begin{split}
 \vartheta_{\kappa,h}
 ={}&2\pi[(k-3l/4)Q+(l/4)q]\\
 &+h(2\pi^2kl-\tfrac32\pi^2l^2)
   +2\pi l\int_0^1G_Q(Q+2\pi uhl,q)\,du.
 \end{split}
 \tag{2.1}
$$

Every sign and factor here was recomputed from the quadratic
difference, rather than copied from the stated formula. In particular,

$$
 \frac{F_0(Q+\delta,q)-F_0(Q,q)}h
 =2\pi l(-3Q/4+q/4)-\frac32\pi^2hl^2.
$$

For real $h$, the shifts are horizontal on the full spatial strip.
The term linear in $h$ in (2.1) is real. The remaining imaginary part
is bounded uniformly over the entire real plane, with a bound
exponential in $|k|+|l|$. Therefore a fixed polynomial $v$ defines a
bounded weighted-shift operator $\mathcal L_{v,h}$ on the same strip,
uniformly in real $h$.

Its bounded-operator exponential

$$
 B_h^v=e^{i2\pi h\mathcal L_{v,h}}B_h
 \tag{2.2}
$$

is legitimate in the spatial analytic norm. Every exponential term
is the actual corresponding finite Weyl word applied to the original
kernel. On the real plane the weight has modulus one. The absolute
coefficient sum is finite, so the kernel series is integrable against
every Schwartz test function. Its limit agrees on tensor-product test
functions with the bounded $L^2$ operator exponential; density then
identifies the distribution kernel. Thus

$$
 C_he^{iF/h}B_h^v
$$

is exactly the kernel of
$e^{i2\pi h\operatorname{Op}_h(v)}\mathcal U_h$.
It is not an asymptotic kernel substitute.

At the comb values of $h$, the ordinary midpoint differs from the
modular midpoint by the given $(-1)^{kl}$. Consequently the finite
restriction is exactly $e^{iQ_N(v)/N}U_N$, up to the same already
retained common metaplectic scalar as for the original family.

## 3. The derivative issue and why the flattened-word proof resolves it

Cauchy's estimate costs a spatial strip gap when a shifted analytic
function is differentiated in $h$. One must not assert that
$\mathcal L_{v,h}$ is twice differentiable as a bounded operator on
one unchanged supremum-norm strip.

The root note correctly allocates fixed outer-to-inner gaps.
Its additional exact flattened-word identity is a particularly
direct justification:

$$
 \mathcal W_{\kappa_1,h}\cdots\mathcal W_{\kappa_n,h}
 =
 e^{\,2\pi^2ih\sum_{r<s}\omega(\kappa_r,\kappa_s)}
 \mathcal W_{\kappa_1+\cdots+\kappa_n,h}.
 \tag{3.1}
$$

This follows by conjugating the ordinary Weyl product law, whose
scalar is $e^{2\pi^2ih\omega}$. For frequencies in one fixed
polynomial, the summed frequency is $O_v(n)$ and the symplectic
area is $O_v(n^2)$. The central phase has modulus one for real $h$.
The remaining weight has bound $C_v^n$. Each of the first two
$h$-derivatives introduces at most a fixed polynomial in $n$ and
at most two spatial derivatives of the original $B_h$.

All such spatial derivatives can be taken with one fixed total
strip gap. Summing the words adds an exponential factor $s_v^n$.
The $1/n!$ in (2.2) dominates these exponentials and all fixed
polynomials in $n$, including the factors from differentiating
$h^n$. The finitely many terms with $n<2$ are treated directly.
Both derivative series converge uniformly on a fixed bounded
real-$h$ interval.

This proves genuine $C_h^2$ regularity in the smaller spatial norm.
At $h=0$,

$$
 \mathcal L_{v,0}B_0=v(Q,F_Q(Q,q))B_0.
$$

Taylor's theorem gives the actual uniform remainder

$$
 B_h^v
 =B_0+ih[b_1+2\pi v(Q,F_Q)B_0]+O_v(h^2).
 \tag{3.2}
$$

Higher fixed spatial derivatives of this remainder follow from
Cauchy's estimate on a further fixed smaller strip. No common
smooth-symbol seminorm bound over the later sequence $v_j$ has
been assumed.

## 4. Deck covariance and the exact sector/Abel transplant

For the deck transformation $(a,c)=L(b,d)$, the phase difference
law gives

$$
 \vartheta_{\kappa,h}(Q+a,q+b)
 -\vartheta_{\kappa,h}(Q,q)=2\pi(ka+lc).
 \tag{4.1}
$$

This is an integer multiple of $2\pi$. The real shifts commute
with the deck translations, so the new exact amplitude has the
same deck law.

There is also an operator check of the covariance needed for
lattice-coset grouping. Every Fourier Weyl operator in
$\operatorname{Op}_h(v)$ commutes with every honest integer
lattice operator $R_n$: their commutator character is
$e^{2\pi i(kn_q+ln_p)}=1$. Therefore the new exponential commutes
with all $R_n$. Since

$$
 \mathcal U_hR_n=R_{Ln}\mathcal U_h,
$$

the new plane operator satisfies the same exact covariance.
Consequently its $m$-th power groups into exactly the same
classes of $\mathbb Z^2/(L^m-I)\mathbb Z^2$, with the same odd
lattice character and no extra multiplicity.

At each fixed $m,h$, expansion into translated metaplectic words
has a summable absolute coefficient mass and every fixed
exponential moment of the real displacement. For the added
exponential this follows directly from

$$
 \sum_{r\ge0}\frac{(2\pi |h|s_v)^r}{r!}
 e^{C\,2\pi |h|d_vr}<\infty.
 \tag{4.2}
$$

The original finite-generator kick has the already established
property. Finite products preserve it after the fixed matrices
$L^j$ transport the displacements.

The old coherent diagonal of a translated metaplectic word has
an absolute Gaussian integral independent of its translation.
The sum over lattice points in a unit cell is uniformly bounded
as the Gaussian center varies. Applying these bounds to (4.2)
justifies absolute rearrangement and unfolding of the new word
series, exactly as in the raw original proof.

For the path-kernel version, each word has the same cyclic
quadratic Hessian

$$
 H_m=-\frac14(6I-R-R^{-1}),
$$

with spectrum in $[-2,-1]$, including the coincident edges when
$m=1,2$. Translations only change the real linear term and a
unimodular constant phase. For the common positive Gaussian
regulator, completion of the square has modulus at most one;
the determinant prefactor is bounded by its zero-regulator
value independently of the linear term. The summable word
coefficient mass therefore allows dominated convergence
through the common Abel limit.

This proves that the new full sector integrals are the actual
finite quantum traces. The exact analytic kernel (2.2) may now
be inserted in them. Its phase, strict concavity, critical
points, and bounded contour are unchanged. Analytic amplitude
boundedness and the derivative estimates supply the remaining
contour and trace-class hypotheses.

## 5. Scalar response and the uniform diagonal threshold

The rescaled edge expansion is in $s=\sqrt h$. Equation (3.2)
changes neither $K_0$ nor $K_1$, and changes the order-$s^2$
coefficient by

$$
 K_2^v(x)-K_2(x)=i2\pi v(\Psi x)K_0(x).
 \tag{5.1}
$$

In the normalized graph quotient, a scalar multiple of $K_0$
cancels between numerator and denominator at this order. The
additional forcing in the coefficient equation for $w_2$ is
therefore zero. The inverse $I-\mathcal T$ exists with the
already verified contraction constant below $0.172$, so the
global continuous fixed section has the same order-$s^2$
coefficient as before.

The scalar itself acquires
$i2\pi v(\Psi x)\gamma_0(x)$ at order $h$. Transverse reflection
makes the scalar even in $s$; amplitude reality gives the
purely imaginary first coefficient. The finite coefficient
recursion with its controlled defect thus proves

$$
 \frac{\gamma_h^v(x)}{\gamma_0(x)}
 =1+ih[\sigma(x)+2\pi v(\Psi x)]+O_v(h^2).
 \tag{5.2}
$$

The old graph leading kernel is unchanged. For each fixed $v$,
all sufficiently small $h$ lie in the same numerical graph
neighborhood. The residual norm bounds and the same absolute
sector count give the asserted common exponentially decreasing
residual in every positive iterate.

For $v=-\sigma\circ\Psi^{-1}/(2\pi)$, Fejér polynomials $v_j$
converge uniformly without a smoothness assumption on $\sigma$.
At stage $j$, the fixed-polynomial remainder and graph threshold
are finite. Their dimension threshold can be increased until
$C_jh_N\le1/j$, along with $h_N\ell_{v_j,a}\le1/j$ on the
common strip and all spectral approximation conditions.

These are finitely many eventual conditions at each fixed
stage. The definition $j(N)=\max\{j:n_j\le N\}$ retains every
odd dimension. It gives

$$
 \sup_x\left|\frac{\gamma_{h_N}^{v_{j(N)}}(x)}{\gamma_0(x)}-1\right|
 \le h_N\left(2\pi\|v_{j(N)}-v\|_\infty+\frac1{j(N)}\right)
 =o(N^{-1}).
 \tag{5.3}
$$

The product estimate for $m\le BN$ then follows from
$(1+a_N)^m-1\le e^{ma_N}-1$ with $a_N=o(N^{-1})$.
The same sequence works for every fixed $B$. No uniform
estimate over unbounded $B$ is needed.

## 6. What the audit does not certify

The root note correctly distinguishes uniform orbitwise
relative error from error after an exponentially large
oscillatory orbit sum. If $|\varepsilon_x|\le\varepsilon_N$
with $\varepsilon_N\to0$, the only unconditional absolute
sum bound furnished here is

$$
 \left|\sum_x A_xe^{iS_x/h}\varepsilon_x\right|
 \le\varepsilon_N\sum_xA_x.
$$

The right side is insufficient at $m\asymp N$ because the
amplitude sum grows exponentially. Neither the exact finite
unitarity nor the scalar product normalization replaces the
missing coherent estimate.

Thus this audit accepts the new realization theorem and
its precision; it does not certify $H_{\rm diag}$ for the
original family, the equivalent family, or any CUE model.

## 7. Exact input hashes

| Actual source read | SHA-256 |
|---|---|
| research_round9_2026_10_21/root_diagonal_cocycle_normalization.md | afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921 |
| research_continuation_2026_10_20/exact_amplitude.md | 69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e |
| research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md | 42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b |
| research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md | c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1 |
| research_round2_2026_10_20/adversarial_all_time_audit.md | dbc1070d04c238213138b5eb433776d3ce0dfb6e9c07fca7eb90ebd9b42c7c25 |

The audited root file and all older sources were left unchanged.
