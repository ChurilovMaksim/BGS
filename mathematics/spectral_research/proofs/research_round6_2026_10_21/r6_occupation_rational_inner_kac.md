> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_occupation_rational_inner_kac.md`. Embedded SHA256: `4bf2d0ef9ea39227cb0af38569df5432722799b32f322811a969a2ac85323e6a`.
> [Thematic guide](../../topics/histories.md).

# Rational inner structure and exact occupation first moments

21 October 2026. A finite-dimensional theorem for the exact occupation amplitudes. The application below retains the prescribed family, the fixed value $\tau=10^{-80}$, and every odd $N\ge3$. No claim of historical novelty is made.

The identities in this note sum over all positive times. They prove normalization and finite first moments for specified squared-amplitude occupation measures. They do not evaluate the spectral form factor at times comparable to $N$, and they do not control its unequal-occupation sector.

## 1. Definitions and theorem

Let $U$ be an $N\times N$ unitary matrix. For $Z=\operatorname{diag}(z_0,\ldots,z_{N-1})$, write
$$
 D_U(z)=\det(I-ZU),\qquad
 A_{n,d}=n[z^d]\{-\log D_U(z)\},\qquad |d|=n\ge1.
 \tag{1.1}
$$
The logarithm in (1.1) is its formal expansion with zero constant term. Equivalently $A_{n,d}$ is the sum of amplitudes of the rooted closed words with occupation vector $d$. The identity follows by formally differentiating
$$
 -\log\det(I-tZU)=\sum_{n\ge1}\frac{t^n}{n}\operatorname{Tr}(ZU)^n
 \tag{1.2}
$$
and comparing coefficients. Thus no quotient by word periods is present.

For each vertex $v$ and integer $k\ge1$,
$$
 \boxed{\displaystyle
 \sum_{d:\,d_v=k}\frac{|A_{|d|,d}|^2}{|d|^2}=\frac1{k^2}.}
 \tag{1.3}
$$
If $w\ne v$ and $U_{vw}U_{wv}\ne0$, then
$$
 \boxed{\displaystyle
 \sum_{d:\,d_v=k}
 d_w\frac{|A_{|d|,d}|^2}{|d|^2}=\frac1k.}
 \tag{1.4}
$$
The equality for $w=v$ follows from (1.3). Every series in (1.3) and (1.4) has nonnegative summands; the proof below establishes its convergence and value.

Consequently, if $U_{vw}U_{wv}\ne0$ for every $w\ne v$, then
$$
 \boxed{\displaystyle
 \sum_{d:\,d_v=k}\frac{|A_{|d|,d}|^2}{|d|}=\frac Nk.}
 \tag{1.5}
$$
In particular
$$
 \mu_{v,k}(d)=k^2\frac{|A_{|d|,d}|^2}{|d|^2},
 \qquad d_v=k,
 \tag{1.6}
$$
is a probability measure satisfying
$$
 \mathbb E_{\mu_{v,k}}d_w=k,\qquad
 \mathbb E_{\mu_{v,k}}|d|=Nk.
 \tag{1.7}
$$
The first equality in (1.7) uses the stated two-way nonvanishing assumption when $w\ne v$. For the original $U_N$ all those assumptions hold, as proved in Section 7.

## 2. Schur complement and contractive transfer function

Reorder coordinates so that $v$ comes first, and set
$$
 U=\begin{pmatrix}a&b\\c&D\end{pmatrix},
 \qquad R=\{0,\ldots,N-1\}\setminus\{v\},\qquad
 Z_R=\operatorname{diag}(z_w:w\in R).
$$
Every compression $D$ of a unitary has operator norm at most one. Thus both $I-Z_RD$ and $I-DZ_R$ are invertible whenever $\max_{w\in R}|z_w|<1$. Put
$$
 Q(z_R)=\det(I-Z_RD),\qquad
 \phi_v(z_R)=a+bZ_R(I-DZ_R)^{-1}c.
 \tag{2.1}
$$
The matrix identity
$$
 (I-Z_RD)^{-1}Z_R=Z_R(I-DZ_R)^{-1}
$$
follows by multiplying by the two invertible factors. The block determinant formula, or elimination of the lower left block, therefore gives
$$
 D_U(z)=Q(z_R)(1-z_v\phi_v(z_R)).
 \tag{2.2}
$$

For clarity, contractivity of $\phi_v$ follows directly from unitarity, without a boundary theorem for transfer functions. Let
$$
 y=(I-DZ_R)^{-1}c.
$$
Then
$$
 U\binom{1}{Z_Ry}=\binom{\phi_v}{y}.
$$
Taking squared norms proves
$$
 1-|\phi_v(z_R)|^2
 =\sum_{w\in R}(1-|z_w|^2)|y_w|^2\ge0.
 \tag{2.3}
$$
In particular $\phi_v$ is a bounded holomorphic function on the polydisc.

Multilinearity of the determinant gives
$$
 D_U(z)=\sum_S(-1)^{|S|}\det(U_{S,S})\prod_{w\in S}z_w.
 \tag{2.4}
$$
Indeed identity rows outside $S$ force their own columns, leaving the indicated principal minor. Thus $D_U$ has degree at most one in each variable. By (2.2),
$$
 D_U(z)=Q(z_R)-z_vP(z_R),\qquad \phi_v=P/Q,
 \tag{2.5}
$$
where both $P$ and $Q$ have degree at most one in every remaining variable. Also $Q(0)=1$.

## 3. Boundary values and the unweighted coefficient identity

We use the elementary fact that a nonzero polynomial in $r$ complex variables has a zero set of Haar measure zero on the $r$-torus. To prove it, regard the polynomial as a polynomial in its last variable. At least one coefficient polynomial is nonzero. By induction, the set where all coefficient polynomials vanish has measure zero; outside it the last-variable polynomial has finitely many roots. Fubini completes the induction. The zero-variable case is immediate.

Apply this fact to $Q$. For almost every $\zeta_R$ with $|\zeta_w|=1$, the value $Q(\zeta_R)$ is nonzero, so $\phi_v(r\zeta_R)$ converges to $P(\zeta_R)/Q(\zeta_R)$ as $r\uparrow1$. The norm calculation preceding (2.3) is valid at such boundary points, with a unitary $Z_R$, and yields
$$
 |\phi_v(\zeta_R)|=1.
 \tag{3.1}
$$
Here $\det(I-DZ_R)=\det(I-Z_RD)$; either equality follows from the identical principal-minor expansions. Thus both inverses used above exist at these points. Equations (2.3) and (3.1) establish precisely the rational inner property needed here.

Fix $k\ge1$ and expand
$$
 \phi_v(z_R)^k=\sum_{\alpha\in\mathbb Z_{\ge0}^{R}}
                      c_\alpha z_R^\alpha.
 \tag{3.2}
$$
For $0<r<1$, integration of the uniformly convergent power series on the radius $r$ torus gives
$$
 \int_{\mathbb T^{R}}|\phi_v(r\zeta_R)^k|^2\,d\zeta_R
   =\sum_\alpha |c_\alpha|^2r^{2|\alpha|}.
 \tag{3.3}
$$
The torus measure is normalized. The integrand is bounded by one and converges almost everywhere to one. Dominated convergence on the left and monotone convergence on the right imply
$$
 \sum_\alpha|c_\alpha|^2=1.
 \tag{3.4}
$$
The conventions in the empty set $R$ give the same result for $N=1$.

Expanding the logarithm of (2.2) at the origin gives, coefficient by coefficient,
$$
 -\log D_U(z)=-\log Q(z_R)
       +\sum_{j\ge1}\frac{z_v^j}{j}\phi_v(z_R)^j.
 \tag{3.5}
$$
Consequently, for $d_v=k$,
$$
 \frac{A_{|d|,d}}{|d|}=\frac{c_{d_R}}k.
 \tag{3.6}
$$
Equations (3.4) and (3.6) prove (1.3).

## 4. The one-variable degree is exactly one

Fix $w\ne v$ and assume $U_{vw}U_{wv}\ne0$. Denote the other variables by $z_T$, so $R=\{w\}\cup T$. From (2.5),
$$
 P=p_0(z_T)+z_wp_1(z_T),\qquad
 Q=q_0(z_T)+z_wq_1(z_T).
 \tag{4.1}
$$
The polynomial $q_0$ is nonzero because $q_0(0)=1$. For all strictly interior $z_T$, the polynomial $q_0+z_wq_1$ has no zero for $|z_w|<1$, by Section 2. It follows that $|q_1(z_T)|\le |q_0(z_T)|$. Continuity extends this inequality to the closed polydisc. Hence, whenever $q_0(\zeta_T)\ne0$, the boundary slice denominator has no zero in the open disc. This argument does not assume a boundary limit of inverse matrices is uniformly bounded.

Define the polynomial
$$
 \Delta(z_T)=p_1(z_T)q_0(z_T)-p_0(z_T)q_1(z_T).
 \tag{4.2}
$$
On setting all $z_T=0$, (2.1) reduces to the explicit two-coordinate expression
$$
 \phi_v(z_w,0)
   =U_{vv}+
     \frac{U_{vw}U_{wv}z_w}{1-U_{ww}z_w}.
 \tag{4.3}
$$
In particular
$$
 \Delta(0)=U_{vw}U_{wv}\ne0.
 \tag{4.4}
$$
By the polynomial zero-set argument, for almost every $\zeta_T$, both $q_0(\zeta_T)$ and $\Delta(\zeta_T)$ are nonzero. Fix any such $\zeta_T$.

For $|z_w|=1$ away from the possible single denominator zero, (2.3) evaluated with every variable of modulus one gives
$$
 |p_0+z_wp_1|=|q_0+z_wq_1|.
 \tag{4.5}
$$
This equality extends to the possible zero by continuity of polynomials. If the denominator had a zero on the circle, the numerator would have the same zero, forcing the two linear polynomials to be proportional. That would contradict $\Delta\ne0$. Thus the slice has no denominator zero on the closed disc. It is nonconstant, analytic on a neighborhood of that disc, and has modulus one on its boundary.

It is therefore a degree-one Blaschke function. Here is the elementary last step. Its numerator must have one zero $\alpha$ in the open disc: otherwise the function and its reciprocal would both be analytic on the disc, continuous on its closure, and bounded by one there by the maximum principle, forcing constant modulus and then a constant function. The numerator has degree at most one, so there is just that zero. Divide the slice by $(z_w-\alpha)/(1-\overline\alpha z_w)$. The resulting function and its reciprocal are again analytic, continuous, and of boundary modulus one; the same argument makes their quotient a unimodular constant. Hence
$$
 \phi_v(z_w,\zeta_T)
    =\eta(\zeta_T)\frac{z_w-\alpha(\zeta_T)}
                              {1-\overline{\alpha(\zeta_T)}z_w},
 \qquad |\eta|=1,\quad |\alpha|<1.
 \tag{4.6}
$$
The degree is exactly one, not merely at most one. No smooth dependence on $\zeta_T$ is required.

## 5. Weighted Parseval without a boundary derivative interchange

Expand the bounded holomorphic function in the selected variable:
$$
 \phi_v(z_w,z_T)^k=\sum_{j\ge0}g_j(z_T)z_w^j.
 \tag{5.1}
$$
Cauchy's coefficient formula on $|z_w|=\rho<1$ bounds $|g_j(z_T)|\le \rho^{-j}$; letting $\rho\uparrow1$ gives $|g_j|\le1$ throughout the remaining polydisc.

Each $g_j$ is rational with denominator a power of $q_0(z_T)$, as follows by expanding the explicit quotient in (4.1) at $z_w=0$. Thus for almost every $\zeta_T$, $g_j(r\zeta_T)$ converges to $g_j(\zeta_T)$, which is exactly the coefficient of $z_w^j$ in the boundary slice. This holds simultaneously for all $j$, since the exceptional set $q_0=0$ is the same null set.

Writing $g_j(z_T)=\sum_\beta c_{j,\beta}z_T^\beta$, the radius $r$ Parseval identity and bounded dominated convergence prove
$$
 \sum_\beta |c_{j,\beta}|^2
       =\int_{\mathbb T^T}|g_j(\zeta_T)|^2\,d\zeta_T.
 \tag{5.2}
$$
For almost every fixed $\zeta_T$, (4.6) makes $\phi_v(\,\cdot\,,\zeta_T)^k$ a power of a degree-one Blaschke function. Its power series and derivative converge uniformly on the unit circle, since its pole is strictly outside it. Thus coefficient orthogonality gives
$$
 \sum_{j\ge0}j|g_j(\zeta_T)|^2
 =\int_{\mathbb T}
    \overline{\phi_v(z_w,\zeta_T)^k}\,
    z_w\partial_{z_w}(\phi_v(z_w,\zeta_T)^k)\,dz_w
 =k.
 \tag{5.3}
$$
The first integral uses normalized circle measure, not contour $dz$. To verify its value directly, on $|z_w|=1$ its integrand is
$$
 k\frac{1-|\alpha|^2}{|z_w-\alpha|^2}.
$$
Expanding the two geometric series in this Poisson kernel shows that its circle integral is $k$.

Multiply (5.2) by $j$, sum, and use Tonelli's theorem, since all summands are nonnegative. Equation (5.3) then yields
$$
 \sum_{j,\beta}j|c_{j,\beta}|^2
 =\int_{\mathbb T^T}\sum_jj|g_j(\zeta_T)|^2\,d\zeta_T
 =k.
 \tag{5.4}
$$
This proves the finite weighted coefficient norm. No differentiated boundary function has been passed through a limit or an integral in the other variables. Substitution of (3.6) proves (1.4). Summing the finitely many coordinate equalities proves (1.5) and (1.7).

## 6. Further exact consequences and their limitations

There is a universal convergent support-weighted identity, without a two-way nonvanishing assumption:
$$
 \boxed{\displaystyle
 \sum_{n\ge1}\frac1{n^2}
   \sum_{|d|=n}|\operatorname{supp}d|\,|A_{n,d}|^2
 =N\sum_{k\ge1}\frac1{k^2}=\frac{\pi^2N}{6}.}
 \tag{6.1}
$$
To prove it, sum (1.3) over $v$ and $k$. Tonelli applies throughout, and each $d$ is counted once for each positive coordinate. In particular
$$
 \sum_{n\ge1}\frac{\mathcal O_n(U)}{n^2}
 \le\frac{\pi^2N}{6},\qquad
 \mathcal O_n(U)=\sum_{|d|=n}|A_{n,d}|^2.
 \tag{6.2}
$$

If the nonvanishing assumptions of (1.7) hold, Markov's inequality gives
$$
 \mu_{v,k}(|d|\ge LNk)\le\frac1L\qquad(L>0).
 \tag{6.3}
$$
This is an all-time occupation tail, not a statement that the measure concentrates near $Nk$. In fact even exact flatness of every matrix entry does not force a finite second moment of these occupation measures; Section 8 gives an explicit example.

All expressions in (1.3)--(1.7) and (6.1) involve squared amplitudes within one occupation sector. They do not involve the phases between two different occupation vectors. In particular they do not evaluate
$$
 \Omega_n(U)=\sum_{\substack{|d|=|e|=n\\d\ne e}}
                         A_{n,d}\overline{A_{n,e}}.
 \tag{6.4}
$$
The identity $|\operatorname{Tr}U^n|^2=\mathcal O_n(U)+\Omega_n(U)$ therefore leaves the same unresolved original spectral estimate.

## 7. Verification for every member of the prescribed family

Every entry of $A_N$ and $M_N$ is algebraic: the coefficients of the finite trigonometric polynomial use only rational numbers, $i$, and $e^{i\alpha_0}=(-3+4i)/5$; the Weyl and Gaussian factors are roots of unity; and $\sqrt N$ is algebraic.

Let $\Lambda_N$ be the distinct eigenvalues of the Hermitian $A_N$. They are algebraic. Its spectral projectors are algebraic matrices because
$$
 P_\lambda=\prod_{\substack{\mu\in\Lambda_N\\\mu\ne\lambda}}
                   \frac{A_N-\mu I}{\lambda-\mu}.
$$
Hence
$$
 (U_N)_{vw}
 =\sum_{\lambda\in\Lambda_N}
       (P_\lambda M_N)_{vw}\,\exp(iN\tau\lambda).
 \tag{7.1}
$$
The coefficients in this finite sum are algebraic, and not all are zero: their sum is the nonzero Gaussian matrix entry $(M_N)_{vw}$.

For the sole external arithmetic input, use the precise Lindemann--Weierstrass statement in Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022, Theorem 1.1, DOI [10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170). The [author PDF](https://arxiv.org/pdf/2112.05004), page 1, was opened on 21 October 2026; it displays version 2, dated 16 May 2022, the publication metadata, and Theorem 1.1. That theorem states that a nontrivial algebraic linear combination of exponentials of distinct algebraic numbers is nonzero.

After zero coefficients are discarded from (7.1), its exponents are distinct algebraic numbers: $iN\tau\lambda$, with nonzero rational $\tau=10^{-80}$. Thus every hypothesis of that theorem is satisfied, and
$$
 (U_N)_{vw}\ne0
 \quad\text{for every odd }N\ge3\text{ and every }v,w.
 \tag{7.2}
$$
Therefore (1.3)--(1.7) apply to every original $U_N$, with no exceptional dimensions or limiting change to $\tau$.

## 8. Flat entries do not supply a second occupation moment

This section is a counterexample to an additional concentration inference, not a counterexample to the original family's target limit.

Take the $3\times3$ Fourier matrix
$$
 F_{jl}=3^{-1/2}\omega^{jl},\qquad
 \omega=e^{2\pi i/3},\quad 0\le j,l\le2.
$$
Every entry has squared modulus $1/3$, every entry is nonzero, and its classical transition matrix is exactly $J_3$.

Consider $v=0$, $w=1$, $k=1$, and put $z=z_2$. Eliminating coordinate $2$ in the unitary colligation at $|z|=1$ produces the $2\times2$ unitary
$$
 S(z)=F_{\{0,1\},\{0,1\}}+
 F_{\{0,1\},2}\frac{z}{1-F_{22}z}F_{2,\{0,1\}}.
 \tag{8.1}
$$
Unitarity follows by the same squared-norm calculation as (2.3), for arbitrary two-dimensional input vectors. The denominator never vanishes on the unit circle since $|F_{22}|=1/\sqrt3<1$.

The off-diagonal entry is
$$
 S_{01}(z)=
 \frac{3^{-1/2}(1-iz)}{1-\omega z/\sqrt3}.
 \tag{8.2}
$$
Indeed its numerator before simplification is $3^{-1/2}+z(\omega^2-\omega)/3$, and $\omega^2-\omega=-i\sqrt3$.

For almost every fixed $z$, the $z_1$ slice of $\phi_0$ is a degree-one Blaschke function. Write its zero as $\alpha(z)$ and put
$$
 a(z)=|\alpha(z)|^2,\qquad
 \delta(z)=1-a(z)=|S_{01}(z)|^2.
 \tag{8.3}
$$
The last equality holds because the slice at $z_1=0$ equals $S_{00}(z)$, whose modulus is $|\alpha|$, and the first row of the unitary $S$ has norm one.

The coefficients of a degree-one Blaschke function have squared moduli
$$
 a\quad(j=0),\qquad (1-a)^2a^{j-1}\quad(j\ge1).
 \tag{8.4}
$$
Using the already justified coefficient Parseval identity (5.2), these are precisely the conditional coefficient weights whose averages give the $d_1$ marginal of $\mu_{0,1}$. Tonelli therefore implies
$$
 \mathbb E_{\mu_{0,1}}d_1^2
 =\int_{\mathbb T}\sum_{j\ge1}j^2\delta(z)^2
                       (1-\delta(z))^{j-1}\,dz
 =\int_{\mathbb T}\frac{2-\delta(z)}{\delta(z)}\,dz.
 \tag{8.5}
$$
The geometric-series computation here uses
$\sum_{j\ge1}j^2a^{j-1}=(1+a)/(1-a)^3$ for $0\le a<1$.

At $z_0=-i$, the numerator in (8.2) vanishes simply and the denominator has squared modulus $1/3$. Thus with $z=-ie^{it}$,
$$
 \delta(-ie^{it})=t^2(1+O(t))
 \quad\text{as }t\to0.
 \tag{8.6}
$$
In particular the integrand in (8.5) is bounded below by a positive constant times $t^{-2}$ for sufficiently small nonzero $t$. Its integral diverges:
$$
 \boxed{\mathbb E_{\mu_{0,1}}d_1^2=\infty,\qquad
        \mathbb E_{\mu_{0,1}}|d|^2=\infty.}
 \tag{8.7}
$$
There is no conflict with (1.7), which gives the finite first moments $\mathbb E d_1=1$ and $\mathbb E|d|=3$. This example rules out deriving universal finite second occupation moments, exponential tails, or concentration from the first-moment identities and exact entry flatness alone. It does not meet or test every additional hypothesis proved for the original matrices, and no such stronger obstruction is asserted.

## 9. Exact remaining gap

The new all-time normalization, first moments, and support identity are established above for the original family. They do not imply a CUE ramp for $\mathcal O_n(U_N)$, and they leave the full weighted unequal-occupation sum uncontrolled. In particular the necessary original signed estimate
$$
 \frac1{N^2}\sum_{n\ge1}
 |\widehat b(n/N)|^2
 \left(\mathcal O_n(U_N)+\Omega_n(U_N)-\min(n,N)\right)
 \longrightarrow0
 \tag{9.1}
$$
has not been proved here, even for every allowed fixed $b$ at order two. Equation (9.1) is the first missing pair estimate, not an assumption introduced into any theorem above. Higher orders of $H_{\rm diag}$ require additional estimates beyond it.
