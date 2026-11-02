# Glued global Γ-bad fiber at m=12, and P_w test on it (Wave 8, task 2)

## Verdict

- **A global Γ-bad fiber at m=12 arising purely by gluing exists** — neither
  component fiber is bad, yet the global fiber splits into 2 Γ-orbits.
  This is in addition to the wave-4 component-derived bad fiber (mod 81 lift).
- **P_w is NOT killed by this fiber**: the two Γ-orbits have different
  sorted(w), so P_w separates them. Global P_w at m=12 remains open in
  general (this is one fiber, not an exhaustive m=12 test), but this
  gluing route does not kill it.

## Setup

m = 12, H = 6I − C − Cᵀ, Fix₁₂ = ker(H mod D),
D = 1536796800 = 128 · 81 · 25 · 49 · 121.
Γ = dihedral permutations j ↦ ±j + k (24 perms), acting by (v∘p)[j] = v[p[j]].
A fiber = sorted-multiset class. A global fiber is Γ-bad if it contains
≥ 2 Γ-orbits. w_y = (H·y)/D as an integer vector (entries in −1..5).

## The glued fiber (explicit, independently re-verified in Python)

Components (all other components zero):

- q = 128: (16, 80, 80, 16, 16, 80, 80, 16, 16, 80, 80, 16) — period 4,
  component fiber size 4, Γ-clean.
- q = 25: (5, 5, 0, 20, 20, 0, 5, 5, 0, 20, 20, 0) — period 6,
  component fiber size 6, Γ-clean.
- q = 81, 49, 121: zero vectors (component fiber size 1).

Global vector y (CRT of the above, verified: y[j] mod q equals the
component entry for every q, and H·y ≡ 0 mod D):

y = (1114177680, 345779280, 960498000, 806818320, 806818320, 960498000,
     345779280, 1114177680, 192099600, 38419920, 38419920, 192099600)

Witness permutation (not dihedral):

τ = (10, 4, 11, 6, 1, 8, 3, 9, 5, 0, 7, 2)

y′ = y∘τ = (38419920, 806818320, 192099600, 345779280, 345779280, 192099600,
            806818320, 38419920, 960498000, 1114177680, 1114177680, 960498000)

Checks (Python, independent of the C++ search that found it):

- H·y ≡ 0 and H·y′ ≡ 0 (mod D); sorted(y) = sorted(y′).
- Component-wise: v₁₂₈∘τ = (80, 16, 16, 80, 80, 16, 16, 80, 80, 16, 16, 80)
  ∈ Fix₁₂₈, and v₂₅∘τ = (20, 20, 0, 5, 5, 0, 20, 20, 0, 5, 5, 0) ∈ Fix₂₅;
  both are dihedral mates of their components, but with *different*
  dihedral effects — that mismatch is exactly the gluing.
- Γ-canonical forms differ (lexicographic minima over the 24 dihedral
  perms), so y and y′ are in different Γ-orbits.
- Exhaustive backtrack over this fiber (all τ with y∘τ ∈ Fix):
  exactly 24 vectors in Fix with this sorted multiset, forming exactly
  2 Γ-orbits of 12 vectors each. So the fiber is *exactly* this split,
  not just at least 2 orbits.

## P_w test on this fiber

- w_y = (4, 0, 3, 2, 2, 3, 0, 4, 0, 0, 0, 0),
  sorted(w_y) = [0, 0, 0, 0, 0, 0, 2, 2, 3, 3, 4, 4].
- w_y′ = (−1, 3, 0, 1, 1, 0, 3, −1, 3, 3, 3, 3),
  sorted(w_y′) = [−1, −1, 0, 0, 1, 1, 3, 3, 3, 3, 3, 3].
- sorted(w) differs ⇒ **P_w separates the two orbits ⇒ no kill**.

## What the search did (and did not) prove

1. Phase 1 (Python, `glue_m12_phase1b.py`): for every non-dihedral τ that
   maps a non-constant q=121 component vector to a fiber-mate (6624 such τ;
   this set is complete for v₁₂₁ ≠ 0, since every non-zero Fix₁₂₁ vector
   has at most 64 τ-mates), and for *every* choice of component vectors
   with v∘τ ∈ Fix, the dihedral-effect sets intersect — i.e. y∘τ is always
   Γ-equivalent to y. So **no glued splitting fiber exists with
   v₁₂₁ ≠ 0 and witness τ in that set**. (The earlier generic-combo run,
   `glue_m12_phase1.py`, found none either; the phase-1b argument is the
   complete version for those τ, via empty-intersection of dihedral
   effect sets.)
2. Phase 2 (C++, `glue_m12_phase2.cpp`): the remaining case v₁₂₁ = 0
   (the only constant vector in Fix₁₂₁). Searched τ from the q=25
   component set minus the q=121 set, with a dihedral-effect backtrack
   over components 25/49/81/128. Found the fiber above within the first
   19050 τ processed (search stopped after 5 hits, all the same fiber
   with different witness τ — **phase 2 was not run to exhaustion**).
3. Therefore: glued Γ-bad fibers at m=12 exist (exhibited above), P_w
   survives this one, and **global P_w at m=12 is still open** — an
   exhaustive m=12 test (1.5B points) was not done, and other glued
   fibers, in particular ones not of the v₁₂₁ = 0 form found here, were
   not all tested.

## Files

- `glue_m12_phase1.py`, `glue_m12_phase1b.py` — phase-1 searches.
- `glue_m12_phase2.cpp`, `glue_m12_phase2_bin`, `glue_m12_phase2_out.txt`
  — phase-2 C++ search (first hits).
- `glue_m12_fiber_orbits.py` — exact orbit count for the exhibited fiber.
- `glue_m12_explore.py`, `glue_m12_structure.py`, `glue_m12_tau.py`,
  `glue_m12_tau2.py`, `glue_m12_tausets.py` — component exploration
  (component fibers: 128: 39 fibers/0 bad, 81: 7/1 bad, 25: 5/0,
  49: 12/0, 121: 11/0; intersection of non-constant component τ-sets
  is exactly the 24 dihedral perms — this alone does *not* rule out
  gluing, because a component may contribute a constant/high-multiplicity
  vector, which is precisely how the exhibited fiber works).

Repository untouched; Lean not built; all enumeration is exact integer
arithmetic, a verifier artefact, not a Lean theorem.
