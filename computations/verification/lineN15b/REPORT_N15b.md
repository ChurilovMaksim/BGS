# REPORT_N15b — exponential-sum route to sublattice equidistribution beyond the separation time

**Verdict.** No known theorem, proved or conjectural in standard form, yields c < 0.387.
- The exponential-sum route fails at the level of the *individual* sums: these sums do not cancel at this scale (§2).
- The required input is an instance of an open "minimal-period, beyond-Ehrenfest" equidistribution problem, stated exactly in §4.
- The best proved exponent stays c_B = 0.7375 (N14b) [P-sketch].

## 1. Scales [P]
- Every prime q | h_p splits in Z[√2] and ord(λ mod q) = p (computed for all q < 3·10⁶, p ≤ 31; in general ord | p prime and λ ≢ 1).
- For the worst classes q ≈ √h_p ≈ λ^{p/4}: |H| = ord = p ≈ 2.27·log q, so log|H|/log q → 0.
- G_p is the cat map mod N = h_p at period p ≈ 2 log_λ N. This is exactly the minimal-period regime of Faure–Nonnenmacher–De Bièvre.

## 2. Exponential sums over ⟨λ⟩ ⊂ F_q^× [N + literature]

| theorem | hypothesis | here |
|---|---|---|
| Bourgain–Glibichuk–Konyagin (J. LMS 2006); exposition: Kowalski, arXiv:2401.04756 | \|H\| ≥ q^δ, fixed δ>0 | fails (log\|H\|/log q ≈ 0.25–0.41, → 0) |
| Bourgain (sharpest form, as cited by Cochrane–Pinner / IAS notes) | log\|H\| > C log q/log log q | fails (\|H\| ≍ log q) |
| Montgomery–Vaughan–Wooley **conjecture** | \|H\|/log q → ∞ | fails even conjecturally (ratio bounded ≈ 1.8–2.4) |
| Korobov/Niederreiter full-period discrepancy for linear recurrences mod m | period ≳ √m | fails |

Kowalski notes that subgroups of size (log p)^C are open; ours have size ≍ log p.

Direct computation (code/c_orbitsums.py) of max_{a≠0}|Σ_{i<ord} e(aL^i/q)|/ord:

| q | 353 | 599 | 15607 | 424577 | 865087 |
|---|---|---|---|---|---|
| max normalized sum | 0.50 | 0.48 | 0.59 | 0.56 | 0.54 |

So there is no o(|H|) cancellation, as forced by geometry: the shortest dual vector has Tr(λ^i b)/q near 0 for ≈ log_λ q indices. This is the separation obstruction of N14b Lemma 1. Any route that bounds characters one at a time therefore gives nothing beyond c_B.

## 3. Cat-map literature

| paper | result | applies here? |
|---|---|---|
| Kurlberg–Rudnick, Duke 103 (2000) | equidistribution of Hecke eigenfunctions | needs ord ≫ N^{1/2+ε} for full QUE |
| Bourgain, GAFA Seminar, LNM 1910 (2007) | ord(A,N) > N^ε suffices | no: here ord ≍ log N |
| Kelmer, Annals 2010 / higher-dim QE | needs polynomial orders | no |
| Bonechi–De Bièvre, CMP 211 (2000) | coherent states equidistribute for \|log ħ\|/(2γ) ≤ t ≤ \|log ħ\|/γ, i.e. only *up to* Ehrenfest time | — |
| Faure–Nonnenmacher–De Bièvre, CMP 239 (2003) | at near-minimal period ≈ 2 log N/log λ, eigenstates with ½ mass on a periodic orbit exist: quantum equidistribution *fails* in our regime | — |

What we need is classical and weighted, so FNDB does not refute it. But it shows that no regime-free equidistribution theorem can exist at this scale.

## 4. The remaining input, stated exactly

Let F_p(β) = ∏_{i<p} g(Tr(λ^iβ)/h), where g(t) = |Σ_a|J_a(1.8)|e(at)|² (the Prop-E majorant; in C′ the τ-profile variants and the k-block majorants have the same structure).

**(R-mix) [H].** For every ideal 𝔡 | h_p of norm d,
E_{β ∈ H_d mixed} F_p(β) ≤ e^{o(p)}·d^c·r₂^p, with c < 0.387, where H_d mixed means Nβ ≡ 0 (d) and Nβ is a unit mod h/d.

Together with C′'s op/Hölder steps, (R-mix) gives the subgroup lemma.

**Equivalent forms.**
- By Poisson summation over O and inclusion–exclusion over the iso-subgroups, (R-mix) says: the digit measure W_p(b) = Σ_{v(λ)=b}∏ĝ(v_i) summed over the ideal 𝔟 = Ann H_d (index ≈ λ^{p−log_λ d}), minus its β=0 main term F_p(0)/|H|, is ≤ d^c·W_p(0).
- In dynamical terms: the Riesz product of the Pisot unit λ at nonzero points of the admissible lattice (1/h)𝔡 is controlled for a full period p = (Ehrenfest time of H_d) + log_λ d.
- This is the classical Erdős–Pisot non-decay at algebraic points, at the minimal-period scale. I know of no theorem or named conjecture that it is equivalent to. It lies strictly beyond MVW's regime and beyond Bonechi–De Bièvre's time window.

**Evidence [N] (exact enumeration, code/b_majorant_exact.py):** the mixed averages of the majorant sit *below* the full-group average.

| p | E_G F | E_{H_d} F | c_maj = log(E_H/E_G)/log d |
|---|---|---|---|
| 11 | 0.787 | 0.264 (d=23), 0.052 (d=353) | −0.35, −0.46 |
| 13 | 0.994 | 0.180 (d=79), 0.073 (d=599) | −0.39, −0.41 |

This suggests the stronger statement E_mixed F ≤ E_G F (c ≤ 0) [H].

**Correction to N14b (D).** The value c_D = 0.899 is the β=0 term of a *subgroup* average. Mixed sets remove it, so it is not a ceiling for mixed averages; the sampled N15b/a_majorant_ceiling.py run is unreliable (heavy tail) and is superseded by the exact runs. N14b files are unchanged.

Nothing pushed. All jobs ran at nice 19, sequentially (each ≤ ~10 min).
