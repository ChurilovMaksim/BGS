# Wave 25, task 5 — C(y) at general m, and the Σ yᵢwᵢ constancy mechanism

## Verdict

1. **C(y) holds wherever it could be tested** (m=8: 39/39; m=16 lifts:
   10/10, all off-support). At m=20 it is **untested, not failed**:
   0 component splits and 0 sampled gluing splits.
2. **The constancy mechanism is NOT proved in general; the wave-23
   identity argument proves only divisibility, not constancy.**
   Exact constancy fails on 264/762 m=12 groups. What survives is a
   sharp law (failing classes only) plus one precisely named open
   lemma (the W-mod lemma, §5).

## 1. C(y) separation tests

| m | test | result |
|---|---|---|
| 8 | full census, 39 split fibers (all off-support) | C separates 39/39 |
| 16 | 10 component lifts at q=2048 (all EMPTY) | C separates 10/10 |
| 16 | on-support | vacuous: 0 gluing splits in wave-22's 122,880,000 checks |
| 20 | 0 component splits at any prime power | no off-support test |
| 20 | sampled gluing search: 4000 points × 15 pairs × 1600 shifts = 96,000,000 checks | 0 splits found |

m=20 bound: pair-shift-detectable on-support split mass < 7.5×10⁻⁴
(95% Poisson bound 3/4000), conditional on pair shifts capturing
gluing (3+ component shifts missed, as in wave 22).

## 2. Mod-D lemma (proved)

Let y, y′ ∈ Fix_m (representatives in [0, D)) satisfy: for every
prime power q ‖ D, y′ mod q is a dihedral image of y mod q
("component-wise dihedral", i.e. a gluing pair). Then for every
dihedral-invariant integer polynomial f in y, D | f(y′) − f(y).
Proof: f(γ_q y) = f(y) as integers by dihedral invariance, so
f(y′) ≡ f(y) (mod q) for all q; the q's are coprime, hence D | diff.
Applies to: A_d = Σ yᵢyᵢ₊d (all d), C (symmetric kernel), and
D·S (since D·S = 6A₀ − 2A₁ with A₀ = Σ yᵢ² fiber-equal).
Verified at m=12: C diffs divisible by D 767/767; A₁ diffs
divisible by D 767/767 — including the 5 non-gluing groups' pairs,
so the hypothesis is sufficient, not necessary.

## 3. Naive mechanism refuted

The wave-23 claim "the identity forces the ab-sum constant" is
incomplete: the identity plus §2 gives only D | A₁-diff, and exact
constancy (diff 0) fails. Cross-tab over the 762 m=12 groups
(pw_ok, component-wise dihedral, S constant across orbits):

| pw_ok | dihedral | S const | groups |
|---|---|---|---|
| False | yes | yes | 152 (the failing groups) |
| True | yes | yes | 341 |
| True | yes | no | 264 ← counterexamples to the naive mechanism |
| True | no | no | 5 (component-split fibers, not gluing) |

So gluing structure alone does not force constancy; 264 gluing
groups have S varying. k = A₁-diff/D takes only the values
0 (493 pairs), −D (221), +D (43), −D/3 (4), −2D/3 (3), +D/3 (2),
−4D/3 (1): A₁ diffs are always multiples of D²/3.

## 4. Sharp law at m=12 (failing classes)

On the 152 failing (fiber, w)-classes, **everything** is constant:
S⁽ᵈ⁾ = Σ yᵢwᵢ₊d for ALL d = 0..11 (0 varying), A_d for all d,
W_d = Σ wᵢwᵢ₊d for all d; C separates 152/152. Moreover, in every
split fiber (762/762), S diffs are multiples of 2D/3 (0 violations);
S takes 1 value in 493 groups, 2 in 264, 3 in the 5 non-gluing
groups. w range on all census reps is [−1, 5], as required for §5.

## 5. Smallness reduction: the remaining lemma

y = adj(H)·w exactly: Hy = Dw with H invertible over ℚ, and
det(H_m) = D_m (verified exactly for m = 2..8; eigenvalues
6 − 2cos(2πj/m) > 0, so det > 0). H is circulant symmetric, hence
so is adj(H), so S = Σ_d X_d W_d and A_d = Σ_e Y_{d,e} W_e with
integer coefficients: S/A_d constancy follows from W_d constancy.
And |W_d| ≤ 25m (wᵢ ∈ [−1, 5]), so 50m < D_m for m ≥ 3: **if**
W_d diffs were divisible by D for failing-class partners, exact
constancy would follow. That "if" is the open **W-mod lemma**:
it does NOT follow from y's component-wise dihedral structure,
because w mod q is not determined by y mod q (division by D),
and w′ is not a global dihedral image of w (0/152 failing classes).
So the mechanism is reduced to one precise lemma, not proved.

## 6. Contrasts: neither divisibility law is a general fiber law

- m=8 split fibers (component splits): S diffs are exactly ±D
  (28 pairs +D, 11 −D); divisible by D 39/39, but never multiples
  of 2D/3. S takes exactly 2 values per fiber.
- m=16 lifts (component splits): S diffs are NOT divisible by D
  in 10/20 pairs. So D-divisibility (m=8) and the 2D/3 step (m=12)
  are both split-type-specific, not fiber laws.
- Numerical coincidence (unproven): the m=12 step 2D/3 and the m=8
  step D both equal 8D/m; both m are divisible by 4. Test this
  pattern if gluing pairs are ever found at m=16 or m=20.

## Files

Scripts: wave25_m8.py/.json, wave25_lifts.py,
wave25_lifts_m16.json, wave25_lifts_m20.json, wave25_m12.py/.json,
wave25_glue20.py/.json. Repository untouched; no Lean build.
