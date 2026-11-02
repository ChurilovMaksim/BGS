# Wave 29, task 1 — R30: the v2 step PROVED via the r = 2 ring power sum

**Verdict: the v2 step GOES THROUGH.** For a pure level-1 twist, full
multiset preservation mod p³ forces c = 0 — no gap hypothesis, no
v1-P₂, no δ. The flagged carry term ΣIm(δ_j)η̄_j ≠ 0 is real, but it
lives in the digit expansion, which the proof never uses. Repository
untouched, no Lean built.

## 1. Why the digit route is blocked (the flag, explained)

Gap symmetry holds element-wise, conj(T_j) = T_{r−j} mod p³, but the
base-p section is not a homomorphism: negating mod p³ borrows. With
T_j = τ̄_j + pδ_j + p²ε_j (section lifts), the correct digit law is
**δ_{r−j} = conj(δ_j) + b(τ̄_j)**, b = (0, p−1) if η_j ≠ 0 else 0,
i.e. w_{r−j} = −w_j − [η_j ≠ 0]. So w is NOT odd under gap symmetry:
e.g. at p = 5, A = (44, 76): δ_0 = (1, 4) but δ_{r−0} = (1, 0), not
(1, 1); Σξw = 1 ≠ 0. Digit moments at v2 are further polluted by
multiplication carries k_j = (c·t_j)//p and digit wraps (2ξ mod p,
4η mod p): the digit Σv² coefficient is a floor sum, not a clean
mod-p expression (752/1637 formula mismatches in the probe). Do not
retry digit moments at v2. (Wave 24's δ-route failure at f = 2 is the
same phenomenon one level down.)

## 2. Proof (all arithmetic in R/p³, no digits)

p odd, |H₀| ≥ 3, C a unit mod p³, β of order |H₀| (coprime to p),
N(β) = 1, so β̄ = β⁻¹. Orbit v_j = Tr(Cβ^j), W_j = Tr(Cβ^j√2) in
ℤ/p³. Twist C′ = C(1 + pc√2), c ∈ 𝔽_p. Then exactly in ℤ/p³:
v′_j = v_j + pc·W_j (trace is linear; pc·W_j needs W_j only mod p²).
Second power sum:
Σ(v′)² − Σv² = 2pc·Σv_jW_j + p²c²·ΣW_j² (mod p³).
Now v_jW_j = √2[(Cβ^j)² − (C̄β̄^j)²] (cross terms cancel), and
Σ_j (β²)^j = Σ_j (β̄²)^j = 0: β² ≠ 1 since |H₀| ≥ 3, and β² − 1 is a
unit (β̄² ≠ 1 mod p), so the geometric sum vanishes. Hence
**Σv_jW_j = 0** in ℤ/p³. And W_j² = 2[(Cβ^j)² − 2N(C) + (C̄β̄^j)²]
(ββ̄ = 1), so **ΣW_j² = −4|H₀|N(C)** in ℤ/p³. Preservation gives
p²c²·(−4|H₀|N(C)) ≡ 0 (mod p³), i.e. c²·4|H₀|N(C) ≡ 0 (mod p);
p odd, gcd(|H₀|, p) = 1, N(C) a unit, so **c = 0**. ∎
Only the second power sum is used — not the full multiset. |H₀| ≤ 2
breaks it (β² = 1, geometric sums = |H₀|), exactly the wave-25
degenerate cases; p = 2 breaks it (4 not a unit).

## 3. Why f = 2 differs, and why this lifts

Mod p² the p²c² term vanishes, so r = 2 gives nothing at f = 2 —
that is why f = 2 needed the digit P₂ (wave 24/28). At f = 3 the same
computation kills c outright. By reduction mod p³, the result also
covers pure level-1 twists at every f ≥ 3.

## 4. Numerical confirmation

- Ring identities ΣvW = 0, ΣW² = −4|H₀|N, and
  Σ(v′)² − Σv² = p²c²(−4|H₀|N) ≠ 0 for c ≠ 0: 540 random cases
  (p = 5, 7, 13; t = 1, 2, 4; random units, random c ≠ 0), 0 failures
  (script wave29_R30_v2_check2.py). The argument needs no gap
  hypothesis, and the check runs on all units, not only gap cases.
- Borrow formula δ_{r−j} = conj(δ_j) + b verified in the §1 example.
- Independent probe (wave29_R30_v2_probe.py): in 1637 gap cases at
  p = 5, 7, 13, the full multiset is preserved ⟺ b1 = 0 (hence
  c = −2b1 = 0 by wave-28 P₂) — exactly as the theorem predicts.

## 5. Scope (honest)

Proved: the v2 step for the pure level-1 twist in the R30 transfer
(G1 at f = 3, s = 0). NOT claimed: mod-p normalisation and the
reduction of a general C′ to twist form at f = 3 (the remaining
R30 steps); Lean formalisation. As in wave 28, checks use
Teichmüller orbits — no genuine k = 3 prime is known below 2×10⁹,
but R30's setting has β Teichmüller, exactly what is checked.

## Files

- This note: wave29_R30_v2.md
- Checks: wave29_R30_v2_check2.py (ring identities + borrow),
  wave29_R30_v2_probe.py (1637-case multiset probe)
- Prior: wave28_R30_P2.md (v1-P₂, residual Q, the flag),
  wave27_R30_gapcond.md, wave25_G1_f2s0_close.md §2 (f = 2 transfer)
