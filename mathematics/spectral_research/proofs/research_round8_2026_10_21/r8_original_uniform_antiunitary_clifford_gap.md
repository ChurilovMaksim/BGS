> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_original_uniform_antiunitary_clifford_gap.md`. Embedded SHA256: `96a22f2e1ef7b79af6fcbd3768f00adb4dac2bbadfef53545bac2199cf96d3e9`.
> [Thematic guide](../../topics/symmetry.md).

# Round 8: a uniform gap from every antiunitary Clifford reverser

Date: 21 October 2026.

## Status and scope

This theorem concerns the exact prescribed matrices, at the fixed
$\tau=10^{-80}$, along all odd dimensions. It excludes approximate
projective time reversal by every antiunitary normalizer of the finite
Weyl system, including arbitrary dimension-dependent modular symplectic
matrices and characters.

The proof distinguishes escaping modular matrices, controlled directly
by the previously proved quantum all-entry estimate, from bounded
matrices, whose limits have affine classical actions. A short independent
proof below excludes every affine reverser of the exact ordinary-half
classical map. Thus the new result does not need the older theorem about
all $C^1$ reversers or its analytic structural conjugacy.

This does not classify arbitrary eigenbasis-dependent antiunitaries. It
does not prove or refute $H_{\rm diag}$, and does not turn symmetry
exclusion into a theorem about the CUE spectral limit.

## 1. Statement and exact antiunitary reduction

Put

$$
 W_v=T_N(l,k),\quad v=(k,l),\qquad
 S_f=\begin{pmatrix}3&2\\4&3\end{pmatrix},\quad S=S_f^T,
 \qquad U_N=E_NM_N,\quad E_N=e^{i\tau NA_N}.
$$

Let $K$ denote coordinatewise complex conjugation, and let
$\mathcal C_N$ be the group of unitary normalizers of the projective
Weyl system. Its exact covariance is

$$
 \Gamma W_v\Gamma^*=e_N(\kappa\cdot v)W_{\sigma v},
 \quad \sigma\in\operatorname{SL}_2(\mathbb Z/N\mathbb Z),
 \quad \kappa\in(\mathbb Z/N\mathbb Z)^2.                 \tag{1.1}
$$

Here no normalizers are omitted. Conjugation permutes projective Weyl
labels by an automorphism of their additive group, hence by an invertible
linear matrix over $\mathbb Z/N\mathbb Z$. Preservation of the exact
Weyl commutator makes its determinant one. Preservation of the Weyl
product then makes the scalar multiplier a character, of the displayed
form. These statements hold for every odd composite modulus as well as
for primes. The scalar freedom in $\Gamma$ is immaterial.

Complex conjugation obeys $KW_{(k,l)}K=W_{(-k,l)}$. Consequently every
antiunitary normalizer is exactly $\Theta=\Gamma K$, with
$\Gamma\in\mathcal C_N$: multiplying an antiunitary normalizer by $K$
gives a unitary normalizer, and conversely.

Define

$$
 R_N^-=\sup_{\Gamma\in\mathcal C_N}
 \frac1N\left|\operatorname{Tr}
      (U_N\Gamma\overline{U_N}\Gamma^*)\right|
 =\sup_{\Theta\in\mathcal C_NK}
 \frac1N\left|\operatorname{Tr}
      (U_N\Theta U_N\Theta^{-1})\right| .
$$

The result is

$$
 \boxed{\limsup_{\substack{N\to\infty\\N\ {\rm odd}}}R_N^-
       \le\sqrt{\frac{1+144\tau}{2}}<\frac34.}             \tag{1.2}
$$

In particular, for all sufficiently large odd $N$, every such
antiunitary $\Theta$, and every $|\zeta|=1$,

$$
 \boxed{\frac{\|\Theta U_N\Theta^{-1}-\zeta U_N^{-1}\|_{\rm HS}}
                    {\sqrt N}\ge\frac1{\sqrt2}.}          \tag{1.3}
$$

The more precise lower bound on the limit inferior of these distances is
$\sqrt{2-\sqrt{2+288\tau}}$. No effective threshold in $N$ is claimed.

For the trace comparison put

$$
 P=U_N\Gamma,\qquad Q=\Gamma U_N^T,\qquad V=P^*Q.
$$

Then $PQ^*=U_N\Gamma\overline{U_N}\Gamma^*$, and
$|\operatorname{Tr}PQ^*|=|\operatorname{Tr}P^*Q|$. Thus the quantity
being estimated is exactly $|\operatorname{Tr}V|/N$; no complex
conjugation or reversal of operator order has been suppressed.

## 2. The exact ordinary-half calculus and the one imported quantum estimate

### 2.1. Correct symbol, product, and cat action

Set $\widetilde W_{(k,l)}=(-1)^{kl}W_{(k,l)}$, with integer labels,
and $Q_N(g)=\sum_v\widehat g(v)\widetilde W_v$. The exact symbol of
the Hamiltonian in this convention is

$$
\begin{split}
 a(q,p)={}&\cos(14\pi q)+r(q)/10
   +r(q)\sin(2\pi q)/100-1/10\\
   &+r(q+1/2)\cos(2\pi p-\alpha_0)/100.                  \tag{2.1}
\end{split}
$$

Indeed the original Fourier coefficient acquires $(-1)^{kl}$.
The $l=0$ terms stay fixed, while $l=\pm1$ translates the
$q$-dependent coefficient by $1/2$. Hence $A_N=Q_N(a)$ exactly.

All frequencies satisfy $|k|+|l|\le9$, and
$\sum|\widehat a(k,l)|<2$. For example
$$
r=1+\cos(2\pi q)-\cos(14\pi q)
  -\tfrac12\cos(16\pi q)-\tfrac12\cos(12\pi q).
$$
Combining the even terms in (2.1) gives Fourier one-norm $11/10$;
the remaining two terms each have one-norm at most $1/25$.
Thus the stronger bound $59/50$ is available.

Writing $\omega(u,v)=u_2v_1-u_1v_2$, the ordinary-half product is
exactly

$$
 \widetilde W_u\widetilde W_v
       =e^{\pi i\omega(u,v)/N}\widetilde W_{u+v}.         \tag{2.2}
$$

This identity retains all modular aliases; it is valid with arbitrary
integer labels, not just labels in a chosen fundamental range.

The kernel of $M_N$ is symmetric, so $M_N^T=M_N$. Direct substitution
in that kernel gives

$$
 M_NT_N(a,b)M_N^*=T_N(3a+4b,2a+3b),
 \qquad M_NW_vM_N^*=W_{S_fv}.                          \tag{2.3}
$$

For verification, compare $M_NT_N(a,b)$ with
$T_N(a',b')M_N$. Matching the two quadratic polynomials gives
$a'=3a+4b$ and $b'=2a+3b$; their constant terms both equal
$-3a^2/8-ab/2$ modulo $N$. All divisions are the modular inverses
specified in the question. In the ordinary-half convention the parity
character is trivial because $3\cdot4$ and $2\cdot3$ are even.
Therefore the classical cat action is precisely $S=S_f^T$, with no
affine shift.

### 2.2. Fixed-symbol Egorov, including the transpose

Let $Z=J\nabla a=(a_p,-a_q)$, let $\Phi_t$ be its flow, and put

$$
 t=\tau/(2\pi),\qquad h=(2\pi N)^{-1},\qquad
 \Psi=S\circ\Phi_t .
$$

Then $E_N=\exp(itQ_N(a)/h)$. Equation (2.2), together with
$|\sin x-x|\le |x|^3/6$, gives for every fixed smooth $g$

$$
 \left\|\frac{i}{h}[Q_N(a),Q_N(g)]-Q_N(Zg)\right\|
                \le C_gN^{-2}.                            \tag{2.4}
$$

The finite Fourier support of $a$ and the rapid decay of the Fourier
coefficients of $g$ make the constant finite. Explicitly the summand
error is bounded by a constant times
$N^{-2}|\widehat a(u)\widehat g(v)|\,|\omega(u,v)|^3$.
The sign is fixed by
$Z e_v=-4\pi^2\sum_u\omega(u,v)\widehat a(u)e_{u+v}$.

Integrating (2.4) along the fixed smooth symbols $g\circ\Phi_s$,
between $s=0$ and $s=t$, proves

$$
 E_NQ_N(g)E_N^*=Q_N(g\circ\Phi_t)+O_g(N^{-2}).
$$

The same proof applies to inverse time. Combining with (2.3) gives

$$
 U_NQ_N(g)U_N^*=Q_N(g\circ\Psi)+O_g(N^{-2}).             \tag{2.5}
$$

Transpose sends $\widetilde W_{(k,l)}$ exactly to
$\widetilde W_{(k,-l)}$, so $A_N^T=Q_N(a\circ R_p)$, where
$R_p(q,p)=(q,-p)$. Since $R_p$ is antisymplectic, the flow of
$J\nabla(a\circ R_p)$ is $R_p\Phi_{-t}R_p$. Also
$R_pSR_p=S^{-1}$. Therefore $U_N^T=M_NE_N^T$ has the exact
fixed-symbol Egorov map

$$
 \boxed{\Psi_T=R_p\Psi^{-1}R_p
             =R_p\Phi_{-t}R_p S.}                         \tag{2.6}
$$

The order here is essential: transpose reverses the two factors of
$U_N$, rather than merely replacing $a$ in (2.5).

### 2.3. Uniform quantum output-label tail

The sole imported quantitative quantum result is the previously proved
all-entry estimate in

research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md,
Sections 2--6, SHA-256

**c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd**.

For the exact kick it states

$$
 |\langle W_w,E_NW_uE_N^*\rangle_N|
 \le C_\tau(1+|w|_N)^{-1/17}+C_\tau/N,                   \tag{2.7}
$$

uniformly for all nonzero input and output labels and all sufficiently
large odd $N$. Here
$\langle A,B\rangle_N=N^{-1}\operatorname{Tr}(A^*B)$;
$|w|_N$ is a centered label norm. That source supplies the actual
finite-shift proof, including the modular-half aliases and the output
version. It has no prime, squarefree, or $7\nmid N$ restriction.
The constant may depend on the prescribed fixed $\tau$. No estimate
uniform as $\tau\downarrow0$ is needed or asserted.

Only (2.7) is used for escaping modular matrices. Egorov (2.5) is used
only for a fixed finite set of matrices after that branch is removed.

## 3. Escaping modular matrices: a direct quantum gap

For either basic label $e_j$, the support and norm bounds in Section 2
give the exact operator-norm bound

$$
 \|[A_N^T,W_{e_j}]\|
 \le\frac{2\pi}{N}
       \sum_u|\widehat{a\circ R_p}(u)|\,|\omega(u,e_j)|
 \le\frac{36\pi}{N}<\frac{144}{N}.
$$

Unitary Duhamel, with no expansion in $\tau N$, therefore gives

$$
 \|E_N^TW_{e_j}(E_N^T)^*-W_{e_j}\|_{2,N}\le144\tau=:\eta,
 \quad \|B\|_{2,N}=N^{-1/2}\|B\|_{\rm HS}.               \tag{3.1}
$$

The same inequality holds in operator norm. Because $U_N^T=M_NE_N^T$,

$$
 U_N^TW_{e_j}(U_N^T)^*
       =W_{S_fe_j}+\mathcal E_j,\qquad
       \|\mathcal E_j\|_{2,N}\le\eta.
$$

For $P,Q,V$ from Section 1, exact covariance gives

$$
 PW_{e_j}P^*=\text{phase}\,E_NW_{S_f\sigma e_j}E_N^*,
$$

$$
 QW_{e_j}Q^*=\text{phase}\,W_{\sigma S_fe_j}
                      +\widetilde{\mathcal E}_j,
 \qquad \|\widetilde{\mathcal E}_j\|_{2,N}\le\eta.
$$

Consequently

$$
\begin{split}
 |\langle W_{e_j},VW_{e_j}V^*\rangle_N|
 &=|\langle PW_{e_j}P^*,QW_{e_j}Q^*\rangle_N|\\
 &\le|\langle W_{\sigma S_fe_j},
           E_NW_{S_f\sigma e_j}E_N^*\rangle_N|+\eta.
\end{split}                                                \tag{3.2}
$$

The output label is $\sigma S_fe_j$, whereas the input is
$S_f\sigma e_j$; they are not equated.

For any unitary $V$, put $c=\operatorname{Tr}V/N$. For a unitary
$W$, scalar subtraction gives

$$
 \|[V,W]\|_{2,N}\le2\|V-cI\|_{2,N}
                 =2\sqrt{1-|c|^2},
$$

while

$$
 \|[V,W]\|_{2,N}^2
       =2-2\operatorname{Re}\langle W,VWV^*\rangle_N.
$$

Choose a fixed radius $R$ so that (2.7) is at most $\varepsilon$
outside that radius for sufficiently large $N$. Equations (3.2)
then imply

$$
 \boxed{|c|^2\le\frac{1+144\tau+\varepsilon}{2}
 \quad\text{if }\max_j|\sigma S_fe_j|_N>R.}              \tag{3.3}
$$

The bound is uniform in the entire modular matrix, its character, and
all sufficiently large odd dimensions.

## 4. Bounded modular matrices and arbitrary character limits

If both centered columns of $\sigma S_f$ have norm at most $R$,
let $B$ be the integral matrix made from these columns. Its entries
are bounded by $R$, and $\det B\equiv1\pmod N$.
For $N>2R^2+1$, this forces $\det B=1$ exactly.
Thus

$$
 \Sigma=BS_f^{-1}\in\operatorname{SL}_2(\mathbb Z)
$$

is one of finitely many fixed matrices representing $\sigma$.
No commutation or reversal equation for $\Sigma$ has been assumed.

Write
$\Sigma=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}$.
Its exact ordinary-half covariance is

$$
 \Gamma Q_N(g)\Gamma^*=Q_N(g\circ\rho_N),\qquad
 \rho_N(x)=\Sigma^Tx+t_N,
$$

$$
 t_N=\kappa_N/N+(\alpha\gamma/2,\beta\delta/2)
                       \pmod{\mathbb Z^2}.                \tag{4.1}
$$

Indeed
$(\Sigma v)_1(\Sigma v)_2-v_1v_2
 \equiv\alpha\gamma v_1+\beta\delta v_2\pmod2$, since
$\det\Sigma=1$. This verifies both the parity and the character shift.

From any sequence of characters extract $t_N\to t_0$ on the torus
and put $\rho(x)=\Sigma^Tx+t_0$. The maps converge in every fixed
smooth norm. If the symbols occurring in a fixed finite product vary
with $t_N$, their smooth convergence gives operator-norm convergence
of their quantizations by the Fourier one-norm bound. Thus fixed-symbol
Egorov suffices; a separate uniform Egorov assertion is unnecessary.

The Egorov maps of $P=U_N\Gamma$ and $Q=\Gamma U_N^T$ are,
respectively, $\rho\Psi$ and $\Psi_T\rho$. This follows from the
composition rule that the map of a product $AB$ is the map of $B$
composed with the map of $A$, in the convention (2.5).
Consequently

$$
 D_N=PQ^*=U_N\Gamma\overline{U_N}\Gamma^*
$$

has the limiting Egorov map

$$
 \chi=\rho^{-1}\Psi_T^{-1}\rho\Psi.                       \tag{4.2}
$$

If $\chi=I$, then $\rho\Psi=\Psi_T\rho$, and (2.6) makes
$R_p\rho$ an affine reverser of $\Psi$:

$$
 (R_p\rho)\Psi=\Psi^{-1}(R_p\rho).                        \tag{4.3}
$$

The next section excludes this for every $\Sigma$, including $I$,
and every translation $t_0$.

## 5. Independent exact exclusion of every affine classical reverser

**Lemma.** For the actual symbol (2.1), let
$\Psi_t=S\Phi_t$, where $\Phi_t$ is the flow of $J\nabla a$.
For every $0<|t|\le10^{-12}$, no affine torus diffeomorphism
$\mathcal R(x)=Lx+u$, $L\in\operatorname{GL}_2(\mathbb Z)$,
satisfies $\mathcal R\Psi_t\mathcal R^{-1}=\Psi_t^{-1}$.

This interval is solely a range for the classical lemma. In the quantum
theorem $t=\tau/(2\pi)$ remains fixed once and for all.

### 5.1. Elementary flow bounds and exactly four fixed points

The finite support and Fourier norm in Section 2 give, in the maximum
vector norm and its induced derivative norm,

$$
 \|Z\|_\infty<120,\qquad \|DZ\|_\infty<6500.              \tag{5.1}
$$

For example the first bound is $36\pi<120$; the second is
$2(2\pi)^2 9^2=648\pi^2<6500$.
Write the natural lift $\Phi_t(x)=x+d_t(x)$. Integration and the
variational equation imply for positive and negative $t$

$$
 \|d_t\|_\infty\le120|t|,\qquad
 \|d_t-tZ\|_\infty\le390000t^2,\qquad
 \|Dd_t\|_\infty\le e^{6500|t|}-1\le6501|t|.             \tag{5.2}
$$

The middle bound follows by integrating
$|Z(\Phi_s x)-Z(x)|\le6500\cdot120|s|$. The last inequality holds
throughout $|t|\le10^{-12}$, for instance using
$e^x-1\le x/(1-x)$ at $x=6500|t|$.

Let

$$
 B=S-I=\begin{pmatrix}2&4\\2&2\end{pmatrix},\qquad
 C=B^{-1}S=\begin{pmatrix}1/2&1\\1/2&1/2\end{pmatrix}.
$$

The fixed-point displacement map factors on the torus as

$$
 \Psi_t(x)-x=B G_t(x),\qquad G_t(x)=x+C d_t(x).           \tag{5.3}
$$

Since $\|C\|=3/2$, (5.2) gives
$\|DG_t-I\|<10^4|t|<1$. The lift of $G_t$ is a global
diffeomorphism: for each $y$ the equation
$x=y-Cd_t(x)$ is a contraction on the complete space
$\mathbb R^2$, and the derivative is invertible. The lift and its
inverse respect integer translations. Thus $G_t$ is a torus
diffeomorphism.

Because $B=2\begin{pmatrix}1&2\\1&1\end{pmatrix}$,
and the latter integer matrix is unimodular, $B$ is a fourfold torus
covering. Equation (5.3) shows that $\Psi_t$ has exactly four fixed
points. Directly, $a_p=a_q=0$ whenever $q=0$ or $q=1/2$;
the flow fixes both lines pointwise. Therefore those four points are
exactly

$$
 F=\{(0,0),(0,1/2),(1/2,0),(1/2,1/2)\}.                 \tag{5.4}
$$

### 5.2. Four exact derivative matrices leave only two linear candidates

At each point of $F$, the Hessian of $a$ has only a $qq$ entry.
Writing this entry as $h_z$, direct differentiation gives

| $z$ | $125h_z/\pi^2$ |
|---|---:|
| $(0,0)$ | $-19606$ |
| $(0,1/2)$ | $-19594$ |
| $(1/2,0)$ | $24306$ |
| $(1/2,1/2)$ | $24894$ |

For a check, the $q$-only second derivatives are
$-156.8\pi^2$ and $196.8\pi^2$.
Also $[r(q+1/2)]''$ is $8\pi^2$ at $q=0$ and
$392\pi^2$ at $q=1/2$, multiplied by $-3/5$ or $3/5$
and divided by $100$. The odd $q$-term contributes zero to
these second derivatives.

Since these flow points are stationary and $J\nabla^2a$ is nilpotent
there, their derivative matrices are exact:

$$
 D_h:=D\Psi_t(z)
    =S\begin{pmatrix}1&0\\-th&1\end{pmatrix}
    =\begin{pmatrix}3-4th&4\\2-3th&3\end{pmatrix},
 \qquad \operatorname{Tr}D_h=6-4th.                     \tag{5.5}
$$

The four traces are distinct for $t\ne0$.
An affine reverser permutes the fixed points; its constant derivative
conjugates $D\Psi_t(z)$ to $D\Psi_t(\mathcal Rz)^{-1}$.
Both matrices have determinant one, so trace is unchanged by inversion.
The distinct traces force it to fix every point of (5.4) individually.
In particular $u=0$ on the torus.

The constant matrix $L$ must therefore obey
$LD_h=D_h^{-1}L$ for two distinct values of $h$.
Both sides are affine in $h$; subtracting the two equations and then
their common linear term gives

$$
 LS=S^{-1}L,\qquad
 -LS E_{21}=E_{21}S^{-1}L.                              \tag{5.6}
$$

If $L=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,
the first identity gives $b=-2c,\ d=-a$. The second additionally gives
$4a+3b=0$. Hence

$$
 L=v\begin{pmatrix}3&-4\\2&-3\end{pmatrix}=vSR_p .
$$

Since $2v$ and $3v$ are integers, $v$ is an integer. Since
$\det L=-v^2=\pm1$, it follows that

$$
 \boxed{L=SR_p\quad\hbox{or}\quad L=-SR_p.}              \tag{5.7}
$$

This simultaneous derivative calculation requires neither a Pell
classification nor differentiability of a structural conjugacy.

### 5.3. Both remaining candidates fail at the original nonzero time

Write $L=SP$, where $P=R_p$ or $P=-R_p$.
Then $PSP=S^{-1}$ and $SPS=P$.
The reversal equation for $L$ is therefore equivalent to

$$
 P\Phi_tP=\Phi_{-t}.                                   \tag{5.8}
$$

The natural lifts of the two sides agree at the origin, which is an
equilibrium. Thus equality on the torus in (5.8) would imply equality
of their lifts. Equation (5.2) would then imply

$$
 \left\|t\big(PZ(Px)+Z(x)\big)\right\|_\infty
                        \le780000t^2.                  \tag{5.9}
$$

Take $x=(1/4,0)$. For $P=R_p$, its first component is

$$
 [PZ(Px)+Z(x)]_q=2a_p(1/4,0)=\frac{4\pi}{125}.          \tag{5.10}
$$

Indeed $r(1/4+1/2)=1$ and $\sin\alpha_0=4/5$.

For $P=-R_p$, its second component is

$$
 [PZ(Px)+Z(x)]_p=-a_q(-1/4,0)-a_q(1/4,0)
                                  =\frac{8\pi}{25}.     \tag{5.11}
$$

To verify this, all even-in-$q$ terms in $a$ have cancelling
derivatives in the displayed sum. The remaining odd term is
$r(q)\sin(2\pi q)/100$. At $q=1/4$,
$r'(q)=-16\pi$, so the derivative of $r(q)\sin(2\pi q)$
is $-16\pi$. Multiplication by $-2/100$ gives (5.11).

For $0<|t|\le10^{-12}$, either (5.10) or (5.11) contradicts
(5.9), since $780000|t|<4\pi/125$. This proves the lemma.

## 6. Vanishing trace for every fixed limiting affine branch

The map in (4.2) is analytic. By Section 5 it is nonidentity for
every fixed $\Sigma$ and every $t_0$. Here is a direct trace
argument; no stationary-phase trace formula is being assumed.

For fixed smooth symbols, (2.2) and rapidly decaying Fourier tails give

$$
 Q_N(f)Q_N(g)=Q_N(fg)+o_{\rm op}(1),\quad
 Q_N(\overline f)=Q_N(f)^*,\quad
 \frac1N\operatorname{Tr}Q_N(f)\longrightarrow\int f.     \tag{6.1}
$$

For the product, use
$|e^{\pi i\omega/N}-1|\le\pi|\omega|/N$.
For the trace, every nonzero mode not divisible by $N$ has trace
zero; the remaining nonzero divisible modes have a rapidly decreasing
tail. The zero mode gives the integral.

A nonidentity analytic torus map $\chi$ has a measure-zero fixed set.
Indeed some real or imaginary component of
$e^{2\pi i(\chi_j(x)-x_j)}-1$ is a nonzero real analytic function.
Near each of its zeros, some directional derivative of finite order
does not vanish. On lines in that direction, Rolle's theorem bounds
the number of zeros in a sufficiently small convex neighborhood.
Fubini and a countable cover prove measure zero.

Choose a neighborhood $O$ of the fixed set with measure less than
$\varepsilon$. There is a finite smooth square partition
$\sum_{j=0}^J h_j^2=1$, with $h_0$ supported in $O$ and
$h_j(x)h_j(\chi x)=0$ for $j\ge1$. To construct it, cover the
compact complement of a smaller neighborhood of the fixed set by
sets disjoint from their own $\chi$-images, add $O$, and
normalize a smooth partition by the square root of its sum of squares.

Egorov for $D_N$ with the fixed limiting $\chi$, (6.1), and
cyclicity of trace give

$$
 \frac1N\operatorname{Tr}D_N
 =\sum_{j=0}^J\frac1N
       \operatorname{Tr}\big(Q_N(h_j)D_NQ_N(h_j)\big)+o(1).
$$

For $j\ge1$, the matrix inside the trace is
$Q_N(h_j(h_j\circ\chi))D_N+o_{\rm op}(1)=o_{\rm op}(1)$.
For $j=0$, the positivity of $Q_N(h_0)^2$ and unitarity of $D_N$
give

$$
 |\operatorname{Tr}(D_NQ_N(h_0)^2)|
              \le\operatorname{Tr}Q_N(h_0)^2.
$$

After division by $N$, the last bound tends to
$\int h_0^2\le |O|<\varepsilon$. Letting $\varepsilon\downarrow0$
proves $\operatorname{Tr}D_N/N\to0$.

This applies along every convergent-character subsequence in Section 4.
If convergence to zero were not uniform over characters for a fixed
$\Sigma$, a violating sequence would have a convergent $t_N$
subsequence and contradict what was just proved. Hence the convergence
is uniform over characters, and over the finite set of bounded matrices.
There is no exception for $\Sigma=I$ in this reversing problem:
Section 5 also excludes every corresponding affine reflection.

## 7. Completion, parameter boundaries, and spectral limitation

Given $\varepsilon>0$, choose the fixed radius $R$ in (3.3).
All antiunitary normalizers whose output columns leave that radius
obey (3.3). All remaining ones are in the finite fixed-matrix branch
of Section 4 and have uniformly vanishing normalized return trace
by Section 6. Taking the supremum, then the limit superior over
all odd $N$, and finally $\varepsilon\downarrow0$ proves (1.2).

For unitaries $A,B$, phase minimization gives
$\min_{|\zeta|=1}\|A-\zeta B\|_{2,N}^2
 =2-2|\operatorname{Tr}(B^*A)|/N$.
Applying this with $A=\Theta U_N\Theta^{-1}$ and $B=U_N^{-1}$
proves (1.3) and its sharper limiting version.

The fixed/moving distinction and parameter scope are as follows:

- The original $\tau=10^{-80}$ is never replaced by a sequence.
- The all-entry constant $C_\tau$ is allowed to depend on that fixed
  number; there is no quantitative dimension threshold uniform in
  $\tau$.
- Arbitrarily growing modular matrices use the exact quantum estimate,
  not Egorov for a growing symbol.
- Fixed matrices permit arbitrary characters; compactness of their
  torus translations supplies the fixed limiting map.
- The independent classical lemma is proved for
  $0<|t|\le10^{-12}$, containing the actual $t=\tau/(2\pi)$.
- No prime or subsequence restriction is imposed on $N$.

The theorem removes antiunitary Clifford reversal as a symmetry
obstruction for this exact family. It supplies no estimate on the
signed weighted products of quantum traces on times proportional to
$N$. Even the fixed pair test stated in the Round 8 ledger remains
unproved, and $H_{\rm diag}$ is not concluded.

## 8. Verification of the older $C^1$ proof and its map convention

Before the independent affine proof above was used, the complete old
$C^1$ symmetry-rigidity source was reread, together with its complete
analytic-potential input and the reverse-conjugacy construction it
references. The exact paths and current hashes are:

| Source | SHA-256 |
|---|---|
| research_round2_2026_10_20/arithmetic_classical_symmetry_rigidity.md | 434e15402b8122051aff0c45e684b53ce07e3ef518642e2b1f7b574b643cd8a3 |
| research_round2_2026_10_20/arithmetic_pressure_analytic_potential.md | 44da5eefab7cce7d7eb222fa54f027eec8a1a545b8ca0c4fd3fcf1fc7520637f |
| research_round2_2026_10_20/arithmetic_iterated_logarithmic_horizon.md, Sections 1 and 3 | 37cae903cc22d77e04ba9848f00fdfd4f19920e9c3a22381de92e965588ce8c6 |

The old source's symbol is exactly (2.1), after combining its even
$q$-terms. Its vector field is $X=J\nabla a/(2\pi)$, its time
parameter is $s$, and its map is $S\Phi_s^X$. Thus its
$s=\tau$ is exactly the present $t=\tau/(2\pi)$, with
$$
 S\Phi_\tau^X=S\Phi_{\tau/(2\pi)}^Z=\Psi.
$$
No change of symbol, no $F_+$ replacement, and no unproved conjugacy
are involved in this identification.

The old theorem applies on $0<|s|\le10^{-30}$; its analytic
potential is constructed on $|s|<10^{-16}$, so the actual parameter
satisfies both strict requirements. Its inverse convention
$\Phi_{-s}^X S^{-1}$ is exactly $\Psi^{-1}$. A diffeomorphism
reverses $\Psi$ if and only if it reverses $\Psi^{-1}$, so the
inverse convention does not alter that conclusion.

The checked old proof chain is: an explicit Green contraction gives
a homeomorphism conjugating the exact map to $S$; the analytic
invariant projective section over that fixed base gives a potential
with first variation
$(a_{pp}-2a_{qq})/(4\pi\sqrt2)$; Cauchy's formula bounds its
first-order remainder by $2\cdot10^{27}s^2$; distinct fixed-point
multipliers fix the half grid; the exact Pell calculation leaves two
possible reversing orbit actions; the period-two discrepancy has
leading coefficient $-8\pi/5$ and error at most
$8\cdot10^{27}s^2$, while the period-three discrepancy has
coefficient greater than $8$ and error at most
$12\cdot10^{27}s^2$. On $|s|\le10^{-30}$ both discrepancies
are nonzero. The analytic input uses only spatial Hölder regularity,
and its reverse-semiconjugacy proof requires
$(1-\lambda^{-1})^{-1}\|DV_s\|<1$, satisfied on its stated disk.

These observations verify the exact-map and parameter applicability
of that older result. They are recorded for provenance, not used as
an additional hypothesis: Sections 5.1--5.3 independently prove every
classical exclusion required for the new quantum theorem.
