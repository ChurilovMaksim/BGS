---

**Stable claim IDs:** BGS-FM-034, BGS-FM-035, BGS-FM-036.
title: "Fixed-strength coboundary kicks: locality, long-time conjugacy, and microscopic clustering"
author: "BGS research programme"
date: "5 September 2026"
---

# Status and result

This is a project proof, not a claim of priority, external acceptance, or full
formalization. It treats a fixed nonzero classical perturbation and obtains
operator-norm control beyond the Heisenberg time, but for a deliberately
nongeneric family smoothly conjugate to an arithmetic cat map. Consequently
it is not positive BGS universality and is not a counterexample to a formulation
that excludes inherited arithmetic structure. The new step within this project
is to establish that the **natural single-exponential kick**, not just a
quantization defined by conjugation, is conjugate modulo every inverse power
of the dimension. We prove this by an elementary Fourier remainder estimate.

Let
$$
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad M=T^{\mathsf T},\qquad
 \mathcal Cg=g\circ M.
$$
On the two-torus choose a real even smooth function $g$ with
$$
 \operatorname{supp}g\cap\operatorname{supp}(\mathcal Cg)=\varnothing,
 \qquad f=g-\mathcal Cg.                                      \tag{1}
$$
There is an infinite-dimensional real vector space of such generators,
constructed in Section 2, containing nonzero functions. Let $N$ be odd, let $U_N$ be the cat quantization with the exact
covariance below, and write
$$
 G_N=\operatorname{Op}_N(g),\quad D_N=\operatorname{Op}_N(\mathcal Cg),
 \quad A_{\kappa,N}=e^{i\kappa NG_N},\quad
 V_{\kappa,N}=e^{i\kappa N(G_N-D_N)}U_N.                       \tag{2}
$$
The real parameter $\kappa$ is fixed as $N\to\infty$. With the conventions
below it represents a classical Hamiltonian time $\kappa/(2\pi)$, not a
classical perturbation that shrinks with $N$.

**Theorem A (all-orders comparison).** For each fixed bounded set of $\kappa$
values and each $R>0$,
$$
 \delta_N:=\|V_{\kappa,N}-A_{\kappa,N}U_NA_{\kappa,N}^*\|_{\rm op}
       =O_{g,\kappa,R}(N^{-R}).                              \tag{3}
$$
For every fixed $p>0$ the same all-orders estimate holds uniformly after
raising both unitaries to any integer power $|t|\leq N^p$.
For the explicit Gevrey-2 bump in Section 2, constants $c,C>0$ also give
$$
 \delta_N\leq C\kappa^2N^2e^{-cN^{1/3}}                      \tag{4}
$$
for sufficiently large $N$. This conservative exponent is not claimed
optimal. It gives vanishing error even for $|t|\leq e^{cN^{1/3}/2}$.

**Theorem B (classical interpretation).** Let $\Phi_g^t$ be the Hamiltonian
flow specified by $\frac{d}{dt}(a\circ\Phi_g^t)=\{g,a\}\circ\Phi_g^t$,
with $\{g,a\}=g_q a_p-g_p a_q$. The map quantized by (2) is
$$
 M_\kappa=M\circ\Phi_f^{\kappa/(2\pi)}
 =\Phi_g^{-\kappa/(2\pi)}\circ M\circ\Phi_g^{\kappa/(2\pi)}. \tag{5}
$$
It is Anosov and mixing for area measure. For any nonzero example $g$ and
all sufficiently small fixed $\kappa\ne0$, it is nonlinear and differs from
$M$. Its conjugacy to $M$ is essential, not a symmetry that may be omitted
when interpreting its spectral statistics.

**Theorem C (microscopic stability along Pell moduli).** Let $K$ tend to
infinity through odd primes, put $N+F\sqrt2=(1+\sqrt2)^K$, and restrict to
the odd parity space of dimension $D=(N-1)/2=Kn$. For fixed $\kappa$ and sufficiently large $N$, the
spectrum consists of $K$ clusters, each containing exactly $n$ eigenvalues,
whose angular halfwidth $a_N$ is $O(N^{-R})$ for every $R$. After a common
rotation their centres are the $K$th roots of unity.

Under unfolding by the mean density $D$, the spacing measure tends weakly
to $\delta_0$. More quantitatively, for every fixed finite $p\geq1$,
$$
 W_p\left(\mu_{\rm gaps},(1-1/n)\delta_0+(1/n)\delta_n\right)
       \leq2Da_N.                                           \tag{6}
$$
For each fixed $x>0$, eventually the normalized ordered close-pair count is
**exactly** $n-1$. The local point process viewed from a uniformly random
origin converges vaguely in probability to the empty process, despite
having mean intensity one at every finite $N$.

Spacing collapse, divergence of close-pair counts, and this empty local
limit remain true under any increasing degree-one unfolding $F_N$ satisfying
$\|F_N'\|_\infty\leq C N^A$ for fixed $C,A$. Thus the present conclusion
cannot be removed by an unfolding with polynomially bounded distortion.
No assertion is made about unfoldings whose derivatives grow faster than
every power of $N$.

# 1. Quantization and a finite locality estimate

For an integer frequency $v=(a,b)$ use the **physical integer Fourier lift**
$$
 (Q_N(a,b)u)(x)=e^{2\pi ia(x-b/2)/N}u(x-b\bmod N).
$$
The half in this exponent is ordinary division, not the inverse of two in
$\mathbb Z/N\mathbb Z$. For the modular-centred convention $W_N$ used in
the earlier notes, $Q_N(a,b)=(-1)^{ab}W_N(a,b)$. In particular,
$$
 Q_N(v)Q_N(w)=e^{\pi i\omega(v,w)/N}Q_N(v+w),\qquad
 \omega(v,w)=v_1w_2-v_2w_1.                                 \tag{7}
$$
Each $Q_N(v)$ is unitary, $Q_N(v)^*=Q_N(-v)$, and parity sends $Q_N(v)$ to
$Q_N(-v)$. Set
$$
 \operatorname{Op}_N(a)=\sum_{v\in\mathbb Z^2}\widehat a(v)Q_N(v),
 \quad \mathcal M_r(a)=\sum_v|\widehat a(v)|(1+|v|_1)^r.
$$
The series converges absolutely in operator norm for smooth $a$;
$\|\operatorname{Op}_N(a)\|\leq\mathcal M_0(a)$, and real symbols give
Hermitian matrices. Frequency aliases cause no problem in this definition.

Since $T$ is the identity modulo two, its finite Weyl implementer also has
exact physical covariance
$$
 U_NQ_N(v)U_N^*=Q_N(Tv),\qquad
 U_N\operatorname{Op}_N(a)U_N^*=\operatorname{Op}_N(a\circ M). \tag{8}
$$
One such implementer has the kernel
$$
 U_N(x,y)=\frac{c_N}{\sqrt N}
 e_N\!\left((3x^2-2xy+3y^2)/8\right),\quad |c_N|=1,         \tag{9}
$$
where division by eight is modular. Orthogonality of additive characters
proves unitarity; direct substitution on the two Weyl generators proves
(8). The kernel is parity-preserving. Its global phase can be fixed later.

**Lemma 1 (disjoint-symbol product).** If $a,b\in C^\infty(\mathbb T^2)$
have disjoint closed supports, then for every integer $r\geq1$,
$$
 \|\operatorname{Op}_N(a)\operatorname{Op}_N(b)\|_{\rm op}
 \leq\frac{\pi^r}{r!N^r}\mathcal M_r(a)\mathcal M_r(b).       \tag{10}
$$

**Proof.** Expand (7) and Taylor-expand $e^{i\pi\omega/N}$ through degree
$r-1$. For real $z$ the integral Taylor remainder satisfies
$|e^{iz}-\sum_{j<r}(iz)^j/j!|\leq|z|^r/r!$, with no restriction on $z$.
For each $j<r$ the coefficient sum
$$
 \sum_{v,w}\widehat a(v)\widehat b(w)\omega(v,w)^j Q_N(v+w)
$$
is the quantization of
$$
 \frac{1}{(-4\pi^2)^j}\sum_{l=0}^j(-1)^l\binom jl
 (\partial_q^{j-l}\partial_p^l a)
 (\partial_q^l\partial_p^{j-l} b).                           \tag{11}
$$
All these functions vanish, including $ab$ at $j=0$, because derivatives
are supported in the respective original closed supports. Their Fourier
cancellation occurs before applying $Q_N$, so aliases do not invalidate it.
The remaining absolutely convergent sum is bounded using
$|\omega(v,w)|\leq|v|_1|w|_1$ and $\|Q_N(v+w)\|=1$. This proves (10).

For real $a,b$, their two products are adjoints, so
$$
 \|[\operatorname{Op}_N(a),\operatorname{Op}_N(b)]\|
 \leq\frac{2\pi^r}{r!N^r}\mathcal M_r(a)\mathcal M_r(b).      \tag{12}
$$
This all-orders statement is stronger than just Poisson commutation.

# 2. An explicit infinite-dimensional family and a Gevrey bound

Put $r_0=1/16$ and let $S$ be the union of the closed torus squares of
halfwidth $r_0$ centred at $(1/4,0)$ and $(3/4,0)$. If $(q,p)\in S$, the
second coordinate $2q+3p$ of $M(q,p)$ has distance at least
$$
 1/2-5r_0=3/16>r_0                                          \tag{13}
$$
from the integers. Therefore $S\cap M^{-1}S=\varnothing$. Every real even
smooth function supported in $S$ satisfies (1). This is an infinite-dimensional
space. For nonzero $g$, $f$ is nonzero because it equals $g$ on $S$.
Also $\int f=0$, regardless of the mean of $g$.

Here is the fixed example used numerically. Write $\langle x\rangle$ for
the representative of $x\bmod1$ in $[-1/2,1/2)$, set
$$
 \beta(u)=\begin{cases}\exp(1-1/(1-u^2)),&|u|<1,\\0,&|u|\geq1,\end{cases}
 \quad u_\pm(q)=\langle q\mp1/4\rangle/r_0,
$$
and choose $\eta=1/3$. Then
$$
 \begin{split}
 A(q)&=\beta(u_+(q))(1+\eta u_+(q))
                +\beta(u_-(q))(1-\eta u_-(q)),\\
 B(p)&=\beta(\langle p\rangle/r_0),\qquad g(q,p)=A(q)B(p).
 \end{split}                                                \tag{14}
$$
This $g$ is real, even and nonzero. The unequal tilts of its two lobes avoid
a spurious half-period translation symmetry in the numerical example; no
absence of all other symmetries is claimed.

For completeness, its Gevrey regularity and the nonoptimal stretched
exponential bound need no black-box pseudodifferential theorem. If
$D_t=1-t^2>0$, use the complex disk $|z-t|\leq D_t/8$. On this disk
$$
 |(1-z^2)-D_t|\leq17D_t/64,\qquad
 \mathop{\rm Re}(1-z^2)^{-1}\geq\frac{3008}{6561D_t}>
 \frac1{3D_t}.
$$
Cauchy's estimate and maximization of $D_t^{-j}e^{-1/(3D_t)}$ give
$$
 |\beta^{(j)}(t)|\leq e\,24^j(j!)^2.                         \tag{15}
$$
All derivatives extend by zero at $\pm1$. Multiplication by $1\pm\eta t$
changes the prefactor to at most $2e$, with the same base 24.

A concrete Fourier-moment estimate follows. Put $L_0=24/r_0$,
$B_0=9L_0/\pi$ and
$$
 A_0=8r_0+(8/3)r_0eL_0^2,\qquad
 B_1=2r_0+(2/3)r_0eL_0^2.
$$
Integrating the one-dimensional Fourier coefficients by parts $j+2$ times
and using $\sum_{k\ne0}k^{-2}=\pi^2/3$ proves
$$
 \sum_k(1+|k|)^j|\widehat A(k)|\leq A_0B_0^j(j!)^2,
 \quad
 \sum_k(1+|k|)^j|\widehat B(k)|\leq B_1B_0^j(j!)^2.           \tag{16}
$$
One uses $(j+2)^2(j+1)^2\leq4\,9^j$. Expanding the sum of the two
frequency weights gives
$$
 \mathcal M_j(g)\leq A_0B_1(2B_0)^j(j!)^2,
 \quad
 \mathcal M_j(\mathcal Cg)\leq A_0B_1(14B_0)^j(j!)^2,        \tag{17}
$$
since $\|T\|_1=7$. These explicit constants are intentionally coarse and
are not useful finite-size error bars for the numerical matrices below.

More generally, suppose $\mathcal M_j(g)\leq A_gB_g^j(j!)^s$ and
$\mathcal M_j(\mathcal Cg)\leq A_dB_d^j(j!)^s$ for some $s>1$.
The comparison proved in Section 3 has the bound
$$
 \delta_N\leq\kappa^2N^2A_gA_d(C/N)^j(j!)^{2s-1},
 \qquad C=\pi B_gB_d.                                      \tag{18}
$$
For $j=\lfloor(N/(2C))^{1/(2s-1)}\rfloor\geq1$, use $j!\leq j^j$ to
bound the last factor by $2^{-j}$. This proves a bound
$C'\kappa^2N^2\exp(-cN^{1/(2s-1)})$, and (4) follows for $s=2$.
The general factorial-growth/optimal-truncation mechanism is established
Gevrey analysis; this note does not claim to originate it or to improve the
best Gevrey remainders in other quantization settings.

# 3. Fixed-strength conjugacy, classical dynamics, and long times

For Hermitian $H,J$ and real $t$, the two-factor Duhamel inequality gives
$$
 \|e^{it(H+J)}-e^{itH}e^{itJ}\|\leq(t^2/2)\|[H,J]\|.        \tag{19}
$$
One proof differentiates
$e^{i(t-u)(H+J)}e^{iuH}e^{iuJ}$ and integrates the conjugation difference
of $J$ twice. Unitary invariance of the norm leaves a triangular integration
domain of area $t^2/2$. In particular, $|t|\|H\|$ need not be small.

By (8),
$$
 A_{\kappa,N}U_NA_{\kappa,N}^*
       =e^{i\kappa NG_N}e^{-i\kappa ND_N}U_N.
$$
Apply (19) with $t=\kappa N$, $H=G_N$, $J=-D_N$, and then (12). For every
integer $r\geq1$,
$$
 \boxed{\displaystyle
 \delta_N\leq\frac{\kappa^2\pi^r}{r!}N^{2-r}
                   \mathcal M_r(g)\mathcal M_r(\mathcal Cg).} \tag{20}
$$
This proves Theorem A and (18). Notice that we have not set the finite
commutator to zero, nor silently replaced the one-exponential kick by a
product of two kicks.

For integer $t$, telescoping products of unitaries, or their adjoints when
$t<0$, yields
$$
 \|V_{\kappa,N}^t-A_{\kappa,N}U_N^tA_{\kappa,N}^*\|
       \leq |t|\delta_N.                                   \tag{21}
$$
Choosing $r$ larger than any fixed polynomial time exponent proves the
all-polynomial-time assertion. The same estimate proves the stretched
exponential-time assertion from (4). Normalized traces differ by at most
$|t|\delta_N$; their absolute squares differ by at most $2|t|\delta_N$.
These statements control Heisenberg times $t\asymp D$, not just $O(\log N)$.

To establish (5), note that (1) implies $\{g,\mathcal Cg\}=0$, so the two
Hamiltonian flows commute and
$$
 \Phi_{\mathcal Cg}^t=M^{-1}\Phi_g^tM,\qquad
 \Phi_f^t=\Phi_g^t\Phi_{\mathcal Cg}^{-t}.
$$
Consequently $M\Phi_f^t=\Phi_g^{-t}M\Phi_g^t$. This is an exact classical
identity for every finite $t$. A smooth symplectic conjugacy transports the
invariant hyperbolic splitting, with bounded derivatives in both directions,
so it preserves uniform hyperbolicity. It also transports area measure;
mixing follows from mixing of $M$. The latter can be checked on Fourier
characters: for nonzero integer $v$, $|T^nv|\to\infty$, and hence fixed
Fourier modes eventually have zero correlation. Density extends the result
to square-integrable observables.

The normalization of classical time is checked rather than presumed:
(7) gives
$$
 [\operatorname{Op}_N(g),\operatorname{Op}_N(a)]
 =-\frac{i}{2\pi N}\operatorname{Op}_N(\{g,a\})+O(N^{-3})
$$
for fixed smooth symbols. Differentiating unitary conjugation and using
Duhamel on a fixed compact time interval gives the pullback by
$\Phi_g^{\kappa/(2\pi)}$, with a remainder tending to zero. Thus (2) is a
quantization of the fixed map in (5).

For nonzero $g$ the smooth function $f$ is nonconstant. Its flow moves some
point for every sufficiently small nonzero time. The complement of the
support of $f$ has nonempty interior (the support occupies less than the
whole torus), and the flow is exactly the identity there. Accordingly
$M_\kappa$ equals $M$ on an open set but is not equal to it everywhere for
small nonzero $\kappa$. An affine torus map agreeing with $M$ on an open
set agrees everywhere. Therefore these fixed maps are genuinely nonlinear,
although smoothly conjugate to the same linear map.

# 4. Arithmetic multiplicities and individual cluster control

The following finite arithmetic facts can be established without primality
of $N$. Write $\alpha=1+\sqrt2$, $\lambda=\alpha^2$ and
$N+F\sqrt2=\alpha^K$ with $K$ an odd prime. The Pell identity gives
$N^2-2F^2=-1$, hence $F$ is invertible modulo $N$. Set
$$
 s=F^{-1}\pmod N,\quad s^2=2,\quad h=3+2s.
$$
Since $(1+s)^K=N+Fs=1$, $h^K=1$. Also $h-1=2(1+s)$ is a unit. Modulo
each prime divisor of $N$, the order of $h$ is exactly $K$. Thus $1-h^j$
is a unit for $1\leq j<K$, and $1+h^j$ is a unit for every $j$.

The symplectic matrix
$$
 P=\begin{pmatrix}1&-1/(2s)\\s&1/2\end{pmatrix}
$$
satisfies $T=P\operatorname{diag}(h,h^{-1})P^{-1}$. Its lower-left entry
is a unit, so its finite modular Weyl implementer has the same type of
quadratic kernel as (9) and preserves parity. Conjugating $S_h^{-1}$ by
this implementer constructs a phase-normalized $U_N$ with $U_N^K=I$.
Here $S_hu(x)=u(h^{-1}x)$. The unit conditions above show that every
nonzero residue has an orbit of length $K$, and that an orbit and its
negative are distinct. On the odd space, there are $n=(N-1)/(2K)$ cyclic
orbits, each contributing every $K$th root once. Hence the multiplicity is
exactly $n$ for each root. A different global phase merely rotates all
centres and changes none of the spacing conclusions.

Let $W=A_{\kappa,N}U_NA_{\kappa,N}^*$ on the odd space. Restriction cannot
increase (20). For large $N$ take $\delta_N<\sin(\pi/K)$. Spectral stability
for a normal matrix places each eigenvalue of $V$ within $\delta_N$ of a
$K$th root. To verify multiplicities, let $E=VW^*$ and use its principal
Hermitian logarithm, $E=e^{iH}$. Then
$\|H\|\leq2\arcsin(\delta_N/2)$, and the path $e^{iuH}W$, $0\leq u\leq1$,
stays within $\delta_N$ of $W$. The disjoint slightly enlarged root disks
have constant Riesz ranks along this path. Thus every disk contains exactly
$n$ eigenvalues. Their circle-coordinate halfwidth is bounded by
$$
 a_N=\pi^{-1}\arcsin(\delta_N/2)=O(N^{-\infty}).              \tag{22}
$$
This is an operator-norm, individual-cluster statement, unlike the earlier
normalized Hilbert--Schmidt comparison. It still makes no claim about
individual eigenvectors inside a nearly degenerate cluster.

# 5. Gaps, local counts, and robustness against unfolding

Sort the $D$ eigenangles cyclically, retaining multiplicities, and put
$S_l=D(\theta_{l+1}-\theta_l)$, with the cyclic final gap. Exactly $D-K$
gaps are within clusters and at most $2Da_N$. The other $K$ gaps are in
$[n-2Da_N,n+2Da_N]$. Matching these two classes to zeros and copies of $n$
proves (6). Since $1/n=K/D\to0$, the reference measures in (6) converge
weakly to $\delta_0$, and so do the actual gap measures. Their means are
nevertheless exactly one at each $N$: rare large gaps carry that mean.

Define the ordered close-pair count
$$
 R_N(x)=\frac1D\#\{(l,j):l\ne j,\ D\operatorname{dist}_{\mathbb T}
                         (\theta_l,\theta_j)\leq x\}.
$$
For fixed $x>0$, eventually $2Da_N<x$ and $D(1/K-2a_N)>x$. Every
within-cluster ordered pair is counted and no cross-cluster pair is counted.
Therefore
$$
 \boxed{R_N(x)=n-1\quad\hbox{eventually}.}                   \tag{23}
$$
For a fixed compactly supported continuously differentiable test $\phi$,
its periodized factorial statistic likewise obeys
$$
 \mathcal R_N(\phi)=(n-1)\phi(0)
       +O\bigl((n-1)Da_N\|\phi'\|_\infty\bigr).             \tag{24}
$$
The remainder is superpolynomially small. This formula is not asserted
with this rate for an arbitrary continuous test.

Choose an origin uniformly on the circle. A window of unfolded length $L$
can meet a cluster only if its origin belongs to one of $K$ arcs of length
at most $L/D+2a_N$. Hence
$$
 \mathbb P\{\hbox{window contains a level}\}
       \leq KL/D+2Ka_N\longrightarrow0.                     \tag{25}
$$
The same argument applies to any fixed compact observation window, giving
vague convergence in probability of the translated local point measures
to the empty measure. Their expected count is still $L$; uniform
integrability fails. This is a point-process statement, not an inference
from diverging second moments alone.

Now let $F_N:\mathbb R\to\mathbb R$ be increasing with
$F_N(x+1)=F_N(x)+1$ and Lipschitz constant at most $C N^A$. Image clusters
have angular diameter at most $2CN^Aa_N$. There are at most $K$ gaps not
internal to these clusters. Internal unfolded gaps tend uniformly to zero,
proving spacing collapse. All $n(n-1)$ ordered pairs in each original
cluster are still close, so $R_N(x)\geq n-1$ eventually. Finally (25) is
replaced by
$$
 \mathbb P\{\hbox{image window contains a level}\}
       \leq KL/D+2KCN^Aa_N\longrightarrow0.                 \tag{26}
$$
No lower bound on $F_N'$ is used, and image clusters need not remain
uniformly separated. Thus (23) need not remain an equality after unfolding;
the lower bound and empty-process conclusion are the correct statements.

# 6. Flat directions, hidden structure, and a falsification control

For every generator in (1), $\{g,\mathcal Cg\}=0$. In the previous smooth
notation, $\Gamma(g)=\sigma^2(\{g,\mathcal Cg\}/(4\pi))=0$. Thus the
second-order exceptional set contains an explicit infinite-dimensional
linear subspace containing nonzero smooth generators. This does not contradict
openness and density of $\Gamma>0$; an infinite-dimensional exceptional
subspace can still have empty interior. Subtracting the mean of $g$ places
it in the zero-mean class without changing $f$, $\Gamma$, or the quantum
commutator. One should apply the support argument to the original bump,
not falsely describe its mean-subtracted version as compactly supported.

Poisson commutation **alone** is insufficient for (3). For a negative
control take $a=b_{(1,0)}+b_{(0,1)}$, where $b_v=2\cos(2\pi v\cdot x)$,
and $b=a^2$. Of course $\{a,b\}=0$. Yet the cubic Weyl coefficient
$$
 \sum_{v+w=k}\widehat a(v)\widehat b(w)\omega(v,w)^3
$$
is nonzero: at frequencies $(-2,-1),(-2,1),(-1,-2),(-1,2)$ its values are
$-6,6,6,-6$, respectively, and the four opposite frequencies give the
same values. The commutator therefore has a nonzero term of order $N^{-3}$.
For a sufficiently large odd $N$ these finite frequencies are distinct
modulo $N$, so this is not a formal nonzero coefficient that disappears
under quantization. Both implementations retain this negative control.
The all-orders cancellation in (11), not just its first term, is essential.

Finally, if $J_N$ commutes with $U_N$ and $\|J_N\|\leq1$, then
$$
 \|[V_{\kappa,N},A_{\kappa,N}J_NA_{\kappa,N}^*]\|
        \leq2\delta_N.                                    \tag{27}
$$
The arithmetic commutant is therefore transported to an all-orders
approximate commutant. These systems do not evade arithmetic structure by
being nonlinear. We do not claim their complete symmetry reduction, simple
spectrum, or generic random-matrix behaviour. Obtaining corresponding
positive universality for fixed maps not conjugate to arithmetic models
is not accomplished by this construction.

# 7. Verification contract and prior work

The proof uses standard Fourier/Weyl calculus, a standard Duhamel product
estimate, and ordinary spectral perturbation theory. The finite comparison
and its application to this explicit smooth family are the project result;
no first-ever or prize-level status is inferred.

The independent Python verifier uses physical Weyl matrices and an alias-aware
separable-symbol assembly. A two-dimensional Fourier construction checks it
separately, and quadrature checks selected Fourier coefficients. It computes
the actual single-exponential propagator, not a spectrum substituted from
the conjugated reference. Fourier refinement is a numerical diagnostic,
not an interval-certified tail or rounding bound. The C++ verifier instead
uses exact integer frequency convolution and integer circle-cluster counts.
The Lean module contains universal scaled support inequalities and finite
integer facts only. Its status requires an actual compiler run; it does not
formalize Theorems A--C.

The full research log records failed low-cutoff comparisons and a timed-out
larger dense run. Finite small-$N$ errors are not fitted to prove an
asymptotic exponent. The source-hashed execution manifest specifies which
commands actually ran. The linked article and figures are generated from
those data, not from selected successful-looking points.

Relevant primary records are M. Hitrik, R. Lascar, J. Sjoestrand and M. Zerzeri,
*Semiclassical Gevrey operators in the complex domain*, Ann. Inst. Fourier
73 (2023), 1269--1318, DOI 10.5802/aif.3546, arXiv:2009.09125; T. Prosen and
M. Znidaric, *Quantum Freeze of Fidelity Decay for Chaotic Dynamics*, Phys.
Rev. Lett. 94 (2005), 044101, arXiv:quant-ph/0401142; and J. P. Keating and
F. Mezzadri, *Pseudo-symmetries of Anosov maps and spectral statistics*,
Nonlinearity 13 (2000), 747--775, DOI 10.1088/0951-7715/13/3/313.
The first paper explicitly discusses factorial $(r!)^{2s-1}$ Weyl remainders;
this is precedent for the nonoptimal truncation exponent, not a novelty
claim. Residual/coboundary perturbations are direct prior physics. The last
paper's bibliographic record is verified, but its full text was not obtained
in this pass, so no assertion that it lacks this particular construction is
made. A prior title-based retrieval returned an unrelated cellular-billiard
paper and was rejected. The source audit records these limits explicitly.
