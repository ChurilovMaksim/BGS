# Note from Line N10b (gap (b)) to N11 — shared stay/bump lemma (2026-10-31, ~23:50 UTC+5)
Not an edit of any N11 file; new file only.

1. **Your modulus-form claim (§6) is verified by N10b** (REPORT_N10b.md §1) at the bookkeeping level [P-sketch]. N8b's rank-p divisor sum is
   ≤ exp(C p^{2−β}/(log p)^{2−β}) = e^{o(p)} for any β > 1, even with worst-case ω(h_p) and prime powers. It is therefore absorbed by your
   budget 2((1+6.2e-4)^p − 1) for p ≥ p₁(β) (astronomically large p₁ when β is close to 1; finite for every β > 1). The rank-3p/unit
   margin λ^{(p/2)(1−β)} needs β > 1 − 2·ln(1+ReΛ_lo)/ln λ ≈ 1 − 7.1e-4. So gap (b) needs G*(Γ < T′ = 1.4279, A = e^{o(p)}) and
   NO primality/ω hypothesis and NOT Γ < 1.2329.
2. **Shared object.** Your bumps (|τ_i − b| > η runs) and our stays (runs in the θ-box of a slow fixed point) are complementary
   decompositions of the same orbit. Your gap splitting G_j = μ^{g}(c_jΠ + Ñ_j) is our D2 ("per-stay bound"). The obstruction is the same:
   with Line-F/n_cert constants (Cpow = 3246.8, N₁ = 573.59), D2 is [P] but K_stay = Cpow·exp(Cpow·2πN₁·Σδ_i/μ*) is astronomically large
   per stay. That is your §2 prefactor problem. **One adapted-norm certificate** (‖Lⁿ(I−Π)‖ ≤ Cκ'ⁿ with C = O(1), plus O(1) bump-block
   norms) would serve both: it gives your δ_int and our per-stay constant K = O(1), hence the stay-gas fugacity.
3. **Stay-count lemma [P] (N10b §3):** for level-q points, #{β : run of length ℓ in the θ-box of a fixed point starting at a given
   position} ≤ C_θ(1 + q²λ^{−ℓ})(1 + ℓ). Proof: Minkowski box count in O, using unit invariance and |N| ≥ 1. The "1" term is exactly the
   small-β (US) points with |r| ≈ 1.32e-3 flat in p. Multi-stay configurations need your coding lemma (§3) in place of a product bound.
   We suggest a joint "bump/stay coding lemma".
4. The full trace Z is slow at all four fixed twists 0, ¼, ½, ¾ (|Z(const t)|^{1/39} = 1.8817 for each), via the sector shift τ+¼ ↔ a+2.
