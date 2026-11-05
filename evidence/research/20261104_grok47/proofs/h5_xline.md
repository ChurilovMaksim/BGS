# The threshold \(\gamma^*\) and the sum on one cross line

Tags in this file are local to the note. **[P]** is proved here. **[P, finite]** is an exact integer check on an explicit finite set. **[P-arith]** is the idealised slack and the greedy divisor sum at 80 decimal places, the same arithmetic as `code/h5_lines.py`. **[N]** is a floating-point evaluation in the N6 Galerkin model and is not a bound. **[C]** is a comparison that assumes an inequality this note does not prove. `record/claims.json` was not edited.

## 0. What was asked, and what holds

The previous note isolated the missing inequality
\[
|X_{\mathrm{line}}(d)| \le C\,\min(d, h_p/d)^{-\gamma}
\]
as the hypothesis that would put the greedy divisor sum inside both idealised rooms. This note attacks that inequality. Three questions are separated.

The threshold \(\gamma^*\) is the smallest exponent at which the greedy sum of \(\min(d, h_p/d)^{-\gamma}\), with \(C = 1\), fits both rooms. It is an enclosure of a monotone function of the primes \(\equiv \pm 1\pmod{2p}\). It is not a bound on a line. In the absolute reading the binding value is \(0.873735223878\), at \(p = 3307\). In the reading multiplied by the gas surplus \(M\), the binding value is \(0.990856413416\), again at \(p = 3307\). Both sit under \(\gamma = 1\). The value \(\gamma = 1/2\) fits neither tight room.

The line sum was evaluated in the N6 model on every cross line at \(p = 11\), \(13\) and \(17\), and on the Binet lines at \(p = 11\) and \(13\). The Binet lines at \(p = 17\) were not summed. No computed cross line has \(|X_{\mathrm{line}}|\cdot\min(d, h/d) > 1\). That is not a counterexample to \(\gamma = 1\) on this set. It is [N], at \(K = 16\), and the enumeration stops at \(p = 17\). Every composite \(h_p\) with \(23\le p\le 199\) was factored and not summed.

The structural route does not produce the power. For every odd positive integer \(p\) and every divisor \(d\mid h_p\), one has \(\varepsilon^{2p}\equiv 1\pmod d\) in \(\mathbb Z[\sqrt 2]\), and not \(-1\). The sum of \(\hat Z\) over an ideal of norm \(h\) is \(h\) times the sum of the kick weights of those words whose partial orbit lands in the conjugate ideal. The factor \(\min(d, h/d)^{-\gamma}\) does not appear. The same congruence holds for every line, Binet or cross.

\(\gamma^*\) is not achieved. H5(b) stays open. The composite branch of H5 is not discharged.

## 1. The threshold

The rooms and the greedy majorant are those of `proofs/h5_lines.md` §6. With \(C = 1\),
\[
\sum_{\substack{d\mid h\\ d\ne 1,h}}\min(d, h/d)^{-\gamma} \le 2\Bigl(\prod_j(1+q_j^{-\gamma})-1\Bigr),
\]
and the product is largest, among admissible prime sets, for the shortest primes \(\equiv \pm 1\pmod{2p}\) whose product is still at most \(h_p\). The slack is the idealised quantity of Proposition 4 in `proofs/h5_factor.md`, recomputed here. \(M = 2(1+R)^p e^{-p\delta}-1\) with \(R = 6.234\cdot 10^{-4}\).

**Proposition 1 [P-arith].** On those greedy sets, eighty bisections at 80 decimal places give the smallest \(\gamma\in[0,2]\) for which the majorant lies under the slack, and under the slack divided by \(M\).

| \(p\) | \(\delta\) | \(\gamma\) absolute | \(\gamma\) times \(M\) | slack |
|---|---|---|---|---|
| \(1409\) | \(7.4115\cdot 10^{-6}\) | \(0.770781916705\) | \(0.895793310664\) | \(0.020112965593\) |
| \(3307\) | \(3.4962\cdot 10^{-4}\) | \(0.873735223878\) | \(0.990856413416\) | \(0.003347184752\) |

The full expansions are `logs/h5_xline_gamma.json`. They agree with the search recorded in `logs/h5_lines.json`.

**Definition.** The absolute threshold for both rooms is the larger absolute entry,
\[
\gamma^*_{\mathrm{abs}} = 0.873735223878,
\]
binding at \(p = 3307\). The threshold for both rooms after multiplication by \(M\) is
\[
\gamma^*_M = 0.990856413416,
\]
again binding at \(p = 3307\). A single exponent that meets both rooms in both readings has to clear \(\gamma^*_M\). The majorant decreases in \(\gamma\), so every larger exponent fits whenever these do. In particular \(\gamma = 1\) fits all four comparisons, and \(\gamma = 1/2\) fits none of the two tight rooms: the sums at \(\gamma = 1/2\) are \(0.47286885\) and \(0.42234330\), as in Proposition 12 of the previous note.

These four numbers are properties of the greedy prime list and of the slack. They become a statement about \(X_{\mathrm{line}}\) only if the per-line inequality is known at that \(\gamma\) and at \(C = 1\). It is not known. Squarefreeness of \(h_p\), which the majorant uses, remains H6.

## 2. The sign of \(\varepsilon^{2p}\)

Let \(\varepsilon = 1+\sqrt 2\) and \(\lambda = \varepsilon^2 = 3+2\sqrt 2\). Write \(\varepsilon^p = h + y\sqrt 2\) with \(h, y\in\mathbb Z\). For odd \(p\), the norm \(N(\varepsilon^p) = (-1)^p = -1\) gives \(h^2 - 2y^2 = -1\), and \(h = h_p\).

**Theorem 2 [P].** Let \(p\) be an odd positive integer and let \(d\) be a positive divisor of \(h_p\). Then, in \(\mathbb Z[\sqrt 2]\),
\[
\lambda^p - 1 = 2 h_p\,\varepsilon^p,
\]
so \(\varepsilon^{2p} = \lambda^p \equiv 1\pmod d\). The opposite sign does not hold: \(\lambda^p\not\equiv -1\pmod d\).

Expanding the square gives
\[
\lambda^p - 1 = (h+y\sqrt 2)^2 - 1 = h^2 + 2y^2 - 1 + 2hy\sqrt 2.
\]
The norm replaces \(2y^2\) by \(h^2+1\), and the rational part collapses to \(2h^2\). Factoring out \(2h\) leaves \(\varepsilon^p\). Every \(d\mid h_p\) therefore divides \(\lambda^p-1\) in \(\mathbb Z[\sqrt 2]\).

For the other sign the same expansion gives
\[
\lambda^p + 1 = 2y(2y + h\sqrt 2).
\]
Reducing modulo \(h\), the coefficient of \(\sqrt 2\) vanishes and the rational coefficient is \(4y^2\). The norm \(h^2-2y^2 = -1\) forces \(\gcd(h, y) = 1\), and \(h\) is odd, so \(4y^2\) is coprime to \(h\) and to every divisor of \(h\). Thus \(\lambda^p+1\not\in d\,\mathbb Z[\sqrt 2]\).

**Proposition 3 [P, finite].** The three boolean checks in Theorem 2 — the norm, the factorisation of \(\lambda^p-1\), and \(4y^2\not\equiv 0\pmod{h_p}\) — and the congruence of Theorem 3 hold for every odd prime \(p\le 400\) and at \(p\in\{1409, 3307\}\). The script is `code/h5_xline.py sign`. The identities are the general ones, so the finite check is a guard against an indexing error, not the proof.

The congruence is modulo \(h_p\), hence modulo every proper divisor. It does not depend on a sign pattern. A Binet line and a cross line satisfy the same relation.

**Theorem 3 [P].** For every odd prime \(p\), \(h_p\equiv 1\pmod{2p}\).

The binomial theorem in \(\mathbb Z[\sqrt 2]\) gives \((1+\sqrt 2)^p\equiv 1+(\sqrt 2)^p\pmod p\), because \(p\) divides \(\binom{p}{k}\) for \(0<k<p\). The remaining term is \((\sqrt 2)^p = 2^{(p-1)/2}\sqrt 2\), so the rational coefficient \(h_p\) is congruent to \(1\) modulo \(p\). The norm \(h_p^2-2y^2 = -1\) forces \(h_p\) odd, hence \(h_p\equiv 1\pmod 2\). Since \(2\) and \(p\) are coprime, \(h_p\equiv 1\pmod{2p}\).

The same congruence is part of the finite guard in Proposition 3. The proof does not use that guard, and it does not use squarefreeness.

## 3. The Gauss sum on the line

Let \(\mathcal O = \mathbb Z[\sqrt 2]\) and let \(h\) be odd and squarefree, with every prime factor split. An ideal \(\mathfrak a\) of norm \(h\) which takes one prime ideal above each rational prime satisfies \((\mathfrak a)(\bar{\mathfrak a}) = (h)\) and \(\mathfrak a+\bar{\mathfrak a} = \mathcal O\). The line is the additive group \(\mathfrak a/h\mathcal O\), of order \(h\).

The twisted sum, in the exact series or in any model with the same phase linearity, has the shape
\[
\hat Z(\beta) = \sum_n w(n)\,e\bigl(\operatorname{Tr}(\beta\,\xi_n)/h\bigr), \qquad \xi_n = \sum_{i<m} n_i\lambda^i,
\]
with weights \(w(n)\) independent of \(\beta\). The N6 transfer law is of this shape: each time step multiplies by \(e(n\tau)\) and the final scalar is a trace, so the Galerkin value \(Z_K\) is the same formula with weights \(w_K\) that still do not depend on the twist. The identity below is exact for \(Z_K\). It does not estimate \(Z_K-\hat Z\).

**Lemma 4 [P].** Let \(q\) be an odd prime, \(w^2\equiv 2\pmod q\), and let \(L_s = \{(x,y): x\equiv swy\pmod q\}\) for \(s = \pm 1\). The \(\mathbb Z\)-trace form \(\operatorname{Tr}(\mu\beta)\equiv 0\pmod q\) for every \(\beta\in L_s\) if and only if \(\mu\in L_{-s}\).

A class \(\beta = y(sw+\sqrt 2)\) and a class \(\mu = u+v\sqrt 2\) have
\[
\operatorname{Tr}(\mu\beta) = 2y(swu+2v).
\]
The form vanishes for every \(y\) precisely when \(v\equiv -swu\cdot 2^{-1}\pmod q\). That line is \(L_{-s}\): substituting \(u\equiv -swv\) recovers the equation, the two coefficients \((sw, 2)\) are not both zero, and both sets have \(q\) points.

**Proposition 5 [P, finite].** For every prime factor of \(h_p\) at an odd prime \(p\le 47\), the square root of \(2\) used above squares to \(2\), the form is nondegenerate, and every checked point of \(L_{-s}\) lies in the kernel. The check is exhaustive in the coordinate \(v\) when \(q\le 5\cdot 10^6\), which covers every such factor except the prime \(h_{47}\). The log is `logs/h5_xline_ann.json`, twenty-five primes. The general step is Lemma 4.

**Theorem 6 [P].** For \(h\) and \(\mathfrak a\) as above,
\[
\sum_{\beta\in\mathfrak a/h\mathcal O}\hat Z(\beta) = h\sum_{n:\,\xi_n\in\bar{\mathfrak a}} w(n).
\]
The sum over the nonzero classes is \(h\,W(\bar{\mathfrak a}) - \hat Z(0)\), where \(W(\bar{\mathfrak a})\) is the inner sum of weights and \(\hat Z(0) = \sum_n w(n)\).

The inner sum over the additive group \(K = \mathfrak a/h\mathcal O\) of the character \(\beta\mapsto e(\operatorname{Tr}(\beta\xi)/h)\) equals \(|K| = h\) when the character is trivial, and equals \(0\) otherwise. It is trivial precisely when \(\operatorname{Tr}(\xi\mathfrak a)\subset h\mathbb Z\). By the Chinese remainder theorem, \(\mathfrak a/h\mathcal O\) is the set of classes whose reduction modulo each \(q\mid h\) lies on the chosen local line \(L_{s_q}\), and a trace integer vanishes modulo \(h\) if and only if it vanishes modulo every such \(q\). Lemma 4 at each \(q\), with the sign flipped, says that this is the condition of lying on \(\bar{\mathfrak a}\).

**Theorem 7 [P].** Let \(p\) be an odd prime and let every prime factor of the squarefree integer \(h\mid h_p\) have multiplicative order \(p\) for \(\lambda\), which holds for the prime factors of \(h_p\) by Theorem 2. The group \(\langle\lambda, -1\rangle\) acts freely on the nonzero classes of any ideal of norm \(h\) in \(\mathcal O/h\mathcal O\). The group has order \(2p\), and the nonzero classes fall into \((h-1)/(2p)\) orbits.

Theorem 2 gives \(\lambda^p\equiv 1\) in \(\mathcal O/q\mathcal O\). The multiplicative order of \(\lambda\) in each residue field divides \(p\), and it is not \(1\): \(\lambda-1 = 2\varepsilon\) has norm \(-4\), so no odd prime ideal divides \(\lambda-1\). Thus the order is exactly \(p\). The quotient \(\mathcal O/\bar{\mathfrak a}\) is a product of these fields. A group element \(s\lambda^k\), with \(s = \pm 1\), fixes a class only if \(s\lambda^k = 1\) in every component where the class is nonzero. That forces \(\lambda^k = s\). The case \(s = 1\) forces \(p\mid k\). The case \(s = -1\) forces \(\lambda^k = -1\), hence \(p\mid 2k\) and not \(p\mid k\), which is impossible for odd \(p\). Every nonzero class has a nonzero component, so the stabiliser is trivial.

The numerical sums use this group and no further quotient. Conjugation swaps a line with the line of the complementary divisor and is not divided out.

## 4. What the evaluation does not give

**Theorem 8 [P].** The identity in Theorem 6 does not contain a factor \(\min(d, h/d)^{-\gamma}\).

The right-hand side is \(h\) times a subsum of the weights that already define \(\hat Z\). Dividing by \(Z_\rho\) produces \(X_{\mathrm{line}}\). Inserting the character formula for the indicator of \(\bar{\mathfrak a}\) returns the same sum over the line. There is no second closed form.

The orbit relation of Theorem 2 is identical for every ideal of norm \(h_p\). It constrains the period of \(\lambda^i\bmod h_p\). It does not see which local signs define the ideal, so it does not separate a cross line from a Binet line.

The coefficient in \(X\) remains \(1\), by Theorem 1 of `proofs/h5_lines.md`. Theorem 6 moves that coefficient onto a thin set of words. It does not divide it by the smaller part of a divisor pair.

## 5. The sums that were computed

The model is the twisted transfer law of `computations/verification/lineL/L2/code/twlaw.py`, batched as in `computations/verification/lineN6/code/twb.py`. The kick is \(i^n J_n(1.8)\), the length cutoff is \(L = 8\), the frozen frequency is \(\rho = (2, 8)\), and \(m = 3p\). The state denominator is \(b = 8\), so the automaton has \(S = 64\) states. The headline truncation is \(K = 16\), the truncation used for the stored isotropic sums. This is [N]. It is not an interval enclosure of \(\hat Z\).

A line is indexed by the product \(d\) of those prime factors at which its sign pattern disagrees with the Binet element \(\gamma = x_{(p+1)/2} + y_{(p-1)/2}\sqrt 2\). Then \(d = 1\) and \(d = h_p\) are the two Binet lines, and every other squarefree \(d\mid h_p\) is a cross line. For a semiprime both cross lines have the same value \(\min(d, h_p/d) = \min(q, h_p/q)\).

\(X_{\mathrm{line}}\) is the sum of \(Z_K(\beta)/Z_K(\rho)\) over the \(h-1\) nonzero classes. The primitive part drops the classes divisible by a rational prime. Those classes lie on more than one ideal; the line sum keeps them, and the comparison with the stored total counts each isotropic class once.

**Proposition 9 [N].** At \(K = 16\), with orbit sums under \(\langle\lambda, -1\rangle\), the cross lines and the Binet lines are as follows. The gap against `computations/verification/lineN6/logs/f_iso_p{11,13}_K16_s1.json` is the modulus of the difference of the two complex totals.

| \(p\) | \(h_p\) | line | \(\min(d, h/d)\) | \(\lvert X_{\mathrm{line}}\rvert\) | \(\lvert X\rvert\cdot\min\) | \(\ell^1\) | \(\max\lvert Z/Z_\rho\rvert\) |
|---|---|---|---|---|---|---|---|
| \(11\) | \(23\cdot 353\) | cross | \(23\) | \(7.95805726\cdot 10^{-6}\) | \(1.83035317\cdot 10^{-4}\) | \(2.28431349\cdot 10^{-5}\) | \(2.24441271\cdot 10^{-7}\) |
| \(11\) | | Binet | — | \(9.21482905\cdot 10^{-3}\) | — | \(9.48313183\cdot 10^{-3}\) | \(3.95580561\cdot 10^{-4}\) |
| \(13\) | \(79\cdot 599\) | cross | \(79\) | \(4.76043945\cdot 10^{-5}\) | \(3.76074717\cdot 10^{-3}\) | \(7.67023026\cdot 10^{-5}\) | \(1.92740371\cdot 10^{-6}\) |
| \(13\) | | Binet | — | \(1.08946442\cdot 10^{-2}\) | — | \(1.121059\cdot 10^{-2}\) | \(3.95454109\cdot 10^{-4}\) |
| \(17\) | \(103\cdot 15607\) | cross | \(103\) | \(7.17498975\cdot 10^{-7}\) | \(7.39023944\cdot 10^{-5}\) | \(1.06300672\cdot 10^{-6}\) | \(2.02279546\cdot 10^{-8}\) |

The two cross lines at a given \(p\) agree to the last printed digit, and so do the two Binet lines at \(p = 11\) and \(p = 13\). The Binet lines at \(p = 17\) were not computed, and there is no stored full isotropic total at that prime in this checkout, so Proposition 9 has no `f_iso` gap at \(p = 17\). The gaps against the stored totals are \(9.8\cdot 10^{-18}\) at \(p = 11\) and \(2.0\cdot 10^{-17}\) at \(p = 13\). On four sample classes per line, \(\lvert Z(\lambda\beta)-Z(\beta)\rvert\) and \(\lvert Z(-\beta)-Z(\beta)\rvert\) are at most \(1.9\cdot 10^{-11}\). One off-sample class at \(p = 11\) has the same agreement for the conjugate class and for the reversed twist, at \(10^{-13}\). That reversal check is one class. It is not a proof that \(\hat Z(\bar\beta) = \hat Z(\beta)\) in general; Theorem 7 does not claim it. The line sums do not depend on it, because conjugation was not quotiented out.

The primitive part of a cross line differs from the full line by less than \(3\cdot 10^{-7}\) at \(p = 11\), by less than \(3\cdot 10^{-9}\) at \(p = 13\), and by less than \(2\cdot 10^{-8}\) at \(p = 17\). The axis classes are not the mass of the cross line. At \(p = 17\) the invariance gap on the sample classes is \(4.9\cdot 10^{-15}\).

**Proposition 10 [N].** At \(p = 11\) the cross-line modulus at three truncations is \(7.927586\cdot 10^{-6}\) for \(K = 8\), \(7.954796\cdot 10^{-6}\) for \(K = 12\), and \(7.958057\cdot 10^{-6}\) for \(K = 16\). The relative change from \(K = 8\) to \(K = 16\) is \(3.8\cdot 10^{-3}\). The same change for a Binet line is \(4.0\cdot 10^{-4}\). The gap between \(7.96\cdot 10^{-6}\) and \(1/23\) is not a truncation effect at this level.

**Proposition 11 [N].** No cross line in Proposition 9 satisfies \(\lvert X_{\mathrm{line}}\rvert > \min(d, h/d)^{-1}\). The products are \(1.830\cdot 10^{-4}\), \(3.761\cdot 10^{-3}\) and \(7.390\cdot 10^{-5}\). The same products against \(\min^{-\gamma^*_{\mathrm{abs}}}\) and against \(\min^{-\gamma^*_M}\) are \(1.232\cdot 10^{-4}\) and \(1.779\cdot 10^{-4}\) at \(p = 11\), \(2.166\cdot 10^{-3}\) and \(3.613\cdot 10^{-3}\) at \(p = 13\), and \(4.116\cdot 10^{-5}\) and \(7.084\cdot 10^{-5}\) at \(p = 17\). None exceeds \(1\). There is no counterexample to \(\gamma = 1\), or to either threshold at \(C = 1\), in this set.

The triangle of the observed maximum does not inherit that conclusion. At \(p = 13\),
\[
(h-1)\max\lvert Z/Z_\rho\rvert = 47320\cdot 1.92740371\cdot 10^{-6} = 0.0912047,
\]
while \(1/79 = 0.0126582\). At \(p = 17\) the same product is \(1607520\cdot 2.02279546\cdot 10^{-8} = 0.0325168\), and \(1/103 = 0.00970874\). The observed maximum, multiplied by the length of the line, exceeds \(\min^{-1}\) at both primes. The summed line lies under \(\min^{-1}\) because most classes are smaller than the maximum and the sum is not the \(\ell^1\) mass. The \(\ell^1\) masses themselves, times the minimum, are \(5.254\cdot 10^{-4}\) at \(p = 11\), \(6.059\cdot 10^{-3}\) at \(p = 13\) and \(1.095\cdot 10^{-4}\) at \(p = 17\), still under \(1\).

**Proposition 12 [N].** The equality exponent of a cross line is \(-\log\lvert X_{\mathrm{line}}\rvert/\log\min(d, h/d)\). It equals \(3.74464912\) at \(p = 11\), \(2.27776731\) at \(p = 13\) and \(3.05249657\) at \(p = 17\). Each of these semiprimes has one minimum for both cross lines, so a power of \(\min(d, h/d)\) is not visible inside one level. The slope of \(\log\lvert X_{\mathrm{line}}\rvert\) against \(\log\min\) is \(+1.44960079\) from \(p = 11\) to \(p = 13\), and \(-15.81306876\) from \(p = 13\) to \(p = 17\). The ordinary least-squares slope through the three points is \(-0.65430938\), which would be an empirical exponent \(0.65430938\).

That least-squares number sits under both thresholds of Proposition 1. It is not a description of the three points: the two pairwise slopes differ by an order of magnitude, and the middle modulus is larger than both neighbours. The direct test in Proposition 11 has no counterexample. The fit does not support a single decaying power of \(\min(d, h/d)\), and it does not produce a value of \(\gamma\) that can be used at \(p\ge 1409\).

The closest twist on a primitive cross class comes within \(1.232\cdot 10^{-4}\) of an integer at \(p = 11\), within \(2.113\cdot 10^{-5}\) at \(p = 13\), and within \(6.221\cdot 10^{-7}\) at \(p = 17\). All three distances are smaller than \(1/\min\). The count of steps lying within \(0.05\) of an integer reaches \(15\), \(21\) and \(27\), out of \(m = 3p\). That count is not a consecutive run, and it is not a test of the run-length cap in `proofs/h5_lines.md`. It does show that a cross line is not kept at a distance \(1/\min\) from \(\mathbb Z\).

The ratio of a cross line to one Binet line is \(8.64\cdot 10^{-4}\) at \(p = 11\) and \(4.37\cdot 10^{-3}\) at \(p = 13\). There is no Binet sum at \(p = 17\).

## 6. How far the enumeration goes

**Proposition 13 [P, finite].** For every odd prime \(p\le 199\), `python-flint` 0.9.0 factored \(h_p\) completely inside a 25-second budget per cofactor, after trial division by the primes up to \(2\cdot 10^6\). The budget never fired. Exact multiplication of the returned factors recovers \(h_p\), every exponent is \(1\), and every prime factor \(q\) satisfies \(q\equiv 1\pmod{2p}\) and \(q\ge 2p-1\). On this range the residue is \(1\), not \(-1\); Lemma W allows both. Eight values are prime, \(p\in\{3,5,7,19,29,47,59,163\}\). The other thirty-seven are composite, with \(\omega\le 6\). The table through \(p = 47\) matches Proposition 6 of `proofs/h5_factor.md`. The log is `logs/h5_xline_factor.json`. Primality of the large prime factors is the flint factorisation. The product check is integer arithmetic. Squarefreeness on \(p\le 199\) is not H6.

A small prime factor does not shorten the line. The ideal has norm \(h_p\), so the line still has \(h_p\) classes. At \(p = 83\) the least factor is \(167\), and one line still has \((h_{83}-1)/166\) orbits.

**Proposition 14 [N].** On each squarefree level the number of orbits on one line is \((h_p-1)/(2p)\), by Theorem 7. The quotient is an integer for every odd prime by Theorem 3, whether or not \(h_p\) is squarefree. At the measured cost of about \(0.11\) seconds per orbit at \(m = 51\) and \(K = 16\), the levels past \(p = 17\) are:

| \(p\) | \(h_p\) | orbits on one line | decision |
|---|---|---|---|
| \(11\) | \(8119\) | \(369\) | computed, four lines |
| \(13\) | \(47321\) | \(1820\) | computed, four lines |
| \(17\) | \(1607521\) | \(47280\) | two cross lines computed, about \(1.06\cdot 10^4\) s together; Binet lines not computed |
| \(23\) | \(47\cdot 6771937\) | \(6919153\) | not computed; about \(7.6\cdot 10^5\) seconds at \(0.11\) s per orbit |
| \(31\) | \(424577\cdot 865087\) | \(5924129729\) | not computed |

\(h_p\) increases with \(p\). No composite level between \(19\) and the factorisation limit has a smaller line than \(h_{17}\). A complete sum at every composite \(h_p\) with \(p\le 200\) was not run, and the orbit count forbids it in this model. Samples are not recorded as line sums. A partial sum cannot certify a counterexample, because later classes can cancel it, and it cannot certify the inequality either.

The \(p = 17\) block of Proposition 9 is the log `logs/h5_xline_p17_K16_cross.json`. Both cross lines are in that file. No intermediate checkpoint is kept.

## 7. Whether \(\gamma^*\) is achieved

**Statement.** \(\gamma^*_{\mathrm{abs}}\) and \(\gamma^*_M\) are not achieved.

Achieved would mean a proved inequality \(\lvert X_{\mathrm{line}}(d)\rvert\le C\min(d, h_p/d)^{-\gamma}\) with \(\gamma\) at least the corresponding threshold and with \(C\) small enough that the greedy sum still fits both rooms. For \(C = 1\) the thresholds of Proposition 1 are exactly those values. No such inequality is proved.

Theorem 6 is the Gauss-sum evaluation asked for. Theorem 8 records that it does not supply the power. Theorem 2 records the sign, and it is the same sign on every line. The numerical products in Proposition 11 lie under \(1\) at \(p = 11\), \(13\) and \(17\). They are values of one Galerkin model at three semiprimes. The three-point least-squares exponent in Proposition 12 is \(0.65430938\), below both thresholds, and the pairwise slopes \(+1.45\) and \(-15.8\) show that the line is not a fit. Neither number is evidence that a positive \(\gamma^*\) persists up to \(p = 3307\).

The conditional arithmetic of `proofs/h5_lines.md` §6 is unchanged. If the missing inequality were known at \(\gamma = 1\) and \(C = 1\), the greedy sum would fit both rooms, absolutely and times \(M\). The inequality is the open step. H5(b) stays open. H5(c) is not treated again; the product weight and the \(\ell^1\) mass \(> h_p/3\) remain as in that note. H5(a), H6, and infinitude of \(\{h_p\text{ prime}\}\) remain open. The idealised slack is not the additive budget of v5. Frozen R′ is untouched. `record/claims.json` was not edited.
