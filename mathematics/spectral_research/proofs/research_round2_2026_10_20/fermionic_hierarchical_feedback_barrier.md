> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_hierarchical_feedback_barrier.md`. Embedded SHA256: `c1ff587a2ffc08d25af21fcff203a2788d2631b98c94f01fb7d888591b3f036a`.
> [Thematic guide](../../topics/histories.md).

# Mesoscopic quantum holes: exact truncation bounds and inherited feedback

Research continuation, 20 October 2026. All applications use the original
$U_N=\exp(i\tau N A_N)M_N$, with unchanged $\tau=10^{-80}$, and all
odd dimensions.

This note examines the new proposal of a hole of area about $1/\log N$,
returns of polylogarithmic length, and subsequent reduction to smaller
holes. The previous fixed-marker exclusion does not exclude this proposal.

The new unconditional conclusions are quantitative. For the actual
mesoscopic Fourier detector, the feedback inverse has norm at least
$c_sN/\log N$ somewhere on $|z|=e^{-s/N}$, and mean squared
Hilbert--Schmidt norm at least $c_sN^2/(\log N)^2$. A good internal
escape estimate would make its channel transfer almost unitary on this
circle; it would not make the channel transfer uniformly contractive.
The visible scalar inner degree remains the number of visible quantum
states, hence $N$ whenever the proposed open decay holds.

A separate exact error calculation shows that
$\|D_N^{T_N}\|\le N^{-6}$, $T_N\le N$, is sufficient for a
short-memory replacement in the full Abel pair functional with error
$O_s(N^{-1/2})$. This power estimate is not proved for the geometric
detector. A spatially constant absorber realizes the replacement exactly
on the original $U_N$, while retaining its phases in an explicit
fractional linear transform. Thus successful memory truncation alone
is not a new cancellation estimate.

The previous input is fermionic_quantum_marker_return.md, SHA-256
31c247eba33f35cdee9123dfbbaf9f711f1a2d47ed257b83e6136bda8793046e.
Its needed algebra is reproduced. No classical mixing or semiclassical
propagation estimate is invoked.

## 1. Exact transfer functions

Let $U=U_N$, and let $0\le E\le I$ be any finite effect. Set
$$
a=\sqrt{I-E},\quad b=\sqrt E,\quad
D=aU,\quad A=-a,\quad B=bU,
$$
$$
F_m=BD^{m-1}b,\qquad
\Theta(z)=-a+\sum_{m\ge1}z^mF_m
         =-a+zB(I-zD)^{-1}b.                         \tag{1.1}
$$
The block matrix
$$
\mathcal V=\begin{pmatrix}-a&bU\\ b&aU\end{pmatrix}    \tag{1.2}
$$
is unitary, since $a,b$ commute and $a^2+b^2=I$.
All resolvents in (1.1) exist for $|z|<1$.

Put
$$
c=b(I+a)^{-1},\qquad W=c^2=\frac{I-a}{I+a},\qquad
\beta=\operatorname{Tr}W.                            \tag{1.3}
$$
Functional calculus gives
$$
0\le W\le I,\qquad E/4\le W\le E.                    \tag{1.4}
$$
Indeed $W=E/(I+a)^2$, whose denominator lies between $I$ and $4I$.

Two exact identities are
$$
I-\Theta(z)^*\Theta(z)
=(1-|z|^2)b(I-\bar zD^*)^{-1}(I-zD)^{-1}b,           \tag{1.5}
$$
$$
\boxed{\displaystyle
(I-\Theta(z))^{-1}=\frac{I-W}{2}+c(I-zU)^{-1}c.}     \tag{1.6}
$$
For (1.5), put $y=(I-zD)^{-1}bx$. Apply unitarity of
$\mathcal V$ to $(x,zy)$:
$$
\|\Theta(z)x\|^2+\|y\|^2=\|x\|^2+|z|^2\|y\|^2.
$$
Polarization proves (1.5).

For (1.6), eliminate blocks in
$$
\begin{pmatrix}I+a&-zB\\-b&I-zD\end{pmatrix}.
$$
The other Schur complement uses
$$
D+b(I+a)^{-1}B=\{a+b^2(I+a)^{-1}\}U=U.
$$
Woodbury's formula, equivalently the two block eliminations, gives
$$
(I-\Theta)^{-1}
=(I+a)^{-1}
+z(I+a)^{-1}B(I-zU)^{-1}b(I+a)^{-1}.
$$
As $B=bU$ and $U$ commutes with its resolvent, this is
$$
(I+a)^{-1}+c\{(I-zU)^{-1}-I\}c.
$$
Finally $(I+a)^{-1}=(I+W)/2$, proving (1.6).

The resulting series is
$$
(I-\Theta(z))^{-1}
=(I+a)^{-1}+\sum_{m\ge1}z^m cU^mc.                  \tag{1.7}
$$
In particular
$$
\boxed{\|(I-\Theta(z))^{-1}\|\le(1-|z|)^{-1}.}       \tag{1.8}
$$
This bound needs no open escape estimate.

## 2. What an open gap would imply for the channels

Let $r=e^{-s/N}$, with fixed $s>0$. Write
$$
G_N(r)=\sup_{|z|=r}\|(I-zD)^{-1}\|.
$$
Equation (1.5) gives the exact consequence
$$
0\le I-\Theta(z)^*\Theta(z)
\le(1-r^2)G_N(r)^2E
\le(1-r^2)G_N(r)^2I.                               \tag{2.1}
$$
Whenever the last scalar is below one,
$$
s_{\min}(\Theta(z))
\ge\sqrt{1-(1-r^2)G_N(r)^2}.                        \tag{2.2}
$$
Thus an actually proved $G_N(r)\le C\log N$ would give
$$
s_{\min}(\Theta(z))
\ge1-C_s(\log N)^2/N                               \tag{2.3}
$$
uniformly on the Heisenberg circle. The transfer would be almost unitary
in every channel. It would not be a contraction bounded away from one.

For a hard hole $E=P=P^2$, $Q=I-P$, the nontrivial transfer on
$P\mathcal H$ is
$$
\theta_P(z)
=zPUP+z^2PUQ(I-zQUQ)^{-1}QUP.                       \tag{2.4}
$$
On $Q\mathcal H$ the full $\Theta$ is simply $-I$. If
$\|(I-zQUQ)^{-1}\|\le G$, then
$$
0\le I_P-\theta_P(z)^*\theta_P(z)
\le(1-r^2)(1+G^2)I_P.                              \tag{2.5}
$$
Indeed
$$
(I-zQU)^{-1}P=P+z(I-zQUQ)^{-1}QUP,
$$
and the two summands have orthogonal ranges. Substitute into (1.5).

These are consequences, not negations, of good internal escape.
The internal propagator describes evolution before a return. The channel
transfer is the boundary scattering function of a finite closed unitary
system. None of (2.1)--(2.5) supplies contraction of a nonidentity inserted
return correlation.

## 3. Unconditional lower bounds for the feedback inverse

Let $R_\Theta(z)=(I-\Theta(z))^{-1}$. From (1.6),
$$
\operatorname{Re}R_\Theta(z)
=\tfrac12I+\tfrac12c\,\mathcal P_U(z)c,              \tag{3.1}
$$
$$
\mathcal P_U(z)
=(1-|z|^2)(I-\bar zU^*)^{-1}(I-zU)^{-1}\ge0.
$$
In an orthonormal eigenbasis $U\psi_j=e^{i\vartheta_j}\psi_j$,
the diagonal entries of $\mathcal P_U$ are
$(1-r^2)/|1-ze^{i\vartheta_j}|^2$. At
$z=re^{-i\vartheta_j}$, the $j$-th entry is
$(1+r)/(1-r)$.

Let $w_j=\langle\psi_j,W\psi_j\rangle=\|c\psi_j\|^2$.
They are nonnegative, sum to $\beta$, and one is at least $\beta/N$.
If $\beta>0$, apply (3.1) to the corresponding direction $c\psi_j$;
if $\beta=0$, $R_\Theta=I/2$. In either case,
$$
\boxed{\displaystyle
\sup_{|z|=r}\|R_\Theta(z)\|
\ge\frac12+\frac{1+r}{2(1-r)}\frac{\beta}{N}.}        \tag{3.2}
$$
Repeated eigenvalues are allowed. No equidistribution of eigenvectors
has been used.

Parseval in (1.7) also gives
$$
\int_0^1\|R_\Theta(re^{2\pi it})\|_{\rm HS}^2dt
=\|(I+a)^{-1}\|_{\rm HS}^2+\sum_{m\ge1}r^{2m}f_m,
\quad f_m=\operatorname{Tr}(WU^mWU^{-m}).           \tag{3.3}
$$
In the same eigenbasis,
$$
f_m=\sum_{j,k}|W_{jk}|^2e^{im(\vartheta_k-\vartheta_j)},\qquad
f_{-m}=f_m.
$$
Hence
$$
f_0+2\sum_{m\ge1}r^{2m}f_m
=\sum_{j,k}|W_{jk}|^2
 \frac{1-r^4}{|1-r^2e^{i(\vartheta_k-\vartheta_j)}|^2}
\ge \frac{1+r^2}{1-r^2}\frac{\beta^2}{N}.            \tag{3.4}
$$
Every term in the Poisson-kernel sum is nonnegative. Its diagonal is
$(1+r^2)(1-r^2)^{-1}\sum_jw_j^2$, and
$\sum_jw_j^2\ge\beta^2/N$. Individual oscillatory power cross terms
have not been discarded.

Using $(I+a)^{-1}=(I+W)/2$ and
$\operatorname{Tr}W^2\le\beta$, we obtain
$$
\boxed{\displaystyle
\int_0^1\|R_\Theta(re^{2\pi it})\|_{\rm HS}^2dt
\ge \frac N4+\frac\beta4
   +\frac{\beta^2}{2N}\frac{1+r^2}{1-r^2}.}          \tag{3.5}
$$
The final quotient is $\coth(s/N)$.

For a hard projection of rank $d$, the constant $-I$ channels can be
removed exactly. Equation (1.6) restricted to $P\mathcal H$ is
$$
(I_P-\theta_P(z))^{-1}=P(I-zU)^{-1}P.
$$
Repeating (3.3)--(3.4), with exact constant term $d$, yields
$$
\boxed{\displaystyle
\int_0^1\|(I_P-\theta_P(re^{2\pi it}))^{-1}\|_{\rm HS}^2dt
\ge\frac12\left(d+\frac{d^2}{N}\coth(s/N)\right).}    \tag{3.6}
$$

### 3.1. The actual mesoscopic Fourier detector

For sufficiently large $N$, choose consecutive coordinate and
frequency windows, centered at the coordinates of $(1/2,0)$, of sizes
$$
r_N=s_N=\left\lfloor N/\sqrt{\log N}\right\rfloor,
$$
and define the exact finite effect
$$
E_N=P_{I_N}\mathcal F_N^*P_{J_N}\mathcal F_NP_{I_N}.  \tag{3.7}
$$
It is a positive contraction, with exact trace
$$
\operatorname{Tr}E_N=r_Ns_N/N
=\frac{N}{\log N}(1+o(1)).
$$
Consequently $\beta_N\ge N(1+o(1))/(4\log N)$.
For the original $U_N$, along every odd dimension,
$$
\boxed{\displaystyle
\liminf_{N\to\infty}\frac{\log N}{N}
\sup_{|z|=e^{-s/N}}\|(I-\Theta_N(z))^{-1}\|
\ge\frac1{4s},}                                    \tag{3.8}
$$
$$
\boxed{\displaystyle
\liminf_{N\to\infty}\frac{(\log N)^2}{N^2}
\int_0^1\|(I-\Theta_N(e^{-s/N}e^{2\pi it}))^{-1}\|_{\rm HS}^2dt
\ge\frac1{32s}.}                                   \tag{3.9}
$$
These estimates do not assume a quantum or classical open gap.
They also do not identify (3.7) with a nonlinear Markov cylinder.
They show unconditionally that this mesoscopic effect retains a growing
feedback denominator on the Heisenberg circle.

## 4. The visible inner degree is preserved

For any unitary colligation
$$
\mathcal V=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad \Theta(z)=A+zB(I-zD)^{-1}C,
$$
one has
$$
\boxed{\displaystyle
\det\Theta(z)
=\det\mathcal V\,
 \frac{\det(D^*-zI)}{\det(I-zD)}.}                   \tag{4.1}
$$
To prove it, multiply
$$
\begin{pmatrix}A&B\\-zC&I-zD\end{pmatrix}
$$
on the right by $\mathcal V^*$. Unitarity makes the result
$$
\begin{pmatrix}I&0\\B^*&D^*-zI\end{pmatrix}.
$$
Compute determinants and eliminate $I-zD$ in the first matrix.
This also proves (4.1) when $A$ is singular.

For (1.2), the unitary reducing part of $D$ is exactly its dark space,
the largest $U$-reducing subspace in $\ker E$. In fact, if
$Dv=\lambda v$ and $|\lambda|=1$, equality in
$\|aUv\|\le\|v\|$ forces $Uv\in\ker E$; thus
$Uv=Dv=\lambda v$ and $v\in\ker E$. The unitary eigenvectors of
a finite contraction span its unitary reducing part; this follows
directly by equality in the norm inequality and orthogonal restriction.
The complementary seen part has spectral radius below one.

Each dark eigenvalue cancels in (4.1). Each remaining eigenvalue
$\lambda$ contributes
$$
\frac{\bar\lambda-z}{1-z\lambda},
$$
a scalar inner factor with one zero in the disk. Hence the degree of
the scalar inner function $\det\Theta$ is exactly
$$
\boxed{\dim\mathcal H_{\rm seen}.}                  \tag{4.2}
$$
Any actual open power decay $\|D^m\|\to0$ would therefore force degree
exactly $N$. Good escape does not decrease this degree.

For a hard hole of rank $d$, $D_Q=QUQ$ on $Q\mathcal H$,
$$
\boxed{\displaystyle
\det\theta_P(z)
=z^d\det U\,
 \frac{\det(D_Q^*-zI_Q)}{\det(I_Q-zD_Q)}.}            \tag{4.3}
$$
Apply (4.1) to the block decomposition of $U$, whose ordinary transfer
is $\theta_P(z)/z$. If there is no dark space, the degree is
$d+(N-d)=N$, including when $d\asymp N/\log N$.

## 5. Exact composition for nested holes

Let $\Pi\le P$, $R=P-\Pi$, $Q=I-P$. Decompose
$\mathcal H=\Pi\mathcal H\oplus R\mathcal H\oplus Q\mathcal H$.
Eliminate $Q$ from $I-zU$, giving $I_P-\theta_P(z)$, then
eliminate $R$. Associativity of these two block eliminations gives
$$
\boxed{\displaystyle
\theta_\Pi(z)
=(\theta_P)_{\Pi\Pi}
+(\theta_P)_{\Pi R}
 (I_R-(\theta_P)_{RR})^{-1}(\theta_P)_{R\Pi}.}        \tag{5.1}
$$
This is not an ordinary product of independently estimated return
probabilities. The new inverse has summed all intermediate returns.

The same elimination in the open compression on $R\oplus Q$ gives
$$
\boxed{\displaystyle
\det(I_{R\oplus Q}-zU_{R\oplus Q,R\oplus Q})
=\det(I_Q-zU_{QQ})\,
 \det(I_R-(\theta_P(z))_{RR}).}                     \tag{5.2}
$$
All inverses exist for $|z|<1$, because the direct open compressions
are contractions. These identities apply to any number of nested
projections and preserve the visible degree.

A degree count does not disprove the mesoscopic proposal. A new
estimate of fully summed noncommutative channel correlations could
still make it useful. Equations (2.1), (3.8)--(3.9), and (5.1) explain
why an internal norm gap, without such an estimate, is not that
correlation contraction.

## 6. A rigorous short-memory error bound

This section is an exact implication with an explicitly unproved
premise for the geometric detector (3.7). It gives a sufficient error
budget without assuming an unknown Heisenberg approximation.

Fix $s>0$, $r=e^{-s/N}$, and $1\le T\le N$. Suppose
$$
q=\|D^T\|\le N^{-6}.                               \tag{6.1}
$$
Define
$$
\Theta^{[T]}(z)=-a+\sum_{m=1}^Tz^mF_m,\qquad
d^{[T]}(z)=\sum_{m=1}^Tz^m\operatorname{Tr}D^m,
$$
$$
\mathcal G^{[T]}(z)
=d^{[T]}(z)+z\operatorname{Tr}\bigl[
 (I-\Theta^{[T]}(z))^{-1}(\Theta^{[T]})'(z)\bigr].    \tag{6.2}
$$
For large $N$, this is analytic on $|z|\le r$, and
$$
\boxed{\displaystyle
\sup_{|z|\le r}\left|
\sum_{m\ge1}z^m\operatorname{Tr}U^m-\mathcal G^{[T]}(z)
\right|\le C_sN^6q\le C_s.}                        \tag{6.3}
$$
Moreover
$$
\boxed{\displaystyle
\left|
N^{-2}\sum_{m\ge1}r^{2m}|\operatorname{Tr}U^m|^2
-N^{-2}\int_0^1|\mathcal G^{[T]}(re^{2\pi it})|^2dt
\right|\le C_sN^{-1/2}.}                           \tag{6.4}
$$
No prior $O(N^2)$ bound for the trace energy is used.

### Proof

The return tail is exactly
$$
\mathcal R_T(z)=\Theta(z)-\Theta^{[T]}(z)
=z^{T+1}BD^T(I-zD)^{-1}b.                          \tag{6.5}
$$
Contraction and $1-r\ge c_s/N$ give
$$
\|\mathcal R_T(z)\|\le C_sNq,\qquad
\|\mathcal R_T'(z)\|\le C_sN^2q                     \tag{6.6}
$$
on the entire disk, since differentiating (6.5) costs at most
$$
q\left(\frac{T+1}{1-r}+\frac1{(1-r)^2}\right).
$$
Also $\|F_m\|\le1$ implies
$$
\|\Theta'(z)\|\le(1-r)^{-2}\le C_sN^2.              \tag{6.7}
$$

By (1.8), the exact feedback inverse has norm at most $C_sN$.
Its product with $\mathcal R_T$ has norm
$\le C_sN^2q=o(1)$. A Neumann series proves invertibility of
$I-\Theta^{[T]}$ everywhere on the disk, with inverse norm at most
$2C_sN$. The resolvent identity gives
$$
\|(I-\Theta)^{-1}-(I-\Theta^{[T]})^{-1}\|
\le C_sN^3q.                                      \tag{6.8}
$$
Thus the difference of the feedback traces is bounded by
$$
N\bigl(C_sN^3q\cdot C_sN^2
       +2C_sN\cdot C_sN^2q\bigr)
\le C_sN^6q.                                      \tag{6.9}
$$

The exact determinant feedback identity yields
$$
\sum_{m\ge1}z^m\operatorname{Tr}U^m
=\sum_{m\ge1}z^m\operatorname{Tr}D^m
 +z\operatorname{Tr}[(I-\Theta)^{-1}\Theta'].
$$
For $m>T$, $\|D^m\|\le q$, so the omitted open-trace tail is
at most $Nqr^{T+1}/(1-r)\le C_sN^2q$. This proves (6.3).

Finally Parseval and $|\operatorname{Tr}U^m|\le N$ give
$$
\left\|\sum_{m\ge1}r^me^{2\pi imt}\operatorname{Tr}U^m
\right\|_{L^2(dt)}\le C_sN^{3/2}.
$$
The $L^2$ error from (6.3) is $O_s(1)$. The difference of
squared norms, divided by $N^2$, is therefore $O_s(N^{-1/2})$.
This proves (6.4).

An $o(N)$ error alone would not give (6.4) from the available bounds:
the norm of the original generating function is only known to be
$O_s(N^{3/2})$. The stronger error in (6.3) avoids that hidden step.

### 6.1. First unproved geometric power estimate

For (3.7), no bound (6.1) with $T=O((\log N)^C)$ has been
established in this research. One sufficient estimate would be
$$
\|(\sqrt{I-E_N}\,U_N)^m\|
\le C\exp(-\kappa m/\log N),\qquad m\ge0,            \tag{6.10}
$$
with constants independent of $N$. Taking
$T=\lceil(8/\kappa)(\log N)^2\rceil$ would then give (6.1)
for all sufficiently large $N$.

Equation (6.10) is not asserted to be true. The proved pressure and
sector bounds do not estimate the norm of this sequence with repeated
effect insertions. A classical escape rate is not a proof of it.

Even if (6.10) were established, the noncommutative correlations in
$\mathcal G^{[T]}$ would remain. The inverse lower bounds and the
degree formula would still apply. No missing correlation estimate
has been adopted as a hypothesis in any claimed conclusion.

## 7. A short-memory check on the original family

For $\log N>1$, take a spatially constant detector
$$
E_N=\epsilon_NI,\qquad
\epsilon_N=1/\log N,\qquad
\sigma_N=\sqrt{1-\epsilon_N}.                       \tag{7.1}
$$
Its trace is $N/\log N$, but its rank is $N$. It is not the
geometric joint coordinate/frequency detector (3.7). Only the detector
has changed; $U_N$ is the exact original matrix.

Here
$$
D_N=\sigma_NU_N,\qquad
F_{m,N}=\epsilon_N\sigma_N^{m-1}U_N^m,\qquad
\|D_N^T\|=\sigma_N^T\le e^{-T/(2\log N)}.            \tag{7.2}
$$
Thus $T=\lceil14(\log N)^2\rceil$ satisfies (6.1) for large $N$.
The full Abel statistic has the bounded-error short-memory
representation (6.4), without a conjecture about $U_N$.

Nevertheless the transfer and its feedback are exactly
$$
\boxed{\displaystyle
\Theta_N(z)=(zU_N-\sigma_NI)(I-\sigma_NzU_N)^{-1},}   \tag{7.3}
$$
$$
\boxed{\displaystyle
(I-\Theta_N(z))^{-1}
=\frac{I-\sigma_NzU_N}{1+\sigma_N}(I-zU_N)^{-1}.}    \tag{7.4}
$$
This follows by summing (7.2). On an eigenvector
$U_Nv=e^{i\vartheta}v$, the channel is
$$
\frac{ze^{i\vartheta}-\sigma_N}
     {1-\sigma_Nze^{i\vartheta}},
$$
and it reaches $1$ at precisely $z=e^{-i\vartheta}$.
The closed denominator therefore contains the original phase exactly.

This is an example on the original family, not a competing unitary
family. It proves that successful polylogarithmic memory truncation,
even with the desired total detector weight, is not by itself an
estimate of signed spectral correlations. It does not rule out an
estimate exploiting the geometry of the nonconstant detector.

## 8. Scope of the result

The fixed-$R_0$ marker-free cancellation theorem does not cover the
mesoscopic regime $N\Lambda^{-2R}\to\infty$. No claim to the contrary
is made here.

For the norm-controlled mesoscopic reduction, the first unproved step
is (6.1) for the actual repeatedly inserted open matrix at a
polylogarithmic time. Section 6 gives a complete error budget if that
step is obtained. Sections 2--5 prove that such a step would not itself
give uniform contraction of the channel transfer, reduce its visible
degree, or remove its feedback denominator.

The next spectral estimate would have to control the fully summed
trace products in
$$
z\operatorname{Tr}\bigl[
(I-\Theta_N^{[T_N]}(z))^{-1}(\Theta_N^{[T_N]})'(z)\bigr]
$$
together with the retained open polynomial, in the complete weighted
pair sum and then in all higher-order analogues. Neither that estimate
nor a refutation of $H_{\rm diag}$ is claimed here.

