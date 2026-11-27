# Fixed-step partition, transport and lift locality for the scalar torus kick

Use the exact scalar Weyl deck operator and the smooth aperture of the [conditional boundary-prefix calculation](boundary_prefix_audit_20261127.md). The identities below are fixed-step inputs. The long-prefix sewing still requires a common-Hilbert-space \(O(h^M)\) remainder with stationary branch support through order \(M-1\), uniformly in the previous prefix, deck, insertion and incoming momentum. Here \(h=1/N\).

## Exact partition and the local principal factor

Let \(T_j\) be one exact unitary step and \(Q=\operatorname{Op}_h^w(q)\) with \(q(\xi)\in C_c^\infty\), \(0\le q\le1\). Choose finitely many nonnegative smooth functions \(\chi_i\) subordinate to small target phase-space charts, summing to one around \(\operatorname{supp}q\). Then
\[
 B_i=\operatorname{Op}_h^w(q\chi_i),\qquad \sum_iB_i=Q,\qquad
 QT_jQ=\sum_i B_iT_jQ
\]
hold by linearity of the exact torus quantization. The contraction in this identity is the full product \(QT_jQ\); no positivity assertion is needed for individual \(B_i\). There is just one chosen partition on the output. A target chart of sufficiently small diameter has a single local lift of its inverse image, because the step is a smooth canonical map and its inverse has bounded derivative on the relevant boxes. This describes one step and one target chart.

Once a branch is localized to such a lift with a mixed generating function \(S(x',\eta)\), the phase for its action on \(a(x)e^{i\psi(x)/h}\) is \(S(x',\eta)-x\cdot\eta+\psi(x)\), using the ordinary oscillatory integral convention. A stationary point has \(x=S_\eta(x',\eta),\,\eta=\psi_x(x)\). In the adapted local coordinates the bare map has \(S_{\eta\eta}=0\). Assume \(\|S_{\eta\eta}\|\|\psi_{xx}\|<1\) on the convex boxes used in this calculation. The fixed point in \(x\) is then unique when present. The stationary Hessian is
\[
  \begin{pmatrix}\psi_{xx}&-I\\-I&S_{\eta\eta}\end{pmatrix}.
\]
It has determinant in absolute value \(|\det(I-S_{\eta\eta}\psi_{xx})|\) and signature zero, by the homotopy that multiplies \(S_{\eta\eta}\) by a scalar in \([0,1]\). For the microlocally unitary uncut branch, the principal kernel amplitude has modulus \(|\det(S_{\eta x'})|^{1/2}\). Implicit differentiation gives \(D_{x'}x=(I-S_{\eta\eta}\psi_{xx})^{-1}S_{\eta x'}\), so the transported principal coefficient has precisely the projected inverse half-Jacobian \(|\det D_{x'}x|^{1/2}\). In this formula the two aperture evaluations are \(q\) at the input and \(q\chi_i\) at the output along the same trajectory. For a fixed expansion order all symbolic derivatives evaluate at points where the corresponding factors have support; a factor zero on a neighborhood makes its differentiated coefficient vanish there. In the fixed-step stationary expansion an order-\(s\) term differentiates the incoming amplitude at most \(2s\) times. These statements assume a valid single lifted representation and uniform bounds on the indicated graph and chart data.

## Exact lift of the position-localized kick

For fixed deck \(c\bmod N\) the exact scalar Weyl symbol is
\[
 H_c(d,\xi)=g(d-J(\xi-c/N)/2)-g(d+J(\xi-c/N)/2).
\]
Each integer Fourier mode \(u\) of the symbol has position frequency \(u\) and momentum exponential \(\exp(\pm\pi i u^TJ\xi)\); its remaining coefficient has modulus \(|\hat g(u)|\). Ordinary midpoint Weyl quantization on the lift sends these terms to a multiplication followed by a translation of length \(h|u|/2\), because \(u^TJu=0\). The same formula on periodic functions is the exact torus Weyl operator (apply to each Fourier basis function). Call the lifted self-adjoint operator \(L_c\), set \(C_0=2\sum_u|\hat g(u)|\) and \(R_0=\tfrac12\max_u|u|\). Each word in \(L_c^m\) has displacement at most \(mhR_0\) and the sum of its absolute coefficients over words is bounded by \(C_0^m\). These constants are independent of the deck gauge.

Use bounded multiplication cutoffs supported in fixed small lifted input and output position patches. On the output lift the exact torus kernel of the kick \(\exp(i\tau L_c/h)\) gives the sum of Euclidean transfers from all integer translates of the input. To see this, periodize the input and apply each word. Whatever its shift, only boundedly many input copies can meet the output patch, since the difference set of the two fixed patches is bounded. The bound on the number of copies is independent of the shift. The operator-norm sum over copies and powers converges absolutely at each \(h\) by \(\sum_m(|\tau|C_0/h)^m/m!\).

For copies whose supports have separation at least a fixed \(a>0\), all words of length below \(L=\lceil a/(hR_0)\rceil\) give zero. Put \(z=|\tau|C_0/h\). For \(L\ge 2z\) the ratio of consecutive tail terms is at most \(1/2\), and \(L!\ge(L/e)^L\) gives a tail bound \(2(ez/L)^L\). If \(|\tau|\le a/(4eC_0R_0)\), this is at most \(2\exp(-(\log4)a/(hR_0))\). The same bound up to the fixed overlap multiplicity holds for the sum over all separated copies. In particular, when there is one potentially interacting lift, the localized torus kick differs from that lifted Euclidean kick by \(O(e^{-c_a/h})\) in ordinary operator norm. The clearance is fixed as \(h\to0\), and the kick restriction depends on that clearance.

The linear cat is an exact pullback on lifts, and signed momentum insertions are exact multiplication operators. For a fixed \(q\in C_c^\infty(\mathbb R^2)\), the Euclidean Fourier multiplier has kernel of the form \(h^{-2}\widehat q((d'-d)/h)\) up to Fourier signs. Periodize it. Its Schwartz bounds, summed over integer translates away from the diagonal, give \(O(h^D)\) for every fixed \(D\) across a fixed position clearance, by the integral Schur test. The exponential estimate above controls distant position aliases before adapted phase-space changes of coordinates. It leaves open the simultaneous support and norm conditions for a coherent growing-prefix torus sewing, where the aperture and graph must be tracked together.
