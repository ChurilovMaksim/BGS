# Wave 34, task 1 — the class-partition lemma for JBL's direct route

## Verdict (read carefully: two readings, opposite outcomes)

Let t = gcd(m,4), O_r = {i : i ≡ r (mod t)}, y_i = Tr(Aα^i) mod D_m,
and let σ be a permutation of Z/m with y'_i = y_{σ(i)} (mod D_m) for
all i (a "matching" for the joint global multiset, which by CRT is
exactly the sorted multiset of the y_i mod D_m).

- **Literal reading ("every matching σ preserves classes") is FALSE**,
  trivially: y = y' = 0 is in Fix_m (0 is in the kernel; A = 0 is
  genuine by the divisibility conventions), and every σ matches it,
  including a transposition swapping a class-0 position with a
  class-1 position. More generally, any value repeated across two
  classes lets one swap σ on its preimages and still match. This
  refutes nothing about JBL: it is an artefact of non-uniqueness of σ.
- **Existence reading ("some matching σ preserves classes") is exactly
  JBL, hence open in general for t = 4.** It is proved below for
  t = 1, 2 (modulo PC in one subcase) and for t = 4 under either of
  two narrow hypotheses, one of which is exactly the m = 60 mechanism.
  No unconditional t = 4 proof is claimed here: one would close JBL.
  Repository untouched; no Lean built.

## 1. Existence reading ⟺ JBL (both directions, short)

(⇒) If σ(O_r) = O_{π(r)} for π ∈ D_t, then as i runs over O_r,
σ(i) runs over O_{π(r)}, and y'_i mod q₂q = y_{σ(i)} mod q₂q, so the
per-class joint multisets satisfy J′^{(q)}_r = J^{(q)}_{π(r)} for
every odd q — JBL's conclusion for this pair.
(⇐) If JBL holds with π, then for fixed r the equalities
J′^{(q)}_r = J^{(q)}_{π(r)} for all odd q give, by CRT across the
coprime moduli q₂·q (product D_m), equality of the multisets
{y'_i mod D_m : i ∈ O_r} and {y_j mod D_m : j ∈ O_{π(r)}}; hence a
bijection σ_r : O_r → O_{π(r)} with y'_i = y_{σ_r(i)} mod D_m
exists, and σ = ⊔_r σ_r preserves classes. So the lemma (existence
reading) and JBL stand or fall together, pair by pair.

## 2. Hypothesis H_aff: σ affine — proved, covers m = 60

Assume the matching σ is affine: σ(i) = ui + c (mod m) with
gcd(u, m) = 1. Then σ preserves classes up to D_t, with no other
input (no G1/G2 needed). Proof: t | m, so reduction mod t is
well-defined, and σ(i) ≡ ur + c (mod t) for i ∈ O_r; σ bijective
gives σ(O_r) = O_{ur+c}. It remains that r ↦ ur + c lies in D_t:
if t = 1 this is vacuous; if t = 2, u is odd (gcd(u,m) = 1, m even),
so u ≡ 1 ≡ −1 (mod 2); if t = 4, then 4 | m, so u is odd, hence
u ≡ ±1 (mod 4). By §1, J′^{(q)}_r = J^{(q)}_{ur+c} for all q.
At m = 60, σ(i) = 11i + 9 has u ≡ −1, c ≡ 1 (mod 4), i.e.
π(r) = −r + 1 — exactly wave 33's π. So the m = 60 pair is not an
accident: every affine matching is class-preserving, and COH's
failure there is purely position-level (no dihedral τ on the
60-window matches σ), while the class-level statement holds.

## 3. Hypothesis H_pat: distinct pattern values — proved (modulo G2)

Assume (i) G2: a per-component π₂ ∈ D_t exists for q₂ (proved as a
sketch in waves 10–13, not re-proved here), and (ii) the pattern
values p_s = y_s mod q₂ are pairwise distinct on Z/P, P = 2^{v₂(m)}
(note t | P always). Then σ(O_r) = O_{π₂(r)}, hence JBL holds for
the pair by §1. Proof: M′_r (mod q₂) equals both the multiset of
p_{σ(i)} over i ∈ O_r (by y'_i = y_{σ(i)}) and M_{π₂(r)} (by G2).
Distinctness turns multiset equality into residue equality: for
each s mod P, the count of i ∈ O_r with σ(i) ≡ s (mod P) equals
the count for O_{π₂(r)}, namely m/P if s ≡ π₂(r) (mod t) and 0
otherwise. Hence every σ(i), i ∈ O_r, lies in O_{π₂(r)}; sizes
|σ(O_r)| = |O_{π₂(r)}| = m/t give equality. This is wave 19's
sufficient condition, made exact; it fails in general because
patterns repeat values (wave 19), which is precisely why t = 4
needs JBL rather than counting.

## 4. t = 2: proved except the a = b subcase (wave 19 argument)

Let m ≡ 2 (mod 4). Then q₂ = 32 and every Fix vector mod 32 is
2-periodic (kernel mod 32 checked: all 32 rows 2-periodic, also
at m = 10, 14): y_i ≡ a (i even), b (i odd). If a ≠ b (mod 32),
the mod-32 multisets {a×u, b×u} = {a′×u, b′×u} (u = m/2) force
(a′, b′) = (a, b) or (b, a); since a ≠ b, the count of σ(E) ∩ E
vs σ(E) ∩ O (E = even positions) is forced, so σ(E) = E or O,
and the matching π (id or swap) lies in Π_q for every q at once.
If a = b (mod 32), then Π₂ = D₂ is full and the lemma reduces to
odd-odd compatibility (PC for m ≡ 2 mod 4), gap G-2odd-1, open in
general. t = 1 (m odd) is vacuous: one class, π = id.

## 5. Computational evidence (existence reading, exact)

New exhaustive joint checks (script `wave34_class_partition_check.py`,
CRT enumeration as in wave 20; joint, not just marginal, π-sets):
m = 4 (t = 4): 949 fiber pairs, 0 joint-π failures; m = 6 (t = 2):
35,596 fiber pairs, 0 failures. Prior: m = 8 exhaustive joint
(wave 20): 1,246,606 pairs, 0 failures; m = 12 sampled joint:
7,905 pairs, 0 failures; m = 60 pair (wave 33): π = −r + 1 works
at every odd q. No counterexample to the existence reading was
found anywhere; the only refutation in this note is the literal
reading (§0), which is trivial and irrelevant to JBL.

## 6. What remains, precisely

1. General t = 4 without H_aff or H_pat: exactly JBL (open). A
   proof of the class-partition lemma in full generality would
   close JBL; it is not claimed here.
2. t = 2, a = b subcase: PC (G-2odd-1), open in general.
3. Lean formalisation (nothing here is a Lean theorem).

## Files

- This note: `methods/wave34_class_partition.md`
- `methods/wave34_class_partition_check.py` (m = 4, 6 exhaustive joint)
- Prior: `methods/wave33_JBL_m60_verdict.md`,
  `methods/wave20_JBL.md`, `methods/wave19_compat_2odd.md`
