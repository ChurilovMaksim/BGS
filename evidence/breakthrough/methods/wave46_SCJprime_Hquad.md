# Wave 46, task 8 — H-quad and H-diff DERIVED from definitions

## Verdict

H-quad and H-diff are no longer fitted: both follow from the definitions
of Q, P, W plus the 3-adic LTE (v₃(D_m) = 6) and one norm computation.
Exact verification: the derived closed form for F matches the exact
T-matrix on all 531,441 entries at m = 36, 72, 144, 180, 252 (0
mismatches each); the expansion reproduces both wave-45 fits exactly
(m = 180: (19,16,0,21); m = 252: (17,20,0,6,6,23)); H-diff holds for
all 4 top-digit pairs per m. The 36 ∤ m case is vacuous, not open:
on the 9t line 36 ∤ m ⟺ 4 ∤ m ⟹ v₃(D_m) = 0, so the kernel at 729
is trivial (verified at m = 45, 90). Hence wave-45's F3 gap argument
now stands on LTE3 alone. No Lean built; repository untouched.

## 1. Definitions (wave-45 scripts)

Kernel points K_i ∈ (Z/729)^m are Tr(C_i α^i), α = 3+2√2, C_i ∈ 27R/729R,
R = Z[√2]. H is cyclic, (Hv)_k = 6v_k − v_{k−1} − v_{k+1}; W_i = (HK_i)/729
(integer, since HK_i ≡ 0 mod 729). Qv[i] = dqm·⟨W_i,K_i⟩,
P[i,j] = dqm·⟨W_i,K_j⟩, dqm = (D_m/729) mod 729 =: u,
T[i,j] = u⁻²(2Qv[i] − P[i,j]) = u⁻¹(2⟨W_i,K_i⟩ − ⟨W_i,K_j⟩) mod 729,
ci = u⁻¹ mod 729, F[i,j] = ((ci·T[i,j] mod 729)/27) mod 27.

## 2. Boundary reduction (the key step)

Write K_i = t^{(i)} − 729·e^{(i)} with t^{(i)}_k = Tr(C_i α^k) over Z.
Ht^{(i)} vanishes except at k = 0, m−1 (cyclic wraparound):
(Ht)_0 = t_{−1} − t_{m−1}, (Ht)_{m−1} = t_m − t_0, both ≡ 0 mod 729
by kernel closure. Since H is symmetric,
⟨W_i,K_j⟩ = ⟨(Ht^{(i)})/729, K_j⟩ − 729⟨e^{(i)},W_j⟩
          ≡ A_i·K_j[0] + B_i·K_j[m−1] (mod 729),
A_i = (t_{−1} − t_{m−1})/729, B_i = (t_m − t_0)/729.
K_j entries are ≡ 0 mod 27 (27 | C_j), so 27 | ⟨W_i,K_j⟩:
this alone gives 27 | ci·T[i,j], i.e. F is well defined.

## 3. Closed form

Write α^m = 1 + 27ν (27 | α^m − 1 by §5) and C_i = 27C'_i. Then
A_i = −Tr(C'_i·ᾱν), B_i = Tr(C'_i·ν). With linear forms (mod 27)
M(C') = Tr(C'ᾱν), N(C') = Tr(C'ν), L_0(C') = Tr(C') = 2x̄,
L_1(C') = Tr(C'α^{m−1}) = τ_0x̄ + τ_1ȳ:
  F[i,j] = u⁻²·[−M_i(2L_0(C'_i) − L_0(C'_j))
                 + N_i(2L_1(C'_i) − L_1(C'_j))] mod 27.
Expansion in dx = x̄_i − x̄_j, dy = ȳ_i − ȳ_j:
  F = a·dx² + b·dy² + c·dx·dy + d_j·dx + e_j·dy + f_j,
  a = (−4μ_0 + 2ν_0τ_0)u⁻², b = 2ν_1τ_1u⁻²,
  c = (−4μ_1 + 2ν_0τ_1 + 2ν_1τ_0)u⁻²,
  d_j = −6μ_0x̄_j·u⁻², e_j = 3ν_1τ_1ȳ_j·u⁻²,
  f_j = u⁻²(−M_j·2x̄_j + N_j(τ_0x̄_j + τ_1ȳ_j)),
where μ_0 = Tr(ᾱν), μ_1 = Tr(√2ᾱν), ν_0 = Tr(ν), ν_1 = Tr(√2ν).

## 4. Why the mod-3 conditions hold (valuations only)

α^m = A_m + B_m√2, D_m = 2(A_m − 1). LTE3 gives v₃(D_m) = 6, so
v₃(A_m − 1) = 6; the norm (A_m−1)(A_m+1) = 2B_m² with v₃(A_m+1) = 0
gives v₃(B_m) = 3. Hence ν_0 = D_m/27 ≡ 0 mod 27;
μ_0 = (6(A_m−1) − 8B_m)/27 has v₃ = 0 (terms of v₃ ≥ 7 and = 3);
ν_1 = 4B_m/27 has v₃ = 0; τ_0 = Tr(α^{m−1}) ≡ Tr(ᾱ) = 6 mod 27;
τ_1 ≡ Tr(√2ᾱ) = −8 mod 27; μ_1 = 3ν_1 − 4ν_0 ≡ 3ν_1 mod 27.
Consequences mod 27: c ≡ 0 (so B := b − c²/4a ≡ b),
a ≡ −4μ_0u⁻² ≢ 0 mod 3, b = 2ν_1τ_1u⁻² ≢ 0 mod 3,
e_j ≡ 0 mod 3, hence E = e_j − c·d/(2a) ≡ 0 mod 3.
These are exactly the inputs of wave-45 §3 (Gauss sum + 1+ω^p+ω^q ≠ 0).

## 5. H-diff derived

For a top-digit pair, C̄_{j′} = C̄_j − (0,9): K[0] is unchanged,
K[m−1] shifts by 27·Tr(−9√2·α^{m−1}) = −243τ_1. So
  T[i,j′] − T[i,j] ≡ u⁻¹·243·B_i·τ_1 ≡ 243·ε·ȳ_i (mod 729),
  ε = u⁻¹τ_1ν_1 mod 3 ∈ {+1, −1},
since B_i ≡ ν_1ȳ_i mod 3 (ν_0 ≡ 0 mod 27) and 243·3 ≡ 0 mod 729.
Verified: ε = −1 at m = 36, 144, 252; +1 at m = 72, 180; 0 bad rows
over all 4 top-digit pairs per m (not just the counted pair).

## 6. Corrections to wave-45

d is not universally shared: d_j = −6μ_0x̄_j·u⁻² depends on x̄_j
(shared on fiber-0 only because x̄_j = 14 there). f_j mod 3 varies
with m (5, 4, 14, 13, 23 at m = 36, 72, 144, 180, 252) and is not
used by the gap argument. Full coefficient table (fiber-0, k = 20):
m = 36: (26,2,0,6,6,5); 72: (10,7,0,21,21,4); 144: (8,11,0,6,6,14);
180: (19,16,0,21,21,13); 252: (17,20,0,6,6,23).

## 7. The 36 ∤ m case: vacuous

On the 9t line (v₃(m) = 2), 36 ∤ m ⟺ 4 ∤ m. By LTE3,
v₃(D_m) = 0 unless 4 | m, so 729 ∤ D_m and there is no 729-component:
kernel_points(m, 729) = {0} only, verified at m = 45 (v₂ = 0) and
m = 90 (v₂ = 1), both with v₃(D_m) = 0. F3 at 729 does not fail
there — it has no section to apply to.
Remark (unverified): for v₃(m) = e ≥ 2 with 4 | m, the same
computation carries over with (729, 27, 243) ↦ (3^{2e+2}, 3^{e+1},
3^{2e+1}), since every valuation above scales with e.

## 8. Remaining gaps

None for H-quad/H-diff themselves on the 36 | m 9t line, modulo
LTE3 (prior wave result) and the kernel parametrization, which
follows from LTE3 + ν a unit mod 3 (ν_1 ≢ 0 mod 3, §4). Still open
elsewhere: the F2 (locked-component) side, F4 in general, and any
Lean formalization (none built here).

## Files

- This note: wave46_SCJprime_Hquad.md
- Scripts: wave46_Hquad_numbers.py (closed-form coefficients vs fits),
  wave46_Hquad_Tcheck.py (full 729×729 F-check, expansion, H-diff,
  m = 45/90 kernel counts).
