# LEDGER CLAIM MAP — HOSTILE AUDIT OF THE BGS / COMPRESSED-CAT-MAP WORKSPACE

Auditor: adversarial referee, no prior context. Date of audit: 2026-08-28.
Sources read in full: `BGS/LEDGER.md` (4308 lines), `BGS/THEORY.md` (1071 lines),
`BGS/paper/resonance_laws_catmaps.tex` (1077 lines). Also read: `README.md`,
`ROADMAP.md`, `IDEAS.md`, `artifacts/MANIFEST.md`, `review/audit_2026-08-26.md`,
`review/redteam_run5.md`, `review/subgroup_kloosterman.md`,
`drafts/tail_bound_proof.md`, `drafts/tail_bound_attempt.md`,
`artifacts/ring2/synthesis.md`, `artifacts/ring3/REPRO.md`,
`src/exact_verify_run5.py` (theta_sign), plus the JSON contents of ~25 artifacts.
Filesystem existence checked for every cited artifact, script and Lean file.

Notation: `L:n` = `BGS/LEDGER.md` line n. `TH:n` = `BGS/THEORY.md` line n.
`PA:n` = `BGS/paper/resonance_laws_catmaps.tex` line n. All paths relative to
`C:\Users\churi\Desktop\BGS\BGS_portable_20260827\BGS\`.

---

## 0. VERDICT UP FRONT

The workspace is unusually well-documented and contains several genuinely proven,
genuinely elementary results (matched resonance identity, zero-count lemmas,
ensemble-mean law, torsion/Egorov/Birkhoff algebra). It also contains, **live and
uncorrected on disk today**:

1. **A "PROVEN" theorem whose proof is explicitly labelled "heuristically" in the
   only document that contains it, and which the same document declares invalid
   for the case it is applied to.** (`drafts/tail_bound_attempt.md:36` + `:49-62`
   vs `drafts/tail_bound_proof.md:75-93`; propagated as PROVEN into `PA:971`,
   `PA:976`, `TH:552-559`, `L:2883-2890`, `ROADMAP.md:126`.)
2. **A retracted fabricated number still printed in the paper.** `PA:881`
   "max/median ≈ 15–40" was retracted as a fabrication at `L:3375-3383`; the
   paper was edited on 2026-08-28 (`PA:27-52` edit log) without removing it.
3. **A "red-team-corrected" bound that misquotes the red team**, replacing one
   wrong constant with a different wrong constant (`TH:436-472`, `PA:929-935`
   claim `EXTRAS ≤ k³p^{−2δ}`, threshold `k ≪ p^{2δ}`; the red team's actual
   correction is `extras ≤ k⁴p^{−2δ}`, threshold `k ≲ p^{δ}`, i.e. vacuous —
   `review/redteam_run5.md` §C3 item 3).
4. **A load-bearing empirical headline that is arithmetically impossible as
   stated and is a misread of a JSON field name.** "Weil bound essentially tight,
   max|S|/(2√p) ≈ 0.99999 at p=4001, k=4" (`L:3746-3748`, `TH:576`,
   `artifacts/ring2/synthesis.md`, `ROADMAP.md`). The artifact field is
   `ratio_over_weil_only` with `weil_only = min(k, 2√p) = 4`; the true ratio to
   2√p is 0.0316. The data show the **trivial** bound is tight (no cancellation
   at k=4), the opposite of the reported conclusion.
5. **A refutation-of-a-prior-run narrative built on a misquotation.** R68/R69/R70
   repeatedly "refute" an alleged R54 threshold "k ≥ 50" (`L:4015`, `L:4060`,
   `L:4241`, `TH:744`, `TH:820`, `TH:889`). R54 never says this; R54 says
   `m ≥ 70` for a *Wigner-spacing* test (`L:2921-2923`), a different quantity.
6. **The paper source does not compile.** `\begin{remark}` count 8,
   `\end{remark}` count 7: `rem:rev` (`PA:363`) is never closed; the
   2026-08-28-added `rem:reversing_degenerate` (`PA:376`) is nested inside it and
   the lone `\end{remark}` at `PA:411` closes the inner one. The `.tex` is dated
   2026-08-28 12:48; the `.pdf` is dated 2026-08-27 02:22. Nobody checked.
7. **The Lean evidence base does not exist on this machine.** `C:\lean\bgs_formal`
   is absent, so `BgsFormal.lean`, `BgsAudit.lean`, `ResonanceLemmas.lean`,
   `card_le_four_draft.lean` — the sole support for "PROVEN (Lean-formalised)"
   at `PA:923` and `README.md` — are unverifiable.
8. **The generator of the T13 evidence artifact is missing, and the artifact
   itself contains the fingerprint of the very defect R65 claims it does not
   have.** See §4 item D-1 and §5 item S-2. This is the single worst
   evidence-chain failure found.

Roughly 20% of cited artifacts/scripts do not exist on disk (§4). Two claims
("BGS at order 4", "arithmetic beats symmetry") were correctly retracted with
loud, dated entries — the retraction hygiene is genuinely good where it exists,
which makes the eight failures above harder to excuse, not easier.

**Nothing in this workspace proves BGS.** The workspace itself says so
(`PA:984` "Full BGS for raw compressions — NOT CLAIMED"). That self-assessment is
accurate and is the single most defensible statement in the corpus.

---

## 1. CLAIM INVENTORY

Status column = the tag the project itself asserts. "AUDIT" column = my verdict:
`OK` (tag defensible), `SKETCH` (called PROVEN, proof not written or incomplete),
`DRIFT` (tag improved without new evidence), `DANGLE` (evidence missing on disk),
`CONTRA` (contradicted elsewhere in the corpus), `VOID` (retracted).

### 1.1 Run-1 retractions (all correctly executed)

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| RET-1 | Kernel `K(x,y)=p^{-1/2}exp(iπ/p·[c^{-1}(dx²−2xy+ay²) mod 2p])` is NOT a quantisation of A: measured Egorov error O(1) (7.6 at p=11, 0.8 at p=101) vs 1e-14 for the correct `U_A = N^{-1/2}ω^{(2c)^{-1}(dx²−2xy+ay²)}`, N odd, gcd(c,N)=1. Voids all run-1 statistics R3–R6. | RETRACTED (fatal) | L:20-31 | "run log of the Egorov scan"; `artifacts/retracted_run1/README.txt` (states artifacts deleted) | Permanent. Lesson L0 at L:44-46 | OK — exemplary. Numeric evidence itself deleted, but the deletion is declared. |
| RET-2 | Run-1 "a=d ⟺ complex-symmetric kernel ⟹ β=1" was a gauge artefact of the wrong kernel. | RETRACTED | L:33-35 | superseded by T3/T4 | Permanent | OK |
| RET-3 | Run-1 "torsion theorem max-dist ≈ π/(2k)" is trivial (half-mesh bound for any quasi-uniform set). | RETRACTED | L:37-38 | — | Permanent | OK |
| RET-4 | Run-1 "DES multiplicities up to 23" were lattice-cell occupancy counts, not spectral multiplicities. | RETRACTED | L:40-42 | superseded by T2 | Permanent | OK |
| (unnumbered) | An intermediate GUE reading of the compression caused by an SVD rank cut at `0.5σ_max` that silently truncated eigenspaces; corrected to a 1e-6 relative cut. | RETRACTED | TH:323-324, L:528-530 | — | Permanent | OK — good self-catch, well recorded. |

### 1.2 T-series (run 2 core algebra), as amended by run 3

| ID | Statement (with hypotheses) | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| T1 | `U_A(x,y)=N^{-1/2}ω^{(2c)^{-1}(dx²−2xy+ay²)}` (N odd, gcd(c,N)=1) is unitary and satisfies exact Egorov `U_A T(n) U_A† = T(An)` for all n∈(Z/N)². | PROVEN, 3e-14 | L:52-55, TH:56 | Egorov scan log; `src/catmap_core.py` (present), `src/perturb_rmt.py` (ONLY in `src/archive/`) | **REPAIRED by A1/R5** (`L:553-561`, `L:701`): the kernel quantises **Aᵀ**, not A, and only up to a scalar phase `s_n` with an extra quadratic `q_A(n)` (`L:670-674`). Run-2 verified only symmetric Arnold (b=c), masking it. | CONTRA-then-fixed. The T1 block at `L:52-55` and `TH:49-52` still assert the FALSE `T(An)` form with no in-place warning; only the header note `TH:5-7` corrects it. A reader of `TH:49` alone gets the wrong statement. |
| T2 | k := ord_N(A) least k≥1 with A^k ≡ ±I; K := k if A^k≡I else 2k. Then `U_A^K = χ·I` exactly, so spec(U_A) ⊂ a coset of K-th roots of unity: ≤K distinct eigenvalues, multiplicity ≥ N/K. | PROVEN 1e-13; **KNOWN, re-derived** | L:57-70, TH:58-64 | measured p=11,101,199,521,3571; `‖U^K/χ−I‖/√p ≤ 2.6e-13` | Attribution block is exemplary (Hannay–Berry 1980; Keating 1991; Kurlberg–Rudnick Duke 103 (2000) 47; FNDB CMP 239 (2003); Mezzadri 2002) | OK. Honest "not ours" labelling. |
| T2′ | Along any sequence of odd N with ord_N(A)/N → 0, the fraction of exactly-zero NN eigenphase spacings → 1, so P(s) → δ₀ ⇒ BGS fails for the unperturbed cat map. Such sequences exist (ord ≪ log N i.o.); under GRH ord ≫ N^{1−ε} on a density-one set. | PROVEN (corollary) | L:72-79, TH:66-69 | literature only (KR CMP 2001; Bonechi–De Bièvre CMP 211 (2000) 659; Kurlberg Acta Arith. 110 (2003) 141) | unchanged | OK, and it is the honest foundation of the whole programme: the raw family is a *counterexample* to naive BGS. |
| T3 | For A∈SL(2,Z), A≠±I, t=a+d, W=2A−tI: any R∈GL(2,Z) with det R=−1, RAR⁻¹=A⁻¹ is traceless, R²=I, and with R=[[p,q],[r,−p]] the conditions are exactly `p(a−d)+qc+br=0`, `p²+qr=1`. With S=diag(1,−1), M=SR, `Θ := U_M ∘ (complex conjugation)` satisfies `ΘU_AΘ⁻¹=U_A⁻¹`, `Θ²=+1`. Hence every quantised cat map is in the β=1 class. | PROVEN, 8e-16 | L:81-102, TH:71-84 | "reversibility/anti-unitary scan log" (no file named); 8e-16 at p=101,257,521 + 8 further A | Existence of R "for every A" is asserted "by the standard SL(2,Z)-conjugacy/ideal-class correspondence" — **no proof, no citation with a theorem number**. `Θ²=+1` later given an analytic proof (R5.1, `L:792-800`) that needs `gcd(M₂₁,N)=1`. | SKETCH on the existence half. The red team also notes (`review/redteam_run5.md` §C1) "R necessarily traceless is correct, though nowhere *proved* in the repo". |
| T4 | Θ preserves every eigenspace H_λ; in an ON basis B, Θ acts as c ↦ W c̄ with W=B†U_M B̄; W unitary, symmetric, W W̄=I; Q=W^{1/2} gives QQᵗ=W and in basis BQ, Θ|H_λ is plain conjugation. Hence for Hermitian V: `[Θ,V]=0 ⟺ V_λ unitarily equiv. to a REAL SYMMETRIC matrix`. | PROVEN, 4e-15 | L:104-115, TH:86-91 | "real-structure verification log" (no file); ‖Im V′‖/‖V′‖ = 4.0e-15 vs 6.7e-01 | unchanged | OK modulo unnamed artifact (D-6). |
| T5 | For the symmetric split `U_ε := e^{iεV/2}U_A e^{iεV/2}`: `ΘU_εΘ⁻¹=U_ε⁻¹ ∀ε ⟺ ΘVΘ⁻¹=V`. (Asymmetric splitting needs `ΘVΘ⁻¹=U_A⁻¹VU_A`.) | PROVEN, 8.9e-15 | L:117-123, TH:93-97 | `artifacts/floquet_symmetric.json` ✔ present | unchanged | OK |
| T6 | With `V̄ := K⁻¹Σ_{j<K}U_A^j V U_A^{−j}`: `[V̄,U_A]=0` and `P_λVP_λ = V̄P_λ = P_λV̄P_λ`. | PROVEN, 3.3e-15 | L:150-158, TH:117-120 | proof given in situ (Egorov + `Σ_J λ^{−J}U^J = K P_λ`) | independently re-verified R3 (`L:681`) | OK. Proof is complete and short. |
| T7 | For all v∈(Z/N)² and all J ≢ 0 mod K: `|Tr(T(v)U_A^J)| = 1`. | PROVEN, 1.6e-15 | L:160-166, TH:122-125 | proof in situ (Parseval in Weyl basis + invertibility of A^J−I) | **HYPOTHESIS ADDED by R2** (`L:603-606`): requires `gcd(N, tr(A)²−4)=1`; at p | tr²−4 the identity FAILS (up to 10.18 at N=25). "Run 2 never stated this." | CONTRA-then-fixed. The T7 blocks at `L:160` and `TH:122` still carry **no** hypothesis in-place; only `TH:7` header notes it. |
| T8 | For `V=Σ_{n∈F}(c_nT(n)+c̄_nT(n)†)`, `C:=2Σ|c_n|`, m=rank P_λ, `a_r(N)` = T(0)-coefficient of V̄^r: `(1/m)Tr((P_λVP_λ)^r) = a_r(N) + θ_r`, `|θ_r| ≤ C^r/m`; and `a_r(N) → ∫_{T²}(V̄_cl)^r`. | PROVEN + verified | L:168-180, TH:127-131 | proof in situ | **REPAIRED by A3/R3** (`L:572-576`, `L:608-611`): the constant is **N/K**, not m; per-multiplet `Tr V_λ^r = (N/K)a_r + O(C^r)` with weight `w_λ = N/(Km_λ) = 1+O(1/N)`. | CONTRA-then-fixed; again no in-place amendment at `L:168`/`TH:127`. |
| T8′ | The empirical eigenvalue distribution of `P_λVP_λ` converges to the law of the classical K-step Birkhoff average under Lebesgue measure; variance `K⁻²Σ_{v≠0}|b_v|²`, i.e. width `σ_cl/√K`. | PROVEN corollary + verified | L:182-197, TH:133-138 | table (KS 0.064→0.015 at p=199…3571 vs m^{−1/2}); `artifacts/birkhoff_density.json` ✔; `src/birkhoff_density.py` **MISSING** | unchanged | DANGLE (script gone, not even in `src/archive/`). |
| T9 | For any u₁,…,u_r ∈(Z/N)² there is a Weyl-cocycle phase φ with `Tr(P_λT(u₁)···T(u_r)) = φ·m·1{Σuᵢ≡0} + E`, `|E| < 1`. | PROVEN, verified | L:199-207, TH:140-146 | `artifacts/cancellation_identity.json` ✔; m to 7e-15, modulus ≤0.53 off-resonance | R3 sharpened to `|E| ≤ (K−1)/K` **including u=0** (`L:579-581`); also inherits the `gcd(N,tr²−4)=1` hypothesis via T7 (`L:605`) | OK, hypothesis-drift as T7. |
| T10 | `‖P_λT(u)P_λ‖²_HS = (m/K²)#{(j,j′):A^{j′}u=A^ju} + O(1) = m/K + O(1)`; cross-orbit HS inner products are O(1). Mean square entry `1/(mK)(1+O(1/m))` with mK ≈ N. | PROVEN, verified | L:209-216, TH:148-153 | p=1597 (m/K=1.353): HS dev ≤0.055, cross ≤0.091; p=199,521 all ≤0.43 | unchanged | OK. Note "O(1)" with measured values up to 0.43 against a target of O(1) is weak evidence but honestly reported. |
| T11 | Centraliser torus `{xI+yA : x²+xyt+y²≡1}` has order N∓1 and commutes with U_A to 1e-15. For split primes, Hecke-basis entries are Gauss sums (n₁=0) and twisted Jacobi–Kloosterman sums (n₁≠0), modulus ≤2√N by Weil. | PROVEN + measured | L:218-229, TH:155-161 | p=521,m=41: moduli [3.5e-4,8.8e-2], mean 0.0388 vs √p/(p−1)=0.0439, Weil ceiling 0.0878; off-diag kurtosis 3.109; diag/off-diag var ratio 1.85–2.10 | The kurtosis 3.109 datum is later **CONTESTED** (F3, `L:684-690`): reviewer measures 6.78–7.94 for A=[[3,1],[2,1]] at p=521, seed-unstable 2.37–6.16, band-dependent | CONTRA (partially). "PROVEN + measured" conflates a proved algebraic statement with a contested statistical one in one tag. |
| T12 | For `f(x)=Σ_{r≤R}f_rx^r`, `C=2Σ|c_n|`, every eigenvalue λ of U_A: `Tr f(V_λ) = m·Σ_r f_r a_r(N) + O_f(1)` and `|Tr f(V_λ) − Tr f(V_{λ′})| ≤ 2Σ_{r≤R}|f_r|C^r`, independent of m,N. Claimed as Dyson–Mehta spectral rigidity, **unconditional**. | PROVEN UNCONDITIONALLY, verified | L:231-246, TH:163-176 | `artifacts/rigidity.json` ✔; `src/rigidity.py` **MISSING**; spreads 8.22 vs 48.3 (p=521), 2.45 vs 12.3 (1597), 7.12 vs 193.7 (3571) | Inherits T8's m→N/K repair and T7's gcd hypothesis, so "unconditional" is false as literally written | DANGLE + CONTRA. "Unconditional" is asserted three times in bold (`L:238`, `TH:170`) while the proof depends on T7, which R2 proved **requires** `gcd(N,tr(A)²−4)=1`. |
| T13 | `M(SMS)=SR·RS=SR²S=I` ⇒ `SMS=M⁻¹` ⇒ `Θ² = U_M conj(U_M) = c(M,M⁻¹)·1`; anti-unitarity forces c real so c=±1, sign independent of the phase normalisation of U_M, hence a metaplectic invariant. c=+1 ⇒ β=1; c=−1 ⇒ GSE. Measured c=+1 for **all** reversing involutions in the box `|·| ≤ 25`, traces 3,4,4,5,6,8,13, p=101,199,521,1009, residual ≤8.3e-16. Conclusion: only β=1,2 occur; GSE does not. | PROVEN + verified 7 matrices × 4 primes | L:248-260, TH:178-211 | `artifacts/theta_sign.json` ✔ (28 entries) | **DOWNGRADED by red team C1** (`review/redteam_run5.md` §C1): proof silently assumes `gcd(M₂₁,N)=1`; the legitimate reverser `R=[[1,−1],[0,−1]]` for Arnold has M₂₁=0 for every N and was **skipped** by `theta_sign.py:64`; "for all R in the box" is therefore false. Hypothesis added 2026-08-28 (`TH:186-211`, `PA:376-411`). | **CONTRA + DANGLE + DRIFT.** See §4/D-1 and §5/S-2: the generator `src/theta_sign.py` is **absent**, and the artifact records only 6–7 involutions per config against the red team's count of 16 in the box — i.e. the artifact itself is evidence that the skip occurred, while `L:3615-3629` claims the opposite. |
| T14 | Robustness: for A with traces 3,4,6,8 at the primes of largest multiplicity in 300..3000 (m=48…96, split+inert), structural identities hold uniformly (1.1e-15; Θ² sign +1 at 7.7e-16; ‖U^K−χ·1‖≈4e-15); Θ-invariant V gives L1(GOE)=0.077…0.148 (control 0.081), generic gives L1(GUE)=0.079…0.132 (control 0.070), 8/8 classified correctly; Σ²(L) table vs GOE/GUE/Poisson. | verified | L:262-281, TH:213-218 | `artifacts/robustness.json` ✔ | unchanged | OK. Note L1(GUE)=0.132 vs control 0.070 is ~2× the control — "all classified correctly" is a rank statement, not an agreement statement, and is worded to sound like the latter. |
| T15 | Weil propagator factorises as chirp·(permuted DFT)·chirp, O(N log N), rel. error 6.2e-16 vs explicit matrix; reaches p=28657 (ord 23, K=46, m=623, residual 3.6e-15): Θ-inv L1(GOE)=0.141 β=0.85 (control 0.123/0.99); generic L1(GUE)=0.125 β=2.03 (control 0.117/1.43); Σ²(32)=1.030/0.630 vs GOE 0.845, GUE 0.631, Poisson 14.995. | verified | L:283-297, TH:220-224 | `artifacts/fast_weil_check.json` ✔, `artifacts/largescale.json` ✔; `src/fast_weil.py` ✔ | unchanged | OK. The generic control β=1.43 vs measured 2.03 is a 40% control failure, reported but not flagged. |
| T16 | Spectral form factor pooled over 224 spectra (p=1597,2161,2207,3001,3469,3571; m=47…210, median 64), Gaussian window on central 60%: RMS over τ∈[0.1,0.9] = 0.0365 vs GOE analytic `2τ−τln(1+2τ)` (Θ-inv) and 0.0270 vs GUE analytic `τ` (generic); 11–19× better than Poisson. | verified, 224-sample ensemble | L:299-323, TH:226-233 | `artifacts/form_factor_pooled.json` ✔, `form_factor.json` ✔ | **CONTRADICTED by R6.5** (`L:1047-1054`): a second pipeline (`form_factor_campaign.py`) disagrees at large τ; "gen FAILS under this pipeline (rms vs GOE 0.175 < vs GUE 0.237)"; recorded [INCONCLUSIVE], "must reuse the pooled-moduli pipeline of run-2 T16 before any claim" | CONTRA. Two pipelines disagree on the sign of the GOE/GUE discrimination for generic V; T16 is never re-tagged. The form factor claim is *not* in the final paper — the only reason this does not damage the paper. |
| T17 | Diagonalising A, single-orbit 4th-order cancellation ⟺ `Σεᵢhᵢ=0` and `Σεᵢhᵢ⁻¹=0`, hᵢ∈H=⟨α⟩, |H|=k (same system split and inert). **Theorem** for signs (+,−,+,−): solution set = (i) `{h₁,h₃}={h₂,h₄}` as multisets, plus (ii) `h₃=−h₁,h₄=−h₂` iff −1∈H. `#sol = 2k²−k` (−1∉H), `3k²−3k` (−1∈H). | PROVEN + 19/19 exact | L:325-352, TH:235-250 | `artifacts/cancellation_r4.json` ✔; `src/cancellation_r4.py` in `src/archive/` only; 19 cases p≤2003, k≤25 | **The written proof was found wrong at R41** (`L:2333-2361`): "Claimed case (a) contributes k²−k … WRONG … Correct count is k². Old proof derived correct totals via compensating mistakes." Statement unchanged; proof rewritten (now `PA:304-330`). Also re-verified 5/5 (`L:2247`), 15/15 (`L:1560`), 7/7 (`L:1532`), 40 configs in Julia (`L:2730`), 51/51 (`review/audit_2026-08-26.md`). | OK now (this is the strongest result in the corpus), but note `L:340-344` and `TH:245-247` still print the run-2 proof sketch with no R41 cross-reference. |
| T18(a) | Structural: for each divisor d≥2 of k the order-d subgroup is all d-th roots of unity, so it and every coset sum to zero (same for inverses) ⇒ non-pairing solutions exist iff s is a sum of divisors ≥2 of k, and are absent for every s below the least prime factor of k. | PROVEN | L:354-362, TH:252-257 | verified p=3001,k=15,d=3,5,15; k=15 has 720 extras at s=3; k=5,7,11,13,25 have 0 at s=2,3 | unchanged | OK |
| T18(b) | Sporadic: mod-p coincidences, present/absent by Chebotarev-type criterion. k=13,s=4: extras 4368 (p=313), exactly 416 (p=521,547,911), 0 (p=599,677,859,937,1093). Over k=13,17,19,23 × 10 primes, `extras/pairings ≈ c·k^s/p²`, c∈[0.01,0.11]. | measured | L:363-368, TH:258-261 | no artifact named | unchanged | DANGLE (no artifact). |
| T18-barrier | The 2s-th moment matches Wigner with relative error `O(k^s/p²)` once k has no prime factor ≤ s; with k=p^θ this is o(1) **iff s < 2/θ**, whereas a local law needs s ≈ log m = (1−θ)log p. Hence **the moment method provably cannot reach the mean-spacing scale**. | PROVEN (stated as such) | L:369-377, TH:263-270 | derived from T18(a)+(b) | Never retracted. **Directly contradicted in spirit by R11-C** (`L:1481-1497`) which claims "all fixed-moment WD matching … = BGS at the level of all fixed-moment statistics"; R11-C is itself retracted at R12-A. | OK, and it is the most valuable negative result here. Note it makes the later "moment hierarchy → local law" plans (`L:1960-1962`, `L:2008`) self-defeating — pursued anyway for ~10 runs. |
| T19 | Weyl completeness `Σ_u T(u)XT(u)† = N·Tr(X)·1` gives `Σ_u (P_λT(u)P_λ)_{ab}·conj((P_λT(u)P_λ)_{cd}) = N δ_{ac}δ_{bd}`; splitting off u=0 and using T6 (compression depends only on the A-orbit) gives `Σ_O (|O|/K)(M_O)_{ab}conj((M_O)_{cd}) = (N/K)δ_{ac}δ_{bd} − (1/K)δ_{ab}δ_{cd}`. The constant is **N/K, not m**. | PROVEN, machine-exact 1e-15 | L:379-402, TH:272-286 | `artifacts/tight_frame.json` ✔; rel. err 1.4e-15…2.2e-16 at p=41,101,199,313; premise made exact-integer at X4 (`L:786-788`) | unchanged; independently re-verified R3 (`L:580-581`) | OK. The self-caught m→N/K error (spurious 5.1e-3 = (N/K−m)/m at p=199) is documented — good practice. |
| T20 | An observable with |F| frequency pairs has 2|F| real parameters vs m eigenvalues. At p=3571 (m=210, 17 multiplets, ≈3550 spacings), **one orbit = two real parameters already gives GOE** (L1_GOE 0.1043 vs control 0.079); from two orbits the GOE/GUE dichotomy is fully resolved. ⇒ the pseudo-randomness is arithmetic, not parametric. | measured, decisive | L:404-424, TH:288-296 | `artifacts/dof_test.json` ✔ | unchanged | OK as a measurement; "decisive" is editorialising. For 1 orbit L1_GOE=0.1043 is 32% above the GOE control 0.079 — i.e. the single-orbit case is the *worst* fit in the table, yet it carries the headline. |
| T21 | Wall statement: no published pointwise explicit power-saving-in-p bound on `S(a,b)=Σ_{h∈H}e_p(ah+b/h)` for `k < p^{3/7+ε}` exists as of 2026-08-28. Best published: OSV arXiv:2110.10941 Cor. 2.9 for `k ≥ p^{3/7+ε}`. | OPEN GAP (honest) | TH:523-622, L:3794-3803, PA:953-962 | `review/subgroup_kloosterman.md` ✔; `artifacts/ring2/*` ✔ | unchanged | OK as a *negative* claim, but `TH:537-542` misstates OSV Cor. 2.9 as `sup|S| ≤ C·p^{1/2+1/14+ε}·k^{1/2}` valid for `k > p^{1/2+ε}`, whereas `drafts/tail_bound_proof.md:61` and `L:1028-1031` state it as `min{k^{23/36}p^{1/6}, k^{20/27}p^{1/9}}` for `k > p^{3/7+ε}`. Two mutually inconsistent renderings of the same corollary in the same workspace. |

### 1.3 N-series (numerical, run 2)

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| N1 | First-order degenerate perturbation: multiplet splitting = spec(V_λ). At p=3571 (ord 17, m=210, 17 multiplets, 3550 spacings) with matched RMT controls (12 trials): Θ-invariant V → L1(β=1)=0.0796 vs GOE control 0.0792±0.0075 (z=+0.1σ); generic V → L1(β=2)=0.0725 vs GUE control 0.0741±0.0095 (z=−0.2σ). | NUMERICALLY ESTABLISHED, 0.2σ | L:125-140, TH:99-110 | `artifacts/scaling_3571_full.json` ✔, `controls_m210.json` ✔, `theta_symmetry_test.json` ✔, `mode_scan_1597.json` ✔ | z-scores quoted as +0.1/−0.2 at `L:138` but +0.06/−0.17 at `L:527` and `TH:110` | OK. Minor unexplained z-score variance between two statements of the same run. |
| N2 | Diagonalising `U_ε` itself at p=1597: Θ-invariant V gives β=1 within bands (ε=5e-3) and merged (ε=3e-2: L1(β=1)=0.146 vs L1(β=2)=0.322). Generic V gives β fit 1.74 (GUE control 1.71) **with a residual L1 excess — honestly reported as not yet clean.** | NUMERICALLY SUPPORTED | L:142-148, TH:112-116 | `artifacts/floquet_symmetric.json` ✔, `full_perturbed_spectrum.json` ✔ | Opened as O2 (`L:509-511`, `TH:388`); **never closed anywhere in runs 3–70** | OK — model honesty. The open item is silently dropped rather than resolved. |
| N3 | Direct entry-covariance estimate over the multiplet ensemble (p=1597, 34 samples): reality-contraction ratio 0.20–0.21, max cross-correlation ratio 0.39–0.44, against noise floor 1/√34=0.17. | **INCONCLUSIVE — recorded as such** | L:426-435, TH:298-303 | `artifacts/covariance_structure.json` ✔ | Reasoning re-used at F3 (`L:690`) and R49-A | OK — best-practice negative reporting (states the three reasons it is inconclusive, including basis-dependence). |
| F3 | Entry statistics remain Gaussian despite the raw-count explosion: pooled over 13 multiplets at p=521 (10180 entries), complex kurtosis 2.0342 (Gaussian 2.000), real-part kurtosis 2.9975 (3.000). | NUMERICALLY ESTABLISHED → **CONTESTED** | L:640-645 → L:684-690, L:704 | no artifact named | Reviewer measures 6.78–7.94 for A=[[3,1],[2,1]] p=521, seed-unstable 2.37–6.16, band-dependent (→2.20 only for |n|≤10). **DOWNGRADED to [CONTESTED]**; `TH:404-405` states it "is not used anywhere downstream" | OK — correct downgrade. But R49-A (`L:2562-2574`) then re-establishes entry Gaussianity at split primes and the paper uses it (`PA:886-894`) without referencing the CONTESTED status. |

### 1.4 C1 and its successors (the fine-scale conjecture)

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| C1 (v1) | In a Hecke basis the entries of V_λ are Kurlberg–Rudnick/Kelmer/Katz-type exponential sums whose equidistribution gives WD statistics. | superseded formulation, kept for the record | L:448-454 | — | superseded by C1 (v2) | OK — good practice keeping the superseded wording. |
| C1 (v2) | `𝒩_r(N) = #{(nᵢ,jᵢ)∈(F∪−F)^r×(Z/K)^r : Σᵢ A^{jᵢ}nᵢ ≡ 0 mod N}` equals its integral (pairing + F-geometric) count for all `r ≤ C log m`; then the unfolded statistics of V_λ are WD, β=1 iff [Θ,V]=0. **Empirical support: for F={|nᵢ|≤2}, r=4, counts at p=1597 (K=34) and p=3571 (K=17) coincide exactly (311100 vs 124848 pairings) — no mod-p coincidences.** | CONJECTURE | L:437-446, TH:305-313 | the two coinciding counts | **REFUTED (the empirical support) by F1** (`L:618-626`): raw 𝒩₄ is ~99% non-Wigner (p=1597,K=34,B=2: total 7.92e9, Wigner-type 1.51e9); "Run-2's claim 'counts coincide exactly / no mod-p coincidences' is **WRONG as stated** (totals actually 7.92e9 vs 4.95e8)". | CONTRA. `TH:309-311` **still prints the refuted 311100/124848 sentence as "Empirical support"**, with only the header note `TH:11-14` correcting it 300 lines earlier. |
| F1 | Raw solution counts N4(F) for box observables are ~99% dominated by non-Wigner, non-integral families; mechanism = additive energy of H=⟨α⟩ (Shkredov–Stevens territory). | NUMERICALLY ESTABLISHED → REFUTES run-2 empirical C1 | L:618-626, L:702 | `artifacts/n4_general_F.json` ✔ (name not cited in the entry) | unchanged | OK. |
| F2 / C1′ | The moment-relevant object is not the raw count but the **phase-weighted** sum; corrected problem: "phase-weighted non-Wigner solution families = o(Wigner contractions) uniformly for r ≤ C log m". | REFORMULATION / CONJECTURE C1′ | L:628-638, L:703 | — | Superseded by U5′ (`L:1098-1105`) and then declared **structurally unable to see the mechanism** by R7 (`L:1120-1132`): "any burst/counting theory framed purely on resonances (C1′, U5′) cannot see the mechanism that makes moments Wigner." | OK — the abandonment is explicit and well-argued. Three successive conjecture reformulations (C1 → C1′ → U5′) each killed by the project's own numerics; that is healthy. |
| R4 | `N4(F,p,k) = Σ_x A⁺(x)A⁻(x)` (additive-energy factorisation of the 4th-order count), computable in O(k²|F|²+p²) instead of k⁴|F|⁴. | PROVEN | L:613-616, L:700 | brute-force match 10935000 = 10935000 | Red team: "SURVIVES for FIXED sign pattern (+,−,+,−); free-sign reading would differ by 16×" (`L:682-683`) | OK, semantics pinned after challenge. |

### 1.5 Run-3 audit results (A/R series)

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| A1 = R5 | Kernel (1) quantises **Aᵀ**, not A: `U_A T(n) U_A† = ω^{(Aᵀn)₁(Aᵀn)₂/2}·T(Aᵀn)` exactly, for every A with gcd(c,N)=1; with m=An the phase spread is N−1 (fails at O(1)). Exhaustive at N=7,11,13; operator level N=101..4001. | MACHINE-EXACT → REPAIR of T1 | L:553-561, L:701 | `src/indep_check.py`, `indep_check2.py` — both **only in `src/archive/`** | **Itself partially BROKEN** by the run-3 adversarial reviewer (`L:670-674`): the scalar is not `ω^{m₁m₂/2}`; there is an extra quadratic `q_A(n)`, nonzero even for b=c. Proportionality survives (10201/10201 shifts at p=101). Repaired to "up-to-phase" form. | OK — two-stage self-correction, both stages recorded. Exact-integer re-certification at X1 (`L:784-786`) with a negative control. Model behaviour. |
| A2 = R1 | `m_j − N/K = (1/K)Σ_{k=1}^{K−1}(Tr U^k/χ^{k/K})ω^{−jk}`, each term of modulus 1 by T7(v=0). Hence `|m_j − N/K| ≤ (K−1)/K < 1` and `m_j ∈ {⌊N/K⌋,⌈N/K⌉}` ALWAYS; if K|N all multiplicities equal N/K. #{large multiplets} = N mod K forced. Hypothesis: `gcd(p, tr(A)²−4)=1`. | PROVEN + machine-verified; **claimed NOT in prior literature** | L:563-570, L:594-601, L:697 | DFT formula = actual dims to 7e-15 (13 cases, 3 maps); floor/ceil across 19 primes; bound near-tight (p=521,K=58: dev 0.9828 vs ceiling 0.9828) | Reviewer adds CAVEAT: when K>N there are only N<K distinct eigenvalues; conclusion still true with m_j∈{0,1} (`L:678-679`) | OK. Novelty claim ("checked against Kurlberg–Rudnick, Hannay–Berry, Keating, Mezzadri, FNDB") is asserted from abstract-level literature search only — treat as unverified. |
| R2 | Hypothesis necessity: at p | tr(A)²−4 (parabolic reduction, e.g. p=5 for Arnold), A^J−I is nilpotent-singular for even J, T7 FAILS (`||Tr U^J|−1|` up to 10.18 at N=25). So T7/T9/R1 REQUIRE `gcd(N,tr(A)²−4)=1`. "Run 2 never stated this." | PROVEN + machine-verified | L:603-606, L:698 | negative control X6 (`L:788-789`) | unchanged | OK — a negative control that changes the hypotheses of four earlier theorems. Best single audit action in the corpus. |
| A3 = R3 | `Σ_λ Tr(V_λ^r) = Tr(V̄^r) = N·a_r` EXACTLY (machine-zero, r≤4) because `Σ_λ P_λ = I`; per multiplet `Tr V_λ^r = (N/K)a_r + O(C^r)` (worst observed dev/bound = 0.015). | EXACT identity / PROVEN | L:572-576, L:608-611, L:699 | re-verified ≤3.2e-15 over three observable types; `P_λV̄P_λ = P_λVP_λ` independently verified | unchanged | OK |
| A4 | Independently confirmed with fresh code: torsion; Θ anti-unitary incl. non-symmetric A (1e-15, |scalar|=1); unimodularity incl. v=0; cancellation `|E| ≤ (K−1)/K` uniformly incl. u=0; tight-frame identity machine-exact (3e-15, own orbit enumeration). | Confirmed independently | L:578-581 | fresh implementations | unchanged | OK |
| Traps | (i) `U_G U_H = s·U_{HG}` is an **ANTI**-homomorphism (|s|=1 ≤1e-15) — derivations treating U_A as multiplicative are wrong. (ii) LAPACK returns non-orthogonal eigenvectors inside degenerate clusters (‖W*W−I‖ ≈ 4e-2) — re-orthonormalise per cluster. | recorded | L:691-694 | — | (ii) recurs as the v5 `cluster_eigs` failure at tol=1e-6 (`L:3916-3920`) — the same trap bites again 60 runs later | OK to record; poor to re-hit. |

### 1.6 M1 master moment formula (run 4) and r=5/r=6 extensions

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| M1 | For every finite-frequency Hermitian V, every r≥2, every multiplet: `Tr(V_λ^r) = (N/K)a_r + (1/K)Σ_{J=1}^{K−1}λ^{−J}S_J` with `S_J = K^{−r}Σ_tuples (Πcoeff)·ζ^{Σεᵢ Q_{jᵢ}(nᵢ) + Σ_{i<l}Ψ_d(gᵢ,g_l)}·ρ_J((Σgᵢ) mod N)`, B=Aᵀ, gᵢ=εᵢB^{jᵢ}nᵢ, ζ=e^{πi/N}, `Ψ_d(g,h)=(N+1)(g₂h₁−g₁h₂) mod 2N`, `ρ_J(v)=Tr(T(v)U^J)/Tr(U^J)` (|ρ|=1 by T7, used as an exact table). | PROVEN + machine-verified 1e-14…1e-16 | L:715-745 | `artifacts/master_formula.json` ✔, `src/master_formula.py` ✔; ALL PASS r=2,3,4 × {Arnold,[[3,1],[2,1]]} × {101,199,521} | Re-verified R40 (`L:2306-2308`) and R54 Phase 0 (`L:2833-2836`). Vectorised in R53 (`L:2808-2822`). | OK. Note the honest structural admissions: ρ_J is **not** globally quadratic (`L:736-739`), and the Weyl convention must match exactly or "a sign/convention slip breaks everything" (`L:733-736`). |
| M1 consequence | `θ_r := Tr(V_λ^r) − (N/K)a_r` is EXACTLY the phase-weighted resonant sum ⇒ the whole fine-scale problem is cancellation in those sums (C1′ made exact). Observed `|S_J|/mean-field-count ~ 1e-2…1e-4`. | (implicit PROVEN) | L:747-761 | as M1 | unchanged | OK |
| M1 at r=5 | Three configs, three λ-branches each: [[7,3],[2,1]]@71 (split,K=5) err ≤4.2e-17; Arnold@233 (INERT,K=26) ≤1.4e-16; Arnold@101 (split,K=25) ≤3.5e-16. Three bugs found and fixed (B1 raw ρ exponents; B2 flat cyclotomic index assembled from separately reduced components; B3 projector normalisation applied twice/not at all). | OPEN GAP CLOSED / PROVEN | L:977-994 | `artifacts/m1_run5.json` ✔ — **I verified: contains exactly these 3 configs, `all_pass: true`, `implementation: src/m1_r5.py`** | **Red team C5** (`review/redteam_run5.md` §C5) states `m1_run5.json` contains ONLY the failed config with `passed:false` and "there is no evidence that everything else passes at r=5 … **All of r=5 is unvalidated**". The file was overwritten in place by R6.1, destroying the red team's evidence. | **CONTRA + provenance destroyed.** Both statements cannot be true of the same filename. The artifact was mutated in place rather than versioned. Then, two runs from the end, `TH:474-521` and `PA:944-952` **demote** r=5 to "ONE pass (Arnold @ N=101)" — ignoring the 3 passing configs (incl. an inert prime) sitting in `m1_run5.json`. See §5/S-5. |
| thm:r6 (v1) | `sol6 = 5k(3k²−9k+8)` for EVEN k; strata identities `[6]=k`, `[2,4]=9k(k−1)`, `odd-[222]=6k(k−1)(k−2)`, `[1113]=18k(k−2)`. | THEOREM (verified exact at 5 points) | L:2513-2516 | `artifacts/phase3_r6.json` ✔ | **RETRACTED → replaced** at R49-A (`L:2576-2579`): counterexample (241,30) gives sol6=417900 vs skeleton 365700. Replaced by `Prop strata + Conj skeleton + excess A_p(k) ≥ 0` (`PA:668-712`). | OK — retraction executed, paper updated. |
| R16/R22–R25 r6 data | Sixth-order counts and family decompositions across (p,k) ∈{101,211,401}×{3..25}; "ratio sol_6/k³ approaches ~15 for large EVEN k"; families at k=4 (C:negpair 64, M:aan 48, other 288). | NUMERICALLY-SUPPORTED | L:1792-1810, L:2011-2030, L:2032-2038 | `artifacts/run16_r6.json` ✔, `run22_classify.json` ✔, `run25_partition.json` ✔ | **RETRACTED at R48 Phase 3** (`L:2508-2512`): "SIGN BUG found in all prior r6 brute force (right-hand sums inverted ⇒ wrong system). Affects R16/R22–R25 numeric claims → RETRACTED (even-k totals coincidentally survived via −1-in-H symmetry; family decompositions were wrong)." | OK — retraction is explicit and names the surviving/dying parts. But the retracted blocks at `L:1792-1810`, `L:2011-2030` carry **no in-place warning** (unlike R10-B, which got one). |
| R63 3\|k closed form | `sol6 = 15k³−5k²−170k` for 3\|k (fit on k=6,12,18,24). | (implicit claim) | L:3474-3484 | `artifacts/sol6_closed_form.txt` ✔ | **REFUTED same entry**: mismatch at k=30 (417000 vs 395400, +5.5%), k=30 p=211 (422400, +6.8%), k=36 (719640 vs 687240, +4.7%). "The 4-point fit was a coincidence." | OK — a 4-point polynomial fit refuted by extending the sweep. Correctly labelled a coincidence. |
| N1(k) micro-formula | `N1(k) = (k/2)(k/2−1)(k/2−2) = 6·C(k/2,3)`, exact fit 6/6 on {10:60,14:210,16:336,20:720,22:990,26:1716}. | (fit) | L:2665-2672 | `artifacts/phase3_pair_classifier.json` ✔ | First printed wrong as `C(k/2,3)` (`L:2656-2657`), corrected within the same run (`L:2665-2672`); then **a second switch found**: config (311,20) gives N1=0, "dead configs" (`L:2681-2684`) | OK — immediate self-correction, explicitly logged as such. |

### 1.7 Run-5 order-4 structure theory (U-series) and the campaign

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| O6 / R5.1 | R reversing involution ⇒ traceless ⇒ M=SR has a_M=d_M=p; then `Q_M(x,y)−Q_M(y,w) = icb[p(x²−w²)+2y(w−x)]` is LINEAR in y, so the y-sum vanishes off-diagonal and equals N on it: `U_M conj(U_M) = I` exactly, `Θ²=+1` identically. "No Weil cocycle needed. Only β=1,2 occur — **unconditional, elementary**." | PROVEN | L:792-800 | analytic, in situ | **DOWNGRADED-scope in the same run** (`L:888-893`): "theorem holds for reversing involutions with `gcd(M₂₁,N)=1` (kernel hypothesis). `theta_sign.py` silently skipped c==0 mod N cases — gap aligned between proof and numerics." Red team C1 is the source. | OK that it was caught; **NOT OK** that the "unconditional, elementary" sentence at `L:800` was left standing verbatim above its own downgrade 90 lines later. |
| U1 | Every fibre of `Φ(x,y)=(a₁x+a₃y, b₁/x+b₃/y)` on H² has ≤2 points (one quadratic in x). Generalises T17 beyond single-orbit. | PROVEN + machine-checked | L:831-833 | `src/archive/fine_r4_struct.py` ✔ | **BROKEN as stated** (red team C2): with a₁=a₃=0 and (b₁,b₃)=(1,2) at p=113, k=14, max fibre = **5**, growing ~k. Cause: `fine_r4_struct.py:127` draws coefficients from `rng.integers(1,p)` so zeros are impossible by construction — "the check verifies the generic case only, giving false confidence in a lemma stated without the needed hypothesis." Hypothesis added 2026-08-28 (`TH:416-434`, `PA:244-249`). | CONTRA-then-fixed, but note the fixed version at `PA:248` adds a **fifth** condition `a₁b₃ ≠ a₃b₁` that the red team never asked for and that `TH:419` does **not** list — the paper and THEORY now state different hypotheses for the same lemma. |
| U2 | `C(u,v) := #{(h,h′): h−h′=u, h⁻¹−h′⁻¹=v} ≤ 4` for (u,v)≠(0,0) (hh′=−u/v forced). Measured max = 1. | PROVEN + machine-checked; **Lean-formalised** | L:834-835, L:1011-1023 | `BgsFormal.lean` (namespace BgsU2: `prod_eq`, `sum_sq`, `same_S_swap`, `S_distinct`) at `C:\lean\bgs_formal` — **DIRECTORY DOES NOT EXIST** | Sharpened to **C ≤ 2** by the 2026-08-26 audit via `h′ = h−u` substitution, formalised as `BgsAudit.collision_card_le_two`; "paper states ≤4; slack harmless" (`L:2756-2760`) | **DANGLE.** The single "PROVEN (Lean-formalised)" tag in the paper (`PA:923`) points at a filesystem path that is absent. The counting corollary (≤4 solutions) was **never** formalised — "documented as the routine finite bookkeeping step" (`L:1019-1021`), then `card_le_four_draft` never compiled (`L:1386-1394`, `L:2760`). |
| U3 | `#solutions(S_F) = Σ_{σ,τ} R_L(σ,τ)R_R(σ,τ)`; EXTRAS = intersection mass of the images `im_L, im_R ⊂ F_p²` of two 2-to-1 maps. | PROVEN + machine-checked | L:836-838 | brute == decomposed re-verified (red team) | unchanged | OK |
| U4 | Conditional: if `sup_{(r,s)≠0}|Σ_{h∈H}e_p(rah+sb/h)| ≤ k p^{−δ}` uniformly, then character orthogonality on H⁴ + Cauchy–Schwarz with the ℓ² table identity gives `extras ≤ 5k⁴p^{δ−2}`, i.e. relative 4th-moment error `O_F(k²p^{δ−2}) = o(1)` whenever `k ≤ p^{1−δ/2−ε}`. | PROVEN conditional | L:846-855 | — | **THREE successive corrections.** (a) `L:896-902`: red team corrects the ℓ² identity to `Σ|S|² = p²k` (diagonal only; the collision-count version was wrong) and restates as `extras ≤ k³p^{−2δ}`, `o(1) iff k ≪ p^{2δ}`. (b) **The red team's own report says otherwise**: `extras ≤ k⁴p^{−2δ}` and "usable threshold collapses to `k ≲ p^{δ}` — **vacuous** for any published δ … U4 downgraded to *conditional sketch with incorrect quantitative conclusion*". (c) `TH:436-472` + `PA:929-935` (2026-08-28) enshrine version (a) as "RED-TEAM-CORRECTED". | **CONTRA — live.** The paper's status table asserts a bound the red team explicitly says does not follow, and labels it with the red team's authority. Numerically: red team computes, at the repo's own scale (k=14,p=113,δ=0.005), corrected ceiling ≈3.7e4 vs printed 15.4 — "**2400× too strong to follow from the stated inputs**". See §5/S-3. |
| U5 | `|im_L ∩ im_R \ pairings| ~ k⁴/(2p²)`. | CONJECTURE, discriminated | L:856 | — | **REFUTED** at R6.7 (`L:1090-1096`): for random generic tuples the images do not intersect at all once k²/p grows (κ=0 identically for k≥128 at k²/p ≤ 2); nonzero cases are rare heavy-tailed bursts. Replaced by U5′. | OK — clean refutation of the project's own conjecture. |
| U5′ | Non-pairing 4th-order solutions exist only on measure-sparse structured label-overlaps; total mass Poisson-bursty with mean ~κk⁴/p², κ∈[1,5]; each burst capped per collision type by U2 (≤4). | NUMERICALLY ESTABLISHED shape | L:1098-1105 | `artifacts/image_intersection.json` ✔, `image_intersection_overlap.json` ✔; SELF-case anchor `T_self = 3k²−3k` EXACT at every grid point | Declared **structurally unable to see the mechanism** at R7 (`L:1120-1132`) | OK. The anchor check against the proven T17 branch (and the admission "my 'cap 2k²' guess was the wrong branch") is good practice. |
| R7 burst finding | Resonant non-Wigner tuples outnumber Wigner tuples 50×–500× at multi-frequency; phase kill is partial and unstable (46%–99.7%); the proxy `|Φ_burst|` exceeds the TRUE θ₄ by 10³–10⁷. ⇒ fine-scale cancellation is NOT visible inside the resonance frame; the working object must be the COMPLETE per-J character sums. | NUMERICALLY ESTABLISHED, structurally decisive | L:1109-1139 | `artifacts/phase_bursts.json` ✔, `theta4_decomp.json` ✔, `burst_split.json` ✔ | Confirmed by R7.2 and R8 | OK. Lesson L11 (`L:1136-1139`) is the best methodological statement in the corpus. |
| R7.2 / R8-A / R8-B | Median over J of `|S_J|/meanfield` is 25×–4000× below the coherent bound across 7 configs (split, inert, symmetric, non-symmetric, mono/multi-frequency); random-(a,b) stress test at p up to 1.7e7 in three regimes k~p^{1/4},p^{1/3},p^{1/2}: max/√k = 3.44/3.98/3.48 (Gaussian max for n=2500 ≈3.9), median 0.67–0.68, q95≈2.0; structured families b=±a, ab=1, monomials all ≤5.21√k. NO SPIKES. | NUMERICALLY ESTABLISHED | L:1150-1161, L:1177-1197 | `artifacts/sj_sqrt_scaling.json` ✔, `s_sqrt_stress.json` ✔; scripts `review/run7_debug/sj_scaling.py`, `sj_scaling_ext.py` **MISSING** | unchanged | DANGLE (scripts). The measurement is the strongest positive evidence in the corpus for the sqrt-cancellation hypothesis and its generating code is gone. |
| R9 / R9-B / R9-E | Character-expansion reduction: `1_H = (k/(p−1))Σ_{χ:χ^k=id}χ`; every S_i becomes a twisted 2-variable Kloosterman sum = trace function of the universal Kloosterman sheaf; `#sol(S_F) = p^{−2}[k⁴ + (k/(p−1))⁴ Σ_{χ⃗} C_χ]` with `C_χ` an FKM-type correlation sum of four rank-2 sheaves. Predicted dichotomy (no cancellation exactly on the label-overlap/Wigner locus, strong cancellation off it) confirmed exactly at p=4099: factor 1.0 (degenerate) vs 37.3× / 58.7× / 30.0× / 21.4×. | PROVEN, machine-exact (after 3 rounds) | L:1222-1264, L:1266-1277, L:1324-1338 | `artifacts/cchi_exact.json` ✔, `char_expansion_cert.json` ✔ (`all_pass`, rel_err 2.1e-16…4.7e-15 — I verified the keys) | Residual 3e-3…3.6e-2 (R9-C) → localised to the (u,v) reparametrisation (R9-D) → **root cause: the aggregation dropped the axes (u,0),(0,v) where `Ktilde(χ;t,0)` are Gauss sums ~√p** (R9-E). Re-verified R40 (`L:2310-2312`) and R54 (`L:2833`). | OK — this is the best debugging chain in the corpus: three entries, each narrowing, ending in an analytic root cause plus machine-exact certification. |

### 1.8 The R9-T/R10/R11 theorem and its retraction (the largest failure)

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| R9-T main theorem | 4th moment of compressions matches WD up to absolute error `O(p^{3/2})`; relative fine-scale error o(1) whenever `k ≫ p^{3/4+ε}`. **UNCONDITIONAL** — Deligne RH for the multihomogeneous complete intersection replaces the Katz-tier hypothesis entirely. | (claimed unconditional) | L:1340-1352 | `drafts/bgs_note_run9_theorem.tex` — **FILE MISSING**; `artifacts/deligne_check.json` ✔, `deligne_check_ext.json` ✔ (I verified: 12 cases, ratios 0.125…1.936) | Single "precision obligation" declared (the p^{3/2} exponent) then **CLOSED** at R10 (`L:1363-1367`) by adding "Proposition prop:count with full weight-bookkeeping proof (Deligne Weil-II on the smooth complete-intersection surface; b₃ ≤ 64 explicit)". Superseded by R11, then retracted by R12-A. | **VOID + DANGLE.** The document containing the alleged proof is not on disk. A theorem whose write-up cannot be inspected cannot be audited; the ledger's claim that its "precision obligation is CLOSED" is unverifiable. |
| Smoothness hypothesis | Smoothness of the variety in `prop:count` verified on instances: 600 sampled solutions at p=2053/4099 zero singular; extended to 800+ across 5 primes, ZERO singular. | verified on instances | L:1364-1366, L:1499-1504 | `artifacts/smoothness_check.json` ✔, `smoothness_ext.json` ✔; script `smooth_ext.py` **MISSING** | Paper adds `rem:smoothconditional`… which is about something else entirely (the OSV tail law), so this obligation is **not** carried into the paper | DANGLE. "Generic smoothness confirmed at every tested instance" is sampling, not a hypothesis check — correctly worded, wrongly weighted ("Hypothesis of Proposition prop:count is solid"). |
| R11 "THE BREAKTHROUGH" | The TRIVIAL bound `|T| ≤ p²k⁴` suffices to prove fine-scale WD matching at order 4 whenever `k⁶/(2p⁴) → 0`, i.e. `k = o(p^{2/3})`. "The previously identified barrier at p^{3/4} was an artifact of insisting on pointwise exponential-sum bounds." | (claimed) | L:1414-1426 | — | RETRACTED (R12-A) | VOID |
| R11 FORMAL THEOREM 6 | A∈SL(2,Z) hyperbolic, p prime, gcd(p,tr(A)²−4)=1, α split eigenvalue of order k, H=⟨α⟩, V finite-frequency Hermitian: `|Tr[(P_λVP_λ)⁴] − WD₄(V,Θ)| ≤ C_F·k⁸/p²`; 5-step proof chain; relative error ≤ `k⁶/(2(p−1)⁴)`. | **PROVEN, unconditional** | L:1428-1446 | numerics: error/pairing_mass 3.28e-08 … 1.23e-07 at campaign primes; 4.8e-3 at p=101,k=10 | **RETRACTED, R12-A** (`L:1558-1594`): (1) double-counted `(k/(p−1))⁴` prefactor between the two formulations ⇒ fake threshold and fake error bound; (2) inconsistent exponents across statement/proof/relative error (`k⁸/p²` vs `k⁸/p⁴` vs `k⁶/p⁴`); (3) OVERCLAIM "BGS at order four" without a local law; (4) claimed coverage of "all physically relevant k" false since typical ord_p(A) ~ p is **outside** `k=o(p^{2/3})`. | VOID. Correctly and thoroughly retracted, with an in-place warning box added 2026-08-28 (`L:1399-1412`) — the **only** in-place retraction warning in the whole ledger. |
| R11 "COMPLETE proof of BGS at order four" | Combining Θ symmetry class + Birkhoff density + rigidity + 5th moment "constitutes a COMPLETE proof of Bohigas–Giannoni–Schmit at order four for quantised cat maps in the physically relevant regime." | (claimed) | L:1456-1470 | — | RETRACTED (R12-A item 3) | VOID |
| R11-C all fixed even orders | At order r the trivial bound gives `|T| ≤ p²k^r`, extras `≤ k^{2r}/p²`, relative error `≤ k^{2r−2}/(2k^{r/2}) → 0` whenever `k=o(p^{1/(r−1)})`. "= Bohigas–Giannoni–Schmit at the level of all fixed-moment statistics." | (claimed theorem for each fixed r) | L:1481-1497 | — | RETRACTED (R12-A, second bullet at `L:1861-1862`? — no: the retraction is generic at `L:1607-1609` and named in the standing list `L:3861-3862`) | VOID. Note this claim **directly contradicts T18-barrier** (`L:369-377`), proven 1100 lines earlier, which says the number of usable moments is capped at 2/θ. Nobody noticed the contradiction at the time. |
| R11-D | `theorem_verify.py` (sign-corrected): ALL 7 cases show `sol == pairings` exactly (p=101: k=2(6),4(36),5(45),10(270); p=4099: k=2(6),3(15),6(90)). Earlier "sol=0" was a SIGN BUG in the brute force. | ALL MATCH | L:1530-1538 | `artifacts/theorem_verify.json` ✔, `theorem_verification.json` ✔; `src/archive/theorem_verify.py` ✔ | unchanged | OK. Third independent sign-bug in this codebase (also R48 Phase 3, R11-D, and the `find_orbit_H`/`proj_order` family) — a systemic weakness, never addressed as such. |
| R12-A corrected theorem | `Tr(V_λ⁴) = WD₄(V,Θ) + O_F(k⁴/p²)`, valid for ALL admissible (p,k) with **NO** threshold on k. Model term (fully matched labels) `sol == #WD-pairings` EXACTLY. Other label patterns contribute `O_F(k⁴/p²)` or 0 — "**needs separate collision/fibre argument, NOT trivial |Sᵢ|≤k**". Local law still open ⇒ do NOT call this BGS yet. | (correct statement to state) | L:1578-1585, L:1604-1605 | `artifacts/grok_identity_check.json` ✔ (I verified: 15 cases, all `match`); `drafts/bgs_note_run12_corrected.tex` — **FILE MISSING** | `TH:599-604` and `L:3798-3803`/`ROADMAP.md` later assert "the BGS-relevant component is **proven unconditionally at fixed order r ≤ 4**" | **DRIFT + DANGLE — live.** R12-A itself says the non-matched part "needs a separate collision/fibre argument", i.e. is **not proven**; the paper's own `cor:domination` (`PA:593-612`) is explicitly **conditional on conj:tight**. Yet THEORY §8.0.3 and the paper status table (`PA:957-958`) now call r≤4 unconditionally proven. See §5/S-1. |
| R12 deliverables | `src/master_general.py` general-r iterative + MITM master formula verified 1e-15 on r=2,3,4 across multiple configs. | ALL PASS | L:1596-1605 | `artifacts/master_general.json` ✔ (I verified: 5 runs — r=2,3,4,4,5, all `passed:true`) | r=5 added R53 (`L:2808-2822`) | OK |

### 1.9 R13–R31: the "arithmetic beats symmetry" episode and the perturbation route

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| R13-A | For A reversible but `k=ord_p(α)` ODD (−1∉H): symmetry prediction (Θ exists ⇒ GOE) gives 3k(k−1); arithmetic prediction (parity of k) gives 2k²−k; ACTUAL count = 2k²−k. Confirmed A=[2,1,1,1] at p={101,199,211}, A=[5,2,2,1] at p=199. ⇒ "This REVERSES our earlier claim that Θ² determines the class." | NUMERICALLY-SUPPORTED (4 cases) | L:1624-1661 | `artifacts/run13_phase23.json` ✔; `mechanism_winner.py` **MISSING** | Survives as the paper's `rem:rev`/`rem:shadow` (`PA:337-341`, `PA:363-374`). The stronger "quantum" version was retracted (next row). | OK, and the framing is right: the resonance-count switch is arithmetic. But `L:1655-1660` ("Earlier claim 'class determined by Θ²=±1' is **WRONG** for the fourth moment … Paper rewrite needed: replace all references to Θ as class determinant") **overstates**: T13/T3 concern the Dyson class of the *operator*, not the pairing count of one moment. Two different statements; the ledger treats them as contradictory. |
| R13 quantum experiment | `src/run13_quantum_w4.py`: Tr(W⁴) for W = V_λ − μI in 12 instances across 4 (A,p) pairs; 12/12 closer to GUE-Wick than GOE-Wick ⇒ "the arithmetic switch SURVIVES quantisation. Title 'Arithmetic Beats Symmetry' is justified at both resonance-counter and quantum-moment level." | NUMERICALLY-SUPPORTED (12/12) | L:1695-1713 | `artifacts/retracted/run13_quantum_w4.json` ✔ (correctly filed under `retracted/`) | **RETRACTED at R34** (`L:2235-2239`, `L:2255-2256`): "Used non-Hermitian V (T10 + 0.7·T01 without daggers), giving negative Tr(W²) — impossible for a Hermitian matrix. Comparison with GOE/GUE Wick values was meaningless." Redone with Hermitian V: discrimination impossible at all tested m; measured TrW⁴ **exceeds both** simulations. Removed from the paper at R47 (`L:2445-2447`). | VOID — exemplary retraction (artifact moved to `retracted/`, paper text excised, lesson recorded). |
| R14-A | For every nondegenerate unmatched label pattern, `sol(a,b) ≤ C·k` with absolute C (empirically 6); `sol = k·N₃`, `N₃ ≤ 6` always; Schwartz–Zippel gives `N₃ ≤ 4k` unconditionally. "FAR STRONGER than O_F(k⁴/p²) which was Grok's guess." | NUMERICALLY-SUPPORTED (p≤809, k≤101) | L:1721-1747 | `artifacts/run14_Ok_test.json` ✔, `run14_unmatched_scan.json` ✔, `run14_degeneracy.json` ✔ | **SUPERSEDED 4 times**: R15 `sol ≤ C·max(k,k⁴/p²)`, ratio ≤16 (`L:1776-1790`); R17 `N₃ = Θ(k²/p)` (`L:1853-1874`); R19 `N₃ ≤ C·k²/p`, C≈2 (`L:1881-1905`); R20 `N₃ ≤ ⌊k²/p⌋+1` with "no slack observed" (`L:1907-1925`); R37 `⌊k²/p⌋+2` after **10/196 violations of +1** (`L:2280-2295`). | OK as a sequence of honest refinements, but note the rhetorical pattern: each version is announced as "BREAKTHROUGH"/"TRUE SCALING LAW"/"TIGHT" and then falsified by the next scan. R20's "constant exactly 1 (no slack observed)" was falsified within 17 runs. |
| conj:tight (final form) | For every **generic** unmatched pattern (no slot-pair or cross proportionality), `N₃(a,b) ≤ ⌊k²/p⌋ + 2`. | NUMERICALLY-SUPPORTED | L:2287-2295, PA:448-458, PA:968-971 | `artifacts/run36_audit.json` ✔ — **I re-computed: 196 configs, 10 violations of ⌊k²/p⌋+1, 0 of +2, max maxN3=44, k≤373, p≤1499**; `run20_constant.json` ✔ (42 configs, k 5–682, p 379–2729); `audit_conj_tight_extended.json` ✔ (25 configs, 800 trials, `violations: []`, k 4–25, p 101–2003) | Config counts quoted inconsistently: "~230" (`PA:512`, README), "~293" (`L:2884`, `PA:969`), "28 configurations" for run20 (`L:1909`) vs 42 in the file, "k ≤ 30" (`L:2870`) vs k ≤ 25 in the file | OK on substance — this is a genuinely well-tested conjecture, correctly tagged NUMERICALLY-SUPPORTED everywhere. Config bookkeeping is sloppy but never in a self-serving direction beyond ±20%. |
| conj:unified | Genericity may be unnecessary: for **every** non-Wick-compatible pattern, `N₃ ≤ ⌊k²/p⌋+2`. Would subsume the unwritten degenerate-strata lemma of `cor:domination`. | NUMERICALLY ESTABLISHED, decisive → CONJECTURE in paper | L:2786-2799, PA:460-488 | `artifacts/audit_degenerate_strata.json` ✔; ladder p∈{1009,2003,4001,8009}, k≤364, ρ=k²/p∈{1,4,16}, 250 instances/cell, 7 classes; means match `k³/p²` per class; WICK class gives exactly Θ(k) | `artifacts/audit_strata_rho{1,4,16}.log` — **MISSING** (cited at `L:2800` and MANIFEST `:79`) | OK, well designed (includes the sharpest near-Wick edge WICK3Q). DANGLE on the logs. |
| R20 addendum | Degenerate patterns break the bound: all-equal labels give N₃=27 ≫ k²/p+1 ≈ 2 at p=101,k=10; proportional forms the same. Bound applies ONLY to generic patterns. | CONCLUSION | L:1927-1944 | in-run test | unchanged | OK — a self-imposed counterexample that scopes the conjecture. Good. |
| thm:meanlaw / R46 | `Σ_{(a,b)∈G⁸} N₃(a,b) = k³[(p−1)(p²−3p+3)]²`, hence `⟨N₃⟩ = k³(p²−3p+3)²/(p−1)⁶ = (k³/p²)(1+O(1/p))`. Proof: double counting + Lemma zerocounts. Degenerate patterns have relative measure O(1/p). | **PROVEN** (fully rigorous elementary proof) | L:2402-2438, PA:542-565 | `artifacts/run46_exact_mean.json` ✔ (5 configs, all \|z\|<1.5 — I verified fields p/k/trials/mc/exact/z); `src/verify_mean_law.py` ✔ (re-run R65: 5/5, max\|z\|=1.47) | Verified again by independent suite V3 (complete label enumeration for p∈{5,7}) | **OK — the single best-supported new result in the corpus.** Proof is 6 lines, checkable, correct. Preceded by an honest note that an initial p=5 "failure" was a test bug (coefficient −5 ≡ 0 mod 5) — `L:2417`. |
| lem:zerocounts | For `c₁,…,c_n ∈ G=F_p^×`, the number of solutions in G^n of `Σcᵢxᵢ=0` is `Z₂=p−1`, `Z₃=(p−1)(p−2)`, `Z₄=(p−1)(p²−3p+3)`, independently of the coefficients. | PROVEN | L:2414-2418, PA:523-540 | `review/scripts/run45_lemma.py` ✔; brute force p∈{5,7,11,13}; independent suite V2 8/8 primes; Julia key | unchanged | OK. Trivial but correctly stated and correctly credited as elementary. |
| R21/R26/R28/R29 | Direct spectral tests of the raw compression fail: KS to semicircle 9.2–9.4 at m={5,11} (W not Hermitian in general — invalid comparison, acknowledged); 7.26 at m=11 with Hermitian V; at p=2207, m=69: moment ratios ρ_m/Catalan = {3.6,15,64}; singular values span FOUR orders of magnitude (1.61 → 4e-5). ⇒ "Compressed cat-map operators carry ARITHMETIC HIERARCHY … This is NOT random-matrix behaviour. Raw cat maps remain COUNTER-EXAMPLES to naive BGS at these parameters." | NEGATIVE RESULT (honest) | L:1964-1982, L:2093-2126, L:2128-2160 | `artifacts/run21_spectral.json` ✔, `run26_resolvent.json` ✔, `run28_bigm.json` ✔, `run29_moments.json` ✔ | Confirmed at split primes too (R49, `L:2540-2542`); becomes the paper's "Scope limitation" (`PA:651-658`) | **OK — the most important negative result after T18.** It kills the naive programme and is reported without hedging. Note it flatly contradicts the T9/T10/T17/T19 rhetoric ("the compression is already a Wigner matrix at the level of entry statistics", `L:228-229`). |
| R30/R31 lem:perturb | Under the perturbation flow (additive at R30/R31, unitary `U_ε=e^{iεE}U_A` from R48), first-order degenerate PT gives phase shifts = eigenvalues of `P_λEP_λ`; for E~GUE(N) this compression is exactly GUE(m) by unitary invariance; hence unfolded intra-multiplet spacings → GUE spacing law as m→∞ with `ε‖E‖/δ_* → 0`. | **PROVEN (sketch)** | L:2200-2224, PA:749-790, PA:977 | proof sketch only (Kato + unitary invariance) | Wording fixed ("spacing law of the GUE", not "surmise") at `L:2752` | OK, and honestly tagged "(sketch)" in the paper status table. The mathematics is standard and almost certainly correct; it is also **nearly vacuous as evidence for BGS** — it says a GUE perturbation produces GUE statistics. The paper concedes this (`PA:96-99`). |
| exp:multi | 4 primes p∈{1597,2161,2207,3001} (m≈47–69), ε=1e-4, Hungarian matching, per-prime KS on the pooled 3 largest multiplets: KS_WD = 0.0638/0.0672/0.0689/0.0756, KS_Poisson ≈ 0.28 for all. All below the 5% critical ≈0.096. | NUMERICALLY-SUPPORTED 4/4 | PA:792-829, PA:978-979 | `artifacts/unitary_perturbation.json` ✔ — **I verified these four KS values exactly** | **R31's own numbers were different and one FAILED**: `artifacts/run31_multiprime.json` (I verified) gives KS_WD = 0.0665/0.0727/**0.1343**/0.0950 and R31 nevertheless labels all four "[WD]" (`L:2204-2207`). 0.1343 > 0.096. | **CONTRA (uncorrected).** R31's 4/4 "WD" verdict is false by the project's own critical value. The paper silently substitutes the unitary-flow artifact. `artifacts/MANIFEST.md:27` still maps the paper's claim to `run31_multiprime.json` — i.e. the manifest points the reader at the superseded, partially-failing artifact. |
| exp:beta | Three further primes (3571,4481,5779), n=13723 pooled spacings, MC references at the observed multiplet dims (397800 refs each): `KS_GOE=0.0676`, `KS_GUE=0.0099`, gap 0.0577 ≫ crit 0.0118. ⇒ **DATA ARE GUE, GOE EXCLUDED**, as lem:perturb predicts for a GUE perturbation. | RESOLVED | L:2501-2507, PA:831-850, PA:980-981 | `artifacts/phase2_beta.json` ✔ (keys `ks_vs_goe/ks_vs_gue/gap/crit/resolved` verified); `phase2_spacings.npy` — **MISSING** | K-labels were wrong (halved) and were fixed by the 2026-08-26 audit (`L:2739-2741`) | OK on statistics. Circular as physics: a GUE perturbation is *designed* to give GUE, so "β resolved" resolves nothing about the cat map. The paper is careful about this; the LEDGER's "** DATA ARE GUE, GOE EXCLUDED **" framing is not. |
| R35 | At n=138–204 the KS statistic **cannot** distinguish GOE from GUE surmises (critical ≈0.096); GUE-pert gave 3/4 cases closer to the GOE surmise. Qualitative "WD not Poisson" survives. | CONCLUSION (honest) | L:2263-2278 | `artifacts/run35_surmise.json` ✔ | Carried into the paper (`PA:824-828`) | OK — a self-limiting statement, correctly propagated. |
| R49 arithmetic perturbation | Replacing the Gaussian E by an arithmetic Hermitian Weyl combination does **NOT** produce WD: p=2207 (n=2175) KS_GOE=0.210/KS_GUE=0.279; p=4481 (n=4417) 0.147/0.200 — far outside the RMT class (vs 0.0099 for the Gaussian flow). Heavy-tail hierarchy holds at split primes too. | NEGATIVE RESULT | L:2528-2547 | `artifacts/arithmetic_perturbation.json` ✔, `check_split_vs_inert.json` ✔ | Becomes `op:local` in the paper (`PA:868-909`) | OK. This is the honest core of the remaining gap: "unconditional local law requires Hecke-type symmetrisation, NOT a deterministic swap of the random input. **Obstruction now measured, not conjectured.**" |
| R49-A | At split primes 4481 (m=71) and 3571 (m=211): off-diagonal entries of `P_λV_arithP_λ` are Gaussian (kurtosis −0.14…0.07, KS p 0.25–0.83); diagonal Gaussian at m=71, heavier (3.24) at m=211; eigenvalues show heavy outliers (excess kurtosis 5.9/9.3, `|λ|max/std ≈ 3.8/5.0`). ⇒ **entry Gaussianity already holds; what fails is DECORRELATION.** | CONCLUSION (sharp) | L:2562-2574 | `artifacts/taskA_entry_gaussianity.json` ✔ — **I verified all six numbers (−0.138, −0.109, −0.176, 3.242, 3.82/4.98, 5.902/9.347)** | Cited correctly at `PA:886-894`. **Mis-cited** as "max/median ≈ 15–40" at `L:3255`, `L:3334`, `L:3376`, and — still today — at `PA:881`. | OK as a measurement; see §3/RET-9 and §4/D-2 for the fabricated derivative number. |
| R52 phase-III correlation probe | "mean \|ρ\| between row-sharing entries = 1.0000 vs GOE baseline 0.1187 ⇒ near-perfect real-linear dependence inside rows." | measured signal (replication pending) | L:2689-2693 | `artifacts/phase_corr_probe.json` ✔ | **REFUTED by R52b same session** (`L:2704-2715`): the statistic (`corrcoef` on 2-vectors (Re,Im)) has E\|ρ\|~0.8+ for ANY two complex Gaussians — the 0.119 baseline was the wrong null. Proper test (Spearman on magnitudes): ρ=0.0736 ≈ 0 (n=579). | OK — false discovery caught and killed within the same session by a pre-committed replication mandate. This is the single best process moment in the corpus (`L:2714-2715`). |

### 1.10 Runs 53–70: audit, wall attack, and the Hecke-collapse claims

| ID | Statement | Status | Stated at | Evidence | Later fate | AUDIT |
|---|---|---|---|---|---|---|
| `op:tail` smooth law | `N₃ ≤ k²/p + √k` at **unit constant C=1** is **PROVEN for `k ≥ p^{3/7+ε}`**, by inserting OSV arXiv:2110.10941 Cor. 2.9 into the nested-completion program of `drafts/tail_bound_attempt.md` §2. | **PROVEN** (conditional on a published citation only) | L:2874-2890, ROADMAP:126-131, TH:552-559, PA:491-510, PA:968-971 | `drafts/tail_bound_proof.md` ✔ §4 (7 lines) | never questioned afterwards | **SKETCH — the worst live overclaim.** Three independent defects: (i) `tail_bound_attempt.md:36` calls the three nested completions "**heuristically**"; (ii) `tail_bound_attempt.md:49-62` states that this very step is **invalid for proper subgroups** and needs Deligne-over-µ_k or a Stepanov loop for H³, "which to our knowledge is open" — inserting another *pointwise* bound (OSV) does not repair a defect whose nature is that pointwise bounds cannot be summed; (iii) the derived form is `N₃ ≪ (k²/p)(log p)^{O(1)} + k^{1/2}(log p)^{O(1)}` (`tail_bound_proof.md:86`) and is then restated as "at unit constant" — polylog factors silently dropped. `tail_bound_attempt.md:78` self-tags the whole program `[OPEN GAP]`. |
| `cor:domination` | Assuming conj:tight, `|Tr(W⁴) − matched-sector| ≤ C_F k(k²/p+1)`; since the matched sector is Θ(k²), the relative unmatched contribution is `O_F(k/p+1/k) → 0` for `k=o(p)`. Any uniform `N₃=O(k^θ)`, θ<1, suffices. | PROVEN under conj:tight; **also under the OSV-conditional smooth law for k ≥ p^{3/7+ε}** | PA:593-624, PA:975-976, L:2888-2890 | proof at `PA:614-624` | The proof's degenerate-strata step is **not written**: "it requires classifying the finitely many proportionality types … and bounding each" (`PA:626-637`, audit finding F5) | SKETCH. The conditional-on-conjecture part is fine and honestly tagged; the second clause inherits every defect of the smooth-law claim above. The unwritten degenerate-strata lemma is flagged in the paper — good — but the corollary is still tagged PROVEN in the status table. |
| Hecke pilot (R54) | Haar-orthogonal surrogate for the centraliser torus, 8 configs, m ≤ 17, 32 rotations: off-diagonal Re-kurtosis raw +5.58/+2.75/+2.61 → Hecke −0.73/+0.37/−0.22; eigenvalue spread 2.9–4.0 → 2.6–3.7; KS_GOE 0.13–0.35 (borderline/inconclusive at m≤17). "Hecke symmetrization **partially mitigates** the R49 obstruction. **NOT** a full WD result." | measured partial | L:2895-2923, PA:895-908, PA:973-974 | `artifacts/hecke_local_law_test.json` ✔ — **I verified all of it: max raw kurt_re = 5.575 at (101,10) → hecke −0.727; ks_goe ∈ [0.133, 0.352]** | R67–R70 recast this as a weaker version of their own result and attribute to it a threshold it never states | OK as stated. See §5/S-4 for the misquotation downstream. |
| R58 Linn transfer | Discriminator on `Σ_{H³} e_p(a u₁+b u₂+c u₃+d u₁u₂+e u₂u₃+f u₁u₂u₃)` over 12 configs: `|sum| ~ c·k`, c∈[2,7]; `|sum|/k^{2/3}` GROWS from 3 to 18 as k goes 5→34. ⇒ Linn 2024's iterated-Weil argument does NOT transfer to H³ at the predicted rate. | NEGATIVE (discriminator) | L:3192-3241 | `artifacts/linn_h3_subgroup.txt` ✔, `tools/linn_h3_subgroup.jl` ✔ | H-2 promoted 70%→85%, then VOIDED in `IDEAS.md` Cycle 1 | OK — a properly falsifiable test with a pre-stated criterion ("any future claim of Linn-style transfer must produce a configuration where `|sum|/k^{2/3}` is bounded"). Model behaviour. |
| Ring 2 (R66) | Three attack lines (Stepanov / Deligne / Bourgain) all close as [OPEN GAP]; 32 configs; "the maximum |S(a,b)| … is **uniformly under the Weil ceiling 2√p**. The Weil bound is **essentially tight**: worst empirical ratio `max|S|/(2√p) ≈ 0.99999` (Deligne big sweep at p=4001, k=4)." | OPEN GAP (verdict) + empirical headline | L:3726-3803, TH:561-596, `artifacts/ring2/synthesis.md`, ROADMAP:206-212 | `artifacts/ring2/{line_A_h2h,line_A_head2head,line_B_head2head,line_B_big_sweep,line_B_calibrator,line_C_head_to_head,line_C_calibrator}.json` ✔; `discriminator.json` present but **INVALID JSON** (trailing commas at lines 13 and 16) | never questioned | **CONTRA — arithmetically impossible as stated.** I read `line_B_big_sweep.json`: the field is `ratio_over_weil_only` with `weil_only = min(k, 2√p)`. At p=4001,k=4: `max_abs_S = 3.99999`, `weil_only = 4`, ratio 0.99999; but `2√4001 ≈ 126.5`, so the true ratio to the Weil ceiling is **0.0316**. For |H|=4 the trivial bound is 4, so a ratio near 1 against 2√p is impossible. **The data say the TRIVIAL bound is tight (zero cancellation at k=4) — which is the opposite of "Weil is tight" and is in fact the mechanism that explains why no power-saving exists.** Furthermore lines A and C use `ratio_max_to_2sqrt_p` / `Weil_2sqrtp` while line B uses `min(k,2√p)`: the synthesis pools **incommensurable denominators** (0.44 / 0.63 / 0.99999) into one sentence. |
| R67 Hecke-centring collapse | At A=(2,1,1,1)@p=4481: off-diagonal kurtosis of V_λ collapses from RAW +25.6385 to `R_n` (Haar-Hecke centred, 64 rotations) +0.0145 — a **1767× reduction**, "**much stronger** than the R54 claim". Residual `R_n` has σ_max/σ_median = 2.42, rank 67–68/68 ⇒ structured DENSE matrix with Gaussian entries, not low-rank. Interpreted as "a numerical probe of QUE in the Hecke basis", "consistent with Lindenstrauss–Soundararajan–Venkatesh (Annals 2016)". | NEW empirical result | L:3880-4001, TH:624-717 | `artifacts/ring1_2/v6_hecke_collapse.json` ✔, `artifacts/julia/hecke_real_centraliser_v6.{log,txt}` ✔ | R69 re-measures the SAME design point with m=81 instead of m=68 and gets **295×**, not 1767× (`L:4096-4103`) — "the 295× is the more recent and stable measurement". `TH:633-641` still prints 1767× as the headline. | **DRIFT + CONTRA.** (i) 1767× vs 295× at the same (A,p) with no reconciliation beyond "different windows for the cluster". (ii) The comparison to R54 is not like-for-like: R54's design points had m ≤ 17 and RAW kurt ≤ 5.58; a reduction *ratio* is not comparable across different RAW values — R70 itself later concedes exactly this (`L:4184-4188`, "the reduction factor is sensitive to the RAW kurtosis … The R_n kurtosis is the invariant"), which retroactively voids the "1767× stronger than R54" headline it was built on. (iii) The LSV citation is decorative: LSV is about arithmetic hyperbolic surfaces and has no logical relation to a kurtosis measurement on a 68×68 matrix. |
| R67 F0 reciprocity | The identity `S(a,b)S(b,a) = −S(ab,1)S(1,ab)` is FALSIFIED at all 273 tested (p,k,a,b), including on F_p^× (classical Kloosterman). "The identity is wrong as stated — the correct Salié reciprocity is a 3-sum." | NEGATIVE methodological result | L:3932-3941, TH:682-691 | `artifacts/frontier/hecke_reciprocity_data.json` ✔ | opened as `op:fano_kloosterman` | OK — a negative result about the project's own test rather than about nature, correctly labelled. |
| R68/R69 (v7/v8) | Hecke-collapse observed at 6 design points, A=(2,1,1,1), k∈{21,40,50,51,60,64}, m∈{12,57,64,71,75,81}: reductions 5.3× / 230× / 70× / 1294× / 187× / 295×, R_n kurtosis ∈[−0.05, 0.25]. Real threshold is statistical: `m ≥ 12` AND `RAW kurt ≥ 1`, **NOT** `k ≥ 50`. | NUMERICALLY-SUPPORTED | L:4003-4147, TH:724-902 | `artifacts/julia/hecke_real_centraliser_v7_fixed.txt` ✔, `v8.txt` ✔ | — | Substance OK; **the "R54 claimed k≥50" premise is a fabrication** (see §5/S-4). Also note `TH:770` states the threshold as `m ≥ 8` while `TH:830` and `L:4065` state `m ≥ 12`, in sections written the same day. And v7 at p=151,k=25,m=9 gives a reduction of **0.6× (negative)**, which is quietly reclassified as "RAW kurt already small" rather than counted as a failure. |
| R70 (v9/v10) | Universality: A=(3,1,2,1) k=42 m=105 → 363×; A=(5,2,2,1) k=41 m=66 → 353×; A=(7,3,2,1) k=59 m=80 → **7842×** (R_n kurt −0.003, "NEW RECORD"). Reproducibility: 5 seeds at (2,1,1,1)@3469 give reductions 178–1907× (CV≈90%) but R_n kurtosis mean 0.026, sd 0.060. "Churilov tail index σ_max/σ_median ≈ 2.3 is **universal**." Total: 11 design points, 4 cat maps, R_n kurt ≤ 0.25 always ⇒ "**strongest numerical confirmation to date of QUE in the Hecke basis**". | NUMERICALLY-SUPPORTED / "first new mathematical content of the Grand Attack" | L:4149-4308, TH:904-1055 | `artifacts/ring1_2/v9_v10_universality_reproducibility.json` ✔, `artifacts/julia/hecke_real_centraliser_v9_v10.{log,txt}` ✔ | `op:r11_universality` admits the 7842× may be "a single-seed artifact" — **Priority 1** (`L:4273-4277`) | **CONTRA + unsupported causal story.** (i) The v9 artifact records **no p value at all** for the three new maps (I checked: fields are `ord_p_A, k, m, kurt_raw, kurt_R, reduction_factor, churilov_ratio`); the LEDGER and THEORY tables print "(best)" / "best" in the p column (`L:4202-4204`, `TH:967-969`). A result at an unrecorded prime is not reproducible. (ii) The 6th seed (271828) timed out and is dropped; "5 valid seeds" is 5/6 with the failure unexplained. (iii) `L:4260-4270` and `TH:989-996` explain the 7842× by "disc = 45 = 3²·5 is well-spread among QR mod p" and "the Hecke mean A_n converges faster for larger k" — **two incompatible mechanisms** (disc-arithmetic vs k-size) asserted in adjacent paragraphs, neither tested, while the project's own `op:r11_universality` says the effect may not exist. (iv) The QUE framing is asserted at least six times but no QUE statement is ever formulated, let alone tested; the measured object (off-diagonal kurtosis of a Hecke-centred random Weyl combination) is not the object QUE is about. (v) `TH:981-987` promotes "σ_max/σ_median ≈ 2.3" to "a universal signature … consistent with a Katz-style sheaf model", and `op:r11_churilov_2.3` proposes "a Katz-style sheaf with Newton polygon of slope ≈ 2.3" — a Newton polygon slope is not a singular-value ratio; this is numerology. |

### 1.11 Named open problems (status of each, as of the last run)

| ID | Content | Status | Stated at | AUDIT |
|---|---|---|---|---|
| `op:tail` | Prove conj:tight with explicit constant. | OPEN | PA:854-859 | OK. Partially confused with the smooth-law claim, which is tagged PROVEN for k≥p^{3/7+ε}. |
| `op:tail_below_p^{3/7}` | Unconditional local law / subgroup-Kloosterman bound below p^{3/7}. | OPEN, named obstacle | L:3825-3827, TH:548-550 | OK — the obstruction is named with a verbatim OSV Rem. 2.11 quote. Best-documented open problem here. |
| `op:r6` | Characterise `A_p(k)`: vanishing locus, size vs k⁶/p², closed strata forms. | OPEN | PA:861-866, L:3831-3834 | OK. R63 sharpened it to "requires character-sum analysis of H as a product of prime-order subgroups; this is a serious paper". |
| `op:local` | Replace Gaussian randomness in lem:perturb by arithmetic perturbations; bridge to a NN law for unperturbed compressions. | OPEN | PA:868-909 | OK, and it correctly records that the direct attempt **failed** (R49). Contains the retracted "15–40" number. |
| `op:inert` | Extend to Δ a non-residue and to composite N. | OPEN | PA:911-914 | OK, though `PA:802-804` admits two of the four `exp:multi` primes are already inert — the scope note and the experiment disagree about whether inert is in scope. |
| `op:r5` | Close r=5 with ≥12 diverse (A,N) configs and a clean independent reimplementation. | OPEN GAP | TH:474-521, L:3819-3823 | Questionable: `m1_run5.json` already holds 3 passing configs across split+inert from an independent implementation (`m1_r5.py`), and `master_general.json` a 4th. See §5/S-5. |
| `op:lean_rebuild` | Re-establish the Lean project on a box with Mathlib cold-load capacity. | OPEN | L:3828-3830 | OK and necessary: `C:\lean\bgs_formal` no longer exists. |
| `op:paper_recompile` | Recompile paper.tex on a machine with a LaTeX engine. | OPEN | L:3987-3988 | OK but incomplete: the source **cannot** compile as written (unbalanced `remark`). |
| `op:r7_hecke_threshold`, `op:r10_hecke_*`, `op:r11_*`, `op:fano_kloosterman` | Hecke-collapse follow-ups (threshold, math model, universality, seeds, paper). | OPEN | L:3973-3986, L:4117-4133, L:4272-4291 | Several are premature: `op:r11_paper` ("the empirical result is publishable") and `op:r10_hecke_que_paper` propose publication while `op:r11_universality` (Priority 1) still asks whether the headline number is a single-seed artifact. |
| O1–O6 (run 2) | O1 prove C1 for split primes; O2 explain N2 residual; O3 Sp(2g,Z) + prime powers; O4 transfer co-rank/resolvent lemmas; O5 reach m~10⁴ via explicit Hecke basis; O6 prove `c(M,M⁻¹)=+1` in general. | O6 "CLOSED" R5.1; O1–O5 silently dropped | TH:379-396, L:506-515 | O6's closure is scope-limited (needs gcd(M₂₁,N)=1). O2/O4/O5 never mentioned again after run 5; O3 listed as "NOT tried this session" at `L:958-959` and then never again. Silence is not coverage — the ledger says so itself at `L:958`. |

### 1.12 IDEAS.md sub-conjectures

| ID | Content | Status | Stated at | AUDIT |
|---|---|---|---|---|
| H-1 | Real-centraliser Hecke symmetrisation achieves Wigner spacing at m ≥ 70. Prob ~40%. Discriminator: `src/hecke_resolvent_m210.py` on p=3571, expect KS_GOE < 0.05. | SUB-CONJECTURED, pending | IDEAS.md (Cycle 0) | **The named discriminator script `src/hecke_resolvent_m210.py` does not exist** and was never written. Nine Julia versions (v1–v10) were written instead, none of which computes a spacing KS at m≥70. The stated discriminator was never run. |
| H-2 / H-2′ | Bourgain's δ is fundamentally non-explicit. 70% → 85% → VOIDED as a "could be made explicit soon" hope. | VOIDED with reason | IDEAS.md Cycle 1 | OK — calibrated probability, dated, then voided with a mechanism-level reason. Good practice. |
| H-3 | Anosov geodesic flow on constant-negative-curvature surfaces is the cleanest Ring-2 test. 30%. | DEFERRED | IDEAS.md | Never attempted. Ring 2 was redirected to the Kloosterman wall. |
| H-4 | Frame-holonomy heat trace as WD skeleton. | RETIRED | IDEAS.md | OK |
| H-5 | Schwartz–Zippel gives `N₃ ≤ 2k`. | **VOIDED** | IDEAS.md; L:2967-2987 | OK — voided for two independent reasons (cleared reciprocal polynomial has total degree 3, not 2; and `u₄ ∈ H` is not automatic). The accompanying lesson ("the right action was to drop the sub-claim, not to keep tightening it") is the most useful sentence in the corpus. |
| H-6 / H-7 | Churilov decomposition applies to the Hecke-centred residual R_n; Hecke mean gives Wigner spacing at m=70. 50% / 30%. | DEFERRED | IDEAS.md Cycle 1 | H-7's discriminator (struct-Hecke block-diagonal at m=70) was never run; v6–v10 all use the **Haar** surrogate, which is precisely what R54 said must be replaced (`L:2921-2923`). Ten script versions later, the one thing the pilot said was needed has still not been done. |
| H-8 | `A_p(k) = 0` iff no prime divisor q of k contributes a non-trivial character sum. ~40%. | NEW (R63) | L:3558-3564 | OK — has a stated discriminator. |

---

## 2. RETRACTION LEDGER

Every retraction found, what it voided, and whether the dependents were actually
marked void. Checked, not taken on trust.

| # | Retraction | Where | What it voided | Dependents actually marked void? |
|---|---|---|---|---|
| RET-1 | Run-1 kernel is not a quantisation (Egorov error O(1)) | L:20-31 | All run-1 statistics R3–R6 of the old THEORY.md | **YES.** `TH:315-322` lists them; `artifacts/retracted_run1/README.txt` records that the artifacts were deleted. Complete. |
| RET-2 | "a=d ⟺ β=1" gauge artefact | L:33-35 | The run-1 symmetry criterion | **YES**, superseded by T3/T4. |
| RET-3 | π/(2k) torsion theorem trivial | L:37-38 | Run-1 torsion claim | **YES.** |
| RET-4 | "multiplicities up to 23" were lattice-cell counts | L:40-42 | Run-1 multiplicity claim | **YES**, superseded by T2. |
| RET-5 | SVD rank cut at 0.5·σ_max silently truncated eigenspaces ⇒ spurious GUE signal | TH:323-324, L:528-530 | An intermediate GUE reading of the compression | **YES** — corrected to a 1e-6 relative cut and disclosed. But note `L:1836` and `L:1688-1689` still list "projector_eigenspace tolerance 1e-6 might merge nearby eigenvalues for large p" as a live fragile point, and `L:3916-3920` records that at tol=1e-6 the v3/v4 `cluster_eigs` **did** fail (every eigenspace size 1). The fix for one failure mode created another; only the first is in the retraction ledger. |
| RET-6 | **R12-A: run-11 Theorem 6 / "BGS at order four"** | L:1558-1594 | (a) `|Tr(V_λ⁴)−WD₄| ≤ C_F k⁸/p²`; (b) threshold `k=o(p^{2/3})`; (c) "BGS at order four" claim; (d) R11-C "all fixed even orders at `k=o(p^{1/(r−1)})`"; (e) `bgs_note_run11_theorem.tex`; (f) `bgs_paper_complete.tex` needs rewrite | **MOSTLY.** ✔ In-place warning box added at `L:1399-1412` (the only one in the ledger). ✔ `artifacts/retracted/bgs_note_run11_theorem.tex` archived. ✔ `ROADMAP.md:20-24` carries an explicit R12-A warning. ✔ Paper carries a "Historical note" (`PA:130-137`). **✗ But the R12-A replacement statement has itself drifted back up to "proven unconditionally"** — see §3/S-1. **✗** `drafts/bgs_paper_complete.tex` and `drafts/bgs_note_run12_corrected.tex` are both **absent from disk**, so neither the rewritten paper nor the corrected theorem can be inspected. **✗** R11-C's claim contradicted the already-proven T18-barrier at the moment it was written; the retraction never notes this, so the underlying reasoning error (trivial bounds beat a proven obstruction) is not recorded as a lesson. |
| RET-7 | **R34: "arithmetic beats symmetry" quantum Tr(W⁴) experiment** | L:2235-2239, L:2255-2256 | The 12/12 GUE-vs-GOE-Wick quantum claim; the paper's `exp:quantum`, contribution 3, and an abstract claim | **YES — exemplary.** Root cause named (non-Hermitian V ⇒ negative Tr(W²)); artifact moved to `artifacts/retracted/run13_quantum_w4.json`; paper text removed at R47 (`L:2445-2447`); lesson recorded ("Always verify Hermiticity before comparing against RMT"). The *resonance-count* version of the claim survives and is correctly retained. |
| RET-8 | **R48 Phase 3: sign bug in all prior r6 brute force** | L:2508-2512 | R16, R22, R23, R24, R25 numeric claims (family decompositions); even-k totals survived "coincidentally via −1-in-H symmetry" | **PARTIALLY.** ✔ The scope is stated precisely and the surviving part is identified. **✗ No in-place warning at `L:1792-1810` (R16), `L:2011-2030` (R22) or `L:2032-2038` (R24-WRAP)** — a reader arriving at R22 sees "STATUS: [NUMERICALLY-SUPPORTED] initial classification" with no hint that the underlying enumeration was wrong. **✗** `artifacts/run16_r6.json`, `run22_classify.json`, `run25_partition.json` remain in the live `artifacts/` tree, not in `artifacts/retracted/`, unmarked. |
| RET-9 | **R49-A / R48 `thm:r6` retracted-and-replaced** | L:2576-2579 | `sol6 = 5k(3k²−9k+8)` as a theorem for all even k | **YES.** Counterexample (241,30) given with numbers; paper replaced with Prop + Conj + excess `A_p(k) ≥ 0` (`PA:668-712`). Note it was tagged "THEOREM thm:r6 … verified exact at 5 points" only 63 lines earlier (`L:2513`) — a 5-point verification promoted to THEOREM and refuted one run later. |
| RET-10 | **R52b: the |ρ|=1.0000 row-correlation signal** | L:2704-2715 | R52 Phase III "near-perfect real-linear dependence inside rows" | **YES — best-in-class.** Refuted in the same session by a pre-committed independent replication; the wrong-null mechanism is explained; a permanent methodological lesson is recorded. |
| RET-11 | **R54 self-correction: Lemma:SZ (`N₃ ≤ 2k`)** | L:2967-2987 | The lemma, `rem:SZtooWeak`, the θ=1 sub-claim in `cor:domination`, and the SZ reference in the "Combining the three layers" paragraph | **YES.** All four dropped; `IDEAS.md` H-5 marked VOIDED; the unconditional ceiling reverts to `N₃ ≤ 4k` (`PA:426-427`). Two independent errors named. Model behaviour, including the meta-lesson about tightening loops. |
| RET-12 | **R61: "max/median ≈ 15–40" fabrication** | L:3351-3405 | The number itself; the R56 draft-triage "DIRECTLY RELEVANT" tag; the R59/R60 "low-rank V_arth constructor" design; the v2 tool as a planning artifact | **NO — INCOMPLETE.** ✔ The retraction is explicit, self-accusing ("Per the contract integrity rules, this is a fabrication"), traces the number through 4 ledger entries, and voids the cascade. ✔ `L:3061`, `L:3255-3264`, `L:3862-3864` all carry the correction. **✗ The number is still printed in the paper at `PA:881`** — "(max/median ≈ 15–40 across split and inert primes alike)" — inside `op:local`, as the stated cause of the local-law failure. The paper was edited on 2026-08-28 (12:48) by the same run that wrote the standing-retraction list; `L:3873-3876` then claims "The paper reflects the corrected state". It does not. This is the single most serious uncorrected dependent in the workspace. |
| RET-13 | **R63: the 3\|k closed form for sol₆** | L:3474-3494 | `sol6 = 15k³−5k²−170k` (fitted on 4 points) | **YES**, within the same entry, with the mismatch table and the verdict "The 4-point fit was a coincidence". Not previously propagated to the paper, so no dependents. |
| RET-14 | **R58/IDEAS: Linn-transfer hope (H-2′)** | L:3217-3241, IDEAS Cycle 1 | The R57 plan to port Linn 2024's stratification to H³ | **YES**, with a pre-stated falsification criterion. |
| — | R41: the **written proof** of thm:core contained counting errors (case (a) counted as k²−k instead of k²; "compensating mistakes" masked it) | L:2333-2361 | Not a retraction of the statement, only of the argument | Handled correctly (statement unchanged, proof rewritten, manual k=2 anchor). But `L:340-344` and `TH:245-247` still carry the run-2 proof text with no pointer to R41. |
| — | R55: the R56 draft-triage entry was **"RETROACTIVELY WITHDRAWN"** and `user_drafts/` deleted at the user's request | L:3049-3078 | Three Churilov 2026 drafts | Executed (directory absent). Note this destroys the primary source for the §3 "USER DRAFTS — independent verification" block at `L:486-502`, which claims to have "independently re-proved" Props 3.2/3.3 — that verification is now unauditable. |

**Retraction hygiene score: 12 of 15 complete, 3 with live uncorrected dependents
(RET-6 → drift back to "proven"; RET-8 → no in-place warnings, artifacts unmarked;
RET-12 → fabricated number still in the paper).**

---

## 3. DANGLING EVIDENCE (verified against the filesystem)

Every path below was checked with `ls`/`stat` on 2026-08-28. `MISSING` = not
present anywhere under `BGS/` (or at the stated absolute path).

### D-1. The T13 evidence chain is broken in both directions (worst case found)

* `artifacts/theta_sign.json` **exists** (28 entries: 7 matrices × 4 primes ∈
  {101,199,521,1009}, split and inert, every entry `signs: {"+1": 6}` or
  `{"+1": 7}`).
* Its generator `src/theta_sign.py` is **MISSING**. `grep -r theta_sign` over the
  whole tree returns only `src/exact_verify_run5.py:209` and a filename mention in
  `src/archive/verify_all2.py:263`.
* `L:3615-3629` (R65/R1.1, 2026-08-28) asserts: "The portable `theta_sign()`
  function in `src/exact_verify_run5.py` (lines 209–248) and its emitted artifact
  `artifacts/theta_sign.json` (28 entries …) make **no** skip on
  `M₂₁ % N == 0`". I read those lines. That function (a) writes to
  `exact_run5.json`, not `theta_sign.json` (`src/exact_verify_run5.py:300`), and
  (b) `break`s out of its search loops at the **first** reversing involution found
  and `assert`s exactly one — it cannot produce a per-config tally of 6–7 signs.
* The red team (`review/redteam_run5.md` §C1) states that
  `theta_sign.reversing_involutions([2,1,1,1],25)` enumerates **16** reversals and
  that `theta_sign.py:64` (`if Mf[2] % N == 0: return None`) skips the degenerate
  ones, `:100` dropping them from the tallies. The artifact records 6–7 per
  config — **consistent with the skip, inconsistent with R65's claim**.
* Consequence: the paper's T13 status row (`PA:936-943`) cites
  `artifacts/theta_sign.json` as evidence for "PROVEN on the chart
  gcd(M₂₁,N)=1 (every reversing involution in the scanned box)", where the
  artifact is the output of an absent script that is known to skip part of the box.

### D-2. Paper-cited numbers with no live source

* `PA:881` "max/median ≈ 15–40" — **retracted as a fabrication** (`L:3375-3383`);
  no artifact anywhere contains such a ratio.
* `PA:899-900` "raw +5.6 → Hecke −0.7 in the worst case" — traceable to
  `artifacts/hecke_local_law_test.json` ✔ (verified). Fine.
* `PA:1036-1037` "Compiled artefacts: `unitary_perturbation.json`,
  `run46_exact_mean.json`, `run36_audit.json`" — all three ✔ present.
* `PA:266-268` Lean theorems `prod_eq`, `sum_sq` in `BgsFormal.lean`,
  "repository path recorded in the artefact manifest" → manifest says
  `C:\lean\bgs_formal\BgsFormal.lean` → **directory MISSING**.

### D-3. Missing drafts (every theorem write-up from runs 9–13 is gone)

`drafts/` contains exactly three files: `hecke_symmetrization_test.md`,
`tail_bound_attempt.md`, `tail_bound_proof.md`. **MISSING**, all cited:

* `drafts/bgs_note_run9_theorem.tex` (`L:1264`, `L:1286`, `L:1337`, `L:1342`,
  `L:1373`, `L:1508`) — the run-9/10 "unconditional" p^{3/2} theorem.
* `drafts/bgs_note_run12_corrected.tex` (`L:1404`, `L:1604`) — **the document
  the R12-A warning box points readers to as "the correct theorem"**.
* `drafts/bgs_paper_complete.tex` (`L:1589`, `ROADMAP.md:38`).
* `drafts/resonance_core_paper.tex` (`L:1704`, `L:1850`, `L:1948`, `L:2122`).
* `drafts/bgs_run13_final.tex` (`L:1673`).
* `drafts/bgs_note_run3.tex` (`TH:4`, `L:634`), `drafts/bgs_note_run5.tex`
  (`TH:399`).
* `drafts/archive/` (`L:1706`, `L:2471`, MANIFEST `:40`) — directory absent.

### D-4. Missing Lean (all formal evidence)

`C:\lean\bgs_formal` — **DIRECTORY MISSING**. Therefore absent:
`BgsFormal.lean` (`L:1013`, `PA:266`, MANIFEST `:44-46`, README),
`BgsAudit.lean` (`L:2756-2760`, `review/audit_2026-08-26.md` §5),
`ResonanceLemmas.lean` (`L:4`, `L:1958`, `L:3588`),
`card_le_four_draft.lean` (`L:1388`, `ROADMAP.md:32`).
`C:\Users\churi\lean-projects\mephisto-lean\MephistoLean\BgsR11.lean` **exists**
(4816 bytes, 2026-08-28 13:34) but has never been type-checked (`L:3943-3951`).
Note also: `L:3696-3699` (R65/R1.6) states "`C:\Users\churi\lean-projects\bgs_ring1\`
was **not** created" — **it exists** (created 2026-08-28 13:08, containing
`BgsRing1.lean`, `BgsRing1/Basic.lean`, `lakefile.toml`); so does `bgs_minimal`.
The claim and the filesystem disagree on the same day.

### D-5. Missing scripts for claims still tagged PROVEN or NUM-SUPPORTED

| Cited script | Cited at | Supports | On disk |
|---|---|---|---|
| `src/rigidity.py` | L:246, TH:176 | T12 spectral rigidity (**PROVEN UNCONDITIONALLY**) | MISSING (not even in `src/archive/`) |
| `src/birkhoff_density.py` | L:197 | T8′ classical density + CLT width | MISSING |
| `src/theta_sign.py` | L:891, red team C1 | T13 / O6 | MISSING |
| `src/m1_new_configs.py` | L:910, L:979, TH:477, PA:950 | r=5 (deprecated, but cited as the thing being deprecated) | MISSING — `L:3594-3596` admits this: "C-NEW-1 (critical): `theta_sign.py`, `m1_new_configs.py`, `s_of_j5` are MISSING from the portable workspace. The red-team C1 and C5 fixes cannot be applied mechanically." |
| `src/s_of_j5.jl` | TH:478, PA:950 | r=5 | MISSING |
| `src/verify_all2.py` (10/10, then 20/20 PASS) | L:523, L:710, L:779, TH:329 | The entire run-2 "second independent implementation" claim | Only `src/archive/verify_all2.py` |
| `src/indep_check.py`, `indep_check2.py` | L:549, L:711-712, L:779 | The run-3 independent verification (A1–A4) | Only in `src/archive/` |
| `src/smooth_ext.py` | L:1501 | Smoothness of `prop:count` (800+ solutions) | MISSING |
| `mechanism_winner.py` | L:1626 | R13-A "arithmetic beats symmetry" | MISSING |
| `review/run30c.py` | L:2164 | R30 — the **first** WD evidence in the perturbed setting | MISSING |
| `review/run42_smallk.py` | L:2365 | R42 small-k stress test (2000 patterns/config) | MISSING |
| `review/run7_debug/{sj_scaling,per_rs_debug,agg_probe,route_cmp}.py`, `sj_scaling_ext.py` | L:1152, L:1191, L:1308-1311 | R7.2/R8-B sqrt-law; R9-D residual localisation | MISSING (directory absent) |
| `review/run5_debug/diff_probe*.py` | L:985 | The three r=5 bug fixes B1–B3 | MISSING |
| `review/run6_julia/{s_of_j5.jl,dump_text.py}` | L:1072-1079 | The Julia cross-validation port | MISSING |
| `src/hecke_resolvent_m210.py` | IDEAS H-1 discriminator | H-1 (the whole Ring-1.2 programme) | MISSING — never written |

### D-6. Named-but-unnamed artifacts ("run log of the …")

T1 ("run log of the Egorov scan", `L:55`), T3 ("reversibility/anti-unitary scan
log", `L:102`), T4 ("real-structure verification log", `L:115`), T7/T9/T10 (no
artifact), T18(b) (no artifact). Five PROVEN-tagged claims rest on artifacts that
have no filename at all. They were re-verified later by exact-integer certificates
(`artifacts/exact_run5.json` ✔, X1–X7, `total_pass` key present), which is what
saves them — but the run-2 evidence itself is unlocatable.

### D-7. Missing verification logs cited by MANIFEST and the 08-26 audit

`artifacts/audit_rerun_independent_suite.log`, `audit_rerun_master_general.log`,
`audit_rerun_verify_mean_law.log` (the whole `audit_rerun_*.log` family except
`audit_verify_all2_rerun.log`), `artifacts/julia_out2.log` (the "Julia
second-language key"), `artifacts/audit_strata_rho{1,4,16}.log`,
`artifacts/run13_strong_master.json`, `artifacts/phase2_spacings.npy` (the 13723
spacings behind `exp:beta`), `artifacts/l^2_table.json` (cited at `TH:440-442` as
"the corrected `l^2_table.json`"), `artifacts/hecke_real_centraliser_v3.txt`,
`lean_projects_setup.log` (cited `L:3971`, `TH:680`).

### D-8. `review/blind_replication/` — MISSING

The blind replication is load-bearing for the campaign claim (`L:872-876`: "BLIND
REPLICATION (fresh agent, from-scratch implementation, no access to our pipeline;
`review/blind_replication/report.md`): REPLICATED at p=39161") and is listed as
"Layer 6: Blind replication … REPLICATED" in the R10 certification stack
(`L:1518`). The directory does not exist. Also missing:
`review/redteam_run5_scratch/` (`rt_c5.py`, `rt_c5b.py`, `rt_c4_c123.py`) — the
red team's own verification code, i.e. the evidence for the corrections that
runs 53–66 spent most of their effort implementing.

### D-9. Broken/mis-pathed references in the traceability documents

* `artifacts/ring3/REPRO.md` triple #5 cites `artifacts/ring2/big_sweep.json` —
  actual name `line_B_big_sweep.json`. Broken path.
* `artifacts/ring3/REPRO.md` "Verdict" cites `artifacts/ring0/MOVE_COUNT.json` —
  **no `artifacts/ring0/` directory exists**; the hygiene JSON is
  `artifacts/ring3_hygiene.json`.
* `artifacts/ring2/discriminator.json` — **invalid JSON** (trailing commas);
  `json.load` fails. Cited by MANIFEST `:117` and `L:3857`.
* `README.md` "Repository layout" lists `user_drafts/`, `archive/` (runs 1–11),
  `review/blind_replication` — all absent; says "LEDGER.md full research log,
  runs 1–46" (actual: 70 runs); points at `C:\lean\bgs_formal` (absent).
* `README.md` reproduce-list maps `exp:multi` to `src/verify_perturbation_wd.py`,
  which regenerates the **superseded** `run31_multiprime.json` (containing the
  0.1343 failure), not the paper's `unitary_perturbation.json`. Same error in
  MANIFEST `:27`.
* `L:2827` and `L:2992` cite the plan at `local://bgs-final-attack-plan.md`;
  `L:3036` cites `local://bgs-grand-attack-plan.md`; `L:3587` cites
  `local://bgs-ring0-audit/REVIEW.md` (18 KB, "F1–F15 audit"). None of these are
  in the workspace, so the scope against which runs 54–66 declare "PASS" cannot
  be checked at all.

**Tally: of ~150 distinct cited paths, 47 are missing.** The missing set is not
random: it is concentrated in (i) every theorem write-up from runs 9–13, (ii) all
Lean, (iii) all blind-replication and red-team scratch code, (iv) the debug
scripts behind the sqrt-law and the r=5 fixes. The surviving evidence is
overwhelmingly the *final* JSON of each run, which is the part that cannot be
re-derived.

---

## 4. SILENT STATUS DRIFT

Cases where a claim's status improved between runs without new evidence, or where
a hedge present at first statement is absent at later citation.

### S-1. `O_F(k⁴/p²)` fourth-moment bound: "needs a separate argument" → "proven unconditionally"

* **First statement (R12-A, `L:1578-1585`):** "Other label patterns contribute
  `O_F(k⁴/p²)` or 0 (**needs separate collision/fibre argument, NOT trivial
  |Sᵢ|≤k**). Correct theorem to state: `Tr(V_λ⁴)=WD₄(V,Θ)+O_F(k⁴/p²)`, valid for
  ALL admissible (p,k) with NO threshold. **Local law still open ⇒ do NOT call
  this BGS yet.**"
* **Later (`TH:599-604`, 2026-08-28):** "the R12-corrected bound
  `Tr(V_λ^r)=WD_r(V,Θ)+O_F(k^r/p²)` holds for ALL admissible (p,k) with NO
  threshold on k. The BGS-relevant component is **proven unconditionally at fixed
  order r ≤ 4**."
* **And in the paper (`PA:957-958`):** "ALL admissible (p,k) for the fixed-order
  moments r ≤ 4 (R12 corrected, no threshold)."
* **New evidence in between: none.** The "separate collision/fibre argument" was
  never written — `L:1614` lists it as NOT DONE ("Collision/fibre bound for
  unmatched labels written up as Lean lemma"), and it never reappears.
* **Internal contradiction:** the paper's own `cor:domination` (`PA:593-612`,
  `PA:975-976`) is *conditional on `conj:tight`*, and `conj:tight` is
  NUMERICALLY-SUPPORTED. The same status table therefore asserts both "r≤4 proven
  unconditionally" and "domination conditional on a conjecture" for what is the
  same 4th-moment statement.
* Also note `L:3798-3800` and `ROADMAP.md:218-222` repeat the upgraded form, so
  three of the four top-level documents now carry it.

### S-2. T13 / O6: "unconditional, elementary" → hypothesis added → "closed"

* R5.1 (`L:792-800`): "`U_M conj(U_M) = I` exactly, `Θ²=+1` identically. No Weil
  cocycle needed. Only β=1,2 occur — **unconditional, elementary**."
* R5.6 (`L:888-893`), same run: "DOWNGRADED-scope: theorem holds for reversing
  involutions with `gcd(M₂₁,N)=1`. `theta_sign.py` **silently skipped** c==0 mod N
  cases."
* R65/R1.1 (`L:3615-3629`, 2026-08-28) then declares the gap **closed** on the
  basis of a factual claim about the code that is false (§3/D-1), and adds an
  analytic paragraph for the degenerate chart (`TH:199-211`, `PA:391-410`).
* The analytic paragraph is a **sketch**: it asserts `Ū_M ∘ U_M = (1/N)·1` is "the
  **pointwise** identity on the basis T(v)" for a factorised
  `chirpx ⊗ chirpy`. No computation is shown, the normalisation `(1/N)` versus
  `Θ²=+1` is not reconciled, and "every v in the kernel is an eigenvector of Θ²
  with eigenvalue +1" conflates the kernel of M₂₁ with a basis of the Hilbert
  space. It may well be true — it is not a proof.
* Net drift: a scoped-down theorem was returned to full generality by a prose
  paragraph plus a false statement about a missing script, and the paper's status
  row now reads "PROVEN on the chart gcd(M₂₁,N)=1 … degenerate chart collapses
  trivially to β=1", i.e. PROVEN everywhere.

### S-3. U4: red-team correction replaced by a *different* wrong bound, under the red team's name

* Original (`L:846-855`): `extras ≤ 5k⁴p^{δ−2}`, usable for `k ≤ p^{1−δ/2−ε}`.
* Red team's actual finding (`review/redteam_run5.md` §C3.3): with `‖S‖₂²=p²k`
  exact and `sup|S| ≤ kp^{−δ}`, Cauchy–Schwarz gives `extras ≤ k⁴p^{−2δ}`; the
  printed bound is "**2400× too strong to follow from the stated inputs**"; the
  usable threshold "collapses to `k ≲ p^{δ}` — **vacuous** for any published δ";
  verdict "**U4 downgraded to conditional sketch with incorrect quantitative
  conclusion**".
* What the ledger recorded (`L:896-902`): `extras ≤ k³p^{−2δ}`, `o(1) iff
  k ≪ p^{2δ}` — a **third** value, matching neither the original nor the red team.
* What is now in THEORY (`TH:436-472`) and the paper status table
  (`PA:929-935`): the `k³p^{−2δ}` / `k ≪ p^{2δ}` version, labelled
  "**PROVEN conditional, RED-TEAM-CORRECTED**" with the parenthetical "(NOT
  p²k²  — the red-team C3 correction)".
* So the paper cites the red team as the authority for a bound the red team never
  endorsed, while omitting the red team's actual verdict (sketch, incorrect
  conclusion, vacuous threshold). `TH:465-472` even asserts the corrected bound
  *is* `k³p^{−2δ}` and calls the alternative "vacuous" — inverting the finding.

### S-4. R54's Hecke pilot: `m ≥ 70` (Wigner test) → "R54 claimed k ≥ 50" (kurtosis collapse)

* What R54 actually says (`L:2916-2923`): "Hecke symmetrization **partially
  mitigates** … **NOT** a full Wigner–Dyson result … clear path to a definitive
  test (**m ≥ 70** with the actual centraliser torus basis, not the Haar
  surrogate)". The words "k ≥ 50" appear nowhere in R54; `grep` finds "k ≥ 50"
  only in R67–R70 and THEORY §8.0.5–8.0.7.
* R68 (`L:4015`): "contradicting the R54 LEDGER R54 threshold of k ≥ 50".
  R69 (`L:4059-4061`): "R54 LEDGER R54 claimed 'k ≥ 50 was needed' … **v8
  disproves this**". R70 (`L:4240-4245`): "R54 had 'k ≥ 50 threshold' — REFUTED".
  `TH:744`, `TH:766`, `TH:819-827`, `TH:889-890` repeat it.
* Three runs (R68, R69, R70) and three THEORY sections are framed as refuting a
  claim that does not exist, while the actual R54 requirement — replace the Haar
  surrogate with the real centraliser basis — remains **undone** in all of
  v6–v10 (all use `n_hecke` Haar-orthogonal rotations).
* Compounding drift: R67 claims its 1767× is "much stronger than R54"; R69
  re-measures the same design point at 295×; R70 then establishes that the
  reduction factor is seed-dependent by a factor of 10 (178×–1907×) and that "the
  R_n kurtosis is the invariant" — which invalidates every "N× stronger than R54"
  comparison made in R67–R69, none of which is withdrawn.

### S-5. r=5: three passing configs → "ONE pass at r=5" (drift downward, still wrong)

* R6.1 (`L:977-994`): three configs, three λ-branches each, err ≤ 4.2e-17 /
  1.4e-16 / 3.5e-16, including an **inert** prime (Arnold@233), artifact
  `m1_run5.json`, clean reimplementation `m1_r5.py`. I verified the artifact:
  `all_pass: true`, three configs, nine rows.
* R53 (`L:2815-2819`) adds a fourth, independent r=5 pass via
  `master_general.py` (err ~1e-17); I verified `master_general.json` contains it.
* `TH:474-521` and `PA:944-952` (2026-08-28) then state: "**ONE** pass at r=5
  (Arnold @ N=101) … `m1_new_configs.py` and `s_of_j5.jl` DEPRECATED; r=5 closure
  is `op:r5` OPEN GAP requiring ≥12 diverse configurations".
* The three `m1_r5.py` passes are not mentioned; `TH:490-493` claims "the active
  r=5 path is the clean-room `src/archive/m1_r5.py` … plus `master_general.py`,
  which at the time of writing produces a single r=5 all-pass configuration" —
  conflating "master_general has one r=5 row" with "there is one r=5 pass".
* This drift is *conservative*, so it does not inflate a result; it is still a
  factual misstatement of the on-disk evidence, and it created an open problem
  (`op:r5`) that is partly already discharged.

### S-6. Smaller drifts

* **T12 "unconditional"** (`L:238`, `TH:170`): asserted in bold, but the proof
  chains through T7, which R2 proved requires `gcd(N,tr(A)²−4)=1` (`L:603-606`).
  No amendment at either location.
* **C1's refuted empirical support** (`TH:309-311`) is still printed as
  "Empirical support" 300 lines after the header note that refutes it.
* **T16 form factor** stays tagged "verified, 224-sample ensemble" (`L:299`,
  `TH:226`) although R6.5 (`L:1047-1054`) found a second pipeline reversing the
  generic-case verdict and recorded [INCONCLUSIVE].
* **F3 entry Gaussianity** was downgraded to CONTESTED (`L:704`, `TH:404-405`
  "not used anywhere downstream"), then re-used as R49-A's positive finding and
  carried into the paper (`PA:886-894`) with no reference to the contest.
* **`conj:tight` config count** inflates from "~230" (`PA:512`, README) to "~293
  configs / ~60,000 random patterns" (`L:2884`, `PA:969`) — the arithmetic
  (196+42+38+25 = 301, or 196+25+38 = 259) never quite lands on 293, and
  `drafts/tail_bound_proof.md:33` uses "34" for `run20_constant` where the file
  has 42 records.
* **R20's "constant exactly 1 (no slack observed)"** (`L:1915-1918`) was falsified
  by 10/196 violations at R37 (`L:2284-2288`). The R20 block carries no warning.
* **`exp:beta` "RESOLVED"** (`PA:980-981`) for a GUE perturbation of a system
  whose own symmetry theory (T3/T4/T13) predicts β=1. The paper explains this
  (the perturbation, not the map, sets the class) but the status word "RESOLVED"
  in a table headed "Claim | Status" reads as a resolution about the cat map.
* **`L:2932` "27 pages"** for the recompiled PDF; the only compile log on disk
  (`paper/resonance_laws_catmaps.log`, dated 6 minutes *before* the PDF) says
  "Output written on resonance_laws_catmaps.xdv (**13 pages**)". Unverifiable
  either way; the log does not correspond to the shipped PDF.

---

## 5. TOP 10 LOAD-BEARING CLAIMS (ranked by how many other claims depend on them)

Dependency counted by explicit downstream citation in LEDGER/THEORY/paper. A
failure of a claim high on this list invalidates everything indented under it.

**1. T1/A1/R5 — the propagator and the Egorov covariance (up to phase, with Aᵀ).**
`L:52-55` + `L:553-561` + `L:670-674`. *Everything* depends on this: T2, T6, T7,
T8, T9, T10, M1, all resonance systems, all numerics. It has already failed twice
(wrong matrix A vs Aᵀ; missing quadratic cocycle) and been repaired twice. It is
now supported by exact-integer certificates with a negative control
(`artifacts/exact_run5.json`, X1). **Risk: low, but the in-place text at `L:54`
and `TH:50` still states the false form.**

**2. T7 — `|Tr(T(v)U^J)| = 1` for J ≢ 0 mod K, under `gcd(N, tr(A)²−4)=1`.**
`L:160-166`. Directly required by T8, T8′, T9, T12 (rigidity), A2/R1 (multiplicity
rigidity), M1 (via the ρ_J table), and hence by every moment statement. R2
(`L:603-606`) showed the hypothesis is **necessary** (failure by 10.18 at N=25).
**Risk: low; hypothesis-labelling risk: high — three dependents still call
themselves unconditional.**

**3. T6 — Birkhoff reduction `P_λVP_λ = V̄P_λ`.**
`L:150-158`. The reason the problem is finite-dimensional and orbit-indexed;
required by T8, T9, T10, T19 (the tight frame depends on "only the A-orbit"), M1,
and the entire resonance-count formalism. Proof is complete and short.
**Risk: very low.**

**4. M1 — the master moment formula.**
`L:715-745`. The bridge from `Tr(V_λ^r)` to resonance counts; explicitly the
"machine-level bridge" invoked at `PA:202-209` and used in the proof of
`cor:domination` (`PA:614-624`). Everything in the published paper about moments
routes through it. Certified at r≤4 in three independent implementations
(`master_formula.py`, `master_general.py`, `m1_r5.py`) and re-run at R40 and R54.
**Risk: low at r≤4; r≥5 rests on 4 configs total (see S-5).**

**5. thm:core (T17) — the matched resonance identity `2k²−k` / `3k(k−1)`.**
`L:325-352`, `PA:290-330`. Load-bearing for: the Wick dictionary (`PA:343-361`),
`rem:shadow`, `rem:rev`, R13-A, `cor:domination`'s matched sector (Θ(k²)),
the whole r=6 strata programme (whose proofs "mirror Theorem thm:core"), U5′'s
self-case anchor, and the abstract's headline (i). Verified 19/19, then 5/5, 7/7,
15/15, 40 (Julia), 51/51 (independent suite), plus manual k=2 and k=4.
**Risk: very low. Its *written proof* failed once (R41) and was rebuilt.**

**6. `conj:tight` — `N₃ ≤ ⌊k²/p⌋+2` for generic patterns.**
`PA:448-458`. The sole hypothesis of `cor:domination` (`PA:593-612`), which is in
turn the paper's only statement about the *complete* fourth moment. Also the
target of `op:tail`, of the Ring-1/Ring-2 wall attacks, and of the OSV-conditional
smooth-law claim. ~293 configs, 0 violations, correctly tagged
NUMERICALLY-SUPPORTED everywhere. **Risk: moderate (unproven); honesty: good.**

**7. thm:meanlaw + lem:zerocounts — the exact ensemble mean `⟨N₃⟩ = k³(p²−3p+3)²/(p−1)⁶`.**
`L:2419-2427`, `PA:523-565`. Load-bearing for the abstract's headline (ii), for
the "typical pattern has no resonance" argument, for the degenerate-strata measure
`O(1/p)` in `rem:collision` and in `conj:unified`'s empirical support, and for
Appendix A.2. Fully proven, elementary, independently re-verified by complete
enumeration at p∈{5,7}. **Risk: very low. This is the safest new result here.**

**8. lem:perturb — GUE perturbation ⇒ GUE(m) compression ⇒ GUE spacings.**
`PA:749-790`. Load-bearing for `exp:multi`, `exp:beta`, the abstract's headline
(iii), R30/R31, and every "WD-not-Poisson" statement in runs 30–54. Tagged
"PROVEN (sketch)". **Risk: low mathematically, high interpretively** — it makes the
perturbed-spectrum results near-tautological, which the paper concedes and the
LEDGER's headlines ("BREAKTHROUGH — PERTURBED SPECTRUM FOLLOWS WIGNER-DYSON",
`L:2162`) do not.

**9. T2/T2′ — torsion `U_A^K = χI` and the resulting failure of naive BGS.**
`L:57-79`. Defines the whole object of study (the degenerate eigenspaces) and
supplies the programme's justification. Classical, correctly attributed.
**Risk: none.** Note that T2′ is also the strongest *negative* claim in the corpus
and is never in tension with anything.

**10. R2 — necessity of `gcd(N, tr(A)²−4)=1`.**
`L:603-606`. A hypothesis, not a theorem, but it re-scopes T7, T9, T12 and R1 and
therefore sits above them in the dependency order. It is the reason several
"unconditional" tags are wrong. **Risk: none; propagation: incomplete.**

*Just below the cut, and worth naming because they are cited as if load-bearing:*
U2/collision lemma (cited as the Lean-formalised anchor — evidence missing, §3/D-4);
T18-barrier (cited to justify abandoning the moment method, then ignored for ten
runs); the OSV-conditional smooth law (cited as PROVEN in four documents — §5/S-1
of the verdict, §1.10).

---

## 6. FURTHER VERIFIED DEFECTS (not covered above)

**6.1 The paper source cannot compile.** `\begin{remark}` × 8, `\end{remark}` × 7.
`rem:rev` opens at `PA:363` and is never closed; `rem:reversing_degenerate`
(`PA:376`, added 2026-08-28) is nested inside it; the single `\end{remark}` at
`PA:411` closes the inner remark. TeX will fail with
"`\begin{remark}` on input line 363 ended by `\end{document}`". `.tex` mtime
2026-08-28 12:48; `.pdf` mtime 2026-08-27 02:22. `L:3843-3850` and `PA:50-52`
instruct a future recompile without noting that the file is broken; `L:3806-3812`
claims "paper.tex has 5 new status-table rows … The .tex is NOT recompiled" and
`L:3873-3876` calls the workspace "reviewer-grade".

**6.2 THEORY.md is textually corrupted in two places.**
(a) `TH:181-182`: "…c=−1 would give a" / "Measured: c = +1 for **every**…" — the
sentence is truncated mid-clause; the words "Kramers degeneracy (β=4, GSE)" are
lost (they survive at `L:254-255`). A reader of THEORY alone never learns what
c=−1 would mean.
(b) `TH:719`: a stray `</input>` tag sits between §8.0.4 and §8.0.5 — a
tool-artifact pasted into the theory document.

**6.3 LEDGER structural damage from append-only editing.**
(a) `L:4003` is `## RUN 69` and `L:4005` is `## RUN 68` — the headers are
inverted, and R69's body resumes at `L:4037` after R68's block.
(b) `L:3453` ("theory applies; if no, the wall is somewhere new. v3 will test
this.") is an orphaned fragment of R61's final sentence, stranded *inside* R62 by
a later insertion.
(c) `L:4308` ("is and is not proven.**") is the orphaned tail of R66's concluding
sentence at `L:3877-3879`, pushed to the end of the file by the R67–R70 appends.
The last line of the ledger is therefore a fragment of an entry four runs earlier.

**6.4 The campaign rigidity number compares mismatched window lengths.**
`L:880-882` states "`Σ²(64)=1.161±0.060` (sym) vs GOE control 0.891, Poisson
11.06: rigidity ~9.5× below Poisson at L=64". I read both artifacts:
`campaign_pooled.json` gives sym `nvar["64"] = 1.1612 ± 0.0596` and
`checks.numbers = {goe_ctl_max: 0.8915, poi_ctl_max: 11.0626}`, while
`campaign_state.json`'s control block gives GOE `nvar` = {…, "16": 0.8915, "32":
0.8785, "64": 0.8057} and Poisson `nvar` = {…, "32": 11.0626, "64": 8.3311}.
So the quoted "GOE control 0.891" is the control's **L=16** value and "Poisson
11.06" is the **L=32** value, both compared against a measurement at **L=64**.
Against the correct L=64 controls the numbers are 1.161 vs GOE 0.806 and Poisson
8.33, i.e. **7.2× below Poisson, not 9.5×**, and 44% above the GOE control rather
than 30%. Additionally `campaign_pooled.json` reports `all_pass: true` with the
key `P3_rigidity_relaxed`, while `campaign_state.json` reports
`prereg_all_pass: false` — and the same state file's own estimator gives sym
`Σ²(64) = 1.0271`, not 1.161. The red team identified the estimator/provenance
inconsistency (`review/redteam_run5.md` §C4) and `L:878-886` records "corrections
accepted … Σ² absolute values carry estimator systematics at this level"; the
mismatched-L comparison itself was never corrected and the numbers at `L:880-882`
still stand.

**6.5 Repeated sign errors are a systemic defect, never treated as one.**
Four independent sign/inversion bugs are recorded: the r=6 brute force
(`L:2508-2512`, retracting five runs of data), the r=4 brute force
(`L:1536-1538`), `proj_order` returning `n//2` and `matrix_order_mod_p` returning
`n//2+1` (`L:2739-2743`, corrupting the K-labels in the paper and in R27), and the
`find_orbit_H` split-only assumption that "returns None silently" (`L:1684-1685`,
listed as a fragile point in three separate handoffs and never fixed). No entry
proposes a systematic remedy (e.g. a negative-control gate on every enumerator),
although the project demonstrably knows how to write negative controls (X6,
`L:788-789`).

**6.6 `L:1399-1412` is the only in-place retraction warning in 4308 lines.**
It was added at R65/R1.5, twelve runs after the retraction it announces. Every
other retracted block (R16/R22/R24 r6 data, R20's constant-1 tail bound, R13's
quantum experiment narrative at `L:1695-1713`, R11-C at `L:1481-1497`, T16's
form-factor verdict, C1's refuted empirical support at `TH:309-311`) is still
readable in place with its original confident tag. Given that the project's own
stated failure mode is "Reading R10-B or R11-C without reading R12-A produces a
**false positive**" (`L:1406-1409`), the same hazard exists uncorrected at six
other locations.

**6.7 Two mutually inconsistent renderings of OSV Cor. 2.9.**
`L:1028-1031` and `drafts/tail_bound_proof.md:61`: `k > p^{3/7+ε}` ⇒
`|S| ≪ min{k^{23/36}p^{1/6}, k^{20/27}p^{1/9}} = k p^{−δ}`, `δ ≥ (7/27)ε`.
`TH:537-542`: `sup|S| ≤ C·p^{1/2+1/14+ε}·k^{1/2}` valid for `k > p^{1/2+ε}`.
These are different statements about the same corollary, in the same workspace,
and the second one is the version written into THEORY on 2026-08-28 as the
canonical "T21 best available bound". Neither is checked against the actual paper
(the PDF is not in `literature/pdf/`, which holds only `gh11.pdf` and
`katz_kr.pdf`).

**6.8 R6.4's own conclusion contradicts the later OSV-conditional claim.**
`L:1036-1041`: "inserting the OSV bound yields extras ≤ k³p^{−2δ} hence relative
error o(1) iff `k ≪ p^{2δ}`; the OSV admissible range `k > p^{3/7+ε}` does **NOT
overlap** `k ≪ p^{2·7ε/27}` for realistic ε. CONCLUSION: the published pointwise
technology bites only for very small k." That is: OSV's regime and the regime
where OSV helps are disjoint. R54 then claims OSV yields a PROVEN smooth law
precisely on `k ≥ p^{3/7+ε}` (`L:2885-2888`). The two conclusions are not
reconciled anywhere; the second is the one that reached the paper.

---

## 7. WHAT A REFEREE WOULD DEMAND BEFORE ANY SUBMISSION

Ordered by severity.

1. **Delete `(max/median ≈ 15–40 …)` from `PA:881`.** It is a retracted
   fabrication (RET-12) sitting in the paper's open-problem section as a physical
   explanation. Replace with the verified `taskA_entry_gaussianity.json` numbers
   (`ev_max/std ≈ 3.8, 5.0`; eigenvalue excess kurtosis 5.9, 9.3).
2. **Downgrade the smooth-law row (`PA:968-971`) and `cor:domination`'s second
   clause (`PA:975-976`) from PROVEN to OPEN/heuristic**, or write the
   nested-completion argument for proper subgroups. As it stands the only document
   containing the argument labels it "heuristically" and then proves it invalid for
   subgroups (`drafts/tail_bound_attempt.md:36`, `:49-62`, `:78`). Also drop
   "at unit constant C=1": the derivation carries `(log p)^{O(1)}`.
3. **Fix the U4 status row (`PA:929-935`, `TH:436-472`)** to state the red team's
   actual correction (`extras ≤ k⁴p^{−2δ}`, threshold `k ≲ p^{δ}`, verdict
   "conditional sketch with incorrect quantitative conclusion") or remove the
   claim of red-team endorsement.
4. **Reconcile `PA:957-958` / `TH:599-604` ("r ≤ 4 proven unconditionally") with
   `PA:975-976` (`cor:domination` conditional on a conjecture).** One of the two
   must change. R12-A's own text says the unmatched part needs an unwritten
   argument.
5. **Close the `\begin{remark}` at `PA:363`** before anyone attempts
   `op:paper_recompile`.
6. **Restore or regenerate `src/theta_sign.py`, `src/rigidity.py`,
   `src/birkhoff_density.py`**, and correct `L:3615-3629`, which makes a false
   claim about which code produced `theta_sign.json`. Until then T13's coverage
   claim ("every reversing involution in the scanned box") must be narrowed to
   "the 6–7 involutions recorded per configuration".
7. **Withdraw or restate the Ring-2 empirical headline** ("Weil essentially tight,
   0.99999"). The correct reading of `line_B_big_sweep.json` is that the *trivial*
   bound `|S| ≤ k` is nearly attained at small k, and that lines A/B/C use
   different denominators.
8. **Withdraw the "R54 claimed k ≥ 50" premise** from R68/R69/R70 and
   `TH:§8.0.5–8.0.7`, and either run R54's actual requirement (real centraliser
   basis at m ≥ 70) or state plainly that ten tool versions have not yet done so.
9. **Record the p values for the v9 universality points** (`L:4202-4204` prints
   "(best)"), and drop the two incompatible ad-hoc explanations of the 7842×
   figure until `op:r11_universality` has run.
10. **Add in-place retraction warnings** at `L:1481-1497` (R11-C),
    `L:1792-1810`/`L:2011-2038` (r6 sign bug), `L:1907-1925` (constant-1 tail
    bound), `L:1695-1713` (quantum experiment), `TH:309-311` (refuted C1 support),
    and move `run16_r6.json`/`run22_classify.json`/`run25_partition.json` into
    `artifacts/retracted/`.
11. **Fix `artifacts/ring2/discriminator.json`** (invalid JSON) and the two broken
    paths in `artifacts/ring3/REPRO.md`, whose stated purpose is that "a fresh
    agent … can locate every cited artifact".

## 8. WHAT IS ACTUALLY SOLID

For balance, and because a hostile referee should still be accurate: the following
survive scrutiny with correct tags, present evidence, and no contradictions found —
`thm:core`/T17, `lem:zerocounts`, `thm:meanlaw`, T2, T2′, T6, T7 (with its
hypothesis), T19, R1/A2 multiplicity rigidity, R2 hypothesis necessity, R3/A3
pooled moments, R4 factorisation, the R9→R9-E character expansion, `conj:tight`
and `conj:unified` **as conjectures**, R21/R26/R28/R29 (the negative result on raw
compressions), R49 (the negative result on arithmetic perturbations), T18 and its
barrier, and `lem:perturb` as a sketch. That is a real body of work. The problem is
not the mathematics that was done; it is the four or five places where the
bookkeeping asserts more than the mathematics delivers, and the ~47 missing files
that make several of the strongest claims unauditable.

---
*End of audit. No project file was modified.*
