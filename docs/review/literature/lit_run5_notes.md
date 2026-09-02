# Literature run 5 — retrieval notes (arXiv API only; websearch broken in this env)

Date: 2026-08-23. Scope: Q1-Q6 as posed. Method: `webfetch` on `https://export.arxiv.org/api/query?...` and on `arxiv.org/abs/<id>` pages. Budget used: 20 fetches.
Tags: [VERIFIED-STATEMENT] = abstract/page actually fetched and read. [LEAD] = seen in a feed/known bibliographically but exact statement not retrieved. [NOT FOUND] = searched, not found.

---

## Q1. Exponential sums over multiplicative subgroups H ⊆ F_p^× (Bourgain–Glibichuk–Konyagin type)

**[VERIFIED-STATEMENT]** E. Kowalski, *Exponential sums over small subgroups, revisited*, **arXiv:2401.04756** (v2, Jan 2024; math.NT; comment: "22 pages, survey paper").
Abstract (fetched): "This is an expository account of the proof of the theorem of Bourgain, Glibichuk and Konyagin which provides non-trivial bounds for exponential sums over very small multiplicative subgroups of prime finite fields."
What this establishes: a modern, citable expository reference for the BGK theorem sup_x |Σ_{h∈H} e_p(xh)| ≪ p^{-δ}|H| for |H| ≥ p^ε with δ = δ(ε) > 0; the survey's v2 explicitly adds references to work of Shkredov. Use this as the pointer to the precise form of BGK rather than citing from memory.

**[VERIFIED-STATEMENT]** D. di Benedetto, M. Z. Garaev, V. C. García, D. González-Sánchez, I. E. Shparlinski, C. A. Trujillo, *New estimates for exponential sums over multiplicative subgroups and intervals in prime fields*, **arXiv:2003.06165** (Mar 2020).
Abstract states exactly: for H ≤ F_p^× with |H| = H > p^{1/4},
  max_{(a,p)=1} |Σ_{x∈H} e_p(ax)| ≤ H^{1 − 31/2880 + o(1)},
which "improves a result of Bourgain and Garaev (2009)". Also: new bounds for double exponential sums with product nx, x ∈ H, n in a short interval N.
What this establishes: an explicit published power-saving exponent (31/2880 ≈ 0.01076) in the pure-subgroup sum regime |H| > p^{1/4}; relative saving H^{−31/2880} is uniform down to p^{1/4}.

**[VERIFIED-STATEMENT]** I. D. Shkredov, *On exponential sums over multiplicative subgroups of medium size*, **arXiv:1311.5726** (Nov 2013).
Abstract (fetched): new upper bounds for Σ_{g∈G} e_p(tg) for |G| ∈ [p^{c1}, p^{c2}], c1,c2 absolute constants close to 1/2; application: symmetric case G additive basis of order five if |G| > p^{1/2} log^{1/3} p; also a new bound for Heilbronn's sum. Exact exponent not retrieved (abstract only).

**[LEAD]** J. Bourgain, A. A. Glibichuk, S. V. Konyagin, *Estimates for the number of sums and products and for exponential sums in fields of prime order*, J. London Math. Soc. **73** (2006), 380–398. NOT on arXiv (not retrievable via this tooling); precise value of δ(ε) as printed there NOT VERIFIED in this run. The Kowalski survey arXiv:2401.04756 is the verified secondary source to consult for the exact statement/constants.

**[VERIFIED-STATEMENT]** P. Kurlberg, *Bounds on exponential sums over small multiplicative subgroups*, **arXiv:0705.4573** (2007, CRM-Clay proceedings): exposition of Bourgain–Chang arguments showing significant cancellation in sums over small subgroups.

Bottom line for Q1: BGK-type bound is real and standard; best EXPLICIT verified power savings found this run: H^{−31/2880+o(1)} for |H| > p^{1/4} (arXiv:2003.06165). The original BGK δ(ε) constant was not directly fetched.

## Q2. Additive energy E^+(H) of multiplicative subgroups

**[VERIFIED-STATEMENT]** B. Murphy, M. Rudnev, I. D. Shkredov, Yu. N. Shteinikov, *On the few products, many sums problem*, **arXiv:1712.00410** (Dec 2017).
Abstract states exactly: main result E(A) ≲_M |A|^{49/20} whenever |AA| ≤ M|A| (real/complex), and "These bounds, with M=1, also apply to multiplicative subgroups of F_p^×, whose order is O(√p)".
What this establishes: E^+(H) ≪ |H|^{49/20} (= |H|^{2.45}) for every subgroup H with |H| ≲ √p. This is the strongest EXPLICIT energy exponent actually verified in this run.

**[VERIFIED-STATEMENT (partial)]** I. D. Shkredov, *Some new inequalities in additive combinatorics*, **arXiv:1208.2344** (2012): abstract confirms "new upper bounds for the additive energy of multiplicative subgroups" and results connecting additive energy to "higher moments of convolutions" — the exact exponents were not retrieved (abstract only).

**[VERIFIED-STATEMENT (related)]** I. D. Shkredov, *On tripling constant of multiplicative subgroups*, **arXiv:1504.04522**: |3G| ≫ |G|^2/log|G| for |G| < p^{1/2}, and multiplicative energy of shifts E^*(G+x) ≪ |G|^2 log|G|. (Multiplicative-energy statement; useful input for moment estimates.)

**[VERIFIED-STATEMENT (related)]** T. Schoen, I. D. Shkredov, *On a question of Cochrane and Pinner concerning multiplicative subgroups*, **arXiv:1008.0723** (Quart. J. Math. 2011): for p^ε < |R| < p^{2/3−ε}: |R±R| > |R|^{3/2+δ(ε)}.

**[NOT FOUND / NOT VERIFIED]:**
- Any arXiv paper by Shkredov–Stevens specifically titled around "additive energy of subgroups": query `au:Stevens AND all:"multiplicative subgroups"` returned 0 hits; `all:"additive energy" AND ti:"subgroups"` returned 0 hits. The often-quoted Shkredov–Stevens attribution could not be confirmed on arXiv in this run.
- No verified published bound of shape E(H) ≪ |H|^{5/2−δ} or better than 49/20 with an explicit printed exponent was retrieved. Current-best status as of 2024–2026 remains UNVERIFIED here; treat any claim like |H|^{12/5+o(1)} or |H|^{5/2−c} as needing direct journal confirmation.

Higher moments T_d(H): no dedicated paper retrieved beyond Shkredov arXiv:1208.2344 ("higher moments of convolutions") and Macourt–Petridis–Shkredov–Shparlinski below. Exact T_d statements NOT verified this run.

## Q3. Sums Σ_{h∈H} e_p(a h + b h^{-1}) and rational-function phases over subgroups

**[VERIFIED-STATEMENT]** J. Bourgain, M. Z. Garaev, *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*, **arXiv:1211.4184** (2012, 70 pp.).
Abstract (fetched): new results on additive properties of I^{-1} = {x^{-1}: x ∈ I} for intervals I mod p; combined with multilinear exponential-sum estimates yields new bounds for incomplete multilinear Kloosterman sums.
What this establishes: the Bourgain–Garaev machinery behind cancellation in Kloosterman-type phases (ax + b/x); the specific subgroup version Σ_{h∈H} e_p(ah+bh^{-1}) with its exact constants/exponents was NOT printed in the abstract and not retrieved.

**[VERIFIED-STATEMENT]** J. Bourgain, M. Garaev, S. Konyagin, I. Shparlinski, *On Congruences with Products of Variables from Short Intervals and Applications*, **arXiv:1203.0017**; and *Multiplicative Congruences with Variables from Short Intervals*, **arXiv:1210.6429**: bounds on Π(x_i+s) ≡ Π(y_i+s) congruences; related double character sums. Abstracts only; no subgroup-phase statement.

**[VERIFIED-STATEMENT]** S. Macourt, G. Petridis, I. D. Shkredov, I. E. Shparlinski, *Bounds of Trilinear and Trinomial Exponential Sums*, **arXiv:2003.03493** (SIAM J. Discrete Math. 34 (2020), 2124–2136, DOI 10.1137/20M1325502): refined estimate for collinear triples in Cartesian products of multiplicative subgroups → stronger trilinear sums with variables in multiplicative subgroups. Closest verified tool for bilinear/trilinear phase sums over H.

**[VERIFIED-STATEMENT (context)]** S. Macourt, *Bounds On Exponential Sums With Quadrinomials*, **arXiv:1703.07066**: improved quadrilinear sums over multiplicative subgroups → quadrinomial sum bounds.

**[NOT FOUND]:** a theorem stated verbatim as "Σ_{h∈H} e_p(ah + bh^{-1}) ≪ ..." (twisted Kloosterman over a subgroup) with explicit exponent and full author list. Query `"twisted Kloosterman" AND "subgroups"` returned 0 hits. Best-known exact bound remains UNVERIFIED this run; the Bourgain–Garaev line above is where such bounds live (their IMRN/JLMS-era papers, partly off-arXiv).

## Q4. Monodromy / Goursat–Kolchin–Ribet; joint equidistribution; Gurevich–Hadani

**[VERIFIED-STATEMENT]** S. Gurevich, R. Hadani, *Proof of the Kurlberg-Rudnick Rate Conjecture*, **arXiv:math-ph/0404074** (v7, 2006).
Abstract (fetched): "we present a proof of the Hecke quantum unique ergodicity rate conjecture for the Berry-Hannay model", i.e., quantized cat maps on the 2-torus. v7 comment (fetched): adds proof that "the character sheaf of the Heisenberg-Weil representation is perverse, geometrically irreducible of pure weight 0", supplies invariant formulas for the character sheaf on an open set, and gives an alternative proof of the rate conjecture using those formulas.
What this establishes: polynomial-rate Hecke QUE (the Kurlberg–Rudnick rate conjecture) for cat maps, proved via monodromy methods (perversity + geometric irreducibility + purity of the Hecke character sheaf ⇒ Goursat-type rigidity). NOTE: the arXiv page shows NO journal-ref field; the commonly cited venue Annals of Mathematics 174 (2011) was NOT verifiable through arXiv metadata in this run ([LEAD] as to the journal data).

**[VERIFIED-STATEMENT]** S. Gurevich, R. Hadani, announcement *Proof of the Kurlberg-Rudnick Rate Conjecture* (4 pp.), **arXiv:math-ph/0510027**, accepted C. R. Acad. Sci. Paris; listed DOI 10.1063/1.2193112. Same claim, short announcement version.

**[VERIFIED-STATEMENT]** S. Gurevich, R. Hadani, *Bounds on certain Higher-Dimensional Exponential Sums via the Self-Reducibility of the Weil Representation*, **arXiv:math/0612765**: self-reducibility method → sharp form of the Hecke QUE theorem for GENERIC linear symplectomorphisms of the 2N-dimensional torus. (Generic case, distinct from the arithmetic/split-eigenvalue case.)

**[LEAD] (bibliographic, NOT fetched this run):**
- N. M. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Annals of Math. Studies 116, Princeton 1988 — the source of the monodromy machinery (big monodromy + Goursat–Kolchin–Ribet criterion for joint equidistribution of Frobenius traces).
- N. M. Katz, *Sums of Betti Numbers in Arbitrary Characteristic* (and *Roos blocks...*) — sheaf-conductor technology controlling the "large monodromy group" hypothesis.
- É. Fouvry, E. Kowalski, P. Michel — algebraic trace function papers (e.g. *Algebraic trace functions over the primes*, Duke; *Algebraic twists of modular forms and Hecke orbits*, GAFA) and their surveys: the working toolkit (Pólya-Vinogradov range, ℓ-adic estimates) that would be applied to families of twisted Jacobi sums K_{χχ'}(a,b).
None of these four items had a statement fetched; they are cited as standard references only.

What JOINT equidistribution needs (per the verified G–H workflow above, which is the same architecture): (i) the family realized as Frobenius-characteristic functions of a compatible family/lisse sheaf; (ii) geometric irreducibility + purity (verified in G–H v7 comment for the Heisenberg–Weil character sheaf); (iii) BIG monodromy group (Goursat–Kolchin–Ribet) so the monodromy group surjects onto the expected compact quotient — this is the step that must be redone for a family indexed by characters χ of the cyclic group ⟨α⟩.

## Q5. Kurlberg–Rosenzweig–Rudnick, short windows

**[VERIFIED-STATEMENT]** P. Kurlberg, L. Rosenzweig, Z. Rudnick, *Matrix elements for the quantum cat map: Fluctuations in short windows*, **arXiv:math/0701685** (v2 Jul 2007; math.NT × math-ph; 18 pp.).
Abstract (fetched): "We consider the sum of matrix coefficients corresponding to eigenstates whose eigenphases lie in a randomly chosen window, assuming that the length of the window shrinks with Planck's constant. We show that if the length of the window is smaller than the square root of Planck's constant, but larger than the separation between distinct eigenphases, then the variance of this sum is proportional to the length of the window, with a proportionality constant which coincides with the variance of the individual matrix elements corresponding to Hecke eigenfunctions."
What this establishes: linear-in-window-length variance law (white-noise/Poisson-like scaling of matrix elements across eigenphases) inside shrinking spectral windows — the natural benchmark against which our fine-scale statistics inside arithmetically degenerate eigenspaces must be compared (there the degeneracy k can exceed √ħ-scale windows).

## Q6. 2024–2026 deterministic-map level spacing / SFF beyond the known list

Searches executed (arXiv API, all fields):
- `"level spacing" AND "deterministic"` → 16 hits, ALL about localization/fractal potentials/photonics/quasiperiodic systems; NONE about cat/baker/kicked maps or arithmetic degeneracies.
- `"spectral form factor" AND ("cat map" OR "baker map" OR "kicked rotator")` → exactly 3 total hits:
  **[VERIFIED-STATEMENT (abstract)]** S. Moudgalya, T. Devakul, C. W. von Keyserlingk, S. L. Sondhi, *Operator Spreading in Quantum Maps*, **arXiv:1808.04889**, PRB 99, 094312 (2019): perturbed Arnold cat map; timescales of operator spreading related to quasi-energy spectrum via spectral form factor. Not a WD proof.
  **[VERIFIED-STATEMENT (abstract)]** T. Dittrich, L. A. Pachon, *Time-domain scars: resolving the spectral form factor in phase space*, **arXiv:0811.3017**, PRL 102, 150401 (2009): SFF resolved via phase-space return probabilities; numerics for quantum cat map. Diagonal-only physics.
  **[VERIFIED-STATEMENT (abstract)]** S. Keppeler, J. Marklof, F. Mezzadri, *Quantum cat maps with spin 1/2*, **nlin/0012012**, Nonlinearity 14 (2001) 719–738: semiclassical trace formula; DIAGONAL approximation of the spectral form factor for small arguments agrees with CSE (symplectic RMT) prediction. Off-diagonal never controlled.
- `"Wigner-Dyson" AND ("quantum map" OR "cat map" OR "baker map")` → 1 hit: O. Giraud, B. Georgeot, *Intermediate quantum maps for quantum computation*, quant-ph/0504230, PRA 72, 042312 (2005): maps with statistics INTERMEDIATE between Poisson and Wigner-Dyson (i.e., explicitly not WD).

**[NOT FOUND]:** No publication dated 2024–2026 proving Wigner-Dyson nearest-neighbor statistics or full (off-diagonal) spectral form factor asymptotics for ANY deterministic quantum chaotic map (cat, baker, kicked rotator) or inside arithmetic degeneracies surfaced under these queries. Nothing new to add beyond the user-supplied list (Pluhář–Weidenmüller PRL 112 (2014); Bertini–Kos–Prosen dual-unitary circuits with disorder; Kurlberg, Ann. H. Poincaré 23 (2022) β≈4 point scatterers; Adhikari–Lemm–Yau semicircle). The three older cat-map SFF items above are diagonal-approximation results only — consistent with the project's premise that fine-scale WD inside arithmetic degeneracies is open.

---

## Explicit list of what was NOT verified
1. Original BGK JLMS 2006 printed δ(ε) (paper off-arXiv); only the survey pointer arXiv:2401.04756 verified.
2. Journal-ref for di Benedetto et al. arXiv:2003.06165 (abstract verified; venue not shown in API output).
3. Existence/exponent of a "Shkredov–Stevens" subgroup-energy paper; current world-best exponent for E^+(H) as of 2024–2026 (best VERIFIED explicit: 49/20, MRSS arXiv:1712.00410, valid |H| ≲ √p).
4. Higher-moment bounds T_d(H) exact statements (only pointers: arXiv:1208.2344, arXiv:2003.03493).
5. An exact printed bound for Σ_{h∈H} e_p(ah + bh^{-1}) over subgroups (closest verified: Bourgain–Garaev arXiv:1211.4184 machinery).
6. Katz books and FKM survey papers: bibliographic [LEAD] only, no fetched statements.
7. Annals-of-Mathematics 174 (2011) journal data for Gurevich–Hadani rate conjecture paper (content verified from arXiv; venue field absent from arXiv metadata).
8. Any 2024–2026 deterministic-map WD/SFF proof (concluded: none exists under the queries tried).
