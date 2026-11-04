# Prop. F’s shadowing mass sits outside the bad set

Status: **[P]**, as a disjointness statement. It uses the lower bound and the neighbourhood constructed in BGS-TRACE-329; it does not re-prove that lower bound. It does not upper-bound the bad sum.

## Statement

Fix g_0 = 4, the gap used by H1 and by Prop. K. Let U_n be the set in the proof of Prop. F (`evidence/executions/20261101/lineNgas/N20/REPORT_N20_v2.md`, §2): the image of

|a| ≤ (δ/2) ε^{−2n}, |b| ≤ δ/2, δ = 1.69×10^{-3},

under (a, b) ↦ (τ_0, τ_1) = (a + b, aε + bε′). On U_n the recurrence holds with no reduction for 0 ≤ k ≤ 2n, and |τ_k| ≤ δ.

Let U_n^† be the subset where |a| ≥ (δ/4) ε^{−2n} and |b| ≥ δ/4. For every n ≥ 3, every twist sequence in U_n^† has an internal ε-zero run of length at least 2n − 1 ≥ 5, so it is excluded from the bad set at g_0 = 4. The area of U_n^† is one quarter of the area of U_n, and the Prop. F pointwise bound |r_A|, |r_B| ≥ 0.502 still applies there. The integral of |r_A|^2 |r_B|^2 over U_n^† is therefore at least one quarter of the Prop. F lower bound.

## Proof

Leading and trailing zeros are trimmed before the internal-run statistic is computed, so a quiet segment that is only a prefix or a suffix does not by itself make the word bad. The subset U_n^† cuts out that null and near-null set.

On U_n, and hence on U_n^†, |τ_k| ≤ δ < 1/2 for 0 ≤ k ≤ 2n. Then red(τ_k) = τ_k, and the odd branch agrees because a half-integer has absolute value at least 1/2 (span proof, §2). The unreduced second difference vanishes, so E_k = 0 for 2 ≤ k ≤ 2n, and the carries n_k vanish on 0 ≤ k ≤ 2n.

On U_n^† the unstable coefficient is bounded below. For k ≥ 2n,

|b (ε′)^k| ≤ (δ/2) ε^{−k} ≤ (δ/2) ε^{−2n}, |a| ε^k ≥ (δ/4) ε^{k − 2n}.

The exit used below is k = 2n + 11. Since ε^2 = 3 + 2√2 > 5, one has ε^4 > 25, ε^8 > 625 and ε^{11} = ε^8 · ε^2 · ε > 625 · 5 · 2 = 6250. Also δ > 1.6×10^{-3}, so 4/δ < 2500 < 6250 and |a| ε^{2n+11} > 1. The conjugate term at that index is at most (δ/2) ε^{−(2n+11)} ≤ (δ/2) ε^{−13}. From ε^{11} > 6250 and ε^2 > 5 one has ε^{13} > 31250, so the conjugate term is < 10^{-4}. Thus |τ_{2n+11}| > 1/2. The first index k_+ with 2n < k_+ ≤ 2n+11 and |τ_{k_+}| ≥ 1/2 has vanishing previous carries, and E_{k_+} = n_{k_+} ≠ 0.

The same bound in the stable direction, at k = −11, gives |b| ε^{11} ≥ (δ/4) ε^{11} > 1 and a negligible unstable piece, so |τ_{−11}| > 1/2. The first index k_- ∈ [−11, −1] with |τ_{k_-}| ≥ 1/2 has E_{k_-} ≠ 0.

The letters E_k for 2 ≤ k ≤ 2n all vanish, a consecutive block of length 2n − 1. It sits strictly between k_- < 0 and k_+ > 2n, so the block is internal even if further nonzero letters occur outside [2, 2n]. For n ≥ 3 the block has length at least 5, which is already longer than g_0 − 1 = 3.

A bad word at g_0 = 4 has every internal zero-run strictly shorter than 4. Sequences in U_n^† are outside that set.

The (a, b)-rectangle of U_n has side lengths δ ε^{−2n} and δ. Cutting to the outer half of each side multiplies the area by 1/4. Prop. F’s lower bound |r_A| ≥ 0.502 uses only |τ| ≤ δ and the certified norm estimates on that neighbourhood, which still hold on the subset. The contribution of U_n^† is at least one quarter of 5.13×10^{-7} λ^{−n}.

## Integer check of the exit time

The only numerical input in the exit time is δ > 1.6×10^{-3} and ε^{11} > 6250. The second is elementary: ε^2 = 3+2√2 > 5 because 2√2 > 2, and ε^4 > 25, ε^8 > 625, ε^{10} > 3125, ε^{11} > 6250. And 4/1.6×10^{-3} = 2500 < 6250. The Prop. F value δ = 1.69×10^{-3} is larger than 1.6×10^{-3}, so the same k = 2n+11 works for it.

## What this does and does not decide

Prop. F remains a proof that no bound built from the unrestricted joint mean can produce the H1 rate. The mass that beats the i.i.d. product is the model channel, which is the channel the gas already extracts as (1+Λ)^p. H1-bad is a statement about the complementary words.

The lemma does not estimate those complementary words. A long zero-run is excluded; a word that returns close to 0 without staying there for g_0 letters is still bad, and nothing here bounds it.
