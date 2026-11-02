# Wave 44, task 1 — replacement for the Pairing Lemma: proved at the
# JBL grade, refuted at the class-by-class grade

## Verdict

The naive class-by-class replacement is **false**, but the replacement
JBL actually needs is **true exhaustively at the first dangerous
pair**. The failure mechanism is exactly the marginal stabilizer,
which is harmless for JBL because every joint π is automatically a
marginal π. Repository untouched; no Lean built.

## 1. Two grades of the statement

After the wave-40 transport (π = id), with A, A′ genuine for (q₂, q):

- **GPL (class-by-class):** equal globals + equal per-class marginals
  ⟹ equal per-class joints. **FALSE** (§2).
- **JBL-grade pairing:** equal globals ⟹ per-class joints agree under
  some π ∈ D_t. **TRUE exhaustively at (8192, 17)** (§3).

The distinction matters: GPL demands π = id after transport, while
JBL only needs some π — and §2's counterexamples all have their
joints agreeing under a π that stabilizes the marginals.

## 2. GPL refuted: exact mechanism

Exhaustive census at m = 32, (8192, 17): 2,367,488 pairs, 46,000
(global, marginals) groups, **20,480 GPL-bad pairs** (vs
first-in-group). Classification is perfectly clean:

- Every bad pair's joints are related by a **unique** joint π:
  reversal (3, 2, 1, 0) in 10,240 cases, adjacent swap (1, 0, 3, 2)
  in 10,240 cases — no other type occurs.
- In **all 20,480** cases, every relating π **stabilizes the
  marginal signature** (marginals permuted by π equal marginals).

So the failure is exactly marginal-symmetry ambiguity: when the
marginal signature has a nontrivial stabilizer, the joints can be
π-permuted without changing globals or marginals. It is not a
crossing of the wave-43 kind (there the joint π-set was empty).

Minimal witness (independently verified, `wave44_GPL_witness.py`):
B₂ = (128, 64) mod 8192 fixed, B_q = (8, 8) vs (9, 9) = −B_q mod 17.
Globals equal, class-by-class marginals equal, joints differ by
reversal (3, 2, 1, 0) only; e.g. class 0: A has (256, 16)×2,
(2304, 1)×2, (4352, 16)×2, (6400, 1)×2, while A′ swaps 16 ↔ 1.
The odd negation preserves odd marginals (values come in ± pairs)
but re-pairs them against a swap-symmetric pattern side.

## 3. JBL-grade pairing holds at (8192, 17)

Same census, grouped by global multiset only: **6,159 global
groups, 0 JBL-bad pairs** — every two parameters sharing a global
multiset have per-class joints agreeing under some π ∈ D₄. This
is the first JBL check at m = 32 for a dangerous pair (both
periods even), and it passes exactly where the standalone
Pairing Lemma failed.

## 4. Why the JBL grade is the right replacement (proved lemma)

**Lemma (projection).** Joint π-set ⊆ marginal π-set, always:
if joints agree under π, taking pattern/odd marginals of the
joints gives marginal agreement under the same π. Hence
"joints agree under some π" ⟺ "marginal π-set ∩ joint π-set ≠ ∅".
The direct route needs exactly this intersection to be nonempty
(after transport by PC's common π, the remaining freedom is the
marginal stabilizer — and §2 shows that freedom is real but
confined to the stabilizer, never a genuine crossing).

## 5. What remains open

- The JBL-grade statement at other dangerous pairs, e.g.
  (8192, 577): exhaustive census infeasible (8192 × 332,929
  pairs); the stabilizer mechanism is general, but no proof yet.
- The multi-component common-π step: pair-level JBL gives, per
  odd q, some π_q ∈ Stab(marginals_q); full JBL needs one π for
  all q. PC supplies a common marginal π, and transport by it
  leaves per-q stabilizer freedom; whether the full-system
  global hypothesis (stronger than pair-global) forces a common
  π is open. This is now the precise remaining gap of the direct
  route, replacing the refuted Pairing Lemma.
- PC in general; Lean formalisation (nothing here is a Lean
  theorem).

## Files

- This note: `methods/wave44_JBL_pairing_replacement.md`
- `methods/wave44_GPL_test.py` (exhaustive census, 49 s)
- `methods/wave44_GPL_recount.py` (classification of all bad pairs)
- `methods/wave44_GPL_witness.py` (independent witness check)
- Prior: `methods/wave43_PairingLemma.md` (+ check), §5's
  cross-class-compensation remark is now realized concretely as
  marginal-stabilizer ambiguity.
