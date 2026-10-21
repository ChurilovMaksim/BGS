> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/subprincipal_stability_theorem.md`. Embedded SHA256: `63597dea1e627925280e79644ccc54ed68b9327c9ab757f6eea9ad69962e2381`.
> [Thematic guide](../../topics/closure.md).

# Microscopic stability under smooth subprincipal changes

Date: 2026-10-21.

## Outcome and scope

**Structural theorem proved.** For the specified odd-dimensional family, let $V_N:[0,1]\to U(N)$ be a $C^1$ unitary path with $V_N(0)=U_N$ and
$$
-iV_N'(t)V_N(t)^*
=N^{-1}Q_N(a_t)+R_N(t),\qquad
\sup_t\|R_N(t)\|_{\rm op}=O(N^{-2}),
\tag{S1}
$$
where the real symbols $a_t$ range in a fixed compact subset of $C^\infty(\mathbb T^2)$. Then there are absolutely continuous eigenangle continuations such that
$$
\max_jN|\theta_{j,N}(1)-\theta_{j,N}(0)|\le C,
\tag{S2}
$$
$$
\sum_{j=1}^N
|\theta_{j,N}(1)-\theta_{j,N}(0)-\phi_N|\longrightarrow0,\qquad
\phi_N=\frac1{2\pi N}\int_0^1\!\int_{\mathbb T^2}a_t(x)\,dx\,dt.
\tag{S3}
$$
Angles are in turns, so an eigenvalue is $e^{2\pi i\theta}$. Differences use real continuous lifts. Both bounds hold uniformly with any intermediate $t$ replacing the final endpoint.

The random-origin local point-process laws at the endpoints approach one another in a metric for weak convergence. If either endpoint satisfies the project's full, all-order $H_{\rm diag}$, then so does the other. The proof includes the necessary higher-moment argument.

The concrete path
$$
V_N(t)=e^{itQ_N(v)/N}U_N
\tag{S4}
$$
is admissible for every fixed real smooth $v$, including every fixed real trigonometric polynomial, with $R_N=0$.

**This is an equivalence theorem, not a proof of $H_{\rm diag}$.** It does not produce an endpoint where $H_{\rm diag}$ is known. Nor does it by itself remove the first quantum cocycle phase: Section 8 identifies the additional construction required.

## 1. Actual quantization and precise hypotheses

The initial family is unchanged:
$$
U_N=e^{i\tau NA_N}M_N,\qquad \tau=10^{-80},\quad N\ {\rm odd}.
$$
Its physical principal map is
$$
\Psi=\phi_{a^{(0)}}^{-t_*}\circ L,\qquad
t_*=\tau/(2\pi),\qquad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
$$
where $a^{(0)}$ denotes the corrected real symbol in odd-trace (5.2), distinguished from the path symbols $a_t$.

Use the ordinary Weyl quantization on the prescribed comb quotient:
$$
Q_N(b)=\sum_{(k,l)\in\mathbb Z^2}\widehat b(k,l)W_N(k,l),
\qquad W_N(k,l)=(-1)^{kl}T_N(l,k).
\tag{1.1}
$$
Smoothness gives absolute operator-norm convergence and
$$
\|Q_N(b)\|\le\sum_{k,l}|\widehat b(k,l)|.
\tag{1.2}
$$
Real $b$ gives a self-adjoint matrix.

If $\operatorname{Op}_N(b)$ instead denotes the original modular convention $\sum\widehat b(k,l)T_N(l,k)$, then $\operatorname{Op}_N(b)=Q_N(Jb)$, with $\widehat{Jb}(k,l)=(-1)^{kl}\widehat b(k,l)$. The fixed involution $J$ preserves real smooth compact families and their phase-space means. Thus (S2)–(S3), including the scalar $\phi_N$, are unchanged under that notation. In the Egorov calculation the classical observable must be $Jb$.

It suffices that $a_t$ is measurable in $t$ with range in a fixed compact smooth-symbol family; a continuous family certainly qualifies. The remainder in (S1) has one bound uniform in $N,t$.

The generator bound immediately gives
$$
\sup_t\|V_N(t)-U_N\|
\le\int_0^1\|V_N'(s)\|\,ds=O(N^{-1}).
\tag{1.3}
$$
Therefore a separate assumption of uniform principal map is redundant once fixed-time Egorov is established for $U_N$.

## 2. Fixed-time Egorov and normalized traces for this exact family

### 2.1. Finite Weyl calculation

For frequency indices $\kappa=(k,l)$, $\eta=(k',l')$, direct multiplication gives
$$
W_N(\kappa)W_N(\eta)
=e^{\pi i\omega(\kappa,\eta)/N}W_N(\kappa+\eta),
\qquad \omega(\kappa,\eta)=lk'-kl'.
\tag{2.1}
$$
This holds before reducing integer frequencies modulo $N$, retaining the aliasing signs, for all odd composite dimensions as well as primes.

Set $h=(2\pi N)^{-1}$ and $\{a,b\}=a_qb_p-a_pb_q$. For Fourier modes, $\{e_\kappa,e_\eta\}=4\pi^2\omega(\kappa,\eta)e_{\kappa+\eta}$. Using $|\sin x-x|\le |x|^3/6$ gives
$$
\left\|\frac{[Q_N(a),Q_N(b)]}{ih}-Q_N(\{a,b\})\right\|
\le Ch^2\sum_{\kappa,\eta}
|\widehat a(\kappa)\widehat b(\eta)|\,|\omega(\kappa,\eta)|^3.
\tag{2.2}
$$
The right side is finite for smooth symbols and uniform over compact smooth families.

Normalized Weyl orthogonality also gives
$$
\frac1N\operatorname{Tr}Q_N(b)\to\int b,\qquad
\frac1N\operatorname{Tr}\bigl(Q_N(b)^*Q_N(c)\bigr)\to\int\overline b\,c.
\tag{2.3}
$$
Indeed, only indices equal modulo $N$ contribute to the product trace. Equal integer indices give the Parseval sum; in every additional pair at least one frequency has size at least $N/2$. Rapid Fourier decay bounds all such alias terms by $o(1)$, uniformly on compact smooth families.

### 2.2. The actual Schrödinger kick

Let $E_N(s)=e^{isA_N/h}$, where $A_N=Q_N(a^{(0)})$. Its Heisenberg derivative is
$$
\frac d{ds}\bigl(E_N(s)^*Q_N(b)E_N(s)\bigr)
=E_N(s)^*\frac{[A_N,Q_N(b)]}{ih}E_N(s).
$$
The classical vector field acting on $b$ here is $(-a^{(0)}_p,a^{(0)}_q)$, since its derivative is $\{a^{(0)},b\}$. Duhamel's formula applied to (2.2) along the fixed classical flow proves
$$
E_N(t_*)^*Q_N(b)E_N(t_*)
=Q_N(b\circ\phi_{a^{(0)}}^{-t_*})+O_b(N^{-2}).
\tag{2.4}
$$
The metaplectic scalar cancels in conjugation, and exact Weyl covariance gives
$$
M_N^*Q_N(b)M_N=Q_N(b\circ L).
\tag{2.5}
$$
Since $t_*/h=\tau N$,
$$
U_N^{-1}Q_N(b)U_N
=Q_N(b\circ\Psi)+O_b(N^{-2}).
\tag{2.6}
$$
For every fixed integer $k$, iteration gives the corresponding fixed-time Egorov statement, uniformly over compact smooth symbol families.

By (1.3), $\|V_N(t)^k-U_N^k\|\le |k|O(N^{-1})$. Consequently
$$
\sup_t\|V_N(t)^{-k}Q_N(b)V_N(t)^k-Q_N(b\circ\Psi^k)\|\to0
\tag{2.7}
$$
for each fixed $k$, uniformly over the same symbol families. This proves the uniform correspondence principle for the entire path without assuming quantum ergodicity.

### 2.3. Classical ergodicity

The original $\Psi$ is smooth, area preserving, and Anosov. The explicit bounds in the classical source place its derivative within $10^{-70}$ of $L$ in stable/unstable coordinates; the invariant cones expand by at least $5$. Area preservation follows from the Hamiltonian flow and $\det L=1$.

The external classical input is precisely Xia, Theorem 4.2: a $C^{1+\alpha}$ volume-preserving Anosov diffeomorphism on a compact connected manifold is ergodic. Its hypotheses apply to this smooth torus map and normalized area. The theorem and its proof were opened and checked; Section 9 gives the source.

Only this ergodicity and fixed-time Egorov are used below. The all-time orbit trace formula is not an input to this theorem.

## 3. Uniform quantum ergodicity from time averages

Write
$$
\bar a_t=\int a_t,\quad b_t=a_t-\bar a_t,\quad
b_{t,T}=\frac1T\sum_{k=0}^{T-1}b_t\circ\Psi^k.
$$
For any orthonormal eigenbasis $\{\psi_{j,N,t}\}$ of $V_N(t)$, set
$$
q_N(t;\psi)=\frac1N\sum_j
|\langle\psi_{j,N,t},Q_N(b_t)\psi_{j,N,t}\rangle|^2.
\tag{3.1}
$$
Define the quantum time average
$$
B_{N,t,T}=\frac1T\sum_{k=0}^{T-1}
V_N(t)^{-k}Q_N(b_t)V_N(t)^k.
$$
Its diagonal expectations are unchanged in eigenvectors. For every matrix $B$ and orthonormal basis,
$$
\sum_j|\langle\psi_j,B\psi_j\rangle|^2
\le\sum_j\|B\psi_j\|^2=\operatorname{Tr}(B^*B).
$$
Thus
$$
q_N(t;\psi)\le N^{-1}\operatorname{Tr}(B_{N,t,T}^*B_{N,t,T}).
\tag{3.2}
$$
For fixed $T$, (2.7) gives $B_{N,t,T}=Q_N(b_{t,T})+o_T(1)$ in operator norm uniformly in $t$. The normalized Hilbert–Schmidt trace (2.3) therefore yields
$$
\limsup_{N\to\infty}\sup_t\sup_{\psi\ {\rm eigenbasis}}q_N(t;\psi)
\le\sup_t\|b_{t,T}\|_2^2.
\tag{3.3}
$$

The right side tends to zero uniformly in $t$. The operators
$C_T=T^{-1}\sum_{k=0}^{T-1}(\cdot)\circ\Psi^k$ are contractions on mean-zero $L^2$, and the mean ergodic theorem gives $C_Tb\to0$ for each such $b$. The set $\{b_t\}$ is compact in $L^2$. A finite $\epsilon$-net and the contraction bound make this convergence uniform on that compact set.

Taking $N\to\infty$ first at fixed $T$, and then $T\to\infty$, proves
$$
\boxed{
q_N:=\sup_t\sup_{\psi\ {\rm eigenbasis}}
\frac1N\sum_j
|\langle\psi_j,Q_N(a_t)\psi_j\rangle-\bar a_t|^2\to0.}
\tag{3.4}
$$
This is the required uniform quantum ergodicity. The bound is basis independent, including within degenerate eigenspaces.

## 4. Eigenangle branches and degeneracies

Let $H_N(t)=-iV_N'(t)V_N(t)^*$. Differentiating $V_NV_N^*=I$ proves self-adjointness, and
$$
\sup_t\|H_N(t)\|\le C_0/N.
\tag{4.1}
$$

Absolutely continuous real eigenangle branches exist. Locally in the parameter choose a cut outside the finite spectrum, take a smooth Hermitian logarithm of $V_N(t)$, and use its ordered Lipschitz eigenvalues. Local branches glue on overlaps by permutations and integer lifts. A finite cover of $[0,1]$ suffices for each fixed $N$. Globally differentiable eigenvectors are unnecessary.

At almost every parameter the branches are differentiable. At a repeated eigenvalue their first-order slopes are the eigenvalues of $P H_N(t)P/(2\pi)$, where $P$ projects onto the eigenspace. Choose an orthonormal basis diagonalizing that compression. Across all eigenspaces this is still an eigenbasis of $V_N(t)$, and
$$
\theta_{j,N}'(t)=\frac1{2\pi}
\langle\psi_{j,N,t},H_N(t)\psi_{j,N,t}\rangle.
\tag{4.2}
$$
For a simple eigenvalue this is obtained directly by differentiating
$V_N\psi=e^{2\pi i\theta}\psi$; restriction to a repeated eigenspace gives the compression formula. No gap estimate is used.

From (4.1), $|\theta_j'|\le C_0/(2\pi N)$, proving (S2). Put
$\phi_N(t)=(2\pi N)^{-1}\int_0^t\bar a_s\,ds$. Equations (S1), (3.4), and (4.2) imply
$$
\begin{aligned}
\sum_j|\theta_j(t)-\theta_j(0)-\phi_N(t)|
&\le\frac1{2\pi N}\int_0^t
\sum_j|\langle\psi_{j,N,s},Q_N(a_s)\psi_{j,N,s}\rangle-\bar a_s|\,ds\\
&\quad+\frac{N}{2\pi}\int_0^t\|R_N(s)\|\,ds\\
&\le\frac{\sqrt{q_N}}{2\pi}+O(N^{-1})\longrightarrow0,
\end{aligned}
\tag{4.3}
$$
uniformly in $t$.

This handles the requested $O_{\rm op}(N^{-2})$ error. More generally the same conclusion follows when $N\int_0^1\|R_N(t)\|dt\to0$, provided the generator retains its uniform $O(N^{-1})$ norm bound.

For the normalization check $a_t\equiv c$, $R_N=0$, the exact path is $e^{ict/N}U_N$, and every angle shifts by $ct/(2\pi N)=\phi_N(t)$.

The conclusion is vanishing *average* centered microscopic displacement:
$$
N^{-1}\sum_j|N(\theta_j(1)-\theta_j(0)-\phi_N)|\to0.
$$
A density-zero exceptional set may have bounded nonzero microscopic shifts. No quantum unique ergodicity or maximum-shift $o(1)$ claim is made.

## 5. Exact random-origin coupling and weak local-law stability

Set
$$
\varepsilon_{j,N}=\theta_{j,N}(1)-\theta_{j,N}(0)-\phi_N,\qquad
\eta_N=\sum_j|\varepsilon_{j,N}|\to0.
$$
There is a fixed $C$ such that $N|\varepsilon_{j,N}|\le C$.
With a common uniform $\alpha\in[0,1)$, couple
$$
\Xi_N^0=\sum_{j,\ell\in\mathbb Z}
\delta_{N(\theta_j(0)-\alpha+\ell)},\qquad
\Xi_N^1=\sum_{j,\ell\in\mathbb Z}
\delta_{N(\theta_j(0)+\varepsilon_j-\alpha+\ell)}.
\tag{5.1}
$$
The second law equals the final spectrum's random-origin law, since the scalar rotation is absorbed in $\alpha$.

For $f\in W^{1,1}(\mathbb R)$, the exact change of variables over $\alpha,\ell$ gives
$$
\begin{aligned}
&\mathbb E_\alpha\sum_{j,\ell}
|f(N(\theta_j(0)+\varepsilon_j-\alpha+\ell))
-f(N(\theta_j(0)-\alpha+\ell))|\\
&\qquad=\frac1N\sum_j
\|f(\cdot+N\varepsilon_j)-f\|_1
\le \|f'\|_1\eta_N.
\end{aligned}
\tag{5.2}
$$
The same holds for bounded-variation $f$, using total variation. In particular it controls changes in counts on each fixed interval.

For nonnegative $F\in C_c^\infty$,
$$
\left|\mathbb E e^{-\langle F,\Xi_N^1\rangle}
-\mathbb E e^{-\langle F,\Xi_N^0\rangle}\right|
\le\|F'\|_1\eta_N\to0.
\tag{5.3}
$$
To state a distance, choose a countable smooth compactly supported family $f_r$ generating the vague topology and use
$$
d(\xi,\zeta)=\sum_{r\ge1}2^{-r}
\min(1,|\langle f_r,\xi-\zeta\rangle|).
$$
The coupling gives
$$
\mathbb E\,d(\Xi_N^0,\Xi_N^1)
\le\sum_{r\ge1}2^{-r}\min(1,\|f_r'\|_1\eta_N)\to0.
\tag{5.4}
$$
Thus the bounded-Lipschitz distance between laws tends to zero. Both endpoint laws have exact intensity one. The argument is uniform for intermediate endpoints and does not assume either endpoint has a particular limiting law.

## 6. Full $H_{\rm diag}$ equivalence, including moments

For an admissible nonnegative Schwartz test $b$ with compact Fourier support and $\sup b<1$, let
$$
b_N(s)=\sum_{\ell\in\mathbb Z}b(N(s+\ell)),\qquad
M^X_{k,N}(b)=\mathbb E_\alpha
e_k\bigl(b_N(\theta_1-\alpha),\ldots,b_N(\theta_N-\alpha)\bigr).
\tag{6.1}
$$
This is the project's distinct-label factorial moment, with the factor $1/k!$.
Its $H_{\rm diag}$ requires convergence of these moments to the corresponding finite CUE moments for every fixed order and admissible test.

### 6.1. Source $H_{\rm diag}$ supplies local-count moments

For a fixed compact interval $I$, choose admissible $b_I\ge c_I>0$ on $I$. Such a test exists: the squared modulus of the inverse Fourier transform of a smooth compactly supported function with nonzero integral is positive near zero; broad dilation and small positive rescaling suffice.

For large $N$, the periodized weights $w_j=(b_I)_N(\theta_j-\alpha)$ lie in $[0,1]$. If $Z=\sum_jw_j$, expansion by repeated indices gives
$$
Z^p\le\sum_{r=1}^p r!\,
\left\{\begin{matrix}p\\r\end{matrix}\right\}e_r(w_1,\ldots,w_N).
\tag{6.2}
$$
Repeated powers of one weight are bounded by that weight; the braces are Stirling numbers of the second kind.

The finite CUE bound is
$$
0\le M^{\rm CUE}_{r,N}(b_I)\le(\int b_I)^r/r!.
$$
Source $H_{\rm diag}$ through order $p$ therefore bounds $\mathbb EZ^p$. Since $\Xi_N^0(I)\le c_I^{-1}Z$,
$$
\sup_N\mathbb E[\Xi_N^0(I)^p]<\infty.
\tag{6.3}
$$
Random-origin laws are translation invariant on the real line, so the bound is uniform over translates of a fixed interval.

### 6.2. Bounded microscopic displacement transfers moments

Every target point is within $C$ of its source point. Hence
$$
\Xi_N^1(I)\le\Xi_N^0(I+[-C,C])
\tag{6.4}
$$
pointwise in the coupling. All target local-count moments are bounded too.

For a fixed Schwartz $b$, set $c_n=\sup_{[n,n+1]}|b|$. This sequence is summable, and
$$
\langle|b|,\Xi_N^i\rangle
\le\sum_{n\in\mathbb Z}c_n\Xi_N^i([n,n+1]).
$$
Minkowski's inequality and local-count moment bounds give
$$
\sup_N\mathbb E[
\langle|b|,\Xi_N^0+\Xi_N^1\rangle^p]<\infty
\tag{6.5}
$$
for each fixed $p$. This handles the full Schwartz tails without assuming a bandlimited majorant.

### 6.3. Transfer of the factorial moments

Let $w_j^i=b_N(\theta_j^i-\alpha)$,
$D_N=\sum_j|w_j^1-w_j^0|$, and $S_N=\sum_j(w_j^0+w_j^1)$.
Equation (5.2) implies $\mathbb ED_N\le\|b'\|_1\eta_N\to0$.
Telescoping each product over a subset of labels gives
$$
|e_k(w^1)-e_k(w^0)|
\le D_NS_N^{k-1}/(k-1)!.
\tag{6.6}
$$
Indeed, each remaining mixed product is bounded by the product of the corresponding $w_j^0+w_j^1$, and their sum is at most $S_N^{k-1}/(k-1)!$.

For $R>0$, use $D_N\le S_N$ and (6.5) at order $k+1$:
$$
|M^1_{k,N}(b)-M^0_{k,N}(b)|
\le\frac1{(k-1)!}
\left(R^{k-1}\|b'\|_1\eta_N+\frac{C_{k+1,b}}R\right).
\tag{6.7}
$$
Taking first $N\to\infty$, then $R\to\infty$, proves moment difference $o(1)$. Optimization also gives $O_{k,b}(\eta_N^{1/k})$ with the stated moment constants.

Subtracting the same finite CUE moment proves target $H_{\rm diag}$ from source $H_{\rm diag}$. Reversing the matching proves the converse, using the other endpoint's $H_{\rm diag}$ as its source of moment bounds:
$$
\boxed{H_{\rm diag}(U_N)\Longleftrightarrow H_{\rm diag}(V_N(1)).}
\tag{6.8}
$$
Neither side is proved absolutely by this equivalence.

### 6.4. Why weak-law stability alone is insufficient

A purely spectral example shows that the moment step cannot be omitted. Put $K_N\sim\sqrt N$, with $K_N$ even, coincident angles at zero, and place the remaining $N-K_N$ angles on a uniform grid. Move half of the coincident angles by $a/N$, where $a\ne0$ is fixed. Then
$$
\max_jN|\varepsilon_j|\le|a|,\qquad
\sum_j|\varepsilon_j|=|a|K_N/(2N)\to0.
$$
Weak local laws approach each other, but the pure-cluster contribution to the second factorial-moment difference tends to
$$
\frac14\left(\int b(x)b(x+a)\,dx-\int b(x)^2\,dx\right)\ne0
\tag{6.9}
$$
for a nonzero Schwartz $b$. The grid–cluster cross change is $o(1)$, because the grid has uniformly bounded weighted local counts. The source cluster's third local-count moment diverges, so the higher-moment hypothesis fails. This example concerns the matching-to-moments implication only; it is not asserted to arise from an admissible perturbation of this Anosov quantization.

## 7. Concrete admissible path and remainder size

For fixed real smooth $v$, the path $V_N(t)=e^{itQ_N(v)/N}U_N$ is exactly unitary and
$$
-iV_N'(t)V_N(t)^*=Q_N(v)/N.
$$
It has $\phi_N=(2\pi N)^{-1}\int v$, and mean-zero $v$ requires no scalar rotation.

Noncommuting time-dependent smooth generators are also covered by the finite-dimensional unitary equation
$V_N'=i(N^{-1}Q_N(a_t)+R_N(t))V_N$.
The remainder's entire contribution to the summed angle error is bounded by
$$
\frac{N}{2\pi}\int_0^1\|R_N(t)\|dt=O(N^{-1}).
$$
No trace-norm remainder bound, eigenvalue-gap bound, or quantum unique ergodicity is required.

## 8. First quantum cocycle phase: transformation law and remaining construction

The previously audited scalar has
$$
\gamma_h(x)=\gamma_0(x)
(1+ih\sigma(x)+O(h^2)),\qquad
\sigma(x)=\frac{\gamma_1(x)}{i\gamma_0(x)}\in\mathbb R.
\tag{8.1}
$$
The established graph construction gives a bounded continuous $\sigma$, with a uniform $h$-expansion in the space of continuous sections. It does not establish smooth dependence of $\sigma$ on $x$.

For a fixed real trigonometric polynomial $v$, the actual plane modification is
$e^{i2\pi h\operatorname{Op}_h^W(v)}V_h$. Finite Weyl shifts applied to the exact old kernel give, in a smaller analytic strip,
$$
B_h^v(Q,q)=B_h(Q,q)
+i2\pi h\,v(Q,F_Q(Q,q))B_0(Q,q)+O(h^2).
\tag{8.2}
$$
The principal phase $F$ and amplitude $B_0$ are unchanged. For an edge $x\mapsto\Psi x$, the order-$s^2$ transverse-kernel change is
$$
K_2^v(x)-K_2(x)=i2\pi v(\Psi x)K_0(x).
\tag{8.3}
$$
A scalar multiple of $K_0(x)$ cancels in the normalized graph quotient. At this order it changes the scalar coefficient without changing the graph coefficient. Therefore
$$
\boxed{\sigma_v(x)=\sigma(x)+2\pi v(\Psi x).}
\tag{8.4}
$$
This is a finite-shift calculation for an actual polynomial-symbol modification, not an assumed endpoint with edited orbit weights.

A sufficient construction to cancel first phases on every periodic orbit up to a scalar rotation would provide an admissible real $v$, scalar $c$, and transfer function $f$ with
$$
\sigma(x)+2\pi v(\Psi x)=c+f(\Psi x)-f(x).
\tag{8.5}
$$
The coboundary telescopes over a period, and $c$ supplies a scalar per iterate. Pointwise cancellation would choose
$$
v(y)=-\sigma(\Psi^{-1}y)/(2\pi),
\tag{8.6}
$$
but existing regularity does not justify this as a smooth-symbol choice.

There are two separate construction issues:

1. Spectral stability applies once a fixed smooth generator exists. It does not show that the continuous graph potential has a smooth representative, even modulo a coboundary.
2. To retain the old exact analytic all-time contour formula at the new endpoint, the new symbol must have appropriate analytic-strip control, or the trace construction needs an additional proof. Arbitrary $C^\infty$ smoothness does not supply that strip.

Deleting the first imaginary coefficient of the one-step amplitude alone would not delete $\sigma$: cubic and quartic phase jets and the normalized graph also contribute to the scalar coefficient.

**Therefore this theorem does not yet permit deleting the first quantum cocycle phase from the original orbit sum.** The missing step is a smooth, preferably analytic, representative satisfying (8.5) and its unitary realization. Approximation to $\sigma$ at fixed accuracy does not identify an exact endpoint with the entire first phase removed.

## 9. Primary-source precedent and external input

### Direct precedent

Lev Kaplan, [Quantization Ambiguity, Ergodicity, and Semiclassics](https://arxiv.org/pdf/quant-ph/9906065), arXiv:quant-ph/9906065v1, 17 June 1999; journal reference New Journal of Physics 4 (2002), 90. Pages 2–3, equations (2)–(9), discuss the same QE-to-common-displacement mechanism and explicitly allow density-zero exceptional states and arbitrary bases at degeneracies. This is direct precedent. Its perturbative discussion is not substituted for the uniform-path, branch, or all-order moment arguments above. No historical priority is claimed.

### Quantum maps framework

Roman Schubert, [On the rate of quantum ergodicity for quantised maps](https://people.maths.bris.ac.uk/~marcvs/publications/rate_maps_revised_final.pdf), revised 31 May 2008; Annales Henri Poincaré 9 (2008), 1455–1477, [DOI](https://doi.org/10.1007/s00023-008-0395-3). The opened author version gives the trace-product estimate in Lemma 1, equation (21), Egorov in (25), and averaged QE for any eigenbasis in Theorem 1, equation (28). They are precise precedents for the framework; Section 3 proves the needed uniform-in-path statement directly.

Jens Marklof and Stephen O'Keefe, [Weyl's law and quantum ergodicity for maps with divided phase space](https://arxiv.org/pdf/nlin/0404038), arXiv:nlin/0404038v2, provides a more general unitary-map framework and its QE theorem in Section 8. It was inspected for context, not used as an additional premise.

### Classical theorem used

Zhihong Xia, [Hyperbolic invariant sets with positive measures](https://arxiv.org/pdf/math/0503437), arXiv:math/0503437v2, 26 August 2005; Discrete and Continuous Dynamical Systems 15 (2006), 811–818. Theorem 4.2, pages 7–8 of the opened version, proves ergodicity for $C^{1+\alpha}$ volume-preserving Anosov diffeomorphisms. Its compact connected manifold and smooth-volume hypotheses match this torus map.

All literature lookups used primary papers or author institutional versions. Retrieved web refs for the parent task: Kaplan turn227view0 / turn228view1 / turn228view2; Schubert turn223view1 / turn223view2 / turn229view0; Xia turn228view3 / turn229view3. The parent should open sources itself before citing those refs in its final answer.

## 10. Exact project provenance

This is a new structural theorem separate from the completed trace-foundation audit. No historical file was changed, and no further subagent was spawned.

| Source | SHA-256 |
|---|---|
| Spectral_partial_results_2026-10-20.md | b8c5e2071d49394270006853ee8316f3900e84f1a7ae9b03e58e5c4eaf29a7cc |
| research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md | 42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b |
| research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md | 355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c |
| research_continuation_2026_10_20/finite_identities_and_closure.md | e1d85ef8ecff65a1fecffe200185d9e721dce14f9c356705cc04f5c97ffd6d35 |
| research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md | c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1 |

The Weyl identities, normalized traces, fixed-time Egorov argument, uniform time-average estimate, eigenangle derivative argument, exact-origin coupling, and moment transfer were derived in this task. The external classical ergodicity theorem is explicitly identified. The first-cocycle-phase realization remains unproved.
