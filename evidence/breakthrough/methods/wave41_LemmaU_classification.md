# Wave 41 — Lemma U: "only three mechanisms" classification

## Verdict

No fourth kind found. The full unconditional classification is still **open**,
but the picture is now sharp:

- **Rigid theorem proved** under H1–H4 (§2): every ℘-collision is (i) dihedral
  or (ii) one partial conjugation (only if g = gcd(T_a,T_b) | 2); (iii) impossible.
- **H4 is exactly empty** at every f = 1 component tested (§3): the rigid
  theorem is a proved implication with (empirically) empty hypotheses.
- **Kernel is a fourth β-cycle mechanism, but only at p = 3 and harmless**
  (§4): kernel translates have identical blocks, so Lemma U is unaffected.
- **Sweep: 27 cases, 44,932,435 points, 344,328 groups, 0 conflicts, 0 UNKNOWN**
  (§5). Every group is (i), (ii), (iii), (ker), or a combination; no group
  type involves partial negation.

## 1. Setup and mechanisms

m = 2u, u odd (PAIR regime); q_a, q_b constraining, distinct odd primes.
block0 = {(Tr(C^a β^k), Tr(C^b β^k))}, block1 = −block0, ℘ = block0 ∪ block1.
Mechanisms: (i) dihedral D = ⟨R, K, N⟩; (ii) partial conjugations J_a, J_b at
degenerate (product) parameters (wave 38); (iii) scaling degeneracies (wave 39
under H2', wave 40: H2' ⟺ order-growth); (ker) p = 3 kernel translates (§4);
(neg) partial negation (§6). Classifier edge types between D-orbits: J, S
(genuine scaling: λ ≡ ±1 mod p but ≢ ±1 mod p^f), N, K; group type = first
connecting edge subset in order J, S, N, K, then pairs, etc.

## 2. Rigid theorem (proved, narrow hypothesis H-rigid)

Assume p ≠ 3 in both components, and for each coordinate trace sequence
(period T, values v_j): H1: T > 1 (so T ≥ 3, since T | u, u odd); H2: values
distinct in one period; H3: value set negation-free (v_j ≠ −v_{j′} ∀j,j′,
so 0 ∉); H4 (branch-free): 34v_j − σv_{j′} = τv_{j′′} (σ, τ ∈ {±1}) has only
the standard solutions σ = τ = +1, {j′, j′′} = {j−1, j+1} mod T.
Conclusion: any (D^a, D^b) with ℘(D) = ℘(C) is D-equivalent to (C^a, C^b),
or — only when g = gcd(T_a, T_b) | 2 — D-equivalent up to one partial
conjugation. So the ℘-group is (i), resp. (ii); (iii) cannot occur: scaling
needs a zero coordinate (violates H1) or pure-√2 saturation with f ≥ 2
(violates H2, values repeat); at f = 1 scaling is just ±1.
Supporting lemmas (proved): point period = trace period, via Lemma C
(Tr(Cβ^k) = 0 for k = 0, 1 ⟹ C = 0, p ≠ 3); relative shifts are rotations:
(β^{k_0}C^a, β^{k_1}C^b) with k_1 − k_0 ≡ 0 mod g equals a rotation by CRT;
the twisted diagonal equals the diagonal iff δ ≡ 0 mod g (both maps factor
through Z/T bijectively onto compatible pairs a ≡ b mod g, each u/T times);
the flipped map lands on a ≡ −b mod g, equal to the compatible set iff g | 2.
Proof sketch. (1) D's block0′ positions lie in ℘ positions, so x_k =
Tr(D^a β^k) satisfies x_{k+1} = 34x_k − x_{k−1} with values in {±t_j};
same for y_k ∈ {±s_j}. (2) H4 induction: from x_0 = ε_0 t_{j_0},
x_1 = ε_1 t_{j_1}, the value x_2 = 34x_1 − x_0 ∈ {±t} forces
ε_0 = ε_1 = ε_2 and {j_0, j_2} = {j_1−1, j_1+1}; propagation by
34t_{j+σ} − t_j = t_{j+2σ} gives x_k = ε t_{σk+k_0} globally, and
y_k = δ s_{τk+k_1}. (3) Joint matching: (x_k, y_k) = η_k(t_{j_k}, s_{j_k});
H2+H3 force η_k = ε, j_k ≡ σk+k_0 (mod T_a), and η_k = δ,
j_k ≡ τk+k_1 (mod T_b); hence ε = δ and σk+k_0 ≡ τk+k_1 (mod g) ∀k —
so σ = τ with k_0 ≡ k_1 (mod g), or g | 2 (σ ≠ τ allowed only then).
(4) Parameters via Lemma C (k = 0, 1): σ = +1 gives a rotation (i);
σ = −1 gives conjugation + rotation (i); σ ≠ τ (g | 2 only) gives one
partial conjugation plus independent shifts (ii). For p = 3 the same proof
goes through with the α-version of Lemma C (not verified computationally).

## 3. H4 is empty: branch-free fails everywhere tested

Exact per-component counts (all H1–H3 sequences checked, not sampled):

| component | T | H1–H3 seqs | pass H4 |
|-----------|---|-----------:|--------:|
| (29,1)    | 5 |        560 |       0 |
| (197,1)   | 9 |     35,280 |       0 |
| (269,1)   | 15|     64,320 |       0 |
| (137,1)   | 17|     14,144 |       0 |
| (389,1)   | 39|    121,056 |       0 |
| (293,1)   | 49|     57,232 |       0 |

Worked exotic solution at (29,1), values (2, 14, 10, 7, 25): 34t_1 − t_1 =
33·14 ≡ −2 = −t_0 (mod 29) — a genuine "stay-and-flip" branch
(x_0, x_1, x_2) = (t_1, t_1, −t_0) that H4 was meant to exclude (recurrence
checks: 34·14−2 = 10 = t_2, etc.). Why generic: each exotic equation is
linear in (t_0, t_1), i.e. a line in the p^{2f}-point plane; there are
~4T³ such lines of p^f points each, so the plane is covered when 4T³ ≫ p^f
(e.g. (269,1): 4·15³ = 13,500 lines × 269 ≫ 269²). Consequence: do not cite
the rigid theorem as covering any real case. The remaining hard core is
full-cycle rigidity: an exotic triple alone does not give a recombinant
full cycle, and ruling out exotic full cycles needs a global argument.

## 4. Kernel mechanism at p = 3 (fourth β-mechanism, harmless)

ker(C ↦ (Tr(Cβ^k))_k) at (3, f) is {(0, b) : 3^{f−1} | b}, size 3 for every f:
Tr(C) = 2a = 0 ⟹ a = 0 mod 3^f; Tr(Cβ) = 2(17a+24b) = 0 ⟹ 48b ≡ 0 mod 3^f
⟹ b ≡ 0 mod 3^{f−1}. For odd p ≠ 3 the kernel is {0} (det 96 a unit mod p^f).
Root cause: β ≡ 2 mod 3R is rational, so Tr(c√2·β^k) = 0 ∀k. Kernel
translates have identical trace sequences, hence identical blocks, hence the
same block pair — Lemma U is unaffected. The α-formulation is immune:
(Tr, Tr∘α) has det 32, a unit mod 3. Verified: kernel sizes 3 for p = 3,
1 otherwise, in all 27 cases. At (3,1), J_a preserves every trace sequence
(β rational) and lands in the same D-orbit ({±C, ±C̄}), so no J-edges arise;
at (3,73) all 518 groups are "ker" alone. u-even cases are β-cycle tests
only (PAIR needs u odd).

## 5. Sweep (scripts: wave41_LemmaU_sweep.py, wave41_sweep_all.py)

u-odd (PAIR regime), q = p^{2f}; types count groups. All-i cases: (54: 25,2809)
70,225 pts, 785 groups; (54: 25,38809) 970,225, 27,445; (102: 25,10201) 255,025,
1,505; (126: 25,38809) 970,225, 27,445. Mixed cases:
(42: 25,28561) 714,025, 7,565, i:5525 ii:2040; (70: 169,841) 142,129, 993,
i:741 ii:252; (90: 25,841) 21,025, 369, i:285 ii:84; (102: 25,18769) 469,225,
2,277, i:1725 ii:552; (114: 25,1369) 34,225, 221, i:185 ii:36;
(126: 25,169) 4,225, 77, i:65 ii:12; (30: 625,841) rerun 525,625, 9,061,
i:8975 ii:84 iii:2; (90: 841,38809) rigid 32,638,369, 112,365, i:39649 ii:72716.
u-even (β-cycle only): (81,121) at m = 12 and 36 identically: 9,801, 307,
ker:162 iii:67 i:3 ii:75; (36: 9,5329) 47,961, 518, all ker;
(36: 81,5329) 431,649, 4,219, ker:2294 iii:926 i:3 ii:996; (36: 121,5329)
644,809, 18,320, all i; (60: 81,361) 29,241, 286, ker:74 iii:56 i:138 ii+iii:18;
(60: 121,361) 43,681, 628, i:403 ii:225; (60: 81,3481) 281,961, 2,298, ker:582
iii:292 i:1134 ii+iii:290; (60: 121,3481) 421,201, 5,004, i:2539 ii:2465;
(60: 361,3481) 1,256,641, 63,393, all i; (84: 81,6889) 558,009, 2,467, ker:1314
iii:535 i:3 ii:615; (84: 121,6889) 833,569, 10,389, all i; (84: 81,12769)
1,034,289, 5,871, ker:1482 iii:682 i:2907 ii+iii:800; (84: 121,12769) 1,545,049,
12,768, i:6208 ii:6560. Total: 44,932,435 points, 344,328 groups, 0 conflicts, 0 UNKNOWN, no D-orbit escaping its group, no rigid violation. At (90: 841,38809): 19,756,800 H1–H3 points; rigid sample 300, 0 pass H4.
Notes. (a) m = 30 rerun reproduces wave 37 totals (9,061 groups, 0 conflicts)
and its 2 scaling groups; its 84 ii groups split as 56×(60,60) + 28×(30,30),
so wave 37's "58" counted only full-orbit collisions — no contradiction.
(b) Genuine scaling (f ≥ 2) appears at (3,2) cases (iii, ii+iii), not only at
m = 30 (5,2). (c) H1–H3 points are 0 in every swept case except
(90: 841,38809): 2T ≤ p^f is a hard filter (e.g. T = 3 at (5,2) lives in 5Z/25,
where 3 negation-free values cannot exist).

## 6. Partial negation: clarified, never needed

At f = 1 the allowed λ are only ±1, so "scaling" edges there are partial
negations (λ = −1 on one coordinate) or conjugation-on-pure-√2
(conj(c√2) = −c√2). For B = {(−t_k, s_k)}, ℘′ = ℘ requires B = A or B = −A;
mixed recombinations would be conflicts (0 observed). If the negated
coordinate is pure √2, negation = conjugation, linking to (ii)/product
structure (wave 38). Empirically: no group type in the sweep contains "neg"
— f = 1 λ-edges were always redundant with J or absent. Partial negation at non-pure-√2 parameters with no product structure would be a genuinely new phenomenon; none observed.

## 7. Remaining gaps

- Full classification without H-rigid still open; the H4 failure (§3) says the
  proof needs full-cycle rigidity, a new idea, not a patch to H4.
- Skipped as too big for this run (future work, not results):
  (54: 2809,38809; 109M), (70: 841,28561; 24M), (98: 169,85849; 14.5M),
  (110: 841,11881; 10M), (126: 169,38809; 6.6M), (130: 841,271441; 228M),
  and mechanism classification of (625,72361) (45.2M, conflict-free in wave 37).
- p = 3 α-version of the rigid theorem unverified computationally.
- Non-constant paddings at m = 30 (wave 38 open question) untouched.
