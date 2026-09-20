# Resonance sparsity and the missing return-amplitude estimate

19 September 2026. Internal elementary proofs and self-review. This note
strengthens a correct arithmetic observation from the uploaded reports
and refutes the claimed inference from sparsity and unitarity alone.
It does not refute BGS for the fixed nonzero kick.

## 1. A bound for every dimension

Let S be a fixed hyperbolic element of SL(2,Z), with spectral radius
lambda>1, and rho_N=min{m>=1:S^m=+I or -I modulo N}. For every N>=3,

\[
\rho_N\ge \frac{2\operatorname{arcosh}(N/2)}{\log\lambda}.
                                                               \tag{1}
\]

Indeed, if S^m-sigma I has every entry divisible by N, its determinant
is divisible by N^2. The determinant is nonzero by hyperbolicity and

\[
N^2\le|\det(S^m-\sigma I)|
=|2-\sigma\operatorname{Tr}S^m|
\le 2+\lambda^m+\lambda^{-m}
=4\cosh^2(m\log\lambda/2).
\]

This proves (1) also for even N>=4; oddness is needed elsewhere for the
chosen quantum representation, not for this arithmetic fact. For the
matrix in both reports lambda=3+2sqrt(2).

In particular, rho_N tends to infinity along ALL dimensions and

\[
\frac{2}{X}\sum_{\substack{3\le N\le X\\N\text{ odd}}}
\rho_N^{-1}=O_S((\log X)^{-1}).                         \tag{2}
\]

Split the sum at sqrt(X). The first part has O(sqrt(X)) terms bounded
by one; (1) bounds each remaining term by O_S(1/log X).
The reports' divisor-counting argument gives a weaker density-one
conclusion that is unnecessary for this particular period definition.

## 2. Normalize the spectral statistic before counting times

For a unitary U of dimension d and the standard unit-intensity anchored
pair statistic, exact Fourier summation gives

\[
C_{2,d}(U;\varphi)
=d^{-2}\sum_{m\in\mathbb Z}\widehat\varphi(m/d)
\big(|\operatorname{Tr}U^m|^2-d\big).                  \tag{3}
\]

Let a positive integer rho designate the times being called resonant,
and put V=U^rho, A(l)=Tr(V^l)/d. The positive trace-square contribution
at nonzero resonant times is EXACTLY

\[
Q^{\rm res}=\sum_{\ell\ne0}
\widehat\varphi(\ell\rho/d)|A(\ell)|^2.                \tag{4}
\]

There is no prefactor 1/d left in (4). If the Fourier support is in
[-T,T], the elementary estimate |A(l)|<=1 yields only

\[
|Q^{\rm res}|\le2\|\widehat\varphi\|_\infty
\lfloor Td/\rho\rfloor=O_\varphi(d/\rho).             \tag{5}
\]

The subtraction of d per term in (3) is O(1/rho), as is the CUE reference
sum: E|Tr(V_CUE^m)|^2=min(|m|,d)<=d at m!=0. The *actual* trace-square
term can be a factor d larger. The reports' estimate O(1/rho+1/N) does
not follow from resonance counting and unitarity.

Any proposed Bessel-walk representation must reproduce (4) with its
actual prefactor and amplitude normalization. A unit-vector return
amplitude bounded by one alone cannot repair (5).

## 3. A sharp control example in the same arithmetic family

For odd K>=3, let N_K+F_K sqrt(2)=(1+sqrt(2))^K. The cat quantization
has M_{N_K}^K scalar, since S^K=I modulo N_K and exact Weyl covariance
makes that power commute with every Weyl matrix. On either parity block
of dimension d=(N_K+/-1)/2,

\[
|\operatorname{Tr}M^{\ell K}|=d.
\]

For a smooth nonnegative Fourier window equal to one on [-1,1], its
resonant positive contribution is at least 2 floor(d/K). Since N_K
grows exponentially in K, this diverges. The O(1/K) subtraction in (3)
cannot remove it. More generally, any unitary with U^rho scalar makes
the counting bound (5) sharp up to its window constant.

This is a counterexample to the inference that was claimed to use
only sparsity and |A|<=1. It is not a counterexample for fixed kappa!=0.
If the latter model has extra cancellation, that cancellation must be
proved and cannot be replaced by the unitarity argument.

Finite checks in `verify.py` confirm the period bound for the 150 odd
dimensions 3,...,301 and the Pell identity for all odd K from 3 to 39.
At K=39, N=423859315570607, the positive parity block alone contributes
at least 10868187578732 from the sharp inner window. No dense matrix
of that size was constructed; this number follows from integer identities.

## 4. The corrected analytic obligation

Let nu be the empirical probability measure of eigenangles of V=U^rho.
For an integer L>=2 define the Fejer kernel

\[
F_L(x)=\sum_{|\ell|<L}(1-|\ell|/L)e^{2\pi i\ell x}
=L^{-1}\left|\sum_{j=0}^{L-1}e^{2\pi i jx}\right|^2.
\]

Then the exact nonnegative return energy is

\[
E_L=\sum_{0<|\ell|<L}(1-|\ell|/L)|\widehat\nu(\ell)|^2
=\iint F_L(x-y)\,d\nu(x)d\nu(y)-1\ge0.                \tag{6}
\]

For Heisenberg-scale resonances L is of order d/rho. Proving E_L=o(1),
at every fixed enlargement of that scale, supplies the needed resonant
suppression for arbitrary bounded compact Fourier windows. Indeed,
F_{2L}'s Fourier weights are at least 1/2 on |l|<=L. Conversely, vanishing
of the nonnegative sharp return sums implies vanishing of E_L.

Condition (6) is a mesoscopic equidistribution requirement for the
spectrum of U^rho. It is not automatic from rho->infinity. If V is
scalar then E_L=L-1. If nu is uniform on d equally spaced angles and
L<=d, E_L=0. Uniformity of the limiting spectral measure alone need
not control a growing L.

A concrete sufficient estimate uses interval discrepancy
D(nu)=sup_{0<=x<=1}|nu([0,x))-x|:

\[
0\le E_L\le C L D(\nu).                              \tag{7}
\]

To see this, integration by parts bounds integration against nu-dx
by discrepancy times the total variation of a periodic test function.
Write F_L=|D_L|^2/L with D_L=sum_{j=0}^{L-1}e^{2pi i jx}. Cauchy--Schwarz
and Parseval give
integral |F_L'| <= 2 ||D_L'||_2 ||D_L||_2/L <= C L.
This bound is uniform under translations; integrate it once more in nu.
Thus D(nu)=o(rho/d) is sufficient, though not necessary. No such estimate
has been established here for the fixed kicked map.

The remaining task is therefore an actual estimate on (6), or another
bound implying it, for the perturbed monodromy. Period growth has been
settled; amplitude control has not. The claimed bypass of spectral
delocalization in the uploaded reports does not close this obligation.
