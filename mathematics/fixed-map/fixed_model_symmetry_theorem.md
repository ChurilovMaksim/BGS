# Fixed frozen model: exact Weyl dictionary, trivial C1 centralizer, and no C1 reversor

**Claim ID:** `BGS-FM-001`

Date: 21 September 2026.

Status: project theorem with author-level author check, exact rational/symbolic checks, and an independent Wolfram recomputation in the recovered handoff. It is not an independent referee report, a Lean proof, a priority claim, or a proof of BGS.

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

## 3. Quantitative proof and complete symmetry classification

All vector norms below are Euclidean, matrix norms are induced Euclidean
operator norms, and the norm of a multilinear derivative is its induced
multilinear norm. Supremum norms are over the torus; displacements use the
periodic lift to \(\mathbb R^2\). Put \(t=|\kappa|\).

Exact Fourier assembly of (1), \(g=\sum c_ve^{2\pi i v\cdot x}\), gives
\[
\sum_v(|\Re c_v|+|\Im c_v|)|v|^2=51451/1000<52,
\qquad |v|<10.
\]
There is no nonzero frequency of length below one. Differentiating the
Fourier series, using \(|c_v|\le|\Re c_v|+|\Im c_v|\), therefore gives
\[
\|X_g\|_\infty\le400=:B,\quad
\|DX_g\|_\infty\le3000=:L,\quad
\|D^2X_g\|_\infty\le200000=:M.                 \tag{5}
\]
Indeed the respective upper bounds before rounding are
\(2\pi52,(2\pi)^252,(2\pi)^310\cdot52\).

### 3.1 Hyperbolicity and a quantitative conjugacy

Let \(\lambda=3+2\sqrt2\). A matrix \(T\) of unit eigenvectors of
\(S\) has condition number \(\sqrt2\), and
\(T^{-1}ST=\operatorname{diag}(\lambda,\lambda^{-1})\).
The variational equation gives
\(\|D\Phi_g^\kappa-I\|\le e^{Lt}-1\), also for the inverse flow.
In eigenvector coordinates both errors are at most
\(\delta=\sqrt2(e^{Lt}-1)<10^{-8}\).
For \(DG=DB\), where \(D=\operatorname{diag}(\lambda,\lambda^{-1})\)
and \(\|B-I\|\le\delta\), the cone \(|y|\le|x|\) is strictly
preserved: its first coordinate expands by at least
\(\lambda(1-\sqrt2\delta)>5\), while its second is bounded by
\(\lambda^{-1}(1+\sqrt2\delta)|x|\).
For \((DG)^{-1}=B^{-1}D^{-1}\), the cone \(|x|\le|y|\) is strictly
preserved with second-coordinate expansion at least
\(\lambda-6\delta>5\) and first-coordinate bound
\((\lambda^{-1}+6\delta)|y|\). Nested cones give invariant contracting
and expanding lines, hence the Anosov property. Analyticity and area
preservation follow from the Hamiltonian flow.

Here is a direct conjugacy construction, including the displacement bound.
On continuous periodic vector fields set \(\mathcal Lv=v\circ S-Sv\).
Write \(P_s,P_u\) for the spectral projections of \(S\). For a given
continuous periodic \(f\), the unique bounded solution of \(\mathcal Lv=f\) is
\[
v_s(x)=\sum_{j\ge1}S_s^{j-1}P_sf(S^{-j}x),\qquad
v_u(x)=-\sum_{j\ge0}S_u^{-j-1}P_uf(S^jx).
\]
The geometric series converge uniformly. Using the eigenbasis above,
\[
\|\mathcal L^{-1}\|\le\sqrt2\left(
\frac1{1-\lambda^{-1}}+\frac1{\lambda-1}\right)=2<3.
\]
Put \(f_\kappa(x)=S(\Phi_g^\kappa(x)-x)\). Since \(\|S\|<7\),
\(\|f_\kappa\|_\infty\le2800t\) and
\(\operatorname{Lip}f_\kappa\le7(e^{Lt}-1)\).
Thus \(v\mapsto\mathcal L^{-1}[f_\kappa(\mathrm{Id}+v)]\)
is a contraction, with constant \(3\cdot7(e^{Lt}-1)<1\).
Its fixed point gives
\[
h_\kappa=\mathrm{Id}+v,\quad h_\kappa S=G_\kappa h_\kappa,
\qquad \|v\|_\infty\le8400t.                         \tag{6}
\]
This continuous degree-one map is onto. It is one-to-one as well: if
\(h_\kappa(x)=h_\kappa(y)\), then all the torus distances between
\(S^nx,S^ny\), \(n\in\mathbb Z\), are at most \(16800t<1/8\).
Choose their small difference lifts \(d_n\). The integer
\(d_{n+1}-Sd_n\) has norm less than \(8\cdot16800t<1\), so is zero.
A two-sided bounded orbit of a hyperbolic linear matrix is zero.
Thus \(x=y\); compactness makes \(h_\kappa\) a homeomorphism.

### 3.2 Fixed points and topological candidates

Direct differentiation of (1) shows that the four points
\(P=\{0,\tfrac12\}^2\) have zero gradient and Hessian
\(\operatorname{diag}(b_x,0)\), with respective values
\[
 b_x/\pi^2=-19606/125,-19594/125,24306/125,24894/125
\]
in the order \((0,0),(0,1/2),(1/2,0),(1/2,1/2)\).
Consequently these points are fixed by \(G_\kappa\), and
\[
\operatorname{tr}DG_\kappa(x)=6-4\kappa b_x.             \tag{7}
\]
The formula is exact because \((J\operatorname{Hess}g(x))^2=0\).
The contraction iteration above starting at zero has \(v|_P=0\),
so \(h_\kappa\) fixes \(P\). Also \(S\) has exactly
\(|\det(S-I)|=4\) fixed points, so these are all the fixed points of
\(G_\kappa\). Their four traces are distinct. A \(C^1\) commuter fixes
each point; the same holds for a reversor, since the inverse of a
\(2\times2\) determinant-one matrix has the same trace.

For completeness, every torus homeomorphism commuting with \(S\), or
conjugating \(S\) to \(S^{-1}\), is affine. Indeed write its lift as
\(Bx+w(x)\), with \(B\in GL(2,\mathbb Z)\) and periodic bounded \(w\).
The lift equation has a constant integer discrepancy. Subtracting a
constant vector \(a\) removes this discrepancy because \(I-S^{\pm1}\)
is invertible. The remaining equation is
\((w-a)(Sx)=S^{\pm1}(w-a)(x)\). Boundedness for all positive and
negative iterates forces \(w=a\). The translation then satisfies
\(Sa=a\) modulo \(\mathbb Z^2\).

The integral equation \(BS=SB\) gives
\(B=\left(\begin{smallmatrix}a&2b\\b&a\end{smallmatrix}\right)\)
with \(a^2-2b^2=\pm1\). Its solutions are precisely
\(B=\pm C^n\), \(n\in\mathbb Z\), where
\[
C=\begin{pmatrix}1&2\\1&1\end{pmatrix},\quad C^2=S,
\qquad R_0=\operatorname{diag}(1,-1).
\]
One elementary completeness check for this Pell description is to multiply
any unit \(a+b\sqrt2\), after choosing its sign, by a power of
\(1+\sqrt2\) until its real value lies in \([1,1+\sqrt2)\).
Its conjugate is \(\pm1/(a+b\sqrt2)\); the resulting integer \(b\)
is in \([0,1)\), hence is zero and the unit is one.
Since \(R_0SR_0=S^{-1}\), all reversors are \(\pm C^nR_0\).

Apply this classification to \(h_\kappa^{-1}Hh_\kappa\) or
\(h_\kappa^{-1}Rh_\kappa\). Fixing zero removes the translation;
fixing all of \(P\) means that the matrix is identity modulo two.
As \(C\bmod2=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)\)
has order two, \(n\) is even. The only candidates are therefore
\(\pm S^j\) and \(\pm S^jR_0\).

### 3.3 Period-three coefficient and uniform remainder

Let \(O=((1,2),(4,1),(2,4))/7\), an oriented \(S\)-orbit. For
\(B\in\{I,-I,R_0,-R_0\}\), let \(T_B(\kappa)\) be the derivative
trace of \(G_\kappa^3\) at the continued orbit \(h_\kappa(BO)\).
Choose the forward \(G_\kappa\)-ordering on each orbit. The trace is
independent of the starting point because the monodromies are conjugate.
Since
\(S^3=\left(\begin{smallmatrix}99&140\\70&99\end{smallmatrix}\right)\),
the exact linear coefficient is
\[
 A_B=\sum_{x\in BO}\operatorname{tr}(S^3DX_g(x))
     =\sum_{x\in BO}(70g_{pp}(x)-140g_{qq}(x)).
                                                        \tag{7a}
\]
This finite trigonometric expression explicitly defines every coefficient;
no derivative of \(h_\kappa\) is needed. For a directly reproducible
rational enclosure, use
\[
 A_B/\pi^2=4\sum_{x\in BO}\sum_{(k,l)}(140k^2-70l^2)
 [\Re(c_{kl})\cos(2\pi(kx_q+lx_p))
 -\Im(c_{kl})\sin(2\pi(kx_q+lx_p))].
\]
Expansion of (1) and rational Taylor bounds give
\[
\begin{array}{c|c}
 B&(A_I-A_B)/\pi^2\\\hline
 -I&[-520.048877703,-520.048877702]\\
 R_0&[568.942361931,568.942361932]\\
 -R_0&[-1088.991239635,-1088.991239634].
\end{array}                                               \tag{7b}
\]
For specificity, these enclosures can be checked without floating point:
use Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\),
90 alternating terms for each arctangent and its next-term remainder;
round outward to
\([3.14159265358979323846,3.14159265358979323847]\).
Reduce each trigonometric argument modulo \(2\pi\) to \([-\pi,\pi]\),
use cosine through degree 40 and sine through degree 41, with respective
Taylor errors \(4^{41}/41!\), \(4^{42}/42!\). Rational interval
arithmetic in the displayed formula yields (7b).

Here is a uniform remainder calculation. The integral variational equation,
\(\|\Phi_g^s(z)-z\|\le B|s|\), and (5) imply
\[
\|D\Phi_g^\kappa(z)-I-\kappa DX_g(z)\|
 \le\tfrac12(MB+L^2)e^{Lt}t^2.
\]
Replacing \(z\) by \(h_\kappa(x)\), using (6), gives
\[
D\Phi_g^\kappa(h_\kappa(x))=I+\kappa DX_g(x)+E_x,
\quad \|E_x\|\le e_0t^2,\qquad e_0=1.8\cdot10^9,
\]
because \(8400M+(MB+L^2)e^{3\cdot10^{-9}}/2<e_0\).
Expanding the three factors \(S(I+\kappa DX_g(x)+E_x)\) and using
\(|\operatorname{tr}A|\le2\|A\|\) gives
\[
|T_B(\kappa)-198-\kappa A_B|
\le2\cdot7^3[3e_0+3(L+e_0t)^2+(L+e_0t)^3t]t^2.
\]
Twice this bracketed bound is less than \(8\cdot10^{12}t^2\)
for \(t\le10^{-12}\). Therefore each difference satisfies
\[
|T_I(\kappa)-T_B(\kappa)-\kappa(A_I-A_B)|
 \le8\cdot10^{12}\kappa^2.                              \tag{7c}
\]
The linear term has magnitude greater than \(500\pi^2t\), whereas
this remainder is at most \(8t\). Thus the three differences never
vanish in the stipulated punctured interval.

A commuter with topological representative \(-S^j\) would identify
\(h_\kappa(O)\) and \(h_\kappa(-O)\), forcing equal derivative traces,
contrary to (7c). The representatives \(\pm S^jR_0\) similarly force
equality with \(T_{\pm R_0}\); reversing a determinant-one monodromy
preserves its trace. This excludes every reversor. The remaining
commuters \(h_\kappa S^jh_\kappa^{-1}\) are exactly \(G_\kappa^j\).
Finally an affine toral map with homological part conjugate to \(S\)
has derivative trace six at every fixed point; (7) excludes a \(C^1\)
conjugacy to it. This proves all four assertions of Section 2.

## 4. Raw-versus-ordinary Weyl regression

For odd \(N>18\), the wrong ordinary-symbol identification has normalized Hilbert--Schmidt discrepancy

\[
\frac1N\|A_N^{\rm raw}-A_N^{\rm wrong}\|_{\rm HS}^2=\frac1{5000}.
\tag{8}
\]

By contrast, the corrected dictionary (1) is exact, and the finite generator regression decays at the expected \(N^{-2}\) scale. This is a structural correction, not a small numerical convention.

## 5. Boundary

The theorem removes smooth classical commuting symmetries, reversibility, and affine conjugacy as explanations for the frozen model. It does not exclude \(N\)-dependent quantum commutants, prove Heisenberg-time trace cancellation, or imply microscopic random-matrix statistics. The fixed-\(\tau\) BGS problem remains open.
