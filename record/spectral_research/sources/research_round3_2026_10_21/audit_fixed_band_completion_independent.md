> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_fixed_band_completion_independent.md`. Embedded SHA256: `cb313ab79e316bd489192876d1411351136b2d833506a57a981a1a1d5f6c36d2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Independent audit of the fixed-band completion countermodel

Date: 2026-10-21.

## Verdict and exact scope

**The frozen statement is justified. No mathematical gap or counterexample was found after reconstructing the ensemble, covariance estimate, tail passage, and deterministic selection.** The result supplies, for each prescribed finite band $B$, a different deterministic unitary sequence matching every fixed factorial order for every admissible test in that band, but failing a test in a larger fixed band. The sequence is selected in every odd dimension.

This is an exclusion of the stated general completion mechanism. It is neither a counterexample to the specified kicked family $U_N$ nor a proof or refutation of its full $H_{\rm diag}$. The constructed sequence depends on the prescribed band $B$. No claim is made of one sequence matching every finite band while failing full $H_{\rm diag}$.

Audited source, read in full before reconstructing the arguments:

research_round3_2026_10_21/fixed_band_completion_countermodel.md

SHA-256:

ee6590231f03a40a36e2a6929145f6c9595a1c14d17e8096ff86621cd71d6fa8

The project's normalization of $M_{k,N}$ was checked against
research_continuation_2026_10_20/finite_identities_and_closure.md,
SHA-256
e1d85ef8ecff65a1fecffe200185d9e721dce14f9c356705cc04f5c97ffd6d35.

No earlier PASS report was used. No source file was modified.

## 1. Finite ensemble and exact equality in the prescribed band

Write $A=1+\eta$, let $P=\Pi_N$, and put
$$
a_\phi(\theta)=1+\eta\cos(2\pi\omega N\theta+\phi).
$$
The nonconstant frequencies of $a_\phi$ are $\pm\omega N$.
Entries of $Pa_\phi P$ use frequencies $i-j$, where
$|i-j|\le N-1<\omega N$. Hence $Pa_\phi P=P$, exactly.

Therefore $f_j=\sqrt{a_\phi}e_j$, $0\le j<N$, are orthonormal.
Expansion of the two determinants and coordinatewise integration gives
$$
\int\left|\det[f_j(\theta_l)]\right|^2\,d\theta_1\cdots d\theta_N=N!.
$$
Inserting $\prod_l(1+t v(\theta_l))$ in the same calculation replaces
the Gram matrix by
$$
I+t[\langle e_i,a_\phi v e_j\rangle]_{i,j=0}^{N-1}.
$$
This proves the claimed generating polynomial without assuming an
infinite determinantal-process construction. Integrating all but $r$
coordinates gives the finite factorial densities of
$$
K=M_{\sqrt{a_\phi}}PM_{\sqrt{a_\phi}},\qquad K^2=K.
$$

For a band-$B$ test, a possibly nonzero entry of
$P(a_\phi-1)b_NP$ would require
$$
|m|=|\omega N\pm(i-j)|
\ge(\omega-1)N+1>BN.
$$
But $\widehat{b_N}(m)=N^{-1}\widehat b(m/N)=0$ there.
Translation of $b_N$ only multiplies its Fourier coefficients by phases.
Consequently the inserted Gram matrix is exactly the CUE matrix for every
translation and every $\phi$. Comparing polynomial coefficients proves
$$
\mathbb E_\phi M_{k,N}(b)=M^{\mathrm{CUE}}_{k,N}(b)
$$
at every order, including the zero coefficients $k>N$. Here
$\mathbb E_\phi$ denotes conditional expectation in the ensemble with
the phase fixed, not a phase average. There is no order-dependent
band enlargement in this calculation.

## 2. Limit process and a test with strictly positive discrepancy

After unfolding, a kernel gauge removes the central frequency, giving
$$
\widetilde K_{N,\phi}(x,y)=
\sqrt{a_\phi(x)a_\phi(y)}
\frac{\sin\pi(x-y)}{N\sin(\pi(x-y)/N)}.
$$
On fixed compact sets the scalar quotient converges uniformly to
$\operatorname{sinc}(\pi(x-y))$. Positivity of the finite Gram matrix
and its diagonal bound yield
$$
0\le\rho_{r,N,\phi}\le A^r.
$$
The Fredholm series for compactly supported $0\le h\le1$ is therefore
dominated term by term by $A^r\|h\|_1^r/r!$. This proves the claimed
Laplace convergence. The expected compact counts are bounded, giving
tightness.

One useful explicit completion of the source's simplicity statement is
as follows. In a bounded interval $I$, the expected number of ordered
distinct-label pairs at separation at most $\delta$ is bounded by
$2A^2|I|\delta$, up to a harmless enlargement of $I$.
The same bound passes to the limit using bounded continuous cutoffs and
the uniform higher count moments from $\rho_r\le A^r$.
Letting $\delta$ decrease to zero excludes multiplicities.
Thus the limiting locally finite counting measure is indeed simple.

Translation rotates $\phi$; uniform phase mixing is stationary.
Its diagonal density averages to one. Direct multiplication gives
$$
\frac1{2\pi}\int_0^{2\pi}a_\phi(x)a_\phi(y)\,d\phi
=1+\frac{\eta^2}{2}\cos(2\pi\omega(x-y)).
$$
This yields exactly the stated two-point density.

For an independent check of the detecting-test constant, put
$$
C_b(r)=\int_{\mathbb R}b(y+r)b(y)\,dy,\qquad
\widehat C_b(u)=|\widehat b(u)|^2
$$
for real $b$. Since the sinc function is the inverse Fourier transform
of $1_{[-1/2,1/2]}$, its square transforms into
$T(u)=(1-|u|)_+$. The pair correction is therefore
$$
\frac{\eta^2}{4}\left[
|\widehat b(\omega)|^2-
\int_{-1}^1T(u)|\widehat b(\omega-u)|^2\,du\right].
$$
The factor $1/4$ includes both the phase average and the unordered-pair
normalization.

For the specified $b_+=cw(1+\cos 2\pi\omega x)$, only its Fourier bump
near $+\omega$ enters the last integral. That bump has width $2\delta$
and modulus at most $|\widehat b_+(\omega)|$. Hence the integral is at
most $2\delta|\widehat b_+(\omega)|^2$. Its discrepancy is bounded below
by the positive number in source equation (5.4). Nonnegativity,
Schwartz decay, compact smooth Fourier support, and the upper bound
$b_+\le1/2$ all hold.

## 3. Reconstructing the two-crossing covariance estimate

This is the principal potential failure point; it survives direct
expansion.

Work on the unfolded circle $C_N$ of length $N$.
For bounded $b$ supported in $[-R,R]$, define explicitly
$$
F_{k,b}(t)=\frac1{k!}
\sum_{j_1,\ldots,j_k\ {\rm distinct}}
\prod_{\nu=1}^k b_{[N]}(x_{j_\nu}-t),
\qquad
b_{[N]}(z)=\sum_{\ell\in\mathbb Z}b(z+\ell N).
$$
For $N>8R$, each label has at most one image in either individual
window. If their centers are at circular distance $d>4R+1$, the
windows are disjoint and a label cannot occur in both. Thus the product
expectation is exactly the $2k$-point determinant integral with
coefficient $(k!)^{-2}$.

Subtracting the product of the separate expectations cancels every
permutation preserving both blocks. A remaining permutation maps at
least one row in the first block to a column in the second. Bijectivity
forces at least one row in the second block to a column in the first.
Thus at least two factors cross; a single-crossing term is impossible.

For any such cross factor,
$$
\operatorname{dist}_N(x-y,0)\ge d-2R,\qquad
|\widetilde K_{N,\phi}(x,y)|\le \frac{A}{2(d-2R)}.
$$
Every other factor has modulus at most $A$. There are at most
$(2k)!$ permutations, and integration of the absolute weights yields
a factor at most $\|b\|_1^{2k}$. For example a valid separated-window
bound is
$$
|\operatorname{Cov}_\phi(F_{k,b}(t),F_{k,b}(s))|
\le
\frac{(2k)!}{(k!)^2}
\frac{A^{2k}\|b\|_1^{2k}}{4(d-2R)^2}.
$$
The source's more flexible constant is justified.

For overlapping windows, expand $F_{k,b}(t)F_{k,b}(s)$ by the number
and placement of shared labels. Each resulting integral has between
$k$ and $2k$ distinct labels, density bounded by $A^r$, and
integrable factors bounded using $\|b\|_1,\|b\|_\infty$.
This gives a uniform constant independent of $N,t,s,\phi$.
Combining both regimes gives $C(1+d)^{-2}$.

Mixed fixed factorial weights and ordinary local-count powers obey the
same argument after partitioning repeated labels. Neither independence
nor a mixing assertion for the phase mixture is being assumed.

## 4. The phase mixture does not leave a variance floor

A potentially serious pitfall would be an order-one variance of the
conditional mean. It is absent here.

Rotation of the original angle by $\phi/(2\pi\omega N)$, equivalently
an unfolded translation by $\phi/(2\pi\omega)$, with the sign chosen
according to the convention, carries the conditional ensemble at phase
$\phi$ to the phase-zero ensemble. The full spatial statistic
$$
M_{k,N}(b)=N^{-1}\int_{C_N}F_{k,b}(t)\,dt
$$
is invariant under this rotation, exactly, including its periodizations.
Therefore its conditional distribution, and in particular its
conditional mean, is independent of $\phi$.

The conditional covariance bound now gives
$$
\begin{aligned}
\operatorname{Var}_\phi M_{k,N}(b)
&\le N^{-2}\int_{C_N}\int_{C_N}
C(1+\operatorname{dist}_N(t-s,0))^{-2}\,dt\,ds\\
&\le \frac{2C}{N}\int_0^\infty(1+r)^{-2}\,dr
=\frac{2C}{N}.
\end{aligned}
$$
The second term in the total-variance formula is zero.
Thus the unconditional variance bound is valid.

The integer choice of $\omega$ is relevant: the finite modulation is
well-defined on the circle, and an entire spatial period is averaged.
A general nonperiodic modulation would not inherit this calculation.

## 5. The restricted tail passage is sufficient and correct

The source has already restricted its tail claim to Schwartz tests,
$w_0(x)=(1+x^2)^{-1}$, and their indicated fixed products and truncations.
That restriction matters.

For any of these fixed absolute test functions $g$,
$$
\sum_{n\in\mathbb Z}\sup_{x\in[n,n+1]}g(x)<\infty.
$$
Since a lattice of spacing $N\ge1$ has at most one point per half-open
unit interval, its periodization satisfies a uniform supremum bound.
Also,
$$
\int_{C_N}g_{[N]}=\int_{\mathbb R}g.
$$
These facts hold uniformly in every positive integer $N$, including
the small dimensions.

For a direct polynomial estimate, write
$Z_g=\sum_jg_{[N]}(x_j-t)$. Expanding a product of such counts by
partitions of its labels expresses its expectation as a finite sum of
integrals
$$
\int_{C_N^r}\rho_{r,N,\phi}(z_1,\ldots,z_r)
\prod_{\beta=1}^r\prod_{i\in B_\beta}
g_{i,[N]}(z_\beta-t)\,dz.
$$
Use $\rho_r\le A^r$. In each block, retain one factor in $L^1$ and
bound the rest by their uniform suprema.

If one factor is a tail $g1_{\{|x|>R\}}$, choose that factor as the
$L^1$ factor in its block. The corresponding integral is then bounded
by a constant times
$\int_{|x|>R}g(x)\,dx$, which tends to zero. All other blocks remain
uniformly bounded.

In particular, telescoping the factorial polynomial gives
$$
|F_{k,b}(t)-F_{k,b1_{[-R,R]}}(t)|
\le C_k Z_{|b|1_{\{|x|>R\}}}Z_{|b|}^{\,k-1}.
$$
Squaring and applying the preceding partition bound proves a uniform
$L^2$ error tending to zero. Jensen's inequality passes the same bound
to the spatial average. The identical argument treats $Z_{w_0}^p$.

Thus compact-window concentration extends to precisely the tests used
in deterministic selection. Expectations converge to the limiting
process moments by the same truncation bound. In particular every
$Q_{p,N}$ converges in probability to a finite $q_p$.

This proof would not apply to all bounded integrable functions. For
example, bounded narrow spikes around every integer can have finite
integral while their periodization diverges at a point. The frozen
source does not make that stronger assertion.

## 6. Laplace concentration

For $f\ge0$ continuous and compactly supported, set $h=1-e^{-f}$.
For sufficiently large $N$, at most one periodic image of a label
meets its support, so the local Laplace functional is exactly the
product over labels of $1-h_{[N]}$.

Bonferroni bounds its spatial average between two consecutive finite
factorial sums. Every fixed term concentrates by the compact-window
argument. The limiting difference of the two sums is bounded by
$$
A^J\|h\|_1^J/J!,
$$
which tends to zero. Choose $J$ first, then let $N$ tend to infinity.
This proves convergence in probability of each selected averaged
Laplace observable. It does not require a covariance estimate for a
nonlinear exponential.

## 7. Selection in every odd dimension and extension to all tests

There is no hidden subsequence selection.

The admissible band-$B$ tests form a subspace, in the topological
sense, of the second-countable Schwartz space. Any such subset is
separable. Inclusion into
$\|b\|_{w_0}=\sup_x(1+x^2)|b(x)|$ is continuous. A countable dense set
in the relative Schwartz topology is therefore dense in the requested
weighted norm as well; all selected approximants remain admissible and
in the same band.

List their fixed factorial orders, the detecting test, all $Q_p$, and
the chosen Laplace observables. For each integer $q$, convergence in
probability implies that the probability of satisfying the first $q$
strict inequalities with tolerance $1/q$ tends to one. Choose an
increasing threshold $N_q$ for which that probability is positive for
**every** odd $N\ge N_q$. This is possible by the definition of
convergence in probability along the full odd sequence.

For each odd $N$, choose a configuration satisfying the first
$q(N)=\max\{q\le N:N_q\le N\}$ inequalities. Then $q(N)\to\infty$
and every fixed listed observable converges. The rule selects one
configuration separately at every dimension.

The optional rational-angle rule is also legitimate. All listed
observables are continuous in the finitely many angles: the Schwartz
and $w_0$ periodizations converge uniformly, and the selected Laplace
tests are continuous. A nonempty strict good set is open and therefore
contains a rational-angle configuration.

The essential all-test estimate is valid with exactly the source's
constant. If
$$
|b-c|\le\epsilon w_0,\qquad |b|,|c|\le Cw_0,
$$
put $z_j=(w_0)_{[N]}(x_j-t)$. For each unordered $k$-tuple,
telescoping gives a bound $k\epsilon C^{k-1}\prod z_j$.
Since $e_k(z)\le(\sum_jz_j)^k/k!$,
$$
|M_{k,N}(b)-M_{k,N}(c)|
\le\frac{\epsilon C^{k-1}}{(k-1)!}\,Q_{k,N}.
$$
Selection of $Q_k$ bounds the right side uniformly in large $N$.
The same estimate holds at the limit using $q_k<\infty$.
Density therefore extends convergence to every fixed admissible test
in the prescribed band. No moment conclusion is being extracted from
weak convergence alone.

Finally, exact intensity one gives tightness of the selected
random-translate laws and
$$
|L_N(f)-L_N(g)|\le\|f-g\|_1
$$
for nonnegative tests. A countable $L^1$-dense determining collection
therefore identifies every subsequential limit with the already
constructed stationary simple law. The whole odd sequence converges.

## 8. What survives, and what does not follow

The following claims survive this audit:

- Exact ensemble equality with finite CUE factorial moments in the
  prescribed band, at all finite orders.
- A stationary simple local limit with the stated modulated two-point
  density and a rigorously positive detecting-test discrepancy.
- Concentration of every fixed observable used in the selection.
- One deterministic configuration in each odd dimension.
- Extension from countably many tests to every admissible band-$B$
  test, with the necessary moment bounds supplied explicitly by $Q_p$.

The proof is an existence argument, not an effective bound for how
large $N$ must be. It supplies no convergence uniform in growing
factorial order, moving tests, or growing bands; none is claimed.
It does not include the special kicked family's orbit phases,
subprincipal weights, or trace formula among its matching hypotheses.
Those original-family conditions can therefore still distinguish
$U_N$ from this construction.

The explicit pair-separation argument above fills the short simplicity
justification; the explicit coincidence-partition argument fills the
compressed tail estimate. Both follow from hypotheses and bounds
already established in the frozen text. Neither requires an additional
external theorem or a change to its statement.
