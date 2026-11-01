import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# BGS-FM-026 — bookkeeping arithmetic of the simple-eigenvalue counts on `N = 7·5^e`

Source: `mathematics/fixed-map/literal_time_multiplicity_bounds.md`; registry boundary of `BGS-FM-026`.

* `count_integral` : for `N = 7·5^e`, `25 ∣ N` (`e ≥ 2`) and `625 ∣ N` (`e ≥ 4`), so `24N/25` and `612N/625` are integers;
  `24N/25 = 600N/625`;
* `special_4375` : at `N = 4375` (`e = 4`), `24N/25 = 4200` and `4200 + 18·7 + 7 = 4333`, and `4333 ≥ 612N/625 + 7`;
* `special_109375` : at `N = 109375` (`e = 6`), `24N/25 = 105000` and `105000 + 324·7 + 175 = 107443`, and
  `107443 ≥ 612N/625 + 175`;
* `core_875` : `875 = 840 + 35` (the odd `e ≥ 7` core, the 35 counted once).

**Partial coverage:** only the additive bookkeeping is formalized.  The multiplicity bound `≤ 7` for every nonzero real
algebraic `t`, the splitting mechanisms that supply each summand (first-old blocks, residual-25 splitting, the deepest
cores, the newest sector) and the bounded simple `U` at `N = 35, 175` rest on the exact certificates
(`cat_jet_certificates.py`, `intermediate_old_layers_certificates.py`, `residual125_certificates.py`,
`odd_newest_certificates.py`) and are **not** formalized.  All proofs are kernel-checked.
-/

namespace Bgs.Fm026Counts

def Nof (e : ℕ) : ℕ := 7 * 5 ^ e

theorem count_integral (e : ℕ) :
    (2 ≤ e → 25 ∣ Nof e) ∧ (4 ≤ e → 625 ∣ Nof e) ∧ (4 ≤ e → 24 * Nof e / 25 = 600 * Nof e / 625) := by
  refine ⟨fun he => ?_, fun he => ?_, fun he => ?_⟩
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le he
    exact ⟨7 * 5 ^ k, by unfold Nof; ring⟩
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le he
    exact ⟨7 * 5 ^ k, by unfold Nof; ring⟩
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le he
    have h1 : 24 * Nof (4 + k) = 25 * (24 * 7 * 25 * 5 ^ k) := by unfold Nof; ring
    have h2 : 600 * Nof (4 + k) = 625 * (24 * 7 * 25 * 5 ^ k) := by unfold Nof; ring
    rw [h1, h2, Nat.mul_div_cancel_left _ (by norm_num), Nat.mul_div_cancel_left _ (by norm_num)]

theorem special_4375 :
    Nof 4 = 4375 ∧ 24 * Nof 4 / 25 = 4200 ∧ 4200 + 18 * 7 + 7 = 4333 ∧ 612 * Nof 4 / 625 + 7 ≤ 4333 := by
  unfold Nof; norm_num

theorem special_109375 :
    Nof 6 = 109375 ∧ 24 * Nof 6 / 25 = 105000 ∧ 105000 + 324 * 7 + 175 = 107443 ∧
      612 * Nof 6 / 625 + 175 ≤ 107443 := by
  unfold Nof; norm_num

theorem core_875 : 840 + 35 = 875 := by norm_num

end Bgs.Fm026Counts
