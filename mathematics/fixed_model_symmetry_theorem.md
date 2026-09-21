# Fixed frozen model: exact Weyl dictionary, trivial C1 centralizer, and no C1 reversor

Date: 21 September 2026.

Status: project theorem with author-level self-review, exact rational/symbolic checks, and an independent Wolfram recomputation in the recovered handoff. It is not an independent referee report, a Lean proof, a priority claim, or a proof of BGS.

## 1. The unchanged quantum operator and the physical symbol

For odd N keep the raw modular Weyl convention

\[
(T_N(a,b)\psi)(x)=e_N(b(x+2^{-1}a))\psi(x+a),
\qquad
(M_N)_{xy}=N^{-1/2}e_N(-8^{-1}(3x^2-2xy+3y^2)),
\]

\[
U_N=\exp(i\tau N A_N)M_N,\qquad \tau=10^{-80},\qquad
S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
\]

The raw symbol is obtained from

\[
r(q)=(1-\cos14\pi q)(1+\cos2\pi q),
\]

\[
f(q,p)=\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}
+\frac{r(q)\cos(2\pi p-\alpha)}{100},
\quad
\cos\alpha=-\frac35,\quad \sin\alpha=\frac45,
\]

by sending \(e^{2\pi i(kq+\ell p)}\) to \(T_N(\ell,k)\), and centering by \(1/10\).

For ordinary midpoint Weyl matrices

\[
W_N(a,b)=(-1)^{ab}T_N(a,b),
\]

the same matrix \(A_N\), with no change of quantization, is the ordinary Weyl quantization of

\[
\boxed{
g(q,p)=\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}
+\frac{r(q+\tfrac12)\cos(2\pi p-\alpha)}{100}
-\frac1{10}.}
\tag{1}
\]

The shift \(q\mapsto q+\tfrac12\) in the \(p\)-dependent term is forced coefficient-by-coefficient by the factor \((-1)^{k\ell}\). This corrects the tempting but wrong identification of the raw symbol with the ordinary midpoint symbol.

## 2. Classical theorem

Let \(\Phi_g^\kappa\) be the Hamiltonian flow of \(g\), with vector field \(X_g=(g_p,-g_q)\), and set

\[
G_\kappa=S\circ\Phi_g^\kappa .
\]

For every real \(0<|\kappa|\le10^{-12}\):

1. \(G_\kappa\) is a real-analytic area-preserving Anosov diffeomorphism, topologically conjugate to \(S\) by a homeomorphism homotopic to the identity.
2. Its complete \(C^1\) centralizer is
   \[
   \{H\in\mathrm{Diff}^1(\mathbb T^2):HG_\kappa=G_\kappa H\}
   =\{G_\kappa^j:j\in\mathbb Z\}.
   \tag{2}
   \]
3. There is no \(C^1\) diffeomorphism, of either orientation, satisfying
   \[
   RG_\kappa R^{-1}=G_\kappa^{-1}.
   \tag{3}
   \]
4. \(G_\kappa\) is not \(C^1\)-conjugate to an affine toral map whose homological linear part is conjugate to \(S\).

In the conventional Egorov direction \(U_N^*\operatorname{Op}(a)U_N\sim
\operatorname{Op}(a\circ F_\tau)\), the classical map of the prescribed frozen operator is

\[
F_\tau=\Phi_g^{-\tau/(2\pi)}\circ S^{-1}
      =G_{\tau/(2\pi)}^{-1}.
\tag{4}
\]

Thus the theorem applies directly to the actual fixed model.

## 3. Quantitative inputs

Exact Fourier assembly gives

\[
\sum_v (|\Re c_v|+|\Im c_v|)|v|^2=\frac{51451}{1000}<52,
\qquad |v|<10,
\]

and the proof uses the safe uniform bounds

\[
\|X_g\|\le400,\qquad \|DX_g\|\le3000,\qquad \|D^2X_g\|\le200000.
\tag{5}
\]

For \(|\kappa|\le10^{-12}\), the perturbation of the cat derivative is small enough to preserve explicit stable and unstable cones. A contraction solution of the conjugacy equation gives

\[
h_\kappa(x)=x+v(x),\qquad h_\kappa S=G_\kappa h_\kappa,
\qquad \|v\|_\infty\le8400|\kappa|.
\tag{6}
\]

The four points \(P=\{0,\tfrac12\}^2\) are the complete fixed-point set. Their Hessians are diagonal and satisfy

\[
\frac{b_x}{\pi^2}\in
\left\{-\frac{19606}{125},-\frac{19594}{125},
\frac{24306}{125},\frac{24894}{125}\right\},
\]

so

\[
\operatorname{tr}DG_\kappa(x)=6-4\kappa b_x
\tag{7}
\]

takes four distinct values for every nonzero \(\kappa\). Any \(C^1\) commuter or reversor must therefore fix all four points.

Conjugating a candidate by \(h_\kappa\) reduces it to an affine symmetry of \(S\). Solving the integral matrix equations gives commuters \(\pm C^n\) and reversors \(\pm C^nR_0\), where

\[
C=\begin{pmatrix}1&2\\1&1\end{pmatrix},\quad C^2=S,\qquad
R_0=\operatorname{diag}(1,-1).
\]

Fixing the four points forces zero translation and even \(n\), leaving only \(\pm S^j\) and \(\pm S^jR_0\) as topological candidates. Exact period-three derivative-trace comparisons on the orbit

\[
(1,2)\to(4,1)\to(2,4)\pmod7
\]

eliminate the residual minus and reversing candidates. The linear coefficient differences divided by \(\pi^2\) have absolute value greater than \(500\), while the explicit quadratic remainder is smaller than this throughout \(0<|\kappa|\le10^{-12}\).

## 4. Raw-versus-ordinary Weyl regression

For odd \(N>18\), the wrong ordinary-symbol identification has normalized Hilbert--Schmidt discrepancy

\[
\frac1N\|A_N^{\rm raw}-A_N^{\rm wrong}\|_{\rm HS}^2=\frac1{5000}.
\tag{8}
\]

By contrast, the corrected dictionary (1) is exact, and the finite generator regression decays at the expected \(N^{-2}\) scale. This is a structural correction, not a small numerical convention.

## 5. Boundary

The theorem removes smooth classical commuting symmetries, reversibility, and affine conjugacy as explanations for the frozen model. It does not exclude \(N\)-dependent quantum commutants, prove Heisenberg-time trace cancellation, or imply microscopic random-matrix statistics. The fixed-\(\tau\) BGS problem remains open.
