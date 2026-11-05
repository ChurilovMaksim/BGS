# H8: window energies by lifting to \(\mathbb Z[\sqrt 2]\)

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure in ball arithmetic. **[N]** is not used. A finite count is a theorem about those integers. It is not an asymptotic bound on a trace ratio. `record/claims.json` was not edited.

The aggregate comparisons at \(p = 19\) and \(p = 29\) are parked, as in `proofs/h8_energy.md`. H7* stays a hypothesis of v5. This note stays in the amplified normalisation of H8. The open interval is the one left by that note: at \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\),
\[
\theta \in (0.16661157,\ 0.26223963).
\]
The upper end is the first-moment threshold of `proofs/h7_h8.md` Proposition 8. The lower end is the exponent-\(1\) wrap.

**What is proved.** A congruence of two \(k\)-sums of powers of \(\lambda\), with every exponent in an interval of span \(l\), is an equality in \(\mathbb Z[\sqrt 2]\) as soon as \(4k^2\lambda^l < d^2\). That span is
\[
l < 2\log_\lambda d - \log_\lambda(4k^2).
\]
On the open interval this contains \(\ell_0 = p/4\). For \(k \le 6\) the only equalities are permutations of the summands, so the ordered energy of such a window \(W\) is at most \(k!\,|W|^k\). The first equality that is not a permutation has \(k = 7\), and it is unique up to translation and swapping the two sides.

**What that energy does to the wrap.** It leaves the amplified loss at exponent \(1\). The \(2k\)-moment of the window beats the trivial character bound \(|S| \le |W|\) only for \(\theta < 0.00576146\) at \(p = 1409\) and \(k = 6\), inside the exponent-\(1\) range. Writing the energy ratio into the factor \(d\), which this note does not justify, reaches at most \(\theta < 0.17973708\) at \(p = 1409\) and \(\theta < 0.17322030\) at \(p = 3307\). Both lie under \(0.26223963\). Covering the upper end would require a loss exponent \(c < 0.63534092\). The formal product of the weight with the energy ratio stays above \(0.92122088\). H8 is not discharged.

## 1. Lifting

Let \(\mathcal O = \mathbb Z[\sqrt 2]\), \(\varepsilon = 1+\sqrt 2\) and \(\lambda = \varepsilon^2 = 3+2\sqrt 2\). The conjugate is \(\lambda^{-1} = 3-2\sqrt 2\). A positive integer \(d > 1\) acts by the ideal \(d\mathcal O\), of norm \(d^2\).

**Lemma 1 [P].** Let \(a_1,\ldots,a_k,b_1,\ldots,b_k\) be integers lying in some interval of span \(l\), that is \(\max - \min \le l\). Set
\[
\xi = \sum_{i=1}^k \lambda^{a_i} - \sum_{i=1}^k \lambda^{b_i}.
\]
Then \(|N(\xi)| \le 4k^2\lambda^l\). If \(\xi \in d\mathcal O\) and \(4k^2\lambda^l < d^2\), then \(\xi = 0\).

The \(+\) embedding of \(\lambda^e\) is \(\lambda^e\), and the conjugate embedding is \(\lambda^{-e}\). With \(M\) the maximum exponent and \(m\) the minimum,
\[
|\sigma_+(\xi)| \le 2k\,\lambda^M, \qquad |\sigma_-(\xi)| \le 2k\,\lambda^{-m}.
\]
The product is at most \(4k^2\lambda^{M-m} \le 4k^2\lambda^l\). A nonzero element of \(d\mathcal O\) has the form \(d(x+y\sqrt 2)\) with \(x,y \in \mathbb Z\) not both zero, so its norm is \(d^2|x^2-2y^2| \ge d^2\). The strict inequality forces \(\xi = 0\).

The location of the window cancels. The same \(l\) works for a window anywhere on \(\mathbb Z\).

Three lengths are easy to confuse.

- The estimate just proved allows every span \(l < 2\log_\lambda d - \log_\lambda(4k^2)\). In the scale \(d = \lambda^{\theta p}\) this is \(l < 2\theta p - \log_\lambda(4k^2)\).
- Bounding both embeddings by \(2k\lambda^l\), and comparing the product with the norm \(d^2\), gives the shorter sufficient condition \(2k\lambda^l < d\), that is \(l < \log_\lambda d - \log_\lambda(2k)\). That length contains \(\ell_0 = p/4\) only for \(\theta > 1/4 + \log_\lambda(2k)/p\).
- Comparing the product of those two crude bounds with \(d\), rather than with \(N(d\mathcal O) = d^2\), gives \(l < \ln d/(2\ln\lambda) - O(\log k) = \theta p/2 - O(\log k)\). That length contains \(\ell_0 = p/4\) only for \(\theta \ge 1/2\).

The open interval lies under \(1/2\) and over \(1/8\). The third length does not contain \(\ell_0\) anywhere in the interval. The second contains it only near the top. The first contains it throughout the interval, for each fixed \(k\) and every large \(p\).

**Lemma 2 [P, arithmetic].** For \(k \le 7\) and \(p \in \{1409, 3307\}\), a window of span \(p/4\) satisfies the hypothesis of Lemma 1 at every
\[
\theta \ge \frac{\alpha(0.28)}{4\ln\lambda}.
\]
The threshold \(\theta > 1/8 + \log_\lambda(4k^2)/(2p)\) lies under \(0.12600049\) for \(k = 6\), \(p = 1409\), and under \(0.12542628\) for \(k = 6\), \(p = 3307\). The same comparison at \(k = 7\) lies under \(0.12606255\) and \(0.12545272\). The exponent-\(1\) threshold is larger than each of these. The slack in the norm inequality, at that exponent-\(1\) threshold and at \(k = 6\), is more than \(200\) nats at \(p = 1409\) and more than \(400\) nats at \(p = 3307\).

The enclosures are in `logs/h8_moments.json`, at arb precision \(200\), with the same \(\alpha(0.28)\) as `code/h7h8.py`. The ball of \(\alpha(0.28)\) reproduces the centre \(1.17477626638003325659\).

Since \(\theta < 1/2\) on the whole interval up to the first-moment end, the liftable span is \(< p\). For odd \(d \mid h_p\) the order of \(\lambda\) is \(p\), and for a prime factor of \(K_p\) other than \(7\) the order is \(3p\), both by the citations in `proofs/h8_energy.md` Lemma 2. A liftable window therefore contains at most one representative of each power. Lemma 1 at \(k = 1\) is the same statement: under \(4\lambda^l < d^2\), the powers themselves are distinct in \(\mathcal O/d\mathcal O\).

The full orbit, of length \(p\) or \(3p\), does not fit in this span. Lemma 1 does not evaluate the additive energy of \(\langle\lambda\rangle\).

## 2. Equal sums of powers

The balanced \(\varepsilon\)-expansion is the one proved in `proofs/span_law.md`. The label TRACE-337 is not a row of `record/claims.json`. The input used here is Lemmas 3 and 4 of that file, applied to one unit.

**Lemma 3 [P].** The balanced word of \(\lambda^n\) is a single digit \(+1\) at the index \(1-2n\).

For \(\alpha = 1\), \(|\theta_k| = (\sqrt 2/4)\,\varepsilon^k\). The left threshold \(K_l\) is the least \(k\) with \(\varepsilon^k \ge \sqrt 2\). Then \(K_l = 1\), because \(\varepsilon^0 = 1 < \sqrt 2 < \varepsilon\). The right threshold \(K_r\) is the greatest \(k\) with \(|\theta_k| \le |N|/4 = 1/4\), that is \(\varepsilon^k \le 1/\sqrt 2\). Since \((\sqrt 2-1)^2 = 3-2\sqrt 2\), the inequality \(3-2\sqrt 2 < 1/2\) expands as \(5 < 4\sqrt 2\), then \(25 < 32\). Thus \(\varepsilon^{-1} < 1/\sqrt 2 < 1\), so \(K_r = -1\). The norm is \(1\), so the class is non-exceptional. Lemmas 3 and 4 of `proofs/span_law.md` put the only nonzero digit at \(K_l = 1\), and that digit is \(+1\) because \(\theta_1 > 0\).

Multiplication by \(\varepsilon^t\) replaces \(\theta_k\) by \(\theta_{k+t}\), so it moves the digit from index \(1\) to index \(1-t\). For \(t = 2n\), the element is \(\lambda^n\) and the site is \(1-2n\). The digit stays \(+1\).

The same computation on \(-12 \le n \le 12\) is the finite check in `code/h8_moments.py`. The lemma is the argument above.

A sum of several such units is not the sum of their words. The integer \(2\) is \(1+1\), and its balanced word is not two copies of the word of \(1\). Multiplicities are handled by the norm of the relation, not by adding digits.

**Theorem 4 [P].** Let \(c:\mathbb Z \to \mathbb Z\) have finite support and satisfy \(\sum c_n\lambda^n = 0\) and \(\sum c_n = 0\). If \(c\) is not identically zero, the positive mass \(k' = \sum_{c_n>0} c_n\) is at least \(7\).

The two conditions say that the Laurent polynomial is divisible by \(x^2-6x+1\) and by \(x-1\). Those factors are coprime, because the value of \(x^2-6x+1\) at \(1\) is \(-4\). The mass bound does not need the factors. Write \(A\) for the multiset with \(c_n\) copies of each \(n\) where \(c_n > 0\), and \(B\) for the multiset of the negative coefficients. Then \(|A| = |B| = k'\), the supports are disjoint, and \(\sum_{a\in A}\lambda^a = \sum_{b\in B}\lambda^b\). Let \(m\) be the largest integer in the support and replace \(c\) by \(-c\) if needed, so the multiplicity \(r\) of \(m\) on \(A\) is positive and \(m\) does not meet \(B\). Dividing the \(+\) embedding by \(\lambda^m\) gives
\[
r + \sum_{j\ge 1}\alpha_j\lambda^{-j} = \sum_{j\ge 1}\beta_j\lambda^{-j},
\]
with \(\alpha_j,\beta_j\) nonnegative integers, \(\sum\alpha_j = k'-r\) and \(\sum\beta_j = k'\). The right-hand side is at most \(k'\lambda^{-1}\). The left-hand side is at least \(r \ge 1\). Hence \(k' \ge \lambda\). The comparison \(5\lambda^{-1} < 1\) expands as \(5(3-2\sqrt 2) < 1\), then \(14 < 10\sqrt 2\), then \(49 < 50\). So \(\lambda > 5\) and \(k' \ge 6\).

If \(k' \le 5\), the right-hand side is at most \(5\lambda^{-1} < 1\).

If \(k' = 6\), then \(r \le 6/\lambda < 2\), so \(r = 1\). If the multiplicity \(\beta_1\) at exponent \(m-1\) is at most \(5\), the right-hand side is at most \(5\lambda^{-1}+\lambda^{-2} = 32-22\sqrt 2\), and \(32-22\sqrt 2 < 1\) is \(31 < 22\sqrt 2\), that is \(961 < 968\). So \(\beta_1 = 6\) and the right-hand side equals \(6\lambda^{-1}\). The identity \(6\lambda^{-1}-1 = \lambda^{-2}\) is
\[
6(3-2\sqrt 2)-1 = 17-12\sqrt 2 = (3-2\sqrt 2)^2.
\]
The left-hand side is then \(1+\eta\) with \(\eta = \lambda^{-2}\) and with five units of multiplicity below \(m\). A unit at \(m-1\) contributes at least \(\lambda^{-1} > \lambda^{-2}\). Two or more units at \(m-2\) contribute at least \(2\lambda^{-2}\). One unit at \(m-2\) leaves four units further down, each positive, so the sum exceeds \(\lambda^{-2}\). No unit at \(m-2\) leaves the whole mass at exponents \(\le m-3\), and five units there contribute at most \(5\lambda^{-3} < \lambda^{-2}\), because \(5 < \lambda\). Every placement contradicts \(\eta = \lambda^{-2}\).

Thus \(k' \ge 7\).

**Corollary 5 [P].** If \(\sum_{i=1}^k \lambda^{a_i} = \sum_{i=1}^k \lambda^{b_i}\) in \(\mathcal O\) and \(k \le 6\), the multisets \(\{a_i\}\) and \(\{b_i\}\) agree.

The difference of the multiplicity functions satisfies both hypotheses of Theorem 4, and its positive mass is at most \(k\).

**Theorem 6 [P].** Up to translation and swapping the two sides, the only equality of positive mass \(7\) is
\[
\lambda^4 + 6\lambda = 6\lambda^3 + 1.
\]

The two sides are the integers \(595+420\sqrt 2\). For the shape: the same division as in Theorem 4, now with \(k' = 7\), forces \(r = 1\). If \(\beta_1 \le 5\), the right-hand side is at most \(5\lambda^{-1}+2\lambda^{-2} = 49-34\sqrt 2\), and \(49-34\sqrt 2 < 1\) is \(24 < 17\sqrt 2\), that is \(576 < 578\). If \(\beta_1 = 7\), the right-hand side equals \(7\lambda^{-1} = 1+\lambda^{-1}+\lambda^{-2}\). A multiplicity \(\alpha_1 \ge 2\) overshoots \(\lambda^{-1}+\lambda^{-2}\). Multiplicity \(\alpha_1 = 1\) leaves five units summing to \(\lambda^{-2}\). Shifting by \(\lambda^2\) makes those five units a sum of powers of \(\lambda\) equal to \(1\): a positive power is at least \(\lambda > 1\), a zero power is \(1\) and the other four units are positive, and five strictly negative powers sum to at most \(5\lambda^{-1} < 1\). Multiplicity \(\alpha_1 = 0\) puts all six units at gap at least \(2\), hence at most \(6\lambda^{-2}\). And \(6\lambda^{-2} < \lambda^{-1}+\lambda^{-2}\) because \(5 < \lambda\).

The remaining case is \(\beta_1 = 6\), with the seventh unit of \(B\) at gap \(t \ge 2\). The right-hand side is \(6\lambda^{-1}+\lambda^{-t} = 1+\lambda^{-2}+\lambda^{-t}\). A positive \(\alpha_1\) gives a left-hand side at least \(1+\lambda^{-1}\), and \(\lambda^{-1} > 2\lambda^{-2}\). So \(\alpha_1 = 0\). If \(\alpha_2 \ge 2\), the six units cannot all sit at \(m-2\) without exceeding \(2\lambda^{-2}\), and any unit further down makes a double contribution at \(m-2\) strictly larger than \(2\lambda^{-2}\). If \(\alpha_2 = 1\), five units at gap at least \(3\) must sum to a pure power \(\lambda^{-t}\). The same shifting argument, now equal to \(1\) after multiplication by \(\lambda^t\), forbids it. So \(\alpha_2 = 0\), and six units at gap at least \(3\) sum to at most \(6\lambda^{-3}\). The identity
\[
6\lambda^{-3} = \lambda^{-2}+\lambda^{-4}
\]
is \(6(99-70\sqrt 2) = 594-420\sqrt 2 = (17-12\sqrt 2)+(577-408\sqrt 2)\). Reaching \(\lambda^{-2}+\lambda^{-t}\) therefore forces \(t = 4\) and all six units at gap \(3\). That placement is the displayed equality, translated so that the lowest exponent is \(0\).

The generator \((x-1)(x^2-6x+1) = x^3-7x^2+7x-1\) is the mass-\(8\) relation \(\lambda^3+7\lambda = 7\lambda^2+1\). It is not needed for \(k \le 7\). Every equal-mass relation is a multiple of this generator, because of the two coprime factors above. Theorem 4 is the statement that no multiple has positive mass \(1,\ldots,6\).

## 3. The window energy

Let \(W\) be a finite set of integers of span \(l\) and cardinality \(|W|\), and let \(d > 1\) satisfy \(4k^2\lambda^l < d^2\). The ordered energy \(E_k(W)\) is the number of
\[
(a_1,\ldots,a_k,b_1,\ldots,b_k) \in W^{2k}
\]
with \(\sum_{i\le k}\lambda^{a_i} \equiv \sum_{i\le k}\lambda^{b_i} \pmod{d\mathcal O}\).

**Theorem 7 [P].** For \(k \le 6\),
\[
E_k(W) = \sum_{a\in W^k}\frac{k!}{\prod_v m_v(a)!} \le k!\,|W|^k.
\]
The injections alone contribute \(k!\,|W|(|W|-1)\cdots(|W|-k+1)\).

Lemma 1 turns the congruence into an equality in \(\mathcal O\). Corollary 5 turns the equality into equality of multisets. An ordered \(k\)-tuple with multiplicities \(m_v\) has \(k!/\prod m_v!\) ordered rearrangements, and every rearrangement remains in \(W\). The denominator is at least \(1\).

**Theorem 8 [P].** For \(k = 7\), \(E_7(W) \le 2\cdot 7!\,|W|^7\).

A fibre of the sum map, on multiplicity functions of mass \(7\), has size at most \(2\). The difference of two such functions is an equal-mass relation of positive mass at most \(7\), hence zero or a translate of the relation in Theorem 6, and that relation determines the partner. Each multiplicity function contributes at most \(7!\) ordered tuples. Therefore the representation function is at most \(2\cdot 7!\), and the sum of its squares is at most that constant times \(|W|^7\).

On a window of \(L\) consecutive exponents, with \(4 \le L \le 10\) and \(k \le 7\), the script counts the energy directly. For \(k \le 6\) the excess over the permutation count is \(0\). For \(k = 7\) the excess is \(98(L-4)\), which is \(2\cdot 7\cdot 7\) for each of the \(L-4\) translates of Theorem 6 that fit in the window. That is a finite identity for those windows. The bound in Theorem 8 is the one used for every window.

## 4. The moment and the loss exponent

The group \(\mathcal O/d\mathcal O\) is isomorphic to \((\mathbb Z/d\mathbb Z)^2\), so it has \(d^2\) additive characters. Orthogonality gives
\[
\sum_{\psi}\Bigl|\sum_{w\in W}\psi(\lambda^w)\Bigr|^{2k} = d^2\,E_k(W).
\]
For \(k \le 6\), Theorem 7 supplies the mean bound
\[
d^{-2}\sum_{\psi}|S_W(\psi)|^{2k} \le k!\,|W|^k.
\]
One character can still be as large as the trivial bound \(|S_W| \le |W|\). Passing from the mean to the maximum costs the number of characters:
\[
\max|S_W| \le d^{1/k}(k!)^{1/(2k)}|W|^{1/2}.
\]
This is smaller than \(|W|\) precisely when
\[
\theta < \frac{k\ln|W| - \ln(k!)}{2p\ln\lambda},
\]
at a modulus of size \(\lambda^{\theta p}\), for the estimate that uses \(E_k \le k!\,|W|^k\). For \(k = 7\) the same comparison with Theorem 8 subtracts an extra \(\ln 2\) from the numerator.

**Proposition 9 [CA].** Take \(|W| = \lfloor p/4\rfloor+1\), the greatest number of integers in an interval of span \(p/4\). At arb precision \(200\) the character-sum threshold above is

| \(p\) | \(k = 6\) | \(k = 7\) |
| --- | --- | --- |
| \(1409\) | \(< 0.00576146\) | \(< 0.00641117\) |
| \(3307\) | \(< 0.00289289\) | \(< 0.00324273\) |

For \(2 \le k \le 6\) the numerator increases with \(k\), because \(|W| \ge 353 > k+1\). The strongest of these bounds is the \(k = 6\) entry, and the \(k = 7\) entry remains of the same size. All four lie under \(0.16661157\).

The shape is the same as the \((2,2)\) meeting point in `proofs/h8_energy.md` Proposition 4. Both are \(O(\ln p/p)\). The window is of length \(O(p) = O(\log d)\), so a factor \(|W|^{O(k)}\) is \(d^{o(1)}\). It is not a fixed negative power of \(d\).

**Proposition 10 [P].** The amplified loss exponent remains \(1\). The range covered by the wrap at \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\) remains
\[
\theta < 0.16661157.
\]

N16b (c2) charges a factor \(d\) for weights \(\asymp d/h\): positivity gives \(E_{\mathrm{coset}} \le d\cdot E_\Gamma\), and the weight sits outside \(\ell^3 \le \ell^2\). The factor is that weight. Theorems 7 and 8 bound the additive energy of a window of powers of \(\lambda\). The ratio \(E_k/|W|^{2k}\) is a power of \(d\) only after taking logarithms, and that power is the \(\gamma\) of the next paragraph. Substituting the ratio for the weight, or multiplying the weight by the ratio, identifies the additive energy of the window with the amplified weight. Proposition 10 does not make that identification. The same separation is Proposition 5 of `proofs/h8_energy.md`, for the second moment of the full graph.

The arithmetic of the identification, kept separate from the proposition, is as follows. The exact energy for \(k \le 6\) is at least the injection count, so
\[
\frac{|W|^{2k}}{E_k(W)} \le \frac{|W|^k}{k!}\prod_{j=1}^{k-1}\frac{|W|}{|W|-j}.
\]
Replacing the factor \(d\) by \(d\cdot E_k/|W|^{2k}\) therefore moves the exponent-\(1\) threshold by at most
\[
\frac{1}{p\ln\lambda}\Biggl(k\ln|W| - \ln(k!) + \sum_{j=1}^{k-1}\ln\frac{|W|}{|W|-j}\Biggr).
\]
The same upper bound holds at \(k = 7\), because the mass-\(7\) solutions only increase \(E_7\). At \(|W| = \lfloor p/4\rfloor+1\):

| \(p\) | \(k = 6\) | \(k = 7\) |
| --- | --- | --- |
| \(1409\) | \(< 0.17815167\) | \(< 0.17973708\) |
| \(3307\) | \(< 0.17240046\) | \(< 0.17322030\) |

The largest entry is \(< 0.17973708\). The first-moment end is \(> 0.26223963\). The gap remains open under the identification.

As a power of \(d\), the same upper bound on the saving says that the formal combined exponent \(1+\ln(E_k/|W|^{2k})/\ln d\) is still greater than \(0.93073649\) at \(p = 1409\), \(k = 6\), when \(\theta\) is the exponent-\(1\) threshold, and greater than \(0.95599406\) when \(\theta = 0.26223963\). At \(k = 7\) the corresponding lower bounds are \(0.92122088\) and \(0.94994840\). Covering \(\theta\) up to \(0.26223963\) requires
\[
c < \frac{\alpha(0.28)}{4\ln\lambda\cdot 0.26223963},
\]
and that quotient lies under \(0.63534092\). Every formal exponent in the table is larger.

The value of \(k\) at which the diagonal expression \(k\ln|W|-\ln(k!)\), with no allowance for relations, would push the same formal sum up to \(0.26223963\) is \(k = 113\) at \(p = 1409\) and \(k = 261\) at \(p = 3307\). Both lie past Theorem 4, so the expression \(E_k \le k!\,|W|^k\) is false there. Lifting is not the obstruction: \(4\cdot 113^2 < \lambda^7\) and \(4\cdot 261^2 < \lambda^8\), and the resulting shift of the threshold \(1/8\) is a few thousandths, still under \(0.16661157\). The relations are the obstruction. This paragraph is the arithmetic of a substitution the note does not justify, at values of \(k\) where the diagonal bound is already false.

## 5. Boundary

H8 remains open. On windows short enough for Lemma 1, and for \(k \le 6\), the ordered energy is the permutation count. The amplified wrap at \(\ell_0 = p/4\) still covers only \(\theta < 0.16661157\). The moment bound of Proposition 9 covers only an \(O(\ln p/p)\) range inside that interval. The formal identification of §4 reaches at most \(0.17973708\), and only as arithmetic, not as a theorem. The interval from that value up to \(0.26223963\) stays open.

The full-group energies \(J_k\) of `computations/verification/lineN/REPORT_N_v2.md` Lemma N1.1 are not evaluated. The orbit of length \(p\) or \(3p\) is longer than the liftable span on this interval, so the window bound does not become a bound on \(J_k\).

H7* remains a hypothesis of v5. H1, H3, and frozen R′ are untouched. The primes \(1409\) and \(3307\) are not recomputed.

The self-referee is `REFEREE_H8_MOMENTS.md`.
