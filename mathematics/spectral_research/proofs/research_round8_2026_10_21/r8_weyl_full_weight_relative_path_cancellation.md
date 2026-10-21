> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_weyl_full_weight_relative_path_cancellation.md`. Embedded SHA256: `038d6c03710c38829fba3d96367d271f5c33cdeacf94889d32cc3d7a22070109`.
> [Thematic guide](../../topics/dephasing.md).

# Full-weight cancellation of closed relative paths and the remaining endpoint interference

21 October 2026. Round 8, original-family Weyl branch.

## 1. Scope of the calculation

This file retains the exact kick
$E_N=e^{i\tau NA_N}$, $\tau=10^{-80}$, throughout.
There is no polynomial truncation, randomization, or dimension
average. All identities below hold at arbitrary positive integer
times, including times proportional to $N$.

Two exact statements are proved.

1. For every specified nonzero change of a Weyl path that preserves
   its endpoint, its full signed sum over all background paths
   vanishes. This includes every nonzero three-site
   Cayley--Hamilton change and every combination of such changes.
2. If $S^m-I$ is invertible modulo $N$, the complete
   endpoint-preserving sector of $|\operatorname{Tr}U_N^m|^2$
   is exactly $1$. The other endpoint sectors factor exactly
   into matrix elements of $\operatorname{Ad}E_N$; their
   residual phase cancels completely.

The first statement is a resolution of unitarity into individual
relative-path sectors. It is more specific than summing the squared
Weyl coefficients, but does not strengthen unitarity into a mixing
estimate. The calculation identifies exact cancellations in the
full weights and also identifies why they do not prove the ramp.
The remaining sum is precisely the trace of the full Weyl-adjoint
propagator on its traceless subspace. No estimate of that remaining
trace at $m\asymp N$ is proved here.

## 2. Conventions and exact coefficient identities

Throughout $N$ is odd, and all labels lie in
$\Lambda_N=(\mathbb Z/N\mathbb Z)^2$. Put

$$
W_N(k,l)=T_N(l,k),\qquad
\omega((k,l),(k',l'))=lk'-kl',\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

Let $\overline2$ and $\overline4$ denote modular inverses.
The previously proved, and independently audited, exact identities
are

$$
W(u)W(v)=e_N(\overline2\,\omega(u,v))W(u+v),
\quad M_NW(v)M_N^{-1}=W(Sv).
\tag{2.1}
$$

They are derived directly from the operators in the question in
`r8_weyl_three_time_resonance_and_exact_recursion.md`, Sections 2--4;
no ordinary-half convention is substituted here.

Expand the exact unitary kick:

$$
E_N=\sum_{\eta\in\Lambda_N}d(\eta)W(\eta),\qquad
d(\eta)=\frac1N\operatorname{Tr}(W(\eta)^*E_N),\qquad
\sum_\eta|d(\eta)|^2=1.
\tag{2.2}
$$

For later use define the finite ambiguity sum

$$
F_d(\delta,z)=\sum_{\eta\in\Lambda_N}
          d(\eta)\overline{d(\eta+\delta)}e_N(\omega(\eta,z)).
\tag{2.3}
$$

**Lemma 1.** For every $\delta\in\Lambda_N$,

$$
F_d(\delta,\overline2\delta)
 =F_d(\delta,-\overline2\delta)
 =\mathbf1_{\delta=0}.
\tag{2.4}
$$

Indeed the coefficient at $W(\delta)$ in $E_N^*E_N=I$
is

$$
\sum_\eta\overline{d(\eta)}d(\eta+\delta)
          e_N(-\overline2\omega(\eta,\delta))
       =\mathbf1_{\delta=0}.
$$

Its complex conjugate proves the first equality in (2.4).
Using $E_NE_N^*=I$ in the same way proves the second.
This verifies both signs rather than inferring one from a
continuous-half formula.

## 3. Exact cancellation for each closed relative path

Fix $m\ge1$. For a background path
$\eta=(\eta_0,\ldots,\eta_{m-1})$, define

$$
x_j=S^j\eta_j,\qquad
\lambda(\eta)=\sum_jx_j,\qquad
\mathcal A(\eta)=\sum_{i<j}\omega(x_i,x_j).
\tag{3.1}
$$

Fix also a relative path
$\delta=(\delta_0,\ldots,\delta_{m-1})$, and put

$$
a_j=S^j\delta_j,\qquad
A_{<j}=\sum_{i<j}a_i,\qquad
\Gamma=\sum_ja_j,\qquad
\mathcal A(\delta)=\sum_{i<j}\omega(a_i,a_j).
\tag{3.2}
$$

The endpoint changes from $\lambda$ to $\lambda+\Gamma$.
Direct expansion of every pair in (3.1) gives

$$
\boxed{
\mathcal A(\eta+\delta)-\mathcal A(\eta)
=\mathcal A(\delta)+
 \sum_j\omega(2A_{<j}+a_j-\Gamma,x_j).}
\tag{3.3}
$$

For completeness, the terms involving a fixed $x_j$ are
$\omega(A_{<j},x_j)+\omega(x_j,\Gamma-A_{<j}-a_j)$.
Antisymmetry of $\omega$ converts their sum to the term
in (3.3). This calculation is in the finite ring; no restriction
on $m$, label sizes, or prime factors of $N$ is involved.

Define the full background sum without the terminal trace factor:

$$
\mathcal C_m(\delta)=
 \sum_{\eta_0,\ldots,\eta_{m-1}}
 \left[\prod_jd(\eta_j)\overline{d(\eta_j+\delta_j)}\right]
 e_N\!\left(-\overline2[
      \mathcal A(\eta+\delta)-\mathcal A(\eta)]\right).
\tag{3.4}
$$

**Theorem 2.** For each relative path with $\Gamma=0$,

$$
\boxed{\mathcal C_m(\delta)=\mathbf1_{\delta_0=\cdots=\delta_{m-1}=0}.}
\tag{3.5}
$$

This is an identity for each fixed relative path, not only for the
sum of all such paths.

To prove it, (3.3) factorizes the finite sum (3.4):

$$
\mathcal C_m(\delta)=e_N(-\overline2\mathcal A(\delta))
 \prod_{j=0}^{m-1}
 F_d\!\left(\delta_j,
       S^{-j}A_{<j}+\overline2\delta_j
                         -\overline2S^{-j}\Gamma\right).
\tag{3.6}
$$

If $\delta\ne0$, let $j_*$ be its first nonzero entry.
Then $A_{<j_*}=0$. Under $\Gamma=0$, the factor at
that entry is exactly
$F_d(\delta_{j_*},\overline2\delta_{j_*})=0$, by (2.4).
Thus the whole sum vanishes. For $\delta=0$, every local
factor is $\sum|d|^2=1$, so (3.5) also holds in that case.

The three-site change $(h,-6h,h)$, located at any consecutive
positions, satisfies $\Gamma=0$ because $S^2-6S+I=0$.
If $h\ne0$, it is a nonzero relative path and its full
weighted background sum is therefore exactly zero. The same
argument covers arbitrary closed relative paths, whether or not
they have been expressed using these local changes.

One can also sum (3.5) over all closed $\delta$ and recover
the norm identity $\sum_\lambda|v_m(\lambda)|^2=1$, where
$v_m$ is the Weyl coefficient vector of
$E_0\cdots E_{m-1}$. Thus (3.5) specifies cancellations
within that identity. Its proof uses only the exact unitarity of
the full kick, and works for any unitary matrix replacing $E_N$.

## 4. The exact terminal Gauss magnitude for every odd modulus

Write $R=S^m$, and put

$$
g_m(\lambda)=\operatorname{Tr}(W(\lambda)M_N^m),
\qquad K_m=\ker(R-I:\Lambda_N\to\Lambda_N).
$$

**Lemma 3.** For every odd $N$ and every $m$,

$$
\boxed{|g_m(\lambda)|^2
       =\sum_{v\in K_m}e_N(\omega(\lambda,v)).}
\tag{4.1}
$$

Here is a direct proof avoiding any assumed Gauss-sum theorem.
For any matrix $V$, the trace of conjugation
$B\mapsto VBV^*$ on the $N^2$-dimensional matrix space
is $|\operatorname{Tr}V|^2$. For example, in the matrix-unit
basis the diagonal coefficients sum to
$\sum_{x,y}V_{xx}\overline{V_{yy}}$.
For $V=W(\lambda)M_N^m$, (2.1) gives

$$
V W(v)V^*=e_N(\omega(\lambda,Rv))W(Rv).
$$

In the orthonormal Weyl basis, a diagonal entry occurs exactly
when $Rv=v$, and has the phase displayed in (4.1).
This proves the lemma.

In particular, if $R-I$ is invertible, $K_m=\{0\}$
and

$$
|g_m(\lambda)|^2=1\quad\text{for every }\lambda.
\tag{4.2}
$$

Under this condition the full $\Gamma=0$ part of the
trace square uses a constant terminal multiplier. By (3.5), it
is exactly $1$, and each specified nonzero relative path
within that sector contributes zero after background summation.
When $R-I$ is not invertible, the nonconstant multiplier
(4.1) must be retained; (3.5) alone does not cancel its additional
characters. That case is not silently discarded.

## 5. Complete off-endpoint factorization when $R-I$ is invertible

Continue under the explicitly stated invertibility condition, and set

$$
H=(R-I)^{-1},\qquad C=(R+I)(R-I)^{-1}=I+2H.
$$

Define the quadratic form

$$
Q_R(\lambda)=-\overline4\,\omega(\lambda,C\lambda)
            =-\overline2\,\omega(\lambda,H\lambda).
\tag{5.1}
$$

The bilinear form $\omega(u,Cv)$ is symmetric. Indeed
$R$ is symplectic, and multiplication of the identity
$C^TJ+JC=0$ on the left by $(R-I)^T$ and on the
right by $R-I$ reduces it to

$$
(R+I)^TJ(R-I)+(R-I)^TJ(R+I)
           =2(R^TJR-J)=0,
$$

where $J$ denotes the matrix of $\omega$.
Consequently

$$
Q_R(\lambda+\Gamma)-Q_R(\lambda)-Q_R(\Gamma)
                  =-\overline2\omega(\lambda,C\Gamma).
\tag{5.2}
$$

The terminal trace has the exact phase law

$$
g_m(\lambda)=g_m(0)e_N(Q_R(\lambda)),\qquad |g_m(0)|=1.
\tag{5.3}
$$

To prove it, take $v=(I-R)^{-1}\lambda=-H\lambda$.
Conjugation by $W(v)$ and (2.1) show

$$
g_m(0)=e_N(-\overline2\omega(v,Rv))g_m((I-R)v).
$$

Since $Rv=v-\lambda$,
$\overline2\omega(v,Rv)
 =-\overline2\omega(\lambda,H\lambda)=Q_R(\lambda)$.
This proves (5.3); its modulus follows already from (4.2).
In particular

$$
g_m(\lambda)\overline{g_m(\lambda+\Gamma)}
=e_N\!\left(\overline2\omega(\lambda,C\Gamma)-Q_R(\Gamma)\right).
\tag{5.4}
$$

For a specified relative path $\delta$, include this full
terminal factor in its background sum and call the result
$\mathcal T_m(\delta)$. Explicitly,

$$
\begin{split}
\mathcal T_m(\delta)=
\sum_\eta&\left[\prod_jd(\eta_j)\overline{d(\eta_j+\delta_j)}\right]
 e_N\!\left(-\overline2[
        \mathcal A(\eta+\delta)-\mathcal A(\eta)]\right)\\
&\quad\cdot g_m(\lambda(\eta))
                \overline{g_m(\lambda(\eta)+\Gamma)}.
\end{split}
\tag{5.5}
$$

Equations (3.3) and (5.4) factor this entire sum into local sums:

$$
\mathcal T_m(\delta)=
e_N(-\overline2\mathcal A(\delta)-Q_R(\Gamma))
\prod_j F_d(\delta_j,w_j+\overline2\delta_j),
\quad
w_j=S^{-j}(A_{<j}+H\Gamma).
\tag{5.6}
$$

No modulus has been taken in obtaining (5.6).

To identify the local factors, define the exact Weyl-adjoint matrix

$$
C^E_{u,v}=\frac1N\operatorname{Tr}(W(u)^*E_NW(v)E_N^*).
\tag{5.7}
$$

Multiplying the three Weyl operators in this expression gives

$$
C^E_{v-\delta,v}
 =e_N(-\overline2\omega(v,\delta))
                  F_d(\delta,v-\overline2\delta).
\tag{5.8}
$$

For example, the phase before summation is exactly
$\omega(\eta,v)-\overline2\omega(\eta,\delta)
 -\overline2\omega(v,\delta)$, which verifies the order
and the signs in (5.8).
Thus the factors in (5.6) are

$$
F_d(\delta_j,w_j+\overline2\delta_j)
 =e_N(\overline2\omega(w_j,\delta_j))
                         C^E_{w_j,w_j+\delta_j}.
\tag{5.9}
$$

The variables $w_j$ satisfy

$$
w_j+\delta_j=Sw_{j+1},\qquad w_m=w_0=H\Gamma.
\tag{5.10}
$$

For the endpoint relation use $I+H=RH$, so
$S^{-m}(\Gamma+H\Gamma)=H\Gamma$.
Moreover,

$$
\begin{split}
\sum_j\omega(w_j,\delta_j)
 &=\sum_j\omega(A_{<j}+H\Gamma,a_j)\\
 &=\mathcal A(\delta)+\omega(H\Gamma,\Gamma)\\
 &=\mathcal A(\delta)+2Q_R(\Gamma).
\end{split}
\tag{5.11}
$$

The phases in (5.9), accumulated using (5.11), therefore cancel
the entire prefactor in (5.6). We obtain the exact identity

$$
\boxed{\mathcal T_m(\delta)
       =\prod_{j=0}^{m-1}C^E_{w_j,Sw_{j+1}}.}
\tag{5.12}
$$

This displays the result of the proposed complete weighted
Cayley--Hamilton resummation in explicit matrix elements.

## 6. What the remaining endpoint sums equal

Let $C^U$ be the Weyl matrix of $\operatorname{Ad}U_N$.
The exact covariance gives

$$
C^U_{u,v}=C^E_{u,Sv}.
\tag{6.1}
$$

For fixed $\Gamma$, the map in (5.10) is a bijection between
relative paths with $\sum_jS^j\delta_j=\Gamma$ and
closed $w$-paths with fixed endpoint $w_0=H\Gamma$.
The inverse is $\delta_j=Sw_{j+1}-w_j$; its accumulated
sum telescopes to $(S^m-I)w_0=\Gamma$.
Summing (5.12) with that endpoint fixed gives

$$
\boxed{
\sum_{\delta:\ \sum S^j\delta_j=\Gamma}
      \mathcal T_m(\delta)
       =((C^U)^m)_{H\Gamma,H\Gamma}.}
\tag{6.2}
$$

Every such fully signed endpoint-sector sum has modulus at most
one, because $C^U$ is unitary on matrix Hilbert space.
This bound applies after all background and relative-path
summations in that sector. It gives no decay with $N$.

For $\Gamma=0$, (6.2) equals $1$, since conjugation
fixes the identity matrix $W(0)$. For nonzero $\Gamma$,
the paths remain in the traceless Weyl subspace: exact unitality
gives $C^U_{0,v}=C^U_{v,0}=0$ for $v\ne0$.
Summing all sectors therefore gives exactly

$$
|\operatorname{Tr}U_N^m|^2
 =1+\operatorname{Tr}\left((C^U|_{W(0)^\perp})^m\right).
\tag{6.3}
$$

Of course (6.3) also follows abstractly from conjugation. Its value
here is that (3.5), (5.12), and (6.2) check precisely what the
full weighted path resummation cancels, with the original modular
phases, and what it leaves. In particular, it does **not** leave
a stochastic transition matrix or an independent-phase model.

The previously proved decay of each entry of $C^E$ at large
Weyl labels does not provide an additional bound for (6.2) at
$m\asymp N$. For example, splitting one matrix product and
using Cauchy--Schwarz gives only

$$
|((C^U)^m)_{v,v}|
\le\left(\sum_w|C^U_{v,w}|^2\right)^{1/2}
   \left(\sum_w|((C^U)^{m-1})_{w,v}|^2\right)^{1/2}=1.
\tag{6.4}
$$

Using the maximum-entry bound instead introduces the $\ell^1$
norm of a column, which is at most $N$, as there are $N^2$
labels. For the known large-label bound of order
$(1+|v|_N)^{-1/17}$, this is weaker than (6.4), even for
labels of order $N$. No additional signed cancellation in
the remaining coherent power is justified by that estimate.

Thus the first unproved step after this full factorization is an
estimate of the original weighted sum of the traces in (6.3),
not a missing local phase or finite-dimensional identity.

## 7. Heisenberg times at which the terminal factor is nondegenerate

The invertibility condition used above occurs at actual times of
order $N$ for infinitely many dimensions of the original family.
More precisely, for every odd prime power $N=p^a$, it holds
at $m=N$.

Here is a direct finite-ring proof. Write

$$
S=3I+2J_0,\qquad
J_0=\begin{pmatrix}0&1\\2&0\end{pmatrix},\qquad J_0^2=2I.
$$

Over $\mathbb F_p$, the commuting binomial terms and the
vanishing intermediate binomial coefficients give

$$
S^p=3I+2J_0^p
   =3I+2\varepsilon J_0,\qquad
\varepsilon=2^{(p-1)/2}\in\{1,-1\}.
$$

The last inclusion follows from Fermat's finite-field identity
$2^{p-1}=1$ and the fact that the only roots of
$x^2-1$ in a field of odd characteristic are $\pm1$.
If desired, Fermat's identity follows by multiplying the permutation
$x\mapsto2x$ of the nonzero elements of $\mathbb F_p$.
Since $(3I+2J_0)(3I-2J_0)=I$, this proves
$S^p=S$ or $S^{-1}$ modulo $p$. Iterating gives
$S^{p^a}=S$ or $S^{-1}$ modulo $p$.
Both choices satisfy

$$
\det(S^{\pm1}-I)=2-\operatorname{Tr}(S^{\pm1})=-4.
$$

Thus $\det(S^N-I)$ is not divisible by $p$, and
$S^N-I$ is invertible modulo $p^a$, as asserted.

Consequently, at $m=N=p^a$, the entire endpoint-preserving
sector of the original trace square is exactly $1$, whereas
the CUE benchmark for that complete trace square is $N$.
The contribution required to reach that benchmark must come
from the nonzero endpoint sectors in (6.2). This observation is
about a component of the exact sum; it does not assert that the
full original trace square fails or meets the benchmark.
Also, one specified time carries too little information to determine
the normalized weighted average in $H_{\mathrm{diag}}$.

For another explicit check on the scope, if $N=3^a$, then
$S^2=-I$ modulo three and $S$ has order four there.
Every $m$ not divisible by four has $S^m-I$ invertible
modulo three, and hence modulo $3^a$. Thus the same exact
sector cancellation applies at three of the four residue classes
of times in a Heisenberg window on this sequence. This still
gives no estimate for the full endpoint-interference sum.

## 8. The unresolved original signed estimate

The concrete pair functional still required for the task is

$$
\frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
 \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)\longrightarrow0.
\tag{8.1}
$$

The support of $\widehat b$ makes this sum finite for each
$N$. The identities above do not prove (8.1), even on the
prime-power sequence, and give no fixed $k,b,\epsilon$
counterexample to $H_{\mathrm{diag}}$. Their rigorously
established content is the full-weight cancellation (3.5), the
terminal character identity (4.1), and the exact residual
off-endpoint formula (5.12)--(6.2), with a precise explanation
of where the attempted resummation stops yielding estimates.

