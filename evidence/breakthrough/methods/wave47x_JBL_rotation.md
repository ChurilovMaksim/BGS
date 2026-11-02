# Wave 47x, task E — JBL rotation families: weak form PROVED, (577,3) consistency PROVED

## Verdict

**Single-q weak form PROVED at q = 577 for all three rotation families R1,
R2, R3** (exact pattern checks, all 8 patterns covered). **Cross-component
consistency PROVED at (577,3) for R1 and R2** (analytic vote-transfer).
At q = 665857 (unique alpha^16 = -1 prime), triple matching is abundant
(8 per D) with FORCED singleton pi-sets (1200 ROT / 1200 PI2 per family)
— but JOINT (577,665857) consistency is NOT closed (overdetermined, no
joint pair constructed; tag-vote cannot extend past q = 3).
Census: 19,660,800 rotation pairs total; proved families cover 15.0%.
No Lean built, repository untouched.

## 1. The rotation families (m = 32, pair (8192,17))

From wave47x_rot_scan.py (capped scan: 12 pairs, 8 R1 + 4 R2; §2 uses only the layout):
- R1: A = ((0,512),(0,k)) vs Ap = ((0,512),(k',0)), pis = {ROT, PI2},
  ROT = (2,3,0,1), PI2 = (2,1,0,3). A-side as the negation family
  (class-0 size 8, two class-2 size 4, two mixed {1,3} size 8, 4/4
  splits); Ap mixed CROSSED: F1' = ({1,9,17,25}, {7,15,23,31}),
  F2' = ({3,11,19,27}, {5,13,21,29}).
- R2: A = ((0,512),(1,5)) vs Ap = ((0,512),(1,12)), pis = {ROT, PI2'},
  PI2' = (0,3,2,1). Mixed {0,2} fibers (size 8, crossed);
  homogeneous class-3 size 8, class-1 size 4 + 4, swapped 1 <-> 3.
- R3: A = ((2048,512),(0,4)) vs Ap = ((0,512),(1,5)),
  pis = {PI1 = (1,2,3,0), PI2 = (3,2,1,0)}. A mixed {1,3}, Ap mixed
  {0,2} (same values (0,2),(0,15)); homogeneous class-0 size 8 +
  class-2 size 4 + 4 on A, class-3 size 8 + class-1 size 4 + 4 on
  Ap. PI1 is NOT an involution, so the Theorem B convention
  (Ap class-r = A class-pi[r]) matters here.
- Separate wave-46 fine pair ((8064,8128),(16,8)) vs ((384,64),(5,12)):
  8 fibers of size 4; exactly 1 triple-matching pair in 577^2 x 577^2,
  passing under both pi's — weak form exact there by enumeration.

## 2. Pattern proof of the weak form at q = 577 (R1/R2 share one, R3 has its own)

Mod 577: alpha^8 = -1, alpha^16 = 1, so b_{i+8} = -b_i, b_{i+16} = b_i;
mixed-fiber b-multisets are {+-x, +-y} x 2. Bases: A fiber-1 (x,y),
A fiber-2 = L(x,y); Ap fiber-1 (x',y'), Ap fiber-2 = Lp(x',y'), with
(wave47x_rot_maps.py, verified on random C)
  L  = ((-1,34),(-34,1)), L^2 = -I (multiplication by omega = alpha^4);
  Lp = ((1,34),(34,1)).
Homogeneous legs are automatic (per-fiber-value triple matching gives
equal b-multisets; homogeneous fibers sit in single classes on both
sides). Only mixed legs matter. Triple matching: T1: {x^2,y^2} =
{x'^2,y'^2} (8 sign/swap patterns S); T2: (L1^2+L2^2, L1^2 L2^2) =
(Lp1^2+Lp2^2, Lp1^2 Lp2^2) after composing Lp with S. Targets: ROT
needs x^2 = y'^2 and L1^2 = Lp2^2; PI2 needs x^2 = x'^2 and
L1^2 = Lp1^2 (other legs follow from T1).
Exact check (wave47x_rot_pattern.py, ALL PATTERNS COVERED):
- Non-swap (x' = +-x, y' = +-y), PI2 candidate: (+x,-y), (-x,+y)
  hold identically; (+x,+y), (-x,-y): T2sum = 305 xy (same
  coefficient as wave 47's M2 condition!) forces xy = 0, and legs
  = 441 xy vanish on both subloci x = 0, y = 0.
- Swap (x' = +-y, y' = +-x), ROT candidate: (+y,-x), (-y,+x)
  hold identically; (+y,+x), (-y,-x): same 305xy / 441xy
  sublocus argument.
Hence every triple-matching pair passes under ROT or PI2. ∎ The proof
uses only the layout + alpha-identities, so it covers every pair with
the R1/R2 position layouts (not just the representatives).

Pattern proof for R3 (wave47x_rot_pattern_R3.py, ALL PATTERNS
COVERED): A mixed (x,y) = (b5,b7), M2 = L(x,y),
L = ((1,543),(34,576)); Ap mixed (x',y') = (b'0,b'2), F2' =
Lp(x',y'), Lp = ((576,34),(543,1)). Under Ap class-r = A
class-pi[r], PI1 legs [Lp1^2 = L1^2, Lp2^2 = L2^2] (first legs
auto in non-swap) and PI2 legs [Lp2^2 = L1^2, Lp1^2 = L2^2]
(first legs auto in swap); homogeneous legs automatic. All 8
patterns: identical hold identically; sign patterns give T2sum
= 305xy, legs = 136xy, so T2 forces xy = 0 and both legs vanish
on x = 0, y = 0. Hence every triple pair passes under PI1 or
PI2. ∎ (L1^2, L2^2 equal R1's — one shared core.)

Exact triple test (completed, wave47x_rot_triple.json): R1, R2,
R3 IDENTICAL — 83,521 common signatures; 1,329,409 triple pairs;
661,248 bad per pi; failboth = 0.

## 3. Cross-component consistency at (577,3): analytic proof + exhaustive check

Tag structure at q = 3 (verified): b_3(i) depends only on class(i),
f = (2s,2t,s,t) on classes 0,1,2,3, for C_3 = (s,t). Quadruple
matching = per-fiber (b577, b3) multisets equal. The C_3-relation
is forced analytically by tag marginals per fiber: homogeneous
marginals pin one coordinate, mixed marginals pin the other to
two options.
- R1: homogeneous (0,0)-fiber tags force s' = 2s; mixed tags
  {2t x 4, t x 4} force t' in {t, 2t}: (s',t') in {(2s,t),
  (2s,2t)}: PI2-type / ROT-type.
- R2: homogeneous tags force t' = 2t; mixed tags force s' in
  {s, 2s}: (s',t') in {(s,2t), (2s,2t)}.
Vote transfer: t' = t (R1 PI2-type) keeps tags aligned
class-by-class, so quadruple equality forces A class-1 b577 =
Ap class-1 b'577 and A class-3 = Ap class-3: PI2 works at 577.
t' = 2t (ROT-type) swaps tags, forcing A class-1 = Ap class-3
and A class-3 = Ap class-1: ROT works at 577. Same with s'/s
for R2. Degenerate t = 0 (R1) / s = 0 (R2): tags carry no
separation, but then pi_3 contains BOTH pi's (tabulated in
wave47x_rot_pi3.py over all 81 (C_3, C'_3) pairs), and the weak
form supplies one at 577. Hence a common pi exists (pattern type
determines joint type: non-swap -> PI2-type, swap -> ROT-type).
(Exhaustive T-matrix COMPLETED: R1, R2, 0 violations,
11,978,511 quadruple pairs, 749,958 common quad signatures each
— as the negation family; all three witness types confirm a
common pi in pis. §3 does not depend on it.)

## 4. General q_2: q = 665857 characterized, joint consistency OPEN

- Uniqueness lemma: b-values are class-determined at q (b_{i+4} = c b_i)
  only if alpha^4 = beta^8 = (17,12) = c mod qR, i.e. q | 12. So q = 3
  is the UNIQUE odd prime with class-constant b: tag-vote cannot
  extend past q = 3.
- At q = 665857 (alpha^8 = (0,470832), alpha^16 = -1): per-D
  solver over 300 random D per family: 2400 triple pairs each
  (8 per D), pi-set ALWAYS singleton: 1200 {ROT} / 1200 {PI2}
  (R1), 1200 {ROT} / 1200 {PI2'} (R2) — rigid, not vacuous
  (negation: 0/500).
- JOINT (577,665857) open: 16 group equations in 2 unknowns,
  overdetermined; no joint pair constructed, so no counterexample
  nor proof claimed. Next: solver-based joint search or a twist
  argument (wave 45 §3-§4).

## 5. Remaining gaps

- (577,3) consistency for R3: NOT done (non-involution PI1 needs its
  own tag analysis; §3 covers R1/R2 only).
- Weak form at other m (Theorem B is m-free, but rotation layouts at
  other m are unexamined); prime-power components with alpha^16 != 1
  (lifting 665857 to 665857^e) untested.
- Joint (577,665857) consistency: open (see §4).
- No Lean formalization of any of this.
- Full layout census COMPLETED (wave47x_layout_count_full.log):
  19,660,800 ordered rotation pairs in 72 (pi-set, layout)
  classes. Proved: R1/R2/R3 classes + reverses by symmetry
  (pi -> pi^-1) = 6 classes, 2,949,120 pairs (15.0%). Open: 66
  classes, 16,711,680 pairs (85.0%) — 8x4 shape 12,582,912
  (64.0%), 4x8 shape 1,179,648 (6.0%), other 2x8 pi-sets
  2,949,120 (15.0%). Weak form for those families is OPEN.

## Files

- This note: methods/wave47x_JBL_rotation.md
- methods/wave47x_rot_scan.py (pair enumeration + layouts); rot_maps.py (L, Lp solves)
- methods/wave47x_rot_pattern.py (8-pattern proof, R1/R2)
- methods/wave47x_rot_pattern_R3.py (8-pattern proof, R3)
- methods/wave47x_rot_pi3.py (pi-set(3) tabulation)
- methods/wave47x_rot_triple.py + .json (exact triple test, §2); cross_rot.py (corroboration); layout_count.py + _full.log (census, §5)
- methods/wave47x_rot_665857.py (complete per-D 665857 solver)
