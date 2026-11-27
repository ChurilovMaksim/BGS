# A fixed-spectrum crowding criterion

Sources: Day 116 and the companion notes “A low-frequency Fejér criterion for the Day116 crowding tail” and “Direct transfer of weak local laws and crowding to the seven-cut model”, November 27 review packet. These are deterministic criteria. Neither the crowding tail nor random-origin Sine₂ convergence is proved for the literal map.

## Equivalent crowding tails

Unfold the spectrum to a circle of length \(N\), including multiplicities. For each point let \(D_i\) count its neighbours at strict distance less than one, including itself. Put \(T(K)=N^{-1}\sum_i D_i\mathbf 1_{D_i>K}\). Let \(C(x)\) count the points in \([x,x+1)\) for uniform \(x\) on the circle and put \(T_s(K)=\mathbb E[C^2\mathbf 1_{C>K}]\). For \(N\ge3\),
\[
T_s(5K)\le(125/4)T(K),\qquad T(9K)\le108T_s(K).
\]
Partition into half-open quarter-unit cells with counts \(q_j\), and write \(B(K)=N^{-1}\sum_{q_j>K}q_j^2\). A sliding unit window intersects at most five cells; one with maximum count has count at least one fifth of the total, and each cell can intersect for a set of origins of length \(5/4\). This gives \(T_s(5K)\le(125/4)B(K)\). A fixed quarter-unit cell is fully contained for a set of origins of length \(3/4\). Summing the squares of counts of such fully contained cells with \(q_j>K\) gives \(T_s(K)\ge(3/4)B(K)\). Each point in a cell counts that entire cell, so \(T(K)\ge B(K)\). A distance-one neighbourhood of a point meets at most nine cells. For each home cell choose the largest count among its nine neighbours. When the home cell contributes to \(T(9K)\), the chosen count exceeds \(K\), and the contribution from the home cell is at most nine times its square. Each chosen cell can be picked by at most nine home cells. These observations also cover grid ties and repeated points.

The ordered limit \(\lim_{K\to\infty}\limsup_{N\to\infty}T(K)=0\) is thus equivalent to uniform integrability of \(C^2\). If random-origin local weak convergence to Sine₂ is independently known, it is equivalent to convergence of the unit second moment, or of all fixed-window second moments. Local weak convergence supplies count convergence in law since the limiting process has no atom at a deterministic endpoint. Conversely, convergence in law and convergence of the second moments imply uniform integrability by bounded truncation. Cover any interval of fixed length by unit intervals and apply Cauchy–Schwarz to extend the uniform-integrability assertion. For a compactly supported pair test, anchor one point with a fixed compact smooth density and use the same bounded-window squared-count control. For a Schwartz pair test, the expected number of pairs in an anchored interval of radius \(R\) is bounded by \(C(1+R)^2\) under the unit second-moment bound, by covering and Cauchy–Schwarz. Dyadic shells control the remaining tails. Subtract the exact self-pair term for factorial tests.

## A sub-Heisenberg trace criterion with ordered limits

Write \(p_n=\operatorname{tr}U_N^n\) and let \(1\le M\le N/4\) be an integer. Define
\[
E_N(M)=(NM)^{-1}\sum_{1\le n<M}(1-n/M)^2|p_n|^2.
\]
For the unit-mass Fejér kernel \(F_M\) and angles \(\theta_i\) in turns, put \(X_M(t)=N^{-1}\sum_i F_M(t-\theta_i)\) and \(c=4/\pi^2\). The bound \(F_M\ge cM\) on distance \(1/(2M)\) implies, on the interval of radius \(1/(4M)\) about \(\theta_i\), that \(X_M\ge cMD_i/N\) and that the integral of \(F_M(t-\theta_i)\) there is at least \(c/2\). Sum these bounds over the offending \(i\) and then use the definition of \(X_M\):
\[
T(K)\le (2/c^2)(N/M)\int_{\{X_M>cMK/N\}}X_M^2.
\]
If \(K\ge(\pi^2/2)N/M\), use \(X_M^2\le4(X_M-1)^2\) on the integration region and Parseval \(\int(X_M-1)^2=(2M/N)E_N(M)\). This gives \(T(K)\le\pi^4 E_N(M)\). Hence \(\liminf_{\delta\downarrow0}\limsup_{N\to\infty} E_N(\lfloor\delta N\rfloor)=0\) suffices for the tail. Choosing just one sequence \(M_N=o(N)\) controls a growing threshold, which does not give this ordered limit.

With both the tail and the weak Sine₂ law, \(E_N(\lfloor\delta N\rfloor)\to\delta/12\) for each fixed \(0<\delta\le1/4\). In unfolded coordinates the smoothed count is the periodization of \(\delta_N\operatorname{sinc}^2(\delta_N s)\), where \(\delta_N=M/N\) and \(\operatorname{sinc}(s)=\sin(\pi s)/(\pi s)\). This follows by its Fourier coefficients. For fixed \(\delta\) the tail of the smoothed count is uniformly small in \(L^2\), by the unit-cell count bound, Minkowski, and decay \(O_\delta((1+s^2)^{-1})\). Local convergence with uniform integrability therefore passes the first two moments to Sine₂. Its variance is \(\int_{\mathbb R}(1-|\xi|/\delta)_+^2\min(|\xi|,1)\,d\xi=\delta^2/6\), from the Fourier transform of its squared-sinc two-point kernel. Divide by \(2\delta\) via Parseval.

## Transfer to the full seven-cut unitary

Use the simultaneous phase labelling in [FM-007](frozen_seven_cut_reduction.md), with unfolded displacements \(d_i\), \(\sum_i|d_i|=O(|\tau|)\) and \(\max_i|d_i|=O(|\tau|)\). Under a common uniform origin the difference of a periodized \(C_c^1\) test has expected absolute value at most \(N^{-1}\sum_i|d_i|\|\varphi'\|_1\), by integrating the derivative along each displacement. Unit intensity gives tightness on compact windows. The weak law therefore transfers in either direction. For crowding, every distance-one neighbour of point \(i\) remains within radius \(1+2\max_i|d_i|\) in the other spectrum. For any fixed radius \(R\), the same cell-maximization argument above bounds its thresholded tail by the radius-one tail with constants depending only on \(R\). This transfers the crowding condition in either direction.

Finally, FM-007's trace difference bound \(|p_n(U)-p_n(V)|\le(28\pi^2|\tau|/(25N))n\) transfers the sufficient Fejér condition by the weighted Euclidean triangle inequality and \(\sum_{n=1}^{M-1} n^2(1-n/M)^2=(M^4-1)/(30M)\). The seven-cut unitary here retains the metaplectic factor, which still couples its kick blocks.

## Exact short traces and a number-variance alternative

Knowing every trace through a prescribed \(t_{\mathrm{cut}}(N)=o(N)\) is insufficient for general unitary spectra, even when a weak local limit is known and unit-window variance is bounded. Repeat the turns of a \(D\)-point seed in \(L\) equally spaced sectors, taking the phases \((\alpha_j+\ell)/L\) with \(0\le\ell<L\). The traces are zero unless \(L\mid n\), in which case they equal \(L p_{n/L}(\text{seed})\). The unfolded spectrum is the \(D\)-periodic repetition of the unfolded seed, so the uniform-origin window distributions and \(T(K)\) are exactly inherited from the seed. This also preserves any band-weighted normalized trace sum, by setting \(n=Lm\) and dividing by \((LD)^2\).

For one seed take a \(D\)-point clock. For the other, remove \(2q\) points, \(q=\lfloor\sqrt D\rfloor\), and place them at distinct sites in two intervals of vanishing diameter whose centers have fixed separation in mean-spacing units. Choose sites away from any retained point. The chance of seeing an edit in a fixed uniform-origin window is \(O(q/D)\). The unit second moments stay bounded: pairs touching an edited site and a retained clock point number \(O(q)\), and pairs with both sites edited number \(O(q^2)\). But the new \(T(K)\) is at least \(2q^2/D\) for each fixed \(K\) and large \(D\), while the clock has \(T(K)=0\) for \(K\ge1\). For each odd \(D\) choose an odd \(L\) so large that \(t_{\mathrm{cut}}(LD)<L\). Both repeated spectra are simple and have exactly the same complex traces through that cutoff. This construction concerns abstract spectra.

For a separate sufficient criterion write \(V_N(R)=\mathbb E(C(x,R)-R)^2\) for the variance in a sliding window of length \(R\), \(1\le R\le N\). Partition the circle into half-unit cells of counts \(q_j\). The five-cell maximum gives
\[
 T(5K)\le\frac{25}{N}\sum_{q_j>K}q_j^2.
\]
If \(q_j>2R\), the cell is fully contained by windows from a set of origins of length at least \(R-1/2\). At an origin whose window fully contains any such cell, the sum of squares of all fully contained heavy cell counts is at most \(C(x,R)^2\le4(C(x,R)-R)^2\). This proves
\[
 T(10R)\le \frac{100}{R-1/2}V_N(R).
\]
Hence \(\liminf_{R\to\infty}\limsup_{N\to\infty}V_N(R)/R=0\) suffices for crowding, with \(R\) fixed in the inner limit. Conditional on weak Sine₂ convergence, the crowding condition conversely gives convergence of each fixed-window variance. The sine kernel yields
\(V_*(R)=2\int_0^R u\,\operatorname{sinc}^2 u\,du+2R\int_R^\infty\operatorname{sinc}^2u\,du=O(\log(2+R))\),
using the integral of the squared sinc over the real line. This proves the converse under that weak-law assumption.

The same obstruction can coexist with agreement in every fixed positive time band. Given a sublinear cutoff \(t_{\rm cut}(N)\), let \(q=\max(2,t_{\rm cut}(N)+1)\) be an integer, \(L=N/q\), \(d=\lfloor L^{3/4}\rfloor\), \(s=d/L\), and \(r=qd\). Decorate a common \((N-r)\)-point clock either with an \(r\)-point clock or with the \(r\) phases \(a/q+bs/N\), \(0\le a<q,\ 0\le b<d\). Rotate each decoration away from coincidences. Both decorations have exactly zero traces through the cutoff. Both change any fixed local window with probability \(O(s)\) and their unit counts have bounded second moment: for the packets \(C\le1+1/s\) and \(\mathbb E C=s\). Every packet point has at least \(1/(2s)\) strict unit neighbours for large \(N\), giving limiting tail at least \(1/2\) at each fixed threshold. The reference decoration has bounded local counts. In a fixed band \(a_0N\le n\le b_0N\), \(a_0>0\), the packet trace vanishes unless \(q\mid n\) and otherwise has modulus at most \(q/(2a_0s)\) by the geometric sum. Its normalized squared sum there is \(O(1/(Ls^2))=o(1)\). The clock decoration has normalized squared sum \(O(r/N)=o(1)\). The common clock background has bounded energy per band, so Cauchy–Schwarz also gives agreement up to \(o(1)\) in every bounded-weight squared-trace test supported in such a band. These spectra explain why separated positive bands can miss the frequencies near zero in the ordered Fejér criterion.
