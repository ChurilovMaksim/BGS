# Wave 20, task 2 — JBL: the joint lemma (numerically established, proof open)

## Verdict (honest)

JBL is **not proved**, but it is upgraded from a vague "joint blocks" gap to
a precise statement with exhaustive numerical backing at m=8 and sampled
backing at m=12, plus a named remaining rigidity lemma. No counterexample
was found anywhere. Repository untouched; no Lean built.

## 1. JBL restated as the Joint Lemma

Let t = gcd(m,4), P = 2^{v₂(m)}, a = v₂(D_m), q₂ = 2^a. For y, y′ ∈ Fix_m
with the same sorted exact multiset, and each odd prime power q ‖ D_m:

**Joint Lemma.** There is a single π ∈ D_t such that for every class r,
the per-class multiset mod q₂·q of y′ at class r equals that of y at
class π(r). Equivalently, with pattern values p_i = y_i mod q₂ (P-periodic)
and joint pairs (p_{i mod P}, y_i mod q), the per-class joint multisets
J^{(q)}_r = {(p_{i mod P}, y_i mod q) : i ≡ r (mod t)} satisfy
J′^{(q)}_r = J^{(q)}_{π(r)} for all r and all odd q, with one π for all q.

Since gcd(q₂, q) = 1, a joint pair is exactly a residue mod q₂·q (CRT), so
the Joint Lemma is the per-class lemma at the composite modulus q₂·q.
It implies marginal compatibility immediately (take marginals mod q₂ and
mod q), so proving it closes JBL and hence 2-vs-odd compatibility.

## 2. Why componentwise methods cannot give it (the pairing problem)

The component lemmas (pattern lemma for q₂, G1 for odd q) see only
marginals: M′^{(q₂)}_r = M^{(q₂)}_{π₂(r)} and M′^{(q)}_r = M^{(q)}_{π_q(r)}.
They say nothing about the pairing inside class r between the mod-q₂ part
and the mod-q part of each value y′_i. A crossed pairing (mod-q₂ part from
class π₂(r), mod-q part from class π_q(r) ≠ π₂(r)) is consistent with
both marginals. The Joint Lemma asserts crossed pairings never occur for
genuine Fix vectors. Its proof must therefore use the joint position data,
not the components separately.

## 3. Numerical evidence

**m=8, exhaustive** (script `wave20_JBL_joint_m8.py`, full Fix₈, 1,331,712
points, 85,106 fibers): 1,246,606 fiber pairs; marginal compatibility
1,246,606; joint π exists 1,246,606; joint π outside the marginal common
set 0; marginal-but-no-joint 0. Note m=8 is the clean case: P=8=m, so the
joint claim is that the pairs {y_r, y_{r+4}} mod 512q are D₄-permuted.

**m=12, sampled** (script `wave20_JBL_joint_m12.py`, 1,000,000 random CRT
points, 992,095 fibers hit, 15,775 repeat samples): 7,905 fiber pairs;
marginal compatibility 7,905; joint π exists 7,905; marginal failures 0;
joint failures 0. (Multiplicity-biased sample, as in wave 12; a falsifier
needs only one pair, none appeared.)

## 4. Proof strategy and the exact remaining lemma

Write class r values as y_{r+t·s} = Tr(B_r β^s), B_r = Aα^r, β = α^t.
Both the pattern class-r data and the odd class-r data are functions of
the single parameter B_r (pattern: {Tr(B_r β^{s′}) mod q₂},
s′ ∈ ℤ/(P/t); odd: {Tr(B_r β^s) mod q}, s ∈ ℤ/(m/t)), and the joint
multiset for class r is the s-pairing of the two. The global multiset
equality constrains A′ vs A; a Lucas-type argument in R/(q₂·p^f) (odd part
reduced by the wave-12 scaling, where α^m ≡ 1) would give B′_r up to
⟨β⟩-action and conjugation — except for extra 2-part roots of unity mod
q₂ (e.g. 1 + 2^{a−1}√2 of order 2), which the trace/multiset data must
rule out, in the same style as the wave-12 L6/L7 and wave-18/19
second-digit rigidity analyses.

**Remaining lemma (rigidity).** If pair(B′) = pair(B) (pattern-data and
odd-data jointly, as multisets over s), then B′ is D-related to B in the
effective sense (⟨β⟩-action or conjugation), with the 2-part roots of
unity excluded by the trace data. This single lemma, plus the already
proved component lemmas, would prove the Joint Lemma. It is not proved
here; the p-part obstruction is that ord(γ), γ = α^P, can be divisible
by p when p | u = m/P (e.g. m=12, q=81), so the column/β-group argument
needs the full G1 machinery, not just the coprime-to-p Lucas step.

## 5. What this changes

2-vs-odd compatibility is no longer "open modulo JBL (vague)": it is open
modulo exactly the rigidity lemma of §4, and the joint statement it
implies is verified exhaustively at m=8 and on 7,905 sampled pairs at
m=12. Together with wave-19 (t=2 proved except a=b mod 32; t=4 reduced to
JBL), the exact per-class lemma's remaining gaps are now: G1 (f≥3,
f=2 s=0 hole), general PC, joint CRT pairing inside classes (the same
pairing problem at the level of exact multisets, of which JBL is the
mod-(q₂·q) shadow), and Lean formalisation.

## Files

- This note: `methods/wave20_JBL.md`
- m=8 exhaustive joint test: `methods/wave20_JBL_joint_m8.py`
- m=12 sampled joint test: `methods/wave20_JBL_joint_m12.py`
- Prior: `methods/wave19_compat_2odd.md`, `methods/wave19_compat_2odd.py`
