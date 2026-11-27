# Conditional boundary-prefix estimates at fixed nonzero coupling

This audit concerns the original odd-dimensional signed family \(U_N=e^{i\tau N A_N}M_N\), with \(\tau\) fixed and \(0<|\tau|\le 10^{-30}\). Sources are Days 99–112 in the November 25–27 review packet, in particular Day 109 and the separate marked-prefix draft. The two proposed stretched-exponential estimates below are conditional. They concern the boundary mean or single nontrivial Fourier coefficients. The distinguished-phase trace, TRACE-005, and BGS-BGS-001 remain open.

## Verified algebraic steps

Write \(S=\bigl(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\bigr)\), \(A=S^T\), and \(J=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)\). On a Fourier–Weyl sector use the integer frequency \(l\) and the deck \(c=l-v\bmod N\). With the literal integer midpoint convention, the kick generator coefficient from \(l\) to \(l+u\), before multiplying by \(i\tau N\), is
\[
-2i\widehat g(u)\sin\!\left(\pi u^TJ(l-c)/N\right).
\]
Replacing \(l\) by its midpoint \(l+u/2\) has no effect on the sine. Thus the exact scalar Weyl symbol of this commutator is
\[
g(d-J(\xi-c/N)/2)-g(d+J(\xi-c/N)/2).
\]
The cat sends \((d,\xi,c)\) to \((S^{-1}d,A\xi,Ac)\). A signed insertion shifts \((\xi,c)\) by \((b/N,b)\) and fixes the two physical points \(z_\pm=d\pm J(\xi-c/N)/2\). Replacing \(c\) by \(c+Nm\) changes the integer Weyl basis by a scalar and a translation of \(d\) by \((m_p,m_q)/2\); the physical points agree modulo integers. In these coordinates the commutator Hamilton equations give the same \(X_g\) on both points. The positive exponential gives the inverse physical flow for propagation.

For the exact positive character convention of Day 99, let \(y\) lift the boundary Fourier character \(h\), let \(z_j\) be the centred lifts of \(S^jNy\), and put \(v_j=Jz_{-j}\). Use the rotated representatives at ties. With \(k_i=z_{i+1}-Sz_i\), the inserted integer shifts are
\[
b_j=v_{j+1}-Av_j=-JS^{-1}k_{-j-1}.
\]
Their total transported shift is \(m'=(I-A^n)v_0\), congruent to \(NJ(S^n-I)y\) modulo \((I-A^n)\mathbb Z^2\). This gives the positive insertion in the trace. A returning affine path satisfies \(c_{j+1}=Ac_j+b_j\bmod N\). Scalar closed paths satisfy the same recurrence in the ordinary **integer** frequency \(l\), which forces \(l_0=v_0\) by invertibility of \(I-A^n\). For nontrivial \(h\) this is not integral. For \(h=0\) the scalar contribution is exactly one with the centred zero representative.

The smooth replacement of the sharp trace in Day 111 works for each returning path. Truncate the incremental jumps at \(J_0\); since \(|b_j|_\infty\le4\), the retained periodic recurrence forces every frequency into the box of radius \(2(J_0+4)\). On this box the chosen smooth multiplier equals one. Thus the two *truncated cyclic traces* agree exactly. Recover the untruncated traces by ordinary operator-norm telescoping on the finite apertures, of dimension \(O(N^2)\) per deck. The exponentially small jump estimate with \(J_0=\lceil1600|\tau|N+C\log(2N)\rceil\) permits the at most \(N^2\) returning decks for a single character. It gives no such bound by absolute summation over all characters.

## Classical energy and the polynomial summation step

Use the near-identity conjugacy \(F_\tau H=HS\). The two primitive coefficients that enter the classical pressure have nonzero linear terms: in the Green series for the first variation of \(H-\mathrm{id}\), only the zero iterate contributes on either axis because \((S^T)^{\pm j}e_q,(S^T)^{\pm j}e_p\) have second coordinate of modulus \(>1\) for \(j\ge1\). Also \(|\widehat g(e_q)|\ge1/20\) and \(|\widehat g(e_p)|=1/200\). With \(P_u\) the unstable projection of \(S\), the factors \(e_i\cdot P_uJe_i\) are \(-1/\sqrt2,1/(2\sqrt2)\). The time parameter in this variation is \(t=\tau/(2\pi)\).

The weighted-word argument has the following structure. In a sufficiently fine two-sided Markov partition a paired Bowen-separated graph set injects into each of its two marginal words, since on the bare torus the paired trajectories are related by a translation at each time. The Gibbs comparison of both word laws gives \(\log Z=-\tfrac12(D_++D_-)+O(1)\) for the half-unstable weights. For an axial character \(f\) with Gibbs mean \(m\), the two centred expectations satisfy \(Y_j-p_jX_j=m(p_j-1)\), where \(p_j=e(-e_i\cdot a_j)\). The bilateral Gibbs concentration bound gives logarithmic exponential moments \(O(s^2\sum_j|p_j-1|^2)\): the separately Lipschitz constants are \(O(|s(p_j-1)|)\). Replacing tests by their representatives on length-\(k\) words costs a fixed error by geometric decay from the two word endpoints. Relative entropy duality at \(s\) a sufficiently small fixed multiple of \(|m|\) bounds \(D_++D_-\) below by \(c_\tau\sum_j|p_j-1|^2-O(1)\). Combine the two axes. For finite aperture trajectories the linear Green bound matches the graph up to exponentially decreasing endpoint errors; Hölder distortion of the potential is summable. This argument uses a Gibbs measure for the fixed coupling. It does not make the concentration constant uniform through \(\tau=0\).

The shrinkage of Bowen separation in the marked-prefix argument can be justified in *physical* coordinates. Within a fixed small Bowen ball, differences obey \(e_{j+1}=D e_j+R_je_j\) in one lift, where \(D\) is the fixed hyperbolic product derivative and \(\|R_j\|=O(|\tau|)\). The finite stable-forward and unstable-backward Green operator is bounded on the maximum norm independently of length. Absorbing the perturbation shows
\[
\max_j\|e_j\|\le C(\|P_s e_0\|+\|P_u e_{\mathrm{last}}\|).
\]
The two endpoint coordinates together have dimension four. Their elementary packing bound gives \(O(\delta^{-4})\) points separated at physical Bowen scale \(\delta\) in each fixed-radius Bowen ball. Merely pulling a metric packing estimate through a Hölder conjugacy would not preserve the stated exponent four.

Suppose now the local chart recurrence specified below holds. An order-\(\ell\) term differentiated \(R\) times has at most \(\ell\) positive-order updates and at most \(2\ell+R\) derivatives on the propagated amplitudes. Distributing those derivatives in the product rule marks a bounded number of sites. Uniform derivative estimates on *each entire inverse subcomposition* bound the transport chain factors. Thus there are polynomially many marked-site patterns for fixed \(\ell,R\). At all other sites the original nonnegative partition weight is retained. In a Bowen ball of radius \((j+1)^{-2}\) the sum of the local unmarked suprema is \(1+O((j+1)^{-2})\); marked sites cost a bounded factor. Comparing the half-Jacobians on the same stationary path, the graph slope discrepancy decays geometrically and the unstable projection-volume ratios telescope. The energy bound therefore gives the polynomial prefix sum
\[
\sum_{\text{prefixes }w}\sum_{\ell<M}\sup_\eta\|a_{w,\ell,\eta}\|_{C^R}
 \le C(1+j)^B e^{-c_\tau E_j}.
\]
The exact contraction telescope, applied after summing the one-step residuals, gives \(O(h^{M-1}(1+j)^{B+1})\) at length \(j\), with \(h=1/N\). The loss \(h^{-1}\) is the single initial Fourier synthesis in two position dimensions.

## Uniform extended graph transforms

The derivative part of the local construction can be obtained without enlarging the expansion constants at each step. This is a local classical statement. Let \(x,y\in\mathbb R^2\) be adapted symplectic coordinates in canonical lifts, with the two growing coordinates in \(x\). The common linear part is \(L(x,y)=(\lambda x,\lambda^{-1}y)\), \(\lambda=3+2\sqrt2\). Take equal-radius input and output charts with the same adapted linear frame, possibly with different origins. On a compatible branch the derivative of the actual canonical map differs from \(L\) by \(O(|\tau|)\) and its derivatives of order at least two are \(O_r(|\tau|)\). A deck translation or a bounded Fourier insertion modifies only the origins in these estimates.

In mixed variables \((x',y)\), the generating function for such a branch has the form
\[
 \mathcal S(x',y)=\lambda^{-1}x'\!\cdot y+\text{affine function}+r(x',y).
\]
Indeed \(x\mapsto x'\) is locally invertible and the pullback symplectic identity makes \(y'\,dx'+x\,dy\) closed on a rectangular mixed-variable box. Subtract the constant and first jet of \(r\) at its center. In an enlarged fixed box of radius \(\epsilon\), its size, first derivative and second derivative are then \(O(|\tau|\epsilon^2), O(|\tau|\epsilon), O(|\tau|)\). Multiplying the entire remainder by a cutoff equal to one on an inner box gives a global generating function with the same affine terms and \(\|D^2r\|_\infty=O(|\tau|)\). It is important to cut the perturbation of the bare mixed quadratic form in full. Cutoff derivatives of a small quadratic term are also small; cutoff derivatives of the bare quadratic form need not be. The equations \(x=\partial_y\mathcal S(x',y)\), \(y'=\partial_{x'}\mathcal S(x',y)\) now define a global exact symplectic map. For each fixed \(y,x\), the first equation is solved by contraction after multiplication by \(\lambda\). Outside the fixed-size enlarged box the perturbation vanishes. All these maps have uniform derivative bounds at any fixed order.

For a graph \(y=\psi(x)\) of slope at most \(1\), write the extended map as \(F=(Q,P)\). The map \(x\mapsto Q(x,\psi(x))\) is globally invertible, by the same contraction applied to \(Q-\lambda x\). Denote its inverse by \(g\). Uniformly in chart centers,
\[
 \|Dg\|\le\beta=(\lambda-O(|\tau|))^{-1}<1,\qquad
 \|D\psi_{\rm new}\|\le(\lambda^{-1}+O(|\tau|))\beta<1
\]
for the outgoing graph \(\psi_{\rm new}\). For \(r\ge2\), differentiate
\(\psi_{\rm new}\circ Q(x,\psi(x))=P(x,\psi(x))\).
The term multiplying \(D^r\psi\) in \(D^r\psi_{\rm new}\) is
\[
 \bigl(P_y-D\psi_{\rm new}\,Q_y\bigr)\,D^r\psi\,(Dg)^{\otimes r},
\]
with evaluation at the corresponding points. All other terms contain derivatives of the graph of orders below \(r\), bounded by induction, and bounded derivatives of \(F\). The coefficient norm is at most
\((\lambda^{-1}+O(|\tau|))\beta^r<1\). This gives a fixed-order bound for arbitrarily long compatible chart chains, starting from affine graphs. Individual inverse maps have bounded higher derivatives by implicit differentiation. For an entire inverse subcomposition the same induction uses composition in reverse time, appending a new inverse map on the left: the coefficient of the previous top-order derivative is at most \(\beta\); all lower derivatives and the individual higher derivatives are bounded. Thus the constants do not grow with the length of the subcomposition.

The graph calculation controls derivatives on the proposed branches, including after extension. To use it inside the weighted trace proof one still has to show that the torus stationary coefficients are supported on those branches and that the remainder has the required common-Hilbert-space bound. In particular, the adapted real frame is only local. The derivative proof does not produce a global finite metaplectic change of coordinates.

## First unverified quantum input and downstream scope

Fix the two nested smooth apertures and a finite physical chart partition. For every fixed expansion order \(M\), the input still to verify is a uniform one-step construction on the **actual scalar torus Weyl transfer**, for every admissible deck, shift \(\|b_j\|_\infty\le4\), prefix and initial leaf momentum in a fixed compact set. The microscopic coordinates on a prefix must be determined before its next chart is chosen. The construction must place every stationary coefficient at orders \(0,\ldots,M-1\) on a single lifted branch agreeing with the actual canonical relation on its full coefficient support, also after differentiation. At order zero it must retain exactly the chosen nonnegative partition factor up to a unit phase and the projected inverse half-Jacobian. The remainder for each next chart must be \(O(h^M)\) times finitely many \(C^R\) norms of the incoming coefficients after sewing back into the same exact Hilbert space, uniformly in the prefix. Derivative bounds for the forward leaf graphs and inverse subcompositions, and these support properties for the positive-order coefficients, have to hold together for this fixed choice of charts.

Nonnenmacher–Zworski, Lemma 4.1 and Proposition 4.1, supply the local expansion and the iteration pattern under their mixed-phase hypotheses. Their displayed estimates (4.31), (4.34), and (4.35) use products of separate determinant suprema. Those suprema do not identify the simultaneous stationary path needed by the energy pressure, nor do they certify the torus chart sewing above. An extra fixed exponential loss at this step is fatal for sparse decks: the available exponent there is of order \(j/\log N\), not order \(j\). The algebraic telescope and marked-word count identify what would suffice without requiring Gevrey estimates. [Nonnenmacher–Zworski](https://arxiv.org/abs/0706.3242) · [Chazottes–Gouëzel, Theorem 2.4](https://gouezel.pages.math.cnrs.fr/webpage/articles/concentration.pdf)

Conditional on that construction, a nonzero denominator-\(N\) grid deck supplies a nonzero wrap in each \(O(\log N)\)-step segment. Indeed, two lifted points with the same wrap sequence differ by a homogeneous recurrence and the nonzero grid quadratic invariant gives a lower bound of order \(N^{-2}\) on the product of the expanding and contracting coordinates. Thus \(j=K\log^2 N\) gives energy at least a constant times \(K\log N\). Sharp-to-smooth loss comparison then gives Day 109's boundary-mean error \(e^{-cN/\log^4 N}\). Day 111 preserves the *smooth trace itself* by the jump argument above and uses high energy or an unshifted zero-deck interior of a long digit-free block. It would give
\[
|a_0-1|+\max_{h\ne0}|a(h)|=O(e^{-cN/\log^2(2N)}).
\]
The small-index coset and local window conclusions of Days 111–112 inherit this condition. The Day 114 cusp test as a raw spectral identity is separate; subtracting that stronger mean inherits the same condition. Many individually small coefficients do not bound the full inverse transform at one fixed boundary phase.
