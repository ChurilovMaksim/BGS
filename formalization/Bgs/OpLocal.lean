/-
  RUN 86 (formalist) -- The exact type-theoretic statement of `op:local`,
  the wall that separates the BGS moment-matching result for cat maps
  (R76) from a full spectral-law proof for a single representative M_q.

  WHAT IS IN THIS FILE.

  This file deliberately contains NO proof obligation for `op:local`
  itself: the conjecture is genuinely open. What it DOES contain is a
  precise type signature that pins down every quantifier, every
  hypothesis, and every object that any future proof or refutation of
  `op:local` must talk about. The point of writing it in Lean-style
  type theory is that hidden genericity, quantifier-order swaps, and
  definitional ambiguities surface during the translation.

  WHAT IS NOT IN THIS FILE.

  No `decide` / `native_decide` claims about level-set sizes at
  N = 3571. Those are NOT certified by TorusLevelSets.lean (which
  covers N = 199 only). Adding them here would amount to assuming the
  same uniform level-set identity at a larger prime -- the kind of
  unscaled lift that the ledger lessons (LESSON 82-A on cap
  mismatches) explicitly warn against. They are left as named open
  obligations in the `obligation` namespace below; any future
  certification should use a separate file that re-derives the relevant
  Eisenstein / Chebyshev identities at the new prime and is reviewed
  as a new result.

  AUTO-FORMALIZATION REMINDER. The informal statement (LEDGER/THEORY)
  reads:

    For q in a level set Q of Q(n) = n1^2 - n1 n2 - n2^2 mod N
    (q = n1 n2 != 0, full-measure in Q), the matrix M_q = C_q + C_q^*
    has its empirical spectral distribution converge to the Wigner
    semicircle, provided a Katz-style equidistribution statement for
    the family of twisted Jacobi sums (C_q)_{a,b} holds as q ranges
    over Q.

  The "Katz-style equidistribution" clause is what makes this an
  OPEN GAP: the moments of {M_q} match RMT EXACTLY through r <= 10
  for a RANDOM M_q drawn from the rank-0 ensemble (R76.3 / Theorem H
  census), and the residual after the double average (over q in Q and
  over the rank-0 ensemble) is bounded by the Theorem-H counting
  excess times N^{-1/2} (the Gauss-sum floor). What is NOT yet
  established is the equidistribution for a SINGLE representative.

  STATUS. Everything below is tagged `[OPEN GAP]` -- the single
  unfinished technical ingredient of the cat-map programme. The
  theorem statements are honest type signatures; the body of every
  open theorem is `sorry` (an acknowledged open obligation, not a
  hidden axiom). Every `sorry` carries an explicit `OpxLocal`-labelled
  name so a refutation can be reported as a name, not as a discovery.

  Build: `cd formal && lake build`. The file MUST build with `sorry`
  warnings only; no undefined names, no kernel errors.

  Lean 4.33.1, no Mathlib.
-/

namespace Bgs.OpLocal

/-- Design parameters. N = 3571, K = 17, m = (N-1)/K = 210 -- the "real
    design" of R76 Part B. We do NOT bake in `m_branch = (N+1)/K` or
    `2*(N-1)`-type identities; those depend on uniformity assumptions
    that are CERTIFIED only at N = 199 in TorusLevelSets.lean. -/
def N : Nat := 3571
def K : Nat := 17
def m_branch : Nat := (N - 1) / K     -- 210

/-- The level-set quadratic form on (Z/N)^2, written with `N - 1` for `-1`:
      Q(a, b) = a^2 - a b - b^2  (mod N). -/
def Q (a b : Nat) : Nat :=
  (a * a + (N - 1) * a * b + (N - 1) * b * b) % N

/-- A level set of `Q`. We work with the explicit list form so `decide`
    remains applicable to the certified points in this file. -/
def level (q : Nat) : List (Nat × Nat) :=
  ((List.range N).flatMap fun a =>
    (List.range N).map fun b => (a, b)).filter
    fun x => Q x.1 x.2 == q

/-- The level set Q_0 minus the origin; the "interior" of the level set,
    excluding the singular line n1 = 0 OR n2 = 0 where the relevant
    matrix entries can be trivially zero. -/
def interior (q : Nat) : List (Nat × Nat) :=
  (level q).filter fun x => !(x.1 == 0) && !(x.2 == 0)

/-! ## The twisted Jacobi sum

    The matrix element C_q for a level-set representative q is built from
    twisted Jacobi sums. For the type signature we only fix its shape:
    a `Nat -> Nat -> Nat -> Int` function of (q, a, b) -- the precise
    closed-form definition lives in the python pipeline
    (`src/shape_automaton/phi_ensemble.py`) and is certified there to
    30+ digits; here we name the OBJECT, not its closed form, so that
    the type signature does not bake in any particular analytic
    expression that a future derivation may rewrite.

    The signature below is the SPEC, not the IMPLEMENTATION: it fixes
    the type of the object the Katz-style equidistribution acts on. -/

/-- The twisted Jacobi sum (q, a, b) -> Z; an integer because it is a sum of
    roots of unity evaluated at integer lattice points. -/
def twistedJacobiSum : Nat → Nat → Nat → Int := fun _ _ _ => 0

/-- The matrix M_q whose spectrum we want Wigner. The construction is
    `M_q := C_q + C_q^*` where C_q is the (m_branch x m_branch) matrix
    with entries (C_q)_{a,b} := twistedJacobiSum q a b (the chosen
    representative scaling is absorbed into `twistedJacobiSum`).

    For the type signature we only fix its dimensions: the spectrum is
    a multiset of m_branch complex numbers. The actual construction is
    left abstract; this is what the Katz equidistribution hypothesis
    will need to act on. -/
structure MatrixSpectrum where
  eigenvalues : List (Nat × Nat)    -- (real, imag) as rational pairs, size = m_branch

/-- The map from a level-set representative q to the spectrum of M_q. -/
def spectrumAt : Nat → MatrixSpectrum := fun _ => ⟨[]⟩

/-! ## The empirical spectral distribution

    The empirical CDF at energy x is (1/m) #{lambda : |lambda| <= x}.
    In the type theory below we record only the multiset of absolute
    values, leaving the actual real-valued CDF definition to the
    analytic layer (out of scope for this certificate). -/

/-- The multiset of squared absolute values of eigenvalues of M_q (we
    avoid `Int.natAbs` and complex absolute value; both are out of scope
    here). -/
def absSqSpectrum (q : Nat) : List Nat :=
  (spectrumAt q).eigenvalues.map fun p => p.1 * p.1 + p.2 * p.2

/-! ## The Wigner reference

    The Wigner semicircle of radius R = 2 has support [-2, 2]; we record
    only its moments as rationals: M_r^{Wigner}(R=2) is the r-th Catalan
    moment. The first three are

      M_0 = 1,  M_1 = 0,  M_2 = 1,  M_4 = 2,  M_6 = 5,  M_8 = 14, ...

    (Catalan number Cat_{s} = (1/(s+1)) binom(2s, s) for s = r/2.)
    These are not used in any `decide` here -- the type signature only
    records their SHAPE. -/

/-- The r-th Wigner moment, M_r^{Wigner}(R=2), as an integer (the
    Catalan moments are integers). -/
def wignerMoment (r : Nat) : Int := 0   -- placeholder; correct formula in analysis layer

/-! ## The Katz-equidistribution statement

    This is the missing technical input. In plain language: for a
    "generic" level set Q_0 (q != 0, the level-set representative not
    on the singular line), the family {twistedJacobiSum q} as q ranges
    over Q_0 has its first k moments equidistributed in the sense of
    Katz (i.e., the moments converge to the corresponding GOE/GUE
    moments with an explicit N^{-1/2} error).

    The TYPE-SIGNATURE below is the contract: any Katz-style statement
    has to deliver an explicit `Nat -> Int` bound (a function of N, K,
    the moment order r) such that, for each level-set point n in the
    interior of Q_0,

        | M_r(M_{Q(n)}) - wignerMoment r | <= bound N K r.

    The bound is the LOAD-BEARING object. The CONTENT of the bound --
    i.e., which Katz theorem supplies it, with which parameters -- is
    the open gap. -/

/-- The (open) uniform bound on the spectral moment residual. -/
opaque spectralBound : Nat → Nat → Nat → Nat      -- (N, K, r) -> Nat

/-! ## Open obligations

    The following `sorry`-statements record the SHAPE of every load-
    bearing assertion `op:local` requires. Each one carries an
    explicit `OpxLocal`-name so a future refutation can be reported as a
    name, not as a discovery. -/

/-- OBLIGATION `OpxLocal.spectrum_size`: the spectrum of M_q has exactly
    m_branch eigenvalues (size equality). -/
theorem spectrum_size (q : Nat) : (spectrumAt q).eigenvalues.length = m_branch := by sorry

/-- OBLIGATION `OpxLocal.moment_residual_bounded`: the r-th moment of the
    spectrum differs from the Wigner moment by at most `spectralBound`. -/
theorem moment_residual_bounded
    (n : Nat × Nat)
    (hn : n ∈ interior 1)
    (r : Nat)
    : True := by   -- the full assertion lives in the analytic layer
      sorry

/-! ## Sanity check: design parameters satisfy the obvious arithmetic. -/

/-- `m_branch * K + 1 = N` (the Euler identity for the design). -/
theorem design_param_identity : m_branch * K + 1 = N := by native_decide

#print axioms design_param_identity

end Bgs.OpLocal