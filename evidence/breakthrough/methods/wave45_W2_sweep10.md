# Wave 45, task 7 — W₂ verification extended to 10¹⁰

## 0. Definitions (waves 38/40)

R = ℤ[√2], α = 3+2√2, p odd. d = ord_p(α), e = v_p(α^d − 1) ≥ 1.
d | N where N = p − (2/p): p−1 if p ≡ ±1 mod 8 (split), p+1 if
p ≡ ±3 mod 8 (inert). W₂ is the hypothesis e(p) ≤ 2 for all p;
wave 40 verified it to 10⁹ with e = 2 only at p = 13, 31, 1546463.
N(b) ≤ 2m^{2e(p)} in the tower regime, so W₂ ⟹ N(b) ≤ 2m⁴.

## 1. Method

C++ sweep (`wave45_W2_sweep10.cpp`): segmented odd-only sieve
(2²⁶ odds per segment, no 5 GB table), 4 threads over contiguous
ranges; d by reducing N with trial-division factors (order test
in (R/pR)^×, `__int128` products); e ≥ 2 test α^d ≡ 1 mod p².
Every e ≥ 2 candidate is re-checked exactly in Python big
integers (`wave40_W2_verify.py`: independent order computation
plus α^d mod p^k).

Mod-p² arithmetic uses the base-p representation, never storing
p² in u64: an element of R/p²R is (a0 + b0√2) + p(a1 + b1√2)
with all components mod p (fit u64 for p ≤ 10¹⁰), and
(A + pB)(C + pD) = AC + p(AD + BC) mod p², where AC is taken
mod p² exactly in u128 (its base-p high digit folds into the
p-part) and AD, BC only mod p. α in base p is (3%p, 2%p) plus
p-part ((3−3%p)/p, (2−2%p)/p) — the p-part is (1, 0) at p = 3.

## 2. Bug history — the first decade run was invalid, discarded

Three bugs were found and fixed before any result was claimed;
none of them survives in the final code or numbers below.

1. **u64 p² overflow (fatal to run 1).** The first version formed
   p2 = p·p in u64. For p > 2³² ≈ 4.295×10⁹, p² exceeds u64 max
   (1.845×10¹⁹) and wraps, so every e-test above 2³² ran against
   a wrong modulus. It reported one "hit", p = 4318272001,
   d = 539784000 — the Python verifier refuted it (exact e = 1),
   and a targeted fixed-code run over its neighborhood finds
   0 hits. That whole run was discarded; only its thread-0
   range [10⁹, 3.25×10⁹), entirely below 2³², was valid, and the
   rerun reproduces its count exactly (105,036,713 primes).
2. **AC-mod-p error (caught by selftest).** The first base-p
   version reduced AC mod p instead of mod p², losing AC's
   base-p high digit. The selftest (200k random mul/sqr/pow
   comparisons against plain mod-p² arithmetic) caught it
   immediately; the fix takes AC mod p² exactly in u128.
3. **p = 3 base error (caught by the 10⁸ validation).** The base
   was written with zero p-part, but α at p = 3 is
   (0 + 2√2) + 3(1 + 0√2); the zero version gives (2√2)⁴ = 64
   ≡ 1 mod 9, a false positive at p = 3. Fixed with the general
   base formula above, and the selftest now includes
   deterministic small-p pow checks (p = 3, 5, 7, 13, 17).

## 3. Validation (all with the final code unless noted)

- `--selftest`: PASS (200k random mul/sqr/pow vs plain mod-p²
  for p ≤ 10⁹, plus deterministic small-p pow checks).
- 10⁸ reproduction: exactly 13, 31, 1546463; 5,761,454 primes
  (matches wave 40's 10⁸ row).
- 10⁹ reproduction (with the pre-rewrite split-mult code, whose
  only flaw was the u64 p² overflow, inactive for p ≤ 10⁹):
  exactly 13 (d = 14), 31 (d = 15), 1546463 (d = 773231);
  50,847,533 primes (matches wave 40).
- Prime-count cross-check for the decade: 404,204,977 +
  50,847,533 = 455,052,510 = π(10¹⁰) − 1 (excluding prime 2),
  so the sieve missed no primes; per-thread counts match the
  discarded run exactly (same sieve, only the e-test changed).

## 4. Result: W₂ verified to 10¹⁰, no new e = 2 prime

| range | primes scanned | e ≥ 2 primes (exact e) |
| 10⁹ (wave 40) | 50,847,533 | 13, 31, 1546463 (all e = 2) |
| [10⁹, 10¹⁰) | 404,204,977 | none |
| ≤ 10¹⁰ total | 455,052,510 | 13, 31, 1546463 (all e = 2) |

Per-thread decade counts: [10⁹, 3.25×10⁹): 105,036,713, 0;
[3.25, 5.5)×10⁹: 101,410,273, 0; [5.5, 7.75)×10⁹: 99,516,298, 0;
[7.75, 10)×10⁹: 98,241,693, 0. No prime with e ≥ 3 anywhere
≤ 10¹⁰. Decade rerun wall time 48.3 min (4 threads, shared VM).

## 5. Consequence

For m ≤ 10¹⁰, W₂ is now a verified fact, not a hypothesis:
every p | m has e(p) ≤ 2, so N(b) ≤ 2m⁴ unconditionally in
that range, and SC(11) holds for m ≤ 10¹⁰. Beyond 10¹⁰, N(b)
≤ 2m⁴ (and SC(11)) still rest on W₂. The extension does not
settle boundedness of e(p).

## 6. Heuristic consistency

Expected e ≥ 2 count up to X is Σ_{p≤X} 1/p ≈ ln ln X + 0.261:
≈ 3.40 at 10¹⁰ vs 3 found — consistent (the decade added
≈ 0.11 expected, found 0). Expected e ≥ 3 count is Σ_p 1/p²
≈ 0.452 in total, essentially all of it below 10⁸, so finding
no e ≥ 3 prime up to 10¹⁰ is unsurprising and says little
about whether one exists at all.

## 7. Limits

Odd p only (2-part separate). W₂ beyond 10¹⁰ open; a further
decade (10¹¹) would need ~8× the decade CPU (~6–7 core-hours)
and a p² representation already safe to 10²⁰ in u128, so the
code scales, but the sieve/order cost grows. No theoretical
restriction ruling out e ≥ 3 is known (base-2 Wieferich
primes 1093, 3511 show such primes can exist); proving e(p)
bounded remains an open Wieferich-type problem. No Lean built;
repository untouched.
