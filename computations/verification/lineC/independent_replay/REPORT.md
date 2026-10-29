# Referee audit of BGS Line C (`/workspace/bgs-lineC/REPORT.md`)

*Audit written 2026-10-29 (Europe/Berlin). Everything here is in `/workspace/audit/lineC/`. Nothing was pushed, and `/workspace/bgs-build` was only read (copied).*
*Box incident: partway through the audit, `/workspace/audit/lineC`, my first Lean copy and `/workspace/bgs-lineC/build` disappeared from the box. Another process seems to have restored the tree. I re-created all code and logs. The Lean copy was rebuilt from `/workspace/bgs-build/formalization` plus the report's `lean/LineCEncounter.lean`. Backup: `/home/box/audit_lineC_backup/`.*

## Verdicts

| Claim | Verdict | One-line reason |
|---|---|---|
| Thm 1: D_θM_N ≅ D_θ′·DFT, measure-preserving; Tanner's ensemble | **CORRECT-WITH-FIXES** | The algebra is right and was checked numerically. The "S enters only through the square class of b" remark needs a caveat: for p≡1 (mod 4) the class *does* change E\|Tr U^m\|² (the sign of every √p term flips). |
| Prop 2: exact Gauss-sum/partition formula; rational for p≡3 (mod 4) | **CORRECT** | Re-derived on paper. Independent brute force matches it exactly at 17 (p,m) pairs, and floating-point checks match at composite N. ℚ(√p) for p≡1 (mod 4); no p^{−1/2} term. |
| Lemmas 3–5: 2-opt / swap / figure-eight classification, counts, weights | **CORRECT-WITH-FIXES** (cosmetic) | Proofs check line by line. The counts were verified exhaustively by direct enumeration (Lemma 4 for m ≤ 10, Lemma 5 for m ≤ 9). The wording of the (4,4) case should be fixed. |
| Thm 6: E = 2m − 2m²/p + O(p^{−3/2}), p > 8^m, m ≥ 5 | **CORRECT-WITH-FIXES** | The classification is complete at order 1/p and the coefficient −2m² is exact. But the explicit error constant C_m is so large that the stated bound only beats the 2m²/p term when p > (C_m/2m²)² ≫ 8^m. Restate it as an exact-coefficient theorem; the threshold can be p > 4^m. |
| Thm 7: exact expansions for m ≤ 10, through p^{−5/2} for m = 11, 12; c₂ ≠ 2m³ at some m (3480 vs 3456); p^{−5/2} and Legendre terms | **CORRECT** | All coefficients were reproduced by an independent engine. All 10 of their logs agree with mine identically, at 171 primes, for m = 3..12. c₂(12) = 3480 confirmed. |
| Novelty: "first exact all-pairs proof of −2τ² for Tanner's ensemble"; "previously only observed numerically" | **OVERSTATED / partly WRONG** | Gnutzmann–Seif 2004 (PRE 69 056220) treat *exactly this ensemble* (a class-AI star graph with a DFT central vertex and i.i.d. uniform peripheral phases) and derive K = 2τ − 2τ² + O(τ³) diagrammatically (n, B → ∞). The report never cites them. Gnutzmann–Altland 2005 and Pluhař–Weidenmüller 2014 also claim, non-rigorously, full GOE statistics for such gapped graphs. What *is* new: a rigorous, exact-in-p, fixed-m result with a complete classification, including the swap class. |
| Lean `LineCEncounter.lean` | **CORRECT** (scope as stated) | Builds in my own copy: `lake exe cache get`, then `lake build Bgs.LineCEncounter`, 292 s. Axioms are {propext} or none; no sorry or native_decide. The statements match §9 of the report. |

## 1. Line-by-line mathematical audit

### Theorem 1
* M_N(x,y) = N^{−1/2}e_N(−8^{−1}(3x²−2xy+3y²)). The cross term is +2·8^{−1}xy = 4^{−1}xy, and the diagonal factors are Δ = diag e_N(−3·8^{−1}x²). So M = ΔF_{1/4}Δ.
* With (Pf)(x) = f(2x):
  * (PAP^{−1})(x,y) = A(2x,2y), so PF_{1/4}P^{−1} = F.
  * P·diag(d)·P^{−1} = diag(d(2x)), which gives θ′_x = θ_{2x} − 2π·(6·8^{−1}(2x)² mod N)/N.
  * This map is a coordinate permutation followed by a translation, so it preserves Haar measure. ✔
* Independent numerical check (`logs/thm1_check.log`): N = 9, 15, 21, 101, 103. Conjugation error ≤ 5.5e−16; eigenphases agree to ≤ 4e−15.
* **S-dependence.** The law depends only on the class of the cross coefficient β in units/squares (x ↦ ux), and the global phase γ is absorbed into θ. That is correct, but the class *does* matter in general:
  * Replacing β by a non-square ν multiplies each Gauss sum by (ν/p)^r = (−1)^r. So every odd-rank term, i.e. every half-integer power p^{−k−1/2}, changes sign.
  * For p≡3 (mod 4) those terms vanish anyway, and the law is just complex-conjugated.
  * For p≡1 (mod 4) the form factor changes. Checked in `logs/square_class.log`: at p = 13, m = 4, E = 14033/2197 ± 8√13/2197 for β = 1 and β = 2 respectively, matching brute force. At p = 7 and p = 11 the two values are identical.
  * Consequence: Theorem 6, c₂, and all integer-order coefficients are S-independent. The p^{−5/2} coefficients of Theorem 7 (8, −72, 128(2/p), 200) are for the square class only. That class applies here, because 4^{−1} is a square.
* "Tanner's ensemble": confirmed from the full text (`lit/nlin_0104014.txt`, eq. (8), Sec. IV b). Ũ is the symmetric Fourier matrix ũ_nm = N^{−1/2}e^{2πi(n−1)(m−1)/N}, and spectral functions need only the N phases of D·Ũ. Theorem 1 covers odd N only, while Tanner allows all N.

### Proposition 2
Re-derived independently:
1. Step 1: the phase average gives the occupation-multiset indicator.
2. Step 2: Δ-factors cancel for equal multisets, which gives the e_N(c(P_x−P_y)) form.
3. Step 3: the stabiliser has order ∏|B|!.
4. Step 4: Möbius inversion on Π_m. The interval [0̂,ρ] factorises over the blocks, and the exponential formula gives Σ w(n)tⁿ/n! = log Σ tⁿ/(n!)². My series gives w = 1, −1/2, 2/3, −11/8, 19/5.

Gauss sum: take I = a row basis of the symmetric matrix B. Then B_II is nonsingular and B ≅ B_II ⊕ 0, so G = p^{n−r/2} ε^r (2^r det B_II / p), since c = 1/4 is a square. ✔

Corollaries:
* For p≡3 (mod 4), E is rational for **every** such p, not just large ones: odd-rank terms are i·√p·ℚ and must cancel.
* There is no p^{−1/2} term: a zero-diagonal symmetric matrix of rank 1 vanishes in characteristic ≠ 2. ✔

Numerical checks:
* My brute force (`code/brute.cpp`) evaluates E·p^m = Σ_{multisets} |Σ_{arrangements} ζ^{cP_x}|² in exact integer class counts. It shares no code with Prop. 2.
  * It agrees with the literal-kernel floating sum (`code/literal_float.py`).
  * It agrees with my Prop.-2 engine in per-prime mode, exactly, at (p,m) = (5,4), (7,3), (7,4), (7,5), (11,5), (11,6), (11,7), (13,4), (13,5), (13,6), (13,7), (17,5), (17,6), (19,6), and at 19 ≤ p ≤ 31 for m = 5..8 (`logs/validity.log`).
* Composite N (`logs/prop2_composite.log`): direct z-sums of Prop. 2 match the literal kernel to ≤ 1e−13 at N = 9, 15, 21.

### Lemma 3
Aut(C_m) = D_m, so the term is 2m for m ≥ 3. ✔

Side error in §8 of the report: "m = 1, 2 sit at the diagonal values 1 and 2". In fact **E|Tr U²|² = 2 − 1/p exactly**: the deficit-1 figure-eight term ρ = {0,1} contributes −1/p. Brute force gives 91/49 at p = 7 and 231/121 at p = 11, and the report's own `symbolic_m1_7.log` says the same. Also, m = 3 is exactly 6 − 9/p + 4/p² for every prime p ≥ 5.

### Lemma 4 (rank-2 classification)
Every step checks:
* balance;
* principal-minor bounds: det of signed P₄ and of signed 2K₂ is 1, det of a signed triangle is 2abc;
* no induced 2K₂ ⇒ one nontrivial component;
* P₄-free and connected ⇒ complement disconnected (Seinsche) ⇒ join;
* triangle-free ⇒ K_{s,t}, with degrees in {2,4};
* rank [[0,X],[Xᵀ,0]] = 2 rank X ⇒ X = uvᵀ, with Σu = Σv = 0;
* the cases (2,2) and (2,4).

The new 2-opt edges {i,j}, {i+1,j+1} are never C-edges when 2 ≤ j−i ≤ m−2, so Γ really is the 4-cycle.

*Fix (wording) for the (4,4) case.* All 8 vertices have Γ-degree 4, so both of their C-edges lie in C∖H ⊂ E(Γ). Hence V(Γ) is closed under C-adjacency, so m = 8 and C∖H = C. But C∖H = {a_ib_j : u_iv_j = +1} is K_{2,2} ⊔ K_{2,2}, two 4-cycles, whereas C is an 8-cycle. Contradiction.

Independent exhaustive check (`code/classify.py`, `logs/classify.log`), m = 4..10, all (m−1)!/2 cycles:
* the rank-2 cycles are exactly the 2-opts, m(m−3)/2 of them, and the swaps, max(0, m(m−5)/2);
* nothing is unclassified;
* ranks 1 and 3 never occur at deficit 0 for m ≤ 10 (the report checked m ≤ 9).

### Lemma 5 (figure eight) and the overcounting
* For p > 2m, B ≡ 0 (mod p) ⇔ B = 0, i.e. equal edge multisets, loops included.
* Eulerian circuits of the figure eight: d(g)d(m−g) cyclic classes, each with m distinct rotations because a singleton label exists for m ≥ 3.
* The σ-count is 2#y, and W = w(2) = μ(0̂,ρ)/1 + 1/2! = −1/2.
* Summing over unordered pairs gives (m/2)Σ_g, so (1,0) = −(m²/2)Σ_g d(g)d(m−g) = −2m³ + 6m² for m ≥ 5.
* m = 3 gives −9 and m = 4 gives 16 − 40 = −24. ✔
* Direct enumeration: #y = m·d(g)d(m−g) for every g and 3 ≤ m ≤ 9.
* In the engine, the (d,r) decomposition gives (0,2) = 2m²(m−4) and (1,0) = −2m³ + 6m² for every m = 5..12. Examples: 2304 and −2592 at m = 12; 1694 and −1936 at m = 11.

The overcounting is therefore handled exactly by the partition-lattice weight.

### Theorem 6: completeness, the error term, and p > 8^m
* **Completeness.** |term| = p^{−d−r_p/2}. For p > 8^m (from the report's own bound), r_p = r_ℚ. So order p^{−1} comes exactly from (0,2) and (1,0), (0,1) is impossible, and Lemmas 4–5 classify both completely.
  * No other pair class can contribute at order 1/p. I confirm that the classification is **complete**.
  * The swap class is essential: without it the coefficient would be −m³ + 3m².
* **Error term.** |R| ≤ m!·Σ_ρ|W(ρ)|·p^{−3/2} is correct and uniform in p > 8^m for fixed m, but the constant is huge:
  * C_5 = 3651, C_8 ≈ 1.36e8, C_12 ≈ 4.4e15.
  * At p = 8^m, C_m p^{−3/2} exceeds the main correction 2m²/p for m ≥ 8. For m = 8 it is 2.0e−3 against 7.6e−6.
  * So, read literally, the explicit bound beats the 1/p term only when p > (C_m/2m²)²: about 1e12 for m = 8 and 2e26 for m = 12. The statement is not false, but its "explicit" framing is misleading.
* **Fix.** State Theorem 6 as an *exact coefficient identity*:
  * For p > 4^m, E is exactly a finite sum Σ_k a_k(p) p^{−k/2}, with coefficients that are rational combinations of Legendre characters.
  * a_0 = 2m, a_1 = 0, and a_2 = −2m² for every m ≥ 5.
  * The O(p^{−3/2}) statement then follows.
* **Threshold.** ∏_B 4|B| ≤ 4^m, because 4k ≤ 4^k. So the report's own Hadamard argument gives p > 4^m. Empirically the expansion is already exact at much smaller primes:
  * all primes p ≥ 5 for m = 3 and 4;
  * every prime 7 ≤ p ≤ 257 for m = 5, 6 (none excluded);
  * every prime 11 ≤ p ≤ 257 for m = 7 (none excluded);
  * every prime 19 ≤ p ≤ 139 for m = 8.

  These were compared exactly, prime by prime, in `logs/validity.log`.
* **Data fit** (`logs/fit.log`; exact per-prime values at 43 primes p≡3 (mod 4) in [211, 3931]):

  | m | fitted c₀ | fitted c₁ | target (2m, −2m²) | p²(E − 2m + 2m²/p) at large p |
  |---|---|---|---|---|
  | 5 | 10.00001 | −50.04 | 10, −50 | → 175 ± 10 |
  | 6 | 12.000000 | −71.999 | 12, −72 | → 390 |
  | 7 | 13.999999 | −97.997 | 14, −98 | → 686 |

  Brute-force values at p = 19..31 also equal the symbolic expansions exactly.
* **Scope.** This is a fixed-m statement. It matches the COE 1/N coefficient −2n² for m ≥ 5 but not for m = 3 or 4, and it says nothing at fixed τ. The report already says this.

### Theorem 7
My engine (`code/engine.cpp` and `code/sym.py`) is written from scratch. Its design:
* exact int64/int128 Bareiss rank over ℚ, with the row basis giving a nonsingular principal block;
* squarefree part of 2^r det;
* rotation reduction of the words, and dihedral orbits of ρ;
* weights from my own log-series.

It reproduces every coefficient in the report's table:
* m = 3..10 to all orders;
* m = 11 and 12 through p^{−5/2}.

Logs: `logs/sym_m*.log`. Cross-check against their logs, read as data only: `logs/compare_theirs.log`.

Confirmed specifically:
* There is no p^{−3/2} term for m ≤ 12.
* c₂ values:

  | m | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
  |---|---|---|---|---|---|---|---|---|
  | c₂ | 175 + 10(5/p) | 390 | 686 | 1008 | 1512 | 2000 | 2662 | **3480** |

  So c₂ = 2m³ only at m = 7, 10, 11. **At m = 12, c₂ = 3480 ≠ 3456 = 2·12³.**
* Decomposition at m = 12: (0,4) = 118200, (1,2) = −315936, (2,0) = 201216, total 3480. Runtime 252 s on 8 threads.
* p^{−5/2} coefficients for p≡1 (mod 4): 8, −72, 128(2/p), 200 at m = 4, 6, 8, 10, and 0 at m = 3, 5, 7, 9, 11, 12.
* At m = 12 the p^{−5/2} classes cancel: 6048 − 12672 + 6624 = 0. In the report's ε-normalisation this is 3024 − 6336 + 3312.
* Character terms at p^{−3}: (5/p), (2/p), (−3/p), (−7/p), e.g. m = 7: −5047 − 98(5/p) + 28(−7/p).
* p^{−3} at m = 10 is −26000, against the COE value −26600.
* The COE reference formula was checked by Monte Carlo (`logs/coe_check.log`).

## 2. Literature: is Theorem 6 new?

Sources: `lit/gs1.txt` and `lit/gs2.txt` (arXiv nlin/0309049 and nlin/0309050), plus the report's `lit/`.

* **Tanner 2001** (nlin/0104014). The ensemble identification is confirmed, and COE is only observed numerically there. **Fix:** the convergence rate is **σ(N) ≈ (3/4)N^{−4/3}** ("slightly smaller prefactor" than the binary-graph N^{−4/3}), not (4/3)N^{−4/3). Also, σ is the τ-averaged standard deviation from RMT.
* **Berkolaiko–Schanz–Whitney 2002 and 2003.** The report's description is accurate: bond phases on B = N² bonds, loop-reversal pairs only, the "not discussed whether other correlated orbits…" caveat, and τ³ for the Fourier graph as B → ∞.
* **Gnutzmann–Seif 2004, PRE 69 056219/056220 (nlin/0309049/50). MISSING from the report and decisive for novelty.**
  * Their class-AI star graph is S_C = B×B DFT, S_P = diag(e^{iβ_k}) with i.i.d. uniform β_k, and equal bond lengths, i.e. **exactly D·DFT** (I §IV, eqs. (73)–(74)).
  * In II §III B they "find all diagrams that contribute to the diagonal approximation and one order beyond". The averaged pairs are exactly the orbits "visiting the same peripheral vertices with the same multiplicities", and they obtain **K₂ = 2τ − 2τ² + O(τ³)**.
  * This is physics-level: B ≫ n ≫ 1, a time average over n, then n, B → ∞, with an overcounting bookkeeping.
  * Their non-complete-diagram criterion (eq. (24): oscillating sums of the form Σ_k e^{2πik(k′−k″)/B} force index coincidences) does not obviously cover the **swap** class. A swap yields a constraint z_{b1} + z_{b2} = z_{b3} + z_{b4}, not a coincidence, and their diagram families never mention it, yet swaps contribute +2m²(m−5)/p, the same order as the 2-opt pairs.
  * So the rigorous, complete classification is genuinely new, but **"−2τ² was previously only observed numerically for this ensemble" is wrong.**
* **Berkolaiko–Keating 1999** (J. Phys. A 32 7827). Neumann star graphs with random bond phases, i.e. the same "D·Σ" structure with Σ = 2/N − 1. They give an exact combinatorial all-pairs (diagonal plus off-diagonal) evaluation of the τ-expansion coefficients as N → ∞, with non-universal results. This is prior art for the method (equal-multiset pairing in star graphs) and should be cited.
* **Gnutzmann–Altland 2004 PRL / 2005 PRE 72 056215.** A supersymmetric σ-model gives Wigner–Dyson statistics for B → ∞ under a gap condition. They explicitly list "complete DFT graphs" and "star graphs with [generic] central vertex scattering matrix" as satisfying it.
* **Pluhař–Weidenmüller 2014** (PRL 112 144102). All GOE correlation functions for mixing graphs as B → ∞. Their massive-mode step needs a gap assumption (Weidenmüller 2018).

  These two works (non-rigorously) predict the *full* COE form factor at fixed τ for this ensemble. That is relevant to the report's Conjecture 8 and §8 and should be cited there.
* **Kottos–Smilansky 1997/99.** DFT complete graphs, numerics plus the diagonal approximation; no fixed-m exact off-diagonal result.
* **Schanz–Smilansky 2000.** Exact combinatorics for a 2-bond graph, which reproduces 2×2 CUE; a different ensemble.
* **Gutkin–Osipov.** The report's own description rests on abstracts only. I did not find DFT/Gauss-sum content there either, so this is not independently verified.

**Honest novelty statement (suggested).** For the random-phase DFT (Tanner / Gnutzmann–Seif star-graph) ensemble, Theorem 6 is the first rigorous derivation of the first off-diagonal coefficient: exact in p for each fixed m ≥ 5 (p > 4^m), with a complete classification of contributing pairs (2-opt, swap, figure-eight). It confirms the COE value −2m² previously obtained diagrammatically in the limit n, B → ∞ by Gnutzmann–Seif (2004) and predicted by the σ-model (Gnutzmann–Altland 2005; Pluhař–Weidenmüller 2014). Theorem 7 adds exact non-universal finite-p structure (c₂ ≠ 2m³, half-integer and character terms) that those limits cannot see. Prop. 2 and the Gauss-sum/rank viewpoint appear new as far as I can tell. The equal-multiset pairing itself goes back to Berkolaiko–Keating 1999.

## 3. Lean

* **Copy.** `/workspace/audit/lineC/build`, copied from `/workspace/bgs-build/formalization` plus `Bgs/LineCEncounter.lean`, which is byte-identical to the report's file.
* **Cache.** `lake exe cache get` downloaded and decompressed 8690 files (`lean_cache_get.log`). Mathlib was not built from source.
* **Build.** `lake build Bgs.LineCEncounter`: "Build completed successfully", 292 s (`lean_build.log`).
* **Axioms** (`lean_axioms.log`): `propext` only for aut5, aut6, rank2_class6, rank2_counts6, fig8_6 and exact_7/11/13_3; none for ham6, msPerms_count, coeff_identity and hyp_counts. No `sorry` and no `native_decide`.
* **Statements vs report.** They match the §9 table:
  * aut5/aut6 count σ preserving the edge multiset (= 2m);
  * rank2_class6 is "all 3×3 minors vanish ⇔ C, or |C∖H| = 2, or swap at distance ≥ 3";
  * fig8_6 is m·d(k)·d(m−k) for k = 1, 2, 3;
  * coeff_identity covers m = 5..300 with exact integer division;
  * exact_p_3 uses c = 4^{−1} mod p (2, 3 and 10), weights 6W = 6, −3, −3, −3, 4, and A₀ − A₁ = E·6·p³ under constOff.
* **Cosmetic.** In `hyp_counts`, `… && hypOK 13 = true` parses as `… && decide (hypOK 13 = true)`. This is harmless.
* **Scope.** Only finite instances are checked (Lemma 4 and Lemma 5 at m = 6, Prop. 2 at m = 3). The report states this honestly.

## 4. Exact fix list for `/workspace/bgs-lineC/REPORT.md`
1. **§0 item 4, §10 Tanner bullet, and §11 item 4.**
   * Delete "There COE behaviour was previously only observed numerically" and "Previously the result was known numerically for this ensemble (Tanner 2001)…".
   * Add Gnutzmann & Seif, PRE 69, 056219 and 056220 (2004), arXiv nlin/0309049 and nlin/0309050: exactly this ensemble, with 2τ − 2τ² derived diagrammatically for n, B → ∞, and the swap class not listed among their diagram families.
   * Replace the novelty claim with the statement in §2 above ("first rigorous, exact-in-p, fixed-m, complete classification").
2. **§10.** Add Berkolaiko–Keating 1999 as prior art for exact all-pairs combinatorics in random-phase star graphs (Neumann vertex). Note that Gnutzmann–Altland 2005 explicitly include DFT and star graphs, and that Gnutzmann–Altland 2005 and Pluhař–Weidenmüller 2014 predict the full COE K(τ) at fixed τ (relevant to Conj. 8 and §8).
3. **§10 Tanner.** σ(N) ≈ (3/4)N^{−4/3}, not (4/3)N^{−4/3}.
4. **§0 item 1 and §2.** Add: "The square class matters for p ≡ 1 (mod 4): a non-square cross coefficient flips the sign of every half-integer (√p) term. Integer-order coefficients, and hence Theorem 6 and c₂, are class-independent. Theorem 7's p^{−5/2} values refer to the square class, which is the case here (cross coefficient 4^{−1})." Also note that Theorem 1 is for odd N only.
5. **§5 Theorem 6.**
   * Restate as an exact coefficient identity: for p > 4^m, E = Σ_k a_k(p)p^{−k/2} exactly, with a₀ = 2m, a₁ = 0, a₂ = −2m² for m ≥ 5.
   * Give the remainder bound as a corollary, and remark that C_m = m!Σ|W| (3651 at m = 5, about 1.4e8 at m = 8) makes the explicit bound non-informative unless p ≫ (C_m/2m²)².
   * Replace 8^m by 4^m (∏4|B| ≤ 4^m), or keep 8^m but drop "explicitly" from §0.
6. **§4 Lemma 4, step 5, case (4,4).** Replace with the argument in §1 above (closure under C-adjacency ⇒ m = 8, C∖H = C = K_{2,2} ⊔ K_{2,2}, contradiction).
7. **§8.** "m = 1, 2 sit at the diagonal values 1 and 2" → "m = 1 gives exactly 1; m = 2 gives exactly 2 − 1/p (figure-eight term)". Optionally add that m = 3 is exactly 6 − 9/p + 4/p² for all p ≥ 5.
8. **§4 checks.** The rank-1/rank-3 absence at deficit 0 now holds for m ≤ 10 (audit check). It is still not a general lemma; (O1) is fine as stated.
9. **§10 Gutkin–Osipov.** Mark it explicitly as unverified beyond abstracts (it already says so), or drop it.
10. **Optional (Lean).** Parenthesise `hyp_counts` as `(hypOK 5 && hypOK 7 && hypOK 11 && hypOK 13) = true`.

## 5. Reproduce
```
cd /workspace/audit/lineC/code
/workspace/tools/bin/g++ -O2 -std=c++17 -pthread brute.cpp -o brute
/workspace/tools/bin/g++ -O2 -std=c++17 -pthread engine.cpp -o engine
python3 brute_exact.py 13 5              # exact E by direct multiset sum
python3 run_sym.py 8                     # full expansion m=8  (run_sym.py 12 5 : m=12 through p^-5/2, ~4 min)
python3 validity.py; python3 fit.py; python3 classify.py; python3 compare_theirs.py   (run from /workspace/audit/lineC)
cd ../build && lake build Bgs.LineCEncounter && lake env lean AxiomsLineC.lean
```
