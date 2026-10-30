# Line I external sources (31 October 2026; owner audit of PR #60, fix R1)

These are the external theorems that BGS-TRACE-215 and BGS-TRACE-219 rest on. They are registered in
`literature/external_dependencies.json` with this note as the review record. Fetches were made on 2026-10-31 from the box
(UTC+5).

## EXT-RS-1962: Rosser–Schoenfeld, Theorem 15
* Identity: J. B. Rosser, L. Schoenfeld, "Approximate formulas for some functions of prime numbers", Illinois J. Math. 6 (1962),
  no. 1, 64–94, DOI 10.1215/ijm/1255631807. The metadata was corroborated by Crossref: title, authors, journal, volume 6, issue 1,
  issued 1962-03-01.
* Primary text: a scan of the journal article (31 pages) was downloaded from https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf,
  2,520,753 bytes, sha256 8e37b06f82e09421bceb2502578c47b61469141f0287e6acedb70e01765ab556. Its text layer was inspected with
  `pdftotext`. The scan carries journal pages 64–94; the copy is not the publisher's file.
* Locator: Theorem 15, journal pp. 71–72 (pdf pages 8–9), inequalities (3.40)–(3.42). For 3 ≤ n,
  n/φ(n) < e^γ log log n + 5/(2 log log n) (3.41), except n = 223092870 = 2·3·5·…·23, where
  n/φ(n) < e^γ log log n + 2.50637/log log n (3.42). Since 5/2 < 2.50637, (3.42) holds for every n ≥ 3.
* Application (BGS-TRACE-215): φ(2h_m) = φ(h_m) ≥ h_m/(e^γ lnln h_m + 2.50637/lnln h_m), with n = h_m odd and ≥ 3. Since h_m is odd,
  the exceptional n (which is even) cannot occur, and in any case (3.42) covers it. This is used in the bound
  7Σ_u|δ_u|²/φ(2h_m) ≤ (13/7)·48·(CV·1.45^m + CE)²·(e^γ lnln h + 2.50637/lnln h)/h (`cert_v2/bounds_sq_v2.py`, `cert_v3/bounds_sq_v3.py`).

## EXT-BHV-2001: Bilu–Hanrot–Voutier, Theorem 1.4
* Identity: Yu. Bilu, G. Hanrot, P. M. Voutier (with an appendix by M. Mignotte), "Existence of primitive divisors of Lucas and
  Lehmer numbers", J. reine angew. Math. 539 (2001), 75–122, DOI 10.1515/crll.2001.080. The metadata was corroborated by Crossref
  (title, authors, journal, volume 539, issued 2001).
* What was seen of the source:
  * the publisher abstract ("for n > 30, every n-th Lucas and Lehmer number has a primitive divisor");
  * the first page of the publisher text, via a search-engine extract of degruyterbrill.com. It includes the §1 definitions: a Lucas
    pair (α, β) of algebraic integers with α+β and αβ non-zero coprime rational integers and α/β not a root of unity, and
    u_n = (αⁿ−βⁿ)/(α−β);
  * a secondary statement of the theorem with its number, "Theorem 1.4 of [BHV]: for n > 30, the nth term of any Lucas sequence has
    a primitive divisor" (S. Akhtar Arif, F. S. Abu Muriefah, Arab J. Math. Sci., short communication), with the definition
    "p | u_n, p ∤ (α−β)² u_1⋯u_{n−1}";
  * P. M. Voutier, "Primitive divisors of Lucas and Lehmer sequences, II", J. Théor. Nombres Bordeaux (DOI 10.5802/jtnb.168), which uses the same definition.
* Not obtained: the primary PDF. The HAL copy (inria-00072867, RR-3792) is behind a bot challenge from the box, and the publisher
  PDF is paywalled. **The theorem number 1.4 and the statement are therefore corroborated (abstract plus a secondary citation), but
  not read in the primary text, and the page within pp. 75–122 is not pinned.**
* Application (BGS-TRACE-219): α, β = 1 ± √2 form a Lucas pair: α+β = 2, αβ = −1, coprime, and α/β = −(1+√2)² is not a root of
  unity. Here u_n = U_n (Pell numbers) and V_n = αⁿ + βⁿ = 2h_n. For n = 2m > 30, i.e. m ≥ 16, a primitive prime p of U_2m satisfies
  p ∤ 8, so p is odd. Also p ∤ U_m, so p | V_m = 2h_m and hence p | h_m. Finally h_{m′} | U_{2m′} with 2m′ < 2m, so p ∤ h_{m′}.
  In Lean, the theorem enters as the hypothesis `hBHV` of `Bgs.LineIArith.finite_set_fails`, which drops p ∤ (α−β)² and is therefore
  implied by Theorem 1.4.

## EXT-CARMICHAEL-1913: Carmichael's theorem on real Lucas sequences (corroborating; not load-bearing)
* Identity: R. D. Carmichael, "On the numerical factors of the arithmetic forms αⁿ ± βⁿ", Ann. of Math. (2) 15 (1913), no. 1/4,
  30–70, DOI 10.2307/1967797. The metadata was corroborated by Crossref.
* Statement, from secondary sources only: for real, non-degenerate Lucas sequences and n ∉ {1, 2, 6}, U_n has a primitive prime
  divisor, except n = 12 for (P, Q) = (±1, −1) (Fibonacci). Sources: M. Yabuta, "A simple proof of Carmichael's theorem on primitive divisors", Fibonacci Quart. 39(5) (2001), Theorem 1;
  Wikipedia "Carmichael's theorem".
* Locator conflict: secondary sources give **Theorem XXIII** (Schweitzer 2025 solutions; Bull. SSMR 65), while Wikipedia gives
  "Theorem 21". The primary text (JSTOR) was not inspected, so the locator is unverified.
* Application: (P, Q) = (2, −1) has D = 8 > 0. This gives a primitive prime of U_2m for every m ≥ 2 with 2m ≠ 6, which is a weaker
  threshold than BHV's m ≥ 16. BGS-TRACE-219 claims m ≥ 16, so BHV alone suffices; Carmichael is recorded as independent
  corroboration.
