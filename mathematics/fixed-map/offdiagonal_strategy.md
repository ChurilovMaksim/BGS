# Strategy note: the signed off-diagonal sum

**Status:** strategy, 29 October 2026. This note is not a theorem and has no claim ID. It does not close `BGS-TRACE-005` or `BGS-BGS-001`.

The diagonal Abel classification for every odd modulus is `BGS-TRACE-124`. Further case splits on the order of \(C\) do not estimate the signed sum that `BGS-TRACE-005` asks for. This note records which uniform methods were examined, why a disproof of `BGS-BGS-001` is not available, and which identity is proved instead in [the uniform overlap law](uniform_orbit_overlap.md).

## 1. The target

`BGS-TRACE-005` asks for the CUE-subtracted signed factorial joint trace, with the dimension outside the whole sum, at every fixed order and every compact Fourier weight. `BGS-BGS-001` asks for the microscopic law that would follow from that estimate together with the trace bridge, the symmetry hypotheses, and the fixed unfolding. The model is the kicked propagator \(U_N=\exp(i\tau N A_N)M_N\) at the fixed coupling \(\tau=10^{-80}\).

The pair form of the same gap can be written through the transported product. At a return where \(M_N^n\) is scalar, \(\lvert\operatorname{Tr}U_N^n\rvert\) equals the modulus of \(\operatorname{Tr}\prod_{j=0}^{n-1}\exp(i\theta A_j)\). The second derivative of that trace at zero coupling is \(-\theta^2\operatorname{Tr}(S^2)\), and \(\operatorname{Tr}(S^2)/N\) is the weighted sum of the symbol overlaps \(\gamma(r)\). The Heisenberg-time signed sum is a different object: times of order \(N\), not the short Pell return \(n\ll N\).

## 2. What the linear cat map does not decide

Quantized linear cat maps are not generic. Kurlberg–Rudnick, arXiv:chao-dyn/9901031, document Hecke degeneracies of the linear quantization, and Keating–Mezzadri, Nonlinearity 13 (2000), 747–775, document arithmetic pseudo-symmetries. Both references are background already recorded in this repository. They are not registered external lemmas, and they are not inputs of `BGS-TRACE-125`.

The pure propagator \(M_N\) is already a proved non-CUE example on the exponential sequence of odd Pell dimensions \(N=u_n\). The integers \(u_n\) satisfy \(u_{n+2}>5u_n\), so the sequence is exponential, not an arithmetic progression. `BGS-TRACE-117`, Theorem 1, gives \(M_N^n=\zeta I\) and \(L_N(M_N;1)>3/4\) at every odd index \(n\ge5\). The distance to \((1-e^{-2})/4\) is greater than \(1/2\), on the side away from the CUE value. That statement does not need a new citation.

The kicked operator is not \(M_N\). `BGS-FM-032` shows that the symbol stays a positive normalized Hilbert–Schmidt distance from the additive commutant of \(M_p\): for an odd prime \(p>99\), the squared distance satisfies an explicit positive bound of order \(1/d\), and at physical strength \(\tau p\) the additive distance tends to infinity. The same note states that this is an additive, linearized obstruction, not a nonperturbative multiplicative coboundary obstruction. The hypothesis is an odd prime \(p>99\), and the distance is the additive Hilbert–Schmidt distance of the symbol from the commutant. The note does not treat Hecke multiplicities, the Pell dimensions \(u_n\), or the kicked propagator \(U_N\). The inference that those multiplicities fail to be eigenvalues of \(U_N\) does not follow from `BGS-FM-032`. That inference is a heuristic. It is not a theorem, and it is not part of `BGS-TRACE-125`.

\(L_N(U_N;1)\) is an Abel sum of \(\lvert\operatorname{Tr}U_N^m\rvert^2/N^2\). A uniform positive lower bound on \(\lvert\operatorname{Tr}U_N^n\rvert/N\) at the single time \(m=n\) does not by itself force that sum away from \((1-e^{-2})/4\). A separation would require one of three bounds. After the weight \(e^{-2n/N}\), that one term exceeds the CUE value by a definite gap. Or an upper bound shows that the whole sum stays below \(5/7\), which is distance less than \(1/2\) from the CUE value. Or a lower bound shows that the whole sum stays above \(3/4\), which is distance greater than \(1/2\). The second-order disk does not supply any of these past the range already certified. `BGS-TRACE-119` shows that the pure second-order center at \(n=207\) lies below \(3/4\). The overlap law below makes that center explicit for every odd return, and the same growth \(u_{n+2}>5u_n\) pushes the second-order term further. Without a remainder bound, a center below \(3/4\) is not a separation of \(L_N(U_N;1)\).

`BGS-BGS-001` stays open. The statements proved in this direction are the pure-map spike of `BGS-TRACE-117` and the overlap identity of `BGS-TRACE-125`. Neither identifies the spectrum of \(U_N\).

## 3. Methods that stop at \(M_N\)

Exact Gauss sums and the Weil representation evaluate traces of \(M_N\). The factor \(\exp(i\theta A_N)\) is the exponential of a sum of noncommuting Weyl operators. It is not a single Weil matrix, and the product of the transported exponentials is not one either. Those formulae do not evaluate \(\operatorname{Tr}U_N^m\).

An eigenbasis of \(M_N\) diagonalizes the linear factor. `BGS-FM-032` does not transfer that basis to \(U_N\). Its obstruction is additive and linearized, for odd primes \(p>99\), and the note states that this is not a multiplicative coboundary obstruction. It does not prove that an eigenbasis of \(M_N\) fails to be an eigenbasis of \(U_N\).

Equidistribution and Kloosterman bounds control exponential sums attached to the linear action. The signed sum for \(U_N\) is a trace of a noncommutative product, weighted by \(e^{-2m/N}\) out to times of order \(N\). No such bound in the present corpus estimates that weight. Sum-product and Cayley-energy reductions in the repository likewise stop before \(Y_{m,N}\). A model-theoretic or representation-theoretic rewriting has to name an object whose matrix coefficient is \(\operatorname{Tr}U_N^m\). The Weil representation names \(\operatorname{Tr}M_N^m\).

## 4. The identity that is uniform

The symbol has 32 Fourier modes, supported in \(\lvert k\rvert\le9\), \(\lvert\ell\rvert\le1\). Along an odd Pell return the frequency matrix satisfies \(C^n\equiv I\pmod{u_n}\). The overlap \(\gamma(r)\) is then a finite congruence condition in a fixed box.

That condition is rigid. For every odd \(n\ge5\), the only nonzero overlaps in \(1\le r\le n-1\) are the lag \(r=1\) and the inverse lag \(r=n-1\), both equal to \(-7/2000000\). The quadratic coefficient is exactly
\[
\frac{\operatorname{Tr}(S^2)}{N}=n\cdot\frac{1650797}{4000000}.
\]
The argument is one size comparison, one archimedean comparison in \(\mathbb Z[\sqrt2]\), and one Pell-norm congruence at the middle index. The single index \(n=5\) has a middle lag too small for the divisibility, and that index is a finite scan. This is `BGS-TRACE-125`. It replaces the separate overlap scans at \(n=203\), \(n=205\), and \(n=207\). It is the same coefficient those notes computed one index at a time.

The identity fixes \(f''(0)\). It does not fix \(f(1)\). The third-derivative majorant of `BGS-TRACE-118` is already larger than the gap once the second-order term is large, and no estimate of the integral remainder is claimed here. The weighted off-diagonal sum at Heisenberg time is untouched.

## 5. What remains open

The next mathematical object is the signed sum itself: either a uniform bound on the remainder past the second derivative, or a different expression for \(\operatorname{Tr}U_N^m\) at \(m\asymp N\). A bound that separates \(L_N(U_N;1)\) from the CUE value, in one of the three senses of Section 2, would refute `BGS-BGS-001` for this map. No such bound is proved. A limit of the signed statistic to the CUE value would be `BGS-TRACE-005` in the pair case. No such limit is proved.

Prime squares are placed by `BGS-TRACE-124`. The modulus \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) is short. They are not an open case of the diagonal classification, and they are not the route of this note. Density of the order classes is not the route either.
