> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_occupation_audit_fixed_powers_49.md`. Embedded SHA256: `0953ee6eb3c665fe667fabcb094651eb7284f6250ebfa2c6d535bd98f7da9b61`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: exact sheet characters and the first 49 physical powers

21 October 2026. Auditor: occupation/cross-phase branch.

## 0. Frozen sources and verdict

The source audited in full is:

- research_round6_2026_10_21/r6_original_fixed_powers_49.md
- SHA256: 3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019

The source was independently read from its raw definitions through its final scope statement. Its hash was checked against the author's frozen hash.

Its analytic and finite-shift predecessor is:

- r6_original_twostep_physical_mixing.md
- SHA256: 7d502a881f133743cd3d28afd6ac373351fd4a12f23e8292c59895358f1e747b

That predecessor was independently audited in:

- r6_occupation_audit_twostep_physical.md
- SHA256: 39b42b5d3706d72de7dfcf7f626334413b156bad8343fba306d5cf929727f9df

**Verdict:** the fixed-power theorem and its exact sheet-character identity are sound as stated. Every changing hypothesis of the predecessor is checked below, including the general odd common-divisor case in the initial Gauss kernel. The exact arithmetic certification of the range through 49 is correct. No change to the frozen proof is needed.

In particular, for each fixed $R$ satisfying
$$
 51200t\Sigma_R^2\le1,\qquad t=10^{-80}/(2\pi),
$$
the source proves
$$
 \bigl\||U_N^R|^2-J_N\bigr\|_{\rm op}
 \le256t\Lambda_R+o_R(1)
 \tag{A0}
$$
along every odd $N$, with the original fixed kick. The finite simultaneous consequence for $1\le R\le49$ follows. Neither the source nor this audit asserts a result for arbitrarily growing powers.

## 1. Recurrences, parity, and the sum of stage scales

Let
$$
 \mathsf S=\begin{pmatrix}3&4\\2&3\end{pmatrix},
 \qquad
 \mathsf S^j=\begin{pmatrix}a_j&b_j\\c_j&a_j\end{pmatrix}.
$$
Matrix multiplication gives the three stated recurrences. Induction gives
$$
 b_j=2c_j,\quad a_j^2-b_jc_j=1,\quad
 a_j\ {\rm odd},\quad b_j,c_j\ {\rm even}.
$$
The base $j=1$ has $a_1=3,b_1=4,c_1=2$. For $j\ge1$, positivity is preserved, and
$$
 b_{j+1}-a_{j+1}=a_j+b_j>0.
$$
Hence $0<a_j/b_j<1$.

There is a direct telescoping verification of the source's closed sum:
$$
 a_{j+1}-a_j=2(a_j+b_j).
$$
Therefore
$$
 \Sigma_R=9\sum_{j=0}^{R-1}(a_j+b_j)
 =\frac92(a_R-1).
$$
All stage scales $L_j=9(a_j+b_j)$ are positive; in particular
$$
 L_{\max}\le\Sigma_R,\qquad
 \Lambda_R=\sum_{j<R}L_j^2\le\Sigma_R^2,
 \qquad \Sigma_R\ge9.
$$
No floating-point property of the eigenvalues of $\mathsf S$ is needed.

## 2. Exact symbol majorant and ordinary-half covariance

The real cosine part of the corrected symbol has the exact expansion
$$
 \frac9{10}\cos7u+\frac1{10}\cos u
 -\frac1{20}\cos6u-\frac1{20}\cos8u,
 \qquad u=2\pi q.
$$
Its Fourier coefficient one-norm is $11/10$.

Expanding products gives
$$
 r(q)\sin u=
 \sin u+\frac12\sin2u+\frac14\sin5u+\frac12\sin6u
 -\frac12\sin8u-\frac14\sin9u.
$$
Thus its one-norm after division by 100 is $3/100$.

For the $p$-dependent term, $\|r\|_1=4$. Since
$e^{i\alpha_0}=(-3+4i)/5$, the total absolute real-plus-imaginary coefficient weight of its $p$-cosine is $7/5$. The corresponding contribution is at most
$$
 4(7/5)/100=7/125.
$$
Using the real-plus-imaginary norm as an upper bound for each complex modulus and adding gives
$$
 \|\widehat a\|_1\le11/10+3/100+7/125=593/500.
$$
Possible overlap of the cosine and sine coefficients only decreases this bound. The support assertions $|k|+|l|\le9$, $|l|\le1$ follow from these same expansions.

The original ordinary-half covariance was checked in the predecessor audit. Its iterate has label map
$$
 (k,l)\longmapsto (a_jk+c_jl,b_jk+a_jl).
$$
This is an invertible integer map, and it preserves both parities because
$\mathsf S^j\equiv I\pmod2$. Consequently it preserves the ordinary-half sign and introduces no additional factor in the formula for $Q_N(H_j)$. Raw integer labels are used throughout, before reduction modulo $N$.

For every original mode,
$$
 |a_jk+c_jl|+|b_jk+a_jl|
 \le(a_j+b_j)|k|+(a_j+c_j)|l|
 \le(a_j+b_j)(|k|+|l|)\le L_j.
$$
The coefficient norm remains the same under the invertible label map.

On the complex tube $\delta=(100L_{\max})^{-1}$, the Fourier exponential multiplier is at most
$$
 e^{2\pi\delta L_j}\le e^{\pi/50}
 <e^{1/15}\le15/14.
$$
The last step follows by termwise comparison of the exponential and geometric series. The strict comparison $\pi/50<1/15$ follows, for example, from $\pi<22/7$.

The two resulting rational bounds are exactly
$$
 \frac{593}{500}\frac{44}{7}\frac{15}{14}
 =\frac{19569}{2450}<8,
$$
$$
 \frac{593}{500}\left(\frac{44}{7}\right)^2\frac{15}{14}
 =\frac{430518}{8575}<64.
$$
Thus the gradient and integrated derivative scales used in the flow construction are valid, with the stated constants. The Hessian bound is the row-sum bound for the derivative of the Hamiltonian vector field, not just a bound on one second derivative.

## 3. Evolution order

The exact factorization
$$
 U_N^R=
 e^{itQ_N(H_0)/h}\cdots
 e^{itQ_N(H_{R-1})/h}M_N^R
$$
follows by repeatedly moving $M_N$ through the next kick using conjugation. Operators act on the initial kernel from the rightmost factor first. Therefore the characteristic stages occur in the order
$$
 H_{R-1},H_{R-2},\ldots,H_0,
$$
each for time $t$, as stated.

The scalar $t/h$ equals $\tau N$. The exact original family is unchanged. $R$ is fixed before $N$ tends to infinity.

## 4. The general all-odd image Gauss formula

Set $a=a_R,b=b_R,c=c_R$, with $R\ge1$, so $b>0$. Define
$$
 K_{R,N}(x,y)=\frac1{\sqrt{bN}}\sum_{m=0}^{b-1}
 e^{-2\pi iQ(x,y+mN)/(2bN)},
 \qquad Q(x,Y)=ax^2-2xY+aY^2.
$$

The polynomial identities used for two steps hold for these general parameters solely because $a^2-bc=1$:
$$
 Q(x+a,Y)-Q(x,Y-1)=bc(2x+a),
$$
$$
 Q(x+b,Y)-Q(x,Y)=2b\{a(x+b/2)-Y\},
$$
$$
 Q(x+N,Y+aN)-Q(x,Y)=bc(2YN+aN^2).
$$
They prove the required two generator covariances and the $x$-periodicity by image reindexing. The $y$-periodicity follows by $m\mapsto m+1$. The image summand is $b$-periodic in $m$ since $ab$ is even. The ordinary halves in the covariance phases agree with modular halves since $ac$ and $ab$ are even.

Both $K_{R,N}$ and $M_N^R$ have exactly the same two Weyl generator covariances. Their quotient commutes with the diagonal matrix of distinct $N$-th roots and with the cyclic shift, so it is scalar. This argument does not require any inverse of $b$ modulo $N$.

Here is the norm calculation for arbitrary odd $g=\gcd(N,b)$, not just $g=1,3$. Factor out the image-independent unit phase. The remaining sum is
$$
 G=\sum_{m=0}^{b-1}
 e^{-\pi iaNm^2/b+2\pi i(x-ay)m/b}.
$$
In $|G|^2$, put $d=m-n$ modulo $b$. The sum over $n$ vanishes unless $b\mid aNd$. Since $a^2-bc=1$, $\gcd(a,b)=1$; thus the surviving shifts are exactly $d=(b/g)r$, $0\le r<g$.

Their residual quadratic phase is
$$
 e^{-\pi i(aN/g)(b/g)r^2}=1.
$$
Indeed $N$ is odd, hence $g$ is odd, and $b/g$ is even. The residual linear sum is $g$ when $g\mid x-ay$, and zero otherwise. Consequently
$$
 |K_{R,N}(x,y)|^2=\frac gN{\bf1}_{g\mid x-ay}.
$$
Since $\gcd(a,g)=1$ and $g\mid N$, exactly $N/g$ columns in each row satisfy this congruence. Every row therefore has norm one, so the proportionality scalar has modulus one.

This proves the image formula for every odd $N$, including all common prime factors of $N$ and the possibly very large $b_R$. The number $b_R$ is fixed in each theorem. Its size does not change the argument.

## 5. Integrated characteristic budgets and analytic inverses

The total displacement and derivative majorants are
$$
 \mathcal G=8t\Sigma_R,\qquad
 \mathcal L=64t\Lambda_R.
$$
The assumed criterion implies
$$
 \mathcal L\le64/51200=1/800,
$$
and
$$
 \frac{\mathcal G}{\delta}
 =800tL_{\max}\Sigma_R
 \le800t\Sigma_R^2\le1/64.
$$
Both statements use integrated stage bounds. Replacing them by the full duration times the largest stage bound would be a different and weaker estimate; the source does not make that replacement.

The uniform complex domain can be chosen explicitly. For example, start with
$|\operatorname{Im}u|,|\operatorname{Im}s|<\delta/8$. Since $a/b<1$ and $b\ge4$,
$$
 |\operatorname{Im}p_m(u,s)|
 \le (a/b)\delta/8+\delta/(8b)<5\delta/32.
$$
The displacement is at most $\mathcal G\le\delta/64$, so the trajectory remains well inside the tube of width $\delta$ on every stage. The integrated Lipschitz constant is at most $\mathcal L<1$, so the integral equation is a contraction on a uniform displacement ball. Piecewise constant time dependence causes no difficulty.

The variational equation gives
$$
 \|D(Q,P)-I\|\le e^{\mathcal L}-1\le2\mathcal L.
$$
The initial tangent $(1,-a/b)$ has maximum norm one. Therefore
$$
 |\partial_uQ-1|\le2\mathcal L<1/2.
$$
For real parameters the endpoint map is increasing and differs from the identity by a bounded amount, so it is a global bijection. On a smaller complex tube the inverse is given by the same contraction estimate. This yields analytic phases and amplitudes, with every required fixed derivative bounded independently of $N$.

The action-variation formulas from the two-step proof hold stage by stage and join continuously:
$$
 \Phi_q=P,\qquad
 \Phi_s=(u-a(s+m))/b.
$$
Thus
$$
 |S_q|\le(1+a/b)\mathcal G\le2\mathcal G,
 \qquad |S_s|\le\mathcal G/b.
$$
The amplitude satisfies
$$
 |B_m^2-1|
 \le\frac{2\mathcal L}{1-2\mathcal L}\le4\mathcal L
 =256t\Lambda_R.
$$

For the first-order phase comparison, let $G(v)=8L_j$ on the active stage. At each intermediate time the same endpoint comparison gives momentum correction at most $2\int_0^vG(w)\,dw$. Hence
$$
 |S_m-t\beta_m|
 \le2\int_0^{Rt}G(v)\int_0^vG(w)\,dw\,dv
 =\left(\int_0^{Rt}G(v)\,dv\right)^2
 =64t^2\Sigma_R^2.
$$
The equality is the elementary identity $2\int A'(v)A(v)\,dv=A(Rt)^2$. It remains valid for the piecewise constant $G$, and includes all stage-order effects in the momentum correction.

## 6. Exact nonlinear sheet character and frequency noncollision

The general image-phase deck identities are
$$
 \begin{split}
 \Theta_{m+b}(q,s)&=\Theta_m(q,s)+q-a(s+m)-ab/2,\\
 \Theta_m(q+1,s)&=\Theta_{m-a}(q,s)-c(s+m)+ac/2,\\
 \Theta_m(q,s+1)&=\Theta_{m+1}(q,s).
 \end{split}
$$
They follow from $a^2-bc=1$ and direct expansion. Periodicity of every stage symbol in both phase-space coordinates propagates them by characteristic uniqueness. In particular corrections and amplitudes are $b$-periodic in both endpoint coordinates.

There is also the stronger literal identity
$$
 \Theta_m(q,s)=\Theta_0(q,s+m).
$$
The initial graphs are identical under the same substitution, and no evolution symbol depends on the endpoint parameter $s$. Therefore uniqueness gives
$$
 \Phi_m(q,s)=\Phi_0(q,s+m),\qquad
 S_m(q,s)=S_0(q,s+m).
$$
This identity includes the entire nonlinear evolution. It is not a first-order approximation in $t$.

For a raw transformed Fourier label $(K,L)$, substitution of the initial graph gives endpoint frequency
$$
 (K-aL/b,L/b).
$$
This map is invertible. Thus producing
$$
 \nu_R=(7-a/b,1/b)
$$
is equivalent to producing raw transformed label $(K,L)=(7,1)$.

The stage-$j$ label transformation is
$$
 \begin{pmatrix}K\\L\end{pmatrix}
 =
 \begin{pmatrix}a_j&c_j\\b_j&a_j\end{pmatrix}
 \begin{pmatrix}k\\l\end{pmatrix}.
$$
Its inverse gives the unique candidate
$$
 (k,l)=(7a_j-c_j,a_j-7b_j).
$$
For $j=0$, this is $(7,1)$. For every $j\ge1$, $a_j<b_j$ and $b_j\ge4$, so
$$
 l=a_j-7b_j<-6b_j\le-24.
$$
The original support has $|l|\le1$, making a collision impossible. This checks both the transpose convention of the label map and its inverse; they must not be replaced by the phase-space map without transposition.

Consequently the first-order coefficient of $\beta_0$ at $\nu_R$ is exactly $e^{-i\alpha_0}/400$. With normalized Fourier coefficients on the $b$-torus, the uniform first-order error gives
$$
 \left|C_R(t)-te^{-i\alpha_0}/400\right|
 \le64t^2\Sigma_R^2\le t/800.
$$
Therefore $|C_R(t)|\ge t/800>0$.

Translation in the second coordinate now gives exactly
$$
 \widehat{S_m-S_n}(\nu_R)
 =C_R(t)(e^{2\pi im/b}-e^{2\pi in/b}).
$$
For distinct sheet labels modulo $b$, the two roots are different. No lower bound on their separation is required: the error has already been included in the common nonzero coefficient $C_R(t)$. This is the reason the sufficient criterion contains no extra factor $b$, even though the number of sheets grows quickly with $R$.

Both components of $\nu_R$ are nonzero, since $7-a/b>6$ and $1/b>0$. The initial sheet-phase difference is separable. Fourier differentiation therefore proves the mixed derivative of each distinct evolved sheet difference is not identically zero.

As in the predecessor audit, the phases are real analytic on a connected neighborhood of the full real endpoint plane. Nontriviality on the $b$-torus consequently implies nontriviality on the unit-square neighborhood by analytic continuation.

## 7. Rectangular phases, aliases, residuals, and probabilities

The rectangular-cycle phase cancels the entire separable initial phase difference. From the endpoint derivative bounds, each $q$-component of its gradient is at most $8\mathcal G=64t\Sigma_R$. The second-coordinate components are smaller. Under the criterion,
$$
 64t\Sigma_R\le1/(800\Sigma_R)\le1/7200<1/8.
$$
Thus the exact nonaliasing hypothesis of the previously proved step-four sampled matrix lemma is satisfied for each pair of distinct sheets.

On the physical lattice, the deck additions multiplied by $N$ are
$$
 -cy-cNm+acN/2,\qquad
 x-ay-aNm-abN/2.
$$
They are integers since $ac$ and $ab$ are even. The whole image sum is therefore exactly periodic. The general source writes “periodic columns”; the required fact is periodicity of the full sampled kernel in its row variable at every stage, which these identities explicitly prove. The corresponding endpoint shift also proves periodicity in the other coordinate.

The finite-shift residual proof imported from the predecessor requires only real finite Fourier symbols, uniform fixed-order derivatives, and the exact branch gluing. All three have been established here. For each fixed $R$, the number of stages and branches is finite and independent of $N$. Thus its constants may depend on $R$, while its residual has entry size $O_R(h/\sqrt N)$. Column Duhamel and unitarity then give
$$
 \|(U_N^R-V_{R,N})e_y\|_2=O_R(h),\qquad
 \|U_N^R-V_{R,N}\|_{\rm HS}=O_R(h\sqrt N).
$$

The amplitude bound is at most $1/200$, so
$$
 |V_{R,N}(x,y)|\le\sqrt{b_R(1+1/200)}/\sqrt N.
$$
The per-column error is $O_R(N^{-1})$, which proves
$$
 |U_N^R(x,y)|\le2\sqrt{b_R}/\sqrt N
$$
for every sufficiently large odd $N$. Combining this entry bound with the Hilbert--Schmidt error gives the probability-matrix error $O_R(N^{-1})$, exactly as in the predecessor audit.

The self-sheet terms differ from $J_N$ entrywise by at most
$256t\Lambda_R/N$. Both their row and column absolute sums are therefore at most $256t\Lambda_R$. The Schur estimate gives the required operator bound.

Each distinct-sheet term has a smooth amplitude and a fixed analytic phase satisfying the mixed-derivative and alias conditions just checked. The sampled matrix lemma applies after a finite split into 16 residue blocks modulo four. There are $b_R(b_R-1)$ sheet pairs. This number may be very large but is fixed before the $N$-limit, so summing the finitely many $o_R(1)$ terms is legitimate.

Together these estimates prove (A0). No rate uniform in $R$, in sheet separation, or in $t$ is required or asserted.

## 8. Exact arithmetic at 49 and 50

Independent recurrence evaluation reproduces
$$
 a_{49}=16255007246704249599863612909970798723,
$$
$$
 \Sigma_{49}=73147532610169123199386258094868594249
 <74\cdot10^{36}.
$$
Since $2\pi>6$,
$$
 51200t\Sigma_{49}^2
 <\frac{51200\cdot74^2}{6\cdot10^8}
 =\frac{280371200}{600000000}<\frac12<1.
$$
The sequence $\Sigma_R$ is positive and increasing, so every $R\le49$ satisfies the criterion.

Likewise,
$$
 \Sigma_{50}=426335063173366200380428859644050080712
 >426\cdot10^{36}.
$$
Since $2\pi<7$,
$$
 51200t\Sigma_{50}^2
 >\frac{51200\cdot426^2}{7\cdot10^8}
 =\frac{9291571200}{700000000}>1.
$$
Monotonicity proves failure of this sufficient criterion for every $R\ge50$. This is not evidence that the physical statement itself fails there.

The coefficient of the limiting bound obeys
$$
 256t\Lambda_R\le256t\Sigma_R^2\le1/200.
$$
For each of the 49 fixed values of $R$, the error $o_R(1)$ is eventually at most $1/200$. Taking the maximum of these finitely many thresholds gives the single all-odd threshold in source (1.9). No uniformity over an unbounded set of powers is used.

For $R=3$, direct integer arithmetic gives
$$
 (a_3,b_3)=(99,140),\quad
 (L_0,L_1,L_2)=(9,63,369),
$$
$$
 \Sigma_3=441,\quad
 \Lambda_3=9^2+63^2+369^2=140211,\quad
 256\Lambda_3=35894016.
$$
The displayed third-power example is therefore correct.

## 9. Executed exact-arithmetic audit

After reading the verification source and its elementary rational polynomial implementation, I independently executed:

- r6_original_fixed_powers_49_checks.py
- SHA256: 7bc426cd2a9c63f38758761accb5271b7def5ceb914167782b0dddf02c0be7f7

Its imported elementary algebra implementation is:

- r6_original_twostep_exact_checks.py
- SHA256: 9274ae69e39e18af6bca91990298eb58a9dc67b3d0cf5e6183acfbb4eecb57d4

The executed run exited successfully. Its report states 2700 exact rational polynomial identities checked, verifies the recurrence and closed sum, confirms all parity and determinant conditions in the finite range, verifies the candidate inverse labels and endpoint transformations, and certifies the rational inequalities at 49 and 50.

The relevant arithmetic uses Python integers and fractions, together with sparse polynomials over the rationals. There is no floating-point comparison with $10^{-80}$. This computation supplements the general algebraic and analytic proofs above; it is not a replacement for the all-odd Gauss argument or the $N$-asymptotic proof.

## 10. Scope

The source establishes a genuine extension from the first and second physical powers to an explicit finite set of 49 powers of the prescribed deterministic family. Its exact sheet-character identity is a structural statement about the nonlinear actions, and the proof correctly explains why branch-root spacing does not enter the perturbative coefficient error.

The number 49 is an explicitly certified limit of the stated sufficient estimate. It is not an Ehrenfest-time result with $R$ increasing with $N$, and it is not a bound for every positive power. The symbol and branch counts are fixed in each use of the sampled matrix lemma.

The full long-time trace sums at $n\asymp N$, the unrestricted adjacent mismatch runs, and the higher factorial orders required by $H_{\rm diag}$ remain unresolved. The fixed-power theorem cannot by itself be promoted to the sine-process limit. The source preserves these distinctions.

