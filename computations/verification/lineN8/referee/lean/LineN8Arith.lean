import Mathlib
set_option exponentiation.threshold 20000
set_option maxRecDepth 200000

/-! Referee arithmetic checks for BGS Lines N8 / N8b (Grok Bot audit). norm_num and kernel decide on Nat only. -/

/-- N8 §1: absolute-class total. Upper bounds of |w| for the 10 'absolute' classes sum to <= 1.2165e-6,
 and (with 10 x 1e-9 Prop X' errors) this is <= 0.43% of Re w*_lo = 2.8895e-4. -/
theorem abs_total :
    (4467:ℚ)/10^10 + 2*616/10^10 + 2*512/10^10 + 2*2636/10^10 + 114/10^10 + 32/10^10 + 19/10^10 ≤ 12165/10^10 := by norm_num
theorem abs_share : ((12165:ℚ)/10^10 + 10/10^9) / (28895/10^8) ≤ 43/10000 := by norm_num

/-- N8 §2(iii): p0 = 4(w0 + L_e) + 5 for the near-0 class (w0 = 320, L_e = 1). -/
theorem p0_near0 : 4*(320+1)+5 = 1289 := by norm_num

/-- N8 §2(ii): other-sector absorption at p = 485 (m = 1455), family cores 6 x 39 steps, cleared to naturals:
 3 * TN * Bop^234 * (C_a*1.0001)^7 <= 1e-6 * Re w*_lo * (mu^m - 3013)/2 * 0.999 with TN <= 730.15, Bop <= 40.85,
 C_a <= 739.91, mu >= 1.9154712, i.e. (all scaled by 10^k)
 3*73015*4085^234*(73991*10001)^7 * 10^6*10^8*2*1000*10^(7*1455) <= 100*100^234*(10^6)^7 * 28895*(19154712^1455 - 3013*10^(7*1455))*999 -/
theorem other_sector_485 :
    3*73015*4085^234*(73991*10001)^7 * (10^6*10^8*2*1000*10^(7*1455))
      ≤ 100*100^234*(10^6)^7 * 28895*(19154712^1455 - 3013*10^(7*1455))*999 := by decide

/-- N8b §7: kappa floor (1/2 ln lam)/(2 ln mu* - ln r2) >= 0.706, exponential form (mu^2/r2)^353 <= lam^250
 with mu <= 1.91548, r2 <= 1.0529012 (certified), lam >= 5.8284; mu^2/r2 = 191548^2/(1000*10529012). -/
theorem kappa_floor : (191548^2)^353 * 10^(4*250) ≤ 58284^250 * (1000*10529012)^353 := by decide
/-- kappa < 0.7062: lam^3531 < (mu^2/r2)^10000/... i.e. 0.7062*(2 ln mu - ln r2) > (1/2) ln lam, with mu >= 1.9154712,
 r2 >= 1.0529, lam <= 5.8285: 58285^3531 * (10^10*10529)^5000 < 19154712^10000 * 10^(4*3531) -/
theorem kappa_upper : 58285^3531 * (10^10*10529)^5000 < 19154712^10000 * 10^(4*3531) := by decide

/-- N8b §7: fixed-point value mu*^2/lam in [0.6294, 0.6296]. -/
theorem fp_r2 : ((19154712:ℚ)/10^7)^2/(58285/10^4) ≥ 6294/10^4 ∧ ((19154753:ℚ)/10^7)^2/(58284/10^4) ≤ 6296/10^4 := by norm_num

/-- N8b §7: s = 3 floor mu*^3/lam in [1.2057, 1.2059]. -/
theorem fp_R3 : ((19154712:ℚ)/10^7)^3/(58285/10^4) ≥ 12057/10^4 ∧ ((19154753:ℚ)/10^7)^3/(58284/10^4) ≤ 12059/10^4 := by norm_num

/-- Referee improvement of N7 F5 using N8b §1(vi) (every prime r | h_p has r = 1 mod 2p): with omega <= 132 distinct primes,
 the j-th smallest is >= 2pj+1, so sum 2/r_i <= (1/p) * H_132 <= 6/1165 < 0.0052 at p = 1165 (vs 11.4%). -/
theorem harmonic132 : (∑ j ∈ Finset.range 132, (1:ℚ)/(j+1)) ≤ 6 := by
  simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num
theorem loss_improved : (6:ℚ)/1165 < 52/10000 := by norm_num
theorem fm_improved : (23344:ℚ)/10^7*(1 - 52/10000) ≥ 232/10^5 := by norm_num
