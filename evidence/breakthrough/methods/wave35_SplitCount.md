# Wave 35, task 3 — Split-Count Lemma: FALSE, with a proved count in the lift regime

## Verdict

**The Split-Count Lemma (n_q ≤ 10 for every component q) is FALSE.**
Two exact counterexamples, both on-support:

- **Odd: (m, q) = (816, 17⁴), n_q = 18** — ten fibers of size 4624
  (17 orbits each) plus eight fibers of size 2312 (17 orbits each),
  all fully supported.
- **2-part: (m, q₂) = (128, 2¹⁷), n_q = 15** (on-support; 25 split
  total, 10 fully unsupported, 0 mixed). Sequence: m = 32 → 5,
  m = 64 → 10, m = 128 → 15 — five new fibers per v₂-level.

The n_q ≤ 10 route to SC(c = 5) is therefore dead. SC(c = 5)
itself is NOT refuted: at (816, 17⁴) the contribution is
10·4624² + 8·2312² = 256,576,512 against m⁵ ≈ 3.6·10¹⁴
(slack ~10⁶×); at (128, 2¹⁷) it is 979,456 against 128⁵ ≈ 3.4·10¹⁰.

## Counterexample 1: (816, 17⁴) — three independent counts agree

Trace model mod 289 (kernel rows mod 17⁴ are 289·Tr(Cα^j),
C ∈ R/289, d' = ord₂₈₉(α) = 136). Counted three ways:
hashed TM census, exact np.unique census (no hashing), and
direct rows (recurrence + periodicity + wave-16 support +
dihedral row orbits, all 18 representatives: rec ✓, supported ✓,
row-orbit sizes 136/272 matching 2312/17, 4624/17). Support is
constant on fibers (mixed = 0). The F2 fiber (4624 = 17·272) is
one of the ten large ones. Scripts: `wave35_tm_census.py`,
`wave35_verify.py`, `wave35_directcheck.py`.

## Counterexample 2: (128, 2¹⁷) — 2-part

Direct kernel census (sorted rows, seed-space Γ-orbits,
wave-16 support): 15 on-support split fibers — sizes 512 (×3),
256 (×2), 128 (×3), 64 (×2), 32 (×4), 16 (×2), with 8/8/4/4/2/2
orbits. Script: `wave35_2part.py` (m = 32, 64 confirm 5, 10).

## Proved count in the f' = 2 lift regime (odd p)

Let qt = p² in trace model (f' = 2), d = ord_p(α),
e = v_p(α^d − 1). Assume e = 1. By LTE,
f' = 2 forces v_p(m/d) = 1, so p | m/d automatically.
Write j = j₀ + d·t. Then α^{dt} ≡ 1 + p·u·t (mod p²), u a unit,
and Tr(Cα^{j₀+dt}) = A_{j₀} + p·t·B_{j₀} (mod p²) with
B_{j₀} = Tr(Cα^{j₀}u) mod p. Since p | m/d, t mod p is uniform
on each line: the line contributes the FULL lift fiber above
A_{j₀} mod p iff B_{j₀} ≠ 0, else the constant A_{j₀}.
Let Z = {j₀ : B_{j₀} = 0}. Then the fiber meets the lifts of
[C] in {C + pE : Tr(Eα^{j₀}) = 0 ∀j₀ ∈ Z}:

- Z = ∅: all p² lifts → the fiber has p orbits → SPLIT.
- Z ≠ ∅: |Z| ≤ 2 (a Lucas sequence has ≤ gcd(d,2) zeros), and
  the constraint space equals the orbit's line shifts ⟨Cu⟩
  (Cu ≠ 0 mod p, Cu ∈ constraint space since Tr(Cu·α^{j₀}) =
  B_{j₀} = 0 on Z) → fiber = orbit → NOT split.

Hence, in this regime, **split fibers ⟷ mod-p orbits [C] with
Z = ∅, one split fiber each, with exactly p orbits**.
Counting orbits with Z = ∅ (element count, min orbit size d):
zero-divisor orbits (p−1)/d, both-nonzero ≤ (p−1)²/d, so

    n_q ≤ (p−1)²/d + (p−1)/d ≤ p² ≤ m²,

using split ⇒ p | m (wave 34 §4). Exact checks: (816, 17):
2 + 16 = 18 ✓ (d even, so the w-twist is trivial); (21, 7):
5 via the w-twisted count (d odd, w = −1: 3 both-nonzero + 2
zero-divisor; the naive formula would give 8 — the twist matters).
The argument shape is the same in the inert case (F_{p²}).

## Consequence for SC, and what remains open

With n_q ≤ m² (lift regime) + s_q ≤ m² (wave 34 §1) +
ω(D_m) < 2.54m, the f' = 2 contribution to Σ is ≤ 2.54·m⁷:
polynomial, so Δ → 0 survives with a worse exponent, but
SC(c = 5) is no longer proved by counting. Open gaps, stated
as lemmas to prove, not facts:

- **Lift-Tower Lemma:** every split fiber mod p^{f'} reduces to
  a split fiber mod p², at most one per depth (data: (147, 343):
  10 = 5 base × 2; (108, 81): 3 = 1 base × 3). With it,
  n_q ≤ (f'−1)·n(p²) = O(m² log m).
- **Outside-regime vanishing:** no splits observed at level 2
  with e ≥ 2 ((465, 31), (30, 31): 0) or level 1 ((48, 577): 0);
  the wave-32 moment argument should lift since d_{p²} = d,
  p ∤ d — sketch only.
- **2-part count:** the 5-per-level pattern is observed at
  three levels, not proved.

Repository untouched, no Lean built.
