---

**Stable claim IDs:** BGS-RET-003, BGS-RET-004.
title: "Noncommuting return words and all-orders arithmetic quantum conjugacy"
author: "BGS research programme"
date: "6 September 2026"
---

# Scope and the new distinction

A nonzero Poisson bracket need not have positive Green--Kubo variance. This
note constructs an explicit nonzero bracket which is a smooth coboundary and,
more strongly, proves all-orders quantum conjugacy at fixed classical strength
for its natural single-exponential kick. The conjugating operator is a product
of local propagators, not the exponential of the linear coboundary generator.
This separates three genuinely different conditions:
$$
\{g,\mathcal Cg\}=0,
\qquad \sigma^2(\{g,\mathcal Cg\})=0,
\qquad V_{\kappa,N}=J_{\kappa,N}U_NJ_{\kappa,N}^*+O(N^{-\infty}).
$$
The construction satisfies the last two but not the first. It does not refute
any previously stated theorem requiring analyticity or Fourier support in a
fixed finite box. The generators are smooth nonanalytic functions with open
critical regions. Arithmetic symmetries are transported, not eliminated.

The elementary telescoping identity for a group-valued coboundary is standard.
No novelty is claimed for that identity, for unitary conjugacy preserving a
spectrum, or for microlocal locality. The project's result is their explicit
combination for one fixed local Hamiltonian kick and a noncommuting generator,
with a finite operator-norm remainder. A targeted source search has not
established priority for this exact example; no first-ever or prize-level
claim is made.

# 1. Quantization and a finite return-word theorem

Put
$$
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\quad S=T^{\mathsf T},
 \quad \mathcal Cf=f\circ S,\quad \hbar_N=(2\pi N)^{-1}.
$$
Use physical integer Weyl operators satisfying
$$
 Q_N(v)Q_N(w)=e^{\pi i\det(v,w)/N}Q_N(v+w),\quad
 U_NQ_N(v)U_N^*=Q_N(Tv).
$$
The latter convention is valid for this T, which is the identity modulo two.
Write $C_N(X)=U_NXU_N^*$ and $\operatorname{Op}_N(f)=\sum_v\widehat f(v)Q_N(v)$.
All symbols in this note are real and smooth; their quantizations are Hermitian.
Even symbols preserve parity. A fixed finite family is used throughout.

Let L >= 2 be a fixed integer. Let E be a closed subset of the torus such that
$E_j=S^{-j}E$, $0\leq j<L$, are pairwise disjoint. Choose symbols
$h_0,\ldots,h_{L-1}$ supported in E, and put
$$
 H_j=\operatorname{Op}_N(h_j),\quad e=\kappa/\hbar_N,
 \quad W_j=e^{ieH_j},\quad G_j=W_jW_{j-1}\cdots W_0.
$$
Assume the exact return identity
$$
                         W_{L-1}\cdots W_0=I.                 \tag{RW1}
$$
The assumption is imposed for the parameters and quantizations being used;
it is automatically true for every e and every N for an anti-palindromic
list $h_{L-1-j}=-h_j$. It is not inferred from the weaker relation $\sum h_j=0$.
Define
$$
 f=\sum_{j=0}^{L-1}\mathcal C^jh_j,\qquad
 J_N=\prod_{j=0}^{L-2}C_N^j(G_j),\qquad
 V_N=e^{ie\operatorname{Op}_N(f)}U_N,                         \tag{RW2}
$$
where the product defining J is in increasing order of j from left to right.

**Return-word theorem.** For all pairs (N,kappa) satisfying (RW1), uniformly with $|\kappa|\leq B$ for each fixed B,
$$
             \|V_N-J_NU_NJ_N^*\|_{\mathrm{op}}=O(N^{-\infty}). \tag{RW3}
$$
For every fixed p the same estimate holds after taking any integer power
$|t|\leq N^p$. The statement holds on the full space, and on each parity
sector if all the local symbols are even.

**Proof.** Locality gives, for i and j at different sites and odd r,
$$
 \|[\operatorname{Op}_N(\mathcal C^ih_a),
          \operatorname{Op}_N(\mathcal C^jh_b)]\|
 \leq\frac{2\pi^r}{r!N^r}B_r^2,
 \qquad B_r=\max_{i,a}M_r(\mathcal C^ih_a),                  \tag{RW4}
$$
with $M_r(a)=\sum_v|\widehat a(v)||v|_2^r$. Each finite Taylor coefficient
of the exact sine commutator is a mixed local derivative and is zero on
account of the disjoint closed supports. A real Taylor remainder proves
(RW4) without an infinite-series convergence assumption.

For Hermitian A,B, integration of two unitary conjugations gives
$$
 \|[e^{ieA},e^{ieB}]\|\leq e^2\|[A,B]\|.                  \tag{RW5}
$$
Consequently elementary factors at distinct sites can be interchanged with
this error; factors at the same site are never interchanged. Reorder the
factors of $J_NC_N(J_N^*)$ by their site. The resulting site factors are
$$
 G_0=W_0,\quad G_jG_{j-1}^*=W_j\ (1\leq j<L-1),\quad
 G_{L-2}^*=W_{L-1},                                        \tag{RW6}
$$
where the last identity uses (RW1). Thus the reordered product is
$\prod_{j=0}^{L-1}C_N^j(W_j)$. The original word has at most $L(L-1)$
elementary exponential factors. Fewer than $L^4/2$ interchanges suffice, so
(RW4)--(RW5) control the accumulated error independently of the size of eH.

The standard two-factor Duhamel estimate, iterated L times, gives
$$
 \left\|e^{ie\sum_j C_N^jH_j}-\prod_j e^{ieC_N^jH_j}\right\|
       \leq\frac{e^2}{2}\sum_{i<j}\|[C_N^iH_i,C_N^jH_j]\|.
$$
Combining these inequalities, for $L\geq2$ one may use the deliberately
conservative explicit bound
$$
 \boxed{\displaystyle
 \|V_N-J_NU_NJ_N^*\|
 \leq\frac{8\kappa^2\pi^{r+2}L^4}{r!}
                      B_r^2 N^{2-r},\qquad r\text{ odd}.}   \tag{RW7}
$$
Choosing r as large as desired proves (RW3). Telescoping unitary powers
costs at most $|t|$ and proves the time statement. Negative t uses adjoints.
No spectral modification and no N-dependent counterterm was introduced.
End of proof.

For an anti-palindromic word, the corresponding identity of classical
Hamiltonian pullbacks holds exactly. Pullbacks belonging to distinct sites
commute, whereas their order at each site is retained. Thus (RW6) also
establishes an exact smooth symplectic conjugacy of the associated classical
map to S. In particular the map is Anosov. This is an exceptional arithmetic
family, not a demonstration of random-matrix universality.

# 2. Four sites with a nonzero second bracket

Choose real even a,b supported in E, with $p=\{a,b\}\ne0$, and use
$$
 (h_0,h_1,h_2,h_3)=(a,b-a,a-b,-a).
$$
This is an anti-palindromic word. Its linear coboundary generator is
$$
 g=a+\mathcal Cb+\mathcal C^2a,\qquad
 f=g-\mathcal Cg
   =a+\mathcal C(b-a)+\mathcal C^2(a-b)-\mathcal C^3a.        \tag{RW8}
$$
Subtracting the mean of g changes neither f nor the bracket below, and only changes an exponential gauge by a scalar. Thus the example also belongs to the mean-zero generator class. Only the overlaps at sites 1 and 2 contribute to the Poisson bracket:
$$
 \boxed{\displaystyle
 \{g,\mathcal Cg\}=\mathcal C^2p-\mathcal Cp
          =(I-\mathcal C)(-\mathcal Cp)\ne0.}               \tag{RW9}
$$
Nonvanishing follows because p is nonzero and its two translated supports
are disjoint. The displayed transfer function proves exactly
$$
                  \Gamma_T(g)=0.                           \tag{RW10}
$$
Thus the implication ``nonzero consecutive bracket implies nonzero second
resonance'' is refuted on the smooth class by an explicit construction, not
merely left as an unproved inference.

Put $A=\operatorname{Op}_N(a)$, $B=\operatorname{Op}_N(b)$,
$X=e^{ieA}$, and $Y=e^{ie(B-A)}$. The actual gauge is
$$
                \boxed{J_N=X\,C_N(YX)\,C_N^2(X).}          \tag{RW11}
$$
The same-site factors Y and X need not commute. Replacing YX by $e^{ieB}$
would replace J by a different gauge and is not justified. Its derivative
at e=0 nevertheless has the generator $A+C_N(B)+C_N^2(A)$, matching (RW8).

With $X_h=(h_p,-h_q)$ and flow $\Phi_h^t$, the smooth conjugacy can be
written explicitly:
$$
 \Psi_\kappa=\Phi_a^\kappa\circ\Phi_{\mathcal C(b-a)}^\kappa
       \circ\Phi_{\mathcal Ca}^\kappa\circ\Phi_{\mathcal C^2a}^\kappa,
 \qquad S\circ\Phi_f^{-\kappa}=\Psi_\kappa S\Psi_\kappa^{-1}. \tag{RW12}
$$
The rightmost classical map acts first. Formula (RW12) is the reversed
composition of the pullbacks quantized by (RW11); it can also be obtained
by the exact classical version of (RW6). The map differs from S for all
sufficiently small nonzero $\kappa$ since f is nonconstant, and agrees with S
on an open set. It is therefore nonaffine in this range.

An additional useful separation is
$$
 \lim_{N\to\infty}N\|[\operatorname{Op}_N(g),
                    \operatorname{Op}_N(\mathcal Cg)]\|_{2,N}
       =\frac{\|\{g,\mathcal Cg\}\|_2}{2\pi}>0.             \tag{RW13}
$$
This follows from the cubic Fourier commutator remainder and the fixed-symbol
Hilbert--Schmidt limit. Equations (RW3) and (RW13) coexist. A large enough
principal commutator rules out the old *commuting-observable proof*, not every
nonlinear unitary gauge. Neither (RW9) nor (RW13) contradicts the analytic
rigidity theorem: the functions used here are not analytic.

On any Pell sequence with $U_N^K=I$, the average of the actual commutator is
smaller than every inverse power, too. The two same-site contributions are
$C_N([B,A])+C_N^2([A,B])$ and telescope under the period average; every
remaining contribution is a cross-site commutator controlled by (RW4).
This conclusion concerns the averaged commutator, not its nonzero local norm.

## Extension to every hyperbolic integral toral automorphism

The construction is not specific to trace six. For any hyperbolic
$A\in\mathrm{SL}(2,\mathbb Z)$ use $S=A^{\mathsf T}$ and the invariant
characteristic $Q_N^*(v)=(-1)^{v_1v_2+v_1+v_2}W_N(v)$ described in the finite
spectral theorem. Choose z outside the finite sets $S^jz=\pm z$ for
$1\leq j<L$ and $2z=0$. Small symmetric neighborhoods of z and -z then
give the required disjoint tower. Real even local a,b with nonzero Poisson
bracket exist inside these neighborhoods by the same bump-and-coordinate
construction. Equations (RW8)--(RW13) remain unchanged, with this S and
quantization. Thus every such A admits a noncommuting smooth generator with
nonzero consecutive bracket, zero second variance, and fixed-strength
all-orders quantum conjugacy under a product gauge. On the prime-period
sequence of the general spectral theorem, use its prescribed uniform parity
sector, which may be even. The cluster and local-statistics conclusions then
follow there. This assertion does not replace A by its square when its trace
is negative.

# 3. An explicit support and nonzero bracket

Let $r=1/96$ and $z=(5/11,0)$. Let E be the two closed torus squares of
halfwidth r centered at z and -z. The four sets $E,S^{-1}E,S^{-2}E,S^{-3}E$
are pairwise disjoint. This is a finite rational geometry assertion, not a
visual assertion from a coarse plot. It suffices to check
$E\cap S^jE=\varnothing$, $j=1,2,3$.

For a matrix $M=S^j$ and sign $\varepsilon\in\{\pm1\}$, all possible
integer translations n of a collision lie in the rectangle
$$
 |n_i-(Mz-\varepsilon z)_i|
 \leq r\left(1+\sum_k|M_{ik}|\right).
$$
For every candidate n, a separating normal w from
$(1,0),(0,1),(-M_{21},M_{11}),(-M_{22},M_{12})$ satisfies
$$
 |w\cdot(n-Mz+\varepsilon z)|
 >r\left(\|w\|_1+\sum_k|w\cdot M e_k|\right).              \tag{RW14}
$$
For j=1,2 the candidate rectangle contains no integer point. For j=3 there
are 30 candidates; all are excluded by (RW14) with exact rational arithmetic.
The full list of normals, both sides and positive gaps is part of the
certificate. An independent C++ check clears all denominators by 1056 and
enumerates a wider integer box, then applies the same necessary inequalities.
The two base lobes have exact separation margin $37/528$.

Put $\beta(t)=e^{1-(1-t^2)^{-1}}$ for $|t|<1$ and zero otherwise. With
periodic lifts near the two lobes define
$$
 \chi_\pm(q,p)=\beta((q\mp5/11)/r)\beta(p/r),\quad
 a=\chi_++\chi_-,\quad
 b=\frac{q-5/11}{r}\chi_+-\frac{q+5/11}{r}\chi_-.            \tag{RW15}
$$
All expressions are periodically extended. Both a,b are real and even. On
the positive lobe b=ua, $u=(q-5/11)/r$, hence
$\{a,b\}=-a a_p/r$. At $(q,p)=(5/11,r/2)$ this is
$-\beta(1/2)\beta'(1/2)/r^2>0$, proving the required nonzero bracket without
numerical integration. The total area of the four support levels is at most
$32r^2=1/288<1$, so their complement contains an open set.

# 4. Exact nodal quantization without the half-period restriction

For arbitrary smooth periodic functions $a(q),b(p)$, physical Weyl
quantization of the separable symbol has the exact finite formula
$$
 \begin{split}
 [\operatorname{Op}_N(a(q)b(p))]_{xy}
 ={}&a((x+y)/(2N))\,B_{x-y}\\
 &+a((x+y)/(2N)-1/2)\,B_{x-y+N},\qquad
 B_l=\frac1{2N}\sum_{z=0}^{2N-1}b(z/(2N))e^{-2\pi ilz/(2N)}.
 \end{split}                                               \tag{RW16}
$$
Subscripts of B are reduced modulo 2N. To prove it, group the integer
momentum frequency as $x-y+kN$ in the Weyl kernel and split k into its even
and odd parts. Summation over the position frequency is exact; the two
residue classes are exactly the indicated 2N-point Fourier coefficients.
Absolute Fourier convergence justifies regrouping.

Unlike the earlier N-point formula, (RW16) does not require a half-periodic
position factor. It therefore applies to both symbols in (RW15) without an
unrecorded Fourier cutoff. It is a finite representation identity; floating
point evaluation of its entries is not interval-certified.

# 5. Verification and what the finite data do not show

The exact geometry certificate has 30 rational separation obligations. The
independent integer C++ verifier also checks the nonabelian prefix identity
for eleven anti-palindromic words and the exact coefficients (0,-1,1,0) in
(RW9). The numerical block control uses four orthogonal sites with two
noncommuting 2-by-2 Hermitian matrices. It verifies (RW11) to rounding accuracy
and rejects the incorrect linear gauge $e^{ie\operatorname{Op}(g)}$.
This finite block model is a falsifier of factor order, not a torus theorem.

The 2N-node formula is compared with independent finite Weyl sums containing
both odd position frequencies and aliases. The invalid N-node formula is
retained as a negative control. Classical ODEs compare both sides of (RW12)
at the four support levels and at both signs of the strength.

Dense torus matrices are tested at N=63,127,255,511. These are mostly not Pell
moduli and are operator-comparison tests, not demonstrations of a Pell limit.
At kappa=0.02 some finite gauge errors are close to the maximal norm 2.
The supports are narrow and the estimates in (RW7) are asymptotic; no monotone
convergence or useful finite-size rate is inferred from these data. Small
fixed strengths provide nonvacuous finite-bound controls. An initial ODE-rich
batch exceeded its time cap; the final documented smaller ODE family completed.
The exact analytic support and word arguments do not depend on that reduction.

The local cluster, factorial correlation and Heisenberg-window consequences
of all-orders operator-norm conjugacy now apply to this noncommuting example
as well. They remain negative results for a smoothly arithmetic-conjugate
family. Theorem (RW3) supplies no positive BGS law, no symmetry elimination,
and no classification of the zero set of Gamma for analytic or finite Fourier
symbols. Its actual advance is the explicit nonzero-coboundary bracket and the
return-word gauge which replaces the commuting-generator mechanism.
