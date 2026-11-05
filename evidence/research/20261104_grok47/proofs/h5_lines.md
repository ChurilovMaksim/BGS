# H5(b) and H5(c): the coefficient on a cross line is 1

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[P, finite]** is an exact integer comparison, including a complete sieve of one arithmetic progression up to an explicit bound. **[P-arith]** is the idealised gas-versus-Robin arithmetic at 80 decimal places, the same inputs as `code/h5_factor.py`, together with the divisor sums enclosed at that precision. **[C]** is conditional on an inequality that this note does not prove. **[N]** is not used for a bound. `record/claims.json` was not edited.

## 0. What was asked, and what holds

H5(b) asks for a bound, inside the budget of v5, on the \(2^{\omega(h_p)}-2\) fully isotropic lines at composite \(h_p\) other than the two lines coded by the gas. The attack tested here is the bound
\[
|X_{\mathrm{line}}(d)| \le C\,\min(d, h_p/d)^{-\gamma}
\]
for a proper divisor \(d\), some \(C\), and some \(\gamma>0\), either absolutely or multiplied by the gas surplus
\[
M = 2(1+R)^p e^{-p\delta}-1, \qquad R = 6.234\cdot 10^{-4}.
\]
The proposed source of the negative power is the Gauss-sum product (TRACE-228, TRACE-229) together with Lemma W.

That source does not produce the power. In the normalisation of N6 §1, N10 and N11b §1, every fully isotropic point enters \(X\) with coefficient \(1\), on a Binet line and on a cross line alike. TRACE-228 multiplies an inherited frequency \(\beta = e\beta'\), \(e>1\). A point of a cross line at conductor \(h_p\) is not of that form. Lemma W constrains the prime factors. It does not divide the coefficient.

What is proved instead is a triangle majorant. One cross line contains \(h_p-1\) points of coefficient \(1\). At the conditional primes, \(h_{1409} > 10^{539}\) and \(h_{3307} > 10^{1265}\). The idealised rooms are \(< 0.02011297\) and \(< 0.00334719\) (Proposition 4 of `proofs/h5_factor.md`). The triangle majorant fits in either room only if \(\max|r| < 10^{-540}\) or \(< 10^{-1267}\). No such bound on \(\hat Z/Z\) is proved. The free-family radius of TRACE-295 lies above \(\mu^*\).

The same holds for H5(c). A partially isotropic point does carry the product weight of Lemma 1 in `proofs/h7_lin.md`, at most \(2/(q-2)\) when a single prime is non-isotropic. Summing the absolute weights over one mixed class restores a mass \(> h_p/3\). The triangle majorant is again larger than either room by a factor \(h_p\).

Section 6 records the divisor arithmetic that would follow if the missing per-line bound were known. On the sharp list of primes \(\equiv \pm 1\pmod{2p}\), the sum at \(\gamma = 1\) and \(C = 1\) lies under both rooms, absolutely and after multiplication by \(M\). The elementary floors from Lemma W lie under both rooms absolutely and miss both rooms after multiplication by \(M\). None of these comparisons is a bound on \(X_{\mathrm{line}}\).

H5(b) and H5(c) stay open. The composite branch of H5 is not discharged. The structural ceiling of v5 does not fall. Primality of \(h_p\) is not used, and it is not removed from the closure.

## 1. The coefficient

The level-\(d\) member sums are those of N6 §1. For \(t\) in the member set \(S_d\),
\[
Z_t = \frac{G_d(t)}{d^2}\sum_\beta e(\bar t\, N\beta/d)\,\hat Z(\beta),
\]
with \(|G_d(t)|^2 = d^2\) on members (TRACE-212). The linear form is
\[
\mathrm{Lin}_d = \frac{2}{d^2}\operatorname{Re}\Bigl(\overline{Z_\rho}\sum_{\beta\not\equiv 0}\kappa_d(N\beta)\,\hat Z(\beta)\Bigr),
\]
where \(\kappa_d(u) = \sum_{t\in S_d} e(\bar t\, u/d)\). If \(N\beta \equiv 0\pmod d\), then \(\kappa_d(N\beta) = n_d = |S_d|\).

**Theorem 1 [P, bookkeeping from N6 §1, N10 and N11b §1].** The Cauchy–Schwarz form
\[
\mathrm{Dev}_d \ge \frac{n_d\,|Z_\rho|^2}{d^2}\bigl(|1+X+Y|^2 - 1\bigr)
\]
holds with
\[
X = \sum_{\substack{N\beta\equiv 0\\ \beta\not\equiv 0}} \frac{\hat Z(\beta)}{Z_\rho}, \qquad
Y = \frac{1}{n_d}\sum_{N\beta\not\equiv 0}\kappa_d(N\beta)\,\frac{\hat Z(\beta)}{Z_\rho}.
\]
Every fully isotropic point, and no other point, has coefficient \(1\) in \(X\).

The linear piece of \(|1+X+Y|^2-1\) is \(2\operatorname{Re}(X+Y)\). Multiplying by \(n_d|Z|^2/d^2\) reproduces \(\mathrm{Lin}_d\), because \(\kappa_d = n_d\) on the isotropic support and \(\operatorname{Re}(\overline{Z}\,\hat Z) = |Z|^2\operatorname{Re}(\hat Z/Z)\). The square \(|X+Y|^2\) is what Cauchy–Schwarz keeps and the linear form drops. N10 records the resulting inequality. N11b §1 records the split between \(\kappa(0)/n_d = 1\) and the non-isotropic weights \(\kappa/n_d\).

**Corollary 2 [P].** At a squarefree composite level \(h\), each of the \(2^{\omega(h)}\) ideals of norm \(h\) determines a line \(\mathfrak a/h\mathcal O\) with \(h\) residue classes. The nonzero classes are fully isotropic, and each enters \(X\) with coefficient \(1\). A cross line is any such line other than the two Binet lines \((\gamma)\) and \((\bar\gamma)\). Its contribution is
\[
X_{\mathrm{line}} = \sum_{\beta\in \mathfrak a/h\mathcal O,\;\beta\not\equiv 0}\frac{\hat Z(\beta)}{Z_\rho},
\]
a sum of \(h-1\) terms of coefficient \(1\). Identity (I) and Lemma P′ do not apply to it (N7-F6). The common factor \(n_h\) sits outside \(X\), in the prefactor of Theorem 1.

The count \(h\) is the index: \(|\mathcal O/h\mathcal O| = h^2\) and \(|\mathcal O/\mathfrak a| = N(\mathfrak a) = h\), so \(|\mathfrak a/h\mathcal O| = h\).

## 2. TRACE-228 does not supply \(\min(d, h/d)^{-\gamma}\)

**Theorem 3 [P, cited TRACE-228].** Let \(c, e\) be coprime odd positive integers, \(d = ce\), and \(\beta = e\beta'\) with \(\beta'\in\mathcal O/c\). Then \(\hat Z^{(d)}_\beta = \hat Z^{(c)}_{\beta'}\) and \(W_{d,\beta} = (n_e/e^2)\, W_{c,\beta'}\).

The identity is the inheritance theorem in `mathematics/fixed-map/lineJ_d7_twisted_coefficient.md` §6. The factor \(n_e/e^2\) is the weight of a whole lower-level sum, copied onto the frequencies divisible by \(e\).

A nonzero point of a cross line at conductor \(h\) lies in an ideal of norm \(h\) and is nonzero in \(\mathcal O/h\mathcal O\). It is not divisible by an integer \(e>1\). Theorem 3 does not apply to it, and it does not insert a factor \(1/e\).

The shape \(n_e/e^2 \asymp 1/\min(d, h/d)\) is real for inherited copies of a lower conductor. Those copies are not the cross lines in \(X\). N7-F6 records that each cross line carries the full weight \(n_d\). The ratios \(0.0014\) and \(0.0009\) at \(p = 11\) in that note are [N]. They are not a bound at \(p\ge 1409\).

## 3. The product formula is the weight in \(Y\)

**Theorem 4 [P, cited].** Let \(d = \prod q\) be a product of distinct primes \(q\parallel h_m\). Then \(\kappa_d\) is the product of the local missing-label sums: \(\kappa_q(0) = q-2\) and \(|\kappa_q(v)| = 2|\cos(\pi k/q)|\) for \(v\not\equiv 0\). In particular, if \(N\beta\equiv 0\) at every prime dividing an integer \(e\mid d\) and \(N\beta\not\equiv 0\) at every prime dividing \(d/e\), then
\[
\Bigl|\frac{\kappa_d(N\beta)}{n_d}\Bigr| \le \prod_{q\mid (d/e)}\frac{2}{q-2}.
\]

The product is Lemma 1 of `proofs/h7_lin.md`. The local formula is TRACE-229. The quotient by \(n_d = \prod(q-2)\) cancels the isotropic factors and leaves the displayed product. For a single non-isotropic prime this is at most \(2/(q-2)\).

This is a bound on a coefficient in \(Y\), not on a coefficient in \(X\). It is the input to H5(c) and to the mixed classes of H5(a). It is not a bound on \(X_{\mathrm{line}}\).

Every odd prime \(q\mid h_p\) splits in \(\mathbb Z[\sqrt 2]\). Indeed \(h_m^2 + 1 = 2{y'}^2\), so \(q\mid h_m\) gives \(2{y'}^2\equiv 1\pmod q\). Thus \(y'\) is a unit and \(2\) is a square modulo \(q\), hence \(q\equiv \pm 1\pmod 8\). This is the observation recorded in J3 §3 and in line K, Theorem K1. Consequently \(\mathcal O/q\mathcal O\cong\mathbb F_q\times\mathbb F_q\) and the norm is the product of the coordinates. For \(u\not\equiv 0\) there are \(q-1\) classes of norm \(u\).

## 4. A run of slow twists is at most half a period

Lemma E (TRACE-268, REPORT_L3.md) is stated for a prime modulus. The first three steps of its proof never use primality. They give, for \(0 < \varepsilon\le 1/16\) and a run of \(k\ge 3\) consecutive traces within \(\varepsilon\) of \(\mathbb Z\),
\[
|\sigma_1(\delta)\sigma_2(\delta)| \le 4\varepsilon^2\lambda^{-(k-1)}\bigl(1-\lambda^{-2(k-1)}\bigr)^{-2}.
\]
The constant is re-derived here from that display, so that the composite statement does not quote the printed \(4.12\) unchecked.

**Lemma 5 [P].** \(\lambda^4 = 577 + 408\sqrt 2 > 1000\), and for \(k\ge 3\),
\[
4\bigl(1-\lambda^{-2(k-1)}\bigr)^{-2} < \frac{201}{50}.
\]

Since \(423^2 = 178929 < 332928 = 2\cdot 408^2\), one has \(423 < 408\sqrt 2\) and \(\lambda^4 > 1000\). Thus \(\lambda^{-4} < 1/1000\). For \(k\ge 3\), \(\lambda^{-2(k-1)}\le\lambda^{-4}\), so
\[
\bigl(1-\lambda^{-4}\bigr)^{-2} < \Bigl(\frac{1000}{999}\Bigr)^2 = \frac{1000000}{998001}
\]
and
\[
4\cdot\frac{1000000}{998001} = \frac{4000000}{998001} < \frac{201}{50},
\]
because \(4000000\cdot 50 = 200000000 < 200598201 = 998001\cdot 201\).

**Proposition 6 [P].** Let \(h\) be an odd squarefree positive integer, let \(\mathfrak a\subset\mathcal O = \mathbb Z[\sqrt 2]\) be an ideal of norm \(h\), and let \(\beta\in\mathfrak a\) be nonzero in \(\mathcal O/h\mathcal O\). Suppose \(0 < \varepsilon\le 1/16\) and \(\operatorname{dist}(\operatorname{Tr}(\beta\lambda^j)/h, \mathbb Z)\le\varepsilon\) for \(k\ge 3\) consecutive \(j\). Then
\[
\lambda^{k-1} \le \frac{6432}{25}\,\varepsilon^2\, h.
\]
If in addition \(h = h_p\) for an odd prime \(p\), then \(k\le (p+1)/2\).

The first three steps of Lemma E, with the modulus \(h\) in place of the prime, produce a \(\gamma\in\tfrac18\mathcal O\) and a \(\delta = \beta/h - \gamma\) satisfying \(|N(\delta)|\le (201/50)\,\varepsilon^2\lambda^{-(k-1)}\), by Lemma 5. Then \(8h\delta = 8\beta - h\cdot(8\gamma)\). Here \(8\gamma\in\mathcal O\), so the second summand lies in \(h\mathcal O\). The ideal factorisation \((h) = \mathfrak a\,\bar{\mathfrak a}\) gives \(h\mathcal O\subset\mathfrak a\), and \(8\beta\in\mathfrak a\), so \(8h\delta\in\mathfrak a\).

The element is nonzero: \(8h\delta\equiv 8\beta\pmod h\), \(h\) is odd, and \(\beta\not\equiv 0\) in \(\mathcal O/h\mathcal O\). Since \(h\) is squarefree, \(\mathfrak a\) is a product of distinct prime ideals, one above each rational prime dividing \(h\). A nonzero element of \(\mathfrak a\) is divisible by each of those prime ideals, so its norm is divisible by each of those rational primes, hence by \(h\). Thus \(|N(8h\delta)|\ge h\). But \(|N(8h\delta)| = 64 h^2 |N(\delta)|\), so \(|N(\delta)|\ge 1/(64h)\) and
\[
\lambda^{k-1} \le \frac{201}{50}\cdot 64\cdot\varepsilon^2 h = \frac{6432}{25}\,\varepsilon^2 h.
\]

For the NSW value at odd \(p\), \(\bar\varepsilon = -\varepsilon^{-1}\), so \(\bar\varepsilon^p = -\varepsilon^{-p}\) and
\[
h_p = \frac{\varepsilon^p - \varepsilon^{-p}}{2} < \frac{\varepsilon^p}{2} = \frac{\lambda^{p/2}}{2}.
\]
At \(\varepsilon = 1/16\),
\[
\frac{6432}{25}\cdot\frac{1}{256} = \frac{201}{200},
\]
and \(\lambda^{k-1} \le (201/200)\, h_p < (201/400)\,\lambda^{p/2} < \lambda^{p/2}\). Hence \(k-1 < p/2\). For odd \(p\) this is \(k-1\le (p-1)/2\).

The bound depends on \(h\), not on a proper divisor of \(h\). A Binet window already has length of order \((p-1)/2\) (N6, the half-window in the pattern lemma). Proposition 6 caps a cross-line excursion by the same order. It removes no line from \(X\).

This proposition is not TRACE-268. The registered lemma is the prime-modulus statement. Trace modulo \(h\) close to an integer does not imply trace modulo \(q\mid h\) close to an integer, because \(\operatorname{Tr}/q = (h/q)\,(\operatorname{Tr}/h)\).

## 5. The triangle majorant

**Theorem 7 [P].** Assume \(h_p\) squarefree and composite, and \(p\ge 11\). Each cross line contributes \(h_p-1\) terms of coefficient \(1\). One mixed class, isotropic at the cofactor of a prime \(q\mid h_p\) and non-isotropic at \(q\), has \(\ell^1\) mass of \(Y\)-coefficients
\[
> \frac{64}{161}\, h_p > \frac{h_p}{3}.
\]
The constant uses \(q\ge 23\). Lemma W gives every prime factor \(\ge 2p-1\). For \(p\ge 13\) this is \(\ge 25\). For \(p = 11\), \(2p-1 = 21\) is not prime, and the least prime \(\equiv \pm 1\pmod{22}\) is \(23\), which does divide \(h_{11} = 23\cdot 353\).

The cross-line count is Corollary 2. For the mixed class, write \(h = qQ\) with \(Q = h/q\) squarefree and coprime to \(q\). Let the class be the set of \(\beta\) that are nonzero and fully isotropic modulo \(Q\), and non-isotropic modulo \(q\). By the Chinese remainder theorem the \(\ell^1\) mass of the coefficients \(\kappa_h/n_h\) is
\[
N_{\mathrm{iso}}(Q)\cdot\frac{1}{q-2}\sum_{\substack{\beta\bmod q\\ N\beta\not\equiv 0}}|\kappa_q(N\beta)|.
\]
Locally, \(N_{\mathrm{iso}}(Q) = \prod_{r\mid Q} 2(r-1)\). Each factor \(2(1-1/r)\) for \(r\ge 3\) is at least \(4/3\), so \(N_{\mathrm{iso}}(Q)\ge Q\). The inner sum equals \((q-1)\sum_{u\not\equiv 0}|\kappa_q(u)|\).

For the character sum, \(\sum_{u\not\equiv 0}|\kappa_q(u)| = \sum_{k=1}^{q-1} 2|\cos(\pi k/q)|\). The integers \(k\in\{1,\ldots,q-1\}\) with \(k\le\lfloor(q-1)/6\rfloor\) or \(k\ge q-\lfloor(q-1)/6\rfloor\) number \(2\lfloor(q-1)/6\rfloor\), and for those \(k\) one has \(|\cos(\pi k/q)|\ge\sqrt 3/2\). Thus the sum is at least \(2\sqrt 3\,\lfloor(q-1)/6\rfloor\).

Now \(12^2 = 144 < 147 = 3\cdot 7^2\), so \(\sqrt 3 > 12/7\) and \(2\sqrt 3 > 24/7\). For \(q\ge 7\), \(\lfloor(q-1)/6\rfloor\ge (q-7)/6\): if \(q = 6t+r\) with \(0\le r\le 5\), the case \(r = 1\) gives \(\lfloor 6t/6\rfloor = t\) and \((q-7)/6 = t-1\), and the case \(r = 5\) gives \(\lfloor(6t+4)/6\rfloor = t\) and \((q-7)/6 = t-1/3\). The other residues are not needed for the inequality, which holds for them by the same arithmetic. Therefore
\[
\sum_{u\not\equiv 0}|\kappa_q(u)| \ge \frac{24}{7}\cdot\frac{q-7}{6} = \frac{4(q-7)}{7}.
\]
Dropping \((q-1)/(q-2)\ge 1\) and using \(N_{\mathrm{iso}}(Q)\ge Q\),
\[
\ell^1 \ge Q\cdot\frac{4(q-7)}{7} = \frac{4h(q-7)}{7q}.
\]
For \(q\ge 23\), \((q-7)/q\ge 16/23\), so \(\ell^1\ge 64h/161\). And \(64\cdot 3 = 192 > 161\), so \(64/161 > 1/3\). The comparison \(64/161 < 2/5\) is also true, since \(320 < 322\), and it is not used as a lower bound.

**Corollary 8 [P].** Under the hypotheses of Theorem 7,
\[
|X_{\mathrm{line}}| \le (h_p-1)\max|r|, \qquad |Y_{\mathrm{class}}| \le \ell^1\max|r|,
\]
with \(\ell^1 > h_p/3\) and with \(r = \hat Z(\beta)/Z_\rho\). Since \(h_{1409} > 10^{539}\) and \(h_{3307} > 10^{1265}\), while the rooms of Proposition 4 in `proofs/h5_factor.md` are \(< 0.02011297\) and \(< 0.00334719\), either triangle majorant lies under the corresponding room only if
\[
\max|r| < 10^{-540}\quad(p = 1409), \qquad \max|r| < 10^{-1267}\quad(p = 3307).
\]
No bound of that size is proved.

The integer comparisons \(h_p > 10^{539}\) and \(h_p > 10^{1265}\) are asserts in `code/h5_lines.py`. A room below \(10^{-1}\) against a count above \(10^{539}\) forces the first display; a room below \(10^{-2}\) against a count above \(10^{1265}\) forces the second.

TRACE-295 gives \(\Lambda_{\mathrm{free}}^{8V}\le 1.9656353\), uniformly over twist sequences, with a certificate prefactor. The cap is larger than \(\mu^* = 1.9154712\). The ratio of those two radii is greater than \(1\), so the length-\(m\) majorant grows away from \(\mu^{*m}\). It does not yield \(|r|\le 1\), and this note does not assign a numerical prefactor to it.

The \(\ell^1\) lower bound is a lower bound on the sum of absolute coefficients. It is not a lower bound on \(|Y_{\mathrm{class}}|\). Cancellation could make the signed sum small. The same sentence applies to \(X_{\mathrm{line}}\). The proved statement is that the weights do not make the triangle majorant fit.

At \(p = 11\), \(q = 23\), \(Q = 353\), the same mass computed from the cosine sum rather than from \(4(q-7)/7\) is greater than \(20139\), while \((64/161)\cdot 8119 < 3228\) (`logs/h5_lines.json`). That is a check of the constant on one integer. The proof of the constant is the rational argument above. The cosine value itself is an 80-decimal evaluation of a sum of \(22\) terms and is not an input to Theorem 7.

## 6. The divisor sum, if the missing bound is assumed

Throughout this section the inequality
\[
|X_{\mathrm{line}}(d)| \le C\min(d, h/d)^{-\gamma}
\]
is a hypothesis. It is not a theorem of §§1–5. Every comparison under the hypothesis is marked **[C]** on that account. The arithmetic that converts the hypothesis into a sum is **[P]** or **[P-arith]** or **[P, finite]**, as labelled.

**Theorem 9 [P].** Let \(h = \prod_{j=1}^{w} q_j\) be squarefree, \(w\ge 2\), and let \(\gamma > 0\). The sum of \(\min(d, h/d)^{-\gamma}\) over the \(2^w-2\) proper divisors equals
\[
2\sum_{\substack{d\mid h\\ d < \sqrt h}} d^{-\gamma}
\]
and is at most \(2\bigl(\prod_j(1 + q_j^{-\gamma}) - 1\bigr)\).

No squarefree \(h>1\) is a square, so no divisor equals \(\sqrt h\). Proper divisors pair as \((d, h/d)\). The two minima in a pair agree and equal the smaller member. The resulting half-sum is at most the sum of \(d^{-\gamma}\) over all divisors greater than \(1\), which is the displayed product.

**Lemma 10 [P].** Fix an odd prime \(p\) and \(\gamma>0\). Among all finite sets of primes \(\equiv \pm 1\pmod{2p}\) whose product is at most \(h_p\), the product \(\prod(1+q^{-\gamma})\) is maximised by the set of the smallest such primes whose product is still at most \(h_p\).

Any set of cardinality one larger than that greedy set has product at least the product of the smallest primes of that larger cardinality, which exceeds \(h_p\). At fixed cardinality the product \(\prod(1+q^{-\gamma})\) is maximised by taking the smallest primes, because \(t\mapsto 1+t^{-\gamma}\) is positive and decreasing. Extending the cardinality up to the greedy length multiplies by factors greater than \(1\).

Thus, for squarefree \(h_p\), the sum in Theorem 9 is at most the greedy value. If a square divides \(h_p\), Theorem 9 does not apply. Squarefreeness remains H6.

**Proposition 11 [P, finite].** The greedy sets at the two conditional primes have lengths \(98\) and \(203\). Both products are \(\le h_p\), and in each case the next prime \(\equiv \pm 1\pmod{2p}\) pushes the product over \(h_p\). The lengths sit under \(w_{\max}(1409) = 112\) and \(w_{\max}(3307) = 231\). The least primes are \(2819\) and \(13229\).

The sieve and the exact integer product are `code/h5_lines.py`. The lengths \(2^{98}-2\) and \(2^{203}-2\) are still larger than either room by many orders of magnitude. Cutting \(\omega\) from \(w_{\max}\) down to the greedy length does not put a coefficient-\(1\) line inside the room.

**Proposition 12 [P-arith], under the hypothesis of this section with \(C = 1\).** On the greedy sets, the \(\gamma = 1\) sum and its multiple by \(M\) compare with the recomputed slacks as follows.

| \(p\) | \(\delta\) | sum | \(M\cdot\mathrm{sum}\) | slack | sum under slack | \(M\cdot\mathrm{sum}\) under slack |
|---|---|---|---|---|---|---|
| \(1409\) | \(7.4115\cdot 10^{-6}\) | \(0.00185727536\) | \(0.00698825118\) | \(0.02011296559\) | yes | yes |
| \(3307\) | \(3.4962\cdot 10^{-4}\) | \(0.00076449640\) | \(0.00301411787\) | \(0.00334718475\) | yes | yes |

The sums are the exact rationals \(2\bigl(\prod(1+1/q)-1\bigr)\), converted at 80 decimal places. The slack is the same expression as Proposition 4 of `proofs/h5_factor.md`, recomputed in this script. The row \(p = 1409\), \(\delta = 3.4962\cdot 10^{-4}\), has negative slack and is not a room.

At \(\gamma = 1/2\) the same sums are \(0.47286885\) and \(0.42234330\). Both exceed both rooms. The binary search on the greedy set, eighty steps at 80 decimal places, puts the smallest fitting \(\gamma\) at \(0.77078192\) absolutely and \(0.89579331\) times \(M\), for the robust room, and at \(0.87373522\) absolutely and \(0.99085641\) times \(M\), for the fragile room. Thus \(\gamma = 1\) clears both readings on this list, and \(\gamma = 1/2\) clears neither tight room. Full digits are in `logs/h5_lines.json`.

**Proposition 13 [P-arith], under the same hypothesis, with the floors instead of the primes.** Let \(v_j\) be the \(j\)-th integer \(\ge 2p-1\) that is \(\equiv \pm 1\pmod{2p}\), and let \(u_j = \max(2p-1, (p-1)j)\). The \(j\)-th prime factor of \(h_p\) is at least both, by Lemma W and the congruence. At \(w = w_{\max}(p)\) and \(\gamma = 1\),

| \(p\) | progression sum | \((p-1)j\) sum | absolute fit | times \(M\) |
|---|---|---|---|---|
| \(1409\) | \(0.00655604612\) | \(0.00682910817\) | both, against \(0.02011297\) | neither |
| \(3307\) | \(0.00322647395\) | \(0.00334308764\) | both, against \(0.00334719\) | neither |

The \((p-1)j\) row at \(p = 3307\) clears the slack \(0.00334718475\) by less than \(5\cdot 10^{-6}\). The progression row clears it by about \(1.2\cdot 10^{-4}\). Both clearances are above the \(10^{-70}\) truncation of the working precision. Neither is a bound on \(X_{\mathrm{line}}\).

**Theorem 14 [P].** For \(x > 3\) set
\[
f(x) = \frac{1 + \ln\bigl(x/\ln(x-1)\bigr)}{x}.
\]
Then \(f\) is strictly decreasing. For an integer \(p\ge 3\) and \(w = \lfloor p/\ln(p-1)\rfloor\ge 2\), the progression-floor sum of Theorem 9 at \(\gamma = 1\) and at this \(w\) is strictly less than \(2(e^{f(p)}-1)\).

Theorem 1 of `proofs/h5_factor.md` gives \(w_{\max}(p) < p/\ln(p-1)\), so \(w_{\max}(p)\le \lfloor p/\ln(p-1)\rfloor\). The \(j\)-th progression integer is at least \(pj\): the odd index \(j = 2m-1\) falls on \(2mp-1 = (j+1)p-1\ge jp\), and the even index \(j = 2m\) falls on \(jp+1\). Hence \(\sum_{j\le w} 1/v_j \le H_w/p\). For \(w\ge 2\), \(H_w < 1+\ln w\), and \(\ln w\le \ln\bigl(p/\ln(p-1)\bigr)\). Also \(\ln(1+1/v) < 1/v\). Combining these strict inequalities gives the exponential majorant.

For the derivative, write \(u(x) = \ln\bigl(x/\ln(x-1)\bigr)\) and \(f = (1+u)/x\). Then
\[
u'(x) = \frac{1}{x} - \frac{1}{(x-1)\ln(x-1)} < \frac{1}{x},
\]
so \(x u' - (1+u) < -u < 0\) whenever \(u>0\), which holds for \(x>e+1\). Thus \(f'<0\).

**Proposition 15 [P-arith].** The majorant of Theorem 14 satisfies \(2(e^{f(1409)}-1) < 0.00892 < 0.02011297\) and \(2(e^{f(4600)}-1) < 0.00318 < 0.00334719\). By Theorem 14, the loose sum is \(< 0.02011297\) for every integer \(p\ge 1409\). The same loose sum at \(p = 3307\) equals \(0.00356995629\), which is greater than \(0.00334719\).

**Proposition 16 [P-arith].** On the integers \(3307\le p\le 4599\), evaluated at 20 decimal places, the loose progression sum attains its maximum at \(p = 3307\), increases \(137\) times, and is \(< 0.00334719\) for every integer from \(3566\) through \(4599\). The last integer in the range at which it is \(\ge 0.00334719\) is \(3565\). The maximum on \([3566, 4599]\) falls at \(p = 3567\). Recomputed at 50 decimal places,
\[
\begin{align*}
p = 3565 &\colon& 0.00334731075,\\
p = 3566 &\colon& 0.00334637131,\\
p = 3567 &\colon& 0.00334672054.
\end{align*}
\]
The gap at \(p = 3567\) is \(4.69455\cdot 10^{-7}\). Combined with Proposition 15, the loose sum is \(< 0.00334719\) for every integer \(p\ge 3566\).

The clearance at the first integers past \(3565\) is thinner than \(10^{-6}\). It sits above the 50-decimal truncation, and it is not a comfortable room. The value is not monotone — it increases \(137\) times on the scanned range — so the scan is the argument, rather than a derivative. Past \(p = 4000\) the same sum is already \(< 0.00303430\).

Propositions 15 and 16 are statements about the majorant. Under the hypothesis \(|X_{\mathrm{line}}(d)|\le \min(d, h_p/d)^{-1}\), and for squarefree \(h_p\), they put the sum of the lines under the robust room for every integer \(p\ge 1409\), and under the fragile room for every integer \(p\ge 3566\). They do not put it under the fragile room at \(p = 3307\). The sharp greedy sum of Proposition 12 does, including after multiplication by \(M\). The hypothesis remains unproved, so none of these fits discharges H5(b).

For the reading with an extra factor \(M\): at either tight room the progression floor of Proposition 13, multiplied by \(M\), exceeds the slack. The greedy sum of Proposition 12, multiplied by \(M\), does not. For a fixed \(\delta < \ln(1+R)\), \(M\to\infty\) and the slack is \(M\) minus a term of size \(\sqrt{\ln p}\), while every majorant in this section tends to \(0\). Under the hypothesis, both readings therefore fit for all sufficiently large \(p\) at that fixed \(\delta\). The passage from the conditional primes to that regime is not given a second numerical threshold here. The binding comparisons are the two rooms in Proposition 12.

H5(c) has the same arithmetic and a stronger negative. Replacing \(\min(d, h/d)^{-\gamma}\) by the proved per-point factor \(2/(q-2)\) does not produce a small \(\ell^1\) mass. Theorem 7 gives \(\ell^1 > h_p/3\) for a single mixed class. The divisor sum of Section 6 would become a bound on \(|Y|\) only after a bound on \(\hat Z/Z\) of the same exponential strength as Corollary 8. No such bound is proved.

Prime powers are not given a substitute. N6 §6 records that the Ramanujan sum \(c_{q^a}(N\beta)\) vanishes unless \(q^{a-1}\mid N\beta\), and that \(|c|\le q^{a-1}\) on that shell. Dividing by the level does not, by itself, produce a negative power of \(q\) in front of a counted mass: the shell is a union of cosets \(\beta_0 + q^{a-1}\mathcal O\). That count is not carried out here. Squarefreeness remains H6.

## 7. What remains

H5(b) is open. The coefficient is \(1\), the run-length cap does not see the divisor, and the triangle majorant exceeds both rooms unless \(\max|\hat Z/Z|\) is smaller than \(10^{-540}\) or \(10^{-1267}\). The divisor arithmetic of §6 would fit the rooms at \(\gamma = 1\), \(C = 1\), on the greedy prime list, and it is not a theorem about \(X_{\mathrm{line}}\).

H5(c) is open for the same reason. The product weight is real and is already the factor \(2/(q-2)\). The \(\ell^1\) mass of one mixed class is \(> h_p/3\).

H5(a) is untouched. The exponent \(c < 0.387\) and the cutoff \(1.588^p\) remain as in `proofs/h5_factor.md`.

The composite branch of H5 is not discharged. The structural ceiling of v5 does not fall. Infinitude of \(\mathcal P = \{h_p\text{ prime}\}\) remains equivalent to the failure of \(R_{\mathrm{NSW}}\) (TRACE-210, as named in the closure of TRACE-303). Squarefreeness remains H6. The idealised slack is not the additive budget of v5. Frozen R′ is untouched. `record/claims.json` was not edited.
