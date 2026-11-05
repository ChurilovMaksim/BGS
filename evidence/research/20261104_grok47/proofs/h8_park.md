# H8 parked: four obstructions

Tags in this file are local to the note. **[P]** is a theorem already proved in this directory, or an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure already recorded in the cited log. This note does not recompute those enclosures. A finite enclosure is not an asymptotic bound on a trace ratio. `record/claims.json` was not edited.

H8 is BGS-TRACE-306. On composite \(h_p\), in the amplified normalisation, the draft asks for a loss exponent \(c < 1.1718\,\ell_0/\ln d\). At \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\) the exponent \(c = 1\) covers
\[
\theta < 0.16661157
\]
and stops there. The first-moment threshold of `proofs/h7_h8.md` Proposition 8 lies above \(0.26223963\). The open interval is
\[
\theta \in (0.16661157,\ 0.26223963).
\]

**Decision.** None of the four routes below enlarges the covered range. The amplified wrap remains \(\theta < 0.16661157\). H8 stays open. This note parks the attack. It does not delete H8 from Theorem R♯-mod v5, and it does not refute H8.

The aggregate comparisons at \(p = 19\) and \(p = 29\) stay parked, as in `proofs/h8_energy.md`. Both primes lie under the conditional thresholds \(1409\) and \(3307\). H7* stays a hypothesis of v5.

## 1. Uniform norm

The amplified weight is uniform in the modulus. N16b (c2), under the hypothesis that the points carry weights \(\asymp d/h\), charges a factor \(d\) sitting outside the power \(\ell^3 \le \ell^2\). The loss exponent is \(1\), for every \(d\). At \(\ell_0 = p/4\) and \(\rho = 0.28\),
\[
\theta < \frac{\alpha(0.28)}{4\ln\lambda}, \qquad \alpha(\rho) = -\ln\bigl((\lambda\rho^2)^{3/2}\bigr).
\]
The ball for \(\alpha(0.28)\) has centre \(1.17477626638003325659\) and radius \(3\cdot 10^{-59}\) (`proofs/h7_h8.md`). The resulting threshold is \(\theta < 0.16661157\).

The trivial character bound on the same sum is \(|S| \le L\). Every later route is an attempt to beat that bound on the open interval. None of them does, at either conditional prime.

The weighted \(2\)-norm of the finite section is a different operator. In `proofs/h7_uniform.md` every twist of the rank-\(280\) section has weighted \(2\)-norm at most \(246/100\). The section majorant is \(6.768238765003160\cdot 10^{44}\), against the \(\eta = 1\) threshold \(3.8762299862656054\cdot 10^{27}\), a quotient \(1.7460880259903623\cdot 10^{17}\). The meeting rate is \(R_* = 1.225865206681737\), a factor \(2.006745918386011\) below \(246/100\). The untwisted section trace alone exceeds that threshold by \(3.9934073393176425\cdot 10^{8}\). That bound is a bound on the finite section. It is not a bound on \(\hat Z\), and it does not change the exponent \(1\) in the wrap.

## 2. Additive energy

`proofs/h8_energy.md`, Theorems 1 and 2. For a split prime the additive energy of the graph of \(\langle\lambda\rangle\) equals \(2L^2 - L\) when the order \(L\) is odd, and \(3L^2 - 3L\) when \(L\) is even. The odd uniqueness is BGS-TRACE-279. For an odd modulus with a split prime factor of the same order, the energy is at most \(2L^2 - L\). The bound does not depend on the modulus. The ratio to the trivial energy \(L^3\) is \(< 2/L\).

The character-sum form of TRACE-279 beats \(|S| \le L\) only for
\[
\theta < \frac{\ln(L^2/2)}{p\ln\lambda}.
\]
At \(L = 3p\) this is \(< 0.00644413\) for \(p = 1409\) and \(< 0.00303834\) for \(p = 3307\), inside the exponent-\(1\) range. The factor \(d\) in the amplified weight is not this energy. Substituting \(d\cdot(2/L)\) for \(d\), which that note does not justify, reaches at most \(\theta < 0.16969410\) at \(p = 1409\) and \(\theta < 0.16807128\) at \(p = 3307\). Both lie under \(0.26223963\). The same formal sum at \(p = 19\) crosses \(0.26223963\). That prime lies under \(p_{\mathrm{thr}}\), and the substitution is not a theorem.

The integers \(49\) and \(343\) have energies \(1617\) and \(122451\), above \(2L^2 - L\), because the order grows. The bound needs a split prime factor of equal order.

## 3. Lifted window energies

`proofs/h8_moments.md`. A congruence of two \(k\)-sums of powers of \(\lambda\), with exponents in an interval of span \(l\), is an equality in \(\mathbb Z[\sqrt 2]\) when \(4k^2\lambda^l < d^2\). The span is \(l < 2\log_\lambda d - \log_\lambda(4k^2)\). It contains \(\ell_0 = p/4\) throughout the open interval, for \(k \le 7\) at \(p \in \{1409, 3307\}\). The length \(\ln d/(2\ln\lambda)\) contains \(p/4\) only for \(\theta \ge 1/2\).

For \(k \le 6\) the only equalities are permutations, so the ordered energy of a liftable window is at most \(k!\,|W|^k\). The first non-permutation has mass \(7\), and it is \(\lambda^4 + 6\lambda = 6\lambda^3 + 1\) up to translation and swapping sides. The \(2k\)-moment beats \(|S| \le |W|\) only for \(\theta < 0.00576146\) at \(p = 1409\), \(k = 6\), and for \(\theta < 0.00289289\) at \(p = 3307\). The full orbit of length \(p\) or \(3p\) does not fit in the liftable span.

The weight \(d\) is not this energy. The formal product of \(d\) with the energy ratio, which that note does not justify, reaches at most \(\theta < 0.17973708\) at \(p = 1409\) and \(\theta < 0.17322030\) at \(p = 3307\). Covering \(0.26223963\) would require an exponent under \(0.63534092\). The formal combined exponent stays above \(0.92122088\).

## 4. BGK and HBK ranges

`proofs/h8_energy.md`, §3. Bourgain–Glibichuk–Konyagin needs a fixed \(\delta > 0\) with \(|\langle\lambda\rangle| \ge q^\delta\). At the bottom of the gap,
\[
\delta_{\max}(1409) < 0.02017629, \qquad \delta_{\max}(3307) < 0.00947485.
\]
A fixed \(\delta \ge 0.01\) fails on \(\theta \ge 0.16661157\) for every prime \(p \ge 3307\). The sharp form that needs \(\log|H| > C\log q/\log\log q\), and the Montgomery–Vaughan–Wooley conjecture that needs \(|H|/\log q \to \infty\), fail for the same reason. \(|H|\) is \(p\) or \(3p\), and \(q\) is a power of \(\lambda\) on the gap.

Heath-Brown–Konyagin, Quart. J. Math. 51 (2000) 221–235, applies to the projection whenever \(L \le q^{2/3}\). That size restriction holds on the open interval at these primes. The projected energy is \(\ll L^{5/2}\), with no numeric implied constant in that paper, and the graph energy of Theorem 1 is the sharper count \(2L^2 - L\). The character-sum form \((q\,T_2/L)^{1/4}\) has shape \(q^{1/4}L^{3/8}\). At \(\theta = 0.16661157\), \(L = 3p\) and \(p \in \{1409, 3307\}\) the ratio of that shape to \(L\) exceeds \(1\) by an exponential in \(p\). A fixed implied constant moves the meeting point by \(\ln C/(p\ln\lambda)\) and does not close a gap of width \(0.09\).

## 5. What stays open

The covered range is \(\theta < 0.16661157\). The interval up to \(0.26223963\) stays open. H8 is not discharged and not refuted. The four routes are recorded in `proofs/h7_uniform.md`, `proofs/h7_h8.md`, `proofs/h8_energy.md` and `proofs/h8_moments.md`. This note is the index of those obstructions.
