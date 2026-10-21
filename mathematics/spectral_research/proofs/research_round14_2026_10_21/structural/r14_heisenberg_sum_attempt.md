> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round14_2026_10_21/structural/r14_heisenberg_sum_attempt.md`. Embedded SHA256: `16b767447bf11c7da1d33819a9614f9884daaf699e702fe798b200e198372a99`.
> [Thematic guide](../../../topics/closure.md).

# Continued attempt on the full weighted trace sum

21 October 2026. Round 14, structural branch. This records the attempt made **after** proving the quartic one-step return calculation. It does not declare that calculation a solution of the original spectral-statistics problem.

## 1. Exact target and a fixed nonzero plateau correction

Retain the fixed test from the Round 13 main report:

$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
I=\int\phi,\quad b_*=|\mathcal F^{-1}\phi|^2/(2I^2),
\quad w=|\widehat b_*|^2.
$$

Then $w$ is smooth, nonnegative, supported in $[-2,2]$, and strictly positive on $(-2,2)$. The first original obligation is

$$
\Delta_{2,N}(b_*)={1\over N^2}\sum_{1\le m<2N}w(m/N)
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\longrightarrow0.
\tag{1.1}
$$

Define

$$
\delta_*:=\int_1^2(t-1)w(t)\,dt>0.
\tag{1.2}
$$

This is a concrete fixed constant. For example, for $1\le t\le5/4$, integrate the convolution $\phi*\phi$ over $1/2\le u\le5/8$. Both $|u|$ and $|t-u|$ are at most $3/4$, so

$$
\phi*\phi(t)\ge\tfrac18e^{-32/7},\qquad I\le2,
\quad w(t)\ge 2^{-12}e^{-64/7}.
$$

Consequently

$$
\delta_*\ge2^{-17}e^{-64/7}>0.
\tag{1.3}
$$

This is not an epsilon for a counterexample; it is the magnitude of a correction that a successful original-family cancellation proof must produce below.

## 2. The actual all-time path class, and recognition of an old result

Let $P_{xy}=|U_N(x,y)|^2$, $J_{xy}=1/N$. For a rooted cyclic word $x=(x_0,\ldots,x_{m-1})$, set

$$
a_N(x)=\prod_{j=0}^{m-1}U_N(x_j,x_{j+1}),\qquad x_m=x_0.
$$

Let $\operatorname{Rot}(x)$ be its set of distinct cyclic rotations, and define

$$
D_{m,N}=\sum_x\sum_{y\in\operatorname{Rot}(x)}
a_N(x)\overline{a_N(y)}\ge0,
$$
$$
Y_{m,N}=\sum_x\sum_{y\notin\operatorname{Rot}(x)}
a_N(x)\overline{a_N(y)}.
\tag{2.1}
$$

Then $|\operatorname{Tr}U_N^m|^2=D_{m,N}+Y_{m,N}$ exactly. No modulus has been taken inside the complementary phase sum.

The natural extension of the new four-sheet result is to use the already proved original-family bounds
$\max P_{xy}\le C/N$ and $\|P-J\|\le1/2$. The new quartic kernel result improves the limiting gap constant, but a check of the historical files showed that the resulting all-time rotational calculation was **already proved**, including all repeated-word corrections, in `research_round5_2026_10_21/root_physical_cycle_classes.md`, Sections 1–3. It is not claimed as a new theorem here. Its exact quantitative conclusion is

$$
\sum_{m\ge1}|D_{m,N}-m|\le7C+1+8C^2/N.
\tag{2.2}
$$

Here is the argument, so that its use is concrete. If a word has least period $d(x)$, it has exactly $d(x)$ distinct rotations. Hence
$D_m=\sum_xd(x)|a(x)|^2$, while $m\operatorname{Tr}P^m=\sum_xm|a(x)|^2$. A word with proper period dividing $d\mid m$ contributes total weight at most
$(C/N)^{m-d}\operatorname{Tr}P^d\le C(C/N)^{m-d}$.
Every proper divisor is at most $m/2$, giving

$$
0\le m\operatorname{Tr}P^m-D_m\le Cm^2(C/N)^{m/2}.
$$

Summing the geometric majorant gives $8C^2/N$ for $N\ge16C^2$. Next, $A=P-J$ has $\|A\|_{\rm HS}^2\le C$, and

$$
|\operatorname{Tr}A^m|\le C2^{-(m-2)}\quad(m\ge2),
\qquad |\operatorname{Tr}P-1|\le C+1.
$$

Summing $m|\operatorname{Tr}P^m-1|$ gives $7C+1$. These arguments give (2.2) through all times, not just fixed times or logarithmic times.

It follows after the **full** weighted time sum that

$$
\frac1{N^2}\sum_{1\le m<2N}w(m/N)D_{m,N}
=\frac1{N^2}\sum_{1\le m<2N}m w(m/N)+O_w(N^{-2})
\longrightarrow\int_0^2t w(t)\,dt.
\tag{2.3}
$$

Subtracting the exact CUE term in (1.1) leaves the following equivalent original obligation:

$$
\boxed{\quad {1\over N^2}\sum_{1\le m<2N}w(m/N)Y_{m,N}
\longrightarrow-\delta_* .\quad}
\tag{2.4}
$$

In particular, it would be wrong to try to bound this entire remaining class by $o(1)$: that would predict the unbroken linear ramp and would fail the fixed band-two CUE comparison. The required correction is nonzero and negative. This is the precise point at which a calculation based only on the positive one-step probability kernel ceases to give the target.

The new Round 14 one-step theorem identifies the first member of this old remainder:

$$
Y_{1,N}=|\operatorname{Tr}U_N|^2-\sum_x|U_N(x,x)|^2,
\quad \liminf Y_{1,N}\ge200\tau.
$$

Its positive contribution divided by $N^2$ vanishes. It neither gives (2.4) nor contradicts its required negative total limit.

## 3. Actual summed bounds available for the complement

Let $W=\|w\|_\infty$, $L_N=2N-1$. From unitarity and (2.2), retaining the signed sum until it is formed,

$$
\begin{aligned}
-{1\over N^2}\sum_{m\le L_N}m w(m/N)-O_w(N^{-2})
&\le {1\over N^2}\sum_{m\le L_N}w(m/N)Y_{m,N}\\
&\le\sum_{m\le L_N}w(m/N)
-{1\over N^2}\sum_{m\le L_N}m w(m/N)+O_w(N^{-2}).
\end{aligned}
\tag{3.1}
$$

Indeed the omitted original term is exactly the nonnegative sum
$N^{-2}\sum_mw(m/N)|\operatorname{Tr}U_N^m|^2$, bounded above by $\sum_mw(m/N)$. Thus the actual bounds furnished by this route are a finite lower bound and an $O_w(N)$ upper bound. They do not even give the required boundedness of the original weighted second moment, let alone the definite negative limit (2.4).

The stronger fixed gap produced by $k_t=1+O(\tau^4)$ affects the absolutely summable error in (2.2), already multiplied by $N^{-2}$. It supplies no estimate for $Y$. This is a quantitative failure after the time sum, not merely a statement that the number of sheets grows.

## 4. Removing a possible quantum-remainder excuse

A second attempted route was to repeat the one-step four-sheet approximation up to $2N$ powers. The following direct error calculation shows where a naive approximation fails and how far correcting it actually gets.

For a matrix $V_N$, put $\varepsilon_N=\|U_N-V_N\|_{\rm HS}$. If $N\varepsilon_N\le1$, telescoping powers gives, uniformly for $m\le2N$,

$$
\|U_N^m-V_N^m\|_{\rm HS}
\le m\varepsilon_Ne^{2N\varepsilon_N},
$$

because $\|V_N\|\le1+\varepsilon_N$. Therefore

$$
|\operatorname{Tr}(U_N^m-V_N^m)|
\le\sqrt N\,m\varepsilon_Ne^{2N\varepsilon_N}.
$$

Using $|\operatorname{Tr}U_N^m|\le N$ and
$|\operatorname{Tr}V_N^m|\le Ne^{2N\varepsilon_N}$, and only then summing in time, gives

$$
\boxed{\left|{1\over N^2}\sum_{m<2N}w(m/N)
\left(|\operatorname{Tr}U_N^m|^2-|\operatorname{Tr}V_N^m|^2\right)\right|
\le C_w N^{3/2}\varepsilon_N.}
\tag{4.1}
$$

This estimate concerns the whole weighted expression. It does not take the modulus of each individual orbit amplitude.

For the leading four-sheet amplitude, the elementary finite-shift estimate only gives $\varepsilon_N=O(N^{-1/2})$. To discuss that order without uncontrolled growth of $V_N^m$, replace $V_N$ by its unitary polar factor. The replacement is well defined for sufficiently large $N$, and changes the Hilbert–Schmidt distance to $U_N$ by at most a factor two. In fact the polar factor minimizes the distance from $V_N$ to a unitary matrix: an SVD reduces this statement to $\Re\operatorname{Tr}(W\Sigma)\le\operatorname{Tr}\Sigma$. The triangle inequality then gives the factor two. For unitary endpoints the telescoping argument in (4.1) needs no exponential factor. Its leading-order bound is only $O_w(N)$.

There is no intrinsic obstacle to improving the **one-step** approximation. The exact finite-shift amplitude operator, after removal of the Hamilton–Jacobi phase, has a Taylor expansion

$$
\mathcal L_h=\mathcal L_0+h\mathcal L_1+h^2\mathcal L_2+O(h^3)
$$

on the fixed smooth strip norms required at this finite order. Each coefficient follows by Taylor expansion of the finitely many shifts and their phases. The leading operator is the transport operator proved in the main note. Solve the successive inhomogeneous transport equations

$$
\partial_tB_j=\mathcal L_0B_j+
\sum_{r=1}^j\mathcal L_rB_{j-r},\qquad
B_0(0)=1,\quad B_j(0)=0\ (j\ge1).
\tag{4.2}
$$

Characteristics on the same fixed small-time strip give bounded smooth solutions; the deck identities are preserved by uniqueness and the exact Weyl covariance of the amplitude operator. Inserting $B_0+hB_1+h^2B_2$ in each of the four sheets leaves evolution residual $O(h^3/\sqrt N)$ per entry. The same column Duhamel argument as in the main note consequently gives

$$
\varepsilon_N=O(N^{-5/2}).
\tag{4.3}
$$

This is enough in (4.1) for an $O_w(N^{-1})$ comparison throughout $m<2N$. An amplitude retained through order $h$ would instead give only the threshold bound $O_w(1)$; through order $h^2$, the comparison does tend to zero. No growing-time Fourier-integral parametrix or expansion of tau is required for this error estimate: the one-step matrix is approximated accurately, then finite matrix powers are telescoped.

This construction is a technical replacement of the exact original matrix by a controlled one-step model. It is **not** the missing signed-sum estimate. Related microscopic replacement theorems already exist in the project, especially `research_round3_2026_10_21/subprincipal_stability_theorem.md`; Sections 1–4 of that source were read here. Its quantum-ergodicity argument handles appropriate smooth subprincipal unitary paths more sharply than the norm estimate just displayed. No novelty or substantive universality conclusion is claimed for (4.1)–(4.3).

Even granting arbitrarily high one-step accuracy, the power trace of the resulting explicit four-sheet matrix still contains the full coherent cyclic-history sum. The corrected amplitudes do not evaluate its off-rotation class or generate the negative constant in (2.4).

## 5. Summing time before eliminating independent coordinate phases

There is also an exact way to keep all time cancellations before attempting a phase comparison. For a visit vector $v\in\mathbb Z_{\ge0}^N$ with $|v|_1=m$, define

$$
C_{m,N}(v)=\sum_{x:\,\#\{j:x_j=a\}=v_a\ \forall a}a_N(x).
$$

Then

$$
\operatorname{Tr}(D_\varphi U_N)^m
=\sum_{|v|_1=m}C_{m,N}(v)e^{2\pi i v\cdot\varphi}.
\tag{5.1}
$$

Form the entire weighted phase polynomial first:

$$
F_N(\varphi)={1\over N^2}\sum_{m<2N}w(m/N)
|\operatorname{Tr}(D_\varphi U_N)^m|^2
=\sum_{\nu:\,\sum\nu_a=0}c_N(\nu)e^{2\pi i\nu\cdot\varphi},
\tag{5.2}
$$

where the finite coefficients are exactly

$$
c_N(\nu)={1\over N^2}\sum_{m<2N}w(m/N)
\sum_{\substack{|v|_1=|u|_1=m\\v-u=\nu}}
C_{m,N}(v)\overline{C_{m,N}(u)}.
\tag{5.3}
$$

Thus the prospective original-to-coordinate-phase comparison is

$$
F_N(0)-\int F_N(\varphi)d\varphi
=\sum_{\nu\ne0}c_N(\nu).
\tag{5.4}
$$

The time sum is already inside each $c_N$. Independent phase integration removes $\nu\ne0$; the allowed common phase removes none of these characters, since $\sum\nu_a=0$ identically. This exact reformulation does not add an averaging permission.

At $m\asymp N$, the unrestricted visit-vector space has dimension
$\binom{N+m-1}{m}$, exponential in $N$. Consequently the generic Cauchy–Schwarz point-evaluation bound for (5.1),

$$
|\operatorname{Tr}U_N^m|^2
\le\binom{N+m-1}{m}\int|\operatorname{Tr}(D_\varphi U_N)^m|^2d\varphi,
$$

is useless at the required scale. It is only an upper bound on what an arbitrary coefficient argument can do; no claim is made that the original coefficients saturate it. Applying unitarity directly to (5.2) gives the better but still insufficient bound

$$
0\le F_N(\varphi)\le\sum_{m<2N}w(m/N)\le2WN,
\quad |F_N(0)-\textstyle\int F_N|\le2WN.
\tag{5.5}
$$

No estimate of $\sum_{\nu\ne0}c_N(\nu)$ tending to zero is obtained. The original four-sheet cancellation establishes specific one-step oscillations and the coefficient of $Y_{1,N}$. It gives neither joint control of the coefficients (5.3) nor their required signed cancellation after summing times proportional to $N$.

## 6. Outcome of the continued attempt

The one-step approximation can be made accurate enough that its contribution to the full weighted quantum error is $o(1)$. The rotational path class can already be summed with $O(N^{-2})$ error, and its value is the full linear ramp. Both checks leave an explicit coherent remainder whose required original-family limit is the **nonzero negative constant** in (2.4). The direct upper bound obtained by this extension is only $O(N)$, as displayed in (3.1), while this direct independent-phase comparison gives only (5.5). These are the bounds of the present attempt, not a claim that every earlier method in the master has the same bound.

Accordingly the first undischarged estimate remains (1.1), equivalently (2.4). Neither it nor a fixed-test countersequence has been proved in this branch. The quartic original return theorem is a verified additional result, and this note identifies precisely why it does not close the remaining problem.
