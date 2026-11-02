# Wave 32, task 4 — bound max|f_qt| ≤ m^b with explicit b

## Verdict

**b is proved, and better than asked: for every square component
qt = p² (p odd, v_p(D_m) = 2), every component fiber satisfies
|f_qt| ≤ 2m.** Formally max|f_qt| ≤ m^b with **b = 2**
(2m ≤ m² for m ≥ 2); the sharp form is b = 1 up to the harmless
constant 2, which the wave-25 counting tolerates (it only needs
polynomiality for Δ → 0). The twin hypothesis is NOT needed:
the bound holds for every square component, twin or not.
For qt = p^{2f}, f ≥ 2, the same route stops at one named lemma
(Lemma F2, §6); the m = 48 counting is unaffected, since both
twin qt there (289, 332929) are squares. Repository untouched;
no Lean built.

## 0. Definitions (wave-16 script, wave-25 §5)

Fix sequences mod q are the length-m rows of snf_kernel(m, q):
solutions of y_{j+1} = 6y_j − y_{j−1} mod q with (M^m − I)·seed = 0,
M = [[6,−1],[1,0]]. A component fiber f_qt is a class of rows
under equality of sorted multisets. Γ = dihedral group (cyclic
shifts + reversal of positions) acts on rows; Γ-orbits lie inside
fibers. Hence |f_qt| ≤ 2m · (#orbits in f_qt); the whole proof is
showing #orbits = 1 for square components.

## 1. Lemma (SNF forcing): v_p(D_m) = 2, p odd ⇒ kernel is p·(F_p²)

Let t = α^m + ᾱ^m ∈ ℤ, α = 3+2√2, ᾱ = α^{−1}. Then
D_m = t − 2 (det(M^m − I) = 2 − t, sign aside) and, with
y_m = (α^m − ᾱ^m)/(α − ᾱ) ∈ ℤ, the identity
y_m²·(α − ᾱ)² = t² − 4 gives y_m²·32 = D_m·(t+2).
If v_p(D_m) = 2 then t ≡ 2 (mod p²), so t+2 ≡ 4 (mod p) and,
p odd, v_p(y_m) = 1. Thus y_m ≡ 0 (mod 𝔭) for every 𝔭 | p, so
α^{2m} ≡ 1 (mod 𝔭) and α^m ≡ ±1 (mod 𝔭). The minus sign would
give t ≡ −2 (mod 𝔭), i.e. D_m = t − 2 ≡ −4 (mod 𝔭), impossible
for p odd. Hence α^m ≡ 1 (mod 𝔭) for all 𝔭 | p, i.e.
M^m ≡ I (mod p). With SNF invariants d1 | d2 of M^m − I,
v_p(d1) ≥ 1 and v_p(d1) + v_p(d2) = v_p(D_m) = 2 force
v_p(d1) = v_p(d2) = 1: the kernel mod p² is exactly
p·(a·u + b·v), a, b ∈ F_p, for fixed sequences u, v.
(The same computation shows the (1, p²) SNF case cannot occur
at a square component.)

## 2. Lemma (trace model): rows/p are Tr(Cα^j)

Dividing by p, w(a, b)_j = a·u_j + b·v_j ∈ F_p satisfies the
α-recurrence, so w_j = Aα^j + Bᾱ^j in R_p := F_p[√2] (split
case) or F_{p²} (inert case). F_p-valuedness forces B = Ā
(α ≠ ᾱ since p ≠ 2), so w_j = Tr(Cα^j) for a unique
C ∈ R_p, and (a, b) ↦ C is an F_p-linear bijection
(Tr(C), Tr(Cα)) ↦ (w_0, w_1) has determinant ᾱ − α ≠ 0).
Γ acts as shift C ↦ Cα (using α^m = 1 from §1) and reversal
C ↦ C̄ (since Tr(Cα^{−j}) = Tr(C̄α^j)). So the Γ-orbit of C is
{Cα^j, C̄α^j}, of size ≤ 2d, where d = ord(α) in R_p.
Moreover d | m, d ≥ 3 (α = ±1 would force 𝔭 | 2+2√2 or
4+2√2, of norms −4, 8, impossible for p odd), and p ∤ d
(d | p−1 split, d | p+1 inert).

## 3. Lemma (moments): the multiset determines (N, S)

The length-m vector (Tr(Cα^j))_{j<m} is (m/d) repeats of the
d-cycle (Tr(Cζ))_{ζ∈⟨α⟩}, so its sorted multiset determines
the cycle multiset (divide counts by m/d). Cycle power sums
in F_p, with N = CC̄ and S = Tr(C^d) = C^d + C̄^d:
p_2 = Σ_ζ Tr(Cζ)² = 2d·N (cross terms vanish since d ≥ 3:
Σ_ζ ζ² = Σ_ζ ζ̄² = 0), and p_d = d·S, plus d·binom(d, d/2)·N^{d/2}
if d is even. Since p ∤ 2d, (N, S) is determined by the fiber.

## 4. Lemma ((N, S) determines C up to Γ)

C^d, C̄^d are the two roots (with multiplicity) of
X² − S·X + N^d over F_p. Inert case (field F_{p²}): a degree-2
polynomial has ≤ 2 roots, so C'^d ∈ {C^d, C̄^d}; then
(C'/C)^d = 1 or (C'/C̄)^d = 1, and μ_d(F_{p²}) has order
gcd(d, p²−1) = d (as d | p+1), hence equals ⟨α⟩: C' ∈ Γ·C.
Split case (F_p × F_p, C = (c₁, c₂)): {c₁^d, c₂^d} is
determined by (S, N^d); c₁'^d, c₂'^d ∈ {c₁^d, c₂^d}; the
norm condition c₁'c₂' = c₁c₂ forces the exponents to be
opposite (ζ₂ = ζ₁^{−1}) in the aligned case and the swap in
the crossed case, using μ_d(F_p) = ⟨α₁⟩ (d | p−1); the
"both equal" subcases collapse via (c₁'c₂')^d = (c₁c₂)^d to
c₁^d = c₂^d; zero components are handled directly (the only
d-th root of 0 is 0). Hence C' ∈ Γ·C in all cases.

## 5. Theorem and corollary

Every fiber at a square component qt = p² (p odd) is a single
Γ-orbit, so |f_qt| ≤ 2d ≤ 2m. In particular, over all square
twin components, max|f_qt| ≤ 2m: the wave-25/31 hypothesis
max|f_qt| ≤ m^b holds with b = 2 (sharp: b = 1 up to factor 2).
No twin hypothesis was used anywhere above.

## 6. Exact verification (wave-24 data, recomputed here)

- qt = 289 (p = 17, d = 8): trace model Tr(Cα^j) verified for
  all 289 rows; the (N, S) partition (27 groups) equals the
  fiber partition, and every group is exactly one Γ-orbit.
- qt = 332929 (p = 577, d = 16): trace model verified for all
  332929 rows; the (N, S) partition (10693 groups) equals the
  fiber partition; all 10693 fibers are exactly Γ-orbits,
  max size 32 ≤ 2m = 96.

## 7. Limits: Lemma F2 (f ≥ 2) is open, and is the only gap

For qt = p^{2f}, f ≥ 2, the route above breaks at §3: the
order d_f = ord_{p^f}(α) is divisible by p (order lifts by ×p),
so p_2 = 2d_f·N recovers N only mod p, and root-uniqueness in
§4 fails when p | Δ = (C^d − C̄^d)². **Lemma F2:** every fiber
at qt = p^{2f} is a single Γ-orbit. The smallest test case is
m = 816, qt = 17⁴ (v_17(D_816) = 4 confirmed by direct
recurrence; 17⁴ is twin since 3 ∤ ord(β)); its SNF structure
was not computed here (sympy SNF on 625-digit entries was too
slow and was killed). Also excluded: the 2-part (RB3 territory)
and p = 3 squares, which do not occur (3-adic LTE:
v_3(D_m) ∈ {0} ∪ [4, ∞)). Lean formalisation is open.
