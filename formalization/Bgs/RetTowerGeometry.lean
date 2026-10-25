import Std
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases

/-! Finite-geometry certificate for BGS-RET-004, §3 of
    `mathematics/returns/noncommuting_return_words.md`.

    Certified here: the explicit finite data that makes the four levels
    `E_j = S^{-j} E` (j = 0, 1, 2, 3) pairwise disjoint, where
    `T = [[3, 2], [4, 3]]`, `S = Tᵀ = [[3, 4], [2, 3]]`, `r = 1/96`,
    `z = (5/11, 0)`, and `E` is the pair of closed torus squares of
    halfwidth `r` centred at `z` and `-z`.

    Concretely: the cube `S³ = [[99, 140], [70, 99]]`; the image centre
    `S³ z = (45, 350/11)`; the separating normal `w = (-70, 99)`, which
    annihilates the first column of `S³` and takes value `1` on the
    second, so that the right-hand side of the separation inequality
    (RW14) at `j = 3` is uniformly `85/48`; the 30 separation
    inequalities (RW14) for the `j = 3` candidates (15 per sign);
    completeness of the `j = 3` candidate enumeration; emptiness of the
    `j = 1` and `j = 2` candidate rectangles; the lobe gap `37/528`;
    and the total support area `32 r² = 1/288 < 1`.

    NOT certified here: the analytic statements RW3/RW7 (operator-norm
    `O(N^-∞)` conjugacy), the bracket computation, and hence the full
    return-word claim. This module certifies the finite certificate
    only, in the same kernel style as the other finite modules. -/
namespace Bgs.RetTowerGeometry

/-- `S²` and `S³` for `S = [[3, 4], [2, 3]]`, by explicit entrywise
    multiplication. -/
theorem s3_entries :
    (3 * 3 + 4 * 2 = 17 ∧ 3 * 4 + 4 * 3 = 24 ∧
      2 * 3 + 3 * 2 = 12 ∧ 2 * 4 + 3 * 3 = 17) ∧
    (17 * 3 + 24 * 2 = 99 ∧ 17 * 4 + 24 * 3 = 140 ∧
      12 * 3 + 17 * 2 = 70 ∧ 12 * 4 + 17 * 3 = 99) := by
  norm_num

/-- `S³ ∈ SL(2, ℤ)`: its determinant is `1`. -/
theorem s3_det : (99 : ℤ) * 99 - 140 * 70 = 1 := by decide

/-- The image centre `S³ z` for `z = (5/11, 0)`. -/
theorem mz_entries : (99 : ℚ) * (5 / 11) = 45 ∧ (70 : ℚ) * (5 / 11) = 350 / 11 := by
  norm_num

/-- The separating normal `w = (-70, 99)` annihilates the first column
    of `S³` and takes value `1` on the second column. -/
theorem w_dots : (-70 : ℚ) * 99 + 99 * 70 = 0 ∧ (-70 : ℚ) * 140 + 99 * 99 = 1 := by
  norm_num

/-- The right-hand side of (RW14) at `j = 3` for `w = (-70, 99)`:
    `r * (‖w‖₁ + |w · col₀| + |w · col₁|) = (1/96) * (169 + 0 + 1)`. -/
theorem w_rhs : (1 : ℚ) / 96 * ((70 + 99) + 0 + 1) = 85 / 48 := by norm_num

/-- The 30 separation inequalities (RW14) for `j = 3`.
    For sign `+1` the displacement is `n - S³z + z`, i.e. the first
    coordinate is `n₀ - 45 + 5/11`; for sign `-1` it is `n₀ - 45 - 5/11`.
    The second coordinate is `n₁ - 350/11` in both cases. Each statement
    is `|w · d| > 85/48` with `w = (-70, 99)`. -/
theorem sep_p_43_31 : |(-70 : ℚ) * ((43 : ℚ) - 45 + 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_43_32 : |(-70 : ℚ) * ((43 : ℚ) - 45 + 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_43_33 : |(-70 : ℚ) * ((43 : ℚ) - 45 + 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_44_31 : |(-70 : ℚ) * ((44 : ℚ) - 45 + 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_44_32 : |(-70 : ℚ) * ((44 : ℚ) - 45 + 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_44_33 : |(-70 : ℚ) * ((44 : ℚ) - 45 + 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_45_31 : |(-70 : ℚ) * ((45 : ℚ) - 45 + 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_45_32 : |(-70 : ℚ) * ((45 : ℚ) - 45 + 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_45_33 : |(-70 : ℚ) * ((45 : ℚ) - 45 + 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_46_31 : |(-70 : ℚ) * ((46 : ℚ) - 45 + 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_46_32 : |(-70 : ℚ) * ((46 : ℚ) - 45 + 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_46_33 : |(-70 : ℚ) * ((46 : ℚ) - 45 + 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_47_31 : |(-70 : ℚ) * ((47 : ℚ) - 45 + 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_47_32 : |(-70 : ℚ) * ((47 : ℚ) - 45 + 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_p_47_33 : |(-70 : ℚ) * ((47 : ℚ) - 45 + 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_43_31 : |(-70 : ℚ) * ((43 : ℚ) - 45 - 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_43_32 : |(-70 : ℚ) * ((43 : ℚ) - 45 - 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_43_33 : |(-70 : ℚ) * ((43 : ℚ) - 45 - 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_44_31 : |(-70 : ℚ) * ((44 : ℚ) - 45 - 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_44_32 : |(-70 : ℚ) * ((44 : ℚ) - 45 - 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_44_33 : |(-70 : ℚ) * ((44 : ℚ) - 45 - 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_45_31 : |(-70 : ℚ) * ((45 : ℚ) - 45 - 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_45_32 : |(-70 : ℚ) * ((45 : ℚ) - 45 - 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_45_33 : |(-70 : ℚ) * ((45 : ℚ) - 45 - 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_46_31 : |(-70 : ℚ) * ((46 : ℚ) - 45 - 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_46_32 : |(-70 : ℚ) * ((46 : ℚ) - 45 - 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_46_33 : |(-70 : ℚ) * ((46 : ℚ) - 45 - 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_47_31 : |(-70 : ℚ) * ((47 : ℚ) - 45 - 5 / 11) + 99 * ((31 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_47_32 : |(-70 : ℚ) * ((47 : ℚ) - 45 - 5 / 11) + 99 * ((32 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num
theorem sep_m_47_33 : |(-70 : ℚ) * ((47 : ℚ) - 45 - 5 / 11) + 99 * ((33 : ℚ) - 350 / 11)| > 85 / 48 := by norm_num

/-- Completeness of the `j = 3` candidate enumeration, sign `+1`:
    any integer pair in the candidate rectangle is one of the 15 pairs
    `(43..47) × (31..33)`. The rectangle is
    `|n₀ - 490/11| ≤ 5/2`, `|n₁ - 350/11| ≤ 85/48`. -/
theorem cand_j3_p_complete (n0 n1 : ℤ)
    (h0 : |(n0 : ℚ) - 490 / 11| ≤ 5 / 2)
    (h1 : |(n1 : ℚ) - 350 / 11| ≤ 85 / 48) :
    (n0 = 43 ∧ n1 = 31) ∨ (n0 = 43 ∧ n1 = 32) ∨ (n0 = 43 ∧ n1 = 33) ∨
    (n0 = 44 ∧ n1 = 31) ∨ (n0 = 44 ∧ n1 = 32) ∨ (n0 = 44 ∧ n1 = 33) ∨
    (n0 = 45 ∧ n1 = 31) ∨ (n0 = 45 ∧ n1 = 32) ∨ (n0 = 45 ∧ n1 = 33) ∨
    (n0 = 46 ∧ n1 = 31) ∨ (n0 = 46 ∧ n1 = 32) ∨ (n0 = 46 ∧ n1 = 33) ∨
    (n0 = 47 ∧ n1 = 31) ∨ (n0 = 47 ∧ n1 = 32) ∨ (n0 = 47 ∧ n1 = 33) := by
  rw [abs_le] at h0 h1
  have b0 : 925 ≤ 22 * n0 ∧ 22 * n0 ≤ 1035 := by
    constructor
    · have h : (925 : ℚ) ≤ 22 * (n0 : ℚ) := by linarith [h0.1]
      exact_mod_cast h
    · have h : 22 * (n0 : ℚ) ≤ 1035 := by linarith [h0.2]
      exact_mod_cast h
  have b1 : 15865 ≤ 528 * n1 ∧ 528 * n1 ≤ 17735 := by
    constructor
    · have h : (15865 : ℚ) ≤ 528 * (n1 : ℚ) := by linarith [h1.1]
      exact_mod_cast h
    · have h : 528 * (n1 : ℚ) ≤ 17735 := by linarith [h1.2]
      exact_mod_cast h
  have c0lo : 43 ≤ n0 := by omega
  have c0hi : n0 ≤ 47 := by omega
  have c1lo : 31 ≤ n1 := by omega
  have c1hi : n1 ≤ 33 := by omega
  interval_cases n0 <;> interval_cases n1 <;> simp

/-- Completeness of the `j = 3` candidate enumeration, sign `-1`:
    the rectangle is `|n₀ - 500/11| ≤ 5/2`, `|n₁ - 350/11| ≤ 85/48`,
    and it contains the same 15 integer pairs. -/
theorem cand_j3_m_complete (n0 n1 : ℤ)
    (h0 : |(n0 : ℚ) - 500 / 11| ≤ 5 / 2)
    (h1 : |(n1 : ℚ) - 350 / 11| ≤ 85 / 48) :
    (n0 = 43 ∧ n1 = 31) ∨ (n0 = 43 ∧ n1 = 32) ∨ (n0 = 43 ∧ n1 = 33) ∨
    (n0 = 44 ∧ n1 = 31) ∨ (n0 = 44 ∧ n1 = 32) ∨ (n0 = 44 ∧ n1 = 33) ∨
    (n0 = 45 ∧ n1 = 31) ∨ (n0 = 45 ∧ n1 = 32) ∨ (n0 = 45 ∧ n1 = 33) ∨
    (n0 = 46 ∧ n1 = 31) ∨ (n0 = 46 ∧ n1 = 32) ∨ (n0 = 46 ∧ n1 = 33) ∨
    (n0 = 47 ∧ n1 = 31) ∨ (n0 = 47 ∧ n1 = 32) ∨ (n0 = 47 ∧ n1 = 33) := by
  rw [abs_le] at h0 h1
  have b0 : 945 ≤ 22 * n0 ∧ 22 * n0 ≤ 1055 := by
    constructor
    · have h : (945 : ℚ) ≤ 22 * (n0 : ℚ) := by linarith [h0.1]
      exact_mod_cast h
    · have h : 22 * (n0 : ℚ) ≤ 1055 := by linarith [h0.2]
      exact_mod_cast h
  have b1 : 15865 ≤ 528 * n1 ∧ 528 * n1 ≤ 17735 := by
    constructor
    · have h : (15865 : ℚ) ≤ 528 * (n1 : ℚ) := by linarith [h1.1]
      exact_mod_cast h
    · have h : 528 * (n1 : ℚ) ≤ 17735 := by linarith [h1.2]
      exact_mod_cast h
  have c0lo : 43 ≤ n0 := by omega
  have c0hi : n0 ≤ 47 := by omega
  have c1lo : 31 ≤ n1 := by omega
  have c1hi : n1 ≤ 33 := by omega
  interval_cases n0 <;> interval_cases n1 <;> simp

/-- Emptiness of the `j = 1`, sign `+1` candidate rectangle:
    centre `(10/11, 10/11)`, radii `(1/12, 1/16)`. The first coordinate
    already excludes every integer: `109 ≤ 132 n₀ ≤ 131` is impossible. -/
theorem noCand_j1_p (n0 n1 : ℤ) :
    ¬(|(n0 : ℚ) - 10 / 11| ≤ 1 / 12 ∧ |(n1 : ℚ) - 10 / 11| ≤ 1 / 16) := by
  rintro ⟨h0, -⟩
  rw [abs_le] at h0
  have b : 109 ≤ 132 * n0 ∧ 132 * n0 ≤ 131 := by
    constructor
    · have h : (109 : ℚ) ≤ 132 * (n0 : ℚ) := by linarith [h0.1]
      exact_mod_cast h
    · have h : 132 * (n0 : ℚ) ≤ 131 := by linarith [h0.2]
      exact_mod_cast h
  omega

/-- Emptiness of the `j = 1`, sign `-1` candidate rectangle:
    centre `(20/11, 10/11)`, radii `(1/12, 1/16)`. The first coordinate
    already excludes every integer: `229 ≤ 132 n₀ ≤ 251` is impossible. -/
theorem noCand_j1_m (n0 n1 : ℤ) :
    ¬(|(n0 : ℚ) - 20 / 11| ≤ 1 / 12 ∧ |(n1 : ℚ) - 10 / 11| ≤ 1 / 16) := by
  rintro ⟨h0, -⟩
  rw [abs_le] at h0
  have b : 229 ≤ 132 * n0 ∧ 132 * n0 ≤ 251 := by
    constructor
    · have h : (229 : ℚ) ≤ 132 * (n0 : ℚ) := by linarith [h0.1]
      exact_mod_cast h
    · have h : 132 * (n0 : ℚ) ≤ 251 := by linarith [h0.2]
      exact_mod_cast h
  omega

/-- Emptiness of the `j = 2`, sign `+1` candidate rectangle:
    centre `(80/11, 60/11)`, radii `(7/16, 5/16)`. The second coordinate
    excludes every integer: `905 ≤ 176 n₁ ≤ 1015` is impossible
    (the first coordinate alone would admit `n₀ = 7`). -/
theorem noCand_j2_p (n0 n1 : ℤ) :
    ¬(|(n0 : ℚ) - 80 / 11| ≤ 7 / 16 ∧ |(n1 : ℚ) - 60 / 11| ≤ 5 / 16) := by
  rintro ⟨-, h1⟩
  rw [abs_le] at h1
  have b : 905 ≤ 176 * n1 ∧ 176 * n1 ≤ 1015 := by
    constructor
    · have h : (905 : ℚ) ≤ 176 * (n1 : ℚ) := by linarith [h1.1]
      exact_mod_cast h
    · have h : 176 * (n1 : ℚ) ≤ 1015 := by linarith [h1.2]
      exact_mod_cast h
  omega

/-- Emptiness of the `j = 2`, sign `-1` candidate rectangle:
    centre `(90/11, 60/11)`, radii `(7/16, 5/16)`. As above, the second
    coordinate excludes every integer. -/
theorem noCand_j2_m (n0 n1 : ℤ) :
    ¬(|(n0 : ℚ) - 90 / 11| ≤ 7 / 16 ∧ |(n1 : ℚ) - 60 / 11| ≤ 5 / 16) := by
  rintro ⟨-, h1⟩
  rw [abs_le] at h1
  have b : 905 ≤ 176 * n1 ∧ 176 * n1 ≤ 1015 := by
    constructor
    · have h : (905 : ℚ) ≤ 176 * (n1 : ℚ) := by linarith [h1.1]
      exact_mod_cast h
    · have h : 176 * (n1 : ℚ) ≤ 1015 := by linarith [h1.2]
      exact_mod_cast h
  omega

/-- Gap between the two base lobes: centres `5/11` and `6/11` on the
    torus, minus two halfwidths `r = 1/96`. -/
theorem lobe_gap : ((6 : ℚ) / 11 - 1 / 96) - (5 / 11 + 1 / 96) = 37 / 528 := by
  norm_num

/-- Total area of the four support levels: 8 squares of side `2r`,
    i.e. `32 r² = 1/288 < 1`. -/
theorem support_area : 32 * ((1 : ℚ) / 96) ^ 2 = 1 / 288 ∧ (1 : ℚ) / 288 < 1 := by
  norm_num

#print axioms sep_p_43_31
#print axioms cand_j3_p_complete
#print axioms cand_j3_m_complete
#print axioms noCand_j1_p
#print axioms noCand_j1_m
#print axioms noCand_j2_p
#print axioms noCand_j2_m
#print axioms lobe_gap
#print axioms support_area

end Bgs.RetTowerGeometry
