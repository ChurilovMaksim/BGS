#!/usr/bin/env python3
"""Append BGS-TRACE-337..341 (span theorem integration, 4 Nov 2026) to record/claims.json. No existing row is modified."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[5]
P = ROOT / 'record/claims.json'
d = json.loads(P.read_text(encoding='utf-8')); cl = d['claims']; ids = {c['id'] for c in cl}
assert not ids & {f'BGS-TRACE-{i}' for i in range(337, 342)}
SRC = 'mathematics/fixed-map/lineN_span_theorem.md'
EV = ['evidence/executions/20261104/span_theorem/receipt.json']
V = 'computations/verification/lineN_span'
LEAN = ['formalization/Bgs/LineNSpanArith.lean']
REF = ('INDEPENDENT REFEREE AUDIT (evidence/executions/20261104/span_theorem/referee/AUDIT.md; HOSTILE AUDIT OF PR #83 WITH PR #85 AND '
       'P2 CROSS-CHECKS, 4 NOV 2026: CONFIRMED AFTER THE FIXES APPLIED IN THE SOURCE NOTE)')
CONV = ('Setting: alpha = a + b sqrt2 in Z[sqrt2] \\ {0}, eps = 1 + sqrt2, lambda = eps^2, N(alpha) = a^2 - 2b^2, shell j: 2^j <= |N| < 2^{j+1}; '
        'mu = (sqrt2/4) alpha, theta_k = sigma+(mu) eps^k, conj theta_k = sigma-(mu) conj(eps)^k, theta_k + conj theta_k = T_k in Z, '
        '|theta_k conj theta_k| = |N|/8; red(x) = x - floor(x + 1/2) in [-1/2, 1/2), n_k = floor(theta_k + 1/2), '
        'E_k = n_k - 2 n_{k-1} - n_{k-2}; span = length of the word from the first to the last nonzero E_k; L(alpha) = log_eps(|N|/2); '
        'c_eps = log 2 / log eps = 0.786440 (0.7864397013573949). ')
def C(i, title, deps, boundary, state, ledger, verifiers, formal=(), fscope=None, closure=None):
    c = dict(id=f'BGS-TRACE-{i}', title=title, source=SRC, dependencies=[f'BGS-TRACE-{x}' for x in deps], boundary=CONV + boundary,
             state=state, ledger_status=ledger, external_dependencies=[], evidence=EV, verifiers=list(verifiers),
             formalization=list(formal), manuscript=[])
    if fscope: c['formalization_scope'] = fscope
    if closure: c['closure_condition'] = closure
    return c
new = [
 C(337, 'Span theorem (Theorem A): for every nonzero alpha in Z[sqrt2], log_eps(|N(alpha)|/2) + 1 < span(alpha) < log_eps(|N(alpha)|/2) + 3; all balanced eps-digits lie in {-1, 0, 1}; span = K_R - K_L + 3 except on the class of sqrt2 (span 2)',
  [],
  '[P] (PR #85 span_law.md Lemmas 1-6 for the statement, the exact formula and the lower bound; upper bound by the two-lift argument of P2 Lemma S, '
  'with the PR #83 floor-form derivation recorded as a secondary proof after its slips were fixed: red range [-1/2, 1/2), the comparison with 2j via '
  '8 < 32 < eps^4 = 17 + 12 sqrt2 (225 < 288), equality of the norm form floor(L) + 3 at alpha = 2, shell form floor(c_eps j) + 3 attained first in shell 2 '
  'by 3 + sqrt2). K_L = min{k : |theta_k| >= 1/2}, K_R = max{k : |conj theta_k| >= 1/2}. The span is a class invariant (alpha -> +-eps^k alpha). '
  'Corollary B (near-sharpness only): neither constant 1 nor 3 can be improved by more than 3.4e-4 (witnesses 82 sqrt2 and 116, BGS-TRACE-339); '
  'it is NOT claimed that 1 and 3 are the best constants. Corollary C (shell form): span < c_eps j + 3, so span <= floor(c_eps j) + 3 for j >= 1 and '
  '<= 2j for j >= 2. Corollary D: the Prop. K exclusion length span + g0 < c_eps j + 3 + g0 for every class in shell j (replaces the N20 [P-sketch] '
  'span <= 2j for j >= 5; prior idea: N20 section 3.4 sketch span <= 0.787 j + O(1)). Finite check [exact integers, not part of the proof]: all 81709 '
  'fundamental-domain classes through shell 16 (span_census.py), span - floor(L) histogram {2: 43304, 3: 38405}, 0 letters outside {-1,0,1}, '
  '0 failures of the exact formula or of the strict two-sided bound. Does not bound |r_A r_B|, does not prove H1 (BGS-TRACE-336), H3 or R-prime.',
  'proved', 'PROVED [P] + EXACT FINITE CENSUS THROUGH SHELL 16 + LEAN ARITHMETIC FOR THE eps^4 STEP (Bgs.LineNSpan.eps4, eps4_gt_32) + ' + REF,
  [f'{V}/code/span_census.py', f'{V}/logs/span_census_J16.json'], LEAN,
  'Partial: only eps^4 = 17 + 12 sqrt2 and 225 < 288 (integer model); Theorem A and its corollaries are not formalised.'),
 C(338, 'Span theorem Lemma 8: on fundamental-domain representatives the project word of digits.eps_digits (lineN14) equals the balanced digit word of BGS-TRACE-337, so its span is the span of Theorem A',
  [337],
  '[P] (PR #85 Lemmas 7-8): the B-embedding of the seeds (2a, 2b) is -theta_{-1}; even sites are red(theta_{2t}), odd sites -red(-theta_{2t-1}); '
  'a half-integer theta_k forces alpha eps^k = B sqrt2 (ratio sigma+/|sigma-| = 1), so on the domain 1 <= sigma+/|sigma-| < lambda it occurs only at '
  'k = 0 (even), and -red(-x) = red(x) on all odd sites. Finite check against the production files (production_match.py): '
  'lineN14 a_enum.jsonl span and zr match the exact census on all 5109 classes (j <= 12); N20 a_cert_ext span and zr match on all 14987 rows '
  '(j = 13, 14), and the 338 coded rows all have exact zr >= 6; the stored a_enum integer word differs on 2182 classes (int()-truncated floats, '
  'letter-wise exact - sign(exact)), span and zr being exact, so the finite bad set of Thm A (BGS-TRACE-331) is unchanged.',
  'proved', 'PROVED [P] + FINITE COMPARISON WITH THE PRODUCTION ARTIFACTS (lineN14 a_enum, N20 a_cert_ext) + ' + REF,
  [f'{V}/code/production_match.py', f'{V}/logs/production_match.json']),
 C(339, 'Span theorem examples: alpha = 116 (N = 13456, span 13, internal zero run 9, span - L = 2.99966264991176), 82 sqrt2 (N = -13448, span 11, run 7, span - L = 1.00033740024809), 118 (N = 13924, span 13, run 3, span - L = 2.96087221277804); alpha = 2 attains floor(L) + 3 = 3',
  [337],
  '[P] exact integer digit words (span_census.py; words [1,-1,0^9,1,1], [1,1,0^7,-1,1], [1,-1,0^3,1,0,-1,0^3,1,1], and (1,0,-1) for alpha = 2); '
  'defects are mpmath (40 digits) values printed to 15 digits. All three lie in shell 13; 118 is bad at g0 = 4 (run 3), 116 is not (run 9). '
  'Lean (Bgs.LineNSpan): norms and shells, and integer floor certificates for the window digits of 116, 82 sqrt2, 118, 2 and 3 + sqrt2 '
  '(decide +kernel); the exact sign test is not proved equal to the real sign in Lean and the vanishing outside the window is the paper Lemma 3.',
  'proved', 'PROVED [P] (EXACT INTEGER COMPUTATION) + LEAN FINITE CHECKS (Bgs.LineNSpan.cert_*, span_*, norm_*) + ' + REF,
  [f'{V}/code/span_census.py', f'{V}/logs/span_census_J16.json', f'{V}/code/gen_lean_span.py'], LEAN,
  'Partial: integer floor certificates and digit words on a finite window, norms and shells; the real-number semantics of the sign test and the out-of-window vanishing are not formalised.'),
 C(340, 'Lemma BI (background interplay, P2): under hypothesis (M) the coded gas factorises exactly as Z = Z_M * Ztilde over decorated bad polymers, and KP gives |ln Ztilde| <= p Stilde_0, i.e. |Z| >= |Z_M| e^{-p Stilde_0}; conditional on (M) and on the unproved per-site normalisation of A_M',
  [332, 337],
  '[P mod (M)] Hypothesis (M): the level-h_p coded gas after the interaction correction delta is a hard-core product-activity polymer system on Z/p '
  '(model polymers: support <= 3, l_M <= 7, per-site anchored activity A_M <= 1.03e-3 (N11); bad polymers: exclusion span + g0, g0 = 4), with '
  'bad-model gap interactions absent or inside delta and wrap-around polymers excluded; (M) is a residual [P-sketch], not covered by delta_true as '
  'registered. NOT PROVED: (M), and the per-site / factor-2 convention of A_M relative to the factor 2 of S_0. Proof [P mod (M)]: BI.1 cluster-expansion '
  'factorisation (Ueltschi 2004 Thm 1, external polymers), BI.2 tree bound with decorated activities <= u(gamma) e^{kappa(l + 7)}, '
  'kappa = e^{7c\'} A_M e^{7c\' + 7(a + S*) + S1*}, BI.3 KP condition S* + (S1* + 12 kappa)/5 <= a. Numbers (crossover_sharp_bi.py, mpmath dps 40, '
  'conditional also on H1-bad through C, V5 idealised additive terms): C = 0.082, J0 = 12: first prime 3389 at the minimal KP weight '
  '(a = 4.318e-3, kappa = 1.1112e-3, Stilde_0 = 3.51054e-4) and 3407 at the N20-style x1.02 iterate (a = 4.409e-3); C = 8.8e-4: 1409 (unchanged); '
  'C = 0.04: 1753; J0 = 14: 1831. Boundary note on BGS-TRACE-332: with BGS-TRACE-337 the H1 => H3 step needs only the shell-law half H1-bad, and is '
  'proved modulo (M) and the per-site normalisation; it is not an unconditional implication, and H1 stays open. No registered value or state '
  '(BGS-TRACE-325, 332, 333, 336, 301, 206) is changed.',
  'conditional', 'CONDITIONAL ON HYPOTHESIS (M) AND THE PER-SITE NORMALISATION OF A_M (NOT PROVED); NUMBERS ALSO CONDITIONAL ON H1-BAD (BGS-TRACE-336) + ' + REF,
  [f'{V}/code/crossover_sharp_bi.py', f'{V}/logs/crossover_sharp_bi.json', f'{V}/logs/crossover_sharp_bi.log'],
  closure='A proof of hypothesis (M) for the level-h_p coded gas (in particular that bad-model gap interactions are absent or inside delta) and of the per-site / factor-2 normalisation of A_M consistent with S_0.'),
 C(341, 'Sharp-span Prop. K crossover rows [P-arith], conditional on H1-bad: bare-activity majorant 3299 -> 3067 at C = 0.082, J0 = 12 (interplay not charged); with Lemma BI (conditional on (M)) 3389 at the minimal KP weight / 3407 at the x1.02 iterate; 1409 at C = 8.8e-4 unchanged; registered 3307 / 1409 unchanged',
  [333, 336, 337, 340],
  'V5 crossover logic (BGS-TRACE-333) re-implemented in mpmath dps 40 (crossover_sharp_bi.py) with delta_true = 5.0313e-6, Re Lambda_lo\' = 6.234e-4, '
  'g0 = 4, idealised additive terms. Bare activities (model-background interplay NOT charged; a majorant on bare activities only): slope-2 tail at '
  'the minimal KP weight 3299 (the registered 3307 is the same majorant at the N20 x1.02 iterate, delta_eff 3.4962e-4, reproduced), sharp span '
  '(BGS-TRACE-337 Corollary D) 3067 (a = 1.52315e-3, S_0 = 3.24040e-4); sensitivity S_0 x 0.99/1/1.01/1.03/1.10: 3037/3067/3109/3181/3463; C = 0.04: 1721; '
  'C = 8.8e-4: 1409; J0 = 14 (H1-shell(C, 12) implies H1-shell(C, 14); shells 13-14 certified for the core functional, BGS-TRACE-331): 1787 '
  '(C = 0.15: 3019), recorded for information; restating BGS-TRACE-325/333 at J0 = 14 is not done. With Lemma BI (BGS-TRACE-340, conditional on (M) '
  'and the normalisation): 3389 (minimal KP weight) / 3407 (x1.02 iterate), 1409 at C = 8.8e-4. The registered 3307 is not supported once the '
  'interplay is charged by BI; none of these values replaces the registered thresholds, and Theorem v5 (BGS-TRACE-325), BGS-TRACE-333 and the '
  'states of BGS-TRACE-301, 332, 336, 206 are unchanged.',
  'conditional', 'CONDITIONAL ON H1-BAD (BGS-TRACE-336, OPEN) [P-arith, MPMATH RECOMPUTATION, IDEALISED ADDITIVE TERMS]; BI ROWS ALSO CONDITIONAL ON (M) (BGS-TRACE-340) + ' + REF,
  [f'{V}/code/crossover_sharp_bi.py', f'{V}/logs/crossover_sharp_bi.json', f'{V}/logs/crossover_sharp_bi.log'],
  closure='A proof of H1-bad (BGS-TRACE-336) with C <= 0.082 at J0 = 12 for the bare rows; in addition (M) and the A_M normalisation (BGS-TRACE-340) for the BI rows; and the additive budgets of p_thr.'),
]
cl.extend(new)
P.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('added', [c['id'] for c in new], 'total', len(cl))
