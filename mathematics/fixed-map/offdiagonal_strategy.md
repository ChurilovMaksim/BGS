# Strategy note: the signed off-diagonal sum

**Status:** strategy, 29 October 2026. This note is not a theorem and has no claim ID. It does not close `BGS-TRACE-005` or `BGS-BGS-001`. Section 6 records an external reconnaissance. That section is a lead list. No constant, window, or mechanism in it has been re-derived here, and none of it is a registered claim.

The diagonal Abel classification for every odd modulus is `BGS-TRACE-124`. Further case splits on the order of \(C\) do not estimate the signed sum that `BGS-TRACE-005` asks for. This note records which uniform methods were examined, which identity is proved in [the uniform overlap law](uniform_orbit_overlap.md), and how the open routes rank. Priority 1 is a correct proved statement about the spectrum of this \(U_N\). Priority 2, kept in parallel in Section 7, is a generalization whose method transfers. Section 7 ranks both by significance and by realistic provability.

## 1. The target

`BGS-TRACE-005` asks for the CUE-subtracted signed factorial joint trace, with the dimension outside the whole sum, at every fixed order and every compact Fourier weight. `BGS-BGS-001` asks for the microscopic law that would follow from that estimate together with the trace bridge, the symmetry hypotheses, and the fixed unfolding. The model is the kicked propagator \(U_N=\exp(i\tau N A_N)M_N\) at the fixed coupling \(\tau=10^{-80}\).

The pair form of the same gap can be written through the transported product. At a return where \(M_N^n\) is scalar, \(\lvert\operatorname{Tr}U_N^n\rvert\) equals the modulus of \(\operatorname{Tr}\prod_{j=0}^{n-1}\exp(i\theta A_j)\). The second derivative of that trace at zero coupling is \(-\theta^2\operatorname{Tr}(S^2)\), and \(\operatorname{Tr}(S^2)/N\) is the weighted sum of the symbol overlaps \(\gamma(r)\). The Heisenberg-time signed sum is a different object: times of order \(N\), not the short Pell return \(n\ll N\).

## 2. What the linear cat map does not decide

Quantized linear cat maps are not generic. Kurlberg–Rudnick, arXiv:chao-dyn/9901031, document Hecke degeneracies of the linear quantization, and Keating–Mezzadri, Nonlinearity 13 (2000), 747–775, document arithmetic pseudo-symmetries. Both references are background already recorded in this repository. They are not registered external lemmas, and they are not inputs of `BGS-TRACE-125`.

The pure propagator \(M_N\) is already a proved non-CUE example on the exponential sequence of odd Pell dimensions \(N=u_n\). The integers \(u_n\) satisfy \(u_{n+2}>5u_n\), so the sequence is exponential, not an arithmetic progression. `BGS-TRACE-117`, Theorem 1, gives \(M_N^n=\zeta I\) and \(L_N(M_N;1)>3/4\) at every odd index \(n\ge5\). The distance to \((1-e^{-2})/4\) is greater than \(1/2\), on the side away from the CUE value. That statement does not need a new citation.

The kicked operator is not \(M_N\). `BGS-FM-032` shows that the symbol stays a positive normalized Hilbert–Schmidt distance from the additive commutant of \(M_p\): for an odd prime \(p>99\), the squared distance satisfies an explicit positive bound of order \(1/d\), and at physical strength \(\tau p\) the additive distance tends to infinity. The same note states that this is an additive, linearized obstruction, not a nonperturbative multiplicative coboundary obstruction. The hypothesis is an odd prime \(p>99\), and the distance is the additive Hilbert–Schmidt distance of the symbol from the commutant. The note does not treat Hecke multiplicities, the Pell dimensions \(u_n\), or the kicked propagator \(U_N\). The inference that those multiplicities fail to be eigenvalues of \(U_N\) does not follow from `BGS-FM-032`. That inference is a heuristic. It is not a theorem, and it is not part of `BGS-TRACE-125`.

\(L_N(U_N;1)\) is an Abel sum of \(\lvert\operatorname{Tr}U_N^m\rvert^2/N^2\). A uniform positive lower bound on \(\lvert\operatorname{Tr}U_N^n\rvert/N\) at the single time \(m=n\) does not by itself force that sum away from \((1-e^{-2})/4\). A separation would require one of three bounds. After the weight \(e^{-2n/N}\), that one term exceeds the CUE value by a definite gap. Or an upper bound gives \(L_N(U_N;1)\le(1-e^{-2})/4-c\) for a fixed \(c>0\). Or a lower bound shows that the whole sum stays above \(3/4\), which is distance greater than \(1/2\) from the CUE value. The coarser comparison \(L_N<5/7\) is a dichotomy threshold of the pure map. It is not one of these three bounds, because \(5/7\) is larger than \((1-e^{-2})/4\). The second-order disk does not supply any of these past the range already certified. `BGS-TRACE-119` shows that the pure second-order center at \(n=207\) lies below \(3/4\). The overlap law below makes that center explicit for every odd return, and the same growth \(u_{n+2}>5u_n\) pushes the second-order term further. Without a remainder bound, a center below \(3/4\) is not a separation of \(L_N(U_N;1)\).

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

A bound that separates \(L_N(U_N;1)\) from the CUE value, in one of the three senses of Section 2, would refute `BGS-BGS-001` for this map. Those senses are the weighted one-term gap, the upper bound \(L_N(U_N;1)\le(1-e^{-2})/4-c\) for a fixed \(c>0\), and the lower bound above \(3/4\). No such bound is proved. A limit of the signed statistic to the CUE value would be `BGS-TRACE-005` in the pair case. No such limit is proved. The remainder past \(f''(0)\), and any other expression for \(\operatorname{Tr}U_N^m\) at times of order \(N\), stay open. They are the missing step of Priority 1, and Section 7 records that this step is not within reach of the methods now proved. A sharper diagonal dichotomy is not that step.

Prime squares are placed by `BGS-TRACE-124`. The modulus \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) is short. Density of the order classes is not the route either.

## 6. Unverified reconnaissance, and the route that has priority

On 29 October 2026 an external reconnaissance was reported. It is unverified by the standard of this repository. The matrix checks, the numerical fixed-point recount, the CRT comparison through odd \(N\le401\), the eigenvalue agreement, the numerical Abel values, the strong-coupling runs, and every extrapolated scale in that report were not repeated here. Their constants are omitted. A later certificate may re-derive any one of them. Until that certificate exists, the sentences below are a description of proposed work, not a theorem, not a numerical result, and not an input of `BGS-TRACE-125`.

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

The symmetry-breaking proposal is one route inside the ranking of Section 7. It is not a substitute for a theorem about this \(U_N\), and it is not yet a theorem. A sharper pure-map gap, a depth-one series, and a longer kick expansion remain uncertified proposals. They do not control the signed sum at times of order \(N\). No new claim ID is opened for any item in this section.

## 7. Ranked routes

Two axes are used. Significance means the distance from a correct statement about spectral statistics. Provability means what the methods already in this repository can realistically close under the quality gate: an exact numeric check, Lean where the statement is an integer comparison, an audit, and wording that stops at the proof. A route may rank high on one axis and low on the other. Nothing in this section is a new claim.

The model of Priority 1 is fixed. \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\), \(C=S^T\), \(\tau=10^{-80}\), and \(U_N=\exp(i\tau N A_N)M_N\). The symbol of \(A_N\) has 32 Fourier modes. `BGS-FM-001` already proves that the classical kicked map has trivial \(C^1\) centralizer and no \(C^1\) reversor for every flow time \(\kappa\) with \(0<\lvert\kappa\rvert\le10^{-12}\). Equation (4) of that note identifies the classical map of this \(U_N\) with that theorem at \(\kappa=\tau/(2\pi)\), and \(\lvert\tau/(2\pi)\rvert\le10^{-12}\). Its boundary excludes ordinary \(C^1\) reversors and does not exclude an \(N\)-dependent quantum symmetry. It does not prove `BGS-BGS-001`.

### Priority 1: this \(U_N\)

1. **The signed sum at times of order \(N\).** Significance is maximal: this is `BGS-TRACE-005` for the pair weight, and `BGS-BGS-001` needs it. Provability is not within reach. Sections 2 and 3 record the obstruction. Gauss sums and the Weil representation stop at \(M_N\). `BGS-FM-032` is an additive distance for odd primes \(p>99\). `BGS-TRACE-125` fixes \(f''(0)\) and does not fix \(f(1)\). No estimate in the corpus controls the noncommutative product out to time \(m\asymp N\).

2. **An exact symmetry test for this 32-mode symbol.** Significance is high and is still about this \(U_N\). The question is whether the Fourier coefficients of the maintained symbol commute with a stated parity operator or satisfy a stated reversal identity. `BGS-FM-001` answers the classical \(C^1\) question for the full symbol and leaves the quantum question open. Provability of the finite test is realistic: the mode list is finite, the arithmetic can be rational, and Lean can decide the resulting integer identities. Provability of a Poisson, COE, two-block COE, or CUE limit from the outcome of that test is not within reach. A truncated kick, built by dropping modes, is a different operator. A theorem about that truncation is not a theorem about \(U_N\) until the dropped part is estimated.

3. **The Abel scalar \(L_N(U_N;1)\).** Significance is real and limited. It is one number. A value near \((1-e^{-2})/4\) would not be a spacing law, and a value far from it would not identify the ensemble. The windows already proved are those of `BGS-TRACE-117` through `BGS-TRACE-124`. Further windows are realistic case work. They are not the strongest statement on this list. The second-derivative identity of `BGS-TRACE-125` rewrites, with \(\theta=\tau N\), as
\[
f''(0)=-\tau^2 N^3\, n\cdot\frac{1650797}{4000000}.
\]
The normalized coefficient is \(f''(0)/N=-\tau^2 N^2 n\cdot 1650797/4000000\). Both monomials are this identity. At the short-kick edge \(N=10^{39}\) one has \(\tau^2 N^3=10^{-43}\). The equation \(\tau^2 N^3=1\) is \(N^3=10^{160}\). These are exponent comparisons. They are not a crossover of \(L_N(U_N;1)\) and not a limit law.

### Priority 2: generalizations whose method transfers

These sit beside Priority 1. A generalization enters the registry only after the same quality gate. None is opened here.

1. **Every hyperbolic matrix in \(\mathrm{SL}(2,\mathbb Z)\), for the pure propagator.** Significance is high. The trace-square formulae in `BGS-TRACE-120` are proved for this \(C\). Section 2 of that note is the fixed-point lemma: \(\lvert\operatorname{Tr}M_N^m\rvert^2\) equals the number of labels fixed by \(C^m\). Section 2 of `BGS-TRACE-122` cites that identity for the Chinese product. The numerical recount in Section 6 was not repeated here. The constants \(3/4\) and \(5/7\), the Pell overlaps, and the 32-mode kick use \(S\) and this symbol. Provability of a written separation is realistic. The work is to mark, lemma by lemma, which steps in `BGS-TRACE-120` through `BGS-TRACE-125` use only a splitting law in \(\mathbb F_p[x]/(x^2-\Delta)\) and which use \(\Delta=2\) or the mode list. That marking is not done in this note. `BGS-CAYLEY-010` already gives finite exact spectra for arbitrary hyperbolic matrices under its fixed-point-free hypothesis, and its boundary says that a later "work verbatim" transfer was not proved. The kicked operator for a general cat map is not within reach, because \(A_N\) is this symbol.

2. **A quantitative symmetry-breaking parameter for a general trigonometric kick.** Significance is high for the ensemble question. Provability splits. For this 32-mode symbol the parameter is the finite test in Priority 1. For a general smooth or trigonometric kick, with an arbitrary Fourier support and an arbitrary size of the breaking part, the required symbol calculus is not in the proved corpus. That general theorem is not within reach.

3. **A scaled-coupling limit.** Significance is high if the fixed \(\tau=10^{-80}\) never leaves a perturbative regime, because the registered statement would then be the wrong limit. Provability of the limit law is not within reach. The monomials \(\tau^2 N^3\) and \(\tau^2 N^2\) occur in the identity above. Sending either to infinity is a proposed limit, not a theorem, and it is not `BGS-BGS-001`. The strong-coupling experiments and the extrapolated scales in Section 6 stay uncertified.

4. **A classification theorem: arithmetic order and pseudo-symmetries decide Poisson, COE, two COE blocks, or CUE.** Significance is maximal among the generalizations. Provability is not within reach. It is the open problem that `BGS-BGS-001` is one instance of. The names of the four ensembles can be recorded as the shape of a future statement. No implication from the order of \(S\), from a Hecke degeneracy, or from a pseudo-symmetry to one of those ensembles is a lemma of this repository. `BGS-FM-001` removes a classical \(C^1\) reversor and does not choose an ensemble.

### What a later certificate can honestly close

Within reach, and not done: the finite symmetry test for this symbol, and a line-by-line separation of the existing Abel proofs into the hyperbolic part and the discriminant-\(2\) part. Out of reach with the present method: `BGS-TRACE-005`, `BGS-BGS-001`, an ensemble classification, a general smooth-kick theorem, a scaled-coupling limit law, and every numerical bound reported in Section 6.
