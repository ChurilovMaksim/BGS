import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Matrix.Basic

/-!
# BGS-TRACE-216 — exact monomial intertwiners of the (±2,8) G2 automaton factors (finite part)

Source: `mathematics/fixed-map/lineI_rprime_reduction.md` §7; registry boundary of `BGS-TRACE-216`; verifier
`computations/verification/lineI/sym_v3/monomial_intertw.py`.

**Data.**  For each case `(m mod 24, a)` with `m ∈ {9, 15, 21, 27}` (`27 ≡ 3 mod 24`) and `a = ±2`, the finite automaton
factor on the 16 reachable states is a family `A_n e_s = e(−p_n(s)/8) e_{t_n(s)}` (`n mod 8`).  The tables `t_·`, `p_·` below
are the output of `gstates.finite` (`computations/verification/lineI/cert_v2/gstates.py`) as used by the verifier,
copied verbatim (generator: `evidence/executions/20261101/lean_batch3/scripts/gen_monomial_data.py`); `conj9` is the family
`(−1)^n conj A_n^{(9,2)}` (exponents `−p_n + 4n`), `neg9` the family `A_{−n}^{(9,2)}`.  A witness `(π, c)` is the monomial
matrix `X e_s = e(−c_s/8) e_{π(s)}`.

* `monomial_intertwines` (generic): if `π ∘ t_n = t′_n ∘ π` and `c(t_n s) + p_n(s) = c(s) + p′_n(π s)` (mod 8) then
  `X · A_n = A′_n · X` as complex 16 × 16 matrices;
* `X_mul_star` : for bijective `π`, `X Xᴴ = 1` (X is a monomial unitary);
* `case_m{15,21,27}p` / `matrix_m{15,21,27}p` : `X A_n^{(9,2)} = A_n^{(m,2)} X` (a = 2, all n; `m = 9, a = 2` is the base);
  `case_m{9,15,21,27}n` : `X ((−1)^n conj A_n^{(9,2)}) = A_n^{(m,−2)} X` (a = −2);
  `reflection` : `Y A_{−n}^{(9,2)} = A_n^{(9,2)} Y`; each witness permutation is bijective.  The finite checks are by `decide`.

**Partial coverage:** the derivation of the automaton tables from the (±2,8) G2 operators (that the factor depends on `m`
only through `(1+√2)^m mod 8` and the twist, and the 8-case reduction for `m ≡ 3 mod 6`) is **not** formalized — the tables are
imported data; the consequences for the infinite-dimensional lifted operators `L^{(m,±2)}_β` (unitary/antiunitary
conjugacy, invariance of spectra, resolvent and trace norms), the referee Galerkin check and the direct certificate at
`m = 15, a = −2` are **not** formalized.  All proofs are kernel-checked.
-/

namespace Bgs.LineIMonomial

open Matrix ComplexConjugate

/-- `ω(k) = e(k/8)`. -/
noncomputable abbrev ω : AddChar (ZMod 8) ℂ := ZMod.stdAddChar

/-- The monomial matrix `M e_s = e(−p(s)/8) e_{t(s)}`. -/
noncomputable def mono (t : Fin 16 → Fin 16) (p : Fin 16 → ZMod 8) : Matrix (Fin 16) (Fin 16) ℂ :=
  fun i j => if i = t j then ω (-p j) else 0

/-- The intertwining condition checked by the verifier. -/
def Intertw (t t' : Fin 16 → Fin 16) (p p' : Fin 16 → ZMod 8) (π : Fin 16 → Fin 16) (c : Fin 16 → ZMod 8) : Prop :=
  ∀ s, π (t s) = t' (π s) ∧ c (t s) + p s = c s + p' (π s)

instance (t t' p p' π c) : Decidable (Intertw t t' p p' π c) := by unfold Intertw; infer_instance

theorem monomial_intertwines (t t' : Fin 16 → Fin 16) (p p' : Fin 16 → ZMod 8) (π : Fin 16 → Fin 16)
    (c : Fin 16 → ZMod 8) (h : Intertw t t' p p' π c) :
    mono π c * mono t p = mono t' p' * mono π c := by
  ext i j
  simp only [mono, mul_apply]
  rw [Finset.sum_eq_single (t j), Finset.sum_eq_single (π j)]
  · obtain ⟨h1, h2⟩ := h j
    simp only [if_true, h1]
    split_ifs with hi
    · rw [← AddChar.map_add_eq_mul, ← AddChar.map_add_eq_mul]; congr 1
      linear_combination (-1 : ZMod 8) * h2
    · simp
  · intro b _ hb; simp [hb]
  · intro h'; exact absurd (Finset.mem_univ _) h'
  · intro b _ hb; simp [hb]
  · intro h'; exact absurd (Finset.mem_univ _) h'

theorem X_mul_star (π : Fin 16 → Fin 16) (hπ : Function.Bijective π) (c : Fin 16 → ZMod 8) :
    mono π c * (mono π c)ᴴ = 1 := by
  ext i j
  simp only [mono, mul_apply, conjTranspose_apply, one_apply]
  obtain ⟨k, rfl⟩ := hπ.2 i
  rw [Finset.sum_eq_single k]
  · by_cases hkj : π k = j
    · subst hkj
      simp only [if_true]
      rw [show star (ω (-c k)) = (starRingEnd ℂ) (ω (-c k)) from rfl, ← AddChar.map_neg_eq_conj,
        ← AddChar.map_add_eq_mul, add_neg_cancel, AddChar.map_zero_eq_one]
    · simp only [if_true, hkj, if_false]
      split_ifs with h1
      · exact absurd (h1.symm) hkj
      · simp
  · intro b _ hb
    have : π k ≠ π b := fun h => hb (hπ.1 h).symm
    simp [this]
  · intro h'; exact absurd (Finset.mem_univ _) h'

/-- family `m9p`: targets `t n s`. -/
def t_m9p : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![2, 10, 12, 4, 6, 14, 1, 9, 3, 11, 13, 5, 7, 15, 0, 8], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![6, 14, 1, 9, 11, 3, 5, 13, 7, 15, 0, 8, 10, 2, 4, 12], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![11, 3, 5, 13, 15, 7, 8, 0, 10, 2, 4, 12, 14, 6, 9, 1], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![15, 7, 8, 0, 2, 10, 12, 4, 14, 6, 9, 1, 3, 11, 13, 5]]

/-- family `m9p`: phase exponents `p n s` (mod 8). -/
def p_m9p : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1]]

/-- family `m9n`: targets `t n s`. -/
def t_m9n : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![2, 10, 12, 4, 6, 14, 1, 9, 3, 11, 13, 5, 7, 15, 0, 8], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![6, 14, 1, 9, 11, 3, 5, 13, 7, 15, 0, 8, 10, 2, 4, 12], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![11, 3, 5, 13, 15, 7, 8, 0, 10, 2, 4, 12, 14, 6, 9, 1], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![15, 7, 8, 0, 2, 10, 12, 4, 14, 6, 9, 1, 3, 11, 13, 5]]

/-- family `m9n`: phase exponents `p n s` (mod 8). -/
def p_m9n : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7]]

/-- family `m15p`: targets `t n s`. -/
def t_m15p : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![10, 2, 4, 12, 14, 6, 9, 1, 11, 3, 5, 13, 15, 7, 8, 0], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![14, 6, 9, 1, 3, 11, 13, 5, 15, 7, 8, 0, 2, 10, 12, 4], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![3, 11, 13, 5, 7, 15, 0, 8, 2, 10, 12, 4, 6, 14, 1, 9], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![7, 15, 0, 8, 10, 2, 4, 12, 6, 14, 1, 9, 11, 3, 5, 13]]

/-- family `m15p`: phase exponents `p n s` (mod 8). -/
def p_m15p : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7]]

/-- family `m15n`: targets `t n s`. -/
def t_m15n : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![10, 2, 4, 12, 14, 6, 9, 1, 11, 3, 5, 13, 15, 7, 8, 0], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![14, 6, 9, 1, 3, 11, 13, 5, 15, 7, 8, 0, 2, 10, 12, 4], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![3, 11, 13, 5, 7, 15, 0, 8, 2, 10, 12, 4, 6, 14, 1, 9], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![7, 15, 0, 8, 10, 2, 4, 12, 6, 14, 1, 9, 11, 3, 5, 13]]

/-- family `m15n`: phase exponents `p n s` (mod 8). -/
def p_m15n : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1]]

/-- family `m21p`: targets `t n s`. -/
def t_m21p : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![11, 3, 5, 13, 15, 7, 8, 0, 10, 2, 4, 12, 14, 6, 9, 1], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![15, 7, 8, 0, 2, 10, 12, 4, 14, 6, 9, 1, 3, 11, 13, 5], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![2, 10, 12, 4, 6, 14, 1, 9, 3, 11, 13, 5, 7, 15, 0, 8], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![6, 14, 1, 9, 11, 3, 5, 13, 7, 15, 0, 8, 10, 2, 4, 12]]

/-- family `m21p`: phase exponents `p n s` (mod 8). -/
def p_m21p : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5]]

/-- family `m21n`: targets `t n s`. -/
def t_m21n : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![11, 3, 5, 13, 15, 7, 8, 0, 10, 2, 4, 12, 14, 6, 9, 1], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![15, 7, 8, 0, 2, 10, 12, 4, 14, 6, 9, 1, 3, 11, 13, 5], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![2, 10, 12, 4, 6, 14, 1, 9, 3, 11, 13, 5, 7, 15, 0, 8], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![6, 14, 1, 9, 11, 3, 5, 13, 7, 15, 0, 8, 10, 2, 4, 12]]

/-- family `m21n`: phase exponents `p n s` (mod 8). -/
def p_m21n : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3]]

/-- family `m27p`: targets `t n s`. -/
def t_m27p : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![3, 11, 13, 5, 7, 15, 0, 8, 2, 10, 12, 4, 6, 14, 1, 9], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![7, 15, 0, 8, 10, 2, 4, 12, 6, 14, 1, 9, 11, 3, 5, 13], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![10, 2, 4, 12, 14, 6, 9, 1, 11, 3, 5, 13, 15, 7, 8, 0], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![14, 6, 9, 1, 3, 11, 13, 5, 15, 7, 8, 0, 2, 10, 12, 4]]

/-- family `m27p`: phase exponents `p n s` (mod 8). -/
def p_m27p : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3]]

/-- family `m27n`: targets `t n s`. -/
def t_m27n : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![3, 11, 13, 5, 7, 15, 0, 8, 2, 10, 12, 4, 6, 14, 1, 9], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![7, 15, 0, 8, 10, 2, 4, 12, 6, 14, 1, 9, 11, 3, 5, 13], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![10, 2, 4, 12, 14, 6, 9, 1, 11, 3, 5, 13, 15, 7, 8, 0], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![14, 6, 9, 1, 3, 11, 13, 5, 15, 7, 8, 0, 2, 10, 12, 4]]

/-- family `m27n`: phase exponents `p n s` (mod 8). -/
def p_m27n : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5]]

/-- family `conj9`: targets `t n s`. -/
def t_conj9 : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![2, 10, 12, 4, 6, 14, 1, 9, 3, 11, 13, 5, 7, 15, 0, 8], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![6, 14, 1, 9, 11, 3, 5, 13, 7, 15, 0, 8, 10, 2, 4, 12], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![11, 3, 5, 13, 15, 7, 8, 0, 10, 2, 4, 12, 14, 6, 9, 1], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![15, 7, 8, 0, 2, 10, 12, 4, 14, 6, 9, 1, 3, 11, 13, 5]]

/-- family `conj9`: phase exponents `p n s` (mod 8). -/
def p_conj9 : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![1, 1, 3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5, 3, 3]]

/-- family `neg9`: targets `t n s`. -/
def t_neg9 : Fin 8 → Fin 16 → Fin 16 :=
  ![![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7], ![15, 7, 8, 0, 2, 10, 12, 4, 14, 6, 9, 1, 3, 11, 13, 5], ![13, 5, 7, 15, 0, 8, 10, 2, 12, 4, 6, 14, 1, 9, 11, 3], ![11, 3, 5, 13, 15, 7, 8, 0, 10, 2, 4, 12, 14, 6, 9, 1], ![9, 1, 3, 11, 13, 5, 7, 15, 8, 0, 2, 10, 12, 4, 6, 14], ![6, 14, 1, 9, 11, 3, 5, 13, 7, 15, 0, 8, 10, 2, 4, 12], ![4, 12, 14, 6, 9, 1, 3, 11, 5, 13, 15, 7, 8, 0, 2, 10], ![2, 10, 12, 4, 6, 14, 1, 9, 3, 11, 13, 5, 7, 15, 0, 8]]

/-- family `neg9`: phase exponents `p n s` (mod 8). -/
def p_neg9 : Fin 8 → Fin 16 → ZMod 8 :=
  ![![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![3, 3, 5, 5, 7, 7, 1, 1, 3, 3, 5, 5, 7, 7, 1, 1], ![4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0], ![3, 3, 1, 1, 7, 7, 5, 5, 3, 3, 1, 1, 7, 7, 5, 5]]

def pi_m9n : Fin 16 → Fin 16 := ![0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def c_m9n : Fin 16 → ZMod 8 := ![0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4]

def pi_m15p : Fin 16 → Fin 16 := ![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7]
def c_m15p : Fin 16 → ZMod 8 := ![0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2]

def pi_m15n : Fin 16 → Fin 16 := ![0, 8, 10, 2, 4, 12, 14, 6, 1, 9, 11, 3, 5, 13, 15, 7]
def c_m15n : Fin 16 → ZMod 8 := ![0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2]

def pi_m21p : Fin 16 → Fin 16 := ![0, 1, 11, 10, 4, 5, 15, 14, 8, 9, 3, 2, 12, 13, 7, 6]
def c_m21p : Fin 16 → ZMod 8 := ![0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4]

def pi_m21n : Fin 16 → Fin 16 := ![0, 1, 11, 10, 4, 5, 15, 14, 8, 9, 3, 2, 12, 13, 7, 6]
def c_m21n : Fin 16 → ZMod 8 := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def pi_m27p : Fin 16 → Fin 16 := ![0, 8, 3, 11, 4, 12, 7, 15, 1, 9, 2, 10, 5, 13, 6, 14]
def c_m27p : Fin 16 → ZMod 8 := ![0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 6, 6]

def pi_m27n : Fin 16 → Fin 16 := ![0, 8, 3, 11, 4, 12, 7, 15, 1, 9, 2, 10, 5, 13, 6, 14]
def c_m27n : Fin 16 → ZMod 8 := ![0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 6, 6]

def pi_refl : Fin 16 → Fin 16 := ![0, 1, 15, 14, 13, 12, 11, 10, 8, 9, 7, 6, 5, 4, 3, 2]
def c_refl : Fin 16 → ZMod 8 := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

theorem case_m15p : ∀ n : Fin 8, Intertw (t_m9p n) (t_m15p n) (p_m9p n) (p_m15p n) pi_m15p c_m15p := by decide
theorem case_m21p : ∀ n : Fin 8, Intertw (t_m9p n) (t_m21p n) (p_m9p n) (p_m21p n) pi_m21p c_m21p := by decide
theorem case_m27p : ∀ n : Fin 8, Intertw (t_m9p n) (t_m27p n) (p_m9p n) (p_m27p n) pi_m27p c_m27p := by decide
theorem case_m9n : ∀ n : Fin 8, Intertw (t_conj9 n) (t_m9n n) (p_conj9 n) (p_m9n n) pi_m9n c_m9n := by decide
theorem case_m15n : ∀ n : Fin 8, Intertw (t_conj9 n) (t_m15n n) (p_conj9 n) (p_m15n n) pi_m15n c_m15n := by decide
theorem case_m21n : ∀ n : Fin 8, Intertw (t_conj9 n) (t_m21n n) (p_conj9 n) (p_m21n n) pi_m21n c_m21n := by decide
theorem case_m27n : ∀ n : Fin 8, Intertw (t_conj9 n) (t_m27n n) (p_conj9 n) (p_m27n n) pi_m27n c_m27n := by decide
theorem reflection : ∀ n : Fin 8, Intertw (t_neg9 n) (t_m9p n) (p_neg9 n) (p_m9p n) pi_refl c_refl := by decide

/-- The `conj9` family is `(−1)^n conj A_n^{(9,2)}`: same targets, exponents `−p_n + 4n` (mod 8). -/
theorem conj9_spec : ∀ n : Fin 8, ∀ s : Fin 16,
    t_conj9 n s = t_m9p n s ∧ p_conj9 n s = -p_m9p n s + 4 * (n.val : ZMod 8) := by decide

/-- The `neg9` family is `A_{−n}^{(9,2)}`. -/
theorem neg9_spec : ∀ n : Fin 8, ∀ s : Fin 16,
    t_neg9 n s = t_m9p (-n) s ∧ p_neg9 n s = p_m9p (-n) s := by decide

theorem pi_bijective : Function.Injective pi_m15p ∧ Function.Injective pi_m21p ∧ Function.Injective pi_m27p ∧
    Function.Injective pi_m9n ∧ Function.Injective pi_m15n ∧ Function.Injective pi_m21n ∧
    Function.Injective pi_m27n ∧ Function.Injective pi_refl := by decide

/-- Matrix form of every case: `X F_n = F′_n X` with `X` a monomial unitary (`X Xᴴ = 1`). -/
theorem matrix_m15p (n : Fin 8) :
    mono pi_m15p c_m15p * mono (t_m9p n) (p_m9p n) = mono (t_m15p n) (p_m15p n) * mono pi_m15p c_m15p :=
  monomial_intertwines _ _ _ _ _ _ (case_m15p n)

theorem unitary_m15p : mono pi_m15p c_m15p * (mono pi_m15p c_m15p)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.1) _

theorem matrix_m21p (n : Fin 8) :
    mono pi_m21p c_m21p * mono (t_m9p n) (p_m9p n) = mono (t_m21p n) (p_m21p n) * mono pi_m21p c_m21p :=
  monomial_intertwines _ _ _ _ _ _ (case_m21p n)

theorem unitary_m21p : mono pi_m21p c_m21p * (mono pi_m21p c_m21p)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.2.1) _

theorem matrix_m27p (n : Fin 8) :
    mono pi_m27p c_m27p * mono (t_m9p n) (p_m9p n) = mono (t_m27p n) (p_m27p n) * mono pi_m27p c_m27p :=
  monomial_intertwines _ _ _ _ _ _ (case_m27p n)

theorem unitary_m27p : mono pi_m27p c_m27p * (mono pi_m27p c_m27p)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.2.2.1) _

theorem matrix_m9n (n : Fin 8) :
    mono pi_m9n c_m9n * mono (t_conj9 n) (p_conj9 n) = mono (t_m9n n) (p_m9n n) * mono pi_m9n c_m9n :=
  monomial_intertwines _ _ _ _ _ _ (case_m9n n)

theorem unitary_m9n : mono pi_m9n c_m9n * (mono pi_m9n c_m9n)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.2.2.2.1) _

theorem matrix_m15n (n : Fin 8) :
    mono pi_m15n c_m15n * mono (t_conj9 n) (p_conj9 n) = mono (t_m15n n) (p_m15n n) * mono pi_m15n c_m15n :=
  monomial_intertwines _ _ _ _ _ _ (case_m15n n)

theorem unitary_m15n : mono pi_m15n c_m15n * (mono pi_m15n c_m15n)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.2.2.2.2.1) _

theorem matrix_m21n (n : Fin 8) :
    mono pi_m21n c_m21n * mono (t_conj9 n) (p_conj9 n) = mono (t_m21n n) (p_m21n n) * mono pi_m21n c_m21n :=
  monomial_intertwines _ _ _ _ _ _ (case_m21n n)

theorem unitary_m21n : mono pi_m21n c_m21n * (mono pi_m21n c_m21n)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.2.2.2.2.2.1) _

theorem matrix_m27n (n : Fin 8) :
    mono pi_m27n c_m27n * mono (t_conj9 n) (p_conj9 n) = mono (t_m27n n) (p_m27n n) * mono pi_m27n c_m27n :=
  monomial_intertwines _ _ _ _ _ _ (case_m27n n)

theorem unitary_m27n : mono pi_m27n c_m27n * (mono pi_m27n c_m27n)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.2.2.2.2.2.2.1) _

theorem matrix_refl (n : Fin 8) :
    mono pi_refl c_refl * mono (t_neg9 n) (p_neg9 n) = mono (t_m9p n) (p_m9p n) * mono pi_refl c_refl :=
  monomial_intertwines _ _ _ _ _ _ (reflection n)

theorem unitary_refl : mono pi_refl c_refl * (mono pi_refl c_refl)ᴴ = 1 :=
  X_mul_star _ (Finite.injective_iff_bijective.mp pi_bijective.2.2.2.2.2.2.2) _

end Bgs.LineIMonomial
