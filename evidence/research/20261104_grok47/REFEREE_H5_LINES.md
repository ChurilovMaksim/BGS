# Self-referee of the cross-line note

Read against `proofs/h5_lines.md`, `code/h5_lines.py` and `logs/h5_lines.json`. Each item is a way the argument can be misread or can fail, followed by the check that was actually made.

## 1. The coefficient 1 is not a small factor

The failure mode is to read "Gauss-sum product" as a factor \(\min(d, h_p/d)^{-1}\) in front of a cross line.

Theorem 1 is the bookkeeping of N6 §1, N10 and N11b §1. On \(N\beta\equiv 0\) one has \(\kappa = n\), so the coefficient in \(X\) is \(1\). Corollary 2 counts \(h-1\) such terms on one line. TRACE-228, quoted as Theorem 3, multiplies frequencies of the form \(e\beta'\) with \(e>1\). A nonzero class in \(\mathfrak a/h\mathcal O\) is not of that form. The factor \(n_e/e^2\) remains attached to inherited lower conductors.

## 2. The conditional sum is not a bound on \(X_{\mathrm{line}}\)

The failure mode is to promote §6, where the sum at \(\gamma = 1\) fits both rooms, into a discharge of H5(b).

Section 6 opens by marking the per-line inequality as a hypothesis. Propositions 12, 13, 15 and 16 are comparisons of that hypothesis with the slack. The sentence that closes §6, and the sentence that closes the note, say that the hypothesis is not proved and that H5(b) stays open. The greedy lengths \(98\) and \(203\) still give \(2^{98}-2\) and \(2^{203}-2\) lines. Those counts exceed both rooms.

## 3. The two readings of "times the main term"

The failure mode is to quote the absolute fit of the elementary floor and omit the factor \(M\), or to quote the sharp fit and transfer it to the floor.

Proposition 12: on the greedy primes, both the sum and \(M\) times the sum lie under both tight slacks, at \(\gamma = 1\), \(C = 1\). Proposition 13: the progression floor and the \((p-1)j\) floor lie under both slacks absolutely, and \(M\) times either floor exceeds both tight slacks. The \((p-1)j\) clearance at \(p = 3307\) is under \(5\cdot 10^{-6}\). It is real at 80 decimal places. It is not a bound on a line, and it is not robust under multiplication by \(M\).

The binary search puts the times-\(M\) threshold on the greedy set at \(0.99085641\) for the fragile room. A value \(\gamma = 1/2\) misses both rooms on that set. The search is an enclosure of a root of a monotone function. It is not a theorem about \(\hat Z\).

## 4. The loose omega cap misses the fragile room at \(p = 3307\)

The failure mode is to pass from "the sum is \(O((\ln p)/p)\)" to "the fragile room is met at the conditional prime".

Proposition 15 records the loose sum \(0.00356995629\) at \(p = 3307\), above \(0.00334719\), and the majorant \(< 0.00892\) at \(p = 1409\), under \(0.02011297\). Proposition 16 scans every integer from \(3307\) to \(4599\). The sum increases \(137\) times. The last exceedance of the fragile cap is \(p = 3565\). From \(3566\) on, through the decreasing majorant of Theorem 14 past \(4600\), the loose sum lies under the cap. The first integers past \(3565\) clear the cap by less than \(10^{-6}\): at \(p = 3567\), recomputed at 50 decimal places, the gap is \(4.69455\cdot 10^{-7}\). That clearance is real and thin. It is not the gap at \(p = 4000\), where the sum has already fallen below \(0.00303430\). The range \(p\ge 3566\) does not include the conditional prime \(3307\). The fit at \(3307\) in Proposition 12 uses the greedy primes, whose product is bounded by \(h_p\), and it is conditional.

## 5. Lemma E at a composite modulus is not TRACE-268

The failure mode is to cite the registered prime-modulus lemma at \(h_p\), or to read Proposition 6 as a divisor saving.

Proposition 6 re-derives the constant from the first three steps of the proof in REPORT_L3.md, which do not use primality, and replaces the norm step. Lemma 5 is the integer comparison \(423^2 < 2\cdot 408^2\) and the fraction \(4000000/998001 < 201/50\). The resulting cap is \(k\le (p+1)/2\), with \(h_p\) and with no proper divisor in the bound. The Binet window is already of that order. The proposition is labelled as a statement of this note, not as TRACE-268.

Trace modulo \(h\) near an integer is not trace modulo \(q\mid h\) near an integer. The factor \(h/q\) sits between them.

## 6. The square root of 3

The failure mode is to use a rational upper bound for \(\sqrt 3\) as a lower bound.

Theorem 7 uses \(12^2 = 144 < 147 = 3\cdot 7^2\), so \(12/7 < \sqrt 3\). The mass is \(> (64/161) h_p\), and \(192 > 161\) gives \(> h_p/3\). The opposite comparison \(320 < 322\) says \(64/161 < 2/5\). That upper bound is recorded so that it cannot be reused as a lower bound. The \(\ell^1\) mass is a sum of absolute coefficients. It is not a lower bound on the signed sum \(|Y|\).

## 7. Squarefree hypotheses

The failure mode is to apply the product formula, the ideal of norm \(h\), or Theorem 9 when a square divides \(h_p\).

Corollary 2, Proposition 6, Theorems 7 and 9, and Lemma 10 state the squarefree hypothesis in the sentence that uses it. Theorem 1, the coefficient \(1\), does not need it: \(\kappa(0) = n_d\) for any odd level. N6 §6 is cited for the Ramanujan shell and is not improved. Squarefreeness remains H6.

The splitting \(q\equiv \pm 1\pmod 8\) used for the norm count is the identity \(h_m^2+1 = 2{y'}^2\), as in J3 §3. It is not Lemma W. Lemma W supplies \(q\equiv \pm 1\pmod{2p}\) and the omega cap.

## 8. \(|r|\le 1\) is not available

The failure mode is to majorise \(\hat Z/Z\) by \(1\), or by \((\Lambda_{\mathrm{free}}/\mu^*)^m\) with a silent prefactor.

Corollary 8 asks for \(\max|r| < 10^{-540}\) and \(< 10^{-1267}\) before the triangle majorant fits. TRACE-295 caps the free radius by \(1.9656353 > \mu^*\). The certificate carries a prefactor. This note does not evaluate that prefactor and does not claim \(|r|\le 1\).

The numerical smallness of cross lines at \(p\le 41\), in N7-F6 and in N8b, stays [N] there. It is not imported as a bound.

## 9. The slack is the idealised slot

The failure mode is to treat a fit inside the slack as a computation of the additive budget of v5.

The slack is Proposition 4 of `proofs/h5_factor.md`: \(n/h_p := 1\), the three \(\varepsilon\) terms at \(0\), and the model tail \(e^{-0.28p}\) put back in. The negative row at \(p = 1409\), \(\delta = 3.4962\cdot 10^{-4}\), is below the crossover and is not used as a room. A conditional fit in this slot would still not be the budget. The fit is not proved in any case.

## 10. Lines that intersect, and classes that were not summed

The failure mode is to multiply \((h-1)\) by \(2^\omega-2\) and call the product a lower bound on the support of \(X\).

Distinct ideals of norm \(h\) meet along the classes divisible by a rational prime. Corollary 2 bounds one line. It does not say the lines are disjoint, and it does not sum their triangle majorants into a lower bound. Theorem 7 bounds one mixed class. The remaining classes are more mass, not less.

## 11. What the note does not claim

H5(b) and H5(c) are not discharged. The composite branch of H5 is not discharged. The structural ceiling of v5 does not fall. \(\mathcal P\) is not proved infinite. H5(a) is not improved. Frozen R′ is untouched. `record/claims.json` was not edited.
