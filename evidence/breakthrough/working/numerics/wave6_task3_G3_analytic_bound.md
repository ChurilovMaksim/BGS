# Wave 6, task 3 — G3: an analytic bound for S, actual kick, m = 3..6

## Status — read first

**This is a proof sketch inside `dlib`'s definitions, not a Lean proof and
not a claim about the bridge.** It closes G3 *conditionally*: it replaces
the numerical values of S (wave 3, task 2) by a *proved* upper bound
S ≤ S_bound(m) that beats the thresholds the wave-5 assembly needs,
for m = 3..6 and for *every* real η — not just the project η-grid.
What it does NOT do:

- It does not prove the identification H4 (bridge `Btup` = `|Z_all|²`
  from `dlib`, kickMatInf = actual kick). That is gap G4, untouched here.
  If H4 fails, this bound is a bound for the `dlib` profile, not for
  the bridge object.
- It is not formalised in Lean. The steps that would need Lean work are
  flagged in §7 (finite SNF certificates, CRT root counts, Parseval
  for the finite FFT — all elementary, none analytic).
- It does not cover general m. §6 reports what happens at m = 7..12
  numerically (extension, not proof); the method's ingredients are
  listed there as per-m checks.

Repository untouched, Lean not built, no numerical value below is
presented as a proved bound — the proved bounds are the integers in
the table of §5, derived from the lemmas, and the *observed* S values
are quoted only for comparison (margins).

## 1. Sources, pinned at HEAD d87dce0

Verified live via the GitHub connector for this task (not copied from
an earlier branch report), repository `ChurilovMaksim/BGS`, HEAD
`d87dce0d9277579568edfee6cffecbc96ea61024` (PR #76):

- `computations/verification/lineB/common/model.py`,
  SHA `ee6296abf76e7a7901132e3ce704ce5baaed3800`:
  `rCoeff`, `fCoeff(k, 0)` — the diagonal coefficients c(0,k), |k| ≤ 9.
- `computations/verification/lineB/phase1/dlib.py`,
  SHA `af79ab79ff6bb5673651afacebb496711aa2bf02`:
  `Orbits` class, `Z_all`, `F`, and the header statement that the
  diagonal kick `f(θ) = Σ_k c(0,k) e(kθ)` is real-valued.
  `f_diag` in `dlib` asserts `|Im| < 1e-12` on its grid and returns
  the real part; the reality below is proved from the coefficients,
  not from that assert (see §3, step 0).

The local re-implementation used for the numerical cross-checks is
`numerics/wave3_task2_actual_kick.py` (wave 3, task 2), whose
`rCoeff`/`fCoeff` logic is verbatim from `model.py` and whose
`Orbits` logic is copied from `dlib.py`. The proof below does not
depend on that script's floating-point output.

## 2. The objects, exactly as in `dlib`

Fix m ∈ {3, 4, 5, 6} and η ∈ ℝ (arbitrary, not just the grid).
Let L = [[0, −1], [1, 6]] (multiplication by λ = 3 + 2√2 on the basis
{1, λ} in `dlib`), A_m = L^m − I, and let (d1, d2, P) be its Smith
normal form data as computed in `dlib.snf2`: P unimodular,
A_m = P · diag(d1, d2) · V⁻¹ for a unimodular V (see §4 for the
explicit certificates). Put D = d1·d2 (= D_m, checked against the
Pell formula in `dlib`), gp = g′_m, yp = y′_m from `dlib.gprime`
(gp = (x−1)/gcd(x−1, y), yp = y/gcd(x−1, y) with (x, y) the Pell pair).

Index set: K = ℤ_{d1} × ℤ_{d2}, |K| = D. For k = (b1, b2) ∈ K,
`dlib` defines

- Φ(k) = exp(i·η·S(k)) ∈ ℂ, where S(k) = Σ_{j=0}^{m−1} f(θ_j(k))
  is a sum of values of the real diagonal kick f (see §3);
- μ = FFT₂(Φ)/D, the normalised 2-D discrete Fourier transform
  of Φ over the grid K (so μ is indexed by the same set K);
- cls(k) = yp · Q(A(k), B(k)) mod gp, where
  (A(k), B(k)) = P·(b1, b2) mod gp (components taken mod gp),
  and Q(A, B) = A² + 6AB + B² (the norm form, `A_*A_ + 6*A_*B_ + B_*B_`
  in `dlib`);
- A_r = Σ_{k ∈ K, cls(k) = r} μ_k for r ∈ ℤ_{gp};
- Z = FFT(A) over ℤ_{gp} (length gp), Z_ν = Σ_r A_r · e(−νr/gp);
- Btup(ν) = |Z_ν|², nuAvgUnits = mean over ν ∈ (ℤ/gp)ˣ of Btup(ν),
  S = Σ_{ν ∈ (ℤ/gp)ˣ} Btup(ν) = φ(gp) · nuAvgUnits.

The class sizes are N_r = #{k ∈ K : cls(k) = r}, r ∈ ℤ_{gp}.

**Needed thresholds** (wave 5, task 4, §3/§7: S ≤ Deff·φ(D)/2,
the factor-2 form; equivalently S < Deff·φ(D) for the exact form):

| m | D | gp | Deff | φ(D) | threshold S ≤ Deff·φ(D)/2 |
|---|---|----|------|------|---------------------------|
| 3 | 196 | 14 | 49 | 84 | 2058 |
| 4 | 1152 | 48 | 72 | 384 | 13824 |
| 5 | 6724 | 82 | 1681 | 3280 | 2756840 |
| 6 | 39200 | 280 | 4900 | 13440 | 32928000 |

Observed (numerical, wave 3 task 2, worst over the η-grid) S values,
for comparison only: 44.75, 168.66, 711.63, 1464.76. The proved
bounds of §5 are far above these — the point is that they are
*proved* and still beat the thresholds.

## 3. The bound: four steps, no analysis of η

**Step 0 — |Φ| = 1 for every real η.** The diagonal coefficients
from `model.py` (l = 0 row) are, in the notation of wave 3, task 2:

k = ±7: 0.45 (real); k = ±1: 0.05 ∓ 0.005i; k = ±6, ±8: −0.025 ± 0.0025i;
k = ±2: ∓0.0025i (i.e. +0.0025i at k = −2, −0.0025i at k = +2);
k = ±5: ∓0.00125i; k = ±9: ∓0.00125i; k = 0: 0.

In every pair, c(0, −k) = conj(c(0, k)). Hence
f(θ) = Σ_k c(0,k) e(kθ) is real-valued for real θ (the terms pair
into 2·Re(c(k)e(kθ))). Therefore S(k) is real for every k, and
|Φ(k)| = |exp(iηS(k))| = 1 for every real η. *This is the only place
the actual kick enters — and only through the conjugation symmetry
of its coefficients, not through their sizes.* In particular the
bound below holds for any real-valued kick on the same grid and
any real η; it is not a fine property of the numbers 0.45, 0.05, …

**Step 1 — ‖μ‖₂ = 1 (Parseval).** μ = FFT₂(Φ)/D over a grid of size D,
so Σ_{k∈K} |μ_k|² = (1/D)·Σ_{k∈K} |Φ(k)|² = (1/D)·D·1 = 1,
by Parseval for the finite Fourier transform. No approximation.

**Step 2 — S ≤ gp · Σ_r |A_r|² ≤ gp · max_r N_r.** First, Z is the
length-gp Fourier transform of A, so Parseval gives
Σ_{ν∈ℤ_{gp}} |Z_ν|² = gp · Σ_r |A_r|². The units (ℤ/gp)ˣ are a
subset of ℤ_{gp} and every term is ≥ 0, so
S = Σ_{units} |Z_ν|² ≤ gp · Σ_r |A_r|².
Second, for each r, Cauchy–Schwarz on the class:
|A_r|² = |Σ_{k: cls(k)=r} μ_k|² ≤ N_r · Σ_{k: cls(k)=r} |μ_k|².
Summing over r and using Σ_r Σ_{k: cls(k)=r} |μ_k|² = ‖μ‖₂² = 1
and N_r ≤ max_r N_r gives Σ_r |A_r|² ≤ max_r N_r. Hence

    S ≤ gp · max_r N_r.                                            (*)

The whole problem is now pure counting: bound max_r N_r.

**Step 3 — the class-count bound (§4–§5).** For m = 3..6,
max_r N_r ≤ 2 · d1 · R(gp), with R(gp) = 4, 8, 4, 16 respectively,
hence S ≤ gp · 2 · d1 · R(gp). The proof of Step 3 is §4; the
resulting table is §5.

Why the earlier `s0` route failed and this one works: the `s0`
route bounds Σ|μ| or Σ|φ| (an ℓ¹ quantity), which for a phase
function is huge (the Fourier coefficients of exp(iηf) spread over
all frequencies, Σ|ĝ| = s0_exp(η) growing fast in η, up to 10²³
in the bridge's units). The route here bounds an ℓ² quantity
(‖μ‖₂ = 1, exact) and pays only the *class multiplicity* max N_r —
a small integer coming from the quadratic-form counting, independent
of η. The toy-ĝ counterexamples of wave 2 are not counterexamples
to (*): there the weights are unnormalised products of ĝ (ℓ² norm
growing like (Σ|ĝ|²)^m, i.e. the t^{2m} explosion), whereas here
the weights are Fourier coefficients of a *phase* (|Φ| = 1), whose
ℓ² norm is pinned to 1 by Parseval. The normalisation is the whole
content — and it is exactly what the wave-3 note identified
(`|exp(iηf)| = 1`) without turning it into a bound.

## 4. Proof of Step 3: class counting

Fix m ∈ {3, 4, 5, 6} and r ∈ ℤ_{gp}. We count
N_r = #{(b1, b2) ∈ ℤ_{d1} × ℤ_{d2} : cls(b1, b2) = r}.

**(a) SNF certificates (finite, checkable by hand).** The matrices
A_m = L^m − I and their SNF data from `dlib` are:

| m | A_m = L^m − I | d1 | d2 | P | V⁻¹ | det P |
|---|---|---|---|---|---|---|
| 3 | [[−7, −35], [35, 203]] | 7 | 28 | [[−1, 0], [5, 1]] | [[1, 5], [0, 1]] | −1 |
| 4 | [[−36, −204], [204, 1188]] | 12 | 96 | [[−3, −1], [17, 6]] | [[1, 3], [0, 1]] | −1 |
| 5 | [[−205, −1189], [1189, 6929]] | 41 | 164 | [[−5, −1], [29, 6]] | [[1, 5], [0, 1]] | −1 |
| 6 | [[−1190, −6930], [6930, 40390]] | 70 | 560 | [[−17, −6], [99, 35]] | [[1, 3], [0, 1]] | −1 |

In each case P · diag(d1, d2) · V⁻¹ = A_m (2×2 integer matrix
multiplication, verifiable by hand), det P = −1 and det V⁻¹ = 1,
so P and V⁻¹ are unimodular, and d1 | d2 (7|28, 12|96, 41|164,
70|560). Hence (d1, d2) is indeed the Smith normal form of A_m
(a diagonal form with d1 | d2 reached by unimodular transformations
is the SNF). Consequences used below, all read off the table:

- d1 | gp and d2 = 2·gp in all four cases:
  (7|14, 28 = 2·14), (12|48, 96 = 2·48), (41|82, 164 = 2·82),
  (70|280, 560 = 2·280).
- det P = −1, so P is invertible mod gp, and its second column
  β = (P01, P11) satisfies gcd(P01, P11) = 1 (any common divisor
  divides det P = −1) and, from the table,
  Q(β) = 1 in all four cases:
  (0, 1) → 1; (−1, 6) → 1 − 36 + 36 = 1; (−1, 6) → 1;
  (−6, 35) → 36 − 1260 + 1225 = 1.
- yp is a unit mod gp: yp = y/gcd(x−1, y), gp = (x−1)/gcd(x−1, y),
  so gcd(yp, gp) = 1 by definition of the gcd. Hence
  cls = r ⟺ Q(A, B) ≡ yp⁻¹·r (mod gp), with yp⁻¹ the inverse mod gp.

**(b) Reduction to a monic quadratic in one variable.** Write
b2 = t + gp·s with t ∈ ℤ_{gp} and s ∈ {0, 1}: this is possible
with exactly 2 lifts per t because d2 = 2·gp, i.e. b2 ranges over
two complete residue systems mod gp. Therefore

    N_r = 2 · #{(b1, t) ∈ ℤ_{d1} × ℤ_{gp} : Q(P·(b1, t)) ≡ yp⁻¹r (mod gp)},

where (b1, t) is read as integers (b1 < d1 ≤ gp, so b1 mod gp is
just b1; the map ℤ_{d1} → ℤ_{gp} by representative is injective,
which is all we need for counting — it is not a homomorphism and
we do not use it as one).

Fix b1 and set α = b1 · (first column of P), β = (second column).
Then P·(b1, t) ≡ α + tβ (mod gp), and with B the bilinear form
of Q, B((A,B),(A′,B′)) = AA′ + 3(AB′ + A′B) + BB′,

    Q(α + tβ) = Q(α) + 2t·B(α, β) + t²·Q(β)
              = t² + L·t + C   (mod gp),

a *monic* quadratic in t, because Q(β) = 1 by (a). (L, C depend
on b1 and r, but the leading coefficient is always 1 — that is
the point of Q(β) = 1.) So for fixed b1, the number of t is the
number of roots of a monic quadratic mod gp, bounded by R(gp)
in (c) below, independently of b1 and r. Hence
#{…} ≤ d1 · R(gp) and N_r ≤ 2·d1·R(gp), as claimed.

**(c) Root-count lemma (CRT).** Let R(gp) be:

| m | gp | factorisation | prime-power root bounds | R(gp) |
|---|---|---|---|---|
| 3 | 14 | 2 · 7 | mod 2: ≤ 2; mod 7: ≤ 2 | 4 |
| 4 | 48 | 2⁴ · 3 | mod 16: ≤ 4; mod 3: ≤ 2 | 8 |
| 5 | 82 | 2 · 41 | mod 2: ≤ 2; mod 41: ≤ 2 | 4 |
| 6 | 280 | 2³ · 5 · 7 | mod 8: ≤ 4; mod 5: ≤ 2; mod 7: ≤ 2 | 16 |

Justification. By the Chinese remainder theorem, roots mod gp
correspond bijectively to tuples of roots mod each prime power
(the polynomial equation is preserved under reduction mod each
prime power), so the total count is the product of the prime-power
counts. For an odd prime p (exponent 1 in all cases above):
t² + Lt + C mod p is a polynomial of degree ≤ 2 over the field
𝔽_p, hence has at most 2 roots unless it is the zero polynomial
(which it is not, being monic). For the 2-powers 2, 8, 16:
a monic quadratic mod 2^e (e = 1, 3, 4) has at most 4 roots
(2 for e = 1), as follows. If L is odd, (2t + L)² ≡ L² − 4C
(mod 2^{e+2}) is equivalent to the original equation (multiply
by 4), and odd square roots mod 2^k (k ≥ 3) are at most 4: if
y² ≡ z² (mod 2^k) with y, z odd, then 2^k | (y−z)(y+z), and since
exactly one of y−z, y+z is ≡ 2 (mod 4) (their sum 2y ≡ 2 mod 4),
the other is divisible by 2^{k−1}, giving at most 4 possibilities.
If L is even, write L = 2L₁: the equation becomes
(t + L₁)² ≡ L₁² − C (mod 2^e), a square equation mod 2^e with
e ≤ 4, whose roots number at most 4 by direct inspection of
squares mod 16 (even x give squares 0 or 4 mod 16, odd x give
1 or 9 mod 16, each value attained by exactly 4 residues mod 16;
mod 8 the same check gives at most 4). The product bounds above
follow. (For the record, the exact maxima, computed by finite
enumeration over residues mod gp, are exactly 4, 8, 4, 16 —
the CRT bounds are sharp here; the enumeration is a check, not
the proof, since the CRT argument above already gives the bounds.)

This completes Step 3 and hence the bound (*).

## 5. Result: proved bounds vs thresholds

| m | gp | d1 | R(gp) | proved S ≤ gp·2·d1·R(gp) | threshold Deff·φ(D)/2 | margin (threshold / bound) | observed worst S (numerical, for comparison) |
|---|---|----|-------|--------------------------|------------------------|----------------------------|----------------------------------------------|
| 3 | 14 | 7 | 4 | **784** | 2058 | 2.6× | 44.75 |
| 4 | 48 | 12 | 8 | **9216** | 13824 | 1.5× | 168.66 |
| 5 | 82 | 41 | 4 | **26896** | 2756840 | 102× | 711.63 |
| 6 | 280 | 70 | 16 | **627200** | 32928000 | 52× | 1464.76 |

In particular, with the wave-5 assembly's S-route, the Deff branch
for the actual kick follows *with a proved S-bound* (not a numerical
S-value) at m = 3..6, for every real η, once G1 (radical), G2
(window counts) and G4 (identification) are in place. The tightest
case is m = 4 (margin 1.5×); m = 3 has margin 2.6×. There is no
room to lose a factor 2 in the counting at m = 4: the factor 2
from d2 = 2·gp and the root bound R(48) = 8 are both load-bearing
there — if either were doubled (b2 multiplicity 4 instead of 2,
or R(48) = 16 instead of 8), the bound would become
18432 > 13824 and fail at m = 4 (it would still pass at m = 3).

**Corollary (η-uniformity).** Since Steps 0–3 use η only through
|exp(iηS(k))| = 1, the bound S ≤ gp·2·d1·R(gp) holds for all real η
simultaneously, not just the project grid
{0.5, 1, 2, 5, 10, 25, 50, 100, 200}. The assembly's restriction to
the grid came from the numerical S-values; the analytic bound
removes it (within the `dlib` model, i.e. modulo G4).

**What the bound is not.** It is not sharp: observed S is 17×–430×
below the proved bound (m = 3: 784/44.75 ≈ 17.5×; m = 6:
627200/1464.76 ≈ 428×). The slack is in Step 2 (Cauchy–Schwarz
assumes adversarial alignment of μ with the classes, and the
units-only sum is replaced by the full sum) and in Step 3 (the
root bound R(gp) is a worst case over all b1, r, and all monic
quadratics, while the actual (L, C) pairs are far from worst-case).
Sharpening is not needed for G3 — the thresholds are beaten as is
— and any sharpening that used the actual μ (e.g. the deviation
bound of wave 4, task 3) would reintroduce η-dependence and the
exact-constant problem, which G3 does not ask for.

## 6. Extension: does the method survive at m ≥ 7? (probe, not proof)

The ingredients of §4 at general m are per-m checks: (i) d1 | gp
and d2/gp small, (ii) det P = ±1 and Q(second column) = 1,
(iii) gp's factorisation and the CRT root bound, (iv) the
threshold Deff·φ(D)/2. A probe was run for m = 7..20 using
*SNF data only* (exact integers: Pell pair, SNF of the 2×2 matrix
L^m − I via sympy, φ(D), Deff) — deliberately *not* the `Orbits`
grid construction, which is infeasible at large m (an earlier
attempt to build the full `Orbits` grids up to m = 12 was killed
by the OOM killer, exit 137, with no output; the grid at m = 11
alone has 263,672,644 points). The probe bound is
S ≤ gp · (d2/gp) · d1 · R(gp) with R(gp) from the CRT product
formula: odd prime p^e contributes 2·p^{⌊e/2⌋} (proved as in §4(c)
for e = 1, and by the valuation argument sketched below for e > 1),
2-power 2^e contributes 2 (e = 1), 4 (e ≤ 4), 2^{⌈e/2⌉} (e ≥ 5,
probe formula only — the §4(c) proof covers only e ≤ 4).

Results (ratio = probe bound / threshold Deff·φ(D)/2):

| m | d1 | gp | d2/gp | R(gp) | probe S-bound | ratio to threshold | passes? |
|---|---|----|-------|-------|---------------|--------------------|---------|
| 7 | 239 | 478 | 2 | 4 | 913,936 | 2.8·10⁻⁴ | yes |
| 8 | 408 | 1632 | 2 | 32 | 42,614,784 | 2.5·10⁻³ | yes |
| 9 | 1393 | 2786 | 2 | 8 | 62,094,368 | 1.9·10⁻⁵ | yes |
| 10 | 2378 | 9512 | 2 | 16 | 723,825,152 | 1.2·10⁻⁵ | yes |
| 11 | 8119 | 16238 | 2 | 8 | 2,109,381,152 | 5.1·10⁻⁷ | yes |
| 12 | 13860 | 55440 | 2 | 192 | 295,064,985,600 | 1.9·10⁻⁵ | yes |
| 13 | 47321 | 94642 | 2 | 8 | 71,656,865,312 | 1.4·10⁻⁸ | yes |
| 14 | 80782 | 323128 | 2 | 208 | 10,858,817,255,936 | 1.4·10⁻⁷ | yes |
| 15 | 275807 | 551614 | 2 | 496 | 150,921,890,478,016 | 3.2·10⁻⁸ | yes |
| 16 | 470832 | 1883328 | 2 | 64 | 113,501,579,378,688 | 3.7·10⁻⁹ | yes |
| 17 | 1607521 | 3215042 | 2 | 8 | 82,691,960,494,112 | 1.3·10⁻¹¹ | yes |
| 18 | 2744210 | 10976840 | 2 | 64 | 3,855,712,524,339,200 | 5.0·10⁻¹¹ | yes |
| 19 | 9369319 | 18738638 | 2 | 4 | 1,404,546,216,380,176 | 1.8·10⁻¹³ | yes |
| 20 | 15994428 | 63977712 | 2 | 128 | 261,961,448,496,316,416 | 6.8·10⁻¹² | yes |

And the structural pattern behind the probe held at *every*
m = 3..20, without exception: d1 | gp, d2 = 2·gp, det P = −1,
Q(second column of P) = 1. Moreover gp/d1 alternates cleanly:
gp = 2·d1 for odd m, gp = 4·d1 for even m (m = 3..20). This is
strong evidence for a general structural lemma — the SNF of
L^m − I is (d1, 2·gp) with gp/d1 ∈ {2, 4} by parity — which,
if proved from the Pell recurrences (d1 = gcd of the entries of
L^m − I; d1·d2 = det = D_m), would promote the whole §4 argument
to general m, with the only remaining general-m inputs being
the CRT root bound for arbitrary prime exponents (odd p^e:
≤ 2·p^{⌊e/2⌋} by the valuation argument: if v_p(Δ) = 2k < e,
y = p^k·u with u² ≡ unit (mod p^{e−2k}) has ≤ 2 solutions mod
p^{e−2k} by Hensel, times p^k lifts; if v_p(Δ) ≥ e, count =
p^{⌊e/2⌋}; if v_p(Δ) odd < e, no solutions; and the analogous
2-adic valuation casework) and the threshold comparison, whose
asymptotics strongly favour the bound (bound ~ gp·d1·R(gp) ~
D·(divisor-like) vs threshold ~ Deff·φ(D) ~ D²/rad-type).

Status, stated plainly: §6 is a *pattern plus a route*, not a
theorem. The proved result of this note is m = 3..6 only (§5).
G6 (general m) remains open, but its next step is now concrete:
prove the SNF pattern (d1, d2) = (gp/2 or gp/4, 2·gp) and
Q(col2) = 1 from the Pell recurrences, and prove the general
prime-power root bound; the threshold comparison then follows
from the same counting as §4. No new idea is needed for the
threshold step — only the two lemmas above.

## 7. What remains for G3 to be fully closed (Lean / formalisation)

G3 as stated in the assembly was: "a proved upper bound for S,
not a numerical value". The mathematical proof sketch above
supplies it modulo G4. To turn the sketch into a Lean lemma
(within the `dlib`-model statement, i.e. assuming the identification
as a hypothesis), the following formalisation steps are needed,
none of which is analytic:

1. **Finite SNF certificates.** The table in §4(a): verify
   P·diag(d1,d2)·V⁻¹ = L^m − I by 2×2 integer matrix multiplication
   (a `decide`/`norm_num`-scale computation), det P = −1, d1 | d2,
   d1 | gp, d2 = 2·gp, Q(second column) = 1. All are closed integer
   identities at fixed m.
2. **Parseval for finite FFTs.** Σ|μ|² = 1 from |Φ| = 1, and
   Σ_ν |Z_ν|² = gp·Σ_r |A_r|². In Mathlib these are instances of
   Plancherel for `ZMod` Fourier transforms, or can be proved by
   the standard orthogonality of roots of unity (finite sums).
3. **Cauchy–Schwarz per class** (finite sums) and the units-subset
   inequality — elementary.
4. **CRT root bound.** The prime-power bounds of §4(c): odd prime
   (degree bound over a field), 2-power e ≤ 4 (the square-root
   case analysis, or finite `decide` over residues mod 16/8/2).
   The CRT product step is standard.
5. **Reality of f.** c(0, −k) = conj(c(0, k)) from the `model.py`
   formula for `fCoeff(k, 0)` — a finite check over k = −9..9
   (the formula is `0.5·[k = ±7] + rCoeff(k)/10 +
   (rCoeff(k−1) − rCoeff(k+1))/(200i) − 0.1·[k = 0]`, with rCoeff
   real and even: rCoeff(−k) = rCoeff(k); the (rCoeff(k−1) −
   rCoeff(k+1)) term is odd in k, hence purely imaginary and
   odd, i.e. conjugated under k ↦ −k).

None of these steps requires the Pell C1 draft or the radical
draft (G1) — the S-bound is independent of them; it is G1/G2
that the assembly needs alongside it, plus G4 for the transfer
to the bridge. The genuinely hard formalisation step in G3's
neighbourhood remains G4 (identifying `dlib`'s Z with the bridge's
Btup), not the S-bound itself.

## 7b. Portable core lemma (for the formalisation wave)

The analytic content of §§3–4, stripped of all `dlib` machinery,
is the following self-contained finite statement. It is the lemma
a Lean formalisation should actually prove; the `dlib` objects
then enter only through its hypotheses (which is exactly G4's job
to discharge for the bridge).

> **Core lemma.** Let K be a finite set, gp ≥ 1 an integer,
> cls : K → ℤ_{gp} a map, N_r = #{k : cls(k) = r}, and
> μ : K → ℂ with Σ_{k∈K} |μ_k|² = 1. Define
> A_r = Σ_{k: cls(k)=r} μ_k and Z_ν = Σ_r A_r·e(−νr/gp).
> Then Σ_{ν ∈ (ℤ/gp)ˣ} |Z_ν|² ≤ gp · max_r N_r.
>
> *Proof.* Parseval for Z (Σ_{ν∈ℤ_{gp}} |Z_ν|² = gp·Σ_r |A_r|²),
> restriction to units (non-negative terms dropped), and
> Cauchy–Schwarz per class as in §3, Steps 1–2. ∎

Everything kick-specific in this note is then: (i) the `dlib`
μ satisfies Σ|μ|² = 1 (Parseval + |Φ| = 1, §3 Step 0–1);
(ii) the `dlib` cls has max_r N_r ≤ 2·d1·R(gp) (§4). A Lean
proof of the core lemma needs no Pell numbers, no SNF, and no
kick coefficients at all.

## 8. Bottom line for the parent

- **G3 is closed as a mathematical argument, modulo G4:**
  S ≤ 784, 9216, 26896, 627200 at m = 3, 4, 5, 6 respectively,
  for all real η, by Parseval + Cauchy–Schwarz + class counting.
  The assembly's Deff branch for the actual kick no longer depends
  on any numerical S-value.
- The binding case is m = 4 (margin only 1.5×); the other cases
  have margins 2.6×, 102×, 52×.
- The method's secret is that it never bounds Σ|μ| (ℓ¹, huge for
  a phase) — it bounds ‖μ‖₂ = 1 (exact) and pays only the small
  class multiplicity max N_r ≤ 2·d1·R(gp).
- Remaining for the assembly as a whole: G1 (radical, draft exists),
  G2 (units, draft exists), G4 (identification — the real blocker
  now), G5 (exact constant, separate), G6 (general m — but §6 shows
  the method's SNF pattern and threshold margin hold as a probe to
  m = 20, so G6's next step is two concrete lemmas, not a new idea).
- No interval arithmetic is needed for G3 anymore; the
  interval-arithmetic fallback proposed in the task is superseded
  by the analytic bound (it remains a possible *alternative*
  certification route for S, but it is no longer the critical path).

## Sources

- Wave 5, task 4 assembly: `numerics/wave5_task4_hEquidistUnits_assembly.md`
  (thresholds, S-route, gaps G1–G8).
- Wave 3, task 2: `numerics/wave3_task2_note.md`,
  `numerics/wave3_task2_actual_kick.py` (numerical S table, `dlib`
  logic, `|exp(iηf)| = 1` observation).
- Wave 4, task 3: `numerics/wave4_task3_note.md` (exact constant as
  oscillation; deviation bound — not used here).
- Main (via connector, HEAD d87dce0, SHAs in §1):
  `computations/verification/lineB/common/model.py`,
  `computations/verification/lineB/phase1/dlib.py`.
