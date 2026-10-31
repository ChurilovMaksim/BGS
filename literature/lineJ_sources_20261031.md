# Line J external sources (31 October 2026; Line J integration)

These are the external theorems that Theorem J3 (BGS-TRACE-231) uses to show that S⁺ is infinite under H_arg. They are registered
in `literature/external_dependencies.json` with this note as the review record. Fetches were made on 2026-10-31 from the box (UTC+5).

**Context.** The J3 report v2 (§5) cited "Iwaniec–Kowalski Thm 13.6" for Σ_{p≤x} e(pγ) = o(π(x)), γ irrational, and
"Dirichlet" for the density of p ≡ p₀ (mod 56). Both citations were checked at integration:
* **IK Theorem 13.6** is Vinogradov's **minor-arc** estimate for Σ_{n≤x} Λ(n)e(αn), under the hypothesis |α − a/q| ≤ q⁻².
  * This identification is corroborated by citing papers, e.g. Mauduit–Rivat arXiv:1105.3895, Drmota et al., a University of
    Oxford thesis and MathOverflow 227809, all of which quote it in this form.
  * On its own it does not give o(π(x)) for every irrational γ. For γ with a good rational approximation a/q with q small relative
    to x, the major arcs are also needed (Siegel–Walfisz).
  * So the polished text cites the equidistribution theorem itself (EXT-VINOGRADOV-1937), and keeps IK Ch. 13 and Vaughan,
    *The Hardy–Littlewood Method*, Ch. 3 as chapter-level textbook references only.
* **Dirichlet's theorem** (already registered as EXT-DIRICHLET-1837) gives infinitely many p ≡ p₀ but no density. The density used
  is the prime number theorem in arithmetic progressions (EXT-DAVENPORT-1980).

## EXT-VINOGRADOV-1937: equidistribution of (pγ) mod 1
* **Identity.** I. M. Vinogradov, *The Method of Trigonometrical Sums in the Theory of Numbers*, Interscience, London–New York 1954
  (transl. K. F. Roth and A. Davenport), Chapter XI. It was first announced in Vinogradov, "The representation of odd numbers as a
  sum of three primes" (Russian), Dokl. Akad. Nauk SSSR 15 (1937), 291–294. No DOI.
* **Where it was located.** L. Kuipers, H. Niederreiter, *Uniform Distribution of Sequences* (Wiley 1974), Chapter 1 §2 Notes,
  author-hosted PDF https://web.maths.unsw.edu.au/~josefdick/preprints/KuipersNied_book.pdf (4,185,358 bytes, sha256
  b52cc1f9a3fa41489d6cb09897608e80644319a3de4a77c284a3671117068b98; text layer read with `pdftotext`). It states that (p_nθ),
  θ irrational, is u.d. mod 1, citing "Vinogradov [3, 4; 5, Chapter 11], Hua [1]". Its bibliography identifies [3] = Dokl. 15
  (1937), 291–294; [4] = Izv. Akad. Nauk SSSR Ser. Mat. 12 (1948), 225–248; [5] = the 1954 book.
* **Corroboration.** Davenport, GTM 74, 2nd ed., §§25–26 (contents page and publisher preface): "Vinogradov devised his method in
  order to estimate the sum Σ_{p≤N} e(pα)".
* **Not obtained.** The primary texts (the Doklady note and the book chapter) were not read, so no page is pinned.
* **Application (BGS-TRACE-231).** Take α = 3·arg ξ₂:₁/2π, irrational under H_arg (BGS-TRACE-233), H ≠ 0, and k mod 56. Then
  Hα + k/56 is irrational, and Σ_{p≤x} e(p(Hα + k/56)) = o(π(x)). Averaging over k with the additive characters of ℤ/56 gives
  Σ_{p≤x, p≡p₀ (56)} e(pHα) = o(π(x)).

## EXT-WEYL-1916: Weyl criterion
* **Identity.** H. Weyl, "Über die Gleichverteilung von Zahlen mod. Eins", Math. Ann. 77 (1916), 313–352, DOI 10.1007/BF01475864
  (Crossref: title, author, journal, volume 77, 1916).
* **Statement used.** (x_n) is u.d. mod 1 iff (1/N)Σ_{n≤N} e(Hx_n) → 0 for every integer H ≠ 0, applied to the sequence of primes
  p ≡ p₀ (mod 56) in increasing order.
* **Textbook locator, read.** Kuipers–Niederreiter Ch. 1, Theorem 2.1 (Weyl Criterion); their Notes attribute it to Weyl [2, 4],
  with [4] = this paper.
* **Not obtained.** The primary page of the criterion within pp. 313–352 is not pinned.

## EXT-DAVENPORT-1980: prime number theorem in arithmetic progressions
* **Identity.** H. Davenport, *Multiplicative Number Theory*, 2nd ed., revised by H. L. Montgomery, GTM 74, Springer 1980,
  DOI 10.1007/978-1-4757-5927-3 (Crossref and publisher page: edition 2, XIII + 177 pp.).
* **Locator.** §20 and §22, "The prime number theorem for arithmetic progressions (I)/(II)": π(x; q, a) ~ π(x)/φ(q) for
  (a, q) = 1. Page ranges are taken from the publisher contents page; the text itself was not read.
* **Application (BGS-TRACE-231).** q = 56 gives #{p ≤ x : p ≡ p₀} ~ π(x)/24. With the two items above, (pα) is equidistributed over
  p ≡ p₀ (mod 56). The window arc cos(arg B_j + 2πpα) ≥ 0.84431 then has relative density arccos(0.84431)/π = 0.18001, so S⁺ is
  infinite.

## Not registered
The Lidskii trace theorem and the Weyl (Horn) inequality Σ|λ_i|^m ≤ … for trace-class operators are used in the Weyl bounds of
Theorem J and in the (±2,16) bounds. They are standard and are used exactly as in Lines F and I, which did not register them; this
precedent is followed.
