# Wave 32, task 3 — RB3: count PROVED, size ≤ 2 REFUTED, repair RB3′

Verdict: RB3 as stated in wave 23 is half true. The count clause is
proved (with a tight bound); the size clause "each of size ≤ 2" is
false, and so is the wave-23 fallback "the trivial single-orbit bound
2m". The Δ → 0 conditional theorem survives via the repair RB3′,
with worse polynomial exponents only. Repository untouched, no Lean.

## 0. Definitions (wave-16/20 code, used exactly)

- q₂ = 2-part of D_m. Kernel points mod q₂: Fix sequences
  y_{i+1} = 6y_i − y_{i−1} mod q₂, m-periodic; exactly q₂ of them
  (SNF of M^m − I, M = [[6,−1],[1,0]]; see §1).
- Fiber: equal sorted multiset of coordinates. Support: the torsion
  criterion 2Q(z) − y·z ≡ 0 (mod q₂) for all z ∈ Z (the mod-4 torsion
  sequences; |Z| = 16 if 4 | m, 8 if m ≡ 2 mod 4, 4 if m odd).
- Supported 2-fiber: a q₂-fiber containing ≥ 1 supported point.
  (Empirically support is constant on 2-fibers — 0 partial fibers
  for all m ≤ 128 — so "meeting support" = "fully supported" in range.)

## 1. Count clause: PROVED — #supported 2-fibers ≤ q₂ ≤ 8m²

(a) |ker mod q₂| = q₂. SNF of M^m − I over ℤ is diag(d₁, d₂) with
d₁d₂ = |det(M^m − I)| = D_m. Then |ker mod 2^e| =
gcd(d₁, 2^e)·gcd(d₂, 2^e) = 2^{min(v₂(d₁),e)+min(v₂(d₂),e)} = 2^e,
since v₂(d₁) + v₂(d₂) = v₂(D_m) = e and each v₂(dᵢ) ≤ e.
(b) Fibers partition the q₂ points, so #fibers ≤ q₂, hence
#supported fibers ≤ q₂.
(c) q₂ ≤ 8m² by the wave-11 2-adic LTE (proved): v₂(D_m) = 2 if m
odd, 2v₂(m)+3 if v₂(m) ≥ 1. If m odd, q₂ = 4 ≤ 8m². If
v₂(m) = k ≥ 1, q₂ = 2^{2k+3} = 8·4^k ≤ 8m² since m ≥ 2^k.
The bound is tight: at m = 2^k, q₂ = 8m² exactly (m = 128:
q₂ = 131072 = 8·128²). Verified computationally: 0 violations
for m ≤ 128; in fact #supported fibers is far below q₂
(m = 128: 278 supported fibers vs q₂ = 131072).

## 2. Size clause "≤ 2": REFUTED — explicit counterexample at m = 16

At m = 16, q₂ = 2048, the fiber with sorted multiset
{0,512,1024,1536} × 4 each contains exactly 8 supported points:
the dihedral orbit of the 4-pattern (0,512,1024,1536) repeated 4
times — 4 rotations and 4 reflections, e.g.
[0,512,1024,1536]×4, [512,1024,1536,0]×4, [0,1536,1024,512]×4.
Completeness is by full enumeration over all 2048 kernel points;
all 8 points satisfy the support criterion. So a supported
2-fiber of size 8 exists, and it is a single Γ-orbit — the
single-orbit reading does not save the clause either.
Wave 23's "observed sizes 1–2" came from q₂ = 128, 512 only
(m = 12, 24, 36, 40); the clause already fails at the next
2-power, m = 16 (sizes there: 1×4, 2×14, 4×18, 8×3).

## 3. Fallback "size ≤ 2m": REFUTED at m = 128

Max supported 2-fiber size by v₂(m), exact for m ≤ 128:
v₂: 0→1, 1→2, 2→2, 3→2, 4→8, 5→32, 6→128, 7→512.
At m = 128 (v₂ = 7) a supported fiber has 512 points > 2m = 256.
Moreover supported fibers need not be single orbits: at m = 64,
10 supported fibers are multi-orbit, e.g. size 128 with 4 orbits —
so no orbit-size argument can bound supported fibers by 2m.

## 4. Repair RB3′ (proved) and salvaged Δ → 0

RB3′: (i) #supported 2-fibers ≤ q₂ ≤ 8m² (proved, §1);
(ii) each supported 2-fiber has size ≤ q₂ ≤ 8m² (trivial:
a fiber is a subset of the q₂ kernel points).
In wave 23's master inequality, with RB1′/RB2 as before
(N(m) ≤ 16m² using ≤ 2 split 3-fibers, M(m) ≤ 4m² × 8m²
= 32m⁴), ΣΔ_F ≤ 16m²·(32m⁴)² = 16384·m¹⁰, hence
Δ(m) ≤ 16·16384·m¹⁰/(ρ^m − 2) → 0 with ρ = 3+2√2.
RB3's false clause was never load-bearing: polynomiality is
all the application needs, and RB3′ supplies it.

## 5. Empirical sharp law (conjecture, verified m ≤ 128)

Max supported 2-fiber size = 2^{2v₂(m)−5} for v₂(m) ≥ 4,
and ≤ 2 for v₂(m) ≤ 3 — exact at every m ≤ 128, including
v₂ = 7 (m = 128: 512). Side facts, same range: #supported
points = q₂/|Z| exactly (m = 128: 8192 = 131072/16);
support constant on 2-fibers (0 partial). Proving the sharp
law is now the named open lemma RB3-size; it needs a genuine
2-adic analysis of supported sequences (their high 2-adic
depth and short periods, cf. the 4-periodic m = 16 fiber),
not a counting argument. It is NOT needed for Δ → 0.

## Files

- `wave32_RB3_check.py` (ALL CHECKS PASS: sweep m ≤ 128 plus the
  explicit m = 16 fiber, reproduced above).
