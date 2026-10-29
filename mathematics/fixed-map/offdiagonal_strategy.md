# Strategy note: the signed off-diagonal sum

**Status:** strategy, 29 October 2026. This note is not a theorem and has no claim ID. It does not close `BGS-TRACE-005` or `BGS-BGS-001`. Section 6 records an external reconnaissance. That section is a lead list. No constant, window, or mechanism in it has been re-derived here, and none of it is a registered claim.

The diagonal Abel classification for every odd modulus is `BGS-TRACE-124`. Further case splits on the order of \(C\) do not estimate the signed sum that `BGS-TRACE-005` asks for. This note records which uniform methods were examined, which identity is proved in [the uniform overlap law](uniform_orbit_overlap.md), and which structural question is the next route.

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

A bound that separates \(L_N(U_N;1)\) from the CUE value, in one of the three senses of Section 2, would refute `BGS-BGS-001` for this map. No such bound is proved. A limit of the signed statistic to the CUE value would be `BGS-TRACE-005` in the pair case. No such limit is proved. The remainder past \(f''(0)\), and any other expression for \(\operatorname{Tr}U_N^m\) at times of order \(N\), stay open. They are not the next route. Section 6 explains why a sharper diagonal dichotomy is also not the next route.

Prime squares are placed by `BGS-TRACE-124`. The modulus \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) is short. Density of the order classes is not the route either.

## 6. Unverified reconnaissance, and the route that has priority

On 29 October 2026 an external reconnaissance was reported. It is unverified by the standard of this repository. The matrix checks, the fixed-point count, the CRT comparison through odd \(N\le401\), the eigenvalue agreement, the numerical Abel values, the strong-coupling runs, and every extrapolated scale in that report were not repeated here. Their constants are omitted. A later certificate may re-derive any one of them. Until that certificate exists, the sentences below are a description of proposed work, not a theorem, not a numerical result, and not an input of `BGS-TRACE-125`.

**Half-order clause, already in the repository.** The reported divisibility is the half-order lemma of `BGS-TRACE-121`, Section 3, recorded again as ERR-061. If \(p\equiv\pm1\pmod8\), then \(t(p)\) divides \((p-1)/2\). If \(p\equiv3\pmod8\) or \(p\equiv5\pmod8\), then the cofactor \((p+1)/t(p)\) is odd. The equality \(t=(p+1)/2\) does not occur. The long class is the inert full order \(t=p+1\). The same search of the maintained notes, the claim boundaries, and the manuscript sections on this branch found no remaining argument that uses \(t=(p+1)/2\) as a nonempty class. The hypothesis \(2t\ge p+1\) in Theorem 2 of `BGS-TRACE-120` is a lower bound on the order. On an odd prime the half-order lemma makes that hypothesis exactly \(t=p+1\). Summaries that say "order at least \((p+1)/2\)" mean this hypothesis. They do not assert that the order equals \((p+1)/2\).

**Proposals that stay outside the registry.** The reconnaissance proposes four mathematical shapes.

1. A closed form for the diagonal contribution to the Abel sum, of size comparable to the number of returns, and an identity expressing the signed off-diagonal Abel sum as \(L_N(M_N;1)-1/4\) plus an error of size \(O(N^{-2})\). If that identity were proved, the CUE target for the signed sum would be \(-e^{-2}/4\), because the CUE value of \(L\) is \((1-e^{-2})/4\). The identity is not proved here. A windowed pair test along full-order primes was also reported. It is not `BGS-TRACE-005`.
2. A convergent series for \(L_{p^k}(M;1)\) when the lifting depth is one or the exponent is one. `BGS-TRACE-121` already decides those powers by the coarser thresholds \(3/4\) and \(5/7\). The series is not certified here.
3. A pure-map gap sharper than `BGS-TRACE-124`, separating inert full-order prime powers of depth one from every other odd modulus, including every non-square-free modulus. The reconnaissance reported a check through every odd modulus up to \(2\cdot10^6\). That check was not repeated. `BGS-TRACE-124` already gives \(L>3/4\) or \(L<5/7\) for every odd \(N\ge3\). The sharper constants, the finite list of primes said to need a direct certificate, and the claimed exclusion of a neighborhood of the CUE value are not certified here. Opening that dichotomy as a new claim would be another diagonal case. It is not the priority.
4. A kick separation on a long initial interval of odd dimensions, read off a kick bound already in the repository, together with a first- and second-order expansion of the kick difference. The expansion was reported to depend on an identity for \(\operatorname{Tr}(T(v)M^m)\) that the reconnaissance itself marked unchecked. The kick windows that are proved remain those of `BGS-TRACE-120` through `BGS-TRACE-124`.

**Symmetry-breaking reformulation.** The same report proposes a mechanism at couplings other than \(\tau=10^{-80}\). It says that a dominant part of the fixed symbol commutes with parity and preserves time reversal, and that a smaller part breaks both, in the sense of the arithmetic pseudo-symmetries discussed by Keating–Mezzadri. This note does not decompose the symbol, does not check a commutation, and does not run a strong-coupling experiment. An extrapolation from another coupling to \(\tau=10^{-80}\) is not a statement about \(U_N\).

The structural target is a negative control and a rescaled limit, and both still have to be proved. A kick built only from the symmetry-preserving part of the symbol would have to be shown to commute with parity and to be time-reversible. The CUE law is the ensemble without time-reversal symmetry, so a time-reversible operator is a candidate for a different ensemble. This note does not identify that ensemble and does not prove a pair law for any truncated kick. If the commutation and a non-CUE pair law for the truncated kick are both proved, a proof of `BGS-BGS-001` for the actual fixed kick has to use the symmetry-breaking part quantitatively. The proposed limit sends \(\tau^2 N^3\) to infinity and sends the symmetry-breaking strength to infinity. That limit is not the fixed coupling \(\tau=10^{-80}\), it is not `BGS-BGS-001` as now registered, and it is not a claim in `record/claims.json`.

One distinction already follows from the proved Abel bounds and does not need the reconnaissance. A value of \(L_N\) near \((1-e^{-2})/4\) would still not be a spacing law. `BGS-TRACE-005` asks for the signed factorial joint trace. An Abel number is one scalar.

**Reading list, not a dependency.** Kurlberg–Rudnick, arXiv:chao-dyn/9901031, and Keating–Mezzadri, Nonlinearity 13 (2000), 747–775, are already background in Section 2. The names Keating (1991), Kurlberg–Rudnick (2001), Kurlberg (2003), Roskam (2000 and 2002), and Boasman–Keating (1995) were not opened in this pass. They are not registered external lemmas. Exact locators belong in `literature/` before any of them is used in a proof.

**Priority.** The next route is the symmetry-breaking reformulation: identify the part of the symbol that preserves parity and time reversal, prove or refute the commutation, and only then write a scaled-coupling statement whose hypotheses match that decomposition. A sharper pure-map gap, a depth-one series, and a longer kick expansion can be certified afterwards. They do not control the signed sum at times of order \(N\). No new claim ID is opened for any item in this section.
