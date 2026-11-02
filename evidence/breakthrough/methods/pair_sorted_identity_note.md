# Why pair_sorted is fiber-constant — the identity, and its one remaining gap

Task: wave 7, task 2. Working note (not a Lean theorem, not for main).
Repository untouched; Lean not built; enumerations are verifier artefacts.

## Verdict

**The identity is found, and it is not "pairNum depends only on the multiset"
by magic — it is a class-sum identity.** In one line:

> `pairNum(z, w_y) = z̄ · Y(y)`, where `Y(y)` is the vector of sums of `y`
> over the `+4`-orbits of the index set, `z̄` is the corresponding class
> vector of the torsion representative `z`, and the set `{z̄}` is invariant
> under the dihedral group `D_t` (`t = gcd(m,4)`) that affine permutations
> induce on the classes.

Consequences, stated precisely (see §5 for what is proved vs verified):

- **Unconditional theorem (all m):** if `y' = σ(y)` for an affine permutation
  `σ(j) = aj + b`, `a ∈ (ℤ/m)ˣ`, then `pair_sorted(y') = pair_sorted(y)`.
- **Unconditional theorem (m odd):** `pair_sorted` is fiber-constant, because
  then `V4` consists only of constant vectors and every pair value is `a·Σy`.
- **Conditional theorem (all m):** `pair_sorted` is fiber-constant **iff**
  the class-sum lemma below (Lemma Y) holds: within a fiber, `Y(y')` is
  always a `D_t`-permutation of `Y(y)`. Lemma Y is **verified exhaustively**
  at m = 4, 6, 8 and on the complete m = 12 bad fiber, but **not proved
  in general**. So full fiber-constancy is proved modulo Lemma Y, not
  proved outright. Anyone claiming it for general m without Lemma Y is
  over-claiming.
- **Support corollary (wherever pair constancy holds):** the support
  criterion is fiber-constant, so `supp φ̂` is a union of fibers. This is
  exactly why pairNum can never separate inside a fiber, and why the O′
  route (exclude whole fibers) is the only support-based route.

## 0. Definitions, reconciled with current main

Re-fetched from `ChurilovMaksim/BGS` at HEAD
`d87dce0d9277579568edfee6cffecbc96ea61024` via the GitHub connector
(`formalization/Bgs/LineDOrbitPairFull.lean`, blob SHA
`dff625c15c61b5fe846a9ec124dc0c601f601285`, unchanged from `6dbcc7a`):

- `pairNum m y w = (Xmat m *ᵥ y) ⬝ᵥ w`, `Qnum m y = pairNum m y y`,
  `Xmat` = adjugate of `Hmat`, so `Hmat *ᵥ Xmat = Dm • 1` and
  `Xmat *ᵥ Hmat = Dm • 1` (main: `Hmat_mul_Xmat`).
- `torsionSubgroup m = {γ : 4 • γ = 0}` in `Vquot m = ℤ^m / H_m ℤ^m`;
  `torsionToV4` / `v4ToTorsion` are inverse bijections with `V4 m`.
- `phiSummand m s w η = e((2s·Qnum m y − pairNum m y w)/Dm)` for a
  representative `y` of `η`; `phihat` is the average over `η`.

Scripts' conventions (identical content, different normalisation):

- `Fix_m = ker(H_m mod D_m)`, `H = 6I − C − Cᵀ`, i.e.
  `(Hy)_i = 6y_i − y_{i−1} − y_{i+1}`, indices mod m.
- For `y ∈ Fix_m` (lifted to representatives `0 ≤ y_i < D_m`),
  `w_y := (Hy)/D_m ∈ ℤ^m` (well defined since `D_m | (Hy)_i`).
- `V4` = `ker(H mod 4)` in `(ℤ/4)^m`, lifted to representatives
  `v_i ∈ {0,1,2,3}`; torsion representatives `z := (Hv)/4 ∈ ℤ^m`.
  This is exactly main's `v4ToTorsion` representative
  `(Hmat *ᵥ lift v)/4`. The set `Z` of these `z` is one representative
  per torsion class (main: `|torsion| = |V4|`).
- `pair_sorted(y) := sorted( z · y : z ∈ Z )` (exact integers).

Representative caveat: if `z` is replaced by `z + Ht`, then
`z·y` changes by `t·(Hy) = D_m·(t·w_y)`, a multiple of `D_m`.
So **exact** `pair_sorted` is a statement about the script's canonical
lifts `v ∈ {0,1,2,3}^m`; **`pair_sorted mod D_m` is intrinsic**
(representative-independent), and that is the version the support
criterion uses. Everything below is proved for the canonical lifts;
the mod-`D_m` corollary needs no choice.

## 1. Step 1 — the adjugate identity

For `z ∈ Z` and `y ∈ Fix_m`, with `w = w_y`:

```
pairNum(z, w) = (Xz) ⬝ w = z ⬝ (Xw) = z ⬝ y.
```

Proof: `X` is symmetric (`Xmat_transpose` in main), so
`(Xz)·w = z·(Xw)`; and `Xw = X(Hy/D_m) = (XH y)/D_m = (D_m y)/D_m = y`
since `XH = D_m·I`. Hence the support summand's pair term is literally
the dot product `z·y`, and `pair_sorted` is the multiset of these dots
over the torsion representatives. (The scripts compute it this way
directly: `pts @ Z.T`.)

## 2. Step 2 — V4 is an arithmetic progression

Let `v : ℤ/m → ℤ/4` satisfy `Hv = 0` in `ℤ/4`. Pointwise,
`6v_i − v_{i−1} − v_{i+1} = 0` in `ℤ/4`; since `6 ≡ 2 (mod 4)`,
`v_{i+1} = 2v_i − v_{i−1}`, i.e. the second difference vanishes.
Hence for some `a, d ∈ ℤ/4`,

```
v_i = a + i·d   in ℤ/4,   with m·d = 0 in ℤ/4   (cyclicity).
```

Conversely every such `(a, d)` gives a `V4` element. Therefore

| m mod 4 | allowed d | \|V4\| |
|---|---|---|
| odd | d = 0 | 4 |
| 2 mod 4 | d ∈ {0, 2} | 8 |
| 0 mod 4 | d ∈ ℤ/4 | 16 |

This matches every enumeration in the programme (m = 8: 16, m = 12: 16,
m = 6: 8, m = 4: 16, and main's remark `|V4 7| = 4`).

## 3. Step 3 — torsion representatives are 4-periodic, and class sums

Lift `v` to `v̄_i ∈ {0,1,2,3}` (the residue `a + id mod 4`).
Then `v̄_{i+4} = v̄_i` as a function on `ℤ/m` (adding 4, or 4−m on wrap,
changes `id` by a multiple of 4, and `md = 0` kills the wrap term).
Since `H` is translation-invariant, `z = (Hv̄)/4` also satisfies
`z_{i+4} = z_i` for all `i ∈ ℤ/m`.

Let `t = gcd(m, 4) ∈ {1, 2, 4}`. The `+4`-action on `ℤ/m` has exactly
`t` orbits `O_r` (`r = i mod t`, well defined since `t | m`), and `z`
is constant on each orbit. Write `z̄_r` for that common value and

```
Y_r(y) := Σ_{i ∈ O_r} y_i,   r ∈ ℤ/t.
```

Then, because `z` is constant on orbits,

```
z · y = Σ_r z̄_r · Y_r(y) = z̄ · Y(y).                (*)
```

So every pair value is a dot product of a fixed class vector `z̄`
with the class-sum vector `Y(y)`. The whole question is therefore
about `Y` and the set `Z̄ = {z̄ : z ∈ Z}`.

### The class vectors, by cases on d

Computing `z̄` from `v̄` (neighbours of class `r` are classes `r±1`):

- **d = 0:** `v̄ ≡ a`, `z̄ = (a, …, a)`, `a ∈ {0,1,2,3}` (constants).
- **d = 2** (m even): `v̄` alternates `a, a+2 (mod 4)`, and
  `z̄ = (α, β, α, β)`-type with
  `(α, β) ∈ {(−1,3), (0,4), (3,−1), (4,0)}`.
  For `t = 2` this is the pair `(α, β)` itself; for `t = 4` it is
  `(α, β, α, β)`.
- **d = ±1** (only when `4 | m`, so `t = 4`): `v̄` cycles through
  `(0,1,2,3)` (d = 1) or `(0,3,2,1)` (d = 3). The class vectors are
  the 4 rotations of `(−1,1,2,4)` (d = 1) and the 4 rotations of
  `(−1,4,2,1)` (d = 3). Note `(−1,4,2,1)` is the reflection
  `(z₀, z₃, z₂, z₁)` of `(−1,1,2,4)`.

Hence, as sets:

- `t = 1` (m odd): `Z̄ = {(0), (1), (2), (3)}`, pair values `a·Σy`.
- `t = 2` (m ≡ 2 mod 4): `Z̄` = 4 constants + 4 alternating pairs.
- `t = 4` (4 | m): `Z̄` = 4 constants + 4 alternating
  `(α,β,α,β)` + 8 cyclic vectors (two rotation orbits). Total 16.

### D_t-invariance of Z̄

Let `D_t` be the dihedral group on the `t` classes: permutations
`r ↦ r + b` and `r ↦ −r + b` (`b ∈ ℤ/t`). Then `Z̄` is `D_t`-invariant:

- constants are fixed by everything;
- alternating pairs swap under `D_2`, and `(α,β,α,β)` goes to
  `(β,α,β,α)` (rotation by 1 / reflection) or itself (rotation by 2),
  both in the set;
- the two rotation orbits for `d = ±1` are swapped by reflection and
  preserved by rotation, so their union is `D_4`-invariant.

This is a finite case check on `(a, d)` (≤ 16 patterns), no enumeration
of `Fix` needed. It is the whole content of "the torsion side is
symmetric enough" — and it is the **only** symmetry the torsion side has:
`Z̄` is *not* invariant under the full symmetric group `S_t` (e.g.
`(4,2,1,−1)` with its first two entries swapped is not in `Z̄`).

## 4. Step 4 — the unconditional affine-pair theorem

Let `σ(j) = aj + b` with `a ∈ (ℤ/m)ˣ`, acting by `(σ·y)_j = y_{σ(j)}`
(the convention of `gluing_components.aff_perms` / `canon`).
Then `σ` sends class `O_r` to class `O_{ar+b}`: indeed `a` is odd, so
`a ≡ ±1 (mod 4)` when `t = 4`, `a ≡ 1 (mod 2)` when `t = 2`, and the
map `r ↦ ar + b` is in `D_t` (for `t = 2`, `D_2` is both permutations).
Hence `Y(σ·y)` is a `D_t`-permutation of `Y(y)`. By (*) and `D_t`-
invariance of `Z̄`,

```
{ z̄ · Y(σ·y) : z̄ ∈ Z̄ } = { z̄ · Y(y) : z̄ ∈ Z̄ },
```

i.e. **`pair_sorted(σ·y) = pair_sorted(y)` for every affine `σ`**.
This needs no assumption about `y ∈ Fix` beyond the definition of
`Y`, and no enumeration. In particular it explains the m = 12 pair:
the two vectors are not affine-equivalent as whole vectors, but their
class sums *are* `D_4`-related (see §5), so their pair multisets agree.

For `t = 2` the argument simplifies further: the alternating dots are
`α·E + β·O` with `E = Y₀, O = Y₁`, `E + O = Σy`, and the four values
`{3S−4E, 4S−4E, 4E−S, 4E}` depend only on the unordered pair `{E, O}`.
For `t = 1` there is nothing to prove beyond `a·Σy`.

## 5. Step 5 — Lemma Y: the one remaining gap, and its verification

**Lemma Y.** If `y, y' ∈ Fix_m` and `sorted(y') = sorted(y)` (same fiber),
then `Y(y') ∈ D_t · Y(y)` (the class-sum vector is permuted by a
dihedral class permutation).

Given Lemma Y, Step 4's argument with `Y(y')` in place of `Y(σ·y)`
gives full fiber-constancy of `pair_sorted` for every m. Without it,
fiber-constancy does not follow from §3 alone: a fiber point whose
`Y` is a non-`D_t` permutation of `Y(y)` could in principle give a
different cyclic-dot multiset (the cyclic `z̄` are not `S_4`-invariant).

**Status of Lemma Y: verified, not proved.** Verification runs
(scripts in `methods/`, exact integer arithmetic):

| case | scope | pair_sorted varying fibers | sorted-Y varying fibers | Y ∉ D_t-orbit violations |
|---|---|---|---|---|
| m = 4 (`D=1152`) | full `Fix_4`, 203 fibers, 1152 pts | 0 | 0 | 0 / 1152 |
| m = 6 (`D=39200`) | full `Fix_6`, 3604 fibers, 39200 pts | 0 | 0 | 0 / 39200 |
| m = 8 (`D=1331712`) | full `Fix_8`, 85106 fibers, 1331712 pts | 0 (sep test) | 0 | 0 / 1331712 |
| m = 12 bad fiber | complete global fiber: all 36 lifts of the mod-81 bad fiber (other components 0; the fiber is exactly these 36, since every value is a multiple of `D/81`) | identical across all 36 | identical | 0 / 36 |

Notes on the m = 12 check: the 36 class-sum vectors take only the
four `D_4`-orbit values of `(2561328000, 2561328000, 2049062400,
2049062400)` — patterns `(A,A,B,B)`, `(A,B,B,A)`, `(B,A,A,B)`,
`(B,B,A,A)` — never `(A,B,A,B)` or `(A,B,B,A)`-outside-`D_4` patterns,
so the check is non-vacuous. The AP-generated `Z` for m = 12 matches
the `tors_z` list in `oprime_m12_counterexample_result.json` exactly.
Odd m needs no check: `t = 1` makes Lemma Y trivial.

**Why Lemma Y is not obvious.** The fiber points are not, in general,
affine images of each other (m = 12 is the counterexample: 3 affine
canons in one fiber, yet all 36 lifts satisfy Lemma Y). So Lemma Y is
strictly weaker than affine separation, and strictly stronger than
sorted-`Y` invariance: it says the class sums permute *dihedrally*,
not arbitrarily. A proof route worth pursuing (not attempted here):
CRT-decompose `Fix_m` into prime-power components, where `Fix mod q`
is a cyclic `ℤ/q`-module, and track class sums component-wise; the
class sums mod each prime power may be forced into `D_t` orbits by the
cyclic structure. Until such a proof exists, pair constancy at
`m ≥ 10` (except the odd-`m` trivial case and the tested m = 12 fiber)
is an open empirical statement, not a theorem.

## 6. What this explains about the support criterion

At `s = 1`, `y ∈ supp φ̂` iff for every torsion `γ`,
`2·Qnum(z_γ) − pairNum(z_γ, w_y) ≡ 0 (mod D_m)`. The term `Qnum(z_γ)`
does not involve `y` at all; the term `pairNum(z_γ, w_y) = z_γ·y`
is, by §1–§5, a fiber function (modulo Lemma Y; unconditionally at
m = 8 by the exhaustive check, where `pair_sorted` — hence
`pair_sorted mod D` — varies on 0 of 85106 fibers). Therefore:

- **The support condition is constant on fibers: `supp φ̂` is a union
  of fibers** (wherever pair constancy holds). At m = 8 this is the
  observed passcount picture: passcounts are 4 (998784 pts), 8
  (249696 pts), 16 (83232 pts), support = passcount-16 fibers only,
  bad fibers have passcount < 16 and never meet support.
- **pairNum cannot separate inside a fiber, in principle, not just
  in the tested cases.** Any invariant built from `pairNum` (exact,
  mod `D`, or the support passcount) is a function of the fiber
  (via `Y` and `z̄`), so it can only exclude whole fibers. This kills
  the pairNum line of inquiry for 152's separation step in the strong
  sense: the failure at m = 8 (39/39 bad fibers) and at m = 12 (the
  counterexample pair, pair lists identical, multiples of `D`) is
  structural, not a small-sample accident.
- At m = 8 there is an extra simplification: `2·Qnum(z_γ) ≡ 0 (mod D)`
  for all `γ`, so support reduces to `pairNum ≡ 0 (mod D)`. At m = 12
  this simplification is **false** (`2·Qnum ≡ D/2` for half the `γ`,
  wave-5 task 2): the full `(2Q − pair)` form is essential there, and
  the m = 12 counterexample pair fails 8 of 16 conditions with value
  `D/2` (torsion sum `8·(+1) + 8·(−1) = 0`), consistent with being
  outside support. The fiber-constancy argument is unaffected, since
  `Qnum` is `y`-independent in both cases.
- For 152, the consequence is the one in the wave-6 note §5: O′ (fiber
  ⇒ Γ-orbit *on support*) is the support-based statement that can
  survive, because on support the fibers do not split at m = 8 and
  the m = 12 killer pair is outside support. Proving O′ in general
  still needs Lemma Y plus the statement that bad fibers have
  passcount < 16 — neither is proved in general.

## 7. What would refute it, and next steps

1. **A single fiber point with `Y` outside the `D_t`-orbit** of its
   fiber's first `Y` refutes Lemma Y — and, unless the cyclic dots
   coincide accidentally, refutes pair constancy. The cheapest
   informative search is at m = 10 (`t = 2`, so only `{E, O}` needs
   checking) on sampled fibers, since full `Fix_10` (45,239,072 points)
   is too large for exhaustive enumeration here; a CRT-component
   search for a bad component fiber is the realistic route.
2. **Prove Lemma Y** (CRT/cyclic-component route in §5), which would
   promote the whole §3–§4 argument to a general theorem and close
   the pairNum line properly, including the support-union-of-fibers
   corollary for general m.
3. Do **not** spend further effort on moments, symmetric functions,
   or `pairNum`-based separators inside a fiber: §0 of the wave-6 note
   (symmetric functions are fiber-constant by definition) plus this
   note (pairNum is a fiber function via `Y`) close both lines.

## Files

- This note: `methods/pair_sorted_identity_note.md`
- Probes: `methods/pair_fiber_probe.py` (m = 8 class sums),
  `methods/pair_identity_probe2.py` (m = 4, 6 full; m = 12 lifts),
  `methods/pair_identity_m8_d4.py` (m = 8 `D_4`-orbit check)
- Prior data reused (not regenerated): `methods/sep_m8_result.json`,
  `methods/oprime_m12_counterexample_result.json`
