# Wave 22, task 3 (retry) — JBL 2-part exclusion: FALSE as stated, harmless for JBL

## Verdict

The 2-part exclusion is **false** as stated in wave 20 §4: there are
2-part roots of unity, invisible to all trace data, that are not in
⟨β⟩ and not conjugation. But the failure is pure parameter ambiguity:
every such twist leaves the vector itself unchanged, so JBL (which is
about vectors/classes, not parameters) is unaffected once rigidity is
restated to allow trace-kernel twists. Repository untouched, no Lean.

## Setup

R = ℤ[√2], α = 3+2√2, Tr(x+y√2) = 2x, q₂ = 2^a, a = v₂(D_m)
(a = 2 if m odd, a ≥ 5 if m even). β = α^t, t = gcd(m,4).

## Lemma 1 — the trace kernel (proved)

κ = u+v√2 satisfies Tr(κz) ≡ Tr(z) (mod 2^a) for all z ∈ R iff
u ≡ 1 (mod 2^{a−1}) and v ≡ 0 (mod 2^{a−2}): 8 elements.
Proof: z = 1 gives 2u ≡ 2; z = √2 gives 4v ≡ 0; conversely
Tr(κz) = 2ux+4vy ≡ 2x (mod 2^a). Verified exhaustively mod 32
(kernel = {(1,0),(1,8),(1,16),(1,24),(17,0),(17,8),(17,16),(17,24)}).

Consequence: **no trace-only argument can ever exclude these twists.**
Wave 20 §4's hope ("excluded by the trace data") is impossible as
stated; exclusion must come from group theory or admissibility.

## Lemma 2 — ε is absorbed for even m (proved)

ε = 1+2^{a−1}√2 equals α^{2^{a−2}} mod 2^a (wave-11 L1 with
j = a−2 ≥ 3, since a ≥ 5 for even m; verified at a = 5,7,9).
Since t | 4 | 2^{a−2}, ε ∈ ⟨β⟩: an ε-twist is just a β-shift.
So for even m the ε-exclusion holds as absorption, not by traces.

## Counterexamples (exact arithmetic)

κ = 1+2^{a−1} is a norm-1 root of unity of order 2, trace-invisible,
and κ ∉ ⟨α⟩ for every a (kernel of ⟨α⟩ mod 2^a → mod 2^{a−1} is
{1, ε}; verified κ ∉ ⟨α⟩ at a = 5,7,9).

- m = 6 (D = 39200, t = 2): A = 35, A′ = 19635, with A′ ≡ κA (mod 32)
  and A′ ≡ A (mod 1225). Both give the vector
  [70,210,1190,6930,1190,210] mod 39200 — identical — but A′ is not
  D-related to A (full β-orbit of size 840 checked). Class-1
  parameters are likewise not D-related mod 32.
- m = 3 (D = 196, t = 1, the ε-case): A = 7, A′ = 7+98√2, with
  A′ ≡ εA (mod 4), A′ ≡ A (mod 49). Both give [14,42,42] mod 196,
  but A′ is not D-related to A (β-orbit of size 42 checked).

In both cases y′ = y mod D: the twist changes the parameter, never
the vector, hence never any per-class multiset.

## Corrected rigidity statement

B′ is D-related to B **up to a trace-kernel unit** (Lemma 1).
Since trace-kernel units act trivially on every trace, they act
trivially on the vector, so this corrected rigidity still implies
JBL. For odd m (t = 1) JBL is vacuous anyway; the ε-ambiguity there
is the same phenomenon at a = 2.

## What remains

The odd part of rigidity and the full rigidity lemma are untouched
by this task; only the 2-part step is now closed in corrected form.
Script: `wave22_JBL_2part_check.py` (checks above, in this directory).
