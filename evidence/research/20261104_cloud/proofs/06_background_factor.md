# The model-renormalised activity, as a factor

Status: the comparison is **[P]** inside the point-insertion model stated below. That model is the interval form of the cycle identity X = 2[(1+Λ)^p − 1], whose structure was checked numerically in N11 and is not a proved theorem. The numerical stability of the prime 3067 under a 0.1% enlargement of S_0 is **[P-arith]**.

## The factor

Let Re Λ_lo′ = 6.234×10^{-4} and δ_true ≤ 5.0313×10^{-6}. Write

c = log(1 + Re Λ_lo′) − δ_true.

Ball arithmetic at precision 200 gives c ∈ [6.18174466939×10^{-4} ± 7×10^{-17}].

**Theorem.** Assume that on every interval I the model partition function has the form

Z(I) = (1+Λ)^{|I|} exp(Δ |I|),

with one and the same Λ and Δ, Re Λ ≥ Re Λ_lo′, and |Δ| ≤ δ_true. Let a bad cluster γ exclude an interval of length ℓ = ℓ(γ) ≥ 1. Define

w̃(γ) = w(γ) · Z(complement) / Z(cycle).

Then

|w̃(γ)/w(γ)| ≤ exp(−c ℓ) ≤ exp(−c) < 1.

In particular, for every bad cluster at g_0 = 4 one has ℓ = span + g_0 ≥ 4, so

|w̃/w| ≤ exp(−4c) < 0.997531.

Every Kotecký–Preiss sum built from the bare moduli |w| is therefore an upper bound for the same sum built from |w̃|.

## Proof

On a cycle of length p the complement of an excluded interval of length ℓ is an interval of length p − ℓ, under the point-insertion model (a bump has no width, so the complement is a pure interval and the same formula applies). Hence

Z(complement)/Z(cycle) = (1+Λ)^{−ℓ} exp(−Δ ℓ).

The modulus satisfies |1+Λ| ≥ 1 + Re Λ ≥ 1 + Re Λ_lo′, because Re Λ > 0, and |exp(−Δ ℓ)| ≤ exp(δ_true ℓ). Therefore

|ratio| ≤ (1 + Re Λ_lo′)^{−ℓ} exp(δ_true ℓ) = exp(−c ℓ).

Since c > 0 and ℓ ≥ 1, the factor is strictly smaller than 1. The numerical bound exp(−4c) < 0.997531 is the same ball arithmetic: the ball for exp(−4c) is 0.9975303567 ± 4×10^{-21}.

## Consequence for 3067

The sharp-span tail of `04_propK_sharp.md` was computed with the bare moduli. Under the theorem, the renormalised activity S_0(w̃) is at most the bare S_0, up to the factor exp(−4c) < 1 on every term with ℓ ≥ 4. The idealised δ_eff = 3.2909×10^{-4} remains an upper bound for the charge that uses w̃. The crossover prime 3067 computed from that δ_eff remains a sufficient threshold: a smaller charge still beats Robin’s bound wherever the larger charge does.

A boundary correction that multiplies every activity by 1.001, larger than any relative error of size 4×10^{-4} coming from one cut bump of the family weight, was fed to the same crossover script. The first prime stays **3067**. At a factor 1.002 the first prime moves to 3079. The threshold is stable at the 0.1% level and not at the 0.2% level.

## Where the hypothesis sits

The identity Z = (1+Λ)^{length} on a cycle is the N11 closed form. The referee of N11 confirmed its structure on sampled configurations and marked that confirmation [N]. The step from the cycle to every interval is automatic for point insertions and is not automatic for bumps of width span ≤ 3. A bump that straddles the cut changes the count by one polymer. That is the 0.1% margin checked above, not a second proof of the cycle identity.

If the model weight on a proper subinterval is not given by the same Λ, the factor can exceed 1 and 3067 can move. The sensitivity already computed for the sharp tail says how far: +1% in S_0 moves the prime to 3109, +3% to 3181. Nothing in this note removes that dependence for a model other than the one stated.
