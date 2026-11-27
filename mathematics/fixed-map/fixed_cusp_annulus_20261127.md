# A fixed signed annular test of the Heisenberg cusp

Source: Day 114, November 27 review packet, fixed cusp annular test. This is a diagnostic for an arbitrary sequence of unitary spectra and a necessary CUE-ramp benchmark. It uses a signed time weight and leaves the original positive pair test and fixed-coupling spectral limit open.

Let \(0<a<1<b\) and \(m\ge2\) be an integer. There exists a real \(w\in C_c^\infty((a,b))\) such that
\[
\int t^{2r}w(t)\,dt=0\quad(0\le r<m),\qquad
\int\min(t,1)w(t)\,dt=1.
\]
Choose \(\psi(x)=(x-1)^{m-2}\rho((x-1)/\epsilon)\) with a smooth compactly supported bump equal to one near zero. For small \(\epsilon>0\) set \(w_0(t)=2t\psi^{(m)}(t^2)\) on the positive axis. Integration by parts in \(x=t^2\) gives all the vanishing moments. The distribution \(D^m\min(\sqrt x,1)\) has highest singular term \(-\tfrac12\delta_1^{(m-2)}\), from the derivative jump at \(1\). Only this term pairs nontrivially among the delta derivatives, with absolute value \((m-2)!/2\). The bounded ordinary part contributes \(O(\epsilon^{m-1})\). Normalize \(w_0\) by its nonzero response.

For phases \(\theta_i\) in turns and \(K_N(s)=N^{-1}\sum_n w(n/N)\cos(2\pi ns)\), the exact identity is
\[
N^{-2}\sum_n w(n/N)|\operatorname{tr}U_N^n|^2
=N^{-1}\sum_{i,l}K_N(\theta_i-\theta_l).
\]
Cosines suffice because pairs are ordered. Poisson summation on each \(t^{2r}w(t)\) gives its scaled quadrature error \(O_B(N^{-B})\) for every fixed \(B\). Taylor expansion of the cosine consequently bounds \(K_N\) by \(O(N^{-2m\eta}+N^{-B})\) on \(\|s\|\le N^{-1-\eta}\), including equal phases. Poisson summation on \(w\) itself yields \(|K_N(s)|\le C_B(1+N\|s\|)^{-B}\) for \(B>1\). Given \(\eta>0\), \(0<\xi<1\), and \(D>0\), take \(2m\eta>D+1\) and \(B\xi>D+1\). The contribution outside \(N^{-1-\eta}<\|\theta_i-\theta_l\|<N^{-1+\xi}\) is then \(O(N^{-D})\) after the factor \(1/N\) and at most \(N^2\) ordered pairs. All multiplicities are allowed.

The bump can be chosen in Gevrey order two. For example, the extension by zero of \(e^{-1/y}\), \(y>0\), has bounds \(C^{r+1}(r!)^2\) on bounded intervals by Cauchy's formula on radius \(y/2\) and maximization of \(y^{-r}e^{-c/y}\). Products of two shifted, reflected copies give a bump, and convolution with a short interval indicator gives a plateau. The fixed derivatives and the composition with \(t^2\) preserve the estimates. Optimizing integration by parts gives \(|\widehat w(\xi)|\le C e^{-c\sqrt{|\xi|}}\). In this construction the outer radius can be \(C_D\log^2(2N)/N\) with the same prescribed \(O(N^{-D})\) error.

For the exact CUE benchmark the time sum is \(N^{-1}\sum_n w(n/N)\min(n/N,1)=1+O(N^{-2})\) by the trapezoid rule on both sides of the grid point \(1\). This use of the benchmark does not determine the statistic for the literal map. In particular no stretched-exponential replacement of a boundary mean is needed for this annulus identity.
