> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_original_uniform_metaplectic_symmetry_gap.md`. Embedded SHA256: `bd607591e7d31980d828762bf4ab01fd7e84b418a8c81cb48bc8e896f86bdc78`.
> [Thematic guide](../../topics/symmetry.md).

# Round 8: a uniform gap from metaplectic commuting symmetries

Date: 21 October 2026. Original-family branch.

## Status

This theorem concerns the exact $U_N=e^{i\tau NA_N}M_N$, with the fixed
$\tau=10^{-80}$, along **all odd dimensions**. It excludes approximate
projective commuting symmetries implemented by any nonidentity finite
metaplectic element centralizing the cat. The finite symplectic matrix may
depend arbitrarily on $N$, and its entries may grow with $N$.

The proof does not infer commutation of exponentials from a bound for
commutators of their generators. It uses the exact low-Weyl commutator,
the already proved all-entry tail estimate for the actual exponential,
and a compactness argument for the remaining bounded symplectic matrices.
For the latter, a fixed-time trace-vanishing lemma is proved below from
finite-quantization estimates and a smooth partition of unity.

This result does not prove or refute $H_{\rm diag}$. It applies to single
metaplectic group elements, including the usual Hecke group elements in
the centralizer, rather than arbitrary linear combinations in a Hecke
operator algebra.

## 1. Exact statement

Write

$$
 W_v=T_N(l,k),\quad v=(k,l),\qquad
 S_f=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
 E_N=e^{i\tau NA_N}.
$$

For odd $N$, let $\sigma\in\operatorname{SL}_2(\mathbb Z/N\mathbb Z)$
commute with $S_f$, and let $\Gamma_{N,\sigma}$ be a unitary
implementing its **exact** Weyl covariance,

$$
 \Gamma_{N,\sigma}W_v\Gamma_{N,\sigma}^*=W_{\sigma v}.
                                                                  \tag{1.1}
$$

Any scalar choice for the implementer gives the same quantities below.
Such an implementer exists for every stated $\sigma$. Indeed, the Weyl
operators form a basis of the full matrix algebra, and their exact product
law shows that $W_v\mapsto W_{\sigma v}$ extends to a unital
$*$-automorphism: $\det\sigma=1$ preserves the symplectic form.
Every such automorphism of the full matrix algebra is unitarily inner.
An elementary proof is to apply it to the matrix units: the $N$ diagonal
units become mutually orthogonal nonzero projections summing to $I$,
and hence each has rank one; the off-diagonal units determine compatible
phases of their unit range vectors. The matrix of these vectors implements
the automorphism. The implementer is unique up to a scalar because the
Weyl operators span the algebra.

For every implementer satisfying (1.1), define

$$
 r_N(\sigma)=\frac1N\left|\operatorname{Tr}
   (U_N\Gamma_{N,\sigma}U_N^*\Gamma_{N,\sigma}^*)\right|.
$$

The theorem is

$$
 \boxed{\limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}
   \sup_{\substack{\sigma S_f=S_f\sigma\\\sigma\ne I}}
       r_N(\sigma)
       \le\sqrt{\frac{1+144\tau}{2}}<\frac34.}                 \tag{1.2}
$$

Consequently, for every sufficiently large odd $N$, every such
nonidentity $\sigma$, and every scalar phase $\zeta$,

$$
 \boxed{\frac{\|U_N\Gamma_{N,\sigma}U_N^*
                   -\zeta\Gamma_{N,\sigma}\|_{\rm HS}}{\sqrt N}
           \ge\frac1{\sqrt2},\qquad |\zeta|=1.}                \tag{1.3}
$$

The limiting lower bound is stronger:

$$
 \liminf_{\substack{N\to\infty\\N\ \mathrm{odd}}}
 \inf_{\substack{\sigma S_f=S_f\sigma\\\sigma\ne I}}
 \inf_{|\zeta|=1}
 \frac{\|U_N\Gamma_{N,\sigma}U_N^*
                   -\zeta\Gamma_{N,\sigma}\|_{\rm HS}}{\sqrt N}
 \ge\sqrt{2-\sqrt{2+288\tau}}>0.                              \tag{1.4}
$$

No effective dimension threshold is asserted.

## 2. Reduction to the kick and an elementary unitary inequality

The covariance of $M_N$ and (1.1) show that
$M_N\Gamma_{N,\sigma}M_N^*$ and $\Gamma_{N,\sigma}$ have identical
actions on every Weyl operator. Their quotient is scalar: commuting with
all diagonal Weyl characters forces an operator to be diagonal, and
commuting with the cyclic shift makes its diagonal constant. Thus

$$
 M_N\Gamma_{N,\sigma}M_N^*=\eta_{N,\sigma}\Gamma_{N,\sigma},
 \qquad |\eta_{N,\sigma}|=1.
$$

Put

$$
 G_N=\Gamma_{N,\sigma}E_N\Gamma_{N,\sigma}^*,\qquad
 V_N=E_N^*G_N,\qquad c_N=N^{-1}\operatorname{Tr}V_N.
$$

Then

$$
 r_N(\sigma)=|c_N|.                                          \tag{2.1}
$$

In this note $\|X\|_{2,N}=N^{-1/2}\|X\|_{\rm HS}$. For any unitary
$V$, with $c=N^{-1}\operatorname{Tr}V$, and any unitary $W$,

$$
 \|[V,W]\|_{2,N}
  =\|[V-cI,W]\|_{2,N}
  \le2\|V-cI\|_{2,N}=2\sqrt{1-|c|^2}.                         \tag{2.2}
$$

Also

$$
 \|[V,W]\|_{2,N}^2
 =2-2\operatorname{Re}\langle W,VWV^*\rangle_N,
 \quad \langle X,Y\rangle_N=N^{-1}\operatorname{Tr}(X^*Y).
                                                                  \tag{2.3}
$$

These identities retain the scalar part of $V$ exactly; no estimate for
the logarithm of a unitary is used.

## 3. A uniform estimate whenever a symplectic column escapes

### 3.1. The exact kick moves a basic Weyl observable by at most $144\tau$

Use the ordinary-half basis $\widetilde W_v=(-1)^{kl}W_v$. The actual
Hamiltonian is $A_N=Q_N(a)$, with the symbol (1.1) in the companion file
`r8_original_uniform_weyl_self_overlap.md`. Its Fourier coefficient
one-norm is less than 2 and its support satisfies $|k|+|l|\le9$.

For $e_1=(1,0)$ or $e_2=(0,1)$, the exact Weyl product and
$|\sin x|\le|x|$ give

$$
 \|[A_N,W_{e_j}]\|
 \le\frac{2\pi}{N}\sum_u|\widehat a(u)|\,|\omega(u,e_j)|
 \le\frac{36\pi}{N}<\frac{144}{N}.                            \tag{3.1}
$$

The modular-half signs do not affect these absolute values. This estimate
holds for every odd $N$, including dimensions in which Fourier modes
alias. Duhamel's formula, using unitarity of the exact propagator, yields

$$
 \boxed{\|E_NW_{e_j}E_N^*-W_{e_j}\|_{2,N}\le144\tau=:\eta.}    \tag{3.2}
$$

The factor $N$ in the exponent is canceled here by an **exact** Weyl
commutator factor of order $N^{-1}$; this is not a claim that $E_N$
itself is close to the identity.

### 3.2. The previously proved tail applies at every modulus

The Round 4 theorem
`research_round4_2026_10_21/root_all_entry_and_arbitrary_weyl_routes.md`,
Sections 2--6, has SHA-256
`c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`.
For the exact $E_N$, it proves uniformly over every nonzero label

$$
 \left|N^{-1}\operatorname{Tr}(W_u^*E_NW_uE_N^*)\right|
  \le C_*(1+|u|_N)^{-1/17}+C_*/N.                             \tag{3.3}
$$

The companion self-overlap proof describes its finite-shift construction,
alias treatment, and independent audit. Equation (3.3) is used as the
proved quantum input; no classical mixing theorem substitutes for it.

Suppose for one $j$ that the centered label
$u=\sigma^{-1}e_j$ has norm larger than a fixed radius $R$. Exact
covariance gives

$$
 \left|\langle W_{e_j},G_NW_{e_j}G_N^*\rangle_N\right|
 =\left|\langle W_u,E_NW_uE_N^*\rangle_N\right|
 \le\varepsilon                                             \tag{3.4}
$$

once $R$, then $N$, are sufficiently large depending on
$\varepsilon$. The estimates are uniform in $\sigma$.

For $V_N=E_N^*G_N$, equations (3.2)--(3.4) imply

$$
\begin{split}
 \left|\langle W_{e_j},V_NW_{e_j}V_N^*\rangle_N\right|
 &=\left|\langle E_NW_{e_j}E_N^*,G_NW_{e_j}G_N^*\rangle_N\right|\\
 &\le\varepsilon+\eta.
\end{split}
$$

Combining (2.2)--(2.3) gives the key quantitative implication

$$
 \boxed{r_N(\sigma)^2\le\frac{1+\eta+\varepsilon}{2}
 \quad\hbox{if}\quad
 \max_j|\sigma^{-1}e_j|_N>R.}                                 \tag{3.5}
$$

This controls the symplectic matrices with growing columns without any
uniform classical approximation for those matrices.

## 4. Bounded columns reduce to finitely many integral centralizers

Suppose $\max_j|\sigma^{-1}e_j|_N\le R$, and form the integer matrix
$P$ whose columns are these centered representatives. Its entries are
bounded by $R$. Since it represents $\sigma^{-1}$,

$$
 \det P\equiv1\pmod N,\qquad PS_f-S_fP\equiv0\pmod N.
$$

For $N>2R^2+1$, the determinant congruence forces $\det P=1$.
Each entry of the commutator is bounded by $14R$, so for $N>14R$
that congruence is the exact integer equation

$$
 PS_f=S_fP.
$$

Thus the bounded-column case consists of a **finite** collection of fixed
matrices $P\in\operatorname{SL}_2(\mathbb Z)$ commuting with $S_f$.
Their inverses $\sigma=P^{-1}$ are fixed integral matrices as well.
The identity is absent because the theorem excludes $\sigma\equiv I$.

It remains to prove for each fixed nonidentity integral centralizer that

$$
 N^{-1}\operatorname{Tr}(E_N^*\Gamma_{N,\sigma}E_N
                                      \Gamma_{N,\sigma}^*)\to0.
                                                                  \tag{4.1}
$$

No uniformity over infinitely many fixed integral matrices is needed in
this step: $R$ has already been fixed.

## 5. Fixed metaplectic covariance includes a half-period translation

Let
$\sigma=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}
\in\operatorname{SL}_2(\mathbb Z)$ be fixed. Changing from the original
modular Weyl basis to the ordinary-half basis gives exactly

$$
 \Gamma_{N,\sigma}\widetilde W_v\Gamma_{N,\sigma}^*
  =(-1)^{\alpha\gamma v_1+\beta\delta v_2}
       \widetilde W_{\sigma v}.                               \tag{5.1}
$$

Indeed
$(\sigma v)_1(\sigma v)_2-v_1v_2\equiv
\alpha\gamma v_1+\beta\delta v_2\pmod2$, since
$\alpha\delta-\beta\gamma=1$. Therefore, for every smooth torus symbol,

$$
 \Gamma_{N,\sigma}Q_N(f)\Gamma_{N,\sigma}^*
  =Q_N(f\circ\rho),\quad
 \rho(x)=\sigma^Tx+\xi\pmod{\mathbb Z^2},\quad
 \xi=(\alpha\gamma/2,\beta\delta/2).                           \tag{5.2}
$$

The affine correction is retained throughout the proof. Treating this
covariance as a purely linear action for all integral matrices would be
incorrect in the specified modular quantization.

In the fixed centralizer under consideration the correction is in fact
integral. Directly solving $\sigma S_f=S_f\sigma$ gives
$\sigma=\begin{pmatrix}a&b\\2b&a\end{pmatrix}$, with
$a^2-2b^2=1$. Reduction modulo 4 forces $b$ even and $a$ odd, so
$\sigma\equiv I\pmod2$ and $\xi\in\mathbb Z^2$. The proof below
allows the general affine notation as well, to keep the covariance issue
explicit; in this centralizer $\rho(x)=\sigma^Tx$ on the torus.

For the exact flow $\Phi_t$ of the original ordinary-half symbol,
$t=\tau/(2\pi)$, the finite commutator and Duhamel argument in the
Round 4 source proves, for each fixed smooth $f$,

$$
 E_NQ_N(f)E_N^*=Q_N(f\circ\Phi_t)+o_{\rm op}(1).               \tag{5.3}
$$

The proof for arbitrary fixed smooth $f$ is the same multiplier
estimate as for a fixed character: the finite Fourier support of $a$
and a convergent third weighted Fourier norm of the transported $f$
bound the commutator error by $O_f(N^{-2})$. Negative time is handled
by $-a$. Combining (5.2)--(5.3) shows that $V_N$ in (4.1) obeys
Egorov with the fixed analytic map

$$
 \chi=\rho^{-1}\circ\Phi_t\circ\rho\circ\Phi_t^{-1}.           \tag{5.4}
$$

We prove that $\chi$ is nonidentity, and then prove trace vanishing
without invoking an unverified trace formula.

## 6. No nonidentity fixed integral centralizer commutes with the kick flow

Set $S_c=S_f^T$. Because $\sigma$ commutes with $S_f$, its
transpose $L=\sigma^T$ commutes with $S_c$. The latter has two
distinct real eigenvalues $3\pm2\sqrt2$. Hence $L$ is diagonal in
the same real eigenbasis. Its eigenvalues are $\mu,\mu^{-1}$.
If they have modulus one, they are both 1 or both -1 and diagonalizability
gives $L=I$ or $L=-I$. Otherwise $L$ is hyperbolic.

### 6.1. Hyperbolic affine maps

Write the lift of the kick flow as $\Phi_t(x)=x+d_t(x)$, where $d_t$
is bounded and periodic. Suppose the affine map $\rho(x)=Lx+\xi$
commuted with this flow on the torus. The lifted difference is integer
valued and continuous, hence for one constant integer vector $m$,

$$
 d_t(Lx+\xi)-Ld_t(x)=m.
$$

Subtract the identities at $x$ and $y$ and iterate in both positive
and negative time under the affine map. This gives

$$
 L^n(d_t(x)-d_t(y))
  =d_t(\rho^n x)-d_t(\rho^n y),\qquad n\in\mathbb Z.
$$

The right side is bounded. Hyperbolicity of $L$ therefore forces
$d_t(x)=d_t(y)$ for every pair $x,y$; the displacement is constant.

For the actual symbol, $\nabla a(0,0)=0$, directly from the displayed
formula for $a$, so $\Phi_t(0)=0$. Thus a constant displacement
would be zero and $\Phi_t$ would be the identity. It is not: the
explicit bounds in Section 4 of the companion self-overlap file give

$$
 \|d_t-tZ\|_\infty\le78000t^2,
 \qquad Z=J\nabla a,
$$

and $|\widehat Z_2(1,0)|=2\pi|a_{1,0}|\ge\pi/10$. Therefore
$d_t$ has a nonzero Fourier coefficient at $(1,0)$ for the fixed
$t<10^{-12}$. This is a contradiction.

### 6.2. The remaining case $L=-I$

For $\sigma=-I$, the affine correction in (5.2) is zero. Commutation
would imply $d_t(-x)=-d_t(x)$. But the exact coefficient
$a_{1,0}=1/20-i/200$ gives

$$
 \widehat Z_2(1,0)=-\frac\pi{100}-i\frac\pi{10},\qquad
 \widehat Z_2(1,0)+\widehat Z_2(-1,0)=-\frac\pi{50}.
$$

The same flow remainder bounds the corresponding coefficient of
$d_t(x)+d_t(-x)$ below in modulus by

$$
 \frac\pi{50}t-156000t^2>0.
$$

Thus $-I$ does not commute with the kick flow. The case $L=I$
would mean $\sigma=I$, already excluded. This proves that (5.4) is
nonidentity for every fixed matrix needed in Section 4.

## 7. A self-contained fixed-time trace-vanishing lemma

We use three elementary finite-quantization properties for fixed smooth
symbols:

$$
 Q_N(f)Q_N(g)=Q_N(fg)+o_{\rm op}(1),\quad
 Q_N(\overline f)=Q_N(f)^*,\quad
 N^{-1}\operatorname{Tr}Q_N(f)\to\int f.                       \tag{7.1}
$$

For completeness, the product assertion follows by subtracting the exact
Weyl convolution from the ordinary convolution and applying
$|e^{\pi i\omega/N}-1|\le\pi|\omega|/N$; the fixed weighted Fourier
one-norms are finite. The adjoint assertion is exact. The trace assertion
follows because all Weyl modes except those divisible by $N$ have zero
trace, and all nonzero divisible modes have rapidly decreasing Fourier
coefficients. These arguments retain the original finite aliases.

**Lemma.** Suppose unitary $V_N$ satisfies

$$
 V_NQ_N(f)V_N^*=Q_N(f\circ\chi)+o_{\rm op}(1)
$$

for each fixed smooth $f$, where $\chi$ is a fixed smooth torus
diffeomorphism whose fixed-point set has Lebesgue measure zero. Then
$N^{-1}\operatorname{Tr}V_N\to0$.

**Proof.** Let $O$ be an open neighborhood of the fixed-point set with
measure less than $\varepsilon$. Outside $O$, choose a finite cover
by small open sets $U_j$ such that
$U_j\cap\chi^{-1}(U_j)=\varnothing$. A smooth partition of unity,
normalized by the square root of the sum of its squares, gives real
smooth functions $h_0,h_1,\ldots,h_J$ satisfying

$$
 \sum_{j=0}^J h_j^2=1,\qquad
 \operatorname{supp}h_0\subset O,\qquad
 h_j(x)h_j(\chi x)=0\quad(j\ge1).
$$

By (7.1) and cyclicity of trace,

$$
 N^{-1}\operatorname{Tr}V_N
 =\sum_{j=0}^J N^{-1}\operatorname{Tr}
                  (Q_N(h_j)V_NQ_N(h_j))+o(1).
$$

For $j\ge1$, Egorov and (7.1) make the matrix inside this trace
$Q_N(h_j(h_j\circ\chi))V_N+o_{\rm op}(1)=o_{\rm op}(1)$.
Its normalized trace therefore vanishes. For $j=0$,

$$
 |\operatorname{Tr}(Q_N(h_0)V_NQ_N(h_0))|
 =|\operatorname{Tr}(V_NQ_N(h_0)^2)|
 \le\operatorname{Tr}Q_N(h_0)^2.
$$

The inequality follows by diagonalizing the positive matrix $Q_N(h_0)^2$
and using unitarity of $V_N$. After normalization, (7.1) bounds the
limit superior by $\int h_0^2\le|O|<\varepsilon$. Let
$\varepsilon\downarrow0$. This proves the lemma.

For the analytic nonidentity map $\chi$ in (5.4), its fixed set has
measure zero. Here is an elementary justification of the analytic step.
At least one real or imaginary component of
$e^{2\pi i(\chi_j(x)-x_j)}-1$ is a nonzero analytic function. At each
zero of a nonzero analytic function there is a finite directional
derivative that is nonzero; otherwise its power series vanishes locally,
and analytic continuation makes it identically zero. In a small
neighborhood that derivative stays bounded away from zero. On each line
in that direction, repeated Rolle's theorem bounds the number of zeros
by the derivative order. Fubini's theorem makes that local zero set
measure zero. A countable cover proves the assertion globally.

Applying the lemma to (5.4) proves (4.1).

## 8. Completion of the uniform gap

Fix $\varepsilon>0$. Choose $R$, then a dimension threshold, so
that (3.4) follows from (3.3) whenever a column escapes the radius. In that
case (3.5) applies. If both columns stay inside the radius, Section 4
reduces the problem to finitely many fixed integral centralizers. For
each of them, Section 7 gives $r_N(\sigma)\to0$, uniformly over this
finite collection. Hence

$$
 \limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}
 \sup_{\substack{\sigma S_f=S_f\sigma\\\sigma\ne I}}r_N(\sigma)
 \le\sqrt{\frac{1+144\tau+\varepsilon}{2}}.
$$

Let $\varepsilon\downarrow0$. This proves (1.2). Finally,

$$
 \min_{|\zeta|=1}
 \|U_N\Gamma U_N^*-\zeta\Gamma\|_{2,N}^2=2-2r_N(\sigma)
$$

proves (1.3)--(1.4).

The two stages are essential: the quantum coefficient tail handles
unbounded modular matrices, and fixed-symbol Egorov is applied only after
the symplectic matrices have been reduced to a finite set. There is no
unproved Egorov estimate with a growing symplectic matrix.

## 9. What this closes, and what remains open

The result excludes an infinite approximate commuting-symmetry mechanism
from every individual cat-centralizing metaplectic element, including
ones on prime-power or CRT subsequences whose matrix entries grow with
dimension. It strengthens finite nonvanishing to an order-one normalized
HS separation, for the actual fixed kick.

It does not exclude a general unitary in the linear span of these group
elements, an eigenbasis-dependent quantum symmetry, a long-time
recurrence, or an obstruction caused by spectral correlations without
such a symmetry. In particular, the first unproved weighted pair
form-factor estimate and the all-order $H_{\rm diag}$ problem are
unchanged. No $\Delta_{k,N}\to0$ conclusion follows from (1.2).
