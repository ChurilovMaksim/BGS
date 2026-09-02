# Pointwise bounds for twisted Kloosterman-type sums over multiplicative subgroups

Object of study:

    S(a,b) := sum_{h in H} e_p(a*h + b/h),   H = <alpha> <= F_p^*, |H| = k,  (a,b) not both 0 mod p.

This is the "generalized Kloosterman sum" K(a,b,p,Lambda) / K_p(G;a,b). Findings verified
2026-08-24 from: (i) full text of Bourgain-Garaev arXiv:1211.4184 (local copy),
(ii) full text (ar5iv HTML) of Ostafe-Shparlinski-Voloch arXiv:2110.10941,
(iii) full text (ar5iv HTML) of Burkhardt-Chan-Currier-Garcia-Luca-Suh arXiv:1505.00018,
(iv) arXiv API metadata searches.

---

## 1. VERIFIED STATEMENTS

### [VERIFIED-STATEMENT] Ostafe-Shparlinski-Voloch, Corollary 2.9 — explicit power saving for k > p^{3/7+eps}

- Source: A. Ostafe, I. E. Shparlinski, J. F. Voloch, "Equations and character sums with
  matrix powers, Kloosterman sums over small subgroups and quantum ergodicity",
  arXiv:2110.10941 (v1 Oct 2021; v2 supersedes arXiv:2108.13146). Published in
  Trans. Amer. Math. Soc. (per authors' page; arXiv is the verified source here).
- Statement (verbatim form): for p prime and G a multiplicative subgroup of F_p^* of order tau,

      K_p(G; a,b) = sum_{u in G} psi(au + b u^{-1}) << min{ tau^{23/36} p^{1/6}, tau^{20/27} p^{1/9} },

  with implied constant depending only on the matrix dimension n = 2.
- Exact hypotheses on k vs p: none needed for the inequality itself, but it is NONTRIVIAL
  (beats the trivial bound tau) exactly when tau > p^{3/7+eps} (Remark 2.11, verbatim:
  "Theorem 2.7 is nontrivial whenever tau > p^{3/7+eps} ... similarly for Corollaries 2.9
  and 2.10"; Corollary 2.9 comes from Theorem 2.7, the split case).
- Power-saving-in-p form: writing theta = log_p k, one has |S| <= k * p^{-delta} with

      delta(theta) = min{ (13/36)theta - 1/6 , (7/27)theta - 1/9 } > 0  iff  theta > 3/7,

  so in particular delta >= (7/27)*eps > 0 whenever k >= p^{3/7+eps}; at k ~ p the saving is
  min{7/36, 4/27} = 4/27. (Branch crossover at theta = 6/11.)
- Fine-print hypotheses inherited from the proof (via Theorem 2.7 applied to
  A = diag(g, g^{-1}), g a generator): requires ab <> 0 and g^2 <> 1 (i.e. k > 2); if
  a = 0 or b = 0 the sum degenerates to a Gauss sum over a subgroup (monomial case), which
  is covered by older separate literature (see item 1d below), not by this corollary.
- Uniformity in (a,b): YES — uniform in all pairs (a,b) with ab not ≡ 0 mod p (any nonzero
  pair), constant independent of (a,b); degenerate one-term cases handled separately.

### [VERIFIED-STATEMENT] Bourgain 2005 — implicit power saving down to k > p^eps (delta NOT explicit)

- Source: J. Bourgain, "Mordell's exponential sum estimate revisited", J. Amer. Math. Soc.
  18 (2005), 477-499. (Not on arXiv; statement below is the characterization given in
  Ostafe-Shparlinski-Voloch arXiv:2110.10941, Remark 2.11, verbatim:)
- Statement: "Bourgain [3] gives a nontrivial bound of the form S_{2,p}(a,b,A) << tau^{1-delta}
  provided tau > p^eps, with some delta > 0 depending only on eps; however this dependence is
  not explicit and it is not obvious how to get such an explicit result."
- Applied to our sum via their reduction (S_{2,p}(a,b;A) = sum_x psi(a A^x b) with
  A = diag(g,g^{-1}) reproduces S(a,b)): |S(a,b)| <<_eps k^{1-delta} = k * p^{-tilde-delta}
  for every fixed eps > 0 with k > p^eps, where tilde-delta = delta*(log_p k) >= delta*eps.
- Exact hypotheses on k vs p: k > p^eps for some eps > 0 (any subgroup size above p^eps);
  conclusion is a genuine power saving but INEFFECTIVE (no numerical delta printed).
- Uniformity in (a,b): yes within the matrix-sum framework (nonzero vectors a,b satisfying
  the linear-independence conditions, which for diag(g,g^{-1}) again means ab <> 0, k > 2).
  CAVEAT: exact primary-source hypotheses (which rational functions f Bourgain's theorem
  allows) were not re-verified from the JAMS paper itself; the OSV paraphrase is the source
  used here.

### [VERIFIED-STATEMENT] Weil baseline (uniform square-root bound, no k-hypothesis)

- Source: Ostafe-Shparlinski-Voloch arXiv:2110.10941, Section 2.2, verbatim: "the Weil bound
  of exponential sums with rational functions implies that K_q(G;a,b) << q^{1/2}, unless
  a=b=0, which becomes trivial for subgroups G of order tau < q^{1/2}."
- Conclusion: |S(a,b)| << p^{1/2} uniformly for all (a,b) != (0,0), all k. This is a saving
  over trivial k only when k > p^{1/2}; it is the yardstick that makes the OSV corollary
  ("first known bound nontrivial below the square-root threshold", Remark 2.12) significant.

### [VERIFIED-STATEMENT] Degenerate cases a = 0 or b = 0 (monomial/Gauss-subgroup sums)

- Source: same paper, Remark 2.12: for Gauss sums G_p(G;a) = sum_{u in G} psi(au)
  (= (1/s) sum_x e_p(a x^s), s = (p-1)/tau), "the first bound of this type has been obtained
  in Shparlinski, 'Estimates for Gauss sums', Mat. Zametki 50 (1991), 122-130" and then
  improved/extended in many works (their refs [3,5,6,7,8,12,17,20,21,29,38,40,49], incl.
  Bourgain-Chang C. R. Acad. Sci. Paris 342 (2006)).
- So when exactly one of a,b vanishes there are explicit power savings available from that
  separate monomial theory (with its own k-vs-p hypotheses); they do not cover the genuine
  two-term case.

### [VERIFIED-STATEMENT] Special subgroups only: explicit evaluations, no general pointwise law

- Source: P. Burkhardt, A. Z.-Y. Chan, G. Currier, S. R. Garcia, F. Luca, H. Suh, "Visual
  properties of generalized Kloosterman sums", arXiv:1505.00018, J. Number Theory 160 (2016),
  237-253. They study exactly K(a,b,m,Lambda) = sum_{u in Lambda} e((au + bu^{-1})/m) but
  prove only structural/special results: hypocycloid confinement for fixed small odd d
  (order-d subgroups), explicit evaluation via Sale sums for Lambda of index 2
  (|Re K|,|Im K| <= sqrt(p)/2 when p ≡ 3 mod 4, p ∤ ab), partial bounds for index 4.
  No uniform pointwise power-saving-in-p estimate for general k is given or cited.

---

## 2. NEGATIVE FINDING (explicit)

**No published statement provides an EXPLICIT power-saving-in-p pointwise estimate
|S(a,b)| <= k*p^{-delta} with printed delta for subgroup sizes k < p^{3/7}.**

Supporting evidence (all verified):
- Ostafe-Shparlinski-Voloch, Remark 2.11: their explicit bound is nontrivial only for
  tau > p^{3/7+eps} (Cor. 2.9) resp. p^{5/11+eps} (Cor. 2.10, norm-subgroup/Gauss case), and
  the only tool reaching smaller subgroups — Bourgain's Mordell-type estimate — has a
  delta = delta(eps) whose dependence "is not explicit and it is not obvious how to get such
  an explicit result."
- Same paper, Remark 2.12: Corollary 2.9 "is the first known bound of this type which is
  nontrivial below the square-root threshold" (for the two-term Kloosterman case).
- Bourgain-Garaev arXiv:1211.4184 (full-text checked): its multilinear Kloosterman estimates
  (Theorems 11, 12, 13) are all for INTERVALS I_1,...,I_n (e.g. Thm 13: product of interval
  lengths > p^{1/2+eps} => max_a |sum alpha_i e_p(a x_1*...*x_n*)| < p^{-delta}|I_1|...|I_n|).
  The word "subgroup" occurs only for additive subgroups/lattices in geometry-of-numbers
  lemmas and in references to Iwaniec-Kowalski Thm 12.21. NO multiplicative-subgroup section;
  the interval theorems do not transfer to H = <alpha>.

Nearest results that do NOT close the gap:
- Garcia-Voloch-type polynomial bounds: the Voloch curve-point machinery (Voloch, Acta
  Arith. 52 (1989), 197-201; #points <= 4 d^{4/3} p^{2/3}) yields k^{2/3}-type savings only
  in the MONOMIAL/Heilbronn setting (Heath-Brown-Konyagin line); no printed k^{2/3} bound
  was found for the two-phase function au + b/u over subgroups prior to OSV 2021, whose new
  use of exactly this machinery is what produces Corollary 2.9. Note also that a k^{2/3}
  bound is a power saving in k, not in p (becomes k*p^{-delta} only for k >> p^{3delta}).
- Shkredov, "On exponential sums over multiplicative subgroups of medium size",
  arXiv:1311.5726: different sums (bilinear/additive-combinatorial), sizes near p^{1/2};
  not pointwise twisted Kloosterman.
- Macourt-Petridis-Shkredov-Shparlinski, arXiv:2003.03493 (SIAM J. Discrete Math. 34 (2020)):
  trilinear sums with variables in products of subgroups — averaged objects, not pointwise.
- OSV Comments (Sec. 9): their method also gives 6th-moment bounds for these subgroup
  Kloosterman sums — average information only.

---

## 3. SUMMARY — what applies to S(a,b) = sum_{h in H} e_p(ah + b/h)

| Regime for k = |H| | Best printed pointwise bound | Effective? | Source |
|---|---|---|---|
| any k, (a,b)!=(0,0) | \|S\| << p^{1/2} (Weil/rational fn) | yes | OSV §2.2 |
| k > p^eps, ab<>0 | \|S\| << k^{1-delta}, delta=delta(eps)>0 | saving real but delta NOT explicit | Bourgain JAMS 2005 (via OSV Rem. 2.11) |
| **k > p^{3/7+eps}, ab<>0** | \|S\| << min{k^{23/36}p^{1/6}, k^{20/27}p^{1/9}} = k*p^{-delta}, delta >= (7/27)eps | **yes** | OSV arXiv:2110.10941, Cor. 2.9 |
| a=0 or b=0 | separate monomial/Gauss-over-subgroup theory (explicit savings since Shparlinski 1991) | yes | OSV Rem. 2.12 + refs |
| k < p^{3/7}, two-term case | NOTHING explicit in print | — | negative finding above |

Uniformity: the OSV corollary and the Weil baseline hold uniformly over all admissible
(a,b) with constants independent of (a,b); the only side conditions are ab <> 0 mod p and
k > 2 (else trivial/degenerate).
