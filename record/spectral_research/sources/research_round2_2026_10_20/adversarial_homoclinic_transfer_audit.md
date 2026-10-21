> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_homoclinic_transfer_audit.md`. Embedded SHA256: `dded43ab4fda8e112ebefb9f2bbf55fb356cbc5ade56986428357020897e529f`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exact homoclinic weights and doubled transfer

Research continuation, 20 October 2026.

## 1. Input and verdict

The input is fermionic_homoclinic_and_doubled_transfer.md,
SHA-256
85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168.
The centered Gaussian kernel and the explicit Berg coding were
also compared directly with their frozen source proofs.

**Verdict: PASS.** This includes the uniform base derivative in
trace norm, fractional regularity of the actual scalar cocycle,
all lattice and inverse-code signs, primitive-orbit matching,
the doubled resolvent normalization, and its full Abel tail.

The original two selected orbit pairs have exponentially small
weight. This audit does not infer an obstruction to the desired
spectral statistics from those pairs.

## 2. Exact Landau gauge

The original winding phase is
$$
(-1)^{n_qn_p}
\exp\left(\frac{i}{h}
  \left[\sum F-n_p(q_0+n_q/2)\right]\right).
$$
For odd $N$, $h^{-1}=2\pi N$, the product of the two
half-winding factors is
$\exp(i\pi(1-N)n_qn_p)=1$. The exact phase is therefore
$$
\exp\left(\frac{i}{h}[\sum F-n_pq_0]\right).
$$

The deck identification
$(z,u)\mapsto(z+n,e^{in_pq/h}u)$ is an action: its
composition discrepancy is an integer multiple of $2\pi iN$.
The generating-function deck law adds
$$
cQ-dq+(ca-db)/2,\qquad (a,c)=L(b,d).
$$
Since $L\equiv I\pmod2$, the last constant is an integer.
The input deck phase cancels the term $-dq$, leaving the
output deck phase $cQ$. Thus the prequantum lift is
equivariant in precisely this gauge.

For a chosen output representative $z'$ and deck
$\Psi z=z'+d_e$, reducing the output multiplies by
$\exp(-id_{e,p}q'/h)$. This gives exactly the local phase
in the input, including its sign. Multiplication around a
cycle recovers the full winding expression.

## 3. Uniform trace-norm regularity of the centered kernel

Let $s=\sqrt h$, and write the centered phase as
$$
\widetilde F_x(Z)=F(X+Z)-F(X)-DF(X)Z.
$$
The contour $z_s(y)=sy-i\psi(sy)$ is independent of the
base point. A base derivative is
$$
D_xX\cdot\big(DF(X+Z)-DF(X)-D^2F(X)Z\big).
$$
The bracket has a zero second-order jet estimate:
it is bounded by $C|Z|^2$. Thus dividing by $s^2$
does not introduce a small-$s$ singularity, because
$|Z|\leq\sqrt2s(|y|+|y'|)$.

The oscillator trace-norm criterion uses up to two
derivatives in each of $y,y'$. Differentiating once
removes at most one zero in the Taylor bracket and
supplies one factor $s$ from the contour derivative.
Differentiating twice or more supplies at least $s^2$.
Higher contour derivatives have further nonnegative
powers of $s$. Consequently all needed mixed kernel
derivatives, with one base derivative included, are
bounded by a fixed polynomial in $|y|+|y'|$ times
the original coercive exponential, uniformly in $h$.

The saturated contour gives
$$
\exp[-cs^{-2}\{sy\psi(sy)+sy'\psi(sy')\}].
$$
For fixed $u_0>0$,
$u\psi(u)\geq c_0\min(u^2,u_0|u|)$. If $s\leq s_0$,
the preceding expression is bounded by
$$
\exp[-c'\{\min(y^2,u_0|y|/s_0)
             +\min((y')^2,u_0|y'|/s_0)\}],
$$
which is integrable after multiplication by every fixed
polynomial. This proves the required dominated
differentiation, including the unbounded real contour tails.

For $A_{\rm osc}=1-\partial_y^2+y^2$, its eigenvalues
are $2n+2$. Hence
$\|A_{\rm osc}^{-1}\|_{\rm HS}^2=\pi^2/24$, and
factorizing the kernel operator on its two sides gives
$$
\|K\|_1\leq\frac{\pi^2}{24}
  \|A_{{\rm osc},y'}A_{{\rm osc},y}k\|_{L^2}.
$$
Applying this both to the kernel and its base
derivatives proves a uniform $C^1(\mathbb T^2;\mathcal S_1)$
bound. The centered deck law makes it a torus derivative;
no rapidly oscillating uncentered phase has been retained.

## 4. Fractional regularity without a false smooth graph claim

The normalized projective map has a nonzero denominator
throughout the stated invariant ball and contraction
constant below $0.172$. The preceding base derivative
gives a uniform base Lipschitz bound. Since
$\operatorname{Lip}(\Psi^{-1})\leq8$, iteration of the
graph transform gives
$$
[w_{n+1}]_{1/2}
\leq0.172\sqrt8\,[w_n]_{1/2}+C\sqrt8.
$$
The coefficient is less than $0.487$. Uniform graph
convergence therefore preserves the uniform half-Holder
bound. Evaluation of the scalar and the fixed logarithm
on $|\gamma_h-1|<0.0002$ give the asserted uniform
$C^{1/2}$ bound for $\log\gamma_h$.

No differentiability of the invariant section follows
from this proof, and none is claimed.

## 5. Symbolic matching and multiplicities

The Berg spines lie on the stable and unstable leaves
of the origin. Their iterates do also. The only periodic
point on either leaf is the origin, by convergence to
the origin in one time direction. Hence the nonzero
fixed point $(1/2,0)$ has a unique constant-loop code.
There are two other loops at the same vertex and a
two-edge excursion through the other vertex.

The two words constructed in the input have length
$m=6R+4$, exactly one visit to the other vertex, and
different orders of the other two marked loops. The
unique visit proves primitive symbolic period. Their
shift orbits have more than four elements, so the
four-element fiber bound excludes the origin. They
are therefore different primitive geometric orbits.

Writing each word as three cells with $R$ zero edges
on both sides gives an exact permutation of positions.
For a matched position, the central $R$ edges in
both directions agree, including positions adjacent
to a cell boundary: the next cell always begins or
ends with $R$ zeros.

The physical map acts on these codes backwards.
If $Sz_{j-1}=z_j+n_e$, the lift conjugacy gives
$$
\Psi(H z_j)=H z_{j-1}-L n_e.
$$
This verifies the sign and shows that the local
inverse-edge deck label is fixed by the preceding
coded edge. The chart list is finite.

The phase variation is $CN\lambda^{-R/2}$; the
scalar logarithm variation is $C\lambda^{-R/4}$.
Replacing both rates by $(2/3)^R$ is valid.
Telescoping the unit phases and summing logarithms
therefore proves the claimed full-weight ratio.
Every primitive orbit contributes $m a_{p,N}$ to
the trace, so the two cross directions contribute
exactly $2m^2\operatorname{Re}(a_p\overline{a_{p'}})$.
The bounds $6^{-m}\leq|a_p|^2\leq5^{-m}$ and
the asymptotically unit ratio give the asserted
positive but exponentially small contribution.

## 6. Doubled operator and Abel normalization

Direct multiplication of the specified Weyl operators gives
$$
T(u)T(v)=e_N(\overline2\,\sigma(u,v))T(u+v).
$$
Thus the displayed finite-hop generator is exactly
$\operatorname{ad}_{A_N}$, self-adjoint on
Hilbert--Schmidt space. The exact Egorov permutation is
$\operatorname{Ad}_{M_N}T(v)=T(Sv)$, with no
semiclassical error. Therefore
$$
\mathscr C_N=\operatorname{Ad}_{U_N}
 =e^{i\tau N\operatorname{ad}_{A_N}}P_S
$$
and $\operatorname{Tr}\mathscr C_N^m=|p_{m,N}|^2$.

The operator is unitary, both on the full space and
on the complement of its entire fixed commutant.
Any remaining unit-modulus eigenvector prohibits
strict all-time norm contraction, even in an equivalent norm.

Expanding two absolutely convergent geometric series gives
$$
\|(I-r\mathscr C_N)^{-1}\|_{\rm HS}^2
 =\frac{N^2+2\sum_{m\geq1}r^m|p_{m,N}|^2}{1-r^2}.
$$
At $r=e^{-2s/N}$, the pair bound $O_s(1)$
is exactly the resolvent bound $O_s(N^3)$.
Substitution of the proposed CUE limit gives
$$
\frac{1+(1-e^{-2s})/(2s^2)}{4s}
$$
after division by $N^3$, as stated.

Finally $|p_m-\mathcal P_m|\leq2q_*^m$ and
$|p_m|\leq N$ imply
$$
\big||p_m|^2-|\mathcal P_m|^2\big|
\leq4Nq_*^m+4q_*^{2m}.
$$
Their full geometric sums are less than $3N+1$
at $q_*=0.421$, uniformly over $0<r<1$.
This justifies replacing the assembled signed
principal orbit sum in the entire Abel statistic.
It does not justify interchanging an infinite
sum of absolute individual orbit-pair terms.

The unresolved $O_s(N^3)$ resolvent estimate
remains explicitly unresolved in the input.
