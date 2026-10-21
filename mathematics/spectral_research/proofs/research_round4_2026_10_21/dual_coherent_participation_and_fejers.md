> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/dual_coherent_participation_and_fejers.md`. Embedded SHA256: `8a0779ea28cd664bf207e50fa2c71f908479b2dd1f5bacde414a87e3352825d1`.
> [Thematic guide](../../topics/dephasing.md).

# A finite-time obstruction to replacing coherent Weyl probabilities by Markov powers

Research continuation, 21 October 2026.

This note concerns the exact family in the question, with the fixed algebraic
kick $\tau=10^{-80}$, in every odd dimension $N\ge3$, $N\ne7$. It is
an additional consequence of the proved primitivity and effective minorization
in `dual_weyl_primitivity_and_quantitative_limits.md`, frozen SHA-256
`90cb06de5c56441dfdb17f6fa32a35484b00c7919bbddd899fb8954f950043c1`.
All linear-algebra and finite-time claims used below are proved here. No spectral
gap or simplicity of the spectrum of the original unitary is assumed.

The result is a quantitative limitation on a particular dephasing approximation.
It is neither a proof nor a refutation of the requested spectral-statistics
limit. The explicit time obtained from the available lower bound is much larger
than the Heisenberg time.

## 1. Exact objects and the result

Put
$$
M=N^2-1,\qquad
\Lambda=(\mathbb Z/N\mathbb Z)^2\setminus\{0\},\qquad
C=C_N(\tau)|_{\Lambda\times\Lambda},\qquad P=|C|^{\circ2}.
\tag{1.1}
$$
Thus throughout this note **C is the restricted M by M matrix**, acting on
the traceless matrices in the Weyl basis; the scalar identity mode has already
been removed. Superscript $\circ2$ denotes entrywise squared modulus, not
matrix squaring. Let
$$
Z_n=|C^n|^{\circ2},\qquad n\in\mathbb Z.
\tag{1.2}
$$
Both $Z_n$ and $P^n$, for $n\ge0$, are doubly stochastic. Only
$Z_1=P$ is automatic: dephasing after every step gives $P^n$, whereas
retaining phases until time n gives $Z_n$. Define the normalized finite
Fejer averages
$$
\mathscr Z_T=\frac1T\left[I+
 \sum_{n=1}^{T-1}\left(1-\frac nT\right)(Z_n+Z_n^t)\right],
\tag{1.3}
$$
$$
\mathscr P_T=\frac1T\left[I+
 \sum_{n=1}^{T-1}\left(1-\frac nT\right)
 \bigl(P^n+(P^n)^t\bigr)\right],\qquad T\in\mathbb N.
\tag{1.4}
$$
The weights in each average sum to one. Write
$\Pi=M^{-1}\mathbf1\mathbf1^t$, the uniform Markov projection, and
$$
\gamma_N=\frac{N-2}{N+1}.
\tag{1.5}
$$

The preceding note supplies explicit numbers
$$
L_N=6N^2,\qquad
a_N=(N^2-1)\exp(-2L_NF_N),\qquad 0<a_N<1,
\tag{1.6}
$$
where $F_N$ is the fully specified Huang exponential-form bound in its
Section 7, and proves
$$
P^{L_N}=a_N\Pi+(1-a_N)Q_N
\tag{1.7}
$$
for a doubly stochastic matrix $Q_N$. Its precise closed form is not
needed in any proof below; (1.6) records that the minorization and all times
below are explicit functions of the original family and N.

**Theorem D (coherent probability floor).** For every positive integer T,
$$
\boxed{\operatorname{Tr}\mathscr Z_T\ \ge\ 1+\gamma_N.}
\tag{1.8}
$$
There is a fixed label $v_N\in\Lambda$, allowed to depend on N but not T,
such that, for every T,
$$
(\mathscr Z_T)_{v_Nv_N}\ge\frac{1+\gamma_N}{M}.
\tag{1.9}
$$
Let
$$
T_N=\left\lceil\frac{4M L_N}{a_N\gamma_N}\right\rceil.
\tag{1.10}
$$
For every integer $T\ge T_N$,
$$
\boxed{\operatorname{Tr}(\mathscr Z_T-\mathscr P_T)
 \ \ge\ \frac{\gamma_N}{2},}
\tag{1.11}
$$
$$
(\mathscr Z_T-\mathscr P_T)_{v_Nv_N}
 \ge\frac{\gamma_N}{2M}.
\tag{1.12}
$$
In particular, for each specified N there is an integer
$N\le n<T_N$ such that
$$
\boxed{\operatorname{Tr}Z_n-\operatorname{Tr}P^n
 \ \ge\ \frac{\gamma_N}{4}.}
\tag{1.13}
$$
The right side tends to $1/4$. The upper endpoint $T_N$ is enormous;
the theorem does not locate this discrepancy at $n=O(N)$.

## 2. The exact fixed-space participation identity

Let the distinct eigenvalues of $U_N$ be $\eta$, with orthogonal
spectral projectors $R_\eta$ and multiplicities $m_\eta$. Orthogonality
of a unitary spectral decomposition follows directly by diagonalizing the
normal matrix. Its adjoint fixes precisely the matrices block diagonal with
respect to these eigenspaces: in an orthonormal eigenbasis, a matrix unit
$|\psi_j\rangle\langle\psi_k|$ has adjoint eigenvalue
$\eta_j\overline{\eta_k}$, which is one exactly when $\eta_j=\eta_k$.
Consequently
$$
r:=\dim\ker(C-I)=\sum_\eta m_\eta^2-1\ge N-1.
\tag{2.1}
$$
The subtraction removes the scalar matrix. Let $Q_1$ be the orthogonal
projection onto this fixed space. For a nonzero Weyl label v define
$$
q_v=(Q_1)_{vv}.
$$
With the normalized Hilbert--Schmidt inner product
$\langle X,Y\rangle=N^{-1}\operatorname{Tr}(X^*Y)$, the exact projection
formula is
$$
Q_1X=\sum_\eta R_\eta X R_\eta
\quad\hbox{for traceless }X.
\tag{2.2}
$$
Indeed, it retains exactly the matrix units identified above, and it preserves
trace. Therefore
$$
\boxed{q_v=\frac1N\sum_\eta
 \|R_\eta W_N(v)R_\eta\|_{\mathrm F}^2
 =\frac1N\sum_{j,k:\eta_j=\eta_k}
   |\langle\psi_j,W_N(v)\psi_k\rangle|^2.}
\tag{2.3}
$$
The matrix units $\sqrt N|\psi_j\rangle\langle\psi_k|$ are orthonormal
for this normalized inner product, which verifies the factor $1/N$.
There is no scalar contribution for nonzero v because $\operatorname{Tr}W_N(v)=0$.

Since $Q_1$ is an orthogonal projection,
$$
0\le q_v\le1,\qquad
\sum_{v\in\Lambda}q_v=r,\qquad
\max_vq_v\ge\frac rM\ge\frac1{N+1}.
\tag{2.4}
$$
Choose $v_N$ once and for all to maximize $q_v$. This is the label
used in Theorem D. The formula gives actual Weyl participation weights of the
commutant, rather than only its abstract dimension.

## 3. Exact Fejer decomposition and positivity

Let $\lambda$ range over the distinct eigenvalues of C, with orthogonal
spectral projectors $Q_\lambda$ and ranks $r_\lambda$. Thus
$$
C=\sum_\lambda\lambda Q_\lambda,\qquad
\sum_\lambda Q_\lambda=I,\qquad r_1=r.
$$
For $|z|=1$, set
$$
\Phi_T(z)=\frac1T\sum_{|n|<T}
  \left(1-\frac{|n|}T\right)z^n
 =\left|\frac1T\sum_{j=0}^{T-1}z^j\right|^2\ge0.
\tag{3.1}
$$
The equality follows by expanding the squared modulus: the difference
$j-k=n$ occurs $T-|n|$ times. Also $\Phi_T(1)=1$, and for fixed
$z\ne1$, the finite geometric-series formula gives
$\Phi_T(z)\to0$ as $T\to\infty$.

Expanding an entry of $C^n$ and its conjugate gives the exact matrix identity
$$
Z_n=\sum_{\lambda,\mu}(\lambda\bar\mu)^n
 Q_\lambda\circ\overline{Q_\mu}.
\tag{3.2}
$$
Here $\circ$ denotes entrywise multiplication. Since $C^{-n}=(C^n)^*$,
$Z_{-n}=Z_n^t$. Substituting (3.2) into (1.3) therefore proves
$$
\boxed{\mathscr Z_T=\sum_{\lambda,\mu}
 \Phi_T(\lambda\bar\mu)
 Q_\lambda\circ\overline{Q_\mu}.}
\tag{3.3}
$$

Every matrix $Q_\lambda\circ\overline{Q_\mu}$ is positive semidefinite.
For completeness, if positive semidefinite matrices A and B have Gram
representations $A_{uv}=\langle a_u,a_v\rangle$ and
$B_{uv}=\langle b_u,b_v\rangle$, then their entrywise product is the Gram
matrix of $a_u\otimes b_u$, hence is positive semidefinite. The complex
conjugate of a positive semidefinite matrix is positive semidefinite by
conjugating its Gram vectors. This proves the claim without importing a
positivity theorem.

It follows from (3.1)--(3.3) that
$$
\mathscr Z_T\succeq\mathscr Z_\infty,
\qquad
\mathscr Z_\infty:=\sum_\lambda
 Q_\lambda\circ\overline{Q_\lambda},
\tag{3.4}
$$
where $\succeq$ is the order on Hermitian matrices. Moreover,
$\mathscr Z_T\to\mathscr Z_\infty$ as $T\to\infty$, since (3.3) is
a finite sum and the off-diagonal eigenvalue pairs have $\lambda\bar\mu\ne1$.
The limiting matrix is real symmetric and positive semidefinite. It is doubly
stochastic because
$$
\sum_u(\mathscr Z_\infty)_{uv}
 =\sum_\lambda\sum_u|(Q_\lambda)_{uv}|^2
 =\sum_\lambda(Q_\lambda)_{vv}=1.
\tag{3.5}
$$
Hence its uniform vector has eigenvalue one and its orthogonal complement
has nonnegative eigenvalues, proving also
$$
\mathscr Z_T\succeq\mathscr Z_\infty\succeq\Pi.
\tag{3.6}
$$
These are finite-time inequalities; they need no lower bound on the spacing
between the eigenvalues of C.

## 4. The trace floor and a fixed Weyl-label witness

For each projector $Q_\lambda$, its diagonal entries are nonnegative and
sum to $r_\lambda$. The scalar Cauchy--Schwarz inequality gives
$$
\sum_v(Q_\lambda)_{vv}^2\ge\frac{r_\lambda^2}{M}.
$$
Taking the trace in (3.4) yields
$$
\operatorname{Tr}\mathscr Z_T
\ge\operatorname{Tr}\mathscr Z_\infty
 =\sum_\lambda\sum_v(Q_\lambda)_{vv}^2
\ge\frac1M\sum_\lambda r_\lambda^2.
\tag{4.1}
$$
All nonzero ranks are positive integers. Their sum is M, and the rank at
one is r. Thus
$$
\sum_\lambda r_\lambda^2
\ge r^2+(M-r)=M+r(r-1),
$$
and (2.1) proves
$$
\operatorname{Tr}\mathscr Z_T
\ge1+\frac{r(r-1)}M
\ge1+\frac{(N-1)(N-2)}{N^2-1}
=1+\gamma_N.
\tag{4.2}
$$
This is (1.8). Eigenvalue degeneracies can only improve the bound.

For the chosen label $v_N$, put $q=q_{v_N}\ge r/M$. Primitivity implies
$r<M$: otherwise $C=I$ and $P=I$, contradicting (1.7) with $a_N>0$.
There are at most $M-r$ distinct eigenvalues different from one. Their
nonnegative participation weights $(Q_\lambda)_{v_Nv_N}$ sum to $1-q$.
A second scalar Cauchy--Schwarz inequality gives
$$
(\mathscr Z_\infty)_{v_Nv_N}
\ge q^2+\frac{(1-q)^2}{M-r}.
\tag{4.3}
$$
The right side is increasing for $q\ge1/(M-r+1)$. Our lower bound
$q\ge r/M$ is in that interval, since
$$
\frac rM\ge\frac1{M-r+1}
\quad\Longleftrightarrow\quad (r-1)(M-r)\ge0.
$$
Inserting $q=r/M$ in (4.3) and then using (3.4) proves
$$
(\mathscr Z_T)_{v_Nv_N}
\ge\frac1M+\frac{r(r-1)}{M^2}
\ge\frac{1+\gamma_N}{M},
\tag{4.4}
$$
as required. The witness label is chosen using the exact commutant and is
independent of the averaging time.

## 5. Effective Markov comparison and the finite-time discrepancy

We derive the required norm estimate directly from (1.7). Every doubly
stochastic matrix B is a contraction on Euclidean space: by the scalar
weighted Cauchy--Schwarz inequality,
$$
\sum_u\left|\sum_vB_{uv}x_v\right|^2
\le\sum_{u,v}B_{uv}|x_v|^2=\sum_v|x_v|^2.
\tag{5.1}
$$
Also $B\Pi=\Pi B=\Pi$. For $n=qL_N+s$, $0\le s<L_N$,
the decomposition (1.7) gives
$$
P^n-\Pi=(1-a_N)^q P^s Q_N^q(I-\Pi).
$$
Using (5.1) proves
$$
\|P^n-\Pi\|_{2\to2}
\le(1-a_N)^{\lfloor n/L_N\rfloor}.
\tag{5.2}
$$
The same estimate holds for the transpose. Since the coefficients in (1.4)
sum to one,
$$
\|\mathscr P_T-\Pi\|_{2\to2}
\le\frac1T\left[1+2\sum_{n=1}^{T-1}
 \left(1-\frac nT\right)(1-a_N)^{\lfloor n/L_N\rfloor}\right]
\le\frac{2L_N}{a_NT}.
\tag{5.3}
$$
For the final inequality, extend the nonnegative sum to infinity and use
$\sum_{n\ge0}(1-a_N)^{\lfloor n/L_N\rfloor}=L_N/a_N$.
In particular
$$
\operatorname{Tr}\mathscr P_T\le1+\frac{2ML_N}{a_NT},
\qquad
(\mathscr P_T)_{vv}\le\frac1M+\frac{2L_N}{a_NT}.
\tag{5.4}
$$
The trace estimate follows by summing diagonal entries, each bounded by
the operator norm; no positivity claim about $\mathscr P_T-\Pi$ is used.
For $T\ge T_N$, (5.4) and (4.2), (4.4) give (1.11) and (1.12).

To prove (1.13), put $d_n=\operatorname{Tr}Z_n-\operatorname{Tr}P^n$.
Then $|d_n|\le M$, $d_0=d_1=0$, and
$$
\frac2{T_N}\sum_{n=1}^{T_N-1}
 \left(1-\frac n{T_N}\right)d_n\ge\frac{\gamma_N}{2}.
\tag{5.5}
$$
The contribution of $n<N$ to the left side is at most
$2M(N-1)/T_N\le\gamma_N/4$, because
$T_N\ge8M(N-1)/\gamma_N$; the latter follows from
$L_N/a_N\ge6N^2\ge2(N-1)$. The remaining weighted sum is therefore at
least $\gamma_N/4$. Its nonnegative weights have sum at most one, so at
least one $N\le n<T_N$ has $d_n\ge\gamma_N/4$.

The same argument using $|(Z_n-P^n)_{vv}|\le1$ and (1.12) shows that the
fixed label $v_N$ has some, possibly different, time $N\le n<T_N$ with
$$
(Z_n-P^n)_{v_Nv_N}\ge\frac{\gamma_N}{4M}.
\tag{5.6}
$$

## 6. What this forces on the omitted interference terms

The exact path expansion gives, for $n\ge0$,
$$
Z_{n+1}=PZ_n+\mathcal E_n,
\tag{6.1}
$$
$$
\mathcal E_n(u,v)=\sum_{w\ne w'}
 C_{u,w}\overline{C_{u,w'}}(C^n)_{w,v}
 \overline{(C^n)_{w',v}}.
\tag{6.2}
$$
Both row and column sums of $\mathcal E_n$ vanish: (6.1) subtracts two
doubly stochastic matrices. In addition $\mathcal E_0=0$, and iterating
(6.1) proves
$$
Z_n-P^n=\sum_{j=1}^{n-1}P^{n-1-j}\mathcal E_j\qquad(n\ge2).
\tag{6.3}
$$
Combining (1.11) with (6.3) shows, at every $T\ge T_N$,
$$
\frac2T\sum_{n=2}^{T-1}\left(1-\frac nT\right)
 \sum_{j=1}^{n-1}\operatorname{Tr}
 \bigl(P^{n-1-j}\mathcal E_j\bigr)
\ge\frac{\gamma_N}{2}.
\tag{6.4}
$$
Thus the omitted coherent cross terms have an unavoidable aggregate
contribution for the specified family, despite exact primitivity and eventual
mixing of P. The assertion is not based only on their possible signs.

One can also extract a small explicit lower bound on their average trace norm.
Since $\Pi\mathcal E_j=0$, (5.2) and the singular-value trace inequality
$|\operatorname{Tr}(AB)|\le\|A\|_{2\to2}\|B\|_*$ give
$$
\left|\operatorname{Tr}(P^q\mathcal E_j)\right|
\le(1-a_N)^{\lfloor q/L_N\rfloor}\|\mathcal E_j\|_*.
$$
The stated trace inequality follows by a singular-value decomposition of B:
each summand is bounded by its singular value times $\|A\|_{2\to2}$.
Summing the preceding bound first over $q=n-1-j$ in (6.4) gives
$$
\boxed{\frac1T\sum_{j=1}^{T-2}\|\mathcal E_j\|_*
 \ge\frac{a_N\gamma_N}{4L_N},\qquad T\ge T_N.}
\tag{6.5}
$$
This lower bound is numerically extremely weak because of the available
minorization constant, but it is quantitative and refers to the exact fixed
family. It rules out setting all coherent errors to zero or treating their
weighted accumulation as uniformly negligible on arbitrary long windows.

## 7. Precise relation to, and limitation for, the original spectral task

The return quantity used here has the exact original-matrix interpretation
$$
\operatorname{Tr}Z_n
 =\frac1{N^2}\sum_{v\in\Lambda}
 \left|\operatorname{Tr}\bigl[
 W_N(v)^*U_N^n W_N(v)U_N^{-n}\bigr]\right|^2.
\tag{7.1}
$$
It takes a squared modulus for each Weyl return amplitude before summing.
The original pair statistic instead involves
$$
\operatorname{Tr}C^n=|\operatorname{Tr}U_N^n|^2-1,
\tag{7.2}
$$
the sum of those complex return amplitudes. This distinction is essential.
The lower bound (1.8), or the failure of the Markov substitution in (1.11),
does not transfer to (7.2).

The first spectral-statistics estimate still not proved by this branch is,
for every admissible fixed b and its fixed Fourier support contained in
$[-B,B]$,
$$
\boxed{\frac1{N^2}\sum_{1\le n\le BN}
 |\widehat b(n/N)|^2
 \left[\operatorname{Tr}C^n-\bigl(\min(n,N)-1\bigr)\right]
 \longrightarrow0.}
\tag{7.3}
$$
This is exactly the required pair discrepancy, after its equal zero-frequency
term cancels. The support endpoint may be included because the smooth compactly
supported Fourier transform vanishes there when it is an endpoint of its support.
None of the all-order estimates needed for the full $H_{\rm diag}$ follow
from the Markov theorem alone.

The new conclusion is therefore specific: the exact fixed-space participation
identity forces a persistent additional Fejer return contribution of asymptotic
size one in the traceless Weyl probability dynamics, while the exactly derived
Markov chain has only its single uniform long-time mode. We have a completely
explicit finite window exhibiting this mismatch, but no control locating it
within a constant multiple of N, and no missing phase-cancellation estimate is
being silently assumed.
