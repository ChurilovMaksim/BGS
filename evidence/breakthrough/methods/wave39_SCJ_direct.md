# Wave 39, task 1 — SCJ tested directly at m = 180: realization is FULL, not thin

## Verdict

Realization thinness does NOT save polynomial SCJ. At m = 180, every blind
configuration realizes as a distinct joint fiber with large Δ_F: one section
alone (locked 625-fiber 0, free 729-fiber 0, locked orbit of a, top-digit pair
k = 20 ↔ 11) contributes ΣΔ_F ≥ 2.96×10²⁶, killing c_J ≤ 11. Polynomial SCJ
is conditionally refuted along m = 9t (B(m) ~ D_{3t} = D_m^{1/3},
superpolynomial), modulo F1–F4 below. But Δ → 0 is NOT killed: it needs only
ΣΔ_F(C) = o(D_m), and D_m^{1/3} = o(D_m). The wave-35 slot should be restated
as SCJ′: ΣΔ_F(C) ≤ D_m^γ for some γ < 1 (γ = 1/3 along m = 9t).

## 1. Setup (m = 180)

Locked rep a = 625-fiber-0 rep 0, C = (0, 550), period 30. Free pair at 729
fiber 0: b (C = (378, 540), k = 20) vs b′ (C = (378, 297), k = 11), the
top-digit move C ↦ C − 243√2. Blind components q0 (all kernel sequences
blind for the 729-move, wave 38): 49, 121, 361, 841, 1681, 3481, 72361.
A configuration is a tuple o = (o^{(k)}) of kernel sequences at the q0's
(zeros at all other components); its fiber F(o) is fixed by the sorted
multiset of position-tuples (a_i, b_i, o^{(k)}_i) (CRT injectivity, as in
the wave-36/37 slice grouping). D_180 computed exactly (138 digits).

## 2. Test A — full-tuple collision: 20/20

Sanity first: single-o collisions reproduce wave 38 exactly (pair collides
at all 7 q0's, non-colliding control k = 20 vs 10 never collides). Then 20
random full tuples (all 7 components nonzero): the tuple-multiset for b
equals that for b′ in 20/20 cases. Mechanism (now verified, not just
argued): each (a, o^{(k)})-fiber is a union of 12-triples (wave 38), and
joint fibers are intersections of triple-unions, hence still triple-unions,
so the top-digit move permutes within every joint fiber.

## 3. Test B — distinctness: PROVED for this section, not just sampled

Sampled: 30/30 configs differing everywhere and 30/30 differing at one
component give different tuple-multisets. Proof: the 180 pairs (a_i, b_i)
are ALL DISTINCT (verified). If M(o) = M(õ), some position permutation π
has (a_{π(i)}, b_{π(i)}, õ^{(k)}_{π(i)}) = (a_i, b_i, o^{(k)}_i); distinct
(a, b) pairs force π = id, hence õ = o. So o ↦ F(o) is injective.
Stab_Γ(a, b) = {id} (all 360 γ's checked). Genuine Γ-probes on o at 72361
(period 30): rotations by 1, 7, 11, 29 and reversal give 0/5 collisions.
(Caution, artifact found and dismissed: an early 5/7 count was rotations
by multiples of 3 fixing o at 49, which has period 3 — same config, not a
collision.)

## 4. Per-fiber Δ_F ≥ 388,800

729-orbit phases via the wave-34 formula (D_180, spreads ~10⁻¹⁴): the free
pair has phases 1.978 vs −2.211 rad, gap θ = 2π/3 exactly (3rd roots).
Diagonal orbit sizes of (a, b, o) and (a, b′, o) are both 360 (full Γ).
Other diagonal orbits can only help the bound, since
|Σ_j w_j ζ_j|² ≤ |F|² − 2ww′(1 − cos θ). Hence
Δ_F ≥ 2·360·360·(1 − cos 2π/3) = 388,800 per fiber.

## 5. Total at m = 180: ≥ 2.96×10²⁶, c_J ≤ 11 dead

B(180) = 49·121·361·841·1681·3481·72361 = 762,185,960,484,837,066,409
≈ 7.62×10²⁰ configurations, all realized as distinct fibers (§3), each
with Δ_F ≥ 388,800 (§4). One-section total ≥ 2.96×10²⁶, vs 180¹¹ ≈ 6.43×10²⁴
and 180¹² ≈ 1.16×10²⁷. Other sections (625-fiber 1, 729-fiber 1 with its
pair, other locked orbits/free pairs, the 2-part factor) only add.
C-membership: S = {625, 729} (both component multisets are split fibers),
same convention as the m = 60 prototype in waves 35–37.

## 6. Family m = 9t: conditional refutation of polynomial SCJ, SCJ′ survives

For m = 9t (3 ∤ t), 729 is the full 3-component (v₃(D_m) = 6) and
D_{3t} | D_{9t} (factorization D_{9t} = D_{3t}·(α^{3t} + 1 + α^{−3t})²).
If (F1) 729 splits with a top-digit colliding pair, (F2) enough components
of D_{3t} are non-split and all-blind for the 729-move at m (top-digit-law
conditions v₃(d_a) ≤ 1, v₃(period o) ≤ 1), (F3) the phase gap stays bounded
away from 0, (F4) distinctness generalizes (e.g. distinct (a, b) pairs),
then B(m) ≥ D_{3t} ~ ρ^{m/3} = D_m^{1/3} (ρ = 3 + 2√2), all realized with
Δ_F ≥ c > 0 — superpolynomial, so no fixed c_J works. F1 is verified only
at m = 36, 180; F2–F4 are open. Replacement: SCJ′ with γ = 1/3 along m = 9t
still implies ΣΔ_F(C)/D_m → 0, so mechanism C does not threaten Δ → 0.

## Limits

No Lean built; repository untouched. Scripts: wave39_SCJ_direct.py (tests +
phases), wave39_SCJ_verify.py (injectivity, orbit sizes, Γ-probes).
Per-fiber Δ_F uses the standing Δ_F = |F|² − |Σ w_j ζ_j|² convention and
the wave-34 phase formula (validated at 625, here at 729 with spreads
~10⁻¹⁴). The m = 180 bound is unconditional except C-membership by the
waves 35–37 convention; the family statement is conditional on F1–F4.
