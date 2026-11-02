# New separation principle to replace O* — working note (not a proof, not for main)

Task: wave 6, task 2. O* (affine separation) is dead in general: it holds at
m = 8, 9, 10, 11 and fails at m = 12 (explicit pair y, y′ below). Question:
is there a computable invariant I(y) that separates distinct Γ-orbits
inside one fiber (sorted(y) class), where modeSum cannot?

## 0. What the separator must and must not be

Definitions (as in M08 / O* / O′ notes): `Fix_m = ker(H_m mod D_m)`,
`H_m = 6I − C − Cᵀ`, fiber = `sorted(y)` class, Γ = dihedral index
permutations `j ↦ ±j + k`. A separator for 152 must be:

- Γ-invariant: `I(γy) = I(y)` for γ ∈ Γ (else it does not even respect
  the orbits it is supposed to separate);
- NOT S_m-invariant: any function constant on the whole fiber is useless
  inside the fiber.

Two candidates from the task are dead **by definition**, no computation needed:

- **Moments / power sums Σ_j y_j^k, for ANY k, including k beyond the
  Newton range.** The fiber IS the S_m-orbit of y (sorted class), so every
  symmetric function of the coordinates is constant on the fiber. Newton
  already gives the full multiset from p_1..p_m; no symmetric function can
  add information inside a fiber. This candidate is not "untested", it is
  impossible.
- **Any function of modeSum alone.** modeSum determines the multiset
  (Newton), hence any function of modeSum is fiber-constant. A separator
  must use information beyond modeSum. Consequence for 152: the proof chain
  cannot be repaired by keeping the hypothesis "equal modeSum" and only
  changing the conclusion — the chain must either add a hypothesis
  (equal I) or show that the ω-decay step kills pairs with different I
  (see §5). This point is independent of which I is chosen.

## 1. The quotient vector w — the mechanism

For y ∈ Fix_m, `H_m y` is divisible by D_m, so

```
w_y := (H_m y) / D_m   (integer vector)
```

is well defined. Two elementary facts, both proved in one line:

- **Bound:** `H y` has entries in (−2D, 6D) (since y_j ∈ [0, D)), and they
  are multiples of D, so `w_j ∈ {−1, 0, 1, 2, 3, 4, 5}` for EVERY m.
  Hence `sorted(w)` takes only C(m+6, 6) possible values — polynomial in m,
  while |Fix_m| grows exponentially. This is a counting tension for any
  general-m theorem based on sorted(w) alone (see §5).
- **Orbit equivalence (tautology, not a principle):** H commutes with Γ
  (circulant, symmetric), and H is invertible over ℚ (det = D ≠ 0), so
  `y′ ∈ Γy ⟺ w_{y′} ∈ Γw_y`. Hence the Γ-canonical of w separates
  perfectly — but that is just orbit computation in linearly transformed
  coordinates, not a new principle. It is used below only as a sanity
  check. The non-trivial candidates are the COARSE invariants of w:
  `sorted(w)`, and the correlation `⟨y, w⟩`.

Neighbour sum identity (cyclic indices, exact integers): from
`y_{j+1} = 6y_j − y_{j−1} − D w_j`, summing `y_j·y_{j+1}` cyclically,

```
S1 := Σ_j y_j y_{j+1}  =  3·p2 − (D/2)·⟨y, w⟩,   p2 := Σ_j y_j².
```

`p2` is symmetric, hence fiber-constant. So **all of S1's separating power
is exactly ⟨y, w⟩**. Verified numerically on the m = 8 example below.
S1 is Γ-invariant by construction (a cyclic adjacent sum); modulo D it
is a quadratic form in the initial pair (y_0, y_1), since the sequence is
linear in (y_0, y_1) over ℤ/D.

Why w should carry orbit information: bad fibers are torsion lifts
`y = c·z` (m = 8: c = 55488 = D/24; m = 12: lift from mod 81). Then
`w_y = (H z)/(D/c)` is a SMALL vector encoding the lift, and the two
Γ-orbits inside a bad fiber correspond to different lifts/multipliers
whose w-multisets differ. w is already a project object: it is the `w`
in the O′ support criterion (`w = (H·lift(y))/D`).

## 2. Exhaustive test at m = 8 — w_sorted and S1 separate PERFECTLY

Script: `sep_m8_test.py`, result: `sep_m8_result.json`.
Enumeration: all 1,331,712 points of Fix_8 (CRT over 9·289·512), 85,106
fibers, 85,145 Γ-orbits, 39 Γ-bad fibers (reproduced). For each invariant
we count distinct (fiber, invariant) classes: perfect separation means
this count equals 85,145 (one class per Γ-orbit); a fiber-constant
invariant gives 85,106 (one class per fiber).

| invariant | distinct values | fiber-classes | fail fibers (all / bad) | verdict |
|---|---|---|---|---|
| sorted(w) | 2,055 | 85,145 | 0 / 0 | SEPARATES ALL |
| S1 = Σ y_j y_{j+1} | 17,809 | 85,145 | 0 / 0 | SEPARATES ALL |
| S1+S2 | 55,230 | 85,145 | 0 / 0 | SEPARATES ALL |
| S1+S2+S3 | 55,247 | 85,145 | 0 / 0 | SEPARATES ALL |
| adjacency pair multiset (bad only) | — | — | 0 / 39 | SEPARATES BAD |
| adjacency diff multiset (bad only) | — | — | 2 / 39 | ALMOST |
| Γ-canon of w | 85,145 | 85,145 | 0 / 0 | tautology (§1) |
| sorted pairNums (z_γ·y over γ∈V4) | 2,047 | 85,106 | 39 / 39 | DEAD, fiber-constant |
| sorted pairNums mod D | 3 | 85,106 | 39 / 39 | DEAD, fiber-constant |
| support passcount #{γ: 2Q_γ−pair_γ ≡ 0 mod D} | 3 values: 4 (998,784 pts), 8 (249,696), 16 (83,232) | 85,106 | 39 / 39 | DEAD as separator |

All separating invariants above are constant on Γ-orbits (checked:
distinct (Γ-orbit, invariant) pairs = 85,145 in each case), so the
separation is genuine, not an artefact of a non-invariant function.

m = 8 first bad fiber (M08_BAD_M8.json ex. 0), key
(0, 55488, 332928, 610368, 665856, 721344, 998784, 1276224):

- y  = (0, 1276224, 998784, 721344, 665856, 610368, 332928, 55488)
- y′ = (0, 721344, 332928, 1276224, 665856, 55488, 998784, 610368)
- w_sorted: y → (−1, 0, 1, 2, 2, 2, 3, 5); y′ → (−1, −1, 0, 2, 2, 3, 4, 5) — differ
- S1: y → 3103549489152; y′ → 2216821063680 — differ
  (p2 identical = 4076487622656; ⟨y,w⟩ = 13705536 vs 15037248 — differ,
  as §1 predicts)
- pair_sorted: IDENTICAL for y, y′ (list in sep_m8_result.json);
  pair_mod_sorted identical; support passcount 4 = 4 — do not separate.

## 3. The m = 12 counterexample pair — w_sorted and S1 separate it too

Script: `sep_m12_pair_test.py`, result: `sep_m12_pair_result.json`.
Pair (wave-4 O* kill, both outside supp φ̂₁₂, same sorted multiset,
distinct affine canons, D = 1536796800):

- y  = (1366041600, 1366041600, 683020800, 1195286400, 341510400, 853776000,
        170755200, 170755200, 853776000, 341510400, 1195286400, 683020800)
- y′ = (1366041600, 1195286400, 1195286400, 1366041600, 853776000, 683020800,
        170755200, 341510400, 341510400, 170755200, 683020800, 853776000)

| invariant | y | y′ | separates? |
|---|---|---|---|
| sorted(w) | (0,0,0,0,1,1,3,3,4,4,4,4) | (0,0,1,1,2,2,2,2,3,3,4,4) | YES |
| S1 | 7085233213470720000 | 8659729483130880000 | YES |
| S2, S3, S6 | equal | equal | NO |
| sorted pairNums (exact) | identical list (multiples of D: 0, 6D, 8D, 9D, 10D, 12D, 18D) | identical | NO |
| pairNums mod D | all 0 | all 0 | NO |
| support passcount | 8 | 8 | NO |
| adjacency pair multiset | differ (full lists in result json) | | YES |
| adjacency diff multiset | differ | | YES |

Note the asymmetry: at m = 8, adjacency diffs failed on 2/39 bad fibers,
but at m = 12 they separate this pair; at m = 12, S2/S3/S6 fail while S1
works. No single neighbour sum is reliable a priori — S1's success at
m = 8 (all fibers) + m = 12 (this pair) is empirical, not structural.

## 4. Dead candidates, stated sharply

- **Moments / power sums / any symmetric function:** impossible (§0).
- **pairNum (exact sorted, mod D) and the support criterion itself:**
  at m = 8 they are constant on EVERY fiber (not just bad ones), and at
  m = 12 they are identical on the counterexample pair. So the support
  criterion cannot separate within a fiber — it can only EXCLUDE whole
  fibers (at m = 8, support is a union of fibers: passcount ∈ {4, 8, 16},
  support = passcount 16, 83,232 points; bad fibers have passcount < 16).
  This is a separate empirical finding worth recording: the V4-pairing
  multiset {z_γ·y : γ} appears to be a function of the fiber alone
  (conjectured identity, not proved here). It kills the task's pairNum
  candidate in the strong sense: pairNum does not even vary inside a
  fiber, so it cannot separate anything there.
- **Adjacency diff multiset:** fails on 2/39 bad fibers at m = 8 — not exact.
- **Adjacency pair multiset:** separates all bad fibers at m = 8 and the
  m = 12 pair, but it is the finest-grained candidate and the least
  theorem-like: recovering a circular sequence from its vertex + edge
  multisets is a reconstruction problem with known non-uniqueness
  phenomena in general, so exactness at larger m is not credible without
  a mechanism. Ranked below sorted(w) and S1.

## 5. Candidate principle, and what it does NOT give for 152

**Candidate P_w (empirical, m-restricted):** for y, y′ ∈ Fix_m,

```
sorted(y) = sorted(y′)  ∧  sorted(w_y) = sorted(w_{y′})   ⟹   y′ ∈ Γy.
```

Status: TRUE at m = 8 for all fibers (exhaustive, §2); consistent with
the one tested pair at m = 12 (separates, §3); unproved for general m,
and the §1 counting bound (only C(m+6, 6) possible sorted(w) values)
means P_w as a general-m theorem would additionally need a bound on the
number of Γ-orbits per fiber — no such bound is known. S1 (equivalently
⟨y, w⟩, §1) is the runner-up with the same empirical status and no
counting obstruction (its range is ~m·D²), but a single integer (a
quadratic form mod D) has no structural reason to be injective on orbits
within a fiber.

Even if P_w (or S1) were proved, it does NOT by itself restore 152's
chain, for the §0 reason: the chain's hypothesis is equal modeSum, and
neither sorted(w) nor S1 is a function of modeSum. One of the following
must additionally hold:

(a) the ω-decay step kills pairs with different w (resp. S1) — i.e. ω
    distinguishes w-classes, not just Γ-orbits; this requires reading
    the actual ω formula in LineDStrongKickConc (from main via connector,
    separate task), not assuming it; or
(b) 152 is restated with the grouping changed from fibers to
    (fiber, w)-classes, and Bsym is recomputed as
    (1/|supp|) Σ over (fiber, w)-classes |class|² — a content change,
    exactly like the Aff restatement, not a silent repair; or
(c) the O′ route is kept: on supp, fibers do not split at all at m = 8
    (and the m = 12 counterexample pair is outside supp), so for 152
    what is actually needed is O′ (fiber ⇒ Γ-orbit ON SUPP), and P_w
    is one possible route to proving O′ rather than a replacement for
    the whole separation step.

The tautological exact separator (Γ-canon of w, or of y) gives a
computational route to Bsym (enumerate orbits directly, as the replays
already do) but no Lean theorem: the theorem content is precisely the
non-trivial separation statement.

## 6. Next informative steps (in order)

1. Test sorted(w) and S1 on Γ-bad fibers at m = 9 (Fix_9 = 7,761,796
   points — chunked numpy or C++ feasible) and on further m = 12 bad
   fibers from components (the mod-81 fiber has 3 affine canons; check
   their Γ-splitting and w/S1 values). A single w_sorted collision
   inside a fiber at m = 9 or 12 kills P_w as stated and demotes it to
   an m = 8 curiosity.
2. Find the reason pair_sorted is fiber-constant (conjectured identity
   in §4) — if proved, it explains why support is a union of fibers
   at m = 8 and closes the pairNum line of inquiry properly.
3. Read the ω formula from main (connector only) and check whether
   ω(ξ, ξ′) distinguishes w-classes (§5a) — this decides whether P_w
   can enter 152 at all, or whether only route (b)/(c) is available.
4. Bound Γ-orbits per fiber (needed for any general-m P_w claim, §5).

## Files

- `sep_m8_test.py`, `sep_m8_test.log`, `sep_m8_result.json` — exhaustive m = 8 test
- `sep_m12_pair_test.py`, `sep_m12_pair_result.json` — m = 12 pair test
- This note: `sep_new_principle_note.md`

Repository untouched; Lean not built; enumeration is a verifier artefact,
not a proof and not a Lean theorem.
