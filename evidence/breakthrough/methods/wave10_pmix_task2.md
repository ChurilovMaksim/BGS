# Wave 10, task 2 — Lemma Y: P-periodicity argument for Pmix, subgaps (1), (2), (3)

## Verdict in one paragraph

Subgap (1) is **closed in its correct form and refuted in the two forms
wave 9 suggested**: a dihedral τ on pattern positions does NOT always
exist, and an affine τ does NOT always exist either — but a
**class-permuting τ always exists** (verified for every pair at
P = 4, 8, 16, 32), and that is exactly what Lemma Y needs.
Subgap (2) (P = m) **dissolves**: the per-class lemma applies to the
whole vector directly, no periodicity is needed, and it is verified
at m = 32. Subgap (3) (Pcarry) is **not proved by the H_t d = ΔW
bound, but is reframed**: exact per-class multisets are D4-related
at m = 4, 6, 8 exhaustively and on both known m = 12 fibers, and
exact per-class multisets imply d = 0 immediately — so the remaining
proof obligation is one lemma (exact per-class multisets), not a
carry estimate. No exact counterexample was found anywhere:
m = 36 joint lifts (93,312 vectors, 91,821 pairs) and m = 32 joint
lifts (73,728 vectors, 72,064 pairs) both give 0 exact failures.

## 0. Setup and notation

m with t = gcd(m, 4) = 4 (only non-trivial case), D = D_m,
a = v₂(D), P = 2^{v₂(m)}. Every Fix vector mod 2^a is P-periodic
(wave 9 §5; the step "v₂(D_m) depends only on v₂(m)" is the usual
LTE phenomenon in Z[√2] and is still to be written out in full —
it is an analytic input to the pattern argument, independent of
the lemmas below). Write z for the mod-2^a component, p for its
pattern (length P), S_r(p) = Σ_{j≡r (mod 4)} p_j for the pattern
class sums. Then Y_r mod 2^a = (m/P)·S_r(p), and m/P is odd, hence
a unit mod 2^a — so Y mod 2^a determines S(p) and vice versa.

A matching τ for patterns p, p' means p' = p∘τ (τ a permutation of
Z/P). A matching τ is **class-permuting** if τ(j) mod 4 = π(j mod 4)
for some π ∈ D_4. Class-permuting matchings exist iff the per-class
multisets of p' are a D_4 permutation of those of p (choose
value-preserving bijections within matched classes).

## 1. Subgap (1): repeats / stabiliser — corrected and closed in form

### 1.1 Dihedral τ is FALSE (P ≥ 8)

Pattern test (script `wave10_pattern_dihedral.py`): enumerate
Fix_P mod 2^a, group by sorted multiset, check whether each group
is a single dihedral orbit.

| P | q = 2^a | groups | strong-fail groups |
|---|---|---|---|
| 4 | 128 | 39 | 0 |
| 8 | 512 | 76 | 5 |
| 16 | 2048 | 145 | 10 |

Example at P = 8, multiset (0, 64, 128, 192, 256, 320, 384, 448):
group size 32, dihedral orbit size 16; p = (0, 64, 384, 192, 256,
320, 128, 448) and p' = (0, 192, 128, 64, 256, 448, 384, 320) are
both recurrence sequences, same multiset, not dihedrally related.
So "adjust σ by the stabiliser to a dihedral τ" is impossible in
general — the stabiliser cannot create a dihedral τ that does not
exist. The same failure is massive at P = 32 (see §1.2).

### 1.2 Affine τ is FALSE at P = 32 (but held at P ≤ 16)

Pattern test (scripts `wave10_pattern_affine.py`,
`wave10_p32.cpp`): for each ordered pair (p, p') in a group, check
for τ(j) = a·j + b, a odd, with p' = p∘τ.

| P | ordered distinct pairs | dihedral-fail | affine-fail |
|---|---|---|---|
| 4 | 412 | 0 | 0 |
| 8 | 5,660 | 1,792 | 0 |
| 16 | 77,852 | 44,800 | 0 |
| 32 | 1,120,284 | 847,616 | 262,144 |

Explicit affine-fail pair at P = 32, q = 8192 (from
`wave10_p32_dump.cpp`):
p = (64, 448, 2624, 7104, 7232, 3520, 5696, 6080, 6208, 6592, 576,
5056, 5184, 1472, 3648, 4032, 4160, 4544, 6720, 3008, 3136, 7616,
1600, 1984, 2112, 2496, 4672, 960, 1088, 5568, 7744, 8128),
p' = (64, 960, 5696, 448, 5184, 6080, 6720, 1472, 2112, 3008, 7744,
2496, 7232, 8128, 576, 3520, 4160, 5056, 1600, 4544, 1088, 1984,
2624, 5568, 6208, 7104, 3648, 6592, 3136, 4032, 4672, 7616).
Values of p are distinct, so the matching τ is unique:
τ = (0, 27, 6, 1, 12, 7, 18, 13, 24, 19, 30, 25, 4, 31, 10, 5, 16,
11, 22, 17, 28, 23, 2, 29, 8, 3, 14, 9, 20, 15, 26, 21).
τ is not affine mod 32 (τ mod 16 = 11j mod 16, τ(j+16) ≡ τ(j)+16
(mod 32), but no single a, b mod 32 works), yet τ mod 4 =
(0, 3, 2, 1) repeated — a reflection on classes. A second
affine-fail pair has τ mod 4 = identity. So the τ that exists is
2-adic in flavour (affine mod 16, lifted with a class-dependent
high bit), not affine mod 32.

### 1.3 Class-permuting τ: TRUE for every pair at P ≤ 32

Per-class multiset test (scripts `wave10_perclass.py`,
`wave10_p32.cpp` patched copy): for each ordered pair, check
whether the 4 per-class multisets of p' are a D_4 permutation of
those of p.

| P | ordered distinct pairs | per-class-fail |
|---|---|---|
| 4 | 412 | 0 |
| 8 | 5,660 | 0 |
| 16 | 77,852 | 0 |
| 32 | 1,120,284 | 0 |

In all cases the weak (class-sum) condition also holds
(0 weak-fail groups at every P). Hence:

**Per-class pattern lemma (verified P ≤ 32, unproved in general).**
If p, p' ∈ Fix_P mod 2^a have the same multiset, then their
per-class multisets are D_4-related.

**Why this closes (1).** Given a class-permuting pattern τ,
define a global σ' blockwise: for i = kP + j (0 ≤ k < m/P),
σ'(i) = kP + τ(j). Since 4 | P, i mod 4 = j mod 4, so σ' maps
global class r to class π(r); and y'_{kP+j} = p'_j = p_{τ(j)} =
y_{kP+τ(j)} = y_{σ'(i)}, so y' = y∘σ'. Thus σ' is a
class-permuting global matching, and it differs from any given
σ with y' = y∘σ by the stabiliser of y (σ⁻¹σ' preserves y
value-wise). This is exactly the stabiliser adjustment wave 9
asked for — with "class-permuting" in place of "dihedral".
Consequence for the 2-component: S(p') = π(S(p)) (sums of equal
multisets), hence Y' ≡ π(Y) (mod 2^a) via the odd factor m/P.
No property of σ beyond multiset equality is used.

Remaining proof obligation for (1): prove the per-class pattern
lemma in general. It is strictly stronger than needed for class
sums, and its mechanism is not yet understood (a plausible route
is 2-adic digit analysis: mod-2^k reductions of patterns have
period 4 in the class direction, cf. the P = 32 example where
p_j mod 1024 depends only on j mod 4 within a class — but this
is an observation, not a proof).

## 2. Subgap (2): P = m — dissolves

When m is a power of 2, P = m, and the period lemma is vacuous
(P-periodic = every sequence). This is no longer an obstacle:
the per-class pattern lemma applies to the vector mod 2^a
itself, which IS the pattern (length m). The P = 32 test above
is precisely the P = m = 32 case: per-class-fail = 0 over
1,120,284 pairs, dihedral-fail = 847,616, affine-fail = 262,144.
So (2) reduces to the same per-class lemma as (1); there is no
separate argument to find for powers of 2. (The m = 16 case was
already covered by the P = 16 pattern test.)

## 3. Subgap (3): Pcarry — H_t d bound stalls, per-class reframes it

### 3.1 The H_t d = ΔW derivation, and where it stops

With t = 4, H_4 Y = D W, W_r = Σ_{i≡r} w_i, w = Hy/D ∈ {-1,…,5}^m
(H_4 is the 4×4 circulant 6I − shift − shift⁻¹, eigenvalues
4, 6, 8, 6, det 1152; H_4 commutes with D_4). If Y' ≡ π(Y)
(mod D), write Y' − π(Y) = D·d with d_r ∈ {-(m/4−1),…,m/4−1},
Σ d_r = 0. Applying H_4 and cancelling D gives H_4 d = ΔW,
ΔW = W' − π(W). The bound available from w_i ∈ {-1,…,5} alone
is ‖ΔW‖_∞ ≤ 3m/2, and ‖H_4⁻¹‖ is constant, so this bounds
|d_r| by O(m) — it does NOT force d = 0. The missing input is
structure of W, W' for Fix vectors, not a better norm estimate:
W and W' are class sums of w for vectors in the same fiber,
and no argument was found that controls ΔW beyond the trivial
bound. So the carry estimate, as posed, is not the right route.

### 3.2 Exact per-class multisets: stronger evidence, and d = 0 follows

**Exact per-class lemma (verified, unproved in general).** If
y, y' ∈ Fix_m have the same multiset, then their exact per-class
multisets {y_i : i ≡ r (mod t)} are D_t-related.

Verification (scripts `wave10_exact_perclass_m8.py`,
`wave10_exact_perclass_m46.py`, plus direct checks below):

| m | scope | fibers | extra (fiber, canon) rows |
|---|---|---|---|
| 4 | full Fix_4, 1,152 pts | 203 | 0 |
| 6 | full Fix_6, 39,200 pts | 3,604 | 0 |
| 8 | full Fix_8, 1,331,712 pts | 85,106 | 0 |
| 12 | mod-81 bad fiber lifts, 36 vectors | 1 | 0 |
| 12 | glued fiber pair (wave 8, task 2) | 1 pair | same canon |

If the exact per-class lemma holds, then Y' = π(Y) exactly
(sums of equal multisets), i.e. d = 0 for that π — Pcarry is
closed as a corollary, with no carry estimate at all. Note the
exact lemma is strictly stronger than Lemma Y and strictly
stronger than the pattern lemma; it is the natural target that
replaces (3). Its proof is open, and it is the single most
valuable next step for Lemma Y: it would close Lemma Y
completely (mod-D and exact together), given the odd-component
vanishing and the 3-component classification already proved.

### 3.3 Targeted exact searches at m ≥ 32 / m = 36: 0 failures

Search design (scripts `wave10_pcarry_m36.py`,
`wave10_p32.cpp` part B): joint CRT lifts with all other
components zero, grouped by sorted multiset, exact Y checked
against a single D_4 orbit.

| m | lifts | groups | pairs checked | exact failures |
|---|---|---|---|---|
| 36 (q₂=128, q₃=729) | 93,312 | 1,491 | 91,821 | 0 |
| 32 (q₂=8192, q₃=9) | 73,728 | 1,664 | 72,064 | 0 |

Mod-D agreement also verified as sanity (0 failures in both).
These are targeted subclasses (other components zero), not
exhaustive global searches — global Fix_36 / Fix_32 enumeration
is infeasible — but they cover the (2,3)-component interaction
that Pmix is about, at larger m than wave 9 (which tested
m = 8, 12 in this class). No exact failure was found.

## 4. What remains, precisely

1. **Prove the per-class pattern lemma** (mod 2^a, any P a power
   of 2): per-class multisets of same-multiset patterns are
   D_4-related. Verified to P = 32 (1,120,284 pairs).
2. **Prove the exact per-class lemma** (any m): exact per-class
   multisets of same-multiset Fix vectors are D_t-related.
   Verified exhaustively at m = 4, 6, 8 and on both known m = 12
   fibers. This single lemma would close Lemma Y and Pcarry.
3. **Compatibility π₂ = π₃ for mod-D Lemma Y in general.**
   Wave 9 closed this at mod-D level for m = 4, 8, 12, 16, 20,
   24, 28 by common-σ searches; the pattern argument gives π₂
   from per-class multisets, but π₃ compatibility in general
   still relies on those searches, not on a proof.
4. **Analytic input:** "v₂(D_m) depends only on v₂(m)" (LTE in
   Z[√2]) to be written out in full, for the pattern reduction.
5. **Not needed anymore:** dihedral-τ and affine-τ forms of the
   argument (both refuted above); H_t d = ΔW carry bounding
   (stalls at O(m)); moments/symmetric functions and pairNum as
   separators (already dead, wave 6–7).

## 5. Files (workspace only; repository untouched, Lean not built)

- `methods/wave10_pattern_dihedral.py` — §1.1 test
- `methods/wave10_pattern_affine.py` — §1.2 test (P ≤ 16)
- `methods/wave10_perclass.py` — §1.3 test (P ≤ 16)
- `methods/wave10_p32.cpp` — §1.2/§1.3 tests at P = 32 and §3.3
  test at m = 32
- `methods/wave10_p32_dump.cpp` — explicit affine-fail pairs
- `methods/wave10_pcarry_m36.py` — §3.3 test at m = 36
- `methods/wave10_exact_perclass_m8.py` — §3.2 test at m = 8
- `methods/wave10_exact_perclass_m46.py` — §3.2 tests at m = 4, 6
- Prior: `methods/wave9_pmix_report.md`,
  `methods/wave8_lemmaY_proof_attempt.md`
