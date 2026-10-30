# Line G — Resonant residues, their classification, and a corrected Conjecture R′

Setting: kicked quantized cat map, S = [[3,4],[2,3]], λ = 3+2√2, odd m, h = h_m (NSW numbers 1,7,41,239,1393,8119,47321,275807,1607521),
Z_m(ν) = Σ_n Φ̂(n) e(−νP(n)/(2h)), P(n) = Σ_{i,j} ψ(|i−j|) n_i n_j, q(n) = P(n)/(4h) = nᵀH⁻¹n,
F_m = (1/φ(2h)) Σ_{ν ∈ (Z/2h)^×} |Z_m(ν)|², exact split F = B^sym + 2mχ + W̃rest (Line B), RMT/BGS target F/2m → 2.
Two kicks: "k1" (ĝ(n) = iⁿJ_n(0.9η), η = 2) and Line E's "full" kick (η = 2).

Status tags: **[P]** proved here (pen-and-paper proof given below), **[L]** additionally machine-checked in Lean 4/Mathlib
(no `sorry`, no `native_decide`, axioms = propext/Classical.choice/Quot.sound only), **[N]** numerical (double precision, independent
cross-check stated), **[C]** conjecture. Nothing tagged [N] is an interval-arithmetic certificate (see §7).

---------------------------------------------------------------------------------------------------------------------------------

## 0. Executive summary

1. **Classification of the resonant set (Step 1–2).** Every outlier ν (|Z(ν)|² ≫ 2m) found at m = 7..15, both kicks, is explained by
   one of three mechanisms, all proved as identities:
   * **G1/G2 (rational reconstruction law)** [P,L-core]: for *every* ν and every pair (a,b) with bν ≡ a (mod 2h), Z(ν) is exactly the
     partial trace of the m-th power of an explicit transfer operator 𝓛_{a,b} = Σ_n ĝ(n) R_n^{(−4ac/b)} ⊗ A_n^{(b)} on
     H²(D_ρ) ⊗ C^{b²}. 𝓛 depends on m only through finitely many residues mod b, hence for fixed (a,b) the sequence m ↦ Z(ν_{a,b}(m))
     is an exponential polynomial on each residue class of m. "Dual Planck number": N ≡ b/a (mod h), coupling θ = −2a/b.
     The primaries are short vectors (a,b) of the lattice {bν ≡ a mod 2h}; the dominant ones are N ≡ ±4 (θ = ∓½, Line E's E1) and
     N ≡ ±8 (θ = ∓¼).
   * **G3 (dilution identity)** [P-sketch, N-exact to 3e-14]: for d | h, the d residues ν0 + 2hj/d (j mod d) satisfy
     Z(ν0+2hj/d) = (G_d(t)/d²) Σ_{β∈O/d} e(t̄ Nm β / d) Z^{(β)}_{ν0}, |G_d| = d; main term |Z|² ≈ |Z_ρ|²/d². These are the
     "N ≡ −s·4a² (mod h_m)"-type secondary families: primaries diluted along the divisors of h_m.
   * **G4 (Galois scaling)** [P]: if supp ĝ ⊂ aZ then Z_g(ν) = Z_{g_a}(a²ν). Line E's full kick is dominated by its frequency-7
     harmonic (f ≈ 0.45·2cos(2π·7x) + small non-7-periodic terms), so it is a *perturbation* of an exactly 7-periodic kick; its
     families N ≡ ±196, ±392, ±98 sit at the 49×-images of ±4, ±8, ±2, with crude two-point (m = 11→13) growth estimates ≈ 1.88–1.92, 1.58–1.65, 1.46–1.49 [N] (close to, not
     equal to, k1's 1.915, 1.615, 1.50). G4 is exact only for the 7-periodic part.
   Plus **G5** (h_d | h_m for d | m) [P,L], which is what makes dilution levels appear (7 | h when 3 | m, 41 | h when 5 | m, …).
2. **Sparsity (G6)** [P]: the resonant set 𝓡 = {primaries} ∪ {dilutions with d ≤ D} has |𝓡| ≤ 2|𝓟|τ(h)D; with D = √h its density
   is h^{−1/2+o(1)}.
3. **Moment hierarchy (G7)** [P, given growth rates]: a family with |Z| ≍ r^m affects the 2k-th moment of |Z|² asymptotically
   iff r > λ^{1/(4k)}; for the mean the threshold is λ^{1/4} = 1.5538. Numerically [N] only N ≡ ±4 (r = 1.9154732) and
   N ≡ ±8 (r ≈ 1.615) exceed it among all families tested (N ≡ ±2: r ≈ 1.50, second tier ≤ 1.41).
4. **Corrected conjecture R′** [C, numerical support]:
   F_m = B^sym + 2mχ + Σ_{ρ∈𝓟*} Σ_{d|h, d≤√h} n_d(ρ) |Z_ρ|²/(d² φ(2h)) + W′_m,  W′_m = o(m),
   with 𝓟* = {N ≡ ±4, ±8} (k1) resp. their 49×-images (full kick). Each |Z_ρ|² is given (G2) by an m-independent operator,
   so the correction is explicit and computable for any m (we evaluated it to m = 29).
   Evidence: the explicit resonance sum reproduces the resonant part of F to 0.1–1% for m = 9..15; the remainder W′/m is
   −0.82, −0.31, −0.04, +0.23 (k1) and −1.11, −0.33, −0.03, +0.14 (full) for m = 9, 11, 13, 15.
   **Honest caveat:** W′/m is still drifting upward (≈ +0.27 per Δm = 2 at the last step); o(m) is *not* established by the data.
   m = 17 was pre-registered (sha256 fa8505f5…aa344) before any m = 17 output existed; the outcome is still pending (§5).
   An η-scan shows the remainder is a coupling-dependent finite-m crossover toward the RMT value, not a kick-universal term (§3).
5. **What is not proved:** R′ itself (the bulk equidistribution). Standard tools (Kloosterman / large sieve over the modulus) do not
   apply because the relevant group is the cyclic orbit of λ of order m = O(log h); see §6.

---------------------------------------------------------------------------------------------------------------------------------

## 1. Theorems and proofs

### G1 (exact phase split) [P; Lean: `LineG.phase_split`]
Let bν = a + 2hk with a,b,k ∈ Z, b ≠ 0. Then for every integer P with P = 4hq,
  −νP/(2h) ≡ −(2a/b) q − kP/b  (mod 1).
*Proof.* −νP/(2h) = −(bν)P/(2hb) = −(a+2hk)P/(2hb) = −aP/(2hb) − kP/b and aP/(2hb) = a·4hq/(2hb) = 2aq/b. ∎
So e(−νP/2h) = e(−(2a/b)q)·e(−kP/b): a real-analytic phase with small coefficient when |a|/b is small, times a phase depending
only on P mod b.

### G1′ (automaton for P mod b) [P; Lean: `u_succ`, `w_succ`, `quad_form`]
With ψ0 = ψ(0) = y′ and ψ1 = ψ(1) = 3y′ − 2h, P is accumulated along the word n_0…n_{m−1} by the linear automaton
(u,w) ↦ (6u − w + nψ1, u + nψ0) with step contribution ψ0n² + 2nu (all mod b). (ψ(d) satisfies the λ-recurrence
ψ(d+1) = 6ψ(d) − ψ(d−1) for 0 < d < m, with the cyclic boundary handled by the periodic orbit; Lean checks the one-step algebra
and the quadratic-form identity; the cyclic boundary bookkeeping is checked numerically: 34/34 cases, §4.)

### G2 (partial-trace transfer law) [P]
Fix (a,b), coef := −4ac/b with c = 1/(4√2), L with supp ĝ ⊂ [−L,L], ρ > L/(λ−1). On H²(D_ρ) let
R_n φ(s) = e(coef(n²/2 + ns)) φ((s+n)/λ) (trace class: composition operators with contracting holomorphic symbol), and on C^{b²}
let A_n be the automaton step with phase e(−k(ψ0n² + 2nu)/b). With 𝓛 = Σ_n ĝ(n) R_n ⊗ A_n:
  Z_m(ν) = (1 − λ^{−m}) Tr_H[(I ⊗ ⟨𝟙|) 𝓛^m (I ⊗ |δ_0⟩)].
*Proof.* Expand 𝓛^m over words. The C^{b²} factor gives ⟨𝟙|A_w|δ_0⟩ = e(−kP(n)/b) by G1′. For the H² factor, R_w is a weighted
composition operator with symbol of derivative λ^{−m} and unique fixed point s*(w) (the periodic orbit); the trace formula
Tr(M_p C_ψ) = p(s*)/(1 − ψ′(s*)) gives Tr R_w = e(coef[Σ n_j s_j + ½Σn_j²])/(1−λ^{−m}) = e(−(2a/b)q(n))/(1−λ^{−m}), using
q = 2c[Σ n_j s_j + ½Σ n_j²]. (The composition order reverses the word; q and P are reversal-invariant because H⁻¹ is a symmetric
circulant.) Summing with Πĝ(n_j) and using G1 gives the claim. ∎
*m-dependence.* 𝓛 depends on (coef, b) and on (k, y′, h) mod b only; k mod b is independent of the lift of ν, and (y′, h) mod b
are periodic in m. Hence on each residue class of m mod that period, Z_m(ν_{a,b}) = (1−λ^{−m})·Σ_μ c_μ μ^m + O(r^m) (Riesz projections
of a fixed trace-class operator), i.e. an exponential polynomial whose leading |μ| is the growth rate r of the family.
For k1 the full alphabet is infinite; Galerkin truncation (L ≤ 12) is a numerical approximation and the rigorous infinite-alphabet
version needs Line E's hypothesis H∞ (not proved here).

### G3 (dilution identity) [P (proof sketch, details in check_dilution.py); numerically exact]
Let d | h, t = j y′ (mod d), G_d(t) the quadratic Gauss sum (|G_d| = d for d odd, gcd(t,d) = 1). Writing n ↦ α_n ∈ O = Z[√2]
(P(n) ≡ y′·Nm(α_n) mod h on the relevant lattice) and splitting α_n mod d,
  Z(ν0 + 2hj/d) = (G_d(t)/d²) Σ_{β ∈ O/d} e(t̄·Nm(β)/d) Z^{(β)}_{ν0},
where Z^{(β)} is the same sum with the kick at site i translated by Tr(βλ^i)/d.
*Proof.* Finite Fourier analysis on O/d: insert the indicator of α_n ≡ β (mod d) as an average of additive characters, and complete
the square in e(jP/d) = e(t·Nm(α_n)/d); the β = 0 term gives the main term (G_d/d²) Z_{ν0}. ∎ (Check: 49 cases, max rel. error
2.8e-14, `logs/check_dilution.log`.) Main term: |Z|² ≈ |Z_ρ|²/d². How good the main term is depends on the family:
dominant primaries 0.1–15% (d = 7, 31 at m = 15: 0.1–2%; d = 23, 79: 1–4%; d = 41: 15%; d = 287: 37%), weak primaries: dilution
members are bulk-dominated (`logs/dil_stats.log`). **The size of the β ≠ 0 terms is not bounded rigorously.**

### G4 (Galois scaling) [P]
If ĝ(n) = 0 unless a | n, write ĝ_a(n) = ĝ(an). Then P(an) = a²P(n) gives Z_g(ν) = Z_{g_a}(a²ν). ∎
Consequence (exact for kicks supported on 7Z, approximate for Line E's full kick, whose non-7-periodic Fourier modes are small
perturbations): the full-kick resonances at N ≡ ±196, ±392, ±98 are images (×49 = 7²) of the families ±4, ±8, ±2 of the
7-compressed kick; two-point rate estimates (tier2full) 1.88–1.92, 1.58–1.65, 1.46–1.49.
When 7 | h (m ≡ 0 mod 3, e.g. m = 9, 15) the image does not exist as a unit residue; the corresponding mass appears as a level-7
dilution family ("virtual primary"), which explains why the full-kick F/2m is small at m = 9, 15 (1.82, 3.91) and large at m = 11, 13.

### G5 (divisibility) [P, L: `nsw_dvd`]
For odd d | m, h_d | h_m (via Re-divisibility in Z[√2], Lean `re_dvd_pow`); Lean also checks nsw 3 = 7, nsw 5 = 41, nsw 7 = 239,
1607521 = 103·15607 and h_17² + 1 = 2·1136689².

### G6 (sparsity) [P]
Each pair (ρ, d) contributes at most d residues (one coset of 2h/d, two signs), so |𝓡| ≤ 2|𝓟|·Σ_{d|h, d≤D} d ≤ 2|𝓟| τ(h) D.
With D = √h and τ(h) = h^{o(1)}: |𝓡|/φ(2h) ≤ h^{−1/2+o(1)}. ∎ (Observed resonant fractions: 7.1%, 2.8%, 1.4%, 1.5% for m = 9..15
with the broad step1e list; 14, 46, 158, 990 residues for the 𝓟* list.)

### G7 (moment hierarchy) [P conditional on growth rates]
If |Z_ρ| ≍ r^m and there are O(h^{o(1)}) members at level d = 1, the family's contribution to (1/φ)Σ|Z|^{2k} is ≍ r^{2km}/h,
and h ≍ λ^{m/2}; so it is relevant iff r > λ^{1/(4k)}. k = 1: λ^{1/4} = 1.5538. ∎ (Dilution levels add a factor
Σ_d d·d^{−2k} = O(1) for k ≥ 1.)

---------------------------------------------------------------------------------------------------------------------------------

## 2. Step 1 — numerical map of the residue distribution (m = 7..15, both kicks) [N]

Class sums: orbit-canonical C code (`code/classes_orb.c`), validated against the independent audit implementation
(`computations/verification/lineE/referee/code`) to ≤ 3e-11 at m = 11, 13, 15, both kicks; |Z(ν)|² for all ν via one FFT.

Bulk (non-resonant) F/2m (step1f, insensitive to height cutoff H):

| m | k1 bulk F/2m | full bulk F/2m | k1 total F/2m | full total F/2m |
|---|---|---|---|---|
| 9  | 1.45 | 1.43 | 4.839 | 1.816 |
| 11 | 1.78 | 1.80 | 6.894 | 5.562 |
| 13 | 1.94 | 1.96 | 11.197 | 8.590 |
| 15 | 2.07 | 2.04 | 27.885 | 3.911 |

Largest residues (k1, m = 15): N ≡ ±4: |Z|² = 7.349e7 (share of F/2m: 10.98 each sign); N ≡ ±8: 4.43e5; N ≡ ±2: 8.8e4;
dilutions of ±4 at d ∈ {7, 31, 41, 217, 287}. Bulk second moment E[x²] (x = |Z|² / bulk mean; exponential statistics would give 2) = 2.1, 2.7, 3.2, 3.2 for m = 9..15, with
second-tier outliers up to x ≈ 135 at m = 15 ((±22,96), (±2,12), (4,18) reconstructions). Exponential-type statistics
(E[x²] = 2) are *not* observed for the bulk — consistent with G7: higher moments see weaker families.

Growth rates of |Z| (law G2, Galerkin; cross-checked against class sums at m = 9..15, `logs/law_vs_class.log`, `tune.log`):

| family (a,b) | N ≡ | r | relevant for mean? |
|---|---|---|---|
| (±2, 8)  | ±4 | 1.9154732 (law m ≤ 29, stable to 1e-8) | yes |
| (±2, 16) | ±8 | ≈ 1.615 | yes |
| (±2, 4)  | ±2 | ≈ 1.50 | no (barely) |
| (±6, 16) | ±8/3 | ≈ 1.37 | no |
| (±22, 96), (±2,12), (4,18) | – | 1.33–1.41 | no |

Law vs class sum (m = 15, (2,16)): 442791.6 vs 442791.6 (rel. 6e-9, L = 10, ρ = 2.6, K = 50). Large-coupling θ = 1 primaries need
L = 6 (rel. 1e-4) because larger L overflows (Galerkin instability, not a failure of the identity: the identity itself is exact,
checked by brute force, `logs/check_law.log`).

---------------------------------------------------------------------------------------------------------------------------------

## 3. Conjecture R′ and the explicit formula [C + N]

**Conjecture R′.** For the kicks above,
F_m = B^sym_m + 2mχ + Res_m + W′_m, Res_m = (1/φ(2h)) Σ_{ρ∈𝓟*} Σ_{d|h, d ≤ √h} n_d(ρ)(|Z_ρ(m)|²/d² − RMT_m), W′_m = o(m),
with |Z_ρ(m)|² from G2 (exponential polynomial, leading rate r_ρ). Since r_{±4} = 1.9154732 > λ^{1/4},
Res_m/2m grows like (r²/λ^{1/2})^m/m → ∞: **the original Conjecture R (F/2m → 2) is false for these kicks along all m** (as
already found in Line E); R′ says that this is the *only* obstruction at the level of the mean.

Formula table (k1; "pred" uses the dilution main term, "act" the true members):

| m | F/2m | RMT/2m | Res_pred/2m | Res_act/2m | W′_pred/m | W′_act/m | #res |
|---|---|---|---|---|---|---|---|
| 9  | 4.839 | 1.997 | 3.212 | 3.252 | −0.74 | −0.82 | 14 |
| 11 | 6.894 | 1.999 | 5.050 | 5.052 | −0.31 | −0.31 | 46 |
| 13 | 11.197 | 2.000 | 9.214 | 9.217 | −0.04 | −0.04 | 158 |
| 15 | 27.885 | 2.000 | 25.651 | 25.770 | +0.47 | +0.23 | 990 |

Full kick: W′_act/m = −1.11, −0.33, −0.03, +0.14 (m = 9..15).
Observation: at η = 2 the two kicks give nearly the same W′/m, but an η-scan (k1 kick, `code/eta_scan.py`, `logs/eta_scan.log`;
bulk = outside PR-dilutions and height ≤ 32) shows W′ is **not** kick-universal; it is a coupling-dependent finite-m crossover:

| bulk F/2m | η = 0.5 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| m = 9  | 0.63 | 1.35 | 1.49 | 1.64 | 1.75 |
| m = 11 | 0.76 | 1.61 | 1.74 | 1.87 | 1.90 |
| m = 13 | 0.86 | 1.83 | 1.92 | 1.93 | 1.97 |

(m = 9 removes 47% of residues at height ≤ 32, so its row is only indicative; m = 11: 10%, m = 13: 2.7%.)
At every η the bulk rises with m toward ≈ 2 from below, and faster for stronger kicks. That is consistent with R′ (an approach
to the RMT value once m exceeds a coupling-dependent scale). The overshoot at η = 2, m = 15 (2.07) and whether it stays bounded
is the open question (m = 17 test). The weak-kick deficit is the expected perturbative regime: as η → 0, Z → 1 and F/2m → 1/(2m).

---------------------------------------------------------------------------------------------------------------------------------

## 4. Cross-checks performed
* classes_orb vs audit `classes.c`: max |ΔZ| ≤ 3e-11 (m = 11, 13, 15; k1 and full; m = 15 full: 2.9e-11 on |Z| ~ 4e5).
* G2 law vs brute-force word sum: 34/34 well-conditioned cases agree to 1e-14..1e-9 (`check_law.log`).
* G3 identity: 49 cases, max rel. err 2.8e-14.
* G4: full-kick families located at the predicted 49×-images at m = 11, 13 (tier2full.log); their sizes are not exact images (kick not exactly 7-periodic).
* Lean file `lean/LineG.lean` compiled against the existing Mathlib cache (`logs/lean_LineG.out`).

---------------------------------------------------------------------------------------------------------------------------------

## 5. Pre-registered m = 17 test

(PREDICTIONS_m17.json, sha256 in PREDICTIONS_m17.sha256, written before any m = 17 class sum existed.)
Registered tests (k1, η = 2): primaries ±4, ±8 to 1e-5 (law), ±2, ±8/3 to 1e-3; d = 103 dilution mean 9.33e4 ∈ [7.5e4, 1.17e5];
second tier (±22,96) ≈ 3.3e4, (±2,12) ≈ 1.4e4 (×1.6); bulk F/2m (H = 8 definition) 2.04 ∈ [1.95, 2.15] ⇔ W′/m ∈ [−0.10, 0.30];
total F/2m 39.1 ∈ [38.7, 39.5]. Full kick: Line E's registered ±196 values (TRACE-196), ±392 ≈ 2.0e6 (×1.5), ±98 ≈ 3e5 (×2),
d = 103 dilution of ±196 ≈ 6e4 ∈ [4e4, 9e4], bulk 2.03 ∈ [1.95, 2.15].

**Outcome: NOT YET AVAILABLE.** The m = 17 class sums (`classes_orb`, h² ≈ 2.6e12 points) were still running when this report was
closed (about 30× the m = 15 cost, competing with Line E's m = 17 certificate; several more hours). The evaluator is set up and
validated: `code/watch17.sh` (detached) waits for `done k1 17` / `done full 17` in `logs/batch_orb.log`, records the sha256 of
the output, and runs `code/eval17.py` (implements exactly the registered definitions, PASS/FAIL per item) plus
`formula_table.py <kick> 17`. Results go to `logs/eval17_{k1,full}.log/.json` and are copied to the backup directory.
A dry run on the m = 15 file reproduced the m = 15 bulk value 2.0704 (same definition as step1e), so the pipeline is consistent.
Until those logs exist, **no m = 17 claim is made.**

---------------------------------------------------------------------------------------------------------------------------------

## 6. Attack on the bulk statement (Step 3) — what does and does not work
* **Moments.** Second moment of the bulk is dominated by second-tier families (G7 with k = 2: threshold λ^{1/8} = 1.247 < 1.33–1.41),
  so a CLT/"Gaussian bulk" statement in moment form is false; any proof of R′ must be a first-moment statement.
* **Kloosterman / large sieve over ν.** F_m is an average over ν of a quadratic exponential sum, and Σ_ν|Z|² unfolds to a count of
  pairs (n,n′) with P(n) ≡ P(n′) mod h weighted by Φ̂Φ̂̄′. The large sieve gives Σ_ν|Z|² ≤ (h + N_eff)Σ|Φ̂|², useless because the
  number of effective words N_eff ~ e^{cm} ≫ h. The arithmetic structure (P(n) ≡ y′Nm(α_n)) reduces the problem to equidistribution
  of the cyclic orbit {λ^i} (order m) in O/h, a group far too small (m ≍ log h) for Weil/Kloosterman bounds or Bourgain–Gamburd
  sum-product expansion in its current form.
* **Spectral route.** G2 gives each fixed (a,b) exactly, but the bulk is a sum over ≍ h different (a,b) with b up to √h; uniformity
  of the spectral gap in b is the missing ingredient (equivalent in spirit to Line E's H∞ plus uniformity).
* Hence R′ remains a conjecture; we do not claim progress beyond the explicit identification of the correction term.

## 7. Rigor statement and failures
* Class sums / |Z|² are IEEE double (a-priori rounding bound ~1e-8 relative on |Z|), **not** interval arithmetic. No certified
  enclosure was produced in Line G (Line E's m = 17 certificate is a separate job).
* Growth rates come from Galerkin truncations (no rigorous error bound for the infinite k1 alphabet).
* Lean covers only the algebraic core (phase split, automaton, quadratic form, NSW divisibility, m = 17 facts); G2, G3, G6, G7 are
  pen-and-paper proofs.
* Negative results: Galois-twisted reconstructions (probe.py) do not simplify outliers; shortest-vector classification misses dilution
  families; broad primary lists over-classify (up to 40% of residues at small m).
* The upward drift of W′/m is the main open risk to R′.

## 8. Relation to Line E (PR #57, TRACE-183..196)
* G1/G2 generalize TRACE-183 (E1: N ≡ −4, collapse to q/2 + κ(Σn)²/8) and TRACE-184 (E2: four-sector IFS law, i.e. b = 8 with the
  automaton reduced to the κ-sector sum) to arbitrary lattice vectors (a,b), including composite b and higher powers of 2. TRACE-194
  (E12: a²-resonance law, N ≡ −s·4a²) is the case b = 8a² with a odd. Our m = 15 value for N ≡ ±4 agrees with TRACE-189 (7.34867e7
  and 7.34915e7, attributed to the correct signs), and our law growth rate r = 1.9154732 lies just below TRACE-185's certified
  enclosure [1.9154751, 1.9154771] for L = 6. That is consistent: we use L = 10, and TRACE-185 certifies the truncated L = 6
  operator only.
* G4 is TRACE-193 (E11: pure 7-mode kick Z_f7(ν) = Z_k1(49ν)). For the Line B kick (TRACE-179, our "full"), the 49-image families
  are TRACE-190/192/194/196. Our two-point rates 1.88–1.92 match TRACE-196's float spectral values 1.884 and 1.897.
* G5 overlaps TRACE-193's Lean lemma (7 | h_m ⇔ 3 | m). Our `nsw_dvd` is the general h_d | h_m for d | m.
* The class-sum representation used throughout is TRACE-195's Prop. G.
* New in Line G relative to PR #57: the general (a,b) law and dual-Planck interpretation; the dilution identity G3 for all d | h
  (the explanation of the secondary families); the classification and sparsity statement (G6); the moment hierarchy (G7), and from
  it the identification of N ≡ ±8 (r ≈ 1.615 > λ^{1/4}) as a second family relevant to the mean, besides E1's N ≡ ±4; the explicit
  corrected conjecture R′ with its numerical test; and the η-scan of the bulk. Like TRACE-187/188, R′ does not concern the
  original Conjecture R, which is already refuted for the k1 kick on a finite m-range (TRACE-187, certified) and asymptotically
  under H∞ (TRACE-188).
* Growth rates for N ≡ ±8, ±2 and the second tier are float/Galerkin only. Certifying them in the style of TRACE-185 would be
  the natural next step; TRACE-191 (η-interval certification) is untouched here.

## 9. Literature and novelty
* Kurlberg–Rudnick (2000): Hecke eigenbases / quantum unique ergodicity for unperturbed cat maps; the arithmetic (Hecke) symmetry is
  why the *unkicked* map is non-generic. Our resonances are a different, ν-dependent phenomenon for kicked maps.
* Keating (1991), Keating–Mezzadri (2000): pseudo-symmetries and periods of cat maps; spectral statistics determined by arithmetic of N.
* Degli Esposti–Winn (2005, J. Phys. A 38, 5895): extra symmetries for a positive-density set of N.
* Faure–Nonnenmacher–De Bièvre (2003): scarring for special N (short quantum period) — the closest analogue: there special N with
  small period give non-generic behaviour; here special *residues of the dual parameter* (N ≡ b/a mod h with small a, b) give
  exponentially large |Z|.
* Gutkin–Osipov (2016, coupled cat maps), Haake (book), Bogomolny–Keating (bootstrap/diagonal corrections): diagonal approximation and its corrections for perturbed cat maps / RMT
  form factor; our B^sym + 2mχ is the diagonal term, and Res_m is a non-diagonal arithmetic correction not covered there.
Novelty (to our knowledge, after a literature search that was not exhaustive): (i) the partial-trace law G2 with the "dual Planck
number" interpretation, (ii) the dilution identity G3 explaining secondary families, (iii) the moment hierarchy G7 that pins down
exactly which families matter for the mean, (iv) the explicit corrected statement R′. Each is elementary once set up; the novelty
claim is modest.
