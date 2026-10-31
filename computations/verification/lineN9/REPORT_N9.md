# REPORT N9 — the Lemma A∞ tail
Labels:
- [P] proved
- [P-sketch] sketched proof
- [CA] arb certificate
- [CA*] float with an a-priori rounding margin on nonnegative matrices
- [N] numerical
- [H] heuristic

N7 fixes (F1, F3, F6, F8–F11) and the Lemma P′(i) erratum are in `REPORT_N7_v2.md`.

## 0. Summary
| # | Result | Status |
|---|---|---|
| 1 | **Referee route computed.** With a Fejér/Selberg majorant (M̂ ≥ 0, compact support) and Poisson summation over the class lattice, the shell sum turns into a near-collision automaton. **Single core** (letters at λ-spacing): rate 1.0511–1.0519 per letter, < 1.481. **But the two cores A and B of one class are driven by the same ζ** (ζ_B = −ε⁻¹ζ_A, Lemma P′). The joint automaton has base ε, with rate **2.32569 per letter**, i.e. 5.409 per λ-step against the needed 1.481² = 2.193. The op·HS·HS shell bound diverges. Hölder splittings (HS⁴, op on one core, S6 norms) give 5.4, 1.855 and 1.855 per depth step, all > 1. | [CA*] rates; reduction [P-sketch] |
| 2 | **R4 by deep-as-generic (Theorem C′):** fails by index loss, not by slow time. A line has ≈ q points against \|G_p\| = q². Theorem C′ gives Σ_line ≤ q²·1.2744^m, while A∞ needs ≲ q·1.42785^m. This would require q ≤ 1.406^p, but q ≈ 2.414^p. Conversely, every class has a balanced representative with \|e_i\| ≲ λ^{k/2}, so Lemma P′ windows exist up to N(e) ≈ q. **No separate deep regime is needed (α = 1)**: the window route covers all depths, including the N8b proper-divisor classes (N(e) ≥ h_p/c). | [P] (arithmetic); [P-sketch] |
| 3 | **Multi-bump ("dilute gas") classes.** Homoclinic seeds ζ = Σ λ^{g_i}ζ_i give classes with one bump per seed. By rank-one collapse, w(class) → ∏ bump factors, *independent of the gaps g_i*. The number of n-bump classes is ~ k^{n−1}/(n−1)!. | [CA] evidence; [P-sketch] mechanism |
| 4 | **Consequence.** Σ_{non-fam}\|w\| at level p grows with p. Any p-uniform A∞ in \|·\| form is **false for large p**. The one-sided form likely fails at p ≳ 6·10³ via 5-bump terms ∝ k⁴w*⁵ (Re < 0) and the resummed phase of sinh(k w*). | [P-sketch] + [CA]/[N] evidence; threshold [H] |
| 5 | **Finite part extended:** missed class z = 0, e = 4 certified positive (dropped). All 4 fixed points enumerated; z = √2/8 and ¼+√2/8 classes are ≤ 1e-24 and decay in p. | [CA] / [N] |
| 6 | Lemma A∞: **not proved**. In its p-uniform form it is very likely false. Proposed replacement in §5. | — |

## 1. Shell majorant → near-collision automaton
**Setup.**
- Classes in the box |e₁| ≤ X₁, |e₂| ≤ X₂ form a lattice Λ_e (a coset of 2O or 2√2O).
- Core twists are exactly linear in (ζ₁, ζ₂) = Minkowski(ζ_A), up to the O(|e|λ^{−k}) linear corrections of identity (I):
  - left half d_j = λ^jζ₁, right half −λ^{−j}ζ₂ (core A);
  - for core B, ζ is replaced by −ε⁻¹ζ.

**Majorants.**
- Lemma O1 (Line L) gives HS²(core) ≤ C_pair·Σ_v Πρ_j(v_j) e(Σ v_jd_j), with ρ̂_j ≥ 0, and ρ̂_j ≤ g_j pointwise, where g_j has finitely many letters and nonnegative coefficients (Prop E).
- Fejér majorant: M(x) = (π²/4)·sinc²(x/2) ≥ 1_{[−1,1]}, with M̂ ≥ 0 supported in |ξ| ≤ ½ and ∫M = π²/2.

**Reduction.**
- Poisson summation over Λ_e: Σ_{box} Π g(d(ζ)) ≤ (X₁X₂/covol)(π²/2)²·Σ_{ξ∈Λ_e^*} Σ_v Πg(v_j)·1[|α_i(v) − ξ_i| ≤ 1/(2X_i)].
- The left/right conditions are one-dimensional near-collisions.
- The Horner states S = Σ v_iβ^{i+I} ∈ Z[√2] stay in the finite box |S| ≤ (V+η)/(β−1), |S′| ≤ V/(1−|β′|).
  - Use backward recursion for S and forward recursion for S′.
  - The finitely many ξ act as boundary letters.
- So the shell average is ≤ C·ρ(F_β)^{#letters}. The tolerance η only enters C. [P-sketch: all steps are standard; constants not computed.]

**Rates** (`code/b_automaton.py`, `logs/b_automaton.jsonl`; 8V weights at τ_mid ≤ 1.68e-11; tails folded into g(0)):

| automaton | V | states | ρ (power iteration) | CW upper [CA*] |
|---|---|---|---|---|
| single core, β = λ | 12 / 20 | 57 / 151 | 1.05193 / 1.05112 | 1.0519341 / 1.0511160 |
| A+B interleaved, β = ε | 12 / 20 / 28 | 269 / 719 / 1385 | 2.32608 / 2.32569 / 2.32569 | 2.3260751 / 2.3256934 / 2.3256934 |

**Exponent bookkeeping.**
- Per class, |Ẑ_e| ≤ ‖Q‖_op‖Q‖²_HS with Q = S₁C_AS₂C_B. This is ≤ C·μ*^{3p−6D}Λ^{2D}·HS²(C_A)HS²(C_B), where D = log_λ N(e) and #classes in a shell ~ λ^D.
- Convergence needs λΛ²r_J²/μ*⁶ < 1, i.e. r_J < μ*³/(Λ√λ) = 1.4810 per ε-letter. Here r_J is the **joint** rate.
- r_J = 2.3257 > 1.481, so the majorant diverges.
- The single-core rate 1.0512 is the referee's r₂(η). It is the right number only if A and B were independent; they are not.
- Alternatives, all > 1:
  - HS on A, op on B: 1.855 per D;
  - Schatten-6 Hölder: 1.855;
  - HS⁴ Cauchy–Schwarz: 5.4 per λ-step.
- **Verdict:** the averaged (restricted Theorem C) route cannot close A∞ with these majorants [CA* + P-sketch].

## 2. Deep points (R4)
- **Index loss [P].** Restricting Theorem C′ to one line costs a factor q relative to the G_p average, as computed in row 2 of §0. The loss is the index, not slow time.
- **Windows persist [P-sketch].**
  - x is defined mod 2√2γ̄O, so every class has e with |e₁|, |e₂| ≤ C√q (unit balancing).
  - The Lemma P′ error |e|λ^{−k} is therefore ≤ Cλ^{−k/2+O(1)}.
  - The windows (total fast time 2·log_λN(e) ≤ p) are well defined for every class.
- Hence the deep regime needs no new idea beyond what fails in §1. The same holds for N8b's proper-divisor classes, which have N(e) = (h_p/c)N(f).

## 3. Multi-bump classes (dilute gas)
- **Valid classes.** At z = ¼ the class is e = 2α with α of odd norm. A sum of seeds is valid iff it contains an odd number of odd seeds. Examples:
  - α = 1 + s√2λ^g (family bump plus a "half" bump);
  - α = 1 + λ^{g₁} + λ^{g₂} (three family bumps).
- **[CA] (n9_cert = N8 certificate, unchanged machinery):**

| class | Re w | \|w\| ≤ |
|---|---|---|
| 1+√2λ^g, g = 1…6 (and s = −1) | g ≥ 3: [1.5e-9, 2.1e-8] (Re > 0) | 2.4–2.7e-8, **flat in g** |
| 1+λ^{g₁}+λ^{g₂}: (2,5), (3,7), (4,9) | — | 1.16e-9, 7.6e-10, 5.4e-10 |

  - For the three-bump classes the midpoints give |r_Ar_B|³ ≈ 6.0e-11 ≈ |w*|³ = 6.18e-11.
  - Also r_A(3-bump) ≈ r_A(fam)³: |·| 0.0285 against 0.0276.
- **Mechanism [P-sketch].** Rank-one collapse across the slow gaps: r(core) = Π r(bump) + O(λ^{−c·min gap}). The proof is Prop X's, applied inside the core.
- **Count.** n-bump classes ≈ k^{n−1}/(n−1)! (relative positions in a half-period). So Σ_{n-bump}w ≈ (k^{n−1}/(n−1)!)·w*^n·(phases), and the odd-bump series resums to ≈ (4p/k)·sinh(k w*) [H].
- **Effect on A∞ [H].**
  - With θ_a = 0.25 the budget is 3.65e-5 per 4p.
  - 3-bump: Re(w*³) ≈ +1e-12 (|w*|³cos(3arg w*), arg w* ≈ −0.518), harmless.
  - 5-bump: k⁴/24·|w*|⁵·0.85 reaches the budget at k ≈ 3.2e3, p ≈ 6.4e3.
  - The resummed sinh(k w*) has arg passing −π/2 at k|w*| ≈ 3.2 (p ≈ 1.6e4), so Re X itself turns negative there.
  - The p = 1165 picture (X ≈ 4p(w* + c₀), < 1% else) is consistent: k|w*| = 0.23.
- **Conclusion.** Lemma A∞ (and the Lin-based Theorem R♯ "for all p ≥ 1165") cannot hold uniformly in p as stated. It can hold for p in a finite window [1165, ~6·10³] [H]. **Flag for the parent: this affects Theorem R♯'s "all p ≥ p₀" claim.**

## 4. Scope statement serving (a) and (b)
**Classes at level h_p on (γ)/(γ̄).**
- **(i) Certified head** (N8 + N9, 18 classes): positive ones dropped; absolute charge ≤ 1.215e-6 + 4.24e-8 + Prop X′ errors.
- **(ii) z ∈ {√2/8, ¼+√2/8}:** exponentially small [N].
- **(iii) Remaining classes, all depths** (including deep classes, multi-bump classes and N8b proper-divisor classes with N(e) = (h_p/c)N(f)):
  - no bound;
  - the averaged majorant diverges (§1);
  - the pointwise hypothesis G(Γ, A) of N8b is **false for p-independent A** on multi-bump classes unless s(x) counts *all* slow time, including internal gaps.
  - With all slow time counted, Lemma Σ's class count acquires the gas factor ~ e^{k·Ψ}, Ψ ≈ Σ_bumps|ψ_b| (~|w*| plus half-bumps ~1e-4). That is e^{O(10⁻⁴p)}, harmless against exponential margins (gap (b)) but fatal for the O(1)-margin A∞ at large p.
- Cross lines → (b′) (REPORT_N7_v2 F6).

## 5. Suggested replacement [H/P-sketch]
- Use N6's Cauchy–Schwarz form Dev_{h_p} ≥ (n|Z|²/d²)(|1+X+Y|² − 1) instead of Lin.
  - It needs |X+Y| ≥ 2, a **modulus** bound, not a sign.
  - The gas resummation gives |X| ≈ 4p|w*|·|sinh(kw*)/(kw*)| ≥ 4p|w*|·(1 − o(1)) along the ray arg = −0.518, where sinh has no zeros. This is ≥ 2 for p ≥ ~1270.
- A proof then needs a lower bound on the *resummed* isotropic sum, e.g. through a transfer operator on bump configurations: a renewal or cluster expansion with bump fugacities ψ_b and certified Σ_b|ψ_b|, plus a bound on non-bump ("chaotic") core parts. Single-bump certificates (N8/N9) are the inputs.
- This is not attempted here.

## 6. Files
- code: n9_cert.py (N8 certificate, output path changed), run_batch.sh, batch_comp.txt, batch_3b.txt, batch_z0.txt, a_bases.py, b_automaton.py
- logs:
  - n9_cert_{comp_*, tri_*, z0_*}.{out,json};
  - a_bases_p29_K40.{out,json}, a_bases_p47_K40.{out,json};
  - b_automaton.jsonl;
  - batch_*.log
- REPORT_N7_v2.md, NOTES_N9.md; hashes in SHA256_N9.txt (+ .sha256)
