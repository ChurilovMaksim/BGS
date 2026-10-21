> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_occupation_audit_twostep_physical.md`. Embedded SHA256: `39b42b5d3706d72de7dfcf7f626334413b156bad8343fba306d5cf929727f9df`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: physical two-step mixing for the exact original family

21 October 2026. Auditor: occupation/cross-phase branch, independent of the author of the source proof.

## 0. Frozen source and verdict

The audited source is:

- research_round6_2026_10_21/r6_original_twostep_physical_mixing.md
- SHA256: 7d502a881f133743cd3d28afd6ac373351fd4a12f23e8292c59895358f1e747b

The source hash was checked immediately before this audit was written. Its mathematical content was examined directly, rather than inferred from its author's summary.

**Verdict:** the claimed physical estimate
$$
 \bigl\||U_N^2|^2-J_N\bigr\|_{\rm op}
 \le 8\cdot10^6t+o(1),\qquad
 t=\frac{10^{-80}}{2\pi},
 \tag{A0}
$$
is justified by the source proof together with the explicitly proved sampled oscillatory matrix lemma in Section 1 of the round-5 source. The limit is along every odd $N$. All $3\mid N$ cases are retained. The additional estimate for the whole signed class of nonadjacent literal substitutions in Section 9 is also justified, using the established original one-step bounds and the exact contraction in the isolated-sector note.

There is no claim that the right side of (A0) tends to zero: $t$ is fixed. The proof gives a very small fixed upper bound for the limsup, which suffices for the subsequent $1/4$ bounds.

I found no mathematical defect requiring a change to the frozen source. Two implicit but elementary details are supplied explicitly below: the finite-symbol coefficient norm in Section 2 and the analytic continuation step from a nonzero coefficient on the 24-torus to nontriviality on the unit square.

This audit does **not** certify $H_{\rm diag}$, the full unequal-occupation sum, or the sine-process limit. The source itself states these boundaries correctly.

## 1. Dependencies examined

For the only substantial oscillatory analytic input, I read the raw proof of Section 1 of:

- research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md

This is the sampled matrix lemma with residue classes modulo four, nonzero mixed derivative, and rectangular-cycle gradient less than $1/8$. Its proof is audited below in Section 8.

For the exact $M_N^2$ initialization I also have an independent derivation in:

- research_round6_2026_10_21/r6_occupation_twostep_gauss.md
- SHA256: 18c580433804f46443d565aed27517bdd5e809017b115c8fb4bc081a215a53da

The source's image-kernel proof agrees with that derivation, with its scalar $\eta_N$ equal to the inverse of the scalar $\rho_N$ in that note. Neither proof relies on numerical verification.

The contraction and counting used in Section 9 were independently checked in:

- research_round6_2026_10_21/r6_occupation_audit_original_isolated.md
- SHA256: 9b0af6c7c2b04ce183ac7f107de50e928d79aa2bc542631db7278e7aa97d9616

The only change in its audited source between hashes 81e6edcb3a7bc50cd9b5ccb190a03510523428fb0ca12030cd7ad06d46ff1bf4 and 20585b313f25044ae8cab78bdd70edeb3922356788d912666d3f690e5676e68f was an appended numerical-verification paragraph. Truncating at the original final sentence reproduces the first hash exactly. Thus the mathematical contraction already audited is unchanged.

For the final corollary, the prior original-family bounds being used are
$$
 \|P_N-J_N\|_{\rm op}\le40000t+o(1),
 \qquad
 \max_{x,y}|U_N(x,y)|\le 3/\sqrt N
 \tag{A1}
$$
for all sufficiently large odd $N$. These are inputs to the corollary, not deductions from (A0). The new physical estimate (A0) does not itself require (A1).

## 2. Modular half, ordinary half, and exact Egorov

For odd $N$, choose the integer representative $2^{-1}=(N+1)/2$. For every raw integer pair $(k,l)$,
$$
 e_N(k\,2^{-1}l)=(-1)^{kl}e^{\pi ikl/N}.
$$
Consequently the definition
$$
 Q_N(H)=\sum_{k,l}\widehat H(k,l)(-1)^{kl}T_N(l,k)
$$
has precisely the finite-shift action in source (1.3). In particular the two factors $(-1)^{kl}$ cancel when this action is written with ordinary halves.

The original $p$-dependent Fourier coefficients have $l=\pm1$, so changing from modular-half to ordinary-half symbols multiplies their $k$-th coefficient by $(-1)^k$. This is exactly the replacement $r(q)\mapsto r(q+1/2)$. All $l=0$ terms remain as displayed in source (1.1).

The two Weyl generator covariances for $M_N$ follow directly from its quadratic kernel. The transformed raw symbol label is
$$
 (k',l')=(3k+2l,4k+3l).
$$
It satisfies $k'\equiv k\pmod2$ and $l'\equiv l\pmod2$, hence
$$
 (-1)^{k'l'}=(-1)^{kl}.
$$
This proves the ordinary-half Egorov statement without an additional phase:
$$
 M_NQ_N(a)M_N^*=Q_N\bigl(a(3q+4p,2q+3p)\bigr).
$$

It matters here that the proof uses raw integer labels before reducing modulo $N$. The equality therefore remains correct even when different raw Fourier modes alias for a small dimension. Distinctness of reduced labels is not assumed.

Finally,
$$
 (e^{itA_N/h}M_N)^2
 =e^{itA_N/h}e^{it(M_NA_NM_N^*)/h}M_N^2.
$$
Thus the initial $M_N^2$ is evolved first under $a^M$, then under $a$, in exactly the order used by the source. Since $t/h=\tau N$, this is the original fixed kick.

## 3. Finite-symbol bounds and the characteristic construction

Here is an elementary coefficient-norm check independent of any previous expansion. In Fourier $\ell^1$ norm,
$$
 \|\cos(14\pi q)\|_1=1,\quad
 \|r\|_1\le4,\quad
 \|\sin(2\pi q)\|_1=1,\quad
 \|\cos(2\pi p-\alpha_0)\|_1=1.
$$
The triangle and product inequalities give
$$
 \|\widehat a\|_1\le1+\frac4{10}+\frac4{100}
   +\frac1{10}+\frac4{100}=1.58<2.
$$
The largest total frequency is at most nine. The transformed total frequency is at most
$$
 |3k+2l|+|4k+3l|\le7|k|+5|l|\le63.
$$
The transformation has determinant one, so it is injective on the raw integer Fourier lattice and preserves the coefficient $\ell^1$ norm.

On the specified complex tube of width $0.002$, Fourier differentiation gives the gradient and Hamiltonian-vector-field derivative bounds stated in the source. In particular the two displayed majorants are less than $2000$ and $10^6$, respectively. The latter bounds the row sums of the derivative matrix, since for each Fourier mode the sum of the relevant second-derivative absolute coefficients is bounded by $(2\pi)^2(|k|+|l|)^2$.

The characteristic equations have the correct signs for the positive Schrödinger exponential:
$$
 \dot Q=-H_p,\qquad \dot P=H_q,\qquad
 \partial_\sigma\Phi=H(q,\Phi_q).
$$
They are piecewise autonomous; this does not affect the integral equation, the displacement estimates, or the derivative majorant.

The claimed uniform complex neighborhood can be made explicit. Start with, for example, $|\operatorname{Im}u|,|\operatorname{Im}r|<0.0005$. The initial momentum
$$
 p_m(u,r)=(-17u+r+m)/24
$$
then has imaginary part of magnitude less than $0.000375$. For $2t\le2\cdot10^{-12}$, the characteristic displacement is less than $4\cdot10^{-9}$, so it stays strictly inside the tube of width $0.002$. The contraction constant $2t\cdot10^6$ is less than one. All real $u,r$ and all integers $m$ are allowed because the symbol bounds are periodic and uniform in their real parts.

The initial tangent $(1,-17/24)$ has maximum norm one. Thus
$$
 |J_\sigma-1|\le2\cdot10^6\sigma<1/2.
$$
For real variables, $u\mapsto Q_\sigma(u)$ is strictly increasing and differs from the identity by a bounded amount, hence is onto and one-to-one. The same bounds give the stated local complex inverse by contraction on a slightly smaller tube. The resulting phase and amplitude are therefore real analytic on a connected neighborhood of the whole real plane. Their relevant fixed-order derivatives are uniformly bounded.

Varying the action in source (4.6) cancels the interior terms by the characteristic equations. The initial endpoint contribution $P_0\,du$ cancels the variation of the initial phase. This gives
$$
 \Phi_q=P_\sigma,\qquad
 \Phi_\sigma=H(q,\Phi_q),\qquad
 \Phi_r=(u-17(r+m))/24.
$$
The last formula is particularly important: it includes the $r$-dependence of the inverse initial point $u$, and leaves no unaccounted term from that dependence.

The Jacobian transport for $B=J^{-1/2}$ gives
$$
 B_\sigma=H_pB_q+
 \tfrac12(H_{pq}+H_{pp}\Phi_{qq})B
$$
with the same sign as the finite-shift expansion. Both $B$ and $\Phi$ are continuous at the join of the two intervals; thus there is no distributional source at that joining time.

## 4. Phase and amplitude estimates

From the endpoint formulas and displacement bounds,
$$
 |S_q|\le(1+17/24)2000\sigma\le4000\sigma,
 \qquad |S_r|\le2000\sigma/24\le100\sigma.
$$
At a fixed real endpoint, $|H|<2$, hence $|S|\le2\sigma$. The inverse Jacobian estimate gives
$$
 |B^2-1|\le
 \frac{2\cdot10^6\sigma}{1-2\cdot10^6\sigma}
 \le4\cdot10^6\sigma.
$$
At $\sigma=2t$, these are precisely the source constants $8000t$, $200t$, and $8\cdot10^6t$.

For the first-order phase expansion, the time integral has $a^M$ on the first interval and $a$ on the second. Comparing both with the same initial momentum $p_m(q,r)$ gives
$$
 \begin{split}
 |S_m(2t)-t(a^M(q,p_m)+a(q,p_m))|
 &\le2000\int_0^{2t}4000\sigma\,d\sigma\\
 &=16\cdot10^6t^2.
 \end{split}
$$
No time-order correction has been dropped: it is included in the bound on the evolved momentum. The statement is uniform over the whole real parameter plane.

## 5. Exact initial Gaussian kernel and deck identities

The independent finite Gaussian proof verifies, including all $3\mid N$,
$$
 K_N(x,y)=\frac1{\sqrt{24N}}\sum_{m=0}^{23}
 e^{-2\pi i[17x^2-2x(y+mN)+17(y+mN)^2]/(48N)}
$$
and $M_N^2=\eta_NK_N$ with $|\eta_N|=1$.

The source's proof does not divide by three, 24, or 48 modulo $N$. Its covariance identities follow from $17^2-24\cdot12=1$, and the ordinary halves in those identities are legitimate because $17\cdot12$ and $17\cdot24$ are even. Commutation with both the cyclic shift and distinct diagonal roots proves scalar proportionality. Squaring the finite image sum gives
$$
 |K_N(x,y)|^2=\frac gN{\bf1}_{g\mid x-17y},
 \qquad g=\gcd(N,24)\in\{1,3\},
$$
so every row has norm one and the proportionality scalar has unit modulus.

For the initial image phases, direct expansion gives exactly
$$
 \begin{split}
 \Theta_{m+24}(q,r)&=\Theta_m(q,r)+q-17(r+m)-204,\\
 \Theta_m(q+1,r)&=\Theta_{m-17}(q,r)-12(r+m)+102,\\
 \Theta_m(q,r+1)&=\Theta_{m+1}(q,r).
 \end{split}
$$
In particular the branch reindexing is $m-17$, and the constant is $+102$.

Both time-stage symbols are one-periodic in both arguments. Their characteristic equations therefore preserve the integer momentum shift and the coordinate translation occurring above. Uniqueness propagates all three phase identities, and propagates their amplitude versions with no additive terms.

On the sampled lattice $q=x/N,r=y/N$, the additional phases, after multiplication by $N$, are integers:
$$
 -12y-12Nm+102N,\qquad
 x-17y-17Nm-204N.
$$
Consequently the whole 24-term kernel is exactly periodic in both discrete coordinates at every time. This proves boundary compatibility for wrapped finite shifts. It would not have been sufficient merely to assert that each branch is periodic; individual branches generally are not.

Subtracting the initial identities also proves that the corrections and amplitudes are 24-periodic in each real coordinate, a fact used later in the Fourier-coefficient argument.

## 6. Residual size and passage to entrywise probabilities

For a mode $(k,l)$, the ordinary-half spatial shift is $2\pi hl$. Expanding the phase difference, amplitude, and midpoint multiplier to first order yields
$$
 Q_N(H)(Be^{i\Phi/h})=e^{i\Phi/h}
 \left[H(q,\Phi_q)B
 -ih\left(H_pB_q+\tfrac12(H_{pq}+H_{pp}\Phi_{qq})B\right)
 +O(h^2)\right].
$$
For example $H_p=\sum2\pi il\,\widehat H(k,l)e^{2\pi i(kq+lp)}$, so the amplitude-shift term $2\pi hlB_q$ is exactly $-ihH_pB_q$. The midpoint and phase-curvature terms likewise give the displayed $-ih/2$ terms. This checks all $2\pi$ factors and the transport sign.

The uniform $O(h^2)$ remainder follows from fixed finite support and bounded derivatives of the real phase of order at least two and of the amplitude. The initial phase is quadratic; its unbounded first derivative on the full plane causes no remainder problem. Its first derivative is retained exactly in the principal oscillation. Exact gluing allows branch lifts to be used even for shifts crossing a matrix boundary.

Multiplication by $i/h$, and cancellation with the phase and transport equations, leaves residual $O(h)$ per unnormalized branch. After the factor $N^{-1/2}$ and the finite branch sum, this is
$$
 |\operatorname{Residual}_{xy}|\le Ch/\sqrt N.
$$
Thus its column Euclidean norm is at most $Ch$. Duhamel over the two successive unitary evolutions gives
$$
 \|(U_N^2-V_N)e_y\|_2\le Cth=O(N^{-1}),\qquad
 \|U_N^2-V_N\|_{\rm HS}\le Cth\sqrt N=O(N^{-1/2}).
$$
These are ordinary, unnormalized Euclidean and Hilbert--Schmidt norms.

The amplitude bound gives $\max|V_N|<5/\sqrt N$. The per-column error then gives $\max|U_N^2|\le6/\sqrt N$ for sufficiently large odd $N$. Finally, entrywise,
$$
 \left|| (U_N^2)_{xy}|^2-|V_{xy}|^2\right|
 \le \bigl(|(U_N^2)_{xy}|+|V_{xy}|\bigr)
       |(U_N^2-V_N)_{xy}|.
$$
Thus
$$
 \bigl\||U_N^2|^2-|V_N|^2\bigr\|_{\rm HS}
 \le \frac{11}{\sqrt N}\|U_N^2-V_N\|_{\rm HS}
 =O(N^{-1}).
$$
This is the required dimension-correct passage to probabilities. No equality between coherent and Markov powers is used.

## 7. The marked frequency and nonseparability

The corrected $p$-term has
$$
 r(q+1/2)=(1+\cos14\pi q)(1-\cos2\pi q),
 \qquad \widehat a(7,1)=e^{-i\alpha_0}/400.
$$
Indeed the first factor contributes $1/2$ at frequency seven, no other product term changes that coefficient, and the positive $p$-cosine coefficient is $e^{-i\alpha_0}/2$.

After substituting the initial momentum,
$$
 b_m(q,r)=a(q,(-17q+r+m)/24)
 +a((q+r+m)/6,(-q+r+m)/8).
$$
In the first term a raw mode $(k,l)$ has frequency
$(k-17l/24,l/24)$. The frequency
$$
 \nu=(151/24,1/24)
$$
therefore uniquely requires $(k,l)=(7,1)$. In the second term the frequency is
$$
 ((4k-3l)/24,(4k+3l)/24).
$$
Matching $\nu$ would require $k=19,l=-25$, excluded by $|l|\le1$. Thus there is no competing contribution and
$$
 \widehat b_m(\nu)=\frac{e^{-i\alpha_0}}{400}e^{2\pi im/24}.
$$

For two distinct image indices, the root separation is at least
$2\sin(\pi/24)\ge1/6$. With normalized Fourier coefficients on the 24-torus, a uniform error bound also bounds every coefficient. Hence
$$
 \left|\widehat{S_m-S_n}(\nu)\right|
 \ge t/2400-32\cdot10^6t^2\ge t/4800>0
$$
throughout the stated $t\le10^{-12}$ interval. In particular the inequality is valid for the exact prescribed $t$.

The initial phase difference is separable, so its mixed derivative vanishes. Integrating the 24-periodic correction twice by parts multiplies this nonzero coefficient by
$$
 -(2\pi)^2(151/24)(1/24)\ne0.
$$
This proves that the mixed derivative of the evolved phase difference is not identically zero on the real plane.

To make the restriction to the sampled unit square explicit: the derivative is real analytic on a connected neighborhood of the real plane. If it vanished identically on an open neighborhood of the unit square, or on its interior, analytic continuation would force it to vanish everywhere, contradicting the coefficient calculation. Thus the precise nontriviality hypothesis of the sampled matrix lemma holds on the needed connected neighborhood of $[0,1]^2$.

The rectangular cycle removes the entire separable initial part. Its $q$-derivatives are bounded by $4\cdot8000t=32000t$; the $r$-derivatives have the smaller bound $800t$. Therefore all four derivatives are less than $1/48$, and in particular less than $1/8$. The potentially large initial linear carrier is absent from this rectangular phase; it cannot create an overlooked Poisson alias.

## 8. Raw verification of the sampled matrix lemma and its use

The lemma's cutoff error has squared Hilbert--Schmidt norm at most
$4\epsilon\|b\|_\infty^2+o(1)$, which gives the stated $2\|b\|_\infty\sqrt\epsilon$ bound.

The fourth Schatten power is exactly the four-variable sampled sum of the rectangular phase. Poisson summation on step-four progressions gives the prefactor $4^{-4}$ and aliases
$$
 \mathcal R(z)-k\cdot z/4.
$$
For $k\ne0$, choose a coordinate of maximum $|k_j|$. The hypothesis gives
$$
 |\partial_j(\mathcal R-k\cdot z/4)|
 \ge |k_j|/4-1/8\ge |k_j|/8.
$$
Six integrations by parts give
$C_\epsilon N^{-6}(1+|k|_\infty)^{-6}$. The derivatives of the phase of order at least two are independent of $k$, so the inverse derivative factors have the necessary powers of $|k_j|^{-1}$. The bound is summable over four-dimensional integer shells. This removes every nonzero alias.

The zero-alias rectangular phase is nonconstant because its mixed $q,r$ derivative contains the nonidentically zero mixed derivative of the original phase. The proof in the source establishes the needed analytic zero-set fact by slicing and induction. A nonzero partial derivative has a zero set of measure zero, so the full critical set has measure zero. Cutting out a small critical neighborhood and integrating once by parts proves the zero-alias integral tends to zero. The critical cutoff is fixed before $N$ tends to infinity and is only then removed. The boundary cutoff is removed last. Thus no unproved stationary-phase estimate, nondegeneracy rate, or uniformity in $t$ is hidden here.

For each ordered pair of distinct sheets, the source has the matrix
$$
 (24N)^{-1}B_m(q,r)B_n(q,r)e^{2\pi iN\phi_{mn}(q,r)}.
$$
Its amplitude is smooth and independent of $N$; the global scalar $\eta_N$ cancels. All phase hypotheses have been checked in Section 7 of this audit. Splitting into 16 residue blocks modulo four is valid even though the number of sheets is 24. The step-four lemma is applied to the sampled entries; the number of sheets does not prescribe the residue spacing.

There are only $24\cdot23=552$ ordered distinct pairs. Summing their vanishing operator norms and the 16 fixed blocks per pair gives $o(1)$ along all odd $N$. No uniform statement over growing families of phases is needed.

The self-sheet matrix has entries
$$
 (24N)^{-1}\sum_m B_m^2,
$$
whose difference from $1/N$ has magnitude at most $8\cdot10^6t/N$. Both its row and column absolute sums are at most $8\cdot10^6t$, hence the Schur bound gives the same operator norm. Combining this with the cross-sheet cancellation and the $O(N^{-1})$ physical probability error proves (A0).

## 9. The defect matrix and all-time isolated class

Unitarity makes both $P_N=|U_N|^2$ and $R_N=|U_N^2|^2$ doubly stochastic. Therefore
$$
 P_N^2=J_N+E_N^2,\quad E_N=P_N-J_N,\qquad
 D_N=R_N-P_N^2=(R_N-J_N)-E_N^2.
$$
This gives
$$
 \|D_N\|_{\rm op}\le8\cdot10^6t+(40000t)^2+o(1).
$$
Together with (A1), both $\|D_N\|$ and $\|E_N\|$ are at most $1/4$ for every sufficiently large odd $N$. Also $D_NJ_N=J_ND_N=0$ exactly.

For a fixed nonempty literal mismatch set with cyclic gaps at least two, summing all labels first gives the exact trace
$$
 \operatorname{Tr}\bigl(DP^{g_1-2}\cdots DP^{g_r-2}\bigr).
$$
Zero-length common arcs are the identity. Positive-length arcs may be replaced by corresponding powers of $E$, since every $J$ is annihilated by an adjacent $D$. This is valid also for singleton mismatch sets and for periodic words; no cyclic-orbit division is introduced.

For a doubly stochastic nonnegative $R$ with entries at most $C/N$,
$$
 \|R-J\|_{\rm HS}^2=\sum R_{ab}^2-1\le C-1.
$$
Using $P_{ab}\le9/N$, $R_{ab}\le36/N$, and the operator norm of $E$,
$$
 \|E\|_{\rm HS}\le\sqrt8,\quad
 \|D\|_{\rm HS}\le\sqrt{35}+\tfrac14\sqrt8<7.
$$
A pattern with $r$ defects has $n-r$ individual $D$ or $E$ factors. For $n\ge3$, there are at least two. Hilbert--Schmidt Cauchy--Schwarz at two factors, and the operator bound $1/4$ on all others, gives
$$
 |\hbox{fully contracted pattern sum}|
 \le49(1/4)^{n-r-2}=784(1/4)^{n-r}.
$$
Thus there is no leftover dimension factor.

The exact rooted mismatch-set count is
$$
 c_{n,r}=\frac nr\binom{n-r-1}{r-1},\qquad n\ge2r.
$$
Its weighted transfer expression is
$$
 Z_n(q,d)=\operatorname{Tr}
 \begin{pmatrix}q&d\\1&0\end{pmatrix}^{n}-q^n.
$$
At $q=d=1/4$, the positive eigenvalue is $(1+\sqrt{17})/8<2/3$, and $Z_n\le2\lambda_+^n$. The generating sum is exactly $7/6$. Since $Z_1=0,Z_2=1/2$, the sum for $n\ge3$ is $2/3$.

At $n=2$, the two singleton mismatch sets give $F_2^{(2)}=2\operatorname{Tr}D$. The terms in
$\operatorname{Tr}D=\operatorname{Tr}R-\operatorname{Tr}P^2$ are nonnegative and bounded by 36 and 9. Their difference therefore has magnitude at most 36, giving $|F_2^{(2)}|\le72$. This uses the maximum of the two nonnegative bounds, not their sum.

It follows that
$$
 \sum_{n\ge1}|F_n^{(2)}|
 \le72+784\cdot\frac23=\frac{1784}{3}<600.
$$
For bounded weights $|w_{n,N}|\le W$, absolute convergence now justifies
$$
 N^{-2}\left|\sum_{n\ge1}w_{n,N}F_n^{(2)}\right|
 <600W/N^2.
$$
All moduli here are taken after the exact label contraction for each fixed mismatch pattern.

## 10. Scope and unresolved estimate

The new result controls an actual coherent two-step operator for the prescribed deterministic family, and its whole signed isolated-substitution class. It is not obtained by random phase substitution, by a limit $\tau_N\to0$, or by deleting $3\mid N$.

The class in Section 9 contains both equal and unequal occupations. Its signed estimate cannot be transferred to its unequal-occupation subset by monotonicity. It also cannot be combined with overlapping signed class bounds using a union bound. Adjacent mismatch runs and the full required weighted trace combinations remain uncontrolled. Higher factorial orders required by $H_{\rm diag}$ remain separate.

Accordingly, this audit accepts the stated new physical theorem and the stated signed-class corollary, and accepts the author's explicit boundary that these do not settle the original spectral-statistics problem.

