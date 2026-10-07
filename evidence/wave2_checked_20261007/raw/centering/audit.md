# Independent audit of the compact-stratum centering candidate

## Normalized claim and primary verdict

For every odd N≥3, every labelled mixed circle/disk sector X_B and every integrable ordinary coefficient function g, the unique conformal-center map gives the exact finite-N integral with gauge factor

Δ(y)(1−|p|²)^(2N−|B|−2) / [∏_(i∉B)|1+p̄y_i|⁴ ∏_(i∈B)|1+p̄y_i|²],

using ordinary d²p and the Euclidean two-dimensional delta of Σy_i against the original normalized circle/disk product measures.

**Primary verdict: proved as written.** The candidate's almost-everywhere restriction and N=1/N=2 exclusions are correct. The full proof, precise induced delta measure, and independent normalization controls are supplied in `compact_stratum_centering.md`. This audit does not change the accepted compact projector's domain or its coefficient conventions.

## Independence and exact authority

The target is the frozen file `evidence/research_checkpoint_20261007/raw/bgs_astra_corrected_integral/frontier/centering_candidate.md`, copied without change to `inputs/centering_candidate.md`. Exact source and dependency hashes are in `input_manifest.json`, bound to the supplied 3930-file checked source snapshot, manifest SHA-256 d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba.

The current claim ledger explicitly leaves the candidate unpromoted. The ordinary source identity is accepted through BGS-TRACE-023 and its separate internal review; body coercivity is BGS-FM-030. Original proof files retain historical author-status text, so the current ledger and checked review records control their status.

The present worker reconstructed the potential, fixed-z derivative, mixed-dimensional coarea factor and global identity directly. Its checker was written independently from ordinary real-coordinate derivatives and elementary integrals; no source author's checker was imported. This establishes an independent internal audit of the candidate, not external referee certification or formalization. The stronger odd-N determinant bound and quantitative complete-source cutoff estimates are new author results in this packet and, until separately reviewed, have only self-review plus their stated exact finite controls.

## Dependency graph

- Elementary Möbius algebra → proper stable potential and geodesic Hessian → unique center and smooth inverse.
- Product circle/disk tangent metric → J_B=½√((2N−k)²−|Σ_B y_i²|²).
- Fixed-z derivative → gauge determinant Δ/(1−|p|²)².
- Fixed-center coordinate derivatives → circle/disk Jacobians → exact centered integral.
- Accepted completed compact projector → bounded finite coefficient functions → application to every signed source sector.
- New cap lemma + product probability bound → quantitative actual-source cutoff error.
- New finite algebra norm estimate → explicit coefficient majorant, retaining all N dependence.

The body-coercivity theorem is a compatibility/boundary check, not an input to the centered identity or cutoff theorem. No new external theorem leaf is required for the geometric argument. The accepted source result retains its authenticated Zirnbauer dependency; that already-accepted kernel is not re-labelled newly externally verified here.

## Obligation matrix

| Obligation | Verdict | Evidence |
|---|---|---|
| Odd-N domain and labelled circle/disk support | Passed | Proof §§1–2 |
| Boundary properness including tangential approaches | Passed | Finite-neighborhood lower bounds, §2 |
| Exact multiplicity threshold and uniqueness | Passed | Projection obstruction and strict geodesic convexity, §2 |
| Null excluded set before centering | Passed | Finite union of circle-coordinate equality sets, §1 |
| Mixed real dimension | Passed | 2N−k−2 with regular sum map, §§1,4 |
| Uniform odd-N nondegeneracy | Passed as new author proof | Δ≥2N−1, §3; vertex controls through N=31 |
| Distinction between coarea J_B and gauge Δ | Passed | Direct tangent matrix and fixed-z derivative, §4 |
| Euclidean delta and π normalization | Passed | §§4–5; N=1, N=2 and N=3 exact mass controls |
| Rotation and labelling multiplicity | Passed | Fixed m_p convention; two N=3 equilateral orientations |
| Global integral and noncompact center domain | Passed | Unique-zero delta identity, exhaustion and L¹ extension, §5 |
| N=1 and N=2 exceptional sectors | Passed | Exact geometric classification, §2 |
| Extraction before centering and retained sources | Passed | Accepted source coefficients carried literally, §6 |
| Actual complete signed-source cutoff estimate | Passed as new author proof | Cap lemma, (12)–(13), §§7–8 |
| Fully explicit fixed-N coefficient bound | Passed as new author proof | BB pivot in a finite coefficient algebra, (16)–(17) |
| Compatibility with exact boundary correction | Passed within scope | No compact sector omitted; zero-source boundary control |
| Super-Berezinian or positive full supermeasure | Out of scope | Explicitly not asserted |
| Uniform microscopic/normalized tail or CUE identification | Not addressed | Coefficient growth and signed cancellation remain open |
| BGS conclusion | Out of scope/open | No change to TRACE-005 |

## Decisive controls

The reproducible command is

python checks/verify_centering.py

Run from this packet or with its absolute script path. `checks/results.json` and `checks/run.log` record the completed run, Python/SymPy versions and all 20 successful checks. Arithmetic is exact rational/algebraic or symbolic; no floating numerical claim is used.

The strongest normalization controls are:

1. N=2 all-disk total mass telescopes to 1 using 1/(2n+1)²−1/(2n+3)².
2. N=3 all-circle center density is exactly 3√3/[π²(1+|p|²+|p|⁴)] and integrates to 1.
3. Direct real Jacobians agree in N=3 sectors k=0,1,2,3, at p=0 and p=1/5+i/7.
4. The N=3 actual completed zero-source observable loses exactly (2√3/π)ε+O(ε²) under |p|≤1−ε. Thus the geometric cutoff is neither an exact source-preserving normalization nor a zero-error deletion.

## Strongest safe conclusion and next missing implication

The ordinary candidate is valid for every compact sector at odd N≥3, and the full signed source now has an exact centered representation plus a genuine effective fixed-N center-cutoff bound. These results do not make the source a positive superintegral and do not permit inserting the strict-interior body inequality into its exact circle-supported sectors.

The missing implication is a dimension-uniform estimate for the complete signed, source-differentiated coefficient combination, including boundary terms, at ab=e^(−2s/N), sufficient for the N^(−2)-normalized pair observable. The cheapest next useful check is the boundary/body worker's coefficient-level synthesis against the exact formulas here. Re-deriving the ordinary gauge or relying on its positivity cannot close that estimate.

No source edits, ledger events, publication, priority claim, external review, or analytic formalization were performed by this worker.
