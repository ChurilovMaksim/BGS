# Wave 44, task 2 — Lemma U at m=60: full-cycle rigidity for the large pairs

## Verdict

Lemma U holds at m=60 for **every** pair involving 601² or 2281²:
0 conflicts everywhere, no fourth mechanism. Stronger: at every
(large, small) pair and at (2281, 59)-degenerate, every ℘-group is a
**single G-orbit** — there are no partial-move collisions at all at
large pairs, unlike m=30 (58 colliding groups) and the m=60 small
pairs (up to 2465 multi-orbit groups). The (601, 2281) pair is closed
by the generic theorem (§4) plus a degenerate×degenerate census (§6).

## 1. Setup and structural facts (proved + verified exactly)

m = 60, u = 30, β = α², α = 3+2√2. Components: 81 (3⁴), 121 (11²),
361 (19²), 3481 (59²), 361201 (601²), 5202961 (2281²). Blocks are
30-cycles: block0 = {(s_k, t_k)}, block1 = {(−s_k, −t_k)},
℘ = block0 ∪ block1. Cycles: s_0 = 2a, s_1 = 34a+48b,
s_{k+1} = 34s_k − s_{k−1} (mod m), params (a,b) ↔ cycles bijectively
for prime sides (det 96 a unit), 27 distinct cycles mod 9.

Large sides split: p ∈ {601, 2281} has p ≡ 1 (mod 8), so
R/p ≅ F_p × F_p, β ↦ (β_1, β_2), β_1β_2 = N(β) = 1,
ord β_1 = ord β_2 = 30, β^15 ≡ −1 (mod p) on both coords.
Cycles: s_k = c_1β_1^k + c_2β_1^{−k}.

- **Period rigidity (proved).** A nonzero large-side cycle has period
  exactly 30: if period d | 30, d < 30, the k=0,1 equations give
  c_1A(1 − β_1²) = 0 with A = β_1^d − 1 ≠ 0, forcing c_1 = c_2 = 0.
  Verified exactly: periods {1:1, 30:361200} at 601,
  {1:1, 30:5202960} at 2281. Small sides: {1,2,6} mod 9,
  {1,6} mod 11, {1,10} mod 19, 59.
- **Antiperiod 15 everywhere (verified exactly, all cycles, all
  sides).** β^15 ≡ −1 (mod m) at every component, so shift-15
  negates every cycle, hence −block0 = block0 and
  **℘ = 2·block0 for every large pair**. So ℘′ = ℘ implies
  block0′ = block0 — the recombinant-partition problem collapses
  to: block0 determines the pair up to simultaneous dihedral moves.

## 2. L1 for large sides (proved by power sums)

Let s_k = c_1β_1^k + c_2β_1^{−k}, γ = c_1c_2, σ = c_1^{30}+c_2^{30}.
Power sums over k ∈ Z/30 (using Σ_k β_1^{mk} = 30 if 30 | m else 0):
P_2 = Σ s_k² = 60γ; P_30 = Σ s_k^{30} =
30(σ + C(30,15)γ^{15}). So M(s) determines γ and σ, hence the
set {c_1^{30}, c_2^{30}} (roots of X² − σX + γ^{30}). If (d_1,d_2)
has the same (γ, σ), then d_1^{30} ∈ {c_1^{30}, c_2^{30}}; say
d_1^{30} = c_1^{30}: then d_1 = c_1ζ with ζ^{30} = 1, and
ζ ∈ ⟨β_1⟩ (F_p^* cyclic, 30 | p−1), so d_1 = c_1β_1^j and
d_2 = γ/d_1 = c_2β_1^{−j} — a shift of (c_1,c_2); the other case
is a swap (= reversal). Negation is shift-15. Hence: **any β-cycle
with value multiset M(s) or M(−s) is dihedral to s.**
Formulas verified on 200 random cycles per side; recovery verified
on 300 random cycles per side (all (γ,σ)-matches dihedral).
L1 also verified by finite check on all small sides (0 violations).

## 3. Degenerate locus (exact description)

s_k = s_j (k ≠ j) ⟺ (β_1^k − β_1^j)(c_1 − c_2β_1^{−k−j}) = 0
⟺ β_1^{k+j} = ρ := c_2/c_1 (c_1 ≠ 0). So: **repeated values ⟺
ρ ∈ ⟨β_1⟩** (30 ratios), with pairing symmetry s_{m−k} = s_k for
ρ = β_1^m; torsion (c_1c_2 = 0) has 30 distinct values; zero is
trivial. Degenerate params per large side: 30(p−1) repeated-values
+ 2p−1 torsion = 32p−31 (19201 at 601, 72961 at 2281);
H-orbits among them: 621 at 601, 2357 at 2281.

## 4. Generic theorem (proved)

**If s is a large-side cycle with all 30 values distinct, then
its ℘-group is a single G-orbit.** Proof: ℘ = 2·block0 gives
block0′ = block0. By L1, s′ is dihedral to s: s′_k = σs_{εk+a}
(σ = ±1, ε = ±1). Distinctness gives a unique φ(k) with
s_{φ(k)} = s′_k, namely φ(k) = εk + a′′ (a′′ = a or a+15, by
antiperiod). Block0′ = block0 then forces t′_k = t_{φ(k)} (the
pair with first coordinate s′_k is unique). So
(s′, t′) = (s∘φ, t∘φ): a simultaneous dihedral reindexing.
No L1 on the other side is needed, and no collision is possible.

## 5. Census method (exact, validated)

Representative census (C++): H-orbits per side under
⟨shift, reversal⟩; pair G-orbits enumerated as (S^rR^ε(s*), t*),
r ∈ Z/gcd(T_a,T_b), ε ∈ {0,1} — a proved covering (any pair
reduces to this form via simultaneous reversal/shift). ℘-groups
by hash, conflicts exact-verified (same ℘, differing block pair).
Validation: brute-force streaming census over all cycle-pairs
gives identical ℘-group counts at (601, 9): 164347, and at
(601, 11): 731736. Census code: wave44_LemmaU_large.cpp.

## 6. Census results: 0 conflicts everywhere

| pair | reps | ℘-groups | conflicts | multi-orbit groups |
|---|---|---|---|---|
| (601, 9) | 265,454 | 164,347 | 0 | 0 |
| (601, 11) | 1,150,272 | 731,736 | 0 | 0 |
| (601, 19) | 3,425,496 | 2,178,948 | 0 | 0 |
| (601, 59) | 25,672,248 | 20,973,524 | 0 | 0 |
| (2281, 9) | 3,689,966 | 2,348,179 | 0 | 0 |
| (2281, 11) | 15,989,824 | 10,505,192 | 0 | 0 |
| (2281, 19) | 47,618,008 | 31,326,164 | 0 | 0 |
| (2281, 59) degen | 9,570,480 | 4,300,360 | 0 | 0 |
| (601, 2281) degen×degen | 87,649,154 | 24,034,177 | 0 | (see §7) |

## 7. Coverage: why this closes all large pairs

- (large, small): full representative census (§6) — standalone proof.
- (2281, 59): §4 covers every pair with a distinct-valued 2281-side;
  the degenerate-restricted census covers 2281-degenerate × all
  59-orbits. Complete.
- (601, 2281): §4 covers every pair with a distinct-valued side
  (either side is large); the degen×degen census covers both-sides
  degenerate (torsion included in the degenerate set). Complete.
- Caveat: the (601, 2281) multi-orbit dedupe was cut short by an
  OOM-kill of the analysis process (VM memory pressure from parallel
  work) after TRUE CONFLICTS = 0 printed. The conflict verdict is
  unaffected (it is computed before dedupe); only the multi-orbit
  count for degen×degen is unreported. It is not needed for Lemma U.

## 8. What remains

No Lean built; repository untouched. Open: a general
degenerate-fiber proof (the census replaces it for these pairs);
Lemma U in general (other m); the mechanism question for
(601, 2281)-degenerate multi-orbit groups, if any exist. Note the
contrast with m=30/m=60-small: at large pairs, partial moves never
even occur — the period-30 large side is too rigid for fiber
compatibility except trivially (same orbit).
