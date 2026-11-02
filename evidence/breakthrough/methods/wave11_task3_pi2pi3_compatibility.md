# Wave 11, task 3 — π₂ = π₃ compatibility for mod-D Lemma Y

## Status in one paragraph

**No mixed counterexample exists at mod-D level for any global fiber pair,
conditional on two explicitly named inputs: (A) the per-class pattern lemma
(Wave 10: per-class multisets of 2-patterns are D₄-related; verified for
P ≤ 32, unproved in general) and (B) the stabilizer-adjustment lemma S below
(verified for all Fix patterns at P = 8 and P = 16, 86 000 cases, 0 failures;
S is NOT a pure D₄ lemma — §5 gives an explicit arbitrary-multiset
counterexample — so S itself needs Fix-pattern structure and is open in
general).** Under (A) and (B), every global fiber pair
y′ = σ(y) admits a single π ∈ D₄ with Y′ ≡ π(Y) (mod D): the 2-component
and the 3-component are simultaneously matched by π. Hence Pmix is closed
at mod-D level in general, modulo (A) and (B). This is **not** exact Lemma Y:
lifting from mod D to exact integer class sums (Pcarry) remains separate,
and (A) itself remains the main open input.

The LTE input v₂(D_m) is proved in full in the companion note
`wave11_task3_LTE_v2Dm.md` (ℤ[√2] valuation, checked for m = 1..30).

## Setup (4 ∣ m; other m are vacuous)

Assume 4 ∣ m, so t = gcd(m, 4) = 4 and D₄ acts on the four class indices
r ∈ ℤ/4. The 3-component exists only when 4 ∣ m (q = 3^e, e = 2f₀,
f₀ = 1 + v₃(m/4)); for 4 ∤ m there is no 3-component to match, and
compatibility is vacuous. Odd prime powers q ≠ 3 give Y ≡ 0 (mod q)
(Wave-8 vanishing lemma), so Π_q is unconstrained there. The only
non-trivial components are q = 2^a and q = 3^e.

- a = v₂(D_m) = 2·v₂(m) + 3 (LTE note). P = 2^{v₂(m)} ≥ 4.
  Every Fix vector mod 2^a is P-periodic (Wave-9 §5); its length-P
  pattern is p ∈ Fix_P mod 2^a. Class sums:
  Y_r mod 2^a = (m/P)·S_r(p), S_r(p) = Σ_{j ≡ r (4)} p_j,
  with m/P odd (a unit mod 2^a). So class sums mod 2^a are
  determined by pattern class sums, and vice versa.
- 3-component: every Fix vector mod 3^e is divisible by 3^{f₀};
  after scaling, Y mod 3^e = 3^{e−1}·n₀·v (mod 3^e) with
  v = (a, b, −a, −b) ∈ 𝔽₃⁴ the mod-3 4-vector, n₀ a unit mod 3
  (Wave-9 P3′). Lemma 6 classifies v into 3 types, and v is
  determined by its mod-3 multiset up to D₄. Hence
  Π₃ = {π ∈ D₄ : v′_r = v_{π(r)} ∀r} = {π : π(r) ∈ F_r ∀r},
  where F_r = {s : v_s = v′_r} is the v-fiber over v′_r.
  Fiber blocks of v: all-zero → one block of size 4;
  one-zero type (e.g. v = (0,1,0,2)) → blocks {0,2}, {1}, {3};
  both-nonzero type (e.g. v = (1,1,2,2) or (1,2,2,1)) → two
  adjacent pairs of size 2.
- Per-class multisets: M_r = multiset of p_j for j ≡ r (mod 4),
  M′_r likewise for p′. Pattern lemma (A): there exists
  π₂ ∈ D₄ with M′_r = M_{π₂(r)} for all r. In particular
  S′_r = S_{π₂(r)}.
- Π₂ (multiset version) = {π ∈ D₄ : M′_r = M_{π(r)} ∀r}.
  Goal: Π₂ ∩ Π₃ ≠ ∅. Then for π in the intersection,
  Y′₂ ≡ π(Y₂) (mod 2^a) (by summing multisets and multiplying
  by the unit m/P) and Y′₃ ≡ π(Y₃) (mod 3^e) (by the v-formula),
  hence Y′ ≡ π(Y) (mod D) by CRT (other components vanish).

## Step 1: a bijective τ′ matching joint values (from σ)

Let y′ = σ(y) with σ ∈ S_m a global permutation (same σ for all
components). Define joint values on pattern positions k ∈ ℤ/P by
J(k) = (p_k, v_{k mod 4}), J′(k) = (p′_k, v′_{k mod 4}).

Claim: there is a bijection τ′ : ℤ/P → ℤ/P with J′(k) = J(τ′(k))
for all k. Proof by counting with multiplicity m/P:
- Mod 2^a: y′_i mod 2^a = p′_{i mod P} and
  y_{σ(i)} mod 2^a = p_{σ(i) mod P}; since y′_i = y_{σ(i)},
  p′_{i mod P} = p_{σ(i) mod P} for all i ∈ ℤ/m.
- Mod 3^{f₀+1} (scaled): v′_{i mod 4} = v_{σ(i) mod 4} for all i.
- Hence for every i, J′(i mod P, i mod 4) = J(σ(i) mod P, σ(i) mod 4)
  in the sense of pairs. Now each pair (k, r) with r ≡ k (mod 4)
  occurs exactly m/P times as (i mod P, i mod 4) when i ranges
  over ℤ/m (P is divisible by 4, so lcm(P, 4) = P; incompatible
  pairs occur 0 times). Therefore the multiset of J′ over i ∈ ℤ/m
  is (m/P) copies of the multiset of J′(k) over k ∈ ℤ/P, and
  likewise for J. Since σ is a bijection, the multisets over i
  coincide; dividing by the multiplicity m/P, the multisets of
  J′(k) and J(k) over k ∈ ℤ/P coincide. A bijection τ′ with
  J′ = J ∘ τ′ follows.

Note: τ′ is **not** σ mod P (σ need not be P-periodic); it is the
bijection obtained from the joint-value multiset equality. The
bijectivity of τ′ is essential: a per-k (non-injective) matching
does **not** imply compatibility — an abstract counterexample with
p = (32,32,160,416,288,288,416,160),
p′ = (32,160,416,288,288,416,160,32), v = v′ = (1,2,2,1) has
Π_pattern ∩ Π_v = ∅ but only a non-bijective per-k matching
(Kuhn adjacency lists [[0],[2],[6],[4],[4],[6],[2],[0]] collide).
Requiring τ′ bijective excludes it (script
`wave11_task3_explore2.py`: P = 8, 5660 pattern pairs, 0 bijective-τ
counterexamples; `wave11_task3_explore3.py`: P = 16, 1 712 528
τ-checks, 0 counterexamples).

## Step 2: union equalities over v-fiber blocks

Fix a value a ∈ 𝔽₃ of v′. Let R_a = {r : v′_r = a} (fiber of v′)
and F_a = {s : v_s = a} (fiber of v). Since v′ = v ∘ π₃ for some
π₃ ∈ D₄ (mod-3 classification), F_a = π₃(R_a); in particular
|R_a| = |F_a|.

Claim: ∪_{r ∈ R_a} M′_r = ∪_{s ∈ F_a} M_s as multisets.
Proof: τ′ restricts to a bijection between
{k : v′_{k mod 4} = a} = ∪_{r ∈ R_a} A_r and
{j : v_{j mod 4} = a} = ∪_{s ∈ F_a} A_s (since J′ = J ∘ τ′
preserves the second component), and p′_k = p_{τ′(k)}.
Taking first components gives the union equality. ∎

## Step 3: reduction to the stabilizer-adjustment lemma

By the pattern lemma (A), M′_r = M_{π₂(r)} for some π₂ ∈ D₄.
Hence for each block a,

```
∪_{s ∈ π₂(R_a)} M_s = ∪_{r ∈ R_a} M′_r = ∪_{s ∈ F_a} M_s.
```

Put γ = π₂ ∘ π₃⁻¹ ∈ D₄. Then π₂(R_a) = γ(F_a), so

```
∪_{s ∈ F_a} M_s = ∪_{s ∈ γ(F_a)} M_s    for every block a.   (*)
```

**Lemma S (stabilizer adjustment).** Let M = (M₀, M₁, M₂, M₃) be
class multisets, v a mod-3 4-vector, F_a its fiber blocks, and
γ ∈ D₄ satisfying (*). Then there exists δ ∈ Stab(M)
= {δ ∈ D₄ : M_{δ(s)} = M_s ∀s} with δ(γ(F_a)) = F_a for every a.

Given Lemma S, set π = δ ∘ π₂. Then π ∈ Π₂ (δ stabilizes M, so
M′_r = M_{π₂(r)} = M_{δ(π₂(r))} = M_{π(r)}), and
π(R_a) = δ(γ(F_a)) = F_a for every a, i.e. π(r) ∈ F_r for all r,
so π ∈ Π₃. Hence π ∈ Π₂ ∩ Π₃. ∎ (modulo (A) and Lemma S)

In particular, class sums satisfy S′_r = S_{π(r)} and
v′_r = v_{π(r)}, giving Y′ ≡ π(Y) (mod D) as in the Setup.

## Step 4: what Lemma S is, and what it is not

- Lemma S is a statement about multisets M and D₄; its
  verification at P = 8 and P = 16 used **all** Fix patterns
  (512 and 2048 patterns, all v-types, all γ satisfying (*):
  17 696 and 68 384 cases, 0 failures). It is **not** proved in
  general here, and §5 shows it is not provable from D₄ alone:
  it needs Fix-pattern structure.
- Lemma S does **not** claim concentration of τ′ on classes:
  the Wave-8 glued m = 12 pair has τ′-splitting
  r = 0 → {2:1, 1:2}, r = 3 → {2:2, 1:1} yet Y′ = π(Y) holds,
  because pattern class sums there coincide
  (p = (16,80,80,16), S = (16,80,80,16)). Concentration is false
  in general; Lemma S is the correct replacement.
- The search for a mixed counterexample at the component level
  (exact integer vectors z₂, z₂′ mod 2^a and z₃, z₃′ mod 3^e
  with same multisets, common σ, Π₂ ∩ Π₃ = ∅) returned nothing
  at P = 8 and P = 16 (bijective-τ searches above, plus the
  Wave-9 common-σ searches to m = 28 with 0 mixing). A genuine
  mixed pair would have to violate Lemma S or the pattern lemma;
  none was found.

## §5: Lemma S is NOT pure D₄ combinatorics (corrected)

An earlier sketch attempted a pure D₄ case proof of Lemma S.
That is **impossible**: Lemma S fails for arbitrary multisets.
Explicit counterexample (found by random search, 528 failures
in 90 780 γ-cases over 30 000 random M):

```
M = ((0,3), (1,2), (0,2), (1,3)),  v = (1,1,2,2),
blocks F = {0,1}, {2,3},  γ = (2,3,0,1) (rotation by 2).
```

Check: M₀ + M₁ = {0,1,2,3} = M₂ + M₃ = M_{γ(0)} + M_{γ(1)},
and likewise for the second block, so (*) holds; but
Stab(M) = {id} (all four M_s distinct), so no δ ∈ Stab(M)
maps γ(F) = {2,3} to F = {0,1}. Hence Lemma S cannot be
proved from D₄ bookkeeping and (*) alone.

Consequence: a proof of Lemma S must use the structure of
Fix-pattern class multisets beyond (*): for Fix patterns, the
bad configuration above does not occur (verified at P = 8, 16:
whenever (*) holds for a Fix pattern, a correcting δ exists).
What Fix property rules it out is the next question — candidates
are recurrence constraints linking class multisets (the pattern
sequence satisfies p_{k+1} = 6p_k − p_{k−1}, so the four class
multisets are not independent), and the fact that pattern values
are residues with 2-adic structure (e.g. common divisibility).
Until such a property is isolated and proved, Lemma S must be
cited as verified (Fix patterns, P = 8, 16) rather than proved,
and it stands alongside (A) as a named open input.

## Remaining gaps (explicit)

1. (A) Per-class pattern lemma in general (verified P ≤ 32).
   This is the main open input; it is Wave-10's lemma, not proved
   here.
2. Lemma S in general (verified for Fix patterns at P = 8, 16;
   §5 shows it is not pure D₄ combinatorics, so a proof must use
   Fix-pattern structure). Closing it needs the Fix property
   that rules out the §5 counterexample configuration.
3. Exact Lemma Y (not mod D): Pcarry — lifting Y′ ≡ π(Y) (mod D)
   to exact integer equality — is separate and still open.
4. General m (not just the 2- and 3-components): odd q ≠ 3 vanish,
   so CRT gives mod-D compatibility from the 2- and 3-components;
   no further prime needs a compatibility argument.
5. No Lean formalisation is claimed: this note is ordinary
   mathematics with two named assumptions; the Lean drafts
   (Pell C1, units reduction, radical, G3 core) remain text with
   `sorry` placeholders and are not cited as proofs.

## Files and verification logs

- This note: `methods/wave11_task3_pi2pi3_compatibility.md`.
- LTE note: `methods/wave11_task3_LTE_v2Dm.md`; check script
  `methods/wave11_task3_LTE_check.py` (m = 1..30, ALL OK).
- Bijective-τ searches: `methods/wave11_task3_explore2.py`
  (P = 8, 0 counterexamples), `methods/wave11_task3_explore3.py`
  (P = 16, 1 712 528 τ-checks, 0 counterexamples).
- Stabilizer-adjustment verification:
  `methods/wave11_task3_stab_check.py`
  (P = 8: 17 696 cases; P = 16: 68 384 cases; 0 failures).
- Per-k (non-bijective) abstract counterexample:
  `methods/wave11_task3_explore1.py` — shows bijectivity is
  load-bearing, not an artefact.
- Arbitrary-multiset failure of Lemma S:
  `methods/wave11_task3_stab_randomM.py`
  (90 780 γ-cases, 528 failures, e.g. M = ((0,3),(1,2),(0,2),(1,3)),
  v = (1,1,2,2), γ = (2,3,0,1)).
