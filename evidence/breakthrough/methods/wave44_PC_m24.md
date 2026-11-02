# Wave 44, task 5 — PC at m=24 with two constraining odd primes

## Verdict

**Slice PC is proved at m=24: 0 failures in 376,185,238 fiber pairs.**
Full-space PC is NOT closed by this alone: the m=18 lift (§4 of
wave 35) fails here, because Π_q is not full at the other components
(§4). What remains is one named compatibility step. No Lean built,
repository untouched.

## 1. Components at m=24 (exact)

D_24 = 2^9 · 3^4 · 5^2 · 7^2 · 11^2 · 17^2 · 1153^2 (verified by
factorization). Here t = gcd(24,4) = 4, so classes are r mod 4 and
π ∈ D_4 (rotations r ↦ r+b, reflections r ↦ −r+b, 8 maps).

**Two constraining odd primes: 17 and 1153.** Tr(α^6) = 39202 =
2·17·1153, so α^12 = −1 in R/pR for p ∈ {17, 1153} (verified:
α^12 = (−1, 0) mod p, α^24 = (1, 0)). Both primes split in ℤ[√2]:
N(5+2√2) = 17, N(35+6√2) = 1153. Since 17^2 ‖ D_24 and 1153^2 ‖ D_24,
v_𝔭(α^24−1) = 1 for each 𝔭 above p (e = 1).

**Kernels.** For p ∈ {17, 1153}, ker mod p^2 =
{ p·Tr(C α^i) mod p^2 : C ∈ R/p }, of size p^2. Proof of
completeness: p splits, so R/p^2R ≅ R/𝔭^2 × R/𝔭̄^2; on each
length-2 factor, multiplication by (α^24−1) with valuation 1 has
kernel of size p; total p^2. Sequences ↔ A ∈ Ann(α^24−1) via
(Tr(A), Tr(Aα)) (injective: 2, 8 invertible mod p^2), and the
parametrization gives p^2 distinct annihilator elements (α^24 = 1
mod pR). Verified by brute force at 289 (kernel == param set,
289 vectors, all values divisible by 17, antiperiod 12 exact) and
by distinctness (first two coordinates determine C) at 1153^2.
All kernel sequences are antiperiodic: y_{i+12} = −y_i.

**Non-constraining odd components: 81, 25, 49, 121.** N(α^12+1) =
2 + Tr(α^12) = 4·17^2·1153^2, coprime to 81, 25, 49, 121, so
α^12+1 is a unit mod each (the wave-35 unit property). Kernel
sizes are q each (brute force: 25, 49, 81, 121).

**2-part: 512.** Kernel has 512 vectors (brute force), periods
1 (4), 2 (28), 4 (96), 8 (384).

## 2. Slice and method (marginal projection, wave-35 style)

Slice: ker_289 × ker_1153^2, all other components zero — fiber-closed
in the slice sense below. A slice point is (C, D), C ∈ R/17,
D ∈ R/1153, with t_i = Tr(C α^i) mod 17, s_i = Tr(D α^i) mod 1153,
i < 24, antiperiodic. The slice fiber key is the multiset of the
24 pairs (t_i, s_i) (== the global multiset of the slice point, by
CRT and injectivity of x ↦ p·x mod p^2). Class profile at a
component: 4 sorted 6-multisets of values at positions i ≡ r
(mod 4) — negation-symmetric triples {v, −v} from the first 12
positions. Π_q for a pair = {π ∈ D_4 : prof′[r] = prof[π(r)] ∀r}.

**Cell algorithm (exact, not sampled).** Fiber pairs must share
marginal multisets, so cells = (t-marginal group × s-marginal
group) are processed independently: 27 t-groups (sizes ≤ 16) ×
28,273 s-groups (sizes ≤ 48) = 763,371 cells. Inside a cell,
points are grouped by a 128-bit pair-multiset hash (sum of random
per-pair hashes over the 24 pairs), then hash groups are split by
exact sorted-pair keys — so hash collisions cannot merge distinct
fibers. Base-vs-other checks suffice by transitivity of the
common-π relation (π₂π₁⁻¹ carries other1 to other2).

## 3. Results (exact computation, C++, 4 threads, 4m41s)

- Slice points: 384,199,201 = 289 × 1153^2 (exact count matched).
- Fibers: 8,013,963; multi-point fibers: 8,013,962 (the single
  singleton is the zero point); fiber pairs checked: 376,185,238
  (= points − fibers, as required by base-vs-other counting).
- **Common-π failures: 0.** Every slice fiber pair has a common
  π ∈ D_4 at (289, 1153^2).

**Independent verification (separate Python code path).** Marginal
group counts match exactly (27 C-groups; 28,273 D-groups, max 48).
30 random cells re-checked by brute force in Python: 315 fibers,
14,781 pairs, 0 failures. The C++ t/s sequences match the Python
reference sequences at sampled (C, D).

## 4. What remains for full-space PC (named gap)

The slice common π must also lie in Π_q at 81, 25, 49, 121, 512.
Unlike m=18, Π_q is NOT full there: the fraction of kernel vectors
with all four class multisets equal is 49/49 at 49, but only 13/25
at 25, 1/81 at 81, 1/121 at 121, 4/512 at 512. So the wave-35 §4
lift ("fixed components are full") fails at m=24, and full-space
PC needs one further step: **compatibility** of the slice π with
the dihedral data at the other components (same kind of gap as
COH in wave 29, not a PC counterexample — none was found anywhere
in the slice). Note t = 4 here, so there is no a=b subcase as at
m=18; PC is the marginal G3 statement ∩_q Π_q ≠ ∅.

## Files

- This note: `methods/wave44_PC_m24.md`
- `methods/wave44_PC_m24.cpp` (exact checker), `methods/wave44_PC_m24.log`
  (POINTS 384199201, FIBERS 8013963, PAIRS 376185238, FAILURES 0)
- Prior: `methods/wave35_G2odd1.md`, `methods/wave35_G2odd1_m18.py`
  (m=18 method), `methods/wave12_g3_common_pi.md` (G3 definition)
