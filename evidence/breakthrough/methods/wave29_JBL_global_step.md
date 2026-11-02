# Wave 29, task 5 — JBL from R**: the global step, closed at two components, open in full

## Verdict

R** alone does not close JBL, and the reason is structural, not a
missing computation: R**'s hypothesis *is* JBL's conclusion (signature
equality up to π), so R** can only convert a π into a parameter
relation, never supply the π. The step that must supply π is the
global-multiset-to-parameter step, and it splits in two:

- **At fixed two-component level (q₂, q), the step is CLOSED**
  (exhaustive, below): joint global multiset ⇒ single parameter
  relation ⇒ JBL, via transport.
- **At full multi-modulus level it is NOT closed by R**: the step
  needs cross-modulus coherence (COH, §4), which is equivalent in
  difficulty to JBL itself. The extra input R** + per-component data
  lacks is exactly the joint (same-index) pairing across components
  (§3, explicit pair). Repository untouched; no Lean built.

## 1. Setup and the transport lemma

R = ℤ[√2], α = 3+2√2, t = gcd(m,4), β = α^t, B_r = Aα^r.
For a component pair (q₂, q), the signature is
S(A) = (J^{(q)}_r(A))_{r mod t}, J^{(q)}_r = sorted multiset over s
of (Tr(B_rβ^s) mod q₂, Tr(B_rβ^s) mod q). JBL's conclusion is
S(A′) = S(A) ∘ π for one π ∈ D_t. JBL's hypothesis is equality of
the *joint* global multiset: sorted list over i of the tuples
(Tr(Aα^i) mod q) over all q ‖ D_m (exact multiset = CRT of these).

**Transport lemma (proved, for the R** slack).** If
A′ = c(A)α^j + z + w (mod q₂·q), c ∈ {id, conj}, z ∈ Ann, w ∈ Shadow,
with one j, c across both components, then S(A′) = S(A) ∘ π for
π induced by (j, c): α^j permutes classes by r ↦ r+j (mod t) and
β-action inside a class preserves sorted pairs; conj reflects;
Ann preserves every trace exactly; Shadow preserves signatures by
its collapse mechanism (wave 25 §3, wave 28: Shadow = {27D :
D ∈ R/(q/27)R}, multiples of 27, hence invariant under α-multiplication
and conjugation, so the form is also closed under composition).
Thus a *single global* parameter relation implies JBL by transport.

## 2. Two-component closure (exhaustive, exact integers)

Group genuine parameters by the *joint* global multiset (sorted
tuples, same-s pairing kept), and test (a) a common π for signatures,
(b) a parameter relation A′ = c(A)α^j + z + w with one j, c.

- m=12, (128, 81), Shadow = {27D : D ∈ R/3R}: 10368 parameters,
  50 joint-global groups, JBL-bad pairs 0, PARAM-bad pairs 0.
- m=8, (512, 9), Shadow = {3D : D ∈ R/3R}: 4608 parameters,
  57 joint-global groups, JBL-bad 0, PARAM-bad 0.
- m=36, (128, 243), ShadowBig = {27D : D ∈ R/9R}: 93312 parameters,
  128 joint-global groups, JBL-bad 0 over all 93184 non-rep pairs.
  PARAM then follows from JBL + wave-28 R** (0/520 escapes) +
  transport (§1), since π can be transported to id before applying R**.

So in every tested two-component subsystem, joint global data
determines the parameter up to Ann + Shadow, and hence π.

## 3. Per-component data provably does not determine π (explicit pair)

Group the same m=12 parameters by *per-component* global multisets
only (sorted mod-128 list, sorted mod-81 list, pairing forgotten).
One per-component group contains both
A = ((0,8), (0,9)) and A′ = ((0,8), (36,0)):
their signatures have disjoint class-multiset sets —
A has classes (64,72)×3 and (64,9)×3, A′ has neither (it has
(0,72)×3 and (0,9)×3 instead) — so no π ∈ D₄ relates them.
This is the Fix-level analogue of the wave-12 abstract G3
obstruction: component π-sets plus a common σ do not imply a common
π. **The extra input needed beyond R** + per-component data is the
joint pairing itself** — the same-index tuple across components,
which JBL's hypothesis does contain but per-component lemmas discard.

## 4. Full level: the coherence gap COH

Apply R** per odd q to a JBL pair and one gets per-q relations
A′ ≡ c_q(A)α^{j_q} + z_q + w_q (mod q₂·q), with j_q, c_q possibly
depending on q. A single global j, c — the form transport needs —
requires **COH**: the j_q, c_q can be chosen compatibly, i.e. one j
mod L = lcm of the orders and one c with A′ ≡ c(A)α^j + z_q + w_q
for every q. COH is not supplied by R** (verified per pair only),
nor by G1/G2 alone (they give per-q π_q, not compatibility).
Consequences, as lemmas:

- (global⇒parameter with single j, c) ⇒ JBL, by transport (§1).
- JBL + COH ⇒ (global⇒parameter), by per-q R** + COH + composition.
- Hence the full global step is *equivalent to JBL + COH*, not a
  simplification of JBL. Closing JBL "from R**" by this route just
  restates the problem: the remaining open lemma is COH, i.e. the
  pair-contingency / PC content (wave 12: 670800 preserved cases,
  0 bad at mod-p level; wave-12 m=12 random full check: 30838
  colliding pairs, 0 π-empty) lifted to prime powers.

## 5. Conditional theorem (narrow hypothesis, as required)

Assume (i) R** with generalized shadow R/(q/27)R at every odd q,
(ii) G1 (odd prime-power lift) and G2 (2-part) preserving the
per-q shift, (iii) PC pair-compatibility across components in the
form COH above. Then JBL holds: COH + R** give one global parameter
relation from the joint global multiset, transport (§1) gives the
common π. Dropping (iii) breaks the theorem by §3; dropping (i)
breaks it by the wave-23/24 rigidity counterexamples (n=1, q=81),
which R** absorbs exactly via Ann + Shadow.

## 6. What remains, precisely

1. COH in general (the only gap between R** and JBL at full level);
   a proof of COH at mod-p level would already reduce the problem
   to G1/G2 lifts.
2. General proof of R** itself (collapse-digit mechanism beyond
   q=81, 243; common-π coherence inside R** is the same COH).
3. Lean formalisation (nothing here is a Lean theorem).

## Files

- This note: `methods/wave29_JBL_global_step.md`
- Scripts: `methods/wave29_JBL_global_step.py` (m=12, m=8: JBL + PARAM),
  `methods/wave29_JBL_global_step2.py` (m=12 per-component pair;
  m=36: JBL over 93184 pairs)
- Prior: `methods/wave25_JBL_rescue.md` (R**),
  `methods/wave28_JBL_Rstar_243.md` (generalized shadow),
  `methods/wave20_JBL.md` (JBL), `methods/wave12_g3_common_pi.md` (PC/G3)
