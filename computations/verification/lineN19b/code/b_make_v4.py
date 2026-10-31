# N19b: THEOREM_DRAFT_v4.md = v3 + referee lineN16 §4 edits E1-E7 (verbatim) + N16 referee minor notes in H1/H4 rows.
import re
s=open('/workspace/bgs-lineN/THEOREM_DRAFT_v3.md').read()
def R(a,b):
    global s
    assert s.count(a)==1, (s.count(a), a[:90]); s=s.replace(a,b)
def Rline(prefix,new):
    global s
    L=s.split('\n'); idx=[i for i,l in enumerate(L) if l.startswith(prefix)]
    assert len(idx)==1,(prefix,idx); L[idx[0]]=new; s='\n'.join(L)
# header
R("# THEOREM_DRAFT v3 — ","# THEOREM_DRAFT v4 — ")
R("*v3: Line N18b, 2026-11-01 (Asia/Yekaterinburg, UTC+5).*","*v4: Line N19b, 2026-11-01 (Asia/Yekaterinburg, UTC+5). v4 = v3 + referee lineN16 §4 edits E1–E7 (verbatim) + N16 referee minor notes (N16-1…N16-4) in the H1/H4 rows; see §10. v1, v2, v3 kept unchanged.*\n\n*v3: Line N18b, 2026-11-01 (Asia/Yekaterinburg, UTC+5).*")
# E1
Rline("| p₁: gas vs Robin", "| p₁: gas vs Robin (tails = Y = X_cross = ε = 0, n/h_p := 1) | all p ≥ 1386 (core δ) / 1390 (δ = 2.470e-6, G ≤ 15 part only; increases once the G > 15 tail is added); **first prime 1399** | [P-arith: float/mpmath evaluation + monotonicity] (N18b a_crossover_v2.py with robin() corrected to 0.6483/ln L; lineN16 §2a) |")
Rline("| Gas vs Robin crossover, first prime 1399", "| Gas vs Robin crossover: all p ≥ 1386 (core) / 1390 (δ_true, G ≤ 15); first prime 1399 | [P-arith] (lineN16) | N18b a_crossover_v2.py (robin() fixed) |")
Rline("| Gas vs Robin, first prime 1399", "| Gas vs Robin, first prime 1399 | [P-arith] | N18b a_crossover_v2.py; corrected N19b a_crossover_v3.py | lineN15 §2(b); lineN16 §2a ✓ after robin() fix (1386/1390; first prime 1399); monotonicity ✓ |")
# E2
R("[N]: scalar torus mean = i.i.d. to ~1e-11; carries cancel across 3 steps; carry correction ≤ 2e-9 relative (n ≤ 12); prefactor does not converge.",
  "[N]: carry sums with |e| ≤ 3 (n ≤ 6) and |e| ≤ 1 (n ≤ 12) equal the i.i.d. value to relative ≤ 1.7e-9 (≈1.35e-11 for n ≥ 5; reproduced without cancellation, lineN16); |e| ≥ 4 not computed ([H] negligible: isolated-carry entry weights 7e-3, 3e-8, 2e-15 for c = 1, 2, 3); N15's apparent prefactor non-convergence was an artefact of the share proxy (N16 §1). Labels (N16-1): the carry reduction and torus identity are [P]; the shell sums entering them are [CA-fp].")
# E3
R("Vector-chain conversion per window: E/\\|r\\| ≈ 1.7e-3 [P-sketch lemma, CA-fp numerics], giving δ_true(G ≤ 15) ≤ 2.470e-6. G > 15 true tail flat in G under box widening, so not controlled (N16 §2).",
  "Vector-chain conversion per window: E/\\|r\\| ≈ 2e-3 for singles, ≈ 8% (median) for pair windows, max 5.27 [P-sketch lemma (the written lemma must include the second-order dPi²·‖Q‖ term), CA-fp numerics], giving δ_true(G ≤ 15) ≤ 2.470e-6. Under box widening the G > 15 bound is flat (≈1.5e-7 per G), so it is not controlled. The pair-window error is dominated (≈93%) by the accumulated per-step core→true perturbation, so a difference-form conversion must cancel that term, not only the end-projector term (N16 §2; lineN16 §1).")
R("**OPEN; now = \"difference-form (pair-minus-product) conversion + G > 15 true-functional tail\".**","**OPEN; now = \"difference-form (pair-minus-product) conversion cancelling the per-step perturbation (dominant) and end-projector terms + G > 15 true-functional tail\"** (lineN16 §5; N16-2: N16 §2's end-projector diagnosis is superseded).")
# E4
R("with S_ρ ≥ c·1.13288^m (TRACE-271: 1.13287)","with S_ρ ≥ c·1.13287^m (TRACE-271; μ²/ε^{4/3} = 1.1328794)")
# E5
Rline("- **Small-p evidence is numerical only.**","- **Small-p evidence is numerical only.** Exact-enumeration W′ tables exist for m ≤ 17 (p ≤ 5); level data at m = 21, 33, 39 (p ≤ 13) come from the I2′ formula. All of it is [N] and is not evidence for the asymptotic statement.")
# E6 §3
Rline("| Step-norm table \\|t\\| > 1/256, max 2.91656, SVD-free |","| Step-norm table \\|t\\| > 1/256, max 2.91656, SVD-free | [CA-fp] (method refereed lineN15 §1a; values not independently recomputed) | N15 nh_table_rig.py |")
Rline("| Lemma 1 (sublattice separation) |","| Lemma 1 (sublattice separation; squarefree d, split primes) | [P] (refereed lineN16 §2b; C = 16λ²δ²h²λ^{−p}) | N14b §2, REPORT_N17b_v2 §6 |")
# E6 §8
Rline("| Lemma 1 | [P] pending |","| Lemma 1 | [P] | N14b §2; N17b_v2 §6 (erratum N19b REPORT_N17b_v3) | lineN16 §2b ✓ |")
Rline("| Carry correction ≤ 2e-9 |","| Carry correction ≤ 2e-9 | [N] | N16 g_scalar.py, g_triple.py | lineN16 §1(a) ✓ reproduced |")
Rline("| δ_true(G ≤ 15) ≤ 2.470e-6 | [CA-fp]+[P-sketch] |","| δ_true(G ≤ 15) ≤ 2.470e-6 | [CA-fp]+[P-sketch] | N16 conv_vec.py, f_post_true.json | lineN16 §1(c–d) ✓ numerics; lemma [P-sketch] |")
Rline("| A_bad j ≤ 12 = 2.031569e-6 |","| A_bad j ≤ 12 = 2.031569e-6 | [CA-fp] | N15 a_cert3.py | lineN14 ✓; lineN16 §1(e) ✓ (10 classes bit-identical; aggregate) |")
Rline("| Step-norm table \\|t\\| > 1/256 | [CA-fp] | N15 | not refereed |","| Step-norm table \\|t\\| > 1/256 | [CA-fp] | N15 | lineN15 §1a (method) |")
# E6 optional row
R("| Theorem W range |","| N15b literature note (H5) / N16b units note (H8) | author notes | N15b, N16b | not refereed |\n| Theorem W range |")
# E6 §7 item 6
R("Lemma 1 referee of the written proof;","Lemma 1 done ([P], lineN16);")
# E7
R("## 7. Referee findings reflected","- N18b a_crossover_v2.py Robin term 0.6483/ln K_p (should be /ln ln K_p): crossovers 1382/1386 and \"12.77 at p = 1289\" superseded by 1386/1390 and 12.85 (lineN16).\n\n## 7. Referee findings reflected")
# §9 map entry 2 numbers (R1 downstream) and changelog
R("p₁ [P-arith, float + monotonicity], first prime 1399.","p₁ [P-arith, float + monotonicity], first prime 1399 (numbers corrected in v4: 1386/1390).")
s=s.rstrip('\n')+"""

## 10. Changes v3 → v4 (referee lineN16 §4)
- **E1:** p₁ row, §3 crossover row and §8 crossover row now read 1386 (core) / 1390 (δ_true, G ≤ 15), first prime 1399. Robin term fixed (N19b a_crossover_v3.py reproduces lineN16 §2a; REPORT_N17b_v3).
- **E2:** H1 row [N] sentence replaced; N16-1 label split noted.
- **E3:** H4 row conversion sentence replaced; H4 definition now names the per-step perturbation term (N16-2).
- **E4:** scale 1.13287^m.
- **E5:** plain-summary small-p bullet replaced.
- **E6:** referee-status cells in §3, §8 and §7 item 6 updated; optional N15b/N16b author-notes row added.
- **E7:** §6 erratum for the N18b Robin term.
- Lemma 1 is now [P] (lineN16 §2b), with cosmetic fixes L1-a/L1-b in N19b/REPORT_N17b_v3.md.
"""
open('/workspace/bgs-lineN/THEOREM_DRAFT_v4.md','w').write(s+"\n" if not s.endswith("\n") else s)
print("ok")

# Post-step applied in N19b after running this script: in the verbatim E2 text, '|e|' was escaped to '\\|e\\|' inside the table row (rendering-identical).
