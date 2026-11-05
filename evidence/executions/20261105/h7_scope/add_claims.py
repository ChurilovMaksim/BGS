#!/usr/bin/env python3
"""Hand-edit of record/claims.json for the H7* scope integration (PR #85 grok47 results, referee-confirmed): new ids 344..347.
Next free id checked against origin/main 5d67f21c (last BGS-TRACE-343) and the open PR branches #83, #84, #85 (none registers >= 344)."""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, pathlib
P = pathlib.Path('record/claims.json'); raw = P.read_text(encoding='utf-8'); d = json.loads(raw); cl = d['claims']; by = {c['id']: c for c in cl}
assert json.dumps(d, indent=2, ensure_ascii=False) + '\n' == raw
NEW = ['BGS-TRACE-344', 'BGS-TRACE-345', 'BGS-TRACE-346', 'BGS-TRACE-347']
assert not any(i in by for i in NEW) and 'BGS-TRACE-343' in by
assert max(int(c['id'].split('-')[-1]) for c in cl if c['id'].startswith('BGS-TRACE-')) == 343
V = 'computations/verification/h7_scope'; E = 'evidence/executions/20261105/h7_scope'
SRC = f'{V}/REPORT_H7_SCOPE.md'; EV = [f'{E}/receipt.json']; LEAN = 'formalization/Bgs/H7KpArith.lean'
REF = (f'INDEPENDENT REFEREE AUDIT ({E}/referee/AUDIT.md; HOSTILE REFEREE, NOTHING WRONG; ITEMS 1a, 1c, 2a-2c, 3a, 3b, 4b CONFIRMED; '
       'NEEDS FIX 1b, 2d, 3c, 4a, 4c, 4d APPLIED IN REPORT_H7_SCOPE.md AND notes/)')
SCOPE = ("Scope: k1 kick 0.9 cos 2 pi q at eta = 2 (ghat(n) = i^n J_n(1.8)), S = [[3,4],[2,3]], lambda = 3+2 sqrt2 = eps^2 (eps = 1+sqrt2), "
         "frozen definition of BGS-TRACE-206; u_0 = 1, u_1 = 7, u_{n+1} = 6 u_n - u_{n-1}, h_p = u_{(p-1)/2}, K_p = 4 h_p^2 + 3, h_{3p} = h_p K_p (BGS-TRACE-265); T' = 1.42785. ")
a = dict(id='BGS-TRACE-344',
 title="H7* arithmetic [P]: for every prime p >= 5, 7 | K_p = 4 h_p^2 + 3 and 7 does not divide h_p; gcd(h_p, K_p) = 1; every prime factor of K_p is = 1 (mod 3)",
 source=SRC, dependencies=['BGS-TRACE-265'],
 boundary=SCOPE + "[P] (REPORT_H7_SCOPE section 1; notes/h7_h8.md Lemmas 3, 4, checked by hand by the referee). Lemma 4: mod 7, u_{n+1} = -u_n - u_{n-1}, so 7 | u_n iff n = 1 (mod 3) iff p = 3 (mod 6), i.e. only p = 3 (K_3 = 199 = 3 mod 7); for p >= 5, h_p = +-1 and K_p = 0 (mod 7). "
 "Lemma 3: mod 3 the sequence 1, 1, 2, 2, ... never vanishes, so 3 does not divide h_p and gcd(h_p, K_p) | 3 is 1; a prime q | K_p has (2h_p)^2 = -3 (mod q); q = 2 is impossible because K_p is odd, q = 3 is excluded, and (-3/q) = (q/3) gives q = 1 (mod 3). "
 "Exact-integer check for all 301 primes 5 <= p < 2000 (kp_arith.py; referee ints.py independently): 7 | K_p, 7 not | h_p, 3 not | h_p, K_p odd, gcd = 1, u_{(3p-1)/2} = h_p K_p. "
 "Lean (Bgs.H7KpArith.seven_dvd_K, decide +kernel, no sorry, no native_decide): the same five facts for primes 5 <= p < 200; finite check only. "
 "Extends BGS-TRACE-265 (7 | K_p checked there for p = 5..23 only). The rank-3p and q = 1 (mod 6p) congruences (TRACE-265, N8b) are not re-proved. Does not bound Lin_d at any level and does not touch H7* (BGS-TRACE-305).",
 state='proved', ledger_status='PAPER PROOF [P] + EXACT CHECK p < 2000 (kp_arith.py; REFEREE ints.py) + LEAN FINITE CHECK p < 200 (Bgs.H7KpArith) + ' + REF,
 external_dependencies=[], evidence=EV,
 verifiers=[f'{V}/code/kp_arith.py', f'{V}/logs/kp_arith.json', f'{V}/code/h7h8.py', f'{V}/logs/h7h8.json', f'{E}/referee/ints.py', f'{E}/referee/ints.out'],
 formalization=[LEAN], manuscript=[],
 formalization_scope="Partial: Bgs.H7KpArith.seven_dvd_K checks 7 | K_p, 7 not | h_p, 3 not | h_p, gcd(h_p, K_p) = 1 and h_{3p} = h_p K_p for the primes 5 <= p < 200 only; Lemmas 3 and 4 for every prime are paper proofs, not formalized.")
b = dict(id='BGS-TRACE-345',
 title="H7* included K_p-levels [P, finite, exact integers]: complete factorisations of K_p for primes 5 <= p <= 31; the conductors 3437426497, 24061985479 | K_19 and 2735635252619983 | K_29 are coprime to h_p with floor(h_{3p}/d^2) = 278, 5, 133 (included by TRACE-273), ord_d(lambda) = 3p; d = 4663 | K_7 is included (4663^2 <= h_21, order 21)",
 source=SRC, dependencies=['BGS-TRACE-265', 'BGS-TRACE-273', 'BGS-TRACE-344'],
 boundary=SCOPE + "[P, finite] (REPORT_H7_SCOPE section 2; exact integers). K_5 = 7 * 31^2, K_7 = 7^2 * 4663, K_11 = 7 * 37667521, K_13 = 7 * 313 * 4088137, K_17 = 7 * 409 * 3610372009, K_19 = 7 * 457 * 14593 * 7521721, K_23 = 7 * 57887325592525441, "
 "K_29 = 7 * 13921 * 5806729 * 28073057689, K_31 = 7 * 2643247 * 7159513 * 4073551591; every factor < 2^64 is prime (sympy BPSW, deterministic below 2^64; h7h8.py trial division), = 1 (mod 3), and = 1 (mod 6p) except 7; h_p is prime exactly for p = 5, 7, 19, 29. "
 "Included K_p-divisors other than 7 (d | K_p, d^2 <= h_{3p}): 31, 217 (p = 5; 31^2 = 961 > sqrt(h_15)); 49, 4663 (p = 7); ten at p = 19 (457 ... 24061985479); ten at p = 29 (13921 ... 2735635252619983); twelve at p = 31; none at p = 11, 23. "
 "Crossing conductors: 3437426497 = 457 * 7521721 and 24061985479 = 7 * 457 * 7521721 divide K_19, 2735635252619983 = 7 * 13921 * 28073057689 divides K_29; gcd(d, h_p) = 1 (so d is neither h_p nor e h_p), floor(h_{3p}/d^2) = 278, 5, 133, gcd(beta, d) = 1 for beta = (-208,0), (227,227), (-89,0); hence included by TRACE-273. "
 "ord_d(lambda) = 3p for all 24 included conductors at p = 5, 7, 19, 29, including 4663 (order 21; omitted from the PR #85 target list, referee fix 2d; not searched). "
 "Lean (Bgs.H7KpArith.K_factorisations, crossings, d4663; decide +kernel): the products, the residues mod 3 and 6p, divisibility, gcd, floors and orders; primality of the factors is not checked in Lean. Finite statement about these integers only; no bound on any Lin_d.",
 state='proved', ledger_status='EXACT FINITE COMPUTATION [P, finite] (kp_arith.py, h7h8.py; REFEREE ints.py, ints2.py) + LEAN FINITE CHECK (Bgs.H7KpArith) + ' + REF,
 external_dependencies=[], evidence=EV,
 verifiers=[f'{V}/code/kp_arith.py', f'{V}/logs/kp_arith.json', f'{V}/code/h7h8.py', f'{V}/logs/h7h8.json', f'{E}/referee/ints.py', f'{E}/referee/ints2.py', f'{E}/referee/ints2.out'],
 formalization=[LEAN], manuscript=[],
 formalization_scope="Partial: Bgs.H7KpArith checks the factorisation products for p = 5..31, the residues of the factors mod 3 and 6p, the divisibility, gcd, floor(h_{3p}/d^2) and order-3p facts for the three crossing conductors and for 4663; primality of the factors and the full included-divisor lists are not formalized.")
c = dict(id='BGS-TRACE-346',
 title="H7* crossings on the finite vertex section [CA, finite section only]: on the TRACE-223 multi-disc vertex operator compressed to |c| <= 3, 40 modes, |n| <= 16, the sector-0 per-step spectral radius of one lambda-orbit exceeds T' = 1.42785 at d = 3437426497 (>= 1.4587724663), 24061985479 (>= 1.5119805975) and 2735635252619983 (>= 1.4686852948); edge comparison and trace-vs-radius are numerical only; the untruncated operator is not claimed",
 source=SRC, dependencies=['BGS-TRACE-221', 'BGS-TRACE-223', 'BGS-TRACE-273', 'BGS-TRACE-345'],
 boundary=SCOPE + "Object: the compression of the TRACE-223 multi-disc VERTEX transfer operator (certG_build_sector.py conventions: rho = 1.2, C = -1/(4 sqrt2)) to centres |c| <= 3, monomials of degree < 40 and letters |n| <= 16 (dimension 280; core forward-invariant, 19/lambda < 3.26). "
 "Per-step rate r = rho(prod_{j<P} L_{a/8 + tau_j})^{1/P}, tau_j = Tr(beta lambda^j)/d mod 1, P = ord_d(lambda). "
 "[CA] (h7_multidisc_cert.py enclose, arb precision 320, Newton-Kantorovich with every error sum in ball arithmetic and directed float conversion, h <= 1.8e-14; rerun 2026-11-05): sector a = 0, d = 3437426497, beta = (-208,0), P = 57: r in [1.4587724663901533, 1.4587724663901547]; "
 "d = 24061985479, beta = (227,227), P = 57: [1.511980597518887, 1.5119805975188885]; d = 2735635252619983, beta = (-89,0), P = 87: [1.4686852948918225, 1.468685294891824]; each > T' (gaps 0.03092, 0.08413, 0.04083). "
 "Independent referee re-enclosure (Krawczyk/Brouwer box test, own orbit/trace/product, arb; krawczyk.py, rerun at integration): d = 3437426497 in [1.45877246639015403, 1.45877246639015426]. "
 "Level-7 calibration against BGS-TRACE-223 on the same section: class 2:1 (a = 4) [1.2835951329030864, 1.2835951329030906] inside the TRACE-223 disc [1.2835950326, 1.2835952326]; class 1:3 (a = 6) upper 1.2837142953109817 <= 1.2837144; class 0:1 (a = 0, referee Krawczyk) upper 1.2624306304893 <= 1.2624308. "
 "One-step tail section -> core < 9.65e-5 [P, arb]; it is NOT a monodromy bound. NOT CLAIMED: the untruncated (core or full) operator; the edge operator (floated only, rates ~0.35) and hence the edge comparison [N]; trace versus spectral radius [N] (|mu_2/mu_1| ~ 2e-16 numerically, other eigenvalues not bounded); any bound on the aggregate sum_beta kappa_d(N beta) Zhat(beta). Finite section, three orbits, one sector only.",
 state='proved', ledger_status='COMPUTER-ASSISTED [CA] (ARB, python-flint 0.9.0; FINITE SECTION ONLY; NEWTON-KANTOROVICH WITH ARB ERROR SUMS, RERUN 2026-11-05) + INDEPENDENT REFEREE KRAWCZYK RE-ENCLOSURE (krawczyk.py) + LEVEL-7 CALIBRATION AGAINST TRACE-223 + ' + REF,
 external_dependencies=[], evidence=EV,
 verifiers=[f'{V}/code/h7_multidisc_cert.py', f'{V}/code/h7_rates.py', f'{V}/logs/h7_multidisc_enclose.json', f'{E}/referee/mine/krawczyk.py', f'{E}/referee/mine/krawczyk_d34.json', f'{E}/referee/mine/krawczyk_l7_21_l7_13_l7_01.json'],
 formalization=[], manuscript=[])
dd = dict(id='BGS-TRACE-347',
 title="H7* scope note [P on TRACE-346; no state change]: the per-orbit sufficient reading of H7* (growth < T') cannot be certified on the finite vertex section at the three included levels d | K_19, K_29; the aggregate H7* (TRACE-305) stays open; Theorem R#-mod v5 (TRACE-325) is unaffected (hypotheses needed at infinitely many primes; p_thr >= 1409 > 29); 18 included conductors remain unsearched",
 source=SRC, dependencies=['BGS-TRACE-305', 'BGS-TRACE-325', 'BGS-TRACE-345', 'BGS-TRACE-346'],
 boundary=SCOPE + "[P on TRACE-346] (REPORT_H7_SCOPE section 4; notes/h7_scope.md, referee safe wording). (1) The closure condition of TRACE-305 is the aggregate bound |Lin_d| <= eps_d |Z_rho|^2/h_p with sum eps_d <= kappa0; 'cross-correlation growth < T'' in its title is a sufficient per-orbit majorant ((sum |kappa|) max |Zhat|). "
 "On the finite vertex section of TRACE-346 that per-orbit sufficient reading fails at d = 3437426497, 24061985479 (p = 19) and 2735635252619983 (p = 29): a per-orbit cap at T' cannot be certified from this section. The edge comparison and trace-vs-radius are [N] only; the untruncated operator is not claimed. "
 "(2) The aggregate H7* (TRACE-305) stays OPEN, neither proved nor refuted at these levels: no enclosure of sum_beta kappa_d(N beta) Zhat(beta) exists there and one orbit is one term. TRACE-305 is not edited (state, title, boundary, closure condition unchanged; no amendment entry needed). "
 "(3) Theorem R#-mod v5 (TRACE-325) is unaffected: its hypotheses (H0, H1, H5-H8 at p and B_p >= kappa > 0) are required for infinitely many primes p >= p_thr (the draft's P-subsequence form, THEOREM_DRAFT_v5 line 128, likewise needs P infinite), so a failure at the finitely many primes 19, 29 can neither fire nor block it; independently p_thr >= p_1 >= 1409 > 29 (3307 fragile / 1409 robust). "
 "(4) Not exhausted: 18 included conductors, d = 4663 (p = 7, not searched) and the seventeen at p = 19, 29 of notes/h7_rates.md section 8. Frozen R' (TRACE-206) stays open and is not refuted.",
 state='proved', ledger_status='SCOPE NOTE [P ON TRACE-346] (NO STATE CHANGE: TRACE-305 OPEN, TRACE-325 CONDITIONAL, TRACE-206 OPEN) + ' + REF,
 external_dependencies=[], evidence=EV,
 verifiers=[f'{V}/notes/h7_scope.md', f'{V}/notes/h7_multidisc.md', f'{V}/notes/h7_rates.md'],
 formalization=[], manuscript=[])
i = max(k for k, x in enumerate(cl) if x['id'] == 'BGS-TRACE-343') + 1
cl[i:i] = [a, b, c, dd]; d['updated'] = '2026-11-05'
P.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8'); print('ok', len(cl))
