# Wave 11, task 2 — exact per-class lemma: no counterexample, mod-p proof, remaining gaps

## Statement

Fix_m = ker(H_m mod D_m), lifts 0 ≤ y_i < D_m, t = gcd(m,4),
O_r = {i : i ≡ r (mod t)}. Per-class multiset of y is {y_i : i ∈ O_r}.
Exact per-class lemma: if y, y′ ∈ Fix_m have the same sorted multiset,
then their per-class multisets are D_t-related: some π ∈ D_t with
per-class′(r) = per-class(π(r)) for all r. If true in general, it closes
Lemma Y and Pcarry together (Y′ = π(Y) exactly, so carry d = 0).
Status after this wave: **not proved in general, no counterexample found**,
but the lemma is **proved mod p for every odd prime p | D_m** (proof below),
with the key polynomial identity and the root step verified numerically.

## New searches (all exact arithmetic, all 0 failures)

1. Component search, per prime power q ‖ D, grouping by sorted multiset,
   D_t-canonical per-class tuple constant
   (`wave11_perclass_component.py`, log `wave11_perclass_component.log`):
   71 cases, 0 bad groups. Nontrivial (t = 2, 4) cases include
   m = 4, 6, 8, 10, 12, 14, 16, 18, 20, 28, 32, 36, 64;
   largest: (16, 577²), (32, 577²) — 332929 vectors, 10693 groups each;
   (64, 32768) — 32768 vectors, 539 groups. Odd-m cases are t = 1, hence
   vacuous for the lemma (single class). Untested components are only
   prime squares > 400000 (e.g. (24, 1153²)); (15, 31⁴) was skipped but is
   t = 1, hence trivial anyway.
2. Joint (2,3)-component search, CRT tuples as exact codes
   (`wave11_joint_multiset.py`, log `wave11_joint_multiset.log`):
   m = 4, 8, 12, 16, 20, 24, 28, 32, 36, 0 bad groups everywhere;
   m = 32: 73728 vectors, 1664 groups; m = 36: 93312 vectors, 1491 groups.
   Triple (128, 81, 25) at m = 12: 259200 vectors, 11397 groups, 0 bad.
3. Mod-p search, all recurrence sequences mod p (p² sequences, since
   M^m ≡ I mod p for odd p | D_m — see proof)
   (`wave11_perclass_modp.py`, log `wave11_perclass_modp.log`):
   m = 4..20, all odd p | D_m with p ≤ 700, 41 cases, 0 bad.
   This is the layer the mod-p proof below covers.

## Mod-p proof (odd p | D_m)

Work in R = Z[√2], α = 3 + 2√2, β = 3 − 2√2 = α⁻¹, Tr(x) = x + x̄.
Let p be odd, p | D_m, so s_m = α^m + β^m ≡ 2 (mod p) as integers.

Step 0 — α^m = 1 in R/p. In R/p, (α^m − 1)² = α^m(α^m + β^m − 2) ≡ 0.
R/p is a product of fields (F_{p²} if 2 is a non-residue, F_p × F_p if
it is a residue), hence reduced, so α^m = 1 in R/p. Also α − β has
norm −32, a unit mod p (p odd), so α − β is a unit in R/p. Hence every
recurrence sequence mod p has a unique representation
y_i = Tr(A α^i) with A ∈ R/p, from y₀ = Tr(A), y₁ = Tr(A α),
and y_{i+m} = y_i automatically. Let L = order of α in (R/p)×; L | m,
L coprime to p (L | p−1 in the split case, L | p²−1 in the inert case).
G = ⟨α⟩ has order L, and ∏_{z∈G}(T − z) = T^L − 1 in (R/p)[T] in both
cases (in the split case G projects to the full L-th-root subgroup in
each component). The length-m sequence is (m/L) copies of the
length-L sequence (Tr(A z))_{z∈G}.

Step 1 — global multiset determines (N, Tr(A^L)).
Let N = A Ā ∈ F_p. Claim, for L ≥ 1:
  ∏_{z∈G} (X − Tr(A z)) = C · (Tr(A^L) − V_L(X, N)),
where C = (−1)^L ∏_{z∈G} z⁻¹ ∈ F_p× (independent of A; ∏ z = 1 if L
odd, = −1 if L even, in both split and inert cases), and V_L is the
Lucas polynomial V₀ = 2, V₁ = X, V_{k+1} = X V_k − N V_{k−1}.
Proof: X − Tr(A z) = −(A z² − X z + Ā)/z. The roots r₁, r₂ of
A z² − X z + Ā satisfy r₁ r₂ = Ā/A, r₁ + r₂ = X/A. Then
∏_{z∈G}(A z² − X z + Ā) = A^L (r₁^L − 1)(r₂^L − 1)
  = Ā^L − A^L(r₁^L + r₂^L) + A^L.
Put u = A r₁, v = Ā/r₁; then u + v = X, uv = N, and
A^L(r₁^L + r₂^L) = u^L + v^L = V_L(X, N). Collecting the factor C
gives the formula. The polynomial on the left is determined by the
global multiset (divide multiplicities by m/L to get the G-multiset,
whose roots with multiplicities are exactly its factors). For L ≥ 2,
the coefficient of X^{L−2} in V_L is −L N, and L ≠ 0 mod p, so N is
recovered; then Tr(A^L) follows from the constant term. (L = 1 means
α = 1 mod p, all sequences constant, lemma trivial.)
Numerical check: identity verified for 50 random A in each of 12
(m, p) pairs (8,17), (12,11), (20,41), (12,5), (12,7), (20,19),
(16,577), (10,29), (6,7), (8,3), (13,599), (16,17). Also (N, Tr(A^L))
is constant inside every mod-p fibre group in all tested cases.

Step 2 — coset multisets up to D_t.
Let H = ⟨α^t⟩ ⊂ G, g = gcd(L, t), |H| = L/g, ζ = α^{|H|} of order g.
Class r (as a multiset over H, ignoring the repetition factor
(m/t)/|H|, independent of r) is {Tr(A α^r h) : h ∈ H}. Apply Step 1
with (G, A) replaced by (H, A α^r): its polynomial depends only on
N (since (A α^r)(Ā β^r) = N, as αβ = 1) and on
Tr((A α^r)^{|H|}) = Tr(B ζ^r), where B = A^{|H|}.
Now B^g = A^L, B̄^g = Ā^L, B B̄ = N^{|H|}. If A′ has the same
(N, Tr(A^L)) as A, then {A′^L, Ā′^L} = {A^L, Ā^L} (roots of
T² − Tr(A^L) T + N^L). If A′^L = A^L, then B′^g = B^g, so B′ = B ω with
ω^g = 1; the g-th roots of unity in (R/p)× form the unique subgroup
⟨ζ⟩, so B′ = B ζ^k (shift r ↦ r + k). If A′^L = Ā^L, then
B′ = B̄ ζ^k, and Tr(B̄ ζ^{r+k}) = Tr(B ζ^{−(r+k)}) (reflection
r ↦ −r). Zero cases: B = 0 forces A = 0 (R/p reduced), trivial;
a split zero component (B = (b, 0)) still gives B′ = B ζ^k, since
the nonzero component's g-th root is unique up to ⟨ζ⟩. Hence the
coset family of A′ is a shift or reflection of that of A, i.e. the
per-class multisets mod p are D_t-related. ∎ (mod p)

Numerical check of Step 2: for every mod-p fibre group in
(8,17), (12,11), (12,5), (12,7), (20,41), (20,19), (10,29), (6,7),
(16,17), every pair satisfies B′ = B ζ^k or B′ = B̄ ζ^k
(3276 pairs total, 0 failures; includes g = 1, where the condition is
B′ ∈ {B, B̄} and cosets coincide with the global multiset).

## Remaining gaps for the full exact lemma

G1. Odd prime-power lift. Mod p^e (e ≥ 2), (α^m − 1)² ≡ 0 but
α^m ≠ 1 in general (α^m = 1 + ε, ε² = 0), so the group ⟨α⟩ in
(R/p^e)× is larger and Step 1 does not apply directly. A digit /
Hensel argument is needed to lift the mod-p D-relation to mod p^e
with the same π. Component searches support it, but there is no
proof yet. (Analogous to the P3′ digit analysis for p = 3.)
G2. 2-primary component. α − β has norm −32, not a unit mod 2, so
the R/p representation fails at p = 2. A separate SNF / pattern
argument is needed (cf. wave-10 P2 analysis, but for multisets, not
just sums). Component searches for 2-powers up to 32768 (m = 64)
support it, but there is no proof yet.
G3. Common π across components. Componentwise D-relations do not
automatically give one π for all components: two components could
in principle force different π (a CRT obstruction — e.g. t = 2,
π = id on one component, π = swap on another, with no common π).
The exact lemma needs a global argument producing one π (e.g. via
an exact α-representation over R/D_odd plus a 2-part argument
matched to it, or via a value occurring with multiplicity 1 in
some class forcing π). No such argument is proved yet; in all
searched cases a common π exists.

## Conclusion for the parent

- Counterexample: none found, in three independent exact searches
  (components, joint (2,3) tuples, mod p), including m = 32, 36, 64.
- Proof: exact per-class lemma is proved mod p for all odd p | D_m
  (sketch above, key identity and root step numerically verified).
- Full exact lemma remains open, with gaps precisely G1 (odd
  prime-power lift), G2 (2-primary), G3 (common π). Recommended next
  step: attack G1 first (odd lift), since G2/G3 are then the only
  remaining obstacles and the 2-part pattern analysis from P2 may
  adapt to multisets.
- No change to main; no Lean built. Scripts and logs:
  `methods/wave11_perclass_component.py` (+`.log`),
  `methods/wave11_joint_multiset.py` (+`.log`),
  `methods/wave11_perclass_modp.py` (+`.log`), this note.
