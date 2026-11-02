# Wave 42, task 4 — SCL in the 3-part: proved bound n_q ≤ v_3(m)

## Verdict

**SCL (n_q ≤ 10) is PROVED for the 3-part** at every m with v_3(m) ≤ 10,
i.e. every m not divisible by 4·3¹¹ = 708588. The bound is
n_q ≤ v_3(m), proved from the lift tower plus a finite mod-3
computation giving N(b) = 1. The first possible SCL failure in
the 3-part is at m = 708588 (full level 12, predicted n = 11 by
the exact formula, verified at levels ≤ 6); a direct census
there is infeasible (mod 3¹², ~2.8×10¹¹ C-values).

## 1. Setup (waves 35–39)

p = 3, α = 3+2√2, R = ℤ[√2]. d = ord_3(α) = 4,
e = v_3(α⁴−1) = 1, base level b = e+1 = 2. Component
q = 3^{2f} of D_m. 3-adic LTE (proved, wave 27):
v_3(D_m) = 0 unless 4 | m, else 2v_3(m)+2 — so the 3-part
exists only for 4 | m, at full level f = v_3(m)+1.
Lift tower (odd p, waves 36/37/39): genuine fibers are full
preimages of base fibers (LT1/LT2, Full Blindness), degenerate
fibers are exact p× lifts (LT3); below base is level 1 only
(e = 1), proved by wave 32. Hence for f ≥ b:

    N(f) ≤ (f−e)·N(b) = (f−1)·N(b),

counting split fibers (on-support counts are a subset, so the
bound covers them; the support-transfer caveat of wave 39 §5
affects only the lower bound / exactness in §4, not this
upper bound).

## 2. N(b) = 1 for p = 3, proved by finite mod-3 computation

α mod 3 = 2√2, ord 4: (2√2)² = 2, (2√2)⁴ = 1 mod 3.
α⁴−1 = 576+408√2, v_3 = min(v_3(576), v_3(408)) = min(2,1) = 1,
u = (α⁴−1)/3 mod 3 = √2. Level-b analysis (wave 35 §f′=2):
split fibers at level b ⟷ Γ-orbits mod 3 with Z = ∅, where
Z = {j₀ : Tr(Cα^{j₀}u) = 0 mod 3}. Since
Tr((x+y√2)·√2) = 4y ≡ y (mod 3), B_{j₀} is the y-coefficient
of Cα^{j₀}: for C = a+b√2 the four values are b, 2a, 2b, a,
so Z = ∅ ⟺ a ≠ 0 and b ≠ 0 mod 3. The four such classes
{(1,1),(1,2),(2,1),(2,2)} form a single Γ-orbit (shift by α
plus conjugation, which stays inside the orbit). Hence
exactly one Γ-orbit mod 3 has Z = ∅, i.e. **N(b) = 1**.
Verified exactly by `wave42_SCL_check.py` Part A
(3 Γ-orbits mod 3 total, 1 with Z = ∅).

## 3. Theorem: n_q ≤ v_3(m) for the 3-part

From §1–§2, at level f: n_q ≤ (f−1)·1 = f−1. At the full
level f = v_3(m)+1 (4 | m):

    n_q ≤ v_3(m).

In particular n_q ≤ 10 whenever v_3(m) ≤ 10. The bound is
new as a proof (previously the 3-part counts were census
values only, at m ≤ 108).

## 4. Exact formula N(f) = f−1, verified at levels ≤ 6

Exact trace-model censuses (`wave35_tm_census.tm_census`,
all on-support, mixed = 0 everywhere):

| m | f | split fibers | sizes | orbits |
|---|---|---|---|---|
| 12 | 2 | 1 | 36 | 3 |
| 36 | 3 | 2 | 324, 36 | 9, 3 |
| 108 | 4 | 3 | 2916, 324, 36 | 27, 9, 3 |
| 324 | 5 | 4 (NEW) | 26244, 2916, 324, 36 | 81, 27, 9, 3 |
| 708588 | 6 (truncated) | 5 (NEW) | 236196, 26244, 2916, 324, 36 | 243, 81, 27, 9, 3 |

Pattern: one fiber per level-step, main size 4·9^{f−1}
(= m²/4 at full level), sizes ÷9 down the tower, orbits
×3 up it; lifts preserve size and orbit count (LT3).
So N(f) = f−1 exactly at every censused level. In general
the exact formula follows from the tower recursion
N(f) = N(f−1)+1 modulo exactly one stated lemma:

**Support-transfer lemma (open):** p× lifts and full
preimages of on-support fibers are on-support.
(Verified at all censused levels: mixed = 0 throughout.)

## 5. SCL status for the 3-part, and what remains

- Proved: n_q ≤ 10 for the 3-part at every m with
  v_3(m) ≤ 10.
- First open case: m = 708588 (and multiples with
  v_3(m) = 11), full level 12, predicted n = 11 by §4.
  Direct census infeasible: mod 3¹² = 531441,
  ~2.8×10¹¹ C-values. A proof of the §4 support-transfer
  lemma would confirm n = 11 there, giving a new exact
  SCL counterexample (n_q = 11 > 10) in the 3-part.
- Correction to an intermediate claim made while running
  this task: the m = 708588 census at f = 6 is a
  truncated-level check (5 = 6−1, consistent with the
  formula), NOT the full-component count; the full level
  is 12, not 6.
- Scope: p = 3 only. Other odd p (tower bound needs
  N(b), known only censused except p = 3 here) and the
  2-part are untouched.

Files: this note; `wave42_SCL_check.py` (Part A exact
mod-3 computation + Part B censuses at m = 12, 36, 108, 324).
No Lean built, repository untouched.
