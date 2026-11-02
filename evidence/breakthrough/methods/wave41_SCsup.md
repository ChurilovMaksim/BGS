# Wave 41, task 4 — SC-sup: proved modulo the S-tuple dihedral lemma

## Verdict

No counterexample: 0 partial fibers in every census below, and SC-sup
is proved modulo exactly one named lemma (the S-tuple dihedral lemma,
§4), which is verified exactly on all fibers at all enumerable
components for m = 3..30 and m = 32, 36, 48, 60, 64, 72, 96, 128.
Two steps are proved unconditionally:
odd-q full support (§2) and dihedral invariance of the support
condition in the class sums (§3). Repository untouched; no Lean built.

## 0. Setup (wave-16 definitions)

Component fiber at q ‖ D_m: kernel points mod q with the same sorted
multiset. Component support (s = 1 torsion criterion): y supported iff
(2·Qnum(z) − z·y) ≡ 0 (mod q) for every torsion rep z = Hv/4,
v ∈ ker(H mod 4), Qnum(z) = D·(z·v)/4 (integer since 4 | D).
Support is Γ-invariant (torsion reps closed under dihedral moves,
Qnum invariant), so partial ⟹ split. SC-sup is what H0's proof uses
to upgrade "a point of a split component fiber is supported" to
"the whole fiber is supported", which the Δ-counting needs.

## 1. Reduction of the support condition (proved)

Let y ∈ ker(H mod q), Hy = q·t (t integer). H is symmetric
(circulant, 6 on diagonal, −1 at ±1), so for z = Hv/4:
4(z·y) = (Hv)·y = v·(Hy) = q(v·t). Also 2·Qnum(z) = D(z·v)/2.
Hence the support condition at q is equivalent to

  v·t ≡ 2·D_q·(z·v) (mod 4) for all (v, z), D_q = D/q.

(multiply the original condition by 4, divide by q.)

## 2. Odd q: full support (proved)

For odd q, D_q = D/q is even, so the §1 condition is v·t ≡ 0
(mod 4) for all v. But q(v·t) = 4(z·y) ≡ 0 (mod 4) and q is odd,
so v·t ≡ 0 (mod 4) always. Hence every point at odd q is
supported: SC-sup at odd q is unconditional, and no computation
is needed there. (Confirmed: supp = q at every odd q censused.)

## 3. Support depends only on class sums, dihedrally (proved)

Torsion reps v ∈ ker(H mod 4) are arithmetic progressions mod 4:
v_k = (a + kd) mod 4 with m·d ≡ 0 (mod 4), so v — and hence
z = Hv/4 — is C-periodic with C = 4 (4|m), C = 2 (m ≡ 2 mod 4),
C = 1 (m odd). Write S_r(y) = Σ_{i≡r mod C} y_i. Then
z·y = Σ_r z_r S_r, and 2·Qnum(z) ≡ 2^{f−1}·((z·v) mod 2)
(mod 2^f) at the 2-part q = 2^f (D_q odd). So component support
is a function of S alone. It is dihedral-invariant in S: a
dihedral permutation π of coordinates sends Σ_r z_r S_{π(r)}
to Σ_r (π⁻¹z)_r S_r, and π⁻¹z is again a torsion rep's z
(V4 closed under dihedral moves, H commuting with them) with
the same (z·v) mod 2, so the conjunction over all z is
unchanged. The dihedral group is exactly right: it is the
commutant of H in permutations (H's symbol has only k ↔ −k
collisions), so no larger coordinate group preserves the
condition set.

## 4. S-tuple dihedral lemma (open in general; verified exactly)

Lemma: for y, y′ in the same component fiber, S(y′) is a dihedral
permutation of S(y) (rotations + reversal for C = 4; swap-or-equal
for C = 2; equal for C = 1, where S = Σy is multiset-determined).
Verified exactly, 0 violations: all fibers at all enumerable
components for m = 3..30 and m = 32, 36, 48, 60, 64, 72, 96, 128
(this wave), including odd q and the 2-part cases at 8192, 32768,
131072. SC-sup follows: support is a dihedral-invariant
function of S (§3), and S varies only dihedrally in a fiber.

## 5. Direct census: 0 partial fibers

All fibers (not just split) at all enumerable q, exact integer
arithmetic, wave-16 torsion criterion: m = 12, 16, 24 (this wave)
and m = 30, 32, 36, 48, 60, 64, 72, 96 (background run):
0 partial fibers everywhere. At m = 128 the 2-part and all
q ≤ 332929 are checked (0 partial); larger q's there are odd
(covered by §2) or skipped. Spot values: (32, 8192): 278 fibers,
15 split, supp 512/8192, 0 partial; (64, 32768): 539 fibers,
supp 2048/32768, 0 partial; (128, 131072): 1056 fibers,
supp 8192/131072, 0 partial. Support fraction at the 2-part is
1/|V4| throughout (1/16 for 4|m, 1/8 for m ≡ 2 mod 4).

## 6. Narrowing for a full proof of the lemma

At the 2-part for 4|m (f ≥ 7), the period-4 constraints on S
(12S_0 ≡ 36S_1, 204S_1 ≡ 36S_0 mod 2^f) force
S = 2^{f−5}·(3a+8c, a, 3a−8c, 17a−48c) with (a, c) ∈ ℤ/32 × ℤ/4:
only 128 possible S-tuples, with explicit dihedral action
(rotation: (a,c) ↦ (3a−8c, −a+3c); reversal similarly).
So the lemma is now a statement about the map fiber ↦ dihedral
class of (a, c); proving it needs the fiber structure of Fix
sequences (which permutations relate fiber points), not more data.

## 7. What is NOT claimed

The S-tuple dihedral lemma is not proved in general, so SC-sup
is proved modulo that lemma, not unconditionally. The Δ → 0
recount v3 therefore still carries SC-sup as a hypothesis, now
reduced to this single lemma with exact verification at 25 values
of m up to 128 (all fibers) and 0 partial fibers to m = 128.

## Files

- This note: wave41_SCsup.md
- Checks: wave41_SCsup_check.py (+ .log), wave41_SCsup_Stuple.py
  (+ wave41_SCsup_Stuple_big.log), wave41_SCsup_explore.py,
  wave41_SCsup_ressums.py
