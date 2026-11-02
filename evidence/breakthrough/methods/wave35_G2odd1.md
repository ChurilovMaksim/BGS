# Wave 35, task 5: gap G-2odd-1 — the t=2, a=b subcase of JBL

## Verdict

G-2odd-1 is **closed for m=18 and for every m ≡ 2 (mod 4) with at most one
constraining odd prime** (m = 6, 10, 14, 22, 26, …). The general case
(≥ 2 constraining primes: m = 30, 34, 38, 42, …) is **reduced to one named
lemma, PAIR** (§5), still open. No counterexample exists at m = 6, 10, 18.

## 1. Constraining primes

Let m = 2u, u odd, β = α². Then
D_m = Tr(α^{2u}) − 2 = Tr(α^u)² − 4 = D_u · (Tr(α^u) + 2),
and for odd p, gcd(D_u, Tr(α^u)+2) = 1 (a common divisor divides 4).
Hence odd prime powers ‖ D_m split into two kinds:

- **Non-constraining:** q ‖ D_u. Then α^u ≢ −1 (mod 𝔭) for every 𝔭 | q
  (else p | Tr(α^u)+2, contradicting gcd = 1), so α^u+1 is a unit mod q.
- **Constraining:** q ‖ Tr(α^u)+2. Then α^u ≡ −1 (mod 𝔭) for some 𝔭 | q,
  so a nonzero antiperiodic part exists.

Tr(α^u)+2 = 8·(square) for u odd (verified to u = 31). Constraining odd
primes: m=6: {5}; m=10: {29}; m=14: {13}; **m=18: {5, 197}** (first with
two); m=22: {5741}; m=26: {33461}; m=30: {5, 29, 269}; m=34: {137, 8297}.

## 2. Unit lemma (non-constraining components never constrain π)

Let q be odd, B genuine mod q (B(α^{2u}−1) ≡ 0). If α^u+1 is a unit mod q,
then Ann(α^{2u}−1) = Ann(α^u−1), so Bα^u = B. The α-orbit of B then has
odd size d | u, so α = β^s on the orbit (2 invertible mod d), hence
T(Bα) = T(B), where T(C) is the β-orbit trace multiset. Class multisets
M_E = (u/d)·T(B), M_O = (u/d)·T(Bα) coincide, so Π_q is full.
In the a=b subcase Π₂ is also full (constant mod-32 vectors). Therefore
**π is determined entirely by the constraining components.**

Corollary: if m has ≤ 1 constraining prime, PC in the a=b subcase is
trivial — the common π is π at that one component (nonempty by G1/G2).

## 3. m=18: exact computation (script `wave35_G2odd1_m18.py`)

D₁₈ = 2⁵·5²·7²·197²·199². Constraining: 25, 38809. Non-constraining:
49, 39601 (α⁹+1 a unit mod both: gcd(Tr(α⁹)+2, 49) = gcd(·, 199) = 1).

Slice: mod-32 constant, mod-49 and mod-39601 components zero. The slice
is fiber-closed (mates must keep multiset {0×18} at 49/39601 and {a×18}
at 32), and in it the global multiset condition is *exactly* the pair
multiset condition on (mod-25, mod-38809) pairs (CRT is injective on
pairs). Kernels: mod 25 by brute force (625 pairs → 25 vectors);
mod 38809 via B = 197·C, C ∈ R/197 (38809 distinct vectors, recurrence +
18-periodicity verified directly; completeness follows from the product
constraint Π|ker_q| = D₁₈).

Results: 970,225 slice points, 27,445 fibers, 942,780 (base, other) pairs.
Π₂₅: neither = 0; Π₃₈₈₀₉: neither = 0. **Common-π failures: 0.**
Patterns (id25, sw25, id38, sw38): swap-only/swap-only 222,264;
id-only/id-only 209,720; singleton/both and both/singleton 10,000–240,786;
both/both 22,060. The two mixed-singleton patterns (id-only/swap-only and
swap-only/id-only) are **absent**.

## 4. From slice to full space at m=18 (marginal reduction)

Any full-space a=b fiber pair projects, mod 25·38809, to a pair-multiset
match, hence to a pair in one slice fiber. By §3 every slice-fiber pair
has a common π (base-vs-other checks suffice by transitivity:
π₁⁻¹π₂ is common for (other1, other2)), and 49/39601/32 are full (§2).
**Therefore every a=b fiber pair at m=18 has a common π ∈ D₂: PC holds
in the a=b subcase at m=18.** This is a proof modulo the established
component lemmas G1/G2 and the exact, reproducible computation above.

## 5. Remaining gap: lemma PAIR (pairwise SPLIT)

For D₂, pairwise agreement implies global agreement: if no global common
π existed, some component would miss id and another would miss swap,
and that pair would disagree. So general a=b PC reduces to:

**PAIR.** For any m ≡ 2 (mod 4) and any two constraining components
q_a, q_b, a pair-multiset match forces π_{q_a}, π_{q_b} to agree.

§3–§4 prove PAIR for the pair (25, 38809) at m=18. Direct enumeration
is infeasible for the next cases (m=30 slice: 625·841·72361 ≈ 3.8×10¹⁰;
m=34: ≈ 1.3×10¹²), so PAIR needs a theoretical proof. Lead: if the trace
multisets T(B), T(Bα) have disjoint supports at both components, a mixed
pair is impossible by signature (even pairs of y′ carry first-coordinate
from the even side and second from the odd side, matching neither side
of y); the general case needs this argument without disjointness.

## 6. What G-2odd-1 needs next

PAIR (above). If PAIR is proved, the t=2 class-partition lemma is complete
(a ≠ b by wave-34 2-periodicity counting; a = b by §2 + PAIR), and the
t=2 case of JBL's class part is closed. No Lean work was done (per brief).
