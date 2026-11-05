#!/usr/bin/env python3
"""Edit of record/claims.json for the H5 structural-ceiling arithmetic: new ids BGS-TRACE-348..351.
Next free id checked against origin/main 3995d691 (last BGS-TRACE-347) and the open PR branches #83, #84, #85
(none registers an id above BGS-TRACE-336)."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, pathlib
P = pathlib.Path('record/claims.json'); raw = P.read_text(encoding='utf-8'); d = json.loads(raw); cl = d['claims']; by = {c['id']: c for c in cl}
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
NEW = ['BGS-TRACE-348', 'BGS-TRACE-349', 'BGS-TRACE-350', 'BGS-TRACE-351']
assert not any(i in by for i in NEW) and 'BGS-TRACE-347' in by
assert max(int(c['id'].split('-')[-1]) for c in cl if c['id'].startswith('BGS-TRACE-')) == 347
V = 'computations/verification/h5_ceiling'; E = 'evidence/executions/20261105/h5_ceiling'
SRC = f'{V}/REPORT_H5_CEILING.md'; EV = [f'{E}/receipt.json']; LEAN = 'formalization/Bgs/H5CeilingArith.lean'
VER = [f'{V}/code/h5_arith.py', f'{V}/logs/h5_arith.json', f'{V}/logs/h5_arith.out']
REV = 'NO INDEPENDENT REFEREE (RE-DERIVED BY THE INTEGRATOR FROM research1105 AUDIT_H5A 1.3 / BYPASS 1.1-1.2)'
CONV = ("Convention (BGS-TRACE-342, Bgs.H6LemmaW): eps = 1 + sqrt2, epsbar = 1 - sqrt2, lambda = eps^2 = 3 + 2 sqrt2, eps^n = a_n + b_n sqrt2, "
        "h_n = (eps^n + epsbar^n)/2 = a_n (h_0 = h_1 = 1, h_{n+2} = 2 h_{n+1} + h_n; h_3 = 7, h_5 = 41, h_11 = 23 * 353); for odd p, h_p = u_{(p-1)/2} "
        "with u_0 = 1, u_1 = 7, u_{n+1} = 6 u_n - u_{n-1} (BGS-TRACE-344); Lean Bgs.H5CeilingArith.a_eq_h6 identifies a_n with Bgs.H6LemmaW.h n for every n. ")
NONCL = " Elementary arithmetic of the integers h_p only: no bound on any class sum; H5 (BGS-TRACE-303) stays open, Theorem R#-mod v5 (BGS-TRACE-325) stays conditional, nothing is claimed about R' (BGS-TRACE-206)."
a = dict(id='BGS-TRACE-348',
 title="Lemma W sharpened [P]: for an odd prime p and a prime q | h_p = (eps^p + epsbar^p)/2, eps = 1 + sqrt2: q = 1 (mod 2p) and q = +-1 (mod 8); the mod-8 part holds for every odd index n",
 source=SRC, dependencies=[],
 boundary=CONV + "[P] (REPORT_H5_CEILING section 1): h_n is odd, so q is odd; a_p^2 - 2 b_p^2 = -1 gives 2 b_p^2 = 1 (mod q), so s = 2 b_p is a square root of 2 mod q and q = +-1 (mod 8) (uses only p odd); "
 "for any such s, e = 1 + s is a unit (e(1 - s) = -1), e^p = b_p s, e^{2p} = 2 b_p^2 = 1 and e^2 - 1 = 2e != 0, so e^2 has order exactly p in F_q^*, p | q - 1 and, q and p odd, 2p | q - 1. "
 "Sharpens BGS-TRACE-342 (q = +-1 mod 2p; not edited, remains true): the inert branch of its proof never occurs because 2 is always a square mod q. "
 "[CA] (h5_arith.py, exact; no residue-class presieve): every prime q < 10^7 against every odd prime p <= 1500, 207 hits, each re-confirmed with the exact big integer h_p, 0 violations of q = 1 (mod 2p) and of q = +-1 (mod 8); complete factorisations for odd primes p <= 61 (sympy; factors above 2^64 are BPSW probable primes) satisfy both congruences and are squarefree. "
 "Lean (Bgs.H5CeilingArith.prime_dvd_mod2p, prime_dvd_mod8, orderOf_lambda; Mathlib; no sorry, no native_decide; axioms propext, Classical.choice, Quot.sound): general proof for every odd prime p, every prime q and every odd n (mod 8). Does not prove that h_p is squarefree." + NONCL,
 state='proved', ledger_status='PAPER PROOF [P] + LEAN GENERAL PROOF (Bgs.H5CeilingArith) + EXACT CHECK q < 1e7, p <= 1500, NO PRESIEVE (h5_arith.py) + ' + REV,
 external_dependencies=[], evidence=EV, verifiers=list(VER), formalization=[LEAN], manuscript=[],
 formalization_scope="Full for the arithmetic statement: Bgs.H5CeilingArith.prime_dvd_mod2p (q % (2p) = 1 for every odd prime p and prime q with q | a_p) and prime_dvd_mod8 (q % 8 in {1, 7} for every odd n); a_n is linked to Bgs.H6LemmaW.h by a_eq_h6.")
b = dict(id='BGS-TRACE-349',
 title="Coprimality [P]: gcd(h_p, h_p') = 1 for distinct odd primes p, p'; each prime q divides h_p for at most one odd prime p, namely the order of lambda modulo a prime of Z[sqrt2] above q",
 source=SRC, dependencies=['BGS-TRACE-348'],
 boundary=CONV + "[P] (REPORT_H5_CEILING section 2): if a prime q divides h_p and h_p', fix one square root s of 2 mod q (it exists by BGS-TRACE-348); the argument of BGS-TRACE-348 gives ord((1 + s)^2) = p and, with the same s, = p', so p = p'. "
 "[CA] (h5_arith.py, exact big-integer gcd): gcd = 1 for all 28,203 pairs of odd primes p < p' <= 1500; no prime q < 10^7 divides h_p for two different p. "
 "Lean (Bgs.H5CeilingArith.coprime_h; Mathlib; no sorry, no native_decide): general proof." + NONCL,
 state='proved', ledger_status='PAPER PROOF [P] + LEAN GENERAL PROOF (Bgs.H5CeilingArith) + EXACT CHECK ALL PAIRS p < p\' <= 1500 (h5_arith.py) + ' + REV,
 external_dependencies=[], evidence=EV, verifiers=list(VER), formalization=[LEAN], manuscript=[],
 formalization_scope="Full: Bgs.H5CeilingArith.coprime_h (Int.gcd (a p) (a p') = 1 for distinct odd primes p, p').")
c = dict(id='BGS-TRACE-350',
 title="Sophie Germain family [P]: if p = 3 (mod 4) and 2p + 1 is prime then (2p + 1) | h_p, the least prime factor of h_p is exactly 2p + 1 and h_p is composite for p >= 5; conversely, for odd p with 2p + 1 prime, (2p + 1) | h_p forces p = 3 (mod 4); 25 such p in [5, 1500], exactly the p there with least prime factor 2p + 1",
 source=SRC, dependencies=['BGS-TRACE-348'],
 boundary=CONV + "[P] (REPORT_H5_CEILING section 3): (i) q = 2n + 1 = 7 (mod 8), so 2 has a square root s mod q and e = 1 + s is a unit; Fermat gives e^{2n} = 1; with A = a_n, B = b_n and 2B^2 = A^2 + 1, e^{2n} - 1 = 2A e^n (the image of lambda^n - 1 = 2 h_n eps^n), so A = 0 mod q; this needs only n = 3 (mod 4), not n prime. "
 "(ii) by the mod-8 part of BGS-TRACE-348, an odd n = 1 (mod 4) gives q = 3 (mod 8), impossible. (iii) every prime factor of h_p is = 1 (mod 2p), hence >= 2p + 1; h_p >= 2^{p-1} > 2p + 1 for p >= 5. "
 "[CA] (h5_arith.py, exact): for every odd prime p <= 1500, (2p+1) | h_p iff (p = 3 mod 4 and 2p+1 prime), no mismatch; trial division of h_p by all primes <= 2p + 1 finds no divisor other than 2p + 1; for 5 <= p <= 1500 the family is {11, 23, 83, 131, 179, 191, 239, 251, 359, 419, 431, 443, 491, 659, 683, 719, 743, 911, 1019, 1031, 1103, 1223, 1439, 1451, 1499} (25), equal to the set of p with least prime factor 2p + 1. "
 "Lean (Bgs.H5CeilingArith.sg_dvd, sg_iff, sg_minFac; Mathlib; no sorry, no native_decide): general proofs. Infinitude of the family is the open Sophie Germain problem; no density of bad or good p follows." + NONCL,
 state='proved', ledger_status='PAPER PROOF [P] + LEAN GENERAL PROOF (Bgs.H5CeilingArith) + EXACT CHECK p <= 1500 (h5_arith.py) + ' + REV,
 external_dependencies=[], evidence=EV, verifiers=list(VER), formalization=[LEAN], manuscript=[],
 formalization_scope="Full for (i)-(iii): Bgs.H5CeilingArith.sg_dvd (n % 4 = 3, 2n+1 prime -> (2n+1) | a_n), sg_iff, sg_minFac (Nat.minFac |a_p| = 2p + 1 and 2p + 1 < |a_p| for p >= 5); the count 25 for p <= 1500 is the Python check only.")
dd = dict(id='BGS-TRACE-351',
 title="Product formula [P]: h_n = prod_{k=1}^{(n-1)/2} (6 - 2 cos(2 pi k/n)) for every odd n >= 1",
 source=SRC, dependencies=[],
 boundary=CONV + "[P] (REPORT_H5_CEILING section 4): with zeta = e^{2 pi i/n}, (lambda^n - 1)/(lambda - 1) = prod_{k=1}^{n-1} (lambda - zeta^k); for odd n, lambda^n - 1 = 2 h_n eps^n and lambda - 1 = 2 eps, so the left side is h_n lambda^{(n-1)/2}; "
 "pairing k with n - k and lambda + 1/lambda = 6 gives (lambda - zeta^k)(lambda - zeta^{-k}) = lambda (6 - 2 cos(2 pi k/n)). "
 "[N] (h5_arith.py, mpmath 80 digits): every odd n, 3 <= n <= 301, maximal relative error 3.3e-80. Not formalized in Lean." + NONCL,
 state='proved', ledger_status='PAPER PROOF [P] + FLOAT CHECK [N] 80 DIGITS, ODD n <= 301 (h5_arith.py) + ' + REV,
 external_dependencies=[], evidence=EV, verifiers=list(VER), formalization=[], manuscript=[])
i = max(k for k, x in enumerate(cl) if x['id'] == 'BGS-TRACE-347') + 1
cl[i:i] = [a, b, c, dd]; d['updated'] = '2026-11-05'
P.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'); print('ok', len(cl))
