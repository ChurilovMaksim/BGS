# Lemma S, the polymer gap lemma and the Binet lattice generator (BGS-TRACE-352..355)

*5 November 2026. Source: the research pass `research1105b` (`REPORT.md` §4, with code and logs) and its independent
internal referee audit `REFEREE.md` (items 1–4, with `referee/`), both copied unchanged to
[`evidence/research/20261105_lemma_s/`](../../../evidence/research/20261105_lemma_s/NOTE.md). Only the results the referee
**confirmed** are registered, in the referee's corrected form. Registry ids BGS-TRACE-352..355 (next free after
BGS-TRACE-351 on origin/main `6f69baa1`; open PR branches #83, #84, #85 register nothing above BGS-TRACE-336).*

**Tags.** [P] paper proof · [CA] exact or exhaustive computation · [N] floating-point numerics · [H] heuristic ·
[C] conjecture. Nothing tagged [N], [H] or [C] in the source is registered.

## 0. Convention and setting

ε = 1 + √2, ε̄ = 1 − √2 = −ε⁻¹, λ = ε², O = Z[√2] (class number 1), h_p = (ε^p + ε̄^p)/2 for an odd prime p
(the convention of BGS-TRACE-342/348; h_11 = 23·353, h_13 = 79·599, h_17 = 103·15607). Every prime factor q of h_p splits
in O (q ≡ ±1 mod 8, BGS-TRACE-348).

**Lines.** A *line* is an ideal 𝔞̄ ⊂ O with O/𝔞̄ ≅ Z/h_p on which λ^p ≡ 1 (grok47 `h5_xline`). Then ε^p ≡ σ_𝔮 ∈ {±1}
modulo each prime 𝔮 | 𝔞̄. Put 𝔞̄_± = ∏_{σ_𝔮 = ±1} 𝔮 and d_± = N𝔞̄_±. A line is *Binet* if min(d₊, d₋) = 1 and *cross*
otherwise. **If h_p is squarefree** (H6, BGS-TRACE-304, open) the lines are the 2^ω ideals of norm h_p with one prime above
each q | h_p, exactly one of 𝔮, 𝔮̄ divides ε^p − 1 (the other divides ε^p + 1), and **d₊d₋ = h_p**. Without H6 the last
identity, and with it max(d₊, d₋) ≥ √h_p, is not available.

**Height.** For a class x ∈ O/𝔞̄, G(x) = min{max(|ρ|, |ρ′|) : ρ ≡ x mod 𝔞̄} = min{|a| + √2|b| : a + b√2 ≡ x}
(max(|a + b√2|, |a − b√2|) = |a| + √2|b|, Lean `ht_eq_max`); the minimum exists because a coset of a lattice is discrete.

## 1. BGS-TRACE-352 — Lemma S on cross lines [P] (referee item 1, corrected scope)

**Statement.** Let 𝔞̄ = 𝔞̄₊𝔞̄₋ with coprime ideals of odd norms d₊, d₋ > 1, ε^p ≡ +1 mod 𝔞̄₊, ε^p ≡ −1 mod 𝔞̄₋, and let σ
be the side with d_σ = max(d₊, d₋). For every n ∈ Z and every class c ∉ 𝔞̄_{−σ} (not only primitive c):

    G(cεⁿ) + G(cε^{n+p}) ≥ √d_σ = √max(d₊, d₋).

More generally (G(cεⁿ) + G(cε^{n+p}))² ≥ d₊·N(gcd(c, 𝔞̄₋)) whenever c ∉ 𝔞̄₋, and symmetrically with + and − exchanged.

*Proof (referee re-derivation).* Take minimal representatives ρ₁ ≡ cεⁿ, ρ₂ ≡ cε^{n+p}. At 𝔮 | 𝔞̄₊, ρ₂ ≡ ρ₁; at 𝔮 | 𝔞̄₋,
ρ₂ ≡ −ρ₁. Hence 𝔞̄₊ | ρ₂ − ρ₁ and 𝔞̄₋ | ρ₂ + ρ₁. Also ρ₂ − ρ₁ ≡ −2cεⁿ mod 𝔞̄₋, which is nonzero when c ∉ 𝔞̄₋ (2 and ε are
units at odd primes), so ρ₂ − ρ₁ ≠ 0 and 𝔞̄₊·gcd(c, 𝔞̄₋) | ρ₂ − ρ₁. Therefore
d₊·N(gcd(c, 𝔞̄₋)) ≤ |N(ρ₂ − ρ₁)| = |ρ₂ − ρ₁|·|ρ₂′ − ρ₁′| ≤ (G₁ + G₂)². Symmetrically for ρ₂ + ρ₁ and d₋. ∎

**Scope caveat (axis sub-line).** The classes 0 ≠ c ∈ 𝔞̄_{−σ} form a sub-line of level d_σ on which ε^p acts by the single
sign σ (a Binet-type sub-line). There G(cε^{n+p}) = G(cεⁿ), and the only bound is **G ≥ √min(d₊, d₋)** (a nonzero element
of 𝔞̄_{−σ} has |N| ≥ d_{−σ}). So the source report's "no hypothesis on P⁻(h_p) is needed for the vacuum part" holds only for
the classes outside 𝔞̄_{−σ}; on the axis sub-line the smallest-prime ceiling returns through √min(d₊, d₋).

**Corollary, conditional on H6.** If h_p is squarefree then d₊d₋ = h_p, so max(d₊, d₋) ≥ √h_p and
G(cεⁿ) + G(cε^{n+p}) ≥ h_p^{1/4} off the axis sub-line. This uses squarefreeness of h_p and is **conditional on H6**
(BGS-TRACE-304, open).

**Checks [CA]** (`code/lemmaS_exact.py`, exhaustive over all h classes of every line; heights evaluated in float64, every
inequality with margin ≥ 3%; `logs/lemmaS_exact.json`):

| p | h | lines | d_σ | Q = min_prim max(G₁,G₂) | Q/√d_σ | min_prim (G₁+G₂)/√d_σ | min over c ∉ 𝔞̄_{−σ} | axis min G | √min |
|---|---|---|---|---|---|---|---|---|---|
| 11 | 23·353 | 4 (2 cross) | 353 | 15.2426 (= 11 + 3√2) | 0.81128 | 1.16181 | 1.16181 | 6.4142 | 4.7958 |
| 13 | 79·599 | 4 (2 cross) | 599 | 21.7990 | 0.89068 | 1.32611 | 1.32611 | 10.4142 | 8.8882 |
| 17 | 103·15607 | 4 (2 cross) | 15607 | 68 | 0.54431 | 1.03454 | 1.03454 | 15.2426 | 10.1489 |

The general form (with gcd) holds on every class; on the axis sub-line G(x) = G(xε^p) and G² ≥ min(d₊, d₋); on Binet
lines Q = 1 (x = 1). All three h_p are semiprimes (ω = 2). The first ω = 3 case, p = 37 (h = 223·37223·8761009 ≈ 7.27e13,
8 lines), is out of exhaustive reach; `code/lemmaS_exact_p37.py` samples 1000 outside-axis and 500 axis classes on every
cross line with exact integer (A+B√2)² ≥ D tests (Lagrange CVP height, 25% margin when not fully b-certified; six fully
b-certified samples on the tightest line with min ratio 7.65), all pass (`logs/lemmaS_exact_p37.json`). These numbers for
p = 11, 13, 17 agree with the referee's `lemmaS_exact_11_13_17.json` to every printed digit.

**Lean (partial)** (`formalization/Bgs/LemmaSArith.lean`): `ht_eq_max`, `norm_le_ht` (|N(a + b√2)| ≤ (|a| + √2|b|)²),
`ht_sub_le`, `ht_add_le`, `lemmaS_core_sub`, `lemmaS_core_add` (d | N(ρ₂ ∓ ρ₁) ≠ 0 ⟹ d ≤ (G(ρ₁) + G(ρ₂))²), `axis_bound`
(G² ≥ d for a nonzero element with d | N) and `mul_le_max_sq` (d₊d₋ ≤ max(d₊, d₋)²). The ideal-theoretic steps
(𝔞̄₊ | ρ₂ − ρ₁, nonvanishing mod 𝔞̄₋, the gcd factor) are not formalized.

**Not claimed.** No bound on X_line or X_cross. Corollary S′ (window lengths, [P-sketch]), the multi-window case [C], the
seam-cost input and the estimate with r < 0.418 are not registered. grok47's "< 3e-7" difference for axis classes is [N].

## 2. BGS-TRACE-353 — Polymer gap lemma, explicit constant [P] (referee item 2)

**Setting.** Z[ζ] = Z[ω] with ω = ζ^{(p+1)/2} (ω² = ζ). On a line, ζ ↦ λ and ω ↦ λ^{(p+1)/2} = ε·ε^p ≡ σ_𝔮 ε at each
𝔮 | 𝔞̄, and η₊η₋ = (ω² − 2ω − 1)(ω² + 2ω − 1) = ω⁴ − 6ω² + 1 = ζ² − 6ζ + 1. For f = F(ω), F ∈ Z[x], f in the line lattice
means F(ε) ∈ 𝔞̄₊ and F(−ε) ∈ 𝔞̄₋.

**Statement.** Let F = Σ_{k≤K} a_k x^k ∈ Z[x] with |a_k| ≤ A and f = F(ω) in the lattice of a cross line. If f ∉ (η₊η₋),
then

    K > log_ε min(d₊, d₋) − 2 log_ε A − log_ε(ε²/2),   log_ε(ε²/2) = 2 − log_ε 2 = 1.21356… < 1.214,

so in particular K > log_ε min(d₊, d₋) − 2 log_ε A − 1.214.

*Proof.* If F(ε) = F(−ε) = 0, the monic factors x² − 2x − 1 and x² + 2x − 1 divide F in Z[x] (Gauss), so f ∈ (η₊η₋).
Otherwise F(ε) ≠ 0, giving d₊ ≤ |N F(ε)|, or F(−ε) ≠ 0, giving d₋ ≤ |N F(−ε)|. With |F(±ε)| ≤ A·Σ_{k≤K} ε^k
< Aε^{K+1}/√2 and |F(±ε̄)| ≤ A·Σ_{k≤K} |ε̄|^k < A/(2 − √2), and 1/(√2(2 − √2)) = ε/2,
|N F(±ε)| < A²ε^{K+2}/2. Hence min(d₊, d₋) < A²ε^{K+2}/2; take log_ε. ∎

**Caveats (referee, wording).** (i) The statement is about the chosen integer polynomial F; representatives differ by
multiples of Φ_p(x), and F(ε) depends on the choice once K ≥ p − 1, but "f ∉ (η₊η₋) ⟹ F(ε) ≠ 0 or F(−ε) ≠ 0" holds for
every representative. (ii) (η₊η₋) contains short vectors: ζ² − 6ζ + 1 (ℓ1 = 8) lies in every line lattice, cross lines
included. (iii) Only min(d₊, d₋) enters; for the 2p+1 family (BGS-TRACE-350) the bound is about log_ε(2p + 1), nearly
vacuous. (iv) |X_cross| ≲ poly(p)·min(d₊, d₋)^{−γ} is [H] and not registered. "−O(log A)" in the source reads
"−2 log_ε A − O(1)"; the additive constant is present even at A = 1.

**Checks [CA]** (`code/polymer_const.py`, `logs/polymer_const.json`): log_ε(ε²/2) = 1.2135602986… (60 digits); exhaustive
over all nonzero coefficient vectors with (A, K) ∈ {(1, ≤ 9), (2, ≤ 5), (3, ≤ 3)}, both signs, exact integer norms:
|N F(σε)| < A²ε^{K+2}/2 always; the largest ratio rises to 0.976 at A = 1, K = 9 (the constant is nearly sharp).

**Lean (partial)**: `polymer_norm_lt` (|F(σε)|·|F(σε̄)| < A²ε^{K+2}/2 for σ = ±1, A > 0, |a_k| ≤ A, every K),
`polymer_gap`, `polymer_gap_of_norm` (the logarithmic form) and `logb_const_lt`, `logb_const_gt`
(1.213 < log_ε(ε²/2) < 1.214, via ε^{103} < 2^{131} and 2^{75} < ε^{59}, `decide +kernel` on h_103, h_59). The
divisibility step (Gauss, f ∉ (η₊η₋) ⟹ F(ε) ≠ 0 or F(−ε) ≠ 0) and the ideal membership are not formalized.

## 3. BGS-TRACE-354 — Binet lattice generator [P] (referee item 4)

**Statement.** Let p be an odd prime, s = ±1, ω = ζ_p^{(p+1)/2} and η_s = ω² − 2sω − 1 = ζ − 1 − 2sζ^{(p+1)/2}. Then
N_{Q(ζ_p)/Q}(η_s) = **+h_p** and N(ζ² − 6ζ + 1) = h_p². On the Binet line 𝔞̄ = (Φ_p(sε)) (where ε^p ≡ s), the lattice
𝔄_s = ker(Z[ζ_p] → O/𝔞̄ ≅ Z/h_p, ζ ↦ λ) equals the principal ideal (η_s). In the word model Z[x]/(x^p − 1) the line
lattice is (η_s) + (Φ_p(x)) (Φ_p(x) the all-ones word), and (η_s) alone has index |η_s(1)|·h_p = 2h_p there, so
"𝔄 = (η_s)" is exact only modulo the all-ones direction.

*Proof.* ω is again a primitive p-th root, and the roots of x² − 2sx − 1 are sε, sε̄. So
N(η_s) = ∏_ω (ω − sε)(ω − sε̄) = Φ_p(sε)Φ_p(sε̄) = N_{Q(√2)/Q}(Φ_p(sε)) = h_p, since
(ε^p − 1)(ε̄^p − 1) = −2h_p, (ε − 1)(ε̄ − 1) = −2 and (−ε^p − 1)(−ε̄^p − 1) = 2h_p, (ε + 1)(ε̄ + 1) = 2. On the Binet
line ω ↦ ε^{p+1} ≡ sε, so η_s ↦ ε² − 2ε − 1 = 0, i.e. (η_s) ⊆ 𝔄_s. No rational prime q divides (Φ_p(sε)) (it would force
ε^p ≡ ε̄^p ≡ s mod q, while ε^pε̄^p = −1), so O/𝔞̄ ≅ Z/h_p, the map is onto and [Z[ζ] : 𝔄_s] = h_p = [Z[ζ] : (η_s)];
hence 𝔄_s = (η_s). N(ζ² − 6ζ + 1) = Φ_p(λ)Φ_p(λ̄) = h_p². In Z[x]/(x^p − 1),
|Res(x^p − 1, η_s)| = |η_s(1)|·|Res(Φ_p, η_s)| = 2h_p. ∎ The squarefreeness of h_p is not used.

**Checks [CA]** (`code/eta_check.py`, `logs/eta_check.json`): exact resultants N(η₊) = N(η₋) = h_p and
N(ζ² − 6ζ + 1) = h_p² for all 20 primes 3 ≤ p ≤ 73; Φ_p(sε)Φ_p(sε̄) = h_p in exact Z[√2] arithmetic for every odd prime
p ≤ 1500; on every line for p ≤ 43 (up to 8 lines, ω ≤ 3): η_s ↦ 0 exactly on the Binet line of sign s, neither η_s
vanishes on cross lines, ζ² − 6ζ + 1 ↦ 0 on every line; |Res(x^p − 1, η_s)| = 2h_p for every prime 5 ≤ p ≤ 43.

**Lean (partial)**: `h_closed` (h_n = (ε^n + ε̄^n)/2), `phi_eps`, `phi_neg_eps` (Φ_n(±ε)Φ_n(±ε̄) = h_n for every odd n),
`phi_lambda` (Φ_n(λ)Φ_n(λ̄) = h_n²), `prod_eta` (∏ over all primitive p-th roots μ ∈ ℂ of (μ² − 2sμ − 1) = h_p, every odd
prime p, s = ±1) and `prod_kernel` (∏_μ (μ² − 6μ + 1) = h_p²). Not formalized: the identification of these products with
Algebra.norm of Q(ζ_p)/Q, the kernel/index argument (𝔄_s = (η_s)) and the index 2h_p in Z[x]/(x^p − 1).

## 4. BGS-TRACE-355 — H5(b) cross-line sufficiency, conditional; constant [CA] (referee item 3, corrected)

The source's "c > 0.048" is **wrong** (it used w_max(3307) = 228 instead of 231, ignored the room and skipped the binding
prime 1409). Corrected statement (referee):

- A uniform bound |X_line| ≤ C e^{−cp} on **all** cross lines discharges the cross-line part (b) of H5 (BGS-TRACE-303) at
  the prime p if (2^{ω(h_p)} − 2)·C·e^{−cp} < slack(p) − |Y| − |X_tail| (the idealised slack already subtracts e^{−0.28p}).
- Unconditionally in ω (Lemma W, BGS-TRACE-342: ω ≤ w_max(p)), it suffices that c > [ln(2^{w_max(p)} − 2) + ln C +
  ln(1/room)]/p.
- With the idealised V5/TRACE-333 room recomputed in `h5b_const.py` from main (R = 6.234e-4, n/h_p := 1,
  Y = X_tail = ε_* = 0; slack = M − √(1+robin) − e^{−0.28p}; delta(1409) = 7.4115e-6, delta(3307) = 3.4962e-4;
  slack(1409) = 0.0201129656, slack(3307) = 0.0033471848) and C = 1: c > 0.05787 at p = 1409 and
  c > 0.05014 at p = 3307. A safe single value is **c ≥ 0.058 for C ≤ 1**. Larger C costs ln C/p.

**Checks [CA]** (`code/h5b_const.py`, `logs/h5b_const.json`): w_max(1409) = 112 and w_max(3307) = 231 by exact integer
comparison of (p − 1)^w w! with ε^p = a_p + b_p√2; thresholds as above; with c = 0.058, C = 1:
(2^{112} − 2)e^{−0.058·1409} = 0.01675 < 0.02011 and (2^{231} − 2)e^{−0.058·3307} = 1.7·10⁻¹⁴ < 0.00335 (so at p = 1409
any C ≤ 1.20 also fits). Under the crude line count 2^{p/ln(p−1)} the thresholds are 0.0984 (1409) and 0.0873 (3307).

**Inputs and status.** The room values are **recomputed** from THEOREM_DRAFT_v5 / BGS-TRACE-333 on main (same
formula and deltas as above); they match the previously cited grok47 Prop. 4 digits, which are no longer used as a
source. The hypothesis (a uniform e^{−cp} bound on every cross line) is **open** and is **not** supplied by §§1–2: lines
with small min(d₊, d₋) (min(d₊, d₋) = 2p + 1 occurs, e.g. p = 11, 23; BGS-TRACE-350) and the axis sub-line are controlled
only through min(d₊, d₋). With nonzero additive budgets |Y|, |X_tail| the threshold rises by
ln(slack/(slack − |Y| − |X_tail|))/p. Not formalized in Lean. H5 (BGS-TRACE-303) stays open; Theorem R♯-mod v5
(BGS-TRACE-325) stays conditional.

## 5. Scope and non-claims

- Registered: the four statements above, in the referee's corrected form. Not registered: the r < 0.418 seam-decay
  threshold, the seam-cost/counting inputs, the "estimate U", Corollary S′, the [N] decompositions of §3 of the source
  report (Dev/main = 0.03389 ± O(1e−5) over ii + ui + iu, uu excluded) and every [H]/[C] item.
- H5 (BGS-TRACE-303) stays **open**, H6 (BGS-TRACE-304) stays **open**, Theorem R♯-mod v5 (BGS-TRACE-325) stays
  **conditional**, frozen R′ (BGS-TRACE-206) is untouched. No existing claim is edited.

## 6. Reproduction

    export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
    python computations/verification/lemma_s/code/lemmaS_exact.py    # TRACE-352, ~3 min -> logs/lemmaS_exact.json
    python computations/verification/lemma_s/code/polymer_const.py   # TRACE-353          -> logs/polymer_const.json
    python computations/verification/lemma_s/code/eta_check.py       # TRACE-354          -> logs/eta_check.json
    python computations/verification/lemma_s/code/h5b_const.py       # TRACE-355          -> logs/h5b_const.json
    (cd formalization && lake build Bgs.LemmaSArith)

Run with Python 3.13.5, numpy 2.5.4, sympy 1.14.0, mpmath 1.3.0 (venv `/workspace/venv7`), 1 thread. Each script asserts
its checks and exits nonzero on failure.
