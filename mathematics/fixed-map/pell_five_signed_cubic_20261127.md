# A finite signed cubic response at the five-step Pell return

Source: Day 115, November 27 review packet, exact cubic certificate. Here \(N=41\), \(t=N\tau\), and \(U_N(\tau)=e^{itA_N}M_N\) uses the literal kick. This is a finite sign-asymmetry result. The quadratic coefficient is the \(n=5\) instance of [TRACE-125](uniform_orbit_overlap.md).

The exact covariance in the modular \(T_N\) basis sends \((a,b)\) to \(S(a,b)\) under \(M_N\)-conjugation. Since \(S^5=I\bmod41\), irreducibility of the shift and clock makes \(M_N^5\) scalar. Dropping that scalar in the intensity, the five-step product is \(\prod_{j=0}^4 e^{itA_j}\), in increasing order, with \(A_j=M_N^jA_NM_N^{-j}\). Put \(B=\sum_j A_j\) and \(T=N^{-1}\operatorname{tr}\sum_{i<j<l}A_iA_jA_l\). The linear trace is zero. Cyclicity and Hermiticity make the traces of all cubic terms with a repeated site real prior to multiplication by \(i^3\). Consequently the cubic coefficient of the intensity is \(2N^5\operatorname{Im}T\) and that of the positive-minus-negative intensity is \(4N^5\operatorname{Im}T\). Its quadratic intensity coefficient is \(-N^4\operatorname{tr}(B^2)/N\), which is unchanged under \(\tau\mapsto-\tau\).

The attached integer calculation gives \(T=4000^{-3}\sum_ep_e e(e/41)\), where \(p_{14}=6480000000\), \(p_{25}=-3239986000\), and all other coefficients have total absolute value below \(10^9\). They are real integers. The positive sine at \(14\) exceeds \(0.7\) by the elementary Taylor bound at \(13\pi/41\); the sine at \(25\) is negative. Hence \(\operatorname{Im}T>0.05\). The calculation uses the exact modular product \(T(a,b)T(c,d)=e_{41}(2^{-1}(ad-bc))T(a+c,b+d)\) and attaches the phase only when the closing three labels sum to zero.

The tensor exponential series for the intensity uses total generator norm at most \(2N\sum_j\|A_j\|<656\). Indeed the absolute Fourier sum bounded using \(|\Re c|+|\Im c|\) for the literal symbol is less than \(8/5\). The magnitude of the odd tail of the intensity difference from order five onwards is at most
\[
2N^2 e^{656|\tau|}(656|\tau|)^5/5! < 10^{16}|\tau|^5
\quad (|\tau|\le10^{-6}).
\]
Thus the positive intensity exceeds the negative intensity for every \(0<\tau\le10^{-6}\), in particular at \(10^{-80}\) and \(N=41\). This excludes an exact sign identity of all trace intensities and gives no asymptotic sign distinction.

Reproduce the certificate with
`python3 computations/verification/coupling_scope_audit/check_day115_pell_cubic.py`.
The checker certifies the coefficients and the sign margin by integer arithmetic. Its decimal line is supplemental.

## Finite Fejér lower bounds at the original coupling

Let \(r\ge5\) be odd, \(N=h_r\) as in the [Pell return proof](fixed_model_pell_crossover.md), and \(t=N10^{-80}\). The [orbit overlap calculation](uniform_orbit_overlap.md) gives \(\|B\|_{2,N}^2=r\sigma\), where \(B=\sum_{j=0}^{r-1}A_j\), \(\sigma=1650797/4000000\), and the Hilbert–Schmidt norm is divided by \(\sqrt N\). Write \(P=\rho^{-1}U_N^r=\prod_j e^{itA_j}\), \(|\rho|=1\). Duhamel for self-adjoint generators and unitary telescoping give
\[
 \|P-e^{itB}\|\le\frac{|t|^2}{2}\sum_{i<j}\|[A_i,A_j]\|
 =\frac{r|t|^2}{2}\sum_{d=1}^{(r-1)/2}\|[A_N,A_d]\|.
\]
For the equality, there are \(r-d\) ordered pairs with difference \(d\), and the commutator norms for \(d,r-d\) are equal by the scalar metaplectic return and conjugation. The Duhamel bound for two factors follows by integrating the difference of their time-dependent generators; differentiating \(e^{isA}D e^{-isA}\) bounds that difference by \(|s|\|[A,D]\|\). Iterating gives the displayed pair sum.

Let \(\eta\) be \(|t|\sqrt{r\sigma}\) plus the displayed commutator bound. Then \(\|P^j-I\|_{2,N}\le j\eta\) for \(j\ge1\), and \(\Re\operatorname{tr}(P^j)/N=1-\|P^j-I\|_{2,N}^2/2\). Retaining the times \(jr<M\) in the positive [Fejér energy](fixed_spectrum_crowding_20261127.md) gives
\[
 E_N(M)\ge (N/M)\sum_{1\le jr<M}(1-jr/M)^2(1-j^2\eta^2/2)_+^2.
\]
For \(M=\lfloor N/4\rfloor\) the [rational checker](../../computations/verification/coupling_scope_audit/check_day117_pell_fejer.py) gives strict lower bounds \(26202,4452,740,109,9\) at \(r=197,199,201,203,205\), respectively. It bounds each absolute Weyl coefficient by the sum of its absolute integer real and imaginary numerators divided by \(4000\). The Weyl commutator contributes at most \(2\min(1,22\,\operatorname{dist}(\det,N\mathbb Z)/(7N))\). An upward rational square-root bound for \(r\sigma\) makes all threshold tests exact. At \(r=207\) the separate [existing first-return bound](pell_microscopic_window.md) gives \(E_N(M)>3/2\) on retaining its \(j=1\) term, with the \(31/50\) trace lower bound. The CUE expectation is \((M^2-1)/(12NM)<1/48\), by summing the squared triangular weights against \(\mathbb E|\operatorname{Tr}U^m|^2=m\) for \(m<M<N\).

These are finite comparisons at fixed coupling. The positive-part bound may become zero as \(N|\tau|\) grows and supplies no infinite fixed-coupling counterexample.
