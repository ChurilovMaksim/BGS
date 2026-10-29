# Bessel form of the scalar-return orbit sum

**Claim ID:** `BGS-TRACE-129`.
**Status:** project proof. The scalar reduction, the vanishing of the time-one coefficient, the Bessel identity for the classical orbit sum, and the second-moment count are proved below. Python and C++ recompute the integer orbit counts and the Bessel sum in floating point. Lean decides \(\det(S-I)=-4\), the orders at \(5\) and \(7\) together with the checked proper divisors, the identity \(S^{12}\equiv I\pmod{11}\) without a certificate that \(12\) is minimal, the quadruple counts at \(5\) and \(7\), and the momentum-row energy. The quadruple rows at \(11\), \(31\), \(41\) and \(47\) are Python-only. Lean does not sum the Bessel average. No external referee.

`BGS-TRACE-126` supplies Egorov, the trace closure, and the order-two coefficient. `BGS-TRACE-005` and `BGS-BGS-001` remain **open**. The COE limit of the sixteen-phase ensemble, and the crossover to CUE produced by the momentum modes, are not proved.

## 1. Statements

Let \(N\ge 3\) be odd, let \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\), and let \(M_N\), \(T_N\) and \(A_N(\varphi)\) be as in `BGS-TRACE-126`. The sixteen phases are independent and uniform. Write \(\sigma=66033/160000\) and \(B=184981/160000\).

**Theorem 1 (scalar return).** Suppose \(S^m\equiv I\pmod N\). Then \(\lvert\operatorname{Tr} M_N^m\rvert=N\), so the unitary \(M_N^m\) is the scalar \((\operatorname{Tr} M_N^m)/N\). Consequently
\[
U_N(\eta,\varphi)^m
=\frac{\operatorname{Tr} M_N^m}{N}
\prod_{j=0}^{m-1}\exp\bigl(i\eta A_j(\varphi)\bigr),
\]
where \(A_j(\varphi)=M_N^j A_N(\varphi)M_N^{-j}=\sum_v c_v(\varphi)\,T_N(S^j v)\), the product runs from the left at \(j=0\), and the transport is the Egorov lemma of `BGS-TRACE-126`. A mode \(v\equiv 0\pmod N\) has \(T_N(v)=I\). Its Hermitian pair contributes a real scalar to every \(A_j\), hence a global phase to \(U_N^m\), and does not change \(\lvert\operatorname{Tr} U_N^m\rvert^2\). Write \(\sigma_0(N)\) for the energy of those modes. The support satisfies \(\lvert\ell\rvert\le 1\) and \(\lvert k\rvert\le 9\), so \(\sigma_0(N)=0\) for every \(N>9\). The three prime values \(\sigma_0(3)=81/64000\), \(\sigma_0(5)=1/320000\) and \(\sigma_0(7)=81/200\) are those of `BGS-TRACE-126`.

**Theorem 2 (time one).** For every odd \(N\), \(\det(S-I)=-4\) is a unit modulo \(N\), so \(S-I\) is invertible, \(\lvert\ker(S-I)\rvert=1\) and the order-two coefficient of `BGS-TRACE-126` vanishes. Therefore
\[
\mathbb E_\varphi\lvert\operatorname{Tr} U_N(\eta,\varphi)\rvert^2
=1+\rho_1(N,\eta),
\]
with the remainder bound of that note. Inside the window \(B\lvert\eta\rvert\le 1\) the expectation equals \(1+\rho_1(N,\eta)\), the pure value plus that remainder, rather than the short-time value \(2\). The identity is not claimed for large \(\lvert\eta\rvert\).

**Theorem 3 (classical orbit sum).** Let the kick be position-diagonal: only modes \((\ell,k)=(0,k)\) are kept, and write \(a_\varphi\) for its real symbol, so
\[
a_\varphi(x)=\sum_r 2\lvert c_r\rvert\cos\bigl(\varphi_r+\alpha_r+2\pi k_r x/N\bigr),
\]
the sum running over the diagonal pairs. Let \(m\ge 1\) and let \(q(S^j z)\) be the first coordinate of \(S^j z\). Define
\[
\mathcal S_N(\eta,\varphi)
=N^{-2}\sum_{z\in(\mathbb Z/N\mathbb Z)^2}
\exp\Bigl(i\eta\sum_{j=0}^{m-1}a_\varphi\bigl(q(S^j z)\bigr)\Bigr).
\]
Let \(V_r(z)=\sum_{j=0}^{m-1}\exp\bigl(i(\alpha_r+2\pi k_r q(S^j z)/N)\bigr)\). Then
\[
\mathbb E_\varphi\lvert\mathcal S_N(\eta,\varphi)\rvert^2
=N^{-4}\sum_{z,z'}\prod_r J_0\bigl(2\eta\lvert c_r\rvert\,\lvert V_r(z)-V_r(z')\rvert\bigr),
\]
where \(J_0(w)=(2\pi)^{-1}\int_0^{2\pi}\exp(iw\cos\theta)\,d\theta\). A mode with \(k_r\equiv 0\pmod N\) has \(V_r\) constant, so its factor is \(J_0(0)=1\).

**Theorem 4 (phasor second moment).** Let \(p\) be an odd prime and let \(m\) be the multiplicative order of \(S\) modulo \(p\). Let \(U_j\) be the first row of \(S^j\) for \(0\le j<m\), and suppose the \(U_j\) are pairwise distinct. For \(k\not\equiv 0\pmod p\),
\[
p^{-2}\sum_z\lvert V(z)\rvert^2=m,
\qquad
p^{-4}\sum_{z,z'}\lvert V(z)-V(z')\rvert^2=2m,
\]
where \(V(z)=\sum_{j<m}e_p(k\,q(S^j z))\). Consequently the degree-two jet of the Bessel average in Theorem 3, at a prime \(p>9\), is
\[
1-m\sigma_{\mathrm{diag}}\eta^2,
\]
with \(\sigma_{\mathrm{diag}}\) the energy of the diagonal modes. The same jet is \(1-m(\sigma_{\mathrm{diag}}-\sigma_0)\eta^2\) when zero modes are present. This is the degree-two jet of \(\exp(-m(\sigma_{\mathrm{diag}}-\sigma_0)\eta^2)\).

**Boundary.** The identity \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2=N^2\exp(-m(\sigma-\sigma_0)\eta^2)\) is not proved for \(\eta^2\sigma m\) of order one. Inside the window \(m B\lvert\eta\rvert\le 1\) of `BGS-TRACE-126`, that exponential and the proved quadratic differ by at most \(\mu^2 e^{\mu}/2\) with \(\mu=m(\sigma-\sigma_0)\eta^2=O(1/m)\), so both lie within the remainder of that note of the expectation. At a scalar return the same quadratic is the jet of Theorem 3. The degree-four gap is the number of non-permutation solutions of \(U_a+U_b=U_c+U_d\). That excess vanishes at the primes \(7\), \(31\), \(41\) and \(47\), and it does not vanish at \(11\). The rows \(\ell=+1\) and \(\ell=-1\) each have energy \(9/160000\), hence \(9/80000\) together. They are the only modes that can break position conjugation. Their smallness is why a COE regime can persist, and it is not a proof of a COE limit or of a CUE crossover. The asymmetry between \(N=201\) and \(N=203\) is not treated. `BGS-TRACE-005` and `BGS-BGS-001` remain open.

## 2. Scalar return and time one

The trace closure of `BGS-TRACE-126` gives \(\lvert\operatorname{Tr} M_N^m\rvert^2=\lvert\ker(S^m-I)\rvert\). If \(S^m\equiv I\), the kernel is the whole plane and the trace has modulus \(N\). A unitary \(N\times N\) matrix whose trace has modulus \(N\) has all eigenvalues equal, because each eigenvalue lies on the unit circle and the only way their sum has modulus \(N\) is if they coincide. Thus \(M_N^m\) is scalar. The interaction identity
\[
U^m=\Biggl(\prod_{j=0}^{m-1}\exp(i\eta A_j)\Biggr)M^m
\]
is Section 4 of `BGS-TRACE-126`, and Egorov supplies the transported symbol.

If \(v=(a,b)\equiv(0,0)\pmod N\), the definition \((T_N(v)\psi)(x)=e_N(b(x+2^{-1}a))\psi(x+a)\) gives \(T_N(v)=I\). A Hermitian pair of such modes adds a real multiple of \(I\) to \(A_N(\varphi)\). That multiple commutes with every factor, and \(\exp(i\eta\theta(\varphi))\) cancels in the squared modulus of the trace.

Now \(\det(S-I)=2\cdot 2-4\cdot 2=-4\). For odd \(N\), \(-4\) is a unit, so \(S-I\) is invertible over \(\mathbb Z/N\mathbb Z\) and the kernel has one element. In the order-two formula of `BGS-TRACE-126`, the image of \(I-S\) is the whole plane, the diagonal sum is the full energy \(\sigma\), and there is no pair \(j<k\) when \(m=1\). The coefficient collapses to \(\sigma-\sigma=0\).

## 3. The Bessel identity

Each diagonal pair contributes \(2\lvert c_r\rvert\cos(\varphi_r+\theta_r(x))\) to \(a_\varphi(x)\), with \(\theta_r(x)=\alpha_r+2\pi k_r x/N\). Along an orbit,
\[
\sum_{j=0}^{m-1}\cos(\varphi_r+\theta_r(q_j))
=\lvert V_r(z)\rvert\cos(\varphi_r+\psi_r(z)),
\]
because the sum of the complex exponentials \(e^{i\theta_r(q_j)}\) is \(V_r(z)\). Therefore
\[
\exp\Bigl(i\eta\sum_j a_\varphi(q_j)\Bigr)
=\prod_r\exp\bigl(i\,2\eta\lvert c_r\rvert\,\lvert V_r(z)\rvert\cos(\varphi_r+\psi_r(z))\bigr).
\]
The phases are independent, and
\[
(2\pi)^{-1}\int_0^{2\pi}\exp(iw\cos(\varphi+\psi))\,d\varphi=J_0(w)
\]
does not depend on \(\psi\). This is the classical Bessel integral, equivalently the constant term of the Jacobi–Anger expansion. A product of such factors, one for each independent random phase, is the classical calculus of a planar random walk with prescribed step lengths: Kluyver, A local probability problem, Proceedings of the Section of Sciences, Koninklijke Akademie van Wetenschappen te Amsterdam, 8 (1905), 341–350, which was read on 29 October 2026 from the Academy record. The product is not new. The content proved here is the bookkeeping that attaches those factors to the cat-map position orbit and that reads the degree-four gap as the quadruple excess of that orbit. The average of one orbit factor is \(\prod_r J_0(2\eta\lvert c_r\rvert\,\lvert V_r(z)\rvert)\).

For the square, the difference of two such cosine sums is
\[
\lvert V_r(z)\rvert\cos(\varphi+\psi)-\lvert V_r(z')\rvert\cos(\varphi+\psi')
=\lvert V_r(z)-V_r(z')\rvert\cos(\varphi+\xi),
\]
since both are the real parts of \(e^{i\varphi}\) times the corresponding complex sum, up to the fixed argument \(\alpha_r\) which cancels in the modulus of the difference. Integrating one phase at a time gives Theorem 3.

A single Hermitian pair \(c e^{i\varphi}T+ \overline c\, e^{-i\varphi}T^{-1}\), with \(T\) unitary, is diagonal in an eigenbasis of \(T\) with eigenvalues \(2\lvert c\rvert\cos(\varphi+\theta_s)\). The average of its exponential is \(J_0(2\eta\lvert c\rvert)I\). This is the one-step case of the same integral. It is not the several-time product: the transports \(T(S^j v)\) do not commute for a hyperbolic orbit.

## 4. Second moment

Let \(\chi_j(z)=e_p(k\, U_j\cdot z)\). For \(k\not\equiv 0\) and \(U_j\ne 0\) this is a nontrivial character, and \(\chi_j=\chi_\ell\) if and only if \(U_j=U_\ell\). The hypothesis that the rows are pairwise distinct makes the characters distinct. Then
\[
p^{-2}\sum_z\lvert V(z)\rvert^2
=\sum_{j,\ell}p^{-2}\sum_z\chi_j(z)\overline{\chi_\ell(z)}
=\sum_{j,\ell}1_{U_j=U_\ell}=m.
\]
The cross term \(\sum_z V(z)\) vanishes for the same reason: each single character sums to zero. Hence
\[
p^{-4}\sum_{z,z'}\lvert V(z)-V(z')\rvert^2
=2m.
\]
Expanding the product of Bessel functions,
\[
\prod_r J_0(2\eta\lvert c_r\rvert\,\lvert\Delta V_r\rvert)
=1-\eta^2\sum_r\lvert c_r\rvert^2\,\lvert\Delta V_r\rvert^2+O(\eta^4),
\]
and the average of \(\lvert\Delta V_r\rvert^2\) is \(2m\) for every non-zero mode. The linear term in \(\eta^2\) is \(-m\sum_r 2\lvert c_r\rvert^2=-m\sigma_{\mathrm{diag}}\) after the zero modes, which contribute nothing, have been removed. The exponential \(\exp(-m\sigma_{\mathrm{diag}}\eta^2)\) has the same jet.

The rows are distinct for every prime in the certificate. In general \(U_j=U_\ell\) would mean that \(S^j-S^\ell\) has first row zero, hence determinant zero, hence \(\operatorname{tr}(S^{j-\ell})\equiv 2\pmod p\). The verifier records the quadruple count rather than relying on that trace condition alone.

## 5. The degree-four gap

The fourth moment \(p^{-2}\sum_z\lvert V\rvert^4\) equals the number of quadruples \((a,b,c,d)\) with \(U_a+U_b=U_c+U_d\). If the rows are pairwise distinct, the permutation solutions \(\{c,d\}=\{a,b\}\) number \(2m^2-m\). Any further solution is an additive coincidence of the orbit. The certificate values are:

| prime | order | quadruples | \(2m^2-m\) | excess |
|---:|---:|---:|---:|---:|
| 5 | 6 | 90 | 66 | 24 |
| 7 | 3 | 15 | 15 | 0 |
| 11 | 12 | 396 | 276 | 120 |
| 31 | 15 | 435 | 435 | 0 |
| 41 | 5 | 45 | 45 | 0 |
| 47 | 23 | 1035 | 1035 | 0 |

Where the excess vanishes, the fourth moment is the Wick count \(2m^2-m\). Where it does not, the Bessel average lies above the exponential once \(\eta^2 m\) is of order one. At \(p=11\), order \(12\), and \(\lambda=m\sigma_{\mathrm{diag}}\eta^2=1\), the programs record a ratio greater than \(1.1\). At \(p=31\) and \(p=47\), where the excess vanishes, the same ratio at \(\lambda=1\) stays within three percent of \(1\). Neither numerical row is the missing estimate that would promote the exponential to an identity.

The momentum row \(\ell=1\) has scaled energy \(\sum 25 r(k)^2=900\), hence energy \(900/4000^2=9/160000\). The row \(\ell=-1\) has the same energy, so the two rows together have energy \(9/80000\). Position conjugation fixes every \(\ell=0\) mode and moves the \(\ell=\pm 1\) modes. That per-row energy is the exact weight of the breaking. The rows of the table at \(11\), \(31\), \(41\) and \(47\) are Python and C++ counts. Lean certifies the quadruple counts only at \(5\) and \(7\), and it does not certify that \(12\) is the minimal order at \(p=11\). A limit shape for the form factor at times of order \(N\), whether orthogonal or unitary, is not deduced from it.

## 6. Self-audit

The factor \(J_0\) is an average over a phase, not an eigenvalue of the propagator. Theorem 3 is an identity for the classical position-diagonal orbit sum. It is not an identity for the quantum sixteen-phase average \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2/N^2\). The several-time quantum product \(\prod_j\exp(i\eta A_j)\) is not the exponential of the sum, and it is not claimed to equal the orbit sum. They share the value \(Z_m\) at \(\eta=0\) and the same order-two coefficient at a scalar return; the gap is not given a uniform bound of size \(o(N^2)\) for \(\eta^2 m\) of order one.

The independent referee audit of 29 October 2026 recorded the following Monte Carlo of \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2/N^2\) at \(m=\operatorname{ord}(S\bmod N)\), beside the Bessel average of Theorem 3, a classical Monte Carlo of the orbit sum, and \(\exp(-m\eta^2(\sigma-\sigma_0))\). The three couplings are \(\eta=1/2\), \(1\) and \(2\). This table is numerical evidence from that audit. It was not re-executed by the certificates of this note.

| \(N\) | \(m\) | quantum | Bessel | classical MC | exponential |
|---:|---:|---|---|---|---|
| 7 | 3 | 0.9942, 0.9770, 0.9122 | 0.9943, 0.9776, 0.9147 | 0.9943, 0.9779, 0.9132 | 0.9942, 0.9771, 0.9117 |
| 11 | 12 | 0.377, 0.111, 0.084 | 0.397, 0.191, 0.115 | 0.386, 0.196, 0.110 | 0.290, 0.0071, 0 |
| 29 | 10 | 0.390, 0.070, 0.0146 | 0.449, 0.195, 0.087 | 0.453, 0.206, 0.080 | 0.356, 0.016, 0 |
| 41 | 5 | 0.593, 0.1154, 0.0088 | 0.595, 0.116, 0.006 | 0.594, 0.1162, 0.0077 | 0.597, 0.127, 0.0003 |
| 199 | 9 | 0.395, 0.032, 0.0011 | 0.391, 0.021, 0.001 |  | 0.395, 0.024, 0 |

The quantum column tracks the Bessel column at the zero-excess primes \(7\) and \(41\) for small \(\lambda\), and at \(N=199\), \(m=9\), with \(\eta=1/2\) (quantum \(0.395\) vs Bessel \(0.391\)); at \(\eta=1\) on that row the quantum value \(0.032\pm 0.002\) differs from Bessel \(0.021\pm 0.001\). At \(N=11\), \(m=12\), and at \(N=29\), \(m=10\), the quantum average and the Bessel average differ by ≈1.7 and by up to ≈6 respectively (\(\eta=2\)). The exponential tracks the Bessel average only for \(\lambda\lesssim 1\) at zero excess. None of these rows promotes Theorem 3 to a quantum identity.

The exponential \(\exp(-m\sigma\eta^2)\) is the degree-two jet, and it is the exact Bessel average of a complex Gaussian whose second moment equals \(2m\). The orbit is not that Gaussian whenever the quadruple excess is positive. A bound \(\lvert\mathbb E\lvert\operatorname{Tr}\rvert^2-N^2 e^{-\mu}\rvert\le N^2\varepsilon(\mu)\) with \(\varepsilon(\mu)\to 0\) for each fixed \(\mu\), uniformly in the prime, is not proved. The window \(m B\lvert\eta\rvert\le 1\) remains the one in which `BGS-TRACE-126` controls the quantum expectation.

The time-one statement does not say that the expectation equals \(1\) for every \(\eta\). The \(N=201\) and \(N=203\) samples are not inputs. No COE or CUE limit is claimed. Weil's bound is not used.

## 7. Certificates

- `computations/verification/scalar_return_bessel.py`
- `computations/cpp/scalar_return_bessel.cpp`
- `formalization/Bgs/ScalarReturnBesselRational.lean`
- `evidence/executions/20261029/scalar-return-bessel/README.md`

The programs check the orders, the quadruple table above, the energy \(9/160000\), the identity \(\sigma_0(N)=0\) for the primes from \(11\) through \(47\), the Bessel sum against a Monte Carlo of the orbit sum at \(N=7\) and \(N=11\), and the ratios to the exponential at \(\lambda=1\). A pass does not prove `BGS-TRACE-005` or `BGS-BGS-001`.
