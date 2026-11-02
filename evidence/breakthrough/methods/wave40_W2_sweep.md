# Wave 40, task 4 — W₂ verification extended to 10⁹

## 0. Definitions (wave 38, task 1)

R = ℤ[√2], α = 3+2√2, p odd. d = ord_p(α), e = v_p(α^d − 1) ≥ 1.
d | N where N = p − (2/p): p−1 if p ≡ ±1 mod 8 (split), p+1 if
p ≡ ±3 mod 8 (inert). W₂ is the hypothesis e(p) ≤ 2 for all p;
wave 38 verified it to 10⁵ with e = 2 only at p = 13, 31.
N(b) ≤ 2m^{2e(p)} in the tower regime, so W₂ ⟹ N(b) ≤ 2m⁴.

## 1. Method

C++ sweep (`wave40_W2_sweep.cpp`): odd-only Eratosthenes sieve,
d by reducing N with trial-division factors (order test in
(R/pR)^×), then the e ≥ 2 test α^d ≡ 1 mod p². Exact `__int128`
arithmetic (p ≤ 10⁹ ⟹ p² ≤ 10¹⁸, products ≤ 2·10³⁶ < 2¹²⁷).
Every e ≥ 2 candidate is re-checked exactly in Python big
integers (`wave40_W2_verify.py`: independent order computation
plus α^d mod p^k for k = 1, 2, 3, …), since p³ arithmetic
overflows `__int128` for p > 10⁶.

## 2. Result: W₂ verified to 10⁹, one new e = 2 prime

| range | primes scanned | e ≥ 2 primes (exact e) |
| 10⁵ (wave 38) | — | 13, 31 (both e = 2) |
| 10⁶ | 78,497 | 13, 31 |
| 10⁸ | 5,761,454 | 13, 31, 1546463 |
| 10⁹ | 50,847,533 | 13, 31, 1546463 (no new) |

New prime p = 1546463: split (≡ 7 mod 8), N = 2 × 773231 with
773231 prime, d = 773231 = N/2 exactly, and α^d ≡ 1 mod p² but
≢ 1 mod p³, so exact e = 2. No prime with e ≥ 3 up to 10⁹.
Runtimes: 10⁸ in 18 s, 10⁹ in 4 m 05 s.

## 3. Consequence

For m ≤ 10⁹, W₂ is now a verified fact, not a hypothesis: every
p | m has e(p) ≤ 2, so N(b) ≤ 2m⁴ unconditionally in that
range. Beyond 10⁹, N(b) ≤ 2m⁴ (and SC(11)) still rest on W₂.
The extension does not settle boundedness of e(p).

## 4. Heuristic consistency

Expected e ≥ 2 count up to X is Σ_{p≤X} 1/p ≈ log log X + M:
≈ 3.29 at 10⁹ vs 3 found — spot on. Expected e ≥ 3 count is
Σ_p 1/p² ≈ 0.452 in total, with only ~5×10⁻¹⁰ of it beyond
10⁸, so finding no e ≥ 3 prime up to 10⁹ is unsurprising and
says little about whether one exists at all.

## 5. No theoretical restriction known

No theorem rules out e ≥ 3. Analogy: base-2 Wieferich primes
1093, 3511 exist (a² ≡ 1 mod p² with a = 2), so α-Wieferich
primes of order ≥ 3 may exist; the Σ 1/p² heuristic says
only finitely many are expected, possibly zero. Proving e(p)
bounded remains an open Wieferich-type problem.

## 6. Validation

- Independent Python big-int implementation agrees with C++ on
  all p ≤ 10⁴ (d and exact e), including wave-38 table values
  (3→d4/e1, 5→d6/e1, 7→d3/e1, 13→d14/e2, 17→d8/e1).
- A refactor bug (factor 2 dropped from trial division, giving
  d = 30 instead of 15 at p = 31) was caught by that cross-check
  and fixed; e ≥ 2 detection was provably unaffected (if d′ is
  a multiple of d with p ∤ d′/d, then α^{d′} ≡ 1 mod p² ⟺
  α^d ≡ 1 mod p²), and fixed-code reruns reproduce every
  result exactly.

## 7. Limits

Odd p only (2-part separate). W₂ beyond 10⁹ open; a further
decade (10¹⁰) would need ~40 min and ~5 GB sieve, not attempted.
No Lean built; repository untouched.
