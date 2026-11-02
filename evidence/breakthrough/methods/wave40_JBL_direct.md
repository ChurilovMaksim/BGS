# Wave 40, task 5 — JBL by the direct route: π-compatibility + transport

## Verdict

The direct route is **proved in the P = t regime and reduced to one
named lemma elsewhere**. New conditional theorem: for v₂(m) ≤ 2,
**JBL ⟺ PC** (G3, marginal common π) — the m ≡ 4 (mod 8) case is
new; t = 1 is vacuous and t = 2 recovers wave 19 / wave 34 §4. For
m divisible by 8 the route needs exactly the Pairing Lemma below,
which is **not proved** but holds exhaustively at m = 8 (both odd
components) and m = 16, with zero crossed pairings in ~20M pairs.
No JBL counterexample found; first JBL evidence at m = 16.
Repository untouched; no Lean built.

## 1. Setup and the transport lemma (proved)

t = gcd(m,4), P = 2^{v₂(m)}, q₂ = 2^{v₂(D_m)}. For a pair (y, y′)
with the same exact multiset, Π_q ⊆ D_t is the marginal π-set at
each prime power q ‖ D_m; PC/G3 is ∩_q Π_q ≠ ∅. Per-class joints
J^{(q)}_r = {(p_{i mod P}, y_i mod q) : i ≡ r (mod t)}; JBL asks
for one π with J′^{(q)}_r = J^{(q)}_{π(r)} for all r and all odd q.

**Transport lemma.** Let π ∈ Π_{q₂} ∩ Π_q for the component pair
(q₂, q), induced by dihedral datum (j, c). Set
A′′ = c(A′)α^{−j} (mod q₂·q). Then A′′ is genuine (α^j commutes
with α^m − 1; conj sends the kernel to itself since
conj(α^m − 1) = −α^{−m}(α^m − 1)), the global multiset is
unchanged (α^j permutes positions, conj sends i ↦ −i), and
marginals/joints of A′′ are those of A′ permuted by π^{−1}.
Hence J′_r = J_{π(r)} ∀r ⟺ J′′_r = J_r ∀r: the direct route
reduces to class-by-class marginal agreement ⟹ class-by-class
joint agreement, after one global transport. The transport is
global — a single (j, c) for all q — which is exactly why a
COMMON π, not per-q π_q, is essential; per-q data alone cannot
be transported simultaneously (wave 29 §4's COH point, in
direct-route language).

## 2. Theorem: P = t ⟹ JBL ⟺ PC (proved)

Assume P = t, i.e. v₂(m) ≤ 2, and PC: one π ∈ Π_{q₂} ∩ ⋂_{odd q} Π_q.
Transport to π = id (§1). For i ≡ r (mod t) we have i mod P = r,
so the pattern part p_{i mod P} is the constant p_r within class r.
Marginal pattern agreement gives p′_r = p_r; marginal odd
agreement gives Q′_r = Q_r; hence
J′^{(q)}_r = {(p_r, y) : y ∈ Q_r} = J^{(q)}_r for every odd q.
The same π works for all q by PC, so JBL holds. Conversely JBL
⟹ PC by taking marginals of the joints. Cases: m odd (t = 1,
vacuous); m ≡ 2 (mod 4) (t = 2, the wave-19 reduction to PC /
G-2odd-1); **m ≡ 4 (mod 8) (t = 4, P = 4): new** — JBL there is
exactly PC, with no pairing input needed. PC itself remains open
in general (reduced to PAIR → Lemma U, waves 35–39), so this is
a conditional theorem, not a proof of JBL.

## 3. What remains for m divisible by 8: the Pairing Lemma

**Pairing Lemma (open).** If per-class marginals of genuine
parameters agree up to a common π, then per-class joints agree
up to the same π. It is false for abstract sequences (crossed
pairings exist: wave 12 §2, wave 20 §2), so any proof must use
Fix structure (recurrence + periodicity); in marginal form it
is the wave-20 rigidity lemma. The pairing test below groups by
marginals (a weaker hypothesis than JBL's global-multiset
hypothesis), so its 0 failures are evidence for step 2 proper,
not just for JBL.

## 4. Computational evidence (exact, scripts below)

Pairing test: group genuine parameters by per-class marginals up
to a common π; classify pairs as same-π (some marginal witness
is a joint witness), diff-π-only (joints agree only under a
different π), no-joint-π (no joint π at all).

| test | params | marg. groups | same-π | diff-π | no-joint |
| m=8, (512,9) | 4,608 | 57 | 226,560 | 0 | 0 |
| m=8, (512,289) | 147,968 | 685 | 17,243,392 | 0 | 0 |
| m=16, (2048,9) | 18,432 | 128 | 2,632,192 | 0 | 0 |

At m = 16, P/t = 4 (four pattern values per class), so the
pairing is genuinely nontrivial — yet no crossed pairing occurs.
JBL test (group by joint global multiset) at m = 16, (2048,9):
18,432 params, 128 global groups, **JBL-bad pairs = 0** — first
JBL evidence at m = 16 (prior: m = 8 exhaustive, m = 12 sampled).

## 5. What remains, precisely

1. Pairing Lemma in general (m divisible by 8) — the sole gap of
   the direct route beyond PC.
2. PC in general (PAIR → Lemma U; partial/conjugation/scaling
   mechanisms proved, "only three mechanisms" open).
3. Lean formalisation (nothing here is a Lean theorem).

## Files

- This note: `methods/wave40_JBL_direct.md`
- `methods/wave40_JBL_direct.py` (pairing tests m=8; JBL test m=16;
  m=16 pairing test run from the same definitions)
- Prior: `methods/wave34_class_partition.md` (existence ⟺ JBL,
  H_aff), `methods/wave29_JBL_global_step.md` (transport, COH),
  `methods/wave20_JBL.md`, `methods/wave12_g3_common_pi.md` (G3)
