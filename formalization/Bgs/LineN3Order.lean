import Bgs.LineMArith
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Algebra.Field.ZMod

/-!
# BGS-TRACE-291 — Line N3 Lemma 1.1: `l = λ mod q'` has order exactly `p`

Source: `mathematics/fixed-map/lineN2N4_inherited_level.md`, Lemma 1.1;
registry boundary of `BGS-TRACE-291`: "`l` has order exactly `p`: it
divides `p` since `λ^p − 1 = 2 h_p ε^p` (BGS-TRACE-277), and is not `1`
since `N(λ − 1) = −4` (`q` odd)."

Formal setting: `p` an odd prime, `q` an odd prime with `q ∣ h_p`
(`h_p = nsw p`), and `q` split in `ℤ[√2]`, encoded by a square root
`s ∈ 𝔽_q` of `2`; the prime `q'` above `q` is the kernel of the ring map
`φ_s : ℤ[√2] → 𝔽_q`, `√2 ↦ s`, and `l = φ_s(λ)`, `λ = ε² = (1 + √2)²`.

* `norm_lam_sub_one` : `N(λ − 1) = −4`;
* `l_pow_p` : `l^p = 1`;
* `l_ne_one` : `l ≠ 1`;
* `orderOf_l` : `orderOf l = p`.

The statement holds for *either* choice of `s` (both primes above `q`).
**Not formalized (partial coverage of BGS-TRACE-291):** the description
of the twist sequences `τ_i(β) = s l^i / q` (isotropic `β`) and
`(s₁ l^i + s₂ l^{−i})/q` (unit `β`), and the orbit count.
No `sorry`, no `native_decide`.
-/

namespace Bgs.LineN3Order

open Bgs.LineIArith Bgs.LineG Bgs.LineM

/-- `λ = ε² = 3 + 2√2`. -/
def lam : ℤ√2 := α ^ 2

theorem lam_eq : lam = ⟨3, 2⟩ := by
  simp [lam, α, pow_two, Zsqrtd.ext_iff]

/-- `N(λ − 1) = −4`. -/
theorem norm_lam_sub_one : (lam - 1).norm = -4 := by
  rw [lam_eq]; simp [Zsqrtd.norm]

section

variable (p : ℕ) (hp : p.Prime) (hpo : Odd p) (q : ℕ) [hq : Fact q.Prime] (hq2 : q ≠ 2)
  (hqh : (q : ℤ) ∣ nsw p) (s : ZMod q) (hs : s * s = 2)

/-- The ring map `φ_s : ℤ[√2] → 𝔽_q`, `√2 ↦ s`. -/
noncomputable def phi (q : ℕ) (s : ZMod q) (hs : s * s = 2) : ℤ√2 →+* ZMod q :=
  Zsqrtd.lift ⟨s, by rw [hs]; norm_num⟩

include hpo hqh in
/-- `l^p = 1`, from `λ^p = 1 + 2 h_p ε^p` and `q ∣ h_p`. -/
theorem l_pow_p : (phi q s hs lam) ^ p = 1 := by
  have h := congrArg (phi q s hs) (lam_pow_eq hpo)
  have hz : ((nsw p : ℤ) : ZMod q) = 0 := (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mpr hqh
  rw [map_add, map_one, map_mul, map_mul, map_intCast, hz, mul_zero, zero_mul, add_zero] at h
  rw [← map_pow, lam, ← pow_mul]
  exact h

include hq2 in
/-- `l ≠ 1`, since `φ_s(λ − 1) · φ_s(conj(λ − 1)) = N(λ − 1) = −4 ≠ 0` in `𝔽_q`. -/
theorem l_ne_one : phi q s hs lam ≠ 1 := by
  intro h1
  have hn : ((lam - 1).norm : ℤ√2) = (lam - 1) * star (lam - 1) := Zsqrtd.norm_eq_mul_conj _
  have h := congrArg (phi q s hs) hn
  rw [map_mul, map_sub, h1, map_one, sub_self, zero_mul, norm_lam_sub_one, map_intCast] at h
  have h4 : ((4 : ℕ) : ZMod q) = 0 := by
    have : ((-4 : ℤ) : ZMod q) = -((4 : ℕ) : ZMod q) := by push_cast; ring
    rw [this] at h; exact neg_eq_zero.mp h
  rw [ZMod.natCast_eq_zero_iff] at h4
  have h2 : q ∣ 2 ^ 2 := by simpa using h4
  have := (Nat.prime_dvd_prime_iff_eq hq.out Nat.prime_two).mp (hq.out.dvd_of_dvd_pow h2)
  exact hq2 this

include hp hpo hq2 hqh in
/-- **Lemma 1.1 (order part): `l = λ mod q'` has order exactly `p`.** -/
theorem orderOf_l : orderOf (phi q s hs lam) = p := by
  have : Fact p.Prime := ⟨hp⟩
  exact orderOf_eq_prime (l_pow_p p hpo q hqh s hs) (l_ne_one q hq2 s hs)

end

end Bgs.LineN3Order
