# Self-referee of the line-sum note

Read against `proofs/h5_xline.md`, `code/h5_xline.py` and the logs `h5_xline_gamma.json`, `h5_xline_sign.json`, `h5_xline_ann.json`, `h5_xline_factor.json`, and `h5_xline_p{11,13}_K16_all.json`. Each item is a way the argument can be misread, followed by the check that was actually made.

## 1. \(\gamma^*\) is not a bound on a line

The failure mode is to read the binary search as a theorem about \(X_{\mathrm{line}}\).

Proposition 1 encloses the smallest \(\gamma\) for which the greedy majorant of `proofs/h5_lines.md` Theorem 9 lies under the slack, and under the slack divided by \(M\). The binding absolute value is \(0.873735223878\), at \(p = 3307\). The binding times-\(M\) value is \(0.990856413416\), at the same prime. Both are properties of a list of primes and of the idealised slack. Section 7 says they are not achieved. The search agrees with `logs/h5_lines.json` to the digits stored there.

## 2. The two readings

The failure mode is to quote \(\gamma^*_{\mathrm{abs}}\) as enough for the reading that multiplies by the gas surplus, or to quote \(\gamma = 1/2\) as close enough.

A single exponent that fits both rooms in both readings has to clear \(\gamma^*_M\). The value \(\gamma = 1\) does. The value \(\gamma = 1/2\) misses both tight rooms; those sums are the ones already computed in the previous note. The absolute threshold is smaller because it does not divide the slack by \(M\).

## 3. The sign is \(+1\), and it does not see the line

The failure mode is to leave \(\varepsilon^{2p}\equiv \pm 1\) unresolved, or to treat the congruence as a property of cross lines only.

Theorem 2 gives \(\lambda^p-1 = 2 h_p\varepsilon^p\), so the sign is \(+1\) for every positive divisor of \(h_p\). The rational part of \(\lambda^p+1\) reduces to \(4y^2\), which is coprime to \(h_p\). The sign script checks the identity and \(h_p\equiv 1\pmod{2p}\) for every odd prime \(p\le 400\) and at the two conditional primes. Theorem 3 proves the congruence from the binomial theorem, without squarefreeness. The same congruence holds for a Binet ideal and for a cross ideal.

## 4. The Gauss sum recovers the line sum and stops

The failure mode is to read Theorem 6 as a factor \(\min(d, h/d)^{-\gamma}\).

The sum of \(\hat Z\) over the ideal equals \(h\) times the sum of those weights whose partial orbit \(\xi_n\) lands in the conjugate ideal. Dividing by \(Z_\rho\) is \(X_{\mathrm{line}}\). Substituting the character formula for the indicator of the conjugate ideal returns the same sum. Theorem 8 says this explicitly. The coefficient in \(X\) remains \(1\).

Lemma 4 identifies the local annihilator with the conjugate line. The finite check in `logs/h5_xline_ann.json` covers the prime factors at \(p\le 47\), exhaustively in one coordinate when the prime is at most \(5\cdot 10^6\). The prime \(h_{47}\) is the algebraic identity, not a full loop. The general step does not depend on that loop.

## 5. The model is a truncation

The failure mode is to call the line sum an exact value of \(\hat Z\), or to treat a Monte Carlo ratio from N7 as this sum.

The sums are the N6 transfer law at \(L = 8\), \(K = 16\), kick \(J_n(1.8)\), \(\rho = (2,8)\). Proposition 10 records the cross-line modulus at \(p = 11\) for \(K = 8, 12, 16\). The relative change from \(K = 8\) to \(K = 16\) is \(3.8\cdot 10^{-3}\). That is stability inside the model. It is not an enclosure of the tail in \(K\). The totals at \(p = 11\) and \(p = 13\), counting each isotropic class once, differ from the stored `f_iso` values by less than \(10^{-16}\). Orbits were reduced by \(\langle\lambda,-1\rangle\) only. The invariance gaps on the sample classes are at most \(1.9\cdot 10^{-11}\).

## 6. No counterexample on the computed set is not a theorem

The failure mode is to promote Proposition 11 to \(p\ge 1409\), or to quote the three-point least-squares exponent as a stable decay.

At \(p = 11\), \(13\) and \(17\), \(\lvert X_{\mathrm{line}}\rvert\cdot\min(d, h/d)\) equals \(1.830\cdot 10^{-4}\), \(3.761\cdot 10^{-3}\) and \(7.390\cdot 10^{-5}\). All three are less than \(1\), and so are the products against either threshold at \(C = 1\). A semiprime has one minimum for both cross lines, so an exponent in \(\min(d, h/d)\) is not visible inside one level. The pairwise slopes of \(\log\lvert X\rvert\) against \(\log\min\) are \(+1.44960079\) and \(-15.81306876\). The three-point least-squares slope is \(-0.65430938\). That formal exponent lies under both thresholds. The note does not use it as a bound: the pairwise slopes disagree, and the middle modulus is larger than both neighbours. The equality exponents \(3.74464912\), \(2.27776731\) and \(3.05249657\) stay above \(1\) on this set only.

## 7. The observed maximum does not save the triangle

The failure mode is to replace the summed line by \((h-1)\) times the largest computed ratio and still claim \(\gamma = 1\).

At \(p = 13\) that product is \(0.0912047\), and \(1/79 = 0.0126582\). At \(p = 17\) it is \(0.0325168\), and \(1/103 = 0.00970874\). The summed moduli are \(4.760\cdot 10^{-5}\) and \(7.175\cdot 10^{-7}\). The \(\ell^1\) mass times the minimum stays under \(1\) at the three computed primes. None of these is a bound at \(p = 3307\).

## 8. Closeness to an integer is not a long run

The failure mode is to read a count of steps within \(0.05\) of \(\mathbb Z\) as a violation, or a confirmation, of the run-length cap in `proofs/h5_lines.md`.

The count is not a consecutive block. The minimal distance on a primitive cross class is \(1.232\cdot 10^{-4}\) at \(p = 11\), \(2.113\cdot 10^{-5}\) at \(p = 13\) and \(6.221\cdot 10^{-7}\) at \(p = 17\), all smaller than \(1/\min\). That rules out a uniform gap of size \(1/\min\). It does not evaluate the cap.

## 9. Conjugate lines agreed; reversal was one class

The failure mode is to quote \(\hat Z(\bar\beta) = \hat Z(\beta)\) as a theorem because the two cross-line sums agreed.

At both computed primes the two cross lines, and the two Binet lines, agreed to the printed precision. One class at \(p = 11\) had \(Z(\bar\beta)\), \(Z(-\beta)\) and the reversed twist within \(10^{-13}\) of \(Z(\beta)\). Theorem 7 does not quotient by conjugation. The sums do not depend on the reversal identity.

## 10. The factorisation is flint, on \(p\le 199\), and it is not H6

The failure mode is to call the table an elementary trial division, or a proof that every \(h_p\) is squarefree, or to think a factor \(167\) makes the line short.

Proposition 13 checks that the factors returned by `python-flint` 0.9.0 multiply back to \(h_p\), are squarefree, and are all \(\equiv 1\pmod{2p}\), for every odd prime \(p\le 199\). The residue \(-1\) does not occur on this range. Lemma W still allows it. Primality of a 70-digit factor is flint's, not a hand division. The ideal of norm \(h_p\) has \(h_p\) classes even when one prime factor is small. The cross lines at \(p = 17\) were summed; the Binet lines at that prime were not, and there is no `f_iso` comparison there. The next uncomputed line, at \(p = 23\), has \(6919153\) orbits. At the measured \(0.11\) seconds per orbit that is not this run. No sample is entered as a line sum. K-convergence was checked only at \(p = 11\).

## 11. H5 is not discharged

The failure mode is to let a small value at \(p\le 17\), or a threshold \(\gamma^*<1\), stand in for the missing inequality.

Section 7 states that neither threshold is achieved. H5(b) stays open. H5(c), H5(a), H6 and infinitude of \(\{h_p\text{ prime}\}\) stay where the previous note left them. `record/claims.json` was not edited.
