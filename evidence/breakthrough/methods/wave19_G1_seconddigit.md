# Wave 19, task 3 — second-digit twist invariant at p=31: YES, it distinguishes

**Verdict: YES.** At p=31, as at p=13, every genuine twist changes the
second-digit distribution — marginal, hence joint. No genuine twist is
invisible to it. The general lemma is formulated below (empirical at
p=13, 31). Repository untouched, no Lean build, exact integer arithmetic.

## Setup

R = ℤ[√2], p = 31, modulus p² = 961. α = 3+2√2 has order L₀ = 15 mod 31
and mod 961 (k = 2, s = 0; α¹⁵ mod 31³ = (1,1922), so k = 2 exactly).
G = ⟨α⟩ mod 961, |G| = 15. H0 = ⟨α²⟩ = G (gcd(2,15) = 1), so the H0 test
coincides with the G test (at p=13 it was a proper subgroup, order 7).
Twist: A′ = A(1+31c√2), c = 1..30 (purely imaginary; ζ ∈ G is irrelevant:
it permutes the orbit). Orbit values v_z = Tr(Az) mod 961, z ∈ G,
v_z = v0_z + 31·v1_z; twisted second digit v1′_z = (v1_z + c·t_z) mod 31,
t_z = Tr(A√2·z) mod 31. Genuine twist: A′ ∉ A·G ∪ Ā·G, tested via
ρ·(1+31c√2) ∈ G with ρ = Ā⁻¹A = A²/N(A). Gap case: B = A¹⁵ real mod 31.

## Numbers (exhaustive over all units mod 961)

- Units: 864900 (= 961²·(1 − 61/961)). B-real: 432450 (exactly half;
  at p=13 B-real was automatic for all 28392 units).
- Pairs: 25,947,000 (all), 12,973,500 (B-real). Genuine: 25,528,500 /
  12,555,000. Trivial: 418,500 (all B-real).
- Marginal coincidences: genuine **0**, trivial 418,500.
  Joint preservations: genuine **0**, trivial 418,500.
- So preserving ⟺ trivial, exactly as at p=13. Exact identity at both
  primes: #{trivial pairs} = #{B-real pairs}/p (12,973,500/31 = 418,500;
  340,704/13 = 26,208). Mechanism sketch: for B-real A the condition
  ρ·tw ∈ G is one second-digit equation, i.e. one 𝔽_p-line condition —
  stated as an observation, not proved in general.

## Validation (why these numbers are trusted)

- The same program at p=13 reproduces wave 18 exactly: units 28392,
  B-real all, pairs 340704, genuine 314496, trivial 26208, genuine
  marginal/joint coincidences 0, first trivial example A=(1,2), c=3
  with orbit [2,10,22,24,39,62,82,87,107,130,145,147,159,167].
- The p=31 example A=(1,3), c=13 was cross-checked by direct Python
  multiplication (not the digit formula): orbits identical,
  A′ ∈ Ā·G (trivial), and the digit formula reproduces the direct
  twisted orbit exactly.
- An earlier run had ρ wrong (Ā/N instead of A/N); it was caught by the
  p=13 reproduction and the Python direct check, and fixed before the
  numbers above were produced.

## Illustrative cases (p=31)

- Trivial: A=(1,3), c=13 — orbits identical
  [2,30,33,77,102,178,284,293,319,464,666,695,829,851,943], A′ ∈ Ā·G.
- Genuine: A=(0,1)=√2, c=1 — base
  [0,8,48,98,232,280,290,298,663,671,681,729,863,913,953], twisted
  [36,63,124,138,144,234,263,364,380,453,464,724,760,801,818];
  v1-marginals differ.

## General lemma (formulated)

**Second-digit rigidity (k=2 case, empirical).** Let p be odd with
k = 2, s = 0 (so |G| = L₀ mod p²). For every unit A mod p² and every
c ∈ 𝔽_p^×, the twist A′ = A(1+pc√2) either lies in A·G ∪ Ā·G (a
symmetry: orbit multisets coincide trivially) or changes the
v1-marginal distribution of {Tr(Az) : z ∈ G} (hence the joint
distribution). Verified exhaustively at p=13 (314,496 genuine twists)
and p=31 (25,528,500 genuine twists).

Why (mechanism sketch, not a proof):
1. (v0, t) injectivity: (Tr(Az) mod p, Tr(A√2 z) mod p) determines Az
   mod p, hence z — the shift labels are distinct across the orbit.
2. Dichotomy with power sums (wave 16 §5): power sums of order < L₀
   are blind in the gap case (B real); S_{L₀} = L₀·f·(B−B̄) detects
   non-real-B twists; second digits detect real-B twists. At p=13, 31
   every twist is detected by one or the other.
3. Trivial coincidences are exactly the conjugation symmetries, at
   exact rate 1/p among B-real pairs (observed identity above).

## Scope (honest limits)

- Verified at p=13, 31 only. The next k=2 prime, 1546463, is infeasible
  for exhaustive check (units ~p⁴ ≈ 5.7×10²⁴); the lemma is empirical,
  not proved.
- The f=2 s=0 hole proper additionally needs 4 | L₀ (no instance below
  2×10⁹), and f ≥ 4, general PC, and Lean formalisation remain open.
- This closes the twist *mechanism* at p=13, 31; it is not a proof of
  L6, only the absence of a counterexample at these primes.

## Files

- This note: [wave19_G1_seconddigit.md](wave19_G1_seconddigit.md)
- Checker (fixed ρ): [wave19_G1_seconddigit.cpp](wave19_G1_seconddigit.cpp),
  log: `wave19_G1_seconddigit.log` (not in repository)
- p=13 reproduction: [wave19_G1_seconddigit_p13.cpp](wave19_G1_seconddigit_p13.cpp)
- Direct Python check of the p=31 example: [wave19_G1_p31_example_check.py](wave19_G1_p31_example_check.py)
- Prior notes: [wave18_G1_hole_invariant.md](wave18_G1_hole_invariant.md),
  [wave16_G1_f2s0.md](wave16_G1_f2s0.md)
