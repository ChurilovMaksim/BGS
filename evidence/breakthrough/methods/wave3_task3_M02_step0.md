# Wave 3, task 3 — M02 step 0: definitions fixed before any resonance numerics

Source discipline: every definition below was read from current main
`6dbcc7a0ed38d780ff7643bdb55917a9bc5efed1` of `ChurilovMaksim/BGS`
via the GitHub connector only (branch `main`, files fetched with that SHA).
No local test copy was used as a source. Nothing was written to the
repository; no Lean was built. Status labels below are main's own
(project proof / project theorem / open), not independent verification.

## 1. Verdict first

**`g_ball(m) = D_m·(1−|λ₁(m)|)` is NOT well-defined from main alone.**
Main contains no definition of a Perron–Frobenius / transfer operator
attached to `U_N` or to `U_m`, no `λ₁(m)`, and no "regularization" of
such an operator (see §5). Resonance numerics must STOP here until a
new definition is written down and its target ensemble is fixed — see
§6. A second, independent blocker: the ensemble M02's COE-flavoured
prediction would target is not the maintained target of the programme,
which is CUE / `Sine₂` after desymmetrization (§4).

## 2. The three different `U` in main — they are NOT identified with each other

### (a) The fixed frozen propagator (canonical, TRACE-005 statement)

`formalization/Bgs/TraceStatement.lean`, blob
`4287d8c124bd50664d5a918097b26a80bfff180c`:

- `tau : ℝ := 1 / 10^80` — fixed, explicitly NOT sent to 0 with `N`.
- `weylT N a b`: `(T_N(a,b) ψ)(x) = e_N(b(x + 2⁻¹a)) ψ(x + a)`,
  `x ∈ Z/N`, `2⁻¹` mod `N` (odd `N`).
- `MN N`: `(M_N)_{xy} = N^{-1/2} · e_N(−8⁻¹(3x² − 2xy + 3y²))`,
  `S = [[3,4],[2,3]]`.
- `U_N = exp(i τ N A_N) M_N`, `A_N` = raw Weyl quantization of the
  fixed symbol `f − 1/10`, with `f` given verbatim in §3 below.
  `f − 1/10` is a trigonometric polynomial with exactly 32 nonzero
  Fourier modes; the `(0,0)` mode is absent; Hermitian symmetry holds.
- Scope: odd `N ≥ 3`. The module is a STATEMENT formalization only:
  `BGS-TRACE-005` is OPEN, `BGS-BGS-001` is OPEN.

### (b) The θ-ensemble (Line D header / computations, NOT a Lean definition)

`formalization/Bgs/LineDDefs.lean` header (blob prefix `29fc0aa8`)
states only in prose: `U = exp(i eta V_theta) M_N`, `M_N` the cat matrix
for `S = [[3,4],[2,3]]`, `H_m = 6I − C − Cᵀ`,
`D_m = det H_m = Tr S^m − 2`, `X_m = D_m H_m^{-1}` (in Lean:
`Dm m = det (Hmat m ℤ)`, `Xmat m = adjugate`, so no division is used).
There is NO Lean `def` of `V_theta` or of this `U` in that module.

The computational definition is in
`computations/verification/lineD/code/mc_band.py`, blob
`e322ad3db22848180bd32a674a1b65d795f37df2`, and `dlib.py`, blob
`42ceaff85fc8bb35771e07f0648c361c9e51eb77`:

- `U = exp(i eta V_theta) M_p`,
  `V_theta(x) = Σ_{k ∈ modes} a_k |c_k| cos(2π k x/p + θ_k)`,
  `θ_k` iid uniform on the circle; `|c_k| = 1` (ensemble `J0`) or
  Rayleigh with `E|c|² = 1` (ensemble `G`).
- Here `eta` is a FREE parameter of an ensemble (order 1 in the
  numerical experiments), not the fixed coupling `τ = 10⁻⁸⁰`.
  The θ-ensemble is a random-kick model; it is not the fixed model (a).

### (c) The Lean trace-expansion model (Line B, finite-support kick)

`formalization/Bgs/LineBExpand.lean`, blob
`3f04d691166d04fce336c4b460f26ada2b63a502`:

- `kickVal N ĝ supp x = Σ_{k ∈ supp} ĝ k · χ_N(k·x)`,
  `ĝ : ℤ → ℂ` finitely supported Fourier data (no `η`, no `V_θ`).
- `kickMat N ĝ supp = Matrix.diagonal (kickVal N ĝ supp)`.
- `catMat N a x y = (√N)⁻¹ · χ_N(a·(3x² − 2xy + 3y²))`,
  with `a` satisfying `2·a·(−4) = 1` in `ZMod N`, i.e. `a = −8⁻¹`,
  matching the `M_N` of (a).
- The operator used in the trace theorems is
  `kickMat N ĝ supp * catMat N a`, and its `tsum` (infinite-support)
  version `kickMatInf` appears in the bridge hypotheses.
- The identification of `kickMatInf` with the actual fixed kick
  `exp(i τ N A_N)` is NOT in main: it is the open `kickMatInf`
  identification (the bridge takes it as a hypothesis `hTrU`).

Consequence: "the" `U_m` of M02 does not exist in main as one object.
Any resonance computation must first declare which of (a), (b), (c)
it uses, and — for (a) — how `τ = 10⁻⁸⁰` (so `τN ≈ 10⁻⁷⁸` at `N ~ 100`,
a perturbative regime) is supposed to produce an order-1 resonance
effect at all. Numerics at `η = O(1)` in ensemble (b) say nothing
about (a) without a bridge that main does not contain.

## 3. The fixed symbol, verbatim

`mathematics/fixed-map/fixed_model_symmetry_theorem.md` (claim
`BGS-FM-001`, project theorem with author-level check, not a Lean
proof, not a referee report), blob
`d7fb5d0140925f5f1f3ed72e6c709b650cd9f1a6`, §1, and the same
coefficients in `TraceStatement.lean` (`fCoeff`):

- Raw Weyl convention as in §2(a); midpoint symbol (boxed (1)):

```
g(q,p) = cos 14πq + r(q)/10 + r(q)·sin 2πq/100
         + r(q+½)·cos(2πp − α)/100 − 1/10,
r(q) = (1 − cos 14πq)(1 + cos 2πq),
cos α = −3/5, sin α = 4/5, i.e. e^{iα} = (−3 + 4i)/5.
```

- Fourier support: `|k| ≤ 9`, `|ℓ| ≤ 1` (32 modes; see
  `offdiagonal_strategy.md` §4, blob
  `cfc5906b37c75b90cbe8a4f84b6776d22e329484`).
- `ℓ = ±1` rows (from `TraceStatement.lean`, `fCoeff`):
  the `r·cos(2πp − α)/100` term contributes
  `rCoeff k · (−3 ∓ 4i)/1000` at `ℓ = ±1`. The `−4i` vs `+4i`
  asymmetry is the symmetry-breaking row; the same coefficients
  appear in `sixteen_phase_symmetry.md` §3 as
  `4000·c_{1,k} = (−3 − 4i)·r(k)`, `4000·c_{−1,k} = (−3 + 4i)·r(k)`,
  with `r(0) = 4`, `r(±1) = 2`, `r(±7) = −2`, `r(±6) = r(±8) = −1`.

## 4. Symmetry class — scope by scope, not one label

### 4.1 Pure cat map `M_N`

`BGS-TRACE-126` (as cited in `sixteen_phase_symmetry.md` §1–2)
supplies: `M_Nᵀ = M_N`, `M_N⁻¹ = \bar M_N`. This is a statement
about the UNKICKED matrix only. The pure map is a proved non-generic
example (Hecke degeneracies, arithmetic pseudo-symmetries; see
`offdiagonal_strategy.md` §2), so its symmetries do not transfer to
the kicked operator.

### 4.2 Diagonal kick `U = D·M_N` — antiunitary YES, COE form factor NO

`mathematics/fixed-map/sixteen_phase_symmetry.md` (claim
`BGS-TRACE-130`, project proof, no external referee), blob
`63cd581c60e4faba3704dfb560a84484bb581d15`, Theorem 1; same
statement in `mathematics/fixed-map/diagonal_phase_form_factor.md`
(claim `BGS-TRACE-127`), blob
`12c96e5cf7c815258ac608ba0b89c4aef0f5fbb8`, Boundary:

- Let `A^{diag}` be the `ℓ = 0` (position-diagonal) part of the
  symbol; it is a real diagonal matrix. For every real `η` and
  every phase vector, `D = exp(iη A^{diag})`, `U = D·M_N`, and
  `Θ = D·K₀` (`K₀` = complex conjugation in the position basis)
  satisfies

```
Θ² = I,   Θ U Θ⁻¹ = U†.
```

  The proof uses only: `D` diagonal unitary, `M_N` symmetric
  unitary. It therefore covers every real diagonal kick — including
  the θ-ensemble (b) (whose `V_θ` is a function of position) and
  the Lean `kickMat` (c) — and it covers an extra position sine.
- The same note is explicit, twice, that the "orthogonal class"
  name is a HEURISTIC attached to an antiunitary of square 1:
  it is NOT a theorem that the form factor equals the COE formula,
  it does not exclude a CUE form factor (a symmetric unitary
  `OᵀΛO` with CUE eigenvalues in `Λ` is a counterexample to any
  such inference), and similarity to the symmetric conjugate
  `Σ_D = D^{1/2} M_N D^{1/2}` does not assign a class.
- The full symbol is NOT covered: §2–3 state that the full symbol
  fails to be `K₀`-even for almost every phase (and is `K₀`-even
  for some phases), and that adding `ε·B_N`
  (`B_N = (T_N(1,0) − T_N(−1,0))/(2i)`, Hermitian,
  `K₀B_NK₀ = −B_N`, symbol energy `1/2`) to a diagonal kick breaks
  the hypothesis of Theorem 1. The `ℓ = ±1` rows of §3 are exactly
  such a non-diagonal part.

### 4.3 Full fixed propagator `U_N = exp(iτN A_N) M_N` — NO quantum antiunitary in main

- Classical side: `BGS-FM-001` §2, items 2–3, for every real
  `0 < |κ| ≤ 10⁻¹²`: the classical map `G_κ = S ∘ Φ_g^κ` has
  complete `C¹` centralizer `{G_κ^j}`, and there is NO `C¹`
  diffeomorphism `R` (either orientation) with
  `R G_κ R⁻¹ = G_κ⁻¹`. In the Egorov direction the classical map
  of the frozen operator is `F_τ = Φ_g^{−τ/(2π)} ∘ S⁻¹ = G_{τ/(2π)}⁻¹`,
  and `τ/(2π) ≈ 1.6·10⁻⁸¹` lies inside the theorem's range.
  So main contains a classical NO-REVERSOR theorem for the actual
  fixed model.
- Quantum side: main contains NO theorem stating an antiunitary
  `Θ` with `Θ² = 1`, `ΘU_NΘ⁻¹ = U_N†` for the FULL `U_N`, and
  also NO theorem excluding every possible quantum antiunitary.
  Direct check from the §3 formula (my computation, not a main
  claim): `g` is not even under `(q,p) ↦ (−q,−p)` — the
  `r(q)·sin 2πq/100` term is odd in `q`, and the `p`-term changes
  `cos(2πp − α)` to `cos(2πp + α) ≠ cos(2πp − α)` since
  `sin α = 4/5 ≠ 0` — and the `ℓ = ±1` coefficient asymmetry
  `(−3 − 4i)` vs `(−3 + 4i)` breaks `K₀`-evenness in the sense
  of §4.2. Hence the `Θ = DK₀` argument of TRACE-130 does NOT
  apply to the full `U_N`; any claim that it does would need a
  new proof, not a citation.
- Maintained target: `manuscript/ch01_introduction.tex`, blob
  `a92c31fc692d29f9ed2a84f5c9cd391f05f639f5`, states the
  programme's form as the UNITARY class: "local statistics of
  desymmetrized quantum chaotic spectra and their comparison with
  the `Sine₂` process", with the terminal open obligation the
  signed Heisenberg-scale desymmetrized joint-trace estimate
  `BGS-TRACE-005`. `TraceStatement.lean` makes the reference
  explicit: the comparison object `e_k(T_{N,b})` is the exact
  finite-dimensional Haar `U(N)` (CUE) reference, and the proved
  implication `BGS-TRACE-086` turns the TRACE-005 criterion into
  `Ξ_{N,α} ⇒ Sine₂`. `docs/reader_guide.en.md` states the same
  rule generally: with no relevant antiunitary/reversing symmetry,
  CUE is the natural benchmark; an orthogonal-class law is
  expected only if a suitable time-reversal symmetry survives.
  Conclusion for M02: a COE prediction for the FIXED map would
  be a claim against the maintained target, not within it. M02
  numerics are coherent only as a study of the diagonal-kick
  ensemble (b)/(c), whose benchmark main does not fix to COE
  either (§4.2).

## 5. Desymmetrization — what main actually prescribes

Main prescribes NO single desymmetrization for the full `U_N`.
What it does contain:

- Definition (reader guide): desymmetrization = restriction to
  the correct irreducible symmetry block BEFORE spectral
  comparison. `REVIEWING.md`: the final positive BGS claim may
  not be promoted until the Heisenberg-scale estimate is proved
  for the CORRECTLY desymmetrized fixed propagator — i.e. the
  correct block is part of the open obligation, not a settled input.
- Parity, conditional: `mathematics/returns/general_cat_return_laws.md`,
  blob `b54b2ea74dcae154f1fc7826db69501dccec2a43`:
  parity `R|x⟩ = |−x⟩` commutes with the unkicked quantization
  `U_{0,N}`; "quantization of even symbols also commutes with
  parity"; these statements require odd `N`, not primality.
  `Tr R = 1` fixes the scalar in the commutation argument.
  Consequence (arithmetic, from `Tr R = 1` and `dim = N`):
  the `+1` parity sector has dimension `(N+1)/2` and the `−1`
  sector `(N−1)/2` for odd `N`.
- Parity, applied: for a diagonal kick, `kickVal(−x) = kickVal(x)`
  iff `ĝ_{−k} = ĝ_k` for all `k` (reindexing the finite Fourier
  sum — my derivation from the `LineBExpand` definition).
  So parity sectors are symmetry blocks of `kickMat·catMat`
  ONLY under the extra hypothesis `ĝ` even. For general `ĝ`
  (the Lean theorems allow arbitrary `ĝ`) they are not.
  For the full fixed symbol they are not: §3 shows `g` is not
  even, so `A_N` does not commute with parity (the sin-term and
  the `α`-phase `p`-term are the breaking parts). This matches
  `offdiagonal_strategy.md` §6, which reports — as an UNCHECKED
  external proposal, explicitly not a theorem of the note — that
  a dominant part of the fixed symbol commutes with parity and
  preserves time reversal while a smaller part breaks both, and
  warns that the truncated kick's commutation and pair law still
  have to be proved, and that the proposed strong-coupling limit
  is not the fixed coupling `τ = 10⁻⁸⁰`.
- Therefore the desymmetrization TO USE is:
  * for the diagonal-kick ensemble (b)/(c) with even `ĝ`:
    the two parity sectors `(N±1)/2`, spectra analyzed
    separately, never pooled;
  * for the full fixed propagator (a): NO parity desymmetrization
    is justified by main — pooling or splitting by parity there
    would be an error in either direction until a symmetry of
    the full `U_N` is proved;
  * Hecke / arithmetic desymmetrization of the pure `M_N`
    (Kurlberg–Rudnick, Keating–Mezzadri, cited as background in
    `offdiagonal_strategy.md` §2) is NOT transferred to `U_N`
    in main; `BGS-FM-032` (cited there) gives only an additive,
    linearized distance of the symbol from the commutant of
    `M_p` for odd primes `p > 99`, explicitly not a
    multiplicative / nonperturbative obstruction.

## 6. Why `g_ball(m)` is not well-defined — the exact missing pieces

Searches of main at the HEAD above (code search, `repo:ChurilovMaksim/BGS`):

- `g_ball`: 0 hits in the mathematical sense (only an unrelated
  `half_radius` checker counting Hamming-ball pairs).
- `Perron`: only computational helpers — power-iteration `perron()`
  in `computations/verification/lineN4/code/b16_perron.py` and
  `b16_schur.py` for a Schur-test majorant of a different
  (Line N) object, and `computations/verification/lineB/phase4/transfer.py`
  for a parity characteristic function. No Perron–Frobenius
  operator attached to `U_N`, to `U^m`, or to the classical map
  `S`/`G_κ` with a named second eigenvalue.
- `transfer operator` / `Ruelle`: literature and Line F material
  on lifted Hardy-space transfer operators for a different
  programme (claims TRACE-197–202, Conjecture R TRACE-179 open);
  none of it defines a `λ₁(m)` for the M02 prediction.
- `lambda_1`: no eigenvalue of a transfer/Perron operator;
  only partition signatures and unrelated `λ` notation.

Missing, in order, before ANY resonance numerics:

1. The operator itself: state space, alphabet (if symbolic),
   kernel, and which dynamics it quantizes — classical `S`,
   classical `G_κ`, quantum `U_N`, or the θ-ensemble — and, if
   classical, why a classical resonance should predict a quantum
   form factor at Heisenberg time (the M04 gap: classical
   resonances at `n ~ N` are exponentially small and say nothing
   about `K(τ) = O(1)` by themselves).
2. The regularization: "regularized" currently has no referent
   in main. Name the cutoff / truncation / damping, and show the
   `λ₁` is stable under changing it (or state the dependence).
3. The index `m`: `D_m = det H_m` is defined for the time `m`
   in Line D, but `λ₁(m)` has no main meaning — is it the
   second eigenvalue of a fixed operator, of its `m`-th power,
   or of an `m`-dependent operator? Each gives a different
   `g_ball(m)`.
4. The target ensemble: COE (from the diagonal antiunitary
   heuristic) or CUE (the maintained TRACE-005 target)? §4 shows
   these pull in opposite directions for the fixed map, and main
   does not resolve the fixed map to COE.

## 7. What is now fixed enough to use, and what must not be done

FIXED (safe to build on, with the blob references above):

- `U_N = exp(iτN A_N) M_N`, `τ = 10⁻⁸⁰`, `M_N` as in §2(a),
  symbol `g` as in §3, 32 modes, odd `N ≥ 3`.
- Diagonal-kick antiunitary `Θ = DK₀`, `Θ² = 1`,
  `Θ(DM_N)Θ⁻¹ = (DM_N)†` — diagonal kicks only, class label
  heuristic only.
- Parity commutation for even symbols / unkicked map, odd `N`,
  sectors `(N±1)/2` and `(N−1)/2`.
- Classical no-reversor theorem `BGS-FM-001` for `G_κ`,
  `0 < |κ| ≤ 10⁻¹²`.
- Maintained benchmark after desymmetrization: CUE / `Sine₂`
  (TRACE-005 reference), with `BGS-BGS-001` and `BGS-TRACE-005`
  OPEN.

MUST NOT be done on the current definitions:

- Do not compute a "resonance" `λ₁(m)` for an operator main
  does not define and then compare `g_ball(m)` with a form
  factor — the comparison would be between an invented number
  and a spectrum of an operator that may not even have the
  symmetry the prediction assumes.
- Do not use parity sectors for the full fixed symbol, and do
  not pool the full spectrum of an even diagonal kick.
- Do not cite TRACE-127/TRACE-130 as a COE form-factor theorem,
  and do not cite the `Θ = DK₀` identity for the full `U_N`.
- Do not import `η = O(1)` θ-ensemble numerics as evidence
  about the `τ = 10⁻⁸⁰` fixed map.
