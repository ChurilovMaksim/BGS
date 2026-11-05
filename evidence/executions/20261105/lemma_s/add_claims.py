#!/usr/bin/env python3
"""Edit of record/claims.json for Lemma S, the polymer gap lemma, the Binet generator and the H5(b) constant:
new ids BGS-TRACE-352..355 (referee-confirmed results of research1105b, in the referee's corrected statements).
Next free id checked against origin/main 6f69baa1 (last BGS-TRACE-351) and the open PR branches #83, #84, #85
(none registers an id above BGS-TRACE-336).  Run from the repository root."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, pathlib
P = pathlib.Path('record/claims.json'); raw = P.read_text(encoding='utf-8'); d = json.loads(raw); cl = d['claims']; by = {c['id']: c for c in cl}
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
NEW = ['BGS-TRACE-352', 'BGS-TRACE-353', 'BGS-TRACE-354', 'BGS-TRACE-355']
assert not any(i in by for i in NEW) and 'BGS-TRACE-351' in by
assert max(int(c['id'].split('-')[-1]) for c in cl if c['id'].startswith('BGS-TRACE-')) == 351
assert by['BGS-TRACE-303']['state'] == 'open' and by['BGS-TRACE-304']['state'] == 'open' and by['BGS-TRACE-325']['state'] == 'conditional'
V = 'computations/verification/lemma_s'; E = 'evidence/executions/20261105/lemma_s'
SRC = f'{V}/REPORT_LEMMA_S.md'; EV = [f'{E}/receipt.json']; LEAN = 'formalization/Bgs/LemmaSArith.lean'
REF = 'REFEREE-CONFIRMED (independent internal referee research1105b REFEREE.md, copied to evidence/research/20261105_lemma_s/REFEREE.md; not external)'
CONV = ("Convention (BGS-TRACE-342/348): eps = 1 + sqrt2, epsbar = 1 - sqrt2 = -1/eps, lambda = eps^2, O = Z[sqrt2], h_p = (eps^p + epsbar^p)/2 for an odd prime p "
        "(h_11 = 23 * 353, h_13 = 79 * 599, h_17 = 103 * 15607). Line setting (REPORT_LEMMA_S section 0; grok47 h5_xline): a line is an ideal abar of O with O/abar = Z/h_p and lambda^p = 1 mod abar; "
        "eps^p = s_q in {+1, -1} mod each prime q of abar; abar_+- = product of the primes with s_q = +-1, d_+- = N(abar_+-); Binet line iff min(d_+, d_-) = 1, cross line otherwise; "
        "if h_p is squarefree (H6, BGS-TRACE-304, open) the lines are the 2^omega ideals of norm h_p with one prime above each q | h_p and d_+ d_- = h_p. "
        "Height G(x) = min{max(|rho|, |rho'|) : rho = x mod abar} = min{|a| + sqrt2 |b| : a + b sqrt2 = x mod abar}. ")
NONCL = (" No bound on X_line, X_cross or any class sum is claimed; the seam-decay threshold r < 0.418, the seam-cost and counting inputs and every [N]/[H]/[C] item of the source are not registered. "
         "H5 (BGS-TRACE-303) stays open, H6 (BGS-TRACE-304) stays open, Theorem R#-mod v5 (BGS-TRACE-325) stays conditional, nothing is claimed about R' (BGS-TRACE-206).")
a = dict(id='BGS-TRACE-352',
 title="Lemma S on cross lines [P]: if abar = abar_+ abar_- (coprime, odd norms d_+, d_- > 1), eps^p = +1 mod abar_+ and -1 mod abar_-, and sigma is the side with d_sigma = max(d_+, d_-), then G(c eps^n) + G(c eps^{n+p}) >= sqrt(max(d_+, d_-)) for every n and every class c not in abar_{-sigma}; on the axis sub-line 0 != c in abar_{-sigma} only G >= sqrt(min(d_+, d_-)) holds; the consequence max(d_+, d_-) >= sqrt(h_p) uses squarefree h_p and is conditional on H6 (BGS-TRACE-304)",
 source=SRC, dependencies=[],
 boundary=CONV + "[P] (REPORT_LEMMA_S section 1; research1105b REPORT section 4.2, re-derived by the referee, item 1): minimal representatives rho_1 = c eps^n, rho_2 = c eps^{n+p} satisfy abar_+ | rho_2 - rho_1 and abar_- | rho_2 + rho_1; "
 "rho_2 - rho_1 = -2 c eps^n != 0 mod abar_- when c is not in abar_- (2, eps units at odd primes), so d_+ N(gcd(c, abar_-)) <= |N(rho_2 - rho_1)| <= (G_1 + G_2)^2, and symmetrically; "
 "general form (G_1 + G_2)^2 >= d_+ N(gcd(c, abar_-)) whenever c is not in abar_-, and with + and - exchanged. "
 "Scope caveat (referee): the classes 0 != c in abar_{-sigma} form a Binet-type sub-line of level d_sigma (eps^p acts by the single sign sigma, G(c eps^{n+p}) = G(c eps^n)) on which only G >= sqrt(min(d_+, d_-)) holds; "
 "so the source's 'no hypothesis on P^-(h_p) is needed for the vacuum part' holds only off this axis sub-line, where the smallest-prime ceiling returns through sqrt(min(d_+, d_-)). "
 "Conditional consequence: with h_p squarefree (H6, BGS-TRACE-304, open) d_+ d_- = h_p, hence max(d_+, d_-) >= sqrt(h_p) and G_1 + G_2 >= h_p^{1/4} off the axis sub-line; without H6 this is not claimed. "
 "[CA] (lemmaS_exact.py, exhaustive over all h classes of every line, heights in float64 with margins >= 3%): p = 11, 13, 17 (h = 23 * 353, 79 * 599, 103 * 15607; omega = 2, 2 cross lines each): "
 "the bound holds for every class outside abar_{-sigma} and the gcd form on every class; Q = min over primitive x of max(G(x), G(x eps^p)) = 15.2426, 21.7990, 68 and Q/sqrt(d_sigma) = 0.8113, 0.8907, 0.5443; "
 "min over primitive x of (G_1 + G_2)/sqrt(d_sigma) = 1.1618, 1.3261, 1.0345 (within 3.5% of equality at p = 17); axis sub-line minima of G = 6.414, 10.414, 15.243 against sqrt(min) = 4.796, 8.888, 10.149; Binet lines Q = 1. "
 "omega >= 3 (first case p = 37) is not tested; the proof does not depend on omega. "
 "Lean (Bgs.LemmaSArith.ht_eq_max, norm_le_ht, ht_sub_le, ht_add_le, lemmaS_core_sub, lemmaS_core_add, axis_bound, mul_le_max_sq; Mathlib; no sorry, no native_decide; axioms propext, Classical.choice, Quot.sound): "
 "the height/norm inequalities (d | N(rho_2 -+ rho_1) != 0 implies d <= (G(rho_1) + G(rho_2))^2) and d_+ d_- <= max(d_+, d_-)^2; the ideal-theoretic steps are not formalized." + NONCL,
 state='proved', ledger_status='PAPER PROOF [P] + ' + REF + ' + LEAN PARTIAL (Bgs.LemmaSArith: height/norm inequalities) + EXHAUSTIVE CHECK p = 11, 13, 17 (lemmaS_exact.py); max(d_+, d_-) >= sqrt(h_p) CONDITIONAL ON H6',
 external_dependencies=[], evidence=EV, verifiers=[f'{V}/code/lemmaS_exact.py', f'{V}/logs/lemmaS_exact.json', f'{V}/logs/lemmaS_exact.out'], formalization=[LEAN], manuscript=[],
 formalization_scope="Partial: Bgs.LemmaSArith.ht_eq_max (max(|a + b sqrt2|, |a - b sqrt2|) = |a| + sqrt2 |b|), norm_le_ht, ht_sub_le, ht_add_le, lemmaS_core_sub/add (the final inequality of the proof), axis_bound (G^2 >= d on a nonzero element with d | N), mul_le_max_sq; not the ideal divisibility, the nonvanishing mod abar_- or the gcd factor.")
b = dict(id='BGS-TRACE-353',
 title="Polymer gap lemma, explicit constant [P]: on a cross line (setting of BGS-TRACE-352), omega = zeta_p^{(p+1)/2}, if f = F(omega) lies in the line lattice with F = sum_{k<=K} a_k x^k in Z[x], |a_k| <= A, and f is not divisible by eta_+ eta_- = omega^4 - 6 omega^2 + 1 = zeta^2 - 6 zeta + 1, then K > log_eps min(d_+, d_-) - 2 log_eps A - 1.214 (exact constant log_eps(eps^2/2) = 1.21356...)",
 source=SRC, dependencies=['BGS-TRACE-352'],
 boundary=CONV + "[P] (REPORT_LEMMA_S section 2; research1105b REPORT section 4.3 with the constant made explicit by the referee, item 2): on a line omega -> lambda^{(p+1)/2} = eps eps^p = s_q eps at each prime, so f in the lattice means F(eps) in abar_+ and F(-eps) in abar_-; "
 "if F(eps) = F(-eps) = 0 then the monic x^2 - 2x - 1 and x^2 + 2x - 1 divide F in Z[x] (Gauss) and f is in (eta_+ eta_-); otherwise d_+ <= |N F(eps)| or d_- <= |N F(-eps)|; "
 "|F(+-eps)| < A eps^{K+1}/sqrt2, |F(+-epsbar)| < A/(2 - sqrt2), 1/(sqrt2 (2 - sqrt2)) = eps/2, so |N F(+-eps)| < A^2 eps^{K+2}/2 and K > log_eps min(d_+, d_-) - 2 log_eps A - log_eps(eps^2/2), log_eps(eps^2/2) = 2 - log_eps 2 = 1.21356 < 1.214. "
 "Caveats (referee): (i) the statement concerns the chosen integer polynomial F (representatives differ by Phi_p(x)-multiples; the implication holds for every representative); "
 "(ii) (eta_+ eta_-) contains short vectors: zeta^2 - 6 zeta + 1 (l1 = 8) lies in every line lattice, cross lines included; (iii) only min(d_+, d_-) enters, so for the 2p+1 family (BGS-TRACE-350) the bound is about log_eps(2p + 1), nearly vacuous; "
 "(iv) |X_cross| <~ poly(p) min(d_+, d_-)^{-gamma} is [H] and not claimed; '-O(log A)' of the source reads '-2 log_eps A - O(1)'. "
 "[CA] (polymer_const.py): the constant at 60 digits; exhaustive over all nonzero coefficient vectors with (A, K) in {(1, <= 9), (2, <= 5), (3, <= 3)}, both signs, exact integer norms: |N F(sigma eps)| < A^2 eps^{K+2}/2, largest ratio 0.976 (A = 1, K = 9). "
 "Lean (Bgs.LemmaSArith.polymer_norm_lt, polymer_gap, polymer_gap_of_norm, logb_const_lt, logb_const_gt; Mathlib; no sorry, no native_decide; decide +kernel for eps^103 < 2^131 and 2^75 < eps^59 via h_103, h_59): "
 "the norm bound for every K, A > 0 and sigma = +-1, the logarithmic form, and 1.213 < log_eps(eps^2/2) < 1.214; the divisibility step and the lattice membership are not formalized." + NONCL,
 state='proved', ledger_status='PAPER PROOF [P] + ' + REF + ' + LEAN PARTIAL (Bgs.LemmaSArith: norm bound, logarithmic form, constant) + EXACT CHECK (polymer_const.py)',
 external_dependencies=[], evidence=EV, verifiers=[f'{V}/code/polymer_const.py', f'{V}/logs/polymer_const.json', f'{V}/logs/polymer_const.out'], formalization=[LEAN], manuscript=[],
 formalization_scope="Partial: Bgs.LemmaSArith.polymer_norm_lt (|F(sigma eps)| |F(sigma epsbar)| < A^2 eps^{K+2}/2), polymer_gap / polymer_gap_of_norm (K > log_eps d - 2 log_eps A - log_eps(eps^2/2) from d <= |N F(sigma eps)|), logb_const_lt / logb_const_gt (1.213 < log_eps(eps^2/2) < 1.214); not the Gauss divisibility step or the ideal membership.")
c = dict(id='BGS-TRACE-354',
 title="Binet lattice generator [P]: for an odd prime p, s = +-1 and omega = zeta_p^{(p+1)/2}, eta_s = omega^2 - 2 s omega - 1 = zeta - 1 - 2 s zeta^{(p+1)/2} has N_{Q(zeta_p)/Q}(eta_s) = +h_p, N(zeta^2 - 6 zeta + 1) = h_p^2, and (eta_s) is the Binet-line lattice in Z[zeta_p] (kernel of zeta -> lambda into O/abar, abar = (Phi_p(s eps)), eps^p = s mod abar); in Z[x]/(x^p - 1) the line lattice is (eta_s) + (Phi_p(x)) and (eta_s) alone has index 2 h_p",
 source=SRC, dependencies=[],
 boundary=CONV + "[P] (REPORT_LEMMA_S section 3; research1105b REPORT section 4.1, proof by the referee, item 4): the roots of x^2 - 2 s x - 1 are s eps, s epsbar, so N(eta_s) = prod_omega (omega - s eps)(omega - s epsbar) = Phi_p(s eps) Phi_p(s epsbar) = N_{Q(sqrt2)/Q}(Phi_p(s eps)) = h_p "
 "((eps^p - 1)(epsbar^p - 1) = -2 h_p, (eps - 1)(epsbar - 1) = -2; (eps^p + 1)(epsbar^p + 1) = 2 h_p, (eps + 1)(epsbar + 1) = 2); on the Binet line omega -> eps^{p+1} = s eps, so eta_s -> eps^2 - 2 eps - 1 = 0; "
 "no rational prime divides Phi_p(s eps) (it would give eps^p = epsbar^p = s mod q against eps^p epsbar^p = -1), so O/abar = Z/h_p, the map Z[zeta] -> Z/h_p is onto and [Z[zeta] : kernel] = h_p = |N(eta_s)|, hence kernel = (eta_s); "
 "N(zeta^2 - 6 zeta + 1) = Phi_p(lambda) Phi_p(lambdabar) = h_p^2; |Res(x^p - 1, eta_s)| = |eta_s(1)| h_p = 2 h_p, so in the word model Z[x]/(x^p - 1) (Theorem 6 of grok47 h5_xline) 'lattice = (eta_s)' is exact only modulo the all-ones word Phi_p(x); "
 "'3-site' means three eps-sites (omega^0, omega^1, omega^2), i.e. lambda-sites 0, 1, (p+1)/2, not lambda-local. Squarefreeness of h_p is not used. "
 "[CA] (eta_check.py, exact): N(eta_+) = N(eta_-) = h_p and N(zeta^2 - 6 zeta + 1) = h_p^2 by sympy resultants for all 20 primes 3 <= p <= 73; Phi_p(s eps) Phi_p(s epsbar) = h_p in exact Z[sqrt2] arithmetic for every odd prime p <= 1500; "
 "on every line for p <= 43 (up to 8 lines): eta_s -> 0 exactly on the Binet line of sign s, neither eta_s vanishes on a cross line, zeta^2 - 6 zeta + 1 -> 0 on every line; |Res(x^p - 1, eta_s)| = 2 h_p for every prime 5 <= p <= 43. "
 "Lean (Bgs.LemmaSArith.h_closed, phi_eps, phi_neg_eps, phi_lambda, prod_eta, prod_kernel; Mathlib; no sorry, no native_decide; axioms propext, Classical.choice, Quot.sound): "
 "Phi_n(+-eps) Phi_n(+-epsbar) = h_n and Phi_n(lambda) Phi_n(lambdabar) = h_n^2 for every odd n, and for every odd prime p the products over all primitive p-th roots of unity mu in C: prod (mu^2 - 2 s mu - 1) = h_p (s = +-1), prod (mu^2 - 6 mu + 1) = h_p^2; "
 "the identification of these products with the field norm of Q(zeta_p)/Q, the kernel/index argument and the index 2 h_p are not formalized." + NONCL,
 state='proved', ledger_status='PAPER PROOF [P] + ' + REF + ' + LEAN PARTIAL (Bgs.LemmaSArith: norm as product over conjugates, every odd prime p) + EXACT CHECK p <= 73 RESULTANTS, p <= 43 ALL LINES (eta_check.py)',
 external_dependencies=[], evidence=EV, verifiers=[f'{V}/code/eta_check.py', f'{V}/logs/eta_check.json', f'{V}/logs/eta_check.out'], formalization=[LEAN], manuscript=[],
 formalization_scope="Partial: Bgs.LemmaSArith.phi_eps, phi_neg_eps, phi_lambda (N_{Q(sqrt2)/Q} Phi_n(+-eps) = h_n, N Phi_n(lambda) = h_n^2, every odd n), prod_eta and prod_kernel (the products of eta_s and zeta^2 - 6 zeta + 1 over all primitive p-th roots of unity in C equal h_p and h_p^2, every odd prime p); not the equality with Algebra.norm, the lattice equality (eta_s) = kernel, or the index 2 h_p in Z[x]/(x^p - 1).")
dd = dict(id='BGS-TRACE-355',
 title="H5(b) cross-line sufficiency at p = 1409 and p = 3307 (conditional; constant [CA]): a uniform bound |X_line| <= C e^{-c p} on every cross line with C <= 1 and c >= 0.058 fits the 2^omega - 2 cross lines into the idealised room of grok47 h5_factor Prop. 4 at p = 1409 (robust delta) and p = 3307 (fragile delta); the source's c > 0.048 is wrong",
 source=SRC, dependencies=['BGS-TRACE-342'],
 boundary=CONV + "[P + CA] (REPORT_LEMMA_S section 4; referee item 3, corrected statement): a uniform bound |X_line| <= C e^{-c p} on all cross lines discharges the cross-line part (b) of H5 (BGS-TRACE-303) at p if (2^{omega(h_p)} - 2) C e^{-c p} < slack(p) - |Y| - |X_tail| "
 "(the idealised slack already subtracts e^{-0.28 p}); unconditionally in omega (Lemma W, BGS-TRACE-342, omega <= w_max(p)) it suffices that c > [ln(2^{w_max(p)} - 2) + ln C + ln(1/room)]/p. "
 "Inputs: the idealised room of grok47 h5_factor.md Prop. 4 (n/h_p = 1, eps_16 = eps_fl = eps_other = 0, |Y| = |X_tail| = 0): slack(1409, robust delta) = 0.0201129656, slack(3307, fragile delta) = 0.0033471848, "
 "an UNREGISTERED research note (branch research-grok46-1104 @ f7986a9f, PR #85, draft), copied, not recomputed. "
 "[CA] (h5b_const.py): w_max(1409) = 112 and w_max(3307) = 231 by exact integer comparison of (p - 1)^w w! with eps^p (the source's 228 is wrong); with C = 1 the thresholds are c > 0.05787 (p = 1409, binding) and c > 0.05014 (p = 3307); "
 "c = 0.058, C = 1 gives (2^112 - 2) e^{-0.058 * 1409} = 0.01675 < 0.02011 and (2^231 - 2) e^{-0.058 * 3307} = 1.7e-14 < 0.00335, so c >= 0.058 suffices for every C <= 1; larger C costs ln C/p; "
 "under the crude line count 2^{p/ln(p-1)} the thresholds are 0.0984 and 0.0873. The source's c > 0.048 is wrong (w_max 228 instead of 231, room ignored, binding prime 1409 skipped). "
 "The hypothesis is OPEN and is not supplied by BGS-TRACE-352/353: lines with small min(d_+, d_-) (min = 2p + 1 occurs, BGS-TRACE-350) and the axis sub-line are controlled only through min(d_+, d_-). "
 "With nonzero additive budgets |Y|, |X_tail| the threshold rises by ln(slack/(slack - |Y| - |X_tail|))/p. Not formalized in Lean." + NONCL,
 state='conditional', ledger_status='CONDITIONAL [P + CA] + ' + REF + ' (source constant 0.048 corrected to 0.058) + EXACT w_max AND mpmath THRESHOLDS (h5b_const.py); ROOM INPUT FROM UNREGISTERED RESEARCH NOTE (grok47 h5_factor Prop. 4, PR #85)',
 external_dependencies=[], evidence=EV, verifiers=[f'{V}/code/h5b_const.py', f'{V}/logs/h5b_const.json', f'{V}/logs/h5b_const.out'], formalization=[], manuscript=[],
 closure_condition="Prove the uniform cross-line bound |X_line| <= C e^{-c p} with C <= 1 and c >= 0.058 on every cross line at p = 1409 and p = 3307 (in particular on lines with small min(d_+, d_-) and on the axis sub-line, which BGS-TRACE-352/353 do not control), register the idealised room of grok47 h5_factor Prop. 4, and bound the additive budgets |Y|, |X_tail| of BGS-TRACE-325; or show that no such bound holds.")
i = max(k for k, x in enumerate(cl) if x['id'] == 'BGS-TRACE-351') + 1
cl[i:i] = [a, b, c, dd]; d['updated'] = '2026-11-05'
P.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'); print('ok', len(cl))
