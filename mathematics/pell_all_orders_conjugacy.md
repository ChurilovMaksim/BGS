---
title: "Fixed-strength nonlinear cat maps with all-orders quantum conjugacy"
author: "WoW research programme"
date: "5 September 2026"
---

# Abstract and scope

We construct an infinite-dimensional family of nonzero smooth coboundary kicks
of a fixed hyperbolic toral automorphism. For fixed nonzero classical strength,
the natural single-exponential quantization is conjugate to the arithmetic cat
map modulo every inverse power of the Hilbert-space parameter, in operator
norm. The comparison holds on every polynomial time interval, including the
Heisenberg scale. Along the prime-period Pell sequence it yields exact cluster
ranks, a complete asymptotic Schwartz pair statistic, and the form factor on
all those times. An exact nodal formula implements the smooth operator without
a Fourier cutoff.

The classical maps are nonaffine Anosov maps but retain arithmetic structure
through smooth symplectic conjugacy. This is a special nonanalytic family, not
a theorem of generic BGS universality. Microlocal locality, unitary product
bounds and residual-perturbation cancellation are established principles. The
proof and finite checks below establish results within this project; world
priority and external referee acceptance are not claimed.

# 1. Conventions and theorem

Let
\[
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
 S=T^{\mathsf T}=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
 \hbar_N=(2\pi N)^{-1}.
\]
The distinction is intentional: T acts on Fourier covectors and S acts in the
pullback of phase-space observables. For an odd integer N let
\[
 W_N(a,b)u(x)=e_N(a(x-b/2))u(x-b),\qquad
 Q_N(a,b)=(-1)^{ab}W_N(a,b),\qquad
 e_N(t)=e^{2\pi it/N}.
\]
Division by two inside W is modular; the arguments of Q are integer vectors
before reduction. Exact multiplication gives
\[
 Q_N(v)Q_N(w)=e^{\pi i\omega(v,w)/N}Q_N(v+w),\quad
 Q_N(v)^*=Q_N(-v),\quad
 \omega(v,w)=v_1w_2-v_2w_1.                         \tag{1}
\]
For a smooth periodic symbol a put
\(\operatorname{Op}_N(a)=\sum_v\widehat a(v)Q_N(v)\).
The series converges in operator norm, bounded by its Fourier l1 norm.

Choose a unitary cat quantization U_N with
\[
 U_N\operatorname{Op}_N(a)U_N^*
       =\operatorname{Op}_N(a\circ S).                       \tag{2}
\]
For example, up to a global phase its position kernel is
\[
 U_N(x,y)=N^{-1/2}e_N((3x^2-2xy+3y^2)/8).                   \tag{3}
\]
Here 8 is invertible modulo N. Unitarity follows by summing the nontrivial
linear character in a matrix element of UU*. Testing the two Weyl generators
verifies covariance T. Since T is the identity modulo 2, the sign correction
in Q is preserved by T, so (2) holds for the physical integer Fourier modes,
not just the centered finite Weyl operators.

Let g_0 be a real even smooth function with
\[
 \operatorname{supp}g_0\ \cap\ S^{-1}(\operatorname{supp}g_0)
       =\varnothing.                                       \tag{4}
\]
Set \(g=g_0-\int g_0\), \(d=g\circ S\), and \(f=g-d\).
The subtraction of the constant is irrelevant to commutators and to f.
Define the natural, single-exponential kicked propagator and the gauge
\[
 V_{\kappa,N}=e^{i\kappa\operatorname{Op}_N(f)/\hbar_N}U_N,
 \qquad J_{\kappa,N}=e^{i\kappa\operatorname{Op}_N(g)/\hbar_N}.
                                                               \tag{5}
\]
In particular kappa, not its quantum exponent \(\kappa/\hbar_N\), is the
classical perturbation strength.

**Theorem 1 (all-orders fixed-strength conjugacy).** For every B>0 and every
A>0 there is a finite constant C depending on g, A and B, but not N, such that
\[
 \sup_{|\kappa|\leq B}
 \|J_{\kappa,N}^*V_{\kappa,N}J_{\kappa,N}-U_N\|_{\rm op}
       \leq C N^{-A}.                                      \tag{6}
\]
The estimate is on the full N-dimensional space and also on either parity
space. For every p,A>0 it implies
\[
 \sup_{|\kappa|\leq B,\ |t|\leq N^p}
 \|J_{\kappa,N}^*V_{\kappa,N}^{t}J_{\kappa,N}-U_N^t\|_{\rm op}
       =O_{g,A,B,p}(N^{-A}).                                \tag{7}
\]
The integer time t may depend on N. There is no shrinking-kappa assumption.
Neither (6) nor (7) asserts equality at finite N.

Write \(\Phi_a^t\) for the Hamiltonian flow of
\(X_a=(\partial_2a,-\partial_1a)\), and use the stated Poisson convention
\(\{a,b\}=\partial_1a\partial_2b-\partial_2a\partial_1b\).
The associated classical map, in the adjoint convention (2), is
\[
 F_\kappa=S\circ\Phi_f^{-\kappa}
       =\Phi_g^{\kappa}\circ S\circ\Phi_g^{-\kappa}.          \tag{8}
\]
It is a fixed smooth symplectic Anosov map for each fixed kappa. For the
explicit nonzero bump of Section 2 it is nonaffine for every kappa not equal
to zero. Thus (6) is not merely a statement about a vanishing classical kick.

# 2. An explicit infinite-dimensional flat branch

Let \(r=1/16\) and define the normalized smooth bump
\[
 \eta(t)=\begin{cases}
  \exp(1-(1-t^2)^{-1}),&|t|<1,\\0,&|t|\geq1,
 \end{cases}\qquad
 b_r(x)=\sum_{n\in\mathbb Z}\eta((x-n)/r).
\]
Put
\[
 \ell(q)=b_r(q-1/4)+b_r(q+1/4),\qquad
 g_0(q,p)=\ell(q)b_r(p).                                    \tag{9}
\]
This is real, even, nonzero, smooth and periodic; ell has period 1/2.
Its support consists of two closed boxes of halfwidth r centered at
\((1/4,0)\) and \((3/4,0)\), with the torus seam understood periodically.

For a point in either box, choose a lift
\(q=(2j+1)/4+u\), \(p=v\), with \(|u|,|v|\leq r\).
The second coordinate of S(q,p), modulo an integer, is
\[
 \frac12+2u+3v\in[3/16,13/16].                              \tag{10}
\]
Its distance from the integers is at least 3/16, greater than r. Hence it
cannot be in either box. The support separation is exact, not a sampled
observation. The gap beyond the permitted halfwidth is 1/8.

More generally any real even smooth function supported in the interiors of
these boxes satisfies (4). Such functions form an infinite-dimensional
linear space. After subtracting their means, every member obeys
\[
 \{g,g\circ S\}=0,
 \qquad \Gamma(g):=\sigma^2(\{g,g\circ S\}/(4\pi))=0.         \tag{11}
\]
In fact all the mixed local bidifferential expressions used in the Weyl
commutator expansion vanish. The map \(g_0\mapsto g_0-g_0\circ S\) is
injective on this space: disjoint support makes equality to zero impossible
unless g_0 is zero. Thus these are nonzero perturbations, not constants in
disguise. An open dense positive set of Gamma in the full smooth space, as
in the earlier project theorem, is compatible with this infinite-dimensional
zero subspace. Generic nondegeneracy does not mean universal nondegeneracy.

## Exact classical conjugacy and nonlinearity

The vector fields of g and d have disjoint supports, so their bracket is
zero and their complete flows commute. The symplectic change of variables S
satisfies \(\Phi_d^t=S^{-1}\Phi_g^tS\). Therefore
\[
 S\Phi_f^{-\kappa}
 =S\Phi_d^\kappa\Phi_g^{-\kappa}
 =\Phi_g^\kappa S\Phi_g^{-\kappa},
\]
which proves (8). The stable and unstable bundles are the pushforwards of
those of S by \(\Phi_g^\kappa\); their contraction estimates follow from
the bounded derivatives of this diffeomorphism and its inverse on the compact
torus. This proves the Anosov assertion for every finite kappa without a
small-perturbation structural-stability argument.

For completeness, a nonconstant smooth Hamiltonian f whose vector field
vanishes on a nonempty open set cannot have a nonzero global flow period.
If \(\Phi_f^a=I\) for a>0, average any Riemannian metric over that period.
Every \(\Phi_f^t\) becomes an isometry fixing the same nonempty open set.
An isometry of a connected complete manifold fixing an open set is the
identity: at an interior point it fixes the point and its differential, and
then every geodesic issuing from that point. Thus all these flows would be
identity and f constant, a contradiction. For (9), f is nonconstant and
vanishes outside a proper compact subset of the torus. Consequently
\(F_\kappa\ne S\) for every nonzero kappa. It agrees with S on an open set,
so it cannot be any other affine torus map either. This proves nonlinearity.

# 3. An elementary all-orders Fourier estimate

For an integer j>=1 define the finite seminorm
\[
 M_j(a)=\sum_{v\in\mathbb Z^2}|\widehat a(v)|\,|v|_2^j.
\]
Smoothness ensures its finiteness for every j. For two functions a,b define
\[
 P_j(a,b)=\sum_{l=0}^j(-1)^l\binom jl
 (\partial_1^{j-l}\partial_2^l a)
 (\partial_1^l\partial_2^{j-l} b).
\]
Its Fourier coefficient formula is, with absolute convergence,
\[
 P_j(a,b)(x)=(2\pi i)^{2j}
       \sum_{v,w}\omega(v,w)^j\widehat a(v)\widehat b(w)e_{v+w}(x).
                                                               \tag{12}
\]
If a=g and b=d, each product of derivatives is zero by (4); subtracting the
mean does not affect positive-order derivatives. Hence \(P_j(g,d)=0\) for
all j>=1. Applying the linear quantization map to (12) gives an exactly
zero finite matrix, regardless of modular aliasing.

From (1) one obtains the exact commutator formula
\[
 [\operatorname{Op}_N(g),\operatorname{Op}_N(d)]
  =2i\sum_{v,w}\widehat g(v)\widehat d(w)
               \sin(\pi\omega(v,w)/N)Q_N(v+w).
\]
For any positive odd integer j, expand sine only through degree j-2.
Every displayed polynomial term vanishes by (12). The real Taylor
remainder is at most \(|z|^j/j!\) for every real z, not merely small z.
Using \(|\omega(v,w)|\leq|v|_2|w|_2\) and unitarity of Q yields
\[
 \boxed{\displaystyle
 \|[\operatorname{Op}_N(g),\operatorname{Op}_N(d)]\|_{\rm op}
 \leq \frac{2\pi^j}{j!N^j}\,M_j(g)M_j(d),\qquad j\text{ odd}.}
                                                               \tag{13}
\]
This proves the all-orders estimate by a finite Taylor remainder for each
chosen order. It does not assume convergence of an infinite Moyal series.
The constants may grow with j. Formula (13) is a direct torus version of
standard microlocal locality, not a claim to originate that principle.

# 4. Fixed strength and the quantum gauge

For bounded Hermitian A,B and real e, the standard product inequality in
operator norm (or any unitarily invariant norm) is
\[
 \|e^{ieA}e^{ieB}-e^{ie(A+B)}\|
       \leq\tfrac12e^2\|[A,B]\|.                            \tag{14}
\]
A proof differentiates
\(e^{i(e-t)(A+B)}e^{itA}e^{itB}\) and bounds the conjugation difference
\(e^{itA}Be^{-itA}-B\) by \(|t|\|[A,B]\|\); integrating a triangle gives
(14). There is no assumption \(|e|\|A\|<1\).

Take \(A=\operatorname{Op}_N(g)\), \(D=U_NAU_N^*\) and
\(e=\kappa/\hbar_N=2\pi N\kappa\). The exact covariance (2) identifies
D with \(\operatorname{Op}_N(d)\). Multiplication by unitaries reduces the
conjugacy error to
\[
 \|e^{-ieA}e^{ie(A-D)}e^{ieD}-I\|
 \leq\tfrac12e^2\|[A,D]\|.
\]
For every odd j this gives the explicit finite inequality
\[
 \boxed{\displaystyle
 \delta_N(\kappa):=
 \|J_{\kappa,N}^*V_{\kappa,N}J_{\kappa,N}-U_N\|_{\rm op}
 \leq\frac{4\kappa^2\pi^{j+2}}{j!}\,M_j(g)M_j(d)N^{2-j}.}
                                                               \tag{15}
\]
Choosing j arbitrarily large proves (6). Telescoping integer powers of
unitaries gives \(\|V'^t-U_N^t\|\leq|t|\delta_N\), with adjoints for
negative t; choosing a larger j proves (7). This is the step which crosses
the earlier logarithmic-time barrier on this special branch.

The classical interpretation is also controlled. With the present Weyl sign,
\([\operatorname{Op}_N(a),\operatorname{Op}_N(b)]
=-i\hbar_N\operatorname{Op}_N(\{a,b\})+O(\hbar_N^3)\).
Differentiate conjugation by \(e^{it\operatorname{Op}_N(a)/\hbar_N}\),
compare to pullback by \(\Phi_a^{-t}\), and integrate the cubic commutator
remainder. For bounded classical time and a fixed smooth test symbol b this
proves an \(O(\hbar_N^2)\) Egorov error. Combined with (2) it assigns
precisely the map \(S\Phi_f^{-\kappa}\) to (5). The family is therefore a
standard local Weyl kick with fixed symbol; it was not defined by replacing
or editing individual eigenvalues.

# 5. Spectral conclusions along the Pell sequence

Let K tend through odd primes and put
\[
 N+F\sqrt2=(1+\sqrt2)^K,\qquad D_N=(N-1)/2,\qquad n_N=D_N/K.
\]
Here N may be composite. The phase of U_N can be chosen so that on its odd
space each K-th root of unity occurs with multiplicity exactly n_N.
Here is the arithmetic verification, independent of any Gaussian limit.
The Pell norm gives \(F^{-2}=2\pmod N\). Set \(s=F^{-1}\) and
\(h=3+2s\). The identity \((1+s)^K=1\pmod N\) gives \(h^K=1\).
The element \(h-1=2(1+s)\) is a unit. Modulo every prime dividing N, the
order of h is consequently K, since K is prime. Thus \(1-h^j\) is a unit
for \(0<j<K\); \(1+h^j\) is a unit as K is odd. Every nonzero residue has
a K-cycle under multiplication by h, and no cycle meets its negative.
The odd space is therefore a direct sum of n_N regular K-cycles. A finite
symplectic change of coordinates conjugates U_N to this dilation, up to a
scalar phase. Its covariance has eigenvectors (1,s) and (1,-s), with
invertible determinant -2s; the corresponding centered Weyl changes can be
implemented by chirps, a Fourier transform and a unit dilation. For example
\[
 M=\begin{pmatrix}-1/(2s)&1\\-1/2&-s\end{pmatrix},\qquad
 \det M=1,\qquad T=M\operatorname{diag}(h,h^{-1})M^{-1}.
\]
Define \(C_tu(x)=e_N(tx^2/2)u(x)\), \(S_bu(x)=u(b^{-1}x)\),
and let the discrete Fourier kernel be \(e_N(xy)/\sqrt N\).
The product \(C_{s^{-1}}S_{1/2}\mathcal F_N C_{2s}\) implements M.
Covariance of these four factors is verified directly on W. All factors
preserve parity. By irreducibility of the multiplication/translation Weyl
pair, any two unitaries with the same covariance differ by a scalar.
Consequently this constructed metaplectic representative and (3) differ
only by a phase, which is the phase normalized above. This also shows that \(n_N\) is an integer.

**Theorem 2 (microscopic clustering and all polynomial times).** For the
fixed-strength family (5), every fixed nonzero kappa has the following
properties on the odd space along the Pell sequence.

(a) For all sufficiently large N, the spectrum lies in K disjoint arcs, each
containing exactly n_N eigenvalues with multiplicities and having angular
width \(O_A(N^{-A})\) for every A.

(b) Let \(x_l\in\mathbb R/\mathbb Z\) be cyclically ordered eigenphases and
\(s_l=D_N(x_{l+1}-x_l)\), including the last circular gap. Then
\[
 \frac1{D_N}\sum_l\delta_{s_l}\ \Longrightarrow\ \delta_0.
                                                               \tag{16}
\]
For every fixed x>0 the normalized number of ordered distinct close pairs
satisfies, eventually,
\[
 \frac1{D_N}\#\{(l,j):l\ne j,\ D_N\operatorname{dist}(x_l,x_j)\leq x\}
       =n_N-1\ \longrightarrow\infty.                       \tag{17}
\]
The equality, not just a lower bound, holds eventually: distinct clusters
are separated by \(n_N+o(1)\) mean spacings.

(c) For every fixed Schwartz function phi, the complete pair statistic
\[
 R_N(\phi)=\frac1{D_N}\sum_{l\ne j}\sum_{z\in\mathbb Z}
                         \phi(D_N(x_l-x_j+z))
\]
obeys
\[
 R_N(\phi)=(n_N-1)\phi(0)+o(1).                             \tag{18}
\]
Thus \(n_N^{-1}R_N\) tends distributionally to the point mass at zero,
not a random-matrix pair kernel.

(d) With the standard map form-factor normalization
\(\mathcal K_N(t)=D_N^{-1}|\operatorname{Tr}_{-}V_{\kappa,N}^t|^2\),
for every p,A>0,
\[
 \sup_{|t|\leq N^p}
 |\mathcal K_N(t)-D_N\mathbf1_{K\mid t}|=O(N^{-A}).           \tag{19}
\]
In particular this holds at and beyond the Heisenberg time \(t\asymp D_N\).
For fixed \(0<a<b\), averaging over all integers in \([aD_N,bD_N]\) gives
\[
 \frac1{\#I_N}\sum_{t\in I_N}\mathcal K_N(t)
       =n_N(1+o(1))\ \longrightarrow\infty.                 \tag{20}
\]
The assertion does not depend on selecting just one narrow resonance peak.

**Proof.** Let delta be the error (15). The resolvent norm of the normal
matrix U_N outside its spectrum is the reciprocal distance to that spectrum.
The homotopy \(U_N+s(V'-U_N)\), \(0\leq s\leq1\), has no eigenvalues
outside the union of closed delta-discs around the roots. For
\(\delta<\sin(\pi/K)\) the discs are disjoint; a contour around each has
constant Riesz rank n_N throughout this homotopy. The endpoint V' is unitary,
so its eigenphases have distance at most
\(\eta_N=\pi^{-1}\arcsin(\delta/2)\) from the root lattice in turns.
Both delta and eta are \(O(N^{-A})\) for all A. This proves (a).

All but K adjacent gaps are within clusters and at most \(2D_N\eta_N\).
The fraction K/D_N tends to zero. Distinct clusters are at least
\(D_N/K-2D_N\eta_N=n_N-o(1)\) apart. Counting ordered pairs within the
clusters gives exactly \(K n_N(n_N-1)/D_N=n_N-1\), proving (b).
The mean gap is still exactly one; weak convergence in (16) is not convergence
of the first moment. Rare intercluster gaps carry it.

For (c), the intracluster contribution differs from \((n_N-1)\phi(0)\)
by at most \(2n_ND_N\eta_N\|\phi'\|_\infty=o(1)\). In the periodized
intercluster sum the possible ideal separations are nonzero integer multiples
of n_N. Per eigenvalue and per such multiple there are n_N terms. For any
s>2, Schwartz decay bounds their normalized sum by
\(C_s n_N\sum_{l\ne0}(1+n_N|l|/2)^{-s}=O(n_N^{1-s})\).
The nonzero windings of intracluster pairs satisfy the same type of bound.
This proves (18), including signed tests.

For (d), (7) controls the normalized trace error uniformly by a quantity e_N
that is smaller than every inverse power of N. If K divides t the normalized
unperturbed trace is 1; otherwise it is zero. For complex numbers of modulus
at most one, the difference of their absolute squares is at most twice their
difference. Hence the form-factor error is at most \(2D_N e_N\), still of
arbitrary inverse-power order. Finally the number of multiples of K in I_N
is \(\#I_N/K+O(1)\); dividing by \(\#I_N\asymp D_N\) proves (20).
End of proof.

A further check identifies the symmetry mechanism. If a norm-bounded matrix
H_N commutes with U_N, then its transported version
\(\widetilde H_N=J_{\kappa,N}H_NJ_{\kappa,N}^*\) satisfies
\[
 \|[V_{\kappa,N},\widetilde H_N]\|_{\rm op}
       \leq2\|H_N\|_{\rm op}\delta_N(\kappa).
\]
Thus arithmetic commutants, including the original spectral projectors,
persist to every inverse-power accuracy. This is not a claim that they
commute exactly at each finite N. It explains why the construction does not
supply an arithmetic-free test of positive BGS universality.

This result does not assume the earlier Floquet Hilbert--Schmidt normal form,
the smooth Gaussian theorem, or a numerical assertion about the fourth moment.
Its analytic dependencies are (1), locality (12), the finite product bound,
and the explicitly verified dilation spectrum.

# 6. Optional Fourier-Gevrey refinement

The all-orders theorem above needs only smoothness. Under the stronger,
explicit assumption that for some s>1 and a>0
\[
 G=\sum_v|\widehat g(v)|e^{a|v|_2^{1/s}}<\infty,\qquad
 H=\sum_v|\widehat d(v)|e^{a|v|_2^{1/s}}<\infty,              \tag{21}
\]
one gets a quantitative stretched-exponential remainder. Indeed
\[
 M_j(g)\leq G(sj/(ae))^{sj},\qquad
 M_j(d)\leq H(sj/(ae))^{sj}.
\]
Using \(j!\geq(j/e)^j\) in (13), define
\(C=\pi e(s/(ae))^{2s}\), \(\nu=2s-1\), and
\(c=(eC)^{-1/\nu}\). For N large choose the largest odd integer
\(j\leq(N/(eC))^{1/\nu}\). Then
\[
 \|[\operatorname{Op}_N(g),\operatorname{Op}_N(d)]\|
       \leq2GH e^2 e^{-cN^{1/\nu}},\qquad
 \delta_N(\kappa)\leq4\pi^2\kappa^2GH e^2N^2e^{-cN^{1/\nu}}.
                                                               \tag{22}
\]
Consequently conjugacy persists uniformly for integer
\(|t|\leq e^{c'N^{1/\nu}}\) whenever \(0<c'<c\). The constants in (21)
are assumptions, not values estimated by fitting the numerical curve.
Here e denotes the base of the natural logarithm. No optimality claim for the exponent is made. General Gevrey composition
remainder estimates are existing microlocal theory; (22) is a direct
conditional Fourier-norm calculation for this setting.

# 7. Exact nodal realization and numerical scope

The explicit bump (9) allows an exact finite matrix formula even though its
Fourier support is infinite. For integer x,y in \(\{0,\ldots,N-1\}\),
\[
 \boxed{\displaystyle
 [\operatorname{Op}_N(g_0)]_{xy}=
 \ell((x+y)/(2N))\frac1N\sum_{z=0}^{N-1}
 b_r(z/N)e^{-2\pi i(x-y)z/N}.}                              \tag{23}
\]
To prove it, write the exact position kernel of Q(v), group the second
Fourier index as \(b=x-y+kN\), and sum the first index. The result is
\(\ell((x+y)/(2N)-k/2)\). Its half-periodicity removes k. The remaining
sum over the residue class of b is exactly the discrete Fourier transform
of the nodal values of b_r. Absolute Fourier convergence justifies grouping.
Without half-periodicity (23) need not hold; the verifier includes a negative
control for that omission. No numerical Fourier truncation of the bump is
being passed off as the exact smooth operator.

Evenness implies that odd-space matrices can be formed as
\(A^-_{xy}=A_{xy}-A_{x,N-y}\), \(1\leq x,y\leq D_N\).
The implementation checks unitarity, Hermiticity, parity, exact Weyl covariance
on small finite Fourier controls, and two independent exponential computations.
It compares the finite loop error to the measured commutator bound in (14),
including both signs of kappa. Classical flow integration checks the order
and sign in (8); these integrations are numerical falsifiers, not a substitute
for the exact flow proof.

The proof of support separation has exact rational and integer checks plus
a small Lean linear-arithmetic certificate. The Lean module's scope does not
include smooth functions, Fourier convergence, matrix exponentials, the
Anosov property, or spectral asymptotics. Its compiler status must be reported
from an actual build, not inferred from the presence of its source.

The numerical report records floating-point matrices from (23), not an
interval certificate. At large N a commutator comparable to floating-point
rounding is reported as a numerical floor, not as an exact zero. Neither a
fitted rate nor a small finite residual is used to prove (6).

# 8. Relation to BGS and prior work

The examples retain arithmetic structure through a smooth symplectic
conjugacy and its quantum counterpart. They therefore cannot be presented
as positive BGS universality for a generic Anosov map, or as systems with all
arithmetic symmetries eliminated. Their content is a fixed-strength,
nonlinear, explicitly quantized family for which the spectral obstruction
and Heisenberg-scale comparison are proved, rather than merely extrapolated
from a shrinking-strength theorem.

Keating and Mezzadri studied arithmetic pseudo-symmetries and anomalous
spectra of nonlinearly perturbed cat maps well before this project. Their
primary report describes shear perturbations and quantum-lattice symmetries.
Prosen and Znidaric established the residual-perturbation and commutator
mechanism for fidelity freeze. Unitary conjugation preserves spectra, and
microlocal separation gives all-orders small products; neither principle is
new here. A targeted search is insufficient to establish whether this exact
single-exponential construction or a stronger one already appears elsewhere.

The productive unresolved positive route is to control a perturbation not
smoothly conjugate to the cat map, with its symmetry assumptions explicit,
at fixed nonzero classical strength. The present proof deliberately does not
claim that result. It also shows why simply iterating the second-order
variance test cannot classify all smooth perturbations: an entire nonzero
smooth subspace has no nonzero local commutator term at any order.

Primary references and the limitations of their retrieval are recorded in
the [companion source audit](../literature/all_orders_conjugacy_sources.md).
