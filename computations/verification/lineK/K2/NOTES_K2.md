# Line K2 notes (started 2026-10-31 10:30 +0500). Do NOT edit ../REPORT.md (under referee review).
Goal: close H♮_mid (levels d < L_m, conductor ∉ {1,7}) or strongest rigorous partial result.
## Findings so far
- (c) Z-bound input of K2 is ALREADY [CA]: P* = {(±2,8),(±2,16)} (TRACE-206 frozen primaries N≡±4,±8).
  |Z_(±2,8)| <= |c_m|(|c0f| mu*^m + H0), H0<=1506.18, |mu*|<=1.9154753 (Line F, J v2 §Z0); |Z_(±2,16)| <= C16*1.6677^m from J3 rest certs
  (assemble16 'R_untwisted_max'=1.6677). Need: script k2c_zbound.py to output S_Z explicitly.
- (b) trivial bound per level is ~|Z|*mu*^m >> D7 (even ONE level kills); counting levels cannot help. Primitive-part factorisation control
  (at most one prime > L_m in primitive part) is beyond reach (like primitive-divisor primality). => (b) negative.
## Plan (main line = (a))
 W1 [P] Weil lemma: q prime, H=<l> order n | q-1, A,B in F_q not both 0: |sum_{h in H} e((Ah+B/h)/q)| <= 2 sqrt q (twisted Kloosterman via
    characters trivial on H; Gauss period if B=0 or A=0). Composite d (CRT): <= 2^{omega} sqrt d. 7q: <= 6 sqrt q.
 W2 [P] Block AM-GM lemma: |Tr prod_{i in Z/m} L_{tau_i}| <= C_s(k) * [ (1/r) sum_{i<r} ||P_k(y_i)||_HS^2 ]^{floor(m/k)/2}, y_i = beta lam^i/d,
    using all m cyclic offsets (each start covered floor(m/k) times) + GM<=QM.
 W3 [P] Fourier: f_k(y)=||P_k(y)||_HS^2 = sum_gamma c_gamma e(Tr(gamma y)), gamma = x_w - x_w' in O; mean over T^2 = I_k (collision sum).
    Orbit average = I_k + sum_{gamma!=0} c_gamma S(gamma)/r; nondegenerate gamma (q > 6B^2 lam^k) -> |S|<=2sqrt q.
 => Theorem W: if I_k^{1/2k} < 1.28359 (OP_k, operator input), all levels q <= p^{2-eps} (and 7q) are negligible for p >= p0. Explicit.
    Bourgain (Mordell-sum 2005, binomial over subgroups; BGK for linear) extends qualitatively to q <= p^C [cite, check].
 N1 [N] compute I_k (collision transfer operator with carry automaton, exact in toy) -> rate lim I_k^{1/2k}; also MC HS^2 cat-map check.
- 10:45 W1 Weil instances OK (code/w1_weil_check.py: max |sum|/sqrt q <= 1.19 < 2 over 20 (p,q), linear <= 0.59 < 1).
- 10:45 N1 RESULT [N]: exact cat-map second moment I_k (carry automaton, code/n1_collision.py): per-step ratio I_{k+1}/I_k -> 1 to 1e-10
  (b=8: K=40/24, NMAX 7/9, EMAX 6/8 all agree; b=16 also 1). So lim I_k^{1/2k} = 1.000 << 1.28359 (toy). Constants e^{20.6} (b=8) from
  non-normal Galerkin basis => I_k^{1/2k} < 1.2836 from k ~ 40, =1.108 at k=100. (OP) numerically very comfortable.
  Observation: the true scalar word weights have |a_w| = prod |ghat(n_j)| with sum |ghat|^2 = sum J_n(1.8)^2 = 1 (unitarity) -> rate 1.
- Theorem W plan stands: Weil range q <= c_k p^2 (explicit c_k = (eta/2A_k)^2), plus 7q. Composite primitive conductors (>= 4p^2) open.
- Positivity/periodic-point trick (sum over O/q <= sum over Fix(T^r)) evaluated: loses index |N(lam^r-1)|/q^2; for rank 3p fails
  (needs q > 1.88^m > sqrt h); rank p needs 6th-moment pressure, only near q ~ lam^{p/2}. Recorded as [H] partial, not pursued.
- scalar mod-q L^2 with absolute values fails (l1 mass 2.35^m vs aliasing 1/q^2).
- n2_factor_h.py running (factor h_{3p}, p<80, classify levels).
- 10:55 N3 [N] toy traces at actual levels (code/n3_levels_toy.py): per-step max_beta rate: p=37: q=223 (Weil, all orbits) 1.071; 6217: 0.93;
  37223: 1.13; 8761009 (log_p q=4.4): 1.292 at slow beta (1,0) > 1.2836 (sampled). p=13: 79: 1.21, 313: 1.09, 599 (rank 13 small-rank): 1.381,
  4088137: 1.356 (slow beta). => Weil-range levels benign; open range has slow beta exceeding threshold at small m (max, not weighted).
- N2: factorisations p<=43: most prime factors of h_{3p} lie in the open range p^2 < q < sqrt h (log_p q 2..15). Weil range catches few.
- 10:56 Referee report on REPORT.md arrived (/workspace/audit/lineK/REPORT.md): all ACCEPT AFTER FIXES. TODO: REPORT_v2.md with
  K2-F1 S_Z extraction (+P* confirmation), K2-F3 eta proof, H♮_mid as alternative, K1-F1..F4, K3-F1..F4, K4-F1..F3, crossover 1.68e9 bisection.
  New files only: code/k2_SZ.py, code/k2_large_v2.py (don't touch v1 files).
- 10:40 REPORT_v2.md written (all referee fixes; S_Z<=0.5000001; crossover 1.682e9; eta proof).
- 10:43 Lean: lean/K3Finite.lean passes (fraction tests b<1339 & 6 exception denominators, sieve enumeration, survivors=9; decide only, no axioms). lean/run_gaps.sh running kernel-decide K3(a) gap<=b'/6 on 447..2645 in chunks (gaps_summary.txt). n2 relaunched (fmpz fix). Next: REPORT_K2.md (Theorem W).
- 10:45 REPORT_K2.md written (Theorem W, K2', negatives).
- 10:45 Lean gaps: switched to 'decide +kernel' (elaborator decide timed out; kernel-only, no native code, no axioms). 20 moduli in 6 s; full 447..2645 running in chunks of 100.
- 11:25 C1 control [N]: scaling ghat by 1.1 (non-unitary) makes I_{k+1}/I_k = 1.21 = 1.1^2 exactly (K=24). So lim I_k^{1/k} = sum|ghat|^2 (=1 by
  unitarity, sum J_n(1.8)^2 = 1) -- strong evidence for Conjecture C1 mechanism. Added to REPORT_K2 §2.
- 10:48 Added segment-Hölder upper-range reduction (q >~ lam^{m/4k}, needs pi_k < 2k log1.28359; blocked by non-normal constants) to REPORT_K2 §5 as [P reduction/H].
- 11:28 Lean gaps: 447..1646 all exit 0, no axioms. Chunks 1647..2645 (n=100) died exit 137 (OOM, lean RSS ~8.6G). Relaunched as run_gaps2.sh with n=20 -> gaps_summary2.txt.
- 11:28 Added explicit BGK-scope paragraph (TRACE-179 remark: subgroup order ~p, BGK only q<=p^C) to REPORT_K2 §3.
- 12:13 Lean gaps COMPLETE: 447..2645 all exit 0, all gaps_* axiom-free (62 chunk logs checked). REPORT_v2 §6 updated. Next: manifests + final summary.
- 12:13 Manifests written & verified: SHA256_v2.txt (154 files, sha b7be7e9c…), K2/SHA256_K2.txt (25 files; for its hash see SHA256_K2.sha256, which is outside the manifest). REPORT_v2 badaafd8…, REPORT_K2 b8d14b60…. REPORT.md unchanged (8fc2e9f1…). DONE for this round.
- 12:26 Referee DELTA fixes applied: REPORT_K2_v2.md (W-F1 non-cyclic W2′, W-F2 1.4742, W-F3..F6, step 6/7). REPORT_v2 in-place η wording + §8 errata. Lean bprime_ge restated (3∣b), recompiled exit 0 (lean_check_v2.log). Manifest hashes are now kept only in *.sha256 side files (W-F6).
