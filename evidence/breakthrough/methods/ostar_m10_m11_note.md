# O* at m=10 and m=11 — working note (not a proof for general m, not a Lean theorem)

Conventions (as in the wave-3 O* test and the wave-4 gluing note):
`Fix_m = ker(H_m mod D_m)`, `H_m = 6I - C - C^T`, i.e. a vector satisfies
`6y_i - y_{i-1} - y_{i+1} = 0 mod q` cyclically. A fiber is a `sorted(y)`
class. The affine group is `p(j) = a*j + b mod m`, `a in (Z/m)^x`,
acting by `(p.y)_j = y_{p(j)}`. Separation reading (R) is the claim
tested: every fiber is contained in a single affine orbit (equivalently,
two vectors in one fiber have the same affine canonical form, the
lexicographic minimum over Aff). The strict reading (fiber = full affine
orbit) is already false at m=8 and is not tested here. All enumeration
is exact integer arithmetic; it is a verifier artefact, not a Lean
theorem. Grounding caveat: this task reuses the H_m / Fix / affine
conventions of the wave-3 O* test (verified against main `6dbcc7a`);
it does not itself re-fetch main, and a HEAD move reported by another
branch (`d87dce0`, PR #76) was not checked here.

## Verdict

- **m=10: O* separation HOLDS** (per-component separation + Tag A +
  Tag B + exhaustive C++ search over the remaining 3,470,912 vectors,
  reduced to 184,590 dihedral-orbit representatives: 0 hits).
- **m=11: O* separation HOLDS** (per-component separation + a short
  argument: distinct-component case, one-nonconstant-component case,
  and the reflection-pair argument below; no brute-force global search
  needed, and targeted samples agree).
- **The m=12 torsion-lift kill does NOT reproduce at m=10 or m=11:**
  no prime-power component has an aff-bad fiber at either m, so there
  is no mod-q bad fiber to lift. The m=12 kill came from a mod-81
  fiber whose values are all multiples of 9 (a lift of a mod-9 kernel
  vector). At m=10/11 the components are instead period vectors
  (period 2 / period 5) and reflection-symmetric vectors, whose value
  partitions are algebraic (parity / mod-5 / reflection orbits), and
  the tag arguments below go through.
- **Status for 152:** O* separation now survives at m = 8, 9, 10, 11
  and fails at m = 12. Any use of O* in 152 must still be
  m-restricted (m ≤ 11 on current evidence) or replaced by a
  different separation principle; it cannot be asserted for general
  m. Next informative cases: m = 13, and whether the m = 12
  counterexample lies in the support of φ̂₁₂ (the O'-style
  restriction at m = 12, flagged already in the wave-4 note).

## Step 1 — per-component separation: 0 aff-bad fibers everywhere

`D_10 = 45239072 = 2^5 * 29^2 * 41^2`; `D_11 = 263672644 = 2^2 * 23^2 * 353^2`.
`Fix mod q` was enumerated by solving `(A^m - I) v = 0 mod q`,
`A = [[0,1],[-1,6]]`, iterating one coordinate and solving the linear
congruence for the other (no `q^2` scan; code reused from
`gluing_components.py`). `H v = 0 mod q` was verified for every vector.

| m | q | \|Fix\| | fibers | aff-bad | periods (minimal) | distinct-valued | repeated |
|---|---|---|---|---|---|---|---|
| 10 | 32 | 32 | 18 | 0 | 1: 4, 2: 28 | 0 | 32 |
| 10 | 841 | 841 | 57 | 0 | 1: 1, 10: 840 | 560 | 281 |
| 10 | 1681 | 1681 | 189 | 0 | 1: 1, 5: 1680 | 0 | 1681 |
| 11 | 4 | 4 | 4 | 0 | 1: 4 (all constant) | 0 | 4 |
| 11 | 529 | 529 | 36 | 0 | 1: 1, 11: 528 | 286 | 243 |
| 11 | 124609 | 124609 | 5841 | 0 | 1: 1, 11: 124608 | 120736 | 3873 |

Fiber-size distributions: m=10 q32: 1:4, 2:14; q841: 1:1, 10:28,
20:28; q1681: 1:1, 5:40, 10:148. m=11 q4: 1:4; q529: 1:1, 11:22,
22:13; q124609: 1:1, 11:352, 22:5488.

## Step 2 — A(v) = D(v) for every component vector

For each component vector `v`, let `A(v) = {p.v : p in Aff, p.v in Fix
mod q}` (distinct vectors) and `D(v) = {d.v : d in Dihedral}` (dihedral
always preserves Fix, since H is cycle-symmetric). **A(v) = D(v) as
sets for every vector at both m** (0 vectors with A ≠ D). Hence any
candidate in the same global fiber is a *dihedral*-effect combination:
if `y'` has the same global sorted multiset as `y`, then per
component `v'_i` has the same sorted multiset as `v_i` (projection of
a multiset), so by Step 1 `v'_i` is affine-equivalent to `v_i`, and
by A = D, `v'_i = d_i . v_i` for some dihedral `d_i`.

A-size (= D-size) distributions: m=10 q32: 1:4, 2:28; q841: 1:1,
10:280, 20:560; q1681: 1:1, 5:200, 10:1480. m=11 q4: 1:4; q529: 1:1,
11:242, 22:286; q124609: 1:1, 11:3872, 22:120736.

## Step 3 — value partitions are exactly stabiliser orbits

For every component vector, the partition of positions by equal value
equals the orbit partition of its dihedral stabiliser (verified for
100% of vectors, both m):

- m=11, q529/q124609, repeated non-zero vectors: exactly 6 distinct
  values (242 / 3872 vectors) — one reflection fixed point + 5 pairs.
  Distinct vectors: 11 distinct values. Zero: 1 value. Stabiliser of
  a non-constant vector is exactly `{e, r}` for one reflection `r`
  (a non-trivial rotation stabiliser would force constancy, since
  11 is prime; the stabiliser has order 22/11 = 2).
- m=10, q841, repeated non-zero vectors: 5 distinct values (140
  vectors, reflection with 0 fixed points: 5 pairs) or 6 distinct
  values (140 vectors, reflection with 2 fixed points: 2 singletons
  + 4 pairs). Distinct vectors: 10 values. Stabiliser order 2
  (orbit size 20/10 = 10).
- m=10, q1681: every vector has period 5 (1681/1681). Pattern = first
  5 values; pattern distinct counts: 1: 1 (zero), 3: 200 (pattern
  reflection-symmetric; A-size 5), 5: 1480 (pattern injective;
  A-size 10).
- m=10, q32: every vector has period 2; first-2 distinct counts:
  1: 4 (constants), 2: 28 (parity tag exact: the two values differ).

## m=11 — the reflection argument (complete)

Let `y` be global (tuple representation over components
4 / 529 / 124609; CRT from triples to integers mod D is a per-position
bijection, so sorted-multiset equality of integers is sorted-multiset
equality of triples, and affine equivalence is the same in both
pictures). Let `y'` be in the same fiber. By Steps 1–2,
`v'_i = d_i . v_i` with `d_i` dihedral. Multiset equality gives a
position permutation `sigma` with `v_i_{sigma(j)} = v'_i_j` for all
`i, j`.

- If some component `v_i` is distinct-valued, then
  `v_i_{sigma(j)} = v_i_{d_i(j)}` forces `sigma(j) = d_i(j)` for all
  `j`, so `y' = d_i . y` globally (for other components,
  `v'_k_j = v_k_{sigma(j)} = v_k_{d_i(j)}`), and `d_i` is affine. Done.
- If no component is distinct-valued: q4 components are constant and
  invariant under every permutation. If exactly one of q529/q124609
  is non-constant, `y' = d . y` with `d` that component's dihedral
  perm (constants invariant). If both are non-constant, both are
  reflection-symmetric (Step 3). Their dihedral orbits equal their
  rotation orbits (size 11: rotation stabiliser is trivial for
  non-constant vectors, rotation orbit ⊆ dihedral orbit, both
  size 11), so `d_i . v_i = rot^{k_i} . v_i` for shifts `k_i`, i.e.
  `v'_i_j = v_i_{j+k_i}`. Let `r_i(j) = b_i - j` be the stabiliser
  reflection of `v_i`. Since value classes are exactly reflection
  orbits (Step 3), `v_i_{sigma(j)} = v_i_{j+k_i}` gives
  `sigma(j) ∈ {j+k_i, b_i - j - k_i}` for `i = 1, 2` and every `j`.
  Hence for every `j` the intersection
  `{j+k_1, b_1-j-k_1} ∩ {j+k_2, b_2-j-k_2}` is non-empty. The four
  possible equalities are: `k_1 = k_2`; `b_1-k_1 = b_2-k_2`;
  `2j = b_2-k_1-k_2`; `2j = b_1-k_1-k_2`. The last two each hold for
  exactly one `j mod 11` (2 is invertible mod 11). If neither of
  the first two holds, at most 2 of the 11 positions `j` could have
  non-empty intersection — contradiction. So either `k_1 = k_2 = k`,
  in which case `y' = rot^k . y` globally (rotation, hence affine);
  or `b_1-k_1 = b_2-k_2 =: c`, in which case `p(j) = c - j` satisfies
  `(p.y)_i_j = v_i_{c-j} = v_i_{r_i(j+k_i)} = v_i_{j+k_i} = v'_i_j`
  (using `c-j = b_i-k_i-j = r_i(j+k_i)` and `r_i`-invariance of
  `v_i`), so `y' = p . y` globally (reflection, hence affine).
  In all cases `y'` is globally affine-equivalent to `y`. ∎
  (The remaining subcase, all components constant/zero, has
  singleton fibers directly.)

## m=10 — Tag A, Tag B, and the C++ search over the remainder

- **Tag A (q841 distinct, 560 vectors):** same distinct-component
  argument as m=11 case 1: `sigma = d_841`, so `y' = d_841 . y`.
- **Tag B (q32 non-constant AND q1681 pattern distinct):**
  q32 values depend only on parity (exact, Step 3) and q1681 values
  only on `j mod 5` (exact, pattern injective). Multiset equality
  gives `sigma` with `sigma(j) ≡ d_32(j) (mod 2)` and
  `sigma(j) ≡ d_1681(j) (mod 5)`. Dihedral perms satisfy
  `d(j) = εj + b mod 10`, `ε = ±1`; mod 2, `εj + b ≡ j + b`
  (since `-1 ≡ 1 mod 2`); mod 5, `d_1681(j) ≡ ε_1681 j + b_1681`.
  By CRT, `sigma(j)` is forced to be `p(j) = a j + b mod 10` where
  `a ≡ 1 (mod 2)`, `a ≡ ε_1681 (mod 5)` — i.e. `a = 1` if
  `ε_1681 = 1`, `a = 9` if `ε_1681 = -1` (units mod 10 are 1, 3, 7,
  9 with mod-5 residues 1, 3, 2, 4) — and `b` is the CRT combination
  of `b_32 mod 2` and `b_1681 mod 5`. So `p` is dihedral (hence
  affine) and `sigma = p` as functions; then `y' = p . y` (for
  q32/q1681 by the parity/mod-5 congruences, for q841 because
  `v_841_{p(j)} = v_841_{sigma(j)} = v_841_{d_841(j)}`). ∎
- **Remainder (C++ search):** NOT Tag A and NOT Tag B, i.e. q841
  non-distinct (281 vectors) AND (q32 constant (4) OR q1681 pattern
  non-distinct (201 vectors: zero + 200 pattern-distinct-3)).
  Count: `281 * (4*1681 + 28*201) = 281 * 12352 = 3,470,912`
  global vectors. The search (`ostar_m10_remaining.cpp`, compiled
  with `-O3`) deduplicates by global dihedral canon (the remainder
  set is dihedral-invariant: distinctness / constancy / pattern
  distinctness are preserved by dihedral perms), leaving **184,590**
  dihedral-orbit representatives, and checks all dihedral-effect
  combinations for each (**17,609,232** combos): a hit would be a
  combination with sorted candidate triples equal to sorted base
  triples but affine tuple-canon different from base affine canon.
  **Result: 0 hits** (run time 2 s for the search itself).
  The C++ result was cross-checked in Python on 200 random
  remaining vectors (19,050 combos, 0 hits), and the m=11
  reflection case was cross-checked on 100 random
  reflection–reflection vectors (12,100 combos, 0 hits); an
  earlier general sample (60 random m=11 vectors, 22,627 combos;
  60 random m=10 Tag-B vectors, 20,200 combos) also gave 0 hits.
  These samples are sanity checks on conventions, not the evidence;
  the evidence is Steps 1–3 + the arguments + the exhaustive C++
  search over the m=10 remainder.

## Files

- `ostar_m10_m11_components.py`, `ostar_m10_m11_components.json` —
  Step 1 (per-component separation; q124609 canon via chunked
  numpy lex-min; vectors saved as `ostar_m11_q124609.npy`).
- `ostar_m10_m11_structure.py`, `ostar_m10_m11_structure.json` —
  Step 2 (A vs D) and periods.
- `ostar_m10_m11_valueclasses.py`, `ostar_m10_m11_valueclasses.json` —
  Step 3 (value partitions vs stabiliser orbits; pattern counts).
- `ostar_m10_m11_samplecheck.py`, `ostar_m10_m11_hardcase_sample.py` —
  sample sanity checks (0 hits).
- `m10_q32.txt`, `m10_q841.txt`, `m10_q1681.txt` — component vectors
  used by the C++ search.
- `ostar_m10_remaining.cpp`, `ostar_m10_remaining_result.json`,
  `ostar_m10_remaining.log` — C++ remainder search (0 hits).
