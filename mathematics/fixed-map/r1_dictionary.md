# R1 dictionary: external §16 phase model ↔ repo fixed-map model

**Status: DRAFT, staging only. Not landed, no claim registered, no repo file
modified, no claim status changed. TRACE-005 and BGS-001 stay OPEN
regardless of this dictionary: it is a reduction step, not a proof of the
local law, the phase model's own Sine₂ law, the uniform-in-word-length
oscillatory estimate at m ≍ N, or the negative coherent correction −δ*.**

**STATUS UPDATE 2026-10-25 (parent-verified, landing version): R-P3 has been
performed and PROVED** — grouped expansion of (9.3) to order h³ equals the
§3.3 predicted 𝒜₃ in all 14 monomials (hand derivation + sympy route A,
diff identically 0; numeric route B agrees to 2.9×10⁻⁶ relative; parent
re-ran rp3_check.py, exit 0). Consequently literal-model (16.15) at R = 3
depends only on the pre-existing R-L6, like (16.10) and (16.15) at R ≤ 2;
R ≥ 4 remains conditional on P_j = 𝒜_j, j ≥ 4. The §3.3 addendum below
records the check; the original CONJECTURAL text is preserved above it
for provenance, and §4/§5 must be read subject to this update. Base note
`phase_model_transfer.md` verified unchanged at live main at landing time
(blob ede5192a, same as the 4b3a577 snapshot copy used here).

## 0. Sources and versions

- External document: `~/workspace/user/files/BGS_exact_obstructions_2026-10-22-1_0_2yte.md`,
  §16 (checkpoint: version 2, SHA-256
  `d8a92e6895c5c4c20b0e885515515a7c96de85dfceeba17f5b5c837d276b3d3257c`
  as printed at the head of §16) with §9 as its stated input (§§9.1–9.4 for
  phases, symbol, transport, gluing) and §1 for the base definitions.
- Landed re-base note: `mathematics/fixed-map/phase_model_transfer.md`
  (commit f7c8f0d), read from the 4b3a577 snapshot copy
  (`~/workspace/bgs_rework_exec/bgs_live_4b3a577/tree/`). The task states
  this file is untouched by the pass-2 files, so the 4b3a577 copy is current
  for it; the parent should re-confirm against live main before landing
  (this subagent has no live-browser access).
- Repo model: `mathematics/fixed-map/fixed_map_path_model.md` (ordinary
  symbol), `four_branch_parametrix.md` §§1–2 (two-amplitude parametrix),
  `factorial_wkb_reduction.md` §6 (general fixed order, BGS-TRACE-017),
  `position_chain_mixing.md` (BGS-FM-021, printed statement only — see §1.4).
- Prior verification: `~/workspace/bgs_rework_exec/trace005_external_verify/`
  (VERIFICATION_REPORT.md: §16 verdict PARTIAL/conditional on §9; U1–U16
  gap list) and `~/workspace/bgs_rework_exec/trace005_rebase16/`
  (REBASE_REPORT.md, streams B/C: R1 stated as "finite dictionary work, not
  new analysis", R2 = Lemma 6 degeneracy handling, minor).
- Repo house rules honoured: no convention is silently changed. In
  particular the repo's convention (AGENTS.md) that frequencies evolve by
  A is kept, and the transport-sign difference below is recorded as a
  notation difference, not resolved by redefining either side.

Status key used in §2: EXACT = same object, possibly renamed, with the
evidence cited; RENAMED = same object, different symbol only; CONSTRUCTED =
built in the landed note from repo objects by an elementary step;
IMPORTED = defined in §16 itself, no repo counterpart needed;
COMPATIBLE = statements differ in inessential constants but agree where
used; CONJECTURAL = match claimed with a stated falsifiable test, not yet
performed; MISSING = no counterpart (see §5).

## 1. The symbol identification (the step everything else hangs on)

### 1.1 Three symbol objects — do not conflate them

| Object | Formula | Home |
|---|---|---|
| §1 `f` (Weyl-side symbol) | `cos14πq + r(q)/10 + r(q)sin2πq/100 + r(q)cos(2πp−α₀)/100`, `r(q)=(1−cos14πq)(1+cos2πq)`, `e^{iα₀}=(−3+4i)/5` | External §1 |
| §9 `a` (ordinary symbol) | `a(q,p)=V(q)+g(q)cos(2πp−α₀)`, `V(q)=cos14πq+r(q)/10+r(q)sin2πq/100−1/10`, `g(q)=r(q+1/2)/100` | External §9.1 |
| Repo `g` (ordinary symbol) | `g(q,p)=cos14πq+r(q)/10+r(q)sin2πq/100+r(q+1/2)cos(2πp−α)/100−1/10`, `cosα=−3/5, sinα=4/5` | `fixed_map_path_model.md` ll.16–21 |

**Identification (EXACT): repo-`g` = §9-`a`, and α = α₀.**
Evidence: the two formulas are term-by-term identical once
`cosα₀=−3/5, sinα₀=4/5` (external §1) is compared with repo's
`cosα=−3/5, sinα=4/5`. The only naming clash in the whole dictionary is
here: §9's `g` is the *kick part only* (`r(q+1/2)/100`), while repo's `g`
is the *full symbol*. Everywhere below, "§9-g" means the kick part and
"repo-g" means the full symbol; §9-`a` = repo-`g`.

§1-`f` differs from §9-`a` by the half-shift `r(q)` vs `r(q+1/2)` in the
cos-coefficient. That shift is exactly the raw-quantizer half-shift, not
a different model: see §1.2. The dictionary identifies repo-`g` with
§9-`a`, never with §1-`f`.

### 1.2 The operator A_N is literally the same on both sides (EXACT)

Repo action (`four_branch_parametrix.md` §2, from `fixed_map_path_model.md`):
`A_N u(x) = Σ_{k,l} c_{kl} e(k(x+hl/2)) u(x+hl)`, `l ∈ {−1,0,1}`,
where `c_{kl}` are the Fourier coefficients of repo-`g`.
§9 action (9.3):
`(A_Nψ)(q) = V(q)ψ(q) + ½g(q+h/2)e^{−iα₀}ψ(q+h) + ½g(q−h/2)e^{iα₀}ψ(q−h)`.

Check by Fourier reconstruction. Write repo-`g = V + (r(q+1/2)/100)cosϑ`,
`ϑ=2πp−α₀`, so the `l=1` coefficient function is
`(r(q+1/2)/100)·e^{−iα₀}/2` and the `l=−1` one is
`(r(q+1/2)/100)·e^{+iα₀}/2`. Summing `Σ_k c_{k,1} e(k(x+h/2))` reconstructs
the `l=1` coefficient function at `q=x+h/2`, i.e.
`½g(q+h/2)e^{−iα₀}` with §9-g, and similarly for `l=−1`; the `l=0` sum
reconstructs `V(q)`. Hence (9.3) is the repo action, grouped into three
terms. §9.1's remark that (9.3) "takes into account the sign of the usual
Weyl rule" and repo §2's "no replacement of the raw quantizer" describe
the same half-shift from opposite sides; neither side redefines the
operator. This grouped-vs-raw presentation difference is the only
presentation gap in the P₂/P₃ matching (§3), and §3 closes it at order 2.

### 1.3 Hamilton–Jacobi, characteristics, transport sign (EXACT)

- HJ: §9 (9.6) `∂_tS_ν = a(q,∂_qS_ν)/(2π)`; repo §2 `S_{r,t} =
  g(x,S_{r,x})/(2π)`. Identical under §1.1.
- Characteristics: §9.3 `Q̇=−a_p/(2π), Ṗ=a_q/(2π)`; repo §2 "the classical
  characteristics are the Hamilton flow of −g/(2π)". Identical; repo's
  remark that "no orientation is inferred from the usual opposite-sign
  Schrödinger convention" is consistent with §9's sign, not opposed to it.
- Transport: §9 (9.7) `(∂_t+ℒ₁)b_ν=0`, `ℒ₁=v∂_q+½∂_qv`,
  `v=g sinϑ`; repo `(∂_t−D₁)a_0=0`, `D₁a=(g_p/2π)a_x+(g_xp+g_ppS_xx)a/(4π)`
  (partial derivatives at fixed p). **D₁ = −ℒ₁ exactly**: for
  §9-`a`, `g_p=−2πv`, so `g_p/(2π)=−v`; and
  `(g_xp+g_ppZ)/(4π) = −½(g′sinϑ+2πgZcosϑ) = −½∂_qv`.
  Hence repo's `(∂_t−D₁)` is §9's `(∂_t+ℒ₁)`; the sign difference is
  notation (repo absorbs the minus into D₁), not mathematics. The same
  computation gives `P₁ = 𝒜₁ = iℒ₁` (see §3.1).

### 1.4 Which repo statement supplies what (do not cite FM-021 §2 alone)

FM-021's printed statement (`position_chain_mixing.md` §2) gives only the
leading amplitude with an `O(h^{3/2})` entrywise remainder; its
`O(N^{−1/2})` operator error fed into §16 Lemma 6 gives `O(N^{1/2})` —
no transfer. The transfer consumes the dependency chain, exactly as the
landed note does: `four_branch_parametrix.md` §2 (two amplitudes,
entrywise `O(h^{5/2})`, operator `O(h^{3/2})`) for Theorem A, and
`factorial_wkb_reduction.md` §6 eq. (18) (`‖U_N−V_{(N,J)}‖ ≤ C_J h^{J+1/2}`)
for Theorem B. Any citation of this dictionary for the literal §16 model
must cite the chain, not FM-021 §2.

## 2. Line-by-line dictionary

`§16 object → repo counterpart (status; evidence)`.

- `N` odd ≥ 3; `h=1/N` → same (EXACT; external §1, repo §2).
- `τ=10⁻⁸⁰` fixed; propagator time `t`, evaluated at `t=τ` (§16.3) →
  same (EXACT; repo `U_N(t)=exp(itNA_N)M_N`, `four_branch_parametrix.md`
  §2; external §1: "τ remains strictly fixed").
- `M_N` → same (EXACT; external §1
  `(M_N)_{xy}=N^{−1/2}e_N(−8̄(3x²−2xy+3y²))` and §9 (9.5) are connected by
  the Gauss identity, which repo §1 proves rigorously by completing the
  square mod 8 — this discharges §9-side U-gap 5 for the transfer, see §4).
- `A_N` → same (EXACT; §1.2 above).
- `U_N(t)=exp(itNA_N)M_N`; `U_N=U_N(τ)` → same (EXACT; repo §2 scope line
  `U_N(t)=exp(itNA_N)M_N`; §16.2 uses `∂_tF=iNA_NF` and Duhamel with
  `exp(itNA_N)`).
- `S_ν(t,q,z)`, `ν=0..3` → `S_r(t,x,y)`, `r=0..3` (EXACT, RENAMED; identical
  initial data `S_ν⁰(q,z)=−(3q²−2q(z+ν)+3(z+ν)²)/8` in §9.2 and repo §1;
  identical HJ equation by §1.3).
- `P=∂_qS_ν` → `S_x` (EXACT, RENAMED).
- `Z=∂_qqS_ν` → `S_xx` (EXACT, RENAMED). `∂_qZ` → `S_xxx` (EXACT, RENAMED).
  (Higher derivatives `∂_qqZ=S_xxxx` appear only in the P₃ formula, §3.3.)
- `ϑ=2πP−α₀` → `2πS_x−α`, no repo symbol (EXACT, RENAMED; α=α₀ by §1.1).
- `v=g sinϑ` (§9-g) → `−g_p/(2π)` with repo-g (EXACT, derived in §1.3).
- `ℒ₁=v∂_q+½∂_qv` → `−D₁` (EXACT; §1.3 computation).
- `b_{0,ν}=b_ν` (§9) → `a_{r,0}` (EXACT; both solve the same transport
  equation with initial value 1: §9 (9.7) vs repo `(∂_t−D₁)a_0=0`,
  `a_0(0)=1`).
- `b_{1,ν}` → `a_{r,1}` (EXACT; §16 (16.5) `(∂_t+ℒ₁)b_1=i𝒜₂b_0`,
  `b_1(0)=0`, vs repo `(∂_t−D₁)a_1=D₂a_0`, `a_1(0)=0`, given `D₂=i𝒜₂`
  from §3.2).
- `b_{r,ν}`, `r≥2` → `a_{r,j}`, `j≥2` (EXACT for `r=2` via §3.2;
  CONJECTURAL for `r≥3`, see §3.3 and §5: the identification
  `P_j=𝒜_j` is proved for `j≤2` and computed-but-unconfirmed for `j=3`,
  uncomputed for `j≥4`).
- `𝒜_j` (§16.4: "finite differential operators obtained by ordinary
  expansion of two shifts in (9.3)") → repo `P_j` (EXACT for `j≤2`,
  CONJECTURAL for `j=3` with explicit formula in §3.3, MISSING as a
  displayed formula for `j≥4` on both sides — repo defines `P_j`
  abstractly for all fixed `j`, §16 never displays `𝒜_j` for `j≥3`).
- Gluing identities (9.10) → repo §2 identities (EXACT; §9:
  `S_{ν+4}⁰=S_ν⁰+q−3z−3ν−6`, `S_ν⁰(q+1,z)=S_{ν−3}⁰(q,z)−2(z+ν)+3`;
  repo: `S_{r+4}−S_r=x−3y−3r−6`, `S_r(t,x+1,y)−S_{r−3}=−2r−2y+3`
  — the same formulas, since `−2(z+ν)+3=−2r−2y+3` under `ν=r, z=y`;
  plus repo's `S_r(t,x,y+1)=S_{r+1}(t,x,y)`, which also follows from
  §9's initial data by the same uniqueness argument. Repo §2 proves
  preservation by uniqueness; this discharges §9-side U-gap 4 for the
  transfer, see §4. Individual branches need not be periodic on either
  side — only the four-branch sum is lattice-periodic.)
- `F_N^{(1)}(t)`, (16.6) → repo two-amplitude approximant `V_{jk}(t)`
  (EXACT up to the landed note's renaming: §16's prefactor
  `e^{2πi3N/8}/(2√N)` is repo's `e(3N/8)√h/2` with `e(z)=exp(2πiz)`,
  `h=1/N`; §16's `b_0+N^{−1}b_1` is repo's `a_{r,0}+ha_{r,1}`; the
  initial identity `F_N^{(1)}(0)=M_N` is repo's `V_N(0)=M_N`).
  NOTE on names: repo notes call the approximant itself `V_N`; the
  landed note renames it `F_N^{(J)}` and reserves `V_N^{(J)}` for its
  polar unitarisation. This dictionary follows the landed note.
- `F_N^{(R)}(t)`, general `R` → repo `V_{(N,J)}(t)`, `J=R`
  (EXACT for the approximant; the amplitude identification is CONJECTURAL
  for orders ≥3 as above).
- `V_N^{(R)}=F(F*F)^{−1/2}` (§16.3, (16.8)) → no named repo counterpart;
  CONSTRUCTED in the landed note from the repo approximant (elementary:
  `δ=‖F−U_N‖<1` puts singular values in `[1−δ,1+δ]`, so
  `‖F−V‖≤δ`, `‖U_N−V‖≤2δ`, §16 (16.9)). Repo's
  `polar_wkb_quantization_stability.md` §3 is a neighbouring stability
  discussion, not the construction; the landed note does not cite it for
  this step and neither does this dictionary.
- Remainder `‖U_N−F_N^{(1)}‖=O(N^{−3/2})`, (16.7) → repo operator bound
  `O(h^{3/2})` (EXACT; repo §2: entrywise `O(h^{5/2})` + `‖R‖_op ≤
  N·max|R_jk|`; §16's per-entry `O(N^{−5/2})`, per-column `O(N^{−2})`,
  Hilbert–Schmidt `O(N^{−3/2})` route gives the same operator order).
  This replaces §9.4's remainder, so §9-side U-gap 1 (amplitude-derivative
  bounds and `C_rem` for §9.4's `O(N^{−3/2})` per-entry remainder) is
  BYPASSED for the transfer, not closed (see §4).
- Remainder `‖U_N−V_N^{(R)}‖=O_R(N^{−R−1/2})`, (16.12) → TRACE-017 §6
  eq. (18) (EXACT; same exponent, same quantifier order: `R` fixed first,
  then `N` large depending on `R`).
- Lemma 6 (16.1), eigenangle matching (16.2) → IMPORTED from §16 (no repo
  counterpart; model-independent perturbation theory). Residual condition
  R-L6 (§4): the degeneracy handling is compressed in §16.1 ("locally
  choosing a cut outside the finite spectrum and continuing branches
  through multiplicities"); it is standard material but it is not
  re-proved in the repo and not independently checked in the verification
  package. Minor, but it is a genuine residual condition on the literal
  transfer, not a proved step.
- `f≥0 ∈ C_c¹`, `f_N(t)=Σ_ℓ f(N(t+ℓ))`, `L_N(f)` with a single common
  shift → IMPORTED from §16 (no repo counterpart; the landed note's
  definition of `L_N(f)` is §16's). Do NOT identify with TRACE-017's
  bridge statistic `F_{k,N}` (see next entry).
- `b` (Schwartz, ≥0, sup<1), `b_N`, `M_{k,N}(b)` (16.13),
  `Δ_{k,N}(b)`, reference `e_k(T_{N,b})` → IMPORTED from §16 (definitions
  live in §16.4; the reference `e_k` is the same for both matrices and
  cancels in the difference (16.15), so no repo counterpart is needed).
  TRACE-017's `F_{k,N}(U;W)` / `F_{k,N}^•(V;W)` and eq. (R)/(14)/(16) are a
  NEIGHBOURING transfer for a different (trace-transform) statistic:
  related by the same `N^k·δ` counting, corroborating, but NOT the same
  object as `Δ_{k,N}` — the two must not be identified. In particular
  TRACE-017 eq. (14)'s `O(N^kδ)` and §16 (16.15)'s `O(N^{k−R−1/2})` agree
  in exponent because both count `N^k` tuples against an
  `N^{−R−1/2}` operator error; that agreement is corroboration, not a
  second proof of (16.15).
- Time interval `|t|≤T` (§9.3: `T=10⁻³⁰`) vs repo §2 ("sufficiently small
  fixed time interval") and §4 (`T=10⁻²⁰`) → COMPATIBLE: both intervals
  contain the only used point `τ=10⁻⁸⁰`; no statement in §16 or the repo
  uses any other `t`, and no uniformity in `t` is claimed. The differing
  `T` values are not a mismatch.
- Startup thresholds `N₀` (FM-021, noneffective), `N₁/N₂` (§9, uncomputed)
  → COMPATIBLE: both sides are noneffective; §16's transfer inherits
  "for large odd N" from the repo side, and no effective threshold is
  claimed by either side.
- `k=2` trace-form pair-sum telescoping check (§16.4, end) → IMPORTED
  elementary check inside §16 (uses only `|Tr U^m−Tr V^m| ≤ Nm‖U−V‖`,
  `m≤BN`, `R=2` giving `O_B(N^{−1/2})`); no repo counterpart needed.
- §16.5 word example (words `(0,1,0,2,0,3)` vs `(0,1,0,3,0,2)` with equal
  oriented-edge multiplicities but not rotations of each other) →
  NO repo counterpart; it is an obstruction remark about why naive
  oscillation claims fail, not a transfer input. It is preserved as a
  warning for the V_N⁽²⁾ step, not matched to anything.

## 3. P₂/P₃ matching (the only new mathematics in R1)

### 3.1 Set-up

Repo's finite-shift coefficients (`four_branch_parametrix.md` §2): for a
smooth amplitude `a`, after factoring `e(S/h)`, `P_n a` is the coefficient
of `h^n` in
`Σ_{k,l} c_{kl} e(kx+lS_x) exp(2πi[(S(x+hl)−S(x))/h − lS_x] + πikl h) a(x+hl)`,
with `P_0 a = g(x,S_x)a` and `D_n = iP_n` for `n≥1`. Transports:
`(∂_t−D_1)a_j = Σ_{n=2}^{j+1} D_n a_{j+1−n}` (TRACE-017 §6 eq. (17)).
§16's coefficients (§16.4): `𝒜_0=a(q,P)`, `𝒜_1=iℒ_1`, `𝒜_j` for `j≥2`
defined only as "finite differential operators obtained by ordinary
expansion of two shifts in (9.3)", with recursion
`(∂_t+ℒ_1)b_r = iΣ_{j=2}^{r+1} 𝒜_j b_{r+1−j}` (16.11).
Since `−D_1=ℒ_1` (§1.3), the two recursions coincide iff `D_n=i𝒜_n`
for `n≥2`, i.e. iff `P_n=𝒜_n`. The cases `n=0,1` are already settled:
`P_0=g=a` (§1.1) and `P_1=iℒ_1=𝒜_1` (§1.3).

### 3.2 P₂ = 𝒜₂: PROVED (sympy-verified against (16.4))

Expanding the repo formula with `Z=S_xx`, `W=S_xxx`,
`A=π(l²Z+kl)`, `B=πl³W/3` gives
`P₂a = Σ c_{kl}e(kx+lS_x)[(l²/2)a_xx + iAl·a_x + (−A²/2+iB)a]`.
Specialising the Fourier sums to §9-`a` via
`Σ c k^αl^β e = (2πi)^{−(α+β)}∂_x^α∂_p^β a` yields exactly §16 (16.4):
`𝒜₂b = cosϑ·(g/2·b_qq + g′/2·b_q + g′′/8·b − π²gZ²/2·b)
− πZ sinϑ·(g b_q + g′/2·b) − (π/3)g·∂_qZ·sinϑ·b`,
term by term (checked by hand and re-checked with sympy: all three
coefficient differences are identically 0). In particular the two terms
the re-base report flagged — `−π²gZ²/2` and `−(π/3)g∂_qZ·sinϑ` — and
all signs match. The grouped-(9.3) vs raw-shift presentation difference
(§1.2) is therefore closed at order 2: the two presentations give the
same operator through `h²`. Consequence: the first-correction transport
(16.5) is literally repo's `(∂_t−D₁)a_1=D₂a_0`, and Theorem A in the
literal §16 reading needs no further amplitude input.

### 3.3 P₃: computed formula, identification CONJECTURAL

§16 never displays `𝒜₃`; repo defines `P₃` only abstractly. Expanding
the repo formula one order further, with `Y=S_xxxx` and
`C=πl⁴Y/12`, gives `P₃a = Σ c e[(l³/6)a_xxx + (iAl²/2)a_xx +
(iBl−A²l/2)a_x + (iC−AB−iA³/6)a]`, which specialises (sympy-checked) to
the predicted `𝒜₃`:
`𝒜₃b = (i/6)g sinϑ·b_qqq + [(iπ/2)gZ cosϑ + (i/4)g′ sinϑ]·b_qq
+ i[πWg cosϑ/3 − π²gZ² sinϑ/2 + πg′Z cosϑ/2 + g′′ sinϑ/8]·b_q
+ i[πYg cosϑ/12 − π²WgZ sinϑ/3 + πWg′ cosϑ/6 − π³gZ³ cosϑ/6
− π²g′Z² sinϑ/4 + πg′′Z cosϑ/8 + g′′′ sinϑ/48]·b`,
with `W=∂_qZ`, `Y=∂_qqZ`. Note the alternating real/imaginary pattern
(`𝒜₀` real, `𝒜₁` imaginary, `𝒜₂` real, `𝒜₃` imaginary) is respected, and
one sign in the hand computation (the `Z³` term) was caught and corrected
by the sympy check — the formula above is the sympy version.

**Falsifiable test that would close P₃ (R-P3):** expand §9's grouped
form (9.3) directly to order `h³` — i.e. expand `g(q±h/2)b(q±h)` and the
phase differences `(2π/h){S(q±h)−S(q)}` through `h³` with the §16.2
identities — and compare the resulting operator with the formula above
term by term, including the `−π³gZ³cosϑ/6` term and the `Y`-term. If
they agree, `P₃=𝒜₃` is proved and the literal-model identification
extends to order 3; if any term disagrees, the literal model at order 3
differs from the repo model and must be treated as a separate model
(the repo-model Theorem B is unaffected — it never uses `𝒜₃`).
The test is a finite symbolic computation, no new analysis. It has NOT
been performed here: the formula above is a prediction from the repo
side, and the identification `P₃=𝒜₃` is labelled CONJECTURAL until the
grouped expansion is done.

> **ADDENDUM — R-P3 PERFORMED 2026-10-25 (staging only; the CONJECTURAL
> label above is retained for provenance and is superseded by this
> addendum, not silently rewritten). Verdict: PROVED.** The grouped
> expansion (9.3) was carried out directly to order h³ — expanding
> `g(q±h/2)b(q±h)` and the phase differences
> `(2π/h){S(q±h)−S(q)} = ±2πP + πhZ ± (π/3)h²W + (π/12)h³Y + O(h⁴)` —
> both by a structured hand derivation (even/odd split
> `𝒜₃ = cosϑ·S_even + i·sinϑ·S_odd`) and with sympy, plus an
> independent numeric route (exact grouped evaluation at 7 small h,
> degree-6 fit). All 14 (derivative × trig) monomials match the
> predicted formula above with sympy difference identically 0,
> including the `−π³gZ³cosϑ/6` term (u³/6 in the phase exponential,
> corrected sign reproduced) and the Y-term `iπYg cosϑ/12` (with no
> Y × sinϑ term on either side); the numeric route agrees to
> 2.9×10⁻⁶ relative. The same method reproduces 𝒜₀'s shift part,
> 𝒜₁ = iℒ₁ and 𝒜₂ = (16.4) exactly (diffs 0), validating the method
> at orders 0–2 before it is trusted at order 3. Full method,
> term-by-term table, and the logged first numeric attempt (degree-4
> fit, 3% error from A₅·e₂(nodes) contamination — a fit-design error,
> diagnosed and fixed) are in `RP3_REPORT.md` and the kept script
> `rp3_check.py` in this directory. **Consequence:** `P₃ = 𝒜₃` is
> proved; literal-model (16.15) at R = 3 no longer depends on R-P3
> and its only remaining residual condition is the pre-existing R-L6
> (Lemma 6 degeneracy handling). The repo-model Theorem B is
> unaffected (it never uses 𝒜₃). Orders j ≥ 4 remain uncomputed.
> TRACE-005 and BGS-001 stay OPEN regardless.

### 3.4 Orders ≥ 4

`P_j=𝒜_j` for `j≥4` is neither proved nor computed anywhere: repo's
`P_j` are abstract, §16's `𝒜_j` are undescribed beyond "finite
differential operators". The same method as §3.3 would compute them, but
the literal-model transfer at order `R≥4` additionally needs each of
them. This does not affect Theorem B at `R=k` for `k≤2`, and it does not
affect the repo-model Theorem B at any `R` (which uses repo amplitudes
throughout).

## 4. Verdict: what becomes PROVED, what stays conditional

**PROVED in the literal §16 reading once this dictionary is accepted**
(all entries EXACT in §2, plus §3.2):
- (16.10), the Laplace transfer to the single model `V⁽¹⁾` with error
  `O_f(N^{−1/2})`: inputs are the symbol/HJ/transport/gluing
  identifications (§1), the two-amplitude remainder (§2), polar
  unitarisation (elementary), and Lemma 6 — modulo residual R-L6 below.
- (16.15), the fixed-`k` transfer at `R≤2`, in particular the first pair
  test (`k=2`, `R=2`, error `O_b(N^{−1/2})`): inputs are the above plus
  the `P₂` match and §16's own (16.14) tuple count (`≤N^k`) and (16.13)
  moment formula, which are model-independent and elementary.
- The structural claims: no single fixed `R` transfers all `k` by this
  method (exponent `k−R−1/2` is identical in TRACE-017 eq. (14) and §16
  (16.15)); the Laplace transfer does not yield `Δ_k`; the `k`-dependence
  of the model is structural, not an artefact of the §9 presentation.

**CONDITIONAL (residual conditions, each falsifiable and finite):**
- R-P3 (§3.3): literal-model (16.15) at `R≥3` is conditional on the
  grouped-expansion check of `P₃=𝒜₃` (and, for `R≥4`, on the analogous
  checks for `P_j=𝒜_j`, `j≥4`). The repo-model Theorem B at every `R`
  is already proved and does not depend on this.
- R-L6: Lemma 6's eigenangle matching through degeneracies (§16.1) is
  compressed, not re-proved or independently checked. This is the only
  residual condition on (16.10) and on (16.15) at `R≤2`. It is standard
  perturbation theory (compression eigenvalues on degenerate subspaces,
  absolute continuity of lifted branches), and the factor `(N/π)` in
  (16.1) was re-checked in the re-base stream C — but "standard" is not
  "checked": a line-by-line reading of §16.1 against a reference
  treatment (e.g. Kato) would discharge it.

**Disposition of the U1–U16 gaps for the transfer (not for §9 as a whole):**
- U1 (amplitude-derivative bounds / `C_rem` for §9.4): BYPASSED — the
  transfer uses the repo remainder, never §9.4's. U1 remains open for
  §9's intensity proof; it is not a condition on the transfer.
- U2 (variable-denominator Abel step, Lemma 9.12), U3 (10⁶⁰ bound (9.16)):
  IRRELEVANT to the transfer — they belong to §9.5–§9.7 (the intensity
  proof), which §16's transfer does not use. The landed note's statement
  that "no §9 intensity bound is used" stands.
- U4 (gluing preservation at `t≠0`, uniqueness class / mod-4 branch
  identification unstated in §9): DISCHARGED for the transfer by repo
  §2's uniqueness argument and explicit identities (§2, gluing entry).
- U5 ((9.5)'s "completing the square mod 8" sentence does not prove the
  identity): DISCHARGED for the transfer by repo §1's Gauss-sum proof.
- U6–U16 (remaining §9.5–§9.7 / intensity items, per the verification
  report's grouping): IRRELEVANT to the transfer, same reason as U2/U3.
  None of them is closed by this dictionary; the dictionary only removes
  them from the transfer's dependency list.

**NOT closed by this dictionary (explicitly):** the phase model's own
Sine₂ law; the uniform-in-word-length oscillatory estimate at `m≍N`;
the negative coherent correction `−δ*`; the Y-sum limit; any `k≥3`
statement about the true `U_N` (as opposed to transfer of tests to the
model); TRACE-005; BGS-001. The next step remains the V_N⁽²⁾
uniform-in-word-length asymptotic attempt, now with the model
identification in hand.

## 5. Honest open list

1. P₃ identification (R-P3, §3.3): formula predicted, grouped-expansion
   check not performed. Why open: §16 never displays `𝒜₃`; the check is
   mechanical but was not done here.
2. `P_j=𝒜_j` for `j≥4`: uncomputed on both sides. Why open: abstract
   definitions only; needed only for literal-model orders `R≥4`.
3. Lemma 6 degeneracy handling (R-L6, §4): compressed proof, not
   independently checked. Why open: it is §16's own argument, outside the
   repo; standard but unchecked.
4. `e_k(T_{N,b})` reference and `Δ_{k,N}` definition: imported from §16,
   no repo counterpart, and no repo definition is proposed here. Why not
   a gap for the transfer: the reference cancels in (16.15)'s difference.
   It WOULD be a gap for any claim about the absolute value of `Δ_{k,N}`,
   which neither §16's transfer nor this dictionary makes.
5. Time-interval constants (`T=10⁻³⁰` vs `10⁻²⁰`): compatible, not
   identical (§2). Why not a gap: only `τ` is used.
6. Effective thresholds: none on either side (`N₀` noneffective, §9's
   `N₁/N₂` uncomputed). Why recorded: any future finite-`N` claim from
   the transfer would need them; the asymptotic transfer does not.
7. §16's analyticity/boundedness claims for `b_{r,ν}` at fixed order
   (`r≥1`): §16 asserts real-analyticity and `N`-uniform derivative
   bounds on the fixed compact; the repo side proves the same for
   `a_{r,j}` via its characteristic-graph bounds (§2, §6: "all finitely
   many derivatives needed are bounded on the fixed compact charts").
   Matched by the amplitude identification, hence EXACT for `r≤2` and
   CONJECTURAL for `r≥3` in the same sense as §3.3 — not a separate gap.
8. The external document's §§9.5–9.7 intensity proof as a whole: untouched
   by this dictionary. Its U-gaps stand as recorded in the verification
   report; the repo already has the intensity result via FM-021, so
   nothing in the transfer depends on closing them.
9. Live-main confirmation: this draft was built against the 4b3a577
   snapshot copy of the landed note per the task instruction, not against
   a fresh live-main read (no live-browser access in this session). The
   parent must confirm `phase_model_transfer.md` is unchanged at landing
   time; if it changed, the dictionary's citations to it must be re-pinned.
