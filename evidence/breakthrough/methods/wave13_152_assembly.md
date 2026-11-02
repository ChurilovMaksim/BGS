# Wave 13, task 4 — Claim 152 assembly sketch via route (b)

**Status: assembly sketch, not a theorem, not a registry edit, not a
Lean formalisation, not a change to main.** Nothing here may be quoted
as the content of claim 152, and no registry state may be changed on
its basis. Every number below that is not a fraction is an exact
integer replay (a verifier artefact), not a proof. The sketch states
exactly what is already closed, what is closed only as a sketch, and
what remains open — §7 is the binding list. Definitions are taken from
the workspace notes cited in §8, which themselves cite main at HEAD
`d87dce0d9277579568edfee6cffecbc96ea61024` (PR #76); nothing was
re-fetched from main for this note, and no definition was changed.

## 0. The original claim, and what route (b) changes

Original claim 152 (project reading, per `LineDStrongKickConc` and the
wave-8 restatement note): under the StrongKickConc hypotheses
(Gaussian-ω hypotheses `hω0`, `hωbound`, `hωlim`; Γ-invariance of
`modeSum`; equality of limits over odd coprime residues), the
strong-kick limit equals

```
Bsym_Γ = (1/|supp|) · Σ_{x ∈ supp} |Γx|,
```

the orbit-size average over the support `supp = supp φ̂_s` (s odd,
coprime to `D_m`). The derivation factors through the separation step
`hSep`: equal mode sums `S_k(ξ) = S_k(ξ')` for all `k ∈ 𝒦 ⊇ {1,…,m}`
imply `ξ' ∈ Γ·ξ`. That step is false: it factors as Newton (power
sums ⇒ equal multisets, i.e. same fiber) followed by `[CA]` (equal
multisets ⇒ same Γ-orbit), and `[CA]` fails — 39 bad fibers at m = 8,
and the affine replacement O* fails in the separation reading at
m = 12 (torsion-lift counterexample from a mod-81 bad fiber).

Route (b) changes exactly one thing: the grouping. Γ-orbits are
replaced by **(fiber, w)-classes**

```
C_w(y) = {y' : sorted(y') = sorted(y) and sorted(w_{y'}) = sorted(w_y)},
  w_y = (H_m y)/D_m ∈ ℤ^m,
```

and `Bsym` is recomputed over those classes:

```
Bsym_w = (1/|supp|) · Σ_{C ⊆ supp} |C|².
```

Everything else — the ω-hypotheses, modeSum invariance, the
limit-over-residues step, and the rest of the 152-full package — is
untouched by the restatement, and its status is unchanged (§7, items
6–7). The restatement is legitimate as a proposal only because of
§3: at m = 8 the two classings coincide as sets on the support, so
the value is preserved there. In general it is a different claim
from original 152, and it must never be cited as original 152.

## 1. What Lemma Y (mod-D) now gives — closed as a sketch

Lemma Y (mod-D): if `y, y' ∈ Fix_m` lie in the same fiber, then
`Y(y') ≡ π(Y(y)) (mod D_m)` for some `π ∈ D_t`, where `t = gcd(m,4)`
and `Y_r(y) = Σ_{i ≡ r (mod t)} y_i` are the class sums over
`+4`-orbits. Status after waves 8–12, **as a proof sketch** (not Lean):

| Component | Status | Source |
|---|---|---|
| Odd primes `p ∤ 24` | Proved: `Y_r ≡ 0 (mod q)`, component lemma trivial | Wave 8 |
| `p = 3`, exponent `e > 1` (P3′) | Proved as sketch: scaling by `3^{f₀}`, top digit `Z' = n₀·v`, mod-3 classification | Wave 9 |
| `p = 2`, uniform in `v₂` (P2) | Proved as sketch: doubling identity `S^{(k)} = 2S^{(k-1)}`, base `k ≤ 6` checked, `k = 7, 8` verified (0 bad) | Wave 10 |
| Per-class pattern lemma (2-primary pattern input) | Proved as sketch: induction L1–L4; verified to P = 128 (129,997,838 pairs, 0 bad) | Wave 11, task 1 |
| π₂ = π₃ compatibility (Pmix, mod-D) | Proved as sketch: conditional on (A) pattern lemma + (B) Lemma S; (B) itself proved as sketch in wave 12 (pair lemma PL + combinatorial step; verified at P = 8, 16, 0 fails) | Wave 11, task 3 + wave 12, task 2 |

Consequence: **Pmix at mod-D level is fully closed as a sketch.**
What Lemma Y (mod-D) does *not* give: exact-integer class-sum
equality (that is Pcarry, §7 item 1), any statement about `sorted(w)`
(that is P_w, §3, a different lemma), or a Lean theorem (all four
components are sketches; none is formalised).

## 2. What Lemma Y + the pair identity give — the support leg

The pair identity (wave 7, task 2) is unconditional algebra:

```
pairNum(z, w_y) = z·y = z̄·Y(y),
```

where `z` runs over torsion representatives, `z̄` is its class vector
(constant on `+4`-orbits), and the set `{z̄}` is `D_t`-invariant (finite
case check on `(a, d)`, ≤ 16 patterns). Therefore:

- **Unconditional:** `pair_sorted` is constant under affine
  permutations, and fiber-constant for odd `m` (`t = 1`, so every pair
  value is `a·Σy`).
- **Modulo Lemma Y (mod-D):** `pair_sorted mod D_m` is fiber-constant
  for every `m`, because `Y(y') ≡ π(Y(y)) (mod D)` and `{z̄}` is
  `D_t`-invariant.
- **Support corollary (modulo Lemma Y):** the support criterion
  `(2·Qnum(z_γ) − pairNum(z_γ, w_y)) ≡ 0 (mod D_m)` is fiber-constant,
  since `Qnum(z_γ)` is `y`-independent and the pair term is
  fiber-constant mod `D`. Hence **`supp φ̂` is a union of fibers**
  wherever Lemma Y (mod-D) holds — i.e. now, as a sketch, for all `m`.

Two cautions that belong to this leg and must not be dropped:

1. The m = 8 shortcut `2·Qnum ≡ 0 (mod D)` is false at m = 12
   (`2·Qnum ≡ D/2` for half the torsion elements); only the full
   `(2Q − pair)` form is fiber-constant there. Any general-m use
   must carry the full form.
2. Pair constancy is a *ceiling*, not a separator: pairNum can only
   exclude whole fibers, never separate inside one. This is structural
   (pair values are functions of `Y` and `z̄`), not a small-sample
   accident. So the support leg can justify grouping by fibers, but
   it can never by itself justify grouping by (fiber, w)-classes —
   that needs P_w (§3) and the D1 derivation (§5).

## 3. What P_w gives — the value leg (m = 8 established, general open)

P_w: `sorted(y) = sorted(y') ∧ sorted(w_y) = sorted(w_{y'}) ⟹ y' ∈ Γy`,
i.e. every (fiber, w)-class is a single Γ-orbit. P_w is **not** a
consequence of Lemma Y: Lemma Y constrains class sums `Y`, while P_w
constrains the quotient vector `w_y = (H_m y)/D_m`, a different object
(`w_j ∈ {−1,…,5}` for every `m`). The two lemmas must not be conflated.

**At m = 8 (exact replay, not a proof):** `Fix_8` has 85,106 fibers,
85,145 Γ-orbits and 85,145 (fiber, w)-classes, and the two partitions
coincide as sets (every (fiber, w)-class contains exactly one Γ-orbit
and vice versa). On the support (`|supp| = 83,232 = D/16`): 5,684
fibers = 5,684 orbits = 5,684 (fiber, w)-classes, 0 straddling classes
in any of the three classings, `Σ|class|² = 1,273,340`, hence

```
Bsym_w(supp) = Bsym_Γ(supp) = Bsym_fiber(supp) = 1273340/83232
             = 318335/20808 ≈ 15.298683.
```

This is reading **(B1), the value reading**: the orbit-counting average
over (fiber, w)-classes on the support equals the original Γ-average
at m = 8. It needs no analytic step. The reason it holds is visible:
no bad fiber meets the support at m = 8 (all 39 bad fibers have 0
support points — the O′ phenomenon), so on the support the fiber
formula, the Γ formula and the w formula cannot differ.

**General m (open):** P_w is verified at m = 8 only, holds vacuously
at m = 9 (0 bad fibers), and is open globally at m = 12 (component
lifts survive P_w; gluing-derived bad fibers untested) and untested
at m = 10, 11, 13 and ≥ 14. There is no known general-m proof strategy,
and the orbit-count-bound route is closed (the `m = 2^k` family gives
`φ(m)/2` orbits per fiber, 16 at m = 64). Any general-m argument must
also face the counting tension: only `C(m+6, 6)` possible `sorted(w)`
values versus exponentially many fibers. Until P_w is proved per-m,
`Bsym_w = Bsym_Γ` is not available beyond m = 8 (and vacuously m = 9),
so route (b) beyond m = 8 is a schema `152-w(m)` with hypotheses
(P_w at `m`, support a union of (fiber, w)-classes at `m`, D1 at `m`),
not a theorem.

## 4. Why ω cannot supply the missing step — route (a) is dead

For the pair sum (bridge doc D3, `LineDStrongKick.pairTerm`):

```
Ψ_m(s/D) = Σ_{ξ,ξ'} φ̂_s(ξ) conj φ̂_s(ξ') ∏_k ω_k(η(S_k(ξ) − S_k(ξ'))),
  S_k(ξ) = Σ_j e(kξ_j),
```

with `ω = J0(a|z|)` (uniform θ) or `exp(−a²|z|²/4)` (Gaussian), and
hypotheses `hω0 : ω_k(0) = 1`, `hωbound : ‖ω_k‖ ≤ 1`,
`hωlim : ω_k(η·Δ) → 0` for `Δ ≠ 0`. The blindness is by principle:

1. `S_k(ξ)` is a symmetric sum, hence a function of the multiset alone.
2. A fiber is by definition a set of vectors with the same multiset,
   so inside one fiber `S_k(ξ) = S_k(ξ')` for every `k`, every `Δ_k = 0`.
3. Hence the pair's ω-factor is `∏_k ω_k(0) = 1` at every `η`, for both
   forms (`exp(0) = 1`, `J0(0) = 1`). Numerically confirmed at m = 8
   (first bad fiber: `max|ΔS_k| ≈ 9×10⁻¹⁶`, ω-factor 1.000000000000 at
   `η = 0, 1, 5, 20, 100`) and on the m = 12 counterexample pair, with a
   non-vacuous control (cross-fiber pair: ω-factor `2.8×10⁻⁶` at
   `η = 1`, `0` at `η = 20`).
4. `sorted(w)` is **not** a function of the multiset (it differs inside
   bad fibers), so ω sees a strictly coarser invariant than `w`. No
   choice of `𝒦` helps: shrinking `𝒦` can only merge more pairs, never
   split a fiber. No symmetric function, and no function of modeSum,
   can separate inside a fiber — by definition of the fiber.

Consequence: ω distinguishes fibers and nothing finer. Route (a) — let
the ω-decay step kill pairs with different `w` — is dead, and any
future "repair" that keeps the hypothesis "equal modeSum" and only
changes the conclusion is impossible for the same reason.

## 5. D1, the analytic gap — decomposed, not closed

D1 is the re-derivation, inside `LineDStrongKickConc` /
`LineDStrongKickBridge`, of the step from the pair sum `Ψ_m(s/D)` to
the class average `Bsym_w`, with (fiber, w)-classes in place of
Γ-orbits. It is **open**, and §4 shows why it cannot be inherited from
the original derivation. Decomposed, D1 is three sub-steps, and the
decomposition matters because exactly one of them is supplied by ω:

- **D1a — pair sum → fiber average.** ω kills cross-fiber pairs
  (`Δ ≠ 0`, `hωlim`), so in the limit only within-fiber pairs survive,
  each with weight exactly 1. What the surviving within-fiber sum
  equals depends on `φ̂_s` on the fiber, and this is where the
  original derivation's Γ-invariance of `φ̂` was used: it made `φ̂`
  constant on Γ-orbits. For a fiber average one needs the corresponding
  statement for fibers — constancy of `φ̂_s` (in the modulus, or in
  the averaged sense the derivation needs) on fibers, or at least on
  the fibers meeting the support — stated as an explicit hypothesis
  and proved, not assumed. Note the sharper form of the problem: with
  weight 1 inside the fiber, the surviving term is the *coherent* sum
  `|Σ_{ξ ∈ fiber} φ̂_s(ξ)|²`, which mixes Γ-orbits inside a split fiber
  with their relative phases. So D1a needs either phase-coherence data
  for `φ̂_s` across Γ-orbits inside one fiber, or a proof that no
  split fiber meets the support (which removes the mixing).
- **D1b — fiber average = w-class average on the support.** This is
  exactly the statement that no split fiber meets the support (the O′
  statement, restricted to the support), plus support being a union
  of (fiber, w)-classes. At m = 8 both are verified exhaustively (§3);
  in general both are open, and D1b is where P_w would enter if it
  were proved (P_w + support-union-of-fibers gives
  support-union-of-w-classes, and P_w on support gives the equality
  of the two averages). Without D1b, even a completed D1a yields the
  fiber average, not `Bsym_w`.
- **D1c — identification of the average with the limit.** The
  limit-over-odd-coprime-residues step and the passage from the
  finite-`Fix` average to the strong-kick limit are untouched by
  route (b) and carry their original status (see §7, item 6).

So the honest status of the limit reading **(B2)** is: at m = 8 it
reduces to D1a (with the m = 8 verified facts doing the work of D1b)
plus the rest of 152-full; in general it is open at D1a and D1b
jointly. What route (b) has established is (B1) at m = 8 plus the
precise statement of what (B2) needs. Calling 152-w a theorem before
D1 is done would be citing a recomputation as a proof of a limit.

## 6. What G4b gives — and what it does not give for 152

G4b is fully closed as an analytic argument (waves 11–12; not Lean).
Its content, with definitions pinned at HEAD `d87dce0`:

- **(D) Duality:** `μ(β) = Σ_{n : [v(n)] = [β]} ∏_j ĝ_η(n_j)` via orbit
  orthogonality, with absolute convergence from a strip Cauchy
  estimate (`Σ|ĝ_η| < ∞`, `Σk²|ĝ_η(k)| < ∞`).
- **(N) Norm class, corrected:** if `[v(n)] = [β]` then
  `yp·NmZ(n) ≡ yp·Nm(β) [MOD gp]`, via `gp | 8y_m` (from
  `t(t+2) = 8y_m²` plus `gcd(gp, yp) = 1`), replacing the wave-10
  `4·gcd` sketch. The SNF pairing check confirms dlib's `FFT2(Φ)/D`
  pairing is exactly `e(−⟨β,ξ⟩)` — no sign/transpose error.
- **(P) Profile identity:** `Ztup m ĝ_η ν = Z_all^{dlib}(m, η)(ν.val)`
  for every `ν`, hence `Btup m ĝ_η ν = |Z_all|²`, for `m ≥ 2` and all
  real `η`; numerically at m = 3, `η = 1`, truncated tuple sums
  converge to dlib's `μ` with max error `4.71×10⁻⁵` at K = 40.
- **Remainders (wave 12, task 3):** `kickValInf N ĝ_η x =
  exp(iη·f_diag(x.val/N))` (character identity via `chi_add`, so
  negative-`k` mod subtleties are absorbed by `e`'s 1-periodicity),
  hence `kickMatInf N ĝ_η` is dlib's diagonal kick under
  `Fin N ≃ ZMod N` transport; `catMat N a = MN(N)` under exactly the
  bridge hypothesis `2·a·(−4) = 1` (i.e. `a = −8⁻¹`; without it the
  two sides are different matrices, and for even `N` both fail
  consistently); m = 1 bookkeeping complete
  (`F₁(η) = nuAvgUnits = Btup 1 ĝ_η 1` = window mean; the
  all-residue mean `(Btup 0 + Btup 1)/2` is not the G4 target).

What G4b does for the 152 assembly: it removes the "wrong profile"
objection to any future step that routes an average through the
bridge's `Btup` — the bridge profile *is* the dlib orbit profile, and
the bridge's tsum kick *is* the diagonal kick. In particular G3's
proved `S`-bound now applies to the bridge's `S`, which is the input
the 175-side window-average assembly needs.

What G4b does **not** do for 152, and must not be cited for:

- It says nothing about `φ̂_s`, mode sums, or ω, so it contributes
  nothing to D1a/D1b. The 152 pair sum and the 175 window average are
  different averages over the same profile family; identifying the
  profile does not derive either average.
- It does not touch G4c (diagonal model vs full fixed propagator
  `UN N = exp(iτN·A_N)·M_N`, `τ = 10⁻⁸⁰`, `A_N` the Weyl quantization
  of the full 32-mode symbol with `l ∈ {−1,0,1}` — non-diagonal).
  "kickMatInf = the actual kick" is false as an equality with the
  full propagator, and no scaling argument in main connects `τN`
  with `η = O(1)`. So even a completed 152-w is, until G4c is done
  or 175 is restated as a diagonal-model theorem, a statement about
  the diagonal model kick — and any transfer from 152-w toward
  TRACE-005 or BGS-001 is blocked at G4c, independently of D1.
- It is analytic, not Lean: a formalisation would still need
  finite-group character orthogonality over `ℤ²/Aℤ²`, the SNF
  parametrisation of the dual grid, the strip estimate, and the
  tuple-sum rearrangements.

## 7. Exact list of open inputs — nothing else is missing, nothing here is closed

For 152-w to be a theorem (any `m`, or the schema `152-w(m)` per `m`),
the following must all be supplied. Items 1–5 are mathematical;
item 6 is the unchanged remainder of 152-full; item 7 is formalisation.

1. **Exact Pcarry.** Lift Lemma Y (mod-D) to exact integer equality:
   `Y(y') = π(Y(y))` exactly, not just mod `D`. Current status: the
   exact per-class lemma (wave 11, task 2) is proved mod `p` for odd
   `p | D_m` as a sketch (Lucas polynomials: the multiset determines
   `N` and `Tr(A^L)`, then `B′ = Bζ^k` or `B̄ζ^k`; verified at m = 4,
   6, 8 and on both known m = 12 fibers, 0 failures) and open in
   general, with exactly three gaps: **G1** (odd prime-power lift;
   wave 12, task 1 reduced it to two named lemmas L6, H₀-orbit
   rigidity, and L7, coset inversion, sharing one unwritten subcase:
   `Cz` real mod `p`; no counterexample found, including at m = 14
   mod 169 with 1,105 groups), **G2** (2-primary component at
   per-class-multiset level), **G3** (one common `π` across
   components; wave 12, task 4 proved G3 does *not* follow from pure
   combinatorics — explicit abstract counterexamples with empty
   `Π₁ ∩ Π₂` — but the Fix-structure pair-contingency lemma holds
   in all 670,800 preserved cases tested and a full m = 12 random
   check over all five prime powers finds 0 failures; the precise
   remaining lemma is PC, common shift/conjugation for pair trace
   distributions). Pcarry is needed for exact `pair_sorted` and for
   the exact per-class lemma; the mod-D sketch suffices only for the
   mod-`D` support leg (§2).
2. **P_w per m / in general (D2).** Proved nowhere; verified at m = 8
   only, vacuous at m = 9, open globally at m = 12, untested at
   m = 10, 11, 13, ≥ 14. Needed for `Bsym_w = Bsym_Γ` beyond m = 8 and
   for D1b. A Lean proof or a finite-certificate proof (orbit
   representatives plus a checkable `sorted(w)` table) per `m` is the
   minimum for any main-bound use.
3. **Support a union of (fiber, w)-classes per m (D3).** The
   union-of-fibers part follows from §2 (modulo Lemma Y sketch).
   The w-class part needs P_w (item 2) or a separate argument that
   the support criterion's pair part is constant on (fiber,
   w)-classes. The m = 12 trap (full `(2Q − pair)` form essential)
   must be carried in any general-m argument.
4. **D1 derivation (D1a + D1b + D1c).** The re-derivation from the
   pair sum to `Bsym_w` with (fiber, w)-classes, identifying the
   `φ̂_s`-constancy hypotheses actually used, the relative phases of
   `φ̂_s` across Γ-orbits inside a split fiber (or the O′ statement
   that no split fiber meets the support, which removes the issue),
   and the limit-over-residues step. ω-decay may not be quoted for
   any within-fiber step (§4). This is the single most important
   open item: without it, route (b) is a recomputation, not a proof
   of a limit.
5. **G4c (diagonal model vs full fixed propagator).** An estimate
   relating `exp(iτN·A_N)` to `diag(exp(iη·f_diag))` and relating
   the regimes `τN` vs `η = O(1)`, or else an explicit restatement
   of 175 (and of any 152-w application) as a diagonal-model theorem.
   Blocks transfer to TRACE-005 / BGS-001, not the value reading (B1).
6. **Rest of 152-full, unchanged (D5).** `hSepC` (complex variant);
   J0 ensemble (Bessel `J0` is not in Mathlib; the Gaussian case has
   the ω lemmas, the J0 case needs analytic input); the N-step `hN`
   (iterated strong limit, `t_N → t*` for true `Psi_m`, not just
   `PsiMode`); identification of finite `Fix m` with torus `Fix_m`;
   symmetry of coefficients `c`. Also: support-independence of `s`
   (odd, coprime to `D`) is a bridge-document claim (D3), not
   re-proved here, and must be re-verified before any main-bound use.
7. **Lean formalisation (D6).** Definitions of `w`, (fiber, w)-class
   and `Bsym_w` in the style of `LineDParity`; the Lemma Y sketch
   (all four components) as Lean proofs; the m = 8 certificate or
   proof of `hSep_w`; the D1 derivation; the G4b formalisation;
   full axiom audit (standard axioms only, `sorryAx = 0`); and
   re-verification of every definition against the then-current
   main HEAD before any push. Until this is done, nothing in §§1–6
   is a Lean theorem, and the m = 8 value `318335/20808` remains an
   exact replay, not a formalised result.

**Bottom line.** What the programme has, for 152 via route (b):
(B1) the value `318335/20808` at m = 8, with (fiber, w)-classes
coinciding with Γ-orbits on the support; Lemma Y at mod-D level as a
complete proof sketch, giving the support-union-of-fibers leg; G4b
fully closed analytically, giving the profile identification for the
175 side; and ω-blindness proved in principle, which kills route (a)
and fixes D1 as the analytic gap. What it does not have: the limit
reading (B2) at any `m` (blocked at D1, and in general at P_w), exact
Lemma Y (blocked at Pcarry: G1/L6/L7, G2, G3/PC), transfer to the full
kick (blocked at G4c), or any Lean theorem in this chain.

## 8. Sources

- Route (b) restatement, m = 8 computation, D1–D6 obligations:
  `methods/wave8_task3_152w_restatement.md`,
  `methods/wave8_task3_bsymw_m8.py`,
  `methods/wave8_task3_bsymw_m8_result.json`.
- Pair identity and Lemma Y (original statement):
  `methods/pair_sorted_identity_note.md`.
- ω-blindness: `methods/wave7_omega_w_note.md`,
  `methods/wave7_omega_w_test.py`.
- Lemma Y components: `methods/wave8_lemmaY_proof_attempt.md`,
  `methods/wave9_lemmaY_P3prime.md`,
  `methods/wave10_p2_topbit.md`,
  `methods/wave11_perclass_pattern_proof.md`,
  `methods/wave11_task3_pi2pi3_compatibility.md`,
  `methods/wave12_lemmaS_proof.md`.
- Exact per-class lemma, G1, G3:
  `methods/wave11_perclass_proof.md`,
  `methods/wave12_G1_lift.md`,
  `methods/wave12_g3_common_pi.md`.
- G4b: `numerics/wave11_task4_G4b_duality.md`,
  `numerics/wave12_task3_G4b_remainders.md`,
  `numerics/wave10_task3_G4_identification.md`.
- Separation background (O1/O*/O′): `methods/ostar_m8_note.md`,
  `methods/oprime_m8_note.md`, `methods/sep_new_principle_note.md`,
  `methods/gamma_orbits_per_fiber_note.md`.
