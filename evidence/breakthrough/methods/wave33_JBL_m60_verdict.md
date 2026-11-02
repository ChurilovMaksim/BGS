# Wave 33, task 1 — JBL verdict at m=60: pair NOT D-related, JBL itself survives

## Verdict (read carefully: two claims, opposite outcomes)

The m=60 COH counterexample pair (A, A') is **not D-related** — not in
the bare dihedral sense, and not up to Ann + Shadow (the R\*\* sense).
But this refutes **parameter recovery / R\*\* in general, not JBL**:
JBL's actual conclusion (wave 20, Joint Lemma) **holds** for this pair,
with π(r) = −r+1 at every odd q. The task's framing ("JBL says: same
joint multiset ⇒ D-related parameters") is the R\*\* claim, not JBL's
claim — exactly the conflation wave 25 §5 warned against: pairs with
identical signatures kill parameter recovery, never JBL's conclusion,
which is about signatures, not parameters. Repository untouched; no
Lean built.

## The pair (exact)

Per-component pairs from wave32_COH_m60.md (rest (0,0)); CRT gives the
global pair mod D_60 = 8572001542975368419584080488440354732051920000:

- A  = (5390753508340721110415603828336227705098720000,
        5810148959856486038839138520222063096365845000)
- A' = (3464217808025549925206050385227158080975940000,
        3833352775990803433192952029273335977192565000)

Hypothesis verified globally (exact): S'_i = S_{σ(i)} for σ(i) = 11i+9,
so the sorted global multisets are equal; all 13 component pairs are
genuine (wave-32 conventions).

## (D) Not D-related: the exact obstruction

For c ∈ {id, conj}, per-component residue sets {j mod ord_q :
A'_q − c(A_q)·α^j ∈ E_q} (E_128 = Ann(128), E_81/E_625 = validated
Shadow, E_q = {0} elsewhere; Ann_60(128) recomputed exactly, 16
elements: x ∈ {0,64}, y ∈ 16·Z/128):

- c = id: **impossible already at q = 49** (no j at all).
- c = conj: j exists at every component, but **no common j**.
  Clean two-line obstruction: at q = 81 the working residues mod 108
  are all **odd** (3, 7, 11, …, 107), while at q = 841 the working
  residues mod 290 are all **even** (0, 10, 20, …, 280); gcd(108, 290)
  = 2, so no j is both. (Full sets: 49: 7/21, 81: 27/108, 121: 11/132,
  128: 32/64, 841: 29/290, 1681: 41/205; zero components: all residues.)
- Bare orbit (no Ann/Shadow): c = id dead at q = 49, c = conj dead at
  q = 128. So neither the bare nor the R\*\* relation holds.

## Sharpening: a clean counterexample to R\*\* in general

Transport (wave 25) makes the pair π = id signature-equal: with
A\* = conj(A)·α³, the signatures J(A\*) and J(A') are **identical**
(J^{(q)}_r(A\*) = J^{(q)}_r(A') for all r, q — verified). Yet (A\*, A')
has no R\*\* relation either (R\*\*-relatedness is dihedral-invariant:
Ann and Shadow are invariant under α and conjugation). So R\*\* as a
general lemma is **false**: identical signatures (π = id) do not imply
A' = c(A)α^j + z + w. (At q = 128 the pair differs by (0,96) ∈ Ann;
at q = 841, 1681 the difference is visible and unabsorbable.)
R\*\* remains verified at m = 12, 8 and (128, 243) only.

## (C) JBL's actual conclusion holds: the mechanism

Wave 20's JBL asks for one π ∈ D_4 with J′^{(q)}_r = J^{(q)}_{π(r)}
for all r and all odd q, where J^{(q)}_r is the multiset of
(y_i mod 128, y_i mod q) for i ≡ r (mod 4) — the mod-128 window is
4-periodic, so this is exactly wave 20's (p_{i mod P}, y_i mod q)
with P = t = 4. Checked over all 8 π ∈ D_4: **exactly one works,
π(r) = −r+1**, at every odd q.

Why JBL survives while COH fails: COH is **position-level** — it
demands a dihedral τ on the full 60-window (120 maps i ↦ ±i + c)
matching σ. JBL is **class-level** — it only asks for the class
permutation π. Now σ(i) = 11i+9 satisfies σ(i) ≡ 3i+1 (mod 4), and σ
is bijective, so σ maps class r **onto** class −r+1; joint multisets
forget within-class positions, which is exactly the information COH's
τ-matching remembers. σ is dihedral at the class level but a
multiplier map at the position level — so JBL holds and COH fails
for the same pair, with no contradiction.

## Consequences

- The R\*\*+COH route to JBL was already dead (wave 32); now the
  R\*\* lemma itself is dead in general. JBL needs a route that does
  not go through parameter recovery: direct π-compatibility plus
  transport (wave 25 §5's second option), with π supplied by the
  class-level argument, not by a parameter relation.
- JBL itself is **not** refuted by this pair; a JBL counterexample
  would need a pair sharing the joint global multiset with **no**
  π ∈ D_t matching the per-class joint multisets.

## Files

- This note: `methods/wave33_JBL_m60_verdict.md`
- `methods/wave33_JBL_m60_verdict.py` (main check: CRT, class-level
  π-scan, per-component residues + CRT merge)
- `methods/wave33_JBL_m60_verdict_check2.py` (independent follow-up:
  4-periodicity, π = id transport, pairwise q = 81/q = 841 obstruction)
