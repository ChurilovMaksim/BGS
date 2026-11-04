# Self-referee of the H7* / H8 note

Read against `proofs/h7_h8.md` and `logs/h7h8.json`. Each item is a way the argument can be misread or can fail, followed by the check that was actually made.

## 1. A finite factorisation is not a bound on Lin_d

The failure mode is to read Proposition 5 as a discharge of H7*, or as a sign computation for Dev_d.

Proposition 5 lists included \(K_p\)-divisors for nine primes. On \(p = 5, 7, 19, 29\), where \(h_p\) is prime, the list is exactly the H7* obligation coming from \(K_p\) inside the inclusion range \(d \le \sqrt{h_m}\), once level \(7\) is removed as the TRACE-223 case. The obligation is still open: the note gives no rate below \(T'\). The N17b Dev table stays **[N]** and was not replayed. Its loader path is not in this checkout.

At \(p = 11\) and \(p = 23\) the only included \(K_p\)-divisor is \(7\). Both \(h_p\) are composite. hp-div and mixed levels remain, so those two rows do not close H7*.

## 2. Inclusion is cited, and \(L_{\mathrm{fl}}\) may sit above \(\sqrt{h_m}\)

The sentence “these divisors are included” uses TRACE-273 as N17b states it: for \(\rho = (\pm 2, 8)\) and odd \(m \ge 15\), every \(d \mid h_m\) with \(d \le \sqrt{h_m}\) is included. That implication was not re-proved. A referee who does not grant TRACE-273 still has the factorisations, and does not have the non-vacuity sentence.

\(L_{\mathrm{fl}} = h_p^{1+o(1)}\) can exceed \(\sqrt{h_m}\) when \(\tau(h_m)\) is as large as the Nicolas–Robin bound. The cofactors at \(p = 11\) and \(p = 23\) lie above \(\sqrt{h_m}\) and might still lie under such an \(L_{\mathrm{fl}}\). The note does not evaluate \(L_{\mathrm{fl}}\) and does not claim those cofactors are outside H7*.

At \(p = 5\), \(31^2 = 961 > \sqrt{h_{15}}\). The draft mentions \(31^2 \mid K_5\) as an example of a prime power. The included prime power in the census is \(49\) at \(p = 7\). Treating \(31^2\) as an included level at \(m = 15\) would be a misreading of the cutoff. Treating it as irrelevant to every larger cutoff would also be a misreading.

## 3. Lemma E does not see the sign

Proposition 6 bounds the length of one close return. The product has \(3p\) factors and the return has length \(< 3p - (p + 7/4)\). A product can be large without containing a return of that length. The proposition blocks one route to a smallness certificate. It does not produce \(|\mathrm{Lin}_d| \le \varepsilon_d |Z_\rho|^2/h_p\), and it does not produce a negative Dev.

The constant \(7/4\) is the elementary margin at \(p = 5\), from \(\log_\lambda\Pi < 1/4\) and \((p-1)/2 \ge 2\). The arb check on the exact integers \(h_p, K_p\) is sharper (excess \(> 6.875\) at \(p = 5\)) and stops at \(p = 79\). The all-\(p\) statement is the elementary comparison, whose two integer asserts are in the script.

The float field `excess_over_run` in the log uses `math.log`. It is a survey. The certificate is the elementary proof together with the arb field `uniform_excess_spotcheck_ends`.

## 4. The two clocks

N14b’s length \(n = p - \log_\lambda d\) is the separation scale of the \(h_p\)-lattice, where \(h_p^2\) has size \(\lambda^p\). Proposition 6 counts factors in \(\prod_{j<m}\), and \(m = 3p\). Adding those lengths, or subtracting them, is not a step in the proof. The excess \(p + 7/4\) is entirely inside the product clock.

## 5. The floor comparison points the wrong way if the shape is dropped

Proposition 7 assumes the positive term is at most \(e^{0.05 p}\). The v5 gas is a lower bound. A lower bound lying under a floor is compatible with the true positive term lying above the floor. Dropping the shape hypothesis turns Proposition 7 into a false obstruction.

Inside the hypothesis, the obstruction is not uniform. At \(p = 19\), four included divisors beat \(e^{0.05\cdot 19}\) and six do not. The six have floors below the cap, several of them below \(1\) because \(d > h_p\). Those six are not obstructed by the floor comparison. They remain open because no rate \(< T'\) is known.

Level \(7\) beats the cap and is already covered by TRACE-223. Quoting the level-\(7\) floor as an open obstruction repeats a closed case. The first open prime power that beats the cap is \(49\) at \(p = 7\).

## 6. \(c_{\mathrm{del}}\) is the number the caps produce

\(\Lambda \le 1.9656353\) and \(r_2 \le 1.0529012\) are upper bounds. The exponent \(c_{\mathrm{del}} = (2\ln\Lambda_{\mathrm{cap}} - \ln r_{2,\mathrm{cap}})/\ln\lambda\) is what N14b’s ratio becomes when those caps are substituted. It is not a proved lower bound for a spectral radius, and \(\tfrac32 c_{\mathrm{del}} > 1\) is not a theorem about the true joint radius.

What it is: the first-moment sketch, if completed at these caps, delivers a factor \(d^{c_{\mathrm{del}}}\). Pushing that delivered factor through the extra power \(\tfrac32\) yields an exponent \(> 1.106 > 1\), which is strictly worse than the exponent \(1\) that N16b (c2) already charges for amplified weights. An argument that later produces a smaller exponent is outside this comparison.

Lemma 2 itself stays **[P-sketch]**. The Hölder step on the shortened window is N14b’s named gap. Proposition 8 does not close it and does not refute it.

## 7. Which normalisation of gap (a) the obstruction talks about

N16b (c1): unit weights give loss exponent \(0\), and H8 reduces to the H1 constant. N16b (c2): weights \(\asymp d/h\) give exponent \(1\). The note’s gap is a statement about (c2). A reading that exports the gap to every normalisation of the composite points is stronger than the proof. N8b’s weight \(A_c\) was not re-derived.

On prime \(h_p\), the draft already reduces H8 to H1, as a sketch. This note does not enter that reduction and does not attack H1.

## 8. The θ-gap is stable under the printed uncertainties, and not under an arbitrary improvement of \(\bar\rho\)

The direct comparison is \(\theta > 0.26223963\) against \(\theta < 0.16661157\) at \(\rho = 0.28\) and \(\ell_0 = p/4\). The balls are disjoint.

The margin, computed in the same script from those balls:

- Closing the gap at this \(\ell_0\) requires \(\rho\) at most the enclosure of centre \(0.22363877201179880126\). The certified upper bound is \(0.28\).
- Closing it by enlarging the mixed rate \(0.2945\) requires that rate to reach at least the enclosure of centre \(0.33354342307356709951\). Moving \(0.2945\) by one unit in the last place does not do this. The \(\pm 5\cdot 10^{-5}\) inflation is the direction that shrinks the first-moment range; it is not a second independent measurement of the rate.

A future certificate \(\bar\rho \le 0.22\) would remove this particular gap at \(\ell_0 = p/4\). The all-divisor length in Proposition 9 would shrink at the same time, and it would remain a positive multiple of \(p\) until \(\alpha(\rho)\) became large. The note does not claim the gap survives every improvement of \(\bar\rho\).

The draft’s figure \(0.28028\) gives a slightly smaller wrap threshold (\(\theta < 0.16618631\)). It is reported as a sensitivity check. The gap theorem uses \(\rho = 0.28\).

## 9. Rank \(3p\) and the stronger congruence are cited

Lemma 3 proves \(q \equiv 1 \pmod 3\). N8b’s congruence \(r \equiv 1 \pmod{6p}\) for \(r \mid K_p\), \(r \ne 7\), is a stronger statement about the order of \(\varepsilon\). It was not re-proved. The census is compatible with it and is not a proof of it.

TRACE-265’s rank-\(3p\) statement is cited. Proposition 6 does not use it. A flaw in the rank statement would not move the excess.

## 10. What the arithmetic does not touch

H1, H3, H5’s missing exponent \(c < 0.387\), H6, the background-interplay step in v5, and frozen R′ are unchanged. The conditional primes \(3307\) and \(1409\) were not recomputed. No row of `record/claims.json` was edited. The span-law note in this directory is a separate argument and is not an input to this one.
