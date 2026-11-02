# Wave 47, task 1 — JBL single-q weak form PROVED (negation family) + cross-component consistency at (577,3)

## Verdict

**Single-q weak form PROVED for the negation family at q = 577** (8 mixed
pairs, identical layout, pis = {id, rev}): every triple-matching pair passes
under id or reversal — no longer empirical. **Cross-component consistency
PROVED for (577, 3)**: no quadruple-matching global pair forces id at one
component and reversal at the other; the forced π is always consistent.
Both results are at m = 32, for the pair ((0,512),(0,1)) vs ((0,512),(0,16))
and its negation family. Repository untouched; no Lean built.

## 1. Layout (exact, from pair data)

Pair: B₂ = (0,512) both sides; B_q = (0,1) vs (0,16); pis = {id, rev}.
Fibers, A side (A' swaps the two mixed fibers and the two class-2 fibers):
- (0,0): class 0, size 8; (0,3), (0,14): class 2, size 4 each (all p = 0).
- Mixed M1 = (4096,8): [1,3,9,11,17,19,25,27], classes {1,3}, 4/4 split.
- Mixed M2 = (4096,9): [5,7,13,15,21,23,29,31], classes {1,3}, 4/4 split.
Both mixed fibers share p = 4096; class p-multisets: 0,2 → {0×8};
1,3 → {4096×8}. Mixed position sets are +8/+16-closed. α⁸ ≡ −1,
α¹⁶ ≡ 1 mod 577R, so b_{i+8} = −b_i, b_{i+16} = b_i.
Pkl scan: 8 pairs with pis = {id, rev} and this exact position layout:
(0,k) vs (0,17−k), k = 1..8, all B₂ = (0,512). The proof below uses only
the layout + α-identities, so it covers all 8.

## 2. Square reduction

Classes 0,2 match under both id and rev automatically: homogeneous fibers
stay in their class (pair joints under id + uniqueness of (p,a) values),
and class-2 fibers share p = 0, so their unions match by per-fiber triple
matching. Only classes 1,3 matter, i.e. M1, M2. Write x = b₁, y = b₃
(A-side M1 bases): M1's b-multiset is {±x,±y}×2, M2's is {±L₁,±L₂}×2
for the linear map L below; A' side uses bases (x',y') = (bp₅,bp₇) and
Lp = −L. Joints under id ⟺ square systems {x²,L₁²} = {x'²,Lp₁²} and
{y²,L₂²} = {y'²,Lp₂²}; under rev ⟺ the crossed systems. ({±x}×2 is
determined by x², and multisets of squares determine multisets of ±pairs.)

## 3. The linear map and the 8-pattern check (exact, mod 577)

b₅ = −b₁ + 34b₃, b₇ = −34b₁ + b₃, i.e. L = [[−1,34],[−34,1]], L² = −I
(multiplication by ω = α⁴). M1 triple matching gives {x'²,y'²} =
{x²,y²}: 8 sign/swap patterns. M2 triple matching gives {L₁²,L₂²} =
{Lp₁²,Lp₂²}. Exact coefficient check (script, ALL PATTERNS COVERED):
- (x,y), (−x,−y): id holds identically.
- (y,x), (−y,−x): rev holds identically.
- (x,−y), (−x,y), (y,−x), (−y,x): the M2 sum-condition is 305xy = 0,
  so xy = 0; on y = 0 or x = 0 the id (first two) resp. rev (last two)
  system holds.
Hence every triple-matching pair passes under id or rev. ∎ (Wave 46's
fail-both = 0, formerly empirical, is now a theorem for this family.)

## 4. Cross-component consistency at (577,3): analytic proof

3 is a genuine D₃₂ odd component (3 | b₃₂ = 2⁵·3·17·577·665857) and the
UNIQUE odd prime with class-constant b-values: α⁴ ≡ 1 mod 3R, and
α⁴ − 1 = (576,408) has gcd 24 (prime divisors 2,3; mod 9, α⁴ = (1,3) ≠ 1).
So at q = 3, b_i depends only on class: for C₃ = (s,t), f = (2s,2t,s,t)
on classes 0,1,2,3. Quadruple matching (per-fiber (b577,b3) multisets
equal = full-global equality for two extensions) gives:
- Homogeneous fibers in classes 0,2 force s' = s (tags 2s, s).
- Mixed-fiber tag multisets {2t×4,t×4} = {2t'×4,t'×4} force t' ∈ {t,2t}.
- t' = t ⟹ f' = f ⟹ id ∈ π₃; t' = 2t ⟹ f' = f∘rev ⟹ rev ∈ π₃.
- Vote transfer: id-type tags + quadruple matching force per-fiber
  id-votes at 577 (class-1↔class-1, class-3↔class-3 b-multisets), hence
  id ∈ π₅₇₇; rev-type tags force rev-votes, hence rev ∈ π₅₇₇.
Therefore every quadruple-matching pair has a common π ∈ {id,rev} across
17, 577, 3. No q₁-forces-id / q₂-forces-reversal split exists at (577,3).

## 5. Exhaustive verification (counts)

Full enumeration over all C₅₇₇ (332,929 per side) × 9 C₃ values:
- Common 577 triple signatures: 83,521 (reproduces wave 46); all 332,929
  C₅₇₇ rows lie in common signatures.
- Common quadruple signatures: 749,958; total quadruple pairs: 11,978,511.
- C₃-relation matrix is block-diagonal by s with only t' = t and t' = 2t
  entries: id-type 3,995,142; rev-type 3,995,142; both-type (t = 0)
  3,988,227; VIOLATIONS 0.
- Nondegenerate witnesses (from wave-46 triple witnesses): rev-type
  (C₅₇₇ = (1,1) vs (1,576), C₃ = (0,1) vs (0,2)): quadruple match,
  π₅₇₇ = {rev}, π₃ = {(2,3,0,1),rev}, common {rev}. Id-type
  (C₅₇₇ = (1,1) vs (239,408), C₃ = (0,1) vs (0,1)): π₅₇₇ = {id},
  π₃ = {id,(2,1,0,3)}, common {id}.
(Note: π₃ also contains the extra partition perms (2,3,0,1) ⟺
(s',t') = (2s,2t) and (2,1,0,3) ⟺ (s',t') = (2s,t); they never occur
alone — each implies id or rev ∈ π₃ for quadruple pairs.)

## 6. Remaining gaps

- Rotation families (pis containing rotations, e.g. {(2,3,0,1),rev} or
  {(1,2,3,0),(3,2,1,0)}, different layouts): weak form still only
  empirical (wave 46 fail-both = 0); the square/pattern machinery should
  transfer, but the pattern check is not run for them.
- Other component pairs: at 665857 triple matching is vacuous for this
  mixed pair (wave 46 §6), so it constrains nothing; consistency for a
  general q₂ with non-class-constant b-values is open.
- General m: mixed-fiber weak form proved only at m = 32, negation
  family. The homogeneous case remains Theorem B (wave 46, m-free).
- No Lean formalization of any of this.

## Files

- This note: methods/wave47_JBL_weakform.md
- methods/wave47_weakform_proof.py (layout + L + exact 8-pattern check)
- methods/wave47_cross_577_3.py, methods/wave47_cross_T.npy (T matrix)
- methods/wave47_cross_witness.py (both witnesses PASS)
- methods/wave47_layout_scan.py (8/12 scanned pairs share the layout;
  4 rotation-family pairs differ)
