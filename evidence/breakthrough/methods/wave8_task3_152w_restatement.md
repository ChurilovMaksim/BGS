# Claim 152 restated via route (b): grouping by (fiber, w)-classes

## Status banner — read first

**PROPOSAL ONLY. This is not the project's claim 152, not a registry
edit, not a Lean theorem, and not a change to main.** Nothing in this
document may be quoted as the content of claim 152, and no registry
state may be changed on its basis. Its m = 8 numbers are exact-integer
replays (a verifier artefact), not proofs and not Lean theorems.

What this document does: it writes down, precisely, the restatement
that wave 6 task 2 called route (b) and wave 7 task 3 left as the only
surviving route for P_w besides the O′ route — grouping the strong-kick
pair sum by (fiber, w)-classes instead of by Γ-orbits, with Bsym
recomputed over those classes — and it computes the restated value at
m = 8, where it can be checked, including the check that at m = 8 the
restatement changes the *lemma* but not the *number* on the support.
Section 5 states plainly what the restatement does **not** do: it does
not supply the decay mechanism that ω was supposed to supply, because
ω is blind inside a fiber (wave 7 task 3). Any use of this restatement
must carry that gap openly (obligation D1, §6).

## 1. What is being restated, and why

### 1.1 The original separation step (hSep)

In the project's strong-kick chain (line 152, `LineDStrongKickConc`),
the separation step, called `hSep`, is:

> Equal mode sums `S_k(ξ) = S_k(ξ')` for all `k` in `𝒦 ⊇ {1, …, m}`
> imply `ξ' ∈ Γ·ξ`, where `Γ` is the dihedral group of index
> permutations `j ↦ ±j + k`.

The step factors as Newton (power sums ⇒ equal multisets) followed by
the combinatorial claim `[CA]` (equal multisets ⇒ same Γ-orbit). The
second factor is the original candidate O1. It is **false**: at m = 8
there are 39 bad fibers (fibers = sorted-multiset classes that contain
more than one Γ-orbit); the first explicit counterexample is
`y = (0, 1276224, 998784, 721344, 665856, 610368, 332928, 55488)` and
`y' = (0, 721344, 332928, 1276224, 665856, 55488, 998784, 610368)`
(fiber size 32 = two Γ-orbits of size 16). The affine replacement O*
is false in the strict "fiber = full affine orbit" reading at m = 8
(84,672 of 85,106 fibers) and false even in the separation reading
("every fiber is contained in one affine orbit") at m = 12 (explicit
torsion-lift counterexample from a mod-81 bad fiber). So no
orbit-grouping that is coarser than the fiber and justified by modeSum
alone survives in general.

### 1.2 The original Bsym

`Bsym` in the project (`LineDParity` definition) is the orbit-size
average over the support `α = supp φ̂`:

```
Bsym_Γ = (1/|supp|) · Σ_{x ∈ supp} |Γx|.
```

If every fiber meeting the support were a single Γ-orbit (original
O1, or its support restriction O′), grouping the sum by fibers gives
the fiber formula `Bsym = (1/|supp|) · Σ_M |fiber(M)|²`. The original
claim 152 asserts, under the StrongKickConc hypotheses (Gaussian-ω
hypotheses `hω0`, `hωbound`, `hωlim`; Γ-invariance of `modeSum`;
equality of limits over odd coprime residues), that the strong-kick
limit equals this `Bsym_Γ`. The separation step is exactly where the
false lemma sits.

### 1.3 Why ω cannot rescue a finer grouping

Wave 7 task 3 established, as a matter of principle and not just
numerically: `S_k(ξ) = Σ_j e(kξ_j)` is a symmetric sum, hence a
function of the multiset alone. Inside one fiber all `S_k` agree, so
every `Δ_k = 0` and the pair's ω-factor is `∏_k ω_k(0) = 1` at every
`η`, for both the Gaussian and the J0 form. Therefore **ω does not
distinguish w-classes inside a fiber**, and it cannot be quoted to
kill cross-w-class pair terms. Any restatement that groups by a
finer-than-fiber invariant must say so explicitly instead of
inheriting the "off-orbit pairs killed by ω" step. See §5 and
obligation D1 (§6).

## 2. Definitions

Work in the finite model used by all waves. `m ≥ 3` unless stated.

- `H_m = 6I − C − Cᵀ` (circulant, `C` the cyclic shift),
  `D_m = det H_m`, `Fix_m = ker(H_m mod D_m)`.
- **Fiber** of `y ∈ Fix_m`: the class `μ⁻¹(μ(y))` where
  `μ(y) = sorted(y)` (the multiset of coordinates).
- `Γ`: dihedral index permutations `j ↦ ±j + k` acting by
  `(γy)_j = y_{γ(j)}` (16 permutations at m = 8, 2m in general).
  `H_m` commutes with `Γ` and is invertible over ℚ, so
  `y' ∈ Γy ⟺ w_{y'} ∈ Γw_y` (tautology, not a principle).
- **Quotient vector** `w_y = (H_m y)/D_m ∈ ℤ^m`. It is well defined
  because `H_m y` is divisible by `D_m` for `y ∈ Fix_m`, and
  `w_j ∈ {−1, 0, 1, 2, 3, 4, 5}` for every m (since
  `(H_m y)_j ∈ (−2D_m, 6D_m)` and is a multiple of `D_m`).
  `w` is already a project object: it is the `w` in the O′ support
  criterion.
- **(fiber, w)-class** of `y`: `C_w(y) = {y' : sorted(y') = sorted(y)
  and sorted(w_{y'}) = sorted(w_y)}`. Since `sorted(w)` is constant
  on Γ-orbits (Γ permutes coordinates of `w`, sorting kills the
  permutation), every Γ-orbit is contained in one (fiber, w)-class.
  The converse containment is the content of P_w.
- **P_w (candidate separation principle, m-restricted):** for
  `y, y' ∈ Fix_m`,
  `sorted(y) = sorted(y') ∧ sorted(w_y) = sorted(w_{y'}) ⟹ y' ∈ Γy`.
  Equivalently: every (fiber, w)-class is a single Γ-orbit.
  P_w is **not** a function of modeSum: `sorted(w)` is not determined
  by the multiset (it differs inside bad fibers), which is exactly
  why it can separate where modeSum cannot — and exactly why the
  chain must either add it as a hypothesis or find a decay step
  that kills pairs with different `w` (the latter is dead, §1.3).
- **Support** `supp = supp φ̂_s` (s odd, coprime to `D_m`). At m = 8
  the support criterion is: `y ∈ supp` iff
  `(2·Qnum(z_γ) − pairNum(z_γ, w_y)) ≡ 0 (mod D_m)` for all 16
  torsion elements `γ ∈ V4 = ker(H_m mod 4)`, where
  `z_γ = (H_m v)/4` and `pairNum(z, w_y) = z·y` (since `X w_y = y`
  for `X` the adjugate of `H_m`). Per the bridge document D3/Prop R,
  the support does not depend on `s` (for odd `s` coprime to `D_m`);
  that independence is a project source claim, to be re-verified
  before any main-bound use, not something this document proves.
- **Restated Bsym:**
  ```
  Bsym_w = (1/|supp|) · Σ_{x ∈ supp} |C_w(x)|
         = (1/|supp|) · Σ_{C ⊆ supp} |C|²,
  ```
  where the second form requires `supp` to be a union of
  (fiber, w)-classes (verified at m = 8, §4; an obligation in
  general, §6).

## 3. The restated claim 152-w (proposal)

**Claim 152-w (m = 8, proposal).** Let `m = 8`, `D = 1331712`,
`supp = supp φ̂_s` as above. Under the StrongKickConc hypotheses
(Gaussian-ω hypotheses; Γ-invariance of `modeSum`; equality of
limits over odd coprime residues) **and** the pair-sum-to-class-
average lemma D1 (§6), the strong-kick limit equals

```
Bsym_w = 318335/20808 ≈ 15.298683.
```

**Separation lemma used (hSep_w, m = 8).** For `y, y' ∈ Fix_8`,
`sorted(y) = sorted(y')` and `sorted(w_y) = sorted(w_{y'})` imply
`y' ∈ Γy`. Status: verified exhaustively at m = 8 (§4); it is not
a Lean theorem and not proved for general m.

**Schema for other m.** `152-w(m)` denotes the same statement with
`m` in place of 8. It is meaningful only when (i) P_w holds at that
m, (ii) `supp` is a union of (fiber, w)-classes at that m, and
(iii) D1 holds at that m. None of (i)–(iii) is asserted for any
`m ≠ 8` in this document; §7 tabulates the per-m status.

**What changed relative to original 152.** Only the separation
lemma and the grouping: Γ-orbits are replaced by (fiber, w)-classes
as the classes over which the support average is computed. The
ω-hypotheses, the modeSum invariance, the limit-over-residues step,
and the rest of the 152-full package (J0 ensemble, N-step, Fix
identification — §6) are untouched by this restatement, and their
status is unchanged.

## 4. Computation at m = 8

Method: exact-integer replay, same conventions as the m = 8 O′ test
and the wave-6 separation test — `Fix_8` enumerated by CRT from
kernels mod 9, 289, 512 (1,331,712 points, every point asserted to
satisfy `H y ≡ 0 mod D`); Γ-orbit canonical = lexicographic minimum
over the 16 dihedral permutations (elementwise minimum is **not** a
canonical and was not used); `w = (H y)/D`; support by the full
`(2Q − pair) ≡ 0 (mod D)` torsion criterion over all 16 `γ`
(`Qnum` via exact rational solve `H t = D z`, `pairNum = z·y`).
Script: `methods/wave8_task3_bsymw_m8.py`;
result: `methods/wave8_task3_bsymw_m8_result.json`.

### 4.1 Global counts and partition coincidence

| quantity | value |
|---|---|
| `\|Fix_8\| = D` | 1,331,712 |
| fibers | 85,106 |
| Γ-orbits | 85,145 |
| distinct `sorted(w)` values | 2,055 |
| (fiber, w)-classes | 85,145 |
| distinct (Γ-orbit, (fiber, w)-class) pairs | 85,145 |
| distinct ((fiber, w)-class, Γ-orbit) pairs | 85,145 |

The last two rows are the point: containment (Γ-orbit ⊆
(fiber, w)-class, since `sorted(w)` is Γ-invariant) plus equal
counts already forces the partitions to coincide, and the direct
check confirms it — **every (fiber, w)-class at m = 8 contains
exactly one Γ-orbit, and vice versa. The partitions coincide as
sets, not merely in count.** Fiber-size distribution:
1:4, 2:14, 4:90, 8:3647, 16:81318, 32:33. Γ-orbit-size distribution:
1:4, 2:14, 4:90, 8:3659, 16:81378 (the 39 bad fibers contribute the
difference: 33 fibers of size 32 split 16+16, 6 fibers of size 16
split 8+8).

### 4.2 Support composition

| quantity | value |
|---|---|
| `\|supp\|` | 83,232 = D/16 |
| passcount distribution (points) | 4: 998,784; 8: 249,696; 16: 83,232 (no other values) |
| fibers contained in supp | 5,684 |
| Γ-orbits contained in supp | 5,684 |
| (fiber, w)-classes contained in supp | 5,684 |
| fibers / orbits / classes straddling supp | 0 / 0 / 0 |
| size distribution on supp (all three classings agree) | 1:4, 2:14, 4:36, 8:878, 16:4752 |
| `Σ \|class\|²` over supp | 1,273,340 |

Check: `4·1 + 14·2 + 36·4 + 878·8 + 4752·16 = 83,232`, and
`4·1 + 14·4 + 36·16 + 878·64 + 4752·256 = 1,273,340`. No fiber of
size 32 lies in the support (all 33 are bad, and bad fibers have
0 support points — the O′ result). Hence on the support, the
fiber formula, the Γ-orbit formula, and the (fiber, w)-class
formula **all agree**.

### 4.3 The values

```
Bsym_w(supp)    = 1273340/83232 = 318335/20808 ≈ 15.298683
Bsym_Γ(supp)    = 318335/20808 ≈ 15.298683   (identical)
Bsym_fiber(supp)= 318335/20808 ≈ 15.298683   (identical)
```

For contrast, over the whole of `Fix_8` (not the project's
definition — shown only to locate where the classings differ):

```
Bsym_w(Fix)     = 5267111/332928 ≈ 15.820571
Bsym_Γ(Fix)     = 5267111/332928 ≈ 15.820571   (identical, as §4.1 forces)
Bsym_fiber(Fix) = 5271527/332928 ≈ 15.833835   (differs by 4416/332928 ≈ 0.013264)
```

The global fiber/orbit difference is exactly the bad-fiber
accounting: 33 fibers contribute `32² − 2·16² = 512` each and 6
fibers contribute `16² − 2·8² = 128` each, total
`33·512 + 6·128 = 17,664` in sum-of-squares, i.e. `17664/1331712 =
4416/332928`. On the support this difference vanishes because no
bad fiber meets the support.

### 4.4 Worked example: the first bad fiber

Sorted key `(0, 55488, 332928, 610368, 665856, 721344, 998784,
1276224)`: fiber size 32; Γ-orbits 16 + 16; (fiber, w)-classes
16 + 16, with the two distinct `sorted(w)` values
`(−1, 0, 1, 2, 2, 2, 3, 5)` and `(−1, −1, 0, 2, 2, 3, 4, 5)`.
Per-fiber contributions (before dividing by `|supp|`): fiber
formula 1024, Γ/w formula 512. The fiber lies entirely outside
the support (0 support points), so it contributes to none of
the §4.3 support values — which is why the restatement is
numerically invisible on the support at m = 8.

## 5. What the restatement does and does not do

**It does do:**

- It replaces a false combinatorial lemma (hSep/O1) by a lemma
  that is true at m = 8 by exhaustive exact check (hSep_w/P_w),
  with a finite per-m verification procedure (enumerate `Fix_m`,
  compare (fiber, w)-classes with Γ-orbits).
- It gives a well-defined recomputed value `Bsym_w` at m = 8 that
  coincides with the original Γ-`Bsym` on the support, so the
  m = 8 numerical claim is preserved, not altered.
- It is a genuine content change in general: at an `m` where the
  support contains a split fiber, `Bsym_w` and the fiber formula
  differ, and `Bsym_w` is the one the restated claim asserts.

**It does not do:**

- It does **not** repair the original chain with the original
  hypotheses. The chain's hypothesis is equal modeSum, i.e. same
  fiber; P_w additionally needs equal `sorted(w)`. A pair in one
  fiber with different `sorted(w)` is present in the pair sum
  with ω-factor exactly 1 (§1.3), so nothing in the ω step removes
  it. The restated claim therefore has two readings, which must
  not be conflated:
  - **(B1) Value reading** (established at m = 8 by §4): the
    orbit-counting average over (fiber, w)-classes on the support
    is `318335/20808`, equal to the original Γ-average. This
    needs no analytic step.
  - **(B2) Limit reading** (open): the strong-kick limit equals
    `Bsym_w`. This additionally needs obligation D1 below.
- It does not prove P_w in general, does not bound Γ-orbits per
  fiber (impossible in general — wave 7 task 4: the `m = 2^k`
  family gives `φ(m)/2` orbits per fiber, 16 at m = 64), and does
  not touch the J0, N-step, or Fix-identification gaps of
  152-full.
- It does not make `sorted(w)` a function of modeSum, and no
  symmetric function or function of modeSum can separate inside a
  fiber (by definition of the fiber). Any future "repair" that
  keeps the hypothesis "equal modeSum" and only changes the
  conclusion is impossible for the same reason.

**Comparison of the four routes:**

| route | grouping on supp | Bsym on supp at m = 8 | status |
|---|---|---|---|
| original (Γ-orbits via hSep) | Γ-orbits | 318335/20808 | hSep false in general; true on supp at m = 8 only because supp has no split fibers |
| Aff restatement (O*) | affine orbits (separation reading) | 318335/20808 | separation false at m = 12; value on supp at m = 8 unchanged (supp fibers unsplit) |
| **(b) this restatement (w-classes)** | (fiber, w)-classes | **318335/20808** | P_w verified at m = 8; global m = 12 open; general m open; D1 open |
| (c) O′ route | fibers restricted to supp | 318335/20808 | at m = 8, supp fibers are unsplit, so O′ holds at m = 8; general m open; m = 12 counterexample pair is outside supp, so it does not kill O′ at m = 12 |

## 6. Exactly what would need proving for 152-w to be a theorem

**D1. Pair-sum-to-class-average derivation (the analytic gap).**
Re-derive, inside `LineDStrongKickConc`/`LineDStrongKickBridge`,
the step from the pair sum
`Ψ_m(s/D) = Σ_{ξ,ξ'} φ̂_s(ξ) conj φ̂_s(ξ') ∏_k ω_k(η(S_k(ξ) − S_k(ξ')))`
to the class average `Bsym_w`, with (fiber, w)-classes in place of
Γ-orbits. Identify precisely where Γ-invariance of `φ̂` and of
`modeSum` is used, whether `φ̂` is constant (in modulus, or in the
averaged sense the derivation needs) on (fiber, w)-classes, and
what happens to cross-w-class terms inside one fiber. Quoting
ω-decay for this step is **not** available (§1.3). Until D1 is
done, only reading (B1) is established; reading (B2) is a
conditional claim. This is the single most important obligation:
without it, route (b) is a recomputation, not a proof of a limit.

**D2. P_w as a theorem, per m.** At m = 8 the statement is verified
exhaustively but not proved; a Lean proof (or a finite-certificate
proof in the style of TARGETS N3(b): orbit representatives plus a
checkable `sorted(w)` table) is needed before any main-bound use.
Per-m status (§7): m = 9 vacuous (0 bad fibers, fibers = orbits);
m = 10, 11, 13: P_w untested (O* separation holding there says
nothing about Γ-splitting); m = 12: P_w open globally (component
lifts survive, gluing-derived bad fibers untested); m ≥ 14:
untested. General m: no proof strategy is known, and the
orbit-count bound route is closed (wave 7 task 4); the counting
tension (only `C(m+6, 6)` possible `sorted(w)` values, versus
exponentially many fibers) must be addressed by any general-m
argument, since it constrains how P_w could possibly hold.

**D3. Support is a union of (fiber, w)-classes (per m).** Verified
at m = 8 (§4.2: 0 straddling classes). In general this needs the
support criterion's pair part to be constant on (fiber, w)-classes
(indeed on fibers, modulo Lemma Y) plus the `2Q` part, which is
`y`-independent. Note the m = 12 trap: `2·Qnum ≡ D/2 (mod D)` for
half the torsion elements at m = 12, so the full `(2Q − pair)`
form is essential there; the m = 8 shortcut `pair ≡ 0` does not
carry over.

**D4. Lemma Y (only for the support-union argument via pairNum).**
`pair_sorted` is fiber-constant because it is a class-sum identity:
with `t = gcd(m, 4)` and class sums `Y_r(y)` over `+4`-orbits,
every pair value is `z̄·Y(y)` for a fixed class vector `z̄`, and
full fiber-constancy is equivalent to Lemma Y (within a fiber,
`Y(y')` is always a `D_t`-permutation of `Y(y)`). Lemma Y is
verified exhaustively at m = 4, 6, 8 and on the m = 12 bad fiber,
and trivial at odd m (`t = 1`), but **not proved** in general.
If D3 is proved by another route, D4 is not needed for 152-w;
it is listed because it is the current route to the
support-union statement and because it explains why pairNum can
only exclude whole fibers, never separate inside one.

**D5. The rest of 152-full, unchanged.** hSepC (complex variant);
J0 ensemble (Bessel `J0` is not in Mathlib; the Gaussian case has
the ω lemmas, the J0 case needs analytic input); the N-step `hN`
(iterated strong limit, `t_N → t*` for true `Psi_m`, not just
`PsiMode`); identification of finite `Fix m` with torus `Fix_m`;
symmetry of coefficients `c`. None of these is addressed by
route (b).

**D6. Lean formalization.** Definitions of `w`, (fiber, w)-class,
and `Bsym_w` in the style of `LineDParity`; the m = 8 certificate
(or proof) of hSep_w; the D1 derivation; full axiom audit
(standard axioms only, `sorryAx = 0`); re-verification of every
definition against the then-current main HEAD before any push
(definitions here are taken from workspace notes citing main at
HEADs `6dbcc7a` (PR #75) and `d87dce0` (PR #76), not re-fetched
for this draft).

## 7. Per-m status of P_w (for the schema 152-w(m))

| m | P_w status | evidence |
|---|---|---|
| 8 | verified (exhaustive) | this document §4; wave-6 separation test (0 failures over 85,106 fibers) |
| 9 | holds vacuously | 0 bad fibers; fibers = orbits = 434,020 (wave-7 kill-test) |
| 10, 11 | untested | O* separation holding there does not imply P_w |
| 12 | open globally | component-derived bad fibers survive P_w (3 lifts, distinct `sorted(w)`); gluing-derived bad fibers untested |
| 13 | untested | O* separation holding there does not imply P_w |
| ≥ 14 | untested | — |
| general m | open, no proof strategy | orbit-count bound route closed (wave 7 task 4); counting tension (§6, D2) |

## 8. Sources and caveats

- Definitions and the m = 8 bad-fiber example: `methods/M08_GAMMA_ORBITS.md`,
  `methods/ostar_m8_note.md`, `methods/sep_new_principle_note.md`,
  `methods/oprime_m8_note.md` (workspace notes; their main citations
  are `LineDParity`, `LineDOrbitPairFull`, `LineDStrongKick`,
  `LineDStrongKickBridge`, `LineDStrongKickConc`, and
  `mathematics/fixed-map/band_limited_kick_bridge.md` D3–D5).
- ω-blindness: `methods/wave7_omega_w_note.md` (wave 7 task 3).
- Pair-sorted identity and Lemma Y: `methods/pair_sorted_identity_note.md`
  (wave 7 task 2).
- Unbounded Γ-orbits per fiber: `methods/gamma_orbits_per_fiber_note.md`
  (wave 7 task 4).
- Computation in this document: `methods/wave8_task3_bsymw_m8.py`,
  `methods/wave8_task3_bsymw_m8_result.json` (this task; exact
  integers, no floats in any count or fraction; the only floats in
  this document are the decimal expansions of exact fractions).
- Caveats carried over: the m = 8 support criterion used here is
  the `s = 1` form; support-independence of `s` (odd, coprime to
  `D`) is a bridge-document claim (D3), not re-proved here. The
  `StrongKickConc` file header in main reportedly still says
  "TEST COPY ONLY — not pushed" although the file is in main and
  imported; that staleness does not affect the mathematics here
  but must be cleaned before any main-bound use. All enumerations
  are verifier artefacts, not Lean theorems.

## 9. Bottom line for the parent

Route (b) at m = 8 is fully computed and value-preserving:
`Bsym_w = Bsym_Γ = Bsym_fiber = 318335/20808 ≈ 15.298683` on the
support, because (fiber, w)-classes coincide exactly with Γ-orbits
at m = 8 and the support contains no split fiber. The restatement's
real content is therefore not a new number at m = 8 but a new,
verified-at-m = 8 separation lemma in place of a false one — and
one explicitly open analytic gap (D1): since ω = 1 inside a fiber,
the step from the pair sum to the class average cannot be inherited
from the original derivation and must be re-derived. Until D1 (and
per-m D2–D3) is done, 152-w is a precisely stated proposal with a
verified value, not a theorem and not a substitute registry entry.
