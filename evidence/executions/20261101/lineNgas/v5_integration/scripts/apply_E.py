import sys
src='/workspace/bgs-lineN/THEOREM_DRAFT_v5.md'
t=open(src,encoding='utf-8').read()
E=[
('E1a','[P] + [CA-fp], refereed lineN21/lineN21b. **H4 is no longer an input.**',
 '[P] + [CA-fp], refereed lineN21/lineN21b, given the standing-package constants taken as certified (N8 n_cert constants, N13 V1–V3b, Line F F2, N6 symmetry), as for H2. **H4 is no longer an input.**'),
('E1b','[P + CA mod H1-shell; span bound P-sketch]','[P + CA mod H1-shell; span bound and background interplay P-sketch]'),
('E2','  - first prime **3307** under H1 as stated (C ≤ 0.082);\n  - first prime **1409** if H1 holds with C ≤ 8.8e-4 (2× the measured finite-shell constant).\n',
 '  - first prime **3307** under H1 as stated (C ≤ 0.082), rate budgets only (additive budgets idealised, item (iv)), and sensitive to the [P-sketch] background normalisation of A_bad^KP (+1% → 3359; referee lineN22);\n  - first prime **1409** under a strengthened H1 with C ≤ 8.8e-4 (2× the measured finite-shell constant; by Prop. F the finite shells are not evidence for the tail). This value is robust (1409 up to 2× A_bad^KP).\n'),
('E3','[P-sketch: the same log→modulus step as H3 (background interplay [P-sketch])]. **Flagged for the referee.**',
 'Precisely: |ln Ξ_bad| ≤ Σ_γ |w̃(γ)| e^{a|γ|} ≤ p·S₀(a) (anchored KP corollary, Ueltschi 2004 Thm 1), so |Ξ_bad| ≥ e^{−pS₀(a)}; the charge is the weighted S₀(a), not a. Here w̃ are the bad activities renormalised by the model background, and S₀ must be evaluated with w̃ [P-sketch, as H3 background interplay]. Refereed lineN22: correct and necessary (no sign information on bad clusters); 3307 moves by ≈ +50 per +1% in S₀, 1409 is stable.'),
('E4a','(N11-F4).','(N11-F4). This is the model-gas bound; with the bad clusters (H3) the factor is e^{−p(δ + A_bad^KP)} (§2).'),
('E4b','| \\|1+X_gas\\| ≥ 2(1+Re Λ)^p e^{−pδ} − 1 | [P given the model form] |',
 '| \\|1+X_gas\\| ≥ 2(1+Re Λ)^p e^{−pδ} − 1 (model gas; with bad clusters e^{−p(δ + A_bad^KP)}, §2) | [P given the model form]; bad-cluster factor [P-sketch] |'),
('E5','the v5 A_bad^KP correction of the exponent is not yet refereed]','the v5 A_bad^KP correction of the exponent is [P-sketch], refereed lineN22 (correct, necessary)]'),
('E6','[P-arith: float/mpmath + monotonicity, N19b logic verbatim (`V5/code/crossover_v5.py`)]',
 '[P-arith: float + exact big-int K_p + monotonicity, N19b logic verbatim (`V5/code/crossover_v5.py`); independently reproduced in mpmath (referee lineN22; C = 0.04 with unrounded input: 1725/1733)]'),
('E7a','A_bad-in-exponent step not yet refereed','lineN22 ✓ (all rows reproduced; A_bad-in-exponent step correct, [P-sketch])'),
('E7b','| KP a = 5.93e-6 | [P]/[CA-fp]/[H] tail | N15 kp.py | lineN15 §1d (F1, F2) |',
 '| KP a = 5.93e-6 (**superseded**: used the withdrawn tail placeholder; now a = a(C), Prop. K) | [P]/[CA-fp]/[H] tail | N15 kp.py | lineN15 §1d (F1, F2) |'),
('E8','  - a referee pass on the A_bad^KP-in-exponent step and on this assembly;','  - (done: referee lineN22, GO after E1–E12);'),
]
LINE={'E1b':20}
for name,old,new in E:
    if name in LINE:
        L=t.split('\n'); i=LINE[name]-1
        assert L[i].count(old)==1, name
        L[i]=L[i].replace(old,new); t='\n'.join(L); print(name,'ok (line-scoped)'); continue
    n=t.count(old)
    if n!=1: sys.exit(f'{name}: occurs {n} times')
    t=t.replace(old,new)
    print(name,'ok')
open('THEOREM_DRAFT_v5_E1E8.md','w',encoding='utf-8').write(t)
