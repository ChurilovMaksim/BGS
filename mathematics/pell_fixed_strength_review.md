---
title: "Review and verification of the fixed-strength flat-kick branch"
author: "BGS research programme"
date: "5 September 2026"
---

# What is proved on this branch

The all-orders construction in `pell_all_orders_conjugacy.md` had been stored
as Git tree content without a reachable main-branch commit. This review records
its mathematical argument independently, executes checks of the natural
single-exponential quantization, and distinguishes this exceptional family
from the positive BGS target.

The result concerns **fixed nonzero classical strength**, not merely a quantum
exponent whose corresponding classical strength vanishes. It also controls all
polynomial times in the inverse Planck parameter. These assertions hold because
the map is smoothly symplectically conjugate to an arithmetic cat map; that
exceptional structure must remain part of every statement of the result.

# 1. Fixed symbol, fixed classical strength

Set
$$
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad S=T^{\mathsf T},
 \qquad \hbar_N=(2\pi N)^{-1},
$$
and use the physical integer Weyl convention
$$
 Q_N(a,b)=(-1)^{ab}W_N(a,b),\quad
 W_N(a,b)u(x)=e_N(a(x-b/2))u(x-b).
$$
The division by two in W is modular; a,b in Q are integer Fourier indices.
One checks exactly that
$$
 Q_N(v)Q_N(w)=e^{\pi i\det(v,w)/N}Q_N(v+w).
$$
Let $U_N$ be a unitary quantization satisfying
$U_N\operatorname{Op}_N(a)U_N^*=\operatorname{Op}_N(a\circ S)$. An explicit
kernel, up to a global phase, is
$$
 U_N(x,y)=N^{-1/2}e_N((3x^2-2xy+3y^2)/8).
$$
The reciprocal of 8 exists for every odd N. Summing a nontrivial linear
character proves unitarity; checking multiplication and translation generators
proves the exact Weyl covariance. Since T is the identity modulo 2, it also
preserves the physical Fourier sign. This point would fail under a careless
omission of $(-1)^{ab}$.

Take a real even smooth nonzero $g_0$ such that
$$
       \operatorname{supp}g_0\cap S^{-1}\operatorname{supp}g_0
                        =\varnothing.                       \tag{F1}
$$
Put $g=g_0-\int g_0$, $d=g\circ S$, and $f=g-d$. Write $A_N=\operatorname{Op}_N(g)$,
$D_N=U_NA_NU_N^*$; in this section $D_N$ denotes an operator, not a dimension.
For a fixed classical strength $\kappa$ define
$$
 V_{\kappa,N}=\exp(i\kappa(A_N-D_N)/\hbar_N)U_N,
 \qquad J_{\kappa,N}=\exp(i\kappa A_N/\hbar_N).
$$
This is one exponential of the fixed symbol f. It has not been defined by
editing eigenvalues or by replacing it with an exactly conjugated operator.

**Theorem F.** For every B,p,L>0,
$$
 \boxed{\displaystyle
 \sup_{|\kappa|\leq B,\ |t|\leq N^p}
 \|J_{\kappa,N}^*V_{\kappa,N}^{t}J_{\kappa,N}-U_N^t\|_{\rm op}
                            =O_{g,B,p,L}(N^{-L}).}            \tag{F2}
$$
The time t is integer and may depend on N. The result is valid on the full
space and on both parity spaces. It asserts arbitrary inverse-power accuracy,
not equality at finite N and not one estimate uniform in the requested order L.

# 2. The all-orders estimate is a finite-remainder argument

Define $M_j(a)=\sum_v|\widehat a(v)|\,|v|^j$. For fixed smooth functions these
numbers are finite at every integer j. The exact commutator is
$$
 [A_N,D_N]=2i\sum_{v,w}\widehat g(v)\widehat d(w)
                 \sin(\pi\det(v,w)/N)Q_N(v+w).
$$
For every positive integer j, the symbol whose Fourier coefficient convolution
contains $\det(v,w)^j$ is a constant multiple of
$$
 \sum_{l=0}^j(-1)^l\binom jl
 (\partial_q^{j-l}\partial_p^l g)
 (\partial_q^l\partial_p^{j-l} d).
$$
Every summand vanishes pointwise by (F1); mean subtraction does not change any
positive-order derivative. Thus every polynomial term of the sine expansion
vanishes after the Fourier summation. Absolute weighted Fourier convergence
justifies that step even in the presence of modular aliases.

For an odd j, Taylor's finite remainder for the real sine function gives
$$
       \|[A_N,D_N]\|_{\rm op}
       \leq\frac{2\pi^j}{j!N^j}M_j(g)M_j(d).                 \tag{F3}
$$
There is no assumption that an infinite Moyal expansion converges. For each
requested power a finite j is selected.

For finite Hermitian A,D and real e, unitary Duhamel integration gives
$$
 \|e^{ie(A-D)}-e^{ieA}e^{-ieD}\|\leq\tfrac12 e^2\|[A,D]\|.
$$
This inequality is valid even when $|e|\|A\|$ is large. With $e=2\pi N\kappa$,
$$
 \delta_N:=\|J_{\kappa,N}^*V_{\kappa,N}J_{\kappa,N}-U_N\|_{\rm op}
 \leq\frac{4\kappa^2\pi^{j+2}}{j!}M_j(g)M_j(d)N^{2-j}.     \tag{F4}
$$
Taking j as large as needed, followed by
$\|V'^t-U^t\|\leq |t|\|V'-U\|$, proves (F2), including negative times by
adjoints. The argument uses operator norm rather than a normalized trace norm.

# 3. Exact classical geometry and an explicit bump

Let $\Phi_a^s$ be the Hamiltonian flow of $(a_p,-a_q)$. Since g and d have
disjoint derivative supports, $\{g,d\}=0$ and the flows commute. Also
$\Phi_d^s=S^{-1}\Phi_g^sS$. It follows exactly that
$$
 F_\kappa:=S\Phi_f^{-\kappa}
                  =\Phi_g^\kappa S\Phi_g^{-\kappa}.          \tag{F5}
$$
With the above Weyl sign, adjoint conjugation by $e^{i\kappa\operatorname{Op}(f)/\hbar}$
quantizes pullback by $\Phi_f^{-\kappa}$. This also follows by differentiating
and using $[\operatorname{Op}(f),\operatorname{Op}(a)]=-i\hbar\operatorname{Op}(\{f,a\})+O(\hbar^3)$.
The signs and order in (F5) agree with the quantum conjugation.

Smooth conjugacy transports the stable and unstable bundles of S, with bounded
changes in their norms on the compact torus. Hence $F_\kappa$ is Anosov for
every finite kappa. This uses smooth symplectic conjugacy, not the much weaker
topological conjugacy supplied for general small Anosov perturbations.

For an explicit example let $r=1/16$ and
$$
 \eta(t)=\begin{cases}\exp(1-(1-t^2)^{-1}),&|t|<1,\\0,&|t|\geq1,\end{cases}
 \quad b_r(x)=\sum_{n\in\mathbb Z}\eta((x-n)/r),
$$
$$
 \ell(q)=b_r(q-1/4)+b_r(q+1/4),\qquad g_0(q,p)=\ell(q)b_r(p).
$$
The two support boxes have centres $(1/4,0),(3/4,0)$ and halfwidth r. A point
in either box has a lift $q=(2j+1)/4+u,p=v$, $|u|,|v|\leq r$. The second
coordinate of Sx modulo an integer lies in
$$
           \tfrac12+2u+3v\in[3/16,13/16],
$$
outside the interval of distance at most $1/16$ from the integers. This proves
(F1) with exact gap $1/8$. Any real even smooth function supported inside the
boxes has the same property, so the construction is infinite-dimensional.

For this nonzero bump $F_\kappa$ is not affine when $\kappa\ne0$. It agrees with
S on an open set, so if affine it must equal S everywhere. That would force
$\Phi_f^\kappa=I$. A nonconstant compactly supported Hamiltonian on this torus
cannot have a nonzero global flow period: averaging a Riemannian metric over
that period would make every flow map an isometry fixing an open set, hence
the identity on the connected manifold. This would make f constant, a
contradiction. The maps are genuinely nonlinear, but retain conjugated
arithmetic structure.

# 4. Microscopic spectrum and Heisenberg times

For odd prime K put $N+F\sqrt2=(1+\sqrt2)^K$ and write
$$
                  d_N=(N-1)/2,\qquad n_N=d_N/K.
$$
Here $d_N$ is now the odd-space dimension. The standard Pell dilation
calculation gives each K-th root of unity multiplicity $n_N$ on that space,
after one scalar phase normalization. It does not require N prime: putting
$s=F^{-1}\bmod N$, $h=3+2s$, every prime divisor of N sees h of order K;
therefore $1-h^j$ is a unit for $0<j<K$ and $1+h^j$ is a unit for all j.
Every nonzero residue lies in a free K-cycle, disjoint from its negative.
The odd dilation representation is a sum of $n_N$ regular K-cycles. A finite
symplectic Weyl change of coordinates relates this dilation to $U_N$.

For completeness, $F^{-2}=2\pmod N$, $(1+s)^K=1\pmod N$, and
$h-1=2(1+s)$ is a unit. The primality of K then proves the order assertion
modulo each prime divisor of N, including repeated factors of N through the
unit criterion. These are the arithmetic hypotheses behind the multiplicity
statement, not a numerical observation about a few prime moduli.

Once $\delta_N<\sin(\pi/K)$, the delta-discs around the roots are disjoint.
The resolvent estimate for the normal matrix $U_N$ and a linear homotopy to
$J^*VJ$ show that the Riesz rank inside each disc is constant, equal to $n_N$.
The eigenphase distance in turns is at most
$\eta_N=\pi^{-1}\arcsin(\delta_N/2)$, smaller than every inverse power of N.
It follows that the full odd spectrum has exactly K clusters of rank $n_N$,
not just that most eigenvalues are close in average squared distance.

Let $s_l=d_N(x_{l+1}-x_l)$ be the cyclically ordered unfolded spacings. All
but K gaps are at most $2d_N\eta_N$ and $K/d_N\to0$, so their empirical measure
tends weakly to $\delta_0$. For every fixed x>0, the normalized number of
ordered distinct pairs at circular distance at most $x/d_N$ is eventually
exactly $n_N-1$. Between clusters the distance is at least $n_N-o(1)$ in
mean spacings; inside a cluster it tends to zero.

For every fixed Schwartz test phi the complete periodized pair statistic obeys
$$
 \frac1{d_N}\sum_{l\ne j}\sum_{z\in\mathbb Z}
       \phi(d_N(x_l-x_j+z))=(n_N-1)\phi(0)+o(1).             \tag{F6}
$$
The intracluster error is bounded by
$2n_Nd_N\eta_N\|\phi'\|_\infty=o(1)$. Intercluster contributions and nonzero
windings are bounded by a convergent Schwartz tail of the form
$C_s n_N\sum_{k\ne0}(1+n_N|k|/2)^{-s}=o(1)$, $s>2$.
This proves (F6) also for signed tests. The mean spacing stays one; rare large
intercluster gaps prevent convergence of first moments.

For the conventional map form factor $\mathcal K_N(t)=d_N^{-1}|\operatorname{Tr}_-V^t|^2$,
(F2) gives, for every p,L>0,
$$
 \sup_{|t|\leq N^p}\left|\mathcal K_N(t)-d_N\mathbf1_{K\mid t}\right|
                          =O(N^{-L}).                       \tag{F7}
$$
The extra factor $d_N$ in this normalization is absorbed by choosing a higher
order in (F4), not omitted. For fixed $0<a<b$, its average over integer times
in $[ad_N,bd_N]$ equals $n_N(1+o(1))\to\infty$. This controls an entire
Heisenberg-size window, not a single selected resonance.

# 5. What the independent numerical test actually checks

Half-periodicity of ell gives an exact nodal formula for the smooth operator:
$$
 [\operatorname{Op}_N(g_0)]_{xy}
 =\ell((x+y)/(2N))\frac1N\sum_{z=0}^{N-1}
                         b_r(z/N)e^{-2\pi i(x-y)z/N}.        \tag{F8}
$$
One proves this by grouping the Fourier index in the p-variable modulo N.
The induced shift by a half-integer in the q-argument disappears only because
ell has period $1/2$. The verifier tests (F8) against direct physical Weyl
sums on finite symbols including aliases. A negative control without that
half-periodicity fails by an operator norm greater than 1.9, as it should.
There is no unrecorded Fourier cutoff of the bump.

The matrices are evaluated in floating point. Tests check Hermiticity,
unitarity, parity, Weyl covariance, two different exponential implementations,
classical flow composition, Pell odd-sector cluster ranks, and the finite
unitary telescope bound at times comparable to the odd dimension. These are
finite falsification tests, not proofs of (F2) or of an asymptotic rate.
All small-N deviations and a timed-out attempted N=2047 batch are recorded;
no failed or uncompleted batch is labelled successful.

# Scientific boundary

This construction supplies a fixed-strength, fixed-symbol nonlinear Anosov
family with all-orders spectral control. It does not supply positive BGS for
a generic nonlinear perturbation. If H commutes with the arithmetic U, then
$JHJ^*$ commutes with V up to $2\|H\|\delta_N$; the hidden arithmetic
commutants persist at all inverse-power accuracies. Nonlinearity by itself is
not a criterion excluding this structure.

Nonlinear cat-map spectral anomalies and pseudo-symmetries predate this project:
Keating--Mezzadri, *Nonlinearity* 13 (2000), 747--775,
[DOI:10.1088/0951-7715/13/3/313](https://doi.org/10.1088/0951-7715/13/3/313).
The present review does not establish priority for the exact special
single-exponential construction. It also does not reduce the positive BGS
problem to one of the Gaussian observable laws from earlier notes.
