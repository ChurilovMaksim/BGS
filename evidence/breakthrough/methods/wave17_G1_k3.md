# Wave 17, task 3 — G1 case (3,0): does k ≥ 3 occur?

**Verdict: no k ≥ 3 prime below 2·10⁹, so case (3,0) is vacuous below
2·10⁹. Globally it is probably vacuous (expected total ≈ 0.45 such
primes), but that is heuristic, not proof — same status as Wieferich
primes. No elementary obstruction to k ≥ 3 was found.**
Repository untouched, no Lean built.

## 0. What (3,0) needs

p odd, L₀ = ord_p(α), α = 3+2√2, k = v_𝔭(α^{L₀}−1), s = v_p(m/L₀),
f = k+s. Case (3,0) at f = 3 means k = 3, s = 0. For any prime with
k = 3, m = L₀ gives s = 0 and v_p(D_m) = 2k = 6, i.e. a genuine (3,0)
instance. Conversely a (3,0) instance needs a k = 3 prime. So (3,0)
is vacuous iff no prime has k = 3.

## 1. The mod-p^t e-test (proved, generalising wave 16)

Let ε = (2/p) and e = p − ε, the order of the norm-1 group in R/p
(split: p−1, inert: p+1; α has norm 1, so α^e ≡ 1 mod p and L₀ | e).

**Theorem.** For odd p and every t ≥ 1: α^e ≡ 1 (mod p^t) ⟺ k ≥ t.

*Proof.* L₀ ≥ 3 for odd p (α−1 = 2+2√2 forces p | 2 if L₀ = 1;
α²−1 = 16+12√2 forces p | 4 if L₀ = 2), so q = e/L₀ ≤ (p+1)/3 < p
and p ∤ q. Write α^{L₀} = 1 + p^k·u with u a unit at 𝔭 (purely
imaginary mod p: ū ≡ −β^{L₀}u ≡ −u mod p, so u ≡ c√2, c ≢ 0 mod p).
Then α^e = (1 + p^k u)^q = 1 + q·p^k·u + Σ_{j≥2} C(q,j)·p^{jk}·u^j.
The j = 1 term has valuation exactly k (q, u units); every j ≥ 2
term has valuation ≥ 2k ≥ k+1. So v_𝔭(α^e − 1) = k exactly, hence
α^e ≡ 1 mod p^t iff k ≥ t. ∎

The t = 3 instance is the test asked for: α^e ≡ 1 (mod p³) ⟺ k ≥ 3.
Note the efficient pipeline this implies: k ≥ 3 ⇒ k ≥ 2, so to find
k ≥ 3 primes one sieves k ≥ 2 with the cheap mod-p² test and only
then runs the mod-p³ check on candidates — a direct mod-p³ sieve
past ~2·10⁶ needs multiprecision (products (p³)² exceed __int128
range) and is unnecessary for the bound.

## 2. Verification (exact arithmetic)

- **Python cross-check, p < 10000:** direct L₀ (order reduction) and
  k (α^{L₀} mod p^t) vs the mod-p³ e-test: **0 mismatches, no k ≥ 3
  prime.** Script: `wave17_G1_k3_check.py`.
- **C++ mod-p³ scan to 2·10⁶** (unsigned __int128, per-term reduction):
  148,932 odd primes (= π(2·10⁶) − 1, sieve count consistent),
  k ≥ 2 primes exactly {13, 31, 1546463}, **k ≥ 3 primes: 0.**
  Program: `wave17_G1_k3_scan.cpp`.

## 3. The bound to 2·10⁹

Wave 16's scan enumerated **all** k ≥ 2 primes below 2·10⁹ via the
mod-p² e-test (its prime count 98,222,286 = π(2·10⁹) − 1, and my
independent pipeline reproduces its k ≥ 2 list exactly below 2·10⁶).
Exact k for the three candidates, computed here (α^{L₀} mod p³):

| p | p mod 8 | e | L₀ | q = e/L₀ | 4 \| L₀ | α^{L₀} mod p² | mod p³ | k |
|---|---|---|---|---|---|---|---|---|
| 13 | 5 | 14 | 14 | 1 | no | 1 | ≠ 1 | 2 |
| 31 | 7 | 30 | 15 | 2 | no | 1 | ≠ 1 | 2 |
| 1546463 | 7 | 1546462 | 773231 | 2 | no | 1 | ≠ 1 | 2 |

Hence **no prime below 2·10⁹ has k ≥ 3, in particular none has
k = 3, so case (3,0) has no instance with p < 2·10⁹.** The same
argument kills every k ≥ 3 case (k,s) with p < 2·10⁹, not just
(3,0); G1 instances with p ≥ 2·10⁹ are untouched by this bound.
(Caveat: the 2·10⁹ step relies on wave 16's scan completeness; it
was not re-run here, only cross-validated below 2·10⁶ and by its
prime count.)

## 4. Global heuristic: (3,0) is probably vacuous, unprovably

Given k ≥ 2, the next digit of α^e is uniform over p values, so
P(k ≥ 3) ≈ 1/p² per prime. Expected total number of k ≥ 3 primes
over all primes: Σ_p 1/p² = P(2) ≈ 0.452247 (partial sum to 10⁶
already 0.452247; tail < 10⁻⁶). So zero k ≥ 3 primes is the likeliest
outcome, but ≈ 0.45 expected means existence cannot be excluded by
heuristics either — exactly the Wieferich situation (base 2 has two
known examples, 1093 and 3511). A proof of impossibility would need
a new obstruction; none is visible: with k = 3, no congruence forces
a contradiction (contrast: L₀ ≥ 3 was forced, k itself is not).

## 5. What remains for G1

- (3,0): settled below 2·10⁹; globally open, probably vacuous.
- f = 2 s = 0 hole (k = 2, 4 | L₀): also no instance below 2·10⁹
  (wave 16); same Wieferich-type status.
- f ≥ 4: needs k ≥ 3 or larger s; the k ≥ 3 part is bounded as above.
- General PC and Lean formalisation: untouched here.
- To extend the bound: extend the k ≥ 2 sieve (mod-p² test) past
  2·10⁹ and mod-p³-check any new candidates. Poor returns: expected
  new k ≥ 2 primes to 10¹⁰ ≈ 0.07, new k ≥ 3 far fewer.

## Files

- This note: `wave17_G1_k3.md`
- Python check: `wave17_G1_k3_check.py`
- C++ scan: `wave17_G1_k3_scan.cpp`
