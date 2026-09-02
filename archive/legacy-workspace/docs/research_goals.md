# GOALS — the prize-track hierarchy for the BGS programme

Set 2026-09-02.  Standing directive: do not stop at the workshop-paper
level; drive the cat-map programme to the full conjecture and the
general theory it opens.

## THE GOAL (the prize-track statement)

**Prove the BGS conjecture for the quantised cat map family: the
eigenvalue statistics of every Hecke-sector observable converge to the
Wigner-Dyson GOE law with an explicit power-saving rate, uniformly in
the moment order — and extract the general mechanism (the
H-coupling/twist cancellation) in a form that applies to arithmetic
chaos beyond cat maps.**

Sub-goal G0 (the tower above the family): the same H-coupling
mechanism controls the *mixed* moments of arbitrary Hecke families —
this is the layer where the result stops being "a family" and becomes
"a theory".

## The four milestones (in dependency order, each has a killer test)

### M1 — δ_off = o(1): the Möbius-fiber theorem   [IN ATTACK]

The conic fiber of the difference map, written as a Möbius graph
v = (u(d−1)+1)/(d−u+1), turns the fiber twist sum into a sum of a
smooth (arithmetic progression) times a multiplicative twist along a
Möbius orbit — cancellable by Weil + summation by parts.

- Status: mechanism identified (RUN 96); **the killer test is M1-T**
  (RUN 101, this session).
- Numerical state: δ_off = +0.8% (N=53), +1.4% (N=199), < 1.5% total
  across the off-diagonal part.
- Deliverable: 10–20 pp note; closes Conjecture 93.2 (E_c ≤ C N³ K⁴).

### M2 — k ≥ 6 layers: the symmetric-power repetition

Each layer needs its own B(t)-table + δ_k estimate.  The template is
Theorem 92.3; the work is computational (heavier varieties) plus a
per-layer Weil range.  Killer test: δ_6 measurable < 5% at N=3571
(permutation-gather, ~40 min machine time).

### M3 — Smooth density + the local law assembly

ESY-type deterministic replacement (the moment bounds + Newtonian
iteration to the resolvent at Im z ≫ m^{-1+δ}).  Literature-standard
but must be adapted to *deterministic* arithmetic matrices.

### M4 — G0: the general mechanism

Extract the H-coupling cancellation as a statement about arbitrary
multiplicative-subgroup-constrained character sums (the BGKS/Katz
bridge).  This is the layer where the work connects to the open
literature frontier and becomes prize-track.

## Anti-goals (what does NOT count)

- Re-measuring the same calibrations with more decimal places.
- Numerical "verification" of things that have elementary proofs.
- Any claim of the full BGS for general chaotic systems.

## Rules of engagement (from the global contract)

- Every claim carries an artifact; every artifact reproduces.
- Killer test before write-up: no theorem is written from an untested
  mechanism.
- Retractions cascade immediately (R91-A precedent).
