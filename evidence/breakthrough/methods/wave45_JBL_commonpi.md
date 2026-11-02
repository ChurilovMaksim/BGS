# Wave 45, task 1 — multi-component common-π step for the JBL direct route

## Verdict

**No counterexample found — and the step is PROVED for both GPL
families at (8192,17) extended by 577, plus proved under one narrow
hypothesis in general.** The full-system global hypothesis forces
the same π in every case tested: the 577-component inherits the
pair-level π through a conjugation identity, it never chooses a
different one. Repository untouched; no Lean built.

## 1. Setup and lifting

m = 32, t = 4, pattern component q₂ = 8192, odd components 17 and
577 (α^32 ≡ 1 mod both, α^16 ≡ 1 mod 577R, α^8 ≡ −1 mod 577R).
A pair (A, A′) at (8192,17) with equal pair-globals is extended by
577-parameters (C, C′). All other odd components of D₃₂ are set to
0 for both parameters: then triple equality implies full global
equality (the same witness permutation works, 0 is preserved), and
joints at zero components impose no constraint beyond the pattern
marginals, which agree under the pair-level π by projection
(wave 44 §4). So a triple counterexample would be a full
counterexample — and none exists in the families below.

## 2. Narrow theorem (proved): trivial pattern stabilizer ⟹ common π

Assume PC transport has been applied, so marginals agree under id
at every odd q. By the projection lemma (wave 44 §4), joint
π-set(q) ⊆ marginal π-set(q). If the pattern marginal signature
has trivial stabilizer in D_t, then any π ∈ marginal π-set(q)
must fix the pattern class multisets (they are equal for A, A′
post-transport), hence π = id. So joint π-set(q) = {id} for every
q (nonempty by pair-JBL), and common π = id. This is generic:
it holds whenever the four pattern class multisets are pairwise
distinct. The hard case is exactly nontrivial pattern stabilizer
— the GPL ambiguity of wave 44 — handled for (8192,17) in §3–§4.

## 3. Reversal family: inheritance proved

Witness (wave 44): B₂ = (128,64) fixed, B_q = (8,8) vs (9,9) = −B_q
mod 17; joint π-set at 17 is exactly {(3,2,1,0)} (reversal).
Fibers of the pair sequence are {i, i+16} (A) and {15−i, 31−i}
(A′), i.e. ρ(i) = (15−i) mod 32 is a pair-witness permutation
with class map reversal. For a 577-extension, fiber-multiset
matching forces fiber-sum matching; with α^16 = 1 mod 577R the
sums are Tr(2C·α^i) and Tr(2C′·α^{15−i}), and
α^{15−i} = α^15·conj(α^i) (N(α) = 1) gives, by nondegeneracy of
the trace pairing, C = α·conj(C′) — the whole extension family
is the graph of this invertible map (2-dimensional, verified
exactly: all 577² (s,t) satisfy the power-sum conditions, and
direct triple sorting passes on samples). Conversely,
C = α·conj(C′) implies b′_{ρ(i)} = b_i for all i, since
conj(α^15) = α^{−15} = α mod 577R: indeed
b′_{ρ(i)} = Tr(C′α^{15−i}) = Tr(conj(C′α^15)α^i)
= Tr(α·conj(C′)α^i) = b_i. Hence triples match, and joints at
577 match under reversal pointwise (p_{ρ(i)} = p_i from the
witness property). So joint π-set(577) ∋ reversal always;
common π = reversal. Survey: 3000 random survivors, 2995 with
π-set(577) = {reversal}, 5 with {id, reversal}.

## 4. Swap family: inheritance proved

Swap witness (found by sampling, seed 42): B_q = (13,2) fixed,
B₂ = (2944,1856) vs (6016,832); joint π-set at 17 is exactly
{(1,0,3,2)} (adjacent swap). Fibers are again 16 pairs of size 2;
the class-map-respecting witness ρ′ is the block reversal
ρ′(j) = ((9−j) mod 16) + 16⌊j/16⌋. The extension graph is
C = mult((−3,2))·conj(C′), and the pointwise identity
b_{ρ′(j)} = b′_j holds because (−3,−2)·α^7 = (1,0) mod 577R
(using α^{ρ′(j)} = α^9·conj(α^j), since α^16 = 1). Hence joints
at 577 match under swap. Survey: 300 random survivors, all with
π-set(577) = {swap}. Same conclusion: common π = swap.

## 5. What this does and does not settle

Settled: for the two GPL mechanisms at (8192,17) — odd negation
with fixed pattern, pattern move with fixed odd parameter — the
577-component cannot break the common π; the full global
hypothesis propagates π through the ρ-conjugation identity.
Not settled in general: pairs whose fibers are not {i, i+16}
pairs, components with α^16 ≢ 1 mod qR, and the question
whether every pair-level π admits a ρ for which the
corresponding conjugation identity holds at q. Precise
reduction: the multi-component step holds iff, for every
pair-level π realized by a position permutation ρ preserving
pair values, triple matching at q implies joint matching under
π at q. The two families above are the cases
ρ(i) = c−i and block-reversal ρ′ with α^16 = 1 mod qR.

## Files

- This note: `methods/wave45_JBL_commonpi.md`
- `methods/wave45_commonpi_reversal.py` (ALL CHECKS PASS)
- `methods/wave45_commonpi_swap.py` (ALL CHECKS PASS)
- Prior: `methods/wave44_JBL_pairing_replacement.md`,
  `methods/wave40_JBL_direct.md` (transport, projection lemma)
