# O\* at m=13 — separation holds (component level + gluing argument)

## Verdict

**O\* separation HOLDS at m=13.** Every fiber of `Fix₁₃` is contained in a
single affine orbit: any two vectors with the same sorted multiset are
affine permutations of each other. This is the separation reading only.
The strict reading "fiber = full affine orbit" is already false at m=8
(affine permutations with multiplier `a ≠ ±1` generally do not preserve
`Fix`) and was not tested here. O\* therefore now survives at
m = 8, 9, 10, 11, 13 and fails at m = 12; it still cannot be asserted
for general m, and any use in claim 152 must remain m-restricted.

## Conventions (same as the wave-3 O\* test)

- `H = 6I − C − Cᵀ` on `ℤ¹³`, `C` the cyclic shift.
- `D₁₃ = det H₁₃ = 8957108164 = 2² · 79² · 599²`.
- `Fix₁₃ = ker(H mod D₁₃)`, enumerated via CRT from `Fix mod q` for
  `q ∈ {4, 6241, 358801}`.
- Fiber = class of vectors with the same sorted multiset (`sorted(y)`).
- Affine group: `p[j] = a·j + b mod 13`, `a ∈ (ℤ/13)ˣ`, `b ∈ ℤ/13`
  (156 perms), acting by `y′_j = y_{p[j]}`.
- Dihedral group: rotations `j ↦ j+k` and reflections `j ↦ c−j`
  (26 perms). Dihedral permutations preserve `Fix` setwise (H is
  circulant and reversal swaps `C, Cᵀ`), so every dihedral orbit lies
  inside its fiber.
- A fiber is aff-bad if it contains vectors with more than one affine
  canonical form (lexicographic minimum over the affine group).

## Enumeration method

`Fix mod q` was enumerated without a `q²` scan. With
`M = [[6,−1],[1,0]]`, a sequence satisfying `Hv = 0` is determined by
`(v₀,v₁)` and is in `Fix` iff `(M¹³ − I)(v₀,v₁)ᵀ = 0 mod q`.
For each `v₀ ∈ ℤ/q` the first equation was solved as a linear
congruence in `v₁` (all solutions, via gcd), the second equation was
checked, and `Hv ≡ 0 mod q` was asserted for every vector produced.
`M¹³` over ℤ and `K = M¹³ − I` are printed by the script; `|Fix mod q| = q`
for all three components, as at m = 9, 10, 11.

Scripts: `ostar_m13_components.py`, `ostar_m13_structure.py`.
Results: `ostar_m13_components.json`, `ostar_m13_structure.json`.

## Component results: 0 aff-bad fibers everywhere

| q | \|Fix\| | fibers | fiber sizes | aff-bad |
|---|------|--------|-------------|---------|
| 4 | 4 | 4 | 1: 4 | 0 |
| 6241 = 79² | 6241 | 280 | 1: 1, 13: 78, 26: 201 | 0 |
| 358801 = 599² | 358801 | 14100 | 1: 1, 13: 598, 26: 13501 | 0 |

## Structure: only three vector types (verified for 100% of vectors)

For each vector: distinct-value count, multiplicity pattern, fiber size,
number of reflections fixing it, number of nontrivial rotations fixing it.

| type | distinct | multiplicities | fiber | refl fixing | rot fixing | count q=6241 | count q=358801 |
|------|----------|---------------|-------|-------------|------------|--------------|----------------|
| constant | 1 | (13,) | 1 | 13 | 12 | 1 | 1 |
| reflection | 7 | (1,2,2,2,2,2,2) | 13 | exactly 1 | 0 | 1014 = 78·13 | 7774 = 598·13 |
| distinct | 13 | (1,…,1) | 26 | 0 | 0 | 5226 = 201·26 | 351026 = 13501·26 |

q=4 contributes only the 4 constant vectors.

## Step 1: A(v) = D(v) in effect, for every component vector

Aff-bad = 0 means: a fiber = (affine orbit ∩ Fix) for its vectors.
Dihedral orbit ⊆ fiber, and its size is `26 / |stabiliser|`:

- distinct vector: stabiliser trivial (a rotation fixing it would force
  constancy since 13 is prime; a reflection fixing it would force a
  repeated value) — computed directly as refl 0, rot 0 — orbit size 26
  = fiber size, hence dihedral orbit = fiber;
- reflection vector: stabiliser exactly `{id, r}` (computed: exactly 1
  reflection fixes it, 0 nontrivial rotations; two distinct fixing
  reflections would compose to a nontrivial fixing rotation) — orbit
  size 13 = fiber size, hence dihedral orbit = fiber;
- constant vector: orbit size 1 = fiber size.

So every affine permutation that lands a Fix vector back in Fix has a
dihedral effect: for each component vector `v` and each affine `p` with
`p·v ∈ Fix`, there is a dihedral `d` with `d·v = p·v`.

## Step 2: gluing — no counterexample at m=13

Let `y, y′ ∈ Fix₁₃` have the same global sorted multiset. By CRT,
`y` is the triple `(y₄, y₆₂₄₁, y₃₅₈₈₀₁)`, and `y′` is likewise.
Per component, `y′ᵢ` lies in the fiber of `yᵢ`, hence (Step 1)
`y′ᵢ = dᵢ·yᵢ` for dihedral `dᵢ`. Also, multiset equality gives a
position permutation `σ` with `y′_j = y_{σ(j)}` for all positions `j`
(triple equality), hence per component `yᵢ_{σ(j)} = yᵢ_{dᵢ(j)}`.

Case A — some component is distinct-valued. Distinctness forces
`σ(j) = dᵢ(j)` for all `j` (from `yᵢ_{σ(j)} = yᵢ_{dᵢ(j)}`), so
`σ = dᵢ` as a permutation and `y′ = dᵢ·y` globally: dihedral, hence
affine. Done.

Case B — no component is distinct-valued. Each nonconstant component
is reflection-type. For a reflection-symmetric vector `v` with symmetry
`r₀(j) = c₀ − j`, a reflection `ref_c` has the same effect as the
rotation `rot^{c₀−c}`: `(ref_c·v)_j = v_{c−j} = v_{c₀−(c−j)} = v_{j+c₀−c}`.
So each `dᵢ` acts as a rotation `rot^{kᵢ}` on its component, and
constant components are unaffected by any permutation. If at most one
component is nonconstant, `y′ = rot^{k}·y` globally. Otherwise the two
nonconstant components are the mod-6241 and mod-358801 ones; write
their symmetries as `rᵢ(j) = cᵢ − j`. Value equality in component `i`
is exactly `b = a` or `b = rᵢ(a)` (pattern 1+6×2), so
`σ(j) ∈ {j+kᵢ, rᵢ(j+kᵢ)}` for both `i`. The intersection over the two
components can be nonempty only via:

- direct–direct: `j+k₁ = j+k₂`, i.e. `k₁ = k₂`;
- cross–cross: `c₁−(j+k₁) = c₂−(j+k₂)`, i.e. `c₁−k₁ = c₂−k₂` for all `j`;
- direct–cross: `j+k₁ = c₂−(j+k₂)`, i.e. `2j = c₂−k₁−k₂` — exactly one `j`
  (2 is invertible mod 13);
- cross–direct: `c₁−(j+k₁) = j+k₂`, i.e. `2j = c₁−k₁−k₂` — exactly one `j`.

If `k₁ = k₂ = k`, then `y′ = rot^{k}·y` globally. If
`c₁−k₁ = c₂−k₂ =: c*`, then `σ(j) = c*−j` works for both components
(`yᵢ_{c*−j} = yᵢ_{rᵢ(j+kᵢ)} = yᵢ_{j+kᵢ}`), so `y′ = ref_{c*}·y` globally:
again dihedral. If neither holds, then for every `j` the intersection
is empty except possibly at the two single positions from the
direct–cross / cross–direct equalities — but `σ` must be defined at
all 13 positions, contradiction. Hence no gluing counterexample exists.

Case C — all components constant: `y′ = y` trivially.

Therefore every global fiber is a single dihedral (hence affine) orbit:
O\* separation holds at m=13.

## Why the m=12 kill does not reproduce here

The m=12 kill came from a mod-81 fiber whose vectors are all multiples
of 9 — a torsion lift with no analogue in the m=13 components: the
only repeated component type at m=13 is the reflection type, whose
value partition (1 singleton + 6 pairs) glues cleanly by the argument
above, and no component has an aff-bad fiber to lift.

## Caveats and next steps

- Exact finite checking plus the short arguments above; not a Lean
  theorem and not a proof for general m. Status for 152 remains:
  O\* separation may be used only with an explicit m-restriction
  (current evidence: m ≤ 11 and m = 13; m = 12 fails; m ≥ 14 untested).
- Conventions (H, Fix, affine action) are those of the wave-3 O\* test;
  they were not re-fetched against the current main HEAD in this task,
  so recheck against the then-current HEAD before any main-bound use.
- Next informative steps: m = 14 (composite, new torsion phenomena
  possible), and the general-m separation principle to replace O\*
  (which is now known to fail at m = 12, so no general-m O\* theorem
  is possible).
