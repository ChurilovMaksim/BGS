# Wave 11, task 3 — LTE input: v₂(D_m) depends only on v₂(m)

## Statement

Let H_m = 6I − C − Cᵀ (cyclic, size m), D_m = det H_m.
Let α = 3 + 2√2, β = 3 − 2√2 (so αβ = 1, α + β = 6),
s_m = α^m + β^m ∈ ℤ, and D_m = s_m − 2.

**Theorem.** For m ≥ 1,

```
v₂(D_m) = 2            if v₂(m) = 0 (m odd),
v₂(D_m) = 2·v₂(m) + 3  if v₂(m) ≥ 1.
```

In particular v₂(D_m) depends only on v₂(m). Values: m odd → 2;
v₂(m)=1 → 5; v₂(m)=2 → 7; v₂(m)=3 → 9; etc.

## The ring and the valuation

Work in R = ℤ[√2], which is Euclidean for |N| (hence a UFD),
with norm N(a + b√2) = a² − 2b².

- √2 is prime in R: if √2 = xy with x, y non-units, then
  N(x)N(y) = N(√2) = −2, forcing one of N(x), N(y) to be ±1,
  i.e. one factor a unit — contradiction. So √2 is irreducible,
  hence prime (UFD). The ideal 𝔭 = (√2) is maximal, with
  R/𝔭 ≅ 𝔽₂ via a + b√2 ↦ a mod 2.
- Let v_𝔭(x) be the exponent of √2 in the factorisation of x
  (x ≠ 0). This is a valuation: v_𝔭(xy) = v_𝔭(x) + v_𝔭(y), and
  v_𝔭(x + y) ≥ min(v_𝔭(x), v_𝔭(y)), with equality if the two
  valuations differ (non-archimedean property).
- Norm–valuation link: for x ≠ 0, v₂(N(x)) = v_𝔭(x).
  Proof: write x = √2^t · u with 𝔭 ∤ u. Then
  N(x) = N(√2)^t · N(u) = (−2)^t · N(u). Moreover 𝔭 ∤ u means
  the constant term a of u = a + b√2 is odd, so
  N(u) = a² − 2b² is odd. Hence v₂(N(x)) = t = v_𝔭(x).
- Consequences used below: v_𝔭(2) = 2 (since 2 = −√2²·(−1),
  or directly 2 = √2² up to unit −1); an element is a 𝔭-unit
  (v_𝔭 = 0) iff its constant term is odd iff its norm is odd.

## Reduction of D_m to α^m − 1

Since β = α⁻¹,

```
D_m = α^m + β^m − 2 = α^(−m)·(α^m − 1)².
```

Hence, with N(α^m − 1) = (α^m − 1)(β^m − 1)
= 1 − (α^m + β^m) + 1 = 2 − s_m = −D_m,

```
v₂(D_m) = v₂(N(α^m − 1)) = v_𝔭(α^m − 1).
```

So it suffices to compute v_𝔭(α^m − 1).

## Base valuations

- α − 1 = 2 + 2√2 = 2(1 + √2). Now 1 + √2 is a unit
  (N(1 + √2) = −1), so v_𝔭(1 + √2) = 0, and
  **v_𝔭(α − 1) = v_𝔭(2) = 2.**
- α + 1 = 4 + 2√2 = 2(2 + √2) = 2·√2·(1 + √2)
  (since √2(1 + √2) = 2 + √2). Hence
  **v_𝔭(α + 1) = 2 + 1 + 0 = 3.**
- Also α ≡ 1 (mod 𝔭), because α − 1 is divisible by 𝔭
  (indeed v_𝔭(α − 1) = 2 ≥ 1). Consequently α^j ≡ 1 (mod 𝔭)
  for all j, and in the residue field 𝔽₂ we have −1 = 1.
- α² ≡ 1 (mod 4): α² = 17 + 12√2, and 17 ≡ 1 (mod 4),
  12√2 ≡ 0 (mod 4) in R. Hence for any even exponent 2e,
  α^{2e} = (α²)^e ≡ 1 (mod 4), so α^{2e} + 1 ≡ 2 (mod 4),
  and therefore v_𝔭(α^{2e} + 1) = 2: indeed if x = 2 + 4k
  in R, then v_𝔭(2) = 2 < 4 ≤ v_𝔭(4k), so the non-archimedean
  property gives v_𝔭(x) = min = 2.

## Odd m

If m is odd,

```
α^m − 1 = (α − 1)·(α^{m−1} + α^{m−2} + ··· + 1).
```

The second factor is a sum of m terms, each ≡ 1 (mod 𝔭)
(since α^j ≡ 1 mod 𝔭), so it is ≡ m ≡ 1 (mod 𝔭)
(m odd, residue field 𝔽₂), hence a 𝔭-unit: its valuation is 0.
Therefore

```
v_𝔭(α^m − 1) = v_𝔭(α − 1) = 2    (m odd).
```

## Even m

Write m = 2^k · t with t odd, k = v₂(m) ≥ 1. Factor:

```
α^m − 1 = (α^t − 1) · ∏_{j=0}^{k−1} (α^{2^j·t} + 1).
```

- v_𝔭(α^t − 1) = 2 by the odd case.
- j = 0 factor: α^t + 1 = (α + 1)·S where
  S = α^{t−1} − α^{t−2} + ··· − α + 1 (t terms, t odd).
  Mod 𝔭, each α^j ≡ 1 and −1 = 1 (characteristic 2), so
  S ≡ t ≡ 1 (mod 𝔭): S is a 𝔭-unit. Hence
  v_𝔭(α^t + 1) = v_𝔭(α + 1) = 3.
- j ≥ 1 factors: 2^j·t is even, so by the mod-4 step above,
  v_𝔭(α^{2^j·t} + 1) = 2 for each j = 1, …, k−1
  (there are k−1 such factors).

Adding (valuation of a product is the sum of valuations):

```
v_𝔭(α^m − 1) = 2 + 3 + 2(k − 1) = 2k + 3    (k ≥ 1).
```

## Conclusion

v_𝔭(α^m − 1) = 2 if v₂(m) = 0, and 2·v₂(m) + 3 if v₂(m) ≥ 1.
By the norm–valuation link, v₂(D_m) is the same number.
∎

## Numerical check (Pell recurrence)

s₀ = 2, s₁ = 6, s_{n+1} = 6·s_n − s_{n−1} (roots α, β of
X² − 6X + 1); D_m = s_m − 2. Checked for m = 1..30 against
the formula above (script: `wave11_task3_LTE_check.py` in this
directory). Spot values: m=2: D=32=2⁵·1; m=3: D=196=2²·49;
m=4: D=1152=2⁷·9; m=6: D=39200=2⁵·1225;
m=8: D=1331712=2⁹·2601; m=10: D=45239072, v₂=5.
All m = 1..30 agree with the formula.

## Where it is used

v₂(D_m) = a is the exponent in the 2-component of the Lemma Y
argument: Fix_m mod 2^a is P-periodic with P = 2^{v₂(m)}, and
m/P is odd (a unit mod 2^a). The LTE formula is what makes a
depend only on v₂(m) — in particular, for the P-periodicity
mechanism, a = 2·v₂(m) + 3 (m even) is determined by v₂(m) alone,
not by the odd part of m. The formula is an ordinary mathematical
proof (not a Lean formalisation); the Lean version would need
the ℤ[√2] valuation infrastructure above, which is not in the
drafts.
