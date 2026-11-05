# H8: the additive energy of \(\langle\lambda\rangle\), and the \(\theta\) range it covers

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[CA]** is a finite enclosure in ball arithmetic. **[N]** is not used. A finite count is a theorem about those integers. It is not an asymptotic bound on a trace ratio. `record/claims.json` was not edited.

The aggregate comparisons at \(p = 19\) and \(p = 29\) are parked. Both primes lie under the conditional thresholds \(1409\) and \(3307\) quoted for Theorem R♯-mod v5, so a bound or a failure at those conductors is not an input the large-\(p\) inequality reads. H7* stays a hypothesis of v5, including at \(K_p\) levels. The decision in `proofs/h7_average.md` stands: the averaged operator does not put the section aggregate under the threshold, and it does not refute it.

This note attacks the input v5 uses at large \(p\): H8 in the amplified normalisation. `proofs/h7_h8.md` §5 records that a second-moment statement with loss exponent \(c\) meets the wrap when \(c\ln d < \alpha(\bar\rho)\,\ell\), and that exponent \(1\), at \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\), covers only
\[
\theta = \frac{\log_\lambda d}{p} < 0.16661157.
\]
The subgroup in the attack is \(\langle\lambda\rangle\) in \(\mathcal O/d\mathcal O\), of order \(p\) for \(d \mid h_p\) and of order \(3p\) for a prime factor of \(K_p\) other than \(7\), with \(d\) allowed up to \(\sqrt{h_{3p}}\).

**What is covered.** For every odd \(d\) that has a split prime factor of the same multiplicative order \(L\), the additive energy of \(\langle\lambda\rangle\) satisfies \(J_2 \le 2L^2 - L\) when \(L\) is odd. The bound does not depend on \(d\) and has no upper restriction on \(d\). The exponent is \(2\): the ratio to the trivial energy \(L^3\) is \(< 2/L\).

**What that exponent does to the wrap.** It leaves the amplified loss at exponent \(1\). At \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\) the covered range remains \(\theta < 0.16661157\). The interval up to the first-moment threshold \(0.26223963\) stays open. H8 is not discharged.

## 1. The graph

Let \(\mathcal O = \mathbb Z[\sqrt 2]\), \(\varepsilon = 1+\sqrt 2\) and \(\lambda = \varepsilon^2 = 3+2\sqrt 2\). The multiplication-by-\(\lambda\) map on \(\mathcal O\) is the matrix \(S = \begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix}\). For an odd prime \(q \equiv \pm 1 \pmod 8\) there is \(w \in \mathbb F_q\) with \(w^2 = 2\), and
\[
\mathcal O/q\mathcal O \xrightarrow{\sim} \mathbb F_q\times\mathbb F_q, \qquad x+y\sqrt 2 \mapsto (x+yw,\ x-yw).
\]
The image of \(\lambda\) is \((g, g^{-1})\) with \(g = 3+2w\). Write \(L = \mathrm{ord}_q(\lambda)\) and \(v_j = (g^j, g^{-j})\). The set \(\Gamma = \{v_j : 0 \le j < L\}\) is the graph of inversion on the subgroup \(\langle g\rangle\).

\(J_2(\Gamma)\) is the number of \((j_1,j_2,j_3,j_4) \in (\mathbb Z/L\mathbb Z)^4\) with \(v_{j_1}+v_{j_2} = v_{j_3}+v_{j_4}\) in \(\mathbb F_q^2\). This is the additive energy \(T_2(\Gamma)\). The same count on exponent tuples, with the equality read in \(\mathcal O/d\mathcal O\), is \(J_2\) at a composite modulus.

**Lemma 1 [P].** \(\lambda - 1 = 2\varepsilon\). For odd \(d\), \(\lambda \not\equiv 1 \pmod d\).

The norm computation \(N(2+2\sqrt 2) = -4\) is the same identity. An odd \(d\) cannot divide the coefficients of \(2\varepsilon\).

**Lemma 2 [P, cited].** For odd \(d \mid h_p\), \(\mathrm{ord}_d(\lambda) = p\). For a prime \(q \mid K_p\), \(q \ne 7\), the rank is \(3p\).

TRACE-277 gives \(\lambda^p \equiv 1 \pmod{2h_p}\). Lemma 1 then forces the order on odd \(d \mid h_p\) to be \(p\). The rank \(3p\) on prime factors of \(K_p\) other than \(7\) is TRACE-265. Both are used as registered inputs. They are not re-proved. TRACE-230 adds that every prime \(q \ne 7\) dividing \(h_{3p}\) has rank \(p\) or \(3p\). Since \(p\) and \(3p\) are odd, \(-1\) is not a power of \(\lambda\) in these subgroups.

## 2. The energy

**Theorem 1 [P].** Let \(q \equiv \pm 1 \pmod 8\) be prime and let \(L = \mathrm{ord}_q(\lambda)\). Then
\[
J_2(\Gamma) =
\begin{cases}
2L^2 - L & \text{if \(L\) is odd},\\
3L^2 - 3L & \text{if \(L\) is even}.
\end{cases}
\]

The odd case is the uniqueness argument of BGS-TRACE-279, Lemma N1.2(a), in `computations/verification/lineN/REPORT_N_v2.md`: if \(v_{j}+v_{k} = v_{j'}+v_{k'}\) and the common sum \(\sigma\) of the first coordinates is nonzero, the common product is \(\sigma\) divided by the second coordinate, so the unordered pair of field elements is the root pair of one quadratic, and \(\{j,k\} = \{j',k'\}\). For \(L\) odd one has \(-1 \notin \langle g\rangle\), so \(\sigma = 0\) does not occur. Every solution is one of the trivial ordered pairs. Counting them gives equality, which TRACE-279 stated as \(\le\) and checked numerically at \(17\) levels. The count is: \(L\) diagonal sums, each with representation \(1\), and \(L(L-1)/2\) off-diagonal sums, each with representation \(2\), hence
\[
J_2 = L + 2L(L-1) = 2L^2 - L.
\]
A diagonal sum \(2v_j\) determines \(g^j\) because \(2 \ne 0\), so it is not an off-diagonal sum.

For \(L\) even, \(g^{L/2} = -1\). Each of the \(L\) ordered antipodal pairs \((j,\ j+L/2)\) sums to \((0,0)\), and no other pair does. Those \(L\) pairs contribute \(L^2\). The remaining \(L^2-2L\) ordered pairs have nonzero sum, fall under the same quadratic uniqueness, and contribute \(2L(L-2)\). The \(L\) diagonal sums contribute \(L\) and are disjoint from \((0,0)\). The total is \(3L^2-3L\). TRACE-279 assumes \(L\) odd, so this case is not part of that lemma. Orders dividing \(3p\) are odd, and the \(\theta\) statements below use only the odd formula.

**Theorem 2 [P].** Let \(d\) be odd and let \(q \mid d\) be a prime with \(q \equiv \pm 1 \pmod 8\) and \(\mathrm{ord}_q(\lambda) = \mathrm{ord}_d(\lambda) = L\). Then the energy of \(\{\lambda^j : 0 \le j < L\}\) in \(\mathcal O/d\mathcal O\) is at most the energy of its image in \(\mathcal O/q\mathcal O\). For \(L\) odd,
\[
J_2(d) \le 2L^2 - L.
\]
The right-hand side does not depend on \(d\).

Reduction modulo \(q\) is a ring homomorphism, so an additive relation modulo \(d\) is an additive relation modulo \(q\). Equal orders mean the \(L\) powers stay distinct after reduction, and the exponent quadruples inject into the exponent quadruples that collide modulo \(q\). Theorem 1 bounds the image.

The trivial energy is \(L^3\): three exponents determine at most one fourth. For \(L \ge 1\),
\[
\frac{J_2(d)}{L^3} \le \frac{2L-1}{L^2} < \frac{2}{L}.
\]
Written as a power of \(d\), the exponent \(\ln(J_2/L^3)/\ln d\) is negative for every \(d > 1\) and every \(L \ge 3\).

No size restriction enters. In particular the bound holds for \(d\) up to \(\sqrt{h_{3p}}\) and past it, whenever the split full-order prime factor exists. From `proofs/h7_h8.md` Proposition 9, \(\limsup(\ln h_p)/p \le (\ln\lambda)/2\). Since \(K_p = 4h_p^2+3\) and \(h_{3p} = h_p K_p\), one has \(\log_\lambda\sqrt{h_{3p}}/p \to 3/4\). That scale is inside Theorem 2.

**Finite checks [P].** The script `code/h8_energy.py` counts the energy by enumerating pair sums.

| modulus | \(L\) | energy | formula |
| --- | --- | --- | --- |
| \(7, 31, 41, 457\) | \(3, 15, 5, 57\) | \(15, 435, 45, 6441\) | \(2L^2-L\) |
| \(73, 89\) | \(36, 44\) | \(3780, 5676\) | \(3L^2-3L\) |
| \(217 = 7\cdot 31\) | \(15 = \mathrm{ord}_{31}(\lambda)\) | \(435\) | \(\le 2L^2-L\), equal |
| \(31^2 = 961\) | \(15 = \mathrm{ord}_{31}(\lambda)\) | \(435\) | equal to \(2L^2-L\) |
| \(49 = 7^2\) | \(21\) | \(1617\) | exceeds \(861\) |
| \(343 = 7^3\) | \(147\) | \(122451\) | exceeds \(43071\) |

At \(49\) and \(343\) the order grows, so Theorem 2 does not apply, and the field identity is false. At \(31^2\) the order stays \(15\), and the identity survives. The obstruction is the growth of the order. Square factors whose order equals the order modulo the underlying prime remain inside Theorem 2.

On the stored factorisations of \(K_p\) for primes \(5 \le p \le 31\), every prime factor is \(1\) or \(7 \pmod 8\), the prime \(7\) has order \(3\), and every other prime factor has order \(3p\). That is a finite check of the splitting and rank hypotheses on that range. It is the input Theorem 2 uses there. An inert prime factor at a larger \(p\) would lie outside Theorem 1.

## 3. Bourgain–Glibichuk–Konyagin and Heath-Brown–Konyagin

Both theorems are the ones the scale \(|\langle\lambda\rangle| = 3p\) against \(d \le \sqrt{h_{3p}}\) was meant to be fed to. For this graph they are weaker than Theorem 1, and on the open interval of `proofs/h7_h8.md` §5 neither one moves the wrap.

**BGK does not meet its hypothesis on the gap, for any fixed positive \(\delta\), once \(p\) is large [P, scale].** Bourgain–Glibichuk–Konyagin, J. London Math. Soc. 73 (2006), and the form cited in `computations/verification/lineN15b/REPORT_N15b.md` §2, need a multiplicative subgroup of size at least \(q^\delta\) for some fixed \(\delta > 0\). N15b records that \(|\langle\lambda\rangle|\asymp\log q\) on the worst classes, so the hypothesis fails. The same comparison at the bottom of the amplified gap is an enclosure. With \(L = 3p\) and \(\ln q = \alpha(0.28)\,p/4\),
\[
\delta_{\max}(p) = \frac{4\ln(3p)}{\alpha(0.28)\,p}
\]
is an upper bound for every \(\delta\) that still has \(L \ge q^\delta\). At arb precision \(200\), \(\delta_{\max}(1409) < 0.02017629\) and \(\delta_{\max}(3307) < 0.00947485\). Every application that needs a fixed \(\delta \ge 0.01\) fails on \(\theta \ge 0.16661157\) for every prime \(p \ge 3307\). The limit is \(0\). The sharp form that needs \(\log|H| > C\log q/\log\log q\), and the Montgomery–Vaughan–Wooley conjecture that needs \(|H|/\log q \to \infty\), fail for the same reason. N15b §2 already records those three failures for the first-moment route. They are not re-opened here.

**Heath-Brown–Konyagin applies on the gap and gives a weaker energy [external].** Heath-Brown and Konyagin, Quart. J. Math. 51 (2000) 221–235, in the form stated as Theorem 2.2 in Konyagin's lectures on exponential sums: if \(G \subset \mathbb F_q^\times\) is a subgroup with \(|G| \le q^{2/3}\), then \(T_2(G) \ll |G|^{5/2}\). The implied constant is absolute and is not numeric in that statement. This note does not use a numeric value of it.

The projection of \(\Gamma\) onto the first coordinate is a subgroup of \(\mathbb F_q^\times\) of order \(L\). Whenever \(L \le q^{2/3}\), the projected energy is \(\ll L^{5/2}\), and the graph energy is at most the projected energy. Theorem 1 gives \(2L^2-L\) with no restriction on \(q\), so the Heath-Brown–Konyagin shape is the coarser one on this set. The size restriction \(L \le q^{2/3}\) does hold throughout the open interval at large \(p\): it is \(\theta \ge \tfrac32\ln L/(p\ln\lambda)\), whose upper envelope at \(L = 3p\) is \(< 0.00504241\) for \(p = 1409\) and \(< 0.00236793\) for \(p = 3307\). Both lie under \(0.16661157\). From the bottom of the gap upward, including the balanced scale \(\theta \to 3/4\), the hypothesis is satisfied and the saving it produces is still only a factor \(L^{1/2}\) against \(L^3\), up to the implied constant.

The character-sum form of that energy is the reason it does not enlarge \(\theta\). Konyagin's Proposition 1.9 with \(k = 2\) gives \(|S| \le (q\,T_2/L)^{1/4}\). Substituting \(T_2 \le C L^{5/2}\) produces a bound of shape \(C^{1/4} q^{1/4} L^{3/8}\). The ratio of this shape to the trivial bound \(L\) is \(q^{1/4}/L^{5/8}\). At \(\theta = 0.16661157\), \(L = 3p\) and \(p \in \{1409, 3307\}\) the enclosure of \(q\) is \(\lambda^{\theta p}\), and \(q^{1/4}/L^{5/8}\) exceeds \(1\) by an exponential in \(p\). A fixed implied constant \(C\) moves the meeting point by \(\ln C/(p\ln\lambda)\). Closing a gap of width \(0.09\) would require \(\ln C\) of size \(p\), which is not an absolute constant. The graph count below has no such constant and gives the same conclusion with an explicit threshold.

## 4. The moment bound and the wrap

**Lemma 3 [P, cited].** For \(a \in \mathbb F_q^2\) with both coordinates nonzero, TRACE-279 Proposition N1.3 with the pair \((2,2)\) gives
\[
\frac{|S(a)|}{L} \le \Bigl(\frac{2q}{L^2}\Bigr)^{1/4},
\]
where \(S(a) = \sum_{j < L} e(a\cdot v_j/q)\). The input \(J_2 \le 2L^2\) is the odd case of Theorem 1, up to the \(-L\) which only improves the constant. TRACE-279 states that this \((2,2)\) bound does not beat the Weil bound. The comparison with the trivial bound \(|S| \le L\) is the condition \(q < L^2/2\).

**Proposition 4 [P, arithmetic].** The \((2,2)\) bound is strictly stronger than \(|S| \le L\) only for
\[
\theta < \frac{\ln(L^2/2)}{p\ln\lambda}.
\]
At arb precision \(200\), with \(L = 3p\):

| \(p\) | upper bound for this \(\theta\) |
| --- | --- |
| \(19\) | \(0.22073666\) |
| \(23\) | \(0.19177245\) |
| \(29\) | \(0.16116437\) |
| \(1409\) | \(0.00644413\) |
| \(3307\) | \(0.00303834\) |

For every prime \(p \ge 29\) and for both \(L = p\) and \(L = 3p\), this upper bound lies under the \(c = 1\) threshold \(0.16661157\). At \(p = 1409\) and \(p = 3307\), which are the conditional thresholds of v5, the \((2,2)\) bound is weaker than \(|S| \le L\) on the whole half-line \(\theta \ge 0.16661157\). The same holds with \(L = p\), where the meeting point is smaller. At \(p = 19\) and \(p = 23\), both below either conditional threshold, the meeting point for \(L = 3p\) sits above \(0.16661157\). Those two primes are the parked range. A character-sum saving there is not an input at \(p \ge p_{\mathrm{thr}}\).

The second moment of \(S\) itself has no saving to spend. Orthogonality gives \(\sum_a |S(a)|^2 = q^2 L\) whenever the \(L\) points are distinct, so the mean of \(|S|^2\) is \(L\). The fourth moment is \(\sum_a |S(a)|^4 = q^2 J_2\), and Theorem 1 puts the ratio of the mean fourth power to the square of the mean second power at \(J_2/L^2 < 2\). The mass is flat. Flatness is what produces the \((2,2)\) bound, and Proposition 4 is where that bound stops beating \(|S| \le L\).

**Proposition 5 [P].** The amplified loss exponent remains \(1\). The \(\theta\) range covered by the wrap at \(\ell_0 = p/4\) and \(\bar\rho \le 0.28\) remains
\[
\theta < 0.16661157.
\]

N16b (c2) charges a factor \(d\) for weights \(\asymp d/h\): positivity gives \(E_{\mathrm{coset}} \le d\cdot E_\Gamma\), and the weight sits outside the power \(\ell^3 \le \ell^2\), so the loss is \(d^1\). That factor is a weight, not an additive energy. Theorem 2 bounds \(J_2\), which is the second moment of the representation function of \(\Gamma+\Gamma\). The ratio \(J_2/L^3 < 2/L\) is a negative power of \(d\). Substituting that ratio for the factor \(d\) identifies the two second moments. Proposition 5 does not make that identification.

The arithmetic of the identification, kept separate from the proposition, is the threshold one would obtain by replacing the factor \(d\) with \(d\cdot(2/L)\):
\[
\theta < 0.16661157 + \frac{\ln(L/2)}{p\ln\lambda}.
\]
At \(L = 3p\) the upper endpoint of this sum is \(< 0.16969410\) for \(p = 1409\) and \(< 0.16807128\) for \(p = 3307\). Both lie under the first-moment threshold, whose lower end in the substitution of `proofs/h7_h8.md` Proposition 8 is \(> 0.26223963\). The gap remains open under the identification as well. At \(p = 19\) the same formal sum has upper endpoint \(< 0.26663201\), which sits above \(0.26223963\). That crossing is an arithmetic remark about a substitution this note does not justify, at a prime below \(p_{\mathrm{thr}}\).

The enclosures use the same \(\alpha(0.28)\) as `code/h7h8.py`. The ball reproduces the centre \(1.17477626638003325659\) recorded in `proofs/h7_h8.md`, and the ball for the \(c = 1\) threshold lies under \(0.16661156569722353507\). The log is `logs/h8_energy.json`.

## 5. Boundary

H8 remains open. The amplified wrap at \(\ell_0 = p/4\) covers \(\theta < 0.16661157\) and does not cover \(\theta \in (0.16661157,\ 0.26223963)\). Theorem 2 is the second-moment bound on \(\langle\lambda\rangle\): exponent \(2\), loss \(< 2/L\) against \(L^3\), uniform in every odd \(d\) with a split prime factor of equal order, with no cap at \(\sqrt{h_{3p}}\).

Outside Theorem 2: a modulus whose every split prime factor has strictly smaller order. The integers \(49\) and \(343\) are examples, with energies \(1617\) and \(122451\). An inert prime factor is outside Theorem 1. The census through \(p = 31\) has none.

H7* remains a hypothesis of v5. The aggregates at \(p = 19\) and \(p = 29\) stay undecided and are not used. H1, H3, and frozen R′ are untouched. The primes \(1409\) and \(3307\) are not recomputed.

The self-referee is `REFEREE_H8_ENERGY.md`.
