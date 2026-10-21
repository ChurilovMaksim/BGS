> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round9_2026_10_21/r9_determinant_exact_cue_detdet_counterexample.md`. Embedded SHA256: `4fd909b04e8ccc1a000930e46e6efe23b520e8d41400d8f923e3aa7911623b7f`.
> [Thematic guide](../../topics/closure.md).

# Exact CUE determinant autocorrelation does not determine microscopic statistics

21 October 2026. Branch `/root/r9_spectral_determinant`.

## 0. Scope and achieved result

This note proves an explicit obstruction to a proposed proof mechanism.
It is **not** a counterexample for the prescribed matrices
$U_N=e^{i10^{-80}NA_N}M_N$, and supplies no estimate of their first
unresolved weighted pair sum.

The result is stronger than the previously recorded fact that finite
self-inversiveness or finitely many short traces do not imply universality.
For every odd $N$, an explicit unitary matrix has exactly the complete
CUE angular determinant autocorrelation, for **all complex arguments**.
Consequently every differentiated version of that polynomial correlation
also agrees exactly. Nevertheless:

1. a fixed admissible pair test has a strictly negative limiting CUE defect;
2. the local point process converges to a uniformly shifted unit lattice;
3. its inverse-determinant second moment at distance $s/N$ from the unit
   circle is bounded, while the corresponding CUE quantity grows linearly
   with $N$.

Thus even proving the entire CUE determinant autocorrelation for the
original family would not, by itself, establish its pair statistics.
The mixed numerator/denominator information is essential.

No priority claim about this elementary construction is made.

## 1. The deleted clock

For $N\ge3$, set
$$
 V_N=\operatorname{diag}\left(e^{2\pi ij/(N+1)}:1\le j\le N\right),
 \qquad D_N(z)=\det(I-zV_N).
$$
These matrices are unitary with simple spectrum. Factoring the roots of
unity gives the polynomial identity
$$
 \boxed{D_N(z)=\frac{1-z^{N+1}}{1-z}=\sum_{k=0}^Nz^k.}
 \tag{1.1}
$$
The quotient is understood by its removable value at $z=1$.
In particular all its secular coefficients have modulus one.

For any unitary matrix $V$, write
$D_V(z)=\sum_{k=0}^Nd_k(V)z^k$, and define
$$
 \mathcal C_V(z,w)=\int_0^{2\pi}
 D_V(ze^{i\alpha})\overline{D_V(we^{i\alpha})}
 \,\frac{d\alpha}{2\pi}.
$$
Finite Fourier orthogonality, with no approximation, yields
$$
 \mathcal C_V(z,w)=\sum_{k=0}^N|d_k(V)|^2(z\overline w)^k.
 \tag{1.2}
$$
Therefore
$$
 \boxed{\mathcal C_{V_N}(z,w)=\sum_{k=0}^N(z\overline w)^k.}
 \tag{1.3}
$$

## 2. A self-contained CUE comparison

### 2.1 Haar eigenvalue integration

We use normalized Haar measure on $U(N)$. In eigenangles
$\lambda_j=e^{i\theta_j}$, its density for symmetric integrands is
$$
 \frac1{N!}\left|\Delta(\lambda)\right|^2
 \prod_{j=1}^N\frac{d\theta_j}{2\pi},
 \qquad \Delta(\lambda)=\det(\lambda_i^{j-1})_{i,j=1}^N.
 \tag{2.1}
$$
Here is the needed verification. On the simple-spectrum locus write
$U=W\operatorname{diag}(\lambda)W^*$. For an off-diagonal complex
coordinate of $W^*dW$, the invariant metric gives the factor
$|\lambda_i-\lambda_j|^2$; the angular directions have constant metric
factors. Multiplying the independent off-diagonal factors gives
$|\Delta|^2$. Repeated-spectrum strata have smaller dimension:
for multiplicities $m_1,\dots,m_r$, their dimension is
$N^2-\sum m_j^2+r<N^2$. They therefore have zero invariant volume.
Normalized invariant volume is Haar measure by invariance and the
double-integration uniqueness argument. Finally, expanding the two
Vandermonde determinants and integrating the torus characters leaves
exactly $N!$ equal permutation pairs. This proves the normalizing factor
in (2.1).

For distinct increasing nonnegative exponent sets $S,T$, each of size
$N$, direct permutation expansion gives
$$
 \frac1{N!}\int_{[0,2\pi]^N}
 \det(\lambda_i^{s_j})\overline{\det(\lambda_i^{t_j})}
 \prod_i\frac{d\theta_i}{2\pi}=\mathbf1_{S=T}.
 \tag{2.2}
$$

### 2.2 Elementary symmetric functions

Let $e_k(\lambda)$ be the elementary symmetric function. Multiplying
row $i$ of $\Delta$ by $1+t\lambda_i$ gives
$$
 \Delta(\lambda)\prod_i(1+t\lambda_i)
 =\det(\lambda_i^{j-1}+t\lambda_i^j).
$$
In the column expansion, a choice of a raised exponent followed
immediately by an unraised exponent makes two columns equal. The only
surviving choice with $k$ raised exponents raises the last $k$
columns. Comparing coefficients of $t^k$ proves
$$
 e_k(\lambda)\Delta(\lambda)
 =\det(\lambda_i^s)_{s\in\{0,1,\ldots,N\}\setminus\{N-k\}}.
 \tag{2.3}
$$
Equations (2.1)--(2.3) imply, including $k=0,N$,
$$
 \mathbb E_{\rm CUE}\!\left[e_k(U)\overline{e_l(U)}\right]
 =\mathbf1_{k=l}.
 \tag{2.4}
$$
Since $d_k=(-1)^ke_k$, we have established
$$
 \boxed{\mathbb E_{\rm CUE}
 D_U(z)\overline{D_U(w)}
 =\sum_{k=0}^N(z\overline w)^k
 =\mathcal C_{V_N}(z,w).}
 \tag{2.5}
$$
This is equality of polynomials on all of $\mathbb C^2$, not an
asymptotic statement or an equality restricted to a small Fourier band.

### 2.3 Complete symmetric functions and the inverse determinant

Define $h_m$ by
$$
 \prod_{j=1}^N(1-z\lambda_j)^{-1}
 =\sum_{m=0}^{\infty}h_m(\lambda)z^m,\qquad |z|<1.
$$
For $N\ge2$, consider the alternant with exponent set
$\{0,1,\ldots,N-2,N-1+m\}$. Its generating series over $m$ is
the determinant whose last column is
$\lambda_i^{N-1}/(1-z\lambda_i)$. Multiplying row $i$ by
$1-z\lambda_i$, and then adding suitable multiples of successive
columns from right to left, reduces this determinant to $\Delta$.
Consequently
$$
 h_m(\lambda)\Delta(\lambda)
 =\det(\lambda_i^s)_{s\in\{0,\ldots,N-2,N-1+m\}}.
 \tag{2.6}
$$
The case $N=1$ is immediate. Thus (2.2) gives
$\mathbb E_{\rm CUE}h_m\overline{h_n}=\mathbf1_{m=n}$ for all
nonnegative $m,n$. Absolute convergence for fixed $|z|<1$ follows
also from $|h_m|\le\binom{N+m-1}{m}$. We may integrate the
convergent series, obtaining
$$
 \boxed{\mathbb E_{\rm CUE}|D_U(r)|^{-2}=\frac1{1-r^2},
 \qquad 0<r<1.}
 \tag{2.7}
$$

## 3. A fixed admissible pair test with nonzero defect

The deleted clock has the exact traces
$$
 p_m(V_N)=\sum_{j=1}^Ne^{2\pi imj/(N+1)}
 =\begin{cases}
 N,&N+1\mid m,\\
 -1,&N+1\nmid m.
 \end{cases}
 \tag{3.1}
$$

For completeness, the CUE comparison is
$\mathbb E|p_m|^2=\min(m,N)$ for $m\ge1$.
To verify it from (2.1), expand the two Vandermondes and integrate all
but two variables. The resulting factorial density is
$$
 \rho_{2,N}(\theta,\varphi)
 =N^2-\left|\sum_{j=0}^{N-1}e^{ij(\theta-\varphi)}\right|^2,
$$
with normalized angular measures. The diagonal contribution to
$\mathbb E|p_m|^2$ is $N$; integration against the displayed
density subtracts $\max(N-m,0)$, by counting the pairs of exponents
whose difference is $m$. This proves the claim.

The exact periodization identity in the question, for $k=2$, now gives
for any admissible real $b$
$$
 \Delta_{2,N}^V(b)
 =\frac1{N^2}\sum_{m=1}^{\infty}|\widehat b(m/N)|^2
 \left(|p_m(V_N)|^2-\min(m,N)\right).
 \tag{3.2}
$$
Indeed the term with $m=0$ is the same for every spectrum, and the
two terms $(m,-m)$, $(-m,m)$ cancel the factor $1/2$.

Choose once and for all
$$
 \phi(\xi)=
 \begin{cases}
 \exp[-1/(1-16\xi^2)],&|\xi|<1/4,\\
 0,&|\xi|\ge1/4,
 \end{cases}
 \quad I=\int_{\mathbb R}\phi(\xi)\,d\xi,
 \quad g(x)=\int_{\mathbb R}\phi(\xi)e^{2\pi ix\xi}\,d\xi,
 \quad b(x)=\frac{|g(x)|^2}{2I^2}.
 \tag{3.3}
$$
The bump is smooth, even, nonnegative, and nonzero. Integration by
parts proves that $g$ and $b$ are Schwartz. Also
$|g|\le I$, so $0\le b\le1/2<1$. The Fourier convolution formula
gives
$$
 \widehat b(\xi)=\frac1{2I^2}\int\phi(\eta)\phi(\eta-\xi)\,d\eta.
 \tag{3.4}
$$
This is in $C_c^\infty$, is supported in $[-1/2,1/2]$, and is
strictly positive on $(-1/2,1/2)$.

Every nonzero summand in (3.2) therefore has $m<N/2<N+1$.
Equations (3.1) and (3.2), with $w=|\widehat b|^2$, reduce to
$$
 \Delta_{2,N}^V(b)
 =\frac1{N^2}\sum_{1\le m<N/2}w(m/N)(1-m).
 \tag{3.5}
$$
The contribution of the constant $1$ is $O(1/N)$, and the other
term is a Riemann sum. Hence, along all odd dimensions,
$$
 \boxed{\lim_{N\to\infty}\Delta_{2,N}^V(b)
 =-c_b,\qquad
 c_b:=\int_0^{1/2}u|\widehat b(u)|^2\,du>0.}
 \tag{3.6}
$$
In particular $\epsilon=c_b/2$ gives
$|\Delta_{2,N}^V(b)|\ge\epsilon$ for every sufficiently large odd
$N$. This is an explicit fixed-test failure for the auxiliary
deleted-clock family only.

## 4. The bounded local observable also differs

Restore the missing eigenvalue $1$, but continue to unfold with
the same factor $N$. The full $(N+1)$-clock process is
$$
 \widetilde\Xi_{N,\alpha}
 =\sum_{k\in\mathbb Z}\delta_{s_Nk-N\alpha},
 \qquad s_N=\frac{N}{N+1}.
$$
Since $N=(N+1)s_N$, its distribution is that of
$\sum_k\delta_{s_N(k-T)}$, with $T$ uniform on $[0,1)$.
Couple using this single $T$. As $s_N\to1$, these measures
converge vaguely for every $T$, hence in law, to
$$
 \mathcal L_T=\sum_{k\in\mathbb Z}\delta_{k-T}.
 \tag{4.1}
$$
Removing the point $1$ deletes the periodic process
$\sum_{\ell\in\mathbb Z}\delta_{N(\ell-\alpha)}$. Its expected
mass on a bounded set $J$ is $|J|/N$. Consequently the probability
that deletion changes the measure on any fixed compact interval tends
to zero. It follows that the deleted-clock process has the same limit
(4.1).

This difference from ${\rm Sine}_2$ can be witnessed by a bounded
Laplace observable. Choose a nonzero $f\in C_c^\infty$, $f\ge0$,
whose support has diameter less than one, and set $h=1-e^{-f}$,
$H=\int h$. There is at most one lattice point in this support,
almost surely, so
$$
 \mathbb E e^{-\langle f,\mathcal L_T\rangle}=1-H.
 \tag{4.2}
$$
For any finite family $h_j\in[0,1]$,
$\prod_j(1-h_j)\ge1-\sum_jh_j$, with a strict inequality if at
least two $h_j$ are positive. For ${\rm Sine}_2$, take a small
interval $J$ where $h\ge h_0>0$. Its factorial second moment is
$$
 \int_{J^2}\left[1-
 \left(\frac{\sin\pi(x-y)}{\pi(x-y)}\right)^2\right]dx\,dy>0.
$$
The integrand is strictly positive off the diagonal. Thus the event of
at least two points in $J$ has positive probability. On that event
the previous product inequality has an excess at least $h_0^2$.
The exact intensity one gives
$$
 \boxed{\mathbb E_{\mathrm{Sine}_2}e^{-\langle f,\Xi\rangle}>1-H.}
 \tag{4.3}
$$
This separates the laws by the actual bounded observable needed for
weak convergence, without assuming uniform integrability of a
factorial moment.

## 5. Quantitative failure of inverse-determinant comparison

For $|z|<1$, (1.1) gives the absolutely convergent series
$$
 D_N(z)^{-1}
 =\frac{1-z}{1-z^{N+1}}
 =\sum_{q\ge0}z^{q(N+1)}-
  \sum_{q\ge0}z^{q(N+1)+1}.
$$
The two exponent sets are disjoint for $N\ge1$. Parseval yields
$$
 \boxed{\int_0^{2\pi}|D_N(re^{i\alpha})|^{-2}
 \frac{d\alpha}{2\pi}
 =\frac{1+r^2}{1-r^{2(N+1)}}.}
 \tag{5.1}
$$
At the microscopic radius $r_N=e^{-s/N}$, fixed $s>0$,
$$
 \int|D_N(r_Ne^{i\alpha})|^{-2}\frac{d\alpha}{2\pi}
 \longrightarrow\frac{2}{1-e^{-2s}},
 \qquad
 \frac1N\mathbb E_{\rm CUE}|D_U(r_N)|^{-2}
 \longrightarrow\frac1{2s}.
 \tag{5.2}
$$
Thus the ratio of these two inverse-determinant moments tends to zero,
although their direct determinant autocorrelations are exactly equal
at every $N$, including at $r_N$.

## 6. Consequence for the original determinant route

The exact determinant identities, exterior-power representation,
self-inversiveness, or even the hypothetical full identity
$\mathcal C_{U_N}=\mathcal C_{\rm CUE}$ do not justify replacing
mixed ratios by CUE ratios. Differentiating a two-determinant product
does not give a product of logarithmic derivatives: the latter contains
reciprocal determinants. Equations (2.5) and (5.2) isolate this loss
quantitatively.

The auxiliary family does not have the prescribed Fourier--Jacobi
construction. Therefore this theorem cannot be used as a rejection of
the original $H_{\rm diag}$. Its legitimate use is to reject a
specific insufficient inference while searching for an estimate that
uses the original family in its mixed ratios or full trace sums.

The first unresolved original test remains
$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)\longrightarrow0,
$$
for the fixed $b_*$ specified in the continuation ledger. No estimate
of this expression is asserted in this note.

## 7. Input identities and reproducibility

The proof above is elementary and independent of the old all-time
stationary-phase claims. The following actual local sources were read
to identify what had already been obtained and to avoid recasting it
as new work. Hashes were computed on 21 October 2026.

| Source | SHA-256 |
|---|---|
| `research_round8_2026_10_21/round8_continuation_ledger.md` | `84469e7eb461cd3c18929424cf3bcdce8e1e6b525d8d077bf61a01adc7d652e7` |
| `research_continuation_2026_10_20/exact_dynamical_determinant.md` | `e75d4e7477246e189ba56f0b6bbbda4d806ad1e8bb114e1f4b7d07613b8f0035` |
| `research_continuation_2026_10_20/selfinverse_countermechanism.md` | `5eaa20f8d1c3621ac69c526db33ba41eed761cbbbd637a8ed77a12bcdedeaf42` |
| `research_round2_2026_10_20/fermionic_pseudoorbit_cutoff.md` | `03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb` |
| `research_round2_2026_10_20/fermionic_resolvent_frame.md` | `1e88189aa0192786ad4947091079efa93079aad8fe9a7194a00692c0fccb184f` |
| `research_round4_2026_10_21/audit_exact_identities_and_closure.md` | `7fc90f4202399ff5fe4a719282ffa0723fd0eb4e16291ac891d13f164ffcd712` |
| `research_round7_2026_10_21/root_original_every_power_minors.md` | `9d3503703b5a5b0df580bb1a2a42e58a0617c7de94c3b340ac26d9ec93d54a48` |

No old file or master document was modified by this branch.
