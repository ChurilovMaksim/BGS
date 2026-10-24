# Exact Haar feedback law and an entropy-stable clock class

**Stable claim:** BGS-TRACE-076.
**State:** PROVED; independent internal reconstruction of the original
candidate, with maintained-transfer review recorded in the
[review packet](../../archive/evidence/executions/20261012/haar-feedback/README.md).
Sections 1–3 are self-contained. The unconditional clock corollaries use
the reviewed [conditional all-fixed-order theorem](conditional_clock_universality.md)
and [reference measure](full_depth_clock_measure.md).
Haar-compatible Schur projections, Cauchy ensembles and matrix beta laws
are prior objects; [source comparison](../../literature/haar_feedback_sources_20261012.md)
states the exact priority boundary. No deterministic-map transfer, analytic
Lean certification, priority or global BGS claim is made.

## 1. Finite feedback and the exact joint law

Let \(U\) be Haar on \(U(N)\). Retain a predetermined set \(R\) of \(u\)
coordinates and eliminate the \(q=N-u\) complementary coordinates \(E\),
with arbitrary fixed unit-modulus phases \(W_E\). Start \(F_N(z)=zU\),
so \(T_N=I_N\). Reorder \(R\) first and absorb the phases into eliminated rows:
\[
\widehat U=\operatorname{diag}(I_u,W_E)U.
\]
This is still Haar, including conditional on an entire independent phase
vector and coordinate order. A set chosen adaptively from \(U\) is outside
this assertion. Solving the eliminated coordinate equations gives
\[
\begin{aligned}
X(z)&=(I_q-z\widehat U_{EE})^{-1}z\widehat U_{ER},\\
F_u(z)&=z\widehat U_{RR}+z\widehat U_{RE}X(z),\\
X&=X(1),\quad S=F_u(1),\quad T=S^*F_u'(1),\quad Q=STS^*.
\end{aligned}                                                    \tag{1}
\]
Sequential feedback gives the same expression: eliminate this same
linear system in the disk, then continue analytically to a nonsingular
boundary point. A Haar unitary has no eigenvalue \(1\) almost surely.
A vector fixed by its principal block \(\widehat U_{EE}\) would, by
conservation of norm, give a vector supported on \(E\) fixed by
\(\widehat U\). Thus all needed inverses at \(z=1\) exist almost surely.
There are finitely many sizes and intermediate steps.
For \(u=N\), \(X\) is empty and \(T=I_N\).

For \(1\le u<N\), the exact joint law is
\[
\begin{gathered}
S\text{ is Haar on }U(u)\text{ and independent of }T,\qquad
T=I_u+X^*X,\\
\mathbb P_X(dX)=c_{q,u}\det(I_u+X^*X)^{-(N+u)}dX.                 \tag{2}
\end{gathered}
\]
Here \(dX\) is ordinary real and imaginary Lebesgue volume on complex
\(q\)-by-\(u\) matrices. \(T\) is invariant under unitary conjugation.
\(Q\) has the same law and is also independent of \(S\), but the pair
\((T,Q)\) need not be independent of \(S\). No independence across sizes
is asserted.

## 2. Proof by Cauchy block factorization

First prove the delay identity. On \(z=e^{i\theta}\),
\[
z\widehat U\begin{pmatrix}I_u\\X(z)\end{pmatrix}
 =\begin{pmatrix}F_u(z)\\X(z)\end{pmatrix}.
\]
Differentiate in \(\theta\) and multiply on the left by
\((F_u(z)^*,X(z)^*)\). The \(X(z)^*\dot X(z)\) terms cancel:
\[
-iF_u(z)^*\dot F_u(z)=I_u+X(z)^*X(z).
\]
At \(\theta=0\), \(-i\dot F_u=F_u'(1)\), proving \(T=I_u+X^*X\).

Introduce the Hermitian Cayley variable
\[
C=i(I+\widehat U)(I-\widehat U)^{-1}
 =\begin{pmatrix}A&B^*\\B&D\end{pmatrix},\qquad
\widehat U=(C-iI)(C+iI)^{-1}.                                    \tag{3}
\]
Its Haar density is proportional to \(\det(I+C^2)^{-N}dC\).
Indeed the left-translated differential is
\[
-i\widehat U^*d\widehat U=2(C-iI)^{-1}dC(C+iI)^{-1}.
\]
Hermitian congruence \(H\mapsto LHL^*\) in dimension \(n\) has real
Jacobian \(|\det L|^{2n}\). Reduce to the singular values \(s_j\) of
\(L\): each real diagonal coordinate gives \(s_j^2\), each off-diagonal
complex coordinate gives \(s_j^2s_k^2\), and the product is
\(\prod_j s_j^{2n}\). Left-invariant unitary volume is Haar volume;
the factor \(2^{N^2}\) enters normalization. This derives the density.

Multiply the colligation equation by \(C+iI\). Its two block rows give
\[
S=(A-iI)(A+iI)^{-1},\qquad X=B(A+iI)^{-1}.                         \tag{4}
\]
Set \(G=I_q+XX^*>0\) and introduce a Hermitian \(Y\) by
\[
B=X(A+iI),\qquad D=XAX^*+G^{1/2}YG^{1/2}.                         \tag{5}
\]
This is a bijective smooth change of variables \((A,X,Y)\mapsto(A,B,D)\)
with real Jacobian
\[
\det(I_u+A^2)^q\det(G)^q.                                        \tag{6}
\]
The first factor is complex rectangular right multiplication, row by
row; the second is Hermitian congruence in dimension \(q\).
The full derivative is block triangular in the displayed variable order.
Derivatives of the \(X\)-dependent square root therefore add no factor.

The Schur determinant identity yields
\[
\begin{aligned}
\det(I+iC)&=\det(I+iA)\det\bigl(G+i(D-XAX^*)\bigr)\\
 &=\det(I+iA)\det(G)\det(I+iY).                                  \tag{7}
\end{aligned}
\]
Here \(B(I+iA)^{-1}B^*=X(I-iA)X^*\); \(G\) and \(D\) were not
assumed to commute. Combine (7), its complex conjugate, and (6).
The transformed density factors as
\[
\det(I+A^2)^{-u}\,
\det(I_q+XX^*)^{-(N+u)}\,
\det(I+Y^2)^{-N}\ dA\,dX\,dY.                                   \tag{8}
\]
Each factor has a finite positive integral: the product integrates to
the finite original mass, and Tonelli excludes an infinite factor
because the other integrals are positive. Thus \(A\) and \(X\) are
independent. The \(A\) factor is the Haar Cayley density in dimension
\(u\), so (4) proves (2). Right-unitary invariance of the \(X\) density
gives conjugation invariance of \(T\). Conditioning on \(S\) proves the
assertions about \(Q\).

## 3. Exact inverse-Jacobi law, rank and mean

Let \(G_0\in\mathbb C^{q\times u}\) and
\(Y_0\in\mathbb C^{2u\times u}\) be independent standard complex Gaussian
matrices, with scalar density \(e^{-|g|^2}/\pi\). Then
\[
X\stackrel{d}{=}G_0W^{-1/2},\qquad W=Y_0^*Y_0.                    \tag{9}
\]
\(W\) has density proportional to \(\det(W)^u e^{-\operatorname{Tr}W}\).
Changing \(G_0=XW^{1/2}\) contributes \(\det(W)^q\).
The Hermitian gamma integral of \(W\) then gives
\(\det(I+X^*X)^{-(2u+q)}\), exactly (2); its congruence Jacobian
supplies the additional power \(u\).

With \(B_0=G_0^*G_0\), the eigenvalues of \(T^{-1}\) are those of
\[
J=(W+B_0)^{-1/2}W(W+B_0)^{-1/2}.                                 \tag{10}
\]
This is the finite Jacobi ratio of independent complex Wishart matrices
of degrees \(2u\) and \(q\). For \(q<u\), \(B_0\) is singular and \(J\)
has exactly \(u-q\) eigenvalues one. The remaining \(r=\min(q,u)\)
eigenvalues \(y_l\in(0,1)\) have density
\[
c\prod_{l=1}^{r}y_l^u(1-y_l)^{|q-u|}
 \prod_{l<k}(y_l-y_k)^2.                                        \tag{11}
\]
To check both regimes, the positive singular-value squares \(t_l\) of
\(X\) have radial Jacobian
\(\prod_l t_l^{|q-u|}\prod_{l<k}(t_l-t_k)^2\prod_l dt_l\).
Locally, at distinct positive singular values \(\sigma_l\), diagonal
angular directions give \(\sigma_l d\sigma_l\), unused complex row or
column directions give \(\sigma_l^{2|q-u|}\), and the two complex
rotation directions for each pair give
\((\sigma_l^2-\sigma_k^2)^2\). Passing to \(t_l=\sigma_l^2\) gives
the radial Jacobian; transposition exchanges the rectangular regimes
without changing real volume or singular values. Multiply by the
density factor \(\prod_l(1+t_l)^{-(N+u)}\) and set
\(y_l=1/(1+t_l)\). Its \(y_l\) power is
\[
N+u-|q-u|-2r=u,
\]
proving (11) without a nonsingular-\(B_0\) assumption.

The exact atom of \(uT/N\) at \(u/N\) has almost-sure mass
\[
\max\{0,(u-q)/u\}=\max\{0,2-N/u\}.                               \tag{12}
\]
This saturates the existing pathwise lower bound for this ensemble.
For \(q>0\) and \(k>0\), \(\mathbb E\operatorname{Tr}(T^k)<\infty\)
exactly when \(k<u+1\). Near a single \(y_l=0\), with the other
eigenvalues in disjoint interior intervals, the density is a positive
constant times \(y_l^u\), proving necessity. For sufficiency, bound
the Vandermonde and \((1-y_l)^{|q-u|}\) on the unit cube and integrate
\(y_l^{u-k}\). Finite-\(N\) clocks are unbounded; compact support of
their limiting reference gives no finite edge bound.

Finally \(\mathbb EW^{-1}=I_u/u\). The reciprocal of its \(j\)-th
diagonal entry is the squared length of a Gaussian column projected off
the other \(u-1\) columns, a gamma variable of shape \(u+1\).
Its inverse has mean \(1/u\), and unitary invariance gives the matrix
identity. Independence and \(\mathbb E B_0=qI_u\) imply
\[
\mathbb ET=(1+q/u)I_u=(N/u)I_u,\qquad
\mathbb E(uT/N)=I_u.                                            \tag{13}
\]
Sections 1–3 require no clock induction, intensity gap or flatness premise.

## 4. All-time Haar flatness discharges the clock premise

Use the fresh independent uniform phases and independent uniform
coordinate order of the maintained clock process, with \(U_N\) Haar
independent of both. At each predetermined retained size \(u\), (2)
makes \(S_u\) Haar on the retained coordinates, also conditional on the
entire independently sampled order and phase vector.
Fix \(\kappa>0\), set \(\ell=\log(2N)\),
\(m=\lceil\ell^{1+\kappa}\rceil<N\), and define
\[
A_m(K)=\{\max_{ij}|(S_u)_{ij}|^2\le K\ell/u
                         \text{ for every }u\ge m\}.
\]
A Haar entry in dimension \(u\ge2\) has tail \((1-t)^{u-1}\) for
\(0\le t<1\); above \(t=1\) its failure probability is zero. This
follows from a normalized complex Gaussian column and Dirichlet squared
coordinates. A union bound gives
\[
\begin{aligned}
\mathbb P_{\mathsf H_N}(A_m(K)^c)
 &\le\sum_{u=m}^{N}u^2e^{-K\ell(u-1)/u}\\
 &\le N^3(2N)^{-K(1-1/m)}=:b_N(K).                               \tag{14}
\end{aligned}
\]
No independence between sizes was used. For fixed \(K>3\),
\[
b_N(K)=2^{-K}N^{3-K}(1+o(1)),
\]
because \(\ell/m\to0\). In particular \(K=4\) gives
\((1+o(1))/(16N)\).

For fixed \(L,K,\kappa\), let \(\mathcal E_{L,N}\) be the maximum
error in all conclusions (1) of the conditional clock theorem, including
all sizes \(u\ge m\) and powers \(1\le r\le L\). That theorem gives
\(\varepsilon_N\to0\), depending only on \(L,K,\kappa\), such that
\[
\sup_{U\in U(N)}
\mathbb P_U(A_m(K)\cap\{\mathcal E_{L,N}>\varepsilon_N\})\to0.      \tag{15}
\]
The supremum formulation follows from its deterministic-sequence
quantifier: if uniformity failed, choose a violating deterministic initial
unitary at infinitely many \(N\), contradicting the theorem for that
sequence. It also follows from the constants in the predictable-stop
proof. Integrate (15) over Haar initial matrices and add (14).
All clock conclusions are now **unconditional in probability**, uniformly
for \(u\ge m\): incoming and outgoing diagonal powers with references
\(f_r(u/N)\), vanishing off-diagonal powers, vanishing mixed entries
\(S_u(uT_u/N)^r\), and all fixed empirical moments.

The empirical clock law also converges uniformly to the maintained
family \(\mu_{u/N}\) in the bounded-Lipschitz metric. The uniform moment
argument is as follows. The measures \(\mu_x\), \(0\le x\le1\), have
a common compact support and continuous moments \(f_r(x)\). For every
positive tolerance there exist finite \(L\) and a moment tolerance such
that, for probability measures on \([0,\infty)\), closeness of moments
\(1,\ldots,L\) to \(f_r(x)\) forces weak-metric
closeness, uniformly in \(x\). Otherwise choose counterexamples with
\(L\to\infty\) and moment tolerance tending to zero, and take a subsequence
\(x\to x_0\). First moments give tightness. A bounded next higher moment
gives uniform integrability for each fixed moment. Every subsequential
weak limit has all moments \(f_r(x_0)\); compact moment determinacy
identifies it with \(\mu_{x_0}\), a contradiction. Apply this finite-\(L\)
assertion to (15). No growing moment order was inserted into that theorem.

## 5. Entropy stability beyond Haar initial matrices

Let \(\nu_N\) be a law on \(U(N)\), independent of the fresh phase/order
process, with finite relative entropy \(D_N=D(\nu_N\Vert\mathsf H_N)\).
Put \(p_N=\mathbb P_{\nu_N}(A_m(K)^c)\) and
\(q_N=\mathbb P_{\mathsf H_N}(A_m(K)^c)\).
The relative entropy of initial matrix together with the independent
randomness is still \(D_N\). Jensen for the density on this event and
its complement gives
\[
\begin{aligned}
D_N&\ge p_N\log(p_N/q_N)
 +(1-p_N)\log((1-p_N)/(1-q_N))\\
 &\ge p_N\log(1/q_N)-\log2.
\end{aligned}
\]
If \(q_N=0\), absolute continuity gives \(p_N=0\). Otherwise, for
large \(N\) with \(b_N(K)<1\),
\[
p_N\le\frac{D_N+\log2}{\log(1/b_N(K))}.                           \tag{16}
\]
Thus \(D_N=o(\log N)\) gives high-probability all-time flatness for
each fixed \(K>3\). The stronger clock conclusion is:

**If \(D_N=O(\log N)\), every fixed clock conclusion of Section 4
holds unconditionally in probability, uniformly for \(u\ge m\).**

Fix \(L,\kappa\) and a tolerance \(\eta>0\). For each fixed \(K>3\),
integrate (15) over \(\nu_N\). Once \(\varepsilon_N(K)<\eta\), the
remaining failure probability is bounded by (16). With
\(C=\limsup_N D_N/\log N<\infty\),
\[
\limsup_N\mathbb P_{\nu_N}(\mathcal E_{L,N}>\eta)
 \le C/(K-3).                                                   \tag{17}
\]
Let the fixed comparison constant \(K\) tend to infinity **after** this
limsup. No \(N\)-dependent constant was substituted into a fixed-constant
theorem. The \(O(\log N)\) class does not thereby receive high-probability
flatness for one specified finite \(K\).
The finite-moment argument of Section 4 gives the same unconditional
full-depth empirical weak law.

## 6. A precise limitation of entropy stability

Fix \(0<c<1\) and an arc \(I_N\) of angular length \(2\pi c/N\) at a
prescribed origin. Haar rotation invariance gives expected eigenangle
count \(c\). Its void event \(E_N\) therefore has probability at least
\(1-c\). For \(\nu_N=\mathsf H_N(\,\cdot\mid E_N)\),
\[
D(\nu_N\Vert\mathsf H_N)
 =-\log\mathbb P_{\mathsf H_N}(E_N)\le-\log(1-c).                  \tag{18}
\]
This ensemble has every clock conclusion above. At initial size \(u=N\),
however, its rescaled point process has a forbidden interval of length
\(c\). A nonzero nonnegative continuous test function compactly supported inside
that interval has identically zero integral against these processes. An
intensity-one Sine₂ process has a positive expected integral, hence a
positive probability of a nonzero one. Weak point-process convergence
to Sine₂ at that prescribed origin is impossible.

This disproves only an entropy-to-prescribed-origin microscopic implication.
It is not a statement about origin-averaged statistics or a BGS
counterexample. A deterministic initial matrix has infinite relative
entropy with respect to continuous Haar measure. Classical dynamical
entropy is a different quantity. This theorem does not supply the
maintained deterministic map's all-time flatness, full physical TRACE-055,
signed TRACE-005 or global BGS.

## 7. Independent finite controls

The [Python verifier](../../computations/verification/haar_feedback_law.py)
uses exact Gaussian-rational colligations in five \((u,q)\) sizes. Direct
resolvent differentiation independently checks the graph delay identity,
including fixed nontrivial feedback phases. Separate symbolic Jacobians
check the scalar block change, a non-diagonal Hermitian congruence and a
non-diagonal rectangular right product. Twelve one-port Haar-diagonal
moments from circle residues and exact radial integration agree with
the beta-prime law through order four.
The [Wolfram source](../../computations/wolfram/haar_feedback_law.wl) was
executed for two scalar polynomial identities and returned two True
values. These finite checks prove none of the probability-limit or
entropy statements. Their contract, bounded execution and initial
comparison-code failure are retained separately in the review packet.
