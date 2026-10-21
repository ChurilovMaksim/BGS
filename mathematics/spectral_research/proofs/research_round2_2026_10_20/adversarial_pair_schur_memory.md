> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_pair_schur_memory.md`. Embedded SHA256: `a9811e26f0aaa15a3f94c61760da7f83446621057b65299c9107d2de1eab2c01`.
> [Thematic guide](../../topics/dephasing.md).

# Direct pair attempt through the actual adjoint dynamics: a sharp norm barrier

## 1. Target and status

For the original matrices, with the original fixed $\tau=10^{-80}$,
the target of this attempt was the weaker prerequisite
$$
 N^{-2}\sum_{m\ge1}e^{-2sm/N}
       |\operatorname{Tr}(U_N^m)|^2=O_s(1)
 \qquad(s>0).
 \tag{1.1}
$$
The proposed route was to eliminate rapidly mixing diagonal observables
from the exact adjoint dynamics and estimate the remaining return
operator by a contraction argument.

This attempt does **not** prove (1.1). It yields a precise obstruction
to that operator-norm route for the original family: after removing
the entire stationary commutant, the compressed return operator still
has norm-one powers almost up to time $N$. The obstruction concerns
the actual finite-dimensional operators, not a substituted comparison
family. It does not obstruct a Hilbert--Schmidt or signed-correlation
estimate of the required size.

The only quantitative family-specific input needed below is the
previously proved bound
$$
 |p_{m,N}|\le C e^{am}+2q_*^m,\qquad
 a=\tfrac12\log(3+2\sqrt2)-1000\tau^2>0,
 \quad 0<q_*<1,
 \tag{1.2}
$$
for every $m\ge1$ and all sufficiently large odd $N$, with a common
threshold. It follows from fermionic_quantitative_pressure.md, SHA-256
d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2,
and the identified all-Weyl quantum transfer input there. That proof was
independently checked in adversarial_quantitative_pressure_audit.md,
SHA-256 4a0276a9ccd8874779c0b886b3abd8b723d746327d881fe40088b3f0fec01e7e.

## 2. A proved bound on the actual commutant dimension

Let the distinct eigenvalues of $U_N$ have multiplicities
$n_{1,N},\ldots,n_{r_N,N}$. On
$\mathcal H_N=\operatorname{End}(\mathbb C^N)$, with its
Hilbert--Schmidt inner product, set
$$
 \mathcal C_N X=U_N XU_N^*,\qquad
 \mathcal E_N=\ker(\mathcal C_N-I).
$$
Then
$$
 d_N:=\dim\mathcal E_N=\sum_j n_{j,N}^2.
 \tag{2.1}
$$
Indeed, in an orthonormal eigenbasis, the matrix unit from the
$j$-eigenspace to the $k$-eigenspace is fixed precisely when the
two eigenvalues agree.

For completeness the following estimate is derived here rather than
assuming simplicity. Let
$$
 \mu_N=N^{-1}\sum_jn_{j,N}\delta_{\zeta_{j,N}},\qquad
 L_N=\left\lfloor\frac{\log N-2\log\log N}{a}\right\rfloor.
$$
In $L^2(\mu_N)$, the $L_N$ vectors $1,\zeta,\ldots,\zeta^{L_N-1}$
have Gram matrix $G_N$ with entries $p_{k-j,N}/N$. Equation (1.2)
and the row-sum bound give
$$
 \|G_N-I\|\le\frac2N\sum_{m=1}^{L_N-1}|p_{m,N}|
 =O((\log N)^{-2})=:\varepsilon_N.
 \tag{2.2}
$$
The bound on the finite geometric series is valid at this choice of
$L_N$, since $e^{aL_N}\le N/(\log N)^2$.

Apply the elementary Gram/Bessel inequality to the normalized
indicator of an atom of $\mu_N$. Each squared inner product with
one of the $L_N$ vectors is exactly that atom's mass. Consequently
$$
 L_N\frac{n_{j,N}}N\le\lambda_{\max}(G_N)\le1+\varepsilon_N.
$$
Summing $n_{j,N}^2\le(\max_k n_{k,N})n_{j,N}$ proves
$$
 \boxed{
 d_N\le\frac{(1+\varepsilon_N)N^2}{L_N}
       \le(a+o(1))\frac{N^2}{\log N}.
 }
 \tag{2.3}
$$
This is sufficient for the norm obstruction. It is much weaker than
simple spectrum and is not being represented as a multiplicity bound
at the CUE scale.

## 3. Removing all stationary modes before compression

Let
$$
 \mathcal H_N^\circ=\mathcal E_N^\perp,\qquad
 D_N^\circ:=\dim\mathcal H_N^\circ=N^2-d_N.
$$
Because $\mathcal C_N$ is unitary, its restriction
$\mathcal V_N$ to $\mathcal H_N^\circ$ is unitary. This removes
every stationary mode, including all extra modes caused by possible
spectral multiplicities.

Let $\mathcal J_N$ be the $N$-dimensional space of coordinate
diagonal matrices. Project it orthogonally to $\mathcal H_N^\circ$
and let $P_N$ be the orthogonal projection onto its resulting range.
Put $Q_N=I-P_N$, on $\mathcal H_N^\circ$, and
$$
 r_N^\circ=\operatorname{rank}P_N\le N-1,\qquad
 \mathcal D_N=Q_N\mathcal V_NQ_N\big|_{\operatorname{Ran}Q_N}.
 \tag{3.1}
$$
The rank bound uses $I\in\mathcal J_N\cap\mathcal E_N$.
The construction does not require an eigenbasis to be algebraic and
does not assume an explicit formula for the commutant projection.
All these are exact operators determined by the prescribed $U_N$.

## 4. An exact isometric subspace at every sufficiently short time

For an integer $t\ge0$, define
$$
 \mathcal K_{t,N}
 =\{X\in\mathcal H_N^\circ:
       P_N\mathcal V_N^jX=0\text{ for }0\le j\le t\}.
 \tag{4.1}
$$
There are $t+1$ linear conditions, each with rank at most
$r_N^\circ$. Hence
$$
 \dim\mathcal K_{t,N}
 \ge D_N^\circ-(t+1)r_N^\circ
 \ge N^2-d_N-(t+1)(N-1).
 \tag{4.2}
$$
For $X\in\mathcal K_{t,N}$, an induction gives
$$
 \mathcal D_N^jX=\mathcal V_N^jX
 \quad(0\le j\le t).
 \tag{4.3}
$$
At each step the defining conditions ensure that the orthogonal
projection $Q_N$ removes nothing. Unitarity therefore gives
$$
 \|\mathcal D_N^tX\|_{\rm HS}=\|X\|_{\rm HS}.
 \tag{4.4}
$$
Since $\mathcal D_N^t$ is a contraction, the positive operator
$I-(\mathcal D_N^t)^*\mathcal D_N^t$ annihilates
$\mathcal K_{t,N}$. Thus singular value one has multiplicity at
least the positive part of the right-hand side of (4.2). In particular,
$$
 \boxed{
 \|\mathcal D_N^t\|=1
 \quad\text{whenever }\quad
 N^2-d_N-(t+1)(N-1)>0.
 }
 \tag{4.5}
$$
The same proof gives the quantitative Hilbert--Schmidt lower bound
$$
 \|\mathcal D_N^t\|_{\rm HS}^2
 \ge [N^2-d_N-(t+1)(N-1)]_+.
 \tag{4.6}
$$

Combining (2.3) and (4.5), for every fixed $c>a$ and all sufficiently
large odd $N$,
$$
 \boxed{
 \|\mathcal D_N^t\|=1
 \qquad
 0\le t\le
 \left\lfloor N-\frac{cN}{\log N}\right\rfloor.
 }
 \tag{4.7}
$$
Indeed, substituting the endpoint into (4.2) leaves
$(c-a+o(1))N^2/\log N>0$. This is an actual consequence of the
proved pressure estimate and finite-dimensional geometry, uniform
over all odd dimensions after one common threshold.

There is also a useful exact special case: if simplicity is available
in a particular dimension, then $d_N=N$, and (4.5) gives
$\|\mathcal D_N^t\|=1$ for all $0\le t\le N-2$.
This statement is conditional only in its explicitly stated
simplicity premise; the all-odd result (4.7) does not require it.

## 5. Where the attempted Schur argument breaks

Write the exact unitary block decomposition of $\mathcal V_N$ as
$$
 \mathcal V_N=
 \begin{pmatrix}
  A_N^{\rm c}&B_N^{\rm c}\\ C_N^{\rm c}&\mathcal D_N
 \end{pmatrix}
 \quad\text{on }
 \operatorname{Ran}P_N\oplus\operatorname{Ran}Q_N.
$$
These block symbols are local to this section and are not the
Hamiltonian $A_N$ or the adjoint operator $\mathcal C_N$.
For $|z|<1$, define
$$
 R_D(z)=(I-z\mathcal D_N)^{-1},\qquad
 F_N(z)=A_N^{\rm c}
        +zB_N^{\rm c}R_D(z)C_N^{\rm c}.
 \tag{5.1}
$$
Eliminating the lower block in a linear equation gives the exact
Schur identity
$$
 P_N(I-z\mathcal V_N)^{-1}P_N
 =(I-zF_N(z))^{-1}.
 \tag{5.2}
$$
No long-time approximation has entered.

Unitarity gives a precise positivity identity as well:
$$
 I-F_N(z)^*F_N(z)
 =(1-|z|^2)(C_N^{\rm c})^*R_D(z)^*R_D(z)C_N^{\rm c}.
 \tag{5.3}
$$
To verify it, apply the block unitary to the vector
$(x,zR_D(z)C_N^{\rm c}x)$. Its output is
$(F_N(z)x,R_D(z)C_N^{\rm c}x)$. Equality of the squared norms
of these two vectors is exactly (5.3).

The failed step would be to replace this return kernel by a rapidly
decaying operator-norm memory, for example a bound
$\|\mathcal D_N^t\|\le C_0\rho^t$ with fixed $\rho<1$, or
even by $o(1)$ at a fixed positive fraction of the Heisenberg time.
Equation (4.7) disproves both proposed estimates for these actual
compressed operators. Removing the entire commutant does not repair
the step.

Equation (5.3) does show that $F_N(z)$ is contractive. By itself this
only yields the radial bound
$\|(I-zF_N(z))^{-1}\|\le(1-|z|)^{-1}$.
At the desired radial scale $1-|z|\asymp N^{-1}$, this does not
identify the angular density or provide the missing trace average.
The exact finite-dimensional return subspaces explain why norm
contraction cannot supply that information.

## 6. The remaining observable is quadratic, not a maximal norm

The exact adjoint spectrum consists of the ratios of the original
unitary eigenvalues. Therefore
$$
 \operatorname{Tr}\mathcal C_N^m=|p_{m,N}|^2.
$$
For $0<r<1$, expansion of the two absolutely convergent resolvent
series, followed by grouping equal exponent differences, gives
$$
 \bigl\|(I-r\mathcal C_N)^{-1}\bigr\|_{\rm HS}^2
 =\frac{N^2+2\sum_{m\ge1}r^m|p_{m,N}|^2}{1-r^2}.
 \tag{6.1}
$$
Thus (1.1), at $r=e^{-2s/N}$, is equivalent to an $O_s(N^3)$
bound for this Hilbert--Schmidt norm squared. The identity (6.1)
is also derived independently in the fermionic doubled-transfer
route; it is included here to specify the target of the failed
Schur estimate.

Removing the commutant separates the expression exactly into
$$
 \frac{d_N}{(1-r)^2}
 +\bigl\|(I-r\mathcal V_N)^{-1}\bigr\|_{\rm HS}^2.
 \tag{6.2}
$$
In particular an $O_s(N^3)$ bound would require $d_N=O(N)$.
Where simplicity is known this necessary condition is satisfied,
but the second term remains unestimated at the needed scale.

The large isometric subspaces in Section 4 do not contradict an
$O(N^3)$ Hilbert--Schmidt resolvent bound: summing their natural
dimensions over a time interval of length $N$ has precisely that
scale. They do contradict the proposed stronger norm-decay
replacement. The unresolved step is therefore the actual averaged
resolvent estimate, with its full coherent return kernel retained.
No contraction hypothesis or random-phase substitute is inserted
to bypass it. No conclusion about $H_{\rm diag}$ follows.
