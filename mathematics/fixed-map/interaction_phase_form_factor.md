# Phase-averaged form factor and classical symmetry defects

**Claim ID:** `BGS-TRACE-126`.
**Status:** project proof. The rational symbol identities, the cyclotomic nonvanishing witness, and the prime-revival coefficient are recomputed in independent Python and C++ integer arithmetic. The stable parity and reversal defects are the same integer sums. A Lean 4.33.1 module certifies the scaled Fourier table, its energy, its parity energy, its majorant, and the unreduced reversal sum. No external referee.

The argument uses the phase-free conjugation from `BGS-TRACE-117`, Section 2, and no other statement from that note.

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**. The phase average below is an average over an auxiliary 16-torus. It is not a theorem about the fixed kick at a single phase.

## 1. Statements

Let \(N\ge 3\) be odd. The operators \(T_N(a,b)\), \(M_N\) and \(A_N\) are those of `formalization/Bgs/TraceStatement.lean`: \(A_N=\sum c_{k\ell}\,T_N(\ell,k)\), the sum runs over the Fourier support of \(f-1/10\), and
\[
(T_N(a,b)\psi)(x)=e_N\bigl(b(x+2^{-1}a)\bigr)\psi(x+a).
\]
Write \(v=(a,b)\), \(T_N(v)=T_N(a,b)\) and \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\). The symplectic form is \(\omega(v,w)=ad-bc\) for \(w=(c,d)\). Let \(\eta\in\mathbb R\) and
\[
U_N(\eta)=\exp(i\eta A_N)\,M_N.
\]
The frozen family is the case \(\eta=\tau N\) with \(\tau=10^{-80}\). The identities in this note hold for every real \(\eta\).

The nonzero modes come in 16 pairs \(\{v,-v\}\). A phase vector \(\varphi\) assigns to the \(r\)-th pair an angle \(\varphi_r\in\mathbb R/2\pi\mathbb Z\). Fix one representative \(v_r\) of each pair, and define
\[
c_v(\varphi)=c_v\,e^{i\sigma(v)\varphi_r},\qquad
\sigma(v_r)=1,\quad\sigma(-v_r)=-1.
\]
The phased kick \(A_N(\varphi)\) uses these coefficients. Hermitian symmetry \(c_{-v}=\overline{c_v}\) is preserved. Write \(U_N(\eta,\varphi)\) for the corresponding propagator, and write \(\mathbb E_\varphi\) for the normalized Haar integral on the 16-torus.

Let \(K_m=\ker(S^m-I)\) on \((\mathbb Z/N\mathbb Z)^2\), and let \(\sigma=\sum\lvert c_v\rvert^2\).

**Theorem 1 (phase-averaged form factor).** For every odd \(N\ge 3\), every integer \(m\ge 1\) and every real \(\eta\),
\[
\mathbb E_\varphi\lvert\operatorname{Tr} U_N(\eta,\varphi)^m\rvert^2
=\lvert K_m\rvert+\eta^2 D_2(N,m)+\rho_m(N,\eta).
\]
The coefficient \(D_2(N,m)\) is real and is the finite sum of Gauss sums in Section 4. It satisfies
\[
\lvert D_2(N,m)\rvert\le 2m^2\sigma\,\lvert K_m\rvert.
\]
If \(x=m B\lvert\eta\rvert\) with the majorant \(B=184981/160000\) of Section 2, then
\[
\lvert\rho_m(N,\eta)\rvert
\le N^2\cdot\frac{x^3}{6}\Bigl(2+\frac{x^3}{6}\Bigr).
\]
In particular the identity is an explicit absolutely convergent series in \(\eta\). The hypothesis \(m\lvert\eta\rvert\le 5/6\) implies \(x\le 1\), since \(B<6/5\).

**Corollary (prime revival, second order).** Let \(N\) be an odd prime and let \(m\) be the multiplicative order of \(S\) modulo \(N\). Then no nonzero symbol mode is fixed by \(S^\delta\) for \(1\le\delta<m\), the image of \(I-S^m\) is \(\{0\}\), and
\[
D_2(N,m)=-m\sigma N^2,\qquad
\sigma=\frac{66033}{160000}.
\]
Thus
\[
\mathbb E_\varphi\lvert\operatorname{Tr} U_N(\eta,\varphi)^m\rvert^2
=N^2\bigl(1-m\sigma\eta^2\bigr)+\rho_m(N,\eta),
\]
with the same remainder. At \(N=41\), the order is \(5\) and
\[
D_2(41,5)=-\frac{111001473}{32000}.
\]

**Theorem 2 (fixed kick through order two).** At the single phase \(\varphi=0\),
\[
\lvert\operatorname{Tr} U_N(\eta)^m\rvert^2
=\lvert K_m\rvert+\eta L_1(N,m)+\eta^2 Q(N,m)+r_m(N,\eta),
\]
where the remainder obeys the same bound as \(\rho_m\), the quadratic coefficient \(Q\) is the same word sum as \(D_2\) before the phase average, and
\[
L_1(N,m)=-2m\,\lvert K_m\rvert\,\operatorname{Im}\Sigma(N,m),
\]
\[
\Sigma(N,m)=\sum_{v\in\operatorname{Im}(I-S^m)}c_v\,e_N(\psi_m(v)).
\]
The phase \(\psi_m\) is the quadratic Gauss phase of Section 3. The linear coefficient is not the zero function of \((N,m)\): at \(N=11\) and \(m=3\), \(\lvert K_3\rvert=1\) and \(4000\bigl(\Sigma-\overline\Sigma\bigr)\) is the nonzero element
\[
3600+7200\zeta+3224\zeta^2+3600\zeta^3+3400\zeta^4+3400\zeta^5+3800\zeta^6+3800\zeta^7+3600\zeta^8+3976\zeta^9
\]
of \(\mathbb Z[\zeta_{11}]/(\Phi_{11})\). Hence \(\operatorname{Im}\Sigma(11,3)\ne 0\).

**Theorem 3 (two classical symmetries).** Let \((P\psi)(x)=\psi(-x)\) and let \(K_0\) be complex conjugation of values in the position basis. For every odd \(N\),
\[
PM_N=M_NP,\qquad K_0M_NK_0=M_N^{-1}.
\]
The parity defect and the reversal defect
\[
\Delta_{\mathrm{par}}(N)=N^{-1}\lVert PA_NP-A_N\rVert_{\mathrm{HS}}^2,
\qquad
\Delta_{\mathrm{rev}}(N)=N^{-1}\lVert K_0A_NK_0-M_N^{-1}A_NM_N\rVert_{\mathrm{HS}}^2
\]
are the squared \(\ell^2\) norms of the folded symbol differences in Section 5.

- \(\Delta_{\mathrm{par}}(7)=\Delta_{\mathrm{rev}}(7)=0\). Consequently \(P\) commutes with \(U_7(\eta)\) for every real \(\eta\), and \(K_0U_7(\eta)K_0=U_7(\eta)^{-1}\).
- For every odd \(N\ne 7\), \(\Delta_{\mathrm{par}}(N)>0\). For every odd \(N\ge 19\),
  \[
  \Delta_{\mathrm{par}}(N)=\frac{663}{1000000}.
  \]
- For every odd \(N\ne 7\), \(\Delta_{\mathrm{rev}}(N)>0\). For every odd \(N\ge 79\),
  \[
  \Delta_{\mathrm{rev}}(N)=\frac{66031}{80000}.
  \]
The finitely many odd moduli from \(3\) through \(77\) are part of the integer certificate. Thus, outside dimension \(7\), neither symmetry survives for the kicked propagator.

**Boundary.** Theorem 1 averages an auxiliary ensemble. Theorem 2 expands the fixed kick; it does not estimate the signed off-diagonal sum in the Abel statistic. The prime-revival corollary is a second-order identity. If \(m\) is comparable to \(N\) and \(m B\lvert\eta\rvert\) stays bounded, then \(\eta^2 N m^2=O(1/N)\) whenever \(\eta=\tau N\) and \(m\le N\), so a limit with \(\tau^2 N^3\) tending to a positive constant lies outside the truncation. No such limit is proved. The second and fourth moments in Kurlberg–Rudnick, arXiv:math/0302277, were re-read from that abstract on 29 October 2026: they concern normalized Hecke matrix elements of the desymmetrized quantum cat map. They are not inputs, and they do not evaluate \(N^{-1}\lvert\operatorname{Tr}U_N^m\rvert\). Theorem 3 concerns parity and position-basis conjugation only. An \(N\)-dependent antiunitary outside that pair is not classified. Dimension \(7\) is an aliasing identity, not a spectral-limit theorem. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. Symbol, cocycle and Egorov

The coefficient \(c_{k\ell}\) is `fCoeff(k, \ell)` in `TraceStatement.lean`. Exactly 32 modes are nonzero. They satisfy \(c_{-k,-\ell}=\overline{c_{k\ell}}\), the mode \((k,\ell)=(7,0)\) has coefficient \(9/20\), and
\[
\sigma=\sum\lvert c_{k\ell}\rvert^2=\frac{66033}{160000}.
\]
Scaling by \(4000\) clears denominators: if \(d_v=4000 c_v\), then \(\sum\lvert d_v\rvert^2=6603300\). Each \(\lvert c_v\rvert^2=p/q\) in lowest terms obeys
\[
\sqrt{p/q}<\bigl(\lfloor\sqrt{pq}\rfloor+1\bigr)/q,
\]
and the sum of these rational majorants is \(B=184981/160000\). Hence \(\sum\lvert c_v\rvert<B\). Every \(T_N(v)\) is unitary, so \(\lVert A_N\rVert\le\sum\lvert c_v\rvert<B\). The same bound holds for every phased kick.

The product rule is
\[
T_N(u)T_N(w)=e_N\bigl(2^{-1}\omega(u,w)\bigr)\,T_N(u+w).
\]
In particular \(T_N(v)^*=T_N(-v)\) and \(T_N(v)^{-1}=T_N(-v)\). A direct expansion gives
\[
T_N(z)T_N(v)T_N(-z)=e_N(\omega(z,v))\,T_N(v).
\]
The trace \(\operatorname{Tr}(T_N(v)^*T_N(w))\) equals \(N\) if \(v\equiv w\pmod N\) and equals \(0\) otherwise, so
\[
\Bigl\lVert\sum_v a_v T_N(v)\Bigr\rVert_{\mathrm{HS}}^2=N\sum_v\lvert a_v\rvert^2.
\]

**Lemma (Egorov).** \(M_NT_N(a,b)M_N^{-1}=T_N(S(a,b))\).

This is the phase-free conjugation of `BGS-TRACE-117`, Section 2, in the labelling \(T_N(a,b)=W_N(b,a)\). That section compares the entries of \(M_NW_N(k,\ell)\) and \(W_N(C(k,\ell))M_N\). Both exponents expand to the same polynomial
\[
-\frac{kl}2+kz-\frac{3\ell^2}8-\frac{\ell x}4+\frac{3\ell z}4-\frac{3x^2}8+\frac{xz}4-\frac{3z^2}8,
\]
and the halves and quarters are the modular inverses of \(2\), \(4\) and \(8\). Substituting \((k,\ell)=(b,a)\) sends \(C(b,a)\) to the frequency vector of \(T_N(S(a,b))\). The only input taken from that note is this identity. Both verifiers recompute it on a fixed set of modes. Iterating gives \(M_N^j A_N M_N^{-j}=\sum_v c_v T_N(S^j v)\), and the same holds with phased coefficients.

**Lemma (gauge).** For integer lifts \(a,b\) and odd \(N\),
\[
T_N(a,b)=(-1)^{ab}\,T_N^{\mathrm{KR}}(a,b),
\]
where the right-hand operator has entries \(\exp(\pi i ab/N)\exp(2\pi i bx/N)\) on the diagonal \(y\equiv x+a\). Indeed \(2^{-1}\equiv(N+1)/2\pmod N\), so the raw phase contributes an extra factor \(\exp(\pi i ab)=(-1)^{ab}\). This identifies the two normalizations. No theorem below quotes a trace formula from the other normalization.

## 3. Quadratic Gauss sums

Let \(Z_m=\operatorname{Tr}(M_N^m)\).

**Lemma (trace closure).** If \(v\notin\operatorname{Im}(I-S^m)\), then \(\operatorname{Tr}(T_N(v)M_N^m)=0\). If \((I-S^m)w\equiv v\), then
\[
\operatorname{Tr}(T_N(v)M_N^m)=e_N(\psi_m(w))\,Z_m,
\qquad
\psi_m(w)=2^{-1}\omega(w,S^m w).
\]
The phase depends only on \(v\). Furthermore \(\lvert Z_m\rvert^2=\lvert K_m\rvert\).

The transport identity \(M_N^m T_N(-w)=T_N(-S^m w)M_N^m\) and the cocycle give
\[
T_N(w)M_N^m T_N(-w)=e_N(-\psi_m(w))\,T_N((I-S^m)w)\,M_N^m.
\]
Taking traces yields the displayed formula whenever a preimage \(w\) exists. If \(w'=w+k\) with \(S^m k=k\), the cross terms in \(\omega(w',S^m w')\) cancel, so the phase is constant on the coset.

The image is contained in the symplectic orthogonal \(K_m^\perp\). For the reverse inclusion, the first isomorphism theorem gives \(\lvert\operatorname{Im}(I-S^m)\rvert=N^2/\lvert K_m\rvert\). A subgroup of \((\mathbb Z/N\mathbb Z)^2\) is the reduction of the image of a \(2\times 2\) integer matrix, and elementary row and column operations put that matrix in Smith form \(\operatorname{diag}(d_1,d_2)\) with \(d_1\mid d_2\). Hence the subgroup is isomorphic to \(\mathbb Z/\gcd(d_1,N)\times\mathbb Z/\gcd(d_2,N)\), and the group of homomorphisms into \(\mathbb Z/N\mathbb Z\) has the same order. The map \(g\mapsto\omega(g,\cdot)\) from \((\mathbb Z/N\mathbb Z)^2\) to that dual therefore has image of size at most \(\lvert K_m\rvert\), which means \(\lvert K_m^\perp\rvert\ge N^2/\lvert K_m\rvert\). The two inclusions force \(\operatorname{Im}(I-S^m)=K_m^\perp\).

If \(v\notin K_m^\perp\), some \(k\in K_m\) has \(\omega(k,v)\ne 0\). Then \(T_N(k)\) commutes with \(M_N^m\), while \(T_N(k)T_N(v)T_N(-k)=e_N(\omega(k,v))T_N(v)\). The trace of \(T_N(v)M_N^m\) equals \(e_N(\omega(k,v))\) times itself, so the trace vanishes.

Finally \(\sum_v\lvert\operatorname{Tr}(T_N(v)M_N^m)\rvert^2=N^2\) by Hilbert–Schmidt orthogonality and \(\lVert M_N^m\rVert_{\mathrm{HS}}^2=N\). The nonzero summands are exactly the image, and each has modulus \(\lvert Z_m\rvert\), so \(\lvert\operatorname{Im}\rvert\,\lvert Z_m\rvert^2=N^2\). Therefore \(\lvert Z_m\rvert^2=\lvert K_m\rvert\).

## 4. Interaction picture and the phase average

Conjugation preserves the exponential series, so
\[
U_N(\eta,\varphi)^m
=\Biggl(\prod_{j=0}^{m-1}\exp\bigl(i\eta A_j(\varphi)\bigr)\Biggr)M_N^m,
\]
with \(A_j(\varphi)=M_N^j A_N(\varphi)M_N^{-j}\) and with the product ordered from \(j=0\) on the left to \(j=m-1\) on the right. Write \(W(\eta)\) for the product and \(f(\eta)=\operatorname{Tr}(W(\eta)M_N^m)\). Then \(f(0)=Z_m\).

Each factor \(\exp(i\eta A_j)\) is unitary. The Leibniz rule bounds the \(n\)th derivative of an \(m\)-fold product by \((m\lVert A\rVert)^n\). Hence \(\lvert f^{(n)}(t)\rvert\le N(m B)^n\) for every \(t\). Lagrange's remainder gives
\[
f(\eta)=Z_m+\eta f_1+\eta^2 f_2+R,
\qquad
\lvert R\rvert\le N\frac{x^3}{6},
\]
and the elementary comparison \(\bigl\lvert\lvert f\rvert^2-\lvert Z_m+\eta f_1+\eta^2 f_2\rvert^2\bigr\rvert\le(2N+\lvert R\rvert)\lvert R\rvert\) is the remainder in Theorems 1 and 2.

Differentiating the product yields
\[
f_1=i\sum_{j<m}\operatorname{Tr}(A_j M_N^m)=im\operatorname{Tr}(A_N M_N^m),
\]
because \(M_N^j\) commutes with \(M_N^m\). The same commutation gives \(\operatorname{Tr}(T_N(S^j v)M_N^m)=\operatorname{Tr}(T_N(v)M_N^m)\). The coefficient of \(\eta^2\) is
\[
f_2=-\operatorname{Tr}\Biggl(\Biggl(\sum_{j<m}\frac{A_j^2}{2}+\sum_{j<k}A_j A_k\Biggr)M_N^m\Biggr).
\]

A monomial \(\prod_s c_{v_s}(\varphi)\) averages to zero unless every pair has total charge zero. Consequently \(\mathbb E_\varphi f_1=0\). The charge of a single mode is \(\pm 1\), so the phase average is an even function of \(\eta\): replacing \(\varphi\) by \(\varphi+\pi\) sends every coefficient to its negative. Only even powers survive.

For the quadratic term, \(\mathbb E_\varphi\bigl(c_v(\varphi)\overline{c_w(\varphi)}\bigr)\) vanishes unless \(v=w\), and then it equals \(\lvert c_v\rvert^2\). Therefore
\[
\mathbb E_\varphi\lvert f_1\rvert^2
=m^2\sum_v\lvert c_v\rvert^2\,\lvert\operatorname{Tr}(T_N(v)M_N^m)\rvert^2
=m^2\lvert K_m\rvert\sum_{v\in\operatorname{Im}(I-S^m)}\lvert c_v\rvert^2.
\]
The average \(\mathbb E_\varphi(c_v(\varphi)c_w(\varphi))\) vanishes unless \(w=-v\), and then it equals \(\lvert c_v\rvert^2\). Since \(N\) is odd and \(c_0=0\), one has \(-v\ne v\) on the support. Hence
\[
\mathbb E_\varphi(A_j A_k)
=\sum_v\lvert c_v\rvert^2\,T_N(S^j v)\,T_N(-S^k v).
\]
The cocycle and the invariance \(\omega(Su,Sw)=\omega(u,w)\) give, for \(j<k\) and \(\delta=k-j\),
\[
T_N(S^j v)\,T_N(-S^k v)
=e_N\bigl(-2^{-1}\omega(v,S^\delta v)\bigr)\,T_N((S^j-S^k)v).
\]
Closing the trace with Section 3 produces a factor \(Z_m\) when \((S^j-S^k)v\) lies in the image and a factor \(0\) otherwise. The diagonal terms \(j=k\) contribute \(\sigma Z_m/2\) each. Collecting the real part \(2\operatorname{Re}(\overline{Z_m}\,\mathbb E f_2)\) gives
\[
D_2(N,m)
=\lvert K_m\rvert\Biggl(
m^2\sum_{v\in\operatorname{Im}}\lvert c_v\rvert^2
-m\sigma
-2\operatorname{Re}\sum_{j<k}\sum_v\lvert c_v\rvert^2\,\theta(j,k,v)
\Biggr),
\]
where \(\theta(j,k,v)\) is the product of the cocycle phase and the Gauss phase, or zero when the transported difference misses the image. Each \(\lvert\theta\rvert\le 1\), and there are \(m(m-1)/2\) pairs \((j,k)\), so \(\lvert D_2\rvert\le 2m^2\sigma\lvert K_m\rvert\).

This is Theorem 1. The same expansion without the average is Theorem 2, and
\[
2\operatorname{Re}(\overline{Z_m} f_1)
=2\operatorname{Re}\bigl(\overline{Z_m}\,im Z_m\Sigma\bigr)
=-2m\lvert K_m\rvert\operatorname{Im}\Sigma.
\]

At a prime \(N\), \(S^\delta-I\) is invertible whenever \(S^\delta\not\equiv I\). If \(m\) is the order, this holds for every \(1\le\delta<m\), so a symbol mode satisfies \(S^\delta v\equiv v\) only for \(v\equiv 0\), which is not a mode. Also \(S^m\equiv I\), so the image of \(I-S^m\) is \(\{0\}\) and the first sum in \(D_2\) vanishes. Every off-diagonal \(\theta\) vanishes with it. The remaining term is \(-m\sigma N^2\). Both verifiers check that the order modulo \(41\) is exactly \(5\), that each proper power is invertible, and that the resulting rational value is \(-111001473/32000\).

The cyclotomic witness is the same arithmetic. The preimages and the phases \(\psi_3(w)\) modulo \(11\) are computed from \(S\), the scaled coefficients lie in \(\mathbb Z[i]\), and the difference \(4000(\Sigma-\overline\Sigma)\) reduces through \(\zeta^{10}=-1-\zeta-\cdots-\zeta^9\) to the displayed polynomial with vanishing Gaussian-imaginary part. The powers \(1,\zeta,\ldots,\zeta^9\) are a basis of \(\mathbb Q(\zeta_{11})\), so the element is nonzero. Hence \(\Sigma\ne\overline\Sigma\).

## 5. Parity and position conjugation

The quadratic form \(Q(x,y)\) is symmetric and even, so \(M_N\) is a symmetric matrix and \(M_{N,-x,-y}=M_{N,xy}\). Therefore \(PM_N=M_NP\) and \(M_N^{-1}=\overline{M_N}=K_0M_NK_0\).

The parity operator satisfies \(PT_N(v)P=T_N(-v)\). Hence
\[
PA_NP-A_N=\sum_w(c_{-w}-c_w)\,T_N(w),
\]
after labels are added when they collide modulo \(N\). Hilbert–Schmidt orthogonality converts the squared norm into \(N\Delta_{\mathrm{par}}(N)\). For \(N\ge 19\) the 32 modes remain distinct modulo \(N\), Hermitian symmetry gives \(\lvert c_{-w}-c_w\rvert^2=4(\operatorname{Im} c_w)^2\), and
\[
\sum_v(\operatorname{Im} c_v)^2=\frac{663}{4000000},
\qquad
\Delta_{\mathrm{par}}(N)=\frac{663}{1000000}.
\]
The odd part of the symbol therefore carries the fraction
\[
\frac{663/4000000}{66033/160000}=\frac{221}{550275}
\]
of the Hilbert–Schmidt energy. Both verifiers recompute the folded defect at every odd modulus from \(3\) through \(77\). It vanishes at \(N=7\) and is positive at every other odd modulus in that range.

Complex conjugation acts by \(K_0T_N(a,b)K_0=T_N(a,-b)\) and by conjugating scalars. The coefficient of \(T_N(w)\) in \(K_0A_NK_0\) is therefore \(\overline{c_{\sigma w}}\) with \(\sigma(a,b)=(a,-b)\). Section 2 gives the coefficient \(c_{Sw}\) in \(M_N^{-1}A_NM_N\). The squared \(\ell^2\) distance of these two finitely supported functions, after folding modulo \(N\), is \(\Delta_{\mathrm{rev}}(N)\).

On \(\mathbb Z^2\) every vector that meets the support of either function has coordinates in \([-39,39]\): the symbol support lies in \(\lvert a\rvert\le 1\), \(\lvert b\rvert\le 9\), and \(S^{-1}=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}\) enlarges a vector by at most \(39\). For odd \(N\ge 79\) these integers remain distinct modulo \(N\), so the folded defect equals the unreduced sum
\[
\Delta_{\mathrm{rev}}(N)=\frac{66031}{80000}.
\]
The integer certificate evaluates the folded sum at every odd modulus from \(3\) through \(77\). The value is \(0\) at \(N=7\) and positive otherwise. The same certificate compares the coefficient operators with the literal matrices at \(N=7,9,11,15\), and at \(N=7\) it checks \(PU_7P=U_7\) and \(K_0U_7K_0=U_7^{-1}\) for one nonzero coupling.

The vanishing at \(N=7\) is the aliasing of the frequency-\(7\) modes of \(\cos(14\pi q)\) onto the zero mode, together with the collisions among the remaining frequencies. The certificate is the exact folded sum, not an interpretation of the aliasing.

## 6. Self-audit

The trace closure and the phase average were rederived from the cocycle and checked against literal matrices. The floating-point agreement is a finite check of those matrices. It is not a substitute for Section 3.

The order-two formula counts each mode once in \(\sum_v\lvert c_v\rvert^2\). Replacing that sum by a sum over the 16 pairs would double it. The matrix assembly of the same balanced words matches the formula; that comparison is what fixes the normalization.

Theorem 1 does not assert that \(D_2\) has a limit, that the series reproduces \(\min(m,N)\), or that the fixed kick is close to its phase average. At a scalar return the phase-averaged second-order term is negative, of size \(m\sigma\eta^2 N^2\). The fixed kick has, in addition, the linear term of Theorem 2, which the witness shows is nonzero.

The passage from \(N^{-1}\lvert\operatorname{Tr} U_N^m\rvert\) to an average of \(\exp(i\eta m\langle\psi,A\psi\rangle)\) would require replacing the time-ordered product by the exponential of the averaged kick. That replacement is not proved. Inside the bound \(m B\lvert\eta\rvert\le 1\) with \(m\le N\) and \(\eta=\tau N\), the quantity \(\tau^2 N^3\) is \(O(1/N)\) along \(m\sim N\). The Kurlberg–Rudnick moment calculation remains a statement about a different matrix-element ensemble.

Theorem 3 does not say that the spectrum at \(N=7\) is COE, and it does not say that every larger dimension is CUE. It says that these two symmetries of \(M_N\) fail to be symmetries of \(U_N(\eta)\) except at \(N=7\).

## 7. Certificates

- `computations/verification/interaction_phase_form_factor.py`
- `computations/cpp/interaction_phase_form_factor.cpp`
- `formalization/Bgs/PhaseFormFactorRational.lean`
- `evidence/executions/20261029/phase-form-factor/README.md`

Lean decides the scaled coefficient table, the count of 32 modes, Hermitian symmetry, the energy \(6603300\), the parity energy \(2652\), the majorant sum, and the unreduced reversal sum \(13206200\). It does not formalize the trace closure, the phase average, or the folding over \(N\). Python and C++ recompute those integer sums from the coefficient formula, the cyclotomic witness, the order at \(41\), and the folded defects. They also compare the Gauss-sum traces and the interaction picture with literal matrices in floating point. A pass of the certificate does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
