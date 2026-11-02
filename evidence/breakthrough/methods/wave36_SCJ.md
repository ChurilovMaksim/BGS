# Wave 36, task 1 — SCJ via locked/free: decomposition proved, polynomial form NOT proved

## Verdict

Locked/free decomposition is proved exactly (§1) and gives a
polynomial bound for *rigid* (others-zero) joint fibers. But
SCJ in wave 35's total form — total joint contribution ≤ m^{c_J}
over ALL global fibers — is NOT proved by it, because
rigidity-as-zero is FALSE: at m = 60, nonzero components at
49/121 are blind for 625-moves and at 361/841 blind for
81-moves (§2, exact triple tests). Joint fibers with nonzero
blind components exist, and their count multiplies by the
blind kernel sizes. Polynomial SCJ now needs two named
inputs: the Blindness Law (which (q0, q*) pairs are blind)
and a bound on the blind product B(m) (§3). Unconditional
yield: the per-fiber structure and the counting formula
ΣΔ_F(joint) ≤ m²·S₂·∏(1+a_q)·B(m). Repo untouched, no Lean.

## 1. Locked/free decomposition (proved)

For a global fiber F with split set S, |S| ≥ 2 (components
whose component fibers have > 1 Γ-orbit): q ∈ S is LOCKED
if all diagonal orbits of F project to one orbit at q,
FREE if they project to ≥ 2 orbits; T(F) = free set.

**Theorem.** Diagonal orbits of F factor as {locked orbit
tuple} × {all orbits at T} (up to alignments at non-split
components), and phases factor via Lemma F (φ̂ = (1/D)·Π_q
S_q, S_q constant on orbits). Hence Δ_F > 0 forces T ≠ ∅
with misaligned free phases: Δ_F = |F|² − |Σ_j w_j ζ_j|²
> 0 iff ≥ 2 distinct free phases ζ_j occur with weight.

Example (wave 34, re-verified): m = 60, (81, 625) slice —
81 locked (1 orbit), 625 free (5 orbits, 5th-root phases);
each joint fiber has exactly 5 diagonal orbits, Δ_F = |F|²
(sizes 300/600, Δ_F = 90000/360000), 24 fibers per section.

Pair bound (wave 34 §1, same proof globally): every fiber
has size ≤ m², since a point is fixed by (y₀, y₁), both in
its own multiset (≤ m values).

## 2. Pinning and blindness: rigidity-as-zero is FALSE

A non-split component q0 is PINNING for a free move if it
forces the free orbit unique in the joint fiber, BLIND if
not. Exact test: fix a locked representative a and a kernel
sequence o mod q0, vary the free component over its
orbits, compare triple multisets (a_i, b_i, o_i); a
collision means o does not pin that move, so the fiber
containing (a, b, o, zeros) has ≥ 2 diagonal orbits with
distinct free phases, hence Δ_F > 0.

Component data at m = 60, re-verified exactly: q = 81: 1
split fiber (36 pts, 3 orbits of 12, period 12); q = 625: 2
split fibers (150 pts, 5 orbits of 30, period 30); q = 128:
39 fibers, 0 splits; kernel size = q at every component.
Other odd components have NO splits (49: 12 fibers, 121:
11, 361: 19, 841: 57, all single-orbit), so their phases
are constant on orbits, as §1 needs. Kernel periods: 49 →
3, 121 → 12, 361 → 20, 841 → 10 (one period per component:
kernel is a line).

Triple-test results (nonzero kernel sequences):

| q0 | blind for 625-moves | blind for 81-moves |
|----|---------------------|--------------------|
| 49 | ALL 48/48 | 0/48 |
| 121 | ALL 120/120 | 0/120 |
| 361 | 0/360 | ALL 360/360 |
| 841 | 0/840 | ALL 840/840 |
| 1681, 3481, 72361, 361201 | 0/6 sampled | 0/6 sampled |
| 5202961 | 0/19 sampled | 0/19 sampled |

Consequences. (i) A joint fiber with free set {625} may
carry ANY sequence at 49 and 121 (49 × 121 = 5929 combos,
each a distinct fiber with Δ_F > 0 by §1: 49/121 are
singleton fibers, hence constant phase factors). (ii)
Dually, free set {81} may carry any sequence at 361/841.
(iii) Free set {81, 625} needs components blind for BOTH
moves: only zero qualifies among tested components.
Blindness is a property of the PAIR (component, free set),
not of the component alone; its law is open (periods do
not decide it: 49, period 3, is blind for 625 but pins 81,
while 841, period 10, does the opposite). Large components:
sampled sequences pin both moves at all five (5202961:
19 scalings of the (2281, 0) direction, gcd(a, q) = 2281).
Sampling caveat: first-by-y0 sequences, not exhaustive
over kernel lines — so large-component blindness is
sampled, not proved; the blind product at m = 60 comes
from the small components, not from sampled large ones.

## 3. Revised counting, and what SCJ needs

Let a_q = n_q·s_q (points in split fibers at q), S₂ ≤ 8m²
the RB3′ 2-part bound, B(m) = total blind configurations
summed over free sets. Each joint fiber lies in a tuple
(split fibers at S) × (2-fiber) × (blind configuration),
and ΣΔ_F over a tuple is ≤ m² × (∏_{q∈S} s_q)·S₂. Hence

  ΣΔ_F(joint) ≤ m²·S₂·∏_{q split-eligible}(1+a_q)·B(m).

With SplitPrime (split ⇒ p | m, all censuses), SizeLaw
(s_q ≤ C·m_p², C ≤ 6 in all data), CountLaw (n_q ≤ p²,
proved in the f′ = 2 regime, wave 35), ∏(1+a_q) is
polynomial (∏ m_p² ≤ m², ∏ p² = rad(m)² ≤ m²,
2^{ω(m)} ≤ 2m). So the ONLY remaining obstruction to
polynomial SCJ is B(m). At m = 60, B(m) ≥ 49·121 = 5929
for T = {625} alone (≥ 361·841 for T = {81}); the wave-35
rigid total 8.64×10⁶ is a lower bound on the true joint
total, not the total. Precise falsification condition: a
family where B(m) grows superpolynomially. None is
exhibited here; the Blindness Law would decide it (blind
periods bounded ⇒ B(m) ≤ D_d constant, SCJ holds; blind
periods growing with m ⇒ B(m) up to ~D_m^{1/2}, and only
the density form ΣΔ_F/D_m → 0 could survive).

## 4. What is NOT claimed

- Polynomial SCJ: OPEN (needs Blindness Law + blind-
  product bound). Wave 35's bare census hypothesis is
  superseded by §3: SCJ ⟺ B(m) polynomial, given
  SplitPrime, SizeLaw, CountLaw, RB3′, SIZE, H0 (Lemma F
  proved, wave 35). Locked/free (§1) and the m = 60
  blindness table (§2, small components) are exact.
- Large-component blindness is sampled, not exhaustive;
  full kernel-line coverage there is open. No Lean claimed.

## Files

- This note: wave36_SCJ.md.
- wave36_m60_components.py, wave36_pin_test.py (pair
  test, superseded), wave36_pin_test2.py (triple tests),
  wave36_periods.py, wave36_pin_test4.py (large comps,
  4/5 done, killed before the 5.2M loop), wave36_pin_test5.py
  (5202961, fast indexed version), wave36_singleton_check.py.
