> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round14_2026_10_21/structural/r14_original_coordinate_phase_bridge_test.md`. Embedded SHA256: `4bc02ec2a3565f34c33a830db584cf761e62e5b69c23c7a727ab124046ca583a`.
> [Thematic guide](../../../topics/classical_trace.md).

# An original-family test of the independent-coordinate-phase bridge

21 October 2026. Round 14, structural-correlation branch.

## 0. Status, scope, and exact result

The original all-odd-dimensional, fixed-parameter `H_diag` is still neither proved nor disproved. This note proves a quantitative statement about the **original matrices**, rather than an auxiliary flat matrix counterexample. It tests the precise averaging step needed before a quantum-graph phase-ensemble argument could be applied.

Throughout, `tau = 10^-80` is the exact prescribed constant and

$$
U_N=e^{i\tau N A_N}M_N,\qquad N\ge3\text{ odd},\qquad
t_*={\tau\over2\pi}.
$$

Define

$$
\mathcal D_N=\sum_{x=0}^{N-1}|U_N(x,x)|^2.
$$

**Theorem A.** There is a positive real-analytic, doubly periodic function $k_t(Q,s)$, defined at the fixed time $t=t_*$, such that

$$
\boxed{\quad \mathcal D_N\longrightarrow\int_0^1 k_{t_*}(q,q)\,dq,
\qquad |k_{t_*}(Q,s)-1|\le10^{44}\tau^4.\quad}
\tag{0.1}
$$

The first three Taylor coefficients of $k_t-1$ at $t=0$ vanish identically. The limit in (0.1) is through **all odd dimensions**. No average over dimensions or change of tau occurs.

**Corollary B, using the proved Round 13 trace formula.** For the same original matrices,

$$
\boxed{\liminf_{N\to\infty,\ N\ {\rm odd}}
\left(|\operatorname{Tr}U_N|^2-\mathcal D_N\right)\ge200\tau>0.}
\tag{0.2}
$$

The relevant Round 13 trace input, its proof location, and the algebra yielding (0.2) are recorded in Section 7. The new proof of Theorem A is given below without using the old operator-norm limit of $|U_N|^{\circ2}$: operator-norm convergence alone would not justify taking its matrix trace.

For $D_\varphi=\operatorname{diag}(e^{2\pi i\varphi_x})$, exact character orthogonality gives

$$
\int_0^1|\operatorname{Tr}(e^{-2\pi i\alpha}U_N)|^2d\alpha
=|\operatorname{Tr}U_N|^2,
\quad
\int_{\mathbb T^N}|\operatorname{Tr}(D_\varphi U_N)|^2d\varphi
=\mathcal D_N.
\tag{0.3}
$$

Consequently the allowed common spectral shift and independent coordinate phases are not interchangeable even with a pointwise $o(1)$ error in the first unnormalized form factor of this family. This statement does **not** disprove a bridge after the full microscopic weighted sum. The first-time discrepancy in (0.2), divided by $N^2$, tends to zero. Section 8 leaves the required long-time comparison explicitly open.

## 1. Correct ordinary symbol and uniform analytic phase

Put $h=(2\pi N)^{-1}$. For integer Fourier labels,

$$
(W_N(k,l)\psi)(x)
=e^{2\pi ikx/N+\pi ikl/N}\psi(x+l),
\qquad T_N(l,k)=(-1)^{kl}W_N(k,l).
$$

The latter equality follows by representing the modular inverse of two by $(N+1)/2$; the coordinate shift is still reduced modulo $N$. Thus the exact ordinary symbol of $A_N$ is

$$
a(Q,p)=V(Q)+{R(Q)\over100}\cos(2\pi p-\alpha_0),
\tag{1.1}
$$
$$
V(Q)=\cos(14\pi Q)+{r(Q)\over10}
 +{r(Q)\sin(2\pi Q)\over100}-{1\over10},
\qquad R(Q)=r(Q+1/2).
$$

It has Fourier support $|k|+|l|\le9$, $|l|\le1$, with total absolute coefficient sum less than two. In particular, it is of degree one in the momentum Fourier variable. This specific feature will matter in Section 4.

Let

$$
F_0(Q,s)=-{3Q^2-2Qs+3s^2\over8},\qquad
p_0(Q,s)=-{3Q\over4}+{s\over4}.
$$

The phase $F=F_0+G$ is the real solution of

$$
\partial_tF=a(Q,\partial_QF),\qquad F(0)=F_0.
\tag{1.2}
$$

Here the characteristic field is $X_{-a}=(-a_p,a_Q)$, as required by the positive sign in $e^{itA_h/h}$. The raw analytic construction in `research_continuation_2026_10_20/exact_amplitude.md`, Section 2, has been read at the precise phase step. For completeness, the construction and constants needed here are as follows.

On $|\Im Q|,|\Im p|<0.01$, the finite Fourier coefficient bound gives

$$
\|a\|<4,\qquad \|X_{-a}\|_\infty<300,
\qquad \|DX_{-a}\|_{\infty\to\infty}<20000.
\tag{1.3}
$$

For example, each derivative introduces the corresponding integer Fourier label and a factor $2\pi$; summing with the factor $e^{2\pi\cdot0.01(|k|+|l|)}$ gives the displayed bounds. Set $T=10^{-12}$. Start a characteristic at $(Q_0,-3Q_0/4+s/4)$. For $|t|\le T$, its displacement is less than $300T$, and its derivative differs from the identity by at most $e^{20000T}-1<2.1\cdot10^{-8}$. Solving its final-coordinate equation for $Q_0$ is a contraction on $|Q_0-Q|\le4\cdot10^{-10}$ whenever $|\Im Q|,|\Im s|<0.004$. The corresponding characteristic action gives (1.2).

These estimates hold for complex time as well: Picard integrals are taken on the straight complex segment from zero to $t$, their absolute estimates use its length $|t|$, and the same invariant strip and contraction bounds apply. Picard iteration, the implicit contraction, and the characteristic action are jointly holomorphic in $(t,Q,s)$. Thus the time Cauchy bounds used below are justified on a complex disk, not inferred merely from smooth dependence on real time.

Write $S_\rho=\{(Q,s):|\Im Q|,|\Im s|<\rho\}$, allowing arbitrary real parts. Although $F_0$ is unbounded, its correction is bounded: integrate (1.2) at fixed endpoints and use (1.3) on the constructed characteristic graph. A convenient uniform bound is

$$
\|G(t)\|_{S_{.003}}\le10|t|,\qquad |t|\le T.
\tag{1.4}
$$

The reserved strip gap $.003-.002=.001$ consequently gives

$$
\|G_Q\|_{S_{.002}},\ \|G_s\|_{S_{.002}}
\le10^4|t|.
\tag{1.5}
$$

All constants are fixed independently of $N$. The phase is evaluated at $t_*$; the auxiliary time interval does not alter the matrix family.

## 2. Exact four-sheet Gauss normalization

For $m=0,1,2,3$, set

$$
F_m(t,Q,s)=F(t,Q,s+m),\qquad
B_m(t,Q,s)=2\sqrt{F_{Qs}(t,Q,s+m)}.
\tag{2.1}
$$

The positive root exists throughout the real small-time interval, because $F_{0,Qs}=1/4$ and the Cauchy bound on $G_{Qs}$ makes its change much smaller than $1/4$. At zero, $B_m=1$.

The **exact initial identity**, including every relative sheet phase, is

$$
M_N(x,y)={e^{3\pi iN/4}\over2\sqrt N}
\sum_{m=0}^3e^{2\pi iN F_0(x/N,y/N+m)}.
\tag{2.2}
$$

Here is a direct check for every odd $N$. Put $d=x-3y$ and $Q_{xy}=3x^2-2xy+3y^2$. After removing $e^{-2\pi iQ_{xy}/(8N)}$, the sum on the right of (2.2) is

$$
\sum_{m=0}^3 e^{2\pi i(dm/4-3Nm^2/8)}
=2e^{-3\pi iN/4}e^{2\pi i\,3Nd^2/8}.
\tag{2.3}
$$

For even $d$, the left side is $2e^{-3\pi iN/4}i^d$; for odd $d$, it is two. These are precisely the two cases of the right side, using that odd squares are one modulo eight. Also $Q_{xy}\equiv3d^2\pmod8$. If $8^{-1}=(1+kN)/8$ is the chosen integral representative, then $k\equiv-N\pmod8$, since $N^2\equiv1\pmod8$. Therefore (2.3) converts the real fraction in the quadratic exponential to the modular inverse in the original $M_N$. This proves (2.2) without imposing primality or any further subsequence.

The initial deck identities are

$$
\begin{aligned}
F_0(Q,s+m+4)&=F_0(Q,s+m)+Q-3(s+m)-6,\\
F_0(Q+1,s+m)&=F_0(Q,s+m-3)-2(s+m)+3.
\end{aligned}
\tag{2.4}
$$

They persist for $F$: the first changes $F_Q$ by the integer one, the second changes $Q$ by the integer one, and the symbol is periodic in both arguments. Uniqueness of (1.2) gives the identities. Mixed derivatives remove the added affine terms, so the amplitudes have the corresponding permutation identities. At $Q=x/N,s=y/N$, multiplying each affine increment by $N$ gives an integer. Consequently the four-sheet matrix below is exactly periodic on the finite grid; wrapped Weyl shifts create no missing boundary term.

## 3. Finite-shift comparison with the exact original matrix

At $t=t_*$, define

$$
V_N(x,y)={e^{3\pi iN/4}\over2\sqrt N}
\sum_{m=0}^3 B_m(t_*,x/N,y/N)
e^{2\pi iN F_m(t_*,x/N,y/N)}.
\tag{3.1}
$$

We prove the comparison needed for a diagonal sum, rather than invoking an operator-norm probability-kernel limit.

For one finite Fourier label, the exact ordinary Weyl action in real coordinates is

$$
W_h(k,l)\psi(Q)=e^{2\pi ik(Q+\pi hl)}\psi(Q+2\pi hl).
$$

Taylor expansion through first order after extracting $e^{iF/h}$, followed by summation over the finite support, gives

$$
A_h(Be^{iF/h})=e^{iF/h}\left[
a(Q,F_Q)B-ih\left(a_pB_Q+
\tfrac12(a_{Qp}+a_{pp}F_{QQ})B\right)+O(h^2)\right].
\tag{3.2}
$$

Every derivative is bounded on the fixed real endpoint region and its sheet translates, so this remainder is uniform. The finite Fourier set, and the grid periodicity just proved, make the same calculation valid at grid wraps. Direct differentiation of (1.2) gives

$$
\partial_tF_{Qs}=a_p\partial_QF_{Qs}
+(a_{Qp}+a_{pp}F_{QQ})F_{Qs}.
$$

Hence the positive amplitude in (2.1) solves

$$
B_t=a_pB_Q+\tfrac12(a_{Qp}+a_{pp}F_{QQ})B.
\tag{3.3}
$$

Equations (1.2) and (3.3) cancel the first two orders of the exact evolution $\partial_t=iA_h/h$. The remaining residual in each entry of the four-sheet matrix is $O(h/\sqrt N)$. Each residual column therefore has Euclidean norm $O(h)$, uniformly for $0\le t\le t_*$. The initial matrix is exactly $M_N$ by (2.2). Duhamel's formula and unitarity of $e^{itA_N/h}$ yield

$$
\|(U_N-V_N)e_y\|_2=O(N^{-1}),\qquad
\|U_N-V_N\|_{\rm HS}=O(N^{-1/2}).
\tag{3.4}
$$

Also $\sup_{x,y}|V_N(x,y)|\le C/\sqrt N$, since there are four bounded amplitudes. Thus $\|\operatorname{diag}V_N\|_2\le C$, and restriction of (3.4) to the diagonal gives

$$
\left|\sum_x|U_N(x,x)|^2-\sum_x|V_N(x,x)|^2\right|
\le\|\operatorname{diag}(U_N-V_N)\|_2
\bigl(2\|\operatorname{diag}V_N\|_2+
\|\operatorname{diag}(U_N-V_N)\|_2\bigr)=o(1).
\tag{3.5}
$$

This establishes the particular trace-like comparison needed below. It does not claim $\operatorname{Tr}(U_N-V_N)=o(1)$, which would not follow from (3.4).

## 4. Exact cancellation of the first three equal-sheet coefficients

The equal-sheet kernel is

$$
k_t(Q,s)={1\over4}\sum_{m=0}^3B_m(t,Q,s)^2
=\sum_{m=0}^3F_{Qs}(t,Q,s+m).
\tag{4.1}
$$

It is positive and real analytic. The deck identities permute its four terms under integer changes of either endpoint, so it is doubly periodic.

Use coordinates $p=(s-3Q)/4$, and write

$$
G(t,Q,s)=\mathcal G(t,Q,p),\qquad
D=\partial_Q-\tfrac34\partial_p.
$$

The Hamilton–Jacobi equation becomes

$$
\partial_t\mathcal G=a(Q,p+D\mathcal G),\qquad
\mathcal G(0)=0.
\tag{4.2}
$$

Expand the genuine holomorphic solution as $\mathcal G=\sum_{n\ge1}t^n\mathcal G_n$. We claim that $\mathcal G_n$ is a finite trigonometric polynomial in $p$ of degree at most $n$. The first coefficient is $a$, of degree one. For the induction, a contribution to the coefficient of $t^{n-1}$ on the right of (4.2) is

$$
{\partial_p^r a(Q,p)\over r!}
(D\mathcal G_{j_1})\cdots(D\mathcal G_{j_r}),
\qquad j_1+\cdots+j_r=n-1,
$$

or the constant-in-time term when $n=1$. Differentiation does not raise Fourier degree. The displayed product therefore has degree at most $1+\sum j_a=n$. There are finitely many terms, proving the induction.

For $n=1,2,3$,

$$
\sum_{m=0}^3\mathcal G_n(Q,p+m/4)
$$

retains only momentum frequencies divisible by four. At these orders the only such frequency is zero, so the sum is independent of $p$, and hence independent of $s$. Applying $\partial_Q\partial_s$ annihilates it. Since $\sum_mF_{0,Qs}=1$, this proves exact vanishing of the first three time coefficients of $k_t-1$.

We now bound the remainder, without truncating tau in the matrix definition. Time Cauchy estimates from (1.4) give

$$
\|G_n\|_{S_{.003}}\le10T^{1-n}.
$$

For $|t|\le T/2$,

$$
\left\|G(t)-\sum_{n=1}^3t^nG_n\right\|_{S_{.003}}
\le{20|t|^4\over T^3}=2\cdot10^{37}|t|^4.
\tag{4.3}
$$

A mixed spatial Cauchy estimate across the reserved gap .001 costs $10^6$, and summing the four real translates costs four. Thus

$$
\|k_t-1\|_\infty\le8\cdot10^{43}|t|^4,
\qquad |t|\le T/2.
\tag{4.4}
$$

Since $t_*<\tau$, the claimed $10^{44}\tau^4$ bound follows. This cancellation uses the actual momentum degree of the corrected original symbol; it is not a consequence of a generic Anosov mixing estimate.

## 5. All discrete aliases on the diagonal

Expanding $\sum_x|V_N(x,x)|^2$, the equal-sheet part is

$$
{1\over N}\sum_{x=0}^{N-1}k_{t_*}(x/N,x/N)
\longrightarrow\int_0^1 k_{t_*}(q,q)\,dq.
\tag{5.1}
$$

For each unequal pair $m,n$, the remaining normalized grid sum has smooth bounded amplitude $B_m(q,q)B_n(q,q)/4$, and phase

$$
F_m(t_*,q,q)-F_n(t_*,q,q)
=-{m-n\over2}q-{3(m^2-n^2)\over8}+d_{mn}(q),
\tag{5.2}
$$
$$
d_{mn}(q)=G(t_*,q,q+m)-G(t_*,q,q+n).
$$

The phase independent of $q$ has unit-modulus exponential and may be removed. By (1.5),

$$
\|d'_{mn}\|_\infty\le4\cdot10^4t_*<1/8.
\tag{5.3}
$$

If $m-n$ is odd, the derivative of the remaining phase stays at distance at least $3/8$ from every integer. Every Poisson alias is therefore nonstationary.

If $m-n$ is even and nonzero, it is $\pm2$. Its linear factor disappears **exactly on the sampled grid**, because $Nq=x$ is integral. In this case we prove that $d_{mn}$ is a nonconstant analytic function; this step cannot be replaced by ignoring the alias.

At $q=0$, the characteristic starts and ends on the equilibrium line $Q=0$. Indeed the first derivatives of $a$ vanish there for every $p$. Thus

$$
G(t,0,m)={9t\over10},\qquad d_{mn}(0)=0
\tag{5.4}
$$

exactly. At $q=1/4$, $R(1/4)=r(3/4)=1$, and the initial momenta are $m/4-1/8$. A time Cauchy estimate also gives

$$
\|G(t)-t a(Q,p_0(Q,s))\|_{S_{.003}}
\le{20t^2\over T}=2\cdot10^{13}t^2.
\tag{5.5}
$$

For the pairs $(m,m+2)$, $m=0,1$, their first-order difference at $q=1/4$ is

$$
{2t\over100}\cos(-\pi/4+m\pi/2-\alpha_0).
$$

Using $\cos\alpha_0=-3/5$, $\sin\alpha_0=4/5$, the two cosines are $-7/(5\sqrt2)$ and $1/(5\sqrt2)$. Its absolute coefficient is therefore at least $1/(250\sqrt2)>1/400$. The difference of the two errors in (5.5) is at most $4\cdot10^{13}t_*^2<t_*/800$. Consequently

$$
|d_{m,m+2}(1/4)|\ge t_*/800>0.
\tag{5.6}
$$

Together with (5.4), this proves nonconstancy. Reversing the ordered pair only changes the sign.

Here is the sampled oscillatory lemma, including all aliases. Let $A$ be smooth near $[0,1]$, and $d$ real analytic there, with $|d'|<1/8$ and $d$ nonconstant. Then

$$
{1\over N}\sum_{x=0}^{N-1}A(x/N)e^{2\pi iN d(x/N)}\longrightarrow0.
\tag{5.7}
$$

To prove it, first insert a smooth cutoff supported in $(0,1)$, equal to one except in endpoint intervals of total length $O(\delta)$. The discarded grid contribution is at most $C\delta+O(N^{-1})$. Poisson summation for the compactly supported smooth function gives exactly a sum over $j\in\mathbb Z$ of

$$
\int A_\delta(q)e^{2\pi iN(d(q)-jq)}\,dq.
$$

For every nonzero $j$, the derivative has modulus at least $|j|-1/8$. Repeated integration by parts gives a summable bound $C_{M,\delta}N^{-M}(1+|j|)^{-M}$, for any fixed $M\ge2$. For $j=0$, analyticity and nonconstancy imply that the zeros of $d'$ on the compact support form a finite set. Remove arbitrarily small neighborhoods of them; their integrals are bounded by their length times a fixed amplitude bound. Integration by parts on the complement then sends its integral to zero. This proves the zero-alias limit. Finally let $\delta\downarrow0$. The identical argument applies when every aliased derivative is separated from zero, as in the odd-difference case; no zero-alias critical-set step is then needed.

For (5.2), use the odd-difference argument or apply (5.7) after the exact integer-slope removal. There are twelve ordered unequal-sheet pairs, so their total tends to zero. Combining this with (5.1) and (3.5) proves Theorem A. The constants in this cancellation may deteriorate extremely badly as $t_*$ becomes small, but the parameter is fixed throughout; no uniform-in-time claim is made.

## 6. Exact comparison of the two averages

For every finite matrix $U$, the common rotation simply multiplies its trace by $e^{-2\pi i\alpha}$, proving the first equality of (0.3). On the other hand,

$$
|\operatorname{Tr}(D_\varphi U)|^2
=\sum_{x,y}e^{2\pi i(\varphi_x-\varphi_y)}U_{xx}\overline{U_{yy}}.
$$

Independent torus integration kills exactly the terms $x\ne y$, proving the second equality of (0.3). The same distinction holds if phases are written symmetrically as $D_{\varphi/2}UD_{\varphi/2}$, because that matrix is unitarily conjugate to $D_\varphi U$.

More generally, a common phase integrates the character $e^{2\pi i\alpha\sum_xv_x}$ to $\mathbf1_{\{\sum_xv_x=0\}}$; independent phases integrate $e^{2\pi i\sum_xv_x\varphi_x}$ to $\mathbf1_{\{v=0\}}$. Equal total traversal time does not imply equal coordinate-visit vector. This is the exact algebraic distinction in any closed-path expansion. Theorem A and Corollary B show that it makes a quantitatively nonvanishing difference for the given generator and metaplectic matrix at one iterate.

## 7. Use of the audited original one-step trace

The internal proved input is Theorem 5.1 and (6.1) of
`research_round13_2026_10_21/orbit_correlations/protected_actions_and_one_step_trace.md`.
Its Sections 1–6 were read directly in this branch. Their proof constructs the correct ordinary symbol, the protected equilibrium lines, all four one-step stationary sectors, the exact action factors, the stationary-phase amplitude, and the fixed-point derivative traces. It uses the full exact one-step amplitude and the modular sector identity already proved in the raw sources retained in the master. Those older raw sector and exact-amplitude proofs were not reaudited in full in this branch: this dependence is explicitly retained, rather than presenting the input as a newly proved external theorem.

For the reader, the precise formula being used is

$$
\operatorname{Tr}U_N=\zeta_N\left[
\mathsf A e^{i(9/10)\tau N}
+\mathsf B e^{-i\pi N/2}e^{-i(11/10)\tau N}\right]+O(N^{-1}),
\tag{7.1}
$$

where $|\zeta_N|=1$, $v=\pi\tau/125$, and

$$
\begin{aligned}
\mathsf A&=(4+39212v)^{-1/2}-(4+39188v)^{-1/2},\\
\mathsf B&=(4-48612v)^{-1/2}+(4-49788v)^{-1/2}.
\end{aligned}
$$

These coefficients come from the four exact linearized traces $6+39212v$, $6+39188v$, $6-48612v$, $6-49788v$, whose fixed-point action phases are the two terms of (7.1) with relative signs $(+,-,+,+)$. The mean-value theorem and convexity respectively give

$$
|\mathsf A|\le3v/2,\qquad \mathsf B\ge1+6150v.
$$

Thus, with $c=12297\pi/250$,

$$
\liminf|\operatorname{Tr}U_N|\ge1+c\tau.
\tag{7.2}
$$

Theorem A gives $\limsup\mathcal D_N\le1+10^{44}\tau^4$. Therefore

$$
\liminf(|\operatorname{Tr}U_N|^2-\mathcal D_N)
\ge2c\tau+c^2\tau^2-10^{44}\tau^4\ge200\tau.
$$

The last numerical inequality follows already from $\pi>3$ and $10^{44}\tau^3=10^{-196}$. This proves Corollary B from the explicitly recorded trace input.

## 8. Actual application attempt and the first remaining estimate

The primary-source quantum-graph step checked in this branch is the conversion of a long wavenumber average to independent bond phases. In Gnutzmann–Altland, *Spectral correlations of individual quantum graphs*, Phys. Rev. E **72**, 056215 (2005), Section II D, equation (20), the bond lengths are rationally independent. The map $k\mapsto(kL_b/2)_b$ is consequently equidistributed on the full bond-phase torus. Section III B, equations (38)–(47), then applies the color-flavor transformation separately to those phase integrals. This is an ensemble construction before the subsequent spectral analysis.

Primary published PDF:
https://www.physik.fu-berlin.de/en/einrichtungen/ag/ag-von-oppen/papers/pre_72_056215.pdf

The literal phase family produced by the question is a common phase: its phase vector is proportional to $(1,\ldots,1)$. Its integer annihilator contains every $e_x-e_y$, so the needed rational independence fails. No ergodic-equidistribution theorem converts this one-dimensional periodic subgroup to the full torus. The original-family calculation (0.2) rules out repairing that exact step by a pointwise $o(1)$ comparison of even the first unnormalized form factor.

One could still try a **weaker**, fully weighted comparison at microscopic scale. Granting for the moment an appropriate theorem for the coordinate-phase ensemble, the first original-family bridge would have to establish, for a fixed admissible test $b_*$ supported in Fourier space as in the master,

$$
{1\over N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\left[|\operatorname{Tr}U_N^m|^2
-\int_{\mathbb T^N}|\operatorname{Tr}(D_\varphi U_N)^m|^2d\varphi\right]
\stackrel{?}{\longrightarrow}0.
\tag{8.1}
$$

No estimate proving (8.1) is obtained here. The common-phase average preserves all pairs of closed paths with equal total length, whereas the independent-phase average additionally requires equality of the visit vector. The original deterministic generator supplies phases to the extra pairs, but (3.2)–(5.7) control only a fixed finite number of one-step sheets. They provide no bound on the full signed sum of these extra histories when $m$ is proportional to $N$.

Even proving (8.1), plus the required ensemble pair theorem, would only settle a pair test. All fixed higher orders and arbitrary fixed Fourier bands would still need the corresponding comparisons. Conversely, (0.2) is not a counterexample to (8.1), to `H_diag`, or to weak sine-process convergence: by (7.1), its individual $m=1$ contribution to (8.1) is $O(N^{-2})$.

The first unproved original criterion therefore remains exactly

$$
\boxed{{1\over N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)
\longrightarrow0.}
\tag{8.2}
$$

Theorem A is a new original-family calculation within this research record, and Corollary B is a concrete test of a literature-transfer step. No claim of literature priority or full spectral universality is made.

## 9. Provenance and read scope

Base master: `Spectral_research_master.md`, SHA-256
`ef38464d8e2b6ad3e917547e3437dcd53ed7c28dd39c4818faa29e5eb7cf6d43`.

| Raw internal input | SHA-256 | Actual read/use scope |
|---|---|---|
| `research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` | Sections 1–4 read; only the phase construction and strips in Sections 1–2 used for Theorem A, with the complex-time extension proved here |
| `research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md` | `46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527` | Sections 1–4 and 8, Appendices A/B, and related proof-scope portions read; one-step Gauss formula and residual argument reconstructed explicitly here; no use of the all-fixed-power operator-norm conclusion to take a trace |
| `research_round13_2026_10_21/orbit_correlations/protected_actions_and_one_step_trace.md` | `6bbde35d4fb3873976d6182b3fb6d9cc969349a3a6ce78e7b9dc48cf480c9fe6` | Sections 1–6 read directly; Theorem 5.1 and (6.1) used for Corollary B; Section 7 not needed |

The current Round 13 raw file differs from its originally reviewed hash only by the documented correction of a hidden carriage return in TeX; the present hash is the one actually read. Exact file hashes should be rechecked at freezing time.

The published 2005 PDF was read at the actual rational-independence definition, Section II D equation (20), and Section III B equations (38)–(47). The entire 14-page universality derivation was **not** independently audited in this branch; no all-order theorem from it is asserted for the original family. The 2004 precursor, *Universal spectral statistics in quantum graphs*, arXiv:nlin/0402029v2 (version 27 September 2004), was also checked at its phase-equivalence equation (2) and its graph-gap setup. Its version is kept distinct from the published Phys. Rev. Lett. **93**, 194101 (2004). A later HTML conversion date is not a publication date.

Several older route-audit files were read to avoid repetition: the Round 3 prequantum/Dolgopyat and dense-transition attempts, Round 5 cubic-character obstruction, Round 6 and 7 literature applicability notes, and Round 10 shrinking-noise note. None is a mathematical dependency of Theorem A. Their old conclusions are not claimed as new results here.
