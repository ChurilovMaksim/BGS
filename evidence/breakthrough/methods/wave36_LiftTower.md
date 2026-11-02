# Wave 36, task 2 — Lift-Tower Lemma: FALSE as stated, repaired with base e+1

## 1. The lemma as stated (wave 35, task 3)

Trace levels f (C ∈ R/p^f, R = Z[√2], α = 3+2√2, fiber = shared sorted
d_f-cycle of Tr(Cα^j), d_f = ord_{p^f}(α); split = ≥ 2 Γ-orbits;
counts are on-support split fibers). Wave 35 claimed: every split fiber
mod p^{f'} reduces to a split fiber mod p², at most one per depth, so
n_q ≤ (f'−1)·n(p²) = O(m² log m). Data cited: (147, 343): 10 = 5 × 2;
(108, 81): 3 = 1 × 3.

## 2. Verdict: FALSE as stated — counterexample at (182, 13)

Exact census (wave36_tower.py, same trace-model code as wave 35):

| case | e = v_p(α^d−1) | N(1) | N(2) | N(3) | N(4) |
|------|------|------|------|------|------|
| (147, 7) | 1 | 0 | 5 | 10 | – |
| (108, 3) | 1 | 0 | 1 | 2 | 3 |
| (150, 5) | 1 | 0 | 2 | 4 | – |
| (36, 3) | 1 | 0 | 1 | 2 | – |
| (182, 13) | 2 | 0 | **0** | **546** | – |

At (182, 13): level 2 has **0** split fibers, level 3 has **546** genuine
on-support split fibers (sizes 2366 = 13·182 and 4732 = 13·364, 13 orbits
each; max 4732 matches wave 35 F2poly exactly). Since level 2 has no split
fiber at all, no level-3 split fiber reduces to one. The lemma is false.

## 3. Mechanism: the base level is e+1, not 2

Let d = ord_p(α), e = v_p(α^d−1). Then d_f = d·p^{max(0, f−e)} (LTE).
At (182, 13): d = 14, α¹⁴ ≡ 1 (mod 169) but ≢ 1 (mod 2197), so e = 2 and
d₂ = d₁ = 14. At level 2 the lines j = j₀ + 14t are CONSTANT
(α^{14t} ≡ 1 mod 169), so the level-2 multiset is a 13-fold repeat of the
A-tuple and no new splitting occurs (census: 0 split). The Z = ∅ splitting
mechanism of wave 35 first operates at level 3 = e+1, where
α^{14t} ≡ 1 + 169·u·t (mod 2197) and lines cover full lift fibers.
In the e = 1 cases the base is e+1 = 2, which is why wave 35's data fit.

## 4. The refined tower (verified at all e = 1 cases)

Split every level-f split fiber into GENUINE (no element divisible by p)
and DEGENERATE (all elements divisible by p; degeneracy is a fiber
property since Tr(C), Tr(Cα) determine C mod p, p odd). Then:

- **(LT3) proved formally.** If F_f is degenerate, F_f = p·F_{f−1} for a
  split fiber F_{f−1} at level f−1, same size and orbit count: cycle(pD)
  = p·cycle(D) up to the multiplicity d_f/d_{f−1}, and pD·α^j = pD·α^k
  (mod p^f) ⟺ Dα^j = Dα^k (mod p^{f−1}), so orbits correspond 1-1.
  Checked exactly at every degenerate fiber in §2 (bad = []).
- **(LT1)+(LT2) for genuine fibers, verified exactly.** At (147, 7),
  (108, 3), (150, 5), (36, 3): every genuine level-f split fiber reduces
  mod p² to a split level-2 fiber, exactly one per base fiber
  (per-base counts [1, 1, …], bad = []), and the genuine fiber EQUALS
  the full preimage of its base fiber (checked element-wise:
  (147, 7) f=3: 294 × 49 = 14406; (108, 3) f=3: 36 × 9 = 324,
  f=4: 36 × 81 = 2916). Hence N(f) = G(f) + N(f−1) with G(f) = N(2):
  (147, 7): 10 = 5 + 5; (108, 3): 2 = 1 + 1, 3 = 1 + 2.
  Wave 35's "10 = 5 base × 2" is therefore 5 genuine lifts + 5 degenerate
  lifts, not 2 genuine lifts per base.

## 5. Repaired lemma, and what is still a hypothesis

**Repaired Lift-Tower Lemma.** Let b = e+1. Then (LT3) holds as above;
genuine split fibers at level f ≥ b reduce to split fibers at level b,
at most one per base fiber; hence N(f) ≤ (f−b+1)·N(b) = (f−e)·N(e+1).

The genuine part follows from one exact hypothesis:

**Full Blindness.** Let C ∈ R/p^f (f ≥ b) be genuine with Z(C mod p) = ∅
(B_{j₀} = Tr(Cα^{j₀}u) ≢ 0 mod p ∀j₀, u from α^d = 1 + p^e·u). Then the
multiset M(C) mod p^f depends only on C mod p^b.

Full Blindness is verified exactly at the four e = 1 cases (genuine =
full preimage) but unproved in general; combined with the level-b line
analysis (split ⟷ Z = ∅ at level b, p orbits per fiber, same proof as
wave 35 §f'=2 with p^e in place of p) it gives (LT1)+(LT2) for base b.
At (182, 13) there is no level above b = 3 (v_13(D_182) = 6), so the
repaired genuine claim is untested for e ≥ 2.

## 6. Consequence for SC counting

The tower SHAPE survives (linear in f, base e+1), but a polynomial bound
on N(b) needs more: crudely N(b) ≤ p^{2e}/d, and p^{2e} is not polynomial
in m in general (only Wieferich-type rarity keeps it small: e ≥ 2 found
only at p = 13, 31 in the wave-35 search to 10⁵). Numerically SC is safe
everywhere tested — worst case (182, 13): Σ ≈ 546·4732² ≈ 1.2×10¹⁰
against m⁵ ≈ 2.0×10¹¹ — but SC(c) via the tower is conditional on
Wieferich-type control of e, now a named gap. The 2-part tower is
separate (wave-35 5-per-level pattern still open).

## 7. Minor anomaly (immaterial)

In the (182, 13) reduction check, a few genuine fibers' canon reductions
did not match any level-2 hash (None) instead of matching a 1-orbit
fiber. The verdict does not depend on this: level 2 has 0 split fibers
by direct census, so no reduction can land on a split fiber. Cause of
the None entries not yet isolated; the level-3 census itself is
cross-validated by the wave-35 F2poly max fiber (4732).

Scripts: wave36_tower.py (tower census + genuine/degenerate analysis),
wave36_preimage.py (full-preimage check), wave36_inspect147.py (degenerate
fiber inspection). Repository untouched, no Lean built.
