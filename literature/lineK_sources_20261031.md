# Line K external sources (31 October 2026; Line K integration)

Line K (`mathematics/fixed-map/lineK_harg_removal.md`, BGS-TRACE-234…247) uses one new external theorem and re-uses four that are
already registered. The registry is `literature/external_dependencies.json`, and this note is the review record. Fetches were made
from the box on 2026-10-31 (UTC+5).

## EXT-WEIL-1948: the Weil bound (new)
* **Identity.** A. Weil, "On some exponential sums", Proc. Nat. Acad. Sci. USA 34 (1948), no. 5, 204–207,
  DOI 10.1073/pnas.34.5.204 (PubMed 16578290, PMC1079093; published 15 May 1948).
* **What was read.** The text of pp. 204–205 was read in a search-index extract. It sets up a multiplicative character χ of k*
  and an additive character ω, forms the abelian character p(m) = ω[R_m(1/T)]·χ[R_m(b)] of k(t) with a conductor of degree N + d,
  and uses the fact that the L-series is then a polynomial of degree N + d − 2. The Riemann hypothesis for curves bounds its roots.
* **Not obtained.** Direct fetches of doi.org and pnas.org timed out; pmc.ncbi.nlm.nih.gov returned 403. The final estimates on
  pp. 206–207, including the Kloosterman case |K(a, b; p)| ≤ 2√p, were **not read**, and no equation is pinned.
* **Form used.** For q prime and (a, b) ≢ (0, 0): |Σ_{x∈F_q*} χ(x) e((ax + b/x)/q)| ≤ 2√q (twisted Kloosterman sum). For a Gauss
  sum with χ ≠ 1 the modulus is √q. These are the standard consequences of the paper's estimate, and they are cited that way in the
  Kloosterman-sum literature (e.g. arXiv:0801.4162, which cites this paper). The application status is therefore
  `unverified_application`.
* **Application (Lemma W1, BGS-TRACE-241).** H = ⟨l⟩ ⊂ F_q* has order r(q). Detecting H by the characters of F_q* that are trivial
  on H gives
  Σ_{h∈H} e((Ah + B/h)/q) = (1/e)·Σ_{χ|H=1} Σ_x χ(x) e((Ax + B/x)/q), with e = (q−1)/r.
  This is ≤ 2√q, and ≤ √q if AB = 0. The author and the referee checked the hypotheses (K2 report v2 §2; referee DELTA). W1 is
  used only in Lemma W3 and in the conditional Theorem W / K2′.

## Existing references re-used by Theorem K3 (BGS-TRACE-235)
* **EXT-DIRICHLET-1837** (rational case). Take b′ ≥ 447 and a unit v mod b′ with v ≡ p₀ (mod gcd(56, b′)). The CRT class mod
  lcm(56, b′) is then a unit class, so it contains infinitely many primes. Only infinitude is used; no density is claimed.
* **EXT-VINOGRADOV-1937, EXT-WEYL-1916, EXT-DAVENPORT-1980** (irrational case). These are used exactly as in BGS-TRACE-231 (see
  `literature/lineJ_sources_20261031.md`), now as one branch of an unconditional case split. H_arg is not assumed.

No new source was fetched for these four. Their review status is unchanged.

## Not registered
* **Bourgain extension (K2 report v2 §3, [P-cite], ineffective).** The report cites J. Bourgain, "Mordell's exponential sum
  estimate revisited", JAMS 18 (2005) 477–499, and Bourgain–Glibichuk–Konyagin, J. London Math. Soc. 73 (2006). With them,
  "q ≤ c_k p²" in Theorem W / K2′ could be replaced by "q ≤ p^C" (ineffective p₀(C, k)). The referee's DELTA §D5 table lists this
  extension as [P-cite, ineffective], conditional on OP, but the integration brief's registration list does not include it. It is
  therefore **not registered**, and neither reference is added (deviation recorded in
  `evidence/executions/20261031/lineK/INTEGRATION.md`). The registered Theorem W
  (BGS-TRACE-245) and K2′ (BGS-TRACE-246) use the Weil range q ≤ c_k p² only.
* The arb / mpmath interval arithmetic used for 0.18001 ≤ A is software. It is not registered as a theorem; it is reproduced in
  `computations/verification/lineK/integration_checks/lineK_checks.py`.
