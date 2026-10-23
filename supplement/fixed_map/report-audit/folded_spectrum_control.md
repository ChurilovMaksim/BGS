# Can local spectral bounds rescue the resonance argument?

Continuation after the 19 September report audit. The attempted implication
is: arithmetic period growth, macroscopic equidistribution, bounded local
correlations and short-time trace control imply small resonant return energy.
The following countercontrol refutes that implication at the level of
spectral information. It is NOT a quantization of the prescribed fixed
smooth map and is NOT a BGS counterexample.

## 1. Construction and strong regularity properties

Let 0<alpha<1. For any N and positive integer rho<N, define a simple
spectrum by eigenangles

\[
\theta_j=\frac jN+\frac{\alpha}{2\pi\rho}
\sin\left(\frac{2\pi\rho j}{N}\right),\quad 0\le j<N.  \tag{1}
\]

The map H_rho(t)=t+alpha sin(2pi rho t)/(2pi rho) has derivative between
1-alpha and 1+alpha. Hence the cyclic unfolded gaps lie in
[1-alpha,1+alpha]; there are no degeneracies and every local counting
moment is bounded uniformly in N and rho. More explicitly, an interval
of unfolded length R contains at most 1+R/(1-alpha) points. The usual
anchored factorial statistics on any fixed compact support are therefore
uniformly bounded at every fixed order.

The macroscopic interval discrepancy is at most
1/N+alpha/(2pi rho). Thus these spectra become macroscopically uniform
as soon as rho tends to infinity.

For T(m)=sum_j exp(2pi i m theta_j), the Jacobi--Anger identity gives

\[
T(m)/N=\sum_{k:\ m+k\rho\equiv0\pmod N}
J_k(\alpha m/\rho).                                  \tag{2}
\]

For 1<=m<rho every contributing k has |k|>=N/rho-1. Contour shifting
in the integral formula for J_k(z) gives
|J_k(z)|<=exp(-|k|+|z|sinh(1)). Summing the resulting geometric series
in (2) yields

\[
\max_{1\le m<\rho}|T(m)|\le C_\alpha N e^{-N/\rho}.   \tag{3}
\]

In particular these unnormalized short traces tend uniformly to zero
when rho=O(log N). If rho divides N they are exactly zero by rotational
symmetry, but divisibility is not required for the argument.

## 2. A nonzero resonant energy at Heisenberg scale

For V=U^rho, let nu_N be its empirical phase measure. Put
M=N/gcd(N,rho), which is at least N/rho. Multiplication by rho modulo N
permutes the M-point grid with a constant multiplicity, so

\[
\widehat\nu_N(\ell)=\frac1M\sum_{j=0}^{M-1}
\exp\left(i\ell[2\pi j/M+\alpha\sin(2\pi j/M)]\right). \tag{4}
\]

Choose a fixed 0<c<1/(1+alpha), set L=floor(cN/rho), and suppose
rho=o(N), so L tends to infinity. The continuum coefficient in (4) is
(-1)^ell J_ell(alpha ell). For 1<=ell<L<=cM, the sum of all alias
coefficients has the uniform bound

\[
\left|\widehat\nu_N(\ell)-(-1)^\ell J_\ell(\alpha\ell)\right|
\le\frac{2e^{-\gamma M}}{1-e^{-hM}},\qquad
\gamma=(1-c)h-\alpha c\sinh h>0,                      \tag{5}
\]

where h>0 is chosen small enough. Indeed, the aliases are
J_{nM-ell}(alpha ell), n!=0. The contour estimate
|J_k(z)|<=exp(-|k|h+|z|sinh h) bounds their sum by the geometric series
in (5). The required positive gamma exists precisely from c(1+alpha)<1.
The error in the sum of L squared amplitudes tends to zero as well,
since L<=cM and (5) decays exponentially.

Let H(t)=t+alpha sin(2pi t)/(2pi). Its pushforward of uniform measure has
density g with g(H(t))=1/(1+alpha cos(2pi t)). Parseval and change of
variables give

\[
\sum_{\ell\ne0}|J_\ell(\alpha\ell)|^2
=\int_0^1g(x)^2dx-1
=\int_0^1\frac{dt}{1+\alpha\cos(2\pi t)}-1
=\frac1{\sqrt{1-\alpha^2}}-1.                         \tag{6}
\]

Dominated convergence applies to the Fejer weights because g is bounded.
Combining (4)--(6) proves the exact limiting return energy

\[
\sum_{0<|\ell|<L}(1-|\ell|/L)
|T(\ell\rho)/N|^2
\longrightarrow \frac1{\sqrt{1-\alpha^2}}-1>0.         \tag{7}
\]

The largest original time ell*rho is of order cN. Thus (7) concerns the
actual Heisenberg window, not a smaller auxiliary time scale. It applies
to any rho sequence with rho->infinity and rho=o(N). In particular one
can choose the actual projective cat periods along the odd Pell dimensions:
the arithmetic bounds already proved give rho_N of order log N there.
The construction remains an abstract spectrum; sharing that arithmetic
stride does not supply a smooth dynamical quantization.

For alpha=1/2 the limit is 2/sqrt(3)-1=0.154700538..., whereas the CUE
reference for this resonant energy is O(1/rho) and tends to zero.

## 3. Consequence for the research route

This example has simultaneously:

- simple spectra and a uniform positive minimum unfolded gap;
- uniformly bounded local factorial correlations at every fixed order;
- macroscopic equidistribution;
- exponentially small short traces below rho when rho is logarithmic;
- the same allowed logarithmic resonant stride, but nonvanishing return
  energy at times of order N.

Therefore adding those spectral inputs to the report's sparsity argument
does not close it. What is still required is a genuinely dynamical estimate
of the folded measure at scale rho/N, or an equivalent coherent return bound.
The existing local-pair bootstrap controls its total size but does not
force the desired decay.

The contour and Parseval proof uses only the Fourier integral definition
of Bessel coefficients; it does not rely on a fitted numerical law.
`folded_spectrum_control.py` evaluates the constructed spectra at odd
Pell dimensions through N=47321, checks the gap bounds and short traces,
and compares return amplitudes with Bessel coefficients. Its recorded
finite energy uses modes through 64 and is explicitly labeled as a
partial nonnegative sum; the proof above controls all modes in (7).

This closes a proposed route using insufficient inputs, not the original
BGS problem. A new attempt must use further information about the fixed
propagator rather than only these spectral regularity properties.
