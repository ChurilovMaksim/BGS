> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md`. Embedded SHA256: `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b`.
> [Thematic guide](../../topics/classical_trace.md).

# Exact odd-dimensional trace identities and algebraic rigidity

Date: 20 October 2026. Independent audit and reconstruction by the global-proof auditor.

This document records proofs that can be reconstructed from the exact definitions below. Earlier scratch files became inaccessible and then disappeared when the execution environment reset; they have not been used as evidence for the conclusions in this document.

## 1. Scope and status

The following statements are proved here.

1. The explicitly normalized plane metaplectic operator descends to the specified finite matrix with the exact scalar $e_8(1-3N)$, for every odd positive integer $N$.
2. The corrected plane symbol descends to the specified finite Hamiltonian. In particular, the half-period shift in its mixed term is necessary with the finite modular Weyl convention used here.
3. For every fixed odd $N$ and every integer $m\geq1$, the finite trace equals a finite sum of absolutely defined coherent-state plane sector traces. The normalization, lattice character, and coset multiplicities are explicit.
4. The same sector traces have a well-defined real Abel/Fresnel kernel interpretation. The exchanges of the word expansion, lattice sum, and regularized integrals are justified.
5. When a generating function for the small-time classical map is used, its deck law gives well-defined sector action phases and exact cyclic invariance.
6. For every odd $N\geq3$, $N\neq7$, every $m\geq1$, and every nonzero algebraic parameter $z$, the matrix $(e^{izNA_N}M_N)^m$ is nonscalar.
7. For every odd positive $N$, every $m\geq1$, and every algebraic $z$, the trace $\operatorname{Tr}(e^{izNA_N}M_N)^m$ is nonzero.

The last two statements use the Lindemann–Weierstrass theorem in its exact linear-independence form. Their proofs give no useful quantitative lower bound on a trace or a distance from a scalar.

This document does not prove the proposed resummed periodic-point formula with a uniformly decaying error. In particular, it does not prove the exact analytic amplitude construction, a trace-norm estimate after a bounded contour deformation, or the claimed bound $2(0.421)^m$. The sector identity below is an exact input to such a result, not a substitute for those analytic estimates. The deterministic CUE/Hdiag target remains unresolved.

Universal simple spectrum is false if $N=7$ is included. Simplicity for the remaining dimensions is not proved here.

## 2. Exact definitions and conventions

Write
$$
 e_N(s)=\exp(2\pi i s/N),\qquad
 h=(2\pi N)^{-1},\qquad
 \tau=10^{-80},\qquad t=\tau/(2\pi).
$$
Here $N$ is odd. Modular fractions such as $\overline2,\overline4,\overline8$ denote inverses in $\mathbb Z/N\mathbb Z$; ordinary fractions inside real phases mean ordinary real division.

The finite Hilbert space is $\mathbb C^N$, indexed by $x\in\mathbb Z/N\mathbb Z$, with its usual inner product. The finite Weyl operators use a plus shift:
$$
 (T_N(a,b)u)(x)=e_N\!\left(b(x+\overline2 a)\right)u(x+a).
 \tag{2.1}
$$
All indices and the argument of $e_N$ in (2.1) are modular. Set
$$
 M_{N,xy}=N^{-1/2}e_N\!\left[-\overline8(3x^2-2xy+3y^2)\right].
 \tag{2.2}
$$

Let
$$
 r(q)=(1-\cos14\pi q)(1+\cos2\pi q),
 \qquad e^{i\alpha_0}=(-3+4i)/5,
$$
and define the finite Fourier polynomial
$$
 f(q,p)=\cos14\pi q+\frac{r(q)}{10}
       +\frac{r(q)\sin2\pi q}{100}
       +\frac{r(q)\cos(2\pi p-\alpha_0)}{100}.
 \tag{2.3}
$$
If
$$
 f(q,p)-\frac1{10}=\sum_{k,l}c_{kl}e^{2\pi i(kq+lp)},
$$
then
$$
 A_N=\sum_{k,l}c_{kl}T_N(l,k),\qquad
 U_N(z)=e^{izNA_N}M_N,\qquad U_N=U_N(\tau).
 \tag{2.4}
$$
Only finitely many $c_{kl}$ are nonzero. They are algebraic numbers. The symmetry $c_{-k,-l}=\overline{c_{kl}}$, together with $T_N(a,b)^*=T_N(-a,-b)$, proves that $A_N$ is Hermitian.

The plane physical Weyl operators are
$$
 (\mathcal T_{(u,v)}\psi)(q)
 =e^{iv(q-u/2)/h}\psi(q-u).
 \tag{2.5}
$$
For an integer vector $n=(n_q,n_p)$, set
$$
 R_n=(-1)^{n_qn_p}\mathcal T_n.
 \tag{2.6}
$$
The classical linear matrix is
$$
 L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
 \qquad
 S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
 \tag{2.7}
$$
The symbol $S$ in (2.7) acts on the finite plus-shift Weyl indices; $L$ acts on physical $(q,p)$ coordinates. Their differing signs are part of the convention, not interchangeable notation.

The chosen plane metaplectic operator has kernel
$$
 K_L(Q,q)=C_h e^{iF_0(Q,q)/h},
 \quad
 C_h=\frac{e^{i\pi/4}}{\sqrt{8\pi h}}
     =e_8(1)\frac{\sqrt N}{2},
 \quad
 F_0(Q,q)=-\frac{3Q^2-2Qq+3q^2}{8}.
 \tag{2.8}
$$
The generating equations $p=-\partial_qF_0$, $P=\partial_QF_0$ give $(Q,P)=L(q,p)$. The ordinary Fourier Gaussian integral, with this prefactor, gives a unitary operator $\mu_L$ and the exact covariance
$$
 \mu_L\mathcal T_w\mu_L^{-1}=\mathcal T_{Lw}.
 \tag{2.9}
$$
Equation (2.9) may also be verified directly by substituting (2.5) into the kernel (2.8).

## 3. The integer representation and the comb quotient

The physical Weyl product is
$$
 \mathcal T_{(u,v)}\mathcal T_{(u',v')}
 =e^{i(vu'-uv')/(2h)}\mathcal T_{(u+u',v+v')}.
$$
For integer vectors and odd $N$, its scalar is
$$
 (-1)^{n_pm_q+n_qm_p}.
$$
Consequently the signs in (2.6) give
$$
 R_nR_m=R_{n+m},\qquad R_n^*=R_{-n}.
 \tag{3.1}
$$
Thus the $R_n$ form an honest abelian unitary representation of $\mathbb Z^2$.

Since $L\equiv I\pmod2$, (2.9) implies
$$
 \mu_LR_n=R_{Ln}\mu_L.
 \tag{3.2}
$$

The distributions fixed by every $R_n$ are precisely the combs
$$
 \mathcal C u=\frac1{\sqrt N}
       \sum_{j\in\mathbb Z}u_{j\bmod N}\delta(q-j/N).
 \tag{3.3}
$$
Indeed, invariance under $R_{(0,1)}=e^{2\pi iNq}$ confines the distribution to the simple zeros $q=j/N$ of $e^{2\pi iNq}-1$, with no derivatives of delta distributions. Invariance under $R_{(1,0)}$ makes the coefficients $N$-periodic. These two invariances imply all the others by (3.1). The normalization in (3.3) identifies the quotient Hilbert norm with the usual norm on $\mathbb C^N$.

For a Schwartz function $\psi$, periodization is a convergent tempered-distribution sum:
$$
 P\psi:=\sum_{n\in\mathbb Z^2}R_n\psi
  =\frac1N\sum_{j\in\mathbb Z}
       \left(\sum_{a\in\mathbb Z}\psi(j/N-a)\right)
       \delta(q-j/N).
 \tag{3.4}
$$
To obtain (3.4), note that the two signs in
$$
 (-1)^{ab}e^{2\pi iNb(q-a/2)}
$$
cancel for odd $N$, and apply
$$
 \sum_{b\in\mathbb Z}e^{2\pi iNbq}
 =\frac1N\sum_{j\in\mathbb Z}\delta(q-j/N).
$$

Define
$$
 (\Theta\psi)_j=\frac1{\sqrt N}\sum_{a\in\mathbb Z}\psi(j/N-a).
 \tag{3.5}
$$
Then $P\psi=\mathcal C(\Theta\psi)$. Grouping the absolutely convergent Schwartz sums by residues gives the exact bilinear identity
$$
 \langle\Theta\psi,\Theta\chi\rangle_{\mathbb C^N}
 =\langle\psi,P\chi\rangle_{\mathbb R}.
 \tag{3.6}
$$
The right side is the distribution pairing with complex conjugation in the first argument.

## 4. Exact metaplectic scalar on the comb quotient

It suffices to act on one residue class
$$
 \sum_{\ell\in\mathbb Z}\delta(q-y/N-\ell),
 \qquad y\in\{0,\ldots,N-1\}.
$$
After substituting $q=y/N+\ell$ into (2.8), split $\ell=a+8z$, where $0\leq a<8$. All $z$-dependent integer phases cancel except $e^{2\pi i(2NQ)z}$. Hence
$$
 \sum_{z\in\mathbb Z}e^{2\pi i(2NQ)z}
 =\frac1{2N}\sum_{j\in\mathbb Z}\delta(Q-j/(2N)).
 \tag{4.1}
$$
The factor $1/(2N)$ in (4.1) is the distributional scaling factor and must be retained.

At $Q=j/(2N)$, the remaining finite sum is
$$
 \sum_{a=0}^{7}e_8\!\left((j-6y)a-3Na^2\right).
$$
Translation $a\mapsto a+4$ multiplies its summand by $(-1)^j$. It therefore vanishes for odd $j$. For $j=2x$, put $d=x-3y$. The sum becomes
$$
 G=\sum_{a=0}^{7}e_8(-3Na^2+2da).
$$
Every odd residue is its own multiplicative inverse modulo $8$; in particular $(-3N)^{-1}\equiv-3N\pmod8$. Completing the square gives
$$
 G=e_8(3Nd^2)\sum_{a=0}^{7}e_8(-3Na^2).
$$
Among the even $a$, the two squares $0$ and the two squares $4$ cancel. Every odd square is $1\pmod8$. Thus
$$
 G=4e_8(-3N+3Nd^2).
 \tag{4.2}
$$

Combining $C_h$, (4.1), and (4.2), the quotient matrix $B_N$ of $\mu_L$ is
$$
 (B_N)_{xy}
 =\frac{e_8(1-3N)}{\sqrt N}
   \exp\!\left[-\frac{2\pi i}{8N}(3x^2-2xy+3y^2)\right]
   e_8\!\left(3N(x-3y)^2\right).
 \tag{4.3}
$$
Let $8\overline8=1+\kappa N$. Then $\kappa\equiv-N\pmod8$, so the phase in (2.2), with $r_{xy}=3x^2-2xy+3y^2$, is
$$
 e_N(-\overline8r_{xy})
 =\exp[-2\pi i r_{xy}/(8N)]e_8(Nr_{xy}).
$$
Finally,
$$
 3(x-3y)^2-r_{xy}=-16xy+24y^2\in8\mathbb Z.
$$
It follows exactly that
$$
 \boxed{B_N=e_8(1-3N)M_N=\zeta_N^{-1}M_N,
 \qquad \zeta_N=e_8(3N-1),\qquad |\zeta_N|=1.}
 \tag{4.4}
$$
No abstract choice of metaplectic scalar or unproved modulus assertion remains in (4.4).

For completeness, $M_N$ is unitary directly from (2.2): the inner product of rows $x,x'$ is a scalar of modulus one times
$$
 N^{-1}\sum_y e_N(\overline4(x-x')y),
$$
which is $\delta_{x,x'}$. This holds for all odd composite $N$ as well as primes.

## 5. Correct plane symbol and exact descent of the kick

Plane Weyl quantization of a Fourier mode gives
$$
 \operatorname{Op}_h^W(e^{2\pi i(kq+lp)})
 =\mathcal T_{(-l/N,k/N)}.
$$
On the comb (3.3), the corresponding real-half phase differs from the modular-half phase in (2.1):
$$
 \left.\mathcal T_{(-l/N,k/N)}\right|_{\rm comb}
 =(-1)^{kl}T_N(l,k).
 \tag{5.1}
$$
Indeed, $\overline2=(N+1)/2$ as an integer representative, and its extra $N/2$ contributes $(-1)^{kl}$.

Accordingly the exact plane symbol descending to $A_N$ is
$$
 a(q,p)=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}-\frac1{10}
 +\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
 \tag{5.2}
$$
The $l=0$ terms need no correction. The mixed term has $l=\pm1$, so $q\mapsto q+1/2$ supplies precisely the factor $(-1)^k=(-1)^{kl}$. Two such factors, one from (5.1), give the coefficients in (2.4).

Let
$$
 A_h=\operatorname{Op}_h^W(a),\qquad
 V=e^{itA_h/h}\mu_L.
 \tag{5.3}
$$
The real trigonometric polynomial $a$ makes $A_h$ a bounded self-adjoint finite sum of physical Weyl translations. Its integer periodicity gives
$$
 A_hR_n=R_nA_h,\qquad VR_n=R_{Ln}V.
 \tag{5.4}
$$
The exponential series is convergent on $L^2$, on Schwartz functions in each Schwartz seminorm, and by duality on tempered distributions. Its comb quotient is the matrix exponential of the comb quotient of $A_h$. As $t/h=\tau N$, equations (4.4) and (5.1) therefore give
$$
 \boxed{\left.V\right|_{\rm comb}=\zeta_N^{-1}U_N.}
 \tag{5.5}
$$

## 6. Exact coherent frame

Use normalized Gaussian coherent states
$$
 \psi_{(q,p)}(x)
 =(\pi h)^{-1/4}
   \exp\!\left[-\frac{(x-q)^2}{2h}
              +\frac{ip(x-q/2)}h\right],
 \qquad |z\rangle=\psi_z.
 \tag{6.1}
$$
Set $\phi_z=\Theta\psi_z$. The finite frame identity is
$$
 \boxed{N\int_{[0,1]^2}|\phi_z\rangle\langle\phi_z|\,dz=I_N.}
 \tag{6.2}
$$
To check every factor, the $(j,j')$ matrix entry before the $q,p$ integrals is a sum over $a,a'$, with phase
$$
 \exp\left[2\pi ip(j-j'-N(a-a'))\right].
$$
Integration over $0\leq p\leq1$ leaves only $j=j'$ and $a=a'$, because $j,j'$ are fixed representatives between $0$ and $N-1$. The remaining sum of $q$-integrals tiles the real line and integrates the normalized Gaussian density to $1$. The factor $1/N$ from (3.5) is canceled by the $N$ in (6.2).

For an operator $W$ that preserves Schwartz space, descends to a finite operator $W_N$, and satisfies $WP=PW$, (3.6) gives
$$
 \langle\phi_z,W_N\phi_z\rangle
 =\langle z|PW|z\rangle.
 \tag{6.3}
$$
Here $W=V^m$ has $WP=PW$, since $L^m$ permutes $\mathbb Z^2$. Once absolute convergence is justified, (6.2)–(6.3) give
$$
 \operatorname{Tr}W_N
 =N\sum_{n\in\mathbb Z^2}\int_{[0,1]^2}
       \langle z|R_{-n}V^m|z\rangle\,dz.
 \tag{6.4}
$$
The replacement $n\mapsto-n$ does not alter the sum.

## 7. Absolute convergence of the sector decomposition

The next bounds are for each fixed $m,N$. Their constants need not be uniform in these parameters.

### 7.1. Summable translated-metaplectic words

Write $A_h=\sum_{\kappa\in F}a_\kappa\mathcal T_{v_\kappa}$, with finite $F$. Weyl products have unimodular scalars for real translations. Expanding the exponential series and moving all $\mu_L$'s to the right gives
$$
 V^m=\sum_\nu d_\nu\mathcal T_{w_\nu}\mu_L^m.
 \tag{7.1}
$$
For every fixed $C\geq0$, this expansion obeys
$$
 \sum_\nu |d_\nu|e^{C|w_\nu|}
 \leq
 \exp\!\left[
 \frac{|t|}{h}
 \sum_{j=0}^{m-1}\sum_{\kappa\in F}
 |a_\kappa|e^{C|L^jv_\kappa|}
 \right]<\infty.
 \tag{7.2}
$$
This follows from the triangle inequality for the sum of the translated displacement vectors, followed by the scalar exponential series for each factor. Equation (7.2) also proves convergence in every Schwartz seminorm, because a Weyl translation has at most polynomial growth in its displacement in such a seminorm.

### 7.2. Gaussian bounds uniform in the translation

Put $G=L^m$. Coherent translation covariance gives
$$
 \left|\langle z|\mathcal T_w\mu_L^m|z\rangle\right|
 =\left|\langle0|\mathcal T_{w+(G-I)z}\mu_L^m|0\rangle\right|.
 \tag{7.3}
$$
The scalar phases disappear in absolute value. Completing the square in the two Gaussian wave functions gives
$$
 \left|\langle0|\mathcal T_u\mu_L^m|0\rangle\right|
 =c_G
   \exp\!\left[-\frac1{2h}u^{\!T}(I+GG^{T})^{-1}u\right],
 \quad
 c_G=\left(\frac2{\sqrt{\det(I+GG^{T})}}\right)^{1/2}.
 \tag{7.4}
$$
In particular, $I+GG^T$ is positive definite.

The eigenvalues of $L$ are $3\pm2\sqrt2$. Thus $G-I$ is invertible for every $m\geq1$. Changing variables in (7.3) shows that the integral over the entire plane is finite and independent of $w$:
$$
 \frac1{2\pi h}\int_{\mathbb R^2}
 \left|\langle z|\mathcal T_w\mu_L^m|z\rangle\right|dz
 =
 \frac{\sqrt2\,\det(I+GG^T)^{1/4}}{|\det(G-I)|}.
 \tag{7.5}
$$

For the lattice sum over a unit cell, (7.4) instead gives
$$
 \sum_{n\in\mathbb Z^2}
 \left|\langle z|R_{-n}\mathcal T_w\mu_L^m|z\rangle\right|
 \leq
 c_G\sum_{n\in\mathbb Z^2}
 \exp[-c_{G,h}|n-w-(G-I)z|^2].
 \tag{7.6}
$$
The lattice Gaussian on the right is a bounded periodic function of its center. Its supremum is finite and independent of $w,z$. Equations (7.1), (7.2), (7.5), and (7.6) prove both:
$$
 \sum_n\int_{[0,1]^2}
 |\langle z|R_{-n}V^m|z\rangle|\,dz<\infty
$$
and absolute integrability of each sector diagonal on $\mathbb R^2$. All sums and integrals in (6.4) may therefore be rearranged. No uniform-in-$m$ smallness estimate has been used.

### 7.3. Grouping by lattice cosets

Let $g_n(z)=\langle z|R_{-n}V^m|z\rangle$. Since a coherent state centered at $z+w$ is a scalar of modulus one times $R_w|z\rangle$, covariance and (3.1) imply
$$
 g_{n_0}(z+w)=g_{n_0-(G-I)w}(z),
 \qquad w\in\mathbb Z^2.
 \tag{7.7}
$$
Indeed,
$$
 R_w^*R_{-n_0}V^mR_w
 =R_{-w-n_0+Gw}V^m.
$$
This calculation is the place where using the honest integer representation $R$, rather than dropping its character, is essential.

Choose one representative $n_0$ of each class in
$$
 \mathcal Q_m=\mathbb Z^2/(L^m-I)\mathbb Z^2.
$$
Its cardinality is $|\det(L^m-I)|$. Write all elements in the class as $n_0-(G-I)w$. By (7.7), summing their unit-cell integrals tiles the plane exactly once. There is no additional determinant multiplier:
$$
 \boxed{
 \frac{\operatorname{Tr}U_N^m}{\zeta_N^m}
 =\sum_{[n]\in\mathcal Q_m}
       \mathfrak T_h(R_{-n}V^m),
 \qquad
 \mathfrak T_h(B)=\frac1{2\pi h}
       \int_{\mathbb R^2}\langle z|B|z\rangle\,dz .
 }
 \tag{7.8}
$$
Every integral in (7.8) is an absolutely convergent ordinary integral. Its value is independent of the representative $n$ by the same translation calculation.

## 8. What is meant by a Fresnel sector trace

Equation (7.8) does not pretend that a unitary operator on $L^2(\mathbb R)$ is trace class. The notation $\mathfrak T_h$ denotes the explicitly defined coherent integral in (7.8).

For the operators at hand it also equals the Abel-regularized diagonal kernel integral
$$
 \mathfrak T_h(R_{-n}V^m)
 =\lim_{\varepsilon\downarrow0}
   \int_{\mathbb R}e^{-\varepsilon q^2}
      K_{R_{-n}V^m}(q,q)\,dq .
 \tag{8.1}
$$
Here is a direct justification of that equality and its convergence.

For one translated metaplectic word with linear matrix
$$
 G=\begin{pmatrix}a&b\\c&d\end{pmatrix}=L^m,
$$
one has $b\neq0$ and $D=a+d-2>0$. Its diagonal kernel has the form
$$
 \frac{\kappa}{\sqrt{2\pi h|b|}}
 \exp\left[\frac{i}{h}
       \left(\frac{D}{2b}q^2+\ell q+c_0\right)\right],
 \qquad |\kappa|=1,\quad \ell,c_0\in\mathbb R.
 \tag{8.2}
$$
For a physical translation $w=(u,v)$, specifically,
$$
 \ell=\frac{u(1-d)}b+v,\qquad
 c_0=\frac{du^2}{2b}-\frac{vu}{2},
$$
up to the already retained word scalar. The elementary Gaussian integral with damping gives the limit
$$
 \frac{\kappa e^{i\pi\operatorname{sgn}(D/b)/4}}{\sqrt{|D|}}
 \exp\left[\frac{i}{h}
       \left(c_0-\frac{b\ell^2}{2D}\right)\right].
 \tag{8.3}
$$
For every $\varepsilon\geq0$, the modulus of the damped integral is at most $1/\sqrt{|D|}$, independently of the translation. The Gaussian determinant factor decreases under positive damping, and the real part of its completed-square linear term is nonpositive.

The coherent integral of this same quadratic kernel equals (8.3). One fully convergent way to see the equality is to insert the trace-class operator
$$
 H_\varepsilon=\frac1{2\pi h}\int
          e^{-\varepsilon|z|^2}|z\rangle\langle z|\,dz.
$$
Then $\operatorname{Tr}(BH_\varepsilon)$ is the damped coherent integral. Its kernel is an explicit Gaussian:
$$
 H_\varepsilon(x,y)=
 \frac{\exp\left[
 -\frac{(x-y)^2}{4\varepsilon h^2}
 -\frac{(x-y)^2}{4h}
 -\frac{\varepsilon(x+y)^2}{4(1+\varepsilon h)}
 \right]}
 {2h\sqrt{\pi\varepsilon(1+\varepsilon h)}} .
 \tag{8.4}
$$
Substitute (8.2)'s two-variable quadratic kernel and use $s=(x+y)/2$, $\delta=x-y$. The $\delta$ integral in (8.4) is an approximate identity and the remaining nonzero $s^2$ coefficient tends to $D/(2b)$. The two elementary Gaussian integrations therefore tend to (8.3). The coherent side also tends to $\mathfrak T_h(B)$ by (7.5) and dominated convergence. This proves the equality for a single word without interchanging an undamped Fourier delta distribution with a conditionally convergent integral.

For the series (7.1), its total absolute coefficient mass is finite. The undamped word kernels have a common constant absolute prefactor, so at $\varepsilon>0$ the diagonal kernel integral and word sum interchange absolutely. The translation-independent bound following (8.3) then permits passage to the Abel limit term by term. The coherent side permits the same passage by (7.5). This proves (8.1).

There is also an exact $m$-variable path-kernel form. If $K_V$ is the exact one-step kernel, put $q_m=q_0+n_q$. Then
$$
 \mathfrak T_h(R_{-n}V^m)=(-1)^{n_qn_p}
 \lim_{\varepsilon\downarrow0}
 \int_{\mathbb R^m}
 e^{-\varepsilon\sum_{j=0}^{m-1}q_j^2}
 e^{-in_p(q_0+n_q/2)/h}
 \prod_{j=0}^{m-1}K_V(q_{j+1},q_j)\,d\mathbf q .
 \tag{8.5}
$$
To justify composition and the common Abel limit, expand each exact one-step kernel into its absolutely summable translated-$\mu_L$ series. Every resulting word integrand is a quadratic exponential with a real linear term. Its Hessian in the $m$ position variables is
$$
 H_m=-\frac14(6I-\mathcal R-\mathcal R^{-1}),
 \tag{8.6}
$$
where $\mathcal R$ is the cyclic shift on $m$ variables. Its eigenvalues lie in $[-2,-1]$, including $m=1$ and $m=2$ with the cyclic-shift multiplicities as written. Thus every damped Gaussian word integral is bounded by the same determinant prefactor independently of its linear term. The product of the one-step absolute coefficient sums is finite. Dominated convergence proves (8.5), and Gaussian composition gives the same word operator as (7.1).

If a separately proved exact analytic representation
$$
 K_V(Q,q)=C_h e^{iF_t(Q,q)/h}B_h(Q,q)
 \tag{8.7}
$$
is available, it may be substituted into (8.5). Equation (8.7), and any contour deformation or trace-norm estimate subsequently imposed on it, is an additional analytic assertion. It is not inferred merely from the convergence of the real word series.

## 9. Deck transformations and cyclic action phases

This section assumes a single-valued generating function $F_t(Q,q)$ for
$$
 \Psi=\phi_a^{-t}\circ L,
$$
with $p=-\partial_qF_t$, $P=\partial_QF_t$, initial value $F_0$ from (2.8), and the Hamilton–Jacobi normalization
$$
 \partial_tF_t=a(Q,\partial_QF_t).
 \tag{9.1}
$$
For sufficiently small real time, its existence follows from the global twist of $L$ and the bounded second derivatives of the finite trigonometric polynomial $a$. For example, the derivative of $\phi_a^{-t}$ differs from the identity by at most $e^{|t|\|D X_a\|_\infty}-1$. Once this is less than $1/(2\|L\|)$, $\partial Q/\partial p$ remains strictly negative and bounded away from zero. The map $p\mapsto Q(q,p)$ is then a global bijection for every $q$, and the generating equations integrate to (9.1). The specified $t=10^{-80}/(2\pi)$ is far inside this condition: from (5.2) one can use the crude bounds $\|a\|_{\ell^1}<2$, Fourier frequencies at most $9$ in $q$ and $1$ in $p$, hence $\|D X_a\|_\infty<10^5$ and $\|L\|<8$.

For an integer vector $w=(b,d)$, write $Lw=(a,c)$. The exact deck identity is
$$
 F_t(Q+a,q+b)-F_t(Q,q)
 =cQ-dq+\frac{ca-db}{2}.
 \tag{9.2}
$$
At $t=0$, (9.2) follows by expansion of (2.8). For general small $t$, subtract its right side from the shifted function. Integer periodicity of $a$, including the integer momentum shift $c$, gives the same equation (9.1) and the same initial value. Uniqueness along the characteristics proves (9.2).

The sector action is
$$
 \mathcal S_n(\mathbf q)
 =\sum_{j=0}^{m-1}F_t(q_{j+1},q_j)
       -n_p(q_0+n_q/2),
 \qquad q_m=q_0+n_q.
 \tag{9.3}
$$
Its critical-point equations are exactly
$$
 \Psi^m(q_0,p_0)=(q_0+n_q,p_0+n_p).
 \tag{9.4}
$$
The boundary term in (9.3) enforces the momentum winding; its half term comes directly from $R_{-n}$ in (8.5).

### 9.1. Independence of the lifted starting point

Put $w_j=L^jw=(a_j,b_j)$. Changing the initial lift by $w$ changes every position variable by $a_j$ and the winding to
$$
 n'=n+(L^m-I)w.
$$
Apply (9.2) to each edge and telescope. The exact action difference is
$$
 2\Delta\mathcal S
 =n_q(b_m+b_0)-n_p(a_m+a_0)+b_0a_m-b_ma_0.
 \tag{9.5}
$$
Because $L\equiv I\pmod2$, $a_m\equiv a_0$ and $b_m\equiv b_0\pmod2$. The right side of (9.5) is an even integer. Therefore $\Delta\mathcal S\in\mathbb Z$, and
$$
 e^{i\Delta\mathcal S/h}=e^{2\pi iN\Delta\mathcal S}=1.
$$
Also $n'\equiv n\pmod2$, so $(-1)^{n'_qn'_p}=(-1)^{n_qn_p}$. The phase
$$
 (-1)^{n_qn_p}e^{i\mathcal S_n/h}
 \tag{9.6}
$$
is consequently independent of the lift.

### 9.2. Cyclic shift of the starting point

Begin the same closed torus orbit at its next point. Its new winding is $Ln$, because $\Psi(z+n)=\Psi(z)+Ln$. The new edge sum differs from the old edge sum by
$$
 F_t(q_1+(Ln)_q,q_0+n_q)-F_t(q_1,q_0).
$$
Equation (9.2) with $w=n$ makes this difference
$$
 (Ln)_p q_1-n_pq_0+
 \frac{(Ln)_p(Ln)_q-n_pn_q}{2}.
$$
The change of the boundary term in (9.3) cancels it exactly. Hence the action itself, not just its exponential, is invariant under the cyclic change of starting point. The character in (9.6) is unchanged because $Ln\equiv n\pmod2$.

These calculations establish phase consistency. They do not establish the analytic size of a stationary-phase remainder or the uniqueness of a critical point in every sector.

## 10. Exact finite Egorov and the Fourier mass bound

With the plus-shift convention (2.1), direct multiplication proves
$$
 \boxed{M_NT_N(a,b)M_N^{-1}=T_N(3a+4b,\,2a+3b).}
 \tag{10.1}
$$
For clarity, the exponent of $(M_NT_N(a,b))_{x,w}$, relative to $M_{N,xw}$, is
$$
 -\frac{ax}{4}+\left(\frac{3a}{4}+b\right)w
       -\frac{3a^2}{8}-\frac{ab}{2}.
$$
For $A=3a+4b$, $B=2a+3b$, the corresponding exponent of
$(T_N(A,B)M_N)_{x,w}$ is
$$
 \left(B-\frac{3A}{4}\right)x+\frac A4w
       -\frac{3A^2}{8}+\frac{BA}{2}.
$$
The coefficients and constants agree; in particular $4B-3A=-a$. Every fraction in this paragraph is modular. Only invertibility of $2$ is used, so (10.1) holds for every odd composite $N$.

The Weyl matrices form a basis of all $N\times N$ matrices. Indeed,
$$
 \operatorname{Tr}T_N(v)=N\,\mathbf1_{\{v=0\}},
 \qquad
 \operatorname{Tr}\bigl(T_N(v)^*T_N(w)\bigr)
      =N\,\mathbf1_{\{v=w\}}.
 \tag{10.2}
$$
The first identity follows from the shift and the finite character sum; the second follows from the Weyl product.

Expand
$$
 r(q)=1+\cos2\pi q-\cos14\pi q
       -\tfrac12\cos16\pi q-\tfrac12\cos12\pi q.
$$
Its Fourier $\ell^1$ norm is $4$, and its constant coefficient is $1$. Consequently, before reducing frequencies modulo $N$,
$$
 A_N=\frac12T_N(0,7)+\frac12T_N(0,-7)+R_N,
 \qquad
 \|R_N\|_{\text{Weyl }\ell^1}\leq
       \frac3{10}+\frac4{100}+\frac4{100}
       =\frac{19}{50}=0.38.
 \tag{10.3}
$$
The two latter bounds use the submultiplicativity of Fourier $\ell^1$ norm and the norm $1$ of a sine or cosine. Aliasing modulo $N$ can combine coefficients but cannot increase their total absolute mass. Thus (10.3) is valid after aliasing, including small and composite dimensions.

## 11. Lindemann–Weierstrass evaluation lemma

Let $\overline{\mathbb Q}$ denote the field of algebraic numbers. The external theorem used is:

**Lindemann–Weierstrass.** If $\gamma_1,\ldots,\gamma_k$ are distinct algebraic numbers, then $e^{\gamma_1},\ldots,e^{\gamma_k}$ are linearly independent over $\overline{\mathbb Q}$.

An exact source is Sever Angel Popescu, *A simple and self-contained proof for the Lindemann–Weierstrass theorem*, arXiv:2306.14352v2, 17 September 2023, Theorem 3.2, printed pages 14–15: https://arxiv.org/pdf/2306.14352 . The theorem statement and proof were opened independently during this audit.

It follows that evaluation at any nonzero algebraic $z_0$ is injective on finite exponential polynomials with algebraic coefficients and algebraic frequencies. Explicitly, after equal frequencies are combined,
$$
 F(z)=\sum_{j=1}^k c_je^{\beta_jz},
 \quad c_j,\beta_j\in\overline{\mathbb Q},
 \quad\beta_j\neq\beta_l\ (j\neq l),
$$
satisfies
$$
 F(z_0)=0,\quad z_0\in\overline{\mathbb Q}\setminus\{0\}
 \quad\Longrightarrow\quad
 c_1=\cdots=c_k=0
 \quad\Longrightarrow\quad F\equiv0.
 \tag{11.1}
$$
Distinctness is preserved because $z_0\neq0$.

All entries of $A_N,M_N$ are algebraic: finite Weyl entries are roots of unity, $N^{-1/2}$ is algebraic, and $e^{i\alpha_0}=(-3+4i)/5$ is algebraic. Since $A_N$ is Hermitian, its distinct eigenvalues $\lambda_1,\ldots,\lambda_s$ are algebraic and its spectral projectors are the algebraic matrices
$$
 P_j=\prod_{k\neq j}\frac{A_N-\lambda_kI}{\lambda_j-\lambda_k}.
$$
Therefore
$$
 e^{izNA_N}=\sum_{j=1}^s e^{iN\lambda_jz}P_j.
 \tag{11.2}
$$
Every entry of $U_N(z)^m$, every trace, and every polynomial in those entries with algebraic coefficients is consequently a finite exponential polynomial of the form in (11.1). Repeated sums of eigenvalues cause coincident frequencies; they must first be combined, as in the statement of the lemma.

## 12. No exact scalar returns outside $N=7$

**Theorem.** For every odd $N\geq3$, $N\neq7$, every integer $m\geq1$, and every $z_0\in\overline{\mathbb Q}\setminus\{0\}$,
$$
 U_N(z_0)^m\notin\mathbb C I_N.
 \tag{12.1}
$$

**Proof.** Suppose the contrary. Every off-diagonal entry and every difference of diagonal entries of $U_N(z)^m$ vanishes at $z_0$. By (11.1), every such function vanishes identically. Hence $U_N(z)^m$ is scalar for all complex $z$.

At $z=0$, $M_N^m$ is scalar. Differentiation at zero gives
$$
 \left.\frac d{dz}U_N(z)^m\right|_{z=0}
 =iNQ_mM_N^m,\qquad
 Q_m=\sum_{j=0}^{m-1}M_N^jA_NM_N^{-j}.
 \tag{12.2}
$$
Thus $Q_m$ is scalar.

By (10.1) and Weyl independence (10.2), scalar $M_N^m$ implies
$$
 S^m=I\quad\text{on }(\mathbb Z/N\mathbb Z)^2.
$$
Let $\mathcal O$ be the $S$-orbit of $v_0=(0,7)$. It is a nonzero orbit for the stated dimensions: $v_0=0$ would require $N\mid7$, and $N=1,7$ have been excluded. Let $d=|\mathcal O|$; then $d\mid m$.

Write $A_N=\sum_v a_vT_N(v)$. At any $v\in\mathcal O$, the Weyl coefficient of $Q_m$ is
$$
 \sum_{j=0}^{m-1}a_{S^{-j}v}
 =\frac md\sum_{w\in\mathcal O}a_w.
 \tag{12.3}
$$
The positive coefficient $1/2$ at $v_0$ belongs to this orbit. If $-v_0$ belongs too, it adds another positive $1/2$. The remainder contributes a sum with absolute value at most $0.38$. Thus
$$
 \operatorname{Re}\sum_{w\in\mathcal O}a_w
 \geq\frac12-\frac{19}{50}
 =\frac3{25}>0.
 \tag{12.4}
$$
Equations (12.3)–(12.4) give a nonzero coefficient at a nonzero Weyl index. This contradicts scalar $Q_m$ by (10.2). $\square$

The theorem in particular applies to $\tau=10^{-80}$. It excludes exact scalar revivals only. It gives no bound that excludes very close returns on growing time scales.

### The exceptional dimension is real

At $N=7$, $r(j/7)=0$ for every grid point. The modular midpoints in the off-diagonal entries are also grid points. The explicit matrix (2.4) therefore gives
$$
 A_7=\frac9{10}I_7.
 \tag{12.5}
$$
Moreover
$$
 S^3=\begin{pmatrix}99&140\\70&99\end{pmatrix}\equiv I\pmod7.
$$
By (10.1), $M_7^3$ commutes with every Weyl matrix, so it is scalar. Equation (12.5) then makes $U_7(z)^3$ scalar for every $z$. The exception cannot be deleted.

## 13. Every power trace is nonzero

**Theorem.** For every odd positive $N$, every integer $m\geq1$, and every algebraic $z_0$,
$$
 \operatorname{Tr}U_N(z_0)^m\neq0.
 \tag{13.1}
$$

**Proof.** The trace of conjugation by a unitary matrix $W$, as an operator on the $N^2$-dimensional matrix space, is
$$
 \operatorname{Tr}(\operatorname{Ad}W)
 =(\operatorname{Tr}W)(\operatorname{Tr}W^{-1})
 =|\operatorname{Tr}W|^2.
$$
For $W=M_N^m$, (10.1) makes this conjugation an exact permutation of the Weyl basis, with no phases. Its trace therefore counts its fixed indices:
$$
 |\operatorname{Tr}M_N^m|^2
 =\#\ker(S^m-I:(\mathbb Z/N\mathbb Z)^2
                     \to(\mathbb Z/N\mathbb Z)^2)\geq1.
 \tag{13.2}
$$
The last inequality includes the zero index.

Now $p_m(z)=\operatorname{Tr}U_N(z)^m$ is a finite algebraic exponential polynomial by (11.2), and $p_m(0)\neq0$ by (13.2). Thus $p_m\not\equiv0$. Equation (11.1) excludes a zero at every nonzero algebraic $z_0$; the value at $z_0=0$ was already handled. $\square$

Taking $m=1$ shows that the finite spectral multiset has no nontrivial multiplicative symmetry. Indeed, invariance under multiplication by a scalar $\rho\neq1$ would give
$$
 \operatorname{Tr}U_N(z_0)=\rho\,\operatorname{Tr}U_N(z_0),
$$
contradicting (13.1). For real $z_0$, this includes every nontrivial rotational symmetry on the unit circle.

## 14. What the argument does and does not say about simple spectrum

Let
$$
 \Delta_N(z)=\operatorname{disc}_{X}
                 \det(XI-U_N(z)).
$$
The discriminant is a polynomial with integer coefficients in the characteristic coefficients, and hence a finite algebraic exponential polynomial by (11.2). Therefore the following implication is proved:
$$
 \Delta_N\not\equiv0
 \quad\Longrightarrow\quad
 \Delta_N(z_0)\neq0
 \quad\text{for every nonzero algebraic }z_0.
 \tag{14.1}
$$
The unproved obligation is $\Delta_N\not\equiv0$ for the specified family and each dimension under consideration.

For $N=7$, that obligation is false. Equation (12.5) makes $U_7(z)$ a scalar multiple of $M_7$, and $M_7^3$ is scalar. Its seven eigenvalues therefore occupy at most three distinct values:
$$
 \Delta_7(z)\equiv0.
 \tag{14.2}
$$

For $7\nmid N$, the supplied explicit matrix for $A_N$ is a cyclic Jacobi matrix with exactly one zero edge, since $r$ vanishes at exactly one of the $N$ odd-grid points. Removing that edge gives an irreducible Jacobi path; a diagonal unitary gauge makes its nonzero edge weights positive. The usual recurrence for an eigenvector along a path shows that an eigenspace has dimension at most one, and Hermiticity therefore gives simple spectrum of $A_N$. This observation alone does not prove (14.1)'s antecedent for $e^{izNA_N}M_N$.

A concrete obstruction to that inference is
$$
 A=\operatorname{diag}(-2,-1,1,2,3),
$$
with $M$ the permutation that swaps indices $1,4$, swaps $2,3$, and fixes $5$. Then $A$ is simple, $M^2=I$, and all powers of $M$ have nonzero trace. Nevertheless
$$
 \operatorname{spec}(e^{izA}M)
 =\{1,-1,1,-1,e^{3iz}\}
$$
for every $z$, so the discriminant vanishes identically. For every nonzero algebraic $z$, this family also has no scalar power: an odd power retains the distinct values $1,-1$, while an even scalar power would force $e^{3imz}=1$, impossible by Lindemann–Weierstrass. Thus simple $A$, nonvanishing power traces, and absence of scalar returns together still do not imply simple spectrum of the product family.

No generic-simplicity assertion is being substituted for the missing family-specific argument.

## 15. Dependency and audit record

| Claim | Load-bearing inputs | Status |
|---|---|---|
| Exact comb scalar (4.4) | Distribution scaling; eight-term Gauss sum; modular arithmetic | Proved directly |
| Corrected symbol descent (5.5) | Real-half versus modular-half Weyl convention | Proved directly |
| Finite coherent frame (6.2) | Finite character orthogonality; Gaussian normalization | Proved directly |
| Sector trace formula (7.8) | Frame; exact covariance; summable word expansion; Gaussian decay | Proved for every fixed $m,N$ |
| Abel/Fresnel identity (8.5) | Quadratic Gaussian integrals; negative word Hessian; absolute coefficient mass | Proved for every fixed $m,N$ |
| Deck and cyclic phases | Existence and stated normalization of the small-time generating function | Proved in the stated small-time regime |
| No scalar returns (12.1) | Exact Egorov; $0.38$ Fourier mass bound; Lindemann–Weierstrass | Proved for odd $N\geq3,\ N\neq7$ |
| Nonzero power traces (13.1) | Exact Egorov permutation trace; Lindemann–Weierstrass | Proved for every odd positive $N$ |
| Simple spectrum for every odd $N$ | Would require $\Delta_N\not\equiv0$ | Refuted by $N=7$ |
| Simple spectrum for remaining $N$ | Family-specific discriminant nonidentity | Not proved |
| Uniform resummed error $2(0.421)^m$ | Exact analytic amplitude; contour and trace-norm bounds | Outside this packet; not certified here |
| Deterministic CUE/Hdiag target | Long-time cancellation/statistical control | Unresolved |

Review provenance: fresh adversarial internal review; independent reconstruction from exact formulas supplied during the continuation. No numerical sample is used to establish a universal assertion. The external Lindemann–Weierstrass theorem was checked against the exact source listed in Section 11. The disappeared earlier files, their audit labels, and agreements by other reviewers are not proofs used in this document.
