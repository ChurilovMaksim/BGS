# Wave 34, task 5 — lemma F2: FALSE as stated (single orbit), bound repaired

## Verdict

**F2 as stated in wave 32 §7 (every fiber at qt = p^{2f} is a single
Γ-orbit) is FALSE.** Exact counterexample below at m = 816,
qt = 17⁴. What survives is a repaired bound: for f = 2,
|f_qt| ≤ 2m·p², which still saves mechanism B of the wave-33
recount; for f ≥ 3 the polynomial bound max|f_qt| ≤ m^b is now
OPEN (F2-poly), and mechanism B is conditional on it.
Repository untouched; no Lean built.

## 1. Setup (generalizing wave 32 §1–2)

Let qt = p^{2f}, v_p(D_m) = 2f, p odd. The eigenvalue argument
(v_p(α^m − 1) = v_p(ᾱ^m − 1) = f, via v_p(α^m − ᾱ^m) = f)
gives SNF (p^f, p^f) for M^m − I, so the kernel mod p^{2f} is
p^f times the trace model mod p^f: rows ↔ C ∈ R_{p^f},
w_j = Tr(Cα^j), Γ acting by C ↦ Cα^j and C ↦ C̄α^j.
Let d = ord_p(α), d_f = ord_{p^f}(α) = d·p^{f−e} with
e = v_p(α^d − 1) ≥ 1 (assume e < f).

## 2. Counterexample (exact, script-verified)

m = 816, p = 17, qt = 17⁴, v_17(D_816) = 4 (direct recurrence).
Mod 289 the ring splits: √2 ≡ 244, α ↦ (α₁, α₂) = (202, 93),
α₁α₂ = 1, ord_{289}(α₁) = 136, α₁⁸ = 1 + 17u₁ with u₁ = 1 a unit,
u₂ = 16, u₁ + u₂ ≡ 0 (mod 17). So Tr(Cα^j) = c₁α₁^j + c₂α₂^j.

Take C₀ = (1, 0) and C′ = (1, 17) in split coordinates. Then:
- the sorted multisets {Tr(C₀α^j) : j < 816} and
  {Tr(C′α^j) : j < 816} mod 289 are EQUAL (script);
- C′ ∉ Γ·C₀: the orbit of C₀ is {(α₁^j, 0)} ∪ {(0, α₂^j)}
  (272 elements), every element having a zero component, while
  C′ has none. Hence one fiber contains ≥ 2 Γ-orbits: F2 false.

## 3. Mechanism: lift lines (proved for f = 2, e = 1)

Write j = j₀ + 8t (d = 8). Since α₁⁸ = 1 + 17u₁,
α₁^j = α₁^{j₀}(1 + 17u₁t) mod 289, and with u₂ = −u₁,
v_j = A_{j₀} + 17t·B_{j₀} mod 289, where
A_{j₀} = c₁α₁^{j₀} + c₂α₂^{j₀} and
B_{j₀} = u₁(c₁α₁^{j₀} − c₂α₂^{j₀}) mod 17.
If B_{j₀} ≠ 0 for all j₀, each j₀-line is the FULL lift fiber
above its mod-17 residue (t·B_{j₀} covers Z/17), so the multiset
depends only on C mod 17: all 17² lifts of a class share it,
while Γ-line shifts α^{8k} account for only 17 of them.
Verified: all 289 lifts of class (1, 0) share the multiset, and
likewise for C = (1, 2) (D_{j₀} ≠ 0 for all j₀).

Top-digit sweep (general f, e < f, D_{j₀} ≠ 0): writing
t = t′ + p^{s−1}t_{s−1}, the top digit of v enters with
coefficient Tr(Cα^{j₀}w) ≡ u₁D_{j₀} mod p ≠ 0, so the multiset
mod p^f is blind to the top digit of C. Lower-digit visibility
for f ≥ 3 is unproved.

## 4. Exact fiber size at the test case

The mod-17 Γ-orbit of (1, 0) has 16 classes; each contributes
289 lifts, all sharing the multiset (script). Hence the fiber
has exactly 4624 rows = 17 Γ-orbits × 272. So |f| = 4624 > 272
(one orbit) but ≤ 816²: the b = 2 polynomial bound survives
HERE, and the m = 48 counting is unaffected (both twin qt there
are squares).

## 5. Consequence for mechanism B (wave-33 recount §4)

Trivial lift counting gives |f_qt| ≤ 2m·p^{2(f−1)} for any f.
For f = 2 this is 2m·p² = 2m√qt, and mechanism B survives:
ΣΔ_F(B) ≤ 512·m^{2c+8}·(Σ qt)², so
ΣΔ_F(B)/D_m ≤ 512·m^{2c+8}·D_m·ε² → 0 with H12-poly
ε = 18u³/α^{8u}, since D_m·ε² ≈ 324u⁶/α^{4u} → 0.
For f ≥ 3 the trivial bound gives instead
ΣΔ_F(B)/D_m ≲ m^{2c+8}·D_m²·ε³ ≈ 5832u⁹ ↛ 0: it FAILS.
So mechanism B is now conditional on F2-poly for f ≥ 3
(e.g. |f_qt| ≤ 2m·p², i.e. one-digit invisibility only), which
is open. The inert case follows the same argument shape
(condition Tr(Cα^{j₀}u) ≠ 0) but is not verified here.

Script: wave34_F2_check.py (ALL CHECKS PASS).
