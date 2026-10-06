# Curated publication copy of the accepted independent review

Editorial paths and spacing have been normalized only. The byte-for-byte original and its SHA-256 remain in record/history/2026/actual_commutant_20261006/historical/actual_family_review_original.md and the original manifest. Commands below point to the portable maintained derivatives; their new execution receipts are separate. No original execution is relabeled.

# Independent audit: actual unramified higher-seven-primary commutant

## Primary verdict

**Proved as written, for every odd N with 49|N and 5∤N, using exact finite-polynomial certificates as part of the proof.** The actual pair (A_N,M_N), not merely its upper-bond truncation over C, has scalar complex common commutant on this family.

All proof-dependent algebra, the complete norm factorization, and every irreducibility identity were independently checked to completion, including degrees 246 and 366. Acceptance does not depend on an unfinished author verification log. This is an independently reviewed project proof with computer-assisted exact polynomial inputs, not an external referee or formal-kernel certificate.

The conclusion excludes 5|N and 7∥N. It does not assert spectral simplicity in this family, an all-odd-N commutant theorem, quantitative spectral gaps, TRACE-005 or microscopic BGS.

## Source-bound scope

The audited candidate is `record/history/2026/actual_commutant_20261006/unramified_actual_commutant_reviewed_v1.md`, frozen in this audit's `the preserved source-data package` directory before execution. The exact polynomial JSON inputs and actual-base result were frozen alongside it. `actual_review_manifest.json` records all source and independent-script/output hashes. No author source or canonical file was changed.

The earlier actual_mod5_bridge.md describes its earlier open rank-six route. The new candidate supplies a different sufficient two-row argument; this review does not silently treat the earlier open assertion as proved. The previously reviewed Casoratian-unit and tail lemmas are explicit dependencies.

## Dependency graph and disposition

1. Actual integral1000A and raw G reduce at the Gaussian prime i→2: **passed**.
2. All upper bonds remain units and both matrices are conjugated by the same D: **passed**.
3. Last-row equations diagonalize C0 in the weighted row basis: **passed**.
4. Actual last-bond relation identifies the penultimate block; its equation gives the two bounded sufficient conditions B1,B2: **passed**.
5. Polynomial dictionary for y and K00: **passed by derivation, full polynomial identities, and direct field evaluations**.
6. Complete factorizations, product identities, Rabin irreducibility and order-degree exclusion: **passed, fully executed**.
7. Tail elimination for L≥21 and exact actual-residue N49 base: **passed**.
8. Nonzero actual commutator-rank minor lifts to characteristic zero: **passed**.

## 1. Actual reduction and all unit conditions

The exact generator has diagonal terms multiplied by 1000,100,10 and 100 after passing to1000A. Trigonometric denominators use only 2 and i, both units at 5. Hence its diagonal reduces to zero. With i→2, the lower coefficient−3+4i becomes0, while upper coefficient−3−4i becomes4. Thus the reduction is exactly the weighted upper generator B in the same position convention.

Since5∤N, a primitive Nth root q reduces with exact orderN. For an internal bond at depthu−1, 1≤u<L, its root coordinate is q^u w^j, with w=q^L. In the Laurent identity for r, q^(7u)≠1 because N=7L and u is strictly between0 and L. The other factor1+q^u w^j is nonzero because its root has odd order. Therefore every internal bond is nonzero in K and every diagonal entry of the recursively defined D, and its inverse, is a unit. This is precisely where the exclusion5|N matters.

The raw G is integral and is an invertible Fourier-type matrix over K: q is primitive and 5∤N. Its omitted scalar√N is irrelevant to common commutants. Both reduced matrices are conjugated by exactly the same D. No archimedean surrogate theorem is substituted for this reduction.

For V, all 1+q^u w^j denominators are units; the seventh-root Fourier evaluation matrix is invertible since5≠7. The previously audited polynomial P is nonzero at every root of order divisible by 49, by its exact Frobenius-gcd certificate. For Q, q^7+1≠0 by odd order, and every1+wq^(−1)w^j is likewise nonzero. These checks cover all denominators in the bounded argument.

## 2. Reconstruction of the two-row lemma

Applying the dual row to the independent u_s columns in the last-row equations annihilates every earlier output column, so v_s^T C0=λ_s v_s^T. Rescaling those rows to the normalized V does not change λ_s. Its row0 has scalar normalization1. Thus VC0V^(−1)=Λ is diagonal, and the s=0 equation gives C0u0=λ0u0. Accordingly h=Vu0 satisfies Λh=λ0h.

For the penultimate row, the raw left Fourier frequency changes from4 to3, while the right frequency changes from3 to1. At the last bond, z=q^(L−1)w^j=wq^(−1)w^j and

b_(L−1,j)=constant·w^(−j)(1+wq^(−1)w^j)^2.

Since D_(L−1)=D_(L−2)/b_(L−1), the penultimate inverse gauge contributes b_(L−1)^(−1). Its factorw^j cancels the left-frequency decrement. Therefore the actual block is exactly a nonzero scalar multiple of Q u0 v0^T R, with R=diag(w^(−2j)). This is a consequential use of the actual adjacent-depth gauge relation, not an arbitrary endpoint assumption.

In the V basis, v0^T V^(−1)=e0^T. Therefore C1E0 has only column 0, whereas F0 becomes a nonzero scalar multiple of xy with x=VQu0 and y=f1^T V^(−1). Every columnj≠0 gives (λ_i−λ_j)x_i y_j=0. There is no need to discard C1 or assume C0 separately commutes with all blocks.

If y1,...,y6 are nonzero, a nonzero component of x equates λ1,...,λ6. If λ0 differs, Λh=λ0h forces h to be a nonzero multiple ofe0. Then x0 is that same nonzero multiple of (VQV^(−1))00. Its nonvanishing contradicts the off-column 0 equation. Thus B1 and B2 indeed force scalar C0.

## 3. Polynomial dictionary: independently reconstructed and checked

Let H_j=∏_(u=1)^6(1+q^u w^j)^2 and T=diag(w^(3j)/H_j). With F the seven-point evaluation matrix, V=CFT. Hence

y=f1^T T^(−1)F^(−1)C^(−1).

The evaluation data f1^T T^(−1) are (w^j)^(1−3)H_j=(w^j)^5 H_j, giving precisely the stated coefficient row r modulo z^7−1. Independently expanded coefficient recurrences verified all seven exact identities y_num C=den·r over Z[q], not only evaluations at one N.

For K00, the row0 of V is f3^T. Removing T from f3^TQ leaves H_j/(1+wq^(−1)w^j)^2. In z^7=1 and w^7=1, multiplying the seven-term alternating geometric sum by 1+wq^(−1)z gives1+q^(−7). Squaring gives exactly

(1+wq^(−1)z)^(−2)=q²[Σ_(k=0)^6(−w)^k q^(6−k)z^k]^2/(q^7+1)^2.

The independent builder retained both summation indices when squaring, rather than reusing the author's triangular-coefficient implementation. All six w-coefficient numerator identities were checked modulo 5. Both saved denominators were verified to be associates of P modulo 5. Thus their nonvanishing follows from the audited P certificate.

For a separate direct check, actual_field_check.py constructed F5[q]/Φ49 using exact polynomial remainder tables, built V and its inverse directly, and compared y and K00 with the saved polynomial numerators for all six primitive seventh roots w=q^(7k), k=1,...,6. Every equality and required nonzero value passed. The actual choicew=q^7 is included. These evaluations corroborate the dictionary; the full symbolic identities establish it uniformly.

## 4. Independent norm and complete factor certification

The author computes Res_w(K,Φ7). This audit instead built the6×6 multiplication-by-K matrix on basis 1,w,...,w5 of F5[q,w]/(Φ7), and computed its determinant. All829 coefficients match the frozen degree 828 norm exactly. Thus the factor data are tied to the correct K numerator, not merely to an unrelated degree 828 polynomial.

actual_factor_check.py independently verified:

- each y numerator's entire factor multiplication, including unit and multiplicities;
- the entire norm factor multiplication up to its explicitly harmless nonzero leading unit;
- every factor's irreducibility by Frobenius and proper-divisor Rabin tests;
- that no irreducible factor degree is divisible by 42.

The independent verifier uses NumPy integer coefficient arithmetic and modular polynomial division/Frobenius/gcd routines, rather than the author's SymPy-power Rabin implementation. Irreducibility is not inferred from a factorization routine label. For a degree d factor f it checked X^(5^d)=X modulo f and gcd(f,X^(5^(d/p))−X)=1 for every prime p dividing d. All checks passed, including d=246 and d=366. Integer intermediates are safely bounded because coefficients are reduced modulo 5 at every polynomial operation; no floating arithmetic is used.

The norm factors have degrees and multiplicities1^24,6^6,36,54,66,246,366. Their weighted degrees sum to828, and the full multiplication, not merely this degree sum, passed. The y factor data similarly reproduce their complete polynomials.

## 5. Uniform degree exclusion, actual w and arbitrary N

Exact modular exponent checks give ord49(5)=42:5^42≡1 mod49, while exponents21,14,6 do not give1. If an elementα in an algebraic closure of F5 has multiplicative order divisible by 49, its minimal-polynomial degree d satisfies49|5^d−1, hence42|d. A polynomial vanishing atα must contain its irreducible minimal polynomial as a factor.

The complete checked lists for every y_j numerator, j=1,...,6, have no such degree. Thus B1 holds uniformly. The complete norm list also has no such degree, so N(α)≠0. Nonzero resultant means K(α,w)≠0 for every root ofΦ7, hence in particular for the actual paired rootw=q^(N/7). Treating w as independent in the norm is a stronger exclusion, not a mistaken loss of their actual relation. This proves B2 uniformly for unbounded N and arbitrarily high v7(N); it is not extrapolation from finite dimensions.

## 6. Tails, actual residue N49 base and rank lift

For L≥21, the already audited minimal-tail dichotomy is valid over K: the first seven weighted rows are independent by the Casoratian-unit result, and seven consecutive bottom right rows are independent Fourier rows. All nonzero scalar factors stay nonzero. Thus scalar C0 kills all higher Cd.

For N49, actual_field_check.py independently constructs the actual reduced B from the Laurent formula for r in position order and the exact quadratic metaplectic G. Its field reduction uses a table of exact polynomial remainders, not the author's reshape reduction. Φ49 is irreducible because its degreeφ(49)=42 equals ord49(5). Exactly seven bonds vanish, leaving42 internal bonds. For T=B+G and e0, the independently assembled Krylov matrix has rank 49, and the commutator-column matrix has rank 48. These reproduce the actual residue certificate without borrowing the earlier characteristic-zero weighted-surrogate rank test.

The cyclic argument is exact: every X commuting with T is a polynomialp(T) of degree≤48. If X also commutes with B, then [p(T),B]e0=0. The first column is zero and the map has rank 48, so only the constant coefficient survives. Therefore the actual residue common commutant is scalar.

For every N in the stated family, the full commutator map of the reduction has rankN²−1. Its nonzero minor lifts from the prime of the integral cyclotomic coefficient ring to a nonzero characteristic-zero minor. The exact scalar identity supplies the opposite rank bound. Hence the actual complex kernel is precisely C I. This is one rank lower-bound argument; it is not a difference-of-ranks projection inference or an attempted lift of an individual idempotent.

## 7. Remaining scope and editorial note

No mathematical gap was found in this exact family after the complete certificates finished. The branches5|N and 7∥N remain unproved by this route. The former can lose root order and internal units; the latter lacks the rank-one endpoint formula used here. Neither is included by continuity or by the successful finite examples.

At review time the author's slower verify_bounded_factors.log had not yet printed its final degree 366 completion. This audit supplies a separately completed exact certificate, so its acceptance is evidence-based rather than anticipatory. The author may still preserve their own final artifact for provenance. A promotion should cite the completed independent results as well as the builders and should reconcile the earlier bridge note's historical open wording without erasing it.

## Reproduction

OPENBLAS_NUM_THREADS=1 python computations/verification/actual_factor_check.py
OPENBLAS_NUM_THREADS=1 python computations/verification/actual_algebra_check.py
OPENBLAS_NUM_THREADS=1 python computations/verification/actual_field_check.py

Completed outputs are actual_factor_results.json, actual_algebra_results.json, actual_field_results.json, the corresponding logs, and actual_review_manifest.json. Source inputs are frozen in the preserved source-data package. No canonical changes were made.

### Final certificate-locator reconciliation

After the checks above finished, the author supplied bounded_factor_certificates_fast.json. Its seven complete records, degrees, multiplicities, proper-divisor checks and Frobenius identities match this audit’s independent results. The fast record was frozen in the preserved source-data package. The candidate’s mathematical statement passes, but its pointer to bounded_factor_certificates.json should be changed to the completed fast filename (or wait until the original file actually exists). This is an evidence-locator correction, not a missing mathematical certificate. The candidate hash matches47b2692f034a23888d4223e73120a685609a6ca58c2a983293310bc735e42d4f.
