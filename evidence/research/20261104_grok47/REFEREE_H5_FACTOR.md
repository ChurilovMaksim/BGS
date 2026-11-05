# Self-referee of the H5 factorisation note

Read against `proofs/h5_factor.md`, `code/h5_factor.py` and `logs/h5_factor.json`. Each item is a way the argument can be misread or can fail, followed by the check that was actually made.

## 1. The omega bound is Lemma W, and it does not replace H5

The failure mode is to read \(\omega(h_p) < p/\ln(p-1)\) as a discharge of TRACE-303.

Theorem 1 is the product in REPORT_P4_v2 §2.1, plus \(\varepsilon < e\). The exact caps are \(w_{\max}(1409) = 112\) and \(w_{\max}(3307) = 231\), equal to the sharper cap against \(h_p\). Proposition 4 gives the idealised room at those primes as \(< 0.00334719\) and \(< 0.02011297\). The count \(2^{112}-2\) and \(2^{231}-2\) exceeds both rooms. H5 stays open.

## 2. \(e^{o(p)}\) is not absorbed by the gas

The failure mode is to see \(w_{\max} = o(p)\) and conclude that \(2^{w_{\max}}\) fits under \(\exp(\rho p)\) with \(\rho \approx 10^{-4}\).

Theorem 2 is an integer comparison at the two conditional primes: \(2e^{pR} < 5 < 2^{112}\) and \(< 16 < 2^{231}\). Theorem 3 extends the same comparison to every integer up to \(e^{170}\), with the weaker coefficient \(1/6\). The shape \(\exp(c p/\ln p)\) dominates \(\exp(\rho p)\) on that range. The root of the sharp \(w_{\max}\) is not computed, and it is not claimed to lie at \(e^{170}\).

## 3. The slack is the idealised slot

The failure mode is to quote Proposition 4 as the additive budget of v5.

v5 sets tails \(= Y = X_{\mathrm{cross}} = \varepsilon = 0\) and \(n/h_p := 1\), and records that the budget has not been computed. The slack puts the model tail \(e^{-0.28p}\) back in and gives the whole remaining slot to \(|X_{\mathrm{cross}}|\), still at \(n/h_p := 1\) and with the three \(\varepsilon\) terms at \(0\). A negative result in that generous slot remains a negative result. It is not a computation of the budget.

The row \(p = 1409\), \(\delta = 3.4962\cdot 10^{-4}\), has negative slack. That pair lies below the crossover. It is not used as a room.

## 4. The per-line bound of size \(1\) is not a theorem

The failure mode is to turn the sentence "under a per-line bound \(L \le 1\), the threshold rooms require \(h_p\) prime" into a proved bound on a cross line.

N7-F6 says each line carries the full weight \(n_d\). The numerical smallness at \(p \le 41\) is [N] there. This note uses \(L \le 1\) only as a comparison with the slack. The proved statement is the opposite direction: fitting the Lemma W count into the slack would require \(L < 2^{-100}\) at both conditional primes, and no such \(L\) is proved.

## 5. Lemma W does not force the mixed-class cutoff

The failure mode is to treat \(c_B = 0.7375\) as a theorem on the set \(q_{\min} \ge 2p-1\), or to treat the cutoff \(d \le 1.588^p\) as a consequence of TRACE-342.

Theorem 5 is the integer comparison \(h_p > (2p-1)(397/250)^p\) at \(p \in \{31, 1409, 3307\}\). The cofactor at the Lemma W floor has \(\theta > 0.49652\) and \(\theta > 0.49837\). TRACE-320 stays a sketch, and \(0.7375\) does not meet \(c < 0.387\). The factorisation of \(h_{31}\) does lie under \(\theta = 0.262\). That is one integer, read off the complete factorisation, and it is the example N14b already records.

## 6. The finite factorisation is not H6, and it is not a sieve

The failure mode is to export squarefreeness from \(p \le 47\), or to read the absence of a sieve theorem as a proof that \(\mathcal P\) is finite.

Proposition 6 is trial division. Every prime factor found is \(\equiv \pm 1 \pmod{2p}\), which agrees with Lemma W on this set and does not re-prove it. Squarefreeness remains BGS-TRACE-304. Infinitude of \(\mathcal P\) remains the closure of BGS-TRACE-303, equivalent there to the failure of BGS-TRACE-210. No positive-density theorem is stated.

## 7. The rational checks that the uniform range uses

The failure mode is a slipped constant in Theorem 3: \(\ln 2\), \(e^{11}\), or the sign of the derivative.

`logs/h5_factor.json` records \(\exp(693/1000) < 2\), a partial sum of \(\exp(7/10)\) above \(2\), \(163/60 > 8/3\), \(40^2 < 2\cdot 29^2\), and a positive `endpoint_margin` for
\[
\frac{693/1000}{1020} - \frac{2\cdot(7/10)}{(8/3)^{11}} - R.
\]
The spot checks \(w_{\max}(1409) \ge 58\), \(w_{\max}(2000) = 151 \ge 83\) and \(w_{\max}(3307) \ge 122\) match \(\lfloor n/(3s)\rfloor\). Those spots are not the proof of the interval. The proof is the integral bound in §2.
