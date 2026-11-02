# Wave 45, task 3 — Lemma U in general via period rigidity: alignment theorem proved, single-cycle rigidity isolated

## Verdict

Full unconditional classification is **not** proved, but the problem is now
sharply decomposed: the **alignment theorem** (§2) is proved in full
generality (no H4, no case analysis), and Lemma U is reduced exactly to two
**single-cycle** lemmas (L1, L3, §3) plus the degenerate locus (§4). The
new gcd ≥ 3 census (§5) tests the alignment prediction where partial
conjugation is forbidden: [PENDING — exploration running].

## 1. Setup (waves 37/41)

m = 2u, u odd; components q_a = p_a^{f_a}, q_b = p_b^{f_b} constraining
(α^u ≡ −1 mod p^f). Trace cycles t (period T_a | u), s (period T_b | u),
β = α². block0 = {(t_k, s_k) : k ∈ Z/u} as a multiset (each diagonal pair
repeated u/lcm times, lcm = lcm(T_a, T_b)), block1 = −block0,
℘ = block0 ∪ block1. A ℘-collision is a parameter pair (D^a, D^b) whose
β-cycle pair (X, Y) partitions ℘: X ∪ Y = ℘ as multisets, |X| = |Y| = u.
Known mechanisms: (i) dihedral moves (simultaneous rotation, reversal,
negation); (ii) partial conjugations (one side conjugated); (iii) scaling
degeneracies (waves 39–40, under H2'); (ker) p = 3 kernel translations.

## 2. Alignment theorem (proved, generic case)

Assume t, s nonzero, with distinct values in one period and negation-free
value sets (0 ∉, v ≠ −v′). Assume L1, L3 (§3). Then every ℘-collision is
dihedral, or — only when g = gcd(T_a, T_b) divides 2 — one partial
conjugation; in both cases the block pair is preserved.

Proof. Let X have coordinate cycles x, y. First-coordinate multisets:
M(x) ∪ M(x′) = M(t) ∪ M(−t) (X, Y partition ℘). By L3,
{M(x), M(x′)} = {M(t), M(−t)}; by L1, x = ε·(dihedral image of t) and
y = δ·(dihedral image of s) for uniform signs ε, δ. Signs must agree:
if ε = −δ, a pair (x_k, y_k) ∈ ℘ would force t_j = −t_{j′} or
s_j = −s_{j′} (negation-free, p odd ⇒ impossible). So ε = δ; if
ε = δ = −1, run the same argument against block1 instead of block0.
Assume ε = δ = 1 and write x_k = t_{σ_a k + r},
y_k = s_{σ_b k + c} (σ ∈ {±1}, shifts r, c), using distinctness: the pair
(x_k, y_k) ∈ ℘ determines j mod lcm, hence j ≡ σ_a k + r (mod T_a) and
j ≡ σ_b k + c (mod T_b) for a single j = j(k).
Index-set computation. The k-map hits (a, b) = (σ_a k + r mod T_a,
σ_b k + c mod T_b) uniformly (u/lcm times each) on the set
S = {(a, b) : σ_b(a − r) ≡ σ_a(b − c) (mod g)} (CRT: the map
Z/lcm → S is a bijection). Block0's pairs are the diagonal
D = {(a, b) : a ≡ b (mod g)} (each u/lcm times).
- σ_a = σ_b: S = {a − b ≡ r − c (mod g)}. Multiset equality S = D
  forces r ≡ c (mod g); then CRT gives j(k) = σk + r₀ mod lcm, i.e. X
  is a simultaneous rotation (σ = 1) or reversal (σ = −1) of block0:
  dihedral.
- σ_a = −σ_b: S = {a + b ≡ r + c (mod g)}. S = D iff a ≡ b (mod g)
  ⟺ a + b ≡ r + c (mod g) for all (a, b), iff 2a ≡ 0 (mod g) ∀a,
  i.e. g | 2 (with r + c ≡ 0 mod g). Then X is the one-sided reversal:
  a partial conjugation, and its block multiset equals block0's.
  For g ≥ 3, S ≠ D: flipped pairs mostly lie outside ℘ entirely, so no
  flipped recombinant exists at all.
No H4 is used anywhere: the only inputs are L1, L3, distinctness, and
negation-freeness. The g | 2 dichotomy (g ∈ {1, 2}) is exactly wave 41's
conclusion, now without branch-free hypotheses.

## 3. The remaining gap, stated exactly: single-cycle lemmas

(L1) A β-cycle with value multiset M(t) is dihedral to t, up to
rational scalings: verified failure of the naive form at m = 30 —
C^a = √2 vs 1 + 2√2 (mod 25) have identical value multisets but are not
dihedral-related (checked: not a rotation, reversal, or negation-rotation);
in fact t2[k] = 21·t1[k−10], i.e. rational scaling by 21 composed with
rotation (1 + 2√2 ≡ 21·β⁵·√2 mod 25). So L1 must classify value-set
permutations λ ∈ Z^×, not just dihedral moves. A scaled cycle does NOT
generally preserve pair blocks (checked at m = 30: block0 and ℘ both
differ for C^b = (1,2), (0,1), (2,3) mod 29) — so scalings are a
degenerate case to classify, not an automatic collision mechanism.
(L3) No single-component recombination: M(x) ∪ M(x′) = M(t) ∪ M(−t)
implies {M(x), M(x′)} = {M(t), M(−t)}.
Precedent: at mod-p level, the trace-polynomial identity
∏(X − Tr(Aα^j)) = C·(Tr(A^L) − V_L(X, N)) determines A up to dihedral
(wave 12 §3a) — the β-cycle mod-p^f analogue of this identity, extended
to rational scalings, is the precise missing ingredient for L1/L3.
Verified exactly so far: L1/L3 at m = 30 (29-side, 841 params; 25-side,
625 params) and at m = 60 (19-side, 361 × 361; 11-side fibers,
1080 matches); no L1/L3 conflict has ever been observed, but neither
lemma is proved in general.

## 4. Degenerate locus (outside §2)

Where §2's hypotheses fail, the known mechanisms live: zero coordinates
(scaling, waves 39–40); torsion C ∈ pR (shorter periods, repeated values);
pure-√2 parameters (odd symmetry ⇒ Cartesian-product blocks ⇒ partial
conjugations, wave 38); negation coincidences s_j = −s_{j′} (fiber
collisions, partial negations at m = 60); p = 3 kernel translations
(identical cycles, Lemma U unaffected); rational scalings λ·(dihedral
image) with λ permuting the value set (§3, m = 30 example λ = 21).
The census (§5) checks whether anything else occurs at gcd ≥ 3, where §2
forbids partial conjugation for generic cycles — so any multi-orbit
group there must be degenerate or a counterexample to L1/L3.

## 5. New stress census at gcd ≥ 3: m = 110, fully rigid

First generic gcd ≥ 3 case: components (29,1) × (109,1) at m = 110
(u = 55), β-orders 5 and 55, gcd 5 (order scan over all m < 400; the
next candidates, (53,1) × (197,1) at m = 54 and (101,1) × (137,1) at
m = 102, are 109M/191M points and were not run). Exact C++ census
(wave45_census_m110.cpp, 8m18s): 9,991,921 points, 47,037 ℘-groups,
**conflicts 0, multi-orbit groups 0, UNKNOWN 0** — every ℘-group is a
single dihedral orbit. So at gcd 5, no partial conjugation, no partial
negation, no scaling, and no fourth kind occurs at all.
Caveat that sharpens the theory: the B-side cannot satisfy §2's generic
hypotheses — cross-tab over all 11,881 B-params: (55-distinct,
negation-free) = (5940, 5940) but the intersection is EMPTY (plus the
zero param). This is counting, not accident: any 55 distinct values mod
109 must contain a negation pair, since 55 > 109/2. In general,
genericity needs T ≤ (p^f − 1)/2; components with T > p^f/2 (like 109
here) are irreducibly degenerate, yet rigidity still holds. Also
census-proved at m = 110: no value-set-preserving rational scaling
λ ≠ ±1 occurs (else a zero-coordinate point would give a multi-orbit
group). A-side generic params: 560/841.

## 6. Conclusion

Lemma U in general is now: alignment theorem (proved) + L1 + L3 +
degenerate-locus classification. The full-cycle problem is reduced to a
single-cycle problem; the alignment step, which previously needed H4
(wave 41, empty hypotheses), needs no branching hypothesis at all.
No Lean built, repository untouched.
