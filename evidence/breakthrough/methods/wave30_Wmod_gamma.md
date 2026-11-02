# Wave 30, task 2 — S⁽ᵈ⁾ cancellation laws from the gluing maps γ_q

**Verdict: mixed.** The τ-structure IS derived from γ_q. The parity and
moment laws hold universally over class-preserving-involution (cpi)
pairs, so they do not need the failing condition — but their closed-form
mechanism is still open. The antipodal law is NOT implied by γ_q, even
with cpi form and S-constancy; its precise scope and the extra input it
needs are pinned down below. Scope: m = 12, D = 1536796800, notation as
wave 29 task 4 (τ with y′ = τ(y), δ = w′ − τ(w), classes r = {r, r+4, r+8}
mod 4). All checks are exact integer arithmetic on the wave-18 census
(772 orbit pairs, 152 failing). Repository untouched, no Lean built.

## 1. The constraint system IS γ_q data

**Lemma (verified 772/772 pairs × all q ‖ D).** The value-fibers of
v_q = y mod q equal the orbits of Stab(v_q), and Stab(v_q) is recovered
from Γ_q alone: Γ_q = Stab∘γ₀ (right coset), so
Stab = {γ∘γ₀⁻¹ : γ ∈ Γ_q} for any γ₀ ∈ Γ_q. Hence the constraint
"τ(j) lies in the v_q-fiber of y′[j] mod q" is exactly "τ(j) lies in the
Stab_q-orbit of γ₀(j)" — a statement purely about Γ_q. A permutation
satisfying all five orbit constraints is a valid τ (CRT over the coprime
q's), and vice versa.

## 2. τ-structure derived from γ_q (CRT assembly)

Write ℤ/12 ≅ ℤ/4 × ℤ/3. The γ_q data forces τ to be a CRT map
(mod-4 map × mod-3 map) with uniform class action:

- **q = 81.** Γ₈₁ is IDENTICAL for all 152 failing pairs:
  {(1,0),(1,4),(1,8),(−1,1),(−1,5),(−1,9)} = ⟨+4, −j+1⟩. So v₈₁ has
  period 4 with pattern (a,a,b,b), a≠b (a=b would enlarge Stab to all
  of Dih). Hence τ(j) mod 4 ∈ {j, 1−j} mod 4: class pairs {0,1}, {2,3}.
  Counting (τ bijective, 3 positions per class) gives class maps in
  {id, swap01, swap23, swapboth} — mixed swaps are still allowed here.
- **q = 128.** Γ₁₂₈ = 12 even-k maps ⟹ v₁₂₈ has period 2 with distinct
  parities ⟹ τ preserves parity; parity + class pairs ⟹
  class-preserving (Type I). Γ₁₂₈ = all 24 (constant v₁₂₈) ⟹ no parity
  constraint — and indeed all 15 Type II pairs have constant v₁₂₈
  (21 Type I pairs also do, so constancy is necessary, not sufficient).
- **q = 49.** With Stab₄₉ = ⟨+3⟩ (v₄₉ values distinct), a reflection
  in Γ₄₉ forces τ(j) ≡ −j+c mod 3 (c = k mod 3 of the reflection);
  rotation-only Γ₄₉ forces τ(j) ≡ j+c mod 3. All Type I rows have a
  reflection in Γ₄₉; 14/15 Type II rows are rotation-only. Exception
  explained: group 689 has a reflection in Γ₄₉ but is Type II, because
  Stab₄₉ there has order 8 (pattern (a,b,b)), so the reflection
  constraint is fiber-vacuous and the rotation wins at j ≡ 1 mod 3.
- **q = 25.** The mod-6 fiber pairs {r, −r+k} are compatible with the
  CRT assembly and, jointly with the other constraints, kill the mixed
  class maps: **0/772 pairs admit a mixed CRT map** (swap01 or swap23
  alone); over failing pairs the valid CRT maps are exactly
  (id, refl) × 131, (swapboth, rot) × 15, both × 6 (value repetitions;
  the cpi one is canonical). The 15 pairs over all 772 with NO valid
  CRT map are all non-failing, so CRT form is universal on failing
  classes, as tasked.

**Corollary.** Type I τ = CRT(id₄, reflection₃) is automatically an
involution with exactly one transposition + one fixed point per class
(a reflection on ℤ/3 has cycle type (2,1)). Type II τ =
CRT(reflection₄, rotation₃) has order 3 (wave 29: "not an involution").
For Type I this derives THE τ (unique cpi); for Type II it derives a
canonical τ with class-reflection form (other non-CRT τ's exist from
value collisions, e.g. group 381).

## 3. Parity and moment laws: universal over cpi pairs, mechanism open

For the 697 pairs with a cpi τ (137 failing, 560 not):

- **Parity.** Failing cpi defect sets: () 80, (1,3) 29, (0,2) 27,
  (0,1,2,3) 1 (group 594, the 8-point exception). So the strong parity
  law holds for failing pairs except 594, as wave 29 stated ("or all").
- **Moment.** Σⱼ j·δⱼ ≡ 0 mod 12 for ALL 697 cpi pairs — failing or
  not, S-constant or not. Hence the failing condition (sorted(w)
  equality) is PROVABLY NOT the extra input for these two laws.
- **What is needed instead:** the full Fix relation (w = Hy/D, exact
  integer division) together with the γ_q-derived cpi form. The
  mechanism is still open; two attempts failed and are recorded:
  (a) reduction to mod-3 class sums W_r of w (the predicted congruence
  W_{1−c} ≡ W_{2−c} mod 3 holds only 213/697 — the reduction itself
  was algebraically wrong, since Σ j·δⱼ also involves w′−w terms);
  (b) a D·M1 bracket argument (bracket divisible by 12, but index
  wrap-around breaks the integer identity; the needed congruence
  Σ t_m·y[m] ≡ 0 mod D is unverified). The universality (697/697)
  says a mechanism within (cpi form + Fix) exists; finding it is the
  remaining step for these two laws, not the failing condition.

## 4. Antipodal law: NOT implied by γ_q — scope and extra input

Among cpi pairs, δ-support sizes are quantized: |sup| ∈ {0, 4, 8} only.
Full table (|sup|, antipodal, S-constant, failing):

| |sup| | antipodal | S-const | failing | count |
| 0 | yes (vacuous) | yes | yes | 80 |
| 4 | yes | yes | no | 224 |
| 4 | yes | yes | yes | 56 |
| 8 | no | no | no | 245 |
| 8 | no | yes | no | 91 |
| 8 | no | yes | yes | 1 (group 594) |

Consequences:

- **Antipodal ⟺ |sup| ∈ {0,4}** among cpi pairs: all 280 4-point
  pairs satisfy the antipodal positioning + N(p) = N(p+6); all 337
  8-point pairs fail it (tsup has 8 elements, not 4). Related
  quantizations: 4-point ⟹ S-constant (280/280); S-varying ⟹ 8-point
  (245/245); but S-constant does NOT imply 4-point (92 8-point
  S-constant pairs).
- **Counterexamples to "γ_q ⟹ antipodal":** the 91 S-constant
  non-failing cpi pairs with |sup| = 8 share the γ_q-derived cpi form
  yet fail antipodal; and group 594 (failing, 8-point) fails it. So
  neither γ_q + cpi form, nor adding S-constancy, nor adding the
  failing condition, implies the antipodal law.
- **Extra input needed:** the antipodal law is a value-level identity
  (N(p) = y_{p−1}+y_{p+1} = y_{p+5}+y_{p+7} = N(p+6)) constraining y
  against itself. γ_q constrains y′ in terms of y mod q; it cannot see
  y-against-y identities, and no coarser invariant tested (Γ_q tuple,
  cpi form, S-constancy, failing status) implies it. The precise
  remaining input is the 4-point/antipodal value identity itself:
  δ is a 4-point rectangle whose τ-image is {x, x+2, x+6, x+8} with
  y[x]+y[x+2] = y[x+6]+y[x+8]. For failing classes the open question
  is therefore sharper than wave 29 §8 stated: not "derive antipodal
  from γ_q" (impossible, by the counterexamples above) but "why do
  failing pairs have |sup| ∈ {0,4}" — with exactly one exception,
  group 594.

## 5. What remains open (do not overclaim)

- Closed-form mechanisms for the parity and moment laws within
  (cpi form + Fix) — universality is proved (697/697), mechanism is
  not; the two failed attempts in §3 are dead ends, do not retry.
- The 4-point ⟹ antipodal positioning holds on all 280 4-point pairs
  but its mechanism is also open; and the failing-class question is
  now "why |sup| ∈ {0,4}" (one exception: 594).
- Type II pairs need their own δ-analysis (no cpi τ exists for them);
  general m is untouched (census is m = 12 only).

## Files

- This note: wave30_Wmod_gamma.md
- Scripts: wave30_gamma_extract.py, wave30_gamma_analyze.py,
  wave30_gamma_check.py, wave30_gamma_corr.py, wave30_gamma_crt.py,
  wave30_gamma_refine.py, wave30_gamma_mech.py, wave30_gamma_final.py.
  Repository untouched; no Lean built.
