> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_complex_interpolation_test.md`. Embedded SHA256: `724273439eb34d7536ac592e67de56d260a7dc46b20c40031eae77e088236216`.
> [Thematic guide](../../topics/closure.md).

# Exact complex interpolation of the character-pinned propagator

Research continuation, 21 October 2026.

**Status.** This note proves a larger complex contraction domain for the exact interpolation $X_N(z)=K_N+zR_N$ of the original matrices. It also proves that this norm domain is optimal given unitarity, the exact conditional expectation, and the available all-block escape estimate. The Hilbert--Schmidt and differentiated trace identities are evaluated exactly. They do not supply the missing pair-trace cancellation at times of order $N$.

The sharpness constructions below are comparison matrices used to establish the limits of these particular norm and interpolation arguments. They are not the specified matrices $U_N$, do not disprove their spectral limit, and do not incorporate their full Fourier symbol or their short-time dispersion theorem. No previous source file is changed.

## 1. Inputs and notation

Work in the dimensions to which the proved character escape estimate applies:
$$
N=d^2m,\qquad m\le\sqrt N,\qquad N\ge10^{140},
$$
with $N$ odd. Set $Q=d^2$. There are $Q$ mutually orthogonal character projections $P_\chi$, each of rank $m$, with sum $I$. Write
$$
\mathcal P(Y)=\sum_\chi P_\chi YP_\chi,\qquad
E=e^{i\tau NA_N},\qquad U=EM_N.
$$
The input from *arithmetic_comb_rescaled_gap.md*, Sections 3 and 3.1, SHA-256
898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f, is
$$
\sup_{\chi,\psi}\|P_\psi EP_\chi\|\le\rho,\qquad
\rho=\sqrt{4095/4096}.
\tag{1}
$$
In particular, for
$$
B=\mathcal P(E),\qquad C=E-B,\qquad
K=BM_N,\qquad R=CM_N,
$$
we have
$$
U=K+R,\qquad \|B\|=\|K\|\le\rho,\qquad
\|C\|=\|R\|\le1+\rho.
\tag{2}
$$
The exact character permutation interpretation of $K$ is established in
*phase_all_character_signed_trace_removal.md* and
*phase_sparse_character_histories.md*. Here the relevant polynomial is
$$
X(z)=K+zR=[zE+(1-z)B]M_N.
\tag{3}
$$
Statements using (1) apply only to the dimensions just specified. This does not establish an all-odd-$N$ estimate for dimensions without such a character decomposition.

## 2. A larger exact complex contraction domain

For every $z\in\mathbb C$,
$$
\boxed{\|X(z)\|\le r_\rho(z):=|z|+\rho|1-z|.}
\tag{4}
$$
Indeed, (3), unitarity of $E,M_N$, and $\|B\|\le\rho$ give (4) directly. Consequently,
$$
\Omega_\rho=\{z:|z|+\rho|1-z|<1\}
\tag{5}
$$
is a complex domain of strict contraction. It contains the entire real interval $[0,1)$, and $1$ belongs to its boundary. More precisely,
$$
\|X(t)\|\le t+(1-t)\rho
=1-(1-\rho)(1-t),\qquad 0\le t\le1.
\tag{6}
$$
The left real endpoint of the domain is
$$
-\frac{1-\rho}{1+\rho}
=-0.0000610426079676596\ldots.
$$
Near $z=1$, put $w=1-z$. Then
$$
r_\rho(1-w)=1-\operatorname{Re}w+\rho|w|+O(|w|^2).
$$
Thus the tangent interior sector at $1$ has half-angle
$$
\arccos\rho=\arcsin(1/64)
=0.01562563585273695\ldots.
\tag{7}
$$
This improves the previously used disk
$|z|<(1-\rho)/(1+\rho)$. It does not make the physical endpoint $z=1$ an interior point.

### 2.1 The exact conditional-expectation multiplier norm

The finite character group $G$ has $Q$ elements, and its exact unitary twirl is
$$
B=\frac1Q\sum_{g\in G}W_gEW_g^*.
$$
Therefore
$$
B+z(E-B)
=\frac{1+(Q-1)z}{Q}E
+\frac{1-z}{Q}\sum_{g\ne0}W_gEW_g^*.
\tag{8}
$$
For the linear map $\Lambda_z(Y)=\mathcal P(Y)+z(Y-\mathcal P(Y))$, this gives
$$
\|\Lambda_z\|\le
L_Q(z):=
\frac{|1+(Q-1)z|+(Q-1)|1-z|}{Q}.
\tag{9}
$$
The bound is exact, even if the supremum is restricted to unitary $Y$. To prove this, identify the equal-rank sectors with
$\mathbb C^Q\otimes\mathbb C^m$, let $F_Q$ be the discrete Fourier matrix, and take
$$
Y=F_Q^*\operatorname{diag}(\lambda_0,\ldots,\lambda_{Q-1})F_Q\otimes I_m,
\qquad |\lambda_j|=1.
$$
Its pinching is $cI$, where $c=Q^{-1}\sum_j\lambda_j$. On the eigenspace belonging to $\lambda_0$, the eigenvalue of $\Lambda_z(Y)$ is
$$
\frac{1+(Q-1)z}{Q}\lambda_0
+\frac{1-z}{Q}\sum_{j>0}\lambda_j.
$$
Choose $\lambda_0$ and the common value of the $\lambda_j$, $j>0$, to align the two displayed terms. Their absolute values then add to $L_Q(z)$, proving equality in (9).

Since the two coefficients in (8), counted with multiplicity, sum to $1$, we have $L_Q(z)\ge1$. Equality holds precisely for the real interval
$$
-\frac1{Q-1}\le z\le1.
\tag{10}
$$
For completeness, equality in the scalar triangle inequality requires both $1-z$ and $1+(Q-1)z$ to be nonnegative real numbers, which is equivalent to (10).

The all-block escape information genuinely improves (9). Indeed,
$$
L_Q(z)\ge |z|+\left(1-\frac2Q\right)|1-z|.
$$
Hence if $Q\ge2/(1-\rho)$, then $L_Q(z)\ge r_\rho(z)$. This condition holds in the dimensions considered here:
$$
\frac2{1-\rho}=16382.99993895739\ldots,\qquad Q\ge\sqrt N.
$$

### 2.2 Optimality of (4), even with the all-block bound

Suppose $Q$ is odd and $Q(1-\rho)\ge2$. For each fixed $z$, there is a unitary $E$, with $\mathcal P(E)=cI$ and all blocks bounded by $\rho$, which attains equality in (4). This assertion concerns the sharpness of the available matrix-norm information.

For $z(1-z)\ne0$, choose
$$
c=\rho\exp\big(i(\arg z-\arg(1-z))\big).
$$
Then
$$
|Qc-1|\le Q\rho+1\le Q-1.
$$
Because $Q-1$ is even, one can choose $Q-1$ unit complex numbers with sum $Qc-1$: if $T=Qc-1\ne0$, take half equal to
$$
e^{i(\arg T+\alpha)}
\quad\hbox{and half to}\quad
e^{i(\arg T-\alpha)},\qquad
\cos\alpha=\frac{|T|}{Q-1}.
$$
For $T=0$, take equal numbers $i$ and $-i$. Set $\lambda_0=1$, use those $Q-1$ numbers as the remaining eigenvalues, and define the circulant unitary $E$ as in Section 2.1. Then $\mathcal P(E)=cI$. On its $\lambda_0=1$ eigenspace,
$$
B+z(E-B)=\big((1-z)c+z\big)I,
$$
whose eigenvalue has absolute value $r_\rho(z)$. Right multiplication by any unitary $M_N$ leaves the norm unchanged. The cases $z=0,1$ follow directly.

Every diagonal scalar entry of this $E$ has absolute value $\rho$. Row unitarity therefore gives, for each off-diagonal scalar entry,
$$
|E_{ij}|\le\sqrt{1-\rho^2}=\frac1{64}<\rho.
$$
Tensoring with $I_m$ proves the same assertion for all equal-rank block norms. Thus the construction satisfies the full bound (1), not merely $\|B\|\le\rho$.

It follows that no universally stronger norm bound than (4), and no larger universally guaranteed complex contraction domain, can be inferred from these matrix properties alone. This is not an assertion that the specified $E_N$ attains the bound.

## 3. Exact Kadison and Hilbert--Schmidt identities

The pinching is an orthogonal projection for the Hilbert--Schmidt inner product. Since $\mathcal P(C)=0$ and $B$ is block diagonal,
$$
\operatorname{Tr}(B^*C)=0,\qquad
\|C\|_{\mathrm{HS}}^2=N-\|B\|_{\mathrm{HS}}^2.
\tag{11}
$$
The bimodule property also gives the operator identities
$$
\mathcal P(B^*C)=0,\qquad
\mathcal P(C^*C)=I-B^*B.
\tag{12}
$$
For example, the second follows by expanding
$\mathcal P((E-B)^*(E-B))$, using $E^*E=I$ and
$\mathcal P(E^*B)=\mathcal P(E)^*B=B^*B$.

It follows that
$$
\boxed{
\|X(z)\|_{\mathrm{HS}}^2
=\|B\|_{\mathrm{HS}}^2+|z|^2\big(N-\|B\|_{\mathrm{HS}}^2\big).
}
\tag{13}
$$
If $\nu=N^{-1}\|B\|_{\mathrm{HS}}^2$, then $0\le\nu\le\rho^2$. In particular, when $|z|\le1$,
$$
\|X(z)\|_{\mathrm{HS}}^2
\le N\big(\rho^2+(1-\rho^2)|z|^2\big),
$$
and
$$
|\operatorname{Tr}X(z)^n|
\le N\,r_\rho(z)^{\,n-1}
\sqrt{\rho^2+(1-\rho^2)|z|^2}.
\tag{14}
$$
Here
$|\operatorname{Tr}Y|\le\sqrt N\|Y\|_{\mathrm{HS}}$ and
$\|X^n\|_{\mathrm{HS}}\le\|X\|^{n-1}\|X\|_{\mathrm{HS}}$
prove (14).

There is a stronger-looking, but sector-restricted, identity. If $v$ lies in one character sector, then $Bv$ lies in that sector and $Cv$ lies in its orthogonal complement. Thus
$$
\|(B+zC)v\|^2
=\|Bv\|^2+|z|^2\|Cv\|^2
\le\big(\rho^2+(1-\rho^2)|z|^2\big)\|v\|^2
\quad (|z|\le1).
\tag{15}
$$
The same statement for $X(z)$ holds after taking account of the permutation of input sectors by $M_N$. It is not a full-space operator-norm bound: a superposition of sectors retains the omitted cross terms. The sharpness construction of Section 2.2 explicitly prevents that replacement.

Equation (13) gives an additional exact boundary obstruction for the original matrices. If $|z|>1$, then
$$
\|X(z)\|^2
\ge\frac1N\|X(z)\|_{\mathrm{HS}}^2
\ge1+(1-\rho^2)(|z|^2-1)>1.
\tag{16}
$$
Thus their actual contraction set is contained in the closed unit disk. In particular, no open neighborhood of $z=1$ is contractive. Along the real axis one has the stronger direct inequality
$$
\sigma_{\min}(X(1+\delta))
\ge1+(1-\rho)\delta>1,\qquad \delta>0,
\tag{17}
$$
by writing $X(1+\delta)=(1+\delta)U-\delta K$.

## 4. What damping costs at the $n\asymp N$ boundary

Put $t=1-\delta$, $0\le\delta\le1$, and
$$
r_t=1-(1-\rho)\delta.
$$
The available power bound is
$$
|\operatorname{Tr}X(t)^n|\le Nr_t^n.
\tag{18}
$$
A nonvanishing damping exponent at $n\asymp N$ requires $\delta N$ not to tend to zero. For a compact time window $aN\le n\le bN$, $a>0$, reducing the dimension-bound sum of $O(N)$ normalized squared traces to $o(1)$ through (18) requires at least a logarithmic exponent, hence $\delta N$ of order $\log N$ in this estimate.

The exact telescoping identity is
$$
U^n-X(t)^n
=\delta\sum_{j=0}^{n-1}U^{n-1-j}R X(t)^j.
\tag{19}
$$
It gives both
$$
\|U^n-X(t)^n\|
\le n\delta(1+\rho)
\tag{20}
$$
and
$$
\|U^n-X(t)^n\|
\le\frac{1+\rho}{1-\rho}(1-r_t^n).
\tag{21}
$$
Since both $U$ and $X(t)$ are contractions,
$$
\frac1{N^2}
\left|
|\operatorname{Tr}U^n|^2-|\operatorname{Tr}X(t)^n|^2
\right|
\le\min\{1,\,2(1+\rho)n\delta\}.
\tag{22}
$$
Consequently, for a bounded weight supported in $[0,b]$,
$$
\frac1{N^2}\sum_{n\ge1}|w(n/N)|
\left|
|\operatorname{Tr}U^n|^2-|\operatorname{Tr}X(t)^n|^2
\right|
=O_w(\delta N^2).
\tag{23}
$$
For the exponential weight $a_N^n=e^{-2sn/N}$, the explicit upper bound is
$$
2(1+\rho)\delta\frac{a_N}{(1-a_N)^2}
=O_s(\delta N^2).
\tag{24}
$$
Thus these continuity estimates certify an $o(1)$ transfer only in the range $\delta N^2\to0$, where the damping in (18) disappears at $n\asymp N$. This is a limitation of the estimates, not a proof that the original trace difference cannot cancel.

The physical Hilbert--Schmidt metric records the same separation. The reverse triangle inequality and (18) at the operator level give
$$
\|U^n-X(t)^n\|_{\mathrm{HS}}
\ge\sqrt N\,(1-r_t^n).
\tag{25}
$$
For $\delta=a/N$, $n/N\to c>0$, the right-hand side divided by $\sqrt N$ tends to $1-e^{-(1-\rho)ac}$. A damped approximation on that scale is therefore not small in this metric. This does not rule out cancellation in its trace.

### 4.1 The $\delta N^2$ transfer order is sharp for these hypotheses

Here is an exact closed-trace test of the preceding continuity step. Let $N=d^2$, with $d$ an odd multiple of $3$, and take coordinate rank-one pinching. Let
$$
E=F_N^*\operatorname{diag}
(\underbrace{1,\ldots,1}_{2N/3},
 \underbrace{-1,\ldots,-1}_{N/3})F_N,\qquad M=I.
$$
Then $E^2=I$, $B=\mathcal P(E)=cI$, $c=1/3$, and every scalar block has absolute value at most
$$
\max\{c,\sqrt{1-c^2}\}=\sqrt{8/9}<\rho.
$$
Thus these matrices satisfy all the pinching, unitarity, and block-gap inequalities used in Sections 2--4. They are not the original matrices.

The two eigenvalues of $X(1-\delta)$ are
$$
x_+=1-(1-c)\delta,\qquad
x_-=-[1-(1+c)\delta],
$$
with normalized multiplicities $(1+c)/2$ and $(1-c)/2$. Therefore, if $n\delta=o(1)$,
$$
\frac1N\operatorname{Tr}X(1-\delta)^n
=
\begin{cases}
1-n(1-c^2)\delta+O(n^2\delta^2),&n\ {\rm even},\\
c+O(n^2\delta^2),&n\ {\rm odd}.
\end{cases}
\tag{26}
$$
The errors are uniform for $n\le bN$ if $\delta N\to0$: Taylor's theorem applied to $(1-a\delta)^n$, $0\le a\le2$, bounds the remainder by $2n^2\delta^2$.

For a real $w\in C_c^1([0,\infty))$, (26) and the even-lattice Riemann sum give
$$
\begin{aligned}
&\frac1{N^2}\sum_{n\ge1}w(n/N)
\left(
|\operatorname{Tr}E^n|^2
-|\operatorname{Tr}X(1-\delta)^n|^2
\right)\\
&\qquad=(1-c^2)\delta N^2\int_0^\infty t\,w(t)\,dt
+O_w(\delta N+\delta^2N^3).
\end{aligned}
\tag{27}
$$
Indeed, the even terms contribute
$2(1-c^2)n\delta+O(n^2\delta^2)$, the odd terms contribute
$O(n^2\delta^2)$, and
$$
\sum_{\substack{n\ge1\\ n\ {\rm even}}}n\,w(n/N)
=\frac{N^2}{2}\int_0^\infty t\,w(t)\,dt+O_w(N).
$$
If $\delta=\kappa/N^2$, the signed trace-pair difference in (27) tends to
$$
\frac{8\kappa}{9}\int_0^\infty t\,w(t)\,dt.
\tag{28}
$$
It is positive for nonnegative $w$ with positive first moment. Thus the $O(\delta N^2)$ scale cannot be improved by a theorem using only these interpolation and block-norm data.

As an arithmetic check of (28), with $w(t)=(1-t)^2$ on $0\le t\le1$, zero otherwise, and $\kappa=1$, the proven limit is $2/27$. Direct evaluation of the two eigenvalue powers gives $0.0737100636$, $0.0740496744$, $0.0740737755$ at $N=81,1089,88209$, respectively. These numbers only check the already proved comparison-matrix formula.

## 5. Differentiated Ward identities and the remaining mixed trace

Let
$$
p_n=\operatorname{Tr}U^n,\qquad
q_n=\operatorname{Tr}(K U^{n-1}).
$$
Differentiating the finite polynomial $X(t)^n$ and using cyclicity gives
$$
\left.\frac{d}{dt}\operatorname{Tr}X(t)^n\right|_{t=1}
=n\operatorname{Tr}(R U^{n-1})=n(p_n-q_n).
\tag{29}
$$
Thus
$$
\boxed{
\left.\frac{d}{dt}|\operatorname{Tr}X(t)^n|^2\right|_{t=1}
=2n\big(|p_n|^2-\operatorname{Re}(\overline{p_n}q_n)\big).
}
\tag{30}
$$
The mixed trace $q_n$ retains the long-time phase information. Pinching alone does not give the sign of (30).

For comparison, the Hilbert--Schmidt derivative is completely evaluated:
$$
\boxed{
\left.\frac{d}{dt}\|X(t)^n\|_{\mathrm{HS}}^2\right|_{t=1}
=2n\big(N-\|B\|_{\mathrm{HS}}^2\big)
=2n\|C\|_{\mathrm{HS}}^2
\ge\frac{2nN}{4096}.
}
\tag{31}
$$
To prove this, differentiate $X(t)^n$. In the Hilbert--Schmidt pairing with $U^n$, each of the $n$ summands has trace $\operatorname{Tr}(RU^*)$ by cyclicity. Moreover,
$$
\operatorname{Tr}(KU^*)=\operatorname{Tr}(BE^*)=\|B\|_{\mathrm{HS}}^2,
$$
by the trace-orthogonality in (11). This proves (31). At the operator level the one-step derivative is
$$
\left.\frac d{dt}(X(t)^*X(t))\right|_{t=1}
=2I-U^*K-K^*U\ge2(1-\rho)I.
\tag{32}
$$
Equations (31)--(32) describe radial loss of singular norm. They do not replace (30).

### 5.1 The squared-trace derivative has neither universal sign

Take $Q=3$, $M=I$, coordinate pinching, and
$$
E=F_3^*\operatorname{diag}(1,e^{i\theta},e^{-i\theta})F_3,\qquad
B=bI,\quad b=(1+2\cos\theta)/3.
$$
Then
$$
\operatorname{Tr}X(t)^2
=3b^2+t^2(\operatorname{Tr}E^2-3b^2).
$$
If $\cos\theta=3/4$, then $b=5/6$, $\operatorname{Tr}E^2=5/4$, and
$$
\left.\frac d{dt}|\operatorname{Tr}X(t)^2|^2\right|_1=-\frac{25}{6}.
$$
If $\cos\theta=0$, then $b=1/3$, $\operatorname{Tr}E^2=-1$, and the same derivative is $16/3$.

Both examples satisfy all scalar block bounds by $\rho$, since a row's off-diagonal entries are bounded by $\sqrt{1-b^2}<\rho$. Repeating these blocks gives examples in arbitrarily large odd square dimensions with the same signs. These examples refute a universal monotonicity inference from the exact identities, not a sign assertion established using the particular original symbol.

## 6. Why holomorphic interpolation alone does not reach the endpoint

The normalized holomorphic traces
$$
f_n(z)=N^{-1}\operatorname{Tr}X(z)^n
$$
satisfy $|f_n(z)|\le r_\rho(z)^n$. In particular, they are exponentially small on any fixed compact subset of $\Omega_\rho$. This supplies no smallness at $z=1$, where the bound is $1$.

One direct scalar witness is
$$
g_n(z)=[\rho+(1-\rho)z]^n.
$$
It obeys $|g_n(z)|\le r_\rho(z)^n$, is exponentially small at every fixed interior point, and has $g_n(1)=1$. It is an actual eigencomponent of the circulant interpolation in Section 2.2 with $c=\rho$. Therefore a Schwarz--Pick, three-lines, or maximum-modulus conclusion based only on these holomorphic bounds cannot produce a decaying endpoint value. Its derivative $g_n'(1)=n(1-\rho)$ explicitly exhibits the $1/n$ boundary layer.

This obstruction occurs for closed traces as well. In the involution family of Section 4.1, $N^{-1}\operatorname{Tr}E^n=1$ for every even $n$, whereas $|N^{-1}\operatorname{Tr}X(z)^n|\le r_\rho(z)^n$ still tends exponentially to zero at every fixed interior point. The signed weighted transfer calculation (27) also shows the larger accumulated $N^2$ sensitivity of the pair functional.

For the exponential pair sum, the direct norm bound makes the endpoint loss visible without any interpolation theorem:
$$
\frac1{N^2}\sum_{n\ge1}e^{-2sn/N}
|\operatorname{Tr}X(t)^n|^2
\le \frac{e^{-2s/N}r_t^2}{1-e^{-2s/N}r_t^2}.
\tag{33}
$$
At $t=1$, its right-hand side is $O_s(N)$. An interior contraction estimate does not turn it into the required $O(1)$ expression at the physical endpoint.

## 7. Outcome of this branch

The executed gains are the complex domain (5), its optimality under the available block information, exact Hilbert--Schmidt and differentiated identities (13), (30), (31), and the quantitative boundary-transfer test (27). They explain precisely why the improved complex domain does not sum the dense-transition trace histories already left over by the sparse-history theorem.

No original spectral discrepancy has been shown to vanish through this interpolation. In particular, even the fixed pair estimate
$$
\frac1{N^2}\sum_{1\le n<2N}
|\widehat b_*(n/N)|^2
\big(|\operatorname{Tr}U_N^n|^2-\min(n,N)\big)\longrightarrow0
$$
remains unproved. The exact polynomial derivative exposes a mixed trace containing the same physical phases, and neither its weighted sum nor a replacement endpoint estimate is bounded at the needed scale here. The full $H_{\mathrm{diag}}$ assertion remains unresolved.

