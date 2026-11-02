# Wave 35, task 4 — F2-poly proved unconditionally (mechanism B saved)

## Verdict

**F2-poly is proved, with no hypothesis on e.** For every component
qt = p^{2f} ‖ D_m (p odd, p ≠ 3, so in particular every twin qt),
every component fiber satisfies |f_qt| ≤ 5m³·p^{e/2} ≤ 5m³·qt^{1/4},
where d = ord_𝔭(α), e = v_𝔭(α^d − 1). Hence mechanism B of the
wave-33 recount is saved for f ≥ 3 (see §4). This does not by
itself restore the wave-33 Δ → 0 theorem, which also lost RB1′′
(wave 34, joint splits) — only the F2-poly gap is closed.
Repository untouched; no Lean built.

## 0. Setup (waves 32 §1–2, 34 §1, taken as given)

α = 3 + 2√2, R = ℤ[√2], qt = p^{2f}, v_p(D_m) = 2f. The eigenvalue
argument gives SNF (p^f, p^f) for M^m − I, so M^m ≡ I (mod p^f),
α^m ≡ 1 (mod p^f), and rows ↔ C ∈ R_{p^f} via w_j = Tr(Cα^j),
j < m. Let d = ord_𝔭(α) (order mod 𝔭, 𝔭 | p). Then d ≥ 3
(α ≡ ±1 mod 𝔭 would force 𝔭 | 2 + 2√2 or 4 + 2√2, norms −4, 8),
p ∤ d (d | p ∓ 1), d | m, and by LTE
f = v_𝔭(α^m − 1) = e + v_p(m/d) ≥ e, where e = v_𝔭(α^d − 1) ≥ 1.
Order lifting gives ord_{p^f}(α) = d·p^{f−e}, so p^{f−e} ≤ m.

## 1. Lemma (level-e determination)

The multiset mod p^f determines (N, S) = (CC̄, Tr(C^d)) mod p^e.
*Proof.* Reduce values mod p^e: α has order d there, so the
reduced length-m multiset is m/d copies of the d-cycle of
C_e = C mod p^e. Cycle power sums in R_{p^e}, d prime to p:
p_2 = Σ_ζ Tr(Cζ)² = 2dN (Σζ² = 0, since ζ² ≠ 1 has ζ² − 1 a unit
mod 𝔭 for d ≥ 3), and p_d = dS (+ binom(d, d/2)N^{d/2} if d even;
cross terms vanish since Σζ^{2i−d} = 0 unless d | 2i − d).
As d is a unit mod p, (N, S) mod p^e is determined. ∎

## 2. Lemma (root count at level e)

At most 5d·p^{e/2} classes C_e ∈ R_{p^e} share a given (N, S).
*Proof.* Write C_e = p^k·C_1 with C_1 ∉ pR (k = 0 is the unit
case; C_e = 0 is one extra point). Dividing values by p^k, the
multiset of C_1 at level e′ = e − k is determined, so it suffices
to bound the unit case at level e′ and sum over k (geometric
series, factor < 2.4 for p ≥ 3, absorbed in the 5).
Let C_1 be a unit (inert) or have a unit coordinate (split).
Then C_1^d is a root X of X² − SX + N^d = 0 in R_{p^{e′}} with
X̄ = S − X. Put Z = X − S/2, so Z² = Δ/4, Z̄ = −Z. If
v(Δ/4) = 2t < e′, then Z = p^t·W with W² a unit: mod 𝔭 at most
2 roots, Hensel lifts uniquely (derivative 2W a unit, p odd),
so ≤ 2 roots. If v(Δ/4) ≥ e′, then Z² ≡ 0 and Z̄ = −Z force
Z = y√2 (inert) or (z, −z) (split) with y, z ∈ p^{⌈e′/2⌉}ℤ/p^{e′}:
p^{⌊e′/2⌋} possibilities. Hence ≤ 2p^{⌊e′/2⌋} valid X.
Given X, C_1 is a d-th root of X: ≤ d possibilities (unit
coordinate: (ℤ/p^{e′})^× cyclic, gcd(d, φ) = d as d | p − 1;
inert: kernel μ_d has order d, reduction mod 𝔭 injective since
1 + 𝔭 is pro-p; the other coordinate, if any, is forced by
Norm = N). Total ≤ 2d·p^{e′/2} per level, summed ≤ 5d·p^{e/2}. ∎

## 3. Theorem (F2-poly)

|f_qt| ≤ 5m³·p^{e/2} ≤ 5m³·qt^{1/4} for every qt = p^{2f}.
*Proof.* By §1–2, the reductions ρ(F) of a fiber F lie among
≤ 5d·p^{e/2} classes C_e. Each lifts to p^{2(f−e)} classes in
R_{p^f}. So |F| ≤ 5d·p^{e/2}·p^{2(f−e)} ≤ 5m³·p^{e/2}, using
d ≤ m and p^{f−e} ≤ m. Since e ≤ f, p^{e/2} ≤ p^{f/2} = qt^{1/4}. ∎
Remark: for f = 1 the sharp bound 2m (wave 32) stands; the new
content is f ≥ 3, where no bound of this shape was known.

## 4. Corollary (mechanism B saved for f ≥ 3)

Use wave-33 §4 counting with SC(c) (c = 5 after wave 34) and
RB3′ (Q₂, S₂ ≤ 8m²), but with M_qt depending on qt:
N_qt ≤ (m^c/4)(8m²)·qt = 2m^{c+2}·qt fibers containing qt,
M_qt ≤ s₃·S₂·|f_qt| ≤ m^{c/2}·8m²·5m³·qt^{1/4} = 40m^{c/2+5}qt^{1/4}.
Hence ΣΔ_F(B) ≤ Σ_qt N_qt·M_qt² = 3200m^{2c+12}·Σ_qt qt^{3/2}
≤ 3200m^{2c+12}·(Σ_qt qt)^{3/2} (Σx_i^{3/2} ≤ (Σx_i)^{3/2}).
Mechanism B is vacuous unless 12 | m (9-split lemma), where
H12-poly gives Σ_qt qt ≤ D_m·ε, ε = 18u³/α^{8u}, m = 12u, and
D_m = 2^a·S_m² ≤ m²·α^{12u} (2^a ≤ 8m², S_m ≤ y_{6u} < α^{6u}/2√2).
So ΣΔ_F(B)/D_m ≤ 3200m^{2c+12}·D_m^{1/2}·ε^{3/2}
≤ 3200m^{2c+13}·(18u³)^{3/2}·α^{−6u} → 0. ∎

## 5. Verification

- e-search (wave35_e_search.py): for all primes p ≤ 10⁵, e_β ≥ 2
  occurs only at p = 13 (d_β = 7, twin) and p = 31 (d_β = 15,
  non-twin); no e ≥ 3 anywhere. The theorem needs none of this.
- Smallest f ≥ 3 twin case, m = 182, p = 13, qt = 13⁶: v₁₃(D₁₈₂) = 6
  (exact recurrence), ord_{13⁶}(β) = 7·13⁴, 3 ∤ ord, so twin;
  e = 2 (α¹⁴ ≡ 1 mod 13², ≢ 1 mod 13³). Exact hash-grouped
  enumeration over all 13⁶ = 4,826,809 classes C (wave35_F2poly_182.cpp,
  largest hash group re-verified by exact sorting) gives max
  fiber size exactly 4732 = 13·364 (13 Γ-orbits of size 364),
  far below the theorem's 5m³·13 ≈ 3.9×10⁸.

## 6. Limits

The bound is crude (actual fibers are far smaller); its only use
is the polynomial-times-qt^{1/4} shape Hölder + H12-poly needs.
Lean formalisation is open.
