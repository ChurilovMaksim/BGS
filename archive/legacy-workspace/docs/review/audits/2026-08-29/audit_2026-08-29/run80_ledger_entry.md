
## RUN 80 (2026-08-29) — THE J-WEIGHTED AUTOMATON: PSI(Y) EVALUATED, WRAP
### COINCIDENCES DISCOVERED, SHAPE GROWTH TO R = 80

Triage: FRONTIER continuation.  Goal per the R79 handoff: the J-weighted DP
(the R77.1 generating function finally evaluated), then the E-residue and the
resolvent step.  Languages: chat RU, work product EN.  ENV: Python 3.14.0
(numpy/scipy/sympy/fractions), Julia 1.11.9 (C:/Tools), tectonic available;
A1-A3, A6 present; subagent infrastructure FAILED this session (3/3 spawns
died: concurrency limit, model-request failure, captcha gate) — all
verification was done inline in the main agent, i.e. the weaker form of the
adversarial-review ladder, flagged per the contract.

### R80.1 — The J-weighted relation automaton [PROVEN + certified end-to-end]

The R77.1 identity is now EVALUATED EXACTLY.  Each accepting walk of the
reversed-normalized automaton (R79) carries the letter weight
J_c(y) = I_c(2y)/I_0(2y) (internal zero gaps carry J_0 = 1), and

    Psi(y)  = sum_{accepting walks} prod_letters J_|c|(2y),
    WPsi(y) = sum_{accepting walks} width . prod_letters J_|c|(2y),

give, for every K <= Kmax and every r <= rmax simultaneously,

    X^Z_r(K)    = 2 r! [y^r] I_0(2y)^K ( (K+1) Psi - WPsi ),
    X_full_r(K) = 2 K r! [y^r] I_0(2y)^K Psi,
    wrap_r(K)   = X_full - X^Z,

with wc(c, r) = r! [y^r] prod_{j<K} I_|c_j|(2y) and
triv(r, K) = r! [y^{2s}] I_0(2y)^K (r = 2s; this exact form is what
reproduces triv(6, 17) = 538900 — the binom(2s,s)P(s,K) shorthand in
THEORY 13.2 is NOT the exact count and needs the caveat below).  The
identity I_0(2y)^K prod_letters J = prod_{j<K} I_|c_j|(2y) (the dense
K-window product, cancelled pairs included) makes the [y^r] reading exact.

Certification (`src/r80_jweight_dp.py`, exact Fractions, rmax = 12,
Kmax = 41; artifact `artifacts/r80/jweight_dp.json`):
  * X^Z / full / wrap at K = 17, r = 5, 6, 8 vs the r74-r77 census: EXACT
    (600/680/80, 5040/6120/1080, 4454240/5464480/1010240);
  * X^Z at r = 10, 12: EXACT (3107822760, 2093152388976) — the census
    Z-part is the clean-placement count, PADDED SHAPES INCLUDED;
  * S_win(R; 17), R = 5..12 vs R79: 8/8 EXACT (30, 28, 26, 76, 200, 624,
    1064, 1760);
  * triv(6, 17) = 538900 EXACT (the R77.4 table);
  * X_full_5(19) = 760, X_full_6(19) = 6840 EXACT.
Second implementation: Julia float64 (`src/r80_julia_bigdp.jl`), calibrated
against the exact rationals at r <= 12, K = 17: max relative deviation
2.2e-15 — two-method certified.

### R80.2 — WRAP COINCIDENCES: the Theorem-H parametrisation is not
### injective from r = 10 [PROVEN: mechanism + exact accounting]

X_full matches the census EXACTLY through r = 8 but EXCEEDS it at r = 10, 12.
Mechanism (`src/r80_wrap_collisions.py`, artifact
`artifacts/r80/wrap_collisions.json`): the map (sig, a, sign) -> collected
vector c = dense(a.sig mod K) of Theorem H has MULTI-VALUED fibres once
padded shapes exist.  A wrapping rotation of a shape can equal another shape
as a signed K-vector:

    Lemma (wrap coincidence).  If sig_A, sig_B are m_t-multiples and
    sig_A = +- x^a sig_B  (mod x^K - 1), then the difference is
    (x^K - 1) h with m_t | h — automatic, since gcd(m_t, x^K - 1) = 1
    over Q (the roots of m_t are the real units lambda > 1 and
    0 < lambda' < 1, not roots of unity) and Gauss's lemma lifts the Q[x]
    divisibility to Z[x].

First collisions appear at L1 = 10 (the padded double-m_t family
m_t(1 + x^d); concretely at K = 17: rot_14(m_t(1+x^3)) = m_t(1+x^14) as
vectors).  Exact collision excess sum_v (mult(v) - 1) wc(v) over signed
vectors v:

    r = 10:   41,126,400     (= X_full_formula - census, EXACT)
    r = 11: 1,244,073,600
    r = 12: 97,037,740,800   (= X_full_formula - census, EXACT)

both census deltas reproduced TO THE LAST DIGIT.  The signed-vector
accounting had two traps, both fixed and documented: (a) distinct sign
PATTERNS with the same |c_j| multiset are DISTINCT census vectors (wc is
sign-invariant, the census is not); (b) the DFS enumerator must RECORD zero
letters (gap variants are distinct shapes), otherwise 230 walks collapse to
114 pseudo-shapes — caught by a per-width cross-check against the position
DP (3/8/37/68/111 at L1 = 8..12, w <= 17, two methods).

Consequences:
  * The census (vector-level, r76/r77) is VINDICATED; the shape-rotation
    sum 2 sum_sig sum_a wc of THEORY 13.2 overcounts by the coincidence
    excess (0 through r = 8; as measured from r = 10).  The correct object
    is the set of DISTINCT collected vectors: D_r - triv - M_r =
    sum_{distinct vectors} wc.  M_r = 0 through r = 12 is unaffected.
  * The r <= 8 certification window of Theorem H was structurally blind to
    this (the first padded family starts at L1 = 10).
  * New exact values (K = 17, never censused): r = 7: X_Z 417060, full
    478380, wrap 61320; r = 9: X_Z 241053984, full 280158912 (collision-
    free, hence census-exact); r = 11: full 164997134940,
    census-corrected 163753061340.

### R80.3 — Ceiling tables extended [NUMERICALLY-SUPPORTED]

X_full/triv for K in {17, 19, 23, 25, 29, 31, 35, 37, 41}, r <= 12, exact
rationals; K = 17 column: 1.136 / 4.664 / 12.28 / 26.84 % at r = 6/8/10/12
(the r = 10, 12 entries multiplicity-inclusive; census-corrected: 12.15 %
and 25.89 %, matching R77.4).  At fixed r the excess follows the K^{1-s}
decay across the whole K range (artifact table).

### R80.4 — Shape growth S(R) to R = 80 [NUMERICALLY EXACT counts]

The count DP (exact Int128, Julia) gives, for the first time without a
width-census cap:
  * dense shapes (width <= L1): S(30) = 301160711, S(50) = 7.64e15,
    S(80) = 1.165e18; S(R)^(1/R) still rising: 2.0781 (R = 50), 2.1794
    (R = 80) — so C_dense > 2.18, while the universal signed-compositions
    bound gives C <= 3 [PROVEN, trivial].
  * width-capped at w <= 80: S(R)^(1/R) peaks at 2.2499 (R = 47-48) and
    turns DOWN — the C^R poly(R) signature, C approximately 2.25 for the
    fixed-width-80 language.
  * padding structure: at L1 = 10, 11, 12 the per-width family count is
    exactly 2, 4, 6 (linear in W - R); at larger L1 the padding mass grows
    much faster.
conj:Sgrowth is thereby upgraded from a wish to: all measured indicators of
a finite growth constant, 2.18 < C_dense <= 3, exact counts to R = 80.
Pinning the constant (Perron analysis of the co-reachable automaton core,
or a Frougny-Steiner transfer) is named op:Cdense.

### R80.5 — Audit of the standing results (Phase A) [11/11 REPRODUCED]

All core certification scripts re-run and green: catmap_independent
(Egorov/torsion/frame <= 6.1e-14), theoremB_covariance (Thm A ~1e-14),
theta_square_theorem (O6 closed), parity_desymmetrised (dichotomy),
theoremE_operator (beta = 1 theorem), lemmaF_quadratic_phase (5000/5000),
moment_certification, subgroup_kloosterman_energy, barrier_slack,
pstar_scan, and (after repair) verify_mean_law 5/5 OK.  ensemble_moments,
r75_multiples (all PASS), r78_eps_minus (3/3 exact vs r74), r79_automaton —
re-run green.  ONE defect found and fixed: verify_mean_law.py still carried
the stale portable-snapshot path (BGS_portable_20260827) in sys.path and in
its artifact target — the run-71 path repair missed it; repaired to
workspace-relative, re-run 5/5 OK.  Log trail:
review/audit_2026-08-29/logs/; the RUN 80 entry itself is preserved at
review/audit_2026-08-29/run80_ledger_entry.md.

### LESSONS (run 80)

* LESSON 80-A: a sign-symmetric statistic (wc depends on |c_j| only) must
  not tempt class-by-|c| accounting: the census counts SIGNED vectors, and
  distinct sign patterns with equal |c| are distinct classes.  The error
  inflated the collision excess by 83 percent before the fix.
* LESSON 80-B: an enumerator that does not record FREE letters (the zero
  gaps here) silently quotients its output space; the defect surfaced only
  as duplicate tuples under a set-level cross-check (230 walks vs 114
  pseudo-shapes) — LESSON 75-A met again in a new guise.
* LESSON 80-C: a certification window (Theorem H at r <= 8) can be
  structurally blind to a mechanism (padded shapes start at L1 = 10); the
  blind spot was exposed by EXTENDING the same certificate one order past
  the first untested family, not by re-running the old range.
* LESSON 80-D (process): bash heredocs with heavy mathematical punctuation
  truncate silently — append ledger entries via an intermediate file.

### RUN 80 HANDOFF

* State: the ensemble excess now has a COMPLETE exact generating function
  (Psi via the automaton), the Theorem-H parametrisation's coincidence
  structure is measured exactly at r <= 12, S(R) is known exactly to
  R = 80, and the R71-R79 certificate chain re-verified green.
* Next actions, by EV: (1) the E-residue at N = 3571 (verify the
  K^{-5} G_5 = 1.341e-07 prediction end-to-end — the R76 handoff item,
  still open); (2) Lean formalisation of the finiteness bound
  |sigma| <= remaining L1 (short induction; the prebuilt Mathlib host at
  C:/Users/churi/lean-projects/mephisto-lean is available); (3) the
  resolvent step (THE only missing ingredient for BGS in this family; the
  R73.4 reduction stands: a resolvent identity for P_lam via the Birkhoff
  reduction and the Lemma-F Gauss-sum coefficients); (4) op:Cdense — pin
  the shape-language growth constant; (5) paper integration of R80 (new
  section: the J-weighted generating function + wrap coincidences) and the
  THEORY 13.2 caveat.
* NOT tried this run: the r >= 14 census (conditional on M_r = 0, heavy);
  composite-K collision analysis (K prime assumed in the clean-placement
  injectivity); eps = -1 collision accounting; R >= 100 count DP (memory
  ceiling ~R^4 cells on the 8 GB box).
* Fragile points: the collision excess is computed for PRIME K = 17 only
  (composite K can have rotational symmetries with gcd(K, delta) > 1);
  the Julia float X_full at r >= 14 is MULTIPLICITY-INCLUSIVE (an upper
  bound on the census quantity, not equal to it).
