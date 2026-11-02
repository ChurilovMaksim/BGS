# Wave 33, task 4 — lemma Q5: FALSE as stated, corrected lemma Q5* proved

## Verdict

Q5 as stated in wave 32 ("vertex equations + level-4 constraints force
the level-5 twist to vanish") is FALSE. The twist parameter η₂ is pinned
only up to a line, not to 0 — and vanishing is not needed: per-class
multisets match anyway. G1 at f=5, case (2,3), follows from the corrected
lemma Q5* below, not from Q5. Repository untouched, no Lean built
(proof sketch + exact checks, not Lean).

## Counterexample (exact, p=13, P=13⁵, m=30758)

A = (238170, 161484) has exactly one tier-3 orbit (i₀=13,
C = (268501, 301496), T₂ = 12) and one tier-2 orbit (i₀=6, T₁″=6, T₂=1).
Solving the full Q5 system (Tr(η₀)=0, Tr(Dη₀)=0 per tier-2/3 orbit,
both vertex equations) over (η₀, η₂) ∈ (R/13)² gives 13 solutions,
12 with η₂ ≠ 0 — all with η₀ = 0, η₂ = (0, y), y ≠ 0.
Direct per-class test mod 13⁵ (classes i mod 2): twists
1 + 13⁴η₂ with η₂ = (0,1), (0,2), (0,3) all give matching per-class
multisets, although η₂ ≠ 0. Control: η₂ = (1,0), which violates the
tier-3 vertex equation (Tr(Cη₂) ≠ 0), gives mismatch, as expected.
Two further independent sequences confirm:
A = (143956, 61901) (tier-3 i₀=5, T₂=8) and A = (41341, 24231)
(tier-3 i₀=4, T₂=8), both match with η₂ = (0,1) ≠ 0.

## Why vanishing fails

η₂ enters the level-5 analysis only through r_C = Tr(Cη₂), one linear
form per tier-2/3 orbit, and level-4 constraints do not touch η₂ at all
(p⁴η₂ ≡ 0 mod p⁴). The two paired orbits give the SAME r-condition:
C₂ ≡ −C₃ mod 13 (§3), so r₂ = 0 ⟺ r₃ = 0, leaving η₂ free on the line
ker Tr(C·) ⊂ R/13. In the example the pair of vertex equations does
force η₀ = 0 (level-4 alone leaves η₀ = (0,y) free; the two quadratics
together give y = 0), but η₂ survives on its line. So a single orbit
never forces vanishing (wave 32's gap note), and neither does the full
system in the generic paired case.

## 1. Pairing lemma (verified 80/80)

Tier-3 at i₀ ⟹ tier-2 at i₀+7, with C₂ ≡ −C₃ mod 13. Mechanism:
α has order 14 mod 13, so α⁷ ≡ −1 mod 13 (unique order-2 element);
writing α⁷ = −1 + 13w gives Tr(Cα⁷u) ≡ 13·Tr(Cwu) mod 13³, which has
valuation exactly 2 generically. Verified: 80/80 tier-3 orbits over
fresh seeds have a tier-2 partner at +7, 0 have a tier-3 partner, and
80/80 satisfy C₂ ≡ −C₃ mod 13. Hence a lone tier-3 orbit does not
occur; the generic tier-3 case is the pair above. (The α^{L₀/2} ≡ −1
step as written needs R/p a field; the split case is not checked.)

## 2. Corrected lemma Q5* (sketch)

Under the level-4 output, per-class multisets mod p⁵ match ⟺ the
per-fiber tier-2/3 patterns match. Proof: non-collapsed/tier-1 orbits
contribute to each mod-p⁴ fiber a full F_p top-digit line, invariant
under the fiber-constant twist shift, and level-4 matching fixes the
fiber counts, so their contribution is uniform and identical on both
sides; tier-2/3 orbits stay in their fibers (δ_C = 0 by the level-4
singleton condition, wave 26 §4); fibers have disjoint value sets, so
global multiset equality forces the tier-2/3 patterns to match fiber
by fiber. Vertex equations are the single-orbit case of this; pooled
matching suffices when a fiber holds several tier-2/3 orbits. Hence
G1 (2,3) holds: per-class matching is exactly the conclusion, and no
vanishing of η₂ is required. Subcase where Q5-as-stated DOES hold: if
the tier-2/3 representatives span (R/p)* as linear forms (≥2
independent C's), then r_C = 0 for all of them forces η₂ = 0.

## Limits and files

- p=13 only for the exact checks; the Q5* sketch is general for odd p
  (modulo the field/split caveat in §1 and the wave-26 singleton input).
- Side catch: tier-3 means Tr(Cu) ≡ 0 mod p³, i.e. t = 0 as an integer
  mod p³; an initial vp(0) = 0 bug in the check script hid every
  tier-3 orbit until fixed (wave33_Q5_check.py).
- Files: wave33_Q5_check.py (search + per-class test),
  wave33_Q5_system.py (system solve + direct test). Remaining for
  G1 at f=5: M5, R50, and Lean formalisation.
