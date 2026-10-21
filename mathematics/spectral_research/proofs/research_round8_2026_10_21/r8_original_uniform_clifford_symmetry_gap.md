> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_original_uniform_clifford_symmetry_gap.md`. Embedded SHA256: `0e4e58867f3f8745f9e3b1724fe8b269fc34cafd4dbea015e3a031495bf9d375`.
> [Thematic guide](../../topics/symmetry.md).

# Round 8: a uniform gap from every nontrivial Clifford commuting symmetry

Date: 21 October 2026. Extension of the metaplectic-centralizer theorem.

## Status and exact scope

For the prescribed $\tau=10^{-80}$, this theorem excludes approximate
projective commuting symmetries from **all unitary Clifford normalizers**
of the original finite Weyl system, uniformly along every odd dimension.
It includes arbitrary dimension-dependent finite symplectic matrices and
Weyl translations. The symplectic matrix is not assumed to commute with
the cat.

This is an operator-theoretic theorem about the original family. It does
not prove or refute $H_{\rm diag}$, and makes no claim about all possible
unitaries outside the Clifford normalizer. In particular it does not
classify arbitrary eigenbasis-dependent symmetries.

## 1. Statement and the normalizer's exact finite form

Let

$$
 W_v=T_N(l,k),\quad v=(k,l),\qquad
 S_f=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
 U_N=E_NM_N,\quad E_N=e^{i\tau NA_N}.
$$

Write $\mathcal C_N$ for the unitaries that conjugate every $W_v$
to a scalar multiple of a Weyl operator. Such a unitary has the exact form

$$
 \Gamma W_v\Gamma^*
       =e_N(\kappa\cdot v)W_{\sigma v},\qquad
 \sigma\in\operatorname{SL}_2(\mathbb Z/N\mathbb Z),\quad
 \kappa\in(\mathbb Z/N\mathbb Z)^2.                            \tag{1.1}
$$

Here is why no normalizers are omitted. Projective multiplication of the
Weyl operators identifies their labels with the additive group
$(\mathbb Z/N\mathbb Z)^2$. Conjugation induces an automorphism of that
group, hence an invertible linear matrix $\sigma$ over $\mathbb Z/N$.
Preservation of the exact Weyl commutator preserves its symplectic form,
so in dimension two $\det\sigma=1$. Preservation of the Weyl product
then makes the scalar multiplier a character; every such character is
$e_N(\kappa\cdot v)$. Conversely, symplectic covariance extends to a
$*$-automorphism of the full matrix algebra and is unitarily inner, as
proved by the matrix-unit argument in the companion metaplectic theorem.
Multiplication by a Weyl operator supplies every character.

In particular, if $\sigma=I$, then $\Gamma$ is a scalar multiple
of a single Weyl operator. Two operators with the same covariance differ
by a scalar because the Weyl operators span the full matrix algebra.

Define

$$
 R_N=\sup_{\Gamma\in\mathcal C_N\setminus\mathbb C I}
 \frac1N\left|\operatorname{Tr}(U_N\Gamma U_N^*\Gamma^*)\right|.
$$

The theorem is

$$
 \boxed{\limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}R_N
             \le\sqrt{\frac{1+600\tau}{2}}<\frac34.}           \tag{1.2}
$$

Thus for all sufficiently large odd $N$, every nonscalar
$\Gamma\in\mathcal C_N$, and every $|\zeta|=1$,

$$
 \boxed{\frac{\|U_N\Gamma U_N^*-\zeta\Gamma\|_{\rm HS}}{\sqrt N}
                 \ge\frac1{\sqrt2}.}                          \tag{1.3}
$$

More precisely, the limit inferior of the infimum of this distance is at
least $\sqrt{2-\sqrt{2+1200\tau}}>0$. No effective dimension threshold
is asserted.

## 2. The two previously proved quantum inputs

Use normalized Hilbert--Schmidt norm and inner product

$$
 \|X\|_{2,N}=N^{-1/2}\|X\|_{\rm HS},\qquad
 \langle X,Y\rangle_N=N^{-1}\operatorname{Tr}(X^*Y).
$$

The Round 4 all-entry theorem, file
`research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md`,
Sections 2--6, SHA-256
`c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`,
proves for the exact kick

$$
 \left|\langle W_w,E_NW_uE_N^*\rangle_N\right|
  \le C_*(1+|w|_N)^{-1/17}+C_*/N                              \tag{2.1}
$$

uniformly over all nonzero input and output labels and every sufficiently
large odd $N$. The **output** estimate is the one needed below. Its
finite-shift proof includes all modular-half aliases and applies without
prime, squarefree, or $7\nmid N$ restrictions.

The new, independently audited companion theorem
`r8_original_uniform_weyl_self_overlap.md`, SHA-256
`7ad8afb5fa2f9098111166b70398aad2fc95bf10de508f47ae661ec25080755d`,
proves

$$
 d_N:=\max_{v\ne0}|\langle W_v,U_NW_vU_N^*\rangle_N|
       \longrightarrow\Gamma_t<11\tau.                      \tag{2.2}
$$

Its stronger exact result identifies eventual maximizing labels
$\pm(4,-8)$ and bounds
$\left|\Gamma_t-(8\pi\sqrt{101}/25)\tau\right|\le10^8\tau^2$.

Only (2.1) is used to handle unbounded symplectic matrices. Equation (2.2)
handles the pure-translation normalizers, including translations that
shrink to zero on the classical torus. Fixed-symbol Egorov is used only
after the remaining symplectic matrices have been reduced to a finite set.

## 3. The unbounded-symplectic case is controlled directly in the quantum system

### 3.1. A fixed cat image of a basic Weyl operator changes little under the kick

The actual ordinary-half Hamiltonian symbol is

$$
\begin{split}
 a(q,p)={}&\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10\\
         &+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
\end{split}                                                    \tag{3.1}
$$

Its Fourier coefficient one-norm is less than 2, and every frequency has
$|k|+|l|\le9$. The exact Weyl commutator and
$|\sin x|\le|x|$ therefore give, for a fixed integer label $v$,

$$
 \|[A_N,W_v]\|
 \le\frac{2\pi}{N}\sum_u|\widehat a(u)|\,|\omega(u,v)|.
$$

The two cat images are $S_fe_1=(3,4)$ and $S_fe_2=(2,3)$. For
either one, $|\omega(u,S_fe_j)|\le36$ on the Fourier support.
The exact unitary Duhamel formula gives, for every odd $N$,

$$
 \boxed{\|E_NW_{S_fe_j}E_N^*-W_{S_fe_j}\|_{2,N}
             \le144\pi\tau<600\tau=:\eta.}                   \tag{3.2}
$$

The estimate concerns these fixed observables, not the operator-norm
distance of the kick from the identity.

### 3.2. Comparing the two products

For any normalizer $\Gamma$ as in (1.1), put

$$
 A=U_N\Gamma,\qquad B=\Gamma U_N,\qquad V=A^*B,
 \qquad c=N^{-1}\operatorname{Tr}V.
$$

The absolute value $|c|$ equals the normalized commutator trace in
the definition of $R_N$. Exact covariance gives

$$
 AW_{e_j}A^*=\text{phase}\cdot E_NW_{S_f\sigma e_j}E_N^*.
$$

On the other hand, (3.2), followed by conjugation with $\Gamma$, gives

$$
 BW_{e_j}B^*=
 \text{phase}\cdot W_{\sigma S_fe_j}+\mathcal E_j,
 \qquad \|\mathcal E_j\|_{2,N}\le\eta.
$$

Thus

$$
\begin{split}
 |\langle W_{e_j},VW_{e_j}V^*\rangle_N|
 &=|\langle AW_{e_j}A^*,BW_{e_j}B^*\rangle_N|\\
 &\le|\langle W_{\sigma S_fe_j},
             E_NW_{S_f\sigma e_j}E_N^*\rangle_N|+\eta.
\end{split}                                                    \tag{3.3}
$$

The input and output labels in this formula are different when
$\sigma$ does not commute with $S_f$; they have not been interchanged.

If one output label $\sigma S_fe_j$ has centered norm above a chosen
fixed radius, (2.1) bounds the right side of (3.3) by
$\varepsilon+\eta$, uniformly in $\sigma$, $\kappa$, and all
sufficiently large odd dimensions.

For any unitary $V$ and unitary $W$, subtracting
$cI$, $c=\operatorname{Tr}V/N$, gives

$$
 \|[V,W]\|_{2,N}\le2\|V-cI\|_{2,N}=2\sqrt{1-|c|^2},
$$

whereas

$$
 \|[V,W]\|_{2,N}^2
   =2-2\operatorname{Re}\langle W,VWV^*\rangle_N.
$$

Consequently,

$$
 \boxed{|c|^2\le\frac{1+600\tau+\varepsilon}{2}
 \quad\hbox{whenever}\quad
 \max_j|\sigma S_fe_j|_N>R.}                                  \tag{3.4}
$$

No classical approximation for an unbounded modular matrix occurs in this
argument.

## 4. The remaining symplectic matrices form a finite integral set

Assume $\max_j|\sigma S_fe_j|_N\le R$. Let $P$ be the integer
matrix with these centered columns. Its entries have modulus at most
$R$, and $\det P\equiv1\pmod N$. For $N>2R^2+1$, this implies
$\det P=1$ exactly. Therefore

$$
 \Sigma=PS_f^{-1}\in\operatorname{SL}_2(\mathbb Z)
$$

is one of finitely many fixed integer matrices and represents $\sigma$
modulo $N$. Unlike the centralizer theorem, no commutation equation is
imposed here.

If $\Sigma=I$, then $\Gamma$ is a scalar Weyl translation. Since
$\Gamma$ is nonscalar, (2.2) bounds its commutator trace by
$d_N<11\tau+o(1)$. It remains to show that for each fixed
$\Sigma\ne I$, the normalized commutator trace tends to zero **uniformly
over all characters** in (1.1).

## 5. Fixed matrices, varying characters, and the exact affine classical action

Write
$\Sigma=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}$.
For a fixed integral determinant-one matrix, conversion to the
ordinary-half basis gives exactly

$$
 \Gamma\widetilde W_v\Gamma^*
  =e^{2\pi i v\cdot t_N}\widetilde W_{\Sigma v},\qquad
 t_N=\kappa_N/N+(\alpha\gamma/2,\beta\delta/2)
             \pmod{\mathbb Z^2}.
$$

Indeed the parity difference of the two quadratic factors equals
$\alpha\gamma v_1+\beta\delta v_2\pmod2$. Thus, for any fixed smooth
torus symbol,

$$
 \Gamma Q_N(f)\Gamma^*=Q_N(f\circ\rho_N),\qquad
 \rho_N(x)=\Sigma^Tx+t_N.                                     \tag{5.1}
$$

From any sequence of characters choose a subsequence with
$t_N\to t_0$ on the torus, and put $\rho(x)=Lx+t_0$,
$L=\Sigma^T$. These affine maps converge in every fixed smooth norm.

Let $\Phi_t$ be the flow of $Z=J\nabla a$, with
$t=\tau/(2\pi)$, and put

$$
 S_c=S_f^T,\qquad \Psi=S_c\circ\Phi_t.
$$

The fixed-symbol finite-commutator Egorov proof in the Round 4 source,
together with the exact cat covariance, gives

$$
 U_NQ_N(f)U_N^*=Q_N(f\circ\Psi)+o_{\rm op}(1)                 \tag{5.2}
$$

for every fixed smooth $f$. The same holds for inverse operators.
The proof uses the exact sine-versus-linear commutator multiplier with
error $O_f(N^{-2})$; all trace aliases have smooth Fourier tails.

Equations (5.1)--(5.2) imply Egorov for
$D_N=U_N\Gamma U_N^*\Gamma^*$ with the limiting map

$$
 \chi=\rho^{-1}\circ\Psi^{-1}\circ\rho\circ\Psi.             \tag{5.3}
$$

There is no hidden uniform Egorov assumption for growing matrices or
characters. Here $\Sigma$ is fixed. If the smooth symbols produced by
$t_N$ vary, they converge in every fixed derivative norm; their
quantizations converge in operator norm by the Fourier coefficient
one-norm bound. Combining that convergence with Egorov for their fixed
limit gives (5.3).

The key remaining fact is that $\chi$ is nonidentity for every
$\Sigma\ne I$ and every $t_0$.

## 6. No nonscalar fixed affine action commutes with the original classical map

Suppose $\rho\Psi=\Psi\rho$. Comparing the induced integer actions
on the fundamental group gives $LS_c=S_cL$. Thus if $\Sigma$ is
not a centralizer of $S_f$, commutation is already impossible.

Assume now that $L$ commutes with $S_c$. Since $S_c$ has two
distinct real eigenvalues, $L$ is diagonal in the same real eigenbasis.
With determinant one it is either $I$, $-I$, or hyperbolic.
The case $I$ was removed by the pure-Weyl argument.

Write the lift $\Phi_t(x)=x+d_t(x)$. The commutation equation on the
torus gives one constant integer vector $m$ such that

$$
 (S_c-I)t_0+S_c\big(d_t(Lx+t_0)-Ld_t(x)\big)=m.               \tag{6.1}
$$

### 6.1. Hyperbolic linear part

Subtract (6.1) at two points and iterate the affine map in both directions:

$$
 L^n(d_t(x)-d_t(y))
       =d_t(\rho^n x)-d_t(\rho^n y),\qquad n\in\mathbb Z.
$$

The right side is bounded. Hyperbolicity forces $d_t$ to be constant.
For the actual symbol $\nabla a(0,0)=0$, so $\Phi_t(0)=0$ and the
constant would be zero. But the exact coefficient
$a_{1,0}=1/20-i/200$, together with

$$
 \|d_t-tZ\|_\infty\le78000t^2,\qquad
 |\widehat Z_2(1,0)|\ge\pi/10,
$$

shows that $d_t\not\equiv0$ at the prescribed $t$. These explicit
flow bounds are proved in Section 4 of the companion self-overlap file.
No condition involving $\|L\|t$ is used.

### 6.2. The linear part $-I$, with every possible translation

The mean of the lifted Hamiltonian displacement is exactly zero:

$$
 \int_{\mathbb T^2}d_t(x)\,dx
  =\int_0^t\int_{\mathbb T^2}Z(\Phi_s(x))\,dx\,ds
  =t\int_{\mathbb T^2}J\nabla a(x)\,dx=0.                    \tag{6.2}
$$

For justification, $\operatorname{div}(J\nabla a)=0$; the variational
Jacobian equation makes $\Phi_s$ preserve Lebesgue measure. The last
integral vanishes by periodicity. Since $\rho$ also preserves Lebesgue
measure, integrating (6.1) gives

$$
 (S_c-I)t_0=m\in\mathbb Z^2.
$$

Here
$S_c-I=2\begin{pmatrix}1&2\\1&1\end{pmatrix}$, and the
matrix after the factor 2 is unimodular. Hence

$$
 2t_0\in\mathbb Z^2.                                         \tag{6.3}
$$

Equation (6.1) now reduces, for $L=-I$, to
$d_t(-x+t_0)=-d_t(x)$. We exclude all four half-period translations
with a single Fourier coefficient.

The mean of $r(q+1/2)$ is 1, so the exact coefficient in (3.1) is

$$
 a_{0,1}=\frac{e^{-i\alpha_0}}{200}
        =\frac{-3-4i}{1000}.
$$

Since $Z_q=a_p$, the displacement coefficient obeys

$$
 \boxed{\widehat{d_{t,q}}(0,1)
  =\frac{\tau(4-3i)}{1000}+\mathcal R,\qquad
  |\mathcal R|\le2200\tau^2.}                                \tag{6.4}
$$

This follows from $d_t=tZ+O_\infty(78000t^2)$,
$t=\tau/(2\pi)$, and $\pi>3$. If $c$ denotes the coefficient
in (6.4), the shifted oddness would require

$$
 c+e^{-2\pi i(t_0)_p}\overline c=0.
$$

By (6.3) the scalar is 1 or -1. For 1, the left side has leading term
$8\tau/1000$; for -1, its leading term is $-6i\tau/1000$.
In either case the error is at most $4400\tau^2$, so its modulus is
at least $6\tau/1000-4400\tau^2>0$. This is a contradiction.

We have proved that (5.3) is nonidentity for every fixed $\Sigma\ne I$
and every translation limit $t_0$.

## 7. Fixed limiting canonical commutators have vanishing normalized trace

Here are the details of the trace step, included to avoid invoking an
unproved semiclassical trace formula.

For fixed smooth symbols, the exact Weyl product and rapidly decreasing
Fourier coefficients give

$$
 Q_N(f)Q_N(g)=Q_N(fg)+o_{\rm op}(1),\quad
 Q_N(\overline f)=Q_N(f)^*,\quad
 N^{-1}\operatorname{Tr}Q_N(f)\to\int f.                       \tag{7.1}
$$

The product error follows from
$|e^{\pi i\omega/N}-1|\le\pi|\omega|/N$; the trace statement follows
by retaining and then estimating all modes divisible by $N$.

A nonidentity analytic torus map $\chi$ has a measure-zero fixed set.
To see this without a separate theorem, take a nonzero real analytic
component of $e^{2\pi i(\chi_j(x)-x_j)}-1$. At any zero it has a
nonzero derivative of finite order, since otherwise analytic continuation
would make it identically zero. A suitable directional derivative stays
nonzero in a small neighborhood. Rolle's theorem bounds the number of
zeros on each line in that direction, and Fubini gives measure zero.
A countable cover completes the argument.

Choose an open neighborhood $O$ of the fixed set with measure below
$\varepsilon$. A finite smooth square partition
$\sum_{j=0}^Jh_j^2=1$ can be chosen with
$\operatorname{supp}h_0\subset O$ and
$h_j(x)h_j(\chi x)=0$ for $j\ge1$. One constructs it from small
sets disjoint from their own $\chi$-images and normalizes a smooth
partition by the square root of the sum of its squares.

If unitary $D_N$ obeys Egorov for this limiting $\chi$, then (7.1)
and cyclic trace give

$$
 N^{-1}\operatorname{Tr}D_N
 =\sum_{j=0}^J N^{-1}\operatorname{Tr}
             (Q_N(h_j)D_NQ_N(h_j))+o(1).
$$

For $j\ge1$, Egorov and (7.1) make the matrix inside the trace
$Q_N(h_j(h_j\circ\chi))D_N+o_{\rm op}(1)=o_{\rm op}(1)$.
For $j=0$, positivity of $Q_N(h_0)^2$ and unitarity of $D_N$
give

$$
 |\operatorname{Tr}(D_NQ_N(h_0)^2)|
       \le\operatorname{Tr}Q_N(h_0)^2.
$$

After division by $N$, its limit is $\int h_0^2\le|O|<\varepsilon$.
Letting $\varepsilon\downarrow0$ proves

$$
 N^{-1}\operatorname{Tr}D_N\to0.                              \tag{7.2}
$$

Apply this to the convergent-character subsequence in Section 5. The map
$\chi$ is analytic and nonidentity by Section 6, so (7.2) holds.
If uniform convergence over characters for a fixed $\Sigma\ne I$
were false, a violating sequence would have such a convergent translation
subsequence, a contradiction. The convergence is therefore uniform over
all characters, and hence over the finite set of matrices in Section 4.

## 8. Completion and precise limitation

Fix $\varepsilon>0$, then choose $R$ for the quantum tail. Every
normalizer is in one of three classes:

1. An output column $\sigma S_fe_j$ lies outside the radius, and (3.4)
   bounds its squared commutator trace by
   $(1+600\tau+\varepsilon)/2$.
2. Its matrix belongs to the bounded finite set with $\Sigma\ne I$,
   and Section 7 makes the commutator trace uniformly $o(1)$.
3. Its symplectic matrix is the identity and it is a nontrivial Weyl
   translation, bounded by (2.2).

Taking the supremum, the limit superior in odd dimensions, and then
$\varepsilon\downarrow0$ proves (1.2), since
$11\tau<\sqrt{(1+600\tau)/2}$. For unitaries, minimizing over the
scalar phase gives exactly

$$
 \min_{|\zeta|=1}\|U_N\Gamma U_N^*-\zeta\Gamma\|_{2,N}^2
 =2-\frac2N|\operatorname{Tr}(U_N\Gamma U_N^*\Gamma^*)|.
$$

This proves (1.3) and the stated limiting distance.

The result closes the approximate commuting-symmetry route for the whole
finite Clifford group, including growing symplectic matrices and
translations on arbitrary composite-modulus subsequences. It does not
estimate the coherent weighted trace sums at times of order $N$ and
therefore supplies no missing implication to $H_{\rm diag}$.
