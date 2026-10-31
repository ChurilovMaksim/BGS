# Lines M and N external sources (31 October 2026; Lines M/N integration)

Lines M and N (`mathematics/fixed-map/lineMN_conductor_structure.md`, BGS-TRACE-269…285) use four new external theorems, all in
Line N. The registry is `literature/external_dependencies.json`, and this note is the review record. The statements were read by
the Line N author and the referee (REPORT_N_v2.md §2; referee report items (3)–(4)). The bibliographic metadata was re-checked at
integration on 2026-10-31 (UTC+5) against the publisher/DOI landing pages and the arXiv abstracts. Third-party PDFs are **not** copied
into the repository.

## EXT-OSV-2023: absolute irreducibility (new)
* **Identity.** A. Ostafe, I. E. Shparlinski, J. F. Voloch, "Equations and character sums with matrix powers, Kloosterman sums over
  small subgroups, and quantum ergodicity", Int. Math. Res. Not. IMRN 2023, no. 16, 14196–14238, DOI 10.1093/imrn/rnac226;
  arXiv:2110.10941. The arXiv text was read; lemma numbers follow it.
* **Used.** Lemma 4.3: (Xˢ+Yˢ+a)(Xˢ+Yˢ+bXˢYˢ) − XˢYˢ is absolutely irreducible for gcd(s, q) = 1 and ab(ab−1) ≠ 0. This enters
  BGS-TRACE-279 (N1.2(b)) and, through it, 280.
* **Context, not load-bearing.** The moment inequality (6.6) is re-derived in N1.1 without constants. Theorem 2.7 / Corollary 2.9 have
  implied constants that are not stated, so they are not used numerically. Remark 2.11 notes that Bourgain's δ is not explicit.
* The Line N author notes (REPORT_N §2) that the IMRN Lemma 4.4 omits "+3p" in the point count. The registry therefore uses EXT-OSV-2024 for the count.

## EXT-OSV-2024: Voloch's point count via OSV (new)
* **Identity.** A. Ostafe, I. E. Shparlinski, J. F. Voloch, "Weil sums over small subgroups", Math. Proc. Cambridge Philos. Soc. 176
  (2024), no. 1, 39–53, DOI 10.1017/S0305004123000415; arXiv:2211.07739.
* **Used.** Lemma 2.1 quotes Voloch, Acta Arith. 52 (1989) 197–201, Theorem (i): for F absolutely irreducible of degree d < p,
  #{F = 0} ≤ 4d^{4/3}p^{2/3} + 3p. Voloch's original could not be retrieved (matwbn/impan errors), so it is cited **via OSV**.
* **Not used.** The file `logs/voloch.pdf` in the author's directory is an unrelated paper (N-F5). It is not used and not copied.

## EXT-CP-2011: explicit Heath-Brown–Konyagin bound (new)
* **Identity.** T. Cochrane, C. Pinner, "Explicit bounds on monomial and binomial exponential sums", Q. J. Math. 62 (2011), no. 2,
  323–349, DOI 10.1093/qmath/hap041.
* **Used.** Theorem 1.1, both explicit branches: |Σ_{x∈A} e_p(ax)| ≤ λ|A|^{5/8}p^{1/8} for 3p^{1/3} < |A| ≤ p^{1/2} and
  ≤ λ|A|^{3/8}p^{1/4} for p^{1/2} < |A| ≤ p^{2/3}/3, with λ = 2/3^{1/4} = 1.519671… (the report rounds it down to 1.51967). They enter
  BGS-TRACE-279 (isotropic x) together with the Gauss-period bound √q.
* **Locator check.** The ranges were read in the author preprint dated 5 Oct 2009 (owner audit of PR #65, R2: the lower limit is
  3p^{1/3}, not p^{1/3}/3). The published QJM text was not accessible (the publisher returned 403 on 31 Oct 2026); identity and
  pages checked on Crossref.
* **Range check (integration note I-1, amended after the owner audit of PR #65, R1).** The middle branch is needed for
  c_W p² < q < τ²; with Gauss, middle and 5/8 branches the isotropic case covers the Theorem W⁺ range for every p
  (`computations/verification/lineN/integration_checks/iso_coverage.py`).
* **Not used.** Theorem 1.3 (binomial sums) is worse than Weil here, as Line K already found.

## EXT-BOURGAIN-2005: Mordell's estimate revisited (new)
* **Identity.** J. Bourgain, "Mordell's exponential sum estimate revisited", J. Amer. Math. Soc. 18 (2005), no. 2, 477–499,
  DOI 10.1090/S0894-0347-05-00476-5.
* **Used.**
  * Theorem 1 / Corollary (1.21): complete sums s = 1..p−1 with all a_i ≠ 0, where ord θ_i > p^ε and ord θ_iθ_j⁻¹ > p^ε, are < p^{1−δ}.
  * The case r = 1 (Remark (1), Bourgain–Konyagin) covers the isotropic sums.
  * §5(1): δ_r > exp(−C₃r(ε^{−C₂} + log r)). So the bound is **effective, constants not computed** (N-F6), not "ineffective".
* **Enters.** BGS-TRACE-281.
* **Context only, not registered.**
  * Bourgain–Glibichuk–Konyagin, J. London Math. Soc. (2) 73 (2006) 380–398, DOI 10.1112/S0024610706022721. Only the abstract was
    read.
  * Bourgain, J. Anal. Math. 101 (2007) 325–355 (finite rings). It was not read, so BGS-TRACE-282 is open.
  * Bourgain, LNM 1910 (2007).

## Annotation only (no registry row)
* **Kurlberg–Rudnick**, "On quantum ergodicity for linear maps of the torus", Commun. Math. Phys. **222** (2001), no. 1, 201–227,
  DOI 10.1007/s002200100501. The volume was checked against the publisher's page. The Line M referee's "221" is a slip, and the
  author's recollection (222) is correct. It is cited in the M7b annotation of BGS-TRACE-277 only.
* **Faure–Nonnenmacher–De Bièvre**, Commun. Math. Phys. 239 (2003) 449–492. Analogy only (M7b, Line L3 notes).
* **Stewart**, Acta Math. 211 (2013). Cited in the N5 notes only.
