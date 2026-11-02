# Wave 29, task 2: the 3-restricted twin-sum lemma — Δ(m) = 0 unless 12 | m

## Theorem (conditional on RB1' and the wave-20 only-split-contributes lemma)

Δ(m) = 0 unless 12 | m. In particular Δ(p) = 0 for every prime p.

## Proof

A contributing global fiber contains a split 3-component fiber, by
RB1' (wave 25: every contributing fiber is one split 3-fiber × one
supported 2-fiber × one twin-qt fiber × singletons). So it suffices
to show there is no split 3-fiber unless 12 | m. By the 3-adic LTE
(wave 24, proved): v₃(D_m) = 0 if 4 ∤ m, and 2v₃(m)+2 if 4 | m.

- Case 4 ∤ m: D_m has no 3-part at all, so no split 3-fiber exists
  and Δ(m) = 0.
- Case 4 | m, 3 ∤ m: the 3-part is exactly 9. By Lemma 9-split below,
  the mod-9 component never splits, so no split 3-fiber exists and
  Δ(m) = 0.
- Hence Δ(m) ≠ 0 forces 4 | m and 3 | m, i.e. 12 | m. ∎

## Lemma 9-split (proved unconditionally)

Let 4 | m, 3 ∤ m. Then ker(H_m mod 9) has exactly 9 vectors, in 3
sorted-multiset fibers, each a single Γ-orbit. In particular the
3-part 9 never splits — on support or off.

*Proof.* H_m y ≡ 0 mod 9 is the recurrence y_{i+1} = 6y_i − y_{i−1}
mod 9. Its characteristic roots in R/9R are β = 3+2√2 and
β̄ = 3−2√2 (ββ̄ = 1), so every solution is y_i = Tr(Bβ^i) for a
unique B ∈ R/9R: indeed (y_0, y_1) = (2a, 6a+8b) is a bijection
R/9R → (Z/9)², since 2 and 8 are units mod 9.
ord_9(β) = 12: β^6 = −1 ≠ 1 and β^12 = 1 force ord ∈ {4, 12},
and β^4 = 1+3√2 ≠ 1. Since m ≡ 4 or 8 mod 12, β^m − 1 = 3√2 or
6√2, i.e. ±3√2 mod 9. Periodicity y_m = y_0, y_{m+1} = y_1 is
Tr(B(β^m−1)) = 0 and Tr(Bβ(β^m−1)) = 0. With B = a+b√2, the
first gives 3b ≡ 0 (resp. 6b ≡ 0) mod 9, i.e. 3 | b; the second
gives 3(2a+3b) ≡ 0 (resp. 6(2a+3b)) mod 9, i.e. 3 | a. Hence
3 | B, so ker(H_m mod 9) = {Tr(Bβ^i) : B ∈ 3R/9R}: 9 vectors.
Write B = 3B', B' ∈ R/3R; then y = 3y' with y'_i = Tr(B'β^i)
mod 3, β ≡ 2√2 mod 3, ord_3(β) = 4.
Γ acts on parameters: shift by j sends B' ↦ B'β^j, and
reversal+shift sends B' ↦ conj(B'β^j) (using β̄ = β^{−1} and
Tr(Xβ^{−i}) = Tr(X̄β^i)). The map B' ↦ y' is a bijection, since
(y'_0, y'_1) = (2a, 2b) mod 3. So Γ-orbits on vectors are the
orbits of B' under ⟨×β, conj⟩, which preserves the norm
(N(β) = 1). They are: {0}; the norm-1 class {1, −1, √2, −√2},
cycled by ×β; the norm-2 class {1+√2, 1−√2, −1+√2, −1−√2},
cycled by ×β. Three orbits.
Their sorted multisets (period 4, and 4 | m) are pairwise
distinct. B' = 0 gives all 0. The norm-1 orbit gives, per period,
(2,0,1,0), (1,0,2,0), (0,2,0,1), (0,1,0,2): counts
(0: m/2, 1: m/4, 2: m/4). The norm-2 orbit gives, per period,
(2,2,1,1), (2,1,1,2), (1,2,2,1), (1,1,2,2): counts
(1: m/2, 2: m/2, 0: 0). Zeros: all / half / none — so no two
orbits share a multiset. Each sorted-multiset fiber is exactly
one Γ-orbit: no splits. ∎

## Verification (exact integer arithmetic)

Script `wave29_9split_check.py` (ALL CHECKS PASS):
- m = 4, 8, 20, 28, 32, 40 at q = 9: |ker| = 9, 3 fibers, 0 splits.
- Parametrization y = 3·Tr(B'β^i) reproduces ker(H_m mod 9)
  exactly at m = 4, 8.
- Method validation at m = 12, q = 81: |ker| = 81, and the known
  census split fiber is reproduced exactly (36 points, 3 orbits),
  so the fiber/orbit code that finds no splits at q = 9 is the
  same code that finds the split at q = 81.

## Status and limits (honest)

- The theorem is conditional on RB1' (wave 25 restatement; its
  joint-nonzero exclusion is still the CRT-injectivity sketch)
  and on the wave-20 lemma that only split-component fibers
  contribute (S_q Γ-invariance sketch). Lemma 9-split itself is
  unconditional.
- The converse is NOT claimed: Δ(m) ≠ 0 is not proved for every
  12 | m (only observed at 12, 24, 36, 48, the last estimated).
- Wave-28 gap (ii) is untouched: controlling twin qt at 12 | m
  with unbounded odd part is still open, so this lemma alone
  does not give Δ → 0; it gives the 3-restricted form: twin
  sums need only run over m ≡ 0 mod 12, plus the unconditional
  2^k·t families.
- No counterexample exists: no m with 12 ∤ m and Δ(m) ≠ 0 is
  known, and the lemma rules one out under RB1'.

## Files

- This note: `wave29_Delta_12.md`.
- Check script: `wave29_9split_check.py`.
- Repository untouched; no Lean built.
