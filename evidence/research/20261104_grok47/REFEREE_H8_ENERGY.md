# Self-referee of the H8 energy note

Read against `proofs/h8_energy.md` and `logs/h8_energy.json`. Each item is a way the argument can be misread or can fail, followed by the check that was actually made.

## 1. The energy is not the wrap exponent

The failure mode is to read \(J_2 \le 2L^2 - L\) as \(E_{H_d}|r|^2 \le (2/L)\,E|r|^2\), and then to declare the amplified exponent negative.

\(J_2\) counts additive quadruples in the graph of \(\langle\lambda\rangle\). N16b (c2) charges a factor \(d\) because the amplified weight sits outside \(\ell^3 \le \ell^2\). Proposition 5 keeps that factor at exponent \(1\). The formal substitution of \(d\cdot(2/L)\) for \(d\) is written out and is not a step in the proposition. At \(p = 1409\) and \(p = 3307\) that formal sum stays under \(0.170\), short of \(0.26223963\). At \(p = 19\) the same formal sum crosses \(0.26223963\). Quoting the \(p = 19\) crossing as a closure of the gap uses a prime below \(p_{\mathrm{thr}}\) and a substitution the note does not justify.

## 2. Equality at odd order is TRACE-279, counted

The failure mode is to present \(J_2 = 2L^2 - L\) as a new idea.

BGS-TRACE-279, Lemma N1.2(a), proves the uniqueness of the unordered pair for odd order, and states \(J_2 \le 2\tau^2 - \tau\). The equality at \(17\) levels is marked **[N]** there. Theorem 1 writes the count that turns the uniqueness into an equality, and credits that lemma. The even formula \(3L^2 - 3L\) is not in TRACE-279. Orders dividing \(3p\) are odd, and no \(\theta\) statement uses the even formula. The checks at \(73\) and \(89\) are finite identities for those two primes.

## 3. The composite bound is an inequality, and it needs equal orders

The failure mode is to export the equality to every \(d \mid h_p\) and every \(d \mid K_p\), or to claim \(J_2(d) = \prod J_2(q)\).

Theorem 2 is \(J_2(d) \le J_2(q)\) for one split prime \(q \mid d\) with the same order. Energy does not tensor under the Chinese remainder theorem in this note. At \(217 = 7\cdot 31\) the order equals the order modulo \(31\), and the energy equals \(435\). At \(49\) and \(343\) the order modulo \(7\) is \(3\), the order of the power is \(21\) and \(147\), and the energies \(1617\) and \(122451\) exceed \(2L^2 - L\). Treating \(49\) as covered by Theorem 2 is a misreading. At \(31^2\) the order stays \(15\) and the equality survives, so a square factor is not automatically outside.

An inert prime has no coordinate \(w\) with \(w^2 = 2\) in \(\mathbb F_q\). Theorem 1 does not apply to it. The census \(5 \le p \le 31\) finds every prime factor of \(K_p\) in the stored factorisation to be \(1\) or \(7 \pmod 8\). That is a finite check, not a proof that every later \(K_p\) splits.

## 4. Heath-Brown–Konyagin is not given a constant

The failure mode is to turn \(T_2 \ll L^{5/2}\) into a numeric character-sum bound and to compare it with \(0.16661157\).

The citation is Heath-Brown–Konyagin, Quart. J. Math. 51 (2000) 221–235, in the form of Konyagin's Theorem 2.2. The implied constant is not numeric here, and no numeric value is used. The graph count is the bound that enters Proposition 4. The shape \(q^{1/4}L^{3/8}\) is recorded only to show that a fixed implied constant cannot move a meeting point near \(0\) up to \(0.16661157\).

Bourgain–Glibichuk–Konyagin is not applied. The enclosure is the failure of \(|H| \ge q^\delta\): \(\delta_{\max}(1409) < 0.02017629\) and \(\delta_{\max}(3307) < 0.00947485\). N15b §2 already recorded this scale for the first-moment route.

## 5. The \((2,2)\) bound beats \(|S| \le L\) only below an explicit \(\theta\)

The failure mode is to read Proposition N1.3 as a saving on the whole gap.

\(|S|/L \le (2q/L^2)^{1/4}\) drops below \(1\) only for \(q < L^2/2\). For \(L = 3p\) the meeting point is under \(0.00644413\) at \(p = 1409\) and under \(0.00303834\) at \(p = 3307\). Both lie inside \(\theta < 0.16661157\). For \(p \le 23\) and \(L = 3p\) the meeting point can sit above \(0.16661157\). Those primes are below either conditional threshold of v5, and a character-sum saving is not the factor \(d\) of N16b (c2).

The mean of \(|S|^2\) is exactly \(L\). The small energy improves the fourth moment, down to a ratio \(< 2\), and that improvement is already spent in the \((2,2)\) bound.

## 6. Parking \(p = 19\) and \(p = 29\) does not delete H7*

The failure mode is to read the opening paragraph as a removal of H7* from v5.

Both primes lie under \(1409\) and under \(3307\). The aggregates stay undecided, as in `proofs/h7_average.md`. They are not an input the large-\(p\) inequality reads. H7* remains a hypothesis at \(p \ge p_{\mathrm{thr}}\), including on \(K_p\) levels. The theorem draft was not edited.

## 7. What would make the note false

- A proof that the positivity factor \(d\) is multiplied by \(J_2/L^3\).
- An extension of \(J_2 = 2L^2 - L\) to \(49\) or \(343\).
- A numeric implied constant for Heath-Brown–Konyagin used as if it were in the source.
- A claim that Bourgain–Glibichuk–Konyagin applies at \(|\langle\lambda\rangle| = 3p\) and \(\theta \ge 0.16661157\) for large \(p\).
- A claim that the covered wrap range is larger than \(\theta < 0.16661157\).
- A claim that H8, H7*, or v5 is discharged.

None of these is asserted. The script checks are exact integer counts and arb balls at precision \(200\). No floating-point energy is used as a bound.
