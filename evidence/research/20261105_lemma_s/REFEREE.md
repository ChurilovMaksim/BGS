# REFEREE — research1105b/REPORT.md (independent, hostile)

Grok Bot (acting as referee), 2026-11-05 (CET). Target: `REPORT.md` with its `code/` and `logs/`, BGS main @ 6f69baa1.
For the grok47 rooms and Lemma W I read `research-grok46-1104` @ f7986a9f (`proofs/h5_factor.md`, `proofs/h5_xline.md`).
I ran `git fetch` of that branch into the local `repo/` clone (read-only, adds objects only). **Nothing pushed.**
All of my code and logs are in `referee/`. I used `/workspace/lineNgas/venv/bin/python`.

| item | verdict | one line |
|---|---|---|
| (1) Lemma S | **CONFIRMED** (one scope gap in how it is *used*) | I re-derived the proof and found no gap. My exhaustive exact recomputation matches 0.8113 / 0.8907 / 0.5443. |
| (2) Polymer gap lemma | **CONFIRMED**, constant made explicit | K ≥ log_ε min(d₊,d₋) − 2 log_ε A − log_ε(ε²/2). The statement is about the integer polynomial F. |
| (3) H5(b) sufficiency, c > 0.048 | **WRONG** (constant); the qualitative implication is fine | With the room included, C = 1 and Lemma W's w_max, you need c > 0.0501 at p = 3307 and c > 0.0579 at p = 1409. Under the crude bound 2^{p/ln(p−1)} you need c > 0.087 / 0.098. |
| (4) Binet generator η_s | **CONFIRMED** in Z[ζ_p]; precision gap for the word lattice | Proof below. N(η_s) = +h_p exactly for 3 ≤ p ≤ 73, and the kernel holds on every line for p ≤ 43. In Z[x]/(x^p−1) the lattice is (η_s) + (Φ_p), and the index of (η_s) alone is 2h. |
| (5) [N] spot checks | **CONFIRMED** (numbers), with wording corrections | 0.0338759, 0.348 / 0.621, and max\|u\| 2.24e-7 / 1.93e-6 vs 3.96e-4 all reproduce. "Exact" leaves out the uu class. |

---

## Setup facts I re-derived (used throughout)

- h_p = (ε^p + ε̄^p)/2 = Q_p/2. For odd p, |N(ε^p − 1)| = |N(ε^p + 1)| = Q_p, N(√2) = −2 and N(2+√2) = 2. So
  h_p = N(Φ_p(ε)) = N(Φ_p(−ε)).
- **No inert prime divides h_p.** Suppose q is inert and q | ε^p − 1. Then q | ε̄^p − 1 = −ε^{−p} − 1, so ε^p ≡ −1 and 2 ≡ 0. That is impossible.
- **For a split prime q | h_p, exactly one of 𝔮, 𝔮̄ divides ε^p − 1 and the other divides ε^p + 1.** If both divided ε^p − 1, then ε̄^p ≡ 1 mod q, but ε̄^p = −ε^{−p} ≡ −1.
  - So lines correspond to subsets of the primes: 2^ω lines, of which 2 are Binet and 2^ω − 2 are cross.
  - d₊d₋ = N𝔞̄ = h_p **exactly**. Hence **max(d₊,d₋) ≥ √h_p for every factorisation.** This is trivial, but it needs h_p squarefree (H6). With q² | h_p, an ideal of norm h_p can contain (q) = 𝔮𝔮̄, and then "ε^p ≡ ±1 mod 𝔞̄ per prime" breaks down.

## (1) Lemma S — CONFIRMED

**Re-derivation.**
- G(x) = min over ρ ∈ x + 𝔞̄ of max(|ρ|,|ρ′|) = min |a| + √2|b| over a + b√2 ≡ x. The minimum is attained because a lattice coset is discrete.
- Take minimal representatives ρ₁ ≡ cεⁿ and ρ₂ ≡ cε^{n+p}.
- At 𝔮 | 𝔞̄₊ we have ρ₂ ≡ ρ₁; at 𝔮 | 𝔞̄₋ we have ρ₂ ≡ −ρ₁. Hence 𝔞̄₊ | ρ₂ − ρ₁ and 𝔞̄₋ | ρ₂ + ρ₁.
- ρ₂ − ρ₁ ≡ −2cεⁿ mod 𝔞̄₋. This is nonzero as soon as c ∉ 𝔞̄₋, because 2 and ε are units at odd primes.
- So d₊ ≤ |N(ρ₂ − ρ₁)| = |ρ₂ − ρ₁|·|ρ₂′ − ρ₁′| ≤ (G₁ + G₂)², and symmetrically for d₋.

Every step holds. The definition of G, the use of representatives in O mod 𝔞̄ ≅ Z/h, and the ± bookkeeping are all correct.

**Sharper and correct form.**
- Let σ be the side with d_σ = max(d₊,d₋). Then (G₁ + G₂)² ≥ d_σ for **every c ∉ 𝔞̄_{−σ}**, not only for primitive c.
- More generally, (G₁ + G₂)² ≥ d₊·N(gcd(c, 𝔞̄₋)) whenever c ∉ 𝔞̄₋.

**Scope gap (in §0.4 / §5, not in the lemma).**
- The exceptional classes 0 ≠ c ∈ 𝔞̄_{−σ} form a sub-line of level d_σ on which ε^p acts as the single sign σ. That is a Binet-type sub-line.
- On it G(n) = G(n+p), and the only bound is G ≥ √min(d₊,d₋), from the norm of a nonzero element of 𝔞̄_{−σ}.
- Exact minima of G over these classes are 6.414 (p=11; √23 = 4.80), 10.41 (p=13; √79 = 8.89) and 15.24 (p=17; √103 = 10.15) (`referee/lemmaS_exact_11_13_17.json`, `min_sum_nonprim_nonzero`/2).
- So the claim "no hypothesis on P⁻(h_p) is needed for the vacuum part" holds only for the classes outside 𝔞̄_{−σ}. On the axis sub-line the smallest-prime ceiling comes back through √min.
- The report calls these "level-d₊ objects" but proves nothing about them. grok47's < 3e-7 is [N].

**Exhaustive check, my own code** (`referee/lemmaS_exact.py`):
- G is computed exactly as min_b (√2|b| + ‖x − b r‖_h) over all classes x ∈ Z/h.
- The search stops only when √2·b exceeds max G. That guarantees exactness, unlike the original Babai + R=3 window, which can only overestimate G.
- Q = min over primitive x of max(G(x), G(x·ε^p)).

| p | h | lines | D (cross) | Q | Q/√D | min (G₁+G₂)/√D | lemma holds on all primitive x |
|---|---|---|---|---|---|---|---|
| 11 | 23·353 | 4 | 353 | 15.2426 (= 11+3√2) | 0.81128 | 1.1618 | yes |
| 13 | 79·599 | 4 | 599 | 21.7990 | 0.89068 | 1.3261 | yes |
| 17 | 103·15607 | 4 | 15607 | 68 | 0.54431 | **1.0345** | yes |

- On Binet lines Q = 1 (c = 1). This matches the report to every printed digit.
- At p = 17 the sum form is within 3.5% of equality, so the report's "nearly sharp" is right.
- Caveat: all three tested h_p are semiprimes (ω = 2). The first ω = 3 case, p = 37, has h ≈ 7e13, which is beyond exhaustive reach. The proof does not depend on ω.

## (2) Polymer gap lemma — CONFIRMED (explicit constant)

**Setting.**
- Work in Z[ζ] = Z[ω] with ω = ζ^{(p+1)/2} (ω² = ζ). Then η₊η₋ = ω⁴ − 6ω² + 1 = ζ² − 6ζ + 1.
- On the line, ω ↦ λ^{(p+1)/2} = ε·ε^p ≡ σ_𝔮 ε at each 𝔮 | 𝔞̄.
- So f = F(ω) ∈ 𝔄_c means F(ε) ∈ 𝔞̄₊ and F(−ε) ∈ 𝔞̄₋.

**The divisibility step.**
- If F(ε) = F(−ε) = 0, then (x² − 2x − 1)(x² + 2x − 1) | F in Z[x] (monic factors, Gauss), so f ∈ (η₊η₋).
- So if f ∉ (η₊η₋), then F(ε) ≠ 0, giving d₊ ≤ |N F(ε)|, or F(−ε) ≠ 0, giving d₋ ≤ |N F(−ε)|.

**The constant.**
- With F = Σ_{k≤K} a_k x^k and |a_k| ≤ A:
  |F(±ε)|·|F(±ε̄)| < A²·(ε^{K+1}/√2)·(1/(2−√2)) = **A² ε^{K+2}/2**, since 1/(2√2 − 2) = ε/2.
- Hence
  **K > log_ε min(d₊,d₋) − 2 log_ε A − log_ε(ε²/2) = log_ε min(d₊,d₋) − 2 log_ε A − 1.214.**
- In the report's notation C² = ε²/2 ≈ 2.914. "−O(log A)" should read "−2 log_ε A − O(1)", because the additive constant is there even at A = 1.

**Caveats (wording, not errors).**
- (i) The lemma is about the chosen integer polynomial F, not the element. Representatives differ by Φ_p(x)-multiples, and F(ε) depends on that choice once K ≥ p − 1. The direction "f ∉ (η₊η₋) ⇒ F(ε) ≠ 0 or F(−ε) ≠ 0" holds for every representative, so the conclusion stands.
- (ii) The excluded set (η₊η₋) is not empty of short vectors. ζ² − 6ζ + 1 (ℓ1 = 8, three consecutive λ-sites) lies in **every** line lattice, cross lines included.
- (iii) The lemma bounds only min(d₊,d₋). For the 2p+1 family the bound is about log_ε(2p+1), i.e. nearly vacuous. The report says this.
- (iv) "|X_cross| ≲ poly(p)·min^{−γ}" is [H], as labelled.

## (3) H5(b) exponential sufficiency — WRONG constant

**Inputs.**
- Rooms (grok47 `h5_factor.md` Prop. 4): slack < 0.00334719 at p = 3307 (fragile δ) and < 0.02011297 at p = 1409 (robust δ). These are the two binding thresholds.
- Lemma W cap: w_max(p) = max{w : (p−1)^w w! ≤ ε^p}. I recomputed **w_max(1409) = 112 and w_max(3307) = 231**. The report's "≈ 228" is wrong.
- Requirement: (2^ω − 2)·C·e^{−cp} < slack(p), i.e. **c > [ln(2^{w} − 2) + ln C + ln(1/slack)]/p**.

My numbers (C = 1; `referee/h5b_const.py`, `.json`):

| p | cap on ω | c needed, no room | c needed, with room |
|---|---|---|---|
| 3307 | w_max = 231 | 0.04842 | **0.05014** |
| 3307 | report's 228 | 0.04779 (the report's 0.048) | 0.04951 |
| 3307 | c♯ = 359 | 0.07525 | 0.07697 |
| 3307 | p/ln(p−1) = 408.1 | 0.08554 | **0.08726** |
| 1409 | w_max = 112 | 0.05510 | **0.05787** |
| 1409 | c♯ = 171 | 0.08412 | 0.08689 |
| 1409 | p/ln(p−1) = 194.3 | 0.09561 | **0.09838** |

**Answers.**
- c > 0.048 is not enough at either threshold, even with Lemma W's sharp cap. It falls short by 0.0021 at p = 3307 and by 0.0099 at p = 1409, which is the binding prime.
- If the number of lines is allowed to be 2^{p/ln(p−1)} (the user's bound, Theorem 1 of h5_factor), it is far short: you need c > 0.087 (3307) or c > 0.098 (1409).
- Ignoring the room, c = 0.048 with the w_max cap first works at p = 3539 (w_max = 245). With the crude cap it first works at p − 1 > e^{ln2/0.048} ≈ 1.87·10⁶.
- **The qualitative part is right.** w_max(p)/p ≤ 1/ln(p−1) → 0, and the slack eventually grows like 2e^{ρp}. So any fixed c > 0 with fixed C closes H5(b) for p ≥ p₀(c, C).

**Corrected statement.**
- A uniform bound |X_line| ≤ C e^{−cp} on all cross lines discharges H5(b) at the prime p if (2^{ω(h_p)} − 2)·C·e^{−cp} < slack(p) − |Y| − |X_tail| − e^{−0.28p}.
- Unconditionally in ω (Lemma W), it suffices that c > [w_max(p) ln 2 + ln C + ln(1/slack(p))]/p.
- At the conditional primes, with C = 1: c > 0.0501 (p = 3307) and c > 0.0579 (p = 1409). Equivalently, a safe single value is **c ≥ 0.058 for C ≤ 1**. Larger C costs ln C/p more.

**Additional gap: the hypothesis is not what §4–§5 deliver.**
- The bridged part is at best poly(p)·min(d₊,d₋)^{−γ}. Lemma W allows min(d₊,d₋) = 2p ± 1 (it happens at p = 11 and p = 23).
- The axis sub-line of item (1) only has height ≥ √min.
- So no *uniform* e^{−cp} on cross lines follows, even conditionally on the seam-cost input. §4.4 is a valid implication whose premise the report's own mechanism does not supply for small-min lines. Those lines need grok47's γ*-sum route, as §5.3 itself says.

## (4) Binet generator — CONFIRMED (Z[ζ_p]); precision gap for words

**Proof.**
- η_s = ω² − 2sω − 1 with ω = ζ^{(p+1)/2}, which is again a primitive p-th root. Its roots in ω are sε and sε̄. So
  N(η_s) = ∏_ω (ω − sε)(ω − sε̄) = Φ_p(sε)Φ_p(sε̄) = N_{Q(√2)}(Φ_p(sε)) = Q_p/2 = h_p. The value is **+h_p**, not only in absolute value.
- On the Binet line where ε^p ≡ s (that ideal is 𝔞̄ = (Φ_p(sε))), the map ζ ↦ λ sends ω ↦ ε^{p+1} ≡ sε. So η_s ↦ ε² − 2ε − 1 = 0.
- The map Z[ζ] → O/𝔞̄ ≅ Z/h is onto (Z already hits Z/h), so the kernel 𝔄_s has index h. Since (η_s) ⊆ 𝔄_s with the same index h, they are equal. ∎
- N(ζ² − 6ζ + 1) = N(Φ_p(λ)) = N(ε^{2p} − 1)/N(ε² − 1) = (−Q_p²)/(−4) = h_p².
- The map ζ ↦ λ is the one in grok47 Theorem 6: ξ_n = Σ n_i λ^i ∈ 𝔞̄.

**Check** (`referee/eta_check.py`, sympy resultants, independent of flint):
- N(η₊) = N(η₋) = h_p and N(η₊η₋) = h_p² for all 20 primes 3 ≤ p ≤ 73.
- For p ≤ 43, on every line:
  - on a Binet line with sign s, η_s ↦ 0 and η_{−s} ↦ 0 fails, as it should;
  - on cross lines neither η_s vanishes, but ζ² − 6ζ + 1 does.

**Precision gap.**
- W(𝔄̄) in Theorem 6 sums over words n ∈ Z^m. Folded mod p, these live in Z[x]/(x^p − 1), not in Z[ζ].
- There the lattice is the preimage (η_s) + Z·Φ_p(x), with Φ_p(x) the all-ones word in each period.
- (η_s) alone has index |Res(x^p − 1, η_s)| = |η_s(1)|·h = **2h** (checked for p = 5…23).
- "𝔄 = (η_s)" is therefore exact only modulo the all-ones direction. Also, "3-site" means 3 ε-sites (ω⁰, ω¹, ω²). In λ-sites these are 0, 1 and (p+1)/2, which is not λ-local.

## (5) Numerical spot checks — CONFIRMED, with corrections

**What I recomputed** (`referee/spot5.py`, `zcheck.py`, `uu_est.py`):

| quantity | report | referee | note |
|---|---|---|---|
| Dev/main, p=11, ρ=(2,8) (ii+ui+iu) | 0.0338759 | 0.033875898 | direct sums over 7371 members, my own E(t̄) (no FFT) |
| ⟨E⟩ (same) | 0.0164166+0.0081227i | same | |
| Var | 7.07e-4 | 7.0727e-4 | |
| Dev/main, ρ=(−2,8) (ii+ui) | 0.033298 | 0.0332977 | |
| ⟨E⟩, ρ=(−2,8) | 0.016481 − 0.008186i | **0.016478** − 0.008186i | typo, 3e-6 |
| Dev/(φm), level h_p, p=11 | ≈ 0.069 | **0.0700** (log 0.06998) | rounding |
| \|X\|/ℓ1 cross, p=11 / 13 | 0.348 / 0.621 | 0.34838 / 0.62064 | my own line membership via √2 ↦ r, and the sign (1+r)^p mod q |
| \|X\|/ℓ1 Binet | 0.972 | 0.97171 / 0.97182 | |
| max\|u\| cross, p=11 / 13 | ≤ 2e-6 | 2.244e-7 / 1.927e-6 | the same with axis classes removed |
| max\|u\| Binet, p=11 / 13 | 3.96e-4 | 3.956e-4 / 3.955e-4 | |

**Other checks.**
- I recomputed Ẑ for the six largest stored ii points directly from the transfer law. The stored values match to 6e-15 relative.
- The same holds for λβ, −β and β̄, which confirms the orbit/conjugation invariance that `linesplit.py` uses.
- §5.3's per-site ratios (0.106 / 0.230 per λ-site) follow from these maxima.

**Corrections.**
- **"Exact" is overstated.** 0.0338759 leaves out the uu class (59,969,536 β, sampled with 4000 points) from both ⟨E⟩ and Var.
  - The sampled uu mean shifts |1+⟨E⟩|² − 1 by +1.5e-5.
  - The uu variance cannot be bounded from the sample. Split-half estimates give 0.04–0.05, which is pure sampling noise.
  - An incoherent-phase estimate gives ≈ (D/n)·Σ|u|² ≈ 1.7e-6 [H].
  - Honest statement: Dev/main = 0.03389 ± O(1e-5) [N+H], "exact over ii, ui, iu". §0 should not say "fully exact enumeration at p = 11".
- `logs/seam_profile_p1{1,3}.json` lists depend on which orbit representatives were kept. It tests only the representatives lying on 𝔞, not on 𝔞̄. So the Binet line (−1,−1) at p=11 shows top |u| 2.3e-7, while its conjugate shows 3.96e-4, and the two cross lines differ by 2.6×.
  - The report's maxima are right only for the union over both members of each conjugate pair. The per-line rows of that log should not be quoted.

## Summary for the parent

- Lemma S and the polymer gap lemma are correct proofs. Lemma S's numbers reproduce exactly.
- The η_s generator is proved, with N = +h_p.
- The H5(b) constant 0.048 is wrong:
  - it uses w_max = 228 instead of 231;
  - it ignores the room (≈ +0.0017 at 3307);
  - it skips the binding robust prime 1409, which needs 0.0579.
  The correct safe threshold is c ≥ 0.058 (C ≤ 1). Under the crude 2^{p/ln p} line count it is c ≥ 0.099.
- The p=11 numbers reproduce. "Exact" must say that uu is excluded.
- Two substantive scope gaps:
  - Lemma S's exceptional axis sub-line (c ∈ 𝔞̄_{−σ}) and the bridged polymers are controlled only by min(d₊,d₋). So the smallest-prime ceiling is not removed from the vacuum side as §0.4 claims.
  - No uniform e^{−cp} cross-line bound follows from §4 for lines with small min(d₊,d₋).
