# Wave 14, task 2 — Lemma PC for (m, p₁, p₂) = (8, 3, 17): PROVED

## Statement

Let a, b be recurrence sequences mod 3, mod 17 of length 8
(y_{j+1} = 6y_j − y_{j−1}), d₁, d₂ ∈ D₈, d(j) = εj + k (mod 8).
Classes O_r = {r, r+4}, r ∈ ℤ/4, D₄ acting by r ↦ εr + k (mod 4).
d maps O_r bijectively onto O_{π_d(r)}, π_d(r) = εr + k (mod 4).
Πᵢ = {π ∈ D₄ : per-class multisets of dᵢ(seq) at r equal those of
seq at π(r) for all r}; π_{dᵢ} ∈ Πᵢ always. Hypothesis (∗):
{(a_{d₁(j)}, b_{d₂(j)})} = {(a_j, b_j)} as multisets of pairs.
**Theorem.** Π₁ ∩ Π₂ ≠ ∅. (Non-degenerate: unlike the wave-13
(6,5,7) case, no Πᵢ is forced full here.)

## 1. Periods, v, and C

Work in R = ℤ[√2], α = 3 + 2√2, Tr(x) = x + x̄, y_j = Tr(Aα^j).
Mod 3: α ≡ 2√2, α² = 2, α⁴ = 1. Hence a_{j+4} = a_j; write
v_r = a_r, r = 0..3. With A₁ = (x, y) mod 3, direct computation gives
v = (2x, 2y, x, y) ≡ (−x, −y, x, y) (mod 3), so v_{r+2} = −v_r.
Class-r multiset of a is {v_r, v_r}.
Mod 17: α² = 17 + 12√2 ≡ 12√2, α⁴ = (12√2)² = 288 ≡ −1. Hence
b_{j+4} = −b_j; write w_r = b_r. Class-r multiset of b is
C_r = {w_r, −w_r}, a symmetric pair.

## 2. Reduction of (∗) to fibre conditions

Original pairs, grouped by class r: (v_r, w_r), (v_r, −w_r).
Mixed pairs, grouped by class r: a_{d₁(j)} = v_{π₁(r)} for j ∈ O_r
(a depends only on j mod 4, d₁(j) ≡ π₁(r) mod 4); as j runs over
O_r, d₂(j) runs over O_{π₂(r)}, so the two mixed pairs are exactly
(v_{π₁(r)}, w_{π₂(r)}), (v_{π₁(r)}, −w_{π₂(r)}).
Grouping all pairs by first coordinate p and reindexing s = π₂(r),
with δ = π₁ ∘ π₂⁻¹ ∈ D₄, (∗) becomes (P): for every p ∈ 𝔽₃,
⊔_{s : v_{δ(s)} = p} C_s = ⊔_{s : v_s = p} C_s as multisets of values.
Put ε = δ⁻¹. For each v-fibre F, (P) says
⊔_{f ∈ F} C_{ε(f)} = ⊔_{f ∈ F} C_f (value multisets).

## 3. Recovery lemma: union determines the item multiset

Each C is a symmetric pair {w, −w}. A multiset U that is a union of
symmetric pairs determines the multiset of pairs: for y ≠ 0, the
number of items equal to {y, −y} is mult_U(y) (= mult_U(−y)); for
y = 0 it is mult_U(0)/2. Hence (P) implies the item-level condition
(I): for each v-fibre F, {C_{ε(f)} : f ∈ F} = {C_f : f ∈ F}.

## 4. Fibres of v, and the reflection ρ

If A₁ = 0, v ≡ 0 and Π₁ = D₄, so π₂ ∈ Π₁ ∩ Π₂. Assume A₁ ≠ 0.
From v = (−x, −y, x, y) mod 3 (note 𝔽₃ˣ has two elements, so any
nonzero x, y satisfy x = ±y), the fibres are:
(A) one pair + two singletons: x = 0: F = {0,2}, singletons 1, 3,
    ρ = (−1, 2); y = 0: F = {1,3}, singletons 0, 2, ρ = (−1, 0);
(B) two pairs: x = y: F = {0,1}, G = {2,3}, ρ = (−1, 1);
    x = −y: F = {0,3}, G = {1,2}, ρ = (−1, 3).
In each case ρ ∈ Stab(v) (direct check from the v-formula), ρ swaps
within each pair fibre and fixes the singletons. Write E = C ∘ ε.
Goal: E = C or E = C ∘ ρ (this is exactly ε ∈ Stab(C) or
ερ ∈ Stab(C), i.e. δ ∈ Stab(C) or ρδ ∈ Stab(C)).

## 5. Case (A): one pair fibre

Singletons give C_{ε(s)} = C_s pointwise. On F = {f₁, f₂}, (I) gives
either (a) C_{ε(f₁)} = C_{f₁}, C_{ε(f₂)} = C_{f₂}, or (b) the swapped
values (or both, if C_{f₁} = C_{f₂}). In (a), E = C everywhere.
In (b), E = C ∘ ρ: on F, (C ∘ ρ)_{f₁} = C_{f₂} = C_{ε(f₁)} and
similarly for f₂; on singletons ρ fixes and ε already matches.

## 6. Case (B): two pair fibres

It suffices to do x = y (F = {0,1}, G = {2,3}, ρ = (−1,1)); x = −y
follows by the mirror relabelling r ↦ −r, which sends its fibres
and ρ = (−1,3) to these. Let E = C ∘ ε.
- ε ∈ {id, ρ}: ε preserves each fibre, giving E = C, resp. C ∘ ρ.
- ε swaps the fibres (shift by 2, or −r + 3): the two fibre
  conditions in (I) coincide into one multiset equation, whose two
  resolutions are exactly E = C and E = C ∘ ρ (e.g. shift by 2:
  E = (C₂, C₃, C₀, C₁); (C₂, C₃) ~ (C₀, C₁) resolves as
  (C₂, C₃) = (C₀, C₁), giving E = C, or (C₁, C₀), giving E = C ∘ ρ).
- ε overlaps the fibres (shift by 1, shift by 3, −r, −r + 2): each
  fibre condition shares one C-value, forcing a single equation,
  from which E = C or E = C ∘ ρ follows by inspection:
  shift by 1: C₀ = C₂, E = C ∘ ρ; shift by 3: C₁ = C₃, E = C ∘ ρ;
  −r: C₁ = C₃, E = C; −r + 2: C₀ = C₂, E = C.
  (E.g. shift by 1: {C₁, C₂} = {C₀, C₁} forces C₂ = C₀ since C₁ is
  common, and {C₃, C₀} = {C₂, C₃} forces the same; then
  E = (C₁, C₂, C₃, C₀) = (C₁, C₀, C₃, C₂) = C ∘ ρ.)
Hence in all cases E = C or E = C ∘ ρ.

## 7. Assembly

From §5–§6, δ ∈ Stab(C) or ρδ ∈ Stab(C); with ρ ∈ Stab(v) this is
δ ∈ Stab(v)·Stab(C): write δ = σ_v ∘ σ_c, σ_v ∈ Stab(v),
σ_c ∈ Stab(C). Set π = σ_c ∘ π₂ ∈ D₄. Then
C_{π(r)} = C_{σ_c(π₂(r))} = C_{π₂(r)}, so π ∈ Π₂; and
v_{π(r)} = v_{σ_c(π₂(r))} = v_{δ(π₂(r))} = v_{π₁(r)} (using
σ_v ∈ Stab(v) and δ ∘ π₂ = π₁), so π ∈ Π₁. Thus Π₁ ∩ Π₂ ≠ ∅. ∎

## 8. Numerical confirmation and scope

Fresh implementation (no wave-12 code reused):
[wave14_PC_m8.py](wave14_PC_m8.py)
enumerates all 9 × 289 pairs (a, b) and all 16 × 16 pairs (d₁, d₂):
**272,640 preserved cases (reproducing wave 12 exactly), 0 bad**;
δ ∈ Stab(v)·Stab(C) in every preserved case. Breakdown by A₁-type:
zero 73,984; each of x = 0, y = 0, x = y, x = −y: 49,664.
This closes Lemma PC only for (8, 3, 17). General PC is still open:
the proof uses t = 4, α⁴ = ±1, and v-fibres of size ≤ 2 (forced by
𝔽₃); larger t or other primes need new ideas. Repository untouched;
no Lean built; nothing here is a Lean theorem.
