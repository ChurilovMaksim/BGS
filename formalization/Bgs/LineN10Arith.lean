import Mathlib
/-! Lines N9, N10: referee arithmetic checks (`mathematics/fixed-map/lineN5N18_gas_conditional.md`).
Referee file `computations/verification/lineN10/referee/lean/LineN10Arith.lean` (sha256 93927501…), integrated verbatim inside the namespace `Bgs.LineN10`;
only `#print axioms` lines were added (one per theorem, 13). No sorry, no native_decide. -/
namespace Bgs.LineN10

/-! Referee arithmetic checks, Line N9/N10 (Grok Bot audit). Pure rational arithmetic; no sorry, no native_decide. -/

-- N9 §C': deep route needs q ≤ ((T'/1.2744)^3)^p ; (1.42785/1.2744)^3 ∈ (1.406, 1.4066) < eps = 1+√2 > 2.414
theorem idx_ratio_lo : (1406:ℚ)/1000 < (142785/127440:ℚ)^3 := by norm_num
theorem idx_ratio_hi : (142785/127440:ℚ)^3 < 14066/10000 := by norm_num
theorem eps_gt (s : ℝ) (hs : s*s = 2) (h0 : 0 ≤ s) : (14066:ℝ)/10000 < 1 + s := by nlinarith
-- N9 §B: joint automaton per lambda-step vs requirement
theorem joint_rate : (232569/100000:ℚ)^2 > 5408/1000 ∧ (1481/1000:ℚ)^2 < 21934/10000 := by norm_num
-- N10: R = 2*sum of activities (c0, c4, phi_{2√2}, phi_4)
theorem R_re_close : |2*((298660:ℚ)/10^10 + 10413/10^10 + 138/10^10 - 20/10^10) - 6185/10^8| < 2/10^8 := by norm_num [abs_lt]
theorem R_im_close : |2*(-(6599:ℚ)/10^9 - 31164/10^10 + 111/10^10 - 9/10^10) + 1943/10^8| < 3/10^8 := by norm_num [abs_lt]
-- N10 m=141 (p=47): Lin = 4p Re(w*+c0); modulus gain 1+|X|^2/(2 Re X)
theorem lin47 : |4*47*((343580:ℚ)/10^9 + 29866/10^9) - 70208/10^6| < 1/10^6 := by norm_num [abs_lt]
theorem modgain47 : let a : ℚ := 70632/10^6; let b : ℚ := 35041/10^6;
    (4400:ℚ)/10^5 < (a^2+b^2)/(2*a) ∧ (a^2+b^2)/(2*a) < 4402/10^5 := by norm_num
theorem lin_vs_gas47 : (70208:ℚ)/10^6 < 70632/10^6 := by norm_num
-- interaction ratio 0.769/1.915
theorem inter_ratio : (4015:ℚ)/10^4 < 769/1915 ∧ (769:ℚ)/1915 < 4016/10^4 := by norm_num
-- short-block table: 8V k=20 below the 1.4810 bar, 16E k=20 just above
theorem r2_k20 : (147591:ℚ)/10^5 < 14810/10^4 ∧ (14810:ℚ)/10^4 < 148126/10^5 := by norm_num
-- |Z|^2/h_p^2 growth: mu*^6/lambda with lambda < 5.8285
theorem growth : (847:ℚ)/100 < (19154712/10^7:ℚ)^6 / (58285/10^4) := by norm_num
theorem growth_hi : (19154712/10^7:ℚ)^6 / (58284/10^4) < 848/100 := by norm_num

#print axioms idx_ratio_lo
#print axioms idx_ratio_hi
#print axioms eps_gt
#print axioms joint_rate
#print axioms R_re_close
#print axioms R_im_close
#print axioms lin47
#print axioms modgain47
#print axioms lin_vs_gas47
#print axioms inter_ratio
#print axioms r2_k20
#print axioms growth
#print axioms growth_hi

end Bgs.LineN10
