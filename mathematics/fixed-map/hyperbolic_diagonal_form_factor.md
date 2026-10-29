# Diagonal phase average for every hyperbolic cat map

**Claim ID:** `BGS-TRACE-131`.
**Status:** project proof. The companion arithmetic, the prime kernel trichotomy, the trace-equivalent kernel split outside the coprimality hypothesis, the prime-power count \(49\), and the revival rationals are recomputed in independent Python and C++ integer arithmetic. Both programs recompute the quantization in floating point: unitarity, flatness, symmetry, and the squared-trace identity. Python also checks the Haar values at times one through three and the second-order revival jet at one small prime. Both programs evaluate the time-one Bessel sum. A Lean 4.33.1 module certifies the companion identity on a finite range, the kernel counts, the order at \(41\), the revival cross-multiplications, and the trace-equivalent split. It does not formalize the operator expansion. No external referee.

The Weyl operators are those of `formalization/Bgs/TraceStatement.lean`, as used in `BGS-TRACE-126`. The expansion below is rederived for a general hyperbolic matrix and a general finite cosine; it does not quote the \(32\)-mode coefficient of that note. The antiunitary, when the quantization is symmetric, is the identity of `BGS-TRACE-130` applied to this matrix. `BGS-TRACE-005` and `BGS-BGS-001` remain **open**. The all-order revival law at \(m=\mathrm{ord}(S\bmod N)\) is not proved here.

## 1. Statements

Let \(S=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}\in\mathrm{SL}(2,\mathbb Z)\) with \(t=\alpha+\delta\) and \(|t|\ge 3\). Then \(\beta\neq 0\). Indeed \(\beta=0\) forces \(\alpha\delta=1\), hence \(\alpha=\delta=\pm 1\) and \(|t|=2\). Write \(\Delta=t^2-4\). Define integer sequences by \(v_0=0\), \(v_1=1\), \(v_n=t v_{n-1}-v_{n-2}\), and \(u_0=2\), \(u_n=t v_n-2 v_{n-1}\). Thus \(u_n=\operatorname{tr}(S^n)\) and
\[
S^n=v_n S-v_{n-1} I.
\]
Both sequences depend on \(S\) only through \(t\).

Let \(N\ge 3\) be odd and assume \(\gcd(\beta,N)=1\). Set \(\kappa\equiv-(2\beta)^{-1}\pmod N\) and
\[
(M_N(S))_{xy}
=N^{-1/2}\,e_N\bigl(\kappa(\delta x^2-2xy+\alpha y^2)\bigr),
\]
where \(e_N(r)=\exp(2\pi i r/N)\). This is the position-basis quantization used for \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\) in `BGS-TRACE-126`: there \(\kappa\equiv-8^{-1}\) and the quadratic form is \(3x^2-2xy+3y^2\). The prefactor is the positive square root. No Legendre symbol is inserted. The hypothesis that \(N\) is odd is the parity condition: \(2\) is a unit, so the Weyl cocycle below is defined over \(\mathbb Z/N\mathbb Z\), and the even-dimensional metaplectic sign is not present. Even \(N\) is not treated.

The Weyl operator is \((T_N(a,b)\psi)(x)=e_N(b(x+2^{-1}a))\psi(x+a)\), with \(\omega((a,b),(c,d))=ad-bc\) and
\[
T_N(u)T_N(w)=e_N\bigl(2^{-1}\omega(u,w)\bigr)\,T_N(u+w).
\]

**Theorem 1 (quantization).** Under the hypotheses above, \(M_N(S)\) is unitary, every entry has modulus \(N^{-1/2}\), and
\[
M_N(S)\,T_N(v)\,M_N(S)^{-1}=T_N(Sv).
\]
The matrix \(M_N(S)\) is symmetric if and only if \(\alpha=\delta\). Consequently, when \(\alpha=\delta\), the antiunitary \(\Theta=DK_0\) of `BGS-TRACE-130` satisfies \(\Theta^2=I\) and \(\Theta(DM_N(S))\Theta^{-1}=(DM_N(S))^\dagger\) for every real diagonal unitary \(D\). When \(\alpha\neq\delta\) that antiunitary does not reverse \(M_N(S)\). The orthogonal-class name remains the heuristic attached to the antiunitary. It is not a COE form factor.

**Corollary (Haar diagonal, times one through three).** Let \(D\) be diagonal with independent uniform phases and set \(U=DM_N(S)\). Then
\[
\mathbb E\lvert\operatorname{Tr} U\rvert^2=1,
\qquad
\mathbb E\lvert\operatorname{Tr} U^2\rvert^2=\frac{2N-1}{N},
\qquad
\mathbb E\lvert\operatorname{Tr} U^3\rvert^2=\frac{6N^2-9N+4}{N^2}.
\]
The first two equalities are the flat-matrix counts of `BGS-TRACE-127`: they use the common modulus of the entries and, at time two, the equality of the two products of scalars. They do not use \(\alpha=\delta\). At time three the one-site and two-site buckets are the same count. For three distinct sites the two orientations have the same amplitude. The sum of the quadratic form around a closed triangle changes with the orientation only through \(\sum_t(x_t^2-x_{t+1}^2)\), which is zero, whether or not \(\alpha=\delta\). The cross term \(-2xy\) is symmetric. The fixed-time limit is not stated here.

**Theorem 2 (pure trace).** For every integer \(m\ge 1\),
\[
\bigl|\operatorname{Tr} M_N(S)^m\bigr|^2
=\lvert\ker(S^m-I)\rvert,
\]
the kernel being taken on \((\mathbb Z/N\mathbb Z)^2\). In particular \(\det(S^m-I)=2-u_m\), and \(2-u_m\neq 0\).

**Theorem 3 (what depends on the trace).** Let \(p\) be an odd prime not dividing \(\beta\).

- If \(p\) does not divide \(2-u_m\), then \(\lvert\ker(S^m-I)\rvert=1\).
- If \(v_m\equiv 0\) and \(v_{m-1}\equiv -1\pmod p\), then \(S^m\equiv I\) and the kernel has order \(p^2\). For such \(p\) this congruence depends only on \(t\).
- If \(p\) divides \(2-u_m\) but \(S^m\not\equiv I\), the kernel has order \(p\).

If \(p\) does not divide \(2\Delta\), the multiplicative order of \(S\) modulo \(p\) divides \(p-(\Delta/p)\). The Legendre symbol is \(+1\) in the split case and \(-1\) in the inert case. The ramified case \(p\mid\Delta\) is not given a divisor.

If \(p\) divides \(\beta\), equal traces need not have equal kernels. For \(t=-16\),
\[
S_+=\begin{pmatrix}-20&-9\\9&4\end{pmatrix},
\qquad
S_-=\begin{pmatrix}-17&-18\\1&1\end{pmatrix}
\]
both have determinant \(1\) and \(\det(S-I)=18\), but
\[
\lvert\ker(S_+-I)\rvert=9,
\qquad
\lvert\ker(S_--I)\rvert=3
\]
on \((\mathbb Z/3\mathbb Z)^2\). Both upper-right entries are divisible by \(3\), so Theorem 1 does not apply at that prime.

At the prime power \(49\), every matrix of trace \(6\) in the certificate, including \(\begin{pmatrix}3&4\\2&3\end{pmatrix}\) and \(\begin{pmatrix}5&2\\2&1\end{pmatrix}\), has \(\lvert\ker(S^3-I)\rvert=49\), not \(7^4\). The valuation \(v_7(2-u_3)=2\) depends only on the trace. The kernel order at a prime power is not claimed to equal \(p^{2v_p(2-u_m)}\) and is not claimed for a general prime power.

**Theorem 4 (cosine kick).** Let \(\mathcal K\) be a finite set of integers not divisible by \(N\), and let \(a_k\in\mathbb R\). Let \(\varphi_k\) be independent and uniform on \(\mathbb R/2\pi\mathbb Z\), and let
\[
f(q)=\sum_{k\in\mathcal K}a_k\cos\bigl(2\pi k q/N+\varphi_k\bigr).
\]
Write \(A(\varphi)\) for multiplication by \(f\), \(U(\eta,\varphi)=\exp(i\eta A(\varphi))\,M_N(S)\), and \(\mathbb E_\varphi\) for the Haar integral on this torus. Set \(\sigma=\sum_{k\in\mathcal K}a_k^2/2\) and \(B=\sum_{k\in\mathcal K}\lvert a_k\rvert\). Then, exactly,
\[
\mathbb E_\varphi\lvert\operatorname{Tr} U(\eta,\varphi)^m\rvert^2
=\sum_{x,y}
A(x)\overline{A(y)}
\prod_{k\in\mathcal K}
J_0\bigl(\eta a_k\lvert\rho_k(x)-\rho_k(y)\rvert\bigr),
\]
where the sum runs over words of length \(m\) in \(\mathbb Z/N\mathbb Z\), \(A(x)=\prod_{t=0}^{m-1}(M_N(S))_{x_t x_{t+1}}\) with \(x_m=x_0\), \(\rho_k(x)=\sum_{t=0}^{m-1}e_N(k x_t)\), and
\[
J_0(z)=\frac1{2\pi}\int_0^{2\pi}\exp(iz\cos\theta)\,d\theta.
\]
This is the quantum average. It is not the classical orbit sum of `BGS-TRACE-129`.

If \(\gcd(2-t,N)=1\), the time-one value equals \(1\) for every real \(\eta\) and every such kick.

For every real \(\eta\) and every \(m\ge 1\),
\[
\mathbb E_\varphi\lvert\operatorname{Tr} U(\eta,\varphi)^m\rvert^2
=\lvert K_m\rvert+\eta^2 D_2(S,a,m,N)+\rho_m(N,\eta),
\]
where \(K_m=\ker(S^m-I)\) and \(D_2\) is the Gauss-sum coefficient of Section 5. It is real and satisfies \(\lvert D_2\rvert\le 2m^2\sigma\,\lvert K_m\rvert\). With \(x=m B\lvert\eta\rvert\),
\[
\lvert\rho_m(N,\eta)\rvert
\le N^2\Biggl(\frac{x^3}{6}\Bigl(2+\frac{x^3}{6}\Bigr)+\frac{x^4}{4}\Biggr).
\]

**Theorem 5 (identity revival, second order).** Let \(p\) be an odd prime not dividing \(\beta\), and let \(m\) be the multiplicative order of \(S\) modulo \(p\), so \(S^m\equiv I\). Let \(\sigma_0(p)\) be the sum of \(a_k^2/2\) over those \(k\in\mathcal K\) divisible by \(p\). Then
\[
D_2(S,a,m,p)=-m\bigl(\sigma-\sigma_0(p)\bigr)\,p^2.
\]
If \(p\) divides no frequency in \(\mathcal K\), then \(\sigma_0(p)=0\). A frequency divisible by \(p\) is a zero-mode defect: that mode acts as a scalar in the Weyl calculus modulo \(p\). The identity \(S^m\equiv I\) is not implied by \(p\mid(2-u_m)\) alone; the unipotent case of Theorem 3 has kernel order \(p\), and the coefficient \(-m(\sigma-\sigma_0)p^2\) is not claimed there.

For the kick \(a_1=1\), \(a_2=1/2\) one has \(\sigma=5/8\). At \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\), \(p=41\), \(m=5\), and at \(S=\begin{pmatrix}2&1\\3&2\end{pmatrix}\), \(p=5\), \(m=3\),
\[
D_2=-\frac{42025}{8},
\qquad
D_2=-\frac{375}{8}
\]
respectively, and \(\sigma_0=0\) in both cases.

**Boundary.** Theorems 4 and 5 average an auxiliary torus of Fourier phases. They do not evaluate the fixed kick at one phase, the signed off-diagonal sum, or the propagator at times of order \(N\). The second-order revival identity is not an exact formula for \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\) at \(m=\mathrm{ord}(S\bmod N)\). The fixed-time limit, the COE value \(2m\), and the CUE value \(m\) are not claimed; those scalings are `BGS-TRACE-132`. The Kurlberg–Rudnick matrix-element moments are not inputs. Hannay and Berry, Physica D 1 (1980), 267–290, introduced the quantization of linear torus maps. Kurlberg and Rudnick, Duke Mathematical Journal 103 (2000), 47–77, arXiv:chao-dyn/9901031, Section 1.2, record exact Egorov for every \(A\in\mathrm{SL}(2,\mathbb Z)\) and, in the companion discussion of degeneracies, the mean multiplicity \(N/\mathrm{ord}(A,N)\). Those statements are prior context. The normalization, the kernel trichotomy under \(\gcd(\beta,p)=1\), the cosine expansion, and the defect split are proved in this note and are not quoted from those papers. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. Companion arithmetic

Cayley–Hamilton gives \(S^2-tS+I=0\), so the powers satisfy the scalar recurrence. The matrix sequence \(v_n S-v_{n-1}I\) agrees with \(S^n\) at \(n=0\) and \(n=1\), because \(v_{-1}=-1\) from \(v_1=t v_0-v_{-1}\). Therefore \(S^n=v_n S-v_{n-1}I\) and \(u_n=\operatorname{tr}(S^n)\).

The determinant identity \(v_n^2-t v_n v_{n-1}+v_{n-1}^2=1\) holds at \(n=1\). If it holds at \(n\), the recurrence \(v_{n+1}=t v_n-v_{n-1}\) substitutes into the same quadratic and returns the value at \(n\). Thus it holds for every \(n\ge 1\), and \(\det S^n=1\) is consistent. Expanding \(\det(S^n-I)\) and inserting this identity produces
\[
\det(S^n-I)=2-(t v_n-2 v_{n-1})=2-u_n.
\]
The same recurrence gives \(u_n(-t)=(-1)^n u_n(t)\). For \(t\ge 3\) one has \(u_1=t\) and \(u_{n+1}=t u_n-u_{n-1}\ge 3u_n-u_{n-1}\). Starting from \(u_1\ge 3\) and \(u_2=t^2-2>u_1\), the inequality \(u_n>u_{n-1}\) propagates, so \(u_n\ge 3\). Hence \(\lvert u_n\rvert\ge 3\) for every \(n\ge 1\) and every \(\lvert t\rvert\ge 3\), and \(2-u_n\neq 0\).

## 3. Quantization, Egorov, symmetry

Every entry of \(M_N(S)\) is a complex number of modulus \(N^{-1/2}\), because the exponent is real. For the columns, 
\[
\sum_x (M_N)_{xy}\overline{(M_N)_{xy'}}
=N^{-1}e_N\bigl(\kappa\alpha(y^2-y'^2)\bigr)
\sum_x e_N\bigl(-2\kappa x(y-y')\bigr).
\]
Here \(-2\kappa\equiv\beta^{-1}\pmod N\) is a unit. The geometric sum equals \(N\) if \(y\equiv y'\) and equals \(0\) otherwise. The same computation with the roles of the two variables reversed shows that the rows are orthonormal. Thus \(M_N(S)\) is unitary. The quadratic coefficient \(\kappa\alpha\) was not required to be a unit: it cancels between a column and itself.

For Egorov, compare \((M_N T_N(a,b)\psi)(x)\) with \((T_N(S(a,b))M_N\psi)(x)\). The quadratic parts in \((x,z)\) agree. The coefficient of \(z\) forces the first coordinate of \(S(a,b)\) to be \(\alpha a+\beta b\), and the coefficient of \(x\) forces the second coordinate to be \(\gamma a+\delta b\), because \(\alpha\delta-\beta\gamma=1\) and \(2\kappa=-\beta^{-1}\). The constant terms then differ by
\[
\frac{\alpha}{2\beta}(\beta\gamma-\alpha\delta+1)=0.
\]
All identities are polynomial identities over \(\mathbb Z[1/2,1/\beta]\) and descend to \(\mathbb Z/N\mathbb Z\). Therefore \(M_N T_N(v)=T_N(Sv)M_N\).

The exponent of \((M_N)_{xy}\) minus the exponent of \((M_N)_{yx}\) is \(\kappa(\delta-\alpha)(x^2-y^2)\). If \(\alpha=\delta\) the matrix is symmetric. If \(\alpha\neq\delta\), then \(\kappa(\delta-\alpha)\) is a unit times a nonzero integer, and the value at \((x,y)=(1,0)\) is nonzero in \(\mathbb Z/N\mathbb Z\) for \(N>1\). A unitary symmetric matrix satisfies \(M^{-1}=\overline M=K_0 M K_0\). The antiunitary argument of `BGS-TRACE-130` then applies verbatim to \(D M_N(S)\). If \(\alpha\neq\delta\), then \(M^{-1}=\overline{M^{\mathsf T}}\neq\overline M\), so \(K_0 M K_0\neq M^{-1}\).

The Haar corollary is the occupation count of `BGS-TRACE-127`, Sections 3 and 4, with one change at the triangle. Write \(Q(u,v)=\kappa(\delta u^2-2uv+\alpha v^2)\). For a closed word the sum of the square terms is \(\kappa(\alpha+\delta)\sum_i x_i^2\) in every ordering. The difference of two orientations is a sum of cross terms. On a triangle those cross terms are \(-2\kappa\) times the same three products \(xy\), \(yz\), and \(zx\), read in either cyclic order. Hence the two amplitudes agree for every \(S\) in the family, and the count \((6N^2-9N+4)/N^2\) follows as in that note.

## 4. Trace closure and the prime trichotomy

The argument of `BGS-TRACE-126`, Section 3, uses only the cocycle and phase-free Egorov. It applies to \(M_N(S)\). If \((I-S^m)w\equiv v\), then
\[
\operatorname{Tr}\bigl(T_N(v)M_N(S)^m\bigr)
=e_N\bigl(2^{-1}\omega(w,S^m w)\bigr)\,\operatorname{Tr} M_N(S)^m,
\]
and the phase depends only on \(v\). If \(v\) is not in the image, the trace vanishes, because the image equals the symplectic orthogonal of the kernel: the two subgroups have the same order by the first isomorphism theorem and by the comparison of a subgroup of \((\mathbb Z/N\mathbb Z)^2\) with its dual through \(\omega\). Hilbert–Schmidt orthogonality of the Weyl basis then yields \(\lvert\operatorname{Tr} M_N^m\rvert^2=\lvert K_m\rvert\).

Over the field \(\mathbb F_p\), with \(p\nmid\beta\), the determinant \(2-u_m\) is the only invariant needed for invertibility. If it is nonzero, the kernel is trivial. The matrix \(S^m-I=v_m S-(v_{m-1}+1)I\) equals zero if and only if \(v_m\equiv 0\) and \(v_{m-1}\equiv-1\), because the upper-right entry is \(v_m\beta\) and \(p\nmid\beta\). In that case the kernel is the whole plane. If the determinant vanishes but the matrix is not zero, its rank is \(1\) and the kernel has order \(p\). This is the unipotent defect. It occurs: for \(S=\begin{pmatrix}2&1\\1&1\end{pmatrix}\), \(t=3\), one has \(u_2=7\) and \(2-u_2=-5\), while \(S^2\not\equiv I\pmod 5\), and the kernel has order \(5\).

If \(p\nmid 2\Delta\), the roots of \(X^2-tX+1\) are distinct and lie in \(\mathbb F_p\) or in \(\mathbb F_{p^2}\). In the split case the root \(\lambda\) lies in \(\mathbb F_p^\times\), so \(\lambda^{p-1}=1\). In the inert case the Frobenius sends \(\lambda\) to the other root \(\lambda^{-1}\), hence \(\lambda^p=\lambda^{-1}\) and \(\lambda^{p+1}=1\). The matrix is diagonalizable, so \(S^m\equiv I\) if and only if \(\lambda^m=1\). The order divides \(p-(\Delta/p)\).

The two matrices of trace \(-16\) in Theorem 3 are an integer identity: both determinants equal \(1\), both values of \(\det(S-I)\) equal \(18\), and the kernels modulo \(3\) are \(9\) and \(3\). The upper-right entries \(-9\) and \(-18\) are divisible by \(3\).

For the prime power, \(u_3(6)=198\) and \(2-u_3=-196=-4\cdot 49\). The kernel count on \((\mathbb Z/49\mathbb Z)^2\) returns \(49\) for both trace-\(6\) matrices named in Theorem 3. The count \(7^4=2401\) would require every factor of \(7\) in the modulus to contribute two dimensions. It does not.

## 5. The cosine average

Multiplication by \(e_N(kq)\) is \(T_N(0,k)\). Therefore
\[
A(\varphi)
=\sum_{k\in\mathcal K}\frac{a_k}{2}
\Bigl(e^{i\varphi_k}T_N(0,k)+e^{-i\varphi_k}T_N(0,-k)\Bigr),
\]
provided \(N\nmid k\), so that \((0,k)\not\equiv(0,-k)\). Each pair contributes \(a_k^2/4+a_k^2/4=a_k^2/2\) to the symbol energy, and \(\sigma\) is that sum. Each \(T_N(v)\) is unitary, so \(\lVert A(\varphi)\rVert\le B\).

The propagator is diagonal in the position basis times \(M_N(S)\). Expanding the trace and averaging the characters \(e^{i\varphi_k}\) produces a factor for each \(k\). The sum of cosines along a word minus the sum along a second word equals \(\lvert\rho_k(x)-\rho_k(y)\rvert\cos(\varphi_k+\alpha)\) for a phase \(\alpha\) independent of \(\varphi_k\). The integral of \(\exp(i\eta a_k r\cos\theta)\) is \(J_0(\eta a_k r)\). Independence of the angles multiplies these factors. This is Theorem 4's exact formula. The classical sum in `BGS-TRACE-129` averages a phase over torus points without the matrix amplitudes \(A(x)\overline{A(y)}\). The two expressions agree only in situations that note does not claim.

At time one the words are sites. The diagonal matrix element is \(e_N(\kappa(t-2)x^2)N^{-1/2}\), because the quadratic form on the diagonal is \(\kappa(\alpha+\delta-2)x^2\). The double sum becomes
\[
N^{-1}\sum_{h,z}
e_N\bigl(\kappa(t-2)h(2z+h)\bigr)
\prod_k J_0\bigl(\eta a_k\lvert e_N(kh)-1\rvert\bigr).
\]
The inner sum over \(z\) equals \(N\) when \(N\) divides \((t-2)h\), since \(2\kappa\equiv-\beta^{-1}\) is a unit, and equals \(0\) otherwise. If \(\gcd(2-t,N)=1\), the only surviving shift is \(h=0\). There \(J_0(0)=1\), and the sum equals \(1\).

The order-two expansion is the interaction-picture argument of `BGS-TRACE-126`, Section 4, with this symbol and this matrix. Conjugation gives
\[
U^m
=\Biggl(\prod_{j=0}^{m-1}\exp(i\eta A_j)\Biggr)M_N^m,
\qquad
A_j=M_N^j A M_N^{-j}.
\]
The integral remainder of Taylor's theorem in \(\mathbb C\), the bound \(\lvert f'''\rvert\le N(mB)^3\), and the splitting of \(\lvert P_2\rvert^2\) into the quadratic jet, the cubic term, and the quartic term are unchanged. The substitution \(\varphi\mapsto\varphi+\pi\) sends every coefficient to its negative, so the averaged cubic term vanishes and the quartic term is kept in \(\rho\). The same estimates give the displayed remainder.

A monomial in the coefficients averages to zero unless each pair has total charge zero. Hence \(\mathbb E f_1=0\) and
\[
\mathbb E\lvert f_1\rvert^2
=m^2\lvert K_m\rvert\sum_{v\in\operatorname{Im}(I-S^m)}\lvert c_v\rvert^2.
\]
The quadratic words \(T_N(S^j v)T_N(-S^k v)\) contribute the cocycle \(e_N(-2^{-1}\omega(v,S^{k-j}v))\) and a Gauss phase when \((S^j-S^k)v\) lies in the image. Collecting \(2\operatorname{Re}(\overline{Z_m}\,\mathbb E f_2)\) produces
\[
D_2
=\lvert K_m\rvert\Biggl(
m^2\sum_{v\in\operatorname{Im}}\lvert c_v\rvert^2
-m\sigma
-2\operatorname{Re}\sum_{j<k}\sum_v\lvert c_v\rvert^2\,\theta(j,k,v)
\Biggr),
\]
with \(\lvert\theta\rvert\le 1\). There are \(m(m-1)/2\) pairs \((j,k)\) and the energy sum is at most \(\sigma\), so \(\lvert D_2\rvert\le 2m^2\sigma\,\lvert K_m\rvert\).

For the diagonal modes, \(\omega((0,\ell),S^\delta(0,\ell))=-\ell^2\beta v_\delta\). The phase therefore sees \(\beta\) and the companion sequence \(v_\delta\), not the trace alone. The image condition sees the whole matrix \(S\).

Now let \(S^m\equiv I\pmod p\). The image of \(I-S^m\) is \(\{0\}\), and \(\lvert K_m\rvert=p^2\). A symbol mode lies in that image precisely when it is \(0\) modulo \(p\), that is, when \(p\) divides its frequency. For \(1\le\delta<m\) the matrix \(S^\delta-I\) is invertible, so \((S^j-S^k)v\equiv 0\) if and only if \(v\equiv 0\). On those modes the cocycle and the Gauss phase both vanish, and \(\theta=1\). On every other mode \(\theta=0\). The parenthesis collapses to \(-m(\sigma-\sigma_0(p))\), which is Theorem 5.

The two numerical revivals are this identity. For \(a_1=1\) and \(a_2=1/2\), \(\sigma=1/2+1/8=5/8\). Neither frequency is divisible by \(41\) or by \(5\). The order of \(\begin{pmatrix}3&4\\2&3\end{pmatrix}\) modulo \(41\) is \(5\), and \(41^2=1681\), so \(D_2=-5\cdot(5/8)\cdot 1681=-42025/8\). The order of \(\begin{pmatrix}2&1\\3&2\end{pmatrix}\) modulo \(5\) is \(3\), so \(D_2=-3\cdot(5/8)\cdot 25=-375/8\).

## 6. Self-audit

The column computation shows unitarity without a hypothesis on \(\gcd(\alpha,N)\). A draft that required \(\alpha\) to be a unit was rejected by the matrices \(\begin{pmatrix}6&1\\5&1\end{pmatrix}\) at \(N=9\) and \(\begin{pmatrix}3&4\\2&3\end{pmatrix}\) at every odd modulus in the certificate: the quadratic coefficient in one variable vanishes modulo a divisor of \(N\), and the geometric sum still orthonormalizes the matrix.

The diagonal phase is \(\kappa(t-2)x^2\), not \(\kappa t x^2\). The factor \(t-2=-(2-u_1)\) is what matches the kernel of \(S-I\). Replacing it by \(t\) makes the time-one sum disagree with \(\lvert\operatorname{Tr} M_N\rvert^2\) at \(N=9\) for the model matrix.

The identity revival was checked by a direct Bessel evaluation at \(N=5\), \(m=3\), \(\eta=0.02\): \((\mathbb E-25)/\eta^2\) equals \(-46.858\), against \(-375/8=-46.875\). The difference is the size of the next term in \(\eta\), not a second value of \(D_2\).

The kernel split at trace \(-16\) is outside Theorem 1. It is recorded so that the dependence on \(S\) is not overstated: the trace determines the prime kernel only together with \(p\nmid\beta\).

No limit \(2m\), no limit \(m\), and no exact revival formula is stated. The fixed kick at one phase is not evaluated.

## 7. Certificates

- `computations/verification/hyperbolic_diagonal_form_factor.py`
- `computations/cpp/hyperbolic_diagonal_form_factor.cpp`
- `formalization/Bgs/HyperbolicDiagonalFormFactor.lean`
- `evidence/executions/20261029/hyperbolic-diagonal-form-factor/README.md`

Lean decides the companion identity for the listed traces and indices, \(\det(S^n-I)=2-u_n\) on that range, the kernels at the primes and at \(49\), the order \(5\) modulo \(41\), the two revival cross-multiplications, and the trace-equivalent kernels \(9\) and \(3\). Python and C++ recompute the same integers. Python checks the Haar values and the revival jet; both programs evaluate the time-one Bessel sum. A pass does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
