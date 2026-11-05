# H5 after Lemma W: the factorisation room

Tags in this file are local to the note. **[P]** is proved here, or is an external theorem with the locator named in the sentence. **[P-arith]** is the idealised gas-versus-Robin arithmetic of `code/crossover_sharp.py`, repeated at the same inputs in `code/h5_factor.py` at 80 decimal places. **[P, finite]** is a complete factorisation by trial division. A finite factorisation is a theorem about those integers. It is not an asymptotic statement about \(h_p\). `record/claims.json` was not edited. The statements of BGS-TRACE-303 and BGS-TRACE-342 are read from `origin/main`.

## 0. The two statements

**H5, BGS-TRACE-303, open.** For composite \(h_p\): (a) the mixed classes, \(E_{\mathrm{mixed},d} F_p \le e^{o(p)} d^c r_2^p\) with \(c < 0.387\), uniformly in \(d \mid h_p\); (b) the \(2^{\omega(h_p)} - 2\) cross lines; (c) the partially isotropic points. Or else \(p \in \mathcal P = \{h_p \text{ prime}\}\). The closure is: prove (a)–(c), or prove \(\mathcal P\) infinite. Infinitude of \(\mathcal P\) is equivalent to the failure of \(R_{\mathrm{NSW}}\), BGS-TRACE-210.

**Lemma W, BGS-TRACE-342, proved.** For odd primes \(p\) and \(q\) with \(q \mid h_p = (\varepsilon^p + \bar\varepsilon^p)/2\), \(\varepsilon = 1+\sqrt 2\): \(q \equiv \pm 1 \pmod{2p}\). Hence \(p \nmid h_p\), the \(j\)-th smallest prime factor of \(h_p\) is at least \(pj - 1\), and
\[
\omega(h_p) \le w_{\max}(p) := \max\bigl\{w : (p-1)^w\, w! \le \varepsilon^p\bigr\}.
\]
The proof is REPORT_P4_v2 §2.1. The product step there is \(\prod_{j\le w}(p-1)j \le h_p < \varepsilon^p\). Squarefreeness is not part of the lemma. Squarefreeness is H6, BGS-TRACE-304.

**Where v5 spends the factorisation.** THEOREM_DRAFT_v5 §1–2. The level-\(h_p\) sum carries \(S_\rho\,(n/h_p)\,(|1+X+Y|^2 - 1)\). At composite \(h_p\), \(X\) contains the \(2^{\omega(h_p)}-2\) cross lines, which the gas does not code (N7-F6). \(Y = Y_U + Y_{\mathrm{mix}} +\) the partially isotropic points. The quantity \(B_p\) subtracts \(|X_{\mathrm{cross}}|\), \(|Y|\), \(|X_{\mathrm{tail}}|\) and \(e^{-0.28p}\) inside one parenthesis, before the square. The structural demand is \(B_p \ge \kappa > 0\) for infinitely many primes \(p \ge p_{\mathrm{thr}}\). On \(\mathcal P\) the three composite clauses vanish. Off \(\mathcal P\) they are the clauses of H5.

The crossover that produces the conditional primes \(3307\) (H1 constant \(C \le 0.082\), \(\delta_{\mathrm{eff}} \le 3.4962\cdot 10^{-4}\)) and \(1409\) (\(C \le 8.8\cdot 10^{-4}\), \(\delta_{\mathrm{eff}} \le 7.4115\cdot 10^{-6}\)) sets tails \(= Y = X_{\mathrm{cross}} = \varepsilon = 0\) and \(n/h_p := 1\). v5 records that the additive budget has not been computed. The slack in §3 is that idealised slot, evaluated with the model tail \(e^{-0.28p}\) put back in. It is not the full budget.

## 1. The omega bound is already a theorem

Let \(h_p\) be the NSW number, \(h_3 = 7\), \(h_5 = 41\), and \(h_p = 6h_{p'} - h_{p''}\) along odd indices. Write \(w_\sharp(p) = \max\{w : (p-1)^w\, w! \le h_p\}\) and \(c_\sharp(p) = \max\{w : (p-1)^w \le \varepsilon^p\}\).

**Theorem 1 [P, cited TRACE-342].** For every odd prime \(p\),
\[
\omega(h_p) \le w_\sharp(p) \le w_{\max}(p) \le c_\sharp(p) < \frac{p}{\ln(p-1)}.
\]
In particular \(\omega(h_p) < p/\ln(p-1)\). Any constant \(C \ge 1\) satisfies \(\omega(h_p) \le C\, p/\ln(p-1)\).

The first inequality is the product in REPORT_P4_v2 §2.1: distinct prime factors occupy distinct slots \(\ge (p-1)j\), so their product is at least \((p-1)^\omega \omega!\), and that product divides \(h_p\) only after the primes themselves are inserted, hence is at most \(h_p\). The registry form uses \(\varepsilon^p\) in place of \(h_p\), which only enlarges the cap. Dropping \(w!\) enlarges it again, and \((p-1)^{c_\sharp(p)} \le \varepsilon^p\).

The comparison with \(p/\ln(p-1)\) is elementary. The series \(1+1+1/2+1/6+1/24 = 163/60 > 8/3\), since \(489 > 480\), so \(e > 8/3\). And \((8/3)^2 = 64/9 > 6 \ge 3 + 2\cdot(3/2) \ge 3+2\sqrt 2 = \varepsilon^2\), so \(\varepsilon < 8/3 < e\) and \(\ln\varepsilon < 1\). Thus \((p-1)^{c_\sharp(p)} \le \varepsilon^p < e^p\), and \(c_\sharp(p)\ln(p-1) < p\).

Exact values, from `code/h5_factor.py`, integer comparison of \((p-1)^{2w}(w!)^2\) with \(\lambda^p = \varepsilon^{2p}\):

| \(p\) | \(w_\sharp\) | \(w_{\max}\) | \(c_\sharp\) |
|---|---|---|---|
| \(1409\) | \(112\) | \(112\) | \(171\) |
| \(3307\) | \(231\) | \(231\) | \(359\) |

At these two primes the factorial and the passage from \(h_p\) to \(\varepsilon^p\) do not move the integer. The shape \(O(p/\ln p)\) is the theorem. It is not a new constraint on top of Lemma W.

## 2. The cap exceeds the gas main term

Let \(R = 6234/10^{7}\), the decimal \(6.234\cdot 10^{-4}\) used as \(\operatorname{Re}\Lambda_{\mathrm{lo}}'\). The gas factor is \(b = (1+R)e^{-\delta}\) with \(\delta \ge 0\), so \(b < 1+R\) and the main term \(M = 2b^p - 1\) satisfies \(M < 2(1+R)^p < 2e^{pR}\).

**Theorem 2 [P].** \(2^{w_{\max}(1409)} > 2e^{1409\, R}\) and \(2^{w_{\max}(3307)} > 2e^{3307\, R}\). The Taylor bound of `code/h5_factor.py` with forty terms gives the stricter display
\[
2e^{1409\, R} < 5 < 2^{112}, \qquad 2e^{3307\, R} < 16 < 2^{231}.
\]
Hence \(2^{w_{\max}(p)}\) exceeds \(M\) at both conditional primes, for every \(\delta \ge 0\).

The same comparison holds far past those primes, with a weaker coefficient than \(w_{\max}\) itself.

**Theorem 3 [P].** For every integer \(n\) with \(2000 \le n \le e^{170}\),
\[
w_{\max}(n) \ge \frac{n}{6\ln n} - 1,
\]
and \(2^{w_{\max}(n)} > 2(1+R)^n\). Here \(w_{\max}(n)\) is the same maximum with \(p\) replaced by \(n\).

Let \(s = \lceil \ln n\rceil\) and \(w = \lfloor n/(3s)\rfloor\). For increasing \(f\), \(\sum_{k=1}^{w-1} f(k) \le \int_1^w f\), so
\[
\ln(w!) \le w\ln w - w + 1 + \ln w.
\]
Then
\[
w\ln(n-1) + \ln(w!) \le w\ln(n-1) + w\ln w + 1 + \ln w.
\]
Here \(w \le n/(3s)\) and \(\ln(n-1) \le s\), so the first summand is at most \(n/3\). Also \(n \le e^s \le 3s\, e^s\), so \(\ln(n/(3s)) \le s\) and \(w\ln w \le n/3\). The logarithm of \(w\) contributes at most \(s+1\). The total is at most \(2n/3 + s + 1\).

Now \(\ln\varepsilon > 4/5\). Indeed \(e < 3\), so \(e^4 < 81\), and \(40^2 = 1600 < 1682 = 2\cdot 29^2\), so \(40 < 29\sqrt 2\) and \(81 < 41 + 29\sqrt 2 = (1+\sqrt 2)^5\). Thus \(e^4 < \varepsilon^5\). The gap \(4/5 - 2/3 = 2/15\) gives
\[
n\ln\varepsilon - \bigl(2n/3 + s + 1\bigr) \ge \tfrac{2n}{15} - s - 1.
\]
For \(n \ge 2000\), \(s \le \ln n + 1\). Since \(e > 8/3\) and \((8/3)^4 = 4096/81 > 49\) (because \(4096 > 3969\)), \(e^8 > (8/3)^8 > 2401 > 2000\), so \(\ln 2000 < 8\) and \((2/15)\cdot 2000 > 10\). The derivative of \((2/15)n - \ln n - 2\) is \(2/15 - 1/n > 0\) for \(n > 15\), so \((2/15)n > \ln n + 2\) on the whole range, and the difference is positive. Hence \((n-1)^w w! < \varepsilon^n\) and \(w_{\max}(n) \ge w\). Since \(s \le \ln n + 1\) and \(\ln n \ge 1\),
\[
w \ge \frac{n}{3(\ln n+1)} - 1 \ge \frac{n}{6\ln n} - 1.
\]

It remains to beat \(2(1+R)^n\). From \(w_{\max}(n) \ge n/(6\ln n) - 1\),
\[
2^{w_{\max}(n)} \ge 2^{n/(6\ln n) - 1}.
\]
The inequality \(2^{n/(6\ln n) - 1} > 2(1+R)^n\) rearranges to
\[
\Bigl(\frac{n}{6\ln n} - 2\Bigr)\ln 2 > n\ln(1+R).
\]
Since \(\ln(1+x) < x\) for \(x > 0\), it is enough that
\[
\frac{\ln 2}{6\ln n} - \frac{2\ln 2}{n} > R.
\]
The left side is decreasing on \([2000, e^{170}]\). Its derivative has the sign of \(2/n - 1/(6\ln^2 n)\), and \(n > 12\ln^2 n\) throughout the interval: at \(n = 2000\) one has \(\ln 2000 < 8\) and \(12\cdot 64 = 768 < 2000\), and \(n/\ln^2 n\) increases once \(\ln n > 2\). The minimum lies at the right endpoint. There \(\ln n \le 170\) and \(n \ge e^{11}\), so the left side exceeds
\[
\frac{\ln 2}{1020} - \frac{2\ln 2}{e^{11}}.
\]
Three rational bounds close this. The Taylor upper bound of \(\exp(693/1000)\) is \(< 2\), so \(\ln 2 > 693/1000\). The partial sum of \(\exp(7/10)\) exceeds \(2\), so \(\ln 2 < 7/10\). And \(e > 8/3\), so \(e^{11} > (8/3)^{11}\). Therefore
\[
\frac{\ln 2}{1020} - \frac{2\ln 2}{e^{11}} > \frac{693/1000}{1020} - \frac{2\cdot(7/10)}{(8/3)^{11}},
\]
and the right-hand side exceeds \(R\). The positive difference is the field `endpoint_margin` of `logs/h5_factor.json`. The left side of the displayed inequality exceeds \(R\).

So on the whole interval the Lemma W cap is already larger than the gas main term. The range \(e^{170}\) is where this coefficient \(1/6\) stops beating \(R\). It is not the root of the sharp \(w_{\max}\). The sharp count is larger, and the obstruction is stronger.

## 3. The idealised room at the conditional primes

Under \(n/h_p := 1\) and with \(\varepsilon_{16} = \varepsilon_{\mathrm{fl}} = \varepsilon_{\mathrm{other}} = 0\), positivity of the idealised \(B_p\) requires
\[
\bigl(M - |X_{\mathrm{cross}}| - |Y| - |X_{\mathrm{tail}}| - e^{-0.28p}\bigr)^2 - 1 > I_p,
\]
where \(M = 2(1+R)^p e^{-p\delta} - 1\) and \(I_p \le e^\gamma \ln\ln K_p + 0.6483/\ln\ln K_p - 1\), \(K_p = 4h_p^2 + 3\), Robin 1984, Theorem 2, as used in `code/crossover_sharp.py`. Giving the whole slot to \(|X_{\mathrm{cross}}|\) and setting the other three subtractions except the model tail to zero, the room is
\[
\operatorname{slack} = M - e^{-0.28p} - \sqrt{1+I_p}.
\]

**Proposition 4 [P-arith].** At 80 decimal places, with the same \(R\) and the same Robin expression:

| \(p\) | \(\delta\) | slack |
|---|---|---|
| \(1409\) | \(3.4962\cdot 10^{-4}\) | \(< -1.80\) |
| \(3307\) | \(3.4962\cdot 10^{-4}\) | \(< 0.00334719\) |
| \(1409\) | \(7.4115\cdot 10^{-6}\) | \(< 0.02011297\) |
| \(3307\) | \(7.4115\cdot 10^{-6}\) | \(< 10.38716\) |

The first row is below the crossover: at the fragile \(\delta\), the idealised \(B_p\) is already negative at \(p = 1409\). The two threshold rows are the fragile room at \(3307\) and the robust room at \(1409\). Both are smaller than \(2\). The fourth row is the robust \(\delta\) evaluated at the larger prime, where the gas has pulled ahead of Robin by about \(10\).

**Consequence for the count.** Lemma W permits up to \(2^{112}-2\) cross lines at \(p = 1409\) and up to \(2^{231}-2\) at \(p = 3307\). Both numbers exceed the corresponding main term, by Theorem 2, and exceed the slack by a larger factor. A bound \(|X_{\mathrm{cross}}| \le (2^{\omega}-2)\, L\) fits in the threshold room only if
\[
L < \frac{\operatorname{slack}}{2^{w_{\max}(p)}-2}.
\]
At both conditional primes the right side is \(< 2^{-100}\). No such per-line bound is proved. N7-F6 records that each cross line carries the full weight \(n_d\), and that the lines at \(p \le 41\) are numerically small. Those ratios are [N] in N7 and N8b. They are not a bound at \(p \ge 1409\).

If one assumes, which this note does not, that each cross line contributes at most \(1\), the threshold rooms still force \(\omega = 1\): two lines already exceed \(0.00334719\) and \(0.02011297\). At \(p = 3307\) with the robust \(\delta\), the same assumption allows \(\omega \le 3\), because \(2^3-2 = 6 < 10.38716\) and \(2^4-2 = 14 > 10.38716\), against a cap of \(231\).

The phrase \(2^{\omega} = e^{o(p)}\) is true under Theorem 1, since \(w_{\max}(p) = o(p)\), and it does not put the count inside \(\exp(\rho p)\) with \(\rho = \ln(1+R)-\delta \approx 2.7\cdot 10^{-4}\) or \(6\cdot 10^{-4}\). An \(e^{o(p)}\) of the shape \(\exp(c p/\ln p)\) dominates \(\exp(\rho p)\) for every \(p\) in Theorem 3.

## 4. The mixed-class cutoff is not implied

N14b Lemma 2 is \(c_B = 0.7375\), [P-sketch], BGS-TRACE-320. The sketch controls the mixed classes when every proper divisor of \(h_p\) is at most \(1.588^p\). That is the condition \(q_{\min}(h_p) \ge h_p/1.588^p\). The exponent \(c < 0.387\) is what the budget asks for at \(\theta = 1/2\). The sketch does not reach it: \(0.7375 > 0.387\).

**Theorem 5 [P].** For \(p \in \{31, 1409, 3307\}\),
\[
h_p > (2p-1)\Bigl(\frac{397}{250}\Bigr)^p.
\]
The integer \(397/250\) is the printed cutoff \(1.588\). Lemma W allows a least prime factor as small as \(2p-1\). The cofactor \(h_p/(2p-1)\) then exceeds \(1.588^p\). The ratio is greater than \(10^{252}\) at \(p = 1409\) and greater than \(10^{597}\) at \(p = 3307\) (`logs/h5_factor.json`, field `log10_ratio`). In the scale \(d = \lambda^{\theta p}\), that cofactor has
\[
\theta > 0.49652 \quad (p = 1409), \qquad \theta > 0.49837 \quad (p = 3307).
\]
Both lie above \(0.262\), which is the \(\theta\)-form of the cutoff \(1.588^p\), and above the \(0.387\) budget's design point only in the sense that they sit near \(1/2\), where the sketch's exponent does not meet \(c < 0.387\).

Lemma W therefore does not force the hypothesis of the sketch. The least prime factor it guarantees, \(2p-1\), leaves a proper divisor at \(\theta \to 1/2\).

## 5. The primes up to \(47\), by trial division

**Proposition 6 [P, finite].** For every odd prime \(p \le 47\), trial division of \(h_p\) is complete, \(h_p\) is squarefree, and every prime factor \(q\) satisfies \(q \equiv \pm 1 \pmod{2p}\). The factorisations are:

| \(p\) | \(h_p\) | \(\omega\) | \(\theta\) of the largest proper divisor |
|---|---|---|---|
| \(3\) | \(7\) | \(1\) | — |
| \(5\) | \(41\) | \(1\) | — |
| \(7\) | \(239\) | \(1\) | — |
| \(11\) | \(23\cdot 353\) | \(2\) | \(0.30255\) |
| \(13\) | \(79\cdot 599\) | \(2\) | \(0.27908\) |
| \(17\) | \(103\cdot 15607\) | \(2\) | \(0.32221\) |
| \(19\) | \(9369319\) | \(1\) | — |
| \(23\) | \(47\cdot 6771937\) | \(2\) | \(0.38794\) |
| \(29\) | \(63018038201\) | \(1\) | — |
| \(31\) | \(424577\cdot 865087\) | \(2\) | \(0.25017\) |
| \(37\) | \(223\cdot 37223\cdot 8761009\) | \(3\) | \(0.40647\) |
| \(41\) | \(2297\cdot 302663\cdot 3553471\) | \(3\) | \(0.38332\) |
| \(43\) | \(19609\cdot 153511\cdot 4783321\) | \(3\) | \(0.36046\) |
| \(47\) | \(489133282872437279\) | \(1\) | — |

The value \(\theta\) is \(\log_\lambda\) of that divisor, divided by \(p\), at 80 decimal places. Full digits are in the log. Among these composites, only \(p = 31\) has \(\theta < 0.262\). That is the semiprime N14b already marks as covered by the sketch and not by \(\mathcal P\). The others have \(\theta\) from \(0.279\) to \(0.406\), outside the sketch's cutoff. Squarefreeness on this finite set does not touch H6.

## 6. What v5 needs, and what remains

The omega bound of Theorem 1 is unconditional and has the shape asked for. It does not replace H5. The three clauses spend the factorisation in three different ways, and the bound is too weak for each of them.

**(a) Mixed classes.** The weakest condition the existing sketch uses is: every proper divisor of \(h_p\) is at most \(1.588^p\). Equivalently, \(q_{\min}(h_p) \ge h_p/1.588^p\). Theorem 5 says Lemma W does not imply this at either conditional prime, nor at \(p = 31\) in the worst slot \(q_{\min} = 2p-1\). The actual factorisation at \(p = 31\) happens to lie inside the cutoff; the lemma does not force the next composite to do so. Even on the set where the cutoff holds, \(c_B = 0.7375\) is a sketch, and the budget asks for \(c < 0.387\). Upgrading the sketch is the closure of BGS-TRACE-320. It is open.

**(b) Cross lines.** The weakest condition compatible with a per-line bound \(L\) is \(2^{\omega(h_p)}-2 < \operatorname{slack}(p)/L\), with the slack of Proposition 4. At the conditional thresholds the slack is \(< 0.00334719\) and \(< 0.02011297\). Theorem 1 allows \(\omega = 112\) and \(\omega = 231\). Closing (b) requires a per-line bound smaller than \(2^{-100}\) at those primes, or a factorisation condition much stronger than Lemma W: under a hypothetical per-line bound \(L \le 1\), the threshold rooms require \(h_p\) prime. No per-line bound of either size is proved. The lines are not coded by the gas (N7-F6).

**(c) Partially isotropic points.** Lemma W does not bound them. They remain as stated in TRACE-303.

**The alternative, \(\mathcal P\) infinite.** This is the other branch of H5, and it is the branch on which (a)–(c) vanish and \(B_p\) reduces to the idealised gas, still conditional on H1, H6's \(p_0\), H7* and H8. Infinitude of \(\mathcal P\) is equivalent to the failure of \(R_{\mathrm{NSW}}\) (TRACE-210, as named in the closure of TRACE-303). It is open.

A positive-density statement is not available from Lemma W. The lemma forbids prime factors outside two residue classes modulo \(2p\), and forbids prime factors below \(2p-1\). That is a restriction on the factors of a single \(h_p\). It does not produce a prime value. The sieves that produce primes apply to linear forms. The value \(h_p\) is a term of a binary recurrence, of size \(\varepsilon^p\). No theorem of that sieve type has those hypotheses. Density zero is the shape of the usual prime-value heuristic, \(\sum_p 1/\ln h_p \asymp \sum_p 1/p\), which diverges and would give infinitude rather than positive density inside the primes. That heuristic is not a theorem, and this note does not use it as one. The closure condition that is actually on the page is infinitude of \(\mathcal P\), and it remains open.

**Squarefreeness** stays H6. Lemma W does not prove it. Proposition 6 is a finite check.

**Not claimed.** H5 is not discharged and not replaced. \(B_p \ge \kappa\) for infinitely many \(p\) is not proved. \(\mathcal P\) is not proved infinite. The additive budget of v5, beyond the idealised slack of Proposition 4, is not computed. Frozen R′ is untouched.
