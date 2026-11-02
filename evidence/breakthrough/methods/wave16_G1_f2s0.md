# Wave 16, task 1 — the f=2 s=0 hole in G1: no instance below 2·10⁹

**Verdict: the hole is NOT closed, but its bound is extended 10⁴ → 2·10⁹
(200,000×), a new k≥2 prime is found, and the gap mechanism is pinned
down exactly at power-sum level.** Repository untouched, no Lean built.

## 0. The hole, restated

f=2, s=0 means k=2 (k = v_𝔭(α^{L₀}−1), L₀ = ord_p(α), α = 3+2√2).
Wave 14, §5: the f=2 s=0 proof has one narrow hole, needing k=2 AND
4 | L₀ (so g = gcd(L₀, t) = 4 with t = 4, α^{|H₀|} non-real mod p, and
the stabiliser argument bites). For any prime p with k=2, m = L₀ gives
an f=2 s=0 instance (v_p(D_{L₀}) = 2k = 4, s = v_p(m/L₀) = 0), so the
relevant primes are exactly the k=2 primes, and the hole is exactly
the question: does a k=2 prime with 4 | L₀ exist?

## 1. One-exponentiation test (e-test lemma, proved)

For odd p, let ε = (2/p) (±1 by p mod 8) and e = p − ε, the order of
the norm-1 group. Then α^e ≡ 1 (mod p²) ⟺ k ≥ 2.
Proof: e = L₀·q with L₀ ≥ 3 for odd p (α−1 = 2+2√2, α²−1 = 16+12√2,
so L₀=1 forces p|2, L₀=2 forces p|4), hence 1 ≤ q = e/L₀ ≤ (p+1)/3 < p
and p ∤ q. If k ≥ 2, α^e = (1+p^k u)^q ≡ 1 (mod p²). If k = 1,
α^e ≡ 1 + pqu (mod p²) with u a unit mod p, hence ≢ 1 (mod p²).

## 2. Validation below 10⁴ (exact, 0 mismatches)

Direct computation of L₀ (order reduction) and k (α^{L₀} mod p^t)
for all 1228 primes < 10⁴ agrees with the e-test everywhere.
k≥2 primes: exactly p=13 (L₀=14, k=2) and p=31 (L₀=15, k=2),
reproducing wave 14. Neither has 4 | L₀.

## 3. Search to 2·10⁹ (segmented sieve, __int128, 4 threads, 55 s)

98,222,286 primes tested, one e-test exponentiation each (p² ≤ 4·10¹⁸,
pair products ≤ 4.8·10³⁷ < 2¹²⁷, so __int128 is exact).
Candidates (k≥2 primes): only 13, 31, and one new prime:

| p | p mod 8 | L₀ | k | 4 \| L₀ |
|---|---|---|---|---|
| 13 | 5 | 14 | 2 | no |
| 31 | 7 | 15 | 2 | no |
| 1546463 | 7 | 773231 = (p−1)/2 | 2 | no (L₀ odd) |

**No prime below 2·10⁹ has k=2 and 4 | L₀.** The new prime 1546463
shows the search works: it is a genuine Wieferich-type prime for α,
but its L₀ is odd, so it is not a hole instance.

## 4. Why further search has poor returns (heuristic, not proof)

P(k≥2) ≈ 1/p per prime (α^e mod p² is 1+pw with w uniform over the
p purely-imaginary residues, since N(α^e)=1 forces Tr(w)=0), and
P(4|L₀) ≈ 0.32 independently (2-part of the order vs p-part growth).
Expected hole primes ≤ N: ≈ 0.32·(ln ln N + 0.26) ≈ 1.06 at 2·10⁹.
Finding 0 is a ~35% event, no contradiction; extending to 10¹⁰ would
add only ≈ 0.02 expected hole primes. No elementary obstruction to
(k=2, 4|L₀) was found: with 4 | L₀, k = v_p(s_{L₀/4}) has no forced
value, and α^{L₀/2} ≡ −1 (mod p²) holds at p=13 as expected.
So the hole stays open in principle; closing it needs either a prime
witness (a lottery) or a general twist lemma (§5).

## 5. Power-sum lemma: the gap is genuine, and exactly located

Let A be a unit mod p², B = A^{L₀}, and A′ = Aζ(1+pf) the twist of
wave-12 §7 (ζ ∈ G, f purely imaginary mod p, f ≠ 0 in the gap case).
Multiset equality mod p² forces, for every r ≥ 1,
S_r := Σ_{z∈G} Tr(Az)^{r−1}·Tr(Afz) ≡ 0 (mod p).
Lemma (proved by the binomial expansion + Σ_{z∈G} z^k = L₀·[L₀|k],
verified numerically at p=13 and p=31):
S_r = 0 for all 1 ≤ r < L₀, and S_{L₀} = L₀·f·(B−B̄).
Since L₀ ≢ 0 (mod p), S_{L₀} ≡ 0 ⟺ f = 0 or B real mod p.
So a nonzero twist is invisible to all power sums of order < L₀,
and the first constraint is exactly the gap condition (B real mod p).
A proof closing the hole must therefore use power sums of order
> L₀ or direct multiset comparison; low power sums cannot do it.
(Caution: an earlier draft of this lemma dropped the factor L₀ and
failed numerically at p=31, A=1+√2: S₁₅ = 23 = 15·16, not 16.)

## 6. What remains for G1

- The f=2 s=0 hole: open, no instance below 2·10⁹ (this note).
- G1 at f≥3: (1,2) closed by S\*=0 (wave 15); (2,1) modulo this hole;
  (3,0) absent below 10⁴.
- G3 (general Lemma PC) and Lean formalisation: untouched here.

## Files

- This note: wave16_G1_f2s0.md
- Search program (C++): wave16_search.cpp (validate + scan modes)
