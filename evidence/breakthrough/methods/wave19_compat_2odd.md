# Wave 19, task 4 — 2-vs-odd per-class compatibility at prime-power level

## Statement

Let t = gcd(m, 4), q₂ = 2^{v₂(D_m)}, classes O_r = {i : i ≡ r mod t}.
For y, y′ ∈ Fix_m with the same sorted multiset (exact integers) and
q ‖ D_m, let Π_q = {π ∈ D_t : per-class multisets mod q of y′ equal
those of y composed with π, i.e. M′_r ≡ M_{π(r)} (mod q) ∀r}.
Put Π₂ = Π_{q₂} and Π_odd = ⋂_{odd q‖D} Π_q. Compatibility is
Π₂ ∩ Π_odd ≠ ∅ for every fiber pair. Each Π_q is either empty
(excluded by the component lemmas G1/G2) or a left coset
Stab(M^{(q)}) ∘ π_q, Stab(M) = {δ : M_{δ(s)} = M_s ∀s}; so per odd q,
compatibility is the meeting of two cosets, while the full Π_odd
version additionally needs the odd q's to agree among themselves
(odd-odd compatibility, i.e. PC). Repository untouched, no Lean build.

## Verification: exhaustive, 0 counterexamples

Script `wave19_compat_2odd.py` (CRT enumeration via prime-power kernels,
as in wave 10; per-class multisets mod each q; π-sets as bitmasks):

| m | t | D | fiber pairs | BAD (empty Π₂ ∩ Π_odd) |
|---|---|---|---:|---:|
| 4 | 4 | 1152 | 949 | 0 |
| 6 | 2 | 39200 | 35 596 | 0 |
| 8 | 4 | 1331712 | 1 246 606 | 0 |
| total | | | 1 283 151 | 0 |

Non-vacuity: the π-sets are often singletons, and they never disagree:
m = 6 has 14 896 pairs with Π₂ and Π_odd both singletons, m = 8 has
248 400 such pairs — all agreeing. So compatibility is a real
constraint, not an artefact of full π-sets.

## Theorem: t = 2 proved except one subcase

Let m ≡ 2 (mod 4), u = m/2, E/O = even/odd positions. Then q₂ = 32 and
every Fix vector mod 32 is 2-periodic: y_i ≡ a (i even), b (i odd).
Let y′ = y ∘ σ for a permutation σ of positions.

- If a ≠ b (mod 32): the multisets mod 32, {a×u, b×u} = {a′×u, b′×u},
  force (a′, b′) = (a, b) or (b, a). The even-class multiset mod 32
  of y′ is {a′×u}, but also {a×|σ(E) ∩ E|, b×|σ(E) ∩ O|}; since
  a ≠ b, σ(E) = E (if a′ = a) or σ(E) = O (if a′ = b). Hence for
  EVERY q ‖ D, E′_q = E_q, O′_q = O_q (σ(E) = E) or E′_q = O_q,
  O′_q = E_q (σ(E) = O): the matching π (id or swap) lies in Π_q
  for all q at once. So for t = 2, a ≠ b, there is a common π
  across ALL components — full G3 at prime-power level. The only
  Fix input used is 2-periodicity mod 32.
- If a = b (mod 32): y and y′ are constant a mod 32, so
  Π₂ = D₂ is full, and compatibility ⟺ Π_odd ≠ ∅ ⟺ odd-odd
  compatibility (PC for m ≡ 2 mod 4). This is gap **G-2odd-1**,
  open in general. It is not rare: at m = 6 it is 492 fibers /
  4 404 pairs (12%, exactly the Π₂-full count), all passing
  numerically but unproved.

## t = 4: not proved, reduced to one gap

The σ argument fails for t = 4: the 2-component is P-periodic
(P = 2^{v₂(m)}), not class-constant, so the multiset
{y_j mod 2^a : j ∈ σ(O_r)} does not force σ(O_r)'s class profile.
Sufficient condition that would save it: if the pattern values p_s
are all distinct, the count equations force σ(O_r) = O_{π(r)} as
sets, hence π ∈ Π_q ∀q — but patterns repeat values in general.
The wave-11 joint counting also fails: the odd side is not
P-periodic, so there is no joint pattern on ℤ/P for σ to match
(the (2, odd) joint object would be (p_s, O_s) multisets over
mod-P fibers, which σ scrambles). A mod-3 partial forcing exists
(v = (a, b, −a, −b) is class-constant) but mod 3 has only two
nonzero values, so it distinguishes blocks, not classes — not enough.
Hence t = 4 is reduced to gap **G-2odd-2**, a joint block lemma
(JBL): the (2, odd) joint data yields Lemma-S-type block union
equalities, from which the wave-12 Lemma S combinatorics (pure D₄
given profile preservation, plus a pair lemma for odd profiles
analogous to PL) would give δ ∈ Stab and π ∈ Π₂ ∩ Π_odd.

## What remains

2-vs-odd compatibility: verified at m = 4, 6, 8; proved for t = 2
except the a = b subcase (G-2odd-1); open for t = 4 modulo JBL
(G-2odd-2). Closing both gaps would remove 2-vs-odd compatibility
from the exact per-class lemma's list, leaving G1 (f ≥ 3, f = 2
s = 0 hole), general PC, and joint CRT pairing inside classes.
