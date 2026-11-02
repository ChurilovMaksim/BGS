# Wave 39, task 5 — Outside-regime vanishing: SLICE PROVED (odd p, scope §5)

## Verdict

For odd p, every split fiber at level f ≥ 2 is an iterated exact lift of a split
fiber at level b = e+1: genuine fibers are full preimages of base fibers, degenerate
fibers are p× lifts. The tower for f ≥ b is LT1+LT2 (wave 37) + LT3 (wave 36); the
missing piece — no split fibers below base — is proved here for all levels that
exist: level 1 (wave 32) and level 2 at the e≥2 primes 13, 31.

## 1. Tower for f ≥ b (assembly)

(1) Level-b line analysis (wave 35 §f'=2 with p^e in place of p): lines
Tr(Cα^{j0+dt}) = A_{j0} + p^e·t·B_{j0} (mod p^{e+1}), t ∈ ℤ/p; split ⟺ Z = ∅
(Z = {j0 : B_{j0} = 0}, |Z| ≤ 2), with exactly p orbits.
(2) Genuine (Z = ∅): Full Blindness (wave 37) gives M_f(C) from {Tr(Cα^{j0}) mod p^e}
alone, so a genuine level-f fiber is the full preimage of its level-b fiber, at most
one per base fiber (LT1/LT2).
(3) Degenerate: F_f = p·F_{f−1}, same size and orbit count (LT3, wave 36 §4).
(4) Iterating (3) down from f stops at a genuine split fiber at level f*; §2 forces
f* ≥ b, so every split fiber at level f ≥ b comes from level b, and
N(f) ≤ (f−e)·N(b).

## 2. Below base: no split fibers at levels 1 ≤ f ≤ e

Level 1 is wave 32 (moments: (N,S) determines C up to Γ). For f = 2 ≤ e (the only
below-base level ≥ 2 at the known e = 2 primes 13, 31), let C' be in the fiber of C.
By level 1, C' ≡ γC (mod p); Γ-adjust to C' = C + pE. Two cases for v_j = Tr(Cα^j).
(a) All-distinct values: two consecutive unique positions force w_j = Tr(Eα^j) = 0
there, hence E = 0 (det 16, p odd). This covers split t = c₂/c₁ ∉ ⟨α₁⟩, where
v_j = v_{j'} ⟺ α₁^{j+j'} = t is impossible, so no value repeats.
(b) Paired case C̄ ≡ Cα^k (mod p): automatic for inert d = p+1 (norm-1 subgroup
= ⟨α⟩) and for split iff t ∈ ⟨α₁⟩. Then values pair by p+q ≡ k (mod d).
Class sums (power sums mod p²) collapse to ONE condition Tr(EX₀) = 0, where X₀
spans ker(conj − α^{−k}) (1-dim; at most one pair has vanishing sum α^p+α^q = 0).
So E = tE₀. On a swap pair {p,q}, (w_p,w_q) = (δ_{pq},−δ_{pq}) with
δ_{pq} = Tr(Fα^{p−k}), F = (C̄ − Cα^k)/p. Two consecutive swap-pair representatives
(existence verified for d = 14, 15 for all k and zero patterns: 0 bad cases) give
Tr(Fα^{r−k}) = t·Tr(E₀α^r) at r, r+1, hence F = tE₀α^k by Lucas determinacy, so
C' = C + ptE₀ = C̄α^{−k} ∈ Γ·C. If no swap pair occurs, w = 0 everywhere, E = 0.
Hence the fiber is a single orbit. Small-d singleton configurations (d ≤ 8) occur
only at p = 7, 3, 41, 5, 239, 17, all e = 1 (checked by gcd of α^d−1 coords), so
never below base. The crude count gives the same for all d ≥ 15.

## 3. Exact verification

Level-2 all-fiber censuses (f = 2 ≤ e): p = 13: 1105 fibers, 0 split; p = 31:
31265 fibers, 0 split. Level-3 census (182,13) re-run: 8749 fibers, 546 split,
all on-support, mixed = 0, degenerate split = 0.
Level-4 tower check (182,13), via Full Blindness shortcut (C mod 169 only):
all 546 level-3 split fibers are hit by exactly one M₄-group, 0 missed; M₄/M₃
partitions differ only on non-split Z≠∅ classes, as expected (M₄ then depends on
higher digits). Orbit lifting: for all 546 on-support split fibers, the 169 lifts
of one element give exactly 13 level-4 orbit canons, 0 reduction mismatches.
Sampled LT3 at level 4: 20/20 clean (13·F₃' a level-4 fiber, orbits matching).

## 4. Computational artifact (not a discrepancy)

numpy S16 strips trailing NUL bytes on read, so 118/28561 census digests ending in
0x00 read back one byte short. Fiber grouping (np.unique) is unaffected, since the
truncation is consistent; all counts above use the grouping, not raw digests.

## 5. Scope and remaining gaps

Odd p only (2-part tower separate). On-support transfer at level 4 assumes mixed = 0
at level 4 (verified at levels ≤ 3, not run at level 4). The Paired Swap counting is
proved for d = 14, 15 and d ≥ 15; d ∈ {9,…,13} with e ≥ 2 is open in principle (no
such prime known; e ≥ 3 primes none known to 10⁵, and would also need digit
induction for f ≥ 3). No Lean built; repository untouched.
Scripts: wave39_OutsideVanishing_checksAB.py, wave39_OutsideVanishing_checkC.py,
wave39_OutsideVanishing_debug.py.
