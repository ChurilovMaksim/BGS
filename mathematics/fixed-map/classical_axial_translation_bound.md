# Classical axial Fourier bounds for a signed interval of small kicks

Let \(g\) be the [literal symbol](fixed_map_path_model.md), \(S=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)\), \(F_t=S\Phi_g^t\) and \(t=\tau/(2\pi)\). For each \(0<|\tau|\le4\cdot10^{-10}\) the near-identity torus conjugacy \(F_tH_t=H_tS\) satisfies, with \(\nu_t=(H_t^{-1})_*\mathrm{Leb}\),
\[
 |\widehat\nu_t(e_q)|,\ |\widehat\nu_t(e_p)|>0.04|t|.
\]
Consequently \(\nu_t\) has trivial translation stabilizer, and \(\|\nu_t-(T_a)_*\nu_t\|_{\rm TV}\ge0.16|t|\operatorname{dist}_\infty(a,\mathbb Z^2)\) for the total variation norm \(\|\sigma\|_{\rm TV}=\sup_{\|f\|_\infty\le1}|\int f\,d\sigma|\). This result is classical and uses the log-Lipschitz modulus of the first variation.

## Uniform displacement

Let \(\lambda=3+2\sqrt2\). The Euclidean spectral projectors have norms \(3/(2\sqrt2)\), by their rank-one matrices. Conjugating \(S\) by the diagonal rescaling that makes its off-diagonal entries equal gives \(\|S^{\pm j}\|\le\sqrt2\lambda^j\); also \(\|S\|<7\). For the inverse \(\mathcal G\) of \(h\mapsto h\circ S-Sh\), the stable and unstable geometric series give
\[
 \|\mathcal G\|_{\infty\to\infty}
 \le\frac{3}{2\sqrt2}\left(\frac1{1-\lambda^{-1}}+\frac1{\lambda-1}\right)
 =\frac32 .
\]
The exact sums of \((|\Re(4000c_w)|+|\Im(4000c_w)|)\) weighted by \(\lceil|w|\rceil,|w|^2\) are \(29964,205804\) respectively. The ordinary midpoint sign has no effect on this absolute mass. They give \(\|X_g\|<48\) and \(\|DX_g\|<2040\), using \(2\pi<44/7\). The [integer and rational check](../../computations/verification/coupling_scope_audit/axial_fourier_range_check.py) reproduces the sums and strict numerical bounds.

In real lifts let \(G_t=F_t-S\). The flow integral and its derivative estimate give
\[
 \|G_t\|\le7\cdot48|t|,\quad \|DG_t\|\le7(e^{2040|t|}-1),\quad
 \|G_t-tSX_g\|\le7\cdot2040\cdot24\,t^2.
\]
On \(|t|\le1/(15\cdot10^9)\) the map \(u\mapsto \mathcal G[G_t(\mathrm{id}+u)]\) is a contraction with factor below \(2\cdot10^{-6}\), using \(e^x-1\le x/(1-x)\) for \(0\le x<1\). Its displacement satisfies \(\|u_t\|\le504|t|\), by applying the uniform bound on \(G_t\) at the fixed point. Set \(H_t=\mathrm{id}+u_t\) and \(h_1=\mathcal G[SX_g]\). Substitution gives
\[
 \|u_t-th_1\|_\infty
 \le (3/2)\cdot7\cdot2040(24+504)t^2=11309760\,t^2 .
\]
The semiconjugacy is onto by degree one. If it identifies two points, all their bare iterates have differences with representatives \(w_j\) of norm at most \(1008|t|\). Each \(w_{j+1}-Sw_j\) is integral and has norm below one. It vanishes; a bounded two-sided orbit of \(S\) in the real lift is zero. This proves injectivity.

## Inverse and axial coefficients

The first variation has the series
\[
 h_1=-\sum_{j\ge0}\lambda^{-j}P_u X_g\circ S^j
       +\sum_{j\ge1}\lambda^{-j}P_s X_g\circ S^{-j}.
\]
Each term has supremum at most \(51\lambda^{-j}\) and Lipschitz constant at most \(3060\). For torus distance \(0<d\le1/2\), split at \(m=\lfloor\log(1/d)/\log\lambda\rfloor\). The head costs at most \(6120(m+1)d\), and the tail at most \(204d/(1-\lambda^{-1})<247d\). Using \(\log\lambda>1.75\) gives the increasing modulus \(d[6400+3500\log(1/d)]\).

The inverse displacement is \(-u_t\circ H_t^{-1}\) and has norm at most \(504|t|\). Substituting that distance in the modulus and adding the forward remainder gives
\[
 \|H_t^{-1}-\mathrm{id}+th_1\|_\infty
 \le t^2[1.5\cdot10^7+1.8\cdot10^6\log(1/|t|)] .
\]
For either unit axis, expand \(e^{-2\pi i v\cdot H_t^{-1}(x)}\). The quadratic Taylor error adds at most \(\tfrac12(2\pi\,504)^2t^2\); thus
\[
 |\widehat\nu_t(v)-2\pi it\,v\cdot\widehat h_1(v)|
 \le t^2[10^8+1.14\cdot10^7\log(1/|t|)] .
\]
After division by \(|t|\) this bound increases over the checked interval and is less than \(0.025\) at its endpoint, using \(\log(15\cdot10^9)<24\).

At either axial Fourier vector all nonzero lags in the series have zero coefficient. For \(j\ge1\) write \((S^T)^j=\left(\begin{smallmatrix}a_j&2b_j\\4b_j&a_j\end{smallmatrix}\right)\), with \(a_j\ge3,b_j\ge1\); negative powers flip the off-diagonal signs. The second coordinate of either axial image then lies outside the literal \(p\)-frequency support \(\{-1,0,1\}\). Hence \(\widehat h_1(v)=-P_u\widehat X_g(v)\). The two moduli of \(v^TP_uJv\) are \(1/\sqrt2\) and \(1/(2\sqrt2)\), with \(|\widehat g(e_q)|\ge1/20\) and \(|\widehat g(e_p)|=1/200\). The smaller axial derivative is exactly \((2\pi)^2/(400\sqrt2)>0.067\). Subtract the relative error to get the asserted \(0.04|t|\). Since \(\pi>3\), the stated interval in \(\tau\) is inside the checked interval in \(t\). Translation multiplies a Fourier coefficient by its corresponding phase. Taking the larger centered component of \(a\) and \(|1-e(s)|\ge4|s|\) for \(|s|\le1/2\) gives the norm bound.
